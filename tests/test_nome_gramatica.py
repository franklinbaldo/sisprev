"""A gramática de ``nome`` (decisão de 2026-07-30) — o teto ancorado na importação.

O teto de comprimento da gramática **não** é escolha estética: é o comprimento
do maior ``NOME`` de ``data/raw/regras-sisprev.csv``, isto é, um valor que o
Sisprev comprovadamente aceita, já que aceitou a planilha de onde o catálogo
veio. As restrições reais da tela (truncamento, busca, ordenação) seguem não
conferidas, e a decisão foi fixar a gramática apesar disso — o que torna este
ancoramento a única prova disponível de que o teto é praticável.

Amarrado a ``data/raw/``, que é **imutável para sempre**: o número não
envelhece, e uma correção de ``nome`` no bundle vivo não o falseia. Nada aqui
roda sobre o bundle vivo de propósito — a gramática é alvo da auditoria, não
invariante do estado atual, e um teste que exigisse conformidade hoje reprovaria
o catálogo por não ter sido auditado ainda.
"""

from __future__ import annotations

import pandas as pd
from nome_gramatica import TETO_DE_COMPRIMENTO
from okf_common import ORIGINAL_CSV

LINHAS_DA_IMPORTACAO = 112


def _nomes_da_importacao() -> list[str]:
    # skiprows=1: a linha em branco no topo é artefato do export do Google
    # Sheets, nunca dado — mesma leitura que tests/test_sentinela.py faz.
    frame = pd.read_csv(ORIGINAL_CSV, skiprows=1, dtype=str, keep_default_na=False)
    nomes = [nome for nome in frame["NOME"].tolist() if nome.strip()]
    assert len(nomes) == LINHAS_DA_IMPORTACAO
    return nomes


def test_teto_e_o_maior_nome_da_importacao() -> None:
    """O teto declarado é exatamente o maior comprimento já aceito pelo Sisprev.

    Se o teto for baixado sem que alguém confira a tela, este teste falha e
    obriga a dizer de onde veio o número novo — que é o ponto: um teto menor
    que o da importação é afirmação sobre a interface, não sobre o dado.
    """
    assert max(len(nome) for nome in _nomes_da_importacao()) == TETO_DE_COMPRIMENTO


def test_nenhum_nome_da_importacao_excede_o_teto() -> None:
    """Trivial por construção acima, e é a asserção que a gramática de fato usa."""
    excedentes = [nome for nome in _nomes_da_importacao() if len(nome) > TETO_DE_COMPRIMENTO]
    assert excedentes == []
