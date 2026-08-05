# Relatório de conformidade do Ciclo 1 da auditoria de regras do Sisprev

> Documento de conferência, elaborado com assistência de IA e revisado pela
> coordenação da auditoria. Não é fonte normativa, não decide questão jurídica e
> não altera regra, achado ou dado por si só — as correções que ele recomenda são
> aplicadas nas fontes, e é a fonte, não este relatório, que passa a valer. Onde a
> verificação depende de leitura não programática, o relatório declara essa
> condição em vez de apresentá-la como resultado automático.
>
> Este relatório usa a
> [matriz de derivação e verificação do Ciclo 1](matriz-derivacao-verificacao-ciclo-01.md)
> como fonte para as seções 5 a 9. A matriz substitui, para as quarenta regras
> do Bloco C, a exigência de uma leitura humana idêntica registrada quarenta
> vezes: a correspondência estrutural entre regra e requisito é demonstrada
> uma vez por requisito, e as decisões jurídicas e operacionais de fato
> pendentes aparecem como linhas específicas da matriz, não como um checkbox
> genérico repetido em cada arquivo.

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

**Conclusão prática:** o Ciclo 1 **não pode ser declarado encerrado**. A
matriz de derivação e verificação cobre os setenta requisitos derivados que
as quarenta regras do Bloco C instanciam, com fonte, regras alcançadas,
representação, modo de verificação, responsável e evidência para cada um.
Dessa cobertura, uma linha permanece pendente de decisão da coordenação:
**C1-R24**, o marco temporal do requisito de magistério do inciso XVI, que
carece de decisão jurídica fundamentada (issue #121), afetando as quatro
regras do inciso XVI. **C1-R32** — a identificação unívoca, no Sisprev, da
fórmula de causa comum da LCE 1.100 — deixou de ser pendência de auditoria
nesta revisão: a derivação está concluída e as duas regras correspondentes
são `estado_proposta: deployable`; o que resta é `estado_implantacao: pendente_mapeamento_sisprev`, que bloqueia apenas a troca da fonte
operacional de exportação dos dois grupos de substituição do Bloco C —
mantidos `estado_grupo: inativo` — sem obstar o fechamento do ciclo quanto
a essa derivação (issue #122). Três dependências externas adicionais —
captura da causa pelo Sisprev, confirmação geral de `tipo_calculo` e
protocolo institucional de nexo de moléstia profissional (issue #124) —
permanecem registradas sem bloquear a cobertura das regras a que se
referem. Nenhuma das demais trinta e seis regras tem pendência material
aberta.

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
correções de erro. A matriz de derivação e verificação preserva essa mesma
decisão: não reabre a granularidade, apenas centraliza a prova de que cada
uma das quarenta regras a instancia corretamente.

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
- a **matriz de derivação e verificação**, construída nesta revisão a partir
  da matriz jurídica já decidida pelo ciclo (T1 a T9 de `ciclo-01.md`): cada
  requisito foi extraído da lei, ligado à sua fonte, associado às regras que o
  materializam e classificado quanto ao modo de verificação — programático,
  quando se reduz a cotejo determinístico de campo contra requisito; não
  programático, quando exige avaliação substantiva de fato ou documento no
  caso concreto; ou misto, quando tem as duas camadas;
- **cada uma das quarenta regras propostas**, cotejadas contra a matriz: o
  dispositivo taxonômico citado foi conferido contra o texto do inciso
  correspondente, as datas de admissão e de direito contra as fronteiras de
  coorte, a projeção de `tipo_calculo`/`integral`/`paridade` contra a classe
  de causa e a coorte, e o nome da causa contra a fundamentação redigida. Essa
  correspondência estrutural — a mesma verificação, repetida quarenta vezes —
  é o que a matriz demonstra por requisito, na seção 5, em vez de exigir uma
  leitura idêntica em cada arquivo;
- os **achados** — as acusações datadas que a auditoria registra — que nomeiam as
  regras do ciclo, para conferir se cada um recebeu disposição escrita;
- os **artefatos derivados** que o repositório publica, para conferir se
  correspondem ao que as fontes gravam.

A verificação não decide questão jurídica nova. Onde a conformidade dependeu de
juízo sobre a lei já fixado pela matriz do ciclo, o método cotejou a regra
contra essa matriz já decidida; não a rederivou. A correspondência estrutural
entre regra e requisito foi verificada por agente, de forma reproduzível — é
verificação programática no sentido que a matriz define, não substituto da
verificação não programática que cada requisito de mérito exige no caso
concreto, nem da revisão que a coordenação faz sobre as próprias decisões
registradas na matriz.

## 5. Síntese executiva

| resultado     | condições                |
| ------------- | ------------------------ |
| cumpridas     | 1, 2, 4, 6, 7, 8, 10, 11 |
| não cumpridas | 3, 5, 9                  |

As três condições não cumpridas decorrem de uma única linha da matriz de
derivação e verificação:

- **C1-R24** — o inciso XVI do § 8º do art. 30 restringe surdez permanente e
  anomalia da fala ao caso de magistério. A restrição já integra o campo de
  seleção das quatro regras correspondentes (`predicados.exercicio_magisterio`,
  sufixo `magisterio` no nome, item próprio de verificação não programática
  com responsável definido), mas o marco temporal da aferição — se o vínculo
  deve existir no acometimento, na instrução do requerimento, na concessão do
  benefício, ou em outro momento — não está fixado em nenhuma fonte
  consultada, e fixá-lo sem fundamento seria decisão jurídica nova. Permanece
  pendente de decisão fundamentada da coordenação (issue #121).

**C1-R32 deixou de ser pendência de auditoria nesta revisão.** A fórmula
jurídica das duas regras de causa comum está decomposta e documentada
(`forma-calculo-media-proporcional-dias-lce1100`): média do art. 24
proporcionalizada pelo art. 26 — derivação concluída, sem pendência. O
rótulo `Proporcionalidade Dias` que as regras projetam, porém, é o mesmo
rótulo que o catálogo legado grava para outras fórmulas de causa comum
(LCE 432, art. 6º-A/EC 70), sem confirmação de que o Sisprev o identifica
sem ambiguidade material perante elas. Essa é uma questão diferente da
derivação: RFC 0004 (round 9) separa a **derivação jurídica concluída**
(`estado_proposta: deployable`, que as duas regras têm) da **confirmação de
implantação** (`estado_implantacao: pendente_mapeamento_sisprev`, que
falta). A pendência de implantação não bloqueia `deployable` nem a
condição 9 — bloqueia especificamente a troca da fonte operacional de
exportação: por exigir todos os destinos do grupo com implantação
confirmada (RFC 0004 §1.4/§1.5, `okf/spec/conjunto.md`), os dois grupos de
substituição do Bloco C permanecem `estado_grupo: inativo`, e as quatro
regras legadas continuam sendo a fonte operacional enquanto isso não se
resolve (issue #122) — sem que isso impeça declarar concluída a derivação
desta hipótese.

Nenhuma das demais trinta e seis regras do Bloco C tem pendência material
aberta: a matriz cobre os setenta requisitos derivados dessas regras — fonte,
regras alcançadas, representação, modo de verificação, responsável e
evidência — e o que resta, fora de C1-R24, é constatação no caso
concreto (junta médica, instrução previdenciária, gestão de pessoas) ou
confirmação de implantação (C1-R32), nenhuma das duas defeito de cadastro.

O documento do ciclo registra o estado "auditoria em fechamento — não
encerrada", com os campos de data e commit de fechamento em branco.

## 6. Resultado por condição

| #   | condição                                                           | resultado                                 |
| --- | ------------------------------------------------------------------ | ----------------------------------------- |
| 01  | nenhuma regra sabidamente errada permanece ativa                   | cumprida                                  |
| 02  | toda regra desativada com substituta ou registro fundamentado      | cumprida                                  |
| 03  | combinações relevantes cobertas por regras ativas                  | **não cumprida** (C1-R24)                 |
| 04  | lacuna preexistente preenchida por regra com identificador próprio | cumprida                                  |
| 05  | ausência de lacunas de cobertura                                   | **não cumprida** (C1-R24)                 |
| 06  | ausência de sobreposição não intencional                           | cumprida por verificação não programática |
| 07  | sobreposição intencional justificada                               | cumprida                                  |
| 08  | mapa de substituição completo                                      | cumprida                                  |
| 09  | ausência de pendência que afete a cobertura material               | **não cumprida** (C1-R24)                 |
| 10  | cenários demonstram a seleção esperada                             | cumprida por verificação não programática |
| 11  | artefatos derivados e demais controles íntegros                    | cumprida                                  |

As condições 3, 5 e 9 não se cumprem porque o marco temporal do requisito de
magistério carece de decisão fundamentada (C1-R24), afetando as quatro
regras do inciso XVI. Isso não impede a exportação do restante do Bloco C
por si só — a seleção de origem única do exportador opera por grupo inteiro
(RFC 0004 §1.5), e os dois grupos do Bloco C incluem essas quatro regras —,
mas mantém aberta uma pendência material que a condição 9 não tolera:
enquanto ela não se resolve, os grupos permanecem `estado_grupo: inativo` e
as quatro origens legadas continuam sendo a fonte operacional.

A condição 9 — ausência de pendência que afete a cobertura material — é
demonstrada pela matriz de derivação e verificação, não por uma leitura
idêntica de cada uma das quarenta regras: toda linha da matriz com status
`coberto` está verificada, e as linhas `pendente` ou `dependência externa`
estão identificadas, classificadas e vinculadas às regras que alcançam. É
esse levantamento, e a decisão da coordenação sobre C1-R24, que zeram a
condição — não quarenta atos de leitura repetidos.

Evidência das condições cumpridas:

- a cadeia de composições resolve sem grupo declarado duas vezes;
- todas as quarenta regras propostas existem e sua correspondência
  estrutural com a matriz de derivação e verificação foi conferida
  programaticamente, requisito a requisito, com evidência registrada no
  corpo de cada regra e detalhada na matriz;
- cada uma das quatro regras substituídas dispõe de todos os achados abertos que
  a nomeiam, inclusive os dois classificados como bloqueantes;
- nenhuma regra do catálogo pertence a dois ciclos, e nenhuma ficou sem ciclo
  responsável;
- os artefatos derivados que o processo de geração cobre correspondem ao que as
  fontes gravam.

Sobre a condição 10: os dezesseis cenários representativos são o artefato que a
especificação exige, e a sua verificação é não programática, como a da
condição 6. Foram lidos contra as fronteiras temporais e a regra de
precedência entre blocos, sem contradição identificada. A ausência de vínculo
automático entre cenário e regra selecionada é oportunidade de
aperfeiçoamento, não descumprimento.

## 7. Achados e providências

Os achados A1, A3-bis, A10 e A11 foram corrigidos nas fontes. Os achados A2, A4,
A5 e A6 são registros sem providência exigida. Os achados A7, A8 e A9, relativos
às quarenta regras propostas, estão hoje refletidos na matriz de derivação e
verificação: A7 foi superado pela própria arquitetura da matriz; A8 continua
aberto, nela representado como C1-R24; A9 está resolvido quanto à derivação
jurídica, com uma pendência de implantação separada (C1-R32) que não bloqueia
mais o fechamento do ciclo.

### A7 — Conferência regra a regra substituída pela matriz de derivação e verificação

**Situação: superado.**

Este achado registrava que nenhuma das quarenta regras tinha revisão humana
da coordenação e que a verificação executada por agente, embora útil,
cotejava cada unidade contra a matriz jurídica sem substituir essa revisão.
A causa da pendência não era a ausência de revisão, mas o desenho do próprio
requisito: exigir uma leitura idêntica, regra a regra, para uma
correspondência estrutural que é a mesma nas quarenta unidades. A matriz de
derivação e verificação substitui esse desenho — a correspondência entre
regra e requisito (dispositivo, coorte, projeção de cálculo, nome) é
demonstrada uma vez por requisito, programaticamente, e documentada na seção
5 da matriz; os requisitos que exigem avaliação de mérito no caso concreto
(diagnóstico, vínculo com o magistério, nexo causal) têm caminho de
verificação não programática definido — responsável, evidência, momento —
também na matriz, sem depender de quarenta cópias do mesmo checklist.

**Providência:** revisão da coordenação sobre a própria matriz — as decisões
jurídicas que ela regista, as classificações de pendência e os caminhos de
verificação escolhidos —, não mais sobre cada uma das quarenta regras
isoladamente. Essa revisão é o que falta para a condição 9 se cumprir por
inteiro.

### A8 — Requisito legal do magistério, marco temporal pendente

**Situação: parcialmente corrigido; pendência remanescente registrada como
`C1-R24`. Impede o encerramento das condições 3, 5 e 9.**

O inciso XVI do § 8º do art. 30 restringe surdez permanente e anomalia da
fala ao caso de magistério. As quatro regras correspondentes já têm essa
restrição incorporada ao campo de seleção — `predicados.exercicio_magisterio`,
sufixo `magisterio` no nome, item próprio de verificação não programática com
responsável definido (a unidade de gestão de pessoas, não a junta médica: o
vínculo com o magistério é fato funcional, não clínico).

O que falta é o marco temporal da aferição desse vínculo. O dispositivo diz
apenas "no caso de magistério", sem indicar se ele deve existir no
acometimento da moléstia, na instrução do requerimento, na concessão do
benefício ou em outro momento; fixar um desses marcos sem fundamento na fonte
seria decisão jurídica nova, não instanciação de decisão já tomada. A matriz
registra essa pendência em `C1-R24` e não a antecipa.

**Providência:** decisão fundamentada da coordenação sobre o marco temporal de
aferição do vínculo com o magistério, com a base normativa ou administrativa
que a sustente.

### A9 — Rótulo de cálculo da causa comum: derivação concluída, mapeamento no Sisprev pendente

**Situação: derivação jurídica concluída; `estado_proposta: deployable`;
pendência de implantação registrada como `C1-R32` e `estado_implantacao: pendente_mapeamento_sisprev`. Não impede mais o encerramento da condição 9
(RFC 0004, round 9) — impede apenas a troca da fonte operacional de
exportação dos dois grupos do Bloco C.**

As duas regras de causa comum projetam `tipo_calculo: Proporcionalidade Dias`
para uma fórmula jurídica já decomposta e documentada
(`forma-calculo-media-proporcional-dias-lce1100`: média do art. 24
proporcionalizada pelo art. 26, reajuste disciplinado à parte).

Uma revisão anterior tratou o problema como "fidelidade textual" — o rótulo
não descrever a fórmula por extenso — e, ao corrigir essa leitura, tratou-o
em seguida como uma colisão de enum que bloqueava a derivação. As duas
formulações erravam pelo mesmo motivo: confundiam a **derivação jurídica**
(se a fórmula que a lei exige está determinada) com a **projeção no
Sisprev** (se o valor de domínio fechado que a representa é reconhecido sem
ambiguidade pelo sistema). A primeira está, e sempre esteve, concluída —
não há alternativa a escolher para `tipo_calculo`: `Proporcionalidade Dias`
é o único valor que o Sisprev já grava para esta hipótese. O que não está
confirmado é a segunda: o mesmo rótulo também é gravado, no catálogo
legado, por outras fórmulas de causa comum (LCE 432/2008; art. 6º-A/EC
70/2012, que nem incide sobre uma média) — fato observável no próprio
catálogo — sem que haja confirmação de que o Sisprev as distingue.

RFC 0004 (round 9) registra essa separação: `estado_proposta: deployable`
passa a afirmar apenas a derivação jurídica concluída, e
`estado_implantacao: pendente_mapeamento_sisprev` — campo próprio, em
`okf/spec/regraproposta.md` — passa a carregar a confirmação de
implantação, quando ela precisa ser feita separadamente. As duas regras de
causa comum são `deployable`. A pendência de implantação não bloqueia mais
a condição 9; bloqueia especificamente a troca da fonte operacional de
exportação do grupo a que pertencem — que exige implantação confirmada em
todos os destinos, porque a troca é atômica e as origens legadas de um
grupo cobrem, juntas, mais de uma hipótese (`okf/spec/conjunto.md`).

O mesmo desacoplamento vale no nível do grupo (RFC 0004, round 10):
`decisao_completude` — a decisão jurídica de que os vinte destinos de cada
grupo cobrem exaustivamente as causas do art. 30 — está preenchida nos
dois grupos do Bloco C desde 03/08/2026 e não foi revista
(`ciclo-01-s4-bloco-c.md`). `estado_grupo` deixou de ser um campo decidido
à parte: é computado a partir de `decisao_completude` mais o estado de
implantação dos destinos, e permanece `inativo` só porque a segunda
condição ainda não se cumpre — não porque a primeira esteja em aberto.

**Providência:** confirmação, pelo IPERON/fornecedor, de que
`Proporcionalidade Dias` identifica esta fórmula sem ambiguidade perante as
demais que compartilham o rótulo, ou implantação de um mecanismo que a
distinga (issue #122, #124). Não é mais providência que a auditoria deva
resolver para encerrar o ciclo quanto a esta hipótese.

### A1 — Rótulo do ciclo mais amplo que o seu objeto

**Situação: corrigido.**

O ciclo denominava-se "Incapacidade e invalidez — continuidade histórica" e seu
objetivo referia-se a "todas as hipóteses de invalidez e incapacidade
permanente", enquanto as regras de que ele é responsável são apenas as quatro do
regime em vigor. As demais constavam como referência, pertencentes ao Ciclo 9 —
isto é, a delimitação já estava correta no dado, e apenas o rótulo a contradizia.
Nome, título e objetivo passaram a expressar o objeto efetivo.

### A2 — Ausência de estado e data de encerramento no registro do ciclo

**Situação: registrado, sem providência exigida nesta revisão.**

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
ainda que a substituição não esteja efetiva pela inativação dos grupos
(C1-R32); nas janelas históricas, porque elas estão fora do escopo e da
responsabilidade deste ciclo.

### A3-bis — Especificação apontava ciclo sucessor incorreto

**Situação: corrigido.**

A especificação de ciclos afirmava que as hipóteses históricas seriam promovidas
pelo Ciclo 2. O Ciclo 2 trata de pensão por morte e benefícios derivados, e as
sete regras pertencem ao Ciclo 9. A passagem passou a nomear o Ciclo 9.

### A4 — Verificação dos cenários é não programática

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

**Situação: corrigido; os itens residuais estão hoje em C1-R24 e C1-R32.**

O documento da sessão que propôs a substituição registrava, no cabeçalho
estruturado, vinte destinos por coorte, enquanto o texto, redigido antes,
ainda descrevia oito unidades e grupos inativos. O texto passou a
declarar-se registro histórico daquela sessão, com regra de precedência
explícita em favor do frontmatter — que, hoje, também reflete
`estado_grupo: inativo` para os dois grupos do Bloco C, tornando o corpo
histórico novamente descritivo do estado corrente nesse ponto específico.

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
  fundamentação invocada seja a correta e que a matriz jurídica esgote as
  hipóteses da lei são conclusões da coordenação da auditoria, fixadas nas
  sessões que produziram a matriz do ciclo (T1 a T9 de `ciclo-01.md`) e não
  rederivadas aqui.

- A correspondência estrutural entre cada uma das quarenta regras e os
  requisitos da matriz de derivação e verificação foi conferida por agente,
  de forma reproduzível — é verificação programática, no sentido que a
  matriz define. Não substitui a verificação não programática que cada
  requisito de mérito exige no caso concreto, nem a revisão da coordenação
  sobre as decisões que a própria matriz registra.

- As condições 6 e 10 dependem de verificação não programática e são
  reportadas como tais. A ausência de contradição identificada não equivale a
  demonstração automática.

- Fidelidade parcial de uma projeção de cálculo
  (`projecao_sisprev.fidelidade: parcial`) não é, por si, impeditiva de
  `deployable` — é a condição da maioria das formas de cálculo do catálogo,
  porque o enum legado do Sisprev é mais pobre que a fórmula jurídica. O caso
  da causa comum (`C1-R32`) é exatamente esse: `Proporcionalidade Dias` é o
  único valor que o Sisprev grava para esta hipótese, e o mesmo rótulo
  também é gravado, no catálogo, por outras fórmulas de causa comum. Isso
  não é dúvida sobre a fórmula — que está integralmente derivada — mas sobre
  se o rótulo a identifica sem ambiguidade perante as demais. RFC 0004
  (round 9) separa essa questão da derivação jurídica: `estado_implantacao: pendente_mapeamento_sisprev`, campo próprio, carrega a pendência, sem
  reabrir `deployable`.

- Permanecem abertas, como dependência operacional externa e não como
  pendência da auditoria, três linhas da matriz que dependem de resposta do
  IPERON e do fornecedor do Sisprev (issue #124):

  - `C1-R73` — como o sistema captura e classifica a causa da incapacidade do
    requerente;
  - `C1-R74` — se o rótulo de cálculo projetado para cada regra identifica
    univocamente a fórmula jurídica que a regra descreve — para a causa
    comum, essa mesma confirmação também resolveria a pendência de
    implantação de `C1-R32`;
  - `C1-R75` — o protocolo institucional de reconhecimento do nexo de
    moléstia profissional, que nenhum dos dois regimes estaduais define (RFC
    0004, P-6). As duas regras de moléstia profissional permanecem
    `deployable` porque já têm caminho de verificação definido para o nexo em
    geral; a lacuna é do protocolo específico, registrada como dependência
    externa, não como defeito das regras — ver matriz, seção 7.

  Fica também registrado, como risco residual que não impede a cobertura
  (`C1-R61`), que a opção pelo regime de previdência complementar do § 16 do
  art. 40 da Constituição Federal não tem coluna própria no cadastro: é
  requisito da fundamentação, conferido no processo administrativo.

- A verificação retrata o estado do repositório na data indicada.

## 9. Conclusão

A análise jurídica do Ciclo 1 está avançada e a sua estrutura se sustenta: a
matriz de hipóteses, o mapa de substituição, a precedência entre regimes e os
cenários representativos foram entregues e resistem à conferência. A matriz
de derivação e verificação organiza essa estrutura numa cadeia auditável —
fonte normativa → requisito → requisito derivado → regra → representação →
forma de verificação → responsável → evidência — e substitui, para o Bloco C,
a exigência de uma leitura idêntica repetida quarenta vezes.

O ciclo, porém, **não está encerrado**. Três das onze condições cumulativas
não se cumprem, por uma única causa pendente de decisão: o marco temporal do
requisito de magistério (`C1-R24`, issue #121), afetando as quatro regras do
inciso XVI. `C1-R32` deixou de ser uma dessas causas nesta revisão — a
derivação da causa comum está concluída, e a pendência restante
(`estado_implantacao: pendente_mapeamento_sisprev`, confirmação de que
`Proporcionalidade Dias` identifica a fórmula sem ambiguidade, issue #122)
é de implantação, não de auditoria: bloqueia a troca da fonte operacional
dos dois grupos de substituição do Bloco C, que permanecem `inativo`, e as
quatro regras legadas continuam sendo a fonte operacional — mas não bloqueia
o fechamento do ciclo quanto a essa derivação. Nenhuma das quarenta regras
propostas tem, além de C1-R24, pendência material que a matriz não tenha
identificado, classificado e vinculado a um responsável e a uma evidência
exigida.

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

**Estado de implantação (`estado_implantacao`)** — campo, distinto de
`estado_proposta`, que afirma se o valor de domínio fechado que uma regra
projeta para o Sisprev (`projecao.tipo_calculo`, por exemplo) identifica a
fórmula sem ambiguidade material (`confirmada`) ou ainda depende de
confirmação do IPERON/fornecedor (`pendente_mapeamento_sisprev`). Separa a
derivação jurídica, que `estado_proposta: deployable` já afirma sozinho, da
confirmação de que o sistema reconhece essa derivação sem ambiguidade —
introduzido em RFC 0004, round 9, a partir do achado deste ciclo sobre o
rótulo `Proporcionalidade Dias`.

**Grupo de substituição** — unidade de decisão que liga regras cadastradas a
regras propostas. Ativa e reverte por inteiro — todos os destinos precisam
estar `deployable` para o grupo ativar juridicamente, e adicionalmente com
`estado_implantacao: confirmada` para a ativação trocar a fonte operacional
de exportação (RFC 0004 §1.4, `okf/spec/conjunto.md`) —, porque aprovar
metade deixaria hipótese sem representação ou representada duas vezes.

**Matriz de derivação e verificação** — documento central do ciclo que lista
os requisitos juridicamente e operacionalmente relevantes, de onde cada um
deriva, quais regras o materializam, como se representa no catálogo, e qual é
o modo de verificação — programático, não programático, ou misto —, com
responsável e evidência definidos por requisito. Substitui, para requisitos
que se repetem em muitas regras, a exigência de uma leitura idêntica
registrada em cada arquivo. Não cria tipo OKF, schema, parser ou gate novo:
é markdown de auditoria, como o próprio relatório de conformidade.

**Preview** — estado de uma regra proposta cujo modelo jurídico está
registrado, mas que ainda admite pendência em campo operacional. Não entra no
export para o sistema.

**Pronta para implantação (`deployable`)** — estado que declara a **derivação
jurídica** da regra proposta concluída: a fórmula que a lei exige está
determinada e representada. Não afirma, por si só, que o valor de domínio
fechado projetado para o Sisprev já é reconhecido pelo sistema sem
ambiguidade — essa afirmação, quando precisa ser feita separadamente, é
`estado_implantacao`. Uma regra pode permanecer `deployable` mesmo com
requisitos de verificação não programática ainda por constatar no caso
concreto, ou com `estado_implantacao: pendente_mapeamento_sisprev`, desde
que o caminho de verificação — responsável, evidência, momento — esteja
definido e representado no nome, na fundamentação ou no protocolo de
verificação da regra: isso é requisito de instrução do benefício ou de
implantação técnica, não defeito da derivação.

**Regra proposta** — regra corrigida, redigida pela auditoria em espaço de
identificação próprio, fora da numeração do catálogo recebido, porque corrigir
frequentemente altera o número de regras.

**Verificação programática / não programática** — distinção pela natureza da
avaliação, não por quem a executa. Programática é a correspondência
determinística entre campo estruturado e requisito codificado — reproduzível
por script ou por agente seguindo o mesmo procedimento. Não programática é a
avaliação substantiva de fato, documento ou texto jurídico que não se reduz a
cotejo de colunas — pode ser feita por pessoa, por agente, ou por pessoa
assistida por agente; o que a define é a natureza do juízo, não o executor.

## 11. Rastreabilidade

| item                                                                      | referência                                                                                                                               |
| ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| ciclo auditado                                                            | `okf/regras-sisprev/ciclos/ciclo-01.md`                                                                                                  |
| matriz de derivação e verificação                                         | `docs/analysis/matriz-derivacao-verificacao-ciclo-01.md`                                                                                 |
| composição proposta                                                       | `okf/conjuntos/ciclo-01-s6-fechamento.md`                                                                                                |
| grupos de substituição do Bloco C                                         | `okf/conjuntos/ciclo-01-s4-bloco-c.md`                                                                                                   |
| critério de encerramento                                                  | `okf/spec/ciclo.md`                                                                                                                      |
| fail-closed de `deployable`                                               | `docs/rfc/0004-schema-enriquecido-e-compilador-para-o-sisprev.md`, §5.3, §1.4                                                            |
| regras propostas                                                          | `okf/regras-propostas/regras/incapacidade-lce1100-*.md`                                                                                  |
| regras substituídas                                                       | `regra-0019` a `regra-0022`                                                                                                              |
| composição corrente registrada pela PR #102                               | `bea6f20c1c6b8b38f7da6db8f24623033a874902`                                                                                               |
| planilha de homologação vigente                                           | `data/regras-propostas.csv`                                                                                                              |
| marco temporal do requisito de magistério (`C1-R24`)                      | [issue #121](https://github.com/franklinbaldo/sisprev/issues/121)                                                                        |
| mapeamento pendente de `tipo_calculo` da causa comum (`C1-R32`)           | `okf/formas-calculo/forma-calculo-media-proporcional-dias-lce1100.md`, [issue #122](https://github.com/franklinbaldo/sisprev/issues/122) |
| matriz de derivação e verificação (substitui a conferência regra a regra) | [issue #123](https://github.com/franklinbaldo/sisprev/issues/123)                                                                        |
| dependências externas registradas (`C1-R73`, `C1-R74`, `C1-R75`)          | [issue #124](https://github.com/franklinbaldo/sisprev/issues/124)                                                                        |
| confirmações do fornecedor                                                | `docs/analysis/confirmacoes-do-fornecedor-do-sisprev.md`                                                                                 |
