---
type: Regra
id: regra-0109
row_index: 109
id_sisprev: '159'
nome_original: Voluntária Policial Civil - Art. 1º, II, "a" da LC nº. 51/85 c/c LC nº. 144/14, c/c art. 4º da EC nº 146/2021
nome: Voluntária · Policial civil · ingresso após 31/12/2003 e até 31/12/2024, requisitos antes de 31/12/2024 · Masculino · proporcional · média
tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 4º
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
data_adm_ate: 31/12/2024 00:00
data_adm_apos: 31/12/2003 00:00
data_direito_ate: 31/12/2024 00:00
data_direito_apos: 01/01/1910 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria especial de policial, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 7º, §§ 2º e 3º da Emenda Constitucional Estadual nº 146/2021, artigo 1º, inciso II, alínea "b", da Lei Complementar nº 51/1985 e artigo 40, §1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019 - regra transitória mulher - idade + tempo + pedágio | Aposentadoria especial de policial, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 7º, §§ 2º e 3º da Emenda Constitucional Estadual nº 146/2021, artigo 1º, inciso II, alínea "a", da Lei Complementar nº 51/1985 e artigo 40, §1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019 - regra transitória de homem - idade + tempo + pedágio
visivel_dtc_integral: N
sexo: MASCULINO
integral: N
tipo_calculo: Valor Médio
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ece-146-2021/art-7-par-2/original.md
  - /dispositivos/ece-146-2021/art-7-par-3/original.md
  - /dispositivos/lc-51-1985/art-1-inc-ii-al-a/lc-144-2014.md
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
      tenha sido tocado, se houver — `nome` está fora da chave material, então
      renomear é incapaz de criar ou dissolver grupo de igualdade material, e o
      baseline de `tests/test_achados_bundle.py` assevera isso; e que a
      padronização deva virar gate, que é a questão 2 do achado e segue aberta.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
  - achado: /achados/achado-0058.md
    disposicao: encaminhada
    justificativa: >-
      A divergência entre os campos de cálculo e o dispositivo citado é fato do
      catálogo e está conferida: esta regra vincula o § 3º do art. 7º da ECE
      146/2021, que manda pagar a totalidade da remuneração no cargo efetivo com
      reajuste vinculado ao servidor em atividade, e grava `paridade: N`,
      `integral: N` e `tipo_calculo: Valor Médio` — nenhuma das duas coisas que o
      parágrafo determina. Das treze regras que vinculam esse parágrafo, dez
      gravam `paridade: S` com `Remuneração de Contribuição`.
      **Por que não é `corrigida`.** Há duas correções opostas e o catálogo não
      contém o fato que decide entre elas. O § 3º exclui quem fez a opção do § 16
      do art. 40 da CF — a adesão à previdência complementar —, e se esta regra
      for a do servidor optante os valores gravados descrevem o cálculo
      corretamente e o defeito é de citação, não de parametrização. Não há coluna
      de adesão à previdência complementar no cadastro, então a hipótese não se
      confirma nem se afasta daqui. Editar os campos de cálculo sob essa
      incerteza mudaria o valor do benefício com base numa leitura não
      verificada, que é o modo de falha da RFC 0008 — e neste caso sobre a coluna
      que mais pesa.
      **Por que não é `nao_se_aplica`.** O defeito se materializa aqui de um jeito
      ou de outro: ou os campos de cálculo contradizem o dispositivo, ou o
      dispositivo citado é o que exclui esta regra. As duas leituras deixam algo
      errado no documento; nenhuma delas absolve.
      Esta disposição **não** afirma qual lado corrigir, nem que alguma concessão
      tenha saído a menor — depende de caso concreto, que o catálogo não
      registra.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
    decisao_pendente_de: >-
      IPERON, como titular do produto: se esta regra é a do servidor que fez a
      opção do § 16 do art. 40 da CF. A resposta decide se o que se corrige são
      os campos de cálculo ou o vínculo de dispositivo, e ela não está no
      catálogo — não há coluna que registre a adesão à previdência complementar.
---
