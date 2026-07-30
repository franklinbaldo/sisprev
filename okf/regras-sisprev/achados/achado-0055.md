---
type: Achado
id: achado-0055
nome: A regra-0084 grava sentinela em data_adm_ate, sem o recorte de ingresso até 13/11/2019 que o caput do art. 7º da ECE 146/2021 exige
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

O *caput* do art. 7º da ECE 146/2021 condiciona a regra de transição ao momento
de ingresso na carreira:

> Art. 7º O policial civil, o policial legislativo e o ocupante de cargo de
> policial penal ou agente de segurança socioeducativo **que tenham ingressado
> na respectiva carreira até a data de entrada em vigor da Emenda Constitucional
> nº 103, de 13 de novembro de 2019**, poderão aposentar-se na forma da Lei
> Complementar nº 51, de 20 de dezembro de 1985, com paridade e integralidade,
> observada a idade mínima de 55 (cinquenta e cinco) anos para ambos os sexos ou
> o disposto no § 2º.

O recorte não é acessório: é a condição que separa quem alcança a transição de
quem cai na regra permanente. A `regra-0084` invoca o § 2º e o § 3º desse
artigo — que existem apenas dentro dele e dependem do *caput*, expressamente
("os servidores de que trata o *caput*") — e grava
`data_adm_ate: 31/12/2099 00:00`.

Esse valor é **sentinela**, no conjunto autorado em `scripts/sentinela.py`
(RFC 0011). Ele não é limite avaliável: o motor não exclui por ele, e ele não
credita critério. O efeito prático é que a regra deixa de recortar por data de
ingresso, quando o dispositivo que a funda recorta.

# Evidências

**As regras irmãs do mesmo artigo gravam a data do dispositivo.** Todas as
regras que vinculam `ece-146-2021/art-7-par-1`, `art-7-par-2` ou `art-7-par-3`,
com o valor de `data_adm_ate`:

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

`13/11/2019` é exatamente a data que o *caput* nomeia. O bloco `regra-0072` a
`regra-0079` grava esse valor; a `regra-0084`, fundada no mesmo § 2º, grava
sentinela.

**A discrepância não se explica pela via de concessão.** A `regra-0084` é
`simulavel: N`, isto é, depende de triagem humana. Isso muda quem lê o campo,
não o que o campo afirma: um limite sentinela num campo de recorte informa ao
leitor que a regra não tem fronteira de ingresso, e o *caput* do dispositivo que
ela cita diz que tem.

**Direção do erro.** Sentinela em `data_adm_ate` **amplia** o universo de
elegíveis: alcança quem ingressou depois de 13/11/2019, a quem a transição não
se destina. O erro não é de precisão, é de extensão, e favorece a concessão
indevida em vez de barrá-la.

# Consequência prática

O que está comprovado é **incompatibilidade entre um campo deployável e o
dispositivo que a própria regra vincula**, na direção que amplia a elegibilidade.

O que **não** se afirma: que alguma concessão tenha efetivamente ocorrido fora
do recorte. Isso depende de caso concreto, e o catálogo não registra caso
concreto. Também não se afirma qual é o valor correto para as demais regras do
§ 2º — ver a questão 2 abaixo.

**Severidade `bloqueante`**, pelo critério de
[`docs/spec/regra.md`](../../../docs/spec/regra.md): o campo deployável contradiz
o critério de incidência do dispositivo que a regra invoca, e a contradição tem
efeito ampliativo sobre quem a regra alcança.

# Relação com o que já está registrado

O `achado-0017` alcança a mesma `regra-0084`, por defeito distinto: lá é a
citação da alínea feminina da LC 51/1985 numa regra `sexo: AMBOS`. Este achado
não o substitui nem depende dele — um é sobre a provisão citada, o outro sobre o
recorte temporal gravado. Convivem, e a `regra-0084` responde aos dois.

O levantamento de fontes em
[`docs/analysis/fontes-do-mandado-de-injuncao-dos-agentes-penitenciarios.md`](../../../docs/analysis/fontes-do-mandado-de-injuncao-dos-agentes-penitenciarios.md)
registra o que se apurou sobre a origem da regra. Ele é contexto: a hipótese de
que a regra seja um cadastro antigo do MI 1.545 reparametrizado explicaria por
que o recorte do art. 7º não foi aplicado a ela — o regime do MI não tinha esse
recorte. **Explicação não é justificação**: se a fundamentação gravada é a do
art. 7º, o recorte do art. 7º incide.

# Questão a investigar

1. **Qual o valor correto de `data_adm_ate` para a `regra-0084`.** Se a
   fundamentação gravada permanecer a do art. 7º da ECE 146/2021, o *caput*
   indica `13/11/2019`, como nas irmãs. Se a regra dever voltar a ser a do
   regime do MI 1.545 — art. 57 da Lei 8.213/1991 —, então é a fundamentação que
   está errada, e não a data, e a correção é outra.

2. **Por que `regra-0109` a `regra-0112` gravam recortes diferentes das demais
   do § 2º.** São `31/12/2024` e `31/12/2003`, contra `13/11/2019` do bloco
   `regra-0072`–`regra-0079`, com o mesmo vínculo de dispositivo. Ou elas se
   fundam em critério que o vínculo declarado não expressa, ou há erro. A
   pergunta é anterior a qualquer correção: mexer na `regra-0084` sem responder
   isto arrisca alinhá-la ao valor errado.

3. **Se o art. 40, § 4º-B da CF deveria integrar a fundamentação** das regras do
   art. 7º. Ele é o dispositivo constitucional que nomeia agente penitenciário,
   agente socioeducativo e policial, e está transcrito no bundle
   (`cf88/art-40-par-4b/ec-103-2019`), vinculado pelas regras `regra-0080` a
   `regra-0083` e não pelas do art. 7º. A omissão de um dispositivo não é erro
   por si — a fundamentação é articulação autorada —, mas a assimetria entre dois
   blocos de regras da mesma matéria merece decisão registrada.
