"""Tests de core/calendario.py: días inhábiles a efectos del cómputo de plazos.

Fundamento (Ley 39/2015; resumen propio, no transcripción): art. 30.2 (sábados, domingos y
festivos son inhábiles), 30.6 (combinación de calendarios de residencia y sede) y 30.7
(calendarios oficiales de días inhábiles).

Texto literal y fuente: knowledge/ley-39-2015.md.

Los festivos y ficheros YAML de estos tests son SINTÉTICOS y no son datos oficiales.
"""

from collections.abc import Callable
from datetime import date
from pathlib import Path
from typing import Any

import pytest
import yaml

from core.calendario import (
    DEFAULT_CALENDARS_DIR,
    Calendar,
    CalendarDataError,
    CalendarNotAvailableError,
    load_calendar,
)


class TestCalendar:
    def test_weekends_are_non_business_days_without_declaring_them(self) -> None:
        calendar = Calendar(holidays=(), years=[2026])
        assert calendar.is_business_day(date(2026, 10, 2))  # viernes
        assert not calendar.is_business_day(date(2026, 10, 3))  # sábado
        assert not calendar.is_business_day(date(2026, 10, 4))  # domingo
        assert calendar.is_business_day(date(2026, 10, 5))  # lunes

    def test_declared_holiday_is_a_non_business_day(self) -> None:
        calendar = Calendar(holidays=[date(2026, 10, 12)], years=[2026])
        assert not calendar.is_business_day(date(2026, 10, 12))
        assert calendar.is_business_day(date(2026, 10, 13))

    @pytest.mark.parametrize(
        "day",
        [date(2027, 1, 4), date(2027, 1, 2), date(2025, 12, 31)],
    )
    def test_uncovered_year_raises(self, day: date) -> None:
        """Sin datos oficiales de un año no se responde nada, ni siquiera para un sábado."""
        calendar = Calendar(holidays=(), years=[2026])
        with pytest.raises(CalendarNotAvailableError):
            calendar.is_business_day(day)

    def test_holiday_outside_covered_years_is_rejected(self) -> None:
        with pytest.raises(CalendarDataError):
            Calendar(holidays=[date(2027, 1, 1)], years=[2026])

    def test_needs_at_least_one_year(self) -> None:
        with pytest.raises(CalendarDataError):
            Calendar(holidays=(), years=[])


class TestMerge:
    """Art. 30.6: se combinan los calendarios de la residencia y de la sede del órgano."""

    def test_no_common_year_raises(self) -> None:
        with pytest.raises(CalendarNotAvailableError):
            Calendar(holidays=(), years=[2026]).merge(Calendar(holidays=(), years=[2027]))

    def test_union_of_holidays_and_intersection_of_years(self) -> None:
        residence = Calendar(holidays=[date(2026, 1, 20), date(2027, 1, 20)], years=[2026, 2027])
        seat = Calendar(holidays=[date(2026, 5, 15)], years=[2026])

        merged = residence.merge(seat)

        assert merged.years == {2026}
        assert not merged.is_business_day(date(2026, 1, 20))
        assert not merged.is_business_day(date(2026, 5, 15))
        with pytest.raises(CalendarNotAvailableError):
            merged.is_business_day(date(2027, 3, 1))


# Formato de un fichero calendars/<territorio>/<año>.yaml.
EXAMPLE_FILE = """\
estado: borrador
fuentes:
  - id: fuente-prueba
    url: https://example.org/fuente-prueba
    consultado: 2026-09-23
festivos:
  - fecha: 2026-01-20
    nombre: Festivo de prueba
    fuente: fuente-prueba
"""

TERRITORIES_FILE = """\
nacional:
  padre: null
illes_balears:
  padre: nacional
palma:
  padre: illes_balears
"""


def calendar_data(holiday: date) -> dict[str, Any]:
    data: dict[str, Any] = yaml.safe_load(EXAMPLE_FILE)
    data["festivos"][0]["fecha"] = holiday
    return data


def write_calendar(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, allow_unicode=True), encoding="utf-8")


@pytest.fixture
def calendars_dir(tmp_path: Path) -> Path:
    """Nacional e Illes Balears con datos de 2026 y 2027; Palma solo de 2026."""
    (tmp_path / "territorios.yaml").write_text(TERRITORIES_FILE, encoding="utf-8")
    write_calendar(tmp_path / "nacional" / "2026.yaml", calendar_data(date(2026, 10, 12)))
    write_calendar(tmp_path / "nacional" / "2027.yaml", calendar_data(date(2027, 10, 12)))
    write_calendar(tmp_path / "illes_balears" / "2026.yaml", calendar_data(date(2026, 3, 2)))
    write_calendar(tmp_path / "illes_balears" / "2027.yaml", calendar_data(date(2027, 3, 1)))
    write_calendar(tmp_path / "palma" / "2026.yaml", calendar_data(date(2026, 1, 20)))
    return tmp_path


def holiday_from_another_year(data: dict[str, Any]) -> None:
    data["festivos"][0]["fecha"] = date(2027, 1, 20)


def undeclared_source(data: dict[str, Any]) -> None:
    data["festivos"][0]["fuente"] = "otra-fuente"


def holiday_without_source(data: dict[str, Any]) -> None:
    del data["festivos"][0]["fuente"]


def source_without_url(data: dict[str, Any]) -> None:
    del data["fuentes"][0]["url"]


def unknown_status(data: dict[str, Any]) -> None:
    data["estado"] = "aprobado"


def no_holidays(data: dict[str, Any]) -> None:
    data["festivos"] = []


class TestLoadCalendar:
    def test_local_calendar_includes_regional_and_national_holidays(
        self, calendars_dir: Path
    ) -> None:
        calendar = load_calendar("palma", calendars_dir)
        for holiday in (date(2026, 10, 12), date(2026, 3, 2), date(2026, 1, 20)):
            assert not calendar.is_business_day(holiday)

    def test_regional_calendar_excludes_local_holidays(self, calendars_dir: Path) -> None:
        calendar = load_calendar("illes_balears", calendars_dir)
        assert not calendar.is_business_day(date(2026, 3, 2))
        assert calendar.is_business_day(date(2026, 1, 20))

    def test_year_is_covered_only_if_every_level_has_data(self, calendars_dir: Path) -> None:
        assert load_calendar("illes_balears", calendars_dir).years == {2026, 2027}
        assert load_calendar("palma", calendars_dir).years == {2026}

    def test_no_common_year_raises(self, calendars_dir: Path) -> None:
        (calendars_dir / "palma" / "2026.yaml").unlink()
        write_calendar(calendars_dir / "palma" / "2025.yaml", calendar_data(date(2025, 1, 20)))
        with pytest.raises(CalendarNotAvailableError):
            load_calendar("palma", calendars_dir)

    def test_unknown_territory_raises(self, calendars_dir: Path) -> None:
        with pytest.raises(CalendarNotAvailableError):
            load_calendar("sevilla", calendars_dir)

    @pytest.mark.parametrize(
        "corrupt",
        [
            holiday_from_another_year,
            undeclared_source,
            holiday_without_source,
            source_without_url,
            unknown_status,
            no_holidays,
        ],
    )
    def test_invalid_data_names_the_file(
        self, calendars_dir: Path, corrupt: Callable[[dict[str, Any]], None]
    ) -> None:
        data = calendar_data(date(2026, 1, 20))
        corrupt(data)
        write_calendar(calendars_dir / "palma" / "2026.yaml", data)
        with pytest.raises(CalendarDataError, match=r"palma[/\\]2026\.yaml"):
            load_calendar("palma", calendars_dir)


class TestRepositoryCalendars:
    """Datos reales de calendars/, contrastados con
    knowledge/dias-inhabiles-2026-illes-balears-palma.md (tabla resumen)."""

    PALMA_2026 = (
        date(2026, 1, 1),
        date(2026, 1, 6),
        date(2026, 1, 20),
        date(2026, 3, 2),
        date(2026, 4, 2),
        date(2026, 4, 3),
        date(2026, 4, 6),
        date(2026, 5, 1),
        date(2026, 6, 24),
        date(2026, 8, 15),
        date(2026, 10, 12),
        date(2026, 12, 8),
        date(2026, 12, 25),
        date(2026, 12, 26),
    )

    def test_palma_2026_holidays(self) -> None:
        calendar = load_calendar("palma", DEFAULT_CALENDARS_DIR)
        assert {day for day in calendar.holidays if day.year == 2026} == set(self.PALMA_2026)

    def test_national_2026_matches_the_age_calendar(self) -> None:
        """Días inhábiles en todo el territorio nacional (anexo de BOE-A-2025-23702)."""
        calendar = load_calendar("nacional", DEFAULT_CALENDARS_DIR)
        assert {day for day in calendar.holidays if day.year == 2026} == {
            date(2026, 1, 1),
            date(2026, 1, 6),
            date(2026, 4, 3),
            date(2026, 5, 1),
            date(2026, 10, 12),
            date(2026, 12, 8),
            date(2026, 12, 25),
        }

    def test_illes_balears_2026_has_the_twelve_days_of_the_caib_agreement(self) -> None:
        """Ap. a) del Acuerdo de BOE-A-2025-26609: doce días, sin las fiestas locales."""
        calendar = load_calendar("illes_balears", DEFAULT_CALENDARS_DIR)
        local = {date(2026, 1, 20), date(2026, 6, 24)}
        assert {day for day in calendar.holidays if day.year == 2026} == (
            set(self.PALMA_2026) - local
        )

    def test_2027_is_not_available_yet(self) -> None:
        with pytest.raises(CalendarNotAvailableError):
            load_calendar("palma", DEFAULT_CALENDARS_DIR).is_business_day(date(2027, 1, 4))

    @pytest.mark.parametrize("territory", ["nacional", "illes_balears", "palma"])
    def test_every_territory_loads(self, territory: str) -> None:
        assert 2026 in load_calendar(territory, DEFAULT_CALENDARS_DIR).years
