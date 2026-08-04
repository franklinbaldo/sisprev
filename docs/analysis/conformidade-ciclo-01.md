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

| #   | condição                                                        | estado                                               |
| --- | --------------------------------------------------------------- | ---------------------------------------------------- |
| 01  | nenhuma regra sabidamente errada permanece ativa                | conforme no recorte — ver A3                         |
| 02  | toda desativada com substituta ou `sem substituta` fundamentada | conforme                                             |
| 03  | combinações relevantes cobertas por regras ativas               | conforme no recorte — ver A1                         |
| 04  | lacuna preexistente preenchida por regra com ID próprio         | conforme — nenhuma demonstrada no escopo             |
| 05  | sem lacunas de cobertura                                        | conforme no recorte — ver A1                         |
| 06  | sem sobreposição não intencional                                | conferência humana, declarada na S5                  |
| 07  | sobreposição intencional justificada                            | conforme — precedência dos Blocos B e C escrita (T8) |
| 08  | mapa `desativada → substituta(s)` completo                      | conforme                                             |
| 09  | sem pendência aberta que afete cobertura material               | conforme — ver A5 para o que sobra                   |
| 10  | cenários demonstram a seleção esperada                          | não conferível mecanicamente — ver A4                |
| 11  | derivados, validadores e gates íntegros                         | conforme                                             |

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

## Achados de conformidade

Nenhum destes é defeito de mérito jurídico: são divergências entre o que o
ciclo afirma e o que o dado grava, ou pontos em que a afirmação não é
conferível.

### A1 — O recorte do fechamento não está declarado onde o dado está

O ciclo se chama **"Incapacidade e invalidez — continuidade histórica"** e
lista nas `regras` e `referencias` do frontmatter as nove unidades históricas
dos Blocos A e B. O fechamento, porém, vale só para o Bloco C: a
`decisao_completude` da S6 diz expressamente que "fora do escopo ficam os Blocos
A e B (…) a completude aqui declarada não os alcança e não afirma nada sobre
eles".

As condições 3 e 5 falam do **tema auditado**. Quem ler o nome do ciclo lê um
tema que inclui a continuidade histórica; quem ler a composição lê um recorte
que a exclui. A divergência está entre o campo e a prosa, e é o campo que
circula: o site lista o ciclo pelo `nome`.

Correção possível: o recorte passar a estar dito no `nome` e no `Objetivo` do
próprio `ciclo-01.md`, do mesmo modo como a S6 já reconhece que os nomes de
`ciclo-01-s2-bloco-a` e `ciclo-01-s3-bloco-b` envelheceram quando o escopo
mudou.

### A2 — Nada distingue ciclo encerrado de ciclo aberto fora da prosa

O tipo `Ciclo` não tem campo de estado: são `id`, `numero`, `nome`, `data`,
`regras`, `referencias` e `conjunto`. O encerramento do Ciclo 1 vive num bloco
de citação ("Estado: auditoria jurídica concluída") e numa lista de caixas
marcadas.

Consequência: nenhum gate pode conferir que um ciclo declarado encerrado cumpre
as onze condições, e nenhuma listagem pode separar os encerrados dos abertos
sem ler texto corrido. O `data` gravado é o de abertura, e não há o par dele.

Nota de escopo: dizer que isto exige campo novo seria construir estrutura antes
da demanda, que é justamente o que este repositório removeu. O registro aqui é
do fato, não da recomendação de esquema — a decisão é da coordenação.

### A3 — Sete origens com achado aberto seguem na composição

`regra-0001`, `regra-0002`, `regra-0004`, `regra-0006`, `regra-0007`,
`regra-0008` e `regra-0009` permanecem na composição proposta, porque os três
grupos dos Blocos A e B estão `inativo`. Quatro delas são nomeadas por achados
**bloqueantes** abertos (`achado-0022`, `achado-0049`) — e os dispõem, o que
confere.

A condição 1 se sustenta por dois motivos que convém ficarem escritos juntos: a
composição do ciclo é `proposto`, e o catálogo vigente continua sendo
`catalogo-legado`. Ou seja, a leitura correta não é "nenhuma regra errada está
ativa", e sim "nenhuma passa a ativa por ato deste ciclo". O que estiver errado
nas sete continua no catálogo em vigor até o Ciclo 9 e o ato do IPERON.

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
