---
type: Achado
id: achado-0010
nome: Divergência entre Sexo Declarado e Texto da Fundamentação (Regra 0078)
situacao: aberto
severidade: informativo
verificacao: mecanica
natureza: dados
regras_afetadas:
  - /regras/regra-0078.md
detectado_em: '2026-07-18'
detectado_por: AI
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
