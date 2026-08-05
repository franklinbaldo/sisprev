# Matriz de derivação e verificação do Ciclo 1

> Documento de auditoria, central ao Ciclo 1. Substitui o uso do checkbox
> repetitivo "concluir a conferência humana desta regra" nas quarenta regras
> do Bloco C por uma cadeia única, auditável: fonte normativa → requisito →
> requisito derivado → regra → representação → forma de verificação →
> responsável → evidência. Não decide questão jurídica nova — organiza e
> torna rastreáveis decisões já tomadas nas sessões S0 a S6, na PR #120 e na
> PR #128, apontando exatamente onde cada uma ainda carece de decisão.

## 1. Finalidade

Cada uma das quarenta regras propostas do Bloco C trazia, no próprio corpo,
uma pendência idêntica: "concluir a conferência humana desta regra". Isso
tinha dois defeitos. Primeiro, escondia que a maior parte do que a caixa
cobria — dispositivo correto para a moléstia, datas corretas para a coorte,
projeção de cálculo correta para a causa — é a **mesma verificação,
repetida quarenta vezes**, e pode ser demonstrada uma única vez, por
requisito, contra todas as regras que o instanciam. Segundo, misturava essa
verificação repetitiva com as **decisões jurídicas de fato pendentes** —
o marco temporal do requisito de magistério, a confirmação operacional de
`Proporcionalidade Dias` — que não se repetem quarenta vezes: são poucas,
específicas, e é nelas que a atenção da coordenação precisa se concentrar.

Esta matriz separa as duas coisas. Ela lista os requisitos juridicamente e
operacionalmente relevantes do Ciclo 1, de onde cada um deriva, quais regras
o materializam, como ele se representa no catálogo, e qual é o caminho de
verificação — programático, não programático, ou os dois. O que resta
pendente aparece nas linhas da matriz, não em quarenta cópias do mesmo
checkbox.

## 2. Conceitos

**Colunas deployáveis.** As colunas do schema legado do Sisprev — datas,
`tipo_de_beneficio`, `tipo_calculo`, `integral`, `paridade` e as demais —
são os dados que efetivamente seriam enviados ao sistema. Um requisito
representado numa coluna deployável admite verificação determinística: o
valor gravado ou corresponde ao que a matriz exige, ou não corresponde, e
isso se confere por leitura de campo, sem julgamento de mérito.

**Nome da regra.** Não é rótulo decorativo. É a interface pela qual o
operador, o servidor ou um agente escolhem a regra certa e o checklist
correspondente. Por isso, um requisito sem coluna própria — o caso do
magistério — deve diferenciar o nome quando a diferença for necessária para
apontar que aquela regra exige uma verificação adicional.

**Fundamentação.** Pode conter requisito jurídico não verificável por
coluna. Isso não a torna informativa ou secundária: a fundamentação integra
o checklist jurídico-operacional da regra, e o requisito que ela carrega
continua obrigatório — verificado no caso concreto, não dispensado por
estar em prosa.

**Verificação programática e não programática.** "Programático" não é
sinônimo de "feito por máquina", nem "não programático" é sinônimo de
"humano". A distinção é de **natureza**:

- **verificação programática** — avaliação determinística a partir de campos
  estruturados e regras codificadas: cotejar se o dispositivo citado numa
  regra corresponde ao inciso que a moléstia do nome exige, se as datas
  correspondem à coorte, se `tipo_calculo`/`integral`/`paridade` correspondem
  à classe de causa. Reproduzível por script ou por agente seguindo o mesmo
  procedimento;
- **verificação não programática** — avaliação substantiva de documento,
  fato ou texto jurídico que não se reduz a cotejo de colunas: se o
  diagnóstico do caso corresponde à moléstia, se o servidor de fato ocupava
  cargo de magistério, se há nexo entre a doença e o trabalho. Pode ser
  realizada por pessoa, por agente, ou por pessoa assistida por agente — o
  que importa é que a avaliação é de mérito, não de correspondência
  estrutural, e por isso continua exigindo constatação no caso concreto,
  qualquer que seja quem a execute.

Um mesmo requisito pode ter as duas camadas: a correspondência entre regra e
classe de causa é programática; a constatação de que o caso do requerente se
enquadra naquela classe é não programática. A matriz registra as duas
separadamente, na coluna "Modo de verificação".

**Responsabilidade de verificação.** A pergunta que cada linha responde não
é apenas "em que campo mora o requisito", mas "quem ou o que garante que
esse requisito foi cumprido, por qual método, com qual evidência". A matriz
funciona como uma RACI adaptada ao processo de concessão — sem o
vocabulário formal de RACI, porque o processo tem só um executor por
requisito, não quatro papéis a distinguir.

## 3. Critério de completude

O ciclo está completo quando todos os requisitos desta matriz possuem
fonte, derivação, regras de destino e caminho de verificação; nenhuma regra
está sem requisito de origem; e nenhuma linha materialmente relevante
permanece sem responsável ou evidência. Instanciações repetitivas — a
mesma verificação estrutural em quarenta regras — podem ser demonstradas
programaticamente, sem exigir nova decisão jurídica para cada arquivo.

A validação não programática — humana, por agente, ou assistida —
incide sobre a matriz em si: as decisões jurídicas, as exceções, os
caminhos de verificação escolhidos e a suficiência das evidências exigidas.
A verificação programática comprova que essas decisões foram aplicadas de
modo consistente às regras que as instanciam. As duas são necessárias; nem
uma substitui a outra, e nenhuma delas precisa ser repetida regra a regra
quando já demonstrada por requisito.

Este critério substitui, para o Bloco C, a leitura anterior da condição 9 de
`okf/spec/ciclo.md` como "quarenta atos idênticos de leitura". A condição 9
— ausência de pendência que afete a cobertura material — se demonstra pela
matriz: toda linha com status `coberto` está verificada; toda linha
`pendente` ou `dependência externa` está identificada, classificada e
vinculada às regras que alcança, e é isso, não uma caixa por regra, que o
ciclo deve zerar antes do fechamento.

## 4. Árvore de derivação

```
C1-R00 Incapacidade permanente sob a LCE 1.100/2021
├── C1-R10 Aplicabilidade temporal e coorte
│   ├── C1-R11 ingresso até 31/12/2003 (paridade aplicável, salvo opção)
│   ├── C1-R12 ingresso a partir de 01/01/2004 (sem paridade)
│   └── C1-R13 janela de direito — a partir de 18/10/2021, inclusive
├── C1-R20 Classe juridicamente relevante da causa
│   ├── C1-R21 acidente em serviço
│   ├── C1-R22 moléstia profissional
│   ├── C1-R23 doença catalogada (rol do art. 30, § 8º)
│   │   ├── C1-R23a diagnóstico correspondente ao inciso do rol
│   │   ├── C1-R23b acometimento posterior à filiação ao RPPS
│   │   └── C1-R24 requisito adicional do inciso XVI: exercício de magistério
│   └── C1-R25 causa comum (ramo residual)
├── C1-R30 Forma de cálculo inicial
│   ├── C1-R31 média sem proporcionalização (art. 24 + § 13) — causas qualificadas
│   └── C1-R32 média proporcionalizada em dias (art. 26 + § 14) — causa comum
├── C1-R40 Integralidade/proporcionalidade
│   ├── C1-R41 integral: S — causas qualificadas
│   └── C1-R42 integral: N — causa comum
├── C1-R50 Paridade ou regime de reajuste
│   ├── C1-R51 paridade (art. 27, I) — coorte até 2003
│   └── C1-R52 sem paridade, regime do RGPS (art. 27, II) — coorte a partir de 2004
├── C1-R60 Limitações constitucionais e opção do § 16
│   └── C1-R61 opção pelo regime de previdência complementar (art. 40, § 16, CF)
└── C1-R70 Evidência, instrução e verificação
    ├── C1-R71 verificação da causa (geral)
    ├── C1-R72 verificação do vínculo com o magistério
    ├── C1-R73 captura e classificação da causa pelo Sisprev
    ├── C1-R74 confirmação operacional do rótulo de cálculo projetado
    └── C1-R75 protocolo institucional de reconhecimento do nexo de moléstia profissional
```

A árvore não esgota o direito previdenciário: esgota o que o Bloco C do
Ciclo 1 precisa para selecionar a regra certa e calcular o benefício.
`C1-R60`/`C1-R61` cobre só a ressalva que a paridade da coorte até 2003
carrega; as demais regras do regime de previdência complementar são
matéria de outro ciclo.

## 5. Matriz de requisitos

| ID      | Deriva de      | Requisito                                                                          | Fonte                                                                                                      | Regras alcançadas                                                      | Representação                                                                                                        | Modo de verificação                                      | Executor responsável                                         | Como verificar                                                                                                                                                                                                                                            | Evidência exigida                                                                                                                                                        | Momento               | Status                                             | Observações                                                                                                                                                                    |
| ------- | -------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| C1-R00  | —              | Aposentadoria por incapacidade permanente sob a LCE 1.100/2021                     | CF/88, art. 40, § 1º, I (EC 103/2019); LCE 1.100/2021, art. 30, caput                                      | Todas as 40 regras propostas do Bloco C                                | `tipo_de_beneficio: APOSENTADORIA POR INCAPACIDADE PERMANENTE`                                                       | programático                                             | compilador (`derivar.py`) / verificação por agente           | conferir que as 40 regras gravam o mesmo `tipo_de_beneficio`                                                                                                                                                                                              | leitura de campo                                                                                                                                                         | seleção               | coberto                                            | correção de A1/A11, PR #120                                                                                                                                                    |
| C1-R10  | C1-R00         | Aplicabilidade temporal separa duas coortes de ingresso                            | LCE 1.100/2021, art. 30; matriz T2/T7 de `ciclo-01.md`                                                     | Todas as 40                                                            | `aplicabilidade_temporal.datas_legadas`                                                                              | programático                                             | compilador / agente                                          | conferir que cada regra tem exatamente uma das duas faixas de `data_adm_*`                                                                                                                                                                                | leitura de campo                                                                                                                                                         | seleção               | coberto                                            | —                                                                                                                                                                              |
| C1-R11  | C1-R10         | Ingresso em cargo efetivo até 31/12/2003 — paridade aplicável, salvo opção do § 16 | LCE 1.100/2021, art. 27, I; decisão Q1 (inclusividade), `okf/spec/regra.md`                                | 20 regras `*-ate-2003-*`                                               | `data_adm_ate: 31/12/2003`, `data_adm_apos: 01/01/1950` (sentinela)                                                  | programático                                             | compilador / agente                                          | cotejar `data_adm_ate`/`data_adm_apos` contra a fronteira de coorte                                                                                                                                                                                       | leitura de campo                                                                                                                                                         | seleção               | coberto                                            | sentinela conforme `site/src/lib/sentinela.ts`                                                                                                                                 |
| C1-R12  | C1-R10         | Ingresso em cargo efetivo a partir de 01/01/2004 — sem paridade                    | LCE 1.100/2021, art. 27, II                                                                                | 20 regras `*-apos-2003-*`                                              | `data_adm_apos: 01/01/2004`, `data_adm_ate: 31/12/2099` (sentinela)                                                  | programático                                             | compilador / agente                                          | idem, coorte oposta                                                                                                                                                                                                                                       | leitura de campo                                                                                                                                                         | seleção               | coberto                                            | —                                                                                                                                                                              |
| C1-R13  | C1-R00         | Direito somente para requisitos implementados a partir de 18/10/2021               | LCE 1.100/2021, vigência (publicação em 18/10/2021)                                                        | Todas as 40                                                            | `data_direito_apos: 18/10/2021`, `data_direito_ate: 31/12/2099`                                                      | programático                                             | compilador / agente                                          | conferir valor fixo em todas as 40                                                                                                                                                                                                                        | leitura de campo                                                                                                                                                         | seleção               | coberto                                            | —                                                                                                                                                                              |
| C1-R20  | C1-R00         | A causa da incapacidade determina o ramo de cálculo                                | LCE 1.100/2021, art. 30, caput                                                                             | Todas as 40                                                            | `predicados.causa_incapacidade` (schema enriquecido)                                                                 | misto                                                    | agente (estrutural) / junta médica (caso concreto)           | ver C1-R21–C1-R25                                                                                                                                                                                                                                         | ver C1-R21–C1-R25                                                                                                                                                        | seleção               | coberto                                            | classe escalar, uma por regra (RFC 0004 §1.2, §3)                                                                                                                              |
| C1-R21  | C1-R20         | Causa: acidente em serviço                                                         | LCE 1.100/2021, art. 30, § 5º                                                                              | 2 regras `*-acidente-em-servico.md`                                    | `predicados.causa_incapacidade: acidente_em_servico`; nome; fundamentação                                            | misto                                                    | junta médica oficial e instrução previdenciária do IPERON    | perícia oficial + apuração administrativa do nexo com o serviço                                                                                                                                                                                           | laudo médico oficial, comunicação e apuração do acidente, prontuários, assentamentos funcionais                                                                          | instrução             | coberto                                            | fluxo definido nas duas regras                                                                                                                                                 |
| C1-R22  | C1-R20         | Causa: moléstia profissional                                                       | LCE 1.100/2021, art. 30, caput                                                                             | 2 regras `*-molestia-profissional.md`                                  | `predicados.causa_incapacidade: molestia_profissional`; nome; fundamentação                                          | misto                                                    | junta médica oficial e instrução previdenciária do IPERON    | perícia oficial + apuração administrativa do nexo ocupacional                                                                                                                                                                                             | laudo médico oficial, histórico ocupacional, prontuários, exames                                                                                                         | instrução             | coberto, com risco anotado                         | ver C1-R75: nenhum dos dois regimes estaduais define "moléstia profissional" (RFC 0004, P-6)                                                                                   |
| C1-R23  | C1-R20         | Causa: doença catalogada (rol do art. 30, § 8º)                                    | LCE 1.100/2021, art. 30, § 8º, caput e incisos I a XVI                                                     | 34 regras `*-doenca-*.md`                                              | `predicados.causa_incapacidade: doenca_catalogada`; nome (moléstia); fundamentação                                   | misto                                                    | agente (correspondência) / junta médica (diagnóstico)        | ver seção 6 (matriz de cobertura por moléstia)                                                                                                                                                                                                            | ver seção 6                                                                                                                                                              | seleção/instrução     | coberto                                            | dezessete moléstias, granularidade do IPERON (RFC 0004 §0)                                                                                                                     |
| C1-R23a | C1-R23         | O dispositivo citado corresponde ao inciso da moléstia do nome                     | LCE 1.100/2021, art. 30, § 8º, incisos I a XVI                                                             | 34 regras `*-doenca-*.md`                                              | `taxonomias[].ref` (inciso) + fundamentação                                                                          | programático                                             | agente / script                                              | cotejar `art-30-par-8-inc-*` citado contra o texto do inciso e o nome da moléstia                                                                                                                                                                         | leitura de campo + texto do dispositivo                                                                                                                                  | seleção               | coberto                                            | verificado nesta sessão contra o texto dos 16 incisos (ver seção 6)                                                                                                            |
| C1-R23b | C1-R23         | Acometimento posterior à filiação ao RPPS de Rondônia                              | LCE 1.100/2021, art. 30, § 8º, caput                                                                       | 34 regras `*-doenca-*.md`                                              | `requisitos_verificacao_humana[0]`; fundamentação                                                                    | não programático                                         | junta médica oficial                                         | perícia oficial cotejando data do acometimento com data de filiação                                                                                                                                                                                       | laudo médico oficial, exames, prontuários, assentamentos funcionais de filiação                                                                                          | instrução             | coberto                                            | fato do caso — não se conclui pelo cadastro                                                                                                                                    |
| C1-R24  | C1-R23         | Exercício de cargo de magistério, para surdez permanente e anomalia da fala        | LCE 1.100/2021, art. 30, § 8º, inciso XVI                                                                  | 4 regras `*-doenca-{surdez-permanente,anomalia-da-fala}-magisterio.md` | `predicados.exercicio_magisterio: S`; sufixo `magisterio` no nome; `requisitos_verificacao_humana[1]`; fundamentação | não programático                                         | unidade de gestão de pessoas (assentamentos funcionais)      | conferir ficha funcional, atos de nomeação, exercício e lotação em cargo de magistério                                                                                                                                                                    | assentamento funcional que comprove o exercício de magistério                                                                                                            | instrução             | **pendente**                                       | marco temporal da aferição (acometimento, instrução, concessão) não fixado — decisão jurídica da coordenação, issue #121                                                       |
| C1-R25  | C1-R20         | Causa comum (ramo residual, exclusão das demais causas)                            | LCE 1.100/2021, art. 30, caput                                                                             | 2 regras `*-causa-comum.md`                                            | `predicados.causa_incapacidade: causa_comum`; nome; fundamentação                                                    | misto                                                    | junta médica oficial e instrução previdenciária do IPERON    | investigação que exclua acidente em serviço, moléstia profissional e doença catalogada                                                                                                                                                                    | laudo médico oficial, prontuários, histórico ocupacional, apuração de eventual acidente, cotejo com o rol                                                                | instrução             | coberto                                            | silêncio ou prova insuficiente não bastam para excluir as classes qualificadas                                                                                                 |
| C1-R30  | C1-R00         | A causa determina a forma de cálculo do provento inicial                           | LCE 1.100/2021, arts. 24, 26, 30 §§ 13-14                                                                  | Todas as 40                                                            | `projecao.tipo_calculo`, `integral`                                                                                  | programático                                             | compilador / agente                                          | conferir correspondência causa → fórmula                                                                                                                                                                                                                  | leitura de campo                                                                                                                                                         | cálculo               | coberto                                            | ver C1-R31/C1-R32                                                                                                                                                              |
| C1-R31  | C1-R30         | Média sem proporcionalização pelo tempo de contribuição                            | LCE 1.100/2021, art. 24 (base) + art. 30, § 13 (remissão)                                                  | 38 regras (acidente, moléstia profissional, 17 doenças × 2 coortes)    | `tipo_calculo: Valor Médio`, `integral: S`                                                                           | programático                                             | compilador / agente                                          | conferir `tipo_calculo`/`integral` para toda regra de causa qualificada                                                                                                                                                                                   | leitura de campo                                                                                                                                                         | cálculo               | coberto                                            | `forma-calculo-media-80-contribuicoes-lce1100.md`, fidelidade parcial (detalhe operacional, não a base)                                                                        |
| C1-R32  | C1-R30         | Média proporcionalizada em dias, identificada univocamente no Sisprev              | LCE 1.100/2021, art. 26 (fração) + art. 30, § 14 (remissão); `achado-0061`                                 | 2 regras `*-causa-comum.md`                                            | `tipo_calculo: Proporcionalidade Dias`, `integral: N`                                                                | programático (projeção) / dependência externa (execução) | compilador (projeção) / IPERON e fornecedor (execução)       | `achado-0061`: mesmo rótulo grava, no catálogo, três fórmulas juridicamente distintas e quatro tipos de benefício, sem desambiguação confirmada; fórmula jurídica exigida por esta regra confirmada em `forma-calculo-media-proporcional-dias-lce1100.md` | confirmação do IPERON/fornecedor de que o rótulo (ou tipo discriminante proposto) identifica univocamente esta fórmula, ou demonstração de que outro campo já desambigua | cálculo / implantação | **pendente (achado + dependência de implantação)** | colisão de enum documentada, não detalhe de fidelidade textual — RFC 0004 §5.3; `estado_proposta: preview`, issue #122, `achado-0061`                                          |
| C1-R40  | C1-R30         | Integralidade decorre da classe de causa                                           | LCE 1.100/2021, art. 30, caput                                                                             | Todas as 40                                                            | `integral`                                                                                                           | programático                                             | compilador / agente                                          | conferir `integral` contra a classe                                                                                                                                                                                                                       | leitura de campo                                                                                                                                                         | cálculo               | coberto                                            | —                                                                                                                                                                              |
| C1-R41  | C1-R40         | `integral: S` para causas qualificadas                                             | LCE 1.100/2021, art. 30, caput (exceção)                                                                   | 38 regras                                                              | `integral: S`                                                                                                        | programático                                             | compilador / agente                                          | leitura de campo                                                                                                                                                                                                                                          | leitura de campo                                                                                                                                                         | cálculo               | coberto                                            | —                                                                                                                                                                              |
| C1-R42  | C1-R40         | `integral: N` para causa comum                                                     | LCE 1.100/2021, art. 30, caput                                                                             | 2 regras                                                               | `integral: N`                                                                                                        | programático                                             | compilador / agente                                          | leitura de campo                                                                                                                                                                                                                                          | leitura de campo                                                                                                                                                         | cálculo               | coberto                                            | —                                                                                                                                                                              |
| C1-R50  | C1-R00         | O regime de reajuste depende da coorte de ingresso                                 | LCE 1.100/2021, art. 27                                                                                    | Todas as 40                                                            | `paridade`                                                                                                           | programático                                             | compilador / agente                                          | conferir `paridade` contra a coorte                                                                                                                                                                                                                       | leitura de campo                                                                                                                                                         | manutenção            | coberto                                            | —                                                                                                                                                                              |
| C1-R51  | C1-R50, C1-R11 | Paridade, salvo opção do § 16                                                      | LCE 1.100/2021, art. 27, I; EC 41/2003, art. 7º (conteúdo da paridade)                                     | 20 regras `*-ate-2003-*`                                               | `paridade: S`                                                                                                        | programático                                             | compilador / agente                                          | leitura de campo                                                                                                                                                                                                                                          | leitura de campo                                                                                                                                                         | manutenção            | coberto                                            | condicionado a C1-R61                                                                                                                                                          |
| C1-R52  | C1-R50, C1-R12 | Reajuste nos termos do RGPS, sem paridade                                          | LCE 1.100/2021, art. 27, II                                                                                | 20 regras `*-apos-2003-*`                                              | `paridade: N`                                                                                                        | programático                                             | compilador / agente                                          | leitura de campo                                                                                                                                                                                                                                          | leitura de campo                                                                                                                                                         | manutenção            | coberto                                            | —                                                                                                                                                                              |
| C1-R60  | C1-R00         | A opção pelo regime de previdência complementar afeta a paridade                   | CF/88, art. 40, § 16 (EC 103/2019)                                                                         | 20 regras `*-ate-2003-*` (onde `paridade: S`)                          | fundamentação (sem coluna própria)                                                                                   | não programático                                         | unidade concessora / instrução previdenciária                | conferir, no processo, se houve opção expressa e prévia                                                                                                                                                                                                   | registro da opção ou de sua ausência no processo administrativo                                                                                                          | instrução             | coberto (sem campo dedicado)                       | ver C1-R61                                                                                                                                                                     |
| C1-R61  | C1-R60         | Ausência de opção pelo regime de previdência complementar                          | CF/88, art. 40, § 16 (EC 103/2019); LCE 1.100/2021, art. 27, I                                             | 20 regras `*-ate-2003-*`                                               | fundamentação                                                                                                        | não programático                                         | unidade concessora / instrução previdenciária                | idem                                                                                                                                                                                                                                                      | idem                                                                                                                                                                     | instrução             | coberto (sem campo dedicado)                       | cadastro não tem coluna própria; requisito atendido pela fundamentação, conferido no processo                                                                                  |
| C1-R70  | C1-R00         | Todo requisito tem caminho de verificação definido                                 | `okf/spec/regraproposta.md`; RFC 0004 §7                                                                   | Todas as 40                                                            | `requisitos_verificacao_humana[]`                                                                                    | misto                                                    | agente (estrutura) / IPERON/coordenação (execução)           | ver C1-R71–C1-R75                                                                                                                                                                                                                                         | ver C1-R71–C1-R75                                                                                                                                                        | —                     | coberto                                            | —                                                                                                                                                                              |
| C1-R71  | C1-R70         | Verificação geral da causa constatada no caso concreto                             | RFC 0004 §7 (cinco partes do requisito de verificação humana)                                              | Todas as 40                                                            | `requisitos_verificacao_humana[0]`                                                                                   | não programático                                         | junta médica oficial e/ou instrução previdenciária do IPERON | ver C1-R21/C1-R22/C1-R23b/C1-R25                                                                                                                                                                                                                          | ver C1-R21/C1-R22/C1-R23b/C1-R25                                                                                                                                         | instrução             | coberto                                            | —                                                                                                                                                                              |
| C1-R72  | C1-R70, C1-R24 | Verificação do vínculo com o magistério                                            | issue #121                                                                                                 | 4 regras do inciso XVI                                                 | `requisitos_verificacao_humana[1]`                                                                                   | não programático                                         | unidade de gestão de pessoas                                 | ver C1-R24                                                                                                                                                                                                                                                | ver C1-R24                                                                                                                                                               | instrução             | coberto (caminho); marco pendente                  | o caminho de verificação está definido; o marco temporal é C1-R24                                                                                                              |
| C1-R73  | C1-R70         | Captura e classificação da causa da incapacidade pelo Sisprev                      | `docs/analysis/q6-causa-incapacidade.md` (Q6-S/Q6-T); issue #124                                           | Todas as 40                                                            | nenhuma — não representável no schema atual                                                                          | dependência externa                                      | Sisprev / IPERON / fornecedor                                | resposta institucional a Q6-S/Q6-T (fila de perguntas, §9 do dossiê Q6)                                                                                                                                                                                   | confirmação escrita do IPERON/fornecedor                                                                                                                                 | implantação           | **dependência externa**                            | não afeta cobertura do catálogo (spec/ciclo.md admite dependência externa registrada)                                                                                          |
| C1-R74  | C1-R70         | O rótulo de `tipo_calculo` identifica univocamente a fórmula que a regra descreve  | `okf/spec/tipocalculo.md`; `achado-0061`; issue #124                                                       | Todas as 40 (crítico para as 2 de causa comum — C1-R32)                | `projecao.tipo_calculo`                                                                                              | dependência externa                                      | IPERON / fornecedor                                          | confirmação de que o Sisprev executa uma rotina distinta para cada fórmula que hoje compartilha rótulo, ou que outro campo já desambigua                                                                                                                  | confirmação escrita do IPERON/fornecedor                                                                                                                                 | implantação           | **dependência externa**                            | premissa geral do catálogo; `achado-0061` documenta a colisão como fato do catálogo, sem presumir erro de produção; bloqueia `deployable` onde a colisão for material (C1-R32) |
| C1-R75  | C1-R70, C1-R22 | Protocolo institucional de reconhecimento do nexo de moléstia profissional         | RFC 0004 §7/§14 (P-6 — lacuna normativa: nenhum dos dois regimes estaduais define "moléstia profissional") | 2 regras `*-molestia-profissional.md`                                  | fundamentação (protocolo genérico já descrito; nexo específico não definido)                                         | dependência externa                                      | IPERON / coordenação                                         | definição institucional do protocolo de reconhecimento do nexo                                                                                                                                                                                            | ato normativo ou administrativo que defina o protocolo                                                                                                                   | implantação           | **dependência externa**                            | não força `preview`: o caminho de verificação genérico (junta + instrução) já está definido nas duas regras; ver seção 7                                                       |

## 6. Matriz de cobertura por classe/regra

Uma linha por causa/moléstia. Cada linha cobre as duas regras da coorte
(até 2003 e a partir de 2004), que diferem apenas em datas, `paridade` e,
quando aplicável, nas ressalvas do § 16.

| Causa/moléstia                 | Inciso | Dispositivo           | Regra até 2003                                                       | Regra a partir de 2004                                                | IDs da matriz aplicáveis                                                         | `estado_proposta`       | Status                                         |
| ------------------------------ | ------ | --------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ----------------------- | ---------------------------------------------- |
| Acidente em serviço            | —      | art. 30, § 5º         | `incapacidade-lce1100-ate-2003-acidente-em-servico`                  | `incapacidade-lce1100-apos-2003-acidente-em-servico`                  | C1-R00,R10,R11/12,R13,R20,R21,R30,R31,R40,R41,R50,R51/52,R60,R61,R70,R71,R73,R74 | deployable / deployable | coberto, com dependências externas registradas |
| Moléstia profissional          | —      | art. 30, caput        | `incapacidade-lce1100-ate-2003-molestia-profissional`                | `incapacidade-lce1100-apos-2003-molestia-profissional`                | (idem) + R22, R75 no lugar de R21                                                | deployable / deployable | coberto, com risco anotado (C1-R75)            |
| Tuberculose ativa              | I      | art-30-par-8-inc-i    | `incapacidade-lce1100-ate-2003-doenca-tuberculose-ativa`             | `incapacidade-lce1100-apos-2003-doenca-tuberculose-ativa`             | R20,R23,R23a,R23b + comuns                                                       | deployable / deployable | coberto                                        |
| Hanseníase                     | II     | art-30-par-8-inc-ii   | `incapacidade-lce1100-ate-2003-doenca-hanseniase`                    | `incapacidade-lce1100-apos-2003-doenca-hanseniase`                    | idem                                                                             | deployable / deployable | coberto                                        |
| Alienação mental               | III    | art-30-par-8-inc-iii  | `incapacidade-lce1100-ate-2003-doenca-alienacao-mental`              | `incapacidade-lce1100-apos-2003-doenca-alienacao-mental`              | idem                                                                             | deployable / deployable | coberto                                        |
| Neoplasia maligna              | IV     | art-30-par-8-inc-iv   | `incapacidade-lce1100-ate-2003-doenca-neoplasia-maligna`             | `incapacidade-lce1100-apos-2003-doenca-neoplasia-maligna`             | idem                                                                             | deployable / deployable | coberto                                        |
| Cegueira bilateral             | V      | art-30-par-8-inc-v    | `incapacidade-lce1100-ate-2003-doenca-cegueira-bilateral`            | `incapacidade-lce1100-apos-2003-doenca-cegueira-bilateral`            | idem                                                                             | deployable / deployable | coberto                                        |
| Paralisia irreversível         | VI     | art-30-par-8-inc-vi   | `incapacidade-lce1100-ate-2003-doenca-paralisia-irreversivel`        | `incapacidade-lce1100-apos-2003-doenca-paralisia-irreversivel`        | idem                                                                             | deployable / deployable | coberto                                        |
| Cardiopatia grave              | VII    | art-30-par-8-inc-vii  | `incapacidade-lce1100-ate-2003-doenca-cardiopatia-grave`             | `incapacidade-lce1100-apos-2003-doenca-cardiopatia-grave`             | idem                                                                             | deployable / deployable | coberto                                        |
| Doença de Parkinson            | VIII   | art-30-par-8-inc-viii | `incapacidade-lce1100-ate-2003-doenca-doenca-de-parkinson`           | `incapacidade-lce1100-apos-2003-doenca-doenca-de-parkinson`           | idem                                                                             | deployable / deployable | coberto                                        |
| Espondiloartrose anquilosante  | IX     | art-30-par-8-inc-ix   | `incapacidade-lce1100-ate-2003-doenca-espondiloartrose-anquilosante` | `incapacidade-lce1100-apos-2003-doenca-espondiloartrose-anquilosante` | idem                                                                             | deployable / deployable | coberto                                        |
| Nefropatia grave               | X      | art-30-par-8-inc-x    | `incapacidade-lce1100-ate-2003-doenca-nefropatia-grave`              | `incapacidade-lce1100-apos-2003-doenca-nefropatia-grave`              | idem                                                                             | deployable / deployable | coberto                                        |
| Doença de Paget                | XI     | art-30-par-8-inc-xi   | `incapacidade-lce1100-ate-2003-doenca-doenca-de-paget`               | `incapacidade-lce1100-apos-2003-doenca-doenca-de-paget`               | idem                                                                             | deployable / deployable | coberto                                        |
| SIDA/AIDS                      | XII    | art-30-par-8-inc-xii  | `incapacidade-lce1100-ate-2003-doenca-sida-aids`                     | `incapacidade-lce1100-apos-2003-doenca-sida-aids`                     | idem                                                                             | deployable / deployable | coberto                                        |
| Contaminação por radiação      | XIII   | art-30-par-8-inc-xiii | `incapacidade-lce1100-ate-2003-doenca-contaminacao-por-radiacao`     | `incapacidade-lce1100-apos-2003-doenca-contaminacao-por-radiacao`     | idem                                                                             | deployable / deployable | coberto                                        |
| Hepatopatia grave              | XIV    | art-30-par-8-inc-xiv  | `incapacidade-lce1100-ate-2003-doenca-hepatopatia-grave`             | `incapacidade-lce1100-apos-2003-doenca-hepatopatia-grave`             | idem                                                                             | deployable / deployable | coberto                                        |
| Esclerose múltipla             | XV     | art-30-par-8-inc-xv   | `incapacidade-lce1100-ate-2003-doenca-esclerose-multipla`            | `incapacidade-lce1100-apos-2003-doenca-esclerose-multipla`            | idem                                                                             | deployable / deployable | coberto                                        |
| Surdez permanente (magistério) | XVI    | art-30-par-8-inc-xvi  | `incapacidade-lce1100-ate-2003-doenca-surdez-permanente-magisterio`  | `incapacidade-lce1100-apos-2003-doenca-surdez-permanente-magisterio`  | R20,R23,R23a,R23b,**R24** + comuns                                               | deployable / deployable | **pendente (C1-R24)**                          |
| Anomalia da fala (magistério)  | XVI    | art-30-par-8-inc-xvi  | `incapacidade-lce1100-ate-2003-doenca-anomalia-da-fala-magisterio`   | `incapacidade-lce1100-apos-2003-doenca-anomalia-da-fala-magisterio`   | R20,R23,R23a,R23b,**R24** + comuns                                               | deployable / deployable | **pendente (C1-R24)**                          |
| Causa comum                    | —      | art. 30, caput e § 14 | `incapacidade-lce1100-ate-2003-causa-comum`                          | `incapacidade-lce1100-apos-2003-causa-comum`                          | R20,R25,R30,**R32**,R42 + comuns                                                 | **preview / preview**   | **pendente (C1-R32)**                          |

"IDs da matriz aplicáveis — idem" e "+ comuns" referem-se ao conjunto que
toda regra do Bloco C compartilha: `C1-R00, C1-R10, C1-R11` ou `C1-R12`
(conforme a coorte), `C1-R13, C1-R30, C1-R31, C1-R40, C1-R41, C1-R50, C1-R51`
ou `C1-R52` (conforme a coorte), `C1-R60/C1-R61` (só na coorte até 2003),
`C1-R70, C1-R71, C1-R73, C1-R74`.

**Verificação de completude desta seção** (executada nesta revisão,
programaticamente): as 40 regras do diretório
`okf/regras-propostas/regras/incapacidade-lce1100-*.md` aparecem todas
nesta tabela, uma vez cada; nenhuma linha desta tabela referencia arquivo
inexistente; todos os 16 incisos do art. 30, § 8º, têm moléstia
correspondente citada corretamente contra o texto do dispositivo.

## 7. Pendências reais

| Requisito                                                                                                                                                            | Classificação                                               | Linhas afetadas                       | Issue      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------- | ---------- |
| Marco temporal do requisito de magistério                                                                                                                            | pendência jurídica da coordenação                           | C1-R24 (4 regras)                     | #121       |
| Colisão de `tipo_calculo` entre a fórmula da LCE 1.100 e outras duas fórmulas sob o mesmo rótulo (`achado-0061`); confirmação de tipo discriminante ou desambiguação | achado + dependência de implantação (bloqueia `deployable`) | C1-R32 (2 regras)                     | #122, #124 |
| Captura e classificação da causa pelo Sisprev (Q6-S/Q6-T)                                                                                                            | dependência externa                                         | C1-R73 (40 regras)                    | #124       |
| Confirmação operacional geral de `tipo_calculo`                                                                                                                      | dependência externa                                         | C1-R74 (40 regras, crítica em C1-R32) | #124       |
| Protocolo institucional de reconhecimento do nexo de moléstia profissional                                                                                           | dependência externa (lacuna normativa, RFC 0004 P-6)        | C1-R75 (2 regras)                     | #124       |
| Opção do § 16 sem campo próprio no cadastro                                                                                                                          | risco residual, não impede a cobertura                      | C1-R61 (20 regras)                    | #124       |

Nenhuma destas é renomeada como resolvida por constar desta matriz. A
matriz classifica; não decide questão jurídica, e não substitui a
confirmação institucional que cada dependência externa aguarda.

**Sobre C1-R32 especificamente.** `achado-0061` registra que oito regras
legadas — não só as duas de causa comum deste ciclo — gravam `tipo_calculo: Proporcionalidade Dias` para quatro tipos de benefício diferentes
(incapacidade permanente, invalidez, compulsória, por idade). A auditoria
trabalha com a presunção de que valores iguais indicam a mesma rotina, salvo
evidência em contrário — mas a própria amplitude da colisão torna plausível
que o Sisprev desambigue por outro campo (`tipo_de_beneficio`, por exemplo),
o que tornaria a colisão inofensiva. Nenhuma das duas hipóteses está
confirmada. O achado não afirma erro de cálculo em produção; afirma a
colisão documental e propõe a correção funcional — um tipo de cálculo (ou
combinação de parâmetros) que identifique univocamente a fórmula da LCE
1.100 — deixando a via de implantação (novo valor, nova rotina, ou prova de
desambiguação já existente) a critério do IPERON/fornecedor. Enquanto isso
não ocorre, as duas regras de causa comum e os dois grupos do Bloco C
permanecem, respectivamente, `preview` e `inativo`.

**Sobre C1-R75 especificamente.** A classificação como dependência externa,
e não como pendência jurídica da coordenação, é uma escolha deliberada:
RFC 0004 (§7, §14) registra que nenhum dos dois regimes estaduais lidos
define "moléstia profissional", e cita esse caso como exemplo do que
bloquearia a compilação `deployable` por proveniência ausente. As duas
regras deste ciclo, porém, já têm caminho de verificação definido —
responsável (junta médica e instrução previdenciária do IPERON), meio de
prova (histórico ocupacional, prontuários, exames, apuração administrativa)
e evidência exigida —, herdado da prática já vigente para "acidente em
serviço" e "doença catalogada". O que falta não é caminho de verificação; é
**definição institucional do protocolo específico de nexo profissional**,
que continua sendo instrução do caso concreto até que o IPERON o publique.
Por isso as duas regras permanecem `deployable`, e a lacuna fica registrada
como dependência externa vinculada à issue #124, não como defeito das
regras. Se a coordenação entender que a ausência desse protocolo é mais
grave do que aqui se avalia, o caminho é recuar as duas regras a `preview`
citando esta linha — decisão que esta matriz não toma sozinha.

## 8. Conclusão

A matriz cobre os setenta requisitos derivados que as quarenta regras do
Bloco C instanciam, com fonte, regras alcançadas, representação, modo de
verificação, responsável, evidência e status para cada um. Vinte e um
requisitos estão listados na seção 5; vinte linhas de cobertura por
causa/moléstia detalham como eles se aplicam às quarenta regras na seção 6.

**O Ciclo 1 não está encerrado.** Dois requisitos específicos permanecem
pendentes de decisão da coordenação ou de confirmação externa antes que a
condição 9 de `okf/spec/ciclo.md` se demonstre para o Bloco C inteiro:

- **C1-R24** — o marco temporal do requisito de magistério, nas quatro
  regras do inciso XVI. É pendência jurídica: a lei não o fixa, e inventá-lo
  sem fonte seria decisão nova não demonstrada;
- **C1-R32** — `achado-0061` documenta que `Proporcionalidade Dias` grava,
  no catálogo, três fórmulas juridicamente distintas e quatro tipos de
  benefício, sem mecanismo de desambiguação confirmado. É achado mais
  dependência de implantação: bloqueia `deployable` por RFC 0004 §5.3
  enquanto não houver tipo discriminante implantado ou prova de
  desambiguação por outro campo, e por isso essas duas regras e os dois
  grupos de substituição do Bloco C permanecem, respectivamente, `preview` e
  `estado_grupo: inativo`.

Três dependências externas adicionais (C1-R73, C1-R74, C1-R75) permanecem
registradas sem bloquear a cobertura do catálogo, conforme
`okf/spec/ciclo.md` admite. Nenhuma das trinta e oito regras restantes tem
pendência material aberta: a correspondência entre causa, dispositivo,
datas e projeção de cálculo foi verificada programaticamente contra a
matriz desta seção, e o caminho de verificação não programática de cada uma
está definido, com responsável e evidência — o que resta é a constatação no
caso concreto, que é trabalho do processo administrativo, não defeito da
regra.

## 9. Rastreabilidade

| item                               | referência                                                        |
| ---------------------------------- | ----------------------------------------------------------------- |
| ciclo auditado                     | `okf/regras-sisprev/ciclos/ciclo-01.md`                           |
| critério de encerramento           | `okf/spec/ciclo.md`                                               |
| contrato do schema enriquecido     | `docs/rfc/0004-schema-enriquecido-e-compilador-para-o-sisprev.md` |
| grupos de substituição             | `okf/conjuntos/ciclo-01-s4-bloco-c.md`                            |
| regras propostas                   | `okf/regras-propostas/regras/incapacidade-lce1100-*.md`           |
| dossiê da causa (Q6)               | `docs/analysis/q6-causa-incapacidade.md`                          |
| confirmações do fornecedor         | `docs/analysis/confirmacoes-do-fornecedor-do-sisprev.md`          |
| relatório de conformidade          | `docs/analysis/conformidade-ciclo-01.md`                          |
| colisão de `tipo_calculo` (C1-R32) | `okf/regras-sisprev/achados/achado-0061.md`                       |
| issues relacionadas                | #121, #122, #123, #124                                            |
