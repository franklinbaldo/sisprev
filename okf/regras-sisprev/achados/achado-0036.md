---
type: Achado
id: achado-0036
nome: O art. 12, II da ECE 146/2021 referenda expressamente a revogação do art. 3º da EC 47/2005, que é o fundamento de regra-0085 e regra-0086
situacao: aberto
severidade: informativo
verificacao: manual
natureza: juridica
regras_afetadas:
  - /regras/regra-0085.md
  - /regras/regra-0086.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

`regra-0085` e `regra-0086` fundam-se no **art. 3º da EC 47/2005** (a "fórmula
85/95"), que citam e vinculam, e o mantêm em aplicação sem termo
(`data_direito_ate: 31/12/2099`).

Esse artigo foi **revogado** pelo art. 35, IV da EC 103/2019. Para os regimes
próprios estaduais a revogação não é imediata: o art. 36, II da EC 103/2019 a
condiciona à publicação de "lei de iniciativa privativa do respectivo Poder
Executivo **que as referende integralmente**". A
[varredura da cadeia de vigência](../../../docs/analysis/cadeia-de-vigencia-dos-dispositivos.md)
§5.2 registrou esse condicionamento e deixou a pendência explícita: "qual lei
estadual cumpre esse papel, e se a LCE 1.100/2021 o cumpre, é conclusão jurídica
que esta varredura não tem base para tomar".

**O que este achado acrescenta é texto, não conclusão:** a ECE 146/2021 — a
mesma Emenda cujo art. 4º as duas regras já citam e vinculam — tem um artigo
que faz exatamente esse referendo, nominalmente, invocando o art. 36, II.

# Evidências

Conferido na publicação oficial da Emenda arquivada localmente
(`fontes-oficiais/arquivos/sapl-emenda_146.pdf`, SAPL/ALE-RO, registrada no
`manifesto.yaml`). PDF digitalizado sem camada de texto — `pdftotext` devolve 10
bytes —, leitura **visual** das páginas 9 e 10. Verbatim:

> Art. 12. Ficam **integralmente referendadas**, nos termos do inciso II do art.
> 36 da Emenda à Constituição Federal nº 103, de 12 de novembro de 2019:
>
> I - a alteração do art. 149 da Constituição Federal promovida pelo art. 1º da
> Emenda Constitucional nº 103, de 12 de novembro de 2019;
>
> II - as revogações do § 21 do art. 40 da Constituição Federal, dos arts. 2º,
> 6º e 6º-A da Emenda Constitucional nº 41, de 19 de dezembro de 2003, e do
> **art. 3º da Emenda Constitucional nº 47, de 5 de julho de 2005**, promovidas
> pela alínea "a" do inciso I e pelos incisos III e IV do art. 35 da Emenda
> Constitucional nº 103, de 12 de novembro de 2019.
>
> Art. 13. Esta Emenda à Constituição entra em vigor na data de sua publicação.

O art. 12 nomeia o dispositivo condicionante (art. 36, II), usa o advérbio que
ele exige ("integralmente") e enumera os quatro dispositivos revogados um a um.
Não é referendo por implicação: é referendo por escrito.

Duas datas relevantes, conferidas: a Emenda é de **9 de setembro de 2021**
(título, p. 1) e entra em vigor na data da publicação (art. 13), que o corpus dá
como **14/09/2021** (`ece-146-2021/norma.md`). O parágrafo único do art. 36 da
EC 103/2019 acrescenta que a lei de referendo "não produzirá efeitos anteriores
à data de sua publicação" — logo, se o art. 12 servir, o efeito é
**prospectivo** a partir dessa data, nunca retroativo.

# A questão jurídica, e por que este achado não a resolve

O art. 36, II fala de "**lei** de iniciativa privativa do respectivo Poder
Executivo". A ECE 146/2021 não é lei: é **emenda à Constituição do Estado**,
promulgada pela Mesa Diretora da Assembleia Legislativa "nos termos do § 3º do
artigo 38 da Constituição Estadual" (p. 1 da publicação). Duas perguntas
decorrem, e nenhuma é decidível aqui:

1. **Emenda constitucional estadual satisfaz a exigência de "lei"?** Há leitura
   pela suficiência (a emenda é ato normativo de hierarquia superior à lei, e o
   art. 12 declara expressamente cumprir o art. 36, II) e leitura pela
   insuficiência (a norma federal escolheu a espécie e o regime de iniciativa,
   e a espécie escolhida não foi a emenda).
2. **A iniciativa foi privativa do Poder Executivo?** A publicação promulgada
   não registra a proposta que a originou. Sem isso, a segunda metade do
   requisito do art. 36, II não é conferível na fonte que tenho.

A [conferência das doze regras de transição](../../../docs/analysis/conferencia-criterio-dispositivo-transicao-ec41-ec47.md)
e a varredura da cadeia deixaram os quatro documentos
(`ec-41-2003/art-2`, `ec-41-2003/art-6`, `ec-41-2003/art-6a`,
`ec-47-2005/art-3`) **sem `vigencia_fim`** por essa exata razão, e a razão
continua valendo: escrever a data ali exige responder às duas perguntas. Este
achado **não** propõe escrevê-la, não altera nenhum dispositivo e não afirma que
o art. 3º da EC 47/2005 esteja revogado em Rondônia.

**Alcance maior que este achado, dito e não enumerado.** O mesmo art. 12, II
referenda também as revogações dos arts. 2º, 6º e 6º-A da EC 41/2003, que são o
fundamento de outras regras de transição do catálogo (`regra-0097`–`0104`, e o
art. 6º-A alcança regras de incapacidade). Elas **não** entram em
`regras_afetadas` porque não foram conferidas nesta rodada — `regras_afetadas` é
o alcance da investigação humana, não a projeção do que a norma alcança. Quem
conferir aquelas regras encontra aqui o texto que faltava.

# Consequência prática

Se o art. 12 da ECE 146/2021 satisfizer o art. 36, II da EC 103/2019, então
desde 14/09/2021 o art. 3º da EC 47/2005 já não é fundamento disponível em
Rondônia para aposentadoria a conceder — e o que resta dele é o que o **art. 4º
da mesma Emenda** preserva: os requisitos e critérios da legislação anterior,
"desde que sejam cumpridos **até 31 de dezembro de 2024**".

Nessa hipótese as duas coisas se encaixam com precisão desconfortável: o art. 4º
não é um artigo qualquer que as duas regras citam por conveniência — é a
**única** base pela qual elas continuam existindo depois de 2021, e o prazo dele
é o termo delas. E é justamente esse prazo que `regra-0085`/`0086` não gravam
(`achado-0035`): o `data_direito_ate: 31/12/2099` estende sem termo uma regra
cujo fundamento primário pode ter sido revogado e cuja sobrevida a norma
estadual limitou a 31/12/2024.

Na hipótese contrária — o referendo não serve —, o art. 3º segue vigente em
Rondônia, e aí é o `data_direito_ate` que precisa de outra justificativa, porque
o art. 4º continua sendo campo citado pelas duas.

Em nenhuma das duas hipóteses o valor gravado hoje se sustenta pelos
dispositivos que as regras declaram. As hipóteses divergem sobre **o que
corrigir**, não sobre **haver o que corrigir**.

# Questão a investigar

1. **Se a ECE 146/2021, art. 12, II satisfaz o art. 36, II da EC 103/2019.**
   Conclusão jurídica sobre norma estadual, de competência da PGE. É a pergunta
   que destrava o `vigencia_fim` dos quatro dispositivos de transição e o
   alcance de pelo menos doze regras do catálogo.

2. **Qual foi a iniciativa da PEC que originou a ECE 146/2021.** Metade do
   requisito do art. 36, II é de iniciativa, e a publicação promulgada não a
   registra. A ficha da norma no SAPL (`/norma/9906`) e a tramitação da proposta
   fecham isso documentalmente.

3. **Se a LCE 1.100/2021 também referenda.** A pendência original da varredura
   perguntava por ela, e a resposta encontrada foi outra norma. Se a LCE 1.100
   contiver cláusula equivalente, há **duas** candidatas com datas diferentes
   (18/10/2021 e 14/09/2021) e a data do fim de vigência depende de qual delas
   conta — o parágrafo único do art. 36 impede retroação, então a **primeira**
   publicação válida é a que fixa o marco.

4. **O que este achado deliberadamente não faz.** Não escreve `vigencia_fim` em
   `ec-47-2005/art-3/original`, não altera `dispositivos:` de nenhuma regra e não
   conclui pela revogação. Encerrar a vigência de uma regra de transição antes da
   hora tornaria "fora de vigência" exatamente a fundamentação de quem tem
   direito adquirido — o erro mais caro disponível aqui.
