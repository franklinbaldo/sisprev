---
type: Regra
id: regra-0097
row_index: 97
id_sisprev: '147'
nome_original: Voluntária por Tempo de Contribuição - Art. 2º da EC nº 41/03 e o art. 4º da EC nº 146/2021
nome: Voluntária · ingresso até 16/12/1998, requisitos a partir de 31/12/2003 e antes de 31/12/2024 · Masculino · integral · média
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
sexo: MASCULINO
integral: S
tipo_calculo: Valor Médio com Redutor da Idade
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ec-41-2003/art-2/original.md
  - /dispositivos/ece-146-2021/art-4/original.md
---

# Estado da análise

Ramo masculino da transição do art. 2º da EC 41/2003 — a regra do pedágio de
20% com redutor de proventos —, preservada pelo art. 4º da ECE 146/2021 para
quem cumpriu os requisitos até 31/12/2024. `regra-0098` é o ramo feminino, e
`regra-0099`/`0100` são as gêmeas de magistério (`apos_especial: S`), que o
`achado-0018` já alcança.

**As quatro janelas estão certas, e cada uma coincide com uma data escrita na
lei.** `data_adm_ate: 16/12/1998` é a data de publicação da EC 20/1998, a que o
*caput* do art. 2º remete ("até a data de publicação daquela Emenda");
`data_direito_apos: 31/12/2003` é o dia de vigência da própria EC 41/2003 (DOU
de 31.12.2003, art. 11), na convenção que o `achado-0015` conta 30 vezes neste
marco; `data_direito_ate: 31/12/2024` é o prazo verbatim do art. 4º da ECE
146/2021, e aqui a leitura inclusiva do campo `ATE` corresponde exatamente ao
texto legal — é o único dos quatro marcos que não é fronteira de vigência, mas
prazo fixado no dispositivo.

Registro uma correção à
[lista consolidada](../../../docs/analysis/achados-candidatos-da-conferencia.md),
§5.1: ela afirma que as regras que citam **e vinculam** o art. 4º da ECE
146/2021 gravam `31/12/2099` ou `03/12/2015`. Varridas as 24 que o vinculam,
**dez gravam 31/12/2024** — `0097`–`0106` —, ou seja, o par mais coerente do
catálogo nesse ponto está do lado que a lista descreveu como ausente. O padrão
sistêmico existe; a formulação daquele item precisa de ajuste.

`paridade: N` está fundado, e por norma positiva: o § 6º do art. 2º manda
aplicar o art. 40, § 8º da CF — reajuste "para preservar-lhes, em caráter
permanente, o valor real" —, que é o oposto da paridade do art. 7º da mesma
emenda. `tipo_calculo: Valor Médio com Redutor da Idade` nomeia os dois
mecanismos do artigo: o *caput* manda calcular na forma dos §§ 3º e 17 (média
das contribuições) e o § 1º impõe 3,5% ou 5% de redução por ano antecipado.
`apos_especial: N` é correto — a hipótese do magistério é o § 4º do mesmo
artigo, e são `0099`/`0100` que a implementam.

O que falta é o **ponto de referência do redutor**: os "limites de idade
estabelecidos pelo art. 40, § 1º, III, a, e § 5º da Constituição Federal", que
o § 1º nomeia verbatim. A alínea "a" não é citada nem vinculada, e o que a regra
cita no lugar dela é a redação da EC 103/2019 do inciso III, que a extinguiu.

- [x] Critérios do cadastro percorridos um a um contra o art. 2º da EC 41/2003, lido na publicação do Planalto arquivada localmente (`planalto-emc41.htm`, sha256 `af74d433…`, cp1252)
- [x] `dispositivos:` conferido item a item contra `fundamentacao_integral`: os três vínculos correspondem às três provisões citadas, nada a acrescentar nem a remover
- [x] `data_adm_ate: 16/12/1998` conferido contra o *caput* do art. 2º e contra a data de publicação da EC 20/1998
- [x] `data_direito_apos: 31/12/2003` conferido contra o art. 11 da EC 41/2003 e a convenção do catálogo
- [x] `data_direito_ate: 31/12/2024` conferido contra o art. 4º da ECE 146/2021, transcrito no bundle a partir do PDF do SAPL/ALE-RO
- [x] `paridade: N` fundado positivamente no § 6º do art. 2º (art. 40, § 8º da CF), não por ausência de norma
- [x] `tipo_calculo: Valor Médio com Redutor da Idade` conferido contra o *caput* (§§ 3º e 17) e o § 1º (3,5%/5% por ano antecipado)
- [x] `apos_especial: N` correto: a hipótese de magistério do art. 2º é o seu § 4º, implementado por `regra-0099`/`0100`
- [x] `sexo: MASCULINO` fundado: o inciso I do art. 2º grava 53 anos para homem e 48 para mulher, e o inciso III, a, 35 e 30 anos de contribuição
- [ ] A alínea "a" do art. 40, § 1º, III — referência sobre a qual o redutor incide — não é citada nem vinculada; a regra cita a redação da EC 103/2019 que a extinguiu — `achado-0046`
- [ ] Idade, tempo de contribuição, pedágio de 20% e percentual do redutor **não têm coluna**: a diferença 53/48 e 35/30 que a lei manda não é conferível contra o cadastro (Q5)
- [ ] Vigência do art. 2º da EC 41/2003 depois de 13/11/2019 em aberto: o art. 35 da EC 103/2019 o revoga e o art. 36, II condiciona a revogação, nos RPPS estaduais, a lei estadual de referendo. `ec-41-2003/art-2/original` segue sem janela declarada; conclusão jurídica, não tomada aqui
- [ ] `ec-41-2003/art-2/original` transcreve só o *caput*: os requisitos que esta regra aplica estão nos incisos, ausentes do corpus (fila `TRANSCREVER`, §5.3 da lista consolidada)
