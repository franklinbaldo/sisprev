# Reconferência do bloco 3 — valor gravado contra a fundamentação da própria regra

> **Nota:** Relatório gerado por IA como apoio à decisão. **Não é artefato
> oficial**, não edita nenhuma `regra-*.md`, nenhum `achado-*.md`, nenhum
> dispositivo, não altera schema, dados derivados
> (`data/regras-sisprev.csv`), motor ou `site/`. Reconfere os itens 3.2 a 3.7
> de
> [`achados-candidatos-da-conferencia.md`](achados-candidatos-da-conferencia.md),
> que ali estão marcados **[R]** — vindos do relatório de grupo e nunca
> verificados. Cada veredito abaixo é resultado de ler o `regra-*.md` inteiro
> e o texto dos dispositivos que ela cita. Toda conclusão sobre valor gravado
> é ato humano, em achado próprio.

## Método, e o que "confirma" significa aqui

Para cada item: leitura do frontmatter completo da regra, leitura do corpo
(nenhuma das regras deste bloco tem corpo — todas estão `importada`, sem
`# Estado da análise`), leitura verbatim de cada dispositivo em
`okf/dispositivos/` que a regra vincula, e comparação das **duas pontas**.

Três vereditos:

- **confirma** — a contradição existe e as duas pontas foram lidas;
- **refuta** — a leitura do relatório está errada, e digo em qual campo;
- **inconclusivo** — falta uma das pontas, e digo exatamente qual.

### O eixo de cada comparação, que não é sempre o mesmo

Duas comparações diferentes aparecem neste bloco, e confundi-las produz
afirmação forte demais:

1. **texto ↔ campo** — a `fundamentacao_*` da própria regra afirma em prosa o
   que um campo da mesma regra grava ao contrário. Os dois lados são
   **deployáveis** e estão no mesmo documento; nada externo é necessário para
   ver a contradição.
2. **dispositivo ↔ campo** — o dispositivo que a regra cita diz o contrário do
   campo. Depende de o dispositivo **alcançar** a população da regra, o que
   nem sempre é verificável nas colunas.

O item 3.2 é enunciado no eixo (1) ("contrário à **própria fundamentação**");
os itens 3.3, 3.6 e 3.7 são enunciados no eixo (2). Onde os dois eixos
coincidem, digo.

### A ressalva que vale para todo o bloco: a semântica das três colunas é "a definir"

`INTEGRAL` (`S/N`), `PARIDADE` (`S/N`) e `TIPO_CALCULO` (`string (enum)`) são
os três "candidatos a resultado/efeito (Q6)" do mapa P13.2
(`scripts/regra_schema.py::COLUMNS`), e a `semantica` declarada dos três é
literalmente `a definir` — `tipo_calculo` com a agravante de `a investigar (Q10 — 'Não identificado' sem significado presumido)`.

Consequência prática, e ela separa os vereditos abaixo:

- quando o texto da regra usa **a mesma palavra do nome da coluna** ("com
  paridade" × `paridade`, "proventos integrais" × `integral`), a contradição
  se sustenta com uma suposição quase tautológica, que registro uma vez e não
  repito: a de que a coluna `PARIDADE` grava o que o texto chama de paridade;
- quando a comparação depende do **referente de um valor do enum**
  (`Valor Médio`, `Valor Efetivo`, `Remuneração de Contribuição`,
  `Tipo Cálculo Nova Previdência`), ela **não fecha** dentro do catálogo:
  o domínio do enum é do Sisprev, e alterá-lo está fora do escopo
  ([`okf/spec/regra.md`](../../okf/spec/regra.md), "O escopo é parametrização").
  A §5.7 do relatório do regime novo já registrava essa disjunção; ela é o
  que rebaixa três itens abaixo.

### O que este documento não afirma

Nada aqui diz o que **o motor faz**. Em regra `simulavel: S` o motor não lê a
fundamentação, e critérios decisivos deste bloco (tempo de contribuição,
opção pelo § 16 do art. 40, grau de deficiência) não têm coluna. Uma
contradição entre dois campos deployáveis é defeito de **registro e de
documento entregue**; o cálculo efetivo não é reconstruível pelo catálogo.

### Verificação das fontes: o que pude e o que não pude reconferir

- **LCE 1.100/2021** e **LCE 432/2008**: além do corpus, conferi as passagens
  usadas contra `fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt` e
  `ditel-LC432-COMPILADA-REVOGADA.txt` (as compilações oficiais da Casa
  Civil). Batem.
- **ECE 146/2021**: **não pude reconferir contra a fonte**. O único arquivo
  local é `fontes-oficiais/arquivos/sapl-emenda_146.pdf`, PDF escaneado **sem
  camada de texto** (`pdftotext` devolve vazio). Todo texto da ECE 146/2021
  citado abaixo vem dos dispositivos autorados em
  `okf/dispositivos/ece-146-2021/`, que são o registro do próprio
  repositório, com `fontes:` apontando para o SAPL — não vem de leitura minha
  da publicação oficial, e **nada foi escrito de memória**.
- **EC 103/2019**: o Planalto está fora do ar. A data de entrada em vigor que
  uso (13/11/2019) é a que `okf/dispositivos/ec-103-2019/norma.md` declara em
  `vigencia_inicio`, corroborada por `regra-0078`/`0079`, que gravam
  `data_adm_ate: 13/11/2019` para o mesmo corte. Não é leitura minha do art.
  36 da EC 103.

______________________________________________________________________

## 3.2 — Onze regras do regime novo gravam resultado contrário à própria fundamentação

**Veredito: confirma para 8 das 11; inconclusivo para 3.** O eixo texto ↔
campo é real e o li nas 11. Mas em três delas (`0065`, `0066`, `0067`) o
**único** campo em conflito é `tipo_calculo`, e aí a comparação depende do
referente do valor do enum — que o repositório não fixa.

As onze são `0059`–`0067`, `0107` e `0108` (§5.2 de
[`conferencia-criterio-dispositivo-voluntaria-regime-novo.md`](conferencia-criterio-dispositivo-voluntaria-regime-novo.md)).

### As duas pontas

Ponta do texto — `fundamentacao_integral`, byte a byte igual dentro de cada
subgrupo:

> `0059`–`0064`: "Aposentadoria voluntária de servidor com deficiência, com
> proventos integrais (**cálculo por integralidade**) e **com paridade**, com
> base no artigo 40, § 4º-A, da Constituição Federal [...] artigos 25, 27,
> I; 35, da Lei Complementar nº 1.100/2021 [...]"

> `0065`–`0067`: "Aposentadoria voluntária de servidor exposto a agentes
> nocivos à saúde, com proventos integrais (**cálculo por integralidade**) e
> **com paridade**, com base nos artigos 25, 27, inciso I, e 41, inciso III,
> da Lei Complementar Estadual 1.100/2021 [...] - regra permanente"

> `0107`/`0108`: "Aposentadoria especial de professor, com proventos
> integrais (**cálculo por integralidade**) e **com paridade**, com base no
> artigo 40, § 5°, da Constituição Federal [...] artigos 25, 27, I; 33, da
> Lei Complementar nº 1.100/2021 [...] - regra permanente da aposentadoria
> especial de professor."

Ponta dos campos:

| regras             | `integral` | `paridade` | `tipo_calculo` | campos contra o próprio texto |
| ------------------ | ---------- | ---------- | -------------- | ----------------------------- |
| `0059`–`0064` (6)  | S          | **N**      | Valor Médio    | `paridade` + `tipo_calculo`   |
| `0065`, `0066` (2) | S          | S          | Valor Médio    | só `tipo_calculo`             |
| `0067` (1)         | S          | S          | Valor Efetivo  | só `tipo_calculo`             |
| `0107`, `0108` (2) | **N**      | **N**      | Valor Médio    | os três                       |

Ponta do dispositivo — as onze vinculam `lce-1100-2021/art-25/original` e
`lce-1100-2021/art-27-inc-i/original`, cujos textos são (conferidos contra a
compilação oficial, linhas 437 e 480 do `.txt`):

> **Art. 25.** Os proventos de aposentadoria do servidor público que tenha
> ingressado no serviço público em cargo efetivo até 31 de dezembro de 2003 e
> que não tenha feito a opção de que trata o § 16 do art. 40 da Constituição
> Federal corresponderá **à totalidade da remuneração no cargo efetivo** em
> que se der a aposentadoria.

> **Art. 27.** [...] **I** - de acordo com o disposto no art. 7° da Emenda
> Constitucional n° 41, de 19 de dezembro de 2003, para aposentadorias
> concedidas a servidor público que tenha ingressado no serviço público em
> cargo efetivo até 31 de dezembro de 2003 [...]

### O que fica provado, e o que não

**Provado (8 regras).** `0059`–`0064` gravam `paridade: N` contra um texto
que, no mesmo documento, afirma "com paridade"; `0107`/`0108` gravam
`integral: N` **e** `paridade: N` contra um texto que afirma "proventos
integrais [...] e com paridade". Nenhuma dessas oito comparações passa pelo
enum: são `S/N` contra a palavra correspondente escrita na própria regra.

**Não provado (3 regras).** Em `0065`, `0066` e `0067` `integral` e
`paridade` estão coerentes com o texto, e o único conflito é
`tipo_calculo: Valor Médio` (ou `Valor Efetivo`) contra "cálculo por
integralidade". Isso só é contradição se `Valor Médio` designar média e
`Valor Efetivo` **não** designar "totalidade da remuneração no cargo
efetivo". A §5.7 daquele relatório já formulava a disjunção — se
`Valor Efetivo` for integralidade, é `0067` que fecha e `0065`/`0066` que
erram, o inverso da leitura ingênua. Continuo sem base para escolher, e a
lista consolidada conta as três como se estivessem provadas.

**Reforço lateral, e ele é forte.** Para `0107`/`0108` existem gêmeas:
`0041`/`0042` carregam `fundamentacao_integral` **idêntica caractere a
caractere**, vinculam os **mesmos cinco dispositivos** e gravam
`integral: S`, `paridade: S`, `tipo_calculo: Remuneração de Contribuição` —
que é o que o texto diz. O par `0041`×`0107` já está autorado no
[`achado-0016`](../../okf/regras-sisprev/achados/achado-0016.md), que
conferiu as janelas e concluiu que **não são duplicatas**: `0041` alcança
quem ingressou até 2003, `0107` não limita a admissão. O defeito está em uma
delas, e o texto não diz qual.

**Sobreposição com o que já existe.** `0020`, `0033`, `0034`, `0057`, `0107`,
`0108`, `0109` e `0110` já estão em
[`achado-0009`](../../okf/regras-sisprev/achados/achado-0009.md)
(`P9_INTEGRAL_SEM_FUNDAMENTACAO`) — mas ali o achado é de **forma**
(`integral: N` com `fundamentacao_proporcional` vazia). O que a reconferência
acrescenta é de mérito: a única fundamentação preenchida afirma o oposto do
campo. Note que `0042` e `0108` **não** estão em `achado-0016`, embora sejam
as gêmeas femininas do par que ele descreve.

**O que ficou faltando:** o significado operacional dos valores de
`tipo_calculo` no Sisprev (pergunta ao IPERON, item 09 dos pontos em aberto
do relatório do regime novo). Sem ele, três das onze não fecham.

______________________________________________________________________

## 3.3 — `regra-0109`/`0110`: três campos contra o único dispositivo que os funda

**Veredito: confirma**, nos dois eixos, para as 2 regras — e a reconferência
acrescenta um achado que o relatório de grupo não tinha: existe um par irmão
(`0111`/`0112`) que grava exatamente o oposto sobre a mesma base citada, e a
partição que separa os dois pares **não é a do dispositivo que ambos citam**.

### Ponta dos campos

`0109` (MASCULINO) e `0110` (FEMININO): `integral: N`, `paridade: N`,
`tipo_calculo: Valor Médio`, `data_adm_apos: 31/12/2003`,
`data_adm_ate: 31/12/2024`.

### Ponta do texto da própria regra

`fundamentacao_integral` (dois segmentos separados por `|`, um por sexo;
`0109`/`0110` invertem a ordem em relação a `0111`/`0112`, então a chave é a
palavra de sexo, nunca a posição):

> "Aposentadoria especial de policial, com **proventos integrais** (cálculo
> por média) e sem paridade, com base no artigo 7º, §§ 2º e 3º da Emenda
> Constitucional Estadual nº 146/2021, artigo 1º, inciso II, alínea "a", da
> Lei Complementar nº 51/1985 [...] - regra transitória de homem - idade +
> tempo + pedágio"

Aqui o texto **já se contradiz sozinho**: afirma "proventos integrais" e, no
mesmo período, "cálculo por média". `integral: N` contradiz a primeira
metade; `paridade: N` e `Valor Médio` acompanham a segunda.

### Ponta do dispositivo

`ece-146-2021/art-7-par-3/original` (corpo autorado no corpus; a cadeia traz
o *caput*, conforme [`okf/spec/dispositivo.md`](../../okf/spec/dispositivo.md)):

> **Art. 7º** O policial civil [...] que tenham ingressado na respectiva
> carreira **até a data de entrada em vigor da Emenda Constitucional nº 103,
> de 13 de novembro de 2019**, poderão aposentar-se na forma da Lei
> Complementar nº 51, de 20 de dezembro de 1985, **com paridade e
> integralidade**, observada a idade mínima de 55 (cinquenta e cinco) anos
> para ambos os sexos ou o disposto no § 2º.

> **§ 3º** Os proventos das aposentadorias concedidas nos termos do disposto
> neste artigo, para aquele que tenha ingressado na respectiva carreira até a
> data de entrada em vigor da Emenda Constitucional nº 103, de 2019, e que
> **não tenha feito a opção de que trata o § 16 do art. 40 da Constituição
> Federal**, corresponderão **à totalidade da remuneração do servidor público
> no cargo efetivo** em que se der a aposentadoria [...] e **serão
> reajustados na mesma proporção e na mesma data, sempre que se modificar a
> remuneração dos servidores em atividade** [...]

E `lc-51-1985/art-1-inc-ii-al-a/lc-144-2014`, também vinculado:

> **II** - voluntariamente, **com proventos integrais**, independentemente da
> idade: **a)** após 30 (trinta) anos de contribuição, desde que conte, pelo
> menos, 20 (vinte) anos de exercício em cargo de natureza estritamente
> policial, se homem;

Os três campos de resultado contradizem, um a um, o único dispositivo citado
que trata de proventos. **Confirmado.**

### A janela de admissão

`data_adm_apos: 31/12/2003` cobre a partir de **01/01/2004** (`APOS` é
exclusivo, confirmado — [`okf/spec/regra.md`](../../okf/spec/regra.md),
"Elegibilidade temporal") e `data_adm_ate: 31/12/2024` cobre **até
31/12/2024** inclusive. O corte do art. 7º é o ingresso até a entrada em
vigor da EC 103/2019 — 13/11/2019 pelo `vigencia_inicio` de
`ec-103-2019/norma.md`, e é a data que `0078`/`0079` gravam em
`data_adm_ate` para o mesmo corte.

Precisão que o enunciado do item 3.3 não faz: a incompatibilidade é do
**limite superior**, não da janela inteira. O trecho 01/01/2004 → 13/11/2019
está dentro do corte; o trecho **14/11/2019 → 31/12/2024** está fora dele, e
para essa população o art. 7º não é fundamento nenhum. **Confirmado, com essa
correção.**

### O que a reconferência acrescenta: o par irmão e a partição que ninguém citou

`0111`/`0112` citam **os mesmos** `art-7-par-2` + `art-7-par-3` + a alínea da
LC 51/1985 conforme o sexo, e gravam `integral: S`, `paridade: S`,
`tipo_calculo: Remuneração de Contribuição` — coerente com o § 3º. A
`fundamentacao_integral` delas difere da de `0109`/`0110` exatamente nas duas
expressões em disputa: "(cálculo por **integralidade**) e **com** paridade"
contra "(cálculo por **média**) e **sem** paridade".

O que separa os dois pares é a admissão: `0111`/`0112` cobrem até 31/12/2003,
`0109`/`0110` de 01/01/2004 em diante. Essa partição por **31 de dezembro de
2003** é exatamente a dos arts. 24 e 25 da LCE 1.100/2021 — média para quem
ingressou depois, totalidade para quem ingressou até —, e **nenhuma das
quatro regras cita a LCE 1.100/2021**. O art. 7º da ECE 146/2021, que as
quatro citam, particiona por **13/11/2019**, não por 2003.

Ou seja: os valores de `0109`/`0110` são explicáveis — provavelmente vêm do
trilho da média do regime novo —, e ainda assim **contradizem o único
dispositivo que a regra cita**, porque a regra não cita a norma que faria
esses valores corretos. É contradição *e* fundamentação incompleta, e a
correção pode ser em qualquer das duas pontas.

**Registro de recusa:** a única hipótese que reconciliaria os campos com o
art. 7º sem mudar nada é o servidor ter feito a opção do § 16 do art. 40 da
CF (o § 3º exclui quem optou). **Nenhuma coluna registra essa opção**, e o
texto que governaria o optante não está citado nem transcrito. Não afirmo que
seja isso; registro que é a única saída textual e que o catálogo não a
expressa.

**O que ficou faltando:** reconferir o texto da ECE 146/2021 contra a
publicação oficial (o PDF local é escaneado, sem camada de texto); e a
decisão humana sobre qual ponta cede.

______________________________________________________________________

## 3.4 — `regra-0033`/`0034`: `integral: N` num texto que diz "proventos integrais"

**Veredito: confirma** no eixo texto ↔ campo, para as 2 regras, **em um único
campo**. O eixo dispositivo ↔ campo **não está disponível** — e o item, como
enunciado, não o invoca.

### As duas pontas

`fundamentacao_integral` (idêntica nas duas; é o único campo de fundamentação
preenchido, `fundamentacao` e `fundamentacao_proporcional` estão vazios):

> "Aposentadoria voluntária de servidor com deficiência, com **proventos
> integrais** (cálculo por média) e sem paridade, com base no artigo 40, §
> 4º-A, da Constituição Federal [...] artigos 24, 27, II; 35, da Lei
> Complementar nº 1.100/2021 [...]"

Campos: `integral: N`, `paridade: N`, `tipo_calculo: Valor Médio`.

**Dois dos três campos estão coerentes com o texto** — "sem paridade" ×
`paridade: N`, "cálculo por média" × `Valor Médio`. Só `integral: N` colide
com "proventos integrais", e a colisão não passa pelo enum. É exatamente o
que o item 3.4 afirma, sem excesso. **Confirmado.**

### Por que a segunda ponta não fecha

Os dispositivos vinculados são coerentes com a **forma de cálculo**, não com
o **percentual**:

> **Art. 24.** No cálculo dos proventos [...] que tenham ingressado no
> serviço público em cargo efetivo **após 31 de dezembro de 2003** [...]
> será considerada a **média aritmética simples das maiores remunerações**
> [...] correspondentes a 80% (oitenta por cento) de todo o período
> contributivo [...]

> **Art. 27. [...] II** - **nos termos estabelecidos para o RGPS**, para as
> aposentadorias concedidas a servidor público que tenha ingressado [...]
> após 31 de dezembro de 2003 [...]

Art. 24 fixa a **base** de cálculo (média de 80%); art. 27, II, o reajuste
(RGPS, isto é, sem paridade). **Nenhum dos dois diz qual fração dessa base o
provento representa** — que é precisamente o que `integral` parece gravar. O
art. 35, que governaria a hipótese, está transcrito só até o *caput*:

> **Art. 35.** O servidor público com deficiência [...] fará jus à
> aposentadoria voluntária, desde que cumprido tempo mínimo de 10 (dez) anos
> [...] **observadas as seguintes condições:**

Os incisos I/II/III (grave/moderada/leve) não estão no corpus. É a fila
`TRANSCREVER` do §5.3 da lista consolidada, e enquanto ela não fechar o
percentual do provento na aposentadoria do servidor com deficiência não tem
provisão transcrita a que se referir.

**O que ficou faltando:** transcrever os incisos do art. 35 da LCE
1.100/2021. Só isso permite dizer se o texto ("proventos integrais") ou o
campo (`integral: N`) está certo — hoje as duas pontas disponíveis são ambas
da própria regra.

______________________________________________________________________

## 3.5 — `regra-0019`/`0020`: "texto diz integrais e com paridade, campos gravam N"

**Veredito: refuta como enunciado.** Duas coisas estão erradas no item:
`paridade` é **`S`** nas duas regras, coerente com o texto; e a `regra-0019`
é **inteiramente coerente** com a própria fundamentação. O que sobra é real,
e alcança **uma** regra, não duas.

### As duas pontas

`fundamentacao_integral`, idêntica nas duas:

> "Aposentadoria por incapacidade permanente, com **proventos integrais**
> (cálculo por **integralidade**) e **com paridade**, com base no artigo 40,
> § 1º, inciso I, da Constituição Federal, com redação dada pela Emenda
> Constitucional n. 103/2019 e os artigos 25 e 27, inciso I e 30, §8°, da Lei
> Complementar Estadual nº 1.100/2021 - fundamento - incapacidade - LCE
> 1.100/2021 (**acidente em serviço, moléstia profissional ou doença grave,
> contagiosa ou incurável**, com ingresso antes de 2004)"

| campo                    | `regra-0019`      | `regra-0020`               |
| ------------------------ | ----------------- | -------------------------- |
| `paridade`               | **S**             | **S**                      |
| `integral`               | **S**             | **N**                      |
| `tipo_calculo`           | **Valor Efetivo** | **Proporcionalidade Dias** |
| `data_adm_ate`           | 31/12/2003        | 31/12/2003                 |
| `fundamentacao_integral` | idêntica          | ←                          |

O `paridade: S` das duas é coerente com "com paridade" e com o art. 27, I
vinculado (reajuste na forma do art. 7º da EC 41/2003, para ingresso até
31/12/2003 — e `data_adm_ate: 31/12/2003` bate). A `0019` grava
`integral: S`, coerente com "proventos integrais". **Não há nada a acusar na
`0019`.**

### O que resta, e é forte, na `regra-0020`

`integral: N` + `tipo_calculo: Proporcionalidade Dias` contra três coisas
concordantes entre si:

1. o **próprio texto** da regra: "proventos integrais (cálculo por
   integralidade)";
2. o **art. 25** vinculado: "corresponderá à totalidade da remuneração no
   cargo efetivo";
3. o **caput do art. 30** da LCE 1.100/2021, cuja cadeia entra no dispositivo
   `art-30-par-8` que a regra vincula (conferido contra a compilação oficial,
   linha 572):

> **Art. 30.** O servidor aposentado por incapacidade permanente para o
> trabalho fará jus a **proventos proporcionais ao tempo de contribuição**,
> **exceto se** a incapacidade for decorrente de **acidente em serviço,
> moléstia profissional ou doença grave, contagiosa ou incurável**.

E a hipótese que a `fundamentacao_integral` da `0020` descreve é, textualmente,
a da **exceção** — as três causas estão escritas no campo, e o § 8º
vinculado é justamente a lista das doenças graves. Ou seja: a regra declara a
hipótese em que o provento **não** é proporcional e grava o cálculo
proporcional.

`Proporcionalidade Dias` é o único ponto que depende do enum, e mesmo ele tem
âncora textual: o art. 26 da mesma lei — o artigo do cálculo proporcional —
diz "os períodos utilizados no cálculo previsto neste artigo serão
considerados em **número de dias**".

`0019`/`0020` são, portanto, mais um caso do padrão de `0041`×`0107`: par de
gêmeas com fundamentação byte-idêntica e resultado oposto. Aqui, ao contrário
de `0041`×`0107`, as janelas **não** as separam — `data_adm_*` e
`data_direito_*` são iguais nas duas —, então a hipótese "populações
diferentes, resultados diferentes" não está disponível.

**Reformulação correta do item:** *`regra-0020` grava `integral: N` e cálculo
proporcional numa regra cuja fundamentação descreve a hipótese excetuada do
art. 30 da LCE 1.100/2021 e afirma integralidade; a `regra-0019`, sua gêmea
de fundamentação idêntica e mesmas janelas, grava o oposto.*

**O que ficou faltando:** o que distingue `0019` de `0020` — nada nas colunas
o registra, e é a mesma pergunta Q6 de `0006`↔`0007`. Enquanto ela não for
respondida, não se sabe se `0020` é a regra proporcional de uma partição que
o catálogo não expressa, ou se está simplesmente errada.

______________________________________________________________________

## 3.6 — `regra-0032`: `tipo_calculo: Tipo Cálculo Nova Previdência`

**Veredito: inconclusivo.** As duas alegações de fato do item são
verdadeiras, mas a contradição que elas sugerem depende inteiramente do
referente do valor do enum — que **não está definido em lugar nenhum**: nem
no mapa P13.2, nem no corpus, nem nas compilações oficiais (nenhuma das duas
leis estaduais usa a expressão "Nova Previdência"). E há contraprova interna
que impede a inferência fácil.

### O que é verdadeiro

`fundamentacao_proporcional` da `0032`:

> "Aposentadoria compulsória, com proventos proporcionais ao tempo de
> contribuição (**média aritmética simples**) e sem paridade, com base no
> artigo 40, § 1º, inciso II, da Constituição Federal, com redação dada pela
> Emenda Constitucional nº 88/2015; em conformidade com a Lei Complementar nº
> 152/2015, combinado com os **artigos 17, 21, § 1º, 45 e 62 da Lei
> Complementar Estadual nº 432/2008**, e com o artigo 4º da Emenda
> Constitucional Estadual nº 146/2021."

E os dispositivos vinculados dizem exatamente isso (conferidos contra
`ditel-LC432-COMPILADA-REVOGADA.txt`, linhas 570 e 1236):

> **Art. 45** (redação da LCE 672/2012): "[...] será considerada a **média
> aritmética simples das maiores remunerações** [...] correspondente a 80%
> [...]"

> **Art. 17**: "Para cálculo dos proventos **proporcionais ao tempo de
> contribuição**, será utilizada fração [...] **§ 2º.** Os períodos de tempo
> utilizados no cálculo previsto neste artigo serão considerados em **número
> de dias**."

> **Art. 21**: "O servidor será aposentado compulsoriamente, aos 70 (setenta)
> anos de idade, com **proventos proporcionais ao tempo de contribuição**."

### Três fatos mecânicos que tornam o valor anômalo

1. **É hapax.** `Tipo Cálculo Nova Previdência` ocorre **1 vez em 112
   regras**. As outras cinco ocorrências da família são
   `Tipo Cálculo Nova Previdência Pensão por morte` (`0014`–`0018`), e as
   cinco vinculam exclusivamente o trilho da LCE 1.100/2021.
2. **`regra-0027` cita os mesmos seis dispositivos** — a lista
   `dispositivos:` das duas é idêntica, e o texto da `0027` é o mesmo da
   `0032` sem a frase descritiva inicial — e grava
   `tipo_calculo: Proporcionalidade Dias`.
3. **Todas as outras compulsórias com cálculo proporcional gravam
   `Proporcionalidade Dias`** (`0027`, `0030`, `0031`), que é literalmente o
   que o art. 17, § 2º descreve.

### Por que não fecho

A inferência natural — "o rótulo diz Nova Previdência, mas os vínculos são do
regime revogado em 18/10/2021, logo está errado" — é bloqueada por
`0030`/`0031`: elas **são** do trilho da LCE 1.100/2021 (vinculam arts. 24,
26, 27-II e 31) e gravam `Proporcionalidade Dias`, não a família "Nova
Previdência". Então o rótulo **não** acompanha simplesmente a norma, e sem
saber o que ele designa no Sisprev não afirmo que colida com "média
aritmética simples". Pode ser um sinônimo operacional, um resíduo de
migração, ou o erro que o relatório supõe.

**O que ficou faltando:** a definição dos valores de `TIPO_CALCULO` no
Sisprev (Q6/Q10). É pergunta ao IPERON e está fora do escopo de
parametrização; nenhuma leitura do catálogo a substitui. O que se pode
autorar hoje é a **anomalia** (hapax + regra irmã com dispositivos idênticos
gravando outro valor), não a contradição.

______________________________________________________________________

## 3.7 — `regra-0057`/`0058`: integralidade dependendo do sexo, sem dispositivo que a funde

**Veredito: confirma**, para as 2 regras, e o achado é mais forte do que o
enunciado sugere: além de o desdobramento por sexo não ter fundamento, a
`0057` contradiz o próprio texto.

### As duas pontas

As duas regras são idênticas em tudo, exceto `sexo` e `integral`:

| campo                    | `regra-0057` | `regra-0058` |
| ------------------------ | ------------ | ------------ |
| `sexo`                   | MASCULINO    | FEMININO     |
| `integral`               | **N**        | **S**        |
| `paridade`               | N            | N            |
| `tipo_calculo`           | Valor Médio  | Valor Médio  |
| `data_adm_apos`          | 01/01/2004   | 01/01/2004   |
| `data_adm_ate`           | 09/09/2021   | 09/09/2021   |
| `fundamentacao_integral` | idêntica     | ←            |

> "Aposentadoria especial de professor, com **proventos integrais** (cálculo
> por média) e sem paridade, com base no artigo 5º, §§ 4° e 6°, inciso II, e
> § 7º, II, da Emenda Constitucional Estadual nº 146/2021, e artigo 40, §5°,
> da Constituição Federal [...]"

Os dispositivos vinculados, lidos verbatim:

> **art-5-par-4**: "§ 4º Para o titular do cargo de professor [...] os
> requisitos **de idade e tempo de contribuição** de que tratam os incisos I
> e II do caput serão: I - 51 anos de idade, se mulher, e 56 anos, se homem;
> II - 25 anos de contribuição, se mulher, e 30 anos, se homem [...]"

> **art-5-par-6-inc-ii**: "§ 6º Os proventos das aposentadorias concedidas
> nos termos do disposto neste artigo corresponderão: II - **à média
> aritmética simples das maiores remunerações** [...] 80% [...] para o
> servidor público **não contemplado no inciso I do § 6º**."

> **art-5-par-7-inc-ii**: "§ 7º Os proventos [...] serão reajustados: II -
> **nos termos estabelecidos para o Regime Geral de Previdência Social**, na
> hipótese prevista no inciso II do § 6º [...]"

> **cf88/art-40-par-5/ec-103-2019**: "§ 5º Os ocupantes do cargo de professor
> terão **idade mínima reduzida em 5 anos** [...]"

### O que fica provado

**O sexo aparece em exatamente um lugar, e não é o do provento.** O § 4º
diferencia por sexo **idade e tempo de contribuição** — dois requisitos que
**não têm coluna** no catálogo. O § 6º, II (a regra do valor do provento) e o
§ 7º, II (a do reajuste) são **silentes quanto a sexo**, e o § 5º da CF
também. Nenhum dispositivo vinculado condiciona a integralidade ao sexo, e
as duas regras carregam a mesma fundamentação. **`integral` divergindo por
sexo não é fundado por nada que as regras citem. Confirmado.**

**A contraprova mais próxima está fora do alcance delas, e reforça.** O § 6º,
**inciso I** — o trilho da integralidade, que estas regras **não** vinculam —
é o único dispositivo desta família em que sexo aparece junto de provento, e
mesmo ali o que varia por sexo é a **idade de acesso** (62/65, ou 57/60 para
professor), não o direito à integralidade. Além disso ele alcança só quem
ingressou **até 31/12/2003**, e a janela de admissão de `0057`/`0058` começa
em **01/01/2004** — a população delas está, por construção, no inciso II.

**E há uma segunda contradição, no eixo texto ↔ campo:** `0057` grava
`integral: N` contra sua própria fundamentação, que afirma "proventos
integrais". É a mesma colisão de 3.4, e a `0057` já está em
[`achado-0009`](../../okf/regras-sisprev/achados/achado-0009.md) pela forma
(`fundamentacao_proporcional` vazia).

**O que ficou faltando:** reconferir a ECE 146/2021 contra a publicação
oficial (PDF sem camada de texto); e, como em 3.5, saber se `0057`/`0058` são
uma partição que o catálogo não expressa — mas aqui a hipótese é mais fraca,
porque o campo que difere (`integral`) é justamente o que nenhum dispositivo
vinculado desdobra.

______________________________________________________________________

## Quadro-resumo

| item    | veredito                          | regras que o item alcança de verdade                              | pronto para achado autorado?                           |
| ------- | --------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------ |
| **3.2** | confirma 8 de 11; 3 inconclusivas | `0059`–`0064`, `0107`, `0108` (8). `0065`–`0067` dependem do enum | **sim**, para as 8 (`0107` já em `achado-0016`)        |
| **3.3** | confirma (dois eixos)             | `0109`, `0110` (2)                                                | **sim** — o mais forte do bloco                        |
| **3.4** | confirma no eixo texto ↔ campo    | `0033`, `0034` (2), em **um** campo (`integral`)                  | **sim**, com o escopo estreitado ao eixo texto ↔ campo |
| **3.5** | **refuta como enunciado**         | `0020` (1) — não 2, e não em `paridade`                           | **sim**, reformulado; `0019` sai da acusação           |
| **3.6** | inconclusivo                      | `0032` (1), como **anomalia**, não como contradição               | não como contradição; sim como pergunta ao IPERON      |
| **3.7** | confirma                          | `0057`, `0058` (2)                                                | **sim**                                                |

Alcance real do bloco 3.2–3.7, sem dupla contagem: **15 regras** confirmadas
(`0020`, `0033`, `0034`, `0057`, `0058`, `0059`–`0064`, `0107`, `0108`,
`0109`, `0110`), **4** inconclusivas (`0065`, `0066`, `0067`, `0032`) e **1**
retirada da acusação (`0019`). A lista consolidada, somando os enunciados
como estão, sugeriria 20.

## Observações adjacentes, que não são itens do bloco

Duas coisas apareceram na conferência e não pertencem a nenhum dos seis
itens. Registro sem propor edição — não toquei em nenhum documento.

1. **Transcrição truncada em `lce-1100-2021/art-25/original`.** O corpo do
   parágrafo único termina em "[...] e das vantagens pessoais permanentes."
   (com ponto final). A compilação oficial segue: "[...] e das vantagens
   pessoais permanentes, **observados os seguintes critérios:**" + incisos I e
   II. É a família de falha do §5.3 da lista consolidada — truncamento
   silencioso, com o agravante de o ponto final fazer o corte parecer o fim
   do dispositivo. Não afeta nenhum veredito acima (a parte usada é o
   *caput*), mas afeta quem for conferir o cálculo da remuneração do cargo
   efetivo.
2. **`regra-0042` e `regra-0108` não estão em `achado-0016`**, embora sejam
   as gêmeas femininas exatas do par `0041`×`0107` que ele descreve, com a
   mesma `fundamentacao_integral` e os mesmos dispositivos.
