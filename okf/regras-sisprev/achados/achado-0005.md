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
    fingerprint: sha256:eab7ba986776cf3f589ac488bab36eeda9c3d8bbe05ffe9856ff10c6595b813d
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
`sha256:eab7ba98…`). `NOME` também coincide.

# Questão a investigar

Apurar se a repetição corresponde a significado externo não modelado,
repetição intencional por configuração do sistema, ou problema de origem.
Resolução (inclusive eventual inativação documentada, P2.1) só após a
conclusão.
