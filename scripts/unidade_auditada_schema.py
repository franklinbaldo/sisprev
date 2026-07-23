"""RFC 0004 §1-§3 — the audited unit concept: schema, parser, loader, validation.

An audited unit (``type: UnidadeAuditada``) lives in a bundle separate from
the legacy catalog (``okf/regras-auditadas/``, see ``okf_common.DEFAULT_BUNDLE_AUDITADO``)
with its own identity space — its ``id`` is never a ``regra-NNNN`` and never
reuses ``row_index`` (RFC 0004 §1.2). Every unit declares ``origens_legacy``,
the legacy regra(s) it descends from — proveniência 1:N and N:1 are both
legitimate (RFC 0004 §1.2), but each unit still compiles to *exactly one*
projected row (§1.6).

Frontmatter *shape* is validated the same way every other concept doc in
this repo is: ``Concept``/``ConceptFrontmatter`` only require the right
Python types; ``UnidadeAuditadaFrontmatter`` is the on-demand semantic
contract (same ``_validation``/``contract``/``validation_error`` pattern as
``Regra``/``Achado``/``Dispositivo``).

``predicados.causa_incapacidade`` is the one field the RFC fixes a closed
enum for (§3, Q6 direção A); every other predicate/metadata field stays a
non-empty string, exactly as far as the RFC actually commits — this module
does not decide P-1...P-6, Q1-Q12, or any legal question (RFC 0004, "não
decide").
"""

from __future__ import annotations

import datetime
import re
from functools import cached_property
from typing import TYPE_CHECKING, Literal, get_args

from concept import Concept, ConceptDocError, ConceptFrontmatter, format_pydantic_errors, parse_concept_doc
from detections import Violation
from dispositivo_schema import DISPOSITIVO_REF_RE
from estado_auditoria import NonEmptyStr
from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator
from regra_schema import COLUMNS

if TYPE_CHECKING:
    from pathlib import Path

    from bundle import Bundle

# Kebab-case (0+ hyphen-separated segments) — the RFC 0004 §1.2 "não é
# regra-NNNN" constraint is enforced separately below via LEGACY_REGRA_REF_RE,
# since that shape (letters + a single hyphenated numeric segment) already
# matches this general kebab-case pattern too.
UNIDADE_ID_RE = re.compile(r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$")
LEGACY_REGRA_REF_RE = re.compile(r"^regra-\d{4}$")

# The actual frontmatter key for each of the 27 legacy columns, in P13.2's
# canonical order — NOT `regra_schema.FRONTMATTER_COLUMNS` (a misleadingly
# named alias for the *original CSV header strings*, e.g. "FUNDAMENTACAO_INTEGRAL";
# derived fresh from COLUMNS here so it can never drift from the real
# frontmatter keys, e.g. "fundamentacao_integral").
LEGACY_FRONTMATTER_KEYS: tuple[str, ...] = tuple(column.frontmatter_key for column in COLUMNS)

# Every column except `nome` (RFC 0004 §4.2: nome is interface, never a
# portador primário alone) is a legitimate carrier for a requisito or a
# directly-authored projection value.
CARRIER_FIELDS = frozenset(LEGACY_FRONTMATTER_KEYS) - {"nome"}

# The four legacy date columns live exclusively in
# `aplicabilidade_temporal.datas_legadas` (RFC 0004 §5.1) — excluded here so
# there is never a second, conflicting place to declare them.
_DATA_FIELDS = frozenset({"data_adm_apos", "data_adm_ate", "data_direito_apos", "data_direito_ate"})
PROJECAO_FIELDS = frozenset(LEGACY_FRONTMATTER_KEYS) - _DATA_FIELDS

# The RFC's Q6-direção-A closed enum (§3) — kept as a plain tuple for
# CAUSA_INCAPACIDADE_VALUES so other modules/tests can enumerate the
# allowed values; Predicados.causa_incapacidade below re-spells the same
# four literals directly (a static type checker requires Literal's
# arguments to be written out, not unpacked from a variable).
CAUSA_INCAPACIDADE_VALUES = (
    "acidente_em_servico",
    "molestia_profissional",
    "doenca_catalogada",
    "causa_comum",
)

# Sentinel marking an operational field as explicitly pending a legal/
# institutional decision (RFC 0004 §5.1/§16.2) — distinct from an absent
# field: "pendente" says the auditor looked and found an open question,
# never a silently-skipped default.
PENDENTE = "pendente"


class UnidadeAuditadaValidationError(Exception):
    """Raised when one or more audited-unit docs violate an RFC 0004 invariant."""


class ProtocoloVerificacao(BaseModel):
    """RFC 0004 §7, part 3 — how a requisito's predicate is normally verified.

    Never the fact of a concrete case (Q6-S) — only the standing protocol
    (Q6-R): who, by what means, when, and what evidence is required.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    pergunta: NonEmptyStr
    responsavel: NonEmptyStr
    meio_de_prova: NonEmptyStr
    momento: NonEmptyStr
    evidencia_exigida: NonEmptyStr


class RequisitoVerificacaoHumana(BaseModel):
    """RFC 0004 §3/§7 — a requisito verificável por humano: predicado + protocolo + portador.

    ``portador_primario`` names the legacy column (one of the 27 minus
    `nome`) where this requisito's condition is textually carried in the
    compiled projection (RFC 0004 §4.2: "exatamente um [portador primário]
    por requisito operacional").
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    predicado: NonEmptyStr
    protocolo_verificacao: ProtocoloVerificacao
    portador_primario: str

    @field_validator("portador_primario")
    @classmethod
    def _portador_valido(cls, value: str) -> str:
        if value not in CARRIER_FIELDS:
            msg = f"portador_primario={value!r} must be one of the 27 legacy columns (excluding 'nome')"
            raise ValueError(msg)
        return value


class Predicados(BaseModel):
    """RFC 0004 §3 — the structured legal predicates (Q6-R), never a requerente fact (Q6-S)."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    causa_incapacidade: (
        Literal["acidente_em_servico", "molestia_profissional", "doenca_catalogada", "causa_comum"] | None
    ) = None
    regime: NonEmptyStr | None = None
    marco_ingresso: NonEmptyStr | None = None
    sexo: NonEmptyStr | None = None


_CAUSA_ANNOTATION = Predicados.model_fields["causa_incapacidade"].annotation
_CAUSA_LITERAL_VALUES = {
    value for arg in get_args(_CAUSA_ANNOTATION) for value in get_args(arg) if arg is not type(None)
}
if set(CAUSA_INCAPACIDADE_VALUES) != _CAUSA_LITERAL_VALUES:
    msg = "CAUSA_INCAPACIDADE_VALUES has drifted from Predicados.causa_incapacidade's Literal"
    raise ValueError(msg)


class DatasLegadas(BaseModel):
    """RFC 0004 §5.1 — the four legacy date columns, verified structurally, not generated.

    Each is either a legacy-format date string, the ``PENDENTE`` sentinel
    (Q1/Q2 open — the compiler defers, it never guesses), or absent
    (not operationally relevant to this unit's predicados).
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    data_adm_apos: str | None = None
    data_adm_ate: str | None = None
    data_direito_apos: str | None = None
    data_direito_ate: str | None = None


class AplicabilidadeTemporal(BaseModel):
    """RFC 0004 §2/§5.1/§16.2 — temporal applicability, operational (never metadata)."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    datas_legadas: DatasLegadas = Field(default_factory=DatasLegadas)
    versao_rol: str | None = None


class TaxonomiaRef(BaseModel):
    """RFC 0004 §3 — a link to `okf/dispositivos/`, projecting to `dispositivos:` (P3)."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    ref: str
    papel: NonEmptyStr

    @field_validator("ref")
    @classmethod
    def _ref_bem_formado(cls, value: str) -> str:
        if DISPOSITIVO_REF_RE.fullmatch(value) is None:
            msg = f"ref={value!r} is not a well-formed /dispositivos/.../<artigo>.md reference"
            raise ValueError(msg)
        return value


class Proveniencia(BaseModel):
    """RFC 0004 §2 — audit metadata; never projects to the legacy target (only in A)."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    fontes_consultadas: list[NonEmptyStr] = Field(default_factory=list)
    notas: str | None = None


class DecisaoAuditoria(BaseModel):
    """RFC 0004 §3 — one recorded audit decision; metadata only, never projects."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    data: datetime.date
    quem: NonEmptyStr
    o_que: NonEmptyStr

    @field_validator("data", mode="before")
    @classmethod
    def _parse_iso_date(cls, value: object) -> object:
        if value is None or isinstance(value, datetime.date):
            return value
        if isinstance(value, str):
            return datetime.date.fromisoformat(value)
        return value


class UnidadeAuditadaFrontmatter(ConceptFrontmatter):
    """Typed frontmatter contract for ``type: UnidadeAuditada`` (RFC 0004 §3)."""

    type: Literal["UnidadeAuditada"]
    schema_version: Literal[1]
    estado_unidade: Literal["elaboracao", "preview", "deployable"]
    origens_legacy: list[str] = Field(min_length=1)
    predicados: Predicados = Field(default_factory=Predicados)
    requisitos_verificacao_humana: list[RequisitoVerificacaoHumana] = Field(default_factory=list)
    aplicabilidade_temporal: AplicabilidadeTemporal = Field(default_factory=AplicabilidadeTemporal)
    taxonomias: list[TaxonomiaRef] = Field(default_factory=list)
    # The directly-authored subset of the 27 legacy columns this unit
    # already has content for (RFC 0004 §4/§6) — nome, efeitos derivados
    # (integral/tipo_calculo/paridade), and any fundamentacao* not covered
    # by a requisito's generated text. A missing key is an operational
    # pendency, not silently defaulted (RFC 0004 §5.3).
    projecao: dict[str, str] = Field(default_factory=dict)
    proveniencia: Proveniencia | None = None
    decisoes: list[DecisaoAuditoria] = Field(default_factory=list)
    confianca: Literal["alta", "media", "baixa"] | None = None

    @field_validator("origens_legacy")
    @classmethod
    def _origens_bem_formadas(cls, value: list[str]) -> list[str]:
        for ref in value:
            if LEGACY_REGRA_REF_RE.fullmatch(ref) is None:
                msg = f"origens_legacy entry {ref!r} is not of the form regra-NNNN"
                raise ValueError(msg)
        if len(value) != len(set(value)):
            msg = "origens_legacy must not contain duplicates"
            raise ValueError(msg)
        return value

    @field_validator("projecao")
    @classmethod
    def _projecao_chaves_conhecidas(cls, value: dict[str, str]) -> dict[str, str]:
        unknown = sorted(set(value) - PROJECAO_FIELDS)
        if unknown:
            msg = f"projecao has unknown column key(s) {unknown!r} — must be one of the 27 legacy columns"
            raise ValueError(msg)
        return value


class UnidadeAuditada(Concept):
    """One authored audited unit — an OKF concept doc (RFC 0004).

    Same fallback pattern as ``Regra``/``Achado``: typed accessors prefer
    the cached, validated ``contract``, but fall back to an ungated raw-dict
    read so a doc invalid on one field doesn't blind a cross-document join
    on another well-formed field.
    """

    @cached_property
    def _validation(self) -> UnidadeAuditadaFrontmatter | ValidationError:
        try:
            return UnidadeAuditadaFrontmatter.model_validate(self.frontmatter)
        except ValidationError as exc:
            return exc

    @property
    def contract(self) -> UnidadeAuditadaFrontmatter | None:
        """Return the validated RFC 0004 frontmatter contract, or None if malformed."""
        result = self._validation
        return result if isinstance(result, UnidadeAuditadaFrontmatter) else None

    @property
    def validation_error(self) -> ValidationError | None:
        """Return the cached contract ValidationError, or None if the doc is valid."""
        result = self._validation
        return result if isinstance(result, ValidationError) else None

    @property
    def estado_unidade(self) -> str:
        """Return the unit's lifecycle state, or an empty string if malformed."""
        if self.contract is not None:
            return self.contract.estado_unidade
        return str(self.frontmatter.get("estado_unidade") or "")

    @property
    def origens_legacy(self) -> list[str]:
        """Return the unit's declared legacy provenance, as declared — not existence-checked."""
        if self.contract is not None:
            return self.contract.origens_legacy
        raw = self.frontmatter.get("origens_legacy")
        return [str(ref) for ref in raw] if isinstance(raw, list) else []


def load_unidades_auditadas(bundle_dir: Path) -> list[UnidadeAuditada]:
    """Load every authored audited-unit document, in filename order.

    Returns an empty list if ``unidades/`` doesn't exist yet — the loader
    must accept an empty audited bundle (RFC 0004 §1.2).
    """
    unidades_dir = bundle_dir / "unidades"
    if not unidades_dir.is_dir():
        return []
    unidades = []
    for doc_path in sorted(unidades_dir.glob("*.md")):
        if doc_path.stem == "index":
            continue
        try:
            frontmatter, body = parse_concept_doc(doc_path.read_text(encoding="utf-8"))
        except ConceptDocError as exc:
            msg = "audited-unit document must contain YAML frontmatter delimited by ---"
            raise UnidadeAuditadaValidationError(msg) from exc
        unidades.append(
            UnidadeAuditada(doc_id=doc_path.stem, frontmatter=frontmatter, body=body, bundle_dir=bundle_dir)
        )
    return unidades


def _validate_identity(unidade: UnidadeAuditada, *, known_legacy_ids: frozenset[str]) -> list[Violation]:
    doc_id = unidade.doc_id
    violations: list[Violation] = []

    if UNIDADE_ID_RE.fullmatch(doc_id) is None or LEGACY_REGRA_REF_RE.fullmatch(doc_id) is not None:
        violations.append(
            Violation(
                "AUDITADA_ID_INVALIDO", f"{doc_id}: id must be kebab-case and must not be a regra-NNNN shape"
            )
        )
    if unidade.frontmatter.get("id") != doc_id:
        violations.append(
            Violation(
                "AUDITADA_ID_INVALIDO",
                f"{doc_id}: frontmatter id={unidade.frontmatter.get('id')!r} does not match filename",
            )
        )

    violations.extend(
        Violation(
            "AUDITADA_ORIGEM_INEXISTENTE", f"{doc_id}: origens_legacy references unknown legacy rule {ref!r}"
        )
        for ref in unidade.origens_legacy
        if ref not in known_legacy_ids
    )
    return violations


def validate_unidade(unidade: UnidadeAuditada, *, known_legacy_ids: frozenset[str]) -> list[Violation]:
    """Return every intra-document and provenance violation for one audited unit."""
    violations: list[Violation] = []
    if unidade.validation_error is not None:
        violations.extend(
            Violation("AUDITADA_FRONTMATTER_INVALIDA", error)
            for error in format_pydantic_errors(unidade.doc_id, unidade.validation_error)
        )
    violations.extend(_validate_identity(unidade, known_legacy_ids=known_legacy_ids))
    return violations


def validate_bundle_auditado(unidades: list[UnidadeAuditada], bundle_legado: Bundle) -> list[Violation]:
    """Camada 1 [bloqueante] — every audited unit satisfies its own structural invariants.

    Never checks manifest-level (cross-unit group) invariants — see
    ``manifesto_substituicao.validate_manifesto`` for those.
    """
    known_legacy_ids = bundle_legado.regra_ids()
    violations: list[Violation] = []

    ids = [u.doc_id for u in unidades]
    duplicates = sorted({doc_id for doc_id in ids if ids.count(doc_id) > 1})
    violations.extend(
        Violation("AUDITADA_ID_DUPLICADO", f"duplicate audited unit id {dup!r}") for dup in duplicates
    )

    for unidade in unidades:
        violations.extend(validate_unidade(unidade, known_legacy_ids=known_legacy_ids))
    return violations
