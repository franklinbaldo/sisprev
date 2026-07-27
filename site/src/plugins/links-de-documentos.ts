/**
 * Reescreve os links `.md` relativos dos documentos publicados na Fase C
 * (RFC 0003) — `docs/analysis/` e `docs/rfc/`.
 *
 * Esses documentos foram escritos para ser lidos no GitHub, onde
 * `[reconciliação](reconciliacao-invalidez-incapacidade.md)` resolve
 * sozinho. Publicados como página, o mesmo link levaria a lugar nenhum. A
 * alternativa seria reescrever os `.md` na fonte para apontarem para URLs
 * do site — mas aí o documento pararia de funcionar no repositório, que é
 * onde ele é editado e revisado. O site se adapta à fonte.
 *
 * É um plugin **mdast do Sätteri**, não um `remarkPlugins` do Astro: a
 * partir do Astro 7 o Sätteri é o processador padrão, e usar
 * `markdown.remarkPlugins` obrigaria a reinstalar o pipeline `unified`
 * legado para o site inteiro — trocar o processador de markdown de todas
 * as páginas já publicadas para reescrever link em duas pastas seria um
 * preço desproporcional.
 *
 * O plugin se limita pelo **caminho do arquivo**: só age em markdown que
 * venha das duas pastas publicadas. Os corpos de regra/achado/dispositivo
 * passam intactos por construção, não por sorte de regex — e as
 * referências OKF canônicas (`/regras/regra-0006.md`), que são identidade
 * de documento e não rótulo de navegação (§4), ficam como estão.
 */

import { reescreverLinkMd } from "../lib/documentos";

/** O subconjunto de nó mdast que este plugin lê. */
interface NoComUrl {
  url?: string;
}

/** O subconjunto do contexto do Sätteri que este plugin usa. */
interface ContextoMdast {
  readonly fileURL: URL | undefined;
  setProperty(node: never, key: never, value: never): void;
}

interface Opcoes {
  base: string;
  repoUrl: string;
}

const COLECAO_POR_PASTA: ReadonlyArray<readonly [string, string]> = [
  ["/docs/analysis/", "relatorios"],
  ["/docs/rfc/", "rfcs"],
];

function colecaoDoArquivo(fileURL: URL | undefined): string | null {
  if (fileURL === undefined) return null;
  const caminho = decodeURIComponent(fileURL.pathname);
  for (const [pasta, colecao] of COLECAO_POR_PASTA) {
    if (caminho.includes(pasta)) return colecao;
  }
  return null;
}

export function pluginDeLinksDeDocumentos({ base, repoUrl }: Opcoes) {
  function reescrever(node: NoComUrl, ctx: ContextoMdast): void {
    if (typeof node.url !== "string") return;
    const colecao = colecaoDoArquivo(ctx.fileURL);
    if (colecao === null) return;
    const alvo = reescreverLinkMd(node.url, colecao, base, repoUrl);
    if (alvo === null) return;
    // `setProperty` é o caminho de mutação do Sätteri: o nó chega
    // `Readonly` e a alteração vai para o buffer de comandos, não para o
    // objeto JS.
    (ctx.setProperty as (n: NoComUrl, k: "url", v: string) => void)(node, "url", alvo.url);
  }

  // Um link markdown pode chegar como `link` (inline, `[x](y.md)`) ou como
  // `definition` (a definição de um link de referência, `[x]: y.md`). Os
  // dois carregam `url` e os dois precisam da mesma reescrita.
  return {
    name: "sisprev-links-de-documentos",
    link: reescrever,
    definition: reescrever,
  };
}
