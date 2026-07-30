# Corpus de processos administrativos do SEI — higienizado

**Corpus higienizado**, com remoção e substituição dos identificadores pessoais
diretos e dos dados sensíveis considerados desnecessários, preservando
referências processuais e elementos necessários à rastreabilidade e à análise
jurídica.

Vinte e cinco documentos (24 informações jurídicas e 1 parecer PGE/IPERON),
convertidos para markdown. O índice é
[`manifesto_processos_higienizados.json`](manifesto_processos_higienizados.json),
que mapeia cada arquivo ao processo, à categoria e ao número SEI.

## O que "higienizado" quer dizer aqui, e o que não quer

Esta é a descrição do procedimento, não uma garantia técnica ou jurídica mais
ampla que ele.

**Substituído** por marcadores estáveis por documento — `_NOME_PESSOA_1_`,
`_CPF_1_`, `_RG_1_`, `_MATRICULA_SERVIDOR_1_`, `_DATA_NASCIMENTO_1_`,
`_DADO_SAUDE_1_`, `_OAB_1_`, `_PROCESSO_JUDICIAL_1_`. A numeração é **local ao
arquivo**: `_NOME_PESSOA_1_` em dois documentos diferentes não é a mesma pessoa.

**Preservado deliberadamente**, porque é o que dá utilidade ao corpus:

- o **NUP** do processo administrativo e o **número SEI** de cada documento —
  por finalidade declarada: são o que permite localizar o precedente citado;
- a fundamentação jurídica integral, com normas, artigos e datas;
- cargo, lotação e datas funcionais quando necessárias à análise da regra;
- nomes de **autoridades públicas citadas em função oficial** (Ministros do STF
  e do STJ em precedentes, por exemplo).

**Consequência que precisa estar dita**: NUP e número SEI são, por construção,
rastreáveis por quem tem acesso ao SEI. Portanto **não se trata de anonimização
em sentido jurídico**, e o corpus não é descrito como "livre de PII". O risco
residual de reidentificação foi aceito de forma expressa, dado o uso pretendido
(auditoria das regras previdenciárias), e não deve ser reinterpretado depois
como garantia que não foi dada.

## Duas falhas encontradas depois da primeira rodada, e a causa

A verificação inicial reportou aprovação em todos os 25 arquivos. Uma
reconferência manual encontrou **nome civil não substituído em dois deles**, o
que falsifica aquele resultado:

| arquivo                                                      | o que escapou                                                                                                                           |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| `0016_102962-2020-85/parecer_608_pge-iperon__0061369704_.md` | nome do beneficiário em **6** ocorrências e do signatário em **2** — o arquivo tinha apenas 4 marcadores, todos `_PROCESSO_JUDICIAL_1_` |
| `0019_376374-2020-56/informação_1463__0021996526_.md`        | nome da requerente em prosa (linha 19), **na mesma frase** em que `_MATRICULA_SERVIDOR_1_`, `_RG_1_` e `_CPF_1_` foram substituídos     |

Ambos corrigidos. As duas causas são distintas e valem registro, porque qualquer
rodada futura tropeça nelas de novo:

1. **`NO-BREAK SPACE` (U+00A0) dentro do nome.** O nome da requerente é
   `LÉA…SOUZA DOS SANTOS`, com NBSP entre duas palavras. Casamento por
   string literal com espaço comum **falha em silêncio** — a primeira tentativa
   de correção manual deste repositório falhou exatamente assim, e só apareceu
   porque a verificação foi refeita. Há **987 NBSP** no corpus. Padrão de busca
   tem de usar `\s`, nunca `" "`.
2. **O `parecer` é o único documento de tipo diferente** (24 `informação` contra
   1 `parecer`), e é onde o nome aparece em prosa e dentro de dispositivo
   judicial citado, não após rótulo. Nas informações, os nomes substituídos
   estão em posições rotuladas (`REQUERENTE:`, bloco de assinatura). A falha
   correlaciona com **estrutura do documento**, então é sistemática e não
   anômala.

## Duas decisões de política, tomadas (2026-07-30)

O corpus aplica dois tratamentos diferentes a nomes de procuradores, e isso é
**deliberado**, não inconsistência residual. Decidido por quem responde pela
publicação:

**Signatário é substituído; autoridade citada não é.** Os procuradores que
assinam os documentos vão para `_NOME_PESSOA_N_` no bloco de assinatura. Um
ex-Procurador-Geral **citado** por manifestação que emitiu — em
`0019_376374-2020-56`, linha 107 — permanece nomeado, pelo mesmo fundamento que
mantém os Ministros do STF e do STJ nos precedentes: **autoridade pública em
função oficial, em contexto histórico**. A manifestação dele é peça da cadeia
argumentativa que o documento reconstrói; suprimir a autoria tornaria a citação
inverificável.

**Número SEI e NUP permanecem por finalidade declarada**: são o que permite
**localizar o precedente**. Um corpus de pareceres cujo identificador foi
removido não é auditável — não se confere se o parecer citado diz o que se
afirma. A rastreabilidade é aqui um requisito, não um resíduo tolerado.

Isso não altera o que a seção anterior diz sobre o alcance da higienização: a
consequência de preservar NUP e número SEI é que **não há anonimização em
sentido jurídico**, e é por isso que o corpus não é descrito assim.

## Como reconferir

```bash
# nenhum arquivo deve ter zero marcador
grep -c -oE "_[A-Z_]+_[0-9]+_" fontes-oficiais/processos-sei/*/*.md

# busca por nome civil tem de tolerar NBSP: use \s, nunca espaço literal
grep -rnPE "\bNOME\s+SOBRENOME\b" fontes-oficiais/processos-sei/
```
