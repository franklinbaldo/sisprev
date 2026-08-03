---
type: UnidadeAuditada
id: incapacidade-lce1100-apos-2003-causa-comum
schema_version: 1
estado_unidade: elaboracao
origens_legacy:
  - regra-0021
predicados:
  causa_incapacidade: causa_comum
  regime: lce1100-incapacidade-ingresso-apos-2003
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente não decorre de acidente em serviço, moléstia
      profissional nem doença grave catalogada
    protocolo_verificacao:
      pergunta: >-
        Há prova suficiente para excluir as classes qualificadas e enquadrar o
        caso no ramo residual proporcional?
      responsavel: junta médica oficial e instrução previdenciária do IPERON
      meio_de_prova: >-
        laudo médico oficial, prontuários, histórico ocupacional, apuração de
        eventual acidente e rol legal vigente
      momento: instrução e seleção da regra
      evidencia_exigida: >-
        incapacidade permanente comprovada e investigação suficiente das causas
        qualificadas; silêncio ou prova insuficiente não bastam
    portador_primario: fundamentacao_proporcional
aplicabilidade_temporal:
  datas_legadas:
    data_adm_apos: 01/01/2004 00:00
    data_direito_apos: 18/10/2021 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-i/ec-103-2019.md
    papel: funda a aposentadoria por incapacidade permanente
  - ref: /dispositivos/lce-1100-2021/art-30-caput/original.md
    papel: determina o ramo residual proporcional
  - ref: /dispositivos/lce-1100-2021/art-30-par-14/original.md
    papel: remete a causa comum à fórmula proporcional do art. 26
  - ref: /dispositivos/lce-1100-2021/art-26/original.md
    papel: aplica fração em dias sobre a média do art. 24
  - ref: /dispositivos/lce-1100-2021/art-24/original.md
    papel: disciplina a base média da proporcionalização
  - ref: /dispositivos/lce-1100-2021/art-27-inc-ii/original.md
    papel: determina reajuste sem paridade para ingresso após 31/12/2003
projecao:
  nome: >-
    Incapacidade permanente · LCE 1.100 · ingresso após 2003 · demais causas ·
    média proporcional · sem paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: N
  sexo: AMBOS
  integral: N
  tipo_calculo: Não identificado
proveniencia:
  fontes_consultadas:
    - /dispositivos/cf88/art-40-par-1-inc-i/ec-103-2019.md
    - /dispositivos/lce-1100-2021/art-24/original.md
    - /dispositivos/lce-1100-2021/art-26/original.md
    - /dispositivos/lce-1100-2021/art-27-inc-ii/original.md
    - /dispositivos/lce-1100-2021/art-30-caput/original.md
    - /dispositivos/lce-1100-2021/art-30-par-14/original.md
    - LCE 1.100/2021 compilada pela DITEL, consultada em 01/08/2026
  notas: >-
    O art. 26 aplica fração em dias sobre a média do art. 24; o art. 27, II,
    disciplina separadamente o reajuste sem paridade. `Não identificado` evita
    reduzir a fórmula composta à mera contagem de dias. Origem material:
    substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Substituir o ramo residual de regra-0021 por unidade com causa, base média
      e proporcionalização explicitadas.
confianca: media
---

# Síntese

Para servidor ingressado após 31/12/2003 cuja incapacidade decorra de causa
comum, o § 14 remete ao art. 26: média do art. 24 proporcionalizada em dias. O
reajuste segue o art. 27, II, sem paridade.

A regra legada precisa ser substituída porque traz fundamentações das causas
qualificadas e o rótulo `Proporcionalidade Dias` não expressa sozinho a base
média.

# Pendências localizadas

- criar ou confirmar FormaCalculo que represente média proporcional em dias;
- confirmar a projeção operacional sem paridade;
- resolver Q6-S/Q6-T e completar o gate humano.
