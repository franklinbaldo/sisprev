---
type: Regra
id: regra-0098
row_index: 98
nome: Voluntária · ingresso até 16/12/1998, requisitos a partir de 31/12/2003 e antes de 31/12/2024 · Feminino · integral · Valor Médio com Redutor da Idade
tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 4º
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
data_adm_ate: 16/12/1998 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2024 00:00
data_direito_apos: 31/12/2003 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria voluntária por idade e tempo de contribuição, com proventos integrais (Média aritmética das contribuições), com Aplicação do redutor de idade (se houver antecipação) e sem paridade, com base no artigo 40, § 1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019, artigo 4º da Emenda à Constituição Estadual nº 146/2021 e artigo 2º da Emenda Constitucional nº 41/2003 - fundamento - regra de transição - EC 41/03 - CF
visivel_dtc_integral: N
sexo: FEMININO
integral: S
tipo_calculo: Valor Médio com Redutor da Idade
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ec-41-2003/art-2/original.md
  - /dispositivos/ece-146-2021/art-4/original.md
---

# Estado da análise

Ramo feminino da transição do art. 2º da EC 41/2003, divergindo da
`regra-0097` **apenas em `sexo`**. Toda a conferência do par masculino se
aplica, e os números que o sexo comanda são os do próprio artigo: 48 anos de
idade (contra 53) pelo inciso I, 30 anos de contribuição (contra 35) pela alínea
*a* do inciso III, e o pedágio de 20% sobre o que faltava em 16/12/1998 para
atingir esses 30 anos.

As quatro janelas coincidem com datas escritas na lei: `data_adm_ate: 16/12/1998` é a publicação da EC 20/1998, a que o *caput* remete;
`data_direito_apos: 31/12/2003` é a vigência da EC 41/2003;
`data_direito_ate: 31/12/2024` é o prazo verbatim do art. 4º da ECE 146/2021.
`paridade: N` é fundado positivamente pelo § 6º do art. 2º, que manda aplicar o
art. 40, § 8º da CF (valor real, não paridade); `tipo_calculo: Valor Médio com Redutor da Idade` nomeia o *caput* (§§ 3º e 17) e o § 1º (3,5%/5% por ano
antecipado). `apos_especial: N` é correto: o magistério é o § 4º do mesmo
artigo, implementado por `regra-0099`/`0100`.

Falta a mesma peça que falta ao par masculino: a alínea "a" do art. 40, § 1º,
III, que é o minuendo do redutor — 55 anos, no ramo feminino — não é citada nem
vinculada.

- [x] Critérios do cadastro percorridos um a um contra o art. 2º da EC 41/2003, lido na publicação do Planalto arquivada localmente (`planalto-emc41.htm`, sha256 `af74d433…`, cp1252)
- [x] `dispositivos:` conferido item a item contra `fundamentacao_integral`: os três vínculos correspondem às três provisões citadas, nada a acrescentar nem a remover
- [x] `sexo: FEMININO` fundado: 48 anos de idade (inciso I) e 30 de contribuição (inciso III, a), contra 53 e 35 do ramo masculino
- [x] As quatro janelas conferidas, uma a uma, contra datas escritas nos dispositivos citados (publicação da EC 20/1998; vigência da EC 41/2003; prazo do art. 4º da ECE 146/2021)
- [x] `paridade: N` fundado positivamente no § 6º do art. 2º (art. 40, § 8º da CF)
- [x] `tipo_calculo: Valor Médio com Redutor da Idade` conferido contra o *caput* e o § 1º do art. 2º
- [x] `apos_especial: N` correto: a hipótese de magistério é o § 4º, implementado por `regra-0099`/`0100`
- [ ] A alínea "a" do art. 40, § 1º, III — os 55 anos sobre os quais o redutor incide — não é citada nem vinculada; a regra cita a redação da EC 103/2019 que a extinguiu — `achado-0046`
- [ ] Idade, tempo de contribuição, pedágio de 20% e percentual do redutor não têm coluna: a diferença por sexo que a lei manda não é conferível contra o cadastro (Q5)
- [ ] Vigência do art. 2º da EC 41/2003 depois de 13/11/2019 em aberto (art. 36, II da EC 103/2019); `ec-41-2003/art-2/original` sem janela declarada
- [ ] `ec-41-2003/art-2/original` transcreve só o *caput*: os requisitos estão nos incisos, ausentes do corpus
