# Reconferência dos itens `[R]` do bloco 4, do item 5.4 e do item 1.2

> **Nota:** Relatório gerado por IA como apoio à decisão. **Não é artefato
> oficial**, não edita nenhuma `regra-*.md`, nenhum `achado-*.md`, nenhum
> dispositivo, não altera schema, dados derivados
> (`data/regras-sisprev.csv`), motor ou `site/`. Reconfere, contra o
> frontmatter das regras e contra o texto dos dispositivos, seis itens que
> [`achados-candidatos-da-conferencia.md`](achados-candidatos-da-conferencia.md)
> marca como **[R]** — vindos do relatório de grupo, não reconferidos. Toda
> conclusão sobre citação ou sobre valor gravado continua sendo ato humano,
> em achado próprio.

## O método, e os limites de fonte de hoje

Para cada item: (1) fixar **quais regras** ele de fato alcança, nominalmente,
porque a lista consolidada diz "doze" e "dezesseis" sem enumerar; (2) ler o
frontmatter dessas regras; (3) ler o corpo dos dispositivos que elas vinculam,
em `okf/dispositivos/`; (4) quando o item afirma "critério X decide e nenhuma
provisão citada o funda", conferir **as duas pontas** — que o critério está
mesmo gravado (ou que mesmo não tem coluna), e que nenhum dispositivo citado o
estabelece.

Três limites de fonte, todos verificados nesta sessão e todos relevantes ao
que segue:

- **Planalto fora do ar.** `curl` a
  `https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp51.htm` devolve HTTP
  `000` (timeout). Logo a **LC 51/1985** e a **LC 152/2015** — cujas únicas
  `fontes` autoradas apontam para o Planalto — não puderam ser reconferidas
  contra a fonte oficial hoje. O que se lê delas abaixo é a transcrição já
  autorada em `okf/dispositivos/`, e está dito onde isso importa.
- **A ECE 146/2021 é PDF escaneado sem camada de texto.**
  `fontes-oficiais/arquivos/sapl-emenda_146.pdf` tem 10 páginas e
  `pdftotext` extrai **10 bytes**. Nenhuma afirmação abaixo sobre o texto da
  ECE 146/2021 vem da fonte oficial: vem da transcrição autorada no corpus.
- **A LCE 1.100/2021 e a LCE 432/2008, ao contrário, são conferíveis
  localmente** — `ditel-LC1100---COMPILAÇÃO.txt` e
  `ditel-LC432-COMPILADA-REVOGADA.txt` são extrações com texto das mesmas
  publicações que os dispositivos citam em `fontes`. É daí que sai o achado
  transversal da §7, e é por isso que o item 4.4 sai **mais forte** do que
  entrou.

`uv run python scripts/validar_regras.py` → **No violations found** nesta
árvore.

## Resumo dos vereditos

| item    | afirmação da lista consolidada                                               | veredito                                | alcance afirmado                                     | alcance real, conferido                                            |
| ------- | ---------------------------------------------------------------------------- | --------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------ |
| **4.1** | a idade-limite não é campo de regra nenhuma na compulsória                   | **confirma** — e mais forte do que dito | "nenhuma das seis regras do tipo"                    | 6 regras: 0023, 0025, 0027, 0030, 0031, 0032                       |
| **4.2** | `apos_especial: S` sem fundamento em campo nenhum                            | **confirma em parte, refuta em parte**  | 0099/0100 + "três dos quatro subgrupos do reg. novo" | 3 regras: **0092**, 0099, 0100. Nenhum subgrupo do reg. novo entra |
| **4.3** | `sexo` não é fundado por provisão transcrita nenhuma nas doze de transição   | **refuta como universal**               | "as doze"                                            | 10 de 12 — 0103/0104 **têm** o critério fundado                    |
| **4.4** | o art. 34 diz "para ambos os sexos", e quatro regras se dividem por sexo     | **confirma**, e a fonte oficial reforça | "quatro regras"                                      | 4 regras: 0080, 0081, 0082, 0083                                   |
| **5.4** | dezesseis regras da ECE 146/2021 não citam o dispositivo dos seus requisitos | **confirma o fato, refuta a contagem**  | "dezesseis"                                          | **19** (0043–0058, 0068–0070); + 13 do art. 7º em grau menor       |
| **1.2** | `regra-0084`: `sexo: AMBOS` vinculando só a alínea feminina                  | **confirma**                            | 1 regra                                              | `regra-0084` — sem detector e sem achado, hoje                     |

______________________________________________________________________

## 1. Item 4.1 — a idade-limite não é campo de regra nenhuma na compulsória

**Veredito: confirma**, nas duas pontas, e a formulação segura é mais forte do
que a da lista.

### 1.1 As regras alcançadas

Conferido o campo `tipo_de_beneficio` das 112, `APOSENTADORIA COMPULSÓRIA`
tem exatamente **seis** ocorrências:

`regra-0023`, `regra-0025`, `regra-0027`, `regra-0030`, `regra-0031`,
`regra-0032`.

(É o mesmo recorte que a
[conferência da compulsória](conferencia-criterio-dispositivo-compulsoria-idade.md)
já havia corrigido; confirmado aqui de forma independente.)

### 1.2 A ponta do schema — conferida contra as colunas reais

`okf/regras-sisprev/regras-sisprev.md`, campo `columns`, lista as 27 colunas:

`NOME`, `TIPO DE BENEFICIO`, `ATUALMENTE NO SISTEMA`, `CICLO DE VALIDAÇÃO`,
`VALIDADO PGE`, `VALIDADO PRESIDENCIA`, `SIMULAVEL`, `TIPO`, `APOS_ESPECIAL`,
`TIPO_REMUN`, `PARIDADE`, `TabelaPontuacao`, `Requisitos da IN Nº 5/2020`,
`Relatório p/ Reserva Remunerada por Idade ex-officio`,
`ADICIONAL_INATIVIDADE`, `DATA_ADM_ATE`, `DATA_ADM_APOS`, `DATA_DIREITO_ATE`,
`DATA_DIREITO_APOS`, `FUNDAMENTACAO_PROPORCIONAL`, `VISIVEL DTC PROPORCIONAL`,
`FUNDAMENTACAO_INTEGRAL`, `VISIVEL DTC INTEGRAL`, `SEXO`, `INTEGRAL`,
`TIPO_CALCULO`, `FUNDAMENTACAO`.

**Nenhuma é idade.** Nem idade-limite, nem idade mínima, nem faixa etária.

Conferido também pelo outro lado, sobre o bundle inteiro: a união das chaves
de frontmatter das 112 regras tem **31** chaves — as 27 colunas mais `type`,
`id`, `row_index` e `dispositivos`, que são identidade e anotação de
auditoria. Não há chave extra que carregue idade em regra nenhuma.

**Consequência de escopo, e ela é o que torna o item um achado e não um
conserto:** criar coluna é alterar o Sisprev, fora do escopo declarado em
[`docs/spec/regra.md`](../spec/regra.md) ("O escopo é parametrização, não
mudança do sistema"). Se a idade-limite tiver de virar parâmetro, isso é
**pedido ao IPERON**, e é assim que precisa ser registrado.

### 1.3 A outra ponta — a idade está no texto legal, e é decisiva

Todos os textos abaixo foram lidos em `okf/dispositivos/`, verbatim:

| dispositivo                                     | idade que o texto fixa                                                                                                            | vinculado por          |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| `cf88/art-40-inc-ii/original`                   | "compulsoriamente, aos **setenta** anos de idade, com proventos proporcionais ao tempo de serviço"                                | 0023                   |
| `cf88/art-40-par-1-inc-ii/ec-20-1998`           | "compulsoriamente, aos **setenta** anos de idade, com proventos proporcionais ao tempo de contribuição"                           | *(nenhuma — ver §1.5)* |
| `cf88/art-40-par-1-inc-ii/ec-88-2015`           | "compulsoriamente, [...] aos **70** (setenta) anos de idade, **ou aos 75** (setenta e cinco) [...], na forma de lei complementar" | 0027, 0030, 0031, 0032 |
| `lce-432-2008/art-21-par-1` (caput no contexto) | "O servidor será aposentado compulsoriamente, aos **70** (setenta) anos de idade"                                                 | 0027, 0032             |
| `lc-152-2015/art-2`                             | "Serão aposentados compulsoriamente [...] aos **75** (setenta e cinco) anos de idade:"                                            | 0030, 0031             |
| `lce-1100-2021/art-31`                          | "O servidor será aposentado, compulsoriamente, aos **75** (setenta e cinco) anos de idade"                                        | 0030, 0031             |

O art. 21, § 1º da LCE 432/2008 usa o termo literal: "a partir do dia imediato
àquele em que o servidor atingir a **idade-limite** de permanência no serviço
ativo". O critério existe na lei, com nome próprio.

### 1.4 O que a reconferência acrescenta ao que a lista dizia

A conferência de origem dizia: "Distinguir 70 de 75 exige ler o
`fundamentacao_proporcional` — campo de texto livre". **Isso é generoso
demais.** Conferido caractere a caractere, **nenhum dos seis documentos
contém o número 70 nem o número 75, em campo nenhum** — nem em coluna, nem no
`nome`, nem no texto da fundamentação. Os campos de fundamentação nomeiam
*normas*, nunca a idade:

> `regra-0030`/`0031`, `fundamentacao_proporcional`: "Aposentadoria
> compulsória com proventos proporcionais ao tempo de contribuição, com base
> na média aritmética simples, e sem paridade, com base no artigo 40, § 1º,
> II, da Constituição Federal, com redação dada pela Emenda Constitucional nº
> 88/2015, artigo 2º da Lei Complementar nº 152/2015, artigos 24, 26, 27,
> inciso II, e 31 da Lei Complementar Estadual nº 1.100/2021."

Ou seja: para saber se uma regra compulsória do catálogo aplica 70 ou 75 anos
é preciso **resolver a citação e abrir a norma**. Ler o registro inteiro não
basta.

E o registro, sozinho, é ambíguo em pelo menos um ponto que já está
documentado: a `regra-0032` cita a EC 88/2015 (que oferece "70 **ou** 75, na
forma de lei complementar") e o art. 21 da LCE 432/2008 (que fixa 70),
enquanto `0030`/`0031` citam a LC 152/2015 e o art. 31 da LCE 1.100/2021
(ambos 75) — com janelas de direito que se sobrepõem. A sobreposição já está
registrada no §2 daquela conferência; o que esta seção acrescenta é que
**nenhum campo do catálogo permite decidir qual idade cada uma pretende**.

### 1.5 Uma correção de enquadramento, e uma pendência que ficou

**O item 4.1 está no bloco errado.** O bloco 4 se chama "Critério decisivo
**sem dispositivo**", e aqui o dispositivo existe, está citado e (salvo a
0025\) está vinculado — o que falta é **coluna**. É a mesma forma da Q6 do 4.5
(causa da incapacidade), e a forma oposta à dos itens 4.2/4.3/4.4, em que o
critério **está gravado** e nenhuma provisão o funda. Duas famílias
diferentes de defeito convivem hoje sob um título só, e o achado autorado
deveria separá-las.

**Pendência conferida de passagem:** `regra-0025` é a única das seis com
`dispositivos:` vazio. Sua `fundamentacao_proporcional` diz "Art 40, §1º, II,
da CF com redação da EC 20/98", e essa redação **agora está autorada**
(`cf88/art-40-par-1-inc-ii/ec-20-1998`, `vigencia_inicio: 1998-12-16`,
`vigencia_fim: 2003-12-30`). A pendência de transcrição que travava o vínculo
fechou; o vínculo continua não declarado.

______________________________________________________________________

## 2. Item 4.2 — `apos_especial: S` sem fundamento em campo nenhum

**Veredito: confirma a primeira metade, refuta a segunda** — e o alcance real
é uma regra *maior* na primeira e *zero* na segunda.

### 2.1 O que o item afirma

> Em `0099`/`0100` (transição) e em três dos quatro subgrupos especiais do
> regime novo, o que **define** a especialidade não tem dispositivo citado.

### 2.2 Primeira metade — 0099/0100: **confirmada**, e o padrão alcança uma terceira regra

`regra-0097` e `regra-0099` divergem, na chave material do P2, em **um único
campo**: `apos_especial` (`N` vs `S`). O mesmo para `0098`/`0100`. A
`fundamentacao_integral` das quatro é **a mesma string, byte a byte**
(sha256 `02a9e757977d…`, 489 caracteres), e ela é esta:

> Aposentadoria voluntária por idade e tempo de contribuição, com proventos
> integrais (Média aritmética das contribuições), com Aplicação do redutor de
> idade (se houver antecipação) e sem paridade, com base no artigo 40, § 1°,
> inciso III, segunda parte, da Constituição Federal, com a redação dada pela
> Emenda Constitucional nº 103/2019, artigo 4º da Emenda à Constituição
> Estadual nº 146/2021 e artigo 2º da Emenda Constitucional nº 41/2003 -
> fundamento - regra de transição - EC 41/03 - CF

Nem "professor", nem "magistério", nem redução alguma. E os três dispositivos
que as quatro vinculam — `cf88/art-40-par-1-inc-iii/ec-103-2019`,
`ec-41-2003/art-2/original`, `ece-146-2021/art-4/original` — tampouco. O
`ec-41-2003/art-2/original` está transcrito **só até o caput** ("quando o
servidor, cumulativamente:"), então o que estiver nos seus parágrafos não é
conferível aqui; a afirmação segura é a estreita: **nada do que 0099/0100
citam ou vinculam funda o `apos_especial: S`**.

**O padrão alcança uma terceira regra que o item não menciona.**
Uma triagem mecânica sobre as 55 regras com `apos_especial: S` — procurando
qualquer palavra de especialidade (`professor`, `magistério`, `deficiên`,
`policial`, `nociv`, `exposiç`, `penal`, `socioeducativo`, `especial`) nos
três campos de fundamentação — devolve **seis** regras sem nenhuma. Conferidas
uma a uma:

| regra            | tem palavra de especialidade nos **dispositivos vinculados**?      | veredito                              |
| ---------------- | ------------------------------------------------------------------ | ------------------------------------- |
| `regra-0084`     | sim — LC 51/1985 é o estatuto policial, vinculado e citado         | fundado por citação (ver §6)          |
| `regra-0088`     | sim — `cf88/art-40-inc-iii-al-b/original` é a alínea do magistério | fundado por citação                   |
| `regra-0090`     | sim — `cf88/art-40-par-5/ec-20-1998`, redução de cinco anos        | fundado por citação                   |
| **`regra-0092`** | **não**                                                            | **`apos_especial: S` sem fundamento** |
| **`regra-0099`** | **não**                                                            | **`apos_especial: S` sem fundamento** |
| **`regra-0100`** | **não**                                                            | **`apos_especial: S` sem fundamento** |

`regra-0092` é o mesmo defeito com outra norma: seu `nome` diz
"(Magistério)", sua `fundamentacao_integral` é **byte a byte idêntica** à da
`regra-0091` (sha256 `ada6a9ea33f6…`) e não menciona magistério, e os três
dispositivos vinculados são os mesmos das duas. O caso já está descrito no
§5.13 da
[conferência voluntária CF/88](conferencia-criterio-dispositivo-voluntaria-cf88.md),
mas **não foi promovido ao item 4.2 da lista consolidada** — e é exatamente o
mesmo achado.

**Alcance real do item 4.2, primeira metade: `regra-0092`, `regra-0099`,
`regra-0100`.**

### 2.3 Segunda metade — "três dos quatro subgrupos especiais do regime novo": **refutada**

Os quatro subgrupos, com o dispositivo que cada um cita **e** vincula, e o
texto verbatim que o define:

| subgrupo        | regras                             | dispositivo da especialidade   | o que o texto diz                                                                                                                                                                                    |
| --------------- | ---------------------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| magistério      | 0041, 0042, 0095, 0096, 0107, 0108 | `lce-1100-2021/art-33`         | "O **professor** que comprove tempo de efetivo exercício, **exclusivamente**, nas funções de magistério [...] terá o requisito de idade reduzido em 5 (cinco) anos."                                 |
| deficiência     | 0059–0064                          | `lce-1100-2021/art-35`         | "O servidor público **com deficiência**, previamente submetido à **avaliação biopsicossocial** realizada por equipe multiprofissional e interdisciplinar, fará jus à aposentadoria voluntária [...]" |
| agentes nocivos | 0065, 0066, 0067, 0071             | `lce-1100-2021/art-41-inc-iii` | "[...] efetiva **exposição a agentes nocivos** químicos, físicos e biológicos [...] **86** (oitenta e seis) pontos e **25** (vinte e cinco) anos de efetiva exposição."                              |
| policial        | 0080, 0081, 0082, 0083             | `lce-1100-2021/art-34`         | "O **policial civil**, o policial legislativo e o ocupante de cargo de policial penal ou de agente de segurança socioeducativo serão aposentados voluntariamente [...]"                              |

Em **quatro de quatro**, o critério que *define* a especialidade tem
dispositivo citado e vinculado. Zero subgrupos entram no item.

**De onde veio o "três".** A §5.3 da
[conferência do regime novo](conferencia-criterio-dispositivo-voluntaria-regime-novo.md)
tem o título "Em três dos quatro subgrupos especiais [...] não tem
dispositivo", mas a **tabela logo abaixo dele marca dois `❌`** (deficiência e
policial), não três — e esses dois `❌` são sobre outra coisa: sobre o
**critério concreto** (o grau da deficiência; os requisitos de idade e tempo
do policial), não sobre o critério que define a especialidade. O título
diverge da própria tabela, e a lista consolidada herdou o título.

**E os dois `❌` restantes também não são "sem dispositivo citado".** Os
documentos `lce-1100-2021/art-34/original` e `lce-1100-2021/art-35/original`
endereçam o **artigo inteiro** (`componentes: [artigo 34]`, `[artigo 35]`) —
os incisos estão dentro do dispositivo vinculado; o que falta é a
**transcrição**, e ela é destravável hoje (§7). A formulação correta é:
*em dois dos quatro subgrupos, o critério concreto da especialidade está num
dispositivo vinculado cuja transcrição no corpus para no caput.* Isso é fila
`TRANSCREVER`, não achado de fundamentação.

______________________________________________________________________

## 3. Item 4.3 — `sexo` não é fundado por provisão transcrita nenhuma nas doze de transição

**Veredito: refuta como universal; confirma para 10 das 12.** A segunda frase
do item (sobre `0030`/`0031`) **confirma**.

### 3.1 As doze regras

Enumeradas contra o `dispositivos:` e o `fundamentacao_integral` de cada uma
(as três famílias da
[conferência de transição](conferencia-criterio-dispositivo-transicao-ec41-ec47.md)):

| família                  | regras                         |
| ------------------------ | ------------------------------ |
| **A** — art. 2º da EC 41 | 0097, 0098, 0099, 0100         |
| **B** — art. 6º da EC 41 | 0101, 0102, **0103**, **0104** |
| **C** — art. 3º da EC 47 | 0085, 0086, 0105, 0106         |

Nas doze, `sexo` é o **único** campo material que separa cada gêmea
(verificado mecanicamente contra a chave do `P2_IGUALDADE_MATERIAL_ATIVA`:
`0085`×`0086`, `0097`×`0098`, `0101`×`0102`, `0103`×`0104`, `0105`×`0106`
divergem só em `sexo`; `0097`×`0099` e `0098`×`0100` divergem só em
`apos_especial`).

### 3.2 O que refuta a afirmação: `regra-0103` e `regra-0104`

As duas vinculam `lce-432-2008/art-46/original` e o citam nominalmente
("artigos 24, 46 e 63 da Lei Complementar nº 432/2008"). O texto transcrito
desse artigo, **conferido também contra a publicação oficial compilada**
(`ditel-LC432-COMPILADA-REVOGADA.txt`, linhas 591–592, idêntico ao corpus):

> I – 60 (sessenta) anos de idade, **se homem**, e 55 (cinqüenta e cinco)
> anos de idade, **se mulher**;
>
> II - 35 (trinta e cinco) anos de contribuição, **se homem**, e 30 (trinta)
> anos de contribuição, **se mulher**;

É provisão **transcrita, vinculada e citada** que parametriza requisitos por
sexo. Logo a afirmação "nas doze, `sexo` não é fundado por provisão
transcrita nenhuma" é **falsa para 0103 e 0104**.

A conferência de origem já dizia isso, aliás, com precisão — "das doze
regras, só duas têm o critério `sexo` fundado por um dispositivo que elas
próprias vinculam". Foi a **consolidação** que apagou a exceção ao encurtar o
título.

### 3.3 O que confirma, para as outras dez

Percorridas as provisões vinculadas pelas dez restantes:

| dispositivo                             | vinculado por          | distingue por sexo?                                                                                                                                                                     |
| --------------------------------------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cf88/art-40-par-1-inc-iii/ec-103-2019` | as doze                | **só na primeira parte** — "aos 62 [...] se mulher, e aos 65 [...] se homem" no âmbito da **União**; a segunda parte, que é a citada, delega a idade estadual sem dizer nada sobre sexo |
| `ec-41-2003/art-2/original`             | 0097–0100              | não — transcrito só até "quando o servidor, cumulativamente:"                                                                                                                           |
| `ec-41-2003/art-6/original`             | 0101–0104              | não — transcrito só até "vier a preencher, cumulativamente, as seguintes condições:"                                                                                                    |
| `ec-47-2005/art-3/original`             | 0085, 0086, 0105, 0106 | não — transcrito só até "desde que preencha, cumulativamente, as seguintes condições:"                                                                                                  |
| `ece-146-2021/art-4/original`           | as doze                | não                                                                                                                                                                                     |
| `lce-432-2008/art-24/original`          | 0103, 0104             | não                                                                                                                                                                                     |
| `lce-432-2008/art-63/original`          | 0103, 0104             | não                                                                                                                                                                                     |

**Uma ressalva de precisão que a formulação larga apaga.** O documento
`cf88/art-40-par-1-inc-iii/ec-103-2019`, vinculado nas doze, **contém** uma
distinção por sexo no seu texto (62/65 na União). Dizer "nenhuma provisão
transcrita distingue por sexo" é literalmente falso a nível de documento. O
que é verdade — e é o que deve entrar no achado — é que **a parte que as doze
citam ("segunda parte") não distingue, e a que distingue não alcança o RPPS
estadual.**

**Alcance real do item 4.3: 0085, 0086, 0097, 0098, 0099, 0100, 0101, 0102,
0105, 0106 — dez das doze.**

### 3.4 A segunda frase: `0030`/`0031` — **confirmada**

> E em `0030`/`0031` o `sexo` M/F é hoje a única coisa que impede o `P2` de
> agrupá-las — sem dispositivo que o justifique.

As duas metades checam:

- **Mecânica.** Aplicada a chave material do `P2_IGUALDADE_MATERIAL_ATIVA`
  (frontmatter menos identidade, `nome`, `dispositivos` e campos
  administrativos), `regra-0030` e `regra-0031` divergem em **exatamente um
  campo: `sexo`**. O detector as reporta hoje só em `P1_NOME_REPETIDO` — elas
  têm o mesmo `nome`.
- **Jurídica.** Nenhuma das seis provisões que as duas vinculam distingue por
  sexo: `cf88/art-40-par-1-inc-ii/ec-88-2015` ("aos 70 [...] ou aos 75 [...]
  anos de idade"), `lc-152-2015/art-2` ("aos 75 [...] anos de idade:"),
  `lce-1100-2021/art-24`, `art-26`, `art-27-inc-ii` e `art-31` ("aos 75
  [...] anos de idade"). Nenhuma delas contém "homem", "mulher" ou "sexo".

*Observação lateral, fora do que a regra cita, e por isso marcada como tal:*
o `art-26` (proporcionalidade) manda usar como denominador "o tempo necessário
à respectiva aposentadoria voluntária por idade e tempo de contribuição", e o
art. 32, II da mesma lei — lido na publicação oficial compilada, **não
transcrito no corpus e não vinculado por 0030/0031** — fixa "25 (vinte e
cinco) anos de contribuição" sem distinguir sexo. Se isso se confirmar como a
leitura correta, nem o cálculo varia por sexo. Não é conclusão: nenhuma das
duas regras cita o art. 32.

**Duas coisas que não se concluem daqui.** Que o `sexo` esteja errado — a
decisão é humana e sobre campo deployable. E o que o motor faz: `simulavel: S`
nas duas, e o motor não lê fundamentação; o que se afirma é sobre o
**registro**, não sobre o comportamento.

______________________________________________________________________

## 4. Item 4.4 — o art. 34 diz "para ambos os sexos", e quatro regras se dividem por sexo

**Veredito: confirma** — e a fonte oficial local, hoje conferida, **fecha a
ressalva** que a conferência de origem deixou aberta.

### 4.1 As regras alcançadas: exatamente quatro

`lce-1100-2021/art-34/original` é vinculado por **quatro** regras, e só por
elas: `regra-0080`, `regra-0081`, `regra-0082`, `regra-0083`. As quatro o
citam nominalmente no `fundamentacao_integral` ("artigos 24, 27, inciso II, e
**34** da Lei Complementar nº 1.100/2021" nas duas primeiras; "artigos 25, 27,
inciso I, e **34**" nas duas últimas).

| regra | `sexo`    | trilho de cálculo     | `data_adm_apos` | `data_adm_ate` |
| ----- | --------- | --------------------- | --------------- | -------------- |
| 0080  | MASCULINO | art. 24 + art. 27, II | 31/12/2003      | 31/12/2099     |
| 0081  | FEMININO  | art. 24 + art. 27, II | 31/12/2003      | 31/12/2099     |
| 0082  | MASCULINO | art. 25 + art. 27, I  | 01/01/1950      | 31/12/2003     |
| 0083  | FEMININO  | art. 25 + art. 27, I  | 01/01/1950      | 31/12/2003     |

`0080`×`0081` e `0082`×`0083` divergem, na chave material do P2, em
**exatamente um campo: `sexo`** (verificado mecanicamente). A
`fundamentacao_integral` de cada par é byte a byte idêntica.

### 4.2 O texto, verbatim

`lce-1100-2021/art-34/original`, no corpus:

> Art. 34. O policial civil, o policial legislativo e o ocupante de cargo de
> policial penal ou de agente de segurança socioeducativo serão aposentados
> voluntariamente, desde que observados, cumulativamente, os seguintes
> requisitos, **para ambos os sexos**:

### 4.3 O que esta reconferência fecha e a de origem não podia fechar

A conferência do regime novo registrou, com razão, uma ressalva: *"silêncio
não é o mesmo que vedação, e os incisos não transcritos do art. 34 poderiam,
em tese, reintroduzir a distinção"*. Os incisos **não estão no corpus** — o
documento transcreve só o caput.

Mas eles estão na publicação oficial compilada que o próprio dispositivo cita
em `fontes`, e essa publicação tem camada de texto local
(`fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt`, linhas 741–752):

> Art. 34. O policial civil, o policial legislativo e o ocupante de cargo de
> policial penal ou de agente de segurança socioeducativo serão aposentados
> voluntariamente, desde que observados, cumulativamente, os seguintes
> requisitos, para ambos os sexos:
>
> I - 55 (cinquenta e cinco) anos de idade;
>
> II - 30 (trinta) anos de contribuição;
>
> III - 25 (vinte e cinco) anos de efetivo exercício em cargo de natureza
> estritamente policial; e
>
> IV - 5 (cinco) anos na carreira em que se dará a aposentadoria.

**Os quatro incisos são numericamente idênticos para homem e mulher.** A
ressalva se resolve contra a reintrodução: o artigo inteiro — caput e os
quatro incisos — fixa **um único conjunto de requisitos, expressamente para
ambos os sexos**.

Nenhuma das outras provisões vinculadas pelas quatro reintroduz a distinção:
`cf88/art-40-par-4b/ec-103-2019` ("Poderão ser estabelecidos por lei
complementar do respectivo ente federativo idade e tempo de contribuição
diferenciados para aposentadoria de ocupantes do cargo de agente
penitenciário, de agente socioeducativo ou de policial [...]"),
`lce-1100-2021/art-24`, `art-25`, `art-27-inc-i` e `art-27-inc-ii` — nenhuma
contém "homem", "mulher" ou "sexo". E `cf88/art-40-par-1-inc-iii/ec-103-2019`
só o faz na primeira parte, da União, que as quatro não citam (elas citam a
"segunda parte").

**Verdade conferida:** o único dispositivo do material vinculado por
0080–0083 que se pronuncia sobre sexo diz "para ambos os sexos", e o catálogo
grava duas regras por trilho, uma para cada sexo.

### 4.4 Onde isso para

- **Não se conclui que o `sexo` esteja errado.** A
  [reconciliação policial](reconciliacao-policial.md) §1 registra que a
  própria matriz to-be da PGE-RO mantém o desdobramento por sexo nas
  hipóteses permanentes, com a mesma base legal nas duas linhas. Há decisão
  institucional a conhecer antes.
- **Não se afirma nada sobre o motor.** As quatro são `simulavel: S`;
  `sexo` é coluna e é lido, mas idade e tempo de contribuição **não têm
  coluna** e o motor não lê fundamentação. O que se prova é uma divergência
  entre o registro e a lei citada, não um comportamento.
- **Não se propõe transcrever nem vincular nada.** Os incisos do art. 34
  estão dentro do dispositivo já vinculado; transcrevê-los é ato de autoria
  humana e está fora do que esta reconferência pode fazer.

______________________________________________________________________

## 5. Item 5.4 — "dezesseis regras da ECE 146/2021 não citam o dispositivo que estabelece seus requisitos"

**Veredito: confirma o fato, refuta a contagem.** São **19**, e o padrão tem
uma extensão de mais 13 que o item não registra.

### 5.1 A contagem

A afirmação vem do §5.1 da
[conferência voluntária CF/88](conferencia-criterio-dispositivo-voluntaria-cf88.md),
cujo **próprio título diz "16 regras" e cuja primeira frase enumera
"(0043–0058, 0068–0070)"** — que são 16 + 3 = **19**. O resumo por categoria
do mesmo relatório escreve "(19)", e o seu ponto em aberto nº 6 escreve
"Dezenove regras". O erro é do título, e a lista consolidada herdou o título.

Conferido contra o `dispositivos:` das 112, as regras que vinculam algum
dispositivo dos arts. 5º, 6º ou 8º da ECE 146/2021 são exatamente:

**`regra-0043`, `0044`, `0045`, `0046`, `0047`, `0048`, `0049`, `0050`,
`0051`, `0052`, `0053`, `0054`, `0055`, `0056`, `0057`, `0058`, `0068`,
`0069`, `0070` — 19 regras.**

(0043–0050 pelo art. 6º; 0051–0058 pelo art. 5º; 0068–0070 pelo art. 8º.)

### 5.2 O fato substantivo: confirmado

Lidos os três campos de fundamentação das 19 (nenhuma tem
`fundamentacao_proporcional` preenchida; `fundamentacao` só em oito):
**nenhuma cita o *caput* de nenhum dos três artigos, nem os incisos do
caput.** Todas citam exclusivamente os §§, sempre nomeados:

| regras           | o que a fundamentação nomeia da ECE 146/2021   |
| ---------------- | ---------------------------------------------- |
| 0043, 0044       | "artigo 6º, § 2º, I, e § 3°, I"                |
| 0045, 0046       | "artigo 6º, §§ 1° e 2°, inciso I, e § 3º, I"   |
| 0047, 0048       | "artigo 6º, § 2º, II, e § 3°, II"              |
| 0049, 0050       | "artigo 6º, §§ 1° e 2°, inciso II, e § 3º, II" |
| 0051, 0052       | "artigo 5º, § 6º, I, e § 7°, I"                |
| 0053, 0054       | "artigo 5º, §§ 4° e 6°, inciso I, e § 7º, I"   |
| 0055, 0056       | "artigo 5º, § 6º, II, e § 7°, II"              |
| 0057, 0058       | "artigo 5º, §§ 4° e 6°, inciso II, e § 7º, II" |
| 0068, 0069, 0070 | "artigo 8, §§ 1° e 2°"                         |

E os caputs onde moram os requisitos **não existem como dispositivo autorado**:
o diretório `okf/dispositivos/ece-146-2021/` tem exatamente `art-4`,
`art-5-par-4`, `art-5-par-6-inc-i`, `art-5-par-6-inc-ii`, `art-5-par-7-inc-i`,
`art-5-par-7-inc-ii`, `art-6-par-1`, `art-6-par-2-inc-i`,
`art-6-par-2-inc-ii`, `art-6-par-3-inc-i`, `art-6-par-3-inc-ii`, `art-7-par-1`,
`art-7-par-2`, `art-7-par-3`, `art-8-par-1`, `art-8-par-2`. Nenhum `art-5`,
`art-6`, `art-7` ou `art-8`.

Os caputs aparecem só como **contexto de leitura** dentro dos docs dos §§, e
os três param na abertura da enumeração — verbatim:

> Art. 5º [...] poderá aposentar-se voluntariamente quando preencher,
> cumulativamente, os seguintes requisitos:

> Art. 6º [...] poderá aposentar-se voluntariamente quando preencher,
> cumulativamente, os seguintes requisitos:

> Art. 8º [...] poderá aposentar-se quando o total da soma resultante da sua
> idade e do tempo de contribuição e o tempo de efetiva exposição forem,
> respectivamente, de:

### 5.3 Duas precisões que o título do item apaga, e que o achado precisa carregar

**Primeira: "não citam o dispositivo dos requisitos" ≠ "não citam requisito
nenhum".** Três §§ efetivamente citados *carregam* requisito no próprio
texto, e por isso a afirmação larga seria falsa:

- `art-5-par-4` (citado por 0053, 0054, 0057, 0058) fixa, para o professor,
  "51 (cinquenta e um) anos de idade, se mulher, e 56 (cinquenta e seis)
  anos, se homem" e "25 [...] anos de contribuição, se mulher, e 30 [...] se
  homem";
- `art-5-par-6-inc-i` (citado por 0051–0054) condiciona a integralidade a "no
  mínimo, 62 (sessenta e dois) anos de idade, se mulher, e 65 (sessenta e
  cinco) anos de idade, se homem";
- `art-6-par-1` (citado por 0045, 0046, 0049, 0050) reduz "para ambos os
  sexos, os requisitos de idade e tempo de contribuição em 5 (cinco) anos".

A formulação exata é: **as 19 não citam o caput nem os incisos dos arts. 5º,
6º e 8º, onde estão os requisitos gerais de idade, tempo de contribuição,
tempo no cargo e pedágio** — e esses textos não existem em lugar nenhum do
corpus.

Consequência colateral, já registrada e agora confirmada: as oito regras do
art. 5º gravam `tabelapontuacao: S` e as oito do art. 6º gravam `N`, e
**nenhum § citado dos dois artigos institui pontuação**. Só o
`art-8-par-1` menciona "somatório de pontos", e ele é dos três de agentes
nocivos.

**Segunda: o padrão se estende ao art. 7º, com outro perfil.** Treze regras
mais vinculam §§ do art. 7º e nunca o caput: `regra-0072`, `0073`, `0074`,
`0075`, `0076`, `0077`, `0078`, `0079`, `0084`, `0109`, `0110`, `0111`,
`0112`. O caput do art. 7º — legível só como contexto dentro dos docs dos §§
— é onde estão o corte de ingresso e a idade mínima:

> Art. 7º O policial civil [...] que tenham ingressado na respectiva carreira
> **até a data de entrada em vigor da Emenda Constitucional nº 103, de 13 de
> novembro de 2019**, poderão aposentar-se na forma da Lei Complementar nº
> 51, de 20 de dezembro de 1985, com paridade e integralidade, observada a
> **idade mínima de 55 (cinquenta e cinco) anos para ambos os sexos** ou o
> disposto no § 2º.

Aqui o dano é **menor em onze** e **igual em duas**: onze das treze vinculam
`art-7-par-2`, que traz a idade alternativa ("aos 52 [...] se mulher, e aos 53
[...] se homem") e o pedágio, e todas vinculam `art-7-par-3`, que repete o
corte de 13/11/2019 no próprio texto. Mas `regra-0078` e `regra-0079`
vinculam `art-7-par-1` + `art-7-par-3` sem o § 2º: para elas, **a idade
mínima de 55 anos, que é o requisito do ramo "sem pedágio", só está no caput
não citado e não autorado.**

**Portanto: 19 regras onde o requisito está inteiramente fora do que se cita;
mais 13 onde só o caput falta, sendo 2 delas (`0078`/`0079`) tão graves
quanto as 19.** Total de regras que vinculam algum dispositivo da ECE
146/2021: 56 — as outras 24 vinculam só o art. 4º, que não é artigo de
requisito.

### 5.4 O que não consegui conferir

**Nada do texto da ECE 146/2021 foi conferido contra a fonte oficial.** O
único arquivo local é `sapl-emenda_146.pdf`, escaneado sem camada de texto
(`pdftotext` extrai 10 bytes de 10 páginas), e a `fontes` do
`ece-146-2021/norma.md` aponta para esse mesmo PDF no SAPL. Todo texto da
Emenda citado nesta seção — inclusive os caputs dos arts. 5º, 6º, 7º e 8º e o
art. 4º — é **a transcrição já autorada em `okf/dispositivos/`**, não a fonte.
Se a pergunta for "o art. 5º da ECE 146/2021 tem mesmo incisos, e quais?",
**não consegui responder**: precisaria de OCR do PDF ou de outra publicação da
Emenda com texto.

______________________________________________________________________

## 6. Item 1.2 — `regra-0084`: `sexo: AMBOS` vinculando só a alínea feminina

**Veredito: confirma**, e a incompatibilidade é mais estreita e mais nítida
do que "sexo sem fundamento".

### 6.1 O registro

| campo                   | valor                                                         |
| ----------------------- | ------------------------------------------------------------- |
| `nome`                  | Aposentadoria por Mandado de Injunção                         |
| `tipo_de_beneficio`     | APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO            |
| `sexo`                  | **AMBOS**                                                     |
| `simulavel`             | N                                                             |
| `apos_especial`         | S                                                             |
| `integral` / `paridade` | S / N                                                         |
| `tipo_calculo`          | Valor Médio                                                   |
| janelas                 | adm. 01/01/1950 → 31/12/2099; direito 01/01/1950 → 31/12/2099 |

`fundamentacao_proporcional` e `fundamentacao_integral` são **a mesma string,
byte a byte** (sha256 `28cfbed8cd32…`), e são uma lista nua de citações:

> Artigo 40, § 1°, inciso III, segunda parte, da Constituição Federal, com
> redação dada pela Emenda Constitucional nº 103/2019, artigo 7º, § 2º e § 3º,
> da Emenda à Constituição Estadual nº 146/2021 e artigo 1º, inciso II,
> **alínea "b"**, da Lei Complementar nº 51/1985.

`dispositivos:` reflete fielmente isso — quatro vínculos:
`cf88/art-40-par-1-inc-iii/ec-103-2019`, `ece-146-2021/art-7-par-2/original`,
`ece-146-2021/art-7-par-3/original`, `lc-51-1985/art-1-inc-ii-al-b/lc-144-2014`.

### 6.2 A alínea, verbatim

`lc-51-1985/art-1-inc-ii-al-b/lc-144-2014`:

> Art. 1o O servidor público policial será aposentado: (Redação dada pela Lei
> Complementar n° 144, de 2014)
>
> II - voluntariamente, com proventos integrais, independentemente da idade:
> (Redação dada pela Lei Complementar n° 144, de 2014)
>
> **b)** após **25** (vinte e cinco) anos de contribuição, desde que conte,
> pelo menos, **15** (quinze) anos de exercício em cargo de natureza
> estritamente policial, **se mulher**. (Incluído pela Lei Complementar n°
> 144, de 2014)

A alínea **"a"** — "após 30 (trinta) anos de contribuição, desde que conte,
pelo menos, 20 (vinte) anos de exercício em cargo de natureza estritamente
policial, **se homem**" — está autorada no corpus
(`lc-51-1985/art-1-inc-ii-al-a/lc-144-2014`) e **não é citada nem vinculada
pela `regra-0084`**.

**Comprovado:** uma regra declarada aplicável a **AMBOS** os sexos invoca,
como única fonte do tempo de contribuição e do tempo de exercício policial, a
provisão restrita a mulheres — e a provisão masculina, existente e transcrita,
não aparece.

### 6.3 A precisão que a formulação larga perderia

Não se pode dizer que o `sexo: AMBOS` esteja *inteiramente* sem fundamento:
entre os quatro dispositivos vinculados, **dois alcançam os dois sexos** —
o caput do art. 7º da ECE 146/2021 (legível como contexto dentro dos docs dos
§§) fala em "idade mínima de 55 anos **para ambos os sexos**", e o
`art-7-par-2` é expressamente bilateral: "aos 52 (cinquenta e dois) anos de
idade, **se mulher**, e aos 53 (cinquenta e três) anos de idade, **se
homem**".

A incompatibilidade é, portanto, **localizada e por isso mais forte**: o § 2º
do art. 7º condiciona o benefício a "cumprido o período adicional de
contribuição correspondente ao tempo que [...] faltaria para atingir **o tempo
de contribuição previsto na Lei Complementar n° 51**" — e o único tempo de
contribuição que a `regra-0084` traz da LC 51/1985 é o de **mulher (25/15)**.
Para um requerente homem, a regra remete a um tempo que ela própria nunca
nomeia.

### 6.4 Por que este é o item mais desprotegido da lista

Verificado nesta árvore:

- **Nenhum detector alcança a `regra-0084`.** Rodados os detectores sobre o
  bundle (79 detecções: 41 `P1_NOME_REPETIDO`, 17
  `P9_INTEGRAL_SEM_FUNDAMENTACAO`, 13 `P9_CAMPOS_VAZIOS_PENDENTES`, 7
  `P2_IGUALDADE_MATERIAL_ATIVA`, 1 `P9_SEXO_FUNDAMENTACAO`), **`regra-0084`
  não aparece em nenhuma**. O `P9_SEXO_FUNDAMENTACAO` — que pegaria o mesmo
  padrão — só confronta MASCULINO/FEMININO, e por isso dispara em
  `regra-0078` e não aqui.
- **Nenhum achado a referencia.** `grep -l "regra-0084"` em
  `okf/regras-sisprev/achados/` não devolve arquivo nenhum.

Ou seja: mesmo padrão da `regra-0078` (que tem detector *e* `achado-0010`),
sem detector e sem achado.

### 6.5 O que ficou faltando, e é decisivo

- **A LC 51/1985 não pôde ser reconferida contra a fonte oficial hoje.** A
  única `fontes` autorada é o Planalto, que devolve HTTP `000`, e não há cópia
  local em `fontes-oficiais/arquivos/`. O texto das duas alíneas acima é o
  transcrito no corpus.
- **O provimento judicial não está em lugar nenhum.** A regra é "por Mandado
  de Injunção", e nenhuma coluna do Sisprev registra decisão judicial. Sem
  conhecer a ordem que a define, **não se diz o que ela de fato aplica a um
  requerente homem** — só que o registro e a citação não podem estar ambos
  certos.
- **`simulavel: N`**, então a fundamentação pode orientar a triagem humana —
  o que torna a citação errada *mais* consequente, não menos, porque é o texto
  que o servidor recebe. Nada se afirma aqui sobre comportamento do motor.

______________________________________________________________________

## 7. Observação transversal — os incisos da LCE 1.100/2021 estão na fonte oficial local

Isto não é item da lista; é o insumo que mudou três vereditos acima e que
provavelmente muda outros.

Quatro documentos do bundle endereçam o **artigo inteiro**
(`componentes: [artigo N]`) e transcrevem **só o caput**, parando em
"requisitos cumulativamente:" / "seguintes requisitos, para ambos os sexos:" /
"observadas as seguintes condições:". São `lce-1100-2021/art-32`, `art-34`,
`art-35` e — na mesma família — `art-41-inc-iii`, este sim já com o inciso.

Os incisos faltantes estão em
`fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt`, que é a extração com
texto da **mesma publicação compilada** que os três documentos declaram em
`fontes`. Lidos ali:

| artigo  | incisos, verbatim da publicação compilada                                                                                                                                                                                                                                                                                | efeito sobre a conferência                                                                               |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| art. 32 | "I - 62 (sessenta e dois) anos de idade, **se mulher**, e 65 (sessenta e cinco) anos de idade, **se homem**; II - 25 [...] anos de contribuição; III - tempo mínimo de 10 [...] anos de efetivo exercício no serviço público; e IV - 5 [...] anos no cargo efetivo"                                                      | `sexo` de `0035`–`0038` **é** fundado pelo dispositivo que elas vinculam — só não está transcrito        |
| art. 34 | "I - 55 [...] anos de idade; II - 30 [...] anos de contribuição; III - 25 [...] anos de efetivo exercício em cargo de natureza estritamente policial; e IV - 5 [...] anos na carreira"                                                                                                                                   | **nenhum distingue sexo** — fecha a ressalva do item 4.4 (§4.3)                                          |
| art. 35 | "I - 20 [...] anos de tempo de contribuição, **se mulher**, e 25 [...], **se homem**, em caso de deficiência **grave**; II - 24 [...] e 29 [...], deficiência **moderada**; III - 28 [...] e 33 [...], deficiência **leve**; ou IV - 55 [...] anos de idade, se mulher, e 60 [...], se homem, independentemente do grau" | o **grau** de `0059`–`0064` e o `sexo` de `0033`/`0034`/`0059`–`0064` **estão** no dispositivo vinculado |

Três consequências, e nenhuma delas é conclusão desta página:

1. **A §5.4 da conferência do regime novo precisa ser relida.** Ela afirma que
   "`art-33` (professor), `art-35` (deficiência) e `cf88/art-40-par-5` são
   **silentes** quanto a sexo". Isso é verdade do *texto transcrito* do art.
   35; é **falso do artigo**, cujos incisos I–IV distinguem por sexo em todos
   os quatro. O mesmo vale para o art. 32 em relação às `0035`–`0038`.
2. **A hipótese de "lacuna de schema" do `achado-0003`/`achado-0004`
   (0059≡0063, 0060≡0064) ganha corpo.** O grau grave/moderada/leve existe na
   lei, com números distintos, e o catálogo o carrega **só no `nome`** — é
   exatamente a leitura que a `CLAUDE.md` antecipa: regras legitimamente
   distintas cuja distinção o catálogo não expressa.
3. **É a "transcrição truncada" do §5.3 da lista consolidada, no seu modo
   silencioso.** Os `componentes` estão certos, o caminho confere, o vínculo
   resolve, e a conferência fecha **pela metade do artigo** sem nada falhar. A
   diferença é que aqui a lacuna é visível — o caput anuncia incisos —, e o
   texto para preenchê-la já está no repositório.

**Não transcrevi nada** (está fora do que esta tarefa pode fazer, e é ato de
autoria humana). Registro que a fila `TRANSCREVER` da LCE 1.100/2021 é hoje
**destravável sem acesso à internet**.

______________________________________________________________________

## 8. O que ficou faltando

| pendência                                                               | por quê                                                                            | destrava com                                            |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------- |
| texto oficial da **ECE 146/2021** (arts. 4º a 8º, caputs e incisos)     | PDF escaneado sem camada de texto — `pdftotext` extrai 10 bytes                    | OCR do PDF, ou outra publicação da Emenda com texto     |
| texto oficial da **LC 51/1985** (alíneas "a" e "b" do art. 1º, II)      | Planalto HTTP `000`; sem cópia local                                               | Planalto de volta, ou fonte alternativa (Câmara/Senado) |
| texto oficial da **LC 152/2015** (incisos do art. 2º)                   | idem — e o doc autorado transcreve só o caput, que termina em ":"                  | idem                                                    |
| parágrafos do **art. 2º da EC 41/2003** (eventual regra de magistério)  | transcrito só até o caput; sem isso, `0099`/`0100` só admitem a afirmação estreita | transcrição do artigo completo                          |
| **incisos** dos arts. 2º e 6º da EC 41/2003 e do art. 3º da EC 47/2005  | idem — é onde estariam os requisitos por sexo das dez regras do item 4.3           | transcrição                                             |
| decisão judicial que define a **`regra-0084`**                          | mandado de injunção não é dispositivo e não tem coluna                             | documento do processo, fora do repositório              |
| se o desdobramento por sexo das policiais tem **decisão institucional** | a matriz to-be da PGE mantém o desdobramento sem apresentar dispositivo            | conversa com PGE/IPERON                                 |

______________________________________________________________________

## 9. O que está pronto para virar achado autorado, e o que não está

**Pronto — provado dentro do repositório, sem depender de fonte externa:**

1. **`regra-0084`, `sexo: AMBOS` com só a alínea feminina** (§6). Os dois
   lados são campo deployable, o texto da alínea está transcrito, a alínea
   masculina existe e não é citada, e **não há detector nem achado cobrindo a
   regra hoje**. É o item mais desprotegido dos seis. A formulação a autorar é
   a estreita: *não é possível que `sexo: AMBOS` e a citação exclusiva da
   alínea "b" estejam ambos certos* — sem dizer qual cede, e sem afirmar
   comportamento do motor.
2. **`apos_especial: S` sem correspondente em campo nenhum: `regra-0092`,
   `regra-0099`, `regra-0100`** (§2.2). Três regras, cada uma com uma gêmea
   (`0091`, `0097`, `0098`) de fundamentação byte-idêntica e
   `apos_especial: N`. O achado deve nomear as três — a lista consolidada só
   registra duas, e a terceira está descrita em outro relatório sem ter sido
   promovida.
3. **`sexo` de `regra-0030`/`regra-0031` sem provisão que o funde** (§3.4).
   Único campo material divergente; nenhuma das seis provisões vinculadas
   distingue por sexo; e a consequência para o `P2` é mecanicamente
   verificável (o grupo que hoje não existe passaria a existir).
4. **`sexo` das dez regras de transição** — `0085`, `0086`, `0097`–`0102`,
   `0105`, `0106` (§3.3). **Com a exclusão explícita de `0103`/`0104`**, que
   têm o critério fundado pelo art. 46 da LCE 432/2008, conferido contra a
   publicação oficial.
5. **As 19 regras da ECE 146/2021 cujos requisitos não são citados por campo
   deployable nenhum** (§5). O achado deve trazer a lista nominal e a
   pergunta que o próprio relatório de origem formula: *uma fundamentação que
   não nomeia a provisão de cujos requisitos o servidor foi considerado
   titular é fundamentação completa?* Vale registrar junto as `0078`/`0079`,
   que são o mesmo caso pelo art. 7º.

**Pronto, mas o enquadramento precisa mudar:**

6. **A idade-limite sem coluna, nas seis compulsórias** (§1). O fato está
   provado nas duas pontas e é mais forte do que a lista diz (o número não
   aparece nem no `nome` nem na fundamentação). Mas **não é "critério sem
   dispositivo"** — é *critério sem coluna*, com dispositivo. Sob o escopo de
   parametrização, o achado é **pedido de coluna ao IPERON**, e deve ser
   escrito como tal. Sugere-se, junto, separar o bloco 4 da lista consolidada
   em duas famílias (sem coluna × sem dispositivo).

**Ainda não pronto:**

7. **O art. 34 e o desdobramento por sexo das policiais** (§4). O lado do
   texto legal fechou — caput *e* os quatro incisos, um só conjunto de
   requisitos "para ambos os sexos". O que falta é institucional: a matriz
   to-be da PGE-RO mantém o desdobramento, e autorar o achado antes de saber
   se há decisão por trás dele seria acusar o registro de um erro que pode ser
   uma escolha. **O achado fica maduro assim que essa pergunta for feita**;
   hoje o que se autora com segurança é a pergunta, não a acusação.

## Referências

- Lista consolidada reconferida aqui,
  [`achados-candidatos-da-conferencia.md`](achados-candidatos-da-conferencia.md)
- [`conferencia-criterio-dispositivo-compulsoria-idade.md`](conferencia-criterio-dispositivo-compulsoria-idade.md)
  (origem do 4.1)
- [`conferencia-criterio-dispositivo-transicao-ec41-ec47.md`](conferencia-criterio-dispositivo-transicao-ec41-ec47.md)
  (origem do 4.2, primeira metade, e do 4.3)
- [`conferencia-criterio-dispositivo-voluntaria-regime-novo.md`](conferencia-criterio-dispositivo-voluntaria-regime-novo.md)
  (origem do 4.2, segunda metade, e do 4.4)
- [`conferencia-criterio-dispositivo-voluntaria-cf88.md`](conferencia-criterio-dispositivo-voluntaria-cf88.md)
  (origem do 5.4)
- [`conferencia-criterio-dispositivo-policial.md`](conferencia-criterio-dispositivo-policial.md)
  (origem do 1.2)
- [`reconciliacao-policial.md`](reconciliacao-policial.md) §1–§2 (matriz to-be
  da PGE-RO, contraponto do §4.4)
- Definição de trabalho de "regra", `sexo` como critério aferido e o escopo de
  parametrização, [`docs/spec/regra.md`](../spec/regra.md)
- Contrato do dispositivo e da norma,
  [`docs/spec/dispositivo.md`](../spec/dispositivo.md)
