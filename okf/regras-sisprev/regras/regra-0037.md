---
type: Regra
id: regra-0037
row_index: 37
nome: Voluntária · pedido a partir de 18/10/2021 · Masculino
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
sexo: MASCULINO
integral: S
tipo_calculo: Valor Médio
fundamentacao: Art. 24 da Lei Complementar 1.100 de 18 de outubro de 2021
dispositivos:
  - /dispositivos/cf88/art-40-par-1-inc-iii/ec-103-2019.md
  - /dispositivos/lce-1100-2021/art-24/original.md
  - /dispositivos/lce-1100-2021/art-27-inc-ii/original.md
  - /dispositivos/lce-1100-2021/art-32/original.md
---

# Estado da análise

Aposentadoria voluntária comum do **regime permanente** da LCE 1.100/2021, pelo
**trilho da média**: proventos pela média aritmética simples das 80% maiores
remunerações (`tipo_calculo: Valor Médio`) e reajuste nos termos do RGPS
(`paridade: N`), por força dos arts. 24 e 27, II. A `regra-0038` é a mesma regra
no feminino.

Cálculo, reajuste e `sexo` fecham. **A janela de admissão não.** Os dois
dispositivos do trilho delimitam a sua clientela pela mesma cláusula literal —
servidor "que tenha ingressado no serviço público em cargo efetivo **após** 31
de dezembro de 2003" — e esta regra grava `data_adm_apos: 01/01/1910` e
`data_adm_ate: 31/12/2099`, isto é, corte nenhum nos dois eixos. Com as gêmeas
de trilho complementar `0035`/`0036` (`data_adm_ate: 31/12/2003`), quem
ingressou antes de 2004 é alcançado pelos quatro registros:
[`achado-0028`](../achados/achado-0028.md).

`integral: S` com `tipo_calculo: Valor Médio` **não** é contradição: é a leitura
corrente do catálogo, em que `integral` significa "100% da base apurada, seja
ela a remuneração do cargo ou a média" — seis outras regras usam a mesma
construção "proventos integrais (cálculo por média)" com `integral: S`.

- [x] Critérios do cadastro percorridos um a um contra a LCE 1.100/2021, na compilação oficial arquivada (`fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt`) — não apenas contra o texto transcrito no corpus
- [x] `dispositivos:` conferido contra `fundamentacao_integral` item a item: os quatro dispositivos citados estão vinculados, nada a acrescentar nem a remover
- [x] `sexo` é critério que o dispositivo funda: o art. 32, I exige "62 (sessenta e dois) anos de idade, se mulher, e 65 (sessenta e cinco) anos de idade, se homem" — o documento do art. 32 no corpus transcreve o artigo **inteiro**, incisos I a IV inclusive
- [x] `apos_especial: N` e `tabelapontuacao: N`: nenhum dispositivo citado institui especialidade (§§ 4º-A/4º-B/4º-C/5º do art. 40 da CF não são citados) nem pontuação
- [x] janela de direito coerente: `apos = 18/10/2021` é a vigência da LCE 1.100/2021, e `ate = 31/12/2099` é sentinela e é o valor certo **aqui**, porque o art. 32 é regra permanente e não fixa prazo de implementação
- [x] Trilho de cálculo conferido nos dois sentidos: o art. 24 dá "média aritmética simples das maiores remunerações [...] correspondentes a 80%" e o art. 27, II manda reajustar "nos termos estabelecidos para o RGPS" — fundam `tipo_calculo: Valor Médio` e `paridade: N`
- [x] `integral: S` coerente com `tipo_calculo: Valor Médio` sob a leitura corrente do catálogo; o art. 26 (proporcionalidade) não é citado nem vinculado
- [x] `fundamentacao: "Art. 24 da Lei Complementar 1.100 de 18 de outubro de 2021"` lido por humano: a norma é inequívoca e o art. 24 **já** está vinculado. Fecha a pendência `LEITURA-HUMANA` desta regra na [lista congelada](../../../docs/analysis/pendencias-de-citacao-congeladas.md), sem vínculo novo
- [ ] A janela de admissão não grava o corte "após 31/12/2003" que os arts. 24 e 27, II declaram, e o par não particiona com `0035`/`0036`: [`achado-0028`](../achados/achado-0028.md). `DATA_ADM_APOS` é deployável — a decisão é de quem responde pelo campo
- [ ] `fundamentacao` preenchida aqui e **vazia** na gêmea `regra-0038`: [`achado-0031`](../achados/achado-0031.md). Dos dois únicos pares do catálogo com essa assimetria, este é um
- [ ] Idade (art. 32, I), tempo de contribuição (25 anos, II), 10 anos de efetivo exercício no serviço público (III) e 5 anos no cargo (IV) **não têm coluna** no Sisprev. A regra é `simulavel: S`, então o motor não afere nenhum dos quatro; criar coluna é alterar o sistema, fora do escopo da parametrização (Q5)
- [ ] A opção do § 16 do art. 40 da CF, exigida tanto pelo art. 25 quanto pelo art. 24, não tem coluna — a data de admissão sozinha nunca separa os dois trilhos de cálculo
- [ ] `nome` idêntico ao das outras três do grupo `0035`–`0038` e sem nada do trilho de cálculo: [`achado-0029`](../achados/achado-0029.md). É campo deployável, e a proposta pertence ao catálogo auditado
