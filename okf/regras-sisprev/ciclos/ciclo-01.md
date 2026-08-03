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

> **Estado:** auditoria jurídica concluída; ativação institucional bloqueada.
> A S6 está materializada na PR #99. Este arquivo é a fonte única das decisões,
> dos resultados e da conclusão do ciclo.

## Identificação

- Data de abertura: 01/08/2026
- Commit-base da execução: `79a112562a7a9172b9cda484f3ac4f6bf5b6853f`
- Issue de execução: [#89](https://github.com/franklinbaldo/sisprev/issues/89)
- S0: PR #92 — `1393314118fad67e0057ee29d5c8740d01b71283`
- S1: PR #93 — `f68689841944000ab89db8379ff48be8e48aaf80`
- S2: PR #94 — `c722c6d3563e52626434c49a72126b516847585d`
- S3: PR #95 — `19b21ae55cd2845194dc77181562cd53cc033c71`
- S4: PR #96 — `ecd9f743391a8743ee536794ad74f72bd7cb2425`
- S5: PR #97 — `269ba448408848ceb3ba2844d791ab4658caf6b9`
- Reabertura da S3: PR #98 — `74259861e5f59cdc9966ed819f1ae1b62f3bfeab`
- S6: PR #99 — branch `cycle/1-s6-fechamento`
- Responsável pelas decisões jurídicas: Franklin Baldo
- Data de fechamento institucional:
- Commit de fechamento institucional:

## Contexto acadêmico e histórico

O benefício atravessa quatro desenhos materiais: invalidez na CF/88 original;
invalidez após a EC 20/1998; regra geral e transição do art. 6º-A após a EC
41/2003; e incapacidade permanente sob a EC 103/2019 e a LCE 1.100/2021.

A auditoria distinguiu direito adquirido, preservação, regime permanente, base
de cálculo, proporcionalidade, paridade e reajuste. Mudança de base, ajuste ou
limitador capaz de alterar o valor foi tratada como mudança material, não como
mera troca de citação.

## Dimensão social

A seleção define a renda de servidor permanentemente incapaz para o trabalho.
Erro de causa, janela, cálculo ou paridade pode reduzir benefício devido,
produzir pagamento sem fundamento ou impedir a explicação do ato concessório.

A cadeia exigida é: fatos do requerente → classe de causa → unidade aplicável →
fórmula inicial → regime de reajuste. Ausência de informação ou prova
insuficiente não equivale a `causa_comum`.

## Objetivo

Representar corretamente todas as hipóteses de invalidez e incapacidade
permanente pertencentes ao escopo, preservando IDs legados como histórico e
criando unidades auditadas para cada combinação materialmente distinta.

## Critério de fechamento

Aplica-se
[`docs/spec/criterio-fechamento-ciclos.md`](../../../docs/spec/criterio-fechamento-ciclos.md).
O ciclo só pode ser encerrado institucionalmente quando o conjunto substituto
estiver vigente, as unidades estiverem `deployable`, houver decisões de
completude e existir ato institucional com efeito `valida`.

A cobertura jurídica pode ser concluída antes da ativação, desde que a diferença
seja expressa e nenhum ato ou validação seja inventado.

## Cotejo jurídico

### T1 — Uma unidade por ramo

Integral e proporcional são unidades distintas. `integral: S` significa apenas
ausência de proporcionalização pelo tempo.

### T2 — Janelas temporais

`DATA_ADM_APOS`, `DATA_ADM_ATE` e `DATA_DIREITO_APOS` são inclusivos.
`DATA_DIREITO_ATE` é exclusivo.

Fronteiras principais:

- CF/88 original: `[05/10/1988, 16/12/1998)`;
- EC 20/1998: `[16/12/1998, 31/12/2003)`;
- Bloco B: `[31/12/2003, 01/01/2025)`;
- LCE 1.100/2021: desde `18/10/2021`.

### T3 — Classes de causa

O vocabulário é `acidente_em_servico`, `molestia_profissional`,
`doenca_catalogada` e `causa_comum`. A causa comum exige exclusão probatória das
classes qualificadas.

### T4 — Situação das regras

As 11 regras proprietárias recebem `desativada_substituida`. Nenhuma hipótese
válida recebe `sem substituta` e nenhuma lacuna preexistente foi demonstrada no
escopo.

### T5 — Bloco A

As três regras legadas são substituídas por oito unidades: quatro classes de
causa na CF/88 original e quatro na EC 20/1998.

### T6 — Bloco B

As quatro regras legadas são substituídas por quatorze unidades.

Na regra geral da EC 41:

- de 31/12/2003 a 19/02/2004, aplica-se a LC 228/2000;
- de 20/02/2004 a 12/03/2008, aplica-se a média federal iniciada pela MP
  167/2004, combinada com a fração anual da LC 228 na causa comum;
- desde 13/03/2008, aplica-se a LCE 432/2008, com limites do art. 45 e fração em
  dias do art. 17 na causa comum.

No art. 6º-A, as causas qualificadas usam remuneração do cargo e paridade; a
causa comum usa a fração anual da LC 228 até 12/03/2008 e a fração em dias da
LCE 432 desde 13/03/2008.

### T7 — Bloco C

As quatro regras legadas são substituídas por oito unidades: quatro para ingresso
até 31/12/2003 e quatro para ingresso a partir de 01/01/2004.

As causas qualificadas usam a média do art. 24 sem proporcionalização; a causa
comum usa a média proporcional em dias do art. 26. O art. 27 disciplina
separadamente o reajuste.

A combinação média proporcional com paridade representada por `regra-0020` é
juridicamente possível.

### T8 — Precedência entre Blocos B e C

Entre 18/10/2021 e 31/12/2024, primeiro se verifica a preservação do art. 4º da
ECE 146/2021. Se os requisitos anteriores foram cumpridos no prazo, aplica-se a
unidade preservada do Bloco B. O Bloco C somente incide quando essa preservação
não se aplica.

Não há escolha livre entre regimes.

### T9 — Composição final proposta

`ciclo-01-s6-fechamento` deriva de
`ciclo-01-s3-reabertura-calculo` e resolve 131 membros:

- 101 regras legadas não afetadas; e
- 30 unidades auditadas substituindo as 11 regras proprietárias.

O conjunto permanece `proposto`. `catalogo-legado` continua sendo o único
conjunto vigente.

## Fluxo processual

- [x] S0 — inventário e linha de base.
- [x] S1 — contratos transversais.
- [x] S2 — Bloco A.
- [x] S3 — Bloco B inicial.
- [x] S4 — Bloco C.
- [x] S5 — consistência e precedência.
- [x] Reabertura da S3 — refinamento 8 → 14 no Bloco B.
- [x] S6 — prova de cobertura e composição final proposta na PR #99.
- [ ] Ativação institucional — depende do IPERON.

## Entregável

A cadeia produz:

- mapa final 11 → 30;
- matriz temporal completa;
- formas de cálculo autoradas;
- sobreposição intencional com regra de precedência;
- combinações impossíveis fundamentadas;
- 16 cenários representativos;
- composição final proposta com 131 membros; e
- distinção expressa entre conclusão jurídica e ativação institucional.

## Resultado por regra

- [x] `regra-0001` — `desativada_substituida`; Bloco A.
- [x] `regra-0002` — `desativada_substituida`; Bloco A.
- [x] `regra-0004` — `desativada_substituida`; Bloco A.
- [x] `regra-0006` — `desativada_substituida`; Bloco B refinado.
- [x] `regra-0007` — `desativada_substituida`; Bloco B refinado.
- [x] `regra-0008` — `desativada_substituida`; Bloco B refinado.
- [x] `regra-0009` — `desativada_substituida`; Bloco B refinado.
- [x] `regra-0019` — `desativada_substituida`; Bloco C.
- [x] `regra-0020` — `desativada_substituida`; média proporcional com paridade.
- [x] `regra-0021` — `desativada_substituida`; Bloco C.
- [x] `regra-0022` — `desativada_substituida`; Bloco C.

## Referências de outros ciclos

`regra-0003` e `regra-0005` foram consultadas apenas como referências de
continuidade histórica. Não são proprietárias do Ciclo 1.

Regras e achados de outros ciclos, como `regra-0032`, permanecem com seus donos.

## Fontes legais consultadas

- Constituição Federal, art. 40, nas redações original, EC 20/1998, EC 41/2003
  e EC 103/2019;
- EC 41/2003, art. 6º-A, com redação da EC 70/2012;
- ECE 146/2021, art. 4º;
- MP 167/2004 e Lei 10.887/2004, art. 1º;
- LC 228/2000, especialmente arts. 43 e 44;
- LCE 432/2008, especialmente arts. 17, 20 e 45;
- LCE 1.100/2021, especialmente arts. 24, 26, 27 e 30;
- dispositivos e formas de cálculo autorados no repositório; e
- decisões semânticas documentadas em `docs/spec/`.

## Pendências que permanecem abertas

As pendências abaixo não reabrem a matriz jurídica, mas bloqueiam simulação,
`deployable` e ativação:

- procedimento do IPERON para frações de ano sob a LC 228;
- Q6-S/Q6-T: captura, persistência e classificação da causa;
- projeção das fórmulas compostas no Sisprev;
- transcrição taxonômica completa do rol da LC 228;
- gate humano das 30 unidades;
- decisões de completude dos grupos e do conjunto; e
- ato institucional com efeito `valida`.

## Conclusão do ciclo

A **auditoria jurídica está concluída**: todas as combinações materiais
identificadas no escopo têm destino, as fronteiras estão fechadas, as fórmulas
estão autoradas e as sobreposições têm desempate.

O **Ciclo 1 não está encerrado institucionalmente**. O critério do repositório
exige substituição efetiva do catálogo vigente, e isso depende de unidades
`deployable`, decisões humanas de completude e ato do IPERON. A S6 registra o
bloqueio em vez de fabricar esses elementos.

A próxima ação legítima é a validação institucional da composição
`ciclo-01-s6-fechamento`. Até lá, o catálogo legado permanece vigente e a issue
#89 deve continuar aberta.
