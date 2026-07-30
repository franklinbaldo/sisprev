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
    fingerprint: sha256:15b3040e863551fe807cc99af9d68d89206940eb1b46ca57e263a477cda4654c
regras_afetadas:
  - /regras/regra-0060.md
  - /regras/regra-0064.md
detectado_em: 2026-07-17
detectado_por: franklinbaldo
---

# Descrição

`regra-0060` e `regra-0064` são o par **masculino** correspondente ao
\[[achado-0003]\]: aposentadoria voluntária do servidor com deficiência, com
`nome` indicando dispositivos e graus distintos:

- `regra-0060`: "Art. 35, **inciso II** da Lei Complementar 1.100/2021
  (**MODERADA**)";
- `regra-0064`: "Art. 35, **inciso III** da Lei Complementar 1.100/2021
  (**LEVE**)".

Como no par feminino, as **26 colunas não-`NOME` são idênticas**, inclusive
a Fundamentação Integral, que cita "artigos 25, 27, I; 35" **sem
distinguir o inciso nem o grau**. A diferença em relação ao
\[[achado-0003]\] é apenas `SEXO` (MASCULINO).

# Evidências

Detecção mecânica `P2_IGUALDADE_MATERIAL_ATIVA` (fingerprint
`sha256:56c97f88…`). A distinção inciso II/moderada × inciso III/leve vive
**apenas no `NOME`**.

# Questão a investigar

Idêntica à do \[[achado-0003]\] (par feminino): a distinção entre os graus
moderada (inciso II) e leve (inciso III) tem efeito jurídico nas regras? Se
tem, deveria estar modelada em colunas hoje idênticas ou na fundamentação,
que não a menciona? Perda de informação na importação, distinção externa ao
CSV, ou equivalência real? Convém investigar os dois pares (feminino e
masculino) em conjunto, pois a causa é presumivelmente a mesma. Sem
predeterminar o desfecho.

# Correção realizada

**A hipótese (a) do parágrafo acima é a que se confirmou, e a resposta estava no
próprio catálogo.** O grau não se perdeu na importação para lugar nenhum: o
`nome` importado de cada regra nomeia o inciso e o grau — "Art. 35, inciso II
[...] (MODERADA)". O que faltava era o critério aparecer no campo que o detector
lê. `fundamentacao_integral` citava "artigos 25, 27, I; 35" com o artigo
achatado, e agora cita o **inciso** de cada uma, com `dispositivos:` apontando as
provisões correspondentes, transcritas no bundle nesta rodada.

O grupo se dissolveu, e por diferenciação real: o art. 35 fixa números distintos
por inciso — 20/25 anos para grave, 24/29 para moderada, 28/33 para leve —, então
o que separa as duas regras é critério que a lei usa, não rótulo. Renomear não
teria feito isto: `nome` está fora da chave material do P2, e é justamente por
isso que o grau podia estar declarado ali enquanto o detector via duas regras
idênticas.

A hipótese (c) fica afastada: as duas **não** são equivalentes para efeito de
aposentadoria, porque exigem tempos de contribuição diferentes.

**O que segue valendo da hipótese (b).** O grau agora está declarado na regra,
mas não é **aferido** por coluna nenhuma — a avaliação biopsicossocial do *caput*
do art. 35 é ato externo ao Sisprev. "A regra diz qual é o seu grau" e "o sistema
afere o grau do requerente" continuam sendo coisas diferentes, e a segunda é
lacuna que esta correção não fecha.

As duas regras dispuseram deste achado como `corrigida`, e é da disposição delas
— não de campo no achado — que se deriva a expectativa de a detecção não
reproduzir mais.
