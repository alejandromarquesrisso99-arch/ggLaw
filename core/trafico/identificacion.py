"""Regla trafico.identificacion_conductor (arts. 11, 77.j, 82 y 93.1 RDL 6/2015).

Procede cuando, sin detención del vehículo, se identificó al conductor en plazo y con los
datos exigidos y aun así se sanciona a quien identificó: por la infracción original (si
identificó a otra persona) o por no identificar (art. 77.j). No valora si la identificación
fue veraz.
"""

from pydantic import BaseModel, ConfigDict

from core.plazos import DateRange, DeadlineSpec, Timeliness, deadline_end_range, timeliness
from core.reglas import Check, CheckStatus, Evaluation, EvaluationContext, all_required
from core.trafico._util import check, fmt, fmt_range, missing
from core.trafico.caso import ContestedSanction, NotificationChannel, TrafficCase


class Params(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    plazo_identificacion: DeadlineSpec
    notificacion_boe: DeadlineSpec


def _not_stopped(case: TrafficCase) -> Check:
    assert case.vehicle_stopped is not None
    if case.vehicle_stopped:
        return check(
            "sin_detencion",
            CheckStatus.NOT_MET,
            "Hubo detención del vehículo: el conductor quedó identificado en el acto.",
        )
    return check("sin_detencion", CheckStatus.MET, "No hubo detención del vehículo (art. 93.1).")


def _identified(case: TrafficCase) -> Check:
    condition = "identificacion_completa"
    assert case.identified_driver is not None
    identification = case.driver_identification
    if not case.identified_driver or identification is None:
        return check(condition, CheckStatus.NOT_MET, "No identificaste al conductor.")
    if not identification.includes_licence:
        return check(
            condition,
            CheckStatus.NOT_MET,
            "La identificación no incluía el número de permiso del conductor ni, si no figura "
            "en el Registro de Conductores, disponías de copia de su autorización (art. 11.1.a).",
        )
    return check(condition, CheckStatus.MET, "Identificaste al conductor con su permiso.")


def _in_time(params: Params, case: TrafficCase, ctx: EvaluationContext) -> Check:
    condition = "identificacion_en_plazo"
    identification = case.driver_identification
    if identification is None:
        return check(condition, CheckStatus.NOT_MET, "No hay identificación.")
    notification = case.complaint_notification
    assert notification is not None
    notified = notification.practiced_on(params.notificacion_boe, ctx.calendar)
    last_day = deadline_end_range(notified, params.plazo_identificacion, ctx.calendar)
    text = (
        f"La denuncia se notificó {fmt_range(notified)}; el plazo para identificar acababa "
        f"{fmt_range(last_day)} y identificaste el {fmt(identification.on)}"
    )
    match timeliness(DateRange.exact(identification.on), last_day):
        case Timeliness.IN_TIME:
            return check(condition, CheckStatus.MET, f"{text}: en plazo.")
        case Timeliness.LATE:
            return check(condition, CheckStatus.NOT_MET, f"{text}: fuera de plazo.")
        case Timeliness.UNCERTAIN:
            return check(
                condition,
                CheckStatus.UNCERTAIN,
                f"{text}. Depende del día en que se entiende practicada la notificación, duda "
                "jurídica abierta.",
            )


def _online_if_dev(case: TrafficCase) -> Check:
    condition = "identificacion_telematica_si_dev"
    notification = case.complaint_notification
    identification = case.driver_identification
    assert notification is not None
    if notification.channel is not NotificationChannel.DEV:
        return check(condition, CheckStatus.MET, "No se notificó en la DEV.")
    if identification is None or identification.online:
        return check(condition, CheckStatus.MET, "Se identificó por medios telemáticos.")
    return check(
        condition,
        CheckStatus.UNCERTAIN,
        "Se notificó en la DEV y la identificación no fue telemática, como exige el art. 93.1. "
        "No está resuelto si eso la invalida.",
    )


def _sanction_on_identifier(case: TrafficCase) -> Check:
    condition = "sancion_a_quien_identifico"
    assert case.contested_sanction is not None
    identification = case.driver_identification
    if case.contested_sanction is ContestedSanction.FAILURE_TO_IDENTIFY:
        return check(
            condition,
            CheckStatus.MET,
            "Se te sanciona por no identificar al conductor (art. 77.j), y lo identificaste.",
        )
    if identification is not None and not identification.other_person:
        return check(
            condition,
            CheckStatus.NOT_MET,
            "Te identificaste a ti mismo como conductor: la sanción se dirige contra ti.",
        )
    return check(
        condition,
        CheckStatus.MET,
        "Se te sanciona por la infracción aunque identificaste a otra persona como conductor; "
        "el procedimiento debía dirigirse contra ella (arts. 82.d y 93.1).",
    )


def evaluate(params: Params, case: TrafficCase, ctx: EvaluationContext) -> Evaluation:
    checks = [_not_stopped(case), _identified(case)]
    if case.driver_identification is not None:
        checks += [_in_time(params, case, ctx), _online_if_dev(case)]
    if case.contested_sanction is None:
        checks.append(missing("sancion_a_quien_identifico", "sancion_recurrida"))
    else:
        checks.append(_sanction_on_identifier(case))
    return all_required(checks)
