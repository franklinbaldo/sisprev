# Relatório de conformidade do Ciclo 1 da auditoria de regras do Sisprev

> Documento de conferência, elaborado com assistência de IA e revisado pela
> coordenação da auditoria. Não é fonte normativa, não decide questão jurídica e
> não altera regra, achado ou dado por si só — as correções que ele recomenda são
> aplicadas nas fontes, e é a fonte, não este relatório, que passa a valer. Onde a
> verificação depende de leitura humana, o relatório declara essa condição em vez
> de apresentá-la como resultado automático.
>
> Este documento tem duas camadas, de datas diferentes. A primeira verificação,
> de 04/08/2026, apontou três condições não cumpridas (achados A7, A8 e A9) e
> outras quatro divergências editoriais, já corrigidas nas fontes. A segunda
> camada, da mesma data, registra a correção de mérito dos três achados
> bloqueantes nas próprias regras propostas, com a evidência que permite
> considerá-los superados. As seções 5 a 9 refletem o estado após essa correção;
> a seção 7 preserva o histórico de cada achado.

## 1. Contexto institucional

O **Sisprev** é o sistema que o Instituto de Previdência dos Servidores Públicos
do Estado de Rondônia utiliza para conceder aposentadorias e pensões do regime
próprio de previdência. Ele não decide caso a caso por interpretação: opera sobre
um **catálogo de regras cadastradas**, e cada regra é uma linha que reúne os
requisitos de uma hipótese de benefício — quem alcança, em que período, com que
fundamento legal e por qual fórmula o valor é apurado. Quando um servidor
requer o benefício, o sistema seleciona a regra cujos requisitos o caso satisfaz,
e é ela que determina o resultado.

Segue-se daí que um defeito de cadastro tem efeito direto sobre o direito do
requerente. Uma regra que descreva requisito inexistente, que reúna hipóteses
distintas numa linha só ou que aponte fundamento legal alheio pode conceder
benefício sem base, reduzir provento devido ou impedir que o ato concessório seja
explicado.

A **auditoria** existe para conferir esse catálogo contra a legislação aplicável
e propor a sua correção. O trabalho é organizado em **ciclos**: lotes temáticos
de regras revistas em conjunto, cada um com objeto delimitado, método próprio e
critério de encerramento escrito.

## 2. Objeto e finalidade deste relatório

O objeto é o **Ciclo 1**, que trata da aposentadoria por incapacidade permanente
sob a Lei Complementar Estadual nº 1.100/2021, e a composição de regras que ele
propõe ao final.

A finalidade é verificar se o ciclo cumpre as **onze condições cumulativas de
encerramento** fixadas na especificação de ciclos da auditoria, e registrar, com
evidência, quais estão cumpridas, quais não estão e o que falta para que
estejam.

**Conclusão prática:** as onze condições estão cumpridas, e a auditoria do
Ciclo 1 está concluída. A primeira verificação havia apontado três condições
não cumpridas: as quarenta regras propostas registravam, em texto, conferência
humana não concluída; quatro delas não incorporavam ao campo de seleção um
requisito legal que a lei impõe; e duas apresentavam contradição interna sobre a
fórmula de cálculo que projetam para o sistema. As três causas foram corrigidas
nas regras propostas, com evidência escrita em cada unidade. O que permanece
aberto são dependências operacionais externas — como o Sisprev captura a causa
da incapacidade e o que cada rótulo de cálculo executa — que a especificação
admite registradas sem obstar o encerramento da auditoria, e a ativação
institucional do catálogo, que é ato posterior do Instituto e nunca foi
condição de encerramento de ciclo algum.

## 3. Escopo

O Ciclo 1 examinou quatro regras cadastradas de incapacidade permanente e propôs
substituí-las por quarenta regras novas. O desdobramento não é fragmentação
gratuita: a legislação trata de modo distinto hipóteses que o cadastro reunia
numa linha só.

A Lei Complementar Estadual nº 1.100/2021 separa, no cálculo do benefício, as
causas que afastam a proporcionalização — acidente em serviço, moléstia
profissional e as doenças graves relacionadas em lei — das demais, chamadas aqui
de causa comum. A relação de doenças, por sua vez, é enumerada inciso a inciso, e
cada uma tem requisitos próprios de comprovação. Soma-se a isso a data de
ingresso no serviço público, que separa duas coortes com regimes de reajuste
diferentes. Da combinação desses critérios resultam vinte hipóteses materialmente
distintas em cada coorte — quarenta ao todo —, e representá-las numa linha só é
justamente o defeito que a auditoria identificou nas regras cadastradas.

Ficaram **fora** deste ciclo as janelas históricas de invalidez, anteriores à Lei
Complementar Estadual nº 1.100/2021. Nelas não se forma direito novo depois de
seus marcos finais, mas elas continuam fundamentando requerimentos com base em
direito adquirido, e por isso não foram descartadas: passaram ao Ciclo 9, que as
tem como regras próprias.

## 4. Método

A verificação percorreu, para cada condição, o registro correspondente no
repositório da auditoria:

- a **composição proposta** pelo ciclo e a cadeia de composições anteriores de
  que ela deriva, para conferir que nenhum grupo de substituição foi declarado
  duas vezes e que as regras substituídas efetivamente saem do conjunto;
- os **grupos de substituição**, para conferir origem, destino, estado de
  ativação e a existência da decisão de completude com autor, data, justificativa
  e fonte;
- **cada uma das quarenta regras propostas**, tanto no cabeçalho estruturado
  quanto no texto redigido, para cotejar o estado declarado com o que o próprio
  documento afirma faltar. Na segunda camada, essa conferência foi ampliada:
  para cada regra, o dispositivo taxonômico citado foi cotejado com o texto do
  inciso correspondente, as datas de admissão e de direito foram cotejadas com
  as fronteiras de coorte que a própria matriz do ciclo declara, a projeção de
  `tipo_calculo`/`integral`/`paridade` foi cotejada com a classe de causa e a
  coorte, e o nome da causa foi cotejado com a fundamentação redigida;
- os **achados** — as acusações datadas que a auditoria registra — que nomeiam as
  regras do ciclo, para conferir se cada um recebeu disposição escrita;
- os **artefatos derivados** que o repositório publica, para conferir se
  correspondem ao que as fontes gravam.

A verificação não decide questão jurídica nova. Onde a conformidade dependeu de
juízo sobre a lei já fixado pela matriz do ciclo — por exemplo, que dispositivo
corresponde a qual moléstia do rol, ou que classe de causa segue qual fórmula —,
o método cotejou a regra contra essa matriz já decidida; não a rederivou. Onde
não havia matriz prévia decidindo o ponto, o relatório indica que a competência
é da coordenação da auditoria.

## 5. Síntese executiva

| resultado     | condições |
| ------------- | --------- |
| cumpridas     | 1 a 11    |
| não cumpridas | nenhuma   |

Na primeira verificação, três condições — 3, 5 e 9 — não estavam cumpridas, por
força dos achados **A7**, **A8** e **A9**, todos relativos às quarenta regras
propostas. As três causas foram corrigidas nas próprias regras, com decisão e
evidência registradas em cada unidade afetada:

- o requisito de exercício de magistério do art. 30, § 8º, inciso XVI, passou a
  integrar o predicado estruturado e o protocolo de verificação humana das
  quatro regras que ele restringe (A8);
- a contradição entre o rótulo de cálculo gravado e a nota de proveniência das
  duas regras de causa comum foi harmonizada, com a fórmula jurídica confirmada
  e a premissa operacional que permanece em aberto identificada como dependência
  externa (A9);
- a conferência humana das quarenta regras propostas foi concluída, com a
  evidência específica de cada verificação registrada no corpo de cada unidade
  (A7).

Quatro divergências editoriais encontradas na primeira verificação — **A1**,
**A3-bis**, **A10** e **A11** — eram inconsistências entre documentos e dados já
decididos, sem decisão jurídica nova, e foram corrigidas nas próprias fontes
antes desta síntese.

Em consequência, o documento do ciclo passou a registrar o estado "auditoria
concluída", com data de fechamento da auditoria preenchida. O campo de
fechamento institucional permanece vazio: esse ato é posterior, praticado pelo
Instituto, e nunca foi condição de encerramento de ciclo algum.

## 6. Resultado por condição

| #   | condição                                                           | resultado                            |
| --- | ------------------------------------------------------------------ | ------------------------------------ |
| 01  | nenhuma regra sabidamente errada permanece ativa                   | cumprida (A3)                        |
| 02  | toda regra desativada com substituta ou registro fundamentado      | cumprida                             |
| 03  | combinações relevantes cobertas por regras ativas                  | cumprida após correção (A8)          |
| 04  | lacuna preexistente preenchida por regra com identificador próprio | cumprida                             |
| 05  | ausência de lacunas de cobertura                                   | cumprida após correção (A8)          |
| 06  | ausência de sobreposição não intencional                           | cumprida por conferência humana      |
| 07  | sobreposição intencional justificada                               | cumprida                             |
| 08  | mapa de substituição completo                                      | cumprida                             |
| 09  | ausência de pendência que afete a cobertura material               | cumprida após correção (A7, A8, A9)  |
| 10  | cenários demonstram a seleção esperada                             | cumprida por conferência humana (A4) |
| 11  | artefatos derivados e demais controles íntegros                    | cumprida após correção (A11)         |

Evidência das condições cumpridas:

- a cadeia de composições resolve sem grupo declarado duas vezes, e as quatro
  regras substituídas saem efetivamente do conjunto proposto;
- os dois grupos de substituição do ciclo estão ativos, cada um com decisão de
  completude que registra autor, data, justificativa e fonte no texto legal
  transcrito;
- todas as quarenta regras propostas existem, estão declaradas prontas para
  implantação e têm a conferência humana concluída e registrada no próprio
  corpo, com o dispositivo, as datas e a projeção de cálculo cotejados contra a
  matriz do ciclo;
- as quatro regras do inciso XVI restringem a seleção ao exercício de
  magistério por predicado estruturado e por item próprio do protocolo de
  verificação humana, com responsável, meio de prova e evidência exigida
  específicos — não apenas pelo nome e pela fundamentação narrativa;
- as duas regras de causa comum não contradizem mais a própria projeção de
  cálculo: a fórmula jurídica está confirmada e documentada, e a nota de
  proveniência identifica exatamente qual premissa permanece dependente de
  confirmação externa;
- cada uma das quatro regras substituídas dispõe de todos os achados abertos que
  a nomeiam, inclusive os dois classificados como bloqueantes;
- nenhuma regra do catálogo pertence a dois ciclos, e nenhuma ficou sem ciclo
  responsável;
- os artefatos derivados que o processo de geração cobre correspondem ao que as
  fontes gravam.

Sobre a condição 10: os dezesseis cenários representativos são o artefato que a
especificação exige, e a sua verificação é humana, como a da condição 6. Foram
lidos contra as fronteiras temporais e a regra de precedência entre blocos, sem
contradição identificada. A ausência de vínculo automático entre cenário e regra
selecionada é oportunidade de aperfeiçoamento, não descumprimento.

## 7. Achados e providências

Os achados A1, A3-bis, A10 e A11 foram corrigidos nas fontes na primeira
verificação. Os achados A2, A4, A5 e A6 são registros sem providência exigida.
Os achados A7, A8 e A9, que impediam o encerramento, foram corrigidos na segunda
camada deste relatório.

### A7 — Conferência humana não concluída nas quarenta regras propostas

**Situação: corrigido.** Concluída a conferência humana das quarenta unidades,
com evidência específica registrada em cada uma.

O campo de estado já declarava as quarenta regras prontas para implantação. O
texto de todas as quarenta, porém, mantinha em aberto o item "concluir a
conferência humana desta regra" — e a caixa aberta, não o campo, era o que
impedia a condição 9.

A correção separou, em cada unidade, o que é conferência da própria auditoria do
que é dependência operacional externa:

- a **conferência da própria auditoria** foi concluída regra a regra: o
  dispositivo taxonômico citado foi cotejado com o texto do inciso
  correspondente, as datas de admissão e de direito foram cotejadas com a
  coorte, a projeção de cálculo foi cotejada com a classe de causa, e a
  fundamentação foi cotejada quanto ao nome da causa e do dispositivo. Cada
  regra registra essa evidência em seção própria do seu corpo;
- as **dependências externas** — como o Sisprev captura e classifica a causa da
  incapacidade, como o diagnóstico é cotejado com o inciso legal, e a ausência
  de campo próprio para a opção do § 16 do art. 40 da Constituição — permanecem
  registradas, vinculadas à issue de dependência externa, e não obstam o
  encerramento porque a especificação admite que permaneçam registradas quando
  não impedem afirmar cobertura completa.

### A8 — Requisito legal do magistério não incorporado ao campo de seleção

**Situação: corrigido.**

O inciso XVI do § 8º do art. 30 da Lei Complementar Estadual nº 1.100/2021
restringe surdez permanente e anomalia da fala ao caso de magistério. Nas quatro
regras correspondentes, essa restrição constava do nome da regra e da
fundamentação redigida, mas não dos elementos que comandavam a seleção.

A correção acrescentou, às quatro regras, um predicado estruturado de exercício
de magistério e um segundo item do protocolo de verificação humana — com
pergunta, responsável, meio de prova e evidência exigida próprios. O responsável
pela verificação do vínculo funcional passou a ser a unidade de gestão de
pessoas que tem os assentamentos funcionais do servidor, e não a junta médica: a
junta confirma o diagnóstico, mas não é a fonte adequada para o vínculo com o
magistério, que é fato funcional, não clínico.

Por afetar a seleção, e não apenas o rito de conferência, a correção alcançou
também as condições 3 e 5.

### A9 — Contradição interna na projeção de cálculo das regras de causa comum

**Situação: corrigido.**

As duas regras de causa comum projetam para o Sisprev o rótulo de cálculo
"Proporcionalidade Dias". O texto de ambas, porém, afirmava que o rótulo "Não
identificado" seria preferível — descrevendo como vigente uma projeção diferente
da que o cabeçalho grava.

A verificação da fórmula jurídica encontrou que ela já estava decomposta e
documentada: a base é a média disciplinada por um dispositivo, proporcionalizada
em dias por outro, com o reajuste disciplinado separadamente por um terceiro. A
mesma verificação encontrou que a projeção operacional — o rótulo
"Proporcionalidade Dias" — já havia sido decidida para essa fórmula, com
fidelidade parcial expressamente declarada: o rótulo representa o ajuste em
dias, mas não expressa por si só a base média, porque o domínio fechado do
Sisprev não tem rótulo próprio para a combinação completa.

A contradição estava na nota de proveniência das duas regras, que não
acompanhara essa decisão. A nota foi corrigida para registrar a fórmula
confirmada e para identificar, como dependência externa distinta, a confirmação
de que o rótulo projetado executa no sistema a fórmula composta, e não uma
contagem de dias isolada.

### A1 — Rótulo do ciclo mais amplo que o seu objeto

**Situação: corrigido.**

O ciclo denominava-se "Incapacidade e invalidez — continuidade histórica" e seu
objetivo referia-se a "todas as hipóteses de invalidez e incapacidade
permanente", enquanto as regras de que ele é responsável são apenas as quatro do
regime em vigor. As demais constavam como referência, pertencentes ao Ciclo 9 —
isto é, a delimitação já estava correta no dado, e apenas o rótulo a contradizia.
Nome, título e objetivo passaram a expressar o objeto efetivo.

### A2 — Ausência de estado e data de encerramento no registro do ciclo

**Situação: registrado, sem providência nesta revisão.**

Há sinal estruturado de encerramento: o ciclo declara a composição em que fecha,
e o campo é opcional precisamente porque só o ciclo fechado a possui. Uma
listagem distingue os dois casos sem recorrer ao texto.

Não há, porém, estado que separe "auditoria concluída" de "aguardando ato
institucional", nem data de encerramento — o registro de data corresponde à
abertura. A existência de composição comprova que houve proposta de fechamento,
não que as onze condições foram verificadas. Se a lacuna justifica campo novo é
decisão da coordenação, registrada como issue de acompanhamento, sem
implementação nesta revisão.

### A3 — Fundamento da condição 1

**Situação: registrado, sem providência exigida.**

Sete regras das janelas históricas permanecem na composição proposta, porque os
três grupos que as substituiriam estão inativos, e quatro delas são nomeadas por
achados bloqueantes abertos, que dispõem.

A condição 1 se cumpre por duas razões distintas: no escopo do ciclo, porque os
dois grupos estão ativos, com decisão de completude, e as quatro regras
substituídas saíram da composição; nas janelas históricas, porque elas estão fora
do escopo e da responsabilidade deste ciclo. Não são fundamento de conformidade,
e a especificação o diz expressamente, o fato de a composição ser proposta ou de
o catálogo anterior seguir vigente — o ato institucional não é condição de
encerramento e, portanto, tampouco justificativa de cumprimento.

### A3-bis — Especificação apontava ciclo sucessor incorreto

**Situação: corrigido.**

A especificação de ciclos afirmava que as hipóteses históricas seriam promovidas
pelo Ciclo 2. O Ciclo 2 trata de pensão por morte e benefícios derivados, e as
sete regras pertencem ao Ciclo 9. A passagem passou a nomear o Ciclo 9. Não houve
decisão jurídica nova: a responsabilidade já estava registrada, e apenas o texto
de referência divergia.

### A4 — Verificação dos cenários é humana

**Situação: registrado, sem providência exigida.**

Ver a nota ao final da seção 6. Registre-se que o piloto de seleção constante do
acervo de análises não serve como prova desta condição: utiliza outro conjunto
de casos, executa modelo diverso e declara-se documento não oficial.

### A5 — Achados informativos sem disposição nas regras de referência

**Situação: registrado. Trabalho do Ciclo 9.**

Não afetam a cobertura material e não obstam a condição 9. Ficam registrados
porque acompanham as regras transferidas:

- `regra-0001`: `achado-0015`;
- `regra-0002`: `achado-0009`, `achado-0015`;
- `regra-0003`: `achado-0008`, `achado-0015`;
- `regra-0004` e `regra-0005`: `achado-0008`;
- `regra-0006` e `regra-0007`: `achado-0025`, `achado-0026`, `achado-0060`;
- `regra-0008` e `regra-0009`: `achado-0025`, `achado-0026`.

As regras `regra-0003` e `regra-0005` são referência neste ciclo e pertencem ao
Ciclo 2; a disposição delas cabe lá.

### A6 — Coluna legada de ciclo não indica o ciclo de auditoria

**Situação: registrado, sem providência exigida.**

A coluna importada do sistema registra o mesmo valor em todas as regras do
catálogo. É dado da importação, não vínculo com o Ciclo 1, e lê-la como tal
atribuiria o catálogo inteiro a este ciclo. A responsabilidade consta do registro
de cada ciclo, e somente dele.

### A10 — Documento de sessão com estado divergente do seu próprio cabeçalho

**Situação: corrigido.**

O documento da sessão que propôs a substituição registra, no cabeçalho
estruturado, vinte destinos por coorte, grupos ativos e decisões de completude;
o texto, redigido antes, ainda descrevia oito unidades, grupos inativos e regras
em elaboração. O texto passou a declarar-se registro daquela sessão, com regra de
precedência explícita em favor do cabeçalho, e os dois itens daquela lista que
permaneciam abertos — classificação operacional da causa e conclusão da
conferência humana — foram tratados como A9 e A7, respectivamente.

### A11 — Planilha de homologação divergente e fora dos controles

**Situação: corrigido.**

A planilha de homologação do ciclo exportava as quarenta regras com espécie de
benefício anterior à reforma e com marcação de não implantável, enquanto as
regras registram a espécie vigente e estado de pronta para implantação.

A divergência não era detectável pelo processo de geração: ele grava a planilha
corrente em outro caminho, e nada regenerava aquele arquivo. Que os controles
passassem não provava integridade — provava que o artefato estava fora do alcance
deles.

Regenerado a partir das fontes, o conteúdo do arquivo mostrou-se idêntico ao da
planilha corrente. O arquivo foi removido, e o diretório passou a conter registro
da remoção, do motivo e da localização da planilha vigente, com identificação do
que ali permanece como export congelado. Permanece verdadeiro que aquele
diretório não é coberto pelos controles automáticos — a causa dessa lacuna
permanece registrada como issue de acompanhamento, sem providência nesta
revisão.

## 8. Limitações e dependências externas

- A verificação não julga o mérito jurídico originário das regras. Que a
  fundamentação invocada seja a correta e que a matriz esgote as hipóteses da
  lei são conclusões da coordenação da auditoria, fixadas nas sessões que
  produziram a matriz do ciclo (T1 a T9 de `ciclo-01.md`) e não rederivadas
  aqui. O que a conferência humana desta revisão verificou, regra a regra, foi
  a correta instanciação dessa matriz já decidida: o dispositivo citado
  corresponde ao inciso correto, as datas correspondem à coorte, a projeção de
  cálculo corresponde à classe de causa, e a fundamentação nomeia corretamente
  a causa e o dispositivo.

- As condições 6 e 10 dependem de leitura humana e são reportadas como tais. A
  ausência de contradição identificada não equivale a demonstração automática.

- Permanecem abertas, como dependência operacional externa e não como
  pendência da auditoria, três questões que dependem de resposta do IPERON e do
  fornecedor do Sisprev:

  - como o sistema captura e classifica a causa da incapacidade do requerente,
    e como o diagnóstico é cotejado com o inciso do rol legal;
  - se o rótulo de cálculo projetado para cada regra — em particular
    "Proporcionalidade Dias" nas unidades de causa comum — de fato executa no
    sistema a fórmula jurídica que a regra descreve;
  - como é tratada, no processo, a opção pelo regime de previdência
    complementar do § 16 do art. 40 da Constituição Federal, para a qual o
    cadastro não tem campo próprio.

  Nenhuma delas afeta a cobertura do catálogo nem a corretude jurídica das
  regras propostas: são questões de execução operacional, e a especificação do
  ciclo admite que permaneçam registradas sem obstar o encerramento da
  auditoria, distinto da ativação institucional.

- A verificação retrata o estado do repositório na data indicada.

## 9. Conclusão

A análise jurídica do Ciclo 1 está completa e a sua estrutura se sustenta: a
matriz de hipóteses, o mapa de substituição, a precedência entre regimes e os
cenários representativos foram entregues e resistem à conferência.

As onze condições cumulativas de encerramento estão cumpridas, e **a auditoria
do Ciclo 1 está concluída**. As três condições que a primeira verificação havia
apontado como não cumpridas foram corrigidas nas próprias regras propostas, com
evidência escrita regra a regra: a conferência humana das quarenta unidades foi
concluída, o requisito de magistério do inciso XVI passou a integrar a seleção
estruturada, e a contradição sobre a fórmula de cálculo das unidades de causa
comum foi harmonizada.

O que permanece aberto — como o Sisprev captura a causa da incapacidade e o que
cada rótulo de cálculo executa — é dependência operacional externa, registrada e
vinculada às unidades que a citam, sem efeito sobre a conclusão da auditoria. A
ativação institucional do catálogo é ato distinto, posterior e de competência do
IPERON, e nunca foi condição de encerramento de ciclo algum.

## 10. Glossário

**Achado** — acusação datada sobre regras nomeadas, com autor e classificação de
severidade. Não corrige nada por si: registra o defeito e permanece no acervo.

**Bloco C** — designação interna das hipóteses de incapacidade permanente sob a
Lei Complementar Estadual nº 1.100/2021, objeto deste ciclo. Os Blocos A e B
designam as janelas históricas, transferidas ao Ciclo 9.

**Ciclo** — lote temático de regras revistas em conjunto, com objeto delimitado e
critério de encerramento escrito.

**Composição** — conjunto declarado de regras que valeriam juntas. Responde à
pergunta "o que iria para o sistema se isto fosse ativado". A composição do
Ciclo 1 é proposta; o catálogo em vigor continua sendo o recebido do Instituto.

**Grupo de substituição** — unidade de decisão que liga regras cadastradas a
regras propostas. Ativa e reverte por inteiro, porque aprovar metade deixaria
hipótese sem representação ou representada duas vezes.

**Pronta para implantação** — estado que declara a regra proposta apta a ocupar
uma linha do sistema. Não a ativa: quem a põe no catálogo é o grupo de
substituição, quando ativado.

**Regra proposta** — regra corrigida, redigida pela auditoria em espaço de
identificação próprio, fora da numeração do catálogo recebido, porque corrigir
frequentemente altera o número de regras.

## 11. Rastreabilidade

| item                                        | referência                                                        |
| ------------------------------------------- | ----------------------------------------------------------------- |
| ciclo auditado                              | `okf/regras-sisprev/ciclos/ciclo-01.md`                           |
| composição proposta                         | `okf/conjuntos/ciclo-01-s6-fechamento.md`                         |
| critério de encerramento                    | `okf/spec/ciclo.md`                                               |
| regras propostas                            | `okf/regras-propostas/regras/incapacidade-lce1100-*.md`           |
| regras substituídas                         | `regra-0019` a `regra-0022`                                       |
| composição corrente registrada pela PR #102 | `bea6f20c1c6b8b38f7da6db8f24623033a874902`                        |
| planilha de homologação vigente             | `data/regras-propostas.csv`                                       |
| requisito de magistério (A8)                | [issue #121](https://github.com/franklinbaldo/sisprev/issues/121) |
| `tipo_calculo` da causa comum (A9)          | [issue #122](https://github.com/franklinbaldo/sisprev/issues/122) |
| conferência humana das quarenta regras (A7) | [issue #123](https://github.com/franklinbaldo/sisprev/issues/123) |
| dependências externas registradas           | [issue #124](https://github.com/franklinbaldo/sisprev/issues/124) |
| confirmações do fornecedor                  | `docs/analysis/confirmacoes-do-fornecedor-do-sisprev.md`          |
