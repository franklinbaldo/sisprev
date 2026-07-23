"""RFC 0004 §5/§6/§10 — the pure, deterministic A → B compiler (Fase 1A: verification mode only).

Never writes to the legacy bundle or the operational CSV — ``compilar()``/
``verificar()`` are pure functions over already-loaded ``UnidadeAuditada``
docs, returning in-memory results a caller may inspect or discard. Nothing
here is wired into ``gerar_indices.py`` or ``okf_to_csv.py`` (deferred to a
later phase, RFC 0004 §15 Fase 2).

Two compilation levels (RFC 0004 §5.3), never confused:

- **preview** — admits operational pendencies; the projection is produced
  and annotated, but its result is *always* ``deployable=False``. It exists
  to let a human review the model, not to ship it.
- **deployable** — fail-closed: any operational pendency, missing role,
  missing provenance, or incoherence blocks compilation outright
  (``linha``/``envelope`` come back ``None``); the unit's own
  ``estado_unidade`` must also already be ``"deployable"``.

The compiler is one-directional: predicate → text. It never reads
``nome``/``fundamentacao*`` prose to infer a predicate (RFC 0004 §12.2's
invariant, restated here for the compiler itself) — see
``papeis_projecao`` for the declared role contract this module implements.
"""

from __future__ import annotations

import datetime
import re
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from detections import Violation, canonical_json
from papeis_projecao import (
    EFEITO_DERIVADO_FIELDS,
    INTERFACE_FIELD,
    SUPORTE_JURIDICO_FIELD,
    is_fundamentacao_field,
)
from regra_schema import COLUMNS
from unidade_auditada_schema import (
    LEGACY_FRONTMATTER_KEYS,
    PENDENTE,
    RequisitoVerificacaoHumana,
    UnidadeAuditadaFrontmatter,
)

if TYPE_CHECKING:
    from unidade_auditada_schema import UnidadeAuditada

_DATA_FIELDS = ("data_adm_apos", "data_adm_ate", "data_direito_apos", "data_direito_ate")
_DATA_PARES = (("data_adm_apos", "data_adm_ate"), ("data_direito_apos", "data_direito_ate"))

# regra_schema.COLUMNS' own declared ``tipo`` per column (P13.2) — reused
# here, never re-decided, as the structural contract a compiled deployable
# line must satisfy (RFC 0004 §5.3's "fail-closed" extends to the target
# shape itself, not just to operational pendencies).
_SN_FIELDS = frozenset(column.frontmatter_key for column in COLUMNS if column.tipo == "S/N")
_BOOL_FIELDS = frozenset(column.frontmatter_key for column in COLUMNS if column.tipo == "TRUE/FALSE")
_DATETIME_FIELDS = frozenset(
    column.frontmatter_key for column in COLUMNS if column.tipo.startswith("datetime")
)
_LEGACY_DATETIME_RE = re.compile(r"^\d{2}/\d{2}/\d{4} \d{2}:\d{2}$")


def _parse_legacy_datetime(valor: str) -> datetime.datetime | None:
    try:
        return datetime.datetime.strptime(valor, "%d/%m/%Y %H:%M")  # noqa: DTZ007
    except ValueError:
        return None


def gerar_fundamentacao_projetada(requisito: RequisitoVerificacaoHumana) -> str:
    """RFC 0004 §6/§7 — template projecting a requisito onto its portador_primario text.

    Carries the predicado (1) and the protocolo (3), and explicitly points
    at the *institutional verification*, never asserting the concrete
    constatação (4) of any case (RFC 0004 §7's five-part distinction,
    §12.2's "avaliação nunca aparece sozinha"). Deterministic and testable
    against synthetic fixtures only — never invoked on real regra content
    in this PR (no real audited unit exists yet).
    """
    protocolo = requisito.protocolo_verificacao
    return (
        f"Aplicável quando {requisito.predicado}, conforme constatação de "
        f"{protocolo.responsavel} no {protocolo.momento}, mediante "
        f"{protocolo.meio_de_prova} ({protocolo.evidencia_exigida})."
    )


def _projetar_linha(contrato: UnidadeAuditadaFrontmatter) -> dict[str, str]:
    """Best-effort projection of the 27 legacy columns, regardless of pendencies.

    Used by both ``preview`` (which must show the annotated projection even
    with open pendencies) and ``verificar`` (which needs a projection to
    diff against, independent of deployable-readiness).
    """
    linha = dict.fromkeys(LEGACY_FRONTMATTER_KEYS, "")
    linha.update(contrato.projecao)  # directly-authored values (§4/§6)
    for requisito in contrato.requisitos_verificacao_humana:
        campo = requisito.portador_primario
        # Templated auto-fill only ever targets a fundamentação carrier
        # (RFC 0004 §6) — a requisito pointing at a structured column
        # (e.g. `sexo`) that the unit never populated directly stays empty,
        # a real P_COMPILA_SEM_PORTADOR, not a silently synthesized value.
        if is_fundamentacao_field(campo) and not linha.get(campo, "").strip():
            linha[campo] = gerar_fundamentacao_projetada(requisito)
    datas = contrato.aplicabilidade_temporal.datas_legadas
    for campo in _DATA_FIELDS:
        valor = getattr(datas, campo)
        if valor and valor != PENDENTE:
            linha[campo] = valor
    return linha


def _checar_origens(
    contrato: UnidadeAuditadaFrontmatter, unidade_id: str, *, legacy_regra_ids: frozenset[str]
) -> list[Violation]:
    return [
        Violation(
            "P_COMPILA_ORIGEM_INEXISTENTE", f"{unidade_id}: origem {origem!r} não existe no bundle legado"
        )
        for origem in contrato.origens_legacy
        if origem not in legacy_regra_ids
    ]


def _checar_portadores(
    contrato: UnidadeAuditadaFrontmatter, unidade_id: str, linha: dict[str, str]
) -> list[Violation]:
    return [
        Violation(
            "P_COMPILA_SEM_PORTADOR",
            f"{unidade_id}: requisito {requisito.predicado!r} sem conteúdo em "
            f"portador_primario={requisito.portador_primario!r}",
        )
        for requisito in contrato.requisitos_verificacao_humana
        if not linha.get(requisito.portador_primario, "").strip()
    ]


def _checar_coerencia_causa(
    contrato: UnidadeAuditadaFrontmatter, unidade_id: str, linha: dict[str, str]
) -> list[Violation]:
    """RFC 0004 §10 — a causa_incapacidade predicate and its requisito must be declared together."""
    tem_requisito_fundamentacao = any(
        is_fundamentacao_field(r.portador_primario) for r in contrato.requisitos_verificacao_humana
    )
    if contrato.predicados.causa_incapacidade is None:
        if tem_requisito_fundamentacao:
            return [
                Violation(
                    "P_COMPILA_INCOERENTE",
                    f"{unidade_id}: requisito_verificacao_humana com portador fundamentacao* sem "
                    "predicados.causa_incapacidade correspondente",
                )
            ]
        return []

    pendencias: list[Violation] = []
    if not tem_requisito_fundamentacao:
        pendencias.append(
            Violation(
                "P_COMPILA_INCOERENTE",
                f"{unidade_id}: predicados.causa_incapacidade="
                f"{contrato.predicados.causa_incapacidade!r} sem requisito_verificacao_humana "
                "com portador fundamentacao*",
            )
        )
    pendencias.extend(
        Violation("P_COMPILA_PENDENTE", f"{unidade_id}: campo operacional {campo!r} pendente")
        for campo in (*EFEITO_DERIVADO_FIELDS, INTERFACE_FIELD)
        if not linha.get(campo, "").strip()
    )
    return pendencias


def _checar_temporalidade(contrato: UnidadeAuditadaFrontmatter, unidade_id: str) -> list[Violation]:
    """RFC 0004 §5.1/§16.2 — versao_rol/datas_legadas pendencies, never generated."""
    pendencias: list[Violation] = []
    if contrato.aplicabilidade_temporal.versao_rol == PENDENTE:
        pendencias.append(
            Violation("P_COMPILA_PENDENTE", f"{unidade_id}: aplicabilidade_temporal.versao_rol pendente")
        )

    datas = contrato.aplicabilidade_temporal.datas_legadas
    if contrato.predicados.regime is not None or contrato.predicados.marco_ingresso is not None:
        valores = [getattr(datas, campo) for campo in _DATA_FIELDS]
        if all(not valor for valor in valores):
            pendencias.append(
                Violation(
                    "P_COMPILA_PENDENTE",
                    f"{unidade_id}: datas_legadas ausentes para regime/marco_ingresso declarado",
                )
            )
        pendencias.extend(
            Violation("P_COMPILA_PENDENTE", f"{unidade_id}: data legada pendente")
            for valor in valores
            if valor == PENDENTE
        )
    return pendencias


def _checar_proveniencia(
    contrato: UnidadeAuditadaFrontmatter, unidade_id: str, *, dispositivo_ids: frozenset[str]
) -> list[Violation]:
    pendencias = [
        Violation(
            "P_COMPILA_SEM_PROVENIENCIA",
            f"{unidade_id}: taxonomia {taxonomia.ref!r} não resolve a dispositivo autorado",
        )
        for taxonomia in contrato.taxonomias
        if taxonomia.ref.removeprefix("/dispositivos/").removesuffix(".md") not in dispositivo_ids
    ]
    if contrato.proveniencia is None or not contrato.proveniencia.fontes_consultadas:
        pendencias.append(Violation("P_COMPILA_SEM_PROVENIENCIA", f"{unidade_id}: proveniencia ausente"))
    return pendencias


def _checar_contrato_legado(linha: dict[str, str], unidade_id: str) -> list[Violation]:
    """Structural validation of the compiled line against the legacy target's own type contract.

    ``regra_schema.COLUMNS.tipo`` (P13.2) already declares each column's
    shape ("S/N", "TRUE/FALSE", the legacy datetime format) — this reuses
    that declared contract rather than inventing a new one, so a compiled
    line can't be considered ``deployable`` while carrying a value the
    legacy schema itself would never accept (e.g. ``integral: banana``).
    An empty value is never flagged here — "no value yet" is a pendency
    (``P_COMPILA_PENDENTE``/``P_COMPILA_SEM_PORTADOR`` elsewhere), not a
    malformed one.
    """
    pendencias: list[Violation] = []
    for campo in _SN_FIELDS:
        valor = linha.get(campo, "")
        if valor and valor not in ("S", "N"):
            pendencias.append(
                Violation("P_COMPILA_VALOR_INVALIDO", f"{unidade_id}: {campo}={valor!r} deve ser 'S' ou 'N'")
            )
    for campo in _BOOL_FIELDS:
        valor = linha.get(campo, "")
        if valor and valor not in ("TRUE", "FALSE"):
            pendencias.append(
                Violation(
                    "P_COMPILA_VALOR_INVALIDO", f"{unidade_id}: {campo}={valor!r} deve ser 'TRUE' ou 'FALSE'"
                )
            )
    for campo in _DATETIME_FIELDS:
        valor = linha.get(campo, "")
        if valor and _LEGACY_DATETIME_RE.fullmatch(valor) is None:
            pendencias.append(
                Violation(
                    "P_COMPILA_DATA_INVALIDA",
                    f"{unidade_id}: {campo}={valor!r} não está no formato DD/MM/AAAA HH:MM",
                )
            )

    for campo_apos, campo_ate in _DATA_PARES:
        apos = _parse_legacy_datetime(linha.get(campo_apos, ""))
        ate = _parse_legacy_datetime(linha.get(campo_ate, ""))
        if apos is not None and ate is not None and apos > ate:
            pendencias.append(
                Violation(
                    "P_COMPILA_DATA_INCOERENTE",
                    f"{unidade_id}: {campo_apos} ({linha[campo_apos]}) é posterior a "
                    f"{campo_ate} ({linha[campo_ate]})",
                )
            )

    if not linha.get("nome", "").strip():
        pendencias.append(Violation("P_COMPILA_PENDENTE", f"{unidade_id}: nome (campo obrigatório) ausente"))
    return pendencias


def _checar_pendencias(
    contrato: UnidadeAuditadaFrontmatter,
    unidade_id: str,
    linha: dict[str, str],
    *,
    legacy_regra_ids: frozenset[str],
    dispositivo_ids: frozenset[str],
) -> list[Violation]:
    """RFC 0004 §14 — every P_COMPILA_* pendency this compiler currently checks."""
    return [
        *_checar_origens(contrato, unidade_id, legacy_regra_ids=legacy_regra_ids),
        *_checar_portadores(contrato, unidade_id, linha),
        *_checar_coerencia_causa(contrato, unidade_id, linha),
        *_checar_temporalidade(contrato, unidade_id),
        *_checar_proveniencia(contrato, unidade_id, dispositivo_ids=dispositivo_ids),
        *_checar_contrato_legado(linha, unidade_id),
    ]


@dataclass(frozen=True)
class ResultadoCompilacao:
    """One unit's compilation result — preview is always ``deployable=False``."""

    unidade_id: str
    modo: Literal["preview", "deployable"]
    deployable: bool
    pendencias: tuple[Violation, ...]
    linha: dict[str, str] | None
    envelope: dict[str, object] | None
    id_projecao: str
    origens_legacy: tuple[str, ...]


def compilar(
    unidade: UnidadeAuditada,
    *,
    modo: Literal["preview", "deployable"],
    legacy_regra_ids: frozenset[str],
    dispositivo_ids: frozenset[str],
) -> ResultadoCompilacao:
    """Compile one audited unit in ``modo`` — pure, no I/O, no legacy-bundle writes."""
    schema_version = unidade.frontmatter.get("schema_version")
    if schema_version != 1:
        pendencias = (
            Violation(
                "P_COMPILA_SCHEMA_DESCONHECIDO",
                f"{unidade.doc_id}: schema_version={schema_version!r} desconhecido",
            ),
        )
        return ResultadoCompilacao(
            unidade_id=unidade.doc_id,
            modo=modo,
            deployable=False,
            pendencias=pendencias,
            linha=None,
            envelope=None,
            id_projecao=unidade.doc_id,
            origens_legacy=(),
        )

    contrato = unidade.contract
    if contrato is None:
        pendencias = (
            Violation(
                "P_COMPILA_FRONTMATTER_INVALIDA", f"{unidade.doc_id}: frontmatter inválida, não compilável"
            ),
        )
        return ResultadoCompilacao(
            unidade_id=unidade.doc_id,
            modo=modo,
            deployable=False,
            pendencias=pendencias,
            linha=None,
            envelope=None,
            id_projecao=unidade.doc_id,
            origens_legacy=(),
        )

    linha = _projetar_linha(contrato)
    envelope = {
        SUPORTE_JURIDICO_FIELD: [taxonomia.ref for taxonomia in contrato.taxonomias],
        "id_projecao": unidade.doc_id,
        "origens_legacy": list(contrato.origens_legacy),
    }
    pendencias = tuple(
        _checar_pendencias(
            contrato,
            unidade.doc_id,
            linha,
            legacy_regra_ids=legacy_regra_ids,
            dispositivo_ids=dispositivo_ids,
        )
    )
    origens = tuple(contrato.origens_legacy)

    if modo == "preview":
        # Preview never ships — it exists for human review of the model,
        # even when every pendency is already resolved (RFC 0004 §5.3).
        return ResultadoCompilacao(
            unidade_id=unidade.doc_id,
            modo="preview",
            deployable=False,
            pendencias=pendencias,
            linha=linha,
            envelope=envelope,
            id_projecao=unidade.doc_id,
            origens_legacy=origens,
        )

    if contrato.estado_unidade != "deployable":
        pendencias = (
            *pendencias,
            Violation(
                "P_COMPILA_ESTADO_INVALIDO",
                f"{unidade.doc_id}: estado_unidade={contrato.estado_unidade!r}, exige 'deployable'",
            ),
        )
    if pendencias:
        return ResultadoCompilacao(
            unidade_id=unidade.doc_id,
            modo="deployable",
            deployable=False,
            pendencias=pendencias,
            linha=None,
            envelope=None,
            id_projecao=unidade.doc_id,
            origens_legacy=origens,
        )
    return ResultadoCompilacao(
        unidade_id=unidade.doc_id,
        modo="deployable",
        deployable=True,
        pendencias=(),
        linha=linha,
        envelope=envelope,
        id_projecao=unidade.doc_id,
        origens_legacy=origens,
    )


@dataclass(frozen=True)
class ResultadoVerificacao:
    """RFC 0004 §5/§14 — P_COMPILA_DIVERGE candidates: one message per diverging column."""

    unidade_id: str
    divergencias: tuple[str, ...]


def verificar(unidade: UnidadeAuditada, valores_esperados: dict[str, str]) -> ResultadoVerificacao:
    """Compare the unit's best-effort projection against caller-supplied expected values.

    Never rewrites the unit — RFC 0004 §5.3: "não reescreve automaticamente
    nenhuma regra."
    """
    contrato = unidade.contract
    if contrato is None:
        return ResultadoVerificacao(
            unidade_id=unidade.doc_id,
            divergencias=(f"{unidade.doc_id}: frontmatter inválida, não verificável",),
        )
    linha = _projetar_linha(contrato)
    divergencias = tuple(
        f"{unidade.doc_id}: campo {campo!r} esperado {esperado!r}, projetado {linha.get(campo, '')!r}"
        for campo, esperado in valores_esperados.items()
        if linha.get(campo, "") != esperado
    )
    return ResultadoVerificacao(unidade_id=unidade.doc_id, divergencias=divergencias)


def ordenar_compilacoes(
    resultados: list[ResultadoCompilacao], *, legacy_row_index: dict[str, int]
) -> list[ResultadoCompilacao]:
    """RFC 0004 §1.6 — the total order's first two rules, applied to audited compilations.

    1. primary key: the smallest ``row_index`` among a unit's origens_legacy
       (also correctly covers an N:1 consolidation — the min across every
       origin in the group);
    2. tie-break between descendants of the same origin (1:N): the audited
       unit's own id.

    Rules 3/4 of the RFC's total order (interleaving not-yet-replaced
    legacy rows into the same merged sequence) belong to the operational
    export this PR deliberately does not wire up yet (RFC 0004 §15, Fase 2)
    — this function only orders a set of *compiled audited units* among
    themselves, which is what Fase 1A's compiler API produces.
    """

    def chave(resultado: ResultadoCompilacao) -> tuple[int, str]:
        indices = [
            legacy_row_index[origem] for origem in resultado.origens_legacy if origem in legacy_row_index
        ]
        primaria = min(indices) if indices else len(legacy_row_index) + 1
        return (primaria, resultado.id_projecao)

    return sorted(resultados, key=chave)


def detectar_colisoes(resultados: list[ResultadoCompilacao]) -> list[Violation]:
    """RFC 0004 §10/§14 — P_COMPILA_COLISAO over the material key (27 columns minus nome).

    Fase 1A has no achado-based override mechanism yet (that needs the
    ``pode_persistir`` wiring RFC 0004 §10 describes, deferred alongside
    the control-1 semantic detector) — every collision found here is
    unconditional, never silently allowed to persist.
    """
    groups: dict[str, list[str]] = {}
    for resultado in resultados:
        if not resultado.deployable or resultado.linha is None:
            continue
        chave_material = canonical_json({k: v for k, v in resultado.linha.items() if k != "nome"})
        groups.setdefault(chave_material, []).append(resultado.unidade_id)
    return [
        Violation("P_COMPILA_COLISAO", f"unidades {sorted(ids)} compilam para a mesma chave material")
        for ids in groups.values()
        if len(ids) > 1
    ]
