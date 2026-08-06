---
type: Especificacao
id: ciclo
nome: Ciclo
---

# Ciclo

> **Minuta.** Escrita a partir do contrato que já vigora no
> `site/src/content.config.ts` e da prática do repositório, para que o tipo
> deixe de existir sem documento. O que ela afirma é descrição do que há, não
> decisão nova — onde estiver errada, quem corrige é a coordenação.
>
> **Emenda (RFC 0004, round 11).** `Conjunto` e o "grupo de substituição"
> foram eliminados como entidades canônicas. O ciclo não fecha mais sobre um
> `conjunto` declarado à parte: fecha sobre o estado das suas próprias
> `RegraProposta` (campo `ciclo`, `okf/spec/regraproposta.md`). Cobertura,
> mapa de substituição e atomicidade de implantação passam a ser
> **relatórios derivados**, não documentos com estado próprio.

Um **Ciclo** é um lote temático de regras revistas juntas, e o documento é a
fonte única das decisões, dos resultados e da conclusão daquele lote — uma
unidade **metodológica e documental**, não um contêiner operacional com
estados em cascata.

## Campos

| campo         | o que é                                                 |
| ------------- | ------------------------------------------------------- |
| `id`          | `ciclo-NN`, e casa com o nome do arquivo                |
| `numero`      | a ordem do ciclo na sequência de revisão                |
| `nome`        | o tema, dito como quem o descreve a quem não o conduziu |
| `data`        | abertura                                                |
| `regras`      | as regras **proprietárias** do ciclo                    |
| `referencias` | regras consultadas, que continuam de outro ciclo        |

Toda `RegraProposta` que este ciclo produz declara `ciclo: <este id>`
diretamente no próprio frontmatter (`okf/spec/regraproposta.md`) — é essa
declaração, não um documento de composição à parte, que liga a proposta ao
ciclo que a revisou.

## Proprietária e referência

A distinção decide de quem é o trabalho. Uma regra é **proprietária** de um
ciclo só; ser referência em outro não a transfere, e a análise feita ali é
herança do ciclo dono, não trabalho a refazer.

## Protocolo de abertura do ciclo

Antes de produzir unidades em massa, o ciclo levanta cinco coisas. Nenhuma
delas é trabalho novo: são as que o Ciclo 1 fez tarde, e cujo atraso custou
retrabalho estrutural — a decomposição foi refeita de duas coortes para três
famílias depois de as quarenta unidades já existirem, e a decisão sobre a carga
foi tomada duas vezes.

1. **Matriz preliminar de discriminantes.** O que separa uma unidade da outra,
   listado antes de existir unidade: janelas temporais, requisitos, causas,
   categorias funcionais, base de cálculo, limitadores, reajuste, opções ou
   vínculos jurídicos, exceções e vias alternativas de seleção. Um
   discriminante descoberto depois da geração não custa uma regra: custa a
   cardinalidade inteira.
2. **Inventário da evidência operacional.** Para a população que o ciclo
   alcança, o que o catálogo legado já mostra — quais regras a atendem hoje,
   que valores de domínio fechado elas gravam, o que é simulável. É esse
   inventário que distingue "o sistema não faz" de "não sabemos como o sistema
   faz", e só o segundo é verdade enquanto ninguém conferiu.
3. **Componentes de atomicidade.** O grafo origem↔destino calculado desde o
   início, para que se saiba de antemão o que avança junto e qual pendência
   contamina qual conjunto — em vez de descobrir na véspera da carga.
4. **Expressão lógica e cenários de fronteira.** A condição de cada família
   escrita em linguagem corrente, com **e** e **ou** explícitos, e os casos de
   fronteira resolvidos: véspera e dia de cada marco, cada opção presente e
   ausente, varredura sem lacuna nem sobreposição. Isso precede o template, não
   o sucede.
5. **Classificação inicial das pendências**, pelo efeito que cada uma produz:
   jurídica (impede definir a regra); operacional testável (entra em
   homologação com ressalva); técnica sem projeção possível (impede a carga);
   externa (depende de informação ou decisão do IPERON); risco residual (não
   impede cobertura nem homologação). Sem essa classificação, todo
   desconhecimento vira bloqueio total, que foi o defeito corrigido em
   `okf/spec/regraproposta.md`.

Cada etapa exige o seu grau de certeza, e não o da seguinte: a auditoria
jurídica exige fundamentação normativa suficiente; a entrada em homologação
exige projeção completa e uma pergunta operacional testável; a ativação em
produção exige o resultado da homologação e os controles. Exigir numa etapa a
certeza que só a próxima pode produzir é o que impede a próxima de acontecer.

## Critério de fechamento dos ciclos de auditoria

### Objeto da auditoria

O objeto final de um ciclo não é a lista de regras legadas individualmente
considerada. É o **conjunto de regras ativas** que, ao término da auditoria, deve
representar de forma correta, completa e não ambígua o tema jurídico auditado.

O ciclo não se encerra apenas porque todas as regras importadas receberam uma
classificação ou porque os defeitos foram descritos em achados.

### Tratamento das regras erradas

Quando uma regra estiver materialmente errada — isto é, quando representar
hipótese jurídica inexistente, misturar hipóteses distintas, usar critérios
incompatíveis ou possuir identidade material diferente da que deveria
representar — ela deve ser:

1. desativada, preservando-se seu ID e seu histórico;
2. vinculada expressamente à conclusão que justificou a desativação;
3. substituída por uma ou mais regras novas, com IDs próprios, **quando
   representar de modo defeituoso uma hipótese jurídica que continua
   existindo**; ou
4. registrada com um bloco `revogada` (`okf/spec/regra.md`) — autor, data,
   justificativa e fonte — quando não houver hipótese material válida a
   preservar.

Não se deve reaproveitar o ID da regra errada para uma hipótese juridicamente
diferente. Correções meramente formais que não alterem a identidade material da
regra podem permanecer no mesmo ID, desde que essa conclusão seja expressamente
registrada.

### Descoberta de regras ausentes

A auditoria não se limita às hipóteses já representadas no catálogo legado. A
matriz normativa pode revelar uma combinação juridicamente existente para a
qual nunca houve regra cadastrada. Nesse caso, deve ser criada uma regra nova,
com ID próprio, ainda que ela não substitua nenhuma regra anterior.

Toda regra nova deve registrar sua origem material como uma destas categorias:

- **substituição** — corrige hipótese existente representada defeituosamente por
  uma regra desativada; ou
- **lacuna preexistente** — cobre hipótese juridicamente existente que não tinha
  antecedente no catálogo.

Uma regra criada para lacuna preexistente deve apontar para a combinação da
matriz que passou a cobrir, e não para uma regra legada artificialmente escolhida
como antecessora.

### Prova de cobertura

Todo ciclo deve produzir uma matriz final das combinações juridicamente
relevantes do tema. Para aposentadoria por incapacidade ou invalidez, a matriz
deve considerar, conforme aplicável:

- regime constitucional e legal;
- janela de ingresso;
- janela de implementação do direito;
- classe juridicamente relevante da causa;
- ramo integral ou proporcional;
- forma de cálculo;
- regime de reajuste e paridade; e
- demais discriminantes que alterem elegibilidade ou resultado.

Para cada combinação juridicamente possível, a matriz deve identificar a regra
ativa que a cobre. Se nenhuma regra ativa a cobrir, a combinação constitui lacuna
do catálogo e exige a criação de regra nova. Combinações juridicamente impossíveis
devem ser marcadas como impossíveis, com fundamento.

### Matriz de derivação e verificação

Quando um ciclo decompõe um pequeno número de regras legadas num número
maior de regras propostas — o caso do Bloco C do Ciclo 1, quatro origens
para quarenta destinos —, a mesma verificação estrutural se repete em cada
regra: o dispositivo citado corresponde à hipótese, as datas correspondem à
coorte, a projeção de cálculo corresponde à classe de causa. Exigir que a
coordenação leia e ateste isso regra a regra, quarenta vezes, confunde
**decisão substantiva** — que é rara e específica — com **repetição
mecânica** — que é frequente e demonstrável de uma vez.

O ciclo deve produzir uma **matriz de derivação e verificação**, documento
Markdown simples em `docs/analysis/`, que substitui essa repetição. Ela
demonstra, para cada requisito juridicamente ou operacionalmente relevante
do ciclo:

1. de onde ele deriva;
2. quais regras o materializam;
3. onde ele é representado no catálogo — coluna deployável, nome,
   fundamentação, ou combinação;
4. como ele é verificado;
5. quem ou o que realiza a verificação;
6. qual evidência é necessária;
7. se a verificação é **programática** (avaliação determinística a partir
   de campos estruturados) ou **não programática** (avaliação substantiva de
   documento, fato ou texto jurídico) — nunca rotulada como "humana" versus
   "automatizada": o que distingue as duas é a natureza da avaliação, não a
   identidade de quem a executa. Verificação não programática pode ser
   feita por pessoa, por agente, ou por pessoa assistida por agente;
8. quais pendências ainda impedem a implantação, e como cada uma se
   classifica: pendência jurídica da coordenação, dependência externa,
   dependência de implantação, ou risco residual que não afeta a cobertura.

A matriz não cria tipo OKF, schema, parser ou gate novo. É documento
revisável por pessoas e por agentes, como qualquer outro em
`docs/analysis/`.

**Efeito sobre a condição 9.** Para um ciclo com matriz, a condição 9 —
ausência de pendência que afete a cobertura material — se demonstra pela
matriz, não por atestado individual de cada regra instanciada. Uma regra
aponta, no próprio corpo, os identificadores da matriz que materializa; a
correspondência estrutural entre a regra e esses identificadores pode ser
verificada programaticamente, contra a própria matriz, sem nova decisão
jurídica por arquivo. O que a condição 9 exige — decisão sobre o mérito,
sobre exceções e sobre a suficiência das evidências — incide sobre a
matriz e é, esse sim, trabalho não programático da coordenação, feito uma
vez por requisito, não uma vez por regra.

### Relatórios derivados

Dois relatórios, gerados a partir das `RegraProposta` do ciclo e sem estado
próprio, cobrem as finalidades que antes exigiam um documento de composição:

- **Relatório do ciclo** — todas as regras do `ciclo`, com requisitos,
  derivação, fundamentação, cobertura, `estado_auditoria` e pendências de
  cada uma.
- **Relatório de implantação** — os componentes conexos do grafo
  origem↔destino (`okf/spec/regraproposta.md`, "Atomicidade é derivada") do
  ciclo, um capítulo por componente, cada um rotulado pronto ou não para a
  carga do Sisprev, com o motivo específico quando não está — sem nunca
  inventar valor de coluna fechada. Tem duas formas: a planilha
  (`data/regras-propostas.csv`), que só lista os componentes já prontos,
  nas colunas do próprio Sisprev, para conferência de campo ao lado do
  export do sistema; e o relatório impresso por ciclo
  (`site/src/pages/relatorio-ciclo/`), que lista **todo** componente do
  ciclo, pronto ou não, e é onde uma regra `estado_auditoria: concluida`
  que ainda aguarda tradução técnica aparece — rotulada como tal, não
  omitida.

Nenhum dos dois é uma entidade persistente: são vistas sobre os mesmos
dados, recalculadas a cada execução. Um recorte que hoje exige um relatório
novo não é razão para criar um tipo OKF novo.

### Gate de pendências de cobertura

Pendências localizadas podem permanecer ao final de sessões intermediárias para
que o restante do bloco prossiga. Antes da sessão de fechamento, porém, deve
haver **zero pendências que afetem a cobertura material do tema**.

A sessão de consistência transversal é responsável por inventariar todas as
pendências deixadas pelos blocos e dar-lhes uma disposição. Cada pendência deve:

1. ser resolvida na própria sessão de consistência, quando a solução for
   transversal; ou
2. retornar obrigatoriamente à sessão proprietária da regra ou do bloco, com a
   reabertura do trabalho necessário.

A sessão de fechamento não pode começar enquanto existir pendência capaz de
impedir a afirmação de cobertura completa, ausência de lacunas ou ausência de
sobreposição injustificada.

### Condições cumulativas de encerramento

Um ciclo somente pode ser encerrado quando:

01. nenhuma regra sabidamente errada permanecer ativa;
02. toda regra desativada possuir uma ou mais regras substitutas identificadas,
    quando a hipótese material continuar existindo, ou o bloco `revogada`
    (`okf/spec/regra.md`), com fundamento, quando não houver;
03. todas as combinações juridicamente relevantes estiverem cobertas por regras
    ativas, inclusive as que não possuíam antecedente no catálogo legado;
04. toda lacuna preexistente identificada tiver sido preenchida por regra nova
    com ID próprio;
05. não houver lacunas de cobertura;
06. não houver sobreposições não intencionais entre regras ativas;
07. toda sobreposição intencional estiver expressamente justificada;
08. o mapa
    `regra desativada → regra(s) substituta(s) | revogada sem substituta`
    estiver completo;
09. nenhuma `RegraProposta` do ciclo permanecer com `estado_auditoria` em
    `elaboracao` ou `preview` — toda pendência restante é de implantação
    (`estado_implantacao`) ou dependência externa, nenhuma das duas
    pendência de auditoria;
10. os cenários representativos demonstrarem que o conjunto seleciona a regra ou
    as regras esperadas; e
11. os artefatos derivados, validadores e demais gates estiverem íntegros.

Uma dependência externa pode permanecer registrada ao fim de uma sessão
intermediária. Ela não permite encerrar o ciclo quando impedir afirmar que o
tema está completamente coberto.

### O ato institucional não é condição de encerramento

As condições acima são de **auditoria**, e um ciclo se encerra quando as cumpre.
A troca efetiva do catálogo vigente é evento **posterior e único**, praticado
pelo IPERON depois de concluídos os ciclos, e não por ciclo.

A confusão entre as duas coisas tem custo prático: exigir o ato para encerrar
faria todo ciclo ficar aberto esperando um evento que não é dele, e a auditoria
não teria como declarar concluído um tema cujo trabalho terminou. O que o ciclo
entrega é a composição proposta e a prova de que ela cobre o tema — hoje o
relatório do ciclo — e o relatório de implantação mostra o que falta para o
ato acontecer; o que o ato faz é pô-la em vigor.

**Emenda (achado do Ciclo 1, RFC 0004 round 9, consolidada no round 11).**
A condição 9 confundia, quando expressa como estado do antigo `Conjunto`,
duas afirmações: que a substituição está juridicamente decidida, e que a
fonte operacional de exportação pode trocar com segurança. A segunda depende
de todos os destinos do mesmo componente do grafo origem↔destino terem
`estado_implantacao` em `confirmada` ou `confirmada_com_ressalva`
(`okf/spec/regraproposta.md`), porque a troca é atômica e um conjunto de
origens legadas tipicamente cobre, junto, mais de uma hipótese. Quando a
única pendência de um componente é `estado_implantacao: pendente_mapeamento_sisprev` — a lei está determinada para todos os destinos,
`estado_auditoria: concluida` para todos, e só a identificação da fórmula no
Sisprev depende de confirmação externa —, a condição de encerramento do
ciclo está cumprida quanto a essa substituição, ainda que o componente não
entre na carga de homologação até a confirmação. Isso não é "regra
sabidamente errada que permanece ativa" (item 1) nem lacuna de cobertura
(itens 3/5): é derivação concluída aguardando tradução técnica, registrada
como tal no relatório de implantação, não como pendência de auditoria.

**Emenda (RFC 0004, round 12 — Ciclo 1, causa comum).** O round 9 tratava
`pendente_mapeamento_sisprev` como bloqueio uniforme à carga, mas a spec já
descrevia esse valor como "a fórmula está determinada, só falta confirmação
de identificação unívoca" — o que é, em si, uma afirmação mais fraca do que
"não sabemos que mecanismo do sistema a fórmula ocupa". A carga que
`scripts/derivar.py` produz é planilha de **homologação**
(`data/regras-propostas.csv`), não ativação em produção; retê-la enquanto
existe evidência operacional concreta — origem legada em produção com a
mesma projeção de vocabulário fechado, para a mesma hipótese — inverte a
função da homologação, que existe justamente para confirmar esse tipo de
detalhe de execução. `confirmada_com_ressalva` entra na carga levando essa
ressalva; `pendente_mapeamento_sisprev` continua fora dela para o caso em
que não há sequer essa evidência.

### Aplicação ao Ciclo 1

No Ciclo 1, a conclusão deve demonstrar que o conjunto ativo cobre integralmente
a aposentadoria por incapacidade permanente **sob a norma em vigor para
requerimento novo**, inclusive suas classes de causa, ramos de cálculo, janelas
de ingresso e regimes de reajuste.

As hipóteses históricas de invalidez — as janelas anteriores, em que não se
forma direito novo depois dos seus marcos finais, mas que seguem fundamentando
requerimento novo com base em direito adquirido — foram deslocadas para o
Ciclo 9, "Janelas históricas de invalidez", que é o dono delas. O deslocamento
é de escopo, não de método: as regras propostas dos Blocos A e B permanecem
autoradas com `estado_auditoria: preview`, e é o Ciclo 9 que as promove.

O relatório final do próprio `ciclo-01.md` deve conter:

- a situação final de cada regra legada;
- as novas regras criadas, classificadas por origem como `substituição` ou
  `lacuna preexistente`;
- o mapa de substituições e os registros fundamentados de revogação sem
  substituta;
- a matriz de cobertura completa, inclusive as lacunas preexistentes descobertas
  e as regras novas que passaram a cobri-las;
- as combinações juridicamente impossíveis e seus fundamentos;
- as sobreposições intencionais, se houver;
- a demonstração de zero pendências que afetem cobertura; e
- os riscos residuais que não comprometam a completude da cobertura.

O Bloco C do Ciclo 1 — quatro origens legadas para quarenta regras
propostas — é o caso concreto que motivou a matriz de derivação e
verificação descrita acima. Está em
[`docs/analysis/matriz-derivacao-verificacao-ciclo-01.md`](../../docs/analysis/matriz-derivacao-verificacao-ciclo-01.md),
e é ela, não uma conferência individual das quarenta regras, que demonstra
a condição 9 para esse bloco.
