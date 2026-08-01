---
type: FormaCalculo
id: forma-calculo-remuneracao-cargo-proporcional-ec70
nome: Remuneração do cargo efetivo sob a EC 70/2012, proporcional ao tempo
base:
  tipo: totalidade_remuneracao_cargo_efetivo
  dispositivos:
    - /dispositivos/ec-41-2003/art-6a/ec-70-2012.md
ajustes:
  - tipo: proporcional_tempo_contribuicao
    dispositivos:
      - /dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
      - /dispositivos/lce-432-2008/art-17/original.md
limitadores: []
projecao_sisprev:
  tipo_calculo: Não identificado
  fidelidade: sem_representacao
  justificativa: >-
    O enum não possui rótulo que combine remuneração do cargo efetivo com
    proporcionalidade ao tempo. `Valor Efetivo` omite a fração e
    `Proporcionalidade Dias` omite a base; `Remuneração de Contribuição` não
    identifica com segurança a totalidade da remuneração do cargo.
autorado_por: franklinbaldo
autorado_em: 2026-08-01
---

# Como calcular

O art. 6º-A da EC 41/2003, incluído pela EC 70/2012, substitui a base contributiva
por proventos calculados com base na remuneração do cargo efetivo. O inciso I do
§ 1º do art. 40 mantém o ramo proporcional para as causas comuns. O art. 17 da
LCE 432/2008 fornece a mecânica da fração e determina a contagem em dias.

A leitura precisa ser conforme à hierarquia normativa: o § 1º do art. 17, ao
remeter genericamente à média do art. 45, não pode afastar a base constitucional
especial posterior do art. 6º-A. Conservam-se do art. 17 o numerador, o
denominador e a granularidade em dias; a base vem do art. 6º-A.

# Fórmula

```
base = totalidade_da_remuneração_do_cargo_efetivo
fração = min(1, tempo_contribuição_dias / tempo_exigido_dias)
provento = base × fração
```

A proporção reduz a base e nunca a amplia. A paridade do art. 6º-A é regime de
reajuste e fica fora desta fórmula de concessão.

# Entradas e saídas

Entradas: remuneração do cargo efetivo, tempo total de contribuição em dias e
tempo exigido em dias para a aposentadoria voluntária de referência.

Saída: provento inicial proporcional, em moeda, nunca superior à remuneração do
cargo efetivo.

O denominador concreto depende da aposentadoria voluntária correspondente ao
caso. A instrução deve registrar qual hipótese forneceu esse tempo exigido.

# Onde esta forma é usada

No Ciclo 1, descreve a unidade de causa comum do art. 6º-A/EC 70. A fórmula é
conhecida, mas não possui representação fiel no enum legado; por isso a unidade
permanece não simulável enquanto o produto não tiver projeção adequada.
