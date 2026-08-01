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

> **Estado:** pronto para execução. Este arquivo é simultaneamente o plano, o
> diário de decisões e o relatório final do ciclo. Análises anteriores são
> insumos de investigação, não conclusões que possam ser copiadas
> automaticamente para as regras.

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
5. a forma de cálculo e o regime de reajuste;
6. a fundamentação e os dispositivos efetivamente citados; e
7. a situação da regra no catálogo após a auditoria; e
8. as hipóteses juridicamente existentes que não possuem nenhuma regra no
   catálogo atual.

O produto não é uma nova análise paralela. O produto é o próprio catálogo
corrigido, os achados autorais necessários e o resultado consolidado neste
arquivo.

O ciclo só termina quando o conjunto de regras ativas estiver juridicamente
correto e cobrir integralmente o tema. Regras materialmente erradas são
desativadas. Se a hipótese jurídica continuar existindo, ela recebe regra ou
regras novas; se a hipótese for juridicamente inexistente, a desativação é
registrada como `sem substituta`, com fundamento. Hipóteses juridicamente
existentes sem qualquer antecedente no catálogo recebem regras novas, com IDs
próprios, classificadas como `lacuna preexistente`.

## Premissas e decisões já consolidadas

01. **Fonte única.** O plano e o relatório do ciclo permanecem neste arquivo. A
    issue serve apenas para rastrear execução e PRs.
02. **Detecção não é conclusão.** Contradições, sobreposições e igualdades
    materiais iniciam investigação; não autorizam, sozinhas, correção,
    inativação ou escolha de uma regra como canônica.
03. **Schema do catálogo mantido.** A causa da incapacidade não ganhará nova
    coluna deployável. A direção adotada em Q6 é representar uma linha por
    **classe de causa material** — acidente em serviço, moléstia profissional,
    doença catalogada em lei ou causa comum — quando a classe alterar
    elegibilidade, cálculo ou fundamentação.
04. **`nome` é interface humana, não identidade material.** A distinção entre
    linhas deve aparecer nos campos de domínio e na fundamentação, não apenas no
    rótulo.
05. **IDs são estáveis.** Nenhum ID existente será reaproveitado para hipótese
    juridicamente diferente. Se a decomposição exigir novas regras, elas recebem
    novos IDs; eventual inativação de regra anterior exige conclusão e
    justificativa próprias.
06. **Vínculo segue citação.** O campo `dispositivos:` registra o que a regra
    efetivamente cita. Um dispositivo citado pode revelar fundamentação errada e,
    ainda assim, o vínculo só muda quando o texto da fundamentação mudar.
07. **Promoção de auditoria é consequência.** Nenhuma regra será marcada como
    `revisada` ou `validada` antes de cumprir os contratos do RFC 0001 e registrar
    as questões semânticas obrigatórias no próprio arquivo da regra.
08. **Um ramo por regra.** Embora o Sisprev permita uma linha com fundamentações
    integral e proporcional ou duas linhas separadas, o modelo auditado adota
    uma regra para cada ramo. Uma linha legada que empacota os dois ramos é
    decomposta antes da validação.
09. **`integral` tem sentido estrito.** `integral: S` significa que o provento não
    é proporcionalizado pelo tempo de contribuição. Não significa última
    remuneração, paridade, ausência de média ou integralidade constitucional.
10. **`tipo_calculo` referencia uma forma de cálculo.** A semântica da fórmula
    vive no conceito `FormaCalculo`. Se a forma necessária não existir, ela pode
    ser criada; se o rótulo legado for ambíguo, ele pode ser renomeado e o
    Sisprev configurado para o novo nome.
11. **`DATA_DIREITO_APOS` é inclusivo.** Todos os requisitos devem estar
    implementados a partir da data gravada, incluindo o próprio dia. O campo não
    é data de requerimento, protocolo ou concessão.
12. **`DATA_ADM_APOS` é inclusivo.** O campo representa a fronteira inferior do
    ingresso no serviço público; para cargo efetivo, o marco jurídico é a posse.
13. **O objeto final é o conjunto ativo.** Nenhuma regra materialmente errada
    permanece ativa. Hipótese existente representada de modo defeituoso recebe
    regra nova com ID próprio; hipótese juridicamente inexistente é desativada
    com o registro `sem substituta`, sem criação artificial de regra.
14. **Cobertura não se limita ao legado.** Se a matriz revelar hipótese
    juridicamente existente nunca representada no catálogo, deve ser criada regra
    nova com ID próprio e origem `lacuna preexistente`, sem antecessora artificial.

A fonte consolidada dessas decisões é
[`docs/spec/decisoes-semanticas-regra.md`](../../../docs/spec/decisoes-semanticas-regra.md).
Elas não são gates pendentes deste ciclo.

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

- `docs/spec/decisoes-semanticas-regra.md`;
- `docs/spec/criterio-fechamento-ciclos.md`;
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

## Decisões transversais aplicáveis e questões restantes

As semânticas de T1 e T2 estão fechadas. O ciclo começa imediatamente; dúvidas
remanescentes são dependências localizadas de uma regra ou de um valor, nunca
bloqueio geral da família.

### T1 — Ramos de fundamentação — decidido

O Sisprev permite os dois modos de parametrização, mas o catálogo auditado adota
**um ramo por regra**. Consequências para o ciclo:

- uma regra integral carrega a fundamentação do ramo integral;
- uma regra proporcional carrega a fundamentação que autoriza a
  proporcionalização;
- `regra-0002`, `regra-0020` e `regra-0021` não ficam suspensas por dúvida de
  coluna: deve-se conferir qual ramo jurídico cada uma representa e corrigir ou
  decompor conforme o mérito;
- `regra-0004` deve ser decomposta se a linha legada efetivamente empacotar os
  dois resultados.

### T2 — Semântica das fronteiras inferiores — decidida

- `DATA_DIREITO_APOS` é inclusivo e se refere à implementação de todos os
  requisitos a partir da data gravada;
- `DATA_ADM_APOS` é inclusivo e se refere ao ingresso no serviço público, com a
  posse como marco jurídico do cargo efetivo;
- nenhuma das duas colunas representa data de requerimento ou concessão.

O que continua aberto é o **lastro jurídico de valores concretos**, inclusive:

- `15/12/1998` e `16/12/1998`;
- `30/12/2003`, `31/12/2003` e `01/01/2004`;
- `18/10/2021` e o valor cadastrado `23/10/2021`.

Nenhuma data será ajustada apenas para alinhar intervalos: cada valor precisa de
função jurídica e fonte declaradas. Isso é conferência de mérito, não dúvida
sobre a semântica da coluna.

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

### T4 — Resultado admissível por regra e cobertura final

Durante a execução, cada regra recebe exatamente uma destas situações:

- **conferida sem alteração**;
- **corrigida e mantida ativa**, quando a correção não altera sua identidade
  material;
- **desativada e substituída**, quando representava defeituosamente hipótese
  jurídica que continua existindo;
- **desativada sem substituta**, quando representava hipótese juridicamente
  inexistente, com fundamento expresso; ou
- **pendente por dependência externa**, com a pergunta, a evidência faltante, o
  responsável pela obtenção e o efeito preciso sobre a regra.

A situação pendente é intermediária. Ela não pode chegar ao fechamento quando
impedir afirmar cobertura completa, ausência de lacuna ou ausência de
sobreposição injustificada. “Não analisada”, “parece correta” e “desativada sem
disposição expressa” não são resultados de encerramento.

### T5 — Detecção e criação de regras ausentes

A avaliação dos blocos não parte da presunção de que as regras legadas esgotam o
tema. Para cada combinação juridicamente possível da matriz de cobertura, deve-se
verificar se existe regra ativa suficiente. Quando não existir, o próprio bloco
proprietário cria regra nova com ID próprio e registra a origem
`lacuna preexistente`.

A regra nova por lacuna não integra o mapa de substituições. Ela integra um
inventário separado `combinação descoberta → regra nova`, com fonte e fundamento.

## Cotejo jurídico

### Bloco A — CF/88 original e EC 20/1998

Regras: `regra-0001`, `regra-0002` e `regra-0004`.

Perguntas de decisão:

1. As regras representam situações de direito adquirido já implementado antes
   de cada reforma, alguma transição expressa ou outra hipótese juridicamente
   sobrevivente? A mera data de ingresso não basta.
2. Quais dispositivos fundam paridade e forma de cálculo nos regimes de 1988 e
   1998?
3. Qual lei especificava as doenças graves no período e qual era sua vigência?
4. `regra-0004` deve permanecer como linha não discriminada ou ser decomposta
   nos ramos integral e proporcional, conforme a decisão de T1?
5. Os valores das janelas cadastradas têm lastro jurídico compatível com T2?

Saída do bloco: matriz de aplicabilidade histórica e decisão individual sobre as
três regras, sem presumir que regra antiga deva permanecer ativa apenas porque a
redação existiu no passado. O bloco também deve criar as regras necessárias para lacunas preexistentes
que identificar em seu regime.

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
integral ou proporcional e com a classe de causa representada. O bloco também deve criar as regras necessárias para lacunas preexistentes
que identificar em seu regime.

### Bloco C — EC 103/2019 e LCE 1.100/2021

Regras: `regra-0019` a `regra-0022`.

Perguntas de decisão:

1. Em `regra-0020` e `regra-0021`, o campo `integral: N` está correto e a
   fundamentação foi copiada do ramo integral, ou o valor gravado é que está
   errado? Aplicar a decisão consolidada de T1, sem escolher por aparência.
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
paridade, fundamentação e dispositivos. O bloco também deve criar as regras necessárias para lacunas preexistentes
que identificar em seu regime.

## Estratégia de execução por sessões

O ciclo será executado em sessões pequenas e sequenciais. Cada sessão parte da
`main` resultante da sessão anterior, entrega uma PR revisável e atualiza este
arquivo. Não serão mantidas PRs paralelas que editem a mesma regra, o mesmo
achado ou o mesmo dispositivo.

A divisão não cria relatórios paralelos. A issue #89 rastreia links e estado; as
decisões, fontes e resultados continuam registrados neste arquivo e nos concepts
autorais diretamente afetados.

### S0 — Linha de base e inventário

- Branch sugerida: `cycle/1-s0-linha-de-base`.
- Escopo: inventariar as 11 regras, seus achados, dispositivos, formas de cálculo
  e fontes já disponíveis, sem decidir mérito.
- Saída obrigatória: matriz inicial preenchida, mapa
  `regra → achados → fontes → lacunas` e inventário inicial de combinações sem
  regra correspondente.
- Critério de saída: nenhuma regra permanece sem população de achados e sem lista
  de fontes a conferir.

### S1 — Causa e resultado admissível

- Branch sugerida: `cycle/1-s1-causa-resultados`.
- Escopo: fechar T3 e T4 — vocabulário de causa, teste de materialidade da
  decomposição e forma de registrar o resultado final.
- Saída obrigatória: decisão transversal escrita neste arquivo e matriz de
  decomposição por regime.
- Critério de saída: cada regra possui classes de causa possíveis e resultado
  admissível definido; T5 fixa como detectar e registrar hipóteses sem regra, sem
  editar ainda o mérito histórico.

### S2 — Bloco A

- Branch sugerida: `cycle/1-s2-bloco-a`.
- Escopo: auditar `regra-0001`, `regra-0002` e `regra-0004`; consultar
  `regra-0003` e `regra-0005` somente como referências.
- Saída obrigatória: decisão individual, correções autorais, dispositivos e
  achados estritamente necessários.
- Critério de saída: as três regras recebem situação T4 ou dependência localizada
  com dono e efeito.

### S3 — Bloco B

- Branch sugerida: `cycle/1-s3-bloco-b`.
- Escopo: auditar `regra-0006` a `regra-0009` sob EC 41/2003, EC 70/2012 e LCE
  432/2008.
- Saída obrigatória: pares geral/transição coerentes quanto a causa, ramo,
  cálculo, reajuste e citação.
- Critério de saída: as quatro regras recebem situação T4; nenhuma citação
  incompatível permanece sem disposição.

### S4 — Bloco C

- Branch sugerida: `cycle/1-s4-bloco-c`.
- Escopo: auditar `regra-0019` a `regra-0022` sob EC 103/2019 e LCE 1.100/2021.
- Saída obrigatória: regras pós-reforma coerentes, inclusive quanto ao marco de
  2021 e às classes de causa.
- Critério de saída: as quatro regras recebem situação T4; dependências reais
  ficam individualizadas.

### S5 — Consistência transversal e resolução de pendências

- Branch sugerida: `cycle/1-s5-consistencia`.
- Escopo: comparar os três blocos, formas de cálculo, classes de causa,
  fronteiras e dispositivos; inventariar todas as pendências deixadas por S2,
  S3 e S4; dar disposição a cada uma; e verificar se a matriz contém combinação
  juridicamente possível ainda sem regra ativa.
- Saída obrigatória: correção de inconsistências entre sessões, matriz final
  consolidada, inventário `combinação descoberta → regra nova` e registro de zero
  pendências ou lacunas que afetem cobertura.
- Critério de saída: a mesma hipótese material recebe tratamento compatível em
  todos os regimes ou a divergência fica expressamente justificada; toda
  pendência de cobertura é resolvida em S5 ou devolvida, com reabertura, à sessão
  proprietária da regra ou do bloco.

### S6 — Fechamento

- Branch sugerida: `cycle/1-s6-fechamento`.
- Gate de entrada: zero pendências abertas que afetem a cobertura material do
  tema. Se o gate falhar, o trabalho retorna obrigatoriamente a S5 ou à sessão
  proprietária correspondente.
- Escopo: regenerar derivados, executar gates, preencher a conclusão e encerrar o
  ciclo.
- Saída obrigatória: PR final com resumo por regra, mapa de substituições e de
  desativações sem substituta, inventário das regras novas por lacuna
  preexistente, matriz de cobertura, fontes, riscos residuais e CI verde.
- Critério de saída: nenhuma regra errada permanece ativa; toda desativação tem
  substituição ou registro fundamentado de `sem substituta`; a matriz demonstra
  cobertura completa sem lacunas ou sobreposições injustificadas; e o checklist
  está integralmente tratado.

### Ordem e dependências

1. S0 e S1 são obrigatoriamente sequenciais.
2. S2, S3 e S4 também serão sequenciais, porque compartilham vocabulário de
   causa, formas de cálculo, dispositivos e espaço de novos IDs.
3. Uma sessão só começa depois do merge da anterior. PR empilhada exige motivo
   explícito e não pode editar concepts já tocados pela PR-base.
4. Questão externa localizada não paralisa a sessão inteira: a regra afetada é
   marcada como pendente e as demais continuam.
5. Descoberta transversal ou hipótese sem regra durante um bloco é registrada
   imediatamente. A regra nova para lacuna material pertence ao bloco do regime;
   a harmonização global pertence à S5.
6. S5 é responsável por inventariar e dar disposição às pendências dos blocos. O
   que não puder resolver transversalmente retorna à sessão proprietária.
7. S6 só começa após o registro explícito de zero pendências que afetem
   cobertura.

### Contrato mínimo de cada sessão

Toda sessão deve:

- declarar no início o commit-base e os concepts proprietários;
- ler integralmente as specs dos tipos que editará;
- conferir se já existe achado para a unidade de investigação;
- separar fato mecânico, interpretação jurídica e decisão autoral;
- atualizar este arquivo no mesmo PR, sem deixar conclusão apenas em comentário;
- relacionar fontes primárias efetivamente abertas;
- regenerar derivados somente quando houver alteração de concept que os afete;
- executar os gates aplicáveis antes do merge; e
- registrar o commit de fechamento e a PR no registro das sessões.

Uma PR de bloco pode editar apenas:

- as regras proprietárias daquela sessão;
- dispositivos e formas de cálculo necessários para fundamentá-las;
- achados que efetivamente alcancem essas regras;
- este arquivo de ciclo; e
- artefatos derivados produzidos pelos scripts oficiais.

Referências de outro ciclo permanecem somente leitura, salvo ampliação de escopo
expressa neste arquivo antes da edição.

### Registro das sessões

- [ ] S0 — não iniciada; PR: —; commit-base: —; fechamento: —.
- [ ] S1 — não iniciada; PR: —; commit-base: —; fechamento: —.
- [ ] S2 — não iniciada; PR: —; commit-base: —; fechamento: —.
- [ ] S3 — não iniciada; PR: —; commit-base: —; fechamento: —.
- [ ] S4 — não iniciada; PR: —; commit-base: —; fechamento: —.
- [ ] S5 — não iniciada; PR: —; commit-base: —; fechamento: —.
- [ ] S6 — não iniciada; PR: —; commit-base: —; fechamento: —.

## Fluxo processual

### Fase 0 — congelar a linha de base

- [ ] Registrar o commit efetivamente usado para iniciar a execução.
- [ ] Montar neste arquivo a matriz
  `regra → regime → janela → causa → integralidade → cálculo → paridade → fundamentação → dispositivos`.
- [ ] Relacionar os achados já abertos que alcançam cada regra.
- [ ] Executar os detectores apenas para registrar fatos mecânicos atuais.

### Fase 1 — aplicar as decisões transversais

- [x] T1 documentada: um ramo por regra no catálogo auditado.
- [x] T2 documentada: `DATA_DIREITO_APOS` e `DATA_ADM_APOS` inclusivos.
- [ ] Fixar o vocabulário e o teste de materialidade de T3.
- [ ] Registrar a forma de resultado de T4.
- [ ] Registrar o método de detecção e criação de regras ausentes de T5.

T1 e T2 não bloqueiam o início das edições de mérito. T3 ou uma questão concreta
pode suspender apenas a alteração diretamente dependente dela.

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

- [ ] Inventariar todas as pendências deixadas pelos blocos e resolvê-las em S5
  ou devolvê-las à sessão proprietária.
- [ ] Registrar zero pendências que afetem cobertura antes de abrir S6.
- [ ] Consolidar o mapa
  `regra desativada → regra(s) substituta(s) | sem substituta fundamentada`.
- [ ] Consolidar a matriz final de cobertura e as combinações juridicamente
  impossíveis.
- [ ] Criar todas as regras necessárias para combinações juridicamente possíveis
  sem antecedente no catálogo e registrar o inventário
  `combinação descoberta → regra nova`.
- [ ] Editar apenas os arquivos OKF autorais correspondentes.
- [ ] Garantir que `dispositivos:` reflita a fundamentação resultante.
- [ ] Atualizar o resultado por regra neste arquivo.
- [ ] Listar fontes efetivamente consultadas e pendências remanescentes.
- [ ] Não deixar conclusão relevante apenas em `docs/analysis/`, comentário de
  PR ou conversa.

### Fase 6 — validar e encerrar

- [ ] Confirmar o gate de entrada: zero pendências que afetem cobertura.
- [ ] Regenerar artefatos com `uv run python scripts/gerar_indices.py`.
- [ ] Executar `uv run python scripts/validar_regras.py`.
- [ ] Executar a suíte de testes e os demais gates definidos no CI.
- [ ] Conferir que a regeneração não deixou diff derivado inesperado.
- [ ] Submeter a PR do ciclo com resumo das decisões, riscos residuais e teste
  por regra.
- [ ] Encerrar a issue #89 somente após preencher a conclusão deste arquivo.

## Entregável

O ciclo deve produzir, numa única cadeia rastreável:

01. este arquivo preenchido com decisões e resultados;
02. regras corretas mantidas ou criadas — por substituição ou por lacuna
    preexistente — e regras materialmente erradas desativadas;
03. mapa completo
    `regra desativada → regra(s) substituta(s) | sem substituta fundamentada`;
04. inventário `combinação descoberta → regra nova` para lacunas preexistentes;
05. matriz final de cobertura, com combinações impossíveis fundamentadas;
06. novos dispositivos apenas quando indispensáveis e conferidos em fonte
    primária;
07. achados autorais novos ou atualizados, sem duplicação;
08. registro de zero pendências que afetem cobertura;
09. artefatos derivados sincronizados; e
10. CI integralmente verde.

Não será criado relatório paralelo do ciclo.

## Matriz inicial de trabalho

| Regra        | Regime representado                    | Papel cadastrado atual                             | Decisão central do ciclo                                        |
| ------------ | -------------------------------------- | -------------------------------------------------- | --------------------------------------------------------------- |
| `regra-0001` | CF/88 original                         | integral, paridade, Valor Efetivo                  | aplicabilidade histórica, causa qualificada, cálculo e paridade |
| `regra-0002` | CF/88 original                         | proporcional, mas texto no ramo integral           | aplicar T1 e confirmar base do proporcional                     |
| `regra-0004` | EC 20/1998                             | ramos não discriminados; campos estruturais vazios | decidir decomposição, cálculo, paridade e janelas               |
| `regra-0006` | EC 41/2003 + LCE 432                   | integral                                           | fronteira temporal, causa e correção da citação constitucional  |
| `regra-0007` | EC 41/2003 + LCE 432                   | proporcional                                       | aplicar T1, base proporcional e fronteira temporal              |
| `regra-0008` | art. 6º-A/EC 70 + LCE 432              | integral                                           | transição expressa, causa e base de cálculo                     |
| `regra-0009` | art. 6º-A/EC 70 + LCE 432              | proporcional                                       | aplicar T1, causa comum e base proporcional                     |
| `regra-0019` | EC 103 + LCE 1.100, ingresso até 2003  | integral, paridade                                 | classe de causa, cálculo por integralidade e dispositivo geral  |
| `regra-0020` | EC 103 + LCE 1.100, ingresso até 2003  | proporcional, texto integral                       | aplicar T1, base proporcional e classes indevidamente citadas   |
| `regra-0021` | EC 103 + LCE 1.100, ingresso após 2003 | proporcional, sem paridade, texto integral         | aplicar T1, ramo temporal, arts. 26/27-II e decomposição        |
| `regra-0022` | EC 103 + LCE 1.100, ingresso após 2003 | média, sem paridade                                | arts. 24/27-II, causa qualificada e decomposição                |

## Resultado por regra

Preencher cada linha com uma das situações de T4 e resumir: decisão, alterações,
fontes, achados, dependências e, quando desativada, as substitutas ou o registro
fundamentado de `sem substituta`.

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

### Regras novas sem antecedente legado

Preencher para cada lacuna preexistente identificada:

- [ ] combinação jurídica descoberta; regra nova; bloco proprietário; fontes;
  fundamento da ausência no catálogo anterior.

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

Na abertura, permanecem como questões de investigação concreta, não como dúvidas
sobre o significado das colunas:

- P-1 — sobrevivência jurídica das regras anteriores às reformas;
- P-2 — fronteira da regra geral EC 41/2003 por exclusão do art. 6º-A;
- P-3/P-4 — citação ao art. 40, § 1º, III, em regras de invalidez;
- P-5 — fundamentação pós-2003 de `regra-0021` e `regra-0022`;
- P-6 — definição normativa de moléstia profissional;
- Q6-S/Q6-T — obtenção, persistência, classificação e vigência da causa no caso
  concreto;
- fundamento do marco `23/10/2021`;
- lastro jurídico dos demais valores temporais específicos;
- dispositivos de paridade e forma de cálculo dos regimes de 1988 e 1998;
- rol de doenças aplicável aos regimes históricos.

Ao fechar o ciclo, substituir esta lista pelas pendências realmente restantes,
com evidência faltante, responsável e impacto por regra. Nenhuma delas pode
afetar a cobertura material do tema.

## Conclusão do ciclo

- [x] T1 e T2 estão decididas e documentadas como semântica vigente.
- [ ] T3 e T4 foram decididas ou convertidas em dependências externas precisas.
- [ ] Todas as regras proprietárias receberam uma situação final de T4.
- [ ] Nenhuma regra materialmente errada permanece ativa.
- [ ] Toda regra desativada possui substituta suficiente ou registro fundamentado
  de `sem substituta — hipótese juridicamente inexistente`.
- [ ] A matriz demonstra cobertura completa das combinações juridicamente
  relevantes e fundamenta as combinações impossíveis.
- [ ] Toda combinação juridicamente possível sem antecedente no catálogo recebeu
  regra nova com ID próprio e origem `lacuna preexistente`.
- [ ] O inventário `combinação descoberta → regra nova` está completo.
- [ ] Toda sobreposição foi eliminada ou expressamente justificada.
- [ ] Não existe pendência aberta que afete cobertura.
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
