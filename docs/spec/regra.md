# Spec semântica — `type: Regra` (RFC 0001, P13.1)

- **Status**: estrutura inicial (2026-07-17) — a fronteira está declarada;
  das doze questões que a preenchem (Q1–Q12), a Q1 está respondida e a Q2 e
  a Q3 parcialmente (quadro em "Questões abertas"). Esta spec evolui conforme a investigação junto ao Sisprev, à
  documentação e à análise jurídica responde cada questão. Atualizada
  (2026-07-17): as seções do corpo da regra deixam de ser convenção
  opcional e passam a ser exigidas estruturalmente para `revisada`,
  verificadas por `scripts/estado_auditoria.py`. Atualizada (2026-07-29):
  as quatro seções fixas dão lugar a **uma**, `# Estado da análise`, com
  checklist — o gate anterior passava no literal `TODO` e não tinha onde
  registrar o que faltava (ver seção própria). Atualizada
  (2026-07-20): a fundamentação (`FUNDAMENTACAO*`) passou a viver no
  frontmatter, não no corpo (o corpo é análise autoral); a infraestrutura
  P3 (`okf/dispositivos/`) já existe — o pendente é a vinculação
  sistemática das regras aos dispositivos. Atualizada (2026-07-21): registra
  o papel do campo `nome` como interface de seleção (ver seção própria).
  Atualizada (2026-07-28): a **Q1 foi respondida** e parte da **Q2** também
  — `ATE` inclusivo, `DATA_ADM_APOS` exclusivo, valor gravado é o marco, e
  `DATA_DIREITO_ATE` é prazo de implementação dos requisitos (ver
  "Elegibilidade temporal"). É a primeira das doze questões a fechar.
  Atualizada (2026-07-28): registra **o que individua uma regra** e que a
  **granularidade da aferição é escolha do IPERON** — com isso a **Q3 fica
  parcialmente respondida** (`sexo` confirmado como critério aferido) e a
  leitura do `P2_IGUALDADE_MATERIAL_ATIVA` muda (ver "Definição de
  trabalho"). Atualizada (2026-07-30): registra que **nenhuma edição de
  conteúdo rompe a identidade de uma regra** e separa isso da pergunta de
  quem pode gravar a edição (ver "Identidade no tempo"; rationale na
  [RFC 0012](../rfc/0012-identidade-estavel-e-alteracao-substancial.md)).
- **Parte de**: [RFC 0001](../rfc/0001-criterios-de-validacao-das-regras.md),
  P13 ("Especificação semântica de `type: Regra` + mapa normativo CSV →
  OKF"). P13 tem dois entregáveis: esta spec (P13.1) e o mapa normativo
  das 27 colunas (P13.2, já implementado em `scripts/regra_schema.py` —
  fonte única do mapeamento CSV ↔ `.md`, não duplicada aqui).
- **Pré-requisito de**: P6 (análise de cobertura — precisa saber quais
  campos são predicados e quais são resultados, Q3), da auditoria de
  mérito (o revisor precisa saber o que é automático, manual ou
  desconhecido, Q11/Q12) e, transitoriamente, dos checks provisórios de
  P9 (Q6, Q10).

## Definição de trabalho

> Uma regra reúne critérios estruturados usados pelo Sisprev, requisitos
> adicionais que podem depender de prova ou análise manual, consequências
> aplicadas depois de sua seleção e a fundamentação jurídica
> correspondente. A correspondência automática dos campos estruturados não
> equivale, por si só, à conclusão jurídica de que a regra se aplica ao
> caso concreto.

Isso **não é uma afirmação sobre como o Sisprev de fato funciona** — é a
hipótese de trabalho que estrutura a investigação (a confirmar por Q3, Q4,
Q5). O catálogo **não deve ser tratado como motor decisório integralmente
automático**.

### O que individua uma regra (confirmado, 2026-07-28)

Confirmado pela coordenação da auditoria:

> Uma regra é o **conjunto de aferições necessário para conceder o
> benefício**. Havendo divergência nos **critérios aferidos**, as regras
> **não são idênticas** — ainda que fundamentadas no mesmo dispositivo legal.

**Benefício, não aposentadoria.** A distinção não é de estilo: o catálogo
cobre também a pensão por morte (`tipo_de_beneficio: PENSÃO POR MORTE`), e
uma definição escrita em torno da aposentadoria deixaria de fora as regras
de pensão — inclusive `regra-0012`/`0013` e `regra-0014`/`0015`, dois dos
três grupos discutidos abaixo.

Três consequências, e é importante não estendê-las além do que a frase diz:

1. **A identidade de uma regra está nos critérios aferidos, não na
   fundamentação.** Duas regras que citam o mesmo dispositivo são regras
   distintas se algum critério aferido diverge. O caminho inverso — mesma
   aferição, fundamentação diferente — a frase não trata.
2. **`sexo` é critério aferido**, dado como exemplo explícito. É a primeira
   coluna de domínio a sair de "candidato" (Q3) para confirmada como
   **predicado**. As demais continuam abertas: isto confirma *um* critério,
   não a lista deles.
3. **Nome repetido não é, por si, duplicação.** Se duas regras diferem em
   critério aferido, elas são legitimamente duas — o que falha ali é o
   `nome`, que não carrega a distinção que o registro carrega (ver "O papel
   do campo `nome`"). Hoje 25 dos 41 grupos `P1_NOME_REPETIDO` diferem
   **apenas** em `sexo`, e por esta definição são regras distintas com
   rótulo ambíguo — não regras duplicadas.

O que a frase **não** responde: se a divergência de critérios é condição
apenas *suficiente* ou também *necessária* para a não-identidade. Ou seja,
duas regras com aferição idêntica que divirjam só em `integral`/
`tipo_calculo`/`paridade` — os "resultados candidatos" da Q6 — podem ou não
ser a mesma regra, e a resposta continua aberta.

### A granularidade da aferição é escolha do IPERON (confirmado, 2026-07-28)

Também confirmado pela coordenação da auditoria:

> As aferições podem ser mais ou menos granulares **por conveniência do
> IPERON**: por exemplo, uma regra para "doença da lista" ou uma regra para
> cada doença específica.

Logo **o número de regras do catálogo não é determinado pela lei**. Dois
catálogos de granularidades diferentes podem ambos estar corretos, e mudar a
granularidade é decisão operacional — não correção de erro jurídico. É essa
elasticidade que a decomposição 1:N e a consolidação N:1 da
[RFC 0004](../rfc/0004-schema-enriquecido-e-compilador-para-o-sisprev.md)
existem para representar.

E é aqui que as duas frases se encontram, com uma consequência que muda a
leitura do `P2_IGUALDADE_MATERIAL_ATIVA`: se o IPERON escolhe uma
granularidade **mais fina do que as colunas registram**, as regras assim
separadas são legitimamente distintas *e* aparecem byte a byte idênticas no
catálogo. O P2 estaria então apontando uma **lacuna de schema** — falta a
coluna que carrega a distinção —, não uma duplicação.

Os 3 grupos sem **nenhum** campo distinto são os candidatos a essa leitura:

| grupo                      | hipótese de granularidade                                                                                                                                                                                    |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `regra-0068`/`0069`/`0070` | o art. 8º da ECE 146/2021 tem **exatamente três incisos** (66 pontos/15 anos de exposição; 76/20; 86/25) e há **exatamente três** regras idênticas — nenhuma coluna registra pontuação ou tempo de exposição |
| `regra-0012`/`0013`        | pensão por morte sob o mesmo dispositivo, distinção não registrada                                                                                                                                           |
| `regra-0014`/`0015`        | idem                                                                                                                                                                                                         |

**Isto é hipótese, não conclusão.** A correspondência 3-incisos/3-regras é
forte, mas nada no repositório *diz* que foi essa a granularidade escolhida —
confirmá-la é pergunta ao IPERON, e é o que separa "o catálogo não consegue
expressar a distinção" de "as regras estão duplicadas". Os três grupos
seguem cobertos por achado aberto e por `P2_IGUALDADE_MATERIAL_ATIVA`, como
antes: a definição reenquadra a pergunta, não a fecha.

### O escopo é parametrização, não mudança do sistema (confirmado, 2026-07-28)

> Alterar enum altera o sistema; o nosso trabalho com as regras é de
> **parametrização**.

Isso delimita o que uma correção de auditoria pode ser, e a fronteira passa
pelo **tipo declarado de cada coluna** no mapa P13.2
(`scripts/regra_schema.py::COLUMNS`, campo `tipo`):

| dentro do escopo (parametrização)                                 | fora do escopo (mudança do Sisprev)                        |
| ----------------------------------------------------------------- | ---------------------------------------------------------- |
| trocar o valor de uma coluna **dentro do domínio que ela já tem** | acrescentar membro a um enum (`string (enum)`, `S/N`, ...) |
| editar coluna de texto livre (`nome`, `FUNDAMENTACAO*`)           | criar coluna nova                                          |
| mudar a granularidade do catálogo (consolidar N:1, decompor 1:N)  | mudar o tipo de uma coluna                                 |

Duas consequências que não são óbvias:

1. **Quando a distinção entre duas regras não cabe em nenhuma coluna
   existente, isso é um achado, não um conserto.** A saída dentro do escopo é
   a granularidade (consolidar as regras que o sistema não sabe separar) ou o
   texto (a fundamentação de cada uma citar a alternativa que implementa) —
   nunca um enum novo. Pedir a coluna é legítimo, mas é pedido ao IPERON, e
   deve ser registrado como tal.
2. **`simulavel` decide se o texto basta.** Uma regra `simulavel: N` é
   escolhida por um humano lendo a fundamentação, então diferenciar o texto
   resolve. Uma regra `simulavel: S` é escolhida pelo motor, que não lê
   prosa: se duas regras `simulavel: S` são idênticas em todos os parâmetros,
   o sistema **não tem como** selecioná-las, e corrigir a fundamentação
   deixa o registro verdadeiro sem resolver a seleção.

É também a razão de a RFC 0004 ter um **compilador** em vez de um schema
substituto: o catálogo auditado pode ser mais rico do que o Sisprev, mas a
projeção deployable tem de caber nas colunas existentes — e
`compilador_auditado._checar_contrato_legado` é onde isso falha fechado.

### Identidade no tempo: o que uma edição pode fazer (2026-07-30)

Confirmado pela coordenação da auditoria:

> Alterações em `nome`, `fundamentacao`, `fundamentacao_integral` e
> `fundamentacao_proporcional` **não criam, por si só, nova regra nem rompem
> sua identidade**. Esses campos podem ser corrigidos ou complementados no
> mesmo documento, preservados `id`, `row_index` e a referência à importação
> original.

O alcance é maior do que os quatro campos citados: **nenhuma** edição de
conteúdo rompe a identidade de uma regra do bundle legado, porque a identidade
não é feita de conteúdo — é `id`, `row_index` e o vínculo com a linha da
importação. Consolidar N:1 ou decompor 1:N não é edição: é outro objeto, com
identidade própria em bundle separado (RFC 0004 §1.2).

**Identidade estável não é conteúdo congelado — e também não é autorização
para gravar.** São três perguntas independentes, e confundi-las é o erro que
esta seção existe para impedir:

| pergunta                              | resposta                                                                                                                                     |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| a edição cria regra nova?             | **nunca**                                                                                                                                    |
| a auditoria pode **gravar** a edição? | só onde o valor **não é deployável**, mais a exceção expressa do `nome`; todo outro campo deployável é decisão de quem responde pelo produto |
| o estado anterior sobrevive?          | só via unidade auditada + grupo de substituição (RFC 0004/0006); edição in loco é destrutiva                                                 |

Para os dois campos que a coordenação nomeou, a política nas quatro dimensões:

| dimensão             | `nome`                                                                              | `FUNDAMENTACAO*`                                                                                                 |
| -------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| identidade           | nunca altera `id`/`row_index`                                                       | idem                                                                                                             |
| substancialidade     | **nunca** — é rótulo de seleção, não critério nem efeito                            | não, na correção descritiva/citatória; **sim** em `simulavel: N` e na troca que muda o regime jurídico aplicável |
| autoridade           | **edição in loco autorizada** — a spec já manda que ele melhore durante a auditoria | **nunca in loco**: fundamento jurídico deployável, gravação de quem responde pelo produto; a auditoria propõe    |
| efeito em `revisada` | não reabre item de critério; pode dissolver um P1 e assim **liberar** `revisada`    | reabre o item que confere dispositivos contra a fundamentação                                                    |
| efeito em `validada` | **não demonstrado** que o ato anterior cubra o novo rótulo — aberto                 | **não demonstrado**: muda o fundamento impresso no ato administrativo — exige nova manifestação ou é da RFC 0007 |

A assimetria da autoridade é deliberada: errar o `nome` faz o usuário escolher
mal e se conserta escrevendo melhor; errar a fundamentação põe fundamento falso
num ato administrativo. É a mesma razão pela qual `nome` está fora da chave
material do P2 e `FUNDAMENTACAO*` está dentro.

**"A auditoria propõe" tem três veículos, em escala**: o corpo da regra (grava
nada — `regra-0025`), a unidade auditada com grupo `inativo` no conjunto (grava
a projeção em bundle separado — `regra-0078`), e a gravação no campo deployável
(decisão do dono do produto — ainda não ocorreu).

Uma alteração é **substancial** quando, depois dela, a regra **não afere os
mesmos critérios** ou **não produz os mesmos efeitos** — o teste não é "o texto
mudou?". Como Q3 e Q6 seguem abertas (só `sexo` está confirmada como critério
aferido), o teste ainda não se aplica campo a campo, e a fronteira vale por
**presunção por família de campo, derrotável por escrito**: corpo do `.md` e
anotações de auditoria (`dispositivos`, `precedentes`,
`disposicao_de_achados`) não são substanciais; `nome` e `FUNDAMENTACAO*` são
presumidos não substanciais; valor de coluna de domínio é presumido
substancial. Duas derrotas previsíveis da presunção, a fronteira completa e os
dois casos já decididos na prática (`regra-0078`/`achado-0017` e `regra-0025`)
estão na
[RFC 0012](../rfc/0012-identidade-estavel-e-alteracao-substancial.md) §3.

**Consequência para o P7, sem gate novo**: uma alteração substancial **reabre o
item do checklist que a cobria, qualquer que seja o campo** — e caixa aberta já
derruba `revisada` por `P7_ESTADO_INVALIDO`. Numa regra `validada`, exige
rebaixamento explícito no mesmo commit: o selo não sobrevive a uma mudança
**substancial** no que foi selado. Isso é escrito e não verificado, porque
`atos_validacao` não registra sobre qual conteúdo a autoridade se pronunciou
(`AtoValidacao` não tem data nem impressão do conteúdo) — a verificação depende
do ato por lote, que é da
[RFC 0007](../rfc/0007-prontidao-de-conjunto.md).

**Três perguntas, e a spec responde duas.** Que a regra corrigida mantém
`id`/`row_index`: **sim**. Que um achado disposto como `corrigida` não a bloqueia
mais: **sim** (P7). Que um `AtoValidacao` anterior cobre a redação corrigida
depois dele: **não está demonstrado**, e a spec não presume que cubra — nem para
`nome`, nem para `FUNDAMENTACAO*`, onde a razão é mais forte, porque a citação
corrigida muda o fundamento impresso no ato administrativo mesmo sem mudar
critério nem efeito. As duas saídas escrituráveis são exigir nova manifestação
ou tratar a cobertura como questão da RFC 0007. Identidade estável evita churn de
regras; **não** estende o alcance de um ato assinado sobre outro texto.

**Nenhum campo de trilha novo.** Quais campos mudaram é o diff; a natureza da
alteração, a fonte, quem decidiu e quando já moram em
`disposicao_de_achados[]` e, do lado da proposta, em
`UnidadeAuditada.decisoes`/`proveniencia` (RFC 0012 §4).

## O que esta spec exige

**Não exige que tudo seja parametrizado.** Exige que a fronteira entre
**automático**, **manual** e **desconhecido** seja explícita para cada
regra `revisada` (P7) — nunca implícita, nunca presumida pelo silêncio de
um campo.

Para cada regra `revisada`, deve ser possível responder, em linguagem
humana:

1. Quais fatos o sistema verifica automaticamente?
2. Quais fatos devem ser confirmados manualmente?
3. Quais documentos/evidências sustentam essa confirmação?
4. O que o sistema faz depois que a regra é selecionada?
5. Quais dispositivos jurídicos justificam cada critério e efeito?

Essas cinco perguntas são um **gate de julgamento humano** — não são
verificáveis por código (`scripts/estado_auditoria.py` documenta
explicitamente essa exceção: a transição para `revisada` depende deste
gate, mas o CI não o avalia). O papel desta spec é dar ao revisor a
estrutura para respondê-las de forma consistente entre regras, não
automatizar a resposta.

## O papel do campo `nome`

**Decisão de produto (2026-07-21):** o `nome` é a principal ferramenta
apresentada ao usuário para **selecionar a regra aplicável** entre as
candidatas que restam após a anamnese do requerente. Não é mero rótulo nem
basta ser único — precisa expressar os elementos que **distinguem
operacionalmente** a regra.

**Princípio central:**

> O nome deve ser a menor descrição, em linguagem humana, capaz de
> distinguir a regra das demais que ainda podem ser aplicáveis depois da
> anamnese do requerente.

Três campos, três papéis distintos:

- **`id`** — identidade técnica **estável** (`regra-NNNN`); nunca muda, é o
  vínculo com a importação e com achados/detecções. Não serve à leitura
  humana de seleção.
- **`nome`** — resumo operacional **mutável**, orientado à seleção; deve
  **melhorar durante a auditoria** conforme os fatos discriminantes ficam
  claros. É o que o usuário lê para escolher.
- **`fundamentacao*`** (e, quando vinculados, `dispositivos`) — suporte
  jurídico da regra; **não substituem** o nome. Se o usuário precisa abrir a
  fundamentação para descobrir a diferença entre duas regras, os nomes
  falharam.

### A gramática (fixada em 2026-07-30, derrotável)

A forma esteve deliberadamente aberta à espera das restrições reais da tela do
Sisprev. A coordenação da auditoria decidiu **fixá-la sem essa confirmação**,
declarando a premissa: `P1_NOME_REPETIDO` é, entre os gates de `revisada`, o que
alcança mais regras do catálogo, então esperar trava o trabalho inteiro por prazo
que a auditoria não controla, e nomear caso a caso garante incoerência entre
famílias. O registro da decisão está em
[decisões transversais da auditoria](../analysis/decisoes-de-auditoria-2026-07-30.md)
§2.

Seis posições, na ordem. **Cada posição só entra quando discrimina** a regra das
que ainda podem ser aplicáveis depois da anamnese — o nome não é descrição
completa, é a menor descrição que distingue.

| #   | posição               | entra quando                            | exemplo                            |
| --- | --------------------- | --------------------------------------- | ---------------------------------- |
| 1   | modalidade            | **sempre**                              | `Aposentadoria voluntária`         |
| 2   | recorte de carreira   | a modalidade tem regime próprio         | `do policial civil`                |
| 3   | marco de ingresso     | há mais de um trilho por data de posse  | `ingresso até 31/12/2003`          |
| 4   | critério aferido      | é o que separa as candidatas restantes  | `mulher`, `deficiência grave`      |
| 5   | resultado             | duas candidatas diferem só no resultado | `proventos integrais com paridade` |
| 6   | fundamento, abreviado | **só** como desempate final             | `(EC 146/2021, art. 7º)`           |

As posições são separadas por **travessão cercado de espaços**. Sem abreviação
opaca como carga principal ("Perm.", "c/c",
"§1º, I" sozinho): o nome é lido por quem escolhe a regra, não por quem já sabe
qual é. O teto de comprimento é o comprimento do maior `nome` da importação
original — um valor que o Sisprev **comprovadamente aceita** —, declarado em
`scripts/nome_gramatica.py` e ancorado em teste contra `data/raw/`, que é
imutável e por isso não envelhece.

Duas regras fazem a gramática ser honesta em vez de cosmética:

- **A citação legal é o último recurso, nunca o primeiro.** Unicidade é
  necessária e insuficiente: dois nomes que diferem **apenas** pelo número de um
  artigo continuam ruins, porque quem lê a tela não sabe qual artigo é o seu
  caso. Um nome que precise da posição 6 é sinal de que o discriminante real não
  foi encontrado.
- **Se as posições 1–5 não distinguem, não se desempata pelo número do
  artigo.** Duas regras que ficam com o mesmo nome depois de aplicada a gramática
  são **lacuna do modelo** — o catálogo não possui o predicado que as separa —, e
  isso é achado a registrar, não problema de redação (é o caso 0022 × P6/P7, ver
  `docs/analysis/reconciliacao-invalidez-incapacidade.md` e o piloto
  `docs/analysis/piloto-selecao-invalidez-incapacidade.md`). Desempatar por
  citação limparia o `P1` e apagaria a lacuna: trocaria um diagnóstico verdadeiro
  por um nome único.

**Continua não conferido**, e a decisão foi expressa em fixar a gramática apesar
disso: truncamento do campo na tela, comportamento de busca e de ordenação por
nome. A gramática é **derrotável** — uma restrição real que apareça depois a
ajusta, e o diff resultante é mecânico.

**O que a gramática não estende.** `nome` está fora da chave material do `P2`, e
renomear **não** dissolve grupo `P2`: o grupo é de igualdade material, e nome não
é material — corrigir nome resolve `P1` e deixa o `P2` de pé, que é o
comportamento correto.

## Categorias

**Só identidade/proveniência e estado (catálogo + auditoria) estão
confirmados.** A atribuição de cada campo de domínio a uma categoria
abaixo é **hipótese de classificação, a confirmar campo a campo** pela
investigação (Q3, Q5, Q6, Q9) — nunca uma classificação normativa já
decidida. A fonte de cada `categoria` por coluna é
`scripts/regra_schema.py::COLUMNS` (P13.2); esta seção apenas organiza
essa fonte única nos grupos que a spec P13.1 define — não a duplica nem
diverge dela.

### Identidade e proveniência (confirmado)

`id` (identidade técnica **estável** do documento — `regra-NNNN`, nunca
muda) e `row_index` (vínculo com a linha da importação congelada). `NOME` ↔
`nome` **não** é mero rótulo humano: é o resumo operacional orientado à
seleção, **mutável** durante a auditoria — ver "O papel do campo `nome`"
abaixo (P1). Nenhuma edição de conteúdo — `nome` e `FUNDAMENTACAO*`
incluídos — rompe a identidade: ver "Identidade no tempo".

### Estado no catálogo e estado da auditoria (confirmado — P2.1/P7/P12)

`status_regra`, `motivo_inativacao` (P2.1); `status_auditoria`,
`auditado_por`, `auditado_em`, `atos_validacao` (P7/P11). Nunca confundir
com aplicabilidade temporal — essa é outra dimensão (P5, ver abaixo).

### Elegibilidade temporal — inclusividade confirmada, fato jurídico parcialmente aberto (P5, Q1, Q2)

`DATA_ADM_ATE`, `DATA_ADM_APOS`, `DATA_DIREITO_ATE`, `DATA_DIREITO_APOS`.
A ordenação estrutural (round-trip, sentinelas preservadas e não
interpretadas) está confirmada.

**Confirmado pela coordenação da auditoria (2026-07-28) — resposta à Q1 e a
parte da Q2:**

- `DATA_*_ATE` é **inclusivo**: `ate = X` cobre o próprio dia X.
- `DATA_ADM_APOS` é **exclusivo**: `apos = X` cobre a partir do dia
  **seguinte** a X (`data_adm_apos = 31/12/2003` significa "admitido a
  partir de 01/01/2004").
- A escolha do campo segue a forma do requisito legal: exigência de data
  *até* usa o campo `ATE`; exigência de data *após* certo dia usa o `APOS`.
- **O valor gravado é o marco**, ajustado à semântica da coluna e ao que
  consta na legislação — não o primeiro dia da cobertura. Daí que janelas
  adjacentes gravem o **mesmo valor** nos dois campos (`ate = M` seguido de
  `apos = M` particiona sem buraco nem sobreposição).
- `DATA_DIREITO_ATE` é **prazo de implementação dos requisitos**: todos
  precisam estar completos até essa data.

**Segue aberto:** a que ato `DATA_ADM_*` se refere (nomeação, posse,
exercício, ingresso em sentido amplo); se `DATA_DIREITO_APOS` tem a leitura
simétrica do `ATE` (presumível, mas não confirmada — é o ponto da issue
#39, que pede resposta **por eixo** em vez de uma resposta única para
`DATA_*`); e, para pensão por morte, se "requisitos completados" equivale à
data do óbito. As sentinelas seguem não interpretadas.

Consequência de conferência: se o valor gravado é o marco, todo limite
não-sentinela deveria coincidir com uma data declarada pelos dispositivos
que a regra cita — vigência da norma ou prazo fixado no dispositivo. O
levantamento está em
[semântica das janelas temporais](../analysis/semantica-das-janelas-temporais.md).

### Critérios parametrizados — candidatos (Q3)

Campos que *talvez* participem da seleção automática — quais realmente
participam, e quais apenas configuram cálculo/apresentação, é
precisamente Q3:

- `TIPO DE BENEFICIO`, `TIPO`, `SEXO`;
- `APOS_ESPECIAL` (também candidato a apresentação — Q9).

### Requisitos de verificação manual/jurídica (Q5)

**Nenhuma das 27 colunas do CSV está mapeada aqui ainda.** A hipótese de
trabalho de Q5 é que requisitos como idade mínima, tempo de contribuição,
pedágio, atividade policial, natureza da incapacidade ou exposição
especial podem viver **fora do CSV** — em código, tabelas externas, outra
tela do Sisprev, ou análise manual sem suporte estruturado algum. Até Q5
ser respondida, esta categoria fica deliberadamente vazia: um campo só
entra aqui quando a investigação confirmar que ele *é* um requisito
verificado manualmente, não por suposição.

### Resultado/efeitos da seleção — candidatos (Q6)

A definição operacional de cada um, e se é resultado ou também predicado,
é justamente Q6:

- `PARIDADE`, `INTEGRAL`, `TIPO_CALCULO`;
- `ADICIONAL_INATIVIDADE` (também candidato a apresentação — Q9).

### Comportamento de implementação/apresentação — candidatos (Q9)

Se são condições, efeitos, ou controles de interface é precisamente Q9:

- `SIMULAVEL`, `TIPO_REMUN`, `TabelaPontuacao`;
- `Requisitos da IN Nº 5/2020`, `Relatório p/ Reserva Remunerada por Idade ex-officio`;
- `VISIVEL DTC PROPORCIONAL`, `VISIVEL DTC INTEGRAL`;
- `APOS_ESPECIAL`, `ADICIONAL_INATIVIDADE` (listados também acima).

### Fundamentação e dispositivos (P3)

`FUNDAMENTACAO_PROPORCIONAL`, `FUNDAMENTACAO_INTEGRAL`, `FUNDAMENTACAO` —
campos do frontmatter (o frontmatter *é* a regra deployável; o corpo do
`.md` é análise autoral, não deployado nem material para o detector P2). A
granularidade de citação (menor unidade citada, decomposição sob demanda) é
P3; o bundle `okf/dispositivos/` **já existe** e a infraestrutura P3 está
implementada — o que permanece pendente é a **cobertura**: as regras ainda
não estão sistematicamente vinculadas aos dispositivos (especialmente os
estaduais).

### Legado a reconciliar (candidatos — P7)

`VALIDADO PGE`, `VALIDADO PRESIDENCIA` — candidatos a derivar de
`atos_validacao` (P7) em vez de permanecerem booleanos soltos. Os 112
valores `FALSE/FALSE` da importação **não demonstram** que sejam um único
ato ou dois atos obrigatórios — ausência de casos divergentes numa base
não validada é falta de evidência, não evidência de unicidade (ver RFC,
P7, ressalvas de Q12).

### Metadados de processo (sem categoria semântica própria)

`ATUALMENTE NO SISTEMA` (estado no Sisprev real — não confundir com
`status_regra`), `CICLO DE VALIDAÇÃO` (ordenação do processo de
auditoria).

## `# Estado da análise` — a seção obrigatória do corpo para `revisada`

**Decisão (2026-07-29):** o corpo exige **uma** seção de nível 1,
`# Estado da análise`, contendo um checklist. Ela substitui as quatro seções
fixas que a versão anterior desta spec exigia (`# Critérios avaliados pelo Sisprev`, `# Requisitos de verificação manual`, `# Documentos ou evidências necessários`, `# Resultado após a seleção`).

**Por que as quatro caíram.** A checagem que as sustentava só conferia que
cada seção *existia e tinha texto não vazio* — o literal `TODO` passava nas
quatro. Ela certificava uma forma, nunca que alguma análise tivesse
acontecido. E, sendo forma fixa, não tinha onde registrar **o que ainda
falta**, que é justamente o estado que uma auditoria em curso precisa
carregar. Na primeira vez que as quatro foram escritas de verdade (regras
0006–0009), foi preciso inventar uma quinta seção só para o que não cabia
nelas.

O checklist inverte as duas coisas: quem escreve decide os itens que
*aquela* regra precisa, e **uma caixa aberta bloqueia `revisada`**.

```markdown
# Estado da análise

Comentário livre é bem-vindo — por que a regra é assim, o que a distingue
das vizinhas, o que se descobriu conferindo.

- [x] Critérios do cadastro conferidos contra a lei
- [x] Dispositivos vinculados conferidos contra os campos de fundamentação
- [ ] Causa da incapacidade — depende da Q6, não decidível hoje
```

`scripts/estado_auditoria.py::check_p7_estados` verifica
**estruturalmente**, para toda regra `revisada` (herdado por `validada`),
código `P7_ESTADO_INVALIDO`:

- a seção existe e não está vazia;
- há **ao menos um item concluído** — texto livre sozinho não afirma nada
  conferível e reconstruiria o buraco das quatro seções;
- **nenhum item está aberto**.

Item é reconhecido por uma gramática só, para os dois estados: marcador
`-` ou `*` **no início da linha** (indentação permitida), seguido da caixa
com exatamente um espaço (aberto) ou `x`/`X` (concluído), seguida de espaço
ou fim de linha.

Tudo o que não casa exatamente com isso é **prosa**, e prosa sozinha não
satisfaz o gate. Em particular `- [TODO] conferir` não é item: é
placeholder vestido de caixa, e admiti-lo devolveria o defeito das quatro
seções com outra grafia. O mesmo vale para colchete não fechado (`- [abc`)
e para ocorrência no meio da linha (`conferi tudo - [x] mesmo`).

Contar `- [ ]` continua sendo verificação de forma, nunca de mérito: o CI não
avalia se os itens são os certos, nem se um item marcado foi honestamente
marcado. Isso segue sendo julgamento humano.

### O item que uma regra `revisada` não pode deixar de ter (2026-07-30)

Quem escreve decide os itens, com **uma** exceção. O checklist de uma regra
`revisada` tem de cobrir a **quinta pergunta do P13.1** — qual dispositivo funda
qual critério —, que deixou de ser recomendação e passou a ser conteúdo exigido
(decisão registrada em
[decisões transversais da auditoria](../analysis/decisoes-de-auditoria-2026-07-30.md)
§7).

A razão é o que `revisada` afirma. Sem esse mapa, o selo diria que a auditoria
terminou sem que ninguém tenha conferido se **cada** critério aferido tem
fundamento — e é esse o conteúdo do trabalho; as outras conferências são
mecânicas em comparação.

**Nenhum campo novo, nenhum gate novo, e é de propósito.** O mecanismo é o
checklist que já existe: uma caixa aberta derruba `revisada` por
`P7_ESTADO_INVALIDO`. O CI continua conferindo forma e nunca mérito — ele não
sabe, e não deve saber, se o item que fala de dispositivos foi honestamente
respondido. A relação `critério → dispositivo` segue **sem schema** pela razão da
RFC 0008 §5: `dispositivos:` é a união achatada da articulação e perde qual
provisão funda qual critério, e recuperar isso é prosa autorada, não campo.

O custo é real e foi aceito: cada regra exige prosa própria, e não há atalho.

**As quatro perguntas não desapareceram.** Elas continuam sendo o que a
seção "Elegibilidade e fronteira de automação" desta spec pede que se
responda, e são os **itens iniciais recomendados** do checklist de uma regra
nova. O que acabou foi a exigência de que fossem headings literais,
conferidos por casamento de string.

A quinta pergunta ("quais dispositivos justificam cada critério e efeito")
tampouco é heading obrigatório — a RFC 0008 §5 registra que ela é
conferência humana, sem campo nem gate. Na prática ela vira um item do
checklist e, quando houver o que mostrar, uma seção livre no mesmo corpo.

**A seção existe onde a análise foi feita, e só ali** — a `regra-0025` é um caso
escrito. Esta spec não a adiciona retroativamente: fabricar a análise violaria o
princípio da autoria humana (RFC 0001, topo). Ela é escrita regra a regra, por um
auditor, no momento em que a investigação de fato acontece — e só então a regra
pode transicionar para `revisada`.

O corpo da regra **nunca** contém uma seção `# Achados`: problemas de
auditoria são conceitos próprios em `achados/`, referenciando a regra via
`regras_afetadas` (P14) — nunca embutidos no `regra-*.md`.

## `disposicao_de_achados` — a regra responde a cada achado que a nomeia

**Decisão (2026-07-29):** o **frontmatter** ganha
`disposicao_de_achados`, uma lista em que a regra responde, uma a uma, aos
achados abertos que a nomeiam. O corpo continua sem `# Achados` — a
proibição do parágrafo anterior segue integralmente em vigor, e é a chave
do desenho.

**Uma ponta declara, a outra dispõe.** O achado continua dono de duas
coisas: *qual é o problema* e *quais regras ele alcança*. O que a regra
ganha é só *como esta regra em particular responde*. Sem essa divisão o
campo seria a segunda ponta declarando a mesma relação — duas verdades sem
gate que as reconcilie, o defeito que a convenção de `dispositivos:` e de
`precedentes` existe para evitar. Aqui **há** gate: uma entrada só vale se
aponta para um achado que existe e que já nomeia esta regra em
`regras_afetadas`.

### Por que o campo é necessário

`situacao` é **um campo só para toda a população do achado**, e a população
é heterogênea por construção. Dos 52 achados abertos, **46 alcançam mais de
uma regra**; o `achado-0047` alcança 16, em três causas com três consertos
diferentes. Ele será resolvido para `regra-0093`/`0094` — basta numerar a
emenda — muito antes das quatro que não citam a norma em campo algum. Hoje
não há como dizer isso: o achado é aberto ou resolvido para todas de uma
vez.

### O campo aperta o gate, não o afrouxa

Antes desta decisão, `revisada` só olhava achado `bloqueante`, e o catálogo
tinha **um** — os achados abertos impunham quase zero ao estado da
auditoria, e uma regra podia atravessar o gate com quatro achados abertos
sobre ela e nada escrito sobre nenhum. (São **sete** bloqueantes desde a
aplicação do critério de severidade adiante; o argumento não depende do
número, e é a razão pela qual o gate não podia depender só dele.)

Agora toda regra `revisada` precisa de disposição escrita para **cada**
achado aberto que a nomeie — hoje, **199 obrigações** que não existiam. O
`informativo` deixou de ser silencioso sem virar `bloqueante`: ele não
impede, mas exige resposta.

E a recíproca é o que sustenta a auditoria viva: **um achado autorado
amanhã sobre uma regra já `revisada` a invalida na hora**, até que ela
disponha dele especificamente. É a mesma semântica de rebaixamento não
automático do P7 — o CI acusa com `P7_ESTADO_INVALIDO`, e um humano decide
entre dispor e rebaixar. Nada aqui rebaixa sozinho.

### Forma

```yaml
disposicao_de_achados:
  - achado: /achados/achado-0022.md
    disposicao: encaminhada
    decisao_pendente_de: dono_do_campo
    justificativa: >-
      O prazo de 31/12/2024 é decisão do dono do campo: gravá-lo torna a
      regra inelegível para requisito completado a partir de 2025. A
      conferência da auditoria terminou; o que resta não é dela.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-29
```

Este exemplo é o que **derrubou** a proibição categórica de dispor de um
bloqueante (2026-07-30). O `achado-0022` é bloqueante; a versão anterior desta
seção exibia exatamente esta entrada como forma canônica e, três parágrafos
abaixo, declarava que bloqueantes não eram disponíveis. O exemplo era reprovado
pelo gate que ele documentava — e não por descuido de redação: a disposição
**é** a coisa certa a escrever aqui, e o gate a tornava inexprimível.

Os três valores de `disposicao`:

| valor           | o que afirma                                                                                                                |
| --------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `nao_se_aplica` | o defeito descrito **não se materializa** nesta regra — a população do achado alcançou além do que devia                    |
| `encaminhada`   | o defeito é **real aqui**, e o que resta não é da auditoria (dono do campo, questão de domínio aberta, fluxo institucional) |
| `corrigida`     | esta regra foi **editada** e o achado não vale mais para ela, embora siga aberto para as outras da população                |

`encaminhada` chamava-se `nao_impede` até 2026-07-30. O nome antigo era verdade
pela metade: ela não impede a **revisão**, mas segue impedindo a **validação**
(ver abaixo). O rename saiu praticamente sem migração de dado, porque o campo
tinha acabado de nascer: a `regra-0025`, autorada em paralelo, gravava o valor
antigo e foi migrada à mão na integração das duas frentes. Um nome que descreve
metade do efeito é o tipo de coisa que só fica mais caro de corrigir.

`justificativa` é **obrigatória e não vazia**. Um achado posto de lado sem
razão escrita é exatamente o modo de falha que este campo existe para
impedir: "ignorado" não é disposição, é omissão com um lugar para morar.
`decidido_por`/`decidido_em` são a mesma trilha que o P11 exige de
`auditado_por`/`auditado_em`, pelo mesmo motivo — dispensar um achado é
decisão, e decisão sem autor nem data é um estado que se flipou.

### O que o gate verifica, e o que deliberadamente não

`scripts/estado_auditoria.py` checa, **em qualquer estado** (código
`P7_DISPOSICAO_INVALIDA` — escrituração malformada é defeito agora, não na
hora da transição):

- o achado referenciado **existe**;
- ele **nomeia esta regra** em `regras_afetadas` — senão é disposição de
  relação que ninguém declarou;
- o mesmo achado não é disposto duas vezes;
- o contrato Pydantic da entrada valida (`justificativa` não vazia,
  `disposicao` no enum, data real). Sem esta checagem o campo ficaria
  invisível quando malformado, e o único sintoma seria "achado aberto sem
  disposição" numa regra que dispôs de tudo e só deixou uma justificativa em
  branco;
- **`decidido_em` não está no futuro.** É a consequência direta de equiparar
  `decidido_por`/`decidido_em` à trilha do P11: `auditado_em` já exige data
  não futura, e uma decisão datada adiante não aconteceu. A checagem vive na
  camada que conhece o "hoje" (`estado_auditoria`, o mesmo valor que
  `RegraAuditoriaContrato` recebe por `context={"today": ...}`), não no
  contrato Pydantic de `DisposicaoDeAchado`, que não recebe contexto.

A data de `detectado_em` é lida pelo **acessor tipado** `Achado.detectado_em`,
nunca do dict bruto do frontmatter, e a regra cronológica de `corrigida`
depende disso. O YAML tipa o valor conforme o autor tenha citado a data ou
não — `2026-07-18` chega como `date`, `'2026-07-18'` como `str` —, e três dos
52 achados usam a forma citada (`achado-0008`/`0009`/`0010`). Um
`isinstance(..., date)` sobre o dict bruto passa por esses três **em
silêncio**: o gate existiria e não checaria nada exatamente onde a data foi
escrita de outro jeito.

E, para `revisada`/`validada` (código `P7_ESTADO_INVALIDO`): **nenhum achado
aberto que nomeie a regra fica sem disposição**.

### Quando um achado é `bloqueante`

`severidade` era, até aqui, escolha do autor sem critério escrito, e o
resultado apareceu no agregado: **1 bloqueante em 50 achados**, com achados
que demonstram campo deployável contradizendo a norma aplicável classificados
como `informativo`. A distribuição não descrevia o conteúdo do corpus.

O critério, doravante:

> Se o achado **demonstra** — não suspeita — que um campo **deployável**
> contradiz a norma aplicável, invoca dispositivo inexistente, pertence a
> outro benefício, ou promete regime de cálculo diferente do que o cadastro
> executa, a severidade presumida é **`bloqueante`**.

Os três termos fazem trabalho:

- **demonstra**: a conferência está fechada contra a fonte. Achado cujo lado do
  erro é indeterminado permanece `informativo`, porque bloquear exigiria fixar
  uma hipótese que o próprio achado declara aberta. O
  [`achado-0024`](../../okf/regras-sisprev/achados/achado-0024.md) é o caso que
  mostra o termo funcionando nos dois sentidos: enquanto não se sabia se o
  `23/10/2021` das quatro regras ou o `vigencia_inicio` do bundle era o errado,
  ele era `informativo`; quando a publicação da LCE 1.100/2021 foi identificada
  em fonte própria (DOE/RO nº 207, de 18/10/2021, na ficha oficial do SAPL), a
  simetria caiu e ele passou a
  `bloqueante` **sem que nenhum fato sobre o campo mudasse**. O que mudou foi o
  direito de afirmar. É por isso que o critério fala de demonstração e não de
  gravidade: um defeito grave e não demonstrado ainda não é bloqueante.
- **deployável**: o campo vai para o Sisprev. Defeito que vive só no corpo,
  no `nome`, ou numa pendência de modelagem sem valor errado gravado
  (`achado-0020`, `achado-0026`) não bloqueia — não há ato administrativo
  saindo errado por causa dele.
- **presumida**: é presunção derrotável, e a derrota se escreve. Um achado
  que satisfaz o critério e ainda assim fica `informativo` deve dizer no
  corpo por quê — o [`achado-0045`](../../okf/regras-sisprev/achados/achado-0045.md)
  é o caso: a redação vinculada é temporalmente impossível, mas o próprio
  achado demonstra que os requisitos materiais das duas redações são iguais,
  então nenhum requerimento é decidido diferente.

O critério é **de mérito, não de gate**. Nada no CI o verifica, e nada
poderia: decidir se um achado demonstra contradição com a norma é exatamente
o julgamento que o CI não faz. Ele existe para que a severidade seja
comparável entre autores e entre lotes, e para que a diferença entre "isto
impede a regra de ser considerada revisada" e "isto precisa de resposta
escrita" seja uma leitura do corpo, não do humor de quem escreveu o
frontmatter.

### Em achado `bloqueante`, o que a disposição libera depende de qual é ela

**Decisão 2026-07-30**, revendo a proibição categórica que valia antes. A
preocupação que a originou é real — uma regra não se absolve da acusação que
recebeu —, mas ela alcança **uma** das três disposições, e proibir as outras
duas custava caro:

| disposição em achado bloqueante | `revisada` | `validada`                     |
| ------------------------------- | ---------- | ------------------------------ |
| `nao_se_aplica`                 | proibida   | proibida                       |
| `corrigida`                     | permitida  | permitida                      |
| `encaminhada`                   | permitida  | **proibida enquanto pendente** |

A distinção resolve o problema conceitual, e é por isso que ela mora entre os
dois estados e não na severidade:

- **`revisada`** afirma que *a auditoria terminou* — identificou o defeito e
  registrou o seu encaminhamento. Isso ela pode afirmar carregando um defeito
  cuja correção não é dela;
- **`validada`** afirma que *a regra pode receber validação institucional*, e
  isso não deve acontecer com defeito bloqueante ainda reconhecido como real
  pela própria regra.

Por disposição:

- **`nao_se_aplica` segue proibida.** É a única autoabsolvição: a regra acusada
  afirmando que o defeito não existe nela contradiz diretamente quem a nomeou.
  Quando a população de um bloqueante estiver errada, quem a corrige é o autor
  do achado — a regra não encolhe o achado por procuração;
- **`corrigida` é liberada**, e proibi-la era o caso mais indefensável: a regra
  consertou o defeito e ficava travada até o autor do achado perceber. É
  afirmação de fato, conferível no diff, não juízo sobre a acusação. Exige
  `decidido_em >= detectado_em` do achado — não se corrige o que ainda não
  existia;
- **`encaminhada` libera `revisada` e nunca `validada`**, e exige
  `decisao_pendente_de` não vazio. "Não é da auditoria" sem dizer de quem é
  deixa o defeito sem dono, e defeito sem dono não é encaminhamento — é
  arquivamento com outro nome.

**Sem disposição, o bloqueante bloqueia os dois estados, como antes.** O
afrouxamento é seletivo: ele não abre porta nenhuma para quem não escreveu nada.

**A severidade não foi tocada, e isso é deliberado.** A alternativa considerada
era redefinir `bloqueante` como "a auditoria consegue fechar sozinha" — o que
rebaixaria a informativo todo defeito que dependa do dono do campo. Foi
recusada: misturaria gravidade com competência, e um defeito jurídico grave não
fica menos grave por depender de terceiro.

**O que o gate ainda não interpreta** é a `justificativa`. Decidir se a razão
escrita é *boa* é mérito, e é a linha que o CI não cruza — a mesma de contar
`- [ ]` sem julgar se os itens são os certos. O que ele passou a interpretar,
desde esta decisão, é *qual* das três disposições foi escolhida: isso não é

### Fora da chave material do P2

`disposicao_de_achados` fica **fora** da chave material do
`P2_IGUALDADE_MATERIAL_ATIVA`, junto de `dispositivos`, `atos_validacao` e
`precedentes`. O argumento é o mesmo e aqui fica **circular** se ignorado:
duas regras materialmente iguais caem na população dos mesmos achados e
recebem as mesmas disposições, e a disposição existe *por causa* do achado
que documenta o grupo. Material, anotar o achado apagaria o grupo que o
achado descreve — o documento invalidaria a si mesmo.

Vai para o CSV **derivado** em coluna própria, JSON-codificada, como
`precedentes`.

**O campo aparece onde alguém dispôs de um achado, e só ali** — a `regra-0025`
dispõe do `achado-0008` como `encaminhada`. Ele não é preenchido
retroativamente, pelo mesmo motivo do `# Estado da análise`: fabricar a
disposição violaria o princípio da autoria humana. Consequência imediata e
esperada: uma regra alcançada por achado **não pode** ser `revisada` até que
alguém escreva, achado por achado, por que ele não a impede.

## Questões abertas (Q1–Q12)

Esta spec organiza a fronteira; não a preenche. As doze questões
semânticas que a preenchem estão listadas no RFC 0001, seção P13, e são
respondidas pela investigação junto ao Sisprev, à documentação e à análise
jurídica — não por este documento. Cada resposta deve atualizar tanto esta
spec (a categoria do campo, se envolvido) quanto o mapa `regra_schema.py`
(a `categoria` da `ColumnSpec` correspondente), mantendo as duas em
sincronia com a mesma fonte de verdade conceitual.

Estado em 2026-07-29 — **não são mais doze em aberto**:

| questão         | estado                                                                                                                                                                                                      |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Q1              | **respondida** — `ATE` inclusivo, `DATA_ADM_APOS` exclusivo, o valor gravado é o marco legal (ver "Elegibilidade temporal")                                                                                 |
| Q2              | **parcial, com premissa** — `DATA_DIREITO_ATE` é prazo de implementação dos requisitos; `DATA_DIREITO_APOS` segue **não confirmado** e é lido por premissa expressa (exclusivo, valor é o marco), issue #37 |
| Q3              | **parcial** — `sexo` confirmado como critério aferido; as demais colunas de domínio seguem candidatas (ver "Critérios parametrizados")                                                                      |
| Q10             | **aberta, com premissa** — vazio é lido como **não gravado**, nunca como `AMBOS` presumido nem como "não aplicável"; ou seja, vazio é pendência, não valor                                                  |
| Q4–Q9, Q11, Q12 | abertas                                                                                                                                                                                                     |

**"Com premissa" não é resposta, e a diferença é o que a torna utilizável.** Q2 e
Q10 são fatos sobre o Sisprev, não decisões da auditoria, e não temos resposta.
Bloquear tudo o que delas depende retiraria da mesa boa parte dos achados por
prazo indeterminado; decidi-las como se fossem nossas contrariaria o escopo, que
é parametrização e não mudança do sistema. A saída decidida em 2026-07-30 é a
terceira: **premissa expressa, marcada como não confirmada**, com uma condição
que é o ponto todo — **toda conclusão que dela depender cita a premissa**. Assim
uma resposta futura do IPERON invalida um conjunto identificável de conclusões,
em vez de deixar dúvida sobre o catálogo inteiro. O registro está em
[decisões transversais da auditoria](../analysis/decisoes-de-auditoria-2026-07-30.md)
§8.

A redação anterior desta seção afirmava que as doze "permanecem abertas por
desenho", o que deixou de ser verdade em 2026-07-28 sem que o texto
acompanhasse — a nota de status no topo já registrava Q1 e parte de Q2/Q3.
Divergência entre duas partes do mesmo documento é o modo de falha que a
regra "quando o mapa e a spec divergirem, a spec ganha" existe para
absorver; dentro de um documento só não há ganhador, então o texto tem de
ser único.
