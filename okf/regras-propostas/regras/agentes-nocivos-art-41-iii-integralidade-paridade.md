---
type: RegraProposta
id: agentes-nocivos-art-41-iii-integralidade-paridade
ciclo: ciclo-06
schema_version: 1
estado_auditoria: preview
origens_legacy:
  - regra-0065
  - regra-0066
  - regra-0067
predicados:
  regime: lce-1100-2021
  marco_ingresso: ate-2003
  faixa_exposicao: 86-pontos-25-anos
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      o servidor tomou posse em cargo efetivo até 31/12/2003, não optou pelo
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
    data_adm_apos: 01/01/1950 00:00
    data_adm_ate: 31/12/2003 00:00
    data_direito_apos: 18/10/2021 00:00
    data_direito_ate: 31/12/2099 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
    papel: remissão dos requisitos da aposentadoria voluntária à lei complementar do ente
  - ref: /dispositivos/cf88/art-40-par-4c/ec-103-2019.md
    papel: autorização de requisitos diferenciados por exposição efetiva a agentes nocivos
  - ref: /dispositivos/lce-1100-2021/art-25/original.md
    papel: totalidade da remuneração e corte de ingresso até 31/12/2003
  - ref: /dispositivos/lce-1100-2021/art-27-inc-i/original.md
    papel: paridade e o mesmo corte de ingresso
  - ref: /dispositivos/lce-1100-2021/art-41-inc-iii/original.md
    papel: 86 pontos e 25 anos de exposição, além dos requisitos do caput
projecao:
  nome: Voluntária · agentes nocivos · ingresso até 31/12/2003 · 86 pontos e 25 anos de exposição · integral · paridade
  tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO
  atualmente_no_sistema: 'TRUE'
  ciclo_de_validacao: 3º
  validado_pge: 'FALSE'
  validado_presidencia: 'FALSE'
  simulavel: S
  tipo: CIVIL
  apos_especial: S
  tipo_remun: ''
  paridade: S
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
    exposição, para servidor ingressado em cargo efetivo até 31/12/2003 que não
    tenha optado pelo regime do art. 40, § 16, da Constituição Federal, com
    proventos correspondentes à totalidade da remuneração no cargo efetivo e
    com paridade, nos termos dos arts. 25, 27, I, e 41, III, da Lei
    Complementar Estadual nº 1.100/2021 e do art. 40, §§ 1º, III, e 4º-C, da
    Constituição Federal.
  visivel_dtc_integral: N
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Efetivo
  fundamentacao: ''
proveniencia:
  fontes_consultadas:
    - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
    - /dispositivos/cf88/art-40-par-4c/ec-103-2019.md
    - /dispositivos/lce-1100-2021/art-25/original.md
    - /dispositivos/lce-1100-2021/art-27-inc-i/original.md
    - /dispositivos/lce-1100-2021/art-41-inc-iii/original.md
    - fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt
    - fontes-oficiais/processos-sei/0016_102962-2020-85/parecer_608_pge-iperon__0061369704_.md
    - docs/analysis/processos-sei-da-planilha-da-pge.md
    - docs/analysis/relatorio-residual-agentes-nocivos.md
    - https://diof.ro.gov.br/data/uploads/2022/07/Doe-20-07-2022.pdf
    - https://www.gov.br/previdencia/pt-br/assuntos/rpps/legislacao-dos-rpps/9PortariaMTPn1.467de02jun2022Atualizadaat3jun2024.pdf
  notas: >-
    O parecer PGE/IPERON nº 608/2025 aplica, num caso concreto, exatamente os
    arts. 25, 27, I, e 41, III, com integralidade da última remuneração,
    paridade e prova por PPP. A planilha da PGE contém uma única linha e um
    único processo para o texto reproduzido nas três origens. O valor
    `Valor Efetivo` é adotado apenas como hipótese de projeção porque é o
    membro usado pela regra-0067 para esse mesmo trilho; o significado do enum
    ainda precisa de confirmação do IPERON.
decisoes:
  - data: 2026-07-30
    quem: franklinbaldo
    o_que: >-
      Tratar regra-0065, regra-0066 e regra-0067 como origens coletivas do ramo.
      O legado não registra qual delas corresponderia a cada faixa e cita o
      inciso III nas três; a proposta auditada decompõe o grupo nas três
      hipóteses legais sem inventar uma correspondência individual.
  - data: 2026-07-30
    quem: franklinbaldo
    o_que: >-
      Corrigir na projeção os limites de admissão e de direito demonstrados
      pelos dispositivos, mas manter a unidade em preview e o grupo inativo
      somente enquanto não estiver confirmado qual membro de `tipo_calculo`
      executa a totalidade da remuneração do art. 25.
  - data: 2026-07-30
    quem: franklinbaldo
    o_que: >-
      Confirmar que `requisitos_verificacao_humana` é mecanismo geral da RFC
      0004, não uma coleção exclusiva de incapacidade. Requisito portado em
      `fundamentacao*` só exige `causa_incapacidade` quando essa causa é
      declarada; o preview desta unidade passa a compilar sem pendência.
  - data: 2026-07-30
    quem: franklinbaldo
    o_que: >-
      Fixar `tabelapontuacao: N` para as faixas fixas do art. 41, modelar a
      faixa 86/25 como predicado explícito e completar o ramo com unidades
      próprias para os incisos I e II. Essas questões foram resolvidas pelo
      corpus normativo e pelo padrão interno do catálogo.
  - data: '2026-07-30'
    quem: franklinbaldo
    o_que: >-
      Registrar a unidade de atomicidade desta proposta (RFC 0004, round 11):
      três origens (regra-0065, regra-0066, regra-0067), três destinos, 1:1
      cada. regra-0065 e regra-0066 são materialmente idênticas, e regra-0067
      difere apenas no membro de tipo_calculo; todas citam somente o inciso
      III do art. 41. Os três destinos corrigem as janelas, explicitam as três
      faixas dos incisos I-III do art. 41 e adotam tabelapontuacao: N, porque
      os somatórios são fixos. Irmãs:
      agentes-nocivos-art-41-{i,ii,iii}-integralidade-paridade. Antes
      registrado no Conjunto proposta-auditoria-2026-07 (retirado).
confianca: media
---

# O que esta unidade propõe

As três origens registram somente o art. 41, III da LCE 1.100/2021, no trilho
do art. 25 e do art. 27, I. Elas têm os mesmos dispositivos, fundamentação,
sexo e janelas; `regra-0067` difere apenas no enum de cálculo. O corpus da PGE
tem um caso concreto do inciso III, mas não autoriza excluir os incisos I e II.

Por isso, as três origens são tratadas coletivamente e decompostas nas três
faixas legais. Esta unidade é a faixa 86/25; suas irmãs carregam 66/15 e 76/20.
Não se inventa qual linha legada corresponderia a cada inciso, porque o legado
não preservou essa distinção. O grupo está inativo e o catálogo operacional
permanece intacto.

# Correções propostas

As duas janelas deixam de usar marcos incompatíveis com os próprios
dispositivos:

| campo               | origens      | projeção     |
| ------------------- | ------------ | ------------ |
| `data_adm_ate`      | `31/12/2099` | `31/12/2003` |
| `data_direito_apos` | `31/12/2003` | `18/10/2021` |

`data_adm_ate` é inclusiva e representa o ingresso até 31/12/2003 escrito nos
arts. 25 e 27, I. O marco jurídico é a posse: a Portaria MTP 1.467/2022 usa a
investidura mais remota e a LC 68/1992 determina que a investidura ocorre com a
posse. `data_direito_apos` é o primeiro dia coberto; 18/10/2021 é a vigência da
LCE 1.100/2021. Os demais limites preservam as sentinelas das origens.

A projeção usa `Valor Efetivo`, o valor já empregado pela `regra-0067` para
o mesmo texto e os mesmos dispositivos. Isso não canoniza o significado do
enum. O catálogo também usa `Remuneração de Contribuição` sob o art. 25, e
resta esclarecer internamente se os dois comandos são equivalentes e qual
deles representa a totalidade da remuneração.

# Requisitos e prova

O art. 41, III exige 20 anos de serviço público, 5 anos no cargo, 86 pontos e
25 anos de efetiva exposição. O art. 25 acrescenta ingresso até 31/12/2003 e
ausência de opção pelo regime do art. 40, § 16, da Constituição.

O parecer PGE/IPERON nº 608/2025 transcreve o protocolo documental do art. 42
da LCE 1.100/2021: formulários SB-40, DSS-8030 ou DIRBEN-8030 para os períodos
mais antigos; formulário apoiado em laudo técnico a partir de 06/03/1997; e
PPP a partir de 01/01/2004. No caso concreto, a exposição foi demonstrada por
PPP. Prova exclusivamente testemunhal ou apenas o adicional de insalubridade
não bastam.

Esses fatos não têm colunas próprias no schema legado. Por isso permanecem
textualmente no portador primário `fundamentacao_integral` e dependem de
verificação humana no processo concessório.

# Por que ainda é preview

Resta uma decisão operacional: qual membro de `tipo_calculo` representa o
comando do art. 25. O catálogo usa `Valor Efetivo` e `Remuneração de Contribuição` para o mesmo comando, sem documentar as fórmulas executadas.

As demais dúvidas foram fechadas. `tabelapontuacao: N` é coerente com faixas
fixas, e os incisos I e II passaram a ter unidades próprias. O relatório
residual registra as evidências, a hipótese atual e a informação interna
necessária para resolver apenas o enum de cálculo.

`preview` torna a proposta revisável sem colocá-la no export. A ativação exige
que essas decisões sejam tomadas, que a unidade seja promovida e que o grupo
receba decisão de completude; nenhuma dessas três coisas é presumida aqui.

# Rastreabilidade

- igualdade material entre `regra-0065` e `regra-0066`:
  [`achado-0005`](../../regras-sisprev/achados/achado-0005.md);
- janelas incompatíveis com os dispositivos:
  [`achado-0042`](../../regras-sisprev/achados/achado-0042.md);
- `Valor Médio` incompatível com o trilho dos arts. 25 e 27, I:
  [`achado-0057`](../../regras-sisprev/achados/achado-0057.md);
- correspondência da planilha da PGE:
  [`processos-sei-da-planilha-da-pge.md`](../../../docs/analysis/processos-sei-da-planilha-da-pge.md);
- parecer utilizado:
  [`parecer_608_pge-iperon__0061369704_.md`](../../../fontes-oficiais/processos-sei/0016_102962-2020-85/parecer_608_pge-iperon__0061369704_.md).
