"""P14 — Achado concept schema, doc I/O, and validation (RFC 0001).

Achados are their own OKF concept (``type: Achado``) in
``okf/regras-sisprev/achados/`` — never sections embedded in a
``regra-*.md``. ``regras_afetadas`` in the achado is the only source of the
achado <-> regra relationship (no ``achados:`` field on regras).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

import yaml

if TYPE_CHECKING:
    from pathlib import Path

DOC_NAME_RE = re.compile(r"^achado-(\d+)$")
HEADING_RE = re.compile(r"^# (.+)$", re.MULTILINE)

SITUACAO_VALUES = ("aberto", "resolvido")
SEVERIDADE_VALUES = ("bloqueante", "informativo")
VERIFICACAO_VALUES = ("mecanica", "manual", "hibrida")

# Starting vocabulary (P8) — explicitly not closed/final. Extend by PR as
# real cases are examined; this is a hypothesis, not a normative list.
NATUREZA_VALUES = ("juridica", "dados", "modelagem", "processo")

BODY_HEADINGS = ("Descrição", "Evidências", "Questão a investigar", "Resolução")


class AchadoValidationError(Exception):
    """Raised when one or more achado docs violate a P14.6 invariant."""


@dataclass
class Achado:
    """One achado, parsed from its `.md` doc."""

    doc_id: str  # filename stem, e.g. "achado-0001"
    frontmatter: dict
    sections: dict[str, str] = field(default_factory=dict)

    @property
    def regras_afetadas(self) -> list[str]:
        """The regra references this achado affects — the only source of the relation (P14.1)."""
        return list(self.frontmatter.get("regras_afetadas") or [])


def parse_achado_doc(text: str) -> tuple[dict, dict[str, str]]:
    """Split an achado doc into its frontmatter dict and named body sections."""
    _, fm_text, body = text.split("---", 2)
    frontmatter = yaml.safe_load(fm_text)

    sections: dict[str, str] = {}
    matches = list(HEADING_RE.finditer(body))
    for idx, match in enumerate(matches):
        heading = match.group(1).strip()
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(body)
        sections[heading] = body[start:end].strip("\n")
    return frontmatter, sections


def build_achado_doc(frontmatter: dict, sections: dict[str, str]) -> str:
    """Render an achado's frontmatter + body sections into `.md` text."""
    fm_text = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False)
    body_parts = [f"# {heading}\n\n{sections.get(heading, '')}\n" for heading in BODY_HEADINGS]
    return f"---\n{fm_text}---\n\n" + "\n".join(body_parts)


def load_achados(bundle_dir: Path) -> list[Achado]:
    """Load every achado-*.md in bundle_dir/achados/, sorted by doc id."""
    achados_dir = bundle_dir / "achados"
    if not achados_dir.is_dir():
        return []
    achados = []
    for doc_path in sorted(achados_dir.glob("achado-*.md")):
        frontmatter, sections = parse_achado_doc(doc_path.read_text(encoding="utf-8"))
        achados.append(Achado(doc_id=doc_path.stem, frontmatter=frontmatter, sections=sections))
    return achados


def _validate_identity_fields(achado: Achado) -> list[str]:
    doc_id = achado.doc_id
    fm = achado.frontmatter
    errors = []

    if DOC_NAME_RE.match(doc_id) is None:
        errors.append(f"{doc_id}: filename is not of the form achado-NNNN.md")
    if fm.get("type") != "Achado":
        errors.append(f"{doc_id}: type must be 'Achado', got {fm.get('type')!r}")
    if fm.get("id") != doc_id:
        errors.append(f"{doc_id}: frontmatter id={fm.get('id')!r} does not match filename")
    return errors


def _validate_enums(achado: Achado) -> list[str]:
    doc_id = achado.doc_id
    fm = achado.frontmatter
    errors = []

    situacao = fm.get("situacao")
    if situacao not in SITUACAO_VALUES:
        errors.append(f"{doc_id}: situacao={situacao!r} not in {SITUACAO_VALUES}")
    severidade = fm.get("severidade")
    if severidade not in SEVERIDADE_VALUES:
        errors.append(f"{doc_id}: severidade={severidade!r} not in {SEVERIDADE_VALUES}")
    if fm.get("verificacao") not in VERIFICACAO_VALUES:
        errors.append(f"{doc_id}: verificacao={fm.get('verificacao')!r} not in {VERIFICACAO_VALUES}")
    natureza = fm.get("natureza")
    if natureza is not None and natureza not in NATUREZA_VALUES:
        errors.append(f"{doc_id}: natureza={natureza!r} not in {NATUREZA_VALUES}")
    return errors


def _validate_detector_consistency(achado: Achado) -> list[str]:
    doc_id = achado.doc_id
    fm = achado.frontmatter
    verificacao = fm.get("verificacao")
    detector = fm.get("detector")
    errors = []

    if verificacao in ("mecanica", "hibrida") and not detector:
        errors.append(f"{doc_id}: verificacao={verificacao!r} requires 'detector'")
    if verificacao == "manual" and detector:
        errors.append(f"{doc_id}: verificacao='manual' must not have 'detector'")
    return errors


def _validate_regras_afetadas(achado: Achado, *, known_regra_ids: frozenset[str]) -> list[str]:
    doc_id = achado.doc_id
    regras_afetadas = achado.regras_afetadas
    errors = []

    if not regras_afetadas:
        errors.append(f"{doc_id}: regras_afetadas must not be empty")
    for ref in regras_afetadas:
        regra_id = ref.rsplit("/", 1)[-1].removesuffix(".md")
        if regra_id not in known_regra_ids:
            errors.append(f"{doc_id}: regras_afetadas references unknown regra {ref!r}")
    return errors


def _validate_resolution(achado: Achado) -> list[str]:
    doc_id = achado.doc_id
    fm = achado.frontmatter
    errors = []

    if fm.get("situacao") != "resolvido":
        return errors
    if not fm.get("resolvido_em"):
        errors.append(f"{doc_id}: situacao=resolvido requires resolvido_em")
    if not fm.get("resolvido_por"):
        errors.append(f"{doc_id}: situacao=resolvido requires resolvido_por")
    if not achado.sections.get("Resolução", "").strip():
        errors.append(f"{doc_id}: situacao=resolvido requires a non-empty # Resolução section")
    return errors


def validate_achado(achado: Achado, *, known_regra_ids: frozenset[str]) -> list[str]:
    """Return P14.6 violations for one achado (empty list = valid)."""
    return [
        *_validate_identity_fields(achado),
        *_validate_enums(achado),
        *_validate_detector_consistency(achado),
        *_validate_regras_afetadas(achado, known_regra_ids=known_regra_ids),
        *_validate_resolution(achado),
    ]


def validate_bundle_achados(bundle_dir: Path, *, known_regra_ids: frozenset[str]) -> list[str]:
    """Validate every achado in the bundle. Returns all violations (empty = valid).

    Also checks doc-id uniqueness/sequencing: ids must be distinct and each
    filename's number must match its own frontmatter id (renumbering or
    reusing an id is a violation — P14.3).
    """
    achados = load_achados(bundle_dir)
    errors: list[str] = []
    seen_numbers: dict[int, str] = {}

    for achado in achados:
        errors.extend(validate_achado(achado, known_regra_ids=known_regra_ids))
        match = DOC_NAME_RE.match(achado.doc_id)
        if match is None:
            continue
        number = int(match.group(1))
        if number in seen_numbers:
            errors.append(f"duplicate achado number {number}: {seen_numbers[number]} and {achado.doc_id}")
        else:
            seen_numbers[number] = achado.doc_id

    return errors


def next_achado_id(bundle_dir: Path) -> str:
    """The next unused achado-NNNN id — sequential, never reused (P14.3)."""
    achados_dir = bundle_dir / "achados"
    max_number = 0
    if achados_dir.is_dir():
        for doc_path in achados_dir.glob("achado-*.md"):
            match = DOC_NAME_RE.match(doc_path.stem)
            if match:
                max_number = max(max_number, int(match.group(1)))
    return f"achado-{max_number + 1:04d}"


def regenerate_achados_index(bundle_dir: Path) -> None:
    """Rewrite achados/index.md from the live docs — SPEC.md §6, no frontmatter.

    Backlinks are generated here, never stored inside regra-*.md (P14.6/P14.7).
    """
    achados_dir = bundle_dir / "achados"
    achados_dir.mkdir(parents=True, exist_ok=True)
    achados = load_achados(bundle_dir)

    lines = []
    for achado in achados:
        fm = achado.frontmatter
        nome = fm.get("nome", "")
        situacao = fm.get("situacao", "")
        severidade = fm.get("severidade", "")
        refs = ", ".join(r.rsplit("/", 1)[-1].removesuffix(".md") for r in achado.regras_afetadas)
        lines.append(f"* [{nome}]({achado.doc_id}.md) - {situacao}/{severidade} - {refs}")

    body = "# Achados\n\n" + ("\n".join(lines) + "\n" if lines else "")
    (achados_dir / "index.md").write_text(body, encoding="utf-8")

    regenerate_root_index(bundle_dir)


def regenerate_root_index(bundle_dir: Path) -> None:
    """Rewrite the bundle-root index.md so it lists achados/ alongside regras/ (P14.1).

    Frontmatter here is limited to okf_version (SPEC.md §11), same as
    csv_to_okf.py's original root index — this just keeps the achados/
    line current as the collection grows.
    """
    dataset_text = (bundle_dir / "regras-sisprev.md").read_text(encoding="utf-8")
    _, dataset_fm_text, _ = dataset_text.split("---", 2)
    dataset_fm = yaml.safe_load(dataset_fm_text)
    row_count = dataset_fm["row_count"]
    description = dataset_fm["description"]

    achados = load_achados(bundle_dir)
    abertos = sum(1 for a in achados if a.frontmatter.get("situacao") == "aberto")

    fm_text = yaml.safe_dump({"okf_version": "0.1"}, sort_keys=False)
    regras_line = f"{row_count} regras individuais, uma por linha da planilha original."
    body = (
        "# Regras do Sisprev\n\n"
        f"* [regras-sisprev.md](regras-sisprev.md) - {description}\n"
        f"* [regras/](regras/index.md) - {regras_line}\n"
        f"* [achados/](achados/index.md) - {len(achados)} achado(s), {abertos} aberto(s).\n"
    )
    (bundle_dir / "index.md").write_text(f"---\n{fm_text}---\n\n{body}", encoding="utf-8")
