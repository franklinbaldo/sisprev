---
paths:
  - "okf/regras-sisprev/**"
  - "okf/regras-propostas/**"
---

# Catálogo de regras (legado e proposto)

- **Vínculo em `dispositivos:` e `taxonomias:` exige conferência
  substantiva.** Localizar a referência pode ser mecânico; gravar o vínculo
  não é — o texto legal precisa ser lido e cotejado com o fundamento que a
  regra invoca. O extrator que gravava por correspondência textual produziu
  nove atribuições erradas (`C/C` lido como inciso, dígitos de data lidos
  como artigo, emenda estadual doando artigos à Constituição federal), todas
  parecendo citação bem formada; a saída congelada dele virou lista de
  trabalho em `docs/analysis/pendencias-de-citacao-congeladas.md`.
- **Achado registra a acusação com sua base.** Fonte, premissa e o que
  distingue fato constatado de inferência vão no próprio `achado-NNNN.md`,
  com autoria real e data (`okf/spec/achado.md`). Um detector fornece a
  ocorrência; a qualificação jurídica dela é análise, e é ela que o achado
  documenta.
- **Achado que chegou a `main` é permanente.** O errado se marca
  `situacao: improcedente`, com justificativa; o CI confere contra o
  merge-base. Achado criado e removido dentro da mesma PR ainda em aberto
  pode sair da árvore sem cerimônia.
- **Quem dispõe de um achado é a regra que ele nomeia**, em
  `disposicao_de_achados`, com justificativa — detector que parou de acusar
  não fecha achado.
- **Decisão editorial vai em `decisoes:`** — data, quem, o quê — no
  frontmatter da unidade afetada.
