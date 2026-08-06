"""Confere, contra os dados reais, o que do Bloco C entra na carga de homologação.

O Bloco C tem **sessenta** destinos (três famílias de vinte causas) e quatro
origens legadas. Todos os sessenta integram a carga: a decisão de 2026-08-06
reconheceu que a ausência de conhecimento sobre o funcionamento interno do
Sisprev não impede a homologação — é ela que existe para verificar em campo o
comportamento do sistema antes da ativação em produção.

Daí o mapa que este script fixa:

- `regra-0019` → as dezenove causas qualificadas de ingresso até 2003 sem
  adesão ao RPC. Entram, sem ressalva.
- `regra-0020` → a causa comum da mesma família. Entra, com ressalva sobre a
  base da proporcionalização.
- `regra-0022` → **trinta e oito** destinos: as dezenove causas qualificadas de
  2004 a 05/11/2018, sem ressalva, e as dezenove da família sujeita ao RPC,
  com ressalva sobre a sujeição e o teto do RGPS.
- `regra-0021` → **dois** destinos: a causa comum de cada uma dessas duas
  famílias, ambas com ressalva.

O que a ressalva registra é questão **operacional**, não jurídica: em qual
etapa o teto do RGPS incide, por qual informação o Sisprev reconhece a
sujeição ao regime complementar, e se `Proporcionalidade Dias` executa a base
composta. Nenhuma delas se responde sem levar a regra a campo, e nenhuma
autoriza, por si, a ativação em produção — o que este script também confere é
que carga e produção não são a mesma coisa: `simulavel` permanece `N` nas
sessenta, de modo que a seleção passa pela instrução administrativa.

A atomicidade continua valendo, e agora com a consequência inversa: como todos
os membros de cada componente estão concluídos e confirmados (com ou sem
ressalva), os componentes entram **inteiros**.

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
    "regra-0022": (38, True, 19),
    "regra-0021": (2, True, 2),
}
TOTAL_BLOCO_C = 60
TOTAL_NA_CARGA = 60
#: Nenhuma unidade do Bloco C pode permanecer neste estado.
ESTADO_PROIBIDO = "pendente_mapeamento_sisprev"


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


def _conferir_estados_do_bloco(propostas: dict[str, dict[str, object]], bloco: set[str]) -> list[str]:
    """Nenhuma unidade do Bloco C em `pendente_mapeamento_sisprev`."""
    presos = sorted(
        pid for pid in bloco if str(propostas[pid].get("estado_implantacao") or "") == ESTADO_PROIBIDO
    )
    if not presos:
        return []
    return [
        f"{len(presos)} unidade(s) do Bloco C em {ESTADO_PROIBIDO}: {presos}. "
        "Falta de confirmação do comportamento interno do Sisprev é ressalva de "
        "homologação, não impedimento à carga."
    ]


def _conferir_carga_nao_e_producao(propostas: dict[str, dict[str, object]], bloco: set[str]) -> list[str]:
    """Entrar na carga não equivale a ativar em produção.

    O sinal disso no dado é `simulavel: N`: a regra não é resolvida sozinha pelo
    motor, e a seleção passa pela instrução administrativa, onde a data de
    ingresso e a eventual opção pelo regime complementar são conferidas antes do
    ato. Se alguma unidade virasse `S` junto com a entrada na carga, o documento
    passaria a afirmar automatismo que a homologação ainda não confirmou.
    """
    simulaveis = sorted(
        pid for pid in bloco if str((propostas[pid].get("projecao") or {}).get("simulavel") or "") != "N"
    )
    if not simulaveis:
        return []
    return [
        f"{len(simulaveis)} unidade(s) do Bloco C com `simulavel` diferente de N: {simulaveis}. "
        "A carga de homologação não pressupõe seleção automática."
    ]


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
    fora = todos - do_bloco_na_carga
    if fora:
        violacoes.append(f"nenhum destino do Bloco C deveria ficar fora da carga, ficaram {sorted(fora)}")

    violacoes += _conferir_estados_do_bloco(propostas, todos)
    violacoes += _conferir_carga_nao_e_producao(propostas, todos)
    return violacoes


def main() -> int:
    """CLI: sai com 1 listando toda violação do mapa da carga do Bloco C."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    violacoes = conferir()
    if violacoes:
        logger.error("Carga de homologação do Bloco C não confere:\n%s", "\n".join(violacoes))
        return 1
    logger.info(
        "Carga de homologação do Bloco C confere: %d destinos ao todo, %d na carga, "
        "nenhum fora e nenhum em pendente_mapeamento_sisprev. Vinte e duas unidades "
        "entram com ressalva (a causa comum de cada família e as vinte sujeitas ao "
        "RPC); os quatro componentes entram inteiros, pela atomicidade. `simulavel` "
        "permanece N nas sessenta: a carga confere o sistema, não ativa produção.",
        TOTAL_BLOCO_C,
        TOTAL_NA_CARGA,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
