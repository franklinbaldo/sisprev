---
type: Regra
id: regra-0057
row_index: 57
id_sisprev: '107'
nome_original: Voluntária por Idade e Tempo de Contribuição - Art.5º, §4º da EC 146/21 (Magistério)
nome: Voluntária · Magistério · ingresso após 01/01/2004 e até 09/09/2021, pedido a partir de 14/09/2021 · pontuação · integral · média
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
sexo: MASCULINO
integral: S
tipo_calculo: Valor Médio
fundamentacao: Art.5º, §4º e § 6º, II, da EC 146/2021 (cálculo pela média das 80% maiores remunerações e sem paridade remuneratória)
dispositivos:
  - /dispositivos/cf88/art-40-par-5/ec-103-2019.md
  - /dispositivos/ece-146-2021/art-5-par-4/original.md
  - /dispositivos/ece-146-2021/art-5-par-6-inc-ii/original.md
  - /dispositivos/ece-146-2021/art-5-par-7-inc-ii/original.md
disposicao_de_achados:
  - achado: /achados/achado-0061.md
    disposicao: corrigida
    justificativa: >-
      Conferido o art. 5º da ECE 146/2021 contra a transcrição oficial
      (`fontes-oficiais/transcricoes/sapl-emenda_146.md`): o § 6º distingue
      **inciso I** (totalidade da remuneração, para quem ingressou até
      31/12/2003 e não fez a opção do § 16 do art. 40 da CF) de **inciso
      II** (média aritmética de 80% do período contributivo, "para o
      servidor público não contemplado no inciso I"). Nenhum dos dois é
      redução proporcional ao tempo de contribuição — são duas **bases de
      cálculo** do provento pleno, e o § 7º só troca a regra de reajuste
      (paridade no inciso I, RGPS no inciso II). Esta regra cita o inciso II
      (`tipo_calculo: Valor Médio`) e o § 7º, II (`paridade: N`), exatamente
      como a `regra-0058` — e a `fundamentacao_integral`, idêntica nas duas,
      já dizia "com proventos integrais (cálculo por média)". `integral: N`
      estava errado: corrigido para `S`, igual à irmã. As duas regras ficam
      materialmente idênticas (mesma janela, mesma fundamentação, mesmos
      dispositivos, mesmo `tipo_calculo`, `paridade` e agora `integral`) —
      um grupo `P2_IGUALDADE_MATERIAL_ATIVA` de fato, que este achado não
      resolve: resolver duplicata é mérito do P2, dispor deste achado é só
      confirmar qual campo estava errado. `nome` unificado por decorrência
      (Decisão 11, posição 5): a única faceta que os distinguia deixou de
      divergir.
    decidido_por: franklinbaldo
    decidido_em: 2026-08-27
---
