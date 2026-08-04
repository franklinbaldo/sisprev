# Especificações

Um documento por `type` em uso, e cada um concentra **tudo o que é preciso
saber sobre os campos daquele tipo** — semântica, vocabulário fechado, decisão
da coordenação, o que o tipo não faz. O que isso significa, e por que documento
histórico não repete regra vigente, está em
[especificacao.md](especificacao.md).

O caminho é derivado do nome do tipo, e não apontado por ele: `Regra` procura
`regra.md`, `RegraProposta` procura `regraproposta.md`. `scripts/conferir_specs_dos_tipos.py`
reprova o tipo em uso que não tenha documento.

## Os tipos

- [especificacao.md](especificacao.md) — o que é uma especificação.
- [regra.md](regra.md) — a regra do Sisprev: as colunas, as decisões
  semânticas de cada campo e a semântica das quatro janelas temporais.
- [regraproposta.md](regraproposta.md) — a regra corrigida, que ocuparia uma
  linha do sistema.
- [achado.md](achado.md) — a acusação datada sobre regras nomeadas.
- [ciclo.md](ciclo.md) — o lote temático, e o critério de fechamento dele.
- [conjunto.md](conjunto.md) — a composição do catálogo e os grupos de
  substituição.
- [dispositivo.md](dispositivo.md) — a unidade legal endereçada, com a cadeia
  que a contém.
- [norma.md](norma.md) — o vocabulário fechado das leis citáveis.
- [dataset.md](dataset.md) — a identidade de um bundle importado.
- [formacalculo.md](formacalculo.md) — a fórmula do provento, descrita
  juridicamente.
- [tipocalculo.md](tipocalculo.md) — o rótulo que o Sisprev grava na coluna de
  cálculo.
