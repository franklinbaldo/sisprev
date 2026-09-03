#!/usr/bin/env node

import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";
import AxeBuilder from "@axe-core/playwright";
import { chromium } from "playwright";

const baseUrl = process.env.CAPTURE_BASE_URL ?? "http://127.0.0.1:4173/sisprev/";
const evaluatedSha = process.env.EVALUATED_SHA ?? process.env.GITHUB_SHA ?? "unknown";
const mergeRefSha = process.env.MERGE_REF_SHA || null;
const phase = process.env.CAPTURE_PHASE ?? "unknown";
const outputDir = path.resolve("../visual-evidence");
const routes = ["", "relatorio/"];

async function keyboardAudit(page) {
  const expected = await page.evaluate(() => {
    const selector = [
      'a[href]',
      'button:not([disabled])',
      'input:not([disabled]):not([type="hidden"])',
      'select:not([disabled])',
      'textarea:not([disabled])',
      '[tabindex]:not([tabindex="-1"])',
      'summary',
    ].join(',');

    const visible = [...document.querySelectorAll(selector)].filter((element) => {
      if (!(element instanceof HTMLElement)) return false;
      const style = getComputedStyle(element);
      const rect = element.getBoundingClientRect();
      return style.display !== "none" && style.visibility !== "hidden" && rect.width > 0 && rect.height > 0 && element.tabIndex >= 0;
    });

    visible.forEach((element, index) => {
      element.dataset.sisprevA11yId = `focus-${index + 1}`;
    });

    return visible.map((element) => ({
      id: element.dataset.sisprevA11yId,
      tag: element.tagName.toLowerCase(),
      text: (element.getAttribute("aria-label") || element.textContent || "").trim().replace(/\s+/g, " ").slice(0, 120),
      href: element instanceof HTMLAnchorElement ? element.getAttribute("href") : null,
    }));
  });

  await page.evaluate(() => {
    if (document.activeElement instanceof HTMLElement) document.activeElement.blur();
  });

  const sequence = [];
  const focusFailures = [];
  const maxTabs = Math.max(expected.length + 3, 3);

  for (let index = 0; index < maxTabs; index += 1) {
    await page.keyboard.press("Tab");
    const state = await page.evaluate(() => {
      const element = document.activeElement;
      if (!(element instanceof HTMLElement)) return null;

      const style = getComputedStyle(element);
      const outlineWidth = Number.parseFloat(style.outlineWidth || "0");
      const borderWidths = [style.borderTopWidth, style.borderRightWidth, style.borderBottomWidth, style.borderLeftWidth]
        .map((value) => Number.parseFloat(value || "0"));
      const visibleIndicator =
        (style.outlineStyle !== "none" && outlineWidth > 0) ||
        style.boxShadow !== "none" ||
        borderWidths.some((width) => width > 0);

      return {
        id: element.dataset.sisprevA11yId || null,
        tag: element.tagName.toLowerCase(),
        text: (element.getAttribute("aria-label") || element.textContent || "").trim().replace(/\s+/g, " ").slice(0, 120),
        href: element instanceof HTMLAnchorElement ? element.getAttribute("href") : null,
        focus_visible: element.matches(":focus-visible"),
        visible_indicator: visibleIndicator,
        outline: `${style.outlineWidth} ${style.outlineStyle} ${style.outlineColor}`,
        box_shadow: style.boxShadow,
      };
    });

    if (!state?.id) continue;
    sequence.push(state);
    if (!state.focus_visible || !state.visible_indicator) {
      focusFailures.push(`${state.id} (${state.tag} ${state.text || state.href || ""}) recebeu foco por teclado sem indicador visual detectável`);
    }
  }

  const reached = new Set(sequence.map((item) => item.id));
  const unreachable = expected.filter((item) => !reached.has(item.id));
  const consecutiveRepeat = sequence.some((item, index) => index > 0 && item.id === sequence[index - 1].id);

  return {
    expected,
    sequence,
    unreachable,
    consecutive_repeat: consecutiveRepeat,
    failures: [
      ...unreachable.map((item) => `${item.id} (${item.tag} ${item.text || item.href || ""}) não foi alcançado por Tab`),
      ...(consecutiveRepeat ? ["a sequência de Tab ficou presa no mesmo controle em passos consecutivos"] : []),
      ...focusFailures,
    ],
  };
}

await mkdir(outputDir, { recursive: true });
const browser = await chromium.launch({ headless: true });
const observations = [];
const failures = [];

try {
  for (const route of routes) {
    const context = await browser.newContext({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 1 });
    const page = await context.newPage();
    const url = new URL(route, baseUrl).toString();
    const response = await page.goto(url, { waitUntil: "networkidle" });
    const status = response?.status() ?? 0;

    const axe = await new AxeBuilder({ page })
      .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
      .analyze();
    const materialViolations = axe.violations
      .filter((violation) => violation.impact === "serious" || violation.impact === "critical")
      .map((violation) => ({
        id: violation.id,
        impact: violation.impact,
        help: violation.help,
        help_url: violation.helpUrl,
        nodes: violation.nodes.map((node) => ({ target: node.target, summary: node.failureSummary })),
      }));

    const keyboard = await keyboardAudit(page);
    const routeFailures = [];
    if (status !== 200) routeFailures.push(`${route || "/"}: HTTP ${status}`);
    for (const violation of materialViolations) {
      routeFailures.push(`${route || "/"}: axe ${violation.impact} ${violation.id} — ${violation.help}`);
    }
    routeFailures.push(...keyboard.failures.map((failure) => `${route || "/"}: ${failure}`));

    observations.push({
      route: new URL(url).pathname,
      status,
      axe: {
        total_violations: axe.violations.length,
        serious_or_critical: materialViolations,
      },
      keyboard,
      failures: routeFailures,
    });
    failures.push(...routeFailures);
    await context.close();
  }
} finally {
  await browser.close();
}

const report = {
  evaluated_sha: evaluatedSha,
  merge_ref_sha: mergeRefSha,
  phase,
  generated_at: new Date().toISOString(),
  base_url: baseUrl,
  contract: {
    axe_tags: ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"],
    material_impacts: ["serious", "critical"],
    keyboard: "todos os controles visíveis na ordem normal devem ser alcançáveis por Tab e exibir indicador perceptível de foco",
  },
  observations,
  failures,
};

await writeFile(path.join(outputDir, "accessibility-evidence.json"), `${JSON.stringify(report, null, 2)}\n`, "utf8");

if (failures.length) {
  console.error(failures.join("\n"));
  process.exit(1);
}

console.log(`Contrato de acessibilidade passou em ${routes.length} rotas.`);
