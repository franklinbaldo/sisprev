---
type: Achado
id: achado-0014
nome: Três regras da compulsória citam a redação EC 41/2003 do art. 40, § 1º, II, mas a janela declarada extrapola a vida dessa redação
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

`regra-0027`, `regra-0028` e `regra-0029` citam o art. 40, § 1º, inciso II da
Constituição Federal "com redação dada pela Emenda Constitucional nº
41/2003" — em `nome` na primeira, em `fundamentacao_proporcional` nas outras
duas.

**A citação está correta.** A redação existe, começa exatamente onde a janela
das três abre, e agora está transcrita
(`cf88/art-40-par-1-inc-ii/ec-41-2003`). O que este achado registra é outra
coisa: **a janela que as três declaram se estende muito além da vida dessa
redação**.

# Evidências

O inciso II é oração subordinada ao *caput* do § 1º, e um dispositivo é a
unidade endereçada com toda a cadeia que a contém (ver
[`okf/spec/dispositivo.md`](../../../okf/spec/dispositivo.md)). A EC
41/2003 alterou esse *caput* — de "calculados os seus proventos a partir dos
valores fixados na forma **do § 3º**" para "na forma **dos §§ 3º e 17**",
isto é, mudou a base de cálculo dos proventos que o inciso determina serem
proporcionais. O texto do inciso não mudou; o dispositivo, sim.

A cadeia completa do dispositivo, conferida nas publicações originais
arquivadas localmente (ver `fontes-oficiais/manifesto.yaml`):

| redação    | vigência                | o que a distingue                                                         |
| ---------- | ----------------------- | ------------------------------------------------------------------------- |
| EC 20/1998 | 1998-12-16 → 2003-12-30 | criou o inciso; *caput* remete só ao § 3º                                 |
| EC 41/2003 | 2003-12-31 → 2015-05-07 | *caput* passa a remeter aos §§ 3º e 17                                    |
| EC 88/2015 | 2015-05-08 → em vigor   | o próprio inciso muda: acrescenta os 75 anos na forma de lei complementar |

Contra isso, as janelas declaradas:

| regra        | `data_direito_apos` | `data_direito_ate` |
| ------------ | ------------------- | ------------------ |
| `regra-0027` | 31/12/2003          | 03/12/2015         |
| `regra-0028` | 31/12/2003          | 31/12/2024         |
| `regra-0029` | 31/12/2003          | 31/12/2024         |

A abertura casa **exatamente** com o início da redação citada — 31/12/2003 é
o primeiro dia de vigência da EC 41/2003. Isso é forte indício de que o marco
foi escolhido com a redação em vista, e não por acaso.

Mas o fim não casa com nada. A redação citada morre em 07/05/2015, quando a
EC 88/2015 altera o próprio inciso II — e as três janelas continuam depois
disso: `0027` por quase sete meses, `0028` e `0029` por mais de nove anos.
Nesse trecho as regras invocam uma redação que já não vigia, e a que vigia —
que acrescenta a idade de setenta e cinco anos — não é citada por nenhuma
delas.

# Consequência prática

A aposentadoria compulsória é justamente onde a EC 88/2015 mexeu, e mexeu no
número que decide o caso: setenta anos, ou setenta e cinco na forma de lei
complementar. Uma regra de compulsória cuja janela alcança 2024 citando só a
redação anterior a 2015 é candidata a aplicar a idade errada — e a idade-
limite **não é campo de regra nenhuma** no catálogo (§4.1 de
[`achados-candidatos-da-conferencia.md`](../../../docs/analysis/achados-candidatos-da-conferencia.md)),
de modo que nada no cadastro contradiz ou confirma a fundamentação.

Nenhum vínculo é proposto. `regra-0028` e `regra-0029` declaram quatro
dispositivos cada e `regra-0027` seis; **nenhum é o art. 40, § 1º, II** em
redação alguma. Declarar o vínculo agora é possível — o documento passou a
existir — mas exigiria decidir *qual* das redações a regra invoca em cada
trecho da janela, que é precisamente a questão aberta.

# Questão a investigar

1. **Se a janela deveria terminar em 07/05/2015.** É a leitura mais simples:
   cada regra vale enquanto vale a redação que cita, e o período seguinte
   pertenceria a outra regra, que citaria a EC 88/2015. Nesse caso `0028` e
   `0029` têm `data_direito_ate` errado, e o valor 31/12/2024 pede explicação
   própria — ele é o mesmo prazo do art. 4º da ECE 146/2021 que aparece em
   cinco dos seis grupos da conferência, registrado ali como padrão sugestivo
   e não como conclusão (§5.1).

2. **Ou se a regra agrega períodos normativos sucessivos** e a fundamentação
   é que está incompleta, por nomear só a primeira redação. É o mesmo formato
   já reconhecido em `regra-0030`/`0031` (§2.2), onde duas normas sucessivas
   produzem o mesmo resultado e o catálogo perde a resolução temporal. Aqui,
   porém, as duas redações **não** produzem o mesmo resultado: uma admite
   setenta e cinco anos e a outra não.

3. **A leitura de `DATA_DIREITO_APOS`/`DATA_DIREITO_ATE` continua pendente**
   (issue #39). A coincidência entre `data_direito_apos: 31/12/2003` e o
   primeiro dia da EC 41/2003 é indício forte de que os campos delimitam o
   período de vigência da fundamentação — mas
   [`semantica-das-janelas-temporais.md`](../../../docs/analysis/semantica-das-janelas-temporais.md)
   §1.2 registra que isso não está confirmado, e este achado não o presume.
   Vale notar que a coincidência observada aqui é **evidência nova** para
   aquela questão, e das mais limpas do catálogo: três regras independentes
   abrindo no primeiro dia de uma redação que elas nomeiam.
