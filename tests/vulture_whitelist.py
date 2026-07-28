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

Covers Pydantic models only. ``TypedDict`` fields (``relatorio_citacoes``'s
``ResumoDeCitacoes``, ``emit_site_data``'s payloads) stay reported: their
only "use" is a string subscript, which vulture's AST pass does not connect
to the declaration, so a whitelist entry for them would be dead code
pretending to help. Vulture is not a CI gate for exactly this kind of
false positive.

Run: ``uv run vulture scripts/ tests/`` (this file is included via the `tests/`
argument already — nothing extra to pass).
"""

from __future__ import annotations

import datetime

from achado_schema import AchadoFrontmatter
from concept import ConceptFrontmatter
from conjunto_schema import Ato as AtoConjunto
from conjunto_schema import ConjuntoFrontmatter
from dispositivo_endereco import Componente, TipoComponente
from dispositivo_schema import DispositivoFrontmatter
from estado_auditoria import AtoValidacao
from norma_schema import NormaFrontmatter
from substituicao_schema import DecisaoCompletude, GrupoSubstituicao
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
    vigencia_inicio=datetime.date(2026, 1, 1),
    vigencia_fim=datetime.date(2026, 1, 1),
    fontes=["https://example.invalid/lei-teste"],
)
_norma.type
_norma.nome
_norma.apelido
_norma.vigencia_inicio
_norma.vigencia_fim
_norma.fontes

_decisao = DecisaoCompletude(
    decidido_por="x",
    decidido_em=datetime.date(2026, 1, 1),
    justificativa="x",
    fonte="x",
)
_decisao.decidido_por
_decisao.decidido_em
_decisao.justificativa
_decisao.fonte

_ato_conjunto = AtoConjunto(
    tipo="parecer",
    autoridade="pge",
    efeito="valida",
    identificador="x",
    fonte="y",
    data=datetime.date(2026, 1, 1),
)
_ato_conjunto.tipo
_ato_conjunto.autoridade
_ato_conjunto.efeito
_ato_conjunto.identificador
_ato_conjunto.fonte
_ato_conjunto.data
_ato_conjunto.escopo.tipo
_ato_conjunto.escopo.regras

_grupo = GrupoSubstituicao(
    grupo="g",
    origens_legacy=("/regras/regra-0001.md",),
    destinos_auditados=("/regras-auditadas/unidades/a.md",),
)
_grupo.grupo
_grupo.origens_legacy
_grupo.destinos_auditados
_grupo.estado_grupo
_grupo.decisao_completude

_conjunto = ConjuntoFrontmatter(
    type="Conjunto",
    id="catalogo-legado",
    nome="Catálogo legado",
    situacao="vigente",
    origem="catalogo-legado",
)
_conjunto.type
_conjunto.nome
_conjunto.situacao
_conjunto.origem
_conjunto.base
_conjunto.substituicoes
_conjunto.revoga
_conjunto.introduz
_conjunto.autoridade
_conjunto.atos
_conjunto.decisao_completude

_ato = AtoValidacao(tipo="x", autoridade="x", identificador="x", fonte="x")
_ato.autoridade
_ato.identificador
_ato.fonte

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

_taxonomia = TaxonomiaRef(ref="/dispositivos/lei-teste/art-1/original.md", papel="x")
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
