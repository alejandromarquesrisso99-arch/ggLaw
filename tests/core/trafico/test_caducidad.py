"""trafico.caducidad_procedimiento: art. 112.3 RDL 6/2015 (un año desde la iniciación), con
las salvedades de los arts. 94 (pago) y 95.4 (denuncia como acto resolutorio)."""

from datetime import date
from typing import Any

import pytest

from core.reglas import Outcome
from tests.core.trafico.conftest import by_post, context, evaluator, in_person

evaluate = evaluator("trafico.caducidad_procedimiento")
FACTS = date(2025, 3, 3)
INITIATED = date(2025, 3, 10)  # incoación; +1 año: martes 10-III-2026


def ordinary(**overrides: Any) -> dict[str, Any]:
    """Grave con puntos notificada después: sin alegaciones no surte efecto de resolución."""
    data: dict[str, Any] = {
        "fecha_hechos": FACTS,
        "gravedad": "grave",
        "detrae_puntos": True,
        "notificacion_denuncia": by_post(date(2025, 3, 20)),
        "fecha_incoacion": INITIATED,
        "pago_voluntario": False,
        "alegaciones_presentadas": True,
        "procedimiento_suspendido": False,
        "expediente_consultado": True,
    }
    data.update(overrides)
    return data


def outcome(**overrides: Any) -> Outcome:
    return evaluate(**ordinary(**overrides)).outcome


class TestDeadline:
    def test_resolution_well_within_the_year(self) -> None:
        resolved = {
            "fecha_resolucion": date(2025, 9, 1),
            "notificacion_resolucion": date(2025, 9, 5),
        }
        assert outcome(**resolved) is Outcome.DOES_NOT_APPLY

    def test_resolution_dictated_after_the_year(self) -> None:
        resolved = {
            "fecha_resolucion": date(2026, 3, 12),
            "notificacion_resolucion": date(2026, 3, 16),
        }
        assert outcome(**resolved) is Outcome.APPLIES

    def test_dictated_in_time_but_notified_late_is_uncertain(self) -> None:
        resolved = {
            "fecha_resolucion": date(2026, 3, 2),
            "notificacion_resolucion": date(2026, 3, 20),
        }
        assert outcome(**resolved) is Outcome.UNCERTAIN

    def test_resolution_on_the_anniversary_is_uncertain(self) -> None:
        resolved = {
            "fecha_resolucion": date(2026, 3, 10),
            "notificacion_resolucion": date(2026, 3, 10),
        }
        assert outcome(**resolved) is Outcome.UNCERTAIN

    def test_resolution_without_notification_date(self) -> None:
        result = evaluate(**ordinary(fecha_resolucion=date(2026, 3, 2)))
        assert result.outcome is Outcome.MISSING_DATA
        assert result.missing == ("notificacion_resolucion",)

    def test_no_resolution_yet_and_still_in_time(self) -> None:
        result = evaluate(context(today=date(2025, 12, 1)), **ordinary())
        assert result.outcome is Outcome.DOES_NOT_APPLY

    def test_no_resolution_after_the_year(self) -> None:
        assert outcome() is Outcome.APPLIES

    def test_no_resolution_without_seeing_the_file_is_uncertain(self) -> None:
        assert outcome(expediente_consultado=False) is Outcome.UNCERTAIN


class TestInitiation:
    def test_in_person_complaint_initiates(self) -> None:
        # Art. 86.2: la denuncia notificada en el acto inicia el procedimiento.
        data = ordinary(notificacion_denuncia=in_person(FACTS), fecha_incoacion=None)
        data.update(fecha_resolucion=date(2026, 3, 5), notificacion_resolucion=date(2026, 3, 9))
        assert evaluate(**data).outcome is Outcome.APPLIES

    def test_unknown_initiation_asks_for_it_when_it_matters(self) -> None:
        resolved = {
            "fecha_resolucion": date(2026, 3, 12),
            "notificacion_resolucion": date(2026, 3, 16),
        }
        result = evaluate(**ordinary(fecha_incoacion=None, **resolved))
        assert result.outcome is Outcome.MISSING_DATA
        assert result.missing == ("fecha_incoacion",)

    def test_unknown_initiation_still_decides_clear_cases(self) -> None:
        # La incoación no puede ser posterior a la notificación de la denuncia (20-III-2025).
        resolved = {
            "fecha_resolucion": date(2026, 6, 1),
            "notificacion_resolucion": date(2026, 6, 3),
        }
        assert outcome(fecha_incoacion=None, **resolved) is Outcome.APPLIES


class TestExclusions:
    def test_payment_ends_the_procedure(self) -> None:
        assert outcome(pago_voluntario=True) is Outcome.DOES_NOT_APPLY

    @pytest.mark.parametrize(
        ("severity", "points", "notification"),
        [
            ("leve", False, by_post(date(2025, 3, 20))),
            ("grave", False, by_post(date(2025, 3, 20))),
            ("grave", True, in_person(FACTS)),
            ("muy_grave", True, in_person(FACTS)),
        ],
    )
    def test_complaint_as_resolution_without_allegations(
        self, severity: str, points: bool, notification: dict[str, Any]
    ) -> None:
        data = ordinary(
            gravedad=severity,
            detrae_puntos=points,
            notificacion_denuncia=notification,
            alegaciones_presentadas=False,
            fecha_incoacion=None,
        )
        assert evaluate(**data).outcome is Outcome.DOES_NOT_APPLY

    @pytest.mark.parametrize(("severity", "points"), [("grave", True), ("muy_grave", False)])
    def test_without_allegations_some_cases_still_need_a_resolution(
        self, severity: str, points: bool
    ) -> None:
        data = ordinary(gravedad=severity, detrae_puntos=points, alegaciones_presentadas=False)
        assert evaluate(**data).outcome is Outcome.APPLIES

    def test_points_unknown_when_they_matter(self) -> None:
        result = evaluate(**ordinary(detrae_puntos=None, alegaciones_presentadas=False))
        assert result.outcome is Outcome.MISSING_DATA
        assert result.missing == ("detrae_puntos",)

    def test_suspension_makes_it_uncertain(self) -> None:
        assert outcome(procedimiento_suspendido=True) is Outcome.UNCERTAIN

    def test_unknown_suspension_is_missing_data(self) -> None:
        result = evaluate(**ordinary(procedimiento_suspendido=None))
        assert result.outcome is Outcome.MISSING_DATA
        assert "procedimiento_suspendido" in result.missing
