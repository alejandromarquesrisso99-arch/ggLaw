"""trafico.identificacion_conductor: arts. 11.1.a, 77.j, 82 y 93.1 RDL 6/2015."""

from datetime import date
from typing import Any

from core.reglas import Outcome
from tests.core.trafico.conftest import by_boe, by_dev, by_post, evaluator, in_person

evaluate = evaluator("trafico.identificacion_conductor")
NOTIFIED = date(2026, 3, 2)  # lunes; +20 naturales: domingo 22-III, prórroga al lunes 23-III


def outcome(**overrides: Any) -> Outcome:
    identification = {"fecha": date(2026, 3, 16), "incluye_permiso": True, "telematica": True}
    identification.update(overrides.pop("identificacion", {}))
    identification.setdefault("otra_persona", True)
    data: dict[str, Any] = {
        "detencion_vehiculo": False,
        "identifico_conductor": True,
        "identificacion_conductor": identification,
        "notificacion_denuncia": by_post(NOTIFIED),
        "sancion_recurrida": "infraccion_original",
        "infraccion_responsabilidad_titular": False,
    }
    data.update(overrides)
    return evaluate(**data).outcome


def test_identified_another_driver_in_time() -> None:
    assert outcome() is Outcome.APPLIES


def test_sanctioned_for_not_identifying_after_identifying() -> None:
    assert outcome(sancion_recurrida="no_identificar_conductor") is Outcome.APPLIES


def test_identified_oneself() -> None:
    assert outcome(identificacion={"otra_persona": False}) is Outcome.DOES_NOT_APPLY


def test_vehicle_stopped() -> None:
    assert outcome(detencion_vehiculo=True, notificacion_denuncia=in_person(NOTIFIED)) is (
        Outcome.DOES_NOT_APPLY
    )


def test_no_identification() -> None:
    assert outcome(identifico_conductor=False, identificacion_conductor=None) is (
        Outcome.DOES_NOT_APPLY
    )


def test_identification_without_licence() -> None:
    assert outcome(identificacion={"incluye_permiso": False}) is Outcome.DOES_NOT_APPLY


def test_last_day_extended_to_monday() -> None:
    assert outcome(identificacion={"fecha": date(2026, 3, 23)}) is Outcome.APPLIES


def test_late_identification() -> None:
    assert outcome(identificacion={"fecha": date(2026, 3, 24)}) is Outcome.DOES_NOT_APPLY


def test_dev_rejection_starts_the_period() -> None:
    # Puesta a disposición el 2-III sin acceso: rechazo el 12-III, plazo hasta el 1-IV.
    assert (
        outcome(notificacion_denuncia=by_dev(NOTIFIED), identificacion={"fecha": date(2026, 4, 1)})
        is Outcome.APPLIES
    )


def test_dev_notification_with_paper_identification_is_uncertain() -> None:
    assert (
        outcome(
            notificacion_denuncia=by_dev(NOTIFIED, NOTIFIED), identificacion={"telematica": False}
        )
        is Outcome.UNCERTAIN
    )


def test_boe_notification_day_is_uncertain() -> None:
    # Publicado el miércoles 4-III: practicada el 24-III o el 25-III (art. 91, duda abierta);
    # el plazo para identificar acaba el 13-IV o el 14-IV.
    boe = by_boe(date(2026, 3, 4))
    assert outcome(notificacion_denuncia=boe, identificacion={"fecha": date(2026, 4, 13)}) is (
        Outcome.APPLIES
    )
    assert outcome(notificacion_denuncia=boe, identificacion={"fecha": date(2026, 4, 14)}) is (
        Outcome.UNCERTAIN
    )
    assert outcome(notificacion_denuncia=boe, identificacion={"fecha": date(2026, 4, 15)}) is (
        Outcome.DOES_NOT_APPLY
    )


def test_missing_sanction_type() -> None:
    result = evaluate(
        detencion_vehiculo=False,
        identifico_conductor=True,
        identificacion_conductor={
            "fecha": date(2026, 3, 16),
            "incluye_permiso": True,
            "telematica": True,
            "otra_persona": True,
        },
        notificacion_denuncia=by_post(NOTIFIED),
    )
    assert result.outcome is Outcome.MISSING_DATA
    assert result.missing == ("sancion_recurrida",)


def test_owner_is_always_liable_for_vehicle_condition_offences() -> None:
    # C2: art. 82.f (p. ej., inspección técnica caducada).
    assert outcome(infraccion_responsabilidad_titular=True) is Outcome.DOES_NOT_APPLY
    assert outcome(infraccion_responsabilidad_titular=None) is Outcome.MISSING_DATA
    # No importa si se recurre la sanción por no identificar.
    assert (
        outcome(
            sancion_recurrida="no_identificar_conductor", infraccion_responsabilidad_titular=None
        )
        is Outcome.APPLIES
    )


def test_refusal_at_home_starts_the_period_before_the_boe() -> None:
    # C1: rechazo el 2-III y edicto el 20-III: el plazo acaba el 23-III, no a finales de abril.
    notification = by_boe(date(2026, 3, 20), (NOTIFIED, "rechazada"))
    late = {"fecha": date(2026, 4, 15)}
    assert outcome(notificacion_denuncia=notification, identificacion=late) is (
        Outcome.DOES_NOT_APPLY
    )


def test_unaccessed_dev_followed_by_boe_is_uncertain() -> None:
    # Pudo haber imposibilidad técnica del acceso (art. 90.2): manda la cota del BOE.
    notification = {**by_dev(NOTIFIED), "canal": "boe", "boe_publicacion": date(2026, 3, 20)}
    late = {"fecha": date(2026, 4, 15)}
    assert outcome(notificacion_denuncia=notification, identificacion=late) is Outcome.UNCERTAIN
