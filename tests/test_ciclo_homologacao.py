"""Projeção de homologação — os grupos de um ciclo e as linhas que ela produz.

O CSV que a PGE recebe é a única superfície em que alguém vê, nas colunas do
próprio Sisprev, o que a proposta de um ciclo levaria ao sistema. Estes testes
seguram três coisas que, quebradas, produzem documento plausível e errado: os
grupos vêm da cadeia inteira e não só do conjunto folha; a linha sai com os
cabeçalhos do sistema e não com as chaves de frontmatter; e a projeção nunca
se apresenta como deployable enquanto a unidade não tiver sido promovida.
"""

from __future__ import annotations

import csv
from typing import TYPE_CHECKING

import pytest
from bundle import Bundle
from ciclo_homologacao import (
    COLUNAS,
    CicloSemGruposError,
    grupos_do_conjunto,
    linhas_de_homologacao,
)
from homologacao_csv import folhas_da_cadeia, regenerate_homologacao
from okf_common import (
    DEFAULT_BUNDLE,
    DEFAULT_BUNDLE_PROPOSTO,
    DEFAULT_HOMOLOGACAO_DIR,
)
from regra_proposta_schema import RegraProposta, load_regras_propostas
from regra_schema import CSV_COLUMN_NAMES

if TYPE_CHECKING:
    from pathlib import Path

CONJUNTO_DO_CICLO_1 = "ciclo-01-s6-fechamento"


@pytest.fixture(scope="module")
def bundle() -> Bundle:
    """O bundle legado comitado — a fonte que a projeção coteja."""
    return Bundle.load(DEFAULT_BUNDLE)


@pytest.fixture(scope="module")
def propostas() -> list[RegraProposta]:
    """As regras propostas comitadas — os destinos dos grupos."""
    return load_regras_propostas(DEFAULT_BUNDLE_PROPOSTO)


def test_grupos_vem_da_cadeia_inteira_nao_so_da_folha(bundle: Bundle) -> None:
    """O conjunto de fechamento não declara delta próprio; os grupos estão nas bases.

    Ler só ``substituicoes`` do conjunto folha devolveria zero e seria exibido
    como "este ciclo não substituiu nada" — o modo de falha mais caro possível
    num documento que existe para submeter substituições.
    """
    por_id = {conjunto.doc_id: conjunto for conjunto in bundle.conjuntos}
    folha = por_id[CONJUNTO_DO_CICLO_1]

    assert folha.contract is not None
    assert folha.contract.substituicoes == ()
    assert grupos_do_conjunto(CONJUNTO_DO_CICLO_1, por_id)


def test_a_ordem_dos_grupos_segue_a_cadeia_de_bases(bundle: Bundle) -> None:
    """Da base mais antiga para a mais recente — a ordem em que a auditoria decidiu."""
    por_id = {conjunto.doc_id: conjunto for conjunto in bundle.conjuntos}
    grupos = grupos_do_conjunto(CONJUNTO_DO_CICLO_1, por_id)

    nomes = [grupo.grupo for grupo in grupos]
    s2 = por_id["ciclo-01-s2-bloco-a"].contract
    assert s2 is not None
    assert nomes[: len(s2.substituicoes)] == [grupo.grupo for grupo in s2.substituicoes]


def test_conjunto_sem_grupo_na_cadeia_levanta(bundle: Bundle, propostas: list[RegraProposta]) -> None:
    """A raiz não propõe substituição — e devolver tupla vazia mentiria sobre isso."""
    with pytest.raises(CicloSemGruposError):
        linhas_de_homologacao(
            "catalogo-legado",
            conjuntos=bundle.conjuntos,
            propostas=propostas,
            bundle=bundle,
        )


def test_toda_origem_e_destino_do_ciclo_aparece_na_projecao(
    bundle: Bundle, propostas: list[RegraProposta]
) -> None:
    """Cada destino declarado vira exatamente uma linha, e as origens viajam com ela."""
    por_id = {conjunto.doc_id: conjunto for conjunto in bundle.conjuntos}
    grupos = grupos_do_conjunto(CONJUNTO_DO_CICLO_1, por_id)
    destinos = [ref for grupo in grupos for ref in grupo.destinos_propostos]

    linhas = linhas_de_homologacao(
        CONJUNTO_DO_CICLO_1,
        conjuntos=bundle.conjuntos,
        propostas=propostas,
        bundle=bundle,
    )

    assert len(linhas) == len(destinos)
    assert all(linha.origens_legacy for linha in linhas)


def test_a_linha_sai_com_os_cabecalhos_do_sisprev(bundle: Bundle, propostas: list[RegraProposta]) -> None:
    """O compilador projeta em chaves de frontmatter; a planilha precisa das colunas.

    Sem a tradução, o CSV sairia com todas as 27 colunas vazias e as chaves de
    frontmatter penduradas fora do cabeçalho — planilha que abre, parece
    completa e não coteja com o export operacional.
    """
    linhas = linhas_de_homologacao(
        CONJUNTO_DO_CICLO_1,
        conjuntos=bundle.conjuntos,
        propostas=propostas,
        bundle=bundle,
    )

    linha = linhas[0].as_csv_row()
    assert set(linha) == set(COLUNAS)
    assert all(coluna in linha for coluna in CSV_COLUMN_NAMES)
    assert linha["NOME"]
    assert linha["TIPO DE BENEFICIO"]


def test_a_projecao_nunca_se_declara_deployable_sem_promocao(
    bundle: Bundle, propostas: list[RegraProposta]
) -> None:
    """``preview`` é sempre ``deployable=False`` — a promoção é ato humano.

    O CSV existe para ser lido *antes* da decisão que promove as unidades. Se
    a coluna dissesse ``S`` aqui, o documento afirmaria pronto para o sistema
    justamente aquilo cuja aprovação ele está pedindo.
    """
    linhas = linhas_de_homologacao(
        CONJUNTO_DO_CICLO_1,
        conjuntos=bundle.conjuntos,
        propostas=propostas,
        bundle=bundle,
    )

    assert all(not linha.deployable for linha in linhas)
    assert all(linha.as_csv_row()["DEPLOYABLE"] == "N" for linha in linhas)


def test_a_raiz_fica_fora_das_folhas(bundle: Bundle) -> None:
    """``catalogo-legado`` registra o estado operacional, não uma proposta."""
    assert "catalogo-legado" not in folhas_da_cadeia(bundle)


def test_folha_e_o_conjunto_que_ninguem_usa_como_base(bundle: Bundle) -> None:
    """Uma folha nunca aparece como ``base`` de outro conjunto."""
    folhas = folhas_da_cadeia(bundle)
    bases = {
        conjunto.contract.base
        for conjunto in bundle.conjuntos
        if conjunto.contract is not None and conjunto.contract.base is not None
    }

    assert folhas
    assert not (set(folhas) & bases)


def test_o_csv_comitado_bate_com_o_bundle_vivo(bundle: Bundle, tmp_path: Path) -> None:
    """Artefato derivado: editar a unidade sem regenerar tem de quebrar."""
    emitidos = regenerate_homologacao(bundle, DEFAULT_BUNDLE_PROPOSTO, tmp_path)

    assert emitidos
    for conjunto_id in emitidos:
        recem_gerado = (tmp_path / f"{conjunto_id}.csv").read_text(encoding="utf-8")
        comitado = (DEFAULT_HOMOLOGACAO_DIR / f"{conjunto_id}.csv").read_text(encoding="utf-8")
        assert recem_gerado == comitado


def test_o_csv_comitado_tem_o_cabecalho_declarado() -> None:
    """A ordem das colunas é a de COLUNAS — 27 do Sisprev, depois a proveniência."""
    with (DEFAULT_HOMOLOGACAO_DIR / f"{CONJUNTO_DO_CICLO_1}.csv").open(encoding="utf-8") as fh:
        cabecalho = next(csv.reader(fh))

    assert tuple(cabecalho) == COLUNAS


def test_regenerate_e_no_op_sem_bundle_proposto(bundle: Bundle, tmp_path: Path) -> None:
    """Um bundle sem `okf/regras-propostas/` ao lado não quebra a derivação."""
    assert regenerate_homologacao(bundle, tmp_path / "inexistente", tmp_path) == ()
