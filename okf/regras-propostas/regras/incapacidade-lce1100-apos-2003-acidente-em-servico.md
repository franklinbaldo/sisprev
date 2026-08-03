---
type: RegraProposta
id: incapacidade-lce1100-apos-2003-acidente-em-servico
schema_version: 1
estado_proposta: elaboracao
origens_legacy:
  - regra-0022
predicados:
  causa_incapacidade: acidente_em_servico
  regime: lce1100-incapacidade-ingresso-apos-2003
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente decorre de acidente em serviço, com nexo causal
      reconhecido
    protocolo_verificacao:
      pergunta: >-
        A prova médica e administrativa demonstra incapacidade permanente,
        impossibilidade de readaptação e nexo causal com acidente em serviço?
      responsavel: junta médica oficial e instrução previdenciária do IPERON
      meio_de_prova: >-
        laudo médico oficial, comunicação e apuração do acidente, prontuários e
        assentamentos funcionais
      momento: instrução e seleção da regra
      evidencia_exigida: >-
        incapacidade permanente comprovada e ato ou conjunto probatório que
        reconheça o nexo com o serviço
    portador_primario: fundamentacao_integral
aplicabilidade_temporal:
  datas_legadas:
    data_adm_apos: 01/01/2004 00:00
    data_direito_apos: 18/10/2021 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-i/ec-103-2019.md
    papel: funda a aposentadoria por incapacidade permanente
  - ref: /dispositivos/lce-1100-2021/art-30-caput/original.md
    papel: separa causas qualificadas e causa comum
  - ref: /dispositivos/lce-1100-2021/art-30-par-5/original.md
    papel: define acidente em serviço
  - ref: /dispositivos/lce-1100-2021/art-30-par-13/original.md
    papel: remete as causas qualificadas à média do art. 24
  - ref: /dispositivos/lce-1100-2021/art-24/original.md
    papel: disciplina a base média
  - ref: /dispositivos/lce-1100-2021/art-27-inc-ii/original.md
    papel: determina reajuste sem paridade para ingresso após 31/12/2003
projecao:
  nome: >-
    Incapacidade permanente · LCE 1.100 · ingresso após 2003 · acidente em
    serviço · média integral · sem paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: N
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Médio
  fundamentacao_integral: >-
    No curso do processo administrativo, ficou demonstrado que o interessado era servidor
    titular de cargo efetivo e que a incapacidade permanente decorria de acidente em serviço,
    com nexo causal reconhecido; a verificação foi realizada por junta médica oficial e instrução
    previdenciária do IPERON, mediante laudo médico oficial, comunicação e apuração do acidente,
    prontuários e assentamentos funcionais, tendo sido exigida a seguinte evidência: incapacidade
    permanente comprovada e ato ou conjunto probatório que reconheça o nexo com o serviço.
    Ficou também demonstrado que os requisitos foram implementados em 18/10/2021 ou depois
    e que o ingresso no serviço público ocorreu em 01/01/2004 ou depois.


    A hipótese e seus efeitos resultam da conjugação dos dispositivos aplicáveis. O art. 40,
    § 1º, inciso I, da Constituição Federal, na redação da EC 103/2019 funda a aposentadoria
    por incapacidade permanente. O art. 30, caput, da Lei Complementar Estadual nº 1.100/2021
    separa causas qualificadas e causa comum. O art. 30, § 5º, da Lei Complementar Estadual
    nº 1.100/2021 define acidente em serviço. O art. 30, § 13, da Lei Complementar Estadual
    nº 1.100/2021 remete as causas qualificadas à média do art. 24. O art. 24 da Lei Complementar
    Estadual nº 1.100/2021 disciplina a base média. O art. 27, inciso II, da Lei Complementar
    Estadual nº 1.100/2021 determina reajuste sem paridade para ingresso após 31/12/2003.


    O cálculo inicial segue a forma “Média das 80% maiores remunerações contributivas — LCE
    1.100/2021”, vinculada a esta regra e sustentada pelos dispositivos articulados acima.
    O resultado não sofre redução proporcional ao tempo. Após a concessão, o reajuste ocorre
    sem paridade, de acordo com o regime articulado acima. Eventual parâmetro ainda indicado
    como pendente na forma de cálculo ou no corpo da regra não é antecipado por esta fundamentação.
proveniencia:
  fontes_consultadas:
    - /formas-calculo/forma-calculo-media-80-contribuicoes-lce1100.md
    - /dispositivos/cf88/art-40-par-1-inc-i/ec-103-2019.md
    - /dispositivos/lce-1100-2021/art-24/original.md
    - /dispositivos/lce-1100-2021/art-27-inc-ii/original.md
    - /dispositivos/lce-1100-2021/art-30-caput/original.md
    - /dispositivos/lce-1100-2021/art-30-par-5/original.md
    - /dispositivos/lce-1100-2021/art-30-par-13/original.md
    - LCE 1.100/2021 compilada pela DITEL, consultada em 01/08/2026
  notas: >-
    O § 13 fixa a média do art. 24 sem proporcionalização; o art. 27, II,
    determina reajuste sem paridade. Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Decompor as causas qualificadas de regra-0022 em unidades selecionáveis.
confianca: media
---

# Síntese

Hipótese da LCE 1.100/2021 para servidor ingressado após 31/12/2003, com
incapacidade decorrente de acidente em serviço. Aplica-se a média do art. 24,
sem proporcionalização e sem paridade.

# Pendências localizadas

- confirmar a projeção operacional da média sem paridade;
- resolver Q6-S/Q6-T quanto à classificação da causa;
- completar o gate humano e a decisão institucional de completude.
