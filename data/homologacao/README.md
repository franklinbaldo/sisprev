# Planilhas de homologação

A planilha corrente das regras propostas é
[`data/regras-propostas.csv`](../regras-propostas.csv), escrita por
`scripts/derivar.py` a cada execução. É ela que a conferência de campo usa, e é
ela que o CI mantém em sincronia com o bundle.

Este diretório é de um layout anterior, em que cada composição exportava a sua
própria planilha e nenhuma delas era regenerada. O que sobrou aqui **não é
derivado vivo**: nada o reescreve, e nenhum gate o confere.

`ciclo-01-s6-fechamento.csv` foi removido: exportava as quarenta unidades do
Bloco C com `TIPO DE BENEFICIO = APOSENTADORIA POR INVALIDEZ` e `DEPLOYABLE = N`
quando as unidades em disco já gravavam a espécie nova e `deployable`. Ficou
divergente por meses parecendo dado bom, e o seu conteúdo corrente é exatamente
`data/regras-propostas.csv`.

`proposta-auditoria-2026-07.csv` fica como **export congelado** da proposta de
julho de 2026, com as unidades de deficiência e agentes nocivos. Não é
autoritativo e não acompanha edição de regra: quem quiser o estado atual roda
`derivar.py`.
