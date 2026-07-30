---
type: Regra
id: regra-0020
row_index: 20
nome: Incapacidade · ingresso até 31/12/2003, requisitos a partir de 23/10/2021 · Ambos · proporcional · paridade
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
  - achado: /achados/achado-0024.md
    disposicao: encaminhada
    justificativa: >-
      As duas conferências do achado estão fechadas contra fonte oficial
      arquivada, e nenhuma delas depende de hipótese sobre convenção de
      fronteira. `data_direito_apos: 23/10/2021` **não corresponde a marco nenhum**
      da LCE 1.100/2021: a publicação foi no DOE/RO nº 207, de **18/10/2021**,
      identificada na ficha da norma no SAPL/ALE-RO, e o texto da lei não contém a
      expressão "23 de outubro". O valor está cinco dias deslocado, e vinte e duas
      das vinte e seis regras que gravam um marco desta norma gravam 18/10/2021.
      No eixo de admissão esta regra grava `data_adm_ate: 31/12/2003`, que é o
      marco literal da lei e está correto; o defeito de `01/01/2004` é das duas
      regras do outro ramo.
      **Por que não é `corrigida`, mesmo com os valores certos conhecidos.** As
      quatro colunas de data são **critério aferido**, não `nome` nem
      `FUNDAMENTACAO*`. A Decisão 10 de
      `docs/analysis/decisoes-de-auditoria-2026-07-30.md` autorizou a auditoria a
      editar aqueles dois campos na regra e deliberadamente não estendeu a
      autorização — alterar critério continua passando pelo conjunto (RFC 0006),
      porque editar a regra legada apaga o que o operador de fato viu. Aqui a
      distância entre saber e poder é inteira: os dois valores certos estão
      escritos na norma, e nenhum deles pode ser gravado neste documento.
      **Por que não é `nao_se_aplica`.** O defeito é desta regra e está em campo
      que decide seleção — é a coluna de data que determina qual regra alcança um
      requerimento.
      Esta disposição **não** lê `data_direito_ate: 31/12/2099` como "sem limite":
      é sentinela, e a RFC 0011 não fixa a leitura dela. E **não** afirma qual dia
      concreto a janela corrigida passa a cobrir — isso depende da semântica de
      `DATA_DIREITO_APOS`, que segue aberta (Q2), enquanto o deslocamento de cinco
      dias vale sob qualquer convenção.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
    decisao_pendente_de: >-
      IPERON, como titular do produto, quanto ao ato de alterar as colunas de data
      — e a auditoria quanto ao veículo, que é um `Conjunto` com a regra
      substitutiva, não uma edição no documento legado. Fica registrado que a
      questão 3 do achado estreitou-se: a empresa responsável pelo Sisprev
      confirmou que `DATA_ADM_*` é data de admissão
      (`docs/analysis/confirmacoes-do-fornecedor-do-sisprev.md`), o que fixa o
      gênero do marco; se "admissão" é nomeação, posse ou exercício segue sem
      resposta, e é o que decide se o dia descoberto é dano real ou defeito
      formal.
---
