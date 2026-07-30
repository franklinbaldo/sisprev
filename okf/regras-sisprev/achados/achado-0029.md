---
type: Achado
id: achado-0029
nome: Um único nome cobre as quatro regras 0035-0038, e o que ele omite não é o sexo — é o trilho de cálculo inteiro
situacao: aberto
severidade: informativo
verificacao: hibrida
natureza: modelagem
deteccoes:
  - detector: P1_NOME_REPETIDO
    fingerprint: sha256:444832f876f579b6589fbf0c88c38b84830715040e6ebd6f3e59734b391a7cc5
regras_afetadas:
  - /regras/regra-0035.md
  - /regras/regra-0036.md
  - /regras/regra-0037.md
  - /regras/regra-0038.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

As quatro regras `0035`, `0036`, `0037` e `0038` compartilham o `nome`

> Voluntária por Idade e Tempo de Contrib. - Art. 40, §1º, III da Constituição
> Federal c/c do Art. 32 da LC 1.100/21

e são **duas regras distintas em dois sexos**, não uma em quatro variantes:

| regra  | `sexo`    | trilho citado              | `tipo_calculo`              | `paridade` | `data_adm_ate` |
| ------ | --------- | -------------------------- | --------------------------- | ---------- | -------------- |
| `0035` | MASCULINO | `art-25` + `art-27-inc-i`  | Remuneração de Contribuição | **S**      | 31/12/2003     |
| `0036` | FEMININO  | `art-25` + `art-27-inc-i`  | Remuneração de Contribuição | **S**      | 31/12/2003     |
| `0037` | MASCULINO | `art-24` + `art-27-inc-ii` | **Valor Médio**             | **N**      | 31/12/2099     |
| `0038` | FEMININO  | `art-24` + `art-27-inc-ii` | **Valor Médio**             | **N**      | 31/12/2099     |

O [`achado-0020`](achado-0020.md) já registra o `nome` como problema de
catálogo e mede cinco dimensões de desvio. Este achado registra uma **sexta**,
que aquela medição não alcança: o nome omite o **trilho de cálculo**, que é
critério gravado em coluna e decide o valor do benefício. A D2 do `achado-0020`
mediu a omissão de `sexo`; aqui `sexo` é a menor parte do que falta.

# Evidências

## A metade mecânica

Detecção `P1_NOME_REPETIDO`, fingerprint
`sha256:444832f8…`, agrupando os quatro registros. É um dos 41 grupos do
detector, e o único deste conjunto de doze regras com **mais de duas** regras.

Aplicada aos 41 grupos a pergunta "algum campo de resultado ou de janela
diverge dentro do grupo?", **nove** grupos divergem, e só **três** têm quatro
regras com `paridade` e `tipo_calculo` opostos dentro do mesmo nome:

| grupo                       | achado que o cobre                                                                 |
| --------------------------- | ---------------------------------------------------------------------------------- |
| `0035`/`0036`/`0037`/`0038` | **nenhum, até este**                                                               |
| `0041`/`0042`/`0107`/`0108` | [`achado-0016`](achado-0016.md) — e ali a fundamentação é byte-idêntica nos quatro |
| `0065`/`0066`/`0067`/`0071` | [`achado-0005`](achado-0005.md) cobre `0065`≡`0066`; o grupo de nome não é coberto |

A contagem saiu de consulta *ad hoc* sobre o bundle, não de detector — daí
`verificacao: hibrida` e não `mecanica`: o agrupamento é mecânico e reproduzível
pelo fingerprint, a leitura de **o que** o nome omite é autoral.

## A metade autoral, e é ela que distingue este caso dos outros dois

Nos outros dois grupos de quatro o nome repetido acompanha um **defeito de
mérito**: em `0041`/`0042` × `0107`/`0108` a `fundamentacao_integral` é a mesma
string byte a byte e os campos gravam resultados opostos, de modo que uma das
duas famílias está errada (`achado-0016`). Aqui **não há defeito de mérito no
resultado**: cada par cita o seu trilho e grava o que aquele trilho determina.

Conferido contra a compilação oficial da LCE 1.100/2021
(`fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt`, sha256 `bcac2238…`):

- `art. 25` dá "totalidade da remuneração no cargo efetivo" e `art. 27, I`
  manda reajustar pelo art. 7º da EC 41/2003 → `0035`/`0036` gravam
  `Remuneração de Contribuição` e `paridade: S`. **Fecha.**
- `art. 24` dá "média aritmética simples das maiores remunerações [...] 80%" e
  `art. 27, II` manda reajustar "nos termos estabelecidos para o RGPS" →
  `0037`/`0038` gravam `Valor Médio` e `paridade: N`. **Fecha.**

E as fundamentações **também** divergem: a de `0035`/`0036` diz "cálculo por
integralidade" e "com paridade" e nomeia os arts. 25 e 27, I; a de
`0037`/`0038` diz "cálculo por média" e "sem paridade" e nomeia os arts. 24 e
27, II. Não é o caso de duas famílias com um texto só.

Logo, ao contrário dos outros dois grupos, aqui **renomear é a correção
inteira** — não há grupo `P2_IGUALDADE_MATERIAL_ATIVA` escondido atrás do nome
nem contradição de campo a resolver primeiro. É a exceção à ordem de atos que o
`achado-0020` recomenda ("fundamentação primeiro, nome depois"): a advertência
existe porque renomear costuma apagar o sintoma e deixar a igualdade material
intacta, e aqui não há igualdade material a mascarar.

# Consequência prática

As quatro são `simulavel: S`, e o simulador não lê fundamentação. Um servidor
admitido antes de 2004 satisfaz a janela de admissão de todas as quatro
([`achado-0028`](achado-0028.md)), e os dois registros do seu sexo chegam a ele
com **o mesmo rótulo** e resultados opostos — totalidade da remuneração com
paridade, ou média de 80% sem paridade. Segundo
[`docs/spec/regra.md`](../../../docs/spec/regra.md), o nome deve ser "a menor
descrição, em linguagem humana, capaz de distinguir a regra das demais que
ainda podem ser aplicáveis depois da anamnese do requerente"; aqui ele não
distingue nem a coorte de ingresso nem o cálculo nem a paridade.

Há um agravante próprio deste grupo: o nome cita **`Art. 32 da LC 1.100/21`**,
que é o artigo dos **requisitos** — comum às quatro — e não cita nenhum dos
quatro artigos de cálculo, que são o que as separa. O único fundamento nomeado
é justamente o que elas têm em comum.

`nome` é campo **deployável**, e o `achado-0020` §4 registra onde a proposta
deve morar: no catálogo auditado (RFC 0004), não numa edição de `regra-*.md`.
Nada aqui é corrigido no bundle legado.

# Questão a investigar

1. **Se o nome deve nomear o trilho ou a coorte de ingresso.** As duas são
   formas de dizer a mesma coisa, e a spec pede o fato conhecido **após a
   anamnese**: a data de ingresso é fato que o requerente traz; "cálculo por
   integralidade" é consequência. Isso sugere nomear pela coorte ("ingresso até
   31/12/2003" × "ingresso após 31/12/2003"), o que tem o efeito lateral de
   tornar visível a ausência de corte que o [`achado-0028`](achado-0028.md)
   registra — o nome não conseguiria ser escrito para `0037`/`0038` sem
   escolher a coorte que o cadastro não grava.

2. **Se `sexo` também entra no nome.** É a D2 do `achado-0020`, e alcança 72
   regras; não é decisão deste grupo. Registro apenas que resolver o trilho
   reduz o grupo de quatro para dois pares, e cada par continua com nome
   repetido — os dois problemas são independentes e nenhum dos dois é
   suficiente.

3. **Se o grupo `0065`/`0066`/`0067`/`0071` tem a mesma leitura.** É o terceiro
   grupo de quatro da tabela acima, está fora do conjunto deste achado, e a
   conferência do lote registra que ali o trilho e a janela **não** fecham
   (`regra-0071` grava o corte invertido). Se lá o nome também for a correção
   inteira ou se houver defeito de mérito antes, é conferência de quem o
   auditar.

# Como a população respondeu

As quatro regras alcançadas responderam `corrigida`: `regra-0035` a `regra-0038` receberam nomes distintos pelo padrão de facetas, e a detecção `P1_NOME_REPETIDO` sobre elas deixou de ser emitida.

**O achado permanece `aberto`.** Sob o modelo de estados do catálogo, um defeito real não se fecha por selo no próprio achado: quem responde é a regra, em `disposicao_de_achados`, e é ali que o tratamento fica registrado com autor e data. `improcedente` afirmaria que a acusação nunca procedeu, o que seria falso — o defeito existiu e foi corrigido.

As quatro regras receberam nome pelo padrão de facetas adotado para o catálogo,
e o `P1_NOME_REPETIDO` sobre elas deixou de ser emitido:

| regra        | `nome`                                                                          |
| ------------ | ------------------------------------------------------------------------------- |
| `regra-0035` | Voluntária · ingresso até 31/12/2003, pedido a partir de 18/10/2021 · Masculino |
| `regra-0036` | Voluntária · ingresso até 31/12/2003, pedido a partir de 18/10/2021 · Feminino  |
| `regra-0037` | Voluntária · pedido a partir de 18/10/2021 · Masculino                          |
| `regra-0038` | Voluntária · pedido a partir de 18/10/2021 · Feminino                           |

**A questão 1 deste achado foi respondida pelo padrão, e na direção que ela
apontava.** Ela perguntava se o nome deveria distinguir pelo trilho de cálculo
(`Remuneração de Contribuição` × `Valor Médio`) ou pela coorte de ingresso, e
argumentava pela coorte, porque a data de ingresso é fato que o requerente traz
à anamnese enquanto o trilho é consequência. O padrão adotado nomeia por
critério aferido e mantém campo de resultado fora do nome, que é a mesma
conclusão obtida por via geral.

**O efeito lateral previsto se confirmou.** O achado registrava que nomear pela
coorte tornaria visível a ausência de corte do
[`achado-0028`](achado-0028.md): `regra-0037` e `regra-0038` gravam sentinela em
`data_adm_ate`, então o nome delas simplesmente **não tem** a faceta de ingresso
que as irmãs têm. A ausência agora se lê na lista, em vez de ficar escondida
atrás de um nome compartilhado. O `achado-0028` segue aberto e é onde essa
lacuna se resolve — este achado não a resolve nem a agrava.

**A questão 2 também foi decidida por via geral:** `sexo` entra no nome, como
faceta final, em toda regra que grave valor. Era a D2 do
[`achado-0020`](achado-0020.md), e alcançava muito mais que estas quatro.

**A questão 3 permanece com quem auditar aquele grupo.** `regra-0065`,
`regra-0066`, `regra-0067` e `regra-0071` também receberam nome pelo padrão, o
que dissolve o `P1` sobre elas — mas a conferência de mérito que o achado
apontava, sobre o corte invertido da `regra-0071`, é independente do nome e não
foi feita aqui.

`efeito_deteccao: deve_desaparecer`, porque a correção remove a causa: nomes
distintos não são mais nome repetido.
