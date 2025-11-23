# 📦 Q27: CommonJS vs ES Modules (ESM) & Bundling Deep Dive




**Trả lời:**

**🎯 Core Concepts:**

**1. CommonJS (CJS) - Node.js Module System:**
- **Syntax**: `require()` để import, `module.exports` để export
- **Loading**: Synchronous (đồng bộ), blocking I/O
- **Execution**: Runtime evaluation, dynamic imports
- **Scope**: File-based, isolated module scope
- **Extension**: `.js`, `.cjs`
- **Use Case**: Node.js backend, legacy packages

**2. ES Modules (ESM) - JavaScript Standard:**
- **Syntax**: `import/export` statements
- **Loading**: Asynchronous (bất đồng bộ), non-blocking
- **Execution**: Static analysis, compile-time resolution
- **Scope**: Module scope với strict mode mặc định
- **Extension**: `.mjs`, `.js` (với `"type": "module"` trong package.json)
- **Use Case**: Modern browsers, Node.js (v12+), frontend frameworks

**✅ Ưu điểm ESM:**
- **Static Analysis**: Bundlers có thể tree-shake dead code tại compile time
- **Async Loading**: Không block main thread, tốt cho performance
- **Browser Native**: Modern browsers hỗ trợ native, không cần bundler cho dev
- **Explicit Dependencies**: Import statements rõ ràng, dễ trace
- **Named Exports**: Hỗ trợ multiple exports từ một file

**⚠️ Nhược điểm ESM:**
- **Backward Compatibility**: Không chạy trên legacy browsers
- **File Extensions Required**: Phải specify `.js` extension trong imports (browser)
- **CORS Issues**: Cần proper headers khi load từ CDN
- **Debugging**: Source maps cần thiết cho bundled code

**Code Example - CommonJS vs ESM:**

```typescript
// ============================================
// COMMONJS (Node.js Traditional)
// ============================================

// math.js - CommonJS Export
function add(a, b) {
  return a + b;
}

function subtract(a, b) {
  return a - b;
}

// Export toàn bộ object
module.exports = {
  add,
  subtract,
};

// Hoặc export individual
exports.add = add;
exports.subtract = subtract;

// app.js - CommonJS Import
const math = require('./math'); // Synchronous loading
console.log(math.add(1, 2)); // 3

// Destructuring import
const { add, subtract } = require('./math');
console.log(add(1, 2)); // 3

// Dynamic import (runtime)
const moduleName = './math';
const math2 = require(moduleName); // ✅ Works - runtime evaluation

// Conditional import
if (condition) {
  const math3 = require('./math'); // ✅ Works
}

// ============================================
// ES MODULES (Modern JavaScript)
// ============================================

// math.mjs - ESM Named Exports
export function add(a: number, b: number): number {
  return a + b;
}

export function subtract(a: number, b: number): number {
  return a - b;
}

// Default export
export default function multiply(a: number, b: number): number {
  return a * b;
}

// app.mjs - ESM Import
import multiply, { add, subtract } from './math.mjs'; // Async loading
console.log(add(1, 2)); // 3
console.log(multiply(3, 4)); // 12

// Import all
import * as math from './math.mjs';
console.log(math.add(1, 2)); // 3

// Dynamic import (async)
const modulePath = './math.mjs';
// import modulePath; // ❌ Error - must be static string

// Dynamic import with await
const { add: dynamicAdd } = await import('./math.mjs'); // ✅ Works

// Conditional import
if (condition) {
  const { add } = await import('./math.mjs'); // ✅ Works with await
}

// ============================================
// BROWSER USAGE - Native ESM
// ============================================
```

```html
<!-- index.html - Browser Native ESM -->
<!DOCTYPE html>
<html>
<head>
  <title>ESM in Browser</title>
</head>
<body>
  <!-- Traditional script (no modules) -->
  <script src="./legacy.js"></script>
  
  <!-- ESM - type="module" enables import/export -->
  <script type="module">
    // Import từ local file
    import { add } from './utils/math.js'; // Phải có .js extension
    console.log('1 + 2 =', add(1, 2));

    // Import từ CDN (ESM format)
    import confetti from 'https://cdn.skypack.dev/canvas-confetti';
    confetti();

    // Dynamic import cho code splitting
    document.getElementById('btn')?.addEventListener('click', async () => {
      // Lazy load heavy module khi user click
      const { heavyFunction } = await import('./heavy-feature.js');
      heavyFunction();
    });

    // Import maps (Chrome 89+)
    // <script type="importmap">
    // {
    //   "imports": {
    //     "lodash": "https://cdn.skypack.dev/lodash",
    //     "react": "https://cdn.skypack.dev/react"
    //   }
    // }
    // </script>
    
    // Then import như package name
    // import _ from 'lodash';
  </script>

  <!-- Preload modules cho better performance -->
  <link rel="modulepreload" href="./utils/math.js">
  <link rel="modulepreload" href="./heavy-feature.js">
</body>
</html>
```

**Vietnamese Explanation - Cách Hoạt Động:**

```typescript
// ============================================
// COMMONJS LOADING MECHANISM
// ============================================
/**
 * Vietnamese Explanation:
 * 
 * 1. SYNCHRONOUS LOADING (Đồng Bộ):
 *    - require() đọc file NGAY LẬP TỨC
 *    - Block execution cho đến khi file loaded
 *    - Cached sau lần đầu (module.exports object được cache)
 * 
 * 2. RUNTIME EVALUATION:
 *    - Code trong module được execute ngay khi require()
 *    - Dynamic imports allowed (require với string variable)
 *    - Conditional requires allowed
 * 
 * 3. CACHING:
 *    - Module chỉ execute MỘT LẦN
 *    - Các lần require() sau return cached exports
 *    - require.cache chứa tất cả loaded modules
 */

// Example: CommonJS caching
// a.js
console.log('Module A loaded'); // Chỉ log 1 lần
module.exports = { name: 'A' };

// main.js
const a1 = require('./a'); // Log: "Module A loaded"
const a2 = require('./a'); // Không log gì (cached)
console.log(a1 === a2); // true - same object reference

// ============================================
// ESM LOADING MECHANISM
// ============================================
/**
 * Vietnamese Explanation:
 * 
 * 1. ASYNCHRONOUS LOADING (Bất Đồng Bộ):
 *    - import statements parsed trước khi execution
 *    - Browser fetch modules parallel, không block
 *    - Modules execute theo dependency order
 * 
 * 2. STATIC ANALYSIS:
 *    - Import/export phải là static strings (không thể dùng variables)
 *    - Bundlers có thể analyze dependencies tại build time
 *    - Tree-shaking possible (remove unused exports)
 * 
 * 3. MODULE GRAPH:
 *    - Browser xây dựng dependency graph
 *    - Fetch → Parse → Instantiate → Evaluate
 *    - Mỗi module chỉ evaluate MỘT LẦN
 * 
 * 4. LIVE BINDINGS:
 *    - Imported values là REFERENCES, không phải copies
 *    - Changes trong export module reflect trong import
 */

// Example: ESM live bindings
// counter.mjs
export let count = 0;
export function increment() {
  count++;
}

// main.mjs
import { count, increment } from './counter.mjs';
console.log(count); // 0
increment();
console.log(count); // 1 - live binding updated!

// CommonJS would copy value:
// const { count } = require('./counter.js');
// increment();
// console.log(count); // Still 0 - copied value

// ============================================
// BUNDLING với ESBuild (Ultra-Fast Bundler)
// ============================================
/**
 * Vietnamese Explanation:
 * 
 * ESBuild là extremely fast bundler viết bằng Go
 * - 10-100x nhanh hơn Webpack/Rollup
 * - Built-in TypeScript support
 * - Tree-shaking tự động
 * - Code splitting
 * - Minification
 */

// esbuild.config.js
import * as esbuild from 'esbuild';

// Basic build
await esbuild.build({
  entryPoints: ['src/index.ts'],
  bundle: true, // Bundle tất cả dependencies
  outfile: 'dist/bundle.js',
  minify: true, // Minify code
  sourcemap: true, // Generate source maps
  target: 'es2020', // Target environment
  format: 'esm', // Output format: 'esm' | 'cjs' | 'iife'
  platform: 'browser', // 'browser' | 'node' | 'neutral'
  
  // Tree-shaking configuration
  treeShaking: true,
  
  // External dependencies (không bundle)
  external: ['react', 'react-dom'],
  
  // Define global constants
  define: {
    'process.env.NODE_ENV': '"production"',
  },
  
  // Plugin system
  plugins: [],
});

// Advanced: Code Splitting với multiple entry points
await esbuild.build({
  entryPoints: {
    home: 'src/pages/home.ts',
    about: 'src/pages/about.ts',
    contact: 'src/pages/contact.ts',
  },
  bundle: true,
  outdir: 'dist',
  splitting: true, // Enable code splitting
  format: 'esm', // Required for splitting
  chunkNames: 'chunks/[name]-[hash]',
});

// Transform single file (không bundle)
const result = await esbuild.transform(
  'const x: number = 1;',
  {
    loader: 'ts',
    target: 'es2020',
    minify: true,
  }
);
console.log(result.code); // "const x=1;"

// Watch mode cho development
const ctx = await esbuild.context({
  entryPoints: ['src/index.ts'],
  bundle: true,
  outfile: 'dist/bundle.js',
  sourcemap: true,
});

await ctx.watch(); // Watch for file changes
await ctx.serve({ port: 3000 }); // Serve với dev server

// ============================================
// TREE-SHAKING với ESM
// ============================================
/**
 * Vietnamese Explanation:
 * 
 * Tree-shaking = Dead Code Elimination
 * - Bundler analyze import/export graph
 * - Remove unused exports từ final bundle
 * - CHỈ works với ESM (static analysis)
 * - CommonJS KHÔNG thể tree-shake (dynamic)
 */

// utils.ts - Library với nhiều functions
export function usedFunction() {
  console.log('Used');
}

export function unusedFunction() {
  console.log('Unused'); // This will be tree-shaken
}

export function anotherUnused() {
  console.log('Also unused'); // This too
}

// main.ts - Chỉ import 1 function
import { usedFunction } from './utils';
usedFunction();

// After bundling với tree-shaking:
// ✅ usedFunction included in bundle
// ❌ unusedFunction removed (dead code)
// ❌ anotherUnused removed (dead code)

// Side-effects prevent tree-shaking
// utils-with-side-effects.ts
console.log('This runs on import!'); // Side effect!

export function myFunction() {
  return 42;
}

// Even if myFunction unused, file still included due to side-effect
// Solution: Mark as side-effect-free in package.json
// {
//   "sideEffects": false
// }

// Or specify which files have side-effects:
// {
//   "sideEffects": ["*.css", "src/polyfills.ts"]
// }

// ============================================
// CODE SPLITTING & LAZY LOADING
// ============================================
/**
 * Vietnamese Explanation:
 * 
 * Code Splitting = Tách code thành nhiều bundles
 * - Initial bundle: Core functionality
 * - Lazy chunks: Load on-demand
 * - Route-based: Load khi navigate to route
 * - Component-based: Load khi component rendered
 */

// React example with lazy loading
import React, { lazy, Suspense } from 'react';

// Lazy load component (code splitting automatic)
const HeavyComponent = lazy(() => import('./HeavyComponent'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <HeavyComponent />
    </Suspense>
  );
}

// Vue example
import { defineAsyncComponent } from 'vue';

const AsyncComp = defineAsyncComponent(() =>
  import('./components/AsyncComponent.vue')
);

// Manual code splitting với dynamic import
async function loadFeature() {
  // Webpack/Vite sẽ tự động tạo separate chunk
  const { feature } = await import('./heavy-feature');
  feature();
}

// Preload important chunks
document.addEventListener('DOMContentLoaded', () => {
  // Preload chunk for better UX
  import(/* webpackPreload: true */ './important-feature');
});

// ============================================
// INTEROPERABILITY: CJS ↔ ESM
// ============================================
/**
 * Vietnamese Explanation:
 * 
 * Mixing CommonJS và ESM có thể tricky
 * - ESM có thể import CJS (Node.js tự convert)
 * - CJS KHÔNG thể synchronously require ESM
 * - Need dynamic import() cho CJS → ESM
 */

// ESM importing CommonJS
import cjsModule from './commonjs-module.js'; // Works
import { namedExport } from './commonjs-module.js'; // Works if exports.namedExport

// CommonJS importing ESM
const esmModule = require('./esm-module.mjs'); // ❌ Error!
// Solution: Use dynamic import
(async () => {
  const esmModule = await import('./esm-module.mjs'); // ✅ Works
})();

// ============================================
// PACKAGE.JSON CONFIGURATION
// ============================================

// Dual package (support both CJS and ESM)
{
  "name": "my-package",
  "version": "1.0.0",
  "type": "module", // Default to ESM
  
  // Exports field (Node.js 12+)
  "exports": {
    ".": {
      "import": "./dist/index.mjs", // ESM version
      "require": "./dist/index.cjs" // CJS version
    },
    "./utils": {
      "import": "./dist/utils.mjs",
      "require": "./dist/utils.cjs"
    }
  },
  
  // Fallback for older tools
  "main": "./dist/index.cjs", // CJS entry
  "module": "./dist/index.mjs", // ESM entry
  
  // TypeScript types
  "types": "./dist/index.d.ts",
  
  // Tree-shaking hints
  "sideEffects": false
}
```

**🎯 Best Practices:**

1. **Use ESM for new projects**: Better tooling, tree-shaking, future-proof
2. **Mark side-effects**: Set `"sideEffects": false` trong package.json nếu possible
3. **Code splitting strategy**: Route-based > Component-based > Manual
4. **Bundle size monitoring**: Use tools như webpack-bundle-analyzer
5. **Source maps**: Always generate cho production debugging
6. **External dependencies**: Don't bundle large libraries (React, Lodash) - load từ CDN
7. **Dynamic imports**: Use cho features hiếm dùng, route-based loading
8. **ESBuild for speed**: 10-100x faster than Webpack, perfect for large projects
9. **Preload critical chunks**: Use `<link rel="modulepreload">` cho important modules
10. **CDN với ESM**: Use ESM-compatible CDNs như Skypack, jsDelivr

**⚠️ Common Mistakes:**

```typescript
// ❌ Sai: Mixing require trong ESM
import React from 'react';
const lodash = require('lodash'); // Error trong ESM!

// ✅ Đúng: Consistent import syntax
import React from 'react';
import _ from 'lodash';

// ❌ Sai: Dynamic import path trong top-level ESM
const moduleName = './utils';
import { fn } from moduleName; // Error - must be static!

// ✅ Đúng: Use dynamic import() for runtime paths
const moduleName = './utils';
const { fn } = await import(moduleName);

// ❌ Sai: Forget file extension trong browser ESM
import { add } from './math'; // Error - need .js!

// ✅ Đúng: Always include extension
import { add } from './math.js';

// ❌ Sai: CommonJS exports trong ESM file
export const a = 1;
module.exports = { a }; // Error - can't mix!

// ✅ Đúng: Use ESM syntax only
export const a = 1;
export default { a };

// ❌ Sai: Không config CORS cho ESM từ CDN
<script type="module">
  import lib from 'https://wrong-cdn.com/lib.js'; // CORS error!
</script>

// ✅ Đúng: Use ESM-compatible CDNs
<script type="module">
  import lib from 'https://cdn.skypack.dev/lib'; // Works!
</script>
```

**📊 Performance Comparison:**

```typescript
// Bundler speed comparison (1000 modules):
// - esbuild: ~0.5s ⚡ (Go-based, parallel)
// - Rollup: ~5s (JavaScript, good tree-shaking)
// - Webpack: ~10s (JavaScript, complex config)
// - Parcel: ~8s (JavaScript, zero-config)

// Bundle size comparison (after tree-shaking):
// - ESM only: 100KB (best tree-shaking)
// - ESM + CJS mixed: 150KB (some dead code)
// - CJS only: 200KB (no tree-shaking)
```

**🎯 Use Cases:**

- **ESM Native (no bundler)**: Prototypes, small apps, HTTP/2
- **ESBuild**: Large apps cần fast builds, TypeScript projects
- **Rollup**: Libraries cần best tree-shaking
- **Webpack**: Complex apps với nhiều loaders/plugins
- **Vite**: Development với ESM native, production với Rollup

