# Conferência `critério → dispositivo` — as 7 regras restantes de invalidez/incapacidade

> **Nota:** Relatório gerado por IA como apoio à decisão. **Não é artefato
> oficial**, não edita nenhuma `regra-*.md`, nenhum `achado-*.md`, nenhum
> dispositivo, não altera schema, dados derivados
> (`data/regras-sisprev.csv`), motor ou `site/`. É a segunda aplicação da
> conferência da RFC 0008 §5 — para cada critério da regra, qual dispositivo
> o funda —, agora sobre as **sete** regras de invalidez/incapacidade que a
> primeira rodada não cobriu. Toda conclusão sobre citação é ato humano, em
> achado próprio.

## O método, e o que ele não é

A relação real é `critério → dispositivo(s)`; `dispositivos:` é a **união
achatada** dela. Conferir é desachatar: percorrer os critérios que a regra
parametriza e dizer, para cada um, qual provisão o funda.

A distinção que a primeira rodada aprendeu do próprio erro
([modelo, "Um erro desta conferência"](conferencia-criterio-dispositivo-invalidez-0006-0009.md))
vale aqui inteira, e é o que mais restringe o que se pode propor:

- *"qual dispositivo funda este critério?"* — pergunta **jurídica**, é o que
  esta conferência responde;
- *"o que este campo cita?"* — pergunta de **leitura**, é o que
  `dispositivos:` registra.

As duas não coincidem. Por isso **nenhuma proposta de acrescentar ou remover
vínculo** aparece abaixo sem que os campos `fundamentacao`,
`fundamentacao_integral` e `fundamentacao_proporcional` da própria regra
tenham sido lidos primeiro — e, como se verá em §4.1, o resultado é que
**nenhum vínculo deste grupo deve ser acrescentado ou removido**, mesmo onde
o critério e o dispositivo claramente não se encontram.

Todo texto legal citado abaixo foi lido em `okf/dispositivos/`, nunca de
memória. Onde o texto necessário **não está transcrito no bundle**, a
conferência recusa a conclusão em vez de completá-la (§4.2, §5).

## 1. O grupo

Sete regras: `regra-0001`, `0002`, `0004`, `0019`, `0020`, `0021`, `0022`.

Comum às sete: `tipo: CIVIL`, `apos_especial: N`, `tipo_remun` vazio,
`tabelapontuacao: N`, `requisitos_da_in_no_5_2020: N`,
`relatorio_p_reserva_remunerada_por_idade_ex_officio: N`,
`adicional_inatividade: N`, `atualmente_no_sistema: TRUE`,
`ciclo_de_validacao: 1º`, `validado_pge`/`validado_presidencia: FALSE`,
`visivel_dtc_integral`/`visivel_dtc_proporcional: N` e — em **todas** —
`fundamentacao` (o campo geral) **vazio**: a fundamentação vive só nos dois
campos especializados.

O que as distingue:

|                              | 0001          | 0002          | 0004                 | 0019          | 0020                   | 0021                     | 0022        |
| ---------------------------- | ------------- | ------------- | -------------------- | ------------- | ---------------------- | ------------------------ | ----------- |
| `tipo_de_beneficio`          | INVALIDEZ     | INVALIDEZ     | INVALIDEZ            | INCAP. PERM.  | INCAP. PERM.           | INCAP. PERM.             | INCAP.PERM. |
| `simulavel`                  | N             | N             | N                    | N             | N                      | **S**                    | **S**       |
| `paridade`                   | S             | S             | S                    | S             | S                      | **N**                    | **N**       |
| `data_adm_apos`              | 01/01/1910    | 01/01/1910    | 01/01/1910           | 01/01/1950    | 01/01/1950             | **01/01/2004**           | 01/01/2004  |
| `data_adm_ate`               | 15/12/1998    | 15/12/1998    | 31/12/2003           | 31/12/2003    | 31/12/2003             | **31/12/2099**           | 31/12/2099  |
| `data_direito_apos`          | 01/01/1910    | 01/01/1910    | 16/12/1998           | 23/10/2021    | 23/10/2021             | 23/10/2021               | 23/10/2021  |
| `data_direito_ate`           | 15/12/1998    | 15/12/1998    | 31/12/2003           | 31/12/2099    | 31/12/2099             | 31/12/2099               | 31/12/2099  |
| `sexo`                       | AMBOS         | AMBOS         | **(vazio)**          | AMBOS         | AMBOS                  | AMBOS                    | AMBOS       |
| `integral`                   | S             | **N**         | **(vazio)**          | S             | **N**                  | **N**                    | S           |
| `tipo_calculo`               | Valor Efetivo | Valor Efetivo | **Não identificado** | Valor Efetivo | Proporcionalidade Dias | Proporcionalidade Dias   | Valor Médio |
| `fundamentacao_integral`     | preenchida    | preenchida    | preenchida           | preenchida    | preenchida             | preenchida (3 cláusulas) | idem        |
| `fundamentacao_proporcional` | **vazia**     | **vazia**     | preenchida           | **vazia**     | **vazia**              | **vazia**                | **vazia**   |
| `dispositivos:`              | 1             | 1             | 1                    | 4             | 4                      | **0**                    | **0**       |

Três pares e um avulso. Dentro de cada par (`0001`/`0002`, `0019`/`0020`,
`0021`/`0022`) o `fundamentacao_integral` é **byte-idêntico** — a diferença
material é só `integral` (e, em dois dos pares, `tipo_calculo`). `regra-0004`
é a única sem par e a única com os **dois** campos de fundamentação
preenchidos — com o mesmo texto nos dois.

Os três pares são os três grupos `P1_NOME_REPETIDO` do catálogo neste
recorte; nenhum forma grupo `P2_IGUALDADE_MATERIAL_ATIVA`, porque `integral`
os separa. Nenhum tem achado próprio — P1 não exige achado.

### 1.1 Como o grupo se liga às 0006–0009 já conferidas

As onze regras de invalidez/incapacidade formam **uma cadeia de regimes**
para o mesmo benefício. As quatro já conferidas ocupam a faixa do meio:

| regime                       | redação-chave                         | regras                                 | conferido em    |
| ---------------------------- | ------------------------------------- | -------------------------------------- | --------------- |
| CF/88, texto original        | `cf88/art-40-inc-i/original`          | **0001**, **0002**                     | aqui            |
| EC 20/1998                   | `cf88/art-40-par-1-inc-i/ec-20-1998`  | **0004**                               | aqui            |
| EC 41/2003 + LCE 432/2008    | `cf88/art-40-par-1-inc-i/ec-41-2003`  | 0006, 0007                             | rodada anterior |
| transição do art. 6º-A       | `ec-41-2003/art-6a/ec-70-2012`        | 0008, 0009                             | rodada anterior |
| EC 103/2019 + LCE 1.100/2021 | `cf88/art-40-par-1-inc-i/ec-103-2019` | **0019**, **0020**, **0021**, **0022** | aqui            |

A ligação é mais forte que a cronologia: **o texto de fundamentação de
0019–0022 é o template de 0006–0009 reescrito para o regime novo**, e a
correspondência é um-para-um.

| par novo      | par antigo correspondente | frase compartilhada                                                  |
| ------------- | ------------------------- | -------------------------------------------------------------------- |
| `0019`/`0020` | `0008`/`0009`             | "proventos integrais (cálculo por integralidade) e **com** paridade" |
| `0021`/`0022` | `0006`/`0007`             | "proventos integrais (cálculo por média) e **sem** paridade"         |

Com uma diferença que a conferência torna decisiva: em 0006–0009 **cada
regra carrega as duas fundamentações** (a integral e a proporcional), e foi
exatamente isso que invalidou a proposta de remover o art. 17 da 0006. Em
0019–0022 a migração **trouxe só a metade integral**: o campo
`fundamentacao_proporcional` das quatro está vazio, e o membro proporcional
de cada par (`0020`, `0021`) ficou com um único texto — o do irmão. É o
mesmo defeito que `0002` já tinha no regime de 1988.

## 2. A conferência

### 2.1 `regra-0001` e `regra-0002` — CF/88, art. 40, I, texto original

Texto conferido em `cf88/art-40-inc-i/original` (vigência 1988-10-05 →
1998-12-15): *"Art. 40. O servidor será aposentado: I - por invalidez
permanente, sendo os proventos integrais quando decorrentes de acidente em
serviço, moléstia profissional ou doença grave, contagiosa ou incurável,
especificadas em lei, e proporcionais nos demais casos"*.

| critério                       | valor                 | fundado por                                                   | fecha?                        |
| ------------------------------ | --------------------- | ------------------------------------------------------------- | ----------------------------- |
| tipo de benefício              | invalidez permanente  | `cf88/art-40-inc-i/original`                                  | ✅                            |
| `sexo`                         | AMBOS                 | a provisão não distingue por sexo                             | ✅ por ausência               |
| `integral: S` (0001)           | proventos integrais   | mesma provisão — "quando decorrentes de acidente em serviço…" | ⚠️ ver nota                   |
| `integral: N` (0002)           | proporcionais         | mesma provisão — "e proporcionais nos demais casos"           | ✅ juridicamente; ❌ no campo |
| `tipo_calculo: Valor Efetivo`  | base de cálculo       | **nenhum** dispositivo citado ou vinculado                    | ❌                            |
| `paridade: S`                  | reajuste com paridade | **nenhum** dispositivo citado ou vinculado                    | ❌                            |
| `data_direito_ate: 15/12/1998` | último dia            | `vigencia_fim` da própria redação (1998-12-15)                | ✅ pela vigência; ⚠️ ver §4.3 |
| `data_adm_ate: 15/12/1998`     | ingresso até          | a provisão **não tem** cláusula de ingresso                   | ❌ (P-1)                      |
| `data_*_apos: 01/01/1910`      | piso                  | sentinela, não interpretada (P5)                              | n/a                           |

**Nota sobre `integral: S`**: a exceção existe no texto, mas ela remete a
doenças "**especificadas em lei**" — e a lei estadual que as especificava no
regime de 1988 não é citada pela regra nem existe no corpus de
`okf/dispositivos/`. O critério fecha na estrutura (há exceção) e **não
fecha no conteúdo** (qual rol). Não nomeio a lei: seria citar de memória.

**Nota sobre `integral: N` (0002)**: a provisão funda o valor. O que não
fecha é o **campo**: 0002 tem `fundamentacao_proporcional` vazia e carrega o
texto no campo `_integral` (`achado-0009`, aberto).

### 2.2 `regra-0004` — CF/88, art. 40, § 1º, I, redação da EC 20/1998

Texto conferido em `cf88/art-40-par-1-inc-i/ec-20-1998` (vigência 1998-12-16
→ 2003-12-30): *"I - por invalidez permanente, sendo os proventos
proporcionais ao tempo de contribuição, exceto se decorrente de acidente em
serviço, moléstia profissional ou doença grave, contagiosa ou incurável,
especificadas em lei"*. Os dois campos de fundamentação da 0004 são
idênticos e citam essa única provisão.

| critério                                | valor                 | fundado por                                                                 | fecha?           |
| --------------------------------------- | --------------------- | --------------------------------------------------------------------------- | ---------------- |
| tipo de benefício                       | invalidez permanente  | `cf88/art-40-par-1-inc-i/ec-20-1998`                                        | ✅               |
| `integral` (vazio)                      | —                     | a provisão traz os **dois** ramos; a regra não escolhe nenhum               | ❌ `achado-0008` |
| `sexo` (vazio)                          | —                     | a provisão não distingue por sexo — um `AMBOS` fecharia por ausência        | ❌ `achado-0008` |
| `tipo_calculo: Não identificado`        | —                     | nada a fundar: o valor não afirma nada (Q10)                                | ❌ `achado-0008` |
| `paridade: S`                           | reajuste com paridade | **nenhum** dispositivo citado ou vinculado                                  | ❌               |
| janela de direito 16/12/1998–31/12/2003 | vigência da redação   | `vigencia_inicio`/`vigencia_fim` do dispositivo (16/12/1998–**30/12/2003**) | ⚠️ ver §4.3      |
| `data_adm_ate: 31/12/2003`              | ingresso até          | a provisão **não tem** cláusula de ingresso                                 | ❌ (P-1)         |

Observação que só a conferência lado a lado produz: **no eixo de admissão,
0004 subsome 0001/0002 inteiras** (`01/01/1910`–`31/12/2003` contém
`01/01/1910`–`15/12/1998`). Quem separa as três é o eixo de **direito**, não
o de ingresso — coerente com P-1, que registra que nenhuma das duas redações
traz cláusula de ingresso.

### 2.3 `regra-0019` e `regra-0020` — EC 103/2019 + LCE 1.100/2021, ingresso até 31/12/2003

Fundamentação (idêntica nas duas): art. 40, § 1º, I, CF, redação da EC
103/2019, e "os artigos 25 e 27, inciso I e 30, §8°" da LCE 1.100/2021.
Vinculados exatamente esses quatro. Textos conferidos:

- `cf88/art-40-par-1-inc-i/ec-103-2019`: *"I - por incapacidade permanente
  para o trabalho, no cargo em que estiver investido, quando insuscetível de
  readaptação…"* — a redação **não distingue** integral × proporcional.
- `lce-1100-2021/art-25/original`: *"…que tenha ingressado no serviço público
  em cargo efetivo **até 31 de dezembro de 2003** … corresponderá à
  totalidade da remuneração no cargo efetivo"*.
- `lce-1100-2021/art-27-inc-i/original`: reajuste "de acordo com o disposto
  no art. 7° da Emenda Constitucional n° 41" para quem ingressou até
  31/12/2003.
- `lce-1100-2021/art-30-par-8/original`: o rol de 16 doenças graves.

| critério                                      | valor                        | fundado por                                                                          | fecha?          |
| --------------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------ | --------------- |
| tipo de benefício                             | incapacidade permanente      | `cf88/art-40-par-1-inc-i/ec-103-2019`                                                | ✅              |
| `sexo`                                        | AMBOS                        | nenhuma das provisões distingue                                                      | ✅ por ausência |
| `data_adm_ate: 31/12/2003`                    | ingresso até                 | `art-25` e `art-27-inc-i` — "até 31 de dezembro de 2003", literal                    | ✅              |
| `tipo_calculo: Valor Efetivo` (0019)          | totalidade da remuneração    | `art-25`                                                                             | ✅ (⚠️ §4.3)    |
| `paridade: S`                                 | reajuste do art. 7º da EC 41 | `art-27-inc-i`                                                                       | ✅              |
| `integral: S` (0019)                          | integrais                    | `art-30-par-8` (rol) — exceção do **art. 30, caput**, não citado                     | ⚠️              |
| `integral: N` (0020)                          | proporcionais                | `art-30-caput` ("fará jus a proventos proporcionais") — **não citado nem vinculado** | ❌              |
| `tipo_calculo: Proporcionalidade Dias` (0020) | fração em dias               | `art-26/original`, § 2º ("em número de dias") — **não citado nem vinculado**         | ❌              |
| classe "acidente em serviço"                  | invocada no texto            | `art-30-par-5`/`par-6` — **não citados** (mas citados por 0021/0022)                 | ❌              |
| classe "moléstia profissional"                | invocada no texto            | **nenhum dispositivo, em nenhum dos dois regimes** (P-6)                             | ❌              |
| `data_direito_apos: 23/10/2021`               | início do direito            | **nenhum** dispositivo vinculado fixa essa data                                      | ❌ (§4.3)       |
| `data_direito_ate: 31/12/2099`                | sentinela                    | não interpretada (P5)                                                                | n/a             |

O art. 40, § 1º, I na redação da EC 103/2019 **perdeu** o discriminante
integral × proporcional que as redações de 1988 e de 1998 tinham no próprio
inciso. Nesse regime, quem discrimina é o **art. 30, *caput*** da LCE
1.100/2021 — e **nenhuma das quatro regras 0019–0022 o cita**. Todas citam
direto os parágrafos (o rol, as definições de acidente), que são as
*exceções* de um caput que ficou implícito.

### 2.4 `regra-0021` e `regra-0022` — mesmo regime, ingresso após 31/12/2003

O campo `fundamentacao_integral` empacota **três** fundamentações separadas
por `|`, uma por classe de causa (acidente em serviço / doença grave,
contagiosa ou incurável / moléstia profissional). A divisão é por **causa da
incapacidade**, critério que nenhuma coluna do cadastro registra: é a **Q6**,
aberta, e é por isso que as duas regras têm `dispositivos:` **vazio** e
figuram na fila `SEGMENTAR` das
[pendências congeladas](pendencias-de-citacao-congeladas.md) (7 itens cada).
**Não forço nenhuma atribuição** — nada abaixo propõe vínculo.

O que se pode conferir sem desempacotar: as três cláusulas citam **o mesmo
conjunto de artigos de cálculo e reajuste** (25 e 27, inciso I), variando só
o parágrafo do art. 30 conforme a classe de causa. Esse conjunto é conferível
contra os critérios gravados.

| critério                                      | valor                   | fundado por                                                                                            | fecha?           |
| --------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------ | ---------------- |
| tipo de benefício                             | incapacidade permanente | `cf88/art-40-par-1-inc-i/ec-103-2019` (citado nas três cláusulas)                                      | ✅ (sem vínculo) |
| `sexo`                                        | AMBOS                   | nenhuma das provisões distingue                                                                        | ✅ por ausência  |
| `data_adm_apos: 01/01/2004`                   | ingresso **após** 2003  | os artigos citados (25 e 27, I) dizem, no próprio texto, "**até** 31 de dezembro de 2003"              | ❌ contradiz     |
| `paridade: N`                                 | reajuste sem paridade   | `art-27-inc-ii` (RGPS) — não citado; o citado (`27-I`) funda paridade **S**                            | ❌ contradiz     |
| `tipo_calculo: Valor Médio` (0022)            | média das 80% maiores   | `art-24/original` — não citado; o citado (`art-25`) funda valor efetivo                                | ❌               |
| `tipo_calculo: Proporcionalidade Dias` (0021) | fração em dias          | `art-26/original`, § 2º — não citado                                                                   | ❌               |
| `integral: S` (0022)                          | integrais               | exceção do `art-30-caput` — não citado; classes via `§§ 5º/6º` e `§ 8º`                                | ⚠️               |
| `integral: N` (0021)                          | proporcionais           | regra geral do `art-30-caput` — não citado; **e o próprio texto da 0021 afirma "proventos integrais"** | ❌ contradiz     |
| classe "moléstia profissional" (cláusula 3)   | causa                   | cita "artigo 30" sem parágrafo; **nenhum dispositivo define a categoria** (P-6)                        | ❌               |
| causa da incapacidade como critério           | três classes num campo  | nenhuma coluna do cadastro                                                                             | **Q6 — recusa**  |

Isto é a **P-5** já registrada em
[`base-normativa-invalidez-incapacidade.md`](base-normativa-invalidez-incapacidade.md)
§3.3, vista pelo lado do critério. A conferência acrescenta duas coisas que a
formulação anterior não tinha: o desacordo atinge **três critérios
independentes** (janela de ingresso, `paridade`, `tipo_calculo`), não só a
janela; e os artigos citados por 0021/0022 são **exatamente os que fundam a
0019** — a citação é coerente com a regra irmã do outro ramo temporal, não
com a regra que a carrega.

## 3. Onde a conferência se recusa a concluir

- **Base de cálculo do "proporcional + ingresso até 2003" (0020).** O art. 26
  fixa a fração em dias, mas seu § 1º manda aplicá-la sobre proventos
  calculados "em conformidade com o disposto no art. 24" — o artigo do ramo
  **pós**-2003. Como se calcula o proporcional de quem ingressou **até** 2003
  não está resolvido nos textos transcritos. Os §§ 13 e 14 do art. 30, que
  [base-normativa §3.3.3](base-normativa-invalidez-incapacidade.md) registra
  como os que roteiam o cálculo para o art. 24 ou o art. 26, **não estão
  transcritos** em `okf/dispositivos/`. Sem esse texto, não afirmo qual é a
  base — nem que haja lacuna.
- **`paridade: S` em 0001/0002/0004.** As redações do art. 40 que fundavam a
  paridade nesses regimes não estão no bundle. Sei que o inciso citado não a
  funda; **não nomeio** qual dispositivo a fundaria.
- **Rol de doenças do regime de 1988/1998** ("especificadas em lei"): a lei
  estadual da época não está no corpus.
- **Qual dos dois campos de fundamentação vale.** Q7 ("por que uma regra pode
  ter as duas fundamentações?") continua aberta em `regra_schema.py`. Por
  isso §4.3 descreve a divergência entre 0020/0021 e seu texto **sem** dizer
  qual dos dois lados está errado.
- **A causa da incapacidade em 0021/0022** — Q6, direção A já decidida
  ([q6, §10](q6-causa-incapacidade.md)), mas a decomposição em linhas por
  classe é ato humano, não desta conferência.

## 4. O que a conferência revelou

### 4.1 Dispositivos vinculados que não fundam critério nenhum

**Nenhum vínculo a remover neste grupo.** O caso que parece um está em
`regra-0020`: ela vincula `lce-1100-2021/art-30-par-8` (o rol de doenças
graves), e o rol é a **exceção que produz `integral: S`** — 0020 grava
`integral: N`. O dispositivo não funda critério algum **dela**.

E ainda assim o vínculo está **certo**: 0020 *cita* o art. 30, § 8º, no seu
próprio `fundamentacao_integral`. Remover o vínculo apagaria uma citação que
existe. O defeito não está no vínculo, está no **campo** — 0020 carrega o
texto da metade integral do par. É literalmente o erro que a rodada anterior
cometeu com o art. 17 da 0006, com os papéis trocados, e a regra de conduta
que dele decorre resolve os dois casos: o vínculo segue a citação, o achado
trata o mérito.

O mesmo raciocínio se aplica preventivamente a 0021/0022: se alguém
segmentar as três cláusulas e vincular os arts. 25 e 27, I, esses vínculos
serão **corretos como citação** ainda que não fundem critério nenhum das
duas. O produto da conferência ali é um achado sobre a **fundamentação**, não
sobre o `dispositivos:`.

### 4.2 Critérios sem dispositivo

Consolidado, por natureza da lacuna:

| lacuna                                                          | regras                 | natureza                                       |
| --------------------------------------------------------------- | ---------------------- | ---------------------------------------------- |
| `paridade: S` sem dispositivo citado                            | 0001, 0002, 0004       | dispositivo não transcrito (§3)                |
| `tipo_calculo` sem dispositivo citado                           | 0001, 0002, 0004       | idem; em 0004 o valor é "Não identificado"     |
| janela de **ingresso** sem cláusula de ingresso na provisão     | 0001, 0002, 0004       | P-1, decisão jurídica pendente                 |
| rol de doenças "especificadas em lei"                           | 0001, 0002, 0004       | norma fora do corpus                           |
| regra geral integral × proporcional (`art-30-caput`) não citada | 0019, 0020, 0021, 0022 | citação a decidir — o texto existe no bundle   |
| `integral: N` e `Proporcionalidade Dias` sem base citada        | 0020, 0021             | `art-26` existe no bundle e não é citado (P-5) |
| `Valor Médio` sem base citada                                   | 0022                   | `art-24` existe no bundle e não é citado (P-5) |
| `paridade: N` sem base citada                                   | 0021, 0022             | `art-27-inc-ii` existe no bundle (P-5)         |
| classe "acidente em serviço" sem dispositivo                    | 0019, 0020             | `§§ 5º/6º` existem e são citados pelas irmãs   |
| classe "moléstia profissional" sem dispositivo                  | 0019, 0020, 0021, 0022 | **P-6 — gap normativo**, não só de citação     |
| `data_direito_apos: 23/10/2021` sem dispositivo                 | 0019, 0020, 0021, 0022 | ver §4.3                                       |

A linha que mais surpreende é a do `art-30-caput`: é o discriminante geral do
regime vigente — o análogo exato do art. 40, § 1º, I das redações antigas — e
**as quatro regras do regime novo citam só as suas exceções**.

### 4.3 Divergências entre valor gravado e dispositivo citado

**(a) O texto afirma o resultado oposto ao valor gravado — 0020 e 0021.**
Em cada par, o `fundamentacao_integral` é byte-idêntico entre os dois membros
e afirma um resultado concreto: "proventos integrais (cálculo por
integralidade) e **com** paridade" (0019/0020), "proventos integrais (cálculo
por média) e **sem** paridade" (0021/0022). Esse texto casa com 0019 e com
0022, e **contradiz** 0020 (`integral: N`, Proporcionalidade Dias) e 0021
(`integral: N`, Proporcionalidade Dias). Como as duas têm
`fundamentacao_proporcional` vazia, **o único texto de fundamentação que
carregam descreve o benefício que elas não concedem**.

Isso é mais forte do que o caso 0006/0007 da rodada anterior. Lá o texto
compartilhado carregava **as duas** fundamentações, e nenhuma das duas regras
era contradita pelo próprio campo. Aqui o campo contradiz.

O detector `P9_INTEGRAL_SEM_FUNDAMENTACAO` já registra 0002, 0020 e 0021, e
`achado-0009` já pergunta se é lapso de preenchimento "ou se o próprio campo
`integral` está marcado incorretamente como 'N'". A conferência **dá conteúdo
à segunda hipótese**: o texto presente não é neutro, ele afirma o contrário
do gravado. Decidir qual lado cede é ato humano (e depende de Q7).

**(b) 0021/0022 citam o ramo temporal oposto — em três critérios.** Detalhado
em §2.4. É P-5, agora com o alcance medido.

**(c) Duas convenções de fecho de janela em três regras da mesma cadeia.**
Conferindo `data_direito_*` contra a vigência da redação citada:

| regra      | valor gravado       | vigência da redação citada | convenção implícita                  |
| ---------- | ------------------- | -------------------------- | ------------------------------------ |
| 0001, 0002 | `ate = 15/12/1998`  | termina em **15/12/1998**  | último dia da própria redação        |
| 0004       | `apos = 16/12/1998` | começa em **16/12/1998**   | primeiro dia da própria redação      |
| 0004       | `ate = 31/12/2003`  | termina em **30/12/2003**  | primeiro dia da redação **seguinte** |

As duas pontas da 0004 usam critérios diferentes entre si, e o fecho de
0001/0002 usa um terceiro. Sob a semântica confirmada (`ATE` inclusivo,
`APOS` exclusivo — [janelas temporais §1](semantica-das-janelas-temporais.md)),
a janela efetiva de 0004 é 17/12/1998–31/12/2003 enquanto a redação viveu
16/12/1998–30/12/2003: **deslocada um dia nas duas pontas**, e o dia
16/12/1998 — justamente o da entrada em vigor da EC 20/1998 — não é coberto
por 0001/0002 nem por 0004.

Duas ressalvas que impedem chamar isso de erro fechado: `DATA_DIREITO_APOS`
**não** teve sua semântica confirmada (§1.2 daquele documento), e o item 01
da §5.2 de lá já pergunta se `15/12/1998` é erro de um dia. A conferência
acrescenta o que faltava: **a vigência autorada no bundle sustenta
`15/12/1998`** como último dia da redação. O conflito, então, não é entre o
catálogo e a lei — é entre duas convenções internas ao catálogo.

**(d) `23/10/2021` não é fundado por nenhum dispositivo vinculado.** As
quatro regras do regime novo abrem o direito em 23/10/2021; a LCE 1.100/2021
vige em **18/10/2021** (`vigencia_inicio` da norma e dos onze dispositivos
lidos) e a EC 103/2019 em 13/11/2019. É o item 06 da §5.2 das janelas
temporais; a conferência confirma pelo lado do fundamento que **nenhum dos
dispositivos que as quatro citam fixa 23/10/2021**.

**(e) O mesmo efeito jurídico gravado em dois valores de enum.** "Totalidade
da remuneração no cargo efetivo" (`art-25`, LCE 1.100/2021) e "remuneração do
cargo efetivo" (`art-6a`, EC 41/2003) são a mesma consequência — e o catálogo
grava `Valor Efetivo` em 0001/0002/0019 e `Remuneração de Contribuição` em
0008/0009. Como o domínio do enum é do Sisprev e **estender domínio está fora
de escopo**, isto é pergunta de parametrização (qual dos dois valores é o
correto para cada regra), não de schema. **Não decido qual.**

## 5. Pontos em aberto

Nenhum destes é fechado por esta conferência.

1. **Q7** — qual a relação entre `integral` e o par `fundamentacao_integral`/
   `fundamentacao_proporcional`. Sem ela, §4.3(a) descreve uma contradição
   mas não diz qual lado cede. É a pergunta que destrava 0002, 0020 e 0021 de
   uma vez (e as outras 14 regras de `achado-0009`).
2. **P-5** (0021/0022) — corrigir a fundamentação para o ramo pós-2003
   (arts. 24, 26, 27-II, 30 *caput*) ou confirmar, contra fonte, que a
   citação atual está certa por motivo não capturado. Continua sendo edição
   de `regra-*.md`, ato humano.
3. **Q6 / 0021/0022** — segmentar as três classes de causa em linhas, na
   direção A já decidida. Só depois disso faz sentido falar em
   `dispositivos:` para essas duas.
4. **P-6** — "moléstia profissional" segue sem dispositivo que a defina, nos
   **dois** regimes estaduais. Afeta 0019–0022 igualmente.
5. **P-1** — se 0001/0002/0004 alcançam algum caso concreto hoje depende de
   requisitos já preenchidos antes da reforma ou de transição expressa, não
   da data de ingresso. A conferência confirma, pelo lado do fundamento, que
   nenhuma das duas redações traz cláusula de ingresso — e as três regras
   gravam janela de ingresso mesmo assim.
6. **`art-30-caput` não citado pelas quatro regras do regime vigente** — é
   citação a decidir, do mesmo tipo de P-3 (o art. 40, § 1º, III em
   0006–0009), mas de sinal contrário: lá um dispositivo citado que não funda
   nada; aqui um dispositivo que funda o critério central e não é citado.
7. **`23/10/2021`, `15/12/1998`, `01/01/2004`** — os três já estão na fila da
   §5.2 das janelas temporais; §4.3(c) e (d) acrescentam o cotejo contra a
   vigência autorada.
8. **Dispositivos a transcrever**, se a auditoria quiser fechar §3: art. 30,
   §§ 13 e 14 da LCE 1.100/2021 (roteamento do cálculo), e as redações do
   art. 40 da CF que fundavam a paridade nos regimes de 1988 e 1998.
