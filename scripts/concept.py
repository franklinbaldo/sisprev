"""Shared OKF concept doc base (RFC 0001) — one representation for Regra/Achado/Dispositivo.

Every ``type: X`` markdown doc in this repo (Regra, Achado, Dispositivo,
...) is an OKF "concept doc": YAML frontmatter + a free-form body. This
module holds the one parsing routine every concept loader uses (split on
the ``---`` delimiters, scan ``# Heading`` sections) and the ``Concept``
base model every concept type inherits from.

``Concept`` itself only requires ``doc_id``/``frontmatter``/``body`` to have
the right *shape* (a string, a dict, a string) — never that the frontmatter
is semantically well-formed. A doc with malformed frontmatter (missing
required keys, wrong enum values, ...) must still *load* — so a validator
can report it as a ``Violation`` — never raise mid-``Bundle.load()``. Each
concept type keeps its own Pydantic ``*Frontmatter`` contract (extending
``ConceptFrontmatter``) for that semantic check, applied only when a
validator explicitly asks.
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict

_HEADING_RE = re.compile(r"^# (.+)$", re.MULTILINE)


class ConceptDocError(Exception):
    """Raised when a concept doc doesn't even have parseable ``---``-delimited frontmatter."""


class ConceptFrontmatter(BaseModel):
    """Fields every OKF concept doc's frontmatter carries (SPEC.md)."""

    model_config = ConfigDict(extra="forbid")

    type: str
    id: str


class Concept(BaseModel):
    """One authored concept doc: raw frontmatter + raw body, never itself semantically validated."""

    model_config = ConfigDict(frozen=True)

    doc_id: str
    frontmatter: dict[str, object]
    body: str = ""
    # Root of the OKF bundle this doc was loaded from (e.g. okf/dispositivos
    # for a Dispositivo, okf/regras-sisprev for a Regra/Achado) — every real
    # loader passes this explicitly; the default is only for tests that don't
    # exercise provenance.
    bundle_dir: Path = Path()

    @property
    def sections(self) -> dict[str, str]:
        """Level-one (``# Heading``) body sections, keyed by heading text."""
        return parse_sections(self.body)


def parse_sections(body: str) -> dict[str, str]:
    """Split body text into level-one heading sections — never nested (``## `` is not a boundary)."""
    sections: dict[str, str] = {}
    matches = list(_HEADING_RE.finditer(body))
    for idx, match in enumerate(matches):
        heading = match.group(1).strip()
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(body)
        sections[heading] = body[start:end].strip("\n")
    return sections


def build_body(sections: dict[str, str]) -> str:
    """Render a sections dict into markdown body text — the inverse of ``parse_sections``.

    Used by scaffolding/derive code and by tests that find it more natural
    to build fixtures from a sections dict than from raw markdown text.
    """
    return "\n".join(f"# {heading}\n\n{content}\n" for heading, content in sections.items())


def parse_concept_doc(text: str) -> tuple[dict[str, object], str]:
    """Split a concept doc into its frontmatter dict and raw body text.

    Returns the body *unparsed* — callers that need named sections use
    ``parse_sections(body)`` or ``Concept.sections``; callers that need the
    exact text (e.g. a dispositivo's provision text) use the body as-is.
    """
    try:
        _, fm_text, body = text.split("---", 2)
    except ValueError as exc:
        msg = "concept document must contain YAML frontmatter delimited by ---"
        raise ConceptDocError(msg) from exc
    frontmatter = yaml.safe_load(fm_text)
    return frontmatter or {}, body.strip("\n")
