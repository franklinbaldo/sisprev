---
type: RegraProposta
id: invalidez-cf88-original-lce68-causa-comum
ciclo: ciclo-09
schema_version: 1
estado_auditoria: elaboracao
estado_implantacao: pendente_mapeamento_sisprev
origens_legacy:
  - regra-0001
  - regra-0002
predicados:
  causa_incapacidade: causa_comum
  regime: cf88-original-lce68-direito-adquirido
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
    data_direito_apos: 09/12/1992 00:00
    data_direito_ate: 16/12/1998 00:00
taxonomias:
  - ref: /dispositivos/cf88/art-40-inc-i/original.md
    papel: define o ramo proporcional residual, sem denominador
  - ref: /dispositivos/cf88/art-40-par-4/original.md
    papel: funda a paridade
  - ref: /dispositivos/ec-20-1998/art-3-caput/original.md
    papel: preserva o direito adquirido
  - ref: /dispositivos/lce-68-1992/art-235/original.md
    papel: confirma a proporcionalidade e registra o veto do parágrafo único, sem fornecer a fração
  - ref: /dispositivos/lce-68-1992/art-236/original.md
    papel: fixa a base estatutária
  - ref: /dispositivos/lce-68-1992/art-137/original.md
    papel: fixa conversão anual e arredondamento, mas não o denominador
projecao:
  nome: Invalidez · CF/88 original · LCE 68/1992 · demais causas · fórmula pendente · paridade
  tipo_de_beneficio: APOSENTADORIA POR INVALIDEZ
  simulavel: N
  paridade: S
  sexo: AMBOS
  integral: N
  tipo_calculo: Valor Efetivo
  fundamentacao_proporcional: >-
    O art. 40, inciso I, da Constituição Federal em seu texto original e o art.
    235 da LCE 68/1992 determinam proventos proporcionais para as demais
    causas. O art. 236 fixa a base e o art. 137 fixa a conversão em anos de 365
    dias e o arredondamento do resto superior a 180 dias. Nenhum deles fixa o
    denominador. O parágrafo único do art. 235 consta expressamente como
    VETADO. Importar 35/30 da aposentadoria voluntária do art. 232, III, “a”,
    seria interpretação sistemática contra uma lacuna produzida por veto e não
    é adotado nesta minuta sem manifestação jurídica específica. O art. 40,
    § 4º, assegura a revisão paritária.
proveniencia:
  fontes_consultadas:
    - /dispositivos/lce-68-1992/art-137/original.md
    - /dispositivos/lce-68-1992/art-235/original.md
    - /dispositivos/lce-68-1992/art-236/original.md
  notas: >-
    A lacuna é jurídica e demonstrada. Enquanto o denominador não for adotado
    em manifestação própria, não há TipoCalculo completo nem projeção de
    homologação capaz de afirmar a fórmula.
decisoes:
  - data: 2026-08-08
    quem: openai-codex
    o_que: >-
      Isolar o segmento da LCE 68/1992 e não preencher por analogia o
      denominador cujo dispositivo foi vetado.
confianca: media
---

# Pendência jurídica localizada

- [ ] obter manifestação jurídica específica sobre o denominador aplicável de
  09/12/1992 a 15/12/1998, considerando o veto ao parágrafo único do art. 235;
- [ ] somente depois definir o TipoCalculo, verificar se sexo é discriminante e
  mapear a projeção no Sisprev.
