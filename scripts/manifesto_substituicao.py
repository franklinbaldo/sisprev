"""RFC 0004 §1.4/§1.5 — the substitution-group manifest and origin selection.

The manifest is a project envelope, not an OKF concept doc: it describes a
relationship between two bundles (which legacy rows a set of audited units
replaces) rather than being itself a rule/finding/provision. A substitution
is a **group**, never a per-unit swap — a legacy row keeps being the
operational origin until *every* destino in its group reaches
``deployable`` and the group's ``decisao_completude`` is fully recorded
(RFC 0004 §1.4).

Fase 1A invariant: the production manifest (``okf_common.DEFAULT_MANIFESTO_SUBSTITUICAO``)
must start empty or inactive-only — ``check_nenhum_grupo_ativo_em_producao``
is the gate that enforces it, called only for the real repo file, never for
the general library validation below (fixtures may exercise a real active
group).
"""

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Literal

import yaml
from concept import format_pydantic_errors
from detections import Violation
from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator

if TYPE_CHECKING:
    from pathlib import Path

    from bundle import Bundle
    from unidade_auditada_schema import UnidadeAuditada


class ManifestoValidationError(Exception):
    """Raised when the manifest file itself is not even well-formed YAML/shape."""


class DecisaoCompletude(BaseModel):
    """RFC 0004 §1.4 — the human completeness decision, structured and verifiable.

    Mirrors ``estado_auditoria.AtoValidacao``'s "same pattern" (P7/P11):
    every field a real, non-empty string — never present-but-blank.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    decidido_por: str = Field(min_length=1)
    decidido_em: datetime.date
    justificativa: str = Field(min_length=1)
    fonte: str = Field(min_length=1)

    @field_validator("decidido_em", mode="before")
    @classmethod
    def _parse_iso_date(cls, value: object) -> object:
        if value is None or isinstance(value, datetime.date):
            return value
        if isinstance(value, str):
            return datetime.date.fromisoformat(value)
        return value


class GrupoSubstituicao(BaseModel):
    """RFC 0004 §1.4 — one atomic substitution group.

    ``estado_grupo`` (the group's activation state) is deliberately a
    separate field from any destino's ``estado_unidade`` (the unit's own
    lifecycle state) — RFC 0004: "Dois estados, dois níveis — nunca
    confundidos."
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    grupo: str = Field(min_length=1)
    origens_legacy: list[str] = Field(min_length=1)
    destinos_auditados: list[str] = Field(min_length=1)
    estado_grupo: Literal["inativo", "ativo"] = "inativo"
    decisao_completude: DecisaoCompletude | None = None

    @field_validator("origens_legacy", "destinos_auditados")
    @classmethod
    def _sem_duplicatas(cls, value: list[str]) -> list[str]:
        if len(value) != len(set(value)):
            msg = "must not contain duplicates"
            raise ValueError(msg)
        return value


class ManifestoSubstituicao(BaseModel):
    """RFC 0004 §1.4 — the whole versioned manifest, one document per project."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    schema_version: Literal[1]
    grupos: list[GrupoSubstituicao] = Field(default_factory=list)


def load_manifesto(path: Path) -> ManifestoSubstituicao:
    """Parse and validate the manifest file. Raises ManifestoValidationError if malformed."""
    try:
        raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as exc:
        msg = f"manifesto is not valid YAML: {exc}"
        raise ManifestoValidationError(msg) from exc
    try:
        return ManifestoSubstituicao.model_validate(raw)
    except ValidationError as exc:
        msg = "; ".join(format_pydantic_errors("manifesto", exc))
        raise ManifestoValidationError(msg) from exc


def _grupo_ativo_incompleto(
    grupo: GrupoSubstituicao, *, unidades_by_id: dict[str, UnidadeAuditada]
) -> list[Violation]:
    violations: list[Violation] = []
    destinos_nao_deployable = [
        destino
        for destino in grupo.destinos_auditados
        if destino in unidades_by_id and unidades_by_id[destino].estado_unidade != "deployable"
    ]
    if destinos_nao_deployable:
        violations.append(
            Violation(
                "MANIFESTO_GRUPO_PARCIAL",
                f"grupo {grupo.grupo!r} está estado_grupo=ativo mas destino(s) "
                f"{destinos_nao_deployable} não estão deployable",
            )
        )
    if grupo.decisao_completude is None:
        violations.append(
            Violation(
                "MANIFESTO_DECISAO_INCOMPLETA",
                f"grupo {grupo.grupo!r} está estado_grupo=ativo sem decisao_completude registrada",
            )
        )
    return violations


def validate_manifesto(
    manifesto: ManifestoSubstituicao,
    unidades: list[UnidadeAuditada],
    bundle_legado: Bundle,
) -> list[Violation]:
    """Every manifest-level (cross-unit, cross-group) structural invariant (RFC 0004 §14).

    Never checks the Fase-1A-specific "no active group in production" rule
    — that is ``check_nenhum_grupo_ativo_em_producao``, applied only to the
    real repo file so this function stays usable by fixtures/tests that
    legitimately exercise a complete, active group.
    """
    known_legacy_ids = bundle_legado.regra_ids()
    unidades_by_id = {u.doc_id: u for u in unidades}
    known_unidade_ids = frozenset(unidades_by_id)
    violations: list[Violation] = []

    grupo_ids = [g.grupo for g in manifesto.grupos]
    duplicates = sorted({gid for gid in grupo_ids if grupo_ids.count(gid) > 1})
    violations.extend(
        Violation("MANIFESTO_GRUPO_DUPLICADO", f"duplicate grupo id {dup!r}") for dup in duplicates
    )

    origem_ativo_owners: dict[str, list[str]] = {}
    destino_owners: dict[str, list[str]] = {}
    for grupo in manifesto.grupos:
        for origem in grupo.origens_legacy:
            if origem not in known_legacy_ids:
                violations.append(
                    Violation(
                        "MANIFESTO_ORIGEM_INEXISTENTE",
                        f"grupo {grupo.grupo!r} references unknown legacy rule {origem!r}",
                    )
                )
            if grupo.estado_grupo == "ativo":
                origem_ativo_owners.setdefault(origem, []).append(grupo.grupo)
        for destino in grupo.destinos_auditados:
            if destino not in known_unidade_ids:
                violations.append(
                    Violation(
                        "MANIFESTO_DESTINO_INEXISTENTE",
                        f"grupo {grupo.grupo!r} references unknown audited unit {destino!r}",
                    )
                )
            destino_owners.setdefault(destino, []).append(grupo.grupo)

        if grupo.estado_grupo == "ativo":
            violations.extend(_grupo_ativo_incompleto(grupo, unidades_by_id=unidades_by_id))
        elif grupo.decisao_completude is not None:
            violations.append(
                Violation(
                    "MANIFESTO_DECISAO_SEM_ATIVACAO",
                    f"grupo {grupo.grupo!r} está estado_grupo=inativo mas ainda carrega decisao_completude "
                    "— rollback deve limpá-la",
                )
            )

    violations.extend(
        Violation(
            "MANIFESTO_ORIGEM_GRUPOS_ATIVOS_CONFLITANTES",
            f"legacy rule {origem!r} claimed by more than one active grupo {sorted(grupos)}",
        )
        for origem, grupos in origem_ativo_owners.items()
        if len(grupos) > 1
    )
    violations.extend(
        Violation(
            "MANIFESTO_DESTINO_EM_GRUPOS_CONFLITANTES",
            f"audited unit {destino!r} claimed by more than one grupo {sorted(grupos)}",
        )
        for destino, grupos in destino_owners.items()
        if len(grupos) > 1
    )
    return violations


def check_nenhum_grupo_ativo_em_producao(manifesto: ManifestoSubstituicao) -> list[Violation]:
    """Fase 1A gate: the production manifest must never declare an active group.

    Activation isn't wired to any exporter yet (RFC 0004 §15, Fase 2) — a
    group can be structurally complete and still must not go live for real
    until that phase lands. Fixtures/tests exercise active groups directly
    against ``validate_manifesto``, never through this function.
    """
    return [
        Violation(
            "MANIFESTO_ATIVACAO_NAO_SUPORTADA",
            f"grupo {grupo.grupo!r} declara estado_grupo=ativo, mas a ativação operacional "
            "ainda não está implementada (RFC 0004, Fase 1A não ativa nenhum grupo real)",
        )
        for grupo in manifesto.grupos
        if grupo.estado_grupo == "ativo"
    ]


def selecionar_origem_operacional(
    regra_id: str, manifesto: ManifestoSubstituicao
) -> Literal["legado", "auditado"]:
    """RFC 0004 §1.5 — the exporter's single-origin invariant for one legacy regra id.

    Returns ``"auditado"`` only when ``regra_id`` is listed in
    ``origens_legacy`` of a group whose ``estado_grupo`` is ``"ativo"`` —
    never for a destino that is merely ``deployable`` in isolation (RFC
    0004: "nenhuma unidade isolada substitui uma origem"). Exactly one
    return value per call is what makes "nunca as duas ao mesmo tempo"
    (``P_EXPORT_ORIGEM_DUPLA``) structurally impossible to violate here.
    """
    for grupo in manifesto.grupos:
        if grupo.estado_grupo == "ativo" and regra_id in grupo.origens_legacy:
            return "auditado"
    return "legado"
