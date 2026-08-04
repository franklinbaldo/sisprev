---
type: Regra
id: regra-0094
row_index: 94
id_sisprev: '144'
nome_original: Voluntária por Tempo de Contribuição - Art. 40, §1º, III, "a" da CF c/c art. 4º da EC 146/21
nome: Voluntária · ingresso até 31/12/2024, requisitos a partir de 31/12/2003 e antes de 31/12/2024 · Feminino · integral · média
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
data_adm_ate: 31/12/2024 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2024 00:00
data_direito_apos: 31/12/2003 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Artigo 40, §1º, inciso III, alínea "a", da Constituição Federal, com redação dada pela Emenda Constitucional nº 20/1998 e artigo 40, §§ 3º e 8º com redação dada pela Emenda Constitucional nº 41/2003, art. 4° da Emenda à Constituição Estadual - CF
visivel_dtc_integral: N
sexo: FEMININO
integral: S
tipo_calculo: Valor Médio
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii-al-a/ec-20-1998.md
---

# Estado da análise

Ramo feminino da transição da alínea "a" do art. 40, § 1º, III da CF —
55 anos de idade e 30 de contribuição, mais dez anos de serviço público e cinco
no cargo exigidos pelo *caput* do inciso —, preservada pelo art. 4º da ECE
146/2021 para quem cumpriu os requisitos até 31/12/2024. O par masculino é a
`regra-0093`, e as duas são **idênticas caractere a caractere** em
`fundamentacao_integral` (246 c, sha256 `8944204766c5…`) e em `dispositivos:`.

Foi a regra que a rodada abriu, pelo sinal do vínculo único, e o sinal se
confirmou: a fundamentação cita **quatro** provisões e `dispositivos:` declara
**uma**. As três causas são distintas — o § 3º não está transcrito, o § 8º cai
na recusa do `achado-0011` (norma dona não nomeada) e o art. 4º da emenda
estadual é citado sem número, embora o `nome` da própria regra o numere e a
regra grave a data que só esse artigo fixa. Nenhum vínculo é acrescentado aqui:
a decisão é do dono do campo, e a RFC 0008 reserva a ato humano explícito
concluir que o `nome` supre a fundamentação.

Segundo achado, independente: o único vínculo declarado é
`al-a/ec-20-1998`, cuja vida termina em 30/12/2003, e a janela de direito da
regra abre em 31/12/2003. A alínea não mudou de texto — o que mudou foi a
cadeia acima dela, quando a EC 41/2003 reescreveu o *caput* do art. 40 e o do
§ 1º —, então a **citação** está certa no nível da alínea e é o **documento**
que está errado. O irmão `al-a/ec-41-2003` existe e cobre a abertura.

- [x] Critérios do cadastro percorridos um a um contra a lei; texto da alínea "a" conferido nas duas redações do bundle e na publicação da EC 41/2003 arquivada localmente
- [x] `dispositivos:` conferido item a item contra `fundamentacao_integral`: **três provisões citadas sem vínculo**, cada uma por causa própria — `achado-0044`
- [x] `sexo: FEMININO` fundado: a alínea "a" distingue explicitamente 55/30 para mulher e 60/35 para homem, e a `regra-0093` é o ramo masculino
- [x] `tipo_calculo: Valor Médio`/`paridade: N` coerentes com os §§ 3º e 8º da CF na redação da EC 41/2003, que a fundamentação cita (média das contribuições; reajuste para preservar valor real, não paridade)
- [x] `data_direito_ate: 31/12/2024` conferido contra o art. 4º da ECE 146/2021, que fixa esse prazo verbatim — é o único dispositivo do corpus a fixá-lo
- [ ] Vínculo aponta a redação `ec-20-1998`, cuja vigência não intersecta a janela da regra — `achado-0045`; a troca por `ec-41-2003` é ato autoral e colide com a hipótese de agregação de períodos
- [ ] `data_adm_ate: 31/12/2024` põe no eixo de admissão o prazo de cumprimento de requisitos do art. 4º da ECE 146/2021, que a regra já grava em `data_direito_ate` — `achado-0045`
- [ ] O que sustenta a regra de 13/11/2019 a 31/12/2024, depois de a EC 103/2019 extinguir a alínea "a": depende do art. 36, II da EC 103/2019 (revogações condicionadas, nos RPPS estaduais, a lei estadual de referendo). Conclusão jurídica, não tomada aqui
- [ ] `cf88/art-40-par-3` não existe no bundle em redação nenhuma: fila `TRANSCREVER` nova, não coberta pela lista congelada
- [ ] `achado-0011` alcança a `regra-0093` e não esta, cuja fundamentação é idêntica. A extensão está registrada no `achado-0044`; unificar as duas populações é decisão de quem mantém o `achado-0011`
