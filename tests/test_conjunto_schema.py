"""P15 — conjuntos: contrato, resolução de pertinência e invariantes (RFC 0006).

Fixtures sintéticas: o que se fixa aqui é a **derivação** (o que pertence a um
conjunto, dado o que ele declara), não a leitura do catálogo real. A prova de
que a fase 0 é um no-op sobre o bundle real vive em ``test_achados_bundle.py``,
que já compara os fingerprints e todo o baseline camada 3.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from bundle import Bundle
from conjunto_schema import (
    Conjunto,
    ResolucaoError,
    conjunto_vigente,
    conjuntos_por_id,
    load_conjuntos,
    resolve,
    validate_conjunto,
    validate_conjuntos,
)
from md_format import write_markdown

if TYPE_CHECKING:
    from collections.abc import Sequence
    from pathlib import Path

    from detections import Violation

import yaml

_LEGADO = ("/regras/regra-0001.md", "/regras/regra-0002.md", "/regras/regra-0003.md")


def _conjunto(doc_id: str, **frontmatter: object) -> Conjunto:
    fm: dict[str, object] = {"type": "Conjunto", "id": doc_id, "nome": f"Conjunto {doc_id}"}
    fm.update(frontmatter)
    return Conjunto(doc_id=doc_id, frontmatter=fm, body=f"# {doc_id}\n")


def _raiz(situacao: str = "vigente") -> Conjunto:
    return _conjunto("catalogo-legado", situacao=situacao, origem="catalogo-legado")


def _codigos(violations: Sequence[Violation]) -> set[str]:
    return {v.code for v in violations}


def test_root_membership_is_the_whole_legacy_catalog() -> None:
    """A raiz declara de onde vem, e não lista — é o que mantém os 112 docs intocados."""
    raiz = _raiz()
    assert resolve("catalogo-legado", conjuntos_por_id([raiz]), _LEGADO) == tuple(sorted(_LEGADO))


def test_substitution_swaps_origin_for_destinations() -> None:
    """1:N: uma origem sai, todas as descendentes do grupo entram."""
    raiz = _raiz()
    proposto = _conjunto(
        "pge-2026",
        situacao="proposto",
        base="catalogo-legado",
        substituicoes=[
            {
                "grupo": "substituicao-regra-0002",
                "origens_legacy": ["/regras/regra-0002.md"],
                "destinos_auditados": ["/regras-auditadas/unidades/a.md", "/regras-auditadas/unidades/b.md"],
            }
        ],
    )
    assert resolve("pge-2026", conjuntos_por_id([raiz, proposto]), _LEGADO) == (
        "/regras-auditadas/unidades/a.md",
        "/regras-auditadas/unidades/b.md",
        "/regras/regra-0001.md",
        "/regras/regra-0003.md",
    )


def test_consolidation_merges_several_origins_into_one() -> None:
    """N:1: as duas origens saem e a unidade única entra."""
    raiz = _raiz()
    proposto = _conjunto(
        "consolida",
        situacao="proposto",
        base="catalogo-legado",
        substituicoes=[
            {
                "grupo": "consolidacao",
                "origens_legacy": ["/regras/regra-0001.md", "/regras/regra-0002.md"],
                "destinos_auditados": ["/regras-auditadas/unidades/c.md"],
            }
        ],
    )
    assert resolve("consolida", conjuntos_por_id([raiz, proposto]), _LEGADO) == (
        "/regras-auditadas/unidades/c.md",
        "/regras/regra-0003.md",
    )


def test_revocation_removes_without_a_successor() -> None:
    """Revogação pura: sai e nada entra — o caso que nenhum grupo representa."""
    raiz = _raiz()
    proposto = _conjunto(
        "revoga", situacao="proposto", base="catalogo-legado", revoga=["/regras/regra-0003.md"]
    )
    assert resolve("revoga", conjuntos_por_id([raiz, proposto]), _LEGADO) == (
        "/regras/regra-0001.md",
        "/regras/regra-0002.md",
    )


def test_introduction_adds_without_a_predecessor() -> None:
    """Introdução pura: entra sem antecessora — o outro caso fora do grupo."""
    raiz = _raiz()
    proposto = _conjunto(
        "introduz",
        situacao="proposto",
        base="catalogo-legado",
        introduz=["/regras-auditadas/unidades/nova.md"],
    )
    assert "/regras-auditadas/unidades/nova.md" in resolve(
        "introduz", conjuntos_por_id([raiz, proposto]), _LEGADO
    )


def test_base_chain_composes_deltas_in_order() -> None:
    """Uma cadeia acumula: o neto herda o que o pai já tinha tirado."""
    raiz = _raiz()
    pai = _conjunto("pai", situacao="proposto", base="catalogo-legado", revoga=["/regras/regra-0001.md"])
    neto = _conjunto("neto", situacao="proposto", base="pai", revoga=["/regras/regra-0002.md"])
    assert resolve("neto", conjuntos_por_id([raiz, pai, neto]), _LEGADO) == ("/regras/regra-0003.md",)


def test_cyclic_base_raises_instead_of_returning_a_partial_answer() -> None:
    """Pertinência que perde a base inteira em silêncio seria lida como 'o catálogo encolheu'."""
    a = _conjunto("a", situacao="proposto", base="b")
    b = _conjunto("b", situacao="proposto", base="a")
    with pytest.raises(ResolucaoError, match="cyclic"):
        resolve("a", conjuntos_por_id([a, b]), _LEGADO)


def test_unknown_base_raises() -> None:
    """Base que não resolve também não vira resposta parcial."""
    orfao = _conjunto("orfao", situacao="proposto", base="inexistente")
    with pytest.raises(ResolucaoError, match="unknown conjunto"):
        resolve("orfao", conjuntos_por_id([orfao]), _LEGADO)


def test_target_outside_the_base_is_reported() -> None:
    """Substituir o que não está na base é declarar sobre um catálogo que não é o seu."""
    raiz = _raiz()
    proposto = _conjunto(
        "fora", situacao="proposto", base="catalogo-legado", revoga=["/regras/regra-0099.md"]
    )
    assert "P15_ALVO_FORA_DA_BASE" in _codigos(validate_conjuntos([raiz, proposto], _LEGADO))


def test_the_same_rule_substituted_and_revoked_is_reported() -> None:
    """Sair de dois jeitos ao mesmo tempo é contradição, não redundância."""
    raiz = _raiz()
    proposto = _conjunto(
        "duplo",
        situacao="proposto",
        base="catalogo-legado",
        substituicoes=[
            {
                "grupo": "g",
                "origens_legacy": ["/regras/regra-0001.md"],
                "destinos_auditados": ["/regras-auditadas/unidades/a.md"],
            }
        ],
        revoga=["/regras/regra-0001.md"],
    )
    assert "P15_ALVO_DUPLO" in _codigos(validate_conjuntos([raiz, proposto], _LEGADO))


def test_two_destinations_for_one_origin_is_not_a_violation() -> None:
    """A decomposição 1:N é o caso que a RFC 0004 ratificou — não pode ser recusada."""
    raiz = _raiz()
    proposto = _conjunto(
        "decompoe",
        situacao="proposto",
        base="catalogo-legado",
        substituicoes=[
            {
                "grupo": "g",
                "origens_legacy": ["/regras/regra-0001.md"],
                "destinos_auditados": ["/regras-auditadas/unidades/a.md", "/regras-auditadas/unidades/b.md"],
            }
        ],
    )
    assert validate_conjuntos([raiz, proposto], _LEGADO) == []


def test_two_vigentes_is_reported() -> None:
    """O catálogo tem um estado atual, não dois."""
    outro = _conjunto("outro", situacao="vigente", base="catalogo-legado")
    assert "P15_VIGENTE_MULTIPLO" in _codigos(validate_conjuntos([_raiz(), outro], _LEGADO))


def test_no_vigente_is_reported() -> None:
    """Nem zero: um catálogo sem estado atual não é um estado, é uma lacuna."""
    assert "P15_VIGENTE_AUSENTE" in _codigos(validate_conjuntos([_raiz("proposto")], _LEGADO))


def test_an_empty_bundle_reports_nothing() -> None:
    """Antes da migração não há conjuntos, e isso não é violação de nada."""
    assert validate_conjuntos([], _LEGADO) == []


def test_root_is_exempt_from_decisao_and_ato() -> None:
    """A raiz não transitou: exigir-lhe a decisão fabricaria um ato que ninguém praticou."""
    assert validate_conjunto(_raiz()) == []


def test_non_root_vigente_requires_decisao_and_ato() -> None:
    """Quem transita a vigente responde pelos dois — a dispensa é da raiz, não do estado."""
    codigos = _codigos(validate_conjunto(_conjunto("x", situacao="vigente", base="catalogo-legado")))
    assert codigos == {"P15_VIGENTE_SEM_DECISAO", "P15_VIGENTE_SEM_ATO"}


def test_a_conjunto_declaring_both_origem_and_base_is_invalid() -> None:
    """Raiz é quem tem origem e não tem base — sem isso a dispensa acima seria reivindicável."""
    ambiguo = _conjunto("ambiguo", situacao="proposto", origem="catalogo-legado", base="catalogo-legado")
    assert "P15_CONJUNTO_INVALIDO" in _codigos(validate_conjunto(ambiguo))


def test_a_conjunto_with_neither_origem_nor_base_is_invalid() -> None:
    """Um conjunto solto não compõe nada."""
    assert "P15_CONJUNTO_INVALIDO" in _codigos(validate_conjunto(_conjunto("solto", situacao="proposto")))


def test_partial_scope_is_reserved_but_refused() -> None:
    """A forma existe no schema para não quebrar depois; o validador ainda a recusa."""
    com_escopo = _conjunto(
        "parcial",
        situacao="proposto",
        base="catalogo-legado",
        atos=[
            {
                "tipo": "parecer",
                "autoridade": "pge",
                "efeito": "valida",
                "identificador": "x",
                "fonte": "y",
                "escopo": {"tipo": "regras", "regras": ["/regras/regra-0001.md"]},
            }
        ],
    )
    assert "P15_ESCOPO_NAO_SUPORTADO" in _codigos(validate_conjunto(com_escopo))


def test_an_active_group_without_decisao_completude_fails_the_contract() -> None:
    """Ativação atômica exige a decisão registrada (RFC 0004 §1.4)."""
    ativo = _conjunto(
        "ativo",
        situacao="proposto",
        base="catalogo-legado",
        substituicoes=[
            {
                "grupo": "g",
                "origens_legacy": ["/regras/regra-0001.md"],
                "destinos_auditados": ["/regras-auditadas/unidades/a.md"],
                "estado_grupo": "ativo",
            }
        ],
    )
    assert ativo.contract is None
    assert "P15_CONJUNTO_INVALIDO" in _codigos(validate_conjunto(ativo))


def test_load_reads_authored_docs_and_skips_the_derived_index(tmp_path: Path) -> None:
    """``index.md`` é derivado; lê-lo como conjunto criaria um membro fantasma."""
    fm = yaml.safe_dump(
        {
            "type": "Conjunto",
            "id": "raiz",
            "nome": "Raiz",
            "situacao": "vigente",
            "origem": "catalogo-legado",
        },
        allow_unicode=True,
        sort_keys=False,
    )
    write_markdown(tmp_path / "raiz.md", f"---\n{fm}---\n\n# Raiz\n")
    write_markdown(tmp_path / "index.md", "# Conjuntos de regras\n")

    conjuntos = load_conjuntos(tmp_path)

    assert [c.doc_id for c in conjuntos] == ["raiz"]
    assert conjunto_vigente(conjuntos) is not None


def test_active_regras_is_unscoped_when_no_conjunto_is_authored() -> None:
    """Bundle sintético sem conjuntos continua exatamente como antes da P15."""
    bundle = Bundle()
    assert bundle.catalogo_vigente is None
    assert bundle.active_regras() == []
