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
    disposicao: encaminhada
    decisao_pendente_de: IPERON, como titular do produto Sisprev
    justificativa: >-
      Conferência fechada contra a fonte, e o que resta não é da auditoria.
      **São duas decisões distintas, e as duas pertencem ao IPERON por títulos
      diferentes** — daí um único `decisao_pendente_de` nomeá-lo como titular
      do produto, e não como dono de um campo. (1) **Preenchimento de campo
      deployável**: os dois campos vazios são lapso com valor conferido —
      `sexo: AMBOS` (o dispositivo não distingue sexo e a sucessora sob o mesmo
      inciso II grava AMBOS) e `integral: N` ("proventos proporcionais",
      literal) —, e gravá-los é decisão de quem responde pelo produto, dentro
      dos domínios que já existem. (2) **Lacuna do domínio de
      `tipo_calculo`**: o valor `"Não identificado"` foi conferido contra o
      art. 40, § 3º na redação da EC 20/1998, transcrito nesta rodada — a base
      é a totalidade da remuneração do cargo efetivo reduzida à proporção do
      tempo de contribuição, e nenhum rótulo do domínio expressa isso. O valor
      descreve corretamente o estado do catálogo; criar o rótulo que falta é
      alteração de enum, isto é, **do sistema**, e não parametrização — fora do
      escopo desta auditoria por natureza, não por conveniência. A acusação
      sobre essa lacuna ainda não foi autorada como achado: pendência
      preservada de propósito.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
---

# Estado da análise

Aposentadoria compulsória sob a redação da **EC 20/1998** do art. 40, § 1º, II:
setenta anos de idade, proventos proporcionais ao tempo de contribuição, com
paridade. Janela de direito de 16/12/1998 — entrada em vigor da EC 20/1998 — a
31/12/2003, marco da EC 41/2003.

**Conferência concluída.** Os critérios aferidos foram lidos verbatim contra os
dispositivos, que estão transcritos no bundle; o que resta não é conferência
pendente, é **decisão de quem responde pelo produto** — dois campos a preencher e
um rótulo de enum que não existe. Está registrado abaixo campo por campo e
disposto no [`achado-0008`](../achados/achado-0008.md) no frontmatter.

Esta foi a regra-piloto da primeira travessia do gate P7. O percurso da
descoberta — a rodada em que ela **não** atravessava, porque o art. 40, § 3º não
estava transcrito — está no log do repositório e na PR que o transcreveu; esta
seção descreve o estado atual, não o histórico.

## O que fecha

O critério aferido é o texto do dispositivo, verbatim: "compulsoriamente, aos
setenta anos de idade, com proventos proporcionais ao tempo de contribuição". Daí
decorrem duas conclusões sobre os campos vazios do `achado-0008`, e as duas são
conferíveis:

- **`sexo` vazio é lapso, e o valor conferido é `AMBOS`.** O dispositivo não
  distingue sexo, e a sucessora imediata sob o **mesmo inciso II**
  (`regra-0027`, redação da EC 41/2003) grava `AMBOS`. As quatro regras
  pós-EC 41 da mesma família preenchem o campo; só as duas anteriores
  (`regra-0023` e esta) o deixam vazio, o que aponta lapso das linhas antigas e
  não significado.
- **`integral` vazio é lapso, e o valor conferido é `N`.** "Proventos
  proporcionais" é literal no dispositivo, e `regra-0027` grava `N`.

`simulavel: N` e `apos_especial: N` conferem.

## A fórmula está conferida, e o que falta é rótulo

O § 1º manda calcular os proventos "a partir dos valores fixados **na forma do
§ 3º**", e o § 3º na redação da EC 20/1998 está transcrito
([`cf88/art-40-par-3/ec-20-1998`](../../dispositivos/cf88/art-40-par-3/ec-20-1998.md)):
a base é a **totalidade da remuneração do cargo efetivo**, e o inciso II a reduz à
**proporção do tempo de contribuição**. O denominador dessa proporção é o tempo
exigido para a voluntária integral — 35 anos se homem, 30 se mulher, art. 40,
§ 1º, III, "a" da mesma redação.

Nenhum rótulo do domínio do `tipo_calculo` expressa essa combinação: `Valor Efetivo` é a base sem a proporção, `Proporcionalidade Dias` é a proporção sem
dizer sobre que base, `Valor Médio` é a base da redação **seguinte**. Então
`tipo_calculo: "Não identificado"` **descreve corretamente o estado do
catálogo**, e o que falta é rótulo — criar rótulo é alteração de enum, isto é, do
Sisprev, fora do escopo desta auditoria (`CLAUDE.md`). A fórmula em si está
autorada em
[`forma-calculo-totalidade-proporcional-tempo`](../../formas-calculo/forma-calculo-totalidade-proporcional-tempo.md),
com um parâmetro aberto (a conversão dos anos constitucionais em dias).

A dependência de sexo é do **cálculo**, não do critério: a compulsória incide
sobre ambos os sexos aos setenta anos, e é por isso que `sexo: AMBOS` continua
sendo o valor conferido apesar de o denominador variar.

## `paridade: S` está conferida, e nenhum campo da regra a funda

A paridade decorre do **art. 40, § 8º na redação da EC 20/1998**, transcrito
nesta rodada
([`cf88/art-40-par-8/ec-20-1998`](../../dispositivos/cf88/art-40-par-8/ec-20-1998.md)):
proventos e pensões "revistos na mesma proporção e na mesma data, sempre que se
modificar a remuneração dos servidores em atividade". É esse dispositivo que
sustenta `paridade: S` — não a mera anterioridade da janela à EC 41/2003, que é
consequência e não fundamento.

O dispositivo **não entra em `dispositivos:`**, e a razão é o que aquele campo
afirma: que a fundamentação *da regra* cita a provisão
([`docs/spec/dispositivo.md`](../../../docs/spec/dispositivo.md)). A
`fundamentacao_proporcional` desta regra cita só o art. 40, § 1º, II — o § 3º
entra por remissão expressa do texto citado ("na forma do § 3º"), o § 8º não é
citado em campo nenhum, e as duas outras fundamentações estão vazias. Registrado
como conferência: `paridade: S` é **materialmente correta e formalmente
desacompanhada** no produto entregue.

- [x] Critério aferido conferido verbatim contra `cf88/art-40-par-1-inc-ii/ec-20-1998`: 70 anos, proventos proporcionais, sem distinção de sexo
- [x] Janela de direito conferida contra as vigências: `16/12/1998` é a entrada em vigor da EC 20/1998 e `31/12/2003` o marco da EC 41/2003, que encerra a redação citada (vigência até 30/12/2003)
- [x] `simulavel: N` e `apos_especial: N` conferidos
- [x] `paridade: S` conferida contra `cf88/art-40-par-8/ec-20-1998` (revisão na mesma proporção e data), transcrito para esta conferência — e registrado que nenhuma fundamentação da regra cita esse dispositivo, razão por que ele não entra em `dispositivos:`
- [x] `dispositivos:` vinculado nesta conferência — a `fundamentacao_proporcional` cita `cf88/art-40-par-1-inc-ii/ec-20-1998`, e o `cf88/art-40-par-3/ec-20-1998` entra pela remissão expressa do § 1º ("na forma do § 3º"); o campo estava vazio antes
- [x] `sexo` vazio diagnosticado como lapso, valor conferido `AMBOS` (dispositivo sem distinção + `regra-0027` sob o mesmo inciso)
- [x] `integral` vazio diagnosticado como lapso, valor conferido `N` ("proventos proporcionais", literal)
- [x] `tipo_calculo: "Não identificado"` conferido contra o § 3º: a base é a totalidade da remuneração do cargo efetivo reduzida à proporção do tempo de contribuição, e **nenhum rótulo do domínio expressa isso**. O valor descreve corretamente o estado do catálogo; o que falta é rótulo, e criar rótulo é alteração do Sisprev, fora do escopo (`CLAUDE.md`)
- [x] Denominador da proporção conferido contra `cf88/art-40-par-1-inc-iii-al-a/ec-20-1998`: 35 anos de contribuição se homem, 30 se mulher — parâmetro constitucional, sem norma estadual conferida a alterá-lo. Vinculado ao ajuste na forma de cálculo, onde o vínculo é por componente
