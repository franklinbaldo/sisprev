"""RFC 0004 §5/§6/§10/§14 — the pure A → B compiler: preview/deployable/verify."""

from __future__ import annotations

from compilador_auditado import (
    compilar,
    detectar_colisoes,
    gerar_fundamentacao_projetada,
    ordenar_compilacoes,
    verificar,
)
from unidade_auditada_schema import LEGACY_FRONTMATTER_KEYS, UnidadeAuditada

_REQUISITO_NEXO = {
    "predicado": "nexo entre a incapacidade e o acidente em serviço",
    "protocolo_verificacao": {
        "pergunta": "Há nexo entre a incapacidade e o acidente em serviço?",
        "responsavel": "IPERON",
        "meio_de_prova": "pericia_oficial",
        "momento": "processo_concessorio",
        "evidencia_exigida": "laudo pericial oficial",
    },
    "portador_primario": "fundamentacao_integral",
}

_PROVENIENCIA_COMPLETA = {"fontes_consultadas": ["Casa Civil/DITEL — LC 1.100/2021"]}

_PROJECAO_PADRAO = {
    "nome": "Invalidez por acidente em serviço — ingresso após 2003",
    "integral": "S",
    "tipo_calculo": "Valor Médio",
    "paridade": "N",
}


def _unidade_completa(doc_id: str = "invalidez-acidente-pos-2003", **overrides: object) -> UnidadeAuditada:
    """RFC 0004 §16.1's own worked example — a fully deployable synthetic unit."""
    frontmatter: dict[str, object] = {
        "type": "UnidadeAuditada",
        "id": doc_id,
        "schema_version": 1,
        "estado_unidade": "deployable",
        "origens_legacy": ["regra-0022"],
        "predicados": {"causa_incapacidade": "acidente_em_servico", "regime": "lc-1100-2021"},
        "requisitos_verificacao_humana": [_REQUISITO_NEXO],
        "aplicabilidade_temporal": {
            "datas_legadas": {"data_adm_apos": "01/01/2004 00:00", "data_adm_ate": None},
        },
        "taxonomias": [{"ref": "/dispositivos/lce-1100-2021/art-30-p5.md", "papel": "nexo-acidente"}],
        "projecao": dict(_PROJECAO_PADRAO),
        "proveniencia": _PROVENIENCIA_COMPLETA,
        "confianca": "alta",
    }
    frontmatter.update(overrides)
    return UnidadeAuditada(doc_id=doc_id, frontmatter=frontmatter)


_LEGACY_IDS = frozenset({"regra-0022"})
_DISPOSITIVO_IDS = frozenset({"lce-1100-2021/art-30-p5"})


def test_deployable_unit_compiles_clean() -> None:
    """A fully-formed unit compiles clean with no pendencies."""
    resultado = compilar(
        _unidade_completa(), modo="deployable", legacy_regra_ids=_LEGACY_IDS, dispositivo_ids=_DISPOSITIVO_IDS
    )
    assert resultado.deployable is True
    assert resultado.pendencias == ()
    assert resultado.linha is not None
    assert resultado.linha["integral"] == "S"


def test_preview_with_a_pending_field_passes_but_is_never_deployable() -> None:
    """Preview admits a pending operational field but never ships."""
    unidade = _unidade_completa(aplicabilidade_temporal={"versao_rol": "pendente"})
    resultado = compilar(
        unidade, modo="preview", legacy_regra_ids=_LEGACY_IDS, dispositivo_ids=_DISPOSITIVO_IDS
    )

    assert resultado.deployable is False
    assert resultado.linha is not None  # the annotated projection is still produced


def test_deployable_with_the_same_pending_field_fails_fail_closed() -> None:
    """The same pendency blocks deployable mode fail-closed."""
    unidade = _unidade_completa(aplicabilidade_temporal={"versao_rol": "pendente"})
    resultado = compilar(
        unidade, modo="deployable", legacy_regra_ids=_LEGACY_IDS, dispositivo_ids=_DISPOSITIVO_IDS
    )

    assert resultado.deployable is False
    assert resultado.linha is None
    assert any(p.code == "P_COMPILA_PENDENTE" for p in resultado.pendencias)


def test_preview_never_deployable_even_when_fully_clean() -> None:
    """Preview is a diagnostic artifact, not a shipping decision — always deployable=False."""
    resultado = compilar(
        _unidade_completa(), modo="preview", legacy_regra_ids=_LEGACY_IDS, dispositivo_ids=_DISPOSITIVO_IDS
    )
    assert resultado.deployable is False


def test_requisito_without_carrier_content_fails() -> None:
    """A requisito pointing at a structured column the unit never populated has no portador.

    The portador_primario is a non-fundamentação column, so no
    auto-generated text fills it either — a real P_COMPILA_SEM_PORTADOR.
    """
    unidade = _unidade_completa()
    frontmatter = dict(unidade.frontmatter)
    frontmatter["requisitos_verificacao_humana"] = [{**_REQUISITO_NEXO, "portador_primario": "sexo"}]
    unidade_sem_portador = UnidadeAuditada(doc_id=unidade.doc_id, frontmatter=frontmatter)

    resultado = compilar(
        unidade_sem_portador,
        modo="deployable",
        legacy_regra_ids=_LEGACY_IDS,
        dispositivo_ids=_DISPOSITIVO_IDS,
    )

    assert resultado.deployable is False
    assert any(p.code == "P_COMPILA_SEM_PORTADOR" for p in resultado.pendencias)


def test_causa_without_requisito_is_incoerente_and_pending() -> None:
    """A causa predicate with no supporting requisito is incoherent."""
    unidade = _unidade_completa()
    frontmatter = dict(unidade.frontmatter)
    frontmatter["requisitos_verificacao_humana"] = []
    unidade_sem_requisito = UnidadeAuditada(doc_id=unidade.doc_id, frontmatter=frontmatter)

    resultado = compilar(
        unidade_sem_requisito,
        modo="deployable",
        legacy_regra_ids=_LEGACY_IDS,
        dispositivo_ids=_DISPOSITIVO_IDS,
    )

    assert resultado.deployable is False
    codes = {p.code for p in resultado.pendencias}
    assert "P_COMPILA_INCOERENTE" in codes


def test_requisito_without_matching_causa_is_incoerente() -> None:
    """A fundamentação requisito with no causa predicate is incoherent."""
    unidade = _unidade_completa()
    frontmatter = dict(unidade.frontmatter)
    frontmatter["predicados"] = {}
    unidade_sem_causa = UnidadeAuditada(doc_id=unidade.doc_id, frontmatter=frontmatter)

    resultado = compilar(
        unidade_sem_causa, modo="deployable", legacy_regra_ids=_LEGACY_IDS, dispositivo_ids=_DISPOSITIVO_IDS
    )

    assert resultado.deployable is False
    assert any(p.code == "P_COMPILA_INCOERENTE" for p in resultado.pendencias)


def test_missing_proveniencia_fails_deployable_only() -> None:
    """Missing proveniencia is a pendency in both modes, but only blocks deployable."""
    unidade = _unidade_completa(proveniencia=None)

    preview = compilar(
        unidade, modo="preview", legacy_regra_ids=_LEGACY_IDS, dispositivo_ids=_DISPOSITIVO_IDS
    )
    deployable = compilar(
        unidade, modo="deployable", legacy_regra_ids=_LEGACY_IDS, dispositivo_ids=_DISPOSITIVO_IDS
    )

    assert any(p.code == "P_COMPILA_SEM_PROVENIENCIA" for p in preview.pendencias)
    assert deployable.deployable is False
    assert any(p.code == "P_COMPILA_SEM_PROVENIENCIA" for p in deployable.pendencias)


def test_unresolved_taxonomia_reference_fails_deployable() -> None:
    """A taxonomia ref that doesn't resolve to an authored dispositivo blocks deployable."""
    resultado = compilar(
        _unidade_completa(), modo="deployable", legacy_regra_ids=_LEGACY_IDS, dispositivo_ids=frozenset()
    )
    assert any(p.code == "P_COMPILA_SEM_PROVENIENCIA" for p in resultado.pendencias)


def test_unit_not_marked_deployable_cannot_compile_in_deployable_mode() -> None:
    """estado_unidade must already be deployable to compile in deployable mode."""
    unidade = _unidade_completa(estado_unidade="preview")
    resultado = compilar(
        unidade, modo="deployable", legacy_regra_ids=_LEGACY_IDS, dispositivo_ids=_DISPOSITIVO_IDS
    )
    assert resultado.deployable is False
    assert any(p.code == "P_COMPILA_ESTADO_INVALIDO" for p in resultado.pendencias)


def test_unknown_schema_version_fails_before_anything_else() -> None:
    """An unknown schema_version fails before any other check runs."""
    unidade = _unidade_completa(schema_version=2)
    resultado = compilar(
        unidade, modo="preview", legacy_regra_ids=_LEGACY_IDS, dispositivo_ids=_DISPOSITIVO_IDS
    )
    assert resultado.linha is None
    assert resultado.pendencias[0].code == "P_COMPILA_SCHEMA_DESCONHECIDO"


def test_unknown_origin_fails() -> None:
    """An origem not present in the legacy bundle is a pendency."""
    resultado = compilar(
        _unidade_completa(), modo="deployable", legacy_regra_ids=frozenset(), dispositivo_ids=_DISPOSITIVO_IDS
    )
    assert any(p.code == "P_COMPILA_ORIGEM_INEXISTENTE" for p in resultado.pendencias)


def test_projection_is_deterministic() -> None:
    """Compiling the same unit twice yields byte-identical results."""
    unidade = _unidade_completa()
    r1 = compilar(unidade, modo="deployable", legacy_regra_ids=_LEGACY_IDS, dispositivo_ids=_DISPOSITIVO_IDS)
    r2 = compilar(unidade, modo="deployable", legacy_regra_ids=_LEGACY_IDS, dispositivo_ids=_DISPOSITIVO_IDS)
    assert r1.linha == r2.linha
    assert r1.id_projecao == r2.id_projecao


def test_compiled_row_uses_the_27_columns_in_regra_schema_order() -> None:
    """The compiled linha's keys follow P13.2's column order."""
    resultado = compilar(
        _unidade_completa(), modo="deployable", legacy_regra_ids=_LEGACY_IDS, dispositivo_ids=_DISPOSITIVO_IDS
    )
    assert resultado.linha is not None
    assert list(resultado.linha) == list(LEGACY_FRONTMATTER_KEYS)


def test_id_projecao_is_stable_and_independent_of_input_order() -> None:
    """id_projecao and its ordering are unaffected by input list order."""
    unidade_a = _unidade_completa("invalidez-acidente-pos-2003")
    unidade_b = _unidade_completa("invalidez-doenca-pos-2003", origens_legacy=["regra-0022"])
    resultado_a = compilar(
        unidade_a, modo="preview", legacy_regra_ids=_LEGACY_IDS, dispositivo_ids=_DISPOSITIVO_IDS
    )
    resultado_b = compilar(
        unidade_b, modo="preview", legacy_regra_ids=_LEGACY_IDS, dispositivo_ids=_DISPOSITIVO_IDS
    )

    ordem_1 = ordenar_compilacoes([resultado_a, resultado_b], legacy_row_index={"regra-0022": 22})
    ordem_2 = ordenar_compilacoes([resultado_b, resultado_a], legacy_row_index={"regra-0022": 22})

    assert [r.id_projecao for r in ordem_1] == [r.id_projecao for r in ordem_2]
    assert ordem_1[0].id_projecao == "invalidez-acidente-pos-2003"
    assert ordem_1[1].id_projecao == "invalidez-doenca-pos-2003"


def test_ordering_uses_smallest_origin_row_index_as_primary_key() -> None:
    """The primary sort key is the smallest row_index among origens_legacy."""
    unidade_later = _unidade_completa("de-0030", origens_legacy=["regra-0030"])
    unidade_earlier = _unidade_completa("de-0010", origens_legacy=["regra-0010"])
    r_later = compilar(
        unidade_later,
        modo="preview",
        legacy_regra_ids=frozenset({"regra-0030"}),
        dispositivo_ids=_DISPOSITIVO_IDS,
    )
    r_earlier = compilar(
        unidade_earlier,
        modo="preview",
        legacy_regra_ids=frozenset({"regra-0010"}),
        dispositivo_ids=_DISPOSITIVO_IDS,
    )

    ordenados = ordenar_compilacoes(
        [r_later, r_earlier], legacy_row_index={"regra-0030": 30, "regra-0010": 10}
    )

    assert [r.id_projecao for r in ordenados] == ["de-0010", "de-0030"]


def test_verify_detects_divergence() -> None:
    """verificar() reports a divergence when the expected value disagrees."""
    resultado = verificar(_unidade_completa(), {"integral": "N"})
    assert resultado.divergencias
    assert "integral" in resultado.divergencias[0]


def test_verify_matches_when_values_agree() -> None:
    """verificar() reports no divergence when expected values match the projection."""
    resultado = verificar(_unidade_completa(), {"integral": "S", "tipo_calculo": "Valor Médio"})
    assert resultado.divergencias == ()


def test_no_inference_from_nome_or_fundamentacao_prose() -> None:
    """Changing nome/fundamentacao* text must never change pendencies or predicate-derived checks."""
    baseline = compilar(
        _unidade_completa(), modo="deployable", legacy_regra_ids=_LEGACY_IDS, dispositivo_ids=_DISPOSITIVO_IDS
    )
    reworded = _unidade_completa(
        projecao={
            "nome": "Um nome completamente diferente, sem qualquer menção a causa",
            "integral": "S",
            "tipo_calculo": "Valor Médio",
            "paridade": "N",
        }
    )
    reworded_result = compilar(
        reworded, modo="deployable", legacy_regra_ids=_LEGACY_IDS, dispositivo_ids=_DISPOSITIVO_IDS
    )
    assert baseline.deployable == reworded_result.deployable
    assert baseline.pendencias == reworded_result.pendencias


def test_generated_fundamentacao_never_asserts_a_concrete_constatacao() -> None:
    """The generated text describes the requirement, never a concrete finding."""
    contrato = _unidade_completa().contract
    assert contrato is not None
    texto = gerar_fundamentacao_projetada(contrato.requisitos_verificacao_humana[0])
    assert "conforme constatação de" in texto
    assert "foi constatado" not in texto
    assert "confirmado no caso" not in texto


def test_collision_between_two_deployable_units_is_flagged() -> None:
    """Two units projecting to the same material key collide."""
    unidade_a = _unidade_completa("invalidez-a")
    unidade_b = _unidade_completa("invalidez-b")  # identical projecao/material content, different id
    resultado_a = compilar(
        unidade_a, modo="deployable", legacy_regra_ids=_LEGACY_IDS, dispositivo_ids=_DISPOSITIVO_IDS
    )
    resultado_b = compilar(
        unidade_b, modo="deployable", legacy_regra_ids=_LEGACY_IDS, dispositivo_ids=_DISPOSITIVO_IDS
    )

    violations = detectar_colisoes([resultado_a, resultado_b])

    assert any(v.code == "P_COMPILA_COLISAO" for v in violations)


def test_no_collision_when_material_content_differs() -> None:
    """Units with different material content never collide."""
    unidade_a = _unidade_completa("invalidez-a")
    unidade_b = _unidade_completa("invalidez-b", projecao={**_PROJECAO_PADRAO, "paridade": "S"})
    resultado_a = compilar(
        unidade_a, modo="deployable", legacy_regra_ids=_LEGACY_IDS, dispositivo_ids=_DISPOSITIVO_IDS
    )
    resultado_b = compilar(
        unidade_b, modo="deployable", legacy_regra_ids=_LEGACY_IDS, dispositivo_ids=_DISPOSITIVO_IDS
    )

    assert detectar_colisoes([resultado_a, resultado_b]) == []
