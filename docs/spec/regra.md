# Spec semântica — `type: Regra` (RFC 0001, P13.1)

- **Status**: estrutura inicial (2026-07-17) — a fronteira está declarada;
  as doze questões que a preenchem (Q1–Q12) permanecem abertas por
  desenho. Esta spec evolui conforme a investigação junto ao Sisprev, à
  documentação e à análise jurídica responde cada questão. Atualizada
  (2026-07-17): as seções do corpo da regra deixam de ser convenção
  opcional e passam a ser exigidas estruturalmente para `revisada`,
  verificadas por `scripts/estado_auditoria.py`. Atualizada (2026-07-29):
  as quatro seções fixas dão lugar a **uma**, `# Estado da análise`, com
  checklist — o gate anterior passava no literal `TODO` e não tinha onde
  registrar o que faltava (ver seção própria). Atualizada
  (2026-07-20): a fundamentação (`FUNDAMENTACAO*`) passou a viver no
  frontmatter, não no corpo (o corpo é análise autoral); a infraestrutura
  P3 (`okf/dispositivos/`) já existe — o pendente é a vinculação
  sistemática das regras aos dispositivos. Atualizada (2026-07-21): registra
  o papel do campo `nome` como interface de seleção (ver seção própria).
  Atualizada (2026-07-28): a **Q1 foi respondida** e parte da **Q2** também
  — `ATE` inclusivo, `DATA_ADM_APOS` exclusivo, valor gravado é o marco, e
  `DATA_DIREITO_ATE` é prazo de implementação dos requisitos (ver
  "Elegibilidade temporal"). É a primeira das doze questões a fechar.
  Atualizada (2026-07-28): registra **o que individua uma regra** e que a
  **granularidade da aferição é escolha do IPERON** — com isso a **Q3 fica
  parcialmente respondida** (`sexo` confirmado como critério aferido) e a
  leitura do `P2_IGUALDADE_MATERIAL_ATIVA` muda (ver "Definição de
  trabalho").
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

### O que individua uma regra (confirmado, 2026-07-28)

Confirmado pela coordenação da auditoria:

> Uma regra é o **conjunto de aferições necessário para conceder o
> benefício**. Havendo divergência nos **critérios aferidos**, as regras
> **não são idênticas** — ainda que fundamentadas no mesmo dispositivo legal.

**Benefício, não aposentadoria.** A distinção não é de estilo: o catálogo
cobre também a pensão por morte (`tipo_de_beneficio: PENSÃO POR MORTE`), e
uma definição escrita em torno da aposentadoria deixaria de fora as regras
de pensão — inclusive `regra-0012`/`0013` e `regra-0014`/`0015`, dois dos
três grupos discutidos abaixo.

Três consequências, e é importante não estendê-las além do que a frase diz:

1. **A identidade de uma regra está nos critérios aferidos, não na
   fundamentação.** Duas regras que citam o mesmo dispositivo são regras
   distintas se algum critério aferido diverge. O caminho inverso — mesma
   aferição, fundamentação diferente — a frase não trata.
2. **`sexo` é critério aferido**, dado como exemplo explícito. É a primeira
   coluna de domínio a sair de "candidato" (Q3) para confirmada como
   **predicado**. As demais continuam abertas: isto confirma *um* critério,
   não a lista deles.
3. **Nome repetido não é, por si, duplicação.** Se duas regras diferem em
   critério aferido, elas são legitimamente duas — o que falha ali é o
   `nome`, que não carrega a distinção que o registro carrega (ver "O papel
   do campo `nome`"). Hoje 25 dos 41 grupos `P1_NOME_REPETIDO` diferem
   **apenas** em `sexo`, e por esta definição são regras distintas com
   rótulo ambíguo — não regras duplicadas.

O que a frase **não** responde: se a divergência de critérios é condição
apenas *suficiente* ou também *necessária* para a não-identidade. Ou seja,
duas regras com aferição idêntica que divirjam só em `integral`/
`tipo_calculo`/`paridade` — os "resultados candidatos" da Q6 — podem ou não
ser a mesma regra, e a resposta continua aberta.

### A granularidade da aferição é escolha do IPERON (confirmado, 2026-07-28)

Também confirmado pela coordenação da auditoria:

> As aferições podem ser mais ou menos granulares **por conveniência do
> IPERON**: por exemplo, uma regra para "doença da lista" ou uma regra para
> cada doença específica.

Logo **o número de regras do catálogo não é determinado pela lei**. Dois
catálogos de granularidades diferentes podem ambos estar corretos, e mudar a
granularidade é decisão operacional — não correção de erro jurídico. É essa
elasticidade que a decomposição 1:N e a consolidação N:1 da
[RFC 0004](../rfc/0004-schema-enriquecido-e-compilador-para-o-sisprev.md)
existem para representar.

E é aqui que as duas frases se encontram, com uma consequência que muda a
leitura do `P2_IGUALDADE_MATERIAL_ATIVA`: se o IPERON escolhe uma
granularidade **mais fina do que as colunas registram**, as regras assim
separadas são legitimamente distintas *e* aparecem byte a byte idênticas no
catálogo. O P2 estaria então apontando uma **lacuna de schema** — falta a
coluna que carrega a distinção —, não uma duplicação.

Os 3 grupos sem **nenhum** campo distinto são os candidatos a essa leitura:

| grupo                      | hipótese de granularidade                                                                                                                                                                                    |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `regra-0068`/`0069`/`0070` | o art. 8º da ECE 146/2021 tem **exatamente três incisos** (66 pontos/15 anos de exposição; 76/20; 86/25) e há **exatamente três** regras idênticas — nenhuma coluna registra pontuação ou tempo de exposição |
| `regra-0012`/`0013`        | pensão por morte sob o mesmo dispositivo, distinção não registrada                                                                                                                                           |
| `regra-0014`/`0015`        | idem                                                                                                                                                                                                         |

**Isto é hipótese, não conclusão.** A correspondência 3-incisos/3-regras é
forte, mas nada no repositório *diz* que foi essa a granularidade escolhida —
confirmá-la é pergunta ao IPERON, e é o que separa "o catálogo não consegue
expressar a distinção" de "as regras estão duplicadas". Os três grupos
seguem cobertos por achado aberto e por `P2_IGUALDADE_MATERIAL_ATIVA`, como
antes: a definição reenquadra a pergunta, não a fecha.

### O escopo é parametrização, não mudança do sistema (confirmado, 2026-07-28)

> Alterar enum altera o sistema; o nosso trabalho com as regras é de
> **parametrização**.

Isso delimita o que uma correção de auditoria pode ser, e a fronteira passa
pelo **tipo declarado de cada coluna** no mapa P13.2
(`scripts/regra_schema.py::COLUMNS`, campo `tipo`):

| dentro do escopo (parametrização)                                 | fora do escopo (mudança do Sisprev)                        |
| ----------------------------------------------------------------- | ---------------------------------------------------------- |
| trocar o valor de uma coluna **dentro do domínio que ela já tem** | acrescentar membro a um enum (`string (enum)`, `S/N`, ...) |
| editar coluna de texto livre (`nome`, `FUNDAMENTACAO*`)           | criar coluna nova                                          |
| mudar a granularidade do catálogo (consolidar N:1, decompor 1:N)  | mudar o tipo de uma coluna                                 |

Duas consequências que não são óbvias:

1. **Quando a distinção entre duas regras não cabe em nenhuma coluna
   existente, isso é um achado, não um conserto.** A saída dentro do escopo é
   a granularidade (consolidar as regras que o sistema não sabe separar) ou o
   texto (a fundamentação de cada uma citar a alternativa que implementa) —
   nunca um enum novo. Pedir a coluna é legítimo, mas é pedido ao IPERON, e
   deve ser registrado como tal.
2. **`simulavel` decide se o texto basta.** Uma regra `simulavel: N` é
   escolhida por um humano lendo a fundamentação, então diferenciar o texto
   resolve. Uma regra `simulavel: S` é escolhida pelo motor, que não lê
   prosa: se duas regras `simulavel: S` são idênticas em todos os parâmetros,
   o sistema **não tem como** selecioná-las, e corrigir a fundamentação
   deixa o registro verdadeiro sem resolver a seleção.

É também a razão de a RFC 0004 ter um **compilador** em vez de um schema
substituto: o catálogo auditado pode ser mais rico do que o Sisprev, mas a
projeção deployable tem de caber nas colunas existentes — e
`compilador_auditado._checar_contrato_legado` é onde isso falha fechado.

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

## O papel do campo `nome`

**Decisão de produto (2026-07-21):** o `nome` é a principal ferramenta
apresentada ao usuário para **selecionar a regra aplicável** entre as
candidatas que restam após a anamnese do requerente. Não é mero rótulo nem
basta ser único — precisa expressar os elementos que **distinguem
operacionalmente** a regra.

**Princípio central:**

> O nome deve ser a menor descrição, em linguagem humana, capaz de
> distinguir a regra das demais que ainda podem ser aplicáveis depois da
> anamnese do requerente.

Três campos, três papéis distintos:

- **`id`** — identidade técnica **estável** (`regra-NNNN`); nunca muda, é o
  vínculo com a importação e com achados/detecções. Não serve à leitura
  humana de seleção.
- **`nome`** — resumo operacional **mutável**, orientado à seleção; deve
  **melhorar durante a auditoria** conforme os fatos discriminantes ficam
  claros. É o que o usuário lê para escolher.
- **`fundamentacao*`** (e, quando vinculados, `dispositivos`) — suporte
  jurídico da regra; **não substituem** o nome. Se o usuário precisa abrir a
  fundamentação para descobrir a diferença entre duas regras, os nomes
  falharam.

**Critérios provisórios** (a validar contra as modalidades reais e a
interface do Sisprev — ver "Limitações a verificar" abaixo; **ainda não** é
uma gramática universal):

- **Fatos discriminantes primeiro**, citação legal por último (ou só na
  fundamentação). O que realmente separa candidatas — modalidade, marco de
  ingresso, causa relevante, integral/proporcional, paridade — vem antes.
- **Linguagem compreensível** ao usuário do Sisprev; evitar abreviações
  opacas ("Perm.", "c/c", "§1º, I") como carga principal do nome.
- **Fatos conhecidos após a anamnese**: o nome usa o que já se sabe do
  requerente ao chegar na seleção (modalidade, datas de ingresso, causa da
  incapacidade, etc.).
- **Unicidade é necessária, mas insuficiente**: dois nomes que diferem
  **apenas** pelo número de um artigo ou da norma continuam ruins, mesmo
  formalmente únicos.
- **Lacuna do modelo**: se duas regras não puderem ser distinguidas por
  fatos conhecidos após a anamnese — porque o catálogo **não possui o
  predicado necessário** —, isso não é problema de redação, é uma **lacuna
  do modelo** a registrar (exatamente o caso 0022 × P6/P7, ver
  `docs/analysis/reconciliacao-invalidez-incapacidade.md` e o piloto
  `docs/analysis/piloto-selecao-invalidez-incapacidade.md`).

**Limitações a verificar antes de fixar uma gramática universal:**
comprimento máximo e truncamento do campo na tela do Sisprev, comportamento
de busca e de ordenação por nome. Este documento registra o **princípio** e
**critérios provisórios**, não uma forma fechada — a gramática só deve ser
fixada depois de conferir essas restrições reais e as demais modalidades.

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

`id` (identidade técnica **estável** do documento — `regra-NNNN`, nunca
muda) e `row_index` (vínculo com a linha da importação congelada). `NOME` ↔
`nome` **não** é mero rótulo humano: é o resumo operacional orientado à
seleção, **mutável** durante a auditoria — ver "O papel do campo `nome`"
abaixo (P1).

### Estado no catálogo e estado da auditoria (confirmado — P2.1/P7/P12)

`status_regra`, `motivo_inativacao` (P2.1); `status_auditoria`,
`auditado_por`, `auditado_em`, `atos_validacao` (P7/P11). Nunca confundir
com aplicabilidade temporal — essa é outra dimensão (P5, ver abaixo).

### Elegibilidade temporal — inclusividade confirmada, fato jurídico parcialmente aberto (P5, Q1, Q2)

`DATA_ADM_ATE`, `DATA_ADM_APOS`, `DATA_DIREITO_ATE`, `DATA_DIREITO_APOS`.
A ordenação estrutural (round-trip, sentinelas preservadas e não
interpretadas) está confirmada.

**Confirmado pela coordenação da auditoria (2026-07-28) — resposta à Q1 e a
parte da Q2:**

- `DATA_*_ATE` é **inclusivo**: `ate = X` cobre o próprio dia X.
- `DATA_ADM_APOS` é **exclusivo**: `apos = X` cobre a partir do dia
  **seguinte** a X (`data_adm_apos = 31/12/2003` significa "admitido a
  partir de 01/01/2004").
- A escolha do campo segue a forma do requisito legal: exigência de data
  *até* usa o campo `ATE`; exigência de data *após* certo dia usa o `APOS`.
- **O valor gravado é o marco**, ajustado à semântica da coluna e ao que
  consta na legislação — não o primeiro dia da cobertura. Daí que janelas
  adjacentes gravem o **mesmo valor** nos dois campos (`ate = M` seguido de
  `apos = M` particiona sem buraco nem sobreposição).
- `DATA_DIREITO_ATE` é **prazo de implementação dos requisitos**: todos
  precisam estar completos até essa data.

**Segue aberto:** a que ato `DATA_ADM_*` se refere (nomeação, posse,
exercício, ingresso em sentido amplo); se `DATA_DIREITO_APOS` tem a leitura
simétrica do `ATE` (presumível, mas não confirmada — é o ponto da issue
#39, que pede resposta **por eixo** em vez de uma resposta única para
`DATA_*`); e, para pensão por morte, se "requisitos completados" equivale à
data do óbito. As sentinelas seguem não interpretadas.

Consequência de conferência: se o valor gravado é o marco, todo limite
não-sentinela deveria coincidir com uma data declarada pelos dispositivos
que a regra cita — vigência da norma ou prazo fixado no dispositivo. O
levantamento está em
[semântica das janelas temporais](../analysis/semantica-das-janelas-temporais.md).

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
campos do frontmatter (o frontmatter *é* a regra deployável; o corpo do
`.md` é análise autoral, não deployado nem material para o detector P2). A
granularidade de citação (menor unidade citada, decomposição sob demanda) é
P3; o bundle `okf/dispositivos/` **já existe** e a infraestrutura P3 está
implementada — o que permanece pendente é a **cobertura**: as regras ainda
não estão sistematicamente vinculadas aos dispositivos (especialmente os
estaduais).

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

## `# Estado da análise` — a seção obrigatória do corpo para `revisada`

**Decisão (2026-07-29):** o corpo exige **uma** seção de nível 1,
`# Estado da análise`, contendo um checklist. Ela substitui as quatro seções
fixas que a versão anterior desta spec exigia (`# Critérios avaliados pelo Sisprev`, `# Requisitos de verificação manual`, `# Documentos ou evidências necessários`, `# Resultado após a seleção`).

**Por que as quatro caíram.** A checagem que as sustentava só conferia que
cada seção *existia e tinha texto não vazio* — o literal `TODO` passava nas
quatro. Ela certificava uma forma, nunca que alguma análise tivesse
acontecido. E, sendo forma fixa, não tinha onde registrar **o que ainda
falta**, que é justamente o estado que uma auditoria em curso precisa
carregar. Na primeira vez que as quatro foram escritas de verdade (regras
0006–0009), foi preciso inventar uma quinta seção só para o que não cabia
nelas.

O checklist inverte as duas coisas: quem escreve decide os itens que
*aquela* regra precisa, e **uma caixa aberta bloqueia `revisada`**.

```markdown
# Estado da análise

Comentário livre é bem-vindo — por que a regra é assim, o que a distingue
das vizinhas, o que se descobriu conferindo.

- [x] Critérios do cadastro conferidos contra a lei
- [x] Dispositivos vinculados conferidos contra os campos de fundamentação
- [ ] Causa da incapacidade — depende da Q6, não decidível hoje
```

`scripts/estado_auditoria.py::check_p7_estados` verifica
**estruturalmente**, para toda regra `revisada` (herdado por `validada`),
código `P7_ESTADO_INVALIDO`:

- a seção existe e não está vazia;
- há **ao menos um** item de checklist — texto livre sozinho não afirma nada
  conferível e reconstruiria o buraco das quatro seções;
- **nenhum item está aberto** (`- [ ]`). `- [x]` e `- [X]` contam como
  feitos; marcador comum (`- item`) é texto, não item.

Contar `- [ ]` continua sendo verificação de forma, nunca de mérito: o CI não
avalia se os itens são os certos, nem se um item marcado foi honestamente
marcado. Isso segue sendo julgamento humano.

**As quatro perguntas não desapareceram.** Elas continuam sendo o que a
seção "Elegibilidade e fronteira de automação" desta spec pede que se
responda, e são os **itens iniciais recomendados** do checklist de uma regra
nova. O que acabou foi a exigência de que fossem headings literais,
conferidos por casamento de string.

A quinta pergunta ("quais dispositivos justificam cada critério e efeito")
tampouco é heading obrigatório — a RFC 0008 §5 registra que ela é
conferência humana, sem campo nem gate. Na prática ela vira um item do
checklist e, quando houver o que mostrar, uma seção livre no mesmo corpo.

**Nenhuma das 112 regras importadas tem essa seção hoje** — todas estão
`importada`, e o gate nunca chegou a rodar sobre nenhuma. Esta spec não a
adiciona retroativamente: fabricar a análise violaria o princípio da autoria
humana (RFC 0001, topo). Ela é escrita regra a regra, por um auditor, no
momento em que a investigação de fato acontece — e só então a regra pode
transicionar para `revisada`.

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
