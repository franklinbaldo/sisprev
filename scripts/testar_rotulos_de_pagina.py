"""Confere a lógica dos rótulos lógicos de página do PDF, com casos sintéticos.

`scripts/gerar_relatorio_pdf.py` lê a numeração que o documento **imprime** e a
grava em `/PageLabels`, para que digitar no leitor o número citado num despacho
leve à folha certa. Este script confere as duas decisões dessa leitura contra
sequências construídas à mão — as que o catálogo real não produz hoje, e que
por isso nenhum build exercitaria.

Os dois modos de falha cobertos já aconteceram neste documento:

- a numeração **saltando**, que tornaria o rótulo lógico fiel a uma sequência
  que ninguém consegue citar;
- a numeração alternando de **representação** sobre um contador só — o leitor
  via 50, `li`, `lii`, 53, e a página 51 não existia para quem a procurasse.
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gerar_relatorio_pdf import (
    RotulosIncoerentesError,
    _conferir_rotulos,
    _romano_para_int,
    _trechos_de_rotulo,
)

logger = logging.getLogger(__name__)


def _romanos() -> list[str]:
    """Violações da conversão de romano para inteiro."""
    casos = {"i": 1, "iv": 4, "vii": 7, "ix": 9, "xi": 11, "xl": 40, "li": 51, "xciv": 94}
    return [
        f"romano {r!r}: esperava {n}, achou {_romano_para_int(r)}"
        for r, n in casos.items()
        if _romano_para_int(r) != n
    ]


def _sequencia_boa() -> list[str]:
    """A forma que o documento tem: capa sem número, romanos, depois arábicos."""
    rotulos = [None, "i", "ii", "iii", "4", "5", "6"]
    try:
        _conferir_rotulos(rotulos)
    except RotulosIncoerentesError as erro:
        return [f"a sequência válida foi recusada: {erro}"]

    trechos = _trechos_de_rotulo(rotulos)
    esperado = [(0, "", 0), (1, "r", 1), (4, "D", 4)]
    if trechos != esperado:
        return [f"esperava os trechos {esperado}, achou {trechos}"]
    return []


def _sequencia_que_salta() -> list[str]:
    """Numeração descontínua: o rótulo lógico não pode ser fiel a ela."""
    try:
        _conferir_rotulos([None, "i", "ii", "5", "6"])
    except RotulosIncoerentesError:
        return []
    return ["uma numeração que salta de 2 para 5 deveria ser recusada"]


def _sequencia_que_alterna() -> list[str]:
    """O defeito concreto: romano no meio de um documento em arábico."""
    try:
        _conferir_rotulos([None, "i", "ii", "3", "4", "v", "vi", "7"])
    except RotulosIncoerentesError:
        return []
    return ["uma numeração alternando r → D → r → D deveria ser recusada"]


def _romano_fora_do_inicio() -> list[str]:
    """Arábico antes de romano é a mesma inversão, e também não passa."""
    try:
        _conferir_rotulos(["1", "2", "iii", "iv"])
    except RotulosIncoerentesError:
        return []
    return ["arábico seguido de romano deveria ser recusado"]


def _documento_todo_arabico() -> list[str]:
    """Documento sem abertura romana é válido: a virada é opcional, não obrigatória."""
    try:
        _conferir_rotulos([None, "1", "2", "3"])
    except RotulosIncoerentesError as erro:
        return [f"um documento só com arábicos foi recusado: {erro}"]
    return []


def _numeracao_perdida_no_meio() -> list[str]:
    """Folha interna sem número: a continuidade sozinha não a pega.

    Só a capa pode não levar número. Quando uma folha interna perde o seu, o
    filtro dos `None` a apaga antes da conferência — e o caso que escapa é
    justamente o silencioso: se a folha perdida **não consome** um número, os
    impressos seguem contíguos e nada acusa. `[None, "i", "ii", None, "iii"]`
    passava; `[None, "i", None, "iii"]` já era recusado pela descontinuidade.
    Os quatro entram porque o que se protege é a folha interna sem número,
    consuma ela um número ou não.

    O efeito de deixar passar não é apenas a contagem: `_trechos_de_rotulo`
    dá àquela folha interna o prefixo `capa`, e o leitor exibe uma segunda
    capa no meio do documento.
    """
    violacoes = []
    for rotulos in (
        [None, "i", None, "iii"],
        [None, "1", "2", None, "4"],
        [None, "i", "ii", None, "iii"],
        [None, "1", "2", None, "3"],
    ):
        try:
            _conferir_rotulos(rotulos)
        except RotulosIncoerentesError:
            continue
        violacoes.append(f"folha sem número no meio de {rotulos} deveria ser recusada")
    return violacoes


def conferir() -> list[str]:
    """As violações de todos os casos; lista vazia se tudo confere."""
    return [
        *_romanos(),
        *_sequencia_boa(),
        *_sequencia_que_salta(),
        *_sequencia_que_alterna(),
        *_romano_fora_do_inicio(),
        *_documento_todo_arabico(),
        *_numeracao_perdida_no_meio(),
    ]


def main() -> int:
    """CLI: sai com 1 listando toda violação da lógica dos rótulos de página."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    violacoes = conferir()
    if violacoes:
        logger.error("Rótulos lógicos de página não conferem:\n%s", "\n".join(violacoes))
        return 1
    logger.info(
        "Rótulos lógicos de página conferem: conversão de romanos, agrupamento em trechos, "
        "e recusa de sequência que salta, que alterna de representação, que abre em arábico "
        "ou que perde a numeração numa folha interna."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
