# 🏗️ Q44: Frontend Tooling & Build Optimization - Bundling, Minify, Tree-shaking, Code Splitting, Polyfill, Transpiling, ESLint/Prettier, Source Maps




**❓ Câu Hỏi:**

Giải thích chi tiết các công cụ và kỹ thuật tối ưu hóa trong frontend development: Bundling (gộp file), Minify (nén code), Tree-shaking (loại bỏ code thừa), Code splitting (tách code), Polyfill (thêm features cho old browsers), Transpiling (convert modern → old JS), ESLint/Prettier, và Source Maps. Bao gồm cách hoạt động, ưu nhược điểm, và ứng dụng thực tế.



**📚 Phần 1: Bundling (Gộp File) - Từ Nhiều Files → 1 File**

#### **💡 Bundling Là Gì? (What is Bundling?)**

**Bundling** là quá trình **gộp nhiều files JavaScript/CSS/assets** thành **ít files hơn** (thường là 1 file duy nhất) để gửi lên browser.

**🔥 Tại Sao Cần Bundling?**

```typescript
// ===================================================
// ❌ KHÔNG DÙNG BUNDLING - Website có 100 files
// ===================================================

// index.html
<!DOCTYPE html>
<html>
<head>
  <!-- ❌ Load 100 files riêng biệt! -->
  <script src="/js/utils.js"></script>
  <script src="/js/api.js"></script>
  <script src="/js/auth.js"></script>
  <script src="/js/components/Button.js"></script>
  <script src="/js/components/Input.js"></script>
  <!-- ...95 files khác -->
</head>
</html>

// 🚨 VẤN ĐỀ:
// ❌ 100 HTTP requests → CỰC CHẬM! (mỗi request có latency ~50-100ms)
// ❌ Total latency: 100 files × 100ms = 10 giây chỉ để load files! 😱
// ❌ HTTP/1.1: Chỉ 6-8 connections đồng thời → phải chờ từng wave
// ❌ Không optimize được (không minify, tree-shake được)

// ===================================================
// ✅ DÙNG BUNDLING - Gộp thành 1 file
// ===================================================

// index.html
<!DOCTYPE html>
<html>
<head>
  <!-- ✅ Load 1 file duy nhất! -->
  <script src="/js/bundle.js"></script>
</head>
</html>

// bundle.js (gộp 100 files thành 1)
// - Chứa tất cả code từ 100 files
// - Đã minify (nén nhỏ hơn)
// - Đã tree-shake (loại code thừa)

// ✅ LỢI ÍCH:
// ✅ 1 HTTP request → NHANH HƠN 100x!
// ✅ Latency: 1 file × 100ms = 100ms (vs 10 giây)
// ✅ Có thể optimize (minify, compress, cache)
```

**🎯 Cách Hoạt Động Của Bundler:**

```
┌──────────────────────────────────────────────────────────┐
│               BUNDLING PROCESS (QUY TRÌNH GỘP FILE)      │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  📁 INPUT: Source files (nhiều files)                   │
│  ├── src/                                               │
│  │   ├── index.js        (10 KB)   ← Entry point       │
│  │   ├── utils.js        (5 KB)                         │
│  │   ├── api.js          (8 KB)                         │
│  │   └── components/                                    │
│  │       ├── Button.js   (3 KB)                         │
│  │       └── Input.js    (4 KB)                         │
│  │                                                       │
│  │   Total: 5 files, 30 KB                             │
│  └─────────────────────────────────────────────────     │
│                                                          │
│  🔍 STEP 1: Dependency Resolution (Phân tích phụ thuộc) │
│  ├── Bundler đọc index.js (entry point)                │
│  ├── Tìm tất cả imports/requires trong index.js        │
│  ├── Đệ quy tìm imports trong utils.js, api.js, ...    │
│  └── Tạo dependency graph (sơ đồ phụ thuộc):           │
│      index.js                                           │
│        ├─ utils.js                                      │
│        ├─ api.js                                        │
│        │   └─ utils.js (đã có, skip)                   │
│        └─ components/                                   │
│            ├─ Button.js                                 │
│            └─ Input.js                                  │
│                                                          │
│  🔄 STEP 2: Transform (Biến đổi code)                  │
│  ├── TypeScript → JavaScript (nếu dùng TS)             │
│  ├── JSX → JavaScript (nếu dùng React)                 │
│  ├── ES6+ → ES5 (nếu cần hỗ trợ IE11)                  │
│  └── CSS Modules → Scoped CSS                          │
│                                                          │
│  🌲 STEP 3: Tree Shaking (Loại code thừa)             │
│  ├── Phân tích exports/imports                         │
│  ├── Loại bỏ functions/variables không dùng           │
│  └── 30 KB → 22 KB (loại 8 KB code thừa)              │
│                                                          │
│  📦 STEP 4: Bundle (Gộp files)                         │
│  ├── Gộp tất cả files thành 1 file                     │
│  ├── Wrap mỗi module trong function scope              │
│  └── 22 KB code trong 1 file: bundle.js                │
│                                                          │
│  🗜️ STEP 5: Minify (Nén code)                          │
│  ├── Remove whitespace, comments                       │
│  ├── Shorten variable names (userName → a)            │
│  ├── Remove unused code                                │
│  └── 22 KB → 8 KB (nén 64%!)                           │
│                                                          │
│  📤 OUTPUT: Bundle file (1 file duy nhất)              │
│  └── dist/                                              │
│      └── bundle.min.js   (8 KB)  ← 1 file tối ưu!     │
│                                                          │
│  ✅ KẾT QUẢ: 5 files (30 KB) → 1 file (8 KB)          │
│  ✅ Giảm 73% kích thước!                                │
│  ✅ Giảm từ 5 HTTP requests → 1 request!               │
└──────────────────────────────────────────────────────────┘
```

**💻 Code Example - Trước và Sau Bundling:**

```typescript
// ===================================================
// 📁 TRƯỚC BUNDLING - Nhiều files riêng biệt
// ===================================================

// src/utils.js
export function add(a, b) {
  return a + b;
}

export function subtract(a, b) {
  return a - b;
}

// src/api.js
import { add } from './utils.js';

export async function fetchData() {
  const response = await fetch('/api/data');
  const data = await response.json();
  return add(data.count, 10); // Dùng add từ utils
}

// src/index.js (Entry point)
import { fetchData } from './api.js';
import { subtract } from './utils.js';

async function main() {
  const result = await fetchData();
  const final = subtract(result, 5);
  console.log(final);
}

main();

// ===================================================
// 📦 SAU BUNDLING - 1 file duy nhất (bundle.js)
// ===================================================

// dist/bundle.js (Simplified version - thực tế phức tạp hơn)
(function() {
  // Module: utils.js
  const utils = {
    add: function(a, b) { return a + b; },
    subtract: function(a, b) { return a - b; }
  };
  
  // Module: api.js
  const api = {
    fetchData: async function() {
      const response = await fetch('/api/data');
      const data = await response.json();
      return utils.add(data.count, 10);
    }
  };
  
  // Module: index.js (Entry)
  async function main() {
    const result = await api.fetchData();
    const final = utils.subtract(result, 5);
    console.log(final);
  }
  
  main();
})();

// ✅ Tất cả code trong 1 file!
// ✅ Modules được wrap trong function scope (tránh global pollution)
// ✅ Dependencies được resolve (utils, api, index)
```

---

**📚 Phần 2: Minify (Nén Code) - Làm Code Nhỏ Gọn**

#### **💡 Minify Là Gì? (What is Minification?)**

**Minify** là quá trình **loại bỏ tất cả ký tự không cần thiết** khỏi code (whitespace, comments, newlines) và **rút ngắn tên biến** để giảm kích thước file.

**🔥 Minify Làm Gì?**

```typescript
// ===================================================
// 📝 TRƯỚC MINIFY - Code dễ đọc (10 KB)
// ===================================================

// Original code (readable - dễ đọc)
function calculateTotalPrice(items, taxRate, discount) {
  // Calculate subtotal - Tính tổng tiền hàng
  let subtotal = 0;
  
  for (let i = 0; i < items.length; i++) {
    const item = items[i];
    subtotal += item.price * item.quantity;
  }
  
  // Apply discount - Áp dụng giảm giá
  const discountedPrice = subtotal * (1 - discount / 100);
  
  // Add tax - Thêm thuế
  const tax = discountedPrice * (taxRate / 100);
  const total = discountedPrice + tax;
  
  return total;
}

// Exported function for external use
export { calculateTotalPrice };

// ===================================================
// 🗜️ SAU MINIFY - Code khó đọc nhưng NHỎ (3 KB)
// ===================================================

// Minified code (unreadable - khó đọc nhưng nhỏ)
function c(a,b,d){let e=0;for(let f=0;f<a.length;f++){const g=a[f];e+=g.price*g.quantity}const h=e*(1-d/100),i=h*(b/100);return h+i}export{c};

// 🎯 NHỮNG GÌ ĐÃ THAY ĐỔI:
// ✅ Remove comments (// Calculate subtotal, etc.) → Tiết kiệm ~200 bytes
// ✅ Remove whitespace (spaces, tabs) → Tiết kiệm ~500 bytes
// ✅ Remove newlines → Tiết kiệm ~300 bytes
// ✅ Shorten variable names:
//    - calculateTotalPrice → c
//    - items → a
//    - taxRate → b
//    - discount → d
//    - subtotal → e
//    - item → g
//    - discountedPrice → h
//    - tax → i
// ✅ Remove unnecessary semicolons, braces → Tiết kiệm ~50 bytes
//
// 📊 KẾT QUẢ: 10 KB → 3 KB (Giảm 70%!)
```

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
function add(a,b){return a+b}

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
function c(a,b){let d=0;for(let e=0;e<a.length;e++){if(a[e]===b[e]){d+=10}}return d}

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
if(user.isActive)console.log('Active')

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
function process(a){return a+10}

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
  calculateAge: function() { return 2024 - this.birthYear; }
};

// After (mangle property names - CẨN THẬN!)
const user = {
  a: 'John',    // firstName → a
  b: 'Doe',     // lastName → b
  c: function() { return 2024 - this.d; } // calculateAge → c
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

```typescript
// ===================================================
// 📦 LIBRARY: math-utils.js (Thư viện toán học)
// ===================================================

// Export 10 functions (nhưng app chỉ dùng 2)
export function add(a, b) {
  return a + b;
}

export function subtract(a, b) {
  return a - b;
}

export function multiply(a, b) {
  return a * b;
}

export function divide(a, b) {
  return a / b;
}

export function power(a, b) {
  return Math.pow(a, b);
}

export function sqrt(a) {
  return Math.sqrt(a);
}

export function abs(a) {
  return Math.abs(a);
}

export function round(a) {
  return Math.round(a);
}

export function floor(a) {
  return Math.floor(a);
}

export function ceil(a) {
  return Math.ceil(a);
}

// ===================================================
// 📱 APP: index.js (Chỉ dùng 2 functions)
// ===================================================

import { add, subtract } from './math-utils.js';
//       ↑      ↑
//       Chỉ import 2 functions (add, subtract)
//       8 functions còn lại KHÔNG import

const result1 = add(10, 20);        // ✅ Dùng add
const result2 = subtract(50, 30);   // ✅ Dùng subtract

console.log(result1, result2);

// ===================================================
// 🌲 TREE SHAKING RESULT (Kết quả sau tree shake)
// ===================================================

// ❌ KHÔNG DÙNG Tree Shaking:
// Bundle chứa TẤT CẢ 10 functions (kể cả 8 functions không dùng)
// Bundle size: ~2 KB

// ✅ DÙNG Tree Shaking:
// Bundle CHỈ chứa 2 functions (add, subtract)
// 8 functions còn lại bị LOẠI BỎ hoàn toàn
// Bundle size: ~400 bytes

// 📊 Giảm 80% kích thước! 🚀
```

**🔍 Tree Shaking Deep Dive - Phân Tích Chi Tiết:**

```
┌──────────────────────────────────────────────────────────┐
│         TREE SHAKING PROCESS (Quy trình rũ cây)          │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  🌳 STEP 1: Build Dependency Tree (Xây cây phụ thuộc)  │
│                                                          │
│         index.js (Entry)                                │
│            │                                             │
│            ├─ import { add, subtract } from math-utils  │
│            │                                             │
│         math-utils.js                                   │
│            ├─ export add ✅ (USED - được dùng)          │
│            ├─ export subtract ✅ (USED - được dùng)     │
│            ├─ export multiply ❌ (UNUSED - không dùng)  │
│            ├─ export divide ❌ (UNUSED)                 │
│            ├─ export power ❌ (UNUSED)                  │
│            ├─ export sqrt ❌ (UNUSED)                   │
│            ├─ export abs ❌ (UNUSED)                    │
│            ├─ export round ❌ (UNUSED)                  │
│            ├─ export floor ❌ (UNUSED)                  │
│            └─ export ceil ❌ (UNUSED)                   │
│                                                          │
│  ✂️ STEP 2: Mark Unused Exports (Đánh dấu không dùng)  │
│  ├── Scan tất cả imports trong app                     │
│  ├── Đánh dấu exports nào được import                  │
│  └── Exports KHÔNG được import = UNUSED (thừa)         │
│                                                          │
│  🗑️ STEP 3: Remove Dead Code (Xóa code thừa)          │
│  ├── Loại bỏ 8 functions không dùng                    │
│  ├── Chỉ giữ lại add và subtract                       │
│  └── Bundle size: 2 KB → 400 bytes                     │
│                                                          │
│  ✅ OUTPUT: Optimized bundle (Bundle tối ưu)           │
│  └── Chỉ chứa code THỰC SỰ được dùng                   │
└──────────────────────────────────────────────────────────┘
```

**⚠️ Điều Kiện Để Tree Shaking Hoạt Động:**

```typescript
// ===================================================
// ✅ YÊU CẦU 1: Dùng ES Modules (import/export)
// ===================================================

// ✅ GOOD: ES Modules - Tree shaking hoạt động
export function add(a, b) {
  return a + b;
}

import { add } from './utils.js';

// ❌ BAD: CommonJS - Tree shaking KHÔNG hoạt động
module.exports = {
  add: function(a, b) { return a + b; }
};

const { add } = require('./utils.js');

// 🔍 TẠI SAO?
// ES Modules: Static imports (biết lúc build time exports nào được dùng)
// CommonJS: Dynamic requires (chỉ biết lúc runtime → không tree shake được)

// ===================================================
// ✅ YÊU CẦU 2: sideEffects: false trong package.json
// ===================================================

// package.json
{
  "name": "my-library",
  "sideEffects": false, // ✅ Báo: "Safe to remove unused exports"
}

// Hoặc chỉ định files có side-effects:
{
  "sideEffects": [
    "*.css",           // CSS files có side-effects (apply styles globally)
    "*.scss",
    "./src/polyfills.ts" // Polyfills có side-effects (modify globals)
  ]
}

// 🔍 SIDE-EFFECTS LÀ GÌ?
// Code có tác dụng phụ khi import (không chỉ export functions/classes)

// ❌ Code có side-effects (KHÔNG tree shake được):
// logger.js
console.log('Logger initialized'); // ⚠️ Side-effect: console.log khi import
window.logger = { log: (msg) => console.log(msg) }; // ⚠️ Modify global

export function log(message) {
  console.log(message);
}

// App import logger:
import { log } from './logger.js';
// → logger.js được execute ngay lập tức
// → console.log('Logger initialized') chạy
// → window.logger được tạo
// → Bundler KHÔNG DÁM xóa code này (vì có side-effects)

// ✅ Code KHÔNG có side-effects (tree shake được):
// math.js
export function add(a, b) {
  return a + b; // ✅ Pure function - không side-effects
}

// ===================================================
// ✅ YÊU CẦU 3: Named Exports (không dùng default export)
// ===================================================

// ❌ BAD: Default export + destructuring → Tree shake KÉM
// utils.js
export default {
  add: (a, b) => a + b,
  subtract: (a, b) => a - b,
  multiply: (a, b) => a * b,
};

// app.js
import utils from './utils.js';
const result = utils.add(1, 2);
// 🚨 Bundler phải include TOÀN BỘ object (vì không biết property nào được dùng)

// ✅ GOOD: Named exports → Tree shake TỐT
// utils.js
export const add = (a, b) => a + b;
export const subtract = (a, b) => a - b;
export const multiply = (a, b) => a * b;

// app.js
import { add } from './utils.js';
const result = add(1, 2);
// ✅ Bundler chỉ include add, loại bỏ subtract và multiply

// ===================================================
// ❌ ANTI-PATTERN: Barrel Exports (Re-exports)
// ===================================================

// ❌ BAD: Barrel file (index.js) re-export tất cả
// index.js
export * from './moduleA'; // Re-export tất cả từ moduleA
export * from './moduleB';
export * from './moduleC';

// app.js
import { funcA } from './index.js'; // Import từ barrel
// 🚨 Bundler phải load TẤT CẢ modules (A, B, C)
// Vì barrel file có thể có side-effects

// ✅ GOOD: Import trực tiếp
import { funcA } from './moduleA.js';
// ✅ Chỉ load moduleA, không load B và C
```

**🎯 Real-World Tree Shaking Example:**

```typescript
// ===================================================
// 📦 VÍ DỤ THỰC TẾ: Lodash Library
// ===================================================

// ❌ BAD: Import toàn bộ Lodash (~70 KB!)
import _ from 'lodash';

const result = _.uniq([1, 2, 2, 3]);
// 🚨 Bundle bao gồm TOÀN BỘ Lodash (300+ functions)
// → Bundle size: +70 KB

// ✅ GOOD: Import chỉ function cần dùng
import uniq from 'lodash/uniq'; // Chỉ import uniq function

const result = uniq([1, 2, 2, 3]);
// ✅ Bundle chỉ bao gồm uniq function (~2 KB)
// → Bundle size: +2 KB

// 📊 Tiết kiệm: 68 KB! (97% nhỏ hơn)

// ✅ BETTER: Dùng lodash-es (ES Modules version)
import { uniq } from 'lodash-es';
// → Tree shaking tự động loại bỏ functions không dùng
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

**Hoạt động:**

```
┌─────────────────────────────────────────────────────────────┐
│              COMPLETE TOOLING WORKFLOW                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. DEVELOPMENT (ESLint + Prettier)                        │
│  ┌──────────────────────────────────────┐                  │
│  │  Write modern code (ES2020+, TS)    │                  │
│  │    ↓                                 │                  │
│  │  ESLint check (errors, warnings)    │                  │
│  │    ↓                                 │                  │
│  │  Prettier format (auto-fix)         │                  │
│  │    ↓                                 │                  │
│  │  Clean, consistent code ✅           │                  │
│  └──────────────────────────────────────┘                  │
│                                                             │
│  2. BUILD PROCESS (Full Pipeline)                         │
│  ┌──────────────────────────────────────┐                  │
│  │  Source: 100 files, 500 KB, ES2020  │                  │
│  │    ↓                                 │                  │
│  │  TRANSPILING (Babel/TypeScript)     │                  │
│  │  - ES2020 → ES5 (arrow fn → fn)    │                  │
│  │  - TypeScript → JavaScript          │                  │
│  │  - JSX → JavaScript                 │                  │
│  │    ↓                                 │                  │
│  │  POLYFILLING (core-js)              │                  │
│  │  - Add Promise, fetch, Array.from   │                  │
│  │  - Only import used polyfills       │                  │
│  │    ↓                                 │                  │
│  │  Transpiled: 100 files, 550 KB, ES5│                  │
│  │    ↓                                 │                  │
│  │  BUNDLING (Webpack/Vite)            │                  │
│  │  - Gộp 100 files → 1 file           │                  │
│  │  - Resolve dependencies             │                  │
│  │    ↓                                 │                  │
│  │  Bundle: 1 file, 550 KB             │                  │
│  │    ↓                                 │                  │
│  │  TREE-SHAKING (Remove dead code)   │                  │
│  │  - Analyze imports/exports          │                  │
│  │  - Remove unused functions          │                  │
│  │    ↓                                 │                  │
│  │  Optimized: 1 file, 300 KB ✅       │                  │
│  │    ↓                                 │                  │
│  │  MINIFY (Terser/esbuild)            │                  │
│  │  - Remove whitespace, comments      │                  │
│  │  - Shorten variable names           │                  │
│  │    ↓                                 │                  │
│  │  Minified: 1 file, 100 KB ✅        │                  │
│  │    ↓                                 │                  │
│  │  CODE SPLITTING (Dynamic imports)   │                  │
│  │  - Split by routes/components       │                  │
│  │  - Vendor chunk (React, libs...)    │                  │
│  │    ↓                                 │                  │
│  │  Final Output:                       │                  │
│  │  - main.js (30KB) - App logic       │                  │
│  │  - vendor.js (40KB) - Libraries     │                  │
│  │  - lazy-1.js (15KB) - Route 1       │                  │
│  │  - lazy-2.js (15KB) - Route 2       │                  │
│  │  Total: 100KB (split into 4 chunks)│                  │
│  └──────────────────────────────────────┘                  │
│                                                             │
│  3. PRODUCTION (Source Maps + Differential Serving)       │
│  ┌──────────────────────────────────────┐                  │
│  │  Modern browsers:                    │                  │
│  │  - Load modern.js (ES2020, 80KB)    │                  │
│  │  - No polyfills needed              │                  │
│  │    ↓                                 │                  │
│  │  Old browsers (IE11):               │                  │
│  │  - Load legacy.js (ES5, 100KB)     │                  │
│  │  - Includes polyfills               │                  │
│  │    ↓                                 │                  │
│  │  Debug với Source Maps:             │                  │
│  │  - app.min.js + app.min.js.map     │                  │
│  │  - DevTools shows original code ✅   │                  │
│  └──────────────────────────────────────┘                  │
│                                                             │
│  📊 OPTIMIZATION RESULTS:                                  │
│  - Original: 500 KB (ES2020, 100 files, readable)        │
│  - Modern: 80 KB (ES2020, minified, split) - 84% smaller │
│  - Legacy: 100 KB (ES5, polyfills, split) - 80% smaller  │
│  - Initial load: 30 KB main.js - 94% smaller! 🚀         │
└─────────────────────────────────────────────────────────────┘
```

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
import { lazy, Suspense } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

// ✅ Lazy load route components
const Home = lazy(() => import('./pages/Home'));        // home.chunk.js
const Dashboard = lazy(() => import('./pages/Dashboard')); // dashboard.chunk.js
const Profile = lazy(() => import('./pages/Profile'));  // profile.chunk.js

function App() {
  return (
    <BrowserRouter>
      <Suspense fallback={<div>Loading...</div>}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/profile" element={<Profile />} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
}

// 🎯 Kết quả:
// - Initial load: Chỉ load main.js + home.chunk.js
// - User vào /dashboard → Load dashboard.chunk.js on-demand
// - User vào /profile → Load profile.chunk.js on-demand

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

// Build #1 (Version 1.0 - Thứ 2)
// dist/
//   ├── main.js        (100 KB) ← Tên file KHÔNG ĐỔI
//   └── vendor.js      (300 KB) ← Tên file KHÔNG ĐỔI

// index.html
/*
<!DOCTYPE html>
<html>
<head>
  <script src="/main.js"></script>     ← Browser cache file này
  <script src="/vendor.js"></script>   ← Browser cache file này
</head>
</html>
*/

// 🚨 SCENARIO:
// 1. User A visit website → Download main.js, vendor.js
// 2. Browser cache với header: Cache-Control: max-age=31536000 (1 năm)
// 3. Developer deploy version mới (Thứ 3)
//    → main.js code mới (fix bug)
//    → Nhưng TÊN FILE VẪN LÀ main.js ❌

// Build #2 (Version 1.1 - Thứ 3 - FIX BUG)
// dist/
//   ├── main.js        (105 KB) ← Nội dung MỚI, tên file CŨ ❌
//   └── vendor.js      (300 KB) ← Không đổi

// 4. User A quay lại website
//    → Browser dùng main.js từ CACHE (version cũ) ❌
//    → User KHÔNG thấy bug fix! 😱
//    → Phải Ctrl+F5 (hard refresh) để tải file mới

// ❌ VẤN ĐỀ:
// - User thấy version cũ (có bug)
// - Phải hard refresh manually
// - Không kiểm soát được cache

// ===================================================
// ✅ GIẢI PHÁP: CONTENT HASHING
// ===================================================

// Build #1 (Version 1.0 - Thứ 2)
// dist/
//   ├── main.a3f8b2c1.js     (100 KB) ← Hash từ NỘI DUNG
//   └── vendor.9d4e7f1a.js   (300 KB) ← Hash từ NỘI DUNG

// index.html (auto-generated)
/*
<!DOCTYPE html>
<html>
<head>
  <script src="/main.a3f8b2c1.js"></script>     ← Tên file có hash
  <script src="/vendor.9d4e7f1a.js"></script>   ← Tên file có hash
</head>
</html>
*/

// Browser cache:
// - main.a3f8b2c1.js: cached 1 năm ✅
// - vendor.9d4e7f1a.js: cached 1 năm ✅

// Build #2 (Version 1.1 - Thứ 3 - FIX BUG)
// dist/
//   ├── main.f7c5d3a9.js     (105 KB) ← HASH MỚI vì nội dung đổi! ✅
//   └── vendor.9d4e7f1a.js   (300 KB) ← HASH CŨ vì nội dung KHÔNG đổi ✅

// index.html (auto-generated)
/*
<!DOCTYPE html>
<html>
<head>
  <script src="/main.f7c5d3a9.js"></script>     ← Tên file MỚI! ✅
  <script src="/vendor.9d4e7f1a.js"></script>   ← Tên file CŨ (from cache) ✅
</head>
</html>
*/

// User A quay lại website:
// 1. Browser fetch index.html (luôn fresh, không cache)
// 2. Browser thấy main.f7c5d3a9.js (tên MỚI!)
//    → Tải file mới (vì chưa có trong cache) ✅
// 3. Browser thấy vendor.9d4e7f1a.js (tên CŨ)
//    → Dùng từ cache (tiết kiệm 300 KB bandwidth) ✅

// ✅ LỢI ÍCH:
// - User LUÔN thấy version mới (tự động)
// - Không cần hard refresh
// - Cache files không đổi vô thời hạn (vendor.js)
// - Chỉ download files đã thay đổi (main.js)

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
