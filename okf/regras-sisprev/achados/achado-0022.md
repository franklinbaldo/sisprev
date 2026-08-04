---
type: Achado
id: achado-0022
nome: Cinco regras invocam o art. 4º da ECE 146/2021 e gravam data_direito_ate 31/12/2099, contra o prazo de 31/12/2024 do próprio dispositivo
situacao: aberto
severidade: bloqueante
verificacao: manual
natureza: juridica
regras_afetadas:
  - /regras/regra-0006.md
  - /regras/regra-0007.md
  - /regras/regra-0008.md
  - /regras/regra-0009.md
  - /regras/regra-0032.md
detectado_em: 2026-07-29
detectado_por: franklinbaldo
---

# Descrição

As regras afetadas invocam o art. 4º da ECE 146/2021 para aplicar legislação
anterior e gravam `data_direito_ate: 31/12/2099`. O dispositivo exige que os
requisitos sejam cumpridos até 31/12/2024.

A acusação permanece válida: a sentinela mantém aberta uma janela que a norma
fecha. A correção do valor, porém, foi refinada pela decisão semântica de
01/08/2026: `DATA_DIREITO_ATE` é **exclusivo**. Portanto, para incluir todo o
dia 31/12/2024, o valor correto é:

```yaml
data_direito_ate: 01/01/2025 00:00
```

A formulação anterior deste achado indicava `31/12/2024`; ela está superada.
Esse valor excluiria justamente o último dia admitido pela norma.

# Evidências

O art. 4º da ECE 146/2021 determina que os requisitos e critérios da legislação
anterior sejam cumpridos até 31/12/2024 e assegura a concessão a qualquer tempo
depois disso. A oração final trata do momento da concessão, não prorroga o prazo
de implementação.

- `regra-0006` e `regra-0007` preservam o art. 40, § 1º, I, da CF, na redação
  da EC 41/2003. O valor legado é `31/12/2099`; o fecho correto é
  `01/01/2025`, exclusivo.
- `regra-0008` e `regra-0009` preservam o art. 6º-A da EC 41/2003, na redação
  da EC 70/2012. O valor legado é `31/12/2099`; o fecho correto também é
  `01/01/2025`, exclusivo.
- `regra-0032` invoca legislação anterior, mas sua hipótese material ainda
  depende da disposição do achado específico de fundamentação. A sentinela,
  contudo, não pode permanecer.

Fontes e decisões:

- `/dispositivos/ece-146-2021/art-4/original.md`;
- `docs/analysis/conferencia-janela-art-4-ece-146.md`;
- `okf/spec/decisoes-semanticas-regra.md`; e
- `okf/spec/janelas-temporais-regra.md`.

`regra-0039` e `regra-0040` permanecem fora da população porque o defeito de
fundamentação delas é anterior à janela e está registrado no `achado-0051`.

# Questão a investigar

Para `regra-0006` a `regra-0009`, a S3 já responde o veículo: as regras legadas
devem ser substituídas por unidades com `data_direito_ate: 01/01/2025`.

Para `regra-0032`, ainda é necessário resolver a divergência entre o regime
descrito no nome e a legislação anterior citada na fundamentação. A pergunta
não é mais qual operador usar no fecho, mas qual hipótese material a regra
pretendia representar.

# Resolução

O achado continua aberto enquanto alguma regra afetada não tiver disposição
final. A S3 encaminha `regra-0006` a `regra-0009` por substituição; a disposição
de `regra-0032` pertence ao ciclo proprietário daquela regra.
