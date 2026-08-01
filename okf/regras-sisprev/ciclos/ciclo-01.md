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

> **Estado:** em execução — S0 concluída; S1 pendente. Este arquivo é a fonte
> única do plano, das decisões, do diário de execução e do relatório final do
> ciclo.

## Identificação

- Data de abertura: 01/08/2026
- Commit de origem do plano: `e17b6e45af763160e70aa6f259d2f98c8ffd08e6`
- Commit-base da execução: `79a112562a7a9172b9cda484f3ac4f6bf5b6853f`
- Issue de execução: [#89](https://github.com/franklinbaldo/sisprev/issues/89)
- PR da S0: [#92](https://github.com/franklinbaldo/sisprev/pull/92)
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
- RFCs 0001, 0002 e 0008;
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

### T3 — Vocabulário das causas — S1

A S1 deve fechar o vocabulário mínimo e o teste de materialidade para:

- acidente em serviço;
- moléstia profissional;
- doença grave, contagiosa ou incurável catalogada em lei; e
- causas comuns ou demais casos.

A lista de doenças individuais é taxonomia, não uma série de regras.

### T4 — Resultado admissível — S1

Cada regra legada deve terminar em uma destas situações:

- conferida sem alteração;
- corrigida e mantida ativa, sem mudança de identidade material;
- desativada e substituída;
- desativada sem substituta, por hipótese juridicamente inexistente; ou
- pendente durante a execução por dependência externa localizada.

A pendência é intermediária e não pode chegar ao fechamento quando afetar a
cobertura.

### T5 — Regras ausentes — S1

Para cada combinação juridicamente possível, deve existir regra ativa
suficiente. Combinação possível sem regra constitui lacuna e exige regra nova
com origem `lacuna preexistente`.

Regras novas devem registrar uma destas origens:

- `substituição`, quando sucedem regra legada desativada; ou
- `lacuna preexistente`, quando não possuem antecessora no catálogo.

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

### S1 — Causa, resultados e regras ausentes

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
  `79a112562a7a9172b9cda484f3ac4f6bf5b6853f`; fechamento a preencher no merge.
- [ ] S1 — não iniciada; PR: —; commit-base: —; fechamento: —.
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
a versão e a data relevantes. A prioridade é:

- Constituição e emendas no Planalto;
- LCE 432/2008 e LCE 1.100/2021 na compilação oficial de Rondônia;
- EC estadual 146/2021 e sua publicação oficial;
- atos e registros oficiais do IPERON;
- jurisprudência primária do STF e do TJRO; e
- normas oficiais sobre doença catalogada, acidente em serviço e moléstia
  profissional.

Fontes efetivamente utilizadas:

- A preencher durante S1–S5.

## Pendências que permanecem abertas

- P-1 — sobrevivência das regras anteriores às reformas;
- P-2 — fronteira da regra geral da EC 41/2003 perante o art. 6º-A;
- P-3/P-4 — citação ao art. 40, § 1º, III, em regras de invalidez;
- P-5 — fundamentação pós-2003 de `regra-0021` e `regra-0022`;
- P-6 — definição normativa de moléstia profissional;
- Q6-S/Q6-T — obtenção, persistência, classificação e vigência da causa;
- lastro dos marcos temporais históricos;
- dispositivos de cálculo e paridade dos regimes de 1988 e 1998; e
- rol de doenças aplicável a cada período.

Nenhuma pendência acima pode permanecer no encerramento se afetar a cobertura.

## Conclusão do ciclo

- [x] T1 e T2 estão decididas e documentadas.
- [ ] T3, T4 e T5 foram fechadas na S1.
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
