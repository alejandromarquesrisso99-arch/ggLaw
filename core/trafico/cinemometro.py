"""Regla trafico.control_metrologico_cinemometro (art. 83.2 RDL 6/2015).

Alcance limitado: la normativa metrológica (y el anexo IV) no está transcrita en knowledge/.
La regla solo detecta que no consta el control metrológico del instrumento, para pedir que se
acredite; no puede valorar si una verificación que consta estaba vigente.
"""

from pydantic import BaseModel, ConfigDict

from core.reglas import Check, CheckStatus, Evaluation, EvaluationContext, all_required
from core.trafico._util import check, missing
from core.trafico.caso import TrafficCase


class Params(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")


def _flag(condition: str, value: bool | None, name: str, met: str, not_met: str) -> Check:
    if value is None:
        return missing(condition, name)
    return check(
        condition, CheckStatus.MET if value else CheckStatus.NOT_MET, met if value else not_met
    )


def evaluate(params: Params, case: TrafficCase, ctx: EvaluationContext) -> Evaluation:
    speeding = _flag(
        "infraccion_de_velocidad",
        case.speeding,
        "infraccion_velocidad",
        "La infracción es por exceso de velocidad (arts. 76.a o 77.a).",
        "La infracción no es por exceso de velocidad.",
    )
    instrument = _flag(
        "medida_con_instrumento",
        case.measured_by_instrument,
        "medida_con_cinemometro",
        "La velocidad se midió con un cinemómetro, sometido a control metrológico (art. 83.2).",
        "La velocidad no se midió con un instrumento.",
    )
    on_record = case.metrological_control_on_record
    if on_record is None:
        control = missing("control_metrologico_no_acreditado", "consta_control_metrologico")
    elif on_record:
        control = check(
            "control_metrologico_no_acreditado",
            CheckStatus.UNCERTAIN,
            "Consta el control metrológico. ggLaw aún no puede comprobar si estaba vigente: la "
            "normativa de metrología no está transcrita.",
        )
    else:
        control = check(
            "control_metrologico_no_acreditado",
            CheckStatus.MET,
            "No consta el control metrológico del cinemómetro: puedes pedir que se acredite "
            "(art. 83.2 y art. 95.1, proponer pruebas).",
        )
    return all_required([speeding, instrument, control])
