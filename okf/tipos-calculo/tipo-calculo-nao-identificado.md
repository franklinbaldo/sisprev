---
type: TipoCalculo
id: tipo-calculo-nao-identificado
valor: Não identificado
autorado_por: franklinbaldo
autorado_em: 2026-07-31
---

# Estado da análise

Rótulo legado usado quando o Sisprev não registra, no campo `tipo_calculo`, um
membro mais específico do enum.

Ele descreve o estado da **projeção no sistema**, não necessariamente o estado do
conhecimento jurídico. Um `TipoCalculo` pode ter fórmula (`base`/`ajustes`/
`limitadores`) integralmente derivada e ainda não ter, no catálogo legado, um
`origem_legada.tipo_calculo` que o represente sem ambiguidade — nesse caso o
documento próprio da fórmula registra essa lacuna em
`origem_legada.fidelidade`, e este rótulo (`Não identificado`) permanece
reservado para as regras cuja fórmula ainda não foi decomposta.

O conceito, por isso, não deve ser interpretado como fórmula desconhecida, valor
nulo ou autorização para escolher outro membro por aproximação.
