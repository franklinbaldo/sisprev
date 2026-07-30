---
type: Regra
id: regra-0065
row_index: 65
nome: Voluntária · Agentes nocivos · pedido a partir de 31/12/2003 · Ambos · integral · paridade · regra-0065
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
data_adm_ate: 31/12/2099 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 31/12/2003 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria voluntária de servidor exposto a agentes nocivos à saúde, com proventos integrais (cálculo por integralidade) e com paridade, com base nos artigos 25, 27, inciso I, e 41, inciso III, da Lei Complementar Estadual 1.100/2021 e artigo 40, § 1º, inciso III, segunda parte, e § 4°-C, da Constituição Federal, com redação dada pela Emenda Constitucional nº 103/2019 - regra permanente
visivel_dtc_integral: N
sexo: AMBOS
integral: S
tipo_calculo: Valor Médio
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/cf88/art-40-par-4c/ec-103-2019.md
  - /dispositivos/lce-1100-2021/art-25/original.md
  - /dispositivos/lce-1100-2021/art-27-inc-i/original.md
  - /dispositivos/lce-1100-2021/art-41-inc-iii/original.md
disposicao_de_achados:
  - achado: /achados/achado-0057.md
    disposicao: encaminhada
    justificativa: >-
      A contradição é tripla dentro desta regra e está conferida. Os
      `dispositivos:` vinculam `lce-1100-2021/art-25` e
      `lce-1100-2021/art-27-inc-i`; a `fundamentacao_integral` escreve por extenso
      "cálculo por integralidade" e "com paridade"; e os campos `integral: S` e
      `paridade: S` confirmam. Só o `tipo_calculo` destoa, gravando `Valor Médio`,
      que é o regime do **art. 24** — o artigo do outro trilho, que esta regra não
      cita. A `regra-0067` fecha o argumento: `fundamentacao_integral` idêntica
      caractere a caractere, `dispositivos:` idênticos item a item, mesma janela,
      mesmo sexo, e grava `Valor Efetivo`.
      **Por que não é `corrigida`, por dois motivos independentes.** O primeiro é
      de competência: `tipo_calculo` é **critério aferido**, não `nome` nem
      `FUNDAMENTACAO*`, e a Decisão 10 de
      `docs/analysis/decisoes-de-auditoria-2026-07-30.md` não estendeu a
      autorização a mais nenhum campo — alterar critério passa pelo conjunto (RFC
      0006). O segundo é de ordem, e o próprio achado o registra na questão 1:
      esta regra grava `data_adm_ate` sentinela enquanto o art. 25 que ela cita
      alcança só quem ingressou até 31/12/2003, que é o defeito do
      [`achado-0042`](../achados/achado-0042.md). Se o recorte estiver errado, pode
      ser que a regra devesse mesmo estar no trilho do art. 24, e aí o campo a
      corrigir é outro. Responder aquele achado é anterior a mexer neste campo.
      **Por que não é `nao_se_aplica`.** A regra é `simulavel: S` e `tipo_calculo`
      é o campo que orienta o cálculo — ao contrário da fundamentação, que o motor
      não lê. Média das maiores remunerações de 80% do período contributivo e
      totalidade da remuneração no cargo efetivo produzem valores diferentes, e a
      diferença se projeta em todo o benefício.
      Esta disposição **não** afirma que `Valor Efetivo` seja o rótulo
      juridicamente exato da totalidade do art. 25 — o enum legado não identifica
      fórmulas (P16) —, nem que alguma concessão tenha saído a menor.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
    decisao_pendente_de: >-
      A auditoria, quanto à ordem: o `achado-0042` decide o recorte de admissão
      desta regra e é anterior a propor valor de `tipo_calculo`. E o IPERON, como
      titular do produto, quanto ao ato sobre o campo — que, sendo critério
      aferido, tem por veículo um `Conjunto` com a regra substitutiva, não uma
      edição no documento legado.
---
