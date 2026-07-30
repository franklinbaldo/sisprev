---
type: Regra
id: regra-0078
row_index: 78
nome: Voluntária · Policial civil · ingresso até 13/11/2019, pedido a partir de 14/09/2021 · Masculino · integral · paridade · regra-0078
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
data_adm_ate: 13/11/2019 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 14/09/2021 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria especial de policial, com proventos integrais (cálculo por integralidade) e com paridade, com base no artigo 7º, § 3º da Emenda Constitucional Estadual nº 146/2021, artigo 1º, inciso II, alínea "a", da Lei Complementar nº 51/1985 e artigo 40, §1°, inciso III, segunda parte, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019 - regra transitória - idade + tempo de contribuição + homem.
visivel_dtc_integral: N
sexo: MASCULINO
integral: S
tipo_calculo: Remuneração de Contribuição
fundamentacao: Artigo 7º, §§1º e 3º da Emenda Constitucional Estadual nº 146/2021
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/ece-146-2021/art-7-par-1/original.md
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
      tenha sido tocado, se houver — `nome` está fora da chave material, e os sete
      grupos P2 do catálogo seguem idênticos, asseverados por teste; e que a
      padronização deva virar gate, que é a questão 2 do achado e segue aberta.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
  - achado: /achados/achado-0017.md
    disposicao: corrigida
    justificativa: >-
      Conferência fechada contra a fonte, e o defeito era real nesta regra: as
      duas alíneas do art. 1º, II da LC 51/1985 na redação da LC 144/2014 estão
      transcritas no bundle — a **"a"** exige 30 anos de contribuição e 20 de
      exercício policial, "se homem"; a **"b"**, 25 e 15, "se mulher" —, e esta
      regra é `sexo: MASCULINO` com `fundamentacao_integral` citando a "b" e
      terminando no descritor "mulher". O texto entregue invocava a provisão que
      a lei reserva ao outro sexo.
      **Corrigida no lugar.** O campo passou a citar a alínea "a" e o descritor
      "homem", com o texto que já estava escrito e conferido na unidade auditada
      `policial-civil-voluntaria-masculino`, e `dispositivos:` passou a apontar
      `lc-51-1985/art-1-inc-ii-al-a` em lugar da alínea "b". O relink é
      consequência, não decisão nova: a entrada afirma que a fundamentação
      **cita** aquela provisão, e depois da correção do texto a alínea "b" não
      era mais citada por esta regra. Até 2026-07-30 esta disposição era
      `encaminhada`, sob o argumento de que reescrever campo deployável não era
      da auditoria; a Decisão 10 de
      `docs/analysis/decisoes-de-auditoria-2026-07-30.md` autorizou a auditoria a
      alterar `FUNDAMENTACAO*`, e o encaminhamento perdeu o fundamento. O grupo
      `policial-civil-alinea-masculina` ficou sem objeto e foi desativado.
      Duas coisas que esta disposição **não** afirma: que o motor afira 25/15 em
      vez de 30/20 — tempo de contribuição e tempo de exercício policial não têm
      coluna, e nesta regra `simulavel: S` o motor não lê a fundamentação; e que
      o achado esteja fechado — ele segue aberto e alcança a `regra-0084`, cujo
      provimento não foi localizado.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
  - achado: /achados/achado-0010.md
    disposicao: corrigida
    justificativa: >-
      O mesmo defeito do `achado-0017` nesta regra, visto pelo lado mecânico: a
      detecção `P9_SEXO_FUNDAMENTACAO` acusava `sexo: MASCULINO` contra um
      `fundamentacao_integral` terminado em "mulher". A conferência que fecha um
      fecha o outro, e a correção foi o mesmo ato — o campo agora cita a alínea
      "a" e o descritor "homem".
      Disposto em entrada própria porque as populações não coincidem: o `0010`
      alcança só esta regra, e o `0017` alcança também a `regra-0084`; uma
      disposição só não responderia pelas duas leituras. A detecção **deixa de
      ser emitida** — o `achado-0010` tem população de uma regra só, e esta
      disposição `corrigida` é toda ela, então a expectativa de que a ocorrência
      mecânica suma é derivada daqui e não declarada no achado. O `0017` segue
      aberto pela regra que esta correção não alcança.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
---

# Estado da análise

Aposentadoria especial de policial civil pela regra de transição do art. 7º da
**ECE 146/2021**, com integralidade e paridade pelo § 3º, para quem ingressou
até 13/11/2019 e adquiriu o direito a partir de 14/09/2021. O tempo exigido não
está na emenda: o art. 40, § 1º, III da CF, na redação da EC 103/2019, remete à
lei complementar, e é a **LC 51/1985** que o fixa — por sexo, em duas alíneas.

**A conferência do fundamento está fechada, achou o defeito e ele foi
corrigido.** Esta regra é `sexo: MASCULINO` e citava a alínea feminina; passou a
citar a alínea "a", a masculina, e `dispositivos:` acompanhou. Está registrado
no [`achado-0017`](../achados/achado-0017.md), com a disposição no frontmatter.

- [x] Fundamento conferido contra a fonte transcrita — as duas alíneas do art.
  1º, II da LC 51/1985 (redação da LC 144/2014) estão no bundle, e a citada não
  era a do sexo declarado.
- [x] Defeito autorado como achado (`achado-0017`) e correção autorada como
  unidade (`policial-civil-voluntaria-masculino`), com a projeção conferida
  coluna a coluna contra esta regra.
- [x] Disposição do achado bloqueante registrada como `corrigida`, com o campo
  deployável e o vínculo de dispositivo alterados no lugar.
- [x] `achado-0010` também disposto — é o mesmo defeito pelo lado mecânico
  (`P9_SEXO_FUNDAMENTACAO`), e `revisada` exige resposta escrita para **cada**
  achado aberto que nomeie a regra, não só para o bloqueante.
- [x] **`nome` não colide mais com a `regra-0079`** (`P1_NOME_REPETIDO`): as
  duas se chamavam "Voluntária do Policial Civil - Art. 7º, § 3º da EC nº
  146/2021", sem que nada no nome dissesse qual sexo cada uma afere. A
  renomeação por facetas do [`achado-0020`](../achados/achado-0020.md) põe o
  sexo no nome das duas, e é ela que dissolve o grupo.
- [ ] **Vínculo critério → dispositivo não escrito.** `dispositivos:` registra
  as quatro provisões que a fundamentação cita, mas não qual funda qual
  critério. A idade mínima, o tempo de contribuição, o tempo de exercício
  policial e a integralidade vêm de provisões diferentes, e esse mapa é
  conferência humana em prosa — ainda não feita aqui.

Estes itens abertos são o que impede `revisada`, e é por isso que o
`status_auditoria` não subiu nesta rodada. O achado bloqueante já não é o
obstáculo: ele está disposto como `corrigida`, que libera `revisada` e
`validada`. O que falta é menos grave e mais chato — um mapa de fundamentação
que ninguém escreveu.

O `achado-0020` está disposto — a decisão dele era a de `nome` do catálogo
inteiro, tomada de uma vez e aplicada a todas as regras, e não uma conferência
por ficha. Os três achados que nomeiam esta regra têm resposta escrita; o que
resta para `revisada` é o item de conferência acima.
