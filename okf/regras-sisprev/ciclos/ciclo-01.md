---
type: Ciclo
id: ciclo-01
numero: 1
nome: Incapacidade permanente sob a LCE 1.100/2021
data: 2026-08-01
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

> **Estado: auditoria encerrada em 2026-08-05.** O Bloco C (quatro
> origens legadas, **sessenta** regras propostas em três famílias de vinte
> causas) tem sua derivação e
> verificação centralizadas em
> [`matriz-derivacao-verificacao-ciclo-01.md`](../../../docs/analysis/matriz-derivacao-verificacao-ciclo-01.md),
> que substitui a exigência de conferência individual em cada uma das
> sessenta regras: a correspondência estrutural entre cada regra e os
> requisitos que ela materializa — dispositivo, datas, projeção de cálculo —
> foi verificada programaticamente contra a matriz. A última pendência que a
> matriz isolava como decisão jurídica da coordenação foi decidida:
>
> - **`C1-R24`** — encerrado em 2026-08-05. O art. 30, § 8º, inciso XVI, da
>   LCE 1.100/2021 restringe surdez permanente e anomalia da fala ao caso de
>   magistério, sem instituir marco temporal autônomo para a aferição desse
>   vínculo — ao contrário do caput do mesmo § 8º, que fixa expressamente o
>   marco do acometimento em relação à filiação. Não havia lacuna a suprir:
>   a exigência é a condição funcional do magistério, verificável no caso
>   concreto pela mesma via que já verifica as demais condições não
>   programáticas do Bloco C, sem marco temporal fixado por lei para nenhuma
>   delas. Fixar um marco que o texto não impõe seria decisão jurídica nova,
>   não leitura da norma. Decisão datada nas quatro regras do inciso XVI
>   (`decisoes`, 2026-08-05) e na issue #121.
>
> `C1-R32` não é pendência de auditoria (RFC 0004, round 9,
> `okf/spec/regraproposta.md`): a fórmula da causa comum sob a LCE
> 1.100/2021 está integralmente derivada, e as regras correspondentes
> são `estado_auditoria: concluida`. **Emenda (RFC 0004, round 12, 2026-08-05).**
> As unidades de causa comum recebem
> `estado_implantacao: confirmada_com_ressalva`: `regra-0020` e `regra-0021`
> já gravam, em produção, a mesma combinação (`integral: N`,
> `tipo_calculo: Proporcionalidade Dias`) para as mesmas hipóteses de causa
> comum, o que sustenta a presunção de que o Sisprev já dispõe de mecanismo
> operacional para elas. O que resta é mais estreito do que a ambiguidade de
> catálogo que motivou `pendente_mapeamento_sisprev`: confirmar em
> homologação prática se a execução aplica a base composta do art. 26 —
> média do art. 24, limitada pelo § 10, então proporcionalizada — e não uma
> proporcionalidade nua. A ressalva viaja com a regra
> (`ressalva_homologacao`) e deve ser resolvida antes da ativação em
> produção, não antes da carga.
>
> **Decomposição em três famílias (RFC 0004, round 16, 2026-08-05).** A
> divisão em duas coortes de ingresso era insuficiente: os arts. 24, *caput*,
> 25 e 27, I condicionam o que dispõem à **ausência** da opção pelo regime de
> previdência complementar, de modo que o servidor optante não era alcançado
> por nenhuma das duas. O Bloco C passou a ter três famílias mutuamente
> excludentes de vinte causas — ingresso até 31/12/2003 sem opção; de
> 01/01/2004 a 05/11/2018 sem opção; e, numa família só, ingresso a partir de
> 06/11/2018 **ou** opção prévia e expressa de quem ingressou antes dessa data
> (art. 24, §§ 11 e 12). São sessenta regras propostas, e não quarenta.
>
> **A atomicidade da carga de homologação, computada por `scripts/derivar.py`
> a partir de `origens_legacy` (RFC 0004, round 11), é mais fina do que a
> antiga declaração por grupo.** Cada uma das sessenta regras propostas do
> Bloco C descende de **uma única** regra legada: as regras de causa
> qualificada descendem da regra que as agrupava incorretamente
> (`regra-0019`/`regra-0022`) e as de causa comum descendem da outra
> (`regra-0020`/`regra-0021`). Com as três famílias, `regra-0021` e
> `regra-0022` passam a ter também os destinos da família sujeita ao regime
> complementar, que está `pendente_mapeamento_sisprev` — o catálogo legado não
> tem valor de `tipo_calculo` que exprima o teto do RGPS nem coluna que
> registre a opção do § 16. Como a troca de fonte operacional é atômica,
> **dos sessenta destinos do Bloco C, vinte entram na carga de homologação e
> quarenta ficam fora**:
>
> - `regra-0019` → dezenove causas qualificadas de ingresso até 2003, na
>   carga, sem ressalva;
> - `regra-0020` → a causa comum da mesma família, na carga, com ressalva de
>   homologação;
> - `regra-0022` → trinta e oito destinos (as qualificadas das outras duas
>   famílias), fora da carga;
> - `regra-0021` → dois destinos (a causa comum de cada uma delas), fora da
>   carga.
>
> Retirar `regra-0021`/`regra-0022` da produção antes de a família sujeita ao
> regime complementar ter representação no Sisprev deixaria essa população sem
> regra aplicável — é o que a atomicidade impede. Isso não reabre nem revê a
> derivação jurídica de nenhuma das sessenta: nenhuma delas aguarda decisão
> jurídica, e sim a representação do teto do RGPS e da opção pelo regime
> complementar no cadastro (`C1-R34`, `C1-R15`; issues #122 e #124).
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
moléstia; os quarenta destinos passaram a sessenta na decomposição em três
famílias (RFC 0004, round 16). **Não é o fechamento da auditoria**, e a #99,
que o precede, já registrava que o ciclo não podia ser encerrado:

- PR #102 — `bea6f20c1c6b8b38f7da6db8f24623033a874902`, de 03/08/2026, ativou
  os dois grupos; revertida em 04/08/2026 (ver Estado, acima) — os grupos
  estão `inativo` desde então, com correções posteriores

Fechamento da **auditoria** — a revisão de mérito da coordenação sobre a
matriz de derivação e verificação (issue #123) tinha, como única decisão
jurídica substantiva pendente, o marco temporal de `C1-R24` (issue #121);
decidida em 2026-08-05, as onze condições de `okf/spec/ciclo.md` se cumprem.
`C1-R32` não bloqueia o fechamento (RFC 0004, round 9): a derivação da
causa comum está concluída, e a pendência restante é de implantação (issue
#122), separada da auditoria. As demais condições permanecem cumpridas,
como registrado em `conformidade-ciclo-01.md`:

- Data de fechamento da auditoria: 05/08/2026
- Commit de fechamento da auditoria: `5642b655121136245ed0a3cf7f2979b5d2e2b1a2`

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
este ciclo faz com elas é analisar e autorar, sem substituir — as 22 regras
propostas dos Blocos A e B ficam `estado_auditoria: preview`.

## Critério de fechamento

Aplica-se
[`okf/spec/ciclo.md`](../../spec/ciclo.md).
O ciclo se encerra quando cumpre as onze condições cumulativas da spec, que são
condições de **auditoria**: cobertura sem lacuna, mapa de substituição completo,
unidades `estado_auditoria: concluida`, cenários que demonstram a seleção e
gates íntegros.

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

Uma regra de origem sai da carga de homologação quando o componente do grafo
origem↔destino a que pertence está pronto — todos os seus membros
`estado_auditoria: concluida` e `estado_implantacao` em `confirmada` ou
`confirmada_com_ressalva` (`okf/spec/regraproposta.md`, "Atomicidade é
derivada, não declarada") —, não por marca gravada nela: o frontmatter das
regras legadas não muda. Das quatro origens do Bloco C, **duas estão prontas
para sair**: `regra-0019`, substituída pelas dezenove causas qualificadas de
ingresso até 2003, sem ressalva; e `regra-0020`, substituída pela causa comum
da mesma família, com `estado_implantacao: confirmada_com_ressalva` — ressalva
de homologação prática, não de derivação.

`regra-0021` e `regra-0022` **não saem ainda**. Seus componentes reúnem
também os destinos da família sujeita ao regime de previdência complementar,
que estão `pendente_mapeamento_sisprev`, e a troca de fonte operacional é
atômica: quarenta dos sessenta destinos ficam fora da carga enquanto o
cadastro não representar o teto do RGPS e a opção do § 16. Não é pendência de
auditoria — as sessenta regras estão `estado_auditoria: concluida`.

As sete origens dos Blocos A e B seguem na composição: as 22
regras propostas que as substituiriam permanecem `estado_auditoria: preview`.

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

As quatro regras legadas descrevem, juridicamente, **sessenta** unidades
propostas, em três famílias mutuamente excludentes de vinte causas: ingresso
até 31/12/2003 sem opção pelo regime de previdência complementar; ingresso de
01/01/2004 a 05/11/2018 sem essa opção; e ingresso a partir de 06/11/2018
**ou** opção prévia e expressa de quem ingressou antes dessa data. O estado de
substituição efetiva de cada origem — `regra-0019` e `regra-0020` prontas para
sair, `regra-0021` e `regra-0022` retidas pela atomicidade — está em T4, acima.

As vinte de cada família saem de duas decisões somadas. A primeira separa por
causa: acidente em serviço, moléstia profissional, doença grave do rol e o ramo
residual da causa comum. A segunda ramifica a terceira delas moléstia a
moléstia, pelo rol do art. 30, § 8º — dezesseis incisos que produzem dezessete
hipóteses, porque o inciso XVI reúne surdez permanente e anomalia da fala, ambas
restritas ao magistério. Daí dezessete moléstias, mais acidente em serviço, mais
moléstia profissional, mais causa comum.

A base de cálculo varia por família: a de ingresso até 2003 usa a remuneração
do cargo efetivo do art. 25; as outras duas usam a média do art. 24, e só a
família sujeita ao regime complementar sofre o limite máximo dos benefícios do
RGPS (art. 24, §§ 11 e 12). Em qualquer delas, as causas qualificadas não
sofrem proporcionalização e a causa comum usa a fração em dias do art. 26. O
art. 27 disciplina separadamente o reajuste, e a paridade do seu inciso I
alcança só a primeira família.

A combinação média proporcional com paridade representada por `regra-0020` é
juridicamente possível.

**Decisão de completude, coorte até 31/12/2003** (decidido por
`franklinbaldo`, 2026-08-03): os vinte destinos cobrem exaustivamente as
causas do art. 30, caput e § 8º, para esta coorte. Justificativa: "O art.
30, caput, da LCE 1.100/2021 enumera exaustivamente as causas que afastam a
proporcionalização — acidente em serviço, moléstia profissional e doença
grave, contagiosa ou incurável — e trata todas as demais como ramo
residual. Os destinos deste grupo cobrem as três causas nomeadas mais a
causa comum, e a terceira delas é decomposta moléstia a moléstia pelo rol
do § 8º: dezesseis incisos que produzem dezessete hipóteses, porque o
inciso XVI reúne surdez permanente e anomalia da fala, ambas restritas ao
magistério. São vinte destinos, e a conferência foi feita item a item
contra o texto transcrito do art. 30, caput e §§ 5º, 8º, 13 e 14, da LCE
1.100/2021, com os dezesseis incisos do § 8º autorados como dispositivos
próprios a partir da compilação da DITEL/Casa Civil — não contra o que já
existia em disco. A cláusula 'dentre outras que a lei indicar' não deixa
hipótese descoberta: ela remete a lei, não a avaliação caso a caso, e
nenhuma outra lei indicativa foi localizada — se vier a existir, faltará
uma regra, e é esse o limite exato desta declaração." Fonte:
`/dispositivos/lce-1100-2021/art-30-caput/original.md`. Decisão jurídica
independente de `estado_implantacao` (RFC 0004, round 10) — não é revista
pela pendência de implantação de `C1-R32`.

**Decisão de completude, coorte a partir de 01/01/2004** (decidido por
`franklinbaldo`, 2026-08-03): mesma análise acima, aplicada à segunda
coorte — os vinte destinos cobrem exaustivamente as mesmas causas do art.
30, caput e § 8º. Mesma fonte, mesma independência frente a
`estado_implantacao`.

**Extensão às três famílias** (2026-08-05, RFC 0004, round 16): a decomposição
por adesão ao regime de previdência complementar repartiu a segunda coorte em
duas famílias e não tocou no eixo das causas — as vinte causas são as mesmas
nas três, e a decisão de completude acima vale, por identidade de análise,
para a família sujeita ao regime complementar. O que mudou foi o critério de
alcance de cada família, não o rol coberto.

A derivação completa desta seção — cada requisito, a regra que o
materializa, a representação no catálogo e o caminho de verificação — está
organizada em
[`matriz-derivacao-verificacao-ciclo-01.md`](../../../docs/analysis/matriz-derivacao-verificacao-ciclo-01.md).
T7 permanece a fonte da matriz jurídica; a matriz é onde essa fonte se
verifica contra as sessenta regras.

### T8 — Precedência entre Blocos B e C

Entre 18/10/2021 e 31/12/2024, primeiro se verifica a preservação do art. 4º da
ECE 146/2021. Se os requisitos anteriores foram cumpridos no prazo, aplica-se a
unidade preservada do Bloco B. O Bloco C somente incide quando essa preservação
não se aplica.

Não há escolha livre entre regimes.

### T9 — Composição final proposta

A composição proposta resolve 168 membros:

- 108 regras legadas não afetadas — entre elas as sete origens dos Blocos A e
  B, cujas 22 regras propostas permanecem `estado_auditoria: preview`, porque
  a substituição delas é do Ciclo 9; e
- as quatro origens do Bloco C, cujas 60 regras propostas estão
  `estado_auditoria: concluida`. Delas, **vinte entram na carga de
  homologação** e **quarenta ficam fora**, pelo grafo origem↔destino computado
  por `scripts/derivar.py` (`okf/spec/regraproposta.md`): entram as dezenove
  causas qualificadas de `regra-0019`, sem ressalva, e a causa comum de
  `regra-0020`, com `estado_implantacao: confirmada_com_ressalva`, carregando
  a ressalva sobre a base do art. 26 que a homologação prática precisa
  confirmar antes da ativação em produção (`C1-R32`, issue #122); ficam fora
  os quarenta destinos de `regra-0021`/`regra-0022`, presos pela atomicidade
  enquanto a família sujeita ao regime de previdência complementar estiver
  `pendente_mapeamento_sisprev` (`C1-R34`, `C1-R15`; issues #122 e #124).

`catalogo-legado` continua sendo o único catálogo vigente.

### T9.1 — Combinações juridicamente impossíveis

Dentro de cada regime, as seguintes combinações são excluídas pela própria
norma: causa qualificada com ramo proporcional; causa comum com ramo sem
proporcionalização; paridade na regra geral da EC 41; ausência de paridade
no art. 6º-A; ausência de paridade na coorte da LCE 1.100 com ingresso até
31/12/2003; e paridade na coorte da LCE 1.100 com ingresso a partir de
01/01/2004.

A combinação média proporcional com paridade **não** é impossível: existe
no Bloco C para causa comum e ingresso até 31/12/2003 (`regra-0020`),
porque o art. 26 disciplina o cálculo inicial e o art. 27, I, disciplina
separadamente o reajuste.

### T9.2 — Cenários representativos

Todos pressupõem incapacidade permanente e prova suficiente da causa
indicada.

01. Direito em 15/12/1998, acidente em serviço: unidade qualificada da CF/88
    original.
02. Direito em 16/12/1998, causa comum: unidade proporcional da EC 20/1998.
03. Direito em 30/12/2003, doença catalogada: unidade qualificada da EC 20/1998.
04. Direito em 31/12/2003, causa comum: unidade pré-MP 167 da regra geral da EC
    41, com remuneração do cargo proporcional por anos.
05. Direito em 19/02/2004, acidente em serviço: unidade pré-MP 167, com
    remuneração integral do cargo.
06. Direito em 20/02/2004, moléstia profissional: unidade pós-MP 167, com média
    sem proporcionalização.
07. Direito em 12/03/2008, causa comum: média federal proporcional pela fração
    anual da LC 228.
08. Direito em 13/03/2008, causa comum: média limitada da LCE 432 proporcional em
    dias.
09. Ingresso até 2003, direito em 2007 e causa comum sob o art. 6º-A: remuneração
    do cargo proporcional pela fração anual, com paridade.
10. Ingresso até 2003, direito em 2008 após 13/03 e causa comum sob o art. 6º-A:
    remuneração do cargo proporcional em dias, com paridade.
11. Direito preservado formado em 2023 e requerido em 2026: unidade do Bloco B,
    porque o art. 4º assegura concessão a qualquer tempo.
12. Direito em 2023 sem preencher os critérios anteriores, ingresso até 2003 e
    acidente em serviço: unidade do Bloco C, média sem proporcionalização e
    paridade.
13. Direito em 2025, ingresso até 2003 e causa comum: unidade do Bloco C, média
    proporcional em dias e paridade.
14. Direito em 2025, ingresso após 2003 e doença catalogada: unidade do Bloco C,
    média sem proporcionalização e sem paridade.
15. Causa não informada em qualquer regime: seleção indeterminada; não se
    presume `causa_comum`.
16. Prova insuficiente para excluir causa qualificada: seleção indeterminada; o
    ramo residual não é escolhido.

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
  individual das regras propostas por demonstração centralizada, por
  requisito; as sessenta regras apontam os identificadores que materializam
  (issue #123).
- [x] Fechamento da auditoria — revisão de mérito da matriz pela
  coordenação e decisão fundamentada sobre `C1-R24` (issue #121),
  concluídas em 05/08/2026: o dispositivo não institui marco temporal
  autônomo para o requisito de magistério.
- [x] Decomposição do Bloco C em três famílias, de quarenta para sessenta
  regras propostas (RFC 0004, round 16) — os arts. 24, *caput*, 25 e 27, I
  exigem a ausência da opção pelo regime de previdência complementar, e sem a
  terceira família o optante não era alcançado por nenhuma das outras duas.
- [x] Entrada de vinte das sessenta regras do Bloco C na carga de homologação
  (RFC 0004, rounds 12 e 16) — as dezenove qualificadas de `regra-0019` sem
  ressalva e a causa comum de `regra-0020` com
  `estado_implantacao: confirmada_com_ressalva`, evidenciada por `regra-0020`
  já produzir a mesma combinação; a ressalva sobre a base do art. 26
  (`C1-R32`, issue #122) viaja com ela.
- [ ] Representação do teto do RGPS e da opção pelo § 16 no cadastro
  (`C1-R34`, `C1-R15`; issues #122 e #124) — condição da entrada em carga dos
  quarenta destinos de `regra-0021`/`regra-0022`, hoje retidos pela
  atomicidade da troca de fonte operacional.
- [ ] Confirmação em homologação prática da fórmula da causa comum — a
  ressalva de `C1-R32` (issue #122), a resolver antes da ativação em
  produção, não antes da carga.
- [ ] Ativação institucional — depende do IPERON.

## Entregável

A cadeia produz:

- mapa de substituição do escopo, de quatro origens para sessenta unidades em
  três famílias — vinte na carga de homologação (dezenove sem ressalva e a
  causa comum de ingresso até 2003 com ressalva sobre a base de cálculo,
  sujeita a confirmação prática antes da ativação em produção) e quarenta
  fora dela, retidas pela atomicidade enquanto a família sujeita ao regime de
  previdência complementar não tiver representação no Sisprev —, e o mapa
  autorado dos Blocos A e B, de sete origens para vinte e duas unidades em
  `estado_auditoria: preview`;
- matriz temporal completa;
- formas de cálculo autoradas;
- sobreposição intencional com regra de precedência;
- combinações impossíveis fundamentadas;
- 16 cenários representativos;
- composição final proposta com 168 membros; e
- distinção expressa entre conclusão jurídica e ativação institucional.

## Resultado por regra

Substitutas autoradas no escopo do ciclo (T4, acima):

- [x] `regra-0019` — Bloco C, família de ingresso até 31/12/2003 sem opção
  pelo regime de previdência complementar; substituída pelas dezenove
  unidades não causa-comum, na carga de homologação sem ressalva.
- [x] `regra-0020` — Bloco C, causa comum com paridade da mesma família;
  unidade sucessora `estado_implantacao: confirmada_com_ressalva`, na carga
  de homologação com ressalva sobre a base do art. 26 (C1-R32, issue #122).
- [x] `regra-0021` — Bloco C, causa comum sem paridade; **dois** destinos —
  a causa comum da família de 2004 a 05/11/2018 e a da família sujeita ao
  regime de previdência complementar. Auditoria concluída nos dois; o
  componente **não entra na carga de homologação** enquanto o segundo estiver
  `pendente_mapeamento_sisprev` (`C1-R34`, `C1-R15`).
- [x] `regra-0022` — Bloco C, causas qualificadas sem paridade; **trinta e
  oito** destinos — as dezenove da família de 2004 a 05/11/2018 e as dezenove
  da família sujeita ao regime complementar. Auditoria concluída em todos; o
  componente **não entra na carga de homologação** pela mesma razão.

Analisadas aqui, com substitutas autoradas, mas **fora do escopo recortado**:
as 22 regras propostas permanecem `estado_auditoria: preview` e as origens
permanecem na composição. A propriedade delas passou ao [Ciclo 9](ciclo-09.md),
que fecha a sequência com as janelas históricas. A matriz jurídica não é
reaberta; o que falta é autoria de fundamentação, vínculo de forma de
cálculo, disposição de achado e ato.

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

- LC 1/1984, LC 39/1990 e LC 68/1992 — regime da CF/88 original, Bloco A;
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

**Pendências da própria auditoria — nenhuma.** `C1-R24` — marco temporal de
aferição do requisito de magistério, quatro unidades do inciso XVI — foi
reavaliado e encerrado em 05/08/2026 (issue #121): o dispositivo não institui
marco temporal autônomo para a aferição do vínculo com o magistério, e a
exigência já estava corretamente modelada no campo de seleção das quatro
regras. A revisão de mérito da matriz pela coordenação (issue #123) tinha
`C1-R24` e `C1-R32` como únicas decisões jurídicas substantivas pendentes;
ambas decididas, não resta revisão de mérito em aberto.

**Ressalva de homologação — não obsta o encerramento nem a carga (RFC 0004,
round 12):**

- `C1-R32` — `Proporcionalidade Dias` grava, no catálogo, três fórmulas
  juridicamente distintas e quatro tipos de benefício; `regra-0020` e
  `regra-0021` já gravam, em produção, essa combinação para as mesmas
  hipóteses de causa comum, o que sustenta a presunção de que o sistema já
  as executa. O que falta confirmar em homologação prática, antes da
  ativação em produção, é mais estreito: se a execução aplica a base
  composta do art. 26 — média do art. 24, limitada pelo § 10, então
  proporcionalizada — e não uma proporcionalidade nua (issue #122). A
  derivação está concluída (`estado_auditoria: concluida` nas três unidades
  de causa comum); a ressalva é `estado_implantacao: confirmada_com_ressalva`
  e não bloqueia, por si, a entrada na carga de homologação — o sucessor de
  `regra-0020` entra levando-a. O que retém o sucessor de `regra-0021` é
  outra coisa: o componente dele reúne também a causa comum da família
  sujeita ao regime de previdência complementar, ainda
  `pendente_mapeamento_sisprev`. A ressalva do art. 26 precisa ser resolvida
  antes da ativação em produção, não antes da carga.

**Dependências externas — não obstam o encerramento, registradas na issue
[#124](https://github.com/franklinbaldo/sisprev/issues/124):**

- `C1-R73` — captura e classificação da causa pelo Sisprev (Q6-S/Q6-T);
- `C1-R74` — confirmação operacional geral do rótulo de `tipo_calculo`;
- `C1-R75` — protocolo institucional de reconhecimento do nexo de moléstia
  profissional (lacuna normativa, RFC 0004 §7/§14);
- `C1-R61`/`C1-R15` — opção do § 16 do art. 40 da Constituição, sem campo
  próprio no cadastro, verificada no processo;
- `C1-R34` — mecanismo pelo qual o Sisprev executa o limite máximo dos
  benefícios do RGPS, sem valor de `tipo_calculo` que o exprima. Com
  `C1-R15`, é o que retém quarenta dos sessenta destinos fora da carga de
  homologação (issues #122 e #124); e
- ato institucional com efeito `valida`, que não é condição de encerramento de
  ciclo algum.

Dos Blocos A e B, cuja substituição é do Ciclo 9:

- procedimento do IPERON para frações de ano sob a LC 228;
- transcrição taxonômica completa do rol da LC 228;
- fundamentação nas três partes da RFC 0014 para as unidades que ainda não a
  têm, vínculo de forma de cálculo e disposição dos achados das origens; e
- decisão de completude das 22 unidades, hoje `estado_auditoria: preview`.

## Conclusão do ciclo

O Ciclo 1 entregou a matriz jurídica, a cobertura e a composição do escopo
em que foi recortado — a aposentadoria por incapacidade permanente sob a
LCE 1.100/2021, norma sob a qual o direito se forma hoje. As sessenta
regras propostas do Bloco C têm sua derivação e verificação centralizadas em
[`matriz-derivacao-verificacao-ciclo-01.md`](../../../docs/analysis/matriz-derivacao-verificacao-ciclo-01.md),
que substitui a conferência individual regra a regra: a correspondência
estrutural entre cada regra e os requisitos que ela materializa foi
verificada programaticamente, e cada regra aponta, no próprio corpo, os
identificadores correspondentes.

**Ele está encerrado.** As onze condições cumulativas de `okf/spec/ciclo.md`
se cumprem. A última pendência que as condições 3, 5 e 9 aguardavam —
`C1-R24`, o marco temporal do magistério, afetando as quatro regras do
inciso XVI — foi reavaliada em 05/08/2026: o art. 30, § 8º, inciso XVI, da
LCE 1.100/2021 restringe surdez permanente e anomalia da fala ao caso de
magistério sem instituir marco temporal autônomo para a aferição desse
vínculo, ao contrário do caput do mesmo parágrafo, que fixa expressamente o
marco do acometimento em relação à filiação. Presumir que a lei exigisse um
marco que ela não fixa seria decisão jurídica nova, não leitura do texto —
e a exigência real, a condição funcional do magistério, já estava
corretamente modelada no campo de seleção das quatro regras desde a issue
#121; só a moldura da pendência estava errada. A revisão de mérito da
própria matriz pela coordenação, que nenhuma verificação programática
substitui, tinha `C1-R24` e `C1-R32` como suas únicas decisões
substantivas pendentes (issue #123); ambas decididas, nenhuma linha da
matriz permanece classificada como pendência jurídica da coordenação.
Nenhuma das sessenta regras do Bloco C tem pendência material aberta.

`C1-R32` não é mais uma dessas pendências (RFC 0004, round 9): a derivação
da causa comum está concluída, as unidades correspondentes são
`estado_auditoria: concluida`, e a condição 9 está satisfeita quanto a essa
substituição. Desde a emenda do round 12 (2026-08-05), o que resta também
não impede, por si, a entrada na carga: `regra-0020` e `regra-0021` já gravam,
em produção, `integral: N` e `tipo_calculo: Proporcionalidade Dias` para as
mesmas hipóteses de causa comum, o que sustenta a presunção de que o
Sisprev já dispõe de mecanismo operacional para elas. A unidade sucessora de
`regra-0020` entra na carga de homologação com
`estado_implantacao: confirmada_com_ressalva`, levando a ressalva sobre se
`Proporcionalidade Dias` executa, para esta hipótese, a base composta do
art. 26 — média do art. 24, limitada pelo § 10, então proporcionalizada —
ou uma proporcionalidade nua; ela precisa ser resolvida em homologação
prática antes da ativação em produção, não antes da carga.

O que mantém quarenta dos sessenta destinos fora da carga é distinto e
posterior à auditoria: os componentes de `regra-0021` e `regra-0022` reúnem
também as vinte unidades da família sujeita ao regime de previdência
complementar, e o catálogo legado não tem valor de `tipo_calculo` que exprima
o teto do RGPS nem coluna que registre a opção do § 16 (`C1-R34`, `C1-R15`).
Como a troca de fonte operacional é atômica, retirar aquelas duas origens
antes da representação deixaria sem regra aplicável quem ingressou a partir
de 06/11/2018. Nenhuma dessas quarenta regras aguarda decisão jurídica.

O ato institucional **também não** faz parte do encerramento, e continua
sendo questão distinta: o catálogo legado segue vigente até que o IPERON
pratique a ativação — evento único, depois de concluídos os ciclos. Isso não
é pendência do Ciclo 1, mas não supre a pendência da própria auditoria
descrita acima.

As janelas históricas de invalidez — CF/88 original, EC 20, EC 41 e art. 6º-A —
ficaram **fora deste ciclo** e passaram ao [Ciclo 9](ciclo-09.md), que encerra a
sequência. Nelas não se forma direito novo depois dos
seus marcos finais, mas elas continuam fundamentando requerimento novo de quem
implementou os requisitos na sua vigência — e por isso vão depois da norma sob
a qual o direito se forma hoje, não antes. As
unidades já estão autoradas em `estado_auditoria: preview`; o trabalho feito
aqui é herança daquele ciclo, não trabalho a refazer.

As sete regras continuam listadas neste documento como **referências**: elas
foram analisadas aqui, e é contra elas que a fronteira da norma em vigor foi
desenhada.
