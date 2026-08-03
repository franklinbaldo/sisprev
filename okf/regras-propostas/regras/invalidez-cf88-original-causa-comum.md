---
type: RegraProposta
id: invalidez-cf88-original-causa-comum
schema_version: 1
estado_proposta: elaboracao
origens_legacy:
  - regra-0001
  - regra-0002
predicados:
  causa_incapacidade: causa_comum
  regime: cf88-original-direito-adquirido
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente não decorre de acidente em serviço, moléstia
      profissional nem doença catalogada na norma aplicável
    protocolo_verificacao:
      pergunta: >-
        Há prova suficiente para excluir as classes qualificadas e enquadrar o
        caso no ramo residual proporcional?
      responsavel: junta médica oficial e instrução previdenciária do IPERON
      meio_de_prova: >-
        laudo médico oficial, prontuários, histórico ocupacional, apuração de
        eventual acidente e rol legal vigente
      momento: instrução e seleção da regra
      evidencia_exigida: >-
        incapacidade permanente comprovada e investigação suficiente das causas
        qualificadas; silêncio ou prova insuficiente não bastam
    portador_primario: fundamentacao_proporcional
aplicabilidade_temporal:
  datas_legadas:
    data_direito_apos: 05/10/1988 00:00
    data_direito_ate: 16/12/1998 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-inc-i/original.md
    papel: define a invalidez permanente e o ramo proporcional residual
  - ref: /dispositivos/cf88/art-40-par-4/original.md
    papel: funda a paridade como regime de revisão dos proventos
  - ref: /dispositivos/ec-20-1998/art-3-caput/original.md
    papel: preserva a concessão pelos critérios anteriores para direito adquirido
projecao:
  nome: Invalidez · CF/88 original · demais causas · proporcional · paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: S
  sexo: AMBOS
  integral: N
  tipo_calculo: Valor Efetivo
  fundamentacao_proporcional: >-
    No curso do processo administrativo, ficou demonstrado que o interessado era
    servidor titular de cargo efetivo e que se encontra em estado de invalidez
    permanente, tendo sido igualmente demonstrado que essa invalidez não decorreu de
    acidente em serviço, de moléstia profissional nem de doença grave, contagiosa ou
    incurável especificada em lei; a incapacidade permanente e a exclusão das causas
    qualificadas foram apuradas por junta médica oficial e pela instrução
    previdenciária do IPERON, mediante laudo médico oficial, prontuários, histórico
    ocupacional, apuração de eventual acidente e o rol legal vigente, tendo sido
    exigidas conclusão médica de incapacidade permanente e investigação suficiente
    das causas qualificadas. Ficou também demonstrado que os requisitos foram
    integralmente cumpridos até 15/12/1998, véspera da publicação da Emenda
    Constitucional nº 20/1998.

    Esses requisitos se extraem da conjugação de três dispositivos. O art. 40,
    inciso I, da Constituição Federal em seu texto original determina a aposentadoria
    por invalidez permanente e atribui proventos proporcionais aos casos que não se
    enquadram nas três causas qualificadas, sendo dele que se retiram a permanência e
    o ramo residual proporcional. O art. 40, § 4º, do mesmo texto funda a paridade,
    ao determinar a revisão dos proventos na mesma proporção e data da remuneração
    dos servidores em atividade. O art. 3º da Emenda Constitucional nº 20/1998
    preserva a concessão, pelos critérios anteriores, a quem cumpriu os requisitos
    até a publicação da emenda.

    Do enquadramento nas demais causas resulta a concessão de proventos
    proporcionais, mediante aplicação de fração relacionada ao tempo sobre a base
    remuneratória juridicamente aplicável, nos termos do art. 40, inciso I, da
    Constituição Federal em sua redação original. A forma de cálculo vinculada
    identifica a base e o ajuste proporcional; a composição concreta da base, o
    denominador e a conversão operacional do tempo serão apurados segundo a
    legislação estadual vigente na data do direito, sem que esta fundamentação
    antecipe parâmetro ainda não identificado. A paridade decorre do art. 40, § 4º,
    da mesma redação e opera como regime de revisão posterior.
proveniencia:
  fontes_consultadas:
    - /formas-calculo/forma-calculo-remuneracao-cargo-proporcional-cf88-original.md
    - /dispositivos/cf88/art-40-inc-i/original.md
    - /dispositivos/cf88/art-40-par-4/original.md
    - /dispositivos/ec-20-1998/art-3-caput/original.md
    - >-
      legislação estadual vigente na data de implementação dos requisitos: LC
      1/1984, LC 39/1990 ou LC 68/1992
    - docs/analysis/base-normativa-invalidez-incapacidade.md
  notas: >-
    A forma proporcional está identificada; permanecem pendentes a composição
    concreta da base, a medida da fração e a conversão operacional do tempo em
    cada trecho da janela. A ausência de informação não equivale a causa comum.
    Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Substituir a regra proporcional legada por unidade com fundamento e
      protocolo próprios.
confianca: media
---

# Síntese

Hipótese residual de invalidez proporcional sob CF/88 original. A forma de
cálculo já está diferenciada e vinculada: base remuneratória com ajuste
proporcional ao tempo. O detalhe numérico da fração permanece pendente de cotejo
da legislação estadual temporalmente aplicável.

# Pendências localizadas

- fechar a composição da base e a medida da fração em cada trecho da janela,
  mediante cotejo da LC 1/1984, LC 39/1990 e LC 68/1992;
- parametrizar forma de cálculo fiel no Sisprev;
- confirmar o fluxo operacional de classificação da causa.
