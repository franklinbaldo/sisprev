---
type: Achado
id: achado-0002
nome: Igualdade material entre regra-0014 e regra-0015 (Pensão por Morte LC 1.100/2021)
situacao: aberto
severidade: informativo
verificacao: mecanica
natureza: dados
deteccoes:
  - detector: P2_IGUALDADE_MATERIAL_ATIVA
    fingerprint: sha256:d2f6ff42b02cf361a4c317b9d2581ee444c906b211f6784091857c6c29df079c
regras_afetadas:
  - /regras/regra-0014.md
  - /regras/regra-0015.md
detectado_em: 2026-07-17
detectado_por: franklinbaldo
---

# Descrição

`regra-0014` e `regra-0015` ("Pensão por Morte - Art. 46 da Lei
Complementar 1.100/2021") são dois registros ativos com o mesmo `nome` e as
26 colunas não-`NOME` byte-a-byte idênticas na importação congelada.

# Evidências

Detecção mecânica `P2_IGUALDADE_MATERIAL_ATIVA` (fingerprint
`sha256:d2f6ff42…`). `NOME` também coincide.

# Questão a investigar

Mesma questão da igualdade material: apurar se a repetição corresponde a um
significado externo não modelado, a uma repetição intencional por
configuração do sistema, ou a um problema de origem. A resolução (inclusive
eventual inativação documentada de um registro, P2.1) só depois da
conclusão da investigação.
