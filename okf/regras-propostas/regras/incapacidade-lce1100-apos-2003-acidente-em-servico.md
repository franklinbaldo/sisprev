---
type: RegraProposta
id: incapacidade-lce1100-apos-2003-acidente-em-servico
ciclo: ciclo-01
schema_version: 1
estado_auditoria: concluida
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
    data_adm_ate: 31/12/2099 00:00
    data_direito_ate: 31/12/2099 00:00
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
  - ref: /dispositivos/lce-1100-2021/art-27-inc-i/original.md
    papel: >-
      reserva a paridade à coorte de ingresso até 31/12/2003, do que decorre a sua
      inaplicabilidade a esta regra
  - ref: /dispositivos/lce-1100-2021/art-27-inc-ii/original.md
    papel: >-
      sujeita a coorte de ingresso a partir de 01/01/2004 ao reajustamento nos termos
      estabelecidos para o RGPS
projecao:
  nome: >-
    Incapacidade permanente · ingresso a partir de 2004 · acidente em serviço · 100% da
    média contributiva
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
  paridade: N
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Médio
  fundamentacao_integral: >-
    No curso do processo administrativo, ficou demonstrado que o interessado era
    servidor titular de cargo efetivo e que se encontrava em estado de incapacidade
    permanente para o trabalho, apurada por junta médica oficial mediante laudo, e que
    essa incapacidade decorreu de acidente em serviço, cujo nexo com a atividade foi
    reconhecido a partir da comunicação e da apuração do acidente, dos prontuários e dos
    assentamentos funcionais. Ficou demonstrado, por fim, que o ingresso no serviço
    público em cargo efetivo se deu depois de 31 de dezembro de 2003 e que os requisitos
    foram implementados a partir de 18 de outubro de 2021.


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
    a provento reduzido. O § 13 do mesmo artigo fecha o cálculo, mandando apurá-lo na
    forma do art. 24 — que disciplina sobre que valor o benefício incide — e ressalvando
    o direito adquirido a outra fórmula, o que preserva quem já reunia requisitos sob
    disciplina anterior.


    Do enquadramento resulta a concessão de proventos calculados sobre a média
    disciplinada no art. 24 da Lei Complementar Estadual nº 1.100/2021, sem redução
    proporcional ao tempo de contribuição, na forma de cálculo vinculada a esta regra.
    Após a concessão, os proventos não se reajustam por paridade: o art. 27, inciso I,
    da mesma Lei Complementar reserva esse regime a quem ingressou em cargo efetivo até
    31 de dezembro de 2003, coorte a que esta regra não se aplica. O reajustamento é o
    do inciso II do mesmo artigo, que o remete aos termos estabelecidos para o Regime
    Geral de Previdência Social.
proveniencia:
  fontes_consultadas:
    - /tipos-calculo/tipo-calculo-media-80-contribuicoes-lce1100.md
    - /dispositivos/cf88/art-40-par-1-inc-i/ec-103-2019.md
    - /dispositivos/lce-1100-2021/art-24/original.md
    - /dispositivos/lce-1100-2021/art-27-inc-i/original.md
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
  - data: 2026-08-04
    quem: franklinbaldo
    o_que: >-
      Gravar `data_adm_apos: 31/12/2003`, e não `01/01/2004`, no corte de
      ingresso: o campo é exclusivo e o valor gravado é o último dia do regime
      anterior (Q1). Com `01/01/2004` a regra deixaria de fora quem tomou posse
      exatamente nesse dia, e a unidade divergia das demais do mesmo ramo.
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
      Repor `data_adm_apos: 01/01/2004`, que é o valor declarado pela decisão
      vigente das janelas temporais. A entrada anterior desta lista gravou
      `31/12/2003` invocando a leitura exclusiva do campo (Q1) — leitura que a
      consolidação de 01/08 substituiu pela inclusiva e que a regra contra
      regressão documental de `okf/spec/index.md` fecha expressamente. A
      demonstração que justificava o `31/12/2003` também não se sustenta: as duas
      grafias particionam a fronteira igualmente, e o que decide entre elas é o
      operador que o motor do Sisprev aplica, que ninguém mediu. Enquanto essa
      medição não existe, vale o que está decidido — e passa a valer conferido,
      por `scripts/conferir_decisoes_da_spec.py`.
  - data: 2026-08-04
    quem: franklinbaldo
    o_que: >-
      Executar verificação automatizada de consistência estrutural desta
      regra (issue #123): cotejados os dispositivos citados (art. 30, caput e
      §§ 5º e 13, e art. 24), as datas contra a matriz T7 e a projeção de
      cálculo contra a causa qualificada da coorte a partir de 2004.
      Evidência em "Verificação automatizada de consistência estrutural", no
      corpo desta unidade. Não é revisão humana da coordenação — o item
      "concluir a conferência humana desta regra" permanece aberto no
      checklist.
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
confianca: media
---

# Síntese

Hipótese da LCE 1.100/2021 para servidor ingressado após 31/12/2003, com
incapacidade decorrente de acidente em serviço. Aplica-se a média do art. 24,
sem proporcionalização e sem paridade.

# Requisitos da matriz do Ciclo 1

Esta regra materializa os requisitos `C1-R00`, `C1-R10`, `C1-R12`, `C1-R13`, `C1-R20`, `C1-R21`, `C1-R30`, `C1-R31`, `C1-R40`, `C1-R41`, `C1-R50`, `C1-R52`, `C1-R70`, `C1-R71`, `C1-R73`, `C1-R74` da
[matriz de derivação e verificação do Ciclo 1](../../../docs/analysis/matriz-derivacao-verificacao-ciclo-01.md). A correspondência
estrutural entre esta regra e esses requisitos foi verificada
programaticamente. Os requisitos não programáticos são verificados no caso
concreto conforme responsável, evidência e momento definidos na matriz.

# Pendências localizadas

Nenhuma pendência específica desta hipótese. As dependências gerais do
ciclo (`C1-R73`, `C1-R74`) estão registradas na matriz e não se repetem
aqui.
