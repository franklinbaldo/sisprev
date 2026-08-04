# Conferência de conformidade — Ciclo 1

> **Documento de conferência, gerado por IA.** Registra a medição feita em
> 2026-08-04. **Não é fonte normativa, não decide
> mérito jurídico e não altera regra, achado ou dado.** Confere o estado
> gravado no bundle contra as onze condições cumulativas de
> [`okf/spec/ciclo.md`](../../okf/spec/ciclo.md), que são condições de
> auditoria. Onde a conferência é humana, o documento diz que é — e não a
> substitui por um verde.

## O que foi conferido, e como

O objeto é o [`ciclo-01`](../../okf/regras-sisprev/ciclos/ciclo-01.md), que se
declara com auditoria jurídica concluída, e a composição
[`ciclo-01-s6-fechamento`](../../okf/conjuntos/ciclo-01-s6-fechamento.md), que
declara as onze condições cumpridas **no escopo recortado**.

A conferência percorreu a cadeia de `base` dos conjuntos, os grupos de
substituição e seus destinos, o `estado_proposta` de cada unidade **e o corpo
dela**, a disposição de achados nas regras de origem e a integridade dos
artefatos derivados. O que está escrito em prosa foi lido; o que está em campo
foi comparado; e os dois foram cotejados um contra o outro, que é onde a
condição 9 cai.

Duas divergências que a primeira versão deste documento apenas registrava foram
corrigidas na fonte no mesmo commit: o rótulo do ciclo (A1) e a passagem da spec
que nomeava o ciclo sucessor errado (A3-bis). Nenhuma das duas exigia decisão
jurídica nova — eram contrato fora de sincronia com decisão já gravada.

## Condição a condição

| #   | condição                                                        | estado                                                    |
| --- | --------------------------------------------------------------- | --------------------------------------------------------- |
| 01  | nenhuma regra sabidamente errada permanece ativa                | conforme — grupos ativos, origens fora da composição (A3) |
| 02  | toda desativada com substituta ou `sem substituta` fundamentada | conforme                                                  |
| 03  | combinações relevantes cobertas por regras ativas               | conforme no escopo do ciclo — ver A1                      |
| 04  | lacuna preexistente preenchida por regra com ID próprio         | conforme — nenhuma demonstrada no escopo                  |
| 05  | sem lacunas de cobertura                                        | conforme no escopo do ciclo — ver A1                      |
| 06  | sem sobreposição não intencional                                | conferência humana, declarada na S5                       |
| 07  | sobreposição intencional justificada                            | conforme — precedência dos Blocos B e C escrita (T8)      |
| 08  | mapa `desativada → substituta(s)` completo                      | conforme                                                  |
| 09  | sem pendência aberta que afete cobertura material               | **não demonstrada** — ver A7, A8 e A9                     |
| 10  | cenários demonstram a seleção esperada                          | conforme por conferência humana — ver A4                  |
| 11  | derivados, validadores e gates íntegros                         | conforme                                                  |

O que sustenta as linhas conformes:

- a cadeia `ciclo-01-s6-fechamento → s3-reabertura-calculo → s5-consistencia → s4-bloco-c → s3-bloco-b → s2-bloco-a → catalogo-legado` resolve sem grupo
  declarado duas vezes;
- os dois grupos do Bloco C estão `ativo`, cada um com `decisao_completude`
  completa — quem decidiu, quando, com justificativa e com fonte no texto
  transcrito;
- todos os destinos declarados existem em disco, e todos os do Bloco C estão em
  `deployable`;
- cada uma das quatro origens do Bloco C dispõe de **todos** os achados abertos
  que a nomeiam, incluindo os bloqueantes `achado-0024` e `achado-0050`. A
  afirmação que a S6 faz sobre isso confere;
- nenhuma regra do catálogo é proprietária de dois ciclos, e nenhuma ficou sem
  ciclo proprietário;
- `derivar.py` não produz diferença sobre o que está comitado, e os dois gates
  de spec passam.

A conferência da condição 10 é humana, como a da 6: os cenários em prosa **são**
o artefato que a spec pede, e a leitura contra fronteiras e precedência não achou
contradição. A ausência de ligação mecânica é oportunidade, não descumprimento.

A condição 9 é a que não se demonstra, e ela não cai sozinha: A7, A8 e A9 são
defeitos das unidades que a composição declara prontas. A1 e A3-bis, que a
primeira versão deste documento registrava como pontos abertos, foram corrigidas
na fonte — `ciclo-01.md` e `okf/spec/ciclo.md` — e ficam abaixo só como registro
do que foi corrigido e por quê.

## Achados de conformidade

Os de A1 a A7 são divergências entre o que o ciclo afirma e o que o dado grava,
ou pontos em que a afirmação não é conferível. A8 e A9 são de outra ordem: são
defeitos nas próprias unidades ativas, apontados na review de 2026-08-04 e
confirmados aqui contra os arquivos.

### A1 — O rótulo do ciclo era mais largo que a propriedade que ele grava

**Corrigido na fonte.** `nome`, título e `Objetivo` do `ciclo-01.md` passaram a
dizer o recorte que a propriedade já expressava, e o `Objetivo` agora nomeia o
Ciclo 9 como dono das janelas anteriores.

O recorte **está** no dado estruturado. A spec define `regras` como as regras
proprietárias e `referencias` como as consultadas que continuam de outro ciclo,
e o `ciclo-01` grava exatamente isso: só `regra-0019` a `regra-0022` em
`regras`, as históricas em `referencias`, e as sete origens dos Blocos A e B
pertencendo ao `ciclo-09`. Quem lê o frontmatter lê o recorte.

O que divergia era o rótulo. O ciclo se chamava **"Incapacidade e invalidez —
continuidade histórica"** e o `Objetivo` falava em "todas as hipóteses de
invalidez e incapacidade permanente pertencentes ao escopo" — leitura mais larga
do que a propriedade sustenta, e é o `nome` que o site lista. Era inconsistência
editorial entre rótulo e propriedade, não ausência do recorte, e por isso a
correção coube aqui: os nomes de `ciclo-01-s2-bloco-a` e `ciclo-01-s3-bloco-b`
envelheceram do mesmo jeito quando o escopo mudou, e a S6 já reconhecia isso.

### A2 — O encerramento tem sinal estruturado, mas não tem estado nem data

O `conjunto` é o sinal: a spec o define como a composição em que o ciclo fecha,
e o schema o declara opcional "porque só o ciclo fechado tem composição". Uma
listagem ou um gate distingue presente de ausente sem ler prosa — e hoje
distingue: o `ciclo-01` grava `ciclo-01-s6-fechamento`, e o `ciclo-02` e o
`ciclo-09` não gravam nada.

O que falta é mais fino. Não há estado explícito que separe "auditoria concluída"
de "aguardando ato", nem **data de fechamento** — o `data` gravado é o de
abertura, e o par dele mora em prosa, junto com as caixas marcadas do fluxo
processual. Um `conjunto` presente prova que existe composição de fechamento,
não que as onze condições foram conferidas.

Nota de escopo: o registro aqui é do fato. Se isso pede campo novo é decisão da
coordenação, e o critério do repositório para guarda nova — caso concreto que já
tenha acontecido — vale igual aqui.

### A3 — Por que a condição 1 se sustenta, e onde ela simplesmente não se aplica

`regra-0001`, `regra-0002`, `regra-0004`, `regra-0006`, `regra-0007`,
`regra-0008` e `regra-0009` permanecem na composição proposta, porque os três
grupos dos Blocos A e B estão `inativo`. Quatro delas são nomeadas por achados
**bloqueantes** abertos (`achado-0022`, `achado-0049`) — e os dispõem.

A razão de conformidade é a que a spec dá, e são duas, distintas:

- **no Bloco C**, a condição 1 está cumprida porque os dois grupos estão
  `ativo`, com decisão de completude, e as quatro origens saíram da composição
  proposta. É esse o ato de auditoria que a spec exige;
- **nos Blocos A e B**, a condição não se aplica a este ciclo porque as sete
  origens estão fora do escopo e da propriedade dele — são `referencias`, e
  pertencem ao `ciclo-09`.

O que **não** sustenta conformidade, e a spec o diz expressamente: a composição
ser `proposto` e o `catalogo-legado` seguir vigente. O ato institucional não é
condição de encerramento, e portanto também não é justificativa de cumprimento.

### A3-bis — A spec mandava para o Ciclo 2 o que o repositório deu ao Ciclo 9

**Corrigido na fonte.** Em "Aplicação ao Ciclo 1", `okf/spec/ciclo.md` dizia que
as hipóteses históricas tinham sido deslocadas para "o ciclo seguinte" e que "o
Ciclo 2 os promove". As sete origens estão no `ciclo-09` — "Janelas históricas
de invalidez" —, e o `ciclo-02` é "Pensão por morte e benefícios derivados" e
não as lista. A passagem passou a nomear o Ciclo 9.

Não havia decisão jurídica nova a tomar: a propriedade já estava gravada, e o
que faltava era o contrato dizer o mesmo que o dado. É a regra da casa — quando
a spec e o código divergem, o código ganha, e a divergência é ela própria
defeito a corrigir na spec.

### A4 — A condição 10 se cumpre por leitura, e é assim que a spec a pede

Os dezesseis cenários existem, estão no conjunto de fechamento e demonstram
fronteira e precedência lendo-se um a um. São o artefato que a condição exige,
e a conferência deles é humana — como a da condição 6. Nada os liga
mecanicamente às unidades que eles dizem selecionar, e isso é oportunidade
futura, não descumprimento.

O piloto em
[`piloto-selecao-invalidez-incapacidade.md`](piloto-selecao-invalidez-incapacidade.md)
**não serve** como essa prova: usa outro corpus, roda o modelo da RFC 0002 à
mão e se declara não oficial no próprio cabeçalho.

Conferi os cenários contra as fronteiras do T2 e não achei contradição — 02 e
04 caem do lado certo das fronteiras exclusivas, e 11 a 14 respeitam a
precedência do T8. É conferência de leitura, e vale o que vale.

### A5 — Achados informativos abertos sem disposição nas regras de referência

Não afetam a cobertura material, e por isso não obstam a condição 9. Ficam
listados porque são trabalho que o Ciclo 9 herda junto com as regras:

- `regra-0001`: `achado-0015`;
- `regra-0002`: `achado-0009`, `achado-0015`;
- `regra-0003`: `achado-0008`, `achado-0015`;
- `regra-0004` e `regra-0005`: `achado-0008`;
- `regra-0006` e `regra-0007`: `achado-0025`, `achado-0026`, `achado-0060`;
- `regra-0008` e `regra-0009`: `achado-0025`, `achado-0026`.

`regra-0003` e `regra-0005` são referências do Ciclo 1 mas proprietárias do
Ciclo 2 — a disposição delas é lá, não aqui.

### A7 — As quarenta unidades estão `deployable` com pendência aberta no corpo

Esta é a única condição que não se demonstra, e ela não se resolve escrevendo.

Conferir `estado_proposta` não basta: o campo diz `deployable` nas quarenta
unidades do Bloco C, e o corpo de **todas as quarenta** ainda traz, em
"Pendências localizadas", a caixa aberta *"concluir a conferência humana desta
regra"*. Junto dela aparecem, distribuídas pelo grupo, *"confirmar a fórmula de
cálculo"*, *"confirmar a projeção operacional"* e *"definir o protocolo
institucional de reconhecimento do nexo profissional"*.

As pendências do grupo não são todas da mesma natureza, e a diferença decide:

- **dependência externa** — *"confirmar que o Sisprev captura e classifica a
  causa"*, *"confirmar o fluxo operacional pelo qual o diagnóstico é cotejado
  com o inciso"*, a opção do § 16 do art. 40 sem campo no cadastro. A spec
  admite que uma dependência externa permaneça registrada, e a S6 já as declara
  como pendentes sem impedir o ato. Estas não obstam;
- **conferência de auditoria** — *"concluir a conferência humana desta regra"*,
  *"confirmar a fórmula de cálculo"*, *"confirmar a projeção operacional"*.
  Estas são trabalho da própria auditoria, e é sobre elas que a condição 9 fala.

Enquanto a caixa da conferência humana estiver aberta em todas as unidades
ativas, "sem pendência aberta" é afirmação que o documento faz e o corpo
contradiz. Há duas saídas, e nenhuma é deste relatório: concluir as conferências
e fechar as caixas com a evidência escrita, ou reconhecer que `deployable` foi
gravado antes do que ele significa. Quem faz qualquer uma das duas é o auditor.

### A8 — As quatro regras do magistério não modelam o requisito do magistério

**Bloqueante.** O inciso XVI do § 8º do art. 30 restringe surdez permanente e
anomalia da fala ao **caso de magistério**. Nas quatro unidades correspondentes,
essa restrição aparece no `nome` e na fundamentação narrativa, e **não** no que
seleciona: `predicados` grava apenas `causa_incapacidade: doenca_catalogada` e o
regime, e o `protocolo_verificacao` pergunta pelo diagnóstico e pela
posterioridade à filiação ao RPPS — nada sobre o cargo ocupado, nem meio de prova
dos assentamentos funcionais quanto ao magistério.

Como está modelado, o protocolo enquadra servidor que não integra o magistério.
O defeito é das unidades, não da matriz: a matriz separa as duas hipóteses
corretamente, e o que falta é o requisito descer do nome para o campo.

### A9 — As duas unidades de causa comum se contradizem no `tipo_calculo`

**Bloqueante.** Ambas projetam `tipo_calculo: Proporcionalidade Dias`, e ambas
trazem no corpo a nota de que **`Não identificado`** evitaria projetar a fórmula
composta como mera proporcionalidade em dias. A nota não está escrita como
histórico: descreve como vigente uma projeção diferente da que o frontmatter
grava.

Some-se a isso que o checklist da mesma unidade ainda manda "confirmar a fórmula
de cálculo que representa a média proporcional em dias" — a decisão que a
contradição depende para se resolver.

### A10 — O documento do grupo tinha dois estados opostos

**Corrigido na sinalização, não no mérito.** O frontmatter de
`ciclo-01-s4-bloco-c` traz vinte destinos por coorte, grupos `ativo` e decisões
de completude; o corpo dizia "oito unidades", grupos `inativo` e unidades em
`elaboracao`, com a lista do que era obrigatório antes de ativar.

O corpo é o registro da sessão S4 e passou a dizer isso no cabeçalho, com a
regra de precedência explícita. O que a sinalização **não** resolve: dois itens
daquela lista — resolver Q6-S/Q6-T e completar o gate humano das unidades —
continuam abertos no corpo das unidades ativas, o que é exatamente o A7.

### A11 — A planilha de homologação do ciclo está órfã e divergente

`data/homologacao/ciclo-01-s6-fechamento.csv` exporta as quarenta unidades com
`TIPO DE BENEFICIO = APOSENTADORIA POR INVALIDEZ` e `DEPLOYABLE = N`. As
unidades em disco projetam `APOSENTADORIA POR INCAPACIDADE PERMANENTE` e estão
`deployable`.

Não é divergência que `derivar.py` conserte: o `CSV_DE_HOMOLOGACAO` do script
aponta para `data/regras-propostas.csv`, e nada regenera `data/homologacao/`.
São artefatos derivados de um layout anterior, que ninguém reescreve e que
seguem parecendo dado bom — o modo de falha que o `CLAUDE.md` nomeia. Ou voltam
a ser gerados, ou saem do repositório; qual das duas é decisão de quem os
publica.

### A6 — `ciclo_de_validacao` não é o ciclo de auditoria

A coluna legada `ciclo_de_validacao` grava `1º` em todas as regras do catálogo.
É valor da importação, não vínculo com o `ciclo-01`. Lida como se fosse, ela
declara o catálogo inteiro pertencente ao Ciclo 1 — que é o oposto do que os
nove documentos de ciclo dizem. A propriedade está no `regras:` de cada ciclo,
e só lá.

## Onde o Ciclo 1 está

As condições de estrutura estão cumpridas, e a matriz jurídica geral está
avançada: a cobertura, o mapa de substituição, a precedência entre blocos e os
cenários se sustentam. As duas divergências de contrato foram corrigidas na
fonte, e a trilha de fechamento passou a registrar a PR #102 como o ato que
fechou a auditoria, separada dos campos institucionais que seguem vazios porque
o ato do IPERON é posterior.

**As quarenta unidades ativas não podem ser tratadas como integralmente
conferidas.** Não é só a condição 9: além da conferência humana aberta em todas
elas (A7), há **quatro unidades com requisito jurídico incompletamente
modelado** — o magistério que só existe no nome (A8) — e **duas com contradição
interna direta** sobre a fórmula que projetam (A9). Uma delas seleciona errado
como está escrita; as outras duas projetam para o Sisprev um rótulo que o
próprio documento diz não representar o cálculo.

Isso desloca o que falta: não é a formalidade de fechar caixas, é conferência de
mérito unidade a unidade, e ela produz correção de campo em regra que iria para
produção. Enquanto A7, A8 e A9 não se resolverem, o fechamento declarado está à
frente do que as unidades sustentam.

## O que o Ciclo 9 herda

As sete origens dos Blocos A e B, os três grupos `inativo` — nenhum deles com
`decisao_completude`, que a spec só exige de grupo ativo —, e as vinte e duas
unidades já autoradas, todas em `elaboracao`. A matriz jurídica dessas janelas
não é reaberta; o que falta é autoria, vínculo de forma de cálculo, disposição
de achado e ato.
