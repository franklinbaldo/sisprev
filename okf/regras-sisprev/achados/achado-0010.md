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
resolvido_em: 2026-07-18
resolvido_por: AI
efeito_deteccao: deve_desaparecer
deteccoes:
- detector: P9_SEXO_FUNDAMENTACAO
  fingerprint: sha256:592557e6c4069cec7556293f351a00614109724506a9e86694dd373f482541c4
---

# Descrição

A `regra-0078` ("Voluntária do Policial Civil - Art. 7º, § 3º da EC nº 146/2021") declara no campo `sexo` o valor "MASCULINO". No entanto, o texto da `# Fundamentação Integral` menciona explicitamente "idade + tempo de contribuição + mulher". (Note que existe a `regra-0079` pareada para o sexo feminino).

# Evidências

Detecção `P9_SEXO_FUNDAMENTACAO`: o campo `sexo` é "MASCULINO", mas há correspondência da palavra "mulher" na fundamentação e não há correspondência da palavra "homem".

# Questão a investigar

Verificar se houve um erro de "copiar e colar" do texto da fundamentação vindo da regra feminina (regra-0079) para a masculina (regra-0078). Sendo o caso, a fundamentação da `regra-0078` deve ser corrigida para referenciar o critério masculino apropriado ("homem").

# Resolução

Corrigido o texto da fundamentação integral da `regra-0078`, substituindo "mulher" por "homem" para condizer com o sexo do benefício.
