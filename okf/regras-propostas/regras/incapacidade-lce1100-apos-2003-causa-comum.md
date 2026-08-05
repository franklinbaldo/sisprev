---
type: RegraProposta
id: incapacidade-lce1100-apos-2003-causa-comum
ciclo: ciclo-01
schema_version: 1
estado_auditoria: concluida
estado_implantacao: confirmada_com_ressalva
ressalva_homologacao: >-
  Confirmar em homologação prática se `Proporcionalidade Dias` executa, para
  esta hipótese, a fórmula composta do art. 26 — média do art. 24, limitada
  previamente pelo teto do § 10 do próprio art. 24, proporcionalizada em dias
  — e não uma proporcionalidade pura sobre a remuneração, sem a base média
  nem o limite. Confirmação obrigatória antes da ativação em produção;
  não bloqueia a entrada na carga de homologação, porque a mesma
  combinação (`integral: N`, `tipo_calculo: Proporcionalidade Dias`) já está
  em produção em `regra-0021` para esta mesma hipótese.
origens_legacy:
  - regra-0021
predicados:
  causa_incapacidade: causa_comum
  regime: lce1100-incapacidade-ingresso-apos-2003
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
    data_adm_apos: 01/01/2004 00:00
    data_direito_apos: 18/10/2021 00:00
    data_adm_ate: 31/12/2099 00:00
    data_direito_ate: 31/12/2099 00:00
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
  - ref: /dispositivos/lce-1100-2021/art-24-par-10/original.md
    papel: >-
      limita a base média à remuneração do cargo efetivo, observada
      previamente à fração do art. 26 por força do § 1º deste último
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
    Incapacidade permanente · LCE 1.100 · ingresso após 2003 · demais causas ·
    média proporcional · sem paridade
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
  integral: N
  tipo_calculo: Proporcionalidade Dias
  fundamentacao_proporcional: >-
    No curso do processo administrativo, ficou demonstrado que o interessado era
    servidor titular de cargo efetivo e que se encontrava em estado de incapacidade
    permanente para o trabalho, apurada por junta médica oficial mediante laudo. Ficou
    demonstrado, ainda, que a incapacidade não decorreu de acidente em serviço, de
    moléstia profissional nem de moléstia relacionada no rol do art. 30, § 8º, da Lei
    Complementar Estadual nº 1.100/2021, exclusão que foi objeto de investigação própria
    — a apuração de eventual acidente, o exame do histórico ocupacional e o cotejo do
    diagnóstico com o rol —, e não de mero silêncio dos autos. Ficou demonstrado, por
    fim, que o ingresso no serviço público em cargo efetivo se deu depois de 31 de
    dezembro de 2003 e que os requisitos foram implementados a partir de 18 de outubro
    de 2021.


    A hipótese se extrai da conjugação dos dispositivos, e é a articulação entre eles
    que a completa. O art. 40, § 1º, inciso I, da Constituição Federal, na redação da
    Emenda Constitucional nº 103/2019, funda a aposentadoria por incapacidade permanente
    para o trabalho. O art. 30, caput, da Lei Complementar Estadual nº 1.100/2021 fixa a
    regra e a exceção: os proventos são proporcionais ao tempo de contribuição, salvo se
    a incapacidade decorrer de acidente em serviço, moléstia profissional ou doença
    grave, contagiosa ou incurável. Esta regra é o ramo residual — aplica-se justamente
    quando nenhuma dessas causas se verifica —, e daí decorre que a exclusão precisa ser
    apurada, e não presumida do silêncio: é ela que distingue esta hipótese das
    qualificadas, e quem não a investiga concede provento reduzido a quem talvez tivesse
    direito ao integral. O § 14 do mesmo artigo remete esse cálculo ao art. 26, que
    aplica a fração de tempo, medida em dias, sobre a média disciplinada no art. 24.


    Do enquadramento resulta a concessão de proventos proporcionais: a média
    disciplinada no art. 24 da Lei Complementar Estadual nº 1.100/2021, limitada
    previamente à remuneração do respectivo cargo efetivo por força do § 10 desse
    mesmo artigo, recebe a fração entre o tempo de contribuição e o tempo exigido,
    medida em dias na forma do art. 26, cujo § 1º determina expressamente essa
    precedência do limite, tudo na forma de cálculo vinculada a esta regra. Após a
    concessão, os proventos não
    se reajustam por paridade: o art. 27, inciso I, da mesma Lei Complementar reserva
    esse regime a quem ingressou em cargo efetivo até 31 de dezembro de 2003, coorte a
    que esta regra não se aplica. O reajustamento é o do inciso II do mesmo artigo, que
    o remete aos termos estabelecidos para o Regime Geral de Previdência Social.
proveniencia:
  fontes_consultadas:
    - /tipos-calculo/tipo-calculo-media-proporcional-dias-lce1100.md
    - /dispositivos/cf88/art-40-par-1-inc-i/ec-103-2019.md
    - /dispositivos/lce-1100-2021/art-24/original.md
    - /dispositivos/lce-1100-2021/art-24-par-10/original.md
    - /dispositivos/lce-1100-2021/art-26/original.md
    - /dispositivos/lce-1100-2021/art-27-inc-i/original.md
    - /dispositivos/lce-1100-2021/art-27-inc-ii/original.md
    - /dispositivos/lce-1100-2021/art-30-caput/original.md
    - /dispositivos/lce-1100-2021/art-30-par-14/original.md
    - LCE 1.100/2021 compilada pela DITEL, consultada em 01/08/2026
  notas: >-
    O art. 26 aplica fração em dias sobre a média do art. 24, previamente
    limitada pelo teto da remuneração do cargo efetivo do § 10 do próprio
    art. 24 (art. 26, § 1º); o art. 27, II, disciplina separadamente o
    reajuste sem paridade. A fórmula jurídica, com o limite expresso, está
    decomposta e documentada em `tipo-calculo-media-proporcional-dias-lce1100`,
    que também decidiu, em 01/08/2026, a projeção `tipo_calculo:
    Proporcionalidade Dias` — com fidelidade parcial expressamente declarada
    ali: o rótulo representa o ajuste em dias, mas não expressa por si só a
    base média do art. 24 que o art. 26 manda proporcionalizar, e o enum do
    Sisprev não possui rótulo próprio para a combinação completa. É essa
    projeção, e não `Não identificado`, que este frontmatter grava (issue
    #122). O que permanece não confirmado é premissa operacional distinta —
    se o rótulo `Proporcionalidade Dias`, no sistema, de fato executa a
    fórmula composta —, e essa confirmação é dependência externa junto ao
    IPERON e ao fornecedor (issue #124), não decisão em aberto desta regra.
    Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Substituir o ramo residual de regra-0021 por unidade com causa, base média
      e proporcionalização explicitadas.
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
      Harmonizar `proveniencia.notas` com a projeção gravada em `tipo_calculo`
      (issue #122). O texto anterior descrevia como preferível o rótulo `Não
      identificado`, contradizendo o frontmatter, que grava `Proporcionalidade
      Dias`. A fórmula jurídica — média do art. 24 proporcionalizada em dias
      pelo art. 26 — já estava decomposta e documentada em
      `tipo-calculo-media-proporcional-dias-lce1100`, que também já havia
      decidido, em 01/08/2026, projetar `Proporcionalidade Dias` com
      fidelidade parcial. A contradição era de redação da nota, não da
      decisão: a nota não acompanhou o que a forma de cálculo já registrava.
  - data: 2026-08-04
    quem: franklinbaldo
    o_que: >-
      Recuar `estado_proposta` de `deployable` para `preview`, em revisão à
      correção anterior desta mesma data. `Proporcionalidade Dias` tem
      fidelidade parcial declarada porque o rótulo não expressa a base média
      do art. 24 — e, diferente de outras formas com fidelidade parcial cuja
      lacuna é de detalhe operacional (ex.: qual conjunto exato de
      remunerações compõe a média), aqui a omissão é da própria base: sem
      confirmação, o rótulo é compatível com uma leitura que zeraria a média e
      computaria proporcionalidade pura em dias, o que alteraria o valor do
      benefício. Isso é a semântica operacional não resolvida que RFC 0004
      §5.3 trata como fail-closed para `deployable` (passa em `preview`, não
      em `deployable`, enquanto a questão operacional estiver aberta). A
      fórmula jurídica continua confirmada e não é reaberta; o que recua é
      apenas a afirmação de que a unidade está pronta para o sistema antes da
      confirmação do IPERON/fornecedor (issue #124).
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
      Separar, no critério de `deployable`, a derivação jurídica (se a
      fórmula que a lei exige está determinada) da confirmação de
      implantação (se o valor gravado no Sisprev a identifica sem
      ambiguidade) — RFC 0004, round 9. A decisão de 2026-08-04 que recuou
      esta unidade para `preview` tratava as duas como uma só; a fórmula
      sempre esteve determinada (`tipo-calculo-media-proporcional-dias-lce1100`),
      e o rótulo `Proporcionalidade Dias` já era, então como agora, o único
      valor que o Sisprev grava para esta hipótese — não havia alternativa a
      escolher. `estado_proposta` volta a `deployable`. A pendência
      operacional passa a `estado_implantacao: pendente_mapeamento_sisprev`,
      campo próprio para isso: falta confirmação de que o rótulo (ou outro
      mecanismo do sistema) identifica esta fórmula sem ambiguidade,
      distinguindo-a de outras fórmulas de causa comum que compartilham o
      mesmo valor no catálogo legado (issue #122, #124). Essa pendência não
      reabre a derivação e não impede o fechamento do ciclo quanto a esta
      hipótese; impede apenas a troca da fonte operacional de exportação do
      grupo a que esta unidade pertence, enquanto não confirmada
      (`okf/spec/conjunto.md`).
  - data: 2026-08-05
    quem: franklinbaldo
    o_que: >-
      Trocar `estado_implantacao` de `pendente_mapeamento_sisprev` para
      `confirmada_com_ressalva` (RFC 0004, round 12) e admitir esta unidade
      na carga de homologação. `regra-0021` já está em produção com
      `integral: N` e `tipo_calculo: Proporcionalidade Dias` para esta mesma
      hipótese — causa comum, ingresso a partir de 01/01/2004 —, o que é
      evidência concreta de que o Sisprev já dispõe de mecanismo operacional
      para essa combinação; a ambiguidade que `pendente_mapeamento_sisprev`
      registrava (o mesmo rótulo também identifica
      `tipo-calculo-media-proporcional-dias-lce432` e
      `tipo-calculo-remuneracao-cargo-ec70-proporcional-dias`) é sobre o
      vocabulário do catálogo legado em geral, não sobre se esta hipótese
      específica tem representação no sistema — e essa segunda pergunta já
      está respondida pela própria `regra-0021` viva. A pendência
      remanescente é mais estreita e genuinamente diferente: confirmar, em
      homologação prática, se a execução aplica a base composta do art. 26
      — média do art. 24 limitada pelo § 10, então proporcionalizada — ou
      uma proporcionalidade nua sem a base e o limite. Tratar essa dúvida
      estreita como impedimento à própria carga é desproporcional: a carga
      que `scripts/derivar.py` produz é planilha de **homologação**
      (`data/regras-propostas.csv`), o lugar exato onde essa conferência de
      campo acontece — não é ativação em produção, que continua sendo ato
      posterior e exclusivo do IPERON (`okf/spec/ciclo.md`). `ressalva_homologacao`
      registra o que fica pendente para quem homologa; a derivação jurídica
      não é reaberta.
confianca: media
---

# Síntese

Para servidor ingressado após 31/12/2003 cuja incapacidade decorra de causa
comum, o § 14 remete ao art. 26: média do art. 24, limitada previamente pelo
teto do § 10 do próprio art. 24, proporcionalizada em dias. O reajuste segue
o art. 27, II, sem paridade.

A regra hoje cadastrada precisa ser substituída pelo mesmo vício da sua
correspondente até 2003: ela é o ramo residual, mas a sua fundamentação é a das
causas qualificadas — acidente em serviço, moléstia profissional e doença grave,
contagiosa ou incurável —, que são justamente as que a residual exclui. Aqui são
três dessas fundamentações empacotadas na mesma célula; lá, uma. Além disso, o
rótulo `Proporcionalidade Dias` não expressa sozinho a base média.

# Requisitos da matriz do Ciclo 1

Esta regra materializa os requisitos `C1-R00`, `C1-R10`, `C1-R12`, `C1-R13`, `C1-R20`, `C1-R25`, `C1-R30`, `C1-R32`, `C1-R40`, `C1-R42`, `C1-R50`, `C1-R52`, `C1-R70`, `C1-R71`, `C1-R73`, `C1-R74` da
[matriz de derivação e verificação do Ciclo 1](../../../docs/analysis/matriz-derivacao-verificacao-ciclo-01.md). A correspondência
estrutural entre esta regra e esses requisitos foi verificada
programaticamente. Os requisitos não programáticos são verificados no caso
concreto conforme responsável, evidência e momento definidos na matriz.

# Pendências localizadas

- [ ] `C1-R32` — auditoria jurídica concluída (`estado_auditoria: concluida`);
  unidade admitida na carga de homologação com ressalva
  (`estado_implantacao: confirmada_com_ressalva`): `regra-0021` já grava, em
  produção, `integral: N` e `tipo_calculo: Proporcionalidade Dias` para esta
  mesma hipótese, o que sustenta a presunção de que o Sisprev já executa
  algum mecanismo para ela. O que falta confirmar em homologação prática,
  antes da ativação em produção, é mais estreito: se a execução aplica a
  base composta do art. 26 — média do art. 24, limitada pelo § 10, então
  proporcionalizada — e não uma proporcionalidade nua (`ressalva_homologacao`,
  issue #122, issue #124). Dependência de homologação, não pendência de
  derivação: origem legada (`regra-0021`) preservada como fonte operacional
  até a confirmação.
