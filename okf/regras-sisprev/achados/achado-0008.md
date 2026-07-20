---
type: Achado
id: achado-0008
nome: 'Pendência de Preenchimento: Regras Ativas com Campos Estruturais Vazios'
situacao: aberto
severidade: informativo
verificacao: mecanica
natureza: dados
regras_afetadas:
  - /regras/regra-0003.md
  - /regras/regra-0004.md
  - /regras/regra-0005.md
  - /regras/regra-0023.md
  - /regras/regra-0024.md
  - /regras/regra-0025.md
  - /regras/regra-0026.md
  - /regras/regra-0087.md
  - /regras/regra-0088.md
  - /regras/regra-0089.md
  - /regras/regra-0090.md
  - /regras/regra-0091.md
  - /regras/regra-0092.md
detectado_em: '2026-07-18'
detectado_por: AI
deteccoes:
  - detector: P9_CAMPOS_VAZIOS_PENDENTES
    fingerprint: sha256:3c9b12deadc2edf537222bf37433c0b3679621a93750dc8dd31c418a96d2149e
  - detector: P9_CAMPOS_VAZIOS_PENDENTES
    fingerprint: sha256:def8cfd7c4db510f3e3a6b94318e5d09c52e9ba07d05121701f41066937b55c9
  - detector: P9_CAMPOS_VAZIOS_PENDENTES
    fingerprint: sha256:88f84ca8993c593c323bfe1b90d27ec6bbc2e1dde7a6c664765c606506d99ec8
  - detector: P9_CAMPOS_VAZIOS_PENDENTES
    fingerprint: sha256:2aade7f2bcb4fcd6f8be522d8679483c2fb14fc1f246cbdefce7a8650b617199
  - detector: P9_CAMPOS_VAZIOS_PENDENTES
    fingerprint: sha256:8680580163a2728b608b0adb9abbefd1dff88bbae662babc8ecdec7d282804e1
  - detector: P9_CAMPOS_VAZIOS_PENDENTES
    fingerprint: sha256:490f378857bf4f6ddafc7c251e86ef422a2c8b930d34e2d365b453ddd9e4327e
  - detector: P9_CAMPOS_VAZIOS_PENDENTES
    fingerprint: sha256:8a37b589b4ae93fe2c4849b942702782476ebfb11331a5238b5107a0f5fb5abf
  - detector: P9_CAMPOS_VAZIOS_PENDENTES
    fingerprint: sha256:f1ad99a2307bd4a598d34916959a35fd8a354ce0ec2c1b67b84a8b7b1cfc8c3f
  - detector: P9_CAMPOS_VAZIOS_PENDENTES
    fingerprint: sha256:3ecd7b20e6fd58865263f566b4425873bb96e9581e916623830ce50ad8c0b25a
  - detector: P9_CAMPOS_VAZIOS_PENDENTES
    fingerprint: sha256:a5d2998dd17f99fe42de724fd86c44e5f14c445324688942b5c297fe7ea4106b
  - detector: P9_CAMPOS_VAZIOS_PENDENTES
    fingerprint: sha256:08f18be399016f4ce1632087d6cb98e64da94b9cc4c6261ae2b607fda178aa18
  - detector: P9_CAMPOS_VAZIOS_PENDENTES
    fingerprint: sha256:9179177bfbb842521095b727e6cbe2ff461e37e9b0240a16be68277df1f209c9
  - detector: P9_CAMPOS_VAZIOS_PENDENTES
    fingerprint: sha256:476c956d82487784e788a05aeabdd79f89dcd753c574d0b4478b7734eab96f46
---

# Descrição

As regras citadas estão marcadas como ativas no catálogo, mas têm campos
estruturais vazios ou marcados como 'Não identificado' na importação —
particularmente `sexo`, `integral` e/ou `tipo_calculo`.

# Evidências

A detecção `P9_CAMPOS_VAZIOS_PENDENTES` (camada 3, informativa) registrou
estas regras com valores vazios nos campos citados. Observação, não
veredito: pelo princípio da semântica adiada (RFC 0001), campos vazios na
importação **não** são, por si só, um defeito bloqueante — a relação exata
entre esses campos e a seleção da regra ainda depende de confirmação
(Q3/Q10). Isto é registrado como **pendência de preenchimento a investigar**.

# Questão a investigar

Para cada regra afetada, confirmar junto às fontes normativas / ao Sisprev
se o campo vazio é um lapso de cadastramento a preencher (e qual o valor
correto de `sexo`/`integral`/`tipo_calculo`) ou se o vazio é semanticamente
significativo (ex.: "não aplicável"). Nenhuma conclusão é presumida aqui.
