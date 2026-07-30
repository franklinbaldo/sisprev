"""P14 — Achado concept: typed schema, doc I/O, and validation (RFC 0001).

Achados are authored Markdown sources. Code may validate their contract and
derive indexes, but never decides their semantic content.
"""

from __future__ import annotations

import datetime
import re
from functools import cached_property
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
from md_format import write_markdown
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


def _coerce_iso_date(value: object) -> datetime.date | None:
    """Return a plain ``date`` for a YAML date/datetime or ISO string, else ``None``.

    ``datetime`` is checked first because it subclasses ``date``: returned
    as-is it would compare against a plain ``date`` and raise ``TypeError``
    instead of answering the question asked.
    """
    if isinstance(value, datetime.datetime):
        return value.date()
    if isinstance(value, datetime.date):
        return value
    if isinstance(value, str):
        try:
            return datetime.date.fromisoformat(value)
        except ValueError:
            return None
    return None


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
    # Três estados, e o terceiro não é uma variação do segundo.
    #
    # `resolvido` afirma que **o defeito existiu e foi tratado**. `improcedente`
    # afirma o contrário na origem: **a acusação não procede** — o defeito
    # descrito não existe, ou não existe do modo como o achado o descreveu.
    # Fechar como `resolvido` um achado equivocado gravaria no catálogo que uma
    # regra teve um problema que ela nunca teve, e essa afirmação sobrevive ao
    # texto do corpo: quem lê o selo não lê a prosa.
    #
    # O estado é necessário porque **id de achado é append-only** — o CI
    # percorre a história inteira e falha em remoção ou renomeação. Um achado
    # equivocado, portanto, não pode sumir; só pode ser marcado. Sem este
    # estado, a única saída era mentir num dos dois selos disponíveis.
    #
    # E é necessário **agora** porque a auditoria decidiu propor a leitura mais
    # provável quando a certa não é reconstruível: uma postura que produz
    # acusação falível por desenho precisa do estado que registra a falha
    # honestamente, em vez de dissolvê-la em "resolvido".
    situacao: Literal["aberto", "resolvido", "improcedente"]
    severidade: Literal["bloqueante", "informativo"]
    verificacao: Literal["mecanica", "manual", "hibrida"]
    natureza: Literal["juridica", "dados", "modelagem", "processo"]
    regras_afetadas: list[str] = Field(min_length=1)
    detectado_em: datetime.date
    detectado_por: str = Field(min_length=1)
    deteccoes: list[Deteccao] = Field(default_factory=list)
    resolvido_em: datetime.date | None = None
    resolvido_por: str | None = None
    # Par próprio, em vez de reusar `resolvido_*`: sobrecarregar aquele par
    # faria "quem resolveu" nomear quem concluiu que não havia o que resolver,
    # e a distinção entre os dois atos é exatamente o que este estado registra.
    improcedente_em: datetime.date | None = None
    improcedente_por: str | None = None
    efeito_deteccao: Literal["deve_desaparecer", "pode_persistir"] | None = None

    @field_validator("detectado_em", "resolvido_em", "improcedente_em", mode="before")
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

    def _check_trilha_de_fechamento(self) -> None:
        """A trilha exigida por um estado terminal, e a proibição da trilha do outro.

        A exclusão mútua é o ponto: um achado que carregue os dois pares de
        datas afirma ao mesmo tempo que o defeito foi tratado e que ele não
        existia, e nenhum leitor tem como saber qual das duas vale.
        """
        exigido, proibido = (
            (("improcedente_em", self.improcedente_em), ("improcedente_por", self.improcedente_por)),
            (("resolvido_em", self.resolvido_em), ("resolvido_por", self.resolvido_por)),
        )
        if self.situacao == "resolvido":
            exigido, proibido = proibido, exigido

        if any(valor for _, valor in proibido):
            nomes = "/".join(nome for nome, _ in proibido)
            msg = f"situacao={self.situacao} forbids {nomes}"
            raise ValueError(msg)
        for nome, valor in exigido:
            if not valor:
                msg = f"situacao={self.situacao} requires {nome}"
                raise ValueError(msg)

        data = exigido[0][1]
        if isinstance(data, datetime.date) and data < self.detectado_em:
            msg = f"{exigido[0][0]} must not be earlier than detectado_em"
            raise ValueError(msg)

    @model_validator(mode="after")
    def _check_resolution_contract(self) -> AchadoFrontmatter:
        """Cada estado exige a sua própria trilha, e proíbe a dos outros."""
        if self.situacao == "aberto":
            if self.resolvido_em or self.resolvido_por or self.efeito_deteccao:
                msg = "situacao=aberto forbids resolution metadata and efeito_deteccao"
                raise ValueError(msg)
            if self.improcedente_em or self.improcedente_por:
                msg = "situacao=aberto forbids improcedência metadata"
                raise ValueError(msg)
            return self

        self._check_trilha_de_fechamento()

        # Vale para os dois estados terminais, e por razões diferentes que
        # levam ao mesmo lugar: um achado resolvido precisa declarar se a
        # detecção que o originou ainda pode reproduzir, e um improcedente
        # **quase sempre** verá a detecção persistir — a ocorrência mecânica
        # continua real, só a conclusão sobre ela é que não procedia. É a
        # separação "detecção ≠ conclusão" aplicada ao fechamento.
        if self.deteccoes and self.efeito_deteccao is None:
            msg = f"{self.situacao} mecanica/hibrida achado requires efeito_deteccao"
            raise ValueError(msg)
        if not self.deteccoes and self.efeito_deteccao is not None:
            msg = "manual achado must not define efeito_deteccao"
            raise ValueError(msg)
        return self


class Achado(Concept):
    """One authored finding — an OKF concept doc (P14).

    Every typed accessor below prefers ``contract`` — the P14 frontmatter
    validated once and cached, not re-parsed from the raw dict per property
    per access — but falls back to an ungated raw-dict read when the doc
    fails *whole-document* validation for an unrelated field. That fallback
    matters: P7/P14's cross-document joins (an achado's ``situacao``/
    ``regras_afetadas`` feeding the bloqueante-achado and bidirectionality
    checks) must still see a real, present ``situacao: aberto`` even from
    an achado that's otherwise incomplete (say, missing ``nome``) —
    "detecção ≠ conclusão" applies to this reader too, not just to achado
    authorship: one malformed field must not blind the join to every other
    field that IS well-formed.
    """

    @cached_property
    def _validation(self) -> AchadoFrontmatter | ValidationError:
        try:
            return AchadoFrontmatter.model_validate(self.frontmatter)
        except ValidationError as exc:
            return exc

    @property
    def contract(self) -> AchadoFrontmatter | None:
        """Return the validated P14 frontmatter contract, or None if malformed."""
        result = self._validation
        return result if isinstance(result, AchadoFrontmatter) else None

    @property
    def validation_error(self) -> ValidationError | None:
        """Return the cached P14 contract ValidationError, or None if the doc is valid."""
        result = self._validation
        return result if isinstance(result, ValidationError) else None

    @property
    def situacao(self) -> str:
        """Return the lifecycle state, or an empty string if malformed."""
        if self.contract is not None:
            return self.contract.situacao
        return str(self.frontmatter.get("situacao") or "")

    @property
    def efeito_deteccao(self) -> str:
        """Return the declared effect of resolution on linked detections."""
        if self.contract is not None:
            return self.contract.efeito_deteccao or ""
        return str(self.frontmatter.get("efeito_deteccao") or "")

    @property
    def regras_afetadas(self) -> list[str]:
        """Return the canonical rule references affected by the finding."""
        if self.contract is not None:
            return self.contract.regras_afetadas
        raw = self.frontmatter.get("regras_afetadas")
        return [str(ref) for ref in raw] if isinstance(raw, list) else []

    @property
    def detection_refs(self) -> list[tuple[str, str]]:
        """Return detector and fingerprint pairs from the finding."""
        if self.contract is not None:
            return [(d.detector, d.fingerprint) for d in self.contract.deteccoes]
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

    @property
    def detectado_em(self) -> datetime.date | None:
        """Return the detection date, or ``None`` when absent or unparseable.

        Exists for the same reason as every accessor above — a caller must
        never read this off the raw dict. YAML types the value by whether the
        author happened to quote it: ``detectado_em: 2026-07-18`` arrives as a
        ``date`` and ``detectado_em: '2026-07-18'`` as a ``str``, and three of
        the 52 achados use the quoted form. A raw ``isinstance(..., date)``
        read therefore skips exactly those three, silently — which is how the
        chronological check on ``corrigida`` came to be a no-op for
        achado-0008/0009/0010 (P7, `docs/spec/regra.md`).

        The fallback parses the ISO string itself, so an achado malformed for
        an unrelated field's sake still yields its date: same
        "detecção ≠ conclusão" reasoning the class docstring gives.
        """
        if self.contract is not None:
            return self.contract.detectado_em
        return _coerce_iso_date(self.frontmatter.get("detectado_em"))

    @property
    def resolvido_em(self) -> datetime.date | None:
        """Return the resolution date, or ``None`` when absent or unparseable.

        Same contract as ``detectado_em``, and it needs the same accessor for
        the same reason: the quoted and unquoted YAML forms both occur in the
        authored corpus, so a raw read would check the pair of dates in one
        document and skip it in the next.
        """
        if self.contract is not None:
            return self.contract.resolvido_em
        return _coerce_iso_date(self.frontmatter.get("resolvido_em"))

    @property
    def improcedente_em(self) -> datetime.date | None:
        """Return the improcedência date, or ``None`` when absent or unparseable."""
        if self.contract is not None:
            return self.contract.improcedente_em
        return _coerce_iso_date(self.frontmatter.get("improcedente_em"))


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
        try:
            frontmatter, body = parse_concept_doc(doc_path.read_text(encoding="utf-8"))
        except ConceptDocError as exc:
            msg = "achado document must contain YAML frontmatter delimited by ---"
            raise AchadoValidationError(msg) from exc
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
    # `# Resolução` é a seção de **fechamento**, seja qual for o desfecho — não
    # se acrescenta um quinto heading para o estado novo, o que obrigaria todo
    # achado a carregar uma seção vazia a mais. Fechar sem escrever por quê é o
    # que o gate impede, e vale igual para "foi tratado" e "não procedia".
    if achado.situacao in ("resolvido", "improcedente") and not achado.sections.get("Resolução", "").strip():
        errors.append(f"{doc_id}: situacao={achado.situacao} requires a non-empty # Resolução section")
    return errors


def _validate_datas_administrativas(achado: Achado, *, today: datetime.date) -> list[str]:
    """Reject a detection or resolution dated ahead of ``today``.

    ``AchadoFrontmatter`` already orders the pair (``resolvido_em >=
    detectado_em``), but ordering alone admits both dates in the future — a
    resolution "signed" next year is ordered consistently and still records
    something that has not happened. It is the same requirement the P7 trail
    already imposes on ``auditado_em`` and, since the #61 decision, on a
    disposição's ``decidido_em``: an administrative date is the date an act
    occurred, and an act does not occur in advance.

    Lives here, not in the Pydantic contract, for the reason that decided
    ``decidido_em``: the model receives no context, so it cannot know "today"
    without reading the clock inside a validator — which would make the
    contract itself untestable at a fixed date. ``today`` is injected instead,
    and read through the typed accessors so both YAML date forms are checked.
    """
    errors: list[str] = []
    for campo, valor in (
        ("detectado_em", achado.detectado_em),
        ("resolvido_em", achado.resolvido_em),
        ("improcedente_em", achado.improcedente_em),
    ):
        if valor is not None and valor > today:
            errors.append(
                f"{achado.doc_id}: {campo}={valor.isoformat()} is in the future (today: {today.isoformat()})",
            )
    return errors


def validate_achado(
    achado: Achado,
    *,
    known_regra_ids: frozenset[str],
    today: datetime.date | None = None,
) -> list[str]:
    """Return every intra-document and contextual P14 violation.

    Reuses ``achado.validation_error`` — cached on first access by any
    caller, including every ``achado.situacao``/``.regras_afetadas``/...
    read above — instead of re-running ``AchadoFrontmatter.model_validate()``.

    ``today`` is injectable so a test fixes the clock; it defaults to the real
    current date, same as ``estado_auditoria.validate_estados``.
    """
    if today is None:
        today = datetime.datetime.now(tz=datetime.UTC).date()
    errors: list[str] = []
    if achado.validation_error is not None:
        errors.extend(format_pydantic_errors(achado.doc_id, achado.validation_error))
    errors.extend(_validate_context(achado, known_regra_ids=known_regra_ids))
    errors.extend(_validate_datas_administrativas(achado, today=today))
    return errors


def validate_bundle_achados(
    bundle_dir: Path,
    *,
    known_regra_ids: frozenset[str],
    today: datetime.date | None = None,
) -> list[str]:
    """Validate all achados and their current-tree sequence."""
    achados = load_achados(bundle_dir)
    errors: list[str] = []
    numbers: list[int] = []

    for achado in achados:
        errors.extend(validate_achado(achado, known_regra_ids=known_regra_ids, today=today))
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
    write_markdown(achados_dir / "index.md", body)
    regenerate_root_index(bundle_dir)


def regenerate_root_index(bundle_dir: Path) -> None:
    """Regenerate the bundle-root index from authored sources."""
    dataset_text = (bundle_dir / "regras-sisprev.md").read_text(encoding="utf-8")
    dataset_fm, _ = parse_concept_doc(dataset_text)
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
    write_markdown(bundle_dir / "index.md", f"---\n{fm_text}---\n\n{body}")


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
    write_markdown(bundle_dir / "achados" / f"{doc_id}.md", build_achado_doc(frontmatter, sections))
    return doc_id
