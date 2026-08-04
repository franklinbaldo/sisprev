# Relatório de conformidade do Ciclo 1 da auditoria de regras do Sisprev

> Documento de conferência, elaborado com assistência de IA e revisado pela
> coordenação da auditoria. Não é fonte normativa, não decide questão jurídica e
> não altera regra, achado ou dado por si só — as correções que ele recomenda são
> aplicadas nas fontes, e é a fonte, não este relatório, que passa a valer. Onde a
> verificação depende de leitura humana, o relatório declara essa condição em vez
> de apresentá-la como resultado automático.
>
> Este documento tem três camadas, todas de 04/08/2026. A primeira verificação
> apontou três condições não cumpridas (achados A7, A8 e A9) e quatro
> divergências editoriais, já corrigidas nas fontes. A segunda camada registrou
> correções nas próprias regras propostas e as tratou como suficientes para
> encerrar a auditoria. A revisão da coordenação sobre essa segunda camada
> identificou que parte da correção excedia o que a evidência sustentava — em
> especial, que uma verificação executada por agente havia sido registrada como
> "conferência humana concluída", e que a projeção de cálculo das duas unidades
> de causa comum não podia permanecer `deployable` sem confirmação operacional.
> A terceira camada aplica essa correção. As seções 5 a 9 refletem o estado após
> ela; a seção 7 preserva o histórico de cada achado.

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
onze condições estão cumpridas; três não. Um defeito de mérito foi corrigido
nesta revisão — a contradição textual entre o rótulo de cálculo e a
proveniência das duas unidades de causa comum — e um segundo foi parcialmente
corrigido — o requisito de magistério passou a integrar a seleção estruturada
das quatro unidades do inciso XVI, mas o marco temporal da aferição permanece
sem decisão fundamentada. O terceiro não foi corrigido: nenhuma das quarenta
regras propostas tem revisão humana da coordenação registrada. O que existe é
verificação automatizada, executada por agente, que cotejou cada regra contra a
matriz jurídica já decidida pelo ciclo — insumo útil para essa revisão, mas não
substituto dela. Adicionalmente, as duas unidades de causa comum recuaram de
`deployable` para `preview`, porque a projeção de cálculo que carregam não tem
confirmação operacional suficiente para essa afirmação; como a ativação de um
grupo de substituição exige que todos os seus destinos estejam `deployable`,
os dois grupos do Bloco C voltaram a `inativo`, e as quatro regras legadas
continuam sendo a fonte operacional.

## 3. Escopo

O Ciclo 1 examinou quatro regras cadastradas de incapacidade permanente e propôs
substituí-las por quarenta regras novas.

A Lei Complementar Estadual nº 1.100/2021 separa, no cálculo do benefício, as
causas que afastam a proporcionalização — acidente em serviço, moléstia
profissional e as doenças graves relacionadas em lei — das demais, chamadas aqui
de causa comum. Essas quatro classes de causa são juridicamente distintas: cada
uma segue fórmula e requisitos de comprovação próprios, e representá-las numa
única linha, como faziam as regras cadastradas, misturava fundamentações que a
lei separa. Isso é o defeito de mérito que a auditoria corrigiu.

Decompor a classe "doença catalogada" em dezessete unidades, uma por moléstia do
rol do art. 30, § 8º, é decisão diferente: as dezessete têm o mesmo tratamento
jurídico entre si — mesma fórmula, mesma ausência de proporcionalização, mesmo
regime de paridade por coorte —, exceto as duas que o inciso XVI restringe ao
magistério. Granularidade de aferição — uma linha por doença, em vez de uma
linha para toda a classe — é **conveniência do IPERON**, não imposição legal:
a decisão de completude de cada grupo de substituição registra que essa
granularidade foi a escolhida, e o catálogo poderia, em tese, consolidar as
quinze moléstias sem a restrição do inciso XVI numa única linha, mantendo a
cobertura. A auditoria não afirma que a lei exigia quarenta linhas; afirma que
a lei distingue quatro classes de causa, e que a granularidade adicional dentro
da classe "doença catalogada" foi escolha documentada do IPERON, registrada
como tal na decisão de completude de cada grupo — RFC 0004 §0 é expressa
nesse ponto: decompor 1:N e consolidar N:1 são escolhas de granularidade, não
correções de erro.

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
  quanto no texto redigido: o dispositivo taxonômico citado foi cotejado com o
  texto do inciso correspondente, as datas de admissão e de direito foram
  cotejadas com as fronteiras de coorte que a própria matriz do ciclo declara,
  a projeção de `tipo_calculo`/`integral`/`paridade` foi cotejada com a classe
  de causa e a coorte, e o nome da causa foi cotejado com a fundamentação
  redigida;
- os **achados** — as acusações datadas que a auditoria registra — que nomeiam as
  regras do ciclo, para conferir se cada um recebeu disposição escrita;
- os **artefatos derivados** que o repositório publica, para conferir se
  correspondem ao que as fontes gravam.

A verificação não decide questão jurídica nova. Onde a conformidade dependeu de
juízo sobre a lei já fixado pela matriz do ciclo, o método cotejou a regra
contra essa matriz já decidida; não a rederivou. **Essa ressalva é central
para esta revisão:** o cotejo regra a regra descrito acima foi executado por
agente, não por leitura humana da coordenação, e não deve ser confundido com a
"conferência humana desta regra" que o checklist de cada unidade exige. É
insumo para essa conferência, não substituto dela.

## 5. Síntese executiva

| resultado     | condições                |
| ------------- | ------------------------ |
| cumpridas     | 1, 2, 4, 6, 7, 8, 10, 11 |
| não cumpridas | 3, 5, 9                  |

As três condições não cumpridas decorrem dos achados **A7**, **A8** e **A9**,
todos relativos às quarenta regras propostas:

- **A7** — nenhuma das quarenta regras tem revisão humana da coordenação
  registrada. Existe verificação automatizada de consistência estrutural,
  registrada no corpo de cada unidade, mas ela coteja campos contra a matriz
  já decidida — não substitui a leitura humana que a condição 9 exige;
- **A8** — o requisito de magistério do inciso XVI passou a integrar
  `predicados` e um item próprio de `requisitos_verificacao_humana` nas quatro
  unidades que ele restringe, corrigindo o defeito central (seleção sem exigir
  magistério). Uma formulação anterior desta mesma revisão havia fixado o
  marco temporal do vínculo ("ao tempo do acometimento") sem fundamento no
  dispositivo; foi retirada, e a decisão sobre o marco correto permanece
  pendente de fundamentação da coordenação;
- **A9** — a contradição textual entre `tipo_calculo` e `proveniencia.notas`
  das duas unidades de causa comum foi corrigida: a fórmula jurídica está
  confirmada e documentada, e a nota não mais defende um rótulo diferente do
  gravado. Mas o próprio rótulo (`Proporcionalidade Dias`) tem fidelidade
  parcial severa o bastante para admitir uma leitura que descarta a base
  média por completo, e RFC 0004 §5.3 trata semântica operacional não
  confirmada como impeditivo de `deployable`. As duas unidades recuaram para
  `preview`.

Quatro divergências editoriais da primeira verificação — **A1**, **A3-bis**,
**A10** e **A11** — eram inconsistências entre documentos e dados já decididos,
sem decisão jurídica nova, e permanecem corrigidas nas fontes.

O documento do ciclo registra o estado "auditoria em fechamento — não
encerrada", com os campos de data e commit de fechamento em branco.

## 6. Resultado por condição

| #   | condição                                                           | resultado                            |
| --- | ------------------------------------------------------------------ | ------------------------------------ |
| 01  | nenhuma regra sabidamente errada permanece ativa                   | cumprida (A3)                        |
| 02  | toda regra desativada com substituta ou registro fundamentado      | cumprida                             |
| 03  | combinações relevantes cobertas por regras ativas                  | **não cumprida** (A8, A9)            |
| 04  | lacuna preexistente preenchida por regra com identificador próprio | cumprida                             |
| 05  | ausência de lacunas de cobertura                                   | **não cumprida** (A8, A9)            |
| 06  | ausência de sobreposição não intencional                           | cumprida por conferência humana      |
| 07  | sobreposição intencional justificada                               | cumprida                             |
| 08  | mapa de substituição completo                                      | cumprida                             |
| 09  | ausência de pendência que afete a cobertura material               | **não cumprida** (A7, A8, A9)        |
| 10  | cenários demonstram a seleção esperada                             | cumprida por conferência humana (A4) |
| 11  | artefatos derivados e demais controles íntegros                    | cumprida após correção (A11)         |

As condições 3 e 5 voltaram a não cumpridas por razão distinta da primeira
verificação: não é mais que o campo de seleção das quatro unidades do inciso
XVI ignore o magistério — isso foi corrigido —, mas sim que (a) o marco
temporal do requisito de magistério carece de decisão fundamentada e (b) os
dois grupos de substituição do Bloco C estão `inativo`, de modo que nenhuma
das quarenta regras propostas efetivamente cobre coisa alguma no catálogo
operacional ainda: as quatro origens legadas continuam sendo a fonte, pela
regra de seleção de origem única do exportador.

Evidência das condições cumpridas:

- a cadeia de composições resolve sem grupo declarado duas vezes;
- todas as quarenta regras propostas existem e têm sua correspondência com a
  matriz T7 verificada por agente, com evidência registrada no próprio corpo;
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
A5 e A6 são registros sem providência exigida. Os achados A7, A8 e A9
permanecem abertos, em graus distintos, e são a razão do não encerramento.

### A7 — Conferência humana não concluída nas quarenta regras propostas

**Situação: aberto. Impede o encerramento.**

O campo de estado declara as quarenta regras prontas para implantação. Uma
verificação automatizada, executada por agente nesta mesma revisão, cotejou
cada unidade contra a matriz jurídica já decidida — dispositivo citado contra
o texto do inciso, datas contra a coorte, projeção de cálculo contra a classe
de causa, nome da causa contra a fundamentação — e registrou essa evidência no
corpo de cada regra. **Essa verificação não é a conferência humana que a
condição 9 exige.** Registrá-la como "conferência humana concluída", com
decisões atribuídas nominalmente à coordenação, teria sido tratar a execução
do agente como revisão que não ocorreu; a redação foi corrigida para nomear a
verificação pelo que ela é, e o item "concluir a conferência humana desta
regra" permanece aberto no checklist de todas as quarenta unidades.

**Providência:** revisão humana expressa da coordenação, regra a regra ou por
decisão consolidada, registrando o que foi lido e aprovado. É trabalho que
esta revisão não pode suprir por si.

### A8 — Requisito legal do magistério não incorporado ao campo de seleção

**Situação: parcialmente corrigido. Impede o encerramento das condições 3, 5 e
9.**

O inciso XVI do § 8º do art. 30 da Lei Complementar Estadual nº 1.100/2021
restringe surdez permanente e anomalia da fala ao caso de magistério. Nas
quatro regras correspondentes, essa restrição constava do nome e da
fundamentação, mas não dos elementos que comandavam a seleção. A correção
acrescentou um predicado estruturado e um item próprio do protocolo de
verificação humana, com responsável (a unidade de gestão de pessoas, não a
junta médica — o vínculo com o magistério é fato funcional, não clínico),
meio de prova e evidência exigida.

Uma formulação intermediária desta mesma revisão fixou o marco temporal do
vínculo como "contemporâneo ao acometimento da moléstia". O dispositivo diz
apenas "no caso de magistério", sem indicar se o vínculo deve existir no
acometimento, na instrução do requerimento, na concessão do benefício ou em
outro momento; fixar um desses marcos sem fundamento na fonte era decisão
jurídica nova, não instanciação de decisão já tomada. A formulação foi
retirada; o protocolo de verificação não presume mais um marco, e a decisão
sobre qual é o correto permanece pendente de fundamentação da coordenação.

**Providência:** decisão fundamentada da coordenação sobre o marco temporal de
aferição do vínculo com o magistério, com a base normativa ou administrativa
que a sustente.

### A9 — Contradição interna na projeção de cálculo das regras de causa comum

**Situação: corrigido quanto à contradição textual; o `estado_proposta`
recuou para `preview`. Impede o encerramento da condição 9, com efeito em 3 e
5 pela inativação do grupo (ver seção 6).**

As duas regras de causa comum projetavam `tipo_calculo: Proporcionalidade Dias` enquanto a nota de proveniência defendia `Não identificado`. A
investigação encontrou que a fórmula jurídica já estava decomposta e
documentada (`forma-calculo-media-proporcional-dias-lce1100`: média
proporcionalizada em dias, reajuste disciplinado à parte) e que a projeção
`Proporcionalidade Dias` já havia sido decidida para essa fórmula, com
fidelidade parcial expressamente declarada. A nota foi corrigida para
acompanhar essa decisão, e a contradição textual não existe mais.

A fidelidade parcial em si, porém, é severa: o rótulo representa o ajuste em
dias, mas não expressa a base média, e sem confirmação é compatível com uma
leitura que zera a média e computa proporcionalidade pura em dias — alterando
o valor do benefício. RFC 0004 §5.3 é expressa: semântica operacional não
confirmada é fail-closed para `deployable`, ainda que passe em `preview`. As
duas unidades recuaram, e como a ativação de um grupo de substituição exige
que **todos** os seus destinos estejam `deployable` (RFC 0004 §1.4), os dois
grupos do Bloco C voltaram a `estado_grupo: inativo`.

**Providência:** confirmação do IPERON/fornecedor de que o rótulo projetado
executa a fórmula composta (issue #124), ou identificação de outra via que
permita afirmar a projeção sem essa confirmação.

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
e o campo é opcional precisamente porque só o ciclo fechado a possui.

Não há, porém, estado que separe "auditoria concluída" de "aguardando ato
institucional", nem data de encerramento — o registro de data corresponde à
abertura. Se a lacuna justifica campo novo é decisão da coordenação, registrada
como issue de acompanhamento, sem implementação nesta revisão.

### A3 — Fundamento da condição 1

**Situação: registrado, sem providência exigida.**

A condição 1 se cumpre por duas razões distintas: no escopo do ciclo, porque
nenhuma regra sabidamente errada permanece ativa sem substituta autorada —
ainda que a substituição não esteja efetiva pela inativação dos grupos (A9);
nas janelas históricas, porque elas estão fora do escopo e da responsabilidade
deste ciclo.

### A3-bis — Especificação apontava ciclo sucessor incorreto

**Situação: corrigido.**

A especificação de ciclos afirmava que as hipóteses históricas seriam promovidas
pelo Ciclo 2. O Ciclo 2 trata de pensão por morte e benefícios derivados, e as
sete regras pertencem ao Ciclo 9. A passagem passou a nomear o Ciclo 9.

### A4 — Verificação dos cenários é humana

**Situação: registrado, sem providência exigida.**

Ver a nota ao final da seção 6.

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
catálogo. É dado da importação, não vínculo com o Ciclo 1.

### A10 — Documento de sessão com estado divergente do seu próprio cabeçalho

**Situação: corrigido na sinalização; os dois itens residuais viraram A7 e
A9.**

O documento da sessão que propôs a substituição registra, no cabeçalho
estruturado, vinte destinos por coorte; o texto, redigido antes, ainda
descrevia oito unidades e grupos inativos. O texto passou a declarar-se
registro histórico daquela sessão, com regra de precedência explícita em
favor do frontmatter — que, nesta revisão, também voltou a `estado_grupo: inativo` (A9), tornando o corpo histórico novamente descritivo do estado
corrente nesse ponto específico.

### A11 — Planilha de homologação divergente e fora dos controles

**Situação: corrigido.**

A planilha de homologação do ciclo exportava as quarenta regras com espécie de
benefício anterior à reforma e com marcação de não implantável, enquanto as
regras registram a espécie vigente. Regenerada a partir das fontes, mostrou-se
idêntica à planilha corrente; o arquivo divergente foi removido, com registro
da remoção no README do diretório. Permanece verdadeiro que aquele diretório
não é coberto pelos controles automáticos — registrado como issue de
acompanhamento.

## 8. Limitações e dependências externas

- A verificação não julga o mérito jurídico originário das regras. Que a
  fundamentação invocada seja a correta e que a matriz esgote as hipóteses da
  lei são conclusões da coordenação da auditoria, fixadas nas sessões que
  produziram a matriz do ciclo (T1 a T9 de `ciclo-01.md`) e não rederivadas
  aqui.

- **A verificação regra a regra desta revisão foi executada por agente, não
  por leitura humana da coordenação.** Ela cotejou cada unidade contra a
  matriz já decidida — é evidência estrutural útil, mas não é, e não deve ser
  registrada como, a "conferência humana" que a condição 9 exige. Uma versão
  anterior desta mesma revisão cometeu esse erro de atribuição; foi corrigida
  antes da publicação desta camada.

- As condições 6 e 10 dependem de leitura humana e são reportadas como tais. A
  ausência de contradição identificada não equivale a demonstração automática.

- Fidelidade parcial de uma projeção de cálculo (`projecao_sisprev.fidelidade: parcial`) não é, por si, impeditiva de `deployable` — é a condição da
  maioria das formas de cálculo do catálogo, porque o enum legado do Sisprev é
  mais pobre que a fórmula jurídica. Neste caso específico, porém, a omissão
  não é de detalhe operacional: é da própria base de cálculo, e por isso RFC
  0004 §5.3 se aplica.

- Permanecem abertas, como dependência operacional externa e não como
  pendência da auditoria, três questões que dependem de resposta do IPERON e do
  fornecedor do Sisprev (issue #124):

  - como o sistema captura e classifica a causa da incapacidade do requerente;
  - se o rótulo de cálculo projetado para cada regra de fato executa a fórmula
    jurídica que a regra descreve — para a causa comum, essa mesma confirmação
    também resolveria A9;
  - como é tratada, no processo, a opção pelo regime de previdência
    complementar do § 16 do art. 40 da Constituição Federal.

- A verificação retrata o estado do repositório na data indicada.

## 9. Conclusão

A análise jurídica do Ciclo 1 está avançada e a sua estrutura se sustenta: a
matriz de hipóteses, o mapa de substituição, a precedência entre regimes e os
cenários representativos foram entregues e resistem à conferência.

O ciclo, porém, **não está encerrado**. Três das onze condições cumulativas
não se cumprem. Duas causas têm providência definida e pendente de decisão da
coordenação: o marco temporal do requisito de magistério (A8) e a confirmação
operacional do rótulo de cálculo da causa comum, ou via alternativa que a
dispense (A9) — enquanto essa segunda não vier, os dois grupos de substituição
do Bloco C permanecem `inativo`, e as quatro regras legadas continuam sendo a
fonte operacional. A terceira — revisão humana da coordenação nas quarenta
regras (A7) — é trabalho que nenhuma verificação automatizada substitui.

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
regras propostas. Ativa e reverte por inteiro — todos os destinos precisam
estar `deployable` para o grupo ativar (RFC 0004 §1.4) —, porque aprovar
metade deixaria hipótese sem representação ou representada duas vezes.

**Preview** — estado de uma regra proposta cujo modelo jurídico está
registrado, mas que ainda admite pendência em campo operacional. Não entra no
export para o sistema.

**Pronta para implantação (`deployable`)** — estado que declara a regra
proposta sem pendência operacional aberta, apta a ocupar uma linha do sistema
quando o grupo a que pertence ativar.

**Regra proposta** — regra corrigida, redigida pela auditoria em espaço de
identificação próprio, fora da numeração do catálogo recebido, porque corrigir
frequentemente altera o número de regras.

## 11. Rastreabilidade

| item                                        | referência                                                                    |
| ------------------------------------------- | ----------------------------------------------------------------------------- |
| ciclo auditado                              | `okf/regras-sisprev/ciclos/ciclo-01.md`                                       |
| composição proposta                         | `okf/conjuntos/ciclo-01-s6-fechamento.md`                                     |
| grupos de substituição do Bloco C           | `okf/conjuntos/ciclo-01-s4-bloco-c.md`                                        |
| critério de encerramento                    | `okf/spec/ciclo.md`                                                           |
| fail-closed de `deployable`                 | `docs/rfc/0004-schema-enriquecido-e-compilador-para-o-sisprev.md`, §5.3, §1.4 |
| regras propostas                            | `okf/regras-propostas/regras/incapacidade-lce1100-*.md`                       |
| regras substituídas                         | `regra-0019` a `regra-0022`                                                   |
| composição corrente registrada pela PR #102 | `bea6f20c1c6b8b38f7da6db8f24623033a874902`                                    |
| planilha de homologação vigente             | `data/regras-propostas.csv`                                                   |
| requisito de magistério (A8)                | [issue #121](https://github.com/franklinbaldo/sisprev/issues/121)             |
| `tipo_calculo` da causa comum (A9)          | [issue #122](https://github.com/franklinbaldo/sisprev/issues/122)             |
| conferência humana das quarenta regras (A7) | [issue #123](https://github.com/franklinbaldo/sisprev/issues/123)             |
| dependências externas registradas           | [issue #124](https://github.com/franklinbaldo/sisprev/issues/124)             |
| confirmações do fornecedor                  | `docs/analysis/confirmacoes-do-fornecedor-do-sisprev.md`                      |
