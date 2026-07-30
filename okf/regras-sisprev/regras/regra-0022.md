---
type: Regra
id: regra-0022
row_index: 22
nome: Incapacidade · ingresso após 01/01/2004, requisitos a partir de 23/10/2021 · Ambos · integral · Valor Médio
tipo_de_beneficio: APOSENTADORIA POR INCAPACIDADE PERMANENTE
atualmente_no_sistema: 'TRUE'
ciclo_de_validacao: 1º
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
data_adm_apos: 01/01/2004 00:00
data_direito_ate: 31/12/2099 00:00
data_direito_apos: 23/10/2021 00:00
fundamentacao_proporcional: ''
visivel_dtc_proporcional: N
fundamentacao_integral: Aposentadoria por incapacidade permanente, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 40, § 1º, inciso I, da Constituição Federal, com redação dada pela Emenda Constitucional n. 103/2019 e os artigos 25 e 27, inciso I e 30, §§ 5° e 6º, da Lei Complementar Estadual nº 1.100/2021 (acidente em serviço com ingresso após 2003) | Aposentadoria por incapacidade permanente, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 40, § 1º, inciso I, da Constituição Federal, com redação dada pela Emenda Constitucional n. 103/2019 e os artigos 25 e 27, inciso I e 30, §8°, da Lei Complementar Estadual nº 1.100/2021 (doença grave, contagiosa ou incurável, com ingresso após 2003) | Aposentadoria por incapacidade permanente, com proventos integrais (cálculo por média) e sem paridade, com base no artigo 40, § 1º, inciso I, da Constituição Federal, com redação dada pela Emenda Constitucional n. 103/2019 e os artigos 25 e 27, inciso I e 30, da Lei Complementar Estadual nº 1.100/2021 (moléstia profissional com ingresso após 2003)
visivel_dtc_integral: N
sexo: AMBOS
integral: S
tipo_calculo: Valor Médio
fundamentacao: ''
---

# Estado da análise

Mesma família da `regra-0021` — art. 40, § 1º, I da CF na redação da EC
103/2019 com a LCE 1.100/2021, ingresso após 31/12/2003, sem paridade —, com
o resultado invertido: proventos integrais calculados por média
(`integral: S`, `tipo_calculo: Valor Médio`).

O frontmatter das duas é idêntico **exceto em quatro chaves**: `id`,
`row_index`, `integral` e `tipo_calculo`. Não formam grupo
`P2_IGUALDADE_MATERIAL_ATIVA` — `integral` e `tipo_calculo` são materiais e
as separam —, mas formam `P1_NOME_REPETIDO`, que não exige achado. Os dois
campos de fundamentação são byte-idênticos entre as duas.

O `fundamentacao_integral` empacota **três fundamentações numa célula só**,
separadas por `|`, com o mesmo tronco nas três — o art. 40, § 1º, I na
redação da EC 103/2019 e os arts. 25 e 27, inciso I da LCE 1.100/2021 —,
variando **apenas** o recorte do art. 30 conforme a classe de causa:

| cláusula | classe de causa                       | recorte do art. 30 citado               |
| -------- | ------------------------------------- | --------------------------------------- |
| 1        | acidente em serviço                   | `§§ 5º e 6º` (definição e equiparações) |
| 2        | doença grave, contagiosa ou incurável | `§ 8º` (rol de 16 doenças)              |
| 3        | moléstia profissional                 | "artigo 30", sem recorte                |

Conferido contra o texto transcrito em `okf/dispositivos/lce-1100-2021/`, as
três são **ramos alternativos, não cumulativos**: o *caput* do art. 30 manda
proventos proporcionais "exceto se a incapacidade for decorrente de acidente
em serviço, moléstia profissional ou doença grave, contagiosa ou incurável"
— enumeração disjuntiva, cada classe bastando sozinha. Os §§ 5º/6º e o § 8º
definem **duas das três classes da mesma exceção**; não se somam, e um
requerimento entra por uma delas.

É por isso que `dispositivos:` segue vazio, aqui como na irmã: a união
achatada das três cláusulas poria `§§ 5º/6º` e `§ 8º` lado a lado como se a
regra se fundasse nos dois ao mesmo tempo, quando cada um pertence a um ramo
que o outro exclui. O que resolve é a **decomposição em uma linha por classe
de causa material** (Q6, direção A já decidida em
[`q6-causa-incapacidade.md`](../../../docs/analysis/q6-causa-incapacidade.md)
§10), ato humano ainda não praticado. Some-se a isso que a cláusula 3 cita
"artigo 30" sem recorte e o artigo inteiro **não está autorado** — o bundle
tem `art-30-caput` e os §§, nunca `lce-1100-2021/art-30`.

Uma diferença em relação à `regra-0021` merece registro, porque inverte o
sinal de um defeito: o texto compartilhado afirma "proventos integrais
(cálculo por média) e sem paridade", e é **esta** regra que ele descreve —
`integral: S`, `Valor Médio`, `paridade: N`. A `regra-0021` carrega o mesmo
texto contradizendo os próprios valores. Aqui o campo e o cadastro concordam
quanto ao resultado; o que não fecha é a **base citada** dele: quem funda a
média das 80% maiores é o art. 24 (ingresso após 31/12/2003), e a
fundamentação cita o art. 25, que é o do valor efetivo para quem ingressou
até 2003.

A conferência `critério → dispositivo` está em
[`conferencia-criterio-dispositivo-incapacidade-restantes.md`](../../../docs/analysis/conferencia-criterio-dispositivo-incapacidade-restantes.md)
§2.4.

## O que a reconferência de 2026-07-29 fechou

A conferência acima apoiava-se no texto transcrito em `okf/dispositivos/`.
Reconferida contra a **compilação oficial** da LCE 1.100/2021
(`fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt`, `sha256` no
manifesto), a **P-5 deixou de ser suspeita e passou a ser conferida** — e o que
a fechou foi um dispositivo que antes não estava disponível.

O corte temporal está **literal no corpo de cada artigo**, com a mesma data e as
mesmas duas preposições: art. 24 para "quem ingressou **após** 31 de dezembro de
2003" (média das 80% maiores = o `Valor Médio` desta regra), art. 25 para
"**até** 31 de dezembro de 2003" (totalidade da remuneração = `Valor Efetivo`),
art. 27, I e II a mesma partição para o reajuste. Não é interpretação
sistemática: cada artigo nomeia a sua classe.

E os **§§ 13 e 14 do art. 30** — que a conferência anterior citou como o que
faltava para concluir, e que **não estão transcritos no bundle** — roteiam o
cálculo: o § 13 manda calcular "na forma do art. 24" quando a incapacidade
decorre de acidente em serviço, moléstia profissional ou doença grave, que são
**exatamente as três classes das três cláusulas desta regra**. Duas provas
independentes, portanto, de que a base desta regra é o art. 24: o corte do
próprio art. 24 e o roteamento do § 13.

Logo as três cláusulas citam, todas, os dois artigos do **ramo temporal
oposto** — os que fundam a irmã `regra-0019` —, e omitem os dois que
correspondem aos valores gravados aqui. Está autorado em
[`achado-0023`](../achados/achado-0023.md).

- [x] As três cláusulas do `fundamentacao_integral` separadas pelo `|` e conferidas uma a uma contra o texto em `okf/dispositivos/lce-1100-2021/`
- [x] Ramos **alternativos**, não cumulativos: as três classes são a exceção disjuntiva do art. 30, *caput*, e cada uma basta sozinha
- [x] Diferença material em relação à `regra-0021` isolada: dois campos, `integral` e `tipo_calculo` — não há grupo `P2_IGUALDADE_MATERIAL_ATIVA`
- [x] Reconferido contra a compilação oficial da LCE 1.100/2021, não só contra o corpus: o corte "até/após 31 de dezembro de 2003" é literal nos arts. 24, 25 e 27, e o art. 30, § 13 roteia esta hipótese ao art. 24
- [ ] `dispositivos:` mantido vazio — a união achatada das três cláusulas não é a citação de nenhuma delas. Depende da decomposição em linha por classe de causa (Q6, direção A)
- [ ] "artigo 30" sem recorte (cláusula 3) não tem dispositivo autorado: existem `art-30-caput` e os §§, não o artigo inteiro. Pode ser, aliás, a citação **honesta** dessa classe, se a norma não oferecer nível mais fino para ela
- [ ] "Moléstia profissional" não é definida em nenhum dos dois regimes estaduais, embora as outras duas classes da mesma enumeração o sejam no mesmo artigo — [`achado-0025`](../achados/achado-0025.md) (P-6). Falta pesquisar decreto/regulamento estadual e eventual remissão à legislação federal
- [ ] `tipo_calculo: Valor Médio` é fundado pelo art. 24 (ingresso **após** 2003), não pelo art. 25 que a fundamentação cita; e `paridade: N` é fundada pelo art. 27, **II**, não pelo 27, I citado. **A conferência está fechada** (P-5, [`achado-0023`](../achados/achado-0023.md)); o que segue aberto é qual lado cede, e isso é decisão de quem responde por campo deployável
- [ ] `integral: S` decorre da exceção do art. 30, *caput* — dispositivo que existe no bundle e que nenhuma das quatro regras do regime vigente cita, embora todas citem as suas exceções
- [ ] `data_direito_apos: 23/10/2021` não é fundado por nenhum dispositivo citado — "23 de outubro" aparece **zero vezes** no texto oficial da lei — [`achado-0024`](../achados/achado-0024.md). O lado do erro **deixou de ser indeterminado**: a publicação está identificada na ficha oficial do SAPL como DOE/RO nº 207, de 18/10/2021, e não apenas a assinatura, logo o valor está cinco dias deslocado e é desta regra que ele sai. Quais datas concretas ficam de fora depende da semântica de `DATA_DIREITO_APOS` (Q2)
- [ ] `data_adm_apos: 01/01/2004` desloca a cobertura um dia: sob `APOS` exclusivo esta regra só alcança admissões a partir de 02/01/2004, enquanto a `regra-0019` fecha em 31/12/2003 — **o dia 01/01/2004 fica sem regra de incapacidade**, e a lei atribui esse dia ao ramo pós-2003. Ver [`achado-0024`](../achados/achado-0024.md)
- [ ] `nome` idêntico ao da `regra-0021` (`P1_NOME_REPETIDO`); o critério que separa as duas — a causa da incapacidade — não tem coluna. Q6. Com `simulavel: S` nas duas, o motor não tem predicado que decida entre elas — [`achado-0026`](../achados/achado-0026.md)
- [ ] §§ 13 e 14 do art. 30 a transcrever: roteiam o cálculo do benefício nos dois ramos e não existem como dispositivo autorado. Ato de transcrição, não edição de regra
