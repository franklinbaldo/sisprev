---
type: Regra
id: regra-0058
row_index: 58
nome: Voluntária · Magistério · ingresso 01/01/2004 a 09/09/2021, requisitos a partir de 14/09/2021 · pontuação · Feminino
tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 3º
validado_pge: 'FALSE'
validado_presidencia: 'FALSE'
simulavel: S
tipo: CIVIL
apos_especial: S
tipo_remun: ''
paridade: N
tabelapontuacao: S
requisitos_da_in_no_5_2020: N
relatorio_p_reserva_remunerada_por_idade_ex_officio: N
adicional_inatividade: N
data_adm_ate: 09/09/2021 00:00
data_adm_apos: 01/01/2004 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 14/09/2021 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria especial de professor, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 5º, §§ 4° e 6°, inciso II, e § 7º, II, da Emenda Constitucional Estadual nº 146/2021, e artigo 40, §5°, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019.
visivel_dtc_integral: N
sexo: FEMININO
integral: S
tipo_calculo: Valor Médio
fundamentacao: Art.5º, §4º e § 6º, II, da EC 146/2021 (cálculo pela média das 80% maiores remunerações e sem paridade remuneratória)
dispositivos:
  - /dispositivos/cf88/art-40-par-5/ec-103-2019.md
  - /dispositivos/ece-146-2021/art-5-par-4/original.md
  - /dispositivos/ece-146-2021/art-5-par-6-inc-ii/original.md
  - /dispositivos/ece-146-2021/art-5-par-7-inc-ii/original.md
---

# Estado da análise

Transição do art. 5º da ECE 146/2021 **para a professora**, na metade do
**§ 6º, II**: reduzidos os requisitos de idade e tempo de contribuição pelo § 4º
(51 anos e 25 de contribuição), mas não contemplada pelo inciso I do § 6º, ela
recebe a média aritmética simples das 80% maiores remunerações de contribuição
(`tipo_calculo: Valor Médio`) e reajuste nos termos do RGPS (`paridade: N`).

`regra-0057` é o par masculino, e o par **não** difere apenas em `sexo`: difere
também em `integral` (`N` na 0057, `S` aqui), com a `fundamentacao_integral`
byte a byte idêntica nas duas afirmando "com proventos integrais (cálculo por
média)". Nenhum dispositivo do art. 5º faz a base de cálculo depender do sexo —
o § 4º diferencia só idade e tempo, o § 6º, II define a média sem mencionar
sexo. Está no [`achado-0034`](../achados/achado-0034.md), e o valor gravado aqui
(`S`) é o que as outras três regras do mesmo inciso II praticam (`regra-0055`,
`regra-0056`) — o que indica a direção sem decidi-la, porque `integral` é campo
deployável.

Esta regra é, das nove conferidas nesta rodada, a que acumula mais defeitos de
janela: o teto de admissão grava a data do **ato** da Emenda em vez da data de
entrada em vigor (`achado-0032`) e o piso grava um limite que o § 6º, II não
estabelece, deixando 01/01/2004 descoberto face à `regra-0054` (`achado-0033`).

- [x] Critérios do cadastro percorridos um a um contra o art. 5º da ECE 146/2021, na publicação oficial arquivada (`fontes-oficiais/arquivos/sapl-emenda_146.pdf`, PDF digitalizado sem camada de texto, leitura visual)
- [x] `dispositivos:` conferido contra `fundamentacao_integral` item a item: os quatro dispositivos citados estão vinculados, nada a acrescentar nem a remover
- [x] `apos_especial: S` fundado no § 4º (requisitos reduzidos do magistério) e na competência do art. 40, § 5º da CF, na redação da EC 103/2019 — ambos citados e vinculados
- [x] `tipo_calculo: Valor Médio` fundado no § 6º, II ("média aritmética simples das maiores remunerações [...] correspondentes a 80% de todo o período contributivo")
- [x] `paridade: N` fundada no § 7º, II ("nos termos estabelecidos para o Regime Geral de Previdência Social")
- [x] `sexo: FEMININO` é critério que o dispositivo funda: o § 4º exige 51 anos e 25 de contribuição se mulher, contra 56 e 30 se homem
- [x] `tabelapontuacao: S` **fundado**: o art. 5º, V exige somatório de pontos, e o § 5º fixa para a professora 81 pontos (91 se homem), acrescido de 1 por ano a partir de 01/01/2022 até 92. Fecha o ponto em aberto nº 3 da [conferência do lote](../../../docs/analysis/conferencia-criterio-dispositivo-voluntaria-cf88.md)
- [x] janela de direito coerente: `apos = 14/09/2021` é a vigência da Emenda (convenção dominante do catálogo, `achado-0015`); `ate = 31/12/2099` é sentinela e é o valor certo aqui — o art. 5º não fixa prazo de implementação, seus requisitos escalonam (§§ 1º, 2º, 4º-III e 5º)
- [ ] [`achado-0034`](../achados/achado-0034.md): `integral` divergindo do par masculino sem dispositivo que sustente a distinção. Qual dos dois valores o par deve compartilhar é decisão de campo deployável
- [ ] [`achado-0032`](../achados/achado-0032.md): `data_adm_ate: 09/09/2021` é a data do **ato** da Emenda (título: "de 9 de setembro de 2021"), e o *caput* do art. 5º exige ingresso até a data de **entrada em vigor**, que o art. 13 amarra à publicação
- [ ] [`achado-0033`](../achados/achado-0033.md): `data_adm_apos: 01/01/2004` é piso que o § 6º, II não estabelece; deixa 01/01/2004 descoberto face à `regra-0054` e exclui do inciso II os ingressos anteriores a 2004 que ele alcança por motivo não temporal (opção do § 16 do art. 40 da CF; aposentadoria antes dos 57 anos)
- [ ] idade mínima, tempo de contribuição, tempo de efetivo exercício no serviço público, tempo no cargo, pontuação e **tempo de efetivo exercício das funções de magistério** não têm coluna no Sisprev — o § 4º remete este último a lei complementar, que não está no corpus
- [ ] `cf88/art-40-par-5/ec-103-2019` condiciona a redução do professor a tempo de magistério "fixado em lei complementar do respectivo ente federativo" — essa lei complementar não é citada por campo nenhum desta regra
