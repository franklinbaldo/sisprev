---
type: Regra
id: regra-0007
row_index: 7
nome: Invalidez - Art. 40, §1º, I da CF, com redação dada pela EC nº 41/2003 e Arts. 17 e 20 da LC 432/2008
tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 1º
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
data_adm_ate: 31/12/2099 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 31/12/2003 00:00
fundamentacao_proporcional: Aposentadoria por incapacidade permanente, com proventos proporcionais ao tempo de contribuição e sem paridade, com base no artigo 40, § 1º, inciso I, da Constituição Federal, com redação dada pela Emenda Constitucional nº 41/2003, artigos 17, 20, caput, 45 e 62 da Lei Complementar Estadual nº 432/2008, artigo 4º da Emenda à Constituição Estadual nº 146/2021 e artigo 40, § 1°, inciso III, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019 - fundamento incapacidade - LCE 432/08 (doença não catalogada com ingresso após 2003)
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria por incapacidade permanente, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 40, § 1º, inciso I, da Constituição Federal, com redação dada pela Emenda Constitucional nº 41/2003, artigos 20, caput, 45 e 62 da Lei Complementar Estadual nº 432/2008, artigo 4º da Emenda à Constituição Estadual nº 146/2021 e artigo 40, § 1°, inciso III, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019 - fundamento incapacidade - LCE 432/08 (acidente em serviço, moléstia profissional ou doença grave, contagiosa ou incurável com ingresso após 2003).
visivel_dtc_integral: N
sexo: AMBOS
integral: N
tipo_calculo: Proporcionalidade Dias
fundamentacao: Art. 20, §14º e Art. 45 da Lei Complementar nº 432/2008
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ece-146-2021/art-4/original.md
  - /dispositivos/lce-432-2008/art-17/original.md
  - /dispositivos/lce-432-2008/art-20-caput/original.md
  - /dispositivos/lce-432-2008/art-20-par-14/original.md
  - /dispositivos/lce-432-2008/art-45/lce-672-2012.md
  - /dispositivos/lce-432-2008/art-62/original.md
---

# Estado da análise

Mesma família da `regra-0006` — art. 40, § 1º, I na redação da EC 41/2003,
sem corte de ingresso, sem paridade —, com o resultado invertido: proventos
proporcionais (`integral: N`), fração apurada em dias
(`tipo_calculo: Proporcionalidade Dias`).

Esta é a única das quatro regras de invalidez com o campo `fundamentacao`
preenchido: "Art. 20, §14º e Art. 45 da Lei Complementar nº 432/2008". É de
lá que vem o vínculo `lce-432-2008/art-20-par-14/original`, que a
`regra-0006` não tem — a diferença no `dispositivos:` das duas é
consequência direta de uma diferença de campo, não de critério. O cálculo em
dias é fundado pelo art. 17, § 2º ("em número de dias") somado ao § 14 do
art. 20.

Vale o mesmo alerta da vizinha, na direção oposta: `integral: N` não faz
desta "a regra proporcional". Ela carrega a `fundamentacao_integral` também,
palavra por palavra igual à da `regra-0006`. O par difere apenas em campos de
resultado; o critério que o justifica — a causa da incapacidade — mora dentro
do parêntese de um texto compartilhado.

- [x] Critérios do cadastro percorridos um a um contra a lei — conferência `critério → dispositivo` de 0006–0009
- [x] `dispositivos:` conferido contra `fundamentacao_integral`, `fundamentacao_proporcional` e `fundamentacao`, item a item: nada a acrescentar nem a remover
- [x] O dispositivo a mais em relação à `regra-0006` (`art-20-par-14`) é citado pelo campo `fundamentacao` desta regra
- [ ] `cf88/art-40-par-1-inc-iii/ec-103-2019` é citado mas não funda critério representado nas colunas — o inciso III é de aposentadoria voluntária por idade
- [ ] `data_direito_ate: 31/12/2099` discorda do prazo de 31/12/2024 do art. 4º da ECE 146/2021, que esta regra cita
- [ ] Causa da incapacidade — o critério que separa esta regra da `regra-0006` não tem coluna. Depende da Q6
