---
type: Achado
id: achado-0001
nome: Igualdade material entre regra-0012 e regra-0013 (Pensão Morte EC 41/2003 + LC 432/2008)
situacao: aberto
severidade: informativo
verificacao: mecanica
natureza: dados
deteccoes:
  - detector: P2_IGUALDADE_MATERIAL_ATIVA
    fingerprint: sha256:f78f8e40de8f48d46f8e6a0390fd3e5ff394444d139697863710033905ca552c
regras_afetadas:
  - /regras/regra-0012.md
  - /regras/regra-0013.md
detectado_em: 2026-07-17
detectado_por: franklinbaldo
---

# Descrição

`regra-0012` e `regra-0013` ("Pensão Morte Art. 40, §7 da EC 41/2003 e
Art. 28 da LC 432/2008 e alterações") são dois registros ativos com o mesmo
`nome` e todas as 26 colunas não-`NOME` byte-a-byte idênticas na importação
congelada. Não há, nas colunas, nada que as distinga.

# Evidências

Detecção mecânica `P2_IGUALDADE_MATERIAL_ATIVA` (fingerprint
`sha256:f78f8e40…`): os dois registros caem no mesmo grupo de igualdade
material. `NOME` também coincide, então nem o rótulo humano os separa.

# Questão a investigar

Dois registros ativos indistinguíveis multiplicam o custo de auditoria e
criam risco de divergência silenciosa. É preciso descobrir se há um
significado externo não capturado nas 27 colunas (p.ex. configuração do
sistema, contexto de origem distinto), se é repetição intencional, ou se é
um problema de origem/modelagem. Nada é fundido nem excluído; se a
investigação concluir que um dos registros não representa uma regra
autônoma, a inativação documentada (P2.1) fica disponível — nunca antes da
conclusão.
