---
type: Regra
id: regra-0032
row_index: 32
id_sisprev: '81'
nome_original: Compulsória - Art. 40, §1º, II da CF com redaçao da EC 103/19 c/c art. 31 da Lc nº 1.100/2021
nome: Compulsória · requisitos a partir de 18/10/2021 · Ambos · proporcional · Tipo Cálculo Nova Previdência
tipo_de_beneficio: APOSENTADORIA COMPULSÓRIA
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 2º
validado_pge: 'FALSE'
validado_presidencia: 'FALSE'
simulavel: S
tipo: CIVIL
apos_especial: N
tipo_remun: ''
paridade: N
tabelapontuacao: N
requisitos_da_in_no_5_2020: N
relatorio_p_reserva_remunerada_por_idade_ex_officio: N
adicional_inatividade: N
data_adm_ate: 31/12/2099 00:00
data_adm_apos: 01/01/1950 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 18/10/2021 00:00
fundamentacao_proporcional: Aposentadoria compulsória, com proventos proporcionais ao tempo de contribuição (média aritmética simples) e sem paridade, com base no artigo 40, § 1º, inciso II, da Constituição Federal, com redação dada pela Emenda Constitucional nº 88/2015; em conformidade com a Lei Complementar nº 152/2015, combinado com os artigos 17, 21, § 1º, 45 e 62 da Lei Complementar Estadual nº 432/2008, e com o artigo 4º da Emenda Constitucional Estadual nº 146/2021.
visivel_dtc_proporcional: N
fundamentacao_integral: ''
visivel_dtc_integral: N
sexo: AMBOS
integral: N
tipo_calculo: Tipo Cálculo Nova Previdência
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-ii/ec-88-2015.md
  - /dispositivos/ece-146-2021/art-4/original.md
  - /dispositivos/lce-432-2008/art-17/original.md
  - /dispositivos/lce-432-2008/art-21-par-1/original.md
  - /dispositivos/lce-432-2008/art-45/lce-672-2012.md
  - /dispositivos/lce-432-2008/art-62/original.md
precedentes:
  - identificador: 0029.000764/2023-81
    fonte: SEI
    parecer: /fontes-oficiais/processos-sei/0029_000764-2023-81/informação_892__0040009501_.md
    observacao: >-
      A Informação 892/2023/PGE-IPERON analisa concretamente a situação de
      servidor que completou 75 anos em 28/02/2023, com 29 anos, 7 meses e 25
      dias de contribuição, e opina pela possibilidade jurídica de aposentadoria
      compulsória com proventos proporcionais, sem paridade e média, com base
      no art. 40, § 1º, II da CF, LC 152/2015, arts. 17, 21, § 1º, 45 e 62 da
      LCE 432/2008 e art. 4º da ECE 146/2021. Esse cotejo confirma diretamente
      o benefício, a proporcionalidade, a ausência de paridade e o trilho de
      cálculo registrados nesta regra, além de coincidir com os seus seis
      dispositivos. O parecer também oferece uma opção alternativa de
      aposentadoria voluntária por idade e tempo, com integralidade e paridade;
      por isso não prova que a compulsória foi efetivamente concedida nem que
      foi a opção escolhida pelo interessado. É precedente de aplicação jurídica
      da hipótese compulsória, não validação automática do cadastro Sisprev.
disposicao_de_achados:
  - achado: /achados/achado-0022.md
    disposicao: encaminhada
    justificativa: >-
      Esta regra invoca o art. 4º da ECE 146/2021 — o dispositivo que preserva a
      legislação anterior, e que exige que os requisitos "sejam cumpridos até 31
      de dezembro de 2024" — e grava `data_direito_ate` sentinela. Ela é, entre as
      cinco da população, a que mais corrobora a leitura: abre o direito em
      `18/10/2021`, a entrada em vigor da LCE 1.100/2021, isto é, exatamente
      dentro do período de graça que o art. 4º concede e que termina em 2024.
      **Aqui há uma divergência interna anterior à janela, e ela pode mudar a
      pergunta.** O `nome` funda esta regra na EC 103/2019 e na LC 1.100/2021 —
      regime novo —, enquanto a `fundamentacao` a funda na EC 88/2015 e na LC
      152/2015, anteriores à ECE 146/2021. Se o nome estiver certo, a regra é do
      regime novo e o defeito deixa de ser a janela: passa a ser a citação do
      art. 4º, que não teria por que alcançá-la. Decidir a janela antes de decidir
      isso é arrumar o campo errado.
      **Por que não é `corrigida` em nenhuma das duas hipóteses.** Se a janela for
      o defeito, `data_direito_ate` é **critério aferido**, e a Decisão 10 de
      `docs/analysis/decisoes-de-auditoria-2026-07-30.md` deliberadamente não
      estendeu a autorização além de `nome` e `FUNDAMENTACAO*` — alterar critério
      passa pelo conjunto (RFC 0006). Se a citação for o defeito, o campo é
      editável pela auditoria, mas qual regime a regra implementa é justamente o
      que não está decidido.
      **Por que não é `nao_se_aplica`.** Nas duas hipóteses sobra defeito nesta
      regra: ou a janela contradiz o dispositivo invocado, ou o dispositivo
      invocado não é o dela.
    decidido_por: franklinbaldo
    decidido_em: 2026-07-30
    decisao_pendente_de: >-
      IPERON, como titular do produto: se esta regra implementa o regime da EC
      103/2019 c/c LCE 1.100/2021, como diz o `nome`, ou o da EC 88/2015 c/c LC
      152/2015, como diz a `fundamentacao`. A resposta decide qual campo se
      corrige, e é anterior à janela.
---

# Estado da análise

Aposentadoria compulsória aos 75 anos: janela de direito abrindo em 18/10/2021 —
a vigência da LCE 1.100/2021 —, `tipo_calculo: Tipo Cálculo Nova Previdência`,
`paridade: N`, `integral: N`, proventos proporcionais ao tempo de contribuição.

O critério aferido está certo e conferido: 75 anos com proventos proporcionais é
o que diz o art. 40, § 1º, II da CF (idêntico nas redações da EC 88/2015 e da EC
103/2019), o que a LC federal 152/2015 fixou, e o que o art. 31 da LCE 1.100/2021
repete para Rondônia.

Duas conferências independentes chegaram a esta regra por lados opostos, e o
resultado combinado é mais forte que cada um: a
[conferência da janela do art. 4º](../../../docs/analysis/conferencia-janela-art-4-ece-146.md)
olhou as 24 regras que vinculam aquele dispositivo; a conferência das regras sem
achado olhou a cadeia de vigência da redação citada. **As duas apontam a mesma
divergência interna, e é ela que decide o resto.**

O `nome` funda a regra na EC 103/2019 e no art. 31 da LCE 1.100/2021 — regime
novo. A `fundamentacao_proporcional` a funda na EC 88/2015 e na LC 152/2015 —
legislação anterior à ECE 146/2021, que é justamente o que o art. 4º daquela
emenda preserva, e preserva **com prazo** (requisitos cumpridos até 31/12/2024).

Qual das duas vale muda o diagnóstico por inteiro, e nos dois sentidos:

- **Se vale a fundamentação** (regime anterior resguardado), então a regra se
  socorre do art. 4º e a janela deveria fechar em `31/12/2024`, não em
  `31/12/2099`. É a leitura da conferência da janela.
- **Se vale o `nome`** (regime novo), então a sentinela está certa — a nova
  previdência não tem prazo de extinção — e o que sobra é o vínculo ao art. 4º,
  que não deveria estar ali. É a leitura inversa.

Há ainda um defeito que independe dessa escolha: a atribuição da redação. A
`fundamentacao_proporcional` dá o art. 40, § 1º, II à EC 88/2015, extinta em
12/11/2019, quase dois anos antes de a janela abrir. O texto do inciso é idêntico
nas duas redações, então nenhum beneficiário recebe coisa diferente; mas a
**cadeia** difere, e o § 1º da redação de 2015 manda calcular os proventos "na
forma dos §§ 3º e 17", caminho que esta regra não segue. É o defeito silencioso
que a `okf/spec/dispositivo.md` descreve: caminho confere, vínculo resolve,
texto verbatim, nenhum gate acusa.

Registro de método, porque é contraintuitivo: o vínculo a
`cf88/art-40-par-1-inc-ii/ec-88-2015` **não** deve ser trocado antes da
fundamentação. Um vínculo afirma que a fundamentação cita aquela provisão, e ela
cita — corrigir o vínculo primeiro romperia a fidelidade e esconderia o defeito
no campo que é entregue.

- [x] Critério aferido (75 anos, proventos proporcionais) conferido contra o art. 40, § 1º, II da CF, a LC 152/2015 e o art. 31 da LCE 1.100/2021
- [x] `data_direito_apos: 18/10/2021` conferido contra a `vigencia_inicio` da LCE 1.100/2021
- [x] Art. 4º da ECE 146/2021 lido verbatim na transcrição oficial: o "sendo assegurada a qualquer tempo" é do momento da concessão, não do implemento dos requisitos
- [x] `paridade: N`, `integral: N` e `tipo_calculo` coerentes entre si
- [x] `dispositivos:` conferido contra `fundamentacao_proporcional` item a item: os seis vínculos correspondem ao que o campo cita — inclusive o da EC 88/2015, que é fiel a um campo errado
- [ ] Divergência `nome` × fundamentação sobre qual regime funda a regra ([`achado-0023`](../achados/achado-0023.md)). É a decisão da qual dependem os dois itens seguintes
- [ ] `data_direito_ate: 31/12/2099` deveria ser `31/12/2024` **se** vale a fundamentação ([`achado-0022`](../achados/achado-0022.md)); se vale o `nome`, o que sobra é o vínculo ao art. 4º. Campo deployável nos dois casos
- [ ] `fundamentacao_proporcional` atribui à EC 88/2015 uma redação que não vigia em nenhum dia da janela, e a cadeia dela aponta fórmula de cálculo que a regra não usa
- [ ] `nome` cita o art. 31 da LCE 1.100/2021 e nenhum campo de fundamentação o cita. Vínculo não proposto: só cabe depois de a fundamentação citar
- [ ] Quatro vínculos a dispositivos da LCE 432/2008 cujo último dia de vigência (18/10/2021) é o primeiro dia da janela desta regra
