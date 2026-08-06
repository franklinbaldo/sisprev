// Acesso tipado a dados-do-site.json — o snapshot que `scripts/derivar.py`
// escreve a cada build.
//
// O snapshot carrega duas coisas que o Astro não tem como saber sozinho: o
// commit exato que está sendo publicado, e o estado de auditoria de cada regra
// e cada achado numa forma já indexada por id, para que a ficha de uma regra
// não precise varrer a coleção de achados atrás de quem a nomeia.
//
// O que ele **não** faz mais é recomputar nada. O `status_auditoria` aqui é o
// que está escrito no frontmatter — não uma conclusão derivada de um join, como
// foi enquanto existiu a biblioteca de domínio em Python. Se um selo estiver
// errado, o erro está no `.md`, e é lá que se corrige. Esse é o preço aceito ao
// remover o join: o campo vale porque alguém o escreveu, não porque um gate o
// reverificou.
//
// A validação com Zod fica: ela não afirma que o estado está certo, só que o
// snapshot tem a forma que esta página espera — um JSON velho ou truncado
// derruba o build em vez de renderizar selo em branco.
import { z } from "zod";
import raw from "../data/dados-do-site.json";
import {
  resumirAchados,
  resumirRegras,
  type ResumoAchados,
  type ResumoRegras,
} from "./painel";

// scripts/derivar.py::SCHEMA_VERSION — um literal, não um número qualquer:
// mudar a versão é mudar o contrato, e o site tem de migrar de propósito em vez
// de aceitar em silêncio porque "veio algum número".
const SCHEMA_VERSION = 1;

const RegraStateSchema = z.object({
  status_auditoria: z.enum(["importada", "revisada", "validada"]),
  validado_pge: z.boolean(),
  validado_presidencia: z.boolean(),
  ciclo_de_validacao: z.string().min(1),
});

const AchadoStateSchema = z.object({
  situacao: z.enum(["aberto", "improcedente"]),
  severidade: z.enum(["bloqueante", "informativo"]),
  regras_afetadas: z.array(z.string()),
});

/**
 * A identificação documental do arquivo de carga de homologação **de um
 * ciclo**.
 *
 * O relatório é assinado e circula fora do repositório, onde um link é
 * promessa e não prova. O resumo criptográfico é o que permite a quem recebe
 * o documento verificar que o CSV em mãos é aquele sobre o qual a
 * manifestação se deu — e é também o que vincula à peça assinada as três
 * fundamentações, que não cabem na folha do anexo e vivem só no arquivo.
 *
 * Por ciclo, e não um só para o repositório: a carga global reúne toda
 * proposta pronta de qualquer ciclo, e identificá-la como anexo de uma
 * manifestação de ciclo garantiria a integridade do arquivo errado para
 * aquele escopo — o relatório concluiria sobre 60 regras determinando a
 * inserção de um arquivo com 64.
 */
const CargaSchema = z.object({
  arquivo: z.string().min(1),
  sha256: z.string().regex(/^[0-9a-f]{64}$/, "sha256 must be 64 lowercase hex chars"),
  bytes: z.number().int().nonnegative(),
  linhas: z.number().int().nonnegative(),
  colunas: z.number().int().nonnegative(),
});

const SiteDataSchema = z.object({
  schema_version: z.literal(SCHEMA_VERSION),
  sha: z
    .string()
    .regex(
      /^[0-9a-f]{40}$/,
      "sha must be a 40-character lowercase hex commit SHA",
    ),
  generated_at: z
    .string()
    .regex(
      /^\d{4}-\d{2}-\d{2}$/,
      "generated_at must be an ISO date (YYYY-MM-DD)",
    ),
  regras: z.record(z.string(), RegraStateSchema),
  achados: z.record(z.string(), AchadoStateSchema),
  cargas: z.record(z.string(), CargaSchema),
});

export type Carga = z.infer<typeof CargaSchema>;
export type RegraState = z.infer<typeof RegraStateSchema>;
export type AchadoState = z.infer<typeof AchadoStateSchema>;

const siteData = SiteDataSchema.parse(raw);

/** O commit exato de que este build foi gerado. */
export const sha = siteData.sha;

/** Short (9-char) form of `sha`, for compact display. */
export const shortSha = sha.slice(0, 9);

/** ISO date (YYYY-MM-DD) of the source commit — the snapshot's freshness date. */
export const generatedAt = siteData.generated_at;

/**
 * A identificação do arquivo de carga de um ciclo: nome, resumo criptográfico
 * e forma.
 *
 * Lida do mesmo arquivo que `emit-data.sh` copia para `downloads/`, de modo
 * que o resumo impresso no relatório é o do arquivo publicado ao lado dele.
 *
 * `undefined` quando o ciclo não tem regra pronta: aí não há arquivo, e o
 * relatório precisa dizer isso em vez de identificar um. Era o caso extremo do
 * defeito que a carga por ciclo corrige — o relatório de um ciclo sem nada
 * pronto imprimia o resumo criptográfico da carga global, concluindo sobre zero
 * regras e mandando inserir um arquivo com sessenta e quatro. Quem consome
 * confere a ausência contra a própria contagem de destinos na carga.
 */
export function getCarga(cicloId: string): Carga | undefined {
  return siteData.cargas[cicloId];
}

/**
 * The regra's effective audit state (status_auditoria, validado_*, ciclo).
 *
 * Throws if `regraId` is unknown to dados-do-site.json — a regra the
 * content collection can see but the emitter can't means the emitter ran
 * against a different, stale bundle state. That must fail the build loudly
 * (RFC 0003 §2: "não há como divergir silenciosamente"), never fall back to
 * a guessed default like "importada" for a regra the emitter never actually
 * looked at.
 */
export function getRegraState(regraId: string): RegraState {
  const state = siteData.regras[regraId];
  if (!state) {
    throw new Error(
      `dados-do-site.json não tem entrada para a regra "${regraId}" — o ` +
        "snapshot foi gerado de um estado do bundle diferente do que o Astro " +
        "está lendo. Rode site/scripts/emit-data.sh.",
    );
  }
  return state;
}

/**
 * The achado's effective state (situacao, severidade, regras_afetadas).
 *
 * Throws if `achadoId` is unknown, for the same reason `getRegraState` does.
 */
export function getAchadoState(achadoId: string): AchadoState {
  const state = siteData.achados[achadoId];
  if (!state) {
    throw new Error(
      `dados-do-site.json não tem entrada para o achado "${achadoId}" — o ` +
        "snapshot foi gerado de um estado do bundle diferente do que o Astro " +
        "está lendo. Rode site/scripts/emit-data.sh.",
    );
  }
  return state;
}

/** Every achado id currently affecting a given regra id (reverse of regras_afetadas). */
export function achadosAffectingRegra(regraId: string): string[] {
  return Object.entries(siteData.achados)
    .filter(([, state]) => state.regras_afetadas.includes(regraId))
    .map(([achadoId]) => achadoId)
    .sort();
}

/**
 * Whether any regra has completed the audit cycle (status_auditoria "validada").
 *
 * Drives noindex and the audit banner's wording (RFC 0003 §5) as a live
 * computation, not a flag a human could forget to flip back — the
 * directive stops applying automatically the moment it stops being true.
 */
export const hasAnyValidatedRegra = Object.values(siteData.regras).some(
  (regra) => regra.status_auditoria === "validada",
);

/**
 * Contagens do painel da home (RFC 0003 §3) — calculadas aqui, o único
 * módulo que enxerga o payload inteiro, e não na página, para que nenhuma
 * outra superfície precise iterar o JSON cru por conta própria.
 *
 * `painel.ts` é puro justamente para não importar este módulo de volta: o
 * job `test` do CI roda vitest sem o emissor, logo sem `dados-do-site.json`.
 */
export const resumoDasRegras: ResumoRegras = resumirRegras(
  Object.values(siteData.regras),
);

/** Contagens de achados por situação/severidade — mesma origem e mesma razão de `resumoDasRegras`. */
export const resumoDosAchados: ResumoAchados = resumirAchados(
  Object.values(siteData.achados),
);
