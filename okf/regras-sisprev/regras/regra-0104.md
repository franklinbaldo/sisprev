---
type: Regra
id: regra-0104
row_index: 104
nome: Voluntária por Tempo de Contribuição - Art. 6º da EC 41/03 c/c art. 4º da EC nº 146/21 (Magistério)
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
sexo: FEMININO
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

Ramo feminino da transição do art. 6º da EC 41/2003 na hipótese do magistério,
divergindo da `regra-0103` **apenas em `sexo`**. Os números do ramo feminino
saem dos mesmos dois lugares: 55 anos de idade e 30 de contribuição pelos
incisos I e II do art. 46 da LCE 432/2008 (que espelham os do art. 6º),
reduzidos em cinco pelo art. 24 da mesma lei — logo 50 anos de idade e 25 de
contribuição, exigido o exercício exclusivo em funções de magistério. Os
incisos III e IV (20 anos de serviço público, 10 de carreira, 5 no cargo) não
distinguem sexo.

Como no par masculino, os três artigos estaduais citados fecham as três pontas:
o art. 46 é a lei a que o "na forma da lei" do art. 6º remete e grava o corte de
ingresso "até 31 de dezembro de 2003" que é o valor de `data_adm_ate`; o art. 63
funda `paridade: S` positivamente, dispensando o parágrafo único revogado do
art. 6º; o art. 24 funda `apos_especial: S`. E citar a LCE 432/2008, revogada em
18/10/2021, numa regra cuja janela vai a 31/12/2024 é o que o art. 4º da ECE
146/2021 — citado e vinculado — manda fazer.

- [x] Critérios do cadastro percorridos um a um contra o art. 6º da EC 41/2003 (publicação do Planalto arquivada, cp1252) e contra os arts. 24, 46 e 63 da LCE 432/2008 (compilação DITEL arquivada)
- [x] `dispositivos:` conferido item a item contra `fundamentacao_integral`: os seis vínculos correspondem às seis provisões citadas, nada a acrescentar nem a remover
- [x] `sexo: FEMININO` fundado nos incisos I e II do art. 46 (55 anos, 30 de contribuição), reduzidos em 5 pelo art. 24 — 50 e 25 no resultado
- [x] `data_adm_ate: 31/12/2003` conferido no *caput* do art. 6º e, em letra, no *caput* do art. 46 da LCE 432/2008
- [x] `data_direito_apos: 31/12/2003` e `data_direito_ate: 31/12/2024` conferidos contra a vigência da EC 41/2003 e o prazo verbatim do art. 4º da ECE 146/2021
- [x] `paridade: S` fundado positivamente no art. 63 da LCE 432/2008, citado e vinculado
- [x] `integral: S` e `tipo_calculo: Remuneração de Contribuição` conferidos contra "totalidade da remuneração do servidor no cargo efetivo"
- [x] `apos_especial: S` fundado no art. 24 da LCE 432/2008
- [x] Citação de norma revogada conferida contra o art. 4º da ECE 146/2021
- [ ] Idade, tempo de contribuição, serviço público, carreira, cargo e a redução de 5 anos não têm coluna: os números não são conferíveis contra o cadastro (Q5)
- [ ] Vigência do art. 6º da EC 41/2003 depois de 13/11/2019 em aberto (art. 36, II da EC 103/2019); `ec-41-2003/art-6/original` sem janela declarada
- [ ] `ec-41-2003/art-6/original` transcreve só o *caput*; o art. 46 estadual supre, transcrito com os incisos
- [ ] `cf88/art-40-par-5` não é citado nem vinculado: a especialidade fecha pela norma estadual, e a constitucional fica implícita na remissão do *caput* do art. 6º
