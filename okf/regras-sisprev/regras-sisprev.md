---
type: Dataset
title: Regras do Sisprev — Regime Próprio de Previdência (RO)
description: Catálogo de regras de aposentadoria e pensão por morte do Sisprev, com
  fundamentação legal, elegibilidade e forma de cálculo.
tags:
- previdencia
- aposentadoria
- pensao
- sisprev
- rondonia
source_file: data/raw/regras-sisprev.csv
row_count: 112
columns:
- NOME
- TIPO DE BENEFICIO
- ATUALMENTE NO SISTEMA
- CICLO DE VALIDAÇÃO
- VALIDADO PGE
- VALIDADO PRESIDENCIA
- SIMULAVEL
- TIPO
- APOS_ESPECIAL
- TIPO_REMUN
- PARIDADE
- TabelaPontuacao
- Requisitos da IN Nº 5/2020
- Relatório p/ Reserva Remunerada por Idade ex-officio
- ADICIONAL_INATIVIDADE
- DATA_ADM_ATE
- DATA_ADM_APOS
- DATA_DIREITO_ATE
- DATA_DIREITO_APOS
- FUNDAMENTACAO_PROPORCIONAL
- VISIVEL DTC PROPORCIONAL
- FUNDAMENTACAO_INTEGRAL
- VISIVEL DTC INTEGRAL
- SEXO
- INTEGRAL
- TIPO_CALCULO
- FUNDAMENTACAO
---

Catálogo de regras de aposentadoria e pensão por morte do Sisprev, com fundamentação legal, elegibilidade e forma de cálculo.

# Schema

| Coluna | Destino | Tipo | Categoria semântica | Semântica de vazio |
|---|---|---|---|---|
| `NOME` | `nome` (frontmatter) | string | identidade humana (P1) | não vazio |
| `TIPO DE BENEFICIO` | `tipo_de_beneficio` (frontmatter) | string (enum) | candidato a predicado de seleção (Q3) | a definir |
| `ATUALMENTE NO SISTEMA` | `atualmente_no_sistema` (frontmatter) | TRUE/FALSE | estado no Sisprev real — não confundir com status_regra (P2.1) | não vazio |
| `CICLO DE VALIDAÇÃO` | `ciclo_de_validacao` (frontmatter) | string (1º-4º) | ordenação do processo de auditoria | não vazio |
| `VALIDADO PGE` | `validado_pge` (frontmatter) | TRUE/FALSE | legado — candidato a derivar de atos_validacao (P7) | não vazio |
| `VALIDADO PRESIDENCIA` | `validado_presidencia` (frontmatter) | TRUE/FALSE | legado — candidato a derivar de atos_validacao (P7) | não vazio |
| `SIMULAVEL` | `simulavel` (frontmatter) | S/N | candidato a apresentação/interface (Q9) | a definir |
| `TIPO` | `tipo` (frontmatter) | string | candidato a predicado de seleção (Q3) | a definir |
| `APOS_ESPECIAL` | `apos_especial` (frontmatter) | S/N | candidato a predicado ou apresentação (Q3, Q9) | a definir |
| `TIPO_REMUN` | `tipo_remun` (frontmatter) | string | candidato a apresentação/interface (Q9) | a definir |
| `PARIDADE` | `paridade` (frontmatter) | S/N | candidato a resultado/efeito (Q6) | a definir |
| `TabelaPontuacao` | `tabelapontuacao` (frontmatter) | S/N | a investigar (Q9) | a definir |
| `Requisitos da IN Nº 5/2020` | `requisitos_da_in_no_5_2020` (frontmatter) | S/N | candidato a apresentação/interface (Q9) | a definir |
| `Relatório p/ Reserva Remunerada por Idade ex-officio` | `relatorio_p_reserva_remunerada_por_idade_ex_officio` (frontmatter) | S/N | candidato a apresentação/interface (Q9) | a definir |
| `ADICIONAL_INATIVIDADE` | `adicional_inatividade` (frontmatter) | S/N | candidato a resultado/efeito ou apresentação (Q6, Q9) | a definir |
| `DATA_ADM_ATE` | `data_adm_ate` (frontmatter) | datetime (DD/MM/AAAA HH:MM) | elegibilidade temporal — ordenação estrutural confirmada (P5); fato jurídico a investigar (Q1) | sentinela — preservada, não interpretada (P5) |
| `DATA_ADM_APOS` | `data_adm_apos` (frontmatter) | datetime (DD/MM/AAAA HH:MM) | elegibilidade temporal — ordenação estrutural confirmada (P5); fato jurídico a investigar (Q1) | sentinela — preservada, não interpretada (P5) |
| `DATA_DIREITO_ATE` | `data_direito_ate` (frontmatter) | datetime (DD/MM/AAAA HH:MM) | elegibilidade temporal — ordenação estrutural confirmada (P5); fato jurídico a investigar (Q2) | sentinela — preservada, não interpretada (P5) |
| `DATA_DIREITO_APOS` | `data_direito_apos` (frontmatter) | datetime (DD/MM/AAAA HH:MM) | elegibilidade temporal — ordenação estrutural confirmada (P5); fato jurídico a investigar (Q2) | sentinela — preservada, não interpretada (P5) |
| `FUNDAMENTACAO_PROPORCIONAL` | `# Fundamentação Proporcional` (corpo) | text | fundamentação (corpo) | a definir (Q7 — por que uma regra pode ter as duas fundamentações?) |
| `VISIVEL DTC PROPORCIONAL` | `visivel_dtc_proporcional` (frontmatter) | S/N | candidato a apresentação/interface (Q9) | a definir |
| `FUNDAMENTACAO_INTEGRAL` | `# Fundamentação Integral` (corpo) | text | fundamentação (corpo) | a definir (Q7 — por que uma regra pode ter as duas fundamentações?) |
| `VISIVEL DTC INTEGRAL` | `visivel_dtc_integral` (frontmatter) | S/N | candidato a apresentação/interface (Q9) | a definir |
| `SEXO` | `sexo` (frontmatter) | string (enum) | candidato a predicado de seleção (Q3) | a investigar (Q10 — AMBOS vs. vazio vs. desconhecido vs. não aplicável) |
| `INTEGRAL` | `integral` (frontmatter) | S/N | candidato a resultado/efeito (Q6) | a definir |
| `TIPO_CALCULO` | `tipo_calculo` (frontmatter) | string (enum) | candidato a resultado/efeito (Q6) | a investigar (Q10 — 'Não identificado' sem significado presumido) |
| `FUNDAMENTACAO` | `# Fundamentação` (corpo) | text | fundamentação (corpo) | a definir |

# Regras

Uma regra por linha da planilha original — ver [regras/](regras/index.md).
