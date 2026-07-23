import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "zod";

// Every collection ids its entries by the file's own relative path (minus
// extension) — the same doc_id convention okf/*.py already uses
// (regra-0001, achado-0001, cf88/art-40-i-original), never Astro's own
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

// A dispositivo's body is the provision's exact transcribed text (P3) — no
// named sections, unlike regra/achado bodies.
const dispositivos = defineCollection({
  loader: glob({
    pattern: ["**/*.md", "!**/index.md"],
    base: "../okf/dispositivos",
    generateId: idFromPath,
  }),
  schema: z.object({
    type: z.literal("Dispositivo"),
    id: z.string().regex(/^[a-z0-9][a-z0-9-]*(\/[a-z0-9][a-z0-9-]*)+$/),
    norma: z.string().min(1),
    artigo: z.string().min(1),
    paragrafo: z.string().optional(),
    inciso: z.string().optional(),
    alinea: z.string().optional(),
    redacao_dada_por: z.string().optional(),
    vigencia_inicio: z.coerce.date().optional(),
    vigencia_fim: z.coerce.date().optional(),
    fonte: z.string().min(1),
  }),
});

export const collections = { regras, achados, dispositivos };
