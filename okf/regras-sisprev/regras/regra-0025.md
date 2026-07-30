---
type: Regra
id: regra-0025
row_index: 25
nome: Aposentadoria Compulsória - Redação EC 20/1998
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
data_adm_ate: 31/12/2003 00:00
data_adm_apos: 01/01/1910 00:00
data_direito_ate: 31/12/2003 00:00
data_direito_apos: 16/12/1998 00:00
fundamentacao_proporcional: Art 40, §1º, II, da CF com redação da EC 20/98
visivel_dtc_proporcional: N
fundamentacao_integral: ''
visivel_dtc_integral: N
sexo: ''
integral: ''
tipo_calculo: Não identificado
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-ii/ec-20-1998.md
  - /dispositivos/cf88/art-40-par-3/ec-20-1998.md
status_auditoria: revisada
auditado_por: franklinbaldo
auditado_em: 2026-07-30
disposicao_de_achados:
  - achado: /achados/achado-0008.md
    disposicao: nao_impede
    justificativa: >-
      Conferência fechada contra a fonte, e o que resta não é da auditoria. Os
      dois campos vazios são lapso com valor conferido — `sexo: AMBOS` (o
      dispositivo não distingue sexo e a sucessora sob o mesmo inciso II grava
      AMBOS) e `integral: N` ("proventos proporcionais", literal) —, e
      preenchê-los é alteração de campo deployável, decisão de quem responde
      pelo produto. O `tipo_calculo: "Não identificado"` foi conferido contra o
      art. 40, § 3º na redação da EC 20/1998, transcrito nesta rodada: a base é
      a totalidade da remuneração do cargo efetivo reduzida à proporção do
      tempo de contribuição, e nenhum rótulo do domínio expressa isso. O valor
      descreve corretamente o estado do catálogo; criar o rótulo que falta é
      alteração de enum, isto é, do Sisprev, fora do escopo desta auditoria.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
---

# Estado da análise

Aposentadoria compulsória sob a redação da **EC 20/1998** do art. 40, § 1º, II:
setenta anos de idade, proventos proporcionais ao tempo de contribuição, com
paridade. Janela de direito de 16/12/1998 — entrada em vigor da EC 20/1998 — a
31/12/2003, marco da EC 41/2003.

Conferida como **piloto da primeira travessia do gate P7**, e o resultado é que
ela **não atravessa** — por uma dependência que a conferência descobriu e que não
é decisão de terceiro. O registro do motivo é o produto principal desta seção.

## O que fecha

O critério aferido é o texto do dispositivo, verbatim: "compulsoriamente, aos
setenta anos de idade, com proventos proporcionais ao tempo de contribuição". Daí
decorrem duas conclusões sobre os campos vazios do
[`achado-0008`](../achados/achado-0008.md), e as duas são conferíveis:

- **`sexo` vazio é lapso, e o valor conferido é `AMBOS`.** O dispositivo não
  distingue sexo, e a sucessora imediata sob o **mesmo inciso II**
  (`regra-0027`, redação da EC 41/2003) grava `AMBOS`. As quatro regras
  pós-EC 41 da mesma família preenchem o campo; só as duas anteriores
  (`regra-0023` e esta) o deixam vazio, o que aponta lapso das linhas antigas e
  não significado.
- **`integral` vazio é lapso, e o valor conferido é `N`.** "Proventos
  proporcionais" é literal no dispositivo, e `regra-0027` grava `N`.

`paridade: S` é coerente com benefício de janela inteiramente anterior à EC
41/2003. `simulavel: N` e `apos_especial: N` conferem.

## O que não fecha, e por quê

`tipo_calculo: "Não identificado"` **não é conferível hoje**, e a razão é
estrutural: o § 1º da redação da EC 20/1998 manda calcular os proventos "a partir
dos valores fixados **na forma do § 3º**", e o **art. 40, § 3º não está
transcrito no bundle em nenhuma redação**. Sem ele não se sabe o que a lei
manda, logo não se pode dizer se "Não identificado" é lapso ou registro honesto
de indeterminação.

Isso **não** é decisão do dono do campo — é transcrição, que é trabalho da própria
auditoria. Dispor do `achado-0008` como `nao_impede` neste estado usaria a
justificativa para cobrir conferência não feita, que é exatamente a brecha que o
campo de justificativa existe para fechar.

A lacuna não é desta regra: as **13** regras com `tipo_calculo: "Não identificado"` são exatamente as 13 do `achado-0008`, e o art. 40, § 3º é citado
por outras **15** regras da fundamentação e transcrito por nenhuma. Transcrevê-lo
é pré-requisito da travessia de todas elas, não só desta.

- [x] Critério aferido conferido verbatim contra `cf88/art-40-par-1-inc-ii/ec-20-1998`: 70 anos, proventos proporcionais, sem distinção de sexo
- [x] Janela de direito conferida contra as vigências: `16/12/1998` é a entrada em vigor da EC 20/1998 e `31/12/2003` o marco da EC 41/2003, que encerra a redação citada (vigência até 30/12/2003)
- [x] `paridade: S`, `simulavel: N` e `apos_especial: N` conferidos
- [x] `dispositivos:` vinculado nesta conferência — a `fundamentacao_proporcional` cita o dispositivo e ele está transcrito; o campo estava vazio antes
- [x] `sexo` vazio diagnosticado como lapso, valor conferido `AMBOS` (dispositivo sem distinção + `regra-0027` sob o mesmo inciso)
- [x] `integral` vazio diagnosticado como lapso, valor conferido `N` ("proventos proporcionais", literal)
- [x] `tipo_calculo: "Não identificado"` conferido contra o § 3º, transcrito nesta rodada: a base é a totalidade da remuneração do cargo efetivo reduzida à proporção do tempo de contribuição, e **nenhum rótulo do domínio expressa isso**. O valor descreve corretamente o estado do catálogo; o que falta é rótulo, e criar rótulo é alteração do Sisprev, fora do escopo (`CLAUDE.md`)
- [x] `dispositivos:` acrescido de `cf88/art-40-par-3/ec-20-1998`, que a `fundamentacao_proporcional` alcança pela remissão do § 1º e que passou a existir nesta rodada
