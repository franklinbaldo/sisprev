---
type: Regra
id: regra-0021
row_index: 21
nome: Incapacidade · ingresso após 01/01/2004, requisitos a partir de 23/10/2021 · Ambos · proporcional · Proporcionalidade Dias
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
integral: N
tipo_calculo: Proporcionalidade Dias
fundamentacao: ''
---

# Estado da análise

Regime vigente — art. 40, § 1º, I da CF na redação da EC 103/2019 combinado
com a LCE 1.100/2021 —, para quem ingressou **após** 31/12/2003
(`data_adm_apos: 01/01/2004`), sem paridade (`paridade: N`), com proventos
proporcionais apurados em dias (`integral: N`,
`tipo_calculo: Proporcionalidade Dias`).

Esta regra e a `regra-0022` são o único par do catálogo cujo
`fundamentacao_integral` empacota **três fundamentações numa célula só**,
separadas por `|`. As três compartilham o mesmo tronco — o art. 40, § 1º, I
na redação da EC 103/2019 e os arts. 25 e 27, inciso I da LCE 1.100/2021 — e
divergem **apenas** no recorte do art. 30, conforme a classe de causa da
incapacidade:

| cláusula | classe de causa                       | recorte do art. 30 citado               |
| -------- | ------------------------------------- | --------------------------------------- |
| 1        | acidente em serviço                   | `§§ 5º e 6º` (definição e equiparações) |
| 2        | doença grave, contagiosa ou incurável | `§ 8º` (rol de 16 doenças)              |
| 3        | moléstia profissional                 | "artigo 30", sem recorte                |

Conferido contra o texto transcrito em `okf/dispositivos/lce-1100-2021/`, as
três cláusulas são **ramos alternativos, não cumulativos**. O *caput* do
art. 30 manda proventos proporcionais "exceto se a incapacidade for
decorrente de acidente em serviço, moléstia profissional ou doença grave,
contagiosa ou incurável": a lista é uma **enumeração disjuntiva**, e cada
classe basta sozinha para afastar a regra geral. Os §§ 5º/6º e o § 8º não se
somam — o § 5º define "acidente em serviço" e o § 6º lista o que a ele se
equipara; o § 8º arrola as dezesseis doenças graves. Definem **duas das três
classes da mesma exceção**, e um requerimento concreto entra por uma delas,
apurada em perícia. Não são condições que se acumulem para conceder o
benefício.

Daí o `dispositivos:` vazio, e ele é deliberado. A união achatada das três
cláusulas — sete provisões — não é a citação de nenhuma delas: seria uma
lista em que `§§ 5º/6º` e `§ 8º` aparecem lado a lado como se a regra se
fundasse nos dois ao mesmo tempo, quando cada um pertence a um ramo que o
outro exclui. O que resolve isso não é um vínculo mais fino, é a
**decomposição em uma linha por classe de causa material** (Q6, direção A
já decidida em [`q6-causa-incapacidade.md`](../../../docs/analysis/q6-causa-incapacidade.md)
§10) — ato humano ainda não praticado, e o único momento em que faz sentido
falar em `dispositivos:` aqui.

Um segundo obstáculo, independente da Q6 e mais estreito: a cláusula 3 cita
"artigo 30" **sem recorte**, e o artigo inteiro não está autorado. O bundle
tem `art-30-caput` e os §§ 1º, 2º, 5º, 6º e 8º, nunca `lce-1100-2021/art-30`.
Vincular o *caput* no lugar seria **estreitar** uma citação que a prosa
deixou larga — o inverso da convenção `ESTREITADA` (a prosa estreita, o
vínculo aponta a provisão inteira). O precedente contrário está na
`regra-0008`, cuja `fundamentacao_proporcional` cita "o artigo 20" sem
recorte e vincula `lce-432-2008/art-20/original`, documento do artigo
inteiro, que existe.

A conferência `critério → dispositivo` das sete regras restantes de
incapacidade está em
[`conferencia-criterio-dispositivo-incapacidade-restantes.md`](../../../docs/analysis/conferencia-criterio-dispositivo-incapacidade-restantes.md)
§2.4; o que segue registra o que ela apurou para esta regra.

- [x] As três cláusulas do `fundamentacao_integral` separadas pelo `|` e conferidas uma a uma contra o texto em `okf/dispositivos/lce-1100-2021/`
- [x] Ramos **alternativos**, não cumulativos: as três classes são a exceção disjuntiva do art. 30, *caput*, e cada uma basta sozinha
- [x] Tronco comum às três cláusulas isolado (art. 40, § 1º, I/EC 103/2019 + arts. 25 e 27, I); só o recorte do art. 30 varia
- [ ] `dispositivos:` mantido vazio — a união achatada das três cláusulas não é a citação de nenhuma delas. Depende da decomposição em linha por classe de causa (Q6, direção A)
- [ ] "artigo 30" sem recorte (cláusula 3) não tem dispositivo autorado: existem `art-30-caput` e os §§, não o artigo inteiro
- [ ] Nenhum dispositivo, em nenhum dos dois regimes estaduais, define "moléstia profissional" — a classe da cláusula 3 fica sem base transcrita (P-6)
- [ ] O único texto de fundamentação que esta regra carrega afirma "proventos integrais (cálculo por média)", e ela grava `integral: N` / `Proporcionalidade Dias`; `fundamentacao_proporcional` está vazia (`achado-0009`, aberto). Qual lado cede depende da Q7
- [ ] Os arts. 25 e 27, I citados pelas três cláusulas são, no próprio texto, do ramo "até 31 de dezembro de 2003"; esta regra é do ramo "após" (P-5). Os artigos do ramo correto — 24, 26 e 27, II — existem no bundle e não são citados
- [ ] `data_direito_apos: 23/10/2021` não é fundado por nenhum dispositivo citado: a LCE 1.100/2021 vige desde 18/10/2021 — publicação identificada na ficha oficial do SAPL como DOE/RO nº 207, de 18/10/2021 — e a EC 103/2019 desde 13/11/2019. O valor está cinco dias deslocado e é desta regra que ele sai; quais datas concretas ficam de fora depende da Q2. Ver [`achado-0024`](../achados/achado-0024.md)
- [ ] `nome` idêntico ao da `regra-0022` (`P1_NOME_REPETIDO`); o que separa as duas é só o resultado (`integral`, `tipo_calculo`), e o critério que o determina — a causa — não tem coluna. Q6
