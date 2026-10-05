"""Utilidades de los tests de reglas de tráfico.

Los calendarios son SINTÉTICOS (sin festivos salvo los que pone cada test), para provocar
casos límite; no son datos oficiales. Todas las fechas y datos son inventados.
"""

from collections.abc import Callable
from datetime import date
from typing import Any

import pytest

from core.calendario import Calendar
from core.reglas import EvaluationContext, RuleResult
from core.trafico import TrafficRule, load_traffic_rules
from core.trafico.caso import TrafficCase

RULES = {rule.definition.id: rule for rule in load_traffic_rules()}
YEARS = range(2025, 2029)
TODAY = date(2026, 9, 23)


def context(*holidays: date, today: date = TODAY, years: range = YEARS) -> EvaluationContext:
    return EvaluationContext(calendar=Calendar(holidays, years), reference_date=today)


def case(**data: Any) -> TrafficCase:
    return TrafficCase.model_validate(data)


def in_person(day: date) -> dict[str, Any]:
    return {"canal": "en_el_acto", "fecha_en_el_acto": day}


def by_post(day: date) -> dict[str, Any]:
    return {"canal": "domicilio", "intentos_domicilio": [{"fecha": day, "resultado": "entregada"}]}


def by_dev(available: date, accessed: date | None = None) -> dict[str, Any]:
    return {"canal": "dev", "dev_puesta_disposicion": available, "dev_acceso": accessed}


def by_boe(published: date, *attempts: tuple[date, str]) -> dict[str, Any]:
    return {
        "canal": "boe",
        "boe_publicacion": published,
        "intentos_domicilio": [{"fecha": d, "resultado": r} for d, r in attempts],
    }


Evaluate = Callable[..., RuleResult]


def evaluator(rule_id: str) -> Evaluate:
    rule: TrafficRule = RULES[rule_id]

    def run(ctx: EvaluationContext | None = None, **data: Any) -> RuleResult:
        return rule.evaluate(case(**data), ctx or context())

    return run


@pytest.fixture
def statuses() -> Callable[[RuleResult], dict[str, str]]:
    def get(result: RuleResult) -> dict[str, str]:
        return {check.condition: check.status.value for check in result.checks}

    return get
