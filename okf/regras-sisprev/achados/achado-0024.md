---
type: Achado
id: achado-0024
nome: As duas datas de janela do quarteto regra-0019 a regra-0022 não constam de nenhum dispositivo citado — uma deixa o dia 01/01/2004 sem regra de incapacidade e a outra manda cinco dias de requerimento para o regime revogado
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

Duas datas gravadas nas regras de incapacidade permanente do regime da LCE
1.100/2021 não correspondem a marco nenhum dos dispositivos que as próprias
regras citam:

| campo               | valor      | regras                 | marco da norma citada                                    |
| ------------------- | ---------- | ---------------------- | -------------------------------------------------------- |
| `data_direito_apos` | 23/10/2021 | `0019`–`0022` (quatro) | publicação da LCE 1.100/2021 → **18/10/2021**, conferida |
| `data_adm_apos`     | 01/01/2004 | `0021`, `0022`         | corte legal → **31/12/2003**, literal na lei             |

**Os dois valores estão errados, e as duas conferências estão fechadas** — a do
`01/01/2004` contra o texto da lei, a do `23/10/2021` contra a publicação no
Diário Oficial (DOE/RO nº 207, 18/10/2021). Nenhuma das duas depende mais de
hipótese sobre convenção de fronteira.

O `01/01/2004` tem consequência aritmética imediata. Sob a semântica confirmada
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

O `23/10/2021` era, até 2026-07-29, o item em que **não se sabia de que lado
estava o erro** — das quatro regras ou do `vigencia_inicio` que o bundle declara
para a LCE 1.100/2021. A publicação foi conferida e a simetria caiu: o bundle
está certo, as quatro regras não. O histórico da dúvida fica registrado adiante
porque é ele que mostra por que a coincidência entre o fecho e a publicação não
podia ser presumida.

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

## `23/10/2021` — a publicação foi conferida, e são as quatro regras que estão erradas

**Resolvido em 2026-07-29.** A LCE 1.100/2021 foi publicada no **Diário Oficial
do Estado de Rondônia nº 207**, com **publicação em 18/10/2021** e
disponibilização em 19/10/2021. Logo:

- o `vigencia_inicio: 2021-10-18` da norma e dos onze dispositivos dela está
  **certo**, e agora por fato conferido, não por datação do fecho;
- o `vigencia_fim: 2021-10-18` dos dispositivos revogados da LCE 432/2008 idem;
- as **22 regras** que gravam `18/10/2021` em `data_direito_apos` estão certas;
- as **quatro** que gravam `23/10/2021` — `0019` a `0022` — estão **erradas**.
  O valor não corresponde a marco nenhum: não é a publicação, não é a
  assinatura, não é a disponibilização, e não aparece no texto da norma.

Fontes arquivadas em `fontes-oficiais/` (`sha256` no `manifesto.yaml`) e
declaradas em `fontes:` da norma:

| fonte                                            | o que estabelece                                                       |
| ------------------------------------------------ | ---------------------------------------------------------------------- |
| ficha da norma no SAPL/ALE-RO (`sapl-9979`)      | "Data de Publicação 18/10/2021 / Veículo de Publicação D.O.E. nº 207"  |
| texto original ali arquivado (`sapl-lc1100.pdf`) | a publicação digitalizada; `CreationDate` do PDF é `2021-10-19T14:21Z` |

A ficha do SAPL nomeia a **edição** do Diário — metadado que não vem do texto
da norma —, e é isso que a distingue de uma leitura do fecho. Foi exatamente a
ausência dessa peça que impedia fechar o caso: a compilação da DITEL reproduz o
fecho, não a folha do Diário.

**A disponibilização posterior é o que torna a coincidência informativa, não
trivial.** O carimbo de criação do PDF (19/10) confirma que a edição só ficou
disponível no dia seguinte ao da publicação — ou seja, este *era* um caso em
que assinatura e publicação poderiam divergir, e a hipótese de 23/10 tinha de
ser testada em vez de descartada. Ela foi testada e caiu: o DOE/RO data a
publicação pela edição, não pela entrega.

Nada disto foi inferido da contagem de lote. O argumento mecânico abaixo — 22
regras contra 4 — apontava para o mesmo lado e **não o provava**; ele agora está
apenas confirmado por fora. Registrado porque a ordem importa: se a contagem
tivesse sido tomada como prova, a conclusão certa teria sido alcançada pelo
método errado, e o mesmo método aplicado ao `achado-0015` (68 × 3) continuaria
sem valer.

### O que a norma diz, e o que ela não diz

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

**Por que a pergunta era aberta antes da publicação ser conferida.** A norma
entra em vigor na data da **publicação**; 18/10/2021 é, no texto, apenas a data
em que ela foi **assinada no Palácio**. As duas podem coincidir e frequentemente
não coincidem, e o `vigencia_inicio: 2021-10-18` do bundle só podia ter vindo da
datação do fecho — nenhuma fonte então arquivada o estabelecia como data de
publicação. Se o DOE tivesse publicado a lei em 23/10/2021, `23/10/2021` seria o
marco correto e o errado seria o bundle inteiro, junto com o
`vigencia_fim: 2021-10-18` dos dispositivos revogados da LCE 432/2008. É essa
simetria que a ficha do SAPL rompeu.

A evidência **interna e mecânica**, que apontava para o mesmo lado sem provar:
das 26 regras que gravam um marco da LCE 1.100/2021 em `data_direito_apos`, **22
gravam 18/10/2021 e apenas 4 gravam 23/10/2021** — e as quatro são exatamente
`0019`–`0022`, um bloco contíguo do mesmo benefício. O padrão de lote (mesmo
benefício, ids adjacentes) sugere preenchimento de um autor ou de uma remessa,
não decisão jurídica — é o mesmo formato de argumento do
[`achado-0015`](achado-0015.md), com a ressalva de que ali a contagem era 68 × 3
e aqui é 22 × 4.

Ele continua **não sendo prova**, e é útil que o caso tenha sido decidido por
fora: uma contagem de lote diz onde está a minoria, não onde está o erro. Aqui
os dois coincidiram; no `achado-0015` a coincidência segue por verificar.

## Limite desta conferência, declarado

- O texto conferido é a **compilação** da DITEL; a **publicação** é conferida
  pela ficha do SAPL, que nomeia a edição do DOE. O PDF do texto original é
  **digitalização sem camada de texto**, de modo que a folha do Diário está
  arquivada mas não é pesquisável por busca — a data vem do metadado da ficha,
  não de leitura do carimbo. Quem quiser conferir o carimbo à vista tem o
  arquivo em `fontes-oficiais/arquivos/sapl-lc1100.pdf`.
- A **disponibilização em 19/10/2021** está sustentada pelo `CreationDate` do
  PDF arquivado, não por leitura da folha. É datum corroborante, não a peça que
  decide — a que decide é a publicação em 18/10, e ela não depende dele.
- A leitura de `DATA_DIREITO_APOS` **segue não confirmada** (issue #37 depois da
  reescrita; §1.2 do documento de janelas temporais). O que este achado afirma
  é que `23/10/2021` **não corresponde a marco nenhum** da norma — o que vale
  sob qualquer semântica de fronteira, porque nenhuma delas produz 23/10 a
  partir de 18/10. **Qual dia** a janela corrigida passa a cobrir é que depende
  da Q2, e não é afirmado aqui.
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

No eixo de direito o efeito **deixou de ser condicional**. Confirmada a
publicação em 18/10/2021, o dano é nomeável: os requerimentos cujo direito se
perfez entre **18 e 23/10/2021** não encontram nenhuma das quatro regras do
regime que já vigia. E não caem no vazio — caem, pela sentinela, nas regras do
regime **revogado** (`0006`–`0009`, `data_direito_ate: 31/12/2099`), que a LCE
1.100/2021 revogou pelo art. 114 sem prazo diferido. São cinco dias em que o
catálogo roteia o requerimento para a lei errada, em vez de não roteá-lo.

A hipótese oposta está descartada: as 22 regras que gravam 18/10/2021 **não**
abrem antes da vigência da norma que citam, porque a vigência é essa data.

**Severidade `bloqueante`.** Pelo critério de
[`docs/spec/regra.md`](../../../docs/spec/regra.md) ("Quando um achado é
`bloqueante`"), o achado passou a satisfazer os três termos que antes não
satisfazia: campo **deployável** (as quatro colunas de data decidem seleção),
contradição com a **norma aplicável** (nem 23/10 nem 01/01/2004 é marco dela) e,
o que faltava, **demonstrada** — a conferência da publicação está fechada contra
fonte arquivada. Enquanto o lado do erro era indeterminado, `informativo` era a
classificação correta justamente porque bloquear exigiria fixar a hipótese que o
achado declarava aberta. Ela não está mais aberta.

# Questão a investigar

1. ~~**Obter a edição do DOE/RO que publicou a LCE 1.100/2021.**~~
   **Respondido em 2026-07-29**: DOE/RO **nº 207**, publicação em **18/10/2021**
   (disponibilização em 19/10). A ficha da norma no SAPL/ALE-RO e o texto
   original ali arquivado estão em `fontes-oficiais/` e em `fontes:` da norma.
   Decorre daí, de uma vez: a vigência da LCE 1.100/2021 e a revogação da LCE
   432/2008 em 18/10/2021 — ambas confirmadas como já estavam no bundle — e o
   erro das quatro regras que gravam `23/10/2021`. O que resta é decisão do dono
   do campo, não investigação.

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
