"""Validación del modelo de datos del caso (core/trafico/caso.py)."""

from datetime import date
from typing import Any

import pytest
from pydantic import ValidationError

from tests.core.trafico.conftest import by_boe, by_dev, by_post, case


@pytest.mark.parametrize(
    "data",
    [
        {"notificacion_denuncia": {"canal": "dev"}},
        {"notificacion_denuncia": {"canal": "boe"}},
        {"notificacion_denuncia": {"canal": "en_el_acto"}},
        {"notificacion_denuncia": by_boe(date(2026, 3, 1)) | {"canal": "domicilio"}},
        {"notificacion_denuncia": by_dev(date(2026, 3, 5), date(2026, 3, 4))},
        {
            "notificacion_denuncia": by_boe(
                date(2026, 3, 9), (date(2026, 3, 3), "ausente"), (date(2026, 3, 2), "ausente")
            )
        },
        {"fecha_hechos": date(2026, 3, 5), "notificacion_denuncia": by_post(date(2026, 3, 4))},
        {"fecha_hechos": date(2026, 3, 5), "fecha_incoacion": date(2026, 3, 4)},
        {"fecha_resolucion": date(2026, 3, 5), "notificacion_resolucion": date(2026, 3, 4)},
        {"fecha_hechos": date(2026, 3, 5), "otras_actuaciones": [date(2026, 3, 4)]},
        {"identifico_conductor": True},
        {"campo_inventado": 1},
    ],
)
def test_inconsistent_data_is_rejected(data: dict[str, Any]) -> None:
    with pytest.raises(ValidationError):
        case(**data)


def test_unknown_values_stay_unknown() -> None:
    assert case().is_known("gravedad") is False
    assert case(gravedad="leve").is_known("gravedad") is True
