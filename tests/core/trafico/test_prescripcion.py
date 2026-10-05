"""trafico.prescripcion_infraccion: art. 112.1 y 112.2 RDL 6/2015
(knowledge/rdl-6-2015-regimen-sancionador.md). Plazos: 3 meses leves, 6 graves y muy graves,
desde el mismo día de los hechos."""

from datetime import date

import pytest

from core.reglas import Outcome
from tests.core.trafico.conftest import by_boe, by_dev, by_post, context, evaluator, in_person

evaluate = evaluator("trafico.prescripcion_infraccion")
FACTS = date(2026, 1, 15)  # jueves; +3 meses: miércoles 15-IV; +6 meses: miércoles 15-VII


def run(notification: dict[str, object], severity: str = "leve", **data: object) -> Outcome:
    data.setdefault("expediente_consultado", True)
    data.setdefault("sancion_recurrida", "infraccion_original")
    return evaluate(
        fecha_hechos=FACTS, gravedad=severity, notificacion_denuncia=notification, **data
    ).outcome


class TestFirstStretch:
    def test_notified_in_person_never_prescribes(self) -> None:
        assert run(in_person(FACTS)) is Outcome.DOES_NOT_APPLY

    def test_notified_well_within_the_period(self) -> None:
        assert run(by_post(date(2026, 3, 2))) is Outcome.DOES_NOT_APPLY

    def test_notified_on_the_day_before_is_in_time_under_every_reading(self) -> None:
        assert run(by_post(date(2026, 4, 14))) is Outcome.DOES_NOT_APPLY

    def test_last_day_depends_on_open_questions(self) -> None:
        # El 15-IV es el último día según el art. 30.4, pero no si computa el día inicial.
        assert run(by_post(date(2026, 4, 15))) is Outcome.UNCERTAIN

    def test_notified_after_every_possible_end(self) -> None:
        assert run(by_post(date(2026, 4, 16))) is Outcome.APPLIES

    @pytest.mark.parametrize(("severity", "months_later"), [("grave", 6), ("muy_grave", 6)])
    def test_serious_offences_have_six_months(self, severity: str, months_later: int) -> None:
        assert run(by_post(date(2026, 4, 16)), severity) is Outcome.DOES_NOT_APPLY
        assert run(by_post(date(2026, 7, 16)), severity) is Outcome.APPLIES

    def test_extension_over_holidays_makes_it_uncertain(self) -> None:
        # Si el 15-IV fuera festivo, la prórroga del art. 30.5 llevaría el final al 16-IV.
        ctx = context(date(2026, 4, 15))
        result = evaluate(
            ctx,
            fecha_hechos=FACTS,
            gravedad="leve",
            notificacion_denuncia=by_post(date(2026, 4, 16)),
            expediente_consultado=True,
            sancion_recurrida="infraccion_original",
        )
        assert result.outcome is Outcome.UNCERTAIN

    def test_without_calendar_it_cannot_apply(self) -> None:
        ctx = context(years=range(2025, 2026))
        result = evaluate(
            ctx,
            fecha_hechos=date(2025, 11, 10),
            gravedad="leve",
            notificacion_denuncia=by_post(date(2026, 6, 1)),
            expediente_consultado=True,
            sancion_recurrida="infraccion_original",
        )
        assert result.outcome is Outcome.UNCERTAIN


class TestInterruption:
    def test_an_earlier_proceeding_interrupts(self) -> None:
        late = by_post(date(2026, 5, 4))
        assert run(late, otras_actuaciones=[date(2026, 3, 2)]) is Outcome.DOES_NOT_APPLY

    def test_failed_attempt_before_the_end_makes_it_uncertain(self) -> None:
        # Qué momento de la notificación interrumpe es una duda abierta.
        notification = by_boe(date(2026, 5, 4), (date(2026, 4, 6), "ausente"))
        assert run(notification) is Outcome.UNCERTAIN

    def test_boe_published_after_the_end(self) -> None:
        assert run(by_boe(date(2026, 4, 20))) is Outcome.APPLIES

    def test_dev_made_available_after_the_end(self) -> None:
        assert run(by_dev(date(2026, 4, 20))) is Outcome.APPLIES

    def test_dev_made_available_before_but_rejected_after(self) -> None:
        assert run(by_dev(date(2026, 4, 10))) is Outcome.UNCERTAIN


class TestUnknownProceedings:
    def test_without_the_file_it_is_only_uncertain(self) -> None:
        late = by_post(date(2026, 5, 4))
        assert run(late, expediente_consultado=False) is Outcome.UNCERTAIN

    def test_unanswered_file_question_is_missing_data(self) -> None:
        result = evaluate(
            fecha_hechos=FACTS,
            gravedad="leve",
            notificacion_denuncia=by_post(date(2026, 5, 4)),
            sancion_recurrida="infraccion_original",
        )
        assert result.outcome is Outcome.MISSING_DATA
        assert result.missing == ("expediente_consultado",)

    def test_in_time_does_not_need_the_file(self) -> None:
        assert run(in_person(FACTS), expediente_consultado=None) is Outcome.DOES_NOT_APPLY

    def test_missing_severity(self) -> None:
        result = evaluate(fecha_hechos=FACTS, notificacion_denuncia=in_person(FACTS))
        assert result.outcome is Outcome.MISSING_DATA
        assert result.missing == ("gravedad",)


class TestReviewRegressions:
    def test_failure_to_identify_does_not_run_from_the_original_facts(self) -> None:
        # C3: la infracción del art. 77.j no se comete el día de los hechos originales.
        late = by_post(date(2026, 7, 20))
        assert run(late, "muy_grave", sancion_recurrida="no_identificar_conductor") is (
            Outcome.UNCERTAIN
        )

    def test_unknown_contested_sanction_blocks_applies(self) -> None:
        result = evaluate(
            fecha_hechos=FACTS,
            gravedad="leve",
            notificacion_denuncia=by_post(date(2026, 5, 4)),
            expediente_consultado=True,
        )
        assert result.outcome is Outcome.MISSING_DATA
        assert result.missing == ("sancion_recurrida",)

    def test_refusal_before_the_boe_interrupts(self) -> None:
        # C1: el rechazo en el domicilio tiene por efectuado el trámite (art. 90.3).
        notification = by_boe(date(2026, 5, 4), (date(2026, 3, 2), "rechazada"))
        assert run(notification) is Outcome.DOES_NOT_APPLY
