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

> **Estado:** em execução — S0 a S4 concluídas; S5 em revisão na PR #97.
> Este arquivo é a fonte única do plano, das decisões, do diário de execução e
> do relatório final do ciclo.

## Identificação

- Data de abertura: 01/08/2026
- Commit-base da execução: `79a112562a7a9172b9cda484f3ac4f6bf5b6853f`
- Issue de execução: [#89](https://github.com/franklinbaldo/sisprev/issues/89)
- S0: PR #92, merge `1393314118fad67e0057ee29d5c8740d01b71283`
- S1: PR #93, merge `f68689841944000ab89db8379ff48be8e48aaf80`
- S2: PR #94, merge `c722c6d3563e52626434c49a72126b516847585d`
- S3: PR #95, merge `19b21ae55cd2845194dc77181562cd53cc033c71`
- S4: PR #96, merge `ecd9f743391a8743ee536794ad74f72bd7cb2425`
- S5: PR #97, branch `cycle/1-s5-consistencia`
- Responsável pelas decisões jurídicas: Franklin Baldo
- Data de fechamento:
- Commit de fechamento:

## Contexto acadêmico e histórico

A aposentadoria por invalidez e sua sucessora terminológica, a aposentadoria por
incapacidade permanente, atravessam sucessivas redações constitucionais e leis
estaduais. O ciclo distingue direito adquirido, regra geral, transição,
fundamento de cálculo, proporcionalidade e regime de reajuste.

A existência histórica de um texto não prova, por si, que ele continue
selecionável. A sobrevivência depende de direito adquirido ou norma expressa de
preservação. Do mesmo modo, a ausência de hipótese no catálogo legado não prova
que ela seja juridicamente inexistente.

O trabalho está organizado em três blocos: CF/88 original e EC 20/1998; EC
41/2003 e EC 70/2012; e EC 103/2019 com LCE 1.100/2021.

## Dimensão social

A regra selecionada define a renda de servidor permanentemente incapaz para o
trabalho. Erros de causa, janela, cálculo, proporcionalidade ou paridade podem
reduzir benefício devido, produzir pagamento sem fundamento ou impedir a
explicação do ato concessório.

Por isso, o ciclo exige cadeia rastreável entre fatos do requerente, classe de
causa, regra selecionada, forma de cálculo e reajuste. Ausência de informação ou
prova insuficiente não pode ser convertida automaticamente em `causa_comum`.

## Objetivo

Entregar um conjunto ativo de regras que represente corretamente e por inteiro
as aposentadorias por incapacidade permanente e as hipóteses históricas de
invalidez do escopo.

O ciclo deve desativar regras materialmente erradas, criar substitutas para
hipóteses existentes, registrar `sem substituta` para hipóteses juridicamente
inexistentes e criar regras novas para lacunas preexistentes.

## Critério de fechamento

Aplica-se
[`docs/spec/criterio-fechamento-ciclos.md`](../../../docs/spec/criterio-fechamento-ciclos.md).
O ciclo só encerra quando:

- nenhuma regra sabidamente errada permanecer ativa;
- toda hipótese possível estiver coberta por regra correta;
- toda desativação tiver substituição suficiente ou fundamento de
  `sem substituta`;
- toda lacuna preexistente tiver unidade própria;
- não houver sobreposição injustificada;
- não houver pendência que afete cobertura; e
- derivados, validadores, testes e CI estiverem íntegros.

## Decisões semânticas consolidadas

Aplicam-se
[`docs/spec/decisoes-semanticas-regra.md`](../../../docs/spec/decisoes-semanticas-regra.md)
e
[`docs/spec/janelas-temporais-regra.md`](../../../docs/spec/janelas-temporais-regra.md).

1. Uma regra representa um único ramo: integral ou proporcional.
2. `integral: S` significa ausência de proporcionalização pelo tempo.
3. `tipo_calculo` referencia uma `FormaCalculo`; o enum legado não limita o
   conceito jurídico.
4. `DATA_ADM_APOS`, `DATA_ADM_ATE` e `DATA_DIREITO_APOS` são inclusivos.
5. `DATA_DIREITO_ATE` é exclusivo e recebe o primeiro dia fora da janela.
6. Causa não informada ou prova insuficiente não equivalem a `causa_comum`.
7. Predicado sem coluna continua modelável e exige aferição humana.
8. ID legado não é reaproveitado para hipótese material diferente.
9. Cobertura não se limita ao catálogo legado.

## Escopo

### Regras proprietárias

- Bloco A: `regra-0001`, `regra-0002`, `regra-0004`.
- Bloco B: `regra-0006` a `regra-0009`.
- Bloco C: `regra-0019` a `regra-0022`.

### Fora de escopo

- implementar motor, tela ou banco do Sisprev;
- criar coluna deployável de causa;
- alterar regra de outro ciclo sem ampliação expressa; e
- validar integralmente regras de pensão.

## Cotejo jurídico

### T1 — Ramos — decidido

Integral e proporcional são unidades distintas. Linha que empacota os dois
resultados deve ser decomposta.

### T2 — Janelas — decidido

- `APOS` do direito e da admissão: inclusivo;
- `ATE` da admissão: inclusivo;
- `ATE` do direito: exclusivo.

Assim, a redação original da CF fecha em `16/12/1998`, a EC 20 fecha em
`31/12/2003`, o prazo legal até 31/12/2024 fecha em `01/01/2025` e a LCE
1.100/2021 começa em `18/10/2021`.

### T3 — Causas — decidido

O vocabulário mínimo é `acidente_em_servico`, `molestia_profissional`,
`doenca_catalogada` e `causa_comum`. A documentação jurídica também descreve a
terceira classe como doença grave catalogada; os dois nomes designam a mesma
classe, e o primeiro é o valor implementado no schema auditado.

A causa é material quando altera elegibilidade, ramo, cálculo, paridade,
reajuste ou combinação normativa da matriz.

### T4 — Resultado admissível — decidido

Cada regra termina em `conferida_sem_alteracao`, `corrigida_mantida_ativa`,
`desativada_substituida`, `desativada_sem_substituta` ou, somente durante a
execução, `pendente_dependencia_localizada`.

### T5 — Lacunas — decidido

Cada combinação normativa possível é mapeada para zero, uma ou mais regras.
Zero significa lacuna; mais de uma exige justificativa ou eliminação da
sobreposição. Regra nova tem origem `substituicao` ou `lacuna_preexistente`.

### T6 — Cálculo da incapacidade sob a LCE 1.100/2021 — decidido na S4

Os §§ 13 e 14 do art. 30 são regras especiais do cálculo da incapacidade:

- as causas qualificadas remetem à média do art. 24, sem proporcionalização;
- a causa comum remete ao art. 26, que proporcionaliza em dias o valor calculado
  na forma do art. 24.

O art. 27 disciplina separadamente o reajuste: paridade para ingresso até
31/12/2003 e reajuste sem paridade para ingresso após essa data. Por isso, a
combinação proporcional com paridade representada imperfeitamente por
`regra-0020` é juridicamente possível.

A ressalva ao direito adquirido a outra fórmula preserva hipóteses formadas sob
regime anterior. Ela não transforma, por si só, o ingresso até 2003 em exceção à
remissão expressa dos §§ 13 e 14 aos arts. 24 e 26.

### T7 — Precedência, fórmulas compostas e Q6 — decidido na S5

A interseção entre o regime preservado do art. 4º da ECE 146/2021 e o regime
permanente da LCE 1.100/2021 não gera escolha livre. Entre 18/10/2021 e
31/12/2024, primeiro se verifica se todos os requisitos e critérios anteriores
foram cumpridos no prazo. Quando o art. 4º incide, aplicam-se a unidade, o
cálculo e o reajuste preservados do Bloco B. O Bloco C somente é selecionado
quando essa preservação não incide e seus próprios requisitos estão satisfeitos.

Depois de 31/12/2024 não nasce novo enquadramento no art. 4º; direitos formados
até essa data continuam assegurados a qualquer tempo.

A S5 autora três formas compostas:

- média contributiva da LCE 432/2008 proporcional em dias;
- remuneração do cargo efetivo do art. 6º-A proporcional ao tempo; e
- média contributiva da LCE 1.100/2021 proporcional em dias.

A forma inicial de cálculo e o regime de reajuste são dimensões diferentes. A
mesma média proporcional da LCE 1.100/2021 pode coexistir com paridade ou sem
paridade, conforme o art. 27.

Q6-R está fechada para o catálogo auditado. Q6-S e Q6-T permanecem dependências
operacionais localizadas porque o repositório não contém tela, banco, solicitação
ou protocolo institucional que demonstre onde a causa do requerente é obtida,
registrada e classificada.

## Fluxo processual

- S0 — linha de base.
- S1 — contratos transversais T3–T5.
- S2 — Bloco A.
- S3 — Bloco B.
- S4 — Bloco C.
- S5 — consistência transversal e resolução das pendências.
- S6 — fechamento com zero lacunas e zero pendências materiais.

As sessões são sequenciais e cada uma parte da `main` resultante da anterior.

### Registro das sessões

- [x] S0 — PR #92; fechamento
  `1393314118fad67e0057ee29d5c8740d01b71283`.
- [x] S1 — PR #93; fechamento
  `f68689841944000ab89db8379ff48be8e48aaf80`.
- [x] S2 — PR #94; fechamento
  `c722c6d3563e52626434c49a72126b516847585d`.
- [x] S3 — PR #95; fechamento
  `19b21ae55cd2845194dc77181562cd53cc033c71`.
- [x] S4 — PR #96; fechamento
  `ecd9f743391a8743ee536794ad74f72bd7cb2425`.
- [ ] S5 — PR #97 em revisão; commit-base
  `ecd9f743391a8743ee536794ad74f72bd7cb2425`.
- [ ] S6 — não iniciada.

### Registro da S0 — Linha de base

A S0 inventariou as 11 regras, seus achados, fontes, precedentes e candidatos a
lacuna. Nenhuma regra deployável foi alterada.

A correção documental central foi reconhecer que `DATA_ADM_APOS` é inclusivo:
`01/01/2004` inclui quem ingressou naquele dia. O defeito remanescente das regras
pós-2021 está no marco do direito, não no ingresso.

### Registro da S1 — Contratos transversais

A S1 fechou o vocabulário de causa, o teste de materialidade, as situações T4 e
o protocolo T5. Q6-R ficou resolvido para a auditoria; Q6-S e Q6-T permanecem
dependências operacionais localizadas.

### Registro da S2 — Bloco A

`regra-0001`, `regra-0002` e `regra-0004` recebem
`desativada_substituida`.

As três origens são substituídas por oito unidades: dois regimes constitucionais
vezes quatro classes de causa. Nenhuma hipótese fica sem substituta e nenhuma
lacuna preexistente foi demonstrada no Bloco A.

Na CF/88 original, as causas qualificadas produzem integralidade e paridade; a
causa comum produz proporcionalidade e paridade. Na EC 20/1998, as qualificadas
produzem totalidade e paridade; a causa comum produz totalidade proporcional e
paridade.

O conjunto cumulativo da S2 é `ciclo-01-s2-bloco-a`.

### Registro da S3 — Bloco B

`regra-0006`, `regra-0007`, `regra-0008` e `regra-0009` recebem
`desativada_substituida`.

No regime geral da EC 41, as três causas qualificadas conduzem à média sem
proporcionalização e sem paridade; a causa comum conduz à média proporcional ao
tempo e sem paridade.

No art. 6º-A da EC 70, as três causas qualificadas conduzem à remuneração do
cargo sem proporcionalização e com paridade; a causa comum conduz à remuneração
do cargo proporcional ao tempo e com paridade.

A S3 cria oito unidades e dois grupos atômicos 2:4. O conjunto
`ciclo-01-s3-bloco-b` deriva de `ciclo-01-s2-bloco-a`. A janela comum é
`[31/12/2003, 01/01/2025)`.

### Registro da S4 — Bloco C

`regra-0019`, `regra-0020`, `regra-0021` e `regra-0022` recebem
`desativada_substituida`.

A S4 cria oito unidades: duas coortes de ingresso vezes quatro classes de causa.
Nenhuma origem fica sem substituta e nenhuma lacuna preexistente foi demonstrada
no Bloco C.

Para ingresso até 31/12/2003, as causas qualificadas conduzem à média sem
proporcionalização e com paridade; a causa comum conduz à média proporcional em
dias, também com paridade.

Para ingresso a partir de 01/01/2004, as causas qualificadas conduzem à média
sem proporcionalização e sem paridade; a causa comum conduz à média proporcional
em dias, sem paridade.

A `regra-0020` não é juridicamente impossível. O defeito está na fundamentação
integral copiada e na projeção incompleta da fórmula, não na combinação
proporcional com paridade.

Os §§ 13 e 14 do art. 30 foram autorados. A janela começa em `18/10/2021`, e a
divisão de ingresso é contínua entre `31/12/2003` e `01/01/2004`.

O conjunto `ciclo-01-s4-bloco-c` deriva de `ciclo-01-s3-bloco-b`, preservando os
Blocos A e B.

### Registro da S5 — Consistência transversal

A S5 não altera a pertinência do conjunto. `ciclo-01-s5-consistencia` deriva da
S4 sem deltas e registra os desempates necessários para ler os três blocos como
um único catálogo.

A interseção dos Blocos B e C recebe precedência expressa: testa-se primeiro a
preservação do art. 4º da ECE 146/2021; o regime permanente somente entra quando
ela não incide.

Três formas compostas são autoradas para separar a ontologia jurídica da
projeção incompleta do enum legado. Com isso, a falta de rótulo deixa de ser
tratada como desconhecimento da fórmula.

Q6-S e Q6-T são atribuídas ao IPERON como dependências operacionais, com a
evidência necessária delimitada: tela ou schema de entrada, modelo de laudo,
protocolo de acidente e nexo profissional, rol de doenças versionado e
integração do fato apurado com a seleção da regra.

## Entregável

O ciclo deverá conter catálogo correto e completo, regras erradas desativadas,
substitutas e regras de lacuna, mapa de substituições, matriz final de cobertura,
combinações impossíveis fundamentadas, formas de cálculo e dispositivos,
derivados sincronizados e CI integralmente verde.

A S5 entrega o desempate entre regimes, três formas de cálculo compostas e a
localização exata das dependências que ainda impedem ativação e fechamento.

## Resultado por regra

- [x] `regra-0001` — `desativada_substituida` na S2.
- [x] `regra-0002` — `desativada_substituida` na S2.
- [x] `regra-0004` — `desativada_substituida` na S2.
- [x] `regra-0006` — `desativada_substituida` na S3.
- [x] `regra-0007` — `desativada_substituida` na S3.
- [x] `regra-0008` — `desativada_substituida` na S3.
- [x] `regra-0009` — `desativada_substituida` na S3.
- [x] `regra-0019` — `desativada_substituida` na S4.
- [x] `regra-0020` — `desativada_substituida` na S4; combinação preservada com
  base média proporcional.
- [x] `regra-0021` — `desativada_substituida` na S4.
- [x] `regra-0022` — `desativada_substituida` na S4.

## Referências de outros ciclos

`regra-0003` e `regra-0005` foram consultadas apenas como referências de
continuidade histórica. Não são proprietárias do Ciclo 1 e não recebem alteração
nesta cadeia.

Achados e regras de outros ciclos, como `regra-0032`, permanecem com seus donos.
A correção geral da semântica temporal pode ser reutilizada, mas a disposição da
hipótese material pertence ao respectivo ciclo proprietário.

## Fontes legais consultadas

- Constituição Federal, art. 40, nas redações original, EC 20/1998, EC 41/2003
  e EC 103/2019;
- EC 41/2003, art. 6º-A, com redação da EC 70/2012;
- ECE 146/2021, art. 4º;
- Lei federal 10.887/2004, art. 1º;
- LC estadual 228/2000;
- LCE 432/2008, especialmente arts. 17, 20 e 45;
- LCE 672/2012, quanto à redação do art. 45 da LCE 432/2008;
- LCE 1.100/2021 compilada, especialmente arts. 24, 25, 26, 27, 29 e 30;
- dispositivos autorados no repositório, inclusive art. 30, §§ 13 e 14; e
- decisões semânticas documentadas em `docs/spec/`.

## Pendências que permanecem abertas

- transcrever e versionar a fórmula estadual anterior à LCE 432/2008,
  inclusive sob a LC 228/2000;
- fechar o cálculo do intervalo entre 31/12/2003 e a vigência da Lei
  10.887/2004;
- transcrever a redação original do art. 45 da LCE 432/2008 e conferir os
  limitadores que devem preceder a fração do art. 17;
- confirmar a projeção das combinações de cálculo e reajuste no Sisprev;
- obter do IPERON a evidência operacional de Q6-S/Q6-T: entrada, persistência,
  classificação, nexo, rol temporal e integração com a seleção;
- completar o gate humano das unidades;
- registrar ato institucional e decisão de completude antes de qualquer
  ativação; e
- executar a S6 sem ocultar nem converter essas dependências em conclusões.

Nenhuma dessas pendências é ocultada por ativação prematura: os grupos de S2,
S3 e S4 permanecem inativos e suas unidades, em elaboração.

## Conclusão do ciclo

O ciclo permanece aberto. S0 a S4 estão concluídas; a S5 está materializada na
PR #97 e aguarda validação, revisão e merge. A S6 ainda precisa decidir, contra o
critério de fechamento, se as dependências localizadas podem ser formalmente
encaminhadas ou se bloqueiam o encerramento.

A conclusão final somente poderá declarar cobertura completa quando todas as
unidades necessárias estiverem prontas, as regras erradas estiverem efetivamente
retiradas do conjunto ativo e não restarem lacunas, sobreposições ou pendências
materiais.
