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

Descreve as dezenove unidades de causa qualificada (doença catalogada,
acidente em serviço, moléstia profissional) da coorte de ingresso até
31/12/2003 da incapacidade permanente pela LCE 1.100/2021
(`incapacidade-lce1100-ate-2003-*`, exceto `causa-comum`), com paridade.
Também fundamenta, por remissão,
`tipo-calculo-remuneracao-cargo-proporcional-dias-lce1100`, que aplica a
mesma base à unidade de causa comum da mesma coorte, proporcionalizada
pelo art. 26 em vez de integral.

# Por que a base do art. 25 se aplica à coorte de ingresso até 31/12/2003

O servidor que ingressou no serviço público até 31/12/2003 pode requerer a
aposentadoria por incapacidade permanente pela legislação permanente
atualmente em vigor, a LCE 1.100/2021 — não depende de invocar direito
adquirido a regime anterior nem de norma revogada.

Dentro desse regime vigente, o art. 24, no próprio *caput*, disciplina
expressamente a base de cálculo dos servidores que ingressaram **após**
31/12/2003 (média das 80% maiores remunerações contributivas). O art. 25
disciplina, também de forma expressa, a base dos que ingressaram **até**
aquela data (totalidade da remuneração do cargo efetivo). Os dois artigos
não competem entre si: são normas complementares que distribuem a base de
cálculo por coorte de ingresso, e ambos integram o mesmo regime
permanente.

O art. 30 remete a base de cálculo da incapacidade permanente ao art. 24
por duas vias. Nas causas qualificadas (doença catalogada, acidente em
serviço, moléstia profissional), o § 13 remete diretamente ao art. 24. Na
causa comum, o § 14 remete ao art. 26, cujo § 1º, por sua vez, remete a
fração proporcional à média do art. 24. As duas vias têm mecanismo
diferente — remissão direta numa, encadeada na outra —, mas o resultado
textual invocável é o mesmo: aplicar, também à coorte de ingresso até
31/12/2003, a base do art. 24.

Essas remissões podem ser invocadas para sustentar esse entendimento.
*Data venia*, considera-se equivocada essa leitura, por três razões
conjugadas. **Primeira**: ela amplia o âmbito pessoal do art. 24 — que,
no próprio texto, disciplina a coorte posterior a 2003 — para alcançar
também a coorte anterior, sem que o art. 24 o diga. **Segunda**: ela
reduz o alcance do art. 25, que disciplina expressamente essa mesma
coorte, sem que os §§ 13 ou 14 do art. 30 tenham declarado a
inaplicabilidade do art. 25 à incapacidade. **Terceira**: ela cria, por
inferência a partir de uma remissão, a combinação entre média
contributiva (art. 24) e paridade (art. 27, I) — regime que a
LCE 1.100/2021 não institui em nenhuma outra hipótese: a coorte que
calcula pela média é, em todas as demais hipóteses da lei, a coorte sem
paridade. Cálculo inicial e reajustamento são categorias distintas, e essa
combinação não é impossível em abstrato — mas não há disposição
inequívoca instituindo esse regime híbrido, nem precedente jurisprudencial
ou administrativo interno seguro que o autorize por inferência.

A interpretação sistemática que preserva a divisão vigente de bases por
coorte — art. 25 para quem ingressou até 31/12/2003, art. 24 para quem
ingressou depois, cada qual com o reajustamento que a lei lhe atribui — é
a que este catálogo adota para a carga atual. Isso não trata as duas
leituras como igualmente válidas: a remissão ao art. 24 é registrada
porque existe no texto e pode ser invocada, não porque seja considerada
tão consistente quanto a leitura pelo art. 25. A fórmula poderá ser
revista caso manifestação jurídica institucional, precedente vinculante
ou decisão judicial estabeleça entendimento contrário.
