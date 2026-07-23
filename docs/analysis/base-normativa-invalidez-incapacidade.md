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
  **não** anotado é a redação original. A **cláusula de vigência** de cada
  lei (seu próprio artigo final, "entra em vigor na data de sua
  publicação") e a data/número do Diário Oficial que a publicou também
  foram lidos no próprio corpo da compilação (nunca inferidos).
- **LexML** (`lexml.gov.br`, registro federal de metadados legislativos)
  usado como **segunda fonte independente**, só para confirmar a data de
  publicação de uma emenda a uma lei já lida no texto integral (nunca como
  fonte do texto normativo em si) — caso da LC 672/2012, que alterou o
  art. 45 da LCE 432/2008 (§2).
- **`sapl.al.ro.leg.br`** (ALE-RO/SAPL, o repositório oficial de normas
  da Assembleia Legislativa) é o `fonte:` de `ece-146-2021/art-4` — a URL
  oficial da ALE para a EC 146/2021,
  `normajuridica/2021/9906/emenda_146.pdf`. O **fetch direto** desse
  endpoint segue **inacessível deste ambiente** (HTTP 429 em todas as
  tentativas — 9 no total, em três dias de trabalho distintos, com e sem
  headers de navegador/cookies/referer; corpo de 17 bytes, sem
  `Retry-After`, `content-type` adulterado — assinatura de bloqueio de
  WAF ao IP do ambiente, não falha pontual). O **conteúdo** foi, ainda
  assim, obtido e verificado por dois caminhos independentes que não
  passam por esse fetch direto:
  1. uma cópia arquivada (Wayback Machine) do mesmo URL, com **OCR
     refeito do zero** em duas rodadas de pesquisa distintas, sem
     reaproveitar transcrição anterior — texto idêntico nas duas;
  2. uma **captura nova do Wayback (Save Page Now), feita ao vivo nesta
     rodada** contra o mesmo URL oficial — **byte-idêntica** (mesmo MD5)
     à cópia arquivada mais antiga usada nas rodadas 1 e 2, confirmando
     que o arquivo no próprio SAPL não mudou desde então e que a
     transcrição usada por este bundle corresponde ao conteúdo real do
     `fonte:` citado, não a um mirror desatualizado.
- **`transparencia.al.ro.leg.br`** (Portal da Transparência da ALE-RO, um
  subdomínio distinto do SAPL, **acessível** deste ambiente) hospeda o
  **Diário Oficial Eletrônico da Assembleia Legislativa de Rondônia**
  (DO-e-ALE/RO) — a publicação oficial em si. A **Edição nº 163, Extra,
  de 14/09/2021**
  (`/media/arquivos_diario/Edição_nr_.163_de_14-09-2021_Extra.pdf`)
  publica o texto integral da EMENDA CONSTITUCIONAL Nº 146, DE 9 DE
  SETEMBRO DE 2021 — um PDF com **texto extraível nativamente** (não
  escaneado). Usado **não** como `fonte:` do dispositivo (que cita o
  repositório de normas da ALE, §2), mas como a **evidência independente
  da data de vigência**: confirma que a emenda cujo texto está em
  `ece-146-2021/art-4` foi **publicada** (não apenas promulgada) em
  14/09/2021 — o marco que o art. 13 da própria emenda exige ("entra em
  vigor na data de sua publicação").

Todas as demais fontes (LCE 432/2008, LCE 1.100/2021, CF/88 e emendas
federais) foram lidas diretamente do PDF/HTML oficial nesta sessão —
confiança **HIGH**.

## 2. Dispositivos adicionados nesta PR

| Dispositivo                  | Norma                                             | Vigência formal             | Fonte                            | Confiança |
| ---------------------------- | ------------------------------------------------- | --------------------------- | -------------------------------- | --------- |
| `cf88/art-40-p1-i-ec20-1998` | CF/88, art. 40 §1º I (EC 20/1998)                 | 1998-12-16 → 2003-12-30     | Planalto (`emc20.htm`)           | HIGH      |
| `lce-432-2008/art-17`        | LCE 432/2008, art. 17 (íntegra)                   | **2008-03-13** → 2021-10-18 | Casa Civil/RO — LC432 compilada  | HIGH      |
| `lce-432-2008/art-20-caput`  | LCE 432/2008, art. 20 caput                       | **2008-03-13** → 2021-10-18 | idem                             | HIGH      |
| `lce-432-2008/art-20-p1`     | LCE 432/2008, art. 20 §1º                         | **2008-03-13** → 2021-10-18 | idem                             | HIGH      |
| `lce-432-2008/art-20-p2`     | LCE 432/2008, art. 20 §2º                         | **2008-03-13** → 2021-10-18 | idem                             | HIGH      |
| `lce-432-2008/art-20-p9`     | LCE 432/2008, art. 20 §9º                         | **2008-03-13** → 2021-10-18 | idem                             | HIGH      |
| `lce-432-2008/art-20-p14`    | LCE 432/2008, art. 20 §14                         | **2008-03-13** → 2021-10-18 | idem                             | HIGH      |
| `lce-432-2008/art-45`        | LCE 432/2008, art. 45 (LC 672/2012)               | **2012-08-09** → 2021-10-18 | idem + LexML (data da LC 672)    | HIGH      |
| `lce-432-2008/art-62`        | LCE 432/2008, art. 62 caput                       | **2008-03-13** → 2021-10-18 | idem                             | HIGH      |
| `ece-146-2021/art-4`         | ECE 146/2021, art. 4º (caput + § único)           | **2021-09-14** →¹           | ALE-RO/SAPL, `norma/9906` (§1)   | **HIGH**¹ |
| `lce-1100-2021/art-24`       | LCE 1.100/2021, art. 24 caput (cálculo por média) | 2021-10-18 →                | Casa Civil/RO — LC1100 compilada | HIGH      |
| `lce-1100-2021/art-25`       | LCE 1.100/2021, art. 25 (íntegra)                 | 2021-10-18 →                | idem                             | HIGH      |
| `lce-1100-2021/art-26`       | LCE 1.100/2021, art. 26 (proporcional)            | 2021-10-18 →                | idem                             | HIGH      |
| `lce-1100-2021/art-27-i`     | LCE 1.100/2021, art. 27, I                        | 2021-10-18 →                | idem                             | HIGH      |
| `lce-1100-2021/art-27-ii`    | LCE 1.100/2021, art. 27, II (reajuste RGPS)       | 2021-10-18 →                | idem                             | HIGH      |
| `lce-1100-2021/art-30-caput` | LCE 1.100/2021, art. 30 caput (regra geral)       | 2021-10-18 →                | idem                             | HIGH      |
| `lce-1100-2021/art-30-p1`    | LCE 1.100/2021, art. 30 §1º                       | 2021-10-18 →                | idem                             | HIGH      |
| `lce-1100-2021/art-30-p2`    | LCE 1.100/2021, art. 30 §2º                       | 2021-10-18 →                | idem                             | HIGH      |
| `lce-1100-2021/art-30-p5`    | LCE 1.100/2021, art. 30 §5º                       | 2021-10-18 →                | idem                             | HIGH      |
| `lce-1100-2021/art-30-p6`    | LCE 1.100/2021, art. 30 §6º                       | 2021-10-18 →                | idem                             | HIGH      |
| `lce-1100-2021/art-30-p8`    | LCE 1.100/2021, art. 30 §8º                       | 2021-10-18 →                | idem                             | HIGH      |

¹ **Sobre `ece-146-2021/art-4`**: `fonte:` é a URL oficial da ALE-RO no
repositório SAPL — `normajuridica/2021/9906/emenda_146.pdf` — a mesma
citada pela regra as-is e o repositório canônico de normas da Assembleia
(mesmo padrão dos demais dispositivos deste bundle: cita-se a URL
oficial permanente, não o caminho usado para efetivamente buscar o
conteúdo). O **fetch direto** desse endpoint segue bloqueado neste
ambiente (§1); o **conteúdo**, porém, foi confirmado por dois OCRs
independentes de uma cópia arquivada mais uma captura Wayback nova,
byte-idêntica à mais antiga (§1) — confiança **HIGH** quanto ao texto.

A **data de vigência** é confirmada por uma fonte primária **distinta**:
o art. 13 da própria emenda diz que ela "entra em vigor **na data de sua
publicação**" — e essa data, `14/09/2021`, vem da **Edição nº 163,
Extra, do Diário Oficial Eletrônico da Assembleia Legislativa de
Rondônia (DO-e-ALE/RO)**, em `transparencia.al.ro.leg.br` (§1), que
publica o texto integral da emenda e é, ela mesma, o ato de publicação —
não `09/09/2021`, que é a data de **promulgação**, lida no rodapé do
documento ("ASSEMBLEIA LEGISLATIVA, 9 de setembro de 2021") mas que o
próprio art. 13 não elege como o marco de vigência. O dispositivo carrega
`vigencia_inicio: 2021-09-14`; a pendência P-EC146 das rodadas anteriores
está **fechada**, tanto quanto ao texto (byte-comparação, acima) quanto à
vigência (fonte primária distinta da fonte do texto — §6).

**LCE 432/2008 — vigência confirmada contra a própria lei, não presumida**:
o art. 94 da LCE 432/2008 (lido no mesmo PDF compilado da Casa Civil,
`fonte:` de cada dispositivo acima) diz "Esta Lei Complementar entra em
vigor **na data de sua publicação**", e o cabeçalho do mesmo documento
mostra "LEI COMPLEMENTAR Nº 432, DE 3 DE MARÇO DE 2008" e "DOE Nº 955, DE
13 DE MARÇO DE 2008" — por isso `2008-03-13` (data de publicação, não de
assinatura) para toda provisão em redação original. Para `art-45`
(redação dada pela LC 672/2012), a mesma compilação só registra a data da
lei alteradora ("9/08/2012"); o registro federal de metadados **LexML**
(`lexml.gov.br`, consultado como segunda fonte, nunca como fonte do texto
normativo) confirma, para a LC 672/2012, tanto a data do ato quanto
"Publicação Original: 2012-08-09" — coincidentes, sem o lapso
observado para a ECE 146/2021 acima — por isso `2012-08-09`, HIGH.

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

**P-1 — pendência estrutural, reformulada nesta rodada (não resolvida por
esta PR)**: nem o texto original de 1988 nem a redação EC 20/1998 do
art. 40, §1º, I contêm, elas mesmas, um critério de ingresso ou de
transição — ao contrário do que se vê em `ec-41-2003/art-6a-ec70-2012` e
em `lce-1100-2021/art-25`/`art-27-i` (§3.2–3.3, ambos **explicitamente**
ancorados em "que tenha ingressado... até..."). A formulação anterior desta
pendência tratava isso como uma escolha entre duas leituras simétricas — a
data da concessão *versus* a data de **ingresso** como discriminante de
direito adquirido. **Essa segunda leitura está incorreta e é retirada**: o
STF (RCL 10.823) é explícito em que **não há direito adquirido a regime
previdenciário pela mera vinculação ao serviço público** — a data de
ingresso, isoladamente, não é fundamento de sobrevivência de regime
anterior. A jurisprudência (não a doutrina, que é fonte secundária de
apoio, nunca a evidência primária desta matriz — ver nota abaixo) admite a
sobrevivência de um regime anterior apenas quando:

- **(a)** os requisitos daquele regime já estavam **integralmente
  preenchidos** antes da reforma que o substituiu (situação jurídica
  consumada), ou
- **(b)** existe **regra expressa de transição ou preservação** — como as
  que o próprio corpo desta matriz já cataloga: `ec-41-2003/art-6a-ec70-2012`
  (ingresso ≤ 2003 + invalidez), `lce-1100-2021/art-25`/`art-27-i` (mesmo
  desenho, regime atual) e `ece-146-2021/art-4` (preserva a legislação
  anterior para quem cumprir requisitos até 31/12/2024) — ou
- **(c)** outro fundamento jurídico específico, a apurar contra fonte
  primária caso a caso.

Nenhum dos dois dispositivos desta linha (`art-40-i-original`,
`art-40-p1-i-ec20-1998`) contém, no próprio texto, uma cláusula de
transição nos moldes de **(b)** — o que essa pendência **de fato** deixa em
aberto não é mais "ingresso vs. concessão", e sim: **regra-0001/0002/0004
correspondem a algum caso concreto em que (a) ou (c) se verificam?** Isso
só se decide com evidência de **normas, atos administrativos e
jurisprudência** (fontes primárias) — nunca por presunção, e nunca só por
doutrina, que aqui serve no máximo como apoio interpretativo, não como
prova. **Não decidido nesta PR** — é exatamente a pergunta do §3 da
reconciliação, ainda aberta, agora com o enquadramento jurídico correto.

### 3.2 EC 41/2003 + LCE 432/2008 (`regra-0006`–`0009`) — hipóteses P1–P4

| Afirmação                                                                                                  | Dispositivo                                                               | Regra(s)                   | Hipótese PGE       | Vigência formal                                            | Critério temporal de aplicação ao caso                                                                                                                                                                                                                                                                | Aplicabilidade                                                                                                                                                         | Fonte da conclusão                                                 | Pendência |
| ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | -------------------------- | ------------------ | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | --------- |
| "Art. 40, §1º, I da CF, EC 41/2003" (regra geral, sem exceção de carve-out)                                | `cf88/art-40-p1-i-ec41-2003`                                              | 0006, 0007, 0008\*, 0009\* | P1, P2, P3\*, P4\* | 2003-12-31 → 2019-11-12                                    | Não fixado pelo próprio texto — aplica-se por exclusão a quem **não** está sob o carve-out do art. 6º-A (ingresso ≤ 2003)                                                                                                                                                                             | **pendente** (leitura por exclusão, não afirmação textual)                                                                                                             | Texto do dispositivo + leitura sistemática com `art-6a-ec70-2012`  | P-2       |
| "Artigos 17, 20 caput, 45 e 62 da LCE 432/2008" (proporcional e integral)                                  | `lce-432-2008/art-17`, `art-20-caput`, `art-45`, `art-62`                 | 0006, 0007                 | P1, P2             | 2008-03-13 (art. 45: 2012-08-09) → 2021-10-18              | Regra geral de cálculo/reajuste do regime LCE 432/2008, sem cláusula de ingresso própria — aplicável a quem se aposenta sob esse regime                                                                                                                                                               | **pendente** (mesma leitura sistemática de P-2)                                                                                                                        | Texto do dispositivo                                               | P-2       |
| "Art. 20, §14º e Art. 45 da LC 432/2008" (fundamentação própria de 0007)                                   | `lce-432-2008/art-20-p14`, `art-45`                                       | 0007                       | P2                 | §14: 2008-03-13 → / art.45: 2012-08-09 → 2021-10-18        | idem                                                                                                                                                                                                                                                                                                  | **pendente**                                                                                                                                                           | Texto do dispositivo                                               | —         |
| "Art. 4º da EC Estadual nº 146/2021"                                                                       | `ece-146-2021/art-4`                                                      | 0006, 0007, 0008, 0009     | P1–P4              | **2021-09-14** →                                           | **Confirmado pelo próprio texto**: preserva a legislação vigente **até 2021-09-14** (data de entrada em vigor da emenda, confirmada no DO-e-ALE/RO — §1/§2) para quem cumprir os requisitos **até 2024-12-31**, "assegurada a qualquer tempo" — critério é cumprimento de requisitos, não ingresso    | **confirmada** (quanto ao próprio art. 4º e à sua vigência; não resolve qual legislação "vigente até 2021-09-14" se aplica a cada caso — isso remonta às linhas acima) | Texto: ALE-RO/SAPL (`fonte:`); vigência: DO-e-ALE/RO Ed. 163 Extra | —         |
| "Art. 40, § 1°, inciso III, da CF, EC 103/2019" (0006/0007, integral)                                      | `cf88/art-40-p1-iii-ec103-2019`                                           | 0006, 0007                 | —                  | 2019-11-13 →                                               | N/A — o inciso III (EC 103/2019) trata de aposentadoria **voluntária** por idade, não de invalidez; citação incompatível com a matéria da regra                                                                                                                                                       | **N/A — citação a revisar**, não a "aplicar"                                                                                                                           | Texto do dispositivo, cotejado com a matéria da regra              | P-3       |
| "Art. 6º-A da EC 41/2003, redação EC 70/2012" + "Art. 20 da LCE 432/2008" (0008/0009, proporcional)        | `ec-41-2003/art-6a-ec70-2012`, `lce-432-2008/art-20-caput`                | 0008, 0009                 | P3, P4             | 6º-A: 2012-03-30 → / LC432 art.20: 2008-03-13 → 2021-10-18 | **Confirmado pelo próprio texto do art. 6º-A**: "servidor... que tenha ingressado no serviço público **até a data de publicação desta Emenda Constitucional** [2003-12-31] e que tenha se aposentado ou venha a se aposentar por invalidez permanente..." — ingresso é o critério, explícito na norma | **confirmada**                                                                                                                                                         | Texto do dispositivo (Planalto)                                    | —         |
| "Art. 20, caput, §9º da LCE 432/2008" + "Art. 40, §1º, III, 2ª parte, CF EC103/2019" (0008/0009, integral) | `lce-432-2008/art-20-caput`, `art-20-p9`, `cf88/art-40-p1-iii-ec103-2019` | 0008, 0009                 | P4                 | ver linhas acima                                           | idem (LCE 432/2008); a citação de CF art. 40 §1 III "2ª parte" tem o mesmo problema de matéria da linha P-3, agravado — ver reconciliação §4                                                                                                                                                          | **N/A — citação a revisar**                                                                                                                                            | idem                                                               | P-3, P-4  |

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

#### 3.3.1 O que a fundamentação as-is de 0019–0022 efetivamente cita

| Afirmação                                                            | Dispositivo                            | Regra(s)                                         | Hipótese PGE                                         | Vigência formal | Critério temporal de aplicação ao caso                                                                                                                                                                                                 | Aplicabilidade                                                                                                                                                                                                            | Fonte da conclusão                         | Pendência |
| -------------------------------------------------------------------- | -------------------------------------- | ------------------------------------------------ | ---------------------------------------------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | --------- |
| "Art. 40, §1º, I da CF, EC 103/2019"                                 | `cf88/art-40-p1-i-ec103-2019`          | 0019, 0020, 0021, 0022                           | P5, P6, P7, P9                                       | 2019-11-13 →    | Regra geral de invalidez/incapacidade em vigor; matéria compatível (ao contrário de P-3)                                                                                                                                               | **confirmada** (quanto à matéria; o ramo etário/ingresso vem das linhas seguintes)                                                                                                                                        | Texto do dispositivo                       | —         |
| "Artigos 25 e 27, inciso I da LCE 1.100/2021" (ramo "antes de 2004") | `lce-1100-2021/art-25`, `art-27-i`     | 0019, 0020, 0021\*, 0022\*                       | P5 (0019/0020); citado também por 0021/0022, ver P-5 | 2021-10-18 →    | **Confirmado pelo próprio texto**: art. 25 — "servidor... que tenha ingressado no serviço público em cargo efetivo **até 31 de dezembro de 2003**"; art. 27, I remete ao art. 7º da EC 41/2003 para quem ingressou até a mesma data    | **confirmada** para 0019/0020 (ramo "até 2003" do título) — **tensão** para 0021/0022, cujo título e `data_adm_apos` dizem "após 31/12/2003" mas a fundamentação cita os mesmos artigos 25/27‑I "antes de 2004" (ver P-5) | Texto do dispositivo (Planalto/Casa Civil) | P-5       |
| "Art. 30, §8º da LCE 1.100/2021" (doença grave/contagiosa/incurável) | `lce-1100-2021/art-30-p8`              | 0019, 0020, 0021 (cláusula 2), 0022 (cláusula 2) | P5 (0019/0020); P6 (cláusula)                        | 2021-10-18 →    | Rol taxativo de doenças (16 incisos) — aplica-se ao segurado acometido **após a filiação ao RPPS-RO**, sem cláusula de ingresso                                                                                                        | **confirmada** (quanto ao rol; a filiação-RPPS não é o mesmo eixo que "ingresso até/após 2003")                                                                                                                           | Texto do dispositivo                       | —         |
| "Art. 30, §§5º e 6º da LCE 1.100/2021" (acidente em serviço)         | `lce-1100-2021/art-30-p5`, `art-30-p6` | 0021 (cláusula 1), 0022 (cláusula 1)             | P7                                                   | 2021-10-18 →    | Define "acidente em serviço" e as hipóteses equiparadas (I–IV, com alíneas) — sem cláusula de ingresso                                                                                                                                 | **confirmada**                                                                                                                                                                                                            | Texto do dispositivo                       | —         |
| "Art. 30 da LCE 1.100/2021" (moléstia profissional, sem § citado)    | *(nenhum — ver P-6)*                   | 0021 (cláusula 3), 0022 (cláusula 3)             | P9\*\*                                               | —               | Não verificável: a fundamentação não indica o parágrafo; §6º, III ("doença proveniente de contaminação acidental do segurado no exercício do cargo") é a candidata textual mais próxima, mas **não confirmada** como a base pretendida | **pendente**                                                                                                                                                                                                              | Nenhuma — gap de citação                   | P-6       |

\* 0021/0022 citam os artigos 25/27‑I "antes de 2004" apesar de seu título
e `data_adm_apos: 01/01/2004` dizerem "após 31/12/2003" — ver P-5.
\*\* Mapeamento P9 é o da reconciliação §2 (0021 → P9, "contradição"); a
cláusula "moléstia profissional" de 0021/0022 (uma das três reunidas na
mesma célula com `|`) não corresponde individualmente a nenhuma das 8
hipóteses PGE — é peculiaridade das regras as-is, sem contraparte no to-be.

#### 3.3.2 O que as hipóteses PGE P6/P7/P9 exigem — cobertura completa (bloqueio de completude, corrigido)

A rodada anterior desta matriz cobria só as citações **literais** de
0019–0022, o que deixou de fora quatro dispositivos que sustentam,
no próprio texto da LCE 1.100/2021, o ramo "ingresso após 2003" das
hipóteses PGE P6/P7/P9 — precisamente o ramo que 0021/0022 (título "Após
31/12/2003") deveriam fundamentar e, por P-5, não fundamentam
corretamente. Ficam adicionados aqui para que a matriz cubra **toda** a
fundamentação de P1–P7/P9, não só o que 0021/0022 efetivamente citam:

| Afirmação (base normativa da hipótese PGE, não necessariamente citada pela regra as-is)                           | Dispositivo                  | Hipótese PGE                                                                    | Regra as-is que deveria citar, por design (título/`tipo_calculo`)                      | Vigência formal | Aplicabilidade                                                                                                                                                                                                                                                         | Pendência |
| ----------------------------------------------------------------------------------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| "Art. 24 da LCE 1.100/2021" (cálculo por média, ingresso após 2003)                                               | `lce-1100-2021/art-24`       | P6, P7                                                                          | 0022 (`tipo_calculo: Valor Médio`, `integral: S`, título "Após 31/12/2003")            | 2021-10-18 →    | **confirmada** quanto ao texto; **não citada** pela `fundamentacao_integral` de 0022, que cita 25/27‑I em vez disso (ver P-5)                                                                                                                                          | P-5       |
| "Art. 26 da LCE 1.100/2021" (proporcional, ingresso após 2003)                                                    | `lce-1100-2021/art-26`       | P9                                                                              | 0021 (`tipo_calculo: Proporcionalidade Dias`, `integral: N`, título "Após 31/12/2003") | 2021-10-18 →    | **confirmada** quanto ao texto; **não citada** por 0021 — a reconciliação (§4) já suspeitava que 0021/0022 "deveriam citar o art. 26"; esta pesquisa confirma que o art. 26 **existe** e é, pelo próprio desenho (proporcional, pós-2003), o candidato textual correto | P-5       |
| "Art. 27, II, da LCE 1.100/2021" (reajuste nos termos do RGPS, ingresso após 2003)                                | `lce-1100-2021/art-27-ii`    | P6, P7, P9                                                                      | 0021, 0022 (`paridade: N` — reajuste RGPS é exatamente o que "sem paridade" indica)    | 2021-10-18 →    | **confirmada** quanto ao texto; **não citada** por 0021/0022, que citam 27‑I (paridade) em seu lugar — a mesma tensão de P-5, agora também no reajuste, não só no cálculo                                                                                              | P-5       |
| "Art. 30, caput, da LCE 1.100/2021" (regra geral: proporcional, exceto acidente/moléstia/doença grave → integral) | `lce-1100-2021/art-30-caput` | P5, P6, P7, P9 (todas — é o discriminante geral, análogo ao art. 40 §1 I da CF) | 0019, 0020, 0021, 0022 (nenhuma cita o caput isoladamente; citam direto os §§)         | 2021-10-18 →    | **confirmada** — mesmo desenho do art. 40, §1º, I: regra geral proporcional, com a mesma exceção literal (acidente em serviço/moléstia profissional/doença grave, contagiosa ou incurável) que discrimina integral × proporcional                                      | —         |

**Leitura**: isto **não** é uma correção de `regra-0021`/`0022` (nenhuma
`regra-*.md` é editada nesta PR) — é o registro, na matriz, de que a
fundamentação **correta** para o ramo "após 2003" das hipóteses P6/P7/P9
existe, tem texto verificável, e diverge da fundamentação que 0021/0022
hoje carregam. Isso **fortalece** P-5 (abaixo): já não é só "0021/0022
citam artigos de um ramo temporal errado", é "existe, na mesma lei, um
conjunto de artigos (24, 26, 27‑II) desenhado exatamente para o ramo que
0021/0022 alegam representar, e nenhum dos dois cita esses artigos".

**P-5 — achado novo desta pesquisa, reforçado nesta rodada**:
`regra-0021`/`0022` têm `data_adm_apos: 01/01/2004` (ingresso **após**
2003\) e nome "Após 31/12/2003", mas sua `fundamentacao_integral` cita, nas
três cláusulas (acidente/doença grave/moléstia profissional), os mesmos
"artigos 25 e 27, inciso I" que `regra-0019`/`0020` usam para o ramo "antes
de 2004" — e o próprio texto do art. 25/27‑I (§3.3.1 acima) só se aplica a
quem ingressou **até** 31/12/2003. A rodada anterior já registrava isso
como possível erro de citação, especulando que 0021/0022 "deveriam citar o
art. 26, que rege proporcional pós-2003, ou uma base equivalente para o
cálculo por média sem paridade". Esta rodada **confirma a especulação
contra o texto**: os artigos 24 (cálculo por média, pós-2003), 26
(proporcional, pós-2003) e 27‑II (reajuste RGPS, pós-2003) existem, têm
texto verificável (§3.3.2) e são exatamente o desenho estrutural que
0021/0022 (título "após 2003", `paridade: N`) deveriam citar. Isso não
decide **por que** a citação diverge — pode ser **erro de citação** em
0021/0022, pode ser algo não capturado nesta pesquisa. **Registrado como
pendência, não corrigido** — cabe à decisão humana confrontar contra a
fonte antes de qualquer edição em `regra-0021`/`0022`; os dispositivos
`lce-1100-2021/art-24`, `art-26` e `art-27-ii` já estão disponíveis no
catálogo (§3.3.2) para essa decisão, quando tomada.

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

| Afirmação/requisito                                                   | Parametrizável nas 27 colunas?                                                                                                  | Dispositivo                                                                                                                                         | Regra/PGE                                               | Exige constatação do IPERON?                                                                                                                               | Redação operacional candidata                                                                                                                                                                                                        | Evidência necessária                                                                         | Pendência                                                                                                                                                                                                                                                                                                                                    |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Existência de incapacidade e impossibilidade de readaptação           | Não — nenhuma das 27 colunas registra um fato pericial                                                                          | `lce-432-2008/art-20-p1` / `lce-1100-2021/art-30-p1`                                                                                                | todas (0006–0022, P1–P9)                                | **Sim** — ver nota sobre a redação abaixo                                                                                                                  | Aplicável quando o IPERON houver constatado o requisito com base em perícia médica oficial do Estado (regime LCE 432/2008) ou em perícia médica oficial por ele indicada (regime LCE 1.100/2021), realizada no processo concessório. | Laudo pericial oficial, no processo administrativo                                           | Q6‑S segue aberta (§9 do dossiê Q6) — este requisito **obtém** o fato, não resolve **onde** ele é registrado                                                                                                                                                                                                                                 |
| Data em que a incapacidade se caracterizou ("fato gerador")           | Não — `data_direito_ate`/`data_direito_apos` registram elegibilidade estrutural da regra (P5), não o fato gerador do requerente | `lce-432-2008/art-20-p2` / `lce-1100-2021/art-30-p2`                                                                                                | todas                                                   | Sim, mesmo laudo do requisito anterior                                                                                                                     | Aplicável à data certa ou provável fixada pelo IPERON no laudo pericial como o momento em que o servidor se tornou incapaz para o cargo, quando essa data for determinável; caso contrário, com justificativa expressa do perito.    | Laudo pericial com data certa/provável ou justificativa de sua impossibilidade               | Liga-se a P-1/P-2/P-5 (§3): a lei fixa **como** apurar a data do fato gerador, mas não resolve qual regime rege o caso — ver P-1 reformulado (requisitos preenchidos ou transição expressa, não a mera data de ingresso)                                                                                                                     |
| Nexo entre a incapacidade e acidente em serviço                       | Não — `integral`/`tipo_calculo` são o resultado já computado, não o predicado de nexo                                           | `lce-1100-2021/art-30-p5`, `art-30-p6` (sob LCE 1.100/2021); sem equivalente decomposto nesta pesquisa sob LCE 432/2008 (art. 20 §§6º–7º, não lido) | 0006(P1)\*, 0021/0022 (P7)                              | **Sim** — a caracterização do acidente e das hipóteses equiparadas (art. 30, §6º, I–IV) depende de apuração pericial/administrativa, não de autodeclaração | Aplicável quando o IPERON houver constatado, mediante perícia oficial, o nexo entre a incapacidade e o acidente em serviço (ou hipótese equiparada, art. 30 §6º) no processo concessório.                                            | Laudo/relatório de nexo técnico + peças do processo administrativo que caracterizem o evento | T‑acidente do dossiê Q6 (§5) — quem caracteriza e com quais critérios segue em aberto                                                                                                                                                                                                                                                        |
| Classificação como "doença grave, contagiosa ou incurável" catalogada | Não — mesma razão acima; a lista em si é taxonomia (Q6‑T), não linha de catálogo                                                | `lce-432-2008/art-20-p9` (rol pré-2021) / `lce-1100-2021/art-30-p8` (rol 2021, 16 incisos — acrescenta "esclerose múltipla" ao rol anterior)        | 0006(P1)\*, 0008/0009(P4), 0019/0020(P5), 0021/0022(P6) | Sim, quanto à constatação médica de que o segurado é "acometido da doença ou afecção" (LCE 1.100/2021, art. 30, §8º, caput)                                | Aplicável quando o IPERON, mediante perícia oficial, houver constatado que o requerente está acometido por doença enquadrada no rol juridicamente aplicável ao caso, permanecendo pendente a definição da versão temporal desse rol. | Laudo médico com diagnóstico enquadrado no rol + data de filiação ao RPPS-RO                 | Rol mudou entre LCE 432/2008 (14 doenças, sem "esclerose múltipla") e LCE 1.100/2021 (16, com "esclerose múltipla") — **qual rol** (o vigente à filiação, à afecção, ao requerimento ou à concessão) rege cada fato gerador **não é decidido aqui**, propositalmente, para não antecipar a mesma pergunta de vigência × aplicabilidade do §3 |
| Moléstia profissional (equiparação a acidente)                        | Não                                                                                                                             | candidato: `lce-1100-2021/art-30-p6`, inciso III — **não confirmado**, ver P-6                                                                      | 0021/0022 (cláusula 3, sem hipótese PGE própria)        | Provavelmente sim, mas sem base de citação confirmada (P-6)                                                                                                | Não redigida — depende de resolver P-6 primeiro                                                                                                                                                                                      | idem                                                                                         | P-6 (§3.3)                                                                                                                                                                                                                                                                                                                                   |

\* `regra-0006` (P1) usa a redação da LCE 432/2008 (art. 20, §9º), anterior
à LCE 1.100/2021 — listada aqui para mostrar que o mesmo requisito muda de
base normativa ao longo do tempo, não porque LCE 432/2008 e LCE 1.100/2021
sejam intercambiáveis para o mesmo fato.

**Sobre "redação operacional candidata"**: nenhuma das frases acima é uma
proposta de texto para `fundamentacao*` — são formulações que tornam
explícita, para revisão humana, a condição diferenciadora e sua forma de
constatação (IPERON/perícia oficial), no padrão que a mensagem de missão
desta PR pediu. Nenhuma edita `regra-*.md`.

## 5. Achado colateral: o critério de transição já está no texto da norma para os ramos pós-2003 — reescrito nesta rodada

A versão anterior desta seção derivava de uma leitura "(a) vs. (b)"
simétrica entre data de concessão e data de ingresso que a §3.1 (P-1),
revisada nesta rodada, já descarta como enquadramento jurídico incorreto
(não há direito adquirido a regime previdenciário pela mera vinculação ao
serviço público — STF, RCL 10.823). Este achado é reescrito para se apoiar
só no que o texto normativo efetivamente diz.

O que os dispositivos mostram, sem inferência: tanto
`ec-41-2003/art-6a-ec70-2012` quanto `lce-1100-2021/art-25`/`art-27-i` **são**,
no próprio texto, regras expressas de transição/preservação — a hipótese
**(b)** do P-1 reformulado (§3.1) — para quem "tenha ingressado... até..."
31/12/2003. Isso é uma cláusula de transição textual, não uma tese de
direito adquirido por ingresso: a norma vigente hoje (LCE 1.100/2021, arts.
25/27‑I, e seu antecessor EC 41/2003 art. 6º-A enquanto vigente)
**preserva, ela mesma, por norma expressa**, o cálculo/paridade do regime
anterior para esse grupo. Para quem ingressou **após** 31/12/2003, a mesma
lei atual já rege diretamente (LC 1.100/2021, arts. 24/26/27‑II/30 — §3.3.2).

O que isso **não** prova, e a versão anterior tratava como consequência
automática: que `regra-0001`/`0002`/`0004` (regimes pré-EC41/2003) estão
"superadas". Sob o enquadramento jurídico correto (§3.1, jurisprudência do
STF), a sobrevivência de um regime sem cláusula de transição expressa
depende de **requisitos já integralmente preenchidos antes da reforma** —
uma situação jurídica individual e histórica (quem já tinha os requisitos
completos antes de 1998/2003), não um desenho de regra que segue
produzindo novos casos elegíveis. Como nem o texto original de 1988 nem a
redação EC 20/1998 contêm cláusula de transição própria (§3.1), a leitura
mais consistente com essa jurisprudência é que 0001/0002/0004 só
alcançariam, hoje, um
servidor cujos requisitos já estivessem completos **antes** da respectiva
reforma — um universo que só se confirma com evidência concreta (registros
funcionais, atos, processos), nunca por presunção da data de ingresso.
**Isto continua sendo uma leitura, não uma conclusão jurídica fechada** —
decidir contra fonte primária (normas, atos, jurisprudência do TJ/STF sobre
situação jurídica consumada em matéria previdenciária; doutrina apenas como
apoio interpretativo, nunca como evidência primária), não presumir.

## 6. Pendências consolidadas

| ID      | Resumo                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Onde                          | Bloqueia edição de                               |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------ |
| P-1     | Redações do art. 40 §1 I anteriores a 2003 não têm cláusula própria de transição; reformulado nesta rodada — **não** é "ingresso vs. concessão" (não há direito adquirido pela mera vinculação ao serviço público, STF RCL 10.823), e sim se 0001/0002/0004 correspondem a requisitos já preenchidos antes da reforma ou a outra transição expressa, a apurar contra fonte primária                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | §3.1                          | 0001, 0002, 0004                                 |
| P-2     | Mesma pendência estrutural para o regime EC41/2003 + LCE 432/2008 ("após 2003" só por exclusão do art. 6º-A)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | §3.2                          | 0006, 0007                                       |
| P-3     | `regra-0006`/`0007`/`0008`/`0009` citam CF art. 40 §1 III (EC103/2019) para fundamentar invalidez — inciso trata de aposentadoria voluntária por idade                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | §3.2 (já em reconciliação §4) | 0006, 0007, 0008, 0009                           |
| P-4     | Citação "2ª parte" do inciso III (0008/0009) não tem correspondência textual dentro do próprio inciso                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | §3.2                          | 0008, 0009                                       |
| P-5     | `regra-0021`/`0022` (título "após 2003") citam art. 25/27‑I da LCE 1.100/2021, cujo próprio texto só alcança ingresso até 2003; **reforçado nesta rodada** — os arts. 24, 26 e 27‑II (§3.3.2), desenhados exatamente para o ramo "após 2003", existem e não são citados por 0021/0022                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | §3.3                          | 0021, 0022                                       |
| P-6     | "Moléstia profissional" em 0021/0022 não cita parágrafo — candidata textual (art. 30 §6º III) não confirmada                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | §3.3, §4                      | 0021, 0022                                       |
| P-EC146 | **Fechada.** `ece-146-2021/art-4`: `fonte:` é a URL oficial da ALE-RO no repositório SAPL (`normajuridica/2021/9906/emenda_146.pdf`); confiança HIGH quanto ao **texto** por dois OCRs independentes de uma cópia arquivada mais uma captura Wayback nova desta rodada, byte-idêntica (mesmo MD5) à mais antiga — confirma que o conteúdo do próprio `fonte:` não mudou. `vigencia_inicio` corrigido de 2021-09-09 (promulgação) para 2021-09-14 (publicação — o marco que o art. 13 da própria emenda exige), confirmado por fonte primária distinta e independente: a Edição nº 163, Extra, do Diário Oficial Eletrônico da Assembleia Legislativa de Rondônia (DO-e-ALE/RO). O endpoint ao vivo do SAPL segue respondendo HTTP 429 neste ambiente (9 tentativas, 3 dias de trabalho distintos) — não impede citar sua URL como `fonte:` canônica, só impede buscar o conteúdo por ela diretamente daqui. | §1, §2                        | nenhuma — pendência resolvida                    |
| Q6‑S    | Obtenção e registro do fato "causa da incapacidade" no Sisprev real seguem abertos (perguntas 1–4 do dossiê Q6, §9) — nenhum achado desta pesquisa os resolve                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | §4                            | qualquer campo de solicitação (fora do catálogo) |
| §5      | Leitura de que 0001/0002/0004 podem estar historicamente superadas — reformulada nesta rodada sob o enquadramento jurídico correto (requisitos preenchidos ou transição expressa, não a mera data de ingresso); continua não sendo conclusão jurídica fechada                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | §5                            | inativação de 0001, 0002, 0004                   |

Nenhuma destas pendências é resolvida nesta PR. O próximo passo (fora de
escopo aqui) é o caderno de propostas por regra, que só deve tratar como
"decidido" o que constar como **confirmada** nas matrizes acima — o
restante permanece pendência a resolver contra fonte, nunca por presunção.
