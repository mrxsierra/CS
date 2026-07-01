---
title: Vite & Modern Build Tools
tags: ['stack/frontend']
created: 2026-06-10
---

# Vite & Modern Build Tools

## Overview
Build tools are a common talking point in frontend interviews — not just "which one do you use" but "how do they work under the hood." Vite has become the industry standard, replacing Webpack for most new projects.

## Why Vite? The Shift from Webpack

| Aspect | Webpack (Legacy) | Vite (Modern) |
|--------|-----------------|---------------|
| Dev server | Bundles everything on startup | **ESM-native** — serves modules on-demand |
| HMR | Re-bundles changed modules | **Native ESM HMR** — instant regardless of app size |
| Build | Single-threaded | **Rollup** — tree-shaking, code-splitting |
| Config | Verbose, plugin-heavy | Minimal, sensible defaults |
| TypeScript | Needs loader config | Built-in (esbuild transforms, no type-check) |

### How Vite's Dev Server Works
1. **No bundling at startup** — serves `.js`/`.ts` files as native ES modules
2. **esbuild transforms** — TypeScript → JavaScript, JSX → JS at lightning speed (Go-based)
3. **Only compiles changed files** on HMR — no re-analysis of the dependency graph

### How Vite's Production Build Works
- Uses **Rollup** for production (mature tree-shaking, code splitting, plugin ecosystem)
- Pre-configured for optimal output: CSS inlining, asset hashing, dynamic imports

## Key Concepts

### Hot Module Replacement (HMR)
HMR updates modules without a full page reload, preserving application state:
```javascript
// In development, Vite sends a WebSocket message when a module changes
// The browser updates only that module's exports
// No full page refresh — state is preserved
```

### Module Federation (Webpack 5 / Vite Plugin)
The pattern that enables **micro-frontends**:
```javascript
// Host app loads remote components at runtime
new ModuleFederationPlugin({
  name: 'host',
  remotes: {
    checkout: 'checkout@http://localhost:3001/remoteEntry.js',
  },
});
// You can now: import('checkout/Cart')
```

### Tree Shaking
Dead-code elimination that removes unused exports:
```javascript
// Only `add` will be bundled — `subtract` is tree-shaken away
import { add } from './math';
export function add(a, b) { return a + b; }
export function subtract(a, b) { return a - b; } // Eliminated
```

## Common Patterns & Config

### Optimizing the Build
```javascript
// vite.config.ts
export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
          ui: ['antd', '@ant-design/icons'],
        },
      },
    },
    target: 'es2020',   // Modern browsers = smaller bundles
    minify: 'terser',   // Better compression than esbuild
    sourcemap: false,   // Disable for production
  },
});
```

### Environment Variables
```javascript
// VITE_ prefix is required for client-side exposure
console.log(import.meta.env.VITE_API_URL);
console.log(import.meta.env.MODE); // 'development' | 'production'
```

## Build Tool Interview Questions

1. **"Why is Vite faster than Webpack?"** — Native ESM dev server avoids bundling on startup. esbuild (Go-based) for transforms vs. Webpack's JS-based loaders. Only changed files are re-transformed on HMR.

2. **"What is the difference between `esbuild` and `Rollup`?"** — esbuild is a bundler written in Go, extremely fast, used by Vite for development transforms. Rollup is a JS-based bundler with better tree-shaking and plugin ecosystem, used by Vite for production builds.

3. **"How do you handle code splitting?"** — Dynamic imports: `const LazyComponent = () => import('./HeavyComponent')`. Vite/Rollup automatically creates separate chunks for each dynamic import boundary.

4. **"What is the difference between `dependencies` and `devDependencies` in a bundler context?"** — `dependencies` are bundled into the output. `devDependencies` (TypeScript, ESLint, test frameworks) are used during development/build but don't appear in production bundles.

## Related Topics
- [[08_stack_deep_dives/01_frontend_stack/03_react|React Mastery]]
- [[08_stack_deep_dives/01_frontend_stack/04_next_js|Next.js & Server Side Patterns]]
- [[08_stack_deep_dives/01_frontend_stack/index|Frontend Stack Index]]
- [[02_role_tracks/02_frontend_engineer|Frontend Engineer Track]]

## Resources
- [Vite Official Docs](https://vitejs.dev/)
- [Vite vs. Webpack Comparison](https://vitejs.dev/guide/why.html)
- [esbuild Documentation](https://esbuild.github.io/)