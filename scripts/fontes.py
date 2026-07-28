"""Shared ``fontes`` validation — the web URLs a transcription can be checked against.

A dispositivo's body is legal text transcribed verbatim, and a norma's name
is a citation: both are only auditable if the reader can reach the official
publication the transcription came from. So ``fontes`` is a **list of web
URLs** (at least one), not free-form prose — an auditor comparing the doc
against Planalto/ALE-RO/the Diário Oficial follows the link, and the site
renders each one as a real anchor rather than as unclickable text.

Stored and compared as the exact string the author wrote: no normalization,
no ``HttpUrl`` coercion. Pydantic's URL types re-render what they parse
(adding a trailing slash, lowercasing a host), which would silently make the
frontmatter disagree with the byte-identical round-trip the bundle relies
on. Validation here only *rejects* what is not a web URL.
"""

from __future__ import annotations

import re

# Deliberately narrow: an official publication is reachable over http(s).
# A DOI, an SEI process number or a bare filename may all be legitimate
# provenance someday, but they are not what this field promises today, and
# accepting them silently would make "every fonte is a link" untrue on the
# published site.
_URL_RE = re.compile(r"^https?://[^\s]+$")


def validar_fontes(fontes: list[str]) -> list[str]:
    """Return ``fontes`` unchanged, or raise if any entry is not an http(s) URL.

    Written as a plain function so both ``NormaFrontmatter`` and
    ``DispositivoFrontmatter`` attach it with ``field_validator("fontes")``
    instead of restating the rule.
    """
    for fonte in fontes:
        if _URL_RE.fullmatch(fonte) is None:
            msg = f"fonte {fonte!r} must be an http(s) URL pointing at the official publication"
            raise ValueError(msg)
    return fontes
