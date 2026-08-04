# Resposta — "incompletude da cadeia normativa" nas fundamentações

> **Nota:** Relatório gerado por IA como apoio à decisão. **Não é artefato
> oficial**, não edita nenhuma `regra-*.md`, não altera schema, dados
> derivados (`data/regras-sisprev.csv`), motor ou `site/`. Responde a uma
> análise externa sobre remissões a norma complementar nas fundamentações.
> **Nada aqui é achado** — achado é documento autorado por humano em
> `achados/`.

## A pergunta

Uma análise externa reconstruiu as citações do catálogo e apontou que, em
várias regras, o dispositivo citado remete a norma complementar ("na forma da
lei", "especificadas em lei", "conforme critérios estabelecidos em lei") sem
que essa norma apareça entre os dispositivos citados. Quatro famílias foram
identificadas: o rol de doenças graves, o reajuste, o cálculo de proventos das
EC 41/2003 art. 6º e 6º-A, e a aposentadoria especial.

A pergunta é se isso é problema real, mal-entendido, já resolvido, ou o que se
propõe.

**Resumo:** os fatos de citação **conferem**; o enquadramento precisa de uma
correção; **não é defeito de `dispositivos:`, e "consertar" ali seria erro
grave**; é candidato a defeito de campo deployável; está parcialmente
registrado e não resolvido.

## 1. O que se confere

Verificado contra o bundle, item a item da primeira família:

| regra        | vincula do art. 20 da LCE 432/2008           | cita o § 9º? |
| ------------ | -------------------------------------------- | ------------ |
| `regra-0006` | `art-20-caput`                               | não          |
| `regra-0007` | `art-20-caput`, `art-20-par-14`              | não          |
| `regra-0008` | `art-20-caput`, **`art-20-par-9`**, `art-20` | sim          |
| `regra-0009` | `art-20-caput`, **`art-20-par-9`**, `art-20` | sim          |

E `regra-0019`/`0020` citam `lce-1100-2021/art-30-par-8`, que é o rol
equivalente do regime novo. O contraste interno é real, e é a melhor evidência
da análise: **a cadeia existe no catálogo e não foi puxada em algumas regras**.

## 2. A correção de enquadramento

A análise descreve a família do rol como "o dispositivo condiciona a
integralidade a doenças *especificadas em lei*, e o rol está fora da citação".
Para o art. 20 da LCE 432/2008 isso **não é exato**. O caput, verbatim:

> Art. 20. O servidor será aposentado por invalidez permanente, com proventos
> proporcionais ao tempo de contribuição, exceto se a invalidez for decorrente
> de acidente em serviço, moléstia profissional ou doença grave, contagiosa ou
> incurável.

Não há cláusula de delegação. O § 9º não *complementa por remissão* — ele
**define** o termo que o caput emprega ("Consideram-se doenças graves,
contagiosas ou incuráveis, **a que se refere o caput deste artigo**, a
tuberculose ativa; hanseníase; [...]").

A diferença importa. Delegação em aberto é norma de eficácia limitada; termo
definido noutro parágrafo do **mesmo artigo** é técnica redacional ordinária. A
moldura de delegação vale para a CF, art. 40, § 1º, I ("na forma da lei"), não
para o caput estadual. A afirmação sobrevive, mais fraca e ainda assim real:
**o critério que decide integral × proporcional tem seu conteúdo noutro
dispositivo, e em duas regras esse dispositivo não é citado.**

## 3. Por que não é defeito de `dispositivos:` — e por que "consertar" ali seria erro

Este é o ponto central da resposta.

Um vínculo `dispositivos:` afirma *"a fundamentação desta regra **cita** esta
provisão"*, nunca *"esta provisão a completa juridicamente"*
([`okf/spec/dispositivo.md`](../../okf/spec/dispositivo.md)). Acrescentar
`lce-432-2008/art-20-par-9` à `regra-0006` **falsificaria o vínculo**: a regra
não cita aquele parágrafo, e o catálogo passaria a afirmar que cita.

Isso não é preciosismo formal. É exatamente o modo de falha que a
[RFC 0008](../rfc/0008-a-fundamentacao-e-articulacao.md) documentou ao remover
o leitor de citações por expressão regular: um vínculo derivado por inferência
é uma acusação jurídica plausível e não verificada em campo consultável. A
inferência aqui ("o caput usa o termo, logo a regra cita a definição") é
melhor que uma regex, e continua sendo inferência.

O corpo P13.1 da `regra-0006` já registra a decisão, desde a PR #44:

> Pelo mesmo motivo o § 9º do art. 20 **não** entra aqui: nenhum campo desta
> regra o cita. Quem o cita é a `regra-0008`.

O que **pode** estar defeituoso é a `FUNDAMENTACAO*` — campo **deployável**,
que é o texto entregue ao servidor. Corrigi-lo é alterar o produto, não
auditar o catálogo.

## 4. Onde isso já estava previsto

A questão não é nova para o repositório: é a **quinta pergunta do P13.1**,
literalmente *"dispositivos que justificam cada critério e efeito"*. A RFC 0008
§5 registra que a fundamentação é **articulação, não lista** — encadeia os
dispositivos para que cada critério fique fundamentado —, e que a relação
`critério → dispositivo` fica como **conferência humana em prosa**, sem campo e
sem gate.

A análise externa, portanto, não encontrou um ponto cego do método: encontrou
uma instância concreta do trabalho que o método declara pendente. O que ela
acrescenta, e é valioso, é a **varredura sistemática** — as famílias 2, 3 e 4
não estavam registradas em lugar nenhum.

## 5. Estado por família

| família                                                    | registrado?               | avaliação                    |
| ---------------------------------------------------------- | ------------------------- | ---------------------------- |
| 1. Rol de doenças (`0001`, `0002`, `0004`, `0006`, `0007`) | corpos P13.1 de 0006–0009 | **candidato forte a achado** |
| 2. Reajuste (`art-62`/`art-63`, `art-40 §8º`) — 12 regras  | não                       | depende de juízo jurídico    |
| 3. Cálculo EC 41 art. 6º/6º-A (`0010`, `0101`, `0102`)     | não                       | candidato médio              |
| 4. Especial — `0068`/`0069`/`0070`                         | não                       | **tratar à parte, ver §6**   |
| Remissões genéricas (`art-25 § único`, 21 regras)          | —                         | **não é defeito**            |

Sobre a última linha: concordamos com a ressalva da própria análise. "Vantagens
pecuniárias permanentes do cargo, estabelecidos em Lei" é referência ao
ordenamento, não delegação de critério. Registrar isso como pendência
produziria 21 falsos positivos.

## 6. `0068`/`0069`/`0070` não são desta categoria

A análise as coloca na família 4, como lacuna. São **outra coisa, e mais
grave**: o art. 40, § 4º-C da CF exige que os requisitos venham de **lei
complementar do respectivo ente**, e o que se cita é o art. 8º da ECE 146/2021
— **emenda à Constituição estadual**, espécie normativa distinta.

Não é elo faltando: é elo de espécie incompatível com a exigida. Merece
tratamento próprio, e a conferência da ECE 146/2021 está hoje bloqueada — o
PDF disponível é digitalização sem camada de texto (ver
[`fontes-oficiais/PENDENCIAS.md`](../../fontes-oficiais/PENDENCIAS.md)).

## 7. Proposta

1. **Autorar achado para a família 1**, e só para ela por enquanto. É a única
   em que a evidência é interna e dispensa juízo sobre eficácia limitada: o
   critério decide **integral × proporcional** (dinheiro), a norma que o define
   **está autorada no corpus**, e o próprio catálogo se contradiz — `0008`/
   `0009` citam, `0006`/`0007` não, mesma norma, mesmo benefício, mesmo lote.
   Essa assimetria é o argumento inteiro.

2. **Tratar `0068`/`0069`/`0070` à parte**, como incompatibilidade de espécie
   normativa, quando a ECE 146/2021 for conferível.

3. **Não registrar as remissões genéricas.**

4. **Deixar as famílias 2 e 3 em espera**, com a razão dita: decidir se
   "conforme critérios estabelecidos em lei" configura eficácia limitada ou
   referência ao ordenamento é juízo jurídico que a conferência de citação não
   alcança — e é a mesma ressalva que a análise externa fez, corretamente,
   sobre si mesma.

5. **Não propor nenhum vínculo novo**, em nenhuma família. A correção, onde
   couber, é no texto da fundamentação, e é ato de quem responde pelo produto.

## 8. Uma divergência que não se resolve aqui

A análise afirma que "nenhum dos **54** achados de auditoria referenciados
cobre essa questão". Este repositório tem **17** achados autorados nesta data.
Não é possível reconciliar os dois números com o corpus daqui — o material
parece referir-se a outro conjunto, talvez de origem institucional distinta.

A afirmação de cobertura fica, portanto, **não verificada nesta resposta**. O
que se pode dizer do corpus deste repositório é o da tabela do §5: a família 1
está registrada nos corpos P13.1 de `0006`–`0009` e as demais não estão em
lugar nenhum.
