---
type: Achado
id: achado-0021
nome: regra-0061 e regra-0062 citam um parágrafo único do art. 39 da LCE 432/2008 que não existe, e é ele que as mantém fora do grupo P2
situacao: aberto
severidade: informativo
verificacao: manual
natureza: juridica
regras_afetadas:
  - /regras/regra-0061.md
  - /regras/regra-0062.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

O campo `fundamentacao` de `regra-0061` e `regra-0062` contém, na íntegra:

> Art. 39, paragrafo unico da Lei Complementar 432/2008

**Esse parágrafo não existe.** O art. 39 da LCE 432/2008 tem **nove parágrafos
numerados** — §§ 1º a 9º — e nenhuma ocorrência de "parágrafo único" em todo o
seu bloco. Por técnica legislativa não poderia ter: parágrafo único existe
apenas quando o artigo tem um parágrafo só.

# Evidências

Conferido na compilação oficial arquivada localmente
(`fontes-oficiais/arquivos/ditel-LC432-COMPILADA-REVOGADA.txt`): o bloco do art.
39 contém os parágrafos numerados de **1º a 9º**, e a expressão "parágrafo
único" aparece **zero vezes** nele.

## A hipótese histórica foi testada, e não se sustenta

A objeção óbvia — e correta — é que o texto lido é a **compilação**: se uma lei
posterior tivesse convertido um parágrafo único em § 1º e acrescentado os
demais, a citação estaria certa para a redação **original** de 2008, e a janela
das regras poderia cair naquele período.

O art. 39 **foi** alterado, o que dava base à hipótese. As notas da compilação
mostram exatamente onde:

| dispositivo        | nota                                                         |
| ------------------ | ------------------------------------------------------------ |
| § 3º               | "(Redação dada pela Lei Complementar n. 504, de 29/04/2009)" |
| § 9º               | "(Incluído pela Lei Complementar n. 504, de 29/04/2009)"     |
| §§ 1º, 2º, 4º a 8º | **nenhuma nota**                                             |

A LC 504/2009 deu nova redação a **um** parágrafo e **acrescentou um**. Não
reestruturou nada. E como a compilação anota o que mudou, a ausência de nota nos
§§ 1º, 2º e 4º a 8º os identifica como **redação original de 2008**.

Um parágrafo único não coexiste com § 1º e § 2º — por definição, é o parágrafo
de artigo que tem só um. Logo o art. 39 **nunca** teve parágrafo único, em
nenhuma das suas redações.

Limite desta conferência, declarado: ela se apoia na prática de anotação da
compilação da DITEL, não na publicação original da LCE 432/2008, que não está
arquivada (o corpus tem a compilada e a página SAPL da norma). Se a publicação
original for obtida e contradizer isto, é ela que vale.

## Isto corrige a classificação anterior

O §1.3 da
[lista consolidada](../../../docs/analysis/achados-candidatos-da-conferencia.md)
registra o item como `[V parcial]`, dizendo que "o objeto literal da citação é o
parágrafo único, que **não está transcrito** no corpus". A ressalva era honesta
para o que se sabia então — o corpus só tinha o caput do art. 39 —, mas a
conclusão que ela deixava aberta ("transcrevê-lo fecha a questão em qualquer
direção") pressupunha que houvesse o que transcrever.

**Não há.** Não é lacuna de transcrição; é citação de provisão inexistente —
mesma classe do `achado-0012`, `achado-0013` e do modo de falha nomeado no §5.3
daquela lista.

# Consequência prática

O dano é duplo, e a segunda metade é a que interessa mais.

**Primeiro**, `FUNDAMENTACAO`/`fundamentacao` é campo **deployável**: as duas
regras entregam ao servidor um documento que invoca dispositivo que não existe,
num artigo de outro benefício.

**Segundo, e é o ponto**: essa citação é **a única coisa** que mantém
`regra-0061` e `regra-0062` fora de um grupo `P2_IGUALDADE_MATERIAL_ATIVA`.

As seis regras de servidor com deficiência (`0059`–`0064`) são 3 graus × 2
sexos. O detector reporta hoje dois grupos:

- `regra-0059` ≡ `regra-0063` (feminino: moderada ≡ leve)
- `regra-0060` ≡ `regra-0064` (masculino: moderada ≡ leve)

`0061`/`0062` (grave) **não** aparecem, e o motivo é mecânico: o campo
`fundamentacao` delas está preenchido com esta citação, e das outras quatro está
vazio. `FUNDAMENTACAO*` está **dentro** da chave material do P2. Corrigir a
citação — em qualquer direção, inclusive apagando-a — faz as duas entrarem nos
grupos, que passam a ter três regras cada.

Não se segue que sejam duplicatas. O que separa as seis é o **grau de
deficiência**, e ele está na lei com números distintos (art. 35, I a III da LCE
1.100/2021: 20/25, 24/29 e 28/33 anos de contribuição) e **em nenhuma coluna do
catálogo** — está só no `nome`, que o P2 não considera. É o caso que o
`CLAUDE.md` descreve: grupo P2 que é **lacuna de schema, não duplicação**.

Ou seja: **uma citação falsa está hoje escondendo uma lacuna real**, e
consertá-la torna o problema visível em vez de criá-lo.

# Questão a investigar

1. **Qual dispositivo a citação pretendia nomear.** Três hipóteses, nenhuma
   verificada: um parágrafo numerado do art. 39 (mas todos são de
   auxílio-reclusão); o parágrafo único de **outro** artigo, com o número
   errado; ou preenchimento indevido, herdado de outra regra. A terceira é a
   mais simples — o campo está vazio nas outras quatro do mesmo grupo de seis —
   e continua hipótese.

2. **Se apagar o campo é a correção.** Apagar alinha `0061`/`0062` às quatro
   irmãs e é o que a leitura de "preenchimento indevido" recomenda. Mas
   `fundamentacao` é deployável, e apagar campo entregue é alteração de produto:
   decisão de quem responde por ele, não da auditoria. Registrado que a
   consequência é entrar nos grupos P2 — o que é o resultado **correto**, não um
   efeito colateral a evitar.

3. **A ordem em relação ao grau.** Se a citação for corrigida antes de o grau
   entrar nas fundamentações, os grupos P2 passam de dois para dois de três
   regras, e o catálogo parecerá ter piorado. Terá apenas parado de esconder. A
   sequência que não produz leitura enganosa é **grau primeiro, citação depois**
   — o inverso da urgência aparente.
