"""Confere, contra os dados reais, que a carga de homologação do Bloco C é 40, duas com ressalva.

Um `Conjunto` antigo declarava as quatro origens do Bloco C
(`regra-0019` a `regra-0022`) como um grupo só, e um relatório apressado podia
ler daí que as quarenta regras propostas aguardam juntas. O grafo
origem↔destino não concorda: `regra-0019` e `regra-0022` não compartilham
origem com a causa comum de cada coorte (`regra-0020`, `regra-0021`), então
formam componentes de implantação próprios — mas isso não afeta a entrada na
carga desde RFC 0004 round 12 (`okf/spec/regraproposta.md`,
`okf/spec/ciclo.md`): a carga que `scripts/derivar.py` produz é planilha de
**homologação**, e as duas unidades de causa comum entram nela com
`estado_implantacao: confirmada_com_ressalva`, evidenciada por `regra-0020` e
`regra-0021` já estarem em produção com a mesma combinação
(`integral: N`, `tipo_calculo: Proporcionalidade Dias`) para as mesmas
hipóteses. Este script confere isso contra `okf/regras-propostas/regras/*.md`,
não contra uma fixture — é a mesma leitura que `scripts/derivar.py` faz para
escrever `data/regras-propostas.csv`.
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from derivar import _carga_de_implantacao, _lista, _regras_propostas

logger = logging.getLogger(__name__)

#: As quatro origens do Bloco C do Ciclo 1 — `okf/regras-sisprev/ciclos/ciclo-01.md`, T4/T7.
ORIGEM_SEM_RESSALVA = ("regra-0019", "regra-0022")
ORIGEM_COM_RESSALVA = ("regra-0020", "regra-0021")
#: Dezenove destinos não causa-comum por origem (T7) — trinta e oito ao todo.
DESTINOS_SEM_RESSALVA_ESPERADOS = 38
#: Uma unidade de causa comum por origem (T7) — duas ao todo.
DESTINOS_COM_RESSALVA_ESPERADOS = 2


def _propostas_por_origem(propostas: dict[str, dict[str, object]], origem: str) -> set[str]:
    """Os ids de `RegraProposta` cujo `origens_legacy` é exatamente `[origem]`."""
    return {
        pid for pid, fm in propostas.items() if [str(o) for o in _lista(fm.get("origens_legacy"))] == [origem]
    }


def _conferir_contagens(esperado_sem_ressalva: set[str], esperado_com_ressalva: set[str]) -> list[str]:
    """As violações de tamanho dos dois grupos esperados."""
    violacoes = []
    if len(esperado_sem_ressalva) != DESTINOS_SEM_RESSALVA_ESPERADOS:
        violacoes.append(
            f"esperava {DESTINOS_SEM_RESSALVA_ESPERADOS} destinos para {ORIGEM_SEM_RESSALVA}, "
            f"o catálogo tem {len(esperado_sem_ressalva)}"
        )
    if len(esperado_com_ressalva) != DESTINOS_COM_RESSALVA_ESPERADOS:
        violacoes.append(
            f"esperava {DESTINOS_COM_RESSALVA_ESPERADOS} destinos para {ORIGEM_COM_RESSALVA}, "
            f"o catálogo tem {len(esperado_com_ressalva)}"
        )
    if not esperado_com_ressalva:
        violacoes.append(f"nenhuma regra proposta com origem exatamente {ORIGEM_COM_RESSALVA} encontrada")
    return violacoes


def _conferir_ressalvas(
    propostas: dict[str, dict[str, object]],
    esperado_sem_ressalva: set[str],
    esperado_com_ressalva: set[str],
) -> list[str]:
    """As violações de `estado_implantacao`/`ressalva_homologacao` por regra."""
    violacoes = []
    for pid in sorted(esperado_com_ressalva):
        fm = propostas.get(pid, {})
        estado_implantacao = str(fm.get("estado_implantacao") or "confirmada")
        if estado_implantacao != "confirmada_com_ressalva":
            violacoes.append(
                f"{pid}: esperava estado_implantacao=confirmada_com_ressalva, achou {estado_implantacao!r}"
            )
        if not str(fm.get("ressalva_homologacao") or "").strip():
            violacoes.append(f"{pid}: confirmada_com_ressalva sem ressalva_homologacao")

    for pid in sorted(esperado_sem_ressalva):
        fm = propostas.get(pid, {})
        if str(fm.get("ressalva_homologacao") or "").strip():
            violacoes.append(f"{pid}: não deveria carregar ressalva_homologacao")
    return violacoes


def conferir() -> list[str]:
    """As violações do mapa 40 (38 sem ressalva, 2 com ressalva); lista vazia se tudo confere."""
    propostas = _regras_propostas()
    prontos, _diagnosticos = _carga_de_implantacao(propostas)
    prontos_ids = [pid for pid, _origens in prontos]

    esperado_sem_ressalva: set[str] = set()
    for origem in ORIGEM_SEM_RESSALVA:
        esperado_sem_ressalva |= _propostas_por_origem(propostas, origem)
    esperado_com_ressalva: set[str] = set()
    for origem in ORIGEM_COM_RESSALVA:
        esperado_com_ressalva |= _propostas_por_origem(propostas, origem)

    violacoes: list[str] = []

    if len(prontos_ids) != len(set(prontos_ids)):
        duplicadas = sorted({pid for pid in prontos_ids if prontos_ids.count(pid) > 1})
        violacoes.append(f"duplicidade na carga de homologação: {duplicadas}")

    prontos_do_bloco_c = set(prontos_ids) & (esperado_sem_ressalva | esperado_com_ressalva)
    violacoes += _conferir_contagens(esperado_sem_ressalva, esperado_com_ressalva)

    faltando = (esperado_sem_ressalva | esperado_com_ressalva) - prontos_do_bloco_c
    if faltando:
        violacoes.append(f"lacuna: destino do Bloco C não entrou na carga: {sorted(faltando)}")

    violacoes += _conferir_ressalvas(propostas, esperado_sem_ressalva, esperado_com_ressalva)

    return violacoes


def main() -> int:
    """CLI: sai com 1 listando toda violação do mapa 40 (38 sem ressalva, 2 com ressalva) do Bloco C."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    violacoes = conferir()
    if violacoes:
        logger.error("Carga de homologação do Bloco C não confere:\n%s", "\n".join(violacoes))
        return 1
    logger.info(
        "Carga de homologação do Bloco C confere: %d destinos de %s sem ressalva, "
        "%d destinos de %s com ressalva de homologação.",
        DESTINOS_SEM_RESSALVA_ESPERADOS,
        ORIGEM_SEM_RESSALVA,
        DESTINOS_COM_RESSALVA_ESPERADOS,
        ORIGEM_COM_RESSALVA,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
