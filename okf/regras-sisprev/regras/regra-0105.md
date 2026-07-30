---
type: Regra
id: regra-0105
row_index: 105
nome: Voluntária · ingresso até 16/12/1998, requisitos 31/12/2003 a 31/12/2024 · Masculino · regra-0105
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
sexo: MASCULINO
integral: S
tipo_calculo: Remuneração de Contribuição
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ec-47-2005/art-3/original.md
  - /dispositivos/ece-146-2021/art-4/original.md
---

# Estado da análise

Ramo masculino da transição do art. 3º da EC 47/2005 — a "fórmula 85/95" do
`nome` —, preservada pelo art. 4º da ECE 146/2021 para requisitos cumpridos até
31/12/2024. `regra-0106` é o ramo feminino.

**Duas janelas conferem contra datas escritas na lei, e a segunda é o achado
positivo da conferência.** `data_adm_ate: 16/12/1998` é o corte de ingresso que
o *caput* do art. 3º grava em letra ("que tenha ingressado no serviço público
até 16 de dezembro de 1998"). E `data_direito_apos: 31/12/2003` — que numa
transição de 2005 parece cedo demais — é exatamente certo: o art. 6º da EC
47/2005 diz que ela "entra em vigor na data de sua publicação, **com efeitos
retroativos à data de vigência da Emenda Constitucional nº 41, de 2003**", isto
é, 31/12/2003. O valor gravado é o marco da retroatividade, não da publicação.
Nota para quem mantém o corpus: `ec-47-2005/norma.md` não declara
`vigencia_inicio` nenhum, então essa conferência não está apoiada no bundle e
sim na publicação oficial arquivada.

`paridade: S` está fundado no **parágrafo único** do art. 3º, que manda aplicar
o art. 7º da EC 41/2003 (proventos "revistos na mesma proporção e na mesma
data"). Ele está autorado como `ec-47-2005/art-3-par-unico/original` e **não é
vinculado**: o vínculo declarado é `ec-47-2005/art-3/original`, que endereça o
artigo inteiro (`componentes: [artigo 3]`) mas transcreve só o *caput*. A
fundamentação cita "artigo 3º da Emenda Constitucional nº 47/2005", sem recorte,
de modo que a citação alcança o parágrafo — o que falta é a resolução do vínculo.

`integral: S` e `tipo_calculo: Remuneração de Contribuição` correspondem a
"poderá aposentar-se com **proventos integrais**" do *caput*, e `apos_especial: N` é correto: o art. 3º não tem hipótese de magistério.

O que falta é o **minuendo da fórmula**. O inciso III fixa a idade mínima como
"resultante da redução, relativamente aos limites do art. 40, § 1º, inciso III,
alínea 'a', da Constituição Federal, de um ano de idade para cada ano de
contribuição que exceder a condição prevista no inciso I". Os 95 do `nome` são
60 (alínea "a") + 35 (inciso I) — e a alínea "a" não é citada nem vinculada. A
regra nomeia-se pelo resultado de um dispositivo que ela não declara.

- [x] Critérios do cadastro percorridos um a um contra o art. 3º da EC 47/2005, lido na publicação do Planalto arquivada localmente (`planalto-emc47.htm`, sha256 `408a9df8…`, cp1252)
- [x] `dispositivos:` conferido item a item contra `fundamentacao_integral`: as três provisões citadas têm vínculo
- [x] `data_adm_ate: 16/12/1998` conferido contra o *caput* do art. 3º, que grava a data em letra
- [x] `data_direito_apos: 31/12/2003` conferido contra o art. 6º da EC 47/2005 (efeitos retroativos à vigência da EC 41/2003)
- [x] `data_direito_ate: 31/12/2024` conferido contra o art. 4º da ECE 146/2021, transcrito no bundle a partir do PDF do SAPL/ALE-RO
- [x] `integral: S` e `tipo_calculo: Remuneração de Contribuição` conferidos contra "proventos integrais" do *caput*
- [x] `paridade: S` fundado positivamente no parágrafo único do art. 3º, que manda aplicar o art. 7º da EC 41/2003
- [x] `apos_especial: N` correto: o art. 3º não tem hipótese de magistério
- [x] `sexo: MASCULINO` fundado: o inciso I grava 35 anos de contribuição para homem e 30 para mulher, e a idade de referência do inciso III é 60 para homem
- [x] "FÓRMULA 85/95" do `nome` conferida: 60 + 35 = 95 (homem), 55 + 30 = 85 (mulher), somas dos limites da alínea "a" com o inciso I
- [ ] A alínea "a" do art. 40, § 1º, III — os 60 anos sobre os quais a redução incide — não é citada nem vinculada; a regra cita a redação da EC 103/2019 do inciso, que a extinguiu — `achado-0046`
- [ ] `ec-47-2005/art-3-par-unico/original` está autorado e não é vinculado, embora seja ele que funda `paridade: S` e a citação ("artigo 3º", sem recorte) o alcance. Proposta de vínculo, não aplicada aqui
- [ ] `ec-47-2005/norma.md` não declara `vigencia_inicio`: a retroatividade do art. 6º admite duas datas (publicação em 06/07/2005, efeitos desde 31/12/2003) e escolher é decisão que o corpus ainda não tomou
- [ ] Tempo de contribuição, serviço público, carreira, cargo e a redução de um ano por ano excedente **não têm coluna**: nem os 35/30 nem a fórmula são conferíveis contra o cadastro (Q5)
- [ ] Vigência do art. 3º da EC 47/2005 depois de 13/11/2019 em aberto: o art. 35, IV da EC 103/2019 o revoga e o art. 36, II condiciona a revogação, nos RPPS estaduais, a lei estadual de referendo. `ec-47-2005/art-3/original` segue sem janela declarada; conclusão jurídica, não tomada aqui
- [ ] `ec-47-2005/art-3/original` transcreve só o *caput*: os três incisos com os requisitos estão fora do corpus (fila `TRANSCREVER`, §5.3 da lista consolidada)
- [ ] `data_adm_apos: 01/01/1910` é sentinela inferior sem correspondência normativa, divergindo do 01/01/1950 usado em 79 regras
