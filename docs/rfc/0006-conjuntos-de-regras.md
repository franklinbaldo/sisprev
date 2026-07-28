# RFC 0006 — Conjuntos de regras: composição normativa historicamente situada

- **Status**: proposta (2026-07-28), revisão 2 no mesmo dia. **Especificação
  revisável, sem implementação.** Não edita nenhum `regra-*.md`, não altera o
  schema deployável, o CSV derivado, os dispositivos, os achados, os
  detectores, o simulador, o site nem os workflows. Entrega o desenho e o
  confronto com os parsers reais.
- **Numeração**: nasceu como RFC 0005 e foi renumerada — o número 0005 já está
  tomado por `0005-simulacao-markov-stress-test-regras.md`, na branch
  `claude/rfc-0005-markov-simulation-441lez`.
- **Parte de / depende de**: [RFC 0001](0001-criterios-de-validacao-das-regras.md)
  (P2 igualdade material, P2.1 `status_regra`, P7 `status_auditoria`, P14
  achados) e [RFC 0004](0004-schema-enriquecido-e-compilador-para-o-sisprev.md),
  cuja **Fase 1A já está implementada** na branch
  `feat/rfc-0004-fase-1a-catalogo-auditado` — bundle `okf/regras-auditadas/`,
  `unidade_auditada_schema.py`, `manifesto_substituicao.py`,
  `compilador_auditado.py`, `catalogo_auditado_gate.py` e cerca de mil linhas
  de teste. Esta RFC **generaliza** aquela infraestrutura; não constrói uma
  segunda.
- **Não-objetivo**: reabrir a identidade separada da RFC 0004; construir o
  schema enriquecido ou o compilador (§3–§6 de lá); decidir o fluxo
  institucional de validação (Q12 da RFC 0001 continua aberta); alterar
  `data/raw/regras-sisprev.csv`, imutável para sempre; criar qualquer
  substituição concreta — autorar é ato humano.

## 0. O problema

Corrigir a `regra-0006` hoje **substitui** a `regra-0006`. O estado anterior
sobrevive em `data/raw/regras-sisprev.csv` (que é a importação, não estados
intermediários) e no histórico do git (que não é registro consultável: não há
como perguntar a ele "quais regras a PGE propôs alterar" e obter resposta
verificada).

Não existe, portanto, forma de o catálogo dizer a frase de que o fluxo de
validação precisa: *"esta é a regra em vigor, e esta é a que a PGE propõe no
lugar dela"*. A auditoria só sabe expressar o estado final.

O sintoma já está nos dados: `validado_pge` e `validado_presidencia` são
booleanos **por regra**, mas validação é ato de **autoridade sobre um lote**.
Os campos existem; o objeto a que os atos se prendem, não.

A RFC 0004 resolveu **substituição** — uma origem legada e suas descendentes,
atomicamente. Falta o objeto que responde por um **recorte do catálogo
inteiro** sobre o qual uma autoridade se pronuncia de uma vez. É esse o
conjunto.

## 1. O que se herda da RFC 0004 — e o que esta RFC acrescenta

Herdado **sem reabertura** (decisões ratificadas, Fase 1A implementada):

| Decisão                                                             | Onde     |
| ------------------------------------------------------------------- | -------- |
| Bundle legado **imutável** em cardinalidade e identidade            | §1.1/1.4 |
| Unidades auditadas têm **identidade própria, em bundle separado**   | §1.2     |
| Uma regra operacional tem **uma única fonte autoral**               | §1.4     |
| Substituição é **grupo atômico** — 1:N e N:1, ativa e reverte junto | §1.4     |
| Estado da **unidade** ≠ estado do **grupo**                         | §1.4/1.5 |
| `decisao_completude` estruturada, nunca prosa                       | §1.4     |
| Exportador escolhe **uma** origem; origem dupla é erro de gate      | §1.5     |
| Chave material do P2 vira **allowlist** das 27 colunas menos nome   | §11      |

Acrescentado aqui, e só isto:

**(a) O manifesto vira documento OKF, por conjunto.** A Fase 1A guarda os
grupos num `okf/regras-auditadas/manifesto-substituicao.yaml` global. Um YAML
solto é um segundo lugar para a verdade morar: sem contrato de concept doc,
sem índice derivado, sem página no site. Aqui os grupos passam a viver num
`type: Conjunto`, com o **mesmo formato** de `GrupoSubstituicao` que a Fase 1A
já validou (`grupo`/`origens_legacy`/`destinos_auditados`/`estado_grupo`/
`decisao_completude`) — é migração de moradia, não de schema.

**(b) A unidade de agrupamento é generalizada.** O grupo da RFC 0004 é *por
origem legada*. Isso resolve decomposição, mas não resolve "as regras que a PGE
pretende validar", que não é um grupo por origem: é um recorte do catálogo. Um
conjunto é esse recorte, e contém zero ou mais grupos.

**(c) Revogação e introdução puras.** A RFC 0004 não as representa:
`origens_legacy` e `destinos_auditados` têm ambos `min_length=1`, então uma
regra que **sai sem sucessora** e uma unidade que **entra sem antecessora** não
cabem em grupo nenhum. As duas são resultados legítimos de validação, e ganham
campos próprios no conjunto (§3).

## 2. O conceito

Um **conjunto** é uma composição do catálogo, historicamente situada, sobre a
qual uma autoridade pode se pronunciar de uma vez.

```
okf/conjuntos/
├── index.md              # listagem derivada, sem frontmatter
├── catalogo-legado.md    # type: Conjunto — raiz; origem = o bundle legado
└── pge-2026.md           # type: Conjunto — o que a PGE propõe alterar
```

| campo                | obrigatório | papel                                                     |
| -------------------- | ----------- | --------------------------------------------------------- |
| `type`               | sim         | `Conjunto`                                                |
| `id`                 | sim         | igual ao nome do arquivo; falante, não numerado           |
| `nome`               | sim         | como o conjunto é citado fora daqui                       |
| `situacao`           | sim         | `proposto` \| `vigente` \| `superado` \| `arquivado` (§6) |
| `origem`             | condicional | só na raiz: `catalogo-legado`; a raiz não tem `base`      |
| `base`               | condicional | id de outro conjunto; obrigatório fora da raiz            |
| `substituicoes`      | não         | lista de grupos atômicos (§3)                             |
| `revoga`             | não         | links OKF de regras que saem sem sucessora                |
| `introduz`           | não         | links OKF de unidades que entram sem antecessora          |
| `autoridade`         | não         | quem responde por ele                                     |
| `atos`               | não         | atos institucionais, com `efeito` e `escopo` (§5)         |
| `decisao_completude` | condicional | obrigatória para `situacao: vigente`                      |

O corpo é a análise humana: por que o conjunto existe, o que pretende mudar, o
que ficou de fora.

## 3. Pertinência: derivada dos deltas, nunca listada

O conjunto **não** lista suas regras — carrega os **deltas explícitos**:

```yaml
type: Conjunto
id: pge-2026
base: catalogo-legado
situacao: proposto

substituicoes:
  - grupo: substituicao-regra-0022
    origens_legacy: [/regras/regra-0022.md]
    destinos_auditados:
      - /regras-auditadas/unidades/invalidez-acidente-pos-2003.md
      - /regras-auditadas/unidades/invalidez-doenca-catalogada-pos-2003.md
    estado_grupo: inativo

revoga: [/regras/regra-0017.md]
introduz: []
```

```text
regras(C) = regras(base(C))
          − origens de todo grupo de C
          − revogações de C
          + destinos de todo grupo de C
          + introduções de C
```

**Por que o grupo é declarado e não descoberto.** Seria possível derivar o
grupo juntando as unidades que apontam para a mesma origem. Não serve: o
sistema não tem como saber que faltava escrever uma terceira descendente. A
completude do grupo é decisão humana (`decisao_completude`, RFC 0004 §1.4), e
uma completude inferida do que existe em disco é verdadeira por construção —
não checa nada.

**Por que os deltas ficam no conjunto e não nas regras.** Revogação pura não
tem documento sucessor onde se pendurar. E, como se vê em §7, manter o conjunto
fora dos documentos históricos é o que faz a fase 0 ser um no-op demonstrável
em vez de argumentado.

## 4. `resolve(C)` é a entrada da auditoria

P1, P2 e P7 recebem **`resolve(C)`**, não as regras cujo campo aponte para `C`.
Procedência não é pertinência: uma regra herdada da base pertence a `C` sem ter
sido introduzida por ele.

O caso que prova: uma unidade auditada que repete o `nome` de uma regra
**herdada** só é vista pelo P1 se o P1 rodar sobre o resolvido. É exatamente
para isso que o P1 existe.

**O catálogo resolvido é heterogêneo** — regras legadas de 27 colunas e
unidades auditadas de schema enriquecido convivem nele. A comparação acontece
na **projeção**, não na fonte: a RFC 0004 §11 já ratificou que a chave material
do P2 é a allowlist das 27 colunas menos `nome`, definida sobre o CSV
importável. É o que torna o resolvido comparável consigo mesmo.

### 4.1 O conjunto fica fora do fingerprint — e fora da `Detection`

O mesmo grupo P2 herdado igual em dois conjuntos produz duas `Detection` com
fingerprint idêntico. Isso exige dedup, e há duas armadilhas concretas:

- `Detection` é `@dataclass(frozen=True)` com `evidencia: Mapping` — um dict.
  **`set(detections)` levanta `TypeError`**; a dedup é por dicionário
  `fingerprint -> Detection`.
- Guardar o conjunto **dentro de `evidencia`** parece inócuo porque o P2 monta
  o `canonical_subject` sem a evidência — mas o `citacao_nao_vinculada` monta
  **com** (`canonical_json({"regra": ..., **evidencia})`), e o fingerprint dele
  se moveria.

Decisão: o conjunto **não entra na `Detection`**. `collect_detections` roda por
conjunto resolvido, deduplica por fingerprint, e a relação
`fingerprint -> conjuntos` vive num índice à parte. Assim o mesmo problema
material observado em dois contextos continua sendo **um** achado, com a
identidade que já tem.

Nota de escopo: a preservação de fingerprints prometida aqui vale para o
trabalho de conjuntos. A RFC 0004 §11 **moverá** os fingerprints do P2 de
propósito, com bump de `VERSION`, quando a allowlist entrar. São mudanças
distintas e não conflitantes; nenhuma fase desta RFC dá o bump.

## 5. Validação: projeção por conjunto, não campo estático

O join proposto na revisão 1 — "existe um ato da PGE em algum conjunto que
contém a regra" — **não funciona**, e o contra-exemplo é decisivo:

```text
catalogo-legado  contém regra-0006          → validado_pge deve ser N
pge-2026         herda a mesma regra-0006,
                 e tem ato de validação da PGE → validado_pge deve ser S
```

É o **mesmo documento** nos dois conjuntos. Editar o campo para `S` altera o
que o conjunto-base exporta — e a base é história, não rascunho. Não editar faz
o conjunto validado exportar `N`. Um campo estático não representa um estado
que depende do conjunto.

Portanto: `validado_pge`, `validado_presidencia` e `ciclo_de_validacao`
continuam existindo no CSV e no envelope deployável — são campos que o Sisprev
tem —, mas o valor exportado passa a ser **projetado pelo exportador, por
conjunto**, a partir dos atos e do seu escopo. O valor no frontmatter da regra
legada permanece como **evidência do que foi importado**, nunca como fonte do
que se exporta.

É seguro introduzir agora justamente porque não muda nada hoje: verificado, as
112 regras têm `validado_pge: 'FALSE'` e `validado_presidencia: 'FALSE'` sem
exceção, e não há ato nenhum registrado — a projeção do conjunto raiz é `FALSE`
em todas.

**O ato declara efeito e escopo.** "Há um ato da PGE" não basta: um ofício que
apenas encaminha uma proposta não sustenta uma validação.

```yaml
atos:
  - tipo: parecer
    autoridade: pge
    efeito: valida          # valida | encaminha | devolve | arquiva
    escopo: {tipo: conjunto}
    identificador: "..."
    fonte: "..."
    data: 2026-01-01
```

`escopo` é estrutural desde já — `{tipo: regras, regras: [...]}` é forma
reservada — mas **o validador aceita apenas `tipo: conjunto`** enquanto não
houver caso real de validação parcial. Assim o schema não precisa de mudança
incompatível depois, e não se constrói caminho que ninguém andou. Validação
parcial, até lá, é **um conjunto menor**.

Isto não fecha a Q12 da RFC 0001 (quais atos e quais fontes valem
institucionalmente): `efeito` é justamente o campo que deixa a pergunta aberta
com a estrutura pronta.

## 6. Situação: quatro estados

- `proposto` — candidato em tramitação;
- `vigente` — composição oficialmente aplicável;
- `superado` — **foi** vigente e deixou de ser;
- `arquivado` — foi proposto e **nunca** vigeu.

Sem o quarto, o histórico diria que uma proposta recusada foi "superada",
sugerindo uma vigência que nunca houve. Um único estado para isso, não dois:
"rejeitado pela PGE" e "retirado pelo proponente" são institucionalmente
diferentes e idênticos para a máquina de estados; o motivo vai no ato e no
corpo, como `situacao: resolvido` + `# Resolução` faz nos achados.

**Exatamente um** conjunto `vigente` — nem zero, nem dois. O catálogo sempre
tem um estado atual.

## 7. O que **não** muda: o bundle legado

As 112 `regra-NNNN` ficam **intactas**. Concretamente:

- Nenhum `regra-NNNN` novo é criado. Substitutivas são unidades auditadas em
  `okf/regras-auditadas/unidades/`, com identidade própria (RFC 0004 §1.2, Fase
  1A implementada).
- **`_validate_identity` não é relaxado.** A contiguidade `row_index` 1..112
  continua valendo para todo `regra-*.md`, porque nenhum documento sem
  `row_index` entra nesse diretório. A revisão 1 desta RFC propunha relaxá-lo;
  era consequência de pôr a substitutiva no lugar errado, e cai junto com ela.
- **Nenhum campo novo nos 112 documentos.** O conjunto raiz declara
  `origem: catalogo-legado` e o resolvedor seleciona todas as regras
  importadas. Não há edição em massa de documento histórico, e a chave material
  do P2 fica **provadamente** intocada — não por argumento, mas porque o
  frontmatter não muda.

## 8. Invariantes

| código                    | invariante                                                       |
| ------------------------- | ---------------------------------------------------------------- |
| `P15_CONJUNTO_INVALIDO`   | frontmatter fora do contrato; `id` ≠ nome do arquivo             |
| `P15_VIGENTE_AUSENTE`     | nenhum conjunto `vigente`                                        |
| `P15_VIGENTE_MULTIPLO`    | mais de um `vigente`                                             |
| `P15_VIGENTE_SEM_DECISAO` | `vigente` sem `decisao_completude`                               |
| `P15_VIGENTE_SEM_ATO`     | transição a `vigente` sem ato de `efeito` suficiente             |
| `P15_BASE_INEXISTENTE`    | `base` não resolve                                               |
| `P15_BASE_CICLICA`        | a cadeia de `base` fecha ciclo                                   |
| `P15_RAIZ_AMBIGUA`        | conjunto com `base` **e** `origem`, ou sem nenhum dos dois       |
| `P15_ALVO_FORA_DA_BASE`   | origem, revogação ou destino fora de `resolve(base)`             |
| `P15_ALVO_DUPLO`          | a mesma regra alvo de dois grupos, ou substituída **e** revogada |
| `P15_LINK_INEXISTENTE`    | link OKF que não resolve para documento autorado                 |
| `P15_ROW_INDEX_INDEVIDO`  | `row_index` em documento fora do bundle legado                   |

`P15_ALVO_DUPLO` substitui o `P15_SUBSTITUICAO_DUPLA` da revisão 1, que estava
errado: ele proibia duas unidades substituírem a mesma origem, que é exatamente
a decomposição 1:N ratificada na RFC 0004. O alvo pode ter vários destinos
**dentro de um grupo**; o que não pode é pertencer a dois grupos.

**Substituição materialmente idêntica ao alvo fica em camada 3**, não na lista
de rejeição. Motivo verificado: `nome` está em `_IGNORED_FRONTMATTER_KEYS` (e
fora da allowlist do §11 da RFC 0004), então uma substituição que corrige **só
o `nome`** é materialmente idêntica ao alvo — e, pela RFC 0002, o `nome` é o
campo de que todo o fluxo de seleção depende. Rejeitá-la bloquearia a correção
mais provável que existe.

## 9. Confronto com os parsers reais

- **`okf_to_csv.py::_validate_identity`** — inalterado (§7).
- **`igualdade_material.py::_material_key`** — inalterado nesta RFC; a
  conversão para allowlist é da RFC 0004 §11, com bump próprio.
- **`bundle.py::active_regras()`** — ponto único por onde P1/P2 leem o
  catálogo; é ali que `resolve(C)` entra.
- **`estado_auditoria.py`** (P7) — passa a fazer o join dentro do resolvido.
- **`manifesto_substituicao.py`** (Fase 1A) — `GrupoSubstituicao`,
  `validate_manifesto` e `selecionar_origem_operacional` são
  **reaproveitados**; muda de onde os grupos são lidos (do conjunto, não do
  YAML global). O YAML global de produção está vazio (`grupos: []`), então a
  migração não move dado nenhum.
- **`emit_site_data.py` / `content.config.ts`** — coleção de conjuntos nova;
  campos de domínio continuam em `.loose()`.
- **`data/raw/regras-sisprev.csv`** — intocado; `original-csv-immutable`
  continua provando o commit único.

## 10. Plano incremental

**Fase 0 — no-op demonstrável.** `type: Conjunto`, o resolvedor puro, e o
conjunto raiz `situacao: vigente` com `origem: catalogo-legado`. P1/P2/P7 e o
exportador passam a consumir `resolve(C)`. Nenhum documento histórico é
editado. A prova é dupla e já é gate de CI: `derived-csv-in-sync` (CSV byte a
byte) e o baseline de detecções — **não só os 7 fingerprints P2**, mas todo o
camada 3, que passa pelo mesmo caminho: P1=41, P9=17/13/1,
`P4_CITACAO_NAO_VINCULADA`=69, `P4_REDACAO_INEXISTENTE`=8.

**Fase 1 — migração dos grupos.** Os grupos saem do
`manifesto-substituicao.yaml` para os conjuntos. Trivial hoje, porque o de
produção está vazio — e por isso mesmo é a hora de fazer.

**Fase 2 — o primeiro conjunto proposto.** Um `proposto` com `base` no vigente
e um grupo real, exercitando `resolve`, o escopo dos detectores e o detector de
no-op.

**Fase 3 — atos e projeção.** `atos` com `efeito`/`escopo`, e `validado_*`
projetado por conjunto no exportador.

**Fase 4 — ativação.** `proposto → vigente` com `decisao_completude` e ato
suficiente; rollback pelo conjunto inteiro. Depois da fase 3, porque ativar sem
os atos registrados é o que o P7 existe para impedir.

**Fase 5 — site.** `/conjuntos/<id>/` e a cadeia de substituição na ficha.

## 11. Questões em aberto

- **Q1 — Base única?** Recomendação: sim. Uma proposta da PGE e uma da
  Presidência sobre o mesmo vigente são conjuntos irmãos; consolidá-las é um
  conjunto novo com grupos autorados à mão. Merge automático de duas propostas
  jurídicas é conclusão sem autor.
- **Q2 — Id do conjunto raiz.** Única decisão que não posso tomar: o id é
  citável em ofício. `importacao-2024` seria impreciso — o bundle legado foi
  auditado no lugar desde o import, e o estado pré-edição não existe nele.
  Recomendo `catalogo-legado`, que é o que ele é e o nome que a Fase 1A usa.
- **Q3 — Uma unidade auditada pode ser substituída dentro do mesmo conjunto?**
  Recomendação: não. Corrigir uma unidade ainda proposta é editá-la; o registro
  existe para atravessar a fronteira da autoridade, não para versionar rascunho.
- **Q4 — `revoga` versus `status_regra: inativa` (P2.1).** Recomendação: coisas
  distintas. `inativa` é propriedade da regra em qualquer conjunto (foi
  desativada no Sisprev); `revoga` é propriedade da relação entre um conjunto e
  sua base. Confundi-las faria uma proposta não aprovada desativar uma regra em
  produção.
- **Q5 — Ordenação do CSV de um conjunto com substituições.** A ordem total
  normativa da RFC 0004 §1.6 se aplica sem mudança, mas precisa de teste
  próprio: o round-trip byte-idêntico é gate.

## 12. O que esta RFC não decide

- O schema enriquecido e o compilador (RFC 0004 §3–§6).
- A conversão do P2 para allowlist (RFC 0004 §11) e o bump de `VERSION`.
- O fluxo institucional de validação (Q12 da RFC 0001): §5 diz **onde** a
  resposta se registra, não qual é.
- Qualquer substituição concreta. Autorar é ato humano: nenhum comando cria uma
  unidade auditada, como nenhum comando cria um achado.
- Q1–Q5 acima.
