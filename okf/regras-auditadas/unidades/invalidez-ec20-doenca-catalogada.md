---
type: UnidadeAuditada
id: invalidez-ec20-doenca-catalogada
schema_version: 1
estado_unidade: elaboracao
origens_legacy:
- regra-0004
predicados:
  causa_incapacidade: doenca_catalogada
  regime: cf88-ec20-direito-adquirido
  sexo: ambos
requisitos_verificacao_humana:
- predicado: a incapacidade permanente decorre de doença grave, contagiosa ou incurável incluída no rol legal vigente na data do direito
  protocolo_verificacao:
    pergunta: O diagnóstico causador da incapacidade consta do rol legal vigente quando os requisitos foram implementados?
    responsavel: junta médica oficial e instrução previdenciária do IPERON
    meio_de_prova: laudo médico oficial, exames, prontuários e texto legal do rol vigente na data do direito
    momento: instrução e seleção da regra
    evidencia_exigida: diagnóstico confirmado, incapacidade permanente e correspondência expressa com o rol legal temporalmente aplicável
  portador_primario: fundamentacao_integral
aplicabilidade_temporal:
  datas_legadas:
    data_direito_apos: 16/12/1998 00:00
    data_direito_ate: 31/12/2003 00:00
  versao_rol: norma-estadual-vigente-na-data-do-direito
taxonomias:
- ref: /dispositivos/cf88/art-40-par-1-inc-i/ec-20-1998.md
  papel: condiciona a integralidade à doença especificada em lei
- ref: /dispositivos/cf88/art-40-par-3/ec-20-1998.md
  papel: fixa a base na totalidade da remuneração do cargo efetivo
- ref: /dispositivos/cf88/art-40-par-8/ec-20-1998.md
  papel: assegura paridade
projecao:
  nome: Invalidez · EC 20/1998 · doença grave catalogada · integral · paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: S
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Efetivo
proveniencia:
  fontes_consultadas:
  - /dispositivos/cf88/art-40-par-1-inc-i/ec-20-1998.md
  - /dispositivos/cf88/art-40-par-3/ec-20-1998.md
  - /dispositivos/cf88/art-40-par-8/ec-20-1998.md
  - EC 41/2003, art. 3º — preservação do direito adquirido
  - legislação estadual vigente na data do direito: LC 68/1992 ou LC 228/2000
  notas: O rol é taxonomia versionada pela data do direito; a mudança de lista não produz uma regra por doença. Origem material: substituição.
decisoes:
- data: 2026-08-01
  quem: franklinbaldo
  o_que: Decompor a regra-0004 por classe de causa e manter o rol como taxonomia temporal.
confianca: media
---

# Síntese

Hipótese integral por doença catalogada no regime da EC 20/1998. O rol aplicável é o vigente na data em que o direito foi implementado.

# Pendências localizadas

- transcrever os rols estaduais temporalmente aplicáveis;
- confirmar a projeção da forma de cálculo no Sisprev;
- confirmar o fluxo operacional de classificação da causa.
