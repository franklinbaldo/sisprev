---
type: RegraProposta
id: invalidez-ec41-geral-pre-mp167-acidente-em-servico
ciclo: ciclo-09
schema_version: 1
estado_auditoria: elaboracao
origens_legacy:
  - regra-0006
predicados:
  causa_incapacidade: acidente_em_servico
  regime: ec41-regra-geral-lc228-pre-mp167
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente decorre de acidente em serviço, com nexo causal
      reconhecido
    protocolo_verificacao:
      pergunta: >-
        A prova médica e administrativa demonstra incapacidade permanente e
        nexo causal com acidente em serviço?
      responsavel: junta médica oficial e instrução previdenciária do IPERON
      meio_de_prova: laudo médico oficial, apuração do acidente e assentamentos funcionais
      momento: instrução e seleção da regra
      evidencia_exigida: incapacidade permanente e nexo reconhecido com o serviço
    portador_primario: fundamentacao_integral
aplicabilidade_temporal:
  datas_legadas:
    data_direito_apos: 31/12/2003 00:00
    data_direito_ate: 20/02/2004 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
    papel: define o ramo qualificado sem proporcionalização
  - ref: /dispositivos/lce-228-2000/art-43/original.md
    papel: separa as causas qualificadas
  - ref: /dispositivos/lce-228-2000/art-44/original.md
    papel: fixa a remuneração integral do cargo
projecao:
  nome: >-
    Invalidez · EC 41 · antes da MP 167 · acidente em serviço · remuneração do
    cargo · sem paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: N
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Efetivo
proveniencia:
  fontes_consultadas:
    - /dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
    - /dispositivos/lce-228-2000/art-43/original.md
    - /dispositivos/lce-228-2000/art-44/original.md
    - /tipos-calculo/tipo-calculo-remuneracao-cargo-integral-lc228.md
  notas: >-
    Segmento entre a publicação da EC 41 e a vigência da MP 167. A lei estadual
    fornece a remuneração integral do cargo; a média federal só incide desde
    20/02/2004. Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: Separar a base remuneratória anterior à regulamentação federal da média.
confianca: alta
---

# Síntese

Acidente em serviço com direito implementado de 31/12/2003 a 19/02/2004:
remuneração integral do cargo, sem proporcionalização e sem paridade.

# Pendências localizadas

- [ ] confirmar a projeção operacional no Sisprev;
- [ ] resolver Q6-S/Q6-T.
