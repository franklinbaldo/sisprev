---
type: Achado
id: achado-0013
nome: Fundamentação de regra-0028 e regra-0029 atribui à EC 41/2003 a redação do art. 40, § 1º, II, da CF, que ela nunca deu
situacao: aberto
severidade: informativo
verificacao: manual
natureza: juridica
regras_afetadas:
  - /regras/regra-0028.md
  - /regras/regra-0029.md
detectado_em: 2026-07-28
detectado_por: franklinbaldo
---

# Descrição

A `FUNDAMENTACAO_PROPORCIONAL` de `regra-0028` e `regra-0029` cita, ipsis
litteris:

> Artigo 40, § 1º, inciso II da Constituição Federal, **com redação dada pela
> Emenda Constitucional nº 41/2003**, artigos 17, 45 e 62 da Lei Complementar
> Estadual nº 432/2008 e art. 1º Lei nº 10.887/2004

O inciso II do § 1º do art. 40 teve exatamente duas redações emendadas em
toda a sua história, e nenhuma delas é da EC 41/2003.

# Evidências

Duas fontes independentes, ambas oficiais, dizem o mesmo:

1. **O texto compilado da Constituição** (Planalto) lista, para o inciso II,
   só duas redações:

   > II - compulsoriamente, aos setenta anos de idade, com proventos
   > proporcionais ao tempo de contribuição; (Redação dada pela Emenda
   > Constitucional nº 20, de 1998)

   > II - compulsoriamente, com proventos proporcionais ao tempo de
   > contribuição, aos 70 (setenta) anos de idade, ou aos 75 (setenta e cinco)
   > anos de idade, na forma de lei complementar; (Redação dada pela Emenda
   > Constitucional nº 88, de 2015)

2. **O texto da própria EC 41/2003** mostra por que: ao reescrever o art. 40,
   ela dá nova redação ao *caput* do § 1º e ao seu **inciso I**, e em seguida
   abre a linha pontilhada que, na convenção do Planalto, significa "o resto
   segue como está". O inciso II não é reencenado.

Logo, a redação em vigor do inciso II durante toda a vigência da EC 41/2003
(2003–2015) era a da **EC 20/1998**, e depois passou a ser a da **EC
88/2015** — que é, aliás, a que `regra-0027` e `regra-0032` citam
corretamente para o mesmo inciso, e já está autorada e vinculada.

Fontes:
<https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm> e
<https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc41.htm>.

# Consequência prática

Estas duas regras pedem `cf88/art-40-par-1-inc-ii/ec-41-2003`, redação que
não existe, e por isso aparecem hoje na fila `redacao_ausente` do
`relatorio_citacoes.py`. Como no `achado-0012`, **não é tarefa de
transcrição**: não há o que transcrever.

A redação da EC 20/1998 desse inciso também não foi autorada — nenhuma regra
do catálogo a cita, e autorá-la só para "resolver" este vínculo seria
escolher pela regra qual norma ela invoca, que é justamente o que o leitor
recusa fazer.

# Questão a investigar

É o mesmo par de hipóteses do `achado-0012`, com um detalhe a mais que
merece ser conferido junto:

1. **Erro de atribuição** — a regra quis dizer EC 20/1998 (a redação em vigor
   à época do fundamento) e escreveu EC 41/2003 por ser a emenda que dominava
   a matéria no período. Correção na origem, e o vínculo passa a ser possível.
2. **Deslize por arraste** — a EC 41/2003 *de fato* reescreveu o § 1º
   (*caput*) e o inciso I; quem redigiu pode ter estendido a atribuição ao
   inciso II sem conferir. Distinguir isso do item 1 importa, porque muda o
   que se corrige: a emenda citada ou o dispositivo citado.
3. **Leitura diferente da nossa** — "com redação dada pela EC 41/2003"
   qualificaria o **§ 1º** (que ela reescreveu), e não o inciso II lido dentro
   dele. É a mesma hipótese 3 do `achado-0012` e, se for essa a intenção, o
   que muda não é a prosa e sim a regra de leitura do `scripts/citacoes.py`.

Vale decidir os dois achados na mesma conversa: são o mesmo modo de falha —
redação atribuída a uma norma que não a deu — em normas diferentes, e a
hipótese 3 é literalmente a mesma pergunta.

`FUNDAMENTACAO*` é campo **deployável** do Sisprev. Enquanto não decidido,
nada é inferido: o registro diz o que o campo diz.
