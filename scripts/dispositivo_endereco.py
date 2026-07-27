"""P3 — a legal provision's structural address: pure model, slug, label and order.

A dispositivo's address is not a record with four independent attributes
(``artigo``/``paragrafo``/``inciso``/``alinea``) — it is one *ordered path*
through the norm's structure: Art. 40 -> § 1º -> inciso I. Modelling it as
flat optional fields admitted states the domain forbids (an alínea with no
parent inciso), stored typography instead of data (``"Art. 40"``, ``"§ 1º"``,
``"I"`` — three conventions in one record), could not represent ``caput`` at
all, and could not be ordered (``"Art. 10" < "Art. 9º"`` as strings).

This module is the fix, and it is deliberately **pure**: no filesystem, no
document, no frontmatter. It holds the ordered ``Componente`` sequence, the
legal-nesting rules over it, and the three derivations every other layer
needs:

- ``slug_do_endereco`` — the path segment, so a dispositivo's location is a
  *function* of its address rather than a hand-composed convention that
  drifts (see RFC 0001 P3, "identidade derivada");
- ``rotulo_do_endereco`` — the canonical citation ("art. 40, § 1º, inciso
  I"). This is P4's canonical citation format, derived rather than authored;
- ``chave_de_ordem`` — the sort key that puts § 2º before § 14.

Every level carries its own prefix in the slug (``art-``/``par-``/``inc-``/
``al-``/``item-``), so no segment's *level* depends on position or on the
reader's convention — ``art-1-inc-ii-al-a`` says what each part is.
"""

from __future__ import annotations

import itertools
import re
from enum import StrEnum
from typing import TYPE_CHECKING, Self

from pydantic import BaseModel, ConfigDict, model_validator

if TYPE_CHECKING:
    from collections.abc import Sequence


class TipoComponente(StrEnum):
    """The structural levels a Brazilian legal provision is addressed by."""

    ARTIGO = "artigo"
    CAPUT = "caput"
    PARAGRAFO = "paragrafo"
    PARAGRAFO_UNICO = "paragrafo_unico"
    INCISO = "inciso"
    ALINEA = "alinea"
    ITEM = "item"


# The slot each level occupies in an address, outermost first. Componentes
# must appear in strictly increasing slot order; gaps are allowed, and each
# gap is meaningful:
#
#   art. 40, inciso I        -> slots 0, 3   (an inciso of the *caput*)
#   art. 40, § 1º, inciso I  -> slots 0, 1, 3
#   art. 40, § 1º, caput     -> slots 0, 1, 2
#
# CAPUT sits *below* PARAGRAFO rather than beside it, because "caput" names
# the opening text of whatever unit encloses it — an article's caput and a
# paragraph's caput are both real addresses in this bundle.
_SLOT: dict[TipoComponente, int] = {
    TipoComponente.ARTIGO: 0,
    TipoComponente.PARAGRAFO: 1,
    TipoComponente.PARAGRAFO_UNICO: 1,
    TipoComponente.CAPUT: 2,
    TipoComponente.INCISO: 3,
    TipoComponente.ALINEA: 4,
    TipoComponente.ITEM: 5,
}

# Levels whose identity is a value ("Art. 40", "inciso I"); the remaining two
# (caput, parágrafo único) are singular by definition and carry none.
_COM_VALOR = frozenset(
    {
        TipoComponente.ARTIGO,
        TipoComponente.PARAGRAFO,
        TipoComponente.INCISO,
        TipoComponente.ALINEA,
        TipoComponente.ITEM,
    }
)

# Levels numbered with an ordinal suffix in the original text (Art. 6º-A,
# § 1º-A) — the suffix is a *separate* field, never fused into the value, so
# "6º-A" stays sortable as (6, "A") rather than becoming an opaque string.
_COM_SUFIXO = frozenset({TipoComponente.ARTIGO, TipoComponente.PARAGRAFO})

_NUMERO_RE = re.compile(r"^[1-9]\d*$")
_ROMANO_RE = re.compile(r"^[IVXLC]+$")
_ALINEA_RE = re.compile(r"^[a-z]$")
_SUFIXO_RE = re.compile(r"^[A-Z]$")

_SLUG_PREFIXO: dict[TipoComponente, str] = {
    TipoComponente.ARTIGO: "art",
    TipoComponente.PARAGRAFO: "par",
    TipoComponente.INCISO: "inc",
    TipoComponente.ALINEA: "al",
    TipoComponente.ITEM: "item",
}

_ROMANOS: tuple[tuple[str, int], ...] = (
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1),
)

# Ordinal typography follows Brazilian legal drafting: 1º..9º carry the
# ordinal marker, 10 onward are cardinal ("art. 9º" but "art. 10").
_ULTIMO_ORDINAL = 9


class ComponenteInvalidoError(ValueError):
    """Raised when a derivation is asked for a componente it cannot represent."""


class Componente(BaseModel):
    """One level of a provision's address — e.g. ``artigo 40`` or ``inciso I``."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    tipo: TipoComponente
    valor: str | None = None
    sufixo: str | None = None

    @model_validator(mode="after")
    def _check_valor(self) -> Self:
        """Require a well-formed ``valor``/``sufixo`` for exactly the levels that take one."""
        if self.tipo in _COM_VALOR:
            if self.valor is None:
                msg = f"componente {self.tipo.value!r} requires a 'valor'"
                raise ValueError(msg)
            self._check_formato_do_valor()
        elif self.valor is not None:
            msg = f"componente {self.tipo.value!r} is singular and takes no 'valor'"
            raise ValueError(msg)

        if self.sufixo is not None:
            if self.tipo not in _COM_SUFIXO:
                msg = f"componente {self.tipo.value!r} takes no 'sufixo'"
                raise ValueError(msg)
            if _SUFIXO_RE.fullmatch(self.sufixo) is None:
                msg = f"sufixo {self.sufixo!r} must be a single uppercase letter (e.g. 'A' in 'Art. 6º-A')"
                raise ValueError(msg)
        return self

    def _check_formato_do_valor(self) -> None:
        """Reject a ``valor`` whose notation doesn't match its level's numbering."""
        valor = self.valor or ""
        if self.tipo is TipoComponente.INCISO:
            if _ROMANO_RE.fullmatch(valor) is None:
                msg = f"inciso {valor!r} must be an uppercase Roman numeral (I, II, XIV, ...)"
                raise ValueError(msg)
        elif self.tipo is TipoComponente.ALINEA:
            if _ALINEA_RE.fullmatch(valor) is None:
                msg = f"alínea {valor!r} must be a single lowercase letter"
                raise ValueError(msg)
        elif _NUMERO_RE.fullmatch(valor) is None:
            msg = f"{self.tipo.value} {valor!r} must be a positive integer written without punctuation"
            raise ValueError(msg)

    @property
    def slug(self) -> str:
        """Return this level's path segment — always prefixed, so its level is explicit."""
        if self.tipo is TipoComponente.CAPUT:
            return "caput"
        if self.tipo is TipoComponente.PARAGRAFO_UNICO:
            return "par-unico"
        prefixo = _SLUG_PREFIXO[self.tipo]
        valor = (self.valor or "").lower()
        sufixo = (self.sufixo or "").lower()
        return f"{prefixo}-{valor}{sufixo}"

    @property
    def rotulo(self) -> str:
        """Return this level's canonical citation fragment (P4)."""
        if self.tipo is TipoComponente.CAPUT:
            return "caput"
        if self.tipo is TipoComponente.PARAGRAFO_UNICO:
            return "parágrafo único"
        if self.tipo is TipoComponente.INCISO:
            return f"inciso {self.valor}"
        if self.tipo is TipoComponente.ALINEA:
            return f"alínea {self.valor}"
        if self.tipo is TipoComponente.ITEM:
            return f"item {self.valor}"
        numero = _ordinal(int(self.valor or "0"))
        if self.sufixo is not None:
            numero = f"{numero}-{self.sufixo}"
        return f"art. {numero}" if self.tipo is TipoComponente.ARTIGO else f"§ {numero}"

    @property
    def numero(self) -> int:
        """Return the level's value as an integer, for ordering (§ 2º before § 14)."""
        if self.tipo is TipoComponente.INCISO:
            return romano_para_int(self.valor or "")
        if self.tipo is TipoComponente.ALINEA:
            return ord(self.valor or "a") - ord("a") + 1
        if self.valor is None:
            # caput / parágrafo único: singular by definition, so their
            # position comes from their slot alone, never from a number.
            return 1
        return int(self.valor)


def romano_para_int(romano: str) -> int:
    """Convert an uppercase Roman numeral to its integer value.

    Only used for ordering incisos, so it accepts the subtractive forms that
    appear in legal drafting (I..C) and nothing else.
    """
    total = 0
    resto = romano
    for simbolo, valor in _ROMANOS:
        while resto.startswith(simbolo):
            total += valor
            resto = resto[len(simbolo) :]
    if resto:
        msg = f"{romano!r} is not a Roman numeral this module can read"
        raise ComponenteInvalidoError(msg)
    return total


def _ordinal(numero: int) -> str:
    """Render a number in Brazilian legal drafting's ordinal convention (1º..9º, then 10)."""
    return f"{numero}º" if numero <= _ULTIMO_ORDINAL else str(numero)


def validar_aninhamento(componentes: Sequence[Componente]) -> list[str]:
    """Return every legal-nesting violation in an address, as human-readable messages.

    Returns messages rather than raising so the caller can decide: the
    Pydantic contract raises on them (they become ``validation_error``),
    while a reporting caller can list them all at once.
    """
    erros: list[str] = []
    if not componentes:
        return ["address must have at least one componente (the artigo)"]

    if componentes[0].tipo is not TipoComponente.ARTIGO:
        erros.append(f"address must start with an artigo, got {componentes[0].tipo.value!r}")

    tipos = [c.tipo for c in componentes]
    for anterior, atual in itertools.pairwise(componentes):
        if _SLOT[atual.tipo] <= _SLOT[anterior.tipo]:
            erros.append(
                f"{atual.tipo.value!r} cannot nest inside {anterior.tipo.value!r} "
                "(componentes must go from the outermost level inwards)"
            )
        if anterior.tipo is TipoComponente.CAPUT:
            erros.append("'caput' addresses the enclosing unit's opening text, so nothing can nest inside it")

    if TipoComponente.ALINEA in tipos and TipoComponente.INCISO not in tipos:
        erros.append("'alinea' must hang off an 'inciso'")
    if TipoComponente.ITEM in tipos and TipoComponente.ALINEA not in tipos:
        erros.append("'item' must hang off an 'alinea'")
    return erros


def slug_do_endereco(componentes: Sequence[Componente]) -> str:
    """Return the address's path segment — ``art-40-par-1-inc-i``."""
    return "-".join(componente.slug for componente in componentes)


def rotulo_do_endereco(componentes: Sequence[Componente]) -> str:
    """Return the address's canonical citation — ``art. 40, § 1º, inciso I`` (P4)."""
    return ", ".join(componente.rotulo for componente in componentes)


def chave_de_ordem(componentes: Sequence[Componente]) -> tuple[int | str, ...]:
    """Return the address's sort key, so provisions list in the order the norm reads.

    One fixed-width slot per level — ``(artigo, sufixo, parágrafo, sufixo,
    inciso, alínea, item)`` — with ``0`` standing for "this level is not part
    of the address". That zero is what makes the ordering *legal* rather than
    merely lexicographic: an inciso of the caput (parágrafo slot ``0``) sorts
    ahead of § 1º, which is how the article actually reads, while a per-level
    "depth rank" would wrongly place every paragraph before every inciso.

    Comparison is numeric throughout, so § 2º precedes § 14 — the failure the
    old path-string ordering could not avoid.
    """
    slots: dict[int, Componente] = {}
    for componente in componentes:
        slots.setdefault(_SLOT[componente.tipo], componente)

    def numero(slot: int) -> int:
        componente = slots.get(slot)
        return componente.numero if componente is not None else 0

    def sufixo(slot: int) -> str:
        componente = slots.get(slot)
        return (componente.sufixo or "") if componente is not None else ""

    return (
        numero(_SLOT[TipoComponente.ARTIGO]),
        sufixo(_SLOT[TipoComponente.ARTIGO]),
        numero(_SLOT[TipoComponente.PARAGRAFO]),
        sufixo(_SLOT[TipoComponente.PARAGRAFO]),
        numero(_SLOT[TipoComponente.INCISO]),
        numero(_SLOT[TipoComponente.ALINEA]),
        numero(_SLOT[TipoComponente.ITEM]),
        # The caput has no slot of its own — "no inciso" already sorts it
        # ahead of its unit's incisos. It only needs to be *distinguished*
        # from the whole-unit address, which is what this final segment does,
        # making the key a total order rather than one with ties.
        slug_do_endereco(componentes),
    )
