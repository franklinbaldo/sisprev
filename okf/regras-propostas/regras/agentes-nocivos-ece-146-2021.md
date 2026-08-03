---
type: RegraProposta
id: agentes-nocivos-ece-146-2021
schema_version: 1
estado_proposta: preview
origens_legacy:
  - regra-0068
  - regra-0069
  - regra-0070
predicados:
  regime: ece-146-2021-art-8
  marco_ingresso: ate-14-09-2021
  faixa_exposicao: 66-pontos-15-anos; 76-pontos-20-anos; 86-pontos-25-anos
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      o servidor ingressou em cargo efetivo até 14/09/2021, não optou pelo
      regime do art. 40, § 16, da Constituição Federal, cumpriu 20 anos de
      serviço público e 5 anos no cargo e comprovou exposição efetiva a
      agentes nocivos pela faixa de 66 pontos/15 anos, 76 pontos/20 anos ou
      86 pontos/25 anos
    protocolo_verificacao:
      pergunta: >-
        Os assentamentos funcionais e previdenciários e a prova técnica
        demonstram todos os requisitos da regra de transição?
      responsavel: >-
        órgão de pessoal e responsável pelos assentamentos funcionais na
        origem, com conferência da equipe de atendimento do IPERON
      meio_de_prova: >-
        assentamentos funcionais e previdenciários, PPP e, conforme o período,
        formulário e laudo técnico de condições ambientais
      momento: instrução e conferência do processo concessório
      evidencia_exigida: >-
        termo de posse, registros de tempo e opção previdenciária e prova
        técnica da exposição exigida pelo art. 8º da ECE 146/2021
    portador_primario: fundamentacao_integral
aplicabilidade_temporal:
  datas_legadas:
    data_adm_apos: 01/01/1950 00:00
    data_adm_ate: 14/09/2021 00:00
    data_direito_apos: 14/09/2021 00:00
    data_direito_ate: 31/12/2024 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-4c/ec-103-2019.md
    papel: autorização constitucional de requisitos diferenciados por exposição efetiva a agentes nocivos
  - ref: /dispositivos/ece-146-2021/art-4/original.md
    papel: preservação dos requisitos e critérios da legislação anterior até 31/12/2024
  - ref: /dispositivos/ece-146-2021/art-8-inc-i/original.md
    papel: faixa de 66 pontos e 15 anos de exposição
  - ref: /dispositivos/ece-146-2021/art-8-inc-ii/original.md
    papel: faixa de 76 pontos e 20 anos de exposição
  - ref: /dispositivos/ece-146-2021/art-8-inc-iii/original.md
    papel: faixa de 86 pontos e 25 anos de exposição
  - ref: /dispositivos/ece-146-2021/art-8-par-1/original.md
    papel: apuração em dias do somatório de idade e tempo de contribuição
  - ref: /dispositivos/ece-146-2021/art-8-par-2/original.md
    papel: cálculo pela média aritmética simples das maiores remunerações
projecao:
  nome: Voluntária · agentes nocivos · ingresso até 14/09/2021 · faixas de 66/15, 76/20 ou 86/25 · integral · média · sem paridade
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
  tabelapontuacao: pendente
  requisitos_da_in_no_5_2020: N
  relatorio_p_reserva_remunerada_por_idade_ex_officio: N
  adicional_inatividade: N
  fundamentacao_proporcional: ''
  visivel_dtc_proporcional: N
  fundamentacao_integral: >-
    Aposentadoria voluntária de servidor exposto de forma efetiva e permanente
    a agentes nocivos à saúde, mediante comprovação de 20 anos de serviço
    público, 5 anos no cargo e uma das faixas de pontuação e exposição do art.
    8º da ECE 146/2021, para servidor ingressado até 14/09/2021, com proventos
    integrais calculados pela média das maiores remunerações e sem paridade,
    nos termos do art. 8º, §§ 1º e 2º, da ECE 146/2021 e do art. 40, § 4º-C,
    da Constituição Federal.
  visivel_dtc_integral: N
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Médio
  fundamentacao: ''
proveniencia:
  fontes_consultadas:
    - /dispositivos/cf88/art-40-par-4c/ec-103-2019.md
    - /dispositivos/ece-146-2021/art-4/original.md
    - /dispositivos/ece-146-2021/art-8-inc-i/original.md
    - /dispositivos/ece-146-2021/art-8-inc-ii/original.md
    - /dispositivos/ece-146-2021/art-8-inc-iii/original.md
    - /dispositivos/ece-146-2021/art-8-par-1/original.md
    - /dispositivos/ece-146-2021/art-8-par-2/original.md
    - docs/analysis/relatorio-residual-agentes-nocivos.md
    - okf/regras-sisprev/achados/achado-0006.md
    - okf/regras-sisprev/achados/achado-0054.md
  notas: >-
    As regras 0068, 0069 e 0070 são materialmente idênticas e não carregam no
    schema legado qual faixa de exposição foi aferida. A unidade preserva as
    três faixas como predicado explícito. `Valor Médio`, integralidade e
    ausência de paridade vêm diretamente do § 2º e do desenho do art. 8º; a
    projeção permanece em preview porque o significado operacional de
    `tabelapontuacao` ainda é a Q9 aberta no achado-0054.
decisoes:
  - data: 2026-07-31
    quem: franklinbaldo
    o_que: >-
      Consolidar as três regras legadas materialmente idênticas em uma unidade
      auditada única, sem editar o catálogo histórico.
  - data: 2026-07-31
    quem: franklinbaldo
    o_que: >-
      Manter `tabelapontuacao` pendente até a decisão institucional sobre se o
      campo representa tabela progressiva ou qualquer somatório de pontos.
confianca: alta
---

# O que esta unidade propõe

As regras 0068, 0069 e 0070 repetem a mesma fundamentação, as mesmas datas e os
mesmos efeitos. A diferença que deveria existir — a faixa de exposição — não é
representada no catálogo legado. A unidade substitui o trio por uma descrição
única que explicita as três faixas do art. 8º, sem escolher artificialmente uma
delas.

O art. 8º, § 2º, funda diretamente o cálculo por média. A ausência de paridade
decorre do regime de reajuste da regra de transição e da própria projeção
legada. Nenhum parecer ou planilha é usado para criar o critério jurídico.

# Por que ainda é preview

O achado-0054 demonstra que as regras transitórias gravam
`tabelapontuacao: S`, enquanto as regras permanentes do art. 41 gravam `N`,
embora os dois dispositivos tenham as mesmas três faixas fixas. A unidade não
antecipa a resposta à Q9: `tabelapontuacao: pendente` registra a dúvida
operacional e impede sua entrada no catálogo deployable.

# Substituição proposta

O conjunto de julho de 2026 registra a relação 3:1:

| legado       | regra proposta |
| ------------ | -------------- |
| `regra-0068` | esta unidade   |
| `regra-0069` | esta unidade   |
| `regra-0070` | esta unidade   |

Enquanto o grupo estiver inativo, as três regras legadas continuam sendo a
exportação operacional. A criação desta unidade é uma proposta auditável, não
uma alteração retroativa do Sisprev.
