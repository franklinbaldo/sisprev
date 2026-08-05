"""Confere, contra os dados reais, que a carga de implantação do Bloco C é 38x2.

Um `Conjunto` antigo declarava as quatro origens do Bloco C
(`regra-0019` a `regra-0022`) como um grupo só, e um relatório apressado podia
ler daí que as quarenta regras propostas aguardam juntas. O grafo
origem↔destino não concorda: `regra-0019` e `regra-0022` não compartilham
origem com a causa comum de cada coorte (`regra-0020`, `regra-0021`), então
formam componentes de implantação próprios. Este script confere isso contra
`okf/regras-propostas/regras/*.md`, não contra uma fixture — é a mesma leitura
que `scripts/derivar.py` faz para escrever `data/regras-propostas.csv`.
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from derivar import _carga_de_implantacao, _lista, _regras_propostas

logger = logging.getLogger(__name__)

#: As quatro origens do Bloco C do Ciclo 1 — `okf/regras-sisprev/ciclos/ciclo-01.md`, T4/T7.
ORIGEM_PRONTA = ("regra-0019", "regra-0022")
ORIGEM_PENDENTE = ("regra-0020", "regra-0021")
#: Dezenove destinos por origem pronta (T7) — o tamanho esperado da carga do Bloco C.
DESTINOS_ESPERADOS = 38


def _propostas_por_origem(propostas: dict[str, dict[str, object]], origem: str) -> set[str]:
    """Os ids de `RegraProposta` cujo `origens_legacy` é exatamente `[origem]`."""
    return {
        pid for pid, fm in propostas.items() if [str(o) for o in _lista(fm.get("origens_legacy"))] == [origem]
    }


def conferir() -> list[str]:
    """As violações do mapa 38x2, ditas uma por linha; lista vazia se tudo confere."""
    propostas = _regras_propostas()
    prontos, _diagnosticos = _carga_de_implantacao(propostas)
    prontos_ids = [pid for pid, _origens in prontos]

    esperado_pronto: set[str] = set()
    for origem in ORIGEM_PRONTA:
        esperado_pronto |= _propostas_por_origem(propostas, origem)
    esperado_pendente: set[str] = set()
    for origem in ORIGEM_PENDENTE:
        esperado_pendente |= _propostas_por_origem(propostas, origem)

    violacoes: list[str] = []

    if len(prontos_ids) != len(set(prontos_ids)):
        duplicadas = sorted({pid for pid in prontos_ids if prontos_ids.count(pid) > 1})
        violacoes.append(f"duplicidade na carga de implantação: {duplicadas}")

    prontos_do_bloco_c = set(prontos_ids) & (esperado_pronto | esperado_pendente)
    if len(esperado_pronto) != DESTINOS_ESPERADOS:
        violacoes.append(
            f"esperava {DESTINOS_ESPERADOS} destinos para {ORIGEM_PRONTA}, "
            f"o catálogo tem {len(esperado_pronto)}"
        )
    faltando = esperado_pronto - prontos_do_bloco_c
    if faltando:
        violacoes.append(f"lacuna: destino de {ORIGEM_PRONTA} não entrou na carga: {sorted(faltando)}")

    vazando = prontos_do_bloco_c & esperado_pendente
    if vazando:
        violacoes.append(
            f"{ORIGEM_PENDENTE} não deveriam entrar na carga enquanto pendentes, mas entraram: "
            f"{sorted(vazando)}"
        )

    if not esperado_pendente:
        violacoes.append(f"nenhuma regra proposta com origem exatamente {ORIGEM_PENDENTE} encontrada")

    return violacoes


def main() -> int:
    """CLI: sai com 1 listando toda violação do mapa 38x2 do Bloco C."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    violacoes = conferir()
    if violacoes:
        logger.error("Carga de implantação do Bloco C não confere com 38x2:\n%s", "\n".join(violacoes))
        return 1
    logger.info(
        "Carga de implantação do Bloco C confere: %d destinos de %s prontos, 2 destinos de %s pendentes.",
        DESTINOS_ESPERADOS,
        ORIGEM_PRONTA,
        ORIGEM_PENDENTE,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
