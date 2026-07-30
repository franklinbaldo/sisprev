# Leituras prováveis das questões abertas — o que o próprio catálogo responde

> **Nota:** Relatório gerado por IA como apoio à decisão, com as leituras
> ratificadas pela coordenação da auditoria em 2026-07-30. **Não é artefato
> oficial**: não edita nenhuma `regra-*.md`, não altera schema nem dados
> derivados, e não responde nenhuma das questões — as respostas são fatos sobre o
> Sisprev, e continuam pertencendo ao IPERON. O que este documento registra é a
> **leitura mais provável de cada questão dado o que o catálogo permite medir**,
> separando explicitamente o que foi medido do que foi inferido.

## 1. Por que medir antes de perguntar

Várias das questões abertas foram tratadas como se só pudessem ser respondidas
por informação externa. Boa parte delas é atacável com o próprio catálogo: a
importação congelada é um corpo de dados sobre como o cadastro foi de fato
preenchido, e certas hipóteses sobre o significado de uma coluna fazem predições
verificáveis sobre a distribuição dela.

Isto tem duas consequências práticas. A primeira é que **algumas perguntas ao
IPERON ficam melhores** — em vez de "o que significa esta coluna", "esta coluna
marca exatamente as regras dos arts. 5º e 8º, é a tabela de pontuação?". A
segunda, que apareceu na prática, é que **uma premissa pode cair na medição**:
foi o que ocorreu com a leitura simétrica de `DATA_DIREITO_APOS`, ratificada como
premissa e retirada no mesmo dia (§5).

Todas as medições são sobre `data/raw/regras-sisprev.csv` e sobre os dispositivos
autorados. A importação é imutável, então nenhuma medição aqui envelhece.

## 2. Q4 — o Sisprev devolve uma regra ou várias candidatas?

**Leitura: várias candidatas. Medido, confiança alta.**

Agrupando as regras pelos critérios que plausivelmente são parametrizados —
benefício, `sexo`, `tipo`, `apos_especial` e as quatro datas —, há grupos que
contêm mais de uma regra, e eles reúnem quase metade do catálogo; o maior tem
seis. Para essas regras os campos estruturados **não determinam uma regra
única**.

Duas conclusões decorrem, e a segunda é a que importa:

1. O Sisprev não pode devolver exatamente uma regra a partir dos campos
   estruturados sem escolher arbitrariamente. Logo devolve candidatas, ou usa
   critério que não está no CSV — as duas leituras exigem a Q5.
2. **O desenho do simulador está certo por razão medida, não por prudência.** A
   RFC 0002 decidiu que só existem `excluida` e `nao_excluida`, nunca
   "compatível", porque afirmar compatibilidade seria alegação de completude que
   o motor não sustenta. A medição mostra que a alegação seria falsa e não apenas
   arriscada.

## 3. Q5 — onde vivem os requisitos que não estão no CSV?

**Leitura: em tabela externa, ao menos para pontuação; em análise manual para o
resto. Parcialmente medido, confiança média-alta para pontuação.**

`TabelaPontuacao` tem valor `S` num conjunto pequeno de regras, e são exatamente
as dos **arts. 5º e 8º da ECE 146/2021**. O art. 8º, § 1º está transcrito no
bundle e diz literalmente:

> A idade e o tempo de contribuição serão apurados em dias para o cálculo do
> **somatório de pontos** a que se refere o caput.

Nenhuma dessas regras menciona "pontos" no `nome` ou na fundamentação: a flag
corrobora a **norma**, não o texto. É a evidência mais direta de que existe ao
menos uma classe de requisito vivendo fora do CSV, com uma coluna do cadastro
funcionando como **ponteiro** para ela.

Para idade mínima, tempo de contribuição e tempo de exercício policial não há
coluna nem flag equivalente. A leitura provável para esses é análise manual sobre
documento, com confiança média — é inferência da ausência, e ausência de coluna
não prova ausência de automação.

## 4. Q6 — `integral`, `tipo_calculo` e `paridade` são independentes?

**Leitura: independentes como conceitos; contaminados como enum. Medido,
confiança alta.**

A tabela cruzada das três colunas mostra três coisas:

1. **`paridade` varia dentro de quase todo valor de `tipo_calculo`** — é dimensão
   independente, e isso é consistente com a decisão do P16 de deixar paridade
   **fora** da forma de cálculo: ela é regra de manutenção do benefício, não de
   apuração na concessão.
2. **`integral: S` ocorre com `Valor Médio`**, e em número expressivo. Logo
   `integral` **não** é sobre a base de cálculo: é sobre haver ou não redução
   proporcional ao tempo de contribuição. Quem lê `integral` como "cálculo pela
   remuneração integral" lê errado.
3. **O enum de `tipo_calculo` mistura os três níveis no mesmo rótulo.**
   `Valor Efetivo mais 70% do que exceder do Teto RGPS` é um **limitador**
   promovido a nome de fórmula; `Proporcionalidade Dias` é um **ajuste**. É
   exatamente a inversão que o P16 registrou — a fórmula é a ontologia e o
   `tipo_calculo` é projeção dela —, agora com a tabela cruzada por trás.

O que a medição **não** responde: a definição operacional exata de cada uma, que
é a segunda metade da Q6.

## 5. Q2 — `DATA_DIREITO_APOS` é inclusivo, e os dois eixos não são simétricos

**Leitura: inclusivo — o valor gravado é o primeiro dia coberto. Medido,
confiança alta; premissa firmada em 2026-07-30 e não confirmada no Sisprev.**

Em toda regra cuja `data_direito_apos` encosta na vigência de um dispositivo que
ela mesma vincula, o valor gravado é **o dia da entrada em vigor**, nunca o dia
anterior — sem exceção na importação. A leitura inclusiva é a única que faz esse
valor significar o que ele de fato é.

O contraste com o outro eixo é o achado conceitual: em `DATA_ADM_APOS`, confirmado
exclusivo, o valor é o **último dia do regime anterior** (`31/12/2003` significa
"admitido a partir de 01/01/2004"); em `DATA_DIREITO_APOS` o valor é o **primeiro
dia coberto**. Nas duas colunas o valor gravado é um marco legal real; o que
difere é a relação entre o marco e a cobertura. **Os dois eixos não compartilham
semântica**, e a Q1 continua respondida apenas para o de admissão.

Esta leitura substituiu a premissa **oposta** — simetria com `DATA_ADM_APOS` —,
que havia sido proposta e ratificada antes da medição. Sob ela, a cobertura
começaria um dia depois da vigência em toda a população, isto é, a maioria do
catálogo negaria o benefício no primeiro dia da norma que o funda. O registro da
população e da bifurcação é o
[`achado-0053`](../../okf/regras-sisprev/achados/achado-0053.md), que segue
**aberto** — premissa não é resposta, e o operador que o motor aplica não se
descobre no catálogo. Sob a premissa firmada, **nenhuma regra da população tem
defeito de data**.

A lição é sobre o método, e vale para as outras premissas: uma premissa que se
sustenta apenas na simetria do nome de uma coluna deve ser medida antes de ser
usada. O curinga `DATA_*` da formulação original da Q1 já pressupunha a resposta —
e a resposta que ele pressupunha era a errada.

## 6. Q7 — por que proporcional E integral na mesma linha?

**Leitura: são os dois ramos de resultado da mesma regra, e `integral` não os
seleciona. Medido em parte, confiança média.**

Três padrões de co-ocorrência aparecem: só integral (o dominante), só
proporcional, e as duas preenchidas. O achado que mata a leitura simples é outro:
**há regras com `integral: N` e `FUNDAMENTACAO_INTEGRAL` preenchida**, em número
que não é anedótico. Se `integral` decidisse qual texto sai, isso seria
impossível.

A hipótese que melhor explica os três padrões é que a regra pode conceder integral
ou proporcional conforme fato que o catálogo não registra, e cada coluna guarda o
texto do seu ramo. Confiança média, e não alta, porque explica os padrões sem ser
a única explicação possível — legado de planilha explicaria parte deles.

## 7. Q8 — pares que só diferem no resultado

**Leitura: decisão manual. Inferido de Q4 e Q7, confiança média.**

Se os critérios estruturados não determinam uma regra (§2) e o texto de
fundamentação tem dois ramos (§6), o desempate entre duas regras que diferem só
no resultado está na análise, não em parâmetro. É inferência composta de duas
outras leituras, e herda a incerteza das duas.

## 8. Q9 — os campos de comportamento, e as seis colunas sem variância

**Leitura: `TabelaPontuacao` é condição; `SIMULAVEL` é controle de interface;
seis colunas são flags dormentes. Medido, confiança alta para as dormentes.**

Seis das 27 colunas têm **um único valor em todo o catálogo**: `TIPO_REMUN`
(vazia), `Requisitos da IN Nº 5/2020`, `ADICIONAL_INATIVIDADE`,
`Relatório p/ Reserva Remunerada por Idade ex-officio`,
`VISIVEL DTC PROPORCIONAL` e `VISIVEL DTC INTEGRAL`.

Uma coluna sem variância **não pode ser critério de seleção** — não separa
nenhuma regra de nenhuma outra, e num filtro devolve tudo ou nada. Também não
pode ser efeito discriminante. A leitura provável é que sejam **flags de
capacidade do Sisprev que este catálogo não exercita**; a alternativa é que sejam
colunas mortas, e só o IPERON distingue as duas.

O contraste confirma que variância era esperada: `SIMULAVEL` divide o catálogo,
`APOS_ESPECIAL` divide quase ao meio, e `TabelaPontuacao` marca precisamente as
regras de pontuação (§3). Uma coluna que discrimina, discrimina de forma legível.

### `VISIVEL DTC INTEGRAL` merece parágrafo próprio

Ela é `N` em **todas** as regras, enquanto a esmagadora maioria delas tem
`FUNDAMENTACAO_INTEGRAL` preenchida. O catálogo inteiro preenche um texto de
fundamentação integral e, no mesmo registro, marca esse texto como não visível na
DTC.

Isso alcança a redação de outros achados. A justificativa recorrente para tratar
`FUNDAMENTACAO_INTEGRAL` como campo deployável crítico é que ele é "o texto
entregue ao servidor". Se a DTC está desligada em todo o catálogo, esse texto não
é lido **na DTC**, e a frase precisa de outro referente — o ato administrativo, o
processo, ou nenhum.

**Não derruba os achados de fundamentação.** O campo segue deployável, e
fundamento falso gravado num campo que o sistema carrega é defeito
independentemente da tela em que aparece. O que muda é a **precisão** da
afirmação sobre onde o defeito se materializa — afirmação que aparece em mais de
um achado e na disposição da `regra-0078`.

Isto **não** foi autorado como achado, e a razão é de forma: um achado precisa
nomear as regras que alcança, e este não acusa regra nenhuma. Nenhuma regra tem
valor errado nessas colunas; o objeto é o cadastro. Forçar uma população para
satisfazer o schema seria deformar o achado — o veículo certo é este relatório.

## 9. Q10 — `AMBOS`, vazio, desconhecido, não aplicável

**Leitura: vazio é "não gravado". Medido, confiança alta.**

`sexo` vazio co-ocorre exatamente com `integral` vazio e
`tipo_calculo: Não identificado`, no mesmo conjunto de regras. Três campos vazios
sempre juntos é assinatura de **linha não preenchida**, não de três decisões
semânticas independentes que por coincidência recaem sobre as mesmas regras.

Confirma a premissa ratificada em 2026-07-30 e registrada na spec: vazio é
pendência, nunca valor.

## 10. Q11 e Q12 — sem leitura

**Não há leitura provável, e afirmar uma seria chute.**

Nada no catálogo informa quais documentos são esperados para cada requisito
manual (Q11): nenhum campo registra evidência exigida, e a única coluna que
aponta para fora do CSV é a de pontuação, que é requisito e não prova. A fronteira
entre correspondência automática, verificação manual dos fatos e validação
jurídica da configuração (Q12) não deixa rastro no dado — é fluxo institucional,
e o dado é o produto dele.

Registrar "sem leitura" é o ponto: as duas ficam de fora da lista de premissas, e
nenhuma conclusão da auditoria deve depender delas.

## 11. O que fazer com isto

Três encaminhamentos, em ordem de retorno.

**Transcrever os incisos do art. 8º da ECE 146/2021 como dispositivos.** O caput
lista três somatórios de pontos "respectivamente", e as três regras do grupo
`regra-0068`/`0069`/`0070` são materialmente idênticas e todas marcadas na
pontuação. Os valores **já estão registrados na spec** (66 pontos com 15 anos de
exposição; 76 com 20; 86 com 25), de leitura anterior; o que não existe é o
**dispositivo** de cada inciso no bundle — há só o caput, o § 1º e o § 2º.
Transcrevê-los dá ao grupo o vínculo por inciso e converte a hipótese de
granularidade em lacuna de schema com endereço: o predicado que falta é a faixa de
pontos.

A transcrição depende de fonte legível, e a fonte declarada não serve: a
publicação no SAPL da Assembleia é um PDF **digitalizado como imagem**, e a
tentativa de leitura nesta sessão devolveu binário. O passo é localizar uma
publicação em texto — inventar o texto de um dispositivo, ainda que os números
estejam anotados na spec, é o modo de falha que a RFC 0008 documenta, e a
transcrição de dispositivo é verbatim por contrato.

**Levar ao IPERON três perguntas, não doze.** Se o motor trata
`DATA_DIREITO_APOS` como inclusivo — confirmação de premissa, não pergunta aberta
(§5); onde a `FUNDAMENTACAO_INTEGRAL` é lida, se a DTC está desligada em todo o
catálogo (§8); e o que o sistema faz quando várias regras passam pelos filtros
(§2). As três destravam Q2, Q4, Q5, Q9 e parte da Q11, e as três já vão com a
evidência pronta — o que é o ponto de medir antes de perguntar.

**Tratar as leituras medidas como premissas expressas**, cada uma citada pelas
conclusões que dela dependerem, na forma decidida em
[decisões transversais da auditoria](decisoes-de-auditoria-2026-07-30.md) §8. As
inferidas (§6, §7) ficam marcadas como tal, e Q11/Q12 ficam sem premissa alguma.
