---
type: Regra
id: regra-0106
row_index: 106
nome: Voluntária por Tempo de Contribuição - Art. 3º da EC 47/05 - FÓRMULA 85/95, c/c art. 4º da EC nº 146/2021
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
data_adm_ate: 16/12/1998 00:00
data_adm_apos: 01/01/1910 00:00
data_direito_ate: 31/12/2024 00:00
data_direito_apos: 31/12/2003 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria voluntária por idade e tempo de contribuição, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 40, § 1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019, artigo 4º da Emenda à Constituição Estadual nº 146/2021 e artigo 3º da Emenda Constitucional nº 47/2005.- fundamento - regra de transição - EC 47/05 - comum- CF
visivel_dtc_integral: N
sexo: FEMININO
integral: S
tipo_calculo: Remuneração de Contribuição
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ec-47-2005/art-3/original.md
  - /dispositivos/ece-146-2021/art-4/original.md
---

# Estado da análise

Ramo feminino da transição do art. 3º da EC 47/2005, divergindo da
`regra-0105` **apenas em `sexo`**. Os números do ramo feminino: 30 anos de
contribuição pelo inciso I (contra 35), e idade mínima resultante da redução de
um ano por cada ano de contribuição que exceder esses 30, aplicada sobre os 55
anos da alínea "a" do art. 40, § 1º, III da CF — daí o "85" da fórmula do
`nome` (55 + 30). O inciso II — 25 anos de efetivo exercício no serviço público,
15 de carreira e 5 no cargo — não distingue sexo.

`data_adm_ate: 16/12/1998` é o corte que o *caput* do art. 3º grava em letra.
`data_direito_apos: 31/12/2003` é correto e a razão não é óbvia: o art. 6º da EC
47/2005 lhe dá "efeitos retroativos à data de vigência da Emenda Constitucional
nº 41, de 2003" — o valor gravado é o marco da retroatividade, não o da
publicação (06/07/2005). `data_direito_ate: 31/12/2024` é o prazo verbatim do
art. 4º da ECE 146/2021.

`paridade: S` está fundado no parágrafo único do art. 3º, que manda aplicar o
art. 7º da EC 41/2003; o documento existe (`ec-47-2005/art-3-par-unico/original`)
e não é vinculado, embora a citação "artigo 3º" o alcance. `integral: S` e
`tipo_calculo: Remuneração de Contribuição` correspondem a "proventos integrais".
`apos_especial: N` é correto.

E falta a mesma peça do par masculino: a alínea "a" do art. 40, § 1º, III, que é
o minuendo da fórmula, não é citada nem vinculada.

- [x] Critérios do cadastro percorridos um a um contra o art. 3º da EC 47/2005, lido na publicação do Planalto arquivada localmente (`planalto-emc47.htm`, sha256 `408a9df8…`, cp1252)
- [x] `dispositivos:` conferido item a item contra `fundamentacao_integral`: as três provisões citadas têm vínculo
- [x] `sexo: FEMININO` fundado: 30 anos de contribuição pelo inciso I e idade de referência de 55 anos pela alínea "a", contra 35 e 60 do ramo masculino
- [x] `data_adm_ate: 16/12/1998` conferido contra o *caput* do art. 3º, que grava a data em letra
- [x] `data_direito_apos: 31/12/2003` conferido contra o art. 6º da EC 47/2005 (efeitos retroativos à vigência da EC 41/2003)
- [x] `data_direito_ate: 31/12/2024` conferido contra o art. 4º da ECE 146/2021
- [x] `integral: S` e `tipo_calculo: Remuneração de Contribuição` conferidos contra "proventos integrais" do *caput*
- [x] `paridade: S` fundado positivamente no parágrafo único do art. 3º
- [x] `apos_especial: N` correto: o art. 3º não tem hipótese de magistério
- [x] "85" da fórmula do `nome` conferido: 55 (alínea "a") + 30 (inciso I)
- [ ] A alínea "a" do art. 40, § 1º, III — os 55 anos sobre os quais a redução incide — não é citada nem vinculada; a regra cita a redação da EC 103/2019 do inciso, que a extinguiu — `achado-0046`
- [ ] `ec-47-2005/art-3-par-unico/original` está autorado e não é vinculado, embora funde `paridade: S` e a citação o alcance. Proposta de vínculo, não aplicada aqui
- [ ] `ec-47-2005/norma.md` não declara `vigencia_inicio`: a retroatividade do art. 6º admite duas datas e o corpus ainda não escolheu
- [ ] Tempo de contribuição, serviço público, carreira, cargo e a redução de um ano por ano excedente não têm coluna: a fórmula não é conferível contra o cadastro (Q5)
- [ ] Vigência do art. 3º da EC 47/2005 depois de 13/11/2019 em aberto (art. 35, IV e art. 36, II da EC 103/2019); `ec-47-2005/art-3/original` sem janela declarada
- [ ] `ec-47-2005/art-3/original` transcreve só o *caput*: os três incisos estão fora do corpus
- [ ] `data_adm_apos: 01/01/1910` é sentinela inferior sem correspondência normativa, divergindo do 01/01/1950 usado em 79 regras
