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

**Conclusão prática:** o Ciclo 1 **pode ser declarado encerrado quanto à
auditoria**. A matriz de derivação e verificação cobre os setenta
requisitos derivados que as quarenta regras do Bloco C instanciam, com
fonte, regras alcançadas, representação, modo de verificação, responsável e
evidência para cada um. A única linha que permanecia pendente de decisão
da coordenação — **C1-R24**, o marco temporal do requisito de magistério do
inciso XVI — foi reavaliada e encerrada em 2026-08-05 (issue #121): o
dispositivo não institui marco temporal autônomo para a aferição desse
vínculo, e a exigência real (a condição funcional do magistério) já estava
corretamente modelada no campo de seleção das quatro regras. **C1-R32** — a
identificação unívoca, no Sisprev, da fórmula de causa comum da LCE 1.100 —
não é pendência de auditoria: a derivação está concluída e as duas regras
correspondentes são `estado_auditoria: concluida`; desde a emenda do round 12
(2026-08-05), o que resta é `estado_implantacao: confirmada_com_ressalva`
— `regra-0020` e `regra-0021` já gravam, em produção, a mesma combinação
para as mesmas hipóteses, o que sustenta a presunção necessária para a
carga — e não bloqueia a entrada das duas origens de causa comum
(`regra-0020`, `regra-0021`) na carga de homologação: as quarenta regras
do Bloco C entram, todas
(`okf/spec/regraproposta.md`, "Atomicidade é derivada, não declarada"),
levando as duas de causa comum a ressalva sobre a base do art. 26, a
resolver em homologação prática antes da ativação em produção — sem
obstar o fechamento do ciclo quanto a essa derivação (issue #122). Três
dependências externas
adicionais — captura da causa pelo Sisprev, confirmação geral de
`tipo_calculo` e protocolo institucional de nexo de moléstia profissional
(issue #124) — permanecem registradas sem bloquear a cobertura das regras a
que se referem. Nenhuma das quarenta regras do Bloco C tem pendência
material aberta.

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
a decisão de completude de cada coorte registra que essa granularidade foi a
escolhida, e o catálogo poderia, em tese, consolidar as quinze moléstias sem
a restrição do inciso XVI numa única linha, mantendo a cobertura. A
auditoria não afirma que a lei exigia quarenta linhas; afirma que a lei
distingue quatro classes de causa, e que a granularidade adicional dentro
da classe "doença catalogada" foi escolha documentada do IPERON, registrada
como tal na decisão de completude de cada coorte — RFC 0004 §0 é expressa
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
  que ela deriva, para conferir que nenhuma origem legada pertence a mais de
  um componente de implantação e que as regras substituídas efetivamente
  saem da composição vigente;
- os **componentes de implantação** derivados do grafo origem↔destino, para
  conferir origem, destinos, estado de implantação e a existência da decisão
  de completude com autor, data, justificativa e fonte;
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

| resultado     | condições                         |
| ------------- | --------------------------------- |
| cumpridas     | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 |
| não cumpridas | nenhuma                           |

**C1-R24 foi reavaliado e encerrado em 2026-08-05, e deixou de ser
pendência das condições 3, 5 e 9.** O inciso XVI do § 8º do art. 30
restringe surdez permanente e anomalia da fala ao caso de magistério. A
restrição já integrava o campo de seleção das quatro regras correspondentes
(`predicados.exercicio_magisterio`, sufixo `magisterio` no nome, item
próprio de verificação não programática com responsável definido) desde a
issue #121. O que estava errado não era a modelagem, mas a moldura da
pendência: supor que o dispositivo exigisse um marco temporal autônomo —
se o vínculo deve existir no acometimento, na instrução do requerimento, na
concessão do benefício, ou em outro momento — e que essa ausência fosse
lacuna a suprir por decisão da coordenação. O art. 30, § 8º, inciso XVI,
diz apenas "no caso de magistério, surdez permanente e anomalia da fala",
sem qualificador temporal algum — ao contrário do caput do mesmo § 8º, que
fixa expressamente o marco do acometimento em relação à filiação
("aplicável ao segurado acometido da doença ou afecção após a sua
filiação"). Fixar um marco que o texto não impõe seria decisão jurídica
nova, não leitura da norma. A exigência é apenas a condição funcional do
magistério, verificável no caso concreto pela mesma via que já verifica as
demais condições não programáticas do Bloco C — histórico funcional, atos
de nomeação, exercício e lotação, certidões e demais documentos da
instrução —, sem que nenhuma delas dependa de um marco temporal fixado por
lei. `C1-R24` está encerrado (issue #121; decisão datada em cada uma das
quatro regras do inciso XVI, `decisoes`, 2026-08-05).

**C1-R32 deixou de ser pendência de auditoria nesta revisão.** A fórmula
jurídica das duas regras de causa comum está decomposta e documentada: a da
coorte a partir de 2004 em `tipo-calculo-media-proporcional-dias-lce1100`
(média do art. 24 proporcionalizada pelo art. 26); a da coorte até
31/12/2003, por revisão jurídica adicional da coordenação de 2026-08-05, em
`tipo-calculo-remuneracao-cargo-proporcional-dias-lce1100` (remuneração do
cargo do art. 25, não a média do art. 24, proporcionalizada pelo art. 26 —
ver `decisoes` da regra `incapacidade-lce1100-ate-2003-causa-comum` para a
tensão registrada com a literalidade do art. 26, § 1º) — derivação
concluída em ambas, sem pendência. O
rótulo `Proporcionalidade Dias` que as regras projetam, porém, é o mesmo
rótulo que o catálogo legado grava para outras fórmulas de causa comum —
`tipo-calculo-media-proporcional-dias-lce432`,
`tipo-calculo-media-80-proporcional-dias-lce432` e
`tipo-calculo-remuneracao-cargo-ec70-proporcional-dias` —, sem confirmação
de que o Sisprev o identifica sem ambiguidade material perante elas — mas
`regra-0020` e `regra-0021` já gravam, em produção, essa mesma combinação
para as mesmas hipóteses, o que é evidência concreta de que o sistema já
executa algum mecanismo para elas. Essa é uma questão diferente da
derivação: RFC 0004 (round 9) separa a **derivação jurídica concluída**
(`estado_auditoria: concluida`, que as duas regras têm) da **confirmação de
implantação**. Desde a emenda do round 12 (2026-08-05), a pendência
restante — se a execução aplica a base composta do art. 26 (média do
art. 24, limitada pelo § 10, então proporcionalizada) — é
`estado_implantacao: confirmada_com_ressalva`, e não bloqueia a entrada
dos componentes de implantação do Bloco C em `data/regras-propostas.csv`:
as quarenta regras propostas entram, todas, substituindo `regra-0019`,
`regra-0020`, `regra-0021` e `regra-0022` por inteiro — as duas de causa
comum levando a ressalva sobre a base do art. 26, a resolver em
homologação prática antes da ativação em produção (issue #122) — sem que
isso impeça declarar concluída a derivação desta hipótese.

Nenhuma das quarenta regras do Bloco C tem pendência material aberta: a
matriz cobre os setenta requisitos derivados dessas regras — fonte,
regras alcançadas, representação, modo de verificação, responsável e
evidência — e o que resta é constatação no caso concreto (junta médica,
instrução previdenciária, gestão de pessoas, inclusive o vínculo com o
magistério de C1-R24) ou confirmação de implantação (C1-R32), nenhuma das
duas defeito de cadastro.

Com `C1-R24` encerrado, nenhum requisito da matriz permanece classificado
como pendência jurídica da coordenação (`docs/analysis/matriz-derivacao-verificacao-ciclo-01.md`,
§7). O documento do ciclo passa a registrar a auditoria como encerrada; a
ativação institucional continua distinta e posterior, a cargo do IPERON.

## 6. Resultado por condição

| #   | condição                                                           | resultado                                 |
| --- | ------------------------------------------------------------------ | ----------------------------------------- |
| 01  | nenhuma regra sabidamente errada permanece ativa                   | cumprida                                  |
| 02  | toda regra desativada com substituta ou registro fundamentado      | cumprida                                  |
| 03  | combinações relevantes cobertas por regras ativas                  | cumprida (C1-R24 encerrado)               |
| 04  | lacuna preexistente preenchida por regra com identificador próprio | cumprida                                  |
| 05  | ausência de lacunas de cobertura                                   | cumprida (C1-R24 encerrado)               |
| 06  | ausência de sobreposição não intencional                           | cumprida por verificação não programática |
| 07  | sobreposição intencional justificada                               | cumprida                                  |
| 08  | mapa de substituição completo                                      | cumprida                                  |
| 09  | ausência de pendência que afete a cobertura material               | cumprida (C1-R24 encerrado)               |
| 10  | cenários demonstram a seleção esperada                             | cumprida por verificação não programática |
| 11  | artefatos derivados e demais controles íntegros                    | cumprida                                  |

As condições 3, 5 e 9 dependiam de uma única pendência: o marco temporal do
requisito de magistério (C1-R24), afetando as quatro regras do inciso XVI.
Reavaliada em 2026-08-05, a pendência não correspondia a uma exigência real
da norma — o dispositivo não institui marco temporal autônomo algum, e
supor que faltava fixá-lo era decisão jurídica nova não demonstrada, não
leitura do texto. Encerrado C1-R24, as três condições se cumprem: os dois
componentes de implantação do Bloco C têm a decisão de completude
registrada, e ambos já estão em `data/regras-propostas.csv` — desde a
emenda do round 12 (2026-08-05), a única pendência remanescente,
`estado_implantacao: confirmada_com_ressalva` (C1-R32), não retira as duas
unidades de causa comum da carga, apenas registra a ressalva de
homologação que precisa ser resolvida antes da ativação em produção. É
dependência de homologação, não de auditoria (RFC 0004, round 9/12), e não
afeta esta condição.

A condição 9 — ausência de pendência que afete a cobertura material — é
demonstrada pela matriz de derivação e verificação, não por uma leitura
idêntica de cada uma das quarenta regras: toda linha da matriz com status
`coberto` está verificada, e as linhas `dependência externa` ou
`dependência de implantação` estão identificadas, classificadas e
vinculadas às regras que alcançam, sem obstar a condição, como a spec
admite. Nenhuma linha da matriz permanece classificada como pendência
jurídica da coordenação depois do encerramento de C1-R24 — é esse
levantamento, e a decisão da coordenação sobre C1-R24, que zeram a
condição, não quarenta atos de leitura repetidos.

Evidência das condições cumpridas:

- a cadeia de composições resolve sem origem legada pertencendo a mais de
  um componente de implantação — a construção por componentes conexos
  (`okf/spec/regraproposta.md`, "Atomicidade é derivada, não declarada")
  garante isso por definição;
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
verificação, e todos encerrados: A7 foi superado pela própria arquitetura da
matriz, e a revisão de mérito que ele exigia da coordenação se completou com
as decisões sobre C1-R24 e C1-R32, as únicas linhas da matriz que a
demandavam; A8 foi encerrado em 2026-08-05, com C1-R24 reavaliado e fechado;
A9 está resolvido quanto à derivação jurídica, com uma pendência de
implantação separada (C1-R32) que não bloqueia o fechamento do ciclo.

### A7 — Conferência regra a regra substituída pela matriz de derivação e verificação

**Situação: encerrado (2026-08-05).**

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

**Providência cumprida.** A revisão de mérito da coordenação sobre a
própria matriz — as decisões jurídicas que ela regista, as classificações
de pendência e os caminhos de verificação escolhidos — tinha, como únicas
linhas exigindo decisão substantiva não programática de mérito jurídico
(classificação "pendência jurídica da coordenação" em `docs/analysis/matriz-derivacao-verificacao-ciclo-01.md`,
§7), `C1-R24` e `C1-R32`. Ambas foram decididas pela coordenação: `C1-R32`
em 2026-08-03 (`decisao_completude` nos dois grupos do Bloco C) e `C1-R24`
em 2026-08-05 (abaixo). As demais linhas da matriz são verificação
programática já demonstrada ou dependência externa/de implantação que a
spec (`okf/spec/ciclo.md`) admite manter registrada sem obstar o
encerramento. Não resta revisão de mérito pendente sobre a matriz.

### A8 — Requisito legal do magistério, marco temporal pendente

**Situação: encerrado (2026-08-05).**

O inciso XVI do § 8º do art. 30 restringe surdez permanente e anomalia da
fala ao caso de magistério. As quatro regras correspondentes já tinham essa
restrição incorporada ao campo de seleção desde a issue #121 —
`predicados.exercicio_magisterio`, sufixo `magisterio` no nome, item
próprio de verificação não programática com responsável definido (a
unidade de gestão de pessoas, não a junta médica: o vínculo com o
magistério é fato funcional, não clínico).

O que faltava não era o marco temporal da aferição desse vínculo — era a
premissa de que a lei exigisse um. O dispositivo diz apenas "no caso de
magistério", sem qualificador temporal, ao contrário do caput do mesmo §
8º, que fixa expressamente o marco do acometimento em relação à filiação
("aplicável ao segurado acometido da doença ou afecção após a sua
filiação"). Se o legislador quisesse condicionar o inciso XVI a um instante
determinado, o próprio parágrafo já mostra como o teria feito — e não fez.
Fixar um marco (acometimento, instrução, concessão) que o texto não impõe
seria decisão jurídica nova, não instanciação de decisão já tomada. A
exigência é apenas a condição funcional do magistério, a constatar no caso
concreto pela mesma via que já verifica as demais condições não
programáticas do Bloco C, sem marco temporal legal para nenhuma delas.

**Providência cumprida.** `C1-R24` foi reavaliado e encerrado; não há
decisão jurídica nova a fixar. A decisão está registrada, com data e
fundamentação, em cada uma das quatro regras do inciso XVI (`decisoes`,
2026-08-05) e detalhada em
`docs/analysis/matriz-derivacao-verificacao-ciclo-01.md` (§7).

### A9 — Rótulo de cálculo da causa comum: derivação concluída, ressalva de homologação registrada

**Situação: derivação jurídica concluída; `estado_auditoria: concluida`;
ressalva de homologação registrada como `C1-R32` e
`estado_implantacao: confirmada_com_ressalva` (RFC 0004, round 12,
2026-08-05). Não impede o encerramento da condição 9 (RFC 0004, round 9) nem
a entrada das duas unidades na carga de homologação — impede apenas a
ativação em produção, até a confirmação prática da base de cálculo.**

As duas regras de causa comum projetam `tipo_calculo: Proporcionalidade Dias`
para uma fórmula jurídica já decomposta e documentada — coorte a partir de
2004 em `tipo-calculo-media-proporcional-dias-lce1100` (média do art. 24
proporcionalizada pelo art. 26); coorte até 31/12/2003, desde a revisão de
2026-08-05, em `tipo-calculo-remuneracao-cargo-proporcional-dias-lce1100`
(remuneração do cargo do art. 25 proporcionalizada pelo art. 26) — reajuste
disciplinado à parte em ambas.

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
legado, pela origem legada de `tipo-calculo-media-proporcional-dias-lce432`,
`tipo-calculo-media-80-proporcional-dias-lce432` e
`tipo-calculo-remuneracao-cargo-ec70-proporcional-dias` — a última nem
incide sobre uma média — fato observável no próprio catálogo — sem que
haja confirmação de que o Sisprev as distingue.

RFC 0004 (round 9) registra essa separação: `estado_auditoria: concluida`
passa a afirmar apenas a derivação jurídica concluída, e
`estado_implantacao` — campo próprio, em `okf/spec/regraproposta.md` —
passa a carregar a confirmação de implantação, quando ela precisa ser
feita separadamente. RFC 0004 (round 12, 2026-08-05) refina essa
confirmação: `regra-0020` e `regra-0021` já gravam, em produção,
`integral: N` e `tipo_calculo: Proporcionalidade Dias` para as mesmas
hipóteses de causa comum, evidência concreta de que o Sisprev já executa
algum mecanismo para elas — a ambiguidade de catálogo é sobre o
vocabulário em geral, não sobre se estas duas hipóteses têm representação
no sistema. As duas regras de causa comum passam a
`estado_implantacao: confirmada_com_ressalva`, com `ressalva_homologacao`
registrando o que resta: confirmar, em homologação prática, se a execução
aplica a base composta do art. 26 (média do art. 24, limitada pelo § 10,
então proporcionalizada) e não uma proporcionalidade nua. A ressalva não
bloqueia a condição 9 nem a entrada do componente de implantação a que
pertencem em `data/regras-propostas.csv` — bloqueia apenas a ativação em
produção, até a confirmação.

O mesmo desacoplamento vale no nível do componente (RFC 0004, round 11):
a decisão jurídica de que os vinte destinos de cada componente cobrem
exaustivamente as causas do art. 30 está registrada e não foi revista
desde 03/08/2026 (`okf/regras-sisprev/ciclos/ciclo-01.md`, T7). A entrada
na carga de homologação depende dessa decisão mais o estado de
implantação dos destinos; desde o round 12, as duas unidades de causa
comum cumprem as duas condições — `confirmada_com_ressalva` conta como
pronta para a carga — e entram nela como as demais trinta e oito.

**Providência:** confirmação, em homologação prática, de que
`Proporcionalidade Dias` executa a base composta do art. 26 para esta
hipótese — não mais se o rótulo identifica a hipótese sem ambiguidade
perante as demais que o compartilham no catálogo legado, questão já
respondida pela própria `regra-0020`/`regra-0021` em produção (issue #122,
#124). Não é providência que a auditoria deva resolver para encerrar o
ciclo quanto a esta hipótese, nem para admiti-la na carga de homologação —
é condição da ativação em produção.

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

O documento da sessão que propôs a substituição — um `Conjunto`, retirado
como entidade canônica em RFC 0004, round 11 — registrava, no cabeçalho
estruturado, vinte destinos por coorte, enquanto o texto, redigido antes,
ainda descrevia oito unidades e grupos inativos. O texto passou a
declarar-se registro histórico daquela sessão, com regra de precedência
explícita em favor do frontmatter. O conteúdo irredutível desse documento
— a matriz jurídica do Bloco C e a decisão de completude — foi migrado
para `okf/regras-sisprev/ciclos/ciclo-01.md` antes da retirada; hoje é lá,
e não mais num `Conjunto`, que se confere se os dois componentes de
implantação do Bloco C seguem fora de `data/regras-propostas.csv`.

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
  `estado_auditoria: concluida` — é a condição da maioria das formas de
  cálculo do catálogo, porque o enum legado do Sisprev é mais pobre que a
  fórmula jurídica. O caso da causa comum (`C1-R32`) é exatamente esse:
  `Proporcionalidade Dias` é o único valor que o Sisprev grava para esta
  hipótese, e o mesmo rótulo também é gravado, no catálogo, por outras
  fórmulas de causa comum — mas `regra-0020` e `regra-0021` já gravam essa
  mesma combinação, em produção, para estas mesmas hipóteses. Isso não é
  dúvida sobre a fórmula — que está integralmente derivada — nem sobre se o
  sistema já a executa de algum modo, mas sobre um detalhe mais estreito da
  execução (a base do art. 26). RFC 0004 (round 9/12) separa essa questão da
  derivação jurídica: `estado_implantacao: confirmada_com_ressalva`, campo
  próprio, carrega a ressalva sem reabrir `estado_auditoria: concluida` e
  sem bloquear a carga de homologação.

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
    `estado_auditoria: concluida` porque já têm caminho de verificação
    definido para o nexo em geral; a lacuna é do protocolo específico,
    registrada como dependência externa, não como defeito das regras — ver
    matriz, seção 7.

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

**O ciclo está encerrado quanto à auditoria.** As onze condições cumulativas
de `okf/spec/ciclo.md` se cumprem. A última pendência que as impedia — o
marco temporal do requisito de magistério (`C1-R24`, issue #121), afetando
as quatro regras do inciso XVI — foi reavaliada em 2026-08-05: o art. 30, §
8º, inciso XVI, da LCE 1.100/2021 restringe surdez permanente e anomalia da
fala ao caso de magistério sem instituir marco temporal autônomo para a
aferição do vínculo, ao contrário do caput do mesmo parágrafo, que fixa
expressamente o marco do acometimento em relação à filiação. Não havia
lacuna normativa a suprir por decisão da coordenação; havia uma premissa
equivocada de que a lei exigisse um marco que ela não exige. `C1-R32`
também deixou de ser causa de não cumprimento nesta revisão — a derivação
da causa comum está concluída, e a ressalva restante
(`estado_implantacao: confirmada_com_ressalva`, confirmação em homologação
prática de que `Proporcionalidade Dias` aplica a base composta do art. 26,
issue #122) é de homologação, não de auditoria: não bloqueia a entrada de
nenhum dos quarenta destinos do Bloco C em `data/regras-propostas.csv` —
as quarenta regras propostas entram, todas, na carga, substituindo
`regra-0019`, `regra-0020`, `regra-0021` e `regra-0022` por inteiro, com as
duas de causa comum levando a ressalva sobre a base do art. 26 —, e não
bloqueia o fechamento do ciclo quanto a essa derivação. A ressalva
condiciona apenas a ativação em produção. Nenhuma das quarenta regras
propostas tem pendência material que a matriz não tenha identificado,
classificado e vinculado a um responsável e a uma evidência exigida.

A ativação institucional — o IPERON pôr em vigor a composição proposta —
permanece distinta e posterior, e não é condição de encerramento de ciclo
algum (`okf/spec/ciclo.md`).

## 10. Glossário

**Achado** — acusação datada sobre regras nomeadas, com autor e classificação de
severidade. Não corrige nada por si: registra o defeito e permanece no acervo.

**Bloco C** — designação interna das hipóteses de incapacidade permanente sob a
Lei Complementar Estadual nº 1.100/2021, objeto deste ciclo. Os Blocos A e B
designam as janelas históricas, transferidas ao Ciclo 9.

**Ciclo** — lote temático de regras revistas em conjunto, com objeto delimitado e
critério de encerramento escrito.

**Composição** — o conjunto de regras que iria para o sistema se a carga de
implantação corrente fosse ativada. Responde à pergunta "o que iria para o
sistema se isto fosse ativado". Não é mais declarada à parte: é derivada a
cada `derivar.py` em `data/regras-propostas.csv` (relatório de
implantação), a partir do estado de cada `RegraProposta`. O catálogo em
vigor continua sendo o recebido do Instituto.

**Estado de implantação (`estado_implantacao`)** — campo, distinto de
`estado_auditoria`, que afirma se o valor de domínio fechado que uma regra
projeta para o Sisprev (`projecao.tipo_calculo`, por exemplo) identifica a
fórmula sem ambiguidade material (`confirmada`), identifica a hipótese com
evidência operacional concreta mas ainda depende de confirmação prática de
um detalhe da execução (`confirmada_com_ressalva`, com `ressalva_homologacao`
carregando o que falta), ou não tem, sequer, mecanismo do sistema
identificado (`pendente_mapeamento_sisprev`). Separa a derivação jurídica,
que `estado_auditoria: concluida` já afirma sozinho, da confirmação de que
o sistema reconhece essa derivação sem ambiguidade — introduzido em RFC
0004, round 9, a partir do achado deste ciclo sobre o rótulo
`Proporcionalidade Dias`; o terceiro valor veio no round 12, do mesmo
achado, para distinguir a ambiguidade de catálogo (bloqueia a carga) da
ressalva de execução sobre uma hipótese já identificada (entra na carga,
resolve-se antes da ativação em produção).

**Componente de implantação** — o conjunto de `RegraProposta` que precisa
subir junto no Sisprev, porque compartilham origem legada. Não é campo
declarado à parte: é calculado por componentes conexos sobre o grafo de
`origens_legacy` a cada `derivar.py` (RFC 0004, round 11;
`okf/spec/regraproposta.md`, "Atomicidade é derivada, não declarada"). Um
componente só entra em `data/regras-propostas.csv` quando **todos** os seus
membros têm `estado_auditoria: concluida` **e** `estado_implantacao` em
`confirmada` ou `confirmada_com_ressalva`, porque aprovar parte deixaria
hipótese sem representação ou representada duas vezes. Substitui o
`Grupo`/`Conjunto` (`estado_grupo`) que este mecanismo tinha antes do
round 11.

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

**Concluída (`estado_auditoria: concluida`)** — estado que declara a
**derivação jurídica** da regra proposta concluída: a fórmula que a lei
exige está determinada e representada. Renomeado de `deployable` em RFC
0004, round 11. Não afirma, por si só, que o valor de domínio fechado
projetado para o Sisprev já é reconhecido pelo sistema sem ambiguidade —
essa afirmação, quando precisa ser feita separadamente, é
`estado_implantacao`. Uma regra pode permanecer `estado_auditoria: concluida` mesmo com requisitos de verificação não programática ainda por
constatar no caso concreto, ou com `estado_implantacao` em
`confirmada_com_ressalva` ou `pendente_mapeamento_sisprev`, desde que o
caminho de verificação — responsável, evidência, momento — esteja
definido e representado no nome, na fundamentação ou no protocolo de
verificação da regra: isso é requisito de instrução do benefício ou de
homologação técnica, não defeito da derivação.

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

| item                                                                      | referência                                                                                                                                   |
| ------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| ciclo auditado                                                            | `okf/regras-sisprev/ciclos/ciclo-01.md`                                                                                                      |
| matriz de derivação e verificação                                         | `docs/analysis/matriz-derivacao-verificacao-ciclo-01.md`                                                                                     |
| composição proposta                                                       | `okf/regras-sisprev/ciclos/ciclo-01.md`, T9                                                                                                  |
| componentes de implantação do Bloco C (derivados)                         | `okf/spec/regraproposta.md`, "Atomicidade é derivada, não declarada"; decisão de completude em `ciclo-01.md`, T7                             |
| critério de encerramento                                                  | `okf/spec/ciclo.md`                                                                                                                          |
| fail-closed de `estado_auditoria: concluida`                              | `docs/rfc/0004-schema-enriquecido-e-compilador-para-o-sisprev.md`, §5.3, §1.4                                                                |
| regras propostas                                                          | `okf/regras-propostas/regras/incapacidade-lce1100-*.md`                                                                                      |
| regras legadas do Bloco C, estado por origem                              | `okf/regras-sisprev/ciclos/ciclo-01.md`, T4 e "Resultado por regra" (`regra-0019`/`regra-0022` prontas; `regra-0020`/`regra-0021` pendentes) |
| composição corrente registrada pela PR #102                               | `bea6f20c1c6b8b38f7da6db8f24623033a874902`                                                                                                   |
| planilha de homologação vigente                                           | `data/regras-propostas.csv`                                                                                                                  |
| marco temporal do requisito de magistério (`C1-R24`)                      | [issue #121](https://github.com/franklinbaldo/sisprev/issues/121)                                                                            |
| mapeamento pendente de `tipo_calculo` da causa comum (`C1-R32`)           | `okf/tipos-calculo/tipo-calculo-media-proporcional-dias-lce1100.md`, [issue #122](https://github.com/franklinbaldo/sisprev/issues/122)       |
| matriz de derivação e verificação (substitui a conferência regra a regra) | [issue #123](https://github.com/franklinbaldo/sisprev/issues/123)                                                                            |
| dependências externas registradas (`C1-R73`, `C1-R74`, `C1-R75`)          | [issue #124](https://github.com/franklinbaldo/sisprev/issues/124)                                                                            |
| confirmações do fornecedor                                                | `docs/analysis/confirmacoes-do-fornecedor-do-sisprev.md`                                                                                     |
