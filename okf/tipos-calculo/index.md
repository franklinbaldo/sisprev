---
okf_version: '0.1'
---

# Tipos de cálculo

Um `type: TipoCalculo` por fórmula juridicamente distinta usada para apurar o
valor inicial de um benefício: a base, o que a proporcionaliza, os limites e
a fundamentação normativa de cada etapa. Cada fórmula materialmente diferente
constitui um tipo distinto — mesmos dados relevantes, submetidos à mesma
operação, produzindo o mesmo resultado, pertencem ao mesmo tipo; mudança
material na base, no método da média, na proporcionalização, nos limites ou
na ordem das operações cria outro.

Este bundle substitui a antiga divisão entre `FormaCalculo` (a fórmula
jurídica) e `TipoCalculo` (o rótulo do enum `TIPO_CALCULO` do Sisprev). As
duas entidades canônicas paralelas geravam confusão sem servir a uma
distinção que o domínio precisasse: o rótulo do Sisprev não é a identidade
da fórmula, é a sua **origem legada** — `origem_legada.tipo_calculo`, dentro
de cada documento. Um mesmo valor legado pode ser a origem de vários tipos
canônicos distintos (é o caso de `Proporcionalidade Dias`, abaixo); a
tradução de volta — que valor, rotina ou combinação de colunas o Sisprev usa
para cada tipo — é decisão de implantação, registrada em
`origem_legada.fidelidade`/`justificativa`, não parte da identidade do tipo.
A relação inversa também ocorre — um mesmo tipo canônico pode ter mais de
uma proveniência legada, quando a consolidação de dois documentos que
descreviam a mesma fórmula herda os rótulos que cada um citava (é o caso da
LCE 1.100/2021 abaixo, listada em `Proporcionalidade Dias` e em `Tipo Cálculo Nova Previdência`).

`tipo-calculo-nao-identificado.md` é a única exceção: não tem fórmula
própria, é o rótulo reservado às regras cuja derivação jurídica ainda não
foi feita.

# Tipos, por origem legada

**Valor Efetivo** (proventos sobre a remuneração ou vencimento do cargo,
integral ou proporcional):

- [Remuneração do cargo efetivo sob a EC 70/2012, proporcional por anos de serviço](tipo-calculo-remuneracao-cargo-ec70-proporcional-anos.md)
- [Remuneração integral do cargo efetivo sob a EC 70/2012](tipo-calculo-remuneracao-cargo-integral-ec70.md)
- [Remuneração integral do cargo efetivo na invalidez qualificada da LC 228/2000](tipo-calculo-remuneracao-cargo-integral-lc228.md)
- [Vencimento do cargo e vantagens, proporcional ao tempo — CF/88 original](tipo-calculo-remuneracao-cargo-proporcional-cf88-original.md)
- [Remuneração do cargo efetivo proporcional por anos na LC 228/2000](tipo-calculo-remuneracao-cargo-proporcional-lc228.md)
- [Totalidade da remuneração do cargo efetivo, proporcional ao tempo de contribuição](tipo-calculo-totalidade-proporcional-tempo.md)
- [Vencimento do cargo acrescido de adicional por tempo e vantagens — CF/88 original](tipo-calculo-totalidade-remuneracao-cargo-efetivo-cf88-original.md)
- [Totalidade da remuneração do cargo efetivo — CF, redação da EC 20/1998](tipo-calculo-totalidade-remuneracao-cargo-efetivo-ec20.md)

**Valor Médio** (proventos sobre a média das remunerações de contribuição):

- [Média das 80% maiores remunerações contributivas — LCE 1.100/2021](tipo-calculo-media-80-contribuicoes-lce1100.md)
- [Média das 80% maiores remunerações contributivas — LCE 432/2008](tipo-calculo-media-80-contribuicoes-lce432.md)
- [Média das 80% maiores remunerações contributivas — Lei 10.887/2004](tipo-calculo-media-80-contribuicoes-lei10887.md)
- [Média de 80% das remunerações de contribuição na invalidez da EC 41/2003](tipo-calculo-media-80-invalidez-ec41.md)
- [Média federal proporcional pela fração anual da LC 228/2000](tipo-calculo-media-proporcional-lc228-lei10887.md)

**Valor Médio com Redutor da Idade**:

- [Média das 80% maiores remunerações com redutor por idade — EC 41/2003](tipo-calculo-media-80-redutor-idade-ec41.md)

**Remuneração de Contribuição**:

- [Totalidade da remuneração do cargo efetivo — LCE 1.100/2021](tipo-calculo-totalidade-remuneracao-cargo-efetivo-lce1100.md)

**Valor Efetivo mais 70% do que exceder do Teto RGPS** (pensão da EC 41/2003):

- [Pensão sobre proventos do servidor aposentado — teto do RGPS e 70% do excedente](tipo-calculo-pensao-ec41-servidor-aposentado.md)
- [Pensão sobre remuneração do servidor em atividade — teto do RGPS e 70% do excedente](tipo-calculo-pensao-ec41-servidor-em-atividade.md)

**Tipo Cálculo Nova Previdência** (proveniência absorvida por consolidação —
ver `origem_legada` abaixo):

- [Média contributiva da LCE 1.100/2021, limitada e proporcional ao tempo em dias](tipo-calculo-media-proporcional-dias-lce1100.md)
  — também `Proporcionalidade Dias`, abaixo

**Tipo Cálculo Nova Previdência Pensão por morte**:

- [Pensão por cotas familiares e rateio igual — LCE 1.100/2021](tipo-calculo-pensao-cotas-lce1100.md)

**Proporcionalidade Dias** (três tipos canônicos distintos compartilham
esta origem legada — o rótulo nomeia o ajuste em dias, nunca a base, e por
isso não distingue, sozinho, fórmulas com bases diferentes; ver
`origem_legada.justificativa` em cada documento):

- [Média contributiva da LCE 1.100/2021, limitada e proporcional ao tempo em dias](tipo-calculo-media-proporcional-dias-lce1100.md)
  — também `Tipo Cálculo Nova Previdência`, acima
- [Média contributiva da LCE 432/2008, limitada e proporcional ao tempo em dias](tipo-calculo-media-proporcional-dias-lce432.md)
- [Remuneração do cargo efetivo sob a EC 70/2012, proporcional em dias](tipo-calculo-remuneracao-cargo-ec70-proporcional-dias.md)

**Sem fórmula própria**:

- [Não identificado](tipo-calculo-nao-identificado.md)
