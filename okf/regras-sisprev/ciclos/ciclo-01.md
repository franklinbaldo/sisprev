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

> **Estado: auditoria em fechamento — não encerrada.** O Bloco C (quatro
> origens legadas, quarenta regras propostas) tem sua derivação e
> verificação centralizadas em
> [`matriz-derivacao-verificacao-ciclo-01.md`](../../../docs/analysis/matriz-derivacao-verificacao-ciclo-01.md),
> que substitui a exigência de conferência individual em cada uma das
> quarenta regras: a correspondência estrutural entre cada regra e os
> requisitos que ela materializa — dispositivo, datas, projeção de cálculo —
> foi verificada programaticamente contra a matriz. O que resta é o que a
> matriz não pode verificar sozinha: a revisão de mérito da própria matriz
> pela coordenação, e uma pendência jurídica concreta que ela isola:
>
> - **`C1-R24`** — o marco temporal do requisito de magistério (art. 30,
>   § 8º, inciso XVI) não consta do dispositivo e não foi fixado por decisão
>   fundamentada. Afeta as quatro regras do inciso XVI (issue #121).
>
> `C1-R32` deixou de ser pendência de auditoria (RFC 0004, round 9,
> `okf/spec/regraproposta.md` e `okf/spec/conjunto.md`): a fórmula da causa
> comum sob a LCE 1.100/2021 está integralmente derivada, e as duas regras
> correspondentes são `estado_proposta: deployable`. O que resta é
> `estado_implantacao: pendente_mapeamento_sisprev` — confirmação de que
> `Proporcionalidade Dias` identifica essa fórmula sem ambiguidade perante
> outras fórmulas de causa comum que compartilham o rótulo no catálogo
> legado. Essa pendência é de implantação, não de derivação: bloqueia
> apenas a troca da fonte operacional de exportação dos dois grupos de
> substituição do Bloco C, que por isso permanecem `estado_grupo: inativo`
> — as quatro regras legadas continuam sendo a fonte operacional (issue
> #122) — mas não bloqueia o fechamento do ciclo quanto a essa derivação.
>
> Três dependências externas adicionais (`C1-R73`, `C1-R74`, `C1-R75` —
> captura da causa pelo Sisprev, confirmação geral de `tipo_calculo`,
> protocolo de nexo de moléstia profissional) permanecem registradas sem
> obstar o encerramento, como a spec admite (issue #124).
>
> A conferência está em
> [`conformidade-ciclo-01.md`](../../../docs/analysis/conformidade-ciclo-01.md).
> O escopo é a incapacidade permanente sob a LCE 1.100/2021, e as janelas
> históricas de invalidez pertencem ao [Ciclo 9](ciclo-09.md). Este arquivo é a
> fonte única das decisões, dos resultados e da conclusão do ciclo.

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

Composição corrente — o ato que recortou o ciclo para a norma em vigor, levou o
Bloco C de quatro origens a quarenta destinos e gravou uma unidade por
moléstia. **Não é o fechamento da auditoria**, e a #99, que o precede, já
registrava que o ciclo não podia ser encerrado:

- PR #102 — `bea6f20c1c6b8b38f7da6db8f24623033a874902`, de 03/08/2026, ativou
  os dois grupos; revertida em 04/08/2026 (ver Estado, acima) — os grupos
  estão `inativo` desde então, com correções posteriores

Fechamento da **auditoria** — depende de revisão de mérito, pela
coordenação, da matriz de derivação e verificação (issue #123) e da decisão
sobre o marco temporal de `C1-R24` (issue #121). `C1-R32` não bloqueia mais
o fechamento (RFC 0004, round 9): a derivação da causa comum está
concluída, e a pendência restante é de implantação (issue #122), separada
da auditoria. As demais oito condições permanecem cumpridas, como já
registrado em
`conformidade-ciclo-01.md`:

- Data de fechamento da auditoria:
- Commit de fechamento da auditoria:

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
1.100/2021** — a disciplina sob a qual o direito se forma hoje —, preservando
IDs legados como histórico e criando regras propostas para cada combinação
materialmente distinta.

As janelas anteriores **não admitem formação de novo direito depois dos seus
marcos finais, mas continuam fundamentando requerimentos novos com base em
direito adquirido**: quem implementou todos os requisitos na vigência de uma
delas pode requerer hoje, e a regra que o alcança é a daquela janela. Elas são
objeto do [Ciclo 9](ciclo-09.md), que as tem como regras proprietárias. O que
este ciclo faz com elas é analisar e autorar, sem substituir — os três grupos
dos Blocos A e B ficam `inativo`.

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
a introdução dos conjuntos é no-op demonstrável. As quatro origens do Bloco C
**não saíram da composição**: os dois grupos que as substituiriam voltaram a
`estado_grupo: inativo` em 04/08/2026 (ver Estado, acima, e
`ciclo-01-s4-bloco-c.md`), porque nem todos os vinte destinos de cada grupo
estão `deployable` — as duas unidades de causa comum recuaram a `preview`.
Pela regra de seleção de origem única do exportador (RFC 0004 §1.5), as
quatro origens legadas continuam sendo a fonte operacional. As sete origens
dos Blocos A e B seguem igualmente na composição, com seus grupos
permanecendo inativos.

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

A derivação completa desta seção — cada requisito, a regra que o
materializa, a representação no catálogo e o caminho de verificação — está
organizada em
[`matriz-derivacao-verificacao-ciclo-01.md`](../../../docs/analysis/matriz-derivacao-verificacao-ciclo-01.md).
T7 permanece a fonte da matriz jurídica; a matriz é onde essa fonte se
verifica contra as quarenta regras.

### T8 — Precedência entre Blocos B e C

Entre 18/10/2021 e 31/12/2024, primeiro se verifica a preservação do art. 4º da
ECE 146/2021. Se os requisitos anteriores foram cumpridos no prazo, aplica-se a
unidade preservada do Bloco B. O Bloco C somente incide quando essa preservação
não se aplica.

Não há escolha livre entre regimes.

### T9 — Composição final proposta

`ciclo-01-s6-fechamento` deriva de `ciclo-01-s3-reabertura-calculo` e resolve
148 membros:

- 108 regras legadas não afetadas;
- as sete origens dos Blocos A e B, cujos grupos permanecem inativos; e
- as quatro origens do Bloco C, cujos dois grupos propõem 40 regras
  substitutas mas estão `inativo` desde 04/08/2026 (T4, acima) — a
  substituição ainda não é efetiva nem mesmo dentro desta composição
  proposta.

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
- [x] Composição corrente — recorte para a norma em vigor, Bloco C de 4 para
  40 e uma unidade por moléstia, na PR #102 (grupos ativados então, revertidos
  a `inativo` em 04/08/2026 — ver Estado, acima).
- [x] Matriz de derivação e verificação — substitui a conferência
  individual das quarenta regras por demonstração centralizada, por
  requisito; as quarenta regras apontam os identificadores que materializam
  (issue #123).
- [ ] Fechamento da auditoria — depende de: revisão de mérito da matriz pela
  coordenação; e decisão fundamentada sobre o marco temporal de `C1-R24`
  (issue #121).
- [ ] Troca da fonte operacional de exportação do Bloco C — depende de
  confirmação de implantação de `C1-R32` (issue #122); não é pendência de
  auditoria (RFC 0004, round 9).
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

Substitutas autoradas no escopo do ciclo — grupos `inativo` desde 04/08/2026,
origens ainda na composição (T4, acima):

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

## Pendências e dependências externas que permanecem abertas

A lista completa, com fonte, regras alcançadas, responsável e evidência
exigida, está na
[matriz de derivação e verificação](../../../docs/analysis/matriz-derivacao-verificacao-ciclo-01.md#7-pend%C3%AAncias-reais)
(seção 7). Resumo:

**Pendências da própria auditoria — obstam o encerramento:**

- `C1-R24` — marco temporal de aferição do requisito de magistério, quatro
  unidades do inciso XVI (issue #121);
- revisão de mérito da matriz pela coordenação — decisões jurídicas,
  exceções e suficiência das evidências que a matriz organiza, mas não
  decide sozinha (issue #123).

**Pendência de implantação — não obsta o encerramento (RFC 0004, round 9):**

- `C1-R32` — `Proporcionalidade Dias` grava, no catálogo, três fórmulas
  juridicamente distintas e quatro tipos de benefício; falta confirmação de
  que o rótulo identifica sem ambiguidade a fórmula da LCE 1.100 (issue
  #122). A derivação está concluída (`estado_proposta: deployable` nas duas
  regras); a pendência é `estado_implantacao: pendente_mapeamento_sisprev`,
  e bloqueia apenas a troca da fonte operacional de exportação do grupo.

**Dependências externas — não obstam o encerramento, registradas na issue
[#124](https://github.com/franklinbaldo/sisprev/issues/124):**

- `C1-R73` — captura e classificação da causa pelo Sisprev (Q6-S/Q6-T);
- `C1-R74` — confirmação operacional geral do rótulo de `tipo_calculo`;
- `C1-R75` — protocolo institucional de reconhecimento do nexo de moléstia
  profissional (lacuna normativa, RFC 0004 §7/§14);
- `C1-R61` — opção do § 16 do art. 40 da Constituição, sem campo próprio no
  cadastro, verificada no processo; e
- ato institucional com efeito `valida`, que não é condição de encerramento de
  ciclo algum.

Dos Blocos A e B, cuja substituição é do Ciclo 9:

- procedimento do IPERON para frações de ano sob a LC 228;
- transcrição taxonômica completa do rol da LC 228;
- fundamentação nas três partes da RFC 0014 para as unidades que ainda não a
  têm, vínculo de forma de cálculo e disposição dos achados das origens; e
- decisões de completude dos três grupos, hoje inativos.

## Conclusão do ciclo

O Ciclo 1 entregou a matriz jurídica, a cobertura e a composição do escopo
em que foi recortado — a aposentadoria por incapacidade permanente sob a
LCE 1.100/2021, norma sob a qual o direito se forma hoje. As quarenta
regras propostas do Bloco C têm sua derivação e verificação centralizadas em
[`matriz-derivacao-verificacao-ciclo-01.md`](../../../docs/analysis/matriz-derivacao-verificacao-ciclo-01.md),
que substitui a conferência individual regra a regra: a correspondência
estrutural entre cada regra e os requisitos que ela materializa foi
verificada programaticamente, e cada regra aponta, no próprio corpo, os
identificadores correspondentes.

**Ele ainda não está encerrado.** Das onze condições cumulativas de
`okf/spec/ciclo.md`, oito permanecem cumpridas; as condições 3, 5 e 9
dependem de um requisito específico que a matriz isola — `C1-R24`, o marco
temporal do magistério, sem decisão fundamentada, afetando as quatro
regras do inciso XVI — e da revisão de mérito da própria matriz pela
coordenação, que nenhuma verificação programática substitui. As demais
trinta e seis regras não têm pendência material aberta.

`C1-R32` não é mais uma dessas pendências (RFC 0004, round 9): a derivação
da causa comum está concluída, as duas regras correspondentes são
`estado_proposta: deployable`, e a condição 9 está satisfeita quanto a essa
substituição. O que resta é `estado_implantacao: pendente_mapeamento_sisprev` — confirmação de que `Proporcionalidade Dias`
identifica essa fórmula sem ambiguidade perante outras fórmulas de causa
comum que compartilham o rótulo no catálogo legado. Essa pendência de
implantação bloqueia apenas a troca da fonte operacional de exportação:
por RFC 0004 §1.4/§1.5 e `okf/spec/conjunto.md`, os dois grupos de
substituição do Bloco C permanecem `estado_grupo: inativo` até a
confirmação, e as quatro regras legadas continuam sendo a fonte
operacional — mas isso não é pendência de auditoria.

O ato institucional **também não** faz parte do encerramento, e continua
sendo questão distinta: a composição `ciclo-01-s6-fechamento` permanece
`proposto` e o catálogo legado segue vigente até que o IPERON pratique a
ativação — evento único, depois de concluídos os ciclos. Isso não é
pendência do Ciclo 1, mas não supre a pendência da própria auditoria descrita
acima.

As janelas históricas de invalidez — CF/88 original, EC 20, EC 41 e art. 6º-A —
ficaram **fora deste ciclo** e passaram ao [Ciclo 9](ciclo-09.md), que encerra a
sequência. Nelas não se forma direito novo depois dos
seus marcos finais, mas elas continuam fundamentando requerimento novo de quem
implementou os requisitos na sua vigência — e por isso vão depois da norma sob
a qual o direito se forma hoje, não antes. As
unidades já estão autoradas e os grupos permanecem inativos; o trabalho feito
aqui é herança daquele ciclo, não trabalho a refazer.

As sete regras continuam listadas neste documento como **referências**: elas
foram analisadas aqui, e é contra elas que a fronteira da norma em vigor foi
desenhada.
