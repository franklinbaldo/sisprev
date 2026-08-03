"""Projeção de homologação de um ciclo — as linhas que iriam para o Sisprev.

Um ciclo de auditoria conclui propondo substituir regras legadas por regras
propostas. Quem decide sobre essa proposta — a PGE, ao se manifestar, e o
IPERON, ao praticar o ato — precisa ver **o que entraria no sistema**, nas
colunas que o sistema tem, e não apenas o mapa de substituição em prosa.

Este módulo é a biblioteca pura que produz essa projeção. Ele não escreve
nada: ``gerar_indices.py`` é o único comando que materializa artefato
derivado, e é ele que chama ``linhas_de_homologacao``.

**A projeção é sempre ``preview``.** O modo ``deployable`` do compilador é
fail-closed e exige, entre outras coisas, que cada regra proposta já esteja em
``estado_proposta: deployable`` — promoção que é ato humano e que a
manifestação institucional existe justamente para destravar. Compilar em
``deployable`` aqui produziria, hoje, trinta pendências
``P_COMPILA_ESTADO_INVALIDO`` e nenhuma linha, isto é, um documento vazio
exatamente para quem precisa lê-lo antes de decidir. O CSV mostra a projeção
e diz, em coluna própria, que ela não é deployable — em vez de não existir.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, NamedTuple

from compilador_proposta import compilar
from regra_schema import CSV_COLUMN_NAMES, FRONTMATTER_KEYS
from substituicao_schema import GrupoSubstituicao, id_da_ref

if TYPE_CHECKING:
    from collections.abc import Sequence

    from bundle import Bundle
    from conjunto_schema import Conjunto
    from regra_proposta_schema import RegraProposta

#: Colunas de proveniência acrescentadas às 27 do Sisprev. Elas não vão para o
#: sistema: existem para que quem confere a planilha saiba, sem abrir o
#: repositório, de que regra proposta a linha veio, que regras ela substitui e por que
#: ela ainda não é deployable.
COLUNAS_DE_PROVENIENCIA: tuple[str, ...] = (
    "REGRA PROPOSTA",
    "GRUPO DE SUBSTITUICAO",
    "SUBSTITUI",
    "ESTADO DA PROPOSTA",
    "DEPLOYABLE",
    "PENDENCIAS",
)

COLUNAS: tuple[str, ...] = (*CSV_COLUMN_NAMES, *COLUNAS_DE_PROVENIENCIA)


class CicloSemGruposError(Exception):
    """Levantada quando o conjunto pedido não alcança grupo de substituição algum."""


class LinhaDeHomologacao(NamedTuple):
    """Uma linha projetada, com a proveniência que o CSV do Sisprev não carrega."""

    proposta_id: str
    grupo: str
    origens_legacy: tuple[str, ...]
    estado_proposta: str
    deployable: bool
    pendencias: tuple[str, ...]
    linha: dict[str, str]

    def as_csv_row(self) -> dict[str, str]:
        """Devolve a linha achatada, com os nomes de coluna do CSV do Sisprev.

        O compilador projeta em chaves de frontmatter (``nome``); o CSV do
        Sisprev é nomeado em colunas (``NOME``). A tradução é feita aqui, por
        :data:`regra_schema.FRONTMATTER_KEYS`, e não por coincidência de
        grafia — a planilha que a PGE recebe tem de ter os cabeçalhos do
        sistema, senão ninguém consegue cotejá-la com o export operacional.
        """
        return {
            **{csv_name: self.linha.get(chave, "") for csv_name, chave in FRONTMATTER_KEYS.items()},
            "REGRA PROPOSTA": self.proposta_id,
            "GRUPO DE SUBSTITUICAO": self.grupo,
            "SUBSTITUI": " ".join(id_da_ref(ref) for ref in self.origens_legacy),
            "ESTADO DA PROPOSTA": self.estado_proposta,
            "DEPLOYABLE": "S" if self.deployable else "N",
            "PENDENCIAS": " ".join(self.pendencias),
        }


def grupos_do_conjunto(
    conjunto_id: str,
    por_id: dict[str, Conjunto],
    *,
    incluir_grupos_inativos: bool = False,
) -> tuple[GrupoSubstituicao, ...]:
    """Colhe os grupos de substituição do conjunto e de toda a sua cadeia de bases.

    A ordem é da base mais antiga para a mais recente, que é a ordem em que a
    auditoria os decidiu — um capítulo por grupo, na sequência das sessões.

    Um conjunto de fechamento tipicamente não declara delta próprio: ele
    consolida o que as sessões anteriores decidiram. Ler só os deltas dele
    devolveria zero grupos e seria lido como "o ciclo não substituiu nada".

    **Só grupos ativos entram.** O CSV responde "que regras vão para o
    Sisprev nesta remessa", e um grupo inativo não vai: ele está autorado e
    conferido, mas a auditoria não o promoveu. Listá-lo apresentaria a quem
    decide um conjunto maior do que o que está sendo submetido, e a coluna
    ``ESTADO DA PROPOSTA`` não resolve — ela fala da unidade, não do grupo, e
    uma unidade em ``elaboracao`` dentro de um grupo ativo é caso diferente
    de uma unidade pronta cujo grupo ninguém ativou.

    A consequência é que o recorte do ciclo passa a ser a ativação, e não a
    cadeia de bases: um ciclo pode encerrar com parte dos seus grupos adiada
    para o seguinte sem que o CSV misture as duas remessas.

    ``incluir_grupos_inativos`` existe pelo mesmo motivo que o homônimo de
    ``conjunto_schema.resolve``, e **tem de andar junto com ele**: quem pergunta
    "o que esta proposta produziria" — a conferência de detecções sobre a
    composição — precisa das duas metades com o mesmo recorte. Resolver a
    pertinência com os inativos incluídos e colher os grupos sem eles tira as
    origens do catálogo sem pôr as substitutas no lugar, e a composição fica com
    um buraco que nenhum gate nomeia.
    """
    grupos = _grupos(conjunto_id, por_id, visitados=())
    if incluir_grupos_inativos:
        return tuple(grupos)
    return tuple(grupo for grupo in grupos if grupo.estado_grupo == "ativo")


def _grupos(
    conjunto_id: str,
    por_id: dict[str, Conjunto],
    *,
    visitados: tuple[str, ...],
) -> list[GrupoSubstituicao]:
    if conjunto_id in visitados:
        return []
    conjunto = por_id.get(conjunto_id)
    if conjunto is None:
        return []
    contrato = conjunto.contract
    if contrato is None:
        return []
    anteriores: list[GrupoSubstituicao] = []
    if contrato.base is not None:
        anteriores = _grupos(contrato.base, por_id, visitados=(*visitados, conjunto_id))
    return [*anteriores, *contrato.substituicoes]


def linhas_de_homologacao(
    conjunto_id: str,
    *,
    incluir_grupos_inativos: bool = False,
    conjuntos: Sequence[Conjunto],
    propostas: Sequence[RegraProposta],
    bundle: Bundle,
) -> tuple[LinhaDeHomologacao, ...]:
    """Projeta, em ``preview``, cada regra proposta de destino dos grupos do conjunto.

    Levanta :class:`CicloSemGruposError` se o conjunto não alcança grupo algum —
    devolver tupla vazia deixaria um CSV de zero linhas passar por "este ciclo
    não propõe nada", que é afirmação diferente de "este conjunto não é o de um
    ciclo de substituição".
    """
    grupos = grupos_do_conjunto(
        conjunto_id,
        {c.doc_id: c for c in conjuntos},
        incluir_grupos_inativos=incluir_grupos_inativos,
    )
    if not grupos:
        msg = f"{conjunto_id}: nenhum grupo de substituição na cadeia de bases"
        raise CicloSemGruposError(msg)

    por_id = {proposta.doc_id: proposta for proposta in propostas}
    legacy_regra_ids = frozenset(regra.doc_id for regra in bundle.active_regras())
    dispositivo_ids = bundle.dispositivo_ids()

    linhas: list[LinhaDeHomologacao] = []
    for grupo in grupos:
        for ref in grupo.destinos_propostos:
            proposta = por_id.get(id_da_ref(ref))
            if proposta is None:
                continue
            resultado = compilar(
                proposta,
                modo="preview",
                legacy_regra_ids=legacy_regra_ids,
                dispositivo_ids=dispositivo_ids,
            )
            linhas.append(
                LinhaDeHomologacao(
                    proposta_id=proposta.doc_id,
                    grupo=grupo.grupo,
                    origens_legacy=tuple(grupo.origens_legacy),
                    estado_proposta=str(proposta.frontmatter.get("estado_proposta") or ""),
                    deployable=resultado.deployable,
                    pendencias=tuple(pendencia.code for pendencia in resultado.pendencias),
                    linha=resultado.linha or {},
                )
            )
    return tuple(linhas)
