---
titulo: Relatório de validação das regras de aposentadoria e pensão por morte
subtitulo: Manifestação da Procuradoria-Geral do Estado sobre o catálogo do Sisprev
orgao: Instituto de Previdência dos Servidores Públicos do Estado de Rondônia
# Processo em que esta remessa é juntada. Fica vazio até que ele exista: a
# capa omite a linha, em vez de estampar um número inventado.
processo_sei: ''
---

# Objeto, método e alcance

## O que este documento é

Este relatório é a **manifestação da Procuradoria-Geral do Estado** sobre as
{{regras}} regras de concessão de benefício cadastradas no Sisprev, uma por
capítulo, e se dirige ao Instituto de Previdência dos Servidores Públicos do
Estado de Rondônia, a quem cabe operar o sistema e praticar os atos que dele
decorrem.

Cada capítulo reproduz a regra *como ela está gravada no sistema* — os
parâmetros do cadastro e os três campos de fundamentação —, transcreve por
extenso os dispositivos legais que a própria fundamentação cita, apresenta a
análise e consigna a conclusão da procuradoria sobre aquela regra.

A análise é jurídica e recai sobre o que está gravado. Ela não alcança o
comportamento do programa: o que o Sisprev faz com um parâmetro, quando o lê e
como o compara não é examinável a partir do cadastro, e por isso os pontos que
dependem disso ficam consignados como questões dirigidas ao Instituto, e não
como conclusão.

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
oficial de cada norma; a conclusão sobre a adequação jurídica é a que a
procuradoria consigna no próprio capítulo. Onde a citação é ambígua a ponto de
não se saber qual disposição foi citada, nada é vinculado, e a análise do
capítulo registra por quê.

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
próprio capítulo, e é ela que a procuradoria afirma ser a devida.

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

## Como ler as conclusões

O documento conclui em dois lugares, e a diferença entre eles importa.

**Nas teses**, sobre o defeito. Uma tese é uma constatação da auditoria que
alcança muitas regras de uma vez; ela é escrita uma vez só, nomeia as regras que
atinge, e é ali que a procuradoria se manifesta sobre o defeito em si.

**Nos capítulos**, sobre a regra. Cada capítulo reúne o que aquela linha do
cadastro tem de próprio — os parâmetros gravados, a fundamentação, os
dispositivos citados —, remete às teses que a alcançam e registra a
manifestação da procuradoria sobre ela.

O que cada capítulo traz sob "Limite desta conferência" é **conferência que a
auditoria ainda não fez** naquela regra, transcrita como está escrita. Não são
questões dirigidas ao Instituto e não pedem resposta: estão ali para que o
capítulo não seja lido como conferência concluída. As questões que de fato
dependem do comportamento do sistema — e que só quem opera o Sisprev pode
responder — são dirigidas ao Instituto expressamente, e a procuradoria não as
presume respondidas.

A validação de cada regra não se constitui por este documento. Ela se constitui
pelo ato registrado no processo — parecer, número e autoridade —, que é anotado
na regra no repositório da auditoria; é esse registro que a marca como validada.

## Sobre quantas regras esta remessa conclui

O catálogo tem {{regras}} regras, e este documento traz um capítulo para cada
uma. **Isso não quer dizer que a Procuradoria conclua sobre todas.** A
conferência de mérito está concluída em {{regrasRevisadas}}; em
{{regrasComDisposicao}} há disposição decidida sobre ao menos um achado; e
{{regrasComRessalva}} trazem conferência ainda em curso, declarada ao fim do
capítulo sob "Limite desta conferência".

Uma regra cujo capítulo não registre conclusão **não está sendo aprovada por
este documento**. O capítulo existe para que ela possa ser conferida contra a
lei e contra o sistema, e a manifestação da Procuradoria sobre ela é a que
estiver escrita no campo próprio — não o silêncio.

As {{teses}} teses da seção "Conclusões" são a outra metade do que se submete:
{{tesesAbertas}} delas seguem abertas, {{tesesBloqueantes}} classificadas como
bloqueantes. Uma tese alcança muitas regras de uma vez, e é por isso que ela é
escrita uma vez só, nomeando as que atinge.

## Situação do catálogo nesta remessa

Das {{regras}} regras analisadas, {{regrasComDispositivos}} já têm dispositivos
vinculados e conferidos, somando {{dispositivosCitados}} citações transcritas
ao longo do documento; {{regrasSemDispositivos}} ainda não têm, e nelas a seção
de base normativa registra essa ausência.
