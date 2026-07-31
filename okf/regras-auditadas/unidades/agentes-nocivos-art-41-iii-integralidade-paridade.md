---
type: UnidadeAuditada
id: agentes-nocivos-art-41-iii-integralidade-paridade
schema_version: 1
estado_unidade: preview
origens_legacy:
  - regra-0065
  - regra-0066
  - regra-0067
predicados:
  regime: lce-1100-2021
  marco_ingresso: ate-2003
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      o servidor ingressou em cargo efetivo até 31/12/2003, não optou pelo
      regime do art. 40, § 16, da Constituição Federal, cumpriu 20 anos de
      serviço público e 5 anos no cargo, somou 86 pontos e comprovou 25 anos
      de exposição efetiva e permanente a agentes nocivos
    protocolo_verificacao:
      pergunta: >-
        Os assentamentos funcionais e previdenciários e a prova técnica
        demonstram todos os requisitos da regra?
      responsavel: IPERON
      meio_de_prova: >-
        assentamentos funcionais e previdenciários e documentação técnica da
        exposição
      momento: processo concessório
      evidencia_exigida: >-
        registros de ingresso, tempo e opção previdenciária, além de PPP ou,
        conforme o período, formulário e laudo técnico de condições ambientais
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
      Propor a consolidação N:1 de regra-0065, regra-0066 e regra-0067. Não há
      critério de domínio que separe as três, e a planilha da PGE vincula o
      mesmo processo e o mesmo texto às três origens.
  - data: 2026-07-30
    quem: franklinbaldo
    o_que: >-
      Corrigir na projeção os limites de admissão e de direito demonstrados
      pelos dispositivos, mas manter a unidade em preview e o grupo inativo:
      o significado operacional de `Valor Efetivo`, `tabelapontuacao` e a
      cobertura dos incisos I e II do art. 41 ainda dependem de decisão.
  - data: 2026-07-30
    quem: franklinbaldo
    o_que: >-
      Confirmar que `requisitos_verificacao_humana` é mecanismo geral da RFC
      0004, não uma coleção exclusiva de incapacidade. Requisito portado em
      `fundamentacao*` só exige `causa_incapacidade` quando essa causa é
      declarada; o preview desta unidade passa a compilar sem pendência.
confianca: media
---

# O que esta unidade propõe

As três origens descrevem a mesma hipótese jurídica: art. 41, III da LCE
1.100/2021, no trilho do art. 25 e do art. 27, I. Elas têm os mesmos
dispositivos, fundamentação, sexo e janelas. `regra-0065` e `regra-0066` são
materialmente idênticas; `regra-0067` só troca `tipo_calculo: Valor Médio` por
`Valor Efetivo`.

O corpus da PGE reforça que não são três hipóteses. A linha “AGENTES NOCIVOS”
da planilha aponta um único processo, `0016.102962/2020-85`, e seu texto
corresponde às três regras. O parecer desse processo conclui pela concessão
com integralidade da última remuneração e paridade, com os arts. 25, 27, I, e
41, III.

Esta unidade, portanto, consolida as três origens em uma projeção N:1. A
consolidação é proposta, não aplicada: o grupo correspondente está inativo e
o catálogo legado permanece como fonte operacional.

# Correções propostas

As duas janelas deixam de usar marcos incompatíveis com os próprios
dispositivos:

| campo               | origens      | projeção     |
| ------------------- | ------------ | ------------ |
| `data_adm_ate`      | `31/12/2099` | `31/12/2003` |
| `data_direito_apos` | `31/12/2003` | `18/10/2021` |

`data_adm_ate` é inclusiva e representa o ingresso até 31/12/2003 escrito nos
arts. 25 e 27, I. `data_direito_apos` é o primeiro dia coberto; 18/10/2021 é a
vigência da LCE 1.100/2021. Os demais limites preservam as sentinelas das
origens.

A projeção usa `Valor Efetivo`, o valor já empregado pela `regra-0067` para
o mesmo texto e os mesmos dispositivos. Isso não canoniza o significado do
enum. O catálogo também usa `Remuneração de Contribuição` sob o art. 25, e o
IPERON ainda precisa dizer se os dois comandos são equivalentes e qual deles
representa a totalidade da remuneração.

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

Três decisões operacionais impedem promover a unidade a `deployable`:

1. qual membro de `tipo_calculo` representa o comando do art. 25;
2. se `tabelapontuacao` deve ser `S`, já que a regra exige 86 pontos;
3. se o catálogo deve conter unidades adicionais para os incisos I e II do
   art. 41 ou se a granularidade atual é deliberada.

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
