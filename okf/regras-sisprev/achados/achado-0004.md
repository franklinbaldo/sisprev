---
type: Achado
id: achado-0004
nome: Incisos II e III (graus de deficiência) indistinguíveis entre regra-0060 e regra-0064 (masculino)
situacao: aberto
severidade: informativo
verificacao: mecanica
natureza: dados
deteccoes:
  - detector: P2_IGUALDADE_MATERIAL_ATIVA
    fingerprint: sha256:566e9274be28a369f6877da75453296b35973f8cdad2209780a30ec0c07e014d
regras_afetadas:
  - /regras/regra-0060.md
  - /regras/regra-0064.md
detectado_em: 2026-07-17
detectado_por: franklinbaldo
---

# Descrição

`regra-0060` e `regra-0064` são o par **masculino** correspondente ao
[[achado-0003]]: aposentadoria voluntária do servidor com deficiência, com
`nome` indicando dispositivos e graus distintos:

- `regra-0060`: "Art. 35, **inciso II** da Lei Complementar 1.100/2021
  (**MODERADA**)";
- `regra-0064`: "Art. 35, **inciso III** da Lei Complementar 1.100/2021
  (**LEVE**)".

Como no par feminino, as **26 colunas não-`NOME` são idênticas**, inclusive
a Fundamentação Integral, que cita "artigos 25, 27, I; 35" **sem
distinguir o inciso nem o grau**. A diferença em relação ao
[[achado-0003]] é apenas `SEXO` (MASCULINO).

# Evidências

Detecção mecânica `P2_IGUALDADE_MATERIAL_ATIVA` (fingerprint
`sha256:566e9274…`). A distinção inciso II/moderada × inciso III/leve vive
**apenas no `NOME`**.

# Questão a investigar

Idêntica à do [[achado-0003]] (par feminino): a distinção entre os graus
moderada (inciso II) e leve (inciso III) tem efeito jurídico nas regras? Se
tem, deveria estar modelada em colunas hoje idênticas ou na fundamentação,
que não a menciona? Perda de informação na importação, distinção externa ao
CSV, ou equivalência real? Convém investigar os dois pares (feminino e
masculino) em conjunto, pois a causa é presumivelmente a mesma. Sem
predeterminar o desfecho.
