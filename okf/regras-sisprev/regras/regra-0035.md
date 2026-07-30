---
type: Regra
id: regra-0035
row_index: 35
nome: Voluntária · ingresso até 31/12/2003, requisitos a partir de 18/10/2021 · Masculino
tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 3º
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
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 18/10/2021 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria voluntária por idade e tempo de contribuição, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 40, § 1°, inciso III, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019, e artigos 25, 27, inciso I, e artigo 32, da Lei Complementar nº 1.100/2021.
visivel_dtc_integral: N
sexo: MASCULINO
integral: S
tipo_calculo: Remuneração de Contribuição
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/lce-1100-2021/art-25/original.md
  - /dispositivos/lce-1100-2021/art-27-inc-i/original.md
  - /dispositivos/lce-1100-2021/art-32/original.md
---

# Estado da análise

Aposentadoria voluntária comum do **regime permanente** da LCE 1.100/2021, pelo
**trilho da integralidade**: quem ingressou no serviço público em cargo efetivo
até 31/12/2003 e não fez a opção do § 16 do art. 40 da CF leva a totalidade da
remuneração do cargo (`tipo_calculo: Remuneração de Contribuição`) com paridade
(`paridade: S`), por força dos arts. 25 e 27, I. A `regra-0036` é a mesma regra
no feminino.

O que a separa das vizinhas é o **trilho**: `regra-0037`/`0038` citam os arts.
24 e 27, II — média das 80% maiores remunerações e reajuste do RGPS — e são a
regra de quem ingressou **depois** de 2003. Os dois pares deveriam particionar a
população por data de ingresso; conferido, não particionam, e é o
[`achado-0028`](../achados/achado-0028.md).

Este par é o mais limpo do grupo: os quatro dispositivos citados fundam cada
critério gravado, e nenhum critério gravado contradiz dispositivo citado.
`data_adm_apos: 01/01/1950` é piso, não marco legal — o trilho só impõe limite
superior — e segue não interpretado (P5).

- [x] Critérios do cadastro percorridos um a um contra a LCE 1.100/2021, na compilação oficial arquivada (`fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt`) — não apenas contra o texto transcrito no corpus
- [x] `dispositivos:` conferido contra `fundamentacao_integral` item a item: os quatro dispositivos citados estão vinculados, nada a acrescentar nem a remover
- [x] `sexo` é critério que o dispositivo funda: o art. 32, I exige "62 (sessenta e dois) anos de idade, se mulher, e 65 (sessenta e cinco) anos de idade, se homem" — o documento do art. 32 no corpus transcreve o artigo **inteiro**, incisos I a IV inclusive
- [x] `apos_especial: N` e `tabelapontuacao: N`: nenhum dispositivo citado institui especialidade (§§ 4º-A/4º-B/4º-C/5º do art. 40 da CF não são citados) nem pontuação
- [x] janela de direito coerente: `apos = 18/10/2021` é a vigência da LCE 1.100/2021, e `ate = 31/12/2099` é sentinela e é o valor certo **aqui**, porque o art. 32 é regra permanente e não fixa prazo de implementação
- [x] Trilho de cálculo conferido nos dois sentidos: o art. 25 dá "totalidade da remuneração no cargo efetivo" e o art. 27, I manda reajustar "de acordo com o disposto no art. 7° da Emenda Constitucional n° 41" — fundam `tipo_calculo` e `paridade: S`
- [x] `data_adm_ate: 31/12/2003` é o corte **literal** dos dois dispositivos do trilho ("até 31 de dezembro de 2003", nos arts. 25 e 27, I)
- [x] `integral: S` sem `fundamentacao_proporcional`: coerente, porque o art. 26 (proventos proporcionais) não é citado nem vinculado
- [ ] Idade (art. 32, I), tempo de contribuição (25 anos, II), 10 anos de efetivo exercício no serviço público (III) e 5 anos no cargo (IV) **não têm coluna** no Sisprev. A regra é `simulavel: S`, então o motor não afere nenhum dos quatro; criar coluna é alterar o sistema, fora do escopo da parametrização (Q5)
- [ ] A opção do § 16 do art. 40 da CF, exigida tanto pelo art. 25 quanto pelo art. 24, não tem coluna — a data de admissão sozinha nunca separa os dois trilhos de cálculo
- [ ] `nome` idêntico ao das outras três do grupo `0035`–`0038` e sem nada do trilho de cálculo: [`achado-0029`](../achados/achado-0029.md). É campo deployável, e a proposta pertence ao catálogo auditado
- [ ] `tipo_calculo: Remuneração de Contribuição` descreve, ao pé da letra, a base do **art. 24** ("remunerações utilizadas como base para as contribuições") e não a do art. 25 ("totalidade da remuneração no cargo efetivo"), que é o que esta regra cita. Alterar domínio de enum é mudar o Sisprev, fora do escopo
