"""Cómputo de plazos administrativos.

Fundamento: art. 30 de la Ley 39/2015 (knowledge/ley-39-2015.md) y, para notificaciones
electrónicas, su art. 43.2 y el art. 90.2 del RDL 6/2015 (knowledge/rdl-6-2015.md).

El calendario que se pasa decide qué días son inhábiles: el llamante combina el de la
residencia y el de la sede del órgano (art. 30.6) o usa solo el de la sede electrónica si
se presenta en un registro electrónico (art. 31.3).
"""

import calendar as pycalendar
from datetime import date, timedelta
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, PositiveInt

from core.calendario import Calendar

ONE_DAY = timedelta(days=1)

# Art. 43.2 Ley 39/2015 (norma general, no sectorial) y art. 90.2 RDL 6/2015 (regla análoga
# para la DEV): rechazo a los diez días naturales sin acceso.
ELECTRONIC_REJECTION_DAYS = 10


class DeadlineUnit(StrEnum):
    BUSINESS_DAYS = "dias_habiles"
    CALENDAR_DAYS = "dias_naturales"
    MONTHS = "meses"
    YEARS = "anios"


class DeadlineSpec(BaseModel):
    """Plazo tal y como lo declara una regla: `{cantidad: 20, unidad: dias_naturales}`."""

    model_config = ConfigDict(frozen=True, validate_by_name=True, validate_by_alias=True)

    amount: PositiveInt = Field(alias="cantidad")
    unit: DeadlineUnit = Field(alias="unidad")


class Deadline(BaseModel):
    model_config = ConfigDict(frozen=True)

    notification_date: date
    spec: DeadlineSpec
    start: date
    """Primer día que computa."""
    nominal_end: date
    """Último día del plazo antes de aplicar la prórroga del art. 30.5."""
    end: date
    """Último día para actuar."""

    @property
    def extended(self) -> bool:
        return self.end != self.nominal_end


def compute_deadline(notification_date: date, spec: DeadlineSpec, calendar: Calendar) -> Deadline:
    """Último día de un plazo para actuar, contado desde una notificación, publicación o
    silencio (art. 30.3 y 30.4), con la prórroga del art. 30.5.

    No sirve para la prescripción (el art. 112.1 del RDL 6/2015 cuenta desde el mismo día de
    los hechos) ni para plazos de notificación presunta como el del art. 91 del RDL 6/2015.
    TODO(juridico): definir su cómputo (día inicial y aplicación del art. 30.5) en la tarea 5.

    Lanza CalendarNotAvailableError si el cómputo necesita un año sin calendario oficial.
    """
    if spec.unit is DeadlineUnit.BUSINESS_DAYS:
        start = _next_business_day(notification_date + ONE_DAY, calendar)
        end = start
        for _ in range(spec.amount - 1):
            end = _next_business_day(end + ONE_DAY, calendar)
        return Deadline(
            notification_date=notification_date, spec=spec, start=start, nominal_end=end, end=end
        )

    if spec.unit is DeadlineUnit.CALENDAR_DAYS:
        nominal_end = notification_date + timedelta(days=spec.amount)
    else:
        months = spec.amount * 12 if spec.unit is DeadlineUnit.YEARS else spec.amount
        nominal_end = _same_day_months_later(notification_date, months)
    return Deadline(
        notification_date=notification_date,
        spec=spec,
        start=notification_date + ONE_DAY,
        nominal_end=nominal_end,
        end=_next_business_day(nominal_end, calendar),
    )


def electronic_notification_date(
    made_available_on: date, accessed_on: date | None, *, rejection_applies: bool
) -> date | None:
    """Fecha en que se entiende practicada una notificación electrónica, para contar los
    plazos del interesado.

    Si se accede dentro de los diez días naturales siguientes a la puesta a disposición, es
    la fecha de acceso. Si no, se entiende rechazada el décimo día, sin prórroga aunque sea
    inhábil (criterio fijado el 2026-09-23: da la fecha más temprana posible).

    `rejection_applies` indica si concurren las condiciones del rechazo: notificación
    electrónica obligatoria o elegida por el interesado (art. 43.2 Ley 39/2015) y, en la DEV,
    constancia de la recepción sin imposibilidad técnica o material del acceso (art. 90.2
    RDL 6/2015). Si no concurren y no hubo acceso, no hay notificación practicada: devuelve
    None.

    No sirve para comprobar si la Administración notificó en plazo (caducidad): el art. 43.3
    da por cumplida esa obligación con la puesta a disposición.
    """
    if accessed_on is not None and accessed_on < made_available_on:
        raise ValueError("La fecha de acceso es anterior a la puesta a disposición.")
    rejection_date = made_available_on + timedelta(days=ELECTRONIC_REJECTION_DAYS)
    if accessed_on is not None and (accessed_on <= rejection_date or not rejection_applies):
        return accessed_on
    return rejection_date if rejection_applies else None


def _next_business_day(day: date, calendar: Calendar) -> date:
    """`day` si es hábil; si no, el primer día hábil siguiente (art. 30.5)."""
    while not calendar.is_business_day(day):
        day += ONE_DAY
    return day


def _same_day_months_later(day: date, months: int) -> date:
    """Art. 30.4: mismo día del mes de vencimiento, o su último día si no existe."""
    month_index = day.month - 1 + months
    year, month = day.year + month_index // 12, month_index % 12 + 1
    last_day = pycalendar.monthrange(year, month)[1]
    return date(year, month, min(day.day, last_day))
