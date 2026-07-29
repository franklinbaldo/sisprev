# RFC 0011 — Sentinelas de data como conjunto declarado

- **Status**: proposta (2026-07-29). Nada implementado. Nenhuma `regra-*.md`,
  nenhum dispositivo e nenhum achado são autorados ou editados por esta RFC; o
  CSV derivado não muda uma célula. O que ela pede é **uma declaração única do
  conjunto das quatro sentinelas** e a correção de dois lugares onde a prosa
  atual diverge de si mesma e o site afirma o que não é o caso.
- **Depende de**:
  [RFC 0001](0001-criterios-de-validacao-das-regras.md) **P5** (a decisão de
  2026-07-17: sentinelas preservadas e **não interpretadas**) e P13.2 (o mapa
  normativo coluna ↔ chave);
  [levantamento das janelas temporais](../analysis/semantica-das-janelas-temporais.md)
  (a semântica confirmada de `ATE`/`APOS` e a fila de conferência dos 230
  limites não-sentinela); [RFC 0002](0002-selecao-explicavel-pos-anamnese.md)
  §4 (o simulador só exclui por critério confirmado).
- **Não-objetivo**: **dizer o que uma sentinela significa.** Se `31/12/2099`
  quer dizer "sem limite superior", e se `01/01/1900`/`01/01/1910`/`01/01/1950`
  são três grafias de um mesmo sentido, é a pergunta 4 da §5.3 do levantamento
  e continua **aberta** depois desta RFC. Também fora de escopo: migrar
  sentinela para `null` ou para campo próprio (a Q4 do RFC 0001 resolveu
  manter, para não quebrar o round-trip); criar coluna, alterar domínio de enum
  ou qualquer outra mudança no Sisprev; corrigir um limite de data (campo
  deployável, veículo é `Conjunto` proposto — §4 do levantamento).

## 0. O problema

O predicado "limite não-sentinela" já é **critério de auditoria em vigor**. A
spec da regra o usa para dizer o que se confere: "todo limite não-sentinela
deveria coincidir com uma data declarada pelos dispositivos que a regra cita"
([`docs/spec/regra.md`](../spec/regra.md), Elegibilidade temporal). O
levantamento das janelas temporais o usa para produzir a fila de conferência
inteira: 230 limites, 166 coincidentes, 64 não.

Esse predicado não está declarado em lugar nenhum. Ele existe em prosa, em
quatro lugares, e **dois deles discordam**:

| onde                                                                  | conjunto declarado                                                  |
| --------------------------------------------------------------------- | ------------------------------------------------------------------- |
| RFC 0001, P5 ("decisão 2026-07-17")                                   | `01/01/1910`, `01/01/1950`, `31/12/2099` — **três**                 |
| [levantamento](../analysis/semantica-das-janelas-temporais.md) §5.3.4 | `01/01/1900`, `01/01/1910`, `01/01/1950`, `31/12/2099` — **quatro** |
| `regra_schema.COLUMNS`, `semantica_vazio` das quatro colunas          | "sentinela — preservada, não interpretada (P5)"                     |
| `site/src/lib/parse-sisprev.ts`, nota de topo                         | "an empty date value is sentinela"                                  |

A divergência não é acadêmica: **o número publicado só fecha com o conjunto de
quatro**. Sobre a importação congelada, as quatro colunas × 112 linhas dão 448
limites; 218 são sentinela e **230 não são** — exatamente o total da §3 do
levantamento. Com o conjunto de três do P5 seriam 216 e 232. Um relatório do
repositório e a RFC normativa contam populações diferentes para o mesmo
critério, e nada acusa.

`01/01/1900` foi esquecido pelo motivo mais previsível: ocorre em **uma linha**
(`regra-0087`, nos dois campos `APOS`), contra 100 ocorrências de sentinela em
`DATA_ADM_APOS` no total. É a mesma `regra-0087` cujo `data_direito_ate` é
`01/12/2002`, item 10 da fila de conferência — a linha mais estranha do
catálogo é a que carrega a sentinela que o P5 não lista.

### 0.1 A confusão entre "vazio" e "sentinela", e onde ela chegou

`regra_schema.COLUMNS` declara, para as quatro colunas de data, que a
**semântica de vazio** é "sentinela — preservada, não interpretada (P5)". Mas
vazio não ocorre: as 448 células estão preenchidas, nas 112 linhas, na
importação congelada e no bundle de hoje. O que existe são **218 sentinelas em
células preenchidas**. A célula do mapa normativo descreve um caso que não
acontece e deixa sem descrição o caso que acontece em 49% dos limites.

Isso saiu do schema e chegou ao produto. A nota de topo de
`site/src/lib/parse-sisprev.ts` diz que "an empty date value is *sentinela —
preservada, não interpretada* (P5)", e o simulador diz ao usuário, em
`simulador.ts:177`, que "valor vazio é sentinela, não interpretado". **A única
frase que o site diz ao público sobre sentinelas é sobre um valor que não
existe no catálogo**, e ele não diz nada sobre os 218 que existem.

### 0.2 O simulador interpreta a sentinela hoje — na direção errada

`avaliarJanela` só considera uma janela não modelada quando **os dois limites
são vazios**. Como vazio não ocorre, esse ramo está morto e a sentinela entra
como limite genuíno. No universo do simulador (84 regras `simulavel: S` e
ativas), sobre a importação congelada:

| janela   | dois limites sentinela | um limite sentinela | nenhum |
| -------- | ---------------------- | ------------------- | ------ |
| admissão | 25                     | 55                  | 4      |
| direito  | 0                      | 62                  | 22     |

Para as **25** regras cuja janela de admissão é inteiramente convencional, o
motor hoje faz duas coisas que a RFC 0002 §4 proíbe em qualquer outro lugar:
pede ao requerente uma data que não pode mudar o resultado (`pendente`, se em
branco) e, se a data vier, escreve "Janela de admissão" em
`criteriosSatisfeitos` — uma **afirmação de critério satisfeito sobre uma
fronteira que o projeto decidiu não interpretar**. Não há exclusão errada: nada
de real cai antes de `01/01/1950`. O defeito é o oposto — confiança relatada
sobre nada.

Vale nomear a inversão, porque ela decide a §5: **hoje o simulador interpreta a
sentinela** (usa `01/01/1950` como piso de verdade). Tratá-la como "janela não
avaliada" **não** é interpretá-la como "sem limite" — é a leitura conservadora,
a única compatível com o P5: não conclui, não exclui, não credita critério.

## 1. O que o conjunto declara, e o que ele não declara

Declara **uma só coisa**: que estes quatro valores são os que a coordenação da
auditoria nomeou como sentinela na decisão de 2026-07-17, isto é, valores que
não pretendem nomear um marco. Nomear o conjunto é **forma**. Dizer o que os
membros significam é **mérito**, e continua aberto.

A constante é, portanto, **autorada** — registro de uma decisão, exatamente
como uma entrada de `dispositivos:`. Ela não deriva de nada e não pode: "este
valor não parece um marco legal" é conclusão jurídica, e produzir conclusões
jurídicas plausíveis por regra mecânica é precisamente o modo de falha que a
RFC 0008 documentou com nove erros reais.

Daí a consequência que mais importa nesta RFC: **`01/01/1969` fica fora**
(`regra-0003`, `data_direito_apos`, data anterior à própria CF/88). É suspeita
registrada — item 9 da fila de conferência —, e uma suspeita que entra no
conjunto vira, sem ato de ninguém, uma decisão de que aquele limite não é
critério. Entra quando alguém confirmar, por edição autorada, com achado.

## 2. A forma: um `StrEnum` em módulo puro

`scripts/sentinela.py`, puro, sem importar `bundle`/`concept` — mesmo lugar
arquitetural de `dispositivo_endereco.py`, e pelo mesmo motivo: quem define
forma não pode depender de quem carrega documento.

```python
class Sentinela(StrEnum):
    """Os quatro valores que a coordenação nomeou sentinela (P5, 2026-07-17).

    O valor de cada membro é a string **exatamente como gravada** — este
    módulo classifica o que está no catálogo, nunca substitui.
    """

    D_1900_01_01 = "01/01/1900 00:00"
    D_1910_01_01 = "01/01/1910 00:00"
    D_1950_01_01 = "01/01/1950 00:00"
    D_2099_12_31 = "31/12/2099 00:00"


def sentinela_de(valor: str) -> Sentinela | None:
    """A sentinela que `valor` é, ou `None`. Nunca levanta."""
```

Quatro escolhas, cada uma contra a alternativa que parece mais natural:

**`StrEnum`, e não `Enum` de `date` nem `frozenset`.** Um membro de `StrEnum` é
igual à string gravada (`Sentinela.D_2099_12_31 == "31/12/2099 00:00"`), então
nada no caminho de escrita muda e **a constante não pode virar uma
representação nova**. Um enum de `datetime.date` seria serializado por alguém,
algum dia, e o round-trip byte-idêntico com a planilha original morre em
silêncio — é o risco que a Q4 do RFC 0001 já avaliou ao decidir manter as
sentinelas como estão. O `frozenset` daria a checagem de pertinência e nada
mais: o enum dá o lugar único para a docstring, a enumeração que o gate da §3
precisa, e o estreitamento de tipo (`Sentinela | None`) que o `ty` confere.

**Nomes que não dizem nada.** É no nome do membro que a interpretação entra sem
pedir licença: `SEM_LIMITE_SUPERIOR` responderia a §5.3.4 num identificador, e
todo `if` que o lesse herdaria a resposta. `D_2099_12_31` é a data em ordem ISO
— derivável do valor, portanto incapaz de divergir dele, e sem nenhum
significado agregado.

**A hora é ignorada na classificação**, como já é ignorada em todo o projeto na
comparação de datas (nota de topo de `parse-sisprev.ts`); `sentinela_de` compara
a parte de data. Validar formato **não** é trabalho deste módulo — quem faz
isso é `_LEGACY_DATETIME_RE` no compilador.

**A função que este módulo não vai ter é `limite_valido()`.** Um limite
não-sentinela não é um limite correto: `15/12/1998` é não-sentinela e é o
candidato a erro de um dia da §3.1 do levantamento. O complemento de "sentinela"
é "valor a conferir", nunca "valor bom", e uma função com esse nome faria a fila
de conferência parecer resolvida.

Considerado e **descartado**: dar a cada membro um atributo `posicao`
(`inferior`/`superior`). A observação é verdadeira e útil — as três de piso
ocorrem só em colunas `APOS`, `31/12/2099` só em colunas `ATE` — mas ela é fato
sobre a importação, não parte da definição, e o lugar de um fato sobre a
importação é um teste (§3), não um campo que convida a `if posicao == "superior"`.

## 3. O gate: a constante amarrada ao dado congelado

Um teste em `tests/`, nenhum job de CI novo, nenhum detector novo. Três
asserções, todas sobre `data/raw/regras-sisprev.csv` — **imutável para
sempre**, portanto números que não envelhecem:

1. **Nenhum membro órfão**: cada um dos quatro ocorre ao menos uma vez na
   importação. Um membro que ninguém usa é conjunto que cresceu por palpite —
   e foi por não ter esta asserção que `01/01/1900` ficou fora do P5.
2. **A posição observada se mantém**: as três de piso só em `APOS`, `31/12/2099`
   só em `ATE`. Se uma importação futura quebrar isso, queremos saber.
3. **218 sentinelas, 230 limites não-sentinela**, dos 448. É o número que a §3
   do levantamento publica; asseverado contra a importação congelada ele nunca
   fica desatualizado, e uma edição de data no bundle vivo não o falseia.

Sobre o bundle vivo, deliberadamente **nada** é gatilhado. Uma regra não fica
inválida por ter sentinela — 49% dos limites têm.

## 4. As duas correções de prosa que isto fecha

Com o conjunto declarado, dois textos passam a poder apontar para ele em vez de
repeti-lo:

1. **RFC 0001, P5** ganha `01/01/1900` e a referência ao módulo. O parágrafo da
   decisão de 2026-07-17 fica como está no mérito; muda a lista.
2. **`regra_schema.COLUMNS`**, `semantica_vazio` das quatro colunas de data:
   hoje descreve o vazio que não ocorre. Passa a dizer que vazio não ocorre nas
   112 linhas e a apontar o módulo para o caso que ocorre. **Consequência a
   registrar**: essa célula é impressa por `render_schema_table()` no doc
   `Dataset`, então a mudança regenera `okf/regras-sisprev/regras-sisprev.md`
   — artefato derivado coberto pelo gate `derived-csv-in-sync`. O CSV derivado
   não muda; nenhuma coluna, nenhuma célula de regra.

Nenhuma das duas é achado. Um achado descreve defeito do catálogo contra a lei
e nomeia regras afetadas; aqui o que divergiu foram **dois documentos nossos**
sobre um predicado nosso, e o veículo disso é esta RFC.

## 5. O porte TypeScript e a correção do simulador

`site/src/lib/sentinela.ts`, testado, com o Python seguindo autoridade — mesma
divisão de `dispositivo_endereco.py` / `dispositivo.ts` (é o Python que derruba
o commit).

**`formato.ts` não muda.** A ficha continua imprimindo `31/12/2099` como a data
que está escrita. A regra 1 daquele módulo — nunca interpretar o que o projeto
decidiu não interpretar — é justamente o que esta RFC preserva.

**`simulador.ts` muda, e o resultado exibido muda com ele.** `avaliarJanela`
passa a tratar limite sentinela como limite ausente para efeito de avaliação —
não como "sem limite", e sim como "fronteira que este projeto não interpreta":

- **os dois limites sentinela** → `nao_modelada`. Sai a pergunta inútil ao
  requerente, sai o critério creditado sem base. São 25 regras na janela de
  admissão.
- **um limite sentinela** → avalia o lado real (exclui se o fato o violar, que
  é o único veredito que o motor tem direito de dar) e devolve `pendente` no
  resto, porque metade de uma janela não confirma a janela. São 55 regras na
  admissão e 62 no direito, e para elas o resultado troca "Janela de admissão
  satisfeita" por uma pendência escrita. **É um resultado pior de ler e mais
  verdadeiro**, e é o efeito principal desta RFC no produto.
- a mensagem de `simulador.ts:177` deixa de falar de "valor vazio" e passa a
  dizer o que é o caso: o limite é valor convencional do catálogo, não
  interpretado.

Opcional, e explicitamente separado porque toca página publicada: marcar na
ficha da regra, ao lado das quatro datas, quando o valor é sentinela — com a
frase que não interpreta ("valor convencional do catálogo, não interpretado"),
nunca com "sem limite". Dizer "o projeto não decidiu nada sobre este valor" é
verdadeiro e é exatamente o que quem lê uma fila de conferência precisa saber.

## 6. Fases

- **Fase 0** — `scripts/sentinela.py`, o teste da §3, as duas correções de
  prosa da §4. Não altera comportamento de nada.
- **Fase 1** — `site/src/lib/sentinela.ts` + a correção do simulador (§5).
  Altera resultado exibido; PR própria, para que o diff de comportamento seja
  revisável isolado.
- **Fase 2 (opcional)** — a marcação na ficha.
- **Nunca, sem decisão de coordenação** — nome de membro que signifique algo,
  `limite_valido()`, `01/01/1969` no conjunto, migração para `null`.

## 7. O que esta RFC não faz, e por que é tentador achar que faz

Não responde §5.3.4 (o que as sentinelas significam) nem §5.3.1–3. Não fecha
nenhum item da fila de conferência da §5.2 do levantamento: `15/12/1998`,
`01/01/2004`, `31/12/2024` e os outros oito continuam pendentes de resposta
humana, e o conjunto declarado não move nenhum deles um milímetro — ele só faz
com que a pergunta "quantos limites estão na fila?" tenha uma resposta única.

Não cria o detector "limite sem marco autorado" (issue #38). O conjunto é
**pré-requisito** dele: sem predicado declarado, o detector escolheria sozinho a
população que acusa. Mas construí-lo continua sendo a decisão que o CLAUDE.md
manda justificar contra a alternativa de conferir e escrever — e a §3 do
levantamento já é a fila, escrita à mão, com o gabarito de marcos ainda parcial
(7 das 16 normas sem `vigencia_inicio`).

## 8. Referências

- RFC 0001, **P5** e **Q4**,
  [`docs/rfc/0001-criterios-de-validacao-das-regras.md`](0001-criterios-de-validacao-das-regras.md)
- RFC 0002 §4 (só excluir por critério confirmado),
  [`docs/rfc/0002-selecao-explicavel-pos-anamnese.md`](0002-selecao-explicavel-pos-anamnese.md)
- RFC 0008 (por que uma conclusão jurídica não se deriva de regra mecânica),
  [`docs/rfc/0008-traducao-sem-perdas-entre-os-dois-esquemas.md`](0008-traducao-sem-perdas-entre-os-dois-esquemas.md)
- Levantamento das janelas temporais, §3 (a fila), §5.2 (as 11 datas sem
  marco), §5.3.4 (o significado das sentinelas),
  [`docs/analysis/semantica-das-janelas-temporais.md`](../analysis/semantica-das-janelas-temporais.md)
- Spec da regra, "Elegibilidade temporal",
  [`docs/spec/regra.md`](../spec/regra.md)
