---
type: Achado
id: achado-0039
nome: As quatro janelas de regra-0111 e regra-0112 são as do art. 4º da ECE 146/2021, e a fundamentação delas é a do art. 7º — duas vias de transição diferentes na mesma regra
situacao: aberto
severidade: informativo
verificacao: manual
natureza: juridica
regras_afetadas:
  - /regras/regra-0111.md
  - /regras/regra-0112.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

A ECE 146/2021 abre **duas** vias de transição que um policial civil pode
percorrer, e elas têm requisitos e prazos diferentes:

- **art. 4º** — preserva os requisitos da *legislação anterior* à Emenda,
  "desde que sejam cumpridos **até 31 de dezembro de 2024**, sendo assegurada a
  qualquer tempo". Para o policial, essa legislação anterior é a LC 51/1985:
  30 anos de contribuição e 20 de exercício policial se homem, **sem idade
  mínima**. O parágrafo único manda calcular e reajustar os proventos também
  pela legislação anterior.
- **art. 7º** — regra criada *pela própria Emenda*, para quem ingressou na
  carreira **até 13/11/2019**: aposenta-se na forma da LC 51/1985 mas
  **observada idade mínima de 55 anos**, ou 52/53 com o pedágio do § 2º. **Não
  tem prazo**: nada nele termina em 31/12/2024.

`regra-0111` e `regra-0112` gravam, nos quatro campos de janela, exatamente a
via do **art. 4º** — e o `nome` das duas o diz. A `fundamentacao_integral`
delas, que é o único campo de fundamentação preenchido, descreve a via do
**art. 7º**, e é o mesmo texto das seis regras que percorrem essa via.

# Evidências

## As janelas dizem art. 4º; a fundamentação diz art. 7º

Comparação com `regra-0072`–`regra-0077`, as seis regras cuja
`fundamentacao_integral` é **a mesma string**:

| campo                    | `0072`–`0077`             | `0111`/`0112`                       | quem explica o valor de `0111`/`0112`           |
| ------------------------ | ------------------------- | ----------------------------------- | ----------------------------------------------- |
| `data_adm_ate`           | 13/11/2019                | **31/12/2003**                      | não é o corte do art. 7º (13/11/2019)           |
| `data_direito_apos`      | 14/09/2021                | **01/01/1910**                      | art. 4º: "assegurada a qualquer tempo"          |
| `data_direito_ate`       | 31/12/2099 (sentinela)    | **31/12/2024**                      | art. 4º: "cumpridos até 31 de dezembro de 2024" |
| `nome`                   | "Art. 7º, §§ 2º e 3º ..." | "... c/c art. 4º da EC nº 146/2021" | art. 4º, nomeado                                |
| `fundamentacao_integral` | texto X                   | texto X (um espaço a menos)         | art. 7º, §§ 2º e 3º                             |
| `dispositivos:`          | art-7-par-2, art-7-par-3  | **os mesmos**                       | art. 7º                                         |

A `fundamentacao_integral` de `0111`/`0112` difere da das seis por **um único
caractere** — "homem-" onde as seis têm "homem -". É cópia, não redação
independente.

E as seis, que citam a mesma coisa, gravam `data_direito_ate: 31/12/2099`. Duas
regras com a mesma fundamentação e prazos diferentes: ou a fundamentação das
duas está errada, ou o prazo. O catálogo não pode estar certo nas oito.

## O art. 4º não pode encurtar o art. 7º

Não se trata de o art. 4º impor 31/12/2024 a toda aposentadoria da Emenda. O
art. 4º ressalva "os requisitos e os critérios exigidos pela **legislação
vigente até a data de entrada em vigor desta Emenda**" — isto é, o direito
*anterior* a ela. O art. 7º é direito **criado por ela**. Um prazo que
resguarda o passado não tem como limitar a regra nova; e o próprio catálogo lê
assim, ao gravar sentinela nas seis regras do art. 7º.

Daí que o desencontro não seja de datas apenas: as duas regras invocam a via
que exige **idade mínima e pedágio** e delimitam a janela da via que **não
exige idade nenhuma**. Nenhum dos requisitos de nenhuma das duas vias tem
coluna no cadastro, então nada no frontmatter desmente o texto.

## Fonte oficial

O art. 4º e o art. 7º (caput, §§ 1º, 2º e 3º) foram conferidos **na publicação
oficial** da Emenda arquivada em
`fontes-oficiais/arquivos/sapl-emenda_146.pdf` — páginas 4 e 8 —, lidas
visualmente porque o PDF é digitalizado e não tem camada de texto (o
`manifesto.yaml` registra exatamente isso). A leitura confirma, além do texto,
dois fatos negativos que a transcrição sozinha não sustentaria: o art. 4º tem
**apenas** caput e parágrafo único, e o art. 7º tem **apenas** os §§ 1º, 2º e
3º — o art. 8º começa na mesma página. Não há no art. 7º parágrafo que fixe
prazo, nem no art. 4º dispositivo que o estenda ao art. 7º.

O que a fonte **não** responde: a data de publicação da Emenda. O PDF traz
"Art. 13. Esta Emenda à Constituição entra em vigor na data de sua publicação"
e a data da Assembleia, **9 de setembro de 2021** — não 14/09/2021, que é o
`vigencia_inicio` declarado em `okf/dispositivos/ece-146-2021/norma.md` e o
valor de `data_direito_apos` das seis regras do art. 7º. A publicação em Diário
Oficial não está arquivada, então a coincidência entre os dois números fica
conferida contra o corpus e **não** contra a fonte.

# Relação com o que já está registrado

O `achado-0047` cita `regra-0109`–`regra-0112` como **grupo de contraste** — as
que gravam 31/12/2024 *e* citam a ECE 146/2021 na fundamentação, restando-lhes
"só o vínculo `dispositivos:` a `ece-146-2021/art-4`". Para `0111`/`0112` isso
precisa de um ajuste, e é o ponto deste achado: a fundamentação delas cita a
Emenda, mas cita o **art. 7º**, não o art. 4º. Citar outro artigo da mesma norma
não é citar o artigo que institui o prazo — e, pela própria regra que o
`achado-0047` aplica às oito que citam só no `nome`, o vínculo a
`ece-146-2021/art-4` **não pode** ser declarado: a fundamentação não o cita, e
vincular seria falsificar o vínculo para consertar o dado. As duas caem, nesse
aspecto, no grupo das oito, não no de contraste.

O `achado-0022` é a face oposta: sete regras invocam o art. 4º e gravam a
sentinela no lugar do prazo. Aqui o prazo está gravado e o artigo não é
invocado em campo de fundamentação.

O [`achado-0037`](achado-0037.md) e o [`achado-0038`](achado-0038.md) tratam de
outros dois defeitos das mesmas duas regras — o empacotamento das duas alíneas
na célula e a alínea masculina no `nome` da regra feminina. São independentes
deste: corrigir a via de transição não conserta nenhum dos dois, e vice-versa.

# Consequência prática

A regra existe para dizer **quem tem direito e com que fundamento**, e aqui as
duas metades apontam para regimes distintos.

Se a janela estiver certa e a fundamentação errada, o documento entregue
justifica com idade mínima e pedágio uma aposentadoria que foi concedida sem
exigir idade — e um requerente que reunia 30/20 antes de 31/12/2024 sem ter 53
anos recebe um ato cuja fundamentação lhe nega o direito que o ato concede.

Se a fundamentação estiver certa e a janela errada, o efeito é o oposto e mais
grave: quem ingressou entre 01/01/2004 e 13/11/2019 é **excluído** por
`data_adm_ate: 31/12/2003`, e todo mundo é excluído a partir de 01/01/2025 por
um prazo que a via do art. 7º não tem. Aí o defeito nega direito, não apenas
motivação.

O `data_adm_ate: 31/12/2003` merece nota própria: ele não é o corte de nenhuma
das duas vias. `paridade: S` e `tipo_calculo: Remuneração de Contribuição`
sugerem que ele venha do regime de integralidade e paridade da legislação
anterior — preservado justamente pelo parágrafo único do art. 4º —, mas nenhum
campo destas regras cita norma que fixe esse corte, e o único dispositivo
vinculado que trata de integralidade e paridade é o art. 7º, § 3º, cujo corte é
13/11/2019. É hipótese, não conclusão.

# Questão a investigar

1. **Qual das duas metades é a regra.** As janelas e o `nome` dizem art. 4º; a
   `fundamentacao_integral` diz art. 7º. Os dois lados são campo **deployável**,
   e a escolha é de quem responde pelo produto. Vale notar que, se a resposta
   for "art. 4º", as duas regras passam a ser a via do art. 4º **e o catálogo
   não tem outra** — nenhuma outra regra de policial grava 31/12/2024.

2. **De onde vem o `data_adm_ate: 31/12/2003`.** Se vier do regime de
   integralidade e paridade preservado pelo art. 4º, parágrafo único, a
   fundamentação precisa dizê-lo (e aí o vínculo vem depois, como consequência).
   Se não vier de norma nenhuma, o corte exclui quem ingressou de 2004 a 2019
   sem fundamento declarado.

3. **A leitura de `DATA_DIREITO_APOS`/`ATE` continua pendente** (issue #39,
   [`semantica-das-janelas-temporais.md`](../../../docs/analysis/semantica-das-janelas-temporais.md)
   §1.2). Este achado não depende dela: a incompatibilidade aqui é entre a
   *norma citada* e o *marco gravado*, e não muda com a inclusividade de um dia.
   O `01/01/1910` é o piso do catálogo, tratado como tal e não interpretado.
