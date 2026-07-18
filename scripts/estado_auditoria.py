"""P7 — máquina mínima de estados de auditoria (RFC 0001).

``status_auditoria`` is a **join** with ``achados/*`` and the detectors, not
a field whose validity can be checked in isolation — a regra ``revisada``
that starts appearing in an open bloqueante achado's ``regras_afetadas``, or
that re-enters an active P1/P2 group, becomes invalid *without anyone
touching that regra's frontmatter*. That's the point (RFC P7): the CI
re-verifies the join on every commit; nothing here auto-downgrades a regra's
declared state — a human commits the explicit rebaixamento, with the
`P7_ESTADO_INVALIDO` violation as the forcing function.

Currently enforced invariants:

- ``status_auditoria`` is a **closed enum** (P8) — any value outside
  ``ESTADOS`` is itself a violation, checked before anything else.
- ``revisada``: no achado with ``situacao: aberto`` and
  ``severidade: bloqueante`` references the regra; the regra is not part of
  a currently-detected ``P2_IGUALDADE_MATERIAL_ATIVA`` group (igualdade
  material com outra ativa) nor a currently-detected ``P1_NOME_REPETIDO``
  group (P1's "unicidade como meta de revisada"); ``auditado_por`` non-empty
  and ``auditado_em`` a real, non-future ISO date (P11 — the transition
  must leave a trail, not just a state flip).
  and ``auditado_em`` a real, non-future ISO date (P11 — the transition
  must leave a trail, not just a state flip); the four P13.1 body sections
  (``Critérios avaliados pelo Sisprev``, ``Requisitos de verificação
  manual``, ``Documentos ou evidências necessários``, ``Resultado após a
  seleção``) each present and non-empty — the CI checks the answer
  *exists*, never its merit.
- ``validada``: every ``revisada`` invariant, plus ``atos_validacao`` a
  non-empty **list**, every item a **mapping** declaring ``tipo``,
  ``autoridade``, ``identificador`` and ``fonte`` — a malformed
  ``atos_validacao`` (wrong type, or an item that isn't a mapping) is
  itself a violation, never silently ignored.

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
from typing import TYPE_CHECKING, TypeGuard

from detections import Violation

if TYPE_CHECKING:
    from bundle import Bundle, Regra
    from detections import Detection

ESTADOS = ("importada", "revisada", "validada")

_P2_DETECTOR_ID = "P2_IGUALDADE_MATERIAL_ATIVA"
_P1_DETECTOR_ID = "P1_NOME_REPETIDO"
_ATOS_VALIDACAO_REQUIRED_KEYS = ("tipo", "autoridade", "identificador", "fonte")
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


def _is_nonempty_str(value: object) -> TypeGuard[str]:
    """True iff value is a str with non-whitespace content — never a merely-truthy object."""
    return isinstance(value, str) and bool(value.strip())


def _atos_validacao_errors(regra: Regra) -> list[str]:
    """Structural + required-field problems in atos_validacao. Nothing is silently dropped.

    ``Regra.atos_validacao`` returns the raw frontmatter value, unfiltered —
    a non-list value, or a list containing a non-mapping item, must surface
    here as a violation rather than vanish from validation the way a
    type-filtering property would silently make it disappear. Each required
    field must be a non-empty string (P7 defines them as textual) — a
    truthy non-string (e.g. an int or a nested mapping) is rejected too.
    """
    raw = regra.atos_validacao
    if not isinstance(raw, list):
        return [f"atos_validacao deve ser uma lista, recebeu {type(raw).__name__}"]

    errors = []
    for index, item in enumerate(raw):
        if not isinstance(item, dict):
            errors.append(f"atos_validacao[{index}] não é um mapeamento: {item!r}")
            continue
        invalid = [key for key in _ATOS_VALIDACAO_REQUIRED_KEYS if not _is_nonempty_str(item.get(key))]
        if invalid:
            errors.append(f"atos_validacao[{index}] exige string não vazia em {invalid}")
    return errors


def _secoes_p13_1_errors(regra: Regra) -> list[str]:
    """P13.1: revisada requires the four boundary-of-automation sections, non-empty.

    Structural only — this checks the section *exists and has text*, never
    that the text correctly answers the question. Merit stays a human
    judgment (see estado_auditoria's module docstring).
    """
    return [
        f'exige a seção "{heading}" não vazia (P13.1)'
        for heading in _SECOES_P13_1_OBRIGATORIAS
        if not regra.sections.get(heading, "").strip()
    ]


def _trilha_p11_errors(regra: Regra, *, today: datetime.date) -> list[str]:
    """P11: revisada/validada must declare who and when, with a real, non-future date.

    ``auditado_por`` must be a non-empty string (not merely truthy — an int
    or a mapping doesn't count). ``auditado_em`` accepts either a proper ISO
    date string or a ``datetime.date`` (YAML parses an unquoted date into
    one, same as achado_schema.py's frontmatter dates) — any other type, or
    an unparseable string, is rejected explicitly rather than coerced.
    """
    errors = []
    if not _is_nonempty_str(regra.frontmatter.get("auditado_por")):
        errors.append("exige auditado_por (string não vazia) (P11)")

    auditado_em = regra.frontmatter.get("auditado_em")
    parsed: datetime.date | None = None
    if isinstance(auditado_em, datetime.date):
        parsed = auditado_em
    elif _is_nonempty_str(auditado_em):
        try:
            parsed = datetime.date.fromisoformat(auditado_em.strip())
        except ValueError:
            errors.append(f"auditado_em={auditado_em!r} não é uma data ISO válida (P11)")
    else:
        errors.append("exige auditado_em (data ISO não vazia) (P11)")

    if parsed is not None and parsed > today:
        errors.append(f"auditado_em={auditado_em!r} está no futuro (P11)")
    return errors


@dataclass(frozen=True)
class _JoinContext:
    """The bundle-wide facts an individual regra's estado is joined against.

    Bundled to keep _estado_reasons's signature small (ruff PLR0913) —
    computed once per check_p7_estados call, not per regra.
    """

    bloqueante_ids: frozenset[str]
    p2_ids: frozenset[str]
    p1_ids: frozenset[str]
    today: datetime.date


def _estado_reasons(regra: Regra, estado: object, context: _JoinContext) -> list[str]:
    """Every invariant violation for a regra already known to declare a valid, non-importada estado."""
    reasons: list[str] = []
    if regra.id in context.bloqueante_ids:
        reasons.append("participa de regras_afetadas de um achado bloqueante aberto")
    if regra.id in context.p2_ids:
        reasons.append(f"participa de uma detecção {_P2_DETECTOR_ID} ativa")
    if regra.id in context.p1_ids:
        reasons.append(f"participa de uma detecção {_P1_DETECTOR_ID} ativa")

    if estado in _ESTADOS_COM_TRILHA_OBRIGATORIA:
        reasons.extend(_trilha_p11_errors(regra, today=context.today))
        reasons.extend(_secoes_p13_1_errors(regra))

    if estado == "validada":
        raw_atos = regra.atos_validacao
        if not isinstance(raw_atos, list) or not raw_atos:
            reasons.append("status_auditoria=validada exige atos_validacao não vazio")
        reasons.extend(_atos_validacao_errors(regra))

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
        today=today,
    )

    violations: list[Violation] = []
    for regra in bundle.regras:
        estado = regra.status_auditoria
        if estado not in ESTADOS:
            violations.append(
                Violation(
                    "P7_ESTADO_INVALIDO",
                    f"{regra.id}: status_auditoria={estado!r} não está no vocabulário fechado {ESTADOS} (P8)",
                ),
            )
            continue
        if estado == "importada":
            continue

        reasons = _estado_reasons(regra, estado, context)
        if reasons:
            violations.append(
                Violation(
                    "P7_ESTADO_INVALIDO",
                    f"{regra.id} declara status_auditoria={estado!r} mas: {'; '.join(reasons)}",
                ),
            )

    return violations
