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

| Sub‑questão | Lado                  | Pergunta                                                                                                                                                                          |
| ----------- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Q6‑R**    | regra (predicado)     | Onde vive o predicado que define **quais causas atendem** cada regra?                                                                                                             |
| **Q6‑S**    | solicitação (fato)    | Onde e **quando** vive o fato concreto da **causa do requerente**?                                                                                                                |
| **Q6‑T**    | classificação (ponte) | Onde vive a **classificação médico‑jurídica, o nexo e a vigência** — doença catalogada, **acidente em serviço** e **moléstia profissional** — que qualifica o fato do requerente? |

Q6‑T é a ponte: sem classificação/nexo, um laudo ("Q6‑S") não vira um valor
comparável ao predicado ("Q6‑R").

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

| Opção                                          | Proveniência                                                                                                                                                                           | Auditabilidade                    | Round-trip              | Integração Sisprev              |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | ----------------------- | ------------------------------- |
| **R1. Interpretação manual**                   | auditor lê a fundamentação                                                                                                                                                             | média (prosa)                     | fora do contrato        | nenhuma                         |
| **R2. Tabela/código externo**                  | Sisprev ou tabela versionada                                                                                                                                                           | baixa se opaco; média se citável  | fora do contrato        | Sisprev precisa **ler** a fonte |
| **R3. Novo predicado estruturado no catálogo** | nova coluna P13.2 (nome neutro, ex.: `criterio_causa_incapacidade` ou `classes_causa_admitidas` — **não** `causas_integral`, pois a relação causa→integral ainda não foi validada, §7) | **alta** (versionada, detectores) | **entra** no round-trip | schema + motor                  |

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
fato (Q6‑S) que foi **obtido** e **classificado** (Q6‑T, na dimensão pertinente).
O **registro** (Q6‑S‑registro) não é pré-condição da *decisão* — uma decisão
humana efêmera pode usar o fato e descartá-lo (**Sr4**); ele é pré-condição da
**auditabilidade e da reprodutibilidade**. Por isso **Sr4 (sem registro) é um
risco a tratar**, não uma opção neutra: a decisão até acontece, mas não é
auditável nem reproduzível. As três respostas (R, S, T) são **independentes** —
nenhuma implica a outra (ver a matriz da §8). Qual combinação é a real **depende
da evidência de §9**; hoje **todo o eixo Q6‑S (obtenção e registro) e a
existência de campo real são desconhecidos**.

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
(dispositivo/tabela) → **comparação** com o predicado da regra (Q6‑R — sob a
direção A do §10, representado por **linha‑classe** discriminada pelos campos
materiais existentes, `fundamentacao*`/flags/cálculos, não por uma coluna nova).
Note que obtenção e registro são passos distintos: ler o laudo não diz onde o
fato fica persistido.

## 9. Fila de perguntas para responsáveis humanos (protocolo de investigação)

O repositório é **insuficiente** para fechar Q6 — sobretudo o lado **Q6‑S**
(solicitação) e a existência de campo real. Responder, com o Sisprev/PGE, **nesta
ordem** (cada resposta pode dispensar as seguintes). **A pergunta 10 já foi
respondida pela decisão do responsável (§10)** — as demais permanecem
perguntas factuais em aberto:

01. **(Q6‑S‑registro/Sr1)** No Sisprev em produção, **existe hoje um campo** que registre a
    causa da incapacidade do requerente — na tela, no banco ou no processo? Onde?
    (Resolve a restrição do §4: confirma ou descarta "campo existente".)
02. **(Q6‑S‑obtenção)** Se **não** há campo, **de onde** viria o fato — laudo médico anexo,
    perícia, sistema externo de CID? Ele é **estruturado** ou prosa?
03. **(Q6‑S‑registro)** Depois de **obtido**, onde o fato fica **persistido** — em
    **campo** (Sr1/Sr2), em **documento/prosa** não estruturada (Sr3) ou em **lugar
    nenhum** (Sr4)? (Distingue decisão auditável de uso efêmero — ver §5.)
04. **(Q6‑S, momento)** A causa é conhecida **no momento da seleção** (após a
    anamnese) ou só depois (perícia posterior)? (Define se cabe no filtro ou é
    verificação tardia — e se C6 é recuperável.)
05. **(Q6‑R)** A seleção da regra hoje **usa** a causa? Se sim, o predicado
    ("quais causas → integral") está em **código/tabela** (R2) ou é **decisão do
    atendente** (R1)? É versionado e citável?
06. **(Q6‑T, doença)** A "**doença catalogada em lei**" (a lista taxativa de doenças
    graves/contagiosas/incuráveis) existe como **norma/lista oficial**? Onde?
    Pode ser citada como `dispositivo`? (É o predicado taxonômico de C11.)
07. **(Q6‑T, acidente/nexo)** **Quem caracteriza** "acidente em serviço" e o
    **nexo de moléstia profissional** — perito, junta, autoridade? Com **quais
    critérios e evidências**? (Essa caracterização é o que Q6‑T resolve para
    além da lista de doenças.)
08. **(Q6‑T, vigência)** **Qual data** determina a **versão vigente** da
    norma/lista/taxonomia aplicável ao caso — a do fato gerador, a do requerimento,
    a da concessão? (Liga Q6‑T‑vigência a Q1/Q2.)
09. **(Q6‑R/PGE)** A coluna "Causa da incapacidade" da análise PGE é **descritiva**
    de cada hipótese ou **prescreve** um dado de entrada estruturado? (Confirma se
    a PGE propõe R3 e/ou Sr2.)
10. **(Produto) — *Respondida pela decisão do §10*.** Há **apetite** para evoluir
    o contrato deployável — novo predicado no catálogo (R3) e/ou novo campo de
    entrada (Sr2) — ou o Sisprev exige manter as 27 colunas fixas? **Resposta:
    o Sisprev mantém as 27 colunas fixas** — o responsável fixou a restrição de
    produto e, sob ela, a direção A do §10 (linha por classe de causa material).

## 10. Decisão do responsável — direção A (classes de causa) e contingência B

O responsável pela decisão fixou uma **restrição de produto** que estreita o
espaço de §5: **manter o schema atual** (as 27 colunas, sem tabela nova) — isto é,
a resposta à pergunta 10 do protocolo é *"o Sisprev mantém as colunas fixas"*.
Sob essa restrição, a alavanca disponível são as **linhas**, não novas colunas
— o que **descarta o R3** (coluna nova) **e uma nova tabela deployável/novo
contrato consumido pelo Sisprev** (ambos incompatíveis com "o formato
deployável só usa os campos que o Sisprev já tem"). Isso **não** descarta uma
**fonte normativa externa** (a lista oficial de doenças, por exemplo) —
apenas a impede de virar um **novo contrato deployável**; como **evidência
versionada e citável**, ela continua representável em **Q6‑T/dispositivos**
(§5), fora do catálogo. Registro a direção adotada (**A**) e a contingência
documentada (**B**).

### A — direção adotada: uma linha por *classe de causa* material

Uma **linha por classe de causa juridicamente material** — a classe que de fato
**altera elegibilidade, cálculo ou fundamentação** (acidente em serviço /
moléstia profissional / doença catalogada em lei / causa comum) — **não** uma
linha por doença individual. A unidade da linha é a **classe de causa material**,
não o diagnóstico.

- **A lista de doenças permanece, por padrão, em Q6‑T**, como **taxonomia
  médico‑jurídica versionada** (norma/lista oficial + vigência — §5, eixo Q6‑T).
  Ela **não** é materializada como linhas de catálogo; o que entra como linha é a
  *classe*, não cada doença da lista.
- **`nome` é a interface humana de seleção** — o rótulo que o atendente lê para
  escolher a regra depois da anamnese/perícia — **mas não é material para o P2**.
- **A distinção material entre regras vem dos campos de domínio que o P2
  considera** — inclusive `fundamentacao`/`fundamentacao_integral`/
  `fundamentacao_proporcional`, além dos flags e cálculos aplicáveis (`integral`,
  `tipo_calculo`, datas, `sexo`, `paridade`, …). Duas linhas que representem
  classes de causa materialmente distintas diferem **nesses campos**, nunca só no
  `nome`.

Forma resultante (tudo em campos existentes; o material é a `fundamentacao*`/
flags, não o rótulo):

```yaml
nome: "Invalidez — doença catalogada em lei — ingresso pós-2003"  # rótulo de seleção; NÃO material ao P2
integral: S
tipo_calculo: <x>
fundamentacao_integral: <dispositivo da classe "doença catalogada">  # material que o P2 considera
# datas/sexo/paridade como nas demais regras
```

### B — contingência documentada: uma linha por doença individual

Uma **linha por doença individual** só se justifica **se futura evidência
normativa ou necessidade operacional exigir essa granularidade** (p.ex. a lei
passar a atribuir resultado distinto a uma doença específica). **Não** é a
direção adotada; é uma contingência registrada, para não reabrir a decisão se o
caso surgir.

- Se B produzir **linhas distintas apenas pelo `nome`** (mesma `fundamentacao*`,
  mesmos flags/cálculos), o **P2 deve detectá-las como materialmente iguais** —
  esse é o comportamento **correto**, não um defeito a corrigir. A **persistência
  intencional** dessas linhas é registrada por um achado `situacao: resolvido`
  com **`efeito_deteccao: pode_persistir`** (mecanismo que já existe no schema de
  achados, `achado_schema.py`) — **sem alterar o P2 e sem tornar `nome`
  material**.

### Q6‑S não é resolvido por esta decisão

A escolha humana pelo `nome` **apenas seleciona a regra** depois que a
anamnese/perícia já apurou a causa; ela **não resolve Q6‑S**. **Obter** o fato da
causa do requerente e **registrá-lo** de forma auditável continuam sendo
responsabilidade do **processo** — as perguntas 1–4 do §9 seguem abertas.
Selecionar por nome ≠ obter/registrar o fato.

### Custos honestos que permanecem (não bloqueiam)

1. **A lista de doenças é manutenção de Q6‑T, não de linhas.** Como a lista fica
   na taxonomia versionada (não vira linhas), alterá-la é editar a taxonomia
   Q6‑T, não adicionar/remover linhas de regra. Uma linha só muda quando muda a
   **classe de causa** materialmente (novo dispositivo, novo resultado).
2. **Cada linha‑classe deve diferir em campo material.** Para as classes de causa
   (acidente / moléstia / doença catalogada / comum) a `fundamentacao` tende a
   diferir de fato (evidência PGE: pós‑2003 separa 6/7/9; épocas distintas →
   dispositivos distintos). Se, por engano, duas linhas não diferirem em **nada
   material** (só no `nome`), o **P2 as acusa — e corretamente**: isso é o caso B,
   e a persistência, se intencional, é registrada por `efeito_deteccao: pode_persistir`, nunca tornando o `nome` material.

**O que continua contingente (não decidido por esta nota):** a **lista oficial**
de doenças catalogadas e sua vigência (Q6‑T, perguntas 6–8), se a **LC 1.100/2021
discrimina as causas em dispositivos distintos**, a **hipótese 8 ausente** do
espelho PGE, e a **validação jurídica** da relação causa→resultado (§7). Esta nota
fixa a *forma* do lado Q6‑R (linha por classe de causa material, discriminada
pelos campos que o P2 considera; `nome` apenas como rótulo), não os *fatos
normativos* que preenchem cada linha, nem o eixo Q6‑S.

## 11. Conclusão

- **Q6 permanece aberta e é tripla.** A evidência do repo prova apenas que **não
  há predicado explícito de causa nas 27 colunas** (Q6‑R), e que **nada em
  código** a avalia; **localiza** a causa na análise PGE e na prosa normativa
  (com a taxonomia remetida "à lei", Q6‑T). O repo **não modela a solicitação**
  (Q6‑S) e **não revela** o que o Sisprev real já tem.
- **A1 ("campo existente") está descartada só como predicado do catálogo**, não
  como campo de entrada do Sisprev real (§4) — isso é a pergunta 1 do protocolo.
- **A escolha é uma combinação Q6‑R × Q6‑S × Q6‑T** — e o responsável fixou a
  **forma do lado Q6‑R** sob schema fixo (§10, direção A): uma **linha por classe
  de causa juridicamente material**, discriminada pelos **campos de domínio que o
  P2 considera** (`fundamentacao*`, flags, cálculos), com o `nome` apenas como
  **rótulo de seleção — não material ao P2**. A **lista de doenças permanece em
  Q6‑T** (taxonomia versionada, representável em dispositivos), não como
  linhas. Isso descarta o R3 e uma nova tabela deployável — **não** a fonte
  normativa externa em si, que Q6‑T continua podendo citar. **Q6‑S segue
  aberto** — obtenção e registro do fato (perguntas 1–4 do
  §9) não são resolvidos pela seleção por nome. Uma linha por doença individual é
  só a **contingência B** (§10), sob a qual o P2 deve acusar igualdade material e
  a persistência intencional se registra por `efeito_deteccao: pode_persistir`.
- **Q6 só é "necessária para o motor" sob duas condições:** (a) a relação
  causa→resultado (§7) ser **juridicamente validada** e (b) o motor de fato
  **selecionar automaticamente por esse eixo**. Se a seleção não usar a causa, ou
  se a relação não for validada, Q6 é relevante para explicação/auditoria, mas
  não um pré-requisito do motor.
- Mesmo satisfeitas essas condições, o piloto (§6) mostra que **Q1/Q2** (limite
  de data, transição de regime) e os **dados defeituosos** (0021, 0004) continuam
  gerando `indeterminado` — resolver Q6 **não basta** para um motor completo.

Sequência recomendada (atualizada): **forma fixada (§10, direção A) → §9
respondido nos fatos normativos (lista oficial, dispositivos, vigência) →
materializar as linhas por *classe de causa material* no catálogo → correções
in-place de invalidez → motor piloto**; a reconciliação de pensão vem depois, já
com o eixo causa decidido.

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

# Ausência em código: nenhum arquivo em scripts/ avalia/importa/classifica a
# causa, nem o insumo do fato (CID/diagnóstico/laudo/perícia). O `! rg` faz a
# ausência ser provada pelo EXIT CODE (0 = nada encontrado = ausência confirmada):
! rg -li "causa.?incapacid|mol[eé]stia|acidente em servi|doen[çc]a.?catalog|\bCID\b|diagn[oó]stic|laudo|per[ií]cia" scripts/ \
  && echo "ausência confirmada"
```
