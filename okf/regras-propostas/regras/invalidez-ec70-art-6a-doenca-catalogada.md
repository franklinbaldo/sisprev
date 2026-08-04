---
type: RegraProposta
id: invalidez-ec70-art-6a-doenca-catalogada
schema_version: 1
estado_proposta: elaboracao
origens_legacy:
  - regra-0008
predicados:
  causa_incapacidade: doenca_catalogada
  regime: ec70-art-6a-preservado-art-4-ece146
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente decorre de doença grave, contagiosa ou
      incurável incluída no rol vigente na data de implementação dos requisitos
    protocolo_verificacao:
      pergunta: >-
        A doença incapacitante consta do rol legal temporalmente aplicável e
        está comprovada pela perícia oficial?
      responsavel: junta médica oficial e instrução previdenciária do IPERON
      meio_de_prova: >-
        laudo médico oficial, prontuários e versão vigente do rol legal de
        doenças
      momento: instrução e seleção da regra
      evidencia_exigida: >-
        incapacidade permanente, diagnóstico e correspondência com o rol
        aplicável ao marco temporal do direito
    portador_primario: fundamentacao_integral
aplicabilidade_temporal:
  datas_legadas:
    data_adm_ate: 31/12/2003 00:00
    data_direito_apos: 31/12/2003 00:00
    data_direito_ate: 01/01/2025 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
    papel: é o fundamento de invalidez exigido pelo art. 6º-A
  - ref: /dispositivos/ec-41-2003/art-6a/ec-70-2012.md
    papel: fixa ingresso, remuneração do cargo e paridade
  - ref: /dispositivos/ece-146-2021/art-4/original.md
    papel: preserva os requisitos anteriores se implementados até 31/12/2024
  - ref: /dispositivos/lce-432-2008/art-20-par-9/original.md
    papel: contém o rol no período da LCE 432/2008
projecao:
  nome: >-
    Invalidez · EC 70/2012 · art. 6º-A · doença grave catalogada · integral ·
    paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: S
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Efetivo
proveniencia:
  fontes_consultadas:
    - /dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
    - /dispositivos/ec-41-2003/art-6a/ec-70-2012.md
    - /dispositivos/ece-146-2021/art-4/original.md
    - /dispositivos/lce-432-2008/art-20-par-9/original.md
    - LC 228/2000, texto oficial do SAPL — rol estadual anterior à LCE 432/2008
  notas: >-
    `doenca_catalogada` é o valor implementado do vocabulário controlado e
    corresponde à classe descrita na S1 como doença grave catalogada. A hipótese
    usa remuneração do cargo efetivo e paridade. Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Decompor o art. 6º-A por classe de causa e ramo de resultado.
confianca: media
---

# Síntese

Hipótese do art. 6º-A por doença grave catalogada: remuneração do cargo efetivo,
sem proporcionalização e com paridade.

O rol é aferido na versão vigente na data do direito; a janela superior
exclusiva em 01/01/2025 inclui 31/12/2024.

# Pendências localizadas

- [ ] transcrever e versionar o rol anterior à LCE 432/2008;
- [ ] confirmar qual enum projeta a remuneração do cargo efetivo;
- [ ] confirmar o fluxo operacional de cotejo do diagnóstico com o rol temporal;
- [ ] resolver Q6-S/Q6-T quanto à classificação operacional da causa.
