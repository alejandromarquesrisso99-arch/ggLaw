"""Regla trafico.caducidad_procedimiento (art. 112.3 RDL 6/2015)."""

from pydantic import BaseModel, ConfigDict, Field

from core.plazos import DateRange, DeadlineSpec, Timeliness, timeliness, uncertain_period_end
from core.reglas import Check, CheckStatus, Evaluation, EvaluationContext, all_required
from core.trafico._util import check, fmt, fmt_range, missing
from core.trafico.caso import NotificationChannel, Severity, TrafficCase


class ResolutoryCase(BaseModel):
    """Supuesto del art. 95.4 en que la denuncia surte efecto de acto resolutorio si no hay
    alegaciones ni pago. Un campo a None no se exige."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    gravedad: Severity
    detrae_puntos: bool | None = None
    en_el_acto: bool | None = None


class Params(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    plazo_caducidad: DeadlineSpec
    denuncia_como_acto_resolutorio: tuple[ResolutoryCase, ...] = Field(min_length=1)


def _no_payment(case: TrafficCase) -> Check:
    if case.paid_voluntarily is None:
        return missing("sin_pago_voluntario", "pago_voluntario")
    if case.paid_voluntarily:
        return check(
            "sin_pago_voluntario",
            CheckStatus.NOT_MET,
            "Pagaste la multa con reducción: el procedimiento terminó con el pago (art. 94.c).",
        )
    return check("sin_pago_voluntario", CheckStatus.MET, "No pagaste la multa con reducción.")


def _matches(pattern: ResolutoryCase, case: TrafficCase, in_person: bool) -> bool | None:
    """True/False si el caso encaja o no en el supuesto; None si faltan datos para saberlo."""
    if case.severity != pattern.gravedad:
        return False
    if pattern.en_el_acto is not None and pattern.en_el_acto != in_person:
        return False
    if pattern.detrae_puntos is not None:
        if case.deducts_points is None:
            return None
        return case.deducts_points == pattern.detrae_puntos
    return True


def _needs_resolution(params: Params, case: TrafficCase) -> Check:
    condition = "requiere_resolucion"
    if case.submitted_allegations is None:
        return missing(condition, "alegaciones_presentadas")
    if case.submitted_allegations:
        return check(
            condition,
            CheckStatus.MET,
            "Presentaste alegaciones: el procedimiento debía terminar con resolución.",
        )
    if case.severity is None:
        return missing(condition, "gravedad")
    assert case.complaint_notification is not None
    in_person = case.complaint_notification.channel is NotificationChannel.IN_PERSON
    matches = [_matches(p, case, in_person) for p in params.denuncia_como_acto_resolutorio]
    if any(matches):
        return check(
            condition,
            CheckStatus.NOT_MET,
            "Sin alegaciones ni pago, la denuncia surtió efecto de acto resolutorio (art. "
            "95.4): no hay resolución posterior que pueda llegar tarde.",
        )
    if None in matches:
        return missing(condition, "detrae_puntos")
    return check(
        condition,
        CheckStatus.MET,
        "Por la gravedad de la infracción y el modo de notificación, la denuncia no surte "
        "efecto de acto resolutorio (art. 95.4): hace falta resolución sancionadora.",
    )


def _not_suspended(case: TrafficCase) -> Check:
    if case.proceedings_suspended is None:
        return missing("sin_suspension", "procedimiento_suspendido")
    if case.proceedings_suspended:
        return check(
            "sin_suspension",
            CheckStatus.UNCERTAIN,
            "El procedimiento estuvo suspendido o paralizado: el plazo de caducidad no corre "
            "durante la suspensión por causa penal (art. 112.3) y ggLaw aún no calcula ese "
            "descuento.",
        )
    return check("sin_suspension", CheckStatus.MET, "No consta suspensión ni paralización.")


def _initiation(case: TrafficCase) -> DateRange:
    """Fecha de iniciación (art. 86): la de la denuncia notificada en el acto, la de la
    incoación si se conoce o, si no, un rango entre los hechos y la primera actuación para
    notificarla (la incoación no puede ser posterior a su notificación)."""
    notification = case.complaint_notification
    assert notification is not None
    if notification.channel is NotificationChannel.IN_PERSON:
        assert notification.handed_over_on is not None
        return DateRange.exact(notification.handed_over_on)
    if case.initiation_date is not None:
        return DateRange.exact(case.initiation_date)
    assert case.offence_date is not None
    return DateRange(earliest=case.offence_date, latest=notification.first_action_on())


def _resolution(case: TrafficCase) -> DateRange | None:
    """Momento en que se «produce» la resolución (art. 112.3), o None si no hay resolución.

    TODO(juridico): ¿basta con dictarla o hace falta notificarla o intentarlo (arts. 25.1, 40.4
    y 43.3 Ley 39/2015)? Se da el rango de la fecha en que se dictó a la de su notificación.
    """
    if case.resolution_date is None:
        return None
    return DateRange(earliest=case.resolution_date, latest=case.resolution_notified_on)


def _expired(params: Params, case: TrafficCase, ctx: EvaluationContext) -> Check:
    condition = "plazo_vencido_sin_resolucion"
    initiation = _initiation(case)
    end = DateRange(
        earliest=uncertain_period_end(
            initiation.earliest, params.plazo_caducidad, ctx.calendar
        ).earliest,
        latest=(
            uncertain_period_end(initiation.latest, params.plazo_caducidad, ctx.calendar).latest
            if initiation.latest is not None
            else None
        ),
    )
    period = f"El plazo de caducidad acaba {fmt_range(end)}"
    resolution = _resolution(case)
    if resolution is None:
        # Sin resolución: solo se sabe que no se ha producido hasta la fecha de referencia.
        produced = f"no consta resolución a fecha {fmt(ctx.reference_date)}"
        if ctx.reference_date <= end.earliest:
            result = Timeliness.IN_TIME
        elif end.latest is not None and ctx.reference_date > end.latest:
            result = Timeliness.LATE
        else:
            result = Timeliness.UNCERTAIN
    else:
        produced = f"la resolución se produjo {fmt_range(resolution)}"
        result = timeliness(resolution, end)
    match result:
        case Timeliness.LATE:
            return check(condition, CheckStatus.MET, f"{period} y {produced}: ha caducado.")
        case Timeliness.IN_TIME:
            return check(condition, CheckStatus.NOT_MET, f"{period} y {produced}: no ha caducado.")
        case Timeliness.UNCERTAIN:
            if resolution is not None and resolution.latest is None:
                return missing(condition, "notificacion_resolucion")
            if initiation.earliest != initiation.latest:
                return missing(condition, "fecha_incoacion")
            return check(
                condition,
                CheckStatus.UNCERTAIN,
                f"{period} y {produced}. El resultado depende de cómo se compute el plazo o "
                "de si la resolución debía notificarse dentro de él, dudas jurídicas abiertas.",
            )


def _resolution_known(case: TrafficCase) -> Check:
    condition = "resolucion_conocida"
    if case.resolution_date is not None:
        return check(condition, CheckStatus.MET, "Conoces la fecha de la resolución.")
    if case.file_reviewed is None:
        return missing(condition, "expediente_consultado")
    if case.file_reviewed:
        return check(condition, CheckStatus.MET, "El expediente no contiene resolución.")
    return check(
        condition,
        CheckStatus.UNCERTAIN,
        "No has recibido resolución, pero pudo dictarse sin que te haya llegado. Pide copia "
        "del expediente (art. 53.1.a Ley 39/2015) antes de alegar la caducidad.",
    )


def evaluate(params: Params, case: TrafficCase, ctx: EvaluationContext) -> Evaluation:
    return all_required(
        [
            _no_payment(case),
            _needs_resolution(params, case),
            _not_suspended(case),
            _expired(params, case, ctx),
            _resolution_known(case),
        ]
    )
