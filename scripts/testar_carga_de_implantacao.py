"""Confere, com fixtures sintéticas, as regras genéricas de `_carga_de_implantacao`.

`scripts/testar_carga_de_implantacao_bloco_c.py` confere o mapa das sessenta
unidades contra o catálogo real do Bloco C — é um teste de regressão de dados,
não da lógica do compilador. Este script é o inverso:
confere a lógica de `_carga_de_implantacao` (`scripts/derivar.py`) contra
fixtures sintéticas que o catálogo real não precisa conter, para que a
consistência entre `estado_implantacao` e `ressalva_homologacao` — genérica para
toda `RegraProposta`, não só para o Bloco C — permaneça coberta mesmo que o
catálogo real nunca produza um caso de violação.
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from derivar import _carga_de_implantacao

logger = logging.getLogger(__name__)


def _fm(
    estado_auditoria: str = "concluida",
    estado_implantacao: str | None = None,
    ressalva_homologacao: str | None = None,
) -> dict[str, object]:
    fm: dict[str, object] = {"estado_auditoria": estado_auditoria}
    if estado_implantacao is not None:
        fm["estado_implantacao"] = estado_implantacao
    if ressalva_homologacao is not None:
        fm["ressalva_homologacao"] = ressalva_homologacao
    return fm


def _prontos_ids(propostas: dict[str, dict[str, object]]) -> set[str]:
    prontos, _diagnosticos = _carga_de_implantacao(propostas)
    return {pid for pid, _origens in prontos}


def _caso_ressalva_preenchida() -> list[str]:
    """1. `confirmada_com_ressalva` com `ressalva_homologacao` preenchida entra na carga."""
    propostas = {
        "unidade-a": _fm(estado_implantacao="confirmada_com_ressalva", ressalva_homologacao="confirmar X"),
    }
    prontos, diagnosticos = _carga_de_implantacao(propostas)
    violacoes = []
    if "unidade-a" not in {pid for pid, _ in prontos}:
        violacoes.append("caso 1: unidade-a com ressalva preenchida deveria entrar na carga")
    if diagnosticos:
        violacoes.append(f"caso 1: não esperava diagnóstico, achou {diagnosticos!r}")
    return violacoes


def _caso_ressalva_ausente() -> list[str]:
    """2. `confirmada_com_ressalva` sem `ressalva_homologacao` bloqueia a carga, com diagnóstico claro."""
    propostas = {
        "unidade-b": _fm(estado_implantacao="confirmada_com_ressalva"),
    }
    prontos, diagnosticos = _carga_de_implantacao(propostas)
    violacoes = []
    if "unidade-b" in {pid for pid, _ in prontos}:
        violacoes.append("caso 2: unidade-b sem ressalva_homologacao não deveria entrar na carga")
    if not any("sem ressalva_homologacao" in d for d in diagnosticos):
        violacoes.append(
            f"caso 2: esperava diagnóstico mencionando 'sem ressalva_homologacao', achou {diagnosticos!r}"
        )
    return violacoes


def _caso_ressalva_indevida_em_confirmada_comum() -> list[str]:
    """3. `confirmada` (comum) com `ressalva_homologacao` preenchida por engano bloqueia a carga."""
    propostas = {
        "unidade-c": _fm(estado_implantacao="confirmada", ressalva_homologacao="ressalva residual indevida"),
        "unidade-d": _fm(ressalva_homologacao="idem, com estado_implantacao implícito"),
    }
    prontos, diagnosticos = _carga_de_implantacao(propostas)
    violacoes = []
    prontos_ids = {pid for pid, _ in prontos}
    if "unidade-c" in prontos_ids:
        violacoes.append("caso 3: unidade-c com ressalva indevida não deveria entrar na carga")
    if "unidade-d" in prontos_ids:
        violacoes.append(
            "caso 3: unidade-d (estado implícito) com ressalva indevida não deveria entrar na carga"
        )
    if not any("ressalva_homologacao preenchida" in d for d in diagnosticos):
        violacoes.append(
            f"caso 3: esperava diagnóstico mencionando ressalva indevida, achou {diagnosticos!r}"
        )
    return violacoes


def _caso_componente_com_membro_invalido() -> list[str]:
    """4. Um membro inválido do componente derruba o componente inteiro (troca atômica)."""
    propostas = {
        "unidade-e": _fm(estado_auditoria="concluida"),
        "unidade-f": _fm(estado_auditoria="preview"),
        # unidade-g e unidade-h compartilham origem legada: formam um único
        # componente conexo (`_componentes_conexos`), e unidade-h é inválida
        # (estado_auditoria=preview) — a troca é atômica, então unidade-g
        # (por si só válida) também deve ficar de fora.
        "unidade-g": {**_fm(estado_auditoria="concluida"), "origens_legacy": ["regra-x"]},
        "unidade-h": {**_fm(estado_auditoria="preview"), "origens_legacy": ["regra-x"]},
    }
    prontos_ids = _prontos_ids(propostas)
    violacoes = []
    if "unidade-f" in prontos_ids:
        violacoes.append("caso 4: unidade-f (estado_auditoria=preview) não deveria entrar na carga")
    if "unidade-h" in prontos_ids:
        violacoes.append("caso 4: unidade-h (estado_auditoria=preview) não deveria entrar na carga")
    if "unidade-g" in prontos_ids:
        violacoes.append(
            "caso 4: unidade-g, por si só válida, compartilha componente com unidade-h "
            "(inválida) e não deveria entrar na carga — troca não é atômica"
        )
    if "unidade-e" not in prontos_ids:
        violacoes.append(
            "caso 4: unidade-e (isolada, válida) deveria entrar na carga, "
            "sem relação com a falha de unidade-f"
        )
    return violacoes


def _caso_sem_selecao_automatica() -> list[str]:
    """5. Falta seleção automática, mas há como selecionar na instrução: entra na carga.

    A regra é `simulavel: N` e traz requisito de verificação humana — quem
    concede confere a data de ingresso e a eventual opção pelo regime
    complementar antes de escolher a regra. Ausência de automatismo é modo de
    operar, não impedimento: `_carga_de_implantacao` não olha `simulavel`, e é
    isso que este caso fixa, para que ninguém volte a tratar seleção manual
    como bloqueio.
    """
    propostas = {
        "unidade-manual": {
            **_fm(
                estado_implantacao="confirmada_com_ressalva",
                ressalva_homologacao="confirmar como o sistema identifica a sujeição",
            ),
            "projecao": {"simulavel": "N"},
            "requisitos_verificacao_humana": ["opção pelo regime complementar, conferida no processo"],
        },
    }
    if "unidade-manual" in _prontos_ids(propostas):
        return []
    return ["caso 5: unidade sem seleção automática, mas conferível na instrução, deveria entrar na carga"]


def _caso_comportamento_a_confirmar() -> list[str]:
    """6. Falta confirmar o teto automático, mas o valor é conferível antes do ato: entra com ressalva."""
    propostas = {
        "unidade-teto": _fm(
            estado_implantacao="confirmada_com_ressalva",
            ressalva_homologacao="confirmar em qual etapa o teto do RGPS incide",
        ),
    }
    prontos, diagnosticos = _carga_de_implantacao(propostas)
    violacoes = []
    if "unidade-teto" not in {pid for pid, _ in prontos}:
        violacoes.append("caso 6: unidade com comportamento a confirmar deveria entrar na carga com ressalva")
    if diagnosticos:
        violacoes.append(f"caso 6: não esperava diagnóstico, achou {diagnosticos!r}")
    return violacoes


def _caso_sem_projecao_conferivel() -> list[str]:
    """7. Sem projeção nem modo de conferência, a unidade permanece fora da carga.

    É o que sobra de `pendente_mapeamento_sisprev` depois da decisão de
    2026-08-06: não "falta confirmação do comportamento interno", e sim não há
    como sequer formular a conferência. O estado continua barrando a carga.
    """
    propostas = {
        "unidade-sem-projecao": _fm(estado_implantacao="pendente_mapeamento_sisprev"),
        "unidade-ok": _fm(),
    }
    prontos_ids = _prontos_ids(propostas)
    violacoes = []
    if "unidade-sem-projecao" in prontos_ids:
        violacoes.append("caso 7: unidade sem projeção conferível não deveria entrar na carga")
    if "unidade-ok" not in prontos_ids:
        violacoes.append("caso 7: a unidade válida, em componente próprio, deveria entrar")
    return violacoes


def _caso_componente_inteiro_entra() -> list[str]:
    """8. Componente com todos os membros confirmados ou confirmados com ressalva entra inteiro.

    O espelho do caso 4: a atomicidade disciplina a entrada **conjunta**, e não
    exige certeza operacional completa. Misturar `confirmada` e
    `confirmada_com_ressalva` no mesmo componente não o derruba.
    """
    propostas = {
        "membro-1": {**_fm(), "origens_legacy": ["regra-y"]},
        "membro-2": {
            **_fm(estado_implantacao="confirmada_com_ressalva", ressalva_homologacao="confirmar a ordem"),
            "origens_legacy": ["regra-y"],
        },
    }
    prontos_ids = _prontos_ids(propostas)
    faltando = {"membro-1", "membro-2"} - prontos_ids
    if not faltando:
        return []
    return [f"caso 8: o componente deveria entrar inteiro, ficaram de fora {sorted(faltando)}"]


def conferir() -> list[str]:
    """As violações de todos os casos sintéticos; lista vazia se tudo confere."""
    violacoes: list[str] = []
    violacoes += _caso_ressalva_preenchida()
    violacoes += _caso_ressalva_ausente()
    violacoes += _caso_ressalva_indevida_em_confirmada_comum()
    violacoes += _caso_componente_com_membro_invalido()
    violacoes += _caso_sem_selecao_automatica()
    violacoes += _caso_comportamento_a_confirmar()
    violacoes += _caso_sem_projecao_conferivel()
    violacoes += _caso_componente_inteiro_entra()
    return violacoes


def main() -> int:
    """CLI: sai com 1 listando toda violação da lógica genérica de `_carga_de_implantacao`."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    violacoes = conferir()
    if violacoes:
        logger.error("Lógica de _carga_de_implantacao não confere:\n%s", "\n".join(violacoes))
        return 1
    logger.info("Lógica genérica de _carga_de_implantacao confere nos oito casos sintéticos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
