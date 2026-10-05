"""Datos de un caso de tráfico que usan las reglas de rules/trafico/.

Los rellena la extracción del LLM (validada contra este esquema) o el propio usuario. Los
nombres de campo están en inglés; los alias en español son los que citan los YAML de reglas
en `datos_necesarios`. Un dato a None significa «no se sabe»: ninguna regla lo presupone.
"""

from __future__ import annotations

from contextlib import suppress
from datetime import date, timedelta
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, model_validator

from core.calendario import Calendar, CalendarNotAvailableError
from core.plazos import (
    DateRange,
    DeadlineSpec,
    compute_deadline,
    electronic_notification_date,
    nominal_end,
)

ONE_DAY = timedelta(days=1)


class Severity(StrEnum):
    """Arts. 75, 76 y 77 RDL 6/2015."""

    MINOR = "leve"
    SERIOUS = "grave"
    VERY_SERIOUS = "muy_grave"


class NotificationChannel(StrEnum):
    """Cauce por el que se practicó la notificación (arts. 89, 90 y 91 RDL 6/2015)."""

    IN_PERSON = "en_el_acto"
    DEV = "dev"
    ADDRESS = "domicilio"
    BOE = "boe"


class AttemptResult(StrEnum):
    """Resultado de un intento de entrega en el domicilio (art. 90.3 RDL 6/2015)."""

    DELIVERED = "entregada"
    NOBODY = "ausente"
    """Nadie se hizo cargo de la notificación."""
    REFUSED = "rechazada"
    UNKNOWN_ADDRESSEE = "desconocido"
    """Destinatario desconocido en el domicilio o dirección incorrecta."""


class _Data(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid", validate_by_name=True)


class AddressAttempt(_Data):
    on: date = Field(alias="fecha")
    result: AttemptResult = Field(alias="resultado")


class Notification(_Data):
    """Notificación de un acto (aquí, la denuncia) con las fechas que constan de cada cauce."""

    channel: NotificationChannel = Field(alias="canal")
    handed_over_on: date | None = Field(default=None, alias="fecha_en_el_acto")
    dev_available_on: date | None = Field(default=None, alias="dev_puesta_disposicion")
    dev_accessed_on: date | None = Field(default=None, alias="dev_acceso")
    address_attempts: tuple[AddressAttempt, ...] = Field(default=(), alias="intentos_domicilio")
    boe_published_on: date | None = Field(default=None, alias="boe_publicacion")

    @model_validator(mode="after")
    def _consistent(self) -> Notification:
        attempts = [attempt.on for attempt in self.address_attempts]
        if attempts != sorted(attempts):
            raise ValueError("Los intentos de notificación deben ir en orden de fecha.")
        if (
            self.dev_available_on is not None
            and self.dev_accessed_on is not None
            and self.dev_accessed_on < self.dev_available_on
        ):
            raise ValueError("La fecha de acceso a la DEV es anterior a la puesta a disposición.")
        required = {
            NotificationChannel.IN_PERSON: self.handed_over_on,
            NotificationChannel.DEV: self.dev_available_on,
            NotificationChannel.BOE: self.boe_published_on,
        }
        if self.channel in required and required[self.channel] is None:
            raise ValueError(f"Falta la fecha de la notificación por el cauce «{self.channel}».")
        if self.channel is NotificationChannel.ADDRESS and self._address_effective() is None:
            raise ValueError("Notificación en domicilio sin un intento entregado o rechazado.")
        return self

    def _address_effective(self) -> date | None:
        """Entrega o rechazo en el domicilio: el trámite se tiene por efectuado (art. 90.3)."""
        for attempt in self.address_attempts:
            if attempt.result in (AttemptResult.DELIVERED, AttemptResult.REFUSED):
                return attempt.on
        return None

    def first_action_on(self) -> date:
        """Primera actuación de la Administración para notificar."""
        dates = [
            self.handed_over_on,
            self.dev_available_on,
            self.boe_published_on,
            *(attempt.on for attempt in self.address_attempts),
        ]
        return min(day for day in dates if day is not None)

    def practiced_on(self, boe_period: DeadlineSpec, calendar: Calendar) -> DateRange:
        """Fecha en que la notificación se entiende practicada: la del primer cauce que produjo
        efecto (art. 41.7 Ley 39/2015), aunque después se publicara en el BOE.

        - En el acto: ese día (art. 89.1).
        - Domicilio: entrega o rechazo (art. 90.3).
        - DEV: acceso o rechazo a los diez días naturales (art. 90.2; criterio de
          core.plazos.electronic_notification_date). Si no hubo acceso y aun así se publicó en
          el BOE, pudo haber imposibilidad técnica del acceso (art. 90.2): no hay cota superior
          propia y manda la del BOE.
        - BOE: «transcurrido el período de veinte días naturales» desde la publicación (art.
          91). TODO(juridico): ¿se entiende practicada el último de esos días o el siguiente?
          ¿Se prorroga si es inhábil? Hasta resolverlo se da el rango que cubre ambas lecturas:
          del día 20 al día siguiente al último día del plazo prorrogado.
        """
        ranges: list[DateRange] = []
        if self.handed_over_on is not None:
            ranges.append(DateRange.exact(self.handed_over_on))
        address = self._address_effective()
        if address is not None:
            ranges.append(DateRange.exact(address))
        if self.dev_available_on is not None:
            dev = electronic_notification_date(
                self.dev_available_on, self.dev_accessed_on, rejection_applies=True
            )
            assert dev is not None
            unaccessed_then_boe = (
                self.dev_accessed_on is None and self.channel is NotificationChannel.BOE
            )
            ranges.append(DateRange(earliest=dev, latest=None if unaccessed_then_boe else dev))
        if self.boe_published_on is not None:
            latest: date | None = None
            with suppress(CalendarNotAvailableError):
                latest = compute_deadline(self.boe_published_on, boe_period, calendar).end
                latest += ONE_DAY
            earliest = nominal_end(self.boe_published_on, boe_period)
            ranges.append(DateRange(earliest=earliest, latest=latest))
        known_latest = [r.latest for r in ranges if r.latest is not None]
        return DateRange(
            earliest=min(r.earliest for r in ranges),
            latest=min(known_latest) if known_latest else None,
        )


class ContestedSanction(StrEnum):
    ORIGINAL_OFFENCE = "infraccion_original"
    """Sanción por la infracción de circulación, impuesta al titular."""
    FAILURE_TO_IDENTIFY = "no_identificar_conductor"
    """Sanción por no identificar al conductor (art. 77.j RDL 6/2015)."""


class DriverIdentification(_Data):
    """Identificación del conductor por el titular, arrendatario o conductor habitual."""

    on: date = Field(alias="fecha")
    includes_licence: bool = Field(alias="incluye_permiso")
    """Incluye el número de permiso del conductor o, si no figura en el Registro de
    Conductores e Infractores, el titular dispone de copia de su autorización (art. 11.1.a)."""
    online: bool = Field(alias="telematica")
    other_person: bool = Field(alias="otra_persona")
    """Se identificó a una persona distinta de quien recurre."""


class TrafficCase(_Data):
    offence_date: date | None = Field(default=None, alias="fecha_hechos")
    severity: Severity | None = Field(default=None, alias="gravedad")
    deducts_points: bool | None = Field(default=None, alias="detrae_puntos")
    complaint_notification: Notification | None = Field(default=None, alias="notificacion_denuncia")
    has_dev: bool | None = Field(default=None, alias="dev_asignada")
    """El denunciado tenía Dirección Electrónica Vial cuando se le notificó."""
    file_reviewed: bool | None = Field(default=None, alias="expediente_consultado")
    """El interesado ha visto el expediente completo (art. 53.1.a Ley 39/2015)."""
    other_proceedings: tuple[date, ...] = Field(default=(), alias="otras_actuaciones")
    """Otras actuaciones del expediente que pudieron interrumpir la prescripción."""
    initiation_date: date | None = Field(default=None, alias="fecha_incoacion")
    submitted_allegations: bool | None = Field(default=None, alias="alegaciones_presentadas")
    """Formuló alegaciones dentro de los veinte días naturales (art. 95.1 y 95.4)."""
    paid_voluntarily: bool | None = Field(default=None, alias="pago_voluntario")
    proceedings_suspended: bool | None = Field(default=None, alias="procedimiento_suspendido")
    """El procedimiento se suspendió por un proceso penal o se paralizó por causa imputable
    al interesado."""
    resolution_date: date | None = Field(default=None, alias="fecha_resolucion")
    resolution_notified_on: date | None = Field(default=None, alias="notificacion_resolucion")
    """Primer intento de notificación o puesta a disposición de la resolución sancionadora."""
    vehicle_stopped: bool | None = Field(default=None, alias="detencion_vehiculo")
    identified_driver: bool | None = Field(default=None, alias="identifico_conductor")
    driver_identification: DriverIdentification | None = Field(
        default=None, alias="identificacion_conductor"
    )
    contested_sanction: ContestedSanction | None = Field(default=None, alias="sancion_recurrida")
    owner_liable_offence: bool | None = Field(
        default=None, alias="infraccion_responsabilidad_titular"
    )
    """La infracción es de documentación del vehículo, reconocimientos periódicos o estado de
    conservación que afecte a la seguridad: el titular responde en todo caso (art. 82.f)."""
    speeding: bool | None = Field(default=None, alias="infraccion_velocidad")
    """Infracción por exceso de velocidad (arts. 76.a y 77.a RDL 6/2015)."""
    measured_by_instrument: bool | None = Field(default=None, alias="medida_con_cinemometro")
    metrological_control_on_record: bool | None = Field(
        default=None, alias="consta_control_metrologico"
    )
    """La denuncia o el expediente acreditan el control metrológico del cinemómetro."""

    @model_validator(mode="after")
    def _dates_in_order(self) -> TrafficCase:
        def before(first: date | None, second: date | None, message: str) -> None:
            if first is not None and second is not None and second < first:
                raise ValueError(message)

        notification = self.complaint_notification
        first_action = notification.first_action_on() if notification else None
        before(self.offence_date, first_action, "La denuncia se notificó antes de los hechos.")
        before(self.offence_date, self.initiation_date, "La incoación es anterior a los hechos.")
        before(self.initiation_date, first_action, "La denuncia se notificó antes de incoarse.")
        before(
            self.resolution_date,
            self.resolution_notified_on,
            "La resolución se notificó antes de dictarse.",
        )
        for day in self.other_proceedings:
            before(self.offence_date, day, "Hay actuaciones anteriores a los hechos.")
        if self.identified_driver is True and self.driver_identification is None:
            raise ValueError("Falta la identificación del conductor.")
        return self

    def is_known(self, alias: str) -> bool:
        return getattr(self, _FIELD_BY_ALIAS[alias]) is not None


_FIELD_BY_ALIAS = {
    str(field.alias): name for name, field in TrafficCase.model_fields.items() if field.alias
}
CASE_DATA_NAMES = frozenset(_FIELD_BY_ALIAS)
