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

Covers Pydantic models only. ``TypedDict`` fields (``emit_site_data``'s
payloads) stay reported: their
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
from forma_calculo_schema import Ajuste, Base, FormaCalculoFrontmatter, Limitador, ProjecaoSisprev
from norma_schema import NormaFrontmatter
from regra_schema import DisposicaoDeAchado, Precedente
from substituicao_schema import DecisaoCompletude, GrupoSubstituicao
from unidade_auditada_schema import (
    DatasLegadas,
    DecisaoAuditoria,
    Predicados,
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

# Precedente (RFC 0010 §6.1) — caso em que a regra foi aplicada, nunca um ato
# que a valide. `parecer` e `observacao` são opcionais e por ora não têm
# leitor em Python (quem os exibe é o site), então o vulture os reporta.
_precedente = Precedente(identificador="x", fonte="x", parecer="x", observacao="x")
_precedente.identificador
_precedente.fonte
_precedente.parecer
_precedente.observacao

# DisposicaoDeAchado — a resposta da regra a um achado que já a nomeia. Só
# `achado` tem leitor em Python: o gate do P7 usa a referência para reconciliar
# a relação. `justificativa` e a trilha são lidos por humanos e pelo site, e o
# gate **não** julga se a razão escrita é boa — decidir se uma disposição é
# legítima é mérito, e a linha que o CI não cruza. Mas `disposicao` e
# `decisao_pendente_de` **são** interpretados desde 2026-07-30: qual das três
# foi escolhida decide o que ela libera num achado bloqueante.
_disposicao = DisposicaoDeAchado(
    achado="/achados/achado-0001.md",
    disposicao="encaminhada",
    justificativa="x",
    decidido_por="x",
    decidido_em=datetime.date(2026, 7, 29),
    decisao_pendente_de="dono_do_campo",
)
_disposicao.achado
_disposicao.disposicao
_disposicao.justificativa
_disposicao.decidido_por
_disposicao.decidido_em
_disposicao.decisao_pendente_de

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

_predicados = Predicados(faixa_exposicao="66-pontos-15-anos")
_predicados.faixa_exposicao

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


# FormaCalculo (P16) — `percentual_excedente` é o número que o enum não carrega
# (o limitador do art. 40, § 7º paga 70% do que excede o teto do RGPS), e quem
# o consome hoje é o leitor humano e o código do corpo do documento, não Python.
_ref_par_3 = "/dispositivos/cf88/art-40-par-3/ec-20-1998.md"
_forma = FormaCalculoFrontmatter(
    type="FormaCalculo",
    id="forma-calculo-exemplo",
    nome="x",
    base=Base(tipo="totalidade_remuneracao_cargo_efetivo", dispositivos=[_ref_par_3]),
    ajustes=[Ajuste(tipo="proporcional_tempo_contribuicao", dispositivos=[_ref_par_3])],
    limitadores=[
        Limitador(
            tipo="teto_rgps_mais_percentual_do_excedente",
            percentual_excedente=70.0,
            dispositivos=[_ref_par_3],
        )
    ],
    projecao_sisprev=ProjecaoSisprev(tipo_calculo="Valor Efetivo", fidelidade="exata"),
    autorado_por="x",
    autorado_em=datetime.date(2026, 7, 30),
)
_forma.nome
_forma.base.tipo
_forma.ajustes
_forma.limitadores[0].tipo
_forma.limitadores[0].percentual_excedente
_forma.base.dispositivos
_forma.projecao_sisprev.tipo_calculo
_forma.projecao_sisprev.fidelidade
_forma.projecao_sisprev.justificativa
_forma.autorado_por
_forma.autorado_em
