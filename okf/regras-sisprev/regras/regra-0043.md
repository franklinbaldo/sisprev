---
type: Regra
id: regra-0043
row_index: 43
id_sisprev: '92'
nome_original: Voluntária por Idade e Tempo de Contribuição - Art. 6º, §2º, I da EC nº 146/2021
nome: Voluntária · ingresso até 31/12/2003, pedido a partir de 14/09/2021 · integral · paridade
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
data_direito_apos: 14/09/2021 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria voluntária por idade e tempo de contribuição, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 6º, § 2º, I, e § 3°, I, da EC nº 146/2021, e artigo 40, § 1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019 - REGRA TRANSITÓRIA - EMENDA ESTADUAL
visivel_dtc_integral: N
sexo: MASCULINO
integral: S
tipo_calculo: Remuneração de Contribuição
fundamentacao: Art. 6º, § 2º, I, da EC 146/2021 (cálculo por integralidade e paridade remuneratória)
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ece-146-2021/art-6-par-2-inc-i/original.md
  - /dispositivos/ece-146-2021/art-6-par-3-inc-i/original.md
---

# Estado da análise

Transição do **art. 6º da ECE 146/2021** na sua metade mais generosa: quem
ingressou em cargo efetivo até a entrada em vigor da Emenda e, além disso, entrou
no serviço público até 31/12/2003 sem optar pelo § 16 do art. 40 da CF, leva a
**totalidade da remuneração do cargo** (`integral: S`,
`tipo_calculo: Remuneração de Contribuição`) com **paridade** (`paridade: S`),
por força do § 2º, I e do § 3º, I. A `regra-0044` é a mesma regra no feminino.

O que a separa das vizinhas: de `regra-0047`/`0048` pelo **inciso do § 2º** — lá
a base é a média das 80% maiores remunerações e o reajuste é o do RGPS; de
`regra-0045`/`0046` pelo **magistério** (`apos_especial: S` lá, `N` aqui).

O lado do **resultado** fecha inteiro. O lado do **requisito** não é citado por
campo nenhum: idade, tempo de contribuição, tempo de serviço público, tempo no
cargo e o pedágio do inciso IV estão no *caput* e nos incisos I a IV, que a
fundamentação não nomeia e que não existem no corpus. E é justamente ali que
mora o fundamento do único critério discriminante que esta regra grava — o
`sexo`. Registrado em [`achado-0030`](../achados/achado-0030.md), que também
corrige a leitura anterior de que o § 1º ("para ambos os sexos") negaria o
desdobramento: aquela oração governa a **redução**, não os requisitos.

- [x] Critérios do cadastro percorridos um a um contra o art. 6º da ECE 146/2021, na publicação oficial arquivada (`fontes-oficiais/arquivos/sapl-emenda_146.pdf`, sha256 `947726c7…`). O PDF é digitalização **sem camada de texto** — `pdftotext` extrai 10 caracteres —, então a conferência foi feita por leitura visual da p. 7 e `grep` vazio nesta norma não é prova de ausência
- [x] `tabelapontuacao: N` fundado por ausência: o art. 6º **não tem inciso de pontuação**, ao contrário do art. 5º, V (86 pontos se mulher, 96 se homem, com progressão nos §§ 2º e 5º). Fecha o ponto em aberto nº 3 da [conferência do lote](../../../docs/analysis/conferencia-criterio-dispositivo-voluntaria-cf88.md)
- [x] Janela de direito coerente: `apos = 14/09/2021` é a vigência declarada da Emenda e `ate = 31/12/2099` é sentinela — e é o valor **certo** aqui, porque o art. 6º não fixa prazo de implementação. O prazo de 31/12/2024 do art. 4º alcança "os requisitos e os critérios exigidos pela legislação vigente **até** a data de entrada em vigor desta Emenda", que o art. 6º não é
- [x] `dispositivos:` conferido contra `fundamentacao` e `fundamentacao_integral` item a item: os três dispositivos citados estão vinculados, nada a acrescentar nem a remover
- [x] `cf88/art-40-par-1-inc-iii/ec-103-2019` é citado com o qualificador "segunda parte" e funda a **competência** do Estado para fixar idade mínima mediante emenda à sua Constituição — que é exatamente o que a ECE 146/2021 faz. É elo de articulação, não critério em coluna
- [x] `integral: S` + `tipo_calculo: Remuneração de Contribuição` fundados no § 2º, I ("à totalidade da remuneração do servidor público no cargo efetivo em que se der a aposentadoria")
- [x] `paridade: S` fundada no § 3º, I, que remete ao art. 7º da EC 41/2003 — norma autorada no corpus
- [x] `data_adm_ate: 31/12/2003` é literal no § 2º, I ("até 31 de dezembro de 2003")
- [ ] O desdobramento por `sexo` **está fundado** — art. 6º, I (57 anos se mulher, 60 se homem) e II (30 anos de contribuição se mulher, 35 se homem) — mas em provisão que campo nenhum desta regra cita e que não existe no corpus: [`achado-0030`](../achados/achado-0030.md)
- [ ] Idade, tempo de contribuição, 20 anos de efetivo exercício no serviço público, 5 anos no cargo (inciso III) e o **período adicional de contribuição** do inciso IV — o pedágio, que é o requisito característico desta transição — não têm coluna no Sisprev nem provisão citada. A regra é `simulavel: S`, então o motor não afere nenhum deles
- [ ] `nome` idêntico ao da gêmea, sem marca de `sexo`: é o padrão sistêmico medido na D2 do [`achado-0020`](../achados/achado-0020.md), não a lacuna de trilho de `0035`–`0038`. Campo deployável, proposta pertence ao catálogo auditado
- [ ] O § 8º do **art. 5º** da Emenda, ao qual o § 2º, I remete expressamente ("observado o disposto no § 8º do art. 5º") para definir o que é "remuneração do servidor público no cargo efetivo", não está transcrito nem vinculado — a base de cálculo desta regra fecha por remissão a texto fora do corpus
- [ ] `fundamentacao` preenchida aqui ("Art. 6º, § 2º, I, da EC 146/2021 (cálculo por integralidade e paridade remuneratória)") e **vazia** na gêmea `regra-0044`: [`achado-0031`](../achados/achado-0031.md). Dos dois únicos pares do catálogo com essa assimetria, este é um
