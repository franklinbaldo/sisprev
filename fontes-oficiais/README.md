# `fontes-oficiais/` — arquivo local das publicações oficiais

Cópia local do que as URLs em `fontes:` servem. Existe para que conferir uma
transcrição **não dependa da rede** — e para que ela seja reproduzível.

Não é um bundle OKF. Não tem frontmatter, não tem `type:`, nada aqui é um
documento de conceito, e nenhum arquivo daqui vira `type: Dispositivo`
automaticamente. A decomposição de uma norma em dispositivos continua sob
demanda e autoral ([`docs/spec/dispositivo.md`](../docs/spec/dispositivo.md)):
ter a norma inteira em disco é o **oposto** de fragmentá-la preventivamente —
é ter o todo à mão para poder recortar dele com a lei aberta na frente.

## Por que isto existe

Na sessão que criou este diretório, o Planalto ficou fora do ar por horas —
primeiro HTTP 503, depois timeout sem sequer devolver status. Duas
transcrições precisaram ser feitas contra a publicação original da Câmara
porque a fonte primária estava inalcançável.

O risco não é o inconveniente. É que **um agente sem a fonte à mão é um agente
tentado a escrever texto legal de memória** — precisamente o modo de falha que
a [RFC 0008](../docs/rfc/0008-a-fundamentacao-e-articulacao.md) baniu ao
remover o leitor de citações por regex. Ter o arquivo local remove a tentação:
a resposta certa para "não consegui buscar" passa a ser `grep`, não lembrança.

O segundo motivo é probatório. Uma transcrição conferida "contra o Planalto em
2026-07" é inauditável depois que o site muda. Conferida contra
`fontes-oficiais/arquivos/<X>` com `sha256` no manifesto, é verificável para sempre.

## Como usar

```bash
# baixa o que falta (idempotente — não rebaixa o que já está aqui)
uv run python scripts/arquivo_de_fontes.py

# confere que nenhum arquivo mudou desde que foi capturado, sem tocar na rede
uv run python scripts/arquivo_de_fontes.py --verificar
```

Ao conferir um dispositivo, prefira o `.txt` — um PDF não se grepa:

```bash
grep -n -A4 'Art\. 39' fontes-oficiais/arquivos/ditel-LC432-COMPILADA-REVOGADA.txt
```

## O que tem aqui

- `arquivos/` — o conteúdo como veio, sem edição. **Nunca editado à mão**: um
  arquivo alterado deixa de bater com o `sha256` e perde o valor de prova, que
  é a única razão de ele estar aqui.
- `manifesto.yaml` — uma entrada por URL, com `sha256`, tamanho, data de
  captura e as normas que a citam. Indexado por **URL**, não por norma: a EC
  20/1998 é fonte de `cf88` e de `ec-20-1998`, a LC 949/2017 é fonte de
  `lce-432-2008` e de `lce-949-2017`. Guardar por norma duplicaria bytes e
  deixaria as cópias divergirem.

## Duas ausências que o manifesto registra de propósito

Um manifesto que listasse só o que deu certo seria lido como cobertura
completa — e é assim que alguém conclui "a norma não trata disso" a partir de
um `grep` num arquivo que nunca foi baixado. Então:

- **`faltando:`** lista cada URL que não baixou, com o motivo. Rode o script de
  novo quando a fonte voltar.
- **`texto: null` + `observacao`** marca PDF que é digitalização, sem camada de
  texto. O caso real é a **ECE 146/2021**: 4,8 MB de imagem, 10 caracteres
  extraíveis. Justo a norma do prazo de 31/12/2024 (art. 4º) e do corte das
  policiais (art. 7º) — os dois padrões sistêmicos mais citados na auditoria.
  Ali a conferência exige leitura visual do PDF; `grep` vazio não é prova de
  ausência.
