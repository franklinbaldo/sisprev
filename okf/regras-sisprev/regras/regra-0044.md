---
type: Regra
id: regra-0044
row_index: 44
nome: Voluntária · ingresso até 31/12/2003, requisitos a partir de 14/09/2021 · Feminino
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
sexo: FEMININO
integral: S
tipo_calculo: Remuneração de Contribuição
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ece-146-2021/art-6-par-2-inc-i/original.md
  - /dispositivos/ece-146-2021/art-6-par-3-inc-i/original.md
---

# Estado da análise

Transição do **art. 6º da ECE 146/2021** pelo trilho da integralidade, no
feminino: `regra-0043` é a mesma regra no masculino, e divergem em dois campos —
`sexo` e `fundamentacao`, esta preenchida lá e vazia aqui
([`achado-0031`](../achados/achado-0031.md)). A frase que falta é uma
explicitação de efeito, "(cálculo por integralidade e paridade remuneratória)",
e não uma citação nova: o § 2º, I já é nomeado pela `fundamentacao_integral` das
duas, e nada em `dispositivos:` muda.

O desdobramento por sexo **está fundado** — art. 6º, I dá 57 anos de idade se
mulher contra 60 se homem, e o inciso II dá 30 anos de contribuição contra 35 —
mas em provisão que nenhum campo desta regra cita e que não está transcrita:
[`achado-0030`](../achados/achado-0030.md).

O lado do resultado fecha inteiro pelo § 2º, I e pelo § 3º, I.

- [x] Critérios do cadastro percorridos um a um contra o art. 6º da ECE 146/2021, na publicação oficial arquivada (`fontes-oficiais/arquivos/sapl-emenda_146.pdf`, sha256 `947726c7…`). O PDF é digitalização **sem camada de texto** — `pdftotext` extrai 10 caracteres —, então a conferência foi feita por leitura visual da p. 7 e `grep` vazio nesta norma não é prova de ausência
- [x] `tabelapontuacao: N` fundado por ausência: o art. 6º **não tem inciso de pontuação**, ao contrário do art. 5º, V (86 pontos se mulher, 96 se homem, com progressão nos §§ 2º e 5º). Fecha o ponto em aberto nº 3 da [conferência do lote](../../../docs/analysis/conferencia-criterio-dispositivo-voluntaria-cf88.md)
- [x] Janela de direito coerente: `apos = 14/09/2021` é a vigência declarada da Emenda e `ate = 31/12/2099` é sentinela — e é o valor **certo** aqui, porque o art. 6º não fixa prazo de implementação. O prazo de 31/12/2024 do art. 4º alcança "os requisitos e os critérios exigidos pela legislação vigente **até** a data de entrada em vigor desta Emenda", que o art. 6º não é
- [x] `dispositivos:` conferido contra `fundamentacao_integral` item a item: os três dispositivos citados estão vinculados, nada a acrescentar nem a remover
- [x] `cf88/art-40-par-1-inc-iii/ec-103-2019` ("segunda parte") funda a **competência** do Estado para fixar idade mínima mediante emenda à sua Constituição — elo de articulação, não critério em coluna
- [x] `integral: S` + `tipo_calculo: Remuneração de Contribuição` fundados no § 2º, I ("à totalidade da remuneração do servidor público no cargo efetivo em que se der a aposentadoria")
- [x] `paridade: S` fundada no § 3º, I, que remete ao art. 7º da EC 41/2003 — norma autorada no corpus
- [x] `data_adm_ate: 31/12/2003` é literal no § 2º, I ("até 31 de dezembro de 2003")
- [ ] O desdobramento por `sexo` **está fundado** — art. 6º, I (57 anos se mulher, 60 se homem) e II (30 anos de contribuição se mulher, 35 se homem) — mas em provisão que campo nenhum desta regra cita e que não existe no corpus: [`achado-0030`](../achados/achado-0030.md)
- [ ] Idade, tempo de contribuição, 20 anos de efetivo exercício no serviço público, 5 anos no cargo (inciso III) e o **período adicional de contribuição** do inciso IV — o pedágio, que é o requisito característico desta transição — não têm coluna no Sisprev nem provisão citada. A regra é `simulavel: S`, então o motor não afere nenhum deles
- [ ] `nome` idêntico ao da gêmea, sem marca de `sexo`: é o padrão sistêmico medido na D2 do [`achado-0020`](../achados/achado-0020.md), não a lacuna de trilho de `0035`–`0038`. Campo deployável, proposta pertence ao catálogo auditado
- [ ] O § 8º do **art. 5º** da Emenda, ao qual o § 2º, I remete expressamente ("observado o disposto no § 8º do art. 5º") para definir o que é "remuneração do servidor público no cargo efetivo", não está transcrito nem vinculado — a base de cálculo desta regra fecha por remissão a texto fora do corpus
- [ ] `fundamentacao` vazia aqui e preenchida na gêmea `regra-0043`: [`achado-0031`](../achados/achado-0031.md). Corrigir em qualquer direção deixa `sexo` como única divergência do par, que é o estado correto
