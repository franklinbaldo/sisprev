---
type: /spec/especificacao.md
id: janelas-temporais-regra
nome: Janelas temporais das regras
# A parte desta decisão que uma máquina consegue conferir contra o catálogo
# proposto. Não é uma segunda fonte de verdade: é este documento, estruturado
# no ponto exato em que ele manda gravar um valor. Quem decide continua sendo
# quem escreve aqui; `scripts/conferir_decisoes_da_spec.py` só compara.
#
# `operador` não é lido como regra — entra na mensagem de falha, para que quem
# vir o gate vermelho leia a razão do valor, e não apenas o valor.
decisoes_verificaveis:
  - campo: data_adm_apos
    operador: inclusivo
    valor: 01/01/2004 00:00
    aplica_a_grupos:
      - incapacidade-lce1100-ingresso-apos-2003
---

# Decisão consolidada — janelas temporais das regras

- **Status:** decisão vigente da coordenação da auditoria
- **Decidido em:** 2026-08-01
- **Escopo:** campos `DATA_ADM_*` e `DATA_DIREITO_*`
- **Precedência:** este documento complementa
  [`decisoes-semanticas-regra.md`](decisoes-semanticas-regra.md) e prevalece
  sobre passagens históricas que descrevam `DATA_ADM_APOS` como exclusivo ou
  `DATA_DIREITO_ATE` como inclusivo.

## Semântica das quatro fronteiras

- `DATA_ADM_APOS` é inclusivo (`>=`) e grava o primeiro dia de ingresso
  coberto.
- `DATA_ADM_ATE` é inclusivo (`<=`) e grava o último dia de ingresso coberto.
- `DATA_DIREITO_APOS` é inclusivo (`>=`) e grava o primeiro dia de
  implementação dos requisitos coberto.
- `DATA_DIREITO_ATE` é exclusivo (`<`) e grava o primeiro dia já fora da
  janela de implementação.

Os dois campos `APOS` são inclusivos, mas os campos `ATE` não são simétricos:
a admissão usa limite inclusivo; o direito usa fecho exclusivo.

## Como representar prazos legais inclusivos

Quando a norma exige que os requisitos sejam implementados **até** determinada
data, inclusive, `DATA_DIREITO_ATE` recebe o dia seguinte.

Exemplo:

> Requisitos cumpridos até 31/12/2024.

Representação correta:

```yaml
data_direito_ate: 01/01/2025 00:00
```

A janela termina no primeiro instante de 01/01/2025 e, portanto, inclui todo o
dia 31/12/2024.

## Consequências para o Ciclo 1

- As unidades históricas com redação original da CF/88 fecham em
  `16/12/1998`, incluindo 15/12/1998.
- As unidades da EC 20/1998 fecham em `31/12/2003`, incluindo 30/12/2003.
- As unidades preservadas pelo art. 4º da ECE 146/2021 fecham em
  `01/01/2025`, incluindo 31/12/2024.
- `DATA_ADM_APOS = 01/01/2004` inclui quem ingressou em 01/01/2004.

## Regra de processo

Leituras anteriores permanecem úteis como histórico, mas não podem voltar a ser
tratadas como dúvida aberta nem orientar novos valores. Uma divergência futura
deve propor expressamente a revisão desta decisão, com evidência e impacto.
