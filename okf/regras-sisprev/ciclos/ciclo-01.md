---
type: Ciclo
id: ciclo-01
numero: 1
nome: Incapacidade e invalidez — continuidade histórica
data: 2026-08-01
regras:
  - regra-0001
  - regra-0002
  - regra-0004
  - regra-0006
  - regra-0007
  - regra-0008
  - regra-0009
  - regra-0019
  - regra-0020
  - regra-0021
  - regra-0022
referencias:
  - regra-0003
  - regra-0005
---

# Ciclo 1 — Incapacidade e invalidez — continuidade histórica

> **Estado:** em execução — S0 e S1 concluídas; S2 pendente. Este arquivo é a
> fonte única do plano, das decisões, do diário de execução e do relatório
> final do ciclo.

## Identificação

- Data de abertura: 01/08/2026
- Commit de origem do plano: `e17b6e45af763160e70aa6f259d2f98c8ffd08e6`
- Commit-base da execução: `79a112562a7a9172b9cda484f3ac4f6bf5b6853f`
- Issue de execução: [#89](https://github.com/franklinbaldo/sisprev/issues/89)
- PR da S0: [#92](https://github.com/franklinbaldo/sisprev/pull/92)
- Merge da S0: `1393314118fad67e0057ee29d5c8740d01b71283`
- PR da S1: [#93](https://github.com/franklinbaldo/sisprev/pull/93)
- Responsável pelas decisões jurídicas: Franklin Baldo
- Data de fechamento:
- Commit de fechamento:

O ciclo encerra por critério material de aceite, não pelo fim do dia nem pela
mera análise das regras legadas.

## Contexto acadêmico e histórico

O benefício atravessa três desenhos normativos: invalidez nas redações
anteriores do art. 40 da Constituição; invalidez sob a EC 41/2003, a EC 70/2012
e a LCE 432/2008; e incapacidade permanente sob a EC 103/2019 e a LCE
1.100/2021.

A auditoria deve distinguir mudança terminológica, alteração de cálculo, regra
de transição e direito adquirido. A mera existência histórica de uma redação
não prova que a regra correspondente deva permanecer ativa para concessões
atuais. Da mesma forma, a ausência de uma hipótese no catálogo legado não prova
que ela seja juridicamente inexistente.

## Dimensão social

A regra selecionada define a proteção de renda de quem não pode continuar no
trabalho. Erros de janela, causa, integralidade, cálculo ou paridade podem gerar
benefício menor que o devido, pagamento maior sem fundamento ou decisão
impossível de explicar.

Por isso, a unidade de validação é a cadeia entre os fatos do requerente, a
classe médico-jurídica, a regra selecionada, o cálculo e o reajuste. O ciclo só
termina quando essa cadeia estiver coberta para todas as combinações
juridicamente possíveis do escopo.

## Objetivo

Entregar um conjunto ativo de regras que represente, de forma correta, completa
e explicável, as aposentadorias por incapacidade permanente e as hipóteses
históricas de invalidez pertencentes ao escopo.

Para isso, o ciclo deve:

1. conferir as 11 regras legadas proprietárias;
2. desativar regras materialmente erradas;
3. criar regras substitutas quando a hipótese jurídica continuar existindo;
4. registrar `sem substituta` quando a hipótese for juridicamente inexistente;
5. criar regras novas para lacunas preexistentes do catálogo; e
6. demonstrar cobertura completa, sem lacunas nem sobreposições injustificadas.

O produto não é um relatório paralelo. O produto é o catálogo corrigido, os
conceitos autorais necessários e a conclusão registrada neste arquivo.

## Critério de fechamento

Aplica-se
[`docs/spec/criterio-fechamento-ciclos.md`](../../../docs/spec/criterio-fechamento-ciclos.md).
O Ciclo 1 somente poderá ser encerrado quando:

- nenhuma regra sabidamente errada permanecer ativa;
- toda desativação tiver substituta suficiente ou registro fundamentado de
  `sem substituta — hipótese juridicamente inexistente`;
- toda combinação juridicamente possível estiver coberta por regra ativa;
- toda lacuna preexistente identificada tiver regra nova com ID próprio;
- combinações juridicamente impossíveis estiverem fundamentadas;
- não houver sobreposição não intencional;
- não houver pendência aberta que afete cobertura; e
- derivados, validadores, testes e CI estiverem íntegros.

## Decisões semânticas consolidadas

A fonte vigente é
[`docs/spec/decisoes-semanticas-regra.md`](../../../docs/spec/decisoes-semanticas-regra.md).
Os pontos abaixo não são perguntas abertas:

1. **Um ramo por regra.** Integral e proporcional são unidades distintas.
2. **`integral: S`.** Significa apenas ausência de proporcionalização pelo tempo
   de contribuição.
3. **`tipo_calculo`.** Referencia uma `FormaCalculo`; fórmulas e nomes novos
   podem ser parametrizados.
4. **`DATA_DIREITO_APOS`.** É inclusivo e se refere à implementação de todos os
   requisitos.
5. **`DATA_ADM_APOS`.** É inclusivo e se refere ao ingresso no serviço público,
   com a posse como marco do cargo efetivo.
6. **IDs estáveis.** Um ID legado não será reaproveitado para hipótese
   juridicamente diferente.
7. **Cobertura não se limita ao legado.** Hipótese existente nunca cadastrada
   recebe regra nova com origem `lacuna preexistente`.
8. **Causa não informada não é causa comum.** Ausência ou insuficiência de prova
   produz avaliação indeterminada, nunca enquadramento automático no ramo
   residual.
9. **Ausência de campo não elimina o predicado.** Requisito juridicamente
   verificável continua modelável e deve ser tratado como aferição humana quando
   não couber nas 27 colunas do legado.

Reabrir qualquer desses pontos exige proposta expressa de revisão, evidência
nova e identificação do impacto.

## Escopo

### Regras proprietárias

- Bloco A — CF/88 original e EC 20/1998: `regra-0001`, `regra-0002` e
  `regra-0004`.
- Bloco B — EC 41/2003, EC 70/2012 e LCE 432/2008: `regra-0006` a
  `regra-0009`.
- Bloco C — EC 103/2019 e LCE 1.100/2021: `regra-0019` a `regra-0022`.

### Fora de escopo

- validar integralmente regras de pensão;
- criar coluna ou tabela deployável para causa da incapacidade;
- implementar motor, telas ou banco do Sisprev;
- alterar regra de outro ciclo sem ampliação expressa do escopo; e
- promover observação mecânica a conclusão jurídica sem cotejo autoral.

## Insumos

A execução deve conferir as fontes primárias quando a decisão depender delas e
partir, entre outros, dos seguintes registros:

- `docs/analysis/reconciliacao-invalidez-incapacidade.md`;
- `docs/analysis/base-normativa-invalidez-incapacidade.md`;
- `docs/analysis/conferencia-criterio-dispositivo-invalidez-0006-0009.md`;
- `docs/analysis/conferencia-criterio-dispositivo-incapacidade-restantes.md`;
- `docs/analysis/q6-causa-incapacidade.md`;
- `docs/analysis/semantica-das-janelas-temporais.md`;
- `docs/analysis/ciclo-1-findings.md`;
- `docs/spec/regra.md`;
- `docs/spec/criterio-fechamento-ciclos.md`;
- RFCs 0001, 0002, 0004 e 0008;
- dispositivos em `okf/dispositivos/`; e
- achados autorais já existentes.

Antes de criar achado novo, deve-se verificar se a mesma unidade de investigação
já está coberta.

## Cotejo jurídico

### T1 — Ramos de fundamentação — decidido

O catálogo auditado adota uma regra por ramo. Regra proporcional precisa de
fundamento próprio para a proporcionalização. Linha legada que empacota os dois
resultados deve ser decomposta antes da validação.

### T2 — Fronteiras inferiores — decidido

`DATA_DIREITO_APOS` e `DATA_ADM_APOS` são inclusivos. O que permanece para os
blocos é verificar o lastro jurídico dos valores concretos, inclusive:

- 15/12/1998 e 16/12/1998;
- 30/12/2003, 31/12/2003 e 01/01/2004; e
- 18/10/2021 e o valor cadastrado 23/10/2021.

### T3 — Vocabulário das causas — decidido na S1

A causa da incapacidade é um **predicado da hipótese jurídica**. Não se confunde
com o resultado (`integral`, `tipo_calculo`, `paridade`) nem com o fato concreto
apurado no processo do requerente.

O vocabulário controlado mínimo do ciclo é:

- `acidente_em_servico`;
- `molestia_profissional`;
- `doenca_grave_catalogada` — doença grave, contagiosa ou incurável
  especificada ou catalogada na norma aplicável; e
- `causa_comum` — demais casos que não preencham nenhuma classe qualificada.

`causa_nao_informada`, `prova_insuficiente` e `classificacao_indeterminada` são
estados da avaliação, não classes jurídicas. Nenhum deles autoriza presumir
`causa_comum`.

A lista de doenças individuais é taxonomia versionada pela norma aplicável, não
uma série obrigatória de regras. Uma regra pode admitir um conjunto de classes
de causa quando todas conduzirem aos mesmos requisitos e efeitos. A
granularidade mais fina somente é necessária quando a distinção alterar a
hipótese aplicável, o resultado jurídico ou for escolhida expressamente para
tornar a aferição explicável.

#### Teste de materialidade da causa

A causa é material em determinado regime quando, mantidos os demais
discriminantes, sua alteração puder modificar pelo menos um destes elementos:

1. elegibilidade ou ramo jurídico aplicável;
2. integralidade ou proporcionalidade;
3. forma ou base de cálculo;
4. paridade ou regime de reajuste; ou
5. combinação normativa que precisa ser coberta separadamente na matriz.

Diferença apenas de rótulo, redação ou citação não torna a causa material. Meio
de prova ou protocolo de constatação diferente deve ser registrado, mas não
cria sozinho outra regra se os critérios e efeitos forem os mesmos.

#### Relação com Q6

A S1 fecha **Q6-R para a auditoria**: o predicado de causa integra a matriz e a
unidade auditada mesmo sem coluna correspondente no legado. Q6-S e Q6-T
permanecem dependências operacionais localizadas: ainda é preciso saber como o
Sisprev obtém, registra e classifica o fato do requerente, inclusive o nexo do
acidente em serviço e da moléstia profissional e a vigência do rol de doenças.

Essas dependências não impedem a auditoria jurídica das combinações, mas
impedem afirmar seleção automática ou reproduzível em produção enquanto não
forem resolvidas. Em regra `simulavel: S`, duas hipóteses materialmente
diferentes que só se distinguam por prosa não podem ser consideradas
automaticamente selecionáveis.

### T4 — Resultado admissível — decidido na S1

Cada regra legada recebe exatamente uma situação no resultado do ciclo:

- `conferida_sem_alteracao`;
- `corrigida_mantida_ativa`;
- `desativada_substituida`;
- `desativada_sem_substituta`; ou
- `pendente_dependencia_localizada`.

As quatro primeiras são situações finais. `pendente_dependencia_localizada` é
somente estado intermediário e não pode sobreviver ao fechamento quando afetar
a cobertura.

#### Critério entre correção e substituição

A regra pode ser `corrigida_mantida_ativa` apenas quando continuar representando
a mesma hipótese material: mesmo benefício, regime, janelas, conjunto de causas
admitidas, ramo integral ou proporcional, forma de cálculo, paridade/reajuste e
demais predicados relevantes. Correção de rótulo, transcrição, remissão,
fundamentação ou valor que apenas restitua a hipótese já representada pode ficar
no mesmo ID, observada a autoridade para gravar o campo.

Se a correção trocar a hipótese material, misturar ou separar hipóteses, mudar
predicado ou efeito jurídico, a regra legada deve ser
`desativada_substituida`. O ID e o histórico permanecem; a hipótese válida passa
a unidades novas com identidade própria.

`desativada_sem_substituta` somente cabe quando a combinação representada for
juridicamente impossível ou inexistente. Falta de prova, silêncio da planilha,
duplicidade aparente ou dependência externa não bastam.

A substituição pode ser 1:1, 1:N ou N:1. Ela só é considerada completa quando o
conjunto de destinos cobre todo o escopo material válido das origens. Não se
ativa substituição parcial que deixe uma classe ou janela sem cobertura.

#### Registro mínimo do resultado

Cada linha de “Resultado por regra” deve registrar:

1. situação T4;
2. hipótese material reconhecida;
3. decisão e alterações;
4. fontes e achados;
5. cobertura resultante;
6. substitutas ou fundamento de `sem substituta`; e
7. dependências e risco residual.

Uma pendência localizada deve ainda identificar a pergunta exata, a evidência
faltante, quem pode fornecê-la e quais combinações ficam bloqueadas.

### T5 — Regras ausentes — decidido na S1

A detecção de lacunas parte da norma, não do catálogo legado nem da planilha da
PGE. A ausência de uma linha nesses artefatos é indício; só existe lacuna quando
uma combinação juridicamente possível, demonstrada por fonte aplicável, não é
coberta por nenhuma regra ativa.

#### Unidade da matriz

Cada combinação deve registrar, conforme material no regime:

- regime constitucional e legal;
- janela de ingresso;
- janela de implementação do direito;
- conjunto admissível de classes de causa;
- ramo integral ou proporcional;
- forma de cálculo;
- paridade e regime de reajuste; e
- outros discriminantes que alterem elegibilidade ou resultado.

A matriz é **constrangida pelas normas**. Não se produz produto cartesiano cego
de todos os valores; cada linha nasce de uma hipótese normativa demonstrável.

#### Protocolo de detecção

Para cada bloco:

1. derivar das fontes primárias as combinações candidatas;
2. marcar como `juridicamente_impossivel` a combinação incompatível, com
   fundamento expresso;
3. mapear cada combinação possível para regras ativas;
4. classificar o mapeamento:
   - zero regras: `lacuna`;
   - uma regra suficiente: `coberta`;
   - mais de uma regra: `sobreposicao`, a justificar ou eliminar;
5. criar ou relacionar as unidades necessárias; e
6. repetir o mapeamento até não restarem lacunas nem sobreposições
   injustificadas.

A presença de regra legada não prova que a combinação exista. A ausência de
regra legada ou de hipótese na planilha da PGE também não prova lacuna. A
conclusão exige fonte normativa e mapeamento de cobertura.

#### Origem das regras novas

Toda regra nova recebe uma origem material:

- `substituicao` — cobre escopo válido de uma ou mais regras legadas
  desativadas; ou
- `lacuna_preexistente` — cobre combinação válida que nunca teve antecedente no
  catálogo.

A origem não será inventada como nova coluna das 27 colunas legadas. Ela deve
ser registrada neste ciclo e, quando a unidade auditada for criada, em seu
metadado de auditoria ou manifesto de cobertura.

Regra de `lacuna_preexistente` aponta para a combinação que passou a cobrir,
nunca para uma antecessora artificial. Substituição N:1 pode declarar múltiplas
origens legadas; substituição 1:N deve declarar o grupo completo de destinos.

### Bloco A — CF/88 original e EC 20/1998

O bloco deve decidir a sobrevivência jurídica das regras históricas, seus ramos
integral e proporcional, a forma de cálculo, a paridade, as classes de causa e
as fronteiras de 1998 e 2003.

### Bloco B — EC 41/2003, EC 70/2012 e LCE 432/2008

O bloco deve separar regra geral e transição do art. 6º-A, individualizar causas
e ramos, conferir cálculo e reajuste e corrigir citações constitucionais e
janelas temporais.

### Bloco C — EC 103/2019 e LCE 1.100/2021

O bloco deve conferir o marco de 2021, as coortes de ingresso, as classes de
causa, os ramos de cálculo, a paridade e os dispositivos dos §§ 13 e 14 do art.
30\.

## Fluxo processual

As sessões são sequenciais. Cada uma parte da `main` resultante da anterior e
entrega uma PR revisável.

### S0 — Linha de base — concluída na PR #92

Inventariar as 11 regras, achados, dispositivos, formas de cálculo, precedentes,
fontes e candidatos iniciais a lacuna, sem decidir mérito.

### S1 — Causa, resultados e regras ausentes — concluída na PR #93

Fechar T3, T4 e T5: vocabulário de causa, teste de materialidade, resultados
admissíveis e protocolo para substituição ou criação por lacuna.

### S2 — Bloco A

Auditar `regra-0001`, `regra-0002` e `regra-0004`, consultando `regra-0003` e
`regra-0005` apenas como referências.

### S3 — Bloco B

Auditar `regra-0006` a `regra-0009`, incluindo regra geral, art. 6º-A, causas,
ramos, cálculo, reajuste, citações e janelas.

### S4 — Bloco C

Auditar `regra-0019` a `regra-0022`, incluindo o marco de 2021, coortes de
ingresso, causas, cálculo, paridade e dispositivos dos §§ 13 e 14 do art. 30.

### S5 — Consistência e resolução de pendências

Comparar os três blocos, harmonizar o tratamento das mesmas hipóteses, resolver
pendências transversais e devolver ao bloco proprietário o que exigir
reabertura.

### S6 — Fechamento

Somente começa com zero pendências ou lacunas que afetem cobertura. Deve
consolidar:

- resultado de cada regra legada;
- mapa de substituições e registros sem substituta;
- inventário `combinação descoberta → regra nova`;
- matriz final de cobertura;
- combinações impossíveis fundamentadas; e
- gates técnicos.

### Ordem e contrato das sessões

1. S0 e S1 são sequenciais.
2. S2, S3 e S4 também são sequenciais.
3. Uma sessão só começa depois do merge da anterior.
4. PR de bloco edita apenas suas regras proprietárias, dispositivos, formas de
   cálculo, achados necessários, este arquivo e derivados oficiais.
5. Decisões e fontes devem ser registradas neste arquivo ou no conceito autoral
   diretamente afetado, nunca apenas em conversa ou comentário de PR.
6. Questão externa localizada não paralisa as demais regras do bloco.
7. S5 inventaria e dá disposição a toda pendência remanescente.
8. S6 exige zero pendências e zero lacunas materiais.

### Registro das sessões

- [x] S0 — concluída; PR #92; commit-base
  `79a112562a7a9172b9cda484f3ac4f6bf5b6853f`; fechamento
  `1393314118fad67e0057ee29d5c8740d01b71283`.
- [x] S1 — concluída; PR #93; commit-base
  `1393314118fad67e0057ee29d5c8740d01b71283`; fechamento a preencher no merge.
- [ ] S2 — não iniciada; PR: —; commit-base: —; fechamento: —.
- [ ] S3 — não iniciada; PR: —; commit-base: —; fechamento: —.
- [ ] S4 — não iniciada; PR: —; commit-base: —; fechamento: —.
- [ ] S5 — não iniciada; PR: —; commit-base: —; fechamento: —.
- [ ] S6 — não iniciada; PR: —; commit-base: —; fechamento: —.

## Entregável

O ciclo deve produzir, numa única cadeia rastreável:

1. este arquivo preenchido com decisões e resultados;
2. regras corretas mantidas ou criadas e regras erradas desativadas;
3. mapa de substituições e registros fundamentados de `sem substituta`;
4. inventário `combinação descoberta → regra nova`;
5. matriz final de cobertura e combinações impossíveis;
6. dispositivos e formas de cálculo necessários;
7. achados autorais sem duplicação;
8. derivados sincronizados; e
9. CI integralmente verde.

## Registro da S0 — Linha de base

A S0 foi executada sobre o commit
`79a112562a7a9172b9cda484f3ac4f6bf5b6853f`. Ela registra o estado recebido e
não decide sobrevivência jurídica, não escolhe qual campo cede em contradição e
não cria regra nova.

### Estado global recebido

- As 11 regras proprietárias estão ativas no legado e têm
  `validado_pge: FALSE` e `validado_presidencia: FALSE`.
- Nove regras possuem `dispositivos:`; `regra-0021` e `regra-0022` não possuem
  vínculos porque o texto atual achata causas alternativas.
- Há precedentes SEI vinculados a `regra-0006`, `regra-0007` e `regra-0008`.
- “Lacuna” abaixo significa combinação sem cobertura demonstrada, não conclusão
  de que uma regra nova já seja devida.

### Inventário

| Regra  | Estado recebido                                                                              | Achados centrais               | Fontes disponíveis                                    | Decisão reservada ao bloco                                            |
| ------ | -------------------------------------------------------------------------------------------- | ------------------------------ | ----------------------------------------------------- | --------------------------------------------------------------------- |
| `0001` | CF/88 original; integral; `Valor Efetivo`; paridade; direito até 15/12/1998                  | `0015`; `0020` quanto ao nome  | CF/88 original; publicação da EC 20; análises de base | sobrevivência histórica, causa, cálculo e fronteira superior          |
| `0002` | mesma janela; proporcional; texto apenas no ramo integral                                    | `0009`; `0015`; `0020`         | mesmas da `0001`                                      | existência e fundamento do proporcional; cálculo e fronteira          |
| `0004` | EC 20; `sexo` e `integral` vazios; cálculo não identificado; dois ramos no mesmo texto       | `0008`; `0053` improcedente    | art. 40, § 1º, I, EC 20; publicação da emenda         | decomposição, cálculo, sexo e janelas                                 |
| `0006` | EC 41/LCE 432; integral; média; sem paridade; causas e ramos agrupados                       | `0022`; `0025`; `0026`; `0049` | CF/EC 41; LCE 432; ECE 146; SEI `0031.117501/2020-19` | causa, fecho em 2024, inciso constitucional e moléstia profissional   |
| `0007` | mesma janela; proporcionalidade em dias; sem paridade                                        | `0022`; `0025`; `0026`; `0049` | mesmas da `0006`; SEI `0029.237532/2020-34`           | fundamento proporcional, causa, fórmula e fecho                       |
| `0008` | art. 6º-A/EC 70; ingresso até 2003; integral; paridade                                       | `0022`; `0025`; `0026`; `0049` | EC 70; LCE 432; ECE 146; SEI `0016.000495/2024-83`    | causa, fecho em 2024, última remuneração e inciso correto             |
| `0009` | mesma janela; proporcional; paridade; mesma forma de cálculo da integral                     | `0022`; `0025`; `0026`; `0049` | mesmas da `0008`                                      | existência e fórmula do proporcional; fundamento e causa comum        |
| `0019` | LCE 1.100; ingresso até 2003; integral; `Valor Efetivo`; paridade; início 23/10/2021         | `0024`; `0025`                 | EC 103; arts. 25, 27-I e 30; compilação DITEL         | início em 18/10/2021, § 13 e relação entre causa e cálculo            |
| `0020` | mesma janela; proporcionalidade em dias; paridade; texto integral                            | `0009`; `0020`; `0024`         | mesmas da `0019`                                      | saber se a combinação existe; fundamentar ou desativar sem substituta |
| `0021` | ingresso desde 01/01/2004; proporcional; sem paridade; causas qualificadas no texto integral | `0009`; `0024`; `0026`; `0050` | arts. 24, 26, 27-II e 30, § 14; compilação DITEL      | causa comum, fundamento próprio, início em 18/10/2021 e vínculos      |
| `0022` | mesma janela; integral; média; sem paridade; três causas achatadas                           | `0024`; `0025`; `0026`; `0050` | arts. 24, 27-II e 30, § 13; compilação DITEL          | corrigir artigos, decompor causas e autorar §§ 13/14                  |

### Correção documental produzida na S0

O `achado-0024` foi estreitado. `DATA_ADM_APOS` é inclusivo; portanto,
`01/01/2004` está alinhado ao texto “após 31/12/2003” e não cria lacuna de
ingresso.

Permanece o defeito de `data_direito_apos: 23/10/2021`. A LCE 1.100/2021 foi
publicada e entrou em vigor em 18/10/2021, sem produção diferida identificada
para o art. 30.

### Combinações sem cobertura demonstrada

A S0 entrega à investigação, sem antecipar o resultado:

1. os regimes da CF/88 original e da EC 20/1998, ausentes do modelo to-be da
   PGE;
2. a hipótese 8 ausente da numeração da planilha da PGE;
3. a combinação proporcional com paridade representada por `regra-0020`, sem
   contraparte naquela planilha;
4. a classe “moléstia profissional”, citada nos dois regimes estaduais, mas não
   definida por eles;
5. os pares `0006/0007`, `0008/0009` e `0021/0022`, nos quais a causa que muda o
   resultado não é predicado estruturado; e
6. as classes pós-2003 agrupadas em `0021/0022`, sem unidades individualmente
   auditáveis por causa.

Cada item deverá terminar como combinação coberta por regra correta, combinação
juridicamente impossível fundamentada, substituição de regra legada ou lacuna
preexistente preenchida por regra nova.

### Critério de saída da S0

- [x] As 11 regras foram inventariadas.
- [x] Cada regra possui população de achados conhecida.
- [x] Cada regra possui fontes normativas ou precedentes relacionados.
- [x] Candidatos a lacuna foram separados de conclusões jurídicas.
- [x] Nenhuma regra deployável foi alterada.

## Registro da S1 — Contratos transversais

A S1 foi executada sobre o commit
`1393314118fad67e0057ee29d5c8740d01b71283`. Ela não decide o mérito de nenhuma
das 11 regras e não altera regra deployável.

### Fontes efetivamente cotejadas

- `docs/analysis/q6-causa-incapacidade.md`;
- `docs/spec/regra.md`;
- `docs/spec/criterio-fechamento-ciclos.md`;
- RFC 0004;
- `cf88/art-40-inc-i/original`; e
- `cf88/art-40-par-1-inc-i/ec-41-2003`.

As duas redações constitucionais confirmam o discriminante entre causas
qualificadas e demais casos. A S1 não universaliza esse efeito para os regimes
posteriores: cada bloco deverá conferir sua própria norma aplicável.

### Decisões produzidas

- T3 fecha o vocabulário de causa e o teste de materialidade.
- T4 fecha as situações admissíveis e o limite entre correção e substituição.
- T5 fecha a matriz normativa, o teste de lacuna e a origem das regras novas.
- Q6-R está fechado para a auditoria; Q6-S e Q6-T permanecem dependências
  operacionais localizadas.
- Nenhum achado novo foi criado: ausência de predicado estruturado, moléstia
  profissional e pares indistinguíveis já estão cobertos pelos achados
  existentes.

### Repasse aos blocos

- S2 deve construir a matriz do regime histórico sem presumir que ausência no
  modelo da PGE seja lacuna.
- S3 deve aplicar as quatro classes à regra geral e ao art. 6º-A, verificando
  se causas qualificadas podem compartilhar uma unidade.
- S4 deve derivar diretamente dos §§ 13 e 14 do art. 30 as combinações
  pós-2021 e decidir a existência de `regra-0020`.
- Todo bloco deve registrar zero, uma ou múltiplas regras por combinação antes
  de encerrar.

### Critério de saída da S1

- [x] Vocabulário mínimo de causa fechado.
- [x] Ausência de informação separada de causa comum.
- [x] Teste de materialidade fechado.
- [x] Situações T4 e registro mínimo definidos.
- [x] Protocolo de lacuna e sobreposição definido.
- [x] Origem `substituicao` e `lacuna_preexistente` definida sem alterar o
  schema legado.
- [x] Nenhuma regra deployável foi alterada.

## Resultado por regra

Preencher durante S2–S4 com situação T4, decisão, alterações, fontes, achados,
dependências e, quando cabível, substitutas ou `sem substituta`.

- [ ] `regra-0001`
- [ ] `regra-0002`
- [ ] `regra-0004`
- [ ] `regra-0006`
- [ ] `regra-0007`
- [ ] `regra-0008`
- [ ] `regra-0009`
- [ ] `regra-0019`
- [ ] `regra-0020`
- [ ] `regra-0021`
- [ ] `regra-0022`

### Regras novas sem antecedente legado

Preencher para cada lacuna preexistente:

- [ ] combinação jurídica; regra nova; bloco proprietário; fontes; fundamento da
  ausência no catálogo anterior.

## Referências de outros ciclos

- `regra-0003` — consultar somente para fronteiras históricas e sobreposição com
  invalidez; a validação integral pertence ao Ciclo 2.
- `regra-0005` — consultar somente para fronteiras históricas e coerência do
  instituto; a validação integral pertence ao Ciclo 2.

## Fontes legais consultadas

Registrar somente fontes efetivamente abertas durante as sessões de mérito, com
uma versão e a data relevantes. A prioridade é:

- Constituição e emendas no Planalto;
- LCE 432/2008 e LCE 1.100/2021 na compilação oficial de Rondônia;
- EC estadual 146/2021 e sua publicação oficial;
- atos e registros oficiais do IPERON;
- jurisprudência primária do STF e do TJRO; e
- normas oficiais sobre doença catalogada, acidente em serviço e moléstia
  profissional.

Fontes efetivamente utilizadas:

- Constituição Federal, art. 40, I, redação original, vigente de 05/10/1988 a
  15/12/1998;
- Constituição Federal, art. 40, § 1º, I, redação da EC 41/2003, vigente de
  31/12/2003 a 12/11/2019; e
- fontes metodológicas e autorais relacionadas no registro da S1.

## Pendências que permanecem abertas

- P-1 — sobrevivência das regras anteriores às reformas;
- P-2 — fronteira da regra geral da EC 41/2003 perante o art. 6º-A;
- P-3/P-4 — citação ao art. 40, § 1º, III, em regras de invalidez;
- P-5 — fundamentação pós-2003 de `regra-0021` e `regra-0022`;
- P-6 — definição normativa de moléstia profissional;
- Q6-S — obtenção e persistência da causa no caso concreto;
- Q6-T — classificação, nexo e vigência do rol aplicável;
- lastro dos marcos temporais históricos;
- dispositivos de cálculo e paridade dos regimes de 1988 e 1998; e
- rol de doenças aplicável a cada período.

Q6-S e Q6-T não impedem construir a matriz jurídica, mas impedem afirmar
seleção automática e reproduzível em produção. Nenhuma pendência acima pode
permanecer no encerramento se afetar a cobertura.

## Conclusão do ciclo

- [x] T1 e T2 estão decididas e documentadas.
- [x] T3, T4 e T5 foram fechadas na S1.
- [ ] Todas as regras proprietárias receberam situação final.
- [ ] Nenhuma regra materialmente errada permanece ativa.
- [ ] Toda desativação possui substituta ou `sem substituta` fundamentado.
- [ ] Toda lacuna preexistente possui regra nova.
- [ ] A matriz demonstra cobertura completa e combinações impossíveis.
- [ ] Sobreposições foram eliminadas ou justificadas.
- [ ] Não existe pendência aberta que afete cobertura.
- [ ] `dispositivos:` corresponde às fundamentações resultantes.
- [ ] Nenhum ID foi reaproveitado para hipótese distinta.
- [ ] Derivados foram regenerados.
- [ ] Validadores, testes e CI passaram.
- [ ] A issue #89 foi encerrada com a PR de fechamento.
