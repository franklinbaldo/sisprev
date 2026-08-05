---
type: Achado
id: achado-0006
nome: Igualdade material entre regra-0068, regra-0069 e regra-0070 (Voluntária - agentes nocivos, EC 146/2021)
situacao: aberto
severidade: informativo
verificacao: mecanica
natureza: dados
deteccoes:
  - detector: P2_IGUALDADE_MATERIAL_ATIVA
    fingerprint: sha256:f2774560c80c6874c74f520cd00fa880372b87d86abc2d4e80f412b3d9f2e383
regras_afetadas:
  - /regras/regra-0068.md
  - /regras/regra-0069.md
  - /regras/regra-0070.md
detectado_em: 2026-07-17
detectado_por: franklinbaldo
---

# Descrição

`regra-0068`, `regra-0069` e `regra-0070` ("Voluntária do Servidor Exposto
a Agentes Nocivos à Saúde da EC 146/2021") são **três** registros ativos
com o mesmo `nome` e as 26 colunas não-`NOME` byte-a-byte idênticas.

# Evidências

Detecção mecânica `P2_IGUALDADE_MATERIAL_ATIVA` (fingerprint
`sha256:8b4bd5cb…`), envolvendo três registros. `NOME` também coincide.

# Questão a investigar

Três registros ativos indistinguíveis. Investigar se há um eixo de
distinção não modelado nas colunas (p.ex. faixas de exposição, grau de
agente nocivo) ou se é repetição de origem. A granularidade da resolução —
um desfecho para os três, ou desfechos distintos — é decidida após a
investigação, não predeterminada. Nada é fundido nem excluído.

# Resolução proposta

As regras 0068, 0069 e 0070 foram investigadas como registros materialmente
idênticos. A distinção que faltava é a faixa de exposição do art. 8º da ECE
146/2021, que deve ser carregada como predicado da regra proposta, não como
edição retroativa do catálogo.

A proposta está registrada na unidade
[`agentes-nocivos-ece-146-2021`](../../regras-propostas/regras/agentes-nocivos-ece-146-2021.md)
(`decisoes`, RFC 0004 round 11). O achado permanece aberto até que o
componente de implantação (`okf/spec/regraproposta.md`) esteja pronto; a
regra legada não é editada e continua sendo a exportação operacional
enquanto isso.
