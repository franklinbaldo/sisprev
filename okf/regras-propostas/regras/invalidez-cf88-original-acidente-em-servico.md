---
type: RegraProposta
id: invalidez-cf88-original-acidente-em-servico
schema_version: 1
estado_proposta: elaboracao
origens_legacy:
  - regra-0001
  - regra-0002
predicados:
  causa_incapacidade: acidente_em_servico
  regime: cf88-original-direito-adquirido
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente decorre de acidente em serviço, com nexo causal
      reconhecido
    protocolo_verificacao:
      pergunta: >-
        A prova médica e administrativa demonstra incapacidade permanente e
        nexo causal com acidente em serviço?
      responsavel: junta médica oficial e instrução previdenciária do IPERON
      meio_de_prova: >-
        laudo médico oficial, comunicação e apuração do acidente, prontuários e
        assentamentos funcionais
      momento: instrução e seleção da regra
      evidencia_exigida: >-
        conclusão médica de incapacidade permanente e ato ou conjunto
        probatório que reconheça o nexo com o serviço
    portador_primario: fundamentacao_integral
aplicabilidade_temporal:
  datas_legadas:
    data_direito_apos: 05/10/1988 00:00
    data_direito_ate: 16/12/1998 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-inc-i/original.md
    papel: define as classes de causa e os ramos integral e proporcional
projecao:
  nome: Invalidez · CF/88 original · acidente em serviço · integral · paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: S
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Efetivo
  fundamentacao_integral: >-
    No curso do processo administrativo, ficou demonstrado que o interessado era
    servidor titular de cargo efetivo, que se encontra em estado de invalidez
    permanente e que essa invalidez decorreu de acidente em serviço, com nexo causal
    reconhecido; a incapacidade permanente e o nexo foram apurados por junta médica
    oficial e pela instrução previdenciária do IPERON, mediante laudo médico
    oficial, comunicação e apuração do acidente, prontuários e assentamentos
    funcionais, tendo sido exigidas conclusão médica de incapacidade permanente e
    ato ou conjunto probatório que reconhecesse o nexo com o serviço. Ficou
    igualmente demonstrado que os requisitos foram integralmente cumpridos até
    15/12/1998, véspera da publicação da Emenda Constitucional nº 20/1998.

    Esses requisitos se extraem da conjugação de três dispositivos, cada um fundando
    uma parte da hipótese. O art. 40, inciso I, da Constituição Federal em seu texto
    original determina a aposentadoria do servidor por invalidez permanente e, no
    mesmo inciso, distingue os ramos do cálculo: reserva os proventos integrais às
    invalidezes decorrentes de acidente em serviço, moléstia profissional ou doença
    grave, contagiosa ou incurável especificada em lei, e atribui proventos
    proporcionais nos demais casos — dele se retiram a exigência de permanência da
    invalidez, a do nexo com o serviço e o efeito de integralidade. O art. 40, § 4º,
    do mesmo texto original assegura que os proventos serão revistos na mesma
    proporção e na mesma data em que se modificar a remuneração dos servidores em
    atividade, e é dele que decorre a paridade. E o art. 3º da Emenda Constitucional
    nº 20/1998 assegura a concessão, a qualquer tempo, a quem tenha cumprido os
    requisitos até a data de sua publicação, pelos critérios da legislação então
    vigente, sendo esse o dispositivo que permite aplicar o texto original depois de
    sua revogação.

    Do reconhecimento do acidente em serviço resulta a concessão de proventos
    integrais, sem redução proporcional ao tempo de contribuição, com base na
    totalidade da remuneração do cargo efetivo em que se deu a aposentadoria, nos
    termos do art. 40, inciso I, da Constituição Federal em sua redação original. A
    paridade em relação aos servidores em atividade decorre do art. 40, § 4º, da
    mesma redação, e opera como regime de revisão posterior à concessão, não como
    elemento do cálculo inicial.
proveniencia:
  fontes_consultadas:
    - /formas-calculo/forma-calculo-totalidade-remuneracao-cargo-efetivo-cf88-original.md
    - /dispositivos/cf88/art-40-inc-i/original.md
    - EC 20/1998, art. 3º — preservação do direito adquirido
    - >-
      legislação estadual vigente na data de implementação dos requisitos: LC
      1/1984, LC 39/1990 ou LC 68/1992
    - docs/analysis/base-normativa-invalidez-incapacidade.md
  notas: >-
    A legislação estadual e o rol de doenças são apurados na versão vigente na
    data de implementação dos requisitos. A mudança de diploma, sem alteração
    demonstrada de critério ou efeito, não cria por si só outra regra. Origem
    material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Decompor o Bloco A por regime constitucional e classe de causa, com uma
      hipótese material por unidade.
confianca: media
---

# Síntese

Hipótese de invalidez sob CF/88 original por acidente em serviço. A seleção
exige prova positiva da causa; ausência de informação não autoriza enquadramento
em `causa_comum`.

# Pendências localizadas

- transcrever os dispositivos estaduais temporalmente aplicáveis;
- confirmar a projeção da forma de cálculo no Sisprev;
- confirmar o fluxo operacional de classificação da causa.
