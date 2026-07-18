"""Pure domain library for bundle loading, detection and validation."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import TYPE_CHECKING

import yaml
from achado_schema import load_achados, validate_bundle_achados
from detections import Violation
from detectors import ALL as ALL_DETECTORS
from estado_auditoria import check_p7_estados
from okf_common import BundleIntegrityError
from okf_to_csv import validate_bundle_identity
from regra_schema import ADMIN_FIELD_DEFAULTS

if TYPE_CHECKING:
    from pathlib import Path

    from achado_schema import Achado
    from detections import Detection

_HEADING_RE = re.compile(r"^# (.+)$", re.MULTILINE)


@dataclass(frozen=True)
class Regra:
    """One authored regra with all frontmatter and level-one body sections."""

    id: str
    frontmatter: dict[str, object]
    sections: dict[str, str]

    @property
    def status_regra(self) -> str:
        """Return the rule's administrative participation status (P2.1)."""
        return str(self.frontmatter.get("status_regra") or ADMIN_FIELD_DEFAULTS["status_regra"])

    @property
    def status_auditoria(self) -> str:
        """Return the rule's audit progress state: importada/revisada/validada (P7)."""
        return str(self.frontmatter.get("status_auditoria") or ADMIN_FIELD_DEFAULTS["status_auditoria"])

    @property
    def atos_validacao(self) -> object:
        """Return the raw atos_validacao value backing a validada state (P7).

        Deliberately unfiltered/untyped — a malformed value (not a list, or
        a list with a non-mapping item) must surface as a validation error
        (see estado_auditoria.py), not silently vanish. A property that
        pre-filtered to "only the dict items" would make bad data
        undetectable: the raw frontmatter/CSV cell still has it, but
        validation would never see it.
        """
        return self.frontmatter.get("atos_validacao", [])


@dataclass(frozen=True)
class Bundle:
    """A loaded bundle, with no write behavior."""

    bundle_dir: Path
    regras: tuple[Regra, ...]
    achados: tuple[Achado, ...]

    @classmethod
    def load(cls, bundle_dir: Path) -> Bundle:
        """Load every authored rule and finding from a bundle directory."""
        regras = []
        for doc_path in sorted((bundle_dir / "regras").glob("regra-*.md")):
            frontmatter, sections = _parse_regra_doc(doc_path.read_text(encoding="utf-8"))
            regras.append(Regra(id=doc_path.stem, frontmatter=frontmatter, sections=sections))
        return cls(
            bundle_dir=bundle_dir,
            regras=tuple(regras),
            achados=tuple(load_achados(bundle_dir)),
        )

    def active_regras(self) -> list[Regra]:
        """Return rules that currently participate as active catalog entries."""
        return [regra for regra in self.regras if regra.status_regra == "ativa"]

    def regra_ids(self) -> frozenset[str]:
        """Return every stable rule id present in the bundle."""
        return frozenset(regra.id for regra in self.regras)

    def open_achados(self) -> list[Achado]:
        """Return findings whose investigations remain open."""
        return [achado for achado in self.achados if achado.situacao == "aberto"]

    def persistent_resolved_achados(self) -> list[Achado]:
        """Return resolved findings that explicitly accept persistent detections."""
        return [
            achado
            for achado in self.achados
            if achado.situacao == "resolvido" and achado.efeito_deteccao == "pode_persistir"
        ]


def _parse_regra_doc(text: str) -> tuple[dict[str, object], dict[str, str]]:
    """Parse every level-one body section, including future semantic sections."""
    _, fm_text, body = text.split("---", 2)
    frontmatter = yaml.safe_load(fm_text) or {}

    sections: dict[str, str] = {}
    matches = list(_HEADING_RE.finditer(body))
    for idx, match in enumerate(matches):
        heading = match.group(1).strip()
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(body)
        sections[heading] = body[start:end].strip("\n")
    return frontmatter, sections


def collect_detections(bundle: Bundle) -> list[Detection]:
    """Run all registered detectors and collect their mechanical occurrences."""
    detections: list[Detection] = []
    for detect in ALL_DETECTORS:
        detections.extend(detect(bundle))
    return detections


def _coverage_fingerprints(bundle: Bundle) -> set[str]:
    """Fingerprints covered by an open investigation or accepted persistence."""
    achados = [*bundle.open_achados(), *bundle.persistent_resolved_achados()]
    return {fingerprint for achado in achados for fingerprint in achado.fingerprints}


def _open_fingerprints(bundle: Bundle) -> dict[str, list[Achado]]:
    fp_to_achados: dict[str, list[Achado]] = {}
    for achado in bundle.open_achados():
        for fingerprint in achado.fingerprints:
            fp_to_achados.setdefault(fingerprint, []).append(achado)
    return fp_to_achados


def uncovered_detections(bundle: Bundle, detections: list[Detection] | None = None) -> list[Detection]:
    """Camada-2 detections lacking an open or persistence-accepting finding.

    Only detections with ``requires_achado`` are enforced — camada-3
    heuristics (P1/P9) are reported but never force an achado (RFC "semântica
    adiada": they must never block the CI).
    """
    detections = collect_detections(bundle) if detections is None else detections
    covered = _coverage_fingerprints(bundle)
    return [
        detection
        for detection in detections
        if detection.requires_achado and detection.fingerprint not in covered
    ]


def stale_detection_refs(bundle: Bundle, detections: list[Detection] | None = None) -> list[Achado]:
    """Return open investigations whose premise is no longer reproduced."""
    detections = collect_detections(bundle) if detections is None else detections
    current = {detection.fingerprint for detection in detections}
    return [
        achado
        for achado in bundle.open_achados()
        if achado.fingerprints and not set(achado.fingerprints) <= current
    ]


def unexpected_persistent_detections(
    bundle: Bundle,
    detections: list[Detection] | None = None,
) -> list[tuple[Achado, str]]:
    """Return resolved findings that required disappearance but still reproduce."""
    detections = collect_detections(bundle) if detections is None else detections
    current = {detection.fingerprint for detection in detections}
    return [
        (achado, fingerprint)
        for achado in bundle.achados
        if achado.situacao == "resolvido" and achado.efeito_deteccao == "deve_desaparecer"
        for fingerprint in achado.fingerprints
        if fingerprint in current
    ]


def mismatched_detector_refs(
    bundle: Bundle,
    detections: list[Detection] | None = None,
) -> list[tuple[Achado, str, str, str]]:
    """Return references whose detector label disagrees with the emitted fact."""
    detections = collect_detections(bundle) if detections is None else detections
    by_fingerprint = {detection.fingerprint: detection.detector for detection in detections}
    return [
        (achado, fingerprint, referenced_detector, by_fingerprint[fingerprint])
        for achado in bundle.achados
        for referenced_detector, fingerprint in achado.detection_refs
        if fingerprint in by_fingerprint and referenced_detector != by_fingerprint[fingerprint]
    ]


def _check_structural(bundle: Bundle) -> list[Violation]:
    violations: list[Violation] = []
    try:
        validate_bundle_identity(bundle.bundle_dir)
    except BundleIntegrityError as exc:
        violations.append(Violation("P_ESTRUTURA_REGRAS", str(exc)))
    violations.extend(
        Violation("P14_ACHADO_INVALIDO", error)
        for error in validate_bundle_achados(bundle.bundle_dir, known_regra_ids=bundle.regra_ids())
    )
    return violations


def _check_bidirectional(bundle: Bundle, detections: list[Detection]) -> list[Violation]:
    fp_to_open_achados = _open_fingerprints(bundle)

    sem_achado = [
        Violation(
            "P14_DETECCAO_SEM_ACHADO",
            f"{detection.detector} detected {sorted(detection.regras)} "
            f"(fingerprint {detection.fingerprint}) without an open achado "
            "or a resolved achado that allows persistence",
        )
        for detection in uncovered_detections(bundle, detections)
    ]
    sem_deteccao = [
        Violation(
            "P14_ACHADO_SEM_DETECCAO",
            f"{achado.doc_id} is open but references a detection no longer emitted",
        )
        for achado in stale_detection_refs(bundle, detections)
    ]
    persistente = [
        Violation(
            "P14_DETECCAO_DEVERIA_DESAPARECER",
            f"{achado.doc_id} was resolved with efeito_deteccao=deve_desaparecer, "
            f"but {fingerprint} is still emitted",
        )
        for achado, fingerprint in unexpected_persistent_detections(bundle, detections)
    ]
    detector_incorreto = [
        Violation(
            "P14_DETECTOR_INCOMPATIVEL",
            f"{achado.doc_id} labels {fingerprint} as {referenced}, but the detector emits {actual}",
        )
        for achado, fingerprint, referenced, actual in mismatched_detector_refs(bundle, detections)
    ]
    duplicada = [
        Violation(
            "P14_DETECCAO_DUPLICADA",
            f"detection {fingerprint} is claimed by more than one open achado "
            f"({', '.join(achado.doc_id for achado in achados)})",
        )
        for fingerprint, achados in fp_to_open_achados.items()
        if len(achados) > 1
    ]
    return [*sem_achado, *sem_deteccao, *persistente, *detector_incorreto, *duplicada]


def validate_bundle(bundle: Bundle, detections: list[Detection] | None = None) -> list[Violation]:
    """Run all blocking structural, detection-contract and audit-state checks.

    Pass ``detections`` when the caller already ran ``collect_detections`` —
    avoids re-running every detector.
    """
    detections = collect_detections(bundle) if detections is None else detections
    return [
        *_check_structural(bundle),
        *_check_bidirectional(bundle, detections),
        *check_p7_estados(bundle, detections),
    ]
