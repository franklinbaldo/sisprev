---
type: Achado
id: achado-0055
nome: A regra-0084 grava sentinela em data_adm_ate onde as demais regras do art. 7º da ECE 146/2021 gravam 13/11/2019, a data de ingresso que o caput exige
situacao: aberto
severidade: bloqueante
verificacao: manual
natureza: juridica
regras_afetadas:
  - /regras/regra-0084.md
detectado_em: 2026-07-30
detectado_por: franklinbaldo
---

# Descrição

As regras que vinculam dispositivos do art. 7º da ECE 146/2021 gravam
`data_adm_ate: 13/11/2019`, com exceções que este achado registra. A
`regra-0084`, que vincula o § 2º e o § 3º do mesmo artigo, grava
`31/12/2099 00:00` — valor **sentinela** no conjunto autorado em
`scripts/sentinela.py` (RFC 0011), que por definição não é limite avaliável.

`13/11/2019` é a data que o *caput* do art. 7º nomeia:

> Art. 7º O policial civil, o policial legislativo e o ocupante de cargo de
> policial penal ou agente de segurança socioeducativo **que tenham ingressado
> na respectiva carreira até a data de entrada em vigor da Emenda Constitucional
> nº 103, de 13 de novembro de 2019**, poderão aposentar-se na forma da Lei
> Complementar nº 51, de 20 de dezembro de 1985, com paridade e integralidade,
> observada a idade mínima de 55 (cinquenta e cinco) anos para ambos os sexos ou
> o disposto no § 2º.

O achado afirma duas coisas em camadas: a **divergência de parametrização**,
que é fato do catálogo, e a **leitura jurídica** dela, que repousa sobre a
hipótese de trabalho declarada na seção seguinte.

# Hipótese de trabalho

**`DATA_ADM_*` é a data de admissão** — confirmado pela empresa responsável pelo
Sisprev, registrado em
[`docs/analysis/confirmacoes-do-fornecedor-do-sisprev.md`](../../../docs/analysis/confirmacoes-do-fornecedor-do-sisprev.md),
e assumido aqui como a hipótese sobre a qual este achado é construído.

Isso não é formalidade. A Q1 da RFC 0001 pergunta a que ato o campo se refere, e
[`docs/analysis/semantica-das-janelas-temporais.md`](../../../docs/analysis/semantica-das-janelas-temporais.md)
registra a pergunta como aberta quanto à distinção fina entre nomeação, posse e
exercício. A confirmação do fornecedor não dissolve essa distinção fina, mas
fixa o gênero: o campo marca **entrada no serviço**, não aquisição de direito
nem qualquer outro marco. É o bastante para confrontá-lo com um dispositivo que
recorta por momento de entrada, e é sobre isso que este achado se apoia.

Auditar exige hipótese de trabalho explícita: sem ela, todo campo cuja semântica
fina não esteja fechada ficaria imune a conferência, e o catálogo inteiro sairia
inauditável por uma questão que a própria auditoria existe para resolver. A
hipótese fica declarada para que, se for revista, se saiba exatamente o que
neste achado cai junto.

**Ressalva que sobrevive à hipótese:** "admissão" e "ingresso na respectiva
carreira" podem não coincidir — quem foi admitido no serviço estadual antes de
13/11/2019 e ingressou na carreira policial depois é caso em que os dois marcos
divergem. O *caput* recorta pelo segundo. Se o Sisprev afere o primeiro, há
questão adicional, que a questão 3 registra.

# Evidências

Todas as regras que vinculam `ece-146-2021/art-7-par-1`, `art-7-par-2` ou
`art-7-par-3`, com o valor gravado de `data_adm_ate`:

| regra        | `data_adm_ate`       | sentinela | §§ vinculados |
| ------------ | -------------------- | --------- | ------------- |
| `regra-0072` | 13/11/2019 00:00     | não       | § 2º, § 3º    |
| `regra-0073` | 13/11/2019 00:00     | não       | § 2º, § 3º    |
| `regra-0074` | 13/11/2019 00:00     | não       | § 2º, § 3º    |
| `regra-0075` | 13/11/2019 00:00     | não       | § 2º, § 3º    |
| `regra-0076` | 13/11/2019 00:00     | não       | § 2º, § 3º    |
| `regra-0077` | 13/11/2019 00:00     | não       | § 2º, § 3º    |
| `regra-0078` | 13/11/2019 00:00     | não       | § 1º, § 3º    |
| `regra-0079` | 13/11/2019 00:00     | não       | § 1º, § 3º    |
| `regra-0084` | **31/12/2099 00:00** | **sim**   | § 2º, § 3º    |
| `regra-0109` | 31/12/2024 00:00     | não       | § 2º, § 3º    |
| `regra-0110` | 31/12/2024 00:00     | não       | § 2º, § 3º    |
| `regra-0111` | 31/12/2003 00:00     | não       | § 2º, § 3º    |
| `regra-0112` | 31/12/2003 00:00     | não       | § 2º, § 3º    |

Quatro valores distintos convivem entre regras que declaram vínculo com o mesmo
artigo: `13/11/2019`, `31/12/2024`, `31/12/2003` e sentinela. A `regra-0084` é a
que grava sentinela, e sentinela é o valor cuja leitura a RFC 0011
deliberadamente não fixa.

A divergência é **material**: `data_adm_ate` integra a chave do
`P2_IGUALDADE_MATERIAL_ATIVA` e é campo deployável, exportado ao Sisprev.

# Consequência prática

Sob a hipótese declarada, a `regra-0084` **não recorta por data de entrada**
onde o dispositivo que ela vincula recorta. A direção do desvio importa:
sentinela em `data_adm_ate` **amplia** o universo alcançado, em vez de
restringi-lo. Uma regra de transição sem a fronteira que a define deixa de ser
transição.

Duas coisas que este achado **não** afirma, e que não devem ser lidas nas
entrelinhas:

**Não afirma que alguma concessão tenha ocorrido fora do recorte.** Isso depende
de caso concreto, e o catálogo não registra caso concreto. A `regra-0084` é
`simulavel: N`, então a aferição é humana, e o que o operador faz diante do
campo não é observável daqui.

**Não afirma qual valor é o correto**, nem para a `regra-0084` nem para
`regra-0109`–`regra-0112`. A divergência entre quatro valores é o fato; qual
deles reflete o direito é a investigação, e a questão 2 é anterior a ela.

**Severidade `bloqueante`**, pelo critério de
[`docs/spec/regra.md`](../../../docs/spec/regra.md): sob a hipótese de trabalho,
um campo deployável deixa de aplicar o recorte de incidência do dispositivo que a
regra invoca, com efeito ampliativo. A severidade é **solidária à hipótese** — se
a confirmação do fornecedor for revista, ou se ficar demonstrado que o Sisprev
não afere este campo nesta regra, este é o primeiro item a reclassificar.

# Relação com o que já está registrado

O `achado-0017` alcança a mesma `regra-0084`, por questão distinta — a citação
da alínea feminina da LC 51/1985 numa regra `sexo: AMBOS`. Um é sobre a provisão
citada, o outro sobre o valor gravado num campo de data. Convivem e não se
implicam.

O levantamento em
[`docs/analysis/fontes-do-mandado-de-injuncao-dos-agentes-penitenciarios.md`](../../../docs/analysis/fontes-do-mandado-de-injuncao-dos-agentes-penitenciarios.md)
registra a hipótese de que a `regra-0084` seja cadastro antigo reparametrizado.
Se ela se confirmar, oferece uma explicação possível para a sentinela — o regime
anterior não teria o recorte do art. 7º. A hipótese carece do documento do
IPERON que reconstrua a sucessão, e explicação possível não é causa demonstrada.

# Questão a investigar

1. **A distinção fina da Q1 — nomeação, posse ou exercício.** O gênero está
   fixado pela confirmação do fornecedor; a espécie, não. Ela decide casos de
   fronteira, não este achado.

2. **Por que `regra-0109`–`regra-0112` gravam `31/12/2024` e `31/12/2003`** com
   o mesmo vínculo de dispositivo das que gravam `13/11/2019`. Ou elas se fundam
   em critério que o vínculo declarado não expressa, ou há erro de
   parametrização. Responder isto é anterior a propor valor para a `regra-0084`.

3. **Se "admissão" e "ingresso na carreira policial" coincidem no Sisprev.** O
   *caput* recorta pelo ingresso na carreira; o campo marca admissão. Quem entrou
   no serviço estadual antes de 13/11/2019 e na carreira policial depois é o caso
   em que os dois divergem, e ele atinge todas as regras do art. 7º, não só a
   `regra-0084`. É pergunta ao IPERON como titular do produto.

4. **Como o Sisprev lê `data_adm_ate` sentinela numa regra `simulavel: N`.** Se a
   triagem é humana, o campo pode nunca ser aferido pelo sistema, e a questão
   passa a ser o que o operador entende ao vê-lo.

5. **Se o art. 40, § 4º-B da CF deveria integrar a fundamentação** das regras do
   art. 7º. Ele nomeia agente penitenciário, agente socioeducativo e policial, e
   está transcrito no bundle (`cf88/art-40-par-4b/ec-103-2019`), vinculado por
   `regra-0080`–`regra-0083` e não pelas do art. 7º. A omissão de um dispositivo
   não é erro por si — a fundamentação é articulação autorada —, mas a assimetria
   entre dois blocos da mesma matéria merece decisão registrada.
