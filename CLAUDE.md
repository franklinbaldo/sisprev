# CLAUDE.md

Project guide for Claude Code. Mapa do repositório: onde as coisas ficam, o que
foi decidido, e quais erros são silenciosos. **Não é contrato** — o contrato de
cada tipo de documento está na spec dele, e é lá que mora o detalhe.

## O que este repo é

`sisprev` audita e valida as regras de aposentadoria e pensão por morte do
regime próprio de previdência do Estado (RO). O catálogo vive em três lugares,
cada um com papel distinto e não negociável:

- **`data/raw/regras-sisprev.csv`** — a importação original congelada, read-only
  para sempre. A linha de base da auditoria: o que foi recebido, como recebido.
- **`okf/regras-sisprev/`** — o registro vivo, um bundle
  [OKF v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
  com um `regra-NNNN.md` por regra. **É aqui que a edição de auditoria
  acontece** — corrigir citação, ajustar data, virar
  `validado_pge`/`validado_presidencia` quando PGE/Presidência assinarem.
- **`data/regras-sisprev.csv`** — export plano derivado e descartável,
  regenerado por script. Conveniente para quem quer tabela em vez de uma centena
  de markdowns; não é lugar de editar nada.

## Antes de editar: leia a spec do tipo

O que um documento *significa* está na spec dele, e é lá que se descobre o que
uma edição implica. Leia a spec do tipo que você vai tocar **antes** de tocá-lo —
inteira, não por `grep`.

E leia **o que já foi decidido**: as
[decisões transversais](docs/analysis/decisoes-de-auditoria-2026-07-30.md) e o
quadro de estado das questões Q1–Q12 em [`docs/spec/regra.md`](docs/spec/regra.md)
registram premissas fixadas — semântica das datas, leitura de campo vazio,
inclusividade de cada limite, o que a auditoria pode alterar. **Elas não se
reabrem por conveniência**: uma leitura que contrarie qualquer delas é
divergência a declarar com evidência, nunca a adotar em silêncio. Redescobrir
uma decisão custa o dia de trabalho que ela já custou, e a leitura intuitiva já
foi a errada mais de uma vez — a simetria dos dois eixos de data foi proposta,
ratificada e derrubada por medição.

| tipo                   | contrato                                                            | onde                                    |
| ---------------------- | ------------------------------------------------------------------- | --------------------------------------- |
| `Regra`                | [`docs/spec/regra.md`](docs/spec/regra.md)                          | P13.1, `# Estado da análise`, Q1–Q12    |
| `Dispositivo`, `Norma` | [`docs/spec/dispositivo.md`](docs/spec/dispositivo.md)              | P3/P4, `componentes`, cadeia, vigências |
| `Achado`               | [`docs/rfc/0001-*.md`](docs/rfc/) §P14 + `scripts/achado_schema.py` | seções obrigatórias, `deteccoes`        |
| `Conjunto`             | [`docs/rfc/0006-*.md`](docs/rfc/)                                   | P15, deltas, resolução                  |
| `RegraProposta`        | [`docs/rfc/0004-*.md`](docs/rfc/)                                   | catálogo proposto, compilador           |
| `FormaCalculo`         | `scripts/forma_calculo_schema.py`                                   | P16, componentes, `projecao_sisprev`    |

Isto não é formalidade. Caso real: a spec de dispositivo diz que **os níveis
acima entram na redação contemporânea a esta**. Quem edita sem ter lido isso não
tira a consequência — alterar um ancestral cria redação nova, logo arquivo novo e
fronteira de vigência nova — e o erro que resulta é **silencioso**: cada
parágrafo é verbatim, o caminho confere, o vínculo resolve, e nenhum gate acusa.
Foi assim que `art-40-par-1-inc-ii` ficou com uma vigência atravessando a EC
41/2003 enquanto o irmão `inc-i` estava certo.

A regra geral: **quando este arquivo e uma spec divergirem, a spec ganha** — e a
divergência é ela própria um achado, porque significa que o mapa envelheceu.

## Em que fase o trabalho está

**A infraestrutura está essencialmente pronta; o trabalho agora é corrigir as
regras.** Bundle OKF, dispositivos, detectores, conjuntos, compilador do catálogo
auditado, site e gates de CI já existem e funcionam. O que falta é **auditoria de
mérito**: conferir cada regra contra a lei, vincular dispositivos à mão, escrever
os corpos P13.1, autorar achados, decidir as citações erradas.

Isso muda a postura padrão de uma sessão. Diante de um problema, a primeira
pergunta é *"que edição autorada num `regra-*.md`, `achado-*.md` ou dispositivo
resolve isto?"* — não *"que campo, gate ou detector eu crio?"*. Dois precedentes,
ambos na direção de **menos maquinaria**: o leitor de citações por regex foi
**removido**, não estendido (RFC 0008), porque produzia acusação jurídica
plausível e não verificada; e a relação `critério → dispositivo` foi
deliberadamente **deixada sem schema**, como conferência humana no corpo P13.1
(RFC 0008 §5). **Quando uma edição de regra e uma mudança de esquema resolvem o
mesmo problema, a edição ganha.**

## O que é uma regra, e o que este trabalho pode mudar

Registro completo em [`docs/spec/regra.md`](docs/spec/regra.md) ("Definição de
trabalho").

- **Uma regra é o conjunto de aferições necessário para conceder o benefício.**
  Divergência em critério aferido já torna duas regras **não idênticas**, ainda
  que fundamentadas no mesmo dispositivo — `sexo` é o exemplo confirmado.
  *Benefício*, não aposentadoria: o catálogo cobre também a pensão por morte.
- **A granularidade da aferição é conveniência do IPERON** ("doença da lista"
  versus uma regra por doença). Logo o número de regras **não é determinado pela
  lei**, e é essa elasticidade que a decomposição 1:N e a consolidação N:1 da RFC
  0004 existem para representar.
- **O trabalho é de parametrização, não de mudança do sistema.** Estender o
  domínio de um enum ou criar coluna é alterar o **Sisprev** — fora do escopo.
  Dentro do escopo: valores dentro dos domínios que já existem, e as colunas de
  texto livre (`nome`, `FUNDAMENTACAO*`). É por isso que a RFC 0004 tem um
  **compilador**: o catálogo proposto pode ser mais rico, mas o que sai tem de
  caber nas colunas que o Sisprev já tem.

Consequência que muda a leitura de dois detectores sem alterar nenhum: um grupo
`P2_IGUALDADE_MATERIAL_ATIVA` pode ser **regras legitimamente distintas cuja
distinção o catálogo não consegue expressar** — lacuna de schema, não
duplicação. `nome` está **fora** da chave material do P2 e `FUNDAMENTACAO*`
**dentro**: diferenciar a fundamentação é parametrização e dissolve o grupo
honestamente, enquanto renomear limpa o `P1_NOME_REPETIDO` sem mascarar o P2.

## Arquitetura

```
data/raw/regras-sisprev.csv   (frozen, read-only forever)
        │  scripts/csv_to_okf.py  — ONE-TIME BOOTSTRAP ONLY, see below
        ▼
okf/regras-sisprev/            <-- living record, edited directly during audits
├── index.md                   # root listing — NO frontmatter except okf_version (SPEC.md §6, §11)
├── regras-sisprev.md          # type: Dataset — columns/row_count frontmatter + "# Schema" table
└── regras/
    ├── index.md                     # listing, no frontmatter
    └── regra-0001.md ...            # type: Regra, one per rule
        │  scripts/okf_to_csv.py  — run after every edit
        ▼
data/regras-sisprev.csv        (derived, always regenerated — never data/raw/)
```

Bundles irmãos, cada um com identidade própria: `okf/dispositivos/` (P3/P4),
`okf/conjuntos/` (P15), `okf/regras-propostas/` (RFC 0004),
`okf/formas-calculo/` (P16).

- **Toda** coluna do CSV original é chave de frontmatter (nome slugificado),
  fundamentação incluída. O **frontmatter *é* a regra deployável do Sisprev** — o
  produto só carrega os campos que o Sisprev já tem, então a regra inteira vive
  lá e faz round-trip com o CSV. O **corpo markdown é a análise do auditor** —
  notas de conciliação, questões abertas, as seções P13.1 —, nunca coluna do CSV,
  nunca deployado, nunca material para a igualdade do P2.
- O campo `columns` de `regras-sisprev.md` é a fonte única de ordem/nome de
  coluna ao reconstruir o CSV: `okf_to_csv.py` lê dali, não de `index.md` (que
  por spec não pode carregar frontmatter arbitrário).
- A linha em branco no topo do CSV (artefato do export do Google Sheets) é
  reproduzida explicitamente por `okf_to_csv.py`, não tratada como dado.

## Rodando as coisas

```bash
# One-time bootstrap only (see "Rules of the road") — never after audit edits start
uv run python scripts/csv_to_okf.py

# "derivar" (RFC 0001 P10): regenerate the derived CSV + every index.md
uv run python scripts/gerar_indices.py

# "validar" (read-only): structural invariants + detection<->achado
# bidirectionality. Never writes anything. --json for machine output.
uv run python scripts/validar_regras.py

uv run pytest -q                                # CI contract runner
uv run python scripts/regras_log.py             # refresh the P11 changelog

# Site (dev/build regeneram a saída do emissor via hooks predev/prebuild)
cd site && npm install
npm run dev     # http://localhost:4321/sisprev/
npm run check   # astro check — .astro/.ts + content collections
npm run test    # vitest — site/src/lib
npm run build   # astro build -> site/dist/, e o postbuild roda o Pagefind

# Relatório da PGE em PDF (exige `npm run build` antes)
uv run python scripts/gerar_relatorio_pdf.py
```

`npm run check` não tem hook: rode `bash site/scripts/emit-data.sh` antes, ou ele
falha no import de `dados-do-site.json`, que não é comitado.

## A biblioteca de domínio

A lógica normativa é uma **biblioteca pura** (RFC 0001, P10) — `bundle.py`
(`Bundle`, `collect_detections`, `validate_bundle`), `achado_schema.py`,
`detectors/` (cada detector devolve `Detection`s com `fingerprint` estável, nunca
markdown) e `estado_auditoria.py` (invariantes do P7). `validar_regras.py` é um
CLI **read-only** sobre ela; `gerar_indices.py` é o único comando que escreve
artefato derivado; `pytest` chama a biblioteca e nunca a reimplementa.
**Achados são escritos à mão** — nenhum comando os autora.

- **Achado → teste**: cada detector declara seu `TESTS`, agregados em
  `detectors.DETECTOR_TESTS`; `bundle.covering_tests(achado)` resolve os
  detectores citados nas `deteccoes` e devolve os arquivos que os cobrem — uma
  afirmação mecânica volta ao teste que a prova, não só à prosa da RFC. Mora em
  `bundle.py` para que `achado_schema.py` fique agnóstico de detector.
- **`concept.py` é a representação única** de todo documento OKF: o modelo
  `Concept` (`doc_id`, `frontmatter`, `body`, `sections`) e `parse_concept_doc()`,
  o único parser delimitado por `---`. Todos os tipos o subclassificam. Os campos
  de `Concept` checam só **forma**: um doc bem formado e semanticamente inválido
  tem de **carregar**, para que um validador o reporte como `Violation` em vez de
  levantar no meio do `Bundle.load()`.
- **Typed contract pattern**: cada subtipo valida sua fatia de frontmatter uma vez
  num `cached_property` que devolve *ou* o modelo validado *ou* o
  `ValidationError` capturado, exposto por `.contract`/`.admin` e
  `.validation_error`. Todo accessor de domínio lê o contrato tipado quando
  válido e **cai para leitura crua do dict** quando é `None` — não é encanamento
  opcional: os joins do P7/P14 precisam de um campo mesmo de um doc inválido por
  causa de **outro** campo ("detecção ≠ conclusão" vale para o leitor, não só
  para o autor; remover esse fallback já causou regressão).
- O contrato de `Regra` cobre só a fatia administrativa P2.1/P3
  (`extra="ignore"`) — os campos de domínio ficam **sem tipo por desenho**: o
  detector do P2 tem de tratar todo campo de domínio, atual e futuro, como
  material, e um schema estrito do documento inteiro contradiria isso. Mesma
  razão por trás do `.loose()` do Zod no site.
- `Bundle` é um Pydantic `BaseModel` frozen aninhando tuplas de subclasses de
  `Concept` — sem `arbitrary_types_allowed`, porque todo tipo aninhado já é
  modelo Pydantic.

## Os documentos, tipo por tipo

### Dispositivo e Norma — `okf/dispositivos/` (P3/P4)

Um `.md` por provisão legal **por redação**, na menor granularidade de fato
citada por uma regra — "decomposição sob demanda", nunca fragmentação preventiva.
Contrato em [`docs/spec/dispositivo.md`](docs/spec/dispositivo.md); aqui só o que
não se adivinha:

- **Identidade é derivada, nunca composta à mão**:
  `<norma>/<endereço>/<redação>.md`. O **diretório é a provisão** e os arquivos
  dentro são **suas redações**, então "toda redação do art. 40, § 1º, I" é uma
  listagem de diretório, e acrescentar redação posterior nunca renomeia a
  anterior. Os três segmentos são recomputados e comparados (`_check_caminho`).
- **O endereço é `componentes`** (lista ordenada, `tipo` de enum fechado), nunca
  campos planos. `dispositivo_endereco.py` é o núcleo puro: aninhamento legal,
  slug, **citação canônica** (derivada, não autorada) e a ordenação que põe § 2º
  antes de § 14. `site/src/lib/dispositivo.ts` é um porte testado para exibição; o
  Python continua a autoridade, porque é ele que derruba o commit.
- **`norma` é chave num vocabulário fechado**: todo `type: Norma` em
  `<chave>/norma.md`. Normas alteradoras são autoradas mesmo sem contribuir
  dispositivo — a alteradora é o que verifica uma redação. `fontes` é lista não
  vazia de URLs guardadas **verbatim** (coerção `HttpUrl` reescreveria a string e
  quebraria o round-trip byte-idêntico).
- **Duas redações de uma provisão nunca podem estar as duas em vigor**
  (`check_vigencias`, `P3_VIGENCIA_SOBREPOSTA`). Um *vão* entre redações
  deliberadamente **não** é erro — transcrição sob demanda deixa faltar a
  intermediária.
- **A cadeia importa, e o erro dela é silencioso.** Um dispositivo é a unidade
  endereçada **com toda a cadeia que a contém**, na redação contemporânea a ela;
  logo alterar um ancestral cria redação nova, ainda que o nível mais interno não
  mude. Vigência que atravessa a alteração de um ancestral monta texto que nunca
  esteve em vigor junto, e **nenhum gate detecta**: `check_vigencias` só compara
  datas dentro de um diretório.
- **"Redação inexistente" é conclusão humana, nunca derivada** (RFC 0008). Se as
  redações autoradas pavimentam a vida inteira da norma sem vão, nenhuma outra
  pode existir — então uma regra que cita fora desse conjunto faz citação legal
  falsa, não espera transcrição. O raciocínio é real, mas a conclusão é
  **acusação** sobre campo deployável: vai escrita à mão num achado, nunca
  emitida por detector (`achado-0012` é o caso trabalhado).
- `bundle.py::check_p3_dispositivos` é o join entre bundles, e a referência nomeia
  a **redação**, não só a provisão.

**Nenhuma regra é populada retroativamente** — transcrever o texto legal e
vinculá-lo é ato de autoria humana, mesmo princípio dos achados e das seções
P13.1. Quase todas já têm `dispositivos:`, e **as que faltam têm causa conhecida
e registrada**: `regra-0003`/`0005` esperam transcrição da redação citada;
`regra-0021`/`0022` são **recusa deliberada**, porque a fundamentação empacota
três articulações numa célula (`|`) cuja divisão é por causa da incapacidade, sem
coluna que a registre (Q6).

**P4 — citação é declarada, nunca parseada (RFC 0008).** Uma entrada de
`dispositivos:` é **autorada**: um humano lê a `FUNDAMENTACAO*` da regra, confere
a provisão contra a fonte, escreve o vínculo. Nada lê aqueles campos
mecanicamente, e nada pode. Não é precaução abstrata: um leitor por regex
existiu, foi feito com cuidado, e produziu **nove atribuições erradas distintas**
— `C/C` (*combinado com*) lido como inciso, dígitos de data lidos como número de
artigo, uma emenda estadual doando seus artigos à Constituição federal. Todas
pareciam citação bem formada. Foi removido, e sua saída final está congelada em
[`docs/analysis/pendencias-de-citacao-congeladas.md`](docs/analysis/pendencias-de-citacao-congeladas.md)
como lista de trabalho autorada.

A entrada afirma *"a fundamentação desta regra cita esta provisão"*, nunca "ela é
juridicamente fundada nela". Cada ambiguidade é recusa, não chute: a norma dona
às vezes é só implícita, a redação citada pode nunca ter sido transcrita, e
alguns campos empacotam duas ou três fundamentações numa célula.

**A fundamentação é uma articulação, não uma lista** (RFC 0008 §5): ela encadeia
os dispositivos para que façam sentido jurídico juntos e para que **cada**
critério fique fundado. A relação real é `critério → dispositivo(s)`, e
`dispositivos:` é a *união achatada* dela — registra que a regra cita oito
provisões e perde qual funda qual critério. Essa relação é a quinta pergunta do
P13.1 e fica **conferência humana na prosa do corpo**, sem campo nem gate. Duas
consequências: renderizar `FUNDAMENTACAO*` a partir de `dispositivos:` foi
**descartado** (articulação não se regenera de lista), e citação estreitada a uma
parte não precisa de representação própria — dizer qual critério a provisão funda
torna o estreitamento implícito.

### Achado e `disposicao_de_achados`

**Dois `situacao`, e a ausência de um terceiro é a decisão.** Um achado **não se
fecha por conta própria**: um defeito real deixa de pender quando **cada regra
alcançada dispõe** dele em `disposicao_de_achados` — ato com autor, data e
justificativa, na regra. Quem responde é a regra; o achado segue `aberto`
enquanto houver população sem resposta. É "uma ponta declara, a outra dispõe"
levado até o fim: o fechamento é da ponta que dispõe.

Existiu um estado `resolvido` no achado, e ele foi **removido** porque permitia
declarar o defeito tratado sem que regra alguma tivesse dito como o tratou — o
selo substituía a disposição que o desenho exige. A spec já registrava a
consequência disso: `situacao` é um campo só para uma população heterogênea, e
com ele o achado era "aberto ou resolvido para todas de uma vez". Com a
disposição por regra, a granularidade passa a existir onde a heterogeneidade
está.

`improcedente` é a **única** saída do próprio achado, e afirma coisa diferente:
**a acusação não procede** — o defeito não existe, ou não existe como o achado o
descreveu. Não há disposição a fazer porque não há defeito a que responder.
Fechar como improcedente um defeito que existiu gravaria no catálogo que uma
regra nunca teve o problema que teve, e o selo sobrevive à prosa: quem lê o
estado não lê o corpo.

O estado é necessário porque **id de achado é append-only** — o CI percorre a
história e falha em remoção ou renomeação —, então um achado errado não some, só
pode ser marcado; e porque a auditoria decidiu propor a leitura mais provável
quando a certa não é reconstruível, postura que produz acusação falível por
desenho. Ele exige a sua trilha (`improcedente_em`/`_por`), proibida em achado
aberto, e a seção `# Resolução` — fechar sem escrever por quê é o que o gate
impede.

**A expectativa sobre a detecção é derivada, não declarada.** Não há
`efeito_deteccao`: quem diz que a ocorrência mecânica deve sumir é a população
ter respondido `corrigida` (`bundle.achados_integralmente_corrigidos`). Daí
`stale_detection_refs` não acusar detecção sumida num achado integralmente
corrigido — antes, corrigir o defeito derrubava o gate e obrigava a fechar o
achado — e `P14_DETECCAO_DEVERIA_DESAPARECER` passar a acusar o inverso: toda a
população disse ter corrigido e a detecção continua reproduzindo, logo alguma
disposição afirma ato que os campos não sustentam.

`improcedente` **não conta como aberto** em nenhum join: não exige disposição de
regra nenhuma, não bloqueia `revisada`. E entra na cobertura de detecções
(`improcedente_achados`), porque a detecção que o originou **segue de pé** — a
ocorrência mecânica continua real, o que caiu foi a conclusão sobre ela.

**A regra responde a cada achado que a nomeia**: uma ponta declara, a outra
dispõe. O achado segue dono de *qual é o problema* e *quais regras alcança*; a
regra ganha só *como responde* — com `justificativa` não vazia e trilha
(`decidido_por`/`decidido_em`), porque "ignorado" não é disposição, é omissão com
um lugar para morar. Há gate de reconciliação: a entrada só vale se o achado
existe e já nomeia a regra. **O campo aperta o gate**: antes achado aberto não
impunha nada; agora toda `revisada` precisa de disposição para cada achado aberto
que a nomeie.

**Em achado `bloqueante`, o que a disposição libera depende de qual é ela** — a
proibição categórica anterior falhou no próprio documento que a descrevia (o
exemplo canônico da spec era reprovado pelo gate documentado três parágrafos
abaixo):

| disposição      | `revisada` | `validada`                     | exige                         |
| --------------- | ---------- | ------------------------------ | ----------------------------- |
| `nao_se_aplica` | proibida   | proibida                       | — (é autoabsolvição)          |
| `corrigida`     | libera     | libera                         | `decidido_em >= detectado_em` |
| `encaminhada`   | libera     | **proibida enquanto pendente** | `decisao_pendente_de`         |

A trava mora **entre os estados, não na severidade**: `revisada` afirma que a
auditoria terminou e registrou o encaminhamento; `validada` afirma que a regra
pode receber validação institucional, o que não se dá com bloqueante ainda real.
Sem disposição, o bloqueante bloqueia os dois. `encaminhada` chamava-se
`nao_impede` — nome que era verdade pela metade. Contrato em
[`docs/spec/regra.md`](docs/spec/regra.md).

`detectado_em`/`improcedente_em` não podem estar no futuro, checado em
`validate_achado` (não no contrato Pydantic, que não recebe contexto) com `today`
injetável. A leitura passa pelos accessors tipados: o YAML tipa a data conforme o
autor a tenha citado ou não, as duas grafias ocorrem no corpus, e um
`isinstance(..., date)` sobre o dict cru checaria um documento e passaria em
silêncio pelo seguinte. **Os achados que citam a data são a cobertura viva desse
ramo do parser — não os normalize por estilo.**

### Estado da auditoria — P7 (`importada`/`revisada`/`validada`)

Um **join** com `achados/*` e os detectores, reverificado em todo commit — nunca
campo que é válido só porque parseia. `revisada` exige nenhum achado bloqueante
aberto sem disposição que libere e nenhuma detecção P1/P2 ativa que a inclua;
`validada` exige além disso `atos_validacao` não vazio (as perguntas Q12 de fluxo
institucional seguem abertas; nada aqui fixa resposta).

**Rebaixamento nunca é automático** — uma regra que deixa de satisfazer as
invariantes derruba o CI (`P7_ESTADO_INVALIDO`) até que um humano comite o
rebaixamento explícito. `revisada` também exige uma seção `# Estado da análise`
com ao menos um item de checklist e **nenhum desmarcado** (`- [ ]`), o que
substituiu quatro headings fixos que só precisavam existir e ser não vazios —
gate que o literal "TODO" passava. Contar `- [ ]` é forma, nunca mérito: o CI
nunca julga se os itens são os certos.

Ainda **não** exigido: `dispositivos:` não vazio para `revisada` — a infra do P3
resolve toda referência declarada, mas não obriga a declarar.

### Conjunto — `okf/conjuntos/` (P15, RFC 0006)

Um `type: Conjunto` é uma **composição do catálogo, historicamente situada** — o
objeto que faltava para o catálogo poder dizer "esta é a regra em vigor, e esta é
a que a PGE propõe no lugar dela". Editar uma regra é destrutivo: o estado
anterior só sobrevive em `data/raw/` e no git (não consultável).

- **Pertinência é derivada, nunca listada** (`conjunto_schema.resolve`): o
  conjunto carrega **deltas explícitos** — `substituicoes` (grupos atômicos
  `origens_legacy`/`destinos_propostos`, cobrindo 1:N e N:1), `revoga` e
  `introduz` — e
  `regras(C) = regras(base) − origens − revogadas + destinos + introduzidas`.
  Base ausente ou cíclica **levanta** `ResolucaoError` em vez de devolver
  resposta parcial: perder a base em silêncio seria lido como "o catálogo
  encolheu".
- **Os deltas ficam no conjunto, não nas regras.** Revogação pura não tem
  documento sucessor onde se pendurar, e é isso que permite introduzir o objeto
  como no-op *demonstrável*: o frontmatter das regras não muda, então a chave
  material do P2 fica intocada por construção, não por argumento.
- **O escopo entra em `active_regras()`, sobre o conjunto resolvido** — nunca
  filtrando por campo de procedência: uma regra herdada da base pertence ao
  conjunto sem ter sido introduzida por ele. `catalogo_vigente` devolve `None` (e
  não conjunto vazio) quando não há conjunto autorado ou a resolução falha, para
  que um Bundle sintético e um bundle quebrado se comportem como antes — quem
  reporta é `validate_conjuntos`.
- **A raiz não transitou.** `decisao_completude` e ato de ativação são exigidos de
  quem passa de `proposto` a `vigente`; a raiz (`origem: catalogo-legado`, sem
  `base`) apenas registra um estado operacional preexistente, e exigir os campos
  dela fabricaria decisão institucional assinada por ninguém.
- **`scripts/substituicao_schema.py` é o dono do grupo** (tipo canônico,
  validações, proveniência, `selecionar_origem_operacional`). Módulo **neutro** de
  propósito — não em `conjunto_schema`, porque o compilador precisa conhecer *um
  grupo* sem depender do documento agregado; e `DestinoProposto` é um `Protocol`
  estrutural, não a `RegraProposta` concreta, senão a neutralidade seria
  nominal.
- **Duas grafias de identidade, conversão explícita**: o grupo endereça por link
  OKF (`/regras/regra-0022.md`), porque o catálogo resolvido é heterogêneo e o
  prefixo diz de qual bundle o item vem; a regra proposta declara origens por id
  nu (`regra-0022`), seu espaço nativo. `ref_de_regra_legada`/`id_da_ref` são
  funções nomeadas usadas dos dois lados — nunca fatia de string num `if`.
- **Proveniência é o que o resolvedor não prova**: pertinência calcula quem entra
  e quem sai, mas nada nela exige que os destinos reconheçam as origens que o
  conjunto afirma substituir (`P15_PROVENIENCIA_DIVERGENTE`/`_INCOMPLETA`,
  checadas mesmo com o grupo `inativo`).
- **Substitutivas não são `regra-NNNN`**: identidade própria, em bundle separado.
  `_validate_identity` **não** é relaxado, e o bundle legado segue imutável em
  cardinalidade e identidade.

### Catálogo proposto — `okf/regras-propostas/` (RFC 0004)

Um segundo bundle **separado**, com espaço de identidade próprio — nunca um
`regra-NNNN`, nunca um `row_index`. O export operacional do Sisprev continua
saindo integralmente do bundle legado: unidades autoradas existem, mas nenhum
grupo de substituição está ativo.

- **`unidades/*.md`** (`type: RegraProposta`) declaram `origens_legacy` de volta
  às regras de que descendem; o `id` é kebab-case e nunca reusa a forma
  `regra-NNNN`. O loader aceita `unidades/` vazio ou ausente — introduzir o bundle
  nunca exigiu autorar unidade.
- **O grupo de substituição mudou de casa**: um `manifesto-substituicao.yaml`
  global existiu e foi **aposentado sem migração de dado** (nasceu vazio). Os
  grupos vivem em `Conjunto.substituicoes`, com o mesmo contrato — só o portador
  mudou.
- **`compilador_proposta.py`** é o compilador puro A → B, que nunca escreve no
  bundle legado nem no CSV operacional. `preview` admite pendência e é sempre
  `deployable=False`; `deployable` é fail-closed (família `P_COMPILA_*`). A linha
  compilada é checada também **contra os tipos declarados da coluna legada**
  (`_checar_contrato_legado`, reusando `regra_schema.COLUMNS.tipo`): uma unidade de
  "schema válido" ainda falha se os valores projetados não forem valores que o
  alvo legado aceitaria. Texto de `requisito_verificacao_humana` sai de
  `gerar_fundamentacao_projetada` — **template**, nunca inferência dos campos
  `nome`/`fundamentacao*`, e nunca afirmando constatação concreta de caso real.
- **`catalogo_proposto_gate.py`** é o único ponto de integração com o gate:
  `validar_regras.py` acrescenta as violações à mesma lista, então a forma do
  payload `--json` não muda. Doc de unidade malformado vira
  `PROPOSTA_DOCUMENTO_INVALIDO` em vez de levantar, para nunca derrubar o CLI.
  Toda unidade `deployable` é de fato compilada nesse modo e suas pendências viram
  violações **independente de algum grupo a referenciar**, para que "formalmente
  deployable" nunca se confunda com "compila numa projeção válida". A validação de
  grupos roda sobre **todo** conjunto cujo contrato valida, não só o vigente — um
  `proposto` com grupo quebrado tem de falhar quando é autorado, não na promoção;
  cada violação carrega o id do conjunto autor.

### Forma de cálculo — `okf/formas-calculo/` (P16)

Um `type: FormaCalculo` por **fórmula de cálculo do benefício**, decomposta em
`base` (sobre que valor o cálculo começa), `ajustes` (aplicados **em ordem**) e
`limitadores` (piso, teto, regra de excedente). O corpo tem `# Como calcular`,
`# Fórmula`, `# Entradas e saídas` e `# Implementação` com código executável — só
as duas primeiras são exigidas pelo gate, porque exigir código produziria
implementação de fachada.

**A proveniência é por componente, e a lista da forma é derivada.** Cada
`base`/`ajuste`/`limitador` carrega o seu próprio `dispositivos:` não vazio: o
que se afirma é *este* dispositivo funda *este* componente. Uma lista no nível da
forma provaria só que as fontes existem, nunca qual fundamenta o quê — a relação
`critério → dispositivo` aplicada ao cálculo. A união ordenada existe como
`FormaCalculoFrontmatter.dispositivos()`, **derivada**, nunca autorada em duas
pontas. Pela mesma lógica, `teto_rgps_mais_percentual_do_excedente` **exige**
`percentual_excedente`: dizer que há excedente sem dizer quanto é menos do que o
dispositivo diz.

**A inversão é o ponto: a fórmula é a ontologia, e o `tipo_calculo` do Sisprev é
projeção dela**, registrada em `projecao_sisprev` com a `fidelidade`
(`exata`/`parcial`/`sem_representacao`/`pendente`) e justificativa obrigatória
quando não for `exata`. O enum legado **não identifica fórmulas**: seus valores
misturam base, ajuste e limitador no mesmo rótulo, e modelar um documento por
valor do enum canonizaria a confusão. A prova é a `regra-0025`: conferido o art.
40, § 3º na redação da EC 20/1998, a base é a **totalidade da remuneração**
reduzida à **proporção do tempo de contribuição** — combinação sem rótulo. O
`Não identificado` gravado é fiel ao estado do **Sisprev** e falso sobre o estado
do **conhecimento**, e é para isso que `fidelidade: sem_representacao` existe.

Cinco cautelas com consequência no código (detalhe em
`scripts/forma_calculo_schema.py`): **nada é inferido do rótulo legado** — não há
mapeador `tipo_calculo → componentes`, e um teste falha se alguém acrescentar um;
**a regra importada não muda** (ausência de representação é achado sobre o
produto, não lapso); **uma forma é combinação reutilizável**, então nenhum campo
aponta para regras; **`paridade` e reajuste ficam fora** (a fórmula é o cálculo na
concessão; manutenção é outro conceito); e o **vocabulário é pequeno**, só com o
que já foi lido em dispositivo transcrito.

### `precedentes` — casos em que a regra foi aplicada (RFC 0010 §6.1)

Casos concretos no frontmatter da regra, **deliberadamente separados de
`atos_validacao`**. Um ato de validação *aprova* a regra e é condição de
`validada`; um precedente registra que ela foi **usada**. Ter sido aplicada não é
ter sido validada — aliás é no processo que um erro de regra se materializa, e sem
campo próprio quem tem um número de processo em mãos é empurrado para o único
campo que existe, acendendo o selo de `validada` justamente onde há mais motivo
para olhar.

**É aqui que o vínculo com um parecer mora** — o parecer não declara a que regras
se refere, mesma convenção de `dispositivos:` (a regra aponta para fora, o
backlink é derivado); duas pontas declarando a mesma relação seriam duas verdades
sem gate que as reconcilie. Fica **fora da chave material do P2**, junto de
`dispositivos`/`atos_validacao`: duas regras materialmente iguais recebem os
mesmos precedentes e divergiriam só enquanto uma foi anotada e a outra não —
material, o grupo se dissolveria no meio da anotação e se reformaria no fim,
invalidando os achados que o documentam. Vai para o CSV **derivado** em coluna
própria, JSON-codificada. Preenchê-lo depende da decisão de PII da RFC 0010
§4.3, porque um número de processo reidentifica.

### Sentinelas de data — `scripts/sentinela.py` (RFC 0011)

`01/01/1900`, `01/01/1910`, `01/01/1950` e `31/12/2099`, nas quatro colunas de
data. Fonte única do predicado **"limite não-sentinela"**, que já era critério de
auditoria enquanto vivia em prosa em quatro lugares, dois deles discordando.

- **Nomear o conjunto é forma; dizer o que ele significa é mérito, e segue
  aberto.** Daí o nome do membro não significar nada (`D_2099_12_31`):
  `SEM_LIMITE_SUPERIOR` responderia por decreto, num identificador, e todo `if`
  que o lesse herdaria a resposta.
- **`StrEnum` cujo membro é a string exatamente como gravada**, para que a
  constante não vire representação nova e o round-trip byte-idêntico continue de
  pé. Não existe `limite_valido()`: o complemento de "sentinela" é "valor a
  conferir", nunca "valor bom" — `15/12/1998` é não-sentinela e é candidato a erro
  de um dia.
- **O conjunto é autorado**, e `01/01/1969` fica **fora** (suspeita registrada,
  `regra-0003`): suspeita que entra sem ato de ninguém vira decisão de que aquele
  limite não é critério, o modo de falha da RFC 0008. O gate é sobre `data/raw/`,
  imutável, então os números que ele afirma não envelhecem.
- **Sentinela não é limite avaliável no simulador** (`limiteAvaliavel`): não
  exclui, não credita critério, e não sai calada — vira pendência escrita.
  Tratá-la como fronteira de verdade, o que o motor fazia, é interpretá-la.
- **Autoridade sem gate é autoridade nominal.** O porte
  (`site/src/lib/sentinela.ts`) declara os valores num único array `as const` com
  o tipo **derivado** dele, e o pytest compara as duas declarações membro a membro,
  falhando se o padrão não casar — senão dava para mexer no enum Python, manter o
  CI verde e deixar simulador, ficha e relatório com o conjunto antigo. Qualquer
  porte novo de constante fechada precisa do mesmo gate.
- **A ficha e o relatório marcam o valor sem dizer o que ele significa**
  (`NOTA_DE_SENTINELA`, em `regra-fields.ts` — não em `formato.ts`, que converte
  formato e não semântica). A data continua impressa como está gravada, e há teste
  proibindo que a nota contenha "sem limite". No relatório pesa mais: num anexo
  impresso, `31/12/2099` sem ressalva é lido como limite real por quem se
  manifesta.

### `regras/log.md` (P11)

Changelog best-effort derivado da história do git (`regras_log.py`), atualizado
por `gerar_indices.py` mas **fora** do diff gated — um commit que toca `regras/`
não pode incluir o próprio hash antecipadamente, então ele sempre atrasaria um
commit se fosse gated. Num rebase, resolva conflito nele **regenerando**:
escolher um lado perde os commits do outro.

## Site (`site/`, RFC 0003)

Site Astro estático que publica o bundle como projeção navegável e pública —
**derivada e read-only**, mesma regra do CSV: edite a regra no `.md`, nunca em
`site/`. Desenho em
[`docs/rfc/0003-site-estatico-de-publicacao.md`](docs/rfc/0003-site-estatico-de-publicacao.md).
Publicado em `https://franklinbaldo.github.io/sisprev/`.

- **`scripts/emit_site_data.py`** é a ponte da biblioteca Python para o site, e
  nada mais atravessa essa fronteira. **Recusa emitir** se o bundle tiver qualquer violação — o site nunca
  serve um estado que o Python considera quebrado. A saída
  (`site/src/data/dados-do-site.json`) **nunca é comitada**, porque carrega o SHA
  exato da fonte e comitá-la seria autorreferencial. Ela leva só os campos de
  estado de auditoria que os selos precisam; todo outro campo de domínio o Astro
  lê direto do frontmatter via content collections, nunca duplicado.
- **URLs são o id do doc, nunca o `nome`** (`/regras/regra-0006/`). Uma correção
  de `nome` durante a auditoria nunca pode quebrar link compartilhado.
- **`lib/painel.ts`, `lib/filtros.ts` e `lib/relatorio.ts` são puros e não
  importam `site-data.ts`** — o job `test` do CI roda vitest *sem* o emissor,
  então um `*.test.ts` que alcance `dados-do-site.json` quebra o CI mesmo
  passando localmente. Quem liga o puro ao JSON é só `site-data.ts`.
- **Controle morto não aparece**: a barra de filtros e o formulário de busca saem
  do build com `hidden` e **só o JS os revela** (a busca, depois de confirmar que
  o índice carregou). Sem JavaScript a listagem continua inteira. O estado do
  filtro é a query string, então o recorte é compartilhável — rótulo de navegação,
  não identidade.
- **Valor exibido nunca esconde o valor gravado** (`lib/formato.ts`): a ficha lê
  `S`/`N` e `TRUE`/`FALSE` como "Sim"/"Não" mas mostra o bruto ao lado, em
  monoespaçado discreto, para quem audita comparar sem abrir o repositório. Data
  perde só a hora `00:00` (constante e já ignorada na comparação), e é o único
  caso sem bruto ao lado. Valor que não casa com o formato declarado sai verbatim,
  nunca coagido a um default.
- **Relatórios e RFCs publicados**: `docs/analysis/` e `docs/rfc/` são coleções
  (`/relatorios/<id>/`, `/rfcs/<id>/`). Esses `.md` **não têm frontmatter**:
  título, `- **Status**:` e a "Nota:" são lidos do corpo por `lib/documentos.ts`.
  Exigir frontmatter deles seria deformar a fonte para caber no site — aqui é o
  site que se adapta. O corpo sai **verbatim**: quem compara a página com o
  arquivo no GitHub tem de achar o mesmo texto na mesma ordem. Links `.md`
  relativos são reescritos no build (`src/plugins/links-de-documentos.ts`) para a
  URL do site quando o destino é publicado e para `blob/main` quando não é — nunca
  link morto. É plugin **mdast do Sätteri** (`markdown.processor`), não
  `markdown.remarkPlugins`: o Sätteri é o processador padrão desde o Astro 7, e
  usar `remarkPlugins` obrigaria a reinstalar o pipeline `unified` legado para o
  site inteiro. Referência OKF absoluta passa intacta.
- **Busca (`/busca/`, Pagefind)**: índice gerado no `postbuild` sobre o `dist/`
  pronto, logo inexistente em `npm run dev`. O que entra é decidido no HTML:
  `data-pagefind-body` no `<main>` (senão o aviso global e o menu casariam com
  tudo), `data-pagefind-ignore` no que se repete igual em toda ficha (rótulos,
  valor bruto, linha de selos), porque termo presente em toda página não recorta
  nada, e `data-pagefind-meta="selo:..."` para o estado de auditoria voltar a
  aparecer no resultado (§5: selo em toda superfície, e uma lista de resultados é
  uma superfície). O `import` do índice é montado em runtime via `new Function`:
  `/* @vite-ignore */` sozinho não basta — o Vite ainda envolve a chamada no
  helper de preload e deixa um `__VITE_PRELOAD__` por substituir, que estoura no
  navegador.
- **`/simulador/` (RFC 0002)** é a exceção interativa num site estático:
  `lib/simulador.ts` (a
  lógica pura, testada) mais `simulador-client.ts` (cola de DOM, sem regra de
  negócio). Só existem dois resultados: `excluida` (um critério conhecido e
  confirmado exclui a regra) e `nao_excluida` — deliberadamente **não**
  "compatível", já que o motor só checa um punhado de campos parametrizados e
  afirmar compatibilidade seria alegação de completude que ele não sustenta.
  `nao_excluida` sempre carrega suas pendências, e fato não respondido é ele mesmo
  pendência, nunca ignorado em silêncio; quando duas regras compartilham todo
  critério conhecido e diferem só nos campos de resultado candidato, o motor marca
  pendência Q6 explícita nas duas em vez de apresentá-las como múltiplo
  silencioso. Datas são comparadas como datas civis (`{ano, mes, dia}`), nunca
  como `Date`/timestamp — comparar instantes misturaria o fuso de build do
  servidor com o do navegador, fazendo uma fronteira exata casar ou não conforme
  onde o visitante está.
- **CI**: `.github/workflows/site.yml`, deliberadamente **separado** de `ci.yml`,
  para que a toolchain Node nunca toque os gates Python. `typecheck` (`astro check` — o `tsc --noEmit` deste projeto, já que um `tsc` nu não parseia `.astro`
  nem os tipos gerados) e `test` rodam em paralelo, e são **os gates de PR do
  site**. **O `build` roda só em push para `main`** (`if: github.event_name == 'push'`) — ele é o job mais caro do repositório (Node, Astro, Pagefind, Pango do
  sistema, paginação do PDF pelo WeasyPrint), e em PR o artefato do Pages era
  construído e descartado a cada push de toda PR que tocasse `okf/**` ou
  `docs/**`, isto é, praticamente toda PR de auditoria.
  **O que se perde está dito no próprio job, e vale repetir porque esta decisão
  já foi tomada nos dois sentidos**: a prova de que a paginação funciona passa a
  aparecer depois do merge, e o modo de falha que ela cobre não se anuncia — um
  `url_fetcher` que não resolve gera PDF legível e sem nenhuma quebra de página.
  A mitigação é a ordem, não a disciplina: o gatilho `push` filtra por branch
  (`branches: [main]`) mas **não por caminho**, então todo merge roda o `build`
  integralmente, e o `deploy` depende dele — build
  quebrado não chega ao Pages, então o site publicado nunca serve estado que o
  job reprovou. Muda **onde** o sinal aparece, não se aparece. Em PR o
  workflow é filtrado por caminho, e o filtro tem de listar
  **toda** fonte que o site publica (`site/**`, `okf/**`, `docs/**`,
  `scripts/**`, ...), senão uma PR que muda conteúdo publicado entra sem nunca
  ter sido buildada. Já **todo push em `main` roda sem filtro nenhum**: o emissor
  depende da biblioteca Python inteira e a prova de frescor da RFC 0003 §2/§7
  exige que todo push republique, então um filtro ali deixaria o SHA publicado
  atrasar em silêncio. O `deploy` (só em `main`) publica no Pages e roda um smoke
  check confirmando que a página no ar mostra o commit que acabou de ser buildado.

## Relatório de validação da PGE (`/relatorio/` + `docs/relatorio/`)

O catálogo inteiro como **um documento único**, um capítulo por regra, feito para
ser impresso em PDF e juntado ao SEI. Projeção congelada do bundle — gerado,
nunca editado à mão.

- **O texto editorial mora em `docs/relatorio/*.md`**, nunca no `.astro` (coleção
  `textosDoRelatorio`): `abertura.md` (objeto, método, como responder, e o
  título/subtítulo da capa), `notas.md` (uma nota por seção, indexada por
  `## chave`) e `encerramento.md`. Quem redige documento que circula assinado
  precisa reescrever uma frase sem tocar em código. Chave de nota ausente
  **derruba o build** (`nota()` estoura): uma seção sem nota sairia sem aviso num
  documento já juntado ao processo. Totais entram por marcador
  `{{regras}}`/`{{pendencias}}` (`aplicarTotais`, que também estoura em marcador
  desconhecido) — o número muda a cada remessa, então nem vira literal no `.md`
  nem migra para o código. Renderizados pelo **mesmo** processador do site.
- **O capítulo é autocontido**: o texto integral de cada dispositivo citado é
  reimpresso dentro dele, mesmo repetindo a mesma norma em dezenas de capítulos.
  A repetição é o preço de o procurador analisar uma regra sem folhear o volume
  nem abrir sete PDFs da Casa Civil — num anexo, que ninguém lê linearmente, é o
  preço certo. É o que faz o documento ser longo, e ele cresce com as
  transcrições, não com a prosa editorial.
- **`validado_pge` não é insumo, é consequência.** A regra chega `revisada`, o
  relatório é o *instrumento* pelo qual a PGE se manifesta, e só o ato registrado
  em `atos_validacao` depois de assinado vira `validado_pge: TRUE`. Filtrar por
  ele aqui inverteria o laço e produziria documento vazio. Pelo mesmo motivo cada
  capítulo termina com campos de resposta: sem lugar onde a PGE se manifeste, o
  documento informa e não colhe manifestação. Os pontos numerados são os `- [ ]`
  não marcados do corpo, transcritos — forma, nunca mérito, como no P7.
- **WeasyPrint, não navegador headless.** Três recursos de CSS Paged Media
  sustentam o documento e nenhum motor de navegador os implementa: `string-set` (o
  cabeçalho de cada folha diz de que regra ela é), `target-counter` (o número de
  página do sumário é resolvido pelo paginador — um sumário escrito pelo gerador
  mentiria na primeira quebra que mudasse) e `bookmark-level`. `astro-pdf` foi
  descartado por isso. O `url_fetcher` mapeia o `base` do site para dentro do
  `dist/` e **estoura** se um recurso não resolver: um PDF sem folha de estilo é
  gerado assim mesmo, legível e sem nenhuma quebra de página, e o defeito só
  apareceria depois de o anexo estar no processo.
- **`styles/relatorio.css` concentra a aparência do impresso**, separada de
  `site.css` de propósito (o site é lido em tela; o relatório é papel). Paleta
  monocromática, porque um anexo circula impresso em preto e branco. A página não
  usa `BaseLayout`, sai do índice do Pagefind e não entra no menu — ela repete o
  conteúdo de todas as fichas e venceria a ficha própria da regra na busca.
- **O PDF não entra no git** (`site/dist/` é ignorado) **mas é publicado**: o job
  `build` o gera depois do `npm run build` e antes do upload, então ele fica em
  `/sisprev/relatorio-de-validacao.pdf`, ao lado da página que o oferece. O Pango
  é instalado explicitamente no workflow, não herdado da imagem do runner. O que
  identifica um relatório é o commit impresso na capa; reimprimir o mesmo commit
  dá o mesmo documento.
- **O link "Baixar em PDF" só existe na tela** (`@media print` o remove): o
  documento que ele oferece não contém a chamada para si mesmo, e navegação não
  existe dentro de um impresso.

## Rules of the road

- **`data/raw/regras-sisprev.csv` is never written to, by anything, ever.**
  `csv_to_okf.py` only reads it; `okf_to_csv.py` raises
  `OriginalCsvProtectedError` if `--out` resolves to that path
  (`guard_not_original()`). CI's `original-csv-immutable` job independently
  verifies the file has exactly one commit in its history.
- **`csv_to_okf.py` is a one-time bootstrap, not a sync step, and it's enforced.**
  `convert()` raises `BundleAlreadyInitializedError` on an `--out` that already
  has `regra-*.md` docs — pass `--force` only to genuinely discard every audit
  edit since the import. It builds into a temp dir and only replaces `--out` after
  full success, so a crash never leaves a half-written bundle.
- **Edit rules in `.md`, never in a CSV.** After editing any `regra-*.md`, run
  `gerar_indices.py` and commit the resulting `data/regras-sisprev.csv` **and**
  every regenerated `index.md`. CI's `derived-csv-in-sync` job (and
  `tests/test_bundle_sync.py`) fail if any derived artifact doesn't match what the
  current bundle regenerates.
- **Achados are authored sources, not generated.** Detectors only *report*
  mechanical occurrences (`Detection` with a stable `fingerprint`); the auditor
  writes the achado and references the detection by fingerprint. No command ever
  creates or edits an `achado-*.md`, and the detection↔achado bidirectional check
  (P14.6) runs over fingerprints. Achado ids are **append-only** — CI walks the
  full history and fails on any delete or rename.
- **`okf_to_csv.py` validates bundle structure before trusting it.**
  `load_bundle()` raises `BundleIntegrityError` unless every `regra-NNNN.md`'s
  `id`/`row_index` matches its filename and the full set of `row_index` values is
  exactly `1..row_count` with no gaps or duplicates (`_validate_identity()`). A
  doc count that merely "looks right" is not sufficient.
- **Pendência que é igual em todas as regras não vira achado sobre regra
  nenhuma.** Quando a dúvida não decide nada sobre nenhuma regra em particular —
  porque a resposta, se vier, corrige a **convenção** de uma vez e não os
  documentos —, ela é **questionamento geral** e vai para
  `docs/relatorio/abertura.md`, fora dos capítulos e da manifestação por regra.
  Mantê-la como achado aberto sobre a população obrigaria cada regra a escrever
  disposição para um ponto idêntico em todas, que é custo sem contrapartida: o
  gate exige disposição para todo achado aberto que nomeie a regra, então uma
  pendência transversal multiplica prosa por dezenas sem produzir uma decisão
  sequer. `achado-0053` é o caso trabalhado — a pergunta sobre o operador do
  fecho das janelas foi resolvida por **adoção de critério uniforme** e o resíduo
  migrou para o relatório. Achado é para defeito que alcança **estas** regras e
  não aquelas; quando a resposta é a mesma para todo o catálogo, o veículo é
  outro.
- **Adote critério uniforme em vez de suspender a conferência.** Diante de
  ambiguidade que a auditoria não pode resolver sozinha, a saída é declarar a
  leitura, aplicá-la a todo o catálogo e registrar de que premissa ela depende —
  nunca deixar a conferência em aberto regra a regra. Critério declarado e
  errado se conserta num lugar; conferência suspensa não se conserta em lugar
  nenhum, e ainda contamina o que dela dependia.
- **Não escreva contagem em prosa** — nem em documentação, nem em spec, nem em
  RFC, nem em corpo de PR. Quantos testes passam, quantas regras estão num estado,
  quantas páginas o relatório tem: são números que **a árvore já responde** e que
  envelhecem a cada commit, então cada um é uma correção futura obrigatória em
  texto que ninguém releu por outro motivo. O churn é garantido e o valor é zero —
  quem quer o número roda o comando. Quando o número **for** o argumento,
  ancore-o em teste contra `data/raw/`, que é imutável e por isso não envelhece
  (`tests/test_sentinela.py` é o modelo).
- **Nem vocabulário que só é verdade num instante**: "hoje", "atualmente", "ainda
  não", "a única", "a primeira", "nenhuma" — e rótulo de fase em título de seção
  ("Fase B", "fase 0"), porque a seção sobrevive à fase. Envelhecem como um
  número e pior, sem deixar dígito para conferir. Escreva a **afirmação
  estrutural**: "a seção existe onde a análise foi feita, e só ali", não "só uma
  regra tem a seção hoje". Citar um caso como **exemplo** ("a `regra-0025` é um
  caso escrito") não declara quantos existem, e segue válido quando aparecer o
  segundo.
- **`index.md` files never carry frontmatter**, except the bundle-root
  `index.md`'s `okf_version` key (the one exception the spec allows). Dataset-level
  metadata goes on the `Dataset` concept doc (`regras-sisprev.md`).
- **Ruff runs with `select = ["ALL"]`.** Fix violations for real — no `# noqa`
  anywhere in this repo. If a rule is fundamentally wrong for this project, add it
  to `[tool.ruff.lint] ignore` with a comment explaining why.
- **`ty` type-checks the whole project.** `scripts/` is on the module search path
  via `[tool.ty.environment] extra-paths`, not as an installed package — keep it in
  sync with `[tool.pytest.ini_options] pythonpath`.
- Python 3.13+, `from __future__ import annotations` at the top of every module.
- **Dead code**: `uv run vulture scripts/ tests/` catches genuinely unused
  top-level functions/classes — the actionable signal (it once found a real one,
  `regra_schema.column()`). Pydantic fields used to report as unused too, since
  vulture doesn't understand declarative schema fields; fixed for real via
  `[tool.vulture]` mutes plus real attribute access in
  `tests/vulture_whitelist.py`. A new finding means either real dead code or a new
  schema class needing the same treatment. Not part of the CI gate (a whitelist
  can lag a brand-new schema class by one commit) — run it when adding or removing
  functions and Pydantic models.

## Before committing

```bash
uv run ruff format --check
uv run ruff check
uv run ty check
uv run pytest -q
uv run python scripts/md_format.py --check okf docs README.md CLAUDE.md
```

Markdown is held to mdformat's normal form (LF endings, canonical
frontmatter/tables). Every *generated* `.md` already goes through
`md_format.write_markdown`, so `gerar_indices`/`okf_to_csv` output is
byte-idempotent; the check above also covers the *authored* docs. Fix drift with
`uv run python scripts/md_format.py okf docs README.md CLAUDE.md`.

If you edited any `regra-*.md` or `achado-*.md`, regenerate the derived artifacts
and verify no diff is left uncommitted:

```bash
uv run python scripts/gerar_indices.py
git status --porcelain data/regras-sisprev.csv okf/regras-sisprev/*/index.md okf/regras-sisprev/index.md
```

O site tem gates próprios, mas **só `typecheck` e `test` rodam em PR**. O
`build` — que inclui o PDF — roda em push para `main`, então o retorno dele vem
**depois** do merge. Se você mexeu no site, no emissor ou no impresso, rode-o à
mão antes de integrar: aqui é lembrete e não gate, e é justamente por isso que
não rodar tem consequência. E é a única forma de **olhar** o resultado, que o CI
não faz:

```bash
bash site/scripts/emit-data.sh && cd site && npm run check && npm run test && npm run build
cd .. && uv run python scripts/gerar_relatorio_pdf.py
```
