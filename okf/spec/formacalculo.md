---
type: Especificacao
id: formacalculo
nome: FormaCalculo
---

# Forma de cálculo

> **Tipo retirado (RFC 0004, round 10; achado do Ciclo 1).** `FormaCalculo`
> existia como conceito canônico paralelo a `TipoCalculo` — a primeira
> descrevia a fórmula jurídica, a segunda o rótulo do Sisprev. A separação
> não servia a uma distinção que o domínio precisasse, e gerava confusão: o
> Ciclo 1 encontrou o mesmo rótulo legado projetando fórmulas juridicamente
> distintas, e resolver isso exigia um só conceito, não dois. Nenhum
> documento do repositório declara mais `type: FormaCalculo`; os vinte e
> dois que existiam foram migrados para `type: TipoCalculo`
> (`okf/tipos-calculo/`), preservando fórmula, fundamentação e proveniência
> por completo. Este documento fica como registro de que o tipo existiu e
> por que foi retirado — não é mais especificação de um tipo em uso. Ver
> [`okf/spec/tipocalculo.md`](tipocalculo.md).

Uma **FormaCalculo** era a fórmula do provento descrita juridicamente: qual
era a base, o que a proporcionalizava, que limites incidiam e em que
dispositivos cada passo se fundava — exatamente o que `TipoCalculo` agora
descreve, com a origem legada (antigo `projecao_sisprev`, hoje
`origem_legada`) como propriedade do mesmo documento, não como referência a
um segundo tipo.
