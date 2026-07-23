"""RFC 0004 §1.4/§1.5/§14 — substitution-group atomicity, rollback and origin selection."""

from __future__ import annotations

from bundle import Bundle, Regra
from manifesto_substituicao import (
    DecisaoCompletude,
    GrupoSubstituicao,
    ManifestoSubstituicao,
    check_nenhum_grupo_ativo_em_producao,
    selecionar_origem_operacional,
    validate_manifesto,
)
from regra_schema import blank_frontmatter
from unidade_auditada_schema import UnidadeAuditada

_DECISAO_COMPLETA = DecisaoCompletude(
    decidido_por="franklinbaldo",
    decidido_em="2026-07-23",
    justificativa="ambas as faces de 0022 chegaram a deployable",
    fonte="SEI 0001/2026",
)


def _legacy_bundle(*regra_ids: str) -> Bundle:
    return Bundle(regras=tuple(Regra(doc_id=rid, frontmatter=blank_frontmatter()) for rid in regra_ids))


def _unidade(doc_id: str, *, estado_unidade: str, origens_legacy: list[str]) -> UnidadeAuditada:
    return UnidadeAuditada(
        doc_id=doc_id,
        frontmatter={
            "type": "UnidadeAuditada",
            "id": doc_id,
            "schema_version": 1,
            "estado_unidade": estado_unidade,
            "origens_legacy": origens_legacy,
        },
    )


def _grupo(**overrides: object) -> GrupoSubstituicao:
    defaults: dict[str, object] = {
        "grupo": "substituicao-regra-0022",
        "origens_legacy": ["regra-0022"],
        "destinos_auditados": ["invalidez-acidente", "invalidez-doenca"],
        "estado_grupo": "inativo",
        "decisao_completude": None,
    }
    defaults.update(overrides)
    return GrupoSubstituicao(**defaults)


def test_group_with_one_deployable_and_one_preview_destino_cannot_validly_activate() -> None:
    """A group can't reach `estado_grupo: ativo` while any destino is still preview/elaboracao.

    Declaring it ativo anyway is itself the invalid state `validate_manifesto`
    exists to catch (`MANIFESTO_GRUPO_PARCIAL`) — CI would block this
    manifesto from ever being committed, so the honest modeling keeps the
    group `inativo` until every destino is deployable, and the exporter
    invariant (`selecionar_origem_operacional`) keeps the legacy origin
    operational for exactly that (valid) state.
    """
    unidades = [
        _unidade("invalidez-acidente", estado_unidade="deployable", origens_legacy=["regra-0022"]),
        _unidade("invalidez-doenca", estado_unidade="preview", origens_legacy=["regra-0022"]),
    ]
    grupo_declarado_ativo = _grupo(estado_grupo="ativo", decisao_completude=_DECISAO_COMPLETA)
    manifesto_invalido = ManifestoSubstituicao(schema_version=1, grupos=[grupo_declarado_ativo])
    violations = validate_manifesto(manifesto_invalido, unidades, _legacy_bundle("regra-0022"))
    assert any(v.code == "MANIFESTO_GRUPO_PARCIAL" for v in violations)

    grupo_honesto = _grupo(estado_grupo="inativo", decisao_completude=None)
    manifesto_honesto = ManifestoSubstituicao(schema_version=1, grupos=[grupo_honesto])
    assert validate_manifesto(manifesto_honesto, unidades, _legacy_bundle("regra-0022")) == []
    assert selecionar_origem_operacional("regra-0022", manifesto_honesto) == "legado"


def test_incomplete_active_group_fails_even_if_all_destinos_are_deployable() -> None:
    """An active group without a recorded decisao_completude fails, even if complete otherwise."""
    unidades = [_unidade("invalidez-a", estado_unidade="deployable", origens_legacy=["regra-0022"])]
    grupo = _grupo(destinos_auditados=["invalidez-a"], estado_grupo="ativo", decisao_completude=None)
    manifesto = ManifestoSubstituicao(schema_version=1, grupos=[grupo])

    violations = validate_manifesto(manifesto, unidades, _legacy_bundle("regra-0022"))

    assert any(v.code == "MANIFESTO_DECISAO_INCOMPLETA" for v in violations)


def test_fully_complete_active_group_passes() -> None:
    """A structurally complete active group passes and selects the audited origin."""
    unidades = [_unidade("invalidez-a", estado_unidade="deployable", origens_legacy=["regra-0022"])]
    grupo = _grupo(
        destinos_auditados=["invalidez-a"], estado_grupo="ativo", decisao_completude=_DECISAO_COMPLETA
    )
    manifesto = ManifestoSubstituicao(schema_version=1, grupos=[grupo])

    assert validate_manifesto(manifesto, unidades, _legacy_bundle("regra-0022")) == []
    assert selecionar_origem_operacional("regra-0022", manifesto) == "auditado"


def test_origin_in_two_active_groups_fails() -> None:
    """The same legacy origin cannot be claimed by two active groups."""
    unidades = [
        _unidade("invalidez-a", estado_unidade="deployable", origens_legacy=["regra-0022"]),
        _unidade("invalidez-b", estado_unidade="deployable", origens_legacy=["regra-0022"]),
    ]
    grupo_a = _grupo(
        grupo="grupo-a",
        destinos_auditados=["invalidez-a"],
        estado_grupo="ativo",
        decisao_completude=_DECISAO_COMPLETA,
    )
    grupo_b = _grupo(
        grupo="grupo-b",
        destinos_auditados=["invalidez-b"],
        estado_grupo="ativo",
        decisao_completude=_DECISAO_COMPLETA,
    )
    manifesto = ManifestoSubstituicao(schema_version=1, grupos=[grupo_a, grupo_b])

    violations = validate_manifesto(manifesto, unidades, _legacy_bundle("regra-0022"))

    assert any(v.code == "MANIFESTO_ORIGEM_GRUPOS_ATIVOS_CONFLITANTES" for v in violations)


def test_rollback_to_inactive_restores_the_legacy_origin_and_must_clear_the_decision() -> None:
    """Rollback to inativo must also clear decisao_completude."""
    unidades = [_unidade("invalidez-a", estado_unidade="deployable", origens_legacy=["regra-0022"])]
    # A rollback that flips estado_grupo back to inativo but forgets to clear
    # decisao_completude must itself be flagged — RFC 0004: "nunca edita os
    # campos silenciosamente".
    grupo_rollback_incompleto = _grupo(
        destinos_auditados=["invalidez-a"], estado_grupo="inativo", decisao_completude=_DECISAO_COMPLETA
    )
    manifesto = ManifestoSubstituicao(schema_version=1, grupos=[grupo_rollback_incompleto])

    violations = validate_manifesto(manifesto, unidades, _legacy_bundle("regra-0022"))

    assert any(v.code == "MANIFESTO_DECISAO_SEM_ATIVACAO" for v in violations)
    assert selecionar_origem_operacional("regra-0022", manifesto) == "legado"

    grupo_rollback_correto = _grupo(
        destinos_auditados=["invalidez-a"], estado_grupo="inativo", decisao_completude=None
    )
    manifesto_correto = ManifestoSubstituicao(schema_version=1, grupos=[grupo_rollback_correto])
    assert validate_manifesto(manifesto_correto, unidades, _legacy_bundle("regra-0022")) == []
    assert selecionar_origem_operacional("regra-0022", manifesto_correto) == "legado"


def test_no_isolated_unit_replaces_an_origin() -> None:
    """A deployable unit with no manifest entry at all must never be treated as operational."""
    manifesto = ManifestoSubstituicao(schema_version=1, grupos=[])
    assert selecionar_origem_operacional("regra-0022", manifesto) == "legado"


def test_unknown_origin_or_destino_is_flagged() -> None:
    """A manifest referencing an unknown legacy origin or audited destino is flagged."""
    grupo = _grupo(origens_legacy=["regra-9999"], destinos_auditados=["unidade-fantasma"])
    manifesto = ManifestoSubstituicao(schema_version=1, grupos=[grupo])

    violations = validate_manifesto(manifesto, [], _legacy_bundle("regra-0022"))

    codes = {v.code for v in violations}
    assert "MANIFESTO_ORIGEM_INEXISTENTE" in codes
    assert "MANIFESTO_DESTINO_INEXISTENTE" in codes


def test_production_gate_rejects_any_active_group_regardless_of_completeness() -> None:
    """Fase 1A invariant: activation isn't wired to any exporter yet — always refused."""
    grupo = _grupo(
        destinos_auditados=["invalidez-a"], estado_grupo="ativo", decisao_completude=_DECISAO_COMPLETA
    )
    manifesto = ManifestoSubstituicao(schema_version=1, grupos=[grupo])

    violations = check_nenhum_grupo_ativo_em_producao(manifesto)

    assert any(v.code == "MANIFESTO_ATIVACAO_NAO_SUPORTADA" for v in violations)


def test_production_gate_passes_an_empty_manifest() -> None:
    """An empty manifest passes the Fase 1A production gate."""
    assert check_nenhum_grupo_ativo_em_producao(ManifestoSubstituicao(schema_version=1, grupos=[])) == []
