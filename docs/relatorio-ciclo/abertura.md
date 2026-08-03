---
titulo: Relatório de fechamento de ciclo de auditoria
subtitulo: Proposta de substituição do catálogo submetida à manifestação da Procuradoria-Geral do Estado
orgao: Instituto de Previdência dos Servidores Públicos do Estado de Rondônia
# Processo em que esta remessa é juntada. Fica vazio até que ele exista: a
# capa omite a linha, em vez de estampar um número inventado.
processo_sei: ''
---

# Objeto, método e como responder

## O que este documento é

Este relatório submete à Procuradoria-Geral do Estado a **proposta de
substituição** produzida por um ciclo de auditoria: quais regras hoje
cadastradas no Sisprev a auditoria concluiu que devem ser desativadas, por
quais regras propostas cada uma seria substituída, e com que fundamento.

Ele é diferente do relatório de validação do catálogo. Aquele apresenta as
regras **como estão gravadas**, uma por capítulo, e pede manifestação sobre
cada uma. Este apresenta o que a auditoria **propõe pôr no lugar** de algumas
delas, agrupado pela decisão que as reuniu.

O documento é gerado a partir do repositório da auditoria, no commit indicado
na capa, e não é editado à mão: uma correção é feita no repositório e produz
um novo relatório, com novo commit de origem.

## O que é uma regra proposta

Uma **regra proposta** é a regra corrigida — a versão que a auditoria propõe
pôr no lugar de uma regra hoje cadastrada. Ela não é uma parte de uma regra
nem um rascunho dela: é uma regra inteira, com nome, parâmetros e
fundamentação próprios, pronta para ocupar uma linha do Sisprev.

Ela existe como documento separado por uma razão específica. O catálogo
recebido é preservado exatamente como veio, sem perder, renumerar ou fundir
linha alguma — é a memória do que o sistema tinha. Mas corrigir muitas vezes
**muda o número de regras**: uma regra que empacota duas hipóteses distintas
precisa de duas regras para ser representada corretamente, e duas regras
idênticas precisam de uma só. As regras propostas vivem, por isso, num
espaço próprio, cada uma declarando de que regras cadastradas descende.

## O que é um grupo de substituição

O que se aprova neste documento não é a regra isolada: é o **grupo**. Um grupo
reúne as regras cadastradas que saem e as regras propostas que entram, e
ativa ou reverte inteiro. Ele existe porque a correspondência raramente é de
um para um.

Por isso cada capítulo apresenta um grupo completo, com as origens e os
destinos lado a lado, e a manifestação é colhida sobre o grupo. Aprovar
metade de um grupo deixaria hipótese sem representação ou hipótese
representada duas vezes.

## O que a auditoria pode e não pode mudar

A auditoria trabalha dentro dos campos que o Sisprev já tem. Estender o
domínio de um campo ou criar coluna seria alterar o sistema, o que está fora
do escopo. Uma regra proposta pode registrar mais do que o Sisprev
comporta — e frequentemente registra —, mas o que sai para o sistema tem de
caber nas colunas existentes.

É isso que a planilha anexa mostra: cada regra proposta **projetada nas
colunas do Sisprev**, do jeito que entraria. Onde a projeção perde alguma
coisa que a regra proposta registra, a perda está declarada nela.

## Por que nenhuma linha está marcada como pronta

A planilha anexa traz, em coluna própria, `DEPLOYABLE = N` para todas as
linhas. Isso não indica defeito: indica que as regras propostas ainda não
foram promovidas, e a promoção é ato humano que depende justamente desta
manifestação. O documento existe para ser lido **antes** da decisão que
libera as linhas; se ele já as desse por prontas, estaria afirmando aprovado
aquilo cuja aprovação está pedindo.

## Como responder

Cada capítulo termina com campos de manifestação sobre o respectivo grupo. Os
pontos numerados, quando existem, são as conferências que a auditoria deixou
expressamente em aberto no documento da regra proposta ou do conjunto —
transcritas como estão escritas, sem juízo do gerador sobre serem as certas.

A manifestação pode ser favorável ao grupo, contrária, ou favorável com
ressalva que identifique a regra proposta e o campo a corrigir. Ressalva que
identifique o defeito é o retorno mais útil: ela volta ao repositório como
correção da regra proposta, e a remessa seguinte já a traz incorporada.
