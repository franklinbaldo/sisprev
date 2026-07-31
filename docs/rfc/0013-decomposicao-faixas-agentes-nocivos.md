# RFC 0013 — Decomposição por Faixas Legais de Aposentadoria Especial por Agentes Nocivos (LCE 1.100/2021 e ECE 146/2021)

- **Status**: proposta (2026-07-31). **Especificação de Decomposição de Regras no Catálogo.**
- **Parte de / depende de**: [RFC 0001](0001-criterios-de-validacao-das-regras.md), [RFC 0004](0004-schema-enriquecido-e-compilador-para-o-sisprev.md), [RFC 0006](0006-conjuntos-de-regras.md) e [RFC 0012](0012-identidade-estavel-e-alteracao-substancial.md).
- **Alcança os Achados**: [`achado-0005`](../okf/regras-sisprev/achados/achado-0005.md), [`achado-0006`](../okf/regras-sisprev/achados/achado-0006.md), [`achado-0054`](../okf/regras-sisprev/achados/achado-0054.md), [`achado-0057`](../okf/regras-sisprev/achados/achado-0057.md).

______________________________________________________________________

## 0. Resumo Executivo & Foco em Regras

Esta RFC estabelece a **decomposição das regras de aposentadoria por exposição a agentes nocivos** no catálogo do Sisprev.

O foco central é a **parametrização precisa das colunas de regras**, garantindo que cada faixa legal de pontos e tempo de exposição definida no **Art. 41 da LCE 1.100/2021** (permanente) e no **Art. 8º da ECE 146/2021** (transição) corresponda a um registro autônomo e unívoco no sistema.

______________________________________________________________________

## 1. Decomposição Estruturada das Regras

A legislação estadual estabelece **três faixas fixas de enquadramento**:

1. **Faixa I (Insalubridade/Periculosidade Nível Alto):** 66 pontos e 15 anos de efetiva exposição;
1. **Faixa II (Insalubridade/Periculosidade Nível Médio):** 76 pontos e 20 anos de efetiva exposição;
1. **Faixa III (Insalubridade/Periculosidade Nível Baixo):** 86 pontos e 25 anos de efetiva exposição.

### 1.1 Mapeamento Decomposicional de Regras Legadas para Unidades Auditadas

| Regras Legadas de Origem     | Regime Normativo & Trilho Financeiro                              | Faixa Legal / Dispositivo              | Regra Auditada Resultante                           |
| :--------------------------- | :---------------------------------------------------------------- | :------------------------------------- | :-------------------------------------------------- |
| `regra-0065`, `0066`, `0067` | LCE 1.100/2021 — Integralidade/Paridade (ingresso até 31/12/2003) | Inciso I (66 pts / 15 anos)            | `agentes-nocivos-art-41-i-integralidade-paridade`   |
| `regra-0065`, `0066`, `0067` | LCE 1.100/2021 — Integralidade/Paridade (ingresso até 31/12/2003) | Inciso II (76 pts / 20 anos)           | `agentes-nocivos-art-41-ii-integralidade-paridade`  |
| `regra-0065`, `0066`, `0067` | LCE 1.100/2021 — Integralidade/Paridade (ingresso até 31/12/2003) | Inciso III (86 pts / 25 anos)          | `agentes-nocivos-art-41-iii-integralidade-paridade` |
| `regra-0071`                 | LCE 1.100/2021 — Média / Sem Paridade (ingresso pós 31/12/2003)   | Inciso I (66 pts / 15 anos)            | `agentes-nocivos-art-41-i-media-sem-paridade`       |
| `regra-0071`                 | LCE 1.100/2021 — Média / Sem Paridade (ingresso pós 31/12/2003)   | Inciso II (76 pts / 20 anos)           | `agentes-nocivos-art-41-ii-media-sem-paridade`      |
| `regra-0071`                 | LCE 1.100/2021 — Média / Sem Paridade (ingresso pós 31/12/2003)   | Inciso III (86 pts / 25 anos)          | `agentes-nocivos-art-41-iii-media-sem-paridade`     |
| `regra-0068`, `0069`, `0070` | ECE 146/2021 — Transição (ingresso até 14/09/2021)                | Art. 8º, Inciso I (66 pts / 15 anos)   | `agentes-nocivos-ece146-art-8-i-transicao`          |
| `regra-0068`, `0069`, `0070` | ECE 146/2021 — Transição (ingresso até 14/09/2021)                | Art. 8º, Inciso II (76 pts / 20 anos)  | `agentes-nocivos-ece146-art-8-ii-transicao`         |
| `regra-0068`, `0069`, `0070` | ECE 146/2021 — Transição (ingresso até 14/09/2021)                | Art. 8º, Inciso III (86 pts / 25 anos) | `agentes-nocivos-ece146-art-8-iii-transicao`        |

______________________________________________________________________

## 2. Ajustes de Parâmetros e Colunas Estruturais

Para garantir a simulação correta no Sisprev, os seguintes atributos das regras são corrigidos e padronizados:

1. **`tabelapontuacao: N`**:
   Como os somatórios de 66, 76 e 86 pontos são fixos e não há cláusula de progressão anual no Art. 41 da LCE 1.100/2021 nem no Art. 8º da ECE 146/2021, todas as regras de agentes nocivos gravam **`N`** (corrigindo o erro apontado no [`achado-0054`](../okf/regras-sisprev/achados/achado-0054.md)).

1. **Janelas Temporais Operacionais (`data_adm_*` e `data_direito_*`):**

   - **Trilho Integralidade/Paridade (Arts. 25 e 27, I):** `data_adm_ate: 31/12/2003 00:00` (corte estrito de ingresso) e `data_direito_apos: 18/10/2021 00:00` (vigência da LCE 1.100/2021), corrigindo a inconsistência temporal das sentinelas do [`achado-0042`](../okf/regras-sisprev/achados/achado-0042.md).
   - **Trilho Média/Sem Paridade (Arts. 24 e 27, II):** `data_adm_apos: 01/01/2004 00:00`.

1. **`tipo_calculo` Homogêneo por Trilho:**

   - **`Valor Efetivo`** para o trilho de integralidade/paridade (resolvendo o conflito do [`achado-0057`](../okf/regras-sisprev/achados/achado-0057.md)).
   - **`Valor Médio`** para o trilho de média/sem paridade.

______________________________________________________________________

## 3. Impacto nos Detectores de Auditoria

- **Eliminação de Grupos P2:** A atribuição unívoca de faixas e a correção dos parâmetros elimina as igualdades materiais mecânicas (`P2_IGUALDADE_MATERIAL_ATIVA`) registradas nos achados `achado-0005` e `achado-0006`.
- **Sanidade da Base Legada:** As 112 regras físicas legadas mantêm suas chaves históricas intocadas no repositório; as substituições operam estritamente via a composição declarativa do `Conjunto` `proposta-auditoria-2026-07.md`.
