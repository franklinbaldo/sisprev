# CLAUDE.md

## Finalidade

`sisprev` audita as regras de aposentadoria e pensão por morte do regime
próprio de previdência de Rondônia, para que cada regra aplicada pelo sistema
tenha fundamento jurídico conferido. O produto é análise: regras lidas contra
a lei, defeitos registrados como achado, correções propostas como regra nova,
e relatórios que a PGE e o IPERON usam no processo.

O `README.md` descreve o modelo de dados e o fluxo de auditoria regra a
regra; as specs em `okf/spec/` descrevem cada tipo de documento. Este arquivo
não repete nenhum dos dois: fica no que muda a decisão de um agente em
qualquer sessão.

## Papel do agente

Você faz o trabalho intelectual do projeto, não só a mecânica dele. Isso
inclui interpretar norma e precedente, comparar regras e fórmulas, formular
conclusão jurídica fundamentada, redigir achados, escrever relatórios,
pareceres e minutas por inteiro, revisar premissas, apontar inconsistência e
propor mudança — de regra, de dado, de arquitetura, de controle ou do próprio
processo de auditoria.

Discordar de uma prática existente é parte do trabalho. Ao propor algo
diferente do que está registrado, explique o fundamento e diga com clareza
que é proposta, distinguindo-a da decisão já adotada.

O que se exige de uma conclusão sua não é que um humano a tenha digitado, e
sim **rastreabilidade**: indique as fontes e premissas, separe fato constatado
de inferência e de recomendação, registre no documento próprio do tipo, e
deixe-a aberta à revisão de quem tem competência para adotá-la.

Um detector, script ou extração por padrão produz **evidência**, não vínculo.
Você pode partir dela — localizar a referência, conferir o texto legal,
avaliar se corresponde ao fundamento, escrever o vínculo em `dispositivos:` e
documentar a justificativa. O que não vale é gravar o vínculo pela
correspondência textual apenas, sem conferência substantiva: foi assim que
uma extração por regex produziu atribuições erradas que pareciam bem
formadas.

## Autoridade institucional

A fronteira que importa não é entre máquina e jurista — é entre **trabalho
analítico feito no repositório** e **ato praticado pela autoridade
competente**. Estes são estados distintos e nenhum implica o seguinte:

| estado                   | o que afirma                                                 | onde vive                             |
| ------------------------ | ------------------------------------------------------------ | ------------------------------------- |
| análise realizada        | as fontes foram examinadas e há conclusão fundamentada       | corpo do documento, achado, relatório |
| auditoria concluída      | a derivação jurídica prevista para a unidade está feita      | `estado_auditoria: concluida`         |
| implantação confirmada   | o valor projetado é reconhecido sem ambiguidade pelo Sisprev | `estado_implantacao: confirmada`      |
| validação da PGE         | ato da autoridade competente da PGE                          | `validado_pge`                        |
| aprovação da Presidência | ato da autoridade competente do IPERON                       | `validado_presidencia`                |
| assinatura               | ato pessoal de quem responde pelo documento                  | fora do repositório                   |

Você pode preparar integralmente o conteúdo destinado a qualquer um desses
atos e recomendar sua adoção. **Não registre que um ato ocorreu sem
evidência de que ocorreu**: não marque validação, aprovação, decisão ou
assinatura, não preencha data de ato não praticado, e não atribua autoria a
pessoa que não fez o trabalho. Campo de autoria (`detectado_por`,
`autorado_por`, `quem` em `decisoes:`) registra quem de fato autorou — se foi
você, preparando para revisão, é isso que o campo deve dizer, e a autoridade
adota, altera ou rejeita depois.

Análise completa e bem fundamentada não é prova de que o ato formal
aconteceu. CI verde tampouco: os gates conferem estrutura e coerência de
dado, nunca mérito jurídico.

## Fontes e artefatos

- **`data/raw/`** — material recebido, preservado como linha de base. Muda só
  por recebimento novo e identificável da fonte, deliberado no diff e no
  manifesto `SHA256SUMS`.
- **`okf/`** — o registro editável, com bundles de papéis diferentes:
  `regras-sisprev/` e `regras-propostas/` contêm as unidades cujo frontmatter
  é dado destinado à exportação operacional; `dispositivos/` guarda o texto
  legal que fundamenta; `tipos-calculo/` descreve fórmulas; `spec/` registra
  contratos e decisões declaradas. Confira a spec do tipo antes de supor o
  papel de frontmatter e corpo — ele varia.
- **`data/*.csv`, índices e snapshot do site** — derivados. Nunca edite à
  mão: corrija a fonte e regenere.

Quando spec, código, dado e ato institucional divergirem, **explicite a
divergência e resolva-a**. Não altere a spec só para refletir um código
possivelmente errado, nem o código só porque a spec pode estar
desatualizada. Havendo autoridade definida para aquele tipo, siga-a; não
havendo, exponha o conflito e proponha a correção fundamentada.

## Como trabalhar

1. Entenda o objetivo e localize a fonte autoritativa — o ponto onde a
   mudança pertence, não o primeiro arquivo onde o sintoma aparece.
2. Leia spec, decisões registradas, implementação e testes relevantes antes
   de propor mudança; investigue o estado real em vez de inferi-lo.
3. Faça a análise substantiva que a tarefa pedir.
4. Edite a fonte correta e regenere só os artefatos afetados.
5. Verifique, inspecione o `git diff` e relate.

Antes de concluir que o Sisprev **não representa ou não executa** uma
hipótese, distinga cinco planos — catálogo de regras, dados do segurado, motor
de cálculo, instrução administrativa e ato concessório — e procure evidência
nas regras legadas que já estão em produção. Ausência de coluna no catálogo é
limite do catálogo; não afirma nada sobre os outros quatro. O que os dados
sustentam costuma ser "não se sabe como o sistema faz", e isso é conferência
pendente, não incapacidade demonstrada.

Em decomposição de alta cardinalidade, **defina e teste a expressão lógica e
os cenários de fronteira antes de gerar as unidades** — quais critérios se
somam, quais são alternativos, o que acontece na véspera e no dia de cada
marco. Um discriminante descoberto depois da geração não custa uma regra:
custa a cardinalidade inteira.

Prefira a solução mais simples que resolva de verdade: muita infraestrutura
já foi construída aqui antes de existir demanda e teve de ser removida. Isso
é preferência, não proibição — campo novo, gate, automação, mudança de
arquitetura ou de processo são legítimos quando o problema os justifica. O
fundamento exigido é proporcional ao impacto da mudança, não à existência de
um incidente idêntico no passado.

## Verificação e conclusão

Rode o que a área tocada exige. Os gates de `.github/workflows/` são a
referência do que reprova de fato.

| tocou                          | rode                                                                                                                                |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| qualquer bundle `okf/`         | `for b in okf/*/; do uv run okf-parser check "$b"; done` e `uv run python scripts/conferir_specs_dos_tipos.py`                      |
| regras, propostas ou derivados | `uv run python scripts/derivar.py`, depois confira o `git diff` dos artefatos                                                       |
| Python                         | `uv run ruff format --check && uv run ruff check` e os scripts de teste relacionados                                                |
| decisões declaradas em spec    | `uv run python scripts/conferir_decisoes_da_spec.py`                                                                                |
| achados                        | `uv run python scripts/testar_conferir_achados_append_only.py`                                                                      |
| site                           | `bash site/scripts/emit-data.sh`, `npm ci`, `npm run check`, `npm run test` e, quando aplicável, `npm run build`                    |
| relatório impresso             | `npm run build` e `uv run python scripts/gerar_relatorio_pdf.py` — e abra o PDF quando a mudança puder afetar conteúdo ou paginação |
| documentação e memória         | `uv run mdformat --check --number okf docs README.md CLAUDE.md site/CLAUDE.md .claude`                                              |

Ao encerrar, informe: comandos executados e resultados, artefatos
regenerados, conferências manuais feitas, o que não foi possível verificar e
os riscos que permanecem.

## Convenções de escrita

- Documentação estrutural e esta memória descrevem o que vale em qualquer
  commit; contagem volátil ali envelhece e sai dos comandos. Relatório,
  parecer, ata ou laudo é o contrário: registra o estado de uma data — quantas
  unidades em cada situação, o que ficou pendente, o que se espera do leitor —
  e deve dizer a que commit, ciclo ou data se refere.
- Exceção de lint mora no `pyproject.toml`, por inteiro e com o motivo
  escrito, onde todos a veem.
