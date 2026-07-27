"""Vulture whitelist for this repo's Pydantic ``*Frontmatter``/``AtoValidacao`` contracts.

These classes are validate-only (see ``achado_schema.validate_achado``,
``dispositivo_schema.validate_dispositivo``, ``estado_auditoria.check_p7_estados``'s
``RegraAuditoriaContrato`` usage): ``Model.model_validate(frontmatter)`` is called
purely for its side effect (raise ``ValidationError`` on a malformed dict) — the
validated instance's fields are, by design, never read back via attribute access
anywhere else in this codebase. Vulture has no notion of Pydantic's declarative
field syntax, so it reports every one of these fields as an "unused variable".

Real instances + real attribute access (not vulture's own bare-name
``--make-whitelist`` stub format) so a future field rename breaks this file's
imports/construction too — ``ty check``/``ruff check`` catch drift here instead
of the whitelist silently going stale. Not executed by vulture (it only parses
this file's AST), but kept genuinely valid so the project's other tools stay
useful on it.

Run: ``uv run vulture scripts/ tests/`` (this file is included via the `tests/`
argument already — nothing extra to pass).
"""

from __future__ import annotations

import datetime

from achado_schema import AchadoFrontmatter
from concept import ConceptFrontmatter
from dispositivo_endereco import Componente, TipoComponente
from dispositivo_schema import DispositivoFrontmatter
from estado_auditoria import AtoValidacao
from norma_schema import NormaFrontmatter

_concept = ConceptFrontmatter(type="Concept", id="x")
_concept.type
_concept.id

_achado = AchadoFrontmatter(
    type="Achado",
    id="achado-0001",
    nome="x",
    situacao="aberto",
    severidade="informativo",
    verificacao="manual",
    natureza="dados",
    regras_afetadas=["/regras/regra-0001.md"],
    detectado_em=datetime.date(2026, 1, 1),
    detectado_por="x",
)
_achado.type
_achado.severidade
_achado.natureza
_achado.detectado_por

_componente = Componente(tipo=TipoComponente.ARTIGO, valor="1", sufixo="A")
_componente.tipo
_componente.valor
_componente.sufixo

_dispositivo = DispositivoFrontmatter(
    type="Dispositivo",
    id="lei-teste/art-1/original",
    norma="lei-teste",
    componentes=[Componente(tipo=TipoComponente.ARTIGO, valor="1")],
    redacao_dada_por=None,
    vigencia_inicio=datetime.date(2026, 1, 1),
    vigencia_fim=datetime.date(2026, 1, 1),
    fontes=["https://example.invalid/lei-teste"],
)
_dispositivo.type
_dispositivo.componentes
_dispositivo.redacao_dada_por
_dispositivo.vigencia_inicio
_dispositivo.vigencia_fim
_dispositivo.fontes

_norma = NormaFrontmatter(
    type="Norma",
    id="lei-teste",
    nome="Lei de Teste nº 1/2026",
    apelido="Lei 1/2026",
    fontes=["https://example.invalid/lei-teste"],
)
_norma.type
_norma.nome
_norma.apelido
_norma.fontes

_ato = AtoValidacao(tipo="x", autoridade="x", identificador="x", fonte="x")
_ato.autoridade
_ato.identificador
_ato.fonte
