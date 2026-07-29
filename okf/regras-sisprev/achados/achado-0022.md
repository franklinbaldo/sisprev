---
type: Achado
id: achado-0022
nome: Sete regras invocam o art. 4º da ECE 146/2021 e gravam data_direito_ate 31/12/2099, contra o prazo de 31/12/2024 do próprio dispositivo
situacao: aberto
severidade: bloqueante
verificacao: manual
natureza: juridica
regras_afetadas:
  - /regras/regra-0006.md
  - /regras/regra-0007.md
  - /regras/regra-0008.md
  - /regras/regra-0009.md
  - /regras/regra-0032.md
  - /regras/regra-0039.md
  - /regras/regra-0040.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

Sete regras fundam os seus **requisitos** em legislação anterior à ECE
146/2021, invocam o art. 4º dessa emenda — que é o dispositivo que preserva
aquela legislação — e gravam `data_direito_ate: 31/12/2099`, a sentinela de
"sem limite".

O art. 4º preserva a legislação anterior **com prazo**:

> Art. 4º A concessão de aposentadoria [...] observará os requisitos e os
> critérios exigidos pela legislação vigente até a data de entrada em vigor
> desta Emenda Constitucional, **desde que sejam cumpridos até 31 de dezembro
> de 2024**, sendo assegurada a qualquer tempo.

Sob a semântica que a Q1 fechou — `DATA_DIREITO_ATE` é o prazo de implementação
dos requisitos —, essas sete regras deveriam fechar em `31/12/2024`.

# Evidências

Fonte: `fontes-oficiais/transcricoes/sapl-emenda_146.md`, transcrição
pesquisável conferida contra o OCR do PDF original da ALE-RO. Conferência
completa em
[`conferencia-janela-art-4-ece-146.md`](../../../docs/analysis/conferencia-janela-art-4-ece-146.md).

| regra          | fundamento dos requisitos                          | `data_direito_ate` |
| -------------- | -------------------------------------------------- | ------------------ |
| `0006`, `0007` | art. 40, § 1º, I, CF, red. EC 41/2003              | 31/12/2099         |
| `0008`, `0009` | art. 6º-A da EC 41/2003, red. EC 70/2012           | 31/12/2099         |
| `0032`         | art. 40, § 1º, II, CF, red. EC 88/2015 + LC 152/15 | 31/12/2099         |
| `0039`, `0040` | art. 40, § 1º, III, "a" e § 5º, CF, red. EC 20/98  | 31/12/2099         |

Três corroborações, e a terceira é a que sustenta a acusação:

1. **`0039`/`0040` separam os eixos na própria fundamentação**: citam a EC
   20/1998 "quanto ao preenchimento dos requisitos" e a EC 41/2003 "no que
   tange à fórmula de cálculo e reajuste". Requisitos por norma anterior à
   EC 146, com o art. 4º invocado.
2. **`0032`, `0039` e `0040` abrem o direito em `18/10/2021`**, a entrada em
   vigor da ECE 146/2021 — exatamente o começo do período que o art. 4º
   garante. A janela dessas regras é esse período, que termina em 31/12/2024.
3. **O catálogo já pratica a leitura correta em 12 regras.** Das 24 que
   vinculam o art. 4º, `0012`, `0013`, `0097`–`0106` fecham em `31/12/2024` —
   todas de legislação anterior à EC 146 (art. 40, § 7º e arts. 2º e 6º da
   EC 41/2003; art. 3º da EC 47/2005). A divergência é destas sete, não da
   interpretação.

A oração "sendo assegurada a qualquer tempo" **não** justifica a sentinela: ela
fala do momento da concessão, não do implemento dos requisitos. Quem cumpriu
até 31/12/2024 requer depois; quem não cumpriu não passa a poder cumprir.

# Questão a investigar

A correção é uniforme (`data_direito_ate: 31/12/2024` nas sete) ou alguma delas
tem fundamento próprio para não fechar?

Duas frentes concretas:

- **`0032` tem divergência interna anterior a esta.** O `nome` a funda na EC
  103/2019 e na LC 1.100/2021 (regime novo); a fundamentação, na EC 88/2015 e
  na LC 152/2015 (anterior à EC 146). Se o nome estiver certo, a regra é de
  regime novo e o problema deixa de ser a janela: passa a ser a citação do
  art. 4º. Registrado em achado próprio.
- **`0006`/`0007` são de regime permanente** (`data_adm_ate: 31/12/2099`, sem
  corte de ingresso). A consequência de fechar em 2024 é que a incapacidade
  permanente sob a redação da EC 41/2003 deixa de ser concedível para
  incapacidades constituídas depois — o que é coerente com a reforma estadual,
  mas é a conclusão de maior alcance deste achado e merece confirmação
  expressa.

**Severidade `bloqueante` por escolha do auditor**: `data_direito_ate` é campo
deployável, e uma janela aberta onde o dispositivo invocado a fecha permitiria
ao Sisprev conceder benefício sob regra cujo prazo expirou. Isso impede
`revisada` nas sete até que a decisão seja tomada — que é o comportamento
desejado, não um efeito colateral.
