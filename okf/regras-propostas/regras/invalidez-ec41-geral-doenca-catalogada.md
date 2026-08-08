---
type: RegraProposta
id: invalidez-ec41-geral-doenca-catalogada
ciclo: ciclo-09
schema_version: 1
estado_auditoria: concluida
estado_implantacao: confirmada_com_ressalva
ressalva_homologacao: >-
  A homologação deve confirmar o fluxo, a projeção e o cotejo do diagnóstico
  com a versão do rol selecionada pela data do direito.
origens_legacy:
  - regra-0006
predicados:
  causa_incapacidade: doenca_catalogada
  regime: ec41-regra-geral-media-desde-mp167-preservada-art-4
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
    data_direito_apos: 20/02/2004 00:00
    data_direito_ate: 01/01/2025 00:00
  versao_rol: norma-estadual-vigente-na-data-do-direito
taxonomias:
  - ref: /dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
    papel: define o ramo sem proporcionalização nas causas qualificadas
  - ref: /dispositivos/ece-146-2021/art-4/original.md
    papel: preserva os requisitos anteriores até 31/12/2024
  - ref: /dispositivos/mp-167-2004/art-1/original.md
    papel: institui a média desde 20/02/2004
  - ref: /dispositivos/lei-10887-2004/art-1/original.md
    papel: mantém a média após a conversão da MP
  - ref: /dispositivos/lce-228-2000/art-44-par-1/lce-253-2002.md
    papel: contém o rol de 20/02/2004 a 12/03/2008
  - ref: /dispositivos/lce-432-2008/art-20/original.md
    papel: inclui doença grave entre as causas qualificadas
  - ref: /dispositivos/lce-432-2008/art-20-par-9/original.md
    papel: >-
      contém o rol desde 13/03/2008 e é preservado pelo art. 4º da ECE 146 até
      o fecho da janela
  - ref: /dispositivos/lce-432-2008/art-45/original.md
    papel: reproduz a média desde 13/03/2008
  - ref: /dispositivos/lce-432-2008/art-45/lce-672-2012.md
    papel: mantém a média desde 09/08/2012
projecao:
  nome: >-
    Invalidez · EC 41/2003 · desde MP 167 · doença catalogada · média sem
    proporcionalização · sem paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: N
  sexo: AMBOS
  integral: S
  tipo_calculo: Valor Médio
proveniencia:
  fontes_consultadas:
    - /dispositivos/cf88/art-40-par-1-inc-i/ec-41-2003.md
    - /dispositivos/ece-146-2021/art-4/original.md
    - /dispositivos/mp-167-2004/art-1/original.md
    - /dispositivos/lei-10887-2004/art-1/original.md
    - /dispositivos/lce-228-2000/art-44-par-1/lce-253-2002.md
    - /dispositivos/lce-432-2008/art-20/original.md
    - /dispositivos/lce-432-2008/art-20-par-9/original.md
    - /dispositivos/lce-432-2008/art-45/original.md
    - /dispositivos/lce-432-2008/art-45/lce-672-2012.md
    - /tipos-calculo/tipo-calculo-media-80-invalidez-ec41.md
  notas: >-
    A unidade foi estreitada para a média vigente desde 20/02/2004. O segmento
    anterior usa remuneração integral do cargo. O rol da LCE 228 rege até
    12/03/2008; o da LCE 432 rege desde 13/03/2008 e continua aplicável até
    31/12/2024 por preservação do art. 4º da ECE 146. A LCE 1.100/2021 é
    posterior ao marco de preservação e não integra esta janela. Origem
    material: substituição.
decisoes:
  - data: 2026-08-01
    quem: franklinbaldo
    o_que: >-
      Separar a base remuneratória anterior à MP 167 da base média posterior.
  - data: 2026-08-08
    quem: openai-codex
    o_que: >-
      Excluir o rol posterior da LCE 1.100/2021 desta janela e manter, desde
      13/03/2008, o rol da LCE 432/2008 preservado pelo art. 4º da ECE 146.
confianca: alta
---

# Síntese

Invalidez por doença catalogada desde 20/02/2004: média de 80% sem
proporcionalização e reajuste sem paridade. O diagnóstico é cotejado com o rol
da LCE 228 até 12/03/2008 e com o rol da LCE 432 desde 13/03/2008; a LCE
1.100/2021 não rege o período preservado pela ECE 146.

# Pendências localizadas

- [ ] confirmar o fluxo operacional de cotejo do diagnóstico;
- [ ] resolver Q6-S/Q6-T.
