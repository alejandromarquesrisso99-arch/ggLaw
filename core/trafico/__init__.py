"""Reglas de defensa en multas de tráfico: une cada YAML de rules/trafico/ con su evaluador."""

from collections.abc import Callable, Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ValidationError

from core.reglas import (
    DEFAULT_RULES_DIR,
    Evaluation,
    EvaluationContext,
    Outcome,
    RuleDataError,
    RuleDefinition,
    RuleResult,
    load_rule_definitions,
)
from core.trafico import caducidad, cinemometro, identificacion, notificacion, prescripcion
from core.trafico.caso import CASE_DATA_NAMES, TrafficCase


@dataclass(frozen=True)
class _Evaluator[P: BaseModel]:
    params_model: type[P]
    run: Callable[[P, TrafficCase, EvaluationContext], Evaluation]
    required: tuple[str, ...]
    """Datos sin los que el evaluador no puede empezar. Los demás de `datos_necesarios` los
    pide el evaluador solo si el caso los necesita."""


EVALUATORS: dict[str, _Evaluator[Any]] = {
    "trafico.prescripcion_infraccion": _Evaluator(
        prescripcion.Params,
        prescripcion.evaluate,
        ("fecha_hechos", "gravedad", "notificacion_denuncia"),
    ),
    "trafico.caducidad_procedimiento": _Evaluator(
        caducidad.Params, caducidad.evaluate, ("fecha_hechos", "notificacion_denuncia")
    ),
    "trafico.defecto_notificacion_denuncia": _Evaluator(
        notificacion.Params, notificacion.evaluate, ("notificacion_denuncia",)
    ),
    "trafico.identificacion_conductor": _Evaluator(
        identificacion.Params,
        identificacion.evaluate,
        ("detencion_vehiculo", "identifico_conductor", "notificacion_denuncia"),
    ),
    "trafico.control_metrologico_cinemometro": _Evaluator(
        cinemometro.Params, cinemometro.evaluate, ()
    ),
}


@dataclass(frozen=True)
class TrafficRule:
    definition: RuleDefinition
    params: BaseModel
    _evaluator: _Evaluator[Any]

    def evaluate(self, case: TrafficCase, context: EvaluationContext) -> RuleResult:
        rule = self.definition
        missing = tuple(name for name in self._evaluator.required if not case.is_known(name))
        if missing:
            return RuleResult(
                rule_id=rule.id, outcome=Outcome.MISSING_DATA, checks=(), missing=missing
            )
        evaluation = self._evaluator.run(self.params, case, context)
        unknown = {check.condition for check in evaluation.checks} - rule.condition_ids
        undeclared = set(evaluation.missing) - set(rule.datos_necesarios)
        if unknown or undeclared:
            raise RuleDataError(
                f"{rule.id}: el evaluador usa condiciones {sorted(unknown)} o datos "
                f"{sorted(undeclared)} que el YAML no declara."
            )
        return RuleResult(
            rule_id=rule.id,
            outcome=evaluation.outcome,
            checks=evaluation.checks,
            missing=evaluation.missing,
        )


def load_traffic_rules(base_dir: Path = DEFAULT_RULES_DIR) -> tuple[TrafficRule, ...]:
    """Carga las reglas de tráfico. Falla si un YAML no tiene evaluador o al revés, si sus
    parámetros no cumplen el esquema o si cita datos que el caso no tiene."""
    definitions = {
        rule_id: rule
        for rule_id, rule in load_rule_definitions(base_dir).items()
        if rule.ambito == "trafico"
    }
    if set(definitions) != set(EVALUATORS):
        raise RuleDataError(
            f"Reglas sin evaluador: {sorted(set(definitions) - set(EVALUATORS))}; "
            f"evaluadores sin regla: {sorted(set(EVALUATORS) - set(definitions))}."
        )
    rules = []
    for rule_id, definition in definitions.items():
        unknown_data = set(definition.datos_necesarios) - CASE_DATA_NAMES
        if unknown_data:
            raise RuleDataError(f"{rule_id}: datos desconocidos {sorted(unknown_data)}.")
        evaluator = EVALUATORS[rule_id]
        if not set(evaluator.required) <= set(definition.datos_necesarios):
            raise RuleDataError(f"{rule_id}: datos imprescindibles que el YAML no declara.")
        try:
            params = evaluator.params_model.model_validate(definition.parametros)
        except ValidationError as error:
            raise RuleDataError(f"{rule_id}: parámetros no válidos: {error}") from error
        rules.append(TrafficRule(definition, params, evaluator))
    return tuple(rules)


def evaluate_rules(
    case: TrafficCase, context: EvaluationContext, rules: Iterable[TrafficRule] | None = None
) -> tuple[RuleResult, ...]:
    return tuple(
        rule.evaluate(case, context) for rule in (load_traffic_rules() if rules is None else rules)
    )
