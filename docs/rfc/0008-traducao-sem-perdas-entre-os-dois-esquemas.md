# RFC 0008 — Tradução sem perdas entre o esquema auditado e o do Sisprev

- **Status**: proposta (2026-07-29). **Especificação revisável, sem
  implementação.** Não edita nenhum `regra-*.md`, não altera o schema
  deployável, o CSV derivado, os dispositivos, os achados, os detectores, o
  simulador, o site nem os workflows. Entrega o desenho da fronteira entre os
  dois esquemas e a medição do estado atual contra ele.
- **Parte de / depende de**:
  [RFC 0001](0001-criterios-de-validacao-das-regras.md) (P13.2, o mapa
  normativo coluna ↔ chave; P3/P4, dispositivos e citações; P14, achados) e
  [RFC 0004](0004-schema-enriquecido-e-compilador-para-o-sisprev.md), cujo
  compilador já resolve metade deste problema para o catálogo auditado —
  `_checar_contrato_legado` é a tradução A → B checada contra os tipos que o
  alvo legado declara. Esta RFC generaliza aquela checagem para o catálogo
  legado e nomeia o que ela ainda não cobre.
- **Não-objetivo**: alterar `data/raw/regras-sisprev.csv`, imutável para
  sempre; alterar qualquer uma das 27 colunas do Sisprev — criar, remover,
  renomear ou estender domínio de enum continua fora de escopo; autorar
  qualquer regra, dispositivo ou achado; responder Q6 (causa da incapacidade)
  ou Q12 (fluxo institucional).

## 0. O problema

O repositório tem dois esquemas e sabe disso. O do **Sisprev** são as 27
colunas de `data/raw/regras-sisprev.csv` — congeladas, fora de escopo,
imutáveis por decisão institucional e não por conveniência. O **nosso** é o
frontmatter dos `regra-*.md`, onde a auditoria trabalha. O `regra_schema.COLUMNS`
é a tradução entre eles, e ela funciona: reescrever uma chave do nosso lado sem
atualizar o mapa quebra o `test_roundtrip.py`, que reconstrói o CSV e o compara
com o congelado. Essa metade está provada a cada commit.

O que não está dito em lugar nenhum é **o outro lado da fronteira**. Hoje o
nosso esquema já tem chaves que o Sisprev não tem coluna para receber. Elas não
viajam, e está certo que não viajem — `dispositivos:` é infraestrutura de
auditoria, não campo de produto. Mas nada no repositório declara isso. Uma
chave nova de frontmatter simplesmente passa a existir, e o repositório não tem
como distinguir duas afirmações que significam coisas opostas:

> "este campo é nosso e deliberadamente não viaja"

> "este campo deveria virar coluna e alguém esqueceu de mapear"

As duas produzem exatamente o mesmo estado em disco: uma chave presente no
frontmatter e ausente do `COLUMNS`. **A perda é correta e é silenciosa**, o que
a torna indistinguível de um esquecimento. É a mesma classe de problema que a
RFC 0001 já resolveu para as colunas — só que do lado que ninguém mapeou,
porque quando o mapa foi escrito não havia nada do lado de cá.

Isso deixou de ser hipotético. O conjunto não-viajante tem 4 chaves hoje e três
delas são identidade OKF; a única substantiva, `dispositivos:`, chegou depois do
mapa. E ele vai crescer: `status_auditoria`, `atos_validacao` e `status_regra`
estão especificados no schema e populados em **zero** das 112 regras. Quando a
primeira regra for revisada, três chaves novas entram do nosso lado de uma vez,
e nada vai perguntar para onde elas vão.

## 1. A fronteira, medida

31 chaves distintas no frontmatter das 112 regras. 27 traduzidas, 4 não.

| Chave              | Destino                 | Declarado onde         |
| ------------------ | ----------------------- | ---------------------- |
| as 27 do `COLUMNS` | coluna do Sisprev       | `regra_schema.COLUMNS` |
| `type`             | não viaja (OKF)         | em lugar nenhum        |
| `id`               | não viaja (identidade)  | em lugar nenhum        |
| `row_index`        | não viaja (procedência) | em lugar nenhum        |
| `dispositivos`     | não viaja (P3/P4)       | em lugar nenhum        |

Especificados no schema e ainda não populados — entram do lado não-viajante
assim que a primeira regra transitar de estado:

| Chave              | Presente em | Origem       |
| ------------------ | ----------- | ------------ |
| `status_auditoria` | 0/112       | RFC 0001, P7 |
| `atos_validacao`   | 0/112       | RFC 0001, P7 |
| `status_regra`     | 0/112       | P2.1         |

A assimetria entre as duas direções é real e não é defeito:

- **Sisprev → nosso** é total e provado. As 27 colunas entram na importação, o
  round-trip devolve o CSV byte a byte idêntico ao congelado. Nada a fazer.
- **Nosso → Sisprev** é total sobre as 27 e **deliberadamente parcial** sobre o
  resto. É essa parcialidade que precisa deixar de ser implícita.

"Sem perdas" nesta RFC não quer dizer que tudo viaja. Quer dizer que **nada se
perde por acidente**: toda chave ou alcança uma coluna, ou está declarada como
nossa, e não existe terceira categoria.

## 2. O princípio: toda chave tem um destino declarado

Uma única regra, e ela é mecanicamente verificável:

> Toda chave de frontmatter de um `regra-*.md` tem exatamente um destino
> declarado — uma coluna do Sisprev, **ou** o registro dos campos próprios.
> Chave em nenhum dos dois é erro. Chave nos dois é erro.

O que isso compra é modesto e concreto: renomear `atualmente_no_sistema` para
`status_operacional` continua livre, porque o destino é declarado no
`ColumnSpec` e a coluna não se move — foi exatamente o que a PR #41 fez, e o
cabeçalho do CSV derivado saiu idêntico ao do `main`. Mas **acrescentar** uma
chave passa a exigir dizer para onde ela vai. Hoje não exige, e é por isso que
`dispositivos:` está há um refactor inteiro do lado de cá sem nenhum documento
registrando que ele não deve chegar ao Sisprev.

Isso também torna explícito o que a RFC 0004 já assume. O compilador do
catálogo auditado projeta uma unidade nas colunas legadas e falha fechado se o
valor projetado não é um que o alvo aceitaria (`P_COMPILA_VALOR_INVALIDO`,
`P_COMPILA_DATA_INCOERENTE`, ...). Ele só consegue fazer isso porque sabe quais
são as colunas de destino. O catálogo legado nunca teve a mesma checagem porque
nunca precisou — suas chaves *eram* as colunas, por construção. A partir do
momento em que uma chave nossa deixa de ser o slug de uma coluna, precisa.

## 3. O registro dos campos próprios

Um segundo tuple ao lado do `COLUMNS`, na mesma forma e no mesmo módulo:

```python
@dataclass(frozen=True)
class CampoProprio:
    """Uma chave do esquema auditado que deliberadamente não alcança o Sisprev."""

    frontmatter_key: str
    papel: str          # o que ela faz do nosso lado
    motivo: str         # por que não viaja
```

O `motivo` não é prosa decorativa: ele é a diferença entre "o Sisprev não tem
onde pôr isto" e "isto é dado de auditoria que não deve ser deployado". As duas
justificam não viajar, mas só a primeira vira pedido de coluna nova ao IPERON
algum dia. Registrar qual é qual agora é mais barato do que reconstruir a
intenção depois.

O registro é declarativo e não muda nenhum dado. `type`, `id` e `row_index`
entram como identidade e procedência; `dispositivos` entra como infraestrutura
de auditoria; as três chaves do P7 entram quando forem populadas, ou já entram
agora, dado que o schema as especifica.

## 4. A consequência: a citação sai do regex

`FUNDAMENTACAO`, `FUNDAMENTACAO_PROPORCIONAL` e `FUNDAMENTACAO_INTEGRAL` são as
colunas 27, 20 e 22 — **do Sisprev**. Viajam. Chegam ao documento do servidor.
`dispositivos:` é nosso e não viaja. A tradução entre os dois é hoje feita ao
contrário do que a fronteira manda: em vez de derivar a coluna a partir da
chave, o repositório **lê a coluna com expressão regular** para adivinhar a
chave.

Isso não é uma imperfeição de conveniência. O `P4_REDACAO_INEXISTENTE` é
**camada 2** — exige achado — e a conclusão dele é *"esta regra faz citação
legal falsa"*, sobre campo deployable. A única acusação automática do
repositório é derivada de parse de prosa. O leitor foi construído com cuidado e
tem 9 misatribuições corrigidas em teste de regressão contra o corpus real,
justamente porque cada uma delas escreveria uma citação legal plausível e
errada. O cuidado é evidência do problema, não solução dele.

### 4.1 O vazio de hoje é transitório, não estrutural

A leitura tentadora é que `dispositivos:` **não caberia** para o trabalho do
detector, porque `check_p3_dispositivos` exige que toda entrada resolva para um
dispositivo autorado, enquanto a acusação é sobre uma redação que não existe.
É verdade que o campo não expressa isso. Não é verdade que isso seja um limite
do desenho.

O catálogo está em construção. O vazio entre a prosa e o vínculo não existe
porque o vínculo seja incapaz — existe porque a transcrição não terminou.
Medido: 106 das 112 regras já têm `dispositivos:`, somando 461 entradas, todas
nomeando norma, endereço e redação sem ambiguidade. Faltam 7 transcrições e 6
regras. **Conforme isso fecha, `dispositivos:` passa a ser o registro completo
do que cada regra cita**, e o vazio que hoje o leitor mede é a lista de tarefas
que o fecha, não um buraco permanente no esquema.

O que sobra depois de fechado — uma citação a redação que provadamente nunca
existiu — não é entrada de catálogo. É **achado**, escrito à mão, e já é: os
`achado-0011`, `achado-0012` e `achado-0013` são exatamente esses registros. O
princípio da autoria humana da RFC 0001 diz que conclusão é ato humano, e uma
acusação de citação legal falsa é a conclusão mais forte que este repositório
emite.

Uma versão anterior desta RFC propunha um campo novo — `citacoes_orfas`, com
vocabulário fechado de motivos — para o catálogo carregar esse resíduo. Está
**descartado**, por dois motivos que se reforçam: daria esquema permanente a um
estado transitório, e poria no frontmatter uma conclusão que a RFC 0001 já
atribui ao achado. O erro era assumir que o detector camada 2 precisa continuar
disparando, e desenhar campo para alimentá-lo. Ele era andaime da transição.

### 4.2 O ponto de chegada torna a citação falsa irrepresentável

Com o vínculo completo, `FUNDAMENTACAO*` passa a ser **renderizada** a partir
de `dispositivos:`, usando a citação canônica que o `dispositivo_endereco` já
deriva (`art. 40, § 1º, inciso I` — formato do P4, derivado e não autorado).

Aí a proibição do regex deixa de ser decreto e vira consequência:

- não sobra prosa livre para parsear, porque a prosa é projeção do vínculo;
- e **uma citação falsa não pode ser escrita**, porque só se renderiza a partir
  de link que resolve.

Um detector existe para pegar uma classe de erro. Quando a arquitetura de
chegada torna aquela classe **irrepresentável**, o detector não é removido por
economia — ele deixa de ter objeto. É a mesma lógica pela qual não há detector
para "regra com `row_index` duplicado": `_validate_identity` torna esse estado
impossível de carregar.

### 4.3 A ordem é a única restrição real

O leitor não pode ser removido antes do vínculo estar completo, e a razão é
prosaica: **é ele que enumera o que falta**. Saber que 75 regras têm lacuna é
uma coisa; saber *quais* provisões faltam na lista de uma regra exige ler a
prosa dela. Depois de lida e vinculada, nunca mais.

Então `citacoes.py` volta a ser o que o `csv_to_okf.py` é — **bootstrap de uso
único, enforçado e não só documentado**. Já fez 106 das 112. As 6 restantes
fecham à mão, e o módulo sai do repositório junto com o
`citacao_nao_vinculada`, o `relatorio_citacoes.py` e o
`P4_REDACAO_INEXISTENTE`.

### 4.4 O que a remoção quebra, nomeadamente

Duas coisas, e nenhuma é surpresa se estiver escrita antes.

**O único sinal mecânico de vínculo incompleto.** O
`P4_CITACAO_NAO_VINCULADA` — 75 detecções camada 3 — mede "a prosa cita algo
que `dispositivos:` não declara". Depois dele, um auditor que esqueça uma
provisão não terá nada apontando o esquecimento. A resposta do repositório é a
quinta pergunta do P13.1 — *"quais dispositivos jurídicos justificam cada
critério e efeito?"* —, que a RFC 0001 já declara ser gate de julgamento
humano. Esta RFC não inventa essa resposta; ela para de simular com regex uma
cobertura que a especificação sempre disse ser humana.

**A bidirecionalidade P14.6 dos três achados.** `achado-0011`, `achado-0012` e
`achado-0013` referenciam fingerprints do `P4_REDACAO_INEXISTENTE` em
`deteccoes:`. Removido o detector, esses refs ficam órfãos e o
`stale_detection_refs` acusa. A conversão é explícita e é trabalho de fase: os
três passam a ser achados **inteiramente autorados**, com a evidência escrita
no corpo em vez de referenciada por fingerprint. Não é perda — é o estado que o
princípio da autoria humana já prescreve para uma acusação dessa gravidade.

## 5. Gates

`P16` está livre; `P15` é o maior em uso. Os três são camada 1 — estruturais,
sem achado — e todos sobre a fronteira do §2, nenhum sobre citação:

| Gate                    | Falha quando                                         |
| ----------------------- | ---------------------------------------------------- |
| `P16_CHAVE_SEM_DESTINO` | chave de frontmatter em nenhum dos dois registros    |
| `P16_DESTINO_DUPLICADO` | chave declarada como coluna **e** como campo próprio |
| `P16_COLUNA_SEM_ORIGEM` | coluna do `COLUMNS` que nenhuma chave alimenta       |

A citação não ganha gate novo. Ela **perde** os que tem, conforme o §4 — que é
o oposto de acrescentar maquinaria, e é o ponto.

## 6. Plano incremental

Cada fase é commitável sozinha. As fases 1–4 são sequenciais por dependência
real (§4.3), não por conveniência.

- **Fase 0** — `CampoProprio`, o registro das 4 chaves atuais e das 3 do P7, e
  os três gates `P16`. **No-op demonstrável**: nenhum frontmatter muda, logo a
  chave material do P2 fica intocada por construção e não por argumento.
  Independente de todo o resto desta RFC.
- **Fase 1** — as 7 transcrições que faltam (6 da LCE 432/2008 e a alínea "b"
  do § 1º, III da CF por EC 20/1998), mais a grafia por extenso da LCE
  1.100/2021 que hoje sai `sem_norma` na regra-0037.
- **Fase 2** — as 6 regras sem `dispositivos:` fecham à mão. `dispositivos:`
  passa a ser o registro completo de citação das 112.
- **Fase 3** — `achado-0011`/`0012`/`0013` convertidos para achados
  inteiramente autorados; `P4_REDACAO_INEXISTENTE` removido. O
  `stale_detection_refs` continua limpo, ou a fase não fecha.
- **Fase 4** — aposentadoria de `citacoes.py`, `citacao_nao_vinculada`,
  `relatorio_citacoes.py` e do baseline `P4_CITACAO_NAO_VINCULADA`. **Nenhuma
  expressão regular sobrevive no caminho de confiança.**
- **Fase 5** — `FUNDAMENTACAO*` renderizada a partir de `dispositivos:`. É
  decisão de auditoria **por regra**, com a PGE no circuito: aquelas três
  colunas viajam e reescrevê-las muda o texto que chega ao documento do
  servidor. Não é sweep de refactor, e é a única fase que esta RFC descreve sem
  propor cronograma.

## 7. Questões em aberto

- **Q13** — uma citação estreitada a fragmento ("inciso III, **segunda
  parte**") é hoje vinculada à provisão inteira, com a perda de resolução
  contabilizada. Na fase 5 a renderização devolveria a provisão inteira, mais
  larga que a citação original. Isso é aceitável, ou o estreitamento precisa de
  representação própria antes da fase 5?
- **Q14** — o registro de campos próprios distingue "o Sisprev não tem coluna"
  de "é dado de auditoria". A primeira categoria é candidata a pedido de coluna
  nova ao IPERON. Existe canal para esse pedido, ou ela é permanentemente
  teórica?
- **Q15** — depois da fase 4, a completude de `dispositivos:` é julgamento
  humano registrado no corpo P13.1. Isso deveria ser exigido pelo `revisada` do
  P7, que hoje não exige nem `dispositivos:` não-vazio?
- **Q16** — na fase 5, o texto renderizado substitui o autorado no mesmo campo,
  ou o autorado é preservado em algum lugar? O `data/raw/` guarda o importado
  para sempre, mas uma fundamentação corrigida durante a auditoria e depois
  renderizada por cima não teria registro fora do git.

## 8. O que esta RFC não decide

Não decide o cronograma da fase 5, nem se ela acontece de uma vez ou regra a
regra — decide apenas que ela é o ponto de chegada e que as fases 1–4 não
dependem dela. Não decide Q6: as regras 0021/0022, cuja fundamentação é
partida por causa da incapacidade e nenhuma coluna registra, continuam sem
vínculo derivável e são trabalho humano na fase 2. Não altera nenhuma das 27
colunas do Sisprev, em nome ou em domínio: a fronteira desta RFC é inteiramente
do nosso lado dela.
