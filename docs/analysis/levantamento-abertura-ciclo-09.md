# Levantamento de abertura — Ciclo 9

**Estado:** Fase 1 — levantamento preliminar; nenhuma das 22 propostas foi
concluída, ativada ou vinculada a ato institucional nesta fase.

**Base:** `main` em `71538f7`, branch
`cycle-09-historical-invalidity-windows`.

Este documento executa o protocolo de abertura do ciclo. Ele não substitui a
auditoria jurídica das propostas, não registra validação da PGE ou aprovação do
IPERON e não resolve, por inferência, as pendências que dependem de decisão ou
de evidência externa.

## 1. Matriz preliminar de discriminantes

Os discriminantes abaixo foram levantados antes de qualquer promoção de estado
das propostas. A cardinalidade observada é a consequência da combinação desses
predicados, não uma afirmação de que a lei exija uma regra para cada combinação.

| discriminante | valores/faces identificados | onde aparece | efeito preliminar |
|---|---|---|---|
| janela constitucional | CF/88 original; EC 20/1998; EC 41/2003 — regra geral; art. 6º-A da EC 41, redação da EC 70/2012 | `predicados.regime`, datas e dispositivos | muda a norma de aquisição e a base/regime de reajuste |
| marco do direito | 05/10/1988; 16/12/1998; 31/12/2003; 20/02/2004; 13/03/2008; 01/01/2025 como fecho exclusivo | `data_direito_apos`/`ate` | separa sucessão normativa e as subfaixas de cálculo |
| ingresso para o art. 6º-A | até 31/12/2003 | `data_adm_ate` | requisito pessoal da transição; não deve ser confundido com a data do direito |
| causa da incapacidade | acidente em serviço; moléstia profissional; doença catalogada; causa comum/residual | `predicados.causa_incapacidade` e protocolo | separa ramo integral/qualificado do ramo proporcional |
| versão temporal do rol | rol vigente na data juridicamente relevante; rol estadual anterior à LCE 432; rol da LCE 432 | `versao_rol`, dispositivos e instrução | pode mudar o enquadramento entre doença catalogada e causa comum |
| ramo do benefício | integral ou proporcional | `projecao.integral` e fundamentação correspondente | muda a existência da fração e, em alguns segmentos, o tipo de cálculo |
| base de cálculo | remuneração/totalidade do cargo; média; média com limitação; base remuneratória sujeita à fração | `projecao.tipo_calculo`, fundamentação e tipo de cálculo | muda o valor inicial |
| medida da proporcionalidade | sem fração; fração anual; fração em dias | dispositivo e `projecao.tipo_calculo` | muda o cálculo do ramo comum |
| regime de reajuste | paridade; sem paridade | `projecao.paridade` e dispositivos | muda a revisão posterior dos proventos |
| sexo | ambos | `predicados.sexo`/`projecao.sexo` | não foi encontrado discriminante sexual nas famílias propostas |
| forma de seleção | causa determinada ou exclusão das causas qualificadas | `requisitos_verificacao_humana` | exige decisão positiva ou negativa documentada; ausência de prova não pode virar exclusão silenciosa |
| sobreposição entre causas qualificadas | acidente, moléstia e doença podem ser alegados simultaneamente | ainda não há regra de precedência | precisa de decisão operacional para que as classes não produzam seleção ambígua |

### Cardinalidade preliminar

| família material | causas representadas | subfaixas de direito | destinos atuais |
|---|---|---|---:|
| CF/88 original | quatro causas | uma | 4 |
| EC 20/1998 | quatro causas | uma | 4 |
| EC 41 — regra geral | três causas qualificadas em duas subfaixas; causa comum em três subfaixas | antes/depois da MP 167/2004 e antes/depois da LCE 432/2008 | 9 |
| art. 6º-A/EC 70 | três causas qualificadas em uma subfaixa; causa comum em duas subfaixas | antes/depois da LCE 432/2008 | 5 |
| **Total** |  |  | **22** |

O quadro descreve a decomposição já autorada. A quantidade não é, por si só,
decisão jurídica: “uma regra por causa” e “uma regra por segmento de cálculo”
são decisões de modelagem que precisam permanecer distintas da norma que
define os efeitos.

## 2. Inventário preliminar da evidência operacional

O catálogo legado alcança todas as sete origens do ciclo e registra-as como
presentes no sistema. A evidência abaixo é a que o catálogo permite afirmar;
ela não prova como o motor, a instrução ou o ato concessório executam cada
hipótese.

| origem | população descrita | valores gravados | simulável | evidência operacional útil | limite do que se pode afirmar |
|---|---|---|---|---|---|
| `regra-0001` | ingresso até 15/12/1998; direito até 15/12/1998; integral; paridade | `Valor Efetivo`, `integral: S`, `paridade: S`, ambos os sexos | N | existe enum fechado e a regra está no sistema | não há causa estruturada nem simulação demonstrada |
| `regra-0002` | mesma janela; proporcional; paridade | `Valor Efetivo`, `integral: N`, `paridade: S` | N | existe enum e ramo proporcional legado | não há medida da fração nem causa estruturada |
| `regra-0004` | ingresso até 31/12/2003; direito desde 16/12/1998 até 31/12/2003 | tipo de cálculo `Não identificado`; paridade S; campos de sexo e remuneração vazios | N | a janela e o dispositivo da EC 20 estão gravados | a projeção não identifica a forma de cálculo nem o sexo; origem marcada como inválida no nome |
| `regra-0006` | direito desde 31/12/2003; integral; sem paridade | `Valor Médio`, `integral: S`, `paridade: N`, ambos os sexos | S | a média é um valor já usado; há fundamentação para ramo qualificado e ramo comum | uma única origem mistura causas e não tem predicado de causa |
| `regra-0007` | mesma janela; proporcional; sem paridade | `Proporcionalidade Dias`, `integral: N`, `paridade: N` | S | a fração em dias é um valor já usado | a distinção da causa não existe como campo e os textos integral/proporcional coexistem |
| `regra-0008` | ingresso até 31/12/2003; direito desde 31/12/2003; integral; paridade | `Remuneração de Contribuição`, `integral: S`, `paridade: S` | S | há precedente administrativo associado e enum fechado | a fundamentação integral e a proporcional divergem quanto ao fundamento constitucional; o prazo está sentinela |
| `regra-0009` | mesma janela; proporcional; paridade | `Remuneração de Contribuição`, `integral: N`, `paridade: S` | S | enum e ramo proporcional legado existem | é indistinguível de 0008 nos demais campos e não contém causa estruturada |

Conclusões operacionais permitidas pelo inventário:

- há projeção candidata para `Valor Efetivo`, `Valor Médio`,
  `Proporcionalidade Dias` e `Remuneração de Contribuição`; portanto a ausência
  de uma coluna de causa não autoriza afirmar que o motor não possa executar a
  hipótese;
- as propostas qualificadas podem formular perguntas de homologação com base
  em origens que já estão no sistema, mesmo quando o enum ainda precisa ser
  confirmado para a fórmula histórica exata;
- a evidência não mostra se a causa está em outro cadastro, no processo
  administrativo, em regra externa ao catálogo ou no ato concessório. Essa é
  uma conferência, não uma incapacidade demonstrada;
- as propostas com `simulavel: N` preservam uma seleção que depende de prova
  administrativa ou médica. Isso é compatível com carga de homologação se
  houver pergunta, responsável, prova e momento de conferência.

Os quatro planos ainda não observáveis diretamente no catálogo — dados do
segurado, motor de cálculo, instrução administrativa e ato concessório — ficam
expressamente fora deste inventário. A Fase 2 deve procurar evidência nesses
planos antes de converter qualquer lacuna de campo em conclusão sobre o
Sisprev.

## 3. Componentes de atomicidade calculados

O cálculo foi feito usando somente `origens_legacy` das 22 propostas e a regra
da spec: propostas conectam-se quando compartilham uma origem, e a conexão é
transitiva.

| componente | origens | destinos | situação herdada |
|---:|---|---:|---|
| 1 | `regra-0001`, `regra-0002` | 4 — CF/88 original | `estado_auditoria: elaboracao`; `estado_implantacao` ausente, portanto presumido `confirmada` |
| 2 | `regra-0004` | 4 — EC 20 | `estado_auditoria: elaboracao`; `estado_implantacao` ausente, portanto presumido `confirmada` |
| 3 | `regra-0006` | 6 — EC 41, causas qualificadas | `estado_auditoria: elaboracao`; `estado_implantacao` ausente, portanto presumido `confirmada` |
| 4 | `regra-0007` | 3 — EC 41, causa comum | `estado_auditoria: elaboracao`; `estado_implantacao` ausente, portanto presumido `confirmada` |
| 5 | `regra-0008` | 3 — art. 6º-A, causas qualificadas | `estado_auditoria: elaboracao`; `estado_implantacao` ausente, portanto presumido `confirmada` |
| 6 | `regra-0009` | 2 — art. 6º-A, causa comum | `estado_auditoria: elaboracao`; `estado_implantacao` ausente, portanto presumido `confirmada` |

Os seis componentes calculados são a atomicidade operacional vigente: a spec
manda derivá-los do grafo origem↔destino, e não reutilizar a referência herdada
a três grupos como entidade concorrente. A menção a “três grupos” no documento
do ciclo é texto obsoleto, corrigido nesta PR. Não há necessidade de uma nova
decisão para tornar a carga determinável: cada componente entra quando todos os
seus destinos tiverem auditoria concluída e estado de implantação confirmado ou
confirmado com ressalva.

O estado de implantação não aparece no frontmatter das 22 propostas porque é
opcional; pela spec, a ausência presume `confirmada`. O bloqueio atual é outro:
todas as unidades ainda estão em `estado_auditoria: elaboracao`. As pendências de
projeção deverão ser resolvidas na auditoria ou, quando já houver projeção
suficiente para teste, registradas como `confirmada_com_ressalva`, sem fabricar
um bloqueio técnico inexistente.

## 4. Expressões lógicas e cenários de fronteira

### 4.1 Convenção temporal usada no levantamento

Para este levantamento foi aplicada a convenção registrada na spec de regra:

- `data_direito_apos` é inclusivo e registra o primeiro dia coberto;
- `data_direito_ate` é exclusivo e registra o primeiro dia fora da faixa;
- `data_adm_ate` é inclusivo;
- `data_adm_apos` é inclusivo e registra o primeiro dia coberto;

Assim, cada janela do direito é `[apos, ate)`. O campo temporal não deve ser
confundido com a data de requerimento: a premissa do ciclo é o direito
adquirido, que pode ser requerido posteriormente.

### 4.2 Famílias

As expressões abaixo reconstroem os predicados, sem classificar pelo nome da
regra:

**CF/88 original:** o direito foi implementado em `[05/10/1988,
16/12/1998)` **e** a incapacidade é permanente **e** ocorre uma das quatro
classes: acidente em serviço **ou** moléstia profissional **ou** doença
catalogada **ou** causa comum. Acidente, moléstia e doença catalogada levam ao
ramo integral; a causa comum leva ao ramo proporcional. A unidade exige a
prova positiva da classe escolhida ou, para a causa comum, a exclusão
documentada das três classes qualificadas.

**EC 20/1998:** o direito foi implementado em `[16/12/1998,
31/12/2003)` **e** a incapacidade é permanente **e** uma das mesmas quatro
classes está demonstrada. As três classes qualificadas são integrais e a
causa comum é proporcional.

**EC 41 — antes da MP 167/2004:** o direito foi implementado em `[31/12/2003,
20/02/2004)` **e** a incapacidade é permanente **e** uma das quatro classes
está demonstrada. A causa qualificada usa remuneração integral do cargo e a
causa comum usa a regra residual/proporcional da legislação aplicável.

**EC 41 — desde a MP 167/2004:** o direito foi implementado em `[20/02/2004,
13/03/2008)` **e** a incapacidade é permanente **e** uma das quatro classes
está demonstrada. A causa qualificada usa média sem paridade; a causa comum
usa a média e a fração anual previstas para o segmento.

**EC 41 — desde a LCE 432/2008:** o direito foi implementado em `[13/03/2008,
01/01/2025)` **e** a incapacidade é permanente **e** uma das quatro classes
está demonstrada. A causa qualificada usa média sem paridade; a causa comum
usa a base e a proporcionalidade em dias previstas para o segmento.

**Art. 6º-A da EC 41, redação da EC 70/2012:** o servidor ingressou até
31/12/2003 **e** o direito foi implementado em `[31/12/2003,
01/01/2025)` **e** a incapacidade é permanente **e** uma das quatro classes
está demonstrada. As três classes qualificadas são integrais e paritárias; a
causa comum é proporcional e paritária. Dentro da causa comum, a fração é
anual em `[31/12/2003,13/03/2008)` e em dias em `[13/03/2008,01/01/2025)`.

### 4.3 Cenários temporais obrigatórios

| marco | véspera | dia do marco | leitura preliminar |
|---|---|---|---|
| início da CF/88 original | 04/10/1988: fora | 05/10/1988: entra | não há lacuna anterior representada pelas propostas |
| EC 20/1998 | 15/12/1998: CF/88 original | 16/12/1998: EC 20 | fronteira sem sobreposição no eixo do direito |
| EC 41/2003 | 30/12/2003: EC 20 | 31/12/2003: EC 41 | o dia do marco entra na família EC 41 |
| MP 167/2004 | 19/02/2004: base anterior | 20/02/2004: média | separa remuneração integral da média |
| LCE 432/2008 | 12/03/2008: fração anual | 13/03/2008: fração em dias | separa as formas de proporcionalização |
| ECE 146/2021 | 30/12/2024: ainda alcançado | 31/12/2024: ainda alcançado | ambos entram porque o fecho é 01/01/2025 |
| fecho histórico | 31/12/2024: último dia alcançado | 01/01/2025: direito implementado fora das propostas históricas | requerimento apresentado depois ainda pode invocar direito histórico; o que fica fora é o direito implementado em 01/01/2025 ou depois |
| ingresso do art. 6º-A | 31/12/2003: entra em `data_adm_ate` | 01/01/2004: fora | a admissão é discriminante independente do direito |

### 4.4 Cenários de causa e sobreposição

- com causa positiva de acidente em serviço, a expressão qualificadora é
  satisfeita;
- com causa positiva de moléstia profissional, a expressão qualificadora é
  satisfeita;
- com diagnóstico no rol temporalmente aplicável, a expressão de doença
  catalogada é satisfeita;
- sem qualquer causa qualificada **e** com investigação suficiente para
  excluir acidente, moléstia e doença catalogada, a causa comum é satisfeita;
- com informação ausente, a causa comum não deve ser selecionada por
  default;
- com duas causas qualificadas simultâneas, mais de uma unidade pode ser
  candidata, embora o resultado econômico de várias delas coincida. Ainda não
  há, nas propostas, uma regra de precedência, multi-classificação ou
  consolidação. Este é um cenário de sobreposição intencional que precisa ser
  resolvido antes do gate de seleção;
- com doença catalogada, mas rol temporal não transcrito ou não identificado,
  não se pode concluir nem “catalogada” nem “comum” apenas pelo rótulo do
  diagnóstico.

### Resultado do levantamento lógico

As janelas de direito apresentam continuidade preliminar e os marcos principais
não deixam dia sem família no espaço histórico proposto. A afirmação de
ausência de sobreposição, porém, ainda não está resolvida no eixo das causas:
as classes qualificadas podem se sobrepor factualmente, e o tratamento dessa
situação é operacional/modelagem, não uma consequência automática dos campos
`integral` ou `tipo_calculo`.

## 5. Pendências classificadas pelo efeito

| pendência | propostas/famílias alcançadas | classificação | efeito nesta fase |
|---|---|---|---|
| fundamentar integralmente os dispositivos contra os textos legais, inclusive os vínculos em `dispositivos:` | 22 propostas | jurídica | impede concluir a auditoria enquanto não houver cotejo substantivo; extração textual não basta |
| transcrever a base estadual anterior à LC 39/1990/LC 1/1984 e os dispositivos estaduais anteriores à LCE 432/2008 | CF/88 original; EC 20; art. 6º-A | externa, com efeito jurídico | depende de fonte legal/documental identificável; sem ela a cobertura da base histórica não está demonstrada |
| transcrever e versionar os rols estaduais temporalmente aplicáveis, inclusive LC 228 e período anterior à LCE 432 | doenças catalogadas das três janelas | jurídica | impede confirmar o predicado de doença catalogada e a fronteira com causa comum |
| resolver o denominador e a medida da fração sob LC 68/1992 e legislação anterior | CF/88 original, causa comum | jurídica | impede fechar a fórmula histórica; não deve ser substituída por uma construção presumida |
| demonstrar como o IPERON trata frações de ano sob LC 228 | causa comum anterior a 13/03/2008 | operacional testável | a hipótese jurídica pode ser formulada, mas a homologação precisa de caso/procedimento verificável |
| confirmar enum/projeção da remuneração do cargo efetivo e da fórmula composta | propostas do art. 6º-A e causa comum EC 41 | operacional testável | há valores candidatos no catálogo; a pergunta é confirmável na homologação, não há incapacidade demonstrada |
| confirmar a projeção da média e da proporcionalidade em dias | propostas EC 41 | operacional testável | as origens já gravam `Valor Médio` e `Proporcionalidade Dias`; falta confirmar a correspondência da fórmula histórica |
| confirmar a projeção `Valor Efetivo` e a fidelidade do enum nas janelas antigas | CF/88 original e EC 20 | operacional testável | o enum existe nas origens; a fidelidade jurídica e o cálculo efetivo ainda precisam ser conferidos |
| resolver Q6-S/Q6-T: onde a causa é obtida, como é classificada e qual taxonomia sustenta a decisão | 22 propostas, especialmente EC 41 e art. 6º-A | externa, com efeito operacional | depende da descrição do processo/IPERON; impede declarar seleção operacional fechada, mas não autoriza afirmar incapacidade do motor |
| definir protocolo institucional para nexo de acidente e moléstia profissional | propostas dessas classes | externa | falta decisão/procedimento do IPERON; a prova exigida está descrita, mas o fluxo institucional não está fechado |
| definir o cotejo do diagnóstico com o rol e a versão do rol | propostas de doença catalogada | operacional testável | pode entrar como pergunta de homologação depois de a taxonomia legal estar disponível |
| decidir como tratar alegação simultânea de acidente, moléstia e doença catalogada | famílias qualificadas | risco residual, com possível efeito operacional | pode gerar duas candidatas; precisa de precedência, multi-rótulo ou regra de desempate antes da seleção |
| conferir completude e prontidão dos seis componentes | seis componentes | operacional testável | depende dos estados derivados; ainda não ocorreu nesta Fase 1 |
| preencher dados administrativos de processo, expediente, unidades e destinatários | relatório e manifestação | externa | não pode ser inventado; deve permanecer como pendência documental nomeada |

### Classificação resumida

Não há, no levantamento, fundamento para marcar qualquer proposta como
`pendente_mapeamento_sisprev` apenas porque a causa não é uma coluna do catálogo
ou porque a instrução é manual. Há, contudo, pendências jurídicas e externas
que impedem a conclusão da auditoria, e a correção do texto obsoleto sobre grupos. As propostas permanecem em
`estado_auditoria: elaboracao` até a Fase 2.

## Decisões que permanecem separadas

- **jurídica:** quais requisitos, causas, bases, frações, paridade e prazos a
  norma impõe;
- **de modelagem:** decompor as famílias por causa e por segmento de cálculo,
  e decidir se causas qualificadas simultâneas são multi-rótulo ou recebem
  precedência;
- **operacional:** onde a causa é obtida, quem a reconhece, qual prova é
  exigida, como o enum é conferido e em que momento a seleção é realizada.

Nenhuma dessas decisões foi convertida em validação, aprovação, assinatura,
ativação ou `estado_auditoria: concluida` neste levantamento.

## Ponto de parada

Os cinco levantamentos estão entregues para revisão. A próxima etapa só deve
começar depois da revisão da matriz, da adoção dos seis componentes, da sobreposição entre causas qualificadas e da
classificação das pendências.
