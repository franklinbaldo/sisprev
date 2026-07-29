"""P3 — Dispositivo concept: typed schema, doc I/O, and validation (RFC 0001).

A dispositivo is one legal provision at the smallest granularity actually
cited by a regra — "decomposição sob demanda", never a preventive
fragmentation of the whole norm (RFC 0001, P3, decisão 2026-07-17). Its body
is the exact text of the provision, in the applicable wording; a wording
change over time is a *separate* file, never an edit in place, since a regra
cites the specific wording that grounds it.

**Identity is derived, never composed by hand** (refactor 2026-07-27). A
dispositivo lives at ``<norma>/<endereço>/<redação>.md``:

    okf/dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md

- ``<norma>`` is a key into the closed vocabulary of citable norms (P4,
  ``norma_schema``), resolved against an authored ``norma.md``;
- ``<endereço>`` is ``slug_do_endereco(componentes)`` — a pure function of
  the frontmatter, recomputed and compared here, so the path can never drift
  from the address it claims to hold;
- ``<redação>`` is the amending norm's key, or literally ``original``. The
  directory is therefore *the provision* and the files inside it are *its
  wordings*: "every wording of art. 40, § 1º, I" is a directory listing, and
  adding a later wording never renames an earlier one.

That split is what the previous flat-slug shape could not express — it fused
provision and wording into one opaque token (``art-40-p1-i-ec41-2003``)
whose redação suffix was present on some docs and absent on others, checked
by nothing.

Dispositivos are authored sources, transcribed verbatim from an official
publication (``fontes``) — never paraphrased, summarized, or inferred. Code
validates the contract (identity, required fields, path/frontmatter
agreement, legal nesting, non-overlapping wordings) but never decides a
provision's text or scope.
"""

from __future__ import annotations

import datetime
import itertools
import re
from functools import cached_property
from typing import TYPE_CHECKING, Literal, Self

import yaml
from concept import Concept, ConceptDocError, ConceptFrontmatter, format_pydantic_errors, parse_concept_doc
from dispositivo_endereco import (
    Componente,
    chave_de_ordem,
    rotulo_do_endereco,
    slug_do_endereco,
    validar_aninhamento,
)
from fontes import validar_fontes
from md_format import write_markdown
from norma_schema import NORMA_DOC, Norma, load_normas, validate_norma
from pydantic import Field, ValidationError, field_validator, model_validator

if TYPE_CHECKING:
    from pathlib import Path

# doc_id is the file's path relative to the dispositivos bundle root, POSIX-
# separated, without the .md suffix — exactly three segments,
# <norma>/<endereço>/<redação>, mirroring the OKF absolute-link form
# `/dispositivos/<doc_id>.md` (P3, SPEC.md §5.1). Unlike achados/regras,
# which are a flat `tipo-NNNN` id, every segment here is meaningful and
# derived, so the shape is pinned rather than left to a generic path regex.
_SEG = r"[a-z0-9][a-z0-9-]*"
DOC_ID_RE = re.compile(rf"^{_SEG}/{_SEG}/{_SEG}$")
DISPOSITIVO_REF_RE = re.compile(rf"^/dispositivos/{_SEG}/{_SEG}/{_SEG}\.md$")

# The redação path segment used when the provision is in its original
# wording — the one value that is not another norm's key.
REDACAO_ORIGINAL = "original"


class DispositivoValidationError(Exception):
    """Raised when one or more dispositivo docs violate a P3 invariant."""


class DispositivoFrontmatter(ConceptFrontmatter):
    """Typed frontmatter contract for ``type: Dispositivo``."""

    type: Literal["Dispositivo"]
    norma: str = Field(min_length=1)
    componentes: list[Componente] = Field(min_length=1)
    redacao_dada_por: str | None = None
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
    def _check_endereco(self) -> Self:
        """Reject an address that doesn't nest legally, or a backwards validity window."""
        erros = validar_aninhamento(self.componentes)
        if erros:
            raise ValueError("; ".join(erros))
        if (
            self.vigencia_inicio is not None
            and self.vigencia_fim is not None
            and self.vigencia_fim < self.vigencia_inicio
        ):
            msg = f"vigencia_fim {self.vigencia_fim} precedes vigencia_inicio {self.vigencia_inicio}"
            raise ValueError(msg)
        return self


class Dispositivo(Concept):
    """One authored legal provision, in one wording — an OKF concept doc (P3).

    Unlike achados/regras, the body has no named sections: it is the
    provision's own text preceded by the text of every level above it — the
    readable chain down to this provision, one paragraph per level, each in
    the wording contemporaneous with this one (see ``docs/spec/dispositivo.md``).
    ``texto`` is a domain-named alias for ``body``.

    The chain is **curated by hand** and only its existence is checked here:
    picking each ancestor's contemporaneous wording is a legal reading, not
    something a validator can derive — the same reason achados and the P13.1
    sections are authored rather than generated.
    """

    @property
    def texto(self) -> str:
        """Return the transcribed chain down to this provision."""
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

    @property
    def norma_id(self) -> str:
        """Return the key of the norm this provision belongs to (P4)."""
        if self.contract is not None:
            return self.contract.norma
        return str(self.frontmatter.get("norma") or self.doc_id.split("/")[0])

    @property
    def endereco_id(self) -> str:
        """Return ``<norma>/<endereço>`` — the provision, independent of wording.

        This is the join key that makes "which regras cite art. 40, § 1º, I
        *in any wording*" answerable, and the group a wording-continuity
        check runs over. Read from the path rather than recomputed, so it is
        available even for a doc whose contract failed to validate.
        """
        return self.doc_id.rsplit("/", 1)[0]

    @property
    def redacao_id(self) -> str:
        """Return the wording segment — an amending norm's key, or ``original``."""
        return self.doc_id.rsplit("/", 1)[-1]

    @property
    def rotulo(self) -> str:
        """Return the canonical citation of the address (P4), or the raw slug if invalid."""
        if self.contract is None:
            return self.endereco_id.split("/")[-1]
        return rotulo_do_endereco(self.contract.componentes)

    @property
    def ordem(self) -> tuple[int | str, ...]:
        """Return the legal-order sort key, so § 2º lists before § 14."""
        if self.contract is None:
            return ()
        return chave_de_ordem(self.contract.componentes)


def parse_dispositivo_doc(text: str) -> tuple[dict[str, object], str]:
    """Split a dispositivo doc into its frontmatter dict and the raw body text."""
    try:
        return parse_concept_doc(text)
    except ConceptDocError as exc:
        msg = "dispositivo document must contain YAML frontmatter delimited by ---"
        raise DispositivoValidationError(msg) from exc


def load_dispositivos(bundle_dir: Path) -> list[Dispositivo]:
    """Load every authored dispositivo document, in path order.

    Skips the generated ``index.md`` files and the authored ``norma.md``
    docs (P4, loaded by ``norma_schema.load_normas``). Returns an empty list
    if the bundle directory doesn't exist yet — P3's infrastructure may be
    present before any dispositivo has been authored.
    """
    if not bundle_dir.is_dir():
        return []
    dispositivos = []
    for doc_path in sorted(bundle_dir.rglob("*.md")):
        if doc_path.name in {"index.md", NORMA_DOC}:
            continue
        doc_id = doc_path.relative_to(bundle_dir).with_suffix("").as_posix()
        frontmatter, body = parse_dispositivo_doc(doc_path.read_text(encoding="utf-8"))
        dispositivos.append(
            Dispositivo(doc_id=doc_id, frontmatter=frontmatter, body=body, bundle_dir=bundle_dir)
        )
    return dispositivos


def _check_caminho(dispositivo: Dispositivo, contract: DispositivoFrontmatter) -> list[str]:
    """Return violations where the file's path disagrees with its own frontmatter.

    The path is a *function* of the frontmatter — norm key, derived address
    slug, wording key. Recomputing and comparing is what stops the id from
    silently drifting away from the doc it names, the failure the previous
    hand-composed slug had no defence against.
    """
    erros: list[str] = []
    doc_id = dispositivo.doc_id
    norma_seg, endereco_seg, redacao_seg = doc_id.split("/")

    if contract.norma != norma_seg:
        erros.append(f"{doc_id}: frontmatter norma={contract.norma!r} does not match its directory")

    esperado = slug_do_endereco(contract.componentes)
    if endereco_seg != esperado:
        erros.append(
            f"{doc_id}: address directory {endereco_seg!r} does not match the componentes, "
            f"which derive {esperado!r}"
        )

    esperada = contract.redacao_dada_por or REDACAO_ORIGINAL
    if redacao_seg != esperada:
        erros.append(
            f"{doc_id}: wording file {redacao_seg!r} does not match redacao_dada_por, "
            f"which derives {esperada!r}"
        )
    return erros


def validate_dispositivo(dispositivo: Dispositivo, normas: dict[str, Norma] | None = None) -> list[str]:
    """Return every intra-document P3 violation.

    Reuses ``dispositivo.validation_error`` (cached on first access) instead
    of re-running ``DispositivoFrontmatter.model_validate()``. Pass
    ``normas`` to also resolve the ``norma`` key against the closed P4
    vocabulary; omit it when only the document-local contract is of interest.
    """
    errors: list[str] = []
    doc_id = dispositivo.doc_id

    if DOC_ID_RE.fullmatch(doc_id) is None:
        errors.append(f"{doc_id}: path is not of the form <norma>/<endereço>/<redação>.md")
    if dispositivo.frontmatter.get("id") != doc_id:
        errors.append(f"{doc_id}: frontmatter id={dispositivo.frontmatter.get('id')!r} does not match path")
    if not dispositivo.texto.strip():
        errors.append(f"{doc_id}: body must contain the chain down to the provision (P3), got empty body")

    if dispositivo.validation_error is not None:
        errors.extend(format_pydantic_errors(doc_id, dispositivo.validation_error))
    elif dispositivo.contract is not None and DOC_ID_RE.fullmatch(doc_id) is not None:
        errors.extend(_check_caminho(dispositivo, dispositivo.contract))

    if normas is not None:
        errors.extend(_check_vocabulario(dispositivo, normas))
    return errors


def _check_vocabulario(dispositivo: Dispositivo, normas: dict[str, Norma]) -> list[str]:
    """Return violations where a norm key doesn't resolve to an authored norma doc (P4).

    Both keys are checked: the norm the provision belongs to, and — when the
    wording is not the original — the norm that amended it. An amending norm
    contributes no dispositivo of its own, but it is still what an auditor
    must open to verify the transcription, so it earns a ``norma.md`` with
    its own official URL rather than living on as unchecked prose.
    """
    erros: list[str] = []
    if dispositivo.norma_id not in normas:
        erros.append(
            f"{dispositivo.doc_id}: norma {dispositivo.norma_id!r} has no authored {NORMA_DOC} "
            "(P4 — a citable norm enters the corpus by being authored)"
        )
    redacao = dispositivo.redacao_id
    if redacao != REDACAO_ORIGINAL and redacao not in normas:
        erros.append(
            f"{dispositivo.doc_id}: redacao_dada_por {redacao!r} has no authored {NORMA_DOC} "
            "(P4 — the amending norm is what verifies this wording)"
        )
    return erros


def check_vigencias(dispositivos: list[Dispositivo]) -> list[str]:
    """Return every pair of wordings of the same provision whose validity windows overlap.

    Two wordings of one provision cannot both be in force at the same
    instant, so an overlap is a real contradiction in the transcription. A
    *gap* is deliberately not reported: P3 authors on demand, so a provision
    may legitimately have the EC 41 and EC 103 wordings transcribed and not
    the EC 20 one in between.
    """
    erros: list[str] = []
    grupos: dict[str, list[Dispositivo]] = {}
    for dispositivo in dispositivos:
        if dispositivo.contract is not None:
            grupos.setdefault(dispositivo.endereco_id, []).append(dispositivo)

    for endereco_id, grupo in sorted(grupos.items()):
        janelas = sorted(
            (
                (d.contract.vigencia_inicio or datetime.date.min, d.contract.vigencia_fim, d.doc_id)
                for d in grupo
                if d.contract is not None
            ),
            # Order by start date alone (doc_id breaking the tie). Sorting the
            # whole tuple would compare `vigencia_fim`, which is `None` for the
            # wording still in force — and `None < date` raises, so two wordings
            # sharing a start date (including two with none at all, both read as
            # date.min) would crash the validator instead of being *reported* as
            # the overlap they are.
            key=lambda janela: (janela[0], janela[2]),
        )
        for (_, fim_a, id_a), (inicio_b, _, id_b) in itertools.pairwise(janelas):
            if fim_a is None or fim_a >= inicio_b:
                erros.append(
                    f"{endereco_id}: wordings {id_a!r} and {id_b!r} are both in force on "
                    f"{inicio_b.isoformat()} — a provision has one wording at a time"
                )
    return erros


def validate_bundle_dispositivos(bundle_dir: Path) -> list[str]:
    """Validate every dispositivo and norma doc in the bundle, plus wording continuity."""
    normas = {norma.doc_id: norma for norma in load_normas(bundle_dir)}
    errors: list[str] = []
    for norma in normas.values():
        errors.extend(validate_norma(norma))

    dispositivos = load_dispositivos(bundle_dir)
    for dispositivo in dispositivos:
        errors.extend(validate_dispositivo(dispositivo, normas))
    errors.extend(check_vigencias(dispositivos))
    return errors


def dispositivo_ids(bundle_dir: Path) -> frozenset[str]:
    """Return every currently authored dispositivo's doc_id, for P3 link resolution."""
    return frozenset(d.doc_id for d in load_dispositivos(bundle_dir))


def _linha_do_dispositivo(dispositivo: Dispositivo, base: str) -> str:
    """Render one dispositivo as a norma-index bullet, relative to ``base``."""
    caminho = dispositivo.doc_id.removeprefix(f"{base}/")
    redacao = dispositivo.redacao_id
    sufixo = "redação original" if redacao == REDACAO_ORIGINAL else f"redação dada por {redacao}"
    return f"* [{dispositivo.rotulo}]({caminho}.md) - {sufixo}"


def regenerate_dispositivos_index(bundle_dir: Path) -> None:
    """Regenerate every norma's ``index.md`` plus the bundle-root ``index.md``.

    Entries are listed in **legal order** (``Dispositivo.ordem``), not path
    order — the old index sorted ``art-20-p1, art-20-p14, art-20-p2`` and
    labelled all seven of art. 20's provisions identically "Art. 20",
    because the flat schema had neither a comparable key nor a field holding
    the full address. Both now derive from ``componentes``.

    No-op if the bundle directory doesn't exist yet — P3's infrastructure
    may land before the first dispositivo is authored.
    """
    if not bundle_dir.is_dir():
        return

    normas = {norma.doc_id: norma for norma in load_normas(bundle_dir)}
    por_norma: dict[str, list[Dispositivo]] = {}
    for dispositivo in load_dispositivos(bundle_dir):
        if DOC_ID_RE.fullmatch(dispositivo.doc_id) is None:
            # Malformed path — already reported by validate_dispositivo();
            # skip rather than write into a norma directory that may not
            # exist, or index a doc under a key nothing can resolve.
            continue
        por_norma.setdefault(dispositivo.doc_id.split("/")[0], []).append(dispositivo)

    for norma_id, itens in por_norma.items():
        norma = normas.get(norma_id)
        titulo = norma.nome if norma is not None else norma_id
        itens.sort(key=lambda d: (d.ordem, d.redacao_id))
        linhas = [_linha_do_dispositivo(item, norma_id) for item in itens]
        body = f"# {titulo}\n\n" + "\n".join(linhas) + "\n"
        write_markdown(bundle_dir / norma_id / "index.md", body)

    root_lines = [
        f"* [{normas[norma_id].nome if norma_id in normas else norma_id}]({norma_id}/index.md) - "
        f"{len(por_norma[norma_id])} dispositivo(s)"
        for norma_id in sorted(por_norma)
    ]
    root_fm = yaml.safe_dump({"okf_version": "0.1"}, sort_keys=False)
    root_body = "# Dispositivos legais\n\n" + ("\n".join(root_lines) + "\n" if root_lines else "")
    write_markdown(bundle_dir / "index.md", f"---\n{root_fm}---\n\n{root_body}")
