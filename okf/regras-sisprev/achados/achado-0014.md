---
type: Achado
id: achado-0014
nome: Três regras da compulsória citam uma redação da EC 41/2003 para o art. 40, § 1º, II que nunca existiu
situacao: aberto
severidade: informativo
verificacao: manual
natureza: juridica
regras_afetadas:
  - /regras/regra-0027.md
  - /regras/regra-0028.md
  - /regras/regra-0029.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

`regra-0027`, `regra-0028` e `regra-0029` atribuem à **EC 41/2003** uma
redação do art. 40, § 1º, inciso II da Constituição Federal. Essa redação
não existe: a EC 41/2003 não alterou aquele inciso.

O campo em que a citação aparece difere entre as três, e a diferença importa:

| regra        | campo                        | trecho                                                                                                           |
| ------------ | ---------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `regra-0027` | `nome`                       | "Compulsória - Art. 40, §1º, II da CF, **com redação dada pela EC nº 41/2003**"                                  |
| `regra-0028` | `fundamentacao_proporcional` | "Artigo 40, § 1º, inciso II da Constituição Federal, **com redação dada pela Emenda Constitucional nº 41/2003**" |
| `regra-0029` | `fundamentacao_proporcional` | idem                                                                                                             |

Nas três é campo **deployável** — o que o Sisprev entrega no documento do
servidor. Em `0028`/`0029` é a fundamentação jurídica do ato; em `0027` é o
rótulo, que erra o mesmo fato com menor consequência.

# Evidências

Conferido contra a publicação original da EC 41/2003, arquivada localmente
(ver `fontes/manifesto.yaml`). O art. 1º da emenda reproduz o bloco do art.
40 assim:

> Art. 40. [...] observados critérios que preservem o equilíbrio financeiro e
> atuarial e o disposto neste artigo.
>
> § 1º Os servidores abrangidos pelo regime de previdência de que trata este
> artigo serão aposentados, calculados os seus proventos a partir dos valores
> fixados na forma dos §§ 3º e 17:
>
> I - por invalidez permanente, sendo os proventos proporcionais ao tempo de
> contribuição, exceto se decorrente de acidente em serviço, moléstia
> profissional ou doença grave, contagiosa ou incurável, na forma da lei;
>
> ................................................................

Depois do inciso I vem a **linha de reticências**, a convenção de técnica
legislativa que marca o texto não alterado. Os incisos II e III estão sob
ela: a EC 41/2003 reescreveu o *caput* do artigo, o *caput* do § 1º e o
inciso I, e mais nada daquele parágrafo.

Três conferências independentes fecham o histórico do inciso:

1. **O § 1º original da CF/88 não tinha incisos** — era a regra sobre lei
   complementar e atividades penosas, insalubres ou perigosas (conferido na
   publicação original de 05/10/1988, também arquivada). Logo o inciso II
   não vem do texto promulgado.
2. **A EC 20/1998 criou o inciso II** ("compulsoriamente, aos setenta anos de
   idade, com proventos proporcionais ao tempo de contribuição"), hoje
   transcrito em `cf88/art-40-par-1-inc-ii/ec-20-1998`.
3. **A EC 88/2015 lhe deu a segunda e última redação**, transcrita em
   `cf88/art-40-par-1-inc-ii/ec-88-2015`. A EC 103/2019 alterou o *caput* do
   artigo, o *caput* do § 1º e os incisos I e III — não o II.

O inciso II teve, portanto, **exatamente duas redações em toda a sua
existência**, e nenhuma delas é da EC 41/2003. O intervalo entre elas está
integralmente coberto pelos dois documentos autorados, sem lacuna — é o
mesmo raciocínio de "redação inexistente" registrado em `achado-0012`: quando
as redações autoradas ladrilham toda a vida do dispositivo, nenhuma outra
pode existir, e a citação divergente é falsa, não pendente de transcrição.

# Consequência prática

As três regras são de aposentadoria compulsória e têm `data_direito_apos: 31/12/2003`. Na abertura da janela vigia a redação da **EC 20/1998** (setenta
anos); a partir de 08/05/2015 passa a vigorar a da **EC 88/2015** (setenta
anos, ou setenta e cinco na forma de lei complementar). A janela de `0028` e
`0029` vai até 31/12/2024 e a de `0027` até 03/12/2015 — as três, portanto,
**atravessam a mudança de redação**, e nenhuma delas é regida por uma única.

Isso quer dizer que a correção não é trocar "EC 41/2003" por uma outra sigla:
a citação, como está redigida, não comporta a janela que a própria regra
declara. Qual é a redação correta em cada ponto da janela é questão de mérito
que este achado não decide.

Nenhum vínculo é proposto e nenhum é removido. `regra-0028` e `regra-0029`
declaram quatro dispositivos cada e `regra-0027` seis; **nenhum deles é o
art. 40, § 1º, II** em redação alguma — a citação errada nunca chegou a virar
vínculo, e é o comportamento correto: vincular exigiria escolher pela regra
uma redação que ela não nomeia.

A linha dessas regras em
[`docs/analysis/pendencias-de-citacao-congeladas.md`](../../../docs/analysis/pendencias-de-citacao-congeladas.md)
está classificada como `REDACAO` — como se faltasse transcrever. **Está mal
classificada**: não há o que transcrever, porque a redação não existe. A
correção do rótulo é consequência deste achado.

# Questão a investigar

1. **Como corrigir na origem.** `nome` e `FUNDAMENTACAO*` são campos
   deployáveis: alterá-los é mudar o produto, não auditar o catálogo, e
   depende de quem responde por ele. E, pelo exposto acima, não há uma
   redação única que sirva para toda a janela declarada — de modo que a
   correção pode implicar decompor a regra por período, e não apenas
   reescrever a citação.

2. **Se a origem do erro é a proximidade de datas.** A EC 41/2003 é de
   dezembro de 2003 e a janela destas regras abre em 31/12/2003; a emenda é
   *a* reforma previdenciária daquele momento e de fato reescreveu o § 1º —
   só que o *caput* e o inciso I. A hipótese de que o autor atribuiu ao
   inciso II a emenda certa do ano errado é plausível e não está verificada.
   Registrada como hipótese, não como causa.

3. **Se `informativo` é a severidade adequada.** Adotada aqui por consistência
   com `achado-0011`/`0012`/`0013`, que registram o mesmo modo de falha —
   citação legal falsa em campo deployável — com essa severidade. Nenhum
   achado do catálogo é hoje `bloqueante`, e a pergunta de se essa é a
   classificação certa para citação falsa é geral, não deste achado: mudá-la
   aqui sozinho tornaria a série incoerente. A decisão cabe à coordenação da
   auditoria.
