# RFC 0001 — Critérios de validação e processo de auditoria das regras

- **Status**: Proposta (em discussão)
- **Criada em**: 2026-07-17
- **Atualizada em**: 2026-07-17 — incorpora as decisões consolidadas sobre
  P1/P2 (duplicatas resolvidas por inativação documentada, nunca fusão ou
  exclusão; campo `status_regra`; CSV derivado estendido) — ver
  [comentário na PR #2](https://github.com/franklinbaldo/sisprev/pull/2#issuecomment-5005164122).
- **Depende de**: PR #1 (bundle OKF inicial, CSV original congelado, CSV derivado)

> **Convenção de referência**: regras são sempre citadas pelo `id`
> (`regra-NNNN`), nunca por "linha do CSV". A linha física do CSV tem
> deslocamento de +2 em relação ao `row_index` (linha em branco +
> cabeçalho da exportação) — citar "linha 76" quando se quer `regra-0074`
> é um erro fácil e já ocorreu durante a discussão deste RFC. Onde a
> linha física for mencionada, é sempre entre parênteses e como
> informação secundária.

## Contexto

O repositório contém o catálogo de regras de aposentadoria e pensão do
Sisprev como um bundle OKF (`okf/regras-sisprev/`), com o objetivo de
auditar e validar cada regra até que possa ser aplicada no sistema com
segurança jurídica (ver `README.md`). Este RFC propõe **o que** significa
uma regra ser válida — os critérios objetivos que o conjunto de regras deve
satisfazer — e **como** o processo de auditoria deve registrar isso.

A análise da importação original (112 linhas) já revela por que critérios
formais são necessários **antes** de começar a auditoria jurídica de mérito.
Evidências encontradas na própria planilha:

| # | Evidência | Quantidade |
|---|---|---|
| E1 | Nomes duplicados (`NOME` repetido em mais de uma linha) | 41 nomes, cobrindo 94 das 112 linhas |
| E2 | Linhas **100% idênticas** em todas as 27 colunas (redundância pura) | 13 regras em 5 grupos: `regra-0012`/`0013`, `regra-0014`/`0015`, `regra-0065`/`0066`, `regra-0068`–`0070`, `regra-0074`–`0077` (esta última, o Policial Civil Art. 7º §§2º-3º, 4× byte-a-byte igual) |
| E3 | `TIPO_CALCULO = "Não identificado"` (pendência assumida) | 13 regras |
| E4 | `SEXO` e `INTEGRAL` vazios (as mesmas 13 regras de E3, todas de ciclos antigos) | 13 regras |
| E5 | `INTEGRAL = N` (proventos proporcionais) mas `FUNDAMENTACAO_PROPORCIONAL` vazia | 17 regras |
| E6 | Citação inconsistente da mesma norma ("LC 1100/21", "LC 1.100/2021", "Lc nº 1100/21") | recorrente |
| E7 | Contradição interna: regra com `SEXO = MASCULINO` cuja fundamentação cita o dispositivo da **mulher** ("artigo 1º, inciso II, alínea 'b', da LC 51/1985 ... regra transitória - idade + tempo de contribuição + mulher") | ao menos 1 (`regra-0078`) |
| E8 | Pares de regras irmãs com datas suspeitas de digitação em `DATA_ADM_ATE`: `14/06/2021` (`regra-0049`/`0050`) e `09/09/2021` (`regra-0057`/`0058`) onde as gêmeas usam `14/09/2021` — a data da ECE 146/2021 | 4 regras |

O corpus normativo citado é pequeno e fechado: CF/88 (art. 40 em múltiplas
redações), ECs 20/1998, 41/2003, 47/2005, 70/2012, 88/2015, 103/2019, ECE
146/2021, LCs 51/1985, 144/2014, 152/2015, LCEs 432/2008, 949/2017,
1.100/2021, Lei 10.887/2004 e IN nº 5/2020 — cerca de 16 normas. Isso torna
viável a proposta P3 (bundle de dispositivos) sem explosão de escopo.

---

## Propostas

Cada proposta tem um identificador (P1, P2, ...) para referência em
discussões e PRs. As marcadas **[bloqueante]** viram checks automáticos
(teste + CI) quando aceitas; as demais são processo/convenção.

### P1 — Nome único por regra, ativas e inativas [bloqueante]

Toda regra deve ter `title` único **globalmente no bundle** — inclusive as
inativas (ver P2.1): uma regra inativa continua sendo um documento próprio,
referenciável e auditável, e por isso não pode conservar o mesmo nome da
canônica. (`title` é o único campo de nome — o antigo par `title`/`nome`
foi eliminado justamente para não haver dois lugares divergindo.)

Nome é identidade: se duas regras têm o mesmo nome, ou são materialmente a
mesma regra (uma delas será inativada como duplicata — ver P2/P2.1), ou são
regras diferentes que o nome não distingue (e o nome deve ser qualificado
com o que as distingue: sexo, período de admissão, magistério,
proporcional/integral etc.).

Hoje 94 das 112 linhas violam isso (E1). A maioria dos pares difere apenas
em `SEXO` (MASCULINO/FEMININO) ou em `TIPO_CALCULO` — a qualificação
natural é sufixar o nome: p.ex. "… — Feminino", "… — Proporcional". Para
duplicatas inativadas, o sufixo referencia **o `id` da canônica** (nunca
"linha do CSV" — ver a convenção de referência no topo deste RFC):
"… — duplicata de regra-0074".

Check proposto: unicidade de `title` (case- e acento-insensível, espaços
normalizados) sobre todos os `regra-*.md`, ativos e inativos.

### P2 — Duplicidade material entre regras ativas é falha de validação [bloqueante]

Duas regras **ativas** não podem ter exatamente as mesmas propriedades
materiais. Regra duplicada não acrescenta capacidade decisória ao sistema e
multiplica o custo de auditoria — cada correção teria que ser repetida N
vezes, e uma cópia esquecida vira regra divergente silenciosa.

Hoje 13 regras violam isso (E2). **A resolução NÃO é fundir nem excluir**:
cada linha da importação original permanece para sempre representada pelo
seu próprio `regra-*.md` (proveniência integral, e nenhuma mudança nas
invariantes estruturais — `row_count` continua 112, a sequência
`1..row_count` de `_validate_identity()` continua válida). A resolução é
**escolher uma regra canônica e inativar as demais**, de forma documentada
(P2.1).

Enquanto duas ou mais regras ativas forem materialmente idênticas, o
validador emite a violação `P2_DUPLICATA_ATIVA`, registrada como achado
aberto (seção `# Achados`) nos `.md` envolvidos. Depois que as cópias forem
inativadas, o grupo deixa de contar como violação — a P2 compara **somente
regras ativas**.

Check proposto: nenhuma dupla de `regra-*.md` com `status_regra: ativa` e
frontmatter + corpo materialmente iguais (ignorando `id`, `row_index`,
`title` e os campos administrativos/de auditoria de P2.1 e P7).

### P2.1 — Inativação documentada de regras

Novo campo `status_regra` no frontmatter, **separado de `status_auditoria`
(P7)** — são dimensões diferentes: `status_regra` responde se a regra vale
operacionalmente; `status_auditoria` responde em que etapa da revisão
jurídica ela está.

- `status_regra: ativa` — participa do conjunto operacional (default;
  regras sem o campo são tratadas como ativas durante a migração).
- `status_regra: inativa` — permanece no bundle apenas para proveniência,
  auditoria e histórico.

Exemplo de duplicata inativada (grupo real `regra-0074`–`0077`):

```yaml
type: Regra
id: regra-0077
row_index: 77
title: Voluntária do Policial Civil - Art. 7º, §§2º e § 3º da EC nº 146/2021 — duplicata de regra-0074
status_regra: inativa
motivo_inativacao: duplicata
regra_canonica: /regras/regra-0074.md
```

**Regras inativas ficam fora de:** detecção de duplicidade (P2), análise de
cobertura e ambiguidade (P6), contagens operacionais, e qualquer motor
decisório futuro. **Continuam sujeitas a:** todos os checks estruturais e
de integridade documental (`_validate_identity`, P1, frontmatter válido), e
aparecem no CSV derivado (ver P12).

**Efeito na P7:** a inativação **congela** o `status_auditoria` no ponto em
que estiver — uma duplicata inativada não precisa (nem deve) avançar até
`validada_pge`; audita-se somente a canônica. Auditar N cópias idênticas
seria o mesmo trabalho N vezes.

**Nota — `status_regra` ≠ `atualmente_no_sistema`:** inativar no bundle é o
veredito da *auditoria*; o Sisprev real continua com a regra até que alguém
a remova lá (`atualmente_no_sistema` segue refletindo o sistema). A
divergência entre os dois campos é, na prática, **a fila de mudanças a
aplicar no sistema** — um subproduto operacional valioso da auditoria.

Invariantes [bloqueantes]:

- Regra inativa tem `motivo_inativacao` (vocabulário fechado — ver P8;
  inicial: `duplicata`; previstos: `revogada`, `erro_de_importacao`).
- `motivo_inativacao: duplicata` exige `regra_canonica`.
- `regra_canonica` resolve para um `regra-*.md` existente, nunca para a
  própria regra, e nunca para outra duplicata — toda duplicata aponta
  **diretamente** para a canônica; cadeias `A → B → C` são violação.
- `regra_canonica` aponta para uma regra ativa **no momento da inativação**
  (sobre a permanência desse invariante, ver questão em aberto nº 4).
- **Igualdade material verificável para sempre**: em vez de "duplicata ≡
  canônica no momento da inativação" (não re-verificável depois que a
  canônica evolui com a auditoria, enquanto a duplicata fica congelada), o
  invariante permanente é **duplicata inativa ≡ sua própria linha no CSV
  congelado** (recuperada por `row_index`), exceto `title` (renomeado pela
  P1) e os campos administrativos (`status_regra`, `motivo_inativacao`,
  `regra_canonica`, `status_auditoria` e correlatos de P7/P11). Como as
  duplicatas de E2 eram byte-a-byte iguais às canônicas na importação, essa
  formulação prova por transitividade a igualdade original com a canônica —
  e o CI consegue re-verificá-la em qualquer commit futuro.
- Não é necessário `nome_original`: a origem é recuperável por
  `id`/`row_index` na linha correspondente do CSV congelado. O CSV original
  preserva o nome recebido; o `.md` preserva a identidade auditada atual;
  `id`/`row_index` ligam os dois.

Aplicadas as decisões aos 5 grupos reais de E2 (13 regras), o bundle passa
a ter **104 regras ativas + 8 inativas** (uma canônica por grupo). Índice
raiz e doc Dataset devem reportar as duas contagens separadamente.

### P3 — Bundle de dispositivos legais (`okf/dispositivos/`)

Criar um segundo bundle OKF onde **cada `.md` é um único dispositivo
legal** (artigo/parágrafo/inciso/alínea) com o **texto exato** da norma, na
redação aplicável:

```
okf/dispositivos/
├── index.md
├── cf88/
│   ├── art-40-caput-original.md          # redação original de 1988
│   ├── art-40-p1-iii-ec-103-2019.md      # redação dada pela EC 103/2019
│   └── ...
├── ec-41-2003/
│   ├── art-2.md
│   ├── art-6.md
│   └── art-6a-ec-70-2012.md              # 6º-A com redação da EC 70/2012
├── lce-432-2008/
│   ├── art-20.md
│   └── ...
├── lce-1100-2021/
├── ece-146-2021/
└── lc-51-1985/
```

Convenções:

- **Um dispositivo por arquivo**, granularidade mínima citável (inciso ou
  alínea quando a regra cita nesse nível). Frontmatter: `type: Dispositivo`,
  `norma`, `artigo`, `paragrafo`/`inciso`/`alinea` (quando houver),
  `redacao_dada_por` (norma alteradora, se não for a redação original),
  `vigencia_inicio` / `vigencia_fim` (quando revogado/alterado), `fonte`
  (URL oficial — Planalto, ALE/RO ou Diário Oficial).
- **Corpo = texto exato** do dispositivo, sem paráfrase. Se a redação mudou
  ao longo do tempo, cada redação é um arquivo separado (a regra cita a
  redação específica que a fundamenta).
- Regras passam a **linkar** seus dispositivos: no frontmatter de cada
  `regra-*.md`, um campo `dispositivos:` com a lista dos concept IDs
  citados (ex.: `- /dispositivos/cf88/art-40-p1-iii-ec-103-2019.md`), na
  forma de links absolutos do OKF (SPEC.md §5.1).

É isso que transforma a conferência de fundamentação de "abrir o site do
Planalto" em "diff entre o que a regra cita e o que o dispositivo diz" — e
uma mudança legislativa futura vira um diff no bundle de dispositivos que
aponta imediatamente quais regras são afetadas (backlinks).

Check proposto (após adoção): todo item de `dispositivos:` resolve para um
arquivo existente; toda regra auditada (P7 ≥ revisão técnica) tem
`dispositivos:` não vazio.

### P4 — Formato canônico de citação [bloqueante após P3]

Definir uma forma canônica de citar cada norma (ex.: sempre
"LCE nº 1.100/2021", nunca "Lc 1100/21") e um vocabulário fechado de
normas citáveis (o corpus de ~16 normas acima; adições passam por PR no
`okf/dispositivos/`). E6 mostra que hoje a mesma norma aparece com pelo
menos 3 grafias — impossível de verificar mecanicamente.

A fundamentação em prosa continua livre; o que é canônico é o frontmatter
`dispositivos:` (P3). A prosa é para humanos; o frontmatter é para checks.

### P5 — Coerência de janelas temporais [bloqueante]

Para toda regra: `DATA_ADM_APOS ≤ DATA_ADM_ATE` e
`DATA_DIREITO_APOS ≤ DATA_DIREITO_ATE`, com datas parseáveis. (Hoje as 112
passam — o check existe para continuar passando.)

Adicionalmente, documentar as **datas-sentinela** (`01/01/1910`,
`01/01/1950`, `31/12/2099` = "sem limite") como convenção explícita no doc
Dataset, e propor a médio prazo substituí-las por campos vazios com
semântica "aberto" — data mágica parece dado real e engana análises (o
check de E8 só é possível porque 14/09/2021 é a data da ECE 146; sentinela
não carrega essa informação).

Check adicional proposto: datas de marcos legais citadas nas janelas devem
pertencer ao conjunto de datas de vigência das normas do bundle de
dispositivos (16/12/1998 = EC 20, 31/12/2003 = EC 41, 14/09/2021 = ECE 146,
etc.) ou ser sentinela — qualquer outra data exige justificativa no corpo
da regra. Isso teria flagrado E8 automaticamente.

### P6 — Cobertura e não-ambiguidade do espaço de decisão

O conjunto de regras funciona como uma função: dado um perfil de servidor
(sexo, data de admissão, data de aquisição do direito, tipo de benefício,
condição especial), quais regras se aplicam? Dois problemas simétricos:

- **Lacuna**: perfil plausível para o qual nenhuma regra se aplica.
- **Ambiguidade**: duas regras do mesmo `TIPO DE BENEFICIO` cobrindo o
  mesmo perfil com **fundamentação ou cálculo diferentes** sem que haja um
  critério de desempate documentado (concurso de regras é legítimo — o
  servidor pode ter direito à regra mais vantajosa — mas o desempate deve
  ser explícito, não acidente).

Proposta: um script de análise (`scripts/analisar_cobertura.py`) que
particiona o espaço (sexo × janela de admissão × janela de direito × tipo)
e reporta lacunas e sobreposições — considerando **somente regras ativas**
(P2.1). Não-bloqueante no início — o resultado é insumo de auditoria, não
critério pass/fail — até calibrarmos o que é sobreposição legítima.

### P7 — Máquina de estados de validação [bloqueante]

Substituir os booleanos soltos por um fluxo explícito. Estados propostos,
por regra (campo novo `status_auditoria` no frontmatter):

```
importada → em_revisao → revisada → validada_pge → validada_presidencia
                │            │
                └── inconsistente (achado registrado, aguardando correção)
```

Invariantes [bloqueantes]:

- `validado_pge: 'TRUE'` exige `status_auditoria` ≥ `validada_pge`, e
  vice-versa (os campos legados viram derivados do estado).
- Transição para `validada_pge`/`validada_presidencia` **exige referência
  ao ato aprovador** (campo `aprovacao:` com documento/processo SEI/data) —
  ninguém marca TRUE sem apontar o ato que o sustenta.
- Mudança de `status_auditoria` deve ser commit próprio (não misturada com
  correção de conteúdo), com a justificativa na mensagem — o histórico git
  é a trilha de auditoria (quem, quando, por quê).
- Regra em `inconsistente` lista os achados abertos em uma seção
  `# Achados` no corpo do `.md`.

### P8 — Vocabulários fechados (enums) [bloqueante]

`TIPO DE BENEFICIO`, `TIPO_CALCULO`, `SEXO`, `TIPO`, os campos S/N e
TRUE/FALSE, e os campos administrativos novos — `status_regra`
(`ativa`/`inativa`), `motivo_inativacao` (`duplicata`; futuros: `revogada`,
`erro_de_importacao`) e `status_auditoria` (estados da P7) — passam a ter
vocabulário fechado, declarado no doc Dataset (`regras-sisprev.md`), e
verificado por teste. Cada `motivo_inativacao` pode exigir campos próprios
(`duplicata` → `regra_canonica`; `revogada` → referência ao
dispositivo/ato revogador, conectando com P3). `"Não identificado"` em
`TIPO_CALCULO` (13 regras — E3) permanece **permitido, porém marcado**: é
uma pendência explícita que impede a regra de avançar além de `em_revisao`
na máquina de estados (P7).

### P9 — Coerência interna dos campos [bloqueante]

Regras de consistência entre colunas da própria regra:

- `INTEGRAL = S` ⟹ `FUNDAMENTACAO_INTEGRAL` não vazia (hoje: 0 violações);
- `INTEGRAL = N` ⟹ `FUNDAMENTACAO_PROPORCIONAL` não vazia (hoje: **17
  violações** — E5; cada uma vira achado de auditoria);
- `SEXO` vazio só é admissível junto com `TIPO_CALCULO = "Não identificado"`
  (as 13 pendências de E3/E4 — regra nova não pode nascer sem sexo);
- Fundamentação que menciona sexo específico ("mulher", "alínea b") deve
  ser compatível com o campo `SEXO` (teria flagrado E7). Este último começa
  como heurística de alerta, não bloqueio.

### P10 — Validação executável (`scripts/validar_regras.py`) [bloqueante]

Todo critério bloqueante deste RFC vira código: um script que lê o bundle e
reporta violações por proposta (P1, P2/P2.1, P5, P7, P8, P9 — P3/P4 quando
o bundle de dispositivos existir), com saída legível, **códigos estáveis
por violação** (ex.: `P2_DUPLICATA_ATIVA`, `P21_INATIVA_SEM_MOTIVO`,
`P21_CANONICA_INVALIDA`, `P21_CADEIA_DE_DUPLICATAS`,
`P21_DIVERGE_DO_ORIGINAL`) e exit code ≠ 0 em violação. Roda no `pytest`
(um teste por proposta) e no CI como job `validar-regras`.

Importante: as violações **pré-existentes** da importação (E1–E5) entram
numa *baseline* explícita (arquivo `data/baseline-violacoes.json` ou
marcador por regra) — o CI bloqueia **regressões** (violação nova) desde o
dia 1, e a baseline vai encolhendo conforme a auditoria corrige o legado.
Sem isso, o CI nasceria vermelho e seria ignorado.

### P11 — Trilha de auditoria por regra

Convenções de registro (complementa P7):

- `log.md` no diretório `regras/` (formato OKF SPEC.md §7) com o histórico
  agregado de mudanças por data;
- No frontmatter de cada regra: `auditado_por` e `auditado_em` (preenchidos
  na transição para `revisada`);
- Achados que não são da regra em si (ex.: inconsistência entre duas
  regras) viram issues no GitHub, referenciadas na seção `# Achados` das
  regras envolvidas.

### P12 — CSV derivado estendido: colunas originais + campos administrativos [bloqueante]

**Decisão (2026-07-17)**: `data/regras-sisprev.csv` (o export derivado do
bundle) passa a conter **as 27 colunas originais E os campos
administrativos novos** — `status_regra`, `motivo_inativacao`,
`regra_canonica`, `status_auditoria` (e os demais campos de P7/P11 conforme
forem adotados) — como colunas adicionais ao final.

Sem isso, o export do estado atual mentiria por omissão: mostraria 112
regras aparentemente operacionais, sem revelar quais foram inativadas ou em
que estágio de auditoria cada uma está. O CSV derivado existe justamente
para ser "o conteúdo exato das regras atuais" em forma plana — e o estado
atual inclui a dimensão administrativa.

Consequências:

- Só o **congelado** (`data/raw/`) tem formato imutável; o derivado é
  regenerado por script e seu formato evolui junto com o bundle.
- `okf_to_csv.py` emite as colunas administrativas com defaults explícitos
  para regras que ainda não têm os campos (`status_regra: ativa`,
  `status_auditoria: importada`, demais vazios) — o CSV derivado nunca tem
  célula "desconhecida".
- O teste de round-trip do bootstrap (CSV congelado → bundle → CSV) segue
  comparando apenas as 27 colunas originais; o teste de sincronia do
  derivado (`tests/test_bundle_sync.py`) compara o CSV completo, com as
  colunas novas.

---

## O que este RFC não propõe

- **Não** propõe corrigir o mérito jurídico de nenhuma regra — isso é o
  trabalho de auditoria que estes critérios estruturam.
- **Não** propõe alterar `data/raw/regras-sisprev.csv` (congelado, sempre).
- **Não** propõe motor de decisão/simulador — P6 analisa cobertura, não
  executa regras.

## Sequenciamento sugerido

1. **Fase 0** (este RFC aceito): P10 com P1, P2/P2.1, P5, P8, P9 + P12
   (estender o CSV derivado) + baseline das violações legadas. CI passa;
   regressões bloqueadas. Inclui a **primeira ação de auditoria concreta**:
   inativar as 8 duplicatas de E2 (uma canônica por grupo — menor
   `row_index` de cada: `regra-0012`, `regra-0014`, `regra-0065`,
   `regra-0068`, `regra-0074`) e renomeá-las conforme P1.
2. **Fase 1**: P7 (máquina de estados) + P11 — adiciona `status_auditoria`
   a todas as regras (`importada`), define o fluxo dos PRs de auditoria.
3. **Fase 2**: P3 + P4 — bundle `okf/dispositivos/` começando pelas normas
   mais citadas (CF/88 art. 40, ECE 146/2021, LCE 1.100/2021, LCE
   432/2008); regras ganham `dispositivos:` conforme são revisadas.
4. **Fase 3**: P6 (análise de cobertura, só regras ativas) quando houver
   massa crítica de regras revisadas.
5. **Auditoria de mérito**: ciclos 1º → 4º, agora com critérios objetivos e
   checks automáticos por trás.

## Questões resolvidas

1. ~~P2: fundir duplicatas altera `row_count` do bundle vs. importação~~ —
   **resolvida (2026-07-17)**: duplicatas não são fundidas nem excluídas;
   são inativadas com documentação (P2.1). `row_count` e a sequência
   `1..N` permanecem intactos; nenhum check de CI existente precisa mudar
   de forma.
2. ~~CSV derivado carrega os campos administrativos novos?~~ — **resolvida
   (2026-07-17)**: sim, colunas originais + campos novos (P12).

## Questões em aberto

1. P3: granularidade — um arquivo por alínea pode gerar centenas de
   arquivos para a LCE 1.100/2021; começar por artigo e subdividir só onde
   as regras citam mais fino?
2. P5: migrar sentinelas para campos vazios quebra o round-trip com o
   formato da planilha original — vale o custo, ou documentar e conviver?
3. P7: os nomes dos estados e a exigência de ato aprovador com número de
   processo — validar com quem opera o fluxo PGE/Presidência na prática.
4. P2.1: o invariante "`regra_canonica` aponta para regra ativa" deve ser
   **permanente** ou valer só **no momento da inativação**? Se a canônica
   for depois inativada por motivo legítimo (ex.: `revogada`), o invariante
   permanente quebra o CI retroativamente para todas as suas duplicatas.
   Isso pode ser intencional (o CI quebra e força uma re-decisão humana
   explícita — defensável) ou pode-se relaxar para "aponta para regra que
   não é duplicata" (que já proíbe cadeias) + "ativa no momento da
   inativação". Decidir antes de implementar o check.
