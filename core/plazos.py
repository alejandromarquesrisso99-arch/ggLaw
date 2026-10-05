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

from pydantic import BaseModel, ConfigDict, Field, PositiveInt, model_validator

from core.calendario import Calendar, CalendarNotAvailableError

ONE_DAY = timedelta(days=1)

# Art. 43.2 Ley 39/2015 (norma general, no sectorial) y art. 90.2 RDL 6/2015, que coincide:
# rechazo a los diez días naturales sin acceso.
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

    No sirve para la prescripción ni la caducidad (el art. 112 del RDL 6/2015 cuenta desde el
    mismo día de los hechos o de la iniciación): para ellas, uncertain_period_end.

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

    last_day = nominal_end(notification_date, spec)
    return Deadline(
        notification_date=notification_date,
        spec=spec,
        start=notification_date + ONE_DAY,
        nominal_end=last_day,
        end=_next_business_day(last_day, calendar),
    )


def nominal_end(notification_date: date, spec: DeadlineSpec) -> date:
    """Último día de un plazo en días naturales, meses o años (art. 30.3 y 30.4), antes de la
    prórroga del art. 30.5. No necesita calendario."""
    if spec.unit is DeadlineUnit.BUSINESS_DAYS:
        raise ValueError("Un plazo en días hábiles necesita calendario: usa compute_deadline.")
    if spec.unit is DeadlineUnit.CALENDAR_DAYS:
        return notification_date + timedelta(days=spec.amount)
    months = spec.amount * 12 if spec.unit is DeadlineUnit.YEARS else spec.amount
    return _same_day_months_later(notification_date, months)


class DateRange(BaseModel):
    """Fecha que no se conoce con exactitud, porque depende de datos que faltan o de una duda
    jurídica abierta: está entre `earliest` y `latest`, ambos incluidos. `latest` es None si
    no hay cota superior (p. ej., falta el calendario oficial del año)."""

    model_config = ConfigDict(frozen=True)

    earliest: date
    latest: date | None

    @model_validator(mode="after")
    def _ordered(self) -> "DateRange":
        if self.latest is not None and self.latest < self.earliest:
            raise ValueError("La cota superior es anterior a la inferior.")
        return self

    @classmethod
    def exact(cls, day: date) -> "DateRange":
        return cls(earliest=day, latest=day)


class Timeliness(StrEnum):
    IN_TIME = "en_plazo"
    LATE = "fuera_de_plazo"
    UNCERTAIN = "dudoso"


def timeliness(event: DateRange, last_day: DateRange) -> Timeliness:
    """¿Ocurrió `event` dentro de un plazo cuyo último día es `last_day`?

    Solo responde «en plazo» o «fuera de plazo» si la respuesta es la misma para cualquier
    fecha posible de ambos rangos. Si depende de cuál sea la real, responde «dudoso»: ggLaw no
    resuelve una duda jurídica eligiendo la interpretación que le conviene.
    """
    if event.latest is not None and event.latest <= last_day.earliest:
        return Timeliness.IN_TIME
    if last_day.latest is not None and event.earliest > last_day.latest:
        return Timeliness.LATE
    return Timeliness.UNCERTAIN


def uncertain_period_end(start_day: date, spec: DeadlineSpec, calendar: Calendar) -> DateRange:
    """Último día de un plazo que la norma cuenta «desde» un hecho sin fijar el cómputo, como
    la prescripción (art. 112.1 RDL 6/2015) o la caducidad (art. 112.3).

    TODO(juridico) (knowledge/rdl-6-2015-regimen-sancionador.md): no está decidido si el día
    inicial computa ni si se aplica la prórroga del art. 30.5 de la Ley 39/2015. Por eso se
    devuelve el rango que cubre todas las respuestas:

    - earliest: el día inicial computa (el plazo acaba la víspera del mismo día del mes de
      vencimiento) y no hay prórroga.
    - latest: art. 30.4 (acaba el mismo día del mes de vencimiento) con la prórroga del art.
      30.5; None si no hay calendario oficial para calcularla.
    """
    last_day = nominal_end(start_day, spec)
    try:
        latest: date | None = _next_business_day(last_day, calendar)
    except CalendarNotAvailableError:
        latest = None
    return DateRange(earliest=last_day - ONE_DAY, latest=latest)


def deadline_end_range(notified: DateRange, spec: DeadlineSpec, calendar: Calendar) -> DateRange:
    """Último día para actuar (con la prórroga del art. 30.5) cuando la fecha de notificación
    es un rango, como en la publicación en el BOE (art. 91 RDL 6/2015).

    Sin calendario oficial, la cota inferior es el último día sin prórroga (o, en días hábiles,
    el mismo número de días naturales) y no hay cota superior.
    """
    try:
        earliest = compute_deadline(notified.earliest, spec, calendar).end
    except CalendarNotAvailableError:
        if spec.unit is DeadlineUnit.BUSINESS_DAYS:
            earliest = notified.earliest + timedelta(days=spec.amount)
        else:
            earliest = nominal_end(notified.earliest, spec)
    latest: date | None = None
    if notified.latest is not None:
        try:
            latest = compute_deadline(notified.latest, spec, calendar).end
        except CalendarNotAvailableError:
            latest = None
    return DateRange(earliest=earliest, latest=latest)


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
