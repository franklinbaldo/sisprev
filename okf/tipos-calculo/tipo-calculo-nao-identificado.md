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
conhecimento jurídico. Uma fórmula pode estar identificada e decomposta em
`type: FormaCalculo` e ainda não possuir rótulo que a represente no enum. A
`forma-calculo-totalidade-proporcional-tempo` é o caso canônico: a base e o
ajuste são conhecidos, mas a combinação não cabe em nenhum dos rótulos
existentes.

O conceito, por isso, não deve ser interpretado como fórmula desconhecida, valor
nulo ou autorização para escolher outro membro por aproximação.
