---
type: Regra
id: regra-0056
row_index: 56
id_sisprev: '105'
nome: Voluntária · pedido a partir de 14/09/2021 · pontuação · Feminino · integral · média
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
sexo: FEMININO
integral: S
tipo_calculo: Valor Médio
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ece-146-2021/art-5-par-6-inc-ii/original.md
  - /dispositivos/ece-146-2021/art-5-par-7-inc-ii/original.md
---

# Estado da análise

Transição do art. 5º da ECE 146/2021 na metade do **§ 6º, II**, no feminino:
cumpridos os requisitos do *caput* mas não contemplada pelo inciso I do § 6º, a
servidora recebe a média aritmética simples das 80% maiores remunerações de
contribuição (`tipo_calculo: Valor Médio`) e reajuste nos termos do RGPS
(`paridade: N`). A `regra-0055` é a mesma regra no masculino, e `sexo` é a única
coluna em que as duas diferem.

`integral: S` com `Valor Médio` **não** é contradição: no catálogo `integral`
significa 100% da base apurada, qualquer que seja ela — oito regras da mesma
Emenda usam a combinação com o mesmo texto "com proventos integrais (cálculo por
média)".

"Não contemplada no inciso I do § 6º" tem **três** portas, e só uma é temporal:
ingresso a partir de 2004; ingresso anterior com a opção do § 16 do art. 40 da
CF; e ingresso anterior sem opção mas aposentadoria **antes dos 62 anos** (a
idade que o inciso I exige da mulher para a integralidade, contra os 56 do
*caput*). As duas últimas fazem esta regra sobrepor-se legitimamente à
`regra-0052` no ingresso até 2003, e nenhuma tem coluna no Sisprev.

- [x] Critérios do cadastro percorridos um a um contra o art. 5º da ECE 146/2021, na publicação oficial arquivada (`fontes-oficiais/arquivos/sapl-emenda_146.pdf`, PDF digitalizado sem camada de texto, leitura visual)
- [x] `dispositivos:` conferido contra `fundamentacao_integral` item a item: os três dispositivos citados estão vinculados, nada a acrescentar nem a remover
- [x] `tipo_calculo: Valor Médio` e `integral: S` fundados no § 6º, II ("média aritmética simples das maiores remunerações [...] correspondentes a 80% de todo o período contributivo")
- [x] `paridade: N` fundada no § 7º, II ("nos termos estabelecidos para o Regime Geral de Previdência Social")
- [x] `sexo: FEMININO` é critério que o dispositivo funda: o *caput*, I exige 56 anos se mulher contra 61 se homem (57 e 62 a partir de 01/01/2024, § 1º), e o inciso II, 30 anos de contribuição contra 35
- [x] `tabelapontuacao: S` **fundado**: o art. 5º, V exige somatório de 86 pontos se mulher (96 se homem), acrescido de 1 por ano a partir de 01/01/2022 até 100 (§ 2º), apurado em dias (§ 3º). Fecha o ponto em aberto nº 3 da [conferência do lote](../../../docs/analysis/conferencia-criterio-dispositivo-voluntaria-cf88.md)
- [x] janela de direito coerente: `apos = 14/09/2021` é a vigência da Emenda (convenção dominante do catálogo, `achado-0015`); `ate = 31/12/2099` é sentinela e é o valor certo aqui — o art. 5º não fixa prazo de implementação, seus requisitos escalonam (§§ 1º e 2º)
- [ ] `achado-0032`: `data_adm_ate: 31/12/2099` é sentinela onde o *caput* do art. 5º exige ingresso **até a data de entrada em vigor da Emenda**. Sem teto, a regra alcança quem ingressou depois — exatamente quem o *caput* exclui
- [ ] idade mínima, tempo de contribuição, tempo de efetivo exercício no serviço público, tempo no cargo e pontuação exigida **não têm coluna** no Sisprev; criá-las é alterar o sistema, fora do escopo
- [ ] a opção do § 16 do art. 40 da CF, uma das três portas do § 6º, II, não tem coluna — e é ela, junto com a idade, que deveria separar esta regra da `regra-0052` no ingresso até 2003. Ambas são `simulavel: S` (Q6)
- [ ] `cf88/art-40-par-1-inc-iii/ec-103-2019` é citado com o qualificador "segunda parte" e funda a **competência** do Estado para fixar idade mínima por emenda, não critério representado em coluna
