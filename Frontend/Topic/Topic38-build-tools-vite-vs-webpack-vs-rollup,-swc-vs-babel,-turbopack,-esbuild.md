# Topic 38: Build Tools - Vite vs Webpack vs Rollup, SWC vs Babel, Turbopack, esbuild

## 🚀 Câu trả lời ngắn gọn

Build tools trong frontend có thể chia thành 3 nhóm chính:

```txt
📦 Bundler: gom module thành bundle chạy trên browser
⚙️ Compiler/Transpiler: đổi TS/JSX/modern JS thành JS browser hiểu
🧹 Minifier/Optimizer: nén, tree-shaking, code splitting, optimize asset
```

Các tool quan trọng:

```txt
🏗️ Webpack   -> bundler trưởng thành, rất linh hoạt, config phức tạp
⚡ Vite      -> dev server rất nhanh, production dùng Rollup
📦 Rollup    -> mạnh cho library build, ESM và tree-shaking tốt
🚀 esbuild   -> Go-based, cực nhanh cho transform/bundle cơ bản
🦀 SWC       -> Rust-based compiler, thay Babel trong nhiều case
🐢 Babel     -> JS compiler/plugin ecosystem lớn nhất, chậm hơn SWC
🌪️ Turbopack -> Rust incremental bundler, tập trung vào Next.js
🧰 Rspack    -> Rust bundler tương thích Webpack ecosystem
```

**Highlight senior/staff:** Không chọn tool chỉ vì “nhanh”. Phải hỏi:

```txt
App hay library?
Dev speed hay production optimization?
Legacy hay greenfield?
Framework nào?
Cần plugin đặc biệt không?
Monorepo lớn không?
SSR/Next.js không?
Cần Module Federation không?
```

---

## 🧠 1. Mental model: Bundler vs Compiler

### 📦 Bundler làm gì?

Bundler đọc dependency graph từ entry file rồi đóng gói thành output cho browser.

Ví dụ:

```txt
src/main.tsx
 -> App.tsx
 -> Button.tsx
 -> styles.css
 -> logo.svg
```

Bundler xử lý:

- module resolution
- code splitting
- tree-shaking
- asset handling
- CSS bundling
- dynamic import
- production chunking

### ⚙️ Compiler/transpiler làm gì?

Compiler/transpiler đổi syntax mới thành syntax browser hiểu.

Ví dụ:

```tsx
const App = () => <h1>Hello</h1>;
```

Có thể được transform thành JS thường.

Tool:

```txt
Babel -> JS-based, plugin cực mạnh
SWC   -> Rust-based, nhanh hơn nhiều trong đa số case
esbuild -> Go-based, transform rất nhanh
```

### 🧩 Một tool có thể làm nhiều việc

Ví dụ:

- Vite là dev server/build tool, dev dùng native ESM + esbuild, prod dùng Rollup.
- esbuild vừa transform vừa bundle cơ bản.
- Turbopack vừa bundler vừa dev server hướng incremental.
- Webpack bundling mạnh nhưng thường cần Babel/SWC loader để transform.

---

## ⚖️ 2. Bảng so sánh nhanh

| Tool | Vai trò chính | Mạnh nhất ở đâu | Điểm yếu |
|---|---|---|---|
| 🏗️ Webpack | Bundler | Legacy/enterprise/custom pipeline | Chậm hơn, config phức tạp |
| ⚡ Vite | Dev server + build tool | Dev experience, app mới | Prod khác dev vì dùng Rollup |
| 📦 Rollup | Bundler | Library build, ESM, tree-shaking | App phức tạp cần config thêm |
| 🚀 esbuild | Bundler/transformer | Tốc độ transform/build | Plugin/optimization chưa sâu như Webpack/Rollup |
| 🦀 SWC | Compiler | Thay Babel, nhanh | Plugin ecosystem ít hơn Babel |
| 🐢 Babel | Compiler | Plugin ecosystem, compatibility | Chậm |
| 🌪️ Turbopack | Incremental bundler | Next.js dev, incremental rebuild | Ecosystem/maturity cần cân nhắc |
| 🧰 Rspack | Webpack-compatible bundler | Webpack migration cần tốc độ | Mới hơn Webpack |

> **Highlight:** Vite nhanh trong dev không có nghĩa production build “là Vite”. Production của Vite chủ yếu dùng **Rollup**.

---

## 🏗️ 3. Webpack

Webpack là bundler lâu đời, cực kỳ linh hoạt và có ecosystem plugin/loader rất lớn.

### ✅ Điểm mạnh

- Rất mature, dùng nhiều trong enterprise.
- Config được gần như mọi pipeline phức tạp.
- Plugin ecosystem lớn.
- Code splitting/chunk optimization rất mạnh.
- Module Federation phổ biến nhất trong Webpack ecosystem.
- Phù hợp legacy app lớn đã dùng Webpack.

### ⚠️ Điểm yếu

- Cold start và rebuild thường chậm hơn Vite/Turbopack/Rspack.
- Config phức tạp: loaders, plugins, optimization, cache.
- Dev experience có thể kém nếu app lớn.
- Migration/upgrade lớn có thể tốn chi phí.

### 🎯 Khi dùng Webpack?

```txt
✅ App enterprise/legacy đang dùng Webpack ổn định
✅ Cần custom build pipeline rất đặc biệt
✅ Cần Module Federation mature
✅ Cần plugin/loader chỉ Webpack có
```

Không nên migrate khỏi Webpack chỉ vì “tool mới nhanh hơn” nếu chi phí/rủi ro lớn hơn lợi ích.

---

## ⚡ 4. Vite

Vite tối ưu mạnh cho dev experience.

### 🔥 Vì sao Vite dev nhanh?

Webpack dev thường bundle nhiều thứ trước khi serve. Vite dev dùng browser native ESM:

```txt
Browser request module nào -> Vite transform module đó -> trả về ngay
```

Vite chia code thành:

```txt
📦 Dependencies: pre-bundle bằng esbuild
🧑‍💻 Source code: serve qua native ESM, transform on-demand
```

Khi sửa một file, HMR chỉ cần update module liên quan, không re-bundle toàn bộ app.

### ✅ Điểm mạnh

- Dev server start rất nhanh.
- HMR nhanh.
- Config đơn giản.
- Dùng tốt cho React, Vue, Svelte, vanilla.
- Ecosystem hiện đại.
- Production dùng Rollup nên output tốt.

### ⚠️ Điểm yếu

- Dev và prod không giống 100%: dev native ESM, prod Rollup bundle.
- Một số dependency CJS/legacy có thể gây issue.
- App cực lớn/monorepo phức tạp vẫn cần tối ưu cache/deps.
- Module Federation không mature bằng Webpack trong nhiều setup.

### 🎯 Khi dùng Vite?

```txt
✅ Greenfield React/Vue/Svelte app
✅ SPA/dashboard/internal tool
✅ Muốn dev speed tốt, config đơn giản
✅ Không bị ràng buộc plugin Webpack đặc biệt
```

> **Highlight:** Với app frontend mới không dùng Next.js, Vite thường là lựa chọn mặc định tốt.

---

## 📦 5. Rollup

Rollup tập trung vào ESM, tree-shaking và output sạch.

### ✅ Điểm mạnh

- Tree-shaking tốt.
- Output nhỏ, sạch, phù hợp package npm.
- Build library tốt: ESM, CJS, UMD.
- Plugin ecosystem ổn.
- Được Vite dùng cho production build.

### ⚠️ Điểm yếu

- Dev server/HMR không phải điểm mạnh chính.
- App lớn nhiều asset/code splitting phức tạp cần setup thêm.
- Không linh hoạt bằng Webpack trong một số enterprise pipeline.

### 🎯 Khi dùng Rollup?

```txt
✅ Build thư viện npm/component library
✅ Package cần ESM/CJS output
✅ Muốn tree-shaking tốt
✅ Muốn output nhỏ và sạch
```

Ví dụ:

```txt
Design system package -> Rollup
Shared utility library -> Rollup
React component library -> Rollup / tsup
```

---

## 🚀 6. esbuild

esbuild viết bằng Go, nổi tiếng vì tốc độ rất cao.

### ✅ Điểm mạnh

- Transform TS/JS/JSX cực nhanh.
- Bundle cơ bản nhanh.
- Minify nhanh.
- Dùng tốt trong toolchain khác như Vite pre-bundling.
- Phù hợp scripts, CLIs, simple build.

### ⚠️ Điểm yếu

- Plugin ecosystem ít hơn Webpack/Rollup.
- Một số transform nâng cao không linh hoạt bằng Babel.
- Code splitting/optimization không sâu bằng bundler chuyên dụng trong app phức tạp.
- Không type-check TypeScript, chỉ transpile.

### 🎯 Khi dùng esbuild?

```txt
✅ Build script/CLI/tool nội bộ
✅ Transform TS/JS nhanh
✅ Pre-bundle dependencies
✅ Project nhỏ cần build nhanh
```

> **Highlight:** esbuild rất nhanh, nhưng “nhanh” không đồng nghĩa “đủ mọi optimization production phức tạp”.

---

## 🦀 7. SWC vs 🐢 Babel

### 🐢 Babel

Babel là JS compiler rất mature.

Điểm mạnh:

- Plugin ecosystem lớn nhất.
- Hỗ trợ nhiều syntax/proposal.
- Dễ custom transform.
- Tương thích nhiều tool cũ.

Điểm yếu:

- Chậm hơn SWC/esbuild.
- Config/plugin nhiều dễ phức tạp.

### 🦀 SWC

SWC viết bằng Rust, thường dùng để thay Babel trong Next.js hoặc app cần build nhanh.

Điểm mạnh:

- Nhanh hơn Babel nhiều trong đa số case.
- Hỗ trợ TS/JSX tốt.
- Dùng trong Next.js compiler.
- Phù hợp monorepo/app lớn muốn giảm build time.

Điểm yếu:

- Plugin ecosystem không rộng bằng Babel.
- Một số Babel plugin custom chưa migrate được.
- Nếu project phụ thuộc plugin Babel đặc biệt, migration cần kiểm tra kỹ.

### 🎯 Chọn SWC hay Babel?

```txt
✅ Dùng SWC khi:
- cần build nhanh
- không phụ thuộc Babel plugin đặc biệt
- dùng Next.js hoặc framework đã tích hợp SWC

✅ Dùng Babel khi:
- cần plugin custom
- cần compatibility đặc biệt
- codebase cũ đã phụ thuộc Babel ecosystem
```

> **Highlight:** SWC thay Babel tốt cho performance, nhưng Babel vẫn thắng ở plugin ecosystem.

---

## 🌪️ 8. Turbopack

Turbopack là bundler viết bằng Rust, được thiết kế như successor của Webpack trong hệ sinh thái Next.js.

### 🔥 Điểm mạnh

- Incremental bundling.
- Cache dependency graph.
- Rebuild/HMR nhanh trong app lớn.
- Tích hợp sâu với Next.js.
- Hướng tới scale tốt hơn khi project lớn.

### ⚠️ Điểm cần cân nhắc

- Maturity và plugin ecosystem cần kiểm tra theo version framework.
- Chủ yếu phù hợp Next.js.
- Không phải lựa chọn mặc định cho mọi non-Next app.
- Production behavior/support cần đánh giá theo framework/version đang dùng.

### 🎯 Khi dùng Turbopack?

```txt
✅ Next.js app
✅ Muốn dev server/HMR nhanh hơn
✅ App lớn, nhiều module
✅ Framework đã support ổn trong version hiện tại
```

---

## 🧰 9. Rspack

Rspack là bundler viết bằng Rust, hướng tới tương thích Webpack API/ecosystem.

### ✅ Điểm mạnh

- Nhanh hơn Webpack trong nhiều case.
- Tương thích nhiều config/plugin Webpack.
- Hữu ích khi muốn tăng tốc nhưng không rewrite toàn bộ build pipeline.
- Có thể phù hợp migration enterprise từ Webpack.

### ⚠️ Điểm cần cân nhắc

- Không phải mọi plugin Webpack đều tương thích 100%.
- Cần test kỹ production build, CSS/assets, Module Federation, sourcemap.
- Ecosystem vẫn mới hơn Webpack.

### 🎯 Khi dùng Rspack?

```txt
✅ Đang có Webpack app lớn
✅ Muốn cải thiện build/dev speed
✅ Không muốn migrate sang Vite hoàn toàn
✅ Cần giữ nhiều Webpack concepts/config
```

---

## 🧩 10. Dev build vs Production build

Senior cần phân biệt rõ dev và production.

### Dev build cần gì?

```txt
⚡ Fast cold start
⚡ Fast HMR
🧭 Good source maps
🔁 Stable watch mode
🧠 Ít config để dev tập trung code
```

### Production build cần gì?

```txt
📦 Bundle size nhỏ
🧹 Tree-shaking tốt
✂️ Code splitting tốt
🗜️ Minification tốt
🧊 Long-term caching/content hash
📊 Bundle analysis
🧯 Source map strategy an toàn
```

> **Highlight:** Một tool dev nhanh chưa chắc production tối ưu nhất. Staff engineer phải đo cả dev speed, build speed, bundle size, cache hit và runtime performance.

---

## 🌳 11. Tree-shaking, code splitting, minification

### 🌳 Tree-shaking

Loại bỏ code không dùng.

Điều kiện để tree-shaking tốt:

- dùng ESM `import/export`
- package khai báo `sideEffects` đúng
- tránh import toàn bộ thư viện lớn

Không tốt:

```ts
import _ from 'lodash';
```

Tốt hơn:

```ts
import debounce from 'lodash/debounce';
```

### ✂️ Code splitting

Chia bundle theo route hoặc feature.

```ts
const SettingsPage = lazy(() => import('./SettingsPage'));
```

Mục tiêu:

```txt
Initial JS nhỏ hơn
Route sau load khi cần
Vendor chunk cache tốt hơn
```

### 🗜️ Minification

Nén JS/CSS để giảm size.

Tool thường gặp:

```txt
Terser
esbuild minify
SWC minify
Lightning CSS
```

---

## 🧭 12. Decision framework

### Chọn theo use case

```txt
🆕 App React/Vue mới        -> Vite
📦 Library npm              -> Rollup / tsup
🏢 Legacy enterprise app    -> Webpack hoặc Rspack
⚛️ Next.js app              -> Next compiler + Turbopack/SWC theo framework
⚡ Script/CLI build nhanh    -> esbuild / tsup
🔌 Cần Babel plugin đặc biệt -> Babel
🦀 Muốn thay Babel cho nhanh -> SWC
🧩 Microfrontend mature      -> Webpack Module Federation / Rspack nếu phù hợp
```

### Câu hỏi cần hỏi trước khi đổi tool

```txt
1. Bottleneck thật là gì: cold start, HMR, prod build, bundle size hay runtime?
2. Tool mới có support framework/plugin hiện tại không?
3. Có SSR, Module Federation, CSS modules, asset pipeline đặc biệt không?
4. Source map, test, CI/CD, deploy có bị ảnh hưởng không?
5. Có thể migrate từng phần không?
6. Có đo baseline trước/sau không?
```

---

## 📊 13. Metrics cần đo

Không nên nói “tool A nhanh hơn tool B” nếu không đo.

Nên đo:

```txt
⏱️ cold start time
🔥 HMR update time
🏗️ production build time
📦 initial JS size
✂️ chunk count/chunk size
🧊 cache hit rate
🧭 source map quality
🚦 Lighthouse/Web Vitals
🧪 CI time
```

Với monorepo:

```txt
affected build/test time
remote cache hit
incremental build performance
dependency graph size
```

---

## 🚨 14. Common mistakes

### ⚠️ Chỉ chọn tool vì benchmark

Benchmark nhỏ không phản ánh app thật. App thật có CSS, assets, legacy deps, plugins, SSR, tests, CI.

### ⚠️ Nghĩ Vite prod cũng giống Vite dev

Vite dev dùng native ESM/on-demand transform. Vite production dùng Rollup bundle.

### ⚠️ Nghĩ SWC/esbuild type-check TypeScript

SWC/esbuild chủ yếu transpile. Type-check vẫn cần:

```txt
tsc --noEmit
```

Hoặc framework/plugin type-check riêng.

### ⚠️ Migration không đo baseline

Trước khi migrate phải đo:

```txt
dev start
HMR
build time
bundle size
CI time
runtime metrics
```

### ⚠️ Source map public không kiểm soát

Production source maps có thể lộ source code. Cần policy rõ:

```txt
hidden source map upload Sentry
không public source map nếu không cần
```

### ⚠️ Bundle nhỏ nhưng runtime vẫn chậm

Build tool chỉ là một phần. Runtime còn phụ thuộc React render, hydration, data fetching, third-party scripts.

---

## 🎤 15. Câu trả lời senior nên nói

**"Em chia build tools thành bundler và compiler/transpiler. Webpack mạnh ở enterprise, legacy, plugin ecosystem và Module Federation nhưng config phức tạp và dev chậm hơn. Vite nhanh trong dev vì dùng native ESM và esbuild pre-bundling; production build của Vite dùng Rollup nên cần nhớ dev/prod khác nhau. Rollup phù hợp library vì output sạch và tree-shaking tốt. esbuild rất nhanh cho transform/bundle cơ bản nhưng plugin/optimization không sâu bằng Webpack/Rollup. SWC là Rust compiler thay Babel tốt cho performance, còn Babel vẫn mạnh nhất về plugin ecosystem. Turbopack/Rspack đại diện xu hướng Rust incremental bundling, phù hợp Next.js hoặc migration từ Webpack tùy maturity. Khi chọn tool, em sẽ đo bottleneck thật: cold start, HMR, production build, bundle size, CI time và runtime metrics, rồi chọn theo use case thay vì chạy theo hype."**

---

## ✅ 16. Checklist phỏng vấn

```txt
□ Phân biệt bundler, compiler/transpiler, minifier
□ Biết Webpack mạnh/yếu ở đâu
□ Biết Vite dev nhanh nhờ native ESM + esbuild pre-bundling
□ Biết Vite production dùng Rollup
□ Biết Rollup phù hợp library build
□ Biết esbuild nhanh nhưng không thay mọi bundler production phức tạp
□ Biết SWC vs Babel trade-off
□ Biết Turbopack phù hợp nhất với Next.js ecosystem
□ Biết Rspack là hướng migration Webpack bằng Rust
□ Biết dev build khác production build
□ Biết tree-shaking cần ESM và sideEffects đúng
□ Biết code splitting bằng dynamic import
□ Biết SWC/esbuild không type-check TypeScript
□ Biết cần đo cold start, HMR, build time, bundle size, CI time
□ Biết source map production cần policy bảo mật
□ Biết chọn tool theo use case, không theo hype
```
