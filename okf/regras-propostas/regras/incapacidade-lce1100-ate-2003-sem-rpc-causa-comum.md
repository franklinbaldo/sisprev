---
type: RegraProposta
id: incapacidade-lce1100-ate-2003-sem-rpc-causa-comum
ciclo: ciclo-01
schema_version: 1
estado_auditoria: concluida
estado_implantacao: confirmada_com_ressalva
ressalva_homologacao: >-
  Confirmar em homologação prática que `Proporcionalidade Dias`, nesta hipótese, executa
  a fração do art. 26 sobre a remuneração do cargo efetivo do art. 25, e não uma
  proporcionalidade nua sobre a remuneração. Se o sistema executar outra base, a regra
  não estará homologada e a divergência deverá retornar para decisão jurídica e
  institucional antes da ativação em produção.
origens_legacy:
  - regra-0020
predicados:
  causa_incapacidade: causa_comum
  regime: lce1100-incapacidade-ate-2003-sem-rpc
  vinculo_rpc: nao_aderiu
  selecao_por:
    - ingresso_na_janela
    - ausencia_de_opcao_rpc
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente não decorre de acidente em serviço nem de hipótese
      equiparada, de moléstia profissional, de doença do rol do art. 30, § 8º, nem de
      outra hipótese legalmente qualificada
    protocolo_verificacao:
      pergunta: >-
        A investigação foi suficiente para excluir acidente em serviço e hipóteses
        equiparadas, moléstia profissional, as moléstias do art. 30, § 8º, e demais
        hipóteses legalmente qualificadas aplicáveis ao caso?
      responsavel: perícia médica oficial indicada pelo IPERON e instrução previdenciária
      momento: instrução e seleção da regra
      meio_de_prova: >-
        laudo da perícia médica oficial, prontuários, histórico ocupacional, apuração de
        eventual acidente e cotejo com o rol legal
      evidencia_exigida: >-
        incapacidade para as atribuições do cargo e impossibilidade de readaptação
        comprovadas, e investigação suficiente das causas qualificadas — silêncio ou
        prova insuficiente não bastam
    portador_primario: fundamentacao_proporcional
aplicabilidade_temporal:
  datas_legadas:
    data_adm_ate: 31/12/2003 00:00
    data_adm_apos: 01/01/1950 00:00
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
      determina o ramo residual proporcional
  - ref: /dispositivos/lce-1100-2021/art-30-par-8/original.md
    papel: >-
      relaciona as moléstias qualificadas, cuja exclusão esta regra exige apurar
  - ref: /dispositivos/lce-1100-2021/art-30-par-14/original.md
    papel: >-
      remete o cálculo desta classe de causa ao art. 26
  - ref: /dispositivos/lce-1100-2021/art-25/original.md
    papel: >-
      disciplina a base de cálculo desta família: totalidade da remuneração do cargo
      efetivo
  - ref: /dispositivos/lce-1100-2021/art-26/original.md
    papel: >-
      fornece a proporcionalização em dias sobre a base do art. 25
  - ref: /dispositivos/lce-1100-2021/art-27-inc-i/original.md
    papel: >-
      assegura paridade a quem ingressou até 31/12/2003 e não fez a opção do § 16 do
      art. 40 da Constituição Federal
  - ref: /dispositivos/ec-41-2003/art-7/original.md
    papel: >-
      define o conteúdo da paridade: revisão na mesma proporção e na mesma data da
      remuneração dos servidores em atividade
  - ref: /dispositivos/cf88/art-40-par-16/ec-103-2019.md
    papel: >-
      subordina o regime de previdência complementar a opção prévia e expressa, cuja
      ausência é condição desta família
projecao:
  nome: >-
    Incapacidade · causa comum — excluídas as causas qualificadas · ingresso até 2003 e
    não aderiu ao RPC · remuneração do cargo proporcional · com paridade
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
  integral: N
  tipo_calculo: Proporcionalidade Dias
  fundamentacao_proporcional: >-
    No curso do processo administrativo, ficou demonstrado que o interessado era
    servidor titular de cargo efetivo e que a perícia médica oficial indicada pelo
    IPERON atestou incapacidade permanente para o desempenho das atribuições do cargo e
    impossibilidade de readaptação. O laudo pericial fixou a data certa ou provável em
    que o interessado se tornou incapaz para o desempenho das atribuições do cargo e
    para a readaptação e, onde não foi possível fixá-la, justificou os motivos
    impeditivos. A aposentadoria foi precedida de afastamento do trabalho por período
    não excedente a vinte e quatro meses, ao fim do qual o interessado foi
    obrigatoriamente reavaliado e não se encontrava em condições de reassumir o cargo
    nem de ser readaptado. Ficou demonstrado, ainda, que a incapacidade não decorreu de
    acidente em serviço nem de hipótese a ele equiparada, de moléstia profissional, de
    doença grave, contagiosa ou incurável juridicamente qualificada, nem de moléstia
    relacionada no art. 30, § 8º, da Lei Complementar Estadual nº 1.100/2021, nem de
    outra hipótese legalmente qualificada aplicável ao caso — exclusão que foi objeto de
    investigação própria, com apuração de eventual acidente, exame do histórico
    ocupacional e cotejo do diagnóstico com o rol legal, e não de mero silêncio dos
    autos. Ficou demonstrado, por fim, que o ingresso no serviço público em cargo
    efetivo se deu até 31 de dezembro de 2003, que o interessado não fez a opção pelo
    regime de previdência complementar de que trata o § 16 do art. 40 da Constituição
    Federal, e que os requisitos foram implementados a partir de 18 de outubro de 2021.


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
    readaptado. O art. 30, caput, fixa a regra e a exceção: os proventos são
    proporcionais ao tempo de contribuição, salvo se a incapacidade decorrer de acidente
    em serviço, moléstia profissional ou doença grave, contagiosa ou incurável. Esta
    regra é o ramo residual — aplica-se justamente quando nenhuma dessas causas se
    verifica —, e daí decorre que a exclusão precisa ser apurada, e não presumida do
    silêncio: é ela que distingue esta hipótese das qualificadas, e quem não a investiga
    concede provento reduzido a quem talvez tivesse direito ao integral. O § 14 do art.
    30 remete o cálculo da causa comum ao art. 26. Para quem ingressou no serviço
    público em cargo efetivo até 31 de dezembro de 2003 e não fez a opção do § 16 do
    art. 40 da Constituição Federal, é o art. 25 que disciplina a base de cálculo — a
    totalidade da remuneração do cargo efetivo —, e o art. 27, inciso I, que assegura a
    paridade, cujo conteúdo está no art. 7º da Emenda Constitucional nº 41/2003.


    Para os servidores que ingressaram no serviço público até 31 de dezembro de 2003 e
    não fizeram a opção pelo regime de previdência complementar, a base de cálculo é a
    totalidade da remuneração do cargo efetivo prevista no art. 25 da LCE nº 1.100/2021,
    proporcionalizada pelo tempo de contribuição na forma do art. 26, com paridade nos
    termos do art. 27, I. Após a concessão, os proventos são reajustados na mesma
    proporção e na mesma data da remuneração dos servidores em atividade, na forma do
    art. 7º da Emenda Constitucional nº 41/2003, a que o art. 27, inciso I, remete. A
    paridade é regime de revisão posterior e não integra o cálculo inicial.
proveniencia:
  fontes_consultadas:
    - /tipos-calculo/tipo-calculo-remuneracao-cargo-proporcional-dias-lce1100.md
    - /dispositivos/cf88/art-40-par-1-inc-i/ec-103-2019.md
    - /dispositivos/lce-1100-2021/art-30-par-1/original.md
    - /dispositivos/lce-1100-2021/art-30-par-2/original.md
    - /dispositivos/lce-1100-2021/art-30-par-3/original.md
    - /dispositivos/lce-1100-2021/art-30-par-4/original.md
    - /dispositivos/lce-1100-2021/art-30-caput/original.md
    - /dispositivos/lce-1100-2021/art-30-par-8/original.md
    - /dispositivos/lce-1100-2021/art-30-par-14/original.md
    - /dispositivos/lce-1100-2021/art-25/original.md
    - /dispositivos/lce-1100-2021/art-26/original.md
    - /dispositivos/lce-1100-2021/art-27-inc-i/original.md
    - /dispositivos/ec-41-2003/art-7/original.md
    - /dispositivos/cf88/art-40-par-16/ec-103-2019.md
  notas: >-
    Uma regra por causa e por regime de ingresso/RPC. Esta unidade cobre exclusivamente
    causa comum — excluídas as causas qualificadas na família «ingresso até 2003 e não
    aderiu ao RPC». A fórmula está decomposta em `tipo-calculo-remuneracao-cargo-
    proporcional-dias-lce1100`. Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Reconhecer a existência da combinação representada por regra-0020,
      corrigindo sua base para média proporcional e preservando a paridade.
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
      na carga de homologação. `regra-0020` já está em produção com
      `integral: N` e `tipo_calculo: Proporcionalidade Dias` para esta mesma
      hipótese — causa comum, ingresso até 31/12/2003 —, o que é evidência
      concreta de que o Sisprev já dispõe de mecanismo operacional para essa
      combinação; a ambiguidade que `pendente_mapeamento_sisprev` registrava
      (o mesmo rótulo também identifica `tipo-calculo-media-proporcional-dias-lce432`
      e `tipo-calculo-remuneracao-cargo-ec70-proporcional-dias`) é sobre o
      vocabulário do catálogo legado em geral, não sobre se esta hipótese
      específica tem representação no sistema — e essa segunda pergunta já
      está respondida pela própria `regra-0020` viva. A pendência
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
  - data: 2026-08-05
    quem: franklinbaldo
    o_que: >-
      Trocar a fórmula de referência de `tipo-calculo-media-proporcional-dias-lce1100` (base no art. 24) para
      `tipo-calculo-remuneracao-cargo-proporcional-dias-lce1100` (base no
      art. 25), por revisão jurídica adicional da coordenação, sem alterar
      `integral: N` nem `tipo_calculo: Proporcionalidade Dias` — ambos já
      corretos e já gravados por `regra-0020` em produção. A leitura
      anterior — base no art. 24 via art. 30, § 14 → art. 26 — é
      juridicamente construível a partir da remissão daqueles dispositivos,
      mas conflita com o art. 25, que rege expressamente, com a mesma
      grafia do art. 27, I, a coorte "que tenha ingressado no serviço
      público em cargo efetivo até 31 de dezembro de 2003"; e carece de
      jurisprudência específica ou precedente administrativo interno
      inequívoco. A orientação conservadora adotada preserva a coerência de
      regime pela coorte, alinhando esta regra às causas qualificadas da
      mesma coorte (que passam de `Valor Médio` para `Valor Efetivo` na
      mesma revisão): quem ingressou até 2003 calcula sobre a remuneração
      do cargo (art. 25), proporcionalizada em dias para a causa comum e
      integral para as qualificadas, sempre com paridade; quem ingressou
      depois calcula pela média (art. 24), sem paridade.
  - data: 2026-08-05
    quem: franklinbaldo
    o_que: >-
      Corrigir o fundamento e a `ressalva_homologacao` registrados na
      decisão anterior desta mesma data, em revisão adicional da
      coordenação. Dois problemas na formulação anterior. **Primeiro**, o
      fundamento: a decisão anterior apresentava o art. 25 como a "outra
      fórmula" ressalvada pelos §§ 13/14 do art. 30, comprovada por
      direito adquirido via `regra-0019`/`regra-0020`. Isso está
      incorreto. A leitura adotada é outra: o servidor ingressado até
      31/12/2003 requer a aposentadoria por incapacidade pela regra
      permanente atual da LCE 1.100/2021, e é o art. 25, dentro desse
      próprio regime vigente, que disciplina diretamente a base de
      cálculo dessa coorte, inclusive para a causa comum — harmonizando
      os arts. 24 e 25 como divisão vigente de coortes, não como direito
      adquirido a regime anterior. A ressalva dos §§ 13/14 ao direito
      adquirido é proteção adicional e independente, não o fundamento
      necessário para aplicar o art. 25. `regra-0020` serve como
      evidência da prática operacional anterior do Sisprev e do enum já
      utilizado, não como prova de direito adquirido dos servidores.
      **Segundo**, a `ressalva_homologacao`: a redação anterior tratava a
      base do art. 24 (a fórmula composta do art. 26, § 1º) e a base do
      art. 25 como dois resultados igualmente aceitáveis para a
      homologação. Isso inverte a função do mecanismo — a homologação
      verifica se o sistema executa a decisão jurídica adotada, não
      escolhe entre duas interpretações da lei. `ressalva_homologacao`
      passa a descrever um único resultado esperado (fração do art. 26
      sobre a base do art. 25) e a tratar a execução de outra base como
      falha de homologação a devolver para decisão jurídica e
      institucional, não como alternativa válida. A tensão entre os arts.
      25 e 30 (§§ 13 e 14, e a literalidade do art. 26, § 1º, que remete
      à média do art. 24) permanece registrada como risco interpretativo,
      revisável diante de manifestação jurídica específica, precedente ou
      decisão institucional posterior — mas não reabre a fórmula adotada
      para a carga atual, nem transforma a homologação em instância de
      escolha entre interpretações.
  - data: 2026-08-05
    quem: franklinbaldo
    o_que: >-
      Fundamentar, para além do registro de tensão das duas decisões
      anteriores desta mesma data, por que a leitura que aplicaria a
      média do art. 24 a esta hipótese é considerada equivocada — não
      apenas uma entre duas leituras igualmente plausíveis. *Data venia*,
      entende-se equivocada a interpretação segundo a qual as remissões
      dos arts. 30, § 14, e 26, § 1º, fariam incidir a média contributiva
      do art. 24 também sobre os servidores que ingressaram até
      31/12/2003. O art. 24, no próprio *caput*, disciplina expressamente
      a base dos servidores que ingressaram **após** 31/12/2003, enquanto
      o art. 25 disciplina, também de forma expressa, a base dos que
      ingressaram **até** aquela data; ambos integram o regime permanente
      vigente da LCE 1.100/2021 e se compreendem como normas
      complementares de distribuição das bases por coorte de ingresso. O
      servidor ingressado até 31/12/2003 não está obrigado a requerer com
      fundamento em legislação revogada ou em direito adquirido — pode
      requerer segundo a lei atual, hipótese em que se aplicam os arts. 25
      e 27, I, que nomeiam a sua coorte com a mesma grafia. Interpretar a
      remissão do § 14/art. 26, § 1º, como afastamento integral do
      art. 25 exigiria admitir que, precisamente na incapacidade, a lei
      criou a combinação entre média contributiva e paridade — regime que
      a LCE 1.100/2021 não institui em nenhuma outra hipótese (a coorte
      que calcula pela média é sempre a sem paridade). Cálculo inicial e
      reajustamento são categorias distintas, e essa combinação não é
      impossível em abstrato, mas não há disposição inequívoca
      instituindo esse regime híbrido, nem precedente jurisprudencial ou
      administrativo interno seguro que o autorize por inferência; a
      leitura pelo art. 24 também reduziria o alcance do art. 25 sem que
      o § 14 tenha declarado sua inaplicabilidade à incapacidade. A
      remissão literal ao art. 24 é registrada porque pode ser invocada
      para sustentar entendimento diverso — isso não significa que as
      duas interpretações sejam consideradas igualmente corretas. Para a
      carga atual, a coordenação considera juridicamente adequada a
      aplicação do art. 25 e, *data venia*, equivocada a interpretação
      que cria, por via indireta, a combinação média contributiva com
      paridade. A fórmula poderá ser revista caso manifestação jurídica
      institucional, precedente vinculante ou decisão judicial estabeleça
      entendimento contrário — o que não transforma, desde já, a
      homologação prática em instância de escolha entre as duas leituras.
  - data: 2026-08-05
    quem: franklinbaldo
    o_que: >-
      Enxugar a fundamentação desta unidade e corrigir o fundamento do
      round 15 do RFC 0004, que restringia a tensão de remissão ao
      art. 24 à causa comum como se fosse a única hipótese afetada. Na
      causa comum, a remissão ao art. 24 ocorre pelo encadeamento entre
      o art. 30, § 14, e o art. 26, § 1º (distinta da remissão direta do
      art. 30, § 13, que afeta as causas qualificadas da mesma coorte).
      *Data venia*, entende-se que essa remissão não afasta a disciplina
      do art. 25 para a coorte de ingresso até 31/12/2003, pelas razões
      desenvolvidas em `tipo-calculo-totalidade-remuneracao-cargo-efetivo-lce1100`,
      que passa a concentrar a fundamentação antes repetida nesta e nas
      demais dezenove unidades da coorte. Mantida a fórmula: totalidade
      da remuneração do cargo efetivo (art. 25), proporcionalizada pelo
      art. 26, com paridade (art. 27, I). `ressalva_homologacao` não é
      alterada por esta decisão.
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
confianca: media
---

# Síntese

Hipótese da LCE 1.100/2021 para ingresso até 2003 e não aderiu ao RPC, com incapacidade
permanente decorrente de causa comum — excluídas as causas qualificadas, atestada por perícia médica oficial
indicada pelo IPERON quanto às atribuições do cargo e à impossibilidade de
readaptação. O cálculo é remuneração do cargo proporcional · com paridade.

# Requisitos da matriz do Ciclo 1

Esta regra materializa os requisitos `C1-R00`, `C1-R01`, `C1-R02`, `C1-R03`, `C1-R10`, `C1-R11`, `C1-R13`, `C1-R20`, `C1-R25`, `C1-R30`, `C1-R32`, `C1-R40`, `C1-R42`, `C1-R50`, `C1-R51`, `C1-R60`, `C1-R61`, `C1-R70`, `C1-R71`, `C1-R73`, `C1-R74` da
[matriz de derivação e verificação do Ciclo 1](../../../docs/analysis/matriz-derivacao-verificacao-ciclo-01.md). A correspondência
estrutural entre esta regra e esses requisitos foi verificada
programaticamente. Os requisitos não programáticos são verificados no caso
concreto conforme responsável, evidência e momento definidos na matriz.

# Pendências localizadas

Nenhuma pendência específica desta hipótese. As dependências gerais do
ciclo (`C1-R73`, `C1-R74`) estão registradas na matriz e não se repetem
aqui.
