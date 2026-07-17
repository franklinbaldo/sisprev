---
type: Achado
id: achado-0007
nome: Igualdade material entre regra-0074, regra-0075, regra-0076 e regra-0077 (Voluntária do Policial Civil)
situacao: aberto
severidade: informativo
verificacao: mecanica
natureza: dados
deteccoes:
  - detector: P2_IGUALDADE_MATERIAL_ATIVA
    fingerprint: sha256:4a900ca0b95eaa4dfd7a7acb3d74fbf047a90b616295ecf073ac0e9eef0fd80b
regras_afetadas:
  - /regras/regra-0074.md
  - /regras/regra-0075.md
  - /regras/regra-0076.md
  - /regras/regra-0077.md
detectado_em: 2026-07-17
detectado_por: franklinbaldo
---

# Descrição

`regra-0074` a `regra-0077` ("Voluntária do Policial Civil - Art. 7º, §§ 2º
e 3º da EC nº 146/2021") são **quatro** registros ativos com o mesmo `nome`
e as 26 colunas não-`NOME` byte-a-byte idênticas — o maior grupo de
igualdade material da importação.

# Evidências

Detecção mecânica `P2_IGUALDADE_MATERIAL_ATIVA` (fingerprint
`sha256:4a900ca0…`), envolvendo quatro registros. `NOME` também coincide.

# Questão a investigar

Quatro registros ativos indistinguíveis. Investigar se correspondem a
situações jurídicas distintas (p.ex. sexo, tempo de serviço policial,
regra transitória vs. permanente) que deveriam estar modeladas em colunas
hoje idênticas, ou se é repetição de origem. Como nos demais grupos, a
granularidade da resolução é decidida após a investigação. Nada é fundido
nem excluído; a proveniência das quatro linhas é preservada.
