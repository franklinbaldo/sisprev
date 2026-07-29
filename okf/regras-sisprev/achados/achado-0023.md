---
type: Achado
id: achado-0023
nome: O nome de regra-0032 a funda na EC 103/2019 e na LC 1.100/2021, e a fundamentação na EC 88/2015 e na LC 152/2015
situacao: aberto
severidade: informativo
verificacao: manual
natureza: juridica
regras_afetadas:
  - /regras/regra-0032.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

O `nome` e a `fundamentacao_proporcional` de `regra-0032` apontam para regimes
jurídicos diferentes.

O nome: "Compulsória - Art. 40, §1º, II da CF com redaçao da **EC 103/19** c/c
art. 31 da **Lc nº 1.100/2021**".

A fundamentação: "artigo 40, § 1º, inciso II, da Constituição Federal, com
redação dada pela **Emenda Constitucional nº 88/2015**; em conformidade com a
**Lei Complementar nº 152/2015**, combinado com os artigos 17, 21, § 1º, 45 e
62 da Lei Complementar Estadual nº 432/2008, e com o artigo 4º da Emenda
Constitucional Estadual nº 146/2021."

# Evidências

As duas redações do art. 40, § 1º, II da CF existem e são distintas: a da EC
88/2015 elevou para 75 anos a compulsória, regulamentada pela LC 152/2015; a da
EC 103/2019 reescreveu o inciso no contexto da reforma federal, e a LC estadual
1.100/2021 é a lei do regime reformado em Rondônia.

Não é divergência de forma: as duas leituras levam a consequências opostas na
conferência da janela temporal.

- Se vale a **fundamentação** (EC 88/2015 + LC 152/2015), a regra é de
  legislação anterior à ECE 146/2021, o art. 4º dessa emenda a alcança, e
  `data_direito_ate` deveria fechar em 31/12/2024 — é o que
  [`achado-0022`](achado-0022.md) sustenta.
- Se vale o **nome** (EC 103/2019 + LC 1.100/2021), a regra é de regime novo,
  posterior à EC 146, e então o art. 4º **não deveria estar citado** — o
  problema deixa de ser a janela e passa a ser a citação.

O `data_direito_apos: 18/10/2021` não desempata: é a entrada em vigor da ECE
146/2021, compatível com as duas leituras.

## A redação atribuída não vigia em nenhum dia da janela, e a cadeia é o que difere

Conferência independente (2026-07-29), somada aqui em vez de virar achado
próprio: é o mesmo campo e o mesmo defeito, e dois achados sobre uma citação
seriam duplicação.

A `fundamentacao_proporcional` atribui o art. 40, § 1º, II à **EC 88/2015**.
Aquela redação vigeu de 08/05/2015 a **12/11/2019**; a janela de direito da regra
é `[18/10/2021, 31/12/2099)`. **Não há um dia de sobreposição** — a redação
invocada estava extinta havia quase dois anos quando a janela abre.

| redação       | vigência                    |
| ------------- | --------------------------- |
| `ec-20-1998`  | 16/12/1998 – 30/12/2003     |
| `ec-41-2003`  | 31/12/2003 – 07/05/2015     |
| `ec-88-2015`  | 08/05/2015 – **12/11/2019** |
| `ec-103-2019` | **13/11/2019** – (em vigor) |

E aqui está o motivo de nenhum gate acusar: **o texto do inciso II é literalmente
idêntico nas duas redações**, palavra por palavra —

> II - compulsoriamente, com proventos proporcionais ao tempo de contribuição,
> aos 70 (setenta) anos de idade, ou aos 75 (setenta e cinco) anos de idade, na
> forma de lei complementar;

Então o critério aferido é o mesmo sob as duas, e **nenhum beneficiário recebe
coisa diferente por causa da atribuição errada**. O vínculo resolve, o caminho
confere, o texto é verbatim, e o `check_vigencias` não tem o que reclamar — ele
só compara datas dentro de um diretório.

O que muda é a **cadeia**, e um dispositivo é a unidade endereçada com toda a
cadeia que a contém (`docs/spec/dispositivo.md`):

| nível | redação da EC 88/2015                                                                                          | redação da EC 103/2019                                                           |
| ----- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| § 1º  | "...serão aposentados, **calculados os seus proventos a partir dos valores fixados na forma dos §§ 3º e 17**:" | "O servidor abrangido por regime próprio de previdência social será aposentado:" |

A diferença é substantiva: a redação de 2015 remete o cálculo dos proventos aos
§§ 3º e 17 do art. 40; a de 2019 não remete a nada — o cálculo passou a ser o da
nova previdência. E a regra grava `tipo_calculo: Tipo Cálculo Nova Previdência`.

Ou seja, a fundamentação invoca uma cadeia cujo § 1º manda calcular por um
caminho que a própria regra não aplica. Isso **reforça o lado do `nome`** na
divergência acima: os campos de resultado da regra são os do regime novo.

Consequência de método, contraintuitiva: o vínculo a
`cf88/art-40-par-1-inc-ii/ec-88-2015` **não** deve ser trocado antes da
fundamentação. Um vínculo afirma que a fundamentação cita aquela provisão, e ela
cita — corrigir o vínculo primeiro romperia a fidelidade e esconderia o defeito
no campo que é entregue.

O `nome` cita ainda o **art. 31 da LCE 1.100/2021**, transcrito no bundle e que
diz exatamente o que a regra grava ("aposentado, compulsoriamente, aos 75 anos de
idade, com proventos proporcionais ao tempo de contribuição"), com vigência a
partir de 18/10/2021 — a mesma data de `data_direito_apos`. Nenhum campo de
fundamentação o cita, e por isso nenhum vínculo é proposto.

# Questão a investigar

Qual das duas é a regra que o Sisprev de fato aplica hoje na compulsória?

A resposta é do dono do campo, não do auditor, e ela decide qual dos dois
textos se corrige. Corrigir o errado — alinhar a fundamentação a um nome que
esteja equivocado, ou o inverso — produziria um documento coerente e falso, que
é pior que a divergência visível.

Nota de escopo: tanto o `nome` quanto a `fundamentacao*` são colunas de texto
livre, logo corrigi-las é parametrização e está dentro do escopo da auditoria.
O que está fora é decidir por conta própria qual delas descreve a prática.
