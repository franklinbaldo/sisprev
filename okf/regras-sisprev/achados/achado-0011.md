---
type: Achado
id: achado-0011
nome: Fundamentação de regra-0039 e regra-0093 omite a norma dona do art. 40 (só nomeia a emenda alteradora)
situacao: aberto
severidade: informativo
verificacao: manual
natureza: dados
regras_afetadas:
  - /regras/regra-0039.md
  - /regras/regra-0093.md
detectado_em: 2026-07-27
detectado_por: franklinbaldo
---

# Descrição

A `FUNDAMENTACAO_INTEGRAL` de `regra-0039` e `regra-0093` cita, ipsis
litteris:

> [...] artigo 40, §§ 3º e 8º **com redação dada pela Emenda Constitucional
> nº 41/2003**, no que tange à fórmula de cálculo e reajuste [...]

A única norma nomeada ao lado do artigo é a **alteradora** (EC 41/2003). A
norma **dona** do dispositivo — a Constituição Federal — não aparece em
lugar nenhum da oração. Um leitor humano supre pelo contexto, porque sabe
que "art. 40, §§ 3º e 8º" nessa matéria é da CF; o registro, não.

Nas demais regras do catálogo a mesma citação vem completa ("artigo 40, § 1º,
inciso I, **da Constituição Federal**, com redação dada pela Emenda
Constitucional nº 41/2003"), o que reforça a leitura de que aqui houve
omissão, não uma convenção diferente.

# Evidências

Confere-se lendo os campos de fundamentação das duas regras: em nenhum
deles a norma **dona** dos artigos é nomeada. A única norma nomeada vem
depois de "com redação dada por" — e essa é, por definição, a alteradora.

Nenhum vínculo é declarado para esses artigos, e é a recusa correta:
atribuir o art. 40 à EC 41/2003 produziria uma citação jurídica errada com
aparência plausível. Sem norma dona nomeada, a citação fica sem endereço, e
o catálogo registra a lacuna em vez de escolher pela regra qual norma ela
invoca.

O registro congelado dessas pendências está em
[`docs/analysis/pendencias-de-citacao-congeladas.md`](../../../docs/analysis/pendencias-de-citacao-congeladas.md),
na fila `LEITURA-HUMANA`.

# Consequência prática

Estas duas regras **não recebem vínculo** para o art. 40, §§ 3º e 8º —
nem no lote da CF/88 nem em nenhum outro — porque não há norma dona a
resolver. A lacuna permanece visível no relatório até que a questão abaixo
seja decidida.

# Questão a investigar

A omissão deve ser corrigida na origem ou apenas registrada?

`FUNDAMENTACAO*` é campo **deployável** do Sisprev — é o texto que o sistema
entrega no documento do servidor. Corrigi-lo não é ato de auditoria sobre o
catálogo, é alteração do produto, e depende de quem responde por ele. As
hipóteses a distinguir:

1. **Erro de digitação/importação** — a fundamentação original nomeava a CF
   e a menção se perdeu. Correção na origem, e o vínculo passa a ser
   possível.
2. **Convenção de redação** — o autor considerou a CF implícita por já
   estar citada antes na mesma frase. Nesse caso a prosa fica como está e o
   vínculo é declarado à mão, com este achado como justificativa.
3. **Citação genuinamente incompleta** — os §§ 3º e 8º pertencem a outra
   norma que não a CF. Improvável pela matéria, mas é o que a leitura
   estrita do campo permite afirmar hoje.

Enquanto não decidido, nada é inferido: o registro diz o que o campo diz.
