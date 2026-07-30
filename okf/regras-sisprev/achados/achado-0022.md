---
type: Achado
id: achado-0022
nome: Cinco regras invocam o art. 4º da ECE 146/2021 e gravam data_direito_ate 31/12/2099, contra o prazo de 31/12/2024 do próprio dispositivo
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
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

Cinco regras fundam os seus **requisitos** em legislação anterior à ECE
146/2021, invocam o art. 4º dessa emenda — que é o dispositivo que preserva
aquela legislação — e gravam `data_direito_ate: 31/12/2099`, a sentinela de
"sem limite".

O art. 4º preserva a legislação anterior **com prazo**:

> Art. 4º A concessão de aposentadoria [...] observará os requisitos e os
> critérios exigidos pela legislação vigente até a data de entrada em vigor
> desta Emenda Constitucional, **desde que sejam cumpridos até 31 de dezembro
> de 2024**, sendo assegurada a qualquer tempo.

Sob a semântica que a Q1 fechou — `DATA_DIREITO_ATE` é o prazo de implementação
dos requisitos —, essas cinco regras deveriam fechar em `31/12/2024`.

**Recorte de escopo (2026-07-30).** A primeira versão deste achado alcançava
sete regras, incluindo `regra-0039`/`0040`. Elas foram **retiradas de
`regras_afetadas`** porque o defeito anterior de fundamentação, registrado no
[`achado-0051`](achado-0051.md), impede concluir neste momento qual deve ser a
janela delas. Se o fundamento for corrigido para norma anterior efetivamente
preservada pelo art. 4º, elas poderão voltar a incidir aqui.

O motivo de retirar em vez de só anotar: `regras_afetadas` tem **efeito
mecânico** — é o campo que determina quem precisa dispor deste achado para
chegar a `revisada`, e sendo ele `bloqueante`, quem ele nomeia não chega lá por
caminho nenhum. Escopo declarado divergindo de escopo mecânico bloquearia duas
regras pelo defeito errado.

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

Duas corroborações, e a segunda é a que sustenta a acusação:

1. **A `0032` abre o direito em `18/10/2021`**, a entrada em vigor da LCE
   1.100/2021 — dentro do período que o art. 4º garante e que termina em
   31/12/2024.
2. **O catálogo já pratica a leitura correta em 12 regras.** Das 24 que
   vinculam o art. 4º, `0012`, `0013`, `0097`–`0106` fecham em `31/12/2024` —
   todas de legislação anterior à EC 146 (art. 40, § 7º e arts. 2º e 6º da
   EC 41/2003; art. 3º da EC 47/2005). A divergência é destas cinco, não da
   interpretação.

A oração "sendo assegurada a qualquer tempo" **não** justifica a sentinela: ela
fala do momento da concessão, não do implemento dos requisitos. Quem cumpriu
até 31/12/2024 requer depois; quem não cumpriu não passa a poder cumprir.

## O modelo federal corrobora essa leitura, sem fechá-la

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

## Não há norma estadual alternativa que sustente a sentinela

A objeção que faltava responder é se a **LCE 1.100/2021**, a lei que implementa a
reforma, teria cláusula de transição própria — o que daria às cinco regras outro
fundamento para não fechar.

Não tem. Busca exaustiva na compilação oficial (166 mil caracteres): **zero**
ocorrências de "transição" e **zero** de "31 de dezembro de 2024". O art. 114
revoga a LCE 432/2008 integralmente, e nada põe no lugar em matéria de
transição. Logo o art. 4º da emenda é a **única ponte** do regime anterior para o
novo, e toda regra que aplica requisitos pré-2021 depois de 18/10/2021 depende
dele — e do prazo dele.

O que a lei estadual tem é preservação de **fórmula**, não de requisito: quatro
ressalvas de "direito adquirido a outra fórmula", duas delas nos §§ 13 e 14 do
art. 30 (incapacidade permanente). Elas convivem com o art. 4º em eixos
diferentes — a emenda governa até quando os requisitos podem ser implementados, a
lei governa qual fórmula se aplica a quem os implementou — e são **mais
estreitas**, porque falam de quem já adquiriu o direito.

Detalhamento na [análise jurídica](../../../docs/analysis/analise-juridica-art-4-ece-146.md) §9.

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

A correção é uniforme (`data_direito_ate: 31/12/2024` nas cinco) ou alguma delas
tem fundamento próprio para não fechar?

Duas frentes concretas:

- **`0032` tem divergência interna anterior a esta.** O `nome` a funda na EC
  103/2019 e na LC 1.100/2021 (regime novo); a fundamentação, na EC 88/2015 e
  na LC 152/2015 (anterior à EC 146). Se o nome estiver certo, a regra é de
  regime novo e o problema deixa de ser a janela: passa a ser a citação do
  art. 4º. Registrado em achado próprio.

- **`0006`/`0007` são do regime permanente**, e o fundamento disso é a **norma
  citada**, não o dado: o art. 40, § 1º, I é a provisão permanente de
  incapacidade, ao contrário do art. 6º-A da EC 41/2003, que é transição e
  condiciona expressamente o ingresso.

  Correção de método (2026-07-30): uma versão anterior deste item dizia "sem
  corte de ingresso", apoiada em `data_adm_ate: 31/12/2099`. **Os dois limites de
  admissão dessas duas regras são sentinela** (`01/01/1950` e `31/12/2099`), e
  ler sentinela como "sem limite" é o que o P5 proíbe. O que se afirma é que
  elas **não declaram coorte de ingresso conferível** — diferente de `0008`/
  `0009`, cujo `data_adm_ate: 31/12/2003` é marco real.

  A consequência de fechar em 2024 é que a incapacidade
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

- **`0039`/`0040` foram retiradas do escopo** (ver o recorte na Descrição), e
  não só do diagnóstico. Nelas o defeito é **anterior** à janela: os requisitos
  são fundados na redação da EC 20/1998 do art. 40, § 1º, III, "a" e § 5º,
  extinta em 30/12/2003, e as regras se aplicam a quem ingressou **após
  31/12/2003** — este sim marco real, não sentinela. O art. 4º preserva a
  legislação vigente em 2021, não uma revogada dezoito anos antes. Autorado em
  [`achado-0051`](achado-0051.md), que é quem as bloqueia, pelo defeito correto.

**Severidade `bloqueante` por escolha do auditor**: `data_direito_ate` é campo
deployável, e uma janela aberta onde o dispositivo invocado a fecha permitiria
ao Sisprev conceder benefício sob regra cujo prazo expirou. Isso impede
`revisada` nas cinco até que a decisão seja tomada — que é o comportamento
desejado, não um efeito colateral.
