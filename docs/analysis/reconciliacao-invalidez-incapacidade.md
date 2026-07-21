# Reconciliação as-is × to-be — Aposentadoria por Invalidez / Incapacidade Permanente

> **Nota:** Relatório gerado por IA como apoio à decisão. **Não é artefato
> oficial** e não edita nenhuma regra nem achado. Cruza as regras hoje no
> sistema (as-is, `okf/regras-sisprev/regras/`) com a análise da PGE-RO
> (to-be, aba "Invalidezincapacidade permanent" de
> `data/raw/xlsx/invalidezincapacidade-permanent.csv`). A análise da PGE
> **também tem erros próprios** (ver §4) — é insumo, não verdade. Toda
> mudança final vai in-place nos `regra-*.md`. **Parte** da análise da PGE —
> correções já individualizadas de flag, cálculo e fundamentação — cabe nos
> campos que o Sisprev já tem (`sexo`, `integral`, `paridade`, `tipo_calculo`
> e `fundamentacao*`, este no frontmatter). **Mas nem tudo se resolve assim:**
> o cruzamento 0022 × P6/P7 (§2) expõe uma **fronteira ainda não resolvida** —
> a "causa da incapacidade", pela qual a PGE separa hipóteses, **não está nas
> 27 colunas**. Ainda é preciso descobrir se essa seleção acontece em
> código/tabela externa, em verificação manual, ou se é lacuna real do
> modelo — hipótese em que **um campo novo poderia ser necessário**. A
> eventual inativação é registrada nos campos administrativos `status_regra` /
> `motivo_inativacao`, nunca reaproveitando `atualmente_no_sistema`.

## 1. Os dois lados

**As-is — 11 regras de invalidez/incapacidade no sistema:** 0001, 0002,
0004, 0006, 0007, 0008, 0009, 0019, 0020, 0021, 0022.

**To-be — 8 hipóteses da PGE** (numeradas **1–7 e 9** na planilha — a **8ª
não existe**, ver §4), organizadas por regime legal × causa × ingresso:

| #   | Hipótese PGE                      | Regime / ingresso                 | Causa                              | Cálculo                                    | Paridade            |
| --- | --------------------------------- | --------------------------------- | ---------------------------------- | ------------------------------------------ | ------------------- |
| P1  | LCE 432/2008 — após 2003          | EC 41/2003; ingresso > 31/12/2003 | acidente/moléstia/doença grave     | integral, por **média** (art. 45)          | Não (RGPS)          |
| P2  | LCE 432/2008 — após 2003          | idem                              | doença **não** catalogada          | **proporcional** (média art. 45 + art. 17) | Não (RGPS)          |
| P3  | EC 41/2003 art. 6º-A — antes 2004 | ingresso ≤ 31/12/2003             | sem acidente/moléstia/doença grave | **proporcional**, última remuneração       | **Sim**             |
| P4  | EC 41/2003 art. 6º-A — antes 2004 | idem                              | acidente/moléstia/doença grave     | integral, última remuneração               | **Sim**             |
| P5  | LC 1.100/2021 — antes 2004        | ingresso ≤ 31/12/2003             | acidente/moléstia/doença grave     | integral, totalidade (art. 25)             | **Sim** (art. 27 I) |
| P6  | LC 1.100/2021 — após 2003         | ingresso > 31/12/2003             | doença grave/contagiosa/incurável  | integral, por **média** (art. 24)          | Não (RGPS)          |
| P7  | LC 1.100/2021 — após 2003         | idem                              | **acidente em serviço**            | integral, por **média** (art. 24)          | Não (RGPS)          |
| P9  | LC 1.100/2021 — após 2003         | idem                              | sem acidente/moléstia/doença grave | **proporcional** (fração art. 26 s/ média) | Não (RGPS)          |

**Headline: 11 regras as-is → 8 hipóteses to-be, mas com lacunas dos dois
lados** — o as-is carrega regimes antigos (pré-EC 20, EC 20) que a PGE não
modelou; a PGE separa por *causa da incapacidade*, o que o Sisprev não tem
como campo de seleção.

## 2. Mapa as-is → to-be + classe do match

**Classes controladas** (só "match limpo" quando **todos** os eixos
relevantes — regime, ingresso, cálculo, paridade, fundamentação — estão
confirmados):

- **match limpo** — todos os eixos confirmados; segue direto.
- **match parcial** — mapeamento provável, mas com um ou mais eixos
  pendentes de confirmação.
- **indeterminado** — sem contraparte clara, ou uma regra cobre várias
  hipóteses / nenhuma.
- **contradição** — conflito interno (flag×texto) ou as-is×PGE.

| as-is                                                  | campos as-is                                                                   | → PGE         | Classe            | O que falta confirmar / observação                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **0006** (int S, `Valor Médio`, par N)                 | Art. 40 §1 I EC 41 + LC 432                                                    | **P1**        | **match limpo**   | Regime, cálculo (`Valor Médio`↔média), sem paridade e ingresso (após 2003) todos alinhados.                                                                                                                                                                                                                                                                                      |
| **0007** (int N, `Proporcionalidade Dias`, par N)      | idem                                                                           | **P2**        | **match parcial** | Confirmar que 0007 representa a causa "doença **não** catalogada" (P2) e que `Proporcionalidade Dias` ↔ o proporcional da P2 (média art. 45 + art. 17).                                                                                                                                                                                                                          |
| **0009** (int N, `Remuneração de Contribuição`, par S) | 6º-A EC 41 (EC 70) + LC 432                                                    | **P3**        | **match parcial** | Confirmar `Remuneração de Contribuição` ↔ "última remuneração" (P3).                                                                                                                                                                                                                                                                                                             |
| **0008** (int S, `Remuneração de Contribuição`, par S) | 6º-A EC 41; campo `fundamentacao_integral` cita Art. 40 §1 III 2ª parte EC 103 | **P4**        | **match parcial** | Confirmar `Remuneração de Contribuição` ↔ "última remuneração"; **além disso** 0008 coincide com a P4 justamente na citação suspeita "Art. 40 §1 III 2ª parte" para incapacidade (ver §4) — a coincidência não valida a citação, só herda a mesma tensão.                                                                                                                        |
| **0019** (int S, `Valor Efetivo`, par S)               | Art. 40 §1 I EC 103 + LC 1.100, "Até 31/12/2003"                               | **P5**        | **match parcial** | Confirmar `Valor Efetivo` ↔ "integralidade, totalidade da remuneração" (P5).                                                                                                                                                                                                                                                                                                     |
| **0022** (int S, `Valor Médio`, par N)                 | Art. 40 §1 I EC 103 + LC 1.100, "Após 31/12/2003"                              | **P6 + P7**   | **indeterminado** | Uma regra cobre **duas** hipóteses PGE (doença grave × acidente em serviço). A PGE separa por "causa da incapacidade", que **não** é uma das 27 colunas. Fronteira não resolvida — três alternativas, **sem escolher aqui**: (a) a seleção ocorre em código/tabela externa ao catálogo; (b) é verificação manual; (c) é lacuna real do modelo (poderia então exigir campo novo). |
| **0021** (int N, `Proporcionalidade Dias`, par N)      | idem, "Após 31/12/2003"                                                        | **P9**        | **contradição**   | Célula alinha (proporcional, sem paridade, após 2003), **mas** `integral: N` com a fundamentação afirmando "proventos **integrais** (cálculo por média)" — contradição flag×texto (já registrada como F2 no ciclo 1). Resolver contra a fonte.                                                                                                                                   |
| **0020** (int N, `Proporcionalidade Dias`, par S)      | Art. 40 §1 I EC 103 + LC 1.100, "Até 31/12/2003"                               | **(nenhuma)** | **indeterminado** | Célula órfã: proporcional + **com paridade** + antes 2004 + LC 1.100 — a PGE só tem P5 (integral/paridade) nesse ramo. Além disso o campo `fundamentacao_integral` é o texto **integral** da 0019 copiado (int=N sem fundamentação proporcional própria). Resolver contra a fonte.                                                                                               |
| **0001** (int S, `Valor Efetivo`, par S)               | Art. 40 I **texto original** (pré-EC 20)                                       | **(nenhuma)** | **indeterminado** | Regime antigo sem contraparte no to-be — ver §3.                                                                                                                                                                                                                                                                                                                                 |
| **0002** (int N, `Valor Efetivo`, par S)               | idem                                                                           | **(nenhuma)** | **indeterminado** | Par proporcional da 0001 (difere **só** no flag `integral`; mesmo `tipo_calculo`) — ver §3 e §5.                                                                                                                                                                                                                                                                                 |
| **0004** (int '', `Não identificado`, par S)           | Art. 40 §1 I EC 20/98 (campos vazios)                                          | **(nenhuma)** | **indeterminado** | Regime EC 20 com campos estruturais vazios (já em achado-0008). Sem contraparte — ver §3.                                                                                                                                                                                                                                                                                        |

## 3. Lacuna de cobertura: regimes antigos ausentes do to-be

A PGE modelou apenas os regimes **EC 41/2003 (após 2003 e 6º-A)** e **EC
103/2019 / LC 1.100/2021**. As regras **0001, 0002 (Art. 40 I original,
pré-EC 20)** e **0004 (EC 20/1998)** **não têm hipótese correspondente** no
to-be.

**Pergunta a confirmar juridicamente (não presumir):** qual data rege a
aposentadoria por invalidez/incapacidade — a do fato gerador (a incapacidade)
ou a da admissão? Isto precisa de fonte jurídica primária. *Se* for confirmado
que a incapacidade pode se dar sob regime anterior mesmo para quem ingressou
há muito tempo, esses regimes antigos podem ainda estar vivos — e a ausência
deles no to-be seria uma lacuna do modelo da PGE, não um sinal de extinção.
No cenário oposto (regimes de fato extintos), a ação seria inativar
0001/0002/0004 via `status_regra` / `motivo_inativacao`. Decidir contra a
fonte, sem presumir a resposta.

## 4. Tensões e erros na própria análise da PGE (não copiar cegamente)

- **A numeração pula a hipótese 8**: a planilha lista 1, 2, 3, 4, 5, 6, 7 e
  **9** — não há hipótese "8". Ou uma hipótese foi removida sem renumerar, ou
  falta uma célula. Conferir se um ramo faltante deveria existir.
- **P4/linha 4 cita "Art. 40, §1º, III, segunda parte" descrevendo
  incapacidade** — tensão observável **dentro da própria planilha**, sem
  juízo jurídico externo: (i) a P4 descreve incapacidade; (ii) cita o inciso
  **III, segunda parte**; (iii) todas as demais hipóteses de incapacidade
  (P1, P2, P3, P5, P6, P7, P9) citam o §1º, **inciso I**. Qual interpretação
  jurídica está correta — se o inciso III, 2ª parte, se aplica aqui ou se é
  citação trocada — permanece **para confirmação em fonte primária**; não
  corrigir por presunção. A regra as-is 0008 herda exatamente essa citação.
- **P5 e P6 repetem a fundamentação final apesar de cálculo e paridade
  distintos**: ambas citam *"artigos 25 e 27, inciso I e 30, §8°"*, embora P5
  seja **integral, totalidade (art. 25), com paridade, antes de 2004** e P6
  seja **integral por média (art. 24), sem paridade, após 2003**. **P6 é o
  caso mais evidente**: sendo sem paridade e com reajuste RGPS (art. 27,
  **II**), citar o art. 27, **I** (paridade) e o art. 25 (totalidade, não a
  média do art. 24) contradiz a própria hipótese — base provavelmente copiada
  da P5. Usar a base correta ao destilar, após confirmação.

## 5. Split integral/proporcional só no flag (rastreabilidade)

Pares que existem só para separar integral de proporcional, distinguidos
**apenas pelo campo `integral`** (mesmo `tipo_calculo` e mesma fundamentação):

- **0001 (S) / 0002 (N)** — ambas `Valor Efetivo`; a metade proporcional
  (0002) herda o cálculo da integral.
- **0008 (S) / 0009 (N)** — ambas `Remuneração de Contribuição`.

Nos demais pares (0006/0007, 0019/0020, 0021/0022) o `tipo_calculo` também
muda, o que é mais coerente. Ponto de auditoria: onde o par difere **só** no
flag, confirmar que a fundamentação de cada metade explicita a hipótese
(integral vs proporcional), hoje implícita só no `integral`.

## 6. `tipo_calculo` a confirmar contra a nomenclatura da PGE

- `Remuneração de Contribuição` (0008/0009) ↔ PGE "última remuneração do
  cargo efetivo" (P3/P4) — confirmar se são o mesmo cálculo.
- `Valor Efetivo` (0019) ↔ PGE "integralidade, totalidade da remuneração"
  (P5) — confirmar equivalência.
- `Valor Médio` (0006, 0022) ↔ PGE "cálculo por média" (P1, P6/P7) — único
  eixo de cálculo confirmado.

## 7. Fila de decisões humanas

Cada linha é uma decisão a tomar contra a fonte (norma / PGE / Sisprev),
**não** uma conclusão. "Fronteira" = a decisão não é sobre um campo, mas
sobre onde a regra de seleção vive.

| Regra / hipótese             | Classificação            | Campo ou fronteira afetada                                  | Evidência favorável                                              | Evidência contrária                                                                                                 | Fonte adicional necessária                                                                                     |
| ---------------------------- | ------------------------ | ----------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| 0007 → P2                    | match parcial            | `integral` / causa                                          | proporcional, sem paridade, EC 41/LC 432 após 2003 batem         | nenhum campo atesta "doença não catalogada"; `Proporcionalidade Dias` não confirmado como o proporcional da P2      | PGE/norma: 0007 é a hipótese "doença não catalogada"? mapeamento do cálculo?                                   |
| 0008 → P4                    | match parcial            | `tipo_calculo`, `fundamentacao_integral`                    | integral, com paridade, 6º-A EC 41, antes 2004 batem             | `Remuneração de Contribuição` não confirmado = "última remuneração"; herda a citação suspeita III 2ª parte (ver §4) | equivalência de cálculo + base legal correta da hipótese                                                       |
| 0009 → P3                    | match parcial            | `tipo_calculo`                                              | proporcional, com paridade, 6º-A EC 41 batem                     | `Remuneração de Contribuição` não confirmado = "última remuneração"                                                 | equivalência de cálculo                                                                                        |
| 0019 → P5                    | match parcial            | `tipo_calculo`                                              | integral, paridade, LC 1.100 antes 2004 batem                    | `Valor Efetivo` não confirmado = "integralidade/totalidade"                                                         | equivalência de cálculo                                                                                        |
| 0020                         | indeterminado            | `integral` / `fundamentacao_integral`                       | é a metade proporcional do ramo LC 1.100 antes 2004              | PGE não tem célula proporcional nesse ramo (só P5 integral); campo copiado da 0019                                  | existe base para proporcional-com-paridade antes 2004? ou 0020 é resíduo?                                      |
| 0021 → P9                    | contradição              | `integral` × fundamentação                                  | célula proporcional / sem paridade / após 2003 bate a P9         | `integral: N` mas a fundamentação diz "proventos integrais"                                                         | qual dado está certo (flag ou texto), contra a fonte                                                           |
| 0022 → P6/P7                 | indeterminado            | **fronteira** "causa da incapacidade" (fora das 27 colunas) | integral, média, sem paridade, após 2003 batem as duas hipóteses | uma regra para duas hipóteses; nenhum campo separa doença grave × acidente                                          | onde a seleção por causa acontece: (a) código/tabela externa; (b) manual; (c) lacuna do modelo (→ campo novo?) |
| 0001 / 0002 / 0004           | indeterminado            | cobertura de regime                                         | são regimes reais (pré-EC 20 / EC 20) presentes no as-is         | o to-be da PGE não os modela                                                                                        | qual data rege a invalidez (fonte primária) e se os regimes ainda alcançam alguém (§3)                         |
| Numeração P8 ausente         | indeterminado (lado PGE) | completude do to-be                                         | a planilha lista 1–7 e 9                                         | não há hipótese "8"                                                                                                 | PGE: falta uma hipótese ou foi removida sem renumerar?                                                         |
| Fundamentação P5/P6 repetida | contradição (lado PGE)   | base legal da P6                                            | —                                                                | P6 (sem paridade, média art. 24) cita a base da P5 (paridade, art. 25)                                              | PGE: base correta da P6 antes de destilar                                                                      |

## 8. Resumo executivo (para autoria in-place)

- **Match limpo (segue):** 0006 → P1.
- **Match parcial (confirmar o eixo pendente antes de seguir):** 0007 → P2
  (doença não catalogada + cálculo proporcional); 0009 → P3 e 0008 → P4
  (`Remuneração de Contribuição` ↔ última remuneração; 0008 herda a citação
  suspeita da P4); 0019 → P5 (`Valor Efetivo` ↔ totalidade).
- **Contradição (resolver contra a fonte):** 0021 (flag×texto).
- **Indeterminado:** 0022 (cobre P6+P7, split por causa sem campo no
  Sisprev); 0020 (célula órfã proporcional-antes-2004 + campo copiado da
  0019); 0001/0002/0004 (regimes antigos sem contraparte — ver §3).
- **Não copiar da PGE sem conferir:** numeração pula a 8; P4 cita III 2ª
  parte para incapacidade; P5/P6 repetem a base apesar de cálculo/paridade
  distintos (P6 o mais evidente).

As correções já individualizadas (flags, cálculo, fundamentação) cabem nos
campos que o Sisprev já tem; a inativação, quando o caso, nos campos
administrativos. **Mas o catálogo não resolve tudo:** a seleção por "causa da
incapacidade" (0022 × P6/P7) é uma fronteira aberta — pode viver em
código/tabela externa, em verificação manual, ou ser lacuna do modelo que
exija um campo novo. Isso precisa ser descoberto contra a fonte, não presumido.
