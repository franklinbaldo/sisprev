"""Fixtures do harness genérico de auditoria jurídica."""

from __future__ import annotations

from datetime import date
from pathlib import Path

from simulador_casos import (
    CasoSimulado,
    assinatura_criterios_conhecidos,
    carregar_catalogo,
    executar_caso,
    selecionar_regras,
)

REPO_ROOT = Path(__file__).parents[1]
CATALOGO = carregar_catalogo(REPO_ROOT / "okf" / "regras-sisprev")
TIPO_AGENTES = next(regra.tipo_de_beneficio for regra in CATALOGO if regra.id == "regra-0068")
BASE = {
    "tipo_de_beneficio": TIPO_AGENTES,
    "sexo": "MASCULINO",
    "apos_especial": "S",
    "data_admissao": date(2020, 1, 10),
    "data_direito": date(2022, 6, 1),
    "anos_servico_publico": 20,
    "anos_no_cargo": 5,
}


def caso(caso_id: str, **fatos: object) -> CasoSimulado:
    """Cria uma fixture com os fatos comuns do caso."""
    return CasoSimulado(id=caso_id, fatos={**BASE, **fatos})


def test_66_15_reproduz_seletor_real_e_divergencias() -> None:
    """Verifica o contrato do harness para este caso."""
    resultado = executar_caso(caso("ece146-66-15", pontos=66, anos_exposicao=15), CATALOGO)

    assert resultado.expectativa.elegivel
    assert resultado.expectativa.faixa_legal == (66, 15)
    assert {"regra-0068", "regra-0069", "regra-0070"}.issubset(resultado.candidatos_legados)
    assert len(resultado.candidatos_legados) > len({"regra-0068", "regra-0069", "regra-0070"})
    assert resultado.tabelapontuacao_legada == ("N", "S")
    assert any("tabelapontuacao" in item for item in resultado.divergencias)
    assert any("devolveu " in item for item in resultado.divergencias)


def test_faixas_e_fatos_alcancados_sao_separados() -> None:
    """Verifica o contrato do harness para este caso."""
    casos = (
        ({"pontos": 76, "anos_exposicao": 20}, (76, 20)),
        ({"pontos": 86, "anos_exposicao": 25}, (86, 25)),
        ({"pontos": 67, "anos_exposicao": 15}, (66, 15)),
        ({"pontos": 86, "anos_exposicao": 24}, (76, 20)),
    )

    for fatos, faixa in casos:
        resultado = executar_caso(caso("faixa", **fatos), CATALOGO)
        assert resultado.expectativa.elegivel
        assert resultado.faixa_alcancada == faixa


def test_insuficiencia_nao_e_elegivel() -> None:
    """Verifica o contrato do harness para este caso."""
    resultado = executar_caso(caso("insuficiente", pontos=65, anos_exposicao=15), CATALOGO)

    assert not resultado.expectativa.elegivel
    assert resultado.expectativa.faixa_legal is None
    assert resultado.candidatos_legados == ()


def test_seletor_consulta_universo_e_exclui_outra_familia() -> None:
    """Verifica o contrato do harness para este caso."""
    fatos = {**BASE, "pontos": 66, "anos_exposicao": 15}
    candidatos = selecionar_regras(CATALOGO, fatos)

    assert len(CATALOGO) > len(candidatos)
    assert {"regra-0068", "regra-0069", "regra-0070"}.issubset({r.id for r in candidatos})
    assert all(r.tipo_de_beneficio == fatos["tipo_de_beneficio"] for r in candidatos)


def test_assinatura_conhecida_e_a_mesma_para_as_tres_regras_legadas() -> None:
    """Verifica o contrato do harness para este caso."""
    regras = {r.id: r for r in CATALOGO}
    assinaturas = {
        assinatura_criterios_conhecidos(regras[regra_id])
        for regra_id in ("regra-0068", "regra-0069", "regra-0070")
    }

    assert len(assinaturas) == 1
