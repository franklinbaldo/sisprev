# RFC 0004 — Schema enriquecido da auditoria e compilador determinístico para o schema legado do Sisprev

- **Status**: proposta (2026-07-23). **Especificação revisável, sem
  implementação.** Não edita nenhum `regra-*.md`, não altera o schema de
  produção, o CSV, os dispositivos, os achados, os detectores, o simulador,
  o site nem os workflows. Entrega apenas o desenho: o que se pretende
  construir, confrontado com os parsers e geradores reais do repositório.
  Revisão 2026-07-23 (round 2, após review da PR #29): resolve identidade e
  cardinalidade 1:N das regras auditadas (§1); separa Q6-R de Q6-S no
  requisito constatado pelo IPERON (§7); distingue **preview** de
  **compilação deployável** (§5.3); troca "destino único" por **papéis de
  projeção** (§4/§5); define os **três artefatos-alvo** e a **allowlist** de
  colisão do P2 (§4/§11); corrige os resíduos (datas/Q1-Q2, fonte, `ref` de
  taxonomia, simulador).
- **Parte de / depende de**: [RFC 0001](0001-criterios-de-validacao-das-regras.md)
  (semântica adiada, autoria humana, P2/P2.1/P3/P5/P7/P13, as 27 colunas),
  [RFC 0002](0002-selecao-explicavel-pos-anamnese.md) (seleção explicável,
  papel do `nome`), a spec P13.1
  ([`docs/spec/regra.md`](../spec/regra.md)), o dossiê Q6
  ([`docs/analysis/q6-causa-incapacidade.md`](../analysis/q6-causa-incapacidade.md))
  e a reconciliação invalidez/incapacidade
  ([`docs/analysis/reconciliacao-invalidez-incapacidade.md`](../analysis/reconciliacao-invalidez-incapacidade.md)).
- **Não-objetivo**: implementar a migração; responder qualquer das questões
  Q1–Q12; fechar Q6-S; redigir `fundamentacao*` definitiva para qualquer
  regra; fixar a gramática de `nome`; transformar interpretação provisória
  em gate de CI (princípio da semântica adiada, RFC 0001).

## 0. Decisão de arquitetura que motiva esta RFC

> O schema atual do Sisprev **deixa de ser o limite da análise**. Ele passa
> a ser um **formato-alvo legado** para o qual as regras auditadas serão
> **compiladas**.

Hoje, o frontmatter das 27 colunas **é** a regra deployável (RFC 0001,
P13.2): o auditor edita diretamente `integral`, `tipo_calculo`,
`fundamentacao*`, e o `okf_to_csv.py` projeta isso na CSV derivada. O
problema estrutural, já documentado, é que **a semântica jurídica que
distingue duas regras muitas vezes não cabe em nenhuma das 27 colunas** — o
caso central é a **causa da incapacidade**, pela qual a PGE separa hipóteses
que o catálogo não tem como campo (reconciliação §2, o cruzamento
`0022 × P6/P7`; Q6 §2). O `integral`/`tipo_calculo` são o **resultado já
pré-computado** da causa, nunca o **predicado** que diz *quais* causas o
produzem.

Esta RFC formaliza a separação entre:

- **(A) o schema enriquecido da auditoria** — onde vivem os predicados
  jurídicos estruturados, a classe da causa, os requisitos não
  parametrizáveis, o meio e o responsável pela constatação, a aplicabilidade
  temporal, os dispositivos vinculados, as taxonomias e vigências, e os
  metadados de auditoria (evidência, proveniência, confiança, decisões); e
- **(B) o schema legado do Sisprev, com as 27 colunas** — o formato-alvo,
  para o qual (A) é **compilado** por um passo determinístico.

E define o **contrato do compilador A → B**: toda semântica operacional
necessária à seleção e aplicação de uma regra tem de ser projetável para o
alvo, com **papéis de projeção declarados** (§4), ou a compilação **falha** —
nunca descarta em silêncio.

## 1. Fonte canônica, identidade e cardinalidade das regras auditadas

### 1.1 O que é canônico

A fonte autoral de uma regra continua sendo **um arquivo por regra** (RFC
0001, "autoria humana"; nada aqui reintroduz um banco paralelo). O que muda é
o que, dentro dela, é canônico: acrescenta-se **uma única chave nova de
frontmatter**, `auditoria:` (um mapa aninhado), que passa a carregar a
**semântica operacional canônica** de uma regra **auditada**. As colunas
deployáveis dessa regra tornam-se a **projeção compilada** de `auditoria:`.

### 1.2 O bloqueio de cardinalidade — e por que 1:N é obrigatório

O caso central `0022 → P6/P7` **não cabe** num modelo que exija, ao mesmo
tempo: um bloco `auditoria:` por regra, `causa_incapacidade` **escalar**, uma
linha por classe material, e nenhuma linha legada tocada. `0022` representa
**pelo menos duas** classes de causa (doença catalogada **e** acidente em
serviço). Um escalar não comporta as duas; e a auditoria precisa de duas
linhas materialmente distintas. É preciso decidir a cardinalidade
explicitamente — o que esta revisão faz.

**Precisão sobre o invariante do RFC 0001.** O invariante não é "nenhuma
linha pode ser criada". É: **as linhas importadas são imutáveis — nunca
removidas, renumeradas ou fundidas** (P2/P2.1); "adicionar é permitido — uma
regra nova recebe o próximo `row_index`; a sequência `1..N` vale para
qualquer `N ≥ 112`". Criar é permitido; destruir/renumerar o que existe, não.

**Tensão de CI encontrada (a registrar).** Apesar do texto do RFC 0001, o job
`bundle-imports-original` hoje compara o número de `regra-*.md` com as linhas
do CSV **congelado** (112) e falha se forem diferentes — ou seja, na prática
**proíbe** anexar linhas ao bundle `okf/regras-sisprev/`. Além disso,
`_validate_identity` exige que os `row_index` sejam exatamente `1..row_count`
sem lacunas. Logo, **não** dá para simplesmente "anexar `regra-0113` auditada"
sem contradizer um gate existente.

**Decisão desta revisão — identidade própria + espaço separado + 1:N.**

- A **unidade auditada tem identidade própria**, num **espaço de identidade
  separado** das 112 linhas congeladas — um bundle próprio (nome a ratificar,
  p.ex. `okf/regras-auditadas/`), **não** mais linhas dentro de
  `okf/regras-sisprev/`. Isso mantém o bundle legado congelado em exatamente
  112 (gate `bundle-imports-original` intacto) e é o que de fato **supera** a
  estrutura de 112 linhas em vez de esticá-la.
- Cada regra auditada declara `origens_legacy: [regra-0022]` — o backlink de
  proveniência para a(s) linha(s) legada(s) de onde descende.
- A projeção **legacy → auditada é 1:N**: `regra-0022` decompõe-se em ≥2
  regras auditadas, cada uma com `causa_incapacidade` **escalar** (uma
  classe), cada uma `origens_legacy: [regra-0022]`.
- A projeção **auditada → linha Sisprev é 1:1**: cada regra auditada compila
  para **uma** linha do alvo (uma linha por classe material — Q6 direção A
  preservada, escalar preservado).
- As linhas legadas **não são tocadas** (0022 permanece). A CSV deployável do
  Sisprev passa a ser a projeção de (catálogo auditado, para famílias
  auditadas) ∪ (linhas legadas ainda não auditadas — §13).

**`variantes:` (a alternativa considerada) — rejeitada.** Colocar
`variantes:` dentro de um único `regra-*.md`, cada variante gerando uma linha
Sisprev, quebra a identidade 1:1 documento↔`row_index` que `_validate_identity`
e `bundle-imports-original` exigem (um doc não pode emitir N linhas com
`row_index` estáveis). `origens_legacy` + identidade própria evita isso e
ainda dá a cada linha deployável um `id` estável (que o consumidor do Sisprev
precisa de qualquer forma).

**Decisão em aberto (não inventada aqui).** Quando uma família é auditada, a
linha legada (0022) e suas descendentes auditadas **coexistem**. Inativar a
legada é P2.1, mas o vocabulário fechado de `motivo_inativacao`
(`duplicata`/`erro_de_importacao`) **não** cobre "decomposta em regras
auditadas". Criar esse motivo é decisão de fase futura — até lá a legada
permanece `ativa` e a divergência `status_regra ≠ atualmente_no_sistema`
(RFC 0001, P2.1) representa a fila de migração pendente.

### 1.3 Efeito nos parsers reais (confronto)

| Camada                            | Efeito de `auditoria:` num bundle auditado separado                                                                                    |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `concept.py::parse_concept_doc`   | Nenhum — parser *shape-only*, mapa aninhado carrega normalmente.                                                                       |
| `okf/regras-sisprev/` (112 docs)  | Nenhum — o bundle legado fica congelado; o catálogo auditado é bundle novo. `bundle-imports-original` e `_validate_identity` intactos. |
| `okf_to_csv.py`                   | Inalterado para o legado; o compilador auditado é um novo derivador (§9), sob `gerar_indices` ("derivar").                             |
| `detectors/igualdade_material.py` | Muda de denylist para **allowlist** explícita (§11) — hoje ele considera `dispositivos` material, o que contamina a "colisão em B".    |
| `site/` (Zod `.loose()`)          | Nenhum para quebrar; `emit_site_data.py` emite só os campos de estado que já emite (§12).                                              |

## 2. A fronteira entre semântica operacional e metadados de auditoria

A fronteira **não** coincide com "tudo que está em `auditoria:`". Dentro de
`auditoria:` há dois sub-mundos com regras opostas:

**Semântica operacional (tem de projetar para o alvo, ou a compilação
falha).** Tudo que o Sisprev precisa para **selecionar e aplicar** a regra:

- predicados jurídicos de seleção (classe da causa, regime, marco de
  ingresso, sexo quando relevante);
- requisitos não parametrizáveis (a condição que diferencia a regra, quem
  verifica, por que meio — §7);
- aplicabilidade temporal (janelas, e o marco que rege a versão da norma);
- dispositivos vinculados (P3);
- a parte **discriminante** das taxonomias e suas vigências (a *classe* e
  **qual versão do rol** rege — operacional, não metadado; §5.3/§16.2).

**Metadados de auditoria (podem viver só no catálogo enriquecido).** Não são
necessários à aplicação da regra, então **não** precisam projetar: evidências,
proveniência, URL consultada, MD5/Wayback, `fonte`; confiança; histórico e
decisões de auditoria; notas de reconciliação e perguntas em aberto.

> "Completamente conversível" **não** significa colocar todo metadado de
> auditoria nas 27 colunas. Evidência, URL, confiança, histórico e decisão
> podem permanecer só no catálogo enriquecido, **desde que não sejam
> necessários à aplicação da regra pelo Sisprev**.

É a distinção Q6-R × Q6-S × Q6-T do dossiê Q6 (§1): **predicado da regra**
(Q6-R, catálogo — operacional) vs. **fato do requerente** (Q6-S, solicitação —
fora de escopo e **não resolvido** aqui) vs. **classificação médico-jurídica
versionada** (Q6-T — taxonomia/dispositivos). O §7 trata explicitamente de
não misturar Q6-R com Q6-S.

## 3. O schema enriquecido mínimo

Forma **sugerida** (a validar contra a implementação). Um único bloco
`auditoria:` no frontmatter da regra auditada, com `schema_version`:

```yaml
auditoria:
  schema_version: 1
  origens_legacy: [regra-0022]          # §1.2 — proveniência 1:N

  # --- semântica operacional (projeta para o alvo — §5) ---
  predicados:
    causa_incapacidade: acidente_em_servico   # classe MATERIAL escalar (Q6-R), enum fechado
    regime: lc-1100-2021
    marco_ingresso: apos-2003
    sexo: ambos
  requisitos_nao_parametrizaveis:
    - condicao: nexo entre a incapacidade e o acidente em serviço
      exige_constatacao_no_concessorio: true   # MODAL (Q6-R), não afirma o fato (Q6-S)
      verificador: IPERON
      meio: pericia_oficial
      portador_primario: fundamentacao_integral   # §4 — papel de projeção
  aplicabilidade_temporal:
    # NÃO derivada de `regime` enquanto Q1/Q2 abertas (§5.1) — datas legadas
    # informadas explicitamente e apenas verificadas (P5).
    datas_legadas:
      data_adm_apos: 2004-01-01
      data_adm_ate: null
  taxonomias:
    - ref: /dispositivos/lce-1100-2021/art-30-p5.md   # projeta para `dispositivos:` (P3)
      papel: nexo-acidente

  # --- metadados de auditoria (NÃO projetam — só aqui) ---
  proveniencia:
    fontes_consultadas: ["Casa Civil/DITEL — LC 1.100/2021"]
    confianca: alta
  decisoes:
    - data: 2026-07-23
      quem: <auditor>
      o_que: "face acidente-em-serviço de 0022 (P7); ver reconciliação §2"
```

Princípios:

- **`schema_version` obrigatório** — sem ele a compilação falha (§14).
- **`origens_legacy` obrigatório** numa regra auditada (§1.2) — a
  proveniência 1:N nunca é implícita.
- **`causa_incapacidade` escalar, enum fechado** (Q6 §10.A):
  `acidente_em_servico`, `molestia_profissional`, `doenca_catalogada`,
  `causa_comum`. **Uma classe por regra auditada** (direção A); a lista de
  doenças **não** vira enum nem linha — fica em Q6-T (§16.2).
- **Requisitos não parametrizáveis são modais e estruturados** (§7): a chave
  `exige_constatacao_no_concessorio` afirma o **requisito da regra**, não o
  **fato do requerente**.
- **Metadados de auditoria são livres** e nunca material para colisão (§10/§11).

Confronto: `auditoria:` é *shape-only* para `concept.py`; a validação do bloco
é *on demand* (mesmo padrão de `Regra.admin`/`Achado._validation`), e um erro
no bloco enriquecido nunca esconde um `status_regra`/`status_auditoria`
bem-formado das junções P7/P14 (RFC 0001; regressão de `test_estado_auditoria.py`).

## 4. Os três artefatos-alvo e os papéis de projeção

### 4.1 Três artefatos distintos (não confundir)

O review corretamente apontou que "B = 27 colunas" é impreciso: a RFC também
projeta `taxonomias[].ref` para `dispositivos:`, que **não** é uma das 27. São
**três** artefatos, com papéis diferentes:

1. **CSV importável pelo Sisprev** — **exatamente** as 27 colunas
   (`regra_schema.py::COLUMNS`), ordem congelada. É o que o Sisprev ingere.
2. **Envelope deployável do projeto** — as 27 colunas **+ `dispositivos:`**
   (P3) **+ campos administrativos** (P12). É o que o bundle carrega por regra.
3. **Chave material de colisão (P2)** — uma **allowlist explícita** do que é
   comparado para igualdade material; **não** "tudo menos uma denylist" (§11).

### 4.2 Papéis de projeção (substitui "destino único")

"Destino único" estava errado: `causa_incapacidade` aparece legitimamente em
`nome`, `fundamentacao*`, `integral` e possivelmente `tipo_calculo`/`paridade`.
Isso não é erro — o erro era chamar de destino único. Cada predicado/requisito
operacional projeta em até quatro **papéis**, todos **declarados** e cuja
**coerência o compilador verifica**:

- **portador semântico primário** — onde a condição continua **textualmente
  expressa** (tipicamente `fundamentacao*` para requisito não parametrizável,
  ou um campo estruturado quando existe, p.ex. `sexo`). **Exatamente um** por
  requisito.
- **efeitos derivados** — o resultado já pré-computado: `integral`,
  `tipo_calculo`, `paridade`.
- **representação de interface** — `nome` (§6). Nunca é portador primário nem
  material sozinho (§10).
- **suporte jurídico** — `dispositivos:` (P3) e a citação na fundamentação.

Invariantes do contrato:

- **Exatamente um portador primário** por requisito operacional; **nada
  operacional fica sem papel** (fail-closed — `P_COMPILA_SEM_PORTADOR`).
- **Coerência entre papéis** verificada: p.ex. `causa=acidente_em_servico` ⇒
  `integral=S`; o `nome` tem de carregar o discriminante. Incoerência é
  `P_COMPILA_INCOERENTE`.

## 5. O contrato do compilador (A → B)

```mermaid
flowchart LR
    A["auditoria: (A)\npredicados + requisitos +\naplicabilidade + taxonomias"] --> C{"compilador\ndeterminístico"}
    M["proveniencia/decisoes/confianca\n(metadados de auditoria)"] -.->|nunca projeta| R["permanece só em A"]
    C -->|portador primário| B1["fundamentacao* / campo estruturado"]
    C -->|efeitos derivados| B2["integral, tipo_calculo, paridade"]
    C -->|interface| B3["nome"]
    C -->|suporte jurídico| B4["dispositivos: (P3)"]
    C -->|papel ausente / incoerente| E["ERRO (fail-closed)"]
    C -->|semântica operacional pendente\n(alvo deployable)| E3["ERRO deployable\n(preview passa)"]
    C -->|colisão pós-projeção| E2["ERRO / decisão humana\nexplícita (§10)"]
```

### 5.1 Manifesto de mapeamento (multi-papel)

Fonte única consumida pelo compilador (análogo a `regra_schema.py::COLUMNS`).
Um predicado sem linha no manifesto é `P_COMPILA_SEM_PORTADOR`, nunca default:

| Predicado / requisito (A)             | Portador primário            | Efeitos derivados           | Interface | Suporte jurídico |
| ------------------------------------- | ---------------------------- | --------------------------- | --------- | ---------------- |
| `predicados.sexo`                     | campo `sexo`                 | —                           | `nome`?   | —                |
| `predicados.causa_incapacidade`       | `fundamentacao*`             | `integral` (`tipo_calculo`) | `nome`    | `dispositivos:`  |
| `predicados.regime`/`marco_ingresso`  | `datas_legadas` (ver abaixo) | —                           | `nome`    | `dispositivos:`  |
| `requisitos_nao_parametrizaveis[]`    | `fundamentacao*` (§7)        | —                           | `nome`?   | `dispositivos:`  |
| `taxonomias[].ref`                    | `dispositivos:` (P3)         | —                           | —         | (o próprio ref)  |
| `proveniencia`/`decisoes`/`confianca` | — (não projeta)              | —                           | —         | —                |

**Resíduo datas × Q1/Q2 (corrigido).** `regime`/`marco_ingresso` **não**
geram deterministicamente as quatro datas enquanto Q1/Q2 (inclusividade de
limite, marco jurídico) seguem abertas. Na Fase 1, as datas são **valores
legados informados explicitamente** (`aplicabilidade_temporal.datas_legadas`)
e o compilador apenas **verifica** a consistência estrutural (P5:
`APOS ≤ ATE`, sentinelas preservadas). Gerar datas a partir de `regime` exige
Q1/Q2 resolvidas — até lá, o alvo deployable **carrega o valor explícito ou
para** (`P_COMPILA_PENDENTE`).

### 5.2 Modo de operação por fase (§15)

- **Modo verificação (Fase 1).** As colunas legadas continuam autoradas; o
  compilador projeta A e **confere** contra elas (`P_COMPILA_DIVERGE` em
  divergência). Nada vira derivado ainda.
- **Modo geração (Fase 2, por regra, ato humano).** As colunas da regra
  auditada passam a ser **geradas** por `gerar_indices.py` a partir de A.

### 5.3 Dois níveis de compilação — preview × deployable

Distinção que faltava (e que o fail-closed exige):

- **`preview` (validação do modelo auditado).** **Admite pendências** — um
  campo operacional `pendente` (p.ex. a versão temporal do rol, §16.2) é OK.
  Produz uma projeção **não-deployable**, anotada, para revisão humana do
  modelo. É onde uma redação que **defere** explicitamente uma pendência pode
  aparecer.
- **`deployable` (Sisprev-ready).** **Fail-closed**: qualquer semântica
  operacional não resolvida — versão de rol pendente, marco de data pendente,
  proveniência normativa ausente — **para** a compilação (`P_COMPILA_PENDENTE`
  / `P_COMPILA_SEM_PROVENIENCIA`). Uma regra com questão operacional aberta
  **existe** no schema da auditoria e passa em `preview`, mas **não é
  compilável para deployment**.

Regra: `pendente` num campo **operacional** ⇒ `preview` passa, `deployable`
falha. `pendente` num campo de **metadado** ⇒ irrelevante para ambos.

## 6. Regras de geração de `nome` e `fundamentacao*`

**`nome`** (RFC 0002 §2; spec P13.1) — papel de **interface**, nunca portador
primário nem material sozinho:

- É a **principal interface humana** de seleção após a anamnese — "a menor
  descrição, em linguagem humana, capaz de distinguir a regra das demais".
- Gerado a partir de A com **fatos discriminantes primeiro** (modalidade,
  marco de ingresso, **causa relevante**, integral/proporcional, paridade),
  citação legal por último.
- **Não é discriminante material sozinho** (§10). O discriminante jurídico
  **também** aparece nos campos materiais (`fundamentacao*`, flags, datas,
  cálculo). Dois `nome` diferentes sendo a única diferença **não** tornam as
  regras materialmente distintas — é o comportamento correto do P2 (Q6 §10.B).

**`fundamentacao*`** (portador primário de requisito não parametrizável —
§7): a redação gerada **explicita a condição diferenciadora**, **identifica
quem verifica**, **indica o meio** e **afirma a constatação pelo IPERON no
processo concessório** — como **requisito da regra** (modal), não como fato
consumado (§7). Gerada a partir da estrutura de
`requisitos_nao_parametrizaveis[]`; divergir dela é `P_COMPILA_DIVERGE`.

## 7. Tratamento de requisitos constatados pelo IPERON (Q6-R, não Q6-S)

O review apontou, com razão, que `constatado_no_concessorio: true` **misturava
Q6-R com Q6-S**: dentro da definição da regra, afirmava algo constatado num
requerimento concreto. Correção — no catálogo o campo é **modal**:

```yaml
exige_constatacao_no_concessorio: true
verificador: IPERON
meio: pericia_oficial
```

A regra **exige** que a condição tenha sido constatada; **a constatação
efetiva pertence à solicitação (Q6-S)**, fora do escopo desta RFC. A
`fundamentacao*` gerada é, portanto, condicional ("Aplicável quando o IPERON
houver constatado…") — o que é correto como **predicado de regra**, não como
afirmação sobre um caso.

A base normativa e a redação já foram **validadas contra fonte primária** no
relatório do PR #27 (§4) — citadas aqui como exemplos validados, não
inventadas:

- **Nexo com acidente em serviço** (validado):
  > "Aplicável quando o IPERON houver constatado, mediante perícia oficial, o
  > nexo entre a incapacidade e o acidente em serviço (ou hipótese equiparada,
  > art. 30 §6º) no processo concessório."
- **Existência de incapacidade / readaptação** (validado):
  > "Aplicável quando o IPERON houver constatado o requisito com base em
  > perícia médica oficial do Estado (regime LCE 432/2008) ou em perícia
  > médica oficial por ele indicada (regime LCE 1.100/2021), realizada no
  > processo concessório."

Ressalvas (PR #27): "IPERON" só existe a partir da LCE 1.100/2021 (a LCE
432/2008 fala em "perícia médica oficial do Estado") — a redação respeita o
regime; **moléstia profissional** depende de resolver a pendência **P-6**
(dispositivo não confirmado) → o alvo deployable **falha** por proveniência
ausente, não gera texto. Nada aqui decide essas frases para regra específica.

## 8. Versionamento e migração

- **`schema_version`** (inteiro, começa em `1`); versão desconhecida é erro,
  nunca best-effort. Bump exige compilador que leia a versão anterior ou
  migração de dados explícita e revisável (rigor de P12).
- **Migração por regra e humana** (autoria humana); sem backfill em massa.
- **1:N via `origens_legacy`** (§1.2); nenhuma linha legada é criada,
  removida, renumerada ou fundida em `okf/regras-sisprev/` — o catálogo
  auditado vive em espaço de identidade próprio.
- **Coexistência legado × auditado** gerida por P2.1 (`status_regra`); o
  motivo de inativação da linha decomposta é decisão em aberto (§1.2).

## 9. Compatibilidade com round-trip e geração idempotente

- **Round-trip legado intacto.** `okf/regras-sisprev/` fica congelado em 112;
  `okf_to_csv.py`, `test_roundtrip.py`, `bundle-imports-original` e
  `_validate_identity` **inalterados** (o catálogo auditado é bundle
  separado, §1.2).
- **Idempotência.** A saída do compilador passa pelos mesmos
  `md_format.write_markdown`/serialização já byte-idempotentes; é função pura
  das fontes autorais → cabe sob `gerar_indices` ("derivar", P10). Quando (Fase
  2\) as colunas de uma regra auditada virarem derivadas, entram num
  `git diff --exit-code` como a CSV hoje — prova mecânica da determinística.

## 10. Detectores de equivalência e colisão — dois controles

O `nome` **não deve, sozinho, tornar duas regras materialmente distintas**
(RFC 0001, P1/P2), mas a distinção jurídica também não pode viver só no
`nome`. Daí **dois controles separados**:

**Controle 1 — equivalência semântica em A.** Novo detector sobre os campos
**operacionais** de `auditoria:` (`predicados`, `requisitos_*`,
`aplicabilidade_temporal`, `taxonomias`) — **nunca** sobre
`proveniencia`/`decisoes`/`confianca` (§2). Informativo (camada 2/3): abre
achado, não decide.

**Controle 2 — colisão depois da projeção.** Opera sobre a **chave material
de colisão** (§4.1, item 3 / §11). Reporta regras que **compilam para
combinações indistinguíveis**.

> Se duas regras forem **semanticamente diferentes em A** mas **compilarem
> para combinações indistinguíveis** no alvo, o compilador **falha**
> (`P_COMPILA_COLISAO`) ou **exige decisão humana explícita**. Não se esconde
> a perda de expressividade.

A decisão humana explícita reusa o mecanismo existente: achado
`situacao: resolvido` com **`efeito_deteccao: pode_persistir`**
(`achado_schema.py`) — exatamente o que Q6 §10.B prevê, **sem alterar a chave
material e sem tornar `nome` material**. É o `0022 × P6/P7` (reconciliação §2)
e o Q8 do RFC 0001.

## 11. Impacto no P2/P3 — a correção da chave material

O review corrigiu meu erro anterior: **hoje o P2 é uma _denylist_**
(`igualdade_material.py::_IGNORED_FRONTMATTER_KEYS` = `type`, `id`,
`row_index`, `nome`, `auditado_por`, `auditado_em`, `atos_validacao` +
`ADMIN_FIELD_DEFAULTS`). Como `dispositivos` **não** está na denylist, o P2
**atualmente considera `dispositivos` material**. Logo, "basta adicionar
`auditoria` à denylist e o P2 vira comparação pura da projeção B" era **falso**.

**Correção proposta.** Converter o P2 de denylist para **allowlist explícita**
da **chave material de colisão** — as **27 colunas de domínio menos `nome`**,
derivadas de `regra_schema.py::COLUMNS`. Assim a colisão é definida sobre o
**CSV importável pelo Sisprev** (artefato 1, §4.1), determinístico e livre de
contaminação por campos fora das 27.

**Decisão a ratificar (não silenciosa): `dispositivos` entra na chave de
colisão?** `dispositivos` é do **envelope deployável** (artefato 2), não do
CSV importável (artefato 1). A recomendação é **manter a colisão sobre o
artefato 1** (27 colunas − `nome`), o que **remove `dispositivos` da chave** —
mudança de comportamento em relação ao P2 atual, que precisa ser ratificada e
acompanhada de bump de `VERSION` do detector (invalida fingerprints antigos de
forma controlada, como no v4). O bloco `auditoria:` fica naturalmente fora da
allowlist (não é coluna).

**P3.** Sem mudança de infraestrutura — `taxonomias[].ref` e os dispositivos
usam o `dispositivos:`/`okf/dispositivos/` que já existem
(`check_p3_dispositivos`). **P7** não muda invariante nesta RFC.

## 12. Impacto no simulador e no site

**Simulador** (RFC 0002; PR #28) — descrição corrigida:

> O simulador deve trabalhar com os **campos estruturados da auditoria** e
> **não** deduzir predicados interpretando `nome` ou `fundamentacao*`.

- **Estado real do #28 (corrigido):** hoje o simulador é um **filtro de
  exclusão** (`excluída`/`não-excluída`), **não** um avaliador trivalente
  completo. Ele só declara `excluída` quando um critério **confirmado** exclui
  a regra; caso contrário, `não-excluída` com as pendências listadas.
- O predicado enriquecido (`predicados.causa_incapacidade`) dá ao filtro **o
  que** a regra exige. Mas — ponto do review — **conhecer o predicado da regra
  não é avaliá-lo**: o simulador só pode **excluir** por causa quando **receber
  o fato correspondente do requerente (Q6-S)**. Sem esse fato, a causa
  permanece **pendência**, e a regra continua `não-excluída`. O ganho é: com o
  predicado estruturado, um fato de causa informado passa a **poder excluir**
  regras de outras classes — coisa que hoje é impossível porque a causa "não é
  campo".
- Invariante duro: lê `auditoria.predicados`, **nunca** faz parsing de
  `nome`/`fundamentacao*`.

**Site** (RFC 0003): permanece projeção derivada e read-only; Zod `.loose()`
deixa `auditoria:` passar; `emit_site_data.py` inalterado. Painel futuro que
exponha predicados é aditivo — fora de escopo.

## 13. Estratégia para regras atuais ainda não auditadas

- Uma linha legada **sem** regra auditada correspondente permanece
  **integralmente legado** em `okf/regras-sisprev/`, intocada (nenhuma das 112
  é modificada por esta RFC).
- A CSV deployável do Sisprev é a união: projeção do catálogo auditado (para
  famílias auditadas) ∪ linhas legadas ainda não auditadas.
- O compilador só roda sobre regras auditadas; ausência de auditoria não é
  erro — é o estado default.
- Enriquecimento avança **por família** (invalidez/incapacidade primeiro,
  sobre a reconciliação §2 e os dispositivos do PR #27), sempre por ato humano.

## 14. Testes e gates necessários

- **Determinismo/idempotência**: mesma entrada A ⇒ mesma saída, byte a byte.
- **Papéis completos** (`P_COMPILA_SEM_PORTADOR`): todo requisito operacional
  tem exatamente um portador primário e nenhum campo operacional fica sem
  papel.
- **Coerência entre papéis** (`P_COMPILA_INCOERENTE`): efeitos derivados
  batem com o predicado (causa→integral etc.); `nome` carrega o discriminante.
- **Preview × deployable** (`P_COMPILA_PENDENTE`): campo operacional pendente
  passa em `preview` e **falha** em `deployable` (§5.3).
- **Proveniência normativa** (`P_COMPILA_SEM_PROVENIENCIA`): predicado/requisito
  sem dispositivo/fonte que o sustente falha no alvo deployable (ex.: moléstia
  profissional enquanto P-6 aberta; versão de rol indefinida — §16.2).
- **Verificação** (`P_COMPILA_DIVERGE`): projeção bate com colunas autoradas
  (Fase 1).
- **Colisão pós-projeção** (`P_COMPILA_COLISAO`): sobre a chave material
  (allowlist, §11); salvo achado `pode_persistir` explícito.
- **Equivalência em A** (controle 1): detector informativo (camada 2/3).
- **`schema_version`/`origens_legacy`** presentes e válidos.
- **Gates existentes** seguem valendo sem mudança: `md_format`, `ruff`, `ty`,
  `pytest`, `derived-csv-in-sync`, `original-raw-immutable`, `validar-regras`,
  `bundle-imports-original`.

## 15. Plano incremental de implementação e rollback

| Fase   | Entrega                                                                                                                                                                                                                                                                                                                    | Rollback                                                                 |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **0**  | Esta RFC (spec revisável). Nenhum código, nenhuma regra.                                                                                                                                                                                                                                                                   | Fechar a PR.                                                             |
| **1**  | Bundle auditado (espaço de identidade próprio) + schema enriquecido + compilador em **modo verificação**, com os dois níveis (`preview`/`deployable`) e os papéis de projeção. Detector do controle 1. P2 → allowlist (§11). Simulador lê `auditoria.predicados` quando presente. **Nenhuma coluna legada vira derivada.** | Remover o bundle auditado reverte ao estado 100% legado, sem perda.      |
| **2**  | Virar a canonicidade **por regra auditada** (colunas compiladas/derivadas), uma família por vez, começando por invalidez. Definir o motivo P2.1 de decomposição da linha legada.                                                                                                                                           | Re-materializar as colunas autoradas a partir da última saída compilada. |
| **3+** | Eventual exigência de `auditoria:` para `revisada` (P7) — invariante novo, decisão de fase própria.                                                                                                                                                                                                                        | Reverter o invariante de P7.                                             |

Cada fase é uma PR revisável e independente; nada aqui autoriza pular para a
Fase 1 sem aprovação.

## 16. Exemplos completos de projeção

### 16.1 Exemplo 1 — `0022` decomposta: acidente em serviço (1:N)

`0022` cobre pelo menos duas classes; aqui a **face acidente em serviço**
(hipótese PGE **P7**, LC 1.100/2021, ingresso > 2003). É **uma** das ≥2 regras
auditadas com `origens_legacy: [regra-0022]` (a outra é a face doença,
§16.2) — a projeção **1:N** que o review exigiu.

**Representação enriquecida (A):**

```yaml
auditoria:
  schema_version: 1
  origens_legacy: [regra-0022]
  predicados:
    causa_incapacidade: acidente_em_servico
    regime: lc-1100-2021
    marco_ingresso: apos-2003
    sexo: ambos
  requisitos_nao_parametrizaveis:
    - condicao: nexo entre a incapacidade e o acidente em serviço
      exige_constatacao_no_concessorio: true
      verificador: IPERON
      meio: pericia_oficial
      portador_primario: fundamentacao_integral
  aplicabilidade_temporal:
    datas_legadas: { data_adm_apos: 2004-01-01, data_adm_ate: null }
  taxonomias:
    - ref: /dispositivos/lce-1100-2021/art-30-p5.md
      papel: nexo-acidente
  proveniencia:
    fontes_consultadas: ["Casa Civil/DITEL — LC 1.100/2021"]
    confianca: alta
```

**Projeção (papéis, §4.2):** portador primário do nexo → `fundamentacao_integral`
(redação §7); efeitos derivados → `integral: S`, `tipo_calculo: Valor Médio`,
`paridade: N`; interface → `nome`; suporte jurídico → `dispositivos: ["/dispositivos/lce-1100-2021/art-30-p5.md"]` (o `ref` **projeta** para
`dispositivos:`; resíduo corrigido). Datas: **valores legados verificados**,
não gerados (§5.1). `sexo: AMBOS`; `tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ`.

**`nome` gerado:** `Invalidez por acidente em serviço — ingresso após 2003 (LC 1.100/2021), integral por média, sem paridade`.

**`fundamentacao_integral` gerada:** redação-IPERON validada (§7, nexo).

**Só na auditoria:** `proveniencia`, `confianca`, `decisoes` (o texto verbatim
do dispositivo vive em P3, não é duplicado na regra).

**Situação que faria a compilação falhar:** se a face doença (§16.2) da mesma
`0022` projetasse para a **mesma** chave material (mesmas 27 colunas − `nome`:
`integral: S`, `Valor Médio`, `paridade: N`, mesmas datas, `fundamentacao*`
idêntica), as duas seriam **indistinguíveis no alvo** apesar de distintas em A
(causa diferente) → `P_COMPILA_COLISAO`: ou a redação difere a causa
explicitamente (§7), ou há um achado `pode_persistir` com decisão humana
(§10). O compilador **não** escolhe sozinho.

### 16.2 Exemplo 2 — doença catalogada, rol de versão temporal pendente

A **face doença** de `0022` (classe `doenca_catalogada`). O rol mudou entre
LCE 432/2008 (14 doenças) e LCE 1.100/2021 (16, com "esclerose múltipla"), e
**qual rol rege cada fato gerador** é Q6-T-vigência — **aberto**. Como a versão
do rol **determina quais doenças satisfazem o requisito**, ela é **operacional**,
não metadado (ponto do review).

**Representação enriquecida (A):**

```yaml
auditoria:
  schema_version: 1
  origens_legacy: [regra-0022]
  predicados:
    causa_incapacidade: doenca_catalogada
    regime: lc-1100-2021
    marco_ingresso: apos-2003
  requisitos_nao_parametrizaveis:
    - condicao: doença enquadrada no rol de doença grave/contagiosa/incurável
      exige_constatacao_no_concessorio: true
      verificador: IPERON
      meio: pericia_oficial
      portador_primario: fundamentacao_integral
  aplicabilidade_temporal:
    versao_rol: pendente            # OPERACIONAL e pendente (Q6-T-vigência)
  taxonomias:
    - ref: /dispositivos/lce-1100-2021/art-30-p8.md   # rol 2021 (16 incisos)
      papel: rol-doencas
    - ref: /dispositivos/lce-1100-2021/art-30-p9.md   # rol pré-2021 (14)
      papel: rol-doencas-anterior
  proveniencia:
    confianca: media
    notas: "qual versão do rol rege o caso é Q6-T (aberto)"
```

**`preview` (admite pendência):** projeta a classe (`integral: S`,
`tipo_calculo: Valor Médio`), gera `nome` (`Invalidez por doença catalogada em lei — ingresso após 2003 (LC 1.100/2021), integral por média`) e uma
`fundamentacao_integral` **anotada** que **defere** a versão: "…doença
enquadrada no rol juridicamente aplicável ao caso, **permanecendo pendente a
definição da versão temporal desse rol**." Saída marcada **não-deployable**.

**`deployable` (fail-closed):** **FALHA** com `P_COMPILA_PENDENTE` — a
`versao_rol` é operacional e está `pendente`. Uma regra com essa questão
aberta **existe** em A e passa em `preview`, mas **não** é compilável para
deployment (correção do blocker 3). A redação que "defere" é legítima só em
`preview`, **nunca** num artefato deployable.

**Só na auditoria:** as duas versões do rol como evidência (`art-30-p8` vs.
`art-30-p9`), a nota de que a escolha é Q6-T, `confianca: media`. A **lista de
doenças** nunca vira linha nem enum — é taxonomia Q6-T versionada (Q6 §10.A).

**Outra situação de falha (mesmo em preview):** tentar **fixar** a versão do
rol **sem proveniência normativa** que diga qual data a rege
(`P_COMPILA_SEM_PROVENIENCIA`), ou criar **uma linha por doença**
(contingência B de Q6, não adotada). O correto enquanto Q6-T-vigência estiver
aberta é **não deployar**, não adivinhar.

## 17. Condições de parada honradas por esta RFC

- **Identidade/cardinalidade** (blocker principal): **resolvida** — regra
  auditada com identidade própria, espaço separado, `origens_legacy`, 1:N
  legacy→auditada e 1:1 auditada→linha (§1.2); `variantes:` rejeitada com
  razão; tensão do `bundle-imports-original` registrada e contornada.
- **Round-trip**: claro (lido em `okf_to_csv.py`/`regra_schema.py`); o legado
  fica congelado. Sem bloqueio.
- **Conversibilidade sem perda operacional**: definida via papéis de projeção,
  dos dois níveis preview/deployable e do fail-closed (§4/§5). Metadado fica só
  em A por decisão explícita (§2), não por descarte.
- **Conflito com decisões anteriores**: nenhum — preserva
  P1/P2/P2.1/P3/P5/P7/P13, semântica adiada, autoria humana, Q6 direção A. O
  ajuste do P2 (denylist→allowlist) **corrige** um comportamento hoje
  incorreto (`dispositivos` material), não contraria o RFC 0001.
- **Campo do simulador sem proveniência**: **erro de compilação** deployable
  (§5.3/§14), não default. E conhecer o predicado ≠ avaliá-lo: o simulador só
  exclui por causa quando receber o fato Q6-S (§12).
- **`nome` como único discriminante material**: **rejeitado** — §10 mantém os
  dois controles; `nome` é papel de interface, nunca material sozinho.
- **Q6-S permanece aberta**: esta RFC enriquece só o catálogo (Q6-R). **Não**
  decide onde/quando o fato da causa do **requerente** é obtido/registrado no
  Sisprev real (Q6-S, perguntas 1–4 do dossiê Q6 §9). Nada aqui a declara
  resolvida.

## 18. O que esta RFC não decide (resumo)

Não responde Q1–Q12; não fecha Q6-S; não redige `fundamentacao*` definitiva
para nenhuma regra; não fixa a gramática de `nome`; não escolhe a versão
temporal de nenhum rol; não define o motivo P2.1 da linha legada decomposta;
não resolve as pendências P-1..P-6 do PR #27; não exige `auditoria:` para
`revisada`; não edita `regra-*.md`, schema, CSV, dispositivos, achados,
detectores, simulador, site ou workflows. Entrega a **fronteira, a
identidade/cardinalidade e o contrato** — a implementação é decisão de fases
posteriores, cada uma revisável e reversível.
