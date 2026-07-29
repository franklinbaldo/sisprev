---
type: Regra
id: regra-0095
row_index: 95
nome: Voluntária por Tempo de Contribuição - Art. 40, §1º, III, "a" da CF c/c art. 4º da EC 146/21 (Magistério)
tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 4º
validado_pge: 'FALSE'
validado_presidencia: 'FALSE'
simulavel: S
tipo: CIVIL
apos_especial: S
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
fundamentacao_integral: Artigo 40, § 5°, da Constituição Federal, com redação dada pela Emenda Constitucional nº 103/2019, artigos 25, 27, I; 33, da Lei Complementar nº 1.100/2021 e artigo 40, § 1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019 - regra permanente da aposentadoria especial de professor.
visivel_dtc_integral: N
sexo: MASCULINO
integral: S
tipo_calculo: Valor Médio
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/cf88/art-40-par-5/ec-103-2019.md
  - /dispositivos/lce-1100-2021/art-25/original.md
  - /dispositivos/lce-1100-2021/art-27-inc-i/original.md
  - /dispositivos/lce-1100-2021/art-33/original.md
---

# Estado da análise

Ramo masculino de um par (`regra-0096` é o feminino) que descreve **duas regras
diferentes em campos diferentes do mesmo frontmatter**. O `nome` anuncia a
transição da alínea "a" do art. 40, § 1º, III da CF c/c o art. 4º da ECE
146/2021, com "(Magistério)"; a `fundamentacao_integral` e os cinco vínculos
são os da **regra permanente** do professor — § 5º e § 1º, III da CF na redação
da EC 103/2019 e arts. 25, 27, I e 33 da LCE 1.100/2021 —, e o texto se
autodenomina "regra permanente da aposentadoria especial de professor". Nem a
alínea "a" nem o art. 4º aparecem em campo de fundamentação ou em
`dispositivos:`.

As quatro datas gravadas são, valor por valor, as de `regra-0093`/`0094` — a
mesma transição sem magistério —, e uma "regra permanente" não pode ter prazo
de implementação em 31/12/2024. A cauda de citação é o final exato, caractere a
caractere, da `fundamentacao_integral` de `0041`/`0042`/`0107`/`0108`: são seis
regras de professor sob a mesma citação, com três parametrizações
incompatíveis, e só `0041`/`0042` é coerente com ela.

Independentemente de qual regra o par pretende ser, há contradição interna: os
arts. 25 e 27, I que ele **cita e vincula** determinam totalidade da remuneração
do cargo e reajuste paritário, e os campos gravam `Valor Médio` e `paridade: N`.
O art. 33, terceiro artigo estadual citado, funda o `apos_especial: S` (redução
de cinco anos de idade do professor) e nada mais — não decide cálculo nem
reajuste.

- [x] `dispositivos:` conferido item a item contra `fundamentacao_integral`: os cinco vínculos espelham exatamente as cinco provisões citadas, nada a acrescentar nem a remover
- [x] Texto dos arts. 25, 27, I e 33 conferido na compilação oficial (`fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt`); art. 7º da EC 41/2003, a que o art. 27, I remete, conferido na publicação do Planalto arquivada
- [x] `apos_especial: S` fundado no art. 33 da LCE 1.100/2021, que nomeia "O professor" e a redução de 5 anos
- [x] `sexo: MASCULINO` distingue este ramo da `regra-0096`; a redução do art. 33 é de idade, e a idade de referência difere por sexo
- [ ] `nome` e fundamentação apontam para regras diferentes, ambas existentes no catálogo — `achado-0043`; reescrever `FUNDAMENTACAO*` é alteração de produto
- [ ] `paridade: N` contra o art. 27, I e `tipo_calculo: Valor Médio` contra o art. 25, ambos citados e vinculados — `achado-0043`
- [ ] `data_adm_ate: 31/12/2024` incompatível com o corte de ingresso até 31/12/2003 dos arts. 25 e 27, I, e põe no eixo de admissão o prazo de cumprimento de requisitos do art. 4º da ECE 146/2021 — `achado-0043`
- [ ] `data_direito_apos: 31/12/2003` anterior à vigência dos cinco dispositivos citados (EC 103/2019 e LCE 1.100/2021) — `achado-0043`
- [ ] Seis regras de professor sob uma citação, com três parametrizações: ou cinco linhas estão erradas ou as fundamentações deveriam divergir. Granularidade é escolha do IPERON; o `achado-0016` deixa a mesma pergunta aberta para quatro delas
