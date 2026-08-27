#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.13"
# dependencies = [
# ]
# ///
"""Confere que a carga de cada ciclo contém exatamente as regras daquele ciclo.

O relatório de um ciclo é manifestação jurídica sobre um conjunto nomeado de
regras propostas, e determina a inserção em homologação do arquivo que
identifica pelo resumo criptográfico. Se esse arquivo contiver regra de outro
ciclo, o resumo garante a integridade do arquivo **errado para aquele escopo**:
quem importa a planilha inteira leva à homologação regra sobre a qual aquele
relatório não concluiu.

Foi o que acontecia. O relatório do Ciclo 1 concluía sobre 60 regras e anexava
`data/regras-propostas.csv`, a carga global, com 64 linhas — quatro delas do
terceiro ciclo de validação. Nada acusava, porque cada lado estava certo
isoladamente: o CSV era exatamente o que `derivar.py` produzia, e o relatório
contava exatamente os destinos do seu grafo.

Este gate confronta os dois. A carga global continua existindo para conferir o
catálogo como um todo, e a soma das cargas por ciclo tem de reproduzi-la
exatamente — nenhuma regra pronta pode ficar sem arquivo, e nenhuma pode
aparecer em dois.
"""

from __future__ import annotations

import csv
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from derivar import (
    CSV_DE_HOMOLOGACAO,
    _carga_de_implantacao,
    _regras_propostas,
    ciclos_com_carga,
    csv_do_ciclo,
)

logger = logging.getLogger(__name__)


def _regras_do_csv(caminho: Path) -> list[str]:
    """A coluna `REGRA PROPOSTA` do arquivo, na ordem em que ele a escreve."""
    with caminho.open(encoding="utf-8", newline="") as arquivo:
        return [linha["REGRA PROPOSTA"] for linha in csv.DictReader(arquivo)]


def conferir() -> list[str]:
    """As violações do escopo das cargas; lista vazia se tudo confere."""
    propostas = _regras_propostas()
    prontos, _ = _carga_de_implantacao(propostas)
    esperado_por_ciclo: dict[str, set[str]] = {}
    for pid, _origens in prontos:
        esperado_por_ciclo.setdefault(str(propostas[pid].get("ciclo")), set()).add(pid)

    violacoes = []
    uniao: set[str] = set()
    for ciclo in ciclos_com_carga():
        caminho = csv_do_ciclo(ciclo)
        if not caminho.exists():
            violacoes.append(f"{caminho.name}: o ciclo tem regra pronta e o arquivo de carga não existe")
            continue
        no_arquivo = _regras_do_csv(caminho)
        esperado = esperado_por_ciclo.get(ciclo, set())
        uniao |= set(no_arquivo)

        repetidas = sorted({r for r in no_arquivo if no_arquivo.count(r) > 1})
        if repetidas:
            violacoes.append(f"{caminho.name}: regra repetida no arquivo: {repetidas[:3]}")

        alheias = sorted(set(no_arquivo) - esperado)
        if alheias:
            violacoes.append(
                f"{caminho.name}: {len(alheias)} regra(s) que não são destinos prontos de "
                f"{ciclo}: {alheias[:3]}"
            )
        faltando = sorted(esperado - set(no_arquivo))
        if faltando:
            violacoes.append(
                f"{caminho.name}: {len(faltando)} destino(s) pronto(s) de {ciclo} fora do "
                f"arquivo: {faltando[:3]}"
            )
        # O número de linhas é o que o relatório imprime como "Regras (linhas
        # de dados)" e o que a página confere contra `destinosNaCarga`.
        if len(no_arquivo) != len(esperado):
            violacoes.append(
                f"{caminho.name}: {len(no_arquivo)} linhas para {len(esperado)} destinos prontos de {ciclo}"
            )

    # E a global tem de ser exatamente a soma — nenhuma regra pronta sem
    # arquivo de ciclo, nenhuma em dois.
    global_ = set(_regras_do_csv(CSV_DE_HOMOLOGACAO))
    if global_ != uniao:
        sobrando = sorted(global_ - uniao)
        faltando = sorted(uniao - global_)
        violacoes.append(
            f"a carga global não é a soma das cargas por ciclo: {len(sobrando)} só na global "
            f"({sobrando[:3]}), {len(faltando)} só nas por ciclo ({faltando[:3]})"
        )
    return violacoes


def main() -> int:
    """CLI: sai com 1 listando toda divergência de escopo entre as cargas."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    violacoes = conferir()
    if violacoes:
        logger.error("As cargas por ciclo não conferem:\n%s", "\n".join(violacoes))
        return 1
    ciclos = ciclos_com_carga()
    logger.info(
        "Cargas por ciclo conferem: %d arquivo(s) (%s), cada um com exatamente os destinos "
        "prontos do seu ciclo, e a soma reproduzindo a carga global.",
        len(ciclos),
        ", ".join(f"{c}: {len(_regras_do_csv(csv_do_ciclo(c)))}" for c in ciclos),
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
