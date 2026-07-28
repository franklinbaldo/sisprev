"""RFC 0004 §14 + RFC 0006 fase 1 — CI gate do catálogo auditado e dos grupos.

Read-only, mesma postura de ``validar_regras.py``: carrega o bundle auditado,
lê os grupos de substituição do **conjunto vigente** e devolve ``Violation``s
que ``validar_regras.py`` anexa ao payload existente — nunca uma forma nova de
JSON, nunca um caminho de saída novo. Bundle auditado vazio e conjunto sem
grupos devem ambos passar limpo (RFC 0004 §14).

**Duas dimensões separadas, nunca confundidas** (é o que a reconciliação da
fase 1 preserva da Fase 1A):

1. *a unidade auditada é válida e compilável* — verificada por unidade, e por
   projeção, independentemente de qualquer grupo. Uma unidade marcada
   ``deployable`` com projeção impossível é defeito mesmo que o grupo dela
   esteja ``inativo``: "schema válido" nunca é a mesma afirmação que "projeção
   deployável válida";
2. *o grupo é válido dentro de um conjunto válido* — cardinalidade, unicidade,
   proveniência e ativação atômica, verificadas sobre os grupos declarados,
   sejam eles quais forem.

A fonte dos grupos passou a ser ``Conjunto.substituicoes`` (RFC 0006 §3); o
antigo ``manifesto-substituicao.yaml`` global foi aposentado sem migração de
dado, porque nascera vazio.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from compilador_auditado import compilar, detectar_colisoes
from conjunto_schema import conjunto_vigente
from detections import Violation
from okf_common import DEFAULT_BUNDLE_AUDITADO
from substituicao_schema import ref_de_regra_legada, validar_grupos
from unidade_auditada_schema import (
    UnidadeAuditadaValidationError,
    load_unidades_auditadas,
    validate_bundle_auditado,
)

if TYPE_CHECKING:
    from pathlib import Path

    from bundle import Bundle
    from substituicao_schema import GrupoSubstituicao
    from unidade_auditada_schema import UnidadeAuditada


def _checar_unidades_deployable(unidades: list[UnidadeAuditada], bundle_legado: Bundle) -> list[Violation]:
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
        if unidade.estado_unidade == "deployable"
    ]
    for resultado in resultados:
        violations.extend(resultado.pendencias)
    violations.extend(detectar_colisoes(resultados))
    return violations


def grupos_vigentes(bundle_legado: Bundle) -> list[GrupoSubstituicao]:
    """Os grupos de substituição declarados pelo conjunto em vigor.

    Vazio quando não há conjunto vigente único ou quando o dele não valida —
    quem reporta isso é ``validate_conjuntos`` (P15), e ler grupos de um
    documento que já se sabe quebrado só empilharia violações derivadas em
    cima da causa.
    """
    vigente = conjunto_vigente(bundle_legado.conjuntos)
    if vigente is None or vigente.contract is None:
        return []
    return list(vigente.contract.substituicoes)


def check_catalogo_auditado(
    bundle_legado: Bundle,
    *,
    bundle_auditado_dir: Path = DEFAULT_BUNDLE_AUDITADO,
) -> list[Violation]:
    """Roda todo gate estrutural do catálogo auditado contra o estado real do repo.

    Um documento de unidade malformado vira ``Violation`` estável em vez de
    exceção — a forma do payload ``--json`` tem de sobreviver a um documento
    corrompido do mesmo jeito que sobrevive a qualquer outra falha de
    invariante.
    """
    try:
        unidades = load_unidades_auditadas(bundle_auditado_dir)
    except UnidadeAuditadaValidationError as exc:
        return [Violation("AUDITADA_DOCUMENTO_INVALIDO", str(exc))]

    violations = validate_bundle_auditado(unidades, bundle_legado)
    violations.extend(_checar_unidades_deployable(unidades, bundle_legado))
    violations.extend(
        validar_grupos(
            grupos_vigentes(bundle_legado),
            unidades=unidades,
            refs_legadas=frozenset(ref_de_regra_legada(rid) for rid in bundle_legado.regra_ids()),
        )
    )
    return violations
