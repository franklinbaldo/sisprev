---
type: Regra
id: regra-0065
row_index: 65
nome: Voluntária · Agentes nocivos · pedido a partir de 31/12/2003 · Ambos · integral · paridade · regra-0065
tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 3º
validado_pge: 'FALSE'
validado_presidencia: 'FALSE'
simulavel: S
tipo: CIVIL
apos_especial: S
tipo_remun: ''
paridade: S
tabelapontuacao: N
requisitos_da_in_no_5_2020: N
relatorio_p_reserva_remunerada_por_idade_ex_officio: N
adicional_inatividade: N
data_adm_ate: 31/12/2099 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 31/12/2003 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria voluntária de servidor exposto a agentes nocivos à saúde, com proventos integrais (cálculo por integralidade) e com paridade, com base nos artigos 25, 27, inciso I, e 41, inciso III, da Lei Complementar Estadual 1.100/2021 e artigo 40, § 1º, inciso III, segunda parte, e § 4°-C, da Constituição Federal, com redação dada pela Emenda Constitucional nº 103/2019 - regra permanente
visivel_dtc_integral: N
sexo: AMBOS
integral: S
tipo_calculo: Valor Médio
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/cf88/art-40-par-4c/ec-103-2019.md
  - /dispositivos/lce-1100-2021/art-25/original.md
  - /dispositivos/lce-1100-2021/art-27-inc-i/original.md
  - /dispositivos/lce-1100-2021/art-41-inc-iii/original.md
precedentes:
  - identificador: 0016.102962/2020-85
    fonte: SEI
    parecer: /fontes-oficiais/processos-sei/0016_102962-2020-85/parecer_608_pge-iperon__0061369704_.md
    observacao: >-
      O parecer coteja-se diretamente com esta regra: trata de aposentadoria
      voluntária por exposição a agentes nocivos e fundamenta a concessão nos
      arts. 25, 27, I e 41, III da LCE 1.100/2021, exatamente os dispositivos
      gravados aqui. A conclusão é por proventos integrais pela integralidade da
      última remuneração e paridade, o que confirma a hipótese jurídica e os
      campos `integral: S` e `paridade: S`, mas contradiz o `Valor Médio` de 0065.
      O parecer não informa que 0065 foi a linha executada nem resolve sua janela
      legada; serve como caso concreto do trilho, não como validação automática.
disposicao_de_achados:
  - achado: /achados/achado-0057.md
    disposicao: encaminhada
    justificativa: >-
      A contradição é tripla dentro desta regra e está conferida. Os
      `dispositivos:` vinculam `lce-1100-2021/art-25` e
      `lce-1100-2021/art-27-inc-i`; a `fundamentacao_integral` escreve por extenso
      "cálculo por integralidade" e "com paridade"; e os campos `integral: S` e
      `paridade: S` confirmam. Só o `tipo_calculo` destoa, gravando `Valor Médio`,
      que é o regime do **art. 24** — o artigo do outro trilho, que esta regra não
      cita. A `regra-0067` fecha o argumento: `fundamentacao_integral` idêntica
      caractere a caractere, `dispositivos:` idênticos item a item, mesma janela,
      mesmo sexo, e grava `Valor Efetivo`.
      **Por que não é `corrigida`.** `tipo_calculo` é campo deployável, não
      `nome` nem `FUNDAMENTACAO*`; alterar o critério passa pelo conjunto (RFC
      0006). A investigação temporal foi concluída no
      [`achado-0042`](../achados/achado-0042.md): os arts. 25 e 27, I exigem o
      corte até 31/12/2003, e a LCE 1.100/2021 fixa o primeiro dia de direito em
      18/10/2021. A regra proposta proposta corrige os dois limites e usa
      `Valor Efetivo` como hipótese de projeção, mas permanece em `preview` e
      seu grupo permanece inativo.
      **Por que não é `nao_se_aplica`.** A regra é `simulavel: S` e `tipo_calculo`
      é o campo que orienta o cálculo — ao contrário da fundamentação, que o motor
      não lê. Média das maiores remunerações de 80% do período contributivo e
      totalidade da remuneração no cargo efetivo produzem valores diferentes, e a
      diferença se projeta em todo o benefício.
      Esta disposição **não** afirma que `Valor Efetivo` seja o rótulo
      juridicamente exato da totalidade do art. 25 — o enum legado não identifica
      fórmulas (P16) —, nem que alguma concessão tenha saído a menor.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
    decisao_pendente_de: >-
      O IPERON, como titular do produto: confirmar qual membro do enum representa
      a totalidade da remuneração do art. 25 e decidir se adota a unidade
      `agentes-nocivos-art-41-iii-integralidade-paridade`. A alteração tem por
      veículo o Conjunto, não uma edição no documento legado.
  - achado: /achados/achado-0042.md
    disposicao: encaminhada
    justificativa: >-
      A incompatibilidade temporal está demonstrada também nesta regra. Os arts.
      25 e 27, I limitam a população ao ingresso até 31/12/2003, mas
      `data_adm_ate` usa a sentinela 31/12/2099. O marco
      `data_direito_apos: 31/12/2003` antecede todos os dispositivos citados; a
      LCE 1.100/2021 entrou em vigor em 18/10/2021. A regra proposta proposta
      grava `data_adm_ate: 31/12/2003` e
      `data_direito_apos: 18/10/2021`. Não é `corrigida` porque a origem
      permanece intacta e operacional enquanto o grupo estiver inativo.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
    decisao_pendente_de: >-
      Decisão interna de adotar ou rejeitar a substituição proposta no
      Conjunto; os marcos já foram confirmados pelas fontes oficiais.
  - achado: /achados/achado-0005.md
    disposicao: encaminhada
    justificativa: >-
      A investigação documental não encontrou critério gravado que separe
      `regra-0065` de `regra-0066`. A proposta posterior trata 0065–0067 como
      origens coletivas e decompõe o ramo nas três faixas legais, sem inventar
      correspondência individual entre linha e inciso. Não é `corrigida`
      porque o grupo está inativo e as linhas legadas continuam no catálogo.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
    decisao_pendente_de: >-
      Decisão interna de adotar ou rejeitar a decomposição completa proposta.
---

# Estado da análise

Regra permanente de aposentadoria voluntária por efetiva exposição a agentes
nocivos. O art. 40, § 1º, III da CF, na redação da EC 103/2019, remete a idade,
tempo de contribuição e demais requisitos à legislação do ente; o § 4º-C
permite idade e tempo diferenciados para a exposição efetiva. A hipótese
material vem do art. 41, III da LCE 1.100/2021: 20 anos de serviço público, 5
anos no cargo, 86 pontos e 25 anos de efetiva exposição. O art. 25 fixa a
**totalidade da remuneração no cargo efetivo** para ingresso até 31/12/2003,
sem opção pelo § 16 do art. 40 da CF; o art. 27, I fixa o reajuste por remissão
ao art. 7º da EC 41/2003 para a mesma população. O conteúdo da remissão foi
conferido no art. 7º transcrito no repositório: revisão na mesma proporção e na
mesma data da remuneração dos servidores em atividade.

O frontmatter põe a regra no motor (`simulavel: S`) e grava valores estruturados
para sexo, tipo, especialidade, pontuação, janelas e resultado. Entre os campos
de domínio, `sexo` é critério aferido confirmado; a semântica das quatro datas
também está fixada. Não há coluna para os 20 anos de serviço público, os 5 anos
no cargo, os 86 pontos, os 25 anos de exposição nem para a ausência de opção
pelo § 16. Esses requisitos dependem de verificação humana por construção. O
parecer PGE/IPERON nº 608/2025 transcreve o protocolo do art. 42: formulários
SB-40/DSS-8030/DIRBEN-8030 nos períodos antigos, laudo técnico a partir de
06/03/1997 e PPP a partir de 01/01/2004; no caso concreto, a prova foi um PPP.
Permanecem a conferir nos assentamentos funcionais e previdenciários os tempos,
os pontos, o ingresso e a ausência de opção.

Os campos `integral: S` e `paridade: S` são coerentes, respectivamente, com os
arts. 25 e 27, I. `tipo_calculo: Valor Médio`, porém, destoa do mesmo conjunto
sem que seja necessário converter o enum em fórmula: a `regra-0067` tem
fundamentação e dispositivos idênticos e grava `Valor Efetivo`, enquanto a
`regra-0071` reserva `Valor Médio` ao trilho dos arts. 24 e 27, II. A divergência
está no campo estruturado que orienta o valor, não no texto entregue ao servidor,
e é objeto do `achado-0057`.

As janelas também não correspondem ao fundamento. `data_adm_apos: 01/01/1950`
e `data_adm_ate: 31/12/2099` são sentinelas e, portanto, não gravam o corte de
ingresso até 31/12/2003 exigido pelos arts. 25 e 27, I.
`data_direito_apos: 31/12/2003` inclui esse próprio dia e antecede todos os
cinco dispositivos citados; nenhuma provisão transcrita funda esse marco. É o
mesmo defeito temporal já demonstrado no `achado-0042` para a `regra-0067`.

A planilha da PGE registra uma única linha e um único processo para o texto que
corresponde a `regra-0065`, `regra-0066` e `regra-0067`; esse caso concreto
aplica o inciso III. Isso não exclui as duas faixas que o próprio art. 41
contém. A proposta auditada passou a tratar as três origens como grupo e
decompô-las nas faixas I–III, sem afirmar qual linha legada correspondia a cada
inciso e sem alterar o catálogo vigente.

- [x] Os cinco arquivos de `dispositivos:` foram lidos integralmente, com a cadeia de ancestrais, e correspondem às cinco provisões nomeadas em `fundamentacao_integral`
- [x] A remissão do art. 27, I ao art. 7º da EC 41/2003 foi conferida no arquivo transcrito `ec-41-2003/art-7/original.md`; o dispositivo descreve revisão na mesma proporção e data da remuneração dos servidores em atividade
- [x] O vínculo critério → dispositivo foi recuperado: art. 40, § 1º, III para a remissão à legislação estadual; art. 40, § 4º-C para a diferenciação por exposição; art. 41, III para 20 anos de serviço público, 5 no cargo, 86 pontos e 25 de exposição; art. 25 para totalidade da remuneração e corte de ingresso; art. 27, I para reajuste e o mesmo corte
- [x] `sexo: AMBOS` conferido contra os dispositivos citados: o art. 41, III não divide a hipótese por sexo, e nenhuma das demais provisões estaduais vinculadas introduz essa distinção
- [x] `integral: S` e `paridade: S` conferidos contra os arts. 25 e 27, I e contra o texto objeto da remissão: coerentes
- [x] Requisitos sem coluna identificados: 20 anos de serviço público, 5 anos no cargo, 86 pontos, 25 anos de efetiva exposição e ausência de opção pelo § 16 do art. 40 da CF; a aferição depende de análise humana
- [x] Identificar a prova da exposição: o parecer PGE/IPERON nº 608/2025 transcreve o art. 42 e documenta formulários, laudo técnico e PPP; o caso concreto foi instruído com PPP
- [ ] Confirmar nos assentamentos funcionais e previdenciários os 20 anos de serviço público, 5 anos no cargo, 86 pontos e a ausência de opção pelo § 16
- [ ] Confirmar, além de `sexo` e das janelas, quais campos de domínio o motor efetivamente afere; `tipo`, `apos_especial`, `tabelapontuacao` e os demais permanecem candidatos sem evidência operacional suficiente
- [ ] Adotar ou rejeitar a substituição de `tipo_calculo: Valor Médio`; a regra proposta propõe `Valor Efetivo`, mas permanece em `preview` até confirmação do IPERON — `achado-0057`
- [x] Estender `regras_afetadas` do `achado-0042` a esta regra e propor `data_adm_ate: 31/12/2003` e `data_direito_apos: 18/10/2021` na regra proposta
- [x] `tabelapontuacao: N` coerente com faixas fixas; o corpus usa `S` quando há progressão anual. O defeito correspondente está nas regras 0068–0070 — `achado-0054`
- [x] Apurar o grupo de igualdade material com a `regra-0066`: a planilha da PGE e o parecer não revelam distinção e sustentam a consolidação 3:1 com `regra-0067`; adoção institucional ainda pendente — `achado-0005`
