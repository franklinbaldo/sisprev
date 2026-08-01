# Critério de fechamento dos ciclos de auditoria

## Objeto da auditoria

O objeto final de um ciclo não é a lista de regras legadas individualmente
considerada. É o **conjunto de regras ativas** que, ao término da auditoria, deve
representar de forma correta, completa e não ambígua o tema jurídico auditado.

O ciclo não se encerra apenas porque todas as regras importadas receberam uma
classificação ou porque os defeitos foram descritos em achados.

## Tratamento das regras erradas

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

## Prova de cobertura

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
ativa que a cobre. Combinações juridicamente impossíveis devem ser marcadas como
impossíveis, com fundamento.

## Gate de pendências de cobertura

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

## Condições cumulativas de encerramento

Um ciclo somente pode ser encerrado quando:

01. nenhuma regra sabidamente errada permanecer ativa;
02. toda regra desativada possuir uma ou mais regras substitutas identificadas,
    quando a hipótese material continuar existindo, ou o registro expresso
    `sem substituta — hipótese juridicamente inexistente`, com fundamento;
03. todas as combinações juridicamente relevantes estiverem cobertas por regras
    ativas;
04. não houver lacunas de cobertura;
05. não houver sobreposições não intencionais entre regras ativas;
06. toda sobreposição intencional estiver expressamente justificada;
07. o mapa
    `regra desativada → regra(s) substituta(s) | sem substituta fundamentada`
    estiver completo;
08. não houver pendência aberta que afete a cobertura material do tema;
09. os cenários representativos demonstrarem que o conjunto seleciona a regra ou
    as regras esperadas; e
10. os artefatos derivados, validadores e demais gates estiverem íntegros.

Uma dependência externa pode permanecer registrada ao fim de uma sessão
intermediária. Ela não permite encerrar o ciclo quando impedir afirmar que o
tema está completamente coberto.

## Aplicação ao Ciclo 1

No Ciclo 1, a conclusão deve demonstrar que o conjunto ativo cobre integralmente
a aposentadoria por incapacidade permanente e as hipóteses históricas de
invalidez pertencentes ao escopo, inclusive suas classes de causa, ramos de
cálculo, janelas temporais e regimes de reajuste.

O relatório final do próprio `ciclo-01.md` deve conter:

- a situação final de cada regra legada;
- as novas regras criadas;
- o mapa de substituições e os registros fundamentados de `sem substituta`;
- a matriz de cobertura completa;
- as combinações juridicamente impossíveis e seus fundamentos;
- as sobreposições intencionais, se houver;
- a demonstração de zero pendências que afetem cobertura; e
- os riscos residuais que não comprometam a completude da cobertura.
