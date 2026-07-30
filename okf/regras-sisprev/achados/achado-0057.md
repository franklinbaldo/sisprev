---
type: Achado
id: achado-0057
nome: regra-0065 e regra-0066 gravam Valor Médio citando o art. 25 da LCE 1.100/2021, que manda calcular pela totalidade da remuneração
situacao: aberto
severidade: bloqueante
verificacao: manual
natureza: juridica
regras_afetadas:
  - /regras/regra-0065.md
  - /regras/regra-0066.md
detectado_em: 2026-07-30
detectado_por: franklinbaldo
---

# Descrição

A LCE 1.100/2021 põe base de cálculo e reajuste em **dois trilhos excludentes**,
separados pelo ingresso até ou após 31/12/2003:

> **Art. 24.** No cálculo dos proventos de aposentadoria dos servidores titulares
> de cargo efetivo que tenham ingressado no serviço público em cargo efetivo
> **após 31 de dezembro de 2003** [...] será considerada a **média aritmética
> simples** das maiores remunerações [...] correspondentes a 80% (oitenta por
> cento) de todo o período contributivo [...]

> **Art. 25.** Os proventos de aposentadoria do servidor público que tenha
> ingressado no serviço público em cargo efetivo **até 31 de dezembro de 2003**
> [...] corresponderá à **totalidade da remuneração no cargo efetivo** em que se
> der a aposentadoria.

O art. 27 espelha a mesma partição no reajuste: o **inciso I** assegura o
tratamento do art. 7º da EC 41/2003 — paridade — a quem ingressou até
31/12/2003; o **inciso II** manda reajustar nos termos do RGPS quem ingressou
depois.

Base e reajuste andam juntos **por construção da lei estadual**: art. 25 com art.
27, I é totalidade da remuneração com paridade; art. 24 com art. 27, II é média
sem paridade.

`regra-0065` e `regra-0066` citam **arts. 25 e 27, I** e gravam
`tipo_calculo: Valor Médio`, que é o regime do art. 24 — o artigo que elas não
citam.

# Evidências

**A contradição é tripla dentro de cada regra.** Os `dispositivos:` vinculam
`lce-1100-2021/art-25` e `lce-1100-2021/art-27-inc-i`; a
`fundamentacao_integral` escreve por extenso o que eles determinam —

> Aposentadoria voluntária de servidor exposto a agentes nocivos à saúde, com
> proventos integrais (**cálculo por integralidade**) e **com paridade**, com
> base nos artigos **25, 27, inciso I**, e 41, inciso III, da Lei Complementar
> Estadual 1.100/2021 [...]

— e os campos `integral: S` e `paridade: S` confirmam. Só o `tipo_calculo`
destoa.

**A irmã idêntica é o controle, e é o que fecha o argumento.** A `regra-0067` tem
`fundamentacao_integral` **idêntica caractere a caractere** e `dispositivos:`
**idênticos item a item**:

| campo                   | `regra-0065` / `regra-0066` | `regra-0067`                | `regra-0071`              |
| ----------------------- | --------------------------- | --------------------------- | ------------------------- |
| dispositivos de cálculo | arts. **25** e **27, I**    | arts. **25** e **27, I**    | arts. **24** e **27, II** |
| texto da fundamentação  | integralidade, com paridade | integralidade, com paridade | média, sem paridade       |
| `integral`              | `S`                         | `S`                         | `S`                       |
| `paridade`              | `S`                         | `S`                         | `N`                       |
| `tipo_calculo`          | **`Valor Médio`**           | `Valor Efetivo`             | `Valor Médio`             |

`regra-0071` é a versão do outro trilho e é **inteiramente coerente**: cita o
artigo da média, diz média no texto, grava `paridade: N` e `Valor Médio`.
`regra-0067` é a versão deste trilho e também é coerente. `regra-0065` e
`regra-0066` têm o cabeçalho de `0067` e o `tipo_calculo` de `0071`.

**A divergência não decorre de as regras alcançarem populações diferentes.** As
três — `0065`, `0066`, `0067` — gravam exatamente a mesma janela
(`data_adm_apos`, `data_adm_ate`, `data_direito_apos`, `data_direito_ate`
iguais), o mesmo `sexo: AMBOS`, o mesmo `apos_especial: S` e o mesmo
`simulavel: S`. Não há critério aferido que as separe e explique cálculos
diferentes.

# Consequência prática

**A divergência é de valor concedido, não de documento.** Estas regras são
`simulavel: S`, e `tipo_calculo` é o campo que orienta o cálculo — ao contrário
da fundamentação, que o motor não lê. Média das maiores remunerações
correspondentes a 80% do período contributivo e totalidade da remuneração no
cargo efetivo produzem valores diferentes, e a diferença é permanente, porque se
projeta em todo o benefício.

A direção do desvio: `Valor Médio` sob o trilho do art. 25 tende a conceder
**menos** do que o dispositivo citado determina.

**Severidade `bloqueante`**, pelo critério de
[`docs/spec/regra.md`](../../../docs/spec/regra.md): campo deployável que
contradiz o dispositivo que a própria regra vincula, alcançando o valor do
benefício.

# O que este achado não afirma

**Não afirma que `Valor Efetivo` seja o rótulo juridicamente exato** da
totalidade da remuneração do art. 25. O `CLAUDE.md` e
`tests/test_forma_calculo_schema.py` registram que o enum legado não identifica
fórmulas — seus valores misturam base, ajuste e limitador. O que se afirma é que
`Valor Efetivo` é o rótulo que a **irmã idêntica** usa para o mesmo trilho, e que
`Valor Médio` é o que a regra do **outro** trilho usa. Isso basta para acusar a
divergência sem canonizar o enum.

**Não afirma que alguma concessão tenha saído a menor.** Depende de caso
concreto, e o catálogo não registra caso concreto.

**Não resolve por que existem três regras para um trilho só.** Corrigir o
`tipo_calculo` aproxima `0065` e `0066` da `0067` sem dissolver o grupo P2 entre
`0065` e `0066`, que o [`achado-0005`](achado-0005.md) já registra.

# Por que não é duplicata de achado existente

O [`achado-0042`](achado-0042.md) adverte que um segundo achado sobre estas
regras "não deve nascer duplicado" dele e que "quem estender a população estende
esta lista, não o raciocínio". A advertência é sobre o **defeito de janela** —
`data_adm_ate` sentinela sob os arts. 25 e 27, I —, que estas regras de fato
partilham com a `regra-0067` e que **continua sendo daquele achado**. Este aqui
não o toca.

O [`achado-0016`](achado-0016.md) registra a forma "fundamentação afirma
integralidade e paridade e os campos dizem o contrário", em `regra-0107` e
`regra-0108`. **A forma é parecida e a estrutura probatória não é**, e a
diferença decide o que se pode concluir:

- em `0107`/`0108` os **três** campos (`integral`, `paridade`, `tipo_calculo`)
  contradizem o texto **de forma coerente entre si** — descrevem o regime novo
  inteiro. Não se sabe qual lado corrigir, e o `achado-0016` deixa isso como
  questão aberta;
- aqui `integral` e `paridade` **concordam** com o texto e com os dispositivos
  citados, e só o `tipo_calculo` destoa. O defeito **isola num campo**, e a
  `regra-0067` fornece o valor que o trilho usa.

Um achado que juntasse os dois casos teria de abandonar a conclusão mais forte
deste — qual campo está errado — para caber na indeterminação daquele.

# Questão a investigar

1. **A janela de admissão é anterior a esta correção.** `0065`, `0066` e `0067`
   gravam `data_adm_ate` sentinela, sem recorte, enquanto o art. 25 que citam
   alcança só quem ingressou até 31/12/2003 — é o defeito do
   [`achado-0042`](achado-0042.md). Se o recorte estiver errado, pode ser que a
   regra devesse mesmo estar no trilho do art. 24, e aí o campo a corrigir é
   outro. Responder aquele achado é anterior a mexer aqui.

2. **Por que três regras para o mesmo trilho.** `0065`, `0066` e `0067`
   partilham janela, sexo e fundamentação. Corrigido o `tipo_calculo`, restam
   três regras materialmente próximas sem critério que as separe — pergunta que
   o [`achado-0005`](achado-0005.md) já levanta para o par e que a `0067`
   estende para o trio.

3. **Se a mesma incompatibilidade alcança as regras de pensão.** `regra-0016`,
   `regra-0017` e `regra-0018` gravam `paridade: S` com
   `tipo_calculo: Tipo Cálculo Nova Previdência Pensão por morte`. Se "Nova
   Previdência" designar base por média, é a mesma contradição noutra família —
   mas é leitura de rótulo, que este achado deliberadamente não faz, e exige
   conferência própria contra os dispositivos daquelas regras.
