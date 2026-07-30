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

**Derrotável, como as demais.** Fechada a Q2 para invalidez ou compulsória, os
rótulos correspondentes passam a poder ser específicos, e a tabela acima é o
único lugar a alterar.

## 11. O que estas decisões não resolvem

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
