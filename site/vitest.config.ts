import { defineConfig } from "vitest/config";

// Unit tests only for the simulador's pure logic (site/src/lib/*.test.ts) —
// no Astro/DOM rendering here, so the plain node environment is enough.
export default defineConfig({
  test: {
    environment: "node",
    include: ["src/**/*.test.ts"],
  },
});
