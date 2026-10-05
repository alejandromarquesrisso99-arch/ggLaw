"""trafico.defecto_notificacion_denuncia: arts. 90.1, 90.3 y 91 RDL 6/2015
(knowledge/rdl-6-2015.md)."""

from datetime import date
from typing import Any

from core.reglas import Outcome
from tests.core.trafico.conftest import by_boe, by_dev, by_post, context, evaluator

evaluate = evaluator("trafico.defecto_notificacion_denuncia")
PUBLISHED = date(2026, 6, 15)
MON, TUE, THU, FRI = date(2026, 6, 1), date(2026, 6, 2), date(2026, 6, 4), date(2026, 6, 5)


def outcome(notification: dict[str, Any], *, has_dev: bool | None = False, **data: Any) -> Outcome:
    data.setdefault("expediente_consultado", True)
    return evaluate(notificacion_denuncia=notification, dev_asignada=has_dev, **data).outcome


def test_only_edictal_notifications_are_evaluated() -> None:
    assert outcome(by_post(MON)) is Outcome.DOES_NOT_APPLY


def test_two_timely_attempts_are_correct() -> None:
    assert outcome(by_boe(PUBLISHED, (MON, "ausente"), (TUE, "ausente"))) is Outcome.DOES_NOT_APPLY


def test_boe_without_any_attempt() -> None:
    assert outcome(by_boe(PUBLISHED)) is Outcome.APPLIES


def test_boe_after_a_single_attempt() -> None:
    assert outcome(by_boe(PUBLISHED, (MON, "ausente"))) is Outcome.APPLIES


def test_single_attempt_with_unknown_addressee_is_uncertain() -> None:
    assert outcome(by_boe(PUBLISHED, (MON, "desconocido"))) is Outcome.UNCERTAIN


def test_refusal_counts_as_notified() -> None:
    assert outcome(by_boe(PUBLISHED, (MON, "rechazada"))) is Outcome.DOES_NOT_APPLY


def test_dev_holder_without_dev_attempt() -> None:
    notification = by_boe(PUBLISHED, (MON, "ausente"), (TUE, "ausente"))
    assert outcome(notification, has_dev=True) is Outcome.APPLIES


def test_dev_attempted_before_boe() -> None:
    notification = {**by_dev(MON), "canal": "boe", "boe_publicacion": PUBLISHED}
    assert outcome(notification, has_dev=True) is Outcome.DOES_NOT_APPLY


def test_unknown_dev_is_missing_only_when_it_matters() -> None:
    timely = by_boe(PUBLISHED, (MON, "ausente"), (TUE, "ausente"))
    assert outcome(timely, has_dev=None) is Outcome.MISSING_DATA
    # Sin ningún intento hay defecto con o sin DEV.
    assert outcome(by_boe(PUBLISHED), has_dev=None) is Outcome.APPLIES


class TestSecondAttempt:
    def test_within_three_days(self) -> None:
        assert (
            outcome(by_boe(PUBLISHED, (MON, "ausente"), (THU, "ausente"))) is Outcome.DOES_NOT_APPLY
        )

    def test_fourth_natural_day_is_within_three_business_days_only(self) -> None:
        # Lunes 1-VI + 3 naturales = jueves 4; + 3 hábiles = jueves 4: el viernes 5 es tarde
        # en ambas lecturas; con un festivo el miércoles, solo en la de naturales.
        late = by_boe(PUBLISHED, (MON, "ausente"), (FRI, "ausente"))
        assert outcome(late) is Outcome.APPLIES
        holiday = context(date(2026, 6, 3))
        result = evaluate(
            holiday,
            notificacion_denuncia=late,
            dev_asignada=False,
            expediente_consultado=True,
        )
        assert result.outcome is Outcome.UNCERTAIN

    def test_same_day_attempts_are_uncertain(self) -> None:
        assert outcome(by_boe(PUBLISHED, (MON, "ausente"), (MON, "ausente"))) is Outcome.UNCERTAIN


class TestFileReviewed:
    def test_defect_without_the_file_is_uncertain(self) -> None:
        assert outcome(by_boe(PUBLISHED), expediente_consultado=False) is Outcome.UNCERTAIN

    def test_defect_with_unanswered_file_question(self) -> None:
        assert outcome(by_boe(PUBLISHED), expediente_consultado=None) is Outcome.MISSING_DATA
