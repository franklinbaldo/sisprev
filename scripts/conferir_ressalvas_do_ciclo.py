"""Confere as populações de ressalva do Ciclo 1 contra o catálogo.

Três coisas conviviam sob a palavra "ressalva" e precisavam ser separadas, cada
uma com a sua contagem:

- a **ressalva de homologação**, atributo da regra proposta
  (`estado_implantacao: confirmada_com_ressalva`), que condiciona a ativação em
  produção da regra que alcança;
- a **conferência em aberto**, questão que a auditoria deixou por responder no
  corpo de uma regra, dirigida ao Instituto;
- a **dependência externa**, matéria que depende de definição institucional
  ainda não produzida.

Somá-las fazia o componente cuja única regra é uma causa comum ressalvada
anunciar "0 ressalvas": verdade sobre as conferências, falsidade sobre a regra.
Este gate fixa cada população e a sua classe contra os dados, de modo que a
distinção não possa se desfazer em silêncio.

A **classe** de cada ressalva sai dos predicados estruturados, não do texto da
ressalva: classificação por correspondência textual já produziu atribuição
errada neste repositório.
"""

from __future__ import annotations

import logging
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from derivar import _regras_propostas

logger = logging.getLogger(__name__)

PREFIXO = "incapacidade-lce1100-"
TOTAL = 60
COM_RESSALVA = 22
SEM_RESSALVA = 38
PROPORCIONALIZACAO = 3
RPC_TETO = 20
ACUMULAM = 1

#: A dependência externa que não é ressalva de implantação de regra alguma.
DEPENDENCIA_EXTERNA = "C1-R75"


def _bloco() -> dict[str, dict[str, object]]:
    return {p: fm for p, fm in _regras_propostas().items() if p.startswith(PREFIXO)}


def _leva_ressalva(fm: dict[str, object]) -> bool:
    """Se a regra leva ressalva de homologação — pelo estado, que é a fonte.

    A população das ressalvadas é o que `estado_implantacao` declara, e nada
    mais. Derivá-la das classes atribuídas tornava a conferência tautológica:
    uma regra `confirmada_com_ressalva` sem nenhum dos predicados reconhecidos
    simplesmente saía da população, e a comparação com as classes fechava
    sempre. Era exatamente a regra perdida que o gate precisava acusar.
    """
    return str(fm.get("estado_implantacao")) == "confirmada_com_ressalva"


def _classes(fm: dict[str, object]) -> set[str]:
    """As classes de ressalva de uma regra — vazio se ela não leva ressalva."""
    if not _leva_ressalva(fm):
        return set()
    predicados = fm.get("predicados") or {}
    classes = set()
    if predicados.get("causa_incapacidade") == "causa_comum":  # type: ignore[union-attr]
        classes.add("proporcionalizacao")
    if predicados.get("vinculo_rpc") == "sujeito":  # type: ignore[union-attr]
        classes.add("rpc_teto")
    return classes


def _conferir_populacoes(bloco: dict[str, dict[str, object]]) -> list[str]:
    """As contagens das três populações e das duas classes."""
    violacoes = []
    if len(bloco) != TOTAL:
        violacoes.append(f"esperava {TOTAL} regras propostas no Bloco C, achou {len(bloco)}")

    por_classe = {p: _classes(fm) for p, fm in bloco.items()}
    # Pelo estado, nunca pelas classes: ver `_leva_ressalva`.
    ressalvadas = {p for p, fm in bloco.items() if _leva_ressalva(fm)}
    if len(ressalvadas) != COM_RESSALVA:
        violacoes.append(f"esperava {COM_RESSALVA} regras com ressalva, achou {len(ressalvadas)}")
    if len(bloco) - len(ressalvadas) != SEM_RESSALVA:
        violacoes.append(
            f"esperava {SEM_RESSALVA} regras sem ressalva, achou {len(bloco) - len(ressalvadas)}"
        )

    prop = {p for p, c in por_classe.items() if "proporcionalizacao" in c}
    rpc = {p for p, c in por_classe.items() if "rpc_teto" in c}
    if len(prop) != PROPORCIONALIZACAO:
        violacoes.append(f"esperava {PROPORCIONALIZACAO} na classe da proporcionalização, achou {len(prop)}")
    if len(rpc) != RPC_TETO:
        violacoes.append(f"esperava {RPC_TETO} na classe do teto do RGPS, achou {len(rpc)}")
    if len(prop & rpc) != ACUMULAM:
        violacoes.append(f"esperava {ACUMULAM} regra acumulando as duas classes, achou {len(prop & rpc)}")
    # Agora a comparação tem lados independentes: à esquerda o que os
    # predicados classificam, à direita o que o estado declara. Uma classe
    # futura que ninguém tivesse implementado, ou um predicado apagado por
    # acidente, aparecem aqui como regra ressalvada sem classe — e sumiriam do
    # Anexo II e das contagens sem este confronto.
    classificadas = {p for p, c in por_classe.items() if c}
    sem_classe = sorted(ressalvadas - classificadas)
    if sem_classe:
        violacoes.append(
            f"{len(sem_classe)} regra(s) com estado_implantacao "
            f"confirmada_com_ressalva sem classe reconhecida: {sem_classe[:3]}"
        )
    classe_sem_ressalva = sorted(classificadas - ressalvadas)
    if classe_sem_ressalva:
        violacoes.append(
            f"{len(classe_sem_ressalva)} regra(s) com classe atribuída sem ressalva "
            f"de homologação: {classe_sem_ressalva[:3]}"
        )

    # Toda ressalvada precisa ter o texto da ressalva: o estado promete uma
    # conferência registrada, e sem ela o rótulo não se sustenta.
    sem_texto = sorted(p for p in ressalvadas if not str(bloco[p].get("ressalva_homologacao") or "").strip())
    if sem_texto:
        violacoes.append(f"{len(sem_texto)} regra(s) ressalvada(s) sem texto de ressalva: {sem_texto[:3]}")
    return violacoes


def _conferir_dependencia_externa(bloco: dict[str, dict[str, object]]) -> list[str]:
    """A dependência externa não entra na contagem das ressalvas de homologação.

    O protocolo do nexo de moléstia profissional é matéria a definir pelo
    Instituto, e não conferência sobre o comportamento do sistema. Se ele
    passasse a contar como classe, a população das ressalvadas mudaria sem que
    regra alguma tivesse mudado de estado.
    """
    alcancadas = {
        p
        for p, fm in bloco.items()
        if DEPENDENCIA_EXTERNA in (Path(f"okf/regras-propostas/regras/{p}.md").read_text(encoding="utf-8"))
    }
    if not alcancadas:
        return [f"{DEPENDENCIA_EXTERNA} não aparece em regra alguma — a dependência externa sumiu"]

    sem_ressalva = {p for p in alcancadas if not _leva_ressalva(bloco[p])}
    if not sem_ressalva:
        return [
            f"toda regra alcançada por {DEPENDENCIA_EXTERNA} leva ressalva de homologação; "
            "a dependência externa deixou de ser distinguível da ressalva"
        ]
    return []


def _conferir_conferencias(bloco: dict[str, dict[str, object]]) -> list[str]:
    """Conferências em aberto e ressalvas são populações independentes.

    O caso que importa é o do componente com regra ressalvada e nenhuma
    conferência aberta: ele existe no catálogo, e é o que fazia o selo mentir.
    """
    violacoes = []
    abertas: dict[str, int] = {}
    for p in bloco:
        corpo = Path(f"okf/regras-propostas/regras/{p}.md").read_text(encoding="utf-8").split("---", 2)[-1]
        abertas[p] = len(re.findall(r"^- \[ \] ", corpo, re.MULTILINE))

    ressalvada_sem_conferencia = [p for p in bloco if _leva_ressalva(bloco[p]) and abertas[p] == 0]
    if not ressalvada_sem_conferencia:
        violacoes.append(
            "nenhuma regra ressalvada tem zero conferências em aberto: o caso que separa as "
            "duas populações desapareceu do catálogo, e o gate deixaria de protegê-lo"
        )

    conferencia_sem_ressalva = [p for p in bloco if abertas[p] > 0 and not _leva_ressalva(bloco[p])]
    if not conferencia_sem_ressalva:
        violacoes.append(
            "nenhuma regra tem conferência em aberto sem ressalva de homologação: o caso "
            "recíproco também desapareceu"
        )
    return violacoes


def conferir() -> list[str]:
    """As violações das populações de ressalva; lista vazia se tudo confere."""
    bloco = _bloco()
    return [
        *_conferir_populacoes(bloco),
        *_conferir_dependencia_externa(bloco),
        *_conferir_conferencias(bloco),
    ]


def main() -> int:
    """CLI: sai com 1 listando toda divergência nas populações de ressalva."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    violacoes = conferir()
    if violacoes:
        logger.error("As populações de ressalva não conferem:\n%s", "\n".join(violacoes))
        return 1
    logger.info(
        "Populações de ressalva conferem: %d regras, %d com ressalva de homologação e %d sem; "
        "%d na classe da proporcionalização, %d na do teto do RGPS, %d acumulando as duas. "
        "A dependência externa do nexo de moléstia profissional segue fora das classes, e "
        "conferência em aberto continua sendo população distinta da ressalva.",
        TOTAL,
        COM_RESSALVA,
        SEM_RESSALVA,
        PROPORCIONALIZACAO,
        RPC_TETO,
        ACUMULAM,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
