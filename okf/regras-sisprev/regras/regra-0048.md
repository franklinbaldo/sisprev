---
type: Regra
id: regra-0048
row_index: 48
nome: Voluntária · ingresso até 14/09/2021, requisitos a partir de 14/09/2021 · Feminino
tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 3º
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
data_adm_ate: 14/09/2021 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 14/09/2021 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria voluntária por idade e tempo de contribuição, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 6º, § 2º, II, e § 3°, II, da EC nº 146/2021, e artigo 40, § 1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019 - REGRA TRANSITÓRIA - EMENDA ESTADUAL
visivel_dtc_integral: N
sexo: FEMININO
integral: S
tipo_calculo: Valor Médio
fundamentacao: Art. 6º, §2º, II da EC 146/2021 (cálculo pela média das 80% maiores remunerações e sem paridade remuneratória).
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ece-146-2021/art-6-par-2-inc-ii/original.md
  - /dispositivos/ece-146-2021/art-6-par-3-inc-ii/original.md
---

# Estado da análise

Transição do **art. 6º da ECE 146/2021** pelo trilho da **média**, no feminino:
`regra-0047` é a mesma regra no masculino, e o único campo que as separa é
`sexo`.

O desdobramento **está fundado** — art. 6º, I (57 anos se mulher, 60 se homem) e
II (30 anos de contribuição se mulher, 35 se homem) — em provisão que campo
nenhum desta regra cita e que não está transcrita no corpus:
[`achado-0030`](../achados/achado-0030.md).

O lado do resultado fecha inteiro pelo § 2º, II e pelo § 3º, II, e
`data_adm_ate: 14/09/2021` é o corte de ingresso do *caput*. A clientela do
inciso II é definida por complemento, e a segunda condição do complemento — a
opção do § 16 do art. 40 da CF — não tem coluna: para quem ingressou antes de
2004, esta regra e a `regra-0044` continuam indistinguíveis pelo cadastro.

- [x] Critérios do cadastro percorridos um a um contra o art. 6º da ECE 146/2021, na publicação oficial arquivada (`fontes-oficiais/arquivos/sapl-emenda_146.pdf`, sha256 `947726c7…`). O PDF é digitalização **sem camada de texto** — `pdftotext` extrai 10 caracteres —, então a conferência foi feita por leitura visual da p. 7 e `grep` vazio nesta norma não é prova de ausência
- [x] `tabelapontuacao: N` fundado por ausência: o art. 6º **não tem inciso de pontuação**, ao contrário do art. 5º, V (86 pontos se mulher, 96 se homem, com progressão nos §§ 2º e 5º). Fecha o ponto em aberto nº 3 da [conferência do lote](../../../docs/analysis/conferencia-criterio-dispositivo-voluntaria-cf88.md)
- [x] Janela de direito coerente: `apos = 14/09/2021` é a vigência declarada da Emenda e `ate = 31/12/2099` é sentinela — e é o valor **certo** aqui, porque o art. 6º não fixa prazo de implementação. O prazo de 31/12/2024 do art. 4º alcança "os requisitos e os critérios exigidos pela legislação vigente **até** a data de entrada em vigor desta Emenda", que o art. 6º não é
- [x] `dispositivos:` conferido contra `fundamentacao` e `fundamentacao_integral` item a item: os três dispositivos citados estão vinculados, nada a acrescentar nem a remover
- [x] `cf88/art-40-par-1-inc-iii/ec-103-2019` ("segunda parte") funda a **competência** do Estado para fixar idade mínima mediante emenda à sua Constituição — elo de articulação, não critério em coluna
- [x] `integral: S` + `tipo_calculo: Valor Médio` fundados no § 2º, II ("média aritmética simples das maiores remunerações [...] correspondentes a 80% de todo o período contributivo"). `integral: S` com média não é contradição: é a leitura corrente do catálogo, em que `integral` significa "100% da base apurada"
- [x] `paridade: N` fundada no § 3º, II ("nos termos estabelecidos para o Regime Geral de Previdência Social")
- [x] `data_adm_ate: 14/09/2021` é o corte de ingresso do *caput* do art. 6º ("até a data de entrada em vigor desta Emenda Constitucional"), na vigência que o corpus declara para a Emenda
- [ ] O desdobramento por `sexo` **está fundado** — art. 6º, I (57 anos se mulher, 60 se homem) e II (30 anos de contribuição se mulher, 35 se homem) — mas em provisão que campo nenhum desta regra cita e que não existe no corpus: [`achado-0030`](../achados/achado-0030.md)
- [ ] Idade, tempo de contribuição, 20 anos de efetivo exercício no serviço público, 5 anos no cargo (inciso III) e o **período adicional de contribuição** do inciso IV — o pedágio, que é o requisito característico desta transição — não têm coluna no Sisprev nem provisão citada. A regra é `simulavel: S`, então o motor não afere nenhum deles
- [ ] `nome` idêntico ao da gêmea, sem marca de `sexo`: é o padrão sistêmico medido na D2 do [`achado-0020`](../achados/achado-0020.md), não a lacuna de trilho de `0035`–`0038`. Campo deployável, proposta pertence ao catálogo auditado
- [ ] A coorte do § 2º, II é definida por **complemento** ("para o servidor público não contemplado no inciso I do § 2º"), e o inciso I exige duas coisas: ingresso até 31/12/2003 **e** não ter feito a opção do § 16 do art. 40 da CF. A segunda não tem coluna, de modo que a janela de admissão sozinha nunca separa as duas clientelas — e esta regra se sobrepõe à do inciso I para quem ingressou antes de 2004. A sobreposição é a forma correta de representar o complemento; a lacuna é o § 16 (parente da Q6)
- [ ] A entrada em vigor da Emenda tem **duas** datas candidatas, e o catálogo grava as duas — 14/09/2021 (declarada no corpus, gravada por esta) e 09/09/2021 (lavrada na Emenda, gravada por `0057`/`0058`). Ver [`achado-0027`](../achados/achado-0027.md) §2
