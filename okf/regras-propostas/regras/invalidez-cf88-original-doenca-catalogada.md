---
type: RegraProposta
id: invalidez-cf88-original-doenca-catalogada
schema_version: 1
estado_proposta: elaboracao
origens_legacy:
  - regra-0001
  - regra-0002
predicados:
  causa_incapacidade: doenca_catalogada
  regime: cf88-original-direito-adquirido
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente decorre de doença grave, contagiosa ou
      incurável incluída no rol legal vigente na data do direito
    protocolo_verificacao:
      pergunta: >-
        O diagnóstico causador da incapacidade consta do rol legal vigente
        quando os requisitos foram implementados?
      responsavel: junta médica oficial e instrução previdenciária do IPERON
      meio_de_prova: >-
        laudo médico oficial, exames, prontuários e texto legal do rol vigente
        na data do direito
      momento: instrução e seleção da regra
      evidencia_exigida: >-
        diagnóstico confirmado, incapacidade permanente e correspondência
        expressa com o rol legal temporalmente aplicável
    portador_primario: fundamentacao_integral
aplicabilidade_temporal:
  datas_legadas:
    data_direito_apos: 05/10/1988 00:00
    data_direito_ate: 16/12/1998 00:00
  versao_rol: norma-estadual-vigente-na-data-do-direito
taxonomias:
  - ref: /dispositivos/cf88/art-40-inc-i/original.md
    papel: condiciona o ramo integral à doença grave especificada em lei
  - ref: /dispositivos/cf88/art-40-par-4/original.md
    papel: funda a paridade como regime de revisão dos proventos
  - ref: /dispositivos/ec-20-1998/art-3-caput/original.md
    papel: preserva a concessão pelos critérios anteriores para direito adquirido
  - ref: /dispositivos/lce-39-1990/art-156/original.md
    papel: fixa a base no vencimento do cargo acrescido do adicional por tempo e de outras vantagens pecuniárias no período da LCE 39/1990
  - ref: /dispositivos/lce-68-1992/art-236/original.md
    papel: mantém a composição da base no período da LCE 68/1992, dizendo "por tempo de serviço" onde o art. 156 dizia "por tempo"
projecao:
  nome: Invalidez · CF/88 original · doença grave catalogada · integral · paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: S
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Efetivo
  fundamentacao_integral: >-
    No curso do processo administrativo, ficou demonstrado que o interessado era servidor
    titular de cargo efetivo, que se encontrava em estado de invalidez permanente e que a
    doença causadora da incapacidade era grave, contagiosa ou incurável e estava especificada
    no rol legal vigente na data do direito; o diagnóstico, a incapacidade e a correspondência
    com o rol foram apurados por junta médica oficial e pela instrução previdenciária do IPERON,
    mediante laudo médico oficial, exames, prontuários e o texto legal temporalmente aplicável.
    Ficou igualmente demonstrado que os requisitos foram integralmente cumpridos até 15/12/1998,
    véspera da publicação da Emenda Constitucional nº 20/1998.

    Esses requisitos se extraem da conjugação de três dispositivos. O art. 40, inciso I, da
    Constituição Federal em seu texto original determina a aposentadoria por invalidez permanente
    e reserva os proventos integrais à doença grave, contagiosa ou incurável especificada
    em lei, sendo dele que se retiram a permanência, a exigência de catalogação legal e o
    ramo integral. O art. 40, § 4º, do mesmo texto funda a paridade, ao determinar a revisão
    dos proventos na mesma proporção e data da remuneração dos servidores em atividade. O
    art. 3º da Emenda Constitucional nº 20/1998 preserva a concessão, pelos critérios anteriores,
    a quem cumpriu os requisitos até a publicação da emenda.

    Do enquadramento da doença no rol legal aplicável resulta a concessão de proventos integrais,
    sem redução proporcional ao tempo, segundo a forma de cálculo fundada no art. 40, inciso
    I, da Constituição Federal em sua redação original. A base inicial corresponde ao vencimento
    do cargo, acrescido da gratificação adicional por tempo e de outras vantagens
    pecuniárias, conforme o estatuto estadual vigente na data de implementação do direito.
    Nos períodos já transcritos no bundle, essa composição resulta do art. 156 da Lei Complementar
    Estadual nº 39/1990 e do art. 236 da Lei Complementar Estadual nº 68/1992. A paridade
    decorre do art. 40, § 4º, da mesma redação e opera como regime de revisão posterior.
proveniencia:
  fontes_consultadas:
    - /formas-calculo/forma-calculo-totalidade-remuneracao-cargo-efetivo-cf88-original.md
    - /dispositivos/cf88/art-40-inc-i/original.md
    - /dispositivos/cf88/art-40-par-4/original.md
    - /dispositivos/ec-20-1998/art-3-caput/original.md
    - >-
      legislação estadual vigente na data de implementação dos requisitos: LC
      1/1984, LC 39/1990 ou LC 68/1992
    - docs/analysis/base-normativa-invalidez-incapacidade.md
    - /dispositivos/lce-39-1990/art-156/original.md
    - /dispositivos/lce-68-1992/art-236/original.md
  notas: >-
    O rol e a composição concreta da base remuneratória são apurados nas versões
    vigentes na data do direito. Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Decompor o Bloco A por regime constitucional e classe de causa e manter o
      rol como taxonomia temporal.
confianca: media
---

# Síntese

Hipótese de invalidez sob CF/88 original por doença grave catalogada. A
correspondência ao rol deve ser verificada na versão vigente quando o direito
foi implementado.

# Pendências localizadas

- transcrever os rols estaduais temporalmente aplicáveis;
- transcrever o dispositivo equivalente da LC 1/1984 para completar a cobertura temporal da base;
- confirmar a projeção da forma de cálculo no Sisprev;
- confirmar o fluxo operacional de classificação da causa.
