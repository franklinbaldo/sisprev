---
okf_version: '0.1'
---

# Catálogo auditado (RFC 0004)

Bundle OKF separado do catálogo legado (`okf/regras-sisprev/`), com espaço de
identidade próprio (RFC 0004 §1.2). Cada unidade auditada em
[`unidades/`](unidades/index.md) declara `origens_legacy` apontando de volta
para a(s) linha(s) legada(s) de que descende — nunca reutiliza `regra-NNNN`
ou `row_index` como sua própria identidade.

Este bundle pode estar vazio: a infraestrutura (schema, manifesto, gates,
compilador) não exige a criação imediata de nenhuma unidade auditada real.
Nenhuma unidade aqui é operacional enquanto o
[manifesto de substituição](manifesto-substituicao.yaml) não tiver o grupo
correspondente com `estado_grupo: ativo` — o que a Fase 1A nunca faz para
dados reais (ver CLAUDE.md).
