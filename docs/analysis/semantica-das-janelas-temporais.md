# Semântica das janelas temporais — decisões consolidadas

> **Atualização de 2026-08-01:** este documento substitui as leituras anteriores
> que tratavam `DATA_ADM_APOS` como exclusivo ou `DATA_DIREITO_APOS` como
> pergunta ainda aberta. A decisão normativa vigente está em
> [`docs/spec/decisoes-semanticas-regra.md`](../spec/decisoes-semanticas-regra.md).

## 1. Estado da questão

A semântica das fronteiras inferiores discutidas pela auditoria está
**confirmada pela coordenação** e não é mais premissa, hipótese ou dependência
externa:

| campo                | referência fática                                      | fronteira |
| -------------------- | ------------------------------------------------------ | --------- |
| `DATA_ADM_APOS`      | ingresso no serviço público; para cargo efetivo, posse | inclusiva |
| `DATA_DIREITO_APOS`  | implementação de todos os requisitos do direito        | inclusiva |

O próprio dia gravado entra nos dois casos.

A resposta anterior para `DATA_ADM_APOS` — valor como último dia do regime
anterior e cobertura somente no dia seguinte — está superada. Não deve ser
reaplicada por agentes futuros nem usada para abrir achado de erro de um dia.

## 2. `DATA_ADM_APOS`

`DATA_ADM_APOS = X` significa que a regra alcança quem ingressou no serviço
público **em X ou depois de X**.

Para ingresso em cargo efetivo, o fato jurídico relevante é a investidura,
concretizada pela posse. Nomeação e exercício são atos distintos e não
substituem esse marco.

Exemplo:

```text
DATA_ADM_APOS = 01/01/2004

31/12/2003  fora da fronteira inferior
01/01/2004  dentro da fronteira inferior
02/01/2004  dentro da fronteira inferior
```

A data gravada deve ser o primeiro dia coberto pela regra. Não se grava o dia
anterior para simular um operador exclusivo.

## 3. `DATA_DIREITO_APOS`

`DATA_DIREITO_APOS = X` significa que a regra alcança quem implementou **todos
os requisitos** do direito **em X ou depois de X**.

O campo é usado sobretudo para regras cuja disciplina passa a produzir efeitos
a partir de certo marco normativo. Em regra, o valor deve coincidir com o
primeiro dia de vigência ou de produção de efeitos da hipótese jurídica.

O campo não representa:

- data do requerimento;
- data do protocolo;
- data da concessão;
- data de publicação do ato de aposentadoria; ou
- data em que o processo administrativo terminou.

Exemplo:

```text
DATA_DIREITO_APOS = 18/10/2021

17/10/2021  fora da fronteira inferior
18/10/2021  dentro da fronteira inferior
19/10/2021  dentro da fronteira inferior
```

Quem implementou os requisitos antes continua sujeito ao regime anterior ou à
regra de direito adquirido cabível. O fato de requerer ou ter a concessão depois
não desloca a data de implementação dos requisitos.

## 4. O que a decisão resolve — e o que não resolve

Ela resolve o significado das colunas e a inclusividade da fronteira inferior.
Logo, não permanecem perguntas como:

- “`DATA_DIREITO_APOS` é inclusivo ou exclusivo?”;
- “o valor é data de requerimento ou de concessão?”;
- “`DATA_ADM_APOS` grava o último dia do regime anterior?”; ou
- “a auditoria precisa testar o Sisprev antes de começar a trabalhar?”.

Ela não confirma automaticamente que cada valor cadastrado está correto. Para
cada regra ainda é necessário identificar:

1. a norma e o dispositivo que instituem o marco;
2. a data exata de início de vigência ou de produção de efeitos;
3. se há regra de transição ou direito adquirido que altere o recorte; e
4. se o valor gravado é realmente o primeiro dia coberto.

Essa distinção é central:

> **semântica da coluna fechada não significa valor concreto validado.**

## 5. Releitura da varredura do catálogo

A varredura anterior encontrou os seguintes valores não coincidentes com os
marcos então autorados no bundle:

| valor        | ocorrências | onde                                                    |
| ------------ | ----------- | ------------------------------------------------------- |
| `31/12/2024` | 34          | `data_adm_ate` de 6 regras; `data_direito_ate` de 28    |
| `15/12/1998` | 6           | `data_adm_ate` e `data_direito_ate` de 0001, 0002, 0003 |
| `01/01/2004` | 6           | `data_adm_apos` de 0014, 0015, 0021, 0022, 0057, 0058   |
| `01/01/2024` | 5           | `data_direito_apos` de 0014–0018                        |
| `23/10/2021` | 4           | `data_direito_apos` de 0019–0022                        |
| `04/12/2015` | 2           | `data_direito_apos` de 0030, 0031                       |
| `14/06/2021` | 2           | `data_adm_ate` de 0049, 0050                            |
| `09/09/2021` | 2           | `data_adm_ate` de 0057, 0058                            |
| `01/01/1969` | 1           | `data_direito_apos` de 0003                             |
| `01/12/2002` | 1           | `data_direito_ate` de 0087                              |
| `03/12/2015` | 1           | `data_direito_ate` de 0027                              |

A tabela continua útil como **fila de conferência de lastro**, mas a conclusão
anterior sobre `01/01/2004` precisa ser retirada. Sob a semântica agora
confirmada, `DATA_ADM_APOS = 01/01/2004` cobre corretamente o próprio dia
01/01/2004. Não há erro de um dia apenas por esse motivo.

Da mesma forma, a igualdade entre `DATA_DIREITO_APOS` e o início de vigência da
norma é o comportamento esperado: o próprio dia entra.

Os demais valores continuam exigindo pesquisa de mérito. Não coincidir com uma
data já autorada pode significar:

- prazo interno do dispositivo;
- produção de efeitos diferida;
- norma ainda não vinculada;
- erro de digitação; ou
- valor sem lastro.

## 6. Fila de conferência jurídica

As perguntas legítimas agora são concretas:

- qual dispositivo sustenta `23/10/2021` nas regras 0019–0022, se a LCE
  1.100/2021 começou a vigorar em 18/10/2021?;
- qual norma sustenta `01/01/2024` nas regras 0014–0018?;
- o que institui o prazo `31/12/2024`?;
- `15/12/1998`, `14/06/2021` e `09/09/2021` são erros de digitação ou marcos
  próprios?;
- `01/01/1969` é sentinela não catalogada ou data real?; e
- qual fonte explica `01/12/2002` na `regra-0087`?

Essas perguntas não reabrem a semântica de `APOS`. Elas pedem o fundamento de
um valor específico.

## 7. Regra para ciclos de auditoria

Nenhum ciclo deve esperar nova confirmação genérica do Sisprev para aplicar as
duas definições acima. A execução começa com a semântica consolidada e suspende
somente a alteração concreta que dependa de fonte ainda ausente.

Uma revisão futura é possível, mas deve ser expressa, fundamentada e identificar
quais conclusões anteriores seriam afetadas. Até isso ocorrer, tratar
`DATA_ADM_APOS` ou `DATA_DIREITO_APOS` como questão aberta é erro documental.