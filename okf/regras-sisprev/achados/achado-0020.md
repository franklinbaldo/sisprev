---
type: Achado
id: achado-0020
nome: O campo nome não tem padrão, e 109 das 112 regras divergem em ao menos uma dimensão
situacao: aberto
severidade: informativo
verificacao: manual
natureza: modelagem
regras_afetadas:
  - /regras/regra-0001.md
  - /regras/regra-0002.md
  - /regras/regra-0016.md
  - /regras/regra-0017.md
  - /regras/regra-0020.md
  - /regras/regra-0059.md
  - /regras/regra-0060.md
  - /regras/regra-0061.md
  - /regras/regra-0062.md
  - /regras/regra-0063.md
  - /regras/regra-0064.md
  - /regras/regra-0078.md
  - /regras/regra-0079.md
  - /regras/regra-0084.md
  - /regras/regra-0109.md
  - /regras/regra-0110.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

`nome` não tem padrão. Das 112 regras, **109 divergem em ao menos uma das cinco
dimensões abaixo**; as únicas três sem desvio nenhum são `regra-0003`,
`regra-0005` e `regra-0032`.

`regras_afetadas` lista os casos em que o desvio já tem consequência
demonstrada noutro achado ou na conferência — a lista completa por dimensão
está em Evidências, e alcança quase o catálogo inteiro.

# Evidências

## D1 — nome repetido: 94 regras

Quarenta e um nomes distintos são compartilhados por duas ou mais regras,
cobrindo **94 das 112**. Faixas: `0001–0002`, `0006–0009`, `0012–0022`,
`0028–0031`, `0033–0083`, `0085–0086`, `0093–0112`.

O detector `P1_NOME_REPETIDO` já reporta cada grupo, e com
`requires_achado: false` — porque nome repetido, isolado, não é defeito: pode
ser rótulo curto de regras legitimamente distintas.

## D2 — o critério que discrimina não está no nome

O campo `sexo` tem **quatro** estados no catálogo, e o nome nunca menciona
nenhum deles:

| `sexo`    | regras | tem marca no nome? |
| --------- | ------ | ------------------ |
| MASCULINO | 38     | **0**              |
| FEMININO  | 34     | **0**              |
| AMBOS     | 27     | **0**              |
| *(vazio)* | 13     | **0**              |

Para as 27 regras `AMBOS`, não marcar o sexo no nome é defensável: não há
critério a discriminar. **Para as 72 de MASCULINO ou FEMININO, a omissão é o
defeito**, e o dano é medível: **32 grupos de nome idêntico contêm mais de um
valor de `sexo`**. São regras que o operador só distingue abrindo o cadastro.

Faixas das 72: `0016–0017`, `0028–0031`, `0033–0064`, `0072–0083`,
`0085–0086`, `0093–0112`.

Duas observações que a contagem por valor trouxe e que valem registro próprio:

- **`AMBOS` não é benigno.** É onde o `P9_SEXO_FUNDAMENTACAO` fica cego: ele
  compara `sexo` com as palavras "homem"/"mulher" no texto, e com `AMBOS`
  qualquer das duas parece coerente. É exatamente o ponto cego que deixou a
  `regra-0084` sem detecção e sem achado até o `achado-0017` — ela é `AMBOS` e
  cita só a alínea feminina da LC 51/1985.

- **Treze regras têm `sexo` vazio**, e o vazio é real. Conferido: valor `''`
  do tipo `str`, não `None` nem espaço em branco — e, o que importa mais,
  **vazio já na importação congelada** (`data/raw/regras-sisprev.csv`, coluna
  `SEXO`, `row_index` 3, 4, 5, 23–26 e 87–92). Não é artefato do bundle nem
  de agrupamento: é estado do dado recebido. Se vazio equivale a `AMBOS` ou é
  preenchimento faltando é questão de domínio que este achado não decide — é
  território da Q3, onde `sexo` está registrado como a primeira coluna de
  domínio a fechar — e que nenhum outro achado registra.

  Nota lateral que decorre disso: duas das três regras sem desvio de nome
  algum (`regra-0003` e `regra-0005`) estão entre as de `sexo` vazio. Não têm
  desvio em D2 porque não há sexo a marcar — o que mostra que "sem desvio" aqui
  mede conformidade de forma, não qualidade do cadastro.

O contraste decisivo está dentro do próprio catálogo. Em `0059`–`0064`, o
**grau de deficiência** (grave/moderada/leve) aparece **no nome e em nenhum
outro lugar** — e é ele que separa as seis, com números distintos na lei (art.
35, I a III da LCE 1.100/2021: 20/25, 24/29, 28/33 anos de contribuição). Ali o
nome carrega um critério material; no sexo, nunca carrega.

Isso torna o nome **estruturalmente ambíguo**: às vezes é o único portador de um
critério que decide o caso, às vezes omite o critério que decide. Quem lê não
tem como saber em qual dos dois casos está.

## D3 — sem separador entre rótulo e fundamento: 10 regras

`0001–0002`, `0010–0013`, `0068–0070`, `0084`. As outras 102 usam `-`.

## D4 — grafia abreviada ou irregular da citação: 37 regras

O nome cita norma, e a grafia varia: `EC nº` (44×) contra `E.C` (8×) e
`Emenda Constitucional` (1×); `LC` (25×) contra `Lei Complementar` (19×); `§ 1º`
(48×) contra `§ 1` sem ordinal (6×); e `Incapacidade Perm.` abreviado.

Faixas: `0001–0002`, `0006–0009`, `0012–0013`, `0019–0022`, `0027`,
`0030–0031`, `0035–0038`, `0041–0042`, `0080–0083`, `0087–0092`, `0107–0112`.

## D5 — rótulo variante para o mesmo benefício: 17 regras

O mesmo benefício aparece sob rótulos diferentes:

| benefício                | rótulos encontrados                                                          |
| ------------------------ | ---------------------------------------------------------------------------- |
| invalidez / incapacidade | `Invalidez` (4), `Incapacidade Perm.` (4), `Aposentadoria por Invalidez` (3) |
| policial civil           | `Voluntária do Policial Civil` (12), `Voluntária Policial Civil` (4)         |
| compulsória              | `Compulsória` (4), `Aposentadoria Compulsória` (2)                           |
| pensão por morte         | `Pensão por Morte` (9), `Pensão Morte Art. …` (2)                            |

Faixas: `0001–0002`, `0004`, `0012–0013`, `0019–0026`, `0082–0083`,
`0109–0110`.

# Consequência prática

`nome` é campo **deployável** — aparece no documento e nas telas de seleção.
Duas consequências distintas:

**Para quem opera.** Numa regra `simulavel: N`, a indicação depende de triagem
humana, e o nome é o primeiro rótulo que a pessoa lê. Trinta e seis pares com
nome idêntico diferindo apenas por sexo obrigam a abrir o cadastro para saber
qual é qual.

**Para a auditoria, e aqui é preciso ser exato.** `nome` está **fora** da chave
material do `P2_IGUALDADE_MATERIAL_ATIVA` e `FUNDAMENTACAO*` está **dentro**.
Logo renomear **limpa o `P1_NOME_REPETIDO` sem tocar no P2** — e é justamente
por isso que padronizar nome, sozinho, pode **piorar** o diagnóstico: apaga o
sintoma visível e deixa intacta a igualdade material.

O caso de `0059`–`0064` mostra o par correto de atos. `0059`≡`0063` e
`0060`≡`0064` são grupos P2 ativos, e o grau que os distingue está só no nome.
Diferenciar a **fundamentação** dissolve o grupo honestamente, porque a
fundamentação é material; ajustar o nome torna a distinção legível. **São dois
atos, e nenhum substitui o outro.**

# Questão a investigar

1. **Qual padrão adotar.** Uma forma que satisfaz as cinco dimensões seria
   `<Benefício> — <critérios discriminantes> — <fundamento>`, com o benefício
   vindo do domínio de `TIPO DE BENEFICIO` (que já é enum, então não se
   inventa rótulo), os critérios discriminantes explicitados sempre que
   existirem, e a citação em grafia única. Não é decisão da auditoria:
   `nome` é deployável, e padronizá-lo em 109 regras é alteração de produto.

2. **Se o padrão deve ser gate.** Um detector de conformidade de nome é
   barato de escrever e caro de acertar — a parte difícil não é a grafia, é
   "os critérios discriminantes estão no nome?", que exige saber quais são, e
   é exatamente o que falta quando não há coluna (grau de deficiência, causa
   da incapacidade). Um gate sobre a parte fácil daria a impressão de padrão
   cumprido com a parte que importa em aberto.

3. **A ordem dos atos importa e é contraintuitiva.** Se o nome for padronizado
   antes das fundamentações, o `P1_NOME_REPETIDO` cala e os grupos P2
   permanecem — o catálogo pareceria mais saudável tendo mudado nada de
   material. A recomendação é o inverso: **fundamentação primeiro, nome
   depois**.

4. **Onde a proposta deve morar.** Sendo `nome` deployável, a correção proposta
   pertence ao catálogo auditado (RFC 0004), não a uma edição em
   `regra-*.md` — mesmo caminho da unidade
   `policial-civil-voluntaria-masculino`, que propõe correção de fundamentação
   sem alterar a origem.

# Como a população respondeu

As dezesseis regras alcançadas responderam `corrigida`: todas receberam `nome` pelo padrão de facetas em ordem de anamnese, e o `P1_NOME_REPETIDO` foi a zero no catálogo.

**O achado permanece `aberto`.** Sob o modelo de estados do catálogo, um defeito real não se fecha por selo no próprio achado: quem responde é a regra, em `disposicao_de_achados`, e é ali que o tratamento fica registrado com autor e data. `improcedente` afirmaria que a acusação nunca procedeu, o que seria falso — o defeito existiu e foi corrigido.

**As 112 regras foram renomeadas pelo padrão de facetas em ordem de anamnese**, e
o `P1_NOME_REPETIDO` foi a zero — os 41 grupos se dissolveram.

**A questão 1 foi respondida, com uma correção de rumo.** O achado propunha
`<Benefício> — <critérios discriminantes> — <fundamento>`. O padrão adotado
mantém os dois primeiros e **descarta o fundamento**: a citação legal gastava a
maior parte dos caracteres e não ajuda a escolher, e a empresa confirmou que o
operador filtra o tipo do benefício **antes** de ver a lista de nomes, o que
torna termo repetido em toda a lista incapaz de recortar.

**A questão 4 foi decidida contra o que o achado propunha.** A coordenação
autorizou a auditoria a alterar `nome` diretamente na regra, em vez de propor a
correção como unidade auditada. Registro em Decisão 10 de
[`docs/analysis/decisoes-de-auditoria-2026-07-30.md`](../../../docs/analysis/decisoes-de-auditoria-2026-07-30.md).

**A questão 3 avisava do risco que se materializou, e a mitigação é
verificável.** O achado recomendava fundamentação primeiro, nome depois, porque
padronizar nome sozinho cala o `P1` e deixa o `P2` intacto — "o catálogo pareceria
mais saudável tendo mudado nada de material". A ordem inversa foi seguida. O que
impede a leitura enganosa não é promessa: `nome` está fora da chave material, os
sete grupos `P2_IGUALDADE_MATERIAL_ATIVA` seguem idênticos e asseverados por
teste, e as 33 regras cujo padrão colidiria carregam sufixo de id — que marca, no
próprio nome, onde os critérios de anamnese não distinguem as regras.

**A questão 2 migra e segue aberta.** Se a conformidade de nome deve virar gate
não foi decidido, e o argumento do achado permanece de pé: a parte difícil não é
a grafia, é "os critérios discriminantes estão no nome?", que exige saber quais
são — exatamente o que falta onde não há coluna, como o grau de deficiência e a
causa da incapacidade.

**O par de atos que o achado exigia para `0059`–`0064` continua devendo metade.**
Ele registrava que ajustar o nome torna a distinção legível e que diferenciar a
**fundamentação** é o que dissolve o grupo P2 honestamente — "são dois atos, e
nenhum substitui o outro". O nome foi feito; a fundamentação, não. Os grupos
`0059`≡`0063` e `0060`≡`0064` seguem ativos, e é onde a metade restante se paga.
