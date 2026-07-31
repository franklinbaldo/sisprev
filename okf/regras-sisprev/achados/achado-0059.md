---
type: Achado
id: achado-0059
nome: regras 0061 a 0064 fundamentam deficiência com integralidade e paridade, mas gravam média e sem paridade
situacao: aberto
severidade: bloqueante
verificacao: manual
natureza: juridica
regras_afetadas:
  - /regras/regra-0061.md
  - /regras/regra-0062.md
  - /regras/regra-0063.md
  - /regras/regra-0064.md
detectado_em: 2026-07-31
detectado_por: franklinbaldo
---

# Descrição

As regras `0061`–`0064` são aposentadorias voluntárias de servidor com
deficiência, posteriores à vigência da LCE 1.100/2021. Todas vinculam o art. 25
(totalidade da remuneração no cargo efetivo) e o art. 27, I (paridade), e a
`fundamentacao_integral` de cada uma afirma expressamente **proventos integrais
por integralidade e com paridade**.

Apesar disso, as quatro regras gravam:

| regras        | `integral` | `paridade` | `tipo_calculo` |
| ------------- | ---------- | ---------- | -------------- |
| `0061`–`0064` | `S`        | `N`        | `Valor Médio`  |

O art. 24, que fundamentaria média e reajuste pelo RGPS, não está entre os
dispositivos vinculados. Portanto, a contradição não é uma diferença de rótulo:
os dispositivos e o texto da regra apontam um regime, enquanto os campos que o
motor usa apontam outro.

# Evidências

Os quatro arquivos repetem a mesma combinação jurídica: `dispositivos:` contém
`lce-1100-2021/art-25`, `lce-1100-2021/art-27-inc-i` e o inciso do art. 35 que
classifica o grau de deficiência; `fundamentacao_integral` diz “proventos
integrais (cálculo por integralidade) e com paridade”. Nenhum dos quatro vincula
o art. 24 ou o art. 27, II, que seriam a base legal para média e reajuste pelo
RGPS.

O conflito, portanto, é comum às quatro regras e independente do grau ou sexo:
os campos materiais divergem dos dispositivos que cada regra declara.

# Consequência

As regras são `simulavel: S`. A combinação `Valor Médio` + `paridade: N` pode
produzir benefício menor e reajuste diferente daquele descrito nos arts. 25 e
27, I. A escolha entre corrigir os campos ou corrigir a fundamentação é decisão
de produto e de interpretação do catálogo; esta auditoria não a toma.

# Limites

Este achado não afirma que `Valor Efetivo` ou `Remuneração de Contribuição` seja
o enum correto para o art. 25. Também não resolve os requisitos de deficiência,
os dez anos de serviço público e os cinco anos no cargo, que não têm colunas
próprias. Ele registra somente a contradição objetiva entre a lei/fundamentação
e os campos deployáveis.

# Questão a investigar

1. Os arts. 25 e 27, I são realmente o regime aplicável às quatro regras?
2. Se sim, qual membro do enum executa a totalidade da remuneração?
3. Se não, quais dispositivos de média e RGPS devem substituir os atuais?
4. Onde o catálogo deve aferir o grau de deficiência e os requisitos gerais?
