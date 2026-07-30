---
type: Regra
id: regra-0028
row_index: 28
nome: Por idade · requisitos a partir de 31/12/2003 e antes de 31/12/2024 · Masculino · proporcional · Proporcionalidade Dias
tipo_de_beneficio: APOSENTADORIA POR IDADE
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 2º
validado_pge: 'FALSE'
validado_presidencia: 'FALSE'
simulavel: S
tipo: CIVIL
apos_especial: N
tipo_remun: ''
paridade: N
tabelapontuacao: N
requisitos_da_in_no_5_2020: N
relatorio_p_reserva_remunerada_por_idade_ex_officio: N
adicional_inatividade: N
data_adm_ate: 31/12/2099 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2024 00:00
data_direito_apos: 31/12/2003 00:00
fundamentacao_proporcional: Artigo 40, § 1º, inciso II da Constituição Federal, com redação dada pela Emenda Constitucional nº 41/2003, artigos 17, 45 e 62 da Lei Complementar Estadual nº 432/2008 e art. 1º Lei nº 10.887/2004
visivel_dtc_proporcional: N
fundamentacao_integral: ''
visivel_dtc_integral: N
sexo: MASCULINO
integral: N
tipo_calculo: Proporcionalidade Dias
fundamentacao: ''
dispositivos:
  - /dispositivos/lce-432-2008/art-17/original.md
  - /dispositivos/lce-432-2008/art-45/lce-672-2012.md
  - /dispositivos/lce-432-2008/art-62/original.md
  - /dispositivos/lei-10887-2004/art-1/original.md
---

# Estado da análise

Aposentadoria por idade (voluntária) sob o art. 40, § 1º, II da Constituição Federal com a redação dada pela **EC 41/2003**, com base de cálculo de média aritmética simples (Proporcionalidade Dias). A regra não inclui paridade (`paridade: N`), alinhado aos ditames pós-EC 41/2003. A regra é `simulavel: S`.

**A janela temporal extrapola a vigência do dispositivo citado.** Como apontado no [`achado-0014`](../achados/achado-0014.md), embora o marco inicial `data_direito_apos: 31/12/2003` case perfeitamente com a data de início da EC 41/2003, o limite superior `data_direito_ate: 31/12/2024` ultrapassa a vida útil da redação invocada. A redação original do art. 40, § 1º, II pela EC 41/2003 vigorou até 07/05/2015, véspera da entrada em vigor da EC 88/2015. A regra prossegue no tempo, sem referenciar as emendas subsequentes que alteraram a redação. O valor 31/12/2024 remete, possivelmente, aos resguardos do art. 4º da ECE 146/2021, mas o catálogo perde a resolução de transição legal temporal de compulsória para a idade dos 75 anos introduzidos em 2015.

Nenhum dispositivo da CF/88 consta do campo `dispositivos:` (a despeito de ser citado na `fundamentacao_proporcional`). As referências estão restritas à LCE 432/2008 e Lei 10.887/2004 (referente à base de cálculo), gerando omissão na ligação estrutural à EC 41/2003.

- [x] O marco limite inferior `data_direito_apos: 31/12/2003` casa exatamente com a data inicial da redação da EC 41/2003 referenciada na `fundamentacao_proporcional`
- [ ] O limite superior `data_direito_ate: 31/12/2024` extrapola a vigência do artigo referenciado (cuja alteração ocorreu via EC 88/2015 em 08/05/2015), incorrendo no problema pontuado pelo [`achado-0014`](../achados/achado-0014.md)
- [ ] A fundamentação menciona a CF/88 (art. 40, § 1º, II, EC 41/2003), mas este dispositivo falta na lista YAML em `dispositivos:`
- [x] `tipo_calculo: Proporcionalidade Dias` está de acordo com o princípio da média estipulado na lei para a época sem paridade
