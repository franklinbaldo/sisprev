---
type: Regra
id: regra-0030
row_index: 30
nome: Compulsória · requisitos a partir de 04/12/2015 e antes de 31/12/2024 · Masculino · proporcional · Proporcionalidade Dias
tipo_de_beneficio: APOSENTADORIA COMPULSÓRIA
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 2º
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
data_direito_ate: 31/12/2024 00:00
data_direito_apos: 04/12/2015 00:00
fundamentacao_proporcional: Aposentadoria compulsória com proventos proporcionais ao tempo de contribuição, com base na média aritmética simples, e sem paridade, com base no artigo 40, § 1º, II, da Constituição Federal, com redação dada pela Emenda Constitucional nº 88/2015, artigo 2º da Lei Complementar nº 152/2015, artigos 24, 26, 27, inciso II, e 31 da Lei Complementar Estadual nº 1.100/2021.
visivel_dtc_proporcional: N
fundamentacao_integral: ''
visivel_dtc_integral: N
sexo: MASCULINO
integral: N
tipo_calculo: Proporcionalidade Dias
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-ii/ec-88-2015.md
  - /dispositivos/lc-152-2015/art-2/original.md
  - /dispositivos/lce-1100-2021/art-24/original.md
  - /dispositivos/lce-1100-2021/art-26/original.md
  - /dispositivos/lce-1100-2021/art-27-inc-ii/original.md
  - /dispositivos/lce-1100-2021/art-31/original.md
---

# Estado da análise

Aposentadoria compulsória sob a redação do **art. 40, § 1º, II da Constituição Federal dada pela EC 88/2015**, cumulada com as normativas estaduais (LCE 1.100/2021) e cálculo proporcional (`Proporcionalidade Dias`).

**A janela temporal e as diretrizes do marco.** A regra inicia em `data_direito_apos: 04/12/2015`. A EC 88/2015 que conferiu a nova redação ao artigo começou a vigorar antes disso (08/05/2015) conforme estabelecido em `/dispositivos/cf88/art-40-par-1-inc-ii/ec-88-2015.md`. A EC 88/2015 delegou à lei complementar a definição para os 75 anos; nesse sentido, a LC 152/2015 (citada nos fundamentos) é que determinou as condições para a compulsória aos 75 anos, entrando em vigor na data provável de 04/12/2015, justificando o marco inicial.

O limite de `data_direito_ate: 31/12/2024` está atrelado ao prazo fixado na reforma e transições documentadas nos normativos da ECE 146/2021 (verificado em outras regras congêneres de aposentadoria no período pós-EC 103/2019/LCE 1.100).

- [x] O marco inicial `data_direito_apos: 04/12/2015` provavelmente se alinha à vigência da LC 152/2015 (e não apenas à EC 88/2015, cuja vigência iniciou em 08/05/2015). A LC 152/2015 regulamentou os 75 anos.
- [x] O marco final `data_direito_ate: 31/12/2024` é compatível com os fechos adotados com base nos prazos garantidores da transição da ECE 146/2021.
- [x] Todos os `dispositivos:` citados na fundamentação (`CF/88 art. 40, § 1º, II pela EC 88/2015`, LC 152/2015 e LCE 1.100/2021) estão listados e vinculados adequadamente ao catálogo OKF.
- [x] A ausência de paridade (`paridade: N`) e o `tipo_calculo: Proporcionalidade Dias` estão estritamente corretos para regras de base da EC 41 em diante.
