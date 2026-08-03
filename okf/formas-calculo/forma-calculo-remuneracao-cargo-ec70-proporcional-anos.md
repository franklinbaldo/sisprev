---
type: FormaCalculo
id: forma-calculo-remuneracao-cargo-ec70-proporcional-anos
nome: Remuneração do cargo efetivo sob a EC 70/2012, proporcional por anos de serviço
base:
  tipo: totalidade_remuneracao_cargo_efetivo
  dispositivos:
    - /dispositivos/ec-41-2003/art-6a/ec-70-2012.md
ajustes:
  - tipo: proporcional_tempo_contribuicao
    ordem: 1
    dispositivos:
      - /dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
      - /dispositivos/lce-228-2000/art-43-par-unico-inc-i/original.md
limitadores: []
projecao_sisprev:
  tipo_calculo: Valor Efetivo
  fidelidade: parcial
  justificativa: >-
    `Valor Efetivo` nomeia a base — a totalidade da remuneração do cargo efetivo
    trazida pelo art. 6º-A —, e a proporcionalidade é carregada por `integral: N`
    na mesma linha. `Proporcionalidade Dias` seria pior que a omissão: no uso do
    Sisprev esse rótulo designa fração medida em dias, e aqui a fração é anual.
    Fica sem coluna a medida da fração, 1/35 por ano para homem e 1/30 para
    mulher.
autorado_por: franklinbaldo
autorado_em: 2026-08-03
---

# Como calcular

O art. 6º-A da EC 41/2003, incluído pela EC 70/2012, substitui a base
contributiva por proventos calculados sobre a remuneração do cargo efetivo. O
inciso I do § 1º do art. 40 mantém o ramo proporcional para as causas comuns.

Esta forma cobre o segmento em que a medida da proporção é **anual**: direitos
formados de 31/12/2003 a 12/03/2008, em que o art. 43, parágrafo único, I, da
LC 228/2000 fornece 1/35 por ano para homem e 1/30 para mulher.

A leitura é conforme à hierarquia normativa: a lei estadual fornece a fração,
mas a sua remissão ordinária à própria base não afasta a base constitucional
especial posterior do art. 6º-A. A remuneração do cargo vem da EC 70; só o
ajuste proporcional varia conforme a legislação aplicável à data do direito.

# Fórmula

```
denominador = 35, se homem; 30, se mulher
fração = min(1, anos_de_serviço / denominador)
provento = remuneração_do_cargo_efetivo × fração
```

A paridade do art. 6º-A é regime de reajuste e fica fora da fórmula de
concessão.

# Entradas e saídas

Entradas: remuneração do cargo efetivo, sexo e tempo de serviço em anos.

Saída: provento inicial proporcional, em moeda, nunca superior à remuneração do
cargo efetivo.

# Onde esta forma é usada

No Ciclo 1, descreve a unidade de causa comum do art. 6º-A/EC 70 no segmento
anterior à LCE 432/2008. O segmento seguinte, com fração medida em dias, é
[forma própria](forma-calculo-remuneracao-cargo-ec70-proporcional-dias.md) — a
medida do ajuste é o que distingue as duas, e uma forma que abrigasse as duas
não teria projeção única no enum do Sisprev.
