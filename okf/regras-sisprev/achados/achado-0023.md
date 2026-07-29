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

# Questão a investigar

Qual das duas é a regra que o Sisprev de fato aplica hoje na compulsória?

A resposta é do dono do campo, não do auditor, e ela decide qual dos dois
textos se corrige. Corrigir o errado — alinhar a fundamentação a um nome que
esteja equivocado, ou o inverso — produziria um documento coerente e falso, que
é pior que a divergência visível.

Nota de escopo: tanto o `nome` quanto a `fundamentacao*` são colunas de texto
livre, logo corrigi-las é parametrização e está dentro do escopo da auditoria.
O que está fora é decidir por conta própria qual delas descreve a prática.
