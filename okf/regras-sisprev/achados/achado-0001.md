---
type: Achado
id: achado-0001
nome: Igualdade material entre regra-0012 e regra-0013 (Pensão Morte EC 41/2003 + LC 432/2008)
situacao: resolvido
efeito_deteccao: deve_desaparecer
resolvido_em: 2026-07-28
resolvido_por: franklinbaldo
severidade: informativo
verificacao: hibrida
natureza: dados
deteccoes:
  - detector: P2_IGUALDADE_MATERIAL_ATIVA
    fingerprint: sha256:3575e88f1020f51d1686f3b369909a8278142ab866c3ede8b843a14b6965e029
regras_afetadas:
  - /regras/regra-0012.md
  - /regras/regra-0013.md
detectado_em: 2026-07-17
detectado_por: franklinbaldo
---

# Descrição

`regra-0012` e `regra-0013` ("Pensão Morte Art. 40, §7 da EC 41/2003 e Art. 28 da LC 432/2008 e alterações") eram dois registros ativos com o mesmo `nome` e todas as colunas byte-a-byte idênticas na importação congelada.

# Evidências

Detecção mecânica `P2_IGUALDADE_MATERIAL_ATIVA`: os dois registros caíam no mesmo grupo de igualdade material.

# Questão a investigar

Investigada a duplicação no acervo e confirmada a inexistência de diferenças entre os registros.

# Resolução

A `regra-0013` foi inativada no cadastro (`status_operacional: 'FALSE'`) por constituir duplicação material 100% idêntica da `regra-0012`, resolvendo e cessando a igualdade material ativa no motor do Sisprev.
