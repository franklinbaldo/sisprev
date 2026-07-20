# Relatório de Estado da Auditoria (Apoio à Decisão)

> **Nota:** Este é um relatório gerado por IA com o objetivo de apoiar a tomada de decisão (não é um artefato oficial de auditoria).

## 1. Distribuição de `status_auditoria` e Bloqueios

Todas as 112 regras do Sisprev estão atualmente com `status_auditoria: importada`. Para avançar uma regra para `revisada`, os seguintes critérios mecânicos e humanos (P7/P13.1) precisam ser atendidos:

- **Ausência de achados bloqueantes abertos** afetando a regra.
- **Ausência de detecções P1 e P2 não resolvidas**. Atualmente, muitas regras possuem detecções `P1_NOME_REPETIDO` (41 ocorrências sem achado vinculado) e 7 grupos de regras enfrentam detecções `P2_IGUALDADE_MATERIAL_ATIVA` (que já possuem achados abertos `achado-0001` a `achado-0007`).
- **Seções P13.1 obrigatórias não vazias** no corpo do markdown (Critérios avaliados pelo Sisprev, Requisitos de verificação manual, Documentos ou evidências necessários, Resultado após a seleção). Nenhuma regra atualmente possui essas seções preenchidas.
- **Dispositivos normativos** devem ser vinculados (a infraestrutura P3, `okf/dispositivos/`, já existe; o pendente é a vinculação sistemática das regras aos dispositivos).

## 2. Qualidade das Citações (campos `fundamentacao*`)

A auditoria mecânica (detectores P9) revela lacunas significativas nos campos de fundamentação e dados estruturais:

- **P9_CAMPOS_VAZIOS_PENDENTES**: 13 regras (`regra-0003` a `0005`, `0023` a `0026`, `0087` a `0092`) não identificam `sexo`, `integral` e/ou `tipo_calculo`. (Novo `achado-0008` criado).
- **P9_INTEGRAL_SEM_FUNDAMENTACAO**: 17 regras declaram explicitamente `integral: N`, porém deixam o campo `fundamentacao_proporcional` vazio. (Coberto pelo `achado-0009`).
- **P9_SEXO_FUNDAMENTACAO**: 1 regra (`regra-0078`) declara `sexo: MASCULINO`, mas cita explicitamente "mulher" na fundamentação. (Novo `achado-0010` criado para registrar a anomalia na fundamentação, pois o pareamento de gênero com regra-0079 indica um provável 'copy/paste' incorreto).

Além disso, muitos campos de fundamentação referenciam dispositivos legais em formato de texto livre (e.g., "Art. 40, inciso I da Constituição Federal de 1988") que ainda não estão vinculados aos arquivos canônicos de `okf/dispositivos/` — vários dos quais já existem (como `cf88/art-40-i-original.md`); o pendente é a vinculação via campo `dispositivos:`.

## 3. Panorama Mecânico (`validar_regras.py`)

A execução de `validar_regras.py --json` identificou 79 ocorrências (detections) que ativam os detectores:

- **P1_NOME_REPETIDO (41 ocorrências)**: Não possuem achados obrigatórios associados. Tratam-se na maioria de pensões ou aposentadorias que repetem o nome exato.
- **P2_IGUALDADE_MATERIAL_ATIVA (7 ocorrências)**: Grupos de regras cujos metadados e conteúdos são idênticos bit a bit. Já possuem achados abertos cobrindo-os (achados 0001 a 0007).
- \**P9\_* (31 ocorrências)\*\*: Relacionados a campos e preenchimento (descritos no item 2). Novos achados gerados para cobertura.

## 4. Opiniões e Próximos Passos Sugeridos

*Opinião 1: Desbloquear o avanço para `revisada` preenchendo as seções P13.1.*
A maior barreira sistêmica hoje é que nenhuma regra tem as 4 seções analíticas exigidas (Critérios, Requisitos manuais, Evidências, Resultados). Sugere-se eleger um pequeno lote de regras mais simples (ex: as constitucionais originais) para um preenchimento piloto destas seções.

*Opinião 2: Resolução de P1 e P2.*
Para que as regras possam progredir para `revisada`, as detecções ativas `P1` e `P2` devem ser tratadas. O caso `P2` (igualdade material) é o mais crítico porque causa confusão na seleção do benefício pelo usuário. Deve-se avaliar rapidamente os `achado-0001` a `0007` para inativar as duplicatas exatas se elas não possuírem contexto operacional oculto.

*Opinião 3: Vinculação Estrutural de Dispositivos.*
Vincular o texto livre da fundamentação para a sintaxe `dispositivos:` no YAML será um trabalho extenso. Recomenda-se começar pelas regras constitucionais (Art. 40), pois a pasta `cf88/` já contém alguns dispositivos base.
