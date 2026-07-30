---
type: Regra
id: regra-0101
row_index: 101
nome: Voluntária · ingresso até 31/12/2003, requisitos a partir de 31/12/2003 e antes de 31/12/2024 · Masculino · integral · paridade · Remuneração de Contribuição
tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 4º
validado_pge: 'FALSE'
validado_presidencia: 'FALSE'
simulavel: S
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
data_direito_ate: 31/12/2024 00:00
data_direito_apos: 31/12/2003 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria voluntária por idade e tempo de contribuição, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 40, § 1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019, artigo 4º da Emenda à Constituição Estadual nº 146/2021 e artigo 6º da Emenda Constitucional nº 41/2003 - fundamento - regra de transição - EC 41/03 - CF
visivel_dtc_integral: N
sexo: MASCULINO
integral: S
tipo_calculo: Remuneração de Contribuição
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ec-41-2003/art-6/original.md
  - /dispositivos/ece-146-2021/art-4/original.md
---

# Estado da análise

Ramo masculino da transição do art. 6º da EC 41/2003 — integralidade e
paridade para quem ingressou no serviço público até a publicação da emenda —,
preservada pelo art. 4º da ECE 146/2021 para requisitos cumpridos até
31/12/2024. `regra-0102` é o ramo feminino e `regra-0103`/`0104` são as gêmeas
de magistério.

**Os campos de resultado e as janelas conferem, um a um, contra o texto do
art. 6º.** `data_adm_ate: 31/12/2003` é a data de publicação da EC 41/2003, que
é o corte que o *caput* fixa ("que tenha ingressado no serviço público até a
data de publicação desta Emenda"); `integral: S` e `tipo_calculo: Remuneração de Contribuição` correspondem a "proventos integrais, que corresponderão à
totalidade da remuneração do servidor no cargo efetivo";
`data_direito_apos: 31/12/2003` é a vigência da emenda e `data_direito_ate: 31/12/2024` o prazo verbatim do art. 4º da ECE 146/2021. `apos_especial: N` é
correto — a redução do magistério que o *caput* ressalva ("observadas as
reduções [...] contidas no § 5º do art. 40") é o que separa `0103`/`0104`
desta.

`paridade: S` está **certo, e a norma que o funda não é citada por esta regra**.
O parágrafo único do art. 6º, que trazia a paridade, foi **revogado** pelo art.
5º da EC 47/2005 — e a nota de revogação consta da publicação compilada. Quem
funda positivamente é o **art. 2º da EC 47/2005**: "Aplica-se aos proventos de
aposentadorias dos servidores públicos que se aposentarem na forma do caput do
art. 6º da Emenda Constitucional nº 41, de 2003, o disposto no art. 7º da mesma
Emenda". Esse artigo não é citado pela fundamentação, não está autorado no
bundle, e é o único caminho positivo até a paridade desta regra. É o mesmo modo
de falha que §5.3 da
[lista consolidada](../../../docs/analysis/achados-candidatos-da-conferencia.md)
registra no art. 6º-A: o *caput* vinculado só afasta normas, e quem manda
aplicar a paridade está em outro dispositivo.

Segunda lacuna, na mesma direção: o art. 6º manda pagar a totalidade da
remuneração "**na forma da lei**", e a lei estadual que dá essa forma é o art.
46 da LCE 432/2008 — que as gêmeas de magistério `0103`/`0104` citam e vinculam,
com os mesmos 60/55, 35/30, 20 anos de serviço público e 10 de carreira + 5 no
cargo, e com o reajuste do art. 63. Esta regra não cita norma estadual nenhuma.

- [x] Critérios do cadastro percorridos um a um contra o art. 6º da EC 41/2003, lido na publicação do Planalto arquivada localmente (`planalto-emc41.htm`, sha256 `af74d433…`, cp1252)
- [x] `dispositivos:` conferido item a item contra `fundamentacao_integral`: os três vínculos correspondem às três provisões citadas, nada a acrescentar nem a remover
- [x] `data_adm_ate: 31/12/2003` conferido contra o *caput* do art. 6º e a data de publicação da EC 41/2003
- [x] `data_direito_apos: 31/12/2003` e `data_direito_ate: 31/12/2024` conferidos contra a vigência da EC 41/2003 e o art. 4º da ECE 146/2021
- [x] `integral: S` e `tipo_calculo: Remuneração de Contribuição` conferidos contra "proventos integrais [...] totalidade da remuneração do servidor no cargo efetivo"
- [x] `apos_especial: N` correto: a redução do magistério que o *caput* ressalva é o que individua `regra-0103`/`0104`
- [x] `sexo: MASCULINO` fundado nos incisos I e II do art. 6º: 60 anos e 35 de contribuição, contra 55 e 30 do ramo feminino
- [ ] `paridade: S` não tem, na fundamentação desta regra, dispositivo que o funde positivamente: o parágrafo único do art. 6º foi revogado pelo art. 5º da EC 47/2005, e quem manda aplicar o art. 7º da EC 41/2003 é o **art. 2º da EC 47/2005**, não citado e não autorado no bundle
- [ ] O "na forma da lei" do art. 6º não é preenchido: o art. 46 da LCE 432/2008, que as gêmeas de magistério citam, não aparece aqui
- [ ] Idade, tempo de contribuição, tempo de serviço público, tempo de carreira e tempo no cargo **não têm coluna**: a diferença 60/55 e 35/30 que a lei manda não é conferível contra o cadastro (Q5)
- [ ] Vigência do art. 6º da EC 41/2003 depois de 13/11/2019 em aberto: o art. 35 da EC 103/2019 o revoga e o art. 36, II condiciona a revogação, nos RPPS estaduais, a lei estadual de referendo. `ec-41-2003/art-6/original` segue sem janela declarada; conclusão jurídica, não tomada aqui
- [ ] `ec-41-2003/art-6/original` transcreve só o *caput*: os quatro incisos com os requisitos estão fora do corpus (fila `TRANSCREVER`, §5.3 da lista consolidada)
- [ ] `data_adm_apos: 01/01/1910` é sentinela inferior sem correspondência normativa, e o catálogo usa dois valores para o mesmo papel (20 regras com 01/01/1910, 79 com 01/01/1950). Cosmético, mas é valor gravado
