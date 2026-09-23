"""Tests de core/plazos.py: cómputo de plazos administrativos.

Fundamento (Ley 39/2015, art. 30; resumen propio, no transcripción):
  - 30.2: los plazos por días son hábiles salvo que una ley diga otra cosa; se excluyen
    sábados, domingos y festivos.
  - 30.3: los plazos en días se cuentan desde el día siguiente a la notificación,
    publicación o silencio.
  - 30.4: los plazos en meses o años se cuentan de fecha a fecha; si en el mes de
    vencimiento no hay día equivalente, el plazo expira el último día del mes.
  - 30.5: si el último día es inhábil, se prorroga al primer día hábil siguiente.
  - 30.6: un día inhábil en la residencia del interesado o en la sede del órgano es
    inhábil en todo caso.
Notificaciones electrónicas: art. 43.2 de la Ley 39/2015.

Texto literal y fuente: knowledge/ley-39-2015.md (BOE consolidado, consultado 2026-09-23).

Los calendarios de estos tests son SINTÉTICOS: sus festivos se eligen para provocar casos
límite y no son datos oficiales. Los calendarios reales viven en calendars/.
"""

import calendar as pycalendar
from collections.abc import Iterable
from datetime import date, timedelta

import pytest
from pydantic import ValidationError

from core.calendario import Calendar, CalendarNotAvailableError
from core.plazos import (
    DeadlineSpec,
    DeadlineUnit,
    compute_deadline,
    electronic_notification_date,
)

YEARS = range(2026, 2030)


def make_calendar(*holidays: date, years: Iterable[int] = YEARS) -> Calendar:
    return Calendar(holidays=holidays, years=years)


NO_HOLIDAYS = make_calendar()

# Jueves Santo, Viernes Santo y Lunes de Pascua de 2026 (Pascua: 5-IV-2026). Con el fin de
# semana suman cinco días inhábiles seguidos.
EASTER_2026 = (date(2026, 4, 2), date(2026, 4, 3), date(2026, 4, 6))


def business_days(amount: int) -> DeadlineSpec:
    return DeadlineSpec(amount=amount, unit=DeadlineUnit.BUSINESS_DAYS)


def calendar_days(amount: int) -> DeadlineSpec:
    return DeadlineSpec(amount=amount, unit=DeadlineUnit.CALENDAR_DAYS)


def months(amount: int) -> DeadlineSpec:
    return DeadlineSpec(amount=amount, unit=DeadlineUnit.MONTHS)


def years(amount: int) -> DeadlineSpec:
    return DeadlineSpec(amount=amount, unit=DeadlineUnit.YEARS)


def days_between(first: date, last: date) -> list[date]:
    """Días de `first` a `last`, ambos incluidos (vacío si `last` < `first`)."""
    return [first + timedelta(days=i) for i in range((last - first).days + 1)]


class TestBusinessDays:
    """Plazos en días hábiles (art. 30.2 y 30.3)."""

    def test_counts_from_next_day_and_skips_weekends(self) -> None:
        # Lunes 14-IX: cuentan 15-18, 21-25 y 28 de septiembre.
        deadline = compute_deadline(date(2026, 9, 14), business_days(10), NO_HOLIDAYS)
        assert deadline.start == date(2026, 9, 15)
        assert deadline.end == date(2026, 9, 28)

    def test_notified_on_friday_starts_on_monday(self) -> None:
        deadline = compute_deadline(date(2026, 10, 2), business_days(1), NO_HOLIDAYS)
        assert deadline.start == date(2026, 10, 5)
        assert deadline.end == date(2026, 10, 5)

    def test_notified_on_saturday_starts_on_monday(self) -> None:
        """Una notificación electrónica puede abrirse en sábado."""
        deadline = compute_deadline(date(2026, 10, 3), business_days(5), NO_HOLIDAYS)
        assert deadline.start == date(2026, 10, 5)
        assert deadline.end == date(2026, 10, 9)

    def test_skips_holiday_inside_the_period(self) -> None:
        calendar = make_calendar(date(2026, 9, 17))
        deadline = compute_deadline(date(2026, 9, 14), business_days(10), calendar)
        assert deadline.end == date(2026, 9, 29)

    def test_holiday_right_after_notification_delays_start(self) -> None:
        calendar = make_calendar(date(2026, 1, 20))
        deadline = compute_deadline(date(2026, 1, 19), business_days(1), calendar)
        assert deadline.start == date(2026, 1, 21)
        assert deadline.end == date(2026, 1, 21)

    @pytest.mark.parametrize(
        ("amount", "expected_end"),
        [(1, date(2026, 4, 7)), (3, date(2026, 4, 9))],
    )
    def test_chained_holidays(self, amount: int, expected_end: date) -> None:
        calendar = make_calendar(*EASTER_2026)
        deadline = compute_deadline(date(2026, 4, 1), business_days(amount), calendar)
        assert deadline.start == date(2026, 4, 7)
        assert deadline.end == expected_end

    @pytest.mark.parametrize(
        ("amount", "expected_end"),
        [(10, date(2027, 1, 5)), (11, date(2027, 1, 7))],
    )
    def test_crosses_year_end(self, amount: int, expected_end: date) -> None:
        calendar = make_calendar(date(2026, 12, 25), date(2027, 1, 1), date(2027, 1, 6))
        deadline = compute_deadline(date(2026, 12, 18), business_days(amount), calendar)
        assert deadline.end == expected_end

    def test_december_24_and_31_are_business_days_unless_declared(self) -> None:
        calendar = make_calendar(date(2026, 12, 25))
        assert compute_deadline(date(2026, 12, 23), business_days(1), calendar).end == date(
            2026, 12, 24
        )
        assert compute_deadline(date(2026, 12, 30), business_days(1), calendar).end == date(
            2026, 12, 31
        )

    def test_august_counts_as_business_days(self) -> None:
        """Agosto es hábil en vía administrativa (su inhabilidad es propia de los plazos
        procesales, no de los administrativos)."""
        deadline = compute_deadline(date(2026, 7, 24), business_days(20), NO_HOLIDAYS)
        assert deadline.end == date(2026, 8, 21)

    def test_end_is_never_extended(self) -> None:
        deadline = compute_deadline(date(2026, 9, 14), business_days(10), NO_HOLIDAYS)
        assert deadline.nominal_end == deadline.end
        assert not deadline.extended


class TestCalendarDays:
    """Plazos en días naturales, cuando una norma sectorial los fija (art. 30.2).

    En tráfico (arts. 87, 93, 94 y 95 del RDL 6/2015) el RDL no regula el último día
    inhábil; su art. 83.1 y la DA 1.ª.2.c) de la Ley 39/2015 remiten supletoriamente a esta,
    así que se aplica la prórroga del art. 30.5 (knowledge/rdl-6-2015.md).
    """

    def test_counts_weekends_and_holidays(self) -> None:
        calendar = make_calendar(date(2026, 9, 11))
        deadline = compute_deadline(date(2026, 9, 1), calendar_days(20), calendar)
        assert deadline.start == date(2026, 9, 2)
        assert deadline.end == date(2026, 9, 21)
        assert not deadline.extended

    def test_last_day_on_saturday_is_extended_to_monday(self) -> None:
        deadline = compute_deadline(date(2026, 3, 4), calendar_days(10), NO_HOLIDAYS)
        assert deadline.nominal_end == date(2026, 3, 14)
        assert deadline.end == date(2026, 3, 16)
        assert deadline.extended

    def test_last_day_on_sunday_is_extended_to_monday(self) -> None:
        deadline = compute_deadline(date(2026, 3, 2), calendar_days(20), NO_HOLIDAYS)
        assert deadline.nominal_end == date(2026, 3, 22)
        assert deadline.end == date(2026, 3, 23)

    def test_extension_skips_chained_holidays(self) -> None:
        calendar = make_calendar(*EASTER_2026)
        deadline = compute_deadline(date(2026, 3, 13), calendar_days(20), calendar)
        assert deadline.nominal_end == date(2026, 4, 2)
        assert deadline.end == date(2026, 4, 7)

    @pytest.mark.parametrize(
        ("notified", "expected_end"),
        [
            (date(2027, 2, 10), date(2027, 3, 2)),  # febrero de 28 días
            (date(2028, 2, 10), date(2028, 3, 1)),  # febrero de 29 días
        ],
    )
    def test_february_in_common_and_leap_years(self, notified: date, expected_end: date) -> None:
        deadline = compute_deadline(notified, calendar_days(20), NO_HOLIDAYS)
        assert deadline.end == expected_end


class TestMonths:
    """Plazos en meses: de fecha a fecha (art. 30.4)."""

    def test_date_to_date_ignoring_holidays_in_between(self) -> None:
        calendar = make_calendar(*EASTER_2026)
        deadline = compute_deadline(date(2026, 3, 16), months(1), calendar)
        assert deadline.start == date(2026, 3, 17)
        assert deadline.end == date(2026, 4, 16)

    def test_no_equivalent_day_ends_on_last_day_of_month(self) -> None:
        deadline = compute_deadline(date(2026, 3, 31), months(1), NO_HOLIDAYS)
        assert deadline.end == date(2026, 4, 30)

    @pytest.mark.parametrize(
        ("notified", "nominal_end", "end"),
        [
            # 2026 no es bisiesto y el 28-II-2026 es sábado: se prorroga al lunes 2-III.
            (date(2026, 1, 30), date(2026, 2, 28), date(2026, 3, 2)),
            (date(2026, 1, 31), date(2026, 2, 28), date(2026, 3, 2)),
            # 2028 es bisiesto y el 29-II-2028 es martes.
            (date(2028, 1, 31), date(2028, 2, 29), date(2028, 2, 29)),
        ],
    )
    def test_end_of_january_into_february(
        self, notified: date, nominal_end: date, end: date
    ) -> None:
        deadline = compute_deadline(notified, months(1), NO_HOLIDAYS)
        assert deadline.nominal_end == nominal_end
        assert deadline.end == end

    @pytest.mark.parametrize(
        ("notified", "expected_end"),
        [
            (date(2026, 1, 28), date(2026, 2, 28)),  # el cómputo empieza el 29, que no existe en II
            (date(2028, 1, 29), date(2028, 2, 29)),  # bisiesto
        ],
    )
    def test_notification_day_exists_in_february(self, notified: date, expected_end: date) -> None:
        deadline = compute_deadline(notified, months(1), NO_HOLIDAYS)
        assert deadline.nominal_end == expected_end

    def test_last_day_of_february_is_not_month_end_to_month_end(self) -> None:
        """De fecha a fecha: del 29-II se va al 29-III, no al 31-III."""
        deadline = compute_deadline(date(2028, 2, 29), months(1), NO_HOLIDAYS)
        assert deadline.end == date(2028, 3, 29)

    def test_several_months_across_year_end(self) -> None:
        deadline = compute_deadline(date(2026, 11, 30), months(3), NO_HOLIDAYS)
        assert deadline.nominal_end == date(2027, 2, 28)  # domingo
        assert deadline.end == date(2027, 3, 1)

    def test_notified_on_non_business_day_keeps_the_date(self) -> None:
        deadline = compute_deadline(date(2026, 10, 3), months(1), NO_HOLIDAYS)  # sábado
        assert deadline.start == date(2026, 10, 4)
        assert deadline.end == date(2026, 11, 3)

    def test_last_day_holiday_followed_by_weekend(self) -> None:
        calendar = make_calendar(date(2027, 1, 1))
        deadline = compute_deadline(date(2026, 12, 1), months(1), calendar)
        assert deadline.nominal_end == date(2027, 1, 1)  # viernes festivo
        assert deadline.end == date(2027, 1, 4)


class TestYears:
    """Plazos en años: de fecha a fecha (art. 30.4)."""

    def test_date_to_date(self) -> None:
        deadline = compute_deadline(date(2026, 5, 15), years(1), NO_HOLIDAYS)
        assert deadline.nominal_end == date(2027, 5, 15)  # sábado
        assert deadline.end == date(2027, 5, 17)

    def test_from_february_29_ends_on_february_28(self) -> None:
        deadline = compute_deadline(date(2028, 2, 29), years(1), NO_HOLIDAYS)
        assert deadline.end == date(2029, 2, 28)

    @pytest.mark.parametrize("notified", [date(2026, 1, 31), date(2026, 5, 15), date(2028, 2, 29)])
    def test_twelve_months_equal_one_year(self, notified: date) -> None:
        by_months = compute_deadline(notified, months(12), NO_HOLIDAYS)
        by_years = compute_deadline(notified, years(1), NO_HOLIDAYS)
        assert (by_months.nominal_end, by_months.end) == (by_years.nominal_end, by_years.end)


class TestResidenceAndSeatCalendars:
    """Art. 30.6: inhábil en la residencia del interesado o en la sede del órgano.

    El art. 31.3 excluye el 30.6 en los registros electrónicos, que aplican solo el
    calendario de su sede electrónica (knowledge/ley-39-2015.md). Quien llame a
    compute_deadline elige el calendario según el canal de presentación.
    TODO(juridico): ¿el 31.3 rige también el vencimiento (art. 30.5) o solo la presentación?
    """

    def test_holiday_in_either_place_is_non_business(self) -> None:
        residence = make_calendar(date(2026, 1, 20))
        seat = make_calendar(date(2026, 1, 23))
        notified = date(2026, 1, 19)

        assert compute_deadline(notified, business_days(5), residence).end == date(2026, 1, 27)
        assert compute_deadline(notified, business_days(5), seat).end == date(2026, 1, 27)
        merged = residence.merge(seat)
        assert compute_deadline(notified, business_days(5), merged).end == date(2026, 1, 28)


class TestMissingCalendarData:
    """Si falta el calendario oficial de un año, no se calcula: nunca se da por hecho que
    ese año no tiene festivos."""

    def test_business_days_reaching_an_uncovered_year(self) -> None:
        only_2026 = make_calendar(years=[2026])
        with pytest.raises(CalendarNotAvailableError):
            compute_deadline(date(2026, 12, 18), business_days(10), only_2026)

    def test_months_ending_in_an_uncovered_year(self) -> None:
        only_2026 = make_calendar(years=[2026])
        with pytest.raises(CalendarNotAvailableError):
            compute_deadline(date(2026, 12, 1), months(1), only_2026)

    def test_extension_into_an_uncovered_year(self) -> None:
        calendar = make_calendar(date(2026, 12, 31), years=[2026])
        with pytest.raises(CalendarNotAvailableError):
            compute_deadline(date(2026, 12, 21), calendar_days(10), calendar)


class TestDeadlineSpec:
    """Especificación de un plazo tal y como la declaran las reglas en rules/*.yaml."""

    @pytest.mark.parametrize("amount", [0, -1])
    def test_amount_must_be_positive(self, amount: int) -> None:
        with pytest.raises(ValidationError):
            DeadlineSpec(amount=amount, unit=DeadlineUnit.BUSINESS_DAYS)

    @pytest.mark.parametrize(
        ("raw_unit", "unit"),
        [
            ("dias_habiles", DeadlineUnit.BUSINESS_DAYS),
            ("dias_naturales", DeadlineUnit.CALENDAR_DAYS),
            ("meses", DeadlineUnit.MONTHS),
            ("anios", DeadlineUnit.YEARS),
        ],
    )
    def test_reads_spanish_rule_data(self, raw_unit: str, unit: DeadlineUnit) -> None:
        spec = DeadlineSpec.model_validate({"cantidad": 20, "unidad": raw_unit})
        assert spec == DeadlineSpec(amount=20, unit=unit)

    def test_hours_are_rejected(self) -> None:
        """Los plazos por horas (art. 30.1) no están implementados: se rechazan en vez de
        aproximarlos."""
        with pytest.raises(ValidationError):
            DeadlineSpec.model_validate({"cantidad": 24, "unidad": "horas"})


class TestElectronicNotification:
    """Art. 43.2: la notificación electrónica se practica al acceder a su contenido. Si es
    obligatoria o la eligió el interesado y no se accede en diez días naturales desde la
    puesta a disposición, se entiende rechazada.

    El art. 90.2 del RDL 6/2015 recoge la misma regla para la DEV.

    Criterio fijado por Alex el 2026-09-23 ante el silencio de la norma: la notificación se
    entiende practicada el décimo día tras la puesta a disposición, sin prórroga aunque ese
    día sea inhábil. Da la fecha más temprana posible, así que el plazo del ciudadano nunca
    vence después de lo real. Ojo: para comprobar si la Administración notificó a tiempo
    (caducidad) el criterio prudente sería el contrario.
    TODO(juridico): revisar con jurisprudencia del TS sobre el cómputo de los diez días.
    """

    MADE_AVAILABLE = date(2026, 6, 1)  # lunes; el décimo día es el jueves 11-VI

    @pytest.mark.parametrize("accessed_on", [date(2026, 6, 1), date(2026, 6, 5), date(2026, 6, 11)])
    def test_access_within_ten_days_is_the_notification_date(self, accessed_on: date) -> None:
        assert (
            electronic_notification_date(self.MADE_AVAILABLE, accessed_on, rejection_applies=True)
            == accessed_on
        )

    def test_no_access_is_rejection_on_the_tenth_day(self) -> None:
        assert electronic_notification_date(
            self.MADE_AVAILABLE, None, rejection_applies=True
        ) == date(2026, 6, 11)

    def test_tenth_day_on_saturday_is_not_extended(self) -> None:
        made_available = date(2026, 6, 3)  # miércoles; el décimo día es el sábado 13-VI
        assert electronic_notification_date(made_available, None, rejection_applies=True) == date(
            2026, 6, 13
        )

    def test_access_after_rejection_does_not_change_the_date(self) -> None:
        late_access = date(2026, 6, 12)
        assert electronic_notification_date(
            self.MADE_AVAILABLE, late_access, rejection_applies=True
        ) == date(2026, 6, 11)

    def test_access_before_being_made_available_is_an_error(self) -> None:
        with pytest.raises(ValueError, match="puesta a disposición"):
            electronic_notification_date(
                self.MADE_AVAILABLE, date(2026, 5, 31), rejection_applies=True
            )

    def test_deadline_runs_from_the_rejection(self) -> None:
        notified = electronic_notification_date(self.MADE_AVAILABLE, None, rejection_applies=True)
        assert notified is not None
        deadline = compute_deadline(notified, months(1), NO_HOLIDAYS)
        assert deadline.nominal_end == date(2026, 7, 11)  # sábado
        assert deadline.end == date(2026, 7, 13)

    def test_without_rejection_conditions_there_is_no_notification(self) -> None:
        """Notificación electrónica voluntaria, o en la DEV sin constancia de recepción o con
        imposibilidad de acceso: sin acceso no hay notificación practicada."""
        assert (
            electronic_notification_date(self.MADE_AVAILABLE, None, rejection_applies=False) is None
        )

    def test_without_rejection_conditions_a_late_access_is_the_notification(self) -> None:
        late_access = date(2026, 6, 20)
        assert (
            electronic_notification_date(self.MADE_AVAILABLE, late_access, rejection_applies=False)
            == late_access
        )


# Calendario sintético con festivos repartidos por el año, algunos encadenados con fines de
# semana (puente del 7 y 8 de diciembre) y uno en sábado (26-XII-2026).
DENSE_CALENDAR = make_calendar(
    date(2026, 1, 1),
    date(2026, 1, 6),
    date(2026, 1, 20),
    *EASTER_2026,
    date(2026, 5, 1),
    date(2026, 10, 12),
    date(2026, 12, 7),
    date(2026, 12, 8),
    date(2026, 12, 25),
    date(2026, 12, 26),
    date(2027, 1, 1),
    date(2027, 1, 6),
)
EVERY_DAY_OF_2026 = days_between(date(2026, 1, 1), date(2026, 12, 31))


def assert_first_business_day_on_or_after(deadline_end: date, nominal_end: date) -> None:
    assert DENSE_CALENDAR.is_business_day(deadline_end)
    skipped = days_between(nominal_end, deadline_end - timedelta(days=1))
    assert not any(DENSE_CALENDAR.is_business_day(day) for day in skipped)


class TestInvariants:
    """Propiedades que deben cumplirse para cualquier fecha de notificación de 2026."""

    @pytest.mark.parametrize("amount", [1, 2, 5, 10, 15, 20, 30])
    def test_business_days(self, amount: int) -> None:
        for notified in EVERY_DAY_OF_2026:
            deadline = compute_deadline(notified, business_days(amount), DENSE_CALENDAR)
            counted = [
                day
                for day in days_between(notified + timedelta(days=1), deadline.end)
                if DENSE_CALENDAR.is_business_day(day)
            ]
            assert len(counted) == amount, notified
            assert counted[0] == deadline.start, notified
            assert counted[-1] == deadline.end, notified
            assert not deadline.extended, notified

    @pytest.mark.parametrize("amount", [1, 10, 15, 20, 30])
    def test_calendar_days(self, amount: int) -> None:
        for notified in EVERY_DAY_OF_2026:
            deadline = compute_deadline(notified, calendar_days(amount), DENSE_CALENDAR)
            assert deadline.start == notified + timedelta(days=1), notified
            assert deadline.nominal_end == notified + timedelta(days=amount), notified
            assert_first_business_day_on_or_after(deadline.end, deadline.nominal_end)

    @pytest.mark.parametrize("amount", [1, 2, 3, 6, 12])
    def test_months(self, amount: int) -> None:
        for notified in EVERY_DAY_OF_2026:
            deadline = compute_deadline(notified, months(amount), DENSE_CALENDAR)
            month_index = notified.month - 1 + amount
            year, month = notified.year + month_index // 12, month_index % 12 + 1
            last_day = pycalendar.monthrange(year, month)[1]
            assert deadline.start == notified + timedelta(days=1), notified
            assert deadline.nominal_end == date(year, month, min(notified.day, last_day)), notified
            assert_first_business_day_on_or_after(deadline.end, deadline.nominal_end)
