# RFC 0013 — Decomposição por Faixas Legais de Aposentadoria Especial por Agentes Nocivos (LCE 1.100/2021 e ECE 146/2021)

- **Status**: proposta (2026-07-31). **Especificação de Decomposição de Regras no Catálogo.**
- **Parte de / depende de**: [RFC 0001](0001-criterios-de-validacao-das-regras.md), [RFC 0004](0004-schema-enriquecido-e-compilador-para-o-sisprev.md), [RFC 0006](0006-conjuntos-de-regras.md) e [RFC 0012](0012-identidade-estavel-e-alteracao-substancial.md).
- **Alcança os Achados**: [`achado-0005`](../../okf/regras-sisprev/achados/achado-0005.md), [`achado-0006`](../../okf/regras-sisprev/achados/achado-0006.md), [`achado-0042`](../../okf/regras-sisprev/achados/achado-0042.md), [`achado-0054`](../../okf/regras-sisprev/achados/achado-0054.md), [`achado-0057`](../../okf/regras-sisprev/achados/achado-0057.md).

______________________________________________________________________

## 0. Resumo Executivo & Foco em Regras

Esta RFC estabelece a **decomposição das regras de aposentadoria por exposição a agentes nocivos** no catálogo do Sisprev.

O foco central é a **parametrização precisa das colunas de regras**, garantindo que cada faixa legal de pontos e tempo de exposição definida no **Art. 41 da LCE 1.100/2021** (permanente) e no **Art. 8º da ECE 146/2021** (transição) corresponda a um enquadramento autônomo nas substituições propostas do catálogo.

______________________________________________________________________

## 1. Decomposição Estruturada das Regras

A legislação estadual estabelece **três faixas fixas de exposição**:

1. **Faixa de 66 pontos e 15 anos de efetiva exposição** (Art. 41, I da LCE 1.100/2021 / Art. 8º, I da ECE 146/2021);
2. **Faixa de 76 pontos e 20 anos de efetiva exposição** (Art. 41, II da LCE 1.100/2021 / Art. 8º, II da ECE 146/2021);
3. **Faixa de 86 pontos e 25 anos de efetiva exposição** (Art. 41, III da LCE 1.100/2021 / Art. 8º, III da ECE 146/2021).

### 1.1 Mapeamento Decomposicional para Unidades Auditadas

| Regras Legadas de Origem     | Regime Normativo & Trilho Financeiro                              | Faixa Legal                 | Unidade Auditada Resultante (Proposta no Conjunto)                         |
| :--------------------------- | :---------------------------------------------------------------- | :-------------------------- | :------------------------------------------------------------------------- |
| `regra-0065`, `0066`, `0067` | LCE 1.100/2021 — Integralidade/Paridade (ingresso até 31/12/2003) | 66 pts / 15 anos            | `agentes-nocivos-art-41-i-integralidade-paridade` (já em `preview`)        |
| `regra-0065`, `0066`, `0067` | LCE 1.100/2021 — Integralidade/Paridade (ingresso até 31/12/2003) | 76 pts / 20 anos            | `agentes-nocivos-art-41-ii-integralidade-paridade` (já em `preview`)       |
| `regra-0065`, `0066`, `0067` | LCE 1.100/2021 — Integralidade/Paridade (ingresso até 31/12/2003) | 86 pts / 25 anos            | `agentes-nocivos-art-41-iii-integralidade-paridade` (já em `preview`)      |
| `regra-0071`                 | LCE 1.100/2021 — Média / Sem Paridade (ingresso pós 31/12/2003)   | 66 pts / 15 anos            | `agentes-nocivos-art-41-i-media-sem-paridade` (já `deployable`)            |
| `regra-0071`                 | LCE 1.100/2021 — Média / Sem Paridade (ingresso pós 31/12/2003)   | 76 pts / 20 anos            | `agentes-nocivos-art-41-ii-media-sem-paridade` (já `deployable`)           |
| `regra-0071`                 | LCE 1.100/2021 — Média / Sem Paridade (ingresso pós 31/12/2003)   | 86 pts / 25 anos            | `agentes-nocivos-art-41-iii-media-sem-paridade` (já `deployable`)          |
| `regra-0068`, `0069`, `0070` | ECE 146/2021 — Transição (ingresso até 14/09/2021)                | Art. 8º, Incisos I, II, III | *Escopo futuro:* Unidades a serem autoradas para o Art. 8º da ECE 146/2021 |

______________________________________________________________________

## 2. Ajustes de Parâmetros e Colunas Estruturais

Para garantir a simulação correta nas projeções das Unidades Auditadas, os seguintes atributos das regras são padronizados:

1. **`tabelapontuacao: N`**:
   Como os somatórios de 66, 76 e 86 pontos são fixos e não há cláusula de progressão anual no Art. 41 da LCE 1.100/2021 nem no Art. 8º da ECE 146/2021, as unidades auditadas de agentes nocivos gravam **`N`** (fundamentando a proposta de correção do [`achado-0054`](../../okf/regras-sisprev/achados/achado-0054.md)).

2. **Janelas Temporais Operacionais (`data_adm_*` e `data_direito_*`):**

   - **Trilho Integralidade/Paridade (Arts. 25 e 27, I da LCE 1.100/2021):** `data_adm_ate: 31/12/2003 00:00` (corte estrito de ingresso) e `data_direito_apos: 18/10/2021 00:00` (vigência da LCE 1.100/2021), corrigindo as sentinelas em desconformidade apontadas no [`achado-0042`](../../okf/regras-sisprev/achados/achado-0042.md).
   - **Trilho Média/Sem Paridade (Arts. 24 e 27, II da LCE 1.100/2021):** `data_adm_apos: 31/12/2003 00:00` (conforme convenção exclusiva do schema temporal, englobando admissões a partir de 01/01/2004).

3. **Status de `tipo_calculo` (Integralidade no Art. 25):**

   - O resultado jurídico é a **totalidade da remuneração no cargo efetivo**. A projeção provisória das unidades de integralidade utiliza `Valor Efetivo`, permanecendo em estado `preview` até a confirmação do significado operacional desse membro do enum pelo IPERON (conforme registrado no [`achado-0057`](../../okf/regras-sisprev/achados/achado-0057.md)).

______________________________________________________________________

## 3. Efeito Esperado no Catálogo Resolvido e Detectores

- **Efeito Esperado na carga de implantação:** Quando os componentes correspondentes do grafo origem↔destino estiverem `estado_auditoria: concluida` e `estado_implantacao: confirmada` (RFC 0004, round 11), o catálogo derivado deixará de reproduzir as igualdades materiais mecânicas (`P2_IGUALDADE_MATERIAL_ATIVA`) (alcançando o desfecho esperado para os achados `achado-0005` and `achado-0006`).
- **Preservação da Base Legada:** O catálogo legado original em `okf/regras-sisprev/regras/` permanece intocado, garantindo auditabilidade histórica integral.
