---
type: UnidadeAuditada
id: invalidez-ec41-geral-causa-comum
schema_version: 1
estado_unidade: elaboracao
origens_legacy:
  - regra-0007
predicados:
  causa_incapacidade: causa_comum
  regime: ec41-regra-geral-preservada-art-4-ece146
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente não decorre de acidente em serviço, moléstia
      profissional nem doença grave catalogada na norma aplicável
    protocolo_verificacao:
      pergunta: >-
        Há prova suficiente para excluir todas as classes qualificadas e
        enquadrar o caso no ramo residual proporcional?
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
    data_direito_apos: 31/12/2003 00:00
    data_direito_ate: 01/01/2025 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
    papel: determina o ramo proporcional nos demais casos
  - ref: /dispositivos/ece-146-2021/art-4/original.md
    papel: preserva os requisitos anteriores se implementados até 31/12/2024
  - ref: /dispositivos/lce-432-2008/art-17/original.md
    papel: disciplina a proporcionalização em dias no período da LCE 432/2008
  - ref: /dispositivos/lce-432-2008/art-20/original.md
    papel: define o ramo residual proporcional
  - ref: /dispositivos/lce-432-2008/art-45/lce-672-2012.md
    papel: disciplina a base média no período final da LCE 432/2008
projecao:
  nome: >-
    Invalidez · EC 41/2003 · regra geral preservada · demais causas ·
    proporcional · sem paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: N
  sexo: AMBOS
  integral: N
  tipo_calculo: Não identificado
proveniencia:
  fontes_consultadas:
    - /dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
    - /dispositivos/ece-146-2021/art-4/original.md
    - /dispositivos/lei-10887-2004/art-1/original.md
    - /dispositivos/lce-432-2008/art-17/original.md
    - /dispositivos/lce-432-2008/art-20/original.md
    - /dispositivos/lce-432-2008/art-45/lce-672-2012.md
    - LC 228/2000, texto oficial do SAPL — regime estadual anterior à LCE 432/2008
  notas: >-
    A fórmula jurídica combina base média e proporcionalidade. O enum legado
    não representa com segurança a combinação inteira. Origem material:
    substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Substituir o ramo proporcional legado por unidade com causa, fundamento e
      protocolo próprios.
confianca: media
---

# Síntese

Hipótese residual da **EC 41/2003 · regra geral preservada**. O provento é
proporcional ao tempo, sobre a base temporalmente aplicável, sem paridade.

`Não identificado` registra falta de projeção fiel no enum, não dúvida sobre a
existência do ramo. A causa comum exige exclusão probatória das classes
qualificadas.

# Pendências localizadas

- transcrever e versionar os dispositivos estaduais anteriores à LCE 432/2008;
- fechar a fórmula do intervalo inicial da EC 41/2003;
- parametrizar a combinação base média + proporcionalidade;
- resolver Q6-S/Q6-T quanto à classificação operacional da causa.
