"""Reglas de defensa: definición en YAML (rules/) y resultado de su evaluación.

Cada regla vive en rules/<ámbito>/<nombre>.yaml y su id es «<ámbito>.<nombre>». El YAML
declara el fundamento (que debe estar transcrito en knowledge/), las condiciones, los datos
que usa y sus plazos (`parametros`). La lógica que evalúa las condiciones está en
core/<ámbito>/ y es determinista: el LLM nunca decide si un motivo procede.

Un motivo que se alega sin proceder resta credibilidad al escrito. Por eso una regla solo
responde «procede» si todas sus condiciones se cumplen sin margen de duda; si el resultado
depende de una duda jurídica abierta (TODO(juridico)) responde «dudoso», y si faltan datos
lo dice y nombra cuáles.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from datetime import date
from enum import StrEnum
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

from core.calendario import Calendar

DEFAULT_RULES_DIR = Path(__file__).resolve().parent.parent / "rules"
DEFAULT_KNOWLEDGE_DIR = Path(__file__).resolve().parent.parent / "knowledge"


class RuleDataError(ValueError):
    """Un fichero de reglas no cumple el esquema o es incoherente."""


class Outcome(StrEnum):
    APPLIES = "procede"
    DOES_NOT_APPLY = "no_procede"
    UNCERTAIN = "dudoso"
    MISSING_DATA = "faltan_datos"


class CheckStatus(StrEnum):
    MET = "se_cumple"
    NOT_MET = "no_se_cumple"
    UNCERTAIN = "dudoso"
    MISSING_DATA = "faltan_datos"


class Check(BaseModel):
    """Resultado de una condición de la regla, con su explicación para el usuario."""

    model_config = ConfigDict(frozen=True)

    condition: str
    status: CheckStatus
    detail: str
    missing: tuple[str, ...] = ()


class Evaluation(BaseModel):
    """Lo que devuelve el evaluador de una regla."""

    model_config = ConfigDict(frozen=True)

    outcome: Outcome
    checks: tuple[Check, ...]

    @property
    def missing(self) -> tuple[str, ...]:
        return tuple(dict.fromkeys(name for check in self.checks for name in check.missing))


class RuleResult(BaseModel):
    model_config = ConfigDict(frozen=True)

    rule_id: str
    outcome: Outcome
    checks: tuple[Check, ...]
    missing: tuple[str, ...]


@dataclass(frozen=True)
class EvaluationContext:
    """`calendar` decide qué días son inhábiles (ver core/plazos.py); `reference_date` es la
    fecha en que se evalúa (normalmente, hoy)."""

    calendar: Calendar
    reference_date: date


def all_required(checks: Iterable[Check]) -> Evaluation:
    """Resultado de una regla cuyas condiciones deben cumplirse todas.

    Una condición que no se cumple basta para descartar el motivo, aunque falten datos de
    otras. Si no hay ninguna así, los datos que faltan van antes que las dudas: al
    completarlos, la regla puede quedar descartada.
    """
    checks = tuple(checks)
    statuses = {check.status for check in checks}
    if CheckStatus.NOT_MET in statuses:
        outcome = Outcome.DOES_NOT_APPLY
    elif CheckStatus.MISSING_DATA in statuses:
        outcome = Outcome.MISSING_DATA
    elif CheckStatus.UNCERTAIN in statuses:
        outcome = Outcome.UNCERTAIN
    else:
        outcome = Outcome.APPLIES
    return Evaluation(outcome=outcome, checks=checks)


class LegalBasis(BaseModel):
    """Precepto en que se funda la regla. `knowledge` es el fichero de knowledge/ con su texto
    transcrito: sin transcripción, no hay fundamento."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    norma: str
    articulo: int | str
    apartado: str | None = None
    knowledge: str


class ConditionDefinition(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str
    descripcion: str
    fundamento: str


class RuleDefinition(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    id: str
    titulo: str
    ambito: str
    estado: Literal["borrador", "revisado", "validado_abogado"]
    fundamento: tuple[LegalBasis, ...] = Field(min_length=1)
    condiciones: tuple[ConditionDefinition, ...] = Field(min_length=1)
    datos_necesarios: tuple[str, ...] = Field(min_length=1)
    parametros: dict[str, object] = Field(default_factory=dict)
    parrafo_tipo: str | None
    notas: str

    @model_validator(mode="after")
    def _unique_ids(self) -> RuleDefinition:
        ids = [condition.id for condition in self.condiciones]
        if len(ids) != len(set(ids)):
            raise ValueError(f"Condiciones repetidas en {self.id}: {ids}")
        if len(self.datos_necesarios) != len(set(self.datos_necesarios)):
            raise ValueError(f"Datos repetidos en {self.id}: {self.datos_necesarios}")
        return self

    @property
    def condition_ids(self) -> frozenset[str]:
        return frozenset(condition.id for condition in self.condiciones)


def load_rule_definitions(base_dir: Path = DEFAULT_RULES_DIR) -> dict[str, RuleDefinition]:
    """Lee rules/<ámbito>/<nombre>.yaml. El id de cada regla debe coincidir con su ruta."""
    rules: dict[str, RuleDefinition] = {}
    for path in sorted(base_dir.glob("*/*.yaml")):
        try:
            raw = yaml.safe_load(path.read_text(encoding="utf-8"))
            rule = RuleDefinition.model_validate(raw)
        except (yaml.YAMLError, ValidationError) as error:
            raise RuleDataError(f"{path}: {error}") from error
        expected_id = f"{path.parent.name}.{path.stem}"
        if rule.id != expected_id:
            raise RuleDataError(f"{path}: el id debe ser «{expected_id}», no «{rule.id}».")
        if rule.ambito != path.parent.name:
            raise RuleDataError(f"{path}: el ámbito debe ser «{path.parent.name}».")
        rules[rule.id] = rule
    return rules


def check_legal_basis(rule: RuleDefinition, knowledge_dir: Path = DEFAULT_KNOWLEDGE_DIR) -> None:
    """Comprueba que cada artículo citado está transcrito en el fichero de knowledge/ que se
    indica (lista `articulos` de su frontmatter)."""
    for basis in rule.fundamento:
        path = knowledge_dir.parent / basis.knowledge
        if path.parent != knowledge_dir or not path.is_file():
            raise RuleDataError(f"{rule.id}: no existe {basis.knowledge} en knowledge/.")
        articles = _frontmatter(path).get("articulos")
        if not isinstance(articles, list) or basis.articulo not in articles:
            raise RuleDataError(
                f"{rule.id}: el art. {basis.articulo} ({basis.norma}) no está transcrito en "
                f"{basis.knowledge}."
            )


def _frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise RuleDataError(f"{path}: falta el frontmatter.")
    block = text[4:].split("\n---\n", 1)[0]
    data = yaml.safe_load(block)
    if not isinstance(data, dict):
        raise RuleDataError(f"{path}: frontmatter no válido.")
    return {str(key): value for key, value in data.items()}
