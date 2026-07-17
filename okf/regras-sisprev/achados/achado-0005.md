---
type: Achado
id: achado-0005
nome: Igualdade material entre regra-0065 e regra-0066 (Voluntária - agentes nocivos, Art. 41)
situacao: aberto
severidade: informativo
verificacao: mecanica
natureza: dados
deteccoes:
  - detector: P2_IGUALDADE_MATERIAL_ATIVA
    fingerprint: sha256:3870207bf705ba647e8292fbf7556e596625367be95f8eeb178ec601add5e832
regras_afetadas:
  - /regras/regra-0065.md
  - /regras/regra-0066.md
detectado_em: 2026-07-17
detectado_por: franklinbaldo
---

# Descrição

`regra-0065` e `regra-0066` ("Voluntária do Servidor Exposto a Agentes
Nocivos à Saúde - Artigo 41 da Lei…") são dois registros ativos com o mesmo
`nome` e as 26 colunas não-`NOME` byte-a-byte idênticas.

# Evidências

Detecção mecânica `P2_IGUALDADE_MATERIAL_ATIVA` (fingerprint
`sha256:3870207b…`). `NOME` também coincide.

# Questão a investigar

Apurar se a repetição corresponde a significado externo não modelado,
repetição intencional por configuração do sistema, ou problema de origem.
Resolução (inclusive eventual inativação documentada, P2.1) só após a
conclusão.
