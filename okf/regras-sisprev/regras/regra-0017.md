---
type: Regra
id: regra-0017
row_index: 17
id_sisprev: '66'
nome_original: Pensão por Morte - Art. 46 da Lei Complementar 1.100/2021 - Paridade
nome: Pensão · óbito a partir de 01/01/2024, ingresso até 31/12/2003 · Feminino · proporcional · Tipo Cálculo Nova Previdência Pensão por morte · paridade
tipo_de_beneficio: PENSÃO POR MORTE
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 1º
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
data_adm_ate: 31/12/2003 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 01/01/2024 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Pensão mensal, com fundamento nos artigos 27, inciso I; 46, inciso I; 47, inciso I e II; 49; 50; 51, inciso I, II, III e VIII, alínea "c", todos da Lei Complementar Estadual nº 1.100/2021 e artigo 40, § 7º, da Constituição Federal, com redação dada pela Emenda Constitucional nº 103/2019 - pensão vitalícia e temporária
visivel_dtc_integral: N
sexo: AMBOS
integral: N
tipo_calculo: Tipo Cálculo Nova Previdência Pensão por morte
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-7/ec-103-2019.md
  - /dispositivos/lce-1100-2021/art-27-inc-i/original.md
  - /dispositivos/lce-1100-2021/art-46-inc-i/original.md
  - /dispositivos/lce-1100-2021/art-47-inc-i/original.md
  - /dispositivos/lce-1100-2021/art-47-inc-ii/original.md
  - /dispositivos/lce-1100-2021/art-49/original.md
  - /dispositivos/lce-1100-2021/art-50/original.md
  - /dispositivos/lce-1100-2021/art-51-inc-i/original.md
  - /dispositivos/lce-1100-2021/art-51-inc-ii/original.md
  - /dispositivos/lce-1100-2021/art-51-inc-iii/original.md
  - /dispositivos/lce-1100-2021/art-51-inc-viii-al-c/original.md
disposicao_de_achados:
  - achado: /achados/achado-0056.md
    disposicao: corrigida
    justificativa: >-
      **Corrigida em 2026-08-13, revendo a disposição de 2026-07-30.**
      Conferência fechada contra as fontes transcritas: os onze dispositivos
      que esta regra cita são os mesmos da `regra-0016` e da `regra-0018`,
      item a item, e nenhum deles diferencia por sexo — a única menção, no
      art. 51, II da LCE 1.100/2021, é cláusula equalizadora ("de ambos os
      sexos"), e trata do dependente, não do instituidor. `sexo: FEMININO`
      era, portanto, um critério de aferição que a articulação normativa
      citada por esta própria regra não sustentava.
      A disposição de 2026-07-30 tratava isso por revogação, descartando
      expressamente a alternativa de gravar `AMBOS` — a leitura era que
      corrigir `sexo` na regra legada alteraria a chave material do P2 como
      efeito colateral de uma edição cujo propósito era outro. Revisão em PR
      #151 (2026-08-13): como nenhum dispositivo sustenta a distinção,
      corrigir `sexo` para `AMBOS` **é** o propósito da edição, não efeito
      colateral — o mesmo raciocínio que já autoriza a auditoria a corrigir
      `nome`/`FUNDAMENTACAO*` in loco quando o campo antigo é o que o
      dispositivo citado não sustenta. `sexo` passou a `AMBOS`, e `nome`
      deixou de carregar a faceta de sexo — igual ao que já valia para
      `regra-0018`.
      **O que esta disposição não desfaz**: o bloco `revogada` (abaixo)
      permanece. A correção de `sexo` torna as três regras materialmente
      idênticas (mesmo `nome`, mesma fundamentação, mesmos dispositivos,
      agora também mesmo `sexo`) — um grupo `P2_IGUALDADE_MATERIAL_ATIVA` de
      fato, não só um nome compartilhado — e a consolidação já decidida
      (revogar `regra-0016`/`regra-0017`, manter `regra-0018`) segue sendo o
      desfecho correto sob essa leitura, ainda pendente do ato de
      `status_regra` que cabe ao IPERON (P2.1).
    decidido_por: franklinbaldo
    decidido_em: 2026-08-13
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
revogada:
  decidido_por: franklinbaldo
  decidido_em: 2026-07-30
  justificativa: >-
    Mesmo desdobramento indevido por sexo de regra-0016, mesma fundamentação
    (achado-0056). regra-0018 permanece ativa. **Atualização de 2026-08-13**:
    `sexo` foi corrigido para `AMBOS` nesta regra (ver `disposicao_de_achados`
    do `achado-0056` acima); a revogação segue de pé, agora fundada em
    `regra-0016`/`regra-0017`/`regra-0018` serem materialmente idênticas, não
    em `sexo` sem lastro.
  fonte: /okf/regras-sisprev/achados/achado-0056.md
---

# Estado da análise

Pensão por morte sob o **art. 46 da LCE 1.100/2021 com paridade** (`paridade: S`),
no regime de cotas: cota familiar de cinquenta por cento mais dez por cento por
dependente, sobre a remuneração ou proventos do instituidor. A regra é
`simulavel: N`, então a seleção depende de triagem humana pela fundamentação.

**Corrigido em 2026-08-13: `sexo` passou de `FEMININO` para `AMBOS`.**
Nenhum dos onze dispositivos citados diferencia por sexo (`achado-0056`), e a
única menção — cláusula equalizadora do art. 51, II — trata do dependente,
não do instituidor. `regra-0016` recebeu a mesma correção (`MASCULINO` →
`AMBOS`); `regra-0018` já gravava `AMBOS`. As três agora carregam o **mesmo
`nome`** (sem faceta de sexo, coerente com a Decisão 11 de
`docs/analysis/decisoes-de-auditoria-2026-07-30.md`) **e a mesma
fundamentação, os mesmos dispositivos e o mesmo `sexo`** — materialmente
idênticas. A questão sobre a que pessoa o campo `sexo` se referia
(beneficiário ou instituidor) deixa de importar: com as três em `AMBOS`, não
há mais valor divergente a atribuir a ninguém. O grupo segue como
`P2_IGUALDADE_MATERIAL_ATIVA` de três candidatas idênticas, e o desfecho já
decidido — revogar esta regra e a `regra-0016`, manter a `regra-0018` — é
quem resolve o grupo; ver bloco `revogada` acima.

**`data_direito_apos: 01/01/2024` não tem fundamento conferido**, como nas outras
regras do art. 46.

Verificação humana que o cadastro não expressa: exame da portaria de aposentadoria
do instituidor comprovando a manutenção da paridade; validação da relação de
dependência previdenciária e do enquadramento do requerente; e apuração do número
de dependentes para a cota familiar, com a tabela de duração do benefício.
Documentos correspondentes: certidão de óbito, ato formal de concessão da
aposentadoria do instituidor com paridade, identidade civil do beneficiário e
prova de vínculo.

- [x] `paridade: S` é coerente com a hipótese de instituidor já aposentado com paridade, que é o que a fundamentação descreve
- [x] `sexo: AMBOS` corrigido — nenhum dispositivo citado diferencia por sexo (achado-0056); a referência antiga a `FEMININO` não tinha lastro
- [x] `nome` idêntico ao das irmãs (`regra-0016`, `regra-0018`), sem faceta de sexo — correto: nenhum critério aferido as distingue, e a igualdade material é o que resta ao grupo `P2` resolver via revogação
- [ ] `data_direito_apos: 01/01/2024` não tem fundamento conferido perante a LCE 1.100/2021
- [ ] Os dispositivos declarados não foram conferidos um a um contra os campos de fundamentação
- [ ] O programa de verificação manual acima está enumerado, não conferido contra dispositivo transcrito
