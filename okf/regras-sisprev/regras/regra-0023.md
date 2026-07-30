---
type: Regra
id: regra-0023
row_index: 23
nome: INVÁLIDA · Compulsória · ingresso até 16/12/1998, requisitos antes de 16/12/1998 · paridade
tipo_de_beneficio: APOSENTADORIA COMPULSÓRIA
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 2º
validado_pge: 'FALSE'
validado_presidencia: 'FALSE'
simulavel: N
tipo: CIVIL
apos_especial: N
tipo_remun: ''
paridade: S
tabelapontuacao: N
requisitos_da_in_no_5_2020: N
relatorio_p_reserva_remunerada_por_idade_ex_officio: N
adicional_inatividade: N
data_adm_ate: 16/12/1998 00:00
data_adm_apos: 01/01/1910 00:00
data_direito_ate: 16/12/1998 00:00
data_direito_apos: 01/01/1910 00:00
fundamentacao_proporcional: Art. 40, inciso II da Constituição Federal de 1988 em seu texto original
visivel_dtc_proporcional: N
fundamentacao_integral: ''
visivel_dtc_integral: N
sexo: ''
integral: ''
tipo_calculo: Não identificado
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-inc-ii/original.md
---

# Estado da análise

Aposentadoria compulsória sob a **redação original do art. 40, II da CF/88** (aos 70 anos de idade, com proventos proporcionais). O registro é `simulavel: N`, implicando que não é passível de processamento automático via motor do Sisprev e requer intervenção humana para análise da fundamentação.

**A janela temporal marca o fim de regime, mas destoa da convenção do catálogo em 1 dia.** A regra indica `data_direito_ate: 16/12/1998`. Conforme diagnosticado no [`achado-0015`](../achados/achado-0015.md), a EC 20/1998 passou a vigorar em 16/12/1998, revogando o regime anterior. Enquanto o restante do catálogo (68 ocorrências) adota a data da nova emenda em intervalos semiabertos `[apos, ate)`, esta regra se apropria do próprio dia da nova emenda para representar o fechamento. A retificação dependerá da definição de um critério comum e seu impacto sobre a avaliação do `MOTOR` do Sisprev, como descrito no achado.

**`data_direito_apos` e `data_adm_apos` usam datas placeholder.** O valor `01/01/1910` é empregado como sentinela de limite inferior por não ter marco de início especificado na norma em relação a um período que antecede a atual estrutura.

Aposentadoria compulsória com proventos proporcionais demanda conferência humana para: o cômputo da idade exata de setenta anos na data da inatividade compulsória e o cálculo apropriado do tempo de serviço exercido para proporção do benefício.

- [x] O marco limite de entrada, 16/12/1998, está associado ao encerramento da vigência da redação original pela EC 20/1998, embora conviva com o desvio de convenção relatado no `achado-0015`
- [ ] O limite superior `data_direito_ate: 16/12/1998` destoa do padrão de fronteiras (dia do início da nova emenda para semiaberto `[apos, ate)`) segundo o [`achado-0015`](../achados/achado-0015.md)
- [ ] Campos estruturais como `sexo`, `integral` vazios e `tipo_calculo` listado como `Não identificado`. Registrado no [`achado-0008`](../achados/achado-0008.md) como pendência
- [x] `dispositivos:` confere perfeitamente com a fundamentação textual (`/dispositivos/cf88/art-40-inc-ii/original.md` transcrito corretamente)
- [x] A regra aplica `paridade: S`, coerente com benefícios de aposentadoria anteriores à EC 41/2003
