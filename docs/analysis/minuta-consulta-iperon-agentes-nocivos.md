# Minuta de consulta ao IPERON — regras permanentes de agentes nocivos

**Estado: minuta interna, não enviada.** Qualquer contato com o IPERON depende
de autorização expressa de Franklin Baldo quanto ao destinatário, canal e texto
final.

# Contexto objetivo

A auditoria encontrou quatro linhas permanentes para agentes nocivos:

- `regra-0065`, `regra-0066` e `regra-0067`: arts. 25, 27, I, e 41, III da
  LCE 1.100/2021, integralidade e paridade;
- `regra-0071`: arts. 24, 27, II, e 41, III, média e reajuste pelo RGPS, sem
  paridade.

As três primeiras foram consolidadas, em proposta, na unidade
`agentes-nocivos-art-41-iii-integralidade-paridade`. A quarta recebeu proposta
própria,
`agentes-nocivos-art-41-iii-media-sem-paridade`. As duas unidades estão em
`preview`, dentro de grupos inativos; nada foi alterado no catálogo
operacional.

# Perguntas propostas

## 1. Corte de ingresso e marco de direito

Confirma-se a seguinte parametrização?

| ramo              | `data_adm_apos` | `data_adm_ate` | `data_direito_apos` |
| ----------------- | --------------- | -------------- | ------------------- |
| arts. 25 + 27, I  | `01/01/1950`    | `31/12/2003`   | `18/10/2021`        |
| arts. 24 + 27, II | `31/12/2003`    | `31/12/2099`   | `18/10/2021`        |

Em particular, qual ato administrativo o Sisprev trata como “ingresso” para
essas colunas: nomeação, posse, exercício ou outro?

## 2. Código de cálculo do art. 25

Qual valor de `tipo_calculo` representa, no Sisprev, a “totalidade da
remuneração no cargo efetivo” do art. 25 da LCE 1.100/2021?

- `Valor Efetivo`;
- `Remuneração de Contribuição`;
- outro valor.

As regras que citam o art. 25 usam hoje os dois primeiros valores. A pergunta
é operacional: pretende identificar o comando efetivamente executado pelo
motor, não apenas escolher o rótulo juridicamente mais próximo.

## 3. Campo `tabelapontuacao`

O art. 41 exige soma de idade e tempo de contribuição — 66, 76 ou 86 pontos.
As regras permanentes gravam `tabelapontuacao: N`, enquanto as regras de
transição do art. 8º da ECE 146/2021 gravam `S`.

O campo deve ser `S` nas regras permanentes? Se não, em qual estrutura do
Sisprev os pontos do art. 41 são aferidos?

## 4. Cobertura dos incisos I e II do art. 41

O art. 41 contém três faixas:

1. 66 pontos e 15 anos de exposição;
2. 76 pontos e 20 anos de exposição;
3. 86 pontos e 25 anos de exposição.

As quatro linhas permanentes existentes citam apenas o inciso III. O catálogo
deve conter unidades próprias para os incisos I e II, em cada um dos dois
ramos de cálculo/reajuste, ou a cobertura exclusiva do inciso III é
deliberada?

## 5. Protocolo de comprovação

Confirma-se, para a operação do Sisprev, o protocolo documental descrito no
art. 42 da LCE 1.100/2021 e transcrito no Parecer PGE/IPERON nº 608/2025:
formulários históricos, laudo técnico conforme o período e PPP a partir de
2004?

Qual unidade ou perfil é responsável por registrar no sistema:

- exposição efetiva e permanente;
- tempo de serviço público e no cargo;
- pontos e tempo de exposição;
- ausência de opção pelo regime do art. 40, § 16, da Constituição?

# Efeito esperado das respostas

As respostas permitem:

1. promover ou rejeitar as duas unidades em `preview`;
2. definir a projeção correta de `tipo_calculo` e `tabelapontuacao`;
3. criar, se necessárias, as unidades dos incisos I e II;
4. registrar a decisão de completude dos grupos, ainda sem colocá-los em
   produção;
5. identificar o responsável institucional por cada requisito de verificação
   humana.

# Referências internas

- [`achado-0042`](../../okf/regras-sisprev/achados/achado-0042.md) — janelas
  temporais;
- [`achado-0057`](../../okf/regras-sisprev/achados/achado-0057.md) — código de
  cálculo do art. 25;
- [`unidade de integralidade e paridade`](../../okf/regras-auditadas/unidades/agentes-nocivos-art-41-iii-integralidade-paridade.md);
- [`unidade de média sem paridade`](../../okf/regras-auditadas/unidades/agentes-nocivos-art-41-iii-media-sem-paridade.md);
- [`Parecer PGE/IPERON nº 608/2025`](../../fontes-oficiais/processos-sei/0016_102962-2020-85/parecer_608_pge-iperon__0061369704_.md).
