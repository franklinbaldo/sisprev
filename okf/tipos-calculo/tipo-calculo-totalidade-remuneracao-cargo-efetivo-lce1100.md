---
type: TipoCalculo
id: tipo-calculo-totalidade-remuneracao-cargo-efetivo-lce1100
nome: Totalidade da remuneração do cargo efetivo — LCE 1.100/2021
base:
  tipo: totalidade_remuneracao_cargo_efetivo
  dispositivos:
    - /dispositivos/lce-1100-2021/art-25/original.md
ajustes: []
limitadores: []
origem_legada:
  - tipo_calculo: Remuneração de Contribuição
    fidelidade: parcial
    justificativa: >-
      O rótulo legado fala em remuneração de contribuição, enquanto o art. 25
      manda usar a totalidade da remuneração no cargo efetivo. É o valor que
      as regras legadas de aposentadoria voluntária por idade e tempo de
      contribuição da coorte até 2003 gravam para esta mesma base (art. 32 da
      LCE 1.100/2021, ex.: `regra-0035`, `regra-0036`).
  - tipo_calculo: Valor Efetivo
    fidelidade: parcial
    justificativa: >-
      Mesma base (totalidade da remuneração do cargo efetivo, art. 25), sob
      rótulo legado diferente: é o valor que `regra-0019` grava, em
      produção, para a incapacidade permanente por causa qualificada da
      mesma coorte, citando o próprio art. 25 em `dispositivos:`. O enum do
      Sisprev não distingue a base pelo tipo de benefício — voluntária ou
      incapacidade —, mas o catálogo legado registra rótulos diferentes para
      cada um; a fórmula e a base são as mesmas (`## Critério de
      identidade`, `okf/spec/tipocalculo.md`).
autorado_por: franklinbaldo
autorado_em: 2026-07-31
---

# Como calcular

O art. 25 da LCE 1.100/2021 fixa como base a totalidade da remuneração no cargo
efetivo em que ocorre a aposentadoria para o servidor alcançado pelo trilho de
ingresso até 31 de dezembro de 2003.

O parágrafo único define a composição da remuneração e disciplina rubricas
variáveis ligadas à carga horária, desempenho ou produtividade. Essas médias
internas servem para compor determinadas parcelas da remuneração; não transformam
a base global em média das contribuições.

# Fórmula

```text
provento = subsídio_ou_vencimento
         + vantagens_permanentes
         + adicionais_individuais
         + vantagens_pessoais_permanentes
```

As rubricas variáveis são integradas conforme os critérios do parágrafo único do
art. 25.

# Entradas e saídas

Entradas: rubricas permanentes do cargo, histórico de carga horária e histórico
dos indicadores das vantagens permanentes variáveis, quando existentes.

Saída: `provento_inicial`, correspondente à remuneração do cargo efetivo formada
segundo o art. 25.

# Onde esta forma é usada

No Ciclo 1, descreve as dezenove unidades de causa qualificada (doença
catalogada, acidente em serviço, moléstia profissional) da coorte de
ingresso até 31/12/2003 da incapacidade permanente pela LCE 1.100/2021
(`incapacidade-lce1100-ate-2003-*`, exceto `causa-comum`), com paridade
(`tipo-calculo-remuneracao-cargo-proporcional-dias-lce1100` descreve a
unidade de causa comum da mesma coorte, que é proporcional em vez de
integral).
