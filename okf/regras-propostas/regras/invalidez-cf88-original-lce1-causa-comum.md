---
type: RegraProposta
id: invalidez-cf88-original-lce1-causa-comum
ciclo: ciclo-09
schema_version: 1
estado_auditoria: concluida
estado_implantacao: confirmada_com_ressalva
ressalva_homologacao: >-
  Confirmar que `Valor Efetivo`, com `integral: N`, aplica a remuneração da
  atividade e a razão de 1/30 por ano apurado segundo o art. 86 da LCE 1/1984.
origens_legacy:
  - regra-0001
  - regra-0002
predicados:
  causa_incapacidade: causa_comum
  regime: cf88-original-lce1-direito-adquirido
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente não decorre de acidente em serviço, moléstia
      profissional nem doença catalogada na norma aplicável
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
        incapacidade permanente comprovada e investigação suficiente das
        causas qualificadas; silêncio ou prova insuficiente não bastam
    portador_primario: fundamentacao_proporcional
aplicabilidade_temporal:
  datas_legadas:
    data_direito_apos: 05/10/1988 00:00
    data_direito_ate: 31/07/1990 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-inc-i/original.md
    papel: define a invalidez permanente e o ramo proporcional residual
  - ref: /dispositivos/cf88/art-40-par-4/original.md
    papel: funda a paridade
  - ref: /dispositivos/ec-20-1998/art-3-caput/original.md
    papel: preserva o direito adquirido
  - ref: /dispositivos/lce-1-1984/art-94/original.md
    papel: define remuneração como vencimento mais vantagens legais
  - ref: /dispositivos/lce-1-1984/art-154-par-2/original.md
    papel: vincula sistematicamente os proventos à remuneração da atividade
  - ref: /dispositivos/lce-1-1984/art-154-par-3/original.md
    papel: fixa 1/30 por ano de serviço
  - ref: /dispositivos/lce-1-1984/art-86/original.md
    papel: fixa conversão em anos de 365 dias e arredondamento acima de 182 dias
projecao:
  nome: Invalidez · CF/88 original · LCE 1/1984 · demais causas · 1/30 por ano · paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: S
  sexo: AMBOS
  integral: N
  tipo_calculo: Valor Efetivo
  fundamentacao_proporcional: >-
    O art. 40, inciso I, da Constituição Federal em seu texto original atribui
    proventos proporcionais à invalidez permanente que não decorra das causas
    qualificadas, e o art. 3º da EC 20 preserva os requisitos implementados
    antes da emenda. Para o direito implementado de 05/10/1988 a 30/07/1990, o
    art. 94 da LCE 1/1984 define remuneração como vencimento mais vantagens
    financeiras asseguradas por lei; o art. 154, § 2º, limita os proventos à
    remuneração percebida na atividade; e o § 3º determina 1/30 por ano de
    serviço. A remuneração como referência da fração é interpretação
    sistemática desses dispositivos, não texto de um artigo autônomo de base.
    O art. 86 manda apurar em dias, converter por anos de 365 dias e arredondar
    para um ano apenas o resto superior a 182 dias. O art. 40, § 4º, assegura a
    revisão paritária.
proveniencia:
  fontes_consultadas:
    - /tipos-calculo/tipo-calculo-remuneracao-lce1-proporcional-anos.md
    - /dispositivos/cf88/art-40-inc-i/original.md
    - /dispositivos/cf88/art-40-par-4/original.md
    - /dispositivos/ec-20-1998/art-3-caput/original.md
    - /dispositivos/lce-1-1984/art-86/original.md
    - /dispositivos/lce-1-1984/art-94/original.md
    - /dispositivos/lce-1-1984/art-154-par-2/original.md
    - /dispositivos/lce-1-1984/art-154-par-3/original.md
  notas: >-
    A separação decorre de fórmula materialmente própria, não apenas da mudança
    de diploma. A seleção da causa continua humana e a projeção é operacional.
decisoes:
  - data: 2026-08-08
    quem: openai-codex
    o_que: >-
      Representar separadamente o trecho da LCE 1/1984, cuja fórmula usa 1/30
      para ambos os sexos e arredondamento próprio.
confianca: media
---

# Síntese

Hipótese residual proporcional da primeira subjanela da CF/88 original. A
fórmula jurídica está determinada; a execução de `Valor Efetivo` será conferida
em homologação.
