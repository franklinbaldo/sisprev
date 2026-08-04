# Conferência de conformidade — Ciclo 1

> **Documento de conferência, gerado por IA.** Registra a medição feita em
> 2026-08-04 sobre o commit `e86a8e2`. **Não é fonte normativa, não decide
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
substituição e seus destinos, o `estado_proposta` de cada unidade, a disposição
de achados nas regras de origem e a integridade dos artefatos derivados. O que
está escrito em prosa foi lido; o que está em campo foi comparado.

## Condição a condição

| #   | condição                                                        | estado                                                    |
| --- | --------------------------------------------------------------- | --------------------------------------------------------- |
| 01  | nenhuma regra sabidamente errada permanece ativa                | conforme — grupos ativos, origens fora da composição (A3) |
| 02  | toda desativada com substituta ou `sem substituta` fundamentada | conforme                                                  |
| 03  | combinações relevantes cobertas por regras ativas               | conforme no recorte — ver A1                              |
| 04  | lacuna preexistente preenchida por regra com ID próprio         | conforme — nenhuma demonstrada no escopo                  |
| 05  | sem lacunas de cobertura                                        | conforme no recorte — ver A1                              |
| 06  | sem sobreposição não intencional                                | conferência humana, declarada na S5                       |
| 07  | sobreposição intencional justificada                            | conforme — precedência dos Blocos B e C escrita (T8)      |
| 08  | mapa `desativada → substituta(s)` completo                      | conforme                                                  |
| 09  | sem pendência aberta que afete cobertura material               | conforme — ver A5 para o que sobra                        |
| 10  | cenários demonstram a seleção esperada                          | não conferível mecanicamente — ver A4                     |
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

Uma não conformidade fica registrada fora da tabela, porque não é de condição
de fechamento e sim do texto-base: a spec nomeia o Ciclo 2 como sucessor das
janelas históricas, e o dado as dá ao Ciclo 9 (A3-bis).

## Achados de conformidade

Nenhum destes é defeito de mérito jurídico: são divergências entre o que o
ciclo afirma e o que o dado grava, ou pontos em que a afirmação não é
conferível.

### A1 — O rótulo do ciclo é mais largo que a propriedade que ele grava

O recorte **está** no dado estruturado. A spec define `regras` como as regras
proprietárias e `referencias` como as consultadas que continuam de outro ciclo,
e o `ciclo-01` grava exatamente isso: só `regra-0019` a `regra-0022` em
`regras`, as históricas em `referencias`, e as sete origens dos Blocos A e B
pertencendo ao `ciclo-09`. Quem lê o frontmatter lê o recorte.

O que diverge é o rótulo. O ciclo se chama **"Incapacidade e invalidez —
continuidade histórica"** e o `Objetivo` fala em "todas as hipóteses de
invalidez e incapacidade permanente pertencentes ao escopo" — leitura mais larga
do que a propriedade sustenta, e é o `nome` que o site lista. É inconsistência
editorial entre rótulo e propriedade, não ausência do recorte.

Correção possível: `nome` e `Objetivo` passarem a dizer o recorte que a
propriedade já expressa, do mesmo modo como a S6 reconhece que os nomes de
`ciclo-01-s2-bloco-a` e `ciclo-01-s3-bloco-b` envelheceram quando o escopo
mudou.

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

### A3-bis — A spec manda para o Ciclo 2 o que o repositório deu ao Ciclo 9

Em "Aplicação ao Ciclo 1", `okf/spec/ciclo.md` diz que as hipóteses históricas
"foram deslocadas para o ciclo seguinte" e que "**o Ciclo 2 os promove**". O
repositório atribui as sete origens ao `ciclo-09` — "Janelas históricas de
invalidez" —, enquanto o `ciclo-02` é "Pensão por morte e benefícios derivados"
e não as lista.

É não conformidade entre a spec e o dado, e não é editorial: a spec nomeia o
ciclo sucessor, e nomeia o errado. Pelo critério do repositório, o código ganha
e a divergência é ela própria defeito a corrigir na spec — o que exige ato da
coordenação, não deste documento. Enquanto a passagem não for corrigida, o
Ciclo 1 fecha apontando um sucessor que o texto-base contradiz.

### A4 — A condição 10 não tem artefato que a conferisse

Os dezesseis cenários existem, estão no conjunto de fechamento e demonstram
fronteira e precedência lendo-se um a um. Nada os liga mecanicamente às
unidades que eles dizem selecionar: são prosa numerada, conferida por quem
lê.

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

### A6 — `ciclo_de_validacao` não é o ciclo de auditoria

A coluna legada `ciclo_de_validacao` grava `1º` em todas as regras do catálogo.
É valor da importação, não vínculo com o `ciclo-01`. Lida como se fosse, ela
declara o catálogo inteiro pertencente ao Ciclo 1 — que é o oposto do que os
nove documentos de ciclo dizem. A propriedade está no `regras:` de cada ciclo,
e só lá.

## O que o Ciclo 9 herda

As sete origens dos Blocos A e B, os três grupos `inativo` — nenhum deles com
`decisao_completude`, que a spec só exige de grupo ativo —, e as vinte e duas
unidades já autoradas, todas em `elaboracao`. A matriz jurídica dessas janelas
não é reaberta; o que falta é autoria, vínculo de forma de cálculo, disposição
de achado e ato.
