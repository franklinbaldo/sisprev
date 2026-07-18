"""P14 — Achado concept: typed schema, doc I/O, and validation (RFC 0001).

Achados are authored Markdown sources. Code may validate their contract and
derive indexes, but never decides their semantic content.
"""

from __future__ import annotations

import datetime
import re
from typing import TYPE_CHECKING, Literal

import yaml
from concept import (
    Concept,
    ConceptDocError,
    ConceptFrontmatter,
    format_pydantic_errors,
    parse_concept_doc,
    parse_sections,
)
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    ValidationError,
    field_validator,
    model_validator,
)

if TYPE_CHECKING:
    from collections.abc import Iterable
    from pathlib import Path

DOC_NAME_RE = re.compile(r"^achado-(\d{4})$")
REGRA_REF_RE = re.compile(r"^/regras/regra-\d{4}\.md$")
FINGERPRINT_RE = re.compile(r"^sha256:[0-9a-f]{64}$")

BODY_HEADINGS = ("Descrição", "Evidências", "Questão a investigar", "Resolução")
_REQUIRED_OPEN_SECTIONS = BODY_HEADINGS[:3]


class AchadoValidationError(Exception):
    """Raised when one or more achado docs violate a P14 invariant."""


class Deteccao(BaseModel):
    """One mechanical occurrence referenced by a stable fingerprint."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    detector: str = Field(min_length=1)
    fingerprint: str

    @field_validator("fingerprint")
    @classmethod
    def _valid_fingerprint(cls, value: str) -> str:
        if FINGERPRINT_RE.fullmatch(value) is None:
            msg = "must match sha256:<64 lowercase hex characters>"
            raise ValueError(msg)
        return value


class AchadoFrontmatter(ConceptFrontmatter):
    """Typed frontmatter contract for ``type: Achado``."""

    type: Literal["Achado"]
    nome: str = Field(min_length=1)
    situacao: Literal["aberto", "resolvido"]
    severidade: Literal["bloqueante", "informativo"]
    verificacao: Literal["mecanica", "manual", "hibrida"]
    natureza: Literal["juridica", "dados", "modelagem", "processo"]
    regras_afetadas: list[str] = Field(min_length=1)
    detectado_em: datetime.date
    detectado_por: str = Field(min_length=1)
    deteccoes: list[Deteccao] = Field(default_factory=list)
    resolvido_em: datetime.date | None = None
    resolvido_por: str | None = None
    efeito_deteccao: Literal["deve_desaparecer", "pode_persistir"] | None = None

    @field_validator("detectado_em", "resolvido_em", mode="before")
    @classmethod
    def _parse_iso_date(cls, value: object) -> object:
        """Accept YAML dates or strict ISO date strings."""
        if value is None or isinstance(value, datetime.date):
            return value
        if isinstance(value, str):
            return datetime.date.fromisoformat(value)
        return value

    @model_validator(mode="after")
    def _check_deteccoes_match_verificacao(self) -> AchadoFrontmatter:
        if self.verificacao in ("mecanica", "hibrida") and not self.deteccoes:
            msg = f"verificacao={self.verificacao!r} requires at least one entry in 'deteccoes'"
            raise ValueError(msg)
        if self.verificacao == "manual" and self.deteccoes:
            msg = "verificacao='manual' must not have 'deteccoes'"
            raise ValueError(msg)

        pairs = [(item.detector, item.fingerprint) for item in self.deteccoes]
        if len(pairs) != len(set(pairs)):
            msg = "deteccoes must not contain duplicate detector/fingerprint pairs"
            raise ValueError(msg)
        fingerprints = [item.fingerprint for item in self.deteccoes]
        if len(fingerprints) != len(set(fingerprints)):
            msg = "one fingerprint must not be claimed more than once in the same achado"
            raise ValueError(msg)
        return self

    @model_validator(mode="after")
    def _check_resolution_contract(self) -> AchadoFrontmatter:
        if self.situacao == "aberto":
            if self.resolvido_em or self.resolvido_por or self.efeito_deteccao:
                msg = "situacao=aberto forbids resolution metadata and efeito_deteccao"
                raise ValueError(msg)
            return self

        if not self.resolvido_em:
            msg = "situacao=resolvido requires resolvido_em"
            raise ValueError(msg)
        if not self.resolvido_por:
            msg = "situacao=resolvido requires resolvido_por"
            raise ValueError(msg)
        if self.resolvido_em < self.detectado_em:
            msg = "resolvido_em must not be earlier than detectado_em"
            raise ValueError(msg)

        if self.deteccoes and self.efeito_deteccao is None:
            msg = "resolved mecanica/hibrida achado requires efeito_deteccao"
            raise ValueError(msg)
        if not self.deteccoes and self.efeito_deteccao is not None:
            msg = "manual achado must not define efeito_deteccao"
            raise ValueError(msg)
        return self


class Achado(Concept):
    """One authored finding — an OKF concept doc (P14)."""

    @property
    def situacao(self) -> str:
        """Return the lifecycle state, or an empty string if malformed."""
        return str(self.frontmatter.get("situacao") or "")

    @property
    def efeito_deteccao(self) -> str:
        """Return the declared effect of resolution on linked detections."""
        return str(self.frontmatter.get("efeito_deteccao") or "")

    @property
    def regras_afetadas(self) -> list[str]:
        """Return the canonical rule references affected by the finding."""
        raw = self.frontmatter.get("regras_afetadas")
        return [str(ref) for ref in raw] if isinstance(raw, list) else []

    @property
    def detection_refs(self) -> list[tuple[str, str]]:
        """Return detector and fingerprint pairs from the finding."""
        raw = self.frontmatter.get("deteccoes")
        if not isinstance(raw, list):
            return []
        refs: list[tuple[str, str]] = []
        for item in raw:
            if not isinstance(item, dict):
                continue
            detector, fingerprint = item.get("detector"), item.get("fingerprint")
            if detector and fingerprint:
                refs.append((str(detector), str(fingerprint)))
        return refs

    @property
    def fingerprints(self) -> list[str]:
        """Return every referenced detection fingerprint."""
        return [fingerprint for _, fingerprint in self.detection_refs]


def parse_achado_doc(text: str) -> tuple[dict, dict[str, str]]:
    """Split an achado doc into frontmatter and named body sections."""
    try:
        frontmatter, body = parse_concept_doc(text)
    except ConceptDocError as exc:
        msg = "achado document must contain YAML frontmatter delimited by ---"
        raise AchadoValidationError(msg) from exc
    return frontmatter, parse_sections(body)


def build_achado_doc(frontmatter: dict, sections: dict[str, str]) -> str:
    """Render a document for tests or an explicitly incomplete scaffold."""
    fm_text = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False)
    body_parts = [f"# {heading}\n\n{sections.get(heading, '')}\n" for heading in BODY_HEADINGS]
    return f"---\n{fm_text}---\n\n" + "\n".join(body_parts)


def load_achados(bundle_dir: Path) -> list[Achado]:
    """Load authored achado documents in filename order."""
    achados_dir = bundle_dir / "achados"
    if not achados_dir.is_dir():
        return []
    achados = []
    for doc_path in sorted(achados_dir.glob("achado-*.md")):
        frontmatter, body = parse_concept_doc(doc_path.read_text(encoding="utf-8"))
        achados.append(
            Achado(doc_id=doc_path.stem, frontmatter=frontmatter, body=body, bundle_dir=bundle_dir)
        )
    return achados


def _validate_context(achado: Achado, *, known_regra_ids: frozenset[str]) -> list[str]:
    doc_id = achado.doc_id
    fm = achado.frontmatter
    errors: list[str] = []

    if DOC_NAME_RE.fullmatch(doc_id) is None:
        errors.append(f"{doc_id}: filename is not of the form achado-NNNN.md")
    if fm.get("id") != doc_id:
        errors.append(f"{doc_id}: frontmatter id={fm.get('id')!r} does not match filename")

    refs = achado.regras_afetadas
    if len(refs) != len(set(refs)):
        errors.append(f"{doc_id}: regras_afetadas must not contain duplicates")
    for ref in refs:
        if REGRA_REF_RE.fullmatch(ref) is None:
            errors.append(f"{doc_id}: non-canonical regra reference {ref!r}")
            continue
        regra_id = ref.rsplit("/", 1)[-1].removesuffix(".md")
        if regra_id not in known_regra_ids:
            errors.append(f"{doc_id}: regras_afetadas references unknown regra {ref!r}")

    errors.extend(
        f"{doc_id}: requires a non-empty # {heading} section"
        for heading in _REQUIRED_OPEN_SECTIONS
        if not achado.sections.get(heading, "").strip()
    )
    if achado.situacao == "resolvido" and not achado.sections.get("Resolução", "").strip():
        errors.append(f"{doc_id}: situacao=resolvido requires a non-empty # Resolução section")
    return errors


def validate_achado(achado: Achado, *, known_regra_ids: frozenset[str]) -> list[str]:
    """Return every intra-document and contextual P14 violation."""
    errors: list[str] = []
    try:
        AchadoFrontmatter.model_validate(achado.frontmatter)
    except ValidationError as exc:
        errors.extend(format_pydantic_errors(achado.doc_id, exc))
    errors.extend(_validate_context(achado, known_regra_ids=known_regra_ids))
    return errors


def validate_bundle_achados(bundle_dir: Path, *, known_regra_ids: frozenset[str]) -> list[str]:
    """Validate all achados and their current-tree sequence."""
    achados = load_achados(bundle_dir)
    errors: list[str] = []
    numbers: list[int] = []

    for achado in achados:
        errors.extend(validate_achado(achado, known_regra_ids=known_regra_ids))
        match = DOC_NAME_RE.fullmatch(achado.doc_id)
        if match is not None:
            numbers.append(int(match.group(1)))

    if len(numbers) != len(set(numbers)):
        errors.append("duplicate achado numeric id")
    if numbers:
        expected = list(range(1, max(numbers) + 1))
        if sorted(numbers) != expected:
            missing = sorted(set(expected) - set(numbers))
            errors.append(f"achado ids must be contiguous; missing {missing}")
    return errors


def next_achado_id(bundle_dir: Path) -> str:
    """Return the next current-tree id; history checks prevent reuse after deletion."""
    numbers = []
    for doc_path in (bundle_dir / "achados").glob("achado-*.md") if (bundle_dir / "achados").is_dir() else ():
        match = DOC_NAME_RE.fullmatch(doc_path.stem)
        if match is not None:
            numbers.append(int(match.group(1)))
    return f"achado-{(max(numbers, default=0) + 1):04d}"


def regenerate_achados_index(bundle_dir: Path) -> None:
    """Regenerate the derived achados and bundle-root indexes."""
    achados_dir = bundle_dir / "achados"
    achados_dir.mkdir(parents=True, exist_ok=True)
    lines = []
    for achado in load_achados(bundle_dir):
        fm = achado.frontmatter
        refs = ", ".join(ref.rsplit("/", 1)[-1].removesuffix(".md") for ref in achado.regras_afetadas)
        lines.append(
            f"* [{fm.get('nome', '')}]({achado.doc_id}.md) - "
            f"{fm.get('situacao', '')}/{fm.get('severidade', '')} - {refs}"
        )
    body = "# Achados\n\n" + ("\n".join(lines) + "\n" if lines else "")
    (achados_dir / "index.md").write_text(body, encoding="utf-8")
    regenerate_root_index(bundle_dir)


def regenerate_root_index(bundle_dir: Path) -> None:
    """Regenerate the bundle-root index from authored sources."""
    dataset_text = (bundle_dir / "regras-sisprev.md").read_text(encoding="utf-8")
    _, dataset_fm_text, _ = dataset_text.split("---", 2)
    dataset_fm = yaml.safe_load(dataset_fm_text)
    achados = load_achados(bundle_dir)
    abertos = sum(1 for achado in achados if achado.situacao == "aberto")

    fm_text = yaml.safe_dump({"okf_version": "0.1"}, sort_keys=False)
    body = (
        "# Regras do Sisprev\n\n"
        f"* [regras-sisprev.md](regras-sisprev.md) - {dataset_fm['description']}\n"
        f"* [regras/](regras/index.md) - {dataset_fm['row_count']} regras individuais, "
        "uma por linha da planilha original.\n"
        f"* [achados/](achados/index.md) - {len(achados)} achado(s), {abertos} aberto(s).\n"
    )
    (bundle_dir / "index.md").write_text(f"---\n{fm_text}---\n\n{body}", encoding="utf-8")


def scaffold_achado(bundle_dir: Path, regra_ids: Iterable[str]) -> str:
    """Reserve an id and write only an intentionally invalid TODO scaffold."""
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
