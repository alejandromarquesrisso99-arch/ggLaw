"""trafico.control_metrologico_cinemometro: art. 83.2 RDL 6/2015 (alcance limitado)."""

import pytest

from core.reglas import Outcome
from tests.core.trafico.conftest import evaluator

evaluate = evaluator("trafico.control_metrologico_cinemometro")


@pytest.mark.parametrize(
    ("speeding", "instrument", "on_record", "expected"),
    [
        (True, True, False, Outcome.APPLIES),
        (True, True, True, Outcome.UNCERTAIN),
        (False, None, None, Outcome.DOES_NOT_APPLY),
        (True, False, None, Outcome.DOES_NOT_APPLY),
        (True, True, None, Outcome.MISSING_DATA),
    ],
)
def test_outcomes(
    speeding: bool, instrument: bool | None, on_record: bool | None, expected: Outcome
) -> None:
    result = evaluate(
        infraccion_velocidad=speeding,
        medida_con_cinemometro=instrument,
        consta_control_metrologico=on_record,
    )
    assert result.outcome is expected
