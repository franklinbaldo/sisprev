---
type: RegraProposta
id: agentes-nocivos-art-41-iii-media-sem-paridade
ciclo: ciclo-06
schema_version: 1
estado_auditoria: concluida
origens_legacy:
  - regra-0071
predicados:
  regime: lce-1100-2021
  marco_ingresso: apos-2003
  faixa_exposicao: 86-pontos-25-anos
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      o servidor tomou posse em cargo efetivo após 31/12/2003, não optou pelo
      regime do art. 40, § 16, da Constituição Federal, cumpriu 20 anos de
      serviço público e 5 anos no cargo, somou 86 pontos e comprovou 25 anos
      de exposição efetiva e permanente a agentes nocivos
    protocolo_verificacao:
      pergunta: >-
        Os assentamentos funcionais e previdenciários e a prova técnica
        demonstram todos os requisitos da regra?
      responsavel: >-
        órgão de pessoal e responsável pelos assentamentos funcionais na
        origem, com conferência da equipe de atendimento do IPERON
      meio_de_prova: >-
        assentamentos funcionais e previdenciários, PPP e, conforme o período,
        formulário e laudo técnico de condições ambientais
      momento: instrução e conferência do processo concessório
      evidencia_exigida: >-
        termo de posse, registros de tempo e opção previdenciária e prova
        técnica da exposição exigida pelo art. 42 da LCE 1.100/2021
    portador_primario: fundamentacao_integral
aplicabilidade_temporal:
  datas_legadas:
    data_adm_apos: 31/12/2003 00:00
    data_adm_ate: 31/12/2099 00:00
    data_direito_apos: 18/10/2021 00:00
    data_direito_ate: 31/12/2099 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
    papel: remissão dos requisitos da aposentadoria voluntária à lei complementar do ente
  - ref: /dispositivos/cf88/art-40-par-4c/ec-103-2019.md
    papel: autorização de requisitos diferenciados por exposição efetiva a agentes nocivos
  - ref: /dispositivos/lce-1100-2021/art-24/original.md
    papel: média das maiores remunerações e corte de ingresso após 31/12/2003
  - ref: /dispositivos/lce-1100-2021/art-27-inc-ii/original.md
    papel: reajuste nos termos do RGPS e o mesmo corte de ingresso
  - ref: /dispositivos/lce-1100-2021/art-41-inc-iii/original.md
    papel: 86 pontos e 25 anos de exposição, além dos requisitos do caput
projecao:
  nome: Voluntária · agentes nocivos · ingresso após 31/12/2003 · 86 pontos e 25 anos de exposição · média · sem paridade
  tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO
  atualmente_no_sistema: 'TRUE'
  ciclo_de_validacao: 3º
  validado_pge: 'FALSE'
  validado_presidencia: 'FALSE'
  simulavel: S
  tipo: CIVIL
  apos_especial: S
  tipo_remun: ''
  paridade: N
  tabelapontuacao: N
  requisitos_da_in_no_5_2020: N
  relatorio_p_reserva_remunerada_por_idade_ex_officio: N
  adicional_inatividade: N
  fundamentacao_proporcional: ''
  visivel_dtc_proporcional: N
  fundamentacao_integral: >-
    Aposentadoria voluntária de servidor exposto de forma efetiva e permanente
    a agentes nocivos à saúde, mediante comprovação no processo concessório de
    20 anos de serviço público, 5 anos no cargo, 86 pontos e 25 anos de
    exposição, para servidor ingressado em cargo efetivo após 31/12/2003 que
    não tenha optado pelo regime do art. 40, § 16, da Constituição Federal,
    com proventos integrais calculados pela média das maiores remunerações
    correspondentes a 80% do período contributivo e reajuste nos termos do
    RGPS, sem paridade, conforme os arts. 24, 27, II, e 41, III, da Lei
    Complementar Estadual nº 1.100/2021 e o art. 40, §§ 1º, III, e 4º-C, da
    Constituição Federal.
  visivel_dtc_integral: N
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Médio
  fundamentacao: ''
proveniencia:
  fontes_consultadas:
    - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
    - /dispositivos/cf88/art-40-par-4c/ec-103-2019.md
    - /dispositivos/lce-1100-2021/art-24/original.md
    - /dispositivos/lce-1100-2021/art-27-inc-ii/original.md
    - /dispositivos/lce-1100-2021/art-41-inc-iii/original.md
    - fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt
    - fontes-oficiais/processos-sei/0016_102962-2020-85/parecer_608_pge-iperon__0061369704_.md
    - docs/analysis/processos-sei-da-planilha-da-pge.md
    - docs/analysis/relatorio-residual-agentes-nocivos.md
    - https://diof.ro.gov.br/data/uploads/2022/07/Doe-20-07-2022.pdf
    - https://www.gov.br/previdencia/pt-br/assuntos/rpps/legislacao-dos-rpps/9PortariaMTPn1.467de02jun2022Atualizadaat3jun2024.pdf
  notas: >-
    A linha da planilha da PGE correspondente à regra-0071 não indica processo
    SEI. O Parecer PGE/IPERON nº 608/2025 é consultado somente quanto ao
    protocolo documental comum da exposição do art. 41/42; seu caso concreto
    segue os arts. 25 e 27, I, e não é evidência do cálculo pós-2003. A média e
    a ausência de paridade desta unidade vêm diretamente dos arts. 24 e 27, II.
decisoes:
  - data: 2026-07-30
    quem: franklinbaldo
    o_que: >-
      Propor a correção da direção do corte de admissão: o valor 31/12/2003 sai
      de `data_adm_ate` e passa para `data_adm_apos`, cuja semântica é excluir
      o último dia do regime anterior e alcançar os ingressos posteriores.
  - data: 2026-07-30
    quem: franklinbaldo
    o_que: >-
      Preservar `Valor Médio`, `paridade: N`, `integral: S` e o marco de direito
      18/10/2021, todos coerentes com os arts. 24, 27, II, e a vigência da LCE
      1.100/2021.
  - data: 2026-07-30
    quem: franklinbaldo
    o_que: >-
      Fixar `tabelapontuacao: N` para as faixas fixas do art. 41, modelar a
      faixa 86/25 como predicado explícito, completar o ramo com os incisos I
      e II e promover esta unidade a deployable. O grupo permanece inativo.
  - data: '2026-07-30'
    quem: franklinbaldo
    o_que: >-
      Registrar a unidade de atomicidade desta proposta (RFC 0004, round 11):
      uma origem (regra-0071), três destinos, 1:3 — o ramo pós-2003. Preserva
      Valor Médio, paridade: N e o marco de direito da LCE 1.100/2021, move o
      corte 31/12/2003 de data_adm_ate para data_adm_apos e completa os
      incisos I-III do art. 41. Irmãs:
      agentes-nocivos-art-41-{i,ii,iii}-media-sem-paridade. Antes registrado
      no Conjunto proposta-auditoria-2026-07 (retirado).
confianca: alta
---

# O que esta unidade propõe

`regra-0071` é o ramo pós-2003 da hipótese do art. 41, III da LCE 1.100/2021.
Os arts. 24 e 27, II determinam, respectivamente, cálculo pela média das
maiores remunerações correspondentes a 80% do período contributivo e reajuste
nos termos do RGPS. `Valor Médio` e `paridade: N` estão coerentes.

O defeito está isolado na direção do corte de admissão. A origem grava
`data_adm_ate: 31/12/2003`, embora os dois artigos alcancem apenas ingresso
**após** essa data. A projeção move o mesmo valor para `data_adm_apos`, campo
cuja semântica é exclusiva: 31/12/2003 é o último dia do regime anterior, e
01/01/2004 é o primeiro dia coberto.

# Comparação com a origem

| campo               | `regra-0071`  | projeção     |
| ------------------- | ------------- | ------------ |
| `data_adm_apos`     | `01/01/1950`  | `31/12/2003` |
| `data_adm_ate`      | `31/12/2003`  | `31/12/2099` |
| `data_direito_apos` | `18/10/2021`  | idêntico     |
| `tipo_calculo`      | `Valor Médio` | idêntico     |
| `paridade`          | `N`           | idêntico     |

A forma proposta já existe nas regras 0080 e 0081, que citam o mesmo par
arts. 24/27, II e gravam `data_adm_apos: 31/12/2003`. Isso não prova a causa
do erro de 0071, mas confirma que o schema expressa o corte correto.

# Requisitos e prova

O art. 41, III exige 20 anos de serviço público, 5 anos no cargo, 86 pontos e
25 anos de exposição efetiva. O art. 24 acrescenta ingresso após 31/12/2003 e
ausência de opção pelo regime do art. 40, § 16, da Constituição.

O Parecer PGE/IPERON nº 608/2025 é usado aqui com alcance limitado: ele
transcreve o protocolo documental do art. 42 — formulários históricos,
formulário apoiado em laudo técnico e PPP — e registra um caso comprovado por
PPP. O parecer não valida o cálculo desta unidade, porque o caso concreto
estava no ramo pré-2004. Média e ausência de paridade são conferidas
diretamente nos arts. 24 e 27, II.

# Estado da unidade

A unidade está `deployable`: os arts. 24, 27, II, e 41, III resolvem janela,
cálculo, reajuste e faixa; `tabelapontuacao: N` é coerente com somatório fixo;
e o protocolo de prova e suas responsabilidades constam do Decreto 27.338/2022
e do art. 42.

O grupo permanece inativo. Portanto, a promoção de maturidade não altera o
catálogo vigente nem a exportação operacional.

# Rastreabilidade

- incompatibilidade da janela:
  [`achado-0042`](../../regras-sisprev/achados/achado-0042.md);
- regra de origem:
  [`regra-0071`](../../regras-sisprev/regras/regra-0071.md);
- parecer usado apenas para o protocolo de prova:
  [`parecer_608_pge-iperon__0061369704_.md`](../../../fontes-oficiais/processos-sei/0016_102962-2020-85/parecer_608_pge-iperon__0061369704_.md).
