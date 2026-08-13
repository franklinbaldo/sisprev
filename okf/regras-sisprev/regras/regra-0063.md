---
type: Regra
id: regra-0063
row_index: 63
id_sisprev: '113'
nome_original: Voluntária do Servidor Com Deficiência - Art. 35, inciso III da Lei Complementar 1.100/2021 (LEVE)
nome: Voluntária · Deficiência · pedido a partir de 18/10/2021 · integral · média
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
tabelapontuacao: N
requisitos_da_in_no_5_2020: N
relatorio_p_reserva_remunerada_por_idade_ex_officio: N
adicional_inatividade: N
data_adm_ate: 31/12/2099 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 18/10/2021 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria voluntária de servidor com deficiência, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 40, § 4º-A, da Constituição Federal, com redação dada pela Emenda Constitucional nº 103/2019, artigos 25, 27, I; 35, inciso III (deficiência leve), da Lei Complementar nº 1.100/2021 e artigo 40, § 1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019
visivel_dtc_integral: N
sexo: FEMININO
integral: S
tipo_calculo: Valor Médio
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/cf88/art-40-par-4a/ec-103-2019.md
  - /dispositivos/lce-1100-2021/art-25/original.md
  - /dispositivos/lce-1100-2021/art-27-inc-i/original.md
  - /dispositivos/lce-1100-2021/art-35-inc-iii/original.md
disposicao_de_achados:
  - achado: /achados/achado-0020.md
    disposicao: nao_se_aplica
    justificativa: >-
      **`nao_se_aplica` desde 2026-08-13, para o par sexo/nome
      especificamente — as demais dimensões do achado (D1, D3, D4, D5) seguem
      corrigidas como estavam.** A renomeação de 2026-07-30 adicionou `sexo`
      (e, no grupo 0059–0064, o grau de deficiência) como faceta de posição 4,
      respondendo à D2 do achado sob a premissa de que nome idêntico por sexo
      obrigava o operador a abrir o cadastro. Em reunião de 13/08/2026, a
      empresa esclareceu que o Sisprev **já diferencia esses dois critérios
      sozinho, pelo cadastro do requerente**, nos passos seguintes à seleção
      da regra — o operador nunca precisa abrir o cadastro para eles. Sob esse
      fato, a alegação de dano da D2 não procede para sexo e grau de
      deficiência: nome idêntico nesses dois critérios deixa de ser o defeito
      que o achado apontava, e volta a ser a forma correta, unificando a
      escolha do operador nas hipóteses que de fato dependem de leitura
      humana. Registro em Decisão 11 de
      `docs/analysis/decisoes-de-auditoria-2026-07-30.md`. As demais
      dimensões do `achado-0020` (D1 grafia, D3 separador, D4 citação, D5
      rótulo variante) não dependem deste esclarecimento e seguem
      `corrigida` como já estavam.
    decidido_por: franklinbaldo
    decidido_em: 2026-08-13
  - achado: /achados/achado-0003.md
    disposicao: corrigida
    justificativa: >-
      **Corrigida diferenciando a fundamentação, que é o campo que o detector
      lê.** O grupo existia porque `regra-0059` e `regra-0063` gravavam
      `fundamentacao_integral` idêntica — "artigos 25, 27, I; 35" com o art. 35
      achatado —, e o que as separa, o **grau de deficiência**, não tem coluna no
      catálogo: vivia só no `nome`, que está fora da chave material do
      `P2_IGUALDADE_MATERIAL_ATIVA`. Era a lacuna de schema que o `CLAUDE.md`
      descreve, não duplicação.
      Esta regra passou a citar o **inciso III do art. 35 da LCE
      1.100/2021 (deficiência leve)**, e `dispositivos:` aponta a provisão
      correspondente, transcrita no bundle. A irmã do grupo passou a citar o
      inciso dela. O grau saiu do campo que o detector ignora e entrou no que ele
      considera material — é a única correção que dissolve o grupo sem mascarar
      nada.
      **O que a diferenciação afirma, e o que ela não afirma.** Afirma que a
      distinção entre as duas regras é a que o art. 35 faz, com números distintos
      (II = moderada, III = leve), e que o catálogo já a declarava —
      o `nome` importado desta regra nomeava o inciso e o grau, então nada aqui é
      leitura nova sobre o que ela pretende ser. **Não** afirma que o grau passe a
      ser critério aferido pelo sistema: continua sem coluna, e a aferição
      biopsicossocial do *caput* é ato externo ao Sisprev. A diferença entre "a
      regra declara o seu grau" e "o sistema afere o grau" permanece, e a segunda
      metade é lacuna de schema que esta edição não fecha.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
---
