# Conferência `critério → dispositivo` — regras 0023 a 0034 (compulsória e por idade)

> **Nota:** Relatório gerado por IA como apoio à decisão. **Não é artefato
> oficial**, não edita nenhuma `regra-*.md`, nenhum `achado-*.md`, nenhum
> dispositivo, não altera schema, dados derivados
> (`data/regras-sisprev.csv`), motor ou `site/`. É a segunda aplicação da
> conferência descrita na RFC 0008 §5 — para cada critério da regra, qual
> dispositivo o funda —, agora sobre as doze regras de aposentadoria
> compulsória e por idade. Toda conclusão sobre citação é ato humano, em
> achado próprio.

## O método, e a distinção que ele exige

A RFC 0008 §5 registra que a fundamentação **articula** os dispositivos de
modo a fundamentar **cada** critério da regra. Logo a relação real é
`critério → dispositivo(s)`, e `dispositivos:` é a união achatada dela.
Conferir é desachatar.

Duas perguntas diferentes convivem aqui e **não coincidem**:

1. *"qual dispositivo funda este critério?"* — jurídica, é o que a
   conferência responde;
2. *"o que este campo cita?"* — de leitura, é o que `dispositivos:` registra.

Um `dispositivos:` afirma *"a fundamentação desta regra **cita** esta
provisão"*, nunca "a regra se funda nela". A seção final de
[`conferencia-criterio-dispositivo-invalidez-0006-0009.md`](conferencia-criterio-dispositivo-invalidez-0006-0009.md)
registra o erro concreto que confundir as duas produz; este documento
mantém a separação e, por isso, **não propõe nenhum vínculo novo nem
nenhuma remoção**.

Todo texto legal citado abaixo foi lido em `okf/dispositivos/`, não de
memória.

## Correção do recorte

O grupo foi encomendado como "compulsória: 0023, 0024, 0025, 0027, 0028,
0029 / por idade: 0026, 0030, 0031, 0032, 0033, 0034". Conferido contra o
campo `tipo_de_beneficio` de cada uma, o recorte correto é outro — a
partição é 6 × 6, mas com membros diferentes:

- **`APOSENTADORIA COMPULSÓRIA`**: 0023, 0025, 0027, 0030, 0031, 0032
- **`APOSENTADORIA POR IDADE`**: 0024, 0026, 0028, 0029, 0033, 0034

O padrão do catálogo é alternado nos quatro primeiros (0023 compulsória,
0024 idade, 0025 compulsória, 0026 idade) e depois em pares.

## As doze, lado a lado

Idêntico nas doze: `tipo: CIVIL`, `atualmente_no_sistema: TRUE`,
`ciclo_de_validacao: 2º`, `validado_pge: FALSE`,
`validado_presidencia: FALSE`, `tipo_remun: ''`, `tabelapontuacao: N`,
`requisitos_da_in_no_5_2020: N`,
`relatorio_p_reserva_remunerada_por_idade_ex_officio: N`,
`adicional_inatividade: N`, `visivel_dtc_proporcional: N`,
`visivel_dtc_integral: N` e — nas doze — `fundamentacao: ''`.

O campo genérico `fundamentacao` está vazio em todas: tudo mora em
`fundamentacao_proporcional` (dez regras) ou em `fundamentacao_integral`
(0033/0034), nunca nos dois.

O que varia:

| regra | benefício   | simulável | esp.  | sexo      | parid. | integral  | `tipo_calculo`                | admissão (após → até) | direito (após → até)  | campo usado  | disp. |
| ----- | ----------- | --------- | ----- | --------- | ------ | --------- | ----------------------------- | --------------------- | --------------------- | ------------ | ----- |
| 0023  | compulsória | N         | N     | *(vazio)* | S      | *(vazio)* | Não identificado              | 01/01/1910→16/12/1998 | 01/01/1910→16/12/1998 | proporc.     | 1     |
| 0024  | idade       | N         | N     | *(vazio)* | S      | *(vazio)* | Não identificado              | 01/01/1910→16/12/1998 | 01/01/1910→16/12/1998 | proporc.     | 1     |
| 0025  | compulsória | N         | N     | *(vazio)* | S      | *(vazio)* | Não identificado              | 01/01/1910→31/12/2003 | 16/12/1998→31/12/2003 | proporc.     | **0** |
| 0026  | idade       | N         | N     | *(vazio)* | S      | *(vazio)* | Não identificado              | 01/01/1910→31/12/2003 | 16/12/1998→31/12/2003 | proporc.     | 1     |
| 0027  | compulsória | S         | N     | AMBOS     | N      | N         | Proporcionalidade Dias        | 01/01/1950→31/12/2099 | 31/12/2003→03/12/2015 | proporc.     | 6     |
| 0028  | idade       | S         | N     | MASCULINO | N      | N         | Proporcionalidade Dias        | 01/01/1950→31/12/2099 | 31/12/2003→31/12/2024 | proporc.     | 4     |
| 0029  | idade       | S         | N     | FEMININO  | N      | N         | Proporcionalidade Dias        | 01/01/1950→31/12/2099 | 31/12/2003→31/12/2024 | proporc.     | 4     |
| 0030  | compulsória | S         | N     | MASCULINO | N      | N         | Proporcionalidade Dias        | 01/01/1950→31/12/2099 | 04/12/2015→31/12/2024 | proporc.     | 6     |
| 0031  | compulsória | S         | N     | FEMININO  | N      | N         | Proporcionalidade Dias        | 01/01/1950→31/12/2099 | 04/12/2015→31/12/2024 | proporc.     | 6     |
| 0032  | compulsória | S         | N     | AMBOS     | N      | N         | Tipo Cálculo Nova Previdência | 01/01/1950→31/12/2099 | 18/10/2021→31/12/2099 | proporc.     | 6     |
| 0033  | idade       | S         | **S** | MASCULINO | N      | N         | Valor Médio                   | 01/01/1950→31/12/2099 | 18/10/2021→31/12/2099 | **integral** | 5     |
| 0034  | idade       | S         | **S** | FEMININO  | N      | N         | Valor Médio                   | 01/01/1950→31/12/2099 | 18/10/2021→31/12/2099 | **integral** | 5     |

Quatro sub-famílias saltam da tabela:

- **A — estratos históricos** (0023, 0024, 0025, 0026): `simulavel: N`,
  `sexo`/`integral` vazios, `tipo_calculo: Não identificado`,
  `paridade: S`, uma única citação constitucional cada, sem nenhuma norma
  estadual. São o registro do regime anterior, não regras operacionais.
- **B — compulsória operacional** (0027, 0030, 0031, 0032).
- **C — voluntária por idade operacional** (0028, 0029).
- **D — voluntária por idade do servidor com deficiência** (0033, 0034),
  as duas únicas com `apos_especial: S` e as duas únicas cuja fundamentação
  está no campo integral.

## A conferência

### A — os quatro estratos históricos (0023, 0024, 0025, 0026)

Cada uma cita exatamente uma provisão da CF, no campo proporcional.

| regra | critério            | valor gravado         | fundado por                                                                                        | fecha? |
| ----- | ------------------- | --------------------- | -------------------------------------------------------------------------------------------------- | ------ |
| 0023  | benefício           | compulsória           | `cf88/art-40-inc-ii/original` — "compulsoriamente, aos setenta anos de idade"                      | ✅     |
| 0023  | idade-limite (70)   | **não há campo**      | mesma provisão — a idade está no texto, não no cadastro                                            | ⚠️     |
| 0023  | proporcionalidade   | `integral` vazio      | mesma provisão — "com proventos proporcionais ao tempo de serviço"                                 | ⚠️     |
| 0023  | janela de direito   | → 16/12/1998          | vigência da redação seguinte (`…al-b/ec-20-1998`, `vigencia_inicio: 1998-12-16`)                   | ✅     |
| 0024  | benefício           | por idade             | `cf88/art-40-inc-iii-al-d/original` — "voluntariamente: […] aos sessenta e cinco anos de idade"    | ✅     |
| 0024  | idade (65 H / 60 M) | `sexo` vazio          | mesma provisão — "se homem […] e aos sessenta, se mulher"                                          | ⚠️     |
| 0025  | benefício           | compulsória           | art. 40, § 1º, II, redação da EC 20/1998 — **não autorado**, nada vinculado                        | ❌     |
| 0026  | benefício           | por idade             | `cf88/art-40-par-1-inc-iii-al-b/ec-20-1998` — "voluntariamente […] sessenta e cinco anos de idade" | ✅     |
| 0026  | idade (65 H / 60 M) | `sexo` vazio          | mesma provisão — "se homem, e sessenta anos de idade, se mulher"                                   | ⚠️     |
| 0026  | proporcionalidade   | `integral` vazio      | mesma provisão — "com proventos proporcionais ao tempo de contribuição"                            | ⚠️     |
| 0026  | janela de direito   | 16/12/1998→31/12/2003 | `vigencia_inicio: 1998-12-16` da própria redação vinculada                                         | ✅     |
| todas | `paridade: S`       | S                     | **nenhum dispositivo citado trata de reajuste**                                                    | ❌     |
| todas | `tipo_calculo`      | Não identificado      | nenhuma das provisões fixa método de cálculo                                                       | ✅     |

**A 0026 é a regra mais limpa do grupo.** A pergunta encomendada — o que a
alínea "b" de fato dizia — tem resposta direta no corpus: *"sessenta e
cinco anos de idade, se homem, e sessenta anos de idade, se mulher, com
proventos proporcionais ao tempo de contribuição"*, precedida pelo caput do
inciso III, que exige "tempo mínimo de dez anos de efetivo exercício no
serviço público e cinco anos no cargo efetivo". É aposentadoria voluntária
por idade, proporcional — exatamente o benefício da regra, exatamente o
campo (`fundamentacao_proporcional`) em que a citação está. A vigência
autorada (16/12/1998 → 12/11/2019) contém integralmente a janela de direito
gravada. **O vínculo fecha em todos os eixos**, e é o único do catálogo
para esse dispositivo.

O `⚠️` de `sexo`/`integral` não é acusação: é a observação de que a resposta
que o `achado-0008` procura ("o campo vazio é lapso ou é semanticamente
significativo?") está, para estas quatro, **escrita no dispositivo que a
própria regra já cita**. Nas quatro o texto diz "proventos proporcionais";
em 0024 e 0026 o texto distingue idades por sexo sem restringir o benefício
a um sexo. Decidir o preenchimento é ato humano — a conferência só mostra
onde a resposta está.

### B — compulsória operacional (0027, 0030, 0031, 0032)

Duas articulações distintas, e é aqui que a conferência produz o achado
mais forte do grupo. Primeiro cada uma isolada.

**0027** (direito 31/12/2003 → 03/12/2015):

| critério                      | valor                   | fundado por                                                                          | fecha? |
| ----------------------------- | ----------------------- | ------------------------------------------------------------------------------------ | ------ |
| benefício                     | compulsória             | `cf88/art-40-par-1-inc-ii/ec-88-2015` + `lce-432-2008/art-21-par-1` (caput: 70 anos) | ⚠️ §1  |
| idade-limite                  | **não há campo**        | CF diz "70 […] ou 75 […] na forma de lei complementar"; LCE 432, art. 21, diz 70     | ⚠️ §1  |
| automaticidade / termo        | **não há campo**        | `lce-432-2008/art-21-par-1` — "automática […] a partir do dia imediato"              | ⚠️ §5  |
| `tipo_calculo: Proporc. Dias` | fração em dias          | `lce-432-2008/art-17` (§ 2º: "em número de dias")                                    | ✅     |
| base de cálculo               | —                       | `lce-432-2008/art-45/lce-672-2012` (média das 80% maiores), via art. 17, § 1º        | ✅     |
| `paridade: N`                 | reajuste por valor real | `lce-432-2008/art-62` — lista o art. 21, que é a compulsória                         | ✅     |
| `sexo: AMBOS`                 | AMBOS                   | nenhuma provisão distingue por sexo                                                  | ✅     |
| janela de direito (fim)       | 03/12/2015              | nenhum dispositivo vinculado fixa essa data                                          | ❌ §3  |
| aplicabilidade pós-2021       | —                       | `ece-146-2021/art-4`                                                                 | ⚠️ §3  |

A cadeia `art. 17 → art. 45` é o exemplo mais limpo de articulação em todo
o grupo: o art. 17, § 1º diz expressamente que a fração "será aplicada
sobre o valor dos proventos calculado conforme art. 45". Um dispositivo
funda o *método* (fração em dias) e o outro funda a *base* (média das 80%
maiores) — e só juntos fundam o `tipo_calculo`.

**0030 e 0031** (direito 04/12/2015 → 31/12/2024):

| critério                      | valor                    | fundado por                                                                          | fecha? |
| ----------------------------- | ------------------------ | ------------------------------------------------------------------------------------ | ------ |
| benefício                     | compulsória              | `cf88/art-40-par-1-inc-ii/ec-88-2015` + `lc-152-2015/art-2` + `lce-1100-2021/art-31` | ✅     |
| idade-limite (75)             | **não há campo**         | `lc-152-2015/art-2` e `lce-1100-2021/art-31` — ambos "aos 75 (setenta e cinco) anos" | ⚠️ §1  |
| `tipo_calculo: Proporc. Dias` | fração em dias           | `lce-1100-2021/art-26` (§ 2º: "considerados em número de dias")                      | ✅     |
| base de cálculo               | —                        | `lce-1100-2021/art-24` (média das 80% maiores), via art. 26, § 1º                    | ⚠️ §7  |
| `paridade: N`                 | reajuste nos termos RGPS | `lce-1100-2021/art-27-inc-ii`                                                        | ⚠️ §7  |
| `sexo: MASCULINO`/`FEMININO`  | M / F                    | **nenhuma provisão citada distingue por sexo**                                       | ❌ §4  |
| janela de direito (fim)       | 31/12/2024               | **nenhum dispositivo vinculado fixa essa data**                                      | ❌ §3  |
| janela de direito (início)    | 04/12/2015               | LC 152/2015 não tem `vigencia_inicio` autorada                                       | ⚠️ §3  |

**0032** (direito 18/10/2021 → 31/12/2099): fundamentação **verbatim** a da
0027, salvo um preâmbulo descritivo, e `dispositivos:` **idêntico** ao da
0027 — mesmos seis vínculos, na mesma ordem.

| critério                   | valor                         | fundado por                                                                               | fecha? |
| -------------------------- | ----------------------------- | ----------------------------------------------------------------------------------------- | ------ |
| benefício                  | compulsória                   | `cf88/art-40-par-1-inc-ii/ec-88-2015` + `lce-432-2008/art-21-par-1`                       | ⚠️ §2  |
| `tipo_calculo`             | Tipo Cálculo Nova Previdência | **nenhum dispositivo vinculado**; a própria prosa da regra diz "média aritmética simples" | ❌ §5  |
| base / proporcionalidade   | —                             | `lce-432-2008/art-17` + `art-45` — `vigencia_fim: 2021-10-18`                             | ❌ §2  |
| `paridade: N`              | valor real                    | `lce-432-2008/art-62` — `vigencia_fim: 2021-10-18`                                        | ❌ §2  |
| janela de direito (início) | 18/10/2021                    | marco autorado — mas é a data em que a **LCE 432/2008 foi revogada**                      | ❌ §2  |
| janela de direito (fim)    | 31/12/2099                    | `ece-146-2021/art-4` fixa 31/12/2024, não 2099                                            | ❌ §3  |

### C — voluntária por idade (0028, 0029)

| critério                      | valor            | fundado por                                                                                           | fecha? |
| ----------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------- | ------ |
| benefício                     | por idade        | a fundamentação cita o **inciso II** (compulsória), não o III                                         | ❌ §8  |
| idade (65 H / 60 M)           | **não há campo** | nenhum dispositivo vinculado fixa idade                                                               | ❌ §8  |
| `sexo: MASCULINO`/`FEMININO`  | M / F            | nenhum dispositivo vinculado distingue por sexo                                                       | ❌ §8  |
| `tipo_calculo: Proporc. Dias` | fração em dias   | `lce-432-2008/art-17` (§ 2º)                                                                          | ✅     |
| base de cálculo               | —                | `lce-432-2008/art-45/lce-672-2012` + `lei-10887-2004/art-1` (mesma regra dos 80%)                     | ✅     |
| `paridade: N`                 | valor real       | `lce-432-2008/art-62` — lista arts. 20, 21, 22, 23, 24 e 47, **nenhum transcrito** além do 20 e do 21 | ⚠️     |
| janela de direito (fim)       | 31/12/2024       | `ece-146-2021/art-4` — citado **só no `nome`**, nunca num campo de fundamentação                      | ❌ §3  |

### D — por idade do servidor com deficiência (0033, 0034)

| critério                         | valor            | fundado por                                                                                                                     | fecha? |
| -------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------ |
| deficiência (`apos_especial: S`) | S                | `cf88/art-40-par-4a/ec-103-2019` + `lce-1100-2021/art-35` (avaliação biopsicossocial)                                           | ✅     |
| tempo mínimo (10 anos / 5 anos)  | **não há campo** | `lce-1100-2021/art-35`, caput                                                                                                   | ⚠️ §5  |
| idade                            | **não há campo** | art. 35 termina em "observadas as seguintes condições:" — **os incisos não estão transcritos**                                  | ❌ §6  |
| `sexo: MASCULINO`/`FEMININO`     | M / F            | idem — a distinção estaria nos incisos não transcritos                                                                          | ❌ §6  |
| competência para fixar a idade   | —                | `cf88/art-40-par-1-inc-iii/ec-103-2019`, 2ª parte — "na idade mínima estabelecida mediante emenda às respectivas Constituições" | ⚠️ §6  |
| `tipo_calculo: Valor Médio`      | média 80%        | `lce-1100-2021/art-24`                                                                                                          | ⚠️ §7  |
| `paridade: N`                    | termos do RGPS   | `lce-1100-2021/art-27-inc-ii`                                                                                                   | ⚠️ §7  |
| `integral: N`                    | N                | o **único** campo de fundamentação preenchido é o integral, e diz "com proventos integrais"                                     | ❌ §5  |

Note o contraste com a
[conferência da invalidez](conferencia-criterio-dispositivo-invalidez-0006-0009.md):
lá, o art. 40, § 1º, III (EC 103/2019) estava vinculado a quatro regras de
invalidez e **não fundava critério nenhum**. Aqui, em 0033/0034, a matéria
do inciso — aposentadoria voluntária por idade — é a matéria da regra, e a
"segunda parte" que a fundamentação recorta é justamente a que alcança o
RPPS estadual. O vínculo é pertinente. O que falta é o outro lado da
delegação: a emenda estadual que **efetivamente fixa** a idade mínima não é
citada por nenhuma das duas.

## O que a conferência revelou

### 1. A idade-limite — o critério que define a compulsória — não é campo de regra nenhuma

Aposentadoria compulsória é, em substância, uma regra sobre uma idade: 70
na CF/88 original e na LCE 432/2008; 70 **ou** 75 "na forma de lei
complementar" na redação da EC 88/2015; 75 na LC 152/2015 e no art. 31 da
LCE 1.100/2021. As seis regras compulsórias não têm **nenhum campo** que
registre esse número. Ele existe só em dois lugares: no texto legal e,
indiretamente, nos limites da janela de direito.

É o mesmo modo de falha da **Q6** na invalidez, do outro lado do catálogo:
lá o critério (causa da incapacidade) não tem coluna e o cadastro grava o
resultado (`integral`); aqui o critério (idade-limite) não tem coluna e o
cadastro grava a janela em que ele vigeu. Distinguir 70 de 75 exige ler o
`fundamentacao_proporcional` — campo de texto livre.

O mesmo vale para as seis regras por idade (65/60 na CF original e na EC
20/1998; idade estadual sob a EC 103/2019): nenhuma grava a idade, e
`sexo` funciona como proxy parcial em 0028/0029 e 0033/0034 — proxy que
não sobrevive à conferência (§4, §8).

### 2. Duas leis estaduais em posições invertidas: a 0032 funda-se no que foi revogado no primeiro dia da sua janela

Este é o achado mais consequente do grupo, e ele é **inteiramente
verificável no corpus**:

- a `regra-0032` tem `data_direito_apos: 18/10/2021` e cita quatro
  provisões da **LCE 432/2008**, todas com `vigencia_fim: 2021-10-18` — a
  janela começa exatamente no dia em que as provisões citadas deixaram de
  viger;
- as `regra-0030`/`0031` têm `data_direito_apos: 04/12/2015` e citam quatro
  provisões da **LCE 1.100/2021**, todas com `vigencia_inicio: 2021-10-18`
  — quase seis anos depois do início da janela.

Some-se a isso que as janelas **se sobrepõem**: 0030/0031 cobrem até
31/12/2024, 0032 cobre a partir de 18/10/2021. No intervalo
18/10/2021 → 31/12/2024 o mesmo benefício, para os mesmos sexos, é
fundado por duas leis estaduais mutuamente excludentes — e as duas
articulações fixam idades diferentes: 0032, via art. 21 da LCE 432, chega
a **70 anos**; 0030/0031, via LC 152/2015 e art. 31 da LCE 1.100, chegam a
**75**.

Há uma leitura que salva parte disso: o `ece-146-2021/art-4`, que a 0032
cita e vincula, é exatamente a ponte de direito adquirido — a concessão
"observará os requisitos e os critérios exigidos pela legislação vigente
até a data de entrada em vigor desta Emenda Constitucional, desde que
sejam cumpridos **até 31 de dezembro de 2024**". Sob essa leitura, citar a
LCE 432 revogada é legítimo. Mas ela deixa dois resíduos: a janela da 0032
vai até 31/12/2099, muito além do teto do próprio art. 4º; e a idade
resultante continua sendo 70, não 75.

**Uma hipótese, marcada como hipótese.** O `nome` da 0032 diz
*"Compulsória - Art. 40, §1º, II da CF com redaçao da EC 103/19 c/c art. 31
da Lc nº 1.100/2021"* — isto é, anuncia exatamente as normas que caberiam
na sua janela e que **não** estão na sua fundamentação; e a fundamentação
que ela tem é cópia literal da 0027, cuja janela é 2003–2015. A hipótese
mais econômica é que o campo tenha sido herdado da 0027 e nunca ajustado.
É hipótese: nada no repositório a prova, e a conferência não decide.

### 3. O 31/12/2024 está gravado em quatro regras que não citam a provisão que o fixa — e citado nas duas que não o gravam

O `ece-146-2021/art-4` é o **único** dispositivo autorado no corpus inteiro
que menciona 2024. A distribuição é exatamente inversa à esperada:

| regra      | grava `data_direito_ate: 31/12/2024`? | cita e vincula o art. 4º da ECE 146/2021? |
| ---------- | ------------------------------------- | ----------------------------------------- |
| 0027       | não (03/12/2015)                      | **sim**                                   |
| 0028, 0029 | **sim**                               | só no `nome`, nunca em campo deployável   |
| 0030, 0031 | **sim**                               | não                                       |
| 0032       | não (31/12/2099)                      | **sim**                                   |

O item 8 da seção 5.2 de
[`semantica-das-janelas-temporais.md`](semantica-das-janelas-temporais.md)
pergunta "qual norma fixa 31/12/2024?" para 34 limites do catálogo. Para os
quatro deste grupo a conferência responde: é o art. 4º da ECE 146/2021, e
o problema não é achar a norma — é que as regras que gravam a data não a
citam, e as que a citam não gravam a data. Enquanto for assim, nenhum
vínculo pode ser declarado nas 0028–0031 sem violar a regra de que
`dispositivos:` registra o que o campo cita.

O caso das 0028/0029 é o mais nítido: o `nome` diz *"c/c art. 4º da EC
146/21"*, a data bate com o teto do art. 4º, e o
`fundamentacao_proporcional` — que é o campo deployável de fundamentação —
não menciona a ECE 146 em lugar nenhum.

Registre-se também que o intervalo 03/12/2015 → 04/12/2015 entre 0027 e
0030/0031 já está catalogado como item 3 da seção 5.2 daquele documento
(um dia descoberto), e que a LC 152/2015 continua sem `vigencia_inicio`
autorada — sem ela, o limite 03/12/2015 da 0027 e o 04/12/2015 das
0030/0031 não podem ser conferidos contra marco nenhum.

### 4. O `sexo` de 0030/0031 não tem dispositivo que o funde

`regra-0030` e `regra-0031` são a mesma regra de compulsória partida em
`MASCULINO` e `FEMININO`. Nenhuma das seis provisões que elas vinculam
distingue por sexo: nem o art. 40, § 1º, II (EC 88/2015) — "aos 70 […] ou
aos 75 […] anos de idade" —, nem o art. 2º da LC 152/2015, nem o art. 31 da
LCE 1.100/2021, nem os arts. 24, 26 e 27, II. Aposentadoria compulsória
nunca dependeu de sexo em nenhuma redação transcrita no corpus.

As outras duas compulsórias operacionais confirmam por contraste:
`regra-0027` e `regra-0032` gravam `sexo: AMBOS` para o mesmo benefício.

Consequência para os detectores, e ela é a que a `CLAUDE.md` antecipa: a
partição por `sexo` é o que impede o `P2_IGUALDADE_MATERIAL_ATIVA` de
agrupar 0030 e 0031 (o detector só as reporta em `P1_NOME_REPETIDO`, por
terem o mesmo `nome`). Se o `sexo` dessas duas for um valor sem
fundamento, o grupo P2 que hoje não existe passaria a existir. Isso é
decisão humana sobre campo deployable, não conclusão desta conferência.

### 5. Três valores gravados que a própria fundamentação da regra contradiz

Nenhum destes depende de leitura externa — os dois lados estão dentro do
mesmo documento:

1. **`regra-0032`, `tipo_calculo: Tipo Cálculo Nova Previdência`.** O
   preâmbulo do seu próprio `fundamentacao_proporcional` diz "com proventos
   proporcionais ao tempo de contribuição (média aritmética simples)", e os
   dispositivos que ela vincula para cálculo são o art. 17 (fração em dias)
   e o art. 45 (média das 80% maiores) da LCE 432/2008. A `regra-0027`, com
   fundamentação **literalmente a mesma**, grava
   `tipo_calculo: Proporcionalidade Dias`.
2. **`regra-0033` e `regra-0034`, `integral: N`.** O único campo de
   fundamentação preenchido nas duas é o `fundamentacao_integral`, e ele
   começa com "Aposentadoria voluntária de servidor com deficiência, **com
   proventos integrais** (cálculo por média)". O `fundamentacao_proporcional`
   está vazio. O `achado-0009` registra a forma mecânica disso ("integral N
   com fundamentação proporcional vazia"); a conferência acrescenta o
   mérito: não é só que falte a fundamentação proporcional — é que a
   fundamentação existente afirma o contrário do campo.
3. **`regra-0027`, no `nome`.** O `nome` diz "Art. 40, §1º, II da CF, com
   redação dada pela EC nº 41/2003". É exatamente a atribuição que o
   `achado-0013` demonstrou não existir (o inciso II teve duas redações
   emendadas, da EC 20/1998 e da EC 88/2015, nenhuma da EC 41/2003). O
   achado registra que 0027 e 0032 "citam corretamente" a EC 88/2015 — e
   isso vale para o `fundamentacao_proporcional` das duas. O `nome` da 0027
   carrega a mesma misatribuição que o achado imputa às 0028/0029, e `nome`
   também é coluna deployable. Vale conferir junto.

Um quarto caso, de natureza diferente: o `lce-432-2008/art-21-par-1`,
vinculado por 0027 e 0032, funda um critério real — "a aposentadoria
compulsória será automática e declarada por ato, com vigência a partir do
dia imediato àquele em que o servidor atingir a idade-limite" — que
**nenhuma coluna do Sisprev registra**. Não é vínculo a remover: é a
articulação alcançando um efeito que o cadastro não representa. E o caput
do art. 21, que é onde estão os 70 anos, só aparece no corpus como
contexto dentro do documento do § 1º; nenhuma regra o vincula como
provisão.

### 6. Um critério cuja fonte o corpus não contém: os incisos do art. 35 da LCE 1.100/2021

O `lce-1100-2021/art-35/original` transcreve **apenas o caput**, que
termina em dois-pontos: "observadas as seguintes condições:". As condições
— entre elas a idade, que é o critério que faz de 0033/0034 aposentadorias
"por idade", e a eventual distinção por sexo que justifica a partição M/F —
estão nos incisos, que não estão transcritos. O `nome` das duas regras
aponta expressamente para o inciso IV.

Isto é **pendência de transcrição**, não de decisão: diferentemente do
`achado-0012`/`achado-0013`, aqui a provisão existe e o que falta é o texto.
Enquanto ele não for autorado, a conferência **se recusa a afirmar** qual é
a idade dessas duas regras, se ela difere por sexo, e se a partição
0033/0034 tem fundamento — do mesmo modo que se recusa a afirmar o
contrário.

Vale registrar que a lista congelada classifica as pendências de 0033/0034
como `ESTREITADA` (o recorte "segunda parte" do inciso III), fila que "não
exige nada". Isso está certo para o item que ela registra e é ortogonal a
este: o que falta aqui é o texto de outra provisão, de outra norma.

### 7. Dispositivos de cálculo restritos a quem ingressou após 31/12/2003, em regras cuja janela de admissão não tem esse corte

Quatro regras (0030, 0031, 0033, 0034) vinculam os arts. 24 e 27, II da
LCE 1.100/2021. Os dois textos são expressos quanto ao destinatário:

> Art. 24. No cálculo dos proventos […] dos servidores titulares de cargo
> efetivo **que tenham ingressado no serviço público em cargo efetivo após
> 31 de dezembro de 2003** e que não tenham feito a opção de que trata o
> § 16 do art. 40 da Constituição Federal […]

> Art. 27. […] II - nos termos estabelecidos para o RGPS, para as
> aposentadorias concedidas a servidor público **que tenha ingressado no
> serviço público em cargo efetivo após 31 de dezembro de 2003** […]

As quatro regras gravam `data_adm_apos: 01/01/1950` e
`data_adm_ate: 31/12/2099` — isto é, admitem qualquer data de ingresso. Os
arts. 25 e 27, I da mesma lei, que tratam de quem ingressou **até**
31/12/2003 (totalidade da remuneração; reajuste do art. 7º da EC 41/2003),
estão autorados no corpus e não são citados por nenhuma das quatro.

Duas leituras cabem, e a conferência não escolhe: ou a janela de admissão
está larga demais para a articulação que a regra declara, ou a regra
pretende alcançar também os ingressantes anteriores e, nesse caso, faltam
os dispositivos que os fundamentam. Ambas mudam campo deployable.

### 8. As 0028/0029 citam o inciso do benefício errado — e isso estreita as hipóteses do `achado-0013`

O `achado-0013` já registra que o `fundamentacao_proporcional` de 0028/0029
atribui à EC 41/2003 uma redação do art. 40, § 1º, II que ela nunca deu.
A conferência acrescenta um dado que o achado não usa: **as duas regras têm
`tipo_de_beneficio: APOSENTADORIA POR IDADE`**, e o inciso II é a
compulsória — "compulsoriamente, com proventos proporcionais ao tempo de
contribuição, aos 70 […] ou aos 75 […] anos de idade" na única redação
autorada. O `nome` das duas, por sua vez, diz *"Voluntária Comum Idade -
Art. 40, §1º, **III, "b"** da CF"*.

Ou seja: o benefício cadastrado, o `nome` e o `sexo` apontam todos para o
inciso III, alínea "b" — a provisão que a `regra-0026` cita, vincula, e que
diz exatamente "sessenta e cinco anos de idade, se homem, e sessenta anos
de idade, se mulher, com proventos proporcionais". A fundamentação aponta
para o inciso II.

Isso reforça as hipóteses 1 e 2 do `achado-0013` contra a hipótese 3: se a
menção à EC 41/2003 fosse apenas qualificação do § 1º (que ela de fato
reescreveu), restaria explicar por que uma regra de aposentadoria
voluntária por idade cita o inciso da compulsória. É pergunta para a mesma
conversa, não conclusão desta conferência.

Um efeito colateral que decorre disso e não estava registrado: as
0028/0029 têm janela de direito de 01/01/2004 a 31/12/2024, que atravessa
a EC 103/2019. A alínea "b" da EC 20/1998 — a provisão que o `nome` invoca
— tem `vigencia_fim: 2019-11-12`. Uma única regra abrange, portanto, dois
regimes constitucionais distintos do critério de idade: o federal fixo
(65/60) até 12/11/2019 e a idade mínima estadual delegada a partir de
13/11/2019.

### 9. A pendência da 0025 está na fila errada da lista congelada

A [lista congelada](pendencias-de-citacao-congeladas.md) põe a `regra-0025`
na fila `REDACAO` — "a provisão existe, a redação citada não", território
do `achado-0012`. Mas o próprio `achado-0013`, escrito depois, transcreve a
redação da EC 20/1998 do inciso II a partir do texto compilado do Planalto:

> II - compulsoriamente, aos setenta anos de idade, com proventos
> proporcionais ao tempo de contribuição; (Redação dada pela Emenda
> Constitucional nº 20, de 1998)

A redação que a 0025 cita **existe**; ela apenas não está autorada em
`okf/dispositivos/`. O rótulo da fila é mecânico — o leitor por regex não
distinguia "não autorado" de "não existe" —, e por isso a 0025 pertence de
fato à fila `TRANSCREVER`, ao lado dos três itens que a lista já identifica
como destraváveis por transcrição. É a única regra deste grupo com
`dispositivos:` vazio, e a única cujo vínculo se abre com um ato de
transcrição em vez de uma decisão jurídica.

O `achado-0013` observa, corretamente, que "autorá-la só para 'resolver'
este vínculo seria escolher pela regra qual norma ela invoca" — mas isso
vale para 0028/0029, que citam uma redação inexistente. Para a 0025 não há
escolha a fazer: a regra cita a redação da EC 20/1998 e é essa que estaria
sendo transcrita.

## Vínculos a acrescentar ou remover

**Nenhum**, nas doze regras.

Percorridos os campos `fundamentacao`, `fundamentacao_integral` e
`fundamentacao_proporcional` de cada uma, toda provisão citada que está
autorada no corpus **já está vinculada**, e toda provisão vinculada **está
citada** em algum campo de fundamentação da própria regra. As lacunas do
grupo não são de vínculo: são de transcrição (0025, incisos do art. 35),
de redação inexistente (0028/0029, `achado-0013`) e de citação que só
existe no `nome` (art. 4º da ECE 146/2021 em 0028/0029; art. 31 da LCE
1.100/2021 em 0032).

Esta seção existe porque a primeira versão da conferência da invalidez
propôs dois vínculos e ambos estavam errados, pela mesma causa: confundir
"funda o critério" com "está citado no campo". Aqui, várias provisões
fundariam critérios melhor do que as citadas — o art. 31 da LCE 1.100/2021
para a janela da 0032, a alínea "b" do inciso III para as 0028/0029, os
arts. 25 e 27, I para as janelas de admissão largas. **Nenhuma delas é
citada pelas regras em questão**, e portanto nenhuma pode ser vinculada. O
que muda isso é corrigir o campo deployable, que é ato humano.

## Pontos em aberto

01. **Qual idade-limite cada regra compulsória pretende aplicar** (70 ou
    75), já que nenhum campo a registra e a janela da 0032 é incompatível
    com a lei estadual que ela cita. Sem isso, a sobreposição
    18/10/2021 → 31/12/2024 entre 0032 e 0030/0031 não se resolve.
02. **Se as 0030/0031 e a 0032 tiveram as leis estaduais trocadas**, e se a
    fundamentação da 0032 é herança não ajustada da 0027 (§2). Hipótese, não
    conclusão.
03. **O que fixa 31/12/2024 nas 0028–0031**, dado que o único dispositivo
    autorado que fixa essa data está citado justamente nas duas regras que
    não a gravam (§3). É o item 8 da seção 5.2 de
    `semantica-das-janelas-temporais.md`, aqui respondido só em parte.
04. **A `vigencia_inicio` da LC 152/2015 e da EC 88/2015** — sem elas, nem o
    limite 03/12/2015 da 0027, nem o 04/12/2015 das 0030/0031, nem a
    anterioridade da janela da 0027 em relação à redação que ela cita podem
    ser conferidos contra marco autorado. Já estão na seção 5.1 daquele
    documento; este grupo é onde elas pesam mais.
05. **Se `sexo` em 0030/0031 tem fundamento** (§4), e o efeito da resposta
    sobre o `P2_IGUALDADE_MATERIAL_ATIVA`.
06. **Transcrever os incisos do art. 35 da LCE 1.100/2021** (§6), única via
    para conferir idade e partição por sexo das 0033/0034.
07. **`integral` das 0033/0034** (§5.2) e `tipo_calculo` da 0032 (§5.1):
    valores que a fundamentação da própria regra contradiz.
08. **O `nome` da 0027** e a atribuição à EC 41/2003 (§5.3), a decidir junto
    com o `achado-0013`.
09. **A fila da 0025 na lista congelada** (§9) — `TRANSCREVER`, não
    `REDACAO`.
10. **Se `paridade: S` nas quatro históricas** (0023–0026) tem fundamento,
    já que nenhuma delas cita provisão sobre reajuste.
11. **Se `sexo`, `integral` e `tipo_calculo` vazios nas quatro históricas**
    devem ser preenchidos com o que os dispositivos já vinculados dizem
    (§A). É o `achado-0008`, aberto; a conferência mostra onde está a
    resposta, não a escreve.
12. **O que funda `data_adm_apos: 01/01/1910` e `01/01/1950`** — as duas
    sentinelas de admissão do grupo, não interpretadas por decisão (P5) e
    não fundadas por dispositivo nenhum.
