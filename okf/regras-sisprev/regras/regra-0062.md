---
type: Regra
id: regra-0062
row_index: 62
id_sisprev: '112'
nome_original: Voluntária do Servidor Com Deficiência - Art. 35, inciso I da Lei Complementar 1.100/2021 (GRAVE)
nome: Voluntária · Deficiência grave · pedido a partir de 18/10/2021 · Masculino · integral · média
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
fundamentacao_integral: Aposentadoria voluntária de servidor com deficiência, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 40, § 4º-A, da Constituição Federal, com redação dada pela Emenda Constitucional nº 103/2019, artigos 25, 27, I; 35, inciso I (deficiência grave), da Lei Complementar nº 1.100/2021 e artigo 40, § 1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019
visivel_dtc_integral: N
sexo: MASCULINO
integral: S
tipo_calculo: Valor Médio
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/cf88/art-40-par-4a/ec-103-2019.md
  - /dispositivos/lce-1100-2021/art-25/original.md
  - /dispositivos/lce-1100-2021/art-27-inc-i/original.md
  - /dispositivos/lce-1100-2021/art-35-inc-i/original.md
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
      tenha sido tocado, se houver — `nome` está fora da chave material, então
      renomear é incapaz de criar ou dissolver grupo de igualdade material, e o
      baseline de `tests/test_achados_bundle.py` assevera isso; e que a
      padronização deva virar gate, que é a questão 2 do achado e segue aberta.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
  - achado: /achados/achado-0021.md
    disposicao: corrigida
    justificativa: >-
      **Corrigida em dois atos, na ordem que a questão 3 do achado determina.**
      Primeiro o grau: `fundamentacao_integral` desta regra citava "artigos 25,
      27, I; 35" com o art. 35 achatado, e passou a citar o **inciso** que lhe
      corresponde — o I, deficiência grave, 20 anos de contribuição se mulher e
      25 se homem —, com `dispositivos:` apontando `lce-1100-2021/art-35-inc-i`
      em lugar do artigo inteiro. Isso não é leitura nova: o `nome` importado
      desta regra já dizia "Art. 35, inciso I [...] (GRAVE)", e o inciso conferido
      contra a compilação oficial confirma a correspondência. O grau estava
      declarado no único campo que o `P2_IGUALDADE_MATERIAL_ATIVA` não lê, e
      ausente do campo que ele lê.
      Depois a citação falsa: `fundamentacao` continha, na íntegra, "Art. 39,
      paragrafo unico da Lei Complementar 432/2008", e esse parágrafo **não
      existe** — o art. 39 tem nove parágrafos numerados, em todas as suas
      redações, e a conferência está fechada no achado contra a compilação
      oficial. O campo foi **esvaziado**, alinhando esta regra às quatro irmãs do
      mesmo grupo de seis, onde ele sempre esteve vazio.
      **Por que esvaziar não é escolher entre as três hipóteses do achado.**
      Apagar uma citação falsa não afirma qual dispositivo ela pretendia nomear;
      remove uma afirmação jurídica falsa de campo deployável sem pôr outra no
      lugar. A alternativa — deixar como está enquanto se investiga — mantém no
      documento entregue ao servidor a invocação de provisão inexistente, num
      artigo de outro benefício. A pista não se perde: ela está registrada no
      achado e sobrevive em `data/raw/`, imutável.
      A competência para o ato veio da Decisão 10 de
      `docs/analysis/decisoes-de-auditoria-2026-07-30.md`, que autorizou a
      auditoria a alterar `FUNDAMENTACAO*` diretamente na regra. Quando o achado
      foi escrito, a questão 2 dele registrava o contrário, e essa premissa caiu.
      **O que esta correção torna visível, de propósito.** O achado antecipa: a
      citação falsa era a única coisa que mantinha esta regra fora de um grupo
      `P2_IGUALDADE_MATERIAL_ATIVA`, porque `FUNDAMENTACAO*` está dentro da chave
      material e o campo estava preenchido só aqui. Esvaziá-lo sozinho faria as
      seis regras colapsarem em dois grupos de três. É por isso que o grau veio
      primeiro: com o inciso na fundamentação, as seis passam a se distinguir
      pelo critério que a lei de fato usa, e o que se dissolve são os dois grupos
      que já existiam, não um grupo novo que esta edição criaria.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
---
