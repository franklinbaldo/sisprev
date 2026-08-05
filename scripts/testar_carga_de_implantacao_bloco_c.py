"""Confere, contra os dados reais, o que do Bloco C entra na carga de homologação.

O Bloco C tem **sessenta** destinos (três famílias de vinte causas) e quatro
origens legadas. O que entra na carga não é decidido por família, e sim pelo
**componente** do grafo origem↔destino: a troca de fonte operacional é atômica
(`okf/spec/regraproposta.md`, "Atomicidade é derivada, não declarada").

Daí o mapa que este script fixa:

- `regra-0019` → as dezenove causas qualificadas de ingresso até 2003 sem
  adesão ao RPC. Entram, sem ressalva.
- `regra-0020` → a causa comum da mesma família. Entra, com ressalva de
  homologação.
- `regra-0022` → **trinta e oito** destinos: as dezenove causas qualificadas de
  2004 a 05/11/2018 e as dezenove da família sujeita ao RPC. Não entram.
- `regra-0021` → **dois** destinos: a causa comum de cada uma dessas duas
  famílias. Não entram.

As duas últimas ficam de fora porque a família sujeita ao regime de previdência
complementar está `pendente_mapeamento_sisprev`: o catálogo legado não tem valor
de `tipo_calculo` que exprima o teto do RGPS, nem coluna que registre a opção do
§ 16 do art. 40 da Constituição Federal. E, porque `regra-0021`/`regra-0022`
cobrem hoje também quem ingressou a partir de 06/11/2018, retirá-las da produção
antes de a nova hipótese ter representação deixaria essa população **sem regra**
— que é exatamente o que a atomicidade impede.

Este script confere contra `okf/regras-propostas/regras/*.md`, não contra uma
fixture: é a mesma leitura que `scripts/derivar.py` faz para escrever
`data/regras-propostas.csv`.
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from derivar import _carga_de_implantacao, _lista, _regras_propostas

logger = logging.getLogger(__name__)

#: origem legada -> (destinos esperados, entra na carga?, quantos com ressalva)
MAPA: dict[str, tuple[int, bool, int]] = {
    "regra-0019": (19, True, 0),
    "regra-0020": (1, True, 1),
    "regra-0022": (38, False, 0),
    "regra-0021": (2, False, 1),
}
TOTAL_BLOCO_C = 60
TOTAL_NA_CARGA = 20


def _propostas_por_origem(propostas: dict[str, dict[str, object]], origem: str) -> set[str]:
    """Os ids de `RegraProposta` cujo `origens_legacy` é exatamente `[origem]`."""
    return {
        pid for pid, fm in propostas.items() if [str(o) for o in _lista(fm.get("origens_legacy"))] == [origem]
    }


def _conferir_ressalvas(
    propostas: dict[str, dict[str, object]], destinos: set[str], esperadas: int, origem: str
) -> list[str]:
    """As violações de `estado_implantacao`/`ressalva_homologacao` nos destinos de uma origem."""
    com = {
        pid
        for pid in destinos
        if str(propostas[pid].get("estado_implantacao") or "confirmada") == "confirmada_com_ressalva"
    }
    violacoes = []
    if len(com) != esperadas:
        violacoes.append(f"{origem}: esperava {esperadas} destino(s) com ressalva, achou {len(com)}")
    violacoes += [
        f"{pid}: confirmada_com_ressalva sem ressalva_homologacao"
        for pid in sorted(com)
        if not str(propostas[pid].get("ressalva_homologacao") or "").strip()
    ]
    violacoes += [
        f"{pid}: não deveria carregar ressalva_homologacao"
        for pid in sorted(destinos - com)
        if str(propostas[pid].get("ressalva_homologacao") or "").strip()
    ]
    return violacoes


def _conferir_origem(
    propostas: dict[str, dict[str, object]], na_carga: set[str], origem: str
) -> tuple[set[str], set[str], list[str]]:
    """(destinos da origem, os que entraram na carga, violações)."""
    esperados, entra, com_ressalva = MAPA[origem]
    destinos = _propostas_por_origem(propostas, origem)
    violacoes = []
    if len(destinos) != esperados:
        violacoes.append(f"{origem}: esperava {esperados} destinos, o catálogo tem {len(destinos)}")

    dentro = destinos & na_carga
    if entra and dentro != destinos:
        violacoes.append(f"{origem}: deveria entrar inteira na carga, faltam {sorted(destinos - dentro)}")
    if not entra and dentro:
        violacoes.append(
            f"{origem}: não deveria entrar na carga enquanto a família sujeita ao RPC "
            f"estiver pendente, mas entraram {sorted(dentro)}"
        )
    violacoes += _conferir_ressalvas(propostas, destinos, com_ressalva, origem)
    return destinos, dentro, violacoes


def conferir() -> list[str]:
    """As violações do mapa da carga do Bloco C; lista vazia se tudo confere."""
    propostas = _regras_propostas()
    prontos, _diagnosticos = _carga_de_implantacao(propostas)
    prontos_ids = [pid for pid, _origens in prontos]
    violacoes: list[str] = []

    if len(prontos_ids) != len(set(prontos_ids)):
        duplicadas = sorted({pid for pid in prontos_ids if prontos_ids.count(pid) > 1})
        violacoes.append(f"duplicidade na carga de homologação: {duplicadas}")
    na_carga = set(prontos_ids)

    todos: set[str] = set()
    do_bloco_na_carga: set[str] = set()
    for origem in MAPA:
        destinos, dentro, erros = _conferir_origem(propostas, na_carga, origem)
        todos |= destinos
        do_bloco_na_carga |= dentro
        violacoes += erros

    if len(todos) != TOTAL_BLOCO_C:
        violacoes.append(
            f"o Bloco C deveria ter {TOTAL_BLOCO_C} destinos nas quatro origens, tem {len(todos)}"
        )
    if len(do_bloco_na_carga) != TOTAL_NA_CARGA:
        violacoes.append(
            f"esperava {TOTAL_NA_CARGA} destinos do Bloco C na carga, achou {len(do_bloco_na_carga)}"
        )
    return violacoes


def main() -> int:
    """CLI: sai com 1 listando toda violação do mapa da carga do Bloco C."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    violacoes = conferir()
    if violacoes:
        logger.error("Carga de homologação do Bloco C não confere:\n%s", "\n".join(violacoes))
        return 1
    logger.info(
        "Carga de homologação do Bloco C confere: %d destinos ao todo; %d na carga "
        "(19 de regra-0019 sem ressalva e 1 de regra-0020 com ressalva); 40 fora, "
        "porque regra-0021/regra-0022 só podem ser trocadas junto com a família "
        "sujeita ao RPC, hoje pendente de mapeamento no Sisprev.",
        TOTAL_BLOCO_C,
        TOTAL_NA_CARGA,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
