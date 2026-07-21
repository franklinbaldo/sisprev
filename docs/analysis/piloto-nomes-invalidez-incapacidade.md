# Piloto de `nome` orientado à seleção — Invalidez / Incapacidade Permanente

> **Nota:** Relatório gerado por IA como apoio à decisão. **Não é artefato
> oficial** e **não altera nenhuma regra** — os "nomes propostos" são
> **exemplos para decisão humana**, não edições. Aplica o princípio do campo
> `nome` registrado em [`docs/spec/regra.md`](../spec/regra.md) às 11 regras
> já reconciliadas em
> [`reconciliacao-invalidez-incapacidade.md`](reconciliacao-invalidez-incapacidade.md).
> `id` continua a identidade técnica estável; só o `nome` mudaria, e só por
> decisão humana.

## Princípio aplicado

> O nome deve ser a menor descrição, em linguagem humana, capaz de distinguir
> a regra das demais que ainda podem ser aplicáveis depois da anamnese do
> requerente.

Forma de trabalho dos exemplos: **modalidade — marco de ingresso — causa
relevante — proventos/cálculo — paridade**, com a citação legal fora do nome
(fica na `fundamentacao*`).

## Diagnóstico dos nomes atuais

**As 11 regras formam 5 pares de nome idêntico** (todos disparam
`P1_NOME_REPETIDO`) mais a 0004 isolada:

- 0001 ≡ 0002 · 0006 ≡ 0007 · 0008 ≡ 0009 · 0019 ≡ 0020 · 0021 ≡ 0022.

Em cada par, as duas regras **só se distinguem no flag `integral`** (e no
`tipo_calculo`) — o nome é o mesmo. Ou seja: hoje o usuário **precisa abrir a
fundamentação** para saber qual das duas se aplica. Pelo princípio, os nomes
falharam.

## Tabela piloto

| Regra | Nome atual (resumido)                                                                | Pode ser confundida com | Fato da anamnese que distingue                                    | Nome proposto (exemplo)                                                                                                            | Informação ainda ausente                                                                                               | Confiança / pendência                                     |
| ----- | ------------------------------------------------------------------------------------ | ----------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| 0001  | "Aposentadoria por Invalidez Anterior E.C 20/1998"                                   | 0002 (idêntico), 0004   | causa **qualificada** (acidente/moléstia/doença grave) → integral | Invalidez permanente — regime anterior à EC 20/1998 — causa qualificada — proventos integrais, com paridade                        | causa não é campo estruturado; o regime ainda alcança alguém? (§3 da reconciliação)                                    | média — regime antigo sem contraparte no to-be            |
| 0002  | idem 0001                                                                            | 0001                    | causa **comum** → proporcional                                    | Invalidez permanente — regime anterior à EC 20/1998 — causa comum — proventos proporcionais, com paridade                          | idem 0001                                                                                                              | média                                                     |
| 0004  | "Aposentadoria por Invalidez - Redação da EC 20/1998"                                | 0001, 0002              | regime **EC 20/1998** (vs pré-EC 20)                              | Invalidez permanente — regime EC 20/1998 — (causa e cálculo a definir)                                                             | **alta**: `sexo`, `integral`, `tipo_calculo` vazios (achado-0008) — não dá para nomear cálculo/causa                   | **baixa** — nome bloqueado até preencher os campos vazios |
| 0006  | "Invalidez - Art. 40, §1º, I ... EC 41/2003 e LC 432/2008"                           | 0007 (idêntico)         | causa **qualificada** → integral                                  | Invalidez permanente — ingresso após 31/12/2003 — acidente em serviço ou doença grave — integral (média), sem paridade             | causa não é campo estruturado                                                                                          | alta — P1 é match limpo na reconciliação                  |
| 0007  | idem 0006                                                                            | 0006                    | **doença não catalogada** (causa comum) → proporcional            | Invalidez permanente — ingresso após 31/12/2003 — doença não catalogada — proporcional, sem paridade                               | confirmar que 0007 = "doença não catalogada" (P2, match parcial)                                                       | média                                                     |
| 0008  | "Invalidez - Art. 6º-A da EC 41/2003 (EC 70/2012) e LC 432/2008"                     | 0009 (idêntico)         | causa **qualificada** → integral                                  | Invalidez permanente — ingresso até 31/12/2003 — acidente em serviço ou doença grave — integral (última remuneração), com paridade | `Remuneração de Contribuição` ↔ última remuneração?; citação suspeita III 2ª parte (§4 da reconciliação)               | média                                                     |
| 0009  | idem 0008                                                                            | 0008                    | causa **comum** → proporcional                                    | Invalidez permanente — ingresso até 31/12/2003 — causa comum — proporcional (última remuneração), com paridade                     | equivalência do cálculo                                                                                                | média                                                     |
| 0019  | "Incapacidade Perm.- Art. 40 §1 I EC 103/19 c/c art. 30 LC 1100/21 - Até 31/12/2003" | 0020 (idêntico)         | causa **qualificada** → integral                                  | Incapacidade permanente — ingresso até 31/12/2003 — acidente em serviço ou doença grave — integral (totalidade), com paridade      | `Valor Efetivo` ↔ totalidade da remuneração?                                                                           | média-alta — P5                                           |
| 0020  | idem 0019                                                                            | 0019                    | causa **comum** → proporcional                                    | Incapacidade permanente — ingresso até 31/12/2003 — causa comum — proporcional, com paridade                                       | a PGE **não tem** essa célula (proporcional-antes-2004-com-paridade); campo `fundamentacao_integral` é cópia da 0019   | **baixa** — o nome expõe uma regra órfã, sem contraparte  |
| 0021  | "Incapacidade Perm.- ... - Após 31/12/2003"                                          | 0022 (idêntico)         | causa **comum** → proporcional                                    | Incapacidade permanente — ingresso após 31/12/2003 — causa comum — proporcional, sem paridade                                      | contradição flag×texto: `integral: N` mas a fundamentação diz "proventos integrais"                                    | **bloqueada** pela contradição da 0021                    |
| 0022  | idem 0021                                                                            | 0021                    | causa **qualificada** → integral                                  | Incapacidade permanente — ingresso após 31/12/2003 — acidente em serviço ou doença grave — integral (média), sem paridade          | **0022 cobre P6 (doença grave) + P7 (acidente)** — o nome agrupado só é correto se forem operacionalmente equivalentes | **baixa** — ver §"0022" abaixo                            |

## Achado transversal: o discriminante é a "causa da incapacidade", que não é campo

Em **todos** os cinco pares, o que separa a regra integral da proporcional é
a **causa da incapacidade** — qualificada (acidente em serviço, moléstia
profissional, doença grave/contagiosa/incurável) leva a integral; comum leva
a proporcional. Consequências pelo princípio do `nome`:

- O nome (texto livre) **pode** carregar a causa, e é isso que os exemplos
  acima fazem — resolvendo a colisão para o usuário que lê o nome.
- Mas hoje as regras se distinguem só pelo flag `integral`, que é o
  **resultado** da causa, não a causa. Na anamnese o requerente conhece o
  **fato** (a causa médica), não o "integral S/N". O nome bom expõe a causa
  (fato conhecido); o `integral` deveria **derivar** dela.
- A "causa da incapacidade" **não é uma das 27 colunas**. Enquanto for só
  texto do nome, a seleção depende do usuário ler certo; se a seleção for
  automática por campos, falta o predicado. Isso é uma **lacuna do modelo** a
  registrar — não um problema de redação.

## Casos que o piloto destaca

- **0022 × P6/P7 (o caso agudo):** uma única regra cobre "acidente em
  serviço" e "doença grave". Os campos do Sisprev (integral, média, sem
  paridade) são iguais para as duas causas, o que **justificaria** o nome
  agrupado. Mas a PGE as separou em duas hipóteses com bases legais
  distintas. **Decisão pendente:** se acidente e doença grave forem
  operacionalmente equivalentes, o nome agrupado está certo; se exigirem
  tratamento distinto, escondê-los sob um nome é errado e falta o predicado
  "causa" para separá-los. Não decidir por presunção.
- **Regimes antigos 0001/0002/0004:** os nomes propostos os identificam por
  regime (pré-EC 20 / EC 20), mas isso só vale se ainda houver candidatos por
  esses regimes (§3 da reconciliação — pergunta jurídica em aberto). Se
  extintos, a decisão é inativar, não renomear.
- **0004 (nome bloqueado):** com `sexo`/`integral`/`tipo_calculo` vazios, o
  nome não pode expressar cálculo nem causa — o piloto mostra que **nomear
  depende de preencher os campos** (achado-0008), não o contrário.
- **0021 (nome bloqueado por contradição):** o nome proposto ("proporcional")
  segue o flag `integral: N`, mas a fundamentação diz "integrais" — até
  resolver qual está certo, o nome não pode ser fixado.

## Limitações da interface a verificar antes de generalizar

Os nomes propostos são **longos**. Antes de virar gramática para as 112
regras, é preciso conferir na tela real do Sisprev: **comprimento máximo /
truncamento** do campo, **busca** (o usuário acha a regra digitando?) e
**ordenação** (nomes que começam por "Invalidez permanente — ingresso..."
agrupam bem ou empilham tudo junto?). Pode ser preciso uma forma mais curta
ou campos de apoio — decisão a tomar com a interface à vista, não aqui.
