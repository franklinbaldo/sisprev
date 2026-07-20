# Reconciliação as-is × to-be — Aposentadoria por Invalidez / Incapacidade Permanente

> **Nota:** Relatório gerado por IA como apoio à decisão. **Não é artefato
> oficial** e não edita nenhuma regra nem achado. Cruza as regras hoje no
> sistema (as-is, `okf/regras-sisprev/regras/`) com a análise da PGE-RO
> (to-be, aba "Invalidezincapacidade permanent" de
> `data/raw/xlsx/invalidezincapacidade-permanent.csv`). A análise da PGE
> **também tem erros próprios** (ver §4) — é insumo, não verdade. Toda
> mudança final vai in-place nos `regra-*.md`, **só nos campos que o Sisprev
> já tem**: a riqueza da PGE (causa da incapacidade, doença catalogada,
> forma de reajuste, artigos decompostos) destila para os valores corretos
> dos campos existentes (`sexo`, `integral`, `paridade`, `tipo_calculo`) e
> para os campos `fundamentacao*` do frontmatter — não vira campo novo. A
> fundamentação legal já mora no frontmatter (não no corpo). A eventual
> inativação é registrada nos campos administrativos `status_regra` /
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

## 2. Mapa as-is → to-be + ação sugerida

| as-is                                                  | campos as-is                                          | → PGE         | Situação / ação sugerida (você autora)                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------ | ----------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **0006** (int S, `Valor Médio`, par N)                 | Art. 40 §1 I EC 41 + LC 432                           | **P1**        | ✅ Match limpo (integral, média, sem paridade, após 2003). Conferir.                                                                                                                                                                                                                                                |
| **0007** (int N, `Proporcionalidade Dias`, par N)      | idem                                                  | **P2**        | ✅ Match limpo (proporcional, sem paridade). Conferir se cobre "doença não catalogada".                                                                                                                                                                                                                             |
| **0009** (int N, `Remuneração de Contribuição`, par S) | 6º-A EC 41 (EC 70) + LC 432                           | **P3**        | ✅ Match (proporcional, paridade, antes 2004).                                                                                                                                                                                                                                                                      |
| **0008** (int S, `Remuneração de Contribuição`, par S) | 6º-A EC 41; corpo cita Art. 40 §1 III 2ª parte EC 103 | **P4**        | ✅ Match (integral, paridade, antes 2004).                                                                                                                                                                                                                                                                          |
| **0019** (int S, `Valor Efetivo`, par S)               | Art. 40 §1 I EC 103 + LC 1.100, "Até 31/12/2003"      | **P5**        | ✅ Match (integral, paridade, antes 2004, LC 1.100).                                                                                                                                                                                                                                                                |
| **0022** (int S, `Valor Médio`, par N)                 | Art. 40 §1 I EC 103 + LC 1.100, "Após 31/12/2003"     | **P6 + P7**   | ⚠️ **Uma regra cobre duas hipóteses PGE** (doença grave × acidente em serviço). A PGE separa por causa; o Sisprev não tem campo "causa da incapacidade" → o split provavelmente vive fora do catálogo. Confirmar se 0022 basta ou se precisa desdobrar.                                                             |
| **0021** (int N, `Proporcionalidade Dias`, par N)      | idem, "Após 31/12/2003"                               | **P9**        | 🔴 Match de célula (proporcional, sem paridade, após 2003), **mas** `integral: N` com a fundamentação afirmando "proventos **integrais** (cálculo por média)" — contradição flag×texto (já registrada como F2 no ciclo 1). Resolver contra a fonte.                                                                 |
| **0020** (int N, `Proporcionalidade Dias`, par S)      | Art. 40 §1 I EC 103 + LC 1.100, "Até 31/12/2003"      | **(nenhuma)** | 🔴 Célula órfã: proporcional + **com paridade** + antes 2004 + LC 1.100. A PGE só tem P5 (integral/paridade) nesse ramo — não há versão proporcional. Além disso o corpo (`fundamentacao_integral`) é o texto **integral** da 0019 copiado (int=N sem fundamentação proporcional própria). Resolver contra a fonte. |
| **0001** (int S, `Valor Efetivo`, par S)               | Art. 40 I **texto original** (pré-EC 20)              | **(nenhuma)** | 🟡 Regime antigo sem contraparte PGE — ver §3.                                                                                                                                                                                                                                                                      |
| **0002** (int N, `Valor Efetivo`, par S)               | idem                                                  | **(nenhuma)** | 🟡 Par proporcional da 0001 (difere **só** no flag `integral`; mesmo `tipo_calculo`) — ver §3 e §5.                                                                                                                                                                                                                 |
| **0004** (int '', `Não identificado`, par S)           | Art. 40 §1 I EC 20/98 (campos vazios)                 | **(nenhuma)** | 🟡 Regime EC 20 com campos estruturais vazios (já em achado-0008). Sem contraparte PGE — ver §3.                                                                                                                                                                                                                    |

## 3. Lacuna de cobertura: regimes antigos ausentes do to-be

A PGE modelou apenas os regimes **EC 41/2003 (após 2003 e 6º-A)** e **EC
103/2019 / LC 1.100/2021**. As regras **0001, 0002 (Art. 40 I original,
pré-EC 20)** e **0004 (EC 20/1998)** **não têm hipótese correspondente** no
to-be.

Como a aposentadoria por invalidez se rege pela data do **fato gerador
(incapacidade)** e não só pela admissão, esses regimes antigos podem ainda
alcançar servidores de ingresso muito anterior. **Questão a investigar:**
esses regimes estão extintos na prática (ninguém mais se aposenta por eles) —
caso em que a ação seria inativar 0001/0002/0004 via `status_regra` /
`motivo_inativacao` — ou o modelo da PGE está **incompleto** para o legado e
precisa ganhar as hipóteses pré-EC 41? Decidir contra a fonte, não presumir.

## 4. Erros na própria análise da PGE (não copiar cegamente)

- **A numeração pula a hipótese 8**: a planilha lista 1, 2, 3, 4, 5, 6, 7 e
  **9** — não há hipótese "8". Ou uma hipótese foi removida sem renumerar, ou
  falta uma célula. Conferir se o ramo faltante (p.ex. "moléstia profissional
  isolada" ou "acidente antes de 2004 LC 1.100") deveria existir.
- **Base legal da P6 copiada da P5**: a P6 (doença grave, **após 2003**, LC
  1.100, **sem paridade**) cita *"artigos 25 e 27, inciso I e 30, §8°"* —
  idêntico à P5 (antes 2004, integral, **com paridade**). Mas P6 é sem
  paridade e usa reajuste RGPS (art. 27, **II**) — citar o art. 27, **I**
  (paridade) contradiz a própria hipótese. Provável copy-paste da P5. Usar a
  base correta (art. 24 / 27 II) ao destilar.

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
- `Valor Médio` (0006, 0022) ↔ PGE "cálculo por média" (P1, P6/P7) ✅.

## 7. Resumo executivo (para autoria in-place)

- **Confirmar e seguir (matches limpos):** 0006→P1, 0007→P2, 0009→P3,
  0008→P4, 0019→P5.
- **Resolver contra a fonte:** 0021 (flag×texto), 0020 (célula órfã
  proporcional-antes-2004 + corpo copiado da 0019).
- **Decidir sobre regimes antigos:** 0001/0002/0004 — extintos (inativar via
  `status_regra`/`motivo_inativacao`) ou faltam hipóteses no to-be da PGE?
- **Confirmar o desdobramento por causa:** 0022 cobre P6 (doença grave) + P7
  (acidente) — o Sisprev não tem campo "causa"; verificar como o split é
  tratado.
- **Não copiar da PGE sem conferir:** numeração pula a 8; base da P6 está
  copiada da P5.

Nenhuma correção de conteúdo demanda campo deployável novo — todas cabem nos
campos atuais (`sexo`, `integral`, `paridade`, `tipo_calculo` e
`fundamentacao*`); inativação, quando o caso, nos campos administrativos.
