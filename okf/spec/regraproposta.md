---
type: Especificacao
id: regraproposta
nome: RegraProposta
---

# Regra proposta

> **Minuta.** Escrita a partir do contrato que já vigora no
> `site/src/content.config.ts` e da prática do repositório, para que o tipo
> deixe de existir sem documento. O que ela afirma é descrição do que há, não
> decisão nova — onde estiver errada, quem corrige é a coordenação.
>
> **Emenda (RFC 0004, round 11).** `Conjunto` e o "grupo de substituição"
> foram eliminados como entidades canônicas — ver `okf/spec/conjunto.md`
> (retirado). O que o grupo registrava (quais destinos compartilham origem,
> se a substituição é segura) é hoje **derivado** dos campos diretos desta
> ficha, não declarado à parte. `estado_proposta` foi renomeado
> `estado_auditoria`, e o valor `deployable` renomeado `concluida`, porque
> "deployable" carregava confusão residual entre derivação jurídica e
> prontidão técnica — exatamente o que este documento já existia para
> desfazer.

Uma **RegraProposta** é a regra corrigida: uma regra inteira, com nome,
parâmetros e fundamentação próprios, pronta para ocupar uma linha do Sisprev.

Ela vive num espaço de identidade próprio, fora da numeração do catálogo
recebido, porque o `regra-NNNN` é a linha que o sistema tem hoje — e corrigir
frequentemente **muda o número de regras**.

## Campos

| campo                                   | o que é                                                     |
| --------------------------------------- | ----------------------------------------------------------- |
| `id`                                    | casa com o nome do arquivo                                  |
| `ciclo`                                 | o `Ciclo` responsável pela revisão desta unidade            |
| `estado_auditoria`                      | `elaboracao`, `preview` ou `concluida`                      |
| `estado_implantacao`                    | opcional; `confirmada` ou `pendente_mapeamento_sisprev`     |
| `origens_legacy`                        | de que regras cadastradas ela descende                      |
| `predicados`                            | o que a unidade afirma sobre o caso, em vocabulário fechado |
| `requisitos_verificacao_humana`         | o que se afere, por quem, com que prova                     |
| `aplicabilidade_temporal.datas_legadas` | as quatro colunas de data                                   |
| `taxonomias`                            | os dispositivos articulados, com o papel de cada um         |
| `projecao`                              | as demais colunas do Sisprev, do jeito que entrariam        |
| `proveniencia`                          | fontes consultadas e notas                                  |
| `decisoes`                              | o registro datado de cada escolha, com autor                |
| `confianca`                             | o quanto a autoria se compromete com a unidade              |

## Por que as colunas moram em dois lugares

`projecao` traz a maioria e `aplicabilidade_temporal.datas_legadas` traz as de
data. Quem lê as colunas do Sisprev tem de reunir as duas: uma projeção sem as
janelas não permite conferir qual regra alcança um requerimento.

## `estado_auditoria` não é o mesmo que pronto para o Sisprev

`concluida` afirma que a **derivação é a que a lei exige**: dispositivo,
requisitos, fórmula e representação estão determinados, e a unidade está
pronta para o catálogo auditado. Não afirma, por si só, que a coluna
`projecao.tipo_calculo` (ou outra coluna de vocabulário fechado) já identifica
univocamente essa fórmula no Sisprev em produção — essa é uma afirmação
diferente, sobre o sistema, não sobre a lei.

`estado_implantacao` carrega essa segunda afirmação, só quando ela precisa
ser feita separadamente da primeira. Ausente, presume-se `confirmada` — o caso
comum, em que o valor gravado já é aceito pelo Sisprev sem dúvida material.
`pendente_mapeamento_sisprev` diz que a fórmula está determinada, mas o valor
ou mecanismo que a identifica univocamente no Sisprev ainda depende de
confirmação do IPERON/fornecedor — sem reabrir a derivação jurídica.

## Atomicidade é derivada, não declarada

Uma origem legada às vezes é substituída por mais de um destino, e um destino
às vezes descende de mais de uma origem — `origens_legacy` é a única fonte
dessa relação. `scripts/derivar.py` computa, a partir de todas as unidades do
mesmo `ciclo`, os **componentes conexos** do grafo origem↔destino: duas
unidades pertencem ao mesmo componente quando compartilham, direta ou
transitivamente, ao menos uma origem legada. Um componente só entra na carga
de implantação quando **todos** os seus membros têm `estado_auditoria: concluida` **e** `estado_implantacao: confirmada` — porque a troca de fonte
operacional é atômica, e um componente cujas origens cobrem, juntas, mais de
uma hipótese não admite substituição parcial sem deixar hipótese sem
representação ou representada duas vezes.

Uma unidade `concluida` com `estado_implantacao: pendente_mapeamento_sisprev`
não impede a auditoria de considerar a regra concluída, nem o ciclo de
considerar a derivação encerrada — impede apenas a entrada do componente
inteiro na carga de implantação, e o diagnóstico de `derivar.py` aponta qual
membro do componente ainda não está pronto.

**Limitação conhecida.** O grafo captura só atomicidade que decorre de
origem compartilhada. Há pelo menos um caso no catálogo — as seis unidades
`servidor-com-deficiencia-{leve,moderada,grave}-{feminino,masculino}`,
cada uma com origem própria e exclusiva (`regra-0059` a `regra-0064`) — em
que a coordenação decidiu que a ativação deve ser conjunta por razão
jurídica (as seis só distinguem operacionalmente umas das outras se
existirem juntas; ativar uma só reproduziria a indistinção que a
decomposição existe para resolver), sem que as origens se sobreponham. O
grafo não computa essa atomicidade — cada uma forma um componente próprio
— e, enquanto isso não se resolver, a decisão de ativar as seis juntas
continua sendo verificação não programática da coordenação, registrada
nos `decisoes` de cada uma, não gate automático de `derivar.py`.

## O que a unidade não decide

**Não se ativa sozinha.** `concluida` diz que a auditoria a considera pronta;
o que a põe na carga de implantação é o componente inteiro do grafo
origem↔destino estar pronto, calculado a cada execução de `derivar.py` — não
um ato de ativação declarado à parte.

**Não inventa valor de domínio fechado.** Onde a coluna do Sisprev tem
vocabulário do produto, a unidade grava o que o sistema já admite — tipicamente
o que a regra de origem grava. `estado_implantacao: pendente_mapeamento_sisprev`
existe exatamente para os casos em que esse "o que o sistema já admite" não
identifica, sozinho, a fórmula com precisão suficiente.

## Revogação sem substituta

Quando uma origem legada é revogada sem que exista hipótese material válida a
preservar, não há `RegraProposta` de destino a criar — o registro pertence à
própria `Regra` de origem, num bloco `revogada` (`okf/spec/regra.md`), não a
esta ficha.
