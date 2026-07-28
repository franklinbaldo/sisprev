"""P15 — ``type: Conjunto``: composições do catálogo, historicamente situadas (RFC 0006).

Editar uma regra na auditoria é destrutivo: o estado anterior sobrevive em
``data/raw/`` (que é a importação, não estados intermediários) e no git (que
não é registro consultável). Não havia como o catálogo dizer *"esta é a regra
em vigor, e esta é a que a PGE propõe no lugar dela"*.

Um **conjunto** é o objeto que diz isso: uma composição do catálogo sobre a
qual uma autoridade se pronuncia de uma vez. Ele **não lista** suas regras —
carrega **deltas explícitos** sobre a sua base, e a pertinência é derivada
(:func:`resolve`). Listar seria abrir espaço para a lista divergir do que
existe em disco, em silêncio.

Duas escolhas que parecem detalhe e não são:

- **Os deltas ficam no conjunto, não nas regras.** Uma revogação pura não tem
  documento sucessor onde se pendurar; e manter o conjunto fora dos documentos
  históricos é o que faz a fase 0 ser um no-op *demonstrável* — o frontmatter
  das 112 regras não muda, então a chave material do P2 fica intocada por
  construção, não por argumento (RFC 0006 §7).
- **O grupo de substituição é declarado, nunca descoberto.** Seria possível
  juntar as unidades que apontam para a mesma origem, mas o sistema não tem
  como saber que faltava escrever uma terceira descendente. Completude é
  decisão humana; inferida do que está em disco, seria verdadeira por
  construção e não checaria nada.

``GrupoSubstituicao`` reproduz deliberadamente o contrato já validado pela
Fase 1A da RFC 0004 (``manifesto_substituicao.GrupoSubstituicao``, na branch
``feat/rfc-0004-fase-1a-catalogo-auditado``): mesmos campos, mesma semântica.
Quando as duas linhas se encontrarem, os dois modelos viram um só — os grupos
mudam de moradia (do YAML global para o conjunto), não de schema. É dívida
declarada, não fork silencioso.
"""

from __future__ import annotations

import datetime
import re
from functools import cached_property
from typing import TYPE_CHECKING, Literal, Self

from concept import Concept, ConceptFrontmatter, format_pydantic_errors, parse_concept_doc
from detections import Violation
from md_format import write_markdown
from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator, model_validator

if TYPE_CHECKING:
    from collections.abc import Iterable, Sequence
    from pathlib import Path

CONJUNTO_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def _parse_iso_date(value: object) -> object:
    """Accept YAML dates or strict ISO date strings — same rule as dispositivo/norma."""
    if value is None or isinstance(value, datetime.date):
        return value
    if isinstance(value, str):
        return datetime.date.fromisoformat(value)
    return value


class DecisaoCompletude(BaseModel):
    """A decisão humana de que um conjunto está completo o bastante para vigorar."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    decidido_por: str = Field(min_length=1)
    decidido_em: datetime.date
    justificativa: str = Field(min_length=1)
    fonte: str = Field(min_length=1)

    _check_data = field_validator("decidido_em", mode="before")(_parse_iso_date)


class EscopoAto(BaseModel):
    """O alcance de um ato institucional.

    ``tipo: regras`` é **forma reservada**: o schema a aceita para não exigir
    mudança incompatível depois, mas :func:`validate_conjunto` a recusa
    enquanto não houver caso real de validação parcial. Até lá, validação
    parcial é *um conjunto menor* — um conceito fazendo um trabalho.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    tipo: Literal["conjunto", "regras"] = "conjunto"
    regras: tuple[str, ...] = ()


class Ato(BaseModel):
    """Um ato institucional praticado sobre o conjunto.

    ``efeito`` é o que separa "há um ato da PGE" de "a PGE validou": um ofício
    que apenas encaminha uma proposta não sustenta uma validação. Quais
    efeitos e quais fontes valem institucionalmente é a Q12 da RFC 0001, que
    segue aberta — este campo deixa a pergunta aberta com a estrutura pronta.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    tipo: str = Field(min_length=1)
    autoridade: str = Field(min_length=1)
    efeito: Literal["valida", "encaminha", "devolve", "arquiva"]
    identificador: str = Field(min_length=1)
    fonte: str = Field(min_length=1)
    data: datetime.date | None = None
    escopo: EscopoAto = EscopoAto()

    _check_data = field_validator("data", mode="before")(_parse_iso_date)


class GrupoSubstituicao(BaseModel):
    """Um grupo atômico de substituição — ativa e reverte inteiro (RFC 0004 §1.4).

    ``origens_legacy`` e ``destinos_auditados`` são listas não vazias, o que
    cobre 1:N (decomposição) e N:1 (consolidação) e **exclui** substituição
    sem sucessora ou introdução sem antecessora — para essas o conjunto tem
    ``revoga`` e ``introduz``.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    grupo: str = Field(min_length=1)
    origens_legacy: tuple[str, ...] = Field(min_length=1)
    destinos_auditados: tuple[str, ...] = Field(min_length=1)
    estado_grupo: Literal["inativo", "ativo"] = "inativo"
    decisao_completude: DecisaoCompletude | None = None

    @model_validator(mode="after")
    def _check_ativacao(self) -> Self:
        """Ativação exige a decisão humana registrada (RFC 0004 §1.4)."""
        if self.estado_grupo == "ativo" and self.decisao_completude is None:
            msg = "estado_grupo='ativo' requires decisao_completude"
            raise ValueError(msg)
        return self


class ConjuntoFrontmatter(ConceptFrontmatter):
    """Contrato tipado de ``type: Conjunto`` (P15)."""

    type: Literal["Conjunto"]
    nome: str = Field(min_length=1)
    situacao: Literal["proposto", "vigente", "superado", "arquivado"]
    # A raiz declara de onde vem o seu conteúdo em vez de uma base. Único
    # valor hoje: o bundle legado de 112 regras, como já vinha sendo operado.
    origem: Literal["catalogo-legado"] | None = None
    base: str | None = None
    substituicoes: tuple[GrupoSubstituicao, ...] = ()
    revoga: tuple[str, ...] = ()
    introduz: tuple[str, ...] = ()
    autoridade: str | None = None
    atos: tuple[Ato, ...] = ()
    decisao_completude: DecisaoCompletude | None = None

    @model_validator(mode="after")
    def _check_raiz(self) -> Self:
        """Ou é raiz (tem ``origem``) ou deriva de outro (tem ``base``) — nunca ambos."""
        if (self.origem is None) == (self.base is None):
            msg = "a conjunto declares exactly one of 'origem' (root) or 'base' (derived)"
            raise ValueError(msg)
        return self


class Conjunto(Concept):
    """Uma composição autorada do catálogo — um concept doc OKF (P15)."""

    @cached_property
    def _validation(self) -> ConjuntoFrontmatter | ValidationError:
        try:
            return ConjuntoFrontmatter.model_validate(self.frontmatter)
        except ValidationError as exc:
            return exc

    @property
    def contract(self) -> ConjuntoFrontmatter | None:
        """Return the validated P15 contract, or None if the frontmatter is malformed."""
        result = self._validation
        return result if isinstance(result, ConjuntoFrontmatter) else None

    @property
    def validation_error(self) -> ValidationError | None:
        """Return the cached contract ValidationError, or None if the doc is valid."""
        result = self._validation
        return result if isinstance(result, ValidationError) else None

    @property
    def nome(self) -> str:
        """Return the set's citable name, with the ungated raw fallback the others use."""
        if self.contract is not None:
            return self.contract.nome
        return str(self.frontmatter.get("nome") or self.doc_id)

    @property
    def situacao(self) -> str:
        """Return the lifecycle state, falling back to an ungated raw read.

        Same reason as ``Achado.situacao``: a doc invalid for an unrelated
        field's sake must still be countable as vigente/proposto, or the
        cross-document checks lose the very field they exist to join on.
        """
        if self.contract is not None:
            return self.contract.situacao
        return str(self.frontmatter.get("situacao") or "")

    @property
    def eh_raiz(self) -> bool:
        """Whether this is the bootstrap root — it declares an origem, not a base."""
        if self.contract is not None:
            return self.contract.origem is not None
        return bool(self.frontmatter.get("origem")) and not self.frontmatter.get("base")


def load_conjuntos(bundle_dir: Path) -> list[Conjunto]:
    """Load every authored conjunto doc, in path order.

    Returns an empty list when the directory doesn't exist: the P15
    infrastructure may be present before any conjunto is authored, and every
    check below treats "no conjuntos" as "not migrated yet", never as a
    violation.
    """
    if not bundle_dir.is_dir():
        return []
    conjuntos = []
    for doc_path in sorted(bundle_dir.glob("*.md")):
        if doc_path.name == "index.md":
            continue
        frontmatter, body = parse_concept_doc(doc_path.read_text(encoding="utf-8"))
        conjuntos.append(
            Conjunto(
                doc_id=doc_path.stem,
                frontmatter=frontmatter,
                body=body,
                bundle_dir=bundle_dir,
            )
        )
    return conjuntos


def conjuntos_por_id(conjuntos: Iterable[Conjunto]) -> dict[str, Conjunto]:
    """Index authored conjuntos by their doc id."""
    return {conjunto.doc_id: conjunto for conjunto in conjuntos}


def conjunto_vigente(conjuntos: Iterable[Conjunto]) -> Conjunto | None:
    """Return the single conjunto in force, or None when there isn't exactly one.

    Returning None for *both* "none" and "several" is deliberate: the caller
    that needs the catalog cannot pick one, and the caller that reports the
    problem is :func:`validate_conjuntos`, which sees the whole list.
    """
    vigentes = [conjunto for conjunto in conjuntos if conjunto.situacao == "vigente"]
    return vigentes[0] if len(vigentes) == 1 else None


class ResolucaoError(Exception):
    """Raised when a conjunto's membership cannot be computed (missing/cyclic base)."""


def resolve(
    conjunto_id: str,
    por_id: dict[str, Conjunto],
    catalogo_legado: Sequence[str],
) -> tuple[str, ...]:
    """Compute a conjunto's membership: the base, minus its deltas, plus its own.

    Returns OKF links, sorted — the catalog is heterogeneous (legacy
    ``/regras/regra-NNNN.md`` and audited units), so a link is the one
    representation both sides share.

    Raises :class:`ResolucaoError` on a missing or cyclic base rather than
    returning a partial answer: membership that silently drops a whole base is
    worse than no answer, because every downstream check would read it as "the
    catalog shrank".
    """
    return tuple(sorted(_resolve(conjunto_id, por_id, catalogo_legado, visitados=())))


def _resolve(
    conjunto_id: str,
    por_id: dict[str, Conjunto],
    catalogo_legado: Sequence[str],
    *,
    visitados: tuple[str, ...],
) -> set[str]:
    if conjunto_id in visitados:
        ciclo = " -> ".join([*visitados, conjunto_id])
        msg = f"cyclic base chain: {ciclo}"
        raise ResolucaoError(msg)
    conjunto = por_id.get(conjunto_id)
    if conjunto is None:
        msg = f"unknown conjunto {conjunto_id!r}"
        raise ResolucaoError(msg)
    contrato = conjunto.contract
    if contrato is None:
        msg = f"{conjunto_id}: frontmatter does not satisfy the Conjunto contract"
        raise ResolucaoError(msg)

    if contrato.base is None:
        membros = set(catalogo_legado)
    else:
        membros = _resolve(
            contrato.base,
            por_id,
            catalogo_legado,
            visitados=(*visitados, conjunto_id),
        )

    for grupo in contrato.substituicoes:
        membros -= set(grupo.origens_legacy)
        membros |= set(grupo.destinos_auditados)
    membros -= set(contrato.revoga)
    return membros | set(contrato.introduz)


def _erros_de_contrato(conjunto: Conjunto) -> list[Violation]:
    erros: list[Violation] = []
    doc_id = conjunto.doc_id
    if CONJUNTO_ID_RE.fullmatch(doc_id) is None:
        erros.append(Violation("P15_CONJUNTO_INVALIDO", f"{doc_id}: id is not lowercase/digits/hyphens"))
    if conjunto.frontmatter.get("id") != doc_id:
        erros.append(
            Violation(
                "P15_CONJUNTO_INVALIDO",
                f"{doc_id}: frontmatter id={conjunto.frontmatter.get('id')!r} does not match the filename",
            )
        )
    if conjunto.validation_error is not None:
        erros.extend(
            Violation("P15_CONJUNTO_INVALIDO", mensagem)
            for mensagem in format_pydantic_errors(doc_id, conjunto.validation_error)
        )
    return erros


def _erros_de_vigencia(conjunto: Conjunto) -> list[Violation]:
    """Checks that only apply to a conjunto in force — with the root exempted.

    ``decisao_completude`` and an activating act are required of whoever
    *transitions* from proposto to vigente. The root did not transition: it
    records a pre-existing operational state. Demanding both of it would
    manufacture a fictional institutional decision, signed by nobody, purely
    to satisfy the schema (RFC 0006 §6.1).
    """
    contrato = conjunto.contract
    if contrato is None or contrato.situacao != "vigente" or conjunto.eh_raiz:
        return []
    erros: list[Violation] = []
    if contrato.decisao_completude is None:
        erros.append(
            Violation(
                "P15_VIGENTE_SEM_DECISAO",
                f"{conjunto.doc_id}: situacao=vigente requires decisao_completude (non-root)",
            )
        )
    if not any(ato.efeito == "valida" for ato in contrato.atos):
        erros.append(
            Violation(
                "P15_VIGENTE_SEM_ATO",
                f"{conjunto.doc_id}: situacao=vigente requires an ato with efeito='valida'",
            )
        )
    return erros


def validate_conjunto(conjunto: Conjunto) -> list[Violation]:
    """Return every intra-document P15 violation for one conjunto doc."""
    erros = _erros_de_contrato(conjunto)
    contrato = conjunto.contract
    if contrato is not None:
        erros.extend(
            Violation(
                "P15_ESCOPO_NAO_SUPORTADO",
                f"{conjunto.doc_id}: ato escopo tipo='regras' is reserved but not yet supported",
            )
            for ato in contrato.atos
            if ato.escopo.tipo != "conjunto"
        )
    return erros + _erros_de_vigencia(conjunto)


def validate_conjuntos(conjuntos: Sequence[Conjunto], catalogo_legado: Sequence[str]) -> list[Violation]:
    """Return every P15 violation across the authored conjuntos.

    An empty bundle is **not** a violation: before the P15 migration there are
    no conjuntos, and reporting "no vigente" then would fail every synthetic
    bundle in the test suite for a state that is simply pre-migration.
    """
    if not conjuntos:
        return []

    erros: list[Violation] = []
    for conjunto in conjuntos:
        erros.extend(validate_conjunto(conjunto))

    vigentes = [c.doc_id for c in conjuntos if c.situacao == "vigente"]
    if not vigentes:
        erros.append(
            Violation("P15_VIGENTE_AUSENTE", "no conjunto is 'vigente' — the catalog has no current state")
        )
    elif len(vigentes) > 1:
        erros.append(
            Violation("P15_VIGENTE_MULTIPLO", f"more than one conjunto is 'vigente': {sorted(vigentes)}")
        )

    por_id = conjuntos_por_id(conjuntos)
    for conjunto in conjuntos:
        erros.extend(_erros_de_deltas(conjunto, por_id, catalogo_legado))
    return erros


def _erros_de_deltas(
    conjunto: Conjunto,
    por_id: dict[str, Conjunto],
    catalogo_legado: Sequence[str],
) -> list[Violation]:
    contrato = conjunto.contract
    if contrato is None:
        return []
    doc_id = conjunto.doc_id
    erros: list[Violation] = []

    if contrato.base is not None and contrato.base not in por_id:
        return [
            Violation("P15_BASE_INEXISTENTE", f"{doc_id}: base={contrato.base!r} is not an authored conjunto")
        ]

    try:
        base = set(resolve(contrato.base, por_id, catalogo_legado)) if contrato.base else set(catalogo_legado)
    except ResolucaoError as exc:
        return [Violation("P15_BASE_CICLICA", f"{doc_id}: {exc}")]

    alvos: dict[str, int] = {}
    for grupo in contrato.substituicoes:
        for origem in grupo.origens_legacy:
            alvos[origem] = alvos.get(origem, 0) + 1
    for revogada in contrato.revoga:
        alvos[revogada] = alvos.get(revogada, 0) + 1

    erros.extend(
        Violation("P15_ALVO_DUPLO", f"{doc_id}: {alvo} is targeted {n} times (substituted and/or revoked)")
        for alvo, n in sorted(alvos.items())
        if n > 1
    )
    erros.extend(
        Violation("P15_ALVO_FORA_DA_BASE", f"{doc_id}: {alvo} is not in the resolved base")
        for alvo in sorted(alvos)
        if alvo not in base
    )
    return erros


def regenerate_conjuntos_index(bundle_dir: Path) -> None:
    """Regenerate ``okf/conjuntos/index.md`` — a derived listing, never authored.

    No-op if the directory doesn't exist: the P15 infrastructure may land
    before the first conjunto is authored.
    """
    if not bundle_dir.is_dir():
        return
    conjuntos = load_conjuntos(bundle_dir)
    linhas = [
        f"* [{conjunto.nome}]({conjunto.doc_id}.md) - {conjunto.situacao or 'situacao ausente'}"
        for conjunto in sorted(conjuntos, key=lambda c: c.doc_id)
    ]
    corpo = "# Conjuntos de regras\n\n" + ("\n".join(linhas) + "\n" if linhas else "")
    write_markdown(bundle_dir / "index.md", corpo)
