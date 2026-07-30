---
type: Regra
id: regra-0051
row_index: 51
nome: Voluntária · ingresso até 31/12/2003, pedido a partir de 14/09/2021 · pontuação · Masculino · integral · paridade · Remuneração de Contribuição
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
fundamentacao_integral: Aposentadoria voluntária por idade e tempo de contribuição, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 5º, § 6º, I, e § 7°, I, da EC nº 146/2021, e artigo 40, § 1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019 - REGRA TRANSITÓRIA - EMENDA ESTADUAL
visivel_dtc_integral: N
sexo: MASCULINO
integral: S
tipo_calculo: Remuneração de Contribuição
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ece-146-2021/art-5-par-6-inc-i/original.md
  - /dispositivos/ece-146-2021/art-5-par-7-inc-i/original.md
---

# Estado da análise

Transição do **art. 5º da ECE 146/2021** na sua metade mais generosa: quem
ingressou no serviço público até 31/12/2003, não fez a opção do § 16 do art. 40
da CF e chega à idade de 65 anos (homem) leva a **totalidade da remuneração do
cargo** (`integral: S`, `tipo_calculo: Remuneração de Contribuição`) e
**paridade** (`paridade: S`), por força do § 6º, I e do § 7º, I. A `regra-0052`
é a mesma regra no feminino.

O que a separa das vizinhas: de `regra-0055`/`0056` pelo **inciso do § 6º** — lá
a base é a média das 80% maiores remunerações e o reajuste é o do RGPS; de
`regra-0053`/`0054` pelo **magistério** (`apos_especial: S` lá, `N` aqui).

Uma leitura que o cadastro não carrega e que vale registrar, porque muda o caso
concreto: o art. 5º tem **duas** idades. O *caput*, inciso I, permite
aposentar-se aos 61 anos (homem) — 62 a partir de 01/01/2024, pelo § 1º. Mas o
§ 6º, I só concede a integralidade e a paridade **aos 65**. Quem se aposenta no
intervalo cumpre o art. 5º e cai no § 6º, II, isto é, na `regra-0055`. Nenhuma
coluna do Sisprev registra idade, então essa fronteira não é aferível pelo
cadastro.

- [x] Critérios do cadastro percorridos um a um contra o art. 5º da ECE 146/2021, na publicação oficial arquivada (`fontes-oficiais/arquivos/sapl-emenda_146.pdf`, PDF digitalizado sem camada de texto, leitura visual)
- [x] `dispositivos:` conferido contra `fundamentacao_integral` item a item: os três dispositivos citados estão vinculados, nada a acrescentar nem a remover
- [x] `data_adm_ate: 31/12/2003` é literal no § 6º, I ("até 31 de dezembro de 2003")
- [x] `integral: S` + `tipo_calculo: Remuneração de Contribuição` fundados no § 6º, I ("à totalidade da remuneração do servidor público no cargo efetivo")
- [x] `paridade: S` fundada no § 7º, I (remete ao art. 7º da EC 41/2003, autorado no corpus)
- [x] `sexo: MASCULINO` é critério que o dispositivo funda: o § 6º, I exige "65 (sessenta e cinco) anos de idade, se homem" contra 62 se mulher; e o *caput*, I, 61 contra 56
- [x] `tabelapontuacao: S` **fundado**: o art. 5º, V exige somatório de idade e tempo de contribuição de 96 pontos se homem (86 se mulher), acrescido de 1 ponto por ano a partir de 01/01/2022 até 105 (§ 2º), apurado em dias (§ 3º). Fecha o ponto em aberto nº 3 da [conferência do lote](../../../docs/analysis/conferencia-criterio-dispositivo-voluntaria-cf88.md)
- [x] janela de direito coerente: `apos = 14/09/2021` é a vigência da Emenda, na convenção dominante do catálogo (`achado-0015`); `ate = 31/12/2099` é sentinela e é o valor certo **aqui**, porque o art. 5º não fixa prazo de implementação — ao contrário do art. 4º, seus requisitos escalonam indefinidamente (§§ 1º, 2º e 5º)
- [ ] idade mínima, tempo de contribuição, tempo de efetivo exercício no serviço público, tempo no cargo e pontuação exigida **não têm coluna** no Sisprev. Criá-las é alterar o sistema, fora do escopo da parametrização; até então a aferição dos cinco incisos do *caput* é manual
- [ ] o § 8º da Emenda, ao qual o § 6º, I remete expressamente ("observado o disposto no § 8º") para definir o que é "remuneração do servidor público no cargo efetivo", não está transcrito nem vinculado — a base de cálculo desta regra fecha por remissão a texto fora do corpus
- [ ] `cf88/art-40-par-1-inc-iii/ec-103-2019` é citado com o qualificador "segunda parte" e funda a **competência** do Estado para fixar idade mínima por emenda, não critério representado em coluna. Não é citação indevida; é elo de articulação (§5.8 e §6 das conferências)
- [ ] sobreposição legítima com `regra-0055`/`0056` para quem ingressou até 2003: o que separa as duas é a opção do § 16 do art. 40 da CF **e** a idade de 62/65 anos, e nenhuma das duas tem coluna. Ambas são `simulavel: S`, então o motor precisa decidir sem o critério que decide (Q6)
