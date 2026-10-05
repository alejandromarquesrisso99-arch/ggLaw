"""Regla trafico.prescripcion_infraccion (art. 112.1 y 112.2 RDL 6/2015).

Solo evalúa el tramo entre los hechos y la primera actuación que pudo interrumpir la
prescripción. La prescripción posterior, por paralización del procedimiento durante más de
un mes (art. 112.2, párrafo segundo), no se evalúa: ver TODO(juridico) en el YAML.
"""

from pydantic import BaseModel, ConfigDict

from core.plazos import DateRange, DeadlineSpec, Timeliness, timeliness, uncertain_period_end
from core.reglas import Check, CheckStatus, Evaluation, EvaluationContext, all_required
from core.trafico._util import check, fmt_range, missing
from core.trafico.caso import ContestedSanction, Severity, TrafficCase


class Params(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    plazo_prescripcion: dict[Severity, DeadlineSpec]
    notificacion_boe: DeadlineSpec


def first_interruption(case: TrafficCase, params: Params, ctx: EvaluationContext) -> DateRange:
    """Momento de la primera actuación que pudo interrumpir la prescripción.

    Para la notificación de la denuncia va de la primera actuación para notificar a la fecha
    en que se entiende practicada: qué momento interrumpe es una duda abierta (ver YAML).
    """
    notification = case.complaint_notification
    assert notification is not None
    practiced = notification.practiced_on(params.notificacion_boe, ctx.calendar)
    candidates = [DateRange(earliest=notification.first_action_on(), latest=practiced.latest)]
    candidates += [DateRange.exact(day) for day in case.other_proceedings]
    known_latest = [c.latest for c in candidates if c.latest is not None]
    return DateRange(
        earliest=min(c.earliest for c in candidates),
        latest=min(known_latest) if known_latest else None,
    )


def _original_offence(case: TrafficCase) -> Check:
    """La fecha de los hechos solo es el día inicial si se recurre la infracción original. La
    del art. 77.j se comete al vencer el plazo para identificar (art. 93.1), dato que el caso
    aún no recoge."""
    condition = "infraccion_original"
    if case.contested_sanction is None:
        return missing(condition, "sancion_recurrida")
    if case.contested_sanction is ContestedSanction.FAILURE_TO_IDENTIFY:
        return check(
            condition,
            CheckStatus.UNCERTAIN,
            "La infracción por no identificar al conductor (art. 77.j) se comete al vencer el "
            "plazo para identificar, no el día de la infracción original. ggLaw aún no calcula "
            "su prescripción.",
        )
    return check(condition, CheckStatus.MET, "Se recurre la sanción por la infracción original.")


def evaluate(params: Params, case: TrafficCase, ctx: EvaluationContext) -> Evaluation:
    assert case.offence_date is not None
    assert case.severity is not None
    spec = params.plazo_prescripcion[case.severity]
    end = uncertain_period_end(case.offence_date, spec, ctx.calendar)
    interruption = first_interruption(case, params, ctx)
    period = f"El plazo de prescripción ({case.severity}) acaba {fmt_range(end)}"
    act = f"la primera actuación que lo interrumpe es {fmt_range(interruption)}"
    match timeliness(interruption, end):
        case Timeliness.LATE:
            expired = check(
                "plazo_vencido_antes_de_interrumpirse",
                CheckStatus.MET,
                f"{period} y {act}: la infracción prescribió antes.",
            )
        case Timeliness.IN_TIME:
            expired = check(
                "plazo_vencido_antes_de_interrumpirse",
                CheckStatus.NOT_MET,
                f"{period} y {act}: se interrumpió a tiempo.",
            )
        case Timeliness.UNCERTAIN:
            expired = check(
                "plazo_vencido_antes_de_interrumpirse",
                CheckStatus.UNCERTAIN,
                f"{period} y {act}. El resultado depende de cómo se compute el plazo o de qué "
                "momento interrumpe, que son dudas jurídicas abiertas.",
            )

    if case.file_reviewed is None:
        known = missing("actuaciones_conocidas", "expediente_consultado")
    elif case.file_reviewed:
        known = check(
            "actuaciones_conocidas",
            CheckStatus.MET,
            "Has consultado el expediente: se conocen todas las actuaciones.",
        )
    else:
        known = check(
            "actuaciones_conocidas",
            CheckStatus.UNCERTAIN,
            "Puede haber actuaciones que no conoces y que interrumpieron la prescripción "
            "(art. 112.2), como averiguaciones de tu domicilio con otras administraciones. "
            "Pide copia del expediente (art. 53.1.a Ley 39/2015) antes de alegarla.",
        )
    return all_required([_original_offence(case), expired, known])
