# RFC 0004 — Schema enriquecido da auditoria e compilador determinístico para o schema legado do Sisprev

- **Status**: proposta (2026-07-23). **Especificação revisável, sem
  implementação.** Não edita nenhum `regra-*.md`, não altera o schema de
  produção, o CSV, os dispositivos, os achados, os detectores, o simulador,
  o site nem os workflows. Entrega apenas o desenho: o que se pretende
  construir, confrontado com os parsers e geradores reais do repositório.
  Revisão 2026-07-23 (round 2, após review da PR #29): resolve identidade e
  cardinalidade 1:N das regras auditadas (§1); separa Q6-R de Q6-S no
  requisito constatado pelo IPERON (§7); distingue **preview** de
  **compilação deployável** (§5.3); troca "destino único" por **papéis de
  projeção** (§4/§5); define os **três artefatos-alvo** e a **allowlist** de
  colisão do P2 (§4/§11); corrige os resíduos (datas/Q1-Q2, fonte, `ref` de
  taxonomia, simulador). Revisão 2026-07-23 (round 3): a decisão de
  **identidade separada foi ratificada pelo responsável** (§1) — não é mais
  questão aberta; consolida o modelo de identidade (incl. N:1), a regra de
  **fonte única de verdade** e o **registro de cobertura/substituição** (§1.4),
  os **estados de transição** e a seleção de origem única do exportador (§1.5),
  o **contrato de identidade da projeção** (§1.6) e os **gates separados** do
  catálogo auditado (§14). Revisão 2026-07-23 (round 4): **grupo de substituição
  atômico** (§1.4 — ativação/rollback só sobre o conjunto completo de
  descendentes); **ordenação total normativa** + `id_projecao` estável (§1.6);
  chave de colisão do P2 **ratificada** sem `dispositivos` (§11); corrige a
  referência do rol anterior para `lce-432-2008/art-20-par-9/original` (§16.2). Revisão
  2026-07-23 (round 5): separa **estado da unidade** (`elaboracao`/`preview`/
  `deployable`) de **`estado_grupo`** (`inativo`/`ativo`) e estrutura
  `decisao_completude` como campo verificável no manifesto (§1.4); Fase 2 do
  plano incremental vira **canonicidade por grupo atômico**, nunca por regra
  isolada (§15); simulador **público** restrito ao export deployable — só
  unidades de grupos ativos, com unidades em elaboração/preview isoladas num
  modo de teste/auditoria explicitamente não-deployable (§12). Revisão
  2026-07-23 (round 6): rebase sobre a `main` pós-merge de #27/#28; reconcilia
  as referências desatualizadas — estado preciso das pendências do PR #27
  por categoria (P-5 cobertura concluída/vinculação futura, P-6 lacuna
  normativa documentada, P-1/P-2/P-3/P-4 e temporalidade do rol como decisão
  jurídica substantiva pendente, Q6-S aberta — §18); confirma que o simulador
  público do PR #28 permanece o filtro conservador sobre o legado (§12). Sem
  mudança de arquitetura. Revisão 2026-07-23 (round 7, dois decisões do
  responsável): **(a)** o simulador público é redefinido como **experimental,
  de site pessoal, não oficial do IPERON** — a restrição do round 5 (só
  export deployable) é **removida**; §12 passa a distinguir a **regra do
  exportador** (§12.1, inalterada — só unidades `deployable` de grupos ativos
  vão para o schema do Sisprev) do **pipeline de simulação exploratório**
  (§12.2, novo — três universos comparáveis, sem efeito sobre
  manifesto/ativação/compilação/exportação, resultado sempre explicável e
  rotulado como não oficial); **(b)** abandona a terminologia "requisito não
  parametrizável" — todo requisito verificável por humano **é modelável**
  (§7): decompõe em **predicado** (Q6-R), **fato da solicitação** (Q6-S, por
  caso), **protocolo de verificação** (Q6-R), **constatação concreta** (Q6-S,
  por caso) e **avaliação** (`satisfeito`/`não satisfeito`/`indeterminado` —
  nunca "não avaliável"); renomeia `requisitos_nao_parametrizaveis` para
  `requisitos_verificacao_humana` com `predicado`/`protocolo_verificacao`
  estruturados (§3/§4/§5/§6/§16). Revisão 2026-07-23 (round 8, revisão final
  de 3c57f44 — quatro resíduos documentais, sem mudança de arquitetura):
  corrige §15 (Fase 1/2), que ainda reintroduzia a restrição revogada do
  round 5 — desde a Fase 1 o simulador exploratório já pode comparar o
  legado com o universo auditado experimental (§12.2); a Fase 2 **acrescenta**
  o universo ativo/deployable, sem remover o experimental; corrige §5.2/§8,
  que ainda falavam em geração/migração "por regra" — autoria/revisão podem
  ser por unidade, mas a transição operacional (geração `deployable`,
  ativação, substituição) é **sempre por grupo atômico** (§1.4); precisa em
  §3 que "não representável" nunca descreve o schema enriquecido (A) — todo
  requisito verificável é modelável em A, só pode faltar campo estruturado
  em B, caso em que compila para `nome`/`fundamentacao*`; e introduz
  `base_avaliacao` (`hipotese_informada`/`constatacao_documentada`/
  `sem_informacao`) no pipeline exploratório (§12.2), para que uma resposta
  do usuário nunca seja confundida com uma constatação real do IPERON.
  Revisão 2026-08-05 (round 9, achado do Ciclo 1 — colisão de `tipo_calculo`
  entre fórmulas juridicamente distintas sob o mesmo rótulo legado,
  `docs/analysis/matriz-derivacao-verificacao-ciclo-01.md`): separa, dentro
  de `deployable`, duas afirmações que o round 5 tratava como uma só —
  **derivação jurídica concluída** (a fórmula que a lei exige está
  determinada) e **projeção confirmada no Sisprev** (o valor de domínio
  fechado que a representa é o que o sistema já reconhece, sem ambiguidade
  material). Introduz `estado_implantacao` (`confirmada`, implícito quando
  ausente, ou `pendente_mapeamento_sisprev`) em `RegraProposta`
  (`okf/spec/regraproposta.md`) para a segunda afirmação, quando ela precisa
  ser feita separadamente da primeira. `deployable` sozinho não muda de
  sentido para o caso comum, em que as duas coincidem. §1.4/§1.5 (grupo
  atômico, seleção de origem única) não mudam: para o efeito de trocar a
  fonte operacional de exportação, `estado_grupo: ativo` continua exigindo
  `estado_implantacao: confirmada` em todos os destinos, além de
  `deployable` — porque as origens legadas de um grupo tipicamente cobrem
  mais de uma hipótese juntas, e não há, em geral, substituição parcial
  segura (`okf/spec/conjunto.md`). O que muda é que uma unidade
  `deployable`/`estado_implantacao: pendente_mapeamento_sisprev` conta como
  derivação jurídica concluída para fins de fechamento do ciclo (§5.3,
  abaixo) e de leitura por quem homologa, ainda que não troque a fonte
  operacional do grupo a que pertence.
  Revisão 2026-08-05 (round 10, mesmo achado — a atomicidade do lote de
  substituição não é incompletude jurídica do grupo): o round 9 separou os
  dois estados **da unidade**; este round separa os dois papéis **do
  grupo**, que §1.4 ainda misturava — `decisao_completude` deixa de ser
  zerada quando `estado_grupo` está `inativo` por pendência de implantação
  (era: "obrigatório para `ativo`, ausente/null enquanto inativo"; passa a:
  presente sempre que a decisão jurídica existir, independente de
  `estado_grupo`). `estado_grupo` deixa de ser um campo decidido à parte e
  passa a ser **computado** a partir de três fatos que `Conjunto` já tem:
  `decisao_completude` preenchida, todos os destinos `deployable`, todos os
  destinos `estado_implantacao: confirmada` — `ativo` só quando os três
  coincidem, `inativo` em qualquer outro caso, sem precisar dizer qual
  faltou fora do próprio manifesto. Não introduz tipo, schema ou gate novo:
  é regra de leitura de dois campos existentes de `Conjunto`
  (`okf/spec/conjunto.md`).
  Revisão 2026-08-05 (round 11, simplificação estrutural pedida pela
  coordenação): **`Conjunto` e o "grupo de substituição" são eliminados
  como entidades canônicas.** Tudo o que os rounds 4–10 desta RFC atribuíam
  ao manifesto de grupo — `grupo`, `origens_legacy`/`destinos_auditados`
  declarados à parte, `estado_grupo` — passa a ser **derivado**: cada
  `RegraProposta` já declara `origens_legacy` diretamente
  (`okf/spec/regraproposta.md`), e `scripts/derivar.py` computa os
  componentes conexos do grafo origem↔destino a cada execução. Um
  componente entra na carga de implantação quando todos os seus membros
  têm `estado_auditoria: concluida` (renomeado de `estado_proposta: deployable` — o nome antigo carregava a mesma confusão entre derivação
  jurídica e prontidão técnica que os rounds 9/10 já vinham desfazendo) e
  `estado_implantacao: confirmada`; nunca há ato de ativação declarado à
  parte. `decisao_completude` não desaparece: passa a viver como decisão
  datada no `Ciclo` responsável e/ou no log `decisoes` de cada
  `RegraProposta` do componente, não como campo de um manifesto de grupo.
  Revogação sem substituta (`Conjunto.revoga`) passa para `Regra.revogada`
  (`okf/spec/regra.md`). §1.4 e §1.5, abaixo, descrevem o mecanismo
  retirado; ver a nota ao final de §1.5 para o que o substitui. Esta
  mudança **não reabre** nenhuma derivação jurídica já concluída — é
  reorganização de onde o fato mora, não novo mérito.
  Revisão 2026-08-05 (round 12, achado do Ciclo 1 — causa comum da LCE
  1.100/2021): o round 9 tratava `estado_implantacao: pendente_mapeamento_sisprev` como bloqueio uniforme à carga, mas a
  própria spec já descrevia esse valor como "a fórmula está determinada, só
  falta confirmação de identificação unívoca" — afirmação mais fraca do que
  "não se sabe que mecanismo do sistema a fórmula ocupa". A carga que
  `scripts/derivar.py` produz (`data/regras-propostas.csv`) é planilha de
  **homologação**, não ativação em produção; retê-la quando já existe
  evidência operacional concreta — a origem legada em produção com a
  mesma projeção de vocabulário fechado, para a mesma hipótese — inverte a
  função da homologação, que existe para confirmar exatamente esse tipo de
  detalhe de execução. `estado_implantacao` ganha um terceiro valor,
  `confirmada_com_ressalva`, que entra na carga levando
  `ressalva_homologacao` — o que falta confirmar antes da ativação em
  produção. `pendente_mapeamento_sisprev` continua fora da carga para o
  caso em que não há essa evidência. Aplicado no Ciclo 1 às duas unidades
  de causa comum da LCE 1.100/2021 (`incapacidade-lce1100-ate-2003-causa-comum`,
  `incapacidade-lce1100-apos-2003-causa-comum`): `regra-0020` e
  `regra-0021` já gravam, em produção, `integral: N` e
  `tipo_calculo: Proporcionalidade Dias` para as mesmas hipóteses, o que
  sustenta a presunção necessária para a carga; a execução completa da
  fórmula do art. 26 — média do art. 24, limitada pelo § 10, então
  proporcionalizada — permanece sujeita a confirmação em homologação
  prática antes da ativação em produção. Não reabre a derivação jurídica de
  nenhuma das quarenta unidades do Bloco C.
  Revisão 2026-08-05 (round 13, revisão jurídica adicional da coordenação
  sobre as vinte unidades da coorte de ingresso até 31/12/2003 do Bloco C):
  a solução do round 12 gravava, para essa coorte, a combinação `Valor Médio` (art. 24) + `paridade: S`, construída a partir da remissão do
  art. 30, §§ 13 e 14, ao art. 24. A coordenação aponta que essa leitura
  conflita com o art. 25 — que rege expressamente, com a mesma grafia do
  art. 27, I, "quem tenha ingressado no serviço público em cargo efetivo
  até 31 de dezembro de 2003" —, altera a fórmula que `regra-0019` já
  grava em produção para as causas qualificadas dessa mesma coorte
  (`tipo_calculo: Valor Efetivo`, citando o próprio art. 25 em
  `dispositivos:`) e carece de jurisprudência específica ou precedente
  administrativo interno inequívoco. A orientação conservadora adotada
  preserva a coerência de regime pela coorte de ingresso, e não mais só
  pela causa: quem ingressou até 2003 calcula sobre a remuneração do cargo
  (art. 25), integral para as causas qualificadas e proporcional em dias
  para a causa comum, sempre com paridade (art. 27, I); quem ingressou
  depois calcula pela média (art. 24), sem paridade — sem mudança nesta
  segunda metade, cuja base nunca esteve em disputa. Aplicado às dezenove
  unidades de causa qualificada da coorte até 2003
  (`incapacidade-lce1100-ate-2003-*`, exceto `causa-comum`): `tipo_calculo`
  passa de `Valor Médio` para `Valor Efetivo`,
  `tipo-calculo-totalidade-remuneracao-cargo-efetivo-lce1100` (base no
  art. 25) substitui `tipo-calculo-media-80-contribuicoes-lce1100` (base no
  art. 24) como fundamento. Aplicado à unidade de causa comum da mesma
  coorte (`incapacidade-lce1100-ate-2003-causa-comum`): `tipo_calculo`
  permanece `Proporcionalidade Dias` e `integral: N` — ambos já corretos e
  já gravados por `regra-0020` em produção —, mas
  `tipo-calculo-remuneracao-cargo-proporcional-dias-lce1100` (base no
  art. 25) substitui `tipo-calculo-media-proporcional-dias-lce1100` (base
  no art. 24) como fundamento, e `ressalva_homologacao` passa a registrar
  as duas leituras possíveis da base (art. 24 ou art. 25), ambas
  compatíveis com o único valor que o Sisprev grava para a hipótese. A
  tensão entre os arts. 25 e 30 (§§ 13 e 14) — se o art. 25 é a "outra
  fórmula" ressalvada por aqueles parágrafos para a coorte de ingresso até
  2003 — fica registrada como questão interpretativa em aberto, não
  decidida em definitivo, em cada uma das vinte unidades afetadas
  (`decisoes`) e nos dois `TipoCalculo` correspondentes; revisável diante
  de manifestação jurídica específica, precedente ou decisão institucional
  posterior. Não reabre a derivação jurídica de nenhuma das quarenta
  unidades do Bloco C quanto ao mérito da causa (qualificada × comum) nem
  quanto à coorte de ingresso — move apenas a base de cálculo da coorte
  até 2003, de volta ao valor que já está em produção.
  Revisão 2026-08-05 (round 14, correção de fundamento e de ressalva pedida
  pela coordenação sobre o round 13): dois ajustes ao round anterior, sem
  reabrir a fórmula adotada. **Primeiro, o fundamento.** O round 13
  apresentava o art. 25 como a "outra fórmula" ressalvada pelos §§ 13/14 do
  art. 30, comprovada por direito adquirido via `regra-0019`/`regra-0020`.
  Essa formulação está incorreta. O servidor ingressado até 31/12/2003
  requer a aposentadoria por incapacidade pela regra permanente atual da
  LCE 1.100/2021, e é o art. 25, dentro desse próprio regime vigente, que
  disciplina diretamente a base de cálculo dessa coorte — harmonizando os
  arts. 24 e 25 como divisão vigente de coortes, não como direito
  adquirido a regime anterior. A ressalva dos §§ 13/14 ao direito
  adquirido é proteção adicional e independente, não o fundamento
  necessário para aplicar o art. 25. `regra-0019`/`regra-0020` servem como
  evidência da prática operacional anterior do Sisprev e dos enums já
  utilizados, não como prova de direito adquirido dos servidores.
  **Segundo, a ressalva de homologação da causa comum.** O round 13
  reescreveu `ressalva_homologacao` da unidade
  `incapacidade-lce1100-ate-2003-causa-comum` para registrar "as duas
  leituras possíveis da base (art. 24 ou art. 25), ambas compatíveis" —
  tratando-as como alternativas igualmente válidas para a homologação.
  Isso inverte a função do mecanismo: a homologação verifica se o sistema
  executa a decisão jurídica adotada, não escolhe entre interpretações da
  lei. `ressalva_homologacao` passa a descrever um único resultado
  esperado — a fração do art. 26 sobre a base do art. 25 — e a tratar a
  execução de outra base como falha de homologação a devolver para
  decisão jurídica e institucional, não como alternativa válida. Em
  nenhum dos dois ajustes a fórmula adotada para a carga muda: continua
  sendo o art. 25 para a coorte até 2003 e o art. 24 para a coorte a
  partir de 2004, exatamente como o round 13 já havia fixado. A tensão
  entre os arts. 25 e 30 (§§ 13/14, e a literalidade do art. 26, § 1º)
  permanece registrada como risco interpretativo, revisável diante de
  manifestação jurídica específica, precedente ou decisão institucional
  posterior — sem transformar a homologação em instância de escolha entre
  leituras.
- **Parte de / depende de**: [RFC 0001](0001-criterios-de-validacao-das-regras.md)
  (semântica adiada, autoria humana, P2/P2.1/P3/P5/P7/P13, as 27 colunas),
  [RFC 0002](0002-selecao-explicavel-pos-anamnese.md) (seleção explicável,
  papel do `nome`), a spec P13.1
  ([`okf/spec/regra.md`](../../okf/spec/regra.md)), o dossiê Q6
  ([`docs/analysis/q6-causa-incapacidade.md`](../analysis/q6-causa-incapacidade.md))
  e a reconciliação invalidez/incapacidade
  ([`docs/analysis/reconciliacao-invalidez-incapacidade.md`](../analysis/reconciliacao-invalidez-incapacidade.md)).
- **Não-objetivo**: implementar a migração; responder qualquer das questões
  Q1–Q12; fechar Q6-S; redigir `fundamentacao*` definitiva para qualquer
  regra; fixar a gramática de `nome`; transformar interpretação provisória
  em gate de CI (princípio da semântica adiada, RFC 0001).

> **Nota de renomeação (2026-08-03).** O conceito que esta RFC chama de
> **unidade auditada** (`type: UnidadeAuditada`, bundle `okf/regras-auditadas/`)
> foi renomeado para **regra proposta** (`type: RegraProposta`, bundle
> `okf/regras-propostas/`), com o subdiretório `unidades/` virando `regras/`,
> `estado_unidade` virando `estado_proposta` e `destinos_auditados` virando
> `destinos_propostos`. O corpo desta RFC é mantido **verbatim**, com a
> nomenclatura da época: ela é o registro da decisão como foi tomada, e
> reescrevê-la apagaria o que se decidiu quando.
>
> Duas razões para a troca. "Unidade" não dizia o que a coisa é — o documento
> é uma regra inteira, com nome e parâmetros próprios, pronta para ocupar uma
> linha do Sisprev, e "unidade" sugeria fragmento ou rascunho. E o termo
> colidia com o uso corrente de "unidade de decisão" para designar o grupo de
> substituição, que é outra coisa.
>
> "Regra homologada" foi considerado e recusado: nenhuma dessas regras foi
> homologada, e o caminho do arquivo afirmaria um estado que o
> `estado_proposta` de cada documento desmente. Pela mesma razão por que
> `validado_pge` é consequência e não insumo, e por que `preview` é sempre
> `deployable=False`, o nome do bundle não pode antecipar o ato.

> **Nota de retirada e renomeação (round 11, 2026-08-05).** O mesmo
> princípio da nota acima vale aqui: o corpo desta RFC é mantido
> **verbatim**, e onde o corpo diverge do que vale hoje, o que vale hoje é
> o que está escrito nesta nota e na emenda do round 11 ao final de §1.5
> (não o texto anterior de §1.4/§1.5/§5.3/§7/§11/§14–17, que descreve o
> mecanismo retirado). Três mudanças atravessam o documento inteiro sem
> que cada seção precise repeti-las: `estado_proposta` foi renomeado
> `estado_auditoria`, e o valor `deployable` renomeado `concluida`; o
> **manifesto de grupo de substituição** (`Conjunto`, `grupo`,
> `estado_grupo`) foi eliminado e substituído por **componentes conexos**
> do grafo origem↔destino, computados por `scripts/derivar.py` a partir de
> `origens_legacy` — onde o texto abaixo diz "grupo atômico" ou
> "`estado_grupo: ativo`", leia-se "componente pronto para implantação";
> `decisao_completude` deixou de ser campo de um manifesto e passa a viver
> como decisão datada no `Ciclo` responsável ou no log `decisoes` de cada
> `RegraProposta`. Nenhum invariante muda: a troca continua sendo
> tudo-ou-nada por lote, `P_EXPORT_ORIGEM_DUPLA` continua valendo, e a
> decisão jurídica continua exigindo autor, data, justificativa e fonte —
> só a forma de declarar e computar isso mudou.

## 0. Decisão de arquitetura que motiva esta RFC

> O schema atual do Sisprev **deixa de ser o limite da análise**. Ele passa
> a ser um **formato-alvo legado** para o qual as regras auditadas serão
> **compiladas**.

Hoje, o frontmatter das 27 colunas **é** a regra deployável (RFC 0001,
P13.2): o auditor edita diretamente `integral`, `tipo_calculo`,
`fundamentacao*`, e o `okf_to_csv.py` projeta isso na CSV derivada. O
problema estrutural, já documentado, é que **a semântica jurídica que
distingue duas regras muitas vezes não cabe em nenhuma das 27 colunas** — o
caso central é a **causa da incapacidade**, pela qual a PGE separa hipóteses
que o catálogo não tem como campo (reconciliação §2, o cruzamento
`0022 × P6/P7`; Q6 §2). O `integral`/`tipo_calculo` são o **resultado já
pré-computado** da causa, nunca o **predicado** que diz *quais* causas o
produzem.

Esta RFC formaliza a separação entre:

- **(A) o schema enriquecido da auditoria** — onde vivem os predicados
  jurídicos estruturados, a classe da causa, os requisitos de verificação
  humana (predicado, protocolo de verificação, meio e responsável pela
  constatação — §7), a aplicabilidade temporal, os dispositivos vinculados,
  as taxonomias e vigências, e os metadados de auditoria (evidência,
  proveniência, confiança, decisões); e
- **(B) o schema legado do Sisprev, com as 27 colunas** — o formato-alvo,
  para o qual (A) é **compilado** por um passo determinístico.

E define o **contrato do compilador A → B**: toda semântica operacional
necessária à seleção e aplicação de uma regra tem de ser projetável para o
alvo, com **papéis de projeção declarados** (§4), ou a compilação **falha** —
nunca descarta em silêncio.

**Por que compilar, e não simplesmente ampliar o alvo** (confirmado pela
coordenação da auditoria em 2026-07-28, registrado na spec P13.1,
[`okf/spec/regra.md`](../../okf/spec/regra.md)):

> Alterar enum altera o sistema; o nosso trabalho com as regras é de
> **parametrização**.

Acrescentar coluna ou membro de enum ao alvo é mudar o **Sisprev** — está
fora do escopo da auditoria. É por isso que (B) é tratado como formato-alvo
**fixo** e a riqueza fica toda em (A): a alternativa "basta criar a coluna
que falta" não é uma alternativa disponível. O `_checar_contrato_legado` do
compilador é onde essa fronteira é verificada — uma unidade auditada válida
ainda falha a compilação `deployable` se o valor projetado não for um que o
alvo já aceite.

**Precisão do round 10.** Essa fronteira é sobre o **alvo B** — as 27
colunas e o que elas já aceitam —, não sobre o **catálogo A**. Criar, em
`okf/tipos-calculo/`, múltiplos `TipoCalculo` canônicos que compartilham a
mesma `origem_legada.tipo_calculo` (`okf/spec/tipocalculo.md`) é
parametrização do catálogo enriquecido — exatamente o que P13.1 já
autorizava —, não ampliação do alvo: nenhuma coluna nem membro de enum do
Sisprev é criado, removido ou renomeado por isso. A tradução de volta —
se um `TipoCalculo` sem origem legada unívoca vira novo valor cadastrado,
combinação de colunas, ou rotina nova — continua decisão do
IPERON/fornecedor, e continua fora do escopo da auditoria decidi-la
sozinha; mas essa decisão pendente não impede a existência do tipo
canônico nem a conclusão da derivação que o produziu.

A mesma confirmação diz que **a granularidade da aferição é conveniência do
IPERON** ("doença da lista" versus uma regra por doença). É a base
declarativa da cardinalidade livre de §1.2: decompor 1:N e consolidar N:1 não
são correções de erro, são escolhas de granularidade — e consolidar é a saída
*dentro do escopo* quando duas regras distintas não têm, no alvo, nenhum
parâmetro que as separe.

## 1. Fonte canônica, identidade e cardinalidade das regras auditadas

### 1.1 O que é canônico — e de quê (terminologia)

Há **duas** fontes canônicas, com papéis **distintos** — a palavra "canônica"
sozinha é ambígua e esta RFC não a usa sem qualificador:

- **Fonte canônica histórica (as-is)** — o bundle legado
  `okf/regras-sisprev/` (as 112 linhas importadas). É a representação
  rastreável do que o Sisprev tinha, **imutável quanto à sua cardinalidade e
  identidade** (não perde, não renumera, não funde linhas). **Continua sendo a
  fonte canônica histórica mesmo depois** de uma regra ser auditada — o que ela
  deixa de ser é a fonte *operacional* daquela regra.
- **Fonte canônica operacional (proposta validada)** — a **unidade auditada**,
  um conceito OKF com **arquivo e identidade próprios** num bundle separado
  (§1.2). Para as regras **já auditadas**, é ela que carrega a semântica
  operacional (o bloco `auditoria:`).
- **Artefato derivado** — a projeção de 27 colunas (o alvo Sisprev) é
  **derivada** da fonte operacional da regra; nunca autorada diretamente para
  uma regra já auditada (§1.4).

Acrescenta-se **uma única chave nova de frontmatter** na unidade auditada,
`auditoria:` (um mapa aninhado), que carrega a semântica operacional; as
colunas deployáveis tornam-se sua **projeção compilada**. Nada disso reintroduz
um banco paralelo (RFC 0001, "autoria humana").

### 1.2 Identidade e cardinalidade das unidades auditadas (ratificada)

O caso central `0022 → P6/P7` **não cabe** num modelo que exija, ao mesmo
tempo: um bloco `auditoria:` por regra, `causa_incapacidade` **escalar**, uma
linha por classe material, e nenhuma linha legada tocada. `0022` representa
**pelo menos duas** classes de causa (doença catalogada **e** acidente em
serviço). Um escalar não comporta as duas; e a auditoria precisa de duas
linhas materialmente distintas. É preciso decidir a cardinalidade
explicitamente — o que esta revisão faz.

**Precisão sobre o invariante do RFC 0001.** O invariante não é "nenhuma
linha pode ser criada". É: **as linhas importadas são imutáveis — nunca
removidas, renumeradas ou fundidas** (P2/P2.1); "adicionar é permitido — uma
regra nova recebe o próximo `row_index`; a sequência `1..N` vale para
qualquer `N ≥ 112`". Criar é permitido; destruir/renumerar o que existe, não.

**Tensão de CI encontrada (a registrar).** Apesar do texto do RFC 0001, o job
`bundle-imports-original` hoje compara o número de `regra-*.md` com as linhas
do CSV **congelado** (112) e falha se forem diferentes — ou seja, na prática
**proíbe** anexar linhas ao bundle `okf/regras-sisprev/`. Além disso,
`_validate_identity` exige que os `row_index` sejam exatamente `1..row_count`
sem lacunas. Logo, **não** dá para simplesmente "anexar `regra-0113` auditada"
sem contradizer um gate existente.

**Decisão ratificada pelo responsável (2026-07-23) — identidade própria +
espaço separado.** Não relaxar o gate `bundle-imports-original`; **não anexar
linhas** ao bundle legado. As 112 regras importadas permanecem preservadas
como representação histórica rastreável do as-is. O modelo de identidade e
cardinalidade fica assim:

- **`regra-NNNN` continua sendo a identidade estável da linha importada**
  (proveniência do as-is), imutável, no bundle legado `okf/regras-sisprev/`.
- A **unidade auditada recebe identidade própria, independente de `row_index`**
  — um conceito OKF com arquivo e id próprios num **bundle separado** (nome a
  ratificar, p.ex. `okf/regras-auditadas/`). Seu id **não** é um `row_index`
  nem reutiliza a numeração legada (§1.6).
- **Toda unidade auditada declara `origens_legacy: [regra-NNNN, ...]`** — a
  proveniência para a(s) linha(s) legada(s) de onde descende (lista, nunca
  implícita).
- **Uma regra legada pode originar várias unidades auditadas** (1:N):
  `regra-0022` decompõe-se em ≥2 unidades, cada uma com `causa_incapacidade`
  **escalar** (uma classe), cada uma `origens_legacy: [regra-0022]`.
- **Várias regras legadas materialmente duplicadas podem originar uma única
  unidade auditada** (N:1) — desde que a **decisão humana e a proveniência**
  fiquem registradas (um achado com a justificativa + `origens_legacy: [regra-00xx, regra-00yy]`). É o desfecho de um grupo de igualdade material P2
  (RFC 0001) *sem* fundir nem apagar nenhuma linha legada.
- **Cada unidade auditada compilável gera exatamente uma linha** no schema
  atual do Sisprev (auditada → linha Sisprev é **1:1**; uma linha por classe
  material — Q6 direção A e escalar preservados).

Isso mantém o bundle legado congelado em exatamente 112 (`bundle-imports-original`
e `_validate_identity` intactos) e é o que de fato **supera** a estrutura de 112
linhas em vez de esticá-la. A CSV deployável do Sisprev passa a ser a projeção de
(catálogo auditado, para famílias auditadas) ∪ (linhas legadas ainda não
substituídas — §1.5/§13), com **origem única por regra operacional** (§1.5).

**`variantes:` (a alternativa considerada) — rejeitada.** Colocar
`variantes:` dentro de um único `regra-*.md`, cada variante gerando uma linha
Sisprev, quebra a identidade 1:1 documento↔`row_index` que `_validate_identity`
e `bundle-imports-original` exigem (um doc não pode emitir N linhas com
`row_index` estáveis). `origens_legacy` + identidade própria evita isso e
ainda dá a cada linha deployável um `id` estável (que o consumidor do Sisprev
precisa de qualquer forma).

**Coexistência durante a migração.** A linha legada e suas descendentes
auditadas coexistem no repositório, mas **nunca as duas como origem operacional
ao mesmo tempo** — quem arbitra é o **registro de cobertura/substituição**
(§1.4) e a **seleção de origem única** do exportador (§1.5). Sub-decisão ainda
em aberto (não inventada aqui): o `motivo_inativacao` de P2.1 tem vocabulário
fechado (`duplicata`/`erro_de_importacao`) que **não** cobre "substituída por
unidade auditada"; criar esse valor é decisão de fase futura. Até lá, a
substituição é registrada no manifesto de cobertura (§1.4), e a divergência
`status_regra ≠ atualmente_no_sistema` (RFC 0001, P2.1) segue representando a
fila de migração pendente.

### 1.3 Efeito nos parsers reais (confronto)

| Camada                            | Efeito de `auditoria:` num bundle auditado separado                                                                                    |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `concept.py::parse_concept_doc`   | Nenhum — parser *shape-only*, mapa aninhado carrega normalmente.                                                                       |
| `okf/regras-sisprev/` (112 docs)  | Nenhum — o bundle legado fica congelado; o catálogo auditado é bundle novo. `bundle-imports-original` e `_validate_identity` intactos. |
| `okf_to_csv.py`                   | Inalterado para o legado; o compilador auditado é um novo derivador (§9), sob `gerar_indices` ("derivar").                             |
| `detectors/igualdade_material.py` | Muda de denylist para **allowlist** explícita (§11) — hoje ele considera `dispositivos` material, o que contamina a "colisão em B".    |
| `site/` (Zod `.loose()`)          | Nenhum para quebrar; `emit_site_data.py` emite só os campos de estado que já emite (§12).                                              |

### 1.4 Não criar duas fontes de verdade — e o registro de cobertura

A separação de identidade só é segura se **uma regra operacional tiver uma
única fonte autoral**. Regras não-negociáveis:

- O **bundle legado** é fonte **histórica/as-is** e permanece **imutável quanto
  à cardinalidade e identidade** (§1.1); seu conteúdo por linha pode receber
  edições de auditoria como hoje, mas nunca ganha/perde/renumera linhas.
- O **catálogo enriquecido** é a fonte **canônica operacional** da semântica das
  unidades **já auditadas**.
- A **projeção de 27 colunas é artefato derivado** do catálogo enriquecido (para
  regras auditadas) — nunca autorada à mão para uma regra já auditada.
- **Uma mesma regra não pode permanecer simultaneamente autorada nos dois
  lados.** Para uma regra já auditada, a semântica operacional vive **só** na
  unidade auditada; a linha legada correspondente deixa de ser editada como
  fonte operacional (permanece como registro histórico).
- **Deve existir um registro explícito de cobertura/substituição** dizendo
  **quais regras legadas foram substituídas por quais unidades auditadas** — o
  **manifesto de substituição** (envelope do projeto, §1.6; não precisa caber
  nas 27 colunas). É ele que torna a substituição auditável e reversível (§14).

**A substituição é um grupo atômico, não uma troca por unidade.** Numa
substituição 1:N, a origem legada só pode ser substituída quando o **conjunto
completo** de descendentes declarado no manifesto estiver `deployable` — nunca
descendente por descendente. Enquanto uma descendente estiver em elaboração ou
`preview`, a origem legada **continua sendo a origem operacional** e **nenhuma**
descendente entra no export deployable.

**Dois estados, dois níveis — nunca confundidos.** `preview`/`deployable`
(§5.3) são o estado de **uma unidade auditada**; `inativo`/`ativo` são o
estado do **grupo de substituição**. O manifesto modela os dois
separadamente, e representa a **decisão humana de completude** como um campo
estruturado e verificável, não como prosa:

```yaml
grupo: substituicao-regra-0022
origens_legacy: [regra-0022]
destinos_auditados:
  - invalidez-acidente-pos-2003        # estado da unidade: deployable
  - invalidez-doenca-catalogada-pos-2003  # estado da unidade: preview
estado_grupo: inativo        # inativo | ativo — ativa só quando TODOS os destinos são deployable
decisao_completude:          # a decisão jurídica em si; presente sempre que decidida (round 10) —
                              # não depende de estado_grupo, nem é zerada por ele estar inativo
  decidido_por: <auditor>
  decidido_em: <data ISO>
  justificativa: <texto>
  fonte: <referência institucional>
```

O grupo só pode transitar para `estado_grupo: ativo` quando: **todas**
as unidades em `destinos_auditados` estão com estado de unidade
`deployable` (nenhuma em `elaboracao`/`preview`); `decisao_completude` está
preenchida (`decidido_por`/`decidido_em`/`justificativa`/`fonte`, todos não
vazios — o mesmo padrão de `atos_validacao`, P7/P11); todos os predicados,
dispositivos e projeções estão completos; e (round 10, abaixo) todos os
destinos têm `estado_implantacao: confirmada`. A consolidação **N:1 também é
atômica** — todas as origens transitam juntas (o grupo lista todas em
`origens_legacy`).

**Emenda do round 10 (achado do Ciclo 1 — atomicidade do lote não é
incompletude jurídica).** A regra original deste parágrafo tratava
`decisao_completude` como parte do mesmo pacote de `estado_grupo: ativo`,
"ausente/null enquanto inativo" — e o rollback "limpa `decisao_completude`".
Isso confundia duas coisas: a **decisão jurídica** de que a substituição
(quais regras substituem quais) está correta e completa, e a **prontidão
operacional** para trocar a fonte do exportador. Um grupo pode ter a
substituição juridicamente decidida — `decisao_completude` preenchida,
válida e não retratada — e ainda estar `estado_grupo: inativo` porque
algum destino tem `estado_implantacao: pendente_mapeamento_sisprev`
(§5.3, round 9): a troca é atômica por ser um lote de implantação (não
por incerteza jurídica), e essa atomicidade é propriedade do **lote**, não
do mérito das regras. A partir deste round, `decisao_completude`
**não é mais zerada** só por `estado_grupo` estar `inativo` — só é
retirada (com registro do porquê) quando a própria decisão jurídica é
revista. `estado_grupo` deixa de ser um flag independente e passa a ser
**computado**: `ativo` se e somente se `decisao_completude` está
preenchida **e** todos os destinos são `deployable` **e** todos os
destinos têm `estado_implantacao: confirmada`; caso contrário `inativo`,
qualquer que seja a causa específica. A presença de `decisao_completude`
com `estado_grupo: inativo` **é** o sinal estrutural de "juridicamente
decidido, implantação pendente" — não precisa de prosa para se
distinguir de "juridicamente não decidido" (`decisao_completude`
ausente). Isso não cria tipo, schema ou gate novo: é regra de leitura dos
dois campos que `Conjunto` já tem (`okf/spec/conjunto.md`).

**Rollback opera sempre sobre o grupo inteiro**, nunca sobre uma unidade
isolada (§1.6): reverter `estado_grupo` a `inativo` por pendência de
implantação não edita `decisao_completude`. Reverter por revisão da
própria decisão jurídica edita os dois, com o registro de qual foi a
razão.

### 1.5 Estados de transição e a origem única do exportador

Durante a migração convivem cinco estados (o exportador precisa distingui-los):

| Estado                                   | Fonte operacional | Entra no export deployable?  |
| ---------------------------------------- | ----------------- | ---------------------------- |
| Regra legada **ainda não auditada**      | linha legada      | Sim (via legado)             |
| Regra legada **já substituída**          | unidade auditada  | **Não** (a legada não; §1.4) |
| Unidade auditada **em elaboração**       | —                 | Não                          |
| Unidade auditada **apenas em preview**   | unidade auditada  | **Não** (preview, §5.3)      |
| Unidade auditada **apta a `deployable`** | unidade auditada  | Sim (via auditado)           |

**Seleção de origem única (invariante do exportador).** Para cada regra
operacional o exportador escolhe **exatamente uma** origem: **legado enquanto
`estado_grupo` não for `ativo`**; **catálogo enriquecido depois da ativação
atômica do grupo** (§1.4, com `decisao_completude` registrada no manifesto).
"Já substituída" na tabela acima significa **`estado_grupo: ativo`** — não uma
descendente isolada com unidade `deployable`. **Nunca** exportar
simultaneamente a linha legada **e** suas substitutas auditadas — é um erro de
gate (`P_EXPORT_ORIGEM_DUPLA`, §14), não uma escolha de desempate. Uma
unidade em elaboração ou apenas em `preview` **nunca** entra no export
deployable, e um **grupo com qualquer destino não-`deployable` permanece
`estado_grupo: inativo`** — mantém a origem legada operacional (§14). Note
que uma unidade com estado `deployable` **não** vira fonte operacional
isoladamente: pertencer a um grupo `inativo` a bloqueia junto com as demais —
`deployable`/`preview` é o estado da **unidade**; `ativo`/`inativo` é o que
decide a exportação, e é sempre o estado do **grupo**.

**Emenda do round 11 — §1.4 e §1.5 descrevem um mecanismo retirado.**
`Conjunto`, o manifesto de grupo, `grupo`, `origens_legacy`/
`destinos_auditados` declarados à parte e `estado_grupo` não existem mais
como campos ou tipo (`okf/spec/conjunto.md`, retirado). O texto acima
permanece porque é o registro de como a decisão evoluiu — rounds 4 a 10
resolveram, um de cada vez, os problemas reais de misturar decisão jurídica
com prontidão técnica num único manifesto — mas não descreve o mecanismo
vigente. O que vale hoje:

- cada `RegraProposta` declara `origens_legacy` diretamente, sem manifesto
  de grupo (`okf/spec/regraproposta.md`);
- `scripts/derivar.py` computa, a cada execução, os **componentes conexos**
  do grafo origem↔destino entre as `RegraProposta` do mesmo `ciclo` —
  substituindo `grupo`/`destinos_auditados` declarados à mão;
- um componente entra na carga de implantação quando **todos** os seus
  membros têm `estado_auditoria: concluida` (renomeado de `estado_proposta: deployable`) **e** `estado_implantacao: confirmada` — a mesma regra de
  "todos ou nenhum" que `estado_grupo` computava, agora derivada em vez de
  declarada;
- a seleção de origem única do exportador (acima) e o gate
  `P_EXPORT_ORIGEM_DUPLA` (§14) não mudam de comportamento: uma origem
  legada só sai quando o componente inteiro que a substitui está pronto;
- `decisao_completude` — a decisão jurídica de que um conjunto de destinos
  cobre exaustivamente as causas do dispositivo — passa a viver como
  decisão datada no `Ciclo` responsável e/ou no log `decisoes` de cada
  `RegraProposta` do componente, não como campo de um manifesto à parte;
- revogação sem substituta (`Conjunto.revoga`) passa para `Regra.revogada`
  (`okf/spec/regra.md`).

O achado que motivou a retirada: o Bloco C do Ciclo 1 tinha, no manifesto,
duas origens legadas declaradas para um grupo de vinte destinos — mas, na
prática, cada destino descende de **uma única** origem, e as duas origens
não compartilham nenhum destino entre si. O manifesto de grupo, por
agrupar no nível do "lote" em vez do nível real do grafo origem↔destino,
bloqueava dezenove destinos legitimamente independentes só porque
compartilhavam um manifesto com o vigésimo (a unidade de causa comum,
pendente de implantação). O cálculo derivado por componente resolve isso
sem introduzir um novo tipo de agrupamento: ele simplesmente enxerga a
granularidade que já estava nos dados.

### 1.6 Contrato de identidade da projeção

O compilador/exportador tem de garantir:

- **Id estável da unidade auditada** — próprio, independente de `row_index`,
  estável ao longo da auditoria (a correção de `nome` ou de um predicado não o
  muda), no espaço do bundle auditado.
- **`id_projecao` estável no manifesto/envelope** — as 27 colunas **não têm
  identidade técnica** (nenhuma coluna é chave), então cada linha compilada
  recebe um `id_projecao` estável registrado no manifesto/envelope. Ele **não
  precisa ser importado pelo Sisprev**, mas precisa permitir **rastrear cada
  linha compilada entre execuções** (e ligá-la a suas `origens_legacy`).
- **Ordenação determinística das linhas compiladas** — uma **ordem total
  normativa** (não "p.ex."), assim:
  1. **chave primária**: menor `row_index` entre as `origens_legacy` da linha;
  2. **desempate entre descendentes de uma mesma origem (1:N)**: o id da
     unidade auditada;
  3. **legadas ainda não substituídas**: seu `row_index`;
  4. **consolidação N:1**: o menor `row_index` das origens do grupo.
     Essa ordem torna o export byte-idempotente (§9/§14).
- **Rastreabilidade linha compilada → `origens_legacy`** — cada linha do alvo
  aponta, via manifesto, para a(s) regra(s) legada(s) de origem. A
  rastreabilidade pode viver em **manifesto auxiliar/envelope**, **não** precisa
  caber nas 27 colunas.
- **Origem dividida em várias regras (1:N)** — as N unidades compartilham a
  mesma `origens_legacy` e cada uma emite sua linha; o manifesto registra a
  decomposição.
- **Várias origens consolidadas (N:1)** — a unidade única lista todas as
  origens em `origens_legacy`; o manifesto registra a consolidação e o achado
  que a justifica (§1.2).
- **Detecção de colisão entre linhas compiladas** — duas unidades auditadas que
  projetam para a mesma chave material (§4.1/§10) → `P_COMPILA_COLISAO`, salvo
  decisão humana explícita.
- **Rollback atômico sobre o grupo, sem perda da ligação com a importação
  original** — reverter opera sobre o **grupo de substituição inteiro** (§1.4),
  nunca sobre uma unidade isolada: restaura a origem legada como operacional
  (ela nunca foi destruída) e desfaz a entrada de substituição no manifesto;
  `origens_legacy` e o manifesto garantem que a ligação nunca se perde (§14/§15).

## 2. A fronteira entre semântica operacional e metadados de auditoria

A fronteira **não** coincide com "tudo que está em `auditoria:`". Dentro de
`auditoria:` há dois sub-mundos com regras opostas:

**Semântica operacional (tem de projetar para o alvo, ou a compilação
falha).** Tudo que o Sisprev precisa para **selecionar e aplicar** a regra:

- predicados jurídicos de seleção (classe da causa, regime, marco de
  ingresso, sexo quando relevante);
- requisitos de verificação humana (o predicado jurídico que a regra exige
  e o protocolo pelo qual ele é normalmente verificado — quem, por que meio,
  em que momento; **modelável por inteiro**, nunca "impossível de
  representar" — §7);
- aplicabilidade temporal (janelas, e o marco que rege a versão da norma);
- dispositivos vinculados (P3);
- a parte **discriminante** das taxonomias e suas vigências (a *classe* e
  **qual versão do rol** rege — operacional, não metadado; §5.3/§16.2).

**Metadados de auditoria (podem viver só no catálogo enriquecido).** Não são
necessários à aplicação da regra, então **não** precisam projetar: evidências,
proveniência, URL consultada, MD5/Wayback, `fonte`; confiança; histórico e
decisões de auditoria; notas de reconciliação e perguntas em aberto.

> "Completamente conversível" **não** significa colocar todo metadado de
> auditoria nas 27 colunas. Evidência, URL, confiança, histórico e decisão
> podem permanecer só no catálogo enriquecido, **desde que não sejam
> necessários à aplicação da regra pelo Sisprev**.

É a distinção Q6-R × Q6-S × Q6-T do dossiê Q6 (§1): **predicado da regra**
(Q6-R, catálogo — operacional) vs. **fato do requerente** (Q6-S, solicitação —
fora de escopo e **não resolvido** aqui) vs. **classificação médico-jurídica
versionada** (Q6-T — taxonomia/dispositivos). O §7 trata explicitamente de
não misturar Q6-R com Q6-S.

## 3. O schema enriquecido mínimo

Forma **sugerida** (a validar contra a implementação). Um único bloco
`auditoria:` no frontmatter da regra auditada, com `schema_version`:

```yaml
auditoria:
  schema_version: 1
  origens_legacy: [regra-0022]          # §1.2 — proveniência 1:N

  # --- semântica operacional (projeta para o alvo — §5) ---
  predicados:
    causa_incapacidade: acidente_em_servico   # classe MATERIAL escalar (Q6-R), enum fechado
    regime: lc-1100-2021
    marco_ingresso: apos-2003
    sexo: ambos
  requisitos_verificacao_humana:
    - predicado: nexo entre a incapacidade e o acidente em serviço   # 1. o que juridicamente deve ser verdadeiro (Q6-R)
      protocolo_verificacao:                                          # 3. como se verifica — nunca o fato do caso (Q6-S)
        pergunta: "Há nexo entre a incapacidade e o acidente em serviço?"
        responsavel: IPERON
        meio_de_prova: pericia_oficial
        momento: processo_concessorio
        evidencia_exigida: laudo pericial oficial
      portador_primario: fundamentacao_integral   # §4 — papel de projeção
  aplicabilidade_temporal:
    # NÃO derivada de `regime` enquanto Q1/Q2 abertas (§5.1) — datas legadas
    # informadas explicitamente e apenas verificadas (P5).
    datas_legadas:
      data_adm_apos: 2004-01-01
      data_adm_ate: null
  taxonomias:
    - ref: /dispositivos/lce-1100-2021/art-30-par-5/original.md   # projeta para `dispositivos:` (P3)
      papel: nexo-acidente

  # --- metadados de auditoria (NÃO projetam — só aqui) ---
  proveniencia:
    fontes_consultadas: ["Casa Civil/DITEL — LC 1.100/2021"]
    confianca: alta
  decisoes:
    - data: 2026-07-23
      quem: <auditor>
      o_que: "face acidente-em-serviço de 0022 (P7); ver reconciliação §2"
```

Princípios:

- **`schema_version` obrigatório** — sem ele a compilação falha (§14).
- **`origens_legacy` obrigatório** numa regra auditada (§1.2) — a
  proveniência 1:N nunca é implícita.
- **`causa_incapacidade` escalar, enum fechado** (Q6 §10.A):
  `acidente_em_servico`, `molestia_profissional`, `doenca_catalogada`,
  `causa_comum`. **Uma classe por regra auditada** (direção A); a lista de
  doenças **não** vira enum nem linha — fica em Q6-T (§16.2).
- **Requisitos de verificação humana são inteiramente modeláveis em A**
  (§7): `predicado` + `protocolo_verificacao` afirmam o **requisito da
  regra** (Q6-R) — o que juridicamente deve ser verdadeiro e como isso é
  normalmente apurado —, nunca o **fato do requerente** (Q6-S) num caso
  concreto. **Todo requisito verificável é modelável no schema enriquecido**
  — "não representável" **nunca** descreve A; descreve, no máximo, **B**:
  um requisito pode não ter **campo estruturado próprio nas 27 colunas**, e
  nesse caso compila para `nome`/`fundamentacao*` (§4/§6), não para um campo
  dedicado. O que permanece institucionalmente aberto é **onde e quando** o
  Sisprev real obtém e registra o fato (Q6-S, §7/§12.2) — nunca a modelagem
  do requisito em A, e nunca sua conversibilidade para B.
- **Metadados de auditoria são livres** e nunca material para colisão (§10/§11).

Confronto: `auditoria:` é *shape-only* para `concept.py`; a validação do bloco
é *on demand* (mesmo padrão de `Regra.admin`/`Achado._validation`), e um erro
no bloco enriquecido nunca esconde um `status_regra`/`status_auditoria`
bem-formado das junções P7/P14 (RFC 0001; regressão de `test_estado_auditoria.py`).

## 4. Os três artefatos-alvo e os papéis de projeção

### 4.1 Três artefatos distintos (não confundir)

O review corretamente apontou que "B = 27 colunas" é impreciso: a RFC também
projeta `taxonomias[].ref` para `dispositivos:`, que **não** é uma das 27. São
**três** artefatos, com papéis diferentes:

1. **CSV importável pelo Sisprev** — **exatamente** as 27 colunas
   (`regra_schema.py::COLUMNS`), ordem congelada. É o que o Sisprev ingere.
2. **Envelope deployável do projeto** — as 27 colunas **+ `dispositivos:`**
   (P3) **+ campos administrativos** (P12). É o que o bundle carrega por regra.
3. **Chave material de colisão (P2)** — uma **allowlist explícita** do que é
   comparado para igualdade material; **não** "tudo menos uma denylist" (§11).

### 4.2 Papéis de projeção (substitui "destino único")

"Destino único" estava errado: `causa_incapacidade` aparece legitimamente em
`nome`, `fundamentacao*`, `integral` e possivelmente `tipo_calculo`/`paridade`.
Isso não é erro — o erro era chamar de destino único. Cada predicado/requisito
operacional projeta em até quatro **papéis**, todos **declarados** e cuja
**coerência o compilador verifica**:

- **portador semântico primário** — onde a condição continua **textualmente
  expressa** (tipicamente `fundamentacao*` para um requisito de verificação
  humana, ou um campo estruturado quando existe, p.ex. `sexo`). **Exatamente
  um** por requisito.
- **efeitos derivados** — o resultado já pré-computado: `integral`,
  `tipo_calculo`, `paridade`.
- **representação de interface** — `nome` (§6). Nunca é portador primário nem
  material sozinho (§10).
- **suporte jurídico** — `dispositivos:` (P3) e a citação na fundamentação.

Invariantes do contrato:

- **Exatamente um portador primário** por requisito operacional; **nada
  operacional fica sem papel** (fail-closed — `P_COMPILA_SEM_PORTADOR`).
- **Coerência entre papéis** verificada: p.ex. `causa=acidente_em_servico` ⇒
  `integral=S`; o `nome` tem de carregar o discriminante. Incoerência é
  `P_COMPILA_INCOERENTE`.

## 5. O contrato do compilador (A → B)

```mermaid
flowchart LR
    A["auditoria: (A)\npredicados + requisitos +\naplicabilidade + taxonomias"] --> C{"compilador\ndeterminístico"}
    M["proveniencia/decisoes/confianca\n(metadados de auditoria)"] -.->|nunca projeta| R["permanece só em A"]
    C -->|portador primário| B1["fundamentacao* / campo estruturado"]
    C -->|efeitos derivados| B2["integral, tipo_calculo, paridade"]
    C -->|interface| B3["nome"]
    C -->|suporte jurídico| B4["dispositivos: (P3)"]
    C -->|papel ausente / incoerente| E["ERRO (fail-closed)"]
    C -->|semântica operacional pendente\n(alvo deployable)| E3["ERRO deployable\n(preview passa)"]
    C -->|colisão pós-projeção| E2["ERRO / decisão humana\nexplícita (§10)"]
```

### 5.1 Manifesto de mapeamento (multi-papel)

Fonte única consumida pelo compilador (análogo a `regra_schema.py::COLUMNS`).
Um predicado sem linha no manifesto é `P_COMPILA_SEM_PORTADOR`, nunca default:

| Predicado / requisito (A)             | Portador primário            | Efeitos derivados           | Interface | Suporte jurídico |
| ------------------------------------- | ---------------------------- | --------------------------- | --------- | ---------------- |
| `predicados.sexo`                     | campo `sexo`                 | —                           | `nome`?   | —                |
| `predicados.causa_incapacidade`       | `fundamentacao*`             | `integral` (`tipo_calculo`) | `nome`    | `dispositivos:`  |
| `predicados.regime`/`marco_ingresso`  | `datas_legadas` (ver abaixo) | —                           | `nome`    | `dispositivos:`  |
| `requisitos_verificacao_humana[]`     | `fundamentacao*` (§7)        | —                           | `nome`?   | `dispositivos:`  |
| `taxonomias[].ref`                    | `dispositivos:` (P3)         | —                           | —         | (o próprio ref)  |
| `proveniencia`/`decisoes`/`confianca` | — (não projeta)              | —                           | —         | —                |

**Resíduo datas × Q1/Q2 (corrigido).** `regime`/`marco_ingresso` **não**
geram deterministicamente as quatro datas enquanto Q1/Q2 (inclusividade de
limite, marco jurídico) seguem abertas. Na Fase 1, as datas são **valores
legados informados explicitamente** (`aplicabilidade_temporal.datas_legadas`)
e o compilador apenas **verifica** a consistência estrutural (P5:
`APOS ≤ ATE`, sentinelas preservadas). Gerar datas a partir de `regime` exige
Q1/Q2 resolvidas — até lá, o alvo deployable **carrega o valor explícito ou
para** (`P_COMPILA_PENDENTE`).

### 5.2 Modo de operação por fase (§15)

- **Modo verificação (Fase 1).** As colunas legadas continuam autoradas; o
  compilador projeta A e **confere** contra elas (`P_COMPILA_DIVERGE` em
  divergência). Nada vira derivado ainda.
- **Modo geração (Fase 2, por grupo atômico de substituição, ato humano).**
  As colunas das unidades auditadas passam a ser **geradas** por
  `gerar_indices.py` a partir de A **quando o grupo a que pertencem ativa**
  (`estado_grupo: ativo`, §1.4) — nunca por unidade isolada. Autoria e
  revisão de cada unidade continuam podendo acontecer uma a uma; é a
  **transição para gerado/deployable** que só ocorre pelo grupo inteiro.

### 5.3 Dois níveis de compilação — preview × deployable

Distinção que faltava (e que o fail-closed exige):

- **`preview` (validação do modelo auditado).** **Admite pendências** — um
  campo operacional `pendente` (p.ex. a versão temporal do rol, §16.2) é OK.
  Produz uma projeção **não-deployable**, anotada, para revisão humana do
  modelo. É onde uma redação que **defere** explicitamente uma pendência pode
  aparecer.
- **`deployable` (Sisprev-ready).** **Fail-closed**: qualquer semântica
  operacional não resolvida — versão de rol pendente, marco de data pendente,
  proveniência normativa ausente — **para** a compilação (`P_COMPILA_PENDENTE`
  / `P_COMPILA_SEM_PROVENIENCIA`). Uma regra com questão operacional aberta
  **existe** no schema da auditoria e passa em `preview`, mas **não é
  compilável para deployment**.

Regra: `pendente` num campo **operacional** ⇒ `preview` passa, `deployable`
falha. `pendente` num campo de **metadado** ⇒ irrelevante para ambos.

**Emenda do round 9.** "Semântica operacional não resolvida" cobre dois
casos que este parágrafo tratava como um só: (a) a **fórmula jurídica**
ainda não está determinada — esse continua fail-closed para `deployable`,
sem exceção; e (b) a fórmula está determinada, mas o **valor de domínio
fechado que a representa no Sisprev** (`projecao.tipo_calculo` e afins)
ainda não tem confirmação de que identifica essa fórmula sem ambiguidade
material. O caso (b) não bloqueia mais `deployable` — é o que
`estado_implantacao: pendente_mapeamento_sisprev` registra
(`okf/spec/regraproposta.md`). O que continua fail-closed no caso (b) é,
especificamente, a **troca da fonte operacional de exportação** do grupo a
que a unidade pertence (§1.4/§1.5): essa exige `estado_implantacao: confirmada` em todos os destinos, além de `deployable`.

## 6. Regras de geração de `nome` e `fundamentacao*`

**`nome`** (RFC 0002 §2; spec P13.1) — papel de **interface**, nunca portador
primário nem material sozinho:

- É a **principal interface humana** de seleção após a anamnese — "a menor
  descrição, em linguagem humana, capaz de distinguir a regra das demais".
- Gerado a partir de A com **fatos discriminantes primeiro** (modalidade,
  marco de ingresso, **causa relevante**, integral/proporcional, paridade),
  citação legal por último.
- **Não é discriminante material sozinho** (§10). O discriminante jurídico
  **também** aparece nos campos materiais (`fundamentacao*`, flags, datas,
  cálculo). Dois `nome` diferentes sendo a única diferença **não** tornam as
  regras materialmente distintas — é o comportamento correto do P2 (Q6 §10.B).

**`fundamentacao*`** (portador primário de um requisito de verificação
humana — §7): a redação gerada, a partir de `predicado` +
`protocolo_verificacao` de cada item de `requisitos_verificacao_humana[]`
(§3/§7), tem de:

1. **descrever a especificidade** que distingue a regra (o `predicado`);
2. **indicar que a aplicação depende de constatação pelo IPERON** — nunca
   afirmar que a constatação já ocorreu;
3. **identificar, quando disponível no `protocolo_verificacao`, o tipo de
   verificação ou evidência** (`meio_de_prova`/`evidencia_exigida`);
4. **não afirmar que houve constatação num caso concreto** — a regra
   descreve a **exigência** (Q6-R); a constatação efetiva pertence à
   solicitação (Q6-S, §7/§12.2).

Divergir da estrutura de `requisitos_verificacao_humana[]` é
`P_COMPILA_DIVERGE`.

## 7. Requisitos de verificação humana constatados pelo IPERON — cinco partes, nunca confundidas

**Decisão do responsável:** todo requisito verificável por um humano **é
modelável** no schema enriquecido — "requisito não parametrizável" é
terminologia **abandonada** por sugerir que algo escapa à modelagem, quando
na verdade o que muda de um requisito estruturado (`predicados.sexo`, por
exemplo) para este é **só** o meio de constatação, nunca a possibilidade de
representá-lo. O termo correto é **requisito de verificação humana** (ou,
quando o ponto é especificamente sobre o schema legado, "requisito não
representável no schema legado" — §4/§5, papéis de projeção).

O modelo tem **cinco partes distintas**, cada uma com seu próprio lugar —
misturar duas delas é exatamente o erro que a distinção Q6-R/Q6-S existe
para evitar:

1. **Predicado da regra** (Q6-R, vive em `auditoria:`, por regra) — o que
   **juridicamente deve ser verdadeiro**. Ex.: "há nexo entre a incapacidade
   e o acidente em serviço".
2. **Fato da solicitação** (Q6-S, vive **fora** do `regra-*.md` — pertence a
   um caso concreto, nunca à definição da regra) — um valor `sim`/`não`/
   `desconhecido`, ou o enum/valor adequado ao predicado. Institucionalmente,
   **onde e quando** o Sisprev real obtém e registra esse fato **segue
   aberto** (Q6-S, dossiê Q6 §9) — esta RFC não o fecha. O pipeline
   exploratório (§12.2) especifica uma forma **própria e não institucional**
   de coletar esse fato, sem resolver a questão institucional.
3. **Protocolo de verificação** (Q6-R, vive em `auditoria:`, por regra) —
   a pergunta, o responsável, o meio de prova, o momento e a evidência
   exigida. É `protocolo_verificacao` no schema (§3).
4. **Constatação concreta** (Q6-S, por caso) — resultado, responsável, data
   e referência da evidência de uma verificação **efetivamente realizada**.
   Nunca vive em `regra-*.md`.
5. **Avaliação** (por caso, derivada de 2+3+4) — `satisfeito` / `não satisfeito` / `indeterminado`. **Indeterminado** é o valor quando o fato
   (2) ainda não foi respondido — **nunca** "não avaliável": o protocolo (3)
   deixa claro que a avaliação é sempre possível, uma vez que o fato chegue.

**Exemplo de projeção** (o padrão que toda `fundamentacao*` gerada segue —
§6):

> "Aplicável quando a incapacidade decorrer de acidente em serviço, conforme
> constatação do IPERON no processo concessório."

Isso **não muda o schema legado** (continua as 27 colunas + admin), mas
**preserva nele** a condição operacional que não cabe em nenhum campo
estruturado — a `fundamentacao*` carrega o **predicado** (1) e aponta o
**protocolo** (3, "conforme constatação do IPERON no processo concessório"),
**nunca** afirma a **constatação concreta** (4) de um caso.

A base normativa e a redação mais detalhada já foram **validadas contra
fonte primária** no relatório do PR #27 (§4) — citadas aqui como exemplos
validados, não inventadas:

- **Nexo com acidente em serviço** (validado):
  > "Aplicável quando o IPERON houver constatado, mediante perícia oficial, o
  > nexo entre a incapacidade e o acidente em serviço (ou hipótese equiparada,
  > art. 30 §6º) no processo concessório."
- **Existência de incapacidade / readaptação** (validado):
  > "Aplicável quando o IPERON houver constatado o requisito com base em
  > perícia médica oficial do Estado (regime LCE 432/2008) ou em perícia
  > médica oficial por ele indicada (regime LCE 1.100/2021), realizada no
  > processo concessório."

Ressalvas (PR #27, mergeado): "IPERON" só existe a partir da LCE 1.100/2021
(a LCE 432/2008 fala em "perícia médica oficial do Estado") — a redação
respeita o regime; **moléstia profissional** depende de resolver a pendência
**P-6**, que o relatório do PR #27 (§7.2) documenta como **lacuna
normativa** — nenhum dos dois regimes estaduais lidos (LCE 432/2008, LCE
1.100/2021) define "moléstia profissional"; pode existir fonte externa a
eles ainda não pesquisada. Enquanto isso, o alvo deployable **falha** por
proveniência ausente, não gera texto. Nada aqui decide essas frases para
regra específica.

## 8. Versionamento e migração

- **`schema_version`** (inteiro, começa em `1`); versão desconhecida é erro,
  nunca best-effort. Bump exige compilador que leia a versão anterior ou
  migração de dados explícita e revisável (rigor de P12).
- **Autoria e revisão por unidade, humana** (autoria humana; sem backfill em
  massa) — mas a **migração operacional** (geração `deployable`, ativação,
  substituição da origem legada) ocorre **sempre por grupo atômico** (§1.4),
  nunca por unidade isolada, mesmo quando cada unidade foi escrita e revisada
  uma a uma.
- **1:N e N:1 via `origens_legacy`** (§1.2); nenhuma linha legada é criada,
  removida, renumerada ou fundida em `okf/regras-sisprev/` — o catálogo
  auditado vive em espaço de identidade próprio.
- **Coexistência legado × auditado** com **fonte única por regra operacional**,
  arbitrada pelo **manifesto de substituição** (§1.4) e pela seleção de origem
  única do exportador (§1.5); o `motivo_inativacao` de P2.1 para a linha
  substituída é sub-decisão de fase futura (§1.2), não bloqueia o manifesto.

## 9. Compatibilidade com round-trip e geração idempotente

- **Round-trip legado intacto.** `okf/regras-sisprev/` fica congelado em 112;
  `okf_to_csv.py`, `test_roundtrip.py`, `bundle-imports-original` e
  `_validate_identity` **inalterados** (o catálogo auditado é bundle
  separado, §1.2).
- **Idempotência.** A saída do compilador passa pelos mesmos
  `md_format.write_markdown`/serialização já byte-idempotentes; é função pura
  das fontes autorais → cabe sob `gerar_indices` ("derivar", P10). Quando (Fase
  2\) as colunas de uma regra auditada virarem derivadas, entram num
  `git diff --exit-code` como a CSV hoje — prova mecânica da determinística.

## 10. Detectores de equivalência e colisão — dois controles

O `nome` **não deve, sozinho, tornar duas regras materialmente distintas**
(RFC 0001, P1/P2), mas a distinção jurídica também não pode viver só no
`nome`. Daí **dois controles separados**:

**Controle 1 — equivalência semântica em A.** Novo detector sobre os campos
**operacionais** de `auditoria:` (`predicados`, `requisitos_*`,
`aplicabilidade_temporal`, `taxonomias`) — **nunca** sobre
`proveniencia`/`decisoes`/`confianca` (§2). Informativo (camada 2/3): abre
achado, não decide.

**Controle 2 — colisão depois da projeção.** Opera sobre a **chave material
de colisão** (§4.1, item 3 / §11). Reporta regras que **compilam para
combinações indistinguíveis**.

> Se duas regras forem **semanticamente diferentes em A** mas **compilarem
> para combinações indistinguíveis** no alvo, o compilador **falha**
> (`P_COMPILA_COLISAO`) ou **exige decisão humana explícita**. Não se esconde
> a perda de expressividade.

A decisão humana explícita reusa o mecanismo de achado — **sem alterar a chave
material e sem tornar `nome` material**, que é o que Q6 §10.B prevê. É o
`0022 × P6/P7` (reconciliação §2) e o Q8 do RFC 0001.

> **Emenda (2026-07-30) — o mecanismo mudou de forma, e o parágrafo acima o
> nomeava pelos campos antigos.** A redação original dizia "achado
> `situacao: resolvido` com `efeito_deteccao: pode_persistir`". **Os dois campos
> não existem mais** (RFC 0001, emenda de 2026-07-30): restam `aberto` e
> `improcedente`, e a expectativa sobre a detecção passou a ser **derivada** de a
> população ter respondido `corrigida` em `disposicao_de_achados`, em vez de
> declarada no achado.
>
> A consequência para o compilador é que **não há mais um selo que autorize a
> colisão a persistir**. Quem quiser que uma `P_COMPILA_COLISAO` conhecida não
> derrube o gate tem de fazê-lo pelo caminho que sobrou: um achado aberto que a
> descreva, e a disposição de cada regra alcançada dizendo como responde a ela.
> Isso é mais trabalho e é deliberado — era exatamente o que o estado
> `resolvido` permitia pular.

## 11. Impacto no P2/P3 — a correção da chave material

O review corrigiu meu erro anterior: **hoje o P2 é uma _denylist_**
(`igualdade_material.py::_IGNORED_FRONTMATTER_KEYS` = `type`, `id`,
`row_index`, `nome`, `auditado_por`, `auditado_em`, `atos_validacao` +
`ADMIN_FIELD_DEFAULTS`). Como `dispositivos` **não** está na denylist, o P2
**atualmente considera `dispositivos` material**. Logo, "basta adicionar
`auditoria` à denylist e o P2 vira comparação pura da projeção B" era **falso**.

**Correção proposta.** Converter o P2 de denylist para **allowlist explícita**
da **chave material de colisão** — as **27 colunas de domínio menos `nome`**,
derivadas de `regra_schema.py::COLUMNS`. Assim a colisão é definida sobre o
**CSV importável pelo Sisprev** (artefato 1, §4.1), determinístico e livre de
contaminação por campos fora das 27.

**Decisão ratificada pelo responsável (2026-07-23): `dispositivos` fica FORA da
chave de colisão.**

- A **chave de colisão Sisprev é a allowlist das 27 colunas menos `nome`**.
- **`dispositivos` não entra na chave de colisão**, porque **não é consumido
  pelo Sisprev** (é do envelope deployável, artefato 2, não do CSV importável,
  artefato 1).
- Diferenças de **suporte jurídico** continuam verificadas pelo **controle
  semântico do schema auditado** (controle 1, §10) e pelo **P3** — não pelo P2.
- Isso **muda o comportamento** do P2 atual (que hoje trata `dispositivos` como
  material): na implementação, **bump da `VERSION`** do detector, reconciliando
  os fingerprints de forma controlada (como no v4). O bloco `auditoria:` fica
  naturalmente fora da allowlist (não é coluna).

**P3.** Sem mudança de infraestrutura — `taxonomias[].ref` e os dispositivos
usam o `dispositivos:`/`okf/dispositivos/` que já existem
(`check_p3_dispositivos`). **P7** não muda invariante nesta RFC.

## 12. Impacto no simulador e no site

**Duas superfícies distintas, com regras diferentes — nunca confundidas.**

### 12.1 O export destinado ao schema atual do Sisprev (regra do exportador — inalterada)

Esta é a única superfície com poder normativo sobre o que o Sisprev real
ingere, e o round 7 **não a toca**:

> **Somente unidades `deployable` de grupos ativos entram no export
> destinado ao schema atual do Sisprev** (§1.5) — nenhuma unidade em
> `elaboracao`/`preview`, nenhuma pertencente a grupo `inativo`. `fail-closed`
> permanece integral: proveniência ausente, papel incompleto ou pendência
> operacional continuam barrando a compilação `deployable` (§5.3/§14),
> exatamente como nos rounds anteriores.

### 12.2 O simulador exploratório — pipeline próprio, sem efeito no exportador

**Decisão do responsável (2026-07-23):** o simulador publicado (RFC 0002; PR
#28, mergeado) é **experimental**, mantido em **site pessoal**, e **não
constitui ferramenta oficial do IPERON**. Por não carregar esse peso
institucional, ele pode ser **mais ambicioso** do que o export — a restrição
introduzida no round 5 ("o simulador público consome apenas o export
deployable") é **removida** e substituída pelo desenho abaixo.

- **Pipeline de simulação é separado do pipeline de exportação.** Lê
  diretamente os blocos `auditoria:` (de qualquer estado de unidade) e as
  linhas legadas — **nunca** passa pelo compilador `deployable`, pelo
  manifesto de ativação, ou pelo exportador. **Não tem efeito** sobre
  manifesto, `estado_grupo`, `decisao_completude`, compilação `deployable` ou
  exportação — são pipelines de leitura independentes da mesma fonte (§1.1),
  nunca o mesmo caminho de dados do §12.1.

- **Três universos comparáveis**, selecionáveis na interface:

  1. **catálogo legado as-is** — as 112 linhas de `okf/regras-sisprev/`, sem
     enriquecimento;
  2. **catálogo auditado ativo/deployable** — exatamente o que §12.1 também
     exportaria (mesmo conjunto, para comparação direta);
  3. **catálogo auditado experimental** — inclui unidades em `elaboracao`,
     `preview`, e unidades pertencentes a **grupos `inativo`** (a face
     completa de uma decomposição 1:N mesmo antes do grupo ativar, por
     exemplo).

- **Cada resultado experimental é explicável, com campos obrigatórios**: o
  **estado** da unidade (`elaboracao`/`preview`/`deployable`) e do seu grupo
  (`inativo`/`ativo`); a **origem** (`origens_legacy`, `id_projecao` quando
  existir); os **dispositivos** vinculados; as **pendências** conhecidas; as
  **premissas assumidas** pela simulação (todo valor que o pipeline
  precisou supor porque o campo estava incompleto — p.ex. uma
  `versao_rol: pendente`, §16.2); e, para cada `requisito_verificacao_humana`
  (§7) da regra, a sua **avaliação** (`satisfeito`/`não satisfeito`/
  `indeterminado`) **acompanhada da sua `base_avaliacao`** (item seguinte) —
  a avaliação **nunca** aparece sozinha. A interface **tem** de deixar claro
  **por que** uma regra apareceu — nunca apenas o nome ou o resultado.

- **Coleta interativa do fato da solicitação (§7, parte 2) — com a base da
  avaliação sempre explícita.** O simulador exploratório pode coletar o fato
  de **duas fontes distintas**, e cada avaliação carrega qual delas usou —
  `base_avaliacao`:

  - **`hipotese_informada`** — o usuário digita/seleciona uma resposta à
    `pergunta` do `protocolo_verificacao` (§7, parte 3), **sem** nenhum
    registro de constatação real por trás. Gera avaliação exploratória
    (`satisfeito`/`não satisfeito`), mas **nunca** pode ser apresentada,
    exportada ou rotulada como se fosse a constatação do IPERON — o
    resultado é sempre acompanhado do rótulo `hipotese_informada` (§12.2,
    "rótulo obrigatório").
  - **`constatacao_documentada`** — um **avaliador humano** registra a
    **constatação concreta** de fato (§7, parte 4: resultado, responsável,
    data, referência da evidência) — um registro real, não uma hipótese.
    Só este caso pode ser lido como equivalente a uma constatação de facto
    (ainda que fora do processo concessório oficial do IPERON — a simulação
    continua não oficial, §12.2).
  - **`sem_informacao`** — nenhuma das duas ocorreu; a avaliação é
    **`indeterminado`**. **Nunca** rotulada como "não avaliável": o
    `protocolo_verificacao` (§7, parte 3) já deixa claro que a avaliação é
    sempre possível, uma vez que uma das duas fontes acima a preencha.

  Isso permite ao simulador ser ambicioso — e até errar, numa hipótese
  informada — **sem fingir** que uma resposta do usuário foi constatada
  pelo IPERON. Nada disso persiste no `regra-*.md` (a solicitação é sempre
  por caso, fora da definição da regra — §7).

- **Não precisa se limitar ao filtro mecânico de exclusão atual.** O pipeline
  exploratório pode produzir **hipóteses**, **ranking**, **cenários
  contrafactuais** e **resultados probabilísticos** — desde que cada saída
  carregue os campos dos dois itens anteriores. Isso é uma ampliação de
  ambição da simulação, não uma nova fonte de verdade (§1.1/§1.4 intactas).

- **Invariante que sobrevive à ambição maior**: lê `auditoria.predicados` e os
  campos estruturados (inclusive de unidades em `elaboracao`/`preview`/grupo
  `inativo`), **nunca** deduz predicado interpretando `nome` ou
  `fundamentacao*` em prosa. E **nunca reclassifica** uma `hipotese_informada`
  como `constatacao_documentada` — a base da avaliação nunca é apagada nem
  embaçada a jusante; sem nenhuma das duas, o requisito é **`indeterminado`**
  (`sem_informacao`), nunca uma exclusão silenciosamente decidida.

- **Rótulo obrigatório e visível, sem exceção**: todo resultado do pipeline
  exploratório indica explicitamente que é **simulação exploratória do site
  pessoal — não decisão, parecer ou validação oficial do IPERON**. O universo
  2 (auditado ativo/deployable) recebe o mesmo rótulo apesar de coincidir com
  o export — a fonte da autoridade normativa nunca é o simulador, é o
  export de §12.1.

- **Tolerância a erro é local à simulação.** Uma premissa assumida ou uma
  avaliação `indeterminada` podem aparecer no universo experimental sem
  barrar a simulação — mas **nunca** relaxam os gates do catálogo
  `deployable` (§14) nem a conversibilidade obrigatória para as 27 colunas
  (§4/§5): esse rigor é do compilador/exportador (§12.1), intocado.

- **Escopo desta RFC**: apenas a especificação do pipeline acima —
  **nenhuma implementação** nesta PR (spec inalterada: "não altera... o
  simulador", topo desta RFC). O desenho concreto de UI/ranking/cenários
  contrafactuais fica para uma proposta de implementação futura, revisável
  separadamente.

**Site** (RFC 0003): permanece projeção derivada e read-only; Zod `.loose()`
deixa `auditoria:` passar; `emit_site_data.py` inalterado. Painel futuro que
exponha predicados (para §12.1 **ou** §12.2) é aditivo — fora de escopo.

## 13. Estratégia para regras atuais ainda não auditadas

- Uma linha legada **sem** regra auditada correspondente permanece
  **integralmente legado** em `okf/regras-sisprev/`, intocada (nenhuma das 112
  é modificada por esta RFC).
- A CSV deployável do Sisprev é a união com **origem única por regra** (§1.5):
  projeção do catálogo auditado (para regras já substituídas e aptas a
  `deployable`) ∪ linhas legadas **ainda não substituídas**. Nunca as duas ao
  mesmo tempo para a mesma regra operacional.
- O compilador só roda sobre regras auditadas; ausência de auditoria não é
  erro — é o estado default.
- Enriquecimento avança **por família** (invalidez/incapacidade primeiro,
  sobre a reconciliação §2 e a base normativa do PR #27, mergeado — estado
  precisado no §18), sempre por ato humano.

## 14. Testes e gates necessários

- **Determinismo/idempotência**: mesma entrada A ⇒ mesma saída, byte a byte.
- **Papéis completos** (`P_COMPILA_SEM_PORTADOR`): todo requisito operacional
  tem exatamente um portador primário e nenhum campo operacional fica sem
  papel.
- **Coerência entre papéis** (`P_COMPILA_INCOERENTE`): efeitos derivados
  batem com o predicado (causa→integral etc.); `nome` carrega o discriminante.
- **Preview × deployable** (`P_COMPILA_PENDENTE`): campo operacional pendente
  passa em `preview` e **falha** em `deployable` (§5.3).
- **Proveniência normativa** (`P_COMPILA_SEM_PROVENIENCIA`): predicado/requisito
  sem dispositivo/fonte que o sustente falha no alvo deployable (ex.: moléstia
  profissional enquanto P-6 aberta; versão de rol indefinida — §16.2).
- **Verificação** (`P_COMPILA_DIVERGE`): projeção bate com colunas autoradas
  (Fase 1).
- **Colisão pós-projeção** (`P_COMPILA_COLISAO`): sobre a chave material
  (allowlist, §11); salvo achado `pode_persistir` explícito.
- **Equivalência em A** (controle 1): detector informativo (camada 2/3).
- **`schema_version`/`origens_legacy`** presentes e válidos.

**Gates preservados (do as-is histórico) — sem mudança:** `bundle-imports-original`
(as 112 linhas), o round-trip da importação original (`test_roundtrip.py`),
`original-raw-immutable`, além de `md_format`, `ruff`, `ty`, `pytest`,
`derived-csv-in-sync`, `validar-regras`.

**Gates novos (do catálogo auditado) — propostos:**

- **Identidade auditada única** — nenhum id de unidade auditada repetido; id
  próprio, independente de `row_index` (§1.6).
- **`origens_legacy` existentes** — toda unidade auditada aponta para
  `regra-NNNN` que existe no bundle legado.
- **Nenhuma substituição sobreposta** — no manifesto (§1.4), uma linha legada
  não é substituída por dois conjuntos auditados conflitantes; **uma origem não
  pode pertencer a dois grupos ativos**.
- **Grupo parcialmente `deployable` não ativa** (§1.4) — se algum
  `destino_auditado` do grupo estiver em elaboração/preview, `estado_grupo`
  permanece `inativo` e a origem legada segue operacional.
- **`decisao_completude` completa e verificável** (§1.4) — `estado_grupo: ativo` exige `decidido_por`/`decidido_em`/`justificativa`/`fonte` todos
  presentes e não vazios; ausência/vazio em qualquer um bloqueia a ativação.
- **Ativação e rollback atômicos** — o grupo de substituição transita como um
  todo; **nenhum destino isolado é exportado antes de `estado_grupo: ativo`**,
  e o rollback volta `estado_grupo` a `inativo` e limpa `decisao_completude`
  sobre o grupo inteiro (§1.4/§1.6).
- **Nenhuma origem exportada duas vezes** (`P_EXPORT_ORIGEM_DUPLA`, §1.5) —
  legado e auditado nunca exportam a mesma regra operacional simultaneamente.
- **`id_projecao` estável e rastreável** (§1.6) — toda linha compilada tem
  `id_projecao` no manifesto, ligando-a às suas `origens_legacy` entre execuções.
- **`preview` nunca no export deployable** (§1.5/§5.3).
- **Compilação auditada determinística** — mesma entrada ⇒ mesma saída,
  ordenação total explícita (§1.6), byte-idempotente.
- **Toda unidade `deployable` completamente conversível** — sem campo
  operacional pendente/sem portador/sem proveniência (§5/§5.3).
- **Cobertura/reversibilidade do manifesto de substituição** — o manifesto é
  consistente e o rollback restaura a origem legada sem perda de ligação (§1.6).

## 15. Plano incremental de implementação e rollback

| Fase   | Entrega                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Rollback                                                                                                                                                             |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **0**  | Esta RFC (spec revisável). Nenhum código, nenhuma regra.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Fechar a PR.                                                                                                                                                         |
| **1**  | Bundle auditado (espaço de identidade próprio) + schema enriquecido + compilador em **modo verificação**, com os dois níveis (`preview`/`deployable`) e os papéis de projeção. Detector do controle 1. P2 → allowlist (§11). **Nenhum `estado_grupo: ativo` ainda existe**, então não há universo 2 (auditado ativo/deployable) para o simulador exploratório mostrar — mas **desde já** (§12.2) ele pode comparar o **universo 1 (legado)** com o **universo 3 (auditado experimental)**, incluindo unidades em `elaboracao`/`preview`/grupo `inativo`, sempre rotulado como não oficial. **Nenhuma coluna legada vira derivada.** | Remover o bundle auditado reverte ao estado 100% legado, sem perda.                                                                                                  |
| **2**  | Virar a canonicidade **por grupo atômico de substituição** (nunca por regra/unidade isolada) — colunas compiladas/derivadas apenas para grupos com `estado_grupo: ativo`, uma família por vez, começando por invalidez. Registrar `decisao_completude` no manifesto (§1.4) e definir o `motivo_inativacao` P2.1 da linha substituída. O **universo 2** (auditado ativo/deployable, §12.2) passa a existir e a ser mostrado no simulador exploratório **junto** dos universos 1 e 3 — o universo 3 (experimental) **não é removido**; os três continuam comparáveis.                                                                 | Reverter `estado_grupo` a `inativo` restaura a origem legada como operacional para o grupo inteiro, sem perda de ligação (§1.6); a linha legada nunca foi destruída. |
| **3+** | Eventual exigência de `auditoria:` para `revisada` (P7) — invariante novo, decisão de fase própria.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Reverter o invariante de P7.                                                                                                                                         |

Cada fase é uma PR revisável e independente; nada aqui autoriza pular para a
Fase 1 sem aprovação.

## 16. Exemplos completos de projeção

### 16.1 Exemplo 1 — `0022` decomposta: acidente em serviço (1:N)

`0022` cobre pelo menos duas classes; aqui a **face acidente em serviço**
(hipótese PGE **P7**, LC 1.100/2021, ingresso > 2003). É **uma** das ≥2 regras
auditadas com `origens_legacy: [regra-0022]` (a outra é a face doença,
§16.2) — a projeção **1:N** que o review exigiu.

**Representação enriquecida (A):**

```yaml
auditoria:
  schema_version: 1
  origens_legacy: [regra-0022]
  predicados:
    causa_incapacidade: acidente_em_servico
    regime: lc-1100-2021
    marco_ingresso: apos-2003
    sexo: ambos
  requisitos_verificacao_humana:
    - predicado: nexo entre a incapacidade e o acidente em serviço
      protocolo_verificacao:
        pergunta: "Há nexo entre a incapacidade e o acidente em serviço?"
        responsavel: IPERON
        meio_de_prova: pericia_oficial
        momento: processo_concessorio
        evidencia_exigida: laudo pericial oficial
      portador_primario: fundamentacao_integral
  aplicabilidade_temporal:
    datas_legadas: { data_adm_apos: 2004-01-01, data_adm_ate: null }
  taxonomias:
    - ref: /dispositivos/lce-1100-2021/art-30-par-5/original.md
      papel: nexo-acidente
  proveniencia:
    fontes_consultadas: ["Casa Civil/DITEL — LC 1.100/2021"]
    confianca: alta
```

**Projeção (papéis, §4.2):** portador primário do nexo → `fundamentacao_integral`
(redação §7); efeitos derivados → `integral: S`, `tipo_calculo: Valor Médio`,
`paridade: N`; interface → `nome`; suporte jurídico → `dispositivos: ["/dispositivos/lce-1100-2021/art-30-par-5/original.md"]` (o `ref` **projeta** para
`dispositivos:`; resíduo corrigido). Datas: **valores legados verificados**,
não gerados (§5.1). `sexo: AMBOS`; `tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ`.

**`nome` gerado:** `Invalidez por acidente em serviço — ingresso após 2003 (LC 1.100/2021), integral por média, sem paridade`.

**`fundamentacao_integral` gerada:** redação-IPERON validada (§7, nexo).

**Só na auditoria:** `proveniencia`, `confianca`, `decisoes` (o texto verbatim
do dispositivo vive em P3, não é duplicado na regra).

**Atomicidade do grupo (§1.4):** esta face **está `deployable`**, mas a face
doença (§16.2) está apenas em `preview`. Logo `substituicao-regra-0022`
permanece `estado_grupo: inativo`, `regra-0022` **continua sendo a origem
operacional**, e **esta linha auditada ainda não entra no export destinado ao
schema atual do Sisprev** (§12.1) — ela só entra quando as **duas** faces
estiverem `deployable` e `decisao_completude` estiver registrada. O pipeline
de simulação exploratório (§12.2, universo 3) **pode** mostrá-la desde já —
rotulada com `estado_grupo: inativo`, `origens_legacy: [regra-0022]` e a
pendência "grupo aguarda a face doença", nunca como resultado do export.

**Situação que faria a compilação falhar:** se a face doença (§16.2) da mesma
`0022` projetasse para a **mesma** chave material (mesmas 27 colunas − `nome`:
`integral: S`, `Valor Médio`, `paridade: N`, mesmas datas, `fundamentacao*`
idêntica), as duas seriam **indistinguíveis no alvo** apesar de distintas em A
(causa diferente) → `P_COMPILA_COLISAO`: ou a redação difere a causa
explicitamente (§7), ou há um achado `pode_persistir` com decisão humana
(§10). O compilador **não** escolhe sozinho.

### 16.2 Exemplo 2 — doença catalogada, rol de versão temporal pendente

A **face doença** de `0022` (classe `doenca_catalogada`). O rol mudou entre
LCE 432/2008 (14 doenças) e LCE 1.100/2021 (16, com "esclerose múltipla"), e
**qual rol rege cada fato gerador** é Q6-T-vigência — **aberto**. Como a versão
do rol **determina quais doenças satisfazem o requisito**, ela é **operacional**,
não metadado (ponto do review).

**Representação enriquecida (A):**

```yaml
auditoria:
  schema_version: 1
  origens_legacy: [regra-0022]
  predicados:
    causa_incapacidade: doenca_catalogada
    regime: lc-1100-2021
    marco_ingresso: apos-2003
  requisitos_verificacao_humana:
    - predicado: doença enquadrada no rol de doença grave/contagiosa/incurável
      protocolo_verificacao:
        pergunta: "O requerente está acometido por doença do rol aplicável?"
        responsavel: IPERON
        meio_de_prova: pericia_oficial
        momento: processo_concessorio
        evidencia_exigida: laudo pericial oficial
      portador_primario: fundamentacao_integral
  aplicabilidade_temporal:
    versao_rol: pendente            # OPERACIONAL e pendente (Q6-T-vigência)
  taxonomias:
    - ref: /dispositivos/lce-1100-2021/art-30-par-8/original.md   # rol 2021 (16 incisos) — LC 1.100/2021
      papel: rol-doencas
    - ref: /dispositivos/lce-432-2008/art-20-par-9/original.md    # rol anterior (14) — LCE 432/2008, art. 20 §9º
      papel: rol-doencas-anterior
  proveniencia:
    confianca: media
    notas: "qual versão do rol rege o caso é Q6-T (aberto)"
```

**`preview` (admite pendência):** projeta a classe (`integral: S`,
`tipo_calculo: Valor Médio`), gera `nome` (`Invalidez por doença catalogada em lei — ingresso após 2003 (LC 1.100/2021), integral por média`) e uma
`fundamentacao_integral` **anotada** que **defere** a versão: "…doença
enquadrada no rol juridicamente aplicável ao caso, **permanecendo pendente a
definição da versão temporal desse rol**." Saída marcada **não-deployable**.

**`deployable` (fail-closed):** **FALHA** com `P_COMPILA_PENDENTE` — a
`versao_rol` é operacional e está `pendente`. Uma regra com essa questão
aberta **existe** em A e passa em `preview`, mas **não** é compilável para
deployment (correção do blocker 3). A redação que "defere" é legítima só em
`preview`, **nunca** num artefato deployable.

**Só na auditoria:** as duas versões do rol como evidência — `art-30-par-8/original` da
**LC 1.100/2021** (16 incisos) vs. `art-20-par-9/original` da **LCE 432/2008** (14, art. 20
§9º), dois regimes distintos —, a nota de que a escolha é Q6-T, `confianca: media`. A **lista de
doenças** nunca vira linha nem enum — é taxonomia Q6-T versionada (Q6 §10.A).

**Outra situação de falha (mesmo em preview):** tentar **fixar** a versão do
rol **sem proveniência normativa** que diga qual data a rege
(`P_COMPILA_SEM_PROVENIENCIA`), ou criar **uma linha por doença**
(contingência B de Q6, não adotada). O correto enquanto Q6-T-vigência estiver
aberta é **não deployar**, não adivinhar.

## 17. Condições de parada honradas por esta RFC

- **Identidade/cardinalidade** (blocker principal): **resolvida e RATIFICADA
  pelo responsável** (2026-07-23) — unidade auditada com identidade própria em
  espaço separado, `origens_legacy`, 1:N (decomposição) e N:1 (consolidação com
  decisão humana), 1:1 auditada→linha (§1.2); fonte única por regra operacional,
  manifesto de cobertura (§1.4), estados de transição e origem única do
  exportador (§1.5), contrato de identidade da projeção (§1.6), atomicidade do
  grupo de substituição com `estado_grupo`/`decisao_completude` verificáveis
  (§1.4/§14/§15). O bundle legado fica preservado como as-is histórico;
  `bundle-imports-original` **não** é relaxado; `variantes:` rejeitada com razão.
- **Round-trip**: claro (lido em `okf_to_csv.py`/`regra_schema.py`); o legado
  fica congelado. Sem bloqueio.
- **Conversibilidade sem perda operacional**: definida via papéis de projeção,
  dos dois níveis preview/deployable e do fail-closed (§4/§5). Metadado fica só
  em A por decisão explícita (§2), não por descarte.
- **Conflito com decisões anteriores**: nenhum — preserva
  P1/P2/P2.1/P3/P5/P7/P13, semântica adiada, autoria humana, Q6 direção A. O
  ajuste do P2 (denylist→allowlist) **corrige** um comportamento hoje
  incorreto (`dispositivos` material), não contraria o RFC 0001.
- **Campo sem proveniência no export do Sisprev (§12.1)**: **erro de
  compilação** deployable (§5.3/§14), não default — inalterado pelo round 7.
  No pipeline exploratório (§12.2), conhecer o predicado ≠ avaliá-lo: sem o
  fato Q6-S efetivamente recebido, o requisito é **`indeterminado`** (§7),
  nunca uma exclusão silenciosamente decidida nem "não avaliável".
- **`nome` como único discriminante material**: **rejeitado** — §10 mantém os
  dois controles; `nome` é papel de interface, nunca material sozinho.
- **Q6-S permanece aberta**: esta RFC enriquece só o catálogo (Q6-R). **Não**
  decide onde/quando o fato da causa do **requerente** é obtido/registrado no
  Sisprev real (Q6-S, perguntas 1–4 do dossiê Q6 §9). Nada aqui a declara
  resolvida.

## 18. O que esta RFC não decide (resumo)

Não responde Q1–Q12; não fecha Q6-S; não redige `fundamentacao*` definitiva
para nenhuma regra; não fixa a gramática de `nome`; não escolhe a versão
temporal de nenhum rol; não define o `motivo_inativacao` P2.1 da linha legada
substituída; não cria diretórios, schema, compilador, manifesto, regras ou
gates (nada além da RFC); não exige `auditoria:` para `revisada`; não edita
`regra-*.md`, schema, CSV, dispositivos, achados, detectores, simulador, site
ou workflows.

**Estado preciso das pendências do PR #27 (mergeado)** — não genericamente
"não resolvidas": o relatório do PR #27 (§6/§7) já distingue por categoria, e
esta RFC não move nenhuma delas de categoria:

- **P-5** — **cobertura documental concluída**: os dispositivos do ramo
  "após 2003" da LC 1.100/2021 (arts. 24, 26, 27-II, 30) já estão coletados
  no bundle `okf/dispositivos/`. O que resta é **vinculação futura** — religar
  `regra-0021`/`0022` a esses dispositivos e corrigir a `fundamentacao*` —,
  trabalho de PR posterior, fora de escopo aqui.
- **P-6** (moléstia profissional) — **documentada como lacuna normativa**:
  confirmado que nenhum dos dois regimes estaduais lidos (LCE 432/2008, LCE
  1.100/2021) define "moléstia profissional"; pode existir fonte externa
  ainda não pesquisada. Por isso a compilação de um requisito de moléstia
  profissional falha por proveniência ausente (§7/§14) até essa lacuna ser
  fechada.
- **P-1/P-2/P-3/P-4 e a temporalidade do rol de doenças** — **decisão
  jurídica substantiva pendente**, não uma busca de texto: se
  `regra-0001`/`0002`/`0004` (e o ramo pós-2003 de `0006`/`0007`) ainda
  alcançam casos atuais (P-1/P-2); qual é a base constitucional correta para
  `0006`–`0009` (P-3/P-4, já que o art. 40 §1º III citado trata de
  aposentadoria por idade, não invalidez); e qual versão do rol de doenças
  rege cada fato gerador. Nenhuma é resolvida por esta RFC nem pelo PR #27.
- **Q6-S** — segue **inteiramente aberta**: obtenção e registro do fato da
  causa no Sisprev real, fora do alcance de uma pesquisa normativa.

As decisões de **identidade separada** (§1), do **simulador exploratório
sem efeito sobre o exportador** (§12.2) e da **modelagem integral de todo
requisito de verificação humana** (§7) foram **ratificadas** e deixaram de
ser questão aberta; o que fica para fases posteriores é a **implementação**
de cada uma — revisável e reversível.
