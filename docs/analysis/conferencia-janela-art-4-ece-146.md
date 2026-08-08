# Conferência — a janela do art. 4º da ECE 146/2021 nas 24 regras que o citam

- **Status**: conferência concluída; 7 correções de campo **propostas, não aplicadas**

> **Aplicação no Ciclo 9 (2026-08-08).** A conferência também resolve qual rol
> rege as propostas históricas preservadas: como a ECE 146 entrou em vigor em
> 14/09/2021 e a LCE 1.100 somente em 18/10/2021, o rol posterior não integra a
> legislação preservada. A proposta
> `invalidez-ec41-geral-doenca-catalogada` passou a vincular apenas os róis da
> LCE 228 e da LCE 432. Isso não aplica as sete correções do catálogo legado
> enumeradas abaixo nem altera estado institucional.

Nota: esta conferência ficou possível quando a transcrição pesquisável da ECE
146/2021 entrou no repositório (`fontes-oficiais/transcricoes/sapl-emenda_146.md`,
PR #52). O PDF original tem 10 caracteres extraíveis, então até então o art. 4º
só podia ser lido na imagem, sem cotejo. Nenhum campo de regra foi alterado
aqui: as correções de `data_direito_ate` mexem no que vai para o Sisprev e
dependem de decisão de quem coordena a auditoria.

## 1. O dispositivo, verbatim

> **Art. 4º** A concessão de aposentadoria ao servidor público vinculado ao
> Regime Próprio de Previdência Social e de pensão por morte a seus dependentes
> observará os requisitos e os critérios exigidos pela legislação vigente até a
> data de entrada em vigor desta Emenda Constitucional, **desde que sejam
> cumpridos até 31 de dezembro de 2024**, sendo assegurada a qualquer tempo.
>
> **Parágrafo único.** Os proventos de aposentadoria devidos ao servidor
> público a que se refere o caput e as pensões por morte devidas a seus
> dependentes serão calculados e reajustados de acordo com a legislação vigente
> até a data de entrada em vigor desta Emenda Constitucional, desde que os seus
> requisitos e critérios sejam atendidos até 31 de dezembro de 2024.

O art. 4º tem **uma função só**: preservar a legislação anterior à própria
ECE 146/2021, com prazo. O caput cuida dos requisitos de concessão; o parágrafo
único, do cálculo e do reajuste. Os dois trazem o mesmo prazo — 31/12/2024.

## 2. O que ele funda, e o que não funda

Cruzando com a semântica que a Q1 fechou
([`semantica-das-janelas-temporais.md`](semantica-das-janelas-temporais.md)):
**`DATA_DIREITO_ATE` é o prazo de implementação dos requisitos** — todos os
requisitos precisam estar completos até essa data.

Logo, **onde o art. 4º funda os requisitos de uma regra, `data_direito_ate`
deveria ser `31/12/2024`.**

**A armadilha que quase inverteu esta conferência.** A oração final do caput —
"sendo assegurada a qualquer tempo" — parece licenciar a sentinela
`31/12/2099`. Não licencia. Ela fala do momento da **concessão**: quem cumpriu
os requisitos até 31/12/2024 pode requerer depois, e o benefício é devido. O
prazo de 31/12/2024 é do **implemento dos requisitos**, que é precisamente o
que `data_direito_ate` grava. São dois eixos, e confundi-los deixaria nove
janelas erradas com aparência de fundamento textual.

## 3. O que o próprio catálogo já pratica

Das 24 regras que vinculam `ece-146-2021/art-4/original`, **12 já fecham em
31/12/2024** — e são todas de legislação anterior à EC 146:

| regras         | fundamento                        |
| -------------- | --------------------------------- |
| `0012`, `0013` | pensão, art. 40, § 7º da EC 41/03 |
| `0097`–`0100`  | art. 2º da EC 41/2003             |
| `0101`–`0104`  | art. 6º da EC 41/2003             |
| `0105`, `0106` | art. 3º da EC 47/2005             |

Todas com `data_direito_apos: 31/12/2003`. Ou seja: a leitura proposta na §2
**não é nova** — é a que o catálogo já aplica em metade dos casos. As 12
restantes são o desvio, não a regra.

## 4. As 12 que divergem

### 4.1 Sete com a janela a corrigir para `31/12/2024`

Em todas, o fundamento dos **requisitos** é legislação anterior à EC 146, e a
janela está gravada `31/12/2099`.

| regra          | fundamento dos requisitos                          | `data_direito` gravado  |
| -------------- | -------------------------------------------------- | ----------------------- |
| `0006`, `0007` | art. 40, § 1º, I, CF, red. EC 41/2003              | 31/12/2003 → 31/12/2099 |
| `0008`, `0009` | art. 6º-A da EC 41/2003, red. EC 70/2012           | 31/12/2003 → 31/12/2099 |
| `0032`         | art. 40, § 1º, II, CF, red. EC 88/2015 + LC 152/15 | 18/10/2021 → 31/12/2099 |
| `0039`, `0040` | art. 40, § 1º, III, "a" e § 5º, CF, red. EC 20/98  | 18/10/2021 → 31/12/2099 |

`0039`/`0040` são o caso mais explícito de todos, porque a própria
fundamentação separa os eixos: cita a EC 20/1998 "**quanto ao preenchimento dos
requisitos**" e a EC 41/2003 "**no que tange à fórmula de cálculo e reajuste**".
Requisitos por norma anterior à EC 146, com art. 4º invocado — o prazo de
31/12/2024 alcança.

`0032`, `0039` e `0040` têm ainda `data_direito_apos: 18/10/2021`, que é a data
de entrada em vigor da ECE 146/2021. Isso reforça a leitura em vez de
contrariá-la: a janela dessas regras é exatamente o período em que o art. 4º
garante a legislação anterior, e esse período **começa** com a EC 146 e
**termina** em 31/12/2024. Gravar `31/12/2099` abre um intervalo que o
dispositivo invocado não sustenta.

### 4.2 Duas com a janela provavelmente correta, e a citação supérflua

| regra          | fundamento                             | `data_direito` gravado  |
| -------------- | -------------------------------------- | ----------------------- |
| `0085`, `0086` | tempo de serviço anterior à EC 20/1998 | 01/01/1950 → 31/12/2099 |

Aqui é **direito adquirido puro**: `data_adm_ate: 16/12/1998`, requisitos
completados sob a redação original da CF/88, antes da EC 20/1998. Um direito já
adquirido em 1998 não é alcançado por prazo criado em 2021 — satisfaz
trivialmente o "até 31/12/2024" e não depende dele. A sentinela `31/12/2099`
está adequada, e o que sobra é a citação do art. 4º, que não funda critério
algum nessas duas.

A distinção com o §4.1 é fina e vale registrar: `0097`–`0100` também têm
`data_adm_ate: 16/12/1998` e **fecham** em 31/12/2024 — mas são *transição*
(art. 2º da EC 41/2003), não direito adquirido. Transição depende do prazo;
direito adquirido, não.

### 4.3 Três corretas, porque um marco anterior prevalece

| regra          | fecha em   | quem fecha                                |
| -------------- | ---------- | ----------------------------------------- |
| `0027`         | 03/12/2015 | LC 152/2015 (compulsória aos 75)          |
| `0091`, `0092` | 31/12/2003 | EC 41/2003 sucede a transição da EC 20/98 |

O art. 4º põe um teto em 31/12/2024; quando outra norma já fechou a janela
antes, o teto não se aplica. Nada a corrigir — `0027` mantém a pendência de um
dia já registrada na §3.1 da análise de janelas (03/12 versus 04/12/2015), que
é assunto de outra conferência.

## 5. Um achado colateral em `regra-0032`

O `nome` diz "Compulsória - Art. 40, §1º, II da CF **com redaçao da EC 103/19**
c/c art. 31 da **Lc nº 1.100/2021**". A `fundamentacao_proporcional` diz
"art. 40, § 1º, inciso II, da Constituição Federal, com redação dada pela
**Emenda Constitucional nº 88/2015**; em conformidade com a **Lei Complementar
nº 152/2015**".

São dois regimes diferentes: o nome aponta para a reforma de 2019 e a lei
estadual de 2021; a fundamentação, para a EC 88/2015 e a LC 152/2015. Um dos
dois está errado, e a diferença não é de forma — decide se a regra é de regime
novo (e então o art. 4º não deveria estar citado) ou de legislação anterior (e
então a janela fecha em 2024). Registrado como achado próprio.

## 6. O que fica proposto, e o que não foi feito

**Proposto** (edição em campo do Sisprev, dependente de decisão):

- `data_direito_ate: 31/12/2024` em `regra-0006`, `0007`, `0008`, `0009`,
  `0032`, `0039`, `0040` — sete regras.

**Registrado como achado, sem edição**:

- a citação supérflua do art. 4º em `0085`/`0086`;
- a divergência entre `nome` e fundamentação em `0032`.

**Não feito, de propósito**: nenhuma alteração de `data_direito_ate`,
`nome` ou `fundamentacao*`. A conferência produz a conclusão; a edição de campo
deployável é decisão de quem responde pelo catálogo.

**Fica de fora do escopo desta conferência** a pergunta de por que
`0032`/`0039`/`0040` abrem o direito em 18/10/2021 quando os requisitos são de
norma bem anterior. A leitura acima explica *o fechamento* da janela; a
abertura em 18/10/2021 é coerente com o art. 4º, mas convive com uma outra
hipótese — que a regra só passou a existir no catálogo com a EC 146 — que esta
conferência não testou.
