---
type: Regra
id: regra-0020
row_index: 20
nome: Incapacidade · ingresso até 31/12/2003, requisitos a partir de 23/10/2021 · Ambos · regra-0020
tipo_de_beneficio: APOSENTADORIA POR INCAPACIDADE PERMANENTE
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 1º
validado_pge: 'FALSE'
validado_presidencia: 'FALSE'
simulavel: N
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
data_direito_apos: 23/10/2021 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria por incapacidade permanente, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 40, § 1º, inciso I, da Constituição Federal, com redação dada pela Emenda Constitucional n. 103/2019 e os artigos 25 e 27, inciso I e 30, §8°, da Lei Complementar Estadual nº 1.100/2021 - fundamento - incapacidade - LCE 1.100/2021 (acidente em serviço, moléstia profissional ou doença grave, contagiosa ou incurável, com ingresso antes de 2004)
visivel_dtc_integral: N
sexo: AMBOS
integral: N
tipo_calculo: Proporcionalidade Dias
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-i/ec-103-2019.md
  - /dispositivos/lce-1100-2021/art-25/original.md
  - /dispositivos/lce-1100-2021/art-27-inc-i/original.md
  - /dispositivos/lce-1100-2021/art-30-par-8/original.md
disposicao_de_achados:
  - achado: /achados/achado-0020.md
    disposicao: corrigida
    justificativa: >-
      Corrigida pela renomeação do catálogo inteiro. Esta regra recebeu
      `nome` pelo padrão de facetas em ordem de anamnese — benefício, categoria
      especial, regime, e sexo quando gravado —, que é a resposta à questão 1 do
      achado ("qual padrão adotar"). A questão 4 dele — se a correção pertencia ao
      catálogo auditado da RFC 0004 em vez de a uma edição em `regra-*.md` — foi
      respondida pela coordenação em 2026-07-30: a auditoria está autorizada a alterar
      `nome`, e o registro está na Decisão 10 de
      `docs/analysis/decisoes-de-auditoria-2026-07-30.md`. Duas coisas que esta
      disposição **não** afirma: que o `P2_IGUALDADE_MATERIAL_ATIVA` sobre esta regra
      tenha sido tocado, se houver — `nome` está fora da chave material, e os sete
      grupos P2 do catálogo seguem idênticos, asseverados por teste; e que a
      padronização deva virar gate, que é a questão 2 do achado e segue aberta.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
---
