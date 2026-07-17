# RFC 0001 — Critérios de validação e processo de auditoria das regras

- **Status**: Proposta (em discussão)
- **Criada em**: 2026-07-17
- **Atualizada em**: 2026-07-17 — incorpora as decisões consolidadas sobre
  P1/P2 (duplicatas resolvidas por inativação documentada, nunca fusão ou
  exclusão; campo `status_regra`; CSV derivado estendido) — ver
  [comentário na PR #2](https://github.com/franklinbaldo/sisprev/pull/2#issuecomment-5005164122) —
  e sobre P3/P5/P7 (dispositivos na menor unidade citada; sentinelas
  mantidas e documentadas; máquina mínima de estados com a regra de
  desenho "estado novo exige invariante novo") — ver
  [segundo comentário](https://github.com/franklinbaldo/sisprev/pull/2#issuecomment-5005233600) —
  e sobre P2.1 (remoção de `regra_canonica`: representante derivada como o
  único membro ativo do grupo; encerramento temporal ≠ inativação) — ver
  [terceiro comentário](https://github.com/franklinbaldo/sisprev/pull/2#issuecomment-5005286024) —
  e sobre a separação detecção × conclusão (evidências são achados a
  investigar, não veredictos; nenhum resultado de auditoria é
  predeterminado) — ver
  [quarto comentário](https://github.com/franklinbaldo/sisprev/pull/2#issuecomment-5005343565).
- **Depende de**: PR #1 (bundle OKF inicial, CSV original congelado, CSV derivado)

> **Convenção de referência**: regras são sempre citadas pelo `id`
> (`regra-NNNN`), nunca por "linha do CSV". A linha física do CSV tem
> deslocamento de +2 em relação ao `row_index` (linha em branco +
> cabeçalho da exportação) — citar "linha 76" quando se quer `regra-0074`
> é um erro fácil e já ocorreu durante a discussão deste RFC. Onde a
> linha física for mencionada, é sempre entre parênteses e como
> informação secundária.

> **Princípio epistemológico — detecção ≠ conclusão**: este RFC define
> critérios, evidências, estados e formas de registrar conclusões — ele
> **não** produz antecipadamente as conclusões de mérito da auditoria que
> pretende organizar. Toda evidência mecânica (igualdade material, data
> divergente, incompatibilidade aparente entre campos, sobreposição) é
> motivo para **abrir um achado e investigar**, nunca um veredito. O
> validador detecta e reporta; quem conclui é a auditoria, e a conclusão é
> registrada com sua justificativa. Antes da investigação, usa-se
> linguagem neutra: "grupo de igualdade material", "registros envolvidos",
> "possível redundância" — não "cópia", "duplicata confirmada" ou
> "canônica".

## Contexto

O repositório contém o catálogo de regras de aposentadoria e pensão do
Sisprev como um bundle OKF (`okf/regras-sisprev/`), com o objetivo de
auditar e validar cada regra até que possa ser aplicada no sistema com
segurança jurídica (ver `README.md`). Este RFC propõe **o que** significa
uma regra ser válida — os critérios objetivos que o conjunto de regras deve
satisfazer — e **como** o processo de auditoria deve registrar isso.

A análise da importação original (112 linhas) já revela por que critérios
formais são necessários **antes** de começar a auditoria jurídica de mérito.
As evidências abaixo são **fatos mecânicos verificados na planilha** — cada
uma justifica abrir um achado e investigar; nenhuma delas é, por si só, uma
conclusão sobre erro, redundância ou qual campo está certo:

| # | Evidência (fato mecânico) | Quantidade |
|---|---|---|
| E1 | Nomes repetidos (`NOME` igual em mais de uma linha) — indicam identidade insuficiente para o bundle; **não provam, por si sós, que as regras sejam iguais** | 41 nomes, cobrindo 94 das 112 linhas |
| E2 | **Grupos de igualdade material**: linhas com as 27 colunas byte-a-byte idênticas na importação congelada — possível redundância **a investigar** (pode haver significado externo não capturado nas colunas, repetição intencional por configuração do sistema, origem em contextos distintos, ou problema de modelagem que exija outra correção) | 13 registros em 5 grupos: `regra-0012`/`0013`, `regra-0014`/`0015`, `regra-0065`/`0066`, `regra-0068`–`0070`, `regra-0074`–`0077` |
| E3 | `TIPO_CALCULO = "Não identificado"` (pendência assumida) | 13 regras |
| E4 | `SEXO` e `INTEGRAL` vazios (as mesmas 13 regras de E3, todas de ciclos antigos) | 13 regras |
| E5 | `INTEGRAL = N` (proventos proporcionais) com `FUNDAMENTACAO_PROPORCIONAL` vazia | 17 regras |
| E6 | Citação da mesma norma com grafias distintas ("LC 1100/21", "LC 1.100/2021", "Lc nº 1100/21") | recorrente |
| E7 | **Incompatibilidade aparente** entre `SEXO = MASCULINO` e fundamentação que cita o dispositivo da mulher ("artigo 1º, inciso II, alínea 'b', da LC 51/1985 ... regra transitória - idade + tempo de contribuição + mulher") — sem conclusão prévia sobre **qual** campo está errado | ao menos 1 (`regra-0078`) |
| E8 | **Datas divergentes** dos marcos legais e das regras relacionadas em `DATA_ADM_ATE`: `14/06/2021` (`regra-0049`/`0050`) e `09/09/2021` (`regra-0057`/`0058`) onde as gêmeas usam `14/09/2021` (data da ECE 146/2021) — divergência a conferir jurídica/documentalmente, não erro de digitação presumido | 4 regras |

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
representante do seu grupo. (`title` é o único campo de nome — o antigo
par `title`/`nome` foi eliminado justamente para não haver dois lugares
divergindo.)

Nome é identidade: nome repetido indica **identidade insuficiente para o
bundle** — não prova que as regras sejam iguais. Se duas regras têm o
mesmo nome, ou pertencem a um grupo de igualdade material (a investigar —
ver P2), ou são regras diferentes que o nome não distingue (e o nome deve
ser qualificado com o que as distingue: sexo, período de admissão,
magistério, proporcional/integral etc.).

Hoje 94 das 112 linhas violam isso (E1). A maioria dos pares difere apenas
em `SEXO` (MASCULINO/FEMININO) ou em `TIPO_CALCULO` — a qualificação
natural é sufixar o nome: p.ex. "… — Feminino", "… — Proporcional". Se a
auditoria concluir pela inativação de um registro por redundância (P2.1),
o sufixo do inativado referencia **o `id` do membro que permaneceu ativo**
(nunca "linha do CSV" — ver a convenção de referência no topo deste RFC):
"… — duplicata de regra-0074". O sufixo é **informativo** — a verdade
normativa é o grupo derivado (P2.1); numa eventual troca posterior de qual
membro fica ativo, o PR retitula os dois lados de qualquer forma.

Check proposto: unicidade de `title` (case- e acento-insensível, espaços
normalizados) sobre todos os `regra-*.md`, ativos e inativos.

### P2 — Igualdade material entre regras ativas é achado a investigar [bloqueante como detecção]

O validador identifica **grupos de regras materialmente idênticas entre as
regras ativas** e registra `P2_DUPLICATA_ATIVA` como achado aberto (seção
`# Achados`) nos `.md` envolvidos. Cada grupo deve ser **investigado** para
determinar se representa redundância indevida, distinção não modelada ou
outro problema de origem. **O RFC não predetermina a resolução.**
Inativação documentada (P2.1) é uma solução **permitida** quando a
auditoria concluir que os registros não representam regras autônomas
distintas — não a única nem a automática.

O que a igualdade material **prova**: que as 27 colunas não distinguem os
registros — evidência forte e suficiente para abrir o achado (dois
registros ativos indistinguíveis multiplicam o custo de auditoria e criam
risco de divergência silenciosa). O que ela **não prova**: que a repetição
é erro, que só um registro deve permanecer operacional, ou qual deles.
Pode haver significado externo não capturado nas colunas, repetição
intencional por configuração do sistema, origem em contextos distintos, ou
um problema anterior de modelagem que exija outra correção.

Em qualquer resolução, **nada é fundido nem excluído**: cada linha da
importação original permanece para sempre representada pelo seu próprio
`regra-*.md` (proveniência integral — nenhum `regra-*.md` importado
desaparece jamais). Isso **não congela o catálogo**: criar regras novas é
parte normal da vida do bundle (legislação nova, distinção que a auditoria
concluir precisar ser modelada) — uma regra nova recebe o próximo
`row_index` da sequência e incrementa o `row_count` do doc Dataset; a
sequência `1..row_count` de `_validate_identity()` continua válida com
qualquer N ≥ 112. O que a integridade proíbe é **remover ou renumerar** o
que já existe, nunca **acrescentar**. (Consequência de implementação: o
check de CI `bundle-imports-original`, que hoje exige contagem exatamente
igual à da importação, passa a exigir **cobertura** — todo `regra-0001..0112`
presente, contagem ≥ 112 — quando a primeira regra nova for criada.)

Estado inicial (até a conclusão de cada investigação): **112 regras
importadas, 112 tratadas como ativas por default, 5 achados de possível
igualdade material envolvendo 13 registros** — e o validador reportando
`P2_DUPLICATA_ATIVA` para os 5 grupos, como deve.

Check proposto: detecção de grupos de `regra-*.md` com `status_regra:
ativa` e frontmatter + corpo materialmente iguais (ignorando `id`,
`row_index`, `title` e os campos administrativos/de auditoria de P2.1 e
P7) → achado, não resolução automática.

### P2.1 — Inativação documentada de regras (mecanismo disponível, não resultado predeterminado)

Esta seção descreve **o mecanismo** que a auditoria usa **quando** (e
somente quando) concluir que um registro não representa uma regra autônoma
distinta. Nada aqui pressupõe que essa conclusão ocorrerá para qualquer
grupo específico.

Novo campo `status_regra` no frontmatter, **separado de `status_auditoria`
(P7)** — são dimensões diferentes: `status_regra` responde se a regra vale
operacionalmente; `status_auditoria` responde em que etapa da revisão
jurídica ela está.

- `status_regra: ativa` — participa do conjunto operacional (default;
  **todas as 112 regras importadas começam ativas**, e regras sem o campo
  são tratadas como ativas durante a migração).
- `status_regra: inativa` — a auditoria **concluiu, com justificativa
  registrada**, que o registro não tem identidade autônoma (motivos
  iniciais: redundância confirmada ou erro de importação); permanece no
  bundle apenas para proveniência, auditoria e histórico.

**Inativação ≠ encerramento temporal** (decisão 2026-07-17): uma regra cuja
janela de aplicação já se encerrou continua `status_regra: ativa` — ela
segue sendo uma regra autônoma, aplicável a fatos pretéritos (*tempus regit
actum*: quem adquiriu direito sob ela continua regido por ela). Revogação
ou término de vigência **não** são motivos de inativação; o encerramento
temporal já está representado pelas janelas de datas da própria regra.

Exemplo **hipotético** — se a auditoria do grupo `regra-0074`–`0077`
concluir que os quatro registros são o mesmo comando normativo e que só um
deve permanecer operacional, o resultado se registra assim:

```yaml
# regra-0074 — único membro ativo do grupo (condição derivada, não campo)
status_regra: ativa
```

```yaml
# regra-0077
type: Regra
id: regra-0077
row_index: 77
title: Voluntária do Policial Civil - Art. 7º, §§2º e § 3º da EC nº 146/2021 — duplicata de regra-0074
status_regra: inativa
motivo_inativacao: duplicata
```

A investigação pode igualmente concluir outra coisa — p.ex. que os
registros se distinguem por algo não capturado nas 27 colunas (caso em que
a correção é **modelar a distinção**, mantendo todos ativos, e o achado se
resolve sem inativação alguma).

**Não existe campo `regra_canonica`** (decisão 2026-07-17): os grupos de
duplicidade são derivados mecanicamente por igualdade material das linhas
no CSV original congelado, e a representante de cada grupo é **inferida**
como o seu único membro ativo. Armazenar o ponteiro repetiria informação
derivável — e com isso desaparecem os checks de autorreferência e de
cadeias `A → B → C`, o risco de ponteiro obsoleto, e a ambiguidade sobre a
"permanência da canônica" (questão que se dissolve em vez de ser
respondida). Trocar a representante é uma transição atômica no mesmo PR:
uma regra passa a `inativa`/`duplicata` e a outra a `ativa` (com os
retítulos correspondentes da P1).

**Regras inativas ficam fora de:** detecção de duplicidade (P2), análise de
cobertura e ambiguidade (P6), contagens operacionais, e qualquer motor
decisório futuro. **Continuam sujeitas a:** todos os checks estruturais e
de integridade documental (`_validate_identity`, P1, frontmatter válido), e
aparecem no CSV derivado (ver P12).

**Efeito na P7:** a inativação **congela** o `status_auditoria` no ponto em
que estiver — um registro inativado não precisa (nem deve) avançar até
`validada`; audita-se somente o membro que permaneceu ativo. Auditar N
registros materialmente idênticos seria o mesmo trabalho N vezes.

**Nota — `status_regra` ≠ `atualmente_no_sistema`:** inativar no bundle é o
veredito da *auditoria*; o Sisprev real continua com a regra até que alguém
a remova lá (`atualmente_no_sistema` segue refletindo o sistema). A
divergência entre os dois campos é, na prática, **a fila de mudanças a
aplicar no sistema** — um subproduto operacional valioso da auditoria.

Invariantes [bloqueantes] — verificados **por grupo de linhas
originalmente idênticas** (grupos derivados do CSV congelado) e por regra:

- Regra inativa tem `motivo_inativacao` (vocabulário fechado — ver P8;
  inicial: `duplicata` e `erro_de_importacao` — **não** existe motivo
  `revogada`: encerramento temporal não é inativação, ver acima).
- Em cada grupo de duplicidade: **no máximo uma regra ativa**; se houver
  membros inativos por `duplicata`, **exatamente uma** regra ativa (a
  representante derivada).
- Toda regra inativa por `duplicata` pertence a um grupo com **mais de uma
  linha original** — ninguém pode ser "duplicata" de nada se sua linha era
  única na importação.
- **Igualdade material verificável para sempre**: duplicata inativa ≡ **sua
  própria linha no CSV congelado** (recuperada por `row_index`), exceto
  `title` (renomeado pela P1) e os campos administrativos
  (`status_regra`, `motivo_inativacao`, `status_auditoria` e correlatos de
  P7/P11). Como os registros de cada grupo de E2 eram byte-a-byte iguais
  entre si na importação, essa formulação prova por transitividade a
  igualdade original dentro do grupo — e o CI consegue re-verificá-la em
  qualquer commit futuro.
- A unicidade global de `title` (P1) continua valendo para todos os
  membros do grupo, ativos e inativos.
- Não é necessário `nome_original`: a origem é recuperável por
  `id`/`row_index` na linha correspondente do CSV congelado. O CSV original
  preserva o nome recebido; o `.md` preserva a identidade auditada atual;
  `id`/`row_index` ligam os dois.

O resultado numérico da auditoria dos 5 grupos de E2 **não é
predeterminado** — depende da conclusão de cada investigação (inativação,
distinção a modelar, ou outra correção). O que o índice raiz e o doc
Dataset devem fazer é reportar as contagens de ativas e inativas
**separadamente**, refletindo o estado corrente do bundle, seja ele qual
for.

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

- **Um dispositivo por arquivo, na menor unidade efetivamente citada
  pelas regras** (decisão 2026-07-17): se a regra cita o artigo, o arquivo
  é o artigo; se cita parágrafo, inciso ou alínea, cria-se o arquivo nessa
  granularidade. A decomposição é **sob demanda** — não se fragmenta
  preventivamente a norma inteira. Frontmatter: `type: Dispositivo`,
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
arquivo existente; toda regra auditada (P7 ≥ `revisada`) tem
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

**Datas-sentinela (decisão 2026-07-17)**: as sentinelas atuais
(`01/01/1910`, `01/01/1950`, `31/12/2099`) **serão mantidas**, para
preservar o round-trip com a planilha original. Elas são documentadas como
**convenção observada** — a hipótese de trabalho é que representam limite
aberto ("sem limite"), mas **não se presume que todas tenham exatamente a
mesma semântica antes da confirmação**: confirmar o significado de cada
sentinela, em cada campo, faz parte da auditoria. Enquanto isso: (a) a
convenção observada e sua condição de hipótese ficam registradas no doc
Dataset; (b) o validador as trata provisoriamente como limite aberto,
nunca como data real (não entram em comparações de marco legal nem em
análises de cobertura como se fossem datas efetivas). Eventual migração
para `null`/campos explícitos fica para RFC/PR próprio.

Check adicional proposto: datas de marcos legais citadas nas janelas devem
pertencer ao conjunto de datas de vigência das normas do bundle de
dispositivos (16/12/1998 = EC 20, 31/12/2003 = EC 41, 14/09/2021 = ECE 146,
etc.) ou ser sentinela — qualquer outra data gera **achado de divergência**
(a conferir jurídica/documentalmente; a data pode estar certa e a
expectativa errada). Teria detectado E8 automaticamente — como achado, não
como veredito de erro de digitação.

### P6 — Cobertura e não-ambiguidade do espaço de decisão

O conjunto de regras funciona como uma função: dado um perfil de servidor
(sexo, data de admissão, data de aquisição do direito, tipo de benefício,
condição especial), quais regras se aplicam? Dois problemas simétricos:

- **Lacuna**: perfil plausível para o qual nenhuma regra se aplica.
- **Sobreposição sem desempate documentado**: duas regras do mesmo
  `TIPO DE BENEFICIO` cobrindo o mesmo perfil com **fundamentação ou
  cálculo diferentes**. Sobreposição **não é previamente erro**: concurso
  de regras é figura legítima (o servidor pode ter direito à regra mais
  vantajosa). O que a análise reporta é a sobreposição **cujo desempate
  não está documentado** — e a auditoria decide, caso a caso, se é
  concurso legítimo (documentar o desempate) ou problema real.

Proposta: um script de análise (`scripts/analisar_cobertura.py`) que
particiona o espaço (sexo × janela de admissão × janela de direito × tipo)
e reporta lacunas e sobreposições — considerando **somente regras ativas**
(P2.1). Não-bloqueante no início — o resultado é insumo de auditoria, não
critério pass/fail — até calibrarmos o que é sobreposição legítima.

### P7 — Máquina mínima de estados de auditoria [bloqueante]

**(Reformulada em 2026-07-17 — substitui a proposta original de 5+
estados.)** Substituir os booleanos soltos pelo **menor conjunto possível**
de estados (campo `status_auditoria` no frontmatter):

```
importada → revisada → validada
```

- `importada` — os invariantes de `revisada` **não estão (ou não estão
  mais) satisfeitos**. Definição negativa, de propósito: uma regra que já
  foi revisada e depois teve um achado bloqueante aberto volta a ser
  `importada` — o histórico de que um dia foi `revisada` fica no git, que
  é a trilha de auditoria. Não existe estado `inconsistente`.
- `revisada` — auditoria técnica concluída: nenhum achado bloqueante
  aberto, nome único (P1), campos coerentes (P9), `dispositivos:`
  vinculados e válidos (P3), sem duplicidade material entre ativas (P2) e,
  se inativa, inativação corretamente justificada (P2.1).
- `validada` — além de `revisada`, existe **documento no SEI** que
  formaliza a validação, registrado em `validacao_sei`.

Não existem `em_revisao`, `aguardando_validacao` ou similares: são estados
de processo — descrevem a agenda de um humano, não um fato sobre a regra —
e quem rastreia "quem está trabalhando em quê" são os PRs e issues.

**As três dimensões são ortogonais e cada uma tem um dono:**
`status_auditoria` = progresso comprovado; `achados` = qualidade (a
existência de problemas é representada por achados, nunca pelo estado);
`status_regra` (P2.1) = vigência operacional.

Exemplo mínimo:

```yaml
status_regra: ativa
status_auditoria: validada
validacao_sei:
  - autoridade: PGE
    processo: "..."
    documento: "..."
    data: 2026-07-17
```

`validacao_sei` é uma **lista** (um item por ato institucional). As colunas
legadas viram derivadas: `validado_pge = TRUE` ⟺ existe entrada da PGE na
lista; idem Presidência. Hoje as duas colunas nunca divergem (112×
FALSE/FALSE — não há evidência empírica de um estado intermediário "PGE
sim, Presidência não"), então um único estado `validada` basta; se o fluxo
institucional confirmar dois atos obrigatórios, muda-se o **invariante** de
`validada` (exigir uma entrada de cada autoridade) sem criar estado novo.
Os campos exatos do registro SEI serão refinados quando o fluxo
institucional for confirmado.

Invariantes [bloqueantes]:

- **Invariantes valem continuamente, não só na transição.** Estado é
  contrato: o CI verifica em todo commit que cada regra satisfaz os
  invariantes do estado que declara (`P7_ESTADO_INVALIDO` quando não). Uma
  regra `revisada` cujo achado bloqueante abre depois vira violação,
  forçando um commit explícito de rebaixamento para `importada` — o
  rebaixamento é *derivável* dos invariantes, sem precisar de estado
  extra.
- Transição para `validada` exige `validacao_sei` não vazio, com documento
  SEI identificável — ninguém marca validada sem apontar o ato que a
  sustenta.
- Mudança de `status_auditoria` deve ser commit próprio (não misturada com
  correção de conteúdo), com a justificativa na mensagem.
- Achados abertos vivem na seção `# Achados` do corpo do `.md`, com o
  schema mínimo da P8.

**Regra de desenho para estados futuros** (catraca contra proliferação):

> Um novo estado só é criado quando muda os invariantes exigidos pelo CI
> ou representa um ato institucional distinto.

Leitura estrita: os dois critérios são um só teste — **estado novo exige
invariante novo verificável**. Um "ato institucional distinto" só qualifica
porque produz um artefato conferível (o documento SEI), e a exigência desse
artefato *é* o invariante novo; ato sem artefato verificável não vira
estado. Dois estados com o mesmo conjunto de invariantes são o mesmo estado
e devem ser fundidos.

Qualquer PR futuro que proponha um estado novo deve preencher este
template:

> **Estado proposto**: X. **Invariantes de CI que passam a valer**: […].
> **Ato institucional**: […]. **Documento verificável exigido**: […].
> **Por que nenhum estado existente cobre isso**: […].

### P8 — Vocabulários fechados (enums) [bloqueante]

`TIPO DE BENEFICIO`, `TIPO_CALCULO`, `SEXO`, `TIPO`, os campos S/N e
TRUE/FALSE, e os campos administrativos novos — `status_regra`
(`ativa`/`inativa`), `motivo_inativacao` (`duplicata` |
`erro_de_importacao` — **sem** `revogada`: encerramento temporal não é
inativação, ver P2.1) e `status_auditoria`
(`importada`/`revisada`/`validada` — P7) — passam a ter vocabulário
fechado, declarado no doc Dataset (`regras-sisprev.md`), e verificado por
teste. `"Não identificado"` em `TIPO_CALCULO` (13 regras — E3) permanece
**permitido, porém marcado**: é uma pendência explícita (achado
bloqueante) que impede a transição para `revisada` (P7).

**Schema mínimo de achados** — como o invariante de `revisada` depende de
"nenhum achado bloqueante aberto", a severidade do achado é estrutural (o
CI decide transições com base nela), então achados não podem ser texto
livre. Cada achado na seção `# Achados` carrega, no mínimo:

- `severidade`: `bloqueante` | `informativo` (enum fechado);
- `situacao`: `aberto` | `resolvido` (enum fechado);
- referência: proposta violada (`P2`, `P9`, …) ou issue/documento externo.

A máquina de estados só é mínima porque a complexidade migrou para os
achados — este schema garante que ela continue verificável lá, em vez de
se esconder em prosa.

### P9 — Coerência interna dos campos [bloqueante]

Regras de consistência entre colunas da própria regra:

- `INTEGRAL = S` ⟹ `FUNDAMENTACAO_INTEGRAL` não vazia (hoje: 0 violações);
- `INTEGRAL = N` ⟹ `FUNDAMENTACAO_PROPORCIONAL` não vazia (hoje: **17
  violações** — E5; cada uma vira achado de auditoria);
- `SEXO` vazio só é admissível junto com `TIPO_CALCULO = "Não identificado"`
  (as 13 pendências de E3/E4 — regra nova não pode nascer sem sexo);
- Fundamentação que menciona sexo específico ("mulher", "alínea b")
  aparentemente incompatível com o campo `SEXO` gera **alerta** (teria
  detectado E7). Heurísticas de texto geram alerta para investigação,
  **nunca conclusão jurídica** — a incompatibilidade aparente não diz qual
  dos dois campos está errado (nem se algum está); isso é a auditoria que
  determina.

### P10 — Validação executável (`scripts/validar_regras.py`) [bloqueante]

Todo critério bloqueante deste RFC vira código: um script que lê o bundle e
reporta violações por proposta (P1, P2/P2.1, P5, P7, P8, P9 — P3/P4 quando
o bundle de dispositivos existir), com saída legível, **códigos estáveis
por violação** (ex.: `P2_DUPLICATA_ATIVA`, `P21_INATIVA_SEM_MOTIVO`,
`P21_GRUPO_SEM_ATIVA`, `P21_GRUPO_MULTIPLAS_ATIVAS`,
`P21_DUPLICATA_SEM_GRUPO`, `P21_DIVERGE_DO_ORIGINAL`,
`P7_ESTADO_INVALIDO`) e exit code ≠ 0 em violação. Roda no `pytest` (um
teste por proposta) e no CI como job `validar-regras`.

A implementação da P7 é uma tabela **estado → conjunto de predicados**,
verificada continuamente para toda regra (`invariantes(status(r)) ⊆
fatos(r)`) — não um verificador de transições. É isso que torna o
rebaixamento derivável (P7) e as violações re-verificáveis em qualquer
commit.

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
`status_auditoria` (e os demais campos de P7/P11 conforme forem
adotados) — como colunas adicionais ao final.

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
   regressões bloqueadas. Estado inicial: 112 regras importadas, todas
   ativas por default. A **primeira ação de auditoria concreta** é abrir
   os 5 achados `P2_DUPLICATA_ATIVA` de E2 (13 registros envolvidos) para
   investigação — inativações, se houver, só depois da conclusão de cada
   investigação, registrada com justificativa.
2. **Fase 1**: P7 (máquina mínima) + P11 — adiciona `status_auditoria`
   a todas as regras (`importada`), implementa a tabela estado→predicados
   no validador e define o fluxo dos PRs de auditoria.
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
3. ~~P3: granularidade dos dispositivos~~ — **resolvida (2026-07-17)**:
   menor unidade efetivamente citada pelas regras, decomposição sob
   demanda, sem fragmentar preventivamente a norma inteira.
4. ~~P5: migrar sentinelas quebra o round-trip?~~ — **resolvida
   (2026-07-17)**: sentinelas mantidas (round-trip preservado),
   documentadas no Dataset e tratadas pelo validador como limite aberto;
   eventual migração fica para RFC/PR próprio.
5. ~~P7: nomes dos estados e exigência do ato aprovador~~ — **resolvida
   (2026-07-17)**: máquina mínima `importada → revisada → validada`;
   `validada` exige documento SEI identificável (`validacao_sei`, lista —
   um item por ato); estados de processo e `inconsistente` eliminados
   (problemas são `achados`; rebaixamento é derivável dos invariantes
   contínuos). Estados futuros só via regra de desenho + template (P7).
   Os campos exatos do registro SEI serão refinados quando o fluxo
   institucional for confirmado — refinamento de invariante, não questão
   estrutural aberta.
6. ~~P2.1: permanência do invariante "`regra_canonica` aponta para regra
   ativa"~~ — **dissolvida (2026-07-17)**: o campo `regra_canonica` foi
   removido. Os grupos de duplicidade são derivados mecanicamente do CSV
   congelado e a representante é inferida como o único membro ativo do
   grupo — não há ponteiro para ficar obsoleto, então a pergunta sobre sua
   permanência deixa de existir. Junto, ficou consolidado que encerramento
   temporal (janela de aplicação vencida) **não** é inativação: a regra
   continua `ativa` porque rege fatos pretéritos; `inativa` significa
   descarte de identidade autônoma pela auditoria (`duplicata`,
   `erro_de_importacao`).

## Questões em aberto

Nenhuma no momento — todas as questões levantadas até aqui foram
resolvidas ou dissolvidas (ver acima).
