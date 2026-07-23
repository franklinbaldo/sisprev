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
from dispositivo_schema import DispositivoFrontmatter
from estado_auditoria import AtoValidacao
from manifesto_substituicao import DecisaoCompletude
from unidade_auditada_schema import (
    DatasLegadas,
    DecisaoAuditoria,
    ProtocoloVerificacao,
    Proveniencia,
    TaxonomiaRef,
    UnidadeAuditadaFrontmatter,
)

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

_dispositivo = DispositivoFrontmatter(
    type="Dispositivo",
    id="lei-teste/art-1",
    norma="x",
    artigo="x",
    paragrafo="x",
    inciso="x",
    alinea="x",
    redacao_dada_por="x",
    vigencia_inicio=datetime.date(2026, 1, 1),
    vigencia_fim=datetime.date(2026, 1, 1),
    fonte="x",
)
_dispositivo.type
_dispositivo.artigo
_dispositivo.paragrafo
_dispositivo.inciso
_dispositivo.alinea
_dispositivo.redacao_dada_por
_dispositivo.vigencia_inicio
_dispositivo.vigencia_fim
_dispositivo.fonte

_ato = AtoValidacao(tipo="x", autoridade="x", identificador="x", fonte="x")
_ato.autoridade
_ato.identificador
_ato.fonte

_decisao_completude = DecisaoCompletude(
    decidido_por="x", decidido_em="2026-01-01", justificativa="x", fonte="x"
)
_decisao_completude.decidido_por
_decisao_completude.decidido_em
_decisao_completude.justificativa

_protocolo = ProtocoloVerificacao(
    pergunta="x", responsavel="x", meio_de_prova="x", momento="x", evidencia_exigida="x"
)
_protocolo.pergunta

_datas_legadas = DatasLegadas(
    data_adm_apos="x", data_adm_ate="x", data_direito_apos="x", data_direito_ate="x"
)
_datas_legadas.data_adm_apos
_datas_legadas.data_adm_ate
_datas_legadas.data_direito_apos
_datas_legadas.data_direito_ate

_taxonomia = TaxonomiaRef(ref="/dispositivos/lei-teste/art-1.md", papel="x")
_taxonomia.papel

_proveniencia = Proveniencia(fontes_consultadas=["x"], notas="x")
_proveniencia.notas

_decisao_auditoria = DecisaoAuditoria(data="2026-01-01", quem="x", o_que="x")
_decisao_auditoria.data
_decisao_auditoria.quem
_decisao_auditoria.o_que

_unidade_frontmatter = UnidadeAuditadaFrontmatter(
    type="UnidadeAuditada",
    id="x-x",
    schema_version=1,
    estado_unidade="elaboracao",
    origens_legacy=["regra-0001"],
    decisoes=[_decisao_auditoria],
    confianca="alta",
)
_unidade_frontmatter.decisoes
_unidade_frontmatter.confianca
