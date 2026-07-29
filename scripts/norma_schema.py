"""P4 — ``type: Norma``: the closed vocabulary of citable norms (RFC 0001).

Every dispositivo declares the norm it belongs to by *key* (``norma: cf88``),
not by prose. The key resolves to an authored ``norma.md`` concept doc that
holds the norm's canonical name, its short form, and its official source
URLs — one place, instead of the same name retyped in every dispositivo of
that norm.

This is P4's "vocabulário fechado de normas citáveis" made structural: a
dispositivo whose ``norma`` key has no authored doc fails validation, so a
new norm enters the corpus by being authored, never by being typed slightly
differently in a frontmatter field. RFC 0001's E6 (the same norm appearing
under at least three spellings) is exactly the drift this prevents.

The doc lives at ``okf/dispositivos/<key>/norma.md`` — colocated with the
provisions it governs, so the directory is self-describing.
"""

from __future__ import annotations

import datetime
import re
from functools import cached_property
from typing import TYPE_CHECKING, Literal, Self

from concept import Concept, ConceptFrontmatter, format_pydantic_errors, parse_concept_doc
from fontes import validar_fontes
from pydantic import Field, ValidationError, field_validator, model_validator

if TYPE_CHECKING:
    from pathlib import Path

# The filename every norma doc uses inside its own directory. Distinct from
# index.md (generated) so a loader can tell authored source from derived
# artifact by name alone.
NORMA_DOC = "norma.md"

NORMA_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


class NormaFrontmatter(ConceptFrontmatter):
    """Typed frontmatter contract for ``type: Norma`` (P4).

    ``vigencia_inicio``/``vigencia_fim`` are the norm's *own* life, not any
    provision's. They are what lets a human establish that a provision's
    wording history is complete — if the authored wordings tile the norm's
    whole life with no gap, no other wording can exist. Both stay optional:
    a norm whose dates were not confirmed is authored without them, and
    every check that depends on them declines to conclude rather than
    assuming.
    """

    type: Literal["Norma"]
    nome: str = Field(min_length=1)
    apelido: str = Field(min_length=1)
    vigencia_inicio: datetime.date | None = None
    vigencia_fim: datetime.date | None = None
    fontes: list[str] = Field(min_length=1)

    _check_fontes = field_validator("fontes")(validar_fontes)

    @field_validator("vigencia_inicio", "vigencia_fim", mode="before")
    @classmethod
    def _parse_iso_date(cls, value: object) -> object:
        """Accept YAML dates or strict ISO date strings."""
        if value is None or isinstance(value, datetime.date):
            return value
        if isinstance(value, str):
            return datetime.date.fromisoformat(value)
        return value

    @model_validator(mode="after")
    def _check_janela(self) -> Self:
        """Reject a backwards validity window, as the dispositivo contract does."""
        if (
            self.vigencia_inicio is not None
            and self.vigencia_fim is not None
            and self.vigencia_fim < self.vigencia_inicio
        ):
            msg = f"vigencia_fim {self.vigencia_fim} precedes vigencia_inicio {self.vigencia_inicio}"
            raise ValueError(msg)
        return self


class Norma(Concept):
    """One authored norm — an OKF concept doc keyed by its citation slug (P4)."""

    @cached_property
    def _validation(self) -> NormaFrontmatter | ValidationError:
        try:
            return NormaFrontmatter.model_validate(self.frontmatter)
        except ValidationError as exc:
            return exc

    @property
    def contract(self) -> NormaFrontmatter | None:
        """Return the validated P4 frontmatter contract, or None if malformed."""
        result = self._validation
        return result if isinstance(result, NormaFrontmatter) else None

    @property
    def validation_error(self) -> ValidationError | None:
        """Return the cached contract ValidationError, or None if the doc is valid."""
        result = self._validation
        return result if isinstance(result, ValidationError) else None

    @property
    def nome(self) -> str:
        """Return the norm's canonical full name, falling back to an ungated raw read.

        The fallback mirrors ``Regra.status_regra``/``Achado.situacao``: an
        index or a page still needs the name from a doc that happens to be
        invalid for an unrelated field's sake.
        """
        if self.contract is not None:
            return self.contract.nome
        return str(self.frontmatter.get("nome") or self.doc_id)

    @property
    def apelido(self) -> str:
        """Return the norm's short citation form (``CF/88``), with the same ungated fallback."""
        if self.contract is not None:
            return self.contract.apelido
        return str(self.frontmatter.get("apelido") or self.nome)

    @property
    def janela(self) -> tuple[datetime.date, datetime.date | None] | None:
        """Return the norm's own validity window, or None when it isn't declared.

        Read from the validated contract only — deliberately **without** the
        ungated raw fallback that ``nome``/``apelido`` use. Those feed a page
        that must still render from a doc invalid for an unrelated field's
        sake; this window feeds a check that can accuse a regra of citing a
        wording that never existed, and a value read past a failed validation
        is not evidence good enough for that.
        """
        contrato = self.contract
        if contrato is None or contrato.vigencia_inicio is None:
            return None
        return (contrato.vigencia_inicio, contrato.vigencia_fim)


def load_normas(bundle_dir: Path) -> list[Norma]:
    """Load every authored norma doc, keyed by its directory name, in path order.

    Returns an empty list if the bundle directory doesn't exist yet — P3/P4
    infrastructure may be present before anything has been authored.
    """
    if not bundle_dir.is_dir():
        return []
    normas = []
    for doc_path in sorted(bundle_dir.glob(f"*/{NORMA_DOC}")):
        frontmatter, body = parse_concept_doc(doc_path.read_text(encoding="utf-8"))
        normas.append(
            Norma(
                doc_id=doc_path.parent.name,
                frontmatter=frontmatter,
                body=body,
                bundle_dir=bundle_dir,
            )
        )
    return normas


def validate_norma(norma: Norma) -> list[str]:
    """Return every intra-document P4 violation for one norma doc."""
    errors: list[str] = []
    doc_id = norma.doc_id

    if NORMA_ID_RE.fullmatch(doc_id) is None:
        errors.append(f"{doc_id}: directory name is not a valid norma key (lowercase, digits, hyphens)")
    if norma.frontmatter.get("id") != doc_id:
        errors.append(
            f"{doc_id}: frontmatter id={norma.frontmatter.get('id')!r} does not match its directory"
        )
    if norma.validation_error is not None:
        errors.extend(format_pydantic_errors(doc_id, norma.validation_error))
    return errors


def normas_por_id(bundle_dir: Path) -> dict[str, Norma]:
    """Return every authored norma keyed by its id, for dispositivo link resolution."""
    return {norma.doc_id: norma for norma in load_normas(bundle_dir)}
