---
type: Regra
id: regra-0010
row_index: 10
id_sisprev: '59'
nome: Pensão · óbito a partir de 31/12/2003 e antes de 31/12/2024, ingresso até 31/12/2003 · integral · Valor Efetivo mais 70% do que exceder do Teto RGPS · paridade
tipo_de_beneficio: PENSÃO POR MORTE
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 1º
validado_pge: 'FALSE'
validado_presidencia: 'FALSE'
simulavel: N
tipo: CIVIL
apos_especial: N
tipo_remun: ''
paridade: S
tabelapontuacao: N
requisitos_da_in_no_5_2020: N
relatorio_p_reserva_remunerada_por_idade_ex_officio: N
adicional_inatividade: N
data_adm_ate: 31/12/2003 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2024 00:00
data_direito_apos: 31/12/2003 00:00
fundamentacao_proporcional: art. 40 § 7º II da CF 88 C/C art. 6º-A § -unico da EC nº 41 com redação EC nº 70/12
visivel_dtc_proporcional: N
fundamentacao_integral: art. 40 § 7º I da CF 88 C/C art. 6º-A § -unico da EC nº 41 com redação EC nº 70/12
visivel_dtc_integral: N
sexo: AMBOS
integral: S
tipo_calculo: Valor Efetivo mais 70% do que exceder do Teto RGPS
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-7-inc-i/ec-41-2003.md
  - /dispositivos/cf88/art-40-par-7-inc-ii/ec-41-2003.md
  - /dispositivos/ec-41-2003/art-6a/ec-70-2012.md
---

# Estado da análise

Pensão por morte derivada da aposentadoria por invalidez do art. 6º-A da EC
41/2003, na redação da EC 70/2012. O instituidor tinha de ter ingressado no
serviço público até a publicação da EC 41/2003 (31/12/2003) e ter-se aposentado
por invalidez permanente; a pensão herda dele o cálculo pela remuneração do
cargo efetivo e o critério de revisão do art. 7º da EC 41/2003.

Três valores foram conferidos contra o texto e batem. `data_adm_ate: 31/12/2003`
é exatamente o corte de ingresso do art. 6º-A ("até a data de publicação desta
Emenda Constitucional"). `paridade: S` decorre do parágrafo único do art. 6º-A,
que manda aplicar o art. 7º da EC 41/2003 "observando-se igual critério de
revisão às pensões derivadas". E `tipo_calculo: Valor Efetivo mais 70% do que exceder do Teto RGPS` é a fórmula literal do § 7º do art. 40 — "até o limite
máximo estabelecido para os benefícios do regime geral (...), acrescido de
setenta por cento da parcela excedente a este limite".

Uma dúvida de mapeamento, que não é defeito provado: os incisos I e II do § 7º
se distinguem por o servidor estar **aposentado** (I) ou **em atividade** (II)
na data do óbito, e não por proventos integrais ou proporcionais. A regra
carrega o inciso I na `fundamentacao_integral` e o II na
`fundamentacao_proporcional`, o que não é a distinção que a norma faz — as duas
hipóteses do § 7º pagam a mesma coisa. Como o art. 6º-A pressupõe instituidor
**aposentado** por invalidez, a hipótese do inciso II talvez não devesse estar
aqui. Não converti em achado por não saber como o Sisprev usa o par
proporcional/integral em pensão, e é isso que o item aberto registra.

- [x] `data_adm_ate: 31/12/2003` conferido contra o corte de ingresso do art. 6º-A da EC 41/2003 (texto transcrito em `okf/dispositivos/ec-41-2003/art-6a/ec-70-2012.md`)
- [x] `paridade: S` conferido: o § único do art. 6º-A remete ao art. 7º da EC 41/2003 e estende o critério de revisão às pensões derivadas
- [x] `tipo_calculo` conferido palavra por palavra contra a fórmula do art. 40, § 7º da CF na redação da EC 41/2003
- [x] `dispositivos:` conferido contra `fundamentacao_integral` e `fundamentacao_proporcional`: os três vínculos correspondem ao que os campos citam, nada a acrescentar nem a remover
- [ ] `data_direito_ate: 31/12/2024` é o prazo do art. 4º da ECE 146/2021, que esta regra cita **apenas no `nome`** — nenhum campo de fundamentação o carrega ([`achado-0047`](../achados/achado-0047.md)). Decisão do dono do campo
- [ ] A janela `[31/12/2003, 31/12/2024)` ultrapassa em cinco anos o fim da redação citada do art. 40, § 7º (12/11/2019). Só o resguardo do art. 4º da ECE 146/2021 legitima isso, e ele não está na fundamentação — mesma pendência do item acima, e é o que a torna material
- [ ] O inciso II do § 7º (óbito **em atividade**) na `fundamentacao_proporcional` de uma regra fundada no art. 6º-A, que pressupõe instituidor aposentado. Depende de saber o que o par proporcional/integral significa em pensão por morte no Sisprev (Q6)
