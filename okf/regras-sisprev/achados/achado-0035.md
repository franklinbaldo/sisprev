---
type: Achado
id: achado-0035
nome: regra-0085 e regra-0086 gravam sentinela nos dois limites da janela de direito, contra o prazo de 31/12/2024 do art. 4º da ECE 146/2021 e contra a retroatividade limitada do art. 6º da EC 47/2005
situacao: aberto
severidade: informativo
verificacao: manual
natureza: dados
regras_afetadas:
  - /regras/regra-0085.md
  - /regras/regra-0086.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

`regra-0085` e `regra-0086` são a "fórmula 85/95" — art. 3º da EC 47/2005,
preservado em Rondônia pelo art. 4º da ECE 146/2021 — e declaram **os dois
limites da janela de direito como sentinela**:

| campo               | valor gravado  | leitura        |
| ------------------- | -------------- | -------------- |
| `data_direito_apos` | **01/01/1950** | sentinela (P5) |
| `data_direito_ate`  | **31/12/2099** | sentinela (P5) |

Sob a P5 o catálogo não interpreta sentinela, então o efeito prático é que as
duas regras **não declaram fronteira temporal nenhuma** para a aquisição do
direito. Só que os três dispositivos que elas citam e vinculam declaram, cada
um, uma fronteira — e as três são muito mais estreitas.

# Evidências

## O teto: o art. 4º da ECE 146/2021 fixa 31/12/2024, e as duas o vinculam

`ece-146-2021/art-4/original` está em `dispositivos:` das duas, e a
`fundamentacao_integral` de ambas o cita nominalmente ("artigo 4º da Emenda à
Constituição Estadual nº 146/2021"). Seu texto, conferido na publicação oficial
arquivada (`fontes-oficiais/arquivos/sapl-emenda_146.pdf`, p. 4 — PDF
digitalizado sem camada de texto, lido visualmente):

> Art. 4º A concessão de aposentadoria ao servidor público vinculado ao Regime
> Próprio de Previdência Social e de pensão por morte a seus dependentes
> observará os requisitos e os critérios exigidos pela legislação vigente até a
> data de entrada em vigor desta Emenda Constitucional, **desde que sejam
> cumpridos até 31 de dezembro de 2024**, sendo assegurada a qualquer tempo.

E `DATA_DIREITO_ATE` é, pela definição confirmada pela coordenação da auditoria,
**prazo de implementação dos requisitos**: exatamente a função que a oração
"desde que sejam cumpridos até 31 de dezembro de 2024" exerce. Os dois campos
falam da mesma coisa e dizem coisas diferentes.

O contraste que fecha o argumento está dentro do catálogo: `regra-0105` e
`regra-0106` citam **as mesmas três provisões**, vinculam os **mesmos três
dispositivos**, têm o mesmo benefício, o mesmo `integral`, o mesmo
`tipo_calculo`, a mesma `paridade`, o mesmo `apos_especial` e o mesmo
`data_adm_ate` — e gravam `data_direito_ate: 31/12/2024`. Não é contraste com
outra família: é o mesmo par de regras noutro ciclo de validação.

## O piso: o art. 6º da EC 47/2005 diz até onde a retroatividade vai

Conferido na publicação oficial do Planalto arquivada localmente
(`fontes-oficiais/arquivos/planalto-emc47.htm`; o arquivo é **cp1252**, não
UTF-8 — decodificar como UTF-8 devolve zero resultados sem levantar erro):

> Art. 6º Esta Emenda Constitucional entra em vigor na data de sua publicação,
> **com efeitos retroativos à data de vigência da Emenda Constitucional nº 41,
> de 2003**.
>
> Este texto não substitui o publicado no DOU 6.7.2005

A EC 41/2003 tem `vigencia_inicio: 2003-12-31` autorada no corpus. Logo o art.
3º da EC 47/2005 **não produz efeito algum antes de 31/12/2003**, por
determinação expressa da própria Emenda. Um piso em `01/01/1950` afirma o
contrário: que o direito da fórmula 85/95 pode ter-se perfeito em qualquer data
desde 1950.

E isto **responde a uma pergunta que o repositório deixou explicitamente
aberta**. A [conferência das doze regras de transição](../../../docs/analysis/conferencia-criterio-dispositivo-transicao-ec41-ec47.md)
§8 registrou, sobre o `data_direito_apos: 31/12/2003` de `regra-0105`/`0106`:
"Há explicação possível numa disposição da própria EC 47 que não está
transcrita nem citada — **não a afirmo**". A disposição é o art. 6º, e ela
existe: `31/12/2003` é o marco correto, e é o que `0105`/`0106` gravam.

Nota lateral, conferível e útil a outros itens: o mesmo texto oficial dá a
publicação da EC 47/2005 no **DOU de 6.7.2005**, o que fecha o
`vigencia_inicio` que `ec-47-2005/norma.md` não tem hoje — item 5.1 da
[semântica das janelas](../../../docs/analysis/semantica-das-janelas-temporais.md).
Este achado não edita o documento da norma; registra a data conferida.

## Os requisitos do art. 3º, conferidos, e o que eles confirmam

O mesmo texto oficial traz os três incisos que o corpus não transcreve
(`ec-47-2005/art-3/original` para na abertura da enumeração):

> I - trinta e cinco anos de contribuição, se homem, e trinta anos de
> contribuição, se mulher;
> II - vinte e cinco anos de efetivo exercício no serviço público, quinze anos
> de carreira e cinco anos no cargo em que se der a aposentadoria;
> III - idade mínima resultante da redução, relativamente aos limites do art.
> 40, § 1º, inciso III, alínea "a", da Constituição Federal, de um ano de idade
> para cada ano de contribuição que exceder a condição prevista no inciso I do
> *caput* deste artigo.

Duas conferências fecham com isso, e vão para o corpo das duas regras em vez de
virarem achado, porque **não** revelam defeito:

- **A "FÓRMULA 85/95" do `nome` é exata.** Os limites da alínea "a" são 60 anos
  (homem) e 55 (mulher); com um ano de redução por ano de contribuição
  excedente, a soma idade + contribuição fica constante em **95 para o homem e
  85 para a mulher**. A conferência anterior registrou o `nome` como não
  sustentado por nada transcrito (§5); está sustentado pela fonte.
- **`sexo` é critério que o dispositivo funda.** Os incisos I e III
  parametrizam contribuição e idade por sexo. A conferência anterior registrou,
  para as doze regras de transição, que "`sexo` não é fundado por nenhuma
  provisão transcrita" (§3) — verdade sobre a transcrição, não sobre a norma.

# Consequência prática

`DATA_DIREITO_APOS` e `DATA_DIREITO_ATE` são campos **deployáveis**: chegam ao
Sisprev e decidem se a regra alcança o requerimento.

O teto aberto é o desvio grave. Se `DATA_DIREITO_ATE` é o prazo de implementação
dos requisitos, então `31/12/2099` mantém as duas regras oferecendo, sem termo,
um regime que a norma estadual que as preserva condicionou a requisitos
cumpridos até 31/12/2024 — e o par gêmeo `0105`/`0106` grava o prazo. Duas
regras materialmente equivalentes, uma com prazo e outra sem, produzem
resultados opostos para quem completar os requisitos em 2025.

O piso em 1950 tem efeito menor na prática — quem se aposentou antes de 2003 o
fez por outra regra —, mas é falso no registro, e é o registro que a PGE lê.

`simulavel: N` nas duas (contra `S` em `0105`/`0106`) reforça a leitura de que o
par pode ser resíduo de ciclo anterior: o catálogo já não as oferece ao
simulador. Reforço, não prova.

# Questão a investigar

1. **Se `data_direito_ate` deve passar a `31/12/2024` e `data_direito_apos` a
   `31/12/2003`**, alinhando as duas ao par `0105`/`0106` e aos dispositivos que
   elas próprias vinculam. Campo deployável: decisão de quem responde por ele, e
   sob a RFC 0006 o veículo é um `Conjunto` `proposto`, não edição in-place.

2. **Se `regra-0085`/`0086` e `regra-0105`/`0106` são quatro regras ou duas.**
   Depois das duas correções do item 1, restariam divergindo apenas
   `ciclo_de_validacao`, `simulavel` e a sentinela de `data_adm_apos`
   (`01/01/1950` × `01/01/1910`) — nenhum deles critério jurídico. O par de
   ciclo 3º seria então candidato a consolidação N:1 (RFC 0004) ou a revogação
   pura num `Conjunto` (RFC 0006, `revoga`). A decisão é do IPERON:
   granularidade do catálogo é conveniência dele, não determinação da lei.

3. **A leitura de `DATA_DIREITO_APOS` continua não confirmada** (issue #39,
   semântica das janelas §5.3.2). Tudo o que este achado diz sobre o piso vale
   sob a leitura simétrica presumida. O que **não** depende dela é o fato
   jurídico: o art. 6º da EC 47/2005 impede efeito antes de 31/12/2003, qualquer
   que seja a semântica exata do campo.

4. **A vigência do art. 3º da EC 47/2005 em Rondônia é questão própria**, e
   está no `achado-0036`. Ela não altera nada do que este achado afirma sobre os
   dois valores gravados, mas altera o alcance da regra inteira.
