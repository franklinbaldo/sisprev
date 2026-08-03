---
type: RegraProposta
id: agentes-nocivos-art-41-ii-media-sem-paridade
schema_version: 1
estado_proposta: deployable
origens_legacy:
  - regra-0071
predicados:
  regime: lce-1100-2021
  marco_ingresso: apos-2003
  faixa_exposicao: 76-pontos-20-anos
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      o servidor tomou posse em cargo efetivo após 31/12/2003, não optou pelo
      regime do art. 40, § 16, da Constituição Federal, cumpriu 20 anos de
      serviço público e 5 anos no cargo, somou 76 pontos e comprovou 20 anos
      de exposição efetiva e permanente a agentes nocivos
    protocolo_verificacao:
      pergunta: >-
        Os assentamentos funcionais e previdenciários e a prova técnica
        demonstram todos os requisitos da regra?
      responsavel: >-
        órgão de pessoal e responsável pelos assentamentos funcionais na
        origem, com conferência da equipe de atendimento do IPERON
      meio_de_prova: >-
        assentamentos funcionais e previdenciários, PPP e, conforme o período,
        formulário e laudo técnico de condições ambientais
      momento: instrução e conferência do processo concessório
      evidencia_exigida: >-
        termo de posse, registros de tempo e opção previdenciária e prova
        técnica da exposição exigida pelo art. 42 da LCE 1.100/2021
    portador_primario: fundamentacao_integral
aplicabilidade_temporal:
  datas_legadas:
    data_adm_apos: 31/12/2003 00:00
    data_adm_ate: 31/12/2099 00:00
    data_direito_apos: 18/10/2021 00:00
    data_direito_ate: 31/12/2099 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
    papel: remissão dos requisitos da aposentadoria voluntária à lei complementar do ente
  - ref: /dispositivos/cf88/art-40-par-4c/ec-103-2019.md
    papel: autorização de requisitos diferenciados por exposição efetiva a agentes nocivos
  - ref: /dispositivos/lce-1100-2021/art-24/original.md
    papel: média das maiores remunerações e corte de ingresso após 31/12/2003
  - ref: /dispositivos/lce-1100-2021/art-27-inc-ii/original.md
    papel: reajuste nos termos do RGPS e o mesmo corte de ingresso
  - ref: /dispositivos/lce-1100-2021/art-41-inc-ii/original.md
    papel: 76 pontos e 20 anos de exposição, além dos requisitos do caput
projecao:
  nome: Voluntária · agentes nocivos · ingresso após 31/12/2003 · 76 pontos e 20 anos de exposição · média · sem paridade
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
  fundamentacao_proporcional: ''
  visivel_dtc_proporcional: N
  fundamentacao_integral: >-
    Aposentadoria voluntária de servidor exposto de forma efetiva e permanente
    a agentes nocivos à saúde, mediante comprovação de 20 anos de serviço
    público, 5 anos no cargo, 76 pontos e 20 anos de exposição, para servidor
    ingressado em cargo efetivo após 31/12/2003 que não tenha optado pelo regime
    do art. 40, § 16, da Constituição Federal, com proventos integrais
    calculados pela média das maiores remunerações correspondentes a 80% do
    período contributivo e reajuste pelo RGPS, sem paridade, nos termos dos
    arts. 24, 27, II, e 41, II, da LCE 1.100/2021 e do art. 40, §§ 1º, III, e
    4º-C, da Constituição Federal.
  visivel_dtc_integral: N
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Médio
  fundamentacao: ''
proveniencia:
  fontes_consultadas:
    - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
    - /dispositivos/cf88/art-40-par-4c/ec-103-2019.md
    - /dispositivos/lce-1100-2021/art-24/original.md
    - /dispositivos/lce-1100-2021/art-27-inc-ii/original.md
    - /dispositivos/lce-1100-2021/art-41-inc-ii/original.md
    - fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt
    - docs/analysis/relatorio-residual-agentes-nocivos.md
    - https://diof.ro.gov.br/data/uploads/2022/07/Doe-20-07-2022.pdf
  notas: >-
    A unidade completa a faixa do inciso II omitida no legado. Cálculo pela
    média e ausência de paridade decorrem diretamente dos arts. 24 e 27, II.
decisoes:
  - data: 2026-07-30
    quem: franklinbaldo
    o_que: >-
      Decompor regra-0071 em uma unidade própria para a faixa fixa de 76 pontos
      e 20 anos de exposição e considerá-la deployable, mantendo o grupo
      inativo.
confianca: alta
---

# Síntese

O inciso II do art. 41 é hipótese legal autônoma e não há fonte que autorize sua
omissão. Esta unidade completa o ramo pós-2003, explicita a faixa no predicado e
preserva o cálculo pela média e a ausência de paridade determinados pelos arts.
24 e 27, II.

A unidade é `deployable`, mas o grupo de substituição continua inativo; não há
efeito sobre o catálogo vigente.
