"""RFC 0004 §1.4/§1.5 — o grupo atômico, fora de qualquer documento que o carregue.

Estes testes exercitam o módulo neutro diretamente. É onde a invariante de
**origem única do exportador** (§1.5) e a de **proveniência** (§1.4) ficam
fixadas independentemente de onde os grupos estejam declarados — o manifesto
global foi aposentado na fase 1 da RFC 0006, e a propriedade não podia sair
junto com ele.
"""

from __future__ import annotations

import pytest
from pydantic import ValidationError
from substituicao_schema import (
    GrupoSubstituicao,
    id_da_ref,
    ref_de_regra_legada,
    ref_de_unidade_auditada,
    selecionar_origem_operacional,
    validar_grupos,
)

_DECISAO = {
    "decidido_por": "auditor",
    "decidido_em": "2026-01-01",
    "justificativa": "grupo completo",
    "fonte": "SEI 0000",
}


class _Unidade:
    """Stand-in mínimo com a superfície que o módulo lê de uma RegraProposta."""

    def __init__(self, doc_id: str, origens: tuple[str, ...], estado: str = "elaboracao") -> None:
        self.doc_id = doc_id
        self.origens_legacy = origens
        self.estado_proposta = estado


def _grupo(**campos: object) -> GrupoSubstituicao:
    base: dict[str, object] = {
        "grupo": "g",
        "origens_legacy": ("/regras/regra-0001.md",),
        "destinos_propostos": ("/regras-propostas/regras/unidade-a.md",),
    }
    base.update(campos)
    return GrupoSubstituicao.model_validate(base)


def test_ref_and_id_round_trip() -> None:
    """As duas grafias de identidade convertem uma na outra sem perda."""
    assert id_da_ref(ref_de_regra_legada("regra-0022")) == "regra-0022"
    assert id_da_ref(ref_de_unidade_auditada("invalidez-acidente")) == "invalidez-acidente"
    assert ref_de_regra_legada("regra-0022") != ref_de_unidade_auditada("regra-0022")


def test_origin_selection_defaults_to_legacy() -> None:
    """Sem grupo ativo, a linha legada continua sendo a origem operacional."""
    assert selecionar_origem_operacional("regra-0001", []) == "legado"
    assert selecionar_origem_operacional("regra-0001", [_grupo()]) == "legado"


def test_only_an_active_group_switches_the_origin() -> None:
    """RFC 0004 §1.5 — nenhuma unidade isolada substitui uma origem."""
    ativo = _grupo(estado_grupo="ativo", decisao_completude=_DECISAO)
    assert selecionar_origem_operacional("regra-0001", [ativo]) == "auditado"
    assert selecionar_origem_operacional("regra-0002", [ativo]) == "legado"


def test_activation_without_a_decision_is_rejected_by_the_contract() -> None:
    """Ativar é ato humano registrado, não um campo que se liga sozinho."""
    with pytest.raises(ValidationError, match="decisao_completude"):
        _grupo(estado_grupo="ativo")


def test_a_group_needs_at_least_one_origin_and_one_destination() -> None:
    """Substituição sem sucessora é `revoga`; introdução sem antecessora é `introduz`."""
    with pytest.raises(ValidationError):
        _grupo(origens_legacy=())
    with pytest.raises(ValidationError):
        _grupo(destinos_propostos=())


def test_provenance_mismatch_is_reported_in_both_directions() -> None:
    """A origem que o grupo declara e a que o destino reconhece têm de ser a mesma."""
    unidade = _Unidade("unidade-a", ("regra-0002",))

    codigos = {
        v.code
        for v in validar_grupos(
            [_grupo()], unidades=[unidade], refs_legadas=frozenset({"/regras/regra-0001.md"})
        )
    }

    assert "P15_PROVENIENCIA_DIVERGENTE" in codigos
    assert "P15_PROVENIENCIA_INCOMPLETA" in codigos


def test_provenance_is_checked_while_the_group_is_still_inactive() -> None:
    """Esperar a ativação para reportar uma divergência é descobri-la no pior momento."""
    unidade = _Unidade("unidade-a", ("regra-0002",))
    grupo = _grupo()

    assert grupo.estado_grupo == "inativo"
    assert validar_grupos([grupo], unidades=[unidade], refs_legadas=frozenset({"/regras/regra-0001.md"}))


def test_matching_provenance_reports_nothing() -> None:
    """O caso bom não gera ruído."""
    unidade = _Unidade("unidade-a", ("regra-0001",))

    assert (
        validar_grupos([_grupo()], unidades=[unidade], refs_legadas=frozenset({"/regras/regra-0001.md"}))
        == []
    )


def test_an_unknown_destination_does_not_produce_a_spurious_provenance_error() -> None:
    """Comparar contra uma unidade que não se consegue ler empilharia erro derivado."""
    codigos = {
        v.code
        for v in validar_grupos([_grupo()], unidades=[], refs_legadas=frozenset({"/regras/regra-0001.md"}))
    }

    assert "P15_DESTINO_INEXISTENTE" in codigos
    assert "P15_PROVENIENCIA_DIVERGENTE" not in codigos


def test_duplicate_group_ids_are_reported() -> None:
    """Dois grupos com o mesmo id tornam ambíguo o que um rollback reverteria."""
    unidade = _Unidade("unidade-a", ("regra-0001",))

    codigos = {
        v.code
        for v in validar_grupos(
            [_grupo(), _grupo()], unidades=[unidade], refs_legadas=frozenset({"/regras/regra-0001.md"})
        )
    }

    assert "P15_GRUPO_DUPLICADO" in codigos
    assert "P15_DESTINO_EM_GRUPOS_CONFLITANTES" in codigos


def test_two_active_groups_claiming_the_same_origin_are_reported() -> None:
    """Uma origem só pode ter uma substituição ativa — senão o exportador não tem origem única."""
    unidade_a = _Unidade("unidade-a", ("regra-0001",), estado="deployable")
    unidade_b = _Unidade("unidade-b", ("regra-0001",), estado="deployable")
    grupos = [
        _grupo(grupo="g1", estado_grupo="ativo", decisao_completude=_DECISAO),
        _grupo(
            grupo="g2",
            destinos_propostos=("/regras-propostas/regras/unidade-b.md",),
            estado_grupo="ativo",
            decisao_completude=_DECISAO,
        ),
    ]

    codigos = {
        v.code
        for v in validar_grupos(
            grupos, unidades=[unidade_a, unidade_b], refs_legadas=frozenset({"/regras/regra-0001.md"})
        )
    }

    assert "P15_ORIGEM_EM_GRUPOS_ATIVOS" in codigos


def test_an_active_group_with_a_non_deployable_destination_is_reported() -> None:
    """Ativação é atômica: basta um destino em elaboração para travar o grupo."""
    unidade = _Unidade("unidade-a", ("regra-0001",), estado="elaboracao")

    codigos = {
        v.code
        for v in validar_grupos(
            [_grupo(estado_grupo="ativo", decisao_completude=_DECISAO)],
            unidades=[unidade],
            refs_legadas=frozenset({"/regras/regra-0001.md"}),
        )
    }

    assert "P15_GRUPO_PARCIAL" in codigos


@pytest.mark.parametrize("campo_em_branco", sorted(_DECISAO))
def test_decisao_completude_rejects_whitespace_only_field(campo_em_branco: str) -> None:
    """min_length=1 alone accepts "   " — normalization has to actually strip it."""
    valores = {**_DECISAO, campo_em_branco: "   "}
    with pytest.raises(ValidationError):
        _grupo(estado_grupo="ativo", decisao_completude=valores)


def test_grupo_id_rejects_whitespace_only() -> None:
    """A grupo id that's only whitespace must not pass min_length=1 by accident."""
    with pytest.raises(ValidationError):
        _grupo(grupo="   ")


def test_duplicate_origens_legacy_are_rejected() -> None:
    """Two identical origens_legacy entries must be rejected, not silently deduplicated."""
    with pytest.raises(ValidationError, match="duplicates"):
        _grupo(origens_legacy=("/regras/regra-0001.md", "/regras/regra-0001.md"))


def test_duplicate_destinos_propostos_are_rejected() -> None:
    """Two identical destinos_propostos entries must be rejected, not silently deduplicated."""
    with pytest.raises(ValidationError, match="duplicates"):
        _grupo(
            destinos_propostos=(
                "/regras-propostas/regras/unidade-a.md",
                "/regras-propostas/regras/unidade-a.md",
            )
        )


def test_origem_with_the_wrong_prefix_is_rejected_even_with_a_real_basename() -> None:
    """A ref carrying the wrong prefix but a real basename must not sneak past existence checks.

    `id_da_ref` strips any prefix down to the basename, so a malformed
    `/regras-propostas/regras/regra-0001.md` — same basename as a real
    legacy id, wrong bundle's prefix — has to be rejected by the model
    itself, before it ever reaches provenance/existence comparisons.
    """
    with pytest.raises(ValidationError):
        _grupo(origens_legacy=("/regras-propostas/regras/regra-0001.md",))


def test_destino_with_the_wrong_prefix_is_rejected_even_with_a_real_basename() -> None:
    """A destino ref with the legacy-regra prefix but a real unit basename must be rejected too."""
    with pytest.raises(ValidationError):
        _grupo(destinos_propostos=("/regras/unidade-a.md",))


def test_an_inactive_group_carrying_a_decision_is_reported() -> None:
    """Rollback limpa a decisão; deixá-la registra uma ativação que não existe."""
    unidade = _Unidade("unidade-a", ("regra-0001",))

    codigos = {
        v.code
        for v in validar_grupos(
            [_grupo(decisao_completude=_DECISAO)],
            unidades=[unidade],
            refs_legadas=frozenset({"/regras/regra-0001.md"}),
        )
    }

    assert "P15_DECISAO_SEM_ATIVACAO" in codigos
