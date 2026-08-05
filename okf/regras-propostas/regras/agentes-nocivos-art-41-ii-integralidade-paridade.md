---
type: RegraProposta
id: agentes-nocivos-art-41-ii-integralidade-paridade
ciclo: ciclo-06
schema_version: 1
estado_auditoria: preview
origens_legacy:
  - regra-0065
  - regra-0066
  - regra-0067
predicados:
  regime: lce-1100-2021
  marco_ingresso: ate-2003
  faixa_exposicao: 76-pontos-20-anos
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      o servidor tomou posse em cargo efetivo até 31/12/2003, não optou pelo
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
    data_adm_apos: 01/01/1950 00:00
    data_adm_ate: 31/12/2003 00:00
    data_direito_apos: 18/10/2021 00:00
    data_direito_ate: 31/12/2099 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
    papel: remissão dos requisitos da aposentadoria voluntária à lei complementar do ente
  - ref: /dispositivos/cf88/art-40-par-4c/ec-103-2019.md
    papel: autorização de requisitos diferenciados por exposição efetiva a agentes nocivos
  - ref: /dispositivos/lce-1100-2021/art-25/original.md
    papel: totalidade da remuneração e corte de ingresso até 31/12/2003
  - ref: /dispositivos/lce-1100-2021/art-27-inc-i/original.md
    papel: paridade e o mesmo corte de ingresso
  - ref: /dispositivos/lce-1100-2021/art-41-inc-ii/original.md
    papel: 76 pontos e 20 anos de exposição, além dos requisitos do caput
projecao:
  nome: Voluntária · agentes nocivos · ingresso até 31/12/2003 · 76 pontos e 20 anos de exposição · integral · paridade
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
  fundamentacao_proporcional: ''
  visivel_dtc_proporcional: N
  fundamentacao_integral: >-
    Aposentadoria voluntária de servidor exposto de forma efetiva e permanente
    a agentes nocivos à saúde, mediante comprovação de 20 anos de serviço
    público, 5 anos no cargo, 76 pontos e 20 anos de exposição, para servidor
    ingressado em cargo efetivo até 31/12/2003 que não tenha optado pelo regime
    do art. 40, § 16, da Constituição Federal, com totalidade da remuneração no
    cargo efetivo e paridade, nos termos dos arts. 25, 27, I, e 41, II, da LCE
    1.100/2021 e do art. 40, §§ 1º, III, e 4º-C, da Constituição Federal.
  visivel_dtc_integral: N
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Efetivo
  fundamentacao: ''
proveniencia:
  fontes_consultadas:
    - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
    - /dispositivos/cf88/art-40-par-4c/ec-103-2019.md
    - /dispositivos/lce-1100-2021/art-25/original.md
    - /dispositivos/lce-1100-2021/art-27-inc-i/original.md
    - /dispositivos/lce-1100-2021/art-41-inc-ii/original.md
    - fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt
    - docs/analysis/relatorio-residual-agentes-nocivos.md
    - https://diof.ro.gov.br/data/uploads/2022/07/Doe-20-07-2022.pdf
  notas: >-
    A unidade completa a faixa do inciso II omitida no legado. `Valor Efetivo`
    é hipótese de projeção; a unidade permanece em preview até a confirmação
    do código que executa a totalidade da remuneração do art. 25.
decisoes:
  - data: 2026-07-30
    quem: franklinbaldo
    o_que: >-
      Decompor as origens em uma unidade própria para a faixa fixa de 76 pontos
      e 20 anos de exposição, sem alterar o catálogo vigente.
  - data: '2026-07-30'
    quem: franklinbaldo
    o_que: >-
      Registrar a unidade de atomicidade desta proposta (RFC 0004, round 11):
      três origens (regra-0065, regra-0066, regra-0067), três destinos, 1:1
      cada. regra-0065 e regra-0066 são materialmente idênticas, e regra-0067
      difere apenas no membro de tipo_calculo; todas citam somente o inciso
      III do art. 41. Os três destinos corrigem as janelas, explicitam as três
      faixas dos incisos I-III do art. 41 e adotam tabelapontuacao: N, porque
      os somatórios são fixos. Irmãs:
      agentes-nocivos-art-41-{i,ii,iii}-integralidade-paridade. Antes
      registrado no Conjunto proposta-auditoria-2026-07 (retirado).
confianca: media
---

# Síntese

O inciso II do art. 41 é hipótese legal autônoma e não há fonte que autorize sua
omissão. Esta unidade completa o ramo de ingresso até 31/12/2003 e explicita a
faixa no predicado, ausente do schema legado.

Permanece em `preview` somente porque o significado operacional de
`tipo_calculo: Valor Efetivo` ainda não está documentado. As datas, a faixa,
`tabelapontuacao: N`, integralidade, paridade e o protocolo documental estão
conferidos.
