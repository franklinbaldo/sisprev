# Decisão consolidada — janelas temporais das regras

- **Status:** decisão vigente da coordenação da auditoria
- **Decidido em:** 2026-08-01
- **Revisto em:** 2026-08-04, quanto a `DATA_ADM_APOS` — ver
  [Revisão de 2026-08-04](#revis%C3%A3o-de-2026-08-04)
- **Escopo:** campos `DATA_ADM_*` e `DATA_DIREITO_*`
- **Precedência:** este documento complementa
  [`decisoes-semanticas-regra.md`](decisoes-semanticas-regra.md) e prevalece
  sobre passagens históricas que descrevam `DATA_DIREITO_ATE` como inclusivo.

## Semântica das quatro fronteiras

- `DATA_ADM_APOS` é exclusivo (`>`) e grava o último dia do regime anterior.
- `DATA_ADM_ATE` é inclusivo (`<=`) e grava o último dia de ingresso coberto.
- `DATA_DIREITO_APOS` é inclusivo (`>=`) e grava o primeiro dia de
  implementação dos requisitos coberto.
- `DATA_DIREITO_ATE` é exclusivo (`<`) e grava o primeiro dia já fora da
  janela de implementação.

Nenhum dos dois eixos é simétrico consigo mesmo, e os dois `APOS` não
compartilham semântica. Na admissão, o par é `ATE` inclusivo e `APOS`
exclusivo, de modo que duas coortes que gravam a **mesma** data se encaixam
sem sobreposição nem buraco. No direito, é o contrário: `APOS` inclusivo e
`ATE` exclusivo.

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
- A coorte de ingresso posterior a 2003 grava `DATA_ADM_APOS = 31/12/2003`, e
  alcança quem ingressou a partir de 01/01/2004. A coorte anterior grava
  `DATA_ADM_ATE = 31/12/2003` e alcança quem ingressou até esse dia,
  inclusive. As duas gravam a mesma data porque uma a exclui e a outra a
  inclui.

## Revisão de 2026-08-04

A redação de 01/08 declarava `DATA_ADM_APOS` **inclusivo** e mandava gravar
`01/01/2004` no corte de ingresso. Esta revisão a substitui: o campo é
**exclusivo**, e o valor gravado é o último dia do regime anterior.

O que a motivou. A leitura inclusiva não convivia com `DATA_ADM_ATE`, que é
inclusivo e grava a mesma fronteira: com as duas coortes inclusivas, quem
ingressou em 31/12/2003 cai nas duas — e o que as separa é justamente a
paridade do art. 27. Com `01/01/2004` do lado inclusivo, o buraco muda de
lugar em vez de fechar: 01/01/2004 fica fora das duas. A leitura exclusiva do
`APOS` é a única das três que particiona a fronteira.

O que ela **não** alcança. `DATA_DIREITO_APOS` continua inclusivo, e por razão
independente: a leitura foi medida contra o catálogo, e não deduzida da
simetria do nome da coluna — sob a exclusiva, a maioria das regras negaria o
benefício no primeiro dia da norma que o funda. A população está no
[`achado-0053`](../../okf/regras-sisprev/achados/achado-0053.md). Os dois
eixos não compartilham semântica, e é isso que as duas revisões desta spec
têm em comum: cada fronteira foi decidida por medição, nunca por analogia com
a coluna vizinha.

## Regra de processo

Leituras anteriores permanecem úteis como histórico, mas não podem voltar a ser
tratadas como dúvida aberta nem orientar novos valores. Uma divergência futura
deve propor expressamente a revisão desta decisão, com evidência e impacto —
foi o que a revisão de 2026-08-04 fez, e é a única forma de mudar o que aqui
está.
