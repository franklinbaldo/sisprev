# RFC 0013 — Decomposição por Faixas Legais de Aposentadoria Especial por Agentes Nocivos (LCE 1.100/2021 e ECE 146/2021)

- **Status**: proposta (2026-07-31). **Especificação e Modelo Normativo de Decomposição.**
- **Parte de / depende de**: [RFC 0001](0001-criterios-de-validacao-das-regras.md), [RFC 0004](0004-schema-enriquecido-e-compilador-para-o-sisprev.md), [RFC 0006](0006-conjuntos-de-regras.md) e [RFC 0012](0012-identidade-estavel-e-alteracao-substancial.md).
- **Alcança os Achados**: [`achado-0005`](../okf/regras-sisprev/achados/achado-0005.md), [`achado-0006`](../okf/regras-sisprev/achados/achado-0006.md), [`achado-0054`](../okf/regras-sisprev/achados/achado-0054.md), [`achado-0057`](../okf/regras-sisprev/achados/achado-0057.md).

---

## 0. Resumo Executivo & Contexto

A auditoria do catálogo legado do Sisprev identificou uma divergência estrutural recorrente nas regras de aposentadoria voluntária por exposição a agentes nocivos à saúde (insalubridade e periculosidade).

Tanto a regra permanente (**Art. 41 da Lei Complementar Estadual nº 1.100/2021**) quanto a regra de transição (**Art. 8º da Emenda Constitucional Estadual nº 146/2021**) estabelecem expressamente **três faixas fixas de exposição e pontuação**, conforme o grau de nocividade do agente:

1. **Inciso I (Insalubridade/Periculosidade Nível Alto):** 66 pontos e 15 anos de efetiva exposição;
2. **Inciso II (Insalubridade/Periculosidade Nível Médio):** 76 pontos e 20 anos de efetiva exposição;
3. **Inciso III (Insalubridade/Periculosidade Nível Baixo/Geral):** 86 pontos e 25 anos de efetiva exposição.

No catálogo legado, contudo:
- As regras `regra-0065`, `regra-0066` e `regra-0067` herdaram genericamente a menção ao **Inciso III**, omitindo as faixas dos incisos I e II;
- As regras de transição `regra-0068`, `regra-0069` e `regra-0070` foram cadastradas como três registros idênticos (`P2_IGUALDADE_MATERIAL_ATIVA`), sem distinguir qual faixa legal cada uma atendia e marcando indevidamente `tabelapontuacao: S`.

Esta RFC formaliza a arquitetura de **decomposição por faixas legais de pontos/tempo**, definindo a transição do catálogo sem consolidação destrutiva e sem alteração da chave material legada.

---

## 1. Princípios e Arquitetura de Solução

### 1.1 Não Fusão Falsa vs. Decomposição Estruturada
Simplesmente fundir as 3 regras legadas em 1 único registro apagaria o direito dos servidores expostos às faixas de 15 e 20 anos de serviço especial. A solução adota a **decomposição 3:3** (ou N:M) por meio do mecanismo de **Unidades Auditadas** (RFC 0004) agrupadas num `Conjunto` derivado (RFC 0006).

### 1.2 Separação de Trilhos Financeiros e Paridade
A LCE 1.100/2021 estabelece dois trilhos de cálculo distintos conforme a data de ingresso no serviço público:
- **Trilho Integralidade/Paridade (Ingresso até 31/12/2003):** Proventos correspondentes à totalidade da remuneração no cargo efetivo (Art. 25) e reajuste por paridade (Art. 27, I).
- **Trilho Média/Sem Paridade (Ingresso após 31/12/2003):** Cálculo por média aritmética (Art. 24) e reajuste sem paridade pelo RGPS (Art. 27, II).

### 1.3 Correção do Campo `tabelapontuacao`
Conforme demonstrado no [`achado-0054`](../okf/regras-sisprev/achados/achado-0054.md), a coluna `tabelapontuacao` indica a presença de **tabela progressiva anual** (ex: acréscimo de 1 ponto por ano). Como nem o Art. 41 da LCE 1.100/2021 nem o Art. 8º da ECE 146/2021 possuem cláusula de progressão anual (as somas de 66, 76 e 86 pontos são fixas), **todas as Unidades Auditadas de Agentes Nocivos adotam estritamente `tabelapontuacao: N`**.

---

## 2. Mapeamento das Unidades Auditadas e Grupos de Substituição

A proposta de decomposição é estruturada em **três grupos atômicos de substituição** no arquivo de conjunto `okf/conjuntos/proposta-auditoria-2026-07.md`:

### Grupo 1: Regime Permanente — Integralidade e Paridade (Art. 41 c/c Arts. 25 e 27, I da LCE 1.100/2021)
* **Origens Legadas (3):** `regra-0065`, `regra-0066`, `regra-0067`
* **Destinos Auditados (3):**
  1. `agentes-nocivos-art-41-i-integralidade-paridade.md` (66 pts / 15 anos)
  2. `agentes-nocivos-art-41-ii-integralidade-paridade.md` (76 pts / 20 anos)
  3. `agentes-nocivos-art-41-iii-integralidade-paridade.md` (86 pts / 25 anos)

### Grupo 2: Regime Permanente — Média e Sem Paridade (Art. 41 c/c Arts. 24 e 27, II da LCE 1.100/2021)
* **Origem Legada (1):** `regra-0071`
* **Destinos Auditados (3):**
  1. `agentes-nocivos-art-41-i-media-sem-paridade.md` (66 pts / 15 anos)
  2. `agentes-nocivos-art-41-ii-media-sem-paridade.md` (76 pts / 20 anos)
  3. `agentes-nocivos-art-41-iii-media-sem-paridade.md` (86 pts / 25 anos)

### Grupo 3: Regra Transitória — ECE 146/2021 (Art. 8º, Incisos I, II e III)
* **Origens Legadas (3):** `regra-0068`, `regra-0069`, `regra-0070`
* **Destinos Auditados (3):**
  1. `agentes-nocivos-ece146-art-8-i-transicao.md` (66 pts / 15 anos)
  2. `agentes-nocivos-ece146-art-8-ii-transicao.md` (76 pts / 20 anos)
  3. `agentes-nocivos-ece146-art-8-iii-transicao.md` (86 pts / 25 anos)

---

## 3. Matriz de Atributos e Predicados Enriquecidos

Nas Unidades Auditadas, a diferenciação de faixas utiliza o predicado estendido `faixa_exposicao`:

```yaml
predicados:
  regime: lce-1100-2021
  marco_ingresso: ate-2003 # ou apos-2003
  faixa_exposicao: 66-pontos-15-anos # | 76-pontos-20-anos | 86-pontos-25-anos
  sexo: ambos
```

E no frontmatter deployável projetado:
- `tabelapontuacao: N`
- `data_adm_ate: 31/12/2003 00:00` (para o trilho de integralidade/paridade)
- `data_direito_apos: 18/10/2021 00:00` (data de vigência da LCE 1.100/2021)

---

## 4. Requisitos de Verificação Humana (Anamnese Probatória)

Como o motor do simulador afere idade e tempo de contribuição mas não possui colunas específicas para tempo de exposição ambiental nem laudos técnicos, as Unidades Auditadas incluem o protocolo explícito:

1. **Laudo Técnico de Condições Ambientais do Trabalho (LTCAT)** ou **Perfil Profissiográfico Previdenciário (PPP)** atestando a exposição contínua e ininterrupta aos agentes nocivos;
2. **Formulários Históricos (SB-40 / DSS-8030 / DIRBEN-8030)** para períodos de atividade anteriores a 01/01/2004;
3. Aferição do tempo mínimo de 20 anos de efetivo exercício no serviço público e 5 anos no cargo efetivo em que se dará a aposentadoria.

---

## 5. Impacto nos Detectores e Validação

- **Dissolvimento dos P2 (Igualdade Material):** Com a decomposição formal nas Unidades Auditadas, os grupos `P2_IGUALDADE_MATERIAL_ATIVA` dos achados 0005 e 0006 deixam de existir no catálogo auditado resolvido (`resolve(C)`).
- **Sanidade de Transição:** As regras legadas continuam 100% preservadas em `okf/regras-sisprev/regras/` para fins de auditoria histórica até que o conjunto `proposta-auditoria-2026-07.md` passe do estado `proposto` para `vigente`.
