---
type: Achado
id: achado-0034
nome: regra-0057 e regra-0058 fazem a integralidade dos proventos depender do sexo, e nenhum dispositivo do art. 5º da ECE 146/2021 o faz
situacao: aberto
severidade: informativo
verificacao: manual
natureza: dados
regras_afetadas:
  - /regras/regra-0057.md
  - /regras/regra-0058.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

`regra-0057` e `regra-0058` são a mesma regra — aposentadoria especial de
professor do art. 5º, § 4º, com proventos do § 6º, II e reajuste do § 7º, II da
ECE 146/2021 — e diferem em **exatamente dois campos**:

| campo      | `regra-0057` | `regra-0058` |
| ---------- | ------------ | ------------ |
| `sexo`     | MASCULINO    | FEMININO     |
| `integral` | **N**        | **S**        |

Todo o resto é idêntico, os quatro `dispositivos:` inclusive. E a
`fundamentacao_integral` é a mesma **byte a byte**, dizendo nas duas:

> Aposentadoria especial de professor, **com proventos integrais** (cálculo por
> média) e sem paridade [...]

Ou seja: as duas entregam ao servidor o mesmo texto afirmando proventos
integrais, e o cadastro grava resultados opostos conforme o sexo. Uma das duas
está errada, e o texto compartilhado não diz qual.

# Evidências

Conferido na publicação oficial da Emenda arquivada localmente
(`fontes-oficiais/arquivos/sapl-emenda_146.pdf`, SAPL/ALE-RO, no
`manifesto.yaml`). PDF digitalizado sem camada de texto, leitura visual das
páginas 4 a 6.

**Nenhum dos quatro dispositivos vinculados faz a base de cálculo depender do
sexo**, e a leitura é positiva, não por ausência:

- **`art-5-par-6-inc-ii`** — o único que define a base destas duas regras —
  manda apurar "à média aritmética simples das maiores remunerações [...]
  correspondentes a 80% (oitenta por cento) de todo o período contributivo".
  Não há qualquer menção a homem, mulher, professor ou professora.
- **`art-5-par-4`** diferencia por sexo, e diferencia **só idade e tempo de
  contribuição**: "os requisitos de idade e tempo de contribuição de que tratam
  os incisos I e II do *caput* serão: I - 51 anos de idade, se mulher, e 56
  anos, se homem; II - 25 anos de contribuição, se mulher, e 30 anos de
  contribuição, se homem". Nada sobre proventos.
- **`art-5-par-7-inc-ii`** trata de reajuste, não de base, e remete ao RGPS sem
  distinguir sexo. As duas regras gravam `paridade: N`, coerentemente.
- **`cf88/art-40-par-5/ec-103-2019`** concede ao professor redução de cinco anos
  na **idade mínima**; não trata de proventos.

O que a Emenda distingue por sexo, portanto, é **quando** se aposenta, nunca
**quanto** se recebe.

## O catálogo tem um controle, e ele é do mesmo inciso

`integral` no catálogo não significa "remuneração do cargo" — significa "100% da
base apurada, qualquer que seja ela". A prova está dentro do próprio art. 5º:
`regra-0055` e `regra-0056`, que são o par **não-magistério do mesmíssimo
§ 6º, II**, gravam `integral: S` com `tipo_calculo: Valor Médio` e usam a mesma
construção "com proventos integrais (cálculo por média)".

Somando as quatro regras do art. 5º, § 6º, II:

| regra                       | `integral` |
| --------------------------- | ---------- |
| `regra-0055` / `regra-0056` | S / S      |
| `regra-0058`                | S          |
| `regra-0057`                | **N**      |

Das quatro regras que aplicam o mesmo inciso, três gravam `S` e uma grava `N`.
A [conferência do lote](../../../docs/analysis/conferencia-criterio-dispositivo-voluntaria-cf88.md)
§5.5 estende esse controle a mais quatro regras da mesma Emenda (`0047`–`0050`),
todas `integral: S` com `Valor Médio`.

Isso **não** decide qual valor o par deve compartilhar — é campo deployável —,
mas registra de que lado está a prática do catálogo.

## O que este achado não é

`regra-0057` já figura no `achado-0009` (`P9_INTEGRAL_SEM_FUNDAMENTACAO`:
`integral: N` com `fundamentacao_proporcional` vazia). São problemas
**distintos** e o vínculo entre eles vale ser dito: o `achado-0009` é uma
detecção mecânica de campo vazio, cujo remédio possível é *preencher* a
fundamentação proporcional; este achado sustenta que talvez não haja
fundamentação proporcional a preencher, porque a regra pode não ser
proporcional. Se `integral: S` for o valor correto, o item de `regra-0057` no
`achado-0009` se resolve por consequência — a detecção deixa de existir. Se
`integral: N` for o correto, ele permanece e passa a alcançar também
`regra-0058`.

# Consequência prática

`INTEGRAL` é campo **deployável** e as duas regras são `simulavel: S`. O motor
lê a coluna, não a prosa. Hoje, dois professores com o mesmo tempo de
magistério, o mesmo ingresso e a mesma idade relativa recebem cálculos
diferentes de proventos **em razão do sexo**, com o mesmo texto de fundamentação
impresso no documento de concessão dos dois — texto que, nos dois casos, afirma
proventos integrais.

A diferença de tratamento por sexo em benefício previdenciário só se sustenta
onde a norma a estabelece, e aqui a norma faz o contrário: fixa idade e tempo
distintos justamente para **equalizar** o acesso, e mantém a base de cálculo
única.

# Questão a investigar

1. **Qual dos dois valores o par deve compartilhar.** A conferência mostra que
   os dois não podem estar ambos certos; a escolha é de quem responde pelo campo
   deployável. Sob a RFC 0006 o veículo indicado é um `Conjunto` `proposto`.

2. **Se a divergência é de origem ou de importação.** As duas linhas vizinhas da
   planilha congelada (`row_index` 57 e 58) diferem numa única célula de uma
   coluna `S/N`. Hipótese mais econômica: preenchimento de uma célula só,
   nunca reconferido. Não verificada — a importação registra o valor, não a sua
   história.

3. **Se o mesmo par diverge em `regra-0041` × `regra-0107`.** O §3.1 da
   [lista consolidada](../../../docs/analysis/achados-candidatos-da-conferencia.md)
   descreve o mesmo formato — string de fundamentação idêntica, `integral`,
   `tipo_calculo` e `paridade` opostos — em outro par. Se houver causa comum, é
   um achado transversal; este não a afirma.
