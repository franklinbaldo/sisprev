---
type: Achado
id: achado-0053
nome: DATA_DIREITO_APOS grava sempre o dia da vigência da norma, e a leitura exclusiva tornaria a janela um dia curta em toda a população
situacao: improcedente
severidade: informativo
verificacao: manual
natureza: modelagem
regras_afetadas:
  - /regras/regra-0004.md
  - /regras/regra-0006.md
  - /regras/regra-0007.md
  - /regras/regra-0008.md
  - /regras/regra-0009.md
  - /regras/regra-0010.md
  - /regras/regra-0011.md
  - /regras/regra-0012.md
  - /regras/regra-0013.md
  - /regras/regra-0025.md
  - /regras/regra-0026.md
  - /regras/regra-0030.md
  - /regras/regra-0031.md
  - /regras/regra-0033.md
  - /regras/regra-0034.md
  - /regras/regra-0035.md
  - /regras/regra-0036.md
  - /regras/regra-0037.md
  - /regras/regra-0038.md
  - /regras/regra-0041.md
  - /regras/regra-0042.md
  - /regras/regra-0043.md
  - /regras/regra-0044.md
  - /regras/regra-0045.md
  - /regras/regra-0046.md
  - /regras/regra-0047.md
  - /regras/regra-0048.md
  - /regras/regra-0049.md
  - /regras/regra-0050.md
  - /regras/regra-0051.md
  - /regras/regra-0052.md
  - /regras/regra-0053.md
  - /regras/regra-0054.md
  - /regras/regra-0055.md
  - /regras/regra-0056.md
  - /regras/regra-0057.md
  - /regras/regra-0058.md
  - /regras/regra-0059.md
  - /regras/regra-0060.md
  - /regras/regra-0061.md
  - /regras/regra-0062.md
  - /regras/regra-0063.md
  - /regras/regra-0064.md
  - /regras/regra-0068.md
  - /regras/regra-0069.md
  - /regras/regra-0070.md
  - /regras/regra-0071.md
  - /regras/regra-0072.md
  - /regras/regra-0073.md
  - /regras/regra-0074.md
  - /regras/regra-0075.md
  - /regras/regra-0076.md
  - /regras/regra-0077.md
  - /regras/regra-0078.md
  - /regras/regra-0079.md
  - /regras/regra-0080.md
  - /regras/regra-0081.md
  - /regras/regra-0082.md
  - /regras/regra-0083.md
  - /regras/regra-0089.md
  - /regras/regra-0090.md
  - /regras/regra-0091.md
  - /regras/regra-0092.md
detectado_em: 2026-07-30
improcedente_em: 2026-07-30
improcedente_por: franklinbaldo
detectado_por: franklinbaldo
---

# Descrição

Este achado registra uma hipótese histórica que foi investigada e rejeitada. A
leitura exclusiva de `DATA_DIREITO_APOS` tornaria a janela inferior um dia curta
em toda a população, porque o catálogo grava sistematicamente o próprio dia de
início de vigência da norma.

A coordenação da auditoria consolidou em 2026-08-01 que:

- `DATA_DIREITO_APOS` é **inclusivo** e representa o primeiro dia em que todos
  os requisitos podem estar implementados sob a regra;
- `DATA_ADM_APOS` também é **inclusivo** e representa a fronteira inferior do
  ingresso no serviço público;
- a leitura anterior de `DATA_ADM_APOS` como exclusivo está superada; e
- essas semânticas não são mais perguntas abertas nem premissas derrotáveis da
  auditoria.

A decisão vigente está em
[`okf/spec/decisoes-semanticas-regra.md`](../../../okf/spec/decisoes-semanticas-regra.md).

# Evidências

Para cada regra, comparou-se `data_direito_apos` com o `vigencia_inicio` de cada
dispositivo declarado em `dispositivos:`. Toda coincidência encontrada é de
igualdade exata; nenhuma é de um dia antes.

| marco          | `DATA_DIREITO_APOS` grava o dia | grava o dia anterior |
| -------------- | ------------------------------- | -------------------- |
| EC 20/1998     | sim                             | nunca                |
| EC 41/2003     | sim                             | nunca                |
| ECE 146/2021   | sim                             | nunca                |
| LCE 1.100/2021 | sim                             | nunca                |

A medição demonstrou que a hipótese exclusiva era incompatível com a convenção
de preenchimento observada no catálogo. A resposta posterior da coordenação
fechou também a semântica do eixo de admissão, retirando a última assimetria que
este achado ainda tratava como possível.

# Consequência prática

Nenhuma regra desta população possui defeito apenas porque
`DATA_DIREITO_APOS` grava o dia de início da vigência. O próprio dia entra na
fronteira inferior.

A conferência de mérito continua necessária para saber se **o valor concreto**
gravado em cada regra corresponde ao marco jurídico correto. Isso é questão de
fonte, vigência e dispositivo aplicável, não questão sobre o significado da
coluna.

# Questão a investigar

A questão histórica foi: **`DATA_DIREITO_APOS` inclui o próprio dia gravado ou
começa somente no dia seguinte?**

Ela está respondida: inclui o próprio dia. Esta seção permanece apenas porque o
contrato de `Achado` exige o registro da pergunta que originou a investigação;
não representa pendência atual.

# Resolução

O achado permanece `improcedente`.

A hipótese que o originou foi superada, e não há questão semântica residual a
investigar neste documento. Eventual divergência futura deve ser aberta como
revisão expressa da decisão consolidada, com evidência nova e impacto
identificado; não pode ser reintroduzida como dúvida genérica em ciclos de
auditoria.
