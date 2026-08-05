---
type: Especificacao
id: conjunto
nome: Conjunto
---

# Conjunto

> **Tipo retirado (RFC 0004, round 11).** `Conjunto` era o objeto de
> composição que declarava, à parte das regras, quais destinos substituíam
> quais origens (`substituicoes[].origens_legacy`/`destinos_propostos`),
> se a substituição estava juridicamente decidida (`decisao_completude`) e
> se a fonte operacional de exportação podia trocar (`estado_grupo`,
> computado a partir da primeira mais o estado de implantação de cada
> destino).
>
> A entidade repetia informação já presente em `RegraProposta.origens_legacy`
> e criava um segundo lugar onde o mesmo fato — quais destinos formam uma
> unidade atômica de substituição — podia divergir do que as próprias regras
> declaravam. `okf/spec/regraproposta.md`, seção "Atomicidade é derivada, não
> declarada", substitui `estado_grupo` por um cálculo de componentes conexos
> do grafo origem↔destino, feito a cada execução de `scripts/derivar.py` — a
> mesma garantia de atomicidade, sem entidade persistente própria.
>
> `decisao_completude` — a decisão jurídica de que um conjunto de destinos
> cobre exaustivamente as causas de um dispositivo — não desapareceu:
> passou a viver como decisão datada no documento do `Ciclo` responsável
> (`okf/spec/ciclo.md`) e no log `decisoes` de cada `RegraProposta`
> envolvida, em vez de um campo por grupo declarado à parte.
>
> A revogação sem substituta (`Conjunto.revoga`) passou para
> `Regra.revogada` (`okf/spec/regra.md`).
>
> Nenhum documento do repositório declara mais `type: Conjunto`. O conteúdo
> jurídico irredutível dos oito documentos que existiam — justificativas,
> decisões da coordenação, referências normativas — foi migrado para
> `okf/regras-sisprev/ciclos/ciclo-01.md` e para as `RegraProposta`
> correspondentes antes da remoção.

Um **Conjunto** era a composição de regras vigente ou proposta num dado
momento: a base sobre a qual um lote de substituições se aplicava, e o
registro de quais grupos de origens/destinos estavam ativos. Cobria também a
revogação sem substituta e a projeção de atos de validação por composição
inteira, em vez de por regra.

Os gates que a acompanhavam (`P15_*`, RFC 0006 §8) nunca chegaram a ser
implementados em código — eram prosa de especificação, não checagem
automática — e são retirados junto com o tipo. RFC 0006 e RFC 0007, que o
descreviam em detalhe, ficam marcadas como superadas.
