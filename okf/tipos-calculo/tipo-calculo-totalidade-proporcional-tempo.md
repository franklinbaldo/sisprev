---
type: TipoCalculo
id: tipo-calculo-totalidade-proporcional-tempo
nome: Totalidade da remuneração do cargo efetivo, proporcional ao tempo de contribuição
base:
  tipo: totalidade_remuneracao_cargo_efetivo
  dispositivos:
    - /dispositivos/cf88/art-40-par-3/ec-20-1998.md
ajustes:
  - tipo: proporcional_tempo_contribuicao
    ordem: 1
    dispositivos:
      - /dispositivos/cf88/art-40-par-1-inc-i/ec-20-1998.md
      - /dispositivos/cf88/art-40-par-1-inc-ii/ec-20-1998.md
      - /dispositivos/cf88/art-40-par-1-inc-iii-al-a/ec-20-1998.md
      - /dispositivos/ec-20-1998/art-4/original.md
      - /dispositivos/lce-68-1992/art-137/original.md
      - /dispositivos/lce-228-2000/art-43-par-unico-inc-i/original.md
limitadores: []
origem_legada:
  tipo_calculo: Valor Efetivo
  fidelidade: parcial
  justificativa: >-
    `Valor Efetivo` nomeia a base — a totalidade da remuneração do cargo
    efetivo — e é o rótulo que a `regra-0002`, origem desta hipótese, já
    gravava. A proporcionalidade não se perde: ela é carregada por
    `integral: N` na mesma linha, e o par recupera o que nenhum dos dois
    campos diz sozinho. O que fica sem coluna é a **medida** da fração, e isso
    é limitação do Sisprev, não indefinição da auditoria.
autorado_por: openai-codex
autorado_em: 2026-08-08
---

# Como calcular

A **base** vem do art. 40, § 3º, na redação da EC 20/1998: a totalidade da
remuneração do cargo efetivo em que ocorre a aposentadoria.

O **ajuste** tem dois ramos constitucionais que não devem ser confundidos: o
art. 40, § 1º, I determina a proporcionalidade da invalidez por causa comum, e
o inciso II determina a da aposentadoria compulsória. Nenhum dos dois fornece
literalmente o denominador. Para ambos, esta forma adota 35 anos para homem e
30 para mulher por interpretação sistemática do § 1º, III, alínea “a”, na
mesma redação constitucional.

Na invalidez, a ponte é reforçada por duas evidências contemporâneas e
convergentes, com pesos jurídicos distintos:

- a IN SEAP 5/1999, art. 5º, § 1º, aplicou 1/35 e 1/30 ao mesmo ramo
  constitucional no SIPEC federal; é evidência interpretativa, não norma
  vinculante para Rondônia;
- desde 31/01/2000, o art. 43, parágrafo único, I, da LCE 228/2000 passou a
  fixar diretamente essas frações no regime estadual.

Para o trecho anterior da janela, a conclusão é assumidamente **interpretação
sistemática**, e não literalidade: a EC 20 exige proporcionalidade, usa 35/30
como tempos contributivos integrais na mesma unidade normativa, e a orientação
federal editada quatro meses depois confirma que essa era uma leitura
contemporânea do texto. A explicitação estadual posterior corrobora a fórmula,
mas não é aplicada retroativamente.

O art. 4º da EC 20 converte o tempo de serviço admitido pela legislação vigente
em tempo de contribuição. O art. 137 da LCE 68/1992, não revogado pela LCE
228/2000, disciplina a apuração: dias são convertidos em anos de 365 dias; o
resto de até 180 dias é desprezado e o resto superior a 180 dias arredonda para
um ano. Logo, a operação é anual, não uma divisão silenciosa por 10.950 ou
12.775 dias.

O piso de um salário mínimo decorre, durante toda a janela, da aplicação
subsidiária determinada pelo art. 40, § 12, combinada com o art. 201, § 2º, e é
explicitado no art. 43, parágrafo único, II, da LCE 228/2000 a partir de
31/01/2000. Ele permanece no corpo porque o vocabulário estrutural de
`limitadores` ainda não representa piso simples.

# Fórmula

```text
anos_inteiros = piso(tempo_contribuição_dias / 365)
resto = tempo_contribuição_dias mod 365
anos_convertidos = anos_inteiros + (1 se resto > 180; 0 se resto <= 180)
exigido = 35, se homem; 30, se mulher
fração = min(1, anos_convertidos / exigido)
provento_bruto = remuneração_cargo_efetivo × fração
provento = max(salário_mínimo, provento_bruto)
```

# Entradas e saídas

| entrada                     | tipo                  | origem                                     |
| --------------------------- | --------------------- | ------------------------------------------ |
| `remuneracao_cargo_efetivo` | moeda                 | totalidade da remuneração no cargo efetivo |
| `tempo_contribuicao_dias`   | inteiro, dias         | tempo apurado no caso                      |
| `sexo`                      | masculino ou feminino | define o denominador de 35 ou 30 anos      |
| `salario_minimo`            | moeda                 | piso vigente na concessão                  |

Saída: `provento_mensal`, limitado à própria base e sujeito ao piso de um
salário mínimo.
