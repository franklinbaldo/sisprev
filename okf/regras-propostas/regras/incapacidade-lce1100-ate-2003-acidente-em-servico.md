---
type: RegraProposta
id: incapacidade-lce1100-ate-2003-acidente-em-servico
ciclo: ciclo-01
schema_version: 1
estado_auditoria: concluida
origens_legacy:
  - regra-0019
predicados:
  causa_incapacidade: acidente_em_servico
  regime: lce1100-incapacidade-ingresso-ate-2003
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
        assentamentos funcionais, e o registro de eventual opção por regime de
        previdência complementar
      momento: instrução e seleção da regra
      evidencia_exigida: >-
        incapacidade permanente comprovada e ato ou conjunto probatório que reconheça o
        nexo com o serviço; e ausência de opção pelo regime de previdência complementar
        de que trata o § 16 do art. 40 da Constituição Federal, de que a paridade
        depende
    portador_primario: fundamentacao_integral
aplicabilidade_temporal:
  datas_legadas:
    data_adm_ate: 31/12/2003 00:00
    data_direito_apos: 18/10/2021 00:00
    data_adm_apos: 01/01/1950 00:00
    data_direito_ate: 31/12/2099 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-i/ec-103-2019.md
    papel: funda a aposentadoria por incapacidade permanente
  - ref: /dispositivos/lce-1100-2021/art-30-caput/original.md
    papel: separa causas qualificadas e causa comum
  - ref: /dispositivos/lce-1100-2021/art-30-par-5/original.md
    papel: define acidente em serviço
  - ref: /dispositivos/lce-1100-2021/art-30-par-13/original.md
    papel: >-
      remete diretamente as causas qualificadas ao art. 24; a base adotada por
      esta regra é a do art. 25, pelas razões desenvolvidas em
      tipo-calculo-totalidade-remuneracao-cargo-efetivo-lce1100
  - ref: /dispositivos/lce-1100-2021/art-25/original.md
    papel: >-
      disciplina a base de cálculo da coorte de ingresso até 31/12/2003:
      totalidade da remuneração do cargo efetivo
  - ref: /dispositivos/lce-1100-2021/art-27-inc-i/original.md
    papel: >-
      assegura paridade à coorte de ingresso até 31/12/2003, salvo opção pelo regime
      do § 16 do art. 40 da Constituição Federal
  - ref: /dispositivos/ec-41-2003/art-7/original.md
    papel: >-
      define o conteúdo da paridade: revisão na mesma proporção e na mesma data da
      remuneração dos servidores em atividade
  - ref: /dispositivos/cf88/art-40-par-16/ec-103-2019.md
    papel: >-
      subordina o regime de previdência complementar a opção prévia e expressa, cuja
      ausência é o que preserva a paridade do art. 27, inciso I
projecao:
  nome: >-
    Incapacidade · acidente em serviço · ingresso até 2003 · remuneração do cargo ·
    integral · com paridade
  tipo_de_beneficio: APOSENTADORIA POR INCAPACIDADE PERMANENTE
  tipo: CIVIL
  apos_especial: N
  tabelapontuacao: N
  requisitos_da_in_no_5_2020: N
  relatorio_p_reserva_remunerada_por_idade_ex_officio: N
  adicional_inatividade: N
  visivel_dtc_proporcional: N
  visivel_dtc_integral: N
  atualmente_no_sistema: 'TRUE'
  validado_pge: 'FALSE'
  validado_presidencia: 'FALSE'
  ciclo_de_validacao: 1º
  simulavel: N
  paridade: S
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Efetivo
  fundamentacao_integral: >-
    No curso do processo administrativo, ficou demonstrado que o interessado era
    servidor titular de cargo efetivo e que se encontrava em estado de incapacidade
    permanente para o trabalho, apurada por junta médica oficial mediante laudo, e que
    essa incapacidade decorreu de acidente em serviço, cujo nexo com a atividade foi
    reconhecido a partir da comunicação e da apuração do acidente, dos prontuários e dos
    assentamentos funcionais. Ficou demonstrado, por fim, que o ingresso no serviço
    público em cargo efetivo se deu até 31 de dezembro de 2003 e que os requisitos foram
    implementados a partir de 18 de outubro de 2021. Ficou demonstrado, também, que o
    interessado não fez a opção pelo regime de previdência complementar de que trata o §
    16 do art. 40 da Constituição Federal, condição a que a lei subordina o
    reajustamento com paridade.


    A hipótese se extrai da conjugação dos dispositivos, e é a articulação entre eles
    que a completa. O art. 40, § 1º, inciso I, da Constituição Federal, na redação da
    Emenda Constitucional nº 103/2019, funda a aposentadoria por incapacidade permanente
    para o trabalho. O art. 30, caput, da Lei Complementar Estadual nº 1.100/2021
    estabelece que essa aposentadoria é proporcional ao tempo de contribuição, mas
    excetua da proporcionalização a incapacidade decorrente de acidente em serviço,
    moléstia profissional ou doença grave, contagiosa ou incurável. O acidente em
    serviço é uma dessas causas, e o § 5º do art. 30 é que o define, de modo que o
    reconhecimento do nexo não é formalidade: dele depende o próprio ramo do cálculo. É
    essa qualificação que afasta a fração: sem ela, o mesmo grau de incapacidade levaria
    a provento reduzido.


    Para os servidores que ingressaram no serviço público até 31 de dezembro de 2003, os
    proventos correspondem à totalidade da remuneração do cargo efetivo, nos termos do
    art. 25 da LCE nº 1.100/2021, com paridade na forma do art. 27, I. Após a
    concessão, os proventos são reajustados na mesma proporção e na mesma data da
    remuneração dos servidores em atividade (art. 7º da Emenda Constitucional nº
    41/2003), salvo opção pelo regime de que trata o § 16 do art. 40 da Constituição
    Federal. A paridade é regime de revisão posterior e não integra o cálculo inicial.
proveniencia:
  fontes_consultadas:
    - /tipos-calculo/tipo-calculo-totalidade-remuneracao-cargo-efetivo-lce1100.md
    - /dispositivos/cf88/art-40-par-1-inc-i/ec-103-2019.md
    - /dispositivos/lce-1100-2021/art-25/original.md
    - /dispositivos/lce-1100-2021/art-27-inc-i/original.md
    - /dispositivos/ec-41-2003/art-7/original.md
    - /dispositivos/cf88/art-40-par-16/ec-103-2019.md
    - /dispositivos/lce-1100-2021/art-30-caput/original.md
    - /dispositivos/lce-1100-2021/art-30-par-5/original.md
    - /dispositivos/lce-1100-2021/art-30-par-13/original.md
    - LCE 1.100/2021 compilada pela DITEL, consultada em 01/08/2026
  notas: >-
    O § 13 é regra especial da incapacidade, remete ao art. 24 e ressalva o
    direito adquirido a outra fórmula (proteção adicional, independente).
    Nota de 2026-08-01: "o art. 25 não substitui essa remissão apenas pelo
    ingresso até 2003; outra fórmula depende de direito adquirido sob
    regime anterior." A revisão de 2026-08-05 (decisões, abaixo) supera
    essa nota, mas não pela via do direito adquirido: dentro do próprio
    regime vigente da LCE 1.100/2021, é o art. 25 que disciplina
    diretamente a base de cálculo desta coorte. `regra-0019` — já em
    produção para esta mesma hipótese, citando o próprio art. 25 em
    `dispositivos:` e gravando `tipo_calculo: Valor Efetivo` — é evidência
    da prática operacional anterior do Sisprev e do enum já utilizado, não
    prova de direito adquirido dos servidores. O art. 27, I, mantém a
    paridade. Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Aplicar a fórmula especial do § 13 separadamente do regime de reajuste do
      art. 27, I.
  - data: 2026-08-04
    quem: franklinbaldo
    o_que: >-
      Preencher as colunas do Sisprev que a projeção deixava em branco — `tipo`,
      `apos_especial`, `tabelapontuacao`, `adicional_inatividade`, os dois
      `visivel_dtc_*`, os dois relatórios, `atualmente_no_sistema`,
      `validado_pge`, `validado_presidencia`, `ciclo_de_validacao` — e as
      sentinelas do lado não usado de cada par de datas. Nenhum valor é escolha
      nova: cada um é o que as origens que saem gravam ou, onde a coluna tem
      valor único, o que as 112 linhas do catálogo gravam. Em branco é
      representação que o Sisprev nunca recebeu, e o compilador não a acusa
      (`_checar_contrato_legado` reprova valor malformado, nunca valor ausente).
  - data: 2026-08-04
    quem: franklinbaldo
    o_que: >-
      Gravar `tipo_de_beneficio: APOSENTADORIA POR INCAPACIDADE PERMANENTE`, como as
      quatro regras de origem já gravam. A unidade trazia APOSENTADORIA POR INVALIDEZ,
      que é o vocabulário anterior à EC 103/2019: a proposta andava para trás num campo
      em que o catálogo já estava atualizado, e a LCE 1.100/2021 — objeto deste ciclo —
      chama o benefício de incapacidade permanente.
  - data: 2026-08-04
    quem: franklinbaldo
    o_que: >-
      Executar verificação automatizada de consistência estrutural desta
      regra (issue #123): cotejados os dispositivos citados (art. 30, caput e
      §§ 5º e 13, e art. 24), as datas contra a matriz T7 e a projeção de
      cálculo contra a causa qualificada da coorte até 2003. Evidência em
      "Verificação automatizada de consistência estrutural", no corpo desta
      unidade. Não é revisão humana da coordenação — o item "concluir a
      conferência humana desta regra" permanece aberto no checklist.
  - data: 2026-08-04
    quem: franklinbaldo
    o_que: >-
      Substituir a verificação automatizada registrada no corpo por
      referência aos requisitos da matriz de derivação e verificação do
      Ciclo 1 (docs/analysis/matriz-derivacao-verificacao-ciclo-01.md).
      A checagem estrutural repetitiva (dispositivo, datas, projeção de
      cálculo) passa a ser demonstrada uma vez por requisito, na matriz,
      em vez de quarenta vezes, uma por regra. Pendências específicas
      desta hipótese continuam registradas no corpo desta unidade.
  - data: 2026-08-05
    quem: franklinbaldo
    o_que: >-
      Trocar a base de cálculo de `Valor Médio` (art. 24) para `Valor Efetivo`
      (art. 25), por revisão jurídica adicional da coordenação, superando a
      nota de 2026-08-01 (`proveniencia.notas`) que recusava a substituição
      por falta de evidência de direito adquirido. A leitura anterior —
      média do art. 24 combinada com paridade, via art. 30, § 13 — é
      juridicamente construível a partir da remissão daquele parágrafo, mas
      conflita com o art. 25, que rege expressamente, com a mesma grafia do
      art. 27, I, a coorte "que tenha ingressado no serviço público em
      cargo efetivo até 31 de dezembro de 2003"; altera a fórmula que
      `regra-0019` já grava em produção para esta mesma hipótese
      (`tipo_calculo: Valor Efetivo`, citando o próprio art. 25 em
      `dispositivos:`); e carece de jurisprudência específica ou precedente
      administrativo interno inequívoco que sustente a combinação média +
      paridade. A orientação conservadora adotada preserva a coerência de
      regime pela coorte: quem ingressou até 2003 calcula sobre a
      remuneração do cargo (art. 25) com paridade (art. 27, I); quem
      ingressou depois calcula pela média (art. 24) sem paridade. A tensão
      entre os arts. 25 e 30, § 13 permanece questão interpretativa, não
      resolvida por esta decisão, e pode ser revista diante de manifestação
      jurídica específica, precedente ou decisão institucional posterior.
      `tipo-calculo-totalidade-remuneracao-cargo-efetivo-lce1100` passa a
      fundamentar esta regra, no lugar de
      `tipo-calculo-media-80-contribuicoes-lce1100`.
  - data: 2026-08-05
    quem: franklinbaldo
    o_que: >-
      Corrigir o fundamento da troca de `Valor Médio` para `Valor Efetivo`
      registrada nesta mesma data, em revisão à correção anterior: a
      decisão anterior apresentava o art. 25 como a "outra fórmula"
      ressalvada pelo art. 30, § 13, comprovada por direito adquirido via
      `regra-0019`. Essa formulação está incorreta. A leitura adotada pela
      coordenação é outra: o servidor ingressado até 31/12/2003 requer a
      aposentadoria por incapacidade pela regra permanente atual da LCE
      1.100/2021, e é o art. 25, dentro desse próprio regime vigente, que
      disciplina diretamente a base de cálculo dessa coorte — harmonizando
      os arts. 24 e 25 como divisão vigente de coortes, não como direito
      adquirido a regime anterior. O art. 27, I, disciplina o
      reajustamento com paridade. A ressalva do art. 30, § 13, ao direito
      adquirido é proteção adicional e independente, não o fundamento
      necessário para aplicar o art. 25. `regra-0019` (e `regra-0020`,
      para a causa comum da mesma coorte) servem como evidência da
      prática operacional anterior do Sisprev e dos enums já utilizados —
      não como prova de direito adquirido dos servidores. A tensão entre
      os arts. 25 e 30, § 13 (a remissão literal ao art. 24) permanece
      registrada como risco interpretativo, revisável diante de
      manifestação jurídica específica, precedente ou decisão
      institucional posterior — mas a carga adota a fórmula definida no
      art. 25, sem apresentar as duas bases como igualmente válidas.
  - data: 2026-08-05
    quem: franklinbaldo
    o_que: >-
      Enxugar a fundamentação desta unidade e corrigir o fundamento do
      round 15 do RFC 0004, que restringia a tensão de remissão ao art.
      24 à causa comum. Nas causas qualificadas, a remissão ao art. 24 é
      direta, pelo art. 30, § 13 (não pelo encadeamento art. 30, § 14 e
      art. 26, § 1º, que só existe na causa comum). *Data venia*,
      entende-se que essa remissão não afasta a disciplina do art. 25
      para a coorte de ingresso até 31/12/2003, pelas razões
      desenvolvidas em `tipo-calculo-totalidade-remuneracao-cargo-efetivo-lce1100`,
      que passa a concentrar a fundamentação antes repetida em cada
      unidade da coorte. Mantida a fórmula: totalidade da remuneração do
      cargo efetivo (art. 25), com paridade (art. 27, I).
confianca: media
---

# Síntese

Hipótese permanente da LCE 1.100/2021 para servidor ingressado até 31/12/2003,
com incapacidade decorrente de acidente em serviço. Os proventos correspondem à
totalidade da remuneração do cargo efetivo (art. 25), sem proporcionalização
pelo tempo, e são reajustados com paridade (art. 27, I).

A janela começa em 18/10/2021, data de publicação e vigência da lei. A seleção
exige prova positiva do nexo; falta de informação não autoriza causa comum.

# Requisitos da matriz do Ciclo 1

Esta regra materializa os requisitos `C1-R00`, `C1-R10`, `C1-R11`, `C1-R13`, `C1-R20`, `C1-R21`, `C1-R30`, `C1-R31`, `C1-R40`, `C1-R41`, `C1-R50`, `C1-R51`, `C1-R60`, `C1-R61`, `C1-R70`, `C1-R71`, `C1-R73`, `C1-R74` da
[matriz de derivação e verificação do Ciclo 1](../../../docs/analysis/matriz-derivacao-verificacao-ciclo-01.md). A correspondência
estrutural entre esta regra e esses requisitos foi verificada
programaticamente. Os requisitos não programáticos são verificados no caso
concreto conforme responsável, evidência e momento definidos na matriz.

# Pendências localizadas

Nenhuma pendência específica desta hipótese. As dependências gerais do
ciclo (`C1-R73`, `C1-R74`) estão registradas na matriz e não se repetem
aqui.
