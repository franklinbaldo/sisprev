---
type: Achado
id: achado-0003
nome: Incisos II e III (graus de deficiência) indistinguíveis entre regra-0059 e regra-0063 (feminino)
situacao: aberto
severidade: informativo
verificacao: mecanica
natureza: dados
deteccoes:
  - detector: P2_IGUALDADE_MATERIAL_ATIVA
    fingerprint: sha256:d9b348aafe1ab0dde2274a0dcd9e6241415cfc599ba6353080e7ed65d4acb5b4
regras_afetadas:
  - /regras/regra-0059.md
  - /regras/regra-0063.md
detectado_em: 2026-07-17
detectado_por: franklinbaldo
---

# Descrição

`regra-0059` e `regra-0063` são a aposentadoria voluntária do servidor com
deficiência (feminino), mas os `nome` indicam **dispositivos e graus de
deficiência distintos**:

- `regra-0059`: "Art. 35, **inciso II** da Lei Complementar 1.100/2021
  (**MODERADA**)";
- `regra-0063`: "Art. 35, **inciso III** da Lei Complementar 1.100/2021
  (**LEVE**)".

Apesar dessa distinção jurídica declarada no nome, as **26 colunas
não-`NOME` são byte-a-byte idênticas** — inclusive a Fundamentação
Integral, que é a mesma texto para os dois registros e cita genericamente
"artigos 25, 27, I; 35, da Lei Complementar nº 1.100/2021", **sem mencionar
o inciso (II ou III) nem o grau de deficiência (moderada ou leve)**. A
única coluna que separa este par do par masculino (`regra-0060`/`regra-0064`,
\[[achado-0004]\]) é `SEXO`.

# Evidências

Detecção mecânica `P2_IGUALDADE_MATERIAL_ATIVA` (fingerprint
`sha256:1753d51a…`). A distinção inciso II/moderada × inciso III/leve vive
**apenas no `NOME`**; nenhuma das 26 colunas comparadas — nem a
fundamentação — a captura.

# Questão a investigar

A distinção entre os graus moderada (inciso II) e leve (inciso III) tem
efeito nas regras de elegibilidade/cálculo? Em caso afirmativo, onde ela
deveria estar modelada — em coluna(s) hoje idênticas, na fundamentação (que
não a menciona), ou em dados externos ao CSV? As hipóteses a distinguir
são: (a) houve **perda de informação** na importação (o grau existia na
origem e não foi transposto); (b) a distinção **existe fora do CSV** (regra
de negócio no sistema, não nas colunas); (c) os dois registros são de fato
equivalentes para efeito de aposentadoria e a diferença é só rotular. O
desfecho — inclusive eventual correção de fundamentação ou inativação
documentada (P2.1) — só após a conclusão.
