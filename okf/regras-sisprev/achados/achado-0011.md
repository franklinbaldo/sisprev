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

Reprodutível por `uv run python scripts/relatorio_citacoes.py`, na linha
`sem_norma` (8 ocorrências, distribuídas por estes dois documentos e seus
campos de fundamentação).

O leitor de citações (`scripts/citacoes.py`) **recusa** atribuir esses
artigos: a regra que ele aplica é que a norma nomeada logo após "com redação
dada por" é a alteradora, nunca a dona, e sem uma norma dona nomeada a
citação fica sem endereço. É a recusa correta — atribuir o art. 40 à EC
41/2003 produziria uma citação jurídica errada com aparência plausível,
que foi o modo de falha que motivou todo o desenho do leitor.

**Por que este achado não fixa um fingerprint.** A detecção existe
(`P4_CITACAO_NAO_VINCULADA` reporta `sem_norma` para as duas regras), mas o
fingerprint desse detector embute a **lacuna inteira** da regra — o que ela
cita, o que está vinculado, o que falta transcrever. Ele muda a cada lote de
vinculação ou transcrição, ainda que a omissão aqui descrita permaneça
idêntica. Fixá-lo faria este achado parecer "não mais reproduzido" no
primeiro lote seguinte, que é exatamente a leitura errada. A verificação
fica, portanto, registrada como manual: o fato se confere lendo o campo.

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
