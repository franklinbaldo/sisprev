"""Escreve o CSV de homologação de cada proposta viva (P15, RFC 0004).

O arquivo é artefato **derivado**, como ``data/regras-sisprev.csv``: regenerado
por ``gerar_indices.py``, nunca editado à mão, e conferido pelo CI. Editar o
CSV corrigiria a planilha e deixaria a unidade auditada errada, que é a fonte.

**Uma proposta por folha da cadeia de conjuntos.** Um ciclo encadeia um
conjunto por sessão, cada um baseado no anterior, e só o último representa a
proposta atual; emitir um CSV por conjunto produziria cinco planilhas quase
iguais para o mesmo ciclo, e quem recebesse a remessa teria de adivinhar qual
vale. A folha — o conjunto que nenhum outro usa como base — é a proposta viva,
e a derivação acompanha a autoria: encadear um conjunto novo sobre a folha
atual move o CSV para ele, que é exatamente o comportamento desejado.

A raiz (``catalogo-legado``) fica de fora: ela não propõe substituição alguma,
registra o estado operacional preexistente.
"""

from __future__ import annotations

import csv
from typing import TYPE_CHECKING

from ciclo_homologacao import COLUNAS, CicloSemGruposError, linhas_de_homologacao
from unidade_auditada_schema import load_unidades_auditadas

if TYPE_CHECKING:
    from pathlib import Path

    from bundle import Bundle


def folhas_da_cadeia(bundle: Bundle) -> tuple[str, ...]:
    """Devolve os conjuntos que nenhum outro usa como base, exceto a raiz."""
    bases = {
        conjunto.contract.base
        for conjunto in bundle.conjuntos
        if conjunto.contract is not None and conjunto.contract.base is not None
    }
    return tuple(
        sorted(
            conjunto.doc_id
            for conjunto in bundle.conjuntos
            if conjunto.doc_id not in bases and not conjunto.eh_raiz
        )
    )


def escrever_csv(caminho: Path, linhas: list[dict[str, str]]) -> None:
    """Escreve ``linhas`` em ``caminho`` com as colunas e a ordem de :data:`COLUNAS`."""
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with caminho.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(COLUNAS), lineterminator="\n")
        writer.writeheader()
        writer.writerows(linhas)


def regenerate_homologacao(bundle: Bundle, auditadas_dir: Path, out_dir: Path) -> tuple[str, ...]:
    """Regenera um CSV por proposta viva. Devolve os ids emitidos.

    Um conjunto folha sem grupo algum na cadeia não gera arquivo — não é erro,
    é uma proposta que ainda não substitui nada.
    """
    if not auditadas_dir.exists():
        return ()
    unidades = load_unidades_auditadas(auditadas_dir)
    emitidos: list[str] = []
    for conjunto_id in folhas_da_cadeia(bundle):
        try:
            linhas = linhas_de_homologacao(
                conjunto_id,
                conjuntos=bundle.conjuntos,
                unidades=unidades,
                bundle=bundle,
            )
        except CicloSemGruposError:
            continue
        escrever_csv(out_dir / f"{conjunto_id}.csv", [linha.as_csv_row() for linha in linhas])
        emitidos.append(conjunto_id)
    return tuple(emitidos)
