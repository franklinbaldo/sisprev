# RFC 0012 — Identidade estável, alteração substancial e quem pode gravá-la

- **Status**: proposta (2026-07-30). **Declaração, sem implementação.** Não
  edita nenhum `regra-*.md`, não cria campo, não cria gate, não altera o CSV
  derivado, os detectores, o site nem os workflows. Entrega a fronteira escrita
  e o confronto dela com os dois casos que o repositório já decidiu na prática.
- **Parte de / depende de**:
  [RFC 0001](0001-criterios-de-validacao-das-regras.md) (P2 igualdade material,
  P7 `status_auditoria`, P13.1, P14 achados),
  [`docs/spec/regra.md`](../spec/regra.md) ("O que individua uma regra", "O
  papel do campo `nome`", `disposicao_de_achados`),
  [RFC 0004](0004-schema-enriquecido-e-compilador-para-o-sisprev.md) §1.2
  (identidade própria da unidade auditada) e
  [RFC 0006](0006-conjuntos-de-regras.md) (o conjunto como preservação do
  estado anterior). A parte que fica em aberto aqui é devolvida à
  [RFC 0007](0007-prontidao-de-conjunto.md), dona do ato que autoriza produção.
- **Depende da [#61](https://github.com/franklinbaldo/sisprev/pull/61) no
  vocabulário e no efeito**: a §5 cita `corrigida`/`encaminhada` e o que cada
  uma libera em achado `bloqueante`. `encaminhada` é o nome que a #61 dá ao
  antigo `nao_impede`; enquanto ela não entrar, o valor gravável é o nome
  antigo e o efeito é o categórico (bloqueante não disponível). Esta RFC não
  cria nem altera nenhum desses valores — ela declara em que célula da tabela
  da #61 cada caso da §3.5 cai.
- **Não-objetivo**: responder Q3 ou Q6 da RFC 0001 (quais colunas são critérios
  aferidos e quais são efeitos) — esta RFC depende delas e diz o que fazer
  enquanto seguem abertas; criar `alteracoes_autoradas` ou qualquer campo de
  trilha (§4 explica por quê); reabrir a identidade separada da RFC 0004;
  alterar `data/raw/regras-sisprev.csv`, imutável para sempre.

## 0. O problema

A auditoria vai corrigir regras — é a fase em que o trabalho está. Não existe,
hoje, frase escrita em lugar nenhum do repositório que diga o que uma correção
faz com a regra corrigida. Duas perguntas ficam sem resposta, e elas **não são
a mesma pergunta**:

1. Editar `nome` ou `FUNDAMENTACAO*` cria uma regra nova?
2. Quem pode gravar essa edição, e o que acontece com o estado anterior?

O silêncio na primeira empurra para dois erros opostos. Um deles já está
fechado por gate: fabricar `regra-0113` para consertar uma citação é impossível
— `_validate_identity` exige que o conjunto de `row_index` seja exatamente
`1..row_count`, e o job `bundle-imports-original` confere a cardinalidade
contra a importação congelada. O outro está aberto: **editar em silêncio uma
regra `validada`**, mantendo o selo sobre um conteúdo que a autoridade não viu.

O silêncio na segunda é mais caro, porque a resposta intuitiva ("é só editar, a
identidade é estável") é a que o próprio repositório **já recusou duas vezes**,
nas duas primeiras correções reais que apareceram (§3.3). A fronteira já está
sendo praticada; o que falta é estar escrita.

## 1. Decidido: identidade é `id` + `row_index` + a importação

> Alterações em `nome`, `fundamentacao`, `fundamentacao_integral` e
> `fundamentacao_proporcional` **não criam, por si só, nova regra nem rompem
> sua identidade**. Esses campos podem ser corrigidos ou complementados no
> mesmo documento, preservados `id`, `row_index` e a referência à importação
> original.

Isso é ratificação, não novidade: a spec já diz que `id` é "identidade técnica
**estável** — nunca muda" e que `nome` é "resumo operacional **mutável**, que
deve **melhorar durante a auditoria**". O que faltava era a afirmação negativa
— *conteúdo corrigido não é regra nova* —, e é ela que autoriza a auditoria a
trabalhar sem inventar identidade.

O alcance é maior do que os quatro campos citados, e vale declarar inteiro:
**nenhuma** edição de conteúdo rompe a identidade de uma regra do bundle
legado. Não há edição capaz disso, porque a identidade não é composta de
conteúdo — é `id`, `row_index` e o vínculo com a linha da importação.
Consolidar seis regras em três ou decompor uma em quatro **não** é edição: é
outro objeto, com identidade própria em bundle separado (RFC 0004 §1.2), e o
bundle legado segue congelado em 112.

**Identidade estável não significa conteúdo congelado** — a frase da
coordenação está certa. Só não decide quem pode descongelar o quê.

## 2. A confusão a evitar: "material" já quer dizer outra coisa

A formulação natural da fronteira — "alteração editorial *versus* alteração
material" — colide com vocabulário em vigor, e colide exatamente no campo mais
editado da auditoria.

O `P2_IGUALDADE_MATERIAL_ATIVA` chama de **chave material** o conjunto de
campos que decide se duas regras são iguais. Essa chave **inclui**
`FUNDAMENTACAO*` e **exclui** `nome` — e a exclusão/inclusão é deliberada e
documentada: diferenciar a fundamentação de duas regras idênticas "dissolve o
grupo honestamente", enquanto renomear limpa o `P1_NOME_REPETIDO` sem mexer no
P2. Se esta RFC chamasse de "alteração material" precisamente o oposto
(fundamentação como atributo editorial), o repositório passaria a ter uma
palavra com dois sentidos incompatíveis sobre os mesmos dois campos.

E há uma diferença de eixo por baixo da colisão, que vale nomear:

| pergunta                                              | eixo                               | quem responde |
| ----------------------------------------------------- | ---------------------------------- | ------------- |
| estas **duas** regras são a mesma regra?              | sincrônico, entre documentos       | P2            |
| esta regra, **depois** da edição, é a mesma de antes? | diacrônico, dentro de um documento | esta RFC      |

São perguntas diferentes com a mesma palavra. Por isso o termo desta RFC é
**alteração substancial**, e ele é definido no vocabulário que a spec já
confirmou — "uma regra é o conjunto de aferições necessário para conceder o
benefício":

> Uma alteração é **substancial** quando, depois dela, a regra **não afere os
> mesmos critérios** ou **não produz os mesmos efeitos**.

É o teste da coordenação ("a regra seleciona os mesmos casos e produz os mesmos
efeitos?"), escrito com os termos que a definição de regra já usa. E ele é o
teste certo: não olha se o texto mudou, olha se mudou o que a regra faz.

## 3. A fronteira, e os dois eixos que a tabela intuitiva mistura

### 3.1 Substancialidade não autoriza a edição

O teste da §2 responde "é a mesma regra?". Ele **não** responde "posso gravar
isso?", e tratar as duas como uma só é o defeito da tabela intuitiva. São três
questões independentes, e cada uma tem dono diferente:

| questão                               | resposta                                                                                                                                                | onde se decide                    |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| a edição cria regra nova?             | **nunca** (§1)                                                                                                                                          | esta RFC / `docs/spec/regra.md`   |
| a auditoria pode **gravar** a edição? | só onde o valor **não é deployável**, **mais a exceção expressa do `nome`** (§3.4); todo outro campo deployável é decisão de quem responde pelo produto | prática já em vigor, aqui escrita |
| o estado anterior sobrevive?          | só se a correção passar por unidade auditada + conjunto; edição in loco é destrutiva                                                                    | RFC 0004 / RFC 0006               |

O eixo **deployável** não é invenção desta RFC: é o mesmo termo que o critério
de severidade de achado usa ("o campo vai para o Sisprev"). E ele atravessa a
substancialidade em diagonal — `nome` e `FUNDAMENTACAO*` são campos
**deployáveis** e ao mesmo tempo os candidatos naturais a "atributo corrigível".
Uma citação errada corrigida na fundamentação pode não mudar aferição nenhuma
(não é substancial) e ainda assim mudar o fundamento que sai num ato
administrativo (é decisão do dono do campo).

### 3.2 A fronteira operacional

Enquanto Q3 e Q6 seguem abertas, o teste da §2 **não é aplicável campo a
campo**: das ~27 colunas, só `sexo` está confirmada como critério aferido, e
`integral`/`tipo_calculo`/`paridade` são candidatos a efeito *e* a predicado.
Logo a fronteira de hoje é uma **presunção por família de campo, derrotável por
escrito** — a mesma forma do critério de severidade, e pela mesma razão:

| alteração                                                                         | presunção                   | instrumento                                                       |
| --------------------------------------------------------------------------------- | --------------------------- | ----------------------------------------------------------------- |
| corpo do `.md` (`# Estado da análise`, análise, conferências)                     | não substancial             | edição direta — não é deployado, não é material para o P2         |
| anotação de auditoria (`dispositivos`, `precedentes`, `disposicao_de_achados`)    | não substancial             | edição direta — fora da chave material por decisão própria        |
| padronização ou esclarecimento de `nome`                                          | não substancial             | edição direta, com o defeito registrado como achado quando houver |
| correção de citação, número ou redação em `FUNDAMENTACAO*`                        | não substancial             | achado + proposta; a gravação é do dono do campo (§3.3)           |
| fundamentação mais completa, sem mudar requisitos nem efeitos                     | não substancial             | idem                                                              |
| troca de fundamento que altera o regime jurídico aplicável                        | **substancial**             | unidade auditada + grupo de substituição (RFC 0004/0006)          |
| valor de coluna de domínio (benefício, população, janela, cálculo, paridade, ...) | **substancial**             | idem                                                              |
| granularidade (consolidar N:1, decompor 1:N)                                      | não é edição — outro objeto | unidade auditada com identidade própria (RFC 0004 §1.2)           |

Duas derrotas previsíveis da presunção, e as duas se escrevem no documento que
propõe a mudança:

- **`FUNDAMENTACAO*` pode ser substancial**, e a spec já diz por quê sem tirar
  esta consequência: numa regra `simulavel: N` a fundamentação **é** o critério
  de seleção — quem escolhe a regra é um humano lendo aquele texto. Corrigi-lo
  muda quais casos a regra alcança sem que nenhuma outra coluna se mova. Numa
  regra `simulavel: S` o motor não lê prosa, e a presunção se sustenta.
- **Coluna de domínio pode não ser substancial** quando a Q9 confirmar que ela
  é apresentação, não condição nem efeito (`visivel_dtc_*`, `simulavel`,
  `tipo_remun`). Hoje isso é candidatura, não resposta — então a presunção
  vale.

### 3.3 Os dois casos que o repositório já decidiu

A fronteira acima não foi derivada da tabela; ela descreve o que já aconteceu
duas vezes em julho de 2026, e as duas vezes contra a leitura intuitiva.

**`regra-0078` (achado-0017) — correção só de fundamentação, e ainda assim por
substituição.** A regra tem `sexo: MASCULINO` e cita a alínea "b" do art. 1º,
II da LC 51/1985 — a alínea feminina (25/15 anos); a masculina é a "a"
(30/20). O texto termina em "mulher". Pela tabela intuitiva isso é "correção de
citação" e sai por edição direta. O que se fez foi
[`policial-civil-voluntaria-masculino`](../../okf/regras-auditadas/unidades/policial-civil-voluntaria-masculino.md):
uma unidade auditada em `elaboracao`, projetando as duas trocas, dentro de um
grupo `inativo` do conjunto `proposta-auditoria-2026-07` — e a `decisoes` da
unidade diz a razão em uma linha: *"a decisão de corrigir o campo deployável é
de quem responde pelo produto"*. Não foi a substancialidade que mandou; foi o
eixo da autoridade.

**`regra-0025` (PR #60) — valor de coluna conferido, gravado no corpo.** A
conferência fechou que `sexo` vazio e `integral` vazio são lapso, com os
valores conferidos (`AMBOS`, `N`). O PR declara: *"nenhum campo deployável
alterado — `sexo` e `integral` seguem vazios, com o valor conferido registrado
no corpo como proposta"*. É a mesma escolha, na família de campo em que a
presunção de substancialidade é mais forte.

Duas ocorrências não fazem uma regra, mas fazem uma prática — e uma prática não
escrita é a que se perde no terceiro caso.

### 3.4 A matriz normativa de `nome` e `FUNDAMENTACAO*`

Os dois campos que motivaram esta RFC, resolvidos nas quatro dimensões. É esta
tabela que responde "posso corrigir?" sem que a resposta se torne "posso gravar
qualquer coisa":

| dimensão                 | `nome`                                                                                                   | `FUNDAMENTACAO*`                                                                                                                                                       |
| ------------------------ | -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **identidade**           | nunca altera `id`/`row_index`; nunca exige `regra-NNNN` novo                                             | idem — e o gate torna a alternativa impossível (`_validate_identity`)                                                                                                  |
| **substancialidade**     | **nunca substancial**: não é critério aferido nem efeito, é rótulo de seleção                            | presumida **não** substancial na correção descritiva/citatória; **substancial** em `simulavel: N` (§3.5c) e na troca que muda o regime jurídico aplicável (§3.3, 0078) |
| **autoridade**           | **edição in loco autorizada** — é o único campo deployável que a spec manda melhorar durante a auditoria | **nunca in loco na regra legada**: é fundamento jurídico que sai em ato administrativo — a auditoria propõe                                                            |
| **efeito em `revisada`** | `importada` intacta; não reabre item de critério; pode **dissolver** um P1 e assim liberar `revisada`    | `importada` intacta; reabre o item "dispositivos vinculados conferidos contra os campos de fundamentação"                                                              |
| **efeito em `validada`** | **não demonstrado** que o ato anterior cubra o novo rótulo — aberto, §5                                  | **não demonstrado**, e com razão mais forte: muda o fundamento impresso no ato administrativo — §5, e a decisão é da RFC 0007                                          |

A assimetria da terceira linha é a parte que não se adivinha, e ela não é
invenção desta RFC: a spec já diz que o `nome` "**deve melhorar durante a
auditoria** conforme os fatos discriminantes ficam claros". Ele é deployável e
ainda assim editável pela auditoria porque é **rótulo de seleção, não fundamento
jurídico** — errar o nome faz o usuário escolher mal e se conserta escrevendo
melhor; errar a fundamentação põe fundamento falso num ato administrativo. É por
isso também que o `nome` está fora da chave material do P2 e a fundamentação
está dentro.

**Três veículos, em escala.** "A auditoria propõe" não é uma coisa só — são três,
e a escolha entre elas é por quanto a proposta já está fechada:

| veículo                                            | o que grava                    | quando                                                                 | precedente                   |
| -------------------------------------------------- | ------------------------------ | ---------------------------------------------------------------------- | ---------------------------- |
| **corpo da regra** (`# Estado da análise`)         | nada — proposta escrita        | o valor está conferido e a decisão de gravá-lo não é da auditoria      | `regra-0025` (PR #60)        |
| **unidade auditada** + grupo `inativo` no conjunto | a projeção, em bundle separado | a correção está fechada e se quer o estado anterior preservado ao lado | `regra-0078` (`achado-0017`) |
| **gravação no campo deployável**                   | a regra legada                 | decisão de quem responde pelo produto                                  | ainda não ocorreu            |

### 3.5 Três casos mínimos

**(a) Renomeação editorial.** Duas regras que diferem **apenas** em `sexo` e
carregam o mesmo `nome` — 25 dos 41 grupos `P1_NOME_REPETIDO` são exatamente
isso. Renomear para que o nome carregue o `sexo`: identidade intacta; **não
substancial** (a aferição não muda — a regra já aferia `sexo`, o rótulo é que
não dizia); autoridade **da auditoria**, in loco; e o efeito no estado é o
contrário do que se espera de uma edição — ela **dissolve** a detecção P1 e com
isso *libera* `revisada`, em vez de bloquear. O achado que documenta o grupo,
havendo um, recebe `corrigida` — que exige `decidido_em >= detectado_em`
(§5).

**(b) Correção de alínea na fundamentação, sem mudar critério.** A
`regra-0078`: `sexo: MASCULINO`, `simulavel: S`, e a `fundamentacao_integral`
cita a alínea "b" (feminina, 25/15) terminando em "mulher". Identidade intacta;
**não substancial** pelo teste — a regra é `simulavel: S`, o motor não lê prosa,
e a aferição é a mesma antes e depois; e ainda assim **não se grava in loco**,
porque o campo é deployável. Veículo: unidade auditada (foi o que se fez). No
estado: o `achado-0017` é **`bloqueante`**, então enquanto a correção não for
gravada a regra dispõe dele como `encaminhada`, com `decisao_pendente_de` no
dono do campo — o que **libera `revisada` e nunca `validada`**. É o caso que
mostra os dois eixos discordando: a substancialidade diz "pode", a autoridade
diz "não é sua".

**(c) Fundamentação de uma `simulavel: N` que muda quem é selecionado.**
`regra-0012` e `regra-0013`: pensão por morte, ambas `simulavel: N`, `nome`
**idêntico** e `fundamentacao_integral` **idêntica** — um dos três grupos P2 sem
nenhum campo distinto. Quem seleciona é um humano, e não há nada por que
selecionar: o rótulo é o mesmo e a prosa é a mesma. Diferenciar a fundamentação
de uma delas é a dissolução honesta do grupo *e* é **substancial**, porque numa
regra `simulavel: N` a fundamentação **é** o critério de seleção: depois da
edição, casos que caíam numa passam a cair na outra. Identidade intacta;
autoridade **não é da auditoria**; veículo: unidade auditada; no estado, derruba
`revisada` e exige rebaixamento explícito se a regra estivesse `validada`.

O caso (c) é o que justifica a matriz existir: o mesmo texto editado dissolve um
P2 (o que *libera* um estado) e é substancial (o que o *derruba*). Sem separar as
quatro dimensões, os dois efeitos parecem uma contradição. **Nada aqui autoriza
fazer essa edição hoje** — qual é a distinção entre 0012 e 0013 é pergunta ao
IPERON, e a hipótese segue registrada como hipótese.

### 3.6 A autorização, e exatamente onde ela para

O que esta RFC autoriza, expressamente:

> `nome` e `FUNDAMENTACAO*` podem ser **corrigidos e complementados** sem churn
> de identidade: nenhuma correção neles cria `regra-NNNN`, renumera `row_index`
> ou rompe o vínculo com a importação.

E onde para, com a mesma clareza:

> Isso **não** é autorização para gravar qualquer mudança diretamente na regra
> ativa, **nem retroatividade para o ato que validou uma versão anterior**.
> Preservar identidade responde à pergunta da identidade e a nenhuma outra:
> `FUNDAMENTACAO*` segue sendo campo deployável cuja gravação é de quem responde
> pelo produto, e a auditoria propõe pelos três veículos da §3.4. A única edição
> in loco que esta RFC autoriza em campo deployável é a do `nome`, e só porque a
> spec já a exigia.

A identidade estável existe para evitar **churn de regras** — não para estender
por tabela o alcance de um ato assinado sobre outro texto. As duas coisas se
pareceriam se "a regra é a mesma" quisesse dizer "o que se disse sobre ela
continua dito"; não quer.

## 4. A trilha: nenhum campo novo

A trilha pedida — quais campos mudaram, natureza da alteração, por quê, com que
fonte, decidido por quem e quando — está certa como exigência. Como campo novo
(`alteracoes_autoradas`) ela seria **quase toda duplicação**, e a parte que não
é duplicação é a que não se pode conferir.

| o que registrar                       | onde já mora                                                                                                                               |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| quais campos mudaram                  | o diff — e ele não pode mentir sobre si mesmo, ao contrário de uma autodeclaração                                                          |
| se é editorial, corretiva ou material | `disposicao_de_achados[].disposicao` (`corrigida` é literalmente "esta regra foi editada e o achado não vale mais para ela")               |
| por que a identidade foi preservada   | esta RFC e a spec — é decisão do repositório, não fato de cada regra                                                                       |
| qual fonte ou achado sustenta         | `disposicao_de_achados[].achado` + `justificativa` (obrigatória, com gate); na unidade auditada, `proveniencia.fontes_consultadas`/`notas` |
| quem decidiu e quando                 | `disposicao_de_achados[].decidido_por`/`decidido_em`; `UnidadeAuditada.decisoes[].quem`/`.data`                                            |

O campo pedido, portanto, **existe** — só não está no `regra-*.md`, e não é
acidente que não esteja: `UnidadeAuditada.decisoes` (`data`/`quem`/`o_que`) mais
`proveniencia` são exatamente a trilha da alteração autorada, e vivem no
documento que **propõe** a mudança, não na regra que ela pretende substituir. É
a mesma razão pela qual os deltas da RFC 0006 ficam no conjunto e não nas
regras: o frontmatter das 112 não muda, e a chave material do P2 fica intocada
por construção em vez de por argumento.

Um campo novo teria ainda dois defeitos próprios. Seria **a segunda ponta
declarando a mesma relação** — o defeito que as convenções de `dispositivos:`,
`precedentes` e `disposicao_de_achados` existem para evitar. E "quais campos
mudaram" não tem gate possível contra o diff, então uma entrada errada ficaria
mais autorizada que a verdade e ninguém saberia.

**Fica uma lacuna real, e ela se fecha sem campo**: a edição que não vem de
achado nenhum (padronizar um `nome`, por exemplo) não tem trilha estruturada.
Decisão: quando a edição **corrige um defeito**, o defeito se escreve como
achado — é o instrumento do repositório para isso, e é o que faz a correção
aparecer no site e no relatório da PGE, onde ela precisa ser visível. Um `nome`
que não distingue *é* defeito, e o `P1_NOME_REPETIDO` já o detecta. Quando a
edição não corrige defeito nenhum, git basta e não se inventa escrituração para
ela.

## 5. P7: o que a edição faz com o estado da auditoria

Os três níveis, e o que o gate de hoje realmente faz em cada um:

**`importada`** — nada a perder, nada a fazer. Correção livre, dentro dos
limites de autoridade da §3.

**`revisada`** — o P7 já é um join reverificado a cada commit, e ele já cai por
achado aberto sem disposição, por detecção P1/P2 ativa e por caixa aberta no
`# Estado da análise`. O que **não** cai é o item marcado: editar um valor de
domínio não desmarca `- [x] Critérios do cadastro conferidos contra a lei`.
Então o gate certifica que alguém conferiu **alguma** versão do documento, não
esta.

A obrigação, e ela não precisa de gate novo porque reusa o que já morde:

> Uma alteração substancial numa regra `revisada` **reabre o item do checklist
> que a cobria**. Reaberto o item, `revisada` cai pelo
> `P7_ESTADO_INVALIDO` que já existe, e a regra volta a `importada` até a
> reconferência.

É ato humano, como marcar a caixa sempre foi — mas é ato **visível** e com
consequência mecânica imediata, em vez de uma exigência que só existe em prosa.

**A disposição do achado é a outra metade, e esta RFC depende do efeito que a
[#61](https://github.com/franklinbaldo/sisprev/pull/61) estabelece** — a §4
falava de `corrigida` como trilha da edição sem dizer o que ela libera. Com o
vocabulário final (`corrigida`/`encaminhada`, o antigo `nao_impede`
renomeado), os efeitos em achado **`bloqueante`** são:

| disposição      | `revisada` | `validada`                     | exige                         |
| --------------- | ---------- | ------------------------------ | ----------------------------- |
| `nao_se_aplica` | proibida   | proibida                       | —                             |
| `corrigida`     | libera     | libera                         | `decidido_em >= detectado_em` |
| `encaminhada`   | libera     | **proibida enquanto pendente** | `decisao_pendente_de`         |

Isso fecha uma parte da matriz da §3.4 sem gate novo: a correção que a auditoria
**pode** gravar sai por `corrigida`; a que ela **não pode** gravar sai por
`encaminhada`, que é a forma escriturada de "identificamos, e a decisão é de
outro" — libera `revisada`, porque a auditoria terminou o que era dela, e nunca
`validada`, porque a regra segue carregando defeito bloqueante reconhecido como
real. O caso (b) da §3.5 é exatamente essa célula.

**E fecha só essa parte.** A tabela acima resolve a relação entre a regra e um
achado bloqueante; ela **não** diz nada sobre se um `AtoValidacao` anterior
cobre conteúdo editado depois dele. São três perguntas distintas, e a RFC
responde duas:

| pergunta                                            | resposta                 | onde                  |
| --------------------------------------------------- | ------------------------ | --------------------- |
| a regra corrigida mantém `id`/`row_index`?          | **sim**                  | §1, decidido aqui     |
| o achado corrigido continua bloqueando?             | **não**                  | #61, tabela acima     |
| o ato institucional anterior valida a nova redação? | **não está demonstrado** | aberto — §8, RFC 0007 |

`corrigida` liberar `validada` significa "este achado não a impede mais", nunca
"o ato que a validou alcança o texto novo". Confundir as duas faria a
estabilidade da identidade produzir **retroatividade do ato**, que é
precisamente o que ela não deve produzir.

**`validada`** — aqui a invariante desejada é clara e **não é computável hoje**:
`atos_validacao` não registra sobre qual conteúdo a autoridade se pronunciou.
`AtoValidacao` tem `tipo`/`autoridade`/`identificador`/`fonte`, todos texto não
vazio, `extra="forbid"` e **sem data** — nada no bundle permite dizer que o ato
veio antes desta edição. A regra fica escrita e não verificada, como o critério
de severidade:

> Alteração substancial numa regra `validada` exige, no mesmo commit, o
> rebaixamento explícito. Rebaixamento nunca é automático (P7), e o selo não
> sobrevive a uma mudança **substancial** no que foi selado.

O adjetivo diz o que **derruba** o selo, e não o converso: uma alteração não
substancial em campo deployável não fica, por não derrubá-lo, **autorizada a
mantê-lo**. Uma versão anterior desta RFC dizia que mantinha, e a afirmação não
se sustenta — nada no repositório demonstra que um
ato assinado sobre a redação A alcance a redação B, e é a fundamentação que
torna isso agudo: mesmo sem mudar critério nem efeito, a citação corrigida da
§3.5b **muda o fundamento jurídico impresso no ato administrativo**. O
`regra-0078` é prova do *veículo* (a correção foi para unidade auditada em grupo
`inativo`), nunca de sobrevivência de validação anterior.

Então, por campo, e separadamente para cada estado:

- **`nome`, não substancial, in loco autorizada** — preserva `revisada`. Sobre
  `validada`, a RFC **não afirma nada**: exigir ato novo por um rótulo
  corrigido é desproporcional e dispensá-lo é indemonstrado, e nenhuma das
  duas se decide aqui.
- **`FUNDAMENTACAO*`, mesma identidade, veículo autorado** — a cobertura por
  ato anterior **exige nova manifestação ou permanece questão da RFC 0007**.
  Não há terceira saída que esta RFC possa escriturar.
- **alteração substancial** — reabre a análise **independentemente do campo**,
  e aí a regra do rebaixamento explícito acima se aplica inteira.

Deixar a pergunta do ato aberta não custa nada hoje, e é o argumento mais forte
para não fabricar a resposta: as 112 regras estão `importada`, com
`validado_pge`/`validado_presidencia` em `FALSE`, e **nenhum** `AtoValidacao`
foi autorado. Não há um caso real esperando por esta decisão — logo tomá-la por
conveniência de redação seria decidir o mais delicado no momento de menor
informação.

**O que esta RFC deliberadamente não propõe** é a impressão do conteúdo
validado dentro de `atos_validacao`. A forma que ela teria é conhecida — o ato
carregaria a `fingerprint` do frontmatter deployável, e `validada` exigiria
igualdade com a impressão atual, reusando `canonical_json`/`fingerprint` de
`detections.py` — mas o objeto sobre o qual a autoridade se pronuncia é o
**conjunto**, não a regra isolada (RFC 0006 §0: "validação é ato de autoridade
sobre um lote"), e a RFC 0007 é a dona desse gate. Fixar a impressão na regra
agora seria construir no lugar errado o campo que um desenho por lote
realocaria.

## 6. Alternativas descartadas

- **`alteracoes_autoradas` como campo do `regra-*.md`** — §4: duplica
  `disposicao_de_achados` e `UnidadeAuditada.decisoes`, e a única parte não
  duplicada ("quais campos mudaram") é a que nenhum gate confere contra o diff.
- **Chamar a fronteira de "material"** — §2: colide com a chave material do P2
  exatamente sobre `nome` e `FUNDAMENTACAO*`, e nos dois sentidos opostos.
- **Derivar a fronteira do próprio P2** — a chave material responde à pergunta
  sincrônica (duas regras são iguais?), não à diacrônica (esta regra continua a
  mesma?). Reusá-la faria toda correção de fundamentação contar como mudança de
  identidade, o que é precisamente o que a §1 nega.
- **Versionar dentro do `id`** (`regra-0078-v2`) — quebra `_validate_identity`,
  a cardinalidade congelada e a proveniência da importação, e reintroduz a
  restrição que a RFC 0004 §1.2 revogou ao dar identidade própria à unidade
  auditada.
- **Guardar estados intermediários em `data/`** — `data/raw/` é imutável para
  sempre e `data/regras-sisprev.csv` é derivado e descartável; nenhum dos dois
  é registro consultável. O objeto para isso é o conjunto (RFC 0006).
- **Proibir toda edição de campo deployável no bundle legado** — seria coerente
  com os dois precedentes da §3.3 e é a direção provável, mas hoje travaria a
  auditoria: a via da substituição só está autorável (`proposto`/`inativo`), e
  ativá-la depende do gate da RFC 0007. Fica como questão aberta, não como
  decisão.

## 7. Fases

- **Fase 0 (esta RFC)** — a declaração. A §1, a fronteira da §3 e a matriz da
  §3.4 entram em [`docs/spec/regra.md`](../spec/regra.md), que é o contrato; o
  `CLAUDE.md` ganha o ponteiro. Nenhum campo, nenhum gate, nenhuma regra
  editada, nenhuma célula do CSV derivado alterada. **Ordem de entrada**: a #61
  primeiro, para que a §5 cite o vocabulário e o efeito já vigentes em vez de
  prometidos — esta RFC não depende dela para ser lida, mas depende dela para
  estar literalmente correta sobre o que `encaminhada` libera.
- **Fase 1 (não desta RFC)** — a impressão do conteúdo validado, no objeto por
  lote, quando a RFC 0007 definir o ato que autoriza produção. É o que torna a
  invariante do `validada` verificável em vez de escrita.
- **Fase 2 (talvez nunca)** — proibir edição de campo deployável no bundle
  legado, se e quando a via da substituição estiver ativável na prática.

## 8. Questões abertas

- **Q3/Q6 são pré-requisito do teste da §2.** Enquanto só `sexo` está
  confirmada como critério aferido, "afere os mesmos critérios" não se decide
  campo a campo, e a fronteira da §3.2 vale por presunção. Cada resposta de Q3
  ou Q6 move uma linha daquela tabela de "presumida" para "decidida".
- **Alteração que apenas *estreita* a população** (uma janela que passa a
  excluir casos que antes alcançava) é substancial pelo teste — mas é também o
  caso em que a correção de um erro de digitação e a mudança de mérito têm o
  mesmo diff. Se a distinção precisa de forma própria, não se sabe ainda.
- **`simulavel: N` e a fundamentação como critério** — a §3.2 deriva da spec
  que nessas regras a fundamentação é o critério de seleção. Se isso deve
  virar presunção invertida (fundamentação presumidamente substancial quando
  `simulavel: N`) depende de Q3, e a RFC não fixa.
- **Um ato anterior cobre a redação corrigida depois dele?** Não está
  demonstrado, para nenhum campo, e a RFC deliberadamente não decide (§5). As
  duas saídas escrituráveis são exigir nova manifestação ou deixar a cobertura
  como questão da RFC 0007; a terceira — presumir cobertura porque a alteração
  não foi substancial — foi afirmada numa versão anterior desta RFC e retirada,
  porque a fundamentação corrigida muda o fundamento impresso no ato
  administrativo mesmo sem mudar critério nem efeito. Nenhum caso real espera
  por isto: as 112 estão `importada` e nenhum `AtoValidacao` foi autorado.
- **Onde a impressão do conteúdo validado mora** — no ato, no conjunto, ou nos
  dois. É a Fase 1, e é da RFC 0007.
