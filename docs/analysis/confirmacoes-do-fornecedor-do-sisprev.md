# Confirmações da empresa responsável pelo Sisprev

> **Nota:** Registro de fatos sobre o **produto** obtidos junto à empresa que
> desenvolveu o Sisprev, trazidos à auditoria pela coordenação. **Não é artefato
> oficial** e não edita regra, dispositivo ou dado derivado. Existe porque um
> fato sobre o comportamento do sistema não é derivável do catálogo — ele vem de
> fora, e sem lugar próprio acabaria sobrevivendo só em conversa. Cada item diz o
> que foi confirmado e o que o item **não** resolve.

## Por que este documento existe

Boa parte das questões abertas da RFC 0001 pergunta o que um campo **significa
no sistema de origem** — a Q1 sobre o fato jurídico das datas, a Q10 sobre `sexo`
vazio e sobre `Não identificado`. Nenhuma delas se responde lendo o catálogo,
porque o catálogo é o que se quer interpretar.

A auditoria precisa de **hipótese de trabalho explícita** para prosseguir. Sem
ela, todo campo cuja semântica não esteja fechada ficaria imune a conferência, e
o catálogo sairia inauditável por uma questão que a auditoria existe para
resolver. Declarar a hipótese, e de onde ela veio, é o que permite saber
exatamente o que cai junto caso ela seja revista.

## As confirmações

### 1. `DATA_ADM_*` é a data de admissão

Fixa o **gênero** do marco: o campo registra entrada no serviço, não aquisição
de direito nem qualquer outro fato.

**Complementação por fontes oficiais (2026-07-30).** A distinção fina foi
resolvida sem nova consulta ao fornecedor. A Portaria MTP 1.467/2022, art. 166,
manda considerar a “data da investidura mais remota”; a LC estadual 68/1992,
art. 10, estabelece que a investidura em cargo público ocorre com a posse.
Logo, para “ingresso em cargo efetivo”, a espécie jurídica de admissão adotada
pela auditoria é a **posse**, não a nomeação nem o início do exercício. Continua
fora do alcance documental apenas verificar qual coluna física do banco o motor
lê, se o cadastro local divergir desse conceito.

**Ressalva com consequência própria.** "Admissão" e "ingresso na respectiva
carreira" podem não coincidir: quem foi admitido no serviço estadual numa data e
ingressou numa carreira específica em outra tem dois marcos distintos.
Dispositivos que recortam por ingresso em carreira — o art. 7º da ECE 146/2021 é
o caso trabalhado — recortam pelo segundo. Se o Sisprev afere o primeiro, o
descompasso atinge todas as regras daquele artigo.

**Onde já incide:** hipótese de trabalho declarada do `achado-0055`.

### 2. `sexo` vazio indica regra provavelmente desativada, mantida por histórico

A ausência de valor não é "ambos", nem "desconhecido": sinaliza que a regra
provavelmente não está mais em uso e permanece no cadastro para fins históricos.

**O que isso ilumina.** É a resposta que faltava para a Q10 na parte que
distingue `AMBOS` de vazio, e o marcador de inativação que o catálogo não
parecia ter — `atualmente_no_sistema` está uniformemente `TRUE` e por isso não
serve para essa leitura.

**Corroboração interna, não circular.** As regras com `sexo` vazio compartilham
uma assinatura que o campo não impõe: `integral` também vazio no mesmo conjunto,
`tipo_calculo: Não identificado` em todas, e `simulavel: N` em quase todas. Três
campos independentes concordando com a leitura do fornecedor é evidência de que
ela descreve um estado real do cadastro, e não uma coincidência de preenchimento.

**O que não resolve.** "Provavelmente desativada" não é ato de revogação. A
representação de uma regra fora de uso é `Conjunto.revoga` (RFC 0006), e isso
depende de decisão autorada por regra, não de inferência a partir de um campo
vazio. Também não se conclui que toda regra desativada tenha `sexo` vazio — a
implicação confirmada tem uma direção só.

### 3. O operador seleciona o **tipo do benefício** antes de escolher a regra pelo nome

O fluxo do sistema filtra por tipo primeiro; a lista de nomes que o operador vê
já está restrita àquele tipo.

**Consequência direta sobre o `nome`.** Repetir no nome o que o filtro anterior
já garantiu não ajuda a escolher e ocupa espaço: em toda a lista visível, o termo
é constante, e termo constante não recorta nada. É o mesmo raciocínio pelo qual o
site marca `data-pagefind-ignore` no que se repete igual em toda ficha.

**O que não resolve.** Se o tipo deve sumir do nome ou aparecer abreviado no
início é decisão de desenho, não fato do produto. Uma abreviação curta ainda
serve de âncora visual e protege contra leitura fora do fluxo — relatório,
planilha, ficha do site —, onde o filtro que dava o contexto não existe.

### 4. `TIPO DE BENEFICIO` é domínio fechado do produto (2026-08-04)

O campo não está aberto a valor novo: os seus membros são do sistema, e
inventar um deixaria a linha irrepresentável no cadastro. A auditoria não
escolhe o valor — ela grava o que o produto já admite.

**O que a confirmação autoriza, e é estreito.** Uma regra proposta pode gravar
o valor que a **regra de origem já grava**, porque esse valor veio do próprio
sistema e está no catálogo recebido. Não é caso de valor novo: é a proposta
deixando de divergir da linha que ela substitui.

O catálogo recebido exibe seis membros, e o corte entre os dois de
incapacidade é o regime: as regras das janelas históricas gravam
`APOSENTADORIA POR INVALIDEZ`, e as da LCE 1.100/2021 — as quatro que o Ciclo
1 substitui, todas com `ATUALMENTE NO SISTEMA: TRUE` — gravam `APOSENTADORIA POR INCAPACIDADE PERMANENTE`.

**O que não resolve.** Não diz que o conjunto de membros observado no catálogo
seja o conjunto completo do produto — o catálogo mostra o que está em uso, não
o domínio. E não autoriza mudar o tipo de uma regra **para outro regime**, que
seria mudar o benefício de tela para quem atende o requerimento: pela
confirmação 3, o operador filtra por tipo antes de ver a lista de nomes.

## O que permanece pendente (issue #124)

As quatro confirmações acima respondem perguntas específicas, já levadas ao
quadro de questões. Nenhuma delas resolve as duas premissas que o Ciclo 1
declara e não confirma — e que, enquanto pendentes, acompanham toda conclusão
que delas dependa (ver `okf/spec/tipocalculo.md`):

1. **Captura e classificação da causa da incapacidade (Q6‑S/Q6‑T).** Não há
   confirmação do fornecedor sobre se o Sisprev em produção tem campo para o
   fato da causa, de onde ele viria (laudo, perícia, anamnese) e como o
   diagnóstico é cotejado com o inciso do rol legal. O dossiê
   [`q6-causa-incapacidade.md`](q6-causa-incapacidade.md) documenta a
   investigação e a fila de perguntas (§9) — nenhuma delas foi respondida pelo
   fornecedor até a data deste documento. É **inferência da auditoria**, não
   confirmação, que causa não informada ou prova insuficiente não equivalem a
   `causa_comum`; o comportamento do produto continua desconhecido.
2. **O que cada `tipo_calculo` implanta.** A auditoria descreve juridicamente a
   fórmula de cada regra e declara a premissa de que o rótulo gravado é aquele
   pelo qual o sistema a executa — para o rótulo `Proporcionalidade Dias`
   projetado nas unidades de causa comum do Ciclo 1, a premissa está registrada
   com fidelidade **parcial** em
   [`forma-calculo-media-proporcional-dias-lce1100`](../../okf/formas-calculo/forma-calculo-media-proporcional-dias-lce1100.md).
   Que o sistema de fato compute a média do art. 24 proporcionalizada em dias
   sob esse rótulo, e não uma contagem de dias isolada, não foi confirmado.
3. **A opção do § 16 do art. 40 da Constituição Federal.** Não há coluna
   própria no cadastro para registrar se o servidor optou pelo regime de
   previdência complementar. As unidades do Ciclo 1 registram que essa opção é
   conferida no processo, junto com o requisito da causa — é **inferência da
   auditoria** sobre como o limite de uma coluna por requisito é contornado na
   prática, não confirmação de como o IPERON efetivamente trata a hipótese.

Nenhuma dessas três é conclusão jurídica, e nenhuma se fecha por leitura do
catálogo: dependem de resposta do IPERON e do fornecedor. Enquanto não
responderem, a issue [#124](https://github.com/franklinbaldo/sisprev/issues/124)
permanece aberta, e as regras do Bloco C que citam Q6‑S/Q6‑T ou a projeção de
`tipo_calculo` mantêm a caixa correspondente aberta como dependência externa —
o que não impede `estado_proposta: deployable`, porque a spec do ciclo admite
que dependência externa permaneça registrada sem obstar o encerramento,
quando não afeta a cobertura material do tema.

## Onde estas confirmações já estão incorporadas

Elas **não vivem só aqui**. Cada uma foi levada ao documento que governa a
leitura do campo, e é lá que quem audita a encontra sem precisar saber que este
documento existe:

- a semântica de `DATA_ADM_*` está na Q1 do quadro de questões e na seção
  "Elegibilidade temporal" de [`okf/spec/regra.md`](../../okf/spec/regra.md);
- a leitura de `sexo` vazio está na Q10 do mesmo quadro;
- a seleção do tipo antes do nome está na
  [Decisão 9](decisoes-de-auditoria-2026-07-30.md), que fixa a gramática de
  `nome`;
- o domínio fechado de `TIPO DE BENEFICIO` está registrado nas quarenta
  unidades do Ciclo 1 que passaram a gravar o valor da sua origem, cada uma
  com a razão em `decisoes:`.

**O quadro de questões é a fonte operativa**; este documento é a proveniência.
Divergindo os dois, o quadro ganha e a divergência é ela própria um defeito a
corrigir — como vale para toda duplicação de verdade no repositório.

## O que este documento não é

Não é fonte normativa: nada aqui interpreta lei. Não é ato do IPERON: as
confirmações são sobre o comportamento do software, e quem responde pelo
conteúdo jurídico das regras é o instituto. E não é substituto de conferência —
uma confirmação sobre o produto explica o que o campo pretende registrar, jamais
que o valor gravado numa regra específica esteja correto.
