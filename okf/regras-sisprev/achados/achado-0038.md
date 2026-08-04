---
type: Achado
id: achado-0038
nome: O nome de regra-0111 e regra-0112 é o mesmo e nomeia a alínea masculina da LC 51/1985 — a regra-0112 é FEMININO
situacao: aberto
severidade: informativo
verificacao: manual
natureza: dados
regras_afetadas:
  - /regras/regra-0111.md
  - /regras/regra-0112.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

`regra-0111` e `regra-0112` têm **um só** `nome`, caractere a caractere:

> Voluntária do Policial Civil - Art. 1º, II, **"a"** da LC nº. 51/85 c/c LC
> nº. 144/14, c/c art. 4º da EC nº 146/2021

A alínea "a" do art. 1º, II da LC 51/1985 é a masculina — 30 anos de
contribuição e 20 de exercício policial, "**se homem**". `regra-0111` é
`sexo: MASCULINO` e `regra-0112` é `sexo: FEMININO`.

O rótulo da regra feminina nomeia, portanto, a provisão que a lei reserva ao
homem. E como o rótulo é **um só** para as duas, ele não pode estar certo nas
duas: a alínea é o que distingue o par, e o `nome` cita apenas uma.

# Evidências

O texto das duas alíneas foi conferido na publicação oficial compilada do
Planalto arquivada localmente (`fontes-oficiais/arquivos/planalto-lcp51.htm`,
cp1252): o inciso II tem exatamente duas alíneas, "a" *se homem* e "b" *se
mulher*, ambas incluídas pela LC 144/2014. A alínea feminina existe e é a "b".

O `nome` das duas é idêntico já em `data/raw/regras-sisprev.csv` — não é
resultado de edição de auditoria.

`dispositivos:` **não** repete o erro: `regra-0111` vincula
`lc-51-1985/art-1-inc-ii-al-a/lc-144-2014` e `regra-0112` vincula
`.../al-b/...`, cada uma a alínea do seu sexo. O defeito está no rótulo, e só
nele — o que significa que a informação certa existe no documento e o campo que
o usuário lê discorda dela.

O par aparece em `P1_NOME_REPETIDO`
(`sha256:d682cc022e3daef41d5f7e0d526e520c0bb40583c34278bef65db521fd6b4530`).
A detecção é informativa (`requires_achado: false`) e não é reivindicada aqui:
ela vê que o nome repete, nunca que a alínea nomeada é a do outro sexo — para
isso é preciso ler a lei. Por isso `verificacao: manual`.

# Relação com o que já está registrado

O `achado-0017` é o mesmo defeito **na fundamentação**: três regras de policial
citam só a alínea feminina, e em duas o `sexo` não é o dela. O
[`achado-0037`](achado-0037.md) é o mesmo defeito na mesma célula destas duas
regras, por empacotamento: lá as duas alíneas convivem em
`fundamentacao_integral`. Este achado é sobre o **`nome`**, e vale registrar por
que é problema separado: mesmo que a célula fosse partida em duas metades
corretas, o rótulo continuaria dizendo "a" para a regra feminina.

O `achado-0020` registra que o `nome` não tem padrão em 109 das 112 regras. Este
caso **não** é falta de padrão: é citação errada dentro do rótulo. Qualquer
padrão que se venha a adotar deixa este defeito de pé.

# Consequência prática

`nome` é a principal ferramenta de **seleção** da regra aplicável depois da
anamnese ([`okf/spec/regra.md`](../../../okf/spec/regra.md), "O papel do campo
`nome`"): é o que uma pessoa lê para escolher entre as candidatas. Aqui as duas
candidatas do par exibem a mesma linha, e a única marca discriminante que essa
linha carrega — a letra da alínea — aponta para o homem nas duas.

O efeito é pior do que o de um nome ambíguo. Um nome que não distingue faz
hesitar; um nome que distingue **errado** faz escolher com confiança. Quem
procura a regra da policial mulher lê "alínea a" e conclui que não é essa.

`NOME` é campo **deployável** e vai ao documento entregue. Corrigi-lo é
alterar o produto, não auditar o catálogo.

# Questão a investigar

1. **Se a correção é a letra ou o rótulo inteiro.** Trocar "a" por "b" na
   `regra-0112` fecha a incoerência e é parametrização de texto livre, dentro do
   escopo. Mas os dois nomes ficariam distintos **apenas** pela letra de uma
   alínea, e a spec registra explicitamente que isso continua sendo nome ruim
   ("dois nomes que diferem apenas pelo número de um artigo ou da norma
   continuam ruins, mesmo formalmente únicos"). O nome que a spec pede diria
   *homem* e *mulher*, não *a* e *b*.

2. **Se o par deve existir.** Aqui a resposta parece ser sim, e por motivo
   material: as alíneas exigem tempos diferentes (30/20 × 25/15), logo o
   critério aferido diverge e as regras não são idênticas. O defeito não é o par
   existir; é ele não ter chegado ao rótulo — a mesma conclusão do item 2 do
   `achado-0017`.

3. **Se `nome` pode carregar citação que a fundamentação não tem.** O `nome`
   destas duas cita o art. 4º da ECE 146/2021, que nenhum campo de fundamentação
   delas cita — questão registrada no
   [`achado-0039`](achado-0039.md) e, em outra forma, no item 3 do
   `achado-0047`. Enquanto ela estiver aberta, o `nome` é fonte parcial de
   fundamentação sem que nada no repositório o trate como tal.
