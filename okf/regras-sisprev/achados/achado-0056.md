---
type: Achado
id: achado-0056
nome: Duas regras de pensão por morte desdobram por sexo sem que nenhum dispositivo citado por elas diferencie por sexo
situacao: aberto
severidade: bloqueante
verificacao: manual
natureza: juridica
regras_afetadas:
  - /regras/regra-0016.md
  - /regras/regra-0017.md
detectado_em: 2026-07-30
detectado_por: franklinbaldo
---

# Descrição

`regra-0016`, `regra-0017` e `regra-0018` citam **o mesmo conjunto de
dispositivos, item por item** — os onze abaixo — e divergem entre si apenas no
campo `sexo`:

| regra        | `sexo`    |
| ------------ | --------- |
| `regra-0016` | MASCULINO |
| `regra-0017` | FEMININO  |
| `regra-0018` | AMBOS     |

Nenhum dos dispositivos que elas invocam diferencia por sexo. O desdobramento
grava, em campo deployável, um critério de aferição que a articulação normativa
declarada pela própria regra não sustenta.

Este achado alcança `regra-0016` e `regra-0017`, que são as que afirmam o
critério. A `regra-0018` é nomeada aqui como termo de comparação e não responde
por este defeito: ela grava `AMBOS`, que é o que os dispositivos dizem.

# Evidências

**Os `dispositivos:` das três são idênticos:**

```
cf88/art-40-par-7/ec-103-2019
lce-1100-2021/art-27-inc-i        lce-1100-2021/art-49
lce-1100-2021/art-46-inc-i        lce-1100-2021/art-50
lce-1100-2021/art-47-inc-i        lce-1100-2021/art-51-inc-i
lce-1100-2021/art-47-inc-ii       lce-1100-2021/art-51-inc-ii
                                  lce-1100-2021/art-51-inc-iii
                                  lce-1100-2021/art-51-inc-viii-al-c
```

**Nos onze textos transcritos, o sexo aparece uma vez — e para ser afastado.**
No art. 51, II da LCE 1.100/2021:

> II - para filho ou pessoa a ele equiparada ou para o irmão dependente, **de
> ambos os sexos**, ao completar 21 (vinte e um) anos de idade, salvo se for
> inválido ou tiver deficiência intelectual ou mental ou deficiência grave
> atestada por perícia médica oficial indicada pelo IPERON ou por sentença
> judicial;

A cláusula **equaliza**: diz expressamente que o sexo não altera o tratamento. A
mesma construção está no art. 32, II, "a" da LCE 432/2008, citado por outras
regras de pensão do catálogo:

> a) o filho ou a pessoa a ele equiparada, **de ambos os sexos**, enquanto não
> completar 21 (vinte e um) anos [...]

**As duas passagens tratam do dependente, não do instituidor.** Portanto nem o
eixo do beneficiário nem o do servidor falecido recebem tratamento diferenciado
nos dispositivos citados — no único ponto em que a norma olha para o sexo, é para
dizer que é indiferente.

**Contraste com o desdobramento legítimo.** As regras de policial também se
desdobram por sexo, e ali o desdobramento tem lastro: a LC 51/1985, art. 1º, II
tem alínea "a" para homem (30/20 anos) e "b" para mulher (25/15). Critério
aferido distinto torna duas regras não idênticas, como a
[`okf/spec/regra.md`](../../../okf/spec/regra.md) registra. A diferença entre os
dois casos é exatamente a presença da provisão que diferencia.

# Consequência prática

**O desdobramento pode bifurcar o procedimento da Administração sem
fundamento.** Duas regras distintas para o que a norma trata como um caso só
produzem dois caminhos de instrução, dois enquadramentos possíveis para o mesmo
requerente e dois textos de fundamentação — sem que exista provisão que
justifique a bifurcação. O risco não é de cálculo errado; é de o ato
administrativo tratar como juridicamente relevante uma distinção que o direito
declarou indiferente.

**Severidade `bloqueante`** por isso: o defeito está em campo deployável e
alcança a condução do procedimento, não apenas a apresentação.

**Efeito colateral sobre o P2.** `sexo` integra a chave material do
`P2_IGUALDADE_MATERIAL_ATIVA`. É por isso que estas três regras não formam grupo:
o campo que as separa é justamente o que o detector considera material. Se o
desdobramento não tem base, o P2 está sendo dissolvido por uma distinção
inexistente no direito — e o detector não tem como perceber, porque ele compara
valores e não os confronta com dispositivo. É a forma inversa da situação
descrita no `CLAUDE.md`: ali, um grupo P2 pode ser regras legitimamente distintas
cuja distinção o catálogo não expressa; aqui, a ausência de grupo esconde regras
que talvez devessem ser uma só.

# O que este achado não afirma

**Não afirma que a legislação de pensão por morte não diferencie por sexo em
lugar nenhum.** O que foi conferido é que **nenhum dispositivo citado por estas
regras** diferencia. A fundamentação é articulação autorada, e provisão
pertinente pode existir sem estar declarada — o que seria, ele próprio, outro
defeito, de citação incompleta em vez de parametrização excessiva.

**Não afirma que o desdobramento tenha pretendido afirmar diferença jurídica.** A
granularidade da aferição é conveniência do IPERON, e as três regras podem ter
sido separadas por razão operacional que ninguém registrou. Isso não torna o
achado falso — o campo deployável afirma o critério de qualquer modo —, mas muda
o que a disposição deve fazer: registrar a razão operacional é resposta legítima,
enquanto silêncio não é.

**Não propunha a correção** quando foi escrito. A coordenação decidiu, e a
decisão está em "Correção decidida".

# Correção decidida

**`regra-0016` e `regra-0017` são revogadas**, e a `regra-0018` permanece. O
delta está declarado em `revoga:` no conjunto
`okf/conjuntos/proposta-auditoria-2026-07.md`, que o justifica por extenso.

A alternativa considerada era gravar `AMBOS` nas duas, alinhando-as ao que a
norma diz. Foi descartada por razão estrutural: alterar critério de regra legada
muda a **chave material** do P2, e as três passariam a formar grupo de igualdade
material — o estado conhecido do catálogo mudaria por efeito colateral de uma
edição cujo propósito era outro. A regra legada registra o que foi operado;
corrigi-la no lugar substitui esse fato pelo que deveria ter sido.

A revogação preserva as duas afirmações ao mesmo tempo: que estas regras foram
operadas, e que a auditoria propõe que deixem de existir. E mantém o frontmatter
intocado, o que deixa a chave material do P2 igual **por construção**.

**Este achado permanece `aberto`.** O conjunto é `proposto`: as duas regras
seguem no catálogo operado e seguem exportadas ao CSV derivado. Ele só se resolve
quando a revogação alcançar o catálogo vigente, o que exige `decisao_completude`
no nível do conjunto e ato de ativação — nenhum dos dois é ato da auditoria
sozinha.

# Questão a investigar

1. **Se existe provisão pertinente não citada que diferencie por sexo.** É a
   pergunta que decide se o defeito é parametrização excessiva ou citação
   incompleta. Só se responde lendo a norma além do que a regra declara.

2. **A quem o campo `sexo` se refere numa regra de pensão** — ao servidor
   instituidor ou ao dependente pensionista. O catálogo não registra, e a
   pergunta é anterior a qualquer correção: os dois eixos têm requisitos
   diferentes, e não se sabe qual deles o campo grava. Alcança todas as regras de
   pensão, não só estas.

3. **Se houve razão operacional para o desdobramento.** Pergunta ao IPERON como
   titular do produto. Resposta afirmativa não dissolve o achado, mas dá à
   disposição um conteúdo que hoje não existe.
