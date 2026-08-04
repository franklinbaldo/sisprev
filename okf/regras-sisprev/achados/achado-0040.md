---
type: Achado
id: achado-0040
nome: O art. 34 da LCE 1.100/2021 fixa os requisitos do policial "para ambos os sexos", e as quatro regras da regra permanente se desdobram por sexo
situacao: aberto
severidade: informativo
verificacao: manual
natureza: modelagem
regras_afetadas:
  - /regras/regra-0080.md
  - /regras/regra-0081.md
  - /regras/regra-0082.md
  - /regras/regra-0083.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

O art. 34 da LCE 1.100/2021 é o dispositivo que estabelece os requisitos da
aposentadoria voluntária do policial civil no regime permanente, e ele os fixa
**para ambos os sexos**, com essas palavras:

> Art. 34. O policial civil, o policial legislativo e o ocupante de cargo de
> policial penal ou de agente de segurança socioeducativo serão aposentados
> voluntariamente, desde que observados, cumulativamente, os seguintes
> requisitos, **para ambos os sexos**:
>
> I - 55 (cinquenta e cinco) anos de idade;
> II - 30 (trinta) anos de contribuição;
> III - 25 (vinte e cinco) anos de efetivo exercício em cargo de natureza
> estritamente policial; e
> IV - 5 (cinco) anos na carreira em que se dará a aposentadoria.

O catálogo tem **quatro** regras dessa modalidade, em dois pares, e a única
divergência material dentro de cada par é `sexo`:

| regra        | `sexo`    | `data_adm_ate` | `tipo_calculo`              | `paridade` |
| ------------ | --------- | -------------- | --------------------------- | ---------- |
| `regra-0080` | MASCULINO | 31/12/2099     | Valor Médio                 | N          |
| `regra-0081` | FEMININO  | 31/12/2099     | Valor Médio                 | N          |
| `regra-0082` | MASCULINO | 31/12/2003     | Remuneração de Contribuição | S          |
| `regra-0083` | FEMININO  | 31/12/2003     | Remuneração de Contribuição | S          |

Os pares se distinguem entre si pelo marco de ingresso, e isso tem dispositivo
— os arts. 24/25 e 27 da mesma lei. O que **não** tem dispositivo é a divisão
por sexo dentro de cada par.

# Evidências

## A fonte oficial, e o que ela também não traz

O art. 34 foi conferido no **texto compilado oficial** da LCE 1.100/2021
arquivado localmente (`fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt`,
extraído do PDF da Casa Civil registrado no `manifesto.yaml`). A conferência
não se apoiou apenas na transcrição do corpus.

E foi feita a busca que a afirmação negativa exige: **todas** as ocorrências de
"policial" no texto compilado inteiro. Fora do art. 34 e do seu parágrafo único,
elas são apenas o título da Seção V, a lista de benefícios do capítulo inicial e
o § 9º sobre pensão por morte de policial. **Nenhum outro dispositivo da lei
fixa requisito de aposentadoria de policial**, e nenhum distingue por sexo.

## O legislador distinguiu onde quis distinguir

O artigo **imediatamente seguinte**, na mesma lei, faz o oposto de forma
explícita:

> Art. 35. [...] I - 20 (vinte) anos de tempo de contribuição, **se mulher**, e
> 25 (vinte e cinco) anos, **se homem**, em caso de deficiência grave;

O art. 35 tem quatro incisos e todos distinguem por sexo. Em outras palavras: no
mesmo capítulo, a lei escreve "se mulher, e ... se homem" quando quer, e "para
ambos os sexos" quando não quer. A ausência de distinção no art. 34 não é
silêncio a interpretar — é opção declarada.

## Nenhum dos outros dispositivos vinculados distingue

As quatro regras vinculam cinco dispositivos cada, e a conferência item a item:

| dispositivo                   | o que estabelece                                                                                    | distingue por sexo?                           |
| ----------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| `cf88/art-40-par-4b`          | autoriza lei complementar do ente a fixar idade e tempo diferenciados para policial                 | não                                           |
| `cf88/art-40-par-1-inc-iii`   | 62/65 **no âmbito da União**; nos Estados, a idade mínima fixada por emenda à Constituição estadual | sim, mas só na parte da União, que não é esta |
| `lce-1100-2021/art-24`        | média das maiores remunerações, para ingresso após 31/12/2003                                       | não                                           |
| `lce-1100-2021/art-25`        | totalidade da remuneração, para ingresso até 31/12/2003                                             | não                                           |
| `lce-1100-2021/art-27` I e II | reajuste paritário ou pelo RGPS, conforme o mesmo marco de ingresso                                 | não                                           |
| `lce-1100-2021/art-34`        | os quatro requisitos, "para ambos os sexos"                                                         | **não, expressamente**                        |

A segunda linha é a única que traz idades por sexo, e é justamente a metade do
inciso que **não** se aplica ao Estado: para os Estados o inciso remete à emenda
à Constituição estadual, e a emenda (art. 7º, caput da ECE 146/2021) também diz
"55 (cinquenta e cinco) anos para ambos os sexos".

## O que os pares fazem hoje

Dentro de cada par, `sexo` é a **única** divergência material, e o `nome` é
idêntico caractere a caractere — daí os dois grupos `P1_NOME_REPETIDO`
(`sha256:b4ef7549…` para `0080`/`0081`, `sha256:f1110813…` para `0082`/`0083`).
As detecções são informativas e não são reivindicadas aqui: elas veem o nome
repetido, nunca que a lei não autoriza a divisão. Para isso é preciso ler o
art. 34, e por isso `verificacao: manual`.

Nenhum dos pares aparece em `P2_IGUALDADE_MATERIAL_ATIVA`, e a razão é
circular: `sexo` **é** material para o P2, então basta divergir nele para o
grupo não se formar. Um desdobramento que a lei não pede é exatamente o que o
detector de igualdade material não consegue ver.

# Relação com o que já está registrado

Esta é a terceira ocorrência da mesma forma no catálogo, e as duas anteriores já
estão registradas: o `achado-0019` (`regra-0030`/`0031` — "sexo é a única
divergência material [...] e nenhuma das seis provisões que elas citam distingue
por sexo") e o `achado-0034` (`regra-0057`/`0058` — a integralidade dependendo
do sexo sem dispositivo que a funde). São regras, normas e benefícios
diferentes; a repetição em três lotes independentes é o que torna a forma
estrutural.

Aqui a afirmação é mais forte do que nos dois: não é que o dispositivo *não
distinga*, é que ele **declara não distinguir**.

O `docs/analysis/achados-candidatos-da-conferencia.md` §4.4 registra este caso
como candidato marcado **[R]** — vindo do relatório do grupo, não reconferido.
Este achado o reconfere contra a fonte oficial e o promove.

# Consequência prática

Duas linhas onde a lei tem uma. O efeito imediato não é de elegibilidade: um
homem casa com a `0080`, uma mulher com a `0081`, e os requisitos que ambos
precisam cumprir são os mesmos quatro do art. 34, que não estão em coluna
nenhuma. Ninguém é excluído por causa disto.

O dano é de **seleção e de manutenção**. As duas regras do par exibem o mesmo
`nome` ao usuário, e a distinção que as separa não é discriminante para ele:
depois da anamnese, uma mulher tem uma candidata e um homem tem outra, ambas
rotuladas igual, sem nada que explique por que são duas. E toda correção futura
no par precisa ser feita duas vezes, com a chance de as duas linhas divergirem
em algo que a lei quer igual — que é precisamente o que o `achado-0016` e o
`achado-0037` documentam já tendo acontecido nas regras de policial e de
professor.

`SEXO` é campo **deployável** e a cardinalidade do catálogo é decisão
operacional, não jurídica: a spec registra que "a granularidade da aferição é
escolha do IPERON" e que o número de regras **não é determinado pela lei**
([`okf/spec/regra.md`](../../../okf/spec/regra.md)). Nada aqui afirma que os
pares estejam proibidos de existir — afirma que a lei citada não os pede.

# Questão a investigar

1. **Se os pares devem virar uma regra `sexo: AMBOS` cada.** `AMBOS` é valor que
   o domínio já tem (`regra-0006`, `regra-0084` o usam), então a consolidação é
   parametrização e não alteração do Sisprev. Mas ela muda a **cardinalidade** do
   catálogo, e é por isso que não é edição de regra: consolidação N:1 é unidade
   auditada mais grupo de substituição
   ([RFC 0004](../../../docs/rfc/0004-schema-enriquecido-e-compilador-para-o-sisprev.md),
   [RFC 0006](../../../docs/rfc/0006-conjuntos-de-regras.md)), e nenhuma é
   proposta aqui.

2. **Se o desdobramento tem razão fora do art. 34.** Duas hipóteses concretas, e
   nenhuma conferida: um provimento judicial que reduza requisito para a policial
   mulher, ou um comportamento do próprio Sisprev que exija uma linha por sexo em
   toda modalidade. A segunda é conferível perguntando ao IPERON; a primeira, não
   pelo catálogo. Enquanto nenhuma delas for respondida, o desdobramento existe
   sem fundamento **declarado**, que é o que este achado afirma — não que seja
   arbitrário.

3. **Se a mesma pergunta alcança o par transitório.** `regra-0072`/`0073`, do
   art. 7º da ECE 146/2021, também se dividem por sexo — mas ali a divisão **tem**
   dispositivo (§ 2º: 52 anos se mulher, 53 se homem; e as duas alíneas da LC
   51/1985, 30/20 × 25/15). O contraste é útil: as mesmas quatro colunas
   sustentam um desdobramento fundado e um não fundado, no mesmo grupo de
   regras, e nada no catálogo distingue os dois casos.
