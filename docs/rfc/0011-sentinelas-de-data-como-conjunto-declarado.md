# RFC 0011 — Sentinelas de data como conjunto declarado

- **Status**: **implementada** (2026-07-29), as três fases.
  `scripts/sentinela.py` declara o conjunto, `tests/test_sentinela.py` o amarra
  à importação congelada, `site/src/lib/sentinela.ts` é o porte, o simulador
  deixou de usar sentinela como fronteira de verdade e a ficha e o relatório
  marcam o valor sem interpretá-lo (`NOTA_DE_SENTINELA`). Nenhuma `regra-*.md`,
  nenhum dispositivo e nenhum achado foram autorados ou editados; o CSV derivado
  não mudou uma célula.
- **Uma coisa a mais do que o proposto**: a "# Schema" publicada no doc
  `Dataset` não tinha gate contra `regra_schema.COLUMNS` — a tabela é escrita
  por `csv_to_okf.py`, bootstrap de uma vez só, enquanto `COLUMNS` continua se
  movendo. A correção da §4 ia deixar o doc afirmando a versão antiga em
  silêncio, então a §4 trouxe o gate junto
  (`test_schema_table_do_doc_dataset_em_sincronia_com_columns`).
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

> Esta seção descreve o estado **anterior** às fases 0 e 1, e fica no presente
> como foi escrita: é o diagnóstico que a RFC precisou fazer, e apagá-lo tiraria
> a razão de cada decisão das seções seguintes. O que mudou está no Status, e
> cada correção diz onde encostou.

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

Um teste em `tests/` (`test_sentinela.py`), nenhum job de CI novo, nenhum
detector novo. As asserções sobre o dado são todas contra
`data/raw/regras-sisprev.csv` — **imutável para sempre**, portanto números que
não envelhecem:

1. **Nenhum membro órfão**: cada um dos quatro ocorre ao menos uma vez na
   importação. Um membro que ninguém usa é conjunto que cresceu por palpite —
   e foi por não ter esta asserção que `01/01/1900` ficou fora do P5.
2. **A posição observada se mantém**: as três de piso só em `APOS`, `31/12/2099`
   só em `ATE`. Se uma importação futura quebrar isso, queremos saber.
3. **218 sentinelas, 230 limites não-sentinela**, dos 448. É o número que a §3
   do levantamento publica; asseverado contra a importação congelada ele nunca
   fica desatualizado, e uma edição de data no bundle vivo não o falseia.
4. **Vazio não ocorre** em nenhuma das 448 células — é esta asserção que
   sustenta a célula `semantica_vazio` corrigida na §4.
5. **`01/01/1969` ocorre e não é membro**: a exclusão deliberada da §1 fica
   escrita como teste, para que incluí-lo seja uma edição visível, com achado,
   e não um `+ 1` numa lista.
6. **O porte TS declara exatamente os mesmos membros** — nas suas duas
   declarações (união de tipo e array), na mesma ordem.

A asserção 6 nasceu de um achado do review da PR #58, e ela é a que faltava:
sem ela a autoridade do Python era **nominal**. Dava para acrescentar ou
remover uma sentinela no `sentinela.py`, manter o CI verde do lado Python, e
deixar simulador, ficha e relatório trabalhando com o conjunto antigo — isto é,
recriar em código a divergência entre duas listas que é a razão de existir
desta RFC, com a agravante de estar dentro dela. A comparação roda no pytest, e
não no vitest, porque a autoridade é quem derruba o commit; e ela **falha** se o
porte mudar de forma a ponto de o padrão não casar, porque um gate de paridade
que passa quando não encontra o que comparar é pior que gate nenhum.

Sobre o bundle vivo, deliberadamente **nada** é gatilhado. Uma regra não fica
inválida por ter sentinela — 49% dos limites têm.

## 4. As duas correções de prosa que isto fecha

Com o conjunto declarado, dois textos passam a poder apontar para ele em vez de
repeti-lo:

1. **RFC 0001, P5** ganha `01/01/1900` e a referência ao módulo. O parágrafo da
   decisão de 2026-07-17 fica como está no mérito; muda a lista.

2. **`regra_schema.COLUMNS`**, `semantica_vazio` das quatro colunas de data:
   descrevia o vazio que não ocorre. Passa a dizer que vazio não ocorre e a
   apontar o módulo para o caso que ocorre. O CSV derivado não muda; nenhuma
   coluna, nenhuma célula de regra.

   **A consequência é pior do que esta RFC previu na proposta**, e é por isso
   que a implementação trouxe um gate a mais. A célula é impressa por
   `render_schema_table()` na "# Schema" do doc `Dataset`, mas quem escreve
   aquele doc é `csv_to_okf.py` — **bootstrap de uma vez só, que se recusa a
   rodar de novo**. `gerar_indices.py` não o regenera, e nenhum teste comparava
   a tabela publicada com `COLUMNS`: a correção ia deixar o doc do bundle (e a
   página que o publica) afirmando a versão antiga, calada. A tabela foi
   atualizada e ganhou a asserção que faltava
   (`test_schema_table_do_doc_dataset_em_sincronia_com_columns`, comparando
   célula a célula para não depender do alinhamento do mdformat). É a mesma
   família de defeito que motivou esta RFC — declaração única sem gate volta a
   divergir —, encontrada dentro dela.

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

- **os dois limites sentinela** → nenhum critério creditado, nenhuma data
  pedida ao requerente (ela não pode mudar o resultado), e **uma pendência
  escrita** dizendo que a janela não foi avaliada. São 25 regras na janela de
  admissão. A proposta dizia `nao_modelada` aqui, isto é, silêncio; ficou
  pendência, porque `nao_modelada` significa "a regra não modela esta janela" e
  estas modelam — o que não há é limite avaliável. Sair calado faria a ficha do
  requerimento parecer conferida onde não foi, e `fatosPendentes` já carrega
  pendência de catálogo (o sexo vazio da Q10), não só fato do requerente.
- **um limite sentinela** → avalia o lado real (exclui se o fato o violar, que
  é o único veredito que o motor tem direito de dar) e devolve `pendente` no
  resto, porque metade de uma janela não confirma a janela. São 55 regras na
  admissão e 62 no direito, e para elas o resultado troca "Janela de admissão
  satisfeita" por uma pendência escrita. **É um resultado pior de ler e mais
  verdadeiro**, e é o efeito principal desta RFC no produto.
- a mensagem que falava de "valor vazio" passa a dizer o que é o caso, e as
  **duas causas de limite não avaliável ficam distintas**: "não está preenchido
  no catálogo" e "é valor convencional do catálogo (sentinela), não
  interpretado". Vazio e sentinela eram a mesma frase; era daí que vinha a
  confusão da §0.1.
- **a assinatura de indistinguibilidade também passa pelo mesmo filtro**
  (`serializarLimite`). Ela existe para dizer o que este motor consegue
  distinguir, e ele não distingue duas regras por qual sentinela cada uma usou
  de piso (`01/01/1910` vs `01/01/1950`, que é uma diferença real no catálogo:
  27 regras contra 2). Com o valor bruto na assinatura, um par indistinguível
  com resultado candidato diferente escaparia do sinal da RFC 0002 §4 por uma
  diferença que o motor não usa. Isto só **acrescenta** pendência; nunca exclui
  regra.
- **o fixture dos testes usava `01/01/1910` como piso** — o mesmo mal-entendido
  do motor, reproduzido justamente onde deveria ser flagrado. Passou a usar
  marcos reais, e as sentinelas ganharam testes próprios.

## 5.1 Fase 2 — a marcação na ficha (e no relatório)

`NOTA_DE_SENTINELA`: *"sentinela: valor convencional do catálogo, não
interpretado"*, ao lado da data, que continua impressa exatamente como está
gravada. Dizer "o projeto não decidiu nada sobre este valor" é verdadeiro e é o
que quem lê uma fila de conferência precisa saber; dizer "sem limite" seria
responder §5.3.4 por legenda de tabela, e **há teste proibindo a frase de contê-la**.

Duas decisões de onde:

- **Mora em `regra-fields.ts`, não em `formato.ts`.** Aquele módulo converte
  *formato* — "este valor é uma fronteira convencional" é semântica da regra, não
  da string. A marcação é por `formato: "data"`, com teste amarrando que os
  campos `data` são exatamente as quatro colunas de limite, para não manter uma
  segunda lista de chaves que possa divergir.
- **Alcança o relatório da PGE junto**, porque a ficha e o capítulo compartilham
  `campoFormatado`. Não foi acidente aceito: é onde a marcação pesa mais — num
  anexo impresso, `31/12/2099` sem ressalva é lido como limite real por quem se
  manifesta sobre a regra, e o documento existe para colher manifestação. Custa
  **2 páginas em 1.094** (medido: mesmo `dist`, com e sem a regra de estilo), e
  sai sem cor própria, como todo o resto do impresso.

No índice do Pagefind a nota entra com `data-pagefind-ignore`, pela mesma regra
do valor bruto e dos rótulos: a mesma frase em 100 fichas não recorta nada.

## 6. Fases

- **Fase 0** (feita) — `scripts/sentinela.py`, o teste da §3, as duas correções
  de prosa da §4. Não altera comportamento de nada.
- **Fase 1** (feita) — `site/src/lib/sentinela.ts` + a correção do simulador
  (§5). Altera resultado exibido.
- **Fase 2** (feita) — a marcação na ficha e no relatório (§5.1). Era "opcional"
  na proposta e foi pedida em seguida; o que a proposta acertou foi separá-la,
  porque ela é a única fase que muda **página publicada e documento assinado**.
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
