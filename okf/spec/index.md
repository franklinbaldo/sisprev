# Especificações

Um documento por `type` em uso, e cada um concentra **tudo o que é preciso
saber sobre os campos daquele tipo** — semântica, vocabulário fechado, decisão
da coordenação, o que o tipo não faz. O que isso significa, e por que documento
histórico não repete regra vigente, está em
[especificacao.md](especificacao.md).

O caminho é derivado do nome do tipo, e não apontado por ele: `Regra` procura
`regra.md`, `RegraProposta` procura `regraproposta.md`. `scripts/conferir_specs_dos_tipos.py`
reprova o tipo em uso que não tenha documento.

## Os tipos vigentes

- [especificacao.md](especificacao.md) — o que é uma especificação.
- [regra.md](regra.md) — a regra do Sisprev: as colunas, as decisões
  semânticas de cada campo e a semântica das quatro janelas temporais.
- [regraproposta.md](regraproposta.md) — a regra corrigida, que ocuparia uma
  linha do sistema.
- [achado.md](achado.md) — a acusação datada sobre regras nomeadas.
- [ciclo.md](ciclo.md) — o lote temático, e o critério de fechamento dele.
- [dispositivo.md](dispositivo.md) — a unidade legal endereçada, com a cadeia
  que a contém.
- [norma.md](norma.md) — o vocabulário fechado das leis citáveis.
- [dataset.md](dataset.md) — a identidade de um bundle importado.
- [tipocalculo.md](tipocalculo.md) — a fórmula juridicamente fundamentada
  usada para apurar o valor inicial de um benefício, com a sua origem no
  catálogo legado do Sisprev, quando houver.

## Tipos retirados (notas históricas)

Documento de especificação que fica como registro de que o tipo existiu e
por que foi retirado — nenhum documento do repositório declara mais o
`type` correspondente. `scripts/conferir_specs_dos_tipos.py` não os conta
entre os tipos em uso.

- [conjunto.md](conjunto.md) — a composição do catálogo e os grupos de
  substituição, retirados em RFC 0004, round 11: a atomicidade de
  implantação é hoje derivada de `RegraProposta.origens_legacy`, não
  declarada à parte.
- [formacalculo.md](formacalculo.md) — a fórmula jurídica como entidade
  canônica paralela a `TipoCalculo`, retirada em RFC 0004, round 10: os
  dois conceitos foram fundidos em `TipoCalculo`.
