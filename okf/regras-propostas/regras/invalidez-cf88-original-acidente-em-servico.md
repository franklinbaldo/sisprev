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
    permanente e que essa invalidez decorreu de acidente em serviço, com nexo
    causal reconhecido; a incapacidade permanente e o nexo foram apurados por junta
    médica oficial e pela instrução previdenciária do IPERON, mediante laudo médico oficial, comunicação e apuração do acidente,
    prontuários e assentamentos funcionais, tendo sido exigidas conclusão médica de
    incapacidade permanente e ato ou conjunto probatório que reconhecesse o nexo com
    o serviço. Ficou igualmente demonstrado que o direito foi implementado antes de
    16/12/1998, data em que entrou em vigor a Emenda Constitucional nº 20/1998, de
    modo que a concessão se rege pelo texto original do art. 40 da Constituição
    Federal, por direito adquirido.

    Todos esses requisitos se extraem do art. 40, inciso I, da Constituição Federal
    em seu texto original, que determina a aposentadoria do servidor por invalidez
    permanente e, no mesmo inciso, distingue os ramos do cálculo: reserva os
    proventos integrais às invalidezes decorrentes de acidente em serviço, moléstia
    profissional ou doença grave, contagiosa ou incurável especificada em lei, e
    atribui proventos proporcionais nos demais casos. É desse mesmo dispositivo que
    se retira o requisito da permanência da invalidez, a exigência do nexo com o
    serviço e o efeito de integralidade aqui reconhecido, sem que outra norma
    precise ser invocada para completar a hipótese.

    Do reconhecimento do acidente em serviço resulta o cálculo dos proventos pela
    totalidade da remuneração do cargo efetivo em que se deu a aposentadoria, sem
    qualquer redução proporcional ao tempo de contribuição, e com paridade em
    relação aos servidores em atividade. O fundamento desse cálculo é o próprio art.
    40, inciso I, da Constituição Federal em sua redação original, na parte em que
    qualifica como integrais os proventos das invalidezes decorrentes de acidente em
    serviço.
proveniencia:
  fontes_consultadas:
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
