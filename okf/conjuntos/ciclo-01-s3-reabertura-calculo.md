---
type: Conjunto
id: ciclo-01-s3-reabertura-calculo
nome: Ciclo 1 — reabertura do Bloco B — fórmulas temporais
situacao: proposto
base: ciclo-01-s5-consistencia
---

# Motivo da reabertura

A S5 identificou que o Bloco B ainda tratava como uma única unidade intervalos
em que a base ou a granularidade da fórmula mudavam. Pelo teste de materialidade
do Ciclo 1, isso não é simples mudança de citação: cálculo diferente exige
unidade diferente.

A reabertura não muda a situação T4 das regras legadas nem cria nova classe de
causa. Ela refina os destinos já propostos e atualiza `ciclo-01-s3-bloco-b`.

# Resultado

O grupo da regra geral da EC 41 passa de quatro para nove unidades:

- três causas qualificadas com remuneração do cargo de 31/12/2003 a 19/02/2004;
- causa comum com remuneração proporcional no mesmo intervalo;
- três causas qualificadas com média desde 20/02/2004;
- causa comum com média federal e fração anual da LC 228 de 20/02/2004 a
  12/03/2008; e
- causa comum com média limitada e fração em dias da LCE 432 desde 13/03/2008.

O grupo do art. 6º-A passa de quatro para cinco unidades. As causas qualificadas
continuam em uma unidade por causa porque a base constitucional retroativa é a
mesma. A causa comum é dividida entre a fração anual da LC 228 até 12/03/2008 e
a fração em dias da LCE 432 desde 13/03/2008.

O Bloco B passa, portanto, de oito para quatorze destinos. Não há lacuna nem
sobreposição entre os segmentos: os marcos superiores são exclusivos e os
inferiores, inclusivos.

# Fontes e formas autoradas

Foram autorados os arts. 43 e 44 da LC 228/2000, a MP 167/2004, a redação
original do art. 45 da LCE 432/2008 e os §§ 9º e 10 desse artigo.

As formas temporais são:

- `forma-calculo-remuneracao-cargo-integral-lc228`;
- `forma-calculo-remuneracao-cargo-proporcional-lc228`;
- `forma-calculo-media-80-invalidez-ec41`;
- `forma-calculo-media-proporcional-lc228-lei10887`;
- `forma-calculo-media-proporcional-dias-lce432`; e
- `forma-calculo-remuneracao-cargo-ec70-proporcional-anos`; e
- `forma-calculo-remuneracao-cargo-ec70-proporcional-dias`.

As duas últimas eram uma só, `forma-calculo-remuneracao-cargo-proporcional-ec70`,
que abrigava os dois segmentos de medida do art. 6º-A num componente único. Foram
partidas em 03/08/2026: a medida do ajuste é o que as distingue — fração anual da
LC 228 até 12/03/2008, razão em dias do art. 17 da LCE 432 desde 13/03/2008 —, e uma
forma que abrigasse as duas não teria projeção única no enum do Sisprev.

# Pendência residual

A LC 228 expressa a proporcionalidade por ano de serviço e não contém, no texto
consultado, regra de conversão de frações de ano para dias. A estrutura e os
denominadores estão fechados; antes de simulação é necessário demonstrar o
procedimento administrativo de contagem usado pelo IPERON para períodos que não
completam ano inteiro.

Essa pendência não reabre a existência ou a cobertura das hipóteses, mas impede
atribuir `simulavel: S` às unidades afetadas.

Q6-S/Q6-T, projeção no produto, gate humano e ato institucional permanecem como
registrados na S5.
