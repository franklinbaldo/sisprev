---
type: TipoCalculo
id: tipo-calculo-valor-efetivo-mais-70-excedente-teto-rgps
valor: Valor Efetivo mais 70% do que exceder do Teto RGPS
autorado_por: franklinbaldo
autorado_em: 2026-07-31
---

# Estado da análise

Rótulo legado que reúne, na mesma expressão, uma referência de base e um
limitador: até o teto do RGPS preserva-se o valor indicado; sobre a parcela
excedente o texto grava o percentual de 70%.

O rótulo é mais próximo de uma fórmula que os demais membros do enum, mas ainda
não identifica sozinho qual “Valor Efetivo” deve ser usado, a competência do teto,
os critérios de atualização nem eventuais ajustes anteriores.

A decomposição normativa deve separar base e limitador em
`type: FormaCalculo`, com o percentual e os dispositivos de cada componente.
Este conceito existe para preservar exatamente a projeção que o Sisprev aceita.
