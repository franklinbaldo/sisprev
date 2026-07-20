---
type: Achado
id: achado-0009
nome: 'Pendência de Preenchimento: Regras Integrais Sem Fundamentação Proporcional Preenchida'
situacao: aberto
severidade: informativo
verificacao: mecanica
natureza: dados
regras_afetadas:
  - /regras/regra-0002.md
  - /regras/regra-0014.md
  - /regras/regra-0015.md
  - /regras/regra-0016.md
  - /regras/regra-0017.md
  - /regras/regra-0018.md
  - /regras/regra-0020.md
  - /regras/regra-0021.md
  - /regras/regra-0033.md
  - /regras/regra-0034.md
  - /regras/regra-0039.md
  - /regras/regra-0040.md
  - /regras/regra-0057.md
  - /regras/regra-0107.md
  - /regras/regra-0108.md
  - /regras/regra-0109.md
  - /regras/regra-0110.md
detectado_em: '2026-07-18'
detectado_por: AI
deteccoes:
  - detector: P9_INTEGRAL_SEM_FUNDAMENTACAO
    fingerprint: sha256:18612a90e006d38f57c89e8e921c8172cb630baa2553039da9ea4285a3fba1c5
  - detector: P9_INTEGRAL_SEM_FUNDAMENTACAO
    fingerprint: sha256:1e0c5aecf8196b64d60c3260fe1c2b69d7f4406b6355afda9b540d70c6b15c9a
  - detector: P9_INTEGRAL_SEM_FUNDAMENTACAO
    fingerprint: sha256:ebc3abba4a2e9e0d5c836385994815c8329084496fd245de538d5ee878c0ed32
  - detector: P9_INTEGRAL_SEM_FUNDAMENTACAO
    fingerprint: sha256:a17399f20c8d434f63189e031f7ace4faff38ee72b8ef3c45f1ad3139fe7329d
  - detector: P9_INTEGRAL_SEM_FUNDAMENTACAO
    fingerprint: sha256:a12bd411c4b25566b8a189f8c379d0c1561b9b08572a581f17610fd5b6fbd594
  - detector: P9_INTEGRAL_SEM_FUNDAMENTACAO
    fingerprint: sha256:6c4fe51b2817a64eb9ea22ff0bb888151fe6522d9365db10cfcdb3c6de683cc5
  - detector: P9_INTEGRAL_SEM_FUNDAMENTACAO
    fingerprint: sha256:a89961b49e1ecdc864f161bba9dcf9ed647ba534d534bda8947ff4c4133dda53
  - detector: P9_INTEGRAL_SEM_FUNDAMENTACAO
    fingerprint: sha256:2a1cd514b489205b5d277f563a50c45132fddc5d7ed9cf274575515e8973cf9d
  - detector: P9_INTEGRAL_SEM_FUNDAMENTACAO
    fingerprint: sha256:8f4bf8e1532dc64c782ade86a7ec4eec7015c5ef7c17b3acb8f94ed243c902ba
  - detector: P9_INTEGRAL_SEM_FUNDAMENTACAO
    fingerprint: sha256:6334503276ffe932de14fde70781f84bd07682cd4bc04d1473a97fbdd39ec350
  - detector: P9_INTEGRAL_SEM_FUNDAMENTACAO
    fingerprint: sha256:2603fc2f8850c5c689bbaa2dbd52f16e7989043fea1728f479bcb14205c25ca9
  - detector: P9_INTEGRAL_SEM_FUNDAMENTACAO
    fingerprint: sha256:08d6a9d24b8c3ad73f42cfd9d4da31fbdc513f64e7abe38d85ecd1a6c08b7d0d
  - detector: P9_INTEGRAL_SEM_FUNDAMENTACAO
    fingerprint: sha256:601547f68aed5ddd39aff5a1f0228ebd2e963f815e31d9f2edc5b19f1b1e7751
  - detector: P9_INTEGRAL_SEM_FUNDAMENTACAO
    fingerprint: sha256:3b503b5f9a90b30c46791a2aa265cdb6deb7e41682d3ba88b05112cccfff942e
  - detector: P9_INTEGRAL_SEM_FUNDAMENTACAO
    fingerprint: sha256:be51ab3f8f20c9ff8afffaac439f7376652a2d77cd5f575c4fd392e023d228be
  - detector: P9_INTEGRAL_SEM_FUNDAMENTACAO
    fingerprint: sha256:d81e6a360713390bbdb84a8efc7a690814b2b2bb27d330689b4afdd3c42c8be8
  - detector: P9_INTEGRAL_SEM_FUNDAMENTACAO
    fingerprint: sha256:bf66415f8b718bbea80b312d0eaddf288e23d42091ca5b971195ed7e39fc47da
---

# Descrição

As regras citadas estão configuradas com o campo `integral` = N (ou seja, presumivelmente são regras de aposentadoria/pensão com cálculo proporcional ou semelhante), porém o campo `fundamentacao_proporcional` (frontmatter) está vazio.

# Evidências

A detecção `P9_INTEGRAL_SEM_FUNDAMENTACAO` registrou a ausência de conteúdo no campo `fundamentacao_proporcional` para as regras listadas, que declaram `integral: N`.

# Questão a investigar

Avaliar se a ausência da fundamentação proporcional é um lapso no cadastramento original (e preencher o texto legal que baseia o cálculo proporcional) ou se o próprio campo `integral` está marcado incorretamente como 'N'.
