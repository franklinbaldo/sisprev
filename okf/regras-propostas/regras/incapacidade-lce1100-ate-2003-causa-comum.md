---
type: RegraProposta
id: incapacidade-lce1100-ate-2003-causa-comum
schema_version: 1
estado_proposta: elaboracao
origens_legacy:
  - regra-0020
predicados:
  causa_incapacidade: causa_comum
  regime: lce1100-incapacidade-ingresso-ate-2003
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente não decorre de acidente em serviço, moléstia
      profissional nem doença grave catalogada
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
    data_adm_ate: 31/12/2003 00:00
    data_direito_apos: 18/10/2021 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-i/ec-103-2019.md
    papel: funda a aposentadoria por incapacidade permanente
  - ref: /dispositivos/lce-1100-2021/art-30-caput/original.md
    papel: determina o ramo residual proporcional
  - ref: /dispositivos/lce-1100-2021/art-30-par-14/original.md
    papel: remete a causa comum à fórmula proporcional do art. 26
  - ref: /dispositivos/lce-1100-2021/art-26/original.md
    papel: aplica fração em dias sobre a média do art. 24
  - ref: /dispositivos/lce-1100-2021/art-24/original.md
    papel: disciplina a base média da proporcionalização
  - ref: /dispositivos/lce-1100-2021/art-27-inc-i/original.md
    papel: assegura paridade à coorte de ingresso até 31/12/2003
projecao:
  nome: >-
    Incapacidade permanente · LCE 1.100 · ingresso até 2003 · demais causas ·
    média proporcional · paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: S
  sexo: AMBOS
  integral: N
  tipo_calculo: Proporcionalidade Dias
  fundamentacao_proporcional: >-
    No curso do processo administrativo, ficou demonstrado que o interessado era servidor
    titular de cargo efetivo e que a incapacidade permanente não decorria de acidente em serviço,
    moléstia profissional nem doença grave catalogada; a verificação foi realizada por junta
    médica oficial e instrução previdenciária do IPERON, mediante laudo médico oficial, prontuários,
    histórico ocupacional, apuração de eventual acidente e rol legal vigente, tendo sido exigida
    a seguinte evidência: incapacidade permanente comprovada e investigação suficiente das
    causas qualificadas; silêncio ou prova insuficiente não bastam. Ficou também demonstrado
    que os requisitos foram implementados em 18/10/2021 ou depois e que o ingresso no serviço
    público ocorreu até 31/12/2003, inclusive.


    A hipótese e seus efeitos resultam da conjugação dos dispositivos aplicáveis. O art. 40,
    § 1º, inciso I, da Constituição Federal, na redação da EC 103/2019 funda a aposentadoria
    por incapacidade permanente. O art. 30, caput, da Lei Complementar Estadual nº 1.100/2021
    determina o ramo residual proporcional. O art. 30, § 14, da Lei Complementar Estadual
    nº 1.100/2021 remete a causa comum à fórmula proporcional do art. 26. O art. 26 da Lei
    Complementar Estadual nº 1.100/2021 aplica fração em dias sobre a média do art. 24. O
    art. 24 da Lei Complementar Estadual nº 1.100/2021 disciplina a base média da proporcionalização.
    O art. 27, inciso I, da Lei Complementar Estadual nº 1.100/2021 assegura paridade à coorte
    de ingresso até 31/12/2003.


    O cálculo inicial segue a forma “Média das 80% maiores remunerações, limitada e proporcional
    em dias — LCE 1.100/2021”, vinculada a esta regra e sustentada pelos dispositivos articulados
    acima. O resultado recebe a proporcionalização pelo tempo descrita nessa forma. Após a
    concessão, os proventos são revistos com paridade, segundo o dispositivo específico articulado
    acima. Eventual parâmetro ainda indicado como pendente na forma de cálculo ou no corpo
    da regra não é antecipado por esta fundamentação.
proveniencia:
  fontes_consultadas:
    - /formas-calculo/forma-calculo-media-80-proporcional-dias-lce1100.md
    - /dispositivos/cf88/art-40-par-1-inc-i/ec-103-2019.md
    - /dispositivos/lce-1100-2021/art-24/original.md
    - /dispositivos/lce-1100-2021/art-26/original.md
    - /dispositivos/lce-1100-2021/art-27-inc-i/original.md
    - /dispositivos/lce-1100-2021/art-30-caput/original.md
    - /dispositivos/lce-1100-2021/art-30-par-14/original.md
    - LCE 1.100/2021 compilada pela DITEL, consultada em 01/08/2026
  notas: >-
    A combinação proporcional com paridade é juridicamente possível. O art. 26
    aplica fração em dias sobre a média do art. 24, enquanto o art. 27, I,
    disciplina separadamente o reajuste. `Não identificado` evita projetar a
    fórmula composta como simples proporcionalidade em dias. Origem material:
    substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Reconhecer a existência da combinação representada por regra-0020,
      corrigindo sua base para média proporcional e preservando a paridade.
confianca: media
---

# Síntese

A `regra-0020` não representa combinação impossível. Para servidor ingressado
até 31/12/2003 cuja incapacidade decorra de causa comum, o § 14 remete ao art.
26: média do art. 24 proporcionalizada em dias. O art. 27, I, assegura paridade.

A regra legada precisa ser substituída porque copia fundamentação integral e o
rótulo `Proporcionalidade Dias` não expressa sozinho a base média.

# Pendências localizadas

- criar ou confirmar FormaCalculo que represente média proporcional em dias;
- confirmar a projeção operacional da combinação com paridade;
- resolver Q6-S/Q6-T e completar o gate humano.
