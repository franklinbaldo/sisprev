---
type: RegraProposta
id: incapacidade-lce1100-ate-2003-molestia-profissional
schema_version: 1
estado_proposta: elaboracao
origens_legacy:
  - regra-0019
predicados:
  causa_incapacidade: molestia_profissional
  regime: lce1100-incapacidade-ingresso-ate-2003
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente decorre de moléstia profissional, com nexo
      ocupacional reconhecido
    protocolo_verificacao:
      pergunta: >-
        A prova médica e administrativa demonstra incapacidade permanente,
        impossibilidade de readaptação e nexo entre a doença e o trabalho?
      responsavel: junta médica oficial e instrução previdenciária do IPERON
      meio_de_prova: >-
        laudo médico oficial, histórico ocupacional, prontuários, exames e
        apuração administrativa do nexo
      momento: instrução e seleção da regra
      evidencia_exigida: >-
        incapacidade permanente e conclusão fundamentada sobre o nexo
        profissional
    portador_primario: fundamentacao_integral
aplicabilidade_temporal:
  datas_legadas:
    data_adm_ate: 31/12/2003 00:00
    data_direito_apos: 18/10/2021 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-i/ec-103-2019.md
    papel: funda a aposentadoria por incapacidade permanente
  - ref: /dispositivos/lce-1100-2021/art-30-caput/original.md
    papel: inclui moléstia profissional entre as causas qualificadas
  - ref: /dispositivos/lce-1100-2021/art-30-par-13/original.md
    papel: remete as causas qualificadas à média do art. 24
  - ref: /dispositivos/lce-1100-2021/art-24/original.md
    papel: disciplina a base média
  - ref: /dispositivos/lce-1100-2021/art-27-inc-i/original.md
    papel: assegura paridade à coorte de ingresso até 31/12/2003
projecao:
  nome: >-
    Incapacidade permanente · LCE 1.100 · ingresso até 2003 · moléstia
    profissional · média integral · paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: S
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Médio
  fundamentacao_integral: >-
    No curso do processo administrativo, ficou demonstrado que o interessado era
    servidor titular de cargo efetivo e que se encontrava em estado de incapacidade
    permanente para o trabalho, apurada por junta médica oficial mediante laudo, e que
    essa incapacidade decorreu de moléstia profissional, com nexo entre a doença e as
    condições de exercício do cargo reconhecido a partir do histórico ocupacional e da
    avaliação médica oficial. Ficou demonstrado, por fim, que o ingresso no serviço
    público em cargo efetivo se deu até 31 de dezembro de 2003 e que os requisitos foram
    implementados a partir de 18 de outubro de 2021.


    A hipótese se extrai da conjugação dos dispositivos, e é a articulação entre eles
    que a completa. O art. 40, § 1º, inciso I, da Constituição Federal, na redação da
    Emenda Constitucional nº 103/2019, funda a aposentadoria por incapacidade permanente
    para o trabalho. O art. 30, caput, da Lei Complementar Estadual nº 1.100/2021
    estabelece que essa aposentadoria é proporcional ao tempo de contribuição, mas
    excetua da proporcionalização a incapacidade decorrente de acidente em serviço,
    moléstia profissional ou doença grave, contagiosa ou incurável. A moléstia
    profissional é uma dessas causas, e o que a caracteriza é o nexo entre a doença e as
    condições de exercício do cargo, de modo que a apuração desse nexo não é
    formalidade: dela depende o próprio ramo do cálculo. É essa qualificação que afasta
    a fração: sem ela, o mesmo grau de incapacidade levaria a provento reduzido. O § 13
    do mesmo artigo fecha o cálculo, mandando apurá-lo na forma do art. 24 — que
    disciplina sobre que valor o benefício incide — e ressalvando o direito adquirido a
    outra fórmula, o que preserva quem já reunia requisitos sob disciplina anterior.


    Do enquadramento resulta a concessão de proventos calculados sobre a média
    disciplinada no art. 24 da Lei Complementar Estadual nº 1.100/2021, sem redução
    proporcional ao tempo de contribuição, na forma de cálculo vinculada a esta regra.
    Após a concessão, os proventos são reajustados com paridade, na forma do art. 27,
    inciso I, da mesma Lei Complementar, que remete ao art. 7º da Emenda Constitucional
    nº 41/2003 para quem ingressou em cargo efetivo até 31 de dezembro de 2003. A
    paridade é regime de revisão posterior e não integra o cálculo inicial.
proveniencia:
  fontes_consultadas:
    - /formas-calculo/forma-calculo-media-80-contribuicoes-lce1100.md
    - /dispositivos/cf88/art-40-par-1-inc-i/ec-103-2019.md
    - /dispositivos/lce-1100-2021/art-24/original.md
    - /dispositivos/lce-1100-2021/art-27-inc-i/original.md
    - /dispositivos/lce-1100-2021/art-30-caput/original.md
    - /dispositivos/lce-1100-2021/art-30-par-13/original.md
    - LCE 1.100/2021 compilada pela DITEL, consultada em 01/08/2026
  notas: >-
    O § 13 remete ao art. 24 e o art. 27, I, mantém paridade. Moléstia
    profissional é classe jurídica própria e exige aferição humana do nexo.
    Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Individualizar a moléstia profissional e aplicar a fórmula especial do §
      13 sem confundi-la com a regra geral do art. 25.
confianca: media
---

# Síntese

Hipótese da LCE 1.100/2021 para servidor ingressado até 31/12/2003, com
incapacidade decorrente de moléstia profissional. Aplica-se a média do art. 24,
sem proporcionalização, com paridade do art. 27, I.

# Pendências localizadas

- definir o protocolo institucional de reconhecimento do nexo profissional;
- confirmar a projeção operacional da média com paridade no Sisprev;
- resolver Q6-S/Q6-T e completar o gate humano.
