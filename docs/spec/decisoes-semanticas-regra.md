# Decisões semânticas consolidadas dos campos de regra

- **Status:** decisão vigente da coordenação da auditoria
- **Decidido em:** 2026-08-01
- **Escopo:** `type: Regra`, catálogo legado do Sisprev e modelo auditado
- **Relação com a spec:** este documento complementa
  [`docs/spec/regra.md`](regra.md) e prevalece sobre leituras anteriores que
  tratem os pontos abaixo como perguntas abertas, hipóteses ou premissas ainda
  dependentes de confirmação.

## Efeito desta decisão

As questões abaixo **não são mais dúvidas semânticas da auditoria**. Não podem
ser usadas como gate geral para impedir o início ou a continuidade de um ciclo
de validação. A auditoria deve aplicar estas definições e investigar apenas o
mérito concreto de cada regra: dispositivo aplicável, valor correto, fórmula
correta, vigência e eventual necessidade de decomposição.

Documentos históricos podem registrar hipóteses anteriores. Quando houver
conflito, esta decisão e a atualização mais recente da spec prevalecem. O
histórico continua útil para explicar como se chegou à decisão, mas não reabre a
questão.

## 1. Ramos integral e proporcional

O Sisprev permite dois modos de parametrização:

1. uma mesma regra pode carregar fundamentação para o ramo integral e para o
   ramo proporcional, cabendo à configuração escolher o texto correspondente ao
   resultado; ou
2. integral e proporcional podem ser cadastrados como regras separadas, cada
   qual com a sua própria fundamentação.

Essa flexibilidade descreve a capacidade do sistema legado; ela não obriga o
catálogo auditado a preservar as duas formas.

### Decisão de modelagem

O modelo auditado adota deliberadamente:

> **uma regra representa um único ramo de resultado: integral ou proporcional.**

A separação ocorre antes da regra. Quando uma linha legada empacota os dois
ramos, ela deve ser decomposta no catálogo auditado. Cada unidade resultante
carrega somente a fundamentação do próprio ramo.

A escolha é opinionada porque torna explícito o que o modelo legado pode deixar
implícito: qual resultado a regra produz, qual fundamento autoriza esse resultado
e qual forma de cálculo lhe corresponde. Isso simplifica seleção, revisão,
explicação e validação individual.

Integral e proporcional sempre produzem resultados diferentes. Mesmo quando a
base normativa é muito próxima, o fundamento do ramo proporcional contém ao
menos o elemento que autoriza a proporcionalização. Portanto, não existe ramo
proporcional juridicamente idêntico ao integral.

Consequências:

- `FUNDAMENTACAO_INTEGRAL` e `FUNDAMENTACAO_PROPORCIONAL` são capacidades do
  legado, não autorização para manter ambiguidade no modelo auditado;
- uma regra com `integral: N` não deve permanecer apoiada apenas em texto do
  ramo integral;
- a presença dos dois textos numa linha é sinal para avaliar decomposição, não
  motivo para suspender a auditoria;
- a decomposição preserva a proveniência da linha legada e cria identidades
  próprias para as unidades auditadas, conforme as RFCs de decomposição e
  compilação.

## 2. Campo `INTEGRAL`

`INTEGRAL = S` significa exclusivamente:

> **o provento não é proporcionalizado pelo tempo de contribuição.**

O campo não significa, por si só:

- cálculo pela última remuneração;
- integralidade constitucional;
- paridade;
- ausência de média contributiva; ou
- igualdade entre provento e remuneração do cargo efetivo.

`INTEGRAL = N` indica que o ramo admite ou determina proporcionalização pelo
tempo de contribuição. A base, os componentes e os limitadores do cálculo são
outra dimensão.

## 3. Campo `TIPO_CALCULO`

Os rótulos legados de `TIPO_CALCULO` são **referências para formas de cálculo**.
Eles não são, isoladamente, a descrição normativa completa da fórmula.

A fonte semântica do cálculo no modelo novo é o conceito `FormaCalculo`, no
bundle OKF correspondente. A regra referencia uma forma de cálculo; a forma de
cálculo descreve fórmula, componentes, ordem de aplicação, ajustes, limitadores
e projeção para o Sisprev.

A parametrização não fica limitada aos nomes atualmente existentes:

- quando as fórmulas atuais já abrangem o caso, reutiliza-se a forma adequada;
- quando for necessária uma forma que ainda não existe, cria-se uma nova;
- quando um nome legado for ambíguo, ele pode ser substituído por nome mais
  preciso e o Sisprev pode ser configurado para referenciar o novo cálculo.

O sistema permite parametrizar novos cálculos. Portanto, ambiguidade de rótulo
não deve ser preservada como restrição do modelo nem convertida em inferência
sobre a fórmula.

## 4. Campo `DATA_DIREITO_APOS`

`DATA_DIREITO_APOS` indica a data a partir da qual a regra pode ser aplicada a
quem implementa **todos os requisitos** do direito.

A fronteira é **inclusiva**: o próprio dia gravado entra.

O campo é usado sobretudo para separar regras que começaram a vigorar em certo
marco. Em regra, o valor acompanha o início de vigência ou de produção de efeitos
da disciplina que institui aquele direito.

Ele não representa:

- data do requerimento;
- data do protocolo;
- data da concessão; ou
- data do ato de aposentadoria.

Exemplo: se `DATA_DIREITO_APOS = 18/10/2021`, quem completa todos os requisitos
em 18/10/2021 já está dentro da fronteira inferior dessa regra.

A semântica da coluna está fechada. Continua sendo questão de mérito, regra por
regra, verificar se a data gravada tem lastro na norma aplicável.

## 5. Campo `DATA_ADM_APOS`

`DATA_ADM_APOS` representa a fronteira inferior da data de ingresso no serviço
público. Para ingresso em cargo efetivo, o marco jurídico adotado é a
investidura, concretizada pela posse.

A fronteira é **inclusiva**: o próprio dia gravado entra.

Exemplo: se `DATA_ADM_APOS = 01/01/2004`, a pessoa admitida em 01/01/2004 já
satisfaz a fronteira inferior.

Esta decisão supera a leitura anterior que tratava `DATA_ADM_APOS` como campo
exclusivo e interpretava o valor como o último dia do regime anterior. Onde essa
leitura aparecer em relatórios, achados, RFCs ou notas históricas, deve ser lida
como superada.

## 6. O que permanece para a auditoria

Fechar a semântica dos campos não valida automaticamente os valores existentes.
A auditoria ainda deve, em cada regra:

- identificar a norma e o dispositivo que instituem o marco temporal;
- verificar se o valor cadastrado corresponde ao primeiro dia coberto;
- identificar o ramo integral ou proporcional aplicável;
- conferir se a fundamentação contém o elemento jurídico próprio daquele ramo;
- vincular a regra à `FormaCalculo` correta;
- criar ou renomear a forma de cálculo quando o conceito existente for
  insuficiente ou ambíguo; e
- registrar eventual dependência externa apenas quando ela impedir uma decisão
  concreta, nunca como dúvida genérica sobre o significado da coluna.

## 7. Regra de processo

> **Dúvida semântica resolvida não volta a ser gate.**

Uma sessão futura pode demonstrar erro nesta decisão e propor sua revisão, mas
precisa fazê-lo expressamente, com evidência e impacto identificado. Até lá, os
agentes e auditores devem aplicar estas definições como estado vigente do
projeto.