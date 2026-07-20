"""P7 — máquina mínima de estados de auditoria (RFC 0001).

``status_auditoria`` is a **join** with ``achados/*`` and the detectors, not
a field whose validity can be checked in isolation — a regra ``revisada``
that starts appearing in an open bloqueante achado's ``regras_afetadas``, or
that re-enters an active P1/P2 group, becomes invalid *without anyone
touching that regra's frontmatter*. That's the point (RFC P7): the CI
re-verifies the join on every commit; nothing here auto-downgrades a regra's
declared state — a human commits the explicit rebaixamento, with the
`P7_ESTADO_INVALIDO` violation as the forcing function.

The intra-document part of the contract (is ``status_auditoria`` one of the
three closed values? does ``auditado_por``/``auditado_em`` form a real,
non-future trail? is ``atos_validacao`` a well-formed list of institutional
acts?) is a Pydantic model, ``RegraAuditoriaContrato`` — same pattern
achado_schema.py already uses for achados. It intentionally covers *only*
the P7/P11 administrative fields, never the domain fields: those stay a
loose dict on ``bundle.Regra`` because P2's material-equality detector
treats every current and future domain field/section as material by
default (RFC 0001, P2 v2) — a strict schema there would contradict that
extensibility. ``extra="ignore"`` lets the model validate just its slice of
a frontmatter dict that also has ``nome``, ``sexo``, and every other
original column mixed in.

Currently enforced invariants:

- ``status_auditoria`` is a **closed enum** (P8) — any value outside
  ``importada``/``revisada``/``validada`` (``RegraAuditoriaContrato``'s
  ``Literal`` field) is itself a violation, checked before anything else. The
  default (``importada``) applies only when the key is genuinely absent;
  Pydantic's own semantics already draw this distinction (a present-but-
  malformed value is validated, not silently defaulted) — no hand-written
  "if key not in frontmatter" check is needed.
- ``revisada``: no achado with ``situacao: aberto`` and
  ``severidade: bloqueante`` references the regra; the regra is not part of
  a currently-detected ``P2_IGUALDADE_MATERIAL_ATIVA`` group (igualdade
  material com outra ativa) nor a currently-detected ``P1_NOME_REPETIDO``
  group, over *all* regras including inactive ones (P1's "unicidade global
  como meta de revisada"); ``auditado_por`` a real non-empty string and
  ``auditado_em`` a real, non-future date (P11 — the transition must leave
  a trail, not just a state flip); the four P13.1 body sections (``Critérios
  avaliados pelo Sisprev``, ``Requisitos de verificação manual``,
  ``Documentos ou evidências necessários``, ``Resultado após a seleção``)
  each present and non-empty — the CI checks the answer *exists*, never its
  merit.
- ``validada``: every ``revisada`` invariant, plus ``atos_validacao`` a
  non-empty **list**, every item a **mapping** declaring non-empty
  ``tipo``/``autoridade``/``identificador``/``fonte`` — a malformed
  ``atos_validacao`` (wrong type, a non-mapping item, or a field that's
  merely truthy instead of real text) is itself a violation, never silently
  ignored or coerced.

Deliberately **not yet enforced** — the infrastructure they depend on
doesn't exist:

- "dispositivos: vinculados e válidos" — depends on P3 (``okf/dispositivos/``),
  not built yet (Fase 2); once it exists, the fifth P13.1 question
  ("quais dispositivos justificam cada critério e efeito") should become a
  fifth required section, the same way the other four are enforced now;
- the *merit* of the four required sections' content — the CI only checks
  they're non-empty text, never that the answer is correct or complete.
  That remains a human-judgment gate.

The RFC's Q12 (institutional flow behind ``atos_validacao`` — is SEI the
only valid ``fonte``? are PGE and Presidência one act or two?) remains
explicitly unconfirmed; this module does not resolve it and does not fix
``fonte`` to any particular authority.
"""

from __future__ import annotations

import datetime
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from detections import Violation
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StringConstraints,
    ValidationError,
    ValidationInfo,
    field_validator,
    model_validator,
)

if TYPE_CHECKING:
    from bundle import Bundle, Regra
    from detections import Detection
    from pydantic_core import ErrorDetails

_P2_DETECTOR_ID = "P2_IGUALDADE_MATERIAL_ATIVA"
_P1_DETECTOR_ID = "P1_NOME_REPETIDO"
_ESTADOS_COM_TRILHA_OBRIGATORIA = ("revisada", "validada")

# P13.1's four required body sections for revisada — flat level-1 headings
# (bundle.py's parser only understands `# Heading`, never `## Heading`).
# A fifth ("quais dispositivos justificam...") is deferred to P3 (Fase 2).
_SECOES_P13_1_OBRIGATORIAS = (
    "Critérios avaliados pelo Sisprev",
    "Requisitos de verificação manual",
    "Documentos ou evidências necessários",
    "Resultado após a seleção",
)

# strip_whitespace + min_length=1: rejects "", "   ", and non-str values
# (Pydantic doesn't coerce int/None to str) in one declarative annotation —
# exactly the "real, non-empty text" bar P7/P11 set for these fields.
NonEmptyStr = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class AtoValidacao(BaseModel):
    """One institutional act backing ``status_auditoria: validada`` (P7).

    ``fonte`` is deliberately free text, not an enum fixed to SEI — the
    RFC's Q12 (is SEI the only valid source of a validation document?)
    remains unconfirmed.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    tipo: NonEmptyStr
    autoridade: NonEmptyStr
    identificador: NonEmptyStr
    fonte: NonEmptyStr


class RegraAuditoriaContrato(BaseModel):
    """The P7/P11 slice of a regra's frontmatter, validated on demand — never stored.

    Pass ``today`` via ``model_validate(..., context={"today": ...})`` for
    the non-future ``auditado_em`` check; omit it (or pass ``None``) to skip
    that check (used by callers that don't care, if any).
    """

    model_config = ConfigDict(extra="ignore")

    status_auditoria: Literal["importada", "revisada", "validada"] = "importada"
    auditado_por: NonEmptyStr | None = None
    auditado_em: datetime.date | None = None
    atos_validacao: list[AtoValidacao] = Field(default_factory=list)

    @field_validator("auditado_em")
    @classmethod
    def _nao_pode_ser_no_futuro(
        cls, value: datetime.date | None, info: ValidationInfo
    ) -> datetime.date | None:
        today = info.context.get("today") if info.context else None
        if value is not None and today is not None and value > today:
            msg = f"está no futuro (hoje: {today})"
            raise ValueError(msg)
        return value

    @model_validator(mode="after")
    def _trilha_p11_obrigatoria_para_revisada_e_validada(self) -> RegraAuditoriaContrato:
        if self.status_auditoria in _ESTADOS_COM_TRILHA_OBRIGATORIA:
            if self.auditado_por is None:
                msg = "auditado_por: exige string não vazia (P11)"
                raise ValueError(msg)
            if self.auditado_em is None:
                msg = "auditado_em: exige data ISO não vazia (P11)"
                raise ValueError(msg)
        return self

    @model_validator(mode="after")
    def _atos_validacao_obrigatorio_para_validada(self) -> RegraAuditoriaContrato:
        if self.status_auditoria == "validada" and not self.atos_validacao:
            msg = "atos_validacao: status_auditoria=validada exige ao menos um ato"
            raise ValueError(msg)
        return self


def _format_pydantic_errors(exc: ValidationError) -> list[str]:
    """One flat message per Pydantic error, ``campo: motivo`` — nothing hidden in a nested structure."""
    return [_format_one_error(err) for err in exc.errors()]


def _format_one_error(err: ErrorDetails) -> str:
    """Render one Pydantic error as ``campo: motivo``, echoing the bad input for structural errors.

    Custom ``raise ValueError(...)`` from our own validators (``type ==
    "value_error"``) already spell out the field name and reason in their
    message — echoing the whole model dict alongside would be redundant.
    Pydantic's own structural rejections (wrong type, bad enum, unparseable
    date) don't, so those get the actual received value appended.
    """
    loc = ".".join(str(part) for part in err["loc"])
    prefix = f"{loc}: " if loc else ""
    if err["type"] == "value_error":
        return f"{prefix}{err['msg']}"
    return f"{prefix}{err['msg']} (recebido: {err['input']!r})"


def _open_bloqueante_regra_ids(bundle: Bundle) -> frozenset[str]:
    """Regra ids referenced by an open, bloqueante achado."""
    return frozenset(
        regra_id
        for achado in bundle.open_achados()
        if achado.frontmatter.get("severidade") == "bloqueante"
        for regra_id in (ref.rsplit("/", 1)[-1].removesuffix(".md") for ref in achado.regras_afetadas)
    )


def _detected_regra_ids(detections: list[Detection], detector_id: str) -> frozenset[str]:
    """Every regra id currently part of any detection from ``detector_id``."""
    ids: set[str] = set()
    for detection in detections:
        if detection.detector == detector_id:
            ids.update(detection.regras)
    return frozenset(ids)


def _secoes_p13_1_errors(regra: Regra) -> list[str]:
    """P13.1: revisada requires the four boundary-of-automation sections, non-empty.

    Structural only — this checks the section *exists and has text*, never
    that the text correctly answers the question. Merit stays a human
    judgment (see this module's docstring). Body sections aren't part of
    the frontmatter Pydantic validates, so this stays a plain check.
    """
    return [
        f'"{heading}": exige seção não vazia (P13.1)'
        for heading in _SECOES_P13_1_OBRIGATORIAS
        if not regra.sections.get(heading, "").strip()
    ]


@dataclass(frozen=True)
class _JoinContext:
    """The bundle-wide facts an individual regra's estado is joined against.

    Computed once per check_p7_estados call, not per regra — these are the
    checks that genuinely can't be expressed as single-document Pydantic
    validation, since they depend on the rest of the bundle (achados,
    detections across every regra).
    """

    bloqueante_ids: frozenset[str]
    p2_ids: frozenset[str]
    p1_ids: frozenset[str]


def _join_reasons(regra: Regra, context: _JoinContext) -> list[str]:
    """Cross-document invariant violations — never expressible as intra-document validation."""
    reasons: list[str] = []
    if regra.doc_id in context.bloqueante_ids:
        reasons.append("participa de regras_afetadas de um achado bloqueante aberto")
    if regra.doc_id in context.p2_ids:
        reasons.append(f"participa de uma detecção {_P2_DETECTOR_ID} ativa")
    if regra.doc_id in context.p1_ids:
        reasons.append(f"participa de uma detecção {_P1_DETECTOR_ID} ativa")
    return reasons


def check_p7_estados(
    bundle: Bundle,
    detections: list[Detection],
    *,
    today: datetime.date | None = None,
) -> list[Violation]:
    """Camada 1 [bloqueante]: every regra satisfies the invariants of its declared state.

    Pass ``today`` explicitly for deterministic tests; defaults to the real
    current date for normal (CLI) use.
    """
    if today is None:
        today = datetime.datetime.now(tz=datetime.UTC).date()
    context = _JoinContext(
        bloqueante_ids=_open_bloqueante_regra_ids(bundle),
        p2_ids=_detected_regra_ids(detections, _P2_DETECTOR_ID),
        p1_ids=_detected_regra_ids(detections, _P1_DETECTOR_ID),
    )

    violations: list[Violation] = []
    for regra in bundle.regras:
        try:
            contrato = RegraAuditoriaContrato.model_validate(regra.frontmatter, context={"today": today})
        except ValidationError as exc:
            violations.append(
                Violation("P7_ESTADO_INVALIDO", f"{regra.doc_id}: {'; '.join(_format_pydantic_errors(exc))}"),
            )
            continue

        if contrato.status_auditoria == "importada":
            continue

        reasons = _join_reasons(regra, context)
        if contrato.status_auditoria in _ESTADOS_COM_TRILHA_OBRIGATORIA:
            reasons.extend(_secoes_p13_1_errors(regra))

        if reasons:
            violations.append(
                Violation(
                    "P7_ESTADO_INVALIDO",
                    f"{regra.doc_id} declara status_auditoria={contrato.status_auditoria!r} mas: "
                    f"{'; '.join(reasons)}",
                ),
            )

    return violations
