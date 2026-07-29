# Análise jurídica do art. 4º da ECE 146/2021 e das sete regras do achado-0022

- **Status**: análise concluída em 2026-07-29. As conclusões interpretativas
  estão fechadas contra fonte oficial; as três decisões de campo deployável que
  elas apontam continuam pendentes de quem responde pelo catálogo.

Nota: este documento sustenta o [`achado-0022`](../../okf/regras-sisprev/achados/achado-0022.md),
corrige o alcance dele em um ponto e produz um achado novo. Não altera campo
nenhum.

## 1. A pergunta

O [`achado-0022`](../../okf/regras-sisprev/achados/achado-0022.md) afirma que
sete regras invocam o art. 4º da ECE 146/2021 e gravam
`data_direito_ate: 31/12/2099` onde o dispositivo fecha em 31/12/2024. Ele é o
**primeiro achado `bloqueante` do catálogo**, e por isso impede `revisada` nas
sete até que a decisão seja tomada.

A pergunta que ele deixa em aberto é se a correção é uniforme. A resposta é
**não**: as sete se separam em três grupos juridicamente distintos, com
consertos diferentes, e um deles tem defeito **anterior** à janela — que fechar
a janela não resolveria.

## 2. O art. 4º é cláusula de graça, não de direito adquirido — e o modelo federal prova

O texto, verbatim da transcrição oficial:

> Art. 4º A concessão de aposentadoria ao servidor público vinculado ao Regime
> Próprio de Previdência Social e de pensão por morte a seus dependentes
> observará os requisitos e os critérios exigidos pela legislação vigente até a
> data de entrada em vigor desta Emenda Constitucional, **desde que sejam
> cumpridos até 31 de dezembro de 2024**, sendo assegurada a qualquer tempo.

A objeção natural — a que o `achado-0022` já registra como armadilha — é que
"sendo assegurada a qualquer tempo" licenciaria a sentinela. O achado responde
que a oração fala do momento da **concessão**, não do **implemento** dos
requisitos. Essa leitura estava correta e agora está **provada**, não apenas
argumentada, porque o dispositivo é cópia estrutural do modelo federal:

> **EC 103/2019, art. 3º** — A concessão de aposentadoria ao servidor público
> federal (...) será assegurada, **a qualquer tempo**, desde que tenham sido
> cumpridos os requisitos para obtenção desses benefícios **até a data de
> entrada em vigor desta Emenda Constitucional**, observados os critérios da
> legislação vigente na data em que foram atendidos os requisitos (...)
>
> (`fontes-oficiais/arquivos/planalto-emc103.htm`, arquivo **cp1252**)

A comparação é direta. As duas cláusulas têm a mesma arquitetura — "assegurada a
qualquer tempo" + "desde que cumpridos até \<data>" —, e no texto federal não há
ambiguidade possível: "a qualquer tempo" convive com um prazo duro de implemento
que é a própria data da emenda. Se ali a oração não dispensa o prazo, aqui
também não.

O que Rondônia alterou foi **apenas a data**, e no sentido mais generoso: em vez
de exigir requisitos completos na entrada em vigor da emenda (o modelo federal,
que é pura proteção de direito adquirido), o Estado abriu **três anos e meio de
graça**, até 31/12/2024. Isso faz do art. 4º uma **regra de transição**, não uma
cláusula declaratória de direito adquirido.

A distinção importa por duas razões:

- **Quem já tinha completado os requisitos antes de 14/09/2021 não depende do
  art. 4º.** Está protegido pelo art. 5º, XXXVI da CF, e a Súmula 359 do STF
  fixa que os proventos se regem pela lei do tempo em que os requisitos foram
  reunidos. Para essa população o art. 4º é declaratório e o prazo é inócuo — é
  por isso que a exclusão de `regra-0027`, `0091` e `0092` do achado (janelas
  fechadas antes de 2021) está certa.
- **Quem não os tinha completado tem mera expectativa de direito**, e cortá-la é
  constitucionalmente válido: não há direito adquirido a regime jurídico, e toda
  a arquitetura das reformas previdenciárias se apoia nisso. O prazo de
  31/12/2024 é, portanto, eficaz.

**Conclusão 1.** A leitura do `achado-0022` está correta e agora tem
fundamento textual comparado, não só sistemático. Onde o art. 4º funda os
requisitos de uma regra, a janela dessa regra fecha em 31/12/2024.

## 3. Para `0008`/`0009` o prazo é duplamente determinado, e isso é novo

`regra-0008` e `regra-0009` fundam-se no **art. 6º-A da EC 41/2003**, na redação
da EC 70/2012. Elas não dependem do art. 4º apenas para o prazo — dependem dele
para **existir**.

O art. 35, IV da EC 103/2019 revogou o art. 6º-A. O art. 36, II da mesma emenda
condicionou essa revogação, nos RPPS estaduais, a lei estadual que a referendasse
integralmente. E o art. 12 da ECE 146/2021 faz exatamente isso:

> Art. 12. Ficam **integralmente referendadas**, nos termos do inciso II do art.
> 36 da Emenda à Constituição Federal nº 103 (...):
>
> II - as revogações do § 21 do art. 40 da Constituição Federal, dos arts. 2º,
> 6º e **6º-A** da Emenda Constitucional nº 41, de 19 de dezembro de 2003, e do
> art. 3º da Emenda Constitucional nº 47, de 5 de julho de 2005 (...)

Logo, **no RPPS de Rondônia o art. 6º-A está revogado desde a entrada em vigor
da ECE 146/2021**. O que o mantém aplicável é só o art. 4º, e só dentro do prazo
dele.

Para essas duas regras, portanto, o 31/12/2024 não é uma interpretação de uma
cláusula de graça: é o limite de sobrevida de uma norma revogada. Duas rotas
independentes — a graça do art. 4º e o referendo do art. 12 — chegam à mesma
data. É a corroboração mais forte do achado, e ela não está nele.

*(A questão que este documento **não** resolve: se emenda constitucional estadual
satisfaz a exigência do art. 36, II da EC 103/2019, que fala em "lei" de
iniciativa privativa do Executivo. É conclusão jurídica sobre norma estadual, e
está registrada como aberta no
[`achado-0036`](../../okf/regras-sisprev/achados/achado-0036.md). Se a resposta
for negativa, o art. 6º-A não foi revogado em Rondônia e esta seção cai — mas o
prazo do art. 4º permanece pela rota da seção 2.)*

## 4. Para `0006`/`0007` a conclusão de maior alcance é segura, e o catálogo prova

O `achado-0022` registra, com razão, que fechar `0006`/`0007` em 2024 é a
conclusão de maior alcance: são regras de **regime permanente**
(`data_adm_ate: 31/12/2099`, sem corte de ingresso), e fechá-las significa que a
incapacidade permanente sob a redação da EC 41/2003 deixa de ser concedível para
incapacidades constituídas depois.

Duas observações fecham essa preocupação.

**Primeira: o requisito de uma regra de incapacidade é um evento, não um
acúmulo.** Não se "progride" para a incapacidade permanente — ela sobrevém.
"Requisitos cumpridos até 31/12/2024" significa, aqui, incapacidade
**constituída** até 31/12/2024, e é uma data verificável no caso concreto, não
uma projeção.

**Segunda, e é a decisiva: existe família sucessora, e ela já está no
catálogo.** As regras `0019`–`0022` são exatamente incapacidade permanente pela
**redação da EC 103/2019** combinada com o art. 30 da LCE 1.100/2021, e cobrem
as duas coortes de ingresso:

| regras         | ingresso                      | direito abre |
| -------------- | ----------------------------- | ------------ |
| `0006`–`0009`  | (permanente / até 31/12/2003) | 31/12/2003   |
| `0019`, `0020` | até 31/12/2003                | 23/10/2021   |
| `0021`, `0022` | após 01/01/2004               | 23/10/2021   |

Fechar `0006`–`0009` em 31/12/2024 **não abre lacuna de cobertura**: a
incapacidade constituída em 2025 cai nas `0019`–`0022`. E a sobreposição entre
23/10/2021 e 31/12/2024, em que as duas famílias estão abertas, é precisamente o
desenho que uma regra de graça produz — nesse intervalo o servidor pode ter o
regime anterior se implementar os requisitos, e o novo se não.

**Conclusão 2.** A confirmação que o `achado-0022` pedia está dada: o alcance é
grande, mas o catálogo já tem para onde mandar os casos posteriores.

## 5. `0039`/`0040` têm defeito anterior à janela, e fechá-la não o resolve

Aqui a análise se separa do achado. As duas regras de magistério fundam os seus
**requisitos** no art. 40, § 1º, III, "a" e § 5º da CF **na redação da EC
20/1998** — a própria `fundamentacao_integral` separa os eixos, atribuindo a essa
redação "o preenchimento dos requisitos" e à EC 41/2003 "a fórmula de cálculo e
reajuste".

Três datas, todas conferidas:

| fato                                                                          | data           |
| ----------------------------------------------------------------------------- | -------------- |
| fim da vigência da redação da EC 20/1998 do art. 40, § 1º, III, "a" e do § 5º | **30/12/2003** |
| `data_adm_apos` das duas regras (ingresso **após**)                           | **31/12/2003** |
| `data_direito_apos` das duas regras                                           | 18/10/2021     |

O art. 4º preserva "os requisitos e os critérios exigidos pela **legislação
vigente até a data de entrada em vigor desta Emenda**" — isto é, a legislação em
vigor em 2021. Em 2021 a redação vigente do art. 40, § 1º, III era a da **EC
103/2019**; a da EC 20/1998 havia sido substituída dezoito anos antes. **O art.
4º não ressuscita redação já revogada quando a emenda entrou em vigor** — ele
congela o estado da legislação naquele momento, não um estado anterior a ele.

E não há como salvar as duas por direito adquirido, porque a própria janela de
admissão o exclui: elas se aplicam a quem ingressou **após 31/12/2003**, ou seja,
depois de a redação invocada ter deixado de existir. Ninguém dessa população
poderia ter adquirido direito sob ela.

Isso é defeito de **fundamento**, não de janela. Gravar `31/12/2024` em
`data_direito_ate` — a correção que o `achado-0022` propõe para as sete —
deixaria as duas regras aplicando, até 2024, requisitos que nunca lhes foram
aplicáveis. Autorado em achado próprio.

## 6. `0032` continua dependendo de decisão anterior

A `regra-0032` tem divergência interna registrada no
[`achado-0023`](../../okf/regras-sisprev/achados/achado-0023.md): o `nome` a funda
no regime novo (EC 103/2019 + art. 31 da LCE 1.100/2021), a
`fundamentacao_proporcional` no anterior (EC 88/2015 + LC 152/2015).

A análise da cadeia dobrada naquele achado pesa a favor do `nome`: o § 1º do art.
40 na redação da EC 88/2015 manda calcular os proventos "na forma dos §§ 3º e
17", e a regra grava `tipo_calculo: Tipo Cálculo Nova Previdência`. Se o `nome`
vale, a regra é de regime novo, a sentinela em `data_direito_ate` está **certa**,
e o defeito passa a ser a **citação do art. 4º** — que não deveria estar ali.

Ou seja: para esta regra, a correção que o `achado-0022` propõe pode ser
exatamente a inversa da correta. A ordem é decidir o `achado-0023` primeiro.

## 7. Uma lacuna de 34 dias, que a análise encontrou e não fecha

A ECE 146/2021 entra em vigor na publicação (art. 13). A LCE 1.100/2021, que a
implementa, vigora a partir de 18/10/2021. Entre uma e outra há um intervalo em
que o regime anterior já foi referendadamente revogado (art. 12) e o novo ainda
não vigia.

O art. 4º cobre esse intervalo — é para isso que ele serve. Mas vale registrar
que **nenhuma regra do regime novo abre antes de 18/10/2021** (e três abrem em
23/10/2021, valor que não corresponde a marco nenhum — ver
[`achado-0026`](../../okf/regras-sisprev/achados/achado-0026.md)). A cobertura do
intervalo depende inteiramente de as janelas do regime anterior estarem corretas,
que é a questão deste documento.

A data exata da publicação da emenda não está confirmada contra o Diário Oficial:
a peça oficial arquivada traz a lavratura em **09/09/2021** e o registro do SAPL
indica **14/09/2021**. Nenhuma conclusão deste documento depende de qual das duas
é, porque as duas são anteriores a 18/10/2021 e muito anteriores a 31/12/2024.

## 8. O que decorre

**Três grupos, três consertos:**

| regras                         | diagnóstico                                                                                               | conserto                                                                                         |
| ------------------------------ | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `0006`, `0007`, `0008`, `0009` | janela aberta onde o art. 4º fecha; nas duas últimas o fundamento está revogado e só sobrevive pela graça | `data_direito_ate: 31/12/2024`                                                                   |
| `0032`                         | divergência interna sobre qual regime funda a regra                                                       | decidir o `achado-0023`; se vale o `nome`, retirar o vínculo ao art. 4º e **manter** a sentinela |
| `0039`, `0040`                 | requisitos fundados em redação extinta antes de a população admitida existir                              | não é a janela; achado próprio                                                                   |

**Duas conclusões interpretativas fechadas**, e nenhuma delas altera campo:

1. "Sendo assegurada a qualquer tempo" é o momento da concessão, provado pela
   comparação com o art. 3º da EC 103/2019, de que o art. 4º é cópia estrutural.
2. Fechar `0006`–`0009` em 31/12/2024 não abre lacuna de cobertura, porque
   `0019`–`0022` são a família sucessora e já existem.

**Uma questão que segue aberta e não é da auditoria**: se o referendo por emenda
constitucional estadual satisfaz o art. 36, II da EC 103/2019, que fala em lei de
iniciativa privativa do Executivo. Dela depende a seção 3, não as demais.
