// Site-wide constants (RFC 0003).
export const SITE_TITLE = "Sisprev — Catálogo em auditoria";
export const REPO_URL = "https://github.com/franklinbaldo/sisprev";

// A origem publicada, a mesma de `astro.config.mjs`. Existe porque o relatório
// impresso precisa dizer o endereço do anexo **por extenso**: um PDF juntado
// ao processo é lido em papel, e ali um link sem endereço legível não existe
// para quem o recebe.
export const SITE_URL = "https://franklinbaldo.github.io";

export function commitUrl(sha: string): string {
  return `${REPO_URL}/commit/${sha}`;
}

/**
 * Join `import.meta.env.BASE_URL` with a site-relative path, exactly one
 * slash between them regardless of whether BASE_URL itself ends in one —
 * Astro's own BASE_URL value has been observed both with and without a
 * trailing slash across configs, and a raw `${base}${path}` template
 * silently drops the separator when it's missing (RFC 0003 §4: URLs are a
 * contract, not a string-concatenation accident).
 */
export function href(path: string, base: string): string {
  return `${base.replace(/\/$/, "")}/${path.replace(/^\//, "")}`;
}
