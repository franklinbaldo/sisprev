"""Roda os detectores da auditoria sobre a composição que uma proposta produziria.

Os detectores do P1/P2 e as co-ocorrências existem porque o catálogo recebido
tinha nome repetido, regras materialmente idênticas e combinações de campos
que não se sustentam. Eles percorrem o bundle legado — e **só** ele. A proposta
de um ciclo, que é o que vai substituí-lo, nunca passou por nenhum deles.

Isso é assimetria sem justificativa: uma regra proposta compila exatamente para
a mesma linha de 27 colunas que uma regra legada ocupa, então todo defeito que
os detectores sabem achar numa pode existir na outra. Uma decomposição
descuidada reintroduz duas regras materialmente iguais; um nome copiado da
origem colide com o da regra que sobreviveu ao grupo. Sem esta passagem, o
catálogo seria auditado para tirar defeitos que a sua substituta poderia
recolocar sem que nada acusasse.

**A checagem é sobre a composição resolvida, não sobre as propostas isoladas.**
O que iria ao Sisprev é a união do que sobra do legado com o que a proposta
introduz, e o defeito mais provável mora exatamente na fronteira: uma proposta
que colide com uma regra legada que o grupo **não** substituiu. Conferir só as
propostas entre si deixaria justamente esse caso passar.

**Os detectores são reusados verbatim**, sobre um `Bundle` sintético montado a
partir das linhas compiladas. Reimplementar a igualdade material aqui criaria
uma segunda definição de "materialmente igual", livre para divergir daquela que
o gate do catálogo legado aplica — e é a divergência entre as duas que
ninguém veria.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from bundle import Bundle, Regra, collect_detections
from ciclo_homologacao import CicloSemGruposError, linhas_de_homologacao
from conjunto_schema import ResolucaoError, resolve
from regra_schema import FRONTMATTER_KEYS
from substituicao_schema import id_da_ref

if TYPE_CHECKING:
    from collections.abc import Sequence

    from detections import Detection
    from regra_proposta_schema import RegraProposta


def _regra_sintetica(doc_id: str, linha: dict[str, str]) -> Regra:
    """Monta a `Regra` que uma linha compilada ocuparia no catálogo.

    O frontmatter é a projeção, mais o mínimo que os accessors do `Regra`
    esperam. `status_regra` fica `ativa` porque uma proposta que entra no
    catálogo entra ativa — é o que `active_regras()` precisa enxergar para
    que o P2 a compare com as legadas sobreviventes.
    """
    frontmatter: dict[str, object] = dict.fromkeys(FRONTMATTER_KEYS.values(), "")
    frontmatter.update(linha)
    frontmatter["type"] = "Regra"
    frontmatter["id"] = doc_id
    return Regra(doc_id=doc_id, frontmatter=frontmatter)


def bundle_da_composicao(
    conjunto_id: str,
    *,
    bundle: Bundle,
    propostas: Sequence[RegraProposta],
) -> Bundle:
    """Monta o `Bundle` sintético da composição que ``conjunto_id`` produziria.

    Junta as regras legadas que **sobrevivem** à resolução com as regras
    propostas compiladas. O resultado não tem `bundle_dir` e não é gravável:
    existe só para os detectores percorrerem.
    """
    # `incluir_grupos_inativos=True`: a pergunta aqui é "o que esta proposta
    # produziria", não "o que está em vigor". Com o default operacional, um
    # ciclo inteiro de grupos inativos resolveria para o catálogo legado e a
    # conferência não veria proposta nenhuma.
    pertinencia = resolve(
        conjunto_id,
        {c.doc_id: c for c in bundle.conjuntos},
        bundle.catalogo_legado,
        incluir_grupos_inativos=True,
    )
    ids_legados_que_ficam = {id_da_ref(ref) for ref in pertinencia}

    sobreviventes = tuple(regra for regra in bundle.regras if regra.doc_id in ids_legados_que_ficam)
    linhas = linhas_de_homologacao(
        conjunto_id,
        conjuntos=bundle.conjuntos,
        propostas=propostas,
        bundle=bundle,
    )
    novas = tuple(_regra_sintetica(linha.proposta_id, linha.linha) for linha in linhas)
    return Bundle(regras=(*sobreviventes, *novas))


def detectar_na_composicao(
    conjunto_id: str,
    *,
    bundle: Bundle,
    propostas: Sequence[RegraProposta],
) -> list[Detection]:
    """Devolve as detecções que a composição de ``conjunto_id`` produziria.

    Devolve lista vazia se o conjunto não resolve — quem reporta resolução
    quebrada é ``validate_conjuntos``, e duplicar a acusação aqui daria duas
    violações para um defeito só. Também devolve vazia para um conjunto sem
    grupo algum, como a raiz: ali a composição **é** o catálogo legado, que os
    detectores já percorrem pelo gate próprio — reportar de novo daria a mesma
    detecção duas vezes, com dois fingerprints de origens diferentes.
    """
    try:
        composicao = bundle_da_composicao(conjunto_id, bundle=bundle, propostas=propostas)
    except (ResolucaoError, CicloSemGruposError):
        return []
    return collect_detections(composicao)
