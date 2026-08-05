---
type: Especificacao
id: tipocalculo
nome: TipoCalculo
---

# Tipo de cálculo

> **Minuta.** Escrita a partir do contrato que já vigora no
> `site/src/content.config.ts` e da prática do repositório, para que o tipo
> deixe de existir sem documento. O que ela afirma é descrição do que há, não
> decisão nova — onde estiver errada, quem corrige é a coordenação.
>
> **Superada e reescrita (RFC 0004, round 10; achado do Ciclo 1).** A versão
> anterior definia `TipoCalculo` só como "um rótulo do domínio da coluna
> `TIPO_CALCULO` do Sisprev" e mantinha, como conceito canônico paralelo,
> `type: FormaCalculo` para a fórmula jurídica. As duas entidades geravam
> confusão sem servir a uma distinção que o domínio precisasse: o Ciclo 1
> encontrou o mesmo rótulo legado (`Proporcionalidade Dias`) projetando ao
> menos quatro fórmulas juridicamente distintas, e a separação em dois tipos
> paralelos não ajudava a resolver isso — só adiava a pergunta certa. Esta
> revisão funde os dois conceitos.

Um **TipoCalculo** é a fórmula juridicamente fundamentada usada para apurar
o valor inicial de um benefício — base, o que a proporcionaliza, limites e
a fundamentação normativa de cada etapa —, com a sua origem no catálogo
legado do Sisprev, quando houver.

## Critério de identidade

Dados relevantes iguais, submetidos à mesma operação, produzindo o mesmo
resultado, pertencem ao mesmo tipo de cálculo. Mudança material na base, no
método da média, na proporcionalização, nos limites ou na ordem das
operações cria outro tipo — ainda que o valor legado observado no Sisprev
seja o mesmo para os dois.

## Campos

| campo                        | o que é                                                             |
| ---------------------------- | ------------------------------------------------------------------- |
| `id`                         | casa com o nome do arquivo                                          |
| `nome`                       | a fórmula dita numa linha, suficientemente discriminante            |
| `base`                       | a base de cálculo, com os dispositivos que a fundam                 |
| `ajustes`                    | proporcionalizações e demais ajustes, em ordem, com fundamento      |
| `limitadores`                | tetos e demais limites, em ordem, com fundamento                    |
| `origem_legada`              | o(s) valor(es) que o Sisprev grava para esta fórmula, quando houver |
| `autorado_por`/`autorado_em` | quem autorou a decomposição e quando                                |

O corpo é autorado e não tem forma fixa: descreve a fórmula em prosa, além
do que os campos estruturados já capturam.

## `origem_legada` não é a identidade do tipo

`origem_legada.tipo_calculo` é o valor que a coluna `TIPO_CALCULO` do
Sisprev grava para regras que instanciam esta fórmula — quando existir um.
Não é o que identifica o tipo: é a **projeção legada** dele, tipicamente
mais pobre do que a fórmula, porque o enum do Sisprev não tem um membro
próprio para cada combinação jurídica.

Segue-se que **o mesmo valor de `origem_legada.tipo_calculo` pode ser a
origem de vários `TipoCalculo` distintos** — é o caso de `Proporcionalidade Dias`, que nomeia o ajuste em dias sem nunca dizer qual é a base, e por
isso é a origem legada de ao menos quatro fórmulas materialmente
diferentes no catálogo. Isso não é erro de modelagem: é o retrato de um
enum mais pobre que o domínio jurídico que ele tenta representar.

A relação inversa também ocorre: **um `TipoCalculo` pode ter mais de uma
proveniência legada**, quando a consolidação de dois documentos que
descreviam a mesma fórmula (`## Critério de identidade`, acima) herda os
rótulos legados distintos que cada um citava — é o caso de
`tipo-calculo-media-proporcional-dias-lce1100`, que consolidou
`Proporcionalidade Dias` e `Tipo Cálculo Nova Previdência`. Nesse caso,
`origem_legada` é uma lista de objetos, cada um com `tipo_calculo`,
`fidelidade` e `justificativa` próprios, em vez de um único objeto.

`origem_legada.fidelidade` (`parcial` ou `pendente`) e `justificativa`
registram o que se perde nessa projeção — nunca dúvida sobre a fórmula em
si, que os campos `base`/`ajustes`/`limitadores` já fixam por completo.
`fidelidade: parcial` é a condição da maioria dos tipos do catálogo, porque
o enum legado é mais pobre que a fórmula jurídica; `pendente` é reservado
para quando a própria estrutura ainda depende de fonte ou decomposição
adicional — nenhuma das duas reabre a fórmula.

## O que este tipo não decide

**Não inventa valor de domínio fechado.** `origem_legada.tipo_calculo`
grava o que o Sisprev já admite — tipicamente o que a regra de origem
grava. Um `TipoCalculo` sem origem legada correspondente ainda é válido: é
a derivação jurídica correta, apenas ainda sem representação unívoca no
enum atual. Isso é pendência de **implantação**
(`estado_implantacao: pendente_mapeamento_sisprev` na `RegraProposta` que o
usa — `okf/spec/regraproposta.md`), não pendência da fórmula, e não impede
que o ciclo que a derivou seja considerado concluído.

**A tradução para o Sisprev é decisão de implantação, separada.** Se a
tradução final for um novo valor cadastrado, uma combinação de colunas já
existentes (`tipo_calculo` mais `tipo_de_beneficio`, por exemplo), uma
rotina interna já existente, ou uma rotina nova, é decisão do
IPERON/fornecedor — não altera o significado canônico do `TipoCalculo`, e
a ausência de tradução imediata não é razão para não derivar a fórmula
corretamente agora.

**Não é implementação.** Que o sistema efetivamente compute a fórmula
descrita, sob o rótulo que a projeta, é comportamento do programa, não do
catálogo. A auditoria descreve a fórmula que entende aplicável e declara a
premissa de que o rótulo gravado — quando confirmado — é aquele pelo qual o
sistema a executa; confirmar isso é providência do Instituto.

## `tipo-calculo-nao-identificado`

Um documento reservado, sem `base`/`ajustes`/`limitadores` próprios: é o
rótulo usado enquanto a fórmula de uma regra ainda não foi decomposta. Não
deve ser confundido com fórmula desconhecida por natureza, valor nulo, ou
autorização para aproximar por outro tipo.
