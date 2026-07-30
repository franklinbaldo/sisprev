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
