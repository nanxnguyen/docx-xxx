# 📦 Topic20: Module Systems - CommonJS vs ES Modules & Bundling Deep Dive

## ⭐ Senior/Staff Summary

> **CommonJS và ESM khác nhau không chỉ ở syntax. Khác biệt thật nằm ở loading model, static analysis, runtime behavior, interop và cách bundler tối ưu production bundle.**

- 📦 **CommonJS (CJS)**: module system truyền thống của Node.js, dùng `require()` và `module.exports`, load đồng bộ, resolve runtime, linh hoạt nhưng khó tree-shake.
- 🎯 **ES Modules (ESM)**: chuẩn JavaScript chính thức, dùng `import/export`, static structure, hỗ trợ native browser, tree-shaking tốt hơn và phù hợp frontend hiện đại.
- 🔥 **Tree-shaking** hoạt động tốt nhất với ESM vì bundler đọc được import/export graph tại build time.
- ⚠️ **CJS interop với ESM** có nhiều edge cases: default import, named import giả, `require()` không sync được ESM, dual package hazard.
- 🚀 **Bundling** không chỉ gom file: còn transform, transpile, minify, code splitting, chunking, tree-shaking, sourcemap, HMR và dependency optimization.
- 🧩 **Vite/esbuild/Rollup/Webpack** có vai trò khác nhau: dev speed, library bundle, app bundle, plugin ecosystem.
- ✅ Senior frontend cần biết đọc `package.json`: `type`, `exports`, `main`, `module`, `types`, `sideEffects`.

## 🧠 Key Mental Model

### 1. CJS là runtime-first, ESM là static-first

| Tiêu chí | CommonJS | ES Modules |
|---|---|---|
| Syntax | `require`, `module.exports` | `import`, `export` |
| Loading | Synchronous | Async/module graph |
| Analysis | Runtime/dynamic | Static/build-time |
| Browser native | Không | Có |
| Tree-shaking | Kém | Tốt |
| Dynamic loading | `require(variable)` | `import()` |
| Binding | Export object/cache | Live bindings |
| Top-level await | Không native | Có |

### 2. Bundler cần biết dependency graph

Bundler tối ưu tốt khi dependency graph rõ:

```text
ESM import/export -> static graph -> tree-shaking -> smaller bundle
CJS require runtime -> dynamic graph -> harder to analyze -> more code included
```

### 3. Production question

Khi bundle phình hoặc import lỗi, hãy hỏi:

- Package đang ship CJS hay ESM?
- `exports` field resolve đúng entry chưa?
- Có side effect làm tree-shaking fail không?
- Có dynamic import tạo chunk đúng kỳ vọng không?
- Có duplicate dependency do CJS/ESM dual package không?
- SSR runtime là Node ESM hay CJS?

## 📚 Main Concepts

### 📦 CommonJS (CJS)

CommonJS phổ biến trong Node.js legacy ecosystem.

```js
// math.cjs
function add(a, b) {
  return a + b;
}

function subtract(a, b) {
  return a - b;
}

module.exports = {
  add,
  subtract,
};
```

```js
// app.cjs
const { add } = require("./math.cjs");

console.log(add(1, 2));
```

Đặc điểm:

- `require()` chạy đồng bộ.
- Module evaluate khi `require`.
- Kết quả được cache sau lần đầu.
- Có thể `require()` theo điều kiện hoặc biến runtime.
- Hợp với Node.js cũ, scripts, tooling legacy.

```js
if (process.env.FEATURE_X === "true") {
  const feature = require("./feature-x.cjs");
  feature.run();
}
```

### 🎯 ES Modules (ESM)

ESM là chuẩn JavaScript chính thức cho modules.

```ts
// math.ts
export function add(a: number, b: number) {
  return a + b;
}

export function subtract(a: number, b: number) {
  return a - b;
}

export default function multiply(a: number, b: number) {
  return a * b;
}
```

```ts
// app.ts
import multiply, { add, subtract } from "./math";

console.log(add(1, 2));
console.log(multiply(3, 4));
```

Đặc điểm:

- Import/export có cấu trúc tĩnh.
- Browser hỗ trợ native qua `<script type="module">`.
- Bundler có thể tree-shake.
- Có live bindings.
- Có `import()` cho dynamic import/code splitting.
- ESM chạy trong strict mode mặc định.

### 🌐 Browser native ESM

```html
<script type="module">
  import { add } from "./utils/math.js";

  console.log(add(1, 2));

  document.querySelector("#load")?.addEventListener("click", async () => {
    const { heavyFeature } = await import("./heavy-feature.js");
    heavyFeature();
  });
</script>
```

Lưu ý browser:

- Relative import thường cần file extension: `./math.js`.
- Module script deferred mặc định.
- Cross-origin module cần CORS headers đúng.
- Có thể dùng `modulepreload`.

```html
<link rel="modulepreload" href="/assets/dashboard.js" />
```

### 🗺️ Import Maps

Import maps cho phép map bare imports trong browser.

```html
<script type="importmap">
{
  "imports": {
    "lodash": "https://cdn.skypack.dev/lodash-es",
    "@app/": "/src/"
  }
}
</script>

<script type="module">
  import _ from "lodash";
  import { add } from "@app/utils/math.js";
</script>
```

💡 Dùng cho prototype/native ESM setup. Với app production lớn, bundler vẫn phổ biến hơn vì tối ưu chunk, cache, transform, minify, legacy support.

### 🔄 Loading, caching và evaluation

#### CommonJS caching

```js
// counter.cjs
console.log("counter module loaded");

let count = 0;

module.exports = {
  increment() {
    count += 1;
    return count;
  },
};
```

```js
const a = require("./counter.cjs");
const b = require("./counter.cjs");

console.log(a === b); // true
console.log(a.increment()); // 1
console.log(b.increment()); // 2
```

Điểm cần nhớ:

- Module chỉ evaluate một lần.
- `require.cache` lưu module.
- Shared mutable state có thể tạo singleton behavior.

#### ESM live bindings

```js
// counter.mjs
export let count = 0;

export function increment() {
  count += 1;
}
```

```js
// app.mjs
import { count, increment } from "./counter.mjs";

console.log(count); // 0
increment();
console.log(count); // 1
```

ESM import là **live binding**, không phải copy value. Đây là điểm khác quan trọng khi debug circular dependencies hoặc state được export.

### 🔁 Circular dependencies

Cả CJS và ESM đều có circular dependency, nhưng behavior khác.

```js
// a.cjs
const b = require("./b.cjs");
module.exports = { name: "a", bName: b.name };

// b.cjs
const a = require("./a.cjs");
module.exports = { name: "b", aName: a.name };
```

CJS có thể trả về object chưa hoàn tất nếu vòng lặp xảy ra trong lúc evaluate.

Với ESM, binding được tạo trước, nhưng value có thể nằm trong `temporal dead zone` nếu truy cập quá sớm.

Rule senior:

- Tránh circular dependency bằng cách tách shared type/helper.
- Không để module top-level chạy logic phức tạp phụ thuộc nhau.
- Với React, tránh barrel file export vòng giữa features.

### 🌲 Tree-shaking

Tree-shaking = loại bỏ code không dùng khỏi production bundle.

```ts
// utils.ts
export function used() {
  return "used";
}

export function unused() {
  return "unused";
}
```

```ts
// main.ts
import { used } from "./utils";

console.log(used());
```

Bundler có thể loại `unused` nếu:

- Module là ESM.
- Export không được dùng.
- File không có side effects quan trọng.
- Minifier/dead-code elimination chạy đúng.

### ⚠️ Side effects và `sideEffects`

File có side effect là file chạy code chỉ bằng việc import.

```ts
// polyfills.ts
import "core-js/stable";
console.log("polyfill loaded");
```

```ts
// styles.ts
import "./global.css";
```

Nếu package khai báo sai `"sideEffects": false`, bundler có thể xóa nhầm import CSS/polyfill.

```json
{
  "sideEffects": [
    "*.css",
    "src/polyfills.ts"
  ]
}
```

Rule:

- Library pure ESM có thể dùng `"sideEffects": false`.
- App có CSS/polyfill/global registration phải khai báo exceptions.
- Không đặt side effect rải rác trong utility modules.

### 🧩 Code splitting và dynamic import

Dynamic import tạo boundary để bundler tách chunk.

```tsx
import { lazy, Suspense } from "react";

const AdminPage = lazy(() => import("./pages/AdminPage"));

export function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <AdminPage />
    </Suspense>
  );
}
```

Manual dynamic import:

```ts
async function exportReport() {
  const { generateCsv } = await import("./report/generateCsv");
  return generateCsv();
}
```

Best use cases:

- Route-level chunks.
- Admin/editor/chart features.
- Heavy libraries: `monaco-editor`, charting, PDF, spreadsheet.
- Rarely used flows.

⚠️ Đừng split quá nhỏ. Quá nhiều chunks gây network waterfall.

### 🔧 CJS ↔ ESM interop

#### ESM import CJS

```js
// legacy.cjs
module.exports = {
  foo: 1,
  bar: 2,
};
```

```js
// app.mjs
import legacy from "./legacy.cjs";

console.log(legacy.foo);
```

Named import từ CJS không phải lúc nào cũng ổn:

```js
import { foo } from "./legacy.cjs"; // ⚠️ runtime/tooling dependent
```

An toàn hơn:

```js
import legacy from "./legacy.cjs";

const { foo } = legacy;
```

#### CJS import ESM

```js
// app.cjs
async function main() {
  const esm = await import("./modern.mjs");
  esm.run();
}

main();
```

CJS không thể `require()` ESM đồng bộ theo cách thông thường.

### 📦 `package.json` fields

```json
{
  "name": "@company/ui",
  "type": "module",
  "main": "./dist/index.cjs",
  "module": "./dist/index.mjs",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.mjs",
      "require": "./dist/index.cjs"
    },
    "./button": {
      "types": "./dist/button.d.ts",
      "import": "./dist/button.mjs",
      "require": "./dist/button.cjs"
    }
  },
  "sideEffects": [
    "*.css"
  ]
}
```

Ý nghĩa:

- `type`: `.js` trong package được hiểu là ESM nếu `"module"`, CJS nếu không khai báo.
- `main`: entry cũ, thường CJS.
- `module`: convention cho bundler, thường ESM, nhưng không phải chuẩn Node chính thức như `exports`.
- `exports`: public entrypoints và conditional exports.
- `types`: TypeScript declaration.
- `sideEffects`: hint cho bundler tree-shaking.

### ⚠️ Dual package hazard

Dual package ship cả CJS và ESM. Nếu app vô tình load cả 2 entry, bạn có thể có 2 instance khác nhau.

Ví dụ bug:

- Shell import ESM entry.
- Một dependency require CJS entry.
- Package có singleton state.
- App có 2 singleton khác nhau.

Senior rule:

- Tránh stateful singleton trong package dual format.
- Kiểm tra bundle analyzer.
- Dùng `exports` rõ ràng.
- Align toolchain để resolve cùng entry khi có thể.

### 🛠️ Bundler responsibilities

Bundler thường làm nhiều việc:

- Build dependency graph.
- Resolve imports.
- Convert TypeScript/JSX.
- Transpile theo target browser.
- Bundle dependencies.
- Tree-shake.
- Minify.
- Code split.
- Generate sourcemaps.
- Inject env constants.
- Handle CSS/assets.
- Dev server + HMR.

## 🧪 Practical TypeScript/JavaScript Examples

### ✅ 1. CJS vs ESM cùng một module

```js
// CJS
const fs = require("node:fs");

module.exports = function readJson(path) {
  return JSON.parse(fs.readFileSync(path, "utf8"));
};
```

```js
// ESM
import { readFile } from "node:fs/promises";

export async function readJson(path) {
  const content = await readFile(path, "utf8");
  return JSON.parse(content);
}
```

### ✅ 2. `__dirname` trong ESM

```js
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

console.log(join(__dirname, "schema.json"));
```

### ✅ 3. esbuild config

```js
import * as esbuild from "esbuild";

await esbuild.build({
  entryPoints: ["src/index.ts"],
  bundle: true,
  outfile: "dist/index.js",
  format: "esm",
  platform: "browser",
  target: ["es2020"],
  minify: true,
  sourcemap: true,
  treeShaking: true,
  external: ["react", "react-dom"],
  define: {
    "process.env.NODE_ENV": '"production"',
  },
});
```

### ✅ 4. esbuild code splitting

```js
await esbuild.build({
  entryPoints: {
    home: "src/pages/home.ts",
    dashboard: "src/pages/dashboard.ts",
    settings: "src/pages/settings.ts",
  },
  bundle: true,
  outdir: "dist",
  format: "esm",
  splitting: true,
  chunkNames: "chunks/[name]-[hash]",
});
```

### ✅ 5. Vite dynamic import trong frontend

```ts
const modules = import.meta.glob("./pages/**/*.tsx");

export async function loadPage(path: string) {
  const loader = modules[`./pages/${path}.tsx`];

  if (!loader) {
    throw new Error(`Page not found: ${path}`);
  }

  return loader();
}
```

`import.meta.glob` giúp Vite biết trước import graph để tạo chunks an toàn hơn so với runtime string import không kiểm soát.

### ✅ 6. Analyze bundle

```bash
npx vite-bundle-visualizer
npx webpack-bundle-analyzer dist/stats.json
npx source-map-explorer "dist/assets/*.js"
```

Khi bundle lớn, kiểm tra:

- Package nào chiếm nhiều KB?
- Có duplicate React/lodash/date library không?
- Package resolve CJS hay ESM?
- Lazy chunk có bị kéo vào initial bundle không?
- Source map có đủ để debug production không?

## ⚛️ Production Notes / React Implications

### 🚀 Performance

- ESM giúp bundler tree-shake tốt hơn, nhưng không đảm bảo bundle nhỏ nếu package có side effects.
- Route-level code splitting thường hiệu quả hơn component-level splitting quá nhỏ.
- `React.lazy` nên đi cùng loading/error state tốt.
- Dùng `modulepreload` hoặc route prefetch cho route sắp vào.
- Theo dõi bundle size trong CI.

### 🧭 SSR / Node runtime

SSR thường gặp lỗi do ESM/CJS mismatch:

- Package ESM-only bị `require()` từ CJS.
- Package CJS dùng Node built-ins không chạy ở edge/browser runtime.
- `window/document` chạy ở module top-level làm SSR crash.
- Conditional exports resolve khác giữa Node/bundler.

Rule:

- Check runtime target: browser, Node, edge, SSR.
- Không chạy browser-only side effect ở top-level.
- Dùng dynamic import cho browser-only package nếu cần.
- Test SSR build, không chỉ dev browser.

### 🔐 Security

- Dynamic import path không nên nhận input tùy ý từ user.
- CDN ESM cần trust boundary rõ, CORS/SRI/CSP phù hợp.
- Bundle có thể leak env nếu define sai biến.
- Source maps production cần policy rõ: public, hidden, uploaded to monitoring, hoặc private.

### 🧪 Testing & Debugging

- Test cả build production, vì dev server có thể resolve khác production bundle.
- Dùng bundle analyzer sau khi thêm dependency lớn.
- Test import CJS/ESM interop trong Node version target.
- Với library, test package bằng consumer app thật.
- Source map phải map đúng stack trace về source.

### 📚 Library publishing

Nếu publish library frontend:

- Ship ESM-first.
- Nếu cần backward compatibility, ship CJS + ESM bằng `exports`.
- Không expose deep private imports ngoài `exports`.
- Generate `.d.ts`.
- Khai báo `sideEffects` chính xác.
- Test tree-shaking bằng app consumer.

## ⚠️ Common Pitfalls

- ❌ Trộn `require()` trong file ESM.
- ❌ Dùng `module.exports` trong file đang là ESM.
- ❌ Import CJS bằng named import rồi tin là luôn ổn.
- ❌ Quên `.js` extension khi dùng native browser ESM.
- ❌ Dynamic import path quá tự do làm bundler không split/analyze đúng.
- ❌ Đặt side effect trong utility file làm tree-shaking fail.
- ❌ Khai báo `"sideEffects": false` sai khiến CSS/polyfill bị xóa.
- ❌ Dual package làm load 2 instance của cùng package.
- ❌ Dùng default export không nhất quán làm interop khó debug.
- ❌ Chỉ test dev server, không test production bundle.
- ❌ Source maps bị thiếu khiến production stack trace khó đọc.

## ✅ Decision Guide / Checklist

**Chọn module system:**

- Project frontend mới -> ưu tiên ESM.
- Node script legacy -> CJS vẫn ổn nếu ecosystem cũ.
- Library mới -> ESM-first, cân nhắc dual package nếu cần.
- SSR/Edge -> kiểm tra package có support runtime target không.

**Chọn bundler/tool:**

- App React/Vue hiện đại -> Vite.
- Library cần output sạch/tree-shaking tốt -> Rollup hoặc tsup/unbuild tùy stack.
- App enterprise Webpack legacy -> Webpack vẫn ổn nếu plugin ecosystem cần.
- Build/transpile cực nhanh -> esbuild/SWC.

**Tối ưu bundle:**

- Dùng ESM imports.
- Kiểm tra `sideEffects`.
- Dùng code splitting theo route/feature.
- Analyze bundle trước khi optimize cảm tính.
- Externalize dependency nếu build library.

**Khi gặp lỗi interop:**

- Kiểm tra `package.json type`.
- Kiểm tra file extension: `.cjs`, `.mjs`, `.js`.
- Kiểm tra `exports.import` vs `exports.require`.
- Thử default import từ CJS thay vì named import.
- Dùng `await import()` khi CJS cần load ESM.

## 🗣️ Short Interview Answer

Em nghĩ khác biệt chính giữa CommonJS và ESM không chỉ là `require` với `import`. CommonJS là runtime-first, load đồng bộ và rất linh hoạt vì có thể require theo điều kiện hoặc biến runtime. ESM thì static-first, import/export được phân tích trước khi chạy nên bundler có thể build dependency graph, tree-shake và code split tốt hơn.

Theo em với frontend hiện đại, em sẽ ưu tiên ESM vì browser và tooling như Vite/Rollup/Webpack/esbuild đều tối ưu tốt hơn cho ESM. Nhưng khi làm production hoặc SSR, em vẫn phải để ý interop với package CJS: named import từ CJS không phải lúc nào cũng an toàn, CJS không require ESM sync được, và dual package có thể gây hai instance nếu resolve sai.

Em thường debug bundle bằng cách xem `package.json` của dependency: `type`, `exports`, `main`, `module`, `sideEffects`, rồi dùng bundle analyzer để xem package nào bị kéo vào initial bundle. Với React app, em dùng dynamic import/`React.lazy` cho route hoặc feature nặng, nhưng không split quá nhỏ vì có thể gây network waterfall.

## 🧠 Ghi nhớ nhanh

- **CJS** = `require/module.exports`, sync, runtime, Node legacy.
- **ESM** = `import/export`, static, browser native, tree-shaking tốt.
- **Tree-shaking cần ESM + không side effects sai**.
- **Dynamic import `import()`** = lazy load/code splitting.
- **CJS -> ESM** thường cần `await import()`.
- **ESM -> CJS** dùng default import an toàn hơn named import.
- **`type: module`** làm `.js` được hiểu là ESM trong package.
- **`exports`** là public API map hiện đại của package.
- **`sideEffects`** khai báo sai có thể làm bundle to hoặc xóa nhầm code.
- **Bundler** không chỉ bundle, còn transform, minify, split, sourcemap, HMR.

## 📖 Giải thích các thuật ngữ trong topic

| Thuật ngữ | Giải thích ngắn |
|---|---|
| CommonJS / CJS | Module system truyền thống của Node.js dùng `require` và `module.exports` |
| ES Modules / ESM | Chuẩn module JavaScript dùng `import` và `export` |
| `require()` | Hàm CJS để load module đồng bộ |
| `module.exports` | Object CJS dùng để export public API |
| `import/export` | Syntax ESM để khai báo dependency và public API |
| Static analysis | Bundler đọc được dependency graph trước runtime |
| Tree-shaking | Loại code không dùng khỏi bundle |
| Dead code elimination | Tối ưu xóa code không bao giờ được dùng/chạy |
| Side effect | Code chạy chỉ vì module được import, ví dụ CSS/polyfill/global registration |
| `sideEffects` | Field trong `package.json` giúp bundler biết file nào có side effect |
| Dynamic import | `import()` trả Promise, dùng để lazy load module |
| Code splitting | Tách app thành nhiều chunks để load theo nhu cầu |
| Chunk | File bundle con được tạo ra sau code splitting |
| Module graph | Đồ thị dependency giữa các modules |
| Live binding | ESM import giữ liên kết sống với exported variable |
| Interop | Cách CJS và ESM import/export qua lại |
| Dual package | Package ship cả CJS và ESM entry |
| `type` | Field quyết định `.js` là ESM hay CJS trong package |
| `exports` | Field khai báo entrypoints public và conditional exports |
| `main` | Entry cũ, thường trỏ CJS |
| `module` | Convention bundler cũ để tìm ESM entry |
| `types` | TypeScript declaration entry |
| Bundler | Tool gom/tối ưu modules như Vite, Webpack, Rollup, esbuild |
| Transpile | Chuyển syntax mới sang syntax target cũ hơn |
| Minify | Rút gọn code production |
| Sourcemap | Map code bundle/minified về source gốc để debug |
| HMR | Hot Module Replacement trong dev server |
| Import map | Browser feature map bare imports sang URL |
| `modulepreload` | Hint browser preload module quan trọng |
