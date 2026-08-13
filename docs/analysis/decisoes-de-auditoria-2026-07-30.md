# Decisões transversais da auditoria — 30 de julho de 2026

> **Nota:** As oito decisões abaixo foram tomadas pela coordenação da
> auditoria; a redação é apoio de IA. **Não é artefato oficial** e não valida
> regra nenhuma: nenhuma decisão aqui grava campo deployável, promove estado
> de auditoria ou põe conjunto em vigor. O que este documento faz é fixar,
> antes da execução, as políticas que atravessam várias famílias de regras —
> justamente para que elas não sejam decididas de novo, e diferente, dentro de
> cada sessão.

## 1. Por que decidir antes

Cada decisão daqui alcança várias famílias ao mesmo tempo. Decidi-la dentro de
uma sessão de família produz respostas incoerentes entre sessões, e a
incoerência não aparece em gate nenhum: cada regra fica plausível isolada, e o
catálogo fica com dois critérios para o mesmo problema. É o mesmo modo de falha
silencioso da cadeia de vigência dos dispositivos — cada parágrafo confere, e o
conjunto não.

O que **não** é decidido aqui: nada que dependa de fato sobre o Sisprev que não
temos (a seção 9 diz como a auditoria segue apesar disso), e nada que pertença
ao titular do produto — as decisões abaixo dizem o que a auditoria **propõe** e
como registra, nunca o que o IPERON grava.

## 2. Decisão 1 — a gramática de `nome` é fixada agora, e é derrotável

`P1_NOME_REPETIDO` é, entre os gates de `revisada`, o que alcança mais regras
do catálogo — `collect_detections` responde quantas em qualquer commit. Isso faz
do `nome` precondição do trabalho inteiro, não polimento de fim de fila: as
famílias das fases seguintes batem nele de qualquer maneira.

A spec já autorizava a edição in loco de `nome` e já mandava que ele melhorasse
durante a auditoria. O que faltava era a **forma**, que a spec deixou aberta à
espera das restrições reais da tela do Sisprev (comprimento, truncamento, busca,
ordenação). A decisão é **fixar a gramática sem essa confirmação**, declarando a
premissa: esperar trava o catálogo por prazo que a auditoria não controla, e
nomear caso a caso garante incoerência entre famílias.

### A gramática

Seis posições, na ordem. **Cada posição só entra quando discrimina** a regra das
que ainda podem ser aplicáveis depois da anamnese — nome não é descrição
completa, é a menor descrição que distingue.

| #   | posição               | entra quando                            | exemplo                            |
| --- | --------------------- | --------------------------------------- | ---------------------------------- |
| 1   | modalidade            | **sempre**                              | `Aposentadoria voluntária`         |
| 2   | recorte de carreira   | a modalidade tem regime próprio         | `do policial civil`                |
| 3   | marco de ingresso     | há mais de um trilho por data de posse  | `ingresso até 31/12/2003`          |
| 4   | critério aferido      | é o que separa as candidatas restantes  | `mulher`, `deficiência grave`      |
| 5   | resultado             | duas candidatas diferem só no resultado | `proventos integrais com paridade` |
| 6   | fundamento, abreviado | **só** como desempate final             | `(EC 146/2021, art. 7º)`           |

As posições são separadas por **travessão cercado de espaços**. Sem abreviação
opaca como carga principal (`Perm.`, `c/c`,
`§1º, I` sozinho). O teto de comprimento é **115 caracteres**: não é escolha
estética, é o comprimento do maior `nome` da importação original, isto é, um
valor que o Sisprev **comprovadamente aceita**. O número está ancorado em teste
contra `data/raw/`, que é imutável, e por isso não envelhece
(`tests/test_nome_gramatica.py`).

### As duas regras que fazem a gramática ser honesta

**A citação legal é o último recurso, nunca o primeiro.** Dois nomes que diferem
apenas pelo número de um artigo continuam ruins mesmo sendo únicos — quem lê a
tela não sabe qual artigo é o seu caso. A posição 6 existe para o desempate que
as cinco anteriores não deram, e um nome que precise dela é sinal de que o
discriminante real não foi encontrado.

**Se as posições 1–5 não distinguem, não se desempata pelo número do artigo.**
Duas regras que ficam com o mesmo nome depois de aplicada a gramática são
**lacuna do modelo**: o catálogo não possui o predicado que as separa. Isso vira
achado, e o `P1` continua acusando até que a lacuna seja resolvida ou registrada.
Desempatar por citação nesse caso limparia o `P1` e apagaria a lacuna — trocar
um diagnóstico verdadeiro por um nome único.

### O que a decisão não estende

`nome` fora da chave material do `P2` continua fora, e renomear **não** dissolve
um grupo `P2`: o grupo é de igualdade material, e nome não é material. Corrigir
nome resolve `P1`, e deixar o `P2` de pé é o comportamento correto. Também não
está demonstrado que um `AtoValidacao` anterior cubra o rótulo novo — a spec já
registra isso como aberto, e nada aqui presume que cubra.

## 3. Decisão 2 — sentinela é ausência de valor conferido

As quatro sentinelas (`01/01/1900`, `01/01/1910`, `01/01/1950`, `31/12/2099`)
estavam nomeadas sem que se dissesse o que significam, e a RFC 0011 registra
essa abstenção como deliberada. A decisão preenche o mérito **sem** mudar o
nome dos membros:

> Uma data sentinela afirma que **ninguém gravou limite conferido** naquela
> coluna. Não afirma "sem limite".

Três consequências operacionais:

1. **Onde o dispositivo citado fixa prazo expresso, a sentinela é erro**, e a
   auditoria propõe a data real em unidade auditada. É o caso do `achado-0022`
   (art. 4º da ECE 146/2021, cinco regras gravando `31/12/2099` contra prazo
   expresso) e do `achado-0035`.
2. **Onde o dispositivo não fixa prazo, a sentinela permanece pendência
   escrita** — não vira "sem limite" por falta de alternativa.
3. **Nada muda no simulador, na ficha e no relatório**, que já marcam o valor
   sem dizer o que significa. A decisão confirma o comportamento que já existe
   em vez de pedir código novo.

`01/01/1969` continua **fora** do conjunto de sentinelas, como suspeita
registrada. Uma suspeita que entra sem ato de ninguém vira decisão de que aquele
limite não é critério.

## 4. Decisão 3 — grupo `P2` é decidido caso a caso, sem presunção

Não há default entre autonomia, consolidação N:1 e revogação pura. Cada grupo é
aberto pelo mérito.

Uma decisão sem presunção declarada tem um risco próprio: o critério fica
implícito no resultado, e a sessão seguinte não sabe por que a anterior decidiu
como decidiu. A trava contra isso é **requisito de registro, não presunção**:

> Todo grupo `P2` resolvido registra, por escrito, qual dos três desfechos foi
> tomado e a razão de mérito que o sustenta — na disposição do achado quando não
> há sucessora, na `UnidadeAuditada.decisoes` quando há.

Isso mantém a decisão caso a caso e ainda deixa o critério auditável depois. O
que segue proibido é o atalho: dissolver um grupo `P2` renomeando, que limparia
o `P1` sem tocar a igualdade material.

## 5. Decisão 4 — citação falsa recebe proposta, mesmo quando a correta não é certa

Quando a provisão correta é determinável, a auditoria propõe — é o que a
`regra-0078` fez. A decisão vai além: **quando não é determinável, a auditoria
ainda propõe a leitura mais provável**, em vez de só acusar.

Isso convive com a RFC 0008, e a distinção é de espécie. O que a RFC 0008
removeu foi **inferência mecânica**: um leitor por regex que produziu nove
atribuições erradas, todas com aparência de citação bem formada. Um humano que
abre o dispositivo, lê a fonte e escreve qual provisão a regra provavelmente
pretendia citar é outra operação — falível, mas autorada, datada e assinada.

Três travas, que são o que torna a proposta auditável em vez de chute com
aparência de conclusão:

1. **`confianca` rebaixada** (`media` ou `baixa`) na unidade, sempre que a
   provisão não foi confirmada contra a fonte.
2. **A unidade diz por escrito o que não foi confirmado** — qual passo é
   reconstrução de intenção e não leitura de texto. Uma proposta que não
   distingue as duas coisas afirma mais do que sabe.
3. **A disposição do achado é `encaminhada`, nunca `corrigida`.** O campo
   deployável segue como está até que o titular do produto decida. `corrigida`
   afirmaria que o defeito não vale mais para esta regra, o que seria falso.

Alcança os bloqueantes de fundamentação inexistente ou extinta: `achado-0021`,
`achado-0049`, `achado-0050`, `achado-0051`, e os informativos `achado-0012` e
`achado-0013`.

## 6. Decisão 5 — data sem lastro: separar erro de data de lacuna de vínculo

A maior família de achados é data **não sentinela** que o dispositivo citado não
sustenta. Esses achados estão numa pilha só, e são dois defeitos distintos:

| situação                                         | leitura               | o que a auditoria faz                         |
| ------------------------------------------------ | --------------------- | --------------------------------------------- |
| a norma citada **fixa** marco expresso, e difere | **erro de data**      | propõe a data do dispositivo em unidade       |
| a norma citada **não fixa** marco algum          | **lacuna de vínculo** | acusa que falta vincular a norma que institui |

A distinção importa porque as duas conclusões são opostas sobre o mesmo campo:
na primeira, a data gravada está errada; na segunda, ela pode estar certa e vir
de fonte que o catálogo não cita. Tratar tudo como lacuna presume a data
correta, e há datas que nenhuma norma sustenta; tratar tudo como erro inventa
correção onde falta é vínculo.

Alcança `achado-0015`, `achado-0024`, `achado-0027`, `achado-0032`,
`achado-0033`, `achado-0039`, `achado-0042`, `achado-0047`, `achado-0048` e
`achado-0052`.

## 7. Decisão 6 — o mapa critério → dispositivo é exigido de `revisada`

A quinta pergunta do P13.1 — qual dispositivo funda qual critério — deixa de ser
recomendação. Sem ela, `revisada` afirmaria que a auditoria terminou sem que
ninguém tenha conferido se **cada** critério aferido tem fundamento, o que é
precisamente o conteúdo do trabalho; as outras conferências são mecânicas em
comparação.

**Nenhum campo novo, nenhum gate novo.** O mecanismo já existe e é o checklist
do `# Estado da análise`: uma caixa aberta derruba `revisada` por
`P7_ESTADO_INVALIDO`. A exigência é que o checklist de uma regra `revisada`
cubra esse item — forma verificada pelo CI, mérito nunca. É a mesma razão pela
qual a relação ficou sem schema na RFC 0008 §5: `dispositivos:` é a união
achatada da articulação e perde qual provisão funda qual critério; recuperar
isso é prosa autorada, não campo.

O custo é real e foi aceito: cada regra exige prosa própria, e não há atalho.

## 8. Decisão 7 — Q2 e Q10 seguem como premissa escrita e derrotável

`DATA_DIREITO_APOS` (Q2) e a distinção entre `AMBOS`, vazio, desconhecido e não
aplicável (Q10) são **fatos sobre o Sisprev**, não decisões da auditoria, e não
temos resposta. Bloquear tudo o que delas depende retiraria da mesa boa parte
dos achados por prazo indeterminado; decidi-las como se fossem nossas
contrariaria o escopo, que é parametrização e não mudança do sistema.

A saída é a terceira: **premissa expressa, marcada como não confirmada**.

- **Q2** — `DATA_DIREITO_APOS` é lido como **inclusivo**: o valor gravado é o
  primeiro dia coberto. Os dois eixos **não** compartilham semântica —
  `DATA_ADM_APOS` é exclusivo e o seu valor é o último dia do regime anterior.
- **Q10** — vazio é lido como **não gravado**, nunca como `AMBOS` presumido nem
  como "não aplicável". Ou seja: vazio é pendência, não valor.

A condição que faz a premissa valer a pena: **toda conclusão que dela depender
cita a premissa**. Assim uma resposta futura do IPERON invalida um conjunto
identificável de conclusões, em vez de deixar dúvida sobre o catálogo inteiro.

**A premissa da Q2 foi corrigida no mesmo dia, e o percurso importa mais que o
resultado.** A primeira redação desta decisão registrou a leitura **exclusiva**,
por simetria com `DATA_ADM_APOS`. A simetria caiu na primeira medição contra o
catálogo: `DATA_DIREITO_APOS` grava invariavelmente o dia da entrada em vigor da
norma vinculada, e sob leitura exclusiva a maioria do catálogo negaria o benefício
no primeiro dia da norma que o funda. A população e a bifurcação estão no
[`achado-0053`](../../okf/regras-sisprev/achados/achado-0053.md).

Duas lições que valem para as próximas premissas. **Premissa que se sustenta só na
simetria do nome de uma coluna deve ser medida antes de ser usada** — o curinga
`DATA_*` da formulação original da Q1 já pressupunha a resposta, e pressupunha a
errada. E **premissa errada não é inócua**: se a exclusiva tivesse sido usada em
vez de medida, a auditoria teria produzido acusação de erro de um dia contra a
maior parte do catálogo — em massa, plausível e falsa, que é exatamente o modo de
falha da RFC 0008 chegando por outra porta.

## 9. Decisão 8 — célula de fundamentação empacotada é decomposta 1:N

Uma célula que empacota duas ou três articulações separadas por barra vertical
carrega mais de uma hipótese numa linha. A decomposição 1:N da RFC 0004 existe
para isso: **N unidades auditadas, uma por articulação**, cada uma com o seu
`dispositivos:`.

Isto **supera** a recusa registrada em `regra-0021`/`regra-0022`, onde não se
vinculou dispositivo porque a divisão é por causa da incapacidade e não há
coluna que a registre. A recusa protegia contra vincular por chute; a
decomposição não tem esse defeito, porque cada unidade declara a sua própria
articulação em vez de achatar as três numa lista.

A falta de coluna não desaparece — ela **muda de lugar e fica demonstrável**. O
compilador dirá se as N projeções cabem no alvo legado, e se não couberem, essa
é a lacuna, provada por compilação em vez de argumentada em prosa. Alcança o
`achado-0037` e o quarteto `regra-0019` a `regra-0022`.

## 10. Decisão 9 — o eixo `DATA_DIREITO_*` é rotulado por tipo de benefício no `nome`

A Q2 pergunta se `DATA_DIREITO` é "implementação dos requisitos, data do óbito,
data do laudo, requerimento, ou outra referência **conforme o benefício**". A
pergunta já previa que a resposta varia, e a gramática de `nome` passa a
refletir isso: o rótulo do eixo muda com o tipo.

| tipo de benefício                    | rótulo       |
| ------------------------------------ | ------------ |
| Pensão por morte                     | `óbito`      |
| Voluntária por tempo de contribuição | `pedido`     |
| Por idade                            | `pedido`     |
| demais                               | `requisitos` |

**Por que `pedido` nos voluntários.** O requerimento é ali requisito sem o qual
não há concessão — o benefício não se defere de ofício —, e enquanto o ato de
aposentadoria não é firmado o servidor pode trocar o pedido por outro. É o fato
que o requerente reconhece e controla, e é o que a apresentação deve nomear.

**Por que os demais ficam genéricos.** Compulsória se dá de ofício, e ali não há
pedido a nomear; invalidez e incapacidade permanente dependem de laudo, hipótese
que a própria Q2 levanta e que ninguém conferiu. Rotular esses eixos com o fato
específico afirmaria conferência que não foi feita, então `requisitos` fica como
o rótulo que não decide.

**O que esta decisão não faz.** Não altera a resposta parcial já registrada para
a Q2 — `DATA_DIREITO_ATE` continua sendo o prazo para que **todos** os requisitos
estejam completos. O rótulo é apresentação: nomeia o requisito que o requerente
reconhece, não afirma que ele seja o único. Um nome que dissesse "pedido" onde o
campo é conferido por outra via seria erro de leitura, e é por isso que ele só
aparece onde o pedido é, de fato, requisito da concessão.

**As duas pontas do eixo não são simétricas, e presumir que fossem era erro.**
`semantica-das-janelas-temporais.md` §5.3 pergunta explicitamente se
`DATA_DIREITO_APOS` tem leitura simétrica à do `ATE`, e adverte contra presumir
que compartilhem semântica. A coordenação respondeu para o limite superior: ele é
o **prazo para implementar os requisitos**, e a data do pedido não importa — quem
implementou até a data pode requerer depois, que é a proteção do direito
adquirido.

Logo `pedido até` seria **falso**, e o rótulo `pedido` sobrevive apenas na ponta
inferior dos benefícios voluntários, onde nomeia o requisito que o requerente
controla. Toda ponta superior — e todo intervalo, cujo limite vinculante é a
superior — usa `requisitos`:

| forma da janela    | rótulo                                            |
| ------------------ | ------------------------------------------------- |
| só limite inferior | `pedido a partir de <data>` (voluntários)         |
| só limite superior | `requisitos antes de <data>`                      |
| intervalo          | `requisitos a partir de <data> e antes de <data>` |

**A preposição carrega a inclusividade, e os quatro limites divergem.** Fechada a
inclusividade dos eixos em [`okf/spec/regra.md`](../../okf/spec/regra.md)
("Elegibilidade temporal"), os quatro limites não se comportam igual. Usar a
mesma preposição nos quatro erra um dia em dois deles, **na direção de incluir
quem a regra não alcança**.

| campo               | inclusividade | preposição           |
| ------------------- | ------------- | -------------------- |
| `DATA_ADM_ATE`      | inclusivo     | `até <data>`         |
| `DATA_ADM_APOS`     | exclusivo     | `após <data>`        |
| `DATA_DIREITO_APOS` | inclusivo     | `a partir de <data>` |
| `DATA_DIREITO_ATE`  | exclusivo     | `antes de <data>`    |

O intervalo junta as preposições das suas duas pontas com "e", porque elas são
diferentes e justapô-las produziria frase truncada.

**A data continua exibida como gravada.** Ajustá-la ao primeiro ou último dia de
cobertura esconderia o marco, e a spec é explícita em que o valor gravado é o
marco, não o primeiro dia da cobertura. Quem carrega a diferença é a preposição.

**`Ambos` é omitido nas regras de pensão por morte.** Ali o sexo não opera como
critério: nenhum dispositivo citado por elas diferencia por sexo, e a única
menção nos textos transcritos é cláusula equalizadora — a conferência está no
[`achado-0056`](../../okf/regras-sisprev/achados/achado-0056.md). `Ambos` anuncia
uma dimensão de aferição que não recorta nada, e faceta que não discrimina é
ruído numa lista feita para escolher.

`Masculino` e `Feminino` **continuam aparecendo** nas regras de pensão que os
gravam, e é deliberado: são justamente as que afirmam o critério sem lastro, e o
nome as mantém visíveis em vez de uniformizá-las com as demais. Quando a
revogação que o `achado-0056` decidiu alcançar o catálogo vigente, elas saem e o
eixo do sexo desaparece da pensão por inteiro.

Isto corrigiu nomes já commitados: a primeira aplicação desta gramática usou `até`
e `a partir de` nos dois eixos, presumindo semântica comum — o mesmo erro que a
spec cometeu duas vezes com o curinga `DATA_*`, e que a resolução do eixo do
direito diagnostica.

**As facetas de resultado vêm no fim, e a posição é o argumento.** `integral` ou
`proporcional`, `paridade` quando houver, e o `tipo_calculo` verbatim fecham o
nome, depois de todo critério. Elas não servem à triagem — ninguém chega ao balcão
sabendo que seu cálculo é "Valor Médio" —, servem ao desempate e à conferência de
quem já escolheu; e nessa posição não competem com os critérios pela atenção de
quem varre a lista.

O ganho é medível: os nomes que precisam de sufixo de id caem de trinta e três
para dezessete. E o que sobra passa a ser exatamente duas situações, ambas
irredutíveis por qualquer faceta — regras **materialmente idênticas**, que o
`P2_IGUALDADE_MATERIAL_ATIVA` já reporta, e regras que divergem **só na
fundamentação**, que a gramática deliberadamente não carrega. O sufixo deixa de
ser desempate genérico e passa a marcar essas duas.

**Cálculo e paridade são duas facetas, não uma, e a primeira aplicação as
fundiu.** A gramática acima abre um espaço para o rótulo de cálculo e outro para
a paridade; a execução gravou **um só**, escolhendo `paridade` sempre que o campo
dizia `S` e descartando o rótulo de cálculo junto. O resultado é o defeito que a
coordenação apontou no Ciclo 1, e ele é duplo:

- **a faceta deixa de desempatar.** Uma parte grande do catálogo grava
  `paridade: S`, então o nome de todas elas termina na mesma palavra, e uma
  faceta que não recorta nada é ruído numa lista feita para escolher — o mesmo
  argumento que tirou `Ambos` das regras de pensão, aplicado ao outro extremo do
  nome;
- **e ela passa a afirmar o que não é.** Ocupando o lugar do cálculo, `paridade`
  é lida **como** o cálculo. Onde o rótulo gravado indica cálculo sobre médias —
  `Remuneração de Contribuição` em `regra-0008`/`regra-0009`, a Nova Previdência
  da pensão em `regra-0016` a `regra-0018` — o nome dizia "paridade" e nada mais,
  e paridade é regra de **reajuste**, não base de cálculo. A leitura que sobrava
  para quem varria a lista era a de um benefício calculado "pela paridade", que
  não existe.

**A correção é ordenar as duas, nunca substituir uma pela outra**: `integral` ou
`proporcional`, o rótulo de cálculo, e `paridade` por último, quando o campo a
gravar. Uma regra pela média com paridade passa a dizer as duas coisas, que é o
que ela é — e a tensão entre elas, se houver, fica **visível** em vez de coberta
pela faceta que sobreviveu.

**O rótulo de cálculo resume sem classificar**, e a distinção é o que o torna
admissível. O `CLAUDE.md` e `tests/test_forma_calculo_schema.py` proíbem um
mapeador `tipo_calculo → componentes`, porque o enum legado mistura base, ajuste
e limitador no mesmo rótulo — `Valor Efetivo mais 70% do que exceder do Teto RGPS` é base **e** limitador; `Proporcionalidade Dias` é ajuste sem base — e
inferir a fórmula dele produziria acusação plausível e não verificada, a classe
de erro da RFC 0008. Nada aqui infere fórmula:

- `paridade` sai do **campo** `paridade`, é faceta própria e **nunca** ocupa o
  lugar do cálculo;
- `média` é leitura **literal** da substring "Médio" no valor gravado — e é por
  ser literal que `Remuneração de Contribuição` sai verbatim, ainda que o nome do
  rótulo sugira média: dizer qual é a base é conferência de dispositivo, não
  leitura de rótulo;
- todo valor que não cai em `média` sai **verbatim**, sem balde;
- `Não identificado` e a célula vazia **não produzem faceta nenhuma** — um rótulo
  que não nomeia cálculo não vira palavra no nome, e a regra fecha na paridade ou
  no `integral`/`proporcional`.

**E o nome não substitui o valor.** `tipo_calculo` continua sendo coluna própria,
ao lado, autoritativa; quem precisa do rótulo exato o tem sem abrir o
repositório. É o princípio da ficha do site — valor exibido não esconde valor
gravado — aplicado a um resumo, não a uma tradução.

**O custo é comprimento**, e agora ele é pago em vez de economizado: recolocar o
rótulo de cálculo ao lado da paridade alonga os nomes que a fusão havia
encurtado. É o preço de o nome não mentir sobre o cálculo, e é o preço certo. Se
o limite da coluna `NOME` do Sisprev vier a apertar, a faceta a sacrificar é o
`integral`/`proporcional` — nunca o rótulo de cálculo em favor da paridade, que
foi exatamente a troca que produziu o defeito.

**Derrotável, como as demais.** Fechada a Q2 para invalidez ou compulsória, os
rótulos correspondentes passam a poder ser específicos, e a tabela acima é o
único lugar a alterar.

## 11. Decisão 10 — a auditoria está autorizada a alterar `nome` e `FUNDAMENTACAO*`

A questão 4 do [`achado-0020`](../../okf/regras-sisprev/achados/achado-0020.md)
registrava que, sendo `nome` deployável, a correção pertenceria ao catálogo
auditado da RFC 0004 e não a uma edição em `regra-*.md`. A coordenação decidiu o
contrário: **a auditoria pode alterar `nome` e `FUNDAMENTACAO*` diretamente na
regra.**

**O que a decisão preserva.** Nada nela toca a distinção que sustenta o P2:
`nome` continua **fora** da chave material e `FUNDAMENTACAO*` continua **dentro**.
Renomear segue sendo incapaz de dissolver um grupo de igualdade material, e
diferenciar fundamentação segue sendo capaz — o que muda é quem tem competência
para o ato, não o que o ato faz.

**O que ela custa, e vale dizer.** Editar a regra é destrutivo: o valor que o
operador de fato viu deixa de ser consultável como catálogo e sobrevive apenas em
`data/raw/`, imutável, e no histórico do git. O conjunto foi criado justamente
para evitar isso. A decisão aceita esse custo para `nome` e `FUNDAMENTACAO*`, e
**não** o estende a campo nenhum: alterar critério aferido continua passando pelo
conjunto, como a revogação da Decisão 9 e o grupo `policial-civil-alinea-masculina`
demonstram.

**Consequência executada, e ela não é automática.** Duas disposições repousavam
na premissa que esta decisão derruba, e as duas foram reavaliadas uma a uma:

- a `regra-0078` no `achado-0017` encaminhava a correção de
  `fundamentacao_integral` a quem responde pelo produto. Passou a `corrigida` —
  o campo cita a alínea "a" da LC 51/1985 e `dispositivos:` acompanhou;
- a `regra-0061` e a `regra-0062` no `achado-0021` esperavam decisão sobre uma
  citação de provisão inexistente. Passaram a `corrigida`, com o campo esvaziado.

A `regra-0084` foi reavaliada **e continua encaminhada**, e é o caso que mostra
por que a reavaliação é trabalho e não efeito: autorização para reescrever não é
conhecimento do que escrever. Ela é `sexo: AMBOS`, e qual citação a corrige
depende de um provimento judicial não localizado.

## 12. Decisão 11 — critério que o Sisprev diferencia sozinho no cadastro sai do `nome`

**Fonte:** ata da reunião com a empresa (Sisprev) de 13 de agosto de 2026. É
esclarecimento institucional sobre **capacidade do sistema**, não decisão da
auditoria — a auditoria registra e aplica a consequência sobre a gramática de
`nome`.

A empresa esclareceu que `nome` idêntico não é, por si, obstáculo à seleção
quando o critério que discriminaria as candidatas é um dado que **o próprio
Sisprev já lê do cadastro do requerente** nos passos seguintes à escolha —
ele filtra ou separa automaticamente, sem depender do rótulo. Nesses casos,
manter o critério fora do nome **facilita** a escolha do operador em vez de
prejudicá-la: agrupar sob um nome comum reduz a lista às hipóteses que de
fato dependem de leitura humana, e o sistema resolve o resto sozinho depois.

Isso inverte, para os critérios alcançados, a leitura que sustentou a
Decisão 9 e a correção descrita no [`achado-0020`](../../okf/regras-sisprev/achados/achado-0020.md)
D2 e no [`achado-0029`](../../okf/regras-sisprev/achados/achado-0029.md): ali
"nome idêntico exige abrir o cadastro para saber qual é qual" foi tratado como
o dano a corrigir. A empresa esclarece que, quando é o **Sisprev** que abre o
cadastro sozinho — e não o operador —, isso deixa de ser dano.

### O que a decisão alcança, hoje

Confirmados na ata, dois critérios:

- **`sexo`** — o Sisprev diferencia MASCULINO/FEMININO automaticamente pelo
  cadastro nos passos seguintes à seleção da regra.
- **grau de deficiência** (grave/moderada/leve) — mesma leitura; hoje só
  aparece no nome do grupo `regra-0059`–`0064`, sem coluna própria no
  catálogo (a lacuna que o `achado-0020` §Q2 já registrava).

Levantado na mesma reunião, mas **sem confirmação equivalente**: **causa da
incapacidade**. Hoje nenhum `nome` do catálogo carrega esse critério — não há
o que reverter —, mas fica registrado aqui para que, se e quando a causa
entrar como faceta de nome, a mesma pergunta ("o sistema diferencia sozinho?")
seja feita antes de decidir se ela nomeia ou não.

A lista **não é fechada por dedução**: só entra aqui o que a ata confirma
critério a critério. Um campo novo de anamnese não migra para esta lista por
analogia — exige a mesma confirmação institucional que estes dois tiveram.

### O que muda na gramática (posição 4)

A tabela do `okf/spec/regra.md` § "A gramática" ganha uma condição negativa na
posição 4 (critério aferido): **entra no nome quando discrimina E o Sisprev
não o diferencia sozinho pelo cadastro**. `sexo` e grau de deficiência saem da
posição 4 para os grupos que só se distinguiam por eles; onde outro critério
(trilho de cálculo, marco de ingresso, recorte de carreira) já discrimina, o
nome permanece como está — a decisão não introduz duplicidade nova, só deixa
de forçar uma distinção que o operador não precisa ler.

### O que a decisão não faz

- **Não altera `sexo` nem `tipo_calculo` nem nenhuma coluna de critério
  aferido.** Só o rótulo muda; o dado gravado, a fundamentação e o vínculo em
  `dispositivos:` continuam exatamente como estavam. É a mesma fronteira que a
  Decisão 10 já traçava para `nome`: editável in loco, nunca substancial.
- **Não dissolve grupo `P2_IGUALDADE_MATERIAL_ATIVA`.** `nome` segue fora da
  chave material; regras materialmente distintas por sexo continuam distintas
  no cadastro, só deixam de anunciar a distinção no rótulo.
- **Não reabre a Q10** (`AMBOS`/vazio) nem a Decisão 9 fora do que está
  listado acima — pensão por morte, onde sexo já era faceta por razão própria
  (marcar citação sem lastro, `achado-0056`), não é alcançada: ali sexo não é
  critério que discrimina candidatas, é o próprio defeito sob investigação, e
  apagá-lo do nome esconderia o que o `achado-0056` existe para mostrar.
- **Não afirma que a lista completa de critérios auto-diferenciáveis esteja
  levantada.** É premissa expressa e derrotável, como a Q2/Q10 da Decisão 7:
  toda conclusão que dependa dela cita esta decisão, e uma resposta futura da
  empresa a ajusta sem invalidar o que não depende dela.

### Execução

`nome` das regras cujo único critério de posição 4 era `sexo` e/ou grau de
deficiência perde essas facetas; onde as duas coexistiam com outro critério
que já discrimina (nenhum caso hoje), só a faceta redundante sai. Cada regra
tocada registra a mudança em `disposicao_de_achados`, para o achado que a
alcançava (`achado-0020` e/ou `achado-0029`): a disposição `corrigida`
daquela rodada de renomeação passa a `nao_se_aplica` para o par
sexo/nome especificamente, porque a alegação de dano que o achado fazia sobre
*esse* par deixou de proceder à luz do esclarecimento da empresa — sem negar
que as demais dimensões daqueles achados (D1, D3, D4, D5 do `achado-0020`;
trilho de cálculo do `achado-0029`) seguem corrigidas como estavam.

### Extensão (2026-08-13): o mesmo vale para pares que só diferem por integralidade/proporcionalidade

Mesma reunião, mesmo princípio, um critério adicional: quando duas regras têm
**exatamente o mesmo conjunto de requisitos de posição 1–4** e diferem só no
resultado `integral`/`proporcional` (posição 5), a preferência é **preencher
a coluna própria** (`integral: S`/`N`, que já existe e já é gravada regra a
regra) e **unificar o nome**, em vez de usar o rótulo para carregar a
distinção. É a mesma lógica de sexo e grau de deficiência: o Sisprev não
precisa que o operador escolha entre a variante integral e a proporcional
pelo nome — o sistema resolve a partir do que está gravado.

**Isso não se aplica por decreto a todo par com `integral` oposto.** Só
qualifica o par cujo nome, removida a faceta de resultado, fica **idêntico**
— sinal de que nenhum outro critério (trilho de cálculo, `tipo_calculo`,
`paridade`) os distingue. Levantamento contra o catálogo em 13/08/2026:
`regra-0001`/`regra-0002` e `regra-0008`/`regra-0009` qualificam e tiveram o
nome unificado. Pares que parecem semelhantes mas também divergem em
`tipo_calculo` (`regra-0006`/`0007`, `regra-0019`/`0020`, `regra-0021`/`0022`)
**não** qualificam — ali a proporcionalidade vem empacotada com outra
diferença de cálculo, e unificar esconderia essa segunda diferença.

**Um caso não foi unificado por achar uma inconsistência de dado, não por não
qualificar.** `regra-0057`/`regra-0058` (depois de removida a faceta de sexo)
diferem só por `integral`, mas `regra-0057` grava `integral: N` com
`fundamentacao_proporcional` vazia e a única fundamentação preenchida —
`fundamentacao_integral`, idêntica à da irmã — descreve "proventos integrais".
Unificar o nome ali esconderia a pergunta em vez de resolvê-la; ficou como
`achado-0061`, aberto, para quem confere o dispositivo decidir qual campo está
errado.

## 13. O que estas decisões não resolvem

- **Q4 a Q9, Q11 e Q12 seguem abertas**, e nenhuma decisão aqui as antecipa. Em
  particular a Q6 (`integral`, `tipo_calculo` e `paridade` são independentes?)
  continua sendo o que impede fechar a leitura de vários grupos.
- **As restrições reais da tela do Sisprev** continuam não conferidas. A
  gramática de `nome` foi fixada apesar disso, por decisão expressa, e o teto de
  115 caracteres é o que a importação prova ser aceito — não o que a interface
  garante.
- **Nenhum campo deployável foi gravado**, nenhum conjunto entrou em vigor e
  nenhuma regra foi promovida. As decisões definem como a auditoria propõe e
  registra; a adoção é ato do titular do produto.
