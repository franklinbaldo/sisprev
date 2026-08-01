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

> **Estado:** em execução — S0, S1 e S2 concluídas; S3 em revisão na PR #95.
> Este arquivo é a fonte única do plano, das decisões, do diário de execução e
> do relatório final do ciclo.

## Identificação

- Data de abertura: 01/08/2026
- Commit-base da execução: `79a112562a7a9172b9cda484f3ac4f6bf5b6853f`
- Issue de execução: [#89](https://github.com/franklinbaldo/sisprev/issues/89)
- S0: PR #92, merge `1393314118fad67e0057ee29d5c8740d01b71283`
- S1: PR #93, merge `f68689841944000ab89db8379ff48be8e48aaf80`
- S2: PR #94, merge `c722c6d3563e52626434c49a72126b516847585d`
- S3: PR #95, branch `cycle/1-s3-bloco-b`
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
`31/12/2003` e o prazo legal até 31/12/2024 fecha em `01/01/2025`.

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
- [ ] S3 — PR #95 em revisão; commit-base
  `c722c6d3563e52626434c49a72126b516847585d`.
- [ ] S4 — não iniciada.
- [ ] S5 — não iniciada.
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

As quatro regras misturam os dois ramos e não registram a causa que escolhe o
resultado. Além disso, mantêm a janela aberta além do prazo do art. 4º da ECE
146/2021. `regra-0008` e `regra-0009` também carregam fundamento no inciso III
do § 1º do art. 40, embora o art. 6º-A exija expressamente o inciso I.

No regime geral da EC 41, as três causas qualificadas conduzem à média sem
proporcionalização e sem paridade; a causa comum conduz à média proporcional ao
tempo e sem paridade.

No art. 6º-A da EC 70, as três causas qualificadas conduzem à remuneração do
cargo sem proporcionalização e com paridade; a causa comum conduz à remuneração
do cargo proporcional ao tempo e com paridade.

A S3 cria oito unidades e dois grupos atômicos 2:4. O conjunto
`ciclo-01-s3-bloco-b` deriva de `ciclo-01-s2-bloco-a`, preservando a proposta
anterior.

A janela comum é `[31/12/2003, 01/01/2025)`. O fecho exclusivo inclui todo o
dia 31/12/2024. A formulação antiga do `achado-0022`, que apontava
`31/12/2024` como valor do campo, foi corrigida.

## Entregável

O ciclo deverá conter catálogo correto e completo, regras erradas desativadas,
substitutas e regras de lacuna, mapa de substituições, matriz final de cobertura,
combinações impossíveis fundamentadas, formas de cálculo e dispositivos,
derivados sincronizados e CI integralmente verde.

A S3 entrega oito unidades auditadas, dois grupos cumulativos, correção da janela
até 31/12/2024 e registro das dependências que ainda impedem ativação.

## Resultado por regra

- [x] `regra-0001` — `desativada_substituida` na S2.
- [x] `regra-0002` — `desativada_substituida` na S2.
- [x] `regra-0004` — `desativada_substituida` na S2.
- [x] `regra-0006` — `desativada_substituida` na S3.
- [x] `regra-0007` — `desativada_substituida` na S3.
- [x] `regra-0008` — `desativada_substituida` na S3.
- [x] `regra-0009` — `desativada_substituida` na S3.
- [ ] `regra-0019` — decisão reservada à S4.
- [ ] `regra-0020` — decisão reservada à S4.
- [ ] `regra-0021` — decisão reservada à S4.
- [ ] `regra-0022` — decisão reservada à S4.

## Referências de outros ciclos

`regra-0003` e `regra-0005` foram consultadas apenas como referências de
continuidade histórica. Não são proprietárias do Ciclo 1 e não recebem alteração
nesta cadeia.

Achados e regras de outros ciclos, como `regra-0032`, permanecem com seus donos.
A correção geral da semântica temporal pode ser reutilizada, mas a disposição da
hipótese material pertence ao respectivo ciclo proprietário.

## Fontes legais consultadas

- Constituição Federal, art. 40, nas redações original, EC 20/1998 e EC
  41/2003;
- EC 41/2003, art. 6º-A, com redação da EC 70/2012;
- ECE 146/2021, art. 4º;
- Lei federal 10.887/2004, art. 1º;
- LC estadual 228/2000;
- LCE 432/2008, especialmente arts. 17, 20 e 45;
- LCE 672/2012, quanto à redação do art. 45 da LCE 432/2008;
- análises e transcrições oficiais registradas no repositório; e
- decisões semânticas documentadas em `docs/spec/`.

## Pendências que permanecem abertas

- transcrever e versionar dispositivos e fórmulas estaduais anteriores à LCE
  432/2008;
- fechar o cálculo do intervalo inicial de aplicação da EC 41/2003;
- projetar fielmente média proporcional e remuneração do cargo proporcional;
- confirmar o enum legado correspondente à remuneração do cargo efetivo;
- resolver Q6-S/Q6-T e o gate humano de classificação da causa;
- executar a S4 sobre `regra-0019` a `regra-0022`;
- harmonizar os três blocos na S5; e
- registrar ato institucional e decisão de completude antes de qualquer
  ativação.

Nenhuma dessas pendências é ocultada por ativação prematura: os grupos da S2 e
da S3 permanecem inativos e suas unidades, em elaboração.

## Conclusão do ciclo

O ciclo permanece aberto. S0, S1 e S2 estão concluídas; a S3 está materializada
na PR #95 e aguarda revisão e merge. S4, S5 e S6 ainda precisam ser executadas.

A conclusão final somente poderá declarar cobertura completa quando todas as
unidades necessárias estiverem prontas, as regras erradas estiverem efetivamente
retiradas do conjunto ativo e não restarem lacunas ou pendências materiais.
