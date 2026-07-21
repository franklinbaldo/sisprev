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

**Eixo Q6‑S — onde vive o fato do requerente:**

| Opção                                      | Proveniência                        | Auditabilidade           | Momento                      |
| ------------------------------------------ | ----------------------------------- | ------------------------ | ---------------------------- |
| **S1. Laudo/perícia manual**               | atendente/perito lê o laudo         | média/alta se registrada | seleção ou perícia posterior |
| **S2. Registro externo**                   | sistema de laudos/CID já existente  | depende da fonte         | conforme a fonte             |
| **S3. Campo já existente no Sisprev real** | tela/banco atual (a confirmar — §4) | a confirmar              | entrada do requerimento      |
| **S4. Novo campo de entrada**              | novo campo de solicitação           | alta se versionado       | entrada do requerimento      |

**Eixo Q6‑T — onde vive a taxonomia (diagnóstico → categoria):**

| Opção                        | Proveniência                                                    | Auditabilidade                         |
| ---------------------------- | --------------------------------------------------------------- | -------------------------------------- |
| **T1. Norma/lista oficial**  | a lei que "especifica" as doenças graves/contagiosas/incuráveis | **alta** se citável como `dispositivo` |
| **T2. Tabela versionada**    | tabela mantida no repo/Sisprev                                  | alta                                   |
| **T3. Interpretação humana** | perito/jurista classifica caso a caso                           | média                                  |

**Como os eixos se combinam:** o predicado (Q6‑R) só é aplicável se houver um
fato (Q6‑S) **já classificado** pela taxonomia (Q6‑T). Ex. de híbrido plausível:
**fato obtido manualmente (S1) + taxonomia oficial (T1) + predicado estruturado
no catálogo (R3)**. Qual combinação é a real **depende da evidência de §9** — em
especial, Q6‑S e a existência de um campo real (S3) são hoje **desconhecidas**.

## 6. Reaplicação de C2, C3, C4, C6, C8, C11 — condicional

Casos do piloto. Agora a leitura separa os três lados: uma indeterminação de
causa só se resolve quando **os três** estão disponíveis (predicado + fato +
taxonomia). "Resolve" deixou de ser incondicional.

| Caso                                         | Natureza                                          | Resolve? (condição)                                                                                                                                                                                                                                                                  |
| -------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **C2** (causa comum não catalogada)          | causa-axis, fato presente                         | **sim**, se R×S×T disponíveis (fato existe)                                                                                                                                                                                                                                          |
| **C3** (acidente, ≤2003)                     | causa-axis, fato presente                         | **sim**, se R×S×T disponíveis                                                                                                                                                                                                                                                        |
| **C4** (acidente, >2003)                     | causa-axis **+ transição de regime** (Q1/Q2)      | resolve **só a metade causa** (R×S×T); a **data/regime permanece indeterminado**                                                                                                                                                                                                     |
| **C6** (causa **não informada**)             | possivelmente **fato ausente** (Q6‑S)             | **condicional**: **resolve** se perícia/laudo/fonte externa (S1/S2/S3) fornecer o fato; **permanece `indeterminado`** se a evidência não existir ou não estiver disponível no momento da seleção. "Não informada" pode significar apenas **ausente na anamnese**, não irrecuperável. |
| **C8** (doença grave; 0021 contraditória)    | causa-axis **+ dado defeituoso** (0021)           | resolve a causa (R×S×T); a **contradição da 0021 permanece**                                                                                                                                                                                                                         |
| **C11** (doença catalogada **desconhecida**) | falta **predicado taxonômico** e/ou o diagnóstico | **condicional**: **resolve** se houver **diagnóstico conhecido (Q6‑S) + taxonomia oficial (Q6‑T = T1)**; **permanece `indeterminado`** se o próprio diagnóstico estiver ausente.                                                                                                     |

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

## 8. Matriz de decisão — combinações Q6‑R × Q6‑S × Q6‑T

O resultado esperado é **uma combinação**, tipicamente híbrida. Nenhuma célula
pode ser **marcada como escolhida** sem a evidência do protocolo abaixo.

| Se o Sisprev real…                     | Então Q6‑S          | Q6‑R provável | Q6‑T  | Observação                                                           |
| -------------------------------------- | ------------------- | ------------- | ----- | -------------------------------------------------------------------- |
| **já tem campo de causa** (tela/banco) | **S3**              | R2 ou R3      | T1/T2 | melhor caso: fato já capturado; falta só auditar predicado+taxonomia |
| tem **laudo mas sem campo**            | S1/S2               | R1→R3         | T1/T3 | fato existe, precisa ser extraído e classificado                     |
| **não captura a causa**                | **S4** (novo campo) | R3            | T1/T2 | pior caso: exige evoluir entrada **e** catálogo                      |

Exemplo de desenho auditável de destino (a validar, não escolhido): **S1 (laudo
manual) + T1 (lista oficial como `dispositivo`) + R3 (predicado estruturado no
catálogo)** — fato registrado no requerimento, classificado por norma citável,
comparado a um predicado versionado que faz round-trip.

## 9. Fila de perguntas para responsáveis humanos (protocolo de investigação)

O repositório é **insuficiente** para fechar Q6 — sobretudo o lado **Q6‑S**
(solicitação) e a existência de campo real. Responder, com o Sisprev/PGE, **nesta
ordem** (cada resposta pode dispensar as seguintes):

1. **(Q6‑S/S3)** No Sisprev em produção, **existe hoje um campo** que registre a
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
   a PGE propõe R3 e/ou S4.)
7. **(Produto)** Há **apetite** para evoluir o contrato deployável — novo
   predicado no catálogo (R3) e/ou novo campo de entrada (S4) — ou o Sisprev
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
- Mesmo resolvida Q6, o piloto (§6) mostra que **Q1/Q2** (limite de data,
  transição de regime) e os **dados defeituosos** (0021, 0004) continuam gerando
  `indeterminado` — Q6 é necessária, não suficiente, para um motor.

Sequência recomendada (inalterada): **§9 respondido → decisão humana sobre a
combinação R×S×T → correções in-place de invalidez → motor piloto**; a
reconciliação de pensão vem depois, já com o eixo causa decidido.

______________________________________________________________________

### Como as contagens foram obtidas (reprodutível)

```bash
# 8 regras com a causa em prosa (fundamentação):
grep -rliE "acidente em servi|mol[eé]stia profissional|doen[çc]a (grave|contagiosa|incur[aá]vel)|catalogada" \
  okf/regras-sisprev/regras/regra-*.md
# → regra-0006, -0007, -0008, -0009, -0019, -0020, -0021, -0022

# 2 dispositivos com o discriminante literal integral↔proporcional:
grep -rliE "acidente em servi.*proporciona|proporciona.*acidente em servi" okf/dispositivos/**/*.md
# → cf88/art-40-i-original.md, cf88/art-40-p1-i-ec41-2003.md

# 27 colunas do contrato (nenhuma de causa):
python -c "from regra_schema import COLUMNS; print(len(COLUMNS))"
```
