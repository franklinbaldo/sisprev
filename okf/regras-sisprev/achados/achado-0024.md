---
type: Achado
id: achado-0024
nome: Quatro regras iniciam o regime da LCE 1.100/2021 em 23/10/2021, cinco dias após a publicação da lei
situacao: aberto
severidade: bloqueante
verificacao: manual
natureza: dados
regras_afetadas:
  - /regras/regra-0019.md
  - /regras/regra-0020.md
  - /regras/regra-0021.md
  - /regras/regra-0022.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

As quatro regras de incapacidade permanente do regime da LCE 1.100/2021 gravam
`data_direito_apos: 23/10/2021`. Esse valor não corresponde a nenhum marco da
norma citada.

A LCE 1.100/2021 foi publicada no Diário Oficial do Estado de Rondônia nº 207,
de **18/10/2021**, e o art. 115 determina que ela entra em vigor na data de sua
publicação. Como `DATA_DIREITO_APOS` é uma fronteira **inclusiva**, o próprio dia
18/10/2021 integra a regra nova.

O valor cadastrado desloca em cinco dias a fronteira inferior das quatro regras.
A questão semântica da coluna está encerrada; o que permanece é corrigir o valor
concreto no conjunto auditado.

## Atualização da delimitação do achado em 2026-08-01

A versão anterior deste documento também tratava
`data_adm_apos: 01/01/2004` de `regra-0021` e `regra-0022` como erro. Essa parte
do diagnóstico usava a antiga hipótese de que `DATA_ADM_APOS` seria exclusiva.
A coordenação consolidou que a coluna é **inclusiva** e representa o primeiro dia
de ingresso coberto.

Portanto:

- o texto legal “após 31 de dezembro de 2003” começa em **01/01/2004**;
- `data_adm_apos: 01/01/2004` inclui esse próprio dia e está alinhado com a
  partição legal;
- não existe a lacuna de admissão anteriormente descrita; e
- a data de admissão deixa de integrar o defeito ativo deste achado.

A decisão vigente está em
[`okf/spec/decisoes-semanticas-regra.md`](../../../okf/spec/decisoes-semanticas-regra.md).
O histórico abaixo explica a origem da investigação, mas não reabre a semântica
da coluna.

# Evidências

## Publicação e vigência da LCE 1.100/2021

A ficha oficial da norma no SAPL/ALE-RO identifica:

- data de publicação: **18/10/2021**;
- veículo: Diário Oficial do Estado de Rondônia nº 207; e
- disponibilização do PDF arquivado em 19/10/2021.

O texto oficial compilado contém:

> Art. 115. Esta Lei Complementar entra em vigor na data de sua publicação.

O texto não contém “23 de outubro” nem cláusula de produção diferida de efeitos
para o art. 30. A data 23/10/2021 tampouco corresponde à assinatura, à
publicação ou à disponibilização identificadas nas fontes oficiais.

Fontes arquivadas:

- `fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt`;
- ficha SAPL/ALE-RO da LCE 1.100/2021 (`sapl-9979`);
- `fontes-oficiais/arquivos/sapl-lc1100.pdf`; e
- `fontes-oficiais/manifesto.yaml`, com os hashes dos arquivos.

## Cotejo com o catálogo

Das regras que usam a LCE 1.100/2021 como marco inferior do direito, a maioria
grava `18/10/2021`. O bloco contíguo `regra-0019` a `regra-0022` é a exceção e
grava `23/10/2021`.

A contagem é evidência de lote de preenchimento, não a prova jurídica. A prova é
a publicação oficial somada ao art. 115. A contagem apenas corrobora que as
quatro regras destoam da sucessão normativa praticada no restante do catálogo.

## Fronteira de admissão preservada

Os arts. 24, 25 e 27 da LCE 1.100/2021 dividem as coortes entre ingresso:

- até 31/12/2003; e
- após 31/12/2003.

Sob a semântica inclusiva de `DATA_ADM_APOS`, o segundo grupo começa em
01/01/2004. Logo o valor atualmente gravado em `regra-0021` e `regra-0022` não é
objeto de correção por este achado.

# Consequência prática

As quatro regras não representam o regime novo durante os cinco primeiros dias
de vigência da LCE 1.100/2021. A eventual existência de sobreposição com regras
históricas ou de transição não torna correta a fronteira: o catálogo auditado
deve demonstrar qual regra cobre cada combinação e por qual fundamento.

Como `data_direito_apos` participa da seleção, o defeito é material. A correção
não deve apagar o registro legado: no modelo do ciclo, regras materialmente
erradas são desativadas e substituídas por regras novas com a fronteira correta,
quando a hipótese jurídica continua existindo.

# Questão a investigar

A questão semântica está respondida e a fonte do marco está identificada. O
trabalho restante é de execução e cobertura:

1. confirmar, no Bloco C do Ciclo 1, que nenhuma norma específica difere a
   produção de efeitos das hipóteses de incapacidade permanente;
2. representar as hipóteses corretas com `data_direito_apos: 18/10/2021`;
3. preservar a proveniência das quatro regras legadas; e
4. demonstrar na matriz final que os dias de 18/10/2021 em diante estão cobertos
   sem lacuna ou sobreposição injustificada.

Ausente fonte superveniente que estabeleça outro marco, `18/10/2021` é o valor a
ser aplicado.
