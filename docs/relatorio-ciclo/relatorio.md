---
titulo: Relatório jurídico conclusivo do Ciclo 1
subtitulo: >-
  Auditoria das regras de aposentadoria por incapacidade permanente no Sisprev —
  conclusões da Procuradoria-Geral do Estado e providências para homologação
  pelo IPERON
orgao: Instituto de Previdência dos Servidores Públicos do Estado de Rondônia
# Origem e referência administrativa. Cada campo vazio é impresso como
# pendência documental na seção própria, com o nome de quem deve informá-lo:
# um documento que circula assinado não pode omitir em silêncio o processo a
# que pertence, nem estampar número que ninguém forneceu.
processo_sei: ''
expediente_de_origem: ''
unidade_solicitante: ''
unidade_coordenadora: ''
destinatarios: ''
---

<!-- Um arquivo só, cinco partes. Os delimitadores são comentários HTML porque
não renderizam e não dependem de título editorial: renomear uma seção do
documento não pode quebrar o gerador. `partesDoRelatorio` estoura se algum
deles faltar, em vez de emitir documento truncado. -->

<!-- encaminhamento -->

# Encaminhamento institucional

Este relatório consolida a manifestação jurídica da Procuradoria-Geral do
Estado sobre a revisão das regras de aposentadoria por incapacidade permanente
cadastradas no Sisprev, e indica as providências que a sua execução exige.

## Conclusão da Procuradoria-Geral do Estado

**Não se identifica óbice jurídico à substituição proposta**, nos limites e
observadas as ressalvas indicadas neste relatório. A auditoria jurídica do
Ciclo 1 está concluída.

## Providência esperada da coordenação

1. tomar ciência da conclusão jurídica e das ressalvas registradas;
2. encaminhar este relatório e o arquivo de carga que o acompanha à unidade
   competente do IPERON;
3. acompanhar a execução e a documentação das medidas descritas adiante;
4. submeter à autoridade administrativa competente a decisão sobre a
   implantação, depois de concluída a homologação;
5. consolidar o encerramento administrativo do ciclo.

## Providência esperada do IPERON

1. inserir no ambiente de homologação as regras propostas relacionadas no
   Anexo I;
2. executar os cenários de homologação, inclusive os que respondem às
   ressalvas registradas;
3. instituir os controles administrativos necessários, onde a seleção
   automática não bastar;
4. documentar entradas, resultados obtidos, resultados esperados e eventuais
   divergências;
5. corrigir os comportamentos divergentes antes de qualquer ativação em
   produção.

## Limite deste relatório

**Este relatório não autoriza, por si, a ativação em produção.** A conclusão
jurídica afirma que a substituição pode ser feita; a homologação é que
confirma que o sistema a executa como descrito. Enquanto o ato de implantação
não for praticado e registrado, o catálogo hoje cadastrado permanece o único em
vigor.

<!-- abertura -->

# Objeto, origem e alcance da auditoria

## Objeto

Este relatório apresenta o resultado do primeiro ciclo de auditoria jurídica
realizado pela Procuradoria-Geral do Estado sobre as regras de aposentadoria
por invalidez e incapacidade permanente cadastradas no Sisprev.

A auditoria verificou se as regras registradas representam, de forma
juridicamente correta e operacionalmente aplicável, os regimes constitucionais
e legais incidentes, especialmente quanto à causa da incapacidade, à forma de
cálculo dos proventos, à proporcionalidade e ao regime de reajuste.

## Alcance temporal

O escopo deste ciclo é a **disciplina permanente vigente na data-base de
{{dataBase}}**: a norma sob a qual se rege a aposentadoria por incapacidade
cujo direito se forma nessa data.

As janelas normativas anteriores não admitem formação de direito novo depois
dos seus marcos finais, mas continuam podendo fundamentar requerimento
apresentado hoje, por quem tenha adquirido o direito na vigência delas. Por
essa razão — e não por desuso — a revisão dessas janelas é objeto de ciclo
próprio, ao fim da sequência de revisão. O que aqui se conclui não alcança nem
antecipa nada sobre elas.

## Conceitos utilizados

**Componente de substituição.** Conjunto formado pela regra cadastrada que será
desativada e pelas regras propostas que a substituirão. O componente é
analisado, encaminhado e implantado como unidade: alcançar parte dele deixaria
hipótese sem representação ou representada duas vezes. A Procuradoria conclui
juridicamente sobre o componente, a homologação o testa e a autoridade
administrativa decide sobre a sua implantação — três atos distintos, e nenhum
deles é o que "aprovar" nomearia sozinho.

**Regra proposta.** Regra corrigida, com nome, parâmetros e fundamentação
próprios, pronta para ocupar uma linha do Sisprev. Recebe identificador próprio
porque o catálogo recebido é preservado como veio, e corrigir frequentemente
muda o número de regras.

**Carga de homologação.** Conjunto das regras propostas aptas a serem
conferidas em campo contra o sistema, antes de qualquer ativação. Integrar a
carga não equivale a estar em produção.

**Ressalva de homologação.** Conferência técnica que condiciona a ativação em
produção da regra que alcança — não a sua entrada em carga. É atributo da
regra.

**Conferência em aberto.** Questão que a auditoria deixou expressamente por
responder num componente, dirigida ao IPERON. Não é atributo de regra, e não se
confunde com a ressalva de homologação.

**Identificadores de auditoria.** Os códigos no formato `C1-Rxx` relacionam
cada conclusão, conferência ou dependência ao registro correspondente deste
ciclo. Não são identificadores de regras do Sisprev, e aparecem neste documento
apenas para permitir a rastreabilidade da matéria.

# Conclusões jurídicas do Ciclo 1

A composição proposta cobre integralmente o tema no escopo do ciclo. As
conclusões abaixo recaem sobre o texto normativo transcrito em cada capítulo.

1. **As causas que afastam a proporcionalização estão cobertas uma a uma**,
   conforme a lei as enumera, e a causa residual tem regra própria.
2. **As doenças graves, contagiosas ou incuráveis deixam de ser categoria
   única** e passam a ter uma regra por moléstia, com o nome da doença expresso
   na regra e na sua fundamentação, e com a restrição de cargo consignada onde
   a lei a impõe.
3. **A lei distingue três famílias de enquadramento**, porque condiciona o
   cálculo não apenas à data de ingresso, mas também à opção pelo regime de
   previdência complementar.
4. **A base de cálculo e o ajuste proporcional são dimensões distintas**: a
   integralidade significa ausência de redução pelo tempo, e não implica, por
   si, cálculo sobre determinada base.
5. **Cada requisito aferido tem fundamento identificado** em dispositivo
   transcrito, e a fundamentação de cada regra articula como eles se combinam.

## As três famílias de enquadramento

**Conclusão jurídica.** A legislação produz três famílias mutuamente
excludentes:

1. ingresso até 31/12/2003, sem opção pelo regime de previdência complementar;
2. ingresso de 01/01/2004 a 05/11/2018, sem essa opção;
3. ingresso a partir de 06/11/2018 **ou** opção prévia e expressa validamente
   feita por quem ingressou antes daquela data.

As duas vias da terceira família produzem o mesmo efeito jurídico — mesma base,
mesmos limitadores, mesmo reajustamento —, razão pela qual constituem uma
família só. Elas são repartidas no tempo: a opção do § 16 do art. 40 da
Constituição cabe a quem ingressou até a implantação do regime complementar, e
de 06/11/2018 em diante a sujeição é automática.

**Demonstração.** A Lei Complementar Estadual nº 1.100/2021 condiciona o
cálculo à posição do servidor perante o regime de previdência complementar em
três dispositivos centrais: o art. 24, *caput*, alcança quem ingressou após 31
de dezembro de 2003 "e que não tenham feito a opção" de que trata o § 16 do
art. 40 da Constituição Federal; o art. 25 alcança quem ingressou até
31/12/2003 e "que não tenha feito a opção" do mesmo dispositivo; e o art. 27,
inciso I, assegura a paridade "desde que não tenha feito a opção". Em sentido
inverso, o art. 24, § 11, sujeita ao limite máximo dos benefícios do Regime
Geral o segurado sujeito àquele regime, e o § 12 estende o mesmo limite a quem
ingressou a partir da implementação do regime complementar estadual, ocorrida
em 6 de novembro de 2018.

## Base de cálculo da família de ingresso até 2003

**Conclusão jurídica.** O servidor ingressado até 31 de dezembro de 2003 requer
a aposentadoria por incapacidade pela regra permanente da Lei Complementar
Estadual nº 1.100/2021, e é o art. 25 — dentro desse próprio regime vigente,
não por direito adquirido a regime anterior — que disciplina a base de cálculo
dessa família: a remuneração do cargo efetivo, integral nas causas
qualificadas e proporcional na causa comum.

**Demonstração.** O art. 25 emprega a mesma delimitação pessoal com que o art.
27, inciso I, assegura a paridade: "que tenha ingressado no serviço público em
cargo efetivo até 31 de dezembro de 2003". O art. 30 remete a base ao art. 24
por duas vias — nas causas qualificadas, diretamente, pelo § 13; na causa
comum, pelo encadeamento entre o § 14 e o art. 26, § 1º. A Procuradoria-Geral
do Estado entende que essa remissão não afasta a disciplina do art. 25 para a
família de ingresso até 31/12/2003, cujo *caput* delimita o alcance pessoal da
norma. A remissão importa a fórmula de cálculo, não o âmbito pessoal do artigo
remetido — o art. 24 fala expressamente de ingresso **após** 31 de dezembro de
2003\.

A família de ingresso passa, assim, a produzir dois efeitos: separa quem tem
paridade de quem não tem (art. 27, incisos I e II) e separa também a base de
cálculo, harmonizando os arts. 24 e 25 como divisão vigente sem exigir que a
média contributiva alcance quem nunca a integrou.

**Alcance desta conclusão.** Entendimento diverso sobre a premissa não comporta
ajuste de uma regra isolada: implica rever a base de cálculo de todo o ramo de
ingresso até 2003.

# Justificativa da individualização e da nomenclatura das regras

## Individualização por moléstia

**Decisão de representação.** O § 8º do art. 30 institui lista nominada de
moléstias, e o que a lei exige é que a causa qualificada seja efetivamente
identificada e comprovada. Quinze das moléstias listadas compartilham o mesmo
tratamento jurídico; a diferença de regime está no inciso XVI, que alcança
surdez permanente e anomalia da fala apenas no magistério.

Representar cada moléstia em regra própria é escolha de granularidade do
catálogo, adotada para tornar a seleção, a fundamentação e a revisão do ato
mais transparentes: a cada moléstia corresponde prova própria, que a junta
médica precisa dizer qual reconheceu, e uma única regra para todas obrigaria o
ato concessório a afirmar que houve doença do rol sem dizer qual.

A individualização **preserva o conteúdo jurídico das hipóteses e altera a sua
representação no catálogo**. As restrições específicas previstas em lei ficam
mantidas em qualquer das duas representações.

## Função operacional da nomenclatura das regras

Quem concede o benefício escolhe o tipo de benefício e depois a regra pela
lista de nomes, de modo que o nome é instrumento de seleção. Ele traz as
facetas que separam uma regra das outras, na ordem em que a instrução do
benefício as apura: benefício; condição funcional especial, quando houver;
causa da incapacidade; família de enquadramento; resultado do cálculo; e
paridade, quando aplicável.

A nomenclatura apresenta primeiro a causa da incapacidade e, em seguida, a
família, reproduzindo a sequência da instrução: primeiro se identifica a causa
apurada — com base no laudo médico e, quando necessário, na prova
administrativa do nexo e das circunstâncias funcionais —; depois se verifica a
família de enquadramento e a fórmula correspondente. Resultado do cálculo e
paridade aparecem separados porque respondem a dispositivos distintos.

## Unicidade dos nomes

No catálogo recebido, **53 das 112 regras repetem o nome de outra**: há quatro
linhas com a mesma denominação, e quem as vê lado a lado na tela não tem como
saber qual aplicar. O nome único é condição de seleção correta: sem ele, a
decisão sobre qual regra incide fica com quem opera o sistema, sem critério à
vista, e a diferença entre duas delas pode ser a paridade do provento pelo
resto da vida do servidor.

<!-- responsabilidades -->

# Ressalvas de homologação

Cada ressalva abaixo é condição verificável: indica o que deve ser conferido,
que evidência a encerra e o que decorre da divergência. Elas condicionam a
ativação em produção das regras que alcançam, **não** a entrada delas na carga.

## Ressalva técnica — base da proporcionalização na causa comum

**Classe.** Base do cálculo proporcional.

**Questão a verificar.** Confirmar que a forma de cálculo proporcional
projetada executa, nesta hipótese, a fração em dias do art. 26 sobre a base já
limitada — e não uma proporcionalidade aplicada diretamente sobre a
remuneração.

**Cenário de homologação.** Requerimento de causa comum em cada família, com
tempo de contribuição inferior ao exigido, comparando o valor calculado pelo
sistema ao valor esperado segundo a base descrita no capítulo do componente.

**Resultado esperado.** Coincidência entre o valor calculado e o valor
esperado, com a base composta explicitada no memorial de cálculo.

**Evidência de encerramento.** Relatório de homologação com os cenários, os
dados de entrada, o resultado calculado, o resultado esperado e a validação da
unidade responsável.

**Efeito da divergência.** As regras alcançadas não podem ser ativadas em
produção até a correção ou a instituição de controle administrativo suficiente.

**Rastreabilidade interna:** `C1-R32`.

## Ressalva técnica — sujeição ao regime complementar e teto do RGPS

**Classe.** Aplicação do limite máximo dos benefícios do Regime Geral.

**Questão a verificar.** Confirmar por qual informação o sistema reconhece a
sujeição ao regime de previdência complementar e em que etapa do cálculo aplica
o limite máximo dos benefícios do Regime Geral, inclusive a sua posição
relativamente ao limite da remuneração do cargo efetivo.

**Cenário de homologação.** Requerimentos de servidor ingressado a partir de
06/11/2018 e de servidor ingressado antes dessa data com opção expressa,
comparando o provento calculado ao limite aplicável.

**Resultado esperado.** Aplicação do limite na etapa descrita no capítulo do
componente, com identificação correta da sujeição em ambas as vias.

**Evidência de encerramento.** Relatório de homologação com os cenários, os
dados de entrada, o resultado calculado, o resultado esperado e a validação da
unidade responsável; e, onde a identificação não for automática, o ato que
institui o controle administrativo correspondente.

**Efeito da divergência.** As regras alcançadas não podem ser ativadas em
produção até a correção ou a instituição de controle administrativo suficiente.

**Rastreabilidade interna:** `C1-R34`, `C1-R15`.

## Dependência externa — protocolo de reconhecimento da moléstia profissional

Matéria que depende de definição institucional ainda não produzida. **Não é
ressalva de implantação de regra** e não integra as duas classes acima: a
regra correspondente está juridicamente definida, e o que falta é o protocolo
administrativo pelo qual o nexo profissional se reconhece no caso concreto.

**Providência.** Definição, pelo IPERON, do protocolo de reconhecimento do nexo
de moléstia profissional, com indicação do órgão competente, da prova exigida e
do momento processual da aferição.

**Rastreabilidade interna:** `C1-R75`.

# Controle administrativo na ausência de seleção automática

Onde a seleção da regra aplicável não for integralmente resolvida pelo sistema,
o IPERON deverá instituir controle administrativo documentado que identifique:

1. a unidade ou o servidor responsável pela conferência;
2. o momento processual em que ela ocorre;
3. os dados e documentos examinados, especialmente a data de ingresso e a
   eventual opção prévia e expressa pelo regime de previdência complementar;
4. o resultado do enquadramento;
5. o registro dessa conferência no processo administrativo;
6. a revisão do cálculo antes da elaboração do ato concessório.

A definição do procedimento é providência do Instituto, anterior à ativação em
produção. Verificação administrativa documentada é controle suficiente: o
mesmo modelo já se aplica à causa da incapacidade, ao nexo de acidente em
serviço e de moléstia profissional, à condição funcional de magistério e à
impossibilidade de readaptação — fatos apurados no processo, e não na linha do
catálogo.

# Responsabilidades e providências

| Responsável                                 | Competência nesta entrega                                                                                                                                                 |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Procuradoria-Geral do Estado                | concluir a auditoria jurídica; definir o enquadramento normativo; registrar as ressalvas; prestar esclarecimentos jurídicos quando necessário                             |
| Coordenação                                 | registrar a providência de sua competência; encaminhar o relatório; acompanhar a execução e a documentação das medidas; consolidar o encerramento do ciclo administrativo |
| IPERON — unidade técnica                    | preparar e inserir a carga; executar os cenários de homologação; documentar entradas, resultados e divergências; corrigir comportamentos incompatíveis                    |
| IPERON — unidade responsável pela concessão | definir os controles administrativos; indicar responsáveis; registrar a conferência no processo; impedir a elaboração do ato sem enquadramento e cálculo conferidos       |
| Autoridade administrativa competente        | decidir sobre a implantação depois de concluída a homologação; não autorizar a produção enquanto houver divergência não tratada                                           |

Onde o titular exato não estiver identificado neste relatório, vale a categoria
institucional indicada, que deve ser preenchida pela unidade coordenadora antes
da assinatura.

<!-- notas -->

# Notas de seção do relatório

Cada `##` abaixo é uma nota, indexada pela sua chave. A página busca a nota
pela chave; chave ausente **derruba o build**, porque uma seção sem nota sairia
sem aviso num documento já juntado ao processo.

Este preâmbulo não entra no índice.

## origens

As regras abaixo estão cadastradas no Sisprev e a auditoria concluiu que devem
ser desativadas. A desativação preserva o identificador e o histórico de cada
uma: nenhum identificador é reaproveitado para hipótese juridicamente
diferente.

## destinos

As regras propostas abaixo são o que a auditoria propõe pôr no lugar. Cada uma
tem identidade própria, fora do espaço de identificadores do catálogo
cadastrado, e declara de que regras descende.

## projecao

O arquivo de carga traz cada regra proposta projetada nas colunas do sistema, em
formato importável. Ele contém exatamente as regras deste ciclo, e nenhuma
outra: a importação integral do arquivo não leva à homologação regra sobre a
qual este relatório não se manifestou. A identificação abaixo permite verificar
que o arquivo recebido é aquele sobre o qual esta manifestação se deu.

## dispositivos

O texto abaixo é o da lei, transcrito na redação vigente à época a que cada
regra se refere, e reimpresso para que a conferência não dependa de outra
fonte. Ele se repete de um capítulo a outro quando as regras citam a mesma
norma: cada capítulo é conferido isoladamente.

Antes de cada transcrição, em itálico, vem o papel que as regras propostas do
capítulo atribuem à provisão — a que critério ela responde. O papel é afirmação
da Procuradoria sobre a norma; a transcrição é a norma. Quando uma provisão é
alcançada por remissão de outra, é o papel que diz o que a remissão importa:
uma remissão à fórmula de cálculo de um artigo não arrasta o âmbito pessoal do
*caput* dele.

## manifestacao

A conclusão da Procuradoria-Geral do Estado sobre este componente vem ao final
da seção. Antes dela vão as conferências que a auditoria deixou expressamente
em aberto: nenhuma é matéria jurídica — dependem do comportamento do sistema ou
de definição administrativa do Instituto —, e o campo que acompanha cada uma é
onde o Instituto consigna a providência correspondente. Quando a mesma
conferência alcança mais de uma regra proposta, ela vai enunciada uma única
vez, com a relação das regras que alcança.

## manifestacao-sem-pontos

Sobre este componente a auditoria não deixou conferência em aberto. As
ressalvas de homologação eventualmente indicadas no selo acima são atributo das
regras propostas e estão descritas na seção própria deste relatório; elas
condicionam a ativação em produção, não a entrada em carga.

## manifestacao-geral

Conclusão da Procuradoria-Geral do Estado sobre o componente: concluída a
auditoria jurídica das regras propostas que o compõem, **não se identifica
óbice jurídico** à substituição das regras cadastradas pelas regras propostas,
nos termos deste capítulo.

Esta conclusão não é autorização de ativação em produção: a homologação deve
confirmar o comportamento do sistema, e o controle administrativo documentado é
admissível onde o automatismo não bastar. Nenhum ato concessório pode ser
produzido sem a conferência dos requisitos e do cálculo no caso concreto.

## manifestacao-bloqueada

Este componente não integra a carga de homologação. Pelo menos uma das regras
propostas que o compõem ainda não tem auditoria jurídica ou representação
concluída; a substituição atômica permanece bloqueada até que a pendência seja
resolvida e o componente seja novamente conferido a partir dos dados.

<!-- encerramento -->

# Etapas posteriores à conclusão da auditoria jurídica

A conclusão jurídica deste ciclo está consolidada. Dos requisitos que a
substituição efetiva do catálogo exige, os que são de auditoria estão cumpridos
e documentados:

- as {{destinos}} regras propostas estão com a auditoria jurídica concluída;
- os {{grupos}} componentes de substituição têm, cada um, decisão de completude
  conferida contra o texto normativo transcrito, e todos integram a carga de
  homologação;
- {{regrasComRessalva}}, em duas classes descritas na seção própria; as demais
  integram a carga sem ressalva específica;
- a composição como um todo tem decisão de completude registrada;
- cada regra cadastrada que sai dispôs expressamente de todo apontamento aberto
  que a nomeia.

O que ainda não ocorreu, e não é de auditoria, se ordena nesta sequência:

1. **inserção das {{destinos}} regras no ambiente de homologação**;
2. **execução dos cenários representativos**, cobrindo cada família, cada
   classe de causa e a causa comum, inclusive os cenários que respondem às
   ressalvas;
3. **confirmação ou definição dos controles**, automáticos e administrativos,
   com a documentação correspondente;
4. **correção do comportamento divergente** que a homologação apontar, por
   parametrização, ajuste do sistema, aplicação do limitador em etapa própria
   ou controle procedimental obrigatório antes do ato;
5. **decisão sobre a implantação**, pela autoridade administrativa competente,
   e o respectivo ato — enquanto ele não for praticado e registrado, o catálogo
   hoje cadastrado permanece o único em vigor.

Divergência apurada em homologação impede a ativação em produção. Nenhum desses
passos é condição de encerramento deste ciclo: a conclusão jurídica aqui firmada
não fica pendente deles.

# Documentos que compõem a entrega

1. este relatório jurídico;
2. o Anexo I, com a relação das regras propostas;
3. o Anexo II, com as regras que levam ressalva de homologação;
4. o Anexo III, com a projeção de cada regra nos campos do sistema;
5. o arquivo de carga de homologação, identificado por resumo criptográfico na
   seção própria, a ser juntado ao mesmo processo administrativo.

A Procuradoria-Geral do Estado permanece à disposição para as questões
jurídicas que a implantação suscitar.
