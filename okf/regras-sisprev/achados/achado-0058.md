---
type: Achado
id: achado-0058
nome: Três regras citam o § 3º do art. 7º da ECE 146/2021, que manda pagar a totalidade da remuneração com paridade, e gravam paridade N com Valor Médio
situacao: aberto
severidade: bloqueante
verificacao: manual
natureza: juridica
regras_afetadas:
  - /regras/regra-0084.md
  - /regras/regra-0109.md
  - /regras/regra-0110.md
detectado_em: 2026-07-30
detectado_por: franklinbaldo
---

# Descrição

O § 3º do art. 7º da ECE 146/2021 determina, em uma frase, base de cálculo **e**
reajuste:

> § 3º Os proventos das aposentadorias concedidas nos termos do disposto neste
> artigo, para aquele que tenha ingressado na respectiva carreira até a data de
> entrada em vigor da Emenda Constitucional nº 103, de 2019, **e que não tenha
> feito a opção de que trata o § 16 do art. 40 da Constituição Federal**,
> corresponderão à **totalidade da remuneração do servidor público no cargo
> efetivo** em que se der a aposentadoria [...] e serão **reajustados na mesma
> proporção e na mesma data, sempre que se modificar a remuneração dos servidores
> em atividade**, sendo também estendidos aos aposentados quaisquer benefícios ou
> vantagens posteriormente concedidos aos servidores em atividade [...]

O *caput* diz a mesma coisa por atacado: aposentar-se na forma da LC 51/1985
"**com paridade e integralidade**".

"Totalidade da remuneração no cargo efetivo" é integralidade; reajuste na mesma
proporção e na mesma data dos servidores em atividade é a definição de paridade.
Treze regras vinculam este parágrafo. **Três gravam `paridade: N` e
`tipo_calculo: Valor Médio`** — nenhuma das duas coisas que o dispositivo
determina.

# Evidências

Todas as regras cujo `dispositivos:` contém `ece-146-2021/art-7-par-3`:

| regra                       | `paridade` | `integral` | `tipo_calculo`              |
| --------------------------- | ---------- | ---------- | --------------------------- |
| `regra-0072` a `regra-0079` | `S`        | `S`        | Remuneração de Contribuição |
| `regra-0111`, `regra-0112`  | `S`        | `S`        | Remuneração de Contribuição |
| **`regra-0084`**            | **`N`**    | `S`        | **Valor Médio**             |
| **`regra-0109`**            | **`N`**    | **`N`**    | **Valor Médio**             |
| **`regra-0110`**            | **`N`**    | **`N`**    | **Valor Médio**             |

**Dez regras contra três, e a maioria não é o argumento — o dispositivo é.** A
uniformidade das dez importa por outra razão: ela mostra que o catálogo **sabe**
parametrizar este parágrafo, e que os valores das três não são consequência de
uma convenção geral do cadastro. O par `paridade: S` + `Remuneração de Contribuição` é o que este vínculo produz em toda parte, menos aqui.

**Na `regra-0084` a contradição é também interna.** Ela grava `integral: S` e
`Valor Médio` no mesmo documento. As duas afirmações não convivem: se a base é a
média das maiores remunerações de 80% do período contributivo, não é a totalidade
da remuneração do cargo efetivo, e `integral: S` deixa de descrever o que a regra
faz. Nenhuma leitura do § 3º produz essa combinação — nem a leitura que este
achado registra como hipótese absolutória na seção seguinte.

`regra-0109` e `regra-0110` são internamente coerentes: `paridade: N`,
`integral: N` e média descrevem um regime único, o do cálculo comum. O defeito
delas é de **vínculo**: elas citam o parágrafo que institui o outro regime.

# Hipótese que absolveria parte disto, e o que ela não alcança

O § 3º é **condicional em dois eixos**: alcança quem ingressou na carreira até
13/11/2019 **e** não fez a opção do § 16 do art. 40 da CF — a adesão ao regime de
previdência complementar. Quem fez a opção fica fora do parágrafo, e o cálculo do
seu benefício não é o dele.

Se `regra-0109` e `regra-0110` forem as regras do servidor **optante**, os
valores gravados descrevem corretamente o cálculo, e o que sobra é uma citação
que invoca o parágrafo pela sua **exclusão** em vez de pela sua incidência. Isso
seria defeito de outra ordem — de fundamentação, não de parametrização —, e
provavelmente menor.

**A hipótese é registrável e não foi verificada**, e há duas coisas contra
tomá-la por resolvida:

- **o catálogo não tem onde registrar a opção do § 16.** Não há coluna de adesão
  à previdência complementar, e sem ela o par `regra-0109`/`regra-0110` não se
  distingue do par `regra-0111`/`regra-0112` por nenhum critério aferido — o que
  é exatamente a forma de lacuna que o `CLAUDE.md` descreve, e que deveria
  aparecer como grupo `P2_IGUALDADE_MATERIAL_ATIVA` se as demais colunas
  coincidissem;
- **ela não alcança a `regra-0084`.** Lá o problema não é a combinação escolhida
  e sim a incompatibilidade entre `integral: S` e `Valor Médio` dentro do mesmo
  documento, que nenhuma das duas hipóteses de regime sustenta.

# Consequência prática

**A divergência é de valor concedido.** `paridade` e `tipo_calculo` orientam o
cálculo e o reajuste; a fundamentação, que o motor não lê, não os corrige.
Totalidade da remuneração com reajuste vinculado ao servidor ativo e média de 80%
do período contributivo com reajuste do RGPS produzem valores diferentes na
concessão e divergentes de forma crescente ao longo do benefício.

A direção do desvio: sob o dispositivo citado, os valores gravados tendem a
conceder **menos** do que ele determina — e a paridade é a parcela que mais pesa
no longo prazo, porque não se recupera com reajuste posterior.

`regra-0109` e `regra-0110` são `simulavel: S`, então o desvio é aferido pelo
motor. `regra-0084` é `simulavel: N`, e ali a contradição interna atinge quem faz
a triagem.

**Severidade `bloqueante`**, pelo critério de
[`okf/spec/regra.md`](../../../okf/spec/regra.md): campos deployáveis que
contradizem o dispositivo que a própria regra vincula, alcançando o valor do
benefício.

# O que este achado não afirma

**Não afirma qual lado corrigir.** Nas três regras, ou os campos de cálculo estão
errados, ou o vínculo com o § 3º está errado. São correções opostas e a escolha
depende de fato que o catálogo não registra — no caso das duas primeiras, a opção
do § 16.

**Não afirma que `Remuneração de Contribuição` seja o rótulo juridicamente exato**
da totalidade da remuneração. O enum legado não identifica fórmulas (P16), e o que
se usa aqui é a comparação com as dez regras do mesmo vínculo, não uma leitura do
rótulo.

**Não afirma que alguma concessão tenha saído a menor.** Depende de caso concreto,
que o catálogo não registra.

# Por que não é duplicata

O [`achado-0055`](achado-0055.md) alcança a `regra-0084` pelo valor sentinela em
`data_adm_ate`; o [`achado-0017`](achado-0017.md), pela alínea da LC 51/1985. Os
três defeitos são independentes e nenhum implica o outro — este é sobre os campos
de cálculo.

O [`achado-0039`](achado-0039.md) registra que as janelas de `regra-0111` e
`regra-0112` são as do art. 4º enquanto a fundamentação é a do art. 7º. Aquelas
duas gravam `paridade: S` e não estão aqui; a forma do defeito é outra —
divergência entre janela e fundamento, não entre cálculo e fundamento.

O [`achado-0057`](achado-0057.md) tem a **mesma forma** noutra família:
`tipo_calculo: Valor Médio` sob dispositivo de totalidade. A diferença que
justifica achado próprio é probatória. Lá, `integral` e `paridade` concordam com o
texto e só o `tipo_calculo` destoa, e existe irmã idêntica que grava o valor certo
— o defeito isola num campo e a correção é determinada. Aqui, dois campos destoam,
uma das regras é internamente incoerente, e existe hipótese absolutória — a opção
do § 16 — que não tem paralelo lá. Juntar os casos obrigaria a abandonar a
conclusão forte do `0057`.

# Questão a investigar

1. **Se `regra-0109` e `regra-0110` são as regras do servidor optante do § 16 do
   art. 40 da CF.** É a pergunta que decide se o defeito delas é de parametrização
   ou de citação. Pergunta ao IPERON como titular do produto; o catálogo não a
   responde, porque não tem coluna de adesão à previdência complementar.

2. **Como a `regra-0084` chega a `integral: S` com `Valor Médio`.** A combinação
   não corresponde a nenhum dos dois regimes do art. 7º, e é anterior a qualquer
   correção: sem saber o que ela pretendia afirmar, corrigir um dos dois campos é
   escolher por conveniência.

3. **Se falta ao catálogo a coluna que registra a opção do § 16.** Se a resposta
   à questão 1 for afirmativa, o critério que separa `regra-0109`/`regra-0110` de
   `regra-0111`/`regra-0112` não é aferível por campo nenhum — lacuna de schema,
   que a RFC 0004 representa pelo catálogo auditado e que está **fora** do que a
   parametrização do Sisprev alcança.

4. **Se `regra-0072`–`regra-0079` gravam o par certo pelo motivo certo.** Elas
   gravam `paridade: S` e `Remuneração de Contribuição`, que é o que o § 3º manda
   — mas nenhuma delas registra a condição do § 16, que também as alcança. Se
   existir optante na população delas, o defeito é o inverso deste, e não foi
   conferido aqui.
