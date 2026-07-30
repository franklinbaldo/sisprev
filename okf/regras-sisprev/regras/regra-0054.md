---
type: Regra
id: regra-0054
row_index: 54
nome: Voluntária · Magistério · ingresso até 31/12/2003, pedido a partir de 14/09/2021 · pontuação · Feminino · integral · paridade · Remuneração de Contribuição
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
tabelapontuacao: S
requisitos_da_in_no_5_2020: N
relatorio_p_reserva_remunerada_por_idade_ex_officio: N
adicional_inatividade: N
data_adm_ate: 31/12/2003 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 14/09/2021 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria especial de professor, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 5º, §§ 4° e 6°, inciso I, e § 7º, I, da Emenda Constitucional Estadual nº 146/2021, e artigo 40, §5°, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019.
visivel_dtc_integral: N
sexo: FEMININO
integral: S
tipo_calculo: Remuneração de Contribuição
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-5/ec-103-2019.md
  - /dispositivos/ece-146-2021/art-5-par-4/original.md
  - /dispositivos/ece-146-2021/art-5-par-6-inc-i/original.md
  - /dispositivos/ece-146-2021/art-5-par-7-inc-i/original.md
---

# Estado da análise

Transição do art. 5º da ECE 146/2021 **para a professora**, na metade generosa
do § 6º: comprovado exclusivamente magistério na educação infantil, no ensino
fundamental e médio, o § 4º reduz os requisitos a 51 anos de idade e 25 de
contribuição; tendo ingressado até 31/12/2003, sem a opção do § 16 do art. 40 da
CF, e aos 57 anos, leva a totalidade da remuneração do cargo com paridade, pelo
§ 6º, I e pelo § 7º, I. A `regra-0053` é a mesma regra no masculino, e `sexo` é a
única coluna em que as duas diferem.

O que a separa das vizinhas: de `regra-0052` pelo **magistério**; de
`regra-0058` pelo **inciso do § 6º** — e é entre este par e aquele que está o
buraco de 01/01/2004 do `achado-0033`.

Bifurcação de idade, com números próprios: o § 4º permite aposentar-se aos **51**
anos (52 a partir de 01/01/2023, § 4º, III), mas o § 6º, I só concede
integralidade e paridade aos **57**. Seis anos em que a professora cumpre o art.
5º e cai no § 6º, II — a `regra-0058`. Idade não é coluna do Sisprev.

- [x] Critérios do cadastro percorridos um a um contra o art. 5º da ECE 146/2021, na publicação oficial arquivada (`fontes-oficiais/arquivos/sapl-emenda_146.pdf`, PDF digitalizado sem camada de texto, leitura visual)
- [x] `dispositivos:` conferido contra `fundamentacao_integral` item a item: os quatro dispositivos citados estão vinculados, nada a acrescentar nem a remover
- [x] `apos_especial: S` fundado no § 4º (requisitos reduzidos do magistério) e na competência do art. 40, § 5º da CF, na redação da EC 103/2019 — ambos citados e vinculados
- [x] `data_adm_ate: 31/12/2003` é literal no § 6º, I
- [x] `integral: S` + `tipo_calculo: Remuneração de Contribuição` fundados no § 6º, I
- [x] `paridade: S` fundada no § 7º, I (remete ao art. 7º da EC 41/2003, autorado no corpus)
- [x] `sexo: FEMININO` é critério que o dispositivo funda **duas vezes**: o § 4º exige 51 anos e 25 de contribuição se mulher (56 e 30 se homem), e o § 6º, I exige 57 anos de idade se mulher (60 se homem) para a integralidade
- [x] `tabelapontuacao: S` **fundado**: o art. 5º, V exige somatório de pontos, e o § 5º fixa para a professora 81 pontos (91 se homem), acrescido de 1 por ano a partir de 01/01/2022 até 92. Fecha o ponto em aberto nº 3 da [conferência do lote](../../../docs/analysis/conferencia-criterio-dispositivo-voluntaria-cf88.md)
- [x] janela de direito coerente: `apos = 14/09/2021` é a vigência da Emenda (convenção dominante do catálogo, `achado-0015`); `ate = 31/12/2099` é sentinela e é o valor certo aqui — o art. 5º não fixa prazo de implementação, seus requisitos escalonam (§§ 1º, 2º, 4º-III e 5º)
- [ ] `achado-0033`: o teto de admissão desta regra (31/12/2003) e o piso de `regra-0057`/`0058` (01/01/2004) deixam **01/01/2004 descoberto** sob a semântica confirmada. Correção é de campo deployável
- [ ] idade mínima, tempo de contribuição, tempo de efetivo exercício no serviço público, tempo no cargo, pontuação e **tempo de efetivo exercício das funções de magistério** não têm coluna no Sisprev — o § 4º remete este último a lei complementar, que não está no corpus
- [ ] o § 8º da Emenda, ao qual o § 6º, I remete para definir "remuneração do servidor público no cargo efetivo", não está transcrito nem vinculado
- [ ] `cf88/art-40-par-5/ec-103-2019` condiciona a redução a tempo de magistério "fixado em lei complementar do respectivo ente federativo" — essa lei complementar não é citada por campo nenhum desta regra
