---
type: Regra
id: regra-0038
row_index: 38
id_sisprev: '87'
nome_original: Voluntária por Idade e Tempo de Contrib. - Art. 40, §1º, III da Constituição Federal c/c do Art. 32 da LC 1.100/21
nome: Voluntária · pedido a partir de 18/10/2021 · integral · média
tipo_de_beneficio: APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 3º
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
data_adm_apos: 01/01/1910 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 18/10/2021 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria voluntária por idade e tempo de contribuição, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 40, § 1°, inciso III, da Constituição Federal, com a redação dada pela Emenda Constitucional nº 103/2019, e artigos 24, 27, inciso II, e artigo 32, da Lei Complementar nº 1.100/2021.
visivel_dtc_integral: N
sexo: FEMININO
integral: S
tipo_calculo: Valor Médio
fundamentacao: ''
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/lce-1100-2021/art-24/original.md
  - /dispositivos/lce-1100-2021/art-27-inc-ii/original.md
  - /dispositivos/lce-1100-2021/art-32/original.md
disposicao_de_achados:
  - achado: /achados/achado-0029.md
    disposicao: nao_se_aplica
    justificativa: >-
      **`nao_se_aplica` desde 2026-08-13, para o par sexo/nome
      especificamente.** A renomeação de 2026-07-30 corrigiu a omissão do
      trilho de cálculo (a correção inteira que o achado exigia) e, seguindo a
      gramática então vigente, também acrescentou `sexo` como faceta final.
      Em reunião de 13/08/2026, a empresa esclareceu que o Sisprev diferencia
      `sexo` sozinho, pelo cadastro do requerente, nos passos seguintes à
      seleção — o operador não precisa do rótulo para isso. `regra-0035` e
      `regra-0036` (e `regra-0037`/`regra-0038`) voltam a compartilhar nome
      entre si; o que o achado exigia — que o trilho de cálculo saia do nome
      compartilhado — continua corrigido e não é revertido por esta disposição.
      Registro em Decisão 11 de
      `docs/analysis/decisoes-de-auditoria-2026-07-30.md`.
    decidido_por: franklinbaldo
    decidido_em: 2026-08-13
---

# Estado da análise

Aposentadoria voluntária comum do **regime permanente** da LCE 1.100/2021, pelo
**trilho da média**, no feminino: `regra-0037` é a mesma regra no masculino, e
divergem em dois campos — `sexo` e `fundamentacao`, esta preenchida lá e vazia
aqui.

O desdobramento por sexo **está fundado** no art. 32, I (62 anos se mulher, 65
se homem), citado, vinculado e transcrito. A assimetria de `fundamentacao`, não:
esta regra entrega um documento sem a frase "Art. 24 da Lei Complementar 1.100
de 18 de outubro de 2021" que a gêmea masculina entrega —
[`achado-0031`](../achados/achado-0031.md). A perda é de reforço e não do único
fundamento, porque a `fundamentacao_integral` das duas nomeia o art. 24 pelo
mesmo número e o vínculo está declarado.

**A janela de admissão não fecha.** Os arts. 24 e 27, II exigem ingresso "após
31 de dezembro de 2003" e a regra grava `data_adm_apos: 01/01/1910` com
`data_adm_ate: 31/12/2099` — corte nenhum:
[`achado-0028`](../achados/achado-0028.md).

- [x] Critérios do cadastro percorridos um a um contra a LCE 1.100/2021, na compilação oficial arquivada (`fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt`) — não apenas contra o texto transcrito no corpus
- [x] `dispositivos:` conferido contra `fundamentacao_integral` item a item: os quatro dispositivos citados estão vinculados, nada a acrescentar nem a remover
- [x] `sexo` é critério que o dispositivo funda: o art. 32, I exige "62 (sessenta e dois) anos de idade, se mulher, e 65 (sessenta e cinco) anos de idade, se homem" — o documento do art. 32 no corpus transcreve o artigo **inteiro**, incisos I a IV inclusive
- [x] `apos_especial: N` e `tabelapontuacao: N`: nenhum dispositivo citado institui especialidade (§§ 4º-A/4º-B/4º-C/5º do art. 40 da CF não são citados) nem pontuação
- [x] janela de direito coerente: `apos = 18/10/2021` é a vigência da LCE 1.100/2021, e `ate = 31/12/2099` é sentinela e é o valor certo **aqui**, porque o art. 32 é regra permanente e não fixa prazo de implementação
- [x] Trilho de cálculo conferido nos dois sentidos: o art. 24 dá "média aritmética simples das maiores remunerações [...] correspondentes a 80%" e o art. 27, II manda reajustar "nos termos estabelecidos para o RGPS" — fundam `tipo_calculo: Valor Médio` e `paridade: N`
- [x] `integral: S` coerente com `tipo_calculo: Valor Médio` sob a leitura corrente do catálogo; o art. 26 (proporcionalidade) não é citado nem vinculado
- [ ] A janela de admissão não grava o corte "após 31/12/2003" que os arts. 24 e 27, II declaram, e o par não particiona com `0035`/`0036`: [`achado-0028`](../achados/achado-0028.md)
- [ ] `fundamentacao` vazia aqui e preenchida na gêmea `regra-0037`: [`achado-0031`](../achados/achado-0031.md). Corrigir em qualquer direção deixa `sexo` como única divergência do par, que é o estado correto
- [ ] Idade (art. 32, I), tempo de contribuição (25 anos, II), 10 anos de efetivo exercício no serviço público (III) e 5 anos no cargo (IV) **não têm coluna** no Sisprev. A regra é `simulavel: S`, então o motor não afere nenhum dos quatro; criar coluna é alterar o sistema, fora do escopo da parametrização (Q5)
- [ ] A opção do § 16 do art. 40 da CF, exigida tanto pelo art. 25 quanto pelo art. 24, não tem coluna — a data de admissão sozinha nunca separa os dois trilhos de cálculo
- [ ] `nome` idêntico ao das outras três do grupo `0035`–`0038` e sem nada do trilho de cálculo: [`achado-0029`](../achados/achado-0029.md). É campo deployável, e a proposta pertence ao catálogo auditado
