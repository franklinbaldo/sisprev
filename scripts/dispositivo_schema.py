"""P3 — Dispositivo concept: typed schema, doc I/O, and validation (RFC 0001).

A dispositivo is one legal provision (article/paragraph/inciso/alínea) at
the smallest granularity actually cited by a regra — "decomposição sob
demanda", never a preventive fragmentation of the whole norm (RFC 0001, P3,
decisão 2026-07-17). Its body is the exact text of the provision, in the
applicable wording; a wording change over time is a *separate* file, never
an edit in place, since a regra cites the specific wording that grounds it.

Dispositivos are authored sources, transcribed verbatim from an official
publication (``fonte``) — never paraphrased, summarized, or inferred. Code
validates the contract (identity, required fields, filename/id agreement)
but never decides a provision's text or scope.
"""

from __future__ import annotations

import datetime
import re
from functools import cached_property
from typing import TYPE_CHECKING, Literal

import yaml
from concept import Concept, ConceptDocError, ConceptFrontmatter, format_pydantic_errors, parse_concept_doc
from md_format import write_markdown
from pydantic import Field, ValidationError, field_validator

if TYPE_CHECKING:
    from pathlib import Path

# doc_id is the file's path relative to the dispositivos bundle root,
# POSIX-separated, without the .md suffix (e.g. "cf88/art-40-i-original") —
# mirrors the OKF absolute-link form `/dispositivos/<doc_id>.md` (P3, SPEC.md
# §5.1), unlike achados/regras which are a flat `tipo-NNNN` id.
DOC_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*(/[a-z0-9][a-z0-9-]*)+$")
DISPOSITIVO_REF_RE = re.compile(r"^/dispositivos/([a-z0-9][a-z0-9-]*/)+[a-z0-9][a-z0-9-]*\.md$")


class DispositivoValidationError(Exception):
    """Raised when one or more dispositivo docs violate a P3 invariant."""


class DispositivoFrontmatter(ConceptFrontmatter):
    """Typed frontmatter contract for ``type: Dispositivo``."""

    type: Literal["Dispositivo"]
    norma: str = Field(min_length=1)
    artigo: str = Field(min_length=1)
    paragrafo: str | None = None
    inciso: str | None = None
    alinea: str | None = None
    redacao_dada_por: str | None = None
    vigencia_inicio: datetime.date | None = None
    vigencia_fim: datetime.date | None = None
    fonte: str = Field(min_length=1)

    @field_validator("vigencia_inicio", "vigencia_fim", mode="before")
    @classmethod
    def _parse_iso_date(cls, value: object) -> object:
        """Accept YAML dates or strict ISO date strings."""
        if value is None or isinstance(value, datetime.date):
            return value
        if isinstance(value, str):
            return datetime.date.fromisoformat(value)
        return value


class Dispositivo(Concept):
    """One authored legal provision — an OKF concept doc (P3).

    Unlike achados/regras, the body has no named sections — P3 requires the
    body to be exactly the provision's text, nothing else; ``texto`` is a
    domain-named alias for ``body``.
    """

    @property
    def texto(self) -> str:
        """Return the provision's exact transcribed text."""
        return self.body

    @cached_property
    def _validation(self) -> DispositivoFrontmatter | ValidationError:
        try:
            return DispositivoFrontmatter.model_validate(self.frontmatter)
        except ValidationError as exc:
            return exc

    @property
    def contract(self) -> DispositivoFrontmatter | None:
        """Return the validated P3 frontmatter contract, or None if malformed."""
        result = self._validation
        return result if isinstance(result, DispositivoFrontmatter) else None

    @property
    def validation_error(self) -> ValidationError | None:
        """Return the cached P3 contract ValidationError, or None if the doc is valid."""
        result = self._validation
        return result if isinstance(result, ValidationError) else None


def parse_dispositivo_doc(text: str) -> tuple[dict[str, object], str]:
    """Split a dispositivo doc into its frontmatter dict and the raw body text."""
    try:
        return parse_concept_doc(text)
    except ConceptDocError as exc:
        msg = "dispositivo document must contain YAML frontmatter delimited by ---"
        raise DispositivoValidationError(msg) from exc


def load_dispositivos(bundle_dir: Path) -> list[Dispositivo]:
    """Load every authored dispositivo document, in path order.

    Returns an empty list if the bundle directory doesn't exist yet — P3's
    infrastructure may be present before any dispositivo has been authored.
    """
    if not bundle_dir.is_dir():
        return []
    dispositivos = []
    for doc_path in sorted(bundle_dir.rglob("*.md")):
        if doc_path.name == "index.md":
            continue
        doc_id = doc_path.relative_to(bundle_dir).with_suffix("").as_posix()
        frontmatter, body = parse_dispositivo_doc(doc_path.read_text(encoding="utf-8"))
        dispositivos.append(
            Dispositivo(doc_id=doc_id, frontmatter=frontmatter, body=body, bundle_dir=bundle_dir)
        )
    return dispositivos


def validate_dispositivo(dispositivo: Dispositivo) -> list[str]:
    """Return every intra-document P3 violation.

    Reuses ``dispositivo.validation_error`` (cached on first access) instead
    of re-running ``DispositivoFrontmatter.model_validate()``.
    """
    errors: list[str] = []
    doc_id = dispositivo.doc_id

    if DOC_ID_RE.fullmatch(doc_id) is None:
        errors.append(f"{doc_id}: path is not of the form <norma>/.../<artigo-slug>.md")
    if dispositivo.frontmatter.get("id") != doc_id:
        errors.append(f"{doc_id}: frontmatter id={dispositivo.frontmatter.get('id')!r} does not match path")
    if not dispositivo.texto.strip():
        errors.append(f"{doc_id}: body must contain the provision's exact text (P3), got empty body")

    if dispositivo.validation_error is not None:
        errors.extend(format_pydantic_errors(doc_id, dispositivo.validation_error))
    return errors


def validate_bundle_dispositivos(bundle_dir: Path) -> list[str]:
    """Validate every dispositivo doc in the bundle."""
    errors: list[str] = []
    for dispositivo in load_dispositivos(bundle_dir):
        errors.extend(validate_dispositivo(dispositivo))
    return errors


def dispositivo_ids(bundle_dir: Path) -> frozenset[str]:
    """Return every currently authored dispositivo's doc_id, for P3 link resolution."""
    return frozenset(d.doc_id for d in load_dispositivos(bundle_dir))


def regenerate_dispositivos_index(bundle_dir: Path) -> None:
    """Regenerate every norma subdirectory's index.md plus the bundle-root index.md.

    No-op if the bundle directory doesn't exist yet — P3's infrastructure
    may land before the first dispositivo is authored.
    """
    if not bundle_dir.is_dir():
        return

    dispositivos = load_dispositivos(bundle_dir)
    by_norma_dir: dict[str, list[Dispositivo]] = {}
    for dispositivo in dispositivos:
        if "/" not in dispositivo.doc_id:
            # Not nested under a norma directory — malformed per DOC_ID_RE,
            # already reported by validate_dispositivo(); skip here rather
            # than write to bundle_dir/<doc_id>/index.md, a directory that
            # (for a top-level file like this) was never created.
            continue
        norma_dir = dispositivo.doc_id.rsplit("/", 1)[0]
        by_norma_dir.setdefault(norma_dir, []).append(dispositivo)

    for norma_dir, items in by_norma_dir.items():
        lines = [
            f"* [{item.frontmatter.get('artigo', '')}]({item.doc_id.rsplit('/', 1)[-1]}.md) - "
            f"{item.frontmatter.get('norma', '')}"
            for item in items
        ]
        body = f"# {norma_dir}\n\n" + "\n".join(lines) + "\n"
        write_markdown(bundle_dir / norma_dir / "index.md", body)

    normas = sorted(by_norma_dir)
    root_lines = [
        f"* [{norma}/]({norma}/index.md) - {len(by_norma_dir[norma])} dispositivo(s)" for norma in normas
    ]
    root_fm = yaml.safe_dump({"okf_version": "0.1"}, sort_keys=False)
    root_body = "# Dispositivos legais\n\n" + ("\n".join(root_lines) + "\n" if root_lines else "")
    write_markdown(bundle_dir / "index.md", f"---\n{root_fm}---\n\n{root_body}")
