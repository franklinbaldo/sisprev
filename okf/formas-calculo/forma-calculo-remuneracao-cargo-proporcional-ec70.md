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
    ordem: 1
    dispositivos:
      - /dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
      - /dispositivos/lce-228-2000/art-43-par-unico-inc-i/original.md
      - /dispositivos/lce-432-2008/art-17/original.md
limitadores: []
projecao_sisprev:
  tipo_calculo: Não identificado
  fidelidade: sem_representacao
  justificativa: >-
    O enum não possui rótulo que combine remuneração do cargo efetivo com
    proporcionalidade ao tempo. `Valor Efetivo` omite a fração,
    `Proporcionalidade Dias` omite a base e não descreve o segmento anual da LC
    228, e `Remuneração de Contribuição` não identifica com segurança a
    totalidade da remuneração do cargo.
autorado_por: franklinbaldo
autorado_em: 2026-08-01
---

# Como calcular

O art. 6º-A da EC 41/2003, incluído pela EC 70/2012, substitui a base contributiva
por proventos calculados com base na remuneração do cargo efetivo. O inciso I do
§ 1º do art. 40 mantém o ramo proporcional para as causas comuns.

A medida da proporção é temporalmente versionada:

- para direitos formados de 31/12/2003 a 12/03/2008, o art. 43, parágrafo único,
  I, da LC 228/2000 fornece 1/35 por ano para homem e 1/30 para mulher;
- desde 13/03/2008, o art. 17 da LCE 432/2008 fornece a razão entre o tempo total
  e o tempo exigido para a aposentadoria voluntária correspondente, com contagem
  em dias.

A leitura é conforme à hierarquia normativa: as leis estaduais fornecem a
fração, mas suas remissões ordinárias à própria base não podem afastar a base
constitucional especial posterior do art. 6º-A. A remuneração do cargo vem da
EC 70; somente o ajuste proporcional varia conforme a legislação aplicável à
data do direito.

# Fórmula

Segmento da LC 228:

```
denominador = 35, se homem; 30, se mulher
fração = min(1, anos_de_serviço / denominador)
provento = remuneração_do_cargo_efetivo × fração
```

Segmento da LCE 432:

```
fração = min(1, tempo_contribuição_dias / tempo_exigido_dias)
provento = remuneração_do_cargo_efetivo × fração
```

A paridade do art. 6º-A é regime de reajuste e fica fora da fórmula de concessão.

# Entradas e saídas

Entradas comuns: remuneração do cargo efetivo, sexo e tempo de contribuição.
No segmento da LC 228, o tempo e o denominador são expressos em anos; no
segmento da LCE 432, em dias e contra a aposentadoria voluntária correspondente.

Saída: provento inicial proporcional, em moeda, nunca superior à remuneração do
cargo efetivo.

# Onde esta forma é usada

No Ciclo 1, descreve a unidade de causa comum do art. 6º-A/EC 70 em toda a janela
retroativa alcançada pela emenda. A fórmula é conhecida, mas não possui
representação fiel no enum legado; a unidade permanece não simulável enquanto o
produto não tiver projeção adequada.
