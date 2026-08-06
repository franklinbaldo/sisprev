---
type: RegraProposta
id: incapacidade-lce1100-apos-2018-ou-rpc-doenca-contaminacao-por-radiacao
ciclo: ciclo-01
schema_version: 1
estado_auditoria: concluida
estado_implantacao: confirmada_com_ressalva
ressalva_homologacao: >-
  Confirmar em homologação a forma pela qual o Sisprev identifica a sujeição ao regime
  de previdência complementar e aplica o limite máximo dos benefícios do RGPS (art. 24,
  §§ 11 e 12). Os dados disponíveis não revelam integralmente em qual etapa do cálculo
  esse limite incide nem por qual informação o sistema reconhece a sujeição; há, porém,
  evidência operacional de que o motor executa a base desta regra, porque `regra-0022`
  já grava `Valor Médio` em produção para população que inclui quem ingressou a partir
  de 06/11/2018. Até que haja seleção automática suficiente, assegurar a verificação
  manual da data de ingresso e da eventual opção prévia e expressa pelo regime
  complementar durante a instrução, antes da seleção da regra e da elaboração do ato
  concessório. Divergência apurada em homologação impede a ativação em produção e
  retorna para decisão técnica ou jurídica, conforme a natureza.
origens_legacy:
  - regra-0022
predicados:
  causa_incapacidade: doenca_catalogada
  regime: lce1100-incapacidade-apos-2018-ou-rpc
  vinculo_rpc: sujeito
  selecao_por:
    - ingresso_apos_implantacao_rpc
    - opcao_expressa_rpc
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente decorre de contaminação por radiação, moléstia
      relacionada no art. 30, § 8º, inciso XIII, da LCE 1.100/2021
    protocolo_verificacao:
      pergunta: >-
        A perícia médica oficial, com base em conclusão da medicina especializada,
        confirma contaminação por radiação como causa da incapacidade, com
        impossibilidade de readaptação, e o acometimento é posterior à filiação?
      responsavel: perícia médica oficial indicada pelo IPERON e medicina especializada
      momento: instrução e seleção da regra
      meio_de_prova: >-
        laudo da perícia médica oficial, exames e prontuários, mais os assentamentos
        funcionais que situam a filiação, e a conclusão da medicina especializada que o
        inciso XIII exige
      evidencia_exigida: >-
        diagnóstico de contaminação por radiação confirmado, incapacidade para as
        atribuições do cargo, impossibilidade de readaptação e acometimento posterior à
        filiação, com conclusão da medicina especializada
    portador_primario: fundamentacao_integral
aplicabilidade_temporal:
  datas_legadas:
    data_adm_apos: 06/11/2018 00:00
    data_adm_ate: 31/12/2099 00:00
    data_direito_apos: 18/10/2021 00:00
    data_direito_ate: 31/12/2099 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-i/ec-103-2019.md
    papel: >-
      funda a aposentadoria por incapacidade permanente
  - ref: /dispositivos/lce-1100-2021/art-30-par-1/original.md
    papel: >-
      exige que a perícia médica oficial indicada pelo IPERON ateste incapacidade para
      as atribuições do cargo e impossibilidade de readaptação
  - ref: /dispositivos/lce-1100-2021/art-30-par-2/original.md
    papel: >-
      manda o laudo fixar a data da incapacidade ou justificar a impossibilidade de
      fixá-la
  - ref: /dispositivos/lce-1100-2021/art-30-par-3/original.md
    papel: >-
      impõe afastamento prévio não excedente a vinte e quatro meses, com reavaliação
      obrigatória ao seu término
  - ref: /dispositivos/lce-1100-2021/art-30-par-4/original.md
    papel: >-
      condiciona a aposentação a não estar o servidor em condições de reassumir o cargo
      ou de ser readaptado
  - ref: /dispositivos/lce-1100-2021/art-30-caput/original.md
    papel: >-
      excetua a doença grave da proporcionalização
  - ref: /dispositivos/lce-1100-2021/art-30-par-8/original.md
    papel: >-
      exige o acometimento posterior à filiação e abre o rol
  - ref: /dispositivos/lce-1100-2021/art-30-par-8-inc-xiii/original.md
    papel: >-
      nomeia contaminação por radiação entre as doenças graves, contagiosas ou
      incuráveis, com base em conclusão da medicina especializada
  - ref: /dispositivos/lce-1100-2021/art-30-par-13/original.md
    papel: >-
      remete o cálculo desta classe de causa ao art. 24
  - ref: /dispositivos/lce-1100-2021/art-24/original.md
    papel: >-
      disciplina a média das maiores remunerações contributivas
  - ref: /dispositivos/lce-1100-2021/art-24-par-10/original.md
    papel: >-
      limita o provento à remuneração do cargo efetivo
  - ref: /dispositivos/lce-1100-2021/art-24-par-11/original.md
    papel: >-
      sujeita ao teto do RGPS o segurado sujeito ao regime de previdência complementar,
      nos termos dos §§ 14 a 16 do art. 40 da Constituição Federal
  - ref: /dispositivos/lce-1100-2021/art-24-par-12/original.md
    papel: >-
      aplica o teto do RGPS a quem ingressou a partir de 6 de novembro de 2018, data da
      implementação do regime de previdência complementar estadual
  - ref: /dispositivos/cf88/art-40-par-16/ec-103-2019.md
    papel: >-
      subordina a opção pelo regime de previdência complementar a manifestação prévia e
      expressa, uma das duas vias de alcance desta família
  - ref: /dispositivos/lce-1100-2021/art-27-inc-ii/original.md
    papel: >-
      sujeita esta família ao reajustamento nos termos estabelecidos para o RGPS, sem
      paridade
projecao:
  nome: >-
    Incapacidade · contaminação por radiação · ingresso após 05/11/2018 ou aderiu ao RPC
    · média contributiva limitada ao teto do RGPS
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
    servidor titular de cargo efetivo e que a perícia médica oficial indicada pelo
    IPERON atestou incapacidade permanente para o desempenho das atribuições do cargo e
    impossibilidade de readaptação. O laudo pericial fixou a data certa ou provável em
    que o interessado se tornou incapaz para o desempenho das atribuições do cargo e
    para a readaptação e, onde não foi possível fixá-la, justificou os motivos
    impeditivos. A aposentadoria foi precedida de afastamento do trabalho por período
    não excedente a vinte e quatro meses, ao fim do qual o interessado foi
    obrigatoriamente reavaliado e não se encontrava em condições de reassumir o cargo
    nem de ser readaptado. Ficou demonstrado que a incapacidade decorreu de contaminação
    por radiação, cujo diagnóstico foi confirmado por perícia médica oficial mediante
    laudo, exames e prontuários, e cotejado com o rol legal em vigor, e que o
    interessado foi acometido da doença depois de sua filiação ao regime próprio de
    previdência de Rondônia. O enquadramento observou a conclusão da medicina
    especializada, que o próprio inciso exige para esta moléstia. Ficou demonstrado, por
    fim, que o interessado está sujeito ao regime de previdência complementar — seja
    porque o ingresso no serviço público em cargo efetivo se deu a partir de 6 de
    novembro de 2018, data da implementação do regime de previdência complementar
    estadual, seja porque fez a opção prévia e expressa de que trata o § 16 do art. 40
    da Constituição Federal, ainda que tenha ingressado antes daquela data — e que os
    requisitos foram implementados a partir de 18 de outubro de 2021.


    A hipótese se extrai da conjugação dos dispositivos, e é a articulação entre eles
    que a completa. O art. 40, § 1º, inciso I, da Constituição Federal, na redação da
    Emenda Constitucional nº 103/2019, funda a aposentadoria por incapacidade permanente
    para o trabalho. O art. 30, § 1º, da Lei Complementar Estadual nº 1.100/2021 define
    o que a perícia médica oficial indicada pelo IPERON deve atestar — incapacidade para
    o desempenho das atribuições do cargo e impossibilidade de readaptação —, de modo
    que não basta incapacidade genérica para o trabalho. Os §§ 2º a 4º do mesmo artigo
    completam o rito: o laudo fixa a data em que a incapacidade se instalou ou justifica
    não fixá-la; o afastamento antecede a aposentadoria e não excede vinte e quatro
    meses; e a aposentação pressupõe a reavaliação obrigatória ao término do
    afastamento, sem que o servidor esteja em condições de reassumir o cargo ou de ser
    readaptado. O art. 30, caput, estabelece que essa aposentadoria é proporcional ao
    tempo de contribuição, mas excetua da proporcionalização a incapacidade decorrente
    de doença grave, contagiosa ou incurável — de modo que o enquadramento da moléstia
    não é detalhe classificatório: dele depende haver ou não redução no provento. Qual
    seja essa doença o caput não diz, e é o § 8º do mesmo artigo que fecha a hipótese,
    relacionando as moléstias assim consideradas e exigindo que o segurado tenha sido
    acometido após a filiação. É o art. 30, § 8º, inciso XIII que nomeia contaminação
    por radiação, e o faz condicionando o enquadramento à conclusão da medicina
    especializada, que por isso integra a instrução e não é peça dispensável. O § 13 do
    art. 30 remete o cálculo das causas qualificadas ao art. 24. O art. 24 disciplina a
    média das maiores remunerações contributivas, e o seu § 10 impede que o provento
    exceda a remuneração do cargo efetivo. A esta hipótese acrescem os §§ 11 e 12 do
    mesmo artigo: o § 11 sujeita ao limite máximo estabelecido para os benefícios do
    Regime Geral de Previdência Social o segurado sujeito ao regime de previdência
    complementar, nos termos dos §§ 14 a 16 do art. 40 da Constituição Federal; e o § 12
    aplica esse mesmo limite a quem ingressou no serviço público a partir da
    implementação do regime de previdência complementar estadual, ocorrida em 6 de
    novembro de 2018. As duas vias levam ao mesmo resultado, e é por isso que a hipótese
    é uma só. O art. 27, inciso II, sujeita esta coorte ao reajustamento nos termos
    estabelecidos para o Regime Geral de Previdência Social, sem paridade.


    Para os servidores sujeitos ao regime de previdência complementar — por ingresso a
    partir de 6 de novembro de 2018 ou por opção prévia e expressa —, os proventos
    correspondem à média aritmética simples das maiores remunerações utilizadas como
    base para as contribuições, correspondentes a 80% de todo o período contributivo
    desde a competência de julho de 1994 ou desde a do início da contribuição, se
    posterior, atualizadas mês a mês na forma do art. 24, § 7º, observados, nesta ordem,
    o limite da remuneração do cargo efetivo (art. 24, § 10) e o limite máximo
    estabelecido para os benefícios do Regime Geral de Previdência Social (art. 24, §§
    11 e 12). O limite do Regime Geral integra o valor inicial do benefício e não é
    informação posterior à concessão. Não há redução proporcional ao tempo de
    contribuição. Após a concessão, os proventos não se reajustam por paridade: o
    reajustamento é o do art. 27, inciso II, nos termos estabelecidos para o Regime
    Geral de Previdência Social.
proveniencia:
  fontes_consultadas:
    - /tipos-calculo/tipo-calculo-media-80-contribuicoes-teto-rgps-lce1100.md
    - /dispositivos/cf88/art-40-par-1-inc-i/ec-103-2019.md
    - /dispositivos/lce-1100-2021/art-30-par-1/original.md
    - /dispositivos/lce-1100-2021/art-30-par-2/original.md
    - /dispositivos/lce-1100-2021/art-30-par-3/original.md
    - /dispositivos/lce-1100-2021/art-30-par-4/original.md
    - /dispositivos/lce-1100-2021/art-30-caput/original.md
    - /dispositivos/lce-1100-2021/art-30-par-8/original.md
    - /dispositivos/lce-1100-2021/art-30-par-8-inc-xiii/original.md
    - /dispositivos/lce-1100-2021/art-30-par-13/original.md
    - /dispositivos/lce-1100-2021/art-24/original.md
    - /dispositivos/lce-1100-2021/art-24-par-10/original.md
    - /dispositivos/lce-1100-2021/art-24-par-11/original.md
    - /dispositivos/lce-1100-2021/art-24-par-12/original.md
    - /dispositivos/cf88/art-40-par-16/ec-103-2019.md
    - /dispositivos/lce-1100-2021/art-27-inc-ii/original.md
  notas: >-
    Uma regra por causa e por regime de ingresso/RPC. Esta unidade cobre exclusivamente
    contaminação por radiação na família «ingresso após 05/11/2018 ou aderiu ao RPC». A
    fórmula está decomposta em `tipo-calculo-media-80-contribuicoes-teto-rgps-lce1100`.
    Origem material: substituição.
decisoes:
  - data: 2026-08-05
    quem: franklinbaldo
    o_que: >-
      Substituir a divisão em duas coortes de ingresso pela divisão em três
      regimes mutuamente excludentes, conforme o texto da LCE 1.100/2021: o
      art. 24, *caput*, condiciona a média tanto ao ingresso posterior a
      31/12/2003 quanto à ausência de opção pelo regime de previdência
      complementar; o § 11 do mesmo artigo sujeita ao limite máximo dos
      benefícios do RGPS o segurado sujeito a esse regime, nos termos dos
      §§ 14 a 16 do art. 40 da Constituição Federal; e o § 12 aplica o mesmo
      limite a quem ingressou a partir da implementação do regime de
      previdência complementar estadual, ocorrida em 6 de novembro de 2018.
      Daí resultam três famílias, e não duas: ingresso até 31/12/2003 sem
      adesão; ingresso de 2004 a 05/11/2018 sem adesão; e ingresso a partir
      de 06/11/2018 ou adesão ao regime complementar em qualquer data. A
      adesão passa a ser predicado estruturado (`vinculo_rpc`), e o modo de
      alcance de cada família, lista estruturada (`selecao_por`) — a terceira
      é alcançada por disjunção, não por data apenas. Também se acrescentam
      às hipóteses os requisitos do art. 30, §§ 1º a 4º: incapacidade para as
      atribuições do cargo e impossibilidade de readaptação atestadas por
      perícia médica oficial indicada pelo IPERON, fixação da data da
      incapacidade, afastamento não excedente a vinte e quatro meses e
      reavaliação obrigatória ao seu término.
  - data: 2026-08-06
    quem: franklinbaldo
    o_que: >-
      Levar esta unidade de `pendente_mapeamento_sisprev` para
      `confirmada_com_ressalva`, sem tocar em requisito, fórmula, data,
      fundamentação ou identidade. O estado anterior tratava a ausência de
      conhecimento sobre o funcionamento interno do Sisprev como impedimento à
      carga de homologação, e isso inverte o papel da etapa: a homologação existe
      para verificar em campo o comportamento do sistema antes da ativação em
      produção. A ausência de coluna própria para a opção do § 16 no catálogo
      exportado demonstra limite do catálogo, não incapacidade do sistema — o dado
      pode vir do cadastro funcional ou previdenciário, do termo de opção ou de
      certidão administrativa, e a regra é `simulavel: N`, de modo que a seleção
      pode ser feita e conferida na instrução, antes do ato concessório, como já
      ocorre com a causa da incapacidade, o nexo e a condição de magistério. A
      questão operacional permanece registrada em `ressalva_homologacao`.
confianca: media
---

# Síntese

Hipótese da LCE 1.100/2021 para ingresso após 05/11/2018 ou aderiu ao RPC, com incapacidade
permanente decorrente de contaminação por radiação, atestada por perícia médica oficial
indicada pelo IPERON quanto às atribuições do cargo e à impossibilidade de
readaptação. O cálculo é média contributiva limitada ao teto do RGPS.

# Requisitos da matriz do Ciclo 1

Esta regra materializa os requisitos `C1-R00`, `C1-R01`, `C1-R02`, `C1-R03`, `C1-R10`, `C1-R13`, `C1-R15`, `C1-R20`, `C1-R23`, `C1-R23a`, `C1-R23b`, `C1-R26`, `C1-R30`, `C1-R31`, `C1-R33`, `C1-R34`, `C1-R40`, `C1-R41`, `C1-R50`, `C1-R52`, `C1-R60`, `C1-R61`, `C1-R70`, `C1-R71`, `C1-R73`, `C1-R74` da
[matriz de derivação e verificação do Ciclo 1](../../../docs/analysis/matriz-derivacao-verificacao-ciclo-01.md). A correspondência
estrutural entre esta regra e esses requisitos foi verificada
programaticamente. Os requisitos não programáticos são verificados no caso
concreto conforme responsável, evidência e momento definidos na matriz.

# Pendências localizadas

- [ ] **Aplicação do limite máximo dos benefícios do Regime Geral e identificação da sujeição ao regime de previdência complementar.** O catálogo de regras não dispõe de valor que exprima esse limite — os valores disponíveis nomeiam a base de cálculo e a proporcionalização, não o limite — nem de campo que registre a opção pelo regime complementar, de que depende alcançar esta família por servidor ingressado antes de 6 de novembro de 2018. A ausência desses campos é limite do catálogo de regras: os dados do segurado, o motor de cálculo, a instrução administrativa e o ato concessório são planos distintos, e nada se afirma sobre eles. Confirmar em homologação por qual mecanismo o sistema aplica o limite, em que etapa ele incide e por qual informação reconhece a sujeição; até que haja seleção automática suficiente, conferir a data de ingresso e a eventual opção prévia e expressa durante a instrução, antes da seleção da regra e da elaboração do ato concessório. *Rastreabilidade interna: C1-R34; C1-R15.*
