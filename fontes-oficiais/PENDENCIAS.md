# Fontes oficiais: o que já está arquivado e o que ainda falta

Este arquivo nasceu como pedido de socorro — o `planalto.gov.br` parecia fora
do ar e 12 documentos de dispositivo estavam sem migrar por causa disso. **O
diagnóstico estava errado, e a correção cabe em uma linha.** O registro fica
aqui porque o modo de falha é enganoso e vai reaparecer.

## O que era, de verdade

O Planalto **filtra o User-Agent padrão do `curl`**. A mesma URL que devolvia
`000` sem status responde **HTTP 200 em 0,36 s** com UA de navegador.

O sintoma imita indisponibilidade de forma convincente: o DNS resolve
(`170.246.255.9`), a conexão sai, o servidor aceita — e nada volta, até o
timeout. Sem comparar com outro host na mesma sessão, a leitura natural é
"site fora do ar". Foi o que aconteceu por uma sessão inteira. O que desfez a
dúvida foi medir `google.com` e `gov.br` nos mesmos segundos: ambos
respondendo, só o Planalto em silêncio — indisponibilidade real não escolhe
cliente.

`scripts/arquivo_de_fontes.py::_baixar` passa a enviar `-A <UA de navegador>`.
Não é evasão de bloqueio: o conteúdo é público e o acesso é idêntico ao de
qualquer navegador.

**Estado atual: `22 fonte(s) arquivada(s), 0 faltando`.**

## O que as fontes responderam

Conferido no texto baixado, não de memória. As três perguntas que travavam a
migração:

### LC 51/1985, art. 1º, II — redação da LC 144/2014

> **a)** após 30 (trinta) anos de contribuição, desde que conte, pelo menos,
> 20 (vinte) anos de exercício em cargo de natureza estritamente policial, **se
> homem**; *(Incluído pela Lei Complementar n° 144, de 2014)*
>
> **b)** após 25 (vinte e cinco) anos de contribuição, desde que conte, pelo
> menos, 15 (quinze) anos de exercício em cargo de natureza estritamente
> policial, **se mulher**. *(Incluído pela Lei Complementar n° 144, de 2014)*

É a fonte que faltava para o `achado-0017`, autorado em paralelo: as três
regras de policial citam só a alínea **"b"** — a feminina —, e a "a" não é
citada por regra nenhuma do catálogo. O achado é o registro da acusação; o que
a fonte acrescenta é que ambas as alíneas foram **incluídas** pela LC 144/2014,
com nota inline no compilado, então a citação está errada *na redação vigente*
— não apenas na leitura de hoje.

Segue autoral o que sempre foi: qual janela de vigência declarar ao transcrever
o dispositivo.

### EC 103/2019, art. 36, II — a condição estadual

O art. 35 revoga dispositivos das EC 41 e 47, mas o efeito nos RPPS estaduais
é condicionado: as revogações da **alínea "a" do inciso I** e dos **incisos
III e IV do art. 35** só valem a partir da publicação de lei de iniciativa
privativa do Executivo estadual **que as referende integralmente**, e o
parágrafo único veda efeito anterior a essa publicação.

Isto é a base mínima; se e quando o art. 2º e o art. 6º da EC 41 e o art. 3º
da EC 47 deixaram de valer em Rondônia continua sendo **conclusão jurídica**,
não coleta.

### EC 47/2005, art. 3º — uma assimetria a conferir

O compilado do Planalto para a EC 47 **não traz nota de revogação alguma**,
enquanto o da EC 41 traz 14. Vale conferir antes de afirmar `vigencia_fim`: a
ausência de nota não é o mesmo que vigência confirmada, e a diferença entre as
duas páginas pede explicação.

## O que ainda falta

### ECE 146/2021 com camada de texto — fora do Planalto

O PDF que temos (`sapl-emenda_146.pdf`, da ALE-RO) é digitalização pura: 4,8 MB
de imagem, 10 caracteres extraíveis. É a norma do prazo de **31/12/2024** (art.
4º) e do corte de ingresso das policiais (art. 7º) — os dois padrões mais
repetidos da auditoria, hoje impossíveis de conferir por `grep`.

Serve qualquer versão com texto selecionável: Diário Oficial do Estado, outra
publicação da ALE-RO, ou o PDF atual passado por OCR (dizendo que foi OCR).

## O que nada disso destrava

Dos 18 documentos sem migrar, **6 nunca dependeram do Planalto**. São os da
redação LCE 949/2017 em `lce-432-2008`, travados em outra coisa: duas fontes
oficiais divergem sobre a data da própria lei (SAPL diz 18/07/2017, DITEL diz
17/07/2017) e a cláusula de 180 dias do art. 3º admite duas contagens (LINDB
art. 8º §1º daria 14/01/2018; "após o 180º dia" daria 15/01/2018). Decisão
humana sobre norma estadual, registrada em
`okf/dispositivos/lce-949-2017/norma.md`.

## Como coletar, se precisar de outra fonte

```bash
uv run python scripts/arquivo_de_fontes.py            # baixa o que falta
uv run python scripts/arquivo_de_fontes.py --verificar # reconfere hashes, sem rede
```

O script grava em `fontes-oficiais/arquivos/`, calcula `sha256`, extrai `.txt`
dos PDFs e move as URLs de `faltando:` para `arquivos:`.

Se não puder rodá-lo, entregue os arquivos HTML/PDF **como vieram**, com a URL
de origem de cada um.

## O que não fazer

Estas travas não são formalidade — são o modo de falha que este repositório já
sofreu e documentou (RFC 0008, sobre a remoção do leitor de citações por
regex).

- **Não resuma, não parafraseie, não "limpe" o texto legal.** O valor do
  arquivo é ser byte-idêntico ao que a fonte oficial serve, para que uma
  transcrição possa ser conferida contra ele anos depois. Um resumo fiel é
  inútil aqui.
- **Não escreva o texto de memória**, mesmo que você o conheça bem. Se a
  fonte não abrir, diga que não abriu. **Recusar é a resposta preferida.**
- **Não deduza datas de vigência** a partir do número ou do ano da norma.
  Entregue o texto e deixe a data ser lida da cláusula de vigência dela.
- **Não substitua uma fonte por outra sem dizer.** A EC 41 na Câmara e no
  Planalto provam coisas diferentes (publicação original vs. texto compilado)
  — é justamente a distinção que travava os documentos constitucionais.
- **Não edite `regra-*.md`, achados nem documentos de dispositivo.** A coleta
  é insumo; a transcrição e a conferência são atos autorais separados.

## Como a coleta é conferida

`--verificar` recalcula o `sha256` de cada arquivo contra o manifesto, e
qualquer transcrição escrita depois é comparada literalmente contra o texto
arquivado. Se um trecho não casar, ele não vira dispositivo — vira pergunta.

Isso só passou a ser verdade em clone novo a partir do `.gitattributes` desta
mesma sessão: sem `-text`, o git normalizava CRLF→LF ao gravar e o arquivo que
saía de um clone **não era** o que fora baixado (9.825 bytes viravam 9.671). O
`--verificar` passava na máquina de quem baixou e falharia em qualquer outra.
