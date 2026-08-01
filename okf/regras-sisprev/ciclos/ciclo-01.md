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

> **Estado:** planejado. Este arquivo é simultaneamente o plano, o diário de
> decisões e o relatório final do ciclo. Análises anteriores são insumos de
> investigação, não conclusões que possam ser copiadas automaticamente para as
> regras.

## Identificação

- Data de abertura prevista: 01/08/2026
- Critério temporal: a data marca a abertura; o ciclo encerra por critério de
  aceite, não pelo fim do dia.
- Commit de origem: `e17b6e45af763160e70aa6f259d2f98c8ffd08e6`
- Issue de execução: [#89](https://github.com/franklinbaldo/sisprev/issues/89)
- Responsável pelas decisões jurídicas: Franklin Baldo
- Responsável pela autoria dos registros: auditor humano, ainda que a pesquisa,
  a conferência e os testes sejam assistidos por agentes.
- Data de fechamento:
- Commit de fechamento:

## Objetivo do ciclo

Determinar, para cada uma das 11 regras proprietárias, se o catálogo representa
corretamente:

1. o regime constitucional e legal aplicável;
2. a janela temporal de ingresso e de implementação do direito;
3. a classe de causa da incapacidade juridicamente relevante;
4. o ramo integral ou proporcional;
5. a base de cálculo e o regime de reajuste;
6. a fundamentação e os dispositivos efetivamente citados; e
7. a situação da regra no catálogo após a auditoria.

O produto não é uma nova análise paralela. O produto é o próprio catálogo
corrigido, os achados autorais necessários e o resultado consolidado neste
arquivo.

## Premissas já decididas

1. **Fonte única.** O plano e o relatório do ciclo permanecem neste arquivo. A
   issue serve apenas para rastrear execução e PRs.
2. **Detecção não é conclusão.** Contradições, sobreposições e igualdades
   materiais iniciam investigação; não autorizam, sozinhas, correção,
   inativação ou escolha de uma regra como canônica.
3. **Schema do catálogo mantido.** A causa da incapacidade não ganhará nova
   coluna deployável. A direção adotada em Q6 é representar uma linha por
   **classe de causa material** — acidente em serviço, moléstia profissional,
   doença catalogada em lei ou causa comum — quando a classe alterar
   elegibilidade, cálculo ou fundamentação.
4. **`nome` é interface humana, não identidade material.** A distinção entre
   linhas deve aparecer nos campos de domínio e na fundamentação, não apenas no
   rótulo.
5. **IDs são estáveis.** Nenhum ID existente será reaproveitado para hipótese
   juridicamente diferente. Se a decomposição exigir novas regras, elas recebem
   novos IDs; eventual inativação de regra anterior exige conclusão e
   justificativa próprias.
6. **Vínculo segue citação.** O campo `dispositivos:` registra o que a regra
   efetivamente cita. Um dispositivo citado pode revelar fundamentação errada e,
   ainda assim, o vínculo só muda quando o texto da fundamentação mudar.
7. **Promoção de auditoria é consequência.** Nenhuma regra será marcada como
   `revisada` ou `validada` antes de cumprir os contratos do RFC 0001 e registrar
   as questões semânticas obrigatórias no próprio arquivo da regra.

## Escopo

### Regras proprietárias

- CF/88 original e EC 20/1998: `regra-0001`, `regra-0002`, `regra-0004`.
- EC 41/2003, EC 70/2012 e LCE 432/2008: `regra-0006` a `regra-0009`.
- EC 103/2019 e LCE 1.100/2021: `regra-0019` a `regra-0022`.

### Referências transversais

`regra-0003` e `regra-0005` serão consultadas somente quando ajudarem a testar
continuidade histórica, fronteiras temporais ou coerência do instituto. A
avaliação completa delas pertence ao Ciclo 2.

### Fora de escopo

- validar integralmente regras de pensão;
- criar nova coluna ou tabela deployável para causa da incapacidade;
- implementar o motor de seleção, telas ou banco do Sisprev;
- refazer análises históricas já existentes sem uma pergunta concreta;
- promover automaticamente uma observação mecânica a achado ou conclusão;
- resolver Q6-S — obtenção e persistência da causa no requerimento — sem
  evidência do Sisprev real.

## Insumos já disponíveis

A execução deve partir do que já foi pesquisado, conferindo a fonte primária
quando a decisão depender dela:

- `docs/analysis/reconciliacao-invalidez-incapacidade.md`;
- `docs/analysis/base-normativa-invalidez-incapacidade.md`;
- `docs/analysis/conferencia-criterio-dispositivo-invalidez-0006-0009.md`;
- `docs/analysis/conferencia-criterio-dispositivo-incapacidade-restantes.md`;
- `docs/analysis/q6-causa-incapacidade.md`;
- `docs/analysis/semantica-das-janelas-temporais.md`;
- `docs/analysis/ciclo-1-findings.md`;
- RFCs 0001, 0002 e 0008;
- dispositivos já transcritos em `okf/dispositivos/`;
- achados já existentes, especialmente os que tratam de campos vazios,
  fundamentação colocada no ramo errado e janelas temporais.

Antes de criar achado novo, deve-se conferir se a mesma unidade de investigação
já está coberta. O ciclo complementa achados existentes; não multiplica
registros sobre o mesmo defeito.

## Contexto acadêmico e histórico

O benefício atravessa três desenhos normativos: invalidez nas redações
anteriores do art. 40 da Constituição; invalidez sob a EC 41/2003, a EC 70/2012
e a LCE 432/2008; e incapacidade permanente sob a EC 103/2019 e a LCE
1.100/2021. A auditoria deve separar mudança terminológica, mudança de cálculo,
regra de transição e direito adquirido. Vigência formal de um dispositivo não
prova, por si, sua aplicação atual a um caso.

## Dimensão social

A regra selecionada define proteção de renda para quem não pode continuar no
trabalho. Erros de janela, causa, integralidade, média ou paridade podem produzir
concessão menor que a devida, concessão maior sem fundamento ou impossibilidade
de explicar a decisão. Por isso a unidade de validação não é apenas o texto da
lei: é a cadeia verificável entre fato do requerente, classe médico-jurídica,
regra selecionada, cálculo e reajuste.

## Questões transversais que devem ser decididas primeiro

Nenhuma correção de mérito nas regras deve começar antes de estas questões serem
resolvidas ou convertidas em dependência externa explicitamente documentada.

### T1 — Semântica dos ramos de fundamentação

Fixar a relação entre `integral`, `fundamentacao_integral` e
`fundamentacao_proporcional` — a Q7 já identificada. A decisão deve explicar:

- se uma regra pode carregar os dois ramos;
- qual campo deve fundamentar uma regra marcada como `integral: N`;
- como tratar `regra-0002`, `regra-0020` e `regra-0021`, cujo único texto
  disponível descreve o ramo integral; e
- quando uma única linha deve ser dividida em duas, como pode ocorrer com
  `regra-0004`.

**Gate T1:** não corrigir esses três casos por mera inferência enquanto a
semântica não estiver registrada.

### T2 — Semântica e valores das janelas temporais

Concluir a semântica ainda aberta de `DATA_DIREITO_APOS` e cotejar as fronteiras
com a vigência e as transições aplicáveis. A decisão deve alcançar, no mínimo:

- `15/12/1998` e `16/12/1998`;
- `30/12/2003`, `31/12/2003` e `01/01/2004`;
- `18/10/2021` e o valor cadastrado `23/10/2021`;
- a diferença entre data de ingresso, implementação dos requisitos, fato
  gerador, concessão e vigência da redação normativa.

**Gate T2:** nenhuma data será ajustada apenas para alinhar intervalos; cada
marco precisa de uma função jurídica declarada.

### T3 — Vocabulário de classes de causa

Aplicar a direção A de Q6 sem criar schema novo. Antes de decompor linhas,
registrar o vocabulário mínimo e a evidência de que cada classe produz efeito
jurídico distinto:

- acidente em serviço;
- moléstia profissional;
- doença grave, contagiosa ou incurável catalogada em lei; e
- causas comuns ou demais casos.

A lista de doenças individuais permanece taxonomia Q6-T, não uma série de
regras. A existência do predicado no catálogo não resolve como o fato do
requerente é obtido ou persistido no Sisprev real.

### T4 — Resultado admissível por regra

Cada regra deve terminar o ciclo em exatamente uma destas situações:

- **conferida sem alteração**;
- **corrigida**;
- **inativada com conclusão, justificativa e substituição identificável**; ou
- **pendente por dependência externa**, com a pergunta, a evidência faltante, o
  responsável pela obtenção e o efeito preciso sobre a regra.

“Não analisada” ou “parece correta” não são resultados de encerramento.

## Cotejo jurídico

### Bloco A — CF/88 original e EC 20/1998

Regras: `regra-0001`, `regra-0002` e `regra-0004`.

Perguntas de decisão:

1. As regras representam situações de direito adquirido já implementado antes
   de cada reforma, alguma transição expressa ou outra hipótese juridicamente
   sobrevivente? A mera data de ingresso não basta.
2. Quais dispositivos fundam paridade e base de cálculo nos regimes de 1988 e
   1998?
3. Qual lei especificava as doenças graves no período e qual era sua vigência?
4. `regra-0004` deve permanecer como linha não discriminada ou ser decomposta
   nos ramos integral e proporcional?
5. As janelas cadastradas correspondem ao critério jurídico decidido em T2?

Saída do bloco: matriz de aplicabilidade histórica e decisão individual sobre as
três regras, sem presumir que regra antiga deva permanecer ativa apenas porque a
redação existiu no passado.

### Bloco B — EC 41/2003, EC 70/2012 e LCE 432/2008

Regras: `regra-0006` a `regra-0009`.

Perguntas de decisão:

1. Qual é a fronteira entre a regra geral e o grupo protegido pelo art. 6º-A da
   EC 41/2003?
2. A leitura “após 2003” das regras gerais é juridicamente confirmada ou apenas
   inferida por exclusão da transição?
3. Qual dispositivo correto substitui, se for o caso, a citação ao art. 40,
   § 1º, III, da Constituição, que trata de aposentadoria voluntária?
4. Os arts. 17, 20, 45 e 62 da LCE 432/2008 sustentam os critérios específicos
   de cálculo e reajuste gravados em cada linha?
5. Como as quatro classes de causa se materializam sem produzir linhas que
   diferem apenas pelo `nome`?

Saída do bloco: pares geral/transição com fundamentação compatível com o ramo
integral ou proporcional e com a classe de causa representada.

### Bloco C — EC 103/2019 e LCE 1.100/2021

Regras: `regra-0019` a `regra-0022`.

Perguntas de decisão:

1. Em `regra-0020` e `regra-0021`, o campo `integral: N` está correto e a
   fundamentação foi copiada do ramo integral, ou o valor gravado é que está
   errado? Aplicar a decisão T1, não escolher por aparência.
2. `regra-0021` e `regra-0022`, destinadas ao ingresso após 2003, devem citar
   os arts. 24, 26 e 27, II, em vez dos arts. 25 e 27, I?
3. O art. 30, caput, deve integrar a fundamentação das quatro regras como
   discriminante geral entre integral e proporcional?
4. Os §§ 13 e 14 do art. 30 precisam ser transcritos para fechar o roteamento do
   cálculo?
5. Existe fonte normativa ou administrativa que defina “moléstia profissional”
   no RPPS-RO? Se não, registrar P-6 como dependência real, sem equipará-la por
   suposição a contaminação acidental.
6. Como decompor as linhas por classe de causa mantendo IDs estáveis e criando
   IDs novos apenas para hipóteses novas?
7. Qual é o fundamento do marco `23/10/2021`?

Saída do bloco: regras pós-reforma coerentes quanto a ingresso, causa, cálculo,
paridade, fundamentação e dispositivos.

## Fluxo processual

### Fase 0 — congelar a linha de base

- [ ] Registrar o commit efetivamente usado para iniciar a execução.
- [ ] Montar neste arquivo a matriz
  `regra → regime → janela → causa → integralidade → cálculo → paridade → fundamentação → dispositivos`.
- [ ] Relacionar os achados já abertos que alcançam cada regra.
- [ ] Executar os detectores apenas para registrar fatos mecânicos atuais.

### Fase 1 — fechar as decisões transversais

- [ ] Resolver T1 ou documentar dependência externa.
- [ ] Resolver T2 ou documentar dependência externa.
- [ ] Fixar o vocabulário e o teste de materialidade de T3.
- [ ] Registrar a forma de resultado de T4.

**Gate:** somente depois desta fase começam as edições de mérito nas regras.

### Fase 2 — auditar o Bloco A

- [ ] Conferir fontes primárias e jurisprudência de aplicabilidade histórica.
- [ ] Decidir `regra-0001`.
- [ ] Decidir `regra-0002`.
- [ ] Decidir `regra-0004` e eventual decomposição.
- [ ] Atualizar ou criar achados somente quando houver unidade de investigação
  ainda não coberta.

### Fase 3 — auditar o Bloco B

- [ ] Conferir regra geral, transição do art. 6º-A e LCE 432/2008.
- [ ] Decidir `regra-0006` e `regra-0007`.
- [ ] Decidir `regra-0008` e `regra-0009`.
- [ ] Corrigir citações incompatíveis somente depois de identificar a base
  normativa correta.
- [ ] Aplicar a decomposição por classe de causa quando juridicamente material.

### Fase 4 — auditar o Bloco C

- [ ] Transcrever dispositivos faltantes indispensáveis, com fonte e vigência.
- [ ] Decidir `regra-0019` e `regra-0020`.
- [ ] Decidir `regra-0021` e `regra-0022`.
- [ ] Corrigir o ramo temporal e o regime de cálculo/reajuste.
- [ ] Aplicar a direção A de Q6 e criar novos IDs apenas quando necessários.
- [ ] Registrar a dependência relativa a moléstia profissional se a pesquisa não
  localizar definição primária suficiente.

### Fase 5 — consolidar o catálogo

- [ ] Editar apenas os arquivos OKF autorais correspondentes.
- [ ] Garantir que `dispositivos:` reflita a fundamentação resultante.
- [ ] Atualizar o resultado por regra neste arquivo.
- [ ] Listar fontes efetivamente consultadas e pendências remanescentes.
- [ ] Não deixar conclusão relevante apenas em `docs/analysis/`, comentário de
  PR ou conversa.

### Fase 6 — validar e encerrar

- [ ] Regenerar artefatos com `uv run python scripts/gerar_indices.py`.
- [ ] Executar `uv run python scripts/validar_regras.py`.
- [ ] Executar a suíte de testes e os demais gates definidos no CI.
- [ ] Conferir que a regeneração não deixou diff derivado inesperado.
- [ ] Submeter a PR do ciclo com resumo das decisões, riscos residuais e teste
  por regra.
- [ ] Encerrar a issue #89 somente após preencher a conclusão deste arquivo.

## Entregável

O ciclo deve produzir, numa única cadeia rastreável:

1. este arquivo preenchido com decisões e resultados;
2. regras corrigidas ou justificadamente mantidas;
3. novos dispositivos apenas quando indispensáveis e conferidos em fonte
   primária;
4. achados autorais novos ou atualizados, sem duplicação;
5. artefatos derivados sincronizados; e
6. CI integralmente verde.

Não será criado relatório paralelo do ciclo.

## Matriz inicial de trabalho

| Regra        | Regime representado                    | Papel cadastrado atual                             | Decisão central do ciclo                                        |
| ------------ | -------------------------------------- | -------------------------------------------------- | --------------------------------------------------------------- |
| `regra-0001` | CF/88 original                         | integral, paridade, Valor Efetivo                  | aplicabilidade histórica, causa qualificada, cálculo e paridade |
| `regra-0002` | CF/88 original                         | proporcional, mas texto no ramo integral           | aplicar T1 e confirmar base do proporcional                     |
| `regra-0004` | EC 20/1998                             | ramos não discriminados; campos estruturais vazios | decidir decomposição, cálculo, paridade e janelas               |
| `regra-0006` | EC 41/2003 + LCE 432                   | integral                                           | fronteira temporal, causa e correção da citação constitucional  |
| `regra-0007` | EC 41/2003 + LCE 432                   | proporcional                                       | T1, base proporcional e fronteira temporal                      |
| `regra-0008` | art. 6º-A/EC 70 + LCE 432              | integral                                           | transição expressa, causa e base de cálculo                     |
| `regra-0009` | art. 6º-A/EC 70 + LCE 432              | proporcional                                       | T1, causa comum e base proporcional                             |
| `regra-0019` | EC 103 + LCE 1.100, ingresso até 2003  | integral, paridade                                 | classe de causa, cálculo por integralidade e dispositivo geral  |
| `regra-0020` | EC 103 + LCE 1.100, ingresso até 2003  | proporcional, texto integral                       | T1, base proporcional e classes indevidamente citadas           |
| `regra-0021` | EC 103 + LCE 1.100, ingresso após 2003 | proporcional, sem paridade, texto integral         | T1, ramo temporal, arts. 26/27-II e decomposição por causa      |
| `regra-0022` | EC 103 + LCE 1.100, ingresso após 2003 | média, sem paridade                                | arts. 24/27-II, causa qualificada e decomposição                |

## Resultado por regra

Preencher cada linha com uma das situações de T4 e resumir: decisão, alterações,
fontes, achados e dependências.

- [ ] `regra-0001` — situação; decisão; alterações; fontes; pendências/achados.
- [ ] `regra-0002` — situação; decisão; alterações; fontes; pendências/achados.
- [ ] `regra-0004` — situação; decisão; alterações; fontes; pendências/achados.
- [ ] `regra-0006` — situação; decisão; alterações; fontes; pendências/achados.
- [ ] `regra-0007` — situação; decisão; alterações; fontes; pendências/achados.
- [ ] `regra-0008` — situação; decisão; alterações; fontes; pendências/achados.
- [ ] `regra-0009` — situação; decisão; alterações; fontes; pendências/achados.
- [ ] `regra-0019` — situação; decisão; alterações; fontes; pendências/achados.
- [ ] `regra-0020` — situação; decisão; alterações; fontes; pendências/achados.
- [ ] `regra-0021` — situação; decisão; alterações; fontes; pendências/achados.
- [ ] `regra-0022` — situação; decisão; alterações; fontes; pendências/achados.

## Referências de outros ciclos

Estas regras aparecem apenas para cotejo transversal; sua avaliação completa
permanece no ciclo proprietário.

- `regra-0003` — conferir somente fronteiras históricas e sobreposição com
  invalidez, quando pertinente.
- `regra-0005` — conferir somente fronteiras históricas e sobreposição com
  invalidez, quando pertinente.

## Fontes legais consultadas

Registrar somente fontes efetivamente abertas durante a execução, com a versão e
a data relevante. Prioridade:

- Constituição e emendas no Planalto;
- LCE 432/2008 e LCE 1.100/2021 na compilação oficial de Rondônia;
- EC estadual 146/2021 e seu ato oficial de publicação;
- atos, manuais ou registros oficiais do IPERON para prática administrativa;
- jurisprudência primária do STF e do TJRO para direito adquirido, transições,
  cálculo, paridade e enquadramento das causas;
- normas oficiais que definam doença catalogada, acidente em serviço e moléstia
  profissional.

Fontes efetivamente utilizadas:

- A preencher durante a execução.

## Pendências que permanecem abertas

Na abertura, permanecem como questões de investigação, não como conclusões:

- T1/Q7 — relação entre `integral` e os campos de fundamentação;
- T2 — semântica de `DATA_DIREITO_APOS` e marcos de 1998, 2003 e 2021;
- P-1 — sobrevivência jurídica das regras anteriores às reformas;
- P-2 — fronteira da regra geral EC 41/2003 por exclusão do art. 6º-A;
- P-3/P-4 — citação ao art. 40, § 1º, III, em regras de invalidez;
- P-5 — fundamentação pós-2003 de `regra-0021` e `regra-0022`;
- P-6 — definição normativa de moléstia profissional;
- Q6-S/Q6-T — obtenção, persistência, classificação e vigência da causa no caso
  concreto;
- fundamento do marco `23/10/2021`;
- dispositivos de paridade e base de cálculo dos regimes de 1988 e 1998;
- rol de doenças aplicável aos regimes históricos.

Ao fechar o ciclo, substituir esta lista pelas pendências realmente restantes,
com evidência faltante, responsável e impacto por regra.

## Conclusão do ciclo

- [ ] T1, T2, T3 e T4 foram decididas ou convertidas em dependências externas
  precisas.
- [ ] Todas as regras proprietárias receberam uma situação final de T4.
- [ ] Todas as regras proprietárias foram comparadas com fontes primárias
  aplicáveis.
- [ ] As correções foram registradas somente nos arquivos OKF correspondentes.
- [ ] Nenhum ID foi reaproveitado para hipótese juridicamente distinta.
- [ ] As dúvidas e os achados foram registrados sem duplicar unidades de
  investigação existentes.
- [ ] `dispositivos:` corresponde às citações da fundamentação resultante.
- [ ] As referências `regra-0003` e `regra-0005` não foram indevidamente
  tratadas como regras proprietárias deste ciclo.
- [ ] Os artefatos derivados foram regenerados.
- [ ] Os testes, validadores e demais gates do CI passaram.
- [ ] A decisão e o risco residual de cada regra estão legíveis neste arquivo.
- [ ] A issue #89 foi encerrada com link para a PR de fechamento.
