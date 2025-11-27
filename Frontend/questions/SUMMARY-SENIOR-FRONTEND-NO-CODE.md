# SUMMARY - Senior Frontend Interview Answers (Tiếng Việt) - BẢN KHÔNG CODE

> **Bản tóm tắt chỉ giữ phần giải thích, định nghĩa, bullets, bảng so sánh. Đã loại bỏ toàn bộ code examples.**

---

## 🗂️ Chú thích thuật ngữ (Tiếng Việt)

Đoạn này là 1 bảng thuật ngữ nhanh để tra cứu khi đọc các câu trả lời. Nếu bạn thấy một từ kỹ thuật trong phần Q*, dùng phần này để hiểu ý nghĩa bằng tiếng Việt.

- **Hoisting**: "nâng" khai báo lên đầu phạm vi (scope). `var` được khởi tạo là `undefined`; `let/const` nằm trong TDZ (Temporal Dead Zone) trước khi khởi tạo.
- **TDZ (Temporal Dead Zone)**: vùng từ đầu block đến khi khai báo `let/const` — truy cập trong vùng này gây `ReferenceError`.
- **Closure (bao đóng)**: hàm nhớ được biến từ scope bên ngoài ngay cả khi hàm ngoài đã trả về.
- **Event Loop**: cơ chế xử lý async — Call Stack ⇒ Microtasks (Promise) ⇒ Render ⇒ Macrotasks (setTimeout, I/O).
- **Microtask**: nhiệm vụ ưu tiên cao (Promise.then, queueMicrotask) — chạy hết trước macrotask.
- **Macrotask**: nhiệm vụ ưu tiên thấp (setTimeout, setInterval, I/O) — lấy 1 macrotask mỗi vòng.
- **Call Stack**: ngăn xếp thực thi mã đồng bộ (LIFO).
- **Heap**: vùng nhớ cấp phát cho objects/arrays/functions.
- **GC (Garbage Collector)**: thu gom rác tự động (mark-and-sweep) — thu dọn các object không còn reachable.
- **Prototype / prototype chain**: cơ chế kế thừa trong JS (class chỉ là syntactic sugar).
- **this binding**: cách xác định `this` (new > explicit call/apply/bind > implicit > default).
- **Promise / async-await**: Promise là object đại diện async; `async/await` là cú pháp dễ đọc cho Promise.
- **Shallow vs Deep copy**: sao chép nông chỉ copy top-level; sao chép sâu clone toàn bộ cấu trúc (ví dụ `structuredClone`).
- **Map / Set**: collection hiện đại (Map cho key bất kỳ; Set cho giá trị duy nhất).
- **WeakMap / WeakSet / WeakRef / FinalizationRegistry**: tham chiếu yếu giúp tránh giữ object khỏi GC; không deterministic, không iterable.
- **Reflow / Repaint**: cost làm layout/paint DOM — tránh thao tác DOM lặp nhiều lần.
- **SSR / SSG / ISR (Next.js)**: các chiến lược render phía server hoặc build-time.
- **XSS / CSRF / CORS**: các rủi ro bảo mật frontend; XSS = script injection; CSRF = giả mạo request; CORS = chính sách chia sẻ nguồn.
- **CSP (Content Security Policy)**: header giúp giảm rủi ro XSS.
- **CDN**: mạng phân phối nội dung, giảm latency.
- **Web Worker**: offload công việc nặng khỏi main thread.
- **requestAnimationFrame (rAF)**: dùng cho animation, chạy trước render frame.
- **Memoization / Cache**: lưu kết quả để tránh tính toán lại; cẩn thận memory leaks.
- **Currying / Higher-Order Functions (HOF)**: kỹ thuật hàm cao cấp để compose và tái sử dụng logic.
- **IIFE**: hàm tự gọi để tạo scope riêng, thường dùng cho module pattern trước ES modules.
- **StructuredClone**: native deep clone hiện đại (hỗ trợ Date, RegExp...), tránh dùng JSON hack nếu cần giữ kiểu phức tạp.

---

## Q01: JavaScript Fundamentals Overview - Tổng Quan Nền Tảng

### 🎯 Câu Trả Lời Ngắn Gọn (3-5 phút):

JavaScript là ngôn ngữ lập trình đơn luồng, bất đồng bộ, chạy trên V8 engine với Event Loop để xử lý I/O không chặn.

### 🔑 5 Trụ Cột Nền Tảng:

**1. Kiểu Dữ Liệu & Bộ Nhớ**:
- 7 kiểu nguyên thủy (number, string, boolean, null, undefined, symbol, bigint) + Object
- Primitive = stack (theo giá trị)
- Reference = heap (theo tham chiếu)
- GC tự động dọn bộ nhớ (Mark-and-Sweep algorithm)

**2. Execution Context & Scope**:
- Call Stack thực thi code đồng bộ (LIFO)
- Scope chain: Global → Function → Block scope
- Hoisting: `var` khởi tạo undefined, `let/const` trong TDZ
- Closure = hàm + môi trường từ vựng xung quanh

**3. Bất Đồng Bộ (Event Loop)**:
- **Microtask Queue** (ưu tiên cao): Promise.then, queueMicrotask
- **Macrotask Queue** (ưu tiên thấp): setTimeout, setInterval
- Event Loop: Call Stack → Microtasks → UI Render → 1 Macrotask
- Async patterns: Callbacks → Promises → Async/Await

**4. OOP & Prototypes**:
- Prototype chain: mỗi object có `__proto__` trỏ đến prototype
- Class = syntactic sugar cho prototype-based inheritance
- `this` binding: new → explicit (call/apply/bind) → implicit → default

**5. Modern JavaScript (ES6+)**:
- `let/const` block scope thay `var`
- Arrow functions = lexical `this`
- Destructuring, spread/rest operators
- Modules (import/export), classes
- Promise, async/await cho async code

### ⚠️ Lỗi Thường Gặp:
- Mutate objects/arrays trực tiếp → dùng spread hoặc immutable methods
- Quên `return` trong arrow function
- `==` vs `===`: luôn dùng `===` (strict equality)
- Closure memory leaks: event listeners không cleanup
- `this` mất context khi pass method: dùng arrow function hoặc bind

### 💡 Kiến Thức Senior:
- **Performance**: Tránh blocking main thread, dùng Web Workers cho heavy computation
- **Memory**: WeakMap/WeakSet cho weak references tránh leaks
- **Security**: XSS prevention (sanitize inputs), CSP headers
- **Tooling**: TypeScript cho type safety, ESLint cho code quality
- **Patterns**: Module pattern, Observer, Factory, Singleton

---

## Q02: Data Types & Memory Management - Tổng Hợp Toàn Diện


**"JavaScript có 8 kiểu dữ liệu: 7 nguyên thủy (không thay đổi được) + 1 phức tạp (object - thay đổi được).**

**📦 Nguyên Thủy vs Tham Chiếu:**
- **Nguyên thủy** (number, string, boolean, undefined, null, symbol, bigint):
  - Lưu theo GIÁ TRỊ trong stack.
  - Không thay đổi được → gán lại tạo giá trị mới.
  - Copy theo giá trị → các bản sao độc lập.
- **Tham chiếu** (object, array, function):
  - Lưu theo THAM CHIẾU trong heap.
  - Thay đổi được → sửa trực tiếp.
  - Copy theo tham chiếu → trỏ đến cùng object.

**🔑 Khái Niệm Cốt Lõi:**
1. **== vs ===**:
   - `==`: So sánh lỏng → chuyển đổi kiểu tự động (vd: `"5" == 5` → true).
   - `===`: So sánh nghiêm ngặt → không chuyển kiểu (vd: `"5" === 5` → false).
   - Thực hành tốt: Luôn dùng `===` trừ khi kiểm tra null/undefined.

2. **null vs undefined**:
   - `undefined`: Biến chưa được assign value (default).
   - `null`: Intentionally empty value (developer set).
   - `typeof null` → "object" (JavaScript bug legacy).

3. **Shallow Copy vs Deep Copy**:
   - **Shallow**: Copy top-level properties only → nested objects vẫn reference.
     ```js
     const shallow = { ...obj }; // Spread
     const shallow2 = Object.assign({}, obj);
     ```
   - **Deep**: Copy recursively tất cả levels → independent clone.
     ```js
     const deep = structuredClone(obj); // Native (modern)
     const deep2 = JSON.parse(JSON.stringify(obj)); // Hack (lose functions, dates)
     ```

4. **Type Checking**:
   - `typeof`: Check primitive types (`typeof "hello"` → "string").
   - `instanceof`: Check object types (`[] instanceof Array` → true).
   - `Array.isArray()`: Check arrays specifically.
   - `Object.prototype.toString.call()`: Most accurate (e.g., `[object Date]`).

**♻️ Memory Management & GC:**
- **Stack**: Primitive values, function calls (LIFO, fast, limited size).
- **Heap**: Objects, arrays (larger, slower, managed by GC).
- **Garbage Collection**: Mark-and-sweep algorithm → auto free unreachable objects.
- **Memory Leaks**:
  - Global variables không cleanup.
  - Event listeners không remove.
  - Closures giữ reference đến large objects.
  - Detached DOM nodes.

**⚠️ Common Pitfalls:**
- **Mutating objects**: `arr.push()` modify original → dùng immutable methods (`[...arr, item]`).
- **Reference comparison**: `{} === {}` → false (khác reference). Dùng deep equality libraries (lodash.isEqual).
- **Type coercion bugs**: `"5" + 3` → "53" (string concat), `"5" - 3` → 2 (number subtract).
- **Falsy values**: `0`, `""`, `null`, `undefined`, `false`, `NaN` → tất cả falsy nhưng khác nhau!

**💡 Senior Insights:**
- **Immutability**: Prefer immutable operations (spread, map, filter) → easier debugging, avoid side effects.
- **WeakMap/WeakSet**: Hold weak references → auto GC khi keys không còn reference → prevent memory leaks.
- **structuredClone()**: Modern deep clone (support Dates, RegExp, Typed Arrays), but lose functions/symbols.
- **Performance**: Primitive faster than objects (stack vs heap). Dùng primitives when possible.
- **TypeScript**: Eliminate runtime type errors → catch type mistakes at compile time.

---

> **Tổng hợp**: Primitive vs Reference, Falsy/Truthy, == vs ===, null vs undefined, Immutable vs Mutable, Deep/Shallow Copy, Type Checking, Memory Management & GC

---

## Q03: ES5 vs ES6+ Features - So Sánh Chi Tiết & Cách Hoạt Động

### 🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):

ES6+ (2015+) mang lại JavaScript hiện đại với classes, modules, arrow functions, async/await.

### 📊 ES5 vs ES6+ (Key Differences):

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

### 🔥 ES6+ Must-Know Features:
1. **let/const**: Block scope → avoid hoisting issues, `const` prevent reassignment.
2. **Arrow Functions**: Lexical `this`, concise syntax, no `arguments` object.
3. **Destructuring**: Extract values easily.
4. **Spread/Rest**: `...` operator → copy arrays/objects, function params.
5. **Template Literals**: Multi-line strings, interpolation.
6. **Classes**: OOP syntax (syntactic sugar cho prototypes).
7. **Modules**: `import { fn } from './module'` → static imports, tree-shaking.
8. **Promises & Async/Await**: Better async handling than callbacks.
9. **Default Parameters**: Không cần `a = a || 1`.
10. **Optional Chaining**: `user?.address?.city` → safe navigation (ES2020).
11. **Nullish Coalescing**: `value ?? 'default'` → khác với `||` (chỉ check null/undefined).

### ⚡ ES2016-ES2023 Highlights:
- **ES2016**: `**` (exponentiation), `Array.includes()`.
- **ES2017**: `async/await`, `Object.values/entries()`, string padding.
- **ES2018**: Rest/spread for objects, async iteration.
- **ES2019**: `Array.flat/flatMap()`, `Object.fromEntries()`.
- **ES2020**: Optional chaining `?.`, nullish coalescing `??`, `BigInt`, dynamic import.
- **ES2021**: `String.replaceAll()`, numeric separators `1_000_000`.
- **ES2022**: Top-level await, private fields `#private`, `Array.at()`.
- **ES2023**: `Array.findLast()`, `toSorted()`, `toReversed()` (immutable array methods).

### ⚠️ Browser Compatibility:
- **ES5**: Universal support (IE9+, all browsers).
- **ES6+**: Modern browsers (Chrome 51+, Firefox 54+, Safari 10+).
- **Solution**: Babel transpile ES6+ → ES5 cho legacy browsers.
- **Trend**: Evergreen browsers auto-update → ES6+ safe cho 95%+ users.

### 💡 Senior Insights:
- **Transpilation**: Babel transform ES6+ → ES5 at build time → support old browsers.
- **Polyfills**: Add missing features at runtime.
- **Bundle Size**: ES6+ code nhỏ hơn sau minify.
- **Performance**: Modern engines optimize ES6+ better.
- **Best Practice**: Write ES6+, transpile for production, use feature detection.

---

## Q04: Hoisting & Temporal Dead Zone

### 🎯 Câu Trả Lời Ngắn Gọn (1-2 phút):

Hoisting = khai báo được đưa lên đầu scope. TDZ = vùng không thể truy cập let/const trước khi khai báo.

### 🔑 Hoisting Behaviors:

| Type | Hoisted? | Initialized? | Access Before Declaration |
|------|----------|--------------|---------------------------|
| **`var`** | ✅ Yes | ✅ Yes (`undefined`) | ✅ OK (undefined) |
| **`let`** | ✅ Yes | ❌ No (TDZ) | ❌ ReferenceError |
| **`const`** | ✅ Yes | ❌ No (TDZ) | ❌ ReferenceError |
| **`function` declaration** | ✅ Yes | ✅ Yes (entire function) | ✅ OK (callable) |
| **`function` expression** | ✅ Yes (variable only) | ❌ No | ❌ ReferenceError/undefined |
| **`class`** | ✅ Yes | ❌ No (TDZ) | ❌ ReferenceError |

### 📊 Detailed Explanation:

**1. `var` Hoisting**:
- Hoisted + initialized với `undefined`.
- Access trước khai báo → `undefined` (không error).

**2. `let/const` Hoisting + TDZ**:
- Hoisted nhưng NOT initialized → Temporal Dead Zone.
- Access trong TDZ → `ReferenceError`.
- TDZ = từ đầu block scope đến dòng khai báo.

**3. Function Declaration Hoisting**:
- Entire function hoisted → gọi trước khai báo OK.

**4. Function Expression**:
- Variable hoisted nhưng function không.

### ⚠️ Common Pitfalls:
- **`typeof` trong TDZ**: `typeof x` với `let x` → ReferenceError (không safe như `var`).
- **Loop variables**: `var` trong loop → function scope, `let` → block scope per iteration.

### 💡 Senior Insights:
- **Why TDZ exists**: Force developers khai báo trước khi dùng → catch bugs sớm.
- **Hoisting mechanism**: JavaScript engine scans code 2 passes:
  1. **Creation phase**: Allocate memory cho declarations.
  2. **Execution phase**: Execute code line-by-line.
- **Best Practice**:
  - Dùng `const` by default, `let` nếu cần reassign, avoid `var`.
  - Khai báo biến ở top của scope → explicit, tránh confusion.
  - Dùng ESLint rule `no-use-before-define`.

---

## Q05: Set/Map, WeakSet/WeakMap, WeakRef & FinalizationRegistry - Collections & Weak References

### 🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):

Set/Map là collections nâng cao của JavaScript, còn WeakSet/WeakMap/WeakRef là phiên bản weak reference không ngăn garbage collection.

### 🔑 4 Điểm Chính:

**1. Set vs Array:**
- Set lưu **unique values**, tự động loại duplicate
- Performance O(1) cho `.has()`, `.add()`, `.delete()` (Array là O(n))
- Use case: deduplicate array, check membership nhanh

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

### ⚠️ Lỗi Thường Gặp:
- Dùng Object khi cần Map → không maintain order, keys bị convert sang string
- Dùng WeakMap với primitive keys → Error (phải dùng objects)
- Expect WeakRef.deref() luôn return object → có thể return `undefined` nếu đã GC

### 💡 Kiến Thức Senior:
- WeakMap dùng cho **private properties pattern** trước khi có `#privateField`
- Set/Map internally dùng **SameValueZero algorithm** (như `===` nhưng `NaN === NaN`)
- WeakMap **không có memory leak** khi attach metadata vào DOM nodes (auto cleanup khi node removed)
- FinalizationRegistry chỉ dùng cho **cleanup non-JS resources** (file handles, WASM memory), không dùng cho app logic

---

## Q06: Event Loop - Cơ Chế Hoạt Động JavaScript (Technical Deep Dive)

### 🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):

JavaScript chạy đơn luồng với Event Loop để xử lý các thao tác bất đồng bộ.

### 🏗️ Kiến Trúc (5 Thành Phần):
1. **Call Stack (Ngăn xếp gọi - LIFO)**: Nơi thực thi code đồng bộ. Đơn luồng → chỉ 1 hàm chạy tại 1 thời điểm.
2. **Heap (Vùng nhớ)**: Cấp phát bộ nhớ cho objects, arrays, functions.
3. **Web APIs (Trình duyệt) / C++ APIs (Node.js)**: Xử lý thao tác bất đồng bộ (setTimeout, fetch, fs.readFile) → chạy trên luồng riêng.
4. **Microtask Queue (Hàng đợi ưu tiên cao)**: Promise callbacks, queueMicrotask, MutationObserver.
5. **Macrotask Queue (Hàng đợi ưu tiên thấp)**: setTimeout, setInterval, I/O, UI rendering.

### ♻️ Luồng Hoạt Động Event Loop (Chi Tiết):

**Thuật toán Event Loop:**
1. Chạy hết Call Stack (đồng bộ).
2. Chạy TẤT CẢ Microtasks.
3. UI Render (nếu cần).
4. Lấy 1 Macrotask.
5. Lặp lại từ bước 1.

### 🔑 Điểm Khác Biệt Quan Trọng:
- **Microtask vs Macrotask**:
  - Microtask chạy TẤT CẢ trước khi Event Loop tiếp tục.
  - Macrotask chỉ chạy 1 task mỗi vòng lặp.
  - Ưu tiên: Microtask > UI Render > Macrotask.
- **Trình duyệt vs Node.js**:
  - Trình duyệt: Có giai đoạn render UI.
  - Node.js: Có `process.nextTick()` (ưu tiên cao hơn Microtask) + 6 giai đoạn (timers, I/O, idle, poll, check, close).

### ⚠️ Lỗi Thường Gặp:
- **Làm đói UI**: Microtasks vô hạn chặn rendering → UI đóng băng.
- **setTimeout(fn, 0) ≠ Tức thì**: Vẫn phải chờ Call Stack trống + Microtasks hoàn thành.
- **Race Conditions**: Callbacks bất đồng bộ có thể thực thi không theo thứ tự mong đợi.

### 💡 Kiến Thức Senior:
- **Hiệu năng**: Tránh chặn Call Stack với tính toán nặng → dùng Web Workers hoặc chia thành chunks với `setTimeout`.
- **Debugging**: Hiểu Event Loop → debug lỗi bất đồng bộ (race conditions, callback hell).
- **React**: `setState` batching dùng Microtask → nhiều lời gọi setState gộp thành 1 lần render lại.
- **Node.js**: `setImmediate()` vs `setTimeout(fn, 0)` → `setImmediate` chạy trong giai đoạn check, nhanh hơn trong I/O callbacks.
- **requestAnimationFrame**: Chạy TRƯỚC render (Chỉ trình duyệt) → animation mượt hơn setTimeout.

### 🔧 Kỹ Thuật Tối Ưu:
- **Chunking (Chia nhỏ)**: Chia tasks dài thành chunks nhỏ với `setTimeout` → không chặn UI.
- **queueMicrotask()**: Nhanh hơn `Promise.resolve().then()` → ít chi phí hơn.
- **Web Workers**: Offload tính toán nặng → luồng riêng (song song thật sự).

---

## Q07: Event Loop - Giải Thích Theo Cách Nói Chuyện Đời Thường

### 🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):

Event Loop là cơ chế JavaScript xử lý async code trong môi trường single-threaded bằng cách liên tục kiểm tra Call Stack và Task Queues.

### 🔑 Ẩn Dụ Quán Cà Phê (dễ nhớ cho phỏng vấn):

Như 1 người phục vụ (JS Engine single-thread) làm việc tại quầy (Call Stack). Khi có việc lâu (async), giao cho máy tự động (Web APIs) rồi ghi tên vào sổ chờ. Liên tục check: ① Quầy trống chưa? ② Có khách VIP chưa? (Microtasks) → Phục vụ hết VIP trước. ③ Có khách thường chưa? (Macrotasks) → Phục vụ 1 người. ④ Lặp lại.

### 🔑 3 Thành Phần Chính:

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

### ⚠️ Lỗi Thường Gặp:
- Nghĩ `setTimeout(fn, 0)` chạy ngay → Sai! Vẫn phải chờ Call Stack empty + Microtasks xong
- Không hiểu Microtask **chạy hết tất cả** → Promise chains dài có thể block UI
- Dùng `setInterval` mà không clear → Memory leak + tasks chồng chéo

### 💡 Kiến Thức Senior:
- **Starvation**: Microtask queue dài vô hạn (recursive Promise) → Macrotasks không bao giờ chạy → UI freeze
- **Rendering timing**: Browser render giữa macrotasks (60fps = ~16ms/task), nếu task > 16ms → jank
- `requestAnimationFrame` chạy **trước render**, `setTimeout` chạy sau → dùng rAF cho animation mượt
- Node.js có **6 phases** trong Event Loop (timers, I/O, poll, check, close) khác Browser (chỉ có Micro + Macro)

---

## Q08: Closure & Data Privacy

### 🎯 Câu Trả Lời Ngắn Gọn (1-2 phút):

Closure = hàm + môi trường từ vựng (các biến xung quanh nó). Hàm bên trong giữ tham chiếu đến biến scope bên ngoài.

### 📦 Core Concepts:
- **Definition**: Function nhớ được và access được biến từ outer scope, ngay cả khi outer function đã return.
- **Mechanism**: Inner function giữ reference đến [[Scope]] (lexical environment) của outer function.
- **Data Privacy**: Dùng closure để tạo private variables/methods (encapsulation).

### 🎯 Use Cases:
1. **Private Variables**: Factory functions trả về object với methods access private state.
2. **Module Pattern**: IIFE + closure → private state + public API.
3. **Event Handlers**: Callback giữ reference đến outer variables.
4. **Partial Application**: Currying, function factories.
5. **Memoization**: Cache results của expensive functions.

### ⚠️ Common Pitfalls:
- **Memory Leaks**: Closure giữ reference → biến không bị GC → memory leak nếu không cleanup.
- **Loop + Closures**: `var` trong loop → mọi closure chia sẻ cùng biến.

### 💡 Senior Insights:
- **Performance**: Closures có overhead nhỏ (memory + lookup time), nhưng negligible trong hầu hết cases.
- **DevTools**: Chrome DevTools → Memory Profiler → check closure retaining objects.
- **ES6 Modules**: Replace IIFE module pattern → native private scope.
- **WeakMap**: Alternative cho private data không dùng closure → auto GC khi object không còn reference.

---

## Q09: Arrow vs Regular Functions & this Binding (call, apply, bind)

### 🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):

Arrow function khác regular function ở cách gắn `this`: từ vựng (scope bên ngoài) vs động (ngữ cảnh runtime).

### 📊 Arrow vs Regular Functions (Key Differences):
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

### 🔧 `this` Binding Methods (call, apply, bind):
- **`call(thisArg, arg1, arg2)`**: Invoke ngay với arguments riêng lẻ.
- **`apply(thisArg, [args])`**: Invoke ngay với arguments array.
- **`bind(thisArg)`**: Return function mới với `this` cố định (không invoke).

### 🎯 `this` Binding Rules (4 Rules - Priority Order):
1. **`new` Binding**: `new Fn()` → `this` = new object.
2. **Explicit Binding**: `call/apply/bind` → `this` = thisArg.
3. **Implicit Binding**: `obj.method()` → `this` = obj.
4. **Default Binding**: Standalone function → `this` = global object (window/global) hoặc undefined (strict mode).

### ⚠️ Common Mistakes:
- **Arrow trong object methods**: `this` không point to object!
- **Event handlers**: Regular function → `this` = event target. Arrow → `this` = outer scope.
- **Class methods as callbacks**: Mất context → dùng arrow hoặc bind.

### 💡 Senior Insights:
- **React Class Components**: Arrow class fields = auto-bind `this` (babel transform).
- **Performance**: Arrow functions trong render → tạo new reference mỗi lần → child re-render. Dùng `useCallback`.
- **call vs apply**: `apply` hữu ích khi arguments đã là array.

---

## Q10: IIFE (Immediately Invoked Function Expression) & Functional Programming

### 🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):

IIFE là function execute ngay sau khi define để tạo private scope, còn Functional Programming bao gồm pure functions, immutability, currying và higher-order functions.

### 🔑 4 Khái Niệm Chính:

**1. IIFE (Immediately Invoked Function Expression):**
- Syntax: `(function(){ ... })()` hoặc `(() => { ... })()`
- **Tạo scope riêng** → tránh pollute global namespace
- Use case: Module pattern (trước ES6 modules), private variables, avoid variable hoisting conflicts

**2. Pure Functions:**
- **Same input → same output**, không có side effects (không modify external state)
- **Predictable**, dễ test, dễ debug
- Ví dụ: `add(a,b) => a+b` (pure) vs `arr.push(x)` (impure - mutate arr)

**3. Currying:**
- Transform `f(a,b,c)` thành `f(a)(b)(c)` - **partial application**
- **Reusable functions** với preset arguments
- Use case: event handlers, middleware, configuration functions

**4. Higher-Order Functions:**
- Functions nhận/return functions: `.map()`, `.filter()`, `.reduce()`
- **Composition**: kết hợp nhiều functions
- Use case: middleware stack, decorators, memoization

### ⚠️ Lỗi Thường Gặp:
- Quên `()` trong IIFE → không execute
- Mutate data trong pure function → side effects, khó debug
- Over-curry functions → code khó đọc

### 💡 Kiến Thức Senior:
- IIFE giờ **ít dùng** vì ES6 modules (`import/export`) và block scope (`let/const`)
- Pure functions quan trọng cho **memoization** (cache kết quả) và **parallelization**
- Currying vs Partial Application: Curry **luôn return unary** (1 param), Partial có thể nhiều params
- Functional Programming giúp **avoid shared mutable state** → tránh race conditions trong async code

---

## Q11: DOM Events - Event Flow, Delegation & Event Properties (Bubbling, Capturing, target vs currentTarget)

### 🎯 Câu Trả Lời Ngắn Gọn (2 phút):

Sự kiện DOM có 3 giai đoạn: Capturing (từ trên xuống) → Target → Bubbling (từ dưới lên).

### ♻️ Luồng Sự Kiện (3 Giai Đoạn):
1. **Capturing Phase (Giai đoạn bắt)**: Sự kiện từ `window` → `document` → `html` → ... → phần tử target (từ trên xuống).
2. **Target Phase (Giai đoạn target)**: Sự kiện chạm phần tử target (phần tử được click).
3. **Bubbling Phase (Giai đoạn nổi)**: Sự kiện từ phần tử target → ... → `html` → `document` → `window` (từ dưới lên).

### 🔑 Khái Niệm Cốt Lõi:
- **Mặc định**: Event listeners chạy trong **Bubbling phase** (useCapture = false).
- **Capturing**: Đặt `useCapture: true` → listener chạy trong Capturing phase.
- **Dừng Lan Truyền**: `event.stopPropagation()` → ngừng bubbling/capturing.
- **Ngăn Hành Vi Mặc Định**: `event.preventDefault()` → ngăn hành vi mặc định (vd: form submit, chuyển link).

### 🎯 Mẫu Event Delegation:
- **Khái niệm**: Gắn listener ở phần tử cha, không phải từng con → tận dụng bubbling.
- **Lợi ích**:
  - Hiệu năng: 1 listener thay vì 100 listeners cho 100 items.
  - Nội dung động: Không cần gắn lại listeners khi thêm/xóa con.

### 🔍 `target` vs `currentTarget`:
- **`event.target`**: Phần tử thực sự được click (phần tử gốc kích hoạt sự kiện).
- **`event.currentTarget`**: Phần tử có listener gắn vào (đang xử lý sự kiện).
- **Trường hợp**: Delegation → `currentTarget` = cha, `target` = con được click.

### ⚠️ Common Pitfalls:
- **stopPropagation() overuse**: Ngăn cả analytics tracking, global handlers → dùng thận trọng.
- **preventDefault() vs stopPropagation()**: Khác nhau! preventDefault ngăn default action, stopPropagation ngăn propagation.
- **Event delegation với dynamic content**: Phải check `e.target.matches()` đúng selector.

### 💡 Senior Insights:
- **Performance**: Event delegation giảm memory usage (1 listener vs 1000) và faster DOM manipulation.
- **Passive listeners**: `{ passive: true }` → improve scroll performance (không block scroll while waiting for preventDefault).
- **once option**: `{ once: true }` → auto remove listener sau 1 lần fire.
- **Capture for debugging**: Dùng capturing phase để intercept events trước khi children handle.

---

## Q12: DOM API & Query Methods

### 🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):

DOM API cung cấp methods để query và manipulate DOM. Query methods có performance và behaviors khác nhau - cần hiểu live vs static collections.

### 🔑 4 Query Methods Chính:

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

### ⚠️ Lỗi Thường Gặp:
- Lặp qua `querySelectorAll` mà nghĩ nó là array → phải convert `[...nodeList]` hoặc `Array.from()`
- Iterate HTMLCollection **trong vòng lặp modify DOM** → collection tự update → infinite loop
- Query toàn document khi chỉ cần query trong container → chậm, dùng `container.querySelector()`

### 💡 Kiến Thức Senior:
- **Live vs Static**: HTMLCollection (live) vs NodeList (có thể live hoặc static tùy method)
  - `getElementsBy*` → live HTMLCollection
  - `querySelectorAll` → static NodeList
  - `childNodes` → live NodeList
- **Reflow/Repaint**: Mỗi DOM manipulation có thể trigger layout recalculation
  - Batch updates: dùng DocumentFragment hoặc `.innerHTML` thay vì nhiều `.appendChild()`
  - Read trước, write sau để tránh **layout thrashing**
- **MutationObserver** hiệu quả hơn polling DOM changes
- Modern frameworks (React, Vue) dùng Virtual DOM để minimize direct DOM manipulation

---

## Q13: Async/Await vs Promises vs Callbacks & Promise.all/any/race

### 🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):

JavaScript async tiến hóa: Callbacks → Promises → Async/Await. Mỗi mẫu giải quyết code bất đồng bộ với đánh đổi khác nhau.

### 📊 Tiến Hóa Mẫu Async:
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

### 🔧 Promise Combinators (4 Phương Thức):
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

### ⚠️ Common Mistakes:
- **Forgot `await`**: Promise không execute → return Promise object, không phải value.
- **Sequential khi có thể parallel**: `await` trong loop → chậm. Dùng `Promise.all()`.
- **Unhandled rejections**: Missing `.catch()` hoặc `try/catch` → silent failures.
- **Promise.all fail-fast**: 1 promise fail → tất cả fail. Dùng `allSettled` nếu cần.

### 💡 Senior Insights:
- **Error handling**: `try/catch` trong async function catch bất kỳ `await` throw.
- **Top-level await**: ES2022 → `await` ngoài async function trong modules.
- **Microtask queue**: Promises execute trong microtask queue → priority hơn setTimeout.
- **Cancellation**: Native promises không support cancel → dùng AbortController (fetch) hoặc libraries (Bluebird).

---

## Q14: Axios Interceptors - Phân Tích Chi Tiết & Tối Ưu Hóa

### 🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):

Interceptors là middleware functions chạy trước/sau mỗi request/response, giúp centralize authentication, error handling, logging, và data transformation.

### 🔑 4 Use Cases Chính:

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

### ⚠️ Lỗi Thường Gặp:
- Không cleanup interceptor khi component unmount → **memory leak**
- Modify request config trực tiếp mà không clone → side effects
- Infinite loop khi retry logic không có **max attempts**
- Token refresh race condition (multiple 401s cùng lúc) → queue requests

### 💡 Kiến Thức Senior:
- **Execution order**: Request interceptors = **LIFO** (last added runs first), Response = **FIFO**
- Interceptor return Promise → có thể **async/await** bên trong
- Eject interceptor: `const id = axios.interceptors.request.use(...); axios.interceptors.request.eject(id)`
- Best practice: Tạo **separate axios instances** cho từng service (auth API, data API) với different interceptors

---

## Q15: Advanced Deferring Execution Techniques - Kỹ Thuật Trì Hoãn Thực Thi Nâng Cao

(Nội dung câu Q15 không được cung cấp đầy đủ trong đoạn mã ban đầu.)

---

## Q16: Compare Data Types - Objects, Strings, Big Numbers & Decimals

### 🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):

So sánh data types phức tạp cần hiểu: Objects so sánh reference vs value, Strings xử lý Unicode/locale, Big Numbers/Decimals dùng libraries vì floating point precision issues.

### 🔑 4 Khái Niệm Chính:

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

### ⚠️ Lỗi Thường Gặp:
- Deep compare objects trong render → re-render loop (dùng `useMemo`)
- So sánh strings không normalize Unicode → "café" ≠ "café"
- Tính toán tiền bằng floats → rounding errors
- Stringify objects để compare → không handle functions, Date, circular refs

### 💡 Kiến Thức Senior:
- **Structural sharing** (Immer, Redux): shallow copy chỉ modified branches → fast comparison
- **Object.is()** vs `===`: `Object.is(NaN, NaN) = true`, `Object.is(+0, -0) = false`
- JSON.stringify **không stable** (key order) → dùng `fast-json-stable-stringify`
- Banking systems: **double-entry bookkeeping**, store as integers, round at display layer only

---

## Q17: React Query (TanStack Query) - Data Fetching, Caching & State Management

### 🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):

React Query là thư viện quản lý DỮ LIỆU TỪ SERVER, khác với state nội bộ ứng dụng (Redux/Zustand).

### 📦 Khái Niệm Cốt Lõi:
- **Dữ liệu Server vs State Client**: Dữ liệu server = bất đồng bộ, chia sẻ, có thể cũ (thông tin user, bài viết). State client = đồng bộ, cục bộ (trạng thái UI, dữ liệu form).
- **Query (Truy vấn)**: Lấy và lưu cache dữ liệu bằng `useQuery({ queryKey, queryFn })`. QueryKey = định danh cache + mảng phụ thuộc.
- **Mutation (Thay đổi)**: Chỉnh sửa dữ liệu server bằng `useMutation()`, tự động làm mới các query liên quan.
- **Chiến lược Cache**: `staleTime` (dữ liệu tươi bao lâu) vs `gcTime` (thời gian giữ cache sau khi component unmount).

### 🔑 Refetch vs Invalidate:
- **`refetch()`**: Buộc lấy lại dữ liệu ngay lập tức (kích hoạt thủ công).
- **`invalidateQueries()`**: Đánh dấu dữ liệu cũ → tự động lấy lại ở background nếu component đang hiển thị.
- **Thực hành tốt**: Dùng `invalidateQueries` sau khi thay đổi dữ liệu để tự động đồng bộ giao diện.

### ♻️ Vòng Đời Query (7 giai đoạn):
1. **Fresh (Tươi)**: Dữ liệu mới lấy, còn trong `staleTime` → không lấy lại.
2. **Stale (Cũ)**: Hết `staleTime` → sẵn sàng lấy lại khi có kích hoạt.
3. **Fetching (Đang lấy)**: Đang gọi API (background hoặc lần đầu).
4. **Inactive (Không hoạt động)**: Component unmount → query không active.
5. **Garbage Collection (Thu hồi)**: Sau `gcTime` (mặc định 5 phút) → xóa cache.
6. **Error (Lỗi)**: Lấy dữ liệu thất bại → tự động thử lại với thời gian chờ tăng dần.
7. **Paused (Tạm dừng)**: Chế độ offline → tạm dừng lấy dữ liệu, tiếp tục khi online.

### 🎯 Các Trường Hợp Sử Dụng:
- **Tự động lấy lại**: Focus cửa sổ, kết nối lại mạng, polling theo khoảng thời gian.
- **Cập nhật lạc quan**: Cập nhật giao diện trước, rollback nếu API thất bại.
- **Cuộn vô hạn**: `useInfiniteQuery()` với `getNextPageParam`.
- **Prefetching**: `queryClient.prefetchQuery()` trước khi chuyển trang.

### ⚠️ Lỗi Thường Gặp:
- Nhầm lẫn `staleTime` với `gcTime`.
- Quên dependencies trong `queryKey` → không lấy lại khi params thay đổi.
- Lạm dụng trạng thái loading → dùng `isLoading` vs `isPending` đúng ngữ cảnh.
- Không xử lý trạng thái lỗi → thiếu error boundaries.

### 💡 Kiến Thức Senior:
- **Hiệu năng**: React Query gộp requests → nhiều components cùng query chỉ gọi API 1 lần.
- **DevTools**: Dùng React Query DevTools để debug trạng thái cache, thời gian stale, trạng thái query.
- **SSR**: Kết hợp với `HydrationBoundary` + `prefetchQuery` trên server.
- **Chuyển đổi**: Thay thế Redux/SWR dần dần → migrate từng tính năng, không làm cùng lúc.

---

## Q18: Browser Rendering (Paint, Repaint, Reflow)

### 🎯 Câu Trả Lời Ngắn Gọn (1-2 phút):

Reflow (tính toán lại bố cục) tốn kém hơn Repaint (vẽ lại). Tối ưu bằng cách gộp thay đổi DOM, dùng transform/opacity.

### 🎨 Quy Trình Render (Đường Ống Render Quan Trọng):
1. **Xây Dựng DOM**: Phân tích HTML → cây DOM.
2. **Xây Dựng CSSOM**: Phân tích CSS → cây CSSOM.
3. **Cây Render**: Kết hợp DOM + CSSOM → chỉ các phần tử hiển thị.
4. **Layout (Reflow)**: Tính toán kích thước/vị trí của mỗi phần tử.
5. **Paint (Vẽ)**: Vẽ pixels (màu sắc, hình ảnh, viền, bóng).
6. **Composite (Tổng hợp)**: Kết hợp các lớp → màn hình cuối cùng.

### 🔑 Paint vs Repaint vs Reflow:

| Thao Tác | Kích Hoạt | Chi Phí | Ví Dụ |
|----------|-----------|---------|-------|
| **Paint** | Render lần đầu | Trung bình | Tải trang lần đầu |
| **Repaint** | Thay đổi hình ảnh (không layout) | Thấp | `color`, `background`, `visibility` |
| **Reflow** | Thay đổi bố cục | **Cao** | `width`, `height`, `margin`, `padding`, `display` |

### ⚡ Kích Hoạt Reflow (Tốn Kém!):
- Thao tác DOM: Thêm/xóa phần tử, thay đổi nội dung.
- Thay đổi CSS: `width`, `height`, `margin`, `padding`, `border`, `display`, `position`.
- Đọc thuộc tính layout: `offsetWidth`, `offsetHeight`, `clientWidth`, `scrollTop` → buộc reflow đồng bộ!
- Thay đổi kích thước cửa sổ, thay đổi font, thay đổi class.

### ♻️ Kích Hoạt Repaint (Rẻ Hơn):
- Thuộc tính hình ảnh: `color`, `background-color`, `visibility`, `outline`, `box-shadow`.
- Không thay đổi layout → chỉ vẽ lại pixels.

### 🚀 Kỹ Thuật Tối Ưu:
1. **Gộp Thay Đổi DOM**: Batch DOM changes với DocumentFragment hoặc clone node.
2. **Dùng transform/opacity (Chỉ Composite)**: Chạy trên GPU, không trigger reflow/repaint.
3. **Tránh Đọc Thuộc Tính Layout Trong Vòng Lặp**: Batch reads/writes để avoid layout thrashing.
4. **requestAnimationFrame Cho Animation**: Sync với browser repaint cycle.
5. **Virtualize Long Lists**: Chỉ render visible items (react-window, react-virtualized).

### ⚠️ Common Mistakes:
- Changing styles trong loop → multiple reflows.
- Reading layout properties (offsetWidth) sau write → force synchronous reflow.
- Animating `width/height/top/left` thay vì `transform`.

### 💡 Senior Insights:
- **Composite Layers**: `transform`, `opacity` run on compositor thread (GPU) → không block main thread.
- **will-change**: `will-change: transform` hint browser tạo separate layer → optimize animations.
- **Layout Thrashing**: Read → Write → Read → Write pattern → force multiple reflows. Dùng FastDOM library.
- **DevTools**: Chrome DevTools → Performance tab → see reflow/repaint events.
- **CSS Containment**: `contain: layout` isolate element → reflow không spread to parent.

---

## Q19: Loop Performance & Async Loops

### 🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):

Loop performance: `for` nhanh nhất, `for...of` readable, `forEach/map` functional. Async loops: `Promise.all()` parallel, `for await...of` sequential.

### 🔑 Performance Ranking:

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

### 🔑 Async Loops - 3 Patterns:

**1. Sequential (chờ từng cái):**
- Use case: API rate limiting, dependencies giữa iterations
- Method: `for...of` + `await`, `Array.reduce()`

**2. Parallel (chạy tất cả cùng lúc):**
- Use case: Independent tasks, no rate limit
- Method: `Promise.all()`, `Promise.allSettled()`

**3. Batched (chia nhỏ):**
- Use case: Rate limiting, server overload prevention
- Method: Process chunks in parallel, wait between batches

### ⚠️ Common Mistakes:
- `forEach` với async/await → không chờ, chạy parallel (dùng `for...of`)
- `map()` với async → return array of Promises (phải `Promise.all()`)
- Parallel requests → overwhelm server (dùng batching)
- Sequential khi có thể parallel → slow performance

### 💡 Senior Insights:
- **Benchmark**: Chrome DevTools Performance tab, `console.time()`
- **Memory**: `forEach/map` tạo function context mỗi iteration → GC pressure
- **JIT optimization**: Modern engines optimize `for` loops tốt hơn
- **Async control flow**: Libraries như `p-limit`, `async.js` cho advanced patterns

---

## Q42: Client-Side Rendering (CSR) vs Server-Side Rendering (SSR) - Phân Biệt & Cách Hoạt Động Chi Tiết

### 🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):

CSR = browser render (SPA), SSR = server render HTML. CSR tốt cho interactive apps, SSR tốt cho SEO/performance. Modern: Hybrid (SSR first paint + CSR hydration).

### 🔑 So Sánh Chi Tiết:

| **Metric** | **CSR** | **SSR** |
|-----------|---------|--------|
| **Initial Load** | Chậm (download JS → execute) | Nhanh (HTML ready) |
| **SEO** | Kém (crawlers không chờ JS) | Tốt (HTML đầy đủ) |
| **Navigation** | Nhanh (no reload) | Chậm (full page reload) |
| **Server Load** | Thấp (static CDN) | Cao (render mỗi request) |
| **Complexity** | Đơn giản (frontend only) | Phức tạp (isomorphic code) |

### 🔑 CSR (Client-Side Rendering):

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

### 🔑 SSR (Server-Side Rendering):

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

### ⚠️ Lỗi Thường Gặp:
- SSR dùng browser APIs (`window`, `localStorage`) → crash server
- Hydration mismatch (server HTML ≠ client HTML) → re-render flicker
- CSR không loading state → blank screen 3-5s
- SSR không cache → overload server

### 💡 Kiến Thức Senior:
- **Hybrid rendering**: Next.js SSG (static) + ISR (revalidate) + SSR (dynamic)
- **Streaming SSR**: Send HTML chunks progressively (React 18 Suspense)
- **Partial Hydration**: Chỉ hydrate interactive components (Islands Architecture - Astro)
- **Edge SSR**: Render on CDN edge (Vercel Edge, Cloudflare Workers) - faster TTFB

### 🎯 Khi Nào Dùng Gì?

**Dùng CSR khi:**
- Internal tools, admin dashboards
- SPAs với heavy interactions
- Không quan tâm SEO (behind auth)
- Team nhỏ, budget thấp

**Dùng SSR khi:**
- Public pages, SEO critical
- E-commerce, marketing sites
- Slow devices, emerging markets
- News, blogs, content-heavy sites

**Dùng SSG (Hybrid) khi:**
- Content không thay đổi thường xuyên
- Blogs, docs, landing pages
- Best performance + SEO
- Use with ISR (Incremental Static Regeneration)

---

## Q43: Authentication Flow An Toàn Cho Hệ Thống Ngân Hàng/Chứng Khoán - Access Token, Refresh Token, Cookie Security

### 🎯 Câu Trả Lời Ngắn Gọn (4-5 phút):

Secure auth flow: Access Token (short-lived, 15min, memory) + Refresh Token (long-lived, 7-30 days, httpOnly cookie). Implement token rotation, XSS/CSRF protection, MFA cho high-security systems.

### 🔑 Architecture - Dual Token Pattern:

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

### 🔑 Authentication Flow:

**A. Login Flow (Đăng Nhập):**
1. User gửi credentials (username/password)
2. Server validate → generate Access Token (15min) + Refresh Token (30 days)
3. Access Token → return JSON body
4. Refresh Token → set httpOnly cookie
5. Client lưu Access Token trong memory (React state/Zustand)

**B. API Call Flow:**
1. Client gửi request với `Authorization: Bearer <access-token>`
2. Server validate Access Token
3. If valid → return data
4. If expired (401) → trigger refresh flow

**C. Refresh Token Flow:**
1. Client detect 401 (Access Token expired)
2. Auto call `/refresh-token` API với httpOnly cookie
3. Server validate Refresh Token:
   - Valid → generate new Access Token + new Refresh Token (rotation)
   - Invalid → logout, redirect login
4. Client lưu Access Token mới, retry failed request

**D. Logout Flow:**
1. Client call `/logout` API
2. Server revoke Refresh Token (blacklist)
3. Client clear Access Token từ memory
4. Server delete httpOnly cookie

### 🛡️ Security Best Practices:

**A. Cookie Security:**
- `httpOnly`: JS không đọc được → chống XSS
- `Secure`: Chỉ gửi qua HTTPS
- `SameSite=Strict`: Chống CSRF attacks
- `Max-Age`: Set expiration time

**B. Token Storage:**
- ✅ Access Token: Memory (state, Zustand, Redux)
- ✅ Refresh Token: httpOnly cookie
- ❌ NEVER localStorage (XSS steal tokens)
- ❌ NEVER sessionStorage (XSS vulnerable)

**C. Token Rotation (Xoay Vòng Token):**
- Mỗi lần dùng Refresh Token → generate token mới
- Old token bị revoke (blacklist)
- Detect stolen token: 2 requests cùng lúc → logout tất cả

### ⚠️ Common Security Mistakes:
- Lưu tokens trong localStorage → XSS steal tokens
- Không rotate refresh tokens → stolen token dùng mãi
- CORS misconfiguration → expose tokens cross-origin
- Không implement CSRF tokens → cross-site request attacks
- Access Token quá dài (>1h) → high risk khi stolen
- Không implement rate limiting → brute force attacks

### 💡 Kiến Thức Senior:
- **JWT structure**: Header.Payload.Signature (Base64URL encoded)
- **Signature algorithms**: HS256 (symmetric, shared secret) vs **RS256** (asymmetric, safer - banking)
- **Silent refresh**: Background refresh trước khi expired (smooth UX)
- **Token introspection**: Server-side validation cho high-security (không tin client JWT)
- **OAuth 2.0 + PKCE**: Authorization Code Flow với Proof Key (mobile apps)

---

## Q44: Microfrontend & Monorepo - Module Federation, Multi-Framework, Communication Patterns

### 🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):

Microfrontend = chia app lớn thành nhiều apps nhỏ độc lập. Module Federation = runtime integration (share code, no rebuild).

### 🏗️ Microfrontend Architecture:
- **Concept**: Mỗi team sở hữu 1 microfrontend (MFE) → deploy độc lập → tech stack riêng.
- **Runtime Integration**: MFEs load at runtime (không phải build time) → independent releases.
- **Shell App (Host)**: Container app load remote MFEs.

### 🔧 Module Federation (Webpack 5 / Vite):

**Expose**: MFE expose components/modules.
- Config: `exposes: { './Button': './src/components/Button' }`

**Consume**: Host import remote modules.
- Config: `remotes: { mfe1: 'mfe1@http://localhost:3001/remoteEntry.js' }`

**Shared Dependencies**: Share React, libraries → load once (not duplicate).
- Config: `shared: { react: { singleton: true } }`

### ♻️ Communication Patterns:
1. **Props/Callbacks**: Parent pass props to child MFE → simple, tightly coupled.
2. **Custom Events**: `window.dispatchEvent()` → loose coupling.
3. **State Management**: Shared Zustand/Redux store → sync state across MFEs.
4. **PubSub**: Event bus (RxJS) → publish/subscribe pattern.

### 🎯 Multi-Framework Support:
- **React + Vue + Angular**: Mỗi MFE dùng framework khác nhau.
- **Web Components**: Wrap MFEs trong custom elements → framework-agnostic.

### 🔑 Monorepo (Nx / Turborepo):
- **Concept**: 1 repo chứa multiple projects → shared tooling, dependencies.
- **Benefits**:
  - Atomic commits across projects.
  - Shared libraries, utilities.
  - Consistent tooling (ESLint, Prettier, TypeScript configs).
  - Dependency graph → build chỉ affected projects.
- **Tools**: Nx (Angular ecosystem), Turborepo (Vercel), Lerna (legacy).

### ⚠️ Trade-offs:

| Aspect | Monolith | Microfrontend |
|--------|----------|---------------|
| **Complexity** | Low | High (orchestration, communication) |
| **Build Time** | Slow (1 large app) | Fast (parallel builds) |
| **Deploy** | All-or-nothing | Independent per MFE |
| **Team Autonomy** | Low (shared codebase) | High (own tech stack) |
| **Bundle Size** | Optimized | Risk of duplication |
| **Developer Experience** | Simple | Complex (tooling, debugging) |

### 💡 Senior Insights:
- **When to use MFE**: Large teams (10+ devs), independent releases critical, different domains (e-commerce: catalog, checkout, profile).
- **When NOT to use**: Small teams, simple apps, tight coupling between features.
- **Module Federation vs Iframe**: MF = shared dependencies, better performance. Iframe = total isolation but clunky UX.
- **Styling Isolation**: CSS Modules, Shadow DOM, CSS-in-JS (styled-components) → prevent style conflicts.
- **Routing**: Each MFE handle own routes + Shell sync URL state.

---

**🎯 Kết Luận Tổng Thể:**

Bản tóm tắt này đã loại bỏ toàn bộ code examples, chỉ giữ lại phần giải thích, định nghĩa, bảng so sánh, bullets points và insights. Format đẹp, dễ scan, tập trung vào khái niệm và best practices ở level Senior.

