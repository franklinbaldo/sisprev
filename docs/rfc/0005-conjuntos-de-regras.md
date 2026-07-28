# RFC 0005 — Conjuntos de regras e regras substitutivas

- **Status**: proposta (2026-07-28). **Especificação revisável, sem
  implementação.** Não edita nenhum `regra-*.md`, não altera o schema
  deployável, o CSV derivado, os dispositivos, os achados, os detectores, o
  simulador, o site nem os workflows. Entrega o desenho e o confronto com os
  parsers reais do repositório.
- **Parte de / depende de**: [RFC 0001](0001-criterios-de-validacao-das-regras.md)
  (P2 igualdade material, P2.1 `status_regra`, P7 `status_auditoria`, P14
  achados) e [RFC 0004](0004-schema-enriquecido-e-compilador-para-o-sisprev.md),
  cujas decisões ratificadas sobre substituição esta RFC **herda sem
  reabrir** (§1).
- **Não-objetivo**: construir o schema enriquecido nem o compilador da RFC
  0004 (§3–§6 de lá); decidir o fluxo institucional de validação (Q12 da RFC
  0001 continua aberta); alterar `data/raw/regras-sisprev.csv`, que é imutável
  para sempre; criar qualquer regra substitutiva concreta — autorar é ato
  humano, e esta RFC só define onde e como ele se registra.

## 0. O problema: a edição de auditoria é destrutiva

Corrigir a `regra-0006` hoje **substitui** a `regra-0006`. O estado anterior
sobrevive em dois lugares, e nenhum dos dois serve como registro:

- `data/raw/regras-sisprev.csv` guarda a **importação**, não estados
  intermediários da auditoria;
- o histórico do git guarda tudo, mas não é consultável como registro — não
  há como perguntar a ele "quais regras a PGE propôs alterar" e obter uma
  resposta verificada.

Disso decorre que **não existe forma de dizer**, no catálogo, a frase que o
fluxo de validação precisa dizer: *"esta é a regra em vigor, e esta é a que a
PGE propõe no lugar dela"*. A auditoria só sabe expressar o estado final.

Há um sintoma disso já nos dados de produção. `validado_pge` e
`validado_presidencia` são booleanos **por regra**, mas validação é ato de
**autoridade sobre um lote**: a PGE não valida 112 vezes, valida um conjunto,
num processo, com um número. Os campos existem; o objeto a que os atos se
prendem, não. É esse objeto que esta RFC define.

## 1. Relação com a RFC 0004 — o que se herda e o que muda

A RFC 0004 já especificou, e teve **ratificado pelo responsável**, o essencial
do modelo de substituição. Esta RFC **não reabre** nada disso:

| Decisão da RFC 0004                                            | Onde     | Status aqui |
| -------------------------------------------------------------- | -------- | ----------- |
| Bundle legado imutável quanto a cardinalidade e identidade     | §1.1/1.4 | herdada     |
| Uma regra operacional tem **uma única fonte autoral**          | §1.4     | herdada     |
| Substituição é **grupo atômico** — ativa/reverte inteira       | §1.4     | herdada     |
| Estado da **unidade** ≠ estado do **grupo**                    | §1.4/1.5 | herdada     |
| `decisao_completude` estruturada, nunca prosa                  | §1.4     | herdada     |
| Exportador escolhe **uma** origem; origem dupla é erro de gate | §1.5     | herdada     |
| Rollback opera sobre o grupo, sem perder ligação com a origem  | §1.6     | herdada     |

Três coisas mudam, e é o que justifica uma RFC nova em vez de uma revisão:

**(a) O manifesto vira documento OKF.** A RFC 0004 chama o registro de
substituição de "manifesto/envelope" e deixa em aberto onde ele mora e em que
formato. Aqui ele é um **concept doc `type: Conjunto`** no próprio bundle,
sujeito ao mesmo tratamento de tudo o mais: frontmatter tipado, validador,
índice derivado, página no site, gate de CI. Um registro de substituição que
vive fora do bundle é um segundo lugar para a verdade morar — exatamente o
que a §1.4 de lá proíbe em outro contexto.

**(b) A unidade de agrupamento é generalizada.** O grupo da RFC 0004 é
*por origem legada* (`substituicao-regra-0022`: uma regra legada e suas
descendentes). Isso serve à decomposição 1:N, mas **não serve ao fluxo de
validação**, que é o pedido concreto: "as regras que a PGE pretende validar"
não é um grupo por origem, é um recorte do catálogo inteiro sobre o qual uma
autoridade se pronuncia de uma vez. Um conjunto é esse recorte; um grupo de
substituição da RFC 0004 passa a ser **derivável** de um conjunto (as
substituições que ele declara sobre uma mesma origem).

**(c) Funciona sobre o schema atual.** A RFC 0004 constrói substituição
*junto* com o schema enriquecido e o compilador — projeto grande, sem
implementação até hoje. Um conjunto opera sobre os `regra-*.md` de 27 colunas
que já existem. Isso não é atalho: é a constatação de que "poder propor uma
regra no lugar de outra" e "enriquecer o schema" são problemas ortogonais, e
amarrá-los adia o primeiro pelo segundo. Quando o catálogo enriquecido
existir, ele é mais um conjunto.

## 2. O conceito

Um **conjunto** é um estado nomeado e coerente do catálogo, sobre o qual uma
autoridade pode se pronunciar de uma vez.

```
okf/regras-sisprev/conjuntos/
├── index.md              # listagem derivada, sem frontmatter
├── importacao-2024.md    # type: Conjunto — as 112 regras como importadas
└── pge-2026.md           # type: Conjunto — o que a PGE propõe alterar
```

Frontmatter de `type: Conjunto`:

| campo                | obrigatório | papel                                                                                  |
| -------------------- | ----------- | -------------------------------------------------------------------------------------- |
| `type`               | sim         | `Conjunto`                                                                             |
| `id`                 | sim         | igual ao nome do arquivo; falante, não numerado (§2.1)                                 |
| `nome`               | sim         | como o conjunto é chamado fora daqui                                                   |
| `base`               | não         | id de outro conjunto; ausente = conjunto-raiz                                          |
| `situacao`           | sim         | `proposto` \| `vigente` \| `superado`                                                  |
| `autoridade`         | não         | quem responde por ele (PGE, Presidência, auditoria)                                    |
| `atos`               | não         | lista no formato de `atos_validacao` (P7): `tipo`/`autoridade`/`identificador`/`fonte` |
| `decisao_completude` | condicional | obrigatória para `situacao: vigente` (RFC 0004 §1.4)                                   |

O corpo é a análise humana: por que este conjunto existe, o que ele pretende
mudar, o que ficou de fora. Mesma divisão de sempre — frontmatter é o
contrato verificável, corpo é o auditor falando.

### 2.1 Ids falantes, não numerados

`regra-NNNN` e `achado-NNNN` são numerados porque ninguém os cita por nome
fora do repositório. Um conjunto é citado num ofício e num processo. O id é
`[a-z0-9][a-z0-9-]*`, como o de norma (P4), e nunca é reaproveitado.

## 3. Pertinência é derivada, nunca listada

Um conjunto **não** carrega a lista das suas regras. Ele declara sua `base` e
as regras declaram a que conjunto pertencem:

```
regras(C) = regras(base(C)) − substituídas(C) − revogadas(C) + introduzidas(C)
```

Duas razões para derivar em vez de listar. A primeira é a mesma de todo o
resto do repositório: uma lista mantida à mão diverge do que existe em disco,
e a divergência é silenciosa. A segunda é operacional: com pertinência
derivada, **propor uma substituição é criar um arquivo** — não criar um
arquivo *e* editar o manifesto, que são dois lugares para errar.

Dois campos novos no `regra-*.md`:

- **`conjunto:`** — o id do conjunto que introduz este documento. Toda regra
  tem um; as 112 atuais recebem o conjunto-raiz (§10, fase 0).
- **`substitui:`** — link OKF (`/regras/regra-0006.md`) para a regra que este
  documento substitui **dentro do seu conjunto**. Ausente = documento novo,
  não substitutivo.

E, no conjunto, um terceiro caso que a RFC 0004 não previa: **`revoga:`** —
uma regra que sai sem ser substituída. É resultado legítimo de validação
("esta hipótese não existe mais"), e sem um campo próprio a única forma de
expressá-la seria substituir por um documento vazio, que é pior: um documento
vazio ainda é uma regra, e o simulador a ofereceria.

## 4. Identidade: a substitutiva é documento novo

Uma regra substitutiva **é outro documento fazendo outra afirmação**, e recebe
id próprio (`regra-0113`, no espaço plano existente). Não é uma versão da
`regra-0006` gravada por cima nem uma cópia dela sob outro diretório.

Isso decorre do compromisso mais duro deste repositório — id é identidade é
URL, e URL compartilhada não quebra (RFC 0003) — e evita dois problemas
concretos:

- **Diretório por conjunto** (uma cópia das 112 regras em cada) faria o P2
  disparar em cima de cada cópia inalterada, que é materialmente idêntica ao
  original por construção. Seriam ~112 grupos de igualdade material espúrios
  por conjunto proposto.
- **Mesmo id em conjuntos diferentes** faria a URL depender do conjunto, e
  `/regras/regra-0006/` deixaria de ter referente único.

`row_index` **não** é propriedade de toda regra: é a identidade da linha na
importação. Substitutivas não têm. Ver §9.

## 5. Um único conjunto vigente

**Invariante**: no máximo um conjunto com `situacao: vigente`. É dele que o
`data/regras-sisprev.csv` derivado é gerado — hoje, o único conjunto que
existe. Conjuntos `proposto` exportam sob demanda, em arquivo próprio e
nomeado, nunca por cima do derivado principal.

Isto é a §1.5 da RFC 0004 ("seleção de origem única") dita em termos de
conjunto: o exportador nunca escolhe entre uma regra e sua substitutiva,
porque só um conjunto é vigente e a pertinência já resolveu qual das duas
está nele.

A transição `proposto → vigente` é a **ativação atômica** da RFC 0004 §1.4:
exige `decisao_completude` preenchida e move o conjunto anterior para
`superado`. Rollback é a transição inversa, sobre o conjunto inteiro. Nada
disso é automático — rebaixamento nunca é (P7).

## 6. Escopo dos detectores: por filtro, nunca por chave

P1 (nome repetido), P2 (igualdade material) e P7 (`status_auditoria`) passam a
rodar **dentro de um conjunto de cada vez**. Duas regras em conjuntos
diferentes não são "duas regras iguais": são a mesma regra em dois estados do
catálogo, e reportá-las seria ruído garantido — uma substituição que corrige
só o `nome` é materialmente idêntica ao original *por definição*.

**O escopo entra por filtro, nunca na chave material.** Acrescentar o
conjunto a `_material_key` mudaria o hash de todos os 7 grupos P2 conhecidos,
e os 7 achados que os referenciam ficariam órfãos (`stale_detection_refs`
quebra o CI). Agrupando por conjunto e mantendo a chave como está, o conjunto
vigente produz **exatamente as mesmas chaves e fingerprints de hoje**.

Pelo mesmo motivo, `conjunto`/`substitui`/`revoga` entram em
`_IGNORED_FRONTMATTER_KEYS` **sem bump de `VERSION`** — é o precedente já
aplicado a `dispositivos:` nesta mesma PR: a premissa do detector não mudou,
então os fingerprints originais voltam e os achados continuam válidos.

### 6.1 Um detector novo: substituição que não substitui nada

Um conjunto que propõe uma substitutiva **materialmente idêntica** à regra que
ela substitui está propondo um no-op — provavelmente por engano (o arquivo foi
criado e a alteração, esquecida). É mecanicamente detectável comparando a
chave material da substitutiva com a da substituída, e é **camada 3**: um
no-op é suspeito, não é defeito — pode ser um passo deliberado de um lote
maior.

## 7. Onde os atos de validação passam a morar

`validado_pge`, `validado_presidencia` e `ciclo_de_validacao` **ficam onde
estão**. São campos deployáveis: o Sisprev os tem, o produto os carrega, e
esta RFC não mexe no schema de produção (§0, não-objetivos).

O que muda é que deixam de se sustentar sozinhos. Um ato de validação é
declarado **no conjunto** (`atos`), e o campo por regra vira um **join
verificado**: uma regra não pode afirmar `validado_pge: S` se nenhum conjunto
que a contém carrega um ato da PGE. É o mesmo movimento do P7 — o campo
continua existindo e continua deployável, mas passa a ter que se sustentar
contra outro documento, em vez de ser verdadeiro por ter sido digitado.

Isto **não** fecha a Q12 da RFC 0001 (quais atos e quais fontes são válidos
institucionalmente — se SEI é a única `fonte`, etc.). Continua aberta; esta
RFC só define onde a resposta será registrada quando existir.

## 8. Invariantes verificáveis

Os gates que a implementação tem de trazer, no formato de `Violation` (P10):

| código                       | invariante                                                         |
| ---------------------------- | ------------------------------------------------------------------ |
| `P15_CONJUNTO_INVALIDO`      | frontmatter não satisfaz o contrato; `id` ≠ nome do arquivo        |
| `P15_BASE_INEXISTENTE`       | `base` não resolve para um conjunto autorado                       |
| `P15_BASE_CICLICA`           | a cadeia de `base` fecha um ciclo                                  |
| `P15_VIGENTE_MULTIPLO`       | mais de um conjunto com `situacao: vigente` (§5)                   |
| `P15_VIGENTE_SEM_DECISAO`    | `vigente` sem `decisao_completude` (RFC 0004 §1.4)                 |
| `P15_CONJUNTO_DESCONHECIDO`  | `conjunto:` de uma regra não resolve                               |
| `P15_SUBSTITUI_FORA_DA_BASE` | `substitui:` aponta para regra que não pertence à base do conjunto |
| `P15_SUBSTITUICAO_DUPLA`     | duas regras do mesmo conjunto substituem a mesma origem            |
| `P15_REVOGA_FORA_DA_BASE`    | `revoga:` idem                                                     |

Todos são **camada 1/2** (estruturais): são contradições no registro, não
leituras de prosa.

## 9. Confronto com os parsers reais

O que efetivamente quebra hoje, verificado no código:

**`scripts/okf_to_csv.py::_validate_identity`** exige que os `row_index` de
todos os `regra-*.md` formem exatamente `1..row_count`, sem furo nem
repetição. Uma substitutiva sem `row_index` viola isso na hora. A correção é
estreita e conceitualmente devida de qualquer forma: a contiguidade passa a
valer para as regras **que têm** `row_index` — a identidade da importação —
e não para toda regra que existe. O invariante não enfraquece; ele passa a
dizer o que sempre quis dizer.

**`scripts/detectors/igualdade_material.py::_material_key`** monta a chave com
*todo* o frontmatter menos as chaves ignoradas. Os três campos novos entram na
lista de ignoradas, pelo motivo e com o precedente da §6.

**`scripts/bundle.py::active_regras()`** filtra por `status_regra == "ativa"`
e é o ponto único por onde P1/P2 leem o catálogo — é lá que o escopo por
conjunto entra, num lugar só.

**`scripts/estado_auditoria.py`** (P7) faz o join com achados e detecções por
`doc_id`; passa a fazê-lo dentro do conjunto.

**`scripts/emit_site_data.py`** e `site/src/content.config.ts` ganham a
coleção de conjuntos e os dois campos novos; os campos de domínio continuam
passando por `.loose()`, como hoje.

**`data/raw/regras-sisprev.csv`** não é tocado por nada disto. Continua
imutável, e o job `original-csv-immutable` continua provando que tem um único
commit no histórico.

## 10. Plano incremental

**Fase 0 — no-op verificável.** Criar `type: Conjunto`, o resolvedor de
pertinência e o conjunto-raiz com as 112 regras atuais; escopar P1/P2/P7 por
conjunto. Como só existe um conjunto, **toda saída é byte a byte idêntica à
de hoje**: mesmo CSV derivado, mesmos 7 fingerprints P2, mesmos 41 grupos P1,
mesmo painel. É a fase que prova o desenho sem mudar nenhum resultado, e a
única em que isso é possível.

**Fase 1 — o primeiro conjunto proposto.** Um conjunto `proposto` com `base`
no vigente e uma única substitutiva. Exercita `substitui:`, o escopo dos
detectores e o detector de no-op (§6.1) num caso real e pequeno.

**Fase 2 — atos e o join do §7.** `atos` no conjunto e a verificação de
`validado_pge`/`validado_presidencia` contra eles.

**Fase 3 — ativação.** A transição `proposto → vigente` com
`decisao_completude`, e o rollback. Só depois de a fase 2 estar em uso, porque
ativar sem os atos registrados é exatamente o que o P7 existe para impedir.

**Fase 4 — site.** `/conjuntos/<id>/`, e a cadeia de substituição visível na
ficha de cada regra ("substitui a regra-0006", "substituída pela regra-0113 no
conjunto pge-2026").

Cada fase é revertível sozinha. A fase 0 não tem efeito observável, então
reverter é remover arquivos.

## 11. Questões em aberto

- **Q1 — Um conjunto pode ter mais de uma base?** Uma proposta da PGE e uma da
  Presidência sobre o mesmo vigente são dois conjuntos irmãos; consolidá-las
  seria um conjunto com duas bases, e aí "pertinência" precisa de regra de
  desempate. Recomendação: **não**, base única, e a consolidação é um conjunto
  novo cujas substitutivas são autoradas explicitamente. Merge automático de
  duas propostas jurídicas é a definição de conclusão sem autor.
- **Q2 — Uma substitutiva pode ser substituída dentro do mesmo conjunto?**
  Recomendação: não; corrigir uma substitutiva ainda `proposta` é editá-la, e
  o histórico disso é o git — o registro existe para atravessar a fronteira da
  autoridade, não para versionar rascunho.
- **Q3 — O `nome` de uma substitutiva pode repetir o da substituída?**
  Provavelmente sim (é o caso normal), e é por isso que o P1 tem de ser
  escopado (§6). Mas dentro do mesmo conjunto continua valendo o P1 de sempre.
- **Q4 — A relação com o `status_regra` `inativa` (P2.1).** Uma regra revogada
  por um conjunto e uma regra `inativa` são a mesma coisa? Recomendação:
  **não** — `inativa` é propriedade da regra em qualquer conjunto (foi
  desativada no Sisprev); `revoga:` é propriedade da relação entre um conjunto
  e a sua base. Confundi-las faria uma proposta não aprovada desativar uma
  regra em produção.
- **Q5 — Ordenação do CSV derivado de um conjunto com substitutivas.** A RFC
  0004 §1.6 define uma ordem total normativa ancorada no menor `row_index` das
  origens. Ela se aplica aqui sem mudança, mas precisa de teste próprio: o
  round-trip byte-idêntico é gate de CI (`derived-csv-in-sync`).

## 12. O que esta RFC não decide

- O schema enriquecido e o compilador da RFC 0004 (§3–§6 de lá). Um conjunto
  opera sobre os `regra-*.md` atuais; o catálogo enriquecido, quando existir,
  é mais um conjunto.
- O fluxo institucional de validação (Q12 da RFC 0001): quais atos valem,
  quais fontes são aceitáveis, quem assina o quê. §7 diz **onde** a resposta
  se registra, não qual ela é.
- Qualquer regra substitutiva concreta. Autorar é ato humano (princípio da
  autoria humana, RFC 0001): nenhum comando cria um `regra-*.md` substitutivo,
  como nenhum comando cria um achado.
- As questões Q1–Q5 acima.
