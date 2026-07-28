---
type: Achado
id: achado-0002
nome: Igualdade material entre regra-0014 e regra-0015 (Pensão Morte LCE 1.100/2021)
situacao: aberto
severidade: informativo
verificacao: mecanica
natureza: dados
deteccoes:
  - detector: P2_IGUALDADE_MATERIAL_ATIVA
    fingerprint: sha256:8777baf8575dc494181aa58d812da6b859b6d5ceea6a016a6926fd1363852f89
regras_afetadas:
  - /regras/regra-0014.md
  - /regras/regra-0015.md
detectado_em: 2026-07-17
detectado_por: franklinbaldo
---

# Descrição

`regra-0014` e `regra-0015` ("Pensão por Morte - Art. 46 da Lei Complementar 1.100/2021") são dois registros ativos com o mesmo `nome` e todas as 26 colunas não-`NOME` byte-a-byte idênticas na importação congelada. Não há, nas colunas, nada que as distinga.

# Evidências

Detecção mecânica `P2_IGUALDADE_MATERIAL_ATIVA` (fingerprint `sha256:9be18d36…`): os dois registros caem no mesmo grupo de igualdade material. `NOME` também coincide, então nem o rótulo humano os separa.

# Questão a investigar

Dois registros ativos indistinguíveis multiplicam o custo de auditoria e criam risco de divergência silenciosa. É preciso descobrir se há um significado externo não capturado nas 27 colunas (p.ex. configuração do sistema, contexto de origem distinto), se é repetição intencional, ou se é um problema de origem/modelagem. Nada é fundido nem excluído; se a investigação concluir que um dos registros não representa uma regra autônoma, a inativação documentada (P2.1) fica disponível — nunca antes da confirmação institucional do IPERON.
