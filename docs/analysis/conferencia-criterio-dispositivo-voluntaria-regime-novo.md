# Conferência `critério → dispositivo` — aposentadoria voluntária no regime novo (LCE 1.100/2021), 24 regras

> **Nota:** Relatório gerado por IA como apoio à decisão. **Não é artefato
> oficial**, não edita nenhuma `regra-*.md`, nenhum `achado-*.md`, nenhum
> dispositivo, não altera schema, dados derivados
> (`data/regras-sisprev.csv`), motor ou `site/`. É a segunda aplicação da
> conferência descrita na RFC 0008 §5 — para cada critério da regra, qual
> dispositivo o funda —, agora sobre as 24 regras de aposentadoria
> voluntária fundadas na LCE 1.100/2021. Toda conclusão sobre citação ou
> sobre valor gravado é ato humano, em achado próprio.

## O método, e o erro que ele já cometeu uma vez

A RFC 0008 §5 registra que a fundamentação **articula** os dispositivos de
modo a fundamentar **cada** critério da regra. A relação é
`critério → dispositivo(s)`; `dispositivos:` é a união achatada dela.
Conferir é desachatar.

Duas perguntas que **não coincidem**, e confundi-las já produziu proposta
errada nesta série (ver a seção "Um erro desta conferência" em
[`conferencia-criterio-dispositivo-invalidez-0006-0009.md`](conferencia-criterio-dispositivo-invalidez-0006-0009.md)):

1. *"qual dispositivo funda este critério?"* — jurídica, é o que a
   conferência responde;
2. *"o que este campo cita?"* — de leitura, é o que `dispositivos:` registra.

Um `dispositivos:` afirma "a fundamentação desta regra **cita** esta
provisão", nunca "a regra se funda nela". Por isso, aqui, **antes de
qualquer observação sobre vínculo**, foram lidos os três campos
`fundamentacao`, `fundamentacao_integral` e `fundamentacao_proporcional` das
24 regras, e o texto verbatim de todos os dispositivos citados.

O resultado desse passo já é uma conclusão, e vale adiantá-la: **não há um
único vínculo a acrescentar ou a remover nas 24 regras** (§5.8). O que a
conferência encontrou está inteiramente do outro lado — em **valores
gravados que contradizem o dispositivo que a própria regra cita**, e, em
onze regras, que contradizem **o próprio texto da fundamentação**.

## 1. O que as 24 têm em comum

Todas: `tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO`,
`atualmente_no_sistema: TRUE`, `validado_pge: FALSE`,
`validado_presidencia: FALSE`, `simulavel: S`, `tipo: CIVIL`,
`tipo_remun: ''`, `tabelapontuacao: N`, `requisitos_da_in_no_5_2020: N`,
`relatorio_p_reserva_remunerada_por_idade_ex_officio: N`,
`adicional_inatividade: N`, `fundamentacao_proporcional: ''`,
`visivel_dtc_proporcional: N`, `visivel_dtc_integral: N`.

Todas vinculam `cf88/art-40-par-1-inc-iii/ec-103-2019` e pelo menos um
artigo da LCE 1.100/2021. Nenhuma tem corpo (`# Estado da análise`), nenhuma
está `revisada`.

### 1.1 A articulação-padrão, e por que ela é o eixo de toda a conferência

Lida a LCE 1.100/2021 no corpus, as 24 regras compõem sempre a **mesma
articulação de quatro camadas**:

| camada                       | dispositivo                                                            | critério que funda                                             |
| ---------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------- |
| sede constitucional          | `cf88/art-40-par-1-inc-iii/ec-103-2019`                                | o benefício é aposentadoria voluntária por idade e tempo       |
| habilitação da especialidade | `cf88/art-40-par-5`, `par-4a`, `par-4b`, `par-4c` (EC 103/2019)        | autoriza a LC estadual a fixar idade/tempo diferenciados       |
| requisitos                   | `lce-1100-2021/art-32`, `art-33`, `art-34`, `art-35`, `art-41-inc-iii` | quem faz jus, e sob que requisitos                             |
| **trilho de cálculo**        | **`art-25` + `art-27-inc-i`** ou **`art-24` + `art-27-inc-ii`**        | **janela de admissão, `tipo_calculo` e `paridade` de uma vez** |

A quarta camada é a descoberta principal desta conferência. Os dois trilhos
não são só modos de cálculo: cada um **carrega dentro de si um corte de data
de admissão**, no texto verbatim.

**Trilho da integralidade** (`art. 25` + `art. 27, I`):

> Art. 25. Os proventos de aposentadoria do servidor público que tenha
> ingressado no serviço público em cargo efetivo **até 31 de dezembro de
> 2003** [...] corresponderá à **totalidade da remuneração no cargo
> efetivo** em que se der a aposentadoria.

> Art. 27. [...] I - de acordo com o disposto no art. 7° da Emenda
> Constitucional n° 41 [...] para aposentadorias concedidas a servidor
> público que tenha ingressado no serviço público em cargo efetivo **até 31
> de dezembro de 2003** [...]

**Trilho da média** (`art. 24` + `art. 27, II`):

> Art. 24. No cálculo dos proventos de aposentadoria dos servidores [...]
> que tenham ingressado no serviço público em cargo efetivo **após 31 de
> dezembro de 2003** [...] será considerada a **média aritmética simples
> das maiores remunerações** [...] correspondentes a 80% [...]

> Art. 27. [...] II - **nos termos estabelecidos para o RGPS**, para as
> aposentadorias concedidas a servidor público que tenha ingressado no
> serviço público em cargo efetivo **após 31 de dezembro de 2003** [...]

Logo, **escolher o trilho é decidir três campos ao mesmo tempo**:
`data_adm_ate`/`data_adm_apos`, `tipo_calculo` e `paridade`. É o análogo,
aqui, do que o art. 6º-A da EC 41/2003 era na conferência da invalidez — um
dispositivo que funda três critérios e que o achatamento em lista esconde.

E é por isso que a conferência morde: se o trilho fixa três campos, então
**um trilho e um valor de campo podem discordar**, e discordam. Muito.

## 2. O que distingue as 24 entre si

`trilho` = par de dispositivos de cálculo vinculado. `esp.` = dispositivos
da especialidade (`apos_especial: S`). Datas sem a hora `00:00`.

| regra | sexo  | esp. (CF + LCE)          | trilho   | `data_adm_apos` | `data_adm_ate` | `data_direito_apos` | `data_direito_ate` | `paridade` | `integral` | `tipo_calculo`              |
| ----- | ----- | ------------------------ | -------- | --------------- | -------------- | ------------------- | ------------------ | ---------- | ---------- | --------------------------- |
| 0035  | M     | — (`apos_especial: N`)   | 25/27-I  | 01/01/1950      | 31/12/2003     | 18/10/2021          | 31/12/2099         | S          | S          | Remuneração de Contribuição |
| 0036  | F     | —                        | 25/27-I  | 01/01/1950      | 31/12/2003     | 18/10/2021          | 31/12/2099         | S          | S          | Remuneração de Contribuição |
| 0037  | M     | —                        | 24/27-II | 01/01/1910      | 31/12/2099     | 18/10/2021          | 31/12/2099         | N          | S          | Valor Médio                 |
| 0038  | F     | —                        | 24/27-II | 01/01/1910      | 31/12/2099     | 18/10/2021          | 31/12/2099         | N          | S          | Valor Médio                 |
| 0041  | M     | § 5º + art. 33           | 25/27-I  | 01/01/1950      | 31/12/2003     | 18/10/2021          | 31/12/2099         | S          | S          | Remuneração de Contribuição |
| 0042  | F     | § 5º + art. 33           | 25/27-I  | 01/01/1950      | 31/12/2003     | 18/10/2021          | 31/12/2099         | S          | S          | Remuneração de Contribuição |
| 0059  | F     | § 4º-A + art. 35 (MOD.)  | 25/27-I  | 01/01/1950      | 31/12/2099     | 18/10/2021          | 31/12/2099         | N          | S          | Valor Médio                 |
| 0060  | M     | § 4º-A + art. 35 (MOD.)  | 25/27-I  | 01/01/1950      | 31/12/2099     | 18/10/2021          | 31/12/2099         | N          | S          | Valor Médio                 |
| 0061  | F     | § 4º-A + art. 35 (GRAVE) | 25/27-I  | 01/01/1950      | 31/12/2099     | 18/10/2021          | 31/12/2099         | N          | S          | Valor Médio                 |
| 0062  | M     | § 4º-A + art. 35 (GRAVE) | 25/27-I  | 01/01/1950      | 31/12/2099     | 18/10/2021          | 31/12/2099         | N          | S          | Valor Médio                 |
| 0063  | F     | § 4º-A + art. 35 (LEVE)  | 25/27-I  | 01/01/1950      | 31/12/2099     | 18/10/2021          | 31/12/2099         | N          | S          | Valor Médio                 |
| 0064  | M     | § 4º-A + art. 35 (LEVE)  | 25/27-I  | 01/01/1950      | 31/12/2099     | 18/10/2021          | 31/12/2099         | N          | S          | Valor Médio                 |
| 0065  | AMBOS | § 4º-C + art. 41, III    | 25/27-I  | 01/01/1950      | 31/12/2099     | **31/12/2003**      | 31/12/2099         | S          | S          | Valor Médio                 |
| 0066  | AMBOS | § 4º-C + art. 41, III    | 25/27-I  | 01/01/1950      | 31/12/2099     | **31/12/2003**      | 31/12/2099         | S          | S          | Valor Médio                 |
| 0067  | AMBOS | § 4º-C + art. 41, III    | 25/27-I  | 01/01/1950      | 31/12/2099     | **31/12/2003**      | 31/12/2099         | S          | S          | **Valor Efetivo**           |
| 0071  | AMBOS | § 4º-C + art. 41, III    | 24/27-II | 01/01/1950      | **31/12/2003** | 18/10/2021          | 31/12/2099         | N          | S          | Valor Médio                 |
| 0080  | M     | § 4º-B + art. 34         | 24/27-II | **31/12/2003**  | 31/12/2099     | 18/10/2021          | 31/12/2099         | N          | S          | Valor Médio                 |
| 0081  | F     | § 4º-B + art. 34         | 24/27-II | **31/12/2003**  | 31/12/2099     | 18/10/2021          | 31/12/2099         | N          | S          | Valor Médio                 |
| 0082  | M     | § 4º-B + art. 34         | 25/27-I  | 01/01/1950      | 31/12/2003     | 18/10/2021          | 31/12/2099         | S          | S          | Remuneração de Contribuição |
| 0083  | F     | § 4º-B + art. 34         | 25/27-I  | 01/01/1950      | 31/12/2003     | 18/10/2021          | 31/12/2099         | S          | S          | Remuneração de Contribuição |
| 0095  | M     | § 5º + art. 33           | 25/27-I  | 01/01/1950      | **31/12/2024** | **31/12/2003**      | **31/12/2024**     | N          | S          | Valor Médio                 |
| 0096  | F     | § 5º + art. 33           | 25/27-I  | 01/01/1950      | **31/12/2024** | **31/12/2003**      | **31/12/2024**     | N          | S          | Valor Médio                 |
| 0107  | M     | § 5º + art. 33           | 25/27-I  | 01/01/1950      | 31/12/2099     | **31/12/2003**      | **31/12/2024**     | N          | **N**      | Valor Médio                 |
| 0108  | F     | § 5º + art. 33           | 25/27-I  | 01/01/1950      | 31/12/2099     | **31/12/2003**      | **31/12/2024**     | N          | **N**      | Valor Médio                 |

Cinco subgrupos por especialidade: **comum** (0035–0038, `apos_especial: N`),
**magistério** (0041/0042, 0095/0096, 0107/0108), **deficiência**
(0059–0064), **agentes nocivos** (0065–0067, 0071) e **policial**
(0080–0083).

## 3. A conferência, por subgrupo

Nas cinco tabelas abaixo, os critérios comuns às 24 aparecem só na primeira
e são referidos depois.

### 3.1 Voluntária comum — 0035/0036 (integralidade) e 0037/0038 (média)

| critério                                | valor                         | fundado por                                                                | fecha?          |
| --------------------------------------- | ----------------------------- | -------------------------------------------------------------------------- | --------------- |
| tipo de benefício                       | voluntária por idade/tempo    | `cf88/art-40-par-1-inc-iii/ec-103-2019` + `lce-1100-2021/art-32` (*caput*) | ✅              |
| idade mínima                            | *não parametrizada*           | § 1º, III, 2ª parte **delega à emenda à Constituição estadual** — ver §5.5 | ⚠️ sem provisão |
| tempo de contribuição                   | *não parametrizado*           | incisos do art. 32, **não transcritos** — ver §5.5                         | ⚠️ sem provisão |
| `sexo: MASCULINO`/`FEMININO`            | dois registros                | § 1º, III distingue por sexo **só na 1ª parte** (União, 62/65) — ver §5.4  | ❌              |
| `apos_especial: N`                      | sem especialidade             | nenhum § 4º-A/4º-B/4º-C/5º é citado                                        | ✅ por ausência |
| `data_adm_ate: 31/12/2003` (0035/0036)  | ingresso até 31/12/2003       | `art-25` e `art-27-inc-i` — "até 31 de dezembro de 2003", literal          | ✅              |
| janela de admissão (0037/0038)          | **nenhuma** (duas sentinelas) | `art-24`/`art-27-inc-ii` exigem "**após** 31 de dezembro de 2003"          | ❌ ver §5.1     |
| `tipo_calculo` (0035/0036)              | Remuneração de Contribuição   | `art-25` — "totalidade da remuneração no cargo efetivo"                    | ✅ (ver §5.7)   |
| `tipo_calculo: Valor Médio` (0037/0038) | média das 80% maiores         | `art-24`                                                                   | ✅              |
| `paridade: S` (0035/0036)               | com paridade                  | `art-27-inc-i` — reajuste pelo art. 7º da EC 41/2003                       | ✅              |
| `paridade: N` (0037/0038)               | sem paridade                  | `art-27-inc-ii` — reajuste nos termos do RGPS                              | ✅              |
| `data_direito_apos: 18/10/2021`         | direito a partir da LCE       | vigência da LCE 1.100/2021 (marco autorado em `lce-1100-2021/norma.md`)    | ✅              |
| `integral: S`                           | proventos integrais           | *nenhum* — nem `art-26` (proporcionalidade) é citado                       | ✅ por ausência |

Este é o subgrupo mais limpo: **0035/0036 fecham inteiramente** no eixo do
trilho, e são o gabarito contra o qual os demais foram lidos. 0037/0038
fecham em cálculo e paridade e **falham na janela** (§5.1).

Um ganho lateral: a pendência `LEITURA-HUMANA` de `regra-0037` na
[lista congelada](pendencias-de-citacao-congeladas.md) (`sem_norma (1×)`) é
o campo `fundamentacao: "Art. 24 da Lei Complementar 1.100 de 18 de outubro de 2021"`. Lido por humano, a norma é inequívoca — LCE 1.100/2021, art. 24,
**já vinculado**. A pendência é fechável por leitura, sem vínculo novo.

### 3.2 Magistério — 0041/0042, 0095/0096, 0107/0108

| critério                             | valor                           | fundado por                                                                    | fecha?             |
| ------------------------------------ | ------------------------------- | ------------------------------------------------------------------------------ | ------------------ |
| especialidade (`apos_especial: S`)   | professor                       | `cf88/art-40-par-5/ec-103-2019` (redução de 5 anos) + `lce-1100-2021/art-33`   | ✅                 |
| exercício exclusivo em magistério    | *não parametrizado*             | `art-33` — "comprove tempo de efetivo exercício, **exclusivamente**"           | ⚠️ aferição manual |
| trilho (todas as seis)               | `art-25` + `art-27-inc-i`       | integralidade + paridade                                                       | —                  |
| `data_adm_ate: 31/12/2003` (0041/42) | ingresso até 31/12/2003         | `art-25`/`art-27-inc-i`, literal                                               | ✅                 |
| `data_adm_ate: 31/12/2024` (0095/96) | ingresso até 31/12/2024         | **nenhum dispositivo citado fixa 31/12/2024**                                  | ❌ ver §5.6        |
| `data_adm_ate: 31/12/2099` (0107/08) | sentinela                       | `art-25`/`art-27-inc-i` exigem o corte de 31/12/2003                           | ❌ ver §5.1        |
| `data_direito_ate: 31/12/2024`       | prazo (0095/96, 0107/08)        | **nenhum dispositivo citado**                                                  | ❌ ver §5.6        |
| `data_direito_apos: 31/12/2003`      | 0065–0067, 0095–0096, 0107–0108 | nenhum dispositivo citado é de 2003 — todos são de 2019/2021                   | ❌ ver §5.6        |
| `paridade`/`integral`/`tipo_calculo` | S/S/Rem. Contrib. (0041/42)     | `art-25` + `art-27-inc-i`                                                      | ✅                 |
| idem                                 | N/S/Valor Médio (0095/96)       | trilho vinculado é o `art-25`+`27-I`                                           | ❌ ver §5.2        |
| idem                                 | N/**N**/Valor Médio (0107/08)   | trilho vinculado é o `art-25`+`27-I`; e o texto diz "integralidade e paridade" | ❌ ver §5.2        |

**As seis compartilham `dispositivos:` idêntico e fundamentação quase
idêntica** — a de 0041/0042 e a de 0107/0108 é **byte-a-byte a mesma
string** — e produzem três combinações de resultado diferentes. O critério
que as separaria (a janela em que o direito se implementa) não é fundado por
provisão nenhuma que elas citem.

### 3.3 Servidor com deficiência — 0059–0064

| critério                                   | valor                                     | fundado por                                                                               | fecha?             |
| ------------------------------------------ | ----------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------ |
| especialidade                              | servidor com deficiência                  | `cf88/art-40-par-4a/ec-103-2019` + `lce-1100-2021/art-35` (*caput*)                       | ✅                 |
| avaliação biopsicossocial                  | *não parametrizada*                       | `art-35` *caput* — "previamente submetido à avaliação biopsicossocial"                    | ⚠️ aferição manual |
| 10 anos serviço + 5 no cargo               | *não parametrizado*                       | `art-35` *caput*, literal                                                                 | ⚠️ aferição manual |
| **grau (GRAVE/MODERADA/LEVE)**             | só no `nome`                              | incisos I/II/III do art. 35, **não transcritos**                                          | ❌ ver §5.3        |
| trilho                                     | `art-25` + `art-27-inc-i`                 | integralidade + paridade                                                                  | —                  |
| `data_adm_ate: 31/12/2099`                 | sentinela                                 | `art-25`/`art-27-inc-i` exigem ingresso até 31/12/2003                                    | ❌ ver §5.1        |
| `paridade: N`, `tipo_calculo: Valor Médio` | média, sem paridade                       | trilho vinculado é o da integralidade; **o próprio texto diz "integralidade e paridade"** | ❌ ver §5.2        |
| `fundamentacao` (só 0061/0062)             | "Art. 39, parágrafo único da LC 432/2008" | `lce-432-2008/art-39/original` é **auxílio-reclusão**                                     | ❌ ver §5.5        |

### 3.4 Exposição a agentes nocivos — 0065, 0066, 0067, 0071

| critério                                  | valor                       | fundado por                                                                          | fecha?                             |
| ----------------------------------------- | --------------------------- | ------------------------------------------------------------------------------------ | ---------------------------------- |
| especialidade                             | exposição a agentes nocivos | `cf88/art-40-par-4c/ec-103-2019` + `lce-1100-2021/art-41-inc-iii`                    | ✅                                 |
| 20 anos serviço + 5 no cargo              | *não parametrizado*         | `art-41` *caput*, literal                                                            | ⚠️ aferição manual                 |
| **86 pontos + 25 anos de exposição**      | *não parametrizado*         | `art-41-inc-iii`, literal — **o inciso está transcrito**                             | ⚠️ ver §5.7                        |
| `tabelapontuacao: N`                      | sem tabela de pontuação     | o dispositivo vinculado **é** uma regra de pontos                                    | ❌ ver §5.7                        |
| `sexo: AMBOS`                             | sem distinção               | `art-41` é neutro quanto a sexo (soma de idade + tempo)                              | ✅                                 |
| trilho (0065/0066/0067)                   | `art-25` + `art-27-inc-i`   | integralidade + paridade                                                             | —                                  |
| `paridade: S` (0065–0067)                 | com paridade                | `art-27-inc-i`                                                                       | ✅                                 |
| `tipo_calculo: Valor Médio` (0065/66)     | média                       | trilho vinculado é o `art-25` (totalidade da remuneração); texto diz "integralidade" | ❌ ver §5.2                        |
| `tipo_calculo: Valor Efetivo` (0067)      | ?                           | `art-25` — se "Valor Efetivo" designar a remuneração do cargo efetivo, **fecha**     | ⚠️ ver §5.7                        |
| `data_direito_apos: 31/12/2003` (0065–67) | direito desde 2003          | todos os dispositivos citados são de 2019/2021                                       | ❌ ver §5.6                        |
| trilho (0071)                             | `art-24` + `art-27-inc-ii`  | média, sem paridade                                                                  | ✅ com `paridade: N`/`Valor Médio` |
| `data_adm_ate: 31/12/2003` (0071)         | ingresso **até** 31/12/2003 | `art-24`/`art-27-inc-ii` exigem ingresso **após** 31/12/2003                         | ❌ **invertido**, §5.1             |

### 3.5 Policial civil — 0080/0081 (média) e 0082/0083 (integralidade)

| critério                                | valor                           | fundado por                                                          | fecha?      |
| --------------------------------------- | ------------------------------- | -------------------------------------------------------------------- | ----------- |
| especialidade                           | policial / agente               | `cf88/art-40-par-4b/ec-103-2019` + `lce-1100-2021/art-34` (*caput*)  | ✅          |
| requisitos de idade e tempo             | *não parametrizados*            | incisos do art. 34, **não transcritos**                              | ⚠️ ver §5.5 |
| `sexo: MASCULINO`/`FEMININO`            | dois registros por trilho       | `art-34` *caput*: "os seguintes requisitos, **para ambos os sexos**" | ❌ ver §5.4 |
| `data_adm_apos: 31/12/2003` (0080/0081) | ingresso após 31/12/2003        | `art-24`/`art-27-inc-ii`, literal                                    | ✅          |
| `data_adm_ate: 31/12/2003` (0082/0083)  | ingresso até 31/12/2003         | `art-25`/`art-27-inc-i`, literal                                     | ✅          |
| `paridade`/`tipo_calculo` (0080/0081)   | N / Valor Médio                 | `art-27-inc-ii` / `art-24`                                           | ✅          |
| `paridade`/`tipo_calculo` (0082/0083)   | S / Remuneração de Contribuição | `art-27-inc-i` / `art-25`                                            | ✅          |

**Os quatro registros de policial são, junto com 0035/0036 e 0041/0042, os
únicos do grupo em que trilho e janela de admissão fecham nos dois sentidos**
— e são os únicos quatro do grupo em que a janela é gravada nos **dois**
eixos de forma complementar (0080/0081 abrem em 31/12/2003 onde 0082/0083
fecham em 31/12/2003, exatamente a convenção `ATE_anterior = APOS_seguinte`
confirmada em
[`semantica-das-janelas-temporais.md`](semantica-das-janelas-temporais.md)
§1.1). Isso confirma, por conferência independente, o "✅ Match limpo" que
[`reconciliacao-policial.md`](reconciliacao-policial.md) §2 já registrava
para 0080–0083 contra a análise da PGE.

## 4. Um contraponto honesto à conferência anterior

Na conferência da invalidez, `cf88/art-40-par-1-inc-iii` estava vinculado às
quatro regras e **não fundava critério nenhum** — porque o inciso III trata
de aposentadoria voluntária por idade, e aquelas eram de invalidez.

Aqui é o oposto: as 24 regras **são** de aposentadoria voluntária por idade
e tempo, e o inciso III é a sede constitucional exata do benefício. Ele
funda o critério `tipo_de_beneficio` em todas as 24. É o mesmo dispositivo,
o mesmo vínculo, e o veredito se inverte — o que só a pergunta
`critério → dispositivo` distingue. A leitura textual do vínculo, sozinha,
daria o mesmo resultado nos dois casos.

Duas ressalvas registradas para não estender isso além do que fecha:

- a "**segunda parte**" que 20 das 24 fundamentações recortam **existe** e é
  a que alcança o RPPS estadual ("no âmbito dos Estados [...] na idade
  mínima estabelecida mediante emenda às respectivas Constituições e Leis
  Orgânicas"). As 67 entradas `ESTREITADA` da lista congelada estão
  corretas: o vínculo é da provisão inteira e a resolução perdida é a que
  esta conferência recupera em prosa;
- `tipo_de_beneficio` grava "**POR TEMPO DE CONTRIBUIÇÃO**", enquanto o
  inciso III e os `nome` das regras dizem "**por idade e tempo de
  contribuição**". Estender o domínio do enum é alterar o Sisprev, **fora do
  escopo** — registro só que o rótulo do enum é mais estreito que o critério
  que ele nomeia.

## 5. O que a conferência revelou

### 5.1 O trilho de cálculo carrega uma janela de admissão — e 14 das 24 a gravam em desacordo com o dispositivo que citam

Este é o achado central. Aplicando §1.1 às 24:

| situação                                                                 | regras                                                           | nº     |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------- | ------ |
| ✅ janela coincide com o corte do trilho                                 | 0035, 0036, 0041, 0042, 0080, 0081, 0082, 0083                   | **8**  |
| ❌ trilho `25`+`27-I` ("até 31/12/2003") e **nenhum corte gravado**      | 0059, 0060, 0061, 0062, 0063, 0064, 0065, 0066, 0067, 0107, 0108 | **11** |
| ❌ trilho `24`+`27-II` ("após 31/12/2003") e **nenhum corte gravado**    | 0037, 0038                                                       | **2**  |
| ❌ trilho `24`+`27-II` e corte gravado **invertido** (`ate: 31/12/2003`) | 0071                                                             | **1**  |
| ⚠️ trilho `25`+`27-I` e corte em 31/12/2024 (não 31/12/2003)             | 0095, 0096                                                       | **2**  |

O caso mais nítido é a **regra-0071**: ela vincula `art-24` e
`art-27-inc-ii`, cujos textos dizem "ingressado [...] **após** 31 de
dezembro de 2003", e grava `data_adm_ate: 31/12/2003`, isto é, "admitido
**até** 31/12/2003". A regra seleciona exatamente o conjunto de servidores
que os dois dispositivos que ela cita excluem. Sua irmã de trilho no mesmo
subgrupo (0065–0067, trilho da integralidade) tampouco grava o corte
complementar, de modo que **as quatro regras de agentes nocivos não
particionam a população por data de admissão** — uma cobre quem ingressou
até 2003 com cálculo de quem ingressou depois, e três cobrem todo mundo com
o cálculo de quem ingressou até 2003.

Registro a favor da prudência: `31/12/2099`, `01/01/1950` e `01/01/1910` são
**sentinelas não interpretadas** (P5). Este documento não as lê como "sem
limite" — lê apenas que **não são o marco 31/12/2003** que os dispositivos
citados declaram, e que oito regras do mesmo grupo, com o mesmo trilho,
gravam esse marco. A comparação é entre regras do próprio grupo, não contra
uma interpretação da sentinela.

### 5.2 Onze regras gravam resultado contrário à sua própria fundamentação

Aqui não é preciso sequer chegar ao dispositivo: o campo **deployable**
`fundamentacao_integral` afirma em texto o que os campos `paridade`,
`tipo_calculo` e `integral` contradizem na mesma regra.

| regras         | o texto da `fundamentacao_integral` diz                                  | os campos gravam                               | campos em conflito |
| -------------- | ------------------------------------------------------------------------ | ---------------------------------------------- | ------------------ |
| 0059–0064 (6)  | "proventos integrais (**cálculo por integralidade**) e **com paridade**" | `paridade: N`, `tipo_calculo: Valor Médio`     | 2                  |
| 0065, 0066 (2) | idem                                                                     | `tipo_calculo: Valor Médio` (`paridade: S` ✅) | 1                  |
| 0107, 0108 (2) | idem                                                                     | `paridade: N`, `Valor Médio`, `integral: N`    | 3                  |
| 0067 (1)       | idem                                                                     | `tipo_calculo: Valor Efetivo`                  | ver §5.7           |

E as onze **também** contradizem o trilho vinculado, que é o da
integralidade (`art-25` + `art-27-inc-i`) em todas elas. São três fontes
concordando entre si — o texto da fundamentação, o art. 25 e o art. 27, I —
contra os campos gravados.

O caso de 0107/0108 é o mais forte porque tem **gêmeas exatas**: a
`fundamentacao_integral` de 0041/0042 e a de 0107/0108 são a **mesma string,
byte a byte**, e as duas famílias vinculam os **mesmos cinco dispositivos**.
0041/0042 gravam `S`/`S`/`Remuneração de Contribuição` — que é o que o texto
diz. 0107/0108 gravam `N`/`N`/`Valor Médio` — que é o oposto, nos três
campos. Uma das duas famílias está errada, e a fundamentação idêntica não
tem como distinguir qual.

Nota: 0107/0108 declaram `integral: N` com `fundamentacao_proporcional`
vazia, o que o `P9_INTEGRAL_SEM_FUNDAMENTACAO` já detecta e o
[`achado-0009`](../../okf/regras-sisprev/achados/achado-0009.md) já registra.
O que a conferência acrescenta é que a fundamentação **integral** delas
afirma o contrário do `integral: N`.

### 5.3 Em três dos quatro subgrupos especiais, o critério que define a especialidade não tem dispositivo

`apos_especial: S` em 20 das 24. O dispositivo que **habilita** a
especialidade está vinculado em todas — mas o que **a mede** só está
transcrito num subgrupo:

| subgrupo        | habilitação (vinculada)                     | critério concreto                 | transcrito?                    |
| --------------- | ------------------------------------------- | --------------------------------- | ------------------------------ |
| magistério      | `cf88/art-40-par-5` + `lce/art-33`          | exercício exclusivo em magistério | ✅ art. 33 está inteiro        |
| deficiência     | `cf88/art-40-par-4a` + `lce/art-35`         | grau (grave/moderada/leve)        | ❌ incisos I/II/III do art. 35 |
| agentes nocivos | `cf88/art-40-par-4c` + `lce/art-41-inc-iii` | 86 pontos + 25 anos de exposição  | ✅ o inciso está transcrito    |
| policial        | `cf88/art-40-par-4b` + `lce/art-34`         | idade e tempo diferenciados       | ❌ incisos do art. 34          |

Os documentos de `art-32`, `art-34` e `art-35` endereçam o **artigo
inteiro** (`componentes: [artigo N]`), mas o corpo transcrito termina no
*caput*, na palavra "requisitos:"/"condições:" — os itens que seguem não
foram transcritos. Isso é legítimo sob a "decomposição sob demanda" do P3,
e a consequência é precisa: **os critérios de idade e tempo de todo o
regime permanente não estão no corpus**.

Para a deficiência isso é mais que uma pendência de transcrição: o
`P2_IGUALDADE_MATERIAL_ATIVA` detecta 0059≡0063 e 0060≡0064
([`achado-0003`](../../okf/regras-sisprev/achados/achado-0003.md),
[`achado-0004`](../../okf/regras-sisprev/achados/achado-0004.md)), e a
conferência mostra por que: as seis regras vinculam exatamente os mesmos
cinco dispositivos e carregam a mesma fundamentação, que cita "artigos 25,
27, I; 35" **sem inciso**. O grau existe só no `nome`.

Vale registrar por que 0061/0062 (GRAVE) escapam do P2 e 0059/0060
(MODERADA) e 0063/0064 (LEVE) não: a **única** diferença material entre o
par GRAVE e os outros dois é o campo `fundamentacao`, que em 0061/0062 diz
"Art. 39, parágrafo unico da Lei Complementar 432/2008" — a citação
problemática de §5.5. Ou seja, o que hoje distingue materialmente o grau
grave dos demais **não é o grau**: é uma citação a outra norma, sobre outro
benefício. Corrigida essa citação, os três pares colapsam.

### 5.4 O art. 34 diz "para ambos os sexos", e quatro regras se dividem por sexo

`sexo` é critério aferido confirmado (Q3, `docs/spec/regra.md`), e 18 das 24
regras se dividem em par masculino/feminino com fundamentação byte-idêntica.
Conferido contra o texto:

- `cf88/art-40-par-1-inc-iii` distingue por sexo **só na primeira parte**
  (União: 62 mulher / 65 homem). A segunda parte — a que alcança RO —
  delega a idade mínima à emenda à Constituição estadual, sem dizer nada
  sobre sexo;
- `art-33` (professor), `art-35` (deficiência) e `cf88/art-40-par-5` são
  **silentes** quanto a sexo;
- `art-41` (agentes nocivos) é neutro por construção (soma de pontos) — e,
  coerentemente, as quatro regras do subgrupo gravam `sexo: AMBOS`;
- `art-34` (policial) é o único **explícito**, e explícito no sentido
  contrário: "[...] desde que observados, cumulativamente, os seguintes
  requisitos, **para ambos os sexos**". As quatro regras de policial deste
  grupo mesmo assim se dividem em M/F, com fundamentação idêntica.

Silêncio não é o mesmo que vedação, e os incisos não transcritos do art. 34
poderiam, em tese, reintroduzir a distinção. Mas a cláusula "para ambos os
sexos" está no *caput*, governando os incisos, e é a única afirmação
positiva sobre sexo em todo o material vinculado pelas 24 regras. Registro,
como contraponto, que a própria matriz to-be da PGE-RO mantém o desdobramento
por sexo nas hipóteses permanentes P1–P4
([`reconciliacao-policial.md`](reconciliacao-policial.md) §1) **com a mesma
base legal nas duas linhas** — isto é, também sem apresentar o dispositivo
que funda o desdobramento. **A conferência não conclui**: aponta que o
critério `sexo` está parametrizado em 18 regras e que nenhuma provisão
vinculada por elas o funda, e uma o contraria.

### 5.5 Critérios sem dispositivo, e um dispositivo sobre outro benefício

Três lacunas, de naturezas diferentes:

1. **A idade mínima do regime permanente não está no corpus.** O § 1º, III,
   2ª parte manda buscá-la "mediante emenda às respectivas Constituições" —
   isto é, na Constituição do Estado de Rondônia, alterada pela ECE
   146/2021. O vocabulário de normas tem `ece-146-2021`, mas nenhum
   dispositivo dela é vinculado por qualquer das 24, e a Constituição
   estadual não é norma do vocabulário. **Nenhuma das 24 regras cita a
   provisão que fixa a idade mínima que elas aferem.** Isso não é vínculo
   faltando (a fundamentação de fato não a cita) — é a fundamentação que
   está incompleta em relação aos seus próprios critérios, o que é
   exatamente o que a quinta pergunta da P13.1 existe para expor.

2. **Os requisitos numéricos dos arts. 32, 34 e 35 não estão transcritos**
   (§5.3). Diferente de (1), esta é pendência de transcrição, mecanicamente
   destravável.

3. **`regra-0061` e `regra-0062` citam o art. 39, parágrafo único, da LCE
   432/2008.** O artigo 39 dessa lei **está transcrito no corpus**, na
   redação original, e é sobre **auxílio-reclusão**:

   > Art. 39. O auxílio-reclusão do segurado, servidor ativo, será concedido
   > ao conjunto de seus dependentes, a contar da data em que o segurado
   > preso deixa de perceber vencimentos [...]

   O parágrafo único citado não está transcrito (é uma das três pendências
   `TRANSCREVER` da lista congelada), então **não afirmo o que ele diz**. O
   que a conferência constata é: (a) o artigo que o contém governa
   auxílio-reclusão, benefício distinto do que 0061/0062 concedem; (b) a
   LCE 432/2008 tem `vigencia_fim: 2021-10-18`, e 0061/0062 têm
   `data_direito_apos: 18/10/2021` — a norma citada deixa de vigorar
   exatamente no dia em que a janela da regra abre; (c) é essa citação, e
   não o grau de deficiência, que hoje separa materialmente 0061/0062 de
   0059/0060/0063/0064 (§5.3). Transcrever o parágrafo único fecha a
   pendência formal; a conferência de mérito é humana.

### 5.6 Sete regras gravam limites temporais que dispositivo citado nenhum estabelece

| valor        | campo               | regras                 | dispositivo citado que o fixe |
| ------------ | ------------------- | ---------------------- | ----------------------------- |
| `31/12/2003` | `data_direito_apos` | 0065, 0066, 0067       | nenhum                        |
| `31/12/2003` | `data_direito_apos` | 0095, 0096, 0107, 0108 | nenhum                        |
| `31/12/2024` | `data_direito_ate`  | 0095, 0096, 0107, 0108 | nenhum                        |
| `31/12/2024` | `data_adm_ate`      | 0095, 0096             | nenhum                        |

As sete vinculam apenas dispositivos da EC 103/2019 (13/11/2019) e da LCE
1.100/2021 (18/10/2021). `31/12/2003` é o marco da EC 41/2003 — norma que
nenhuma das sete cita — e as outras 17 regras do grupo gravam `18/10/2021`
nesse mesmo campo, coerentemente com a vigência da LCE que fundamenta todas.

`31/12/2024` é o **prazo do art. 4º da ECE 146/2021** ("desde que sejam
cumpridos até 31 de dezembro de 2024"), transcrito no corpus. E o `nome` de
0095/0096 diz literalmente "c/c art. 4º da EC 146/21". Mas a
`fundamentacao_integral` de 0095/0096 **não cita o art. 4º** — cita § 5º,
arts. 25, 27, I, 33 e § 1º, III, 2ª parte, exatamente como 0041/0042 e
0107/0108. Portanto:

**Não proponho vincular `ece-146-2021/art-4/original` a nenhuma das sete.**
`dispositivos:` registra o que a fundamentação cita, e ela não o cita. É
precisamente o erro corrigido na conferência da invalidez, e a tentação aqui
é maior porque o `nome` aponta o dispositivo e as datas batem com o prazo
dele. O que a conferência entrega é a disjunção, não a escolha: **ou a
`fundamentacao_integral` de 0095/0096 está incompleta** (o `nome` e as três
datas indicam que a articulação passa pelo art. 4º, e o texto perdeu isso),
**ou as datas estão erradas**. Decidir é ato humano.

Isso reencontra, pelo lado do fundamento, o item 08 da §5.2 de
[`semantica-das-janelas-temporais.md`](semantica-das-janelas-temporais.md)
("`31/12/2024` — o maior grupo sem marco. Qual norma fixa 31/12/2024?"). A
resposta candidata é o art. 4º da ECE 146/2021, e o que faltava para
confirmá-la não era a norma: era saber se a regra a cita.

Um contraste que fecha o argumento: 0095/0096 e 0107/0108 gravam
`data_direito_ate: 31/12/2024` **sem citar** o art. 4º; as `regra-0068`–`0070`
(agentes nocivos, ECE 146/2021 art. 8º) citam e vinculam a ECE 146 e gravam
`data_direito_ate: 31/12/2099`. Os dois lados do catálogo trocaram de lugar.

### 5.7 Duas divergências de enum, nenhuma resolvível dentro do escopo

**`tabelapontuacao: N` nas quatro regras de agentes nocivos.** O art. 41 é
uma regra de pontos, e o inciso vinculado é literalmente um limiar: "86
(oitenta e seis) pontos e 25 (vinte e cinco) anos de efetiva exposição". No
mesmo catálogo, as `regra-0068`, `0069` e `0070` — versão transitória do
mesmo benefício, fundada no art. 8º da ECE 146/2021, também por pontos —
gravam `tabelapontuacao: S`. As quatro do art. 41 gravam `N`. Não sei o que
o campo significa operacionalmente no Sisprev (se é "usa tabela de
pontuação" ou "usa a tabela progressiva de transição"), então **não concluo
que esteja errado** — registro que o mesmo critério jurídico recebe valores
opostos em regras irmãs.

**`Valor Efetivo` × `Remuneração de Contribuição` × `Valor Médio`.** Três
valores do enum aparecem no grupo para duas situações jurídicas. As
regras 0035/0036, 0041/0042 e 0082/0083 usam `Remuneração de Contribuição`
para o art. 25 (integralidade); `regra-0067` usa `Valor Efetivo` para o
mesmo art. 25. Se `Valor Efetivo` designar "totalidade da remuneração no
cargo **efetivo**", então **0067 é a única das três regras de agentes
nocivos do trilho da integralidade que fecha**, e 0065/0066 (`Valor Médio`)
é que estão erradas — o inverso da leitura ingênua, que trataria 0067 como
a exceção. Não decido: depende do significado dos valores do enum no
Sisprev, que é domínio do sistema, não do catálogo.

Registro adjacente, sem proposta: o rótulo `Remuneração de Contribuição`
descreve, ao pé da letra, a base do **art. 24** ("remunerações utilizadas
como base para as **contribuições**"), não a do art. 25 ("totalidade da
remuneração no **cargo efetivo**"), que é onde ele é de fato usado. Se
alguma das inversões de §5.2 tiver origem em leitura do rótulo, esta é a
explicação mais econômica. Alterar o domínio do enum é alterar o Sisprev —
fora do escopo.

### 5.8 Nenhum vínculo a acrescentar ou remover — nas 24

Conferido campo a campo (`fundamentacao`, `fundamentacao_integral`,
`fundamentacao_proporcional`) contra `dispositivos:` nas 24 regras:

- **toda** provisão listada em `dispositivos:` é citada por algum campo de
  fundamentação da própria regra — inclusive
  `cf88/art-40-par-1-inc-iii/ec-103-2019`, que aqui, ao contrário do caso da
  invalidez, também **funda** critério;
- **toda** provisão citada nos campos está vinculada, com duas exceções
  corretas: `lce-432-2008/art-39-par-unico` (0061/0062), não transcrito, e a
  redação da ECE 146/2021 que o `nome` de 0095/0096 menciona **e a
  fundamentação não cita** (§5.6);
- `fundamentacao_proporcional` está vazia nas 24, logo não contribui com
  citação nenhuma — o que exclui, por construção, o modo de erro específico
  cometido na conferência da 0006.

As 31 pendências da lista congelada que tocam este grupo são 28
`ESTREITADA` (nada a fazer — a resolução perdida é a prosa desta
conferência), 2 `TRANSCREVER` (0061/0062, §5.5) e 1 `LEITURA-HUMANA`
(0037, fechável por leitura, §3.1). Nenhuma é `REDACAO` ou `SEGMENTAR`.

## 6. Pontos em aberto

Nenhum item abaixo é conclusão; são as decisões que a conferência deixa
formuladas para autoria humana em achado próprio.

01. **A inversão da janela na `regra-0071`** — trilho `art. 24`/`art. 27, II`
    ("após 31/12/2003") com `data_adm_ate: 31/12/2003`. Corrige-se a data ou
    o trilho? Idem para as 13 outras regras da tabela de §5.1.

02. **As onze regras que contradizem a própria `fundamentacao_integral`**
    (§5.2). Prevalece o texto (integralidade + paridade) ou os campos (média,
    sem paridade)? A decisão é diferente por subgrupo: em 0107/0108 há
    gêmeas com fundamentação byte-idêntica e resultado oposto (0041/0042), o
    que sugere que uma das duas famílias foi criada por cópia; em 0059–0064
    as seis erram no mesmo sentido, o que sugere origem única.

03. **A idade mínima do regime permanente** (§5.5.1): qual dispositivo da
    Constituição do Estado, na redação da ECE 146/2021, a fixa? A norma
    precisa entrar no vocabulário antes que qualquer vínculo seja possível.

04. **Transcrever os incisos dos arts. 32, 34 e 35 da LCE 1.100/2021** — sem
    eles, os critérios de idade, tempo e grau de deficiência não têm
    provisão a que se referir (§5.3). É a pendência com maior efeito
    destravante do grupo.

05. **`lce-432-2008/art-39-par-unico`** (0061/0062): transcrever e conferir.
    Se o parágrafo único acompanhar o *caput* no assunto (auxílio-reclusão),
    a citação é estranha ao benefício — e a distinção material do grau GRAVE
    desaparece junto com ela (§5.3, §5.5.3).

06. **A disjunção do art. 4º da ECE 146/2021** em 0095/0096 e 0107/0108
    (§5.6): fundamentação incompleta ou datas erradas? Fecha o item 08 de
    `semantica-das-janelas-temporais.md` §5.2 num sentido ou no outro.

07. **`data_direito_apos: 31/12/2003`** em 0065/0066/0067 (§5.6): as outras
    17 regras do grupo gravam `18/10/2021`. Erro de origem, ou há norma
    anterior que a fundamentação não cita?

08. **`sexo` em 18 das 24** (§5.4): qual provisão funda o desdobramento? Em
    particular, como se concilia com "para ambos os sexos" do art. 34 nas
    0080–0083? A resposta muda a leitura de nove pares P1/P2 deste grupo.

09. **Semântica dos valores de `tipo_calculo`** (§5.7): `Valor Efetivo` é
    integralidade? Se for, 0067 fecha e 0065/0066 não; se não for, o inverso.

10. **`tabelapontuacao`** (§5.7): o que o campo significa, e por que as
    regras do art. 41 (pontos) gravam `N` enquanto as do art. 8º da ECE
    146/2021 (pontos) gravam `S`?

11. **As duplicatas do grupo**, já detectadas e com achado aberto:
    0059≡0063 e 0060≡0064 ([`achado-0003`](../../okf/regras-sisprev/achados/achado-0003.md),
    [`achado-0004`](../../okf/regras-sisprev/achados/achado-0004.md)) e
    0065≡0066 ([`achado-0005`](../../okf/regras-sisprev/achados/achado-0005.md)).
    A conferência não as resolve, mas mostra que a primeira dupla é lacuna
    de expressão (o grau existe na lei, não no catálogo) e a segunda não —
    0065 e 0066 têm o mesmo `nome`, a mesma fundamentação e nenhum critério
    jurídico as separando.

## 7. Referências

- RFC 0008 §5 (`critério → dispositivo` como conferência humana, sem campo
  nem gate),
  [`docs/rfc/0008-traducao-sem-perdas-entre-os-dois-esquemas.md`](../rfc/0008-traducao-sem-perdas-entre-os-dois-esquemas.md)
- Spec P13.1, quinta pergunta, [`docs/spec/regra.md`](../spec/regra.md)
- Contrato do dispositivo, [`docs/spec/dispositivo.md`](../spec/dispositivo.md)
- [`conferencia-criterio-dispositivo-invalidez-0006-0009.md`](conferencia-criterio-dispositivo-invalidez-0006-0009.md)
  — a primeira aplicação, e o erro que ela registra
- [`semantica-das-janelas-temporais.md`](semantica-das-janelas-temporais.md)
  §1 (semântica confirmada), §5.2 item 08 (`31/12/2024`)
- [`reconciliacao-policial.md`](reconciliacao-policial.md) §1–§2
  (0080–0083 as-is × to-be da PGE)
- [`pendencias-de-citacao-congeladas.md`](pendencias-de-citacao-congeladas.md)
  (filas `ESTREITADA`, `TRANSCREVER`, `LEITURA-HUMANA` deste grupo)
