---
type: Regra
id: regra-0072
row_index: 72
id_sisprev: '122'
nome_original: Voluntária do Policial Civil - Art. 7º, §§2º e § 3º da EC nº 146/2021
nome: Voluntária · Policial civil · ingresso até 13/11/2019, pedido a partir de 14/09/2021 · integral · paridade · regra-0072
tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 3º
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
data_adm_ate: 13/11/2019 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 14/09/2021 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria especial de policial, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 7º, §§ 2º e 3º da Emenda Constitucional Estadual nº 146/2021, artigo 1º, inciso II, alínea "a", da Lei Complementar nº 51/1985 e artigo 40, §1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019 - regra transitória homem - idade + tempo + pedágio | Aposentadoria especial de policial, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 7º, §§ 2º e 3º da Emenda Constitucional Estadual nº 146/2021, artigo 1º, inciso II, alínea "b", da Lei Complementar nº 51/1985 e artigo 40, §1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019 - regra transitória mulher - idade + tempo + pedágio
visivel_dtc_integral: N
sexo: MASCULINO
integral: S
tipo_calculo: Remuneração de Contribuição
fundamentacao: Artigo 7º, §§ 2º e 3º, da Emenda Constitucional Estadual nº 146/2021.
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ece-146-2021/art-7-par-2/original.md
  - /dispositivos/ece-146-2021/art-7-par-3/original.md
  - /dispositivos/lc-51-1985/art-1-inc-ii-al-a/lc-144-2014.md
---

# Estado da análise

Regra de transição do art. 7º da ECE 146/2021: o policial civil que ingressou na
carreira até 13/11/2019 aposenta-se na forma da LC 51/1985, com integralidade e
paridade, mas sujeito a idade mínima — 55 anos pelo *caput*, ou 53 anos, se
homem, pelo § 2º, mediante o pedágio do tempo que faltava em 14/09/2021. É a via
do § 2º que a fundamentação desta regra descreve ("idade + tempo + pedágio").

**A pergunta da alínea — a que o `achado-0017` responde mal em três regras
vizinhas — se responde bem aqui.** `sexo: MASCULINO` e o vínculo é
`lc-51-1985/art-1-inc-ii-al-a`, a alínea masculina: 30 anos de contribuição, 20
de exercício policial, "se homem". Conferido na publicação oficial compilada do
Planalto arquivada em `fontes-oficiais/`, não apenas na transcrição do corpus. O
defeito do `achado-0017` **não** ocorre no `dispositivos:` desta regra.

Ocorre no texto, em outra forma: `fundamentacao_integral` empacota as **duas**
alíneas numa célula só, separadas por `|`
([`achado-0037`](../achados/achado-0037.md)). E há um segundo problema, que não é
de mérito jurídico: esta regra é a quinta cópia idêntica de `regra-0074` a
`regra-0077`, separada delas por um único campo que repete o que o `nome` já diz
([`achado-0041`](../achados/achado-0041.md)).

- [x] `sexo` × alínea: MASCULINO ↔ `al-a` (30/20, "se homem"), conferido na fonte oficial (`planalto-lcp51.htm`, cp1252) — o inciso II tem exatamente duas alíneas e a masculina é a "a"
- [x] Cada item de `dispositivos:` resolve, e o dispositivo apontado é citado por um campo de fundamentação desta regra
- [x] `integral: S`, `tipo_calculo: Remuneração de Contribuição` e `paridade: S` fundados no art. 7º, § 3º da ECE 146/2021 (totalidade da remuneração do cargo efetivo + reajuste na mesma proporção e data)
- [x] `data_adm_ate: 13/11/2019` é o corte de ingresso do *caput* do art. 7º, conferido na publicação oficial da Emenda (`sapl-emenda_146.pdf`, p. 8, lida visualmente — o PDF é digitalizado)
- [x] `data_direito_ate: 31/12/2099` coerente com o art. 7º não ter prazo: conferido na mesma página que ele tem *caput* e §§ 1º a 3º, e mais nada. A sentinela segue não interpretada (P5) — é o valor gravado, não "sem limite"
- [ ] `fundamentacao_integral` traz também a articulação feminina (alínea "b", 25/15) — `achado-0037`. Campo deployável: a decisão é de quem responde por ele
- [ ] `dispositivos:` declara uma alínea e a fundamentação cita duas: a união achatada é mais estreita que o campo que ela espelha. Não corrigido de propósito — `achado-0037`, item 3
- [ ] Cópia idêntica de `regra-0074`–`0077` exceto pelo campo `fundamentacao` — `achado-0041`. Granularidade do catálogo é decisão do IPERON, não do auditor
- [ ] `data_direito_apos: 14/09/2021` casa com o `vigencia_inicio` declarado da ECE 146/2021, mas **não** foi conferido contra fonte: a Emenda diz "entra em vigor na data de sua publicação" e a publicação em Diário Oficial não está arquivada — o PDF oficial traz 09/09/2021, data da Assembleia
- [ ] Idade mínima (53 anos), tempo de contribuição (30) e tempo de exercício policial (20) não têm coluna no cadastro, e a regra é `simulavel: S` — o motor seleciona sem aferir nenhum dos três (Q5)
- [ ] `cf88/art-40-par-1-inc-iii/ec-103-2019` é citado e não fixa critério gravado em coluna alguma: para os Estados o inciso remete à idade mínima da emenda estadual, funcionando como norma de competência e remissão (§5.2 de [`achados-candidatos-da-conferencia.md`](../../../docs/analysis/achados-candidatos-da-conferencia.md))
