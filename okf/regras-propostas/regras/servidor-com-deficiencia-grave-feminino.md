---
type: RegraProposta
id: servidor-com-deficiencia-grave-feminino
ciclo: ciclo-05
schema_version: 1
estado_auditoria: elaboracao
origens_legacy:
  - regra-0061
predicados:
  sexo: feminino
  regime: lce-1100-2021
requisitos_verificacao_humana:
  - predicado: o servidor tem deficiência de grau grave e conta 20 anos de tempo de contribuição, se mulher
    protocolo_verificacao:
      pergunta: A deficiência do servidor é de grau grave, e o tempo de contribuição alcança 20 anos?
      responsavel: equipe multiprofissional e interdisciplinar designada pelo IPERON
      meio_de_prova: avaliação biopsicossocial somada à contagem de tempo de contribuição
      momento: ato de concessão, previamente a ele
      evidencia_exigida: laudo da avaliação biopsicossocial atestando o grau grave e certidão de tempo de contribuição
    portador_primario: fundamentacao_integral
taxonomias:
  - ref: /dispositivos/lce-1100-2021/art-35/original.md
    papel: grau de deficiência e tempo de contribuição exigido — inciso I, 20 anos se mulher; caput exige avaliação biopsicossocial prévia, 10 anos de serviço público e 5 no cargo
  - ref: /dispositivos/lce-1100-2021/art-25/original.md
    papel: base de cálculo dos proventos
  - ref: /dispositivos/lce-1100-2021/art-27-inc-i/original.md
    papel: critério de reajuste
  - ref: /dispositivos/cf88/art-40-par-4a/ec-103-2019.md
    papel: autoriza requisitos diferenciados para servidor com deficiência
  - ref: /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
    papel: competência e remissão à lei complementar do ente
projecao:
  nome: Aposentadoria Voluntária de Servidor com Deficiência GRAVE (MULHER) - Art. 35, inciso I, da Lei Complementar Estadual nº 1.100/2021
  fundamentacao_integral: Aposentadoria voluntária de servidor público com deficiência grave, com proventos integrais (cálculo por integralidade) e com paridade. O direito exige, cumulativamente, 20 anos de tempo de contribuição — prazo que o artigo 35, inciso I, da Lei Complementar Estadual nº 1.100/2021 fixa para a deficiência grave, se mulher —, além do tempo mínimo de 10 anos de efetivo exercício no serviço público e 5 anos no cargo efetivo em que se dará a aposentadoria, exigidos pelo caput do mesmo artigo. O grau de deficiência é apurado em avaliação biopsicossocial realizada por equipe multiprofissional e interdisciplinar, prévia à concessão, na forma do caput do artigo 35 e do artigo 36 da mesma Lei Complementar. A base de cálculo dos proventos é a do artigo 25 e o reajuste o do artigo 27, inciso I, ambos da Lei Complementar Estadual nº 1.100/2021. A competência e a remissão à lei complementar do ente vêm do artigo 40, § 4º-A, e do artigo 40, § 1º, inciso III, segunda parte, da Constituição Federal, com redação dada pela Emenda Constitucional nº 103/2019.
proveniencia:
  fontes_consultadas:
    - https://ditel.casacivil.ro.gov.br/cotel/Livros/Files/LC1100%20-%20COMPILA%C3%87%C3%83O.pdf
    - /dispositivos/lce-1100-2021/art-35/original.md
  notas: Os incisos do art. 35 foram transcritos ao corpus em 2026-07-29; antes disso o documento trazia só o caput, e o grau não era conferível no repositório.
decisoes:
  - data: '2026-07-29'
    quem: franklinbaldo
    o_que: Levar o grau de deficiência para a fundamentação, que é campo material do P2, e explicitá-lo também no nome. Sem alterar a regra de origem.
  - data: '2026-07-30'
    quem: franklinbaldo
    o_que: >-
      Registrar a unidade de atomicidade desta proposta (RFC 0004, round 11;
      okf/spec/regraproposta.md, “Atomicidade é derivada, não declarada”):
      seis origens (regra-0059 a regra-0064), seis destinos, 1:1 cada, mas as
      seis unidades só fazem sentido juntas. O que cada uma acrescenta é a
      identificação do seu grau (leve/moderado/grave) na fundamentação, e é a
      existência das outras cinco que torna a distinção informativa: ativar só
      a “grave” deixaria as outras quatro no estado atual, em que moderada e
      leve continuam materialmente idênticas, trocando dois grupos
      P2_IGUALDADE_MATERIAL_ATIVA por um sem resolver nada. As seis irmãs são:
      servidor-com-deficiencia-{moderada,grave,leve}-{feminino,masculino}.
      Antes registrado no Conjunto proposta-auditoria-2026-07 (retirado).
confianca: alta
---

# O que esta unidade propõe

A `regra-0061` é a aposentadoria de servidor com deficiência de grau
**grave**, sexo feminino. Hoje o grau aparece **só no `nome`** — as
seis regras do grupo (`0059`–`0064`, três graus × dois sexos) partilham uma
`fundamentacao_integral` idêntica, que cita "artigos 25, 27, I; 35" sem nomear o
inciso de cada uma.

Esta unidade grava o grau nos dois lugares que o catálogo tem para isso: na
**fundamentação**, que é campo material do `P2_IGUALDADE_MATERIAL_ATIVA`, e no
**nome**, que é o rótulo que o operador lê. São dois atos e nenhum substitui o
outro — diferenciar só o nome limparia o `P1_NOME_REPETIDO` e deixaria o P2
intacto.

# A fundamentação como articulação, não como lista

A fundamentação projetada não enumera normas: diz **como cada dispositivo se
aplica** e **o que é aferido**. Para esta unidade, o art. 35, inciso I
fixa 20 anos de tempo de contribuição para a deficiência grave, se
mulher; o *caput* do mesmo artigo exige a avaliação biopsicossocial prévia, 10
anos de serviço público e 5 no cargo; o art. 25 dá a base de cálculo e o art. 27,
I o reajuste; e a competência vem do art. 40, § 4º-A da CF.

O `requisitos_verificacao_humana` registra o protocolo de aferição — quem
verifica, por qual meio, em que momento e com qual evidência. O template
`gerar_fundamentacao_projetada` monta texto a partir dele **sem nunca afirmar a
constatação de um caso concreto**: aponta a verificação institucional, não o
resultado dela.

# O que esta unidade não faz

- **Não altera a `regra-0061`.** `estado_proposta: elaboracao` — nada compila,
  nada é exportado, e a exportação operacional segue 100% do bundle legado.
- **Não toca o campo `fundamentacao`** (o terceiro, distinto dos dois
  `fundamentacao_*`). Em `regra-0061` e `regra-0062` ele contém a citação de um
  parágrafo único do art. 39 da LCE 432/2008 que não existe — defeito próprio,
  registrado no [`achado-0021`](../../regras-sisprev/achados/achado-0021.md), e
  que precisa ser decidido separadamente.
- **Não afirma o que o motor faz.** O grau não tem coluna; o motor não o afere.
  A projeção o torna legível e material, não computável.
- **Não propõe promoção de estado.** Passar a `preview` ou `deployable` é
  decisão institucional.
