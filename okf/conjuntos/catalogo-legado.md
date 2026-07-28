---
type: Conjunto
id: catalogo-legado
nome: Catálogo legado do Sisprev
situacao: vigente
origem: catalogo-legado
---

# Catálogo legado do Sisprev

O conjunto-raiz: as 112 regras de `okf/regras-sisprev/regras/`, tal como já
vinham sendo operadas. Não tem `base` — declara `origem`, porque não deriva de
nenhuma composição anterior registrada aqui.

**Não é a importação.** `data/raw/regras-sisprev.csv` guarda o arquivo recebido
e é imutável para sempre; este conjunto é o catálogo **autorado hoje**, que
recebeu edições de auditoria desde então (achados, dispositivos vinculados,
correções). Chamá-lo de `importacao-*` nomearia um estado que o bundle não
contém — ele existe no CSV congelado e no histórico do git, não em documento
consultável.

## Por que a raiz não traz `decisao_completude` nem ato de ativação

Os dois são exigidos de quem **transita** de `proposto` para `vigente`. Este
conjunto não transitou: ele registra um estado operacional preexistente.
Exigir-lhe os campos produziria uma decisão institucional fictícia, assinada
por ninguém, só para satisfazer o schema — o oposto do que
`decisao_completude` existe para garantir (RFC 0006 §6.1).

A dispensa é da **raiz**, não de "quem já estava vigente": raiz é quem tem
`origem` e não tem `base`, e um segundo conjunto não pode reivindicá-la sem
cair no `P15_RAIZ_AMBIGUA`.
