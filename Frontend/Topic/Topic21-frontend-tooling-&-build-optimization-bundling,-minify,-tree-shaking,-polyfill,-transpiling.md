# Topic21: Frontend Tooling & Build Optimization

## ⭐ Mục tiêu phỏng vấn Senior/Staff

> **Frontend build optimization là quá trình biến source code thành artifact nhỏ hơn, nhanh hơn, cache tốt hơn, tương thích browser mục tiêu và dễ debug/observe trong production.**

Senior/staff frontend cần nắm:

- 🧩 Dependency graph và bundling.
- ✂️ Minification và compression.
- 🌳 Tree shaking và dead code elimination.
- 🧱 Code splitting, lazy loading, chunk strategy.
- 🔁 Transpiling và polyfill.
- ⚡ Dev build vs production build.
- 🗃️ Browser/CDN caching.
- 🧭 Source maps, monitoring, DX.
- 🛡️ Security và performance budget.

---

## 1. 🧠 Big Picture: Build Tool Làm Gì?

Build tool nhận source code:

```txt
TypeScript / JSX / CSS / Assets / Env
```

Sau đó tạo output:

```txt
HTML + JS chunks + CSS chunks + assets + source maps
```

Pipeline thường có các bước:

```txt
Entry point
  -> Resolve imports
  -> Build dependency graph
  -> Transform TS/JSX/CSS/assets
  -> Tree shake
  -> Code split
  -> Bundle
  -> Minify
  -> Hash filename
  -> Generate source maps
```

### 🔥 Highlight

> **Build optimization không chỉ là "bundle nhỏ hơn". Mục tiêu thật là tải nhanh hơn, parse/execute ít hơn, cache hiệu quả hơn và production dễ vận hành hơn.**

---

## 2. 🧩 Dependency Graph

Bundler bắt đầu từ entry point:

```ts
import { createRoot } from "react-dom/client";
import App from "./App";
import "./styles.css";

createRoot(document.getElementById("root")!).render(<App />);
```

Sau đó lần theo toàn bộ `import` để tạo graph:

```txt
main.tsx
  -> App.tsx
    -> routes/Dashboard.tsx
    -> components/Button.tsx
  -> styles.css
  -> react
  -> react-dom
```

Graph giúp bundler biết:

- File nào phụ thuộc file nào.
- Module nào cần transform.
- Module nào có thể tree-shake.
- Chunk nào nên tách riêng.
- File nào cần rebuild khi dev.

### Senior note

> **Build nhanh hay chậm phụ thuộc nhiều vào cách tool xử lý dependency graph: cache, incremental rebuild, parallelization và transform engine.**

---

## 3. 📦 Bundling

**Bundling** là gộp nhiều module thành một hoặc nhiều file output để browser tải.

Trước bundling:

```txt
src/
  main.tsx
  App.tsx
  api.ts
  utils.ts
```

Sau bundling:

```txt
dist/
  index.html
  assets/main-a1b2c3.js
  assets/vendor-d4e5f6.js
  assets/main-a1b2c3.css
```

### Vì sao cần bundling?

- Browser cần ít request hơn.
- Có thể optimize toàn cục.
- Có thể minify/tree-shake/code split.
- Có thể hash filename để cache lâu.
- Có thể xử lý TS, JSX, CSS Modules, assets.

### HTTP/2 có làm bundling hết cần thiết không?

Không.

HTTP/2 xử lý nhiều request tốt hơn HTTP/1, nhưng bundling vẫn quan trọng vì:

- Mỗi JS file vẫn cần parse/compile/execute.
- Nhiều module nhỏ vẫn có overhead.
- Cần tree-shaking và minification.
- Cần cache strategy rõ ràng.

### 🔥 Highlight

> **Bundling hiện đại không phải gộp tất cả thành 1 file. Nó tạo chunk hợp lý để cân bằng request count, cache và lazy loading.**

---

## 4. 🧱 Chunk Strategy

Production app thường có nhiều chunk:

```txt
main.[hash].js
vendor.[hash].js
dashboard.[hash].js
settings.[hash].js
```

Các loại chunk:

| Chunk | Mục đích |
|---|---|
| Entry chunk | Code khởi động app |
| Vendor chunk | Library ít đổi như React |
| Route chunk | Code cho từng route |
| Shared chunk | Code dùng chung nhiều route |
| Async chunk | Code load khi user cần |

### Chunk tốt là gì?

Chunk tốt cần:

- Initial JS nhỏ.
- Route load nhanh.
- Vendor cache ổn định.
- Không tạo quá nhiều request nhỏ.
- Không duplicate dependency giữa chunks.

### ⚠️ Lỗi thường gặp

Over-splitting:

```txt
100 chunks nhỏ -> quá nhiều request + overhead
```

Under-splitting:

```txt
1 bundle lớn -> user tải cả app dù chỉ vào 1 route
```

---

## 5. 🌳 Tree Shaking

**Tree shaking** là loại bỏ code không được dùng khỏi bundle.

Ví dụ:

```ts
// math.ts
export function add(a: number, b: number) {
  return a + b;
}

export function multiply(a: number, b: number) {
  return a * b;
}
```

```ts
import { add } from "./math";

add(1, 2);
```

Nếu setup tốt, `multiply` sẽ không vào production bundle.

### Điều kiện để tree shaking tốt

- Dùng ES Modules: `import/export`.
- Tránh CommonJS nếu có thể: `require/module.exports`.
- Package khai báo đúng `sideEffects`.
- Không import cả library khi chỉ cần một phần.
- Code không có side effect khó phân tích.

### `sideEffects` trong `package.json`

```json
{
  "sideEffects": false
}
```

Nghĩa là import module không tạo side effect ngoài exports, bundler có thể loại bỏ an toàn.

Nếu có file CSS hoặc setup side effect:

```json
{
  "sideEffects": ["*.css", "./src/setup.ts"]
}
```

### ⚠️ Lỗi thường gặp

```ts
import _ from "lodash";
```

Dễ kéo nhiều code không cần thiết.

Tốt hơn:

```ts
import debounce from "lodash/debounce";
```

Hoặc dùng package hỗ trợ ESM tốt:

```ts
import { debounce } from "lodash-es";
```

### 🔥 Highlight

> **Tree shaking không phải magic. Nó phụ thuộc vào ESM, side effect, cách package publish và cách import.**

---

## 6. ✂️ Minification

**Minification** làm code nhỏ hơn bằng cách:

- Xóa whitespace/comment.
- Rút gọn tên biến local.
- Rút gọn expression.
- Loại dead code.
- Tính trước constant nếu an toàn.

Trước:

```ts
function calculateTotalPrice(items, taxRate) {
  let subtotal = 0;

  for (const item of items) {
    subtotal += item.price * item.quantity;
  }

  return subtotal * (1 + taxRate);
}
```

Sau minify:

```ts
function t(t,n){let r=0;for(const n of t)r+=n.price*n.quantity;return r*(1+n)}
```

Các tool phổ biến:

- ⚡ esbuild: rất nhanh.
- 🧬 SWC: rất nhanh, Rust-based.
- 🧰 Terser: tối ưu JS lâu đời, nhiều option.
- 🎨 cssnano/lightningcss: minify CSS.

### Minify khác compression

| Kỹ thuật | Chạy ở đâu | Mục tiêu |
|---|---|---|
| Minify | Build time | Giảm kích thước source output |
| Gzip/Brotli | Server/CDN | Nén khi transfer qua network |

Production nên có cả hai:

```txt
Minified JS + Brotli/Gzip
```

---

## 7. 🧨 Dead Code Elimination

Dead code là code không bao giờ chạy hoặc không được dùng.

```ts
if (false) {
  expensiveDebugCode();
}
```

Hoặc:

```ts
const DEBUG = false;

if (DEBUG) {
  console.log("debug");
}
```

Bundler/minifier có thể xóa khi biết giá trị ở build time.

Ví dụ với env:

```ts
if (process.env.NODE_ENV !== "production") {
  console.log("dev only");
}
```

Production build thường replace:

```ts
process.env.NODE_ENV -> "production"
```

Sau đó minifier xóa nhánh dev.

### ⚠️ Lưu ý

Nếu env không được replace đúng, code dev/debug có thể lọt vào production.

---

## 8. 🪓 Code Splitting

**Code splitting** là tách code thành nhiều chunk để chỉ load khi cần.

### Route-based splitting

```tsx
const Dashboard = lazy(() => import("./routes/Dashboard"));
const Settings = lazy(() => import("./routes/Settings"));
```

User vào `/dashboard` thì không cần tải code của `/settings`.

### Component-based splitting

```tsx
const HeavyChart = lazy(() => import("./HeavyChart"));
```

Chỉ load chart khi user mở tab analytics.

### Library splitting

```ts
const { default: confetti } = await import("canvas-confetti");

confetti();
```

Chỉ load library nặng khi thật sự cần.

### Khi nào nên split?

Nên split:

- Route lớn.
- Modal/workflow ít dùng.
- Chart/editor/map/library nặng.
- Admin-only feature.

Không nên split:

- Component nhỏ dùng ngay trên first screen.
- Utility vài KB.
- Code luôn cần cho initial render.

### 🔥 Highlight

> **Code splitting tốt làm initial load nhẹ hơn. Code splitting quá tay làm app chậm vì waterfall request.**

---

## 9. ⏳ Lazy Loading Và Preloading

Lazy loading trì hoãn tải code/data/assets đến khi cần.

```tsx
const ReportPage = lazy(() => import("./ReportPage"));
```

Nhưng nếu đợi user click mới bắt đầu tải, có thể bị delay. Có thể prefetch/preload thông minh:

```html
<link rel="prefetch" href="/assets/report.js">
<link rel="preload" href="/assets/main.css" as="style">
```

Khác nhau:

| Kỹ thuật | Ý nghĩa |
|---|---|
| `preload` | Tải sớm resource quan trọng cho current page |
| `prefetch` | Tải rảnh tay resource có thể cần ở page sau |
| `preconnect` | Kết nối sớm tới domain quan trọng |

### Senior note

> **Preload sai có thể tranh bandwidth với resource quan trọng hơn. Không preload mọi thứ.**

---

## 10. 🔁 Transpiling

**Transpiling** chuyển code hiện đại hoặc non-standard sang JavaScript browser hiểu được.

Ví dụ:

```ts
const getName = (user?: User) => user?.profile?.name ?? "Guest";
```

Có thể chuyển thành code tương thích browser cũ hơn.

Tool phổ biến:

- Babel.
- SWC.
- esbuild.
- TypeScript compiler.

Transpiling thường xử lý:

- TypeScript -> JavaScript.
- JSX -> JavaScript.
- Modern JS syntax -> older JS syntax.

### Transpiling không phải polyfill

Transpiling đổi syntax:

```ts
const fn = () => {};
```

Polyfill thêm API runtime:

```ts
Promise
Array.prototype.includes
Intl
fetch
```

### 🔥 Highlight

> **Transpile xử lý cú pháp. Polyfill xử lý API thiếu trong runtime.**

---

## 11. 🧩 Polyfill

Polyfill là code bổ sung tính năng browser chưa hỗ trợ.

Ví dụ browser cũ không có:

```ts
Array.prototype.includes
Promise
Intl.PluralRules
URLPattern
```

Polyfill có thể thêm implementation tương thích.

### Cách dùng polyfill

Theo browser target:

```json
{
  "browserslist": [
    ">0.5%",
    "last 2 versions",
    "not dead"
  ]
}
```

Tool sẽ dựa vào target để quyết định cần transform/polyfill gì.

### Polyfill strategy

| Strategy | Cách làm | Khi dùng |
|---|---|---|
| Global polyfill | Patch global API | App bình thường |
| Ponyfill | Import function riêng, không patch global | Library hoặc muốn tránh side effect |
| Differential serving | Modern bundle cho browser mới, legacy cho browser cũ | App cần support rộng |

### ⚠️ Lỗi thường gặp

- Ship quá nhiều polyfill cho browser hiện đại.
- Polyfill global trong library gây side effect.
- Quên polyfill `Intl` khi làm i18n.
- Chỉ test Chrome mới, bỏ sót Safari.

---

## 12. ⚡ Dev Build Vs Production Build

### Dev build ưu tiên tốc độ feedback

Dev build thường có:

- Source map nhanh.
- HMR/Fast Refresh.
- Ít minify.
- Transform nhanh.
- Error overlay.
- Incremental rebuild.

Vite dev nhanh vì:

- Dùng native ESM.
- Không bundle toàn bộ app ngay từ đầu.
- Dùng esbuild cho transform dependency nhanh.

### Production build ưu tiên output tối ưu

Production build thường có:

- Minification.
- Tree shaking.
- Code splitting.
- Content hash.
- CSS extraction/minify.
- Asset optimization.
- Source map kiểm soát.

### 🔥 Highlight

> **Dev build tối ưu cho developer feedback. Production build tối ưu cho user experience và vận hành.**

---

## 13. 🧰 Tooling: Vite, Webpack, Rollup, esbuild, SWC

| Tool | Vai trò chính | Điểm mạnh |
|---|---|---|
| Vite | Dev server + build tool | Dev rất nhanh, DX tốt |
| Webpack | Bundler tổng quát | Plugin ecosystem mạnh, flexible |
| Rollup | Bundler thiên về library | Output sạch, tree-shaking tốt |
| esbuild | Transpile/minify/bundle | Rất nhanh |
| SWC | Compiler/minifier | Rất nhanh, dùng nhiều trong Next.js |
| Babel | Transform JS | Plugin ecosystem lớn |

### Cách nói phỏng vấn

> **Vite dùng native ESM cho dev nên không cần bundle toàn bộ app trước khi chạy. Production build của Vite thường dựa trên Rollup để tối ưu chunk và output. Webpack linh hoạt và mature hơn cho case phức tạp, nhưng dev speed thường chậm hơn nếu setup lớn.**

---

## 14. 🗃️ Caching

Build optimization phải đi cùng caching.

Output production thường có content hash:

```txt
main.8f3a91.js
vendor.1c7d22.js
style.9a0b31.css
```

Nếu nội dung không đổi, hash không đổi. Browser/CDN có thể cache lâu.

### Cache headers

Static assets:

```http
Cache-Control: public, max-age=31536000, immutable
```

HTML:

```http
Cache-Control: no-cache
```

Vì HTML cần cập nhật để trỏ tới asset hash mới.

### Vendor chunk

Tách vendor có thể giúp cache:

```txt
react vendor chunk ít đổi
app chunk đổi thường xuyên
```

Nhưng không phải lúc nào tách vendor lớn cũng tốt. Cần đo bằng bundle analyzer và real metrics.

### 🔥 Highlight

> **Hash filename + cache header đúng thường cải thiện repeat visit mạnh hơn việc tối ưu vài KB nhỏ lẻ.**

---

## 15. 🧭 Source Maps

Source map map code minified về source gốc để debug.

Không có source map:

```txt
main.8f3a91.js:1:182839
```

Có source map:

```txt
src/features/checkout/CheckoutPage.tsx:42
```

### Các kiểu source map

| Type | Khi dùng |
|---|---|
| `eval` / `eval-source-map` | Dev, rebuild nhanh |
| `source-map` | Production debug đầy đủ nhưng cần kiểm soát expose |
| `hidden-source-map` | Upload cho Sentry, không public link rõ |
| `nosources-source-map` | Có stack trace nhưng không expose source |

### Production recommendation

- Không public source map bừa bãi nếu source nhạy cảm.
- Upload source map lên monitoring như Sentry.
- Dùng release version để map error đúng artifact.

---

## 16. 📊 Bundle Analysis

Không tối ưu bằng cảm tính. Cần đo.

Các câu hỏi cần trả lời:

- Bundle nào lớn nhất?
- Package nào chiếm nhiều KB?
- Có duplicate dependency không?
- Có import nhầm full library không?
- Initial JS có vượt budget không?
- Route nào đang load quá nhiều?

Tool phổ biến:

- `webpack-bundle-analyzer`
- `rollup-plugin-visualizer`
- `source-map-explorer`
- Lighthouse
- WebPageTest
- Chrome Performance panel

### Metrics nên quan tâm

| Metric | Ý nghĩa |
|---|---|
| Transfer size | Kích thước tải qua network sau gzip/brotli |
| Parsed size | Kích thước JS browser phải parse |
| Execution time | Thời gian chạy JS |
| LCP | Nội dung chính hiển thị nhanh không |
| INP | Tương tác có mượt không |
| TBT | Main thread có bị block không |

### 🔥 Highlight

> **JS cost không chỉ là download size. Browser còn phải parse, compile và execute. Mobile yếu bị ảnh hưởng nặng hơn desktop.**

---

## 17. 🎨 CSS Build Optimization

CSS cũng cần optimize:

- Extract CSS ra file riêng.
- Minify CSS.
- Remove unused CSS nếu có thể.
- Critical CSS cho first render nếu cần.
- Avoid CSS quá lớn từ UI framework.
- Dùng CSS Modules/Tailwind purge/content scan đúng.

Ví dụ Tailwind cần content config đúng:

```ts
export default {
  content: ["./src/**/*.{ts,tsx,html}"],
};
```

Nếu config sai, CSS output có thể rất lớn hoặc mất class cần thiết.

---

## 18. 🖼️ Asset Optimization

Build không chỉ tối ưu JS.

Images:

- Dùng AVIF/WebP nếu phù hợp.
- Responsive images.
- Lazy load ảnh dưới fold.
- Set width/height để tránh CLS.

Fonts:

- Subset font.
- Preload font quan trọng.
- Dùng `font-display: swap`.
- Tránh load quá nhiều weight.

Assets:

- Inline asset nhỏ nếu hợp lý.
- Hash asset để cache.
- CDN cho static file.

---

## 19. 🛡️ Security Trong Build

Build pipeline có thể tạo rủi ro security.

Cần kiểm soát:

- Không leak `.env` private vào client bundle.
- Không public source map chứa secret/internal code nhạy cảm.
- Không dùng dependency có vulnerability nghiêm trọng.
- Không inject user input vào build-time HTML/script.
- Có Subresource Integrity nếu dùng asset từ CDN ngoài.
- Có CSP phù hợp nếu app có risk XSS cao.

### Env trên frontend

Mọi biến env được bundle vào frontend đều public.

```ts
VITE_PUBLIC_API_URL=...
NEXT_PUBLIC_ANALYTICS_ID=...
```

Không bao giờ để secret:

```txt
AWS_SECRET_ACCESS_KEY
DATABASE_PASSWORD
PRIVATE_API_TOKEN
```

### 🔥 Highlight

> **Frontend env không phải secret. Nếu value vào bundle, user có thể đọc được.**

---

## 20. 🧪 Quality Tooling

Build pipeline thường đi cùng quality gates:

- ESLint: bắt lỗi pattern và rule code.
- Prettier: format thống nhất.
- TypeScript: type checking.
- Unit tests.
- E2E tests.
- Bundle budget.
- Dependency audit.
- CI build verification.

### ESLint vs Prettier

| Tool | Vai trò |
|---|---|
| ESLint | Code correctness, bug-prone pattern, convention |
| Prettier | Formatting |

Không nên để ESLint và Prettier tranh nhau format. Dùng config tương thích.

---

## 21. 🚦 Performance Budget

Performance budget là giới hạn để không cho app phình ra âm thầm.

Ví dụ budget:

```txt
Initial JS <= 200 KB gzip
Initial CSS <= 50 KB gzip
Route chunk <= 150 KB gzip
LCP <= 2.5s
INP <= 200ms
```

CI có thể fail nếu vượt budget.

### Senior note

> **Không có budget, bundle size thường tăng dần sau mỗi feature. Staff engineer cần biến performance thành guardrail, không phải chiến dịch dọn dẹp thỉnh thoảng.**

---

## 22. 🚀 Build Optimization Checklist

### JavaScript

- ✅ Dùng production build.
- ✅ Minify JS.
- ✅ Tree-shake được package.
- ✅ Tránh import full library nếu chỉ dùng một phần.
- ✅ Split route/library nặng.
- ✅ Tránh duplicate dependency.
- ✅ Kiểm tra parse/execute time, không chỉ gzip size.

### CSS

- ✅ Minify CSS.
- ✅ Remove unused CSS.
- ✅ Load critical CSS sớm.
- ✅ Tránh CSS framework output quá lớn.

### Assets

- ✅ Optimize image.
- ✅ Lazy load ảnh không quan trọng.
- ✅ Preload font quan trọng.
- ✅ Set cache header đúng.

### Production

- ✅ Content hash filename.
- ✅ Long cache cho static assets.
- ✅ HTML no-cache.
- ✅ Source map strategy rõ ràng.
- ✅ Upload source map cho monitoring nếu cần.
- ✅ Bundle analyzer trong CI hoặc release check.
- ✅ Performance budget.

---

## 23. ⚠️ Lỗi Thường Gặp Khi Phỏng Vấn

### 1. Nói tree shaking chỉ là xóa function không dùng

Thiếu. Cần nói thêm ESM, side effects, package format, import style.

### 2. Nhầm minify với gzip/brotli

Minify là build-time transform. Gzip/Brotli là transfer compression.

### 3. Nghĩ code splitting càng nhiều càng tốt

Sai. Quá nhiều chunk gây waterfall và overhead.

### 4. Ship polyfill cho mọi browser

Làm tăng bundle không cần thiết. Cần dựa trên browserslist/target.

### 5. Public source map không kiểm soát

Có thể expose source code, internal route, comments, implementation detail.

### 6. Chỉ nhìn bundle size

Thiếu parse time, execution time, main thread blocking, Core Web Vitals.

### 7. Đưa secret vào frontend env

Mọi thứ trong client bundle đều có thể bị đọc.

---

## 24. 🧾 Câu Trả Lời Phỏng Vấn 2 Phút

> **Frontend build optimization là quá trình biến source code thành production artifact tối ưu cho browser. Bundler bắt đầu từ entry point, tạo dependency graph, transform TypeScript/JSX/CSS, tree-shake code không dùng, chia code thành chunks, minify output, gắn content hash và tạo source maps.**
>
> **Các kỹ thuật chính gồm bundling để gom module hợp lý, tree shaking để loại unused exports, code splitting để lazy load route hoặc feature nặng, minification để giảm size, transpiling để đổi syntax hiện đại về target browser, và polyfill để bổ sung runtime API còn thiếu. Ngoài ra production cần cache strategy đúng: static assets dùng hash và cache lâu, HTML no-cache để nhận version mới.**
>
> **Ở senior level, tôi không tối ưu bằng cảm tính. Tôi dùng bundle analyzer, Lighthouse/WebPageTest và real user metrics để xem transfer size, parsed size, execution time, LCP/INP/TBT. Tôi cũng đặt performance budget trong CI để bundle không tăng âm thầm.**

---

## 25. 🎯 Câu Trả Lời Staff-Level

> **Ở staff level, tôi xem build tooling là một phần của frontend platform. Nó phải cân bằng bốn mục tiêu: developer feedback nhanh, production artifact nhỏ và cache tốt, browser compatibility đúng với business target, và observability đủ tốt khi production lỗi.**
>
> **Tôi sẽ thiết kế chunk strategy dựa trên user journey: initial route cần nhẹ, route hiếm dùng hoặc dependency nặng như chart/editor/map sẽ lazy load, vendor chunk cần ổn định để cache tốt nhưng không được duplicate. Tôi kiểm tra tree-shaking bằng analyzer, rà soát package CommonJS/ESM, sideEffects và import style.**
>
> **Tôi cũng tách rõ transpiling và polyfill: syntax transform không tự thêm API runtime. Với production, tôi kiểm soát source map bằng hidden/nosources source map và upload vào monitoring theo release. Quan trọng nhất, tôi đưa performance budget vào CI để performance trở thành tiêu chuẩn phát triển hằng ngày thay vì xử lý sau khi app đã chậm.**

---

## 26. 🧠 Ghi Nhớ Nhanh

| Icon | Ý chính |
|---|---|
| 🧩 | Bundler tạo dependency graph từ entry point |
| 📦 | Bundling gom module thành chunk hợp lý |
| 🌳 | Tree shaking xóa unused exports nếu ESM/sideEffects đúng |
| ✂️ | Minify giảm source output, gzip/brotli giảm transfer |
| 🪓 | Code splitting giảm initial JS nhưng không được quá tay |
| 🔁 | Transpile đổi syntax, polyfill thêm runtime API |
| 🗃️ | Hash filename + cache header đúng rất quan trọng |
| 🧭 | Source map cần cho debug nhưng phải kiểm soát exposure |
| 🚦 | Performance budget ngăn bundle tăng âm thầm |
| 🛡️ | Frontend env không bao giờ là secret |

---

## 27. ✅ Kết Luận

> **Frontend tooling tốt không chỉ giúp build chạy được. Nó giúp app tải nhanh, tương thích đúng browser, cache hiệu quả, debug được production và giữ performance ổn định khi team scale.**

Câu nhớ nhanh:

> **Build tool tạo graph, transform code, loại phần thừa, chia chunk, nén output, gắn hash, tạo source map và giúp production vận hành có kiểm soát.**
