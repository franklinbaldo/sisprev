---
type: Achado
id: achado-0012
nome: Fundamentação de regra-0012 e regra-0013 atribui à LCE 949/2017 a redação de cinco dispositivos que ela nunca alterou
situacao: aberto
severidade: informativo
verificacao: hibrida
natureza: juridica
deteccoes:
  - detector: P4_REDACAO_INEXISTENTE
    fingerprint: sha256:499512975a1cef22fac031e8f4744ec091906e4b03ad11a188793b83ebda99bf
  - detector: P4_REDACAO_INEXISTENTE
    fingerprint: sha256:9958fc6ad44cd381ae7c7d136d49ab3dcae8039c3af6dbb82ec22276edad3655
regras_afetadas:
  - /regras/regra-0012.md
  - /regras/regra-0013.md
detectado_em: 2026-07-27
detectado_por: franklinbaldo
---

# Descrição

A `FUNDAMENTACAO_INTEGRAL` de `regra-0012` e `regra-0013` cita, ipsis
litteris:

> Pensão mensal, com fundamento nos artigos 10, I; 28, I; 30, II; 31, §§ 1º e
> 2º; 32, I e II, "a", e § 1º; 33; 34, I a III, e § 2º; 38; e 62 da Lei
> Complementar Estadual nº 432/2008, **com redação dada pela Lei Complementar
> Estadual nº 949/2017** [...]

A oração "com redação dada por" vem **uma única vez, ao fim de uma lista de
nove itens**, e por construção da frase alcança todos eles. Conferido item a
item contra o texto compilado da própria LCE 432/2008, isso é falso para
cinco dos nove.

# Evidências

Fonte: o PDF compilado oficial da LCE 432/2008 (Casa Civil/RO), o mesmo já
usado como `fontes` dos dispositivos desta norma —
<https://ditel.casacivil.ro.gov.br/COTEL/Livros/Files/LC432%20COMPILADA%20REVOGADA.pdf>.
Um documento compilado marca cada redação com a norma que a deu, então a
conferência é leitura direta:

| citado na regra     | redação dada pela LCE 949/2017?                                |
| ------------------- | -------------------------------------------------------------- |
| art. 10, I          | **sim**                                                        |
| art. 28, I          | **não** — o inciso I é a redação original                      |
| art. 30, II         | **não** — o art. 30 nunca foi alterado                         |
| art. 31, §§ 1º e 2º | **não** — redação dada pela **LC 504, de 29/04/2009**          |
| art. 32, I e II "a" | **sim** (alínea "c" do inciso I; alínea "a" do inciso II)      |
| art. 32, § 1º       | **sim**                                                        |
| art. 33             | **sim** (caput)                                                |
| art. 34, I a III    | **sim**                                                        |
| art. 34, § 2º       | **sim**                                                        |
| art. 38             | **não** — nunca alterado                                       |
| art. 62             | **não** — só o parágrafo único, pela **LC 458, de 17/06/2008** |

O art. 62 é o caso mais nítido: o único ponto do artigo que já teve redação
substituída é o seu parágrafo único, e quem a deu foi a LC 458/2008, cinco
anos antes de existir a LC 949/2017. O caput — que é o que a regra invoca,
já que cita "62" sem recorte — está na redação original desde 2008.

# Consequência prática

O leitor de citações (`scripts/citacoes.py`) aplica a regra que a prosa
manda: norma nomeada após "com redação dada por" é a redação de tudo que a
antecede na oração. Ele portanto pede, para estas duas regras, a redação
`lce-949-2017` dos cinco dispositivos, que não existe e não pode ser
transcrita.

Para o **art. 62** isso deixou de ser afirmação de auditor e passou a ser
verificação de máquina, com as duas detecções acima
(`P4_REDACAO_INEXISTENTE`, camada 2, refeitas a cada commit): a única
redação autorada do artigo cobre de 13/03/2008 a 18/10/2021, que é a vida
inteira da LCE 432/2008 — logo não sobra espaço para outra, e a redação
citada é provadamente inexistente, não pendente. Os outros quatro
dispositivos ainda não foram transcritos, então a mesma prova não pode
ser feita para eles: aparecem como transcrição pendente até que sejam, e
só então a detecção os alcança.

Enquanto o campo não for decidido, esses cinco vínculos ficam pendentes nas
duas regras — que é o comportamento correto, e a razão de o leitor recusar
em vez de "consertar" a atribuição sozinho.

Vale distinguir do `achado-0011`: lá a omissão é da norma **dona**; aqui a
norma dona está correta (LCE 432/2008) e o que é falso é a **redação**
atribuída. O modo de falha é o mesmo — uma citação jurídica errada com
aparência plausível — mas o dado errado é outro.

# Questão a investigar

Como este achado se resolve depende de o que a frase quis dizer, e isso é do
dono do campo, não do auditor:

1. **Generalização de redação** — o autor sabia que só parte da lista fora
   alterada pela LCE 949/2017 e escreveu a oração como rótulo do conjunto.
   Nesse caso a prosa deveria ser recortada (a oração passa a valer só para
   os itens que ela de fato alcança), e os cinco restantes se vinculam à
   redação original.
2. **Erro de redação** — a lista foi montada a partir de uma fundamentação
   anterior e a oração final veio junto sem reconferência. Correção na
   origem.
3. **Leitura diferente da nossa** — "com redação dada pela LCE 949/2017"
   qualifica a *Lei Complementar Estadual nº 432/2008* como um todo (isto é,
   "a LCE 432/2008 na sua redação vigente após a LCE 949/2017"), e não cada
   dispositivo da lista. É gramaticalmente possível pela posição da oração,
   logo depois do nome da lei. Se for essa a intenção, nenhum item está
   errado e o que precisa mudar é a regra de leitura do
   `scripts/citacoes.py` — hipótese que, se confirmada, provavelmente
   também afeta outras regras do catálogo.

`FUNDAMENTACAO*` é campo **deployável** do Sisprev — é o texto entregue no
documento do servidor. Corrigi-lo é alteração do produto, não ato de
auditoria sobre o catálogo. Enquanto não decidido, nada é inferido: o
registro diz o que o campo diz.
