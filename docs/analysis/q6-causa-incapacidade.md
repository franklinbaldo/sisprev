# Q6 — Onde vive a "causa da incapacidade"? (dossiê de decisão)

> **Nota:** Dossiê de apoio à decisão, gerado por IA. **Não altera schema,
> regras, dados nem motor** e **não resolve Q6** — Q6 só se fecha com
> **evidência operacional** de como o Sisprev de fato trata a causa. Onde o
> repositório não tem essa evidência, o resultado correto é um **protocolo de
> investigação** (§7), não uma escolha arquitetural inventada. Distingo
> **evidência** (o que encontrei no repo) de **hipótese** (o que ainda precisa
> ser confirmado com o Sisprev/PGE).

## 1. A pergunta

A [RFC 0002](../rfc/0002-selecao-explicavel-pos-anamnese.md) e o
[piloto de seleção](piloto-selecao-invalidez-incapacidade.md) mostraram que o
discriminante entre a metade **integral** e a **proporcional** das regras de
invalidez é a **causa da incapacidade** (acidente em serviço / moléstia
profissional / doença grave, contagiosa ou incurável → integral; causa comum
→ proporcional). **Q6** pergunta: essa causa já existe **em campo**, em
**código/tabela externa**, é **verificação manual**, ou é **lacuna real do
modelo** que exige evolução do schema?

## 2. Inventário — as 27 colunas do catálogo deployável

Fonte: `scripts/regra_schema.py::COLUMNS` (P13.2). Busca por qualquer coluna
que aluda a causa/doença/acidente/moléstia/catalogada/laudo/CID:

> **Evidência:** **nenhuma** das 27 colunas representa a causa da incapacidade.
> As colunas de domínio são identidade, datas de elegibilidade, `sexo`,
> `paridade`, `integral`, `tipo_calculo`, fundamentação e flags de
> apresentação — o `integral`/`tipo_calculo` é o **resultado** da causa, não a
> causa.

## 3. Onde a causa aparece no repositório (evidência × hipótese)

| Onde                                               | O que encontrei                                                                                                                                                                                                                                                                                         | Classificação                                                                                                                            |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Código** (`scripts/`)                            | **Nada** avalia, importa ou deriva a causa. Nenhum importador, motor ou fluxo a representa.                                                                                                                                                                                                             | **Evidência**: causa **não** está em código neste repo                                                                                   |
| **Dados congelados** (`data/raw/xlsx/`)            | A **análise da PGE** modela a causa como **coluna estruturada**: "Causa da incapacidade" e "Doença catalogada em lei?" nas abas invalidez, policial e PCD. Valores são **prosa descritiva** por hipótese (ex.: "Acidente em serviço, moléstia profissional…"; "Sim, quando a causa for doença grave…"). | **Evidência**: a causa existe como **coluna de análise (to-be) congelada**, **não** integrada por código, **não** no catálogo deployável |
| **Texto legal** (`okf/`)                           | A causa aparece como **prosa** na fundamentação de **8 regras** e em **2 dispositivos** (o texto do Art. 40, I original e correlatos).                                                                                                                                                                  | **Evidência**: causa como **texto livre** no suporte jurídico, não como campo consultável                                                |
| **Catálogo as-is** (`data/raw/regras-sisprev.csv`) | **Nenhuma** coluna de causa.                                                                                                                                                                                                                                                                            | **Evidência**: confirmada a ausência no deployável                                                                                       |
| **Sisprev real** (o sistema em produção)           | **Não há artefato no repo** que revele como o Sisprev trata a causa na seleção (campo oculto? tabela? tela manual?).                                                                                                                                                                                    | **Lacuna de evidência** → §7                                                                                                             |

**Leitura:** o repositório prova que a causa **não** está no catálogo
deployável nem em código aqui; prova que a **PGE a reconheceu** como um eixo
(coluna na análise) e que ela vive na **prosa jurídica**. O repositório **não**
prova como o **Sisprev em produção** a trata — essa é a evidência que falta
para fechar Q6.

## 4. As quatro alternativas, comparadas

| Alternativa                                                             | Proveniência do dado                                                                                         | Auditabilidade                                                           | Impacto no `nome`                                         | Avaliação trivalente                                                                                          | Round-trip CSV↔md                                               | Integração com o Sisprev                                        |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| **A1. Campo existente** (reaproveitar uma das 27)                       | nenhuma coluna representa a causa (§2)                                                                       | —                                                                        | —                                                         | —                                                                                                             | —                                                               | **descartada por evidência**                                    |
| **A2. Tabela/código externo**                                           | Sisprev (código) ou tabela externa; a PGE já tem a coluna na análise                                         | **Baixa** se código opaco; **média** se tabela versionada e citável      | Permite o nome expor a causa                              | O filtro automático poderia narrar por causa **se** integrado                                                 | **Fora** do catálogo — sem impacto no round-trip                | Exige o Sisprev **ler** essa fonte na seleção                   |
| **A3. Verificação manual**                                              | Laudo médico → atendente/perito; registrada nas seções P13.1 ("verificação manual", "documentos/evidências") | **Média/alta** se o auditor registra a verificação e a evidência exigida | Permite o nome expor a causa (fato conhecido na anamnese) | O **filtro automático** segue `indeterminado`; o **humano** resolve a metade                                  | **Fora** do catálogo (seções P13.1 são análise, não coluna CSV) | Exige um passo de verificação manual no fluxo (pode já existir) |
| **A4. Campo novo** (`causa_incapacidade`, e talvez `doenca_catalogada`) | Laudo → novo campo no schema                                                                                 | **Alta**: campo versionado no bundle, round-trip, detectores             | Nome deriva da causa estruturada                          | O filtro automático **narra por causa** (quando o fato existe) → resolve as indeterminações causa-dependentes | **Entra** no round-trip (nova coluna P13.2)                     | Exige evolução do schema **e** do motor de seleção do Sisprev   |

- **A1 está descartada por evidência**: não há coluna que represente a causa
  (§2). Não é uma escolha em aberto — o repo já a refuta.
- **A2, A3 e A4 permanecem em aberto** e **não são mutuamente exclusivas**:
  o Sisprev pode já resolver por A2/A3 e o catálogo evoluir por A4 para torná-la
  auditável. Qual é a realidade **depende da evidência de §7**.

## 5. Reaplicação de C2, C3, C4, C6, C8, C11 — o que cada alternativa resolve

Casos do piloto de seleção. "Resolve" = leva o desfecho de `indeterminado` a
um resultado (única/humano-decidível); "não resolve" = a pendência é de outra
natureza (fato ausente, data, dado defeituoso).

| Caso                                         | Natureza da indeterminação                      | A2 externo                                         | A3 manual                          | A4 campo novo                                       |
| -------------------------------------------- | ----------------------------------------------- | -------------------------------------------------- | ---------------------------------- | --------------------------------------------------- |
| **C2** (causa comum não catalogada)          | causa-axis (fato presente)                      | resolve **se** integrado                           | resolve no passo humano            | **resolve** (narra por causa)                       |
| **C3** (acidente, ≤2003)                     | causa-axis (fato presente)                      | resolve se integrado                               | resolve no humano                  | **resolve**                                         |
| **C4** (acidente, >2003)                     | causa-axis **+ sobreposição de regime** (Q1/Q2) | resolve só a **metade causa**; regime segue aberto | idem                               | resolve a causa; **regime permanece indeterminado** |
| **C6** (causa **não informada**)             | **fato ausente**                                | **não resolve** (campo vazio)                      | **não resolve** (nada a verificar) | **não resolve** (campo vazio)                       |
| **C8** (doença grave; 0021 contraditória)    | causa-axis **+ dado defeituoso** (0021)         | resolve a causa; **contradição da 0021 permanece** | idem                               | resolve a causa; contradição permanece              |
| **C11** (doença catalogada **desconhecida**) | **fato ausente**                                | **não resolve**                                    | **não resolve**                    | **não resolve**                                     |

**Conclusão da reaplicação:** qualquer das alternativas de causa (A2/A3/A4)
resolve **apenas** a indeterminação **causa-axis** (C2, C3, e a metade de C4 e
C8). **Não** resolve: **fato ausente** (C6, C11 — um campo vazio continua
vazio), **semântica de data / transição de regime** (a outra metade de C4,
Q1/Q2), nem **dado defeituoso** (0021 em C8). Ou seja: **resolver Q6 é
necessário, mas não suficiente** — Q1/Q2 e os defeitos de dados continuam.

## 6. Matriz de decisão

| Critério                         | A2 externo                     | A3 manual                         | A4 campo novo                                    |
| -------------------------------- | ------------------------------ | --------------------------------- | ------------------------------------------------ |
| Auditável no repo                | não (fora do catálogo)         | parcial (seções P13.1)            | **sim**                                          |
| Nome pode expor a causa          | sim                            | sim                               | sim                                              |
| Seleção **automática** por causa | sim (se integrado)             | não (humano decide)               | **sim**                                          |
| Custo de mudança no Sisprev      | ler fonte externa              | passo de fluxo (talvez já existe) | **schema + motor**                               |
| Round-trip / detectores          | não afeta                      | não afeta                         | **entra no contrato P13.2**                      |
| Risco de decidir sem evidência   | **alto** (inventar integração) | **médio**                         | **alto** (evoluir schema sem confirmar a lacuna) |

**Nenhuma linha pode ser marcada como escolhida** sem a evidência de §7: A2
pressupõe uma integração que não vimos; A4 pressupõe uma lacuna que só se
confirma descartando A2/A3 no Sisprev real.

## 7. Fila de perguntas para responsáveis humanos (protocolo de investigação)

O repositório é **insuficiente** para fechar Q6. O próximo passo correto é
responder, com o Sisprev/PGE, **nesta ordem** (cada resposta pode dispensar as
seguintes):

1. **No Sisprev em produção, a seleção da regra usa a causa da incapacidade?**
   Se sim, **de onde** ela vem — campo de tela, tabela, código, ou decisão do
   atendente? (Distingue A2 × A3 × A4.)
2. Se há **tabela/código** (A2): é versionado e citável? Onde? Pode ser
   auditado como os `dispositivos`?
3. Se é **decisão do atendente** (A3): há registro estruturado dessa decisão
   (o "porquê" da metade integral/proporcional) ou ela se perde?
4. A **"doença catalogada em lei"** (a lista taxativa de doenças graves/
   contagiosas/incuráveis) existe como **norma/lista oficial**? Onde? (É o
   predicado de C11.)
5. A causa é conhecida **no momento da seleção** (após a anamnese) ou só
   depois (perícia posterior)? (Define se cabe no filtro ou é verificação
   tardia.)
6. Para a PGE: a coluna "Causa da incapacidade" da análise é **descritiva** de
   cada hipótese ou **prescreve** um dado de entrada? (Confirma se a PGE
   propõe A4.)
7. Há **apetite** para evoluir o schema deployável (A4), ou o Sisprev exige
   manter as 27 colunas fixas? (Restrição de produto sobre A4.)

## 8. Conclusão

- **Q6 permanece aberta.** A evidência do repo **refuta A1** (não há campo),
  **localiza** a causa na análise da PGE (coluna to-be) e na prosa jurídica, e
  **não encontra** nenhum código que a avalie — mas **não revela** como o
  Sisprev real a trata.
- **A2, A3 e A4 seguem candidatas**, possivelmente combinadas. Escolher entre
  elas **exige** as respostas de §7 — decidir agora seria inventar uma
  integração (A2) ou uma lacuna (A4) sem evidência operacional.
- Mesmo resolvida Q6, o piloto (§5) mostra que **Q1/Q2** (limite de data,
  transição de regime) e os **dados defeituosos** (0021, 0004) continuam
  gerando `indeterminado` — Q6 é necessária, não suficiente, para um motor.

Sequência recomendada (inalterada): **§7 respondido → decisão humana sobre
A2/A3/A4 → correções in-place de invalidez → motor piloto**; a reconciliação de
pensão vem depois, já com o eixo causa decidido.
