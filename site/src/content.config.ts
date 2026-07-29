import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "zod";

// Every collection ids its entries by the file's own relative path (minus
// extension) — the same doc_id convention okf/*.py already uses
// (regra-0001, achado-0001, cf88/art-40-par-1-inc-i/ec-41-2003), never Astro's own
// slug-from-frontmatter heuristics. Keeps URLs and cross-links a pure
// function of the filename, not of any rendered "slug" field.
function idFromPath({ entry }: { entry: string }) {
  return entry.replace(/\.md$/, "");
}

// A regra's frontmatter *is* the deployable Sisprev rule (CLAUDE.md, P13.2)
// — ~27 domain fields, extensible by design (P2 treats every current and
// future domain field as material). Only the handful the site actually
// routes/links/lists on are declared strictly here; everything else passes
// through untouched, exactly like bundle.py's Concept (RFC 0003 §4: "shape,
// not semantics"). status_auditoria/validado_pge/validado_presidencia are
// deliberately *not* read from here — their *effective*, P7-joined value
// comes only from dados-do-site.json (see src/lib/site-data.ts); reading
// the raw frontmatter value here would silently recompute a join that
// belongs to the Python library, never to Astro/Zod.
//
// The fields below status_regra/dispositivos are the simulador's (RFC 0002)
// match criteria — a case of "filtering", one of the categories this
// project's own convention says should be typed strictly rather than left
// loose. Kept as plain `z.string()` rather than a closed enum: this widens
// from `unknown` to "a string", it does not commit to today's set of
// observed values, so a future new tipo_de_beneficio/tipo_calculo value
// can't fail the whole build.
const regras = defineCollection({
  loader: glob({ pattern: "regra-*.md", base: "../okf/regras-sisprev/regras", generateId: idFromPath }),
  schema: z
    .object({
      type: z.literal("Regra"),
      id: z.string().regex(/^regra-\d{4}$/),
      nome: z.string().min(1),
      tipo_de_beneficio: z.string(),
      ciclo_de_validacao: z.string(),
      dispositivos: z.array(z.string()).default([]),
      status_regra: z.string().optional(),
      sexo: z.string(),
      apos_especial: z.string(),
      data_adm_ate: z.string(),
      data_adm_apos: z.string(),
      data_direito_ate: z.string(),
      data_direito_apos: z.string(),
      integral: z.string(),
      tipo_calculo: z.string(),
      paridade: z.string(),
      simulavel: z.string(),
    })
    .loose(),
});

// An achado's frontmatter is a closed P14 contract (achado_schema.py) — no
// passthrough needed, every field here is one the site renders.
// regras_afetadas is transformed from the canonical "/regras/regra-NNNN.md"
// OKF reference into a bare regra id, so pages can link/join directly
// without every template re-deriving the same string manipulation.
const achados = defineCollection({
  loader: glob({ pattern: "achado-*.md", base: "../okf/regras-sisprev/achados", generateId: idFromPath }),
  schema: z.object({
    type: z.literal("Achado"),
    id: z.string().regex(/^achado-\d{4}$/),
    nome: z.string().min(1),
    situacao: z.enum(["aberto", "resolvido"]),
    severidade: z.enum(["bloqueante", "informativo"]),
    verificacao: z.enum(["mecanica", "manual", "hibrida"]),
    natureza: z.enum(["juridica", "dados", "modelagem", "processo"]),
    regras_afetadas: z
      .array(z.string())
      .min(1)
      .transform((refs) => refs.map((ref) => ref.replace(/^\/regras\//, "").replace(/\.md$/, ""))),
    detectado_em: z.coerce.date(),
    detectado_por: z.string().min(1),
    deteccoes: z
      .array(z.object({ detector: z.string(), fingerprint: z.string() }))
      .default([]),
    resolvido_em: z.coerce.date().optional(),
    resolvido_por: z.string().optional(),
    efeito_deteccao: z.enum(["deve_desaparecer", "pode_persistir"]).optional(),
  }),
});

// O vocabulário fechado de normas citáveis (P4). Cada `norma.md` guarda o
// nome canônico e as URLs oficiais que uma transcrição pode ser conferida
// contra — uma vez, em vez do mesmo nome redigitado em cada dispositivo.
const normas = defineCollection({
  loader: glob({
    pattern: "*/norma.md",
    base: "../okf/dispositivos",
    generateId: ({ entry }) => entry.replace(/\/norma\.md$/, ""),
  }),
  schema: z.object({
    type: z.literal("Norma"),
    id: z.string().regex(/^[a-z0-9][a-z0-9-]*$/),
    nome: z.string().min(1),
    apelido: z.string().min(1),
    fontes: z.array(z.url()).min(1),
  }),
});

// A dispositivo's body is the provision's exact transcribed text (P3) — no
// named sections, unlike regra/achado bodies.
//
// `componentes` é o endereço estrutural, uma lista ordenada — nunca quatro
// campos planos: rótulo e ordem são *derivados* dela (`lib/dispositivo.ts`),
// então a ficha e a listagem não têm como discordar do `.md`. O id tem
// exatamente três segmentos, `<norma>/<endereço>/<redação>`: o diretório é
// o dispositivo, os arquivos dentro dele são as suas redações.
const dispositivos = defineCollection({
  loader: glob({
    pattern: ["**/*.md", "!**/index.md", "!**/norma.md"],
    base: "../okf/dispositivos",
    generateId: idFromPath,
  }),
  schema: z.object({
    type: z.literal("Dispositivo"),
    id: z.string().regex(/^[a-z0-9][a-z0-9-]*\/[a-z0-9][a-z0-9-]*\/[a-z0-9][a-z0-9-]*$/),
    norma: z.string().min(1),
    // `redacao_dada_por`/`vigencia_*` também no componente (RFC 0009): um
    // dispositivo é a unidade endereçada com toda a cadeia que a contém, então
    // alterar um ancestral cria redação nova mesmo com o nível interno
    // intacto. Sem isso a ficha só consegue mostrar *uma* procedência para um
    // corpo que exibe vários níveis, cada um com a sua — e era essa perda que
    // deixava passar vigência atravessando a alteração de um ancestral.
    componentes: z
      .array(
        z.object({
          tipo: z.enum(["artigo", "caput", "paragrafo", "paragrafo_unico", "inciso", "alinea", "item"]),
          valor: z.string().optional(),
          sufixo: z.string().optional(),
          redacao_dada_por: z.string().optional(),
          vigencia_inicio: z.coerce.date().optional(),
          vigencia_fim: z.coerce.date().optional(),
        }),
      )
      .min(1),
    redacao_dada_por: z.string().optional(),
    vigencia_inicio: z.coerce.date().optional(),
    vigencia_fim: z.coerce.date().optional(),
    fontes: z.array(z.url()).min(1),
  }),
});

// Os documentos de texto (RFC 0003, Fase C) — relatórios de análise e as
// próprias RFCs. Ao contrário de regra/achado/dispositivo, **não têm
// frontmatter**: são markdown escrito para ser lido no GitHub, com título,
// status e nota de apoio no corpo. O schema aqui é, portanto,
// deliberadamente vazio e `.loose()` — declarar campos obrigatórios
// obrigaria a poluir os documentos com frontmatter só para satisfazer o
// site, exatamente o inverso da regra que vale para o resto do bundle. O
// que o site precisa ler sai do corpo, em `lib/documentos.ts`.
const documentoSchema = z.object({}).loose();

const relatorios = defineCollection({
  loader: glob({ pattern: "*.md", base: "../docs/analysis", generateId: idFromPath }),
  schema: documentoSchema,
});

const rfcs = defineCollection({
  loader: glob({ pattern: "*.md", base: "../docs/rfc", generateId: idFromPath }),
  schema: documentoSchema,
});

export const collections = { regras, achados, normas, dispositivos, relatorios, rfcs };
