---
type: Regra
id: regra-0039
row_index: 39
nome: Voluntária · Magistério · ingresso após 31/12/2003, pedido a partir de 18/10/2021 · Masculino · proporcional · média
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
data_adm_ate: 31/12/2099 00:00
data_adm_apos: 31/12/2003 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 18/10/2021 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria especial de professor, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 40, §1º, inciso III, alínea “a” e §5º, da Constituição Federal, com redação dada pela Emenda Constitucional nº 20/1998, quanto ao preenchimento dos requisitos de aposentadoria; artigo 40, §§ 3º e 8º com redação dada pela Emenda Constitucional nº 41/2003, no que tange à fórmula de cálculo e reajuste; artigos 24, 45 e 62 da Lei Complementar Estadual nº 432/2008, e no artigo 4º da Emenda Constitucional Estadual nº 146/2021.
visivel_dtc_integral: N
sexo: MASCULINO
integral: N
tipo_calculo: Valor Médio
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii-al-a/ec-20-1998.md
  - /dispositivos/cf88/art-40-par-5/ec-20-1998.md
  - /dispositivos/ece-146-2021/art-4/original.md
  - /dispositivos/lce-432-2008/art-24/original.md
  - /dispositivos/lce-432-2008/art-45/lce-672-2012.md
  - /dispositivos/lce-432-2008/art-62/original.md
disposicao_de_achados:
  - achado: /achados/achado-0051.md
    disposicao: encaminhada
    justificativa: >-
      O defeito é real nesta regra e a conferência está fechada contra as fontes
      transcritas. `fundamentacao_integral` atribui **expressamente** à redação da
      EC 20/1998 do art. 40, § 1º, III, "a" e do § 5º da CF "o preenchimento dos
      requisitos de aposentadoria", e `dispositivos:` vincula as duas. Aquelas
      redações deixaram de vigorar em **30/12/2003**, e esta regra grava
      `data_adm_apos: 31/12/2003` — a população que ela descreve começa no dia
      seguinte ao último dia de vigência do fundamento que ela invoca.
      As duas defesas disponíveis foram testadas no achado e não sustentam. O art.
      4º da ECE 146/2021, que a regra cita e vincula, congela "a legislação
      vigente até a data de entrada em vigor desta Emenda Constitucional" — em
      2021 —, e cláusula que preserva o que está em vigor não ressuscita o que não
      estava havia dezoito anos. Direito adquirido também não alcança: a própria
      janela de admissão exclui quem poderia ter reunido requisitos sob aquela
      redação.
      **Por que não é `corrigida`.** A Decisão 10 de
      `docs/analysis/decisoes-de-auditoria-2026-07-30.md` autoriza a auditoria a
      alterar `FUNDAMENTACAO*`, mas há três candidatas à redação pretendida e
      nenhuma verificada — a da EC 41/2003, que é a vizinha imediata e a mais
      econômica; a da EC 103/2019, que era a vigente em 2021 mas **não tem
      alíneas**, de modo que a alínea "a" citada não existiria nela; ou o art. 24
      da LCE 432/2008, já citado no mesmo campo. Pior: a escolha **não é
      indiferente à janela**. Se a redação certa for a da EC 41/2003, ela se
      extinguiu em 12/11/2019, antes de a janela desta regra abrir em 18/10/2021,
      e a regra recai no `achado-0022`; se for o art. 24 da LCE 432/2008, aquele
      artigo deixou de vigorar em 18/10/2021, o primeiro dia da janela. Corrigir o
      fundamento sem decidir a janela produziria uma regra formalmente arrumada e
      materialmente sem base — e a aparência de conferência é pior que o estado
      atual, porque quem lê depois não desconfia.
      **Por que não é `nao_se_aplica`.** `fundamentacao_integral` é entregue no
      ato de concessão, e o professor recebe como fundamento dos seus requisitos
      texto constitucional que não vigia nem quando ele ingressou nem quando
      adquiriu o direito. É vício de motivação, não anotação de auditoria.
      Esta disposição **não** afirma qual redação a regra pretendia invocar, nem
      que as duas regras devam deixar de existir — a questão 3 do achado registra
      que a hipótese de lacuna, caso fossem revogadas, não está estabelecida nem
      afastada, porque as janelas das regras do art. 33 da LCE 1.100/2021 que as
      cobririam são sentinelas, e ler sentinela como "sem limite" é interpretá-la.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
    decisao_pendente_de: >-
      IPERON, como titular do produto, decidindo **em conjunto** o fundamento e a
      janela: qual redação o eixo dos requisitos pretendia invocar, e qual passa a
      ser o fecho de `data_direito_ate` à luz dela. O `achado-0022` e o
      `achado-0051` não se decidem em separado — cada saída do primeiro muda a
      resposta do segundo —, e a questão 3 acrescenta a decisão sobre a
      convivência com `regra-0107`/`regra-0108`, que têm o defeito de janela
      espelhado (`achado-0052`).
---

# Estado da análise

Conferida contra a transcrição pesquisável da ECE 146/2021, na
[conferência da janela do art. 4º](../../../docs/analysis/conferencia-janela-art-4-ece-146.md) — que cobre as 24 regras que
vinculam esse dispositivo e é onde o raciocínio completo está.

Os requisitos desta regra vêm de art. 40, § 1º, III, "a" e § 5º, da CF na redação da EC 20/1998 — legislação **anterior** à ECE
146/2021. O art. 4º dessa emenda, que a regra invoca, é justamente o que
preserva aquela legislação, e preserva **com prazo**: os requisitos precisam
estar cumpridos até 31/12/2024. Sob a semântica que a Q1 fechou
(`DATA_DIREITO_ATE` é o prazo de implementação dos requisitos), a janela
deveria fechar em `31/12/2024`, e está gravada `31/12/2099`.

O `data_direito_apos: 18/10/2021` reforça a leitura: é a entrada em vigor da
ECE 146/2021, ou seja, o começo exato do período que o art. 4º garante. A
janela desta regra é esse período — e ele termina em 31/12/2024.

É o caso mais explícito do grupo: a própria fundamentação separa os eixos — cita a EC 20/1998 "quanto ao preenchimento dos requisitos" e a EC 41/2003 "no que tange à fórmula de cálculo e reajuste". Requisitos por norma anterior à EC 146, com o art. 4º invocado.

- [x] Fundamento dos requisitos identificado e conferido contra a transcrição oficial da ECE 146/2021
- [x] Art. 4º lido verbatim: o "sendo assegurada a qualquer tempo" é do momento da concessão, não do implemento dos requisitos
- [ ] `data_direito_ate: 31/12/2099` deveria ser `31/12/2024` — correção proposta em [`achado-0022`](../achados/achado-0022.md), não aplicada: é campo deployável
