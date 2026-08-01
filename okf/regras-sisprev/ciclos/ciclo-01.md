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

> **Estado:** em execução — S0 a S5 concluídas; Bloco B reaberto na PR #98
> para refinamento temporal das fórmulas. Este arquivo é a fonte única do plano,
> das decisões, do diário de execução e do relatório final do ciclo.

## Identificação

- Data de abertura: 01/08/2026
- Commit-base da execução: `79a112562a7a9172b9cda484f3ac4f6bf5b6853f`
- Issue de execução: [#89](https://github.com/franklinbaldo/sisprev/issues/89)
- S0: PR #92, merge `1393314118fad67e0057ee29d5c8740d01b71283`
- S1: PR #93, merge `f68689841944000ab89db8379ff48be8e48aaf80`
- S2: PR #94, merge `c722c6d3563e52626434c49a72126b516847585d`
- S3: PR #95, merge `19b21ae55cd2845194dc77181562cd53cc033c71`
- S4: PR #96, merge `ecd9f743391a8743ee536794ad74f72bd7cb2425`
- S5: PR #97, merge `269ba448408848ceb3ba2844d791ab4658caf6b9`
- Reabertura da S3: PR #98, branch `cycle/1-s3-reabertura-calculo`
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
preservação. Do mesmo modo, ausência de hipótese no catálogo legado não prova
que ela seja juridicamente inexistente.

O tema está organizado em três blocos: CF/88 original e EC 20/1998; EC 41/2003
e EC 70/2012; e EC 103/2019 com LCE 1.100/2021.

## Dimensão social

A regra selecionada define a renda de servidor permanentemente incapaz para o
trabalho. Erros de causa, janela, base de cálculo, proporcionalidade ou paridade
podem reduzir benefício devido, gerar pagamento sem fundamento ou impedir a
explicação do ato concessório.

Por isso, o ciclo exige cadeia rastreável entre fatos do requerente, classe de
causa, regra selecionada, fórmula inicial e regime de reajuste. Ausência de
informação ou prova insuficiente não pode ser convertida automaticamente em
`causa_comum`.

## Objetivo

Entregar composição que represente corretamente as aposentadorias por
incapacidade permanente e as hipóteses históricas de invalidez do escopo,
preservando o histórico das regras legadas e criando unidades auditadas para
cada combinação materialmente distinta.

O ciclo deve desativar regras materialmente erradas, criar substitutas para
hipóteses existentes, registrar `sem substituta` para hipóteses juridicamente
inexistentes e criar unidades próprias para lacunas preexistentes.

## Critério de fechamento

Aplica-se
[`docs/spec/criterio-fechamento-ciclos.md`](../../../docs/spec/criterio-fechamento-ciclos.md).
O ciclo somente encerra quando:

- nenhuma regra sabidamente errada permanecer ativa;
- toda hipótese juridicamente possível estiver coberta;
- toda desativação tiver substituição suficiente ou fundamento de
  `sem substituta`;
- toda lacuna preexistente estiver representada;
- não houver sobreposição injustificada;
- não houver pendência que afete a cobertura material; e
- derivados, validadores, testes e CI estiverem íntegros.

## Decisões semânticas consolidadas

Aplicam-se
[`docs/spec/decisoes-semanticas-regra.md`](../../../docs/spec/decisoes-semanticas-regra.md)
e
[`docs/spec/janelas-temporais-regra.md`](../../../docs/spec/janelas-temporais-regra.md).

1. Uma unidade representa um único ramo integral ou proporcional.
2. `integral: S` significa ausência de proporcionalização pelo tempo.
3. `tipo_calculo` é projeção de uma `FormaCalculo`; o enum legado não limita a
   ontologia jurídica.
4. `DATA_ADM_APOS`, `DATA_ADM_ATE` e `DATA_DIREITO_APOS` são inclusivos.
5. `DATA_DIREITO_ATE` é exclusivo e recebe o primeiro instante fora da janela.
6. Causa não informada ou prova insuficiente não equivalem a `causa_comum`.
7. Predicado sem coluna continua modelável e exige aferição humana.
8. ID legado não é reaproveitado para hipótese material diferente.
9. Mudança de base, ajuste ou limitador capaz de alterar o valor exige unidade
   distinta, mesmo que benefício e classe de causa permaneçam iguais.

## Escopo

### Regras proprietárias

- Bloco A: `regra-0001`, `regra-0002`, `regra-0004`.
- Bloco B: `regra-0006`, `regra-0007`, `regra-0008`, `regra-0009`.
- Bloco C: `regra-0019`, `regra-0020`, `regra-0021`, `regra-0022`.

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

Assim, a CF/88 original fecha em `16/12/1998`, a EC 20 fecha em
`31/12/2003`, o prazo legal até 31/12/2024 fecha em `01/01/2025` e a LCE
1.100/2021 começa em `18/10/2021`.

### T3 — Causas — decidido

O vocabulário mínimo é `acidente_em_servico`, `molestia_profissional`,
`doenca_catalogada` e `causa_comum`. A terceira classe corresponde à doença
grave, contagiosa ou incurável catalogada na norma temporalmente aplicável.

A causa é material quando altera elegibilidade, ramo, cálculo, paridade,
reajuste ou combinação normativa da matriz.

### T4 — Resultado admissível — decidido

Cada regra termina em `conferida_sem_alteracao`, `corrigida_mantida_ativa`,
`desativada_substituida`, `desativada_sem_substituta` ou, somente durante a
execução, `pendente_dependencia_localizada`.

### T5 — Lacunas — decidido

Cada combinação normativa possível é mapeada para zero, uma ou mais unidades.
Zero significa lacuna; mais de uma exige justificativa ou eliminação da
sobreposição. Regra nova tem origem `substituicao` ou `lacuna_preexistente`.

### T6 — Incapacidade sob a LCE 1.100/2021 — decidido na S4

Os §§ 13 e 14 do art. 30 são regras especiais do cálculo:

- causas qualificadas remetem à média do art. 24, sem proporcionalização;
- causa comum remete ao art. 26, que proporcionaliza em dias o valor calculado
  na forma do art. 24.

O art. 27 disciplina separadamente o reajuste: paridade para ingresso até
31/12/2003 e reajuste sem paridade para ingresso posterior. Por isso, a
combinação proporcional com paridade representada imperfeitamente por
`regra-0020` é juridicamente possível.

### T7 — Precedência e consistência — decidido na S5

Entre 18/10/2021 e 31/12/2024, primeiro se verifica se todos os requisitos e
critérios anteriores foram cumpridos no prazo do art. 4º da ECE 146/2021.
Quando ele incide, aplicam-se unidade, cálculo e reajuste preservados do Bloco B.
O Bloco C somente é selecionado quando essa preservação não incide.

Depois de 31/12/2024 não nasce novo enquadramento no art. 4º; direitos formados
até essa data continuam assegurados a qualquer tempo.

Cálculo inicial e reajuste são dimensões diferentes. A mesma média proporcional
pode coexistir com paridade ou sem paridade.

Q6-R está fechada para o catálogo auditado. Q6-S e Q6-T são dependências
operacionais porque o corpus ainda não demonstra onde a causa é obtida,
registrada e classificada no produto e no processo concessório.

### T8 — Fórmulas temporais do Bloco B — decidido na reabertura da S3

A composição inicial da S3 agrupava intervalos com fórmulas materialmente
distintas. A reabertura refina o Bloco B de oito para quatorze destinos.

Na regra geral da EC 41:

- de 31/12/2003 a 19/02/2004, as causas qualificadas usam a remuneração
  integral do cargo da LC 228/2000; a causa comum usa a mesma base com fração
  anual de 1/35 para homem ou 1/30 para mulher e piso de um salário mínimo;
- de 20/02/2004 a 12/03/2008, as causas qualificadas usam a média federal de
  80% iniciada pela MP 167/2004; a causa comum combina essa média com a fração
  anual e o piso da LC 228;
- desde 13/03/2008, as causas qualificadas usam a média do art. 45 da LCE
  432/2008; a causa comum usa essa média, depois dos limites dos §§ 9º e 10,
  proporcionalizada em dias pelo art. 17.

No art. 6º-A da EC 70:

- as causas qualificadas usam remuneração do cargo sem proporcionalização e com
  paridade em toda a janela retroativa;
- a causa comum usa a remuneração do cargo com a fração anual da LC 228 até
  12/03/2008 e com a fração em dias da LCE 432 desde 13/03/2008.

Os marcos `20/02/2004` e `13/03/2008` são inclusivos nos segmentos que começam
nessas datas; os limites superiores anteriores são exclusivos. Não há dia
sem cobertura nem sobreposição entre as fórmulas.

## Fluxo processual

- S0 — linha de base.
- S1 — contratos transversais T3–T5.
- S2 — Bloco A.
- S3 — Bloco B.
- S4 — Bloco C.
- S5 — consistência transversal.
- Reabertura da S3 — refinamento das fórmulas temporais do Bloco B.
- S6 — fechamento, após o merge da reabertura e conferência final.

As sessões são sequenciais e cada uma parte da `main` resultante da anterior.

### Registro das sessões

- [x] S0 — PR #92; `1393314118fad67e0057ee29d5c8740d01b71283`.
- [x] S1 — PR #93; `f68689841944000ab89db8379ff48be8e48aaf80`.
- [x] S2 — PR #94; `c722c6d3563e52626434c49a72126b516847585d`.
- [x] S3 — PR #95; `19b21ae55cd2845194dc77181562cd53cc033c71`.
- [x] S4 — PR #96; `ecd9f743391a8743ee536794ad74f72bd7cb2425`.
- [x] S5 — PR #97; `269ba448408848ceb3ba2844d791ab4658caf6b9`.
- [ ] Reabertura da S3 — PR #98 em revisão; commit-base
  `269ba448408848ceb3ba2844d791ab4658caf6b9`.
- [ ] S6 — não iniciada.

### Registro da S0 — Linha de base

A S0 inventariou as 11 regras, achados, fontes, precedentes e candidatos a
lacuna. Nenhuma regra deployável foi alterada.

### Registro da S1 — Contratos transversais

A S1 fechou o vocabulário de causa, o teste de materialidade, as situações T4 e
o protocolo T5. Q6-R ficou resolvida para a auditoria.

### Registro da S2 — Bloco A

`regra-0001`, `regra-0002` e `regra-0004` recebem
`desativada_substituida` e são substituídas por oito unidades: dois regimes
constitucionais vezes quatro classes de causa.

### Registro da S3 — Bloco B

`regra-0006`, `regra-0007`, `regra-0008` e `regra-0009` recebem
`desativada_substituida`. A proposta inicial criou oito destinos; a reabertura
da PR #98 os refina para quatorze por mudança material de base e ajuste.

A regra geral da EC 41 passa a nove unidades e o art. 6º-A passa a cinco. A
situação T4 e as classes de causa não mudam.

### Registro da S4 — Bloco C

`regra-0019`, `regra-0020`, `regra-0021` e `regra-0022` recebem
`desativada_substituida` e são substituídas por oito unidades: duas coortes de
ingresso vezes quatro classes de causa.

A `regra-0020` não é combinação impossível: a causa comum usa média
proporcional e o art. 27, I, assegura paridade à coorte até 2003.

### Registro da S5 — Consistência transversal

A S5 registra a precedência entre regime preservado e permanente, separa fórmula
inicial de reajuste e localiza Q6-S/Q6-T como dependência operacional.

### Registro da reabertura da S3 — Cálculo temporal

Foram autorados os arts. 43 e 44 da LC 228/2000, o art. 1º da MP 167/2004, a
redação original do art. 45 da LCE 432/2008 e os §§ 9º e 10 desse artigo.

Foram autoradas ou completadas as formas:

- remuneração integral do cargo sob a LC 228;
- remuneração do cargo proporcional pela LC 228;
- média de 80% da invalidez pós-MP 167;
- média federal proporcional pela fração anual da LC 228;
- média da LCE 432 proporcional em dias; e
- remuneração do cargo do art. 6º-A proporcional conforme a legislação temporal.

A cobertura jurídica das fórmulas do Bloco B fica completa. A única questão de
cálculo remanescente é operacional: como o IPERON trata frações de ano no
segmento em que a LC 228 fala em 1/35 ou 1/30 por ano de serviço.

## Entregável

O ciclo deverá conter catálogo correto e completo, regras erradas desativadas,
substitutas, mapa de substituições, matriz final de cobertura, formas de cálculo
e dispositivos, derivados sincronizados e CI integralmente verde.

A PR #98 entrega a matriz refinada do Bloco B, seis novas unidades, cinco formas
novas ou completadas e os dispositivos que fecham a linha temporal de cálculo.

## Resultado por regra

- [x] `regra-0001` — `desativada_substituida` na S2.
- [x] `regra-0002` — `desativada_substituida` na S2.
- [x] `regra-0004` — `desativada_substituida` na S2.
- [x] `regra-0006` — `desativada_substituida` na S3; destinos refinados na #98.
- [x] `regra-0007` — `desativada_substituida` na S3; destinos refinados na #98.
- [x] `regra-0008` — `desativada_substituida` na S3; destinos refinados na #98.
- [x] `regra-0009` — `desativada_substituida` na S3; destinos refinados na #98.
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
A semântica temporal pode ser reutilizada, mas a disposição da hipótese material
pertence ao ciclo proprietário.

## Fontes legais consultadas

- Constituição Federal, art. 40, nas redações original, EC 20/1998, EC 41/2003
  e EC 103/2019;
- EC 41/2003, art. 6º-A, com redação da EC 70/2012;
- ECE 146/2021, art. 4º;
- MP 167/2004 e Lei 10.887/2004, art. 1º;
- LC estadual 228/2000, especialmente arts. 43 e 44;
- LCE 432/2008, especialmente arts. 17, 20 e 45, §§ 9º e 10;
- LCE 672/2012, quanto à redação do art. 45 da LCE 432/2008;
- LCE 1.100/2021, especialmente arts. 24, 26, 27 e 30;
- dispositivos e formas de cálculo autorados no repositório; e
- decisões semânticas documentadas em `docs/spec/`.

## Pendências que permanecem abertas

- demonstrar o procedimento administrativo usado pelo IPERON para frações de
  ano na fórmula da LC 228;
- confirmar a projeção das fórmulas compostas no Sisprev;
- obter evidência operacional de Q6-S/Q6-T: entrada, persistência,
  classificação, reconhecimento de acidente e nexo profissional, rol temporal
  e integração com a seleção;
- transcrever o rol completo de doenças da LC 228 em unidade taxonômica própria;
- completar o gate humano das unidades;
- registrar decisão de completude e ato institucional antes de ativação; e
- executar a S6 após o merge da PR #98.

As dependências de fração, Q6 e projeção impedem simulação automática e ativação
institucional, mas não reabrem a existência das hipóteses nem a cobertura
jurídica da matriz proposta.

## Conclusão do ciclo

O ciclo permanece aberto. S0 a S5 estão concluídas. A reabertura da S3 está
materializada na PR #98 e precisa passar por validação, revisão e merge antes da
S6.

Com o refinamento, a proposta cobre todas as combinações materiais identificadas
no escopo e separa os segmentos cuja fórmula altera o valor. A S6 deverá
confirmar a completude contra os gates, distinguir fechamento da auditoria de
ativação no produto e não converter dependências operacionais em afirmações
jurídicas não demonstradas.
