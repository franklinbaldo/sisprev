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

- ``revisada``: no achado with ``situacao: aberto`` and
  ``severidade: bloqueante`` references the regra; the regra is not part of
  a currently-detected ``P2_IGUALDADE_MATERIAL_ATIVA`` group (igualdade
  material com outra ativa) nor a currently-detected ``P1_NOME_REPETIDO``
  group (P1's "unicidade como meta de revisada").
- ``validada``: every ``revisada`` invariant, plus ``atos_validacao``
  non-empty, each entry declaring ``tipo``, ``autoridade``,
  ``identificador`` and ``fonte``.

Deliberately **not yet enforced** — the infrastructure they depend on
doesn't exist:

- "dispositivos: vinculados e válidos" — depends on P3 (``okf/dispositivos/``),
  not built yet (Fase 2);
- the five P13.1 questions being answerable — a human-judgment gate, not a
  machine-checkable fact.

The RFC's Q12 (institutional flow behind ``atos_validacao`` — is SEI the
only valid ``fonte``? are PGE and Presidência one act or two?) remains
explicitly unconfirmed; this module does not resolve it and does not fix
``fonte`` to any particular authority.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from detections import Violation

if TYPE_CHECKING:
    from bundle import Bundle, Regra
    from detections import Detection

ESTADOS = ("importada", "revisada", "validada")

_P2_DETECTOR_ID = "P2_IGUALDADE_MATERIAL_ATIVA"
_P1_DETECTOR_ID = "P1_NOME_REPETIDO"
_ATOS_VALIDACAO_REQUIRED_KEYS = ("tipo", "autoridade", "identificador", "fonte")


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


def _atos_validacao_errors(regra: Regra) -> list[str]:
    """Missing-field problems in each declared ato de validação."""
    errors = []
    for index, ato in enumerate(regra.atos_validacao):
        missing = [key for key in _ATOS_VALIDACAO_REQUIRED_KEYS if not ato.get(key)]
        if missing:
            errors.append(f"atos_validacao[{index}] missing {missing}")
    return errors


def check_p7_estados(bundle: Bundle, detections: list[Detection]) -> list[Violation]:
    """Camada 1 [bloqueante]: every regra satisfies the invariants of its declared state."""
    bloqueante_ids = _open_bloqueante_regra_ids(bundle)
    p2_ids = _detected_regra_ids(detections, _P2_DETECTOR_ID)
    p1_ids = _detected_regra_ids(detections, _P1_DETECTOR_ID)

    violations: list[Violation] = []
    for regra in bundle.regras:
        estado = regra.status_auditoria
        if estado == "importada":
            continue

        reasons: list[str] = []
        if regra.id in bloqueante_ids:
            reasons.append("participa de regras_afetadas de um achado bloqueante aberto")
        if regra.id in p2_ids:
            reasons.append(f"participa de uma detecção {_P2_DETECTOR_ID} ativa")
        if regra.id in p1_ids:
            reasons.append(f"participa de uma detecção {_P1_DETECTOR_ID} ativa")

        if estado == "validada":
            if not regra.atos_validacao:
                reasons.append("status_auditoria=validada exige atos_validacao não vazio")
            reasons.extend(_atos_validacao_errors(regra))

        if reasons:
            violations.append(
                Violation(
                    "P7_ESTADO_INVALIDO",
                    f"{regra.id} declara status_auditoria={estado!r} mas: {'; '.join(reasons)}",
                ),
            )

    return violations
