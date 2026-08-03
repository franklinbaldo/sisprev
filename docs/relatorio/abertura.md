---
titulo: Relatório de validação das regras de aposentadoria e pensão por morte
subtitulo: Catálogo do Sisprev submetido à manifestação da Procuradoria-Geral do Estado
orgao: Instituto de Previdência dos Servidores Públicos do Estado de Rondônia
# Processo em que esta remessa é juntada. Fica vazio até que ele exista: a
# capa omite a linha, em vez de estampar um número inventado.
processo_sei: ''
---

# Objeto, método e como responder

## O que este documento é

Este relatório submete à Procuradoria-Geral do Estado as {{regras}} regras de
concessão de benefício cadastradas no Sisprev, uma por capítulo. Cada capítulo
reproduz a regra *como ela está gravada no sistema* — os parâmetros do cadastro
e os três campos de fundamentação —, transcreve por extenso os dispositivos
legais que a própria fundamentação cita, apresenta a análise da auditoria e
abre espaço para a manifestação.

O documento é gerado automaticamente a partir do repositório da auditoria, no
commit indicado na capa. Ele não é editado à mão: uma correção de regra é feita
no repositório e produz um novo relatório, com novo commit de origem. Dois
relatórios do mesmo catálogo em datas diferentes são, portanto, documentos
distintos, e o commit da capa é o que os distingue.

## O que a auditoria pode e não pode mudar

Uma regra é o conjunto de aferições necessário para conceder o benefício. A
auditoria trabalha dentro dos campos que o Sisprev já tem: os valores dentro
dos domínios existentes e os campos de texto livre (nome e fundamentações).
Criar coluna nova ou estender o domínio de um campo seria alterar o Sisprev, o
que está fora do escopo — quando a análise de um capítulo registra que um
critério não tem onde ser representado, é disso que se trata, e a pendência
fica anotada em vez de ser resolvida por conta própria.

Pelo mesmo motivo, nenhum valor é reinterpretado neste documento. Onde o
cadastro grava `31/12/2099`, o relatório imprime `31/12/2099` — nunca "sem
limite". Sempre que a leitura amigável de um campo difere do que está gravado
(`S` lido como "Sim"), o valor de origem aparece ao lado, em fonte
monoespaçada.

## Vínculo entre regra e dispositivo

A lista de dispositivos de um capítulo afirma que *a fundamentação daquela
regra cita aquelas disposições* — não que a regra esteja juridicamente fundada
nelas. É uma conferência de citação, feita à mão, item a item, contra o texto
oficial de cada norma; a conclusão sobre a adequação jurídica é justamente o
que se pede à PGE. Onde a citação é ambígua a ponto de não se saber qual
disposição foi citada, nada é vinculado, e a análise do capítulo registra por
quê.

## Duas questões gerais, que não são de nenhum capítulo

Há dois pontos que atravessam o catálogo inteiro e por isso não aparecem na
manifestação de nenhuma regra. O primeiro é **como o sistema compara as datas
de fronteira das janelas**.

O cadastro delimita cada janela por um par de datas. A auditoria conferiu como
elas foram preenchidas e encontrou uma convenção seguida sem exceção
relevante: o limite inferior do direito grava **o primeiro dia** de vigência da
norma, e o limite superior grava **o primeiro dia da norma seguinte** — de modo
que uma janela vai do início de uma redação até a véspera da próxima, e janelas
sucessivas se encaixam sem deixar dia descoberto nem dia coberto duas vezes.
Esse é o critério adotado uniformemente neste relatório, e é o que sustenta a
leitura das janelas em todos os capítulos.

O que a auditoria **não** tem como verificar é se o sistema aplica esse mesmo
critério ao selecionar a regra. Se ele tratar a data superior como um dia ainda
coberto, cada janela concede um dia a mais do que a norma autoriza — um efeito
uniforme, de um dia, na fronteira entre dois regimes.

Não se afirma que isso ocorra: a auditoria examina o cadastro, e o
comportamento do programa está fora do que ela alcança. O ponto é registrado
aqui, uma vez, porque seria artificial repeti-lo em cada capítulo, e porque a
resposta não muda nenhuma regra individualmente — muda, se for o caso, a
convenção inteira de uma vez.

O segundo ponto é **o que o campo de tipo de cálculo do cadastro implanta**.

Cada capítulo descreve a fórmula de cálculo do benefício por extenso: sobre que
valor o cálculo começa, que ajustes incidem e em que ordem, e que limites se
aplicam. Essa descrição é jurídica, extraída dos dispositivos transcritos no
próprio capítulo, e é ela que a auditoria submete à manifestação.

O cadastro, porém, não guarda a fórmula. Guarda um rótulo — `Valor Efetivo`,
`Proporcionalidade Dias` e outros —, e um mesmo rótulo não diz sobre que valor
o cálculo incide, nem a que redação da norma se refere, nem se há fração a
aplicar. **Adota-se, para efeito deste relatório, a premissa de que o rótulo
gravado em cada regra é aquele pelo qual o sistema implanta a fórmula descrita
no capítulo correspondente.**

É premissa declarada, não constatação. A auditoria examina o cadastro e os
textos normativos; o que o programa faz com o rótulo está fora do que ela
alcança, e não há no material disponível elemento que permita confirmar a
correspondência de modo assertivo. É por isso que cada forma de cálculo registra
o grau de fidelidade da sua projeção, em vez de afirmar equivalência.

Confirmada a premissa, nada muda. Infirmada, o que se corrige é a
parametrização do sistema, e não a fundamentação: o que os capítulos afirmam é
a fórmula que a norma impõe, não o comportamento do rótulo. Vale aqui a mesma
razão do ponto anterior — a resposta não altera nenhuma regra em particular, e
sim a convenção inteira de uma vez.

## Como responder

Cada capítulo termina com uma seção de manifestação. Os pontos numerados nela
são as questões que a auditoria deixou expressamente em aberto naquela regra —
transcritas, não reformuladas. Há ainda um campo de manifestação geral, para o
que não couber nos pontos listados, e um capítulo pode não ter ponto algum, o
que significa que a auditoria não deixou questão pendente nele.

Registrada a manifestação, o ato correspondente (número do processo, parecer e
autoridade) é anotado na regra no repositório da auditoria, e é esse registro —
não este documento — que marca a regra como validada pela PGE.

## Situação do catálogo nesta remessa

Das {{regras}} regras submetidas, {{regrasComDispositivos}} já têm dispositivos
vinculados e conferidos, somando {{dispositivosCitados}} citações transcritas
ao longo do documento; {{regrasSemDispositivos}} ainda não têm, e nelas a seção
de base normativa registra essa ausência. {{regrasComPendencia}} regras têm ao
menos um ponto submetido a manifestação, {{pendencias}} no total, e
{{regrasComAchado}} são alcançadas por algum achado de auditoria.
