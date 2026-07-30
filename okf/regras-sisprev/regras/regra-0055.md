---
type: Regra
id: regra-0055
row_index: 55
nome: Voluntária · pedido a partir de 14/09/2021 · pontuação · Masculino · integral · média
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
tabelapontuacao: S
requisitos_da_in_no_5_2020: N
relatorio_p_reserva_remunerada_por_idade_ex_officio: N
adicional_inatividade: N
data_adm_ate: 31/12/2099 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 14/09/2021 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria voluntária por idade e tempo de contribuição, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 5º, § 6º, II, e § 7°, II, da EC nº 146/2021, e artigo 40, § 1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019 - REGRA TRANSITÓRIA - EMENDA ESTADUAL
visivel_dtc_integral: N
sexo: MASCULINO
integral: S
tipo_calculo: Valor Médio
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ece-146-2021/art-5-par-6-inc-ii/original.md
  - /dispositivos/ece-146-2021/art-5-par-7-inc-ii/original.md
---

# Estado da análise

Transição do art. 5º da ECE 146/2021 na metade do **§ 6º, II**: cumpridos os
requisitos do *caput* (idade, tempo de contribuição, 20 anos de serviço público,
5 no cargo e o somatório de pontos), mas **não** contemplado pelo inciso I do
§ 6º, o servidor recebe a média aritmética simples das 80% maiores remunerações
de contribuição (`tipo_calculo: Valor Médio`) e reajuste nos termos do RGPS
(`paridade: N`). A `regra-0056` é a mesma regra no feminino.

`integral: S` com `Valor Médio` **não** é contradição: no catálogo `integral`
significa 100% da base apurada, qualquer que seja ela — as gêmeas do art. 6º
(`regra-0047`–`0050`) e a `regra-0058` usam a mesma combinação com o mesmo texto
"com proventos integrais (cálculo por média)". Conferido, e é a leitura corrente
de oito regras da mesma Emenda.

"Não contemplado no inciso I do § 6º" tem **três** portas, e só uma é temporal:
ingresso a partir de 2004; ingresso anterior com a opção do § 16 do art. 40 da
CF; e ingresso anterior sem opção mas aposentadoria **antes dos 65 anos** (a
idade que o inciso I exige do homem para a integralidade, contra os 61 do
*caput*). As duas últimas portas são o que faz esta regra sobrepor-se
legitimamente à `regra-0051` para quem ingressou até 2003 — e nenhuma delas tem
coluna no Sisprev.

- [x] Critérios do cadastro percorridos um a um contra o art. 5º da ECE 146/2021, na publicação oficial arquivada (`fontes-oficiais/arquivos/sapl-emenda_146.pdf`, PDF digitalizado sem camada de texto, leitura visual)
- [x] `dispositivos:` conferido contra `fundamentacao_integral` item a item: os três dispositivos citados estão vinculados, nada a acrescentar nem a remover
- [x] `tipo_calculo: Valor Médio` e `integral: S` fundados no § 6º, II ("média aritmética simples das maiores remunerações [...] correspondentes a 80% de todo o período contributivo")
- [x] `paridade: N` fundada no § 7º, II ("nos termos estabelecidos para o Regime Geral de Previdência Social")
- [x] `sexo: MASCULINO` é critério que o dispositivo funda: o *caput*, I exige 61 anos se homem contra 56 se mulher (62 e 57 a partir de 01/01/2024, § 1º), e o inciso II, 35 anos de contribuição contra 30
- [x] `tabelapontuacao: S` **fundado**: o art. 5º, V exige somatório de 96 pontos se homem (86 se mulher), acrescido de 1 por ano a partir de 01/01/2022 até 105 (§ 2º), apurado em dias (§ 3º). Fecha o ponto em aberto nº 3 da [conferência do lote](../../../docs/analysis/conferencia-criterio-dispositivo-voluntaria-cf88.md)
- [x] janela de direito coerente: `apos = 14/09/2021` é a vigência da Emenda (convenção dominante do catálogo, `achado-0015`); `ate = 31/12/2099` é sentinela e é o valor certo aqui — o art. 5º não fixa prazo de implementação, seus requisitos escalonam (§§ 1º e 2º)
- [ ] `achado-0032`: `data_adm_ate: 31/12/2099` é sentinela onde o *caput* do art. 5º exige ingresso **até a data de entrada em vigor da Emenda**. Sem teto, a regra alcança quem ingressou depois — exatamente quem o *caput* exclui. O par gêmeo do art. 6º (`regra-0047`/`0048`) grava `14/09/2021`
- [ ] idade mínima, tempo de contribuição, tempo de efetivo exercício no serviço público, tempo no cargo e pontuação exigida **não têm coluna** no Sisprev; criá-las é alterar o sistema, fora do escopo
- [ ] a opção do § 16 do art. 40 da CF, que é uma das três portas do § 6º, II, não tem coluna — e é ela, junto com a idade, que deveria separar esta regra da `regra-0051` no ingresso até 2003. Ambas são `simulavel: S`, então o motor decide sem o critério que decide (Q6)
- [ ] `cf88/art-40-par-1-inc-iii/ec-103-2019` é citado com o qualificador "segunda parte" e funda a **competência** do Estado para fixar idade mínima por emenda, não critério representado em coluna
