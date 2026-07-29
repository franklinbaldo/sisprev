# RFC 0008 — Tradução sem perdas entre o esquema auditado e o do Sisprev

- **Status**: parcialmente implementada (2026-07-29). As fases 2, 3 e 4
  estão **aplicadas** — nenhuma expressão regular sobrevive no caminho de
  confiança. A fase 0 (registro de campos próprios e os três gates `P16`) e
  a fase 1 (as transcrições) continuam pendentes; a fase 5 (renderização) é
  decisão de auditoria sem cronograma. Nada aqui altera o schema deployável,
  o CSV derivado ou as 27 colunas do Sisprev.
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

Isso não é hipótese, mas também não é o vazio completo: medindo, o
repositório declara mais do que parecia. Uma primeira versão desta RFC
afirmou que 4 chaves estavam "declaradas em lugar nenhum". Errado — e o erro
importa, porque a correção mostra que o problema é mais estreito e mais
tratável do que o diagnóstico original.

## 1. A fronteira, medida

Há **três** destinos, não dois, e o CSV derivado já os separa. Ele tem 34
colunas: as 27 do original, byte a byte no mesmo prefixo e na mesma ordem,
mais 7 de auditoria que a RFC 0001 P12 já previu.

| Destino                   | Chaves                                                                                                                   | Declarado em                                                       | Alcança o Sisprev? |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------ |
| coluna do Sisprev         | 27                                                                                                                       | `regra_schema.COLUMNS`                                             | **sim**            |
| coluna só do CSV derivado | `status_regra`, `motivo_inativacao`, `status_auditoria`, `auditado_por`, `auditado_em`, `atos_validacao`, `dispositivos` | `ADMIN_FIELD_DEFAULTS` + `ATOS_VALIDACAO_KEY` + `DISPOSITIVOS_KEY` | não                |
| não viaja                 | `type`, `id`, `row_index`                                                                                                | **em lugar nenhum**                                                | não                |

Das 31 chaves distintas hoje presentes no frontmatter das 112 regras, 27 são
colunas do Sisprev, `dispositivos` é coluna do derivado, e as três de
identidade OKF não são declaradas em canto nenhum. As outras seis
administrativas ainda não aparecem em nenhuma regra — são emitidas com
default (`ativa`, `importada`, `[]`, ...) — mas a coluna já existe para
recebê-las.

Então a lacuna real é menor e mais precisa do que "o outro lado não está
declarado":

1. **Três chaves de identidade sem destino declarado.** `type`, `id` e
   `row_index` funcionam por convenção.
2. **A declaração existe mas está espalhada e é orientada a emissão.** Um
   dict de defaults mais duas constantes soltas respondem "o que sai no
   CSV", não "para onde vai esta chave". São coisas diferentes, e a segunda
   é a que uma chave nova precisa responder.
3. **Nada verifica exaustividade.** Não há checagem de que toda chave de
   frontmatter caia em algum dos três destinos. Uma chave nova simplesmente
   existe.

A assimetria entre as duas direções continua real e não é defeito:

- **Sisprev → nosso** é total e provado. As 27 colunas entram na importação, o
  round-trip devolve o CSV byte a byte idêntico ao congelado. Nada a fazer.
- **Nosso → Sisprev** é total sobre as 27 e **deliberadamente parcial** sobre o
  resto — e essa parcialidade é *correta*: `dispositivos` não deve chegar ao
  produto.

"Sem perdas" nesta RFC não quer dizer que tudo viaja. Quer dizer que **nada se
perde por acidente**: toda chave tem um destino que alguém escreveu, e uma
chave sem destino é erro em vez de silêncio.

## 2. O princípio: toda chave tem um destino declarado

Uma única regra, e ela é mecanicamente verificável:

> Toda chave de frontmatter de um `regra-*.md` tem exatamente um destino
> declarado — coluna do Sisprev, coluna só do CSV derivado, ou não-viajante.
> Chave em nenhum é erro. Chave em mais de um é erro.

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

O registro é declarativo e não muda nenhum dado nem nenhuma coluna. Ele
**recolhe** o que já está espalhado — `ADMIN_FIELD_DEFAULTS`,
`ATOS_VALIDACAO_KEY`, `DISPOSITIVOS_KEY` — e acrescenta as três de
identidade (`type`, `id`, `row_index`) que hoje funcionam por convenção. O
CSV derivado continua com as mesmas 34 colunas na mesma ordem; o que muda é
que passa a existir um lugar único que responde "para onde vai esta chave",
e um gate que falha quando a resposta não existe.

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
repositório é derivada de parse de campo de texto livre. O leitor foi construído com cuidado e
tem 9 misatribuições corrigidas em teste de regressão contra o corpus real,
justamente porque cada uma delas escreveria uma citação legal plausível e
errada. O cuidado é evidência do problema, não solução dele.

### 4.1 O vazio de hoje é transitório, não estrutural

A leitura tentadora é que `dispositivos:` **não caberia** para o trabalho do
detector, porque `check_p3_dispositivos` exige que toda entrada resolva para um
dispositivo autorado, enquanto a acusação é sobre uma redação que não existe.
É verdade que o campo não expressa isso. Não é verdade que isso seja um limite
do desenho.

O catálogo está em construção. O vazio entre a fundamentação e o vínculo não
existe
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

### 4.2 A renderização foi considerada e descartada

Uma versão anterior desta RFC apontava como ponto de chegada `FUNDAMENTACAO*`
**renderizada** a partir de `dispositivos:`, usando a citação canônica que o
`dispositivo_endereco` deriva. O argumento era que, assim, uma citação falsa
ficaria irrepresentável — só se renderiza a partir de link que resolve.

Está **descartado**, e por uma razão que vale mais que o ganho: a fundamentação
não é uma lista de citações, é uma **articulação**. Ela encadeia os dispositivos
de modo a fazerem sentido jurídico entre si e a fundamentar **cada critério** da
regra. Uma lista achatada não regenera isso — o achatamento é precisamente o que
destrói a coisa que se quereria gerar. Renderizar não produziria uma
fundamentação mal formatada; produziria outro tipo de objeto, uma enumeração
onde havia um argumento.

Some-se o que a medição mostrou: o campo tem três partes — descrição do
benefício, lista de citações, qualificador de hipótese —, e só a do meio seria
derivável; e a renderização alargaria 67 citações hoje estreitadas a cláusula,
num campo que chega ao documento do servidor.

Nada disso custa a proibição do regex, que já está aplicada (§4.3–4.4) e nunca
dependeu da renderização.

### 4.3 A ordem é a única restrição real

O leitor não pode ser removido antes do vínculo estar completo, e a razão é
prosaica: **é ele que enumera o que falta**. Saber que 75 regras têm lacuna é
uma coisa; saber *quais* provisões faltam na lista de uma regra exige ler a
fundamentação dela. Depois de lida e vinculada, nunca mais.

Então `citacoes.py` volta a ser o que o `csv_to_okf.py` é — **bootstrap de uso
único, enforçado e não só documentado**. Já fez 106 das 112. As 6 restantes
fecham à mão, e o módulo sai do repositório junto com o
`citacao_nao_vinculada`, o `relatorio_citacoes.py` e o
`P4_REDACAO_INEXISTENTE`.

### 4.4 O que a remoção quebra, nomeadamente

Duas coisas, e nenhuma é surpresa se estiver escrita antes.

**O único sinal mecânico de vínculo incompleto.** O
`P4_CITACAO_NAO_VINCULADA` — 75 detecções camada 3 — mede "a fundamentação
cita algo
que `dispositivos:` não declara". Depois dele, um auditor que esqueça uma
provisão não terá nada apontando o esquecimento. A resposta do repositório é a
quinta pergunta do P13.1 — *"quais dispositivos jurídicos justificam cada
critério e efeito?"* —, que a RFC 0001 já declara ser gate de julgamento
humano. Esta RFC não inventa essa resposta; ela para de simular com regex uma
cobertura que a especificação sempre disse ser humana.

**A bidirecionalidade P14.6.** Só o `achado-0012` referenciava fingerprints do
`P4_REDACAO_INEXISTENTE` em `deteccoes:` — dez deles; o `achado-0011` e o
`achado-0013` já eram `verificacao: manual`, sem detecção nenhuma. Removido o
detector, aqueles refs ficariam órfãos e o `stale_detection_refs` acusaria, de
modo que o achado passou a `verificacao: manual` com a evidência no corpo — que
já estava lá, na conferência item a item contra o PDF compilado oficial. Não é
perda: os fingerprints não carregavam evidência, e o estado resultante é o que o
princípio da autoria humana já prescreve para uma acusação dessa gravidade.

Efeito colateral registrado: `dispositivo_schema.historico_completo` ficou sem
consumidor e foi removida junto. A lógica que ela codificava — redações que
ladrilham a vida da norma não deixam espaço para outra — sobrevive em prosa no
corpo do `achado-0012`, que é onde a RFC diz que ela pertence.

## 5. A fundamentação é uma articulação, não uma lista

Definição da coordenação da auditoria, e ela reorganiza tudo que vem antes:

> Cada regra se vincula a dispositivos. A fundamentação **articula** esses
> dispositivos de forma a fazerem sentido juridicamente e a fundamentar os
> critérios da própria regra — **cada um deles**.

O vínculo, então, não é `regra → dispositivos`. É **`critério → dispositivo(s)`**,
e o `dispositivos:` do frontmatter é a **união achatada** dessa relação: registra
que a regra cita oito provisões, e perde qual delas funda qual critério.

Isso não é conceito novo no repositório — é a **quinta pergunta da P13.1**,
escrita com essas palavras: *"dispositivos que justificam cada critério e
efeito"*. O conceito está declarado desde a RFC 0001; o que não existe é
estrutura para ele, e **não deve existir**.

### 5.1 Seguir isso é conferência, não código

A relação vive no corpo P13.1, em prosa autorada. Não precisa de campo novo, de
gate, de detector nem de schema — a RFC 0001 já classifica essa pergunta como
julgamento humano, e a auditoria de mérito é o lugar onde ela se responde, regra
a regra.

O trabalho é: listar os critérios da regra, e para cada um dizer qual dispositivo
o funda. Onde não fecha, aparece — e vira achado.

### 5.2 O recorte de cláusula se dissolve

Era a Q13: "inciso III, **segunda parte**" é citação estreitada, o vínculo é da
provisão inteira, e a resolução se perde. Parecia exigir representação própria —
componente novo no endereço, dispositivo próprio, ou qualificador na entrada.

Nenhuma é necessária, porque **o estreitamento é artefato do achatamento**. Dizer
só "esta regra cita o art. 40, § 1º, III" exige o qualificador para não afirmar
junto a regra federal de 62/65. Dizer qual critério aquele dispositivo funda
torna o recorte implícito, porque só uma das metades funda aquele critério.

Ressalva: isso vale quando as partes de uma provisão fundam critérios distintos,
que é o caso da maioria dos 67 registros hoje congelados. Não é garantia geral —
uma provisão cujas partes fundem o *mesmo* critério de modos diferentes
continuaria sem representação. Nenhum caso desses foi observado no corpus.

### 5.3 A conferência é um teste afiado

Se todo dispositivo tem de fundar algum critério, a pergunta deixa de ser vaga.
As pendências **P-3 e P-4** de
[`docs/analysis/base-normativa-invalidez-incapacidade.md`](../analysis/base-normativa-invalidez-incapacidade.md)
já registram o caso exemplar: `regra-0006`/`0007`/`0008`/`0009` citam o art. 40,
§ 1º, III da CF — aposentadoria voluntária por idade — para fundamentar
**invalidez**, e a "2ª parte" não encontra correspondência que socorra a citação.

O inciso de fato se biparte (União: 62/65; Estados: idade mínima por emenda à
Constituição estadual), e é a segunda metade que alcança o RPPS estadual. Mas
**nenhuma das duas funda critério de aposentadoria por incapacidade** — que é o
que a pergunta da P13.1 revela ao ser feita, e o que a leitura textual sozinha
não revelava.

## 6. Gates

`P16` está livre; `P15` é o maior em uso. Os três são camada 1 — estruturais,
sem achado — e todos sobre a fronteira do §2, nenhum sobre citação:

| Gate                    | Falha quando                                         |
| ----------------------- | ---------------------------------------------------- |
| `P16_CHAVE_SEM_DESTINO` | chave de frontmatter em nenhum dos dois registros    |
| `P16_DESTINO_DUPLICADO` | chave declarada como coluna **e** como campo próprio |
| `P16_COLUNA_SEM_ORIGEM` | coluna do `COLUMNS` que nenhuma chave alimenta       |

A citação não ganha gate novo. Ela **perde** os que tem, conforme o §4 — que é
o oposto de acrescentar maquinaria, e é o ponto.

## 7. Plano incremental

Cada fase é commitável sozinha. As fases 1–4 são sequenciais por dependência
real (§4.3), não por conveniência.

- **Fase 0** — `CampoProprio`, o registro das 4 chaves atuais e das 3 do P7, e
  os três gates `P16`. **No-op demonstrável**: nenhum frontmatter muda, logo a
  chave material do P2 fica intocada por construção e não por argumento.
  Independente de todo o resto desta RFC.
- **Fase 1** — as 7 transcrições que faltam (6 da LCE 432/2008 e a alínea "b"
  do § 1º, III da CF por EC 20/1998), mais a grafia por extenso da LCE
  1.100/2021 que hoje sai `sem_norma` na regra-0037.
- **Fase 2** ✅ — a fila `VINCULAR` zerada: cinco vínculos autorados em
  `regra-0008`, `regra-0009`, `regra-0012`, `regra-0013` e `regra-0026`,
  cada um conferido contra a fundamentação da própria regra. O que restou não é
  mecanicamente fechável, e está congelado em
  [`docs/analysis/pendencias-de-citacao-congeladas.md`](../analysis/pendencias-de-citacao-congeladas.md)
  (108 pendências em 74 regras).
- **Fase 3** ✅ — `achado-0012` convertido para `verificacao: manual`;
  `P4_REDACAO_INEXISTENTE` removido; `stale_detection_refs` limpo.
- **Fase 4** ✅ — `citacoes.py`, `citacao_nao_vinculada`,
  `relatorio_citacoes.py`, seus testes e o baseline
  `P4_CITACAO_NAO_VINCULADA` removidos. **Nenhuma expressão regular
  sobrevive no caminho de confiança.**
- **Fase 5** ❌ **descartada** — era `FUNDAMENTACAO*` renderizada a partir de
  `dispositivos:`. Uma articulação não se regenera de uma lista (§4.2, §5).
- **Fase 6** — a **conferência** `critério → dispositivo`, regra a regra, no
  corpo P13.1. Não é fase de código: não cria campo, gate nem schema (§5.1). É
  a auditoria de mérito, e é o que substitui — melhor — tudo que as fases 5 e
  os gates de citação prometiam.

## 8. Questões em aberto

- ~~**Q13**~~ — **respondida** (§5.2): a citação estreitada a fragmento não
  precisa de representação própria. O estreitamento é artefato do achatamento
  e se dissolve ao registrar qual critério o dispositivo funda. Fica aberto
  apenas o caso não observado no corpus — partes de uma provisão fundando o
  *mesmo* critério de modos diferentes.
- **Q14** — o registro de campos próprios distingue "o Sisprev não tem coluna"
  de "é dado de auditoria". A primeira categoria é candidata a pedido de coluna
  nova ao IPERON. Existe canal para esse pedido, ou ela é permanentemente
  teórica?
- **Q15** — depois da fase 4, a completude de `dispositivos:` é julgamento
  humano registrado no corpo P13.1. Isso deveria ser exigido pelo `revisada` do
  P7, que hoje não exige nem `dispositivos:` não-vazio?
- ~~**Q16**~~ — **prejudicada** pelo descarte da fase 5: sem renderização, não
  há texto gerado passando por cima do autorado.
- **Q17** — a conferência da fase 6 produz, por regra, a lista de critérios e o
  dispositivo que funda cada um. Isso mora só na prosa do corpo P13.1, ou o
  `revisada` do P7 passa a exigir que ela exista? É a mesma pergunta da Q15,
  vista do outro lado.

## 9. O que esta RFC não decide

Não decide o mérito de nenhuma citação. As pendências **P-3** e **P-4** de
[`docs/analysis/base-normativa-invalidez-incapacidade.md`](../analysis/base-normativa-invalidez-incapacidade.md)
— o art. 40, § 1º, III citado para fundamentar invalidez em quatro regras —
são exemplo do que a conferência da fase 6 resolve, e a conclusão delas é
achado autorado, nunca derivação desta RFC.

Não decide Q6: as regras 0021/0022, cuja fundamentação é partida por causa da
incapacidade e nenhuma coluna registra, continuam sem vínculo derivável.

Não decide se a relação `critério → dispositivo` algum dia ganha forma
estruturada. A posição desta RFC é que **não precisa** — a P13.1 já a
classifica como julgamento humano, e a experiência do leitor por regex é o
argumento contra dar forma de máquina ao que é ato de leitura jurídica.

Não altera nenhuma das 27 colunas do Sisprev, em nome ou em domínio: a
fronteira desta RFC é inteiramente do nosso lado dela.
