---
type: Especificacao
id: ciclo
nome: Ciclo
---

# Ciclo

> **Minuta.** Escrita a partir do contrato que já vigora no
> `site/src/content.config.ts` e da prática do repositório, para que o tipo
> deixe de existir sem documento. O que ela afirma é descrição do que há, não
> decisão nova — onde estiver errada, quem corrige é a coordenação.

Um **Ciclo** é um lote temático de regras revistas juntas, e o documento é a
fonte única das decisões, dos resultados e da conclusão daquele lote.

## Campos

| campo         | o que é                                                 |
| ------------- | ------------------------------------------------------- |
| `id`          | `ciclo-NN`, e casa com o nome do arquivo                |
| `numero`      | a ordem do ciclo na sequência de revisão                |
| `nome`        | o tema, dito como quem o descreve a quem não o conduziu |
| `data`        | abertura                                                |
| `regras`      | as regras **proprietárias** do ciclo                    |
| `referencias` | regras consultadas, que continuam de outro ciclo        |
| `conjunto`    | a composição em que o ciclo fecha, quando fechado       |

`conjunto` é declarado, nunca deduzido do prefixo do id: um conjunto chamado
`ciclo-01-…` é convenção de quem o nomeou, não vínculo, e navegar por
coincidência de grafia aponta um ciclo para o relatório de outro.

## Proprietária e referência

A distinção decide de quem é o trabalho. Uma regra é **proprietária** de um
ciclo só; ser referência em outro não a transfere, e a análise feita ali é
herança do ciclo dono, não trabalho a refazer.

## Critério de fechamento dos ciclos de auditoria

### Objeto da auditoria

O objeto final de um ciclo não é a lista de regras legadas individualmente
considerada. É o **conjunto de regras ativas** que, ao término da auditoria, deve
representar de forma correta, completa e não ambígua o tema jurídico auditado.

O ciclo não se encerra apenas porque todas as regras importadas receberam uma
classificação ou porque os defeitos foram descritos em achados.

### Tratamento das regras erradas

Quando uma regra estiver materialmente errada — isto é, quando representar
hipótese jurídica inexistente, misturar hipóteses distintas, usar critérios
incompatíveis ou possuir identidade material diferente da que deveria
representar — ela deve ser:

1. desativada, preservando-se seu ID e seu histórico;
2. vinculada expressamente à conclusão que justificou a desativação;
3. substituída por uma ou mais regras novas, com IDs próprios, **quando
   representar de modo defeituoso uma hipótese jurídica que continua
   existindo**; ou
4. registrada no mapa como
   `sem substituta — hipótese juridicamente inexistente`, com o respectivo
   fundamento, quando não houver hipótese material válida a preservar.

Não se deve reaproveitar o ID da regra errada para uma hipótese juridicamente
diferente. Correções meramente formais que não alterem a identidade material da
regra podem permanecer no mesmo ID, desde que essa conclusão seja expressamente
registrada.

### Descoberta de regras ausentes

A auditoria não se limita às hipóteses já representadas no catálogo legado. A
matriz normativa pode revelar uma combinação juridicamente existente para a
qual nunca houve regra cadastrada. Nesse caso, deve ser criada uma regra nova,
com ID próprio, ainda que ela não substitua nenhuma regra anterior.

Toda regra nova deve registrar sua origem material como uma destas categorias:

- **substituição** — corrige hipótese existente representada defeituosamente por
  uma regra desativada; ou
- **lacuna preexistente** — cobre hipótese juridicamente existente que não tinha
  antecedente no catálogo.

Uma regra criada para lacuna preexistente deve apontar para a combinação da
matriz que passou a cobrir, e não para uma regra legada artificialmente escolhida
como antecessora.

### Prova de cobertura

Todo ciclo deve produzir uma matriz final das combinações juridicamente
relevantes do tema. Para aposentadoria por incapacidade ou invalidez, a matriz
deve considerar, conforme aplicável:

- regime constitucional e legal;
- janela de ingresso;
- janela de implementação do direito;
- classe juridicamente relevante da causa;
- ramo integral ou proporcional;
- forma de cálculo;
- regime de reajuste e paridade; e
- demais discriminantes que alterem elegibilidade ou resultado.

Para cada combinação juridicamente possível, a matriz deve identificar a regra
ativa que a cobre. Se nenhuma regra ativa a cobrir, a combinação constitui lacuna
do catálogo e exige a criação de regra nova. Combinações juridicamente impossíveis
devem ser marcadas como impossíveis, com fundamento.

### Gate de pendências de cobertura

Pendências localizadas podem permanecer ao final de sessões intermediárias para
que o restante do bloco prossiga. Antes da sessão de fechamento, porém, deve
haver **zero pendências que afetem a cobertura material do tema**.

A sessão de consistência transversal é responsável por inventariar todas as
pendências deixadas pelos blocos e dar-lhes uma disposição. Cada pendência deve:

1. ser resolvida na própria sessão de consistência, quando a solução for
   transversal; ou
2. retornar obrigatoriamente à sessão proprietária da regra ou do bloco, com a
   reabertura do trabalho necessário.

A sessão de fechamento não pode começar enquanto existir pendência capaz de
impedir a afirmação de cobertura completa, ausência de lacunas ou ausência de
sobreposição injustificada.

### Condições cumulativas de encerramento

Um ciclo somente pode ser encerrado quando:

01. nenhuma regra sabidamente errada permanecer ativa;
02. toda regra desativada possuir uma ou mais regras substitutas identificadas,
    quando a hipótese material continuar existindo, ou o registro expresso
    `sem substituta — hipótese juridicamente inexistente`, com fundamento;
03. todas as combinações juridicamente relevantes estiverem cobertas por regras
    ativas, inclusive as que não possuíam antecedente no catálogo legado;
04. toda lacuna preexistente identificada tiver sido preenchida por regra nova
    com ID próprio;
05. não houver lacunas de cobertura;
06. não houver sobreposições não intencionais entre regras ativas;
07. toda sobreposição intencional estiver expressamente justificada;
08. o mapa
    `regra desativada → regra(s) substituta(s) | sem substituta fundamentada`
    estiver completo;
09. não houver pendência aberta que afete a cobertura material do tema;
10. os cenários representativos demonstrarem que o conjunto seleciona a regra ou
    as regras esperadas; e
11. os artefatos derivados, validadores e demais gates estiverem íntegros.

Uma dependência externa pode permanecer registrada ao fim de uma sessão
intermediária. Ela não permite encerrar o ciclo quando impedir afirmar que o
tema está completamente coberto.

### O ato institucional não é condição de encerramento

As condições acima são de **auditoria**, e um ciclo se encerra quando as cumpre.
A troca efetiva do catálogo vigente — o conjunto passar a `vigente`, com ato de
efeito `valida` — é evento **posterior e único**, praticado pelo IPERON depois
de concluídos os ciclos, e não por ciclo.

A confusão entre as duas coisas tem custo prático: exigir o ato para encerrar
faria todo ciclo ficar aberto esperando um evento que não é dele, e a auditoria
não teria como declarar concluído um tema cujo trabalho terminou. O que o ciclo
entrega é a composição proposta e a prova de que ela cobre o tema; o que o ato
faz é pô-la em vigor.

O que **é** condição de encerramento, e não se confunde com o ato: os grupos de
substituição do ciclo estarem **ativos**, com decisão de completude. Ativar o
grupo é ato da auditoria e afirma que a substituição está decidida; é isso que
o item 1 exige ao falar em regra sabidamente errada que não permanece ativa.

### Aplicação ao Ciclo 1

No Ciclo 1, a conclusão deve demonstrar que o conjunto ativo cobre integralmente
a aposentadoria por incapacidade permanente **sob a norma em vigor para
requerimento novo**, inclusive suas classes de causa, ramos de cálculo, janelas
de ingresso e regimes de reajuste.

As hipóteses históricas de invalidez — as janelas anteriores, em que não se
forma direito novo depois dos seus marcos finais, mas que seguem fundamentando
requerimento novo com base em direito adquirido — foram deslocadas para o
Ciclo 9, "Janelas históricas de invalidez", que é o dono delas. O deslocamento
é de escopo, não de método: os grupos delas permanecem autorados e inativos, e
é o Ciclo 9 que os promove.

O relatório final do próprio `ciclo-01.md` deve conter:

- a situação final de cada regra legada;
- as novas regras criadas, classificadas por origem como `substituição` ou
  `lacuna preexistente`;
- o mapa de substituições e os registros fundamentados de `sem substituta`;
- a matriz de cobertura completa, inclusive as lacunas preexistentes descobertas
  e as regras novas que passaram a cobri-las;
- as combinações juridicamente impossíveis e seus fundamentos;
- as sobreposições intencionais, se houver;
- a demonstração de zero pendências que afetem cobertura; e
- os riscos residuais que não comprometam a completude da cobertura.
