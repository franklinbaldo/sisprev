---
type: Achado
id: achado-0002
nome: Igualdade material entre regra-0014 e regra-0015 (Pensão Morte LCE 1.100/2021)
situacao: resolvido
efeito_deteccao: deve_desaparecer
resolvido_em: 2026-07-28
resolvido_por: franklinbaldo
severidade: informativo
verificacao: hibrida
natureza: dados
deteccoes:
  - detector: P2_IGUALDADE_MATERIAL_ATIVA
    fingerprint: sha256:c22c07ef0cb53fce8fbfa59c4ff433eb1f2ea196659fbe9f9ee5ca399caecbb5
regras_afetadas:
  - /regras/regra-0014.md
  - /regras/regra-0015.md
detectado_em: 2026-07-17
detectado_por: franklinbaldo
---

# Descrição

`regra-0014` e `regra-0015` ("Pensão por Morte - Art. 46 da Lei Complementar 1.100/2021") eram dois registros ativos com o mesmo `nome` e todas as colunas byte-a-byte idênticas na importação congelada.

# Evidências

Detecção mecânica `P2_IGUALDADE_MATERIAL_ATIVA`: os dois registros caíam no mesmo grupo de igualdade material.

# Questão a investigar

Investigada a duplicação no acervo e confirmada a inexistência de diferenças entre os registros.

# Resolução

A `regra-0015` foi inativada no cadastro (`status_operacional: 'FALSE'`) por constituir duplicação material 100% idêntica da `regra-0014`, resolvendo e cessando a igualdade material ativa no motor do Sisprev.
