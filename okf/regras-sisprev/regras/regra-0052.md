---
type: Regra
id: regra-0052
row_index: 52
nome: Voluntária · ingresso até 31/12/2003, requisitos a partir de 14/09/2021 · pontuação · Feminino
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
sexo: FEMININO
integral: S
tipo_calculo: Remuneração de Contribuição
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ece-146-2021/art-5-par-6-inc-i/original.md
  - /dispositivos/ece-146-2021/art-5-par-7-inc-i/original.md
---

# Estado da análise

Transição do **art. 5º da ECE 146/2021** na sua metade mais generosa, no
feminino: quem ingressou no serviço público até 31/12/2003, não fez a opção do
§ 16 do art. 40 da CF e chega aos 62 anos leva a **totalidade da remuneração do
cargo** (`integral: S`, `tipo_calculo: Remuneração de Contribuição`) e
**paridade** (`paridade: S`), pelo § 6º, I e pelo § 7º, I. A `regra-0051` é a
mesma regra no masculino, e `sexo` é a única coluna em que as duas diferem — por
isso o `P1_NOME_REPETIDO` do par não é duplicação (as duas idades do § 6º, I são
62 e 65).

O que a separa das vizinhas: de `regra-0056` pelo **inciso do § 6º** (lá, média
das 80% maiores e reajuste do RGPS); de `regra-0054` pelo **magistério**.

Registro a mesma leitura anotada na gêmea, porque muda o caso concreto: o
*caput*, I permite aposentar-se aos 56 anos (57 a partir de 01/01/2024, § 1º),
mas o § 6º, I só concede integralidade e paridade **aos 62**. Quem se aposenta
no intervalo cai no § 6º, II — a `regra-0056` — e nenhuma coluna do Sisprev
registra idade.

- [x] Critérios do cadastro percorridos um a um contra o art. 5º da ECE 146/2021, na publicação oficial arquivada (`fontes-oficiais/arquivos/sapl-emenda_146.pdf`, PDF digitalizado sem camada de texto, leitura visual)
- [x] `dispositivos:` conferido contra `fundamentacao_integral` item a item: os três dispositivos citados estão vinculados, nada a acrescentar nem a remover
- [x] `data_adm_ate: 31/12/2003` é literal no § 6º, I ("até 31 de dezembro de 2003")
- [x] `integral: S` + `tipo_calculo: Remuneração de Contribuição` fundados no § 6º, I ("à totalidade da remuneração do servidor público no cargo efetivo")
- [x] `paridade: S` fundada no § 7º, I (remete ao art. 7º da EC 41/2003, autorado no corpus)
- [x] `sexo: FEMININO` é critério que o dispositivo funda: o § 6º, I exige "62 (sessenta e dois) anos de idade, se mulher" contra 65 se homem; e o *caput*, I, 56 contra 61
- [x] `tabelapontuacao: S` **fundado**: o art. 5º, V exige somatório de idade e tempo de contribuição de 86 pontos se mulher (96 se homem), acrescido de 1 ponto por ano a partir de 01/01/2022 até 100 (§ 2º), apurado em dias (§ 3º). Fecha o ponto em aberto nº 3 da [conferência do lote](../../../docs/analysis/conferencia-criterio-dispositivo-voluntaria-cf88.md)
- [x] janela de direito coerente: `apos = 14/09/2021` é a vigência da Emenda, na convenção dominante do catálogo (`achado-0015`); `ate = 31/12/2099` é sentinela e é o valor certo **aqui**, porque o art. 5º não fixa prazo de implementação — ao contrário do art. 4º, seus requisitos escalonam indefinidamente (§§ 1º, 2º e 5º)
- [ ] idade mínima, tempo de contribuição, tempo de efetivo exercício no serviço público, tempo no cargo e pontuação exigida **não têm coluna** no Sisprev. Criá-las é alterar o sistema, fora do escopo da parametrização; até então a aferição dos cinco incisos do *caput* é manual
- [ ] o § 8º da Emenda, ao qual o § 6º, I remete expressamente ("observado o disposto no § 8º") para definir o que é "remuneração do servidor público no cargo efetivo", não está transcrito nem vinculado
- [ ] `cf88/art-40-par-1-inc-iii/ec-103-2019` é citado com o qualificador "segunda parte" e funda a **competência** do Estado para fixar idade mínima por emenda, não critério representado em coluna
- [ ] sobreposição legítima com `regra-0056` para quem ingressou até 2003: o que separa as duas é a opção do § 16 do art. 40 da CF **e** a idade de 62 anos, e nenhuma das duas tem coluna. Ambas são `simulavel: S` (Q6)
