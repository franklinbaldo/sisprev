# Retrospectiva do Ciclo 1

Este documento é memória de método, não peça institucional. Ele registra o
percurso da auditoria do Ciclo 1 — inclusive as inferências que foram feitas e
depois desfeitas —, porque isso não cabe no relatório que circula assinado, que
se manifesta sobre o resultado e não sobre como se chegou a ele
(`docs/relatorio-ciclo/relatorio.md`, "Como este documento está organizado").

Refere-se ao estado do repositório na PR #131, em 06/08/2026.

## O que mudou durante o ciclo

O Bloco C entrou no ciclo com quatro origens legadas e oito destinos, e saiu
com quatro origens e **sessenta** destinos, em três famílias de vinte causas.
Entre um estado e outro houve três decomposições sucessivas — 8, depois 40,
depois 60 — e duas decisões opostas sobre a carga de homologação.

A cronologia importa menos que os pontos em que o desenho mudou:

- **8 → 40.** Uma unidade por moléstia do rol do art. 30, § 8º, em vez de uma
  categoria "doença catalogada", mais o recorte do ciclo para a norma em vigor.
- **40 → 60.** A revisão das fundamentações mostrou que a divisão em duas
  coortes de ingresso era **insuficiente**, não apenas incompleta: os arts. 24,
  *caput*, 25 e 27, I condicionam o que dispõem à ausência da opção pelo regime
  de previdência complementar, de modo que o servidor optante não era alcançado
  por nenhuma das duas coortes.
- **Carga: 40 → 20 → 60.** As vinte unidades da família sujeita ao regime
  complementar foram marcadas `pendente_mapeamento_sisprev`, o que — pela
  atomicidade — reteve quarenta destinos fora da carga; depois a decisão foi
  revista e as sessenta entraram.

## Onde houve retrabalho

**A cardinalidade foi refeita com as unidades já escritas.** As quarenta
unidades de 2004+ tiveram de ser renomeadas (ids e nomes projetados), e vinte
novas foram geradas, porque o discriminante "vínculo com o regime complementar"
só apareceu na revisão das fundamentações. O custo não foi de uma regra: foi da
decomposição inteira, mais os documentos centrais que a descreviam.

**Os nomes projetados foram reescritos três vezes** — ordem das facetas,
vocabulário ("Incapacidade permanente" → "Incapacidade"), e depois a troca de
"coorte de ingresso" por "família de ingresso e vínculo com o RPC".

**A decisão sobre a carga foi tomada duas vezes**, com propagação documental
completa em cada uma: relatório, ciclo, conformidade, matriz, RFC e corpo da PR.

**Um índice ficou quebrado por várias rodadas.** `okf/regras-propostas/regras/index.md`
era o único índice do repositório mantido à mão, e nenhuma guarda o cobria:
depois da renomeação em massa ele passou a listar os quarenta ids anteriores,
com quarenta links para arquivos inexistentes. Foi encontrado por acaso, ao se
conferir outra coisa.

## Inferências rejeitadas, e o que as corrigiu

| inferência inicial                                                             | evidência que a corrigiu                                                                                                                            | decisão final                                                                                                |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Duas coortes de ingresso bastam para a LCE 1.100/2021                          | O texto dos arts. 24, *caput*, 25 e 27, I exige, em todos, a ausência da opção pelo § 16                                                            | Três famílias; o optante deixa de ficar sem regra                                                            |
| `selecao_por` estava juridicamente errado nas 40 unidades sem RPC              | A conferência mostrou que os requisitos estavam certos; o defeito era do **contrato do campo**, que declara os itens disjuntivos                    | Campo retirado das 40; nenhum requisito alterado; correção descrita como de schema, não como achado jurídico |
| A opção pelo regime complementar pode ser feita em qualquer data               | CF, art. 40, § 16 — a opção cabe a quem ingressou até a data da instituição; a partir dela a sujeição é automática                                  | As duas vias da terceira família são **repartidas no tempo**                                                 |
| O Sisprev não comporta o teto do RGPS nem a opção pelo § 16                    | O catálogo não tem coluna para a opção — mas as origens legadas estão em produção, são simuláveis e já alcançam quem ingressou depois de 06/11/2018 | A formulação passa a ser "não se sabe **como** o sistema faz"; a conferência é objeto da homologação         |
| As 40 unidades retidas aguardam representação no cadastro para entrar na carga | Exigir certeza operacional antes da carga impede a verificação capaz de produzi-la                                                                  | As sessenta entram, vinte e duas com ressalva                                                                |
| A granularidade de uma regra por moléstia é imposição do § 8º                  | Quinze moléstias compartilham o mesmo regime; só o inciso XVI restringe ao magistério                                                               | Escolha de modelagem, declarada como tal no relatório                                                        |

Nenhuma dessas hipóteses virou campo novo, estado novo ou camada de schema. É
deliberado: hesitação de revisão não deve ser promovida a regra permanente.

## Lições generalizáveis

**Cada etapa exige o seu grau de certeza, e não o da seguinte.** A auditoria
jurídica exige fundamentação normativa suficiente; a entrada em homologação,
projeção completa e uma pergunta operacional testável; a ativação em produção,
o resultado da homologação e os controles. Boa parte do retrabalho veio de
exigir, numa etapa, a certeza que só a seguinte poderia produzir.

**Reconhecimento operacional antes do desenho.** Antes de concluir que o
sistema "não comporta", levantar quais regras já atendem a população, que
valores de domínio fechado já são usados, onde o dado mora (linha da regra,
cadastro do segurado, processo) e o que é conferível antes do ato.

**Matriz de discriminantes antes da geração em massa.** Um discriminante
descoberto depois custa a cardinalidade inteira.

**Expressão lógica e cenários antes do template.** Escrever a condição de cada
família em linguagem corrente, marcar onde há **e** e onde há **ou**, resolver
as fronteiras, e só então replicar.

**Verificação manual é controle de primeira classe.** `simulavel: N` pode ser a
representação honesta de uma regra cuja seleção exige instrução. O que se exige
é declarar quem verifica, quando, com que prova, antes de qual ato e com que
consequência na falta.

**Classificar a pendência pelo efeito.** Jurídica, operacional testável,
técnica sem projeção, externa, risco residual. Sem isso, todo desconhecimento
vira bloqueio.

**Atomicidade define entrada conjunta, não certeza prévia.** Ela protege contra
substituição parcial; usá-la para reter um componente por dúvida operacional de
um membro a converte de garantia em obstáculo.

**O que pode envelhecer deve ser derivado; o que pode quebrar, testado.** O
índice manual é a demonstração: contrato escrito no `CLAUDE.md` ("índices são
derivados"), implementação que não o cumpria, nenhuma guarda entre os dois.

**Separar escolha jurídica, de modelagem e operacional.** Uma regra por moléstia
é modelagem; o teto do RGPS é norma; o controle manual é operação. O relatório
deve dizer de qual tipo é cada decisão, sem vestir arquitetura com toga de
dispositivo legal.

**Testar também o erro que se quer impedir.** Gate que só se exercita quando
passa não está sendo exercitado.

## Controles promovidos a spec, gate ou memória

| lição                                                                                                                      | onde ficou permanente                            |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| Limiar de evidência para a carga; `pendente_mapeamento_sisprev` restrito                                                   | `okf/spec/regraproposta.md`                      |
| Carga não pressupõe automatização integral; cinco planos distintos                                                         | `okf/spec/regraproposta.md`                      |
| Atomicidade disciplina entrada conjunta, não certeza prévia                                                                | `okf/spec/regraproposta.md`                      |
| Seleção é conjugação cumulativa; `selecao_por` só onde há alternativa                                                      | `okf/spec/regraproposta.md`                      |
| Protocolo de abertura do ciclo (cinco levantamentos)                                                                       | `okf/spec/ciclo.md`                              |
| Distinguir catálogo/dados/motor/instrução/ato; testar a lógica antes de gerar                                              | `CLAUDE.md`                                      |
| Três famílias, janelas sem lacuna, cenários de fronteira                                                                   | `scripts/testar_tres_regimes_incapacidade.py`    |
| 60 destinos, 60 na carga, nenhum `pendente`, `simulavel: N` nas sessenta                                                   | `scripts/testar_carga_de_implantacao_bloco_c.py` |
| Seleção manual entra; comportamento a confirmar entra com ressalva; sem projeção fica fora; componente misto entra inteiro | `scripts/testar_carga_de_implantacao.py`         |
| Índice de propostas derivado e conferido no CI                                                                             | `scripts/derivar.py`, `.github/workflows/ci.yml` |
| Pendência repetida consolidada por enunciado                                                                               | `site/src/lib/relatorio-ciclo.ts`                |
| Pendência em lista frouxa não some do impresso                                                                             | `site/src/lib/relatorio.ts`                      |

## Débitos técnicos remanescentes

- **Gate de existência de links internos** nos bundles `okf/`. O índice de
  propostas deixou de poder apodrecer porque passou a ser derivado, mas nada
  confere as demais referências entre documentos.
- **Marcadores do relatório sem gate.** `aplicarTotais` estoura em marcador
  desconhecido, mas nada impede que um número volte a ser escrito literal na
  prosa — foi assim que "as duas regras com ressalva" sobreviveu à mudança de
  contagem.
- **Testes de mutação** existem como prática manual (as regressões injetadas
  nesta PR), não como rotina executável.
- **Consolidação de pendência por família.** A pendência `C1-R34` imprime os
  dezenove ids que alcança; como são exatamente as causas qualificadas de uma
  família, uma redação por conjunto seria mais legível. É escolha de produto,
  não defeito.
- **`cf88/art-40-par-14` e `art-40-par-15`** não foram transcritos: a fonte
  esteve indisponível, e transcrição literal exige fonte consultada.
- **Dependências externas** `C1-R73`, `C1-R74`, `C1-R75`, `C1-R34`, `C1-R15` —
  registradas na issue #124 e nas ressalvas das unidades que alcançam.

## Checklist para o próximo ciclo

Antes de gerar unidade alguma:

- [ ] matriz preliminar de discriminantes escrita e revista;
- [ ] inventário da evidência operacional do catálogo legado para a população
  alcançada;
- [ ] componentes de atomicidade calculados;
- [ ] expressão lógica de cada família em linguagem corrente, com **e** e
  **ou** explícitos;
- [ ] cenários de fronteira definidos, incluindo véspera e dia de cada marco;
- [ ] pendências classificadas pelo efeito que produzem.

Ao gerar:

- [ ] template replicado só depois de a lógica passar nos cenários;
- [ ] gate que reconstrói a semântica a partir do dado, não que compara
  rótulos;
- [ ] gate exercitado contra regressão injetada, e não só contra o caminho
  feliz.

Ao fechar:

- [ ] derivados regenerados e conferidos no `git diff`;
- [ ] relatório **renderizado** inspecionado, não só o Markdown;
- [ ] números do relatório vindo de marcador, nunca literais;
- [ ] cada decisão identificada como jurídica, de modelagem ou operacional.
