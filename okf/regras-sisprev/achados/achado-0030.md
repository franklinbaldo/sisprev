---
type: Achado
id: achado-0030
nome: As oito regras do art. 6º da ECE 146/2021 citam só os parágrafos de resultado; o dispositivo dos requisitos — que traz o pedágio e é o que funda o desdobramento por sexo — não é citado nem existe no corpus
situacao: aberto
severidade: informativo
verificacao: manual
natureza: juridica
regras_afetadas:
  - /regras/regra-0043.md
  - /regras/regra-0044.md
  - /regras/regra-0045.md
  - /regras/regra-0046.md
  - /regras/regra-0047.md
  - /regras/regra-0048.md
  - /regras/regra-0049.md
  - /regras/regra-0050.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

As oito regras `0043`–`0050` são a transição estadual do **art. 6º da ECE
146/2021**, em quatro pares (comum e magistério × integralidade e média). Os
campos de fundamentação das oito citam, sem exceção, apenas os **parágrafos de
resultado** do artigo:

| regras        | o que a `fundamentacao_integral` nomeia do art. 6º |
| ------------- | -------------------------------------------------- |
| `0043`/`0044` | § 2º, I e § 3º, I                                  |
| `0045`/`0046` | §§ 1º e 2º, I e § 3º, I                            |
| `0047`/`0048` | § 2º, II e § 3º, II                                |
| `0049`/`0050` | §§ 1º e 2º, II e § 3º, II                          |

O *caput* do art. 6º e seus **incisos I a IV** — onde estão idade mínima, tempo
de contribuição, tempo de serviço público, tempo no cargo e o **período
adicional de contribuição** (o pedágio) — não são citados por nenhuma das oito,
não são vinculados em `dispositivos:` e **não existem como texto em lugar nenhum
do corpus**.

Isso já estava registrado como padrão pela
[conferência do lote](../../../docs/analysis/conferencia-criterio-dispositivo-voluntaria-cf88.md)
§5.1, sobre 16 regras. Este achado o autora para as oito do art. 6º, com o texto
oficial em mãos — e ao fazê-lo **corrige** a conclusão daquela conferência sobre
o critério `sexo`, que estava errada.

# Evidências

## O texto que falta, lido na fonte oficial

Conferido por **leitura visual** da p. 7 do PDF oficial da ALE-RO arquivado
localmente (`fontes-oficiais/arquivos/sapl-emenda_146.pdf`, sha256
`947726c7…`, `manifesto.yaml`). O arquivo é digitalização sem camada de texto —
`pdftotext` extrai 10 caracteres —, então nenhuma conclusão aqui se apoia em
`grep`, e **`grep` vazio nesta norma não é prova de ausência**. Verbatim:

> **Art. 6º** O servidor público que tenha ingressado em cargo efetivo até a
> data de entrada em vigor desta Emenda Constitucional poderá aposentar-se
> voluntariamente quando preencher, cumulativamente, os seguintes requisitos:
>
> **I** - 57 (cinquenta e sete) anos de idade, se mulher, e 60 (sessenta) anos,
> se homem;
>
> **II** - 30 (trinta) anos de contribuição, se mulher, e 35 (trinta e cinco)
> anos de contribuição, se homem;
>
> **III** - 20 (vinte) anos de efetivo exercício no serviço público e 5 (cinco)
> anos no cargo efetivo em que se der a aposentadoria; e
>
> **IV** - período adicional de contribuição correspondente ao tempo que, na
> data de entrada em vigor desta Emenda Constitucional, faltaria para atingir o
> tempo mínimo de contribuição referido no inciso II.

E o § 1º, que **é** citado por `0045`/`0046` e `0049`/`0050`:

> **§ 1º** Para o professor que comprovar exclusivamente tempo de efetivo
> exercício das funções de magistério na educação infantil e no ensino
> fundamental e médio serão reduzidos, **para ambos os sexos**, os requisitos de
> idade e tempo de contribuição em 5 (cinco) anos.

## A correção: o desdobramento por sexo está fundado, e no dispositivo que falta

A conferência do lote concluiu, para o subgrupo A (estas oito):

> `sexo` (o eixo que separa cada par) | MASCULINO / FEMININO | **nenhum
> dispositivo vinculado distingue por sexo** — `art-6-par-1` diz o oposto: "para
> ambos os sexos" | ❌

**A primeira metade é verdadeira e a segunda é leitura errada do § 1º.** A
oração "para ambos os sexos" governa a **redução de cinco anos**, não os
requisitos: ela diz que o professor e a professora recebem *a mesma* redução, e
para isso pressupõe que haja requisitos distintos a reduzir. Lê-la como negação
do desdobramento é tomar uma norma sobre o desconto por uma norma sobre a base.

E a base existe, com os números na cara: os incisos I e II do *caput*
distinguem 57/60 anos de idade e 30/35 anos de contribuição. Aplicado o § 1º, o
par de magistério fica em 52/55 e 25/30. **O critério `sexo` de `0043`–`0050`
está juridicamente fundado** — no único dispositivo do art. 6º que as oito
regras **não** citam.

A distinção entre as duas metades importa porque elas pedem ações opostas:
"critério sem fundamento" é candidato a supressão do critério; "critério fundado
em provisão não citada" é fundamentação incompleta. Este é o segundo caso, e é o
mesmo modo de falha que o [`achado-0019`](achado-0019.md) já corrigiu para as
doze regras de transição **federal**: lá o item de candidatura afirmava que
`sexo` não teria dispositivo fundante nas doze, e a conferência contra as
publicações originais mostrou que tinha, nos arts. 2º e 6º da EC 41/2003 e no
art. 3º da EC 47/2005. A mesma acusação, o mesmo desfecho, agora na emenda
estadual — com a diferença de que aqui o dispositivo continua sem transcrição.

## Uma confirmação lateral que a mesma leitura fecha

`tabelapontuacao: N` nas oito é **correto**, e isso responde o ponto em aberto 3
da conferência do lote ("a relação entre `tabelapontuacao` e os arts. 5º/6º não
é conferível hoje"). Lidos os dois artigos na mesma fonte: o art. 5º tem um
inciso **V** que exige "somatório da idade e do tempo de contribuição [...]
equivalente a 86 (oitenta e seis) pontos, se mulher, e 96 (noventa e seis)
pontos, se homem" (p. 5), com progressão anual nos §§ 2º e 5º; **o art. 6º não
tem inciso de pontuação nenhum**. Logo `N` no subgrupo do art. 6º e `S` no do
art. 5º é exatamente a distinção legal, e o campo está certo dos dois lados.
Registro aqui porque é a mesma leitura de página que sustenta o resto do achado;
as regras do art. 5º estão fora deste conjunto.

## O contraste dentro do mesmo benefício

O regime **permanente** do mesmo benefício não tem este defeito. `regra-0035` a
`regra-0038` citam e vinculam `lce-1100-2021/art-32`, cujo documento no corpus
transcreve o artigo inteiro — *caput* e incisos I a IV — e cujo inciso I diz "62
(sessenta e dois) anos de idade, se mulher, e 65 (sessenta e cinco) anos de
idade, se homem". Ali o critério `sexo` fecha contra provisão citada, vinculada
**e** transcrita.

É o mesmo par de artigos, a mesma estrutura, a mesma auditoria: a diferença é
que a regra permanente nomeia o artigo dos requisitos e a transitória nomeia só
os parágrafos de cálculo.

# Consequência prática

O que o cadastro não carrega, aqui, é quase tudo o que decide o caso. Das cinco
exigências do art. 6º — idade, tempo de contribuição, 20 anos de serviço
público, 5 anos no cargo e o pedágio do inciso IV — **nenhuma tem coluna no
Sisprev**, e as oito regras são `simulavel: S`. O que o motor afere nelas é
`tipo_de_beneficio`, `sexo`, `apos_especial` e duas janelas de data; o pedágio,
que é o requisito característico de uma regra de transição, não aparece em campo
nem em texto.

Isso não faz da seleção um erro — o simulador é deliberadamente conservador e só
conclui "não excluída" (RFC 0002). Faz do **documento entregue** uma
fundamentação que nomeia como se paga e como se reajusta, e não nomeia a
provisão de cujos requisitos o servidor foi considerado titular.

**Nenhum vínculo é proposto.** `dispositivos:` das oito espelha fielmente o que
os campos citam — conferido item a item, nada listado deixa de ser citado e
nada citado deixa de ser listado. Vincular o *caput* do art. 6º agora seria
inventar citação que a fundamentação não faz, que é precisamente o erro que a
RFC 0008 baniu. O que se propõe é **transcrever** o dispositivo, o que é ato
autoral independente da citação:

- `ece-146-2021/art-6-caput/original` — ou, se a decomposição sob demanda
  preferir, `art-6-inc-i` a `art-6-inc-iv`, cada um com a cadeia até o *caput*.
  O texto verbatim está acima, com a fonte e o sha256 que o comprovam.
- A vigência a declarar depende da mesma pendência do
  [`achado-0027`](achado-0027.md): o art. 13 da Emenda entra em vigor "na data
  de sua publicação", e a publicação não está arquivada.

# Questão a investigar

1. **Se a omissão é convenção de redação ou defeito.** O § 2º abre com "os
   proventos das aposentadorias concedidas nos termos do disposto **neste
   artigo**", o que remete ao *caput* por dentro — de modo que citar "art. 6º,
   § 2º, I" pode ser tido como citar o artigo. É a hipótese que o ponto em
   aberto 6 da conferência do lote formula, e ela decide se há oito correções de
   produto a fazer ou nenhuma. Não a resolvo: a granularidade do vínculo é a
   provisão, e a provisão citada é o parágrafo.

2. **Se o pedágio do inciso IV pede coluna.** É o requisito que individua esta
   transição e nada no catálogo o registra. Pedir coluna é alterar o Sisprev —
   fora do escopo desta auditoria —, e a saída dentro do escopo é a
   fundamentação nomear o inciso. Registrado como pedido ao IPERON, não como
   correção.

3. **Se a leitura do § 1º precisa ser corrigida onde já foi escrita.** A
   conferência do lote é relatório de apoio à decisão, não artefato oficial, e
   este achado a contradiz num ponto. Se outras conferências herdaram a mesma
   leitura de "para ambos os sexos" — a mesma oração aparece no art. 34 da LCE
   1.100/2021, e lá ela está no *caput*, governando os incisos, o que é
   situação diferente —, cada uma precisa ser reconferida por si. Não estendo a
   correção além das oito deste achado.
