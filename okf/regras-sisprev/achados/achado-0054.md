---
type: Achado
id: achado-0054
nome: Duas normas exigem as mesmas três faixas fixas de pontos e as regras gravam tabelapontuacao oposto — S na transição, N no regime permanente
situacao: aberto
severidade: informativo
verificacao: manual
natureza: dados
regras_afetadas:
  - /regras/regra-0065.md
  - /regras/regra-0066.md
  - /regras/regra-0067.md
  - /regras/regra-0068.md
  - /regras/regra-0069.md
  - /regras/regra-0070.md
  - /regras/regra-0071.md
detectado_em: 2026-07-30
detectado_por: franklinbaldo
---

# Descrição

Duas normas distintas concedem aposentadoria por exposição a agentes nocivos com
a **mesma estrutura de requisito** e as **mesmas três faixas**:

- **ECE 146/2021, art. 8º** — regra de transição, para quem ingressou até
  14/09/2021;
- **LCE 1.100/2021, art. 41** — regra permanente.

Os dois caputs dizem "quando o total da soma resultante da sua idade e do tempo de
contribuição e o tempo de efetiva exposição forem, **respectivamente**, de:", e os
dois listam 66 pontos com 15 anos de exposição, 76 com 20, 86 com 25.

As regras que os aplicam gravam `tabelapontuacao` **oposto**:

| regras                 | norma                   | `tabelapontuacao` |
| ---------------------- | ----------------------- | ----------------- |
| 0068, 0069, 0070       | ECE 146/2021, art. 8º   | `S`               |
| 0065, 0066, 0067, 0071 | LCE 1.100/2021, art. 41 | `N`               |

Mesmo requisito, mesmas faixas, marcação contrária.

# Evidências

**As cinco transcrições que tornam isto conferível foram feitas em 2026-07-30.**
Antes existiam apenas `ece-146-2021/art-8-par-1`, `art-8-par-2` e
`lce-1100-2021/art-41-inc-iii` — as faixas do art. 8º não estavam no bundle, e as
do art. 41 estavam pela metade. Agora os três incisos do art. 8º e os três do art.
41 estão transcritos, cada parágrafo conferido literalmente contra a fonte
arquivada em `fontes-oficiais/`. A coincidência das faixas foi **lida nos dois
textos**, nunca presumida de um para o outro.

**A leitura vigente de `tabelapontuacao` é "tabela progressiva", e ela já estava
registrada.** O checklist da `regra-0086` diz, sobre um somatório fixo:

> `tabelapontuacao: N` coerente: a soma 95 do art. 3º é fixa e resulta de redução
> de idade, não de tabela progressiva — ao contrário do art. 5º, V da ECE
> 146/2021, cujo somatório de pontos cresce 1 por ano e onde as regras gravam `S`

O art. 5º, V da ECE 146/2021 tem a progressão no § 2º: "a partir de 1° de janeiro
de 2022, a pontuação [...] será acrescida a cada ano de 1 (um) ponto, até atingir
o limite de 100 (cem) pontos, se mulher e de 105 (cento e cinco) pontos, se
homem". As regras do art. 5º gravam `S`, e são coerentes com essa leitura.

**Nem o art. 8º da ECE nem o art. 41 da LCE têm cláusula de progressão.** Nos
dois, o único parágrafo sobre a apuração é o que manda contar idade e tempo de
contribuição **em dias** para o somatório — que é forma de apuração, não
progressão. As faixas são fixas nos dois.

Daí o desenho do defeito: sob a leitura progressiva, **as três regras da transição
são as destoantes**, e não as quatro do permanente. São o único `S` do catálogo
cujo dispositivo não tem progressão, e as regras estruturalmente idênticas do
outro regime gravam `N`.

# Consequência prática

A inconsistência está **demonstrada**: mesma estrutura de requisito, mesmas
faixas, marcação oposta. Uma das duas marcações está errada, e as duas não podem
estar certas ao mesmo tempo.

**A direção adotada pela auditoria é a leitura progressiva.** Ela é a única
explicação documentada no corpus e distingue precisamente as normas que têm
progressão anual das que têm somatórios fixos. Assim, `N` fica preservado no
art. 41 e as três regras da transição, 0068–0070, são as candidatas à correção
para `N`. A leitura ampla (“qualquer regra exige pontos”) foi rejeitada porque
contradiz o uso de `N` na `regra-0086` para soma fixa.

Se a coluna aciona consulta a tabela externa de pontuação, a diferença tem
consequência operacional: um dos dois conjuntos não recebe a aferição que o outro
recebe, para um requisito que a norma escreve igual nos dois.

**Por que `informativo`, e não `bloqueante`.** O critério de severidade da
[spec](../../../okf/spec/regra.md) exige demonstração de que o campo deployável
contradiz a norma aplicável. O que está demonstrado aqui é a **contradição entre
as duas marcações**; qual delas contradiz a norma depende do significado da
coluna, que é questão aberta. É a mesma posição do
[`achado-0053`](achado-0053.md) e o mesmo precedente do
[`achado-0024`](achado-0024.md): se a Q9 confirmar a leitura progressiva, este
achado passa a `bloqueante` sem que nenhum fato sobre o campo mude — o que muda é
o direito de afirmar.

# Questão a investigar

1. Propor a troca de `S` para `N` nas regras 0068–0070 pelo veículo de
   substituição, sem editar diretamente o catálogo legado. A proposta está
   registrada na unidade [`agentes-nocivos-ece-146-2021`](../../regras-propostas/regras/agentes-nocivos-ece-146-2021.md)
   e no conjunto [`proposta-auditoria-2026-07`](../../conjuntos/proposta-auditoria-2026-07.md).
2. Manter `N` nas seis regras propostas do art. 41.
3. Preservar como verificação adicional, não como bloqueio dessas unidades, um
   teste funcional que demonstre a tela ou tabela acionada pelo campo.
4. Usar `predicados.faixa_exposicao` nas regras propostas para carregar a
   distinção 66/15, 76/20 e 86/25 que o schema legado não expressa.

# Resolução

Em 2026-07-30, a auditoria adotou `tabelapontuacao` como sinalizador de tabela
progressiva. Isso resolve a direção do achado: o `N` do regime permanente é
coerente, e o `S` da transição é o defeito a corrigir. O achado permanece aberto
até existir proposta específica para 0068–0070; a dúvida não bloqueia mais as
unidades do art. 41.
