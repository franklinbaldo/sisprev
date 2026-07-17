---
type: Achado
id: achado-0006
nome: Igualdade material entre regra-0068, regra-0069, regra-0070
situacao: aberto
severidade: bloqueante
verificacao: mecanica
detector: P2_IGUALDADE_MATERIAL_ATIVA
natureza: dados
regras_afetadas:
- /regras/regra-0068.md
- /regras/regra-0069.md
- /regras/regra-0070.md
detectado_em: '2026-07-17'
detectado_por: scripts/validar_regras.py
---

# Descrição

As regras regra-0068, regra-0069, regra-0070 têm todas as colunas originais materialmente idênticas, exceto NOME (P2 ignora o nome na comparação — ver RFC 0001, P1/P2).

# Evidências

Detectado por `P2_IGUALDADE_MATERIAL_ATIVA` em 2026-07-17.

# Questão a investigar

A igualdade material representa redundância indevida, uma distinção não modelada nas 27 colunas, ou outro problema de origem? Ver RFC 0001, P2.

# Resolução


