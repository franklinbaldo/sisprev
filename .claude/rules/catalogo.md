---
paths:
  - "okf/regras-sisprev/**"
  - "okf/regras-propostas/**"
---

# Catálogo de regras (legado e proposto)

- **Citação é vínculo autorado.** A entrada em `dispositivos:` (e as refs em
  `taxonomias:`) nasce de um humano que lê a fundamentação, confere contra a
  fonte e escreve o vínculo. O extrator automático que já existiu produziu
  nove atribuições erradas — `C/C` lido como inciso, dígitos de data lidos
  como artigo — todas parecendo citação bem formada; a saída congelada dele é
  lista de trabalho em
  `docs/analysis/pendencias-de-citacao-congeladas.md`.
- **Conclusão jurídica é achado autorado.** "Esta redação nunca existiu",
  "estas duas regras são a mesma" — conclusões assim vão escritas à mão num
  `achado-NNNN.md`, com autor e data, porque são acusações sobre campo que
  vai para produção. Detector aponta ocorrência mecânica; quem conclui é o
  auditor.
- **Achado em `main` é permanente.** O errado se marca
  `situacao: improcedente`, com justificativa (`okf/spec/achado.md`); o CI
  confere contra o merge-base. Achado criado e removido dentro da mesma PR
  ainda em aberto pode simplesmente sair da árvore.
- **Decisão editorial vai em `decisoes:`** — data, quem, o quê — no
  frontmatter da unidade que ela afeta.
