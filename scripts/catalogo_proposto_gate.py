"""RFC 0004 §14 + RFC 0006 fase 1 — CI gate do catálogo auditado e dos grupos.

Read-only, mesma postura de ``validar_regras.py``: carrega o bundle auditado,
lê os grupos de substituição declarados por **todo conjunto cujo contrato
valida** e devolve ``Violation``s que ``validar_regras.py`` anexa ao payload
existente — nunca uma forma nova de JSON, nunca um caminho de saída novo.
Bundle auditado vazio e conjunto sem grupos devem ambos passar limpo (RFC
0004 §14).

**Duas dimensões separadas, nunca confundidas** (é o que a reconciliação da
fase 1 preserva da Fase 1A):

1. *a unidade auditada é válida e compilável* — verificada por unidade, e por
   projeção, independentemente de qualquer grupo. Uma unidade marcada
   ``deployable`` com projeção impossível é defeito mesmo que o grupo dela
   esteja ``inativo``: "schema válido" nunca é a mesma afirmação que "projeção
   deployável válida";
2. *o grupo é válido dentro de um conjunto válido* — cardinalidade, unicidade,
   proveniência e ativação atômica, verificadas sobre os grupos declarados,
   sejam eles quais forem — **inclusive num conjunto ``proposto``**. É na
   proposta que a revisão acontece; esperar a promoção a ``vigente`` para
   reportar um defeito de declaração é descobri-lo no pior momento possível.
   (``substituicao_schema.selecionar_origem_operacional`` já implementa a
   leitura restrita a um único conjunto vigente para quem precisar dela —
   este gate ainda não a chama, porque nenhuma exportação real depende
   disso nesta fase.)

A fonte dos grupos passou a ser ``Conjunto.substituicoes`` (RFC 0006 §3); o
antigo ``manifesto-substituicao.yaml`` global foi aposentado sem migração de
dado, porque nascera vazio.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from compilador_proposta import compilar, detectar_colisoes
from deteccoes_da_proposta import detectar_na_composicao
from detections import Violation
from okf_common import DEFAULT_BUNDLE_PROPOSTO
from regra_proposta_schema import (
    RegraPropostaValidationError,
    load_regras_propostas,
    validate_bundle_proposto,
)
from substituicao_schema import id_da_ref, ref_de_regra_legada, validar_grupos

if TYPE_CHECKING:
    from pathlib import Path

    from bundle import Bundle
    from regra_proposta_schema import RegraProposta
    from substituicao_schema import GrupoSubstituicao


def _checar_unidades_deployable(unidades: list[RegraProposta], bundle_legado: Bundle) -> list[Violation]:
    """RFC 0004 §5.3/§14 — toda unidade ``deployable`` tem de compilar limpo.

    Roda independentemente de qualquer estado de grupo, e as colisões são
    verificadas entre todas as unidades compiladas, não por unidade.
    """
    legacy_regra_ids = bundle_legado.regra_ids()
    dispositivo_ids = bundle_legado.dispositivo_ids()
    violations: list[Violation] = []
    resultados = [
        compilar(
            unidade, modo="deployable", legacy_regra_ids=legacy_regra_ids, dispositivo_ids=dispositivo_ids
        )
        for unidade in unidades
        if unidade.estado_proposta == "deployable"
    ]
    for resultado in resultados:
        violations.extend(resultado.pendencias)
    violations.extend(detectar_colisoes(resultados))
    return violations


_DETECTORES_QUE_BLOQUEIAM = ("P1_NOME_REPETIDO", "P2_IGUALDADE_MATERIAL_ATIVA")


def _checar_deteccoes_da_composicao(
    unidades: list[RegraProposta],
    bundle_legado: Bundle,
) -> list[Violation]:
    """Nenhuma proposta ``deployable`` pode carregar detecção ativa de P1/P2.

    É o invariante do P7 transposto. Uma regra legada não chega a ``revisada``
    enquanto houver detecção P1/P2 que a inclua; sem esta checagem, a regra que
    vem **substituí-la** poderia entrar no sistema carregando exatamente o
    defeito que a auditoria existe para tirar — nome repetido ou igualdade
    material com outra ativa.

    A conferência é sobre a **composição resolvida** de cada conjunto, não
    sobre as propostas entre si: o que iria ao Sisprev é o que sobra do legado
    mais o que a proposta introduz, e a colisão mais provável é entre uma
    proposta e uma regra legada que o grupo não substituiu.

    Só bloqueia `deployable`. Numa proposta em `elaboracao` ou `preview` a
    detecção é informação de auditoria — "detecção ≠ conclusão" vale aqui como
    em todo o resto: quem conclui é o achado, escrito à mão.
    """
    deployable = {u.doc_id for u in unidades if u.estado_proposta == "deployable"}
    if not deployable:
        return []

    violations: list[Violation] = []
    for conjunto in bundle_legado.conjuntos:
        if conjunto.contract is None:
            continue
        for deteccao in detectar_na_composicao(conjunto.doc_id, bundle=bundle_legado, propostas=unidades):
            if deteccao.detector not in _DETECTORES_QUE_BLOQUEIAM:
                continue
            alcancadas = sorted(deteccao.regras & deployable)
            if not alcancadas:
                continue
            violations.append(
                Violation(
                    "PROPOSTA_DETECCAO_ATIVA",
                    f"[{conjunto.doc_id}] {', '.join(alcancadas)}: {deteccao.detector} "
                    f"na composição, com {sorted(deteccao.regras)}",
                )
            )
    return violations


def _grupos_para_validar(bundle_legado: Bundle) -> list[tuple[str, list[GrupoSubstituicao]]]:
    """Os grupos de todo conjunto cujo contrato intra-documento valida.

    Não só o vigente: uma proposta (``situacao: proposto``) precisa falhar
    cedo, no momento em que é autorada — é aí que a revisão de fato acontece
    (RFC 0006 §6). Um conjunto cujo contrato não valida não tem
    ``substituicoes`` confiáveis para ler — quem reporta isso é
    ``validate_conjuntos`` (P15_CONJUNTO_INVALIDO), não este gate.
    """
    return [
        (conjunto.doc_id, list(conjunto.contract.substituicoes))
        for conjunto in bundle_legado.conjuntos
        if conjunto.contract is not None
    ]


def _checar_achados_das_origens(bundle_legado: Bundle) -> list[Violation]:
    """Um grupo não ativa enquanto as origens dele tiverem achado aberto sem disposição.

    A análise de achado é ato humano e precede a substituição: promover uma
    regra proposta com a origem ainda carregando defeito não respondido
    trocaria a regra sem nunca dizer o que aconteceu com o problema que a
    auditoria achou nela. O achado ficaria aberto para sempre, apontando uma
    regra que saiu do catálogo.

    A trava é na **ativação**, não na autoria da proposta. Autorar a substituta
    é justamente parte de responder ao achado — muitas vezes a resposta *é* a
    substituição, e proibir a autoria antes da disposição tornaria a disposição
    impossível de escrever, porque ela precisa nomear o grupo.

    Não exige que o achado esteja fechado: ele segue aberto enquanto houver
    outra regra da população sem responder, e isso não é problema desta origem.
    O que se exige é que **esta** regra tenha disposto.
    """
    abertos = bundle_legado.open_achados()
    if not abertos:
        return []
    disposicoes_por_regra = {
        regra.doc_id: {
            item.achado.rsplit("/", 1)[-1].removesuffix(".md")
            for item in (regra.admin.disposicao_de_achados if regra.admin is not None else ())
        }
        for regra in bundle_legado.regras
    }

    violations: list[Violation] = []
    for conjunto in bundle_legado.conjuntos:
        if conjunto.contract is None:
            continue
        for grupo in conjunto.contract.substituicoes:
            if grupo.estado_grupo != "ativo":
                continue
            for ref in grupo.origens_legacy:
                regra_id = id_da_ref(ref)
                pendentes = sorted(
                    achado.doc_id
                    for achado in abertos
                    if regra_id in {r.rsplit("/", 1)[-1].removesuffix(".md") for r in achado.regras_afetadas}
                    and achado.doc_id not in disposicoes_por_regra.get(regra_id, frozenset())
                )
                if pendentes:
                    violations.append(
                        Violation(
                            "P15_ORIGEM_COM_ACHADO_PENDENTE",
                            f"[{conjunto.doc_id}] grupo {grupo.grupo!r}: origem {regra_id} tem "
                            f"achado aberto sem disposição ({', '.join(pendentes)}) — a análise "
                            "precede a substituição",
                        )
                    )
    return violations


def check_catalogo_proposto(
    bundle_legado: Bundle,
    *,
    bundle_proposto_dir: Path = DEFAULT_BUNDLE_PROPOSTO,
) -> list[Violation]:
    """Roda todo gate estrutural do catálogo auditado contra o estado real do repo.

    Um documento de unidade malformado vira ``Violation`` estável em vez de
    exceção — a forma do payload ``--json`` tem de sobreviver a um documento
    corrompido do mesmo jeito que sobrevive a qualquer outra falha de
    invariante.
    """
    try:
        unidades = load_regras_propostas(bundle_proposto_dir)
    except RegraPropostaValidationError as exc:
        return [Violation("PROPOSTA_DOCUMENTO_INVALIDO", str(exc))]

    violations = validate_bundle_proposto(unidades, bundle_legado)
    violations.extend(_checar_unidades_deployable(unidades, bundle_legado))
    violations.extend(_checar_deteccoes_da_composicao(unidades, bundle_legado))
    violations.extend(_checar_achados_das_origens(bundle_legado))

    refs_legadas = frozenset(ref_de_regra_legada(rid) for rid in bundle_legado.regra_ids())
    for conjunto_id, grupos in _grupos_para_validar(bundle_legado):
        violations.extend(
            Violation(v.code, f"[{conjunto_id}] {v.message}")
            for v in validar_grupos(grupos, unidades=unidades, refs_legadas=refs_legadas)
        )
    return violations
