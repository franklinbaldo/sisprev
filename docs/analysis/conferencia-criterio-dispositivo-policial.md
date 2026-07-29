# Conferência `critério → dispositivo` — as 13 regras de policial (LC 51/1985)

> **Nota:** Relatório gerado por IA como apoio à decisão. **Não é artefato
> oficial**, não edita nenhuma `regra-*.md`, nenhum `achado-*.md`, nenhum
> dispositivo, não altera schema, dados derivados
> (`data/regras-sisprev.csv`), motor ou `site/`. É a aplicação da conferência
> descrita na RFC 0008 §5 — para cada critério da regra, qual dispositivo o
> funda — ao grupo da aposentadoria especial de policial. Toda conclusão
> sobre citação é ato humano, em achado próprio.

## O método, e a distinção que ele exige

A RFC 0008 §5 registra a definição da coordenação: a fundamentação
**articula** os dispositivos de forma a fundamentar **cada** critério da
própria regra. Logo a relação real é `critério → dispositivo(s)`, e
`dispositivos:` é a união achatada dela. Conferir é desachatar.

Duas perguntas convivem aqui e **não coincidem**:

1. *"qual dispositivo funda este critério?"* — jurídica; é o que esta
   conferência responde;
2. *"o que este campo cita?"* — de leitura; é o que `dispositivos:` registra.

Um `dispositivos:` afirma *"a fundamentação desta regra **cita** esta
provisão"*, **nunca** "a regra se funda nela" (ver
[`docs/spec/dispositivo.md`](../spec/dispositivo.md)). Toda proposta de
alteração de vínculo abaixo foi conferida contra os campos `fundamentacao`,
`fundamentacao_integral` e `fundamentacao_proporcional` da própria regra —
e o resultado dessa conferência está na seção final: **nenhum vínculo a
acrescentar ou remover nas treze**.

## 1. As treze regras

`regra-0072`, `0073`, `0074`, `0075`, `0076`, `0077`, `0078`, `0079`,
`0084`, `0109`, `0110`, `0111`, `0112`.

Constante nas treze: `tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO`, `tipo: CIVIL`, `apos_especial: S`, `tipo_remun: ''`,
`tabelapontuacao: N`, `requisitos_da_in_no_5_2020: N`,
`adicional_inatividade: N`, `relatorio_p_reserva_remunerada_por_idade_ex_officio: N`,
`atualmente_no_sistema: TRUE`, `validado_pge: FALSE`,
`validado_presidencia: FALSE`, `fundamentacao_proporcional: ''` (salvo
`0084`), `visivel_dtc_*: N`.

O que varia:

| regra  | sexo      | integral | paridade | tipo_calculo       | data_adm_apos  | data_adm_ate   | data_direito_apos | data_direito_ate | ciclo | simulável | alínea LC 51 vinculada |
| ------ | --------- | -------- | -------- | ------------------ | -------------- | -------------- | ----------------- | ---------------- | ----- | --------- | ---------------------- |
| `0072` | MASCULINO | S        | S        | Remun. de Contrib. | 01/01/1950     | 13/11/2019     | 14/09/2021        | 31/12/2099       | 3º    | S         | "a"                    |
| `0073` | FEMININO  | S        | S        | Remun. de Contrib. | 01/01/1950     | 13/11/2019     | 14/09/2021        | 31/12/2099       | 3º    | S         | "b"                    |
| `0074` | MASCULINO | S        | S        | Remun. de Contrib. | 01/01/1950     | 13/11/2019     | 14/09/2021        | 31/12/2099       | 3º    | S         | "a"                    |
| `0075` | MASCULINO | S        | S        | Remun. de Contrib. | 01/01/1950     | 13/11/2019     | 14/09/2021        | 31/12/2099       | 3º    | S         | "a"                    |
| `0076` | MASCULINO | S        | S        | Remun. de Contrib. | 01/01/1950     | 13/11/2019     | 14/09/2021        | 31/12/2099       | 3º    | S         | "a"                    |
| `0077` | MASCULINO | S        | S        | Remun. de Contrib. | 01/01/1950     | 13/11/2019     | 14/09/2021        | 31/12/2099       | 3º    | S         | "a"                    |
| `0078` | MASCULINO | S        | S        | Remun. de Contrib. | 01/01/1950     | 13/11/2019     | 14/09/2021        | 31/12/2099       | 3º    | S         | **"b"**                |
| `0079` | FEMININO  | S        | S        | Remun. de Contrib. | 01/01/1950     | 13/11/2019     | 14/09/2021        | 31/12/2099       | 3º    | S         | "b"                    |
| `0084` | **AMBOS** | S        | **N**    | **Valor Médio**    | 01/01/1950     | **31/12/2099** | **01/01/1950**    | 31/12/2099       | 3º    | **N**     | **"b"**                |
| `0109` | MASCULINO | **N**    | **N**    | **Valor Médio**    | **31/12/2003** | **31/12/2024** | **01/01/1910**    | **31/12/2024**   | 4º    | S         | "a"                    |
| `0110` | FEMININO  | **N**    | **N**    | **Valor Médio**    | **31/12/2003** | **31/12/2024** | **01/01/1910**    | **31/12/2024**   | 4º    | S         | "b"                    |
| `0111` | MASCULINO | S        | S        | Remun. de Contrib. | 01/01/1950     | **31/12/2003** | **01/01/1910**    | **31/12/2024**   | 4º    | S         | "a"                    |
| `0112` | FEMININO  | S        | S        | Remun. de Contrib. | 01/01/1950     | **31/12/2003** | **01/01/1910**    | **31/12/2024**   | 4º    | S         | "b"                    |

Quatro subgrupos se desenham, e é por eles que a conferência anda:

- **A** — `0072`–`0077`, `0111`, `0112`: transitória do art. 7º, §§ 2º e 3º
  (com pedágio), integralidade e paridade;
- **B** — `0078`, `0079`: art. 7º, §§ 1º e 3º (sem pedágio);
- **C** — `0109`, `0110`: mesma base do subgrupo A, mas **os três campos de
  resultado invertidos**;
- **D** — `0084`: mandado de injunção, sem janela de admissão, `sexo: AMBOS`.

## 2. Os dispositivos vinculados — o que cada texto de fato diz

Só cinco provisões distintas aparecem nas treze. Transcrito do corpo de cada
`.md` em `okf/dispositivos/`:

| dispositivo                                | o que o texto estabelece                                                                                                                           |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cf88/art-40-par-1-inc-iii/ec-103-2019`    | aposentadoria voluntária por **idade**: 62/65 na União; nos Estados, "na idade mínima estabelecida mediante emenda às respectivas Constituições"   |
| `ece-146-2021/art-7-par-1/original`        | define o que conta como **tempo de exercício estritamente policial** (civil, legislativo, penal, socioeducativo, militar)                          |
| `ece-146-2021/art-7-par-2/original`        | **pedágio**: 52 anos se mulher, 53 se homem, com período adicional de contribuição                                                                 |
| `ece-146-2021/art-7-par-3/original`        | proventos = **totalidade da remuneração do cargo efetivo** + **reajuste na mesma proporção e data** dos ativos, para quem ingressou até 13/11/2019 |
| `lc-51-1985/art-1-inc-ii-al-a/lc-144-2014` | 30 anos de contribuição, 20 em cargo estritamente policial, **se homem**                                                                           |
| `lc-51-1985/art-1-inc-ii-al-b/lc-144-2014` | 25 anos de contribuição, 15 em cargo estritamente policial, **se mulher**                                                                          |

Duas observações de leitura, ambas verificadas no corpus e não de memória:

- o **caput** do art. 7º da ECE 146/2021 — que fixa o corte de ingresso
  ("até a data de entrada em vigor da Emenda Constitucional nº 103, de 13 de
  novembro de 2019"), a idade mínima de 55 anos para ambos os sexos, e a
  remissão "na forma da Lei Complementar nº 51, de 1985, com paridade e
  integralidade" — **não existe como dispositivo autorado**. Só há
  `art-7-par-1`, `art-7-par-2` e `art-7-par-3`; o texto do caput aparece
  neles apenas como contexto de leitura;
- as duas alíneas do art. 1º, II da LC 51/1985 trazem, no próprio texto
  transcrito, a marca "(Incluído pela Lei Complementar n° 144, de 2014)" —
  logo a única redação autorada (`lc-144-2014`) é a que as instituiu, e a
  escolha de redação nas treze é segura, ainda que nenhuma fundamentação
  nomeie a emenda.

## 3. A conferência

### Subgrupo A — `0072`–`0077`, `0111`, `0112` (art. 7º, §§ 2º e 3º)

| critério                                           | valor                            | fundado por                                                                                                                                | fecha?                                           |
| -------------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------ |
| tipo de benefício                                  | voluntária por tempo de contrib. | `lc-51-1985/art-1-inc-ii-al-a`/`-al-b` ("voluntariamente")                                                                                 | ✅ parcial (ver §5.7)                            |
| `apos_especial: S`                                 | aposentadoria especial           | LC 51/1985, art. 1º, II — regime próprio do servidor policial                                                                              | ✅                                               |
| `sexo: MASCULINO`                                  | homem                            | alínea **"a"** — "se homem"                                                                                                                | ✅                                               |
| `sexo: FEMININO`                                   | mulher                           | alínea **"b"** — "se mulher"                                                                                                               | ✅                                               |
| `data_adm_ate: 13/11/2019`                         | ingresso até a EC 103/2019       | `art-7-par-3` ("que tenha ingressado ... até ... 13 de novembro de 2019"); caput, por remissão do § 2º ("servidores de que trata o caput") | ✅ — mas o caput não é dispositivo autorado      |
| `data_direito_apos: 14/09/2021`                    | direito a partir da ECE 146      | vigência da própria ECE 146/2021 (`norma.md`, `vigencia_inicio: 2021-09-14`)                                                               | ✅ derivado da norma, não de provisão            |
| `data_direito_ate: 31/12/2099`                     | sentinela                        | o art. 7º não fixa termo final                                                                                                             | ✅ por ausência (P5: sentinela não interpretada) |
| `integral: S`                                      | integralidade                    | `art-7-par-3` — "totalidade da remuneração ... no cargo efetivo"                                                                           | ✅                                               |
| `tipo_calculo: Remun. de Contrib.`                 | base = remuneração do cargo      | `art-7-par-3`, mesma oração                                                                                                                | ✅                                               |
| `paridade: S`                                      | paridade                         | `art-7-par-3` — "reajustados na mesma proporção e na mesma data, sempre que se modificar a remuneração dos servidores em atividade"        | ✅                                               |
| idade 52/53 + pedágio                              | **não parametrizada**            | `art-7-par-2` — vinculado, mas nenhuma coluna registra idade ou pedágio                                                                    | ⚠️ dispositivo sem critério correspondente       |
| tempo de contribuição (30/25 anos)                 | **não parametrizado**            | alíneas "a"/"b"                                                                                                                            | ⚠️ idem                                          |
| `data_adm_ate: 31/12/2003` (`0111`/`0112` só)      | ingresso até 2003                | **nada citado o funda** — ver §5.6                                                                                                         | ❌                                               |
| `data_direito_ate: 31/12/2024` (`0111`/`0112` só)  | prazo de 2024                    | **nada citado o funda** — ver §5.6                                                                                                         | ❌                                               |
| `data_direito_apos: 01/01/1910` (`0111`/`0112` só) | direito desde 1910               | nenhum dispositivo citado alcança data anterior a 14/09/2021                                                                               | ❌                                               |

O `art-7-par-3` é aqui o que o art. 6º-A da EC 41/2003 foi na conferência de
invalidez: **funda três critérios de uma vez** — integralidade, base de
cálculo e paridade. No `dispositivos:` achatado ele é uma linha entre quatro,
indistinguível das demais.

`0111` e `0112` são materialmente o subgrupo A com **três janelas trocadas**
e nenhum dispositivo novo citado para justificá-las.

### Subgrupo B — `0078`, `0079` (art. 7º, §§ 1º e 3º)

Idênticas ao subgrupo A em todos os campos de resultado; diferem no vínculo:
substituem `art-7-par-2` (pedágio) por `art-7-par-1` (definição de tempo
policial). O `nome` diz "Art. 7º, § 3º"; o campo `fundamentacao` diz "§§ 1º e
3º"; o `fundamentacao_integral` diz "§ 3º". O vínculo cobre a união (§ 1º e
§ 3º) e é, nesse sentido, **fiel aos campos**.

| critério                             | valor                 | fundado por                         | fecha?                                            |
| ------------------------------------ | --------------------- | ----------------------------------- | ------------------------------------------------- |
| `integral`/`tipo_calculo`/`paridade` | S / Remun. / S        | `art-7-par-3`                       | ✅                                                |
| `data_adm_ate: 13/11/2019`           | ingresso até a EC 103 | `art-7-par-3`                       | ✅                                                |
| `sexo: FEMININO` (`0079`)            | mulher                | alínea **"b"** — "se mulher"        | ✅                                                |
| `sexo: MASCULINO` (`0078`)           | homem                 | alínea **"b"** — "se mulher"        | ❌ **o dispositivo vinculado rege o sexo oposto** |
| tempo policial computável            | não parametrizado     | `art-7-par-1`                       | ⚠️ dispositivo sem critério correspondente        |
| idade mínima de 55 anos              | não parametrizada     | caput do art. 7º — **não autorado** | ⚠️ ver §5.2                                       |

### Subgrupo C — `0109`, `0110` (mesma base, resultado invertido)

Citam e vinculam exatamente o que o subgrupo A cita e vincula
(`art-7-par-2` + `art-7-par-3` + alínea conforme o sexo), mas gravam o
resultado oposto:

| critério                                                 | valor                      | fundado por                                                                           | fecha?                                          |
| -------------------------------------------------------- | -------------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------- |
| `sexo` × alínea                                          | M→"a", F→"b"               | alíneas "a"/"b"                                                                       | ✅                                              |
| `integral: N`                                            | proporcional               | `art-7-par-3` diz "totalidade da remuneração"; a alínea diz "com proventos integrais" | ❌ **contradiz os dois dispositivos citados**   |
| `tipo_calculo: Valor Médio`                              | média                      | `art-7-par-3` fixa a remuneração do cargo como base                                   | ❌ contradiz                                    |
| `paridade: N`                                            | sem paridade               | `art-7-par-3` estabelece a paridade                                                   | ❌ contradiz                                    |
| `data_adm_apos: 31/12/2003` + `data_adm_ate: 31/12/2024` | admissão entre 2003 e 2024 | o art. 7º exige ingresso **até 13/11/2019**                                           | ❌ janela incompatível com o dispositivo citado |
| `data_direito_ate: 31/12/2024`                           | prazo de 2024              | **nada citado o funda** — ver §5.6                                                    | ❌                                              |
| `data_direito_apos: 01/01/1910`                          | desde 1910                 | ECE 146/2021 só vige desde 14/09/2021                                                 | ❌                                              |

Os próprios campos de texto dessas duas regras se contradizem: o
`fundamentacao_integral` afirma "com proventos integrais (cálculo por média)
e sem paridade" enquanto `integral: N`. E `fundamentacao_proporcional` está
vazio com `integral: N` — é a detecção `P9_INTEGRAL_SEM_FUNDAMENTACAO`
(`achado-0009`). A conferência acrescenta o que a detecção não vê: **não é
só que falta a fundamentação proporcional; a única fundamentação presente,
e os dois dispositivos que ela cita, afirmam integralidade.**

### Subgrupo D — `0084` (Aposentadoria por Mandado de Injunção)

Única com `fundamentacao_proporcional` preenchido (idêntico ao
`fundamentacao_integral`), único `simulavel: N`, único `sexo: AMBOS`. Sem
prosa descritiva: os dois campos são uma lista nua de citações.

| critério                        | valor                 | fundado por                                            | fecha?                                              |
| ------------------------------- | --------------------- | ------------------------------------------------------ | --------------------------------------------------- |
| `sexo: AMBOS`                   | homens e mulheres     | alínea **"b"** — "se mulher"                           | ❌ a única alínea vinculada rege só um dos sexos    |
| `integral: S`                   | integral              | `art-7-par-3` + "proventos integrais" da alínea        | ✅                                                  |
| `tipo_calculo: Valor Médio`     | média                 | `art-7-par-3` fixa a remuneração do cargo              | ❌ contradiz                                        |
| `paridade: N`                   | sem paridade          | `art-7-par-3` estabelece a paridade                    | ❌ contradiz                                        |
| `data_adm_ate: 31/12/2099`      | sem corte de ingresso | o art. 7º (caput e § 3º) exige ingresso até 13/11/2019 | ❌ a janela é aberta e o dispositivo citado a fecha |
| `data_direito_apos: 01/01/1950` | direito desde 1950    | ECE 146/2021 vige desde 14/09/2021                     | ❌                                                  |
| o mandado de injunção em si     | —                     | **nenhum dispositivo; é decisão judicial**             | ❌ nenhuma coluna registra o provimento judicial    |

`0084` é o caso em que a conferência mostra o limite do modelo, não um erro
de preenchimento: o que torna essa regra o que ela é — uma ordem judicial em
mandado de injunção — **não é dispositivo legal e não tem onde ser
registrado**. Os dispositivos citados descrevem o regime que a decisão
provavelmente mandou aplicar, não o fundamento da regra.

## 4. O `|` nas fundamentações: qual segmento vale

Seis das treze (`0072`, `0073`, `0109`, `0110`, `0111`, `0112`) empacotam
**duas** fundamentações no `fundamentacao_integral`, separadas por `|`: uma
com a alínea "a" e a palavra "homem", outra com a alínea "b" e a palavra
"mulher". Essa é a fila `SEGMENTAR` da
[lista congelada](pendencias-de-citacao-congeladas.md) — mas **estas seis não
estão lá**; a fila registrada tem só `regra-0021`/`0022`.

Aqui, ao contrário de `0021`/`0022` (cuja divisão é por *causa da
incapacidade*, que nenhuma coluna registra), **a divisão é por `sexo`, que é
coluna existente e está preenchida**. O segmento operativo é, portanto,
identificável com segurança, e **não pela ordem**: em `0072`/`0073`/`0111`/
`0112` o primeiro segmento é o masculino, e em `0109`/`0110` a ordem está
invertida (primeiro o feminino). A chave confiável é a palavra de sexo dentro
do segmento e a alínea que ele nomeia — nunca a posição.

Conferido segmento a segmento, **as seis vinculam a alínea correta para o
próprio `sexo`**. O que sobra é o segmento do sexo oposto, que permanece
como texto morto num campo *deployable* — uma regra masculina carregando a
frase "regra transitória mulher". Isso é defeito do campo, não do vínculo:
**não se deve acrescentar a alínea do sexo oposto ao `dispositivos:`** para
"cobrir" o segundo segmento. O vínculo registra a provisão que a regra
efetivamente aplica.

## 5. O que a conferência revelou

### 5.1 O art. 40, § 1º, III não fixa critério representado nas colunas — nas treze

`cf88/art-40-par-1-inc-iii/ec-103-2019` está vinculado nas treze regras (e
citado, "segunda parte", em todas as fundamentações preenchidas).
Percorrendo os critérios efetivamente parametrizados — tipo de benefício,
sexo, `apos_especial`, as quatro janelas, `integral`, `tipo_calculo`,
`paridade` — **nenhum é fundado por ele**. O inciso trata de aposentadoria
voluntária **por idade**, e nenhuma dessas regras parametriza idade.

A "segunda parte" que as fundamentações invocam existe de fato no texto — "no
âmbito dos Estados, do Distrito Federal e dos Municípios, na idade mínima
estabelecida mediante emenda às respectivas Constituições" — e é ela que
autoriza a ECE 146/2021 a fixar idade. Mas isso funda a **competência da
emenda estadual**, não um critério da regra. É a mesma conclusão a que a
[conferência de invalidez](conferencia-criterio-dispositivo-invalidez-0006-0009.md)
chegou para o mesmo inciso, agora por um caminho independente.

**E há um agravante próprio deste grupo:** o dispositivo constitucional
específico da aposentadoria policial é o **art. 40, § 4º-B** ("Poderão ser
estabelecidos por lei complementar do respectivo ente federativo idade e
tempo de contribuição diferenciados para aposentadoria de ocupantes do cargo
de ... policial"), que **está autorado no corpus**
(`cf88/art-40-par-4b/ec-103-2019`) e é citado e vinculado pelas outras quatro
regras de policial do catálogo (`0080`–`0083`, fora deste grupo). Nenhuma das
treze o cita. Não proponho vinculá-lo — nenhum campo delas o menciona, e
vincular seria exatamente o erro que a §6 registra —, mas a divergência entre
duas famílias de regras de policial quanto ao ancoradouro constitucional é
achado autorável.

### 5.2 O caput do art. 7º funda critérios e não existe como dispositivo

O corte de ingresso em 13/11/2019 (oito regras), a idade mínima de 55 anos e
a própria remissão "na forma da LC 51/1985, com paridade e integralidade"
estão no **caput** do art. 7º da ECE 146/2021. O caput não está transcrito
como dispositivo (só `art-7-par-1`, `-par-2`, `-par-3`). O corte de ingresso
sobrevive porque o § 3º o repete no próprio texto; a idade de 55 anos, não —
e é justamente o ramo "sem pedágio" que a
[reconciliação policial](reconciliacao-policial.md) §3 aponta como faltante
(hipóteses P7/P8 da PGE, "art. 7º caput e § 3º").

É pendência de **transcrição**, análoga às três da fila `TRANSCREVER` da
lista congelada. Na mesma condição, e citados dentro do § 3º: o § 8º do art.
5º da própria ECE 146/2021 e o § 16 do art. 40 da CF — nenhum dos dois
autorado.

### 5.3 `regra-0078`: o problema não é a palavra "mulher"

A detecção `P9_SEXO_FUNDAMENTACAO` (única do catálogo, `achado-0010`) é
mecânica e modesta: o campo `sexo` diz MASCULINO e a fundamentação contém
"mulher" sem conter "homem". A conferência endurece o achado sem inventar
nada:

- o dispositivo vinculado é `lc-51-1985/art-1-inc-ii-al-b/lc-144-2014`, cujo
  texto **termina em "se mulher"**;
- é a mesma alínea da `regra-0079`, sua par feminina, cujos 26 demais campos
  são idênticos;
- a alínea "a", que rege o homem (30/20 anos), não é citada nem vinculada.

Ou seja: não é uma palavra copiada em texto livre — **é a provisão legal do
sexo oposto que a regra invoca**. O vínculo está fiel ao campo; o campo é que
está em desacordo com `sexo`.

**Até onde isso vai, e onde para.** O que fica comprovado é a incompatibilidade
entre `sexo` e a única alínea citada. O que **não** se conclui daqui é que o
motor afira 25/15 em vez de 30/20: tempo de contribuição e tempo de exercício
policial não têm coluna no cadastro, e numa regra `simulavel: S` o motor não lê
a fundamentação. O risco é de **justificação jurídica errada** e de lacuna de
parametrização — o comportamento efetivo do motor não é reconstruível pelo
catálogo. A decisão continua sendo humana e continua sendo a que
o `achado-0010` já formula (conferir contra a fonte real do Sisprev se
`0078` é duplicata de `0079` ou o ramo masculino "sem pedágio" mal
preenchido) — a conferência apenas mostra que o desacordo é **jurídico**, e
não redacional.

### 5.4 `regra-0084` com `sexo: AMBOS` e só a alínea feminina

Mesmo padrão, sem detector que o pegue: `0084` vale para AMBOS os sexos e a
única alínea citada/vinculada é a "b", "se mulher". Não afirmo qual é o erro —
pode ser a citação, pode ser o `sexo` —, mas **não é possível que os dois
estejam certos ao mesmo tempo**.

Aqui `simulavel: N`, então a fundamentação pode orientar a triagem humana. Mas
esta é a regra "por Mandado de Injunção", e sem conhecer o provimento judicial
que a define não se diz o que ela de fato aplica a um requerente homem.

Nota: o `P9_SEXO_FUNDAMENTACAO` não dispara aqui porque `sexo: AMBOS` não é
um dos valores que ele confronta. Registro o fato; **não proponho estender o
detector** — a postura da fase é conferir e autorar, não criar maquinaria
(CLAUDE.md, "Em que fase o trabalho está").

### 5.5 `0109`/`0110`: os três campos de resultado contradizem o único dispositivo que os funda

O `art-7-par-3` é a única provisão citada que fala de proventos, e ela diz
integralidade **e** paridade **e** remuneração do cargo. `0109`/`0110`
gravam `integral: N`, `paridade: N`, `tipo_calculo: Valor Médio` — os três
contra o texto. E a janela de admissão (2003–2024) é incompatível com o corte
de ingresso do próprio art. 7º (até 13/11/2019).

A [reconciliação policial](reconciliacao-policial.md) §2 já havia marcado
essa célula como inexistente na matriz da PGE ("ou a base está errada, ou o
cálculo está errado"). A conferência confirma pelo lado do texto legal e
estreita: **não é uma célula ausente da matriz; é uma contradição direta com
o dispositivo citado**, em três campos independentes.

### 5.6 Janelas sem dispositivo: o art. 4º da ECE 146/2021 só aparece no `nome`

`0109`–`0112` gravam `data_direito_ate: 31/12/2024`. Esse prazo é
exatamente o do **art. 4º da ECE 146/2021** ("desde que sejam cumpridos até
31 de dezembro de 2024"), e o `nome` das quatro o cita textualmente ("c/c
art. 4º da EC nº 146/2021"). Mas **nenhum campo de fundamentação o cita**, e
por isso nenhuma das quatro o tem vinculado — corretamente, porque `nome`
não é fundamentação.

O resultado é um critério gravado, com fundamento legal existente, autorado
no corpus (`ece-146-2021/art-4/original`) e **sem caminho legítimo até o
vínculo**: fechar essa lacuna exige editar o campo de fundamentação, não o
`dispositivos:`. É a demonstração mais limpa, neste grupo, de que
`dispositivos:` responde "o que o campo cita" e não "o que funda a regra".

O mesmo vale, sem sequer a menção no `nome`, para `data_adm_ate: 31/12/2003`
em `0111`/`0112` (nada citado estabelece 2003) e para `data_direito_apos: 01/01/1910` em `0109`–`0112`.

### 5.7 O tipo de benefício e o que a LC 51/1985 diz sobre idade

`tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO` é
fundado pela alínea da LC 51/1985 na parte "voluntariamente" e pelo tempo de
contribuição que ela fixa. Mas o inciso II diz, literalmente,
"**independentemente da idade**", e o art. 7º da ECE 146/2021 impõe idade
mínima (55 no caput, 52/53 no § 2º). O benefício efetivamente concedido é
"idade + tempo", como as próprias fundamentações dizem em prosa
("idade + tempo + pedágio").

Não é erro de vínculo e **não é corrigível dentro do escopo**: estender o
domínio de `TIPO DE BENEFICIO` seria alterar o Sisprev (CLAUDE.md, "O
trabalho é de parametrização"). Registro como o que é — uma perda de
resolução entre a lei e a coluna.

### 5.8 Dispositivos vinculados que não fundam critério parametrizado

Além do art. 40, § 1º, III (§5.1), dois casos em que o vínculo é **legítimo**
(o campo cita, e a provisão é articulada na fundamentação) mas não alcança
nenhuma coluna:

- `ece-146-2021/art-7-par-2` (idade 52/53 + pedágio) — nas dez regras que o
  vinculam;
- `ece-146-2021/art-7-par-1` (o que conta como tempo policial) — em `0078` e
  `0079`.

O catálogo não tem coluna de idade, de tempo de contribuição, nem de tempo
de exercício policial. São, portanto, dispositivos que fundam **requisitos
reais do benefício que o Sisprev não parametriza** — o oposto de um vínculo
supérfluo. Isso é exatamente o que a P13.1 pede para ficar escrito, e é a
razão pela qual "dispositivo que não fixa critério representado nas colunas"
é *suspeita*, não veredito — e por que a formulação larga ("não funda nada")
seria errada: um dispositivo pode fundar competência, remissão ou requisito
que o cadastro simplesmente não representa.

## 6. Nenhum vínculo a acrescentar ou remover

Conferidos os campos `fundamentacao`, `fundamentacao_integral` e
`fundamentacao_proporcional` das treze, um a um, contra o `dispositivos:` de
cada uma: **os 52 vínculos existentes correspondem ao que os campos citam, e
não há provisão citada sem vínculo**, com a única exceção do art. 4º da ECE
146/2021 — que não é citado em campo de fundamentação nenhum, apenas no
`nome` (§5.6), e por isso não é vinculável.

Três tentações foram examinadas e recusadas, todas pela mesma razão — elas
respondem "o que funda", quando `dispositivos:` responde "o que o campo
cita":

| tentação                                                    | por que não                                                                                           |
| ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| vincular `cf88/art-40-par-4b` (o dispositivo policial real) | nenhum campo das treze o menciona; quem o cita é `0080`–`0083`                                        |
| vincular `ece-146-2021/art-4` a `0109`–`0112`               | citado só no `nome`, que não é fundamentação                                                          |
| vincular a alínea do sexo oposto nas seis com `\|`          | o segmento do outro sexo é texto morto na regra; o vínculo registra a provisão que a regra **aplica** |
| remover `cf88/art-40-par-1-inc-iii` por não fundar critério | é citado, explicitamente e nas treze; a citação errada se decide em achado, não apagando o vínculo    |

## 7. Pontos em aberto

1. **`regra-0078`** — duplicata de `0079` a inativar, ou ramo masculino "sem
   pedágio" com alínea e sexo trocados? A decisão é a do `achado-0010` e
   depende da fonte real do Sisprev. A conferência acrescenta que a
   divergência é de provisão aplicada, não de redação.
2. **`regra-0084`** — `sexo: AMBOS` com a alínea feminina; e, mais fundo, uma
   regra cujo fundamento (decisão em mandado de injunção) não tem
   representação possível no catálogo. Vale decidir se isso é caso de achado
   ou de questão de escopo.
3. **`0109`/`0110`** — qual dos lados cede: a base citada (art. 7º, §§ 2º e
   3º) ou os três campos de resultado? A PGE não tem essa célula.
4. **`0111`/`0112` vs `0072`/`0073`** — mesma base, mesmos resultados, janelas
   diferentes e sem dispositivo que as funde. Se as janelas caírem, as quatro
   colapsam num par; se ficarem, falta a fundamentação que as sustente.
5. **Transcrever o caput do art. 7º** da ECE 146/2021 (e, secundariamente, o
   § 8º do art. 5º da mesma emenda e o § 16 do art. 40 da CF, ambos citados
   dentro do § 3º).
6. **A divergência de ancoradouro constitucional** entre as treze (art. 40,
   § 1º, III) e `0080`–`0083` (art. 40, § 4º-B) — duas famílias de regras de
   policial no mesmo catálogo apoiadas em provisões diferentes.
7. **O art. 4º da ECE 146/2021 no `nome` e não na fundamentação** — se a
   coordenação quiser o vínculo, o caminho é editar o campo de
   fundamentação, e essa é decisão sobre campo *deployable*.
8. **A fila `SEGMENTAR` da lista congelada não inclui estas seis regras**
   (`0072`, `0073`, `0109`–`0112`), embora empacotem duas fundamentações com
   `|`. A lista está congelada e não se regenera; registro a lacuna sem
   propor atualizá-la.
9. **`P9_SEXO_FUNDAMENTACAO` não alcança `sexo: AMBOS`** (§5.4). Registrado
   como fato, sem proposta de mudança no detector.
