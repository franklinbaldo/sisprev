---
type: Achado
id: achado-0024
nome: As duas datas de janela do quarteto regra-0019 a regra-0022 não constam de nenhum dispositivo citado — e uma delas deixa o dia 01/01/2004 sem regra de incapacidade
situacao: aberto
severidade: informativo
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

Duas datas gravadas nas regras de incapacidade permanente do regime da LCE
1.100/2021 não correspondem a marco nenhum dos dispositivos que as próprias
regras citam:

| campo               | valor      | regras                 | marco da norma citada                 |
| ------------------- | ---------- | ---------------------- | ------------------------------------- |
| `data_direito_apos` | 23/10/2021 | `0019`–`0022` (quatro) | LCE 1.100/2021 → 18/10/2021 no bundle |
| `data_adm_apos`     | 01/01/2004 | `0021`, `0022`         | corte legal → **31/12/2003**          |

O segundo tem consequência aritmética imediata. Sob a semântica confirmada
(`DATA_*_ATE` inclusivo, `DATA_ADM_APOS` exclusivo — ver
[`docs/spec/regra.md`](../../../docs/spec/regra.md), "Elegibilidade
temporal"), `regra-0019`/`0020` cobrem admissões **até 31/12/2003 inclusive**
e `regra-0021`/`0022` cobrem admissões **a partir de 02/01/2004**. **O dia
01/01/2004 não é coberto por nenhuma das quatro** — e é um dia que a lei
atribui inequivocamente ao ramo pós-2003.

As quatro se organizam em duas partições paralelas do mesmo benefício, uma
por trilho de cálculo: `0019`/`0020` no ramo até 2003 (proventos integrais e
proporcionais) e `0021`/`0022` no ramo após 2003 (idem). Cada partição tem o
mesmo dia descoberto, pelo mesmo valor gravado.

O primeiro é mais interessante do que parecia, porque **não se sabe de que
lado está o erro**: a divergência pode ser das quatro regras ou do
`vigencia_inicio` que o bundle declara para a LCE 1.100/2021.

# Evidências

Conferido na compilação oficial da LCE 1.100/2021 da DITEL/Casa Civil,
arquivada localmente (`fontes-oficiais/arquivos/ditel-LC1100---COMPILAÇÃO.txt`,
`sha256` no `fontes-oficiais/manifesto.yaml`).

## `01/01/2004` — o corte legal é 31 de dezembro de 2003, literal

Os três artigos de cálculo e reajuste do regime nomeiam a data no próprio
corpo, com a mesma grafia:

- **art. 24** — "que tenham ingressado no serviço público em cargo efetivo
  **após 31 de dezembro de 2003**";
- **art. 25** — "que tenha ingressado no serviço público em cargo efetivo
  **até 31 de dezembro de 2003**";
- **art. 27, I e II** — a mesma partição, "até" e "após 31 de dezembro de
  2003".

Nenhum deles menciona 1º de janeiro de 2004. O marco da lei é **31/12/2003**,
e a coluna `DATA_ADM_APOS` é exatamente a que grava marco exclusivo: `apos = 31/12/2003` significa "admitido a partir de 01/01/2004", que é a intenção
evidente do valor gravado. Gravar `01/01/2004` no campo `APOS` desloca a
cobertura um dia para frente.

A partição que a lei quer, e a que o catálogo produz:

```
lei:              [...  31/12/2003]  [01/01/2004  ...]
regra-0019/0022:  [...  31/12/2003]         [02/01/2004  ...]
                                    ^
                                    01/01/2004 — descoberto
```

Isto é o item **02** da §5.2 de
[`semantica-das-janelas-temporais.md`](../../../docs/analysis/semantica-das-janelas-temporais.md),
que registra o mesmo valor em `0014`, `0015`, `0021`, `0022`, `0057` e `0058`.
O que este achado acrescenta é o **par concreto**: aqui as duas metades da
partição existem e são conferíveis lado a lado (`0019` fecha em 31/12/2003,
`0022` abre em 01/01/2004), e a lei que ambas citam nomeia a fronteira em
texto. Não é inferência sobre convenção — é a fronteira escrita na norma.

O dia 01/01/2004 é feriado, o que torna improvável (não impossível) que uma
posse ou exercício tenha caído nele. Isso reduz a probabilidade do dano, não a
existência do defeito — e `DATA_ADM_*` ainda não teve confirmado a que ato se
refere (nomeação, posse, exercício), de modo que nem a improbabilidade está
estabelecida.

## `23/10/2021` — não está no texto da norma, e o lado do erro é indeterminado

Duas buscas exaustivas no texto oficial arquivado:

| busca             | ocorrências |
| ----------------- | ----------- |
| `23 de outubro`   | **0**       |
| `outubro de 2021` | 1           |

A única ocorrência é a cláusula de encerramento:

> **Art. 115.** Esta Lei Complementar entra em vigor **na data de sua
> publicação**.
>
> Palácio do Governo do Estado de Rondônia, em **18 de outubro de 2021**, 133º
> da República.

E o art. 114 revoga a LCE 432/2008 — sem prazo diferido —, de modo que a mesma
data decide as duas pontas da sucessão de regimes. O art. 30, que as quatro
regras citam, **não tem vacatio própria nem cláusula de produção diferida de
efeitos**: percorrido o artigo inteiro (*caput* e §§ 1º a 14), nenhum
parágrafo difere a aplicação.

**Aqui está o ponto que inverte a pergunta.** A norma entra em vigor na data
da **publicação**; 18/10/2021 é a data em que foi **assinada no Palácio**. As
duas podem coincidir e frequentemente não coincidem. O bundle declara
`vigencia_inicio: 2021-10-18` para a norma e para os onze dispositivos dela —
data que **nenhuma fonte arquivada estabelece como a da publicação**, e que só
pode ter vindo da datação do fecho. Se o Diário Oficial do Estado publicou a
lei em 23/10/2021, então `data_direito_apos: 23/10/2021` é exatamente o marco
correto pela convenção confirmada do catálogo, e o que está errado é o
`vigencia_inicio` do bundle — junto com o `vigencia_fim: 2021-10-18` dos
dispositivos revogados da LCE 432/2008.

O que **pesa contra** essa hipótese, e é evidência interna e mecânica: das 26
regras que gravam um marco da LCE 1.100/2021 em `data_direito_apos`, **22
gravam 18/10/2021 e apenas 4 gravam 23/10/2021** — e as quatro são exatamente
`0019`–`0022`, um bloco contíguo do mesmo benefício. Pela hipótese da
publicação em 23/10, as 22 estariam erradas; pela hipótese oposta, as 4. O
padrão de lote (mesmo benefício, ids adjacentes) sugere preenchimento de um
autor ou de uma remessa, não decisão jurídica — é o mesmo formato de argumento
do [`achado-0015`](achado-0015.md), com a ressalva de que ali a contagem era
68 × 3 e aqui é 22 × 4.

**Nenhuma das duas hipóteses está fechada, e nenhuma fonte arquivada as
separa.** O que as separa é um documento: a edição do Diário Oficial do Estado
de Rondônia de outubro de 2021 que publicou a LCE 1.100/2021. Ela não está em
`fontes-oficiais/` (o manifesto tem a compilação da DITEL e nada do DOE).

## Limite desta conferência, declarado

- A fonte é a **compilação** da DITEL, não a publicação original no DOE. É
  precisamente essa a lacuna que impede fechar o caso do `23/10/2021`: o
  compilado reproduz o fecho do texto, não a folha do Diário.
- A leitura de `DATA_DIREITO_APOS` **não está confirmada** (issue #39; §1.2 do
  documento de janelas temporais). A afirmação sobre o dia descoberto acima
  vale para o eixo de **admissão**, onde `DATA_ADM_APOS` exclusivo *está*
  confirmado. Para `data_direito_apos: 23/10/2021` este achado não afirma qual
  dia a janela passa a cobrir — só que o valor gravado não corresponde a marco
  nenhum.
- `data_direito_ate: 31/12/2099` das duas é **sentinela e segue não
  interpretada** (P5). Nada aqui a lê como "sem limite".
- **A conferência documental foi feita sobre `0019` e `0022`**, as duas metades
  conferíveis lado a lado. `regra-0020` e `regra-0021` gravam as mesmas datas
  — `23/10/2021` as quatro, `01/01/2004` a `0021` — e por isso **estão em
  `regras_afetadas`**: a população do achado é a do defeito, não a do lote de
  conferência. Um lote pode limitar o que foi investigado; não pode limitar
  quem responde ao achado depois que o próprio texto afirma que o defeito
  também está lá. Deixá-las fora as faria atravessar o gate de
  `disposicao_de_achados` sem dispor de um defeito já nomeado.

# Consequência prática

As quatro colunas de data são **deployáveis** e são o que decide qual regra
alcança um requerimento.

No eixo de admissão o efeito é nomeável: um servidor empossado em 01/01/2004
que se aposente por incapacidade permanente não é alcançado por
`regra-0019`/`0020` (fechadas em 31/12/2003) nem por `regra-0021`/`0022`
(abertas a partir de 02/01/2004), embora a LCE 1.100/2021 o coloque sem
ambiguidade no ramo pós-2003. Como as quatro são as únicas regras do benefício
nesse regime, o requerimento cai fora de todas — em qualquer dos dois trilhos
de cálculo.

No eixo de direito o efeito depende de qual lado cede, e as duas
possibilidades doem em direções opostas. Se as quatro regras estão erradas, os
requerimentos cujo direito se perfez entre 18 e 23/10/2021 não encontram a
regra do regime que já vigia — e encontram, pela sentinela, as regras do regime
revogado (`0006`–`0009`, `data_direito_ate: 31/12/2099`). Se é o bundle que
está errado, então 22 regras de outros benefícios abrem cinco dias antes da
vigência da norma que citam, e o defeito é muito maior do que este achado.

# Questão a investigar

1. **Obter a edição do DOE/RO que publicou a LCE 1.100/2021.** É o único
   documento que decide o `23/10/2021`, e decide de uma vez a vigência da LCE
   1.100/2021, a revogação da LCE 432/2008 e as 26 regras que gravam esse
   marco. Enquanto ele não existir em `fontes-oficiais/`, a pergunta não é
   respondível — e o `vigencia_inicio: 2021-10-18` do bundle deve ser lido
   como **data de assinatura tomada por data de publicação**, não como fato
   conferido.

2. **Confirmar que `01/01/2004` deveria ser `31/12/2003`.** A correção é
   mecânica e a fronteira está escrita na lei; o que falta é a decisão de quem
   responde pelo campo. É pergunta idêntica para as outras quatro regras que
   gravam o mesmo valor.

3. **A que ato `DATA_ADM_*` se refere.** Sem isso não se sabe sequer se
   "admitido em 01/01/2004" é um estado possível — o que decide se o dia
   descoberto é dano real ou apenas defeito formal. É a pendência 5.3.1 do
   documento de janelas temporais.

4. **Se estes casos entram em achado único com os demais marcos sem
   fundamento.** A §5.4 daquele documento deixa a granularidade em aberto.
   Este achado escolhe o recorte **por família de regras** — as de
   incapacidade do regime vigente —, porque a correção de cada valor é decisão
   do mesmo dono de campo e a evidência é a mesma norma. Um achado por *valor*
   (todos os `01/01/2004` do catálogo, todos os `23/10/2021`) é o recorte
   alternativo, e é o que faria sentido se a decisão for tomada de uma vez
   para o catálogo inteiro.
