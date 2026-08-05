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
>
> **Emenda (RFC 0004, round 12 — Ciclo 1, causa comum).** A carga que
> `scripts/derivar.py` produz (`data/regras-propostas.csv`) é planilha de
> **homologação**, não ativação em produção: existe para que a conferência
> de campo aconteça ao lado do export do Sisprev, e o ato institucional do
> IPERON a sucede, nunca a antecede (`okf/spec/ciclo.md`). Bloquear a
> entrada nessa planilha só se justifica quando não se sabe, sequer, que
> mecanismo do sistema a fórmula ocupa — não quando já há evidência
> operacional concreta de que ocupa algum, e falta apenas confirmar em
> homologação prática um detalhe da execução. `estado_implantacao` ganhou o
> valor `confirmada_com_ressalva` para o segundo caso, com `ressalva_homologacao`
> registrando o que fica para quem homologa.

Uma **RegraProposta** é a regra corrigida: uma regra inteira, com nome,
parâmetros e fundamentação próprios, pronta para ocupar uma linha do Sisprev.

Ela vive num espaço de identidade próprio, fora da numeração do catálogo
recebido, porque o `regra-NNNN` é a linha que o sistema tem hoje — e corrigir
frequentemente **muda o número de regras**.

## Campos

| campo                                   | o que é                                                                                                                |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `id`                                    | casa com o nome do arquivo                                                                                             |
| `ciclo`                                 | o `Ciclo` responsável pela revisão desta unidade                                                                       |
| `estado_auditoria`                      | `elaboracao`, `preview` ou `concluida`                                                                                 |
| `estado_implantacao`                    | opcional; `confirmada`, `confirmada_com_ressalva` ou `pendente_mapeamento_sisprev`                                     |
| `ressalva_homologacao`                  | obrigatório com `confirmada_com_ressalva`; o que a homologação prática precisa confirmar antes da ativação em produção |
| `origens_legacy`                        | de que regras cadastradas ela descende                                                                                 |
| `predicados`                            | o que a unidade afirma sobre o caso, em vocabulário fechado                                                            |
| `predicados.vinculo_rpc`                | opcional; `nao_aderiu` ou `sujeito` — a posição do caso perante o regime de previdência complementar                   |
| `predicados.selecao_por`                | opcional; vias alternativas de alcance de **um** requisito — só se declara onde a alternativa existe (ver abaixo)      |
| `requisitos_verificacao_humana`         | o que se afere, por quem, com que prova                                                                                |
| `aplicabilidade_temporal.datas_legadas` | as quatro colunas de data                                                                                              |
| `taxonomias`                            | os dispositivos articulados, com o papel de cada um                                                                    |
| `projecao`                              | as demais colunas do Sisprev, do jeito que entrariam                                                                   |
| `proveniencia`                          | fontes consultadas e notas                                                                                             |
| `decisoes`                              | o registro datado de cada escolha, com autor                                                                           |
| `confianca`                             | o quanto a autoria se compromete com a unidade                                                                         |

## O regime de previdência complementar é predicado, não prosa

A LCE 1.100/2021 condiciona **três** dos seus dispositivos centrais de cálculo
à posição do servidor perante o regime de previdência complementar, e não
apenas à data de ingresso: o art. 24, *caput* ("após 31 de dezembro de 2003 **e
que não tenham feito a opção** de que trata o § 16 do art. 40 da Constituição
Federal"), o art. 25 (mesma exigência para a coorte até 2003) e o art. 27, I
(paridade "desde que não tenha feito a opção"). Em sentido inverso, o art. 24,
§ 11, sujeita ao teto do RGPS quem **está** sujeito àquele regime, e o § 12
estende o mesmo teto a quem ingressou a partir de 6 de novembro de 2018.

Um critério que a lei põe no *caput* de três artigos não pode viver só no nome
da regra ou na fundamentação: quem seleciona a regra precisa poder conferi-lo
como campo. Daí **`vinculo_rpc`** — `nao_aderiu` (o caso exige a ausência da
opção) ou `sujeito` (o caso a pressupõe, por opção ou por imposição legal).

### Como os campos se combinam na seleção

A seleção de uma `RegraProposta` resulta da **conjugação cumulativa** dos seus
predicados, da aplicabilidade temporal e dos demais requisitos estruturados.
`selecao_por` registra modos de satisfação ou vias de alcance de **um requisito
específico**; seus itens são disjuntivos apenas quando representam alternativas
materiais para o mesmo efeito. A lista **não substitui nem enfraquece** os
demais predicados da regra, e a presença de vários itens não transforma os
requisitos da unidade numa expressão global com `OU`.

Daí a regra prática: `selecao_por` só se declara onde exista via alternativa
real. Onde o requisito é único, ele mora no campo que já o representa — a
janela de ingresso em `aplicabilidade_temporal.datas_legadas`, a posição
perante o regime complementar em `vinculo_rpc` — e repeti-lo na lista não
acrescenta informação: só cria a leitura falsa de que bastaria um deles.

No Bloco C, portanto:

| família                 | condição de seleção                               | `selecao_por` |
| ----------------------- | ------------------------------------------------- | ------------- |
| até 2003 sem RPC        | janela temporal **e** ausência de opção           | ausente       |
| 2004–05/11/2018 sem RPC | janela temporal **e** ausência de opção           | ausente       |
| após 05/11/2018 ou RPC  | ingresso após a implantação **ou** opção expressa | dois itens    |

Vocabulário em uso:

| valor                           | significa                                                                   |
| ------------------------------- | --------------------------------------------------------------------------- |
| `ingresso_apos_implantacao_rpc` | ingresso a partir de 06/11/2018 — sujeição **automática** (art. 24, § 12)   |
| `opcao_expressa_rpc`            | opção prévia e expressa, possível **só até 05/11/2018** (CF, art. 40, § 16) |

**As duas vias não se sobrepõem, e não são simétricas.** A opção do § 16 da
Constituição só cabe "ao servidor que tiver ingressado no serviço público **até
a data da publicação do ato de instituição**" do regime complementar — isto é,
até 05/11/2018. Quem ingressou de 06/11/2018 em diante é sujeito ao regime por
imposição legal, automaticamente: não há opção a fazer, e `opcao_expressa_rpc`
não é hipótese possível para ele. Por isso a disjunção é real mas **repartida
no tempo**: antes da implantação, a opção é o que distingue esta família das
duas primeiras; a partir dela, a data basta sozinha.

**A disjunção existe numa família só.** Nas duas primeiras, a lei exige as
duas coisas ao mesmo tempo — estar na janela **e** não ter optado —, e nenhuma
delas admite via alternativa. É por isso que só a terceira declara
`selecao_por`.

**Por que a disjunção não vira família nova.** O servidor que ingressou antes
de 06/11/2018 e optou pelo regime complementar recebe exatamente o mesmo
tratamento de quem ingressou depois: a mesma base, os mesmos limitadores, o
mesmo reajustamento — o art. 24 os alcança pelos §§ 11 e 12, que convergem no
mesmo resultado. Separá-los em duas unidades criaria duas regras com projeção
idêntica e nenhuma diferença material, que é exatamente o defeito que a
decomposição do catálogo existe para desfazer. A pluralidade fica em
`selecao_por`, onde ela é: no caminho de seleção, não no efeito.

**O que o cadastro ainda não representa.** O catálogo do Sisprev não tem coluna
que registre a opção pelo regime complementar — fato já anotado em
`regra-0109`/`regra-0110`, com decisão pendente do IPERON. Enquanto essa coluna
não existir, a disjunção é verificável no processo administrativo e no
predicado desta ficha, não no cadastro; unidade cuja seleção dependa dela não
pode ser dada como implantada só porque a origem legada existe.

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

Os outros dois valores distinguem **duas pendências diferentes**, e só uma
delas impede a entrada na carga de homologação:

- `pendente_mapeamento_sisprev` diz que não se sabe, sequer, que mecanismo
  do Sisprev a fórmula ocupa — não há evidência operacional de que o
  sistema já execute algo para esta hipótese. Não entra na carga: pô-la na
  planilha ofereceria a quem homologa uma linha sem base para conferir.
- `confirmada_com_ressalva` diz que há evidência operacional concreta de
  que o sistema já executa algum mecanismo para a hipótese — tipicamente
  porque a origem legada (`origens_legacy`) já está em produção com a
  mesma projeção de vocabulário fechado —, e o que falta é confirmar, na
  prática de homologação, um detalhe específico da execução, registrado em
  `ressalva_homologacao`. Entra na carga: a homologação é exatamente onde
  essa conferência de campo acontece, e reter a linha adiaria a única
  verificação capaz de resolvê-la.

Nenhum dos dois reabre a derivação jurídica. A carga de homologação
(`data/regras-propostas.csv`, `scripts/derivar.py`) não é ativação em
produção: é o insumo para a conferência que precede o ato do IPERON.

## Atomicidade é derivada, não declarada

Uma origem legada às vezes é substituída por mais de um destino, e um destino
às vezes descende de mais de uma origem — `origens_legacy` é a única fonte
dessa relação. `scripts/derivar.py` computa, a partir de todas as unidades do
mesmo `ciclo`, os **componentes conexos** do grafo origem↔destino: duas
unidades pertencem ao mesmo componente quando compartilham, direta ou
transitivamente, ao menos uma origem legada. Um componente só entra na carga
de homologação quando **todos** os seus membros têm `estado_auditoria: concluida` **e** `estado_implantacao` em `confirmada` ou `confirmada_com_ressalva`
— porque a troca de fonte operacional é atômica, e um componente cujas
origens cobrem, juntas, mais de uma hipótese não admite substituição parcial
sem deixar hipótese sem representação ou representada duas vezes.

Uma unidade `concluida` com `estado_implantacao: pendente_mapeamento_sisprev`
não impede a auditoria de considerar a regra concluída, nem o ciclo de
considerar a derivação encerrada — impede apenas a entrada do componente
inteiro na carga de homologação, e o diagnóstico de `derivar.py` aponta qual
membro do componente ainda não está pronto. Uma unidade
`confirmada_com_ressalva` entra normalmente, carregando a ressalva na
planilha para quem homologa.

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
