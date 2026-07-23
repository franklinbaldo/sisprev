"""RFC 0004 §4 — the projection-role contract ("papéis de projeção").

Each operational predicate/requisito of an audited unit projects into up to
four declared roles onto the legacy target — never an inferred "single
destination" (RFC 0004 §4.2 explicitly rejects that framing):

- **portador semântico primário** — where the condition stays textually
  expressed (a `fundamentacao*` field, or a structured column like `sexo`).
  Exactly one per operational requisito.
- **efeitos derivados** — the already-precomputed result: `integral`,
  `tipo_calculo`, `paridade`.
- **representação de interface** — `nome`. Never a portador primário nor
  material alone (RFC 0004 §10).
- **suporte jurídico** — `dispositivos:` (P3) and the citation.

This module only holds the *contract* (which fields play which role) — it
never infers a predicate from `nome`/`fundamentacao*` prose (RFC 0004: the
compiler is one-directional, predicate → text, never text → predicate).
"""

from __future__ import annotations

# `dispositivos` is a project-envelope field (P3), not one of the 27
# original CSV columns — kept here as its own name rather than importing
# regra_schema.FRONTMATTER_COLUMNS for a name that isn't in that tuple.
INTERFACE_FIELD = "nome"
EFEITO_DERIVADO_FIELDS = ("integral", "tipo_calculo", "paridade")
SUPORTE_JURIDICO_FIELD = "dispositivos"


def is_fundamentacao_field(campo: str) -> bool:
    """Return whether ``campo`` is one of the three fundamentação carrier fields."""
    return campo in ("fundamentacao", "fundamentacao_proporcional", "fundamentacao_integral")
