"""Regla trafico.defecto_notificacion_denuncia (arts. 90 y 91 RDL 6/2015).

Solo evalúa el paso a la notificación edictal en el BOE: si se publicó sin intentar antes la
DEV o, sin DEV, sin los dos intentos en el domicilio del art. 90.3.
"""

from datetime import timedelta

from pydantic import BaseModel, ConfigDict, PositiveInt

from core.plazos import (
    DateRange,
    DeadlineSpec,
    DeadlineUnit,
    Timeliness,
    deadline_end_range,
    timeliness,
)
from core.reglas import Check, CheckStatus, Evaluation, EvaluationContext, Outcome
from core.trafico._util import check, fmt, fmt_range, missing
from core.trafico.caso import AttemptResult, Notification, NotificationChannel, TrafficCase


class Params(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    reintento_domicilio_dias: PositiveInt
    """Art. 90.3: «dentro de los tres días siguientes». La norma no dice si son hábiles o
    naturales: se evalúan ambas lecturas."""


def _dev_not_tried(case: TrafficCase, notification: Notification) -> Check:
    condition = "dev_no_intentada"
    if notification.dev_available_on is not None:
        return check(condition, CheckStatus.NOT_MET, "Consta la puesta a disposición en la DEV.")
    if case.has_dev is None:
        return missing(condition, "dev_asignada")
    if case.has_dev:
        return check(
            condition,
            CheckStatus.MET,
            "Tenías Dirección Electrónica Vial y no consta que se intentara notificar en ella "
            "antes de publicar en el BOE (arts. 90.1 y 91).",
        )
    return check(condition, CheckStatus.NOT_MET, "No tenías Dirección Electrónica Vial.")


def _too_few_attempts(notification: Notification) -> Check:
    condition = "intentos_domicilio_insuficientes"
    if notification.dev_available_on is not None:
        return check(condition, CheckStatus.NOT_MET, "Se notificó primero en la DEV.")
    attempts = notification.address_attempts
    results = {attempt.result for attempt in attempts}
    if AttemptResult.REFUSED in results or AttemptResult.DELIVERED in results:
        return check(
            condition,
            CheckStatus.NOT_MET,
            "Consta una entrega o un rechazo en el domicilio: el trámite se tuvo por "
            "efectuado (art. 90.3).",
        )
    if not attempts:
        return check(
            condition,
            CheckStatus.MET,
            "No consta ningún intento de entrega en el domicilio antes de publicar en el BOE "
            "(arts. 90.1, 90.3 y 91).",
        )
    if len(attempts) >= 2:
        return check(condition, CheckStatus.NOT_MET, "Constan dos intentos en el domicilio.")
    if attempts[0].result is AttemptResult.UNKNOWN_ADDRESSEE:
        return check(
            condition,
            CheckStatus.UNCERTAIN,
            "Solo hubo un intento, con resultado «desconocido». No está resuelto si el art. "
            "90.3 exige un segundo intento cuando el destinatario es desconocido en el "
            "domicilio (art. 44 Ley 39/2015).",
        )
    return check(
        condition,
        CheckStatus.MET,
        f"Solo consta un intento en el domicilio ({fmt(attempts[0].on)}) en que nadie se hizo "
        "cargo; el art. 90.3 exige repetirlo antes de publicar en el BOE.",
    )


def _late_second_attempt(
    params: Params, notification: Notification, ctx: EvaluationContext
) -> Check:
    condition = "segundo_intento_fuera_de_plazo"
    attempts = notification.address_attempts
    if notification.dev_available_on is not None or len(attempts) < 2:
        return check(condition, CheckStatus.NOT_MET, "No hay segundo intento que comprobar.")
    first, second = attempts[0].on, attempts[1].on
    if second == first:
        return check(
            condition,
            CheckStatus.UNCERTAIN,
            "Los dos intentos son del mismo día. No está resuelto si cumplen el art. 90.3 "
            "(«de nuevo dentro de los tres días siguientes»).",
        )
    days = params.reintento_domicilio_dias
    business = deadline_end_range(
        DateRange.exact(first),
        DeadlineSpec(amount=days, unit=DeadlineUnit.BUSINESS_DAYS),
        ctx.calendar,
    )
    # Cota inferior: días naturales sin prórroga. Superior: días hábiles.
    last_day = DateRange(earliest=first + timedelta(days=days), latest=business.latest)
    window = f"el segundo intento ({fmt(second)}) debía hacerse {fmt_range(last_day)} a más tardar"
    match timeliness(DateRange.exact(second), last_day):
        case Timeliness.LATE:
            return check(condition, CheckStatus.MET, f"Según el art. 90.3, {window}.")
        case Timeliness.IN_TIME:
            return check(condition, CheckStatus.NOT_MET, f"Según el art. 90.3, {window}: cumple.")
        case Timeliness.UNCERTAIN:
            return check(
                condition,
                CheckStatus.UNCERTAIN,
                f"Según el art. 90.3, {window}. Depende de si los tres días son hábiles o "
                "naturales, duda jurídica abierta.",
            )


def evaluate(params: Params, case: TrafficCase, ctx: EvaluationContext) -> Evaluation:
    notification = case.complaint_notification
    assert notification is not None
    if notification.channel is not NotificationChannel.BOE:
        return Evaluation(
            outcome=Outcome.DOES_NOT_APPLY,
            checks=(
                check(
                    "notificada_en_boe",
                    CheckStatus.NOT_MET,
                    "La denuncia no se notificó por edicto en el BOE.",
                ),
            ),
        )
    published = check(
        "notificada_en_boe", CheckStatus.MET, "La denuncia se notificó por edicto en el BOE."
    )
    if case.file_reviewed is None:
        reviewed = missing("intentos_conocidos", "expediente_consultado")
    elif case.file_reviewed:
        reviewed = check(
            "intentos_conocidos", CheckStatus.MET, "Los intentos constan en el expediente."
        )
    else:
        reviewed = check(
            "intentos_conocidos",
            CheckStatus.UNCERTAIN,
            "Los intentos de notificación solo se conocen viendo el expediente (acuses de "
            "recibo). Pide copia (art. 53.1.a Ley 39/2015) antes de alegar este defecto.",
        )
    defects = (
        _dev_not_tried(case, notification),
        _too_few_attempts(notification),
        _late_second_attempt(params, notification, ctx),
    )
    checks = (published, reviewed, *defects)
    statuses = {defect.status for defect in defects}
    if CheckStatus.MET in statuses:
        outcome = {
            CheckStatus.MET: Outcome.APPLIES,
            CheckStatus.UNCERTAIN: Outcome.UNCERTAIN,
            CheckStatus.MISSING_DATA: Outcome.MISSING_DATA,
            CheckStatus.NOT_MET: Outcome.DOES_NOT_APPLY,
        }[reviewed.status]
    elif CheckStatus.MISSING_DATA in statuses:
        outcome = Outcome.MISSING_DATA
    elif CheckStatus.UNCERTAIN in statuses:
        outcome = Outcome.UNCERTAIN
    else:
        outcome = Outcome.DOES_NOT_APPLY
    return Evaluation(outcome=outcome, checks=checks)
