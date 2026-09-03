import { chromium } from "playwright";
import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";

const baseUrl = process.env.CAPTURE_BASE_URL ?? "http://127.0.0.1:4173/sisprev/";
const evaluatedSha = process.env.EVALUATED_SHA ?? process.env.GITHUB_SHA ?? "unknown";
const mergeRefSha = process.env.MERGE_REF_SHA || null;
const phase = process.env.CAPTURE_PHASE ?? "unknown";
const outputDir = path.resolve("../visual-evidence");

const surfaces = [
  {
    name: "home",
    path: "",
    requiredText: ["Sisprev — Catálogo em auditoria", "Leve o catálogo com você", "Baixar relatório completo em PDF"],
  },
  {
    name: "relatorio",
    path: "relatorio/",
    requiredText: ["Baixar em PDF", "origem: commit"],
  },
];

const viewports = [
  { name: "desktop", width: 1280, height: 900 },
  { name: "mobile", width: 390, height: 844 },
];

await mkdir(outputDir, { recursive: true });
const browser = await chromium.launch({ headless: true });
const evidence = {
  evaluated_sha: evaluatedSha,
  merge_ref_sha: mergeRefSha,
  phase,
  generated_at: new Date().toISOString(),
  surfaces: [],
};

let failed = false;
try {
  for (const surface of surfaces) {
    for (const viewport of viewports) {
      const context = await browser.newContext({ viewport: { width: viewport.width, height: viewport.height } });
      const page = await context.newPage();
      const url = new URL(surface.path, baseUrl).toString();
      const response = await page.goto(url, { waitUntil: "networkidle" });
      if (!response?.ok()) throw new Error(`${surface.name}/${viewport.name}: HTTP ${response?.status() ?? "sem resposta"}`);

      const text = await page.locator("body").innerText();
      const missingText = surface.requiredText.filter((expected) => !text.includes(expected));
      const dimensions = await page.evaluate(() => ({
        viewport_width: window.innerWidth,
        document_width: document.documentElement.scrollWidth,
        body_width: document.body.scrollWidth,
      }));
      const overflow = dimensions.document_width > dimensions.viewport_width + 1 || dimensions.body_width > dimensions.viewport_width + 1;
      const screenshot = `${surface.name}-${viewport.width}x${viewport.height}.png`;
      await page.screenshot({ path: path.join(outputDir, screenshot), fullPage: false });

      const result = {
        route: new URL(url).pathname,
        surface: surface.name,
        viewport,
        screenshot,
        http_status: response.status(),
        required_text_present: missingText.length === 0,
        missing_text: missingText,
        ...dimensions,
        horizontal_overflow: overflow,
      };
      evidence.surfaces.push(result);

      if (missingText.length > 0) {
        console.error(`${surface.name}/${viewport.name}: texto obrigatório ausente: ${missingText.join(", ")}`);
        failed = true;
      }
      if (viewport.name === "mobile" && overflow) {
        console.error(`${surface.name}/${viewport.name}: documento ${dimensions.document_width}px em viewport ${dimensions.viewport_width}px`);
        failed = true;
      }
      await context.close();
    }
  }
} finally {
  await browser.close();
  await writeFile(path.join(outputDir, "evidence.json"), `${JSON.stringify(evidence, null, 2)}\n`, "utf8");
}

if (failed) process.exit(1);
