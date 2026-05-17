# 🏗️ Topic38: Build Tools - Vite vs Webpack vs Rollup, SWC vs Babel, Turbopack, esbuild

> Mục tiêu: hiểu đúng vai trò của build tools trong frontend hiện đại: dev server, bundler, compiler/transpiler, minifier, tree-shaking, code splitting, source maps, caching, performance budget và production debugging.

---

## ⭐ Senior/Staff Summary

Build tool không chỉ để “chạy React app”. Nó quyết định:

- ✅ Dev server nhanh hay chậm.
- ✅ HMR/Fast Refresh có ổn định không.
- ✅ Bundle production có nhỏ và cache tốt không.
- ✅ Tree-shaking có loại được dead code không.
- ✅ Code splitting có giảm initial load thật không.
- ✅ Source map có debug được production mà không leak source không.
- ✅ Monorepo/library/microfrontend có build được ổn định không.
- ✅ CI build có predictable và có performance budget không.

Mental model ngắn:

```txt
Source code
→ Parse dependency graph
→ Transform/transpile: TS/JSX/modern JS/CSS
→ Bundle/split chunks
→ Tree-shake/dead-code eliminate
→ Minify/compress
→ Hash assets for cache
→ Emit HTML/JS/CSS/assets/source maps
```

Chọn tool theo mục tiêu:

- **Vite**
  - ✅ Default tốt cho app React/Vue/Svelte hiện đại.
  - ✅ Dev nhanh nhờ native ESM + HMR; production build dùng Rollup/Rolldown ecosystem tùy version/config.
  - ⚠️ Cần hiểu khác biệt dev pipeline và production pipeline.

- **Webpack**
  - ✅ Mạnh cho app enterprise, legacy, customization sâu, Module Federation.
  - ✅ Ecosystem loader/plugin rất lớn.
  - ⚠️ Config phức tạp, dev speed thường cần tuning.

- **Rollup**
  - ✅ Rất tốt cho library/package.
  - ✅ Tree-shaking mạnh, output ESM/CJS/UMD rõ.
  - ⚠️ Không phải lựa chọn ergonomic nhất cho app lớn nếu tự setup từ đầu.

- **esbuild**
  - ✅ Cực nhanh cho transform, bundling, minify.
  - ✅ Dùng bên trong nhiều tool như Vite.
  - ⚠️ Plugin ecosystem và một số tối ưu nâng cao không rộng như Webpack/Rollup.

- **SWC**
  - ✅ Rust-based compiler nhanh cho TS/JSX/modern JS, minify.
  - ✅ Được dùng trong Next.js và nhiều stack build hiện đại.
  - ⚠️ Babel vẫn mạnh hơn nếu cần plugin transform tùy biến rất sâu.

- **Babel**
  - ✅ JavaScript compiler rất mature, plugin ecosystem cực lớn.
  - ✅ Tốt cho custom transforms, legacy browser, proposal plugins.
  - ⚠️ Chậm hơn SWC/esbuild trong nhiều case.

- **Turbopack**
  - ✅ Bundler incremental viết bằng Rust, tích hợp sâu với Next.js.
  - ✅ Hợp khi ở Next.js stack và muốn dev/build pipeline mới.
  - ⚠️ Không phải generic replacement cho mọi Webpack config ngoài Next.js.

> 💡 Key senior: **Tool nhanh nhất chưa chắc tốt nhất. Tool đúng là tool phù hợp constraint của app, team, ecosystem, deploy target và khả năng debug production.**

---

## 🧠 Key Mental Model

### 1. Tách vai trò: build tool không phải một thứ

Một frontend toolchain thường gồm nhiều vai trò:

- **Dev Server**
  - Serve source trong development.
  - HMR/Fast Refresh.
  - Proxy API.
  - Source map nhanh.

- **Bundler**
  - Đọc dependency graph.
  - Gộp module thành bundle/chunk.
  - Code splitting.
  - Tree-shaking.

- **Compiler / Transpiler**
  - TypeScript → JavaScript.
  - JSX/TSX → JavaScript.
  - Modern syntax → syntax tương thích target browser.

- **Minifier**
  - Xóa whitespace/comment.
  - Rename variable.
  - Dead-code elimination đơn giản.
  - Compress expression.

- **Optimizer**
  - Tree-shaking.
  - Chunk splitting.
  - Asset hashing.
  - CSS extraction/minification.
  - Dependency pre-bundling.

- **Quality Gates**
  - Type check.
  - ESLint/Prettier.
  - Bundle analyzer.
  - Performance budget.
  - Security scan.

---

### 2. Dev build khác production build

Development ưu tiên feedback loop:

- Fast startup.
- Fast rebuild.
- HMR/Fast Refresh.
- Source map dễ debug.
- Ít hoặc không minify.
- Ít optimization nặng.

Production ưu tiên runtime performance:

- Minification.
- Tree-shaking.
- Code splitting.
- Content hash.
- CSS extraction.
- Compression.
- Source maps có kiểm soát.
- Bundle budget.

> ⚠️ Không đánh giá tool chỉ bằng `npm run dev`. Phải đo cả `build`, bundle size, HMR stability, CI time và production runtime.

---

### 3. Dependency graph là nền tảng

Bundler bắt đầu từ entry points rồi đi theo imports để tạo dependency graph.

```ts
// main.tsx
import { createRoot } from 'react-dom/client';
import { App } from './App';
import './styles.css';

createRoot(document.getElementById('root')!).render(<App />);
```

Graph đơn giản:

```txt
main.tsx
├─ react-dom/client
├─ ./App
│  ├─ ./routes
│  └─ ./components/Button
└─ ./styles.css
```

Bundler dùng graph để:

- tìm module cần emit
- detect circular dependency
- split chunks
- remove unused exports
- resolve assets/CSS
- generate source map
- optimize cache invalidation

---

## 📚 Main Concepts

### 1. Bundling

`Bundling` là quá trình gom nhiều module/assets thành ít file hơn để browser tải hiệu quả.

Trước bundling:

```txt
100 modules
→ nhiều HTTP requests
→ khó minify/tree-shake đồng bộ
→ khó cache theo content hash
```

Sau bundling:

```txt
main.[hash].js
vendor.[hash].js
dashboard.[hash].js
styles.[hash].css
```

Senior note:

- HTTP/2/HTTP/3 giảm chi phí nhiều request, nhưng production vẫn thường cần bundle/split hợp lý.
- Bundle quá ít file có thể làm initial JS quá lớn.
- Bundle quá nhiều chunk có thể tăng waterfall.
- Cần đo bằng Performance panel, Lighthouse, WebPageTest, bundle analyzer.

---

### 2. Tree-shaking

`Tree-shaking` là loại bỏ unused exports/dead code khỏi bundle.

✅ Tốt cho tree-shaking:

```ts
// utils.ts
export function add(a: number, b: number) {
  return a + b;
}

export function subtract(a: number, b: number) {
  return a - b;
}

// app.ts
import { add } from './utils';

console.log(add(1, 2));
```

Bundler có thể bỏ `subtract` nếu chắc chắn không dùng.

⚠️ Kém hơn:

```ts
import * as utils from './utils';

console.log(utils.add(1, 2));
```

Hoặc CommonJS:

```ts
const { add } = require('./utils');
```

Key để tree-shaking tốt:

- dùng ESM imports/exports
- tránh side effects không rõ
- package khai báo `"sideEffects": false` đúng chỗ
- import theo subpath khi library không tree-shake tốt
- tránh barrel file export quá rộng nếu gây kéo module thừa

---

### 3. Side effects

Side effect là code chạy có tác động ngoài export value:

```ts
import './global.css';
import './polyfills';

window.analytics = createAnalyticsClient();
```

Nếu package khai báo sai:

```json
{
  "sideEffects": false
}
```

Bundler có thể xóa nhầm CSS/polyfill/global setup.

✅ Khai báo cẩn thận:

```json
{
  "sideEffects": ["*.css", "./src/polyfills.ts"]
}
```

---

### 4. Code splitting

`Code splitting` tách code thành nhiều chunks để giảm initial load.

React route-based splitting:

```tsx
import { Suspense, lazy } from 'react';
import { Route, Routes } from 'react-router-dom';

const HomePage = lazy(() => import('./pages/HomePage'));
const DashboardPage = lazy(() => import('./pages/DashboardPage'));
const SettingsPage = lazy(() => import('./pages/SettingsPage'));

export function AppRoutes() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/dashboard" element={<DashboardPage />} />
        <Route path="/settings" element={<SettingsPage />} />
      </Routes>
    </Suspense>
  );
}
```

✅ Dùng code splitting cho:

- routes ít vào
- dashboard/admin
- chart/editor/map libraries nặng
- modal flow hiếm dùng
- feature flags/experiments

⚠️ Không split quá nhỏ:

- tăng request waterfall
- UX loading nhiều nơi
- cache overhead
- dễ gặp `ChunkLoadError` khi deploy version mới

---

### 5. Minification

Minification giảm size JS/CSS:

```ts
function calculateTotal(price: number, quantity: number) {
  const tax = 0.1;
  return price * quantity * (1 + tax);
}
```

Sau minify có thể thành:

```js
function calculateTotal(t,n){return 1.1*t*n}
```

Tools:

- `Terser`: mature, output thường nhỏ, chậm hơn esbuild.
- `esbuild`: rất nhanh, output có thể hơi lớn hơn Terser tùy case.
- `SWC minify`: nhanh, dùng trong nhiều stack Rust-based.
- `cssnano`/Lightning CSS: CSS minification/optimization.

---

### 6. Transpiling và polyfills

Transpiling đổi syntax:

```ts
const double = (value: number) => value * 2;
```

Target cũ có thể thành:

```js
var double = function double(value) {
  return value * 2;
};
```

Polyfill thêm API runtime thiếu:

```ts
Promise.any(promises);
Array.prototype.at.call(items, -1);
```

Nếu browser target không hỗ trợ, cần polyfill như `core-js`.

Khác biệt:

- **Transpile**
  - Đổi syntax.
  - Ví dụ: arrow function, optional chaining, JSX.

- **Polyfill**
  - Thêm runtime API.
  - Ví dụ: `Promise`, `Array.prototype.includes`, `URLPattern`.

> ⚠️ Babel/SWC/esbuild không tự “thần kỳ” thêm mọi polyfill đúng cách nếu bạn không cấu hình target/polyfill strategy.

---

### 7. Source maps

Source map map code minified/transpiled về source gốc.

Development:

- cần nhanh
- debug dễ
- source map có thể inline/eval tùy tool

Production:

- cần debug error stack
- không nên public source map nếu source chứa logic nhạy cảm
- upload source maps lên Sentry/Datadog/private storage
- dùng hidden source map khi cần

Webpack example:

```js
module.exports = {
  devtool: process.env.NODE_ENV === 'production'
    ? 'hidden-source-map'
    : 'eval-source-map',
};
```

Vite example:

```ts
import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    sourcemap: true,
  },
});
```

---

### 8. Content hashing và caching

Production asset nên dùng content hash:

```txt
assets/main.3f9a12c8.js
assets/vendor.a8d91e2f.js
assets/styles.80ad12aa.css
```

Header thường dùng:

```nginx
location = /index.html {
  add_header Cache-Control "no-cache, no-store, must-revalidate";
}

location /assets/ {
  add_header Cache-Control "public, max-age=31536000, immutable";
}
```

Mental model:

- `index.html` không cache lâu vì nó trỏ đến asset version mới.
- JS/CSS/assets có content hash cache lâu vì nội dung đổi thì filename đổi.
- Vendor chunk ổn định giúp browser reuse cache qua nhiều deploy.

⚠️ Sai thường gặp:

- cache `index.html` quá lâu → user kẹt version cũ
- không dùng content hash → browser dùng JS cũ
- mỗi build làm vendor hash đổi dù code vendor không đổi → cache miss

---

## 🧰 Tool Comparison

### 1. Vite

Vite là build tool/dev server cho frontend hiện đại.

Điểm mạnh:

- Dev server nhanh nhờ native ESM.
- HMR/Fast Refresh tốt.
- Config đơn giản.
- Plugin ecosystem lớn vì tương thích nhiều pattern Rollup/Vite.
- Tốt cho React/Vue/Svelte apps.
- Production build có optimization/chunking tốt với Rollup/Rolldown ecosystem.

Điểm cần hiểu:

- Dev không bundle toàn bộ app theo kiểu Webpack truyền thống.
- Production vẫn cần bundling vì shipping unbundled nested ESM thường không tối ưu.
- TypeScript trong Vite chủ yếu transpile nhanh; type-check nên chạy `tsc --noEmit` riêng.

Vite config thực tế:

```ts
import react from '@vitejs/plugin-react';
import { defineConfig } from 'vite';
import { visualizer } from 'rollup-plugin-visualizer';

export default defineConfig(({ mode }) => ({
  plugins: [
    react(),
    mode === 'analyze' &&
      visualizer({
        filename: 'bundle-analysis.html',
        gzipSize: true,
        brotliSize: true,
      }),
  ].filter(Boolean),
  build: {
    sourcemap: true,
    minify: 'esbuild',
    chunkSizeWarningLimit: 700,
    rollupOptions: {
      output: {
        manualChunks: {
          react: ['react', 'react-dom'],
          charts: ['recharts'],
        },
      },
    },
  },
  server: {
    proxy: {
      '/api': 'http://localhost:3000',
    },
  },
}));
```

---

### 2. Webpack

Webpack là bundler cực kỳ linh hoạt và mature.

Điểm mạnh:

- Loader/plugin ecosystem lớn.
- Custom pipeline sâu.
- Module Federation cho microfrontends runtime.
- Hỗ trợ nhiều legacy app và enterprise constraints.
- Split chunks, runtime chunk, persistent cache, asset modules.

Điểm yếu:

- Config phức tạp hơn.
- Dev startup/rebuild có thể chậm nếu không tuning.
- Dễ tạo config khó maintain.

Webpack production example:

```js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  mode: 'production',
  entry: './src/main.tsx',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'assets/[name].[contenthash:8].js',
    chunkFilename: 'assets/[name].[contenthash:8].chunk.js',
    clean: true,
  },
  module: {
    rules: [
      {
        test: /\.[jt]sx?$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            cacheDirectory: true,
          },
        },
      },
    ],
  },
  optimization: {
    runtimeChunk: 'single',
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        react: {
          test: /[\\/]node_modules[\\/](react|react-dom)[\\/]/,
          name: 'react',
          priority: 20,
        },
        vendors: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          priority: 10,
        },
      },
    },
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './index.html',
      minify: true,
    }),
  ],
};
```

---

### 3. Rollup

Rollup rất mạnh cho library vì output sạch và tree-shaking tốt.

Phù hợp:

- Design system package.
- Component library.
- Utility library.
- SDK.
- Package cần emit ESM/CJS/types.

Rollup config library:

```ts
import typescript from '@rollup/plugin-typescript';
import { defineConfig } from 'rollup';

export default defineConfig({
  input: 'src/index.ts',
  output: [
    {
      file: 'dist/index.mjs',
      format: 'esm',
      sourcemap: true,
    },
    {
      file: 'dist/index.cjs',
      format: 'cjs',
      sourcemap: true,
      exports: 'named',
    },
  ],
  external: ['react', 'react-dom'],
  plugins: [typescript()],
});
```

Package config:

```json
{
  "name": "@acme/ui",
  "type": "module",
  "main": "./dist/index.cjs",
  "module": "./dist/index.mjs",
  "types": "./dist/index.d.ts",
  "sideEffects": ["*.css"],
  "peerDependencies": {
    "react": "^18 || ^19",
    "react-dom": "^18 || ^19"
  }
}
```

---

### 4. esbuild

esbuild là bundler/minifier/transpiler rất nhanh, viết bằng Go.

Phù hợp:

- Fast transform.
- Bundling scripts/tools nhỏ.
- Minify nhanh.
- Dev pipeline.
- Pre-bundling dependencies.
- Internal tooling.

esbuild script:

```ts
import * as esbuild from 'esbuild';

await esbuild.build({
  entryPoints: ['src/main.tsx'],
  bundle: true,
  minify: true,
  sourcemap: true,
  splitting: true,
  format: 'esm',
  outdir: 'dist',
  target: ['es2020'],
  define: {
    'process.env.NODE_ENV': '"production"',
  },
});
```

Cẩn thận:

- TypeScript type-check không phải nhiệm vụ chính của esbuild.
- Plugin ecosystem nhỏ hơn Webpack/Rollup.
- Một số transform/polyfill nâng cao vẫn cần Babel/SWC/tool khác.

---

### 5. SWC vs Babel

SWC và Babel đều transform JavaScript/TypeScript/JSX, nhưng tradeoff khác nhau.

- **SWC**
  - Rust-based, nhanh.
  - Tốt cho transpile/minify ở Next.js hoặc toolchain hiện đại.
  - Phù hợp khi cần performance và transform phổ biến.

- **Babel**
  - Mature nhất về plugin ecosystem.
  - Tốt cho custom transforms/codemods/proposals/legacy.
  - Phù hợp khi project phụ thuộc plugin Babel cụ thể.

Babel config:

```json
{
  "presets": [
    ["@babel/preset-env", { "targets": ">0.5%, not dead" }],
    ["@babel/preset-react", { "runtime": "automatic" }],
    "@babel/preset-typescript"
  ]
}
```

SWC config:

```json
{
  "jsc": {
    "parser": {
      "syntax": "typescript",
      "tsx": true
    },
    "transform": {
      "react": {
        "runtime": "automatic"
      }
    },
    "target": "es2020"
  },
  "minify": true,
  "sourceMaps": true
}
```

Decision:

- Cần plugin Babel đặc thù → Babel.
- Cần speed và transform phổ biến → SWC/esbuild.
- Dùng Next.js → ưu tiên SWC/Turbopack defaults trừ khi có lý do rõ.

---

### 6. Turbopack

Turbopack là bundler incremental viết bằng Rust, tích hợp sâu với Next.js.

Phù hợp:

- Next.js app.
- Dev server/HMR với project lớn.
- Team muốn theo toolchain mặc định mới của Next.js.
- App không phụ thuộc quá nhiều Webpack-specific plugin/loader khó migrate.

Cẩn thận:

- Không assume mọi Webpack plugin đều tương thích.
- Với app enterprise, cần test build/dev parity, CSS pipeline, MDX, aliases, monorepo packages.
- Đo thực tế trên repo của mình thay vì tin benchmark chung.

Next.js scripts:

```json
{
  "scripts": {
    "dev": "next dev --turbopack",
    "build": "next build",
    "start": "next start"
  }
}
```

---

### 7. Rspack, Rolldown, Bun, Parcel

Senior frontend không cần thuộc mọi tool, nhưng nên biết landscape:

- **Rspack**
  - Rust-based bundler, Webpack-compatible direction.
  - Hợp khi muốn tăng speed nhưng vẫn cần Webpack-like ecosystem.

- **Rolldown**
  - Rust-based bundler lấy cảm hứng/tương thích Rollup ecosystem.
  - Đang ảnh hưởng mạnh đến hướng đi của Vite ecosystem.

- **Bun bundler**
  - Nhanh, nằm trong Bun runtime/toolchain.
  - Hợp nếu stack đã chọn Bun và constraints phù hợp.

- **Parcel**
  - Zero-config bundler, phù hợp project cần setup nhanh.

---

## 🧪 Practical TypeScript/JavaScript Examples

### Example 1: Package scripts production-friendly

```json
{
  "scripts": {
    "dev": "vite",
    "type-check": "tsc --noEmit",
    "lint": "eslint .",
    "format:check": "prettier . --check",
    "build": "npm run type-check && npm run lint && vite build",
    "build:analyze": "vite build --mode analyze",
    "preview": "vite preview"
  }
}
```

Ý nghĩa:

- `vite` transpile nhanh trong dev.
- `tsc --noEmit` bắt type error thật.
- `eslint` bắt bug pattern.
- `build:analyze` kiểm tra bundle size.
- `preview` test production build local.

---

### Example 2: Dynamic import cho chart nặng

```tsx
import { Suspense, lazy, useState } from 'react';

const RevenueChart = lazy(() => import('./RevenueChart'));

export function Dashboard() {
  const [showChart, setShowChart] = useState(false);

  return (
    <section>
      <button type="button" onClick={() => setShowChart(true)}>
        Show chart
      </button>

      {showChart && (
        <Suspense fallback={<div>Loading chart...</div>}>
          <RevenueChart />
        </Suspense>
      )}
    </section>
  );
}
```

✅ Chart library không nằm trong initial bundle.

⚠️ Cần UX fallback tốt; đừng để người dùng click rồi màn hình đứng im.

---

### Example 3: Handle `ChunkLoadError`

Khi deploy version mới, user đang mở tab cũ có thể request chunk cũ đã bị xóa khỏi CDN.

```ts
window.addEventListener('error', (event) => {
  const message = event.message || '';

  if (message.includes('Loading chunk') || message.includes('ChunkLoadError')) {
    window.location.reload();
  }
});
```

Production tốt hơn:

- giữ old assets trên CDN một thời gian
- deploy immutable assets trước, HTML sau
- có error boundary cho lazy routes
- track `ChunkLoadError` bằng Sentry/Datadog

---

### Example 4: Import để tree-shaking tốt hơn

❌ Dễ kéo nhiều code:

```ts
import _ from 'lodash';

const ids = _.uniq(items.map((item) => item.id));
```

✅ Tốt hơn:

```ts
import uniq from 'lodash/uniq';

const ids = uniq(items.map((item) => item.id));
```

Hoặc dùng native API nếu đủ:

```ts
const ids = [...new Set(items.map((item) => item.id))];
```

---

### Example 5: Bundle analyzer

Vite:

```ts
import { visualizer } from 'rollup-plugin-visualizer';

export default defineConfig({
  plugins: [
    visualizer({
      filename: 'bundle-analysis.html',
      gzipSize: true,
      brotliSize: true,
    }),
  ],
});
```

Webpack:

```js
const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');

module.exports = {
  plugins: [
    new BundleAnalyzerPlugin({
      analyzerMode: 'static',
      reportFilename: 'bundle-report.html',
    }),
  ],
};
```

Đọc report để tìm:

- library quá lớn
- duplicate dependency
- moment/lodash import sai
- chart/editor/map nằm trong initial bundle
- vendor chunk đổi hash quá thường xuyên

---

### Example 6: Performance budget bằng `size-limit`

```json
{
  "size-limit": [
    {
      "path": "dist/assets/*.js",
      "limit": "220 KB"
    }
  ],
  "scripts": {
    "size": "size-limit",
    "build": "vite build && npm run size"
  }
}
```

✅ Fail build khi JS vượt budget giúp team không “vô tình” ship thêm 500KB.

---

### Example 7: Module Federation với Webpack

```js
const { ModuleFederationPlugin } = require('webpack').container;

module.exports = {
  plugins: [
    new ModuleFederationPlugin({
      name: 'checkout',
      filename: 'remoteEntry.js',
      exposes: {
        './CheckoutApp': './src/CheckoutApp',
      },
      shared: {
        react: { singleton: true, requiredVersion: '^18.0.0' },
        'react-dom': { singleton: true, requiredVersion: '^18.0.0' },
      },
    }),
  ],
};
```

Use case:

- microfrontend runtime integration
- independent deploy
- shared dependency

⚠️ Tradeoffs:

- runtime failure mode phức tạp
- version mismatch
- observability/debug khó hơn
- security boundary cần rõ

---

## ⚛️ Production Notes / React Implications

### React build không chỉ là compile JSX

React production cần:

- JSX transform đúng.
- Fast Refresh trong dev.
- Production mode loại dev warnings.
- Code splitting theo route/component.
- Lazy chunk có fallback UX tốt.
- Error boundary cho lazy-loaded UI.
- Source maps đủ để debug stack trace.

---

### TypeScript với build tools

Nhiều tool transpile TypeScript nhưng không type-check đầy đủ trong dev/build nhanh.

✅ Setup nên có:

```json
{
  "scripts": {
    "type-check": "tsc --noEmit",
    "build": "npm run type-check && vite build"
  }
}
```

⚠️ Nếu chỉ dựa vào esbuild/SWC transpile, type error có thể lọt CI nếu không chạy `tsc`.

---

### CSS pipeline

Build tool còn xử lý CSS:

- CSS Modules.
- PostCSS.
- Autoprefixer.
- Tailwind.
- CSS extraction.
- CSS minification.
- Critical CSS/SSR style order.

Production pitfalls:

- CSS import bị tree-shake sai do `sideEffects: false`.
- CSS order khác dev/prod.
- Tailwind content config sai làm purge nhầm class.
- CSS source map public leak source path.

---

### SSR / Next.js

SSR framework như Next.js có build pipeline riêng:

- client bundle
- server bundle
- React Server Components payload
- route chunks
- image/font optimization
- edge/server runtime targets

Guideline:

- Ưu tiên framework default trước.
- Chỉ override Webpack/Turbopack config khi có lý do rõ.
- Kiểm tra server/client boundary khi import package browser-only.
- Bundle analyze cả client và server.

---

### Monorepo

Monorepo thêm constraints:

- package transpilation
- symlink resolution
- duplicate React
- shared TS config
- incremental build/cache
- dependency graph workspace-level

Checklist:

- đảm bảo chỉ có một React instance
- externalize peer dependencies cho libraries
- build packages theo dependency order
- dùng Nx/Turborepo/pnpm workspace nếu cần task cache
- tránh import source vượt boundary không kiểm soát

---

### Security

Build pipeline có rủi ro security:

- Public source maps leak source.
- Inject env vars nhầm vào client bundle.
- Dependency supply-chain attack.
- CDN asset bị thay đổi nếu không dùng SRI ở script ngoài.
- HTML minify/injection sai có thể ảnh hưởng CSP.

Checklist:

- chỉ expose env prefix public như `VITE_`/`NEXT_PUBLIC_`
- upload hidden source maps lên monitoring, không public nếu source nhạy cảm
- lockfile và dependency audit
- CSP cho script/style
- SRI cho third-party scripts

---

### Observability & debugging

Production build nên hỗ trợ debug:

- source maps riêng tư
- release id/commit SHA trong build
- bundle analyzer artifact trong CI
- Web Vitals reporting
- error tracking source map upload
- performance marks cho critical flow

```ts
performance.mark('app:start');

// bootstrap app

performance.mark('app:mounted');
performance.measure('app-bootstrap', 'app:start', 'app:mounted');
```

---

## ⚠️ Common Pitfalls

### ❌ 1. Nghĩ Vite dev nhanh nghĩa là production tự tối ưu hoàn hảo

Dev speed và production bundle quality là hai thứ khác nhau.

✅ Luôn kiểm tra:

- bundle analyzer
- chunk size
- source map
- cache headers
- route loading waterfall

---

### ❌ 2. Không chạy type-check

esbuild/SWC thường transpile rất nhanh nhưng không thay thế `tsc --noEmit`.

---

### ❌ 3. Import sai làm bundle phình

```ts
import moment from 'moment';
import _ from 'lodash';
```

✅ Cân nhắc:

- native API
- `date-fns`
- subpath import
- lighter alternatives
- bundle analyzer trước khi quyết định

---

### ❌ 4. Public production source maps không kiểm soát

Source maps giúp debug nhưng có thể leak source.

✅ Upload lên monitoring/private storage nếu cần.

---

### ❌ 5. Cache sai `index.html`

Nếu `index.html` cache lâu, user có thể bị kẹt version cũ.

✅ HTML fresh, assets hashed cache long-term.

---

### ❌ 6. Code splitting quá mức

Split mọi component thành chunk riêng có thể làm UX tệ vì waterfall.

✅ Split theo route/feature nặng, không split vô tội vạ.

---

### ❌ 7. Quên xử lý deploy race với chunks

User mở app cũ, deploy mới xóa old chunks → lazy import fail.

✅ Giữ old assets hoặc handle reload/error boundary.

---

### ❌ 8. Dùng Babel plugin cũ khi đã chuyển SWC/esbuild

Không phải mọi Babel plugin đều chạy trong SWC/esbuild.

✅ Audit plugin compatibility trước khi migrate.

---

### ❌ 9. Override framework config quá nhiều

Next/Vite đã có default tốt. Override sâu dễ phá optimization.

✅ Override ít, đo rõ, document lý do.

---

## ✅ Decision Guide / Checklist

### Chọn tool theo tình huống

- React/Vue/Svelte app mới:
  - ✅ Vite

- Next.js app:
  - ✅ Next.js default pipeline
  - ✅ Turbopack nếu phù hợp version/config và đã test thực tế

- Enterprise legacy app/custom loader/plugin sâu:
  - ✅ Webpack
  - ✅ cân nhắc Rspack nếu muốn compatibility + speed

- Library/package/design system:
  - ✅ Rollup
  - ✅ tsup/unbuild/esbuild nếu package đơn giản

- Microfrontend runtime sharing:
  - ✅ Webpack Module Federation
  - ✅ cân nhắc framework-specific federation nếu stack hỗ trợ

- Transform nhanh TS/JSX:
  - ✅ SWC hoặc esbuild

- Custom syntax transform/codemod/plugin ecosystem:
  - ✅ Babel

---

### Build review checklist

- ✅ Có type-check riêng không?
- ✅ Có lint/format trong CI không?
- ✅ Bundle analyzer có chạy định kỳ không?
- ✅ Initial JS có budget không?
- ✅ Route chunks có hợp lý không?
- ✅ Vendor chunk có cache ổn định không?
- ✅ `index.html` có cache đúng không?
- ✅ Assets có content hash không?
- ✅ Source maps có strategy bảo mật không?
- ✅ Env vars client có bị leak không?
- ✅ CSS side effects có được giữ không?
- ✅ Legacy browser target/polyfill strategy rõ không?
- ✅ Dynamic import có fallback/error boundary không?
- ✅ Monorepo có tránh duplicate React không?

---

## 🗣️ Short Interview Answer

Em nghĩ build tools nên được nhìn theo vai trò chứ không chỉ theo tên tool. Một toolchain thường có dev server, bundler, transpiler/compiler, minifier, source map, cache hashing và quality gates như type-check, lint, bundle budget. Vite mạnh ở dev experience vì dùng native ESM và HMR nhanh, production thì vẫn cần bundling và chunk optimization. Webpack mạnh ở ecosystem, legacy app, customization sâu và Module Federation. Rollup thì em thường chọn cho library vì output sạch và tree-shaking tốt.

Về compiler, em chọn SWC hoặc esbuild khi cần tốc độ cho transform phổ biến, còn Babel khi project cần plugin ecosystem hoặc custom transform đặc thù. Với Next.js thì em ưu tiên default pipeline, Turbopack nếu stack phù hợp và đo thực tế trên repo, chứ không chỉ tin benchmark.

Điểm em thấy quan trọng ở senior level là phải đo production chứ không chỉ nhìn dev server nhanh. Em sẽ kiểm tra bundle analyzer, code splitting, content hash/cache headers, source map strategy, type-check riêng, env var leak, và performance budget trong CI. Build tool tốt là tool giúp team ship nhanh nhưng vẫn kiểm soát được runtime performance, caching, debugging và maintainability.

---

## 🧠 Ghi nhớ nhanh

- ✅ Vite mạnh cho app hiện đại và DX nhanh.
- ✅ Webpack mạnh cho customization sâu, enterprise, Module Federation.
- ✅ Rollup mạnh cho library và tree-shaking.
- ✅ esbuild rất nhanh cho transform/bundle/minify.
- ✅ SWC nhanh, hợp stack hiện đại/Next.js.
- ✅ Babel mature nhất về plugin ecosystem.
- ✅ Turbopack phù hợp nhất trong Next.js context.
- ✅ Dev build khác production build.
- ✅ TypeScript transpile không thay thế `tsc --noEmit`.
- ✅ Tree-shaking cần ESM và side effects rõ.
- ✅ Code splitting phải theo UX, không split quá nhỏ.
- ✅ Source maps production cần strategy bảo mật.
- ✅ `index.html` không cache lâu; hashed assets cache lâu.
- ✅ Bundle analyzer và performance budget nên nằm trong CI.

---

## 📖 Giải thích các thuật ngữ trong topic

- **Build Tool**
  - Công cụ xử lý source code thành output chạy được trong browser/production.

- **Dev Server**
  - Server development hỗ trợ HMR, proxy, source maps và rebuild nhanh.

- **Bundler**
  - Công cụ đọc dependency graph và xuất bundle/chunks.

- **Dependency Graph**
  - Sơ đồ quan hệ import/export giữa modules.

- **Bundle**
  - File JS/CSS output chứa nhiều modules đã được xử lý.

- **Chunk**
  - Một phần bundle được tách riêng để load theo nhu cầu hoặc cache tốt hơn.

- **Code Splitting**
  - Tách code thành chunks, thường qua dynamic `import()`.

- **Tree-shaking**
  - Loại bỏ unused exports/dead code khỏi bundle.

- **Side Effect**
  - Code có tác động ngoài export value, ví dụ import CSS, polyfill, mutate global.

- **Minification**
  - Nén code để giảm size bằng cách xóa whitespace, đổi tên biến, rút gọn expression.

- **Transpiling**
  - Chuyển syntax hiện đại/TS/JSX sang JavaScript target.

- **Polyfill**
  - Code thêm runtime API thiếu trong browser cũ.

- **Source Map**
  - File map code output về source gốc để debug.

- **HMR**
  - Hot Module Replacement: cập nhật module khi dev mà không reload toàn trang.

- **Fast Refresh**
  - Cơ chế React giữ state khi update component trong dev.

- **Content Hash**
  - Hash dựa trên nội dung file, dùng cho cache busting.

- **Cache Busting**
  - Kỹ thuật đổi filename khi nội dung đổi để browser tải bản mới.

- **Vendor Chunk**
  - Chunk chứa thư viện bên thứ ba như React, lodash, chart library.

- **Performance Budget**
  - Giới hạn size/time để build fail hoặc warning khi vượt.

- **Vite**
  - Dev server/build tool hiện đại, nổi bật với native ESM dev và HMR nhanh.

- **Webpack**
  - Bundler mature, linh hoạt, ecosystem loader/plugin lớn.

- **Rollup**
  - JavaScript module bundler mạnh cho library và tree-shaking.

- **esbuild**
  - Bundler/minifier/transpiler rất nhanh viết bằng Go.

- **SWC**
  - Rust-based compiler/toolchain cho JavaScript/TypeScript.

- **Babel**
  - JavaScript compiler mature với plugin ecosystem lớn.

- **Turbopack**
  - Incremental bundler viết bằng Rust, tích hợp với Next.js.

- **Module Federation**
  - Webpack feature cho phép nhiều build độc lập chia sẻ/expose module runtime.

- **Differential Serving**
  - Phục vụ bundle khác nhau cho browser hiện đại và legacy.

- **SRI**
  - Subresource Integrity, đảm bảo third-party script không bị thay đổi ngoài ý muốn.

---

## 🔗 Nguồn tham khảo chính thức

- Vite docs: https://vite.dev/guide/why.html
- Webpack tree-shaking: https://webpack.js.org/guides/tree-shaking/
- Webpack code splitting: https://webpack.js.org/guides/code-splitting/
- Webpack Module Federation: https://webpack.js.org/concepts/module-federation/
- Rollup docs: https://rollupjs.org/
- Babel docs: https://babel.dev/docs/
- SWC repository/docs entry: https://github.com/swc-project/swc
- Next.js Turbopack docs: https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack
