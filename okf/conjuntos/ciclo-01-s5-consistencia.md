---
type: Conjunto
id: ciclo-01-s5-consistencia
nome: Ciclo 1 — S5 — consistência transversal de invalidez e incapacidade
situacao: proposto
base: ciclo-01-s4-bloco-c
---

# Função desta composição

Este conjunto não acrescenta nem retira unidades. Ele deriva de
`ciclo-01-s4-bloco-c` e registra os desempates, as formas de cálculo e as
dependências necessárias para ler os três blocos como catálogo coerente.

# Precedência entre o regime preservado e o permanente

Entre 18/10/2021 e 31/12/2024, primeiro se verifica se todos os requisitos e
critérios da legislação anterior foram cumpridos no prazo do art. 4º da ECE
146/2021. Se foram, aplicam-se unidade, cálculo e reajuste preservados do Bloco
B. O regime permanente do Bloco C somente é selecionado quando essa preservação
não incide e seus próprios requisitos estão preenchidos.

Não há escolha livre entre regimes. Depois de 31/12/2024 não nasce novo
enquadramento no art. 4º; direitos já formados continuam assegurados a qualquer
tempo.

# Matriz de compatibilidade

- Bloco A e Bloco B têm janelas contíguas, sem sobreposição.
- Bloco B e Bloco C têm interseção intencional resolvida pela precedência do art.
  4º.
- As quatro classes de causa são mutuamente excludentes; `causa_comum` exige
  exclusão probatória das qualificadas.
- As coortes até 31/12/2003 e desde 01/01/2004 são contínuas.

# Formas de cálculo

A S5 havia autorado três formas compostas. A reabertura do Bloco B completou a
linha temporal e refinou as unidades:

- remuneração integral do cargo sob a LC 228;
- remuneração do cargo proporcional por 1/35 ou 1/30 sob a LC 228;
- média federal de 80% desde 20/02/2004;
- média federal combinada com a fração anual da LC 228 até 12/03/2008;
- média limitada da LCE 432 proporcional em dias desde 13/03/2008;
- remuneração do cargo do art. 6º-A com fração anual ou em dias, conforme a
  legislação temporalmente aplicável; e
- média proporcional da LCE 1.100/2021 nas duas coortes do Bloco C.

Cálculo inicial e reajuste permanecem dimensões diferentes. Média proporcional e
paridade podem coexistir, como demonstra o art. 27, I, da LCE 1.100/2021.

# Pendências resolvidas

- precedência entre Blocos B e C;
- existência da combinação proporcional com paridade da antiga `regra-0020`;
- fórmulas materiais de toda a janela do Bloco B;
- redação original e limites do art. 45 da LCE 432;
- fórmula da LC 228 e marco inicial da média federal; e
- Q6-R para o catálogo auditado.

# Dependências localizadas

## Frações de ano na LC 228

A LC 228 fixa 1/35 ou 1/30 por ano de serviço, mas o corpus ainda não demonstra
como o IPERON trata períodos que não completam ano inteiro. A estrutura,
denominadores e piso estão fechados; falta apenas o procedimento administrativo
de contagem para simulação reproduzível.

## Q6-S e Q6-T

O repositório não contém tela, banco, solicitação, laudo real ou contrato de API
que demonstre onde o Sisprev obtém e registra a causa do requerente. Também não
contém protocolo institucional suficiente para caracterização de acidente,
nexo de moléstia profissional e vigência do rol de doenças.

A evidência necessária do IPERON é:

1. tela ou schema de entrada da causa;
2. modelo de laudo e responsável pela classificação;
3. procedimento de reconhecimento do acidente e do nexo profissional;
4. fonte versionada do rol e regra temporal; e
5. integração do fato apurado com a seleção da regra.

Enquanto essa evidência não existir, as unidades permanecem `simulavel: N`. A
dependência é operacional e de auditabilidade, não lacuna da matriz jurídica.

# Estado para S6

A cobertura jurídica e as fórmulas materiais estão fechadas. Antes de promover o
conjunto, S6 deve:

1. obter ou formalmente encaminhar o procedimento de frações de ano e Q6-S/Q6-T;
2. conferir os dispositivos e formas de cada unidade;
3. completar o gate humano;
4. registrar decisão de completude e ato institucional; e
5. executar todos os gates técnicos sobre a composição final.
