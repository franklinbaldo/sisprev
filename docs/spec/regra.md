# Spec semântica — `type: Regra` (RFC 0001, P13.1)

- **Status**: estrutura inicial (2026-07-17) — a fronteira está declarada;
  as doze questões que a preenchem (Q1–Q12) permanecem abertas por
  desenho. Esta spec evolui conforme a investigação junto ao Sisprev, à
  documentação e à análise jurídica responde cada questão. Atualizada
  (2026-07-17): as quatro seções obrigatórias do corpo da regra deixam de
  ser convenção opcional e passam a ser exigidas estruturalmente para
  `revisada`, verificadas por `scripts/estado_auditoria.py`.
- **Parte de**: [RFC 0001](../rfc/0001-criterios-de-validacao-das-regras.md),
  P13 ("Especificação semântica de `type: Regra` + mapa normativo CSV →
  OKF"). P13 tem dois entregáveis: esta spec (P13.1) e o mapa normativo
  das 27 colunas (P13.2, já implementado em `scripts/regra_schema.py` —
  fonte única do mapeamento CSV ↔ `.md`, não duplicada aqui).
- **Pré-requisito de**: P6 (análise de cobertura — precisa saber quais
  campos são predicados e quais são resultados, Q3), da auditoria de
  mérito (o revisor precisa saber o que é automático, manual ou
  desconhecido, Q11/Q12) e, transitoriamente, dos checks provisórios de
  P9 (Q6, Q10).

## Definição de trabalho

> Uma regra reúne critérios estruturados usados pelo Sisprev, requisitos
> adicionais que podem depender de prova ou análise manual, consequências
> aplicadas depois de sua seleção e a fundamentação jurídica
> correspondente. A correspondência automática dos campos estruturados não
> equivale, por si só, à conclusão jurídica de que a regra se aplica ao
> caso concreto.

Isso **não é uma afirmação sobre como o Sisprev de fato funciona** — é a
hipótese de trabalho que estrutura a investigação (a confirmar por Q3, Q4,
Q5). O catálogo **não deve ser tratado como motor decisório integralmente
automático**.

## O que esta spec exige

**Não exige que tudo seja parametrizado.** Exige que a fronteira entre
**automático**, **manual** e **desconhecido** seja explícita para cada
regra `revisada` (P7) — nunca implícita, nunca presumida pelo silêncio de
um campo.

Para cada regra `revisada`, deve ser possível responder, em linguagem
humana:

1. Quais fatos o sistema verifica automaticamente?
2. Quais fatos devem ser confirmados manualmente?
3. Quais documentos/evidências sustentam essa confirmação?
4. O que o sistema faz depois que a regra é selecionada?
5. Quais dispositivos jurídicos justificam cada critério e efeito?

Essas cinco perguntas são um **gate de julgamento humano** — não são
verificáveis por código (`scripts/estado_auditoria.py` documenta
explicitamente essa exceção: a transição para `revisada` depende deste
gate, mas o CI não o avalia). O papel desta spec é dar ao revisor a
estrutura para respondê-las de forma consistente entre regras, não
automatizar a resposta.

## Categorias

**Só identidade/proveniência e estado (catálogo + auditoria) estão
confirmados.** A atribuição de cada campo de domínio a uma categoria
abaixo é **hipótese de classificação, a confirmar campo a campo** pela
investigação (Q3, Q5, Q6, Q9) — nunca uma classificação normativa já
decidida. A fonte de cada `categoria` por coluna é
`scripts/regra_schema.py::COLUMNS` (P13.2); esta seção apenas organiza
essa fonte única nos grupos que a spec P13.1 define — não a duplica nem
diverge dela.

### Identidade e proveniência (confirmado)

`id` (identidade estável do documento), `row_index` (vínculo com a linha
da importação congelada), `NOME` ↔ `nome` (rótulo humano — P1).

### Estado no catálogo e estado da auditoria (confirmado — P2.1/P7/P12)

`status_regra`, `motivo_inativacao` (P2.1); `status_auditoria`,
`auditado_por`, `auditado_em`, `atos_validacao` (P7/P11). Nunca confundir
com aplicabilidade temporal — essa é outra dimensão (P5, ver abaixo).

### Elegibilidade temporal — estrutural confirmada, semântica a investigar (P5, Q1, Q2)

`DATA_ADM_ATE`, `DATA_ADM_APOS`, `DATA_DIREITO_ATE`, `DATA_DIREITO_APOS`.
A ordenação estrutural (round-trip, sentinelas preservadas e não
interpretadas) está confirmada; o fato jurídico exato que cada data
representa, e se os limites são inclusivos ou exclusivos, é Q1/Q2.

### Critérios parametrizados — candidatos (Q3)

Campos que *talvez* participem da seleção automática — quais realmente
participam, e quais apenas configuram cálculo/apresentação, é
precisamente Q3:

- `TIPO DE BENEFICIO`, `TIPO`, `SEXO`;
- `APOS_ESPECIAL` (também candidato a apresentação — Q9).

### Requisitos de verificação manual/jurídica (Q5)

**Nenhuma das 27 colunas do CSV está mapeada aqui ainda.** A hipótese de
trabalho de Q5 é que requisitos como idade mínima, tempo de contribuição,
pedágio, atividade policial, natureza da incapacidade ou exposição
especial podem viver **fora do CSV** — em código, tabelas externas, outra
tela do Sisprev, ou análise manual sem suporte estruturado algum. Até Q5
ser respondida, esta categoria fica deliberadamente vazia: um campo só
entra aqui quando a investigação confirmar que ele *é* um requisito
verificado manualmente, não por suposição.

### Resultado/efeitos da seleção — candidatos (Q6)

A definição operacional de cada um, e se é resultado ou também predicado,
é justamente Q6:

- `PARIDADE`, `INTEGRAL`, `TIPO_CALCULO`;
- `ADICIONAL_INATIVIDADE` (também candidato a apresentação — Q9).

### Comportamento de implementação/apresentação — candidatos (Q9)

Se são condições, efeitos, ou controles de interface é precisamente Q9:

- `SIMULAVEL`, `TIPO_REMUN`, `TabelaPontuacao`;
- `Requisitos da IN Nº 5/2020`, `Relatório p/ Reserva Remunerada por Idade ex-officio`;
- `VISIVEL DTC PROPORCIONAL`, `VISIVEL DTC INTEGRAL`;
- `APOS_ESPECIAL`, `ADICIONAL_INATIVIDADE` (listados também acima).

### Fundamentação e dispositivos (P3)

`FUNDAMENTACAO_PROPORCIONAL`, `FUNDAMENTACAO_INTEGRAL`, `FUNDAMENTACAO` —
corpo do documento. A granularidade de citação (menor unidade citada,
decomposição sob demanda) é P3; o bundle `okf/dispositivos/` ainda não
existe (Fase 2).

### Legado a reconciliar (candidatos — P7)

`VALIDADO PGE`, `VALIDADO PRESIDENCIA` — candidatos a derivar de
`atos_validacao` (P7) em vez de permanecerem booleanos soltos. Os 112
valores `FALSE/FALSE` da importação **não demonstram** que sejam um único
ato ou dois atos obrigatórios — ausência de casos divergentes numa base
não validada é falta de evidência, não evidência de unicidade (ver RFC,
P7, ressalvas de Q12).

### Metadados de processo (sem categoria semântica própria)

`ATUALMENTE NO SISTEMA` (estado no Sisprev real — não confundir com
`status_regra`), `CICLO DE VALIDAÇÃO` (ordenação do processo de
auditoria).

## Seções obrigatórias do corpo da regra para `revisada`

**Decisão (revisão da PR #7, round 2):** a spec dizia que a fronteira
automático/manual/desconhecido deveria ser "explícita para cada regra
revisada", mas tratava como opcionais as únicas seções propostas para
registrá-la — as duas afirmações não se sustentavam juntas: uma regra
chegava a `revisada` só com `auditado_por`/`auditado_em`, sem nenhum
conteúdo semântico auditável. Corrigido: as quatro primeiras perguntas
(automático, manual, documentos, resultado) têm resposta **obrigatória e
não vazia** no corpo do `regra-*.md`, em seções de nível 1 sem
aninhamento — o parser do bundle só reconhece `# Heading`, nunca `##`:

```markdown
# Critérios avaliados pelo Sisprev

# Requisitos de verificação manual

# Documentos ou evidências necessários

# Resultado após a seleção
```

`scripts/estado_auditoria.py::check_p7_estados` verifica **estruturalmente**
que as quatro seções existem e têm texto não vazio para toda regra
`revisada` (herdado por `validada`) — código `P7_ESTADO_INVALIDO` quando
ausente ou vazia. Isso prova apenas que a resposta *existe*, nunca seu
mérito ou correção jurídica: o CI não avalia se o texto responde
corretamente a pergunta, só que o auditor efetivamente escreveu algo.

A quinta pergunta ("quais dispositivos justificam...") **não** é seção
obrigatória ainda — depende de P3 (`okf/dispositivos/`), ainda não
construído (Fase 2). Quando existir, deve se tornar a quinta seção
obrigatória do mesmo jeito.

**Nenhuma das 112 regras importadas tem essas seções hoje**, e esta spec
não as adiciona retroativamente — isso exigiria um julgamento de mérito
sobre cada regra que ainda não foi feito, e fabricá-lo aqui violaria o
princípio da autoria humana (RFC 0001, topo). As seções são escritas regra
a regra, por um auditor, no momento em que a investigação de fato responde
as perguntas para aquela regra específica — e só então a regra pode
transicionar para `revisada` (o CI bloqueia a transição até lá).

O corpo da regra **nunca** contém uma seção `# Achados`: problemas de
auditoria são conceitos próprios em `achados/`, referenciando a regra via
`regras_afetadas` (P14) — nunca embutidos no `regra-*.md`.

## Questões abertas (Q1–Q12)

Esta spec organiza a fronteira; não a preenche. As doze questões
semânticas que a preenchem estão listadas no RFC 0001, seção P13, e
**permanecem abertas por desenho**: são respondidas pela investigação
junto ao Sisprev, à documentação e à análise jurídica — não por este
documento. Cada resposta deve atualizar tanto esta spec (a categoria do
campo, se envolvido) quanto o mapa `regra_schema.py` (a `categoria` da
`ColumnSpec` correspondente), mantendo as duas em sincronia com a mesma
fonte de verdade conceitual.
