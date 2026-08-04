# Especificações

Os contratos semânticos do catálogo. Cada arquivo é a **autoridade única** do
seu assunto — o que isso significa, e por que documento histórico não repete
regra vigente, está em [especificacao.md](especificacao.md).

## Os documentos

- [especificacao.md](especificacao.md) — o que é uma especificação, e a regra
  de autoridade única por assunto.
- [regra.md](regra.md) — contrato do tipo `Regra`: estrutura, estados e as
  questões Q1–Q12.
- [decisoes-semanticas-regra.md](decisoes-semanticas-regra.md) — decisões da
  coordenação sobre ramos integral/proporcional, `INTEGRAL`, `TIPO_CALCULO`,
  `DATA_DIREITO_APOS` e `DATA_ADM_APOS`, e a lista de pontos fechados.
- [janelas-temporais-regra.md](janelas-temporais-regra.md) — a semântica das
  quatro fronteiras `DATA_*` e a decisão verificável que o gate confere.
- [dispositivo.md](dispositivo.md) — contrato do tipo `Dispositivo`.
- [criterio-fechamento-ciclos.md](criterio-fechamento-ciclos.md) — o estado
  final obrigatório de um ciclo de auditoria.

## Onde uma divergência se resolve

Entre `decisoes-semanticas-regra.md` e `regra.md`, nos temas que a primeira
enumera, prevalece a primeira até que a consolidação seja incorporada ao
contrato geral. Fora desse par, cada assunto tem um documento só, e não há o
que desempatar — se houver dois, é defeito a corrigir, não regra a aplicar.
