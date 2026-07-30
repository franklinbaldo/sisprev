---
type: Regra
id: regra-0103
row_index: 103
nome: Voluntária · Magistério · ingresso até 31/12/2003, requisitos a partir de 31/12/2003 e antes de 31/12/2024 · Masculino · integral · paridade · Remuneração de Contribuição
tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 4º
validado_pge: 'FALSE'
validado_presidencia: 'FALSE'
simulavel: S
tipo: CIVIL
apos_especial: S
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
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria especial de professor, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 6º da Emenda Constitucional nº 41/2003, artigos 24, 46 e 63 da Lei Complementar nº 432/2008, artigo 4º da Emenda à Constituição Estadual nº 146/2021 e artigo 40, § 1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019 - fundamento - especial de professor - regra transitória - EC 41/03
visivel_dtc_integral: N
sexo: MASCULINO
integral: S
tipo_calculo: Remuneração de Contribuição
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ec-41-2003/art-6/original.md
  - /dispositivos/ece-146-2021/art-4/original.md
  - /dispositivos/lce-432-2008/art-24/original.md
  - /dispositivos/lce-432-2008/art-46/original.md
  - /dispositivos/lce-432-2008/art-63/original.md
---

# Estado da análise

Ramo masculino da transição do art. 6º da EC 41/2003 **na hipótese do
magistério**, e é o par mais bem fundamentado dos onze que esta rodada
conferiu. `regra-0104` é o ramo feminino; `regra-0101`/`0102` são as gêmeas não
especiais.

O que a distingue é que a norma estadual está citada e vinculada, e os três
artigos da LCE 432/2008 fecham exatamente as três pontas que faltam às gêmeas:

- **art. 46** é o espelho estadual do art. 6º da EC 41/2003, e é a "lei" a que
  o *caput* daquele artigo remete ao dizer "na forma da lei". Grava os mesmos
  requisitos, verbatim: 60/55 anos de idade, 35/30 de contribuição, 20 anos de
  efetivo exercício no serviço público, 10 de carreira e 5 no cargo, com o corte
  de ingresso "até 31 de dezembro de 2003" — que é o valor de `data_adm_ate` — e
  proventos correspondentes "à totalidade da remuneração do servidor no cargo
  efetivo", que é `integral: S` + `tipo_calculo: Remuneração de Contribuição`;
- **art. 63** funda `paridade: S` **positivamente**, e é o que as gêmeas
  `0101`/`0102` não têm: "será assegurado o reajustamento, na mesma proporção e
  na mesma data, sempre que se modificar a remuneração dos servidores em
  atividade". O art. 46, § 1º remete a ele nominalmente;
- **art. 24** funda `apos_especial: S`: "O professor que comprove,
  exclusivamente, tempo de efetivo exercício das funções de magistério [...]
  terá os requisitos de idade e de tempo de contribuição reduzidos em 5 (cinco)
  anos" — que é a redução que o *caput* do art. 6º ressalva por remissão ao § 5º
  do art. 40 da CF, aqui exercida pela lei estadual. O art. 46 também o cita.

Citar a LCE 432/2008, revogada em 18/10/2021, para uma regra cuja janela vai até
31/12/2024 **não é anacronismo**: é exatamente o que o art. 4º da ECE 146/2021 —
também citado e vinculado — manda fazer, ao preservar "os requisitos e os
critérios exigidos pela legislação vigente até a data de entrada em vigor desta
Emenda Constitucional [14/09/2021], desde que sejam cumpridos até 31 de dezembro
de 2024". A LCE 432/2008 estava em vigor naquela data.

- [x] Critérios do cadastro percorridos um a um contra o art. 6º da EC 41/2003 (publicação do Planalto arquivada, `planalto-emc41.htm`, cp1252) e contra os arts. 24, 46 e 63 da LCE 432/2008 (compilação DITEL arquivada, `ditel-LC432-COMPILADA-REVOGADA.txt`)
- [x] `dispositivos:` conferido item a item contra `fundamentacao_integral`: os seis vínculos correspondem às seis provisões citadas, nada a acrescentar nem a remover
- [x] `data_adm_ate: 31/12/2003` conferido **duas vezes**: no *caput* do art. 6º (data de publicação da emenda) e no *caput* do art. 46 da LCE 432/2008, que grava a data em letra
- [x] `data_direito_apos: 31/12/2003` (vigência da EC 41/2003) e `data_direito_ate: 31/12/2024` (prazo verbatim do art. 4º da ECE 146/2021) conferidos
- [x] `paridade: S` fundado positivamente no art. 63 da LCE 432/2008, citado e vinculado — sem depender do parágrafo único revogado do art. 6º nem do art. 2º da EC 47/2005
- [x] `integral: S` e `tipo_calculo: Remuneração de Contribuição` conferidos contra "totalidade da remuneração do servidor no cargo efetivo" (arts. 6º e 46)
- [x] `apos_especial: S` fundado no art. 24 da LCE 432/2008, que nomeia o professor e a redução de 5 anos
- [x] `sexo: MASCULINO` fundado nos incisos I e II do art. 46 (60 anos, 35 de contribuição), reduzidos em 5 pelo art. 24
- [x] Citação de norma revogada conferida contra o art. 4º da ECE 146/2021: a preservação da legislação vigente até 14/09/2021 é o que a autoriza
- [ ] Idade, tempo de contribuição, tempo de serviço público, carreira, cargo e a redução de 5 anos **não têm coluna**: os números 60/55, 35/30 e a redução do magistério não são conferíveis contra o cadastro (Q5)
- [ ] Vigência do art. 6º da EC 41/2003 depois de 13/11/2019 em aberto: art. 35 da EC 103/2019 o revoga, art. 36, II condiciona a revogação, nos RPPS estaduais, a lei estadual de referendo. `ec-41-2003/art-6/original` sem janela declarada; conclusão jurídica, não tomada aqui
- [ ] `ec-41-2003/art-6/original` transcreve só o *caput*: os quatro incisos estão fora do corpus. Aqui o dano é menor, porque o art. 46 estadual está transcrito com os incisos e grava os mesmos números
- [ ] `cf88/art-40-par-5` (a redução constitucional do magistério, a que o *caput* do art. 6º remete) não é citado nem vinculado: a especialidade fecha pela norma estadual, e a constitucional fica implícita na remissão
