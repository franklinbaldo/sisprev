/**
 * Leitura dos documentos de texto do repositório (RFC 0003, Fase C —
 * "coleções de relatórios e RFCs").
 *
 * Diferente de regra/achado/dispositivo, esses `.md` **não têm
 * frontmatter**: título, status e nota de apoio vivem no próprio corpo,
 * escritos para quem lê o arquivo no GitHub. Este módulo lê esses três
 * fatos do markdown em vez de exigir que os documentos ganhem frontmatter
 * só para o site — a mesma regra dos outros artefatos derivados: o site se
 * adapta à fonte, a fonte não se deforma para o site.
 *
 * Puro de propósito, sem nenhum import de `site-data.ts`: o job `test` do
 * CI roda vitest **sem** o emissor, então um `*.test.ts` que alcance
 * `dados-do-site.json` quebra o CI mesmo passando localmente.
 */

/** Primeiro `# Título` do corpo, ou `null` se o documento não tiver um. */
export function tituloDoMarkdown(body: string): string | null {
  for (const linha of body.split("\n")) {
    const m = /^#\s+(.+?)\s*$/.exec(linha);
    if (m) return m[1];
  }
  return null;
}

/**
 * A "Nota:" de abertura dos relatórios — o aviso de que aquilo é apoio à
 * decisão gerado por IA, não artefato oficial de auditoria.
 *
 * Sai como texto corrido (marcações `**` removidas, quebras juntadas) para
 * caber num aviso de listagem. É **extraída, nunca sintetizada**: um
 * relatório que não traga a nota não ganha uma inventada pelo site — a
 * função devolve `null` e a página mostra o aviso genérico da §5.
 */
export function notaDeApoio(body: string): string | null {
  const linhas = body.split("\n");
  const bloco: string[] = [];
  let dentro = false;
  for (const linha of linhas) {
    if (linha.startsWith(">")) {
      dentro = true;
      bloco.push(linha.replace(/^>\s?/, ""));
      continue;
    }
    if (dentro) break;
    if (linha.trim() !== "" && !linha.startsWith("#")) break;
  }
  if (bloco.length === 0) return null;
  // A nota é exibida como texto num card, não renderizada como markdown:
  // ênfase e `código` viram o texto que envolvem, senão o card mostra a
  // marcação crua (`**Não é artefato oficial**`, crases em volta de
  // `regra-*.md`) em vez do que ela quer dizer.
  const texto = bloco
    .join(" ")
    .replace(/\*\*([^*]+)\*\*/g, "$1")
    .replace(/`([^`]+)`/g, "$1")
    .replace(/\*\*/g, "")
    .replace(/\s+/g, " ")
    .replace(/^Nota:\s*/i, "")
    .trim();
  return texto === "" ? null : texto;
}

/**
 * O status declarado por uma RFC (`- **Status**: Aceita (2026-07-17)`).
 *
 * Só a primeira frase: as RFCs escrevem o status seguido de parágrafos de
 * ressalva (a 0002 explica o que foi e o que não foi implementado), úteis
 * na ficha e ruído numa listagem. O corte é no primeiro `;` ou `.` —
 * nunca por truncamento cego em N caracteres, que cortaria no meio de uma
 * palavra e mudaria o que a RFC diz de si mesma.
 */
export function statusDaRfc(body: string): string | null {
  const m = /^[-*]\s+\*\*Status\*\*:\s*([\s\S]+?)(?=\n[-*]\s+\*\*|\n\n|$)/m.exec(body);
  if (!m) return null;
  const inteiro = m[1].replace(/\s+/g, " ").trim();
  const corte = /^(.+?)[;.](?:\s|$)/.exec(inteiro);
  const texto = (corte ? corte[1] : inteiro).trim();
  return texto === "" ? null : texto;
}

/** Número da RFC a partir do id de arquivo (`0003-site-...` → `0003`). */
export function numeroDaRfc(id: string): string | null {
  const m = /^(\d{4})-/.exec(id);
  return m ? m[1] : null;
}

export interface AlvoDeLink {
  /** URL final já pronta para o `href` (inclui a base do site quando interna). */
  readonly url: string;
  /** `true` quando o destino é uma página do próprio site. */
  readonly interno: boolean;
}

const DIRETORIO_DA_COLECAO: Record<string, string> = {
  relatorios: "docs/analysis",
  rfcs: "docs/rfc",
  spec: "okf/spec",
};

const COLECAO_DO_DIRETORIO: Record<string, string> = {
  "docs/analysis": "relatorios",
  "docs/rfc": "rfcs",
  // As especificações passaram a ser bundle OKF publicado, e por isso um link
  // para elas vira link interno em vez de sair para o GitHub. Enquanto elas
  // viviam em `docs/spec/` sem rota, a citação mais frequente do repositório
  // mandava o leitor para fora do site.
  "okf/spec": "spec",
};

/** Resolve `caminho` (estilo POSIX, relativo) a partir do diretório `origem`. */
function resolverCaminho(origem: string, caminho: string): string {
  const partes = origem.split("/").filter(Boolean);
  for (const parte of caminho.split("/")) {
    if (parte === "" || parte === ".") continue;
    if (parte === "..") partes.pop();
    else partes.push(parte);
  }
  return partes.join("/");
}

/**
 * Reescreve um link `.md` **relativo** de um documento para a URL certa.
 *
 * Um documento é escrito para ser lido no GitHub, onde
 * `[reconciliação](reconciliacao-invalidez-incapacidade.md)` funciona; no
 * site esse mesmo link levaria a lugar nenhum. Aqui ele vira
 * `/sisprev/relatorios/reconciliacao-invalidez-incapacidade/` quando o
 * destino é publicado, e o arquivo no GitHub quando não é (`okf/spec/`,
 * `CLAUDE.md`) — **nunca um link morto e nunca um link silenciosamente
 * omitido**.
 *
 * Só mexe em link relativo: as referências OKF canônicas
 * (`/regras/regra-0006.md`) começam com `/` e passam intactas, porque
 * identidade de documento não é rótulo de navegação (§4).
 *
 * O destino externo aponta para `blob/main` de propósito, não para o SHA
 * publicado: é um arquivo que o site não publica, então o que interessa é
 * a versão viva no repositório — e amarrar isso ao SHA exigiria que o
 * plugin de markdown dependesse do emissor, que só roda no build.
 */
export function reescreverLinkMd(
  link: string,
  colecaoDeOrigem: string,
  base: string,
  repoUrl: string,
): AlvoDeLink | null {
  if (/^[a-z][a-z0-9+.-]*:/i.test(link) || link.startsWith("/") || link.startsWith("#")) return null;
  const [semAncora, ...resto] = link.split("#");
  if (!semAncora.endsWith(".md")) return null;
  const ancora = resto.length > 0 ? `#${resto.join("#")}` : "";

  const origem = DIRETORIO_DA_COLECAO[colecaoDeOrigem];
  if (origem === undefined) return null;

  const alvo = resolverCaminho(origem, semAncora);
  const barra = alvo.lastIndexOf("/");
  const diretorio = barra === -1 ? "" : alvo.slice(0, barra);
  const nome = alvo.slice(barra + 1).replace(/\.md$/, "");
  const colecao = COLECAO_DO_DIRETORIO[diretorio];

  if (colecao !== undefined) {
    const prefixo = base.replace(/\/$/, "");
    return { url: `${prefixo}/${colecao}/${nome}/${ancora}`, interno: true };
  }
  return { url: `${repoUrl}/blob/main/${alvo}${ancora}`, interno: false };
}
