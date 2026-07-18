"""Pure domain library for bundle loading, detection and validation."""

from __future__ import annotations

from functools import cached_property
from pathlib import Path
from typing import TYPE_CHECKING

from achado_schema import Achado, load_achados, validate_bundle_achados
from concept import UNSET_BUNDLE_DIR, Concept, parse_concept_doc
from detections import Violation
from detectors import ALL as ALL_DETECTORS
from dispositivo_schema import DISPOSITIVO_REF_RE, load_dispositivos, validate_dispositivo
from estado_auditoria import check_p7_estados
from okf_common import BundleIntegrityError, default_dispositivos_dir
from okf_to_csv import validate_bundle_identity
from pydantic import BaseModel, ConfigDict, ValidationError
from regra_schema import ADMIN_FIELD_DEFAULTS, DISPOSITIVOS_KEY, RegraAdminContrato

if TYPE_CHECKING:
    from detections import Detection
    from dispositivo_schema import Dispositivo


class Regra(Concept):
    """One authored regra — an OKF concept doc (P2.1/P3).

    ``status_regra``/``dispositivos`` prefer the validated ``admin``
    contract (P2.1/P3, a slice of the frontmatter — the rest stays a loose
    dict since P2's material-equality detector treats every current and
    future *domain* field/section as material by default, RFC 0001 P2 v2;
    a strict whole-document schema there would contradict that
    extensibility). Each property falls back to an ungated raw-dict read
    when the *other* field in this slice is what's malformed — e.g. a bad
    ``dispositivos`` value must not also hide a perfectly well-formed
    ``status_regra`` from ``active_regras()``.
    """

    @cached_property
    def _validation(self) -> RegraAdminContrato | ValidationError:
        try:
            return RegraAdminContrato.model_validate(self.frontmatter)
        except ValidationError as exc:
            return exc

    @property
    def admin(self) -> RegraAdminContrato | None:
        """Return the validated P2.1/P3 administrative contract, or None if malformed."""
        result = self._validation
        return result if isinstance(result, RegraAdminContrato) else None

    @property
    def status_regra(self) -> str:
        """Return the rule's administrative participation status (P2.1)."""
        if self.admin is not None:
            return self.admin.status_regra
        return str(self.frontmatter.get("status_regra") or ADMIN_FIELD_DEFAULTS["status_regra"])

    @property
    def dispositivos(self) -> list[str]:
        """Return the rule's linked legal provisions (P3), as declared — not validated."""
        if self.admin is not None:
            return self.admin.dispositivos
        raw = self.frontmatter.get(DISPOSITIVOS_KEY)
        return [str(ref) for ref in raw] if isinstance(raw, list) else []


class Bundle(BaseModel):
    """A loaded bundle, with no write behavior."""

    model_config = ConfigDict(frozen=True)

    # bundle_dir/dispositivos_dir default to UNSET_BUNDLE_DIR (never a real
    # directory) and regras/achados to () only for tests building a
    # synthetic Bundle in memory — every real loader (Bundle.load()) always
    # passes every field explicitly. Path() (cwd) would be a real directory
    # and silently pass every loader's `.is_dir()` guard, walking the whole
    # repo instead of no-op'ing (see dispositivo_schema.load_dispositivos).
    bundle_dir: Path = UNSET_BUNDLE_DIR
    regras: tuple[Regra, ...] = ()
    achados: tuple[Achado, ...] = ()
    dispositivos_dir: Path = UNSET_BUNDLE_DIR

    @classmethod
    def load(cls, bundle_dir: Path, *, dispositivos_dir: Path | None = None) -> Bundle:
        """Load every authored rule and finding from a bundle directory.

        ``dispositivos_dir`` defaults to the conventional sibling
        ``okf/dispositivos/`` (P3) — pass it explicitly only in tests that
        use a bundle_dir with no such sibling.
        """
        regras = []
        for doc_path in sorted((bundle_dir / "regras").glob("regra-*.md")):
            frontmatter, body = parse_concept_doc(doc_path.read_text(encoding="utf-8"))
            regras.append(
                Regra(doc_id=doc_path.stem, frontmatter=frontmatter, body=body, bundle_dir=bundle_dir)
            )
        if dispositivos_dir is None:
            dispositivos_dir = default_dispositivos_dir(bundle_dir)
        return cls(
            bundle_dir=bundle_dir,
            regras=tuple(regras),
            achados=tuple(load_achados(bundle_dir)),
            dispositivos_dir=dispositivos_dir,
        )

    def active_regras(self) -> list[Regra]:
        """Return rules that currently participate as active catalog entries."""
        return [regra for regra in self.regras if regra.status_regra == "ativa"]

    def regra_ids(self) -> frozenset[str]:
        """Return every stable rule id present in the bundle."""
        return frozenset(regra.doc_id for regra in self.regras)

    def dispositivo_ids(self) -> frozenset[str]:
        """Return every authored dispositivo's doc_id (P3), for link resolution."""
        return frozenset(d.doc_id for d in load_dispositivos(self.dispositivos_dir))

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


def check_p3_dispositivos(bundle: Bundle, dispositivos: list[Dispositivo] | None = None) -> list[Violation]:
    """P3 — every declared ``dispositivos:`` reference resolves to an authored dispositivo.

    Only structural resolution is checked here; whether a regra *should*
    have ``dispositivos:`` populated is not enforced yet — that's P7's
    fifth P13.1 question, deferred until this bundle has enough content to
    make the requirement meaningful (see estado_auditoria.py).

    Pass ``dispositivos`` when the caller already loaded the P3 bundle
    (``validate_bundle`` does) — avoids re-reading and re-parsing every
    dispositivo doc from disk a second time.
    """
    if dispositivos is None:
        dispositivos = load_dispositivos(bundle.dispositivos_dir)
    known_ids = frozenset(d.doc_id for d in dispositivos)
    violations: list[Violation] = []
    for regra in bundle.regras:
        for ref in regra.dispositivos:
            if DISPOSITIVO_REF_RE.fullmatch(ref) is None:
                violations.append(
                    Violation(
                        "P3_DISPOSITIVO_INVALIDO",
                        f"{regra.doc_id}: non-canonical dispositivo reference {ref!r}",
                    )
                )
                continue
            doc_id = ref.removeprefix("/dispositivos/").removesuffix(".md")
            if doc_id not in known_ids:
                violations.append(
                    Violation(
                        "P3_DISPOSITIVO_INVALIDO", f"{regra.doc_id}: references unknown dispositivo {ref!r}"
                    )
                )
    return violations


def _check_structural(bundle: Bundle, dispositivos: list[Dispositivo] | None = None) -> list[Violation]:
    if dispositivos is None:
        dispositivos = load_dispositivos(bundle.dispositivos_dir)
    violations: list[Violation] = []
    try:
        validate_bundle_identity(bundle.bundle_dir)
    except BundleIntegrityError as exc:
        violations.append(Violation("P_ESTRUTURA_REGRAS", str(exc)))
    violations.extend(
        Violation("P14_ACHADO_INVALIDO", error)
        for error in validate_bundle_achados(bundle.bundle_dir, known_regra_ids=bundle.regra_ids())
    )
    violations.extend(
        Violation("P3_DISPOSITIVO_INVALIDO", error)
        for dispositivo in dispositivos
        for error in validate_dispositivo(dispositivo)
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
    avoids re-running every detector. Dispositivos (P3) are loaded from disk
    exactly once here and shared between the structural and link-resolution
    checks below, for the same reason.
    """
    detections = collect_detections(bundle) if detections is None else detections
    dispositivos = load_dispositivos(bundle.dispositivos_dir)
    return [
        *_check_structural(bundle, dispositivos),
        *_check_bidirectional(bundle, detections),
        *check_p3_dispositivos(bundle, dispositivos),
        *check_p7_estados(bundle, detections),
    ]
