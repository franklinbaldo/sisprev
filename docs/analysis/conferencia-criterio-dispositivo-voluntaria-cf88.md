# Conferência `critério → dispositivo` — as 29 regras de voluntária por tempo de contribuição fundadas na CF/88 e na ECE 146/2021

> **Nota:** Relatório gerado por IA como apoio à decisão. **Não é artefato
> oficial**, não edita nenhuma `regra-*.md`, `achado-*.md` ou dispositivo,
> não altera schema, dados derivados (`data/regras-sisprev.csv`), motor ou
> `site/`. É a segunda aplicação da conferência descrita na RFC 0008 §5 —
> para cada critério da regra, qual dispositivo o funda —, agora sobre o
> maior bloco homogêneo do catálogo. Toda conclusão sobre citação é ato
> humano, em achado próprio.

## O método

A RFC 0008 §5 registra a definição da coordenação: a fundamentação
**articula** os dispositivos de forma a fundamentar **cada** critério da
própria regra. Logo a relação é `critério → dispositivo(s)`, e
`dispositivos:` é a união achatada dela. Conferir é desachatar.

Duas perguntas que não coincidem, e a distinção é o que este relatório mais
tenta preservar:

1. *"qual dispositivo funda este critério?"* — jurídica, é o que a
   conferência responde;
2. *"o que este campo cita?"* — de leitura, é o que `dispositivos:` registra.

Um `dispositivos:` afirma "a fundamentação desta regra **cita** esta
provisão", nunca "a regra se funda nela". A
[conferência anterior](conferencia-criterio-dispositivo-invalidez-0006-0009.md)
errou nas duas direções exatamente por confundir as duas, e registrou o erro.
Aqui, **nenhum vínculo é proposto para acréscimo ou remoção**: onde a
conferência encontrou um critério sem dispositivo, ela verificou primeiro se
a provisão está citada em algum campo `fundamentacao*` da própria regra — e
quando não está, o resultado é uma lacuna a registrar, não um vínculo a criar.

## Uma correção de premissa, antes de tudo

O recorte deste lote foi descrito como "regras que não vinculam nenhuma lei
complementar estadual". **Isso não vale para `regra-0039` e `regra-0040`**,
que vinculam três dispositivos da LCE 432/2008 (arts. 24, 45 e 62) e os
citam expressamente. As outras 27 de fato não vinculam nenhuma LCE.

A correção não é cosmética: é justamente por vincularem a LCE 432/2008 que
0039/0040 produzem uma das divergências mais nítidas do lote (§5.5).

## O grupo

As 29 são `APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO`, `tipo: CIVIL`,
`atualmente_no_sistema: TRUE`, `validado_pge: FALSE`,
`validado_presidencia: FALSE`, `tipo_remun` vazio,
`requisitos_da_in_no_5_2020: N`,
`relatorio_p_reserva_remunerada_por_idade_ex_officio: N`,
`adicional_inatividade: N`, `visivel_dtc_integral: N` e
`visivel_dtc_proporcional: N`. Nenhuma foi validada.

Elas se organizam em seis subgrupos pela norma que articulam:

| subgrupo | regras     | articulação                                                        | ciclo |
| -------- | ---------- | ------------------------------------------------------------------ | ----- |
| **A**    | 0043–0050  | ECE 146/2021, **art. 6º** (+ CF art. 40, § 1º, III ou § 5º)        | 3º    |
| **B**    | 0051–0058  | ECE 146/2021, **art. 5º** (+ CF art. 40, § 1º, III ou § 5º)        | 3º    |
| **C**    | 0068–0070  | ECE 146/2021, **art. 8º** (+ CF art. 40, § 4º-C)                   | 3º    |
| **D**    | 0087–0092  | CF/88 texto original e EC 20/1998 (+ EC 20/1998, art. 8º)          | 4º    |
| **E**    | 0039, 0040 | LCE 432/2008 + CF art. 40 (EC 20/1998 e EC 41/2003) + ECE art. 4º  | 3º    |
| **F**    | 0093, 0094 | CF art. 40, § 1º, III, "a" (EC 20/1998) + emenda estadual truncada | 4º    |

### Os campos que variam

Onze das 27 colunas de domínio são constantes no lote. Estas variam:

| regra          | esp. | sexo      | integral  | tipo_calculo     | parid. | pontos | simul. | adm após   | adm até        | dir. após  | dir. até       |
| -------------- | ---- | --------- | --------- | ---------------- | ------ | ------ | ------ | ---------- | -------------- | ---------- | -------------- |
| **0039**       | S    | MASCULINO | **N**     | Valor Médio      | N      | N      | S      | 31/12/2003 | 31/12/2099     | 18/10/2021 | 31/12/2099     |
| **0040**       | S    | FEMININO  | **N**     | Valor Médio      | N      | N      | S      | 31/12/2003 | 31/12/2099     | 18/10/2021 | 31/12/2099     |
| 0043           | N    | MASCULINO | S         | Remun. Contrib   | S      | N      | S      | 01/01/1950 | 31/12/2003     | 14/09/2021 | 31/12/2099     |
| 0044           | N    | FEMININO  | S         | Remun. Contrib   | S      | N      | S      | 01/01/1950 | 31/12/2003     | 14/09/2021 | 31/12/2099     |
| 0045           | S    | MASCULINO | S         | Remun. Contrib   | S      | N      | S      | 01/01/1950 | 31/12/2003     | 14/09/2021 | 31/12/2099     |
| 0046           | S    | FEMININO  | S         | Remun. Contrib   | S      | N      | S      | 01/01/1950 | 31/12/2003     | 14/09/2021 | 31/12/2099     |
| 0047           | N    | MASCULINO | S         | Valor Médio      | N      | N      | S      | 01/01/1950 | 14/09/2021     | 14/09/2021 | 31/12/2099     |
| 0048           | N    | FEMININO  | S         | Valor Médio      | N      | N      | S      | 01/01/1950 | 14/09/2021     | 14/09/2021 | 31/12/2099     |
| **0049**       | S    | MASCULINO | S         | Valor Médio      | N      | N      | S      | 01/01/1950 | **14/06/2021** | 14/09/2021 | 31/12/2099     |
| **0050**       | S    | FEMININO  | S         | Valor Médio      | N      | N      | S      | 01/01/1950 | **14/06/2021** | 14/09/2021 | 31/12/2099     |
| 0051           | N    | MASCULINO | S         | Remun. Contrib   | S      | S      | S      | 01/01/1950 | 31/12/2003     | 14/09/2021 | 31/12/2099     |
| 0052           | N    | FEMININO  | S         | Remun. Contrib   | S      | S      | S      | 01/01/1950 | 31/12/2003     | 14/09/2021 | 31/12/2099     |
| 0053           | S    | MASCULINO | S         | Remun. Contrib   | S      | S      | S      | 01/01/1950 | 31/12/2003     | 14/09/2021 | 31/12/2099     |
| 0054           | S    | FEMININO  | S         | Remun. Contrib   | S      | S      | S      | 01/01/1950 | 31/12/2003     | 14/09/2021 | 31/12/2099     |
| **0055**       | N    | MASCULINO | S         | Valor Médio      | N      | S      | S      | 01/01/1950 | **31/12/2099** | 14/09/2021 | 31/12/2099     |
| **0056**       | N    | FEMININO  | S         | Valor Médio      | N      | S      | S      | 01/01/1950 | **31/12/2099** | 14/09/2021 | 31/12/2099     |
| **0057**       | S    | MASCULINO | **N**     | Valor Médio      | N      | S      | S      | 01/01/2004 | **09/09/2021** | 14/09/2021 | 31/12/2099     |
| **0058**       | S    | FEMININO  | **S**     | Valor Médio      | N      | S      | S      | 01/01/2004 | **09/09/2021** | 14/09/2021 | 31/12/2099     |
| 0068/0069/0070 | S    | AMBOS     | S         | Valor Médio      | N      | S      | S      | 01/01/1950 | 14/09/2021     | 14/09/2021 | 31/12/2099     |
| 0087           | N    | *(vazio)* | *(vazio)* | Não identificado | S      | N      | N      | 01/01/1900 | 16/12/1998     | 01/01/1900 | **01/12/2002** |
| 0088           | S    | *(vazio)* | *(vazio)* | Não identificado | S      | N      | N      | 01/01/1910 | 16/12/1998     | 01/01/1910 | 16/12/1998     |
| 0089           | N    | *(vazio)* | *(vazio)* | Não identificado | S      | N      | N      | 01/01/1910 | 31/12/2003     | 16/12/1998 | 31/12/2003     |
| 0090           | S    | *(vazio)* | *(vazio)* | Não identificado | S      | N      | N      | 01/01/1910 | 31/12/2003     | 16/12/1998 | 31/12/2003     |
| 0091           | N    | *(vazio)* | *(vazio)* | Não identificado | S      | N      | **S**  | 01/01/1910 | 16/12/1998     | 16/12/1998 | 31/12/2003     |
| 0092           | S    | *(vazio)* | *(vazio)* | Não identificado | S      | N      | **N**  | 01/01/1910 | 16/12/1998     | 16/12/1998 | 31/12/2003     |
| 0093           | N    | MASCULINO | S         | Valor Médio      | N      | N      | S      | 01/01/1950 | 31/12/2024     | 31/12/2003 | 31/12/2024     |
| 0094           | N    | FEMININO  | S         | Valor Médio      | N      | N      | S      | 01/01/1950 | 31/12/2024     | 31/12/2003 | 31/12/2024     |

Em **doze** dos treze pares o único campo que difere é `sexo` — o que
confirma, no maior lote do catálogo, a definição de trabalho registrada em
[`okf/spec/regra.md`](../../okf/spec/regra.md): divergência em critério aferido já
torna duas regras não idênticas. As exceções são `0043`/`0044` (diferem
também no campo curto `fundamentacao`, preenchido só na 0043) e
`0057`/`0058` (diferem também em `integral` — §5.6).

## A conferência

### Subgrupo A — ECE 146/2021, art. 6º (regras 0043 a 0050)

Quatro pares, todos citando o art. 6º da ECE 146/2021 e vinculando os §§
efetivamente nomeados no campo.

| critério                                                  | valor                                                  | fundado por                                                                                                                    | fecha?                   |
| --------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------ |
| tipo de benefício (voluntária)                            | por idade e tempo contr.                               | `ece-146-2021/art-6-par-2-*` (caput: "poderá aposentar-se voluntariamente")                                                    | ✅                       |
| habilitação do RPPS estadual                              | —                                                      | `cf88/art-40-par-1-inc-iii/ec-103-2019`, 2ª parte: "na idade mínima estabelecida mediante emenda às respectivas Constituições" | ✅ (0043/0044/0047/0048) |
| redução do magistério                                     | `apos_especial: S`                                     | `ece-146-2021/art-6-par-1` + `cf88/art-40-par-5/ec-103-2019`                                                                   | ✅ (0045/0046/0049/0050) |
| ingresso até 31/12/2003 (0043–0046)                       | `data_adm_ate: 31/12/2003`                             | `art-6-par-2-inc-i`: "até 31 de dezembro de 2003"                                                                              | ✅                       |
| ingresso — cohort do inciso II                            | 0047/0048 `até 14/09/2021`; 0049/0050 `até 14/06/2021` | `art-6-par-2-inc-ii`: "para o servidor público não contemplado no inciso I"                                                    | ❌ ver §5.3 e §5.4       |
| `integral: S` + `Remuneração de Contribuição` (0043–0046) | integral pela remuneração do cargo                     | `art-6-par-2-inc-i`: "à totalidade da remuneração do servidor público no cargo efetivo"                                        | ✅                       |
| `integral: S` + `Valor Médio` (0047–0050)                 | integral sobre a média                                 | `art-6-par-2-inc-ii`: "média aritmética simples das maiores remunerações [...] 80%"                                            | ✅                       |
| `paridade: S` (0043–0046)                                 | reajuste com paridade                                  | `art-6-par-3-inc-i`: "de acordo com o disposto no art. 7º da Emenda Constitucional nº 41"                                      | ✅                       |
| `paridade: N` (0047–0050)                                 | reajuste pelo RGPS                                     | `art-6-par-3-inc-ii`: "nos termos estabelecidos para o Regime Geral de Previdência Social"                                     | ✅                       |
| idade mínima, tempo de contribuição                       | não parametrizados                                     | **art. 6º, caput, incisos — não transcritos e não citados**                                                                    | ❌ ver §5.1              |
| `sexo` (o eixo que separa cada par)                       | MASCULINO / FEMININO                                   | **nenhum dispositivo vinculado distingue por sexo** — `art-6-par-1` diz o oposto: "para ambos os sexos"                        | ❌ ver §5.2              |
| `tabelapontuacao: N`                                      | sem tabela                                             | nenhuma provisão vinculada institui pontuação                                                                                  | ✅ por ausência          |

**O núcleo de cálculo e reajuste fecha inteiro.** Os §§ 2º e 3º do art. 6º
são um par de tabelas espelhadas — inciso I dá totalidade + paridade, inciso
II dá média + RGPS — e os quatro pares as parametrizam corretamente,
inclusive na leitura de `integral` como "100% da base apurada", não como
"remuneração do cargo" (0047–0050 gravam `integral: S` com `Valor Médio`).
Essa leitura será decisiva em §5.5 e §5.6.

**O que não fecha é a metade dos requisitos.** Nenhum dos oito campos cita o
*caput* do art. 6º nem seus incisos — que é onde estão idade, tempo de
contribuição e pedágio. A citação é honesta (o campo diz "artigo 6º, § 2º,
I, e § 3º, I"), o vínculo é honesto, e ainda assim os critérios que decidem
a concessão não têm dispositivo.

### Subgrupo B — ECE 146/2021, art. 5º (regras 0051 a 0058)

Mesma arquitetura, artigo diferente, e uma diferença importante: **o § 6º, I
do art. 5º carrega idades mínimas no próprio texto**, o que o § 2º, I do art.
6º não faz.

| critério                                                  | valor                                                                  | fundado por                                                                                                                   | fecha?                                 |
| --------------------------------------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| habilitação do RPPS estadual                              | —                                                                      | `cf88/art-40-par-1-inc-iii/ec-103-2019`, 2ª parte                                                                             | ✅ (0051/0052/0055/0056)               |
| redução do magistério                                     | `apos_especial: S`                                                     | `ece-146-2021/art-5-par-4` (51/56 anos, 25/30 de contribuição) + `cf88/art-40-par-5/ec-103-2019`                              | ✅ (0053/0054/0057/0058)               |
| **`sexo`**                                                | MASCULINO / FEMININO                                                   | `art-5-par-6-inc-i`: "62 anos [...] se mulher, e 65 [...] se homem"; `art-5-par-4`: "51 [...] se mulher, e 56 [...] se homem" | ✅ **(o único subgrupo em que fecha)** |
| ingresso até 31/12/2003 (0051–0054)                       | `data_adm_ate: 31/12/2003`                                             | `art-5-par-6-inc-i`: "até 31 de dezembro de 2003"                                                                             | ✅                                     |
| ingresso — cohort do inciso II                            | 0055/0056 `31/12/2099`; 0057/0058 `após 01/01/2004` e `até 09/09/2021` | `art-5-par-6-inc-ii`: "não contemplado no inciso I do § 6º"                                                                   | ❌ ver §5.3, §5.4 e §5.7               |
| `integral: S` + `Remuneração de Contribuição` (0051–0054) | totalidade da remuneração                                              | `art-5-par-6-inc-i`: "à totalidade da remuneração do servidor público no cargo efetivo"                                       | ✅                                     |
| `Valor Médio` (0055–0058)                                 | média das 80% maiores                                                  | `art-5-par-6-inc-ii`                                                                                                          | ✅                                     |
| `paridade: S` (0051–0054)                                 | art. 7º da EC 41/2003                                                  | `art-5-par-7-inc-i`                                                                                                           | ✅                                     |
| `paridade: N` (0055–0058)                                 | termos do RGPS                                                         | `art-5-par-7-inc-ii`                                                                                                          | ✅                                     |
| **`tabelapontuacao: S`**                                  | soma idade + tempo                                                     | **nenhum dispositivo vinculado institui pontuação** — os quatro §§ citados não a mencionam                                    | ❌ ver §5.1                            |
| idade e tempo de contribuição                             | não parametrizados                                                     | **art. 5º, caput, incisos — não transcritos e não citados**                                                                   | ❌ ver §5.1                            |

A diferença mais informativa deste subgrupo é a que **não** aparece em campo
nenhum: `tabelapontuacao` vale `N` em todo o subgrupo A e `S` em todo o
subgrupo B. É o único traço que separa mecanicamente os arts. 5º e 6º da
Emenda no cadastro — e nenhum dispositivo vinculado o funda, dos dois lados.

### Subgrupo C — ECE 146/2021, art. 8º (regras 0068, 0069 e 0070)

Os três registros materialmente idênticos do `achado-0006`.

| critério                                     | valor                 | fundado por                                                                                                                                              | fecha?                        |
| -------------------------------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| exposição a agentes nocivos                  | `apos_especial: S`    | `cf88/art-40-par-4c/ec-103-2019` (habilitação do ente) + art. 8º, caput, citado no corpo dos dois §§                                                     | ✅                            |
| **`tabelapontuacao: S`**                     | somatório de pontos   | `ece-146-2021/art-8-par-1`: "a idade e o tempo de contribuição serão apurados em dias para o cálculo do **somatório de pontos** a que se refere o caput" | ✅ **(o único caso do lote)** |
| `integral: S` + `Valor Médio`                | média das 80% maiores | `art-8-par-2`                                                                                                                                            | ✅                            |
| `paridade: N`                                | —                     | `art-8-par-2` não remete ao art. 7º da EC 41/2003, ao contrário dos §§ 3º/7º, I dos arts. 6º/5º                                                          | ✅ por ausência               |
| `sexo: AMBOS`                                | —                     | nenhuma provisão vinculada distingue por sexo                                                                                                            | ✅ por ausência               |
| pontuação exigida, tempo mínimo de exposição | não parametrizados    | **art. 8º, caput, incisos — não transcritos, e o caput não é dispositivo autorado**                                                                      | ❌ ver §5.9                   |

Aqui a conferência **produz um eixo candidato** para o `achado-0006`, e é o
resultado mais útil deste subgrupo. O *caput* do art. 8º, transcrito como
contexto dentro dos dois §§ vinculados, termina assim:

> [...] poderá aposentar-se quando o total da soma resultante da sua idade e
> do tempo de contribuição **e o tempo de efetiva exposição forem,
> respectivamente, de:**

"Respectivamente, de:" abre uma enumeração de **faixas**, e três registros
idênticos com um dispositivo que enumera faixas é a coincidência que o
`achado-0006` pede para investigar ("faixas de exposição, grau de agente
nocivo"). A conferência **não confirma** a hipótese: os incisos não estão
transcritos em lugar nenhum do corpus, e nenhum campo do cadastro registra
faixa de exposição. O que ela faz é apontar exatamente onde a resposta está
e o que precisa ser autorado para obtê-la — a transcrição do *caput* do art.
8º com seus incisos.

### Subgrupo D — CF/88 texto original e EC 20/1998 (regras 0087 a 0092)

Seis regras de 4º ciclo, todas com `sexo`, `integral` vazios e
`tipo_calculo: Não identificado` (detecção `P9_CAMPOS_VAZIOS_PENDENTES`,
`achado-0008`).

**0087 e 0088 — texto original da CF/88:**

| critério                        | valor                        | fundado por                                                                                                                                    | fecha?       |
| ------------------------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| voluntária integral por tempo   | `fundamentacao_integral`     | `cf88/art-40-inc-iii-al-a/original`: "trinta e cinco anos de serviço, se homem, e trinta, se mulher, com proventos integrais"                  | ✅           |
| voluntária proporcional (0087)  | `fundamentacao_proporcional` | `cf88/art-40-inc-iii-al-c/original`: "trinta anos de serviço, se homem, e vinte e cinco, se mulher, com proventos proporcionais"               | ✅           |
| magistério (0088)               | `apos_especial: S`           | `cf88/art-40-inc-iii-al-b/original`: "trinta anos de efetivo exercício em funções de magistério, se professor, e vinte e cinco, se professora" | ✅           |
| ausência de proporcional (0088) | campo vazio                  | a alínea "b" não tem variante proporcional no texto original — a lacuna é **correta**                                                          | ✅           |
| `sexo` (vazio)                  | —                            | as três alíneas **parametrizam sexo expressamente**                                                                                            | ❌ ver §5.10 |
| `paridade: S`                   | —                            | nenhuma das alíneas trata de reajuste                                                                                                          | ❌           |
| `data_direito_ate` (0087)       | **01/12/2002**               | nenhuma provisão vinculada, e a redação original cessa em 16/12/1998                                                                           | ❌ ver §5.11 |

Este é o subgrupo mais bem vinculado do lote: cada alínea funda exatamente o
campo de fundamentação em que é citada, e a ausência do proporcional na 0088
é uma lacuna que o próprio texto legal explica. Vale registrar o acerto com
o mesmo peso das falhas.

**0089 e 0090 — regra permanente da EC 20/1998:**

| critério                            | valor                 | fundado por                                                                                                                                                                       | fecha?       |
| ----------------------------------- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| voluntária por idade+tempo          | —                     | `cf88/art-40-par-1-inc-iii-al-a/ec-20-1998` (60/35 homem, 55/30 mulher)                                                                                                           | ✅           |
| magistério (0090)                   | `apos_especial: S`    | `cf88/art-40-par-5/ec-20-1998`: "reduzidos em cinco anos, em relação ao disposto no § 1º, III, 'a'"                                                                               | ✅           |
| `fundamentacao_proporcional` (0089) | cita a alínea **"a"** | a alínea "a" nada diz sobre proporcionalidade; quem a estabelece é a alínea **"b"** ("com proventos proporcionais ao tempo de contribuição"), **autorada no corpus e não citada** | ❌ ver §5.12 |
| `paridade: S`                       | —                     | nenhuma provisão vinculada trata de reajuste                                                                                                                                      | ❌           |

**0091 e 0092 — regra de transição do art. 8º da EC 20/1998:**

| critério                         | valor                          | fundado por                                                                                                                                   | fecha?       |
| -------------------------------- | ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| regra de transição               | —                              | `ec-20-1998/art-8/original` — **transcrito só até "quando o servidor, cumulativamente:"**; os requisitos (idade, pedágio) não estão no corpus | ⚠️ ver §5.9  |
| janela `16/12/1998`–`31/12/2003` | —                              | `cf88/art-40-par-1-inc-iii/ec-103-2019` — redação **vigente a partir de 13/11/2019**                                                          | ❌ ver §5.8  |
| prazo de implementação           | `data_direito_ate: 31/12/2003` | `ece-146-2021/art-4/original` — que fixa **31/12/2024**                                                                                       | ❌ ver §5.2  |
| magistério (0092)                | `apos_especial: S`             | **nada** — a fundamentação da 0092 é byte-a-byte idêntica à da 0091 e não menciona magistério                                                 | ❌ ver §5.13 |

### Subgrupo E — LCE 432/2008 + CF/88 + art. 4º da ECE (regras 0039 e 0040)

| critério                        | valor                              | fundado por                                                                             | fecha?      |
| ------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------- | ----------- |
| magistério                      | `apos_especial: S`                 | `lce-432-2008/art-24/original` (redução de 5 anos) + `cf88/art-40-par-5/ec-20-1998`     | ✅          |
| `tipo_calculo: Valor Médio`     | média das 80% maiores              | `lce-432-2008/art-45/lce-672-2012` — e o art. 24, § 4º remete a ele expressamente       | ✅          |
| `paridade: N`                   | reajuste para preservar valor real | `lce-432-2008/art-62/original` — e o art. 24, § 2º remete a ele expressamente           | ✅          |
| requisitos de idade e tempo     | não parametrizados                 | o art. 24 remete ao **art. 22**, que não é citado nem vinculado                         | ❌          |
| `integral: N`                   | proporcional                       | **contraditado pelo próprio campo**: "com proventos **integrais** (cálculo por média)"  | ❌ ver §5.5 |
| `data_direito_apos: 18/10/2021` | direito a partir de 19/10/2021     | `ece-146-2021/art-4/original` — mas 18/10/2021 é o dia em que a LCE 432/2008 é revogada | ⚠️ ver §5.2 |
| `data_direito_ate: 31/12/2099`  | sentinela                          | `ece-146-2021/art-4/original` fixa **31 de dezembro de 2024**                           | ❌ ver §5.2 |

O art. 24 da LCE 432/2008 é o exemplo mais limpo do lote de uma articulação
que se auto-explica: seu § 2º manda reajustar na forma do art. 62 e seu § 4º
mandar calcular na forma do art. 45 — os três dispositivos que a regra cita
e vincula. Os critérios de resultado fecham perfeitamente. O que não fecha
são as **datas** e o campo `integral`.

### Subgrupo F — art. 40, § 1º, III, "a" + emenda estadual truncada (0093 e 0094)

Estas duas citam quatro provisões e vinculam **uma**.

| critério                         | valor                   | fundado por                                                                       | fecha?       |
| -------------------------------- | ----------------------- | --------------------------------------------------------------------------------- | ------------ |
| voluntária por idade e tempo     | —                       | `cf88/art-40-par-1-inc-iii-al-a/ec-20-1998` (60/35 homem, 55/30 mulher)           | ✅           |
| `sexo`                           | MASCULINO / FEMININO    | a mesma alínea "a", que parametriza idade e tempo por sexo                        | ✅           |
| `tipo_calculo: Valor Médio`      | média                   | citado o art. 40, § 3º (EC 41/2003) — **não transcrito no corpus**                | ❌           |
| `paridade: N`                    | —                       | citado o art. 40, § 8º (EC 41/2003) — **transcrito, não vinculado**               | ❌ ver §5.14 |
| janela `31/12/2003`–`31/12/2024` | —                       | citado "art. 4° da Emenda à Constituição Estadual - **CF**" — norma indeterminada | ⚠️ ver §6    |
| `data_adm_ate: 31/12/2024`       | admissão até 31/12/2024 | nenhuma provisão vinculada; ver §5.15                                             | ⚠️           |

## O que a conferência revelou

### 5.1 Nenhuma das 16 regras da ECE 146/2021 cita o dispositivo que estabelece os requisitos

É o achado estrutural do lote. Os arts. 5º, 6º e 8º da Emenda têm a mesma
forma: um *caput* que diz "poderá aposentar-se voluntariamente quando
preencher, **cumulativamente, os seguintes requisitos:**" seguido de incisos,
e depois §§ que dizem quanto se paga e como se reajusta.

As 16 regras (0043–0058, 0068–0070) citam e vinculam **exclusivamente os §§
de resultado**. O *caput* e seus incisos — idade mínima, tempo de
contribuição, tempo no cargo, pontuação, pedágio — não são citados por
nenhuma delas, não existem como dispositivo autorado, e seus incisos não
estão transcritos em lugar nenhum do corpus.

O efeito prático é assimétrico e visível na conferência: **a coluna
"resultado" fecha quase inteira e a coluna "requisito" está quase inteira
vazia.** As duas únicas exceções são as provisões de magistério (art. 5º,
§ 4º e art. 6º, § 1º), que são requisitos e *são* citadas, e o art. 8º, § 1º,
que menciona o "somatório de pontos".

Isso não é um vínculo a acrescentar. É o que o campo cita, e o campo cita
corretamente o que cita. É uma pergunta sobre a **fundamentação deployável**:
um documento de concessão que não nomeia a provisão de cujos requisitos o
servidor foi considerado titular é uma fundamentação completa?

### 5.2 O art. 4º da ECE 146/2021 é vinculado quatro vezes, e nenhuma das quatro grava o prazo que ele fixa

`ece-146-2021/art-4/original` é vinculado por `regra-0039`, `regra-0040`,
`regra-0091` e `regra-0092`. Seu texto condiciona:

> [...] observará os requisitos e os critérios exigidos pela legislação
> vigente até a data de entrada em vigor desta Emenda Constitucional, **desde
> que sejam cumpridos até 31 de dezembro de 2024**, sendo assegurada a
> qualquer tempo.

Os `data_direito_ate` das quatro: `31/12/2099`, `31/12/2099`, `31/12/2003`,
`31/12/2003`. **Nenhum é 31/12/2024.**

E a inversão que fecha o argumento: as **únicas** duas regras do lote que
gravam `31/12/2024` são `regra-0093` e `regra-0094` — precisamente as que
citam "art. 4° da Emenda à Constituição Estadual" com o número truncado e
que, por isso, **não vinculam o artigo**. O catálogo grava o prazo onde não
consegue declarar o vínculo, e não o grava nas quatro em que o vínculo está
declarado.

Isto reencontra, por outro caminho e num lote independente, a pendência já
registrada na
[conferência da invalidez](conferencia-criterio-dispositivo-invalidez-0006-0009.md)
§2. O padrão agora é grande demais para ser tratado como caso: **ou o art. 4º
não é o fundamento da janela temporal, ou as janelas estão gravadas erradas.**
A conferência não decide qual.

Caso particular de 0039/0040: `data_direito_apos: 18/10/2021` é **exatamente**
o dia em que a LCE 432/2008 é revogada (`vigencia_fim: 2021-10-18`) e a LCE
1.100/2021 entra em vigor. Sob a semântica confirmada em
[`semantica-das-janelas-temporais.md`](semantica-das-janelas-temporais.md)
(`apos` é exclusivo), a regra cobre direitos adquiridos **a partir de
19/10/2021 sob uma lei já revogada** — o que só o art. 4º da ECE explica, e é
justamente por isso que o `data_direito_ate: 31/12/2099` é incoerente: o art.
4º abre a janela **e** a fecha, e a regra usa metade dele.

### 5.3 Três parametrizações diferentes para o mesmo critério legal

Os arts. 5º, § 6º, II e 6º, § 2º, II definem sua clientela por complemento:
"para o servidor público **não contemplado no inciso I**". Seis regras
parametrizam esse mesmo complemento de três formas incompatíveis:

| regras    | dispositivo     | `data_adm_apos` | `data_adm_ate` | leitura                       |
| --------- | --------------- | --------------- | -------------- | ----------------------------- |
| 0047/0048 | art. 6º, §2º,II | 01/01/1950      | 14/09/2021     | todos, até a Emenda           |
| 0049/0050 | art. 6º, §2º,II | 01/01/1950      | **14/06/2021** | todos, até uma data sem fonte |
| 0055/0056 | art. 5º, §6º,II | 01/01/1950      | **31/12/2099** | todos, sem limite (sentinela) |
| 0057/0058 | art. 5º, §6º,II | **01/01/2004**  | 09/09/2021     | só os do complemento temporal |

Só 0057/0058 aplicam o complemento. As demais cobrem também quem ingressou
até 31/12/2003 — isto é, sobrepõem-se à janela das regras do inciso I
(0043–0046, 0051–0054), que gravam `data_adm_ate: 31/12/2003`.

**A sobreposição não é, por si, erro.** O inciso I exige duas coisas —
ingresso até 31/12/2003 **e** não ter feito a opção do § 16 do art. 40 da CF
— e quem ingressou antes de 2003 mas optou pela previdência complementar cai
no inciso II. A sobreposição é a forma correta de representar isso. O
problema é que **nenhuma coluna do Sisprev registra a opção do § 16**, de
modo que, para um servidor admitido antes de 2003, o simulador apresenta as
duas regras sem nada que as separe; e que **as seis não concordam entre si**
sobre qual das duas leituras adotar.

### 5.4 Duas datas de ingresso que não são a data de entrada em vigor da Emenda

Os *caputs* dos arts. 5º, 6º e 8º condicionam ao ingresso "até a data de
entrada em vigor desta Emenda Constitucional". A ECE 146/2021 tem
`vigencia_inicio: 2021-09-14` no corpus, e é o que 0047/0048 e 0068–0070
gravam (`14/09/2021`).

- `regra-0049` e `regra-0050` gravam **`14/06/2021`** — junho, não setembro.
- `regra-0057` e `regra-0058` gravam **`09/09/2021`** — dia 9, não dia 14.

Nenhuma das duas datas corresponde a qualquer `vigencia_*` do corpus. As
duas anomalias são pares de magistério cujos gêmeos não-magistério gravam a
data correta (0047/0048 e 0055/0056), o que torna a hipótese de erro de
digitação a mais econômica — mas `DATA_ADM_ATE` é campo deployável e a
conferência não a corrige.

### 5.5 `regra-0039` e `regra-0040`: `integral: N` num campo que diz "proventos integrais"

A `fundamentacao_integral` das duas começa, ipsis litteris:

> Aposentadoria especial de professor, **com proventos integrais** (cálculo
> por média) e sem paridade [...]

E o campo `integral` grava **`N`**. A `fundamentacao_proporcional` está vazia
(detecção `P9_INTEGRAL_SEM_FUNDAMENTACAO`, `achado-0009`).

O que este lote acrescenta ao `achado-0009` é o **controle**: `regra-0047`,
`0048`, `0049`, `0050`, `0055` e `0056` usam a mesmíssima construção — "com
proventos integrais (cálculo por média)" — e gravam `integral: S`. A leitura
de `integral` como "100% da base apurada, seja ela a remuneração do cargo ou
a média" é, portanto, a leitura corrente do próprio catálogo, e 0039/0040
divergem dela. Não é ambiguidade de vocabulário: são duas regras fora do
padrão de seis.

### 5.6 `regra-0057` e `regra-0058`: mesma regra, `integral` diferente por sexo

As duas diferem em exatamente dois campos: `sexo` (MASCULINO/FEMININO) e
`integral` (**N**/**S**). Todo o resto — inclusive a `fundamentacao_integral`,
byte a byte — é idêntico, e o texto compartilhado diz "com proventos
integrais (cálculo por média)".

Nenhum dispositivo vinculado (`art-5-par-4`, `art-5-par-6-inc-ii`,
`art-5-par-7-inc-ii`, `cf88/art-40-par-5/ec-103-2019`) faz a
integralidade dos proventos depender do sexo. O § 4º diferencia por sexo
**idade e tempo de contribuição**; o § 6º, II define a base de cálculo sem
mencionar sexo.

Ou seja: das duas, uma está errada, e a conferência mostra por que a
pergunta é decidível — basta que o auditor determine qual valor o par
deveria compartilhar. É o achado mais acionável do lote.

### 5.7 Um dia descoberto entre `regra-0053`/`0054` e `regra-0057`/`0058`

`regra-0053`/`0054` (magistério, art. 5º, § 6º, I) gravam
`data_adm_ate: 31/12/2003`. `regra-0057`/`0058` (magistério, art. 5º, § 6º,
II) gravam `data_adm_apos: 01/01/2004`.

Sob a semântica confirmada (`ATE` inclusivo, `APOS` exclusivo), a primeira
cobre até 31/12/2003 e a segunda a partir de **02/01/2004**. O servidor
admitido em **01/01/2004** não é coberto por nenhuma das duas. É exatamente
o padrão `ATE_anterior + 1 dia = APOS_seguinte` que
[`semantica-das-janelas-temporais.md`](semantica-das-janelas-temporais.md)
§1.1 identifica como a convenção **incorreta**.

O par não-magistério equivalente (0051/0052 versus 0055/0056) não tem o
problema — porque 0055/0056 não usam o complemento (§5.3). O buraco existe
só onde o complemento foi aplicado.

### 5.8 `regra-0091` e `regra-0092`: janela que fecha em 2003, redação vinculada de 2019

As duas vinculam `cf88/art-40-par-1-inc-iii/ec-103-2019`
(`vigencia_inicio: 2019-11-13`) e gravam `data_direito_apos: 16/12/1998`,
`data_direito_ate: 31/12/2003`. A redação vinculada **não existia** durante
nenhum dia da janela de direito da regra — nasce quase dezesseis anos depois
de ela fechar.

O vínculo é fiel ao campo (a fundamentação diz "artigo 40, § 1°, inciso III,
segunda parte, da Constituição Federal, com a redação dada pela Emenda
Constitucional nº 103/2019"), então **não é vínculo a remover**. É a
fundamentação que junta três normas de três épocas — a redação de 2019, o
art. 8º da EC 20/1998 e o art. 4º da ECE 146/2021 — para uma regra cuja
janela de direito é 1998–2003. A articulação, que é o que a fundamentação
deveria ser, não se sustenta cronologicamente.

Note-se o contraste com o subgrupo A: nas regras da ECE 146/2021 a mesma
citação da "segunda parte" do inciso III **fecha** — é ela que habilita o
Estado a fixar idade mínima por emenda à própria Constituição, e é
precisamente isso que a ECE 146/2021 faz. O mesmo vínculo é coerente num
subgrupo e anacrônico no outro. Isso também contrasta com a
[conferência da invalidez](conferencia-criterio-dispositivo-invalidez-0006-0009.md)
§1, onde o inciso III não fundava critério nenhum: aqui, no benefício certo,
ele funda.

### 5.9 Três dispositivos vinculados cujo texto crítico não está no corpus

| dispositivo                              | vinculado por | o que falta                                                                                                 |
| ---------------------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------- |
| `ec-20-1998/art-8/original`              | 0091, 0092    | o corpo termina em "quando o servidor, cumulativamente:" — os requisitos da transição não estão transcritos |
| art. 8º da ECE 146/2021 (*caput*)        | — (só os §§)  | os incisos das faixas de exposição; o *caput* não é dispositivo autorado                                    |
| arts. 5º e 6º da ECE 146/2021 (*caputs*) | — (só os §§)  | os incisos de idade, tempo e pedágio                                                                        |

Os *caputs* dos arts. 5º, 6º e 8º **aparecem** no corpus, transcritos como
contexto dentro dos docs dos seus §§ — mas sempre parando na abertura da
enumeração. A transcrição sob demanda funcionou como projetada: transcreveu-se
o que foi citado. A consequência é que os critérios de habilitação de 18
das 29 regras deste lote não são conferíveis contra texto legal nenhum
dentro do repositório.

### 5.10 Em seis regras o `sexo` é critério que o dispositivo funda e o campo não grava

`regra-0087` a `regra-0092` têm `sexo` vazio. Mas as alíneas vinculadas
distinguem expressamente: "trinta e cinco anos de serviço, **se homem**, e
trinta, **se mulher**" (art. 40, III, "a", original); "trinta anos [...] **se
professor**, e vinte e cinco, **se professora**" (alínea "b"); "sessenta anos
de idade e trinta e cinco de contribuição, **se homem**" (art. 40, § 1º, III,
"a", EC 20/1998).

Nas 23 regras restantes do lote, `sexo` é o eixo que separa cada par. Nestas
seis, o mesmo critério — fundado pelo mesmo tipo de dispositivo — está vazio.
A detecção `P9_CAMPOS_VAZIOS_PENDENTES` já o registra (`achado-0008`); o que
a conferência acrescenta é que o vazio **não** é "critério inexistente": o
dispositivo vinculado o parametriza, e o cadastro é que não o grava.

### 5.11 `regra-0087`: `data_direito_ate: 01/12/2002` sem fonte no corpus

Nenhuma das duas alíneas vinculadas tem data. A redação original do art. 40
da CF/88 é substituída pela EC 20/1998 em **16/12/1998**, que é o que
`regra-0088` grava para o mesmo regime. `01/12/2002` não corresponde a
nenhuma `vigencia_inicio` ou `vigencia_fim` de nenhuma norma do corpus, e a
conferência não encontrou dispositivo que a explique.

### 5.12 `regra-0089`: a fundamentação proporcional cita a alínea integral

Os dois campos de fundamentação de `regra-0089` são idênticos e citam ambos
"Art 40, §1º, III, alinea 'a' da CF com redação da EC 20/98".

Lido o corpus: a alínea "a" da redação da EC 20/1998 fixa "sessenta anos de
idade e trinta e cinco de contribuição, se homem, e cinqüenta e cinco anos de
idade e trinta de contribuição, se mulher" — sem qualificar os proventos. É a
**alínea "b"** da mesma redação que diz "sessenta e cinco anos de idade, se
homem, e sessenta anos de idade, se mulher, **com proventos proporcionais ao
tempo de contribuição**". Essa alínea "b" **está autorada no corpus**
(`cf88/art-40-par-1-inc-iii-al-b/ec-20-1998`) e não é vinculada por regra
nenhuma deste lote.

Duas leituras, e a conferência não escolhe: ou a `FUNDAMENTACAO_PROPORCIONAL`
aponta para a alínea errada, ou `regra-0089` não tem variante proporcional e
o campo foi preenchido por cópia do integral. **Não é vínculo a acrescentar**
— a alínea "b" não é citada em campo nenhum da regra, e acrescentá-la
repetiria o erro corrigido na conferência anterior. É uma pergunta sobre o
campo deployable.

### 5.13 `regra-0092` é "(Magistério)" sem citar nada de magistério

`regra-0091` e `regra-0092` diferem em três campos: `nome`, `simulavel`
(S/N) e `apos_especial` (N/S). A `fundamentacao_integral` é **byte a byte
idêntica** e não menciona professor, magistério ou redução de requisitos; os
`dispositivos:` são os mesmos três.

Compare-se com os outros três pares de magistério do subgrupo D, onde a
distinção é fundada e vinculada: 0088 vincula a alínea "b" (magistério);
0090 acrescenta a `cf88/art-40-par-5/ec-20-1998` (redução de cinco anos). A
0092 não acrescenta nada. O critério que a distingue da 0091 — o único
motivo de ela existir — não tem dispositivo, nem citação, nem texto.

### 5.14 O § 8º do art. 40 existe no corpus, é citado por quatro regras e não é vinculado por nenhuma

`cf88/art-40-par-8/ec-41-2003` está autorado ("É assegurado o reajustamento
dos benefícios para preservar-lhes, em caráter permanente, o valor real") e
é citado pela `fundamentacao_integral` de `regra-0039`, `0040`, `0093` e
`0094` — "artigo 40, §§ 3º e 8º com redação dada pela Emenda Constitucional
nº 41/2003". O § 3º não está transcrito.

O `achado-0011` já registra por que o vínculo não é declarado: a oração
nomeia apenas a norma **alteradora**, e a norma **dona** do art. 40 não
aparece — atribuí-lo à CF seria supor pelo contexto. **A conferência
confirma a recusa e não propõe o vínculo.** O que ela acrescenta são duas
coisas.

Primeira: a decisão pendente no `achado-0011` **não é simétrica entre as
quatro regras**. Em 0039/0040 o critério `paridade: N` já é fundado por
dispositivo vinculado — `lce-432-2008/art-62/original`, com redação
equivalente à do § 8º e citado no mesmo campo. Em 0093/0094 **não é**: o
único vínculo é a alínea "a", que nada diz sobre reajuste, de modo que
`paridade: N` e `tipo_calculo: Valor Médio` ficam sem nenhum dispositivo. A
mesma pendência é redundante num par e determinante no outro.

Segunda: o `achado-0011` lista em `regras_afetadas` apenas
`regra-0039` e `regra-0093`. As respectivas gêmeas femininas — `regra-0040`
e `regra-0094` — carregam a `fundamentacao_integral` **byte a byte
idêntica** e têm a mesma omissão. O achado alcança metade dos casos que
descreve.

### 5.15 `regra-0093` e `regra-0094`: um prazo de implementação gravado no eixo de admissão

As duas gravam `data_adm_ate: 31/12/2024` **e** `data_direito_ate: 31/12/2024`.
O prazo de 31/12/2024 que aparece na única norma capaz de o fixar — o art. 4º
da ECE 146/2021 — é prazo de **cumprimento dos requisitos**, não de
**ingresso no serviço público**: "desde que sejam cumpridos até 31 de
dezembro de 2024". Nada no corpus condiciona a admissão a essa data.

Não afirmo que seja erro: `data_adm_ate: 31/12/2024` pode estar sendo usado
como "sem restrição de admissão", à maneira da sentinela. Registro que o
valor coincide com um prazo cuja fonte se aplica ao outro eixo, e que a
regra também grava `data_direito_ate: 31/12/2024` — o que torna a
coincidência conferível.

## Resumo por categoria

**Dispositivos vinculados que não fundam critério nenhum:** nenhum. Ao
contrário da conferência da invalidez, todo vínculo declarado neste lote
funda pelo menos um critério da regra que o declara — inclusive o art. 40,
§ 1º, III (EC 103/2019), que aqui está no benefício certo. A ressalva é
`regra-0091`/`0092`, onde o vínculo funda o critério mas é anacrônico em
relação à janela da própria regra (§5.8).

**Critérios sem dispositivo:**

| critério                                       | regras                    | §          |
| ---------------------------------------------- | ------------------------- | ---------- |
| idade mínima, tempo de contribuição, pedágio   | 0043–0058, 0068–0070 (19) | 5.1        |
| `tabelapontuacao: S`                           | 0051–0058 (8)             | 5.1        |
| faixa de exposição a agentes nocivos           | 0068–0070 (3)             | 5.9        |
| requisitos da transição da EC 20/1998          | 0091, 0092                | 5.9        |
| `sexo` (subgrupo A)                            | 0043–0050                 | subgrupo A |
| `paridade: S`                                  | 0087–0092                 | subgrupo D |
| `paridade: N` e `Valor Médio`                  | 0093, 0094                | 5.14       |
| magistério                                     | 0092                      | 5.13       |
| requisitos de idade/tempo (art. 22 da LCE 432) | 0039, 0040                | subgrupo E |

**Divergências entre valor gravado e dispositivo citado:**

| divergência                                        | regras                                                                   | §        |
| -------------------------------------------------- | ------------------------------------------------------------------------ | -------- |
| `data_direito_ate` versus o prazo de 31/12/2024    | 0039, 0040, 0091, 0092                                                   | 5.2      |
| `data_adm_ate` versus a vigência da Emenda         | 0049, 0050 (14/06/2021); 0057, 0058 (09/09/2021); 0055, 0056 (sentinela) | 5.3, 5.4 |
| `integral: N` com texto "proventos integrais"      | 0039, 0040, 0057                                                         | 5.5      |
| `integral` divergindo por sexo no mesmo par        | 0057, 0058                                                               | 5.6      |
| dia 01/01/2004 descoberto                          | 0053/0054 × 0057/0058                                                    | 5.7      |
| redação vinculada posterior à janela               | 0091, 0092                                                               | 5.8      |
| `data_direito_ate: 01/12/2002` sem fonte           | 0087                                                                     | 5.11     |
| fundamentação proporcional citando alínea integral | 0089                                                                     | 5.12     |
| prazo de implementação no eixo de admissão         | 0093, 0094                                                               | 5.15     |

## Pontos em aberto

1. **A norma dona do "art. 4° da Emenda à Constituição Estadual - CF"
   (0093/0094) não foi determinada, e não a determinei.** O prazo de
   31/12/2024 gravado nas duas coincide com o art. 4º da ECE 146/2021, e
   `regra-0091`/`0092` — que nomeiam a emenda por extenso — vinculam esse
   artigo. Coincidência de data não é identificação de norma: é exatamente o
   tipo de inferência plausível que o leitor por regex produzia. Fica em
   aberto.

2. **A hipótese de faixas de exposição no `achado-0006` (0068–0070) não foi
   confirmada.** A conferência mostra onde a resposta estaria — os incisos
   do *caput* do art. 8º da ECE 146/2021 — e que ela não está no corpus. Se
   as faixas se confirmarem, o grupo `P2_IGUALDADE_MATERIAL_ATIVA` é lacuna
   de schema (três regras legitimamente distintas que o catálogo não
   consegue expressar), não duplicação; se não, é repetição de origem. A
   transcrição do *caput* decide.

3. **A relação entre `tabelapontuacao` e os arts. 5º/6º da ECE 146/2021 não
   é conferível hoje.** O campo é `S` em todo o subgrupo B e `N` em todo o
   subgrupo A, o que sugere que só o art. 5º institui pontuação — mas
   nenhum dos §§ vinculados dos dois artigos a menciona, e os *caputs* não
   estão transcritos. A única confirmação possível no lote é a do art. 8º,
   § 1º ("somatório de pontos"), e essa fecha.

4. **A opção do § 16 do art. 40 da CF não tem coluna no Sisprev** e é o que
   separa os incisos I e II dos §§ 6º/2º (§5.3). Se a leitura correta for a
   das 0047/0048 e 0055/0056 (sobreposição deliberada), o catálogo tem duas
   regras indistinguíveis por servidor admitido antes de 2003 — e isso é
   parente próximo da **Q6**: um critério real que nenhuma coluna registra.

5. **Qual dos dois valores de `integral` o par 0057/0058 deveria
   compartilhar** (§5.6). A conferência mostra que os dois não podem estar
   ambos certos; não escolhe qual, porque é campo deployable.

6. **Se o padrão do §5.1 é defeito ou convenção.** Dezenove regras cujas
   fundamentações nomeiam os §§ de cálculo e reajuste mas não o dispositivo
   de requisitos: pode ser uma convenção de redação do IPERON (o § remete ao
   *caput* por "nos termos do disposto neste artigo") ou uma omissão
   sistemática. A distinção decide se há dezenove correções a fazer no
   produto ou nenhuma.

7. **`simulavel` divide um par idêntico** (0091 = `S`, 0092 = `N`) sem que
   nenhum dispositivo o explique. Não é critério jurídico e a conferência
   não o alcança — registro por ser a única divergência do par além do
   magistério do §5.13.
