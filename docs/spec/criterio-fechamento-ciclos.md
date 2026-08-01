# Critério de fechamento dos ciclos de auditoria

## Objeto da auditoria

O objeto final de um ciclo não é a lista de regras legadas individualmente considerada. É o **conjunto de regras ativas** que, ao término da auditoria, deve representar de forma correta, completa e não ambígua o tema jurídico auditado.

O ciclo não se encerra apenas porque todas as regras importadas receberam uma classificação ou porque os defeitos foram descritos em achados.

## Tratamento das regras erradas

Quando uma regra estiver materialmente errada — isto é, quando representar hipótese jurídica inexistente, misturar hipóteses distintas, usar critérios incompatíveis ou possuir identidade material diferente da que deveria representar — ela deve ser:

1. desativada, preservando-se seu ID e seu histórico;
2. vinculada expressamente à conclusão que justificou a desativação; e
3. substituída por uma ou mais regras novas, com IDs próprios, que representem corretamente as hipóteses juridicamente existentes.

Não se deve reaproveitar o ID da regra errada para uma hipótese juridicamente diferente. Correções meramente formais que não alterem a identidade material da regra podem permanecer no mesmo ID, desde que essa conclusão seja expressamente registrada.

## Prova de cobertura

Todo ciclo deve produzir uma matriz final das combinações juridicamente relevantes do tema. Para aposentadoria por incapacidade ou invalidez, a matriz deve considerar, conforme aplicável:

- regime constitucional e legal;
- janela de ingresso;
- janela de implementação do direito;
- classe juridicamente relevante da causa;
- ramo integral ou proporcional;
- forma de cálculo;
- regime de reajuste e paridade; e
- demais discriminantes que alterem elegibilidade ou resultado.

Para cada combinação juridicamente possível, a matriz deve identificar a regra ativa que a cobre. Combinações juridicamente impossíveis devem ser marcadas como impossíveis, com fundamento.

## Condições cumulativas de encerramento

Um ciclo somente pode ser encerrado quando:

1. nenhuma regra sabidamente errada permanecer ativa;
2. toda regra desativada possuir uma ou mais regras substitutas identificadas, quando a hipótese material continuar existindo;
3. todas as combinações juridicamente relevantes estiverem cobertas por regras ativas;
4. não houver lacunas de cobertura;
5. não houver sobreposições não intencionais entre regras ativas;
6. toda sobreposição intencional estiver expressamente justificada;
7. o mapa `regra desativada → regra(s) substituta(s)` estiver completo;
8. os cenários representativos demonstrarem que o conjunto seleciona a regra ou as regras esperadas; e
9. os artefatos derivados, validadores e demais gates estiverem íntegros.

Uma dependência externa pode permanecer registrada ao fim de uma sessão intermediária. Ela não permite encerrar o ciclo quando impedir afirmar que o tema está completamente coberto.

## Aplicação ao Ciclo 1

No Ciclo 1, a conclusão deve demonstrar que o conjunto ativo cobre integralmente a aposentadoria por incapacidade permanente e as hipóteses históricas de invalidez pertencentes ao escopo, inclusive suas classes de causa, ramos de cálculo, janelas temporais e regimes de reajuste.

O relatório final do próprio `ciclo-01.md` deve conter:

- a situação final de cada regra legada;
- as novas regras criadas;
- o mapa de substituições;
- a matriz de cobertura completa;
- as combinações juridicamente impossíveis e seus fundamentos;
- as sobreposições intencionais, se houver; e
- os riscos residuais que não comprometam a completude da cobertura.
