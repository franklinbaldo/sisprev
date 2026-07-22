# Q6 — Onde vive a "causa da incapacidade"? (dossiê de decisão)

> **Nota:** Dossiê de apoio à decisão, gerado por IA. **Não altera schema,
> regras, dados nem motor** e **não resolve Q6** — Q6 só se fecha com
> **evidência operacional** de como o Sisprev de fato obtém, classifica e
> registra a causa. Onde o repositório não tem essa evidência, o resultado
> correto é um **protocolo de investigação** (§9), não uma escolha arquitetural
> inventada. Distingo **evidência** (o que encontrei no repo) de **hipótese**
> (o que ainda precisa ser confirmado com o Sisprev/PGE).

## 1. A pergunta — e por que ela tem três lados

A [RFC 0002](../rfc/0002-selecao-explicavel-pos-anamnese.md) e o
[piloto de seleção](piloto-selecao-invalidez-incapacidade.md) observaram, **nos
pares as-is e na proposta da PGE**, uma relação entre a **causa da incapacidade**
e a metade **integral** vs **proporcional** das regras de invalidez (acidente em
serviço / moléstia profissional / doença grave, contagiosa ou incurável →
integral; causa comum → proporcional). Essa relação é **observada e proposta**,
**ainda sujeita à validação jurídica** — não é uma regra universal já fechada
(ver §7).

O erro a evitar é tratar Q6 como uma pergunta só. **A causa aparece em dois
contratos distintos**, que um avaliador precisa cruzar:

- **O predicado da regra** — "quais causas satisfazem *esta hipótese*?" Vive no
  **catálogo** (bundle/regra). É genérico, uma vez por regra.
- **O fato do requerente** — "qual foi a causa *apurada neste caso*?" Vive na
  **solicitação** (laudo, perícia, processo). É concreto, uma vez por
  requerimento.

Um "campo causa" no lugar errado não resolve nada: mesmo que o catálogo ganhe um
predicado, o sistema ainda precisa **obter e registrar** o fato correspondente do
requerente. Por isso Q6 se decompõe:

| Sub‑questão | Lado               | Pergunta                                                                                                      |
| ----------- | ------------------ | ------------------------------------------------------------------------------------------------------------- |
| **Q6‑R**    | regra (predicado)  | Onde vive o predicado que define **quais causas atendem** cada regra?                                         |
| **Q6‑S**    | solicitação (fato) | Onde e **quando** vive o fato concreto da **causa do requerente**?                                            |
| **Q6‑T**    | taxonomia (ponte)  | Onde vive a classificação que transforma **diagnóstico/laudo** em causa comum / acidente / doença catalogada? |

Q6‑T é a ponte: sem taxonomia, um laudo ("Q6‑S") não vira um valor comparável ao
predicado ("Q6‑R").

## 2. Inventário — as 27 colunas do catálogo (contrato atual)

Fonte: `scripts/regra_schema.py::COLUMNS` (P13.2), o mapa normativo único
CSV↔md. Busca por qualquer coluna que aluda a
causa/doença/acidente/moléstia/catalogada/laudo/CID:

> **Evidência (Q6‑R):** **nenhuma** das 27 colunas expressa um **predicado
> explícito de causa**. As colunas de domínio são identidade, datas de
> elegibilidade, `sexo`, `paridade`, `integral`, `tipo_calculo`, fundamentação e
> flags de apresentação. `integral`/`tipo_calculo` é o **resultado** já
> pré-computado da causa por regra, **não** o predicado que diz *quais* causas o
> produzem — e nunca o fato do requerente.

O contrato atual é o mesmo nos dois artefatos do catálogo (ver a nota da
[CLAUDE.md](../../CLAUDE.md) sobre os papéis):

- **`data/raw/regras-sisprev.csv`** — **baseline congelada da importação**
  (read-only, o que foi recebido). **Não** é o catálogo vivo.
- **`okf/regras-sisprev/`** — o **bundle vivo**, onde as edições de auditoria
  acontecem, e que deriva o `data/regras-sisprev.csv`.

Ambos usam o **mesmo contrato atual de 27 colunas, sem predicado explícito de
causa**. A ausência não é um artefato da baseline; é uma propriedade do contrato
em vigor.

## 3. Onde a causa aparece no repositório (evidência × hipótese)

Contagens abaixo são reproduzíveis pelo padrão registrado no rodapé (§ *Como as
contagens foram obtidas*).

| Onde                                                        | O que encontrei                                                                                                                                                                                                                                                                                  | Lado             | Classificação                                                                                                                                                 |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Código** (`scripts/`)                                     | **Nada** avalia, importa, deriva ou classifica a causa. Nenhum importador, motor, taxonomia ou fluxo a representa.                                                                                                                                                                               | R/S/T            | **Evidência**: causa **não** está em código neste repo                                                                                                        |
| **Análise PGE** (`data/raw/xlsx/`)                          | Colunas estruturadas "Causa da incapacidade" e "Doença catalogada em lei?" nas abas invalidez, policial e PCD. Valores são **prosa descritiva por hipótese** (ex.: "Acidente em serviço, moléstia profissional…"; "Sim, quando a causa for doença grave…").                                      | R (+esboço de T) | **Evidência**: a PGE modela a causa como **coluna de análise (to-be) congelada**, por hipótese — **não** integrada por código, **não** no contrato deployável |
| **Texto legal** (`okf/dispositivos/`)                       | O **discriminante literal** integral↔proporcional aparece em **2 dispositivos**: `cf88/art-40-i-original.md` e `cf88/art-40-p1-i-ec41-2003.md` ("…acidente em serviço, moléstia profissional ou doença grave, contagiosa ou incurável, especificadas em lei, e proporcionais nos demais casos"). | R + T            | **Evidência**: o predicado existe como **prosa normativa**, remetendo a "**especificadas em lei**" (a taxonomia Q6‑T é externa)                               |
| **Fundamentação das regras** (`okf/regras-sisprev/regras/`) | A causa aparece como **prosa** na fundamentação de **8 regras**: `regra-0006/0007/0008/0009/0019/0020/0021/0022`.                                                                                                                                                                                | R                | **Evidência**: causa como **texto livre** no suporte, não como campo consultável                                                                              |
| **Solicitação do requerente** (laudo/perícia/processo)      | **Nenhum artefato no repo** modela a solicitação: não há laudo, campo de entrada, nem registro de perícia.                                                                                                                                                                                       | **S**            | **Lacuna de evidência (Q6‑S)** → §9                                                                                                                           |
| **Sisprev real** (tela / banco / processo)                  | **Nenhum artefato no repo** revela se a tela, o banco ou o processo do Sisprev já têm um campo de causa.                                                                                                                                                                                         | R/S/T            | **Lacuna de evidência** → §9                                                                                                                                  |

**Leitura:** o repositório prova que **não há predicado explícito de causa no
contrato de 27 colunas** e que **nada em código** a avalia; localiza a causa na
**análise da PGE** (Q6‑R, to-be) e na **prosa normativa** (Q6‑R + remessa a Q6‑T
"em lei"). O repositório **não** modela a **solicitação** (Q6‑S) e **não** revela
o que o **Sisprev em produção** já tem. Essas são as evidências que faltam.

## 4. Restrição explícita sobre A1 ("campo existente")

O que o repo prova é **estreito**: **não existe predicado explícito de causa nas
27 colunas do catálogo** (§2). Ele **não** prova que inexista um campo de causa
na **tela, no banco ou no processo do Sisprev real** — sobre isso o repo é
**silencioso** (§3, últimas linhas). Portanto "campo já existente" continua
**vivo como hipótese do lado da solicitação (Q6‑S)**; só está descartado como
predicado do catálogo (Q6‑R). Confirmar isso é a pergunta 1 do protocolo (§9).

## 5. Alternativas como eixos combináveis (não quatro substitutos)

Q6 não é "escolher 1 de 4". É **compor uma opção em cada eixo**. O desenho final
será quase certamente **híbrido**.

**Eixo Q6‑R — onde vive o predicado da regra:**

| Opção                                          | Proveniência                               | Auditabilidade                    | Round-trip              | Integração Sisprev              |
| ---------------------------------------------- | ------------------------------------------ | --------------------------------- | ----------------------- | ------------------------------- |
| **R1. Interpretação manual**                   | auditor lê a fundamentação                 | média (prosa)                     | fora do contrato        | nenhuma                         |
| **R2. Tabela/código externo**                  | Sisprev ou tabela versionada               | baixa se opaco; média se citável  | fora do contrato        | Sisprev precisa **ler** a fonte |
| **R3. Novo predicado estruturado no catálogo** | nova coluna P13.2 (ex.: `causas_integral`) | **alta** (versionada, detectores) | **entra** no round-trip | schema + motor                  |

**Eixo Q6‑S — o fato do requerente, em duas dimensões independentes.**
"Obter" e "registrar" **não** são alternativas: o fato pode ser **obtido** de um
laudo **e depois registrado** em campo. São dois sub-eixos que se combinam.

*Q6‑S‑obtenção — de onde o fato é apurado:*

| Opção                    | Proveniência                      | Momento              |
| ------------------------ | --------------------------------- | -------------------- |
| **So1. Laudo**           | laudo médico anexo                | entrada / perícia    |
| **So2. Perícia**         | perícia oficial                   | seleção ou posterior |
| **So3. Anamnese**        | declaração/entrevista na anamnese | entrada              |
| **So4. Sistema externo** | base de CID/laudos de terceiro    | conforme a fonte     |

*Q6‑S‑registro — onde o fato apurado fica persistido:*

| Opção                                    | Persistência                        | Auditabilidade          |
| ---------------------------------------- | ----------------------------------- | ----------------------- |
| **Sr1. Campo existente** (Sisprev real)  | tela/banco atual (a confirmar — §4) | a confirmar             |
| **Sr2. Campo novo de entrada**           | novo campo de solicitação           | alta se versionado      |
| **Sr3. Documento/prosa não estruturada** | anexo, observação livre             | baixa (não consultável) |
| **Sr4. Sem registro**                    | fato usado e descartado             | nenhuma                 |

**Eixo Q6‑T — classificação médico‑jurídica e nexo** (não só
diagnóstico→doença catalogada): "acidente em serviço" e "moléstia profissional"
dependem de **nexo causal/caracterização**, não apenas de uma tabela de doenças.

| Dimensão de Q6‑T | O que classifica                                            | Fonte possível                                         |
| ---------------- | ----------------------------------------------------------- | ------------------------------------------------------ |
| **T‑doença**     | doença é grave/contagiosa/incurável **catalogada**          | norma/lista oficial, tabela versionada ou juízo humano |
| **T‑acidente**   | o evento **caracteriza acidente em serviço**                | perícia + norma; caracterização, não tabela            |
| **T‑nexo**       | há **nexo de moléstia profissional**                        | perícia/nexo técnico + norma                           |
| **T‑vigência**   | **qual norma/tabela** aplicável e **sua vigência temporal** | dispositivo versionado (liga-se a Q1/Q2)               |

Cada dimensão pode vir de **norma/lista oficial**, **tabela versionada** ou
**interpretação humana** — auditável na proporção em que a fonte for citável.

**Como os eixos se combinam:** um predicado da regra (Q6‑R) só é aplicável a um
fato (Q6‑S: obtido **e** registrado) depois de **classificado** (Q6‑T, na
dimensão pertinente). As três respostas são **independentes** — nenhuma implica
a outra (ver a matriz da §8). Qual combinação é a real **depende da evidência de
§9**; hoje **todo o eixo Q6‑S (obtenção e registro) e a existência de campo real
são desconhecidos**.

## 6. Reaplicação de C2, C3, C4, C6, C8, C11 — condicional

Casos do piloto. Agora a leitura separa os três lados: uma indeterminação de
causa só se resolve quando **os três** estão disponíveis (predicado + fato +
taxonomia). "Resolve" deixou de ser incondicional.

| Caso                                         | Natureza                                          | Resolve? (condição)                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------- | ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **C2** (causa comum não catalogada)          | causa-axis, fato presente                         | **sim**, se R×S×T disponíveis (fato existe)                                                                                                                                                                                                                                                                                      |
| **C3** (acidente, ≤2003)                     | causa-axis, fato presente                         | **sim**, se R×S×T disponíveis                                                                                                                                                                                                                                                                                                    |
| **C4** (acidente, >2003)                     | causa-axis **+ transição de regime** (Q1/Q2)      | resolve **só a metade causa** (R×S×T); a **data/regime permanece indeterminado**                                                                                                                                                                                                                                                 |
| **C6** (causa **não informada**)             | possivelmente **fato ausente** (Q6‑S)             | **condicional**: **resolve** se a obtenção (laudo/perícia/anamnese/externo, So1–So4) fornecer o fato **e** houver onde registrá-lo; **permanece `indeterminado`** se a evidência não existir ou não estiver disponível no momento da seleção. "Não informada" pode significar apenas **ausente na anamnese**, não irrecuperável. |
| **C8** (doença grave; 0021 contraditória)    | causa-axis **+ dado defeituoso** (0021)           | resolve a causa (R×S×T); a **contradição da 0021 permanece**                                                                                                                                                                                                                                                                     |
| **C11** (doença catalogada **desconhecida**) | falta **predicado taxonômico** e/ou o diagnóstico | **condicional**: **resolve** se houver **diagnóstico conhecido (Q6‑S) + classificação por norma oficial (Q6‑T, dimensão T‑doença)**; **permanece `indeterminado`** se o próprio diagnóstico estiver ausente.                                                                                                                     |

**Conclusão da reaplicação:** resolver Q6 (nos três lados) resolve a
indeterminação **causa-axis** (C2, C3, metade de C4/C8) e **pode** resolver C6 e
C11 — **desde que o fato exista e esteja disponível** (C6) e que haja diagnóstico
mais taxonomia oficial (C11). **Não** resolve a **transição de regime** (a outra
metade de C4, Q1/Q2) nem o **dado defeituoso** (0021 em C8). Ou seja: **Q6 é
necessária, não suficiente** — Q1/Q2 e os defeitos de dados continuam.

## 7. Ressalva sobre a relação causa → integral/proporcional

A relação usada em toda esta análise ("acidente/moléstia/doença grave →
integral; causa comum → proporcional") é uma **relação observada** nos pares
as-is e **proposta** pela PGE, **ainda sujeita à validação jurídica** (as
hipóteses PGE têm `Validação PGE/Presidência = False`). Ela remete a doenças
"**especificadas em lei**" (§3), cuja lista (Q6‑T) é externa. **Não** a
apresento como regra universal fechada; fechá-la depende da taxonomia oficial e
da validação institucional.

## 8. Matriz de evidência — cada achado prova só o seu eixo

**Sem inferências entre eixos.** Uma evidência sobre um eixo (p.ex. persistência
em Q6‑S) **não** torna nada provável nos outros. Cada linha diz apenas: **o que
confirma**, **o que não confirma** e **qual pergunta permanece**. Nenhuma célula
autoriza "marcar como escolhida" uma opção em outro eixo.

| Evidência observável                      | Confirma                                                                  | **Não** confirma                                                                        | Pergunta que permanece                                             |
| ----------------------------------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **Existe campo de causa** no Sisprev real | **persistência** em Q6‑S (Sr1)                                            | nada sobre Q6‑S‑obtenção, Q6‑R nem Q6‑T                                                 | o campo é preenchido de onde? há predicado? há classificação/nexo? |
| **Laudo disponível** (anexo/perícia)      | uma **fonte de obtenção** possível (So1/So2)                              | **não** confirma registro (Sr?) nem o predicado (Q6‑R) nem o nexo (Q6‑T)                | o fato é persistido? onde? classificado como?                      |
| **Não há campo de causa**                 | ausência de **Sr1**                                                       | **não** obriga Sr2/So4/R3 — pode haver laudo (So1) + prosa (Sr3) + juízo humano em Q6‑T | qual obtenção e qual registro passam a valer?                      |
| **PGE tem coluna "Causa"** (§3)           | causa reconhecida como eixo na **análise**                                | **não** confirma integração em código, nem Q6‑S, nem vigência (Q6‑T)                    | a coluna prescreve entrada (Sr2) ou só descreve?                   |
| **Discriminante em 2 dispositivos** (§3)  | o **predicado** existe em prosa normativa (Q6‑R) + remessa "à lei" (Q6‑T) | **não** confirma estrutura consultável nem qualquer fato do requerente                  | a lista/nexo é citável como norma vigente?                         |
| **Nada em `scripts/`** avalia a causa     | ausência de motor/predicado **em código**                                 | **não** confirma ausência no Sisprev real (§4)                                          | como o Sisprev de produção decide hoje?                            |

**Leitura:** a única combinação que o repo **fixa** é parcial e só do lado do
predicado (Q6‑R existe em prosa). Todo o eixo **Q6‑S** (obtenção **e** registro)
e as dimensões de **Q6‑T** (doença/acidente/nexo/vigência) permanecem em aberto —
por isso não há linha "melhor caso/pior caso": não temos evidência para ordená-las.

Exemplo de **arquitetura auditável de destino** (a validar, **não** escolhido),
cobrindo **obtenção e persistência** explicitamente:
**obtenção** por laudo/perícia (So1/So2) → **persistência** em campo do
requerimento (Sr2) → **classificação/nexo** (Q6‑T) por fonte versionada e vigente
(dispositivo/tabela) → **comparação** com o predicado da regra (Q6‑R, ideal­mente
R3, que faz round-trip). Note que obtenção e registro são passos distintos: ler o
laudo não diz onde o fato fica persistido.

## 9. Fila de perguntas para responsáveis humanos (protocolo de investigação)

O repositório é **insuficiente** para fechar Q6 — sobretudo o lado **Q6‑S**
(solicitação) e a existência de campo real. Responder, com o Sisprev/PGE, **nesta
ordem** (cada resposta pode dispensar as seguintes):

1. **(Q6‑S‑registro/Sr1)** No Sisprev em produção, **existe hoje um campo** que registre a
   causa da incapacidade do requerente — na tela, no banco ou no processo? Onde?
   (Resolve a restrição do §4: confirma ou descarta "campo existente".)
2. **(Q6‑S)** Se **não** há campo, **de onde** viria o fato — laudo médico anexo,
   perícia, sistema externo de CID? Ele é **estruturado** ou prosa?
3. **(Q6‑S, momento)** A causa é conhecida **no momento da seleção** (após a
   anamnese) ou só depois (perícia posterior)? (Define se cabe no filtro ou é
   verificação tardia — e se C6 é recuperável.)
4. **(Q6‑R)** A seleção da regra hoje **usa** a causa? Se sim, o predicado
   ("quais causas → integral") está em **código/tabela** (R2) ou é **decisão do
   atendente** (R1)? É versionado e citável?
5. **(Q6‑T)** A "**doença catalogada em lei**" (a lista taxativa de doenças
   graves/contagiosas/incuráveis) existe como **norma/lista oficial**? Onde?
   Pode ser citada como `dispositivo`? (É o predicado taxonômico de C11.)
6. **(Q6‑R/PGE)** A coluna "Causa da incapacidade" da análise PGE é **descritiva**
   de cada hipótese ou **prescreve** um dado de entrada estruturado? (Confirma se
   a PGE propõe R3 e/ou Sr2.)
7. **(Produto)** Há **apetite** para evoluir o contrato deployável — novo
   predicado no catálogo (R3) e/ou novo campo de entrada (Sr2) — ou o Sisprev
   exige manter as 27 colunas fixas?

## 10. Conclusão

- **Q6 permanece aberta e é tripla.** A evidência do repo prova apenas que **não
  há predicado explícito de causa nas 27 colunas** (Q6‑R), e que **nada em
  código** a avalia; **localiza** a causa na análise PGE e na prosa normativa
  (com a taxonomia remetida "à lei", Q6‑T). O repo **não modela a solicitação**
  (Q6‑S) e **não revela** o que o Sisprev real já tem.
- **A1 ("campo existente") está descartada só como predicado do catálogo**, não
  como campo de entrada do Sisprev real (§4) — isso é a pergunta 1 do protocolo.
- **A escolha é uma combinação Q6‑R × Q6‑S × Q6‑T**, tipicamente híbrida, e
  **exige** as respostas de §9 — decidir agora seria inventar uma integração ou
  uma lacuna sem evidência operacional.
- **Q6 só é "necessária para o motor" sob duas condições:** (a) a relação
  causa→resultado (§7) ser **juridicamente validada** e (b) o motor de fato
  **selecionar automaticamente por esse eixo**. Se a seleção não usar a causa, ou
  se a relação não for validada, Q6 é relevante para explicação/auditoria, mas
  não um pré-requisito do motor.
- Mesmo satisfeitas essas condições, o piloto (§6) mostra que **Q1/Q2** (limite
  de data, transição de regime) e os **dados defeituosos** (0021, 0004) continuam
  gerando `indeterminado` — resolver Q6 **não basta** para um motor completo.

Sequência recomendada (inalterada): **§9 respondido → decisão humana sobre a
combinação R×S×T → correções in-place de invalidez → motor piloto**; a
reconciliação de pensão vem depois, já com o eixo causa decidido.

______________________________________________________________________

### Como as contagens foram obtidas (reprodutível)

Executar a partir da **raiz do repositório**.

```bash
# 8 regras com a causa em prosa (fundamentação):
rg -li "acidente em servi|mol[eé]stia profissional|doen[çc]a (grave|contagiosa|incur[aá]vel)|catalogada" \
  okf/regras-sisprev/regras/
# → regra-0006, -0007, -0008, -0009, -0019, -0020, -0021, -0022  (8 arquivos)

# 2 dispositivos com o discriminante literal integral↔proporcional
# (alternância nas duas ordens: "acidente…proporcionais" e "proporcionais…exceto…acidente"):
rg -li "(acidente em servi.*proporciona)|(proporciona.*acidente em servi)" okf/dispositivos/
# → cf88/art-40-i-original.md, cf88/art-40-p1-i-ec41-2003.md  (2 arquivos)

# 27 colunas do contrato (nenhuma de causa) — import a partir da raiz:
uv run python -c "from scripts.regra_schema import COLUMNS; print(len(COLUMNS))"
# → 27

# Ausência em código: nenhum arquivo em scripts/ avalia/importa/classifica a causa
# (o comando não retorna nada — ausência confirmada):
rg -li "causa.?incapacid|mol[eé]stia|acidente em servi|doen[çc]a.?catalog" scripts/
```
