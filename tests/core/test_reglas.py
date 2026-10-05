"""Tests de core/reglas.py y de la integridad de rules/: cada regla está en borrador, cita
solo artículos transcritos en knowledge/ y declara lo que su evaluador usa."""

from pathlib import Path

import pytest

from core.reglas import (
    Check,
    CheckStatus,
    Outcome,
    RuleDataError,
    all_required,
    check_legal_basis,
    load_rule_definitions,
)
from core.trafico import EVALUATORS, load_traffic_rules
from core.trafico.caso import CASE_DATA_NAMES

RULES = load_rule_definitions()
EXPECTED_RULES = {
    "trafico.prescripcion_infraccion",
    "trafico.caducidad_procedimiento",
    "trafico.defecto_notificacion_denuncia",
    "trafico.identificacion_conductor",
    "trafico.control_metrologico_cinemometro",
}

VALID_RULE = """\
id: trafico.ejemplo
titulo: Ejemplo
ambito: trafico
estado: borrador
fundamento:
  - norma: RDL 6/2015
    articulo: 112
    knowledge: knowledge/rdl-6-2015-regimen-sancionador.md
condiciones:
  - id: una
    descripcion: Una condición.
    fundamento: RDL 6/2015, art. 112
datos_necesarios: [fecha_hechos]
parrafo_tipo: null
notas: ""
"""


def write_rule(base: Path, text: str, name: str = "ejemplo") -> Path:
    path = base / "trafico" / f"{name}.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return base


class TestRepositoryRules:
    def test_the_five_traffic_rules_exist(self) -> None:
        assert set(RULES) == EXPECTED_RULES

    @pytest.mark.parametrize("rule_id", sorted(EXPECTED_RULES))
    def test_new_rules_are_drafts(self, rule_id: str) -> None:
        # Solo Alex o un abogado revisor cambian el estado (CLAUDE.md).
        assert RULES[rule_id].estado == "borrador"

    @pytest.mark.parametrize("rule_id", sorted(EXPECTED_RULES))
    def test_every_cited_article_is_transcribed_in_knowledge(self, rule_id: str) -> None:
        check_legal_basis(RULES[rule_id])

    @pytest.mark.parametrize("rule_id", sorted(EXPECTED_RULES))
    def test_declared_data_exist_in_the_case_model(self, rule_id: str) -> None:
        assert set(RULES[rule_id].datos_necesarios) <= CASE_DATA_NAMES

    def test_rules_and_evaluators_match(self) -> None:
        assert {rule.definition.id for rule in load_traffic_rules()} == set(EVALUATORS)


class TestLoader:
    def test_loads_a_valid_rule(self, tmp_path: Path) -> None:
        rules = load_rule_definitions(write_rule(tmp_path, VALID_RULE))
        assert set(rules) == {"trafico.ejemplo"}

    def test_id_must_match_path(self, tmp_path: Path) -> None:
        with pytest.raises(RuleDataError, match="id debe ser"):
            load_rule_definitions(write_rule(tmp_path, VALID_RULE, name="otro"))

    @pytest.mark.parametrize(
        ("old", "new"),
        [
            ("estado: borrador", "estado: aprobado"),
            ('notas: ""', 'notas: ""\nextra: 1'),
            ("datos_necesarios: [fecha_hechos]", "datos_necesarios: []"),
            ("  - id: una", "  - id: una\n    descripcion: x\n    fundamento: x\n  - id: una"),
        ],
    )
    def test_rejects_invalid_rules(self, tmp_path: Path, old: str, new: str) -> None:
        with pytest.raises(RuleDataError):
            load_rule_definitions(write_rule(tmp_path, VALID_RULE.replace(old, new, 1)))

    def test_untranscribed_article_is_rejected(self, tmp_path: Path) -> None:
        rule = load_rule_definitions(
            write_rule(tmp_path, VALID_RULE.replace("articulo: 112", "articulo: 999"))
        )["trafico.ejemplo"]
        with pytest.raises(RuleDataError, match="no está transcrito"):
            check_legal_basis(rule)

    def test_missing_knowledge_file_is_rejected(self, tmp_path: Path) -> None:
        rule = load_rule_definitions(
            write_rule(tmp_path, VALID_RULE.replace("rdl-6-2015-regimen", "no-existe"))
        )["trafico.ejemplo"]
        with pytest.raises(RuleDataError, match="no existe"):
            check_legal_basis(rule)

    def test_traffic_rule_without_evaluator_is_rejected(self, tmp_path: Path) -> None:
        with pytest.raises(RuleDataError, match="sin evaluador"):
            load_traffic_rules(write_rule(tmp_path, VALID_RULE))


def check(status: CheckStatus) -> Check:
    return Check(condition="c", status=status, detail="")


class TestAllRequired:
    @pytest.mark.parametrize(
        ("statuses", "expected"),
        [
            ([CheckStatus.MET, CheckStatus.MET], Outcome.APPLIES),
            ([CheckStatus.MET, CheckStatus.UNCERTAIN], Outcome.UNCERTAIN),
            ([CheckStatus.UNCERTAIN, CheckStatus.MISSING_DATA], Outcome.MISSING_DATA),
            ([CheckStatus.MISSING_DATA, CheckStatus.NOT_MET], Outcome.DOES_NOT_APPLY),
        ],
    )
    def test_a_failed_condition_wins_then_missing_data_then_doubt(
        self, statuses: list[CheckStatus], expected: Outcome
    ) -> None:
        assert all_required(check(s) for s in statuses).outcome is expected
