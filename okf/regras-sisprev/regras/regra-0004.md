---
type: Regra
id: regra-0004
row_index: 4
nome: INVÁLIDA · Invalidez · ingresso até 31/12/2003, requisitos a partir de 16/12/1998 e antes de 31/12/2003 · paridade
tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
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
data_adm_apos: 01/01/1910 00:00
data_direito_ate: 31/12/2003 00:00
data_direito_apos: 16/12/1998 00:00
fundamentacao_proporcional: Art 40, §1º, I, da CF com redação da EC 20/98
visivel_dtc_proporcional: N
fundamentacao_integral: Art 40, §1º, I, da CF com redação da EC 20/98
visivel_dtc_integral: N
sexo: ''
integral: ''
tipo_calculo: Não identificado
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-i/ec-20-1998.md
---

# Estado da análise

Aposentadoria por invalidez sob o **art. 40, § 1º, I da CF/88 na redação da EC 20/1998**. A regra prevê `paridade: S`, o que é coerente com o regime anterior à EC 41/2003. O registro é `simulavel: N`, indicando que a determinação do enquadramento exige leitura e triagem humana.

**A janela temporal está correta e coerente com as fronteiras de redação.** `data_direito_apos: 16/12/1998` é exatamente a data de vigência da EC 20/1998 (conferida em fonte oficial). O fim da janela `data_direito_ate: 31/12/2003` é o marco de publicação da EC 41/2003. Conforme apontado no `achado-0015`, esta regra segue a convenção dominante de intervalo semiaberto `[apos, ate)` para representar a vigência de redações: abre no primeiro dia da EC 20/1998 e fecha no primeiro dia da EC 41/2003, encaixando com o fecho da `regra-0001` (15/12/1998) de forma ininterrupta.

Itens de verificação não expressos no cadastro da regra: o laudo pericial atestando a invalidez permanente; se a aposentadoria será com proventos integrais, o enquadramento em acidente em serviço, moléstia profissional ou doença grave (que o dispositivo delega a definição em lei); e se for com proventos proporcionais, a aferição da proporção correta com base no tempo de contribuição.

- [x] A fronteira inicial `data_direito_apos: 16/12/1998` corresponde à entrada em vigor da EC 20/1998
- [x] A fronteira final `data_direito_ate: 31/12/2003` corresponde à entrada em vigor da EC 41/2003
- [x] `dispositivos:` confere perfeitamente com a fundamentação textual. A redação da EC 20/1998 para o art. 40, § 1º, I está corretamente transcrita e vinculada
- [ ] Campos estruturais como `sexo`, `integral` vazios e `tipo_calculo` igual a `Não identificado`. Isso é apontado pelo [`achado-0008`](../achados/achado-0008.md) como pendência de preenchimento
- [ ] Falta vinculação do dispositivo legal, na esfera estadual, que define o rol de doenças graves e moléstias profissionais citado pelo inciso I transcrito
