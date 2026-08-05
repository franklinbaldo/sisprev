---
okf_version: '0.1'
---

# Catálogo proposto (RFC 0004)

Bundle OKF separado do catálogo legado (`okf/regras-sisprev/`), com espaço de
identidade próprio (RFC 0004 §1.2). Cada regra proposta em
[`unidades/`](unidades/index.md) declara `origens_legacy` apontando de volta
para a(s) linha(s) legada(s) de que descende — nunca reutiliza `regra-NNNN`
ou `row_index` como sua própria identidade.

O bundle admite unidades em `elaboracao`, `preview` e `concluida`
(`estado_auditoria`); o [`índice de regras propostas`](unidades/index.md)
mostra o estado atual. Nenhuma regra proposta aqui é operacional enquanto o
componente do grafo origem↔destino a que pertence — calculado por
`scripts/derivar.py` a partir de `origens_legacy` de todas as unidades do
mesmo `ciclo` — não tiver todos os membros `estado_auditoria: concluida` e
`estado_implantacao: confirmada` (`okf/spec/regraproposta.md`, "Atomicidade
é derivada, não declarada").
