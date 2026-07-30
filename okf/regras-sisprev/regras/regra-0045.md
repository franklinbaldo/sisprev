---
type: Regra
id: regra-0045
row_index: 45
nome: Voluntária · Magistério · ingresso até 31/12/2003, requisitos a partir de 14/09/2021 · Masculino
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
data_adm_ate: 31/12/2003 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 14/09/2021 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria especial de professor, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 6º, §§ 1° e 2°, inciso I, e § 3º, I, da Emenda Constitucional Estadual nº 146/2021, e artigo 40, §5°, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019.
visivel_dtc_integral: N
sexo: MASCULINO
integral: S
tipo_calculo: Remuneração de Contribuição
fundamentacao: Art. 6º, §2º, I, da EC 146/2021 (cálculo por integralidade e paridade remuneratória)
dispositivos:
  - /dispositivos/cf88/art-40-par-5/ec-103-2019.md
  - /dispositivos/ece-146-2021/art-6-par-1/original.md
  - /dispositivos/ece-146-2021/art-6-par-2-inc-i/original.md
  - /dispositivos/ece-146-2021/art-6-par-3-inc-i/original.md
---

# Estado da análise

Transição do **art. 6º da ECE 146/2021** para o **magistério**, pelo trilho da
integralidade: o professor que comprove exclusivamente tempo de magistério tem
idade e tempo de contribuição reduzidos em cinco anos (§ 1º) e, tendo ingressado
no serviço público até 31/12/2003, leva a totalidade da remuneração do cargo com
paridade (§ 2º, I e § 3º, I). A `regra-0046` é a mesma regra no feminino.

O que a separa das vizinhas: de `regra-0043`/`0044` pelo **magistério**
(`apos_especial: S`); de `regra-0049`/`0050` pelo **inciso do § 2º** — lá a base
é a média das 80% maiores e o reajuste é o do RGPS.

Diferentemente de `0043`/`0044`, este par é **simétrico**: `fundamentacao` está
preenchida com o mesmo texto nos dois registros. O que não fecha é o mesmo do
resto do subgrupo: os requisitos que o § 1º reduz estão nos incisos I e II do
*caput*, que campo nenhum cita — [`achado-0030`](../achados/achado-0030.md).

- [x] Critérios do cadastro percorridos um a um contra o art. 6º da ECE 146/2021, na publicação oficial arquivada (`fontes-oficiais/arquivos/sapl-emenda_146.pdf`, sha256 `947726c7…`). O PDF é digitalização **sem camada de texto** — `pdftotext` extrai 10 caracteres —, então a conferência foi feita por leitura visual da p. 7 e `grep` vazio nesta norma não é prova de ausência
- [x] `tabelapontuacao: N` fundado por ausência: o art. 6º **não tem inciso de pontuação**, ao contrário do art. 5º, V (86 pontos se mulher, 96 se homem, com progressão nos §§ 2º e 5º). Fecha o ponto em aberto nº 3 da [conferência do lote](../../../docs/analysis/conferencia-criterio-dispositivo-voluntaria-cf88.md)
- [x] Janela de direito coerente: `apos = 14/09/2021` é a vigência declarada da Emenda e `ate = 31/12/2099` é sentinela — e é o valor **certo** aqui, porque o art. 6º não fixa prazo de implementação. O prazo de 31/12/2024 do art. 4º alcança "os requisitos e os critérios exigidos pela legislação vigente **até** a data de entrada em vigor desta Emenda", que o art. 6º não é
- [x] `dispositivos:` conferido contra `fundamentacao` e `fundamentacao_integral` item a item: os quatro dispositivos citados estão vinculados, nada a acrescentar nem a remover
- [x] `apos_especial: S` fundado no § 1º do art. 6º ("serão reduzidos, para ambos os sexos, os requisitos de idade e tempo de contribuição em 5 anos") articulado com `cf88/art-40-par-5/ec-103-2019`, que habilita a redução no plano federal
- [x] `integral: S` + `tipo_calculo: Remuneração de Contribuição` fundados no § 2º, I ("à totalidade da remuneração do servidor público no cargo efetivo em que se der a aposentadoria")
- [x] `paridade: S` fundada no § 3º, I, que remete ao art. 7º da EC 41/2003 — norma autorada no corpus
- [x] `data_adm_ate: 31/12/2003` é literal no § 2º, I ("até 31 de dezembro de 2003")
- [ ] O desdobramento por `sexo` **está fundado** — art. 6º, I (57 anos se mulher, 60 se homem) e II (30 anos de contribuição se mulher, 35 se homem) — mas em provisão que campo nenhum desta regra cita e que não existe no corpus: [`achado-0030`](../achados/achado-0030.md)
- [ ] Idade, tempo de contribuição, 20 anos de efetivo exercício no serviço público, 5 anos no cargo (inciso III) e o **período adicional de contribuição** do inciso IV — o pedágio, que é o requisito característico desta transição — não têm coluna no Sisprev nem provisão citada. A regra é `simulavel: S`, então o motor não afere nenhum deles
- [ ] `nome` idêntico ao da gêmea, sem marca de `sexo`: é o padrão sistêmico medido na D2 do [`achado-0020`](../achados/achado-0020.md), não a lacuna de trilho de `0035`–`0038`. Campo deployável, proposta pertence ao catálogo auditado
- [ ] O § 8º do **art. 5º** da Emenda, ao qual o § 2º, I remete expressamente ("observado o disposto no § 8º do art. 5º") para definir o que é "remuneração do servidor público no cargo efetivo", não está transcrito nem vinculado — a base de cálculo desta regra fecha por remissão a texto fora do corpus
- [ ] O § 1º exige comprovação **exclusiva** de tempo de magistério na educação infantil e no ensino fundamental e médio. É aferição manual, sem coluna e sem documento de suporte declarado — e a redução de 5 anos que ele concede incide sobre os incisos I e II do *caput*, que esta regra não cita ([`achado-0030`](../achados/achado-0030.md))
- [ ] `cf88/art-40-par-5/ec-103-2019` reduz a idade mínima "em relação às idades decorrentes da aplicação do disposto no inciso III do § 1º" do art. 40 da CF — que esta regra não cita. Na transição estadual quem opera a redução é o § 1º do art. 6º, então o vínculo federal é habilitação e não a norma aplicada; a articulação entre os dois não está explicitada em campo nenhum
