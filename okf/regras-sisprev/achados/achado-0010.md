---
type: Achado
id: achado-0010
nome: Divergência entre Sexo Declarado e Texto da Fundamentação (Regra 0078)
situacao: resolvido
severidade: informativo
verificacao: mecanica
natureza: dados
regras_afetadas:
  - /regras/regra-0078.md
detectado_em: '2026-07-18'
detectado_por: AI
resolvido_em: 2026-07-30
resolvido_por: franklinbaldo
efeito_deteccao: deve_desaparecer
deteccoes:
  - detector: P9_SEXO_FUNDAMENTACAO
    fingerprint: sha256:592557e6c4069cec7556293f351a00614109724506a9e86694dd373f482541c4
---

# Descrição

A `regra-0078` ("Voluntária do Policial Civil - Art. 7º, § 3º da EC nº 146/2021") declara no campo `sexo` o valor "MASCULINO". No entanto, o texto do campo `fundamentacao_integral` menciona explicitamente "idade + tempo de contribuição + mulher". (Note que existe a `regra-0079` pareada para o sexo feminino).

# Evidências

Detecção `P9_SEXO_FUNDAMENTACAO`: o campo `sexo` é "MASCULINO", mas há correspondência da palavra "mulher" na fundamentação e não há correspondência da palavra "homem".

# Questão a investigar

Verificar, **contra a fonte real do Sisprev** (não por inferência), se a
menção a "mulher" na fundamentação da `regra-0078` (sexo MASCULINO) é um
erro de "copiar e colar" a partir da regra feminina pareada (`regra-0079`),
ou se reflete o texto efetivamente cadastrado na origem. Só após essa
confirmação humana a fundamentação poderá — ou não — ser corrigida. Até lá
o dado importado é preservado como está (baseline da auditoria); este
achado permanece **aberto**.

# Resolução

# Resolução

`fundamentacao_integral` da `regra-0078` passou a citar a alínea **"a"** do art.
1º, II da LC 51/1985 — a masculina, 30 anos de contribuição e 20 de exercício
policial — e o descritor "homem", em lugar da alínea "b" e do descritor
"mulher". O campo deixou de contradizer o `sexo: MASCULINO` que a regra declara,
e a detecção `P9_SEXO_FUNDAMENTACAO` deixou de ser emitida.

`efeito_deteccao: deve_desaparecer`, porque a correção remove a causa: o
detector procura "mulher" sem "homem" num campo cujo `sexo` é MASCULINO, e
nenhuma das duas condições subsiste.

**O texto não foi redigido aqui.** Ele estava escrito e conferido desde
2026-07-30 na unidade auditada `policial-civil-voluntaria-masculino`, que existia
para propor exatamente esta correção sem tocar na regra de origem. O que mudou
não foi o texto e sim a competência: a Decisão 10 de
[`docs/analysis/decisoes-de-auditoria-2026-07-30.md`](../../../docs/analysis/decisoes-de-auditoria-2026-07-30.md)
autorizou a auditoria a alterar `FUNDAMENTACAO*` diretamente, e o caminho pelo
catálogo auditado deixou de ser necessário para este caso.

**O `achado-0017` segue aberto**, e a diferença de população é a razão: ele
descreve o mesmo defeito de citação alcançando também a `regra-0079`, pela
citação truncada, e a `regra-0084`, cujo provimento judicial não foi localizado.
Esta correção não alcança nenhuma das duas.
