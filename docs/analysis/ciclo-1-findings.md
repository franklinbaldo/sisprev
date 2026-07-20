# Auditoria do 1º Ciclo de Validação — Findings (Apoio à Decisão)

> **Nota:** Relatório gerado por IA como apoio à decisão. **Não é artefato
> oficial de auditoria** e não autora achados nem edita regras. Todo item
> abaixo é observação ou pergunta a investigar contra a fonte real do
> Sisprev/legislação — nenhuma conclusão jurídica é presumida. Nenhum
> `regra-*.md` foi alterado para produzir este relatório.

Escopo: as **22 regras** com `ciclo_de_validacao: 1º` (regra-0001 a
regra-0022). Todas estão `validado_pge/presidencia: FALSE`.

## Sumário

| #   | Finding                                                                                            | Regras                                                | Tipo                         | Prioridade        |
| --- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | ---------------------------- | ----------------- |
| F1  | Duplicatas materiais exatas (mesma fundamentação e metadados)                                      | 0012≡0013; 0014≡0015                                  | igualdade material (P2-like) | alta              |
| F2  | `integral: N` mas corpo afirma "proventos integrais"                                               | 0021                                                  | flag × texto                 | alta              |
| F3  | Cobertura de sexo sobreposta: MASCULINO+FEMININO **e** AMBOS para a mesma regra                    | 0016+0017 vs 0018                                     | redundância                  | média             |
| F4  | Split integral/proporcional codificado só no flag `integral`, não na fundamentação                 | 0001/0002, 0006/0007, 0008/0009, 0019/0020, 0021/0022 | rastreabilidade              | média             |
| F5  | `tipo_calculo` "…70% do que exceder o Teto RGPS" (fórmula EC103) em regra pré-reforma com paridade | 0010, 0011                                            | cálculo × fundamento         | média             |
| F6  | Campos estruturais vazios (`sexo`/`integral`/`tipo_calculo`)                                       | 0003, 0004, 0005                                      | dados (já em achado-0008)    | baixa             |
| F7  | `dispositivos:` não vinculado em nenhuma regra, apesar de dispositivos já autorados                | todas (0001–0022)                                     | infraestrutura P3            | baixa (sistêmico) |
| F8  | Assimetria de seção `# Fundamentação` (geral) entre pares equivalentes                             | 0006 vs 0007                                          | consistência                 | baixa             |

______________________________________________________________________

## F1 — Duplicatas materiais exatas (prioridade alta)

Dois pares com **nome, fundamentação e todos os metadados idênticos** —
mesmo padrão dos achados P2 já abertos (0001–0007), mas ainda não cobertos:

- **regra-0012 ≡ regra-0013** — "Pensão Morte Art. 40, §7 da EC 41/2003 e
  Art.28 da LC 432/2008". Fundamentação Integral idêntica caractere a
  caractere; mesmos `paridade: N`, `sexo: AMBOS`, `integral: S`,
  `tipo_calculo`, mesmas datas.
- **regra-0014 ≡ regra-0015** — "Pensão por Morte - Art. 46 da Lei
  Complementar 1.100/2021". Idem: fundamentação e metadados idênticos.

**Questão a investigar:** cada par é uma duplicata a inativar, ou há
contexto operacional oculto (algum campo não-material que os distingue no
Sisprev) que justifica duas linhas? Se for duplicata pura, é candidato a
achado P2 + inativação de uma das cópias — decisão humana.

## F2 — `integral: N` mas fundamentação afirma "proventos integrais" (alta)

**regra-0021** tem `integral: N` e `tipo_calculo: Proporcionalidade Dias`,
mas as **três** hipóteses do corpo dizem, todas, *"proventos integrais
(cálculo por média)"*. O texto é idêntico ao da **regra-0022** (que é
`integral: S`). Ou o corpo da 0021 foi copiado da 0022 sem ajustar, ou o
flag `integral` está errado. Contradição interna a resolver contra a fonte.

## F3 — Cobertura de sexo sobreposta (média)

Para "Pensão por Morte - Art. 46 LC 1.100/2021 - Paridade", com
fundamentação idêntica:

- **regra-0016** — `sexo: MASCULINO`
- **regra-0017** — `sexo: FEMININO`
- **regra-0018** — `sexo: AMBOS`

`AMBOS` (0018) já subsume MASCULINO+FEMININO (0016+0017). Três linhas para o
que duas (ou uma) cobririam. Além disso, para **pensão por morte** o
benefício vai ao dependente — não é óbvio por que a regra se separa pelo
sexo *do instituidor*. **Questão:** a separação por sexo aqui tem efeito
real de cálculo/elegibilidade, ou é redundância de cadastramento?

## F4 — Split integral/proporcional só no flag, não na fundamentação (média)

Vários pares existem só para separar o caso de proventos integrais do
proporcional, mas a **fundamentação em prosa é idêntica** nos dois; o que
distingue é apenas o campo `integral` (e às vezes `tipo_calculo`):

- 0001 (`S`) / 0002 (`N`) — Invalidez anterior à EC 20, Art. 40, I original.
- 0006 (`S`) / 0007 (`N`) — Invalidez EC 41/2003.
- 0008 (`S`) / 0009 (`N`) — Invalidez 6º-A EC 41/2003 (mesmo `tipo_calculo`
  "Remuneração de Contribuição" nos dois — par ainda mais próximo).
- 0019 (`S`) / 0020 (`N`) — Incapacidade permanente EC 103/2019.
- 0021 (`N`) / 0022 (`S`) — Incapacidade permanente, ingresso após 2003.

Isto é *coerente* com o Art. 40, I (texto original), que dá proventos
integrais só nas causas taxativas — acidente em serviço, moléstia
profissional, doença grave/contagiosa/incurável — e proporcionais nos
demais. O ponto de auditoria é de **rastreabilidade**: a fundamentação não
diz a qual hipótese (integral vs proporcional) cada regra corresponde;
essa informação só vive no flag. Ao preencher as seções P13.1 / vincular
dispositivos, valeria a fundamentação de cada uma explicitar a hipótese.

## F5 — `tipo_calculo` pós-reforma em regra pré-reforma (média)

**regra-0010** e **regra-0011** são pensões com `paridade: S`, `integral: S`, direito adquirido a partir de 31/12/2003, fundadas no **Art. 6º-A da EC
41/03 (red. EC 70/12)** e **Art. 3º da EC 47/2005** — regimes *com
paridade*. Mas o `tipo_calculo` é *"Valor Efetivo mais 70% do que exceder o
Teto RGPS"*, que é a fórmula redutora de pensão da EC 103/2019.

Para **0012/0013** (que citam expressamente Art. 40, §7 EC 103/2019) esse
`tipo_calculo` é consistente. Para **0010/0011** (paridade, 6º-A/EC 47)
parece anacrônico. **Questão:** o `tipo_calculo` da 0010/0011 está correto,
ou herdou por engano a fórmula EC 103 das regras vizinhas?

## F6 — Campos estruturais vazios (baixa — já rastreado)

**regra-0003, 0004, 0005**: `sexo: ''`, `integral: ''`, `tipo_calculo: Não identificado`. Já cobertos pelo `achado-0008` (aberto/informativo). Sem
ação nova aqui além do que aquele achado já pede.

## F7 — `dispositivos:` vazio em todas as 22 (baixa, sistêmico)

Nenhuma das 22 regras popula o campo estrutural `dispositivos:`; a citação
legal vive só como texto livre no corpo. Vários dispositivos citados **já
estão autorados** em `okf/dispositivos/` e resolveriam de imediato, p.ex.:

- 0001/0002 → `cf88/art-40-i-original`
- 0003 → `cf88/art-40-p5-original` (**ainda não autorado** — só há
  `art-40-p5-ec103-2019`; o texto original do §5 precisaria ser criado)
- 0008/0009 → `ec-41-2003/art-6a-ec70-2012`
- 0011 → `ec-47-2005/art-3-unico`

Vincular é ato de autoria humana (RFC P3) — não fiz. Fica como a maior
frente mecânica-mas-verificável disponível para o ciclo. Observação: a
0003 citando o **§5 em texto original** revela que o bundle de dispositivos
ainda não tem esse dispositivo específico.

## F8 — Assimetria de seção geral entre pares equivalentes (baixa)

**regra-0007** tem `# Fundamentação` (geral) preenchida com *"Art. 20, §14º
e Art. 45 da LC 432/2008"*; sua par **regra-0006** (mesma fundamentação
integral/proporcional) tem a seção vazia. Se as duas modelam o mesmo
dispositivo diferindo só em integral/proporcional, a assimetria na seção
geral parece um lapso — conferir se o conteúdo cabe também na 0006.

______________________________________________________________________

## Sugestão de sequência (não-vinculante)

1. **F1 + F2** (alta): decidir sobre duplicatas 0012≡0013, 0014≡0015 e a
   contradição da 0021. São os itens com potencial de virar achado P2 /
   correção de flag.
2. **F3** (média): resolver a sobreposição de sexo 0016/0017/0018.
3. **F5** (média): confirmar `tipo_calculo` da 0010/0011.
4. **F7** (sistêmico): iniciar a vinculação `dispositivos:` pelas regras
   cujo dispositivo já existe (0001, 0002, 0008, 0009, 0011), e autorar o
   `cf88/art-40-p5-original` faltante para a 0003.
