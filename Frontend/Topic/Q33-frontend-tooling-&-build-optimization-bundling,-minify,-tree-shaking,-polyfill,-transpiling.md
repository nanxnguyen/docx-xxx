# 🏗️ Q33: Frontend Tooling & Build Optimization - Dependency Graph, Bundling, Tree-shaking, Code Splitting, Minification, Transpiling, Polyfills, Caching, Dev vs Prod Build, Runtime Performance, Security, Observability & DX, ESLint/Prettier, Source Maps

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (4-5 phút):**

**"Build tools optimize frontend: Bundling (gộp files), Minify (nén), Tree-shaking (loại unused code), Code splitting (lazy load), Polyfill (old browsers support), Transpiling (modern → old JS), ESLint/Prettier (code quality), Source maps (debugging)."**

**🔑 8 Kỹ Thuật Chính:**

**1. Bundling (Webpack, Vite, Rollup):**

- Gộp nhiều files thành 1-2 bundles → giảm HTTP requests
- Resolve dependencies, handle imports/exports
- Ví dụ: 100 files → 1 `bundle.js` (10 requests → 1 request)

**2. Minification:**

- Xóa whitespace, shorten variable names, remove comments
- **Terser** (JS), **cssnano** (CSS) - giảm 40-60% file size
- `const myVariableName = 123` → `const a=123`

**3. Tree-shaking:**

- **Loại unused exports** - chỉ bundle code thực sự dùng
- Cần ES modules (`import/export`), không work với CommonJS
- Ví dụ: `import {add} from 'utils'` → chỉ bundle `add`, không bundle `subtract`

**4. Code Splitting:**

- Tách code thành nhiều chunks, **lazy load** khi cần
- Route-based: mỗi route 1 bundle riêng
- Dynamic imports: `const module = await import('./heavy.js')`

**5. Polyfills:**

- Thêm **missing features** cho old browsers (IE11, Safari cũ)
- Core-js, Babel polyfills - support Promise, async/await, Array.includes...
- **Differential serving**: modern bundle (ESM) + legacy bundle (polyfilled)

**6. Transpiling (Babel, SWC):**

- Convert **modern JS → old JS** (ES2022 → ES5)
- JSX → JS, TypeScript → JS
- `const arrow = () => {}` → `var arrow = function() {}`

**7. ESLint/Prettier:**

- **ESLint**: Find bugs, enforce code patterns (unused vars, no-console...)
- **Prettier**: Auto-format code (spacing, quotes, semicolons)
- Pre-commit hooks (Husky) để enforce

**8. Source Maps:**

- Map minified code → original source cho debugging
- DevTools show **original code** thay vì minified
- Types: `inline`, `hidden`, `eval` (dev), `source-map` (production)

**⚠️ Lỗi Thường Gặp:**

- Ship polyfills cho modern browsers → waste bandwidth (dùng differential serving)
- Không tree-shake → bundle lodash toàn bộ (570KB) thay vì 1 function
- Source maps trong production → expose source code (dùng `hidden-source-map`)
- Over-splitting code → quá nhiều requests, worse than bundling

**💡 Kiến Thức Senior:**

- **Vite** nhanh hơn Webpack vì: ESBuild (Go) transpile, native ESM trong dev (không bundle)
- **Module Federation** (Webpack 5): Share code giữa apps runtime (microfrontends)
- **Turbopack** (Next.js 14): Rust-based, 700x faster than Webpack dev mode
- Performance budget: Set limits (JS < 200KB, CSS < 50KB), fail build nếu vượt

**❓ Câu Hỏi:**

Giải thích chi tiết các công cụ và kỹ thuật tối ưu hóa trong frontend development: Bundling (gộp file), Minify (nén code), Tree-shaking (loại bỏ code thừa), Code splitting (tách code), Polyfill (thêm features cho old browsers), Transpiling (convert modern → old JS), ESLint/Prettier, và Source Maps. Bao gồm cách hoạt động, ưu nhược điểm, và ứng dụng thực tế.

**📚 Phần 1: Bundling (Gộp File) - Từ Nhiều Files → 1 File**

#### **💡 Bundling Là Gì? (What is Bundling?)**

**Bundling** là quá trình **gộp nhiều files JavaScript/CSS/assets** thành **ít files hơn** (thường là 1 file duy nhất) để gửi lên browser.

**🔥 Tại Sao Cần Bundling?**

**❌ Không dùng bundling:**
- 100 files = 100 HTTP requests → Rất chậm (10 giây load time)
- HTTP/1.1 chỉ 6-8 connections đồng thời → phải chờ từng đợt
- Không optimize được (không minify, tree-shake)

**✅ Dùng bundling:**
- 100 files → 1 bundle.js → 1 HTTP request → Nhanh hơn 100x (100ms)
- Có thể minify, tree-shake, compress, cache
- Giảm 73% kích thước, giảm latency đáng kể

**🎯 Cách Hoạt Động Của Bundler:**

**5 bước chính:**
1. **Dependency Resolution**: Đọc entry point, tìm tất cả imports, tạo dependency graph
2. **Transform**: TypeScript → JS, JSX → JS, ES6+ → ES5, CSS Modules
3. **Tree Shaking**: Phân tích exports/imports, loại code không dùng (30KB → 22KB)
4. **Bundle**: Gộp tất cả files thành 1 file, wrap modules trong function scope
5. **Minify**: Remove whitespace, comments, shorten names (22KB → 8KB)

**Kết quả:** 5 files (30KB) → 1 file (8KB) - Giảm 73% kích thước, 5 requests → 1 request

**💻 Code Example:**

**Trước bundling (3 files):**
```typescript
// utils.js
export function add(a, b) { return a + b; }

// api.js
import { add } from './utils.js';
export async function fetchData() { /* ... */ }

// index.js
import { fetchData } from './api.js';
```

**Sau bundling (1 file):**
```typescript
// bundle.js
(function() {
  const utils = { add: (a, b) => a + b };
  const api = { fetchData: async () => { /* ... */ } };
  // ... tất cả code trong 1 file
})();
```

---

**📚 Phần 2: Minify (Nén Code) - Làm Code Nhỏ Gọn**

#### **💡 Minify Là Gì? (What is Minification?)**

**Minify** là quá trình **loại bỏ tất cả ký tự không cần thiết** khỏi code (whitespace, comments, newlines) và **rút ngắn tên biến** để giảm kích thước file.

**🔥 Minify Làm Gì?**

**Trước minify (10 KB):**
```typescript
function calculateTotalPrice(items, taxRate, discount) {
  let subtotal = 0;
  for (let i = 0; i < items.length; i++) {
    subtotal += items[i].price * items[i].quantity;
  }
  const discountedPrice = subtotal * (1 - discount / 100);
  const tax = discountedPrice * (taxRate / 100);
  return discountedPrice + tax;
}
```

**Sau minify (3 KB - giảm 70%):**
```typescript
function c(a,b,d){let e=0;for(let f=0;f<a.length;f++){e+=a[f].price*a[f].quantity}const h=e*(1-d/100),i=h*(b/100);return h+i}
```

**Kỹ thuật:** Remove comments, whitespace, newlines, shorten variable names (calculateTotalPrice → c), optimize boolean logic, constant folding

**🔧 Các Kỹ Thuật Minify Chi Tiết:**

```typescript
// ===================================================
// 🔧 KỸ THUẬT 1: Remove Whitespace & Comments
// ===================================================

// Before (với whitespace, comments)
function add(a, b) {
  // This function adds two numbers
  return a + b; // Return sum
}

// After (remove whitespace, comments)
function add(a, b) {
  return a + b;
}

// Tiết kiệm: ~50 bytes

// ===================================================
// 🔧 KỸ THUẬT 2: Shorten Variable Names (Mangle)
// ===================================================

// Before (tên biến dài, có nghĩa)
function calculateUserTotalScore(userAnswers, correctAnswers) {
  let totalScore = 0;
  for (let index = 0; index < userAnswers.length; index++) {
    if (userAnswers[index] === correctAnswers[index]) {
      totalScore += 10;
    }
  }
  return totalScore;
}

// After (tên biến ngắn - 1 ký tự)
function c(a, b) {
  let d = 0;
  for (let e = 0; e < a.length; e++) {
    if (a[e] === b[e]) {
      d += 10;
    }
  }
  return d;
}

// Tiết kiệm: ~100 bytes

// ⚠️ LƯU Ý: Chỉ mangle LOCAL variables
// KHÔNG mangle exported names (để external code gọi được)

// ===================================================
// 🔧 KỸ THUẬT 3: Optimize Boolean Logic
// ===================================================

// Before
if (user.isActive === true) {
  console.log('Active');
}

// After
if (user.isActive) console.log('Active');

// Before
const value = condition ? true : false;

// After
const value = !!condition; // Hoặc: value = condition

// ===================================================
// 🔧 KỸ THUẬT 4: Dead Code Elimination
// ===================================================

// Before
function process(data) {
  const temp = data * 2; // ❌ temp không dùng
  const result = data + 10;
  return result;
}

// After (remove unused variable)
function process(a) {
  return a + 10;
}

// ===================================================
// 🔧 KỸ THUẬT 5: Constant Folding (Gộp hằng số)
// ===================================================

// Before
const total = 10 + 20 + 30; // Tính lúc runtime

// After
const total = 60; // Tính lúc build time

// Before
const area = Math.PI * 5 * 5; // Tính lúc runtime

// After
const area = 78.53981633974483; // Tính sẵn lúc build

// ===================================================
// 🔧 KỸ THUẬT 6: Property Mangling (Advanced)
// ===================================================

// Before
const user = {
  firstName: 'John',
  lastName: 'Doe',
  calculateAge: function () {
    return 2024 - this.birthYear;
  },
};

// After (mangle property names - CẨN THẬN!)
const user = {
  a: 'John', // firstName → a
  b: 'Doe', // lastName → b
  c: function () {
    return 2024 - this.d;
  }, // calculateAge → c
};

// ⚠️ NGUY HIỂM: Nếu external code access user.firstName → BỊ LỖI!
// → Chỉ dùng khi chắc chắn property KHÔNG được access từ bên ngoài
```

**📊 Minify Performance Impact:**

```
┌──────────────────────────────────────────────────────────┐
│           MINIFY IMPACT (Ảnh hưởng của Minify)          │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  📦 React App Example (Production build):               │
│                                                          │
│  BEFORE Minify:                                         │
│  ├── main.js:          850 KB (code dễ đọc)            │
│  ├── vendor.js:        1.2 MB (libraries)              │
│  └── Total:            2.05 MB                          │
│                                                          │
│  AFTER Minify:                                          │
│  ├── main.min.js:      280 KB (67% nhỏ hơn!) ✅        │
│  ├── vendor.min.js:    420 KB (65% nhỏ hơn!) ✅        │
│  └── Total:            700 KB                           │
│                                                          │
│  AFTER Minify + Gzip:                                   │
│  ├── main.min.js.gz:   95 KB (89% nhỏ hơn!) 🚀         │
│  ├── vendor.min.js.gz: 145 KB (88% nhỏ hơn!) 🚀        │
│  └── Total:            240 KB                           │
│                                                          │
│  ⏱️ Load Time Impact (3G network ~400 KB/s):           │
│  ├── Before: 2.05 MB ÷ 400 KB/s = 5.1 giây ❌          │
│  ├── After Minify: 700 KB ÷ 400 KB/s = 1.75 giây ✅    │
│  └── After Minify+Gzip: 240 KB ÷ 400 KB/s = 0.6 giây 🚀│
│                                                          │
│  📈 Cải thiện: Nhanh hơn 8.5x!                          │
└──────────────────────────────────────────────────────────┘
```

---

**📚 Phần 3: Tree Shaking (Loại Bỏ Code Thừa) - Rũ Cây**

#### **💡 Tree Shaking Là Gì?**

**Tree Shaking** là quá trình **loại bỏ dead code** (code không được sử dụng) khỏi bundle. Tên gọi "rũ cây" vì giống như rũ cây để lá chết rơi xuống.

**🌲 Cách Hoạt Động:**

**Ví dụ:** Library có 10 functions, app chỉ dùng 2:
```typescript
// math-utils.js - Export 10 functions
export function add(a, b) { return a + b; }
export function subtract(a, b) { return a - b; }
export function multiply(a, b) { return a * b; }
// ... 7 functions khác

// app.js - Chỉ import 2 functions
import { add, subtract } from './math-utils.js';

// Kết quả:
// ❌ Không tree-shake: Bundle 2KB (10 functions)
// ✅ Có tree-shake: Bundle 400 bytes (2 functions) - Giảm 80%!
```

**🔍 Quy Trình Tree Shaking:**

**3 bước:**
1. **Build Dependency Tree**: Phân tích imports/exports, tạo dependency graph
2. **Mark Unused Exports**: Scan imports → đánh dấu exports không được import = UNUSED
3. **Remove Dead Code**: Loại bỏ code không dùng → Bundle size giảm (2KB → 400 bytes)

**⚠️ Điều Kiện Để Tree Shaking Hoạt Động:**

**1. Dùng ES Modules (import/export):**
```typescript
// ✅ GOOD: ES Modules
export function add(a, b) { return a + b; }
import { add } from './utils.js'; // Tree-shake được

// ❌ BAD: CommonJS
module.exports = { add: (a, b) => a + b; };
const { add } = require('./utils.js'); // Không tree-shake được
```

**2. Set `sideEffects: false` trong package.json:**
```json
{
  "sideEffects": false  // Hoặc ["*.css", "polyfills.ts"]
}
```

**3. Named exports thay vì default export:**
```typescript
// ✅ GOOD: Named exports
export const add = (a, b) => a + b;
import { add } from './utils.js'; // Chỉ bundle add

// ❌ BAD: Default export
export default { add, subtract, multiply };
import utils from './utils.js'; // Bundle cả 3 functions
```

**4. Tránh barrel exports:**
```typescript
// ❌ BAD: Barrel file
export * from './moduleA';
import { funcA } from './index.js'; // Load tất cả modules

// ✅ GOOD: Import trực tiếp
import { funcA } from './moduleA.js'; // Chỉ load moduleA
```

**🎯 Real-World Example - Lodash:**

```typescript
// ❌ BAD: Import toàn bộ Lodash (70KB)
import _ from 'lodash';
const result = _.uniq([1, 2, 2, 3]); // Bundle: +70KB

// ✅ GOOD: Import chỉ function cần dùng (2KB)
import uniq from 'lodash/uniq';
// Hoặc: import { uniq } from 'lodash-es';
const result = uniq([1, 2, 2, 3]); // Bundle: +2KB

// Kết quả: Tiết kiệm 68KB (97% nhỏ hơn)!
```

---

**📚 Phần 4: Code Splitting, ESLint/Prettier, Source Maps**

Các công cụ quan trọng trong frontend development:

1. **ESLint/Prettier** - Code Quality & Formatting

   - **ESLint**: Linter - phát hiện lỗi, enforce coding standards
   - **Prettier**: Formatter - format code tự động, giữ style nhất quán
   - **Tích hợp**: ESLint check logic + Prettier format code

2. **Source Maps** - Debugging

   - Map từ minified/transpiled code → original source code
   - Debug trong browser như code gốc (trước build)
   - Xem line numbers, variable names chính xác

3. **Code Splitting** - Performance Optimization
   - Chia bundle thành nhiều chunks nhỏ
   - Load code khi cần (lazy loading)
   - Cải thiện initial load time

**Hoạt động - Build Pipeline:**

**Development:** Code (ES2020+, TS) → ESLint → Prettier → Clean code

**Build Process:**
1. **Transpiling**: ES2020 → ES5, TS → JS, JSX → JS
2. **Polyfilling**: Add Promise, fetch, Array.from (chỉ cần thiết)
3. **Bundling**: 100 files → 1 file (550KB)
4. **Tree-shaking**: Loại dead code (550KB → 300KB)
5. **Minify**: Remove whitespace, shorten names (300KB → 100KB)
6. **Code Splitting**: Split thành chunks (main.js 30KB, vendor.js 40KB, lazy chunks)

**Production:**
- Modern browsers: modern.js (80KB, ES2020, no polyfills)
- Old browsers: legacy.js (100KB, ES5, with polyfills)
- Source Maps: Debug với original code

**Kết quả:** 500KB → 80KB (84% nhỏ hơn), Initial load: 30KB (94% nhỏ hơn)

**Ưu điểm:**

- ✅ **Bundling**: 100 requests → 1 request, giảm latency 100x
- ✅ **Minify**: Giảm 60-70% kích thước file (850KB → 280KB)
- ✅ **Tree-shaking**: Loại bỏ dead code, giảm 30-50% bundle size
- ✅ **Polyfill**: Dùng modern features trên old browsers (IE11)
- ✅ **Transpiling**: Viết ES2020+, deploy ES5 (backward compatible)
- ✅ **ESLint**: Catch bugs sớm, enforce best practices
- ✅ **Prettier**: Không tranh cãi về code style, tự động format
- ✅ **Source Maps**: Debug dễ dàng như development mode
- ✅ **Code Splitting**: Initial load nhanh hơn, better UX
- ✅ **Differential Serving**: Modern browsers tải 66% ít hơn

**Nhược điểm:**

- ❌ **Bundling**: Build time chậm hơn (phải gộp files)
- ❌ **Minify**: Code khó đọc (cần source maps để debug)
- ❌ **Tree-shaking**: Không hoạt động với CommonJS, side-effects
- ❌ **Polyfill**: Tăng bundle size (core-js ~90KB nếu import all)
- ❌ **Transpiling**: Code dài hơn (arrow fn → function declaration)
- ❌ **ESLint**: Cấu hình phức tạp, rules conflict
- ❌ **Prettier**: Đôi khi format không như ý muốn
- ❌ **Source Maps**: File .map tăng bandwidth (nên serve riêng)
- ❌ **Code Splitting**: Phức tạp hơn, nhiều HTTP requests

**Chú thích:**

**📦 Bundling Best Practices:**

- **Webpack**: Bundler phổ biến nhất, nhiều features
- **Vite**: Bundler mới, cực nhanh (dùng esbuild)
- **Rollup**: Tốt cho libraries (tree-shaking xuất sắc)

**🗜️ Minify Tools:**

- **Terser**: Minifier tốt nhất cho JavaScript (default trong Webpack 5)
- **esbuild**: Cực nhanh (Golang), dùng trong Vite
- **UglifyJS**: Cũ hơn, chậm hơn (deprecated)

**🌲 Tree-shaking Tips:**

- **Yêu cầu**: ESM (`import/export`), không dùng CommonJS (`require`)
- **`sideEffects: false`**: Báo cho bundler biết "safe to remove unused exports"
- **Side-effects**: Code có tác dụng phụ (global variables, CSS imports, polyfills...)

**🔧 Polyfill Best Practices:**

- **core-js**: Comprehensive polyfill library (500+ polyfills)
- **polyfill.io**: Dynamic polyfill service (auto-detect browser)
- **Strategy**: Import only needed polyfills (`import 'core-js/features/array/includes'`)
- **Avoid**: Import all polyfills (`import 'core-js'` → +90KB!)

**🔄 Transpiling Best Practices:**

- **Babel**: Industry standard transpiler (ES6+ → ES5)
- **@babel/preset-env**: Auto-detect transforms needed based on targets
- **TypeScript**: Type checking + transpiling (slower than Babel)
- **Best**: TypeScript (type check) + Babel (transpile)
- **Differential Serving**: Modern bundle (ES2020) + Legacy bundle (ES5)

**🔍 ESLint vs Prettier:**

- **ESLint**: Tập trung vào **logic** (unused vars, missing return, potential bugs...)
- **Prettier**: Tập trung vào **formatting** (spaces, quotes, line breaks...)
- **Tích hợp**: `eslint-config-prettier` tắt ESLint formatting rules → không conflict

**🗺️ Source Maps:**

- Development: `devtool: 'eval-source-map'` (fast rebuild)
- Production: `devtool: 'source-map'` (separate .map file)
- **Hidden source maps**: Deploy .map riêng, không public → bảo mật source code

**✂️ Code Splitting:**

- **Route-based**: Split theo routes (React Router, Vue Router)
- **Component-based**: Lazy load components nặng (React.lazy, Vue defineAsyncComponent)
- **Vendor splitting**: Tách libraries (React, Lodash...) ra vendor chunk

---

**📚 Phần 5: Dependency Graph (Sơ Đồ Phụ Thuộc)**

#### **💡 Dependency Graph Là Gì?**

**Dependency Graph** là **sơ đồ mô tả quan hệ phụ thuộc** giữa các modules/files trong ứng dụng. Bundler dùng graph này để:

- Tìm tất cả files cần bundle
- Xác định thứ tự load modules
- Loại bỏ code không dùng (tree-shaking)
- Tối ưu code splitting

**🔍 Cách Hoạt Động:**

```typescript
// ===================================================
// 📊 DEPENDENCY GRAPH CONSTRUCTION (Xây Dựng Sơ Đồ)
// ===================================================

/**
 * QUY TRÌNH XÂY DỰNG DEPENDENCY GRAPH:
 *
 * 1️⃣ Start từ Entry Point (index.js)
 * 2️⃣ Scan imports/requires trong file
 * 3️⃣ Đệ quy scan imports trong các file được import
 * 4️⃣ Tạo graph (tree structure) với dependencies
 * 5️⃣ Detect circular dependencies (phụ thuộc vòng)
 * 6️⃣ Determine load order (thứ tự tải)
 */

// ===================================================
// 📂 PROJECT STRUCTURE (Cấu Trúc Dự Án)
// ===================================================

// src/index.js (Entry point)
import { initAuth } from './auth.js';
import { fetchUserData } from './api.js';
import { renderDashboard } from './dashboard.js';

initAuth();
const userData = await fetchUserData();
renderDashboard(userData);

// src/auth.js
import { setToken, getToken } from './utils.js';
import { API_URL } from './config.js';

export function initAuth() {
  const token = getToken();
  if (!token) {
    // Redirect to login
  }
}

// src/api.js
import { getToken } from './utils.js';
import { API_URL } from './config.js';

export async function fetchUserData() {
  const token = getToken();
  const response = await fetch(`${API_URL}/user`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  return response.json();
}

// src/dashboard.js
import { formatDate } from './utils.js';
import { Chart } from './chart.js';

export function renderDashboard(data) {
  const chart = new Chart(data);
  chart.render();
}

// src/utils.js
export function setToken(token) {
  localStorage.setItem('token', token);
}

export function getToken() {
  return localStorage.getItem('token');
}

export function formatDate(date) {
  return new Date(date).toLocaleDateString();
}

// src/config.js
export const API_URL = 'https://api.example.com';

// src/chart.js
import { formatDate } from './utils.js';

export class Chart {
  constructor(data) {
    this.data = data;
  }
  render() {
    console.log('Rendering chart...');
  }
}

// ===================================================
// 📊 DEPENDENCY GRAPH (Sơ Đồ Phụ Thuộc)
// ===================================================

/**
 * 🌳 VISUAL DEPENDENCY GRAPH:
 *
 *                  index.js (Entry)
 *                      │
 *        ┌─────────────┼─────────────┐
 *        │             │             │
 *      auth.js       api.js    dashboard.js
 *        │             │             │
 *    ┌───┴───┐     ┌───┴───┐     ┌───┴───┐
 *    │       │     │       │     │       │
 * utils.js config.js utils.js config.js utils.js chart.js
 *    │                                       │
 *    │                                   utils.js
 *    │                                    (đã có)
 *    └───────────────────┬─────────────────┘
 *                        │
 *                  (Shared module)
 *
 * ✅ INSIGHTS:
 * - utils.js được dùng bởi 3 modules (auth, api, dashboard, chart)
 * - config.js được dùng bởi 2 modules (auth, api)
 * - Không có circular dependencies ✅
 * - Load order: config.js, utils.js → auth.js, api.js, chart.js → dashboard.js → index.js
 */

// ===================================================
// 🔢 DEPENDENCY GRAPH DATA STRUCTURE
// ===================================================

// Bundler internal representation (simplified)
const dependencyGraph = {
  'index.js': {
    path: '/src/index.js',
    dependencies: ['auth.js', 'api.js', 'dashboard.js'],
    size: 250, // bytes
    exports: [], // Entry point không export
    imports: ['initAuth', 'fetchUserData', 'renderDashboard'],
  },

  'auth.js': {
    path: '/src/auth.js',
    dependencies: ['utils.js', 'config.js'],
    size: 180,
    exports: ['initAuth'],
    imports: ['setToken', 'getToken', 'API_URL'],
  },

  'api.js': {
    path: '/src/api.js',
    dependencies: ['utils.js', 'config.js'],
    size: 200,
    exports: ['fetchUserData'],
    imports: ['getToken', 'API_URL'],
  },

  'dashboard.js': {
    path: '/src/dashboard.js',
    dependencies: ['utils.js', 'chart.js'],
    size: 150,
    exports: ['renderDashboard'],
    imports: ['formatDate', 'Chart'],
  },

  'utils.js': {
    path: '/src/utils.js',
    dependencies: [], // Leaf node - không depend vào file nào
    size: 120,
    exports: ['setToken', 'getToken', 'formatDate'],
    imports: [],
  },

  'config.js': {
    path: '/src/config.js',
    dependencies: [], // Leaf node
    size: 50,
    exports: ['API_URL'],
    imports: [],
  },

  'chart.js': {
    path: '/src/chart.js',
    dependencies: ['utils.js'],
    size: 300,
    exports: ['Chart'],
    imports: ['formatDate'],
  },
};

// ===================================================
// 🔄 CIRCULAR DEPENDENCY DETECTION (Phát Hiện Phụ Thuộc Vòng)
// ===================================================

// ❌ CIRCULAR DEPENDENCY EXAMPLE (Ví dụ phụ thuộc vòng)

// moduleA.js
import { funcB } from './moduleB.js';
//    ↓ moduleA depends on moduleB

export function funcA() {
  return funcB() + 1;
}

// moduleB.js
import { funcA } from './moduleA.js';
//    ↓ moduleB depends on moduleA (CIRCULAR!)

export function funcB() {
  return funcA() - 1; // ⚠️ Infinite loop!
}

// 🚨 PROBLEM:
// moduleA → moduleB → moduleA → moduleB → ... (vòng lặp vô hạn)
// Bundler sẽ detect và warning: "Circular dependency detected!"

/**
 * 🔍 CIRCULAR DEPENDENCY DETECTION ALGORITHM:
 *
 * 1. Dùng DFS (Depth-First Search) để traverse graph
 * 2. Track visited nodes
 * 3. Nếu visit lại node đang trong stack → Circular!
 */

function detectCircularDependency(graph, startNode) {
  const visited = new Set();
  const stack = new Set(); // Nodes đang được visit

  function dfs(node) {
    if (stack.has(node)) {
      // ❌ Circular dependency detected!
      throw new Error(`Circular dependency: ${[...stack, node].join(' → ')}`);
    }

    if (visited.has(node)) {
      return; // Already processed
    }

    visited.add(node);
    stack.add(node);

    // Visit dependencies
    const deps = graph[node]?.dependencies || [];
    for (const dep of deps) {
      dfs(dep);
    }

    stack.delete(node); // Remove from stack sau khi xong
  }

  dfs(startNode);
}

// Example usage:
try {
  detectCircularDependency(dependencyGraph, 'index.js');
  console.log('✅ No circular dependencies');
} catch (error) {
  console.error('❌ Circular dependency detected:', error.message);
}

// ===================================================
// 📦 BUNDLING ORDER (Thứ Tự Gộp File)
// ===================================================

/**
 * 🎯 TOPOLOGICAL SORT (Sắp Xếp Topo):
 *
 * Xác định thứ tự bundle sao cho:
 * - Dependencies được load TRƯỚC modules phụ thuộc vào nó
 * - Không vi phạm dependencies
 *
 * Algorithm:
 * 1. Tìm nodes không có dependencies (leaf nodes)
 * 2. Add vào bundle
 * 3. Remove khỏi graph
 * 4. Repeat cho đến khi hết nodes
 */

function topologicalSort(graph) {
  const result = [];
  const visited = new Set();

  function visit(node) {
    if (visited.has(node)) return;

    visited.add(node);

    // Visit dependencies first (post-order traversal)
    const deps = graph[node]?.dependencies || [];
    for (const dep of deps) {
      visit(dep);
    }

    result.push(node);
  }

  // Start from entry point
  visit('index.js');

  return result;
}

const bundleOrder = topologicalSort(dependencyGraph);
console.log('📦 Bundle order:', bundleOrder);
// Output: ['config.js', 'utils.js', 'auth.js', 'api.js', 'chart.js', 'dashboard.js', 'index.js']

/**
 * 💡 GIẢI THÍCH:
 *
 * 1. config.js, utils.js → Leaf nodes (không depend gì) → Bundle trước
 * 2. auth.js, api.js → Depend vào config.js, utils.js → Bundle sau
 * 3. chart.js → Depend vào utils.js → Bundle sau
 * 4. dashboard.js → Depend vào utils.js, chart.js → Bundle sau
 * 5. index.js → Entry point, depend vào tất cả → Bundle cuối
 *
 * ✅ Đảm bảo: Khi index.js execute, tất cả dependencies đã loaded!
 */

// ===================================================
// 🌲 TREE SHAKING với DEPENDENCY GRAPH
// ===================================================

/**
 * Tree-shaking dùng dependency graph để:
 * 1. Tìm exports nào được import (used exports)
 * 2. Loại bỏ exports không được import (unused exports)
 */

function analyzeUsedExports(graph) {
  const usedExports = new Map();

  // Scan tất cả imports
  for (const [moduleName, moduleInfo] of Object.entries(graph)) {
    const imports = moduleInfo.imports;

    for (const importName of imports) {
      // Tìm module export importName này
      for (const [depModule, depInfo] of Object.entries(graph)) {
        if (depInfo.exports.includes(importName)) {
          if (!usedExports.has(depModule)) {
            usedExports.set(depModule, new Set());
          }
          usedExports.get(depModule).add(importName);
        }
      }
    }
  }

  return usedExports;
}

const usedExports = analyzeUsedExports(dependencyGraph);

// Print tree-shaking results
for (const [moduleName, moduleInfo] of Object.entries(dependencyGraph)) {
  const allExports = moduleInfo.exports;
  const used = usedExports.get(moduleName) || new Set();
  const unused = allExports.filter((exp) => !used.has(exp));

  if (unused.length > 0) {
    console.log(
      `🌲 ${moduleName}: Remove unused exports: ${unused.join(', ')}`
    );
  }
}

// Output:
// 🌲 utils.js: Remove unused exports: setToken
// (setToken exported nhưng không được import bởi module nào)

// ===================================================
// 🔍 DEPENDENCY GRAPH VISUALIZATION TOOLS
// ===================================================

/**
 * 📊 WEBPACK BUNDLE ANALYZER
 *
 * Visualize dependency graph & bundle sizes
 */

// Install
// npm install --save-dev webpack-bundle-analyzer

// webpack.config.js
const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');

module.exports = {
  plugins: [
    new BundleAnalyzerPlugin({
      analyzerMode: 'static', // Generate HTML report
      reportFilename: 'bundle-report.html',
      openAnalyzer: true, // Auto-open in browser
      generateStatsFile: true, // Generate stats.json
      statsFilename: 'bundle-stats.json',
    }),
  ],
};

// Run build
// npm run build

// Output:
// ✅ bundle-report.html - Interactive treemap visualization
//    - Xem size từng module
//    - Xem dependencies giữa modules
//    - Identify large modules (candidates for code splitting)

/**
 * 📊 VITE: rollup-plugin-visualizer
 */

// vite.config.ts
import { visualizer } from 'rollup-plugin-visualizer';

export default {
  plugins: [
    visualizer({
      open: true, // Auto-open report
      gzipSize: true, // Show gzip sizes
      brotliSize: true, // Show brotli sizes
      filename: 'bundle-analysis.html',
    }),
  ],
};

/**
 * 📊 NX: Dependency Graph
 */

// nx.json (Nx workspace)
// Run command
// npx nx graph

// Output:
// ✅ Interactive graph showing:
//    - Project dependencies
//    - Library dependencies
//    - Affected projects (khi file thay đổi)

// ===================================================
// 💡 DEPENDENCY GRAPH BEST PRACTICES
// ===================================================

/**
 * ✅ DO (NÊN):
 *
 * 1. Tránh circular dependencies
 *    - Refactor code để break cycles
 *    - Dùng dependency injection thay vì direct imports
 *
 * 2. Minimize dependencies
 *    - Mỗi module nên có ít dependencies nhất có thể
 *    - Tách large modules thành smaller, focused modules
 *
 * 3. Shared modules cho common code
 *    - utils.js, config.js → Shared by many modules
 *    - Avoid code duplication
 *
 * 4. Layer architecture
 *    - UI Layer → Business Logic Layer → Data Layer
 *    - Dependencies flow ONE DIRECTION (top → bottom)
 *
 * 5. Analyze bundle regularly
 *    - Run bundle analyzer mỗi sprint
 *    - Track bundle size over time
 *    - Set budget limits (main.js < 200 KB)
 */

/**
 * ❌ DON'T (KHÔNG NÊN):
 *
 * 1. Circular dependencies
 *    moduleA → moduleB → moduleA ❌
 *
 * 2. Deep dependency chains
 *    A → B → C → D → E → F (quá sâu, hard to maintain)
 *
 * 3. God modules (modules quá lớn)
 *    utils.js with 100+ functions ❌
 *    → Tách thành utils/math.js, utils/string.js, utils/date.js
 *
 * 4. Barrel exports abuse
 *    index.ts export tất cả → Bundle size lớn
 *    → Import trực tiếp từ specific files
 *
 * 5. Unused dependencies
 *    Install library nhưng không dùng → Tăng node_modules size
 *    → Regularly run `npm prune`, `depcheck`
 */

// ===================================================
// 🎯 REAL-WORLD EXAMPLE: Trading App Dependency Graph
// ===================================================

/**
 * 📊 TRADING APP STRUCTURE:
 *
 *                        index.tsx (Entry)
 *                             │
 *          ┌──────────────────┼──────────────────┐
 *          │                  │                  │
 *       App.tsx          auth-provider.tsx   theme-provider.tsx
 *          │                  │                  │
 *    ┌─────┴─────┐       auth-api.ts        theme-config.ts
 *    │           │            │
 * Router.tsx  Layout.tsx  api-client.ts
 *    │           │
 *    │      ┌────┴────┐
 *    │      │         │
 * pages/  Header.tsx Sidebar.tsx
 *    │      │
 *    ├─ Dashboard.tsx
 *    ├─ Trading.tsx
 *    ├─ Portfolio.tsx
 *    └─ Analytics.tsx
 *         │
 *    components/
 *         ├─ StockChart.tsx
 *         ├─ OrderForm.tsx
 *         └─ PortfolioTable.tsx
 *              │
 *         utils/
 *              ├─ format-currency.ts
 *              ├─ calculate-profit.ts
 *              └─ validate-order.ts
 *
 * ✅ INSIGHTS:
 * - utils/ → Shared by all components (high reusability)
 * - api-client.ts → Shared by all API modules
 * - pages/ → Lazy loaded (code splitting)
 * - components/ → Can be code-split if heavy
 * - No circular dependencies ✅
 */

// ===================================================
// 📊 DEPENDENCY GRAPH METRICS
// ===================================================

/**
 * 🎯 KEY METRICS TO TRACK:
 *
 * 1. Module Count
 *    - Total modules in project
 *    - Trend: Should grow linearly with features
 *
 * 2. Average Dependencies per Module
 *    - Ideal: 2-5 dependencies per module
 *    - Warning: >10 dependencies → Module too coupled
 *
 * 3. Max Dependency Depth
 *    - Ideal: <5 levels deep
 *    - Warning: >7 levels → Hard to maintain
 *
 * 4. Circular Dependencies
 *    - Ideal: 0
 *    - Warning: Any circular dependency → Refactor needed
 *
 * 5. Shared Modules
 *    - Track most-used modules (utils, config, api-client)
 *    - Optimize these first (high impact)
 *
 * 6. Bundle Size by Module
 *    - Identify largest modules
 *    - Candidates for code splitting
 */

// Example metrics output
const metrics = {
  totalModules: 45,
  avgDependenciesPerModule: 3.2,
  maxDepth: 6,
  circularDependencies: 0,
  topSharedModules: [
    { name: 'utils/format-currency.ts', usedBy: 12 },
    { name: 'api-client.ts', usedBy: 8 },
    { name: 'theme-config.ts', usedBy: 6 },
  ],
  largestModules: [
    { name: 'StockChart.tsx', size: 45000 },
    { name: 'OrderForm.tsx', size: 38000 },
    { name: 'PortfolioTable.tsx', size: 32000 },
  ],
};

console.log('📊 Dependency Graph Metrics:', metrics);

/**
 * 💡 ACTIONABLE INSIGHTS:
 *
 * 1. utils/format-currency.ts used by 12 modules
 *    → Optimize this function (high impact)
 *    → Consider memoization
 *
 * 2. StockChart.tsx is 45KB
 *    → Candidate for code splitting (lazy load)
 *    → Consider using lightweight chart library
 *
 * 3. avgDependenciesPerModule: 3.2 ✅
 *    → Good! Modules are well-decoupled
 *
 * 4. circularDependencies: 0 ✅
 *    → Excellent! Clean architecture
 */
```

---

**📚 Phần 6: Caching Strategies (Chiến Lược Cache)**

#### **💡 Caching Là Gì?**

**Caching** là kỹ thuật **lưu trữ tạm thời** data/assets để **tái sử dụng** mà không cần fetch lại từ server. Trong frontend, caching giúp:

- Giảm network requests → Nhanh hơn
- Giảm server load → Tiết kiệm bandwidth
- Offline support → PWA capabilities

**🔥 Caching Strategies:**

```typescript
// ===================================================
// 🗄️ CACHING LEVELS (Các Cấp Độ Cache)
// ===================================================

/**
 * 1️⃣ BROWSER CACHE (HTTP Cache)
 * 2️⃣ SERVICE WORKER CACHE (PWA Cache)
 * 3️⃣ MEMORY CACHE (Runtime Cache)
 * 4️⃣ LOCALSTORAGE/INDEXEDDB (Persistent Cache)
 */

// ===================================================
// 1️⃣ BROWSER HTTP CACHE
// ===================================================

/**
 * 🔐 CACHE-CONTROL HEADERS
 *
 * Directives:
 * - max-age=<seconds>: Cache thời gian tối đa
 * - no-cache: Revalidate với server trước khi dùng
 * - no-store: KHÔNG cache (sensitive data)
 * - public: CDN có thể cache
 * - private: Chỉ browser cache (không CDN)
 * - immutable: File không bao giờ thay đổi
 */

// Nginx configuration (production)
server {
  location / {
    root /var/www/html;

    # 📄 HTML Files: Không cache (luôn fresh)
    location ~* \.html$ {
      add_header Cache-Control "no-cache, no-store, must-revalidate";
      add_header Pragma "no-cache";
      add_header Expires "0";
    }

    # 🎨 Static Assets với Content Hash: Cache vô thời hạn
    location ~* \.(js|css)$ {
      # File có hash (main.a3f8b2c1.js)
      if ($request_filename ~* "\.([a-f0-9]{8})\.(js|css)$") {
        add_header Cache-Control "public, max-age=31536000, immutable";
        # immutable = Browser KHÔNG revalidate (tiết kiệm requests)
      }
    }

    # 🖼️ Images: Cache 1 tháng
    location ~* \.(jpg|jpeg|png|gif|svg|webp)$ {
      add_header Cache-Control "public, max-age=2592000"; # 30 days
    }

    # 🔤 Fonts: Cache 1 năm
    location ~* \.(woff|woff2|ttf|eot)$ {
      add_header Cache-Control "public, max-age=31536000";
      add_header Access-Control-Allow-Origin "*"; # CORS for fonts
    }

    # 📦 API Responses: Không cache hoặc cache ngắn
    location /api/ {
      add_header Cache-Control "no-cache"; # Revalidate mỗi lần
      # Hoặc: Cache-Control "max-age=60" (cache 1 phút)
    }
  }
}

// ===================================================
// 🎯 CACHE STRATEGIES (Chiến Lược Cache)
// ===================================================

/**
 * 📋 CACHE FIRST (Cache trước, Network sau)
 *
 * Use case: Static assets (JS, CSS, images)
 * Flow:
 * 1. Check cache → Có → Return từ cache
 * 2. Không có → Fetch từ network → Save vào cache
 */

// Service Worker: Cache First Strategy
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((cachedResponse) => {
        if (cachedResponse) {
          // ✅ Có trong cache → Return ngay
          return cachedResponse;
        }

        // ❌ Không có → Fetch từ network
        return fetch(event.request)
          .then((networkResponse) => {
            // Save vào cache cho lần sau
            return caches.open('static-v1')
              .then((cache) => {
                cache.put(event.request, networkResponse.clone());
                return networkResponse;
              });
          });
      })
  );
});

/**
 * 🌐 NETWORK FIRST (Network trước, Cache fallback)
 *
 * Use case: API data, dynamic content
 * Flow:
 * 1. Fetch từ network → Success → Update cache & return
 * 2. Network fail → Return từ cache (stale data)
 */

self.addEventListener('fetch', (event) => {
  event.respondWith(
    fetch(event.request)
      .then((networkResponse) => {
        // ✅ Network success → Update cache
        return caches.open('api-v1')
          .then((cache) => {
            cache.put(event.request, networkResponse.clone());
            return networkResponse;
          });
      })
      .catch(() => {
        // ❌ Network fail → Fallback to cache
        return caches.match(event.request);
      })
  );
});

/**
 * 🔄 STALE WHILE REVALIDATE
 *
 * Use case: Data cần fresh nhưng chấp nhận stale (user profile, settings)
 * Flow:
 * 1. Return từ cache ngay lập tức (stale data)
 * 2. Background: Fetch từ network → Update cache
 * 3. Lần sau user load → Thấy fresh data
 */

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((cachedResponse) => {
        // 🔄 Background fetch để update cache
        const fetchPromise = fetch(event.request)
          .then((networkResponse) => {
            return caches.open('dynamic-v1')
              .then((cache) => {
                cache.put(event.request, networkResponse.clone());
                return networkResponse;
              });
          });

        // ✅ Return cache ngay lập tức (không chờ network)
        return cachedResponse || fetchPromise;
      })
  );
});

/**
 * 📡 NETWORK ONLY (Không cache)
 *
 * Use case: Sensitive data (payment, private info)
 * Flow:
 * 1. Always fetch từ network
 * 2. KHÔNG cache
 */

self.addEventListener('fetch', (event) => {
  if (event.request.url.includes('/api/payment')) {
    // ❌ Payment data → KHÔNG cache
    event.respondWith(fetch(event.request));
  }
});

/**
 * 💾 CACHE ONLY (Offline-first)
 *
 * Use case: PWA app shell, critical assets
 * Flow:
 * 1. Only use cache
 * 2. Không fetch từ network
 */

self.addEventListener('fetch', (event) => {
  if (event.request.url.includes('/app-shell')) {
    // ✅ App shell luôn từ cache (offline support)
    event.respondWith(caches.match(event.request));
  }
});

// ===================================================
// 2️⃣ SERVICE WORKER CACHE (PWA)
// ===================================================

/**
 * 📱 PWA CACHING STRATEGIES
 *
 * Service Worker = Proxy giữa browser và network
 * → Intercept requests và control caching
 */

// service-worker.js

const CACHE_VERSION = 'v1.0.0';
const STATIC_CACHE = `static-${CACHE_VERSION}`;
const API_CACHE = `api-${CACHE_VERSION}`;
const IMAGE_CACHE = `images-${CACHE_VERSION}`;

// 📦 Files to cache on install
const STATIC_ASSETS = [
  '/',
  '/index.html',
  '/main.a3f8b2c1.js',
  '/vendor.9d4e7f1a.js',
  '/styles.c4d9e2f3.css',
  '/logo.svg',
  '/offline.html' // Fallback page khi offline
];

// 🔧 Install event: Cache static assets
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(STATIC_CACHE)
      .then((cache) => {
        console.log('📦 Caching static assets...');
        return cache.addAll(STATIC_ASSETS);
      })
      .then(() => {
        // ✅ Skip waiting → Activate ngay lập tức
        return self.skipWaiting();
      })
  );
});

// 🗑️ Activate event: Xóa old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((cacheNames) => {
        return Promise.all(
          cacheNames
            .filter((name) => {
              // Xóa caches không phải version hiện tại
              return name.startsWith('static-') && name !== STATIC_CACHE ||
                     name.startsWith('api-') && name !== API_CACHE ||
                     name.startsWith('images-') && name !== IMAGE_CACHE;
            })
            .map((name) => {
              console.log('🗑️ Deleting old cache:', name);
              return caches.delete(name);
            })
        );
      })
      .then(() => {
        // ✅ Claim clients → SW control ngay
        return self.clients.claim();
      })
  );
});

// 🌐 Fetch event: Route requests to caching strategies
self.addEventListener('fetch', (event) => {
  const { request } = event;
  const url = new URL(request.url);

  // 📄 HTML: Network first
  if (request.headers.get('accept')?.includes('text/html')) {
    event.respondWith(networkFirst(request, STATIC_CACHE));
  }

  // 📦 Static assets (JS, CSS): Cache first
  else if (url.pathname.match(/\.(js|css)$/)) {
    event.respondWith(cacheFirst(request, STATIC_CACHE));
  }

  // 🖼️ Images: Cache first với fallback
  else if (url.pathname.match(/\.(png|jpg|jpeg|gif|svg|webp)$/)) {
    event.respondWith(cacheFirst(request, IMAGE_CACHE));
  }

  // 📡 API: Stale while revalidate
  else if (url.pathname.startsWith('/api/')) {
    event.respondWith(staleWhileRevalidate(request, API_CACHE));
  }

  // 🌐 Default: Network first
  else {
    event.respondWith(networkFirst(request, STATIC_CACHE));
  }
});

// Helper functions
async function cacheFirst(request, cacheName) {
  const cached = await caches.match(request);
  if (cached) return cached;

  try {
    const response = await fetch(request);
    const cache = await caches.open(cacheName);
    cache.put(request, response.clone());
    return response;
  } catch (error) {
    // Fallback to offline page
    return caches.match('/offline.html');
  }
}

async function networkFirst(request, cacheName) {
  try {
    const response = await fetch(request);
    const cache = await caches.open(cacheName);
    cache.put(request, response.clone());
    return response;
  } catch (error) {
    const cached = await caches.match(request);
    return cached || caches.match('/offline.html');
  }
}

async function staleWhileRevalidate(request, cacheName) {
  // 💡 Stale-While-Revalidate: Trả về cache ngay, fetch mới ở background
  const cached = await caches.match(request);
  //    ↑
  //    💡 Kiểm tra cache trước → Trả về ngay nếu có (dù có thể cũ)

  const fetchPromise = fetch(request).then((response) => {
    // 💡 Fetch dữ liệu mới từ network
    const cache = caches.open(cacheName);
    //    💡 Mở cache storage
    cache.then((c) => c.put(request, response.clone()));
    //    💡 Lưu response mới vào cache (clone vì response chỉ đọc 1 lần)
    return response;
  });

  return cached || fetchPromise;
  //    ↑
  //    💡 Trả về cache ngay (nếu có) HOẶC đợi fetch mới
  //    💡 UX: User thấy data ngay, data mới được update ở background
}

// ===================================================
// 3️⃣ MEMORY CACHE (Runtime Caching)
// ===================================================

/**
 * 💾 IN-MEMORY CACHING
 *
 * Cache trong RAM (JavaScript variables)
 * → Cực nhanh nhưng mất khi refresh page
 */

// Simple memory cache implementation
// 💡 Memory Cache: Cache trong RAM (JavaScript Map)
// 💡 Ưu điểm: Cực nhanh (O(1) lookup)
// 💡 Nhược điểm: Mất khi refresh page (không persistent)
class MemoryCache {
  private cache = new Map<string, { data: any; expiry: number }>();
  //    ↑
  //    💡 Map lưu key-value với expiry time

  set(key: string, data: any, ttl = 60000) {
    // ttl = time to live (ms) - Thời gian sống của cache
    // 💡 TTL mặc định: 60 giây (60000ms)
    const expiry = Date.now() + ttl;
    //    💡 Tính thời điểm hết hạn: Thời gian hiện tại + TTL
    this.cache.set(key, { data, expiry });
    //    💡 Lưu data và expiry time vào cache
  }

  get(key: string) {
    const item = this.cache.get(key);
    //    💡 Lấy item từ cache
    if (!item) return null;
    //    💡 Nếu không có → Trả về null

    // Check expiry - Kiểm tra hết hạn
    if (Date.now() > item.expiry) {
      // 💡 Nếu thời gian hiện tại > thời điểm hết hạn
      this.cache.delete(key); // Expired → Remove
      //    💡 Xóa item đã hết hạn khỏi cache
      return null;
    }

    return item.data;
    // 💡 Trả về data nếu chưa hết hạn
  }

  clear() {
    this.cache.clear();
    // 💡 Xóa toàn bộ cache
  }
}

// Usage - Cách sử dụng Memory Cache
const apiCache = new MemoryCache();
// 💡 Tạo instance của MemoryCache

async function fetchUserData(userId: string) {
  // Check cache first - Kiểm tra cache trước
  const cached = apiCache.get(`user-${userId}`);
  //    💡 Tạo key: "user-123" (userId = "123")
  //    💡 Kiểm tra xem đã có trong cache chưa
  if (cached) {
    console.log('✅ From memory cache');
    // 💡 Nếu có trong cache → Trả về ngay (không cần fetch API)
    return cached;
  }

  // Fetch từ API - Lấy dữ liệu từ server
  const response = await fetch(`/api/users/${userId}`);
  //    💡 Gọi API để lấy dữ liệu user
  const data = await response.json();
  //    💡 Parse JSON response

  // Save to cache (TTL: 5 phút) - Lưu vào cache
  apiCache.set(`user-${userId}`, data, 5 * 60 * 1000);
  //    💡 Lưu data vào cache với TTL = 5 phút (5 * 60 * 1000 ms)
  //    💡 Lần sau gọi sẽ lấy từ cache (nhanh hơn!)

  return data;
  // 💡 Trả về data
}

// ===================================================
// 4️⃣ LOCALSTORAGE / INDEXEDDB CACHE
// ===================================================

/**
 * 💾 PERSISTENT CACHE
 *
 * Cache trong disk (persistent across page reloads)
 * - LocalStorage: 5-10 MB, sync API (slow)
 * - IndexedDB: Unlimited, async API (fast)
 */

// LocalStorage Cache (simple key-value)
// 💡 LocalStorage: Persistent cache trong browser (5-10 MB limit)
// 💡 Ưu điểm: Persistent (giữ sau khi refresh), đơn giản
// 💡 Nhược điểm: Sync API (blocking), giới hạn 5-10 MB
class LocalStorageCache {
  set(key: string, data: any, ttl = 3600000) {
    // 💡 TTL mặc định: 1 giờ (3600000ms)
    const item = {
      data, // 💡 Dữ liệu cần cache
      expiry: Date.now() + ttl // 💡 Thời điểm hết hạn
    };
    localStorage.setItem(key, JSON.stringify(item));
    //    💡 Lưu vào LocalStorage (phải stringify vì chỉ lưu string)
  }

  get(key: string) {
    const itemStr = localStorage.getItem(key);
    //    💡 Lấy string từ LocalStorage
    if (!itemStr) return null;
    //    💡 Nếu không có → Trả về null

    const item = JSON.parse(itemStr);
    //    💡 Parse string về object

    // Check expiry - Kiểm tra hết hạn
    if (Date.now() > item.expiry) {
      // 💡 Nếu đã hết hạn
      localStorage.removeItem(key);
      //    💡 Xóa item khỏi LocalStorage
      return null;
    }

    return item.data;
    // 💡 Trả về data nếu chưa hết hạn
  }
}

// IndexedDB Cache (for large data)
// 💡 IndexedDB: Persistent database trong browser (unlimited size)
// 💡 Ưu điểm: Async API (non-blocking), không giới hạn size, structured data
// 💡 Nhược điểm: API phức tạp hơn LocalStorage
class IndexedDBCache {
  private dbName = 'app-cache'; // 💡 Tên database
  private storeName = 'api-responses'; // 💡 Tên object store (table)

  async open() {
    // 💡 Mở kết nối đến IndexedDB database
    return new Promise<IDBDatabase>((resolve, reject) => {
      const request = indexedDB.open(this.dbName, 1);
      //    💡 Mở database với version 1 (tăng version khi schema thay đổi)

      request.onerror = () => reject(request.error);
      //    💡 Xử lý lỗi: Reject promise nếu có lỗi
      request.onsuccess = () => resolve(request.result);
      //    💡 Thành công: Resolve với database instance

      request.onupgradeneeded = (event) => {
        // 💡 Chạy khi database chưa tồn tại hoặc version mới
        const db = (event.target as IDBOpenDBRequest).result;
        //    💡 Lấy database instance
        if (!db.objectStoreNames.contains(this.storeName)) {
          // 💡 Kiểm tra object store đã tồn tại chưa
          const store = db.createObjectStore(this.storeName, { keyPath: 'key' });
          //    💡 Tạo object store với keyPath là 'key' (primary key)
          store.createIndex('expiry', 'expiry', { unique: false });
          //    💡 Tạo index trên field 'expiry' để query nhanh hơn
        }
      };
    });
  }

  async set(key: string, data: any, ttl = 3600000) {
    // 💡 Lưu data vào IndexedDB với TTL mặc định 1 giờ
    const db = await this.open();
    //    💡 Mở database
    const transaction = db.transaction([this.storeName], 'readwrite');
    //    💡 Tạo transaction với mode 'readwrite' (cho phép ghi)
    const store = transaction.objectStore(this.storeName);
    //    💡 Lấy object store từ transaction

    const item = {
      key, // 💡 Primary key
      data, // 💡 Dữ liệu cần cache
      expiry: Date.now() + ttl // 💡 Thời điểm hết hạn
    };

    store.put(item);
    // 💡 Lưu item vào store (put = insert hoặc update nếu key đã tồn tại)
  }

  async get(key: string) {
    // 💡 Lấy data từ IndexedDB
    const db = await this.open();
    //    💡 Mở database
    const transaction = db.transaction([this.storeName], 'readonly');
    //    💡 Tạo transaction với mode 'readonly' (chỉ đọc, nhanh hơn)
    const store = transaction.objectStore(this.storeName);
    //    💡 Lấy object store

    return new Promise((resolve) => {
      const request = store.get(key);
      //    💡 Query item theo key
      request.onsuccess = () => {
        const item = request.result;
        //    💡 Lấy kết quả từ request
        if (!item) return resolve(null);
        //    💡 Nếu không có → Trả về null

        // Check expiry - Kiểm tra hết hạn
        if (Date.now() > item.expiry) {
          // 💡 Nếu đã hết hạn
          this.delete(key);
          //    💡 Xóa item khỏi database
          return resolve(null);
        }

        resolve(item.data);
        // 💡 Trả về data nếu chưa hết hạn
      };
    });
  }

  async delete(key: string) {
    // 💡 Xóa item khỏi IndexedDB
    const db = await this.open();
    //    💡 Mở database
    const transaction = db.transaction([this.storeName], 'readwrite');
    //    💡 Tạo transaction với mode 'readwrite' (cần để xóa)
    const store = transaction.objectStore(this.storeName);
    //    💡 Lấy object store
    store.delete(key);
    // 💡 Xóa item theo key
  }
}

// Usage - Cách sử dụng IndexedDB Cache
const idbCache = new IndexedDBCache();
// 💡 Tạo instance của IndexedDBCache (cho dữ liệu lớn)

async function fetchLargeData() {
  // 💡 Hàm lấy dữ liệu lớn (VD: 10MB dataset)
  const cached = await idbCache.get('large-dataset');
  //    💡 Kiểm tra cache trước (async vì IndexedDB là async API)
  if (cached) return cached;
  //    💡 Nếu có trong cache → Trả về ngay (tiết kiệm bandwidth!)

  // 💡 Nếu không có trong cache → Fetch từ API
  const response = await fetch('/api/large-dataset');
  //    💡 Gọi API để lấy dataset lớn
  const data = await response.json();
  //    💡 Parse JSON response

  await idbCache.set('large-dataset', data, 24 * 60 * 60 * 1000); // 24h
  //    💡 Lưu vào IndexedDB với TTL = 24 giờ
  //    💡 IndexedDB phù hợp cho dữ liệu lớn (không giới hạn size như LocalStorage)

  return data;
  // 💡 Trả về data
}
```

---

**Code Example (TypeScript):**

```typescript
// ============================================
// 1. ESLint + Prettier Configuration
// ============================================

// .eslintrc.js
module.exports = {
  root: true,
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaVersion: 2022,
    sourceType: 'module',
    project: './tsconfig.json'
  },
  plugins: ['@typescript-eslint', 'react', 'react-hooks'],
  extends: [
    'eslint:recommended',                          // ESLint base rules
    'plugin:@typescript-eslint/recommended',       // TypeScript rules
    'plugin:react/recommended',                    // React rules
    'plugin:react-hooks/recommended',              // React Hooks rules
    'prettier'                                     // Disable formatting rules (conflict với Prettier)
  ],
  rules: {
    // Customize rules
    '@typescript-eslint/no-unused-vars': 'error',  // ❌ Error khi có unused vars
    '@typescript-eslint/explicit-function-return-type': 'warn', // ⚠️ Warning khi không có return type
    'react/prop-types': 'off',                     // ✅ Tắt (vì dùng TypeScript)
    'no-console': 'warn',                          // ⚠️ Warning với console.log
  }
};

// .prettierrc.js
module.exports = {
  semi: true,                    // Thêm semicolon
  singleQuote: true,             // Dùng single quotes
  tabWidth: 2,                   // 2 spaces
  trailingComma: 'es5',          // Trailing comma cho ES5
  printWidth: 100,               // Max line length
  arrowParens: 'avoid',          // (x) => x thay vì (x) => x
  endOfLine: 'lf'                // Unix line endings
};

// package.json scripts
{
  "scripts": {
    "lint": "eslint . --ext .ts,.tsx",                    // Check lỗi
    "lint:fix": "eslint . --ext .ts,.tsx --fix",          // Auto-fix lỗi
    "format": "prettier --write \"**/*.{ts,tsx,json}\"",  // Format code
    "format:check": "prettier --check \"**/*.{ts,tsx,json}\"" // Check format
  }
}

// ============================================
// 2. Source Maps Configuration
// ============================================

// webpack.config.js
module.exports = {
  mode: 'production',

  // 🗺️ Source maps cho production
  devtool: 'source-map', // Tạo file .map riêng

  // Alternative options:
  // devtool: 'hidden-source-map' → Không reference trong bundle (bảo mật hơn)
  // devtool: 'eval-source-map'   → Development (rebuild nhanh)
  // devtool: 'cheap-source-map'  → Faster build, less accurate

  output: {
    filename: '[name].[contenthash].js',
    path: path.resolve(__dirname, 'dist'),

    // 🔒 Serve source maps từ private server (optional)
    sourceMapFilename: '[file].map',
    publicPath: 'https://sourcemaps.example.com/'
  }
};

// tsconfig.json
{
  "compilerOptions": {
    "sourceMap": true,  // Generate .map files cho TypeScript
    "inlineSources": true // Include source code trong .map (debugging easier)
  }
}

// 🎯 Sử dụng: Debug trong browser
// 1. Open DevTools
// 2. Source maps tự động load
// 3. Set breakpoint trong ORIGINAL TypeScript code
// 4. Xem variables với original names (không bị minified)

// ============================================
// 3. Tree-shaking Setup
// ============================================

// package.json
{
  "name": "my-app",
  "sideEffects": false, // ✅ Báo cho bundler: "safe to remove unused exports"

  // Hoặc specify files có side-effects:
  // "sideEffects": ["*.css", "*.scss", "./src/polyfills.ts"]
}

// ✅ GOOD: Named exports cho tree-shaking
// utils.ts
export function add(a: number, b: number): number {
  return a + b;
}

export function subtract(a: number, b: number): number {
  return a - b;
}

export function multiply(a: number, b: number): number {
  return a * b;
}

// app.ts
import { add } from './utils'; // ✅ Chỉ import add

console.log(add(2, 3));

// 🌲 Tree-shaking result:
// subtract() và multiply() BỊ LOẠI BỎ khỏi bundle!
// Bundle chỉ chứa add() → nhỏ hơn

// ❌ BAD: Default export + namespace import → tree-shaking KÉM
// utils.ts
export default {
  add: (a, b) => a + b,
  subtract: (a, b) => a - b,
  multiply: (a, b) => a * b
};

// app.ts
import utils from './utils'; // ❌ Import CẢ object
console.log(utils.add(2, 3));
// 🚨 Tree-shaking KHÔNG hoạt động!
// Bundle chứa cả subtract, multiply (dù không dùng)

// ❌ BAD: Barrel exports với side-effects
// index.ts (barrel file)
export * from './moduleA'; // ❌ Nếu moduleA có side-effects
export * from './moduleB';
export * from './moduleC';

// app.ts
import { funcA } from './index'; // Import from barrel
// 🚨 Bundler phải load TẤT CẢ modules (A, B, C)
// Vì không biết module nào có side-effects

// ✅ GOOD: Import trực tiếp
import { funcA } from './moduleA'; // ✅ Chỉ load moduleA

// ============================================
// 4. Code Splitting
// ============================================

// 📍 A. Route-based Code Splitting (React Router)
// 💡 Tách code theo routes → Mỗi route là 1 chunk riêng
import { lazy, Suspense } from 'react';
//    ↑      ↑
//    💡 lazy() = Lazy load component (chỉ load khi cần)
//    💡 Suspense = Hiển thị loading khi đang tải component
import { BrowserRouter, Routes, Route } from 'react-router-dom';

// ✅ Lazy load route components
// 💡 React.lazy() + dynamic import() = Code splitting tự động
const Home = lazy(() => import('./pages/Home'));
//    ↑
//    💡 Home page → Tạo file home.chunk.js riêng
//    💡 Chỉ load khi user vào route "/"

const Dashboard = lazy(() => import('./pages/Dashboard'));
//    ↑
//    💡 Dashboard page → Tạo file dashboard.chunk.js riêng
//    💡 Chỉ load khi user vào route "/dashboard"

const Profile = lazy(() => import('./pages/Profile'));
//    ↑
//    💡 Profile page → Tạo file profile.chunk.js riêng
//    💡 Chỉ load khi user vào route "/profile"

function App() {
  return (
    <BrowserRouter>
      {/* 💡 Suspense: Hiển thị "Loading..." khi đang tải chunk */}
      <Suspense fallback={<div>Loading...</div>}>
        <Routes>
          <Route path="/" element={<Home />} />
          {/* 💡 Route "/" → Load Home chunk */}
          <Route path="/dashboard" element={<Dashboard />} />
          {/* 💡 Route "/dashboard" → Load Dashboard chunk */}
          <Route path="/profile" element={<Profile />} />
          {/* 💡 Route "/profile" → Load Profile chunk */}
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
}

// 🎯 Kết quả:
// ✅ Initial load: Chỉ load main.js + home.chunk.js
//    💡 User vào trang chủ → Chỉ tải code cần thiết
//    💡 Nhanh hơn vì không tải Dashboard và Profile
// ✅ User vào /dashboard → Load dashboard.chunk.js on-demand
//    💡 Chỉ tải khi user thực sự vào route này
// ✅ User vào /profile → Load profile.chunk.js on-demand
//    💡 Chỉ tải khi user thực sự vào route này
// 💡 Lợi ích: Initial load nhanh hơn, chỉ tải code khi cần!

// 📦 B. Component-based Code Splitting
// Heavy component (Chart library)
const ChartComponent = lazy(() => import('./components/Chart'));

function Dashboard() {
  const [showChart, setShowChart] = React.useState(false);

  return (
    <div>
      <button onClick={() => setShowChart(true)}>Show Chart</button>

      {showChart && (
        <Suspense fallback={<div>Loading chart...</div>}>
          <ChartComponent /> {/* Load khi click button */}
        </Suspense>
      )}
    </div>
  );
}

// 🎯 Lợi ích: Chart library (VD: 500KB) chỉ load khi user click

// 🔧 C. Dynamic Import (Vanilla JS)
async function loadHeavyModule() {
  const module = await import('./heavy-module'); // Load on-demand
  module.doSomething();
}

// Example: Load trading calculator khi cần
document.getElementById('calculate-btn')?.addEventListener('click', async () => {
  // Load calculator module (chứa complex math logic)
  const { calculateProfit } = await import('./trading-calculator');

  const result = calculateProfit(100, 150);
  console.log(result);
});

// 📊 D. Vendor Splitting (Webpack)
// webpack.config.js
module.exports = {
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        // Tách React vào vendor chunk
        vendor: {
          test: /[\\/]node_modules[\\/](react|react-dom)[\\/]/,
          name: 'vendor',
          priority: 10
        },
        // Tách libraries khác
        libs: {
          test: /[\\/]node_modules[\\/]/,
          name: 'libs',
          priority: 5
        }
      }
    }
  }
};

// 🎯 Kết quả:
// - vendor.js (React + ReactDOM) → cache lâu dài (ít thay đổi)
// - libs.js (Lodash, Axios...) → cache lâu dài
// - main.js (App code) → thay đổi thường xuyên

// ============================================
// 5. Content Hashing (Hash File) - Cache Busting
// ============================================

/**
 * 🔐 CONTENT HASHING LÀ GÌ? (What is Content Hashing?)
 *
 * Content Hashing là kỹ thuật thêm HASH (chuỗi ký tự duy nhất) vào tên file
 * dựa trên NỘI DUNG của file. Khi nội dung thay đổi → hash thay đổi → tên file mới.
 *
 * 🎯 MỤC ĐÍCH:
 * ✅ Cache Busting: Bắt buộc browser tải file mới khi code thay đổi
 * ✅ Long-term Caching: Cache files không đổi vô thời hạn (1 năm)
 * ✅ Performance: Giảm requests cho files không đổi
 */

// ===================================================
// 🔥 VẤN ĐỀ: KHÔNG DÙNG HASH (The Problem)
// ===================================================

// 📦 Build #1 (Version 1.0 - Thứ 2)
// 💡 Build đầu tiên của ứng dụng
// dist/
//   ├── main.js        (100 KB) ← Tên file KHÔNG ĐỔI
//   │   💡 File chứa code ứng dụng chính
//   └── vendor.js      (300 KB) ← Tên file KHÔNG ĐỔI
//       💡 File chứa thư viện (React, Lodash, etc.)

// 📄 index.html
/*
<!DOCTYPE html>
<html>
<head>
  <script src="/main.js"></script>
  <!-- 💡 Browser tải và cache file này với tên "main.js" -->
  <script src="/vendor.js"></script>
  <!-- 💡 Browser tải và cache file này với tên "vendor.js" -->
</head>
</html>
*/

// 🚨 SCENARIO (Kịch bản):
// 1. 👤 User A visit website → Download main.js, vendor.js
//    💡 Browser lưu vào cache với tên "main.js" và "vendor.js"
// 2. 💾 Browser cache với header: Cache-Control: max-age=31536000 (1 năm)
//    💡 Browser sẽ dùng file từ cache trong 1 năm
// 3. 👨‍💻 Developer deploy version mới (Thứ 3)
//    → main.js code mới (fix bug quan trọng)
//    → Nhưng TÊN FILE VẪN LÀ main.js ❌
//    ⚠️ VẤN ĐỀ: Tên file không đổi → Browser nghĩ là file cũ!

// 📦 Build #2 (Version 1.1 - Thứ 3 - FIX BUG)
// 💡 Build mới với bug fix
// dist/
//   ├── main.js        (105 KB) ← Nội dung MỚI, tên file CŨ ❌
//   │   💡 Code đã được sửa (fix bug) nhưng tên file vẫn là "main.js"
//   └── vendor.js      (300 KB) ← Không đổi
//       💡 Vendor code không thay đổi

// 4. 👤 User A quay lại website
//    → Browser kiểm tra cache: "Có file main.js rồi!" ✅
//    → Browser dùng main.js từ CACHE (version cũ) ❌
//    → User KHÔNG thấy bug fix! 😱
//    → Phải Ctrl+F5 (hard refresh) để tải file mới
//    ⚠️ VẤN ĐỀ: User phải tự refresh → Không tự động!

// ❌ VẤN ĐỀ:
// - 👤 User thấy version cũ (có bug) → Trải nghiệm xấu
// - 🔄 Phải hard refresh manually → Không tiện
// - 🎛️ Không kiểm soát được cache → Khó quản lý

// ===================================================
// ✅ GIẢI PHÁP: CONTENT HASHING
// ===================================================

// 📦 Build #1 (Version 1.0 - Thứ 2)
// 💡 Build đầu tiên với Content Hashing
// dist/
//   ├── main.a3f8b2c1.js     (100 KB) ← Hash từ NỘI DUNG
//   │   💡 Hash "a3f8b2c1" được tạo từ nội dung file
//   │   💡 Nếu nội dung không đổi → Hash không đổi
//   └── vendor.9d4e7f1a.js   (300 KB) ← Hash từ NỘI DUNG
//       💡 Hash "9d4e7f1a" được tạo từ nội dung file

// 📄 index.html (auto-generated - tự động tạo)
// 💡 Bundler tự động inject tên file có hash vào HTML
/*
<!DOCTYPE html>
<html>
<head>
  <script src="/main.a3f8b2c1.js"></script>
  <!-- 💡 Tên file có hash: main.a3f8b2c1.js -->
  <script src="/vendor.9d4e7f1a.js"></script>
  <!-- 💡 Tên file có hash: vendor.9d4e7f1a.js -->
</head>
</html>
*/

// 💾 Browser cache:
// - main.a3f8b2c1.js: cached 1 năm ✅
//   💡 Browser lưu file này với tên "main.a3f8b2c1.js"
// - vendor.9d4e7f1a.js: cached 1 năm ✅
//   💡 Browser lưu file này với tên "vendor.9d4e7f1a.js"

// 📦 Build #2 (Version 1.1 - Thứ 3 - FIX BUG)
// 💡 Build mới với bug fix
// dist/
//   ├── main.f7c5d3a9.js     (105 KB) ← HASH MỚI vì nội dung đổi! ✅
//   │   💡 Nội dung file đổi (fix bug) → Hash mới: "f7c5d3a9"
//   │   💡 Tên file mới → Browser biết là file mới!
//   └── vendor.9d4e7f1a.js   (300 KB) ← HASH CŨ vì nội dung KHÔNG đổi ✅
//       💡 Nội dung file không đổi → Hash giữ nguyên: "9d4e7f1a"
//       💡 Tên file cũ → Browser dùng từ cache!

// 📄 index.html (auto-generated)
/*
<!DOCTYPE html>
<html>
<head>
  <script src="/main.f7c5d3a9.js"></script>
  <!-- 💡 Tên file MỚI! Hash đổi: a3f8b2c1 → f7c5d3a9 -->
  <script src="/vendor.9d4e7f1a.js"></script>
  <!-- 💡 Tên file CŨ (from cache) Hash không đổi -->
</head>
</html>
*/

// 👤 User A quay lại website:
// 1. 🌐 Browser fetch index.html (luôn fresh, không cache)
//    💡 index.html luôn được tải mới để lấy tên file mới nhất
// 2. 🔍 Browser thấy main.f7c5d3a9.js (tên MỚI!)
//    💡 Browser kiểm tra cache: "Không có file main.f7c5d3a9.js"
//    → Tải file mới (vì chưa có trong cache) ✅
//    💡 User nhận được version mới với bug fix!
// 3. 🔍 Browser thấy vendor.9d4e7f1a.js (tên CŨ)
//    💡 Browser kiểm tra cache: "Có file vendor.9d4e7f1a.js rồi!"
//    → Dùng từ cache (tiết kiệm 300 KB bandwidth) ✅
//    💡 Không cần tải lại vendor.js → Nhanh hơn!

// ✅ LỢI ÍCH:
// - 👤 User LUÔN thấy version mới (tự động)
//   💡 Không cần hard refresh, tự động cập nhật
// - 🔄 Không cần hard refresh
//   💡 Browser tự động tải file mới khi có hash mới
// - 💾 Cache files không đổi vô thời hạn (vendor.js)
//   💡 Files không đổi → Hash không đổi → Cache mãi mãi
// - 📥 Chỉ download files đã thay đổi (main.js)
//   💡 Tiết kiệm bandwidth, tải nhanh hơn

// ===================================================
// 🔧 CÁCH HOẠT ĐỘNG CỦA CONTENT HASHING
// ===================================================

/**
 * QUY TRÌNH TẠO HASH:
 *
 * 1. Bundler đọc NỘI DUNG file (main.js)
 * 2. Chạy hashing algorithm (MD5, SHA-256, etc.) trên nội dung
 * 3. Tạo hash string (VD: a3f8b2c1d5e9f7a2)
 * 4. Lấy 8 ký tự đầu (a3f8b2c1) để tên file ngắn gọn
 * 5. Rename file: main.js → main.a3f8b2c1.js
 * 6. Update index.html với tên file mới
 */

// Ví dụ minh họa:
const crypto = require('crypto');
const fs = require('fs');

// Đọc nội dung file
const fileContent = fs.readFileSync('dist/main.js', 'utf-8');

// Tạo hash từ nội dung (MD5)
const hash = crypto
  .createHash('md5')              // Dùng MD5 algorithm
  .update(fileContent)            // Hash nội dung file
  .digest('hex')                  // Convert sang hex string
  .substring(0, 8);               // Lấy 8 ký tự đầu

console.log(hash); // "a3f8b2c1"

// Rename file
const newFileName = `main.${hash}.js`; // "main.a3f8b2c1.js"

// ===================================================
// 📊 HASH STRATEGIES (Các Chiến Lược Hash)
// ===================================================

/**
 * 1️⃣ [contenthash] - RECOMMENDED (Khuyên dùng)
 *    Hash dựa trên NỘI DUNG file
 *    → File không đổi → hash không đổi → cache hiệu quả
 *
 * 2️⃣ [chunkhash]
 *    Hash dựa trên CHUNK (group of modules)
 *    → Modules trong cùng chunk share hash
 *
 * 3️⃣ [hash] (fullhash)
 *    Hash dựa trên TOÀN BỘ build
 *    → Build mới → TẤT CẢ files đổi hash (không tối ưu)
 */

// webpack.config.js (Webpack)
module.exports = {
  output: {
    path: path.resolve(__dirname, 'dist'),

    // ✅ RECOMMENDED: [contenthash] - hash theo nội dung
    filename: '[name].[contenthash:8].js',
    //                ↑            ↑
    //             name chunk    8 ký tự hash

    // Output: main.a3f8b2c1.js, vendor.9d4e7f1a.js

    // Alternative strategies:
    // filename: '[name].[chunkhash:8].js',  // Hash theo chunk
    // filename: '[name].[fullhash:8].js',   // Hash toàn bộ build (không khuyên)
  },

  optimization: {
    // ⚠️ QUAN TRỌNG: moduleIds: 'deterministic'
    // → Đảm bảo module IDs không đổi giữa các builds
    // → vendor.js hash KHÔNG đổi nếu code không đổi
    moduleIds: 'deterministic',

    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendor',
          priority: 10
        }
      }
    }
  }
};

// vite.config.ts (Vite)
import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        // ✅ Vite tự động dùng content hash
        entryFileNames: '[name].[hash].js',      // Entry files
        chunkFileNames: '[name].[hash].js',      // Lazy chunks
        assetFileNames: '[name].[hash].[ext]',   // CSS, images, fonts
      }
    }
  }
});

// ===================================================
// 🎯 REAL-WORLD SCENARIO (Kịch Bản Thực Tế)
// ===================================================

/**
 * 🏢 SCENARIO: E-commerce Website
 *
 * BEFORE Content Hashing:
 * ❌ Deploy version mới → Users vẫn thấy version cũ (cached)
 * ❌ Phải đợi cache expire (1 tuần) hoặc user hard refresh
 * ❌ Bug fix không đến users ngay lập tức
 *
 * AFTER Content Hashing:
 * ✅ Deploy version mới → Users TỰ ĐỘNG thấy version mới
 * ✅ Vendor files (React, libraries) cached vô thời hạn
 * ✅ Chỉ download files đã thay đổi
 */

// Build Timeline Example:
/*
┌────────────────────────────────────────────────────────────┐
│         CONTENT HASHING TIMELINE                           │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  📅 MONDAY (Build #1 - Initial Release)                   │
│  ├── dist/                                                │
│  │   ├── index.html                                      │
│  │   ├── main.a3f8b2c1.js        (50 KB - app code)     │
│  │   ├── vendor.9d4e7f1a.js      (300 KB - React, etc.) │
│  │   └── styles.c4d9e2f3.css     (10 KB)                │
│  │                                                        │
│  └── User A visit:                                        │
│      ✅ Download all files (360 KB total)                │
│      ✅ Browser cache: 1 năm                              │
│                                                            │
│  📅 TUESDAY (Build #2 - Fix Bug in App Code)             │
│  ├── dist/                                                │
│  │   ├── index.html                                      │
│  │   ├── main.f7c5d3a9.js        (52 KB) ← HASH MỚI ✅  │
│  │   ├── vendor.9d4e7f1a.js      (300 KB) ← CŨ ✅       │
│  │   └── styles.c4d9e2f3.css     (10 KB) ← CŨ ✅        │
│  │                                                        │
│  └── User A revisit:                                      │
│      ✅ Download: index.html + main.f7c5d3a9.js (52 KB) │
│      ✅ From cache: vendor.js + styles.css (310 KB)     │
│      📊 Bandwidth saved: 86% (310/360)                   │
│                                                            │
│  📅 FRIDAY (Build #3 - Upgrade React 18.2 → 18.3)        │
│  ├── dist/                                                │
│  │   ├── index.html                                      │
│  │   ├── main.f7c5d3a9.js        (52 KB) ← CŨ ✅        │
│  │   ├── vendor.b8f1a4c7.js      (305 KB) ← HASH MỚI ✅ │
│  │   └── styles.c4d9e2f3.css     (10 KB) ← CŨ ✅        │
│  │                                                        │
│  └── User A revisit:                                      │
│      ✅ Download: index.html + vendor.b8f1a4c7.js       │
│      ✅ From cache: main.js + styles.css                │
│      📊 Smart caching: Chỉ tải files đổi!               │
└────────────────────────────────────────────────────────────┘
*/

// ===================================================
// 🔐 CACHE HEADERS với CONTENT HASH
// ===================================================

// Nginx configuration (production)
server {
  location / {
    root /var/www/html;

    # ⚠️ index.html: KHÔNG cache (luôn fresh)
    location = /index.html {
      add_header Cache-Control "no-cache, no-store, must-revalidate";
      add_header Pragma "no-cache";
      add_header Expires "0";
    }

    # ✅ Hashed files: Cache vô thời hạn (1 năm)
    location ~* \.(js|css|png|jpg|jpeg|gif|svg|woff|woff2|ttf|eot)$ {
      # Nếu file có hash trong tên (VD: main.a3f8b2c1.js)
      if ($request_filename ~* "\.([a-f0-9]{8})\.(js|css)$") {
        add_header Cache-Control "public, max-age=31536000, immutable";
        # immutable = Browser KHÔNG revalidate (tiết kiệm requests)
      }
    }
  }
}

// ===================================================
// 📦 HTML INJECTION (Tự Động Inject Hash Files)
// ===================================================

// HtmlWebpackPlugin (Webpack)
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  plugins: [
    new HtmlWebpackPlugin({
      template: './public/index.html', // Template HTML
      inject: 'body',                  // Inject scripts vào <body>
      minify: true                     // Minify HTML
    })
  ]
};

// public/index.html (Template - KHÔNG có hash)
/*
<!DOCTYPE html>
<html>
<head>
  <title>My App</title>
</head>
<body>
  <div id="root"></div>
  <!-- Scripts sẽ được inject tự động -->
</body>
</html>
*/

// dist/index.html (Generated - CÓ hash)
/*
<!DOCTYPE html>
<html>
<head>
  <title>My App</title>
  <link href="/styles.c4d9e2f3.css" rel="stylesheet"> ← Auto-injected
</head>
<body>
  <div id="root"></div>
  <script src="/vendor.9d4e7f1a.js"></script>  ← Auto-injected
  <script src="/main.a3f8b2c1.js"></script>    ← Auto-injected
</body>
</html>
*/

// ===================================================
// 🎯 BEST PRACTICES (Thực Hành Tốt Nhất)
// ===================================================

/**
 * ✅ DO (NÊN):
 * 1. Dùng [contenthash] cho production builds
 * 2. Cache hashed files: max-age=31536000 (1 năm)
 * 3. KHÔNG cache index.html (luôn fresh)
 * 4. Dùng moduleIds: 'deterministic' (Webpack)
 * 5. Split vendor code (React, libraries) ra riêng
 * 6. Tên file: [name].[contenthash:8].js (8 ký tự hash)
 *
 * ❌ DON'T (KHÔNG NÊN):
 * 1. Dùng [hash] (fullhash) → tất cả files đổi hash
 * 2. Cache index.html → users không thấy version mới
 * 3. Không split vendor → download lại React mỗi deploy
 * 4. Hash quá dài (>12 ký tự) → tên file dài
 */

// ===================================================
// 📊 PERFORMANCE METRICS (Số Liệu Hiệu Suất)
// ===================================================

/**
 * 🎯 REAL APP EXAMPLE (Ứng dụng thực tế):
 *
 * WITHOUT Content Hashing:
 * ├── Build #1: Users download 1.2 MB
 * ├── Build #2 (1 tuần sau): Users download 1.2 MB (lại!) ❌
 * ├── Build #3 (1 tuần sau): Users download 1.2 MB (lại!) ❌
 * └── Total: 3.6 MB trong 3 tuần
 *
 * WITH Content Hashing:
 * ├── Build #1: Users download 1.2 MB
 * │   ├── main.js: 200 KB
 * │   ├── vendor.js: 800 KB
 * │   └── styles.css: 200 KB
 * │
 * ├── Build #2: Users download 220 KB ✅
 * │   ├── main.js: 220 KB (changed - hash mới)
 * │   ├── vendor.js: from cache (không đổi)
 * │   └── styles.css: from cache (không đổi)
 * │
 * ├── Build #3: Users download 150 KB ✅
 * │   ├── main.js: from cache (không đổi)
 * │   ├── vendor.js: from cache (không đổi)
 * │   └── styles.css: 150 KB (changed - hash mới)
 * │
 * └── Total: 1.57 MB trong 3 tuần
 *
 * 📊 Bandwidth Saved: 2.03 MB (56% nhỏ hơn!) 🚀
 * ⚡ Load Time: Nhanh hơn 3-5x (từ cache)
 */

// ===================================================
// 🔥 COMMON MISTAKES (Lỗi Thường Gặp)
// ===================================================

// ❌ MISTAKE 1: Cache index.html
// nginx.conf
location = /index.html {
  add_header Cache-Control "max-age=3600"; // ❌ SAI! Cache 1 giờ
}
// → Users không thấy deploy mới trong 1 giờ!

// ✅ FIX:
location = /index.html {
  add_header Cache-Control "no-cache"; // ✅ ĐÚNG! Luôn fresh
}

// ❌ MISTAKE 2: Dùng [hash] thay vì [contenthash]
filename: '[name].[hash:8].js'; // ❌ Tất cả files đổi hash mỗi build
// → vendor.js hash mới dù code không đổi → users tải lại 800 KB ❌

// ✅ FIX:
filename: '[name].[contenthash:8].js'; // ✅ Chỉ files đổi mới có hash mới

// ❌ MISTAKE 3: Không split vendor code
// → main.js chứa app + React (1 MB)
// → Mỗi lần sửa app → users tải lại cả React ❌

// ✅ FIX: Split vendor
optimization: {
  splitChunks: {
    cacheGroups: {
      vendor: {
        test: /[\\/]node_modules[\\/]/,
        name: 'vendor'
      }
    }
  }
}

// ===================================================
// 💡 SUMMARY (Tóm Tắt)
// ===================================================

/**
 * 🔐 CONTENT HASHING:
 *
 * ✅ LÀ GÌ?
 *    - Thêm hash vào tên file dựa trên nội dung
 *    - File thay đổi → hash mới → tên file mới
 *
 * ✅ HOẠT ĐỘNG SAO?
 *    1. Bundler hash nội dung file (MD5/SHA-256)
 *    2. Tạo string hash (a3f8b2c1)
 *    3. Rename: main.js → main.a3f8b2c1.js
 *    4. Update index.html với tên mới
 *
 * ✅ DÙNG ĐỂ LÀM GÌ?
 *    - Cache Busting: Users luôn thấy version mới
 *    - Long-term Caching: Cache files không đổi vô thời hạn
 *    - Performance: Chỉ download files đã thay đổi
 *    - Bandwidth Saving: Tiết kiệm 50-80% bandwidth
 *
 * ✅ KHI NÀO DÙNG?
 *    - LUÔN LUÔN dùng cho production builds!
 *    - Kết hợp với vendor splitting
 *    - Kết hợp với aggressive caching (1 năm)
 *
 * ✅ CÔNG CỤ:
 *    - Webpack: output.filename = '[name].[contenthash:8].js'
 *    - Vite: Tự động enable
 *    - Rollup: rollup-plugin-hash
 */

// ============================================
// 6. Real-world Trading App Example
// ============================================

// 🎯 Setup ESLint + Prettier + Tree-shaking + Code Splitting

// package.json
{
  "name": "trading-app",
  "sideEffects": [
    "*.css",
    "./src/polyfills.ts" // Polyfills có side-effects
  ],
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "lint": "eslint . --ext .ts,.tsx",
    "format": "prettier --write \"src/**/*.{ts,tsx}\""
  }
}

// vite.config.ts (Vite = modern bundler)
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],

  build: {
    sourcemap: true, // ✅ Generate source maps

    rollupOptions: {
      output: {
        // 📦 Manual chunks cho better caching
        manualChunks: {
          'vendor': ['react', 'react-dom'],
          'charts': ['recharts'], // Heavy chart library
          'utils': ['lodash-es', 'date-fns']
        }
      }
    }
  }
});

// 📂 App structure với code splitting
// src/App.tsx
import { lazy, Suspense } from 'react';
import { Routes, Route } from 'react-router-dom';

// ✅ Lazy load pages
const Dashboard = lazy(() => import('./pages/Dashboard'));
const Trading = lazy(() => import('./pages/Trading'));
const Portfolio = lazy(() => import('./pages/Portfolio'));
const Analytics = lazy(() => import('./pages/Analytics')); // Heavy (charts)

export default function App() {
  return (
    <Suspense fallback={<LoadingSpinner />}>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/trading" element={<Trading />} />
        <Route path="/portfolio" element={<Portfolio />} />
        <Route path="/analytics" element={<Analytics />} /> {/* Load khi cần */}
      </Routes>
    </Suspense>
  );
}

// src/utils/index.ts (Tree-shakable exports)
// ✅ GOOD: Named exports
export { calculateProfit } from './profit-calculator';
export { validateOrder } from './order-validator';
export { formatCurrency } from './formatters';

// KHÔNG dùng: export * from './profit-calculator' (barrel export)

// src/pages/Analytics.tsx (Lazy load heavy components)
import { lazy, Suspense } from 'react';

// ✅ Lazy load chart component (recharts lib ~500KB)
const ProfitChart = lazy(() => import('../components/ProfitChart'));

export default function Analytics() {
  return (
    <div>
      <h1>Analytics</h1>

      <Suspense fallback={<div>Loading chart...</div>}>
        <ProfitChart /> {/* Load khi render page này */}
      </Suspense>
    </div>
  );
}

// 🎯 Build results:
// ✅ main.js (50KB) - App shell + routing
// ✅ vendor.js (150KB) - React + ReactDOM (cache lâu)
// ✅ charts.js (500KB) - Recharts (load khi vào /analytics)
// ✅ dashboard.chunk.js (30KB)
// ✅ trading.chunk.js (40KB)
// ✅ portfolio.chunk.js (35KB)
// ✅ analytics.chunk.js (20KB)

// 💡 Lợi ích:
// - Initial load: 50KB + 150KB = 200KB (thay vì 825KB)
// - User vào /analytics → Load thêm charts.js (500KB) khi cần
// - Faster initial render, better UX
```

---

**Best Practices:**

1. **ESLint + Prettier**

   ```bash
   # Install
   npm install -D eslint prettier eslint-config-prettier
   npm install -D @typescript-eslint/parser @typescript-eslint/eslint-plugin

   # Run on pre-commit (husky + lint-staged)
   npx husky install
   npx husky add .husky/pre-commit "npx lint-staged"
   ```

   ```json
   // package.json
   {
     "lint-staged": {
       "*.{ts,tsx}": ["eslint --fix", "prettier --write"]
     }
   }
   ```

2. **Source Maps**

   - ✅ Development: `eval-source-map` (fast rebuild)
   - ✅ Production: `source-map` hoặc `hidden-source-map`
   - ✅ Deploy .map files riêng (không public) → bảo mật
   - ✅ Set `sourceMapFilename` để serve từ CDN riêng

3. **Tree-shaking**

   - ✅ Dùng ESM (`import/export`), KHÔNG dùng CommonJS
   - ✅ Set `sideEffects: false` trong package.json
   - ✅ Named exports thay vì default exports
   - ✅ Import trực tiếp, tránh barrel exports (`index.ts`)
   - ✅ Check bundle size: `npm run build -- --analyze`

4. **Code Splitting**

   - ✅ Route-based splitting (React Router, Next.js pages)
   - ✅ Component-based splitting (lazy load heavy components)
   - ✅ Vendor splitting (separate React, libraries...)
   - ✅ Set `Suspense` fallback cho UX tốt
   - ✅ Prefetch critical chunks: `<link rel="prefetch">`

5. **TypeScript Strict Mode**
   ```json
   // tsconfig.json
   {
     "compilerOptions": {
       "strict": true, // Enable tất cả strict checks
       "noUncheckedIndexedAccess": true, // Check array/object access
       "noImplicitReturns": true, // Function phải return
       "noFallthroughCasesInSwitch": true // Switch case phải break
     }
   }
   ```

---

**Common Mistakes:**

1. **❌ ESLint + Prettier Conflict**

   ```typescript
   // ❌ BAD: ESLint format rules conflict với Prettier
   // .eslintrc.js (KHÔNG dùng indent, quotes rules)
   {
     rules: {
       'indent': ['error', 2], // ❌ Conflict với Prettier
       'quotes': ['error', 'single'] // ❌ Conflict với Prettier
     }
   }

   // ✅ GOOD: Dùng eslint-config-prettier
   {
     extends: ['prettier'] // Tắt format rules
   }
   ```

2. **❌ Source Maps trong Production**

   ```typescript
   // ❌ BAD: Public source maps → leak source code
   // webpack.config.js
   {
     devtool: 'source-map', // .map files public
   }

   // ✅ GOOD: Hidden source maps hoặc serve riêng
   {
     devtool: 'hidden-source-map', // Không reference trong bundle
     output: {
       sourceMapFilename: '[file].map',
       publicPath: 'https://private-sourcemaps.example.com/'
     }
   }
   ```

3. **❌ Tree-shaking Không Hoạt động**

   ```typescript
   // ❌ BAD: CommonJS → tree-shaking KHÔNG work
   const utils = require('./utils'); // CommonJS

   // ❌ BAD: Default export + destructure
   export default { add, subtract, multiply };
   import utils from './utils';
   const { add } = utils; // Bundle chứa cả subtract, multiply

   // ❌ BAD: Barrel exports với side-effects
   // index.ts
   export * from './moduleA'; // moduleA có side-effects

   // ✅ GOOD: Named exports + ESM
   export function add(a, b) {
     return a + b;
   }
   import { add } from './utils'; // Chỉ bundle add()
   ```

4. **❌ Code Splitting Quá Nhiều**

   ```typescript
   // ❌ BAD: Split quá nhỏ → nhiều HTTP requests
   const Button = lazy(() => import('./Button')); // ❌ Component nhỏ không nên split
   const Icon = lazy(() => import('./Icon')); // ❌ Quá nhỏ

   // ✅ GOOD: Chỉ split components/routes nặng
   const Dashboard = lazy(() => import('./pages/Dashboard')); // ✅ Page nặng
   const ChartLibrary = lazy(() => import('./ChartLibrary')); // ✅ Library nặng (500KB+)
   ```

5. **❌ Path Alias Phá Tree-shaking**

   ```typescript
   // tsconfig.json
   {
     "paths": {
       "@utils/*": ["./src/utils/*"]
     }
   }

   // ❌ BAD: Import từ barrel file
   import { add } from '@utils'; // → import from index.ts (barrel)
   // Tree-shaking kém vì phải load toàn bộ index.ts

   // ✅ GOOD: Import trực tiếp
   import { add } from '@utils/math'; // → import trực tiếp
   ```

6. **❌ Quên Set `sideEffects`**

   ```json
   // ❌ BAD: Không set sideEffects
   // package.json
   {} // Bundler assume MỌI module có side-effects

   // ✅ GOOD: Explicit declare
   {
     "sideEffects": false // Hoặc ["*.css", "polyfills.ts"]
   }
   ```

7. **❌ Dynamic Import Không Có Error Handling**

   ```typescript
   // ❌ BAD: Không handle error
   const mod = await import('./module'); // Nếu fail → crash app

   // ✅ GOOD: Handle error
   try {
     const mod = await import('./module');
     mod.doSomething();
   } catch (error) {
     console.error('Failed to load module:', error);
     // Fallback logic
   }
   ```

---

**📚 Phần 7: Dev vs Prod Build (Development vs Production)**

#### **💡 Dev vs Prod Build - Khác Biệt Gì?**

**Development Build** và **Production Build** có mục đích và tối ưu khác nhau hoàn toàn:

```typescript
// ===================================================
// 🔧 DEVELOPMENT BUILD (Build Phát Triển)
// ===================================================

/**
 * 🎯 MỤC ĐÍCH: Developer Experience (DX)
 *
 * ✅ FEATURES:
 * - Fast rebuild (nhanh như chớp)
 * - Source maps (debug dễ dàng)
 * - Hot Module Replacement (HMR - update không reload page)
 * - Detailed error messages (lỗi chi tiết)
 * - No minification (code dễ đọc)
 * - No optimization (build nhanh)
 *
 * ❌ KHÔNG DÙNG:
 * - Minification (giữ code readable)
 * - Tree-shaking (skip để build nhanh)
 * - Image optimization (skip để build nhanh)
 * - Code splitting (optional)
 */

// webpack.config.dev.js
module.exports = {
  mode: 'development', // ✅ Development mode

  // 🗺️ Source maps: Detailed, inline
  devtool: 'eval-source-map', // Fast rebuild, accurate source maps

  // 🚫 NO minification
  optimization: {
    minimize: false, // Giữ code readable để debug
    usedExports: false, // Skip tree-shaking
    splitChunks: false // Skip code splitting
  },

  // 📦 Output: Readable code
  output: {
    filename: '[name].js', // No hash (không cần cache)
    path: path.resolve(__dirname, 'dist'),
    pathinfo: true // Include comments về modules
  },

  // 🔥 Dev Server: Hot reload
  devServer: {
    hot: true, // ✅ Hot Module Replacement
    port: 3000,
    open: true, // Auto-open browser
    historyApiFallback: true, // SPA routing support

    // 🔄 Watch files và auto-reload
    watchFiles: ['src/**/*'],

    // ⚡ Fast refresh (React)
    liveReload: true
  },

  // 🔧 Plugins: Development tools
  plugins: [
    // ❌ NO minification plugins
    // ❌ NO image optimization

    new webpack.DefinePlugin({
      'process.env.NODE_ENV': JSON.stringify('development'),
      __DEV__: true // Enable development-only code
    }),

    // 🔥 Hot Module Replacement
    new webpack.HotModuleReplacementPlugin(),

    // 📊 Bundle analyzer (optional)
    new BundleAnalyzerPlugin({
      analyzerMode: 'disabled' // Chỉ enable khi cần
    })
  ],

  // 📊 Stats: Detailed output
  stats: {
    colors: true,
    modules: true,
    reasons: true, // Why modules were included
    errorDetails: true,
    chunks: true,
    chunkModules: true
  },

  // ⚡ Performance: NO limits (accept large bundles)
  performance: {
    hints: false // Không warning về bundle size
  }
};

// vite.config.dev.ts (Vite - Modern Bundler)
import { defineConfig } from 'vite';

export default defineConfig({
  mode: 'development',

  // ⚡ Dev Server: Native ESM (SIÊU NHANH!)
  server: {
    port: 3000,
    open: true,
    hmr: true, // Hot Module Replacement

    // 🚀 Vite dùng esbuild (Go) để transpile → 100x nhanh hơn Webpack
  },

  // 🗺️ Source maps
  build: {
    sourcemap: true,
    minify: false // NO minification
  },

  // 🔧 Optimizations: DISABLED để build nhanh
  optimizeDeps: {
    force: false // Cache dependencies
  }
});

// ===================================================
// 🏭 PRODUCTION BUILD (Build Sản Xuất)
// ===================================================

/**
 * 🎯 MỤC ĐÍCH: Performance & Size Optimization
 *
 * ✅ FEATURES:
 * - Minification (code nhỏ nhất)
 * - Tree-shaking (loại dead code)
 * - Code splitting (lazy load)
 * - Image optimization (compress images)
 * - Content hashing (cache busting)
 * - Gzip/Brotli compression
 * - Remove console.log, debugger
 * - Source maps (separate .map files hoặc hidden)
 *
 * ❌ KHÔNG DÙNG:
 * - Detailed error messages (compact errors)
 * - Development-only code (__DEV__ blocks)
 * - HMR (không cần trong production)
 */

// webpack.config.prod.js
module.exports = {
  mode: 'production', // ✅ Production mode

  // 🗺️ Source maps: Separate files (hidden)
  devtool: 'source-map', // hoặc 'hidden-source-map'

  // 🗜️ FULL minification + optimization
  optimization: {
    minimize: true, // ✅ Minify code
    minimizer: [
      new TerserPlugin({
        terserOptions: {
          compress: {
            drop_console: true, // ❌ Remove console.log
            drop_debugger: true, // ❌ Remove debugger
            pure_funcs: ['console.info', 'console.debug'], // Remove specific logs
            passes: 2 // Multiple passes cho better compression
          },
          mangle: {
            safari10: true // Fix Safari 10 bugs
          },
          output: {
            comments: false, // Remove comments
            ascii_only: true // ASCII only (smaller size)
          }
        },
        extractComments: false // Không tạo .LICENSE.txt files
      }),

      // 🎨 CSS minification
      new CssMinimizerPlugin()
    ],

    // 🌲 Tree-shaking
    usedExports: true, // Mark unused exports
    sideEffects: true, // Respect package.json sideEffects

    // ✂️ Code splitting
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        // 📦 Vendor chunk (React, libraries)
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendor',
          priority: 10,
          reuseExistingChunk: true
        },
        // 🎨 CSS chunk
        styles: {
          name: 'styles',
          type: 'css/mini-extract',
          chunks: 'all',
          enforce: true
        }
      }
    },

    // 🔐 Module IDs: Deterministic (consistent hashes)
    moduleIds: 'deterministic',
    runtimeChunk: 'single' // Runtime code → separate chunk
  },

  // 📦 Output: Minified + Hashed
  output: {
    filename: '[name].[contenthash:8].js',
    chunkFilename: '[name].[contenthash:8].chunk.js',
    path: path.resolve(__dirname, 'dist'),
    publicPath: '/',
    clean: true, // Clean dist/ before build
    pathinfo: false // NO comments (smaller size)
  },

  // 🔧 Plugins: Production optimizations
  plugins: [
    new webpack.DefinePlugin({
      'process.env.NODE_ENV': JSON.stringify('production'),
      __DEV__: false // Disable development code
    }),

    // 🗜️ Gzip/Brotli compression
    new CompressionPlugin({
      algorithm: 'gzip',
      test: /\.(js|css|html|svg)$/,
      threshold: 10240, // Only compress files > 10KB
      minRatio: 0.8
    }),

    new CompressionPlugin({
      algorithm: 'brotliCompress',
      test: /\.(js|css|html|svg)$/,
      compressionOptions: { level: 11 },
      threshold: 10240,
      minRatio: 0.8,
      filename: '[path][base].br'
    }),

    // 🖼️ Image optimization
    new ImageMinimizerPlugin({
      minimizer: {
        implementation: ImageMinimizerPlugin.imageminMinify,
        options: {
          plugins: [
            ['gifsicle', { interlaced: true }],
            ['jpegtran', { progressive: true }],
            ['optipng', { optimizationLevel: 5 }],
            ['svgo', { plugins: [{ removeViewBox: false }] }]
          ]
        }
      }
    }),

    // 📊 Bundle analyzer (generate report)
    new BundleAnalyzerPlugin({
      analyzerMode: 'static',
      reportFilename: 'bundle-report.html',
      openAnalyzer: false
    }),

    // 📄 HTML injection với minification
    new HtmlWebpackPlugin({
      template: './public/index.html',
      minify: {
        removeComments: true,
        collapseWhitespace: true,
        removeRedundantAttributes: true,
        useShortDoctype: true,
        removeEmptyAttributes: true,
        removeStyleLinkTypeAttributes: true,
        keepClosingSlash: true,
        minifyJS: true,
        minifyCSS: true,
        minifyURLs: true
      }
    }),

    // 🎨 Extract CSS to separate files
    new MiniCssExtractPlugin({
      filename: '[name].[contenthash:8].css',
      chunkFilename: '[name].[contenthash:8].chunk.css'
    })
  ],

  // 📊 Stats: Minimal output
  stats: {
    colors: true,
    modules: false, // Hide modules list
    children: false,
    chunks: false,
    chunkModules: false,
    reasons: false,

    // Show warnings và errors only
    warnings: true,
    errors: true,
    errorDetails: true
  },

  // ⚡ Performance budgets
  performance: {
    hints: 'error', // Fail build nếu vượt budget
    maxEntrypointSize: 250000, // 250 KB
    maxAssetSize: 250000, // 250 KB per file
    assetFilter: (assetFilename) => {
      // Only check JS/CSS files
      return /\.(js|css)$/.test(assetFilename);
    }
  }
};

// vite.config.prod.ts
import { defineConfig } from 'vite';
import { visualizer } from 'rollup-plugin-visualizer';
import viteImagemin from 'vite-plugin-imagemin';

export default defineConfig({
  mode: 'production',

  build: {
    // 🗜️ Minification
    minify: 'esbuild', // esbuild (fast) hoặc 'terser' (smaller)

    // 🌲 Tree-shaking
    rollupOptions: {
      output: {
        // ✂️ Manual chunks
        manualChunks: {
          'vendor-react': ['react', 'react-dom'],
          'vendor-utils': ['lodash-es', 'date-fns']
        }
      }
    },

    // 🗺️ Source maps
    sourcemap: true, // hoặc 'hidden'

    // 📦 Output với content hash
    assetsInlineLimit: 4096, // Inline assets < 4KB

    // ⚡ Performance
    chunkSizeWarningLimit: 1000, // Warning nếu chunk > 1MB

    // 🎯 Target browsers
    target: 'es2015', // Modern browsers

    // 📊 Report size
    reportCompressedSize: true
  },

  // 🔧 Plugins
  plugins: [
    // 📊 Bundle analyzer
    visualizer({
      open: true,
      gzipSize: true,
      brotliSize: true
    }),

    // 🖼️ Image optimization
    viteImagemin({
      gifsicle: { optimizationLevel: 7 },
      optipng: { optimizationLevel: 7 },
      mozjpeg: { quality: 80 },
      svgo: {
        plugins: [
          { removeViewBox: false },
          { removeEmptyAttrs: false }
        ]
      }
    })
  ]
});

// ===================================================
// 📊 COMPARISON: Dev vs Prod Build
// ===================================================

/**
 * ┌──────────────────────────────────────────────────────────┐
 * │         DEV BUILD vs PROD BUILD COMPARISON               │
 * ├──────────────────────────────────────────────────────────┤
 * │                                                          │
 * │  📊 METRIC             DEV           PROD                │
 * │  ─────────────────────────────────────────────────       │
 * │  Build Time           3 seconds     45 seconds           │
 * │  Bundle Size          2.5 MB        800 KB               │
 * │  Gzip Size            N/A           240 KB               │
 * │  Source Maps          Inline        Separate (.map)      │
 * │  Minified             ❌ No         ✅ Yes               │
 * │  Tree-shaking         ❌ No         ✅ Yes               │
 * │  Code Splitting       ❌ No         ✅ Yes               │
 * │  HMR                  ✅ Yes        ❌ No                │
 * │  console.log          ✅ Keep       ❌ Remove            │
 * │  Error Details        ✅ Verbose    ⚠️ Minimal           │
 * │  Content Hash         ❌ No         ✅ Yes               │
 * │  Image Optimization   ❌ No         ✅ Yes               │
 * │  CSS Extraction       ❌ No         ✅ Yes               │
 * │  Rebuild Speed        ⚡ 100ms      ❌ N/A               │
 * │                                                          │
 * │  🎯 PRIORITY:                                            │
 * │  DEV  → Developer Experience (DX) - Speed, Debug        │
 * │  PROD → User Experience (UX) - Size, Performance        │
 * └──────────────────────────────────────────────────────────┘
 */

// ===================================================
// 🔧 CONDITIONAL CODE (Dev-only / Prod-only)
// ===================================================

// Development-only code
if (__DEV__) {
  // ✅ Chỉ chạy trong development
  console.log('🔧 Development mode enabled');

  // Performance monitoring
  if (typeof window !== 'undefined') {
    window.__REACT_DEVTOOLS_GLOBAL_HOOK__ = window.__REACT_DEVTOOLS_GLOBAL_HOOK__ || {};
  }
}

// Production-only code
if (process.env.NODE_ENV === 'production') {
  // ✅ Chỉ chạy trong production

  // Sentry error tracking
  Sentry.init({
    dsn: 'https://xxx@sentry.io/xxx',
    environment: 'production'
  });

  // Google Analytics
  gtag('config', 'GA-TRACKING-ID');
}

// ===================================================
// 📦 ENVIRONMENT VARIABLES
// ===================================================

// .env.development
/*
NODE_ENV=development
REACT_APP_API_URL=http://localhost:8000
REACT_APP_ENABLE_MOCKS=true
REACT_APP_LOG_LEVEL=debug
*/

// .env.production
/*
NODE_ENV=production
REACT_APP_API_URL=https://api.production.com
REACT_APP_ENABLE_MOCKS=false
REACT_APP_LOG_LEVEL=error
*/

// Usage trong code
const API_URL = process.env.REACT_APP_API_URL;
const ENABLE_MOCKS = process.env.REACT_APP_ENABLE_MOCKS === 'true';

if (ENABLE_MOCKS) {
  // ✅ Development: Enable MSW (Mock Service Worker)
  if (typeof window !== 'undefined') {
    const { worker } = require('./mocks/browser');
    worker.start();
  }
}

// ===================================================
// 🚀 BUILD SCRIPTS (package.json)
// ===================================================

// package.json
{
  "scripts": {
    // 🔧 Development
    "dev": "vite",                              // Dev server với HMR
    "dev:debug": "vite --debug",                // Dev với debug logs

    // 🏭 Production
    "build": "vite build",                      // Production build
    "build:analyze": "vite build --mode analyze", // Build + bundle analyzer
    "build:staging": "vite build --mode staging", // Staging build

    // 🧪 Testing builds
    "build:test": "cross-env NODE_ENV=test vite build",

    // 📊 Preview production build
    "preview": "vite preview",                  // Serve production build locally

    // 🔍 Type checking
    "type-check": "tsc --noEmit",               // Check types (không emit files)

    // 📏 Linting
    "lint": "eslint . --ext .ts,.tsx",
    "lint:fix": "eslint . --ext .ts,.tsx --fix",

    // 🎨 Formatting
    "format": "prettier --write \"src/**/*.{ts,tsx,json}\"",

    // ✅ Pre-build checks
    "prebuild": "npm run type-check && npm run lint",

    // 🔬 Bundle size check
    "size": "size-limit",

    // 🧹 Clean
    "clean": "rimraf dist"
  }
}

// ===================================================
// ⚡ BUILD PERFORMANCE OPTIMIZATION
// ===================================================

/**
 * 🚀 TIPS ĐỂ BUILD NHANH HƠN:
 *
 * 1️⃣ USE CACHE:
 */

// webpack.config.js
module.exports = {
  cache: {
    type: 'filesystem', // Cache to disk
    buildDependencies: {
      config: [__filename] // Invalidate cache khi config thay đổi
    }
  },

  // 📦 Persistent cache cho loaders
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: [
          {
            loader: 'babel-loader',
            options: {
              cacheDirectory: true, // ✅ Cache transpiled files
              cacheCompression: false // Faster cache write
            }
          }
        ]
      }
    ]
  }
};

/**
 * 2️⃣ PARALLEL BUILD:
 */

// webpack.config.js
const TerserPlugin = require('terser-webpack-plugin');

module.exports = {
  optimization: {
    minimizer: [
      new TerserPlugin({
        parallel: true, // ✅ Use multiple CPUs
        terserOptions: { /* ... */ }
      })
    ]
  }
};

/**
 * 3️⃣ SCOPE HOISTING:
 */

// webpack.config.js
module.exports = {
  optimization: {
    concatenateModules: true, // ✅ Merge modules → smaller bundle
    providedExports: true,
    usedExports: true
  }
};

/**
 * 4️⃣ USE ESBUILD (SIÊU NHANH):
 */

// vite.config.ts
export default {
  build: {
    minify: 'esbuild', // ✅ esbuild (Go) = 100x nhanh hơn Terser
  },

  optimizeDeps: {
    esbuildOptions: {
      target: 'es2020' // Modern browsers only
    }
  }
};

/**
 * 5️⃣ EXCLUDE NODE_MODULES FROM BABEL:
 */

// babel.config.js
module.exports = {
  exclude: [
    /node_modules/, // ✅ Không transpile node_modules
    /\.min\.js$/    // Skip minified files
  ]
};
```

---

**📚 Phần 8: Runtime Performance (Hiệu Năng Runtime)**

#### **💡 Runtime Performance - Tối Ưu Khi Chạy**

**Runtime Performance** là hiệu năng khi app đang chạy trong browser. Khác với build optimization (tối ưu khi build), runtime optimization tập trung vào:

- JavaScript execution speed
- Rendering performance
- Memory usage
- Network requests

```typescript
// ===================================================
// ⚡ JAVASCRIPT PERFORMANCE OPTIMIZATION
// ===================================================

/**
 * 1️⃣ AVOID BLOCKING THE MAIN THREAD
 *
 * JavaScript là single-threaded → Heavy computation block UI
 */

// ❌ BAD: Sync heavy computation (Block UI)
function processLargeData(data: number[]) {
  let result = 0;
  for (let i = 0; i < data.length; i++) {
    result += Math.sqrt(data[i]) * Math.log(data[i]); // Heavy math
  }
  return result;
}

// Main thread BLOCKED → UI frozen! ❌
const result = processLargeData(Array(10_000_000).fill(100));

// ✅ GOOD: Web Worker (Non-blocking)
// worker.ts
self.onmessage = (e) => {
  const data = e.data;
  let result = 0;

  for (let i = 0; i < data.length; i++) {
    result += Math.sqrt(data[i]) * Math.log(data[i]);
  }

  self.postMessage(result);
};

// main.ts
const worker = new Worker('worker.ts');

worker.postMessage(Array(10_000_000).fill(100));

worker.onmessage = (e) => {
  console.log('Result:', e.data);
  // ✅ UI KHÔNG bị block!
};

/**
 * 2️⃣ DEBOUNCE & THROTTLE (Giảm số lần gọi function)
 */

// ❌ BAD: Call API mỗi keystroke (quá nhiều requests!)
function handleSearch(query: string) {
  fetch(`/api/search?q=${query}`); // ❌ Gọi mỗi lần type
}

input.addEventListener('keyup', (e) => {
  handleSearch(e.target.value); // Type "hello" → 5 API calls! ❌
});

// ✅ GOOD: Debounce (Chờ user ngừng typing)
function debounce<T extends (...args: any[]) => any>(
  func: T,
  delay: number
): (...args: Parameters<T>) => void {
  let timeoutId: NodeJS.Timeout;

  return (...args: Parameters<T>) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => func(...args), delay);
  };
}

const debouncedSearch = debounce((query: string) => {
  fetch(`/api/search?q=${query}`); // ✅ Chỉ gọi khi user NGỪNG type 300ms
}, 300);

input.addEventListener('keyup', (e) => {
  debouncedSearch(e.target.value); // Type "hello" → 1 API call! ✅
});

// ✅ Throttle: Giới hạn số lần gọi trong khoảng thời gian
function throttle<T extends (...args: any[]) => any>(
  func: T,
  limit: number
): (...args: Parameters<T>) => void {
  let inThrottle: boolean;

  return (...args: Parameters<T>) => {
    if (!inThrottle) {
      func(...args);
      inThrottle = true;
      setTimeout(() => (inThrottle = false), limit);
    }
  };
}

// Use case: Scroll event (fire too many times)
const throttledScroll = throttle(() => {
  console.log('Scrolling...'); // ✅ Chỉ log MAX 1 lần / 100ms
}, 100);

window.addEventListener('scroll', throttledScroll);

/**
 * 3️⃣ MEMOIZATION (Cache kết quả tính toán)
 */

// ❌ BAD: Recalculate mỗi lần (slow!)
function fibonacci(n: number): number {
  if (n <= 1) return n;
  return fibonacci(n - 1) + fibonacci(n - 2); // ❌ Exponential time: O(2^n)
}

console.log(fibonacci(40)); // Takes 2 seconds! ❌

// ✅ GOOD: Memoization (cache results)
function memoize<T extends (...args: any[]) => any>(func: T): T {
  const cache = new Map<string, ReturnType<T>>();

  return ((...args: Parameters<T>) => {
    const key = JSON.stringify(args);

    if (cache.has(key)) {
      return cache.get(key)!; // ✅ Return from cache
    }

    const result = func(...args);
    cache.set(key, result);
    return result;
  }) as T;
}

const fibonacciMemo = memoize((n: number): number => {
  if (n <= 1) return n;
  return fibonacciMemo(n - 1) + fibonacciMemo(n - 2);
});

console.log(fibonacciMemo(40)); // Takes 0.1ms! ✅

/**
 * 4️⃣ LAZY EVALUATION (Chỉ tính khi cần)
 */

// ❌ BAD: Tính TẤT CẢ ngay lập tức
const allData = [1, 2, 3, /* ...1 million items */ 1_000_000]
  .map((x) => x * 2) // ❌ Process 1M items
  .filter((x) => x > 100) // ❌ Filter 1M items
  .slice(0, 10); // Chỉ lấy 10 items → Lãng phí! ❌

// ✅ GOOD: Generator (Lazy evaluation)
function* lazyMap<T, U>(
  iterable: Iterable<T>,
  mapper: (item: T) => U
): Generator<U> {
  for (const item of iterable) {
    yield mapper(item);
  }
}

function* lazyFilter<T>(
  iterable: Iterable<T>,
  predicate: (item: T) => boolean
): Generator<T> {
  for (const item of iterable) {
    if (predicate(item)) {
      yield item;
    }
  }
}

function* range(start: number, end: number): Generator<number> {
  for (let i = start; i < end; i++) {
    yield i;
  }
}

// ✅ Chỉ process 10 items cần thiết!
const lazyData = lazyFilter(
  lazyMap(range(1, 1_000_000), (x) => x * 2),
  (x) => x > 100
);

// Take first 10
const result = [];
for (const item of lazyData) {
  result.push(item);
  if (result.length === 10) break; // ✅ Stop early!
}

/**
 * 5️⃣ VIRTUALIZATION (Render chỉ items visible)
 */

// ❌ BAD: Render 10,000 items (DOM HUGE!)
function renderList(items: string[]) {
  const ul = document.createElement('ul');

  items.forEach((item) => {
    const li = document.createElement('li');
    li.textContent = item;
    ul.appendChild(li); // ❌ 10,000 DOM nodes! Slow!
  });

  document.body.appendChild(ul);
}

renderList(Array(10_000).fill('Item')); // ❌ Page frozen!

// ✅ GOOD: Virtual scrolling (chỉ render visible items)
// React Virtual / react-window
import { FixedSizeList } from 'react-window';

function VirtualList({ items }: { items: string[] }) {
  return (
    <FixedSizeList
      height={600} // Container height
      itemCount={items.length} // Total items: 10,000
      itemSize={35} // Each item height
      width="100%"
    >
      {({ index, style }) => (
        <div style={style}>
          {items[index]} {/* ✅ Only render ~20 visible items */}
        </div>
      )}
    </FixedSizeList>
  );
}

// ✅ Render 20 items instead of 10,000 → 500x faster!

/**
 * 6️⃣ AVOID MEMORY LEAKS
 */

// ❌ BAD: Event listener không remove (memory leak!)
class Component {
  constructor() {
    window.addEventListener('resize', this.handleResize);
    // ❌ Không remove listener → Component unmount nhưng listener còn!
  }

  handleResize = () => {
    console.log('Resizing...');
  };
}

// ✅ GOOD: Remove listener khi unmount
class ComponentFixed {
  constructor() {
    window.addEventListener('resize', this.handleResize);
  }

  handleResize = () => {
    console.log('Resizing...');
  };

  destroy() {
    window.removeEventListener('resize', this.handleResize); // ✅ Cleanup!
  }
}

// React: useEffect cleanup
function MyComponent() {
  useEffect(() => {
    const handleResize = () => console.log('Resizing...');

    window.addEventListener('resize', handleResize);

    return () => {
      window.removeEventListener('resize', handleResize); // ✅ Cleanup!
    };
  }, []);
}

/**
 * 7️⃣ REQUEST ANIMATION FRAME (Smooth animations)
 */

// ❌ BAD: setTimeout cho animations (janky!)
function animate() {
  element.style.left = position + 'px';
  position += 1;

  setTimeout(animate, 16); // ❌ Không sync với browser refresh rate
}

// ✅ GOOD: requestAnimationFrame (60 FPS)
function animateRAF() {
  element.style.left = position + 'px';
  position += 1;

  requestAnimationFrame(animateRAF); // ✅ Sync với browser (smooth!)
}

requestAnimationFrame(animateRAF);

// ===================================================
// 🎨 RENDERING PERFORMANCE
// ===================================================

/**
 * 1️⃣ AVOID LAYOUT THRASHING (Reflow/Repaint)
 */

// ❌ BAD: Read-Write-Read-Write (forced reflows!)
function updateElements(elements: HTMLElement[]) {
  elements.forEach((el) => {
    const height = el.offsetHeight; // ❌ READ (trigger reflow)
    el.style.height = height + 10 + 'px'; // ❌ WRITE (invalidate layout)
    // → Browser phải reflow mỗi iteration! Slow!
  });
}

// ✅ GOOD: Batch reads, then batch writes
function updateElementsOptimized(elements: HTMLElement[]) {
  // Phase 1: Read tất cả (1 reflow duy nhất)
  const heights = elements.map((el) => el.offsetHeight);

  // Phase 2: Write tất cả (1 repaint duy nhất)
  elements.forEach((el, i) => {
    el.style.height = heights[i] + 10 + 'px';
  });

  // ✅ Chỉ 1 reflow + 1 repaint (thay vì N reflows!)
}

/**
 * 2️⃣ USE CSS TRANSFORMS (GPU-accelerated)
 */

// ❌ BAD: Animate với top/left (trigger layout)
element.style.top = '100px'; // ❌ Layout + Paint + Composite
element.style.left = '200px';

// ✅ GOOD: Animate với transform (chỉ composite)
element.style.transform = 'translate(200px, 100px)'; // ✅ Composite only (GPU)

// ===================================================
// 💾 MEMORY OPTIMIZATION
// ===================================================

/**
 * 1️⃣ AVOID CREATING OBJECTS IN LOOPS
 */

// ❌ BAD: Create new object mỗi iteration
function processData(items: any[]) {
  items.forEach((item) => {
    const config = {
      /* ... */
    }; // ❌ New object mỗi lần!
    doSomething(item, config);
  });
}

// ✅ GOOD: Reuse object
function processDataOptimized(items: any[]) {
  const config = {
    /* ... */
  }; // ✅ Create once

  items.forEach((item) => {
    doSomething(item, config); // Reuse config
  });
}

/**
 * 2️⃣ OBJECT POOLING (Reuse objects)
 */

class ObjectPool<T> {
  private pool: T[] = [];

  constructor(
    private factory: () => T,
    private reset: (obj: T) => void,
    initialSize = 10
  ) {
    for (let i = 0; i < initialSize; i++) {
      this.pool.push(factory());
    }
  }

  acquire(): T {
    if (this.pool.length > 0) {
      return this.pool.pop()!; // ✅ Reuse from pool
    }
    return this.factory(); // Create new nếu pool empty
  }

  release(obj: T) {
    this.reset(obj);
    this.pool.push(obj); // Return to pool
  }
}

// Usage: Particle system
interface Particle {
  x: number;
  y: number;
  velocity: { x: number; y: number };
}

const particlePool = new ObjectPool<Particle>(
  () => ({ x: 0, y: 0, velocity: { x: 0, y: 0 } }), // Factory
  (p) => {
    p.x = 0;
    p.y = 0;
    p.velocity.x = 0;
    p.velocity.y = 0;
  }, // Reset
  100 // Initial pool size
);

function createParticle() {
  const particle = particlePool.acquire(); // ✅ Reuse from pool
  particle.x = Math.random() * 100;
  particle.y = Math.random() * 100;
  return particle;
}

function destroyParticle(particle: Particle) {
  particlePool.release(particle); // ✅ Return to pool (không GC!)
}
```

---

**📚 Phần 9: Security (Bảo Mật)**

#### **💡 Frontend Security - Bảo Vệ Ứng Dụng**

```typescript
// ===================================================
// 🔐 COMMON SECURITY VULNERABILITIES
// ===================================================

/**
 * 1️⃣ XSS (Cross-Site Scripting)
 *
 * Attacker inject malicious script vào page
 */

// ❌ VULNERABLE: innerHTML với user input
function displayUsername(username: string) {
  document.getElementById('user').innerHTML = username;
  // ❌ Nếu username = '<script>alert("XSS")</script>' → Execute! ❌
}

// ✅ SAFE: textContent (escape HTML)
function displayUsernameSafe(username: string) {
  document.getElementById('user').textContent = username;
  // ✅ Script được escape → Không execute
}

// ✅ SAFE: Sanitize HTML (DOMPurify)
import DOMPurify from 'dompurify';

function displayHTMLContent(html: string) {
  const clean = DOMPurify.sanitize(html, {
    ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'a'],
    ALLOWED_ATTR: ['href']
  });
  document.getElementById('content').innerHTML = clean;
  // ✅ Remove <script>, event handlers, etc.
}

/**
 * 2️⃣ CSRF (Cross-Site Request Forgery)
 *
 * Attacker trick user vào submit form từ malicious site
 */

// ✅ PROTECTION: CSRF Token
// Backend gửi CSRF token trong cookie/header
// Frontend gửi token trong request

// Axios interceptor
axios.interceptors.request.use((config) => {
  const token = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content');

  if (token) {
    config.headers['X-CSRF-Token'] = token; // ✅ Add CSRF token
  }

  return config;
});

/**
 * 3️⃣ SENSITIVE DATA EXPOSURE
 */

// ❌ BAD: Hardcode secrets trong code
const API_KEY = 'sk-1234567890abcdef'; // ❌ Committed to Git!
const PASSWORD = 'admin123'; // ❌ NEVER do this!

// ✅ GOOD: Environment variables
const API_KEY = process.env.REACT_APP_API_KEY; // ✅ From .env (not committed)

// ⚠️ WARNING: Environment variables CÔNG KHAI trong frontend!
// → KHÔNG lưu sensitive data (database passwords, private keys)
// → Chỉ dùng cho public API keys, URLs, etc.

/**
 * 4️⃣ DEPENDENCY VULNERABILITIES
 */

// ✅ Regularly audit dependencies
// npm audit
// npm audit fix

// ✅ Use Snyk, Dependabot để auto-detect vulnerabilities

// package.json
{
  "scripts": {
    "audit": "npm audit",
    "audit:fix": "npm audit fix",
    "check-deps": "npx depcheck" // Find unused deps
  }
}

/**
 * 5️⃣ CONTENT SECURITY POLICY (CSP)
 */

// ✅ CSP Header: Restrict resource loading
// index.html
/*
<meta http-equiv="Content-Security-Policy" content="
  default-src 'self';
  script-src 'self' 'unsafe-inline' https://cdn.example.com;
  style-src 'self' 'unsafe-inline';
  img-src 'self' data: https:;
  font-src 'self' data:;
  connect-src 'self' https://api.example.com;
">
*/

// Nginx
/*
add_header Content-Security-Policy "
  default-src 'self';
  script-src 'self' 'nonce-random123';
  style-src 'self' 'nonce-random456';
";
*/

/**
 * 6️⃣ SECURE COOKIES
 */

// ✅ Set cookies với security flags
document.cookie = "session=abc123; Secure; HttpOnly; SameSite=Strict";
//                                   ↑       ↑         ↑
//                                 HTTPS   No JS    No CSRF

// Backend (Express)
res.cookie('session', 'abc123', {
  httpOnly: true,   // ✅ JavaScript không access được
  secure: true,     // ✅ Chỉ send qua HTTPS
  sameSite: 'strict', // ✅ Không send cross-site (CSRF protection)
  maxAge: 3600000   // 1 hour
});

/**
 * 7️⃣ SANITIZE USER INPUT
 */

// ❌ BAD: Trust user input
function searchProducts(query: string) {
  fetch(`/api/search?q=${query}`); // ❌ SQL injection, XSS...
}

// ✅ GOOD: Validate & sanitize
import validator from 'validator';

function searchProductsSafe(query: string) {
  // Validate
  if (!validator.isAlphanumeric(query.replace(/\s/g, ''))) {
    throw new Error('Invalid search query');
  }

  // Sanitize
  const sanitized = validator.escape(query); // Escape HTML

  fetch(`/api/search?q=${encodeURIComponent(sanitized)}`); // ✅ URL encode
}

/**
 * 8️⃣ SUBRESOURCE INTEGRITY (SRI)
 */

// ✅ Verify CDN scripts không bị tamper
/*
<script
  src="https://cdn.example.com/library.js"
  integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/ux..."
  crossorigin="anonymous"
></script>
*/

// Generate SRI hash:
// openssl dgst -sha384 -binary library.js | openssl base64 -A
```

---

**📚 Phần 10: Observability & Developer Experience (DX)**

#### **💡 Monitoring & DX Tools**

````typescript
// ===================================================
// 📊 MONITORING & OBSERVABILITY
// ===================================================

/**
 * 1️⃣ ERROR TRACKING (Sentry)
 */

import * as Sentry from '@sentry/react';

Sentry.init({
  dsn: 'https://xxx@sentry.io/xxx',
  environment: process.env.NODE_ENV,
  release: process.env.REACT_APP_VERSION,

  // 🎯 Performance monitoring
  tracesSampleRate: 1.0, // 100% transactions

  // 🔍 Session replay
  replaysSessionSampleRate: 0.1, // 10% sessions
  replaysOnErrorSampleRate: 1.0, // 100% error sessions

  // 🚫 Filter sensitive data
  beforeSend(event) {
    // Remove passwords, tokens
    if (event.request) {
      delete event.request.cookies;
      delete event.request.headers?.Authorization;
    }
    return event;
  }
});

// Catch errors
try {
  throw new Error('Something went wrong');
} catch (error) {
  Sentry.captureException(error, {
    tags: { section: 'trading' },
    extra: { userId: '123' }
  });
}

/**
 * 2️⃣ PERFORMANCE MONITORING
 */

// Web Vitals (Google)
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals';

function sendToAnalytics(metric: any) {
  // Send to analytics service
  console.log(metric);

  // Google Analytics
  gtag('event', metric.name, {
    value: Math.round(metric.value),
    event_category: 'Web Vitals',
    non_interaction: true
  });
}

getCLS(sendToAnalytics);  // Cumulative Layout Shift
getFID(sendToAnalytics);  // First Input Delay
getFCP(sendToAnalytics);  // First Contentful Paint
getLCP(sendToAnalytics);  // Largest Contentful Paint
getTTFB(sendToAnalytics); // Time to First Byte

/**
 * 3️⃣ CUSTOM PERFORMANCE METRICS
 */

// Mark performance milestones
performance.mark('start-fetch');

await fetch('/api/data');

performance.mark('end-fetch');

// Measure duration
performance.measure('fetch-duration', 'start-fetch', 'end-fetch');

// Get metrics
const measures = performance.getEntriesByType('measure');
console.log('Fetch took:', measures[0].duration, 'ms');

/**
 * 4️⃣ LOGGING
 */

// Structured logging
class Logger {
  private context: Record<string, any> = {};

  setContext(key: string, value: any) {
    this.context[key] = value;
  }

  log(level: 'info' | 'warn' | 'error', message: string, data?: any) {
    const log = {
      timestamp: new Date().toISOString(),
      level,
      message,
      context: this.context,
      data
    };

    // Send to logging service
    console.log(JSON.stringify(log));

    // Send to backend
    if (level === 'error') {
      fetch('/api/logs', {
        method: 'POST',
        body: JSON.stringify(log)
      });
    }
  }
}

const logger = new Logger();
logger.setContext('userId', '123');
logger.setContext('sessionId', 'abc-456');

logger.log('error', 'API call failed', {
  url: '/api/orders',
  status: 500
});

// ===================================================
// 🛠️ DEVELOPER EXPERIENCE (DX) TOOLS
// ===================================================

/**
 * 1️⃣ TYPE CHECKING (TypeScript)
 */

// tsconfig.json (Strict mode)
{
  "compilerOptions": {
    "strict": true,                      // Enable all strict checks
    "noUncheckedIndexedAccess": true,    // Array access safety
    "noImplicitReturns": true,           // Function must return
    "noFallthroughCasesInSwitch": true,  // Switch case must break
    "exactOptionalPropertyTypes": true   // Strict optional props
  }
}

/**
 * 2️⃣ PRE-COMMIT HOOKS (Husky + lint-staged)
 *
 * 💡 Note: ESLint/Prettier configuration đã được trình bày chi tiết trong phần "Code Example" (dòng 2290-2338)
 */

// package.json
{
  "lint-staged": {
    "*.{ts,tsx}": [
      "eslint --fix",
      "prettier --write",
      "git add"
    ]
  }
}

// .husky/pre-commit
/*
#!/bin/sh
npx lint-staged
npm run type-check
npm test -- --bail --findRelatedTests
*/

/**
 * 5️⃣ DOCUMENTATION (JSDoc/TSDoc)
 */

/**
 * Calculate profit/loss for a trade
 *
 * @param buyPrice - Price when bought
 * @param sellPrice - Price when sold
 * @param quantity - Number of shares
 * @returns Profit (positive) or loss (negative)
 *
 * @example
 * ```ts
 * const profit = calculateProfit(100, 150, 10);
 * console.log(profit); // 500
 * ```
 */
function calculateProfit(
  buyPrice: number,
  sellPrice: number,
  quantity: number
): number {
  return (sellPrice - buyPrice) * quantity;
}

/**
 * 6️⃣ DEBUGGING TOOLS
 */

// React DevTools
// Redux DevTools
// Chrome DevTools Performance tab

// Custom debug utility
const DEBUG = process.env.NODE_ENV === 'development';

function debug(label: string, data: any) {
  if (DEBUG) {
    console.group(`🐛 ${label}`);
    console.log(data);
    console.trace(); // Stack trace
    console.groupEnd();
  }
}

// Usage
debug('User data', userData);

/**
 * 7️⃣ BUNDLE SIZE MONITORING
 */

// size-limit (package.json)
{
  "size-limit": [
    {
      "path": "dist/main.*.js",
      "limit": "200 KB"
    },
    {
      "path": "dist/vendor.*.js",
      "limit": "400 KB"
    }
  ]
}

// Run: npm run size
// Fails CI nếu vượt limit → Force optimization!
````

---

**🎓 SUMMARY (Tổng Kết Toàn Bộ)**

```
┌────────────────────────────────────────────────────────────────┐
│     FRONTEND TOOLING & BUILD OPTIMIZATION - COMPLETE GUIDE     │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  📦 DEPENDENCY GRAPH                                           │
│  ├─ Mô tả quan hệ giữa modules                                │
│  ├─ Detect circular dependencies                              │
│  ├─ Determine load order (topological sort)                   │
│  └─ Visualize: webpack-bundle-analyzer, nx graph              │
│                                                                │
│  🗂️ BUNDLING                                                  │
│  ├─ Gộp nhiều files → 1-2 bundles                            │
│  ├─ Giảm HTTP requests (100 requests → 1 request)            │
│  ├─ Tools: Webpack, Vite, Rollup                             │
│  └─ Optimization: Vendor splitting, async chunks             │
│                                                                │
│  🌲 TREE-SHAKING                                              │
│  ├─ Loại unused exports (dead code elimination)              │
│  ├─ Yêu cầu: ESM (import/export), sideEffects: false         │
│  ├─ Named exports > Default exports                          │
│  └─ Example: Lodash 70KB → uniq 2KB (97% smaller)            │
│                                                                │
│  ✂️ CODE SPLITTING                                            │
│  ├─ Tách code thành nhiều chunks                             │
│  ├─ Route-based: React.lazy(), dynamic import()              │
│  ├─ Component-based: Lazy load heavy components              │
│  └─ Result: Initial load 800KB → 200KB (75% faster)          │
│                                                                │
│  🗜️ MINIFICATION                                              │
│  ├─ Remove whitespace, comments                              │
│  ├─ Shorten variable names (calculateTotal → a)              │
│  ├─ Tools: Terser, esbuild                                   │
│  └─ Result: 850KB → 280KB (67% smaller)                      │
│                                                                │
│  🔄 TRANSPILING                                               │
│  ├─ ES2020+ → ES5 (old browsers)                             │
│  ├─ TypeScript → JavaScript                                  │
│  ├─ JSX → JavaScript                                          │
│  └─ Tools: Babel, TypeScript, SWC                            │
│                                                                │
│  🔌 POLYFILLS                                                 │
│  ├─ Add missing features (Promise, fetch, async/await)       │
│  ├─ Differential serving: Modern vs Legacy bundles           │
│  ├─ Tools: core-js, polyfill.io                              │
│  └─ Strategy: Import only needed polyfills                   │
│                                                                │
│  💾 CACHING                                                   │
│  ├─ Content hashing: main.[hash].js                          │
│  ├─ Cache strategies: Cache-first, Network-first, SWR        │
│  ├─ Service Worker: PWA offline support                      │
│  └─ Result: 56% bandwidth saved, 3-5x faster loads           │
│                                                                │
│  🔧 DEV vs PROD BUILD                                         │
│  ├─ Dev: Fast rebuild (3s), HMR, source maps, no minify     │
│  ├─ Prod: Minify, tree-shake, split, hash, optimize         │
│  ├─ Dev: 2.5MB (readable) vs Prod: 240KB (optimized)        │
│  └─ Tools: mode: 'development' vs 'production'               │
│                                                                │
│  ⚡ RUNTIME PERFORMANCE                                       │
│  ├─ Web Workers: Non-blocking heavy computation              │
│  ├─ Debounce/Throttle: Reduce function calls                 │
│  ├─ Memoization: Cache expensive calculations                │
│  ├─ Virtualization: Render only visible items                │
│  └─ Memory: Avoid leaks, object pooling                      │
│                                                                │
│  🔐 SECURITY                                                  │
│  ├─ XSS: Sanitize HTML (DOMPurify)                           │
│  ├─ CSRF: Token protection                                   │
│  ├─ CSP: Content Security Policy                             │
│  ├─ Secure cookies: HttpOnly, Secure, SameSite               │
│  └─ Dependencies: npm audit, Snyk, Dependabot                │
│                                                                │
│  📊 OBSERVABILITY & DX                                        │
│  ├─ Error tracking: Sentry                                   │
│  ├─ Performance: Web Vitals (LCP, FID, CLS)                  │
│  ├─ Logging: Structured logs                                 │
│  ├─ DX: TypeScript strict, ESLint, Prettier                  │
│  ├─ Pre-commit: Husky + lint-staged                          │
│  └─ Bundle size: size-limit, bundle analyzer                 │
│                                                                │
│  🗺️ SOURCE MAPS                                              │
│  ├─ Map minified code → original source                      │
│  ├─ Dev: eval-source-map (fast rebuild)                      │
│  ├─ Prod: source-map or hidden-source-map                    │
│  └─ Debug với original code, variables, line numbers         │
│                                                                │
│  🎨 ESLINT / PRETTIER                                         │
│  ├─ ESLint: Find bugs, enforce patterns                      │
│  ├─ Prettier: Auto-format code                               │
│  ├─ Integration: eslint-config-prettier                      │
│  └─ Automation: Pre-commit hooks                             │
└────────────────────────────────────────────────────────────────┘

📈 REAL-WORLD IMPACT:
├─ Initial load: 2.5MB → 240KB (90% faster) 🚀
├─ Build time: Dev 3s, Prod 45s
├─ Cache hit rate: 80-90% (returning users)
├─ Bandwidth saved: 56% on average
├─ Error rate: Reduced 70% (Sentry monitoring)
└─ Developer productivity: +40% (better DX tools)

🎯 KEY TAKEAWAYS:
✅ Bundling: Fewer requests → Faster loads
✅ Minification: Smaller files → Less bandwidth
✅ Tree-shaking: Remove dead code → Smaller bundles
✅ Code splitting: Lazy load → Faster initial render
✅ Caching: Content hash + strategies → 80% cache hit
✅ Security: XSS, CSRF, CSP → Protect users
✅ Monitoring: Sentry, Web Vitals → Catch issues early
✅ DX: TypeScript, ESLint, Prettier → Better code quality
```

---
