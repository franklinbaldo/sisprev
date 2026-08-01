# Questões semânticas — leituras medidas e decisões consolidadas

> **Atualização de 2026-08-01:** Q2, o núcleo de Q6 e Q7 foram respondidas
> diretamente pela coordenação da auditoria. As seções correspondentes deixam de
> registrar “leituras prováveis” e passam a registrar decisões vigentes. A fonte
> normativa consolidada é
> [`docs/spec/decisoes-semanticas-regra.md`](../spec/decisoes-semanticas-regra.md).

## 1. Como ler este documento

O catálogo continua útil para medir padrões e formular perguntas melhores, mas
medição não substitui uma resposta institucional. Quando a coordenação responde,
a medição passa a ser evidência de consistência ou de aplicação — não motivo
para manter a pergunta aberta.

As decisões de 2026-08-01 têm três efeitos de processo:

1. agentes futuros não devem redescobrir a semântica desses campos;
2. ciclos não podem usar Q2, Q6 ou Q7 como gate geral; e
3. dúvidas remanescentes devem ser formuladas sobre uma regra, um valor ou uma
   integração concreta.

Todas as medições mencionadas abaixo usam `data/raw/regras-sisprev.csv` e os
dispositivos autorados. A importação é imutável.

## 2. Q4 — o Sisprev devolve uma regra ou várias candidatas?

**Leitura: várias candidatas. Medido, confiança alta.**

Agrupando as regras pelos critérios plausivelmente parametrizados — benefício,
`sexo`, `tipo`, `apos_especial` e as quatro datas —, há grupos que contêm mais
de uma regra; o maior tem seis. Os campos estruturados disponíveis não
determinam sempre uma regra única.

A conclusão operacional permanece: o simulador deve trabalhar com candidatas e
nunca declarar compatibilidade total apenas porque uma linha não foi excluída.
O Sisprev pode usar critério fora do CSV ou deixar o desempate para análise
manual; distinguir essas duas hipóteses continua sendo questão de integração.

## 3. Q5 — onde vivem requisitos não representados no CSV?

**Leitura: em tabela externa, ao menos para pontuação progressiva; em análise
manual ou outra estrutura para o restante. Parcialmente medido.**

`TabelaPontuacao` funciona como ponteiro para comportamento externo ao CSV. O
padrão mais consistente é tabela progressiva: o art. 5º da ECE 146/2021 contém
somatório que cresce por ano; faixas fixas não exigem a mesma tabela.

O art. 8º da ECE 146/2021 e o art. 41 da LCE 1.100/2021 possuem faixas fixas de
66, 76 e 86 pontos. A divergência de `TabelaPontuacao` entre esses grupos é
candidata a defeito e permanece coberta pelo `achado-0054`.

Para idade mínima, tempo de contribuição, pedágio, atividade policial, causa da
incapacidade e exposição especial, a ausência de coluna não prova ausência de
automação. Continua necessário identificar tabela, código, outra tela ou etapa
manual responsável por cada requisito.

## 4. Q6 — `integral`, `tipo_calculo` e `paridade`

**Estado: semântica central respondida.**

### `integral`

`integral: S` significa exclusivamente que o provento **não é
proporcionalizado pelo tempo de contribuição**.

Não significa:

- última remuneração;
- integralidade constitucional;
- paridade;
- ausência de média; ou
- provento igual à remuneração do cargo.

A ocorrência de `integral: S` com `Valor Médio` é coerente com essa definição:
a média pode ser a base de um provento sem redução proporcional por tempo.

### `tipo_calculo`

Os rótulos legados são **referências para formas de cálculo**. A fórmula e seus
componentes vivem no conceito `FormaCalculo`, não no texto isolado do enum.

A parametrização pode:

- reutilizar uma forma já existente;
- criar uma nova forma quando o caso não estiver coberto; e
- renomear um cálculo ambíguo e configurar o Sisprev para o novo nome.

Logo, a auditoria não deve inferir fórmula completa de rótulos como `Valor
Médio` ou `Proporcionalidade Dias`, nem preservar ambiguidade apenas porque ela
existe no legado.

### `paridade`

`paridade` permanece uma dimensão distinta da forma de cálculo inicial. Ela
trata do regime de reajuste/manutenção do benefício e não altera o significado
de `integral`.

A discussão jurídica sobre quais combinações são permitidas por cada regra
continua sendo mérito; o significado dos três campos não é mais pergunta
aberta.

## 5. Q2 — `DATA_DIREITO_APOS` e `DATA_ADM_APOS`

**Estado: respondida para as fronteiras inferiores.**

As duas colunas `APOS` discutidas são **inclusivas**:

- `DATA_DIREITO_APOS = X`: todos os requisitos do direito podem ser
  implementados em X ou depois de X;
- `DATA_ADM_APOS = X`: o ingresso no serviço público pode ocorrer em X ou
  depois de X; para cargo efetivo, o marco é a posse.

A leitura anterior que tratava `DATA_ADM_APOS` como exclusivo está superada.
Não se grava o último dia do regime anterior para simular uma comparação
estrita; grava-se o primeiro dia coberto.

`DATA_DIREITO_APOS` não representa requerimento, protocolo ou concessão. A
medição do catálogo é consistente com essa resposta: quando a coluna coincide
com a vigência da norma, ela grava o próprio dia de início, nunca a véspera.

A semântica não precisa ser confirmada novamente no Sisprev para que a auditoria
avance. O que ainda deve ser conferido é se cada **valor concreto** tem lastro
na norma aplicável.

## 6. Q7 — fundamentações integral e proporcional na mesma linha

**Estado: capacidade do legado confirmada; modelagem alvo decidida.**

O Sisprev permite duas formas de parametrização:

1. uma regra com `FUNDAMENTACAO_INTEGRAL` e
   `FUNDAMENTACAO_PROPORCIONAL`, selecionando o texto do ramo aplicável; ou
2. regras separadas, uma integral e outra proporcional.

O catálogo auditado escolhe a segunda forma:

> **uma regra representa um único ramo de resultado.**

Uma linha legada que empacota os dois ramos deve ser decomposta. Integral e
proporcional sempre produzem resultados distintos e o ramo proporcional contém
ao menos o elemento jurídico que autoriza a proporcionalização.

Portanto:

- `integral: N` com texto apenas no ramo integral não é mais uma ambiguidade a
  tolerar; é caso de conferência e correção/decomposição;
- a presença dos dois textos numa linha não bloqueia o trabalho; orienta a
  decomposição; e
- a decisão vale para `regra-0002`, `regra-0004`, `regra-0020`, `regra-0021`
  e qualquer outro caso equivalente.

## 7. Q8 — pares que diferem no resultado

A decisão de um ramo por regra elimina a hipótese de representar integral e
proporcional como modos invisíveis da mesma unidade auditada. Se duas hipóteses
produzem ramos diferentes, elas são unidades separadas no catálogo auditado,
ainda que tenham origem na mesma linha legada.

Permanece manual a identificação do predicado ou fato que conduz a cada ramo e a
conferência de que a projeção para o Sisprev é executável. O que não permanece
aberto é a escolha de modelagem.

## 8. Q9 — campos de comportamento e colunas sem variância

**Leitura: parcialmente medida.**

`TabelaPontuacao` é condição/ponteiro para estrutura externa;
`SIMULAVEL` é controle de execução/interface. As colunas sem variância no
catálogo — `TIPO_REMUN`, `Requisitos da IN Nº 5/2020`,
`ADICIONAL_INATIVIDADE`, `Relatório p/ Reserva Remunerada por Idade ex-officio`,
`VISIVEL DTC PROPORCIONAL` e `VISIVEL DTC INTEGRAL` — não discriminam nenhuma
regra na população atual.

Isso sustenta a leitura de flags dormentes ou capacidades não exercitadas, mas
não permite concluir, sem informação do Sisprev, se são campos mortos.

A ausência de visibilidade na DTC não torna a fundamentação irrelevante: o campo
continua deployável e pode aparecer em outro ato ou fluxo. Apenas impede afirmar
sem evidência que a DTC é o local exato de materialização do texto.

## 9. Q10 — `AMBOS`, vazio, desconhecido e não aplicável

**Leitura vigente: vazio é “não gravado”.**

`sexo` vazio coocorre com `integral` vazio e `tipo_calculo: Não identificado` em
um conjunto estável de regras. O padrão é compatível com linha incompleta ou
histórica, não com três decisões semânticas independentes.

Vazio permanece pendência, nunca `AMBOS` presumido nem “não aplicável” por
silêncio.

## 10. Q11 e Q12 — ainda abertas

O catálogo não informa de forma completa:

- quais documentos são exigidos para cada requisito manual; e
- a fronteira institucional entre correspondência automática, conferência
  manual dos fatos e validação jurídica da configuração.

Essas duas questões continuam sem leitura suficiente. Nenhuma conclusão da
auditoria deve inventar a resposta.

## 11. Perguntas que ainda valem levar ao IPERON

As perguntas úteis são agora específicas:

1. onde e como o motor obtém requisitos que não aparecem no CSV;
2. o que o sistema faz quando mais de uma regra passa pelos filtros;
3. onde os textos de fundamentação são apresentados ou consumidos;
4. como a causa da incapacidade é obtida, persistida e classificada; e
5. quais campos dormentes são capacidades válidas e quais estão descontinuados.

Não devem voltar à pauta como perguntas abertas:

- o significado de `integral`;
- a relação conceitual entre `tipo_calculo` e `FormaCalculo`;
- a possibilidade de parametrizar novas formas de cálculo;
- a inclusividade de `DATA_DIREITO_APOS` e `DATA_ADM_APOS`; ou
- a escolha de um ramo por regra no modelo auditado.

## 12. Regra para trabalhos futuros

As decisões consolidadas são aplicadas até revisão expressa. Uma evidência nova
pode justificar mudança, mas a divergência deve indicar:

- qual decisão está sendo contestada;
- qual evidência nova a derrota;
- quais regras, achados e ciclos seriam afetados; e
- como a documentação será migrada.

Sem isso, reabrir Q2, Q6 ou Q7 é regressão documental, não prudência.