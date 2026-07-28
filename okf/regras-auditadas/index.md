---
okf_version: '0.1'
---

# Catálogo auditado (RFC 0004)

Bundle OKF separado do catálogo legado (`okf/regras-sisprev/`), com espaço de
identidade próprio (RFC 0004 §1.2). Cada unidade auditada em
[`unidades/`](unidades/index.md) declara `origens_legacy` apontando de volta
para a(s) linha(s) legada(s) de que descende — nunca reutiliza `regra-NNNN`
ou `row_index` como sua própria identidade.

Este bundle pode estar vazio: a infraestrutura (schema, gates, compilador)
não exige a criação imediata de nenhuma unidade auditada real. Nenhuma
unidade aqui é operacional enquanto o grupo de substituição correspondente,
declarado em `okf/conjuntos/` (RFC 0006, `Conjunto.substituicoes`), não
tiver `estado_grupo: ativo` num conjunto `vigente` — o que nenhum conjunto
real faz ainda (ver CLAUDE.md).
