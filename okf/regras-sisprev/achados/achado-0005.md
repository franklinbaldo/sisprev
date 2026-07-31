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
    fingerprint: sha256:79e25591ca457ab8777de9a8ae6d17735909e53d1974b807d94d7d1d0ac0b666
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
`sha256:79e25591…`). `NOME` também coincide.

A investigação documental não encontrou distinção externa. A linha 37 da
planilha da PGE, “AGENTES NOCIVOS”, contém um único processo
(`0016.102962/2020-85`) e um único texto. O casamento textual desse registro
alcança `regra-0065`, `regra-0066` e `regra-0067`; as três citam os mesmos
dispositivos e descrevem a mesma hipótese. A `regra-0067` difere das duas
primeiras apenas em `tipo_calculo`.

O parecer PGE/IPERON nº 608/2025 daquele processo aplica uma única regra:
arts. 25, 27, I, e 41, III da LCE 1.100/2021, com integralidade da última
remuneração e paridade. Não há no processo ou na planilha evidência de três
configurações distintas.

# Questão a investigar

A evidência disponível favorece repetição de origem, não significado externo.
A proposta
[`agentes-nocivos-art-41-iii-integralidade-paridade`](../../regras-auditadas/unidades/agentes-nocivos-art-41-iii-integralidade-paridade.md)
consolida as três linhas em uma unidade auditada, dentro de grupo inativo.

Resta ao IPERON confirmar que nenhuma configuração externa exige linhas
separadas e decidir se adota a consolidação. Até essa decisão, as origens
continuam intactas e operacionais e o achado permanece aberto.
