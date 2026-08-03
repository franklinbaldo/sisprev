---
type: RegraProposta
id: invalidez-cf88-original-doenca-catalogada
schema_version: 1
estado_proposta: elaboracao
origens_legacy:
  - regra-0001
  - regra-0002
predicados:
  causa_incapacidade: doenca_catalogada
  regime: cf88-original-direito-adquirido
  sexo: ambos
requisitos_verificacao_humana:
  - predicado: >-
      a incapacidade permanente decorre de doença grave, contagiosa ou
      incurável incluída no rol legal vigente na data do direito
    protocolo_verificacao:
      pergunta: >-
        O diagnóstico causador da incapacidade consta do rol legal vigente
        quando os requisitos foram implementados?
      responsavel: junta médica oficial e instrução previdenciária do IPERON
      meio_de_prova: >-
        laudo médico oficial, exames, prontuários e texto legal do rol vigente
        na data do direito
      momento: instrução e seleção da regra
      evidencia_exigida: >-
        diagnóstico confirmado, incapacidade permanente e correspondência
        expressa com o rol legal temporalmente aplicável
    portador_primario: fundamentacao_integral
aplicabilidade_temporal:
  datas_legadas:
    data_direito_apos: 05/10/1988 00:00
    data_direito_ate: 16/12/1998 00:00
  versao_rol: norma-estadual-vigente-na-data-do-direito
taxonomias:
  - ref: /dispositivos/cf88/art-40-inc-i/original.md
    papel: condiciona a integralidade à doença especificada em lei
projecao:
  nome: Invalidez · CF/88 original · doença grave catalogada · integral · paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: S
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Efetivo
proveniencia:
  fontes_consultadas:
    - /formas-calculo/forma-calculo-totalidade-remuneracao-cargo-efetivo-cf88-original.md
    - /dispositivos/cf88/art-40-inc-i/original.md
    - EC 20/1998, art. 3º — preservação do direito adquirido
    - >-
      legislação estadual vigente na data de implementação dos requisitos: LC
      1/1984, LC 39/1990 ou LC 68/1992
    - docs/analysis/base-normativa-invalidez-incapacidade.md
  notas: >-
    O rol é taxonomia versionada pela data do direito, não uma série de regras
    por doença ou por diploma. Origem material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Decompor o Bloco A por regime constitucional e classe de causa e manter o
      rol como taxonomia temporal.
confianca: media
---

# Síntese

Hipótese de invalidez sob CF/88 original por doença grave catalogada. A
correspondência ao rol deve ser verificada na versão vigente quando o direito
foi implementado.

# Pendências localizadas

- transcrever os rols estaduais temporalmente aplicáveis;
- confirmar a projeção da forma de cálculo no Sisprev;
- confirmar o fluxo operacional de classificação da causa.
