---
type: Achado
id: achado-0031
nome: regra-0037/0038 e regra-0043/0044 são os dois únicos pares do catálogo cuja fundamentação está preenchida só no registro masculino
situacao: aberto
severidade: informativo
verificacao: manual
natureza: dados
regras_afetadas:
  - /regras/regra-0037.md
  - /regras/regra-0038.md
  - /regras/regra-0043.md
  - /regras/regra-0044.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

Dois pares masculino/feminino têm o campo `FUNDAMENTACAO` preenchido no
registro masculino e **vazio** no feminino:

| par             | `fundamentacao` do masculino                                                            | `fundamentacao` do feminino |
| --------------- | --------------------------------------------------------------------------------------- | --------------------------- |
| `0037` / `0038` | "Art. 24 da Lei Complementar 1.100 de 18 de outubro de 2021"                            | *(vazia)*                   |
| `0043` / `0044` | "Art. 6º, § 2º, I, da EC 146/2021 (cálculo por integralidade e paridade remuneratória)" | *(vazia)*                   |

Em tudo o mais os dois pares divergem **apenas em `sexo`** — as janelas, os
campos de resultado, `fundamentacao_integral` (byte a byte) e a lista de
`dispositivos:` são idênticos dentro de cada par.

São, no catálogo inteiro, **os dois únicos casos** dessa assimetria. E nenhum
gate do repositório a detecta.

# Evidências

## A contagem

Percorridas as 112 regras, agrupadas por igualdade de todo o frontmatter exceto
`id`, `row_index`, `nome`, `dispositivos`, `sexo` e `fundamentacao` — isto é, os
grupos que divergem *no máximo* nesses campos —, quatro grupos têm mais de um
valor de `fundamentacao`:

| grupo                       | `fundamentacao` dentro do grupo                                                    |
| --------------------------- | ---------------------------------------------------------------------------------- |
| `0037` / `0038`             | **preenchida no masculino, vazia no feminino**                                     |
| `0043` / `0044`             | **preenchida no masculino, vazia no feminino**                                     |
| `0059`–`0064` (deficiência) | preenchida em `0061`/`0062` (os dois sexos do grau GRAVE), vazia nas outras quatro |
| `0072`–`0077` (policial)    | preenchida em `0072`/`0073` (os dois sexos), vazia nas outras quatro               |

Nos dois últimos grupos a divergência **respeita o par**: os dois sexos do mesmo
subgrupo carregam o mesmo texto, e o que separa preenchidos de vazios é outro
critério (o grau de deficiência em `0061`/`0062` — objeto do
[`achado-0021`](achado-0021.md) —, e o subgrupo em `0072`/`0073`). Só em
`0037`/`0038` e `0043`/`0044` a linha de corte cai **dentro** do par, entre o
homem e a mulher.

`verificacao: manual`, e a razão é a mesma do [`achado-0015`](achado-0015.md): a
contagem é reproduzível mas **nenhum detector a produz**. Saiu de consulta *ad
hoc* sobre o bundle.

## Por que nenhum gate a vê

`FUNDAMENTACAO` está **dentro** da chave material do
`P2_IGUALDADE_MATERIAL_ATIVA` — mas `sexo` também está, e já difere em cada
par. Logo o P2 nunca agruparia estes pares, com ou sem a assimetria: ela não
muda detecção nenhuma. O `P1_NOME_REPETIDO` os reporta, mas por causa do nome,
não do campo. E o `P9_INTEGRAL_SEM_FUNDAMENTACAO` olha a relação entre
`integral` e os campos `FUNDAMENTACAO_INTEGRAL`/`_PROPORCIONAL`, não este.

Ou seja: é um defeito de campo deployável **invisível a todo o aparato
mecânico**, e conferível só lendo os dois registros lado a lado. É por isso que
está autorado.

## O que cada texto ausente carrega

Não é a mesma perda nos dois pares.

Em `0037`/`0038` o texto que falta nomeia **`art. 24 da LCE 1.100/2021`** — o
dispositivo do trilho da média, que é justamente o que o
[`achado-0028`](achado-0028.md) mostra em conflito com a janela de admissão das
duas. A `regra-0038` entrega, portanto, um documento que não nomeia o artigo do
cálculo que ela aplica, embora o cite pelo mesmo número na
`fundamentacao_integral` ("artigos 24, 27, inciso II, e artigo 32"). A perda é
de reforço, não do único fundamento — e o vínculo `dispositivos:` de `0038`
inclui `lce-1100-2021/art-24/original` corretamente, porque a
`fundamentacao_integral` o cita.

Em `0043`/`0044` o texto que falta é uma **explicitação de efeito** — "(cálculo
por integralidade e paridade remuneratória)" — e não uma citação nova: o § 2º,
I do art. 6º já é nomeado pela `fundamentacao_integral` das duas. A perda é de
legibilidade do efeito, e nada em `dispositivos:` muda.

Em nenhum dos dois casos a assimetria produz vínculo faltando ou sobrando:
conferido item a item, `dispositivos:` de `0038` e de `0044` continua espelhando
o que os campos preenchidos daquela regra citam.

# Consequência prática

`FUNDAMENTACAO` é campo **deployável**. Duas servidoras e dois servidores em
situação juridicamente idêntica salvo o sexo recebem documentos de fundamentação
diferentes — e o mais curto é sempre o da mulher. Não há hipótese jurídica em que
isso seja intencional: o que separa `0037` de `0038` e `0043` de `0044` é a
idade e o tempo de contribuição exigidos, não o que se cita.

O achado não decide a direção da correção, porque as duas existem e são
opostas: copiar o texto para o registro feminino, ou apagá-lo do masculino
(alinhando os dois ao padrão do resto do catálogo, onde `FUNDAMENTACAO` está
vazia em quase todas as regras destes dois grupos). Apagar tem a vantagem de não
acrescentar citação a campo deployável; copiar tem a de não retirar informação
já entregue. É decisão de quem responde pelo campo.

Registro a consequência mecânica, para que não seja lida como efeito colateral
indesejado: **igualar o campo em qualquer direção deixa `sexo` como única
divergência material do par**, que é o estado correto segundo
[`docs/spec/regra.md`](../../../docs/spec/regra.md) ("divergência em critério
aferido já torna duas regras não idênticas"). O P2 continua não os agrupando.

# Questão a investigar

1. **Qual direção corrige.** Ver acima. A pista mais forte é o resto do
   catálogo: nas 24 regras do grupo LCE 1.100/2021 e nas 16 da ECE 146/2021,
   `FUNDAMENTACAO` está vazia na esmagadora maioria, o que sugere que o campo é
   preenchido por exceção e que o preenchido é o desvio — mas "a maioria está
   vazia" não é argumento de que preencher esteja errado.

2. **Se a assimetria tem origem comum com a de `0049`/`0050`.** Nos quatro pares
   do art. 6º da ECE 146/2021, `0043`/`0044` é o único com a assimetria e
   `0049`/`0050` o único com a data anômala ([`achado-0027`](achado-0027.md)).
   Os dois defeitos apontam para preenchimento manual por par, não por lote — o
   que, se confirmado, é informação sobre onde procurar os próximos. Hipótese.

3. **Se vale um detector.** Um check de "campos de texto divergentes entre
   regras que divergem só em `sexo`" seria barato e acharia exatamente estes
   dois casos hoje. Registro a possibilidade e **não a proponho**: o repositório
   já decidiu duas vezes na direção de menos maquinaria (RFC 0008), e um
   detector que hoje encontra dois casos conhecidos, ambos já autorados, não se
   justifica contra a alternativa de conferir e escrever.
