# Brief para quem tem acesso ao Planalto

Este arquivo existe porque o `planalto.gov.br` esteve inalcançável deste
ambiente durante toda a sessão de 2026-07-29 — primeiro HTTP 503, depois
timeout sem sequer devolver status. Doze documentos de dispositivo ficaram sem
migrar por causa disso.

Se você tem acesso, o que está pedido aqui destrava trabalho concreto. Leia a
seção "Como devolver" antes de começar: **a forma importa tanto quanto o
conteúdo**, e uma coleta bem-intencionada mas resumida não serve.

## O que se pede, em ordem de valor

### 1. LC 51/1985 e LC 144/2014 — a mais importante

```
https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp51.htm
https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp144.htm
```

Destrava 4 documentos (`lc-51-1985/art-1*/lc-144-2014`) e, mais que isso,
toca o item mais grave do catálogo: `regra-0078` tem `sexo: MASCULINO` e cita
a alínea **"b"** do art. 1º, II — que é a feminina (25 anos de contribuição,
15 de exercício policial, "se mulher"), enquanto a alínea "a" é a masculina
(30 e 20). `regra-0084` repete o padrão com `sexo: AMBOS`, e não tem detector
nem achado.

**A pergunta que só a fonte responde:** qual é o texto exato das alíneas "a" e
"b" do art. 1º, II na redação dada pela **LC 144/2014**, e desde quando ela
vige. O repositório tem essas alíneas transcritas, mas sem janela declarada —
então nem se confirma nem se refuta que a citação da `0078` está errada *na
redação vigente à época do requerimento*.

### 2. Lei 10.887/2004 e LC 152/2015

```
https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/lei/l10.887.htm
https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp152.htm
```

Um documento cada. A LC 152/2015 é a que fixou os 75 anos da compulsória a
partir de 04/12/2015 e aparece na conferência de `regra-0030`/`0031`; a Lei
10.887/2004 é citada pelas regras de compulsória.

### 3. As emendas constitucionais

```
https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc20.htm
https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc41.htm
https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc47.htm
https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc70.htm
https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc88.htm
https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc103.htm
https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm
```

Destrava 6 documentos (`ec-20-1998/art-8`, `ec-41-2003/art-2|art-6|art-7`,
`ec-47-2005/art-3` e `art-3-par-unico`).

**Atenção — aqui o pedido é específico e é o ponto do brief inteiro.** Já
temos as *publicações originais* dessas emendas, baixadas da Câmara
(`www2.camara.leg.br/legin/...`). O que falta **não** é o texto: é a versão
**compilada**, com as notas inline do tipo `(Revogado pela Emenda Constitucional nº X)` e `(Redação dada pela...)`.

A razão é direta: esses 6 documentos não migraram porque migrar exige afirmar
o **fim** da vigência, e "sem `vigencia_fim`" quer dizer "ainda em vigor" —
afirmação que ninguém pode fazer de memória. As notas do texto compilado do
Planalto respondem isso diretamente; a publicação original, por definição, não
traz alteração posterior nenhuma.

O caso mais concreto: o art. 35 da EC 103/2019 revoga dispositivos das EC 41 e
EC 47, mas o art. 36, II condiciona o efeito, nos RPPS estaduais, à publicação
de lei estadual de referendo. Saber se e quando o art. 2º, o art. 6º da EC 41 e
o art. 3º da EC 47 deixaram de valer em Rondônia é **conclusão jurídica**, não
coleta — mas o texto compilado é a base mínima para tomá-la.

### 4. Fora do Planalto, se puder: ECE 146/2021 com camada de texto

O PDF que temos (`sapl-emenda_146.pdf`, da ALE-RO) é digitalização pura: 4,8 MB
de imagem, 10 caracteres extraíveis. É a norma do prazo de **31/12/2024** (art.
4º) e do corte de ingresso das policiais (art. 7º) — os dois padrões mais
repetidos da auditoria, hoje impossíveis de conferir por `grep`.

Serve qualquer versão com texto selecionável: Diário Oficial do Estado, outra
publicação da ALE-RO, ou o PDF atual passado por OCR (dizendo que foi OCR).

## Como devolver

**Prefira os bytes crus.** O repositório tem o coletor pronto:

```bash
uv run python scripts/arquivo_de_fontes.py            # baixa o que falta
uv run python scripts/arquivo_de_fontes.py --verificar # reconfere hashes, sem rede
```

Se você conseguir rodar isso de um ambiente com acesso, é o caminho completo:
ele grava em `fontes-oficiais/arquivos/`, calcula `sha256`, extrai `.txt` dos
PDFs e atualiza `fontes-oficiais/manifesto.yaml`, movendo as URLs de
`faltando:` para `arquivos:`. Commite o resultado e acabou.

Se não puder rodar o script, entregue os arquivos HTML/PDF **como vieram**,
com a URL de origem de cada um. Eu rodo o resto.

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
- **Não substitua uma fonte por outra sem dizer.** Se pegar a EC 41 na Câmara
  em vez do Planalto, isso muda o que o documento prova (publicação original
  vs. texto compilado) — e é justamente a distinção que motiva o item 3.
- **Não edite `regra-*.md`, achados nem documentos de dispositivo.** A coleta
  é insumo; a transcrição e a conferência são atos autorais separados.

## Como eu vou conferir o que você trouxer

Não é desconfiança, é o contrato do arquivo: `--verificar` recalcula o
`sha256` de cada arquivo contra o manifesto, e qualquer transcrição que eu
escrever depois é comparada literalmente contra o texto que você entregou.
Se um trecho não casar, ele não vira dispositivo — vira pergunta.

## O que este brief **não** destrava

Para não gerar expectativa errada: dos 18 documentos sem migrar, **6 não
dependem do Planalto**. São os da redação LCE 949/2017 em `lce-432-2008`, e
estão travados em outra coisa — duas fontes oficiais divergem sobre a data da
própria lei (SAPL diz 18/07/2017, DITEL diz 17/07/2017) e a cláusula de 180
dias do art. 3º admite duas contagens (LINDB art. 8º §1º daria 14/01/2018;
"após o 180º dia" daria 15/01/2018). Isso é decisão humana sobre norma
estadual, registrada em `okf/dispositivos/lce-949-2017/norma.md`. Nada no
Planalto ajuda.
