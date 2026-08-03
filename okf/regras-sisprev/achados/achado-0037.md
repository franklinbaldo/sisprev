---
type: Achado
id: achado-0037
nome: Quatro regras de policial carregam as duas alíneas da LC 51/1985 na mesma célula de fundamentação, e nas femininas a masculina vem primeiro
situacao: aberto
severidade: informativo
verificacao: manual
natureza: juridica
regras_afetadas:
  - /regras/regra-0072.md
  - /regras/regra-0073.md
  - /regras/regra-0111.md
  - /regras/regra-0112.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

O art. 1º, II da LC 51/1985, na redação da LC 144/2014, tem duas alíneas — uma
por sexo:

> **a)** após **30** (trinta) anos de contribuição, desde que conte, pelo
> menos, **20** (vinte) anos de exercício em cargo de natureza estritamente
> policial, **se homem**;
>
> **b)** após **25** (vinte e cinco) anos de contribuição, desde que conte,
> pelo menos, **15** (quinze) anos de exercício em cargo de natureza
> estritamente policial, **se mulher**.

Em `regra-0072`, `regra-0073`, `regra-0111` e `regra-0112` o campo
`fundamentacao_integral` é **uma célula com duas articulações separadas por
`|`** — a primeira citando a alínea "a" e terminando em "regra transitória
homem", a segunda citando a alínea "b" e terminando em "regra transitória
mulher". As quatro têm `sexo` gravado:

| regra        | `sexo`    | alíneas citadas na célula | ordem no texto        | `dispositivos:` vincula |
| ------------ | --------- | ------------------------- | --------------------- | ----------------------- |
| `regra-0072` | MASCULINO | "a" **e** "b"             | homem, depois mulher  | só `al-a`               |
| `regra-0073` | FEMININO  | "a" **e** "b"             | **homem**, depois ela | só `al-b`               |
| `regra-0111` | MASCULINO | "a" **e** "b"             | homem, depois mulher  | só `al-a`               |
| `regra-0112` | FEMININO  | "a" **e** "b"             | **homem**, depois ela | só `al-b`               |

O texto deployável de uma regra masculina afirma também os 25/15 da alínea
feminina, e o de uma regra feminina afirma também os 30/20 da masculina. Nas
duas femininas a articulação que **não** é delas é a que aparece primeiro na
célula.

# Evidências

O texto das duas alíneas foi conferido na **publicação oficial compilada** do
Planalto arquivada localmente
(`fontes-oficiais/arquivos/planalto-lcp51.htm`, decodificada em cp1252 — o
arquivo não é UTF-8). O inciso II tem **exatamente** duas alíneas, ambas com a
nota inline "(Incluído pela Lei Complementar n° 144, de 2014)", e a alínea "a" é
a masculina. A conferência não depende, portanto, apenas da transcrição do
corpus: os dois dispositivos autorados
(`lc-51-1985/art-1-inc-ii-al-a/lc-144-2014` e `.../al-b/...`) reproduzem a
fonte.

**O empacotamento vem da importação, não de edição de auditoria.** As quatro
linhas de `data/raw/regras-sisprev.csv` já traziam uma ocorrência de `|` em
`FUNDAMENTACAO_INTEGRAL` e o mesmo `NOME` — nada aqui foi produzido depois.

**O vínculo é mais estreito do que o campo que ele espelha.** Um item de
`dispositivos:` afirma *"a fundamentação desta regra cita este dispositivo"*
(RFC 0008, [`docs/spec/dispositivo.md`](../../../docs/spec/dispositivo.md)). Nas
quatro, a fundamentação cita **as duas** alíneas e o vínculo declara **uma** —
a que casa com o `sexo` gravado. Quem vinculou escolheu a metade aplicável, o
que é a leitura útil, mas o resultado é que a união achatada de `dispositivos:`
não reflete o que o campo diz. Nenhum vínculo é proposto aqui, e a razão é a
mesma nas duas direções: acrescentar `al-b` à `regra-0072` formalizaria
justamente a metade que não deveria estar no texto, e remover a que está
apagaria a única leitura correta que a regra tem.

**O `P9_SEXO_FUNDAMENTACAO` é cego nas quatro, e por um motivo novo.** O
detector exige a menção **exclusiva** do outro sexo — `sexo == MASCULINO and has_mulher and not has_homem` (`scripts/detectors/co_ocorrencias.py`). Uma célula
que traz as duas articulações menciona os dois sexos, então a condição não pode
disparar. É um segundo ponto cego, distinto do que o `achado-0017` descreve
(ali o campo `sexo: AMBOS` neutraliza o detector): aqui é a **completude** do
texto errado que o silencia. Quanto mais a célula carrega, menos o detector vê.

**A mesma célula está em quatro regras fora do alcance desta conferência.**
`regra-0074`, `regra-0075`, `regra-0076` e `regra-0077` — as quatro
`sexo: MASCULINO`, byte a byte idênticas entre si (`achado-0007`) — trazem o
mesmo empacotamento, caractere a caractere. São **oito** regras do catálogo com
esta forma; `regras_afetadas` lista só as quatro auditadas aqui para não
reivindicar o que outra conferência está examinando. O registro fica para não
perder a extensão real.

# Relação com o que já está registrado

O `achado-0017` descreve o defeito **espelhado**: em `regra-0078`, `regra-0079`
e `regra-0084` a célula traz **só** a alínea feminina, e em duas delas o `sexo`
não é o dela. É o mesmo lapso — o desdobramento por sexo não chegou à
fundamentação — em direção oposta: lá o par masculino perdeu a sua alínea; aqui
nenhuma das duas perdeu nada, as duas ficaram com tudo. A recorrência da forma
em oito regras é ela própria informação, como o `achado-0016` já registrou para
as regras de professor.

O [`CLAUDE.md`](../../../CLAUDE.md) registra o empacotamento por `|` como forma
conhecida e dá `regra-0021`/`0022` como o caso em que a divisão **não tem
coluna** (causa da incapacidade, Q6) — e é por isso que ali nada é vinculado.
Aqui a divisão é por **`sexo`**, que é coluna, está preenchida nas quatro e é
critério aferido confirmado ([`docs/spec/regra.md`](../../../docs/spec/regra.md),
"O que individua uma regra"). Logo isto **não** é lacuna de schema: a distinção
é expressável, e está expressa — em duplicidade com um texto que a ignora.

# Consequência prática

O dano é sobre o **documento entregue** e sobre a triagem humana, não sobre a
seleção automática. As quatro são `simulavel: S`, e em regra simulável o motor
não lê a fundamentação — nem teria com que conferi-la: tempo de contribuição e
tempo de exercício policial não têm coluna no cadastro. O que sai errado é a
justificativa: o ato que aposenta um homem afirma, no mesmo campo, o requisito
de 25/15 que a lei reserva à mulher.

Nada aqui afirma que o motor afira 25/15 em vez de 30/20 — a distinção é a
mesma do `achado-0010` e do `achado-0017`.

# Questão a investigar

1. **Se a correção é partir a célula em duas.** É a leitura mais simples: cada
   regra fica com a articulação do seu próprio `sexo`, e o resultado é o que a
   `regra-0078` já teria se o par tivesse sido desdobrado por inteiro (a
   regra proposta `policial-civil-voluntaria-masculino` é o precedente da
   forma, para outra regra). `FUNDAMENTACAO_INTEGRAL` é campo **deployável**:
   editá-lo é alterar o produto, e a decisão é de quem responde por ele — não
   do auditor.

2. **Se o `|` significa "duas regras numa linha" em vez de "um texto com duas
   metades".** As seis regras de `0072` a `0077` e o par `0111`/`0112` carregam
   a mesma célula, e nelas o `sexo` já separa o que a célula ainda junta. Se a
   intenção da importação foi guardar as duas redações num campo único antes do
   desdobramento por sexo, o empacotamento é resíduo — e aí a resposta ao item
   1 é imediata. Não há no repositório documento que responda isso; é pergunta
   ao IPERON.

3. **Se `dispositivos:` deve seguir o campo ou o `sexo`.** Hoje segue o `sexo`,
   contra a definição do vínculo. Resolvido o item 1, a questão desaparece: o
   campo passa a citar uma alínea só e as duas leituras coincidem. Enquanto não
   for, a divergência fica registrada aqui e **não** é corrigida no
   frontmatter, porque corrigi-la nos termos da definição pioraria o registro.
