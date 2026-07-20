# Reconciliação as-is × to-be — Aposentadoria Especial de Policial (piloto)

> **Nota:** Relatório gerado por IA como apoio à decisão. **Não é artefato
> oficial** e não edita nenhuma regra. Cruza as regras hoje no sistema
> (as-is, `okf/regras-sisprev/regras/`) com a análise da PGE-RO (to-be, aba
> "Especial de policial" de `data/raw/xlsx/especial-de-policial.csv`). A
> análise da PGE **também tem erros próprios** (ver §4) — é insumo, não
> verdade. Toda mudança final vai in-place nos `regra-*.md`, **só nos campos
> que o Sisprev já tem** (a riqueza da PGE — idade, tempo, pedágio, pareceres
> — se destila para os valores corretos dos campos existentes e para o texto
> de fundamentação, não vira campo novo).

## 1. Os dois lados

**As-is — 16 regras de policial no sistema:** 0072, 0073, 0074, 0075, 0076,
0077, 0078, 0079, 0080, 0081, 0082, 0083, 0109, 0110, 0111, 0112.

**To-be — 8 hipóteses da PGE**, uma matriz limpa de 2×2×2
(permanente/transitória × modo de cálculo × sexo):

| #   | Hipótese PGE                                  | Sexo | Base                                                                   | Cálculo                                                          |
| --- | --------------------------------------------- | ---- | ---------------------------------------------------------------------- | ---------------------------------------------------------------- |
| P1  | Permanente LCE 1.100 - integralidade/paridade | H    | art. 40 §1º III 2ª parte + §4º-B (EC103); arts. 25, 27 I, 34 LCE 1.100 | integralidade, paridade                                          |
| P2  | idem                                          | M    | idem                                                                   | integralidade, paridade                                          |
| P3  | Permanente - média/RGPS                       | H    | §4º-B (EC103); arts. 24, 27 II, 34 LCE 1.100                           | média, sem paridade                                              |
| P4  | idem                                          | M    | idem                                                                   | média, sem paridade                                              |
| P5  | Transitória idade+tempo+**pedágio**           | H    | art. 7º §§2º e 3º EC 146/2021; LC 51/85 art. 1º II "a"                 | integralidade, paridade (53 anos)                                |
| P6  | idem                                          | M    | LC 51/85 art. 1º II "b"                                                | integralidade, paridade (50 anos — ADI 7.727)                    |
| P7  | Transitória idade+tempo (**sem pedágio**)     | H    | art. 7º caput e §3º EC 146; LC 51/85 II "a"                            | integralidade, paridade (55 anos — Parecer 324/2025)             |
| P8  | idem                                          | M    | art. 7º caput e §3º; LC 51/85 II "b"                                   | integralidade, paridade (52 anos — ADI 7.727 + Parecer 452/2026) |

**Headline: 16 regras as-is → 8 hipóteses to-be.** O excesso do as-is é quase
todo duplicata, erro de sexo, ou combinação inválida.

## 2. Mapa as-is → to-be + ação sugerida

| as-is                                           | campos as-is                                                  | → PGE                  | Situação / ação sugerida (você autora)                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------- | ------------------------------------------------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **0082** H / **0083** M                         | §4º-B, integralidade, paridade, `Remuneração de Contribuição` | **P1 / P2**            | ✅ Match limpo. Fundamentação as-is já bate. Só conferir.                                                                                                                                                                                                                                                                                    |
| **0080** H / **0081** M                         | §4º-B, média, sem paridade, `Valor Médio`                     | **P3 / P4**            | ✅ Match limpo. Conferir.                                                                                                                                                                                                                                                                                                                    |
| **0072** H / **0073** M                         | art. 7º §§2,3, integralidade, paridade                        | **P5 / P6**            | ⚠️ Base certa, mas **corpo traz texto de H e M concatenado** (`… homem …` + `… mulher …`) nas duas. Separar: 0072→só "a"/homem, 0073→só "b"/mulher.                                                                                                                                                                                          |
| **0074, 0075, 0076, 0077** (todas H, idênticas) | art. 7º §§2,3                                                 | **P5** (colapsam em 1) | 🔴 4 cópias MASCULINO idênticas (= achado-0007). A PGE tem **uma** hipótese masculina de pedágio. Manter uma (P5), inativar 3.                                                                                                                                                                                                               |
| **0078** H / **0079** M                         | art. 7º §3, "alínea b", texto "+ mulher"                      | **P7? / P8**           | 🔴 0078 tem flag MASCULINO mas **conteúdo 100% feminino** (alínea "b", "mulher") — idêntico à 0079 (= achado-0010). Ou 0078 é dup de 0079 a inativar, **ou** deveria ser o homem P7 (alínea "a", 55 anos) e o conteúdo está errado. Decidir contra a fonte.                                                                                  |
| **0111** H / **0112** M                         | art. 7º §§2,3, integralidade, paridade                        | **P5 / P6**            | 🔴 **Duplicam 0072/0073** (mesma base, mesmo cálculo, mesmo par). Corpo também concatena H+M. Colapsar com 0072/0073.                                                                                                                                                                                                                        |
| **0109** H / **0110** M                         | art. 7º §§2,3, **média, sem paridade**, `Valor Médio`         | **(nenhuma)**          | 🔴 Combinação estranha: base de **transição EC146 art. 7º** (que na PGE é integralidade/paridade) com **cálculo por média / sem paridade**. A PGE não tem essa célula. Ou a base está errada (deveria ser §4º-B → P3/P4), ou o cálculo está errado (deveria ser integralidade → P5/P6). Resolver contra a fonte. Corpo também concatena H+M. |

## 3. Lacuna estrutural: pedágio × sem-pedágio

A PGE separa **P5/P6 (art. 7º §§2º e 3º — com pedágio)** de **P7/P8 (art. 7º
caput e §3º — idade+tempo, sem pedágio)**. O as-is **não faz essa distinção
de forma consistente**: quase todas as transitórias citam "§§2º e 3º"
(pedágio), e a única que cita "§3º" isolado (0078/0079) está mal-sexada. Se a
distinção pedágio × sem-pedágio for real para o Sisprev, faltam hipóteses
masculinas/femininas bem-formadas do ramo "sem pedágio" (P7/P8) — hoje só
existe conteúdo feminino duplicado.

## 4. Erros na própria análise da PGE (não copiar cegamente)

Nas linhas **femininas** da aba policial (P2, P4) aparecem "EC 103/**2020**"
e "LCE 1.100/**2022**" — copy-paste incrementado de 2019/2021. As datas
corretas são as das linhas masculinas (2019 / 2021). Ao destilar, usar as
versões corretas.

## 5. Resumo executivo (para autoria in-place)

- **Confirmar e seguir:** 0080/0081 (P3/P4), 0082/0083 (P1/P2).
- **Limpar corpo (separar H/M concatenado):** 0072, 0073, 0111, 0112, 0109, 0110.
- **Inativar duplicatas:** 3 das 4 em {0074,0075,0076,0077}; 0111/0112 vs 0072/0073.
- **Resolver contra a fonte:** 0078 (flag×conteúdo), 0109/0110 (base×cálculo).
- **Confirmar se existe o ramo "sem pedágio" (P7/P8)** e, se sim, corrigir
  0078 para o homem P7.

Nenhuma dessas ações precisa de campo novo — todas cabem nos campos atuais
(`sexo`, `integral`, `paridade`, `tipo_calculo`, `atualmente_no_sistema` para
inativar, e o texto das seções de fundamentação).
