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

### 4.1 Por que não basta apontar o detector para `dispositivos:`

Porque não cabe. `check_p3_dispositivos` exige que toda entrada de
`dispositivos:` resolva para um dispositivo autorado, e a acusação é
precisamente sobre uma **redação que não existe**. Um vínculo explícito que não
resolve quebra o bundle. Medido: as cinco provisões que o `achado-0012` prova
(`art-28-inc-i`, `art-30-inc-ii`, `art-32-inc-i`, `art-38`, `art-62` da LCE
432/2008) estão **ausentes** do `dispositivos:` da regra-0012, e estão ausentes
por construção.

O catálogo não tem onde registrar *"a regra afirma citar X"* quando X não
existe. Só a prosa diz isso, e é por isso que o detector foi parar no regex.
Faltava campo.

### 4.2 O campo que falta

Um irmão de `dispositivos:`, também campo próprio, também não-viajante:

```yaml
dispositivos:            # o que a regra cita e resolve
  - /dispositivos/cf88/art-40-par-7/ec-103-2019.md

citacoes_orfas:          # o que a regra afirma citar e não resolve
  - endereco: lce-432-2008/art-62
    redacao: lce-949-2017
    motivo: redacao_inexistente
```

O `motivo` vem de vocabulário fechado, e ele é exatamente o que hoje o relatório
de citações produz como duas filas — só que autorado em vez de parseado:

| `motivo`                 | significa                                                            |
| ------------------------ | -------------------------------------------------------------------- |
| `redacao_nao_transcrita` | a redação existe, ninguém transcreveu ainda (fila TRANSCREVER)       |
| `redacao_inexistente`    | a provisão está inteiramente transcrita e essa redação nunca existiu |
| `norma_nao_autorada`     | a norma citada não tem `norma.md`                                    |
| `indecidivel`            | a prosa não permite concluir — regra-0021/0022, Q6 aberta            |

A inversão é o ponto. Hoje a máquina **descobre** a acusação lendo prosa; com o
campo, a máquina **verifica** uma acusação que um humano fez. O
`P4_REDACAO_INEXISTENTE` deixa de extrair citação e passa a conferir se o
histórico transcrito sustenta o `redacao_inexistente` que a regra declara —
recusando quando não sustenta, com a mesma severidade com que hoje recusa
concluir na presença de uma redação sem data. Continua camada 2, continua
falhando fechado, e para de depender de expressão regular.

Isso também é o princípio da autoria humana aplicado onde ele mais importa. O
repositório já exige que achados sejam escritos à mão porque uma conclusão é ato
humano. Uma acusação de citação legal falsa é conclusão mais forte que a média
dos achados, e é a única que hoje nasce de um parser.

### 4.3 O leitor vira ferramenta de migração

Com `citacoes_orfas` autorado, `citacoes.py` deixa de ser componente e volta a
ser o que o `csv_to_okf.py` é: **bootstrap de uso único, enforçado e não só
documentado**. Ele já fez 106 das 112 regras. As 6 restantes fecham à mão, e
depois disso o módulo, o `citacao_nao_vinculada` e o `relatorio_citacoes.py`
saem do repositório.

O custo tem de ser dito por inteiro, porque é real e não é pequeno. O
`P4_CITACAO_NAO_VINCULADA` — 75 detecções camada 3 — é inteiramente derivado do
leitor. Ele mede "a prosa cita algo que `dispositivos:` não declara", e é hoje o
**único sinal mecânico de que uma lista de vínculos está incompleta**.
Aposentá-lo significa que um auditor que esqueça uma provisão não terá nada
apontando o esquecimento. A resposta do repositório é a quinta pergunta do
P13.1 — *"quais dispositivos jurídicos justificam cada critério e efeito?"* —
que a RFC 0001 já declara ser gate de julgamento humano, não checagem de
máquina. Esta RFC não inventa essa resposta; ela apenas para de simular com
regex uma cobertura que a especificação sempre disse ser humana.

### 4.4 O que esta RFC deliberadamente não faz com a fundamentação

A saída simétrica seria **renderizar** `FUNDAMENTACAO*` a partir de
`dispositivos:`, usando a citação canônica que o `dispositivo_endereco` já
deriva. Aí não sobraria prosa para parsear e a fronteira ficaria perfeita nas
duas direções.

Não está proposto aqui, por um motivo de escopo e não de gosto: aquelas três
colunas **viajam**, e reescrevê-las muda o texto que chega ao documento do
servidor em 112 regras. É decisão de auditoria por regra, com a PGE no circuito,
não sweep de refactor. Fica registrado como direção natural (§7) e depende de o
vínculo explícito estar completo primeiro — o que é o trabalho desta RFC.

## 5. Gates

`P16` está livre; `P15` é o maior em uso.

| Gate                          | Falha quando                                                                                     |
| ----------------------------- | ------------------------------------------------------------------------------------------------ |
| `P16_CHAVE_SEM_DESTINO`       | chave de frontmatter em nenhum dos dois registros                                                |
| `P16_DESTINO_DUPLICADO`       | chave declarada como coluna **e** como campo próprio                                             |
| `P16_COLUNA_SEM_ORIGEM`       | coluna do `COLUMNS` que nenhuma chave alimenta                                                   |
| `P16_CITACAO_ORFA_RESOLVIVEL` | entrada de `citacoes_orfas` que na verdade resolve — é vínculo, e o lugar dela é `dispositivos:` |
| `P16_ACUSACAO_NAO_SUSTENTADA` | `motivo: redacao_inexistente` que o histórico transcrito não sustenta                            |

Os três primeiros são camada 1 (estrutural, sem achado). Os dois últimos são
camada 2 pela mesma razão que o `P4_REDACAO_INEXISTENTE` já é: tocam o que
chega ao servidor.

## 6. Plano incremental

Cada fase é commitável sozinha e nenhuma depende da seguinte.

- **Fase 0** — `CampoProprio` + o registro das 4 chaves atuais e das 3 do P7 +
  `P16_CHAVE_SEM_DESTINO`/`_DESTINO_DUPLICADO`/`_COLUNA_SEM_ORIGEM`. **No-op
  demonstrável**: nenhum frontmatter muda, logo a chave material do P2 fica
  intocada por construção e não por argumento.
- **Fase 1** — schema de `citacoes_orfas` + gates `P16_CITACAO_ORFA_RESOLVIVEL`
  e `P16_ACUSACAO_NAO_SUSTENTADA`. Nenhuma regra autorada ainda.
- **Fase 2** — autorar `citacoes_orfas` nas duas regras que o `achado-0012` já
  prova (regra-0012 e regra-0013), à mão. É o teste real do desenho: se o campo
  não consegue expressar o que o achado afirma, o desenho está errado e se
  descobre com duas regras, não com 112.
- **Fase 3** — `P4_REDACAO_INEXISTENTE` passa a ler `citacoes_orfas` e para de
  importar `citacoes`. O teste que fixa exatamente o que o `achado-0012` prova
  continua verde, ou a fase não fecha.
- **Fase 4** — as 6 regras sem `dispositivos:` fecham à mão; `citacoes_orfas`
  autorado onde a prosa hoje só é lida por regex.
- **Fase 5** — aposentadoria de `citacoes.py`, `citacao_nao_vinculada`,
  `relatorio_citacoes.py` e do baseline `P4_CITACAO_NAO_VINCULADA`.
- **Fase 6** *(separada, decisão de auditoria)* — renderização de
  `FUNDAMENTACAO*` a partir do vínculo. Fora do escopo desta RFC (§4.4).

## 7. Questões em aberto

- **Q13** — `motivo` cobre os quatro casos observados. Uma citação estreitada a
  fragmento ("inciso III, **segunda parte**") é hoje vinculada à provisão
  inteira com a perda de resolução contabilizada. Isso é um quinto `motivo` ou
  continua sendo vínculo com nota?
- **Q14** — o registro de campos próprios distingue "o Sisprev não tem coluna"
  de "é dado de auditoria". A primeira categoria é candidata a pedido de coluna
  nova. Existe um canal para esse pedido, ou ela é permanentemente teórica?
- **Q15** — depois da fase 5, a completude de `dispositivos:` é julgamento
  humano registrado no corpo P13.1. Isso deveria ser exigido pelo `revisada`
  do P7, que hoje não exige nem `dispositivos:` não-vazio?

## 8. O que esta RFC não decide

Não decide o nome final de `citacoes_orfas` nem a grafia exata do
`endereco`/`redacao` na entrada — a fase 1 fixa isso contra o caso real da fase
2\. Não decide se `FUNDAMENTACAO*` passa a ser derivada (§4.4). Não decide Q6, e
por isso `indecidivel` existe como motivo em vez de forçar regra-0021/0022 a uma
conclusão. Não altera nenhuma das 27 colunas do Sisprev, em nome ou em domínio:
a fronteira desta RFC é inteiramente do nosso lado dela.
