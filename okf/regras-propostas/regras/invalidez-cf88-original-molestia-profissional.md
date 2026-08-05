---
type: RegraProposta
id: invalidez-cf88-original-molestia-profissional
ciclo: ciclo-09
schema_version: 1
estado_auditoria: elaboracao
origens_legacy:
  - regra-0001
  - regra-0002
predicados:
  causa_incapacidade: molestia_profissional
  regime: cf88-original-direito-adquirido
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente decorre de moléstia profissional, com nexo
      ocupacional reconhecido
    protocolo_verificacao:
      pergunta: >-
        A prova médica e ocupacional demonstra incapacidade permanente e nexo
        entre a moléstia e o trabalho?
      responsavel: junta médica oficial e instrução previdenciária do IPERON
      meio_de_prova: >-
        laudo médico oficial, histórico ocupacional, prontuários, laudo
        ambiental e assentamentos funcionais
      momento: instrução e seleção da regra
      evidencia_exigida: >-
        conclusão médica de incapacidade permanente e prova suficiente do nexo
        ocupacional
    portador_primario: fundamentacao_integral
aplicabilidade_temporal:
  datas_legadas:
    data_direito_apos: 05/10/1988 00:00
    data_direito_ate: 16/12/1998 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-inc-i/original.md
    papel: define a invalidez permanente, a moléstia profissional e o ramo integral
  - ref: /dispositivos/cf88/art-40-par-4/original.md
    papel: funda a paridade como regime de revisão dos proventos
  - ref: /dispositivos/ec-20-1998/art-3-caput/original.md
    papel: preserva a concessão pelos critérios anteriores para direito adquirido
  - ref: /dispositivos/lce-39-1990/art-156/original.md
    papel: fixa a base no vencimento do cargo acrescido do adicional por tempo e de outras vantagens pecuniárias no período da LCE 39/1990
  - ref: /dispositivos/lce-68-1992/art-236/original.md
    papel: mantém a composição da base no período da LCE 68/1992, dizendo "por tempo de serviço" onde o art. 156 dizia "por tempo"
projecao:
  nome: Invalidez · CF/88 original · moléstia profissional · integral · paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: S
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Efetivo
  fundamentacao_integral: >-
    No curso do processo administrativo, ficou demonstrado que o interessado era servidor
    titular de cargo efetivo, que se encontrava em estado de invalidez permanente e que essa
    invalidez decorreu de moléstia profissional, com nexo ocupacional reconhecido; a incapacidade
    e o nexo foram apurados por junta médica oficial e pela instrução previdenciária do IPERON,
    mediante laudo médico oficial, histórico ocupacional, prontuários, laudo ambiental e assentamentos
    funcionais, tendo sido exigidas conclusão médica de incapacidade permanente e prova suficiente
    do nexo entre a moléstia e o trabalho. Ficou igualmente demonstrado que os requisitos
    foram integralmente cumpridos até 15/12/1998, véspera da publicação da Emenda Constitucional
    nº 20/1998.

    Esses requisitos se extraem da conjugação de três dispositivos. O art. 40, inciso I, da
    Constituição Federal em seu texto original determina a aposentadoria por invalidez permanente
    e reserva os proventos integrais às invalidezes decorrentes de moléstia profissional,
    sendo dele que se retiram a permanência, o nexo ocupacional e o ramo integral. O art.
    40, § 4º, do mesmo texto funda a paridade, ao determinar a revisão dos proventos na mesma
    proporção e data da remuneração dos servidores em atividade. O art. 3º da Emenda Constitucional
    nº 20/1998 preserva a concessão, pelos critérios anteriores, a quem cumpriu os requisitos
    até a publicação da emenda.

    Do reconhecimento da moléstia profissional resulta a concessão de proventos integrais,
    sem redução proporcional ao tempo, segundo a forma de cálculo fundada no art. 40, inciso
    I, da Constituição Federal em sua redação original. A base inicial corresponde ao vencimento
    do cargo, acrescido da gratificação adicional por tempo e de outras vantagens
    pecuniárias, conforme o estatuto estadual vigente na data de implementação do direito.
    Nos períodos regidos por essas normas, essa composição resulta do art. 156 da Lei Complementar
    Estadual nº 39/1990 e do art. 236 da Lei Complementar Estadual nº 68/1992. A paridade
    decorre do art. 40, § 4º, da mesma redação e opera como regime de revisão posterior.
proveniencia:
  fontes_consultadas:
    - /tipos-calculo/tipo-calculo-totalidade-remuneracao-cargo-efetivo-cf88-original.md
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
    A composição concreta da base remuneratória é apurada pela legislação
    estadual vigente na data do direito. Mudança apenas de fonte não cria outra
    regra. Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Decompor o Bloco A por regime constitucional e classe de causa, com uma
      hipótese material por unidade.
confianca: media
---

# Síntese

Hipótese de invalidez sob CF/88 original por moléstia profissional. A seleção
exige prova positiva do nexo ocupacional.

# Pendências localizadas

- [ ] transcrever o dispositivo equivalente da LC 1/1984 para completar a cobertura temporal da base;
- [ ] confirmar a projeção da forma de cálculo no Sisprev;
- [ ] confirmar o fluxo operacional de classificação da causa.
