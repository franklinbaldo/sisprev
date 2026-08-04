# Relatório de conformidade do Ciclo 1 da auditoria de regras do Sisprev

> Documento de conferência, elaborado com assistência de IA e revisado pela
> coordenação da auditoria. Não é fonte normativa, não decide questão jurídica e
> não altera regra, achado ou dado. Onde a verificação depende de leitura humana,
> o relatório declara essa condição em vez de apresentá-la como resultado
> automático.

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

**Conclusão prática:** o Ciclo 1 **não pode ser declarado encerrado**. Oito das
onze condições estão cumpridas; três não. A causa é comum às três e está nas
regras propostas, não na análise jurídica que as gerou: as quarenta unidades que
a composição apresenta como prontas ainda registram, em seus próprios textos,
conferência humana não concluída; quatro delas não incorporam ao campo de
seleção um requisito legal que a lei impõe; e duas apresentam contradição interna
sobre a fórmula de cálculo que projetam para o sistema.

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
  documento afirma faltar;
- os **achados** — as acusações datadas que a auditoria registra — que nomeiam as
  regras do ciclo, para conferir se cada um recebeu disposição escrita;
- os **artefatos derivados** que o repositório publica, para conferir se
  correspondem ao que as fontes gravam.

A verificação não decide questão jurídica. Onde a conformidade depende de juízo
sobre a lei, o relatório indica que a competência é da coordenação da auditoria.

## 5. Síntese executiva

| resultado     | condições                |
| ------------- | ------------------------ |
| cumpridas     | 1, 2, 4, 6, 7, 8, 10, 11 |
| não cumpridas | 3, 5, 9                  |

As três condições não cumpridas decorrem dos achados **A7**, **A8** e **A9**,
todos relativos às quarenta regras propostas. Nenhum deles se resolve por
redação: exigem conferência de mérito e decisão da coordenação, com efeito sobre
campos que iriam para o sistema.

Quatro divergências encontradas durante a verificação — **A1**, **A3-bis**,
**A10** e **A11** — eram inconsistências entre documentos e dados já decididos, e
foram corrigidas nas próprias fontes, sem decisão jurídica nova.

Em consequência deste relatório, o documento do ciclo deixou de declarar a
auditoria concluída e passou a registrar o estado "auditoria em fechamento — não
encerrada", com os campos de data e commit de fechamento em branco.

## 6. Resultado por condição

| #   | condição                                                           | resultado                            |
| --- | ------------------------------------------------------------------ | ------------------------------------ |
| 01  | nenhuma regra sabidamente errada permanece ativa                   | cumprida (A3)                        |
| 02  | toda regra desativada com substituta ou registro fundamentado      | cumprida                             |
| 03  | combinações relevantes cobertas por regras ativas                  | **não cumprida** (A8)                |
| 04  | lacuna preexistente preenchida por regra com identificador próprio | cumprida                             |
| 05  | ausência de lacunas de cobertura                                   | **não cumprida** (A8)                |
| 06  | ausência de sobreposição não intencional                           | cumprida por conferência humana      |
| 07  | sobreposição intencional justificada                               | cumprida                             |
| 08  | mapa de substituição completo                                      | cumprida                             |
| 09  | ausência de pendência que afete a cobertura material               | **não cumprida** (A7, A8, A9)        |
| 10  | cenários demonstram a seleção esperada                             | cumprida por conferência humana (A4) |
| 11  | artefatos derivados e demais controles íntegros                    | cumprida após correção (A11)         |

Evidência das condições cumpridas:

- a cadeia de composições resolve sem grupo declarado duas vezes, e as quatro
  regras substituídas saem efetivamente do conjunto proposto;
- os dois grupos de substituição do ciclo estão ativos, cada um com decisão de
  completude que registra autor, data, justificativa e fonte no texto legal
  transcrito;
- todas as quarenta regras propostas existem e estão declaradas prontas para
  implantação;
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

Os achados A1, A3-bis, A10 e A11 foram corrigidos nas fontes. Os achados A2, A4,
A5 e A6 são registros sem providência exigida. Os achados A7, A8 e A9 permanecem
abertos e são a razão do não encerramento.

### A7 — Conferência humana não concluída nas quarenta regras propostas

**Situação: aberto. Impede o encerramento.**

O campo de estado declara as quarenta regras prontas para implantação. O texto de
todas as quarenta, contudo, mantém em aberto o item "concluir a conferência
humana desta regra". Distribuídos pelo grupo, aparecem ainda "confirmar a fórmula
de cálculo", "confirmar a projeção operacional" e "definir o protocolo
institucional de reconhecimento do nexo profissional".

As pendências registradas não têm a mesma natureza, e a distinção é relevante:

- **dependências externas** — confirmar como o sistema captura e classifica a
  causa da incapacidade, como o diagnóstico é cotejado com o inciso legal, e a
  ausência de campo próprio para a opção do § 16 do art. 40 da Constituição.
  A especificação admite que dependência externa permaneça registrada, e estas
  não impedem o encerramento;
- **conferências da própria auditoria** — concluir a conferência humana da regra,
  confirmar a fórmula de cálculo e confirmar a projeção operacional. É a estas
  que a condição 9 se refere, e são elas que impedem.

**Providência:** concluir as conferências e registrar a evidência em cada regra,
ou rever o estado declarado. Ambas são competência da coordenação da auditoria.

### A8 — Requisito legal do magistério não incorporado ao campo de seleção

**Situação: aberto. Impede o encerramento. Classificação: bloqueante.**

O inciso XVI do § 8º do art. 30 da Lei Complementar Estadual nº 1.100/2021
restringe surdez permanente e anomalia da fala ao caso de magistério. Nas quatro
regras correspondentes, essa restrição consta do nome da regra e da fundamentação
redigida, mas **não** dos elementos que comandam a seleção: o cabeçalho
estruturado registra apenas a classe da causa e o regime de ingresso, e o
protocolo de verificação pergunta pelo diagnóstico e pela posterioridade à
filiação ao regime próprio, sem exigir prova de que o servidor ocupa cargo de
magistério.

Tal como modelado, o protocolo admite selecionar essas regras para servidor que
não integra o magistério — hipótese que a lei exclui. Por afetar a seleção, e não
apenas o rito de conferência, o defeito compromete também as condições 3 e 5.

O defeito é das regras propostas, não da análise jurídica: a matriz do ciclo
separa corretamente as duas hipóteses, e o que falta é o requisito descer do nome
para o campo.

**Providência:** incorporar o requisito de magistério ao cabeçalho estruturado, à
pergunta do protocolo e à evidência exigida das quatro regras. É modelagem com
efeito sobre campo que vai para o sistema, e depende de decisão da coordenação.

### A9 — Contradição interna na projeção de cálculo das regras de causa comum

**Situação: aberto. Impede o encerramento. Classificação: bloqueante.**

As duas regras de causa comum projetam para o Sisprev o rótulo de cálculo
"Proporcionalidade Dias". O texto de ambas, porém, afirma que o rótulo "Não
identificado" evitaria representar como simples proporcionalidade em dias uma
fórmula que é composta — média apurada na forma de um dispositivo, proporcional
na forma de outro, com o reajuste disciplinado em terceiro.

A afirmação não está redigida como registro histórico: descreve como vigente uma
projeção diferente da que o cabeçalho grava. Some-se que a mesma regra mantém em
aberto o item "confirmar a fórmula de cálculo", que é precisamente a decisão de
que a contradição depende.

**Providência:** decidir qual rótulo o sistema deve receber e harmonizar
cabeçalho e texto. A decisão é da coordenação, porque define o que o Sisprev
executa.

### A1 — Rótulo do ciclo mais amplo que o seu objeto

**Situação: corrigido nesta revisão.**

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
decisão da coordenação.

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

**Situação: corrigido nesta revisão.**

A especificação de ciclos afirmava que as hipóteses históricas seriam promovidas
pelo Ciclo 2. O Ciclo 2 trata de pensão por morte e benefícios derivados, e as
sete regras pertencem ao Ciclo 9. A passagem passou a nomear o Ciclo 9. Não houve
decisão jurídica nova: a responsabilidade já estava registrada, e apenas o texto
de referência divergia.

### A4 — Verificação dos cenários é humana

**Situação: registrado, sem providência exigida.**

Ver a nota ao final da seção 6. Registre-se que o piloto de seleção constante do
acervo de análises **não** serve como prova desta condição: utiliza outro
conjunto de casos, executa modelo diverso e declara-se documento não oficial.

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

**Situação: corrigido na sinalização.**

O documento da sessão que propôs a substituição registra, no cabeçalho
estruturado, vinte destinos por coorte, grupos ativos e decisões de completude;
o texto, redigido antes, ainda descrevia oito unidades, grupos inativos e regras
em elaboração. O texto passou a declarar-se registro daquela sessão, com regra de
precedência explícita em favor do cabeçalho.

A sinalização não resolve dois itens daquela lista — a classificação operacional
da causa e a conclusão da conferência humana —, que permanecem abertos nas regras
e integram o achado A7.

### A11 — Planilha de homologação divergente e fora dos controles

**Situação: corrigido nesta revisão.**

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
diretório não é coberto pelos controles automáticos.

## 8. Limitações

- A verificação não julga o mérito jurídico das regras. Que a fundamentação
  invocada seja a correta, que a fórmula descreva o cálculo devido e que a
  matriz esgote as hipóteses da lei são conclusões da coordenação da auditoria.
- As condições 6 e 10 dependem de leitura humana e são reportadas como tais. A
  ausência de contradição identificada não equivale a demonstração automática.
- Os achados A8 e A9 foram identificados na revisão da coordenação de 04/08/2026
  e confirmados aqui contra os arquivos. Não se afirma que a verificação
  esgotou os defeitos das quarenta regras: ela alcançou o que os campos e os
  textos permitem cotejar.
- A verificação retrata o estado do repositório na data indicada.

## 9. Conclusão

A análise jurídica do Ciclo 1 está avançada e a sua estrutura se sustenta: a
matriz de hipóteses, o mapa de substituição, a precedência entre regimes e os
cenários representativos foram entregues e resistem à conferência.

O ciclo, porém, **não está encerrado**, e as quarenta regras propostas não podem
ser tratadas como integralmente conferidas. Três das onze condições cumulativas
não se cumprem, e a razão está nas próprias regras: conferência humana não
concluída em todas elas, requisito legal ausente do campo de seleção em quatro, e
contradição interna sobre a fórmula projetada em duas.

O que resta não é formalidade de registro. É conferência de mérito, regra a
regra, com correção de campos que seriam implantados no sistema — e é competência
da coordenação da auditoria.

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

| item                                        | referência                                              |
| ------------------------------------------- | ------------------------------------------------------- |
| ciclo auditado                              | `okf/regras-sisprev/ciclos/ciclo-01.md`                 |
| composição proposta                         | `okf/conjuntos/ciclo-01-s6-fechamento.md`               |
| critério de encerramento                    | `okf/spec/ciclo.md`                                     |
| regras propostas                            | `okf/regras-propostas/regras/incapacidade-lce1100-*.md` |
| regras substituídas                         | `regra-0019` a `regra-0022`                             |
| composição corrente registrada pela PR #102 | `bea6f20c1c6b8b38f7da6db8f24623033a874902`              |
| planilha de homologação vigente             | `data/regras-propostas.csv`                             |
