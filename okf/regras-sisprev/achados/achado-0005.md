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

A investigação documental mostrou que o legado não grava a distinção. A linha
37 da planilha da PGE, “AGENTES NOCIVOS”, contém um único processo
(`0016.102962/2020-85`) e um único texto do inciso III. O casamento textual
alcança `regra-0065`, `regra-0066` e `regra-0067`; as três citam o inciso III,
embora o art. 41 tenha exatamente três faixas: 66/15, 76/20 e 86/25. A
`regra-0067` difere das duas primeiras apenas em `tipo_calculo`.

O parecer PGE/IPERON nº 608/2025 daquele processo aplica o caso concreto do
arts. 25, 27, I, e 41, III da LCE 1.100/2021, com integralidade da última
remuneração e paridade. Ele comprova a faixa III, mas não autoriza eliminar as
faixas I e II previstas na lei.

# Questão a investigar

A proposta trata 0065–0067 como origens coletivas e cria três destinos, um por
faixa. O novo `predicados.faixa_exposicao` carrega a distinção que as 27 colunas
legadas não expressam. Nenhuma correspondência individual origem→inciso é
inventada.

Resta decidir internamente se o grupo de substituição será adotado. O achado
permanece aberto até essa decisão. Enquanto o grupo estiver inativo, as origens
continuam intactas e operacionais.
