# Conferência `critério → dispositivo` — as 12 regras de transição (EC 41/2003 e EC 47/2005)

> **Nota:** Relatório gerado por IA como apoio à decisão. **Não é artefato
> oficial**, não edita nenhuma `regra-*.md`, nenhum `achado-*.md`, nenhum
> dispositivo, não altera schema, dados derivados
> (`data/regras-sisprev.csv`), motor ou `site/`. É a segunda aplicação da
> conferência descrita na RFC 0008 §5 — para cada critério da regra, qual
> dispositivo o funda —, agora sobre as doze regras de aposentadoria
> voluntária fundadas nas **regras de transição** das Emendas 41/2003 e
> 47/2005. Toda conclusão sobre citação é ato humano, em achado próprio.

## O método, e a distinção que ele exige

A RFC 0008 §5 registra a definição da coordenação da auditoria: a
fundamentação **articula** os dispositivos de forma a fundamentar os
critérios da própria regra, cada um deles. Logo a relação é
`critério → dispositivo(s)`, e `dispositivos:` é a união achatada dela.
Conferir é desachatar.

Duas perguntas diferentes convivem nesta página e **não coincidem**:

1. *"qual dispositivo funda este critério?"* — jurídica, é o que a
   conferência responde;
2. *"o que este campo cita?"* — de leitura, é o que `dispositivos:` registra.

Um `dispositivos:` afirma apenas a segunda ([`docs/spec/dispositivo.md`](../spec/dispositivo.md)).
A conferência anterior errou por confundi-las, nas duas direções, e a seção
final daquele relatório registra o erro. Aqui a separação é mantida
explícita: toda vez que um critério ficou sem fundamento, a pergunta
seguinte foi *"e algum campo da regra cita algo que o fundaria?"* — e quando
a resposta foi não, o resultado é **lacuna a decidir**, nunca vínculo a
acrescentar.

## As doze regras, lado a lado

Todas: `tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO`,
`tipo: CIVIL`, `atualmente_no_sistema: TRUE`, `integral: S`,
`validado_pge: FALSE`, `validado_presidencia: FALSE`, `tabelapontuacao: N`,
`requisitos_da_in_no_5_2020: N`, `adicional_inatividade: N`,
`relatorio_p_reserva_remunerada_por_idade_ex_officio: N`, `tipo_remun` vazio,
`fundamentacao` e `fundamentacao_proporcional` **vazios** (a regra inteira
vive em `fundamentacao_integral`), `visivel_dtc_*: N`. Nenhuma das doze tem
corpo — nenhuma seção P13.1 foi escrita.

Três famílias, pelo artigo de transição que cada uma invoca:

| campo                | **A** — art. 2º EC 41                | **B** — art. 6º EC 41       | **C** — art. 3º EC 47 (ciclo 3º) | **C'** — art. 3º EC 47 (ciclo 4º) |
| -------------------- | ------------------------------------ | --------------------------- | -------------------------------- | --------------------------------- |
| regras               | 0097–0100                            | 0101–0104                   | 0085, 0086                       | 0105, 0106                        |
| `ciclo_de_validacao` | 4º                                   | 4º                          | **3º**                           | 4º                                |
| `simulavel`          | S                                    | S                           | **N**                            | S                                 |
| `paridade`           | **N**                                | S                           | S                                | S                                 |
| `tipo_calculo`       | **Valor Médio com Redutor da Idade** | Remuneração de Contribuição | Remuneração de Contribuição      | Remuneração de Contribuição       |
| `data_adm_ate`       | 16/12/1998                           | **31/12/2003**              | 16/12/1998                       | 16/12/1998                        |
| `data_direito_apos`  | 31/12/2003                           | 31/12/2003                  | **01/01/1950**                   | 31/12/2003                        |
| `data_direito_ate`   | 31/12/2024                           | 31/12/2024                  | **31/12/2099**                   | 31/12/2024                        |
| `apos_especial: S`   | 0099, 0100                           | 0103, 0104                  | —                                | —                                 |

Dentro de cada família, `sexo` é o que separa as gêmeas — e é por isso que
o P2 não as agrupa. O que o P1 registra são seis grupos de `nome` repetido,
um por par (`0085/0086`, `0097/0098`, `0099/0100`, `0101/0102`,
`0103/0104`, `0105/0106`).

## A conferência

### Família A — art. 2º da EC 41/2003 (0097, 0098, 0099, 0100)

`dispositivos:` das quatro: `cf88/art-40-par-1-inc-iii/ec-103-2019`,
`ec-41-2003/art-2/original`, `ece-146-2021/art-4/original`. Os três estão
citados em `fundamentacao_integral`, e nada além deles está.

| critério                               | valor                            | fundado por                                                                                                          | fecha?          |
| -------------------------------------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------- | --------------- |
| tipo de benefício                      | voluntária por tempo de contrib. | `ec-41-2003/art-2` — "é assegurado o direito de opção pela aposentadoria voluntária"                                 | ✅              |
| `sexo` (MASC 0097/0099, FEM 0098/0100) | um por regra                     | nenhuma provisão transcrita distingue por sexo                                                                       | ⛔ ver §3       |
| `data_adm_ate: 16/12/1998`             | ingresso até a EC 20/1998        | `ec-41-2003/art-2` — "até a data de publicação **daquela** Emenda", e `ec-20-1998` tem `vigencia_inicio: 1998-12-16` | ✅ por remissão |
| `data_direito_apos: 31/12/2003`        | direito a partir da EC 41        | `ec-41-2003` tem `vigencia_inicio: 2003-12-31`                                                                       | ✅              |
| `data_direito_ate: 31/12/2024`         | prazo de implementação           | `ece-146-2021/art-4` — "desde que sejam cumpridos até 31 de dezembro de 2024"                                        | ✅ literal      |
| `integral: S`                          | proventos integrais              | nenhuma provisão transcrita; o caput do art. 2º só remete o cálculo                                                  | ⚠️ ver §5       |
| `tipo_calculo: Valor Médio ...`        | média das contribuições          | `ec-41-2003/art-2` — "proventos calculados de acordo com o art. 40, §§ 3º e 17" (§§ não transcritos)                 | ⚠️ por remissão |
| ... **com Redutor da Idade**           | redutor por antecipação          | o redutor está em parte do art. 2º que **não foi transcrita**                                                        | ⚠️ ver §5       |
| `paridade: N`                          | sem paridade                     | o art. 2º nada estende do art. 7º da EC 41 — o campo diz "sem paridade"                                              | ✅ por ausência |
| `apos_especial: S` (0099, 0100)        | magistério                       | **nada** — nenhum campo da regra menciona professor ou magistério                                                    | ⛔ ver §2       |
| art. 40, § 1º, III, 2ª parte           | —                                | não funda critério nenhum                                                                                            | ⚠️ ver §6       |

### Família B — art. 6º da EC 41/2003 (0101, 0102, 0103, 0104)

`dispositivos:` de 0101/0102: `cf88/art-40-par-1-inc-iii/ec-103-2019`,
`ec-41-2003/art-6/original`, `ece-146-2021/art-4/original`. As de 0103/0104
acrescentam `lce-432-2008/art-24`, `art-46` e `art-63` — e a
`fundamentacao_integral` delas cita exatamente "artigos 24, 46 e 63 da Lei
Complementar nº 432/2008". Os vínculos são fiéis aos campos nas quatro.

| critério                                    | valor                     | fundado por                                                                                                                                                | fecha?     |
| ------------------------------------------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| tipo de benefício                           | voluntária por tempo      | `ec-41-2003/art-6` — "poderá aposentar-se com proventos integrais"                                                                                         | ✅         |
| `data_adm_ate: 31/12/2003`                  | ingresso até a EC 41      | `ec-41-2003/art-6` — "até a data de publicação **desta** Emenda"; e, em 0103/0104, `lce-432-2008/art-46` diz **literalmente** "até 31 de dezembro de 2003" | ✅         |
| `data_direito_apos: 31/12/2003`             | direito a partir da EC 41 | `ec-41-2003`, `vigencia_inicio: 2003-12-31`                                                                                                                | ✅         |
| `data_direito_ate: 31/12/2024`              | prazo de implementação    | `ece-146-2021/art-4`, texto literal                                                                                                                        | ✅ literal |
| `integral: S`                               | integrais                 | `ec-41-2003/art-6` — "proventos integrais"                                                                                                                 | ✅         |
| `tipo_calculo: Remuneração de Contribuição` | totalidade da remuneração | `ec-41-2003/art-6` — "corresponderão à totalidade da remuneração do servidor no cargo efetivo"; em 0103/0104 também `lce-432-2008/art-46`                  | ✅         |
| `paridade: S` — **0103/0104**               | reajuste com paridade     | `lce-432-2008/art-63` — "na mesma proporção e na mesma data, sempre que se modificar a remuneração dos servidores em atividade"                            | ✅         |
| `paridade: S` — **0101/0102**               | reajuste com paridade     | **nada citado, e nada transcrito**                                                                                                                         | ⛔ ver §4  |
| `apos_especial: S` (0103, 0104)             | magistério                | `lce-432-2008/art-24` (redução de 5 anos), incorporado por `art-46` — e a regra diz "Aposentadoria especial de professor"                                  | ✅         |
| art. 40, § 1º, III, 2ª parte                | —                         | não funda critério nenhum                                                                                                                                  | ⚠️ ver §6  |

A cadeia de 0103/0104 merece registro porque **só fecha lida como cadeia** —
e uma leitura descuidada produziria uma contradição inexistente. O art. 24
da LCE 432/2008 concede a redução de cinco anos "quando da aposentadoria
prevista no **art. 22**", e seu § 4º manda calcular "na forma do art. 45"
(a média). Se o art. 24 fosse lido isolado, contradiria o
`tipo_calculo: Remuneração de Contribuição` gravado. Não contradiz: é o
art. 46 que incorpora do art. 24 **apenas** "as reduções de idade e tempo de
contribuição", mantendo o próprio cálculo pela totalidade da remuneração, e
remetendo o reajuste ao art. 63 no seu § 1º. Três dispositivos, três
critérios distintos, uma ordem de leitura que o `dispositivos:` achatado não
carrega.

### Família C — art. 3º da EC 47/2005 (0085, 0086, 0105, 0106)

`dispositivos:` das quatro: `cf88/art-40-par-1-inc-iii/ec-103-2019`,
`ec-47-2005/art-3/original`, `ece-146-2021/art-4/original`. Fiéis aos campos.

| critério                                    | valor                     | fundado por                                                                                                                        | fecha?     |
| ------------------------------------------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| tipo de benefício                           | voluntária por tempo      | `ec-47-2005/art-3` — "poderá aposentar-se com proventos integrais"                                                                 | ✅         |
| `data_adm_ate: 16/12/1998`                  | ingresso até 16/12/1998   | `ec-47-2005/art-3` — "que tenha ingressado no serviço público **até 16 de dezembro de 1998**"                                      | ✅ literal |
| `integral: S`                               | integrais                 | `ec-47-2005/art-3` — "com proventos integrais"                                                                                     | ✅         |
| `tipo_calculo: Remuneração de Contribuição` | totalidade                | o art. 3º diz "proventos integrais" sem definir a base; a definição vem do art. 7º da EC 41, via parágrafo único **não vinculado** | ⚠️ ver §7  |
| `paridade: S`                               | com paridade              | `ec-47-2005/art-3-par-unico` — remete ao art. 7º da EC 41/2003 — **transcrito, não vinculado**                                     | ⚠️ ver §7  |
| "FÓRMULA 85/95" (no `nome`)                 | soma idade + contribuição | condição inscrita nos incisos do art. 3º, **não transcritos**                                                                      | ⚠️ ver §5  |
| `data_direito_ate` — **0105/0106**          | 31/12/2024                | `ece-146-2021/art-4`, texto literal                                                                                                | ✅ literal |
| `data_direito_ate` — **0085/0086**          | 31/12/2099 (sentinela)    | citam o mesmo art. 4º, que fixa 31/12/2024                                                                                         | ⛔ ver §1  |
| `data_direito_apos` — **0105/0106**         | 31/12/2003                | marco da EC 41/2003, não da EC 47/2005 (sem vigência autorada)                                                                     | ⚠️ ver §8  |
| `data_direito_apos` — **0085/0086**         | 01/01/1950 (sentinela)    | nada; e diverge de 0105/0106, mesma citação                                                                                        | ⛔ ver §1  |
| art. 40, § 1º, III, 2ª parte                | —                         | não funda critério nenhum                                                                                                          | ⚠️ ver §6  |

## O que a conferência revelou

### 1. Duas regras gravam a sentinela onde outras duas, com a mesma citação, gravam o prazo

`regra-0085`/`0086` e `regra-0105`/`0106` citam **as mesmas três provisões**,
têm o mesmo benefício, o mesmo `integral`, o mesmo `tipo_calculo`, a mesma
`paridade`, o mesmo `apos_especial` e o mesmo `data_adm_ate`. Divergem em:

| campo                | 0085 / 0086    | 0105 / 0106    |
| -------------------- | -------------- | -------------- |
| `ciclo_de_validacao` | 3º             | 4º             |
| `simulavel`          | N              | S              |
| `data_adm_apos`      | 01/01/1950     | 01/01/1910     |
| `data_direito_apos`  | 01/01/1950     | **31/12/2003** |
| `data_direito_ate`   | **31/12/2099** | **31/12/2024** |

`data_direito_ate` é a divergência grave, porque o valor **não é indiferente
ao dispositivo citado**: o art. 4º da ECE 146/2021, que as quatro citam e as
quatro vinculam, condiciona a preservação do regime a que os requisitos
"sejam cumpridos até 31 de dezembro de 2024". Duas das quatro gravam esse
prazo; duas gravam a sentinela `31/12/2099`, que o catálogo não interpreta
(P5) e que na prática não fecha janela nenhuma.

É o mesmo padrão do achado nº 2 da conferência de invalidez, mas mais forte
aqui: lá o contraste era com regras de outra família; aqui **as quatro regras
articulam a mesma fundamentação** e ainda assim gravam valores diferentes.
Ou 0085/0086 são regra distinta cuja distinção nenhum campo expressa, ou
uma das duas metades está errada. A conferência não decide qual — mas o par
que difere apenas em `sexo` de 0105/0106, com fundamentação equivalente e
janela incompatível, é o objeto mais óbvio de decisão deste grupo.

`simulavel: N` em 0085/0086 e `S` em 0105/0106 reforça a leitura de que o
par antigo pode ser resíduo: o catálogo já não as oferece ao simulador.

### 2. `apos_especial: S` em 0099/0100 não tem fundamento em campo nenhum da regra

`regra-0097` e `regra-0099` diferem **apenas** em `nome` e `apos_especial`
(o mesmo vale para `0098`/`0100`). Todos os demais campos, incluindo
`fundamentacao_integral` **caractere por caractere**, são idênticos. E o
texto compartilhado não menciona professor, magistério, nem redução de
idade por exercício de magistério — é a fundamentação genérica do art. 2º da
EC 41/2003.

Isto é diferente do que ocorre na família B, onde a mesma distinção **está**
fundamentada: 0103/0104 dizem "Aposentadoria especial de professor" e citam
os arts. 24, 46 e 63 da LCE 432/2008, sendo o art. 24 exatamente a redução de
cinco anos para o magistério. A família A carrega o mesmo critério sem
nenhum correspondente na fundamentação.

O que **não** se conclui daqui: que 0099/0100 estejam erradas. O art. 2º da
EC 41/2003 está transcrito apenas no caput; se algum de seus parágrafos
concede acréscimo ou redução ao professor, ele está fora do corpus e a
conferência não pode afirmar nem negar. O que se conclui é mais estreito e
suficiente: **nenhum campo dessas duas regras cita o que fundaria seu
`apos_especial: S`**, e por isso nenhum vínculo pode ser proposto.

### 3. `sexo` não é fundado por nenhuma provisão transcrita, nas doze

`sexo` é a única coluna de domínio que separa as gêmeas de cada par, e é
material para o P2 (CLAUDE.md, "O que é uma regra"). Nas doze, ele não é
fundado por nenhuma provisão transcrita: os requisitos diferenciados por
sexo estão nos **incisos** dos arts. 2º e 6º da EC 41 e do art. 3º da EC 47,
que não foram transcritos, e no art. 46 da LCE 432/2008 — este sim
transcrito, com "60 (sessenta) anos de idade, se homem, e 55 (cinquenta e
cinco) anos de idade, se mulher", e vinculado apenas em 0103/0104.

Ou seja: **das doze regras, só duas têm o critério `sexo` fundado por um
dispositivo que elas próprias vinculam** — e por acidente, porque o art. 46
foi citado pela integralidade, não pelo sexo. É a demonstração mais direta
de que o achatamento esconde: `lce-432-2008/art-46` funda quatro critérios
distintos em 0103/0104 e aparece no `dispositivos:` como uma linha entre
seis.

### 4. `paridade: S` em 0101/0102 não é fundada por nada citado nem transcrito

O art. 6º da EC 41/2003, transcrito no caput, não diz nada sobre reajuste. A
paridade dessas aposentadorias vem do art. 7º da mesma Emenda — que **não
está transcrito no corpus** e **não é citado** por nenhum campo de
0101/0102.

De novo o contraste interno à família resolve a pergunta pelo lado certo:
0103/0104, mesma transição, citam e vinculam o `lce-432-2008/art-63`, que é
a norma estadual de paridade e cobre expressamente "as aposentadorias de que
trata o art. 46". Os arts. 46 e 63 alcançariam 0101/0102 tanto quanto
0103/0104 — mas **elas não os citam**, e o vínculo registra citação, não
fundamento. Portanto: nada a acrescentar em `dispositivos:`; o que há é
divergência entre dois campos deployable (`fundamentacao_integral` de
0101/0102 e de 0103/0104) sobre a base legal do mesmo efeito jurídico. É
decisão do auditor sobre o texto do campo, no mesmo formato do item 3 da
conferência de invalidez.

### 5. Os três artigos de transição estão transcritos só no caput — e é aí que estão os requisitos

`ec-41-2003/art-2/original`, `ec-41-2003/art-6/original` e
`ec-47-2005/art-3/original` são documentos de **artigo inteiro**
(`componentes` sem `caput`), mas seus corpos terminam em
"quando o servidor, cumulativamente:" / "vier a preencher, cumulativamente,
as seguintes condições:" / "desde que preencha, cumulativamente, as
seguintes condições:". Os incisos não estão.

Isso é legítimo — a transcrição é sob demanda (P3, "decomposição sob
demanda") — mas tem consequência direta na conferência: **idade mínima,
tempo de contribuição, tempo de serviço público, tempo de carreira, o redutor
de idade do art. 2º e a "fórmula 85/95" do art. 3º são todos critérios cujo
fundamento está fora do corpus**. Nenhum deles é coluna do Sisprev, o que
limita o dano; mas o `nome` de quatro regras (0085, 0086, 0105, 0106) afirma
"FÓRMULA 85/95" sem que nada transcrito a sustente, e `tipo_calculo`
carrega "com Redutor da Idade" na mesma situação.

Vale registrar o que **está** conferido apesar da lacuna: o
`tabelapontuacao: N` das quatro regras da fórmula 85/95 é coerente com o uso
que o catálogo faz do campo — as onze regras com `tabelapontuacao: S` são
todas de transições da ECE 146/2021 (arts. 5º e 8º), com tabela progressiva.
A soma fixa do art. 3º da EC 47 não é tabela nesse sentido.

### 6. O art. 40, § 1º, III não funda critério nas doze — mas aqui não é o caso da invalidez

As doze vinculam `cf88/art-40-par-1-inc-iii/ec-103-2019`, e as doze aparecem
na lista congelada de pendências como `ESTREITADA` ("segunda parte"). Nenhum
dos critérios conferidos acima é fundado por ele: a idade mínima dessas
regras vem do artigo de transição, não do inciso III.

Mas a leitura honesta aqui difere da que a conferência de invalidez alcançou.
Lá o inciso III era do benefício **errado** — tratava de aposentadoria
voluntária por idade, num grupo de regras de incapacidade. Aqui o benefício é
o certo, e a "segunda parte" ("no âmbito dos Estados, do Distrito Federal e
dos Municípios, na idade mínima estabelecida mediante emenda às respectivas
Constituições") é plausivelmente citada como **elo de competência** — o que
autoriza a ECE 146/2021, cujo art. 4º é o que preserva o regime anterior.
Uma articulação pode conter um elo que não funda critério algum sem por isso
ser falsa.

Registro, portanto, sem propor remoção: *não funda critério* é fato
conferido; *é citação indevida* é conclusão que esta página não alcança.

### 7. Um dispositivo transcrito, que fundaria dois critérios, e que ninguém vinculou

`ec-47-2005/art-3-par-unico/original` está no bundle, transcrito, e é o
único texto do corpus que funda a `paridade: S` e a base de cálculo de
0085/0086/0105/0106 — remete ao art. 7º da EC 41/2003. As quatro regras
citam "artigo 3º da Emenda Constitucional nº 47/2005", sem estreitar.

A pergunta é de **granularidade de leitura**, não de mérito: uma citação a
"artigo 3º", sem qualificador, alcança o parágrafo único do artigo? Se
alcança, o vínculo caberia; se a convenção é que o vínculo siga o endereço
literalmente escrito, não cabe.

Complica um pouco: `ec-47-2005/art-3/original` está endereçado como artigo
inteiro (`componentes: [artigo 3]`, sem componente `caput`), mas transcreve
**apenas o caput**. Quem clica no vínculo que a regra tem hoje lê um
documento chamado "art. 3º" que não contém o parágrafo único do art. 3º.
Isso é observação sobre o corpus, conferível, e não acusação jurídica — mas
é o que faz a pergunta acima não ser acadêmica.

**Não proponho o vínculo.** Proponho que a decisão seja tomada, e registro
por que ela não é dedutível: propor `art-3-par-unico` porque ele funda a
paridade seria exatamente o erro da conferência anterior (art. 20, § 9º na
regra-0006).

### 8. Conferência das janelas contra os dispositivos citados

Aplicando o critério da [semântica das janelas](semantica-das-janelas-temporais.md)
§2 — todo limite não-sentinela deve coincidir com uma data declarada por um
dispositivo que a própria regra cita:

| regras           | campo               | valor      | dispositivo que declara a data                                                   | fecha?              |
| ---------------- | ------------------- | ---------- | -------------------------------------------------------------------------------- | ------------------- |
| 0097–0100        | `data_adm_ate`      | 16/12/1998 | `ec-41-2003/art-2` → "publicação daquela Emenda" → EC 20/1998                    | ✅                  |
| 0101–0104        | `data_adm_ate`      | 31/12/2003 | `ec-41-2003/art-6` → "publicação desta Emenda"; e `lce-432-2008/art-46`, literal | ✅                  |
| 0085/86, 0105/06 | `data_adm_ate`      | 16/12/1998 | `ec-47-2005/art-3`, literal no texto                                             | ✅                  |
| 0097–0106        | `data_direito_apos` | 31/12/2003 | `ec-41-2003`, `vigencia_inicio`                                                  | ✅ / ⚠️ (0105/0106) |
| 0097–0106        | `data_direito_ate`  | 31/12/2024 | `ece-146-2021/art-4`, literal no texto                                           | ✅                  |
| 0085, 0086       | `data_direito_ate`  | 31/12/2099 | sentinela; contradiz o art. 4º que a regra cita                                  | ⛔                  |
| 0085, 0086       | `data_direito_apos` | 01/01/1950 | sentinela; nada no corpus a sustenta                                             | ⛔                  |
| todas            | `data_adm_apos`     | sentinelas | P5 — não interpretadas                                                           | —                   |

**Isto responde, para dez destas doze regras, a pergunta 5.2.08 da semântica
das janelas** ("Qual norma fixa 31/12/2024?"). A resposta estava no corpus
desde que `ece-146-2021/art-4/original` foi transcrito: o prazo é fixado
**no texto do próprio dispositivo**, não pela vigência de nenhuma norma —
"desde que sejam cumpridos até 31 de dezembro de 2024". Era exatamente a
hipótese que aquele documento levantou ("prazo de regra de transição e não
vigência de norma"), aqui confirmada contra o texto. A conferência não
alcança as demais ocorrências de 31/12/2024 no catálogo, em especial as seis
que o gravam em `data_adm_ate` — o art. 4º não estabelece data de ingresso, e
nenhuma das doze regras deste grupo o usa assim.

Duas ressalvas honestas sobre `data_direito_apos: 31/12/2003` em 0105/0106:
`ec-47-2005/norma.md` **não tem `vigencia_inicio` autorada** (é um dos sete
buracos da §5.1 daquele documento), então o valor não é conferível contra a
norma que a regra invoca; e a §5.3.2 registra que a semântica de
`DATA_DIREITO_APOS` não foi confirmada. O valor coincide com o marco da
EC 41/2003, não com o da EC 47/2005. Há explicação possível numa disposição
da própria EC 47 que não está transcrita nem citada — **não a afirmo**, pelo
motivo que este trabalho inteiro existe para respeitar.

### 9. `data_adm_apos` usa três sentinelas diferentes dentro do mesmo grupo

`01/01/1950` em 0085, 0086, 0097–0100, 0103, 0104; `01/01/1910` em 0101,
0102, 0105, 0106. A divergência atravessa famílias e chega a atravessar um
par irmão: 0101/0102 gravam 1910 e 0103/0104, mesma transição do art. 6º,
gravam 1950. Sob P5 nenhuma das duas é interpretada, então isto não é erro —
mas é evidência empírica para a pergunta 5.3.4 daquele documento ("são três
valores para o mesmo sentido, ou distinguem algo?"): dentro de uma mesma
família jurídica, a escolha entre 1910 e 1950 não acompanha nenhum critério
identificável.

## Vínculos: nada a acrescentar, nada a remover

As doze regras têm `dispositivos:` **fiéis aos seus campos**. Conferido campo
a campo (`fundamentacao_integral` é o único preenchido nas doze;
`fundamentacao` e `fundamentacao_proporcional` estão vazios):

| regras     | o que `fundamentacao_integral` cita                                                           | vinculado |
| ---------- | --------------------------------------------------------------------------------------------- | --------- |
| 0085, 0086 | art. 3º EC 47/05; art. 4º ECE 146/21; art. 40 § 1º III 2ª parte                               | os 3      |
| 0097–0100  | art. 40 § 1º III 2ª parte; art. 4º ECE 146/21; art. 2º EC 41/03                               | os 3      |
| 0101, 0102 | art. 40 § 1º III 2ª parte; art. 4º ECE 146/21; art. 6º EC 41/03                               | os 3      |
| 0103, 0104 | art. 6º EC 41/03; arts. 24, 46 e 63 LCE 432/08; art. 4º ECE 146/21; art. 40 § 1º III 2ª parte | os 6      |
| 0105, 0106 | art. 40 § 1º III 2ª parte; art. 4º ECE 146/21; art. 3º EC 47/05                               | os 3      |

Nenhuma citação ficou sem vínculo, nenhum vínculo ficou sem citação — salvo
a pergunta de granularidade do §7. **Os problemas deste grupo não estão nos
vínculos; estão nos valores gravados e nos textos dos campos de
fundamentação.**

## O que decorre, e para quem

**Para o auditor** (ato humano, achado próprio):

1. Decidir a divergência de `data_direito_ate` entre 0085/0086 (31/12/2099) e
   0105/0106 (31/12/2024), com a mesma fundamentação e o mesmo vínculo ao
   art. 4º da ECE 146/2021 — e, junto com ela, a de `data_direito_apos`
   (01/01/1950 vs 31/12/2003). Campo deployable; sob a RFC 0006 o veículo
   indicado para a correção é um `Conjunto` `proposto`, não edição in-place.
2. Decidir se 0085/0086 e 0105/0106 são quatro regras ou duas — o par de
   ciclo 3º, não simulável, pode ser resíduo de um ciclo anterior.
3. Decidir o `apos_especial: S` de 0099/0100, sem qualquer correspondente na
   fundamentação que compartilham integralmente com 0097/0098.
4. Decidir se a `fundamentacao_integral` de 0101/0102 deve invocar a base
   estadual da paridade, como a de 0103/0104 faz (arts. 46 e 63 da LCE
   432/2008). É mudança de campo deployable, não de vínculo.
5. Decidir a granularidade do §7: uma citação a "artigo 3º da EC 47/2005"
   alcança `ec-47-2005/art-3-par-unico`?
6. Decidir a citação do art. 40, § 1º, III nas doze — com a ressalva do §6 de
   que aqui, ao contrário do grupo de invalidez, há leitura defensável.

**Para quem transcreve dispositivos** (P3, sob demanda):

7. Os incisos dos arts. 2º e 6º da EC 41/2003 e do art. 3º da EC 47/2005, e
   os parágrafos do art. 2º (redutor de idade; eventual regra de magistério).
   Sem eles, `sexo`, o redutor, a fórmula 85/95 e o `apos_especial` da
   família A permanecem sem fundamento conferível.
8. O art. 7º da EC 41/2003 — referenciado pelo parágrafo único do art. 3º da
   EC 47 e fundamento da paridade de metade deste grupo, ausente do corpus.
9. A `vigencia_inicio` da EC 47/2005 (§5.1 da semântica das janelas), sem a
   qual `data_direito_apos: 31/12/2003` de 0105/0106 não é conferível.

## Pontos em aberto

- **Q6, de novo, por outro caminho.** Na família A, o critério que separa
  0097/0098 de 0099/0100 (magistério) não está em campo nenhum além do
  `apos_especial` — que é a *marcação* do resultado, não o critério aferido,
  e não vem acompanhado de fundamentação que o justifique. Na família B, o
  mesmo critério está fundamentado. A pergunta "onde mora o critério que o
  cadastro não grava" reaparece intacta.
- **Se 0085/0086 são legitimamente distintas de 0105/0106**, a distinção não
  é expressável no schema atual — seria o caso de
  `P2_IGUALDADE_MATERIAL_ATIVA` descrito no CLAUDE.md ("regras legitimamente
  distintas cuja distinção o catálogo não consegue expressar"), exceto que
  aqui o P2 não as agrupa, porque as janelas divergem. O detector se cala
  justamente onde a divergência é o problema.
- **`DATA_DIREITO_APOS` continua sem semântica confirmada** (§5.3.2). Tudo o
  que esta conferência diz sobre esse campo vale sob a leitura simétrica
  presumida, e cai se ela for outra.
- **Nenhuma das doze tem corpo P13.1.** Esta página não substitui a seção
  `# Estado da análise` de nenhuma delas — é insumo para escrevê-las, e a
  quinta pergunta da P13.1 ("dispositivos que justificam cada critério e
  efeito") é exatamente o que as tabelas acima instruem, sem autorá-las.

## O que esta conferência recusou concluir

- Que o art. 40, § 1º, III seja citação indevida nestas doze (§6).
- Que `apos_especial: S` de 0099/0100 esteja errado — só que nada nos campos
  dela o funda (§2).
- Que a EC 47/2005 tenha vigência em qualquer data específica, e portanto
  qualquer veredito sobre `data_direito_apos: 31/12/2003` de 0105/0106 (§8).
- Que `ec-47-2005/art-3-par-unico` deva ser vinculado (§7).
- Qualquer conteúdo dos incisos não transcritos dos três artigos de
  transição, inclusive os que a memória sobre a legislação brasileira
  ofereceria de pronto (§5).

## Referências

- RFC 0008 §5, `critério → dispositivo` como conferência humana,
  [`docs/rfc/0008-traducao-sem-perdas-entre-os-dois-esquemas.md`](../rfc/0008-traducao-sem-perdas-entre-os-dois-esquemas.md)
- Conferência anterior e o erro que ela registra,
  [`conferencia-criterio-dispositivo-invalidez-0006-0009.md`](conferencia-criterio-dispositivo-invalidez-0006-0009.md)
- Semântica das janelas temporais, especialmente §2, §5.1 e §5.2.08,
  [`semantica-das-janelas-temporais.md`](semantica-das-janelas-temporais.md)
- Pendências de citação congeladas (as doze constam como `ESTREITADA`),
  [`pendencias-de-citacao-congeladas.md`](pendencias-de-citacao-congeladas.md)
- Contrato do dispositivo e da norma, [`docs/spec/dispositivo.md`](../spec/dispositivo.md)
- Definição de trabalho de "regra" e P13.1, [`docs/spec/regra.md`](../spec/regra.md)
