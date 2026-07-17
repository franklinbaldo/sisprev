"""P14 — Achado concept: typed schema, doc I/O, and validation (RFC 0001).

Achados are their own OKF concept (``type: Achado``) in
``okf/regras-sisprev/achados/`` — **written and edited directly by a
person** (princípio da autoria humana). No command generates their content.

The frontmatter contract lives in the Pydantic model ``AchadoFrontmatter``:
enums, required fields and **cross-field** rules (``manual`` forbids
``deteccoes``; ``mecanica``/``hibrida`` require them) are enforced there,
and unknown keys are rejected (``extra="forbid"``). Invariants that need
context beyond a single document — the filename↔id match, references to
existing regras, the non-empty ``# Resolução`` body — live in
``validate_achado`` and the bundle layer. The same model/parser is reused
by the CLI and by pytest.
"""

from __future__ import annotations

import datetime
import re
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Literal

import yaml
from pydantic import BaseModel, ConfigDict, ValidationError, field_validator, model_validator

if TYPE_CHECKING:
    from collections.abc import Iterable
    from pathlib import Path

DOC_NAME_RE = re.compile(r"^achado-(\d+)$")
HEADING_RE = re.compile(r"^# (.+)$", re.MULTILINE)

# Starting vocabulary (P8) — explicitly not closed/final. Extend by PR as
# real cases are examined; this is a hypothesis, not a normative list.
NATUREZA_VALUES = ("juridica", "dados", "modelagem", "processo")

BODY_HEADINGS = ("Descrição", "Evidências", "Questão a investigar", "Resolução")


class AchadoValidationError(Exception):
    """Raised when one or more achado docs violate a P14.6 invariant."""


class Deteccao(BaseModel):
    """One mechanical occurrence an achado references, by stable fingerprint (P14.6)."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    detector: str
    fingerprint: str


class AchadoFrontmatter(BaseModel):
    """The typed ``type: Achado`` frontmatter — intra-document contract (P14.2/P14.6)."""

    model_config = ConfigDict(extra="forbid")

    type: Literal["Achado"]
    id: str
    nome: str
    situacao: Literal["aberto", "resolvido"]
    severidade: Literal["bloqueante", "informativo"]
    verificacao: Literal["mecanica", "manual", "hibrida"]
    natureza: Literal["juridica", "dados", "modelagem", "processo"]
    regras_afetadas: list[str]
    detectado_em: str
    detectado_por: str
    deteccoes: list[Deteccao] = []
    resolvido_em: str | None = None
    resolvido_por: str | None = None

    @field_validator("detectado_em", "resolvido_em", mode="before")
    @classmethod
    def _isodate(cls, value: object) -> object:
        """Accept an unquoted YAML date (parsed to date) as its ISO string."""
        if isinstance(value, datetime.date):
            return value.isoformat()
        return value

    @model_validator(mode="after")
    def _check_deteccoes_match_verificacao(self) -> AchadoFrontmatter:
        """P14.5/P14.6: mecanica/hibrida need deteccoes; manual forbids them."""
        if self.verificacao in ("mecanica", "hibrida") and not self.deteccoes:
            msg = f"verificacao={self.verificacao!r} requires at least one entry in 'deteccoes'"
            raise ValueError(msg)
        if self.verificacao == "manual" and self.deteccoes:
            msg = "verificacao='manual' must not have 'deteccoes'"
            raise ValueError(msg)
        return self

    @model_validator(mode="after")
    def _check_resolution_metadata(self) -> AchadoFrontmatter:
        """P14.3: situacao=resolvido requires resolvido_em/resolvido_por (body checked elsewhere)."""
        if self.situacao == "resolvido":
            if not self.resolvido_em:
                msg = "situacao=resolvido requires resolvido_em"
                raise ValueError(msg)
            if not self.resolvido_por:
                msg = "situacao=resolvido requires resolvido_por"
                raise ValueError(msg)
        return self


@dataclass
class Achado:
    """One achado: its typed-or-raw frontmatter plus body sections."""

    doc_id: str  # filename stem, e.g. "achado-0001"
    frontmatter: dict
    sections: dict[str, str] = field(default_factory=dict)

    @property
    def situacao(self) -> str:
        """The lifecycle state (``aberto``/``resolvido``); '' if malformed."""
        return str(self.frontmatter.get("situacao") or "")

    @property
    def regras_afetadas(self) -> list[str]:
        """The regra references this achado affects — the only source of the relation (P14.4)."""
        return list(self.frontmatter.get("regras_afetadas") or [])

    @property
    def fingerprints(self) -> list[str]:
        """The detection fingerprints this achado claims, from ``deteccoes`` (P14.6)."""
        return [d["fingerprint"] for d in self.frontmatter.get("deteccoes") or [] if "fingerprint" in d]


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
    """Render an achado's frontmatter + body sections into ``.md`` text.

    Used by tests and by the optional TODO scaffold — never to author real
    findings, which are written by hand (princípio da autoria humana).
    """
    fm_text = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False)
    body_parts = [f"# {heading}\n\n{sections.get(heading, '')}\n" for heading in BODY_HEADINGS]
    return f"---\n{fm_text}---\n\n" + "\n".join(body_parts)


def load_achados(bundle_dir: Path) -> list[Achado]:
    """Load every achado-*.md in bundle_dir/achados/, sorted by doc id.

    Loading is lenient (raw frontmatter dict) so ``validate_achado`` can
    report every problem instead of crashing on the first malformed doc.
    """
    achados_dir = bundle_dir / "achados"
    if not achados_dir.is_dir():
        return []
    achados = []
    for doc_path in sorted(achados_dir.glob("achado-*.md")):
        frontmatter, sections = parse_achado_doc(doc_path.read_text(encoding="utf-8"))
        achados.append(Achado(doc_id=doc_path.stem, frontmatter=frontmatter or {}, sections=sections))
    return achados


def _format_pydantic_errors(doc_id: str, exc: ValidationError) -> list[str]:
    """Turn a Pydantic ValidationError into one flat message per problem."""
    messages = []
    for err in exc.errors():
        loc = ".".join(str(part) for part in err["loc"]) or "<root>"
        messages.append(f"{doc_id}: {loc}: {err['msg']}")
    return messages


def _validate_context(achado: Achado, *, known_regra_ids: frozenset[str]) -> list[str]:
    """Invariants that need context beyond the single-document frontmatter model."""
    doc_id = achado.doc_id
    fm = achado.frontmatter
    errors = []

    if DOC_NAME_RE.match(doc_id) is None:
        errors.append(f"{doc_id}: filename is not of the form achado-NNNN.md")
    if fm.get("id") != doc_id:
        errors.append(f"{doc_id}: frontmatter id={fm.get('id')!r} does not match filename")

    regras_afetadas = achado.regras_afetadas
    if not regras_afetadas:
        errors.append(f"{doc_id}: regras_afetadas must not be empty")
    for ref in regras_afetadas:
        regra_id = ref.rsplit("/", 1)[-1].removesuffix(".md")
        if regra_id not in known_regra_ids:
            errors.append(f"{doc_id}: regras_afetadas references unknown regra {ref!r}")

    if achado.situacao == "resolvido" and not achado.sections.get("Resolução", "").strip():
        errors.append(f"{doc_id}: situacao=resolvido requires a non-empty # Resolução section")
    return errors


def validate_achado(achado: Achado, *, known_regra_ids: frozenset[str]) -> list[str]:
    """Return P14.6 violations for one achado (empty list = valid).

    Schema/enum/cross-field rules come from the Pydantic model; the
    filename↔id match, references to real regras and the non-empty
    resolution body come from the bundle context.
    """
    errors: list[str] = []
    try:
        AchadoFrontmatter.model_validate(achado.frontmatter)
    except ValidationError as exc:
        errors.extend(_format_pydantic_errors(achado.doc_id, exc))
    errors.extend(_validate_context(achado, known_regra_ids=known_regra_ids))
    return errors


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

    A **derived** artifact (P14.7): generated by the derivar step, never by
    validation. Backlinks are generated here, never stored inside regra-*.md.
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
    """Rewrite the bundle-root index.md so it lists achados/ alongside regras/ (P14.1)."""
    dataset_text = (bundle_dir / "regras-sisprev.md").read_text(encoding="utf-8")
    _, dataset_fm_text, _ = dataset_text.split("---", 2)
    dataset_fm = yaml.safe_load(dataset_fm_text)
    row_count = dataset_fm["row_count"]
    description = dataset_fm["description"]

    achados = load_achados(bundle_dir)
    abertos = sum(1 for a in achados if a.situacao == "aberto")

    fm_text = yaml.safe_dump({"okf_version": "0.1"}, sort_keys=False)
    regras_line = f"{row_count} regras individuais, uma por linha da planilha original."
    body = (
        "# Regras do Sisprev\n\n"
        f"* [regras-sisprev.md](regras-sisprev.md) - {description}\n"
        f"* [regras/](regras/index.md) - {regras_line}\n"
        f"* [achados/](achados/index.md) - {len(achados)} achado(s), {abertos} aberto(s).\n"
    )
    (bundle_dir / "index.md").write_text(f"---\n{fm_text}---\n\n{body}", encoding="utf-8")


def scaffold_achado(bundle_dir: Path, regra_ids: Iterable[str]) -> str:
    """Reserve the next id and write an **incomplete** TODO scaffold (P14.2).

    This only reserves the number and lists the regras under investigation —
    it fills no semantic field. The TODO markers are invalid for the CI on
    purpose: the auditor must complete the authoring by hand.
    """
    doc_id = next_achado_id(bundle_dir)
    frontmatter = {
        "type": "Achado",
        "id": doc_id,
        "nome": "TODO",
        "situacao": "aberto",
        "severidade": "TODO",
        "verificacao": "TODO",
        "natureza": "TODO",
        "regras_afetadas": [f"/regras/{regra_id}.md" for regra_id in regra_ids],
        "detectado_em": "TODO",
        "detectado_por": "TODO",
    }
    sections = dict.fromkeys(BODY_HEADINGS, "")
    (bundle_dir / "achados").mkdir(parents=True, exist_ok=True)
    (bundle_dir / "achados" / f"{doc_id}.md").write_text(
        build_achado_doc(frontmatter, sections),
        encoding="utf-8",
    )
    return doc_id
