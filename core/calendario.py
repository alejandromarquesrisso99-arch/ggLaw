"""Días inhábiles a efectos del cómputo de plazos administrativos.

Fundamento: art. 30.2, 30.6 y 30.7 de la Ley 39/2015 (knowledge/ley-39-2015.md).
Los datos oficiales viven en calendars/<territorio>/<año>.yaml y cada festivo cita su fuente.
"""

from __future__ import annotations

from collections.abc import Iterable
from datetime import date
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

DEFAULT_CALENDARS_DIR = Path(__file__).resolve().parent.parent / "calendars"
TERRITORIES_FILE = "territorios.yaml"


class CalendarNotAvailableError(LookupError):
    """No hay datos oficiales para el territorio o el año pedido."""


class CalendarDataError(ValueError):
    """Los datos de calendario son incoherentes o no cumplen el esquema."""


class Calendar:
    """Días inhábiles de uno o varios territorios para los años con datos oficiales.

    Sábados y domingos son siempre inhábiles (art. 30.2). Para un año sin datos no se
    responde nada: nunca se da por hecho que un año no tiene festivos.
    """

    def __init__(self, holidays: Iterable[date], years: Iterable[int]) -> None:
        self._years = frozenset(years)
        self._holidays = frozenset(holidays)
        if not self._years:
            raise CalendarDataError("Un calendario necesita al menos un año con datos.")
        outside = sorted(day for day in self._holidays if day.year not in self._years)
        if outside:
            raise CalendarDataError(f"Festivos fuera de los años cubiertos: {outside}")

    @property
    def years(self) -> frozenset[int]:
        return self._years

    @property
    def holidays(self) -> frozenset[date]:
        return self._holidays

    def is_business_day(self, day: date) -> bool:
        if day.year not in self._years:
            raise CalendarNotAvailableError(
                f"No hay calendario oficial de días inhábiles para {day.year}."
            )
        return day.weekday() < 5 and day not in self._holidays

    def merge(self, *others: Calendar) -> Calendar:
        """Combina calendarios: un día inhábil en cualquiera de ellos es inhábil (art. 30.6).

        Solo quedan cubiertos los años que todos cubren.
        """
        years = self._years.intersection(*(other.years for other in others))
        if not years:
            raise CalendarNotAvailableError("Los calendarios no tienen ningún año en común.")
        holidays = self._holidays.union(*(other.holidays for other in others))
        return Calendar((day for day in holidays if day.year in years), years)


class _Source(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str
    url: str
    consultado: date


class _Holiday(BaseModel):
    model_config = ConfigDict(extra="forbid")

    fecha: date
    nombre: str
    fuente: str


class _CalendarFile(BaseModel):
    model_config = ConfigDict(extra="forbid")

    estado: Literal["borrador", "revisado", "validado_abogado"]
    fuentes: list[_Source]
    # Un año sin festivos declarados es casi seguro un fichero a medias: se rechaza.
    festivos: list[_Holiday] = Field(min_length=1)

    @model_validator(mode="after")
    def _holidays_cite_declared_sources(self) -> _CalendarFile:
        declared = {source.id for source in self.fuentes}
        for holiday in self.festivos:
            if holiday.fuente not in declared:
                raise ValueError(f"{holiday.fecha}: fuente no declarada «{holiday.fuente}»")
        return self


class _Territory(BaseModel):
    model_config = ConfigDict(extra="forbid")

    padre: str | None


def _read_yaml(path: Path) -> object:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as error:
        raise CalendarDataError(f"{path}: YAML no válido: {error}") from error


def _load_territories(base_dir: Path) -> dict[str, _Territory]:
    path = base_dir / TERRITORIES_FILE
    raw = _read_yaml(path)
    if not isinstance(raw, dict):
        raise CalendarDataError(f"{path}: se esperaba un diccionario de territorios.")
    try:
        return {str(name): _Territory.model_validate(data) for name, data in raw.items()}
    except ValidationError as error:
        raise CalendarDataError(f"{path}: {error}") from error


def _load_territory_years(directory: Path) -> dict[int, frozenset[date]]:
    years: dict[int, frozenset[date]] = {}
    for path in sorted(directory.glob("*.yaml")):
        if not path.stem.isdigit():
            raise CalendarDataError(f"{path}: el nombre del fichero debe ser el año (AAAA.yaml).")
        year = int(path.stem)
        try:
            data = _CalendarFile.model_validate(_read_yaml(path))
        except ValidationError as error:
            raise CalendarDataError(f"{path}: {error}") from error
        wrong_year = [h.fecha for h in data.festivos if h.fecha.year != year]
        if wrong_year:
            raise CalendarDataError(f"{path}: festivos que no son de {year}: {wrong_year}")
        years[year] = frozenset(h.fecha for h in data.festivos)
    return years


def load_calendar(territory: str, base_dir: Path = DEFAULT_CALENDARS_DIR) -> Calendar:
    """Calendario de un territorio con los festivos de todos sus ámbitos superiores.

    Un año solo queda cubierto si todos los niveles (p. ej. nacional, autonómico y local)
    tienen datos publicados para él.
    """
    territories = _load_territories(base_dir)
    chain: list[str] = []
    current: str | None = territory
    while current is not None:
        if current not in territories:
            raise CalendarNotAvailableError(f"No hay calendario para el territorio «{current}».")
        if current in chain:
            raise CalendarDataError(f"{base_dir / TERRITORIES_FILE}: ciclo en «{current}».")
        chain.append(current)
        current = territories[current].padre

    levels = [_load_territory_years(base_dir / name) for name in chain]
    years = set.intersection(*(set(level) for level in levels))
    if not years:
        raise CalendarNotAvailableError(
            f"No hay ningún año con datos completos para «{territory}» ({' + '.join(chain)})."
        )
    holidays = {day for level in levels for year in years for day in level[year]}
    return Calendar(holidays, years)
