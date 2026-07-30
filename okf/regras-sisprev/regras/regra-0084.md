---
type: Regra
id: regra-0084
row_index: 84
nome: Voluntária · Policial penal · por mandado de injunção · Ambos · integral · média
tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 3º
validado_pge: 'FALSE'
validado_presidencia: 'FALSE'
simulavel: N
tipo: CIVIL
apos_especial: S
tipo_remun: ''
paridade: N
tabelapontuacao: N
requisitos_da_in_no_5_2020: N
relatorio_p_reserva_remunerada_por_idade_ex_officio: N
adicional_inatividade: N
data_adm_ate: 31/12/2099 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 01/01/1950 00:00
fundamentacao_proporcional: Artigo 40, § 1°, inciso III, segunda parte, da Constituição Federal, com redação dada pela Emenda Constitucional nº 103/2019, artigo 7º, § 2º e § 3º, da Emenda à Constituição Estadual nº 146/2021 e artigo 1º, inciso II, alínea "b", da Lei Complementar nº 51/1985.
visivel_dtc_proporcional: N
fundamentacao_integral: Artigo 40, § 1°, inciso III, segunda parte, da Constituição Federal, com redação dada pela Emenda Constitucional nº 103/2019, artigo 7º, § 2º e § 3º, da Emenda à Constituição Estadual nº 146/2021 e artigo 1º, inciso II, alínea "b", da Lei Complementar nº 51/1985.
visivel_dtc_integral: N
sexo: AMBOS
integral: S
tipo_calculo: Valor Médio
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ece-146-2021/art-7-par-2/original.md
  - /dispositivos/ece-146-2021/art-7-par-3/original.md
  - /dispositivos/lc-51-1985/art-1-inc-ii-al-b/lc-144-2014.md
disposicao_de_achados:
  - achado: /achados/achado-0020.md
    disposicao: corrigida
    justificativa: >-
      Corrigida pela renomeação do catálogo inteiro. Esta regra recebeu
      `nome` pelo padrão de facetas em ordem de anamnese — benefício, categoria
      especial, regime, e sexo quando gravado —, que é a resposta à questão 1 do
      achado ("qual padrão adotar"). A questão 4 dele — se a correção pertencia ao
      catálogo auditado da RFC 0004 em vez de a uma edição em `regra-*.md` — foi
      respondida pela coordenação em 2026-07-30: a auditoria está autorizada a alterar
      `nome`, e o registro está na Decisão 10 de
      `docs/analysis/decisoes-de-auditoria-2026-07-30.md`. Duas coisas que esta
      disposição **não** afirma: que o `P2_IGUALDADE_MATERIAL_ATIVA` sobre esta regra
      tenha sido tocado, se houver — `nome` está fora da chave material, e os sete
      grupos P2 do catálogo seguem idênticos, asseverados por teste; e que a
      padronização deva virar gate, que é a questão 2 do achado e segue aberta.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
  - achado: /achados/achado-0017.md
    disposicao: encaminhada
    justificativa: >-
      O defeito é real nesta regra e a conferência está fechada: as duas
      `FUNDAMENTACAO*` e o `dispositivos:` invocam a alínea "b" do art. 1º, II da
      LC 51/1985, que a lei reserva à mulher, enquanto a regra é `sexo: AMBOS`. O
      § 2º do art. 7º da ECE 146/2021 não fixa tempo de contribuição e manda
      buscá-lo naquela lei complementar, então, para o requerente homem, a única
      provisão que a regra invoca para o período adicional é a que não se aplica
      a ele.
      **Por que não é `corrigida`, ao contrário da `regra-0078`.** A Decisão 10
      de `docs/analysis/decisoes-de-auditoria-2026-07-30.md` autoriza a auditoria
      a alterar `FUNDAMENTACAO*`, mas autorização para reescrever não é
      conhecimento do que escrever. Na `regra-0078` o texto correto era
      determinado — regra de um sexo só, alínea daquele sexo. Aqui não é:
      acrescentar a alínea "a" pressupõe que a regra alcance os dois sexos pelo
      regime da LC 51/1985, e o que esta regra aplica depende do provimento
      judicial que lhe dá nome, que não foi localizado. O levantamento em
      `docs/analysis/fontes-do-mandado-de-injuncao-dos-agentes-penitenciarios.md`
      chega a um candidato provável — o MI nº 1.545/DF —, e o próprio documento
      registra que o vínculo permanece inferencial e que aquele provimento
      determina análise à luz do art. 57 da Lei 8.213/1991, sem mencionar a LC
      51/1985. Corrigir sob essa incerteza seria inventar citação.
      **Por que não é `nao_se_aplica`.** O defeito se materializa aqui, e é nesta
      regra que ele é mais grave: `simulavel: N`, logo a triagem é humana e a
      fundamentação é justamente o que a pessoa lê para decidir.
      Duas coisas que esta disposição **não** afirma: que o motor afira 25/15 em
      vez de 30/20 — tempo de contribuição e tempo de exercício policial não têm
      coluna, e esta regra sequer é simulável; e que o achado esteja fechado —
      ele segue aberto, e esta é a única regra da população que ainda carrega o
      defeito.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
    decisao_pendente_de: >-
      IPERON, como titular do produto: localizar o ato, parecer ou nota técnica
      que liga este cadastro ao provimento judicial que lhe dá nome. Sem ele não
      se sabe qual regime a regra aplica, e portanto nem qual citação a corrige.
---
