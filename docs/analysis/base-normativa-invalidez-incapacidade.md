# Base normativa — Aposentadoria por Invalidez / Incapacidade Permanente

> **Nota:** Relatório gerado por IA como apoio à decisão. **Não é artefato
> oficial**, não edita nenhuma `regra-*.md`, não altera schema, dados
> derivados (`data/regras-sisprev.csv`), motor ou `site/`. Cobre **apenas**
> `okf/dispositivos/` (bundle P3, decomposição sob demanda) e este documento
> de análise. Toda mudança final nas regras é ato humano, in-place, em PR
> separada, depois de decisão sobre as pendências abaixo.

## 1. Escopo e método

Inventaria **cada afirmação jurídica** citada pelas 11 regras as-is de
invalidez/incapacidade (`regra-0001`, `0002`, `0004`, `0006`–`0009`,
`0019`–`0022`) e pelas 8 hipóteses da análise PGE (**P1–P7 e P9** — a
numeração pula a 8, ver
[reconciliação, §4](reconciliacao-invalidez-incapacidade.md#4-tens%C3%B5es-e-erros-na-pr%C3%B3pria-an%C3%A1lise-da-pge-n%C3%A3o-copiar-cegamente)),
confronta cada uma com uma **fonte oficial primária**, e adiciona a
`okf/dispositivos/` **apenas** os dispositivos ausentes cuja redação e
vigência puderam ser verificadas.

Fontes usadas (URLs completas em cada dispositivo, campo `fonte:`):

- **Planalto** (`planalto.gov.br`) para CF/88 e emendas constitucionais
  federais — texto compilado buscado diretamente (nunca de memória).
- **Casa Civil/Governadoria de Rondônia** (`ditel.casacivil.ro.gov.br`) para
  as compilações oficiais de LCE 432/2008 e LCE 1.100/2021 — cada uma
  marca inline toda alteração ("Redação dada pela...", "Acrescido
  pela...", "Revogado pela..."), o que permite confirmar quando um trecho
  **não** anotado é a redação original.
- **ALE-RO/SAPL** (`sapl.al.ro.leg.br`) para a ECE 146/2021 — o PDF é
  digitalizado/assinado (sem texto extraível); conferido por OCR e
  **verificado visualmente** contra a imagem da página. O endpoint ao vivo
  respondeu HTTP 429 durante a pesquisa; o arquivo foi obtido por uma
  cópia arquivada (Wayback Machine) do mesmo URL oficial — confiança
  **MEDIUM**, registrada na pendência P-EC146 (§6).

Todas as demais fontes (LCE 432/2008, LCE 1.100/2021, CF/88 e emendas
federais) foram lidas diretamente do PDF/HTML oficial nesta sessão —
confiança **HIGH**.

## 2. Dispositivos adicionados nesta PR

| Dispositivo                  | Norma                                   | Vigência formal                       | Fonte                            | Confiança |
| ---------------------------- | --------------------------------------- | ------------------------------------- | -------------------------------- | --------- |
| `cf88/art-40-p1-i-ec20-1998` | CF/88, art. 40 §1º I (EC 20/1998)       | 1998-12-16 → 2003-12-30               | Planalto (`emc20.htm`)           | HIGH      |
| `lce-432-2008/art-17`        | LCE 432/2008, art. 17 (íntegra)         | (original) → 2021-10-18               | Casa Civil/RO — LC432 compilada  | HIGH      |
| `lce-432-2008/art-20-caput`  | LCE 432/2008, art. 20 caput             | (original) → 2021-10-18               | idem                             | HIGH      |
| `lce-432-2008/art-20-p1`     | LCE 432/2008, art. 20 §1º               | (original) → 2021-10-18               | idem                             | HIGH      |
| `lce-432-2008/art-20-p2`     | LCE 432/2008, art. 20 §2º               | (original) → 2021-10-18               | idem                             | HIGH      |
| `lce-432-2008/art-20-p9`     | LCE 432/2008, art. 20 §9º               | (original) → 2021-10-18               | idem                             | HIGH      |
| `lce-432-2008/art-20-p14`    | LCE 432/2008, art. 20 §14               | (original) → 2021-10-18               | idem                             | HIGH      |
| `lce-432-2008/art-45`        | LCE 432/2008, art. 45                   | 2012-08-09 (LC 672/2012) → 2021-10-18 | idem                             | HIGH      |
| `lce-432-2008/art-62`        | LCE 432/2008, art. 62 caput             | (original) → 2021-10-18               | idem                             | HIGH      |
| `ece-146-2021/art-4`         | ECE 146/2021, art. 4º (caput + § único) | 2021-09-09 →                          | ALE-RO/SAPL (via Wayback)        | MEDIUM    |
| `lce-1100-2021/art-25`       | LCE 1.100/2021, art. 25 (íntegra)       | 2021-10-18 →                          | Casa Civil/RO — LC1100 compilada | HIGH      |
| `lce-1100-2021/art-27-i`     | LCE 1.100/2021, art. 27, I              | 2021-10-18 →                          | idem                             | HIGH      |
| `lce-1100-2021/art-30-p1`    | LCE 1.100/2021, art. 30 §1º             | 2021-10-18 →                          | idem                             | HIGH      |
| `lce-1100-2021/art-30-p2`    | LCE 1.100/2021, art. 30 §2º             | 2021-10-18 →                          | idem                             | HIGH      |
| `lce-1100-2021/art-30-p5`    | LCE 1.100/2021, art. 30 §5º             | 2021-10-18 →                          | idem                             | HIGH      |
| `lce-1100-2021/art-30-p6`    | LCE 1.100/2021, art. 30 §6º             | 2021-10-18 →                          | idem                             | HIGH      |
| `lce-1100-2021/art-30-p8`    | LCE 1.100/2021, art. 30 §8º             | 2021-10-18 →                          | idem                             | HIGH      |

Também foi completado `vigencia_inicio`/`vigencia_fim` — a pedido explícito
de revisão — nos dispositivos **federais já existentes** e efetivamente
citados por este conjunto (conferidos no Planalto): `cf88/art-40-i-original`
(1988-10-05 → 1998-12-15), `cf88/art-40-p1-i-ec41-2003` (2003-12-31 →
2019-11-12), `cf88/art-40-p1-i-ec103-2019` e
`cf88/art-40-p1-iii-ec103-2019` (2019-11-13 →, EC 103/2019 art. 36, III —
"nos demais casos, na data de sua publicação"), `ec-41-2003/art-6a-ec70-2012`
(2012-03-30 →).

**Distinção que a coluna "vigência formal" acima cobre — e não cobre**: é a
data em que **aquela redação do dispositivo** existiu, nunca por si só uma
afirmação sobre **quem** ela alcança hoje (direito adquirido, regra de
transição, data do fato gerador × data de ingresso). Essa segunda pergunta
é o "critério temporal de aplicação ao caso" da matriz do §3 — as duas
colunas são deliberadamente mantidas separadas, a pedido de revisão desta
PR: reduzir vigência formal a aplicabilidade seria presumir a resposta a
uma pergunta ainda em aberto (reconciliação, §3).

## 3. Matriz afirmação → dispositivo → regra/hipótese → vigência

Legenda de **Aplicabilidade**: **confirmada** = o próprio texto do
dispositivo (não uma inferência externa) declara o critério temporal;
**pendente** = nenhum dispositivo lido nesta pesquisa fixa o critério, ou
há tensão entre o texto e o rótulo dado pela regra/PGE.

### 3.1 Regimes anteriores a EC 41/2003 (`regra-0001`, `0002`, `0004`) — sem hipótese PGE correspondente

| Afirmação                                            | Dispositivo                         | Regra(s)   | Hipótese PGE | Vigência formal         | Critério temporal de aplicação ao caso                                                                                                                                | Aplicabilidade | Fonte da conclusão                                            | Pendência |
| ---------------------------------------------------- | ----------------------------------- | ---------- | ------------ | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------- | --------- |
| "Art. 40, inciso I da CF/1988 em seu texto original" | `cf88/art-40-i-original`            | 0001, 0002 | (nenhuma)    | 1988-10-05 → 1998-12-15 | Não fixado pelo próprio texto (regra geral de invalidez, sem cláusula de ingresso/transição) — nem confirma nem descarta alcançar fato gerador posterior a 1998-12-15 | **pendente**   | Texto do dispositivo (Planalto) — silente sobre ultratividade | P-1       |
| "Art 40, §1º, I, da CF com redação da EC 20/98"      | `cf88/art-40-p1-i-ec20-1998` (novo) | 0004       | (nenhuma)    | 1998-12-16 → 2003-12-30 | idem — regra geral, sem cláusula de ingresso/transição no próprio texto                                                                                               | **pendente**   | idem                                                          | P-1       |

**P-1 — pendência estrutural (não resolvida por esta PR):** nem o texto
original de 1988 nem a redação EC 20/1998 do art. 40, §1º, I contêm, elas
mesmas, um critério de ingresso ou de transição — ao contrário do que se vê
em `ec-41-2003/art-6a-ec70-2012` e em `lce-1100-2021/art-25`/`art-27-i`
(§3.2–3.3, ambos **explicitamente** ancorados em "que tenha ingressado...
até..."). Isso é compatível com duas leituras opostas, nenhuma decidida
aqui: **(a)** a redação vigente no momento da concessão/fato gerador é a
que se aplica (regra geral de efeito imediato de norma de custeio/benefício
público) — nesse caso 0001/0002/0004 estariam **de fato superadas**, porque
qualquer fato gerador atual cairia sob a redação em vigor hoje (LC
1.100/2021, se pós-EC103, ou EC 41/2003 art. 6º-A, se o servidor ingressou
até 31/12/2003 — que **inclui** quem ingressou antes de 1998, ver §5);
**(b)** direito adquirido preserva a redação vigente no momento do
**ingresso**, hipótese sob a qual 0001/0002/0004 continuariam vivas para
quem ingressou nessas janelas. **Decidir contra fonte jurídica primária
(doutrina/jurisprudência de direito previdenciário), não presumir** — é
exatamente a pergunta do §3 da reconciliação, ainda aberta.

### 3.2 EC 41/2003 + LCE 432/2008 (`regra-0006`–`0009`) — hipóteses P1–P4

| Afirmação                                                                                                  | Dispositivo                                                               | Regra(s)                   | Hipótese PGE       | Vigência formal                                            | Critério temporal de aplicação ao caso                                                                                                                                                                                                                                                                | Aplicabilidade                                                                                                                                        | Fonte da conclusão                                                | Pendência                        |
| ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | -------------------------- | ------------------ | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | -------------------------------- |
| "Art. 40, §1º, I da CF, EC 41/2003" (regra geral, sem exceção de carve-out)                                | `cf88/art-40-p1-i-ec41-2003`                                              | 0006, 0007, 0008\*, 0009\* | P1, P2, P3\*, P4\* | 2003-12-31 → 2019-11-12                                    | Não fixado pelo próprio texto — aplica-se por exclusão a quem **não** está sob o carve-out do art. 6º-A (ingresso ≤ 2003)                                                                                                                                                                             | **pendente** (leitura por exclusão, não afirmação textual)                                                                                            | Texto do dispositivo + leitura sistemática com `art-6a-ec70-2012` | P-2                              |
| "Artigos 17, 20 caput, 45 e 62 da LCE 432/2008" (proporcional e integral)                                  | `lce-432-2008/art-17`, `art-20-caput`, `art-45`, `art-62`                 | 0006, 0007                 | P1, P2             | (original) → 2021-10-18                                    | Regra geral de cálculo/reajuste do regime LCE 432/2008, sem cláusula de ingresso própria — aplicável a quem se aposenta sob esse regime                                                                                                                                                               | **pendente** (mesma leitura sistemática de P-2)                                                                                                       | Texto do dispositivo                                              | P-2                              |
| "Art. 20, §14º e Art. 45 da LC 432/2008" (fundamentação própria de 0007)                                   | `lce-432-2008/art-20-p14`, `art-45`                                       | 0007                       | P2                 | (original) → 2021-10-18                                    | idem                                                                                                                                                                                                                                                                                                  | **pendente**                                                                                                                                          | Texto do dispositivo                                              | —                                |
| "Art. 4º da EC Estadual nº 146/2021"                                                                       | `ece-146-2021/art-4`                                                      | 0006, 0007, 0008, 0009     | P1–P4              | 2021-09-09 →                                               | **Confirmado pelo próprio texto**: preserva a legislação vigente **até 2021-09-09** para quem cumprir os requisitos **até 2024-12-31**, "assegurada a qualquer tempo" — critério é cumprimento de requisitos, não ingresso                                                                            | **confirmada** (quanto ao próprio art. 4º; não resolve qual legislação "vigente até 2021-09-09" se aplica a cada caso — isso remonta às linhas acima) | Texto do dispositivo (ALE-RO)                                     | P-EC146 (confiança da fonte, §6) |
| "Art. 40, § 1°, inciso III, da CF, EC 103/2019" (0006/0007, integral)                                      | `cf88/art-40-p1-iii-ec103-2019`                                           | 0006, 0007                 | —                  | 2019-11-13 →                                               | N/A — o inciso III (EC 103/2019) trata de aposentadoria **voluntária** por idade, não de invalidez; citação incompatível com a matéria da regra                                                                                                                                                       | **N/A — citação a revisar**, não a "aplicar"                                                                                                          | Texto do dispositivo, cotejado com a matéria da regra             | P-3                              |
| "Art. 6º-A da EC 41/2003, redação EC 70/2012" + "Art. 20 da LCE 432/2008" (0008/0009, proporcional)        | `ec-41-2003/art-6a-ec70-2012`, `lce-432-2008/art-20-caput`                | 0008, 0009                 | P3, P4             | 6º-A: 2012-03-30 → / LC432 art.20: (original) → 2021-10-18 | **Confirmado pelo próprio texto do art. 6º-A**: "servidor... que tenha ingressado no serviço público **até a data de publicação desta Emenda Constitucional** [2003-12-31] e que tenha se aposentado ou venha a se aposentar por invalidez permanente..." — ingresso é o critério, explícito na norma | **confirmada**                                                                                                                                        | Texto do dispositivo (Planalto)                                   | —                                |
| "Art. 20, caput, §9º da LCE 432/2008" + "Art. 40, §1º, III, 2ª parte, CF EC103/2019" (0008/0009, integral) | `lce-432-2008/art-20-caput`, `art-20-p9`, `cf88/art-40-p1-iii-ec103-2019` | 0008, 0009                 | P4                 | ver linhas acima                                           | idem (LCE 432/2008); a citação de CF art. 40 §1 III "2ª parte" tem o mesmo problema de matéria da linha P-3, agravado — ver reconciliação §4                                                                                                                                                          | **N/A — citação a revisar**                                                                                                                           | idem                                                              | P-3, P-4                         |

\* 0008/0009 → P3/P4 citam o **art. 40 §1º I EC41/2003** apenas na
fundamentação **proporcional**; a integral cita o inciso III (linha
seguinte).

**P-2 — mesma pendência estrutural de P-1, agora para o regime EC 41/2003 +
LCE 432/2008**: nem `cf88/art-40-p1-i-ec41-2003` nem os artigos gerais da
LCE 432/2008 (17, 20 caput, 45, 62) trazem, no próprio texto, uma cláusula
de ingresso ou transição — a fronteira "após 2003" de `regra-0006`/`0007`
só existe **por exclusão** do carve-out explícito do art. 6º-A (que cobre
"quem ingressou até 2003"). Isto é uma leitura sistemática razoável, não
uma afirmação textual direta — permanece pendente de confirmação jurídica
formal, como P-1.

**P-3 — citação suspeita, já registrada na reconciliação (§4), agora
localizada em dispositivo concreto**: `cf88/art-40-p1-iii-ec103-2019`
contém a regra de aposentadoria **voluntária por idade** (62/65 anos), não
de invalidez. `regra-0006` e `0007` citam esse inciso na
`fundamentacao_integral` para fundamentar invalidez; `regra-0008`/`0009`
citam o mesmo inciso "2ª parte" — o texto do inciso III não tem "partes"
distintas de invalidez × não-invalidez, o que agrava a suspeita.
**Nenhuma correção é feita aqui** — cabe à decisão humana (§10 da nota
Q6) determinar a base correta antes de destilar a regra.

**P-4 — decorrência de P-3**: como `art-40-p1-iii-ec103-2019` não trata de
invalidez, a citação "2ª parte" de `regra-0008`/`0009` não tem
correspondência textual verificável dentro do próprio inciso III. Fica
registrada como pendência, não corrigida.

### 3.3 EC 103/2019 + LCE 1.100/2021 (`regra-0019`–`0022`) — hipóteses P5, P6, P7, P9

| Afirmação                                                            | Dispositivo                            | Regra(s)                                         | Hipótese PGE                                      | Vigência formal | Critério temporal de aplicação ao caso                                                                                                                                                                                                 | Aplicabilidade                                                                                                                                                                                                            | Fonte da conclusão                         | Pendência |
| -------------------------------------------------------------------- | -------------------------------------- | ------------------------------------------------ | ------------------------------------------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | --------- |
| "Art. 40, §1º, I da CF, EC 103/2019"                                 | `cf88/art-40-p1-i-ec103-2019`          | 0019, 0020, 0021, 0022                           | P5, P6, P7, P9                                    | 2019-11-13 →    | Regra geral de invalidez/incapacidade em vigor; matéria compatível (ao contrário de P-3)                                                                                                                                               | **confirmada** (quanto à matéria; o ramo etário/ingresso vem das linhas seguintes)                                                                                                                                        | Texto do dispositivo                       | —         |
| "Artigos 25 e 27, inciso I da LCE 1.100/2021" (ramo "antes de 2004") | `lce-1100-2021/art-25`, `art-27-i`     | 0019, 0020, 0021\*, 0022\*                       | P5 (0019/0020); parte de P6/P7/P9 herda a citação | 2021-10-18 →    | **Confirmado pelo próprio texto**: art. 25 — "servidor... que tenha ingressado no serviço público em cargo efetivo **até 31 de dezembro de 2003**"; art. 27, I remete ao art. 7º da EC 41/2003 para quem ingressou até a mesma data    | **confirmada** para 0019/0020 (ramo "até 2003" do título) — **tensão** para 0021/0022, cujo título e `data_adm_apos` dizem "após 31/12/2003" mas a fundamentação cita os mesmos artigos 25/27‑I "antes de 2004" (ver P-5) | Texto do dispositivo (Planalto/Casa Civil) | P-5       |
| "Art. 30, §8º da LCE 1.100/2021" (doença grave/contagiosa/incurável) | `lce-1100-2021/art-30-p8`              | 0019, 0020, 0021 (cláusula 2), 0022 (cláusula 2) | P5 (0019/0020); P6 (cláusula)                     | 2021-10-18 →    | Rol taxativo de doenças (16 incisos) — aplica-se ao segurado acometido **após a filiação ao RPPS-RO**, sem cláusula de ingresso                                                                                                        | **confirmada** (quanto ao rol; a filiação-RPPS não é o mesmo eixo que "ingresso até/após 2003")                                                                                                                           | Texto do dispositivo                       | —         |
| "Art. 30, §§5º e 6º da LCE 1.100/2021" (acidente em serviço)         | `lce-1100-2021/art-30-p5`, `art-30-p6` | 0021 (cláusula 1), 0022 (cláusula 1)             | P7                                                | 2021-10-18 →    | Define "acidente em serviço" e as hipóteses equiparadas (I–IV, com alíneas) — sem cláusula de ingresso                                                                                                                                 | **confirmada**                                                                                                                                                                                                            | Texto do dispositivo                       | —         |
| "Art. 30 da LCE 1.100/2021" (moléstia profissional, sem § citado)    | *(nenhum — ver P-6)*                   | 0021 (cláusula 3), 0022 (cláusula 3)             | P9\*\*                                            | —               | Não verificável: a fundamentação não indica o parágrafo; §6º, III ("doença proveniente de contaminação acidental do segurado no exercício do cargo") é a candidata textual mais próxima, mas **não confirmada** como a base pretendida | **pendente**                                                                                                                                                                                                              | Nenhuma — gap de citação                   | P-6       |

\* 0021/0022 citam os artigos 25/27‑I "antes de 2004" apesar de seu título
e `data_adm_apos: 01/01/2004` dizerem "após 31/12/2003" — ver P-5.
\*\* Mapeamento P9 é o da reconciliação §2 (0021 → P9, "contradição"); a
cláusula "moléstia profissional" de 0021/0022 (uma das três reunidas na
mesma célula com `|`) não corresponde individualmente a nenhuma das 8
hipóteses PGE — é peculiaridade das regras as-is, sem contraparte no to-be.

**P-5 — achado novo desta pesquisa, não presente na reconciliação
original**: `regra-0021`/`0022` têm `data_adm_apos: 01/01/2004` (ingresso
**após** 2003) e nome "Após 31/12/2003", mas sua `fundamentacao_integral`
cita, nas três cláusulas (acidente/doença grave/moléstia profissional), os
mesmos "artigos 25 e 27, inciso I" que `regra-0019`/`0020` usam para o ramo
"antes de 2004" — e o próprio texto do art. 25/27‑I (§3.2 acima) só se
aplica a quem ingressou **até** 31/12/2003. Ou é **erro de citação** em
0021/0022 (deveriam citar o art. 26, que rege proporcional pós-2003, ou uma
base equivalente para o cálculo por média sem paridade — a própria
reconciliação, §4, já assinala uma base repetida da P5 na P6), ou há algo
não capturado nesta pesquisa. **Registrado como pendência, não corrigido**
— cabe à decisão humana confrontar contra a fonte antes de qualquer edição
em `regra-0021`/`0022`.

**P-6 — gap de citação, não gap normativo**: a lei tem texto para
"moléstia profissional equiparada a acidente" (art. 30, §6º, III — "doença
proveniente de contaminação acidental do segurado no exercício do cargo"),
mas a fundamentação de 0021/0022 não cita nenhum parágrafo específico para
essa cláusula ("...e 30, da Lei Complementar..."), então não há uma
afirmação textual verificável para mapear a um dispositivo com confiança.
Fica **pendente**, não resolvida por suposição.

## 4. Requisitos não parametrizáveis nas 27 colunas

A [decisão Q6 (§10, direção A)](q6-causa-incapacidade.md#10-decis%C3%A3o-do-respons%C3%A1vel--dire%C3%A7%C3%A3o-a-classes-de-causa-e-conting%C3%AAncia-b)
já fixou que o catálogo mantém as 27 colunas — a causa da incapacidade é
uma **linha por classe material**, discriminada pela `fundamentacao*`, não
um campo novo. Esta seção não reabre essa decisão; registra, para cada
afirmação que **depende de um fato ou juízo humano não capturável em
nenhuma das 27 colunas**, a evidência exigida e se depende de constatação
do IPERON (o sucessor, no regime LCE 1.100/2021, da "perícia médica oficial
do Estado" da LCE 432/2008 — o nome "IPERON" só aparece a partir da
LCE 1.100/2021; a LCE 432/2008 fala genericamente em "perícia médica
oficial do Estado", sem nomear o instituto).

| Afirmação/requisito                                                   | Parametrizável nas 27 colunas?                                                                                                  | Dispositivo                                                                                                                                         | Regra/PGE                                               | Exige constatação do IPERON?                                                                                                                               | Redação operacional candidata                                                                                                                                                                                         | Evidência necessária                                                                         | Pendência                                                                                                                                                                                                         |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Existência de incapacidade e impossibilidade de readaptação           | Não — nenhuma das 27 colunas registra um fato pericial                                                                          | `lce-432-2008/art-20-p1` / `lce-1100-2021/art-30-p1`                                                                                                | todas (0006–0022, P1–P9)                                | **Sim**, sob LCE 1.100/2021 ("perícia médica oficial indicada pelo IPERON"); sob LCE 432/2008, "perícia médica oficial do Estado" (sem nome de instituto)  | Aplicável quando a incapacidade e a impossibilidade de readaptação houverem sido atestadas por perícia médica oficial (IPERON, sob a LCE 1.100/2021) no processo concessório.                                         | Laudo pericial oficial, no processo administrativo                                           | Q6‑S segue aberta (§9 do dossiê Q6) — este requisito **obtém** o fato, não resolve **onde** ele é registrado                                                                                                      |
| Data em que a incapacidade se caracterizou ("fato gerador")           | Não — `data_direito_ate`/`data_direito_apos` registram elegibilidade estrutural da regra (P5), não o fato gerador do requerente | `lce-432-2008/art-20-p2` / `lce-1100-2021/art-30-p2`                                                                                                | todas                                                   | Sim, mesmo laudo do requisito anterior                                                                                                                     | Aplicável à data certa ou provável fixada no laudo pericial como o momento em que o servidor se tornou incapaz para o cargo, quando essa data for determinável; caso contrário, com justificativa expressa do perito. | Laudo pericial com data certa/provável ou justificativa de sua impossibilidade               | Liga-se a P-1/P-2/P-5 (§3): a lei fixa **como** apurar a data do fato gerador, mas não resolve se é essa data ou a de ingresso que escolhe o regime aplicável                                                     |
| Nexo entre a incapacidade e acidente em serviço                       | Não — `integral`/`tipo_calculo` são o resultado já computado, não o predicado de nexo                                           | `lce-1100-2021/art-30-p5`, `art-30-p6` (sob LCE 1.100/2021); sem equivalente decomposto nesta pesquisa sob LCE 432/2008 (art. 20 §§6º–7º, não lido) | 0006(P1)\*, 0021/0022 (P7)                              | **Sim** — a caracterização do acidente e das hipóteses equiparadas (art. 30, §6º, I–IV) depende de apuração pericial/administrativa, não de autodeclaração | Aplicável quando o nexo entre a incapacidade e o acidente em serviço (ou hipótese equiparada, art. 30 §6º) houver sido constatado pelo IPERON no processo concessório.                                                | Laudo/relatório de nexo técnico + peças do processo administrativo que caracterizem o evento | T‑acidente do dossiê Q6 (§5) — quem caracteriza e com quais critérios segue em aberto                                                                                                                             |
| Classificação como "doença grave, contagiosa ou incurável" catalogada | Não — mesma razão acima; a lista em si é taxonomia (Q6‑T), não linha de catálogo                                                | `lce-432-2008/art-20-p9` (rol pré-2021) / `lce-1100-2021/art-30-p8` (rol 2021, 16 incisos — acrescenta "esclerose múltipla" ao rol anterior)        | 0006(P1)\*, 0008/0009(P4), 0019/0020(P5), 0021/0022(P6) | Sim, quanto à constatação médica de que o segurado é "acometido da doença ou afecção" (LCE 1.100/2021, art. 30, §8º, caput)                                | Aplicável quando o diagnóstico do requerente corresponder a uma das doenças do rol vigente à data de filiação/afecção (art. 30, §8º) e houver sido atestado por perícia oficial.                                      | Laudo médico com diagnóstico enquadrado no rol + data de filiação ao RPPS-RO                 | Rol mudou entre LCE 432/2008 (14 doenças, sem "esclerose múltipla") e LCE 1.100/2021 (16, com "esclerose múltipla") — qual rol vale para cada fato gerador é a mesma pendência de vigência × aplicabilidade do §3 |
| Moléstia profissional (equiparação a acidente)                        | Não                                                                                                                             | candidato: `lce-1100-2021/art-30-p6`, inciso III — **não confirmado**, ver P-6                                                                      | 0021/0022 (cláusula 3, sem hipótese PGE própria)        | Provavelmente sim, mas sem base de citação confirmada (P-6)                                                                                                | Não redigida — depende de resolver P-6 primeiro                                                                                                                                                                       | idem                                                                                         | P-6 (§3.3)                                                                                                                                                                                                        |

\* `regra-0006` (P1) usa a redação da LCE 432/2008 (art. 20, §9º), anterior
à LCE 1.100/2021 — listada aqui para mostrar que o mesmo requisito muda de
base normativa ao longo do tempo, não porque LCE 432/2008 e LCE 1.100/2021
sejam intercambiáveis para o mesmo fato.

**Sobre "redação operacional candidata"**: nenhuma das frases acima é uma
proposta de texto para `fundamentacao*` — são formulações que tornam
explícita, para revisão humana, a condição diferenciadora e sua forma de
constatação (IPERON/perícia oficial), no padrão que a mensagem de missão
desta PR pediu. Nenhuma edita `regra-*.md`.

## 5. Achado colateral: o critério "ingresso" já está no texto da norma para os ramos pós-2003

Merece registro porque **avança**, sem fechar, a pergunta aberta no §3 da
reconciliação ("qual data rege a invalidez — a do fato gerador ou a da
admissão?"): tanto `ec-41-2003/art-6a-ec70-2012` quanto
`lce-1100-2021/art-25`/`art-27-i` **são**, no próprio texto, cláusulas de
ingresso ("que tenha ingressado... até..."). Isso significa que, para quem
ingressou **até** 31/12/2003 — não importa quando —, já existe cobertura
textual explícita no regime vigente hoje (LCE 1.100/2021, arts. 25/27‑I, ou
seu antecessor EC 41/2003 art. 6º-A enquanto vigente). Não resolve se
`regra-0001`/`0002`/`0004` (regimes pré-EC41) ainda "vivem" para alguém —
mas **sugere** que, se o fato gerador de hoje sempre cai sob a redação e o
regime em vigor no momento da concessão (leitura (a) de P-1), então
qualquer servidor cujo fato gerador ocorra agora, tenha ingressado quando
tiver ingressado, já está coberto por `regra-0008`/`0009` (P3/P4, se
ingresso ≤ 2003) ou por `regra-0019`/`0020`/`0021`/`0022` (P5–P9, se
ingresso ≤ 2003 pelo art. 25/27‑I, ou sem cláusula de ingresso nos demais
casos) — tornando 0001/0002/0004 **candidatas a regras historicamente
superadas**, não regras com fato gerador ainda alcançável. **Isto é uma
leitura, não uma conclusão jurídica** — decidir contra fonte primária de
direito previdenciário (doutrina, jurisprudência do TJ/STF sobre direito
adquirido a regime de proventos), não presumir.

## 6. Pendências consolidadas

| ID      | Resumo                                                                                                                                                        | Onde                          | Bloqueia edição de                                            |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------- |
| P-1     | Redações do art. 40 §1 I anteriores a 2003 não têm cláusula própria de ingresso/transição — ingresso × fato gerador em aberto                                 | §3.1                          | 0001, 0002, 0004                                              |
| P-2     | Mesma pendência estrutural para o regime EC41/2003 + LCE 432/2008 ("após 2003" só por exclusão do art. 6º-A)                                                  | §3.2                          | 0006, 0007                                                    |
| P-3     | `regra-0006`/`0007`/`0008`/`0009` citam CF art. 40 §1 III (EC103/2019) para fundamentar invalidez — inciso trata de aposentadoria voluntária por idade        | §3.2 (já em reconciliação §4) | 0006, 0007, 0008, 0009                                        |
| P-4     | Citação "2ª parte" do inciso III (0008/0009) não tem correspondência textual dentro do próprio inciso                                                         | §3.2                          | 0008, 0009                                                    |
| P-5     | **Achado novo**: `regra-0021`/`0022` (título "após 2003") citam art. 25/27‑I da LCE 1.100/2021, cujo próprio texto só alcança ingresso até 2003               | §3.3                          | 0021, 0022                                                    |
| P-6     | "Moléstia profissional" em 0021/0022 não cita parágrafo — candidata textual (art. 30 §6º III) não confirmada                                                  | §3.3, §4                      | 0021, 0022                                                    |
| P-EC146 | `ece-146-2021/art-4` foi conferido via cópia arquivada (Wayback), não fetch ao vivo do SAPL — reconfirmar quando o endpoint deixar de responder 429           | §2                            | qualquer edição que dependa deste dispositivo especificamente |
| Q6‑S    | Obtenção e registro do fato "causa da incapacidade" no Sisprev real seguem abertos (perguntas 1–4 do dossiê Q6, §9) — nenhum achado desta pesquisa os resolve | §4                            | qualquer campo de solicitação (fora do catálogo)              |
| §5      | Leitura de que 0001/0002/0004 podem estar historicamente superadas pelo alcance textual dos regimes atuais — não é conclusão jurídica fechada                 | §5                            | inativação de 0001, 0002, 0004                                |

Nenhuma destas pendências é resolvida nesta PR. O próximo passo (fora de
escopo aqui) é o caderno de propostas por regra, que só deve tratar como
"decidido" o que constar como **confirmada** nas matrizes acima — o
restante permanece pendência a resolver contra fonte, nunca por presunção.
