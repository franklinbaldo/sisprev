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

> **Estado:** em execução — S0, S1 e S2 concluídas; S3 em revisão. Este arquivo
> é a fonte única do plano, das decisões, do diário de execução e do relatório
> final do ciclo.

## Identificação

- Data de abertura: 01/08/2026
- Commit-base da execução: `79a112562a7a9172b9cda484f3ac4f6bf5b6853f`
- Issue de execução: [#89](https://github.com/franklinbaldo/sisprev/issues/89)
- S0: PR #92, merge `1393314118fad67e0057ee29d5c8740d01b71283`
- S1: PR #93, merge `f68689841944000ab89db8379ff48be8e48aaf80`
- S2: PR #94, merge `c722c6d3563e52626434c49a72126b516847585d`
- S3: branch `cycle/1-s3-bloco-b`; PR a preencher
- Responsável pelas decisões jurídicas: Franklin Baldo
- Data de fechamento:
- Commit de fechamento:

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

Assim:

- a redação original da CF fecha em `16/12/1998`;
- a EC 20 fecha em `31/12/2003`; e
- o prazo legal até 31/12/2024 fecha em `01/01/2025`.

### T3 — Causas — decidido

Vocabulário mínimo:

- `acidente_em_servico`;
- `molestia_profissional`;
- `doenca_grave_catalogada`; e
- `causa_comum`.

A causa é material quando altera elegibilidade, ramo, cálculo, paridade,
reajuste ou combinação normativa da matriz.

### T4 — Resultado admissível — decidido

Cada regra termina em:

- `conferida_sem_alteracao`;
- `corrigida_mantida_ativa`;
- `desativada_substituida`;
- `desativada_sem_substituta`; ou
- `pendente_dependencia_localizada`, apenas durante a execução.

### T5 — Lacunas — decidido

Cada combinação normativa possível é mapeada para zero, uma ou mais regras.
Zero significa lacuna; mais de uma exige justificativa ou eliminação da
sobreposição. Regra nova tem origem `substituicao` ou `lacuna_preexistente`.

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
- [ ] S3 — em revisão; commit-base
  `c722c6d3563e52626434c49a72126b516847585d`.
- [ ] S4 — não iniciada.
- [ ] S5 — não iniciada.
- [ ] S6 — não iniciada.

## Registro da S0 — Linha de base

A S0 inventariou as 11 regras, seus achados, fontes, precedentes e candidatos a
lacuna. Nenhuma regra deployável foi alterada.

A correção documental central foi reconhecer que `DATA_ADM_APOS` é inclusivo:
`01/01/2004` inclui quem ingressou naquele dia. O defeito remanescente das regras
pós-2021 está no marco do direito, não no ingresso.

## Registro da S1 — Contratos transversais

A S1 fechou o vocabulário de causa, o teste de materialidade, as situações T4 e
o protocolo T5. Q6-R ficou resolvido para a auditoria; Q6-S e Q6-T permanecem
dependências operacionais localizadas.

## Registro da S2 — Bloco A

### Resultado T4

- `regra-0001`: `desativada_substituida`.
- `regra-0002`: `desativada_substituida`.
- `regra-0004`: `desativada_substituida`.

As três origens são substituídas por oito unidades: dois regimes constitucionais
vezes quatro classes de causa. Nenhuma hipótese fica sem substituta e nenhuma
lacuna preexistente foi demonstrada no Bloco A.

### Cobertura

| regime | qualificadas | causa comum |
| --- | --- | --- |
| CF/88 original | integral e paridade | proporcional e paridade |
| EC 20/1998 | totalidade e paridade | totalidade proporcional e paridade |

O conjunto cumulativo da S2 é `ciclo-01-s2-bloco-a`.

## Registro da S3 — Bloco B

### Resultado T4

- `regra-0006`: `desativada_substituida`.
- `regra-0007`: `desativada_substituida`.
- `regra-0008`: `desativada_substituida`.
- `regra-0009`: `desativada_substituida`.

As quatro regras misturam os dois ramos e não registram a causa que escolhe o
resultado. Além disso, mantêm a janela aberta além do prazo do art. 4º da ECE
146/2021. `regra-0008` e `regra-0009` também carregam fundamento no inciso III
do § 1º do art. 40, embora o art. 6º-A exija expressamente o inciso I.

### Matriz material

| regime | acidente | moléstia | doença catalogada | causa comum |
| --- | --- | --- | --- | --- |
| EC 41, regra geral | média sem proporção; sem paridade | média sem proporção; sem paridade | média sem proporção; sem paridade | média proporcional; sem paridade |
| EC 70, art. 6º-A | remuneração do cargo; paridade | remuneração do cargo; paridade | remuneração do cargo; paridade | remuneração do cargo proporcional; paridade |

A S3 cria oito unidades e dois grupos atômicos 2:4. O conjunto
`ciclo-01-s3-bloco-b` deriva de `ciclo-01-s2-bloco-a`, preservando a proposta
anterior.

A janela comum é `[31/12/2003, 01/01/2025)`. O fecho exclusivo inclui todo o
dia 31/12/2024. A formulação antiga do `achado-0022`, que apontava
`31/12/2024` como valor do campo, foi corrigida.

### Pendências localizadas

- dispositivos e fórmulas estaduais anteriores à LCE 432/2008;
- cálculo no intervalo inicial de aplicação da EC 41/2003;
- projeção fiel de média proporcional e remuneração do cargo proporcional;
- correspondência do enum legado com a remuneração do cargo efetivo;
- Q6-S/Q6-T e gate humano de classificação da causa; e
- ato institucional e decisão de completude.

Os dois grupos permanecem inativos e as unidades em elaboração. Essas
pendências devem ser resolvidas até S5 e não podem sobreviver ao fechamento.

## Resultado por regra

- [x] `regra-0001` — `desativada_substituida` na S2.
- [x] `regra-0002` — `desativada_substituida` na S2.
- [x] `regra-0004` — `desativada_substituida` na S2.
- [x] `regra-0006` — `desativada_substituida` na S3.
- [x] `regra-0007` — `desativada_substituida` na S3.
- [x] `regra-0008` — `desativada_substituida` na S3.
- [x] `regra-0009` — `desativada_substituida` na S3.
- [ ] `regra-0019`.
- [ ] `regra-0020`.
- [ ] `regra-0021`.
- [ ] `regra-0022`.

## Entregável final

O ciclo deverá conter:

1. catálogo correto e completo;
2. regras erradas desativadas;
3. substitutas e regras de lacuna;
4. mapa de substituições;
5. matriz final de cobertura;
6. combinações impossíveis fundamentadas;
7. formas de cálculo e dispositivos necessários;
8. derivados sincronizados; e
9. CI integralmente verde.
