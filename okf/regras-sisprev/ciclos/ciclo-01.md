---
type: Ciclo
id: ciclo-01
numero: 1
nome: Incapacidade permanente sob a LCE 1.100/2021
data: 2026-08-01
conjunto: ciclo-01-s6-fechamento
regras:
  - regra-0019
  - regra-0020
  - regra-0021
  - regra-0022
referencias:
  - regra-0001
  - regra-0002
  - regra-0003
  - regra-0004
  - regra-0005
  - regra-0006
  - regra-0007
  - regra-0008
  - regra-0009
---

# Ciclo 1 — Incapacidade permanente sob a LCE 1.100/2021

> **Estado:** auditoria jurídica concluída. O escopo é a incapacidade permanente
> sob a norma em vigor para requerimento novo — o Bloco C —, e as janelas
> históricas de invalidez pertencem ao [Ciclo 9](ciclo-09.md). A ativação
> institucional é ato posterior do IPERON e não é condição de encerramento.
> Este arquivo é a fonte única das decisões, dos resultados e da conclusão do
> ciclo.

## Identificação

- Data de abertura: 01/08/2026
- Commit-base da execução: `79a112562a7a9172b9cda484f3ac4f6bf5b6853f`
- Issue de execução: [#89](https://github.com/franklinbaldo/sisprev/issues/89)
- S0: PR #92 — `1393314118fad67e0057ee29d5c8740d01b71283`
- S1: PR #93 — `f68689841944000ab89db8379ff48be8e48aaf80`
- S2: PR #94 — `c722c6d3563e52626434c49a72126b516847585d`
- S3: PR #95 — `19b21ae55cd2845194dc77181562cd53cc033c71`
- S4: PR #96 — `ecd9f743391a8743ee536794ad74f72bd7cb2425`
- S5: PR #97 — `269ba448408848ceb3ba2844d791ab4658caf6b9`
- Reabertura da S3: PR #98 — `74259861e5f59cdc9966ed819f1ae1b62f3bfeab`
- S6 inicial: PR #99 — `e12fde90…`, que entregou o Bloco C de quatro origens
  para oito destinos e declarou que o ciclo **ainda não** podia ser encerrado
- Responsável pelas decisões jurídicas: Franklin Baldo

Fechamento da **auditoria** — o ato que recortou o ciclo para a norma em vigor,
levou o Bloco C de quatro origens a quarenta destinos, ativou os dois grupos e
gravou uma unidade por moléstia:

- Data de fechamento da auditoria: 03/08/2026
- Commit de fechamento da auditoria:
  `bea6f20c1c6b8b38f7da6db8f24623033a874902` — PR #102, com correções
  posteriores

Fechamento **institucional** — ato do IPERON, posterior e único, que não é
condição de encerramento deste ou de qualquer ciclo:

- Data de fechamento institucional:
- Commit de fechamento institucional:

## Contexto acadêmico e histórico

O benefício atravessa quatro desenhos materiais: invalidez na CF/88 original;
invalidez após a EC 20/1998; regra geral e transição do art. 6º-A após a EC
41/2003; e incapacidade permanente sob a EC 103/2019 e a LCE 1.100/2021.

A auditoria distinguiu direito adquirido, preservação, regime permanente, base
de cálculo, proporcionalidade, paridade e reajuste. Mudança de base, ajuste ou
limitador capaz de alterar o valor foi tratada como mudança material, não como
mera troca de citação.

## Dimensão social

A seleção define a renda de servidor permanentemente incapaz para o trabalho.
Erro de causa, janela, cálculo ou paridade pode reduzir benefício devido,
produzir pagamento sem fundamento ou impedir a explicação do ato concessório.

A cadeia exigida é: fatos do requerente → classe de causa → unidade aplicável →
fórmula inicial → regime de reajuste. Ausência de informação ou prova
insuficiente não equivale a `causa_comum`.

## Objetivo

Representar corretamente as hipóteses de **incapacidade permanente sob a LCE
1.100/2021** — a disciplina em vigor para requerimento novo —, preservando IDs
legados como histórico e criando regras propostas para cada combinação
materialmente distinta.

As janelas anteriores continuam existindo para direito adquirido, mas não
recebem pedido novo: são objeto do [Ciclo 9](ciclo-09.md), que as tem como
regras proprietárias. O que este ciclo faz com elas é analisar e autorar, sem
substituir — os três grupos dos Blocos A e B ficam `inativo`.

## Critério de fechamento

Aplica-se
[`okf/spec/ciclo.md`](../../spec/ciclo.md).
O ciclo se encerra quando cumpre as onze condições cumulativas da spec, que são
condições de **auditoria**: cobertura sem lacuna, mapa de substituição completo,
unidades `deployable`, grupos ativos com decisão de completude, cenários que
demonstram a seleção e gates íntegros.

**O ato institucional não é condição de encerramento.** A troca efetiva do
catálogo vigente é evento posterior e único, praticado pelo IPERON depois de
concluídos os ciclos, e não por ciclo. Exigi-lo aqui deixaria todo ciclo aberto
esperando um evento que não é dele.

## Cotejo jurídico

### T1 — Uma unidade por ramo

Integral e proporcional são unidades distintas. `integral: S` significa apenas
ausência de proporcionalização pelo tempo.

### T2 — Janelas temporais

`DATA_ADM_APOS`, `DATA_ADM_ATE` e `DATA_DIREITO_APOS` são inclusivos.
`DATA_DIREITO_ATE` é exclusivo.

Fronteiras principais:

- CF/88 original: `[05/10/1988, 16/12/1998)`;
- EC 20/1998: `[16/12/1998, 31/12/2003)`;
- Bloco B: `[31/12/2003, 01/01/2025)`;
- LCE 1.100/2021: desde `18/10/2021`.

### T3 — Classes de causa

O vocabulário é `acidente_em_servico`, `molestia_profissional`,
`doenca_catalogada` e `causa_comum`. A causa comum exige exclusão probatória das
classes qualificadas.

### T4 — Situação das regras

Uma regra de origem sai do catálogo pela ativação do grupo que a substitui, e
não por marca gravada nela: o frontmatter das regras não muda, e é por isso que
a introdução dos conjuntos é no-op demonstrável. Saem da composição as quatro
origens do Bloco C, cujos dois grupos estão ativos. As sete origens dos Blocos A
e B seguem na composição, porque os seus grupos permanecem inativos.

Nenhuma hipótese válida do escopo fica sem substituta e nenhuma lacuna
preexistente foi demonstrada nele.

### T5 — Bloco A

As três regras legadas são substituídas por oito unidades: quatro classes de
causa na CF/88 original e quatro na EC 20/1998.

### T6 — Bloco B

As quatro regras legadas são substituídas por quatorze unidades.

Na regra geral da EC 41:

- de 31/12/2003 a 19/02/2004, aplica-se a LC 228/2000;
- de 20/02/2004 a 12/03/2008, aplica-se a média federal iniciada pela MP
  167/2004, combinada com a fração anual da LC 228 na causa comum;
- desde 13/03/2008, aplica-se a LCE 432/2008, com limites do art. 45 e fração em
  dias do art. 17 na causa comum.

No art. 6º-A, as causas qualificadas usam remuneração do cargo e paridade; a
causa comum usa a fração anual da LC 228 até 12/03/2008 e a fração em dias da
LCE 432 desde 13/03/2008.

### T7 — Bloco C

As quatro regras legadas são substituídas por quarenta unidades: vinte para
ingresso até 31/12/2003 e vinte para ingresso a partir de 01/01/2004.

As vinte de cada coorte saem de duas decisões somadas. A primeira separa por
causa: acidente em serviço, moléstia profissional, doença grave do rol e o ramo
residual da causa comum. A segunda ramifica a terceira delas moléstia a
moléstia, pelo rol do art. 30, § 8º — dezesseis incisos que produzem dezessete
hipóteses, porque o inciso XVI reúne surdez permanente e anomalia da fala, ambas
restritas ao magistério. Daí dezessete moléstias, mais acidente em serviço, mais
moléstia profissional, mais causa comum.

As causas qualificadas usam a média do art. 24 sem proporcionalização; a causa
comum usa a média proporcional em dias do art. 26. O art. 27 disciplina
separadamente o reajuste, e é ele que distingue as duas coortes.

A combinação média proporcional com paridade representada por `regra-0020` é
juridicamente possível.

### T8 — Precedência entre Blocos B e C

Entre 18/10/2021 e 31/12/2024, primeiro se verifica a preservação do art. 4º da
ECE 146/2021. Se os requisitos anteriores foram cumpridos no prazo, aplica-se a
unidade preservada do Bloco B. O Bloco C somente incide quando essa preservação
não se aplica.

Não há escolha livre entre regimes.

### T9 — Composição final proposta

`ciclo-01-s6-fechamento` deriva de `ciclo-01-s3-reabertura-calculo` e resolve
148 membros:

- 108 regras legadas não afetadas, entre elas as sete origens dos Blocos A e B,
  cujos grupos não ativaram; e
- 40 regras propostas substituindo as quatro origens do Bloco C.

O conjunto permanece `proposto`. `catalogo-legado` continua sendo o único
conjunto vigente.

## Fluxo processual

- [x] S0 — inventário e linha de base.
- [x] S1 — contratos transversais.
- [x] S2 — Bloco A.
- [x] S3 — Bloco B inicial.
- [x] S4 — Bloco C.
- [x] S5 — consistência e precedência.
- [x] Reabertura da S3 — refinamento 8 → 14 no Bloco B.
- [x] S6 inicial — prova de cobertura e composição proposta na PR #99, que
  registrou que o ciclo ainda não podia ser encerrado.
- [x] Fechamento da auditoria — recorte para a norma em vigor, Bloco C de 4
  para 40, grupos ativos e uma unidade por moléstia, na PR #102.
- [ ] Ativação institucional — depende do IPERON.

## Entregável

A cadeia produz:

- mapa de substituição do escopo, de quatro origens para quarenta unidades, e o
  mapa autorado dos Blocos A e B, de sete origens para vinte e duas unidades,
  com os grupos inativos;
- matriz temporal completa;
- formas de cálculo autoradas;
- sobreposição intencional com regra de precedência;
- combinações impossíveis fundamentadas;
- 16 cenários representativos;
- composição final proposta com 148 membros; e
- distinção expressa entre conclusão jurídica e ativação institucional.

## Resultado por regra

Substituídas no escopo do ciclo — grupos ativos, origens fora da composição:

- [x] `regra-0019` — Bloco C, coorte de ingresso até 31/12/2003.
- [x] `regra-0020` — Bloco C, média proporcional com paridade.
- [x] `regra-0021` — Bloco C, coorte de ingresso a partir de 01/01/2004.
- [x] `regra-0022` — Bloco C, coorte de ingresso a partir de 01/01/2004.

Analisadas aqui, com substitutas autoradas, mas **fora do escopo recortado**:
os grupos seguem inativos e as origens permanecem na composição. A propriedade
delas passou ao [Ciclo 9](ciclo-09.md), que fecha a sequência com as janelas
históricas. A matriz jurídica não é reaberta; o que falta é autoria de
fundamentação, vínculo de forma de cálculo, disposição de achado e ato.

- [x] `regra-0001` — Bloco A.
- [x] `regra-0002` — Bloco A.
- [x] `regra-0004` — Bloco A.
- [x] `regra-0006` — Bloco B refinado.
- [x] `regra-0007` — Bloco B refinado.
- [x] `regra-0008` — Bloco B refinado.
- [x] `regra-0009` — Bloco B refinado.

## Correção de nome posterior ao fechamento

A coordenação apontou que os nomes das regras do ciclo terminavam quase todos na
mesma palavra, `paridade`, e que ela aparecia **no lugar** do rótulo de cálculo —
inclusive onde o rótulo gravado indica cálculo sobre médias. A causa está na
execução da gramática de `nome`, não na matriz jurídica: cálculo e paridade são
duas facetas, e a primeira aplicação as fundiu numa só, sempre em favor da
paridade.

Os nomes foram corrigidos para trazer as duas, o cálculo antes da paridade, e a
gramática está retificada em
[`decisoes-de-auditoria-2026-07-30.md`](../../../docs/analysis/decisoes-de-auditoria-2026-07-30.md)
(Decisão 10). Nenhum critério aferido mudou: `nome` está fora da chave material
do P2, e a Decisão 10 autoriza a auditoria a editá-lo na própria regra.

A correção **torna visível** uma tensão que o nome antes cobria — regras que
gravam `paridade: S` ao lado de um rótulo de cálculo que soa a média, caso de
`regra-0008`/`regra-0009` e de `regra-0016` a `regra-0018`. Em `regra-0008` a
conferência do art. 6º-A da EC 41/2003 já explica a convivência, e o corpo dela a
registra. Nas regras de pensão a conferência é do ciclo que as tem, e o nome
agora mostra os dois campos em vez de um.

## Referências de outros ciclos

`regra-0003` e `regra-0005` foram consultadas apenas como referências de
continuidade histórica. Não são proprietárias do Ciclo 1.

Regras e achados de outros ciclos, como `regra-0032`, permanecem com seus donos.

## Fontes legais consultadas

- Constituição Federal, art. 40, nas redações original, EC 20/1998, EC 41/2003
  e EC 103/2019;
- EC 41/2003, art. 6º-A, com redação da EC 70/2012;
- ECE 146/2021, art. 4º;
- MP 167/2004 e Lei 10.887/2004, art. 1º;
- LC 228/2000, especialmente arts. 43 e 44;
- LCE 432/2008, especialmente arts. 17, 20 e 45;
- LCE 1.100/2021, especialmente arts. 24, 26, 27 e 30;
- dispositivos e formas de cálculo autorados no repositório; e
- decisões semânticas documentadas em `okf/spec/`.

## Pendências que permanecem abertas

Nenhuma delas reabre a matriz jurídica. No escopo do ciclo, elas não impedem o
ato — as unidades estão em `deployable`, os grupos ativos e as decisões de
completude tomadas:

- Q6-S/Q6-T: captura, persistência e classificação da causa;
- premissa sobre o que o `tipo_calculo` implanta no produto, questão geral do
  catálogo e não de regra alguma, registrada na abertura do relatório;
- transcrição do § 16 do art. 40 da Constituição Federal, hoje alcançado apenas
  pela remissão do art. 27, inciso I, de que a paridade da coorte de ingresso
  até 31/12/2003 depende; e
- ato institucional com efeito `valida`, que não é condição de encerramento de
  ciclo algum.

Dos Blocos A e B, cuja substituição é do Ciclo 9:

- procedimento do IPERON para frações de ano sob a LC 228;
- transcrição taxonômica completa do rol da LC 228;
- fundamentação nas três partes da RFC 0014 para as unidades que ainda não a
  têm, vínculo de forma de cálculo e disposição dos achados das origens; e
- decisões de completude dos três grupos, hoje inativos.

## Conclusão do ciclo

O **Ciclo 1 está concluído**, no escopo em que foi recortado: a aposentadoria
por incapacidade permanente sob a LCE 1.100/2021 — a norma em vigor para
requerimento novo.

As quatro regras legadas do tema saíram da composição, substituídas por quarenta
unidades: em cada coorte de ingresso, acidente em serviço, moléstia profissional,
causa comum e uma regra por moléstia do rol do art. 30, § 8º. Todas em
`deployable`, todas com forma de cálculo vinculada e fundamentação autorada nas
três partes da RFC 0014. Os dois grupos estão ativos, com decisão de completude
conferida contra o texto transcrito, e cada origem dispôs de todo achado aberto
que a nomeia.

O que **não** faz parte do encerramento é o ato institucional. A composição
`ciclo-01-s6-fechamento` permanece `proposto` e o catálogo legado segue vigente
até que o IPERON pratique a ativação — evento único, depois de concluídos os
ciclos. Isso não é pendência do Ciclo 1.

As janelas históricas de invalidez — CF/88 original, EC 20, EC 41 e art. 6º-A —
ficaram **fora deste ciclo** e passaram ao [Ciclo 9](ciclo-09.md), que encerra a
sequência. Elas seguem valendo para direito adquirido, mas não recebem
requerimento novo, e por isso vão depois da norma em vigor, não antes. As
unidades já estão autoradas e os grupos permanecem inativos; o trabalho feito
aqui é herança daquele ciclo, não trabalho a refazer.

As sete regras continuam listadas neste documento como **referências**: elas
foram analisadas aqui, e é contra elas que a fronteira da norma em vigor foi
desenhada.
