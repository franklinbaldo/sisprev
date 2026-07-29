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

## O modelo federal prova essa leitura, em vez de apenas sustentá-la

Acrescentado em 2026-07-29, da
[análise jurídica](../../../docs/analysis/analise-juridica-art-4-ece-146.md). O
art. 4º é **cópia estrutural** do art. 3º da EC 103/2019:

> A concessão de aposentadoria ao servidor público federal (...) será assegurada,
> **a qualquer tempo**, desde que tenham sido cumpridos os requisitos para
> obtenção desses benefícios **até a data de entrada em vigor desta Emenda
> Constitucional** (...)
>
> (`fontes-oficiais/arquivos/planalto-emc103.htm`, arquivo **cp1252** — decodificar
> como UTF-8 devolve zero sem erro)

Mesma arquitetura: "assegurada a qualquer tempo" + "desde que cumpridos até
\<data>". No texto federal não há ambiguidade possível — "a qualquer tempo"
convive com um prazo duro de implemento, que é a própria data da emenda. Se ali a
oração não dispensa o prazo, aqui também não.

O que Rondônia mudou foi **só a data**, e no sentido mais generoso: em vez de
exigir requisitos completos na entrada em vigor da emenda, abriu três anos e meio
de graça. Isso faz do art. 4º **regra de transição**, não cláusula declaratória
de direito adquirido — e é o que torna o prazo eficaz contra expectativa de
direito, sem tocar em quem já havia adquirido o seu (art. 5º, XXXVI da CF;
Súmula 359 do STF).

## Para `0008`/`0009` o prazo é duplamente determinado

Essas duas fundam-se no **art. 6º-A da EC 41/2003**, que o art. 35, IV da EC
103/2019 revogou e cuja revogação o **art. 12, II da própria ECE 146/2021
referenda integralmente**, nos termos do art. 36, II da emenda federal.

Logo elas não dependem do art. 4º só para o prazo: dependem dele para **existir**.
O que mantém o art. 6º-A aplicável no RPPS de Rondônia é a graça do art. 4º, e só
dentro dela. Duas rotas independentes chegam à mesma data.

*(Fica aberta, e não é desta auditoria, a questão de se referendo por emenda
constitucional estadual satisfaz o art. 36, II, que fala em "lei" de iniciativa
privativa do Executivo — ver [`achado-0036`](achado-0036.md). Se a resposta for
negativa, esta seção cai e o prazo permanece pela rota acima.)*

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

  **Confirmado em 2026-07-29** pela
  [análise jurídica](../../../docs/analysis/analise-juridica-art-4-ece-146.md), por
  duas vias. O requisito de uma regra de incapacidade é um **evento**, não um
  acúmulo — "cumpridos até 31/12/2024" quer dizer incapacidade *constituída* até
  ali, data verificável no caso concreto. E existe **família sucessora já no
  catálogo**: `0019`–`0022` são incapacidade permanente pela redação da EC
  103/2019 c/c art. 30 da LCE 1.100/2021, nas duas coortes de ingresso. Fechar
  `0006`–`0009` em 2024 **não abre lacuna de cobertura**, e a sobreposição entre
  23/10/2021 e 31/12/2024 é o desenho que uma regra de graça produz.

- **`0039`/`0040` saem deste diagnóstico.** A mesma análise encontrou nelas
  defeito **anterior** à janela: os requisitos são fundados na redação da EC
  20/1998 do art. 40, § 1º, III, "a" e § 5º, extinta em 30/12/2003, e as regras
  se aplicam a quem ingressou **após 31/12/2003**. O art. 4º preserva a
  legislação vigente em 2021, não uma revogada dezoito anos antes, e a janela de
  admissão exclui direito adquirido. Gravar `31/12/2024` nelas produziria regra
  formalmente arrumada e materialmente sem base. Autorado em
  [`achado-0051`](achado-0051.md), e os dois têm de ser decididos juntos.

**Severidade `bloqueante` por escolha do auditor**: `data_direito_ate` é campo
deployável, e uma janela aberta onde o dispositivo invocado a fecha permitiria
ao Sisprev conceder benefício sob regra cujo prazo expirou. Isso impede
`revisada` nas sete até que a decisão seja tomada — que é o comportamento
desejado, não um efeito colateral.
