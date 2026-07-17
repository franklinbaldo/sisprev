---
type: Achado
id: achado-0002
nome: Igualdade material entre regra-0014, regra-0015
situacao: aberto
severidade: bloqueante
verificacao: mecanica
detector: P2_IGUALDADE_MATERIAL_ATIVA
natureza: dados
regras_afetadas:
- /regras/regra-0014.md
- /regras/regra-0015.md
detectado_em: '2026-07-17'
detectado_por: scripts/validar_regras.py
---

# Descrição

As regras regra-0014, regra-0015 têm todas as colunas originais materialmente idênticas, exceto NOME (P2 ignora o nome na comparação — ver RFC 0001, P1/P2).

# Evidências

Detectado por `P2_IGUALDADE_MATERIAL_ATIVA` em 2026-07-17.

# Questão a investigar

A igualdade material representa redundância indevida, uma distinção não modelada nas 27 colunas, ou outro problema de origem? Ver RFC 0001, P2.

# Resolução


