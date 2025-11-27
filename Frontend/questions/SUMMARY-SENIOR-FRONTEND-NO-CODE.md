zz# SUMMARY - Senior Frontend Interview Answers (Tiếng Việt)

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

## Q01: JavaScript Fundamentals Overview - Tổng Quan Nền Tảng JavaScript

### 🎯 Trả Lời Ngắn Gọn (Cho Interviewer):

**"JavaScript là ngôn ngữ lập trình đơn luồng (single-threaded), chạy bất đồng bộ (asynchronous) nhờ Event Loop, được thực thi trên V8 engine (Chrome) hoặc SpiderMonkey (Firefox), cho phép xử lý I/O không chặn (non-blocking I/O)."**

### 📖 Giải Thích Chi Tiết (Deep Dive):

JavaScript được thiết kế để chạy trên trình duyệt (browser) nhưng giờ cũng chạy trên server (Node.js). Dù là đơn luồng (chỉ có 1 Call Stack), JavaScript vẫn xử lý được nhiều tác vụ cùng lúc nhờ **Event Loop** phối hợp với **Web APIs** (setTimeout, fetch, DOM events).

**Tại sao single-threaded nhưng vẫn async?**

- **Main Thread**: Chỉ có 1 thread chạy JavaScript code.
- **Web APIs**: Browser cung cấp APIs chạy trên threads riêng (C++ threads).
- **Event Loop**: Điều phối giữa Call Stack và Task Queues.

### 🔑 5 Trụ Cột Nền Tảng:

#### **1. Kiểu Dữ Liệu & Quản Lý Bộ Nhớ (Data Types & Memory Management)**

**Chú thích tiếng Việt:**

- **7 kiểu nguyên thủy (Primitives)**:
  - `number` (số: 42, 3.14, NaN, Infinity)
  - `string` (chuỗi ký tự: "hello", 'world')
  - `boolean` (đúng/sai: true, false)
  - `null` (rỗng có chủ đích - developer set)
  - `undefined` (chưa gán giá trị - default)
  - `symbol` (định danh duy nhất - ES6)
  - `bigint` (số nguyên cực lớn - ES2020)
- **1 kiểu phức tạp**: `object` (đối tượng: objects, arrays, functions, dates, RegExp...)

**Cách hoạt động bộ nhớ:**

- **Stack (Ngăn xếp)**:

  - Lưu: Primitives và references (tham chiếu) đến objects.
  - Đặc điểm: Nhanh, kích thước cố định, LIFO (Last In First Out - vào sau ra trước).
  - Tự động quản lý (auto cleanup khi function return).

- **Heap (Đống)**:
  - Lưu: Objects thực tế (data structure phức tạp).
  - Đặc điểm: Chậm hơn, kích thước động (dynamic), quản lý bởi Garbage Collector.
  - Không tự động cleanup → cần GC.

**Garbage Collection (Thu gom rác - Dọn dẹp bộ nhớ tự động):**

- **Mark-and-Sweep Algorithm** (Thuật toán đánh dấu và quét):
  1. **Mark phase (Giai đoạn đánh dấu)**: Đánh dấu tất cả objects còn "reachable" (có thể truy cập từ root - global scope, call stack).
  2. **Sweep phase (Giai đoạn quét)**: Quét và giải phóng (free) các objects không được đánh dấu.
- Tự động chạy khi heap gần đầy.
- Không thể điều khiển trực tiếp (không có API để trigger GC).

#### **2. Execution Context & Scope (Ngữ cảnh thực thi & Phạm vi)**

**Call Stack (Ngăn xếp gọi):**

- Cấu trúc dữ liệu LIFO theo dõi vị trí thực thi code.
- Mỗi lần gọi function → push execution context lên stack.
- Function return → pop context ra khỏi stack.
- **Stack Overflow**: Xảy ra khi recursion không có điểm dừng (infinite recursion).

**Scope Chain (Chuỗi phạm vi - Nơi tìm biến):**

- **Global Scope** (Phạm vi toàn cục): Biến khai báo ngoài tất cả functions.
  - Browser: `window` object.
  - Node.js: `global` object.
- **Function Scope** (Phạm vi hàm): Biến trong function, chỉ truy cập được trong function đó (`var`).
- **Block Scope** (Phạm vi khối): Biến trong `{}` (if, for, while...), chỉ truy cập trong block (`let`, `const`).

**Hoisting (Nâng khai báo):**

- JavaScript "nâng" (hoist) khai báo lên đầu scope trước khi execute.
- **`var`**: Hoisted + initialized = `undefined` → có thể access trước khai báo (nhưng = undefined).
- **`let/const`**: Hoisted nhưng KHÔNG initialized → **TDZ (Temporal Dead Zone)** → ReferenceError.
- **`function declaration`**: Hoisted cả khai báo lẫn giá trị → có thể gọi trước khi khai báo.

**Closure (Bao đóng - Hàm nhớ scope bên ngoài):**

- Function "nhớ" và truy cập được biến từ outer scope ngay cả khi outer function đã return.
- **Cơ chế**: Inner function giữ reference đến `[[Scope]]` (lexical environment) của outer function.
- **Use case**: Private variables, factory functions, callbacks.

#### **3. Bất Đồng Bộ (Asynchronous) - Event Loop**

**Luồng xử lý: Call Stack → Web APIs → Task Queues → Event Loop**

**Microtask Queue (Hàng đợi vi nhiệm vụ - ưu tiên cao):**

- Các loại: `Promise.then()`, `Promise.catch()`, `Promise.finally()`, `queueMicrotask()`, `MutationObserver`.
- Đặc điểm: Chạy **TẤT CẢ** microtasks trước khi chuyển sang macrotask.
- Thứ tự: FIFO (First In First Out - vào trước ra trước).

**Macrotask Queue (Hàng đợi vĩ nhiệm vụ - ưu tiên thấp):**

- Các loại: `setTimeout()`, `setInterval()`, `setImmediate()` (Node.js), I/O operations, UI rendering events.
- Đặc điểm: Chỉ chạy **1** macrotask mỗi vòng lặp Event Loop.
- Thứ tự: FIFO.

**Event Loop Algorithm (Thuật toán vòng lặp sự kiện):**

```
1. Execute all synchronous code in Call Stack (Chạy hết code đồng bộ)
2. Execute ALL microtasks (Chạy HẾT microtasks)
3. Render UI if needed (Browser only - Vẽ lại giao diện nếu cần)
4. Execute ONE macrotask (Chỉ chạy 1 macrotask)
5. Repeat từ bước 1 (Lặp lại mãi mãi)
```

**Async Patterns Evolution (Tiến hóa mẫu bất đồng bộ):**

- **Callbacks** (ES5): Đơn giản nhưng → Callback Hell (kim tự tháp hủy diệt).
- **Promises** (ES6): Chaining với `.then()`, xử lý lỗi tốt với `.catch()`.
- **Async/Await** (ES2017): Syntax sugar của Promises, code đọc như đồng bộ (synchronous-like).

#### **4. OOP & Prototypes (Lập trình hướng đối tượng & Nguyên mẫu)**

**Prototype Chain (Chuỗi nguyên mẫu - Cơ chế kế thừa trong JS):**

- Mỗi object có internal property `[[Prototype]]` (truy cập qua `__proto__` hoặc `Object.getPrototypeOf()`).
- Khi truy cập property không có trong object → tìm trong prototype chain.
- Chuỗi kết thúc tại `Object.prototype` (có `[[Prototype]]: null`).

**Class (ES6) - Syntactic Sugar:**

- `class` chỉ là cú pháp đẹp hơn cho prototype-based inheritance.
- Internally vẫn dùng prototypes.
- Support: `extends` (kế thừa), `super()` (gọi parent constructor), `static` methods, `#private` fields (ES2022).

**`this` Binding (4 quy tắc - theo thứ tự ưu tiên):**

1. **new Binding**: `new Fn()` → `this` = new object được tạo.
2. **Explicit Binding**: `fn.call(obj)`, `fn.apply(obj)`, `fn.bind(obj)` → `this` = obj.
3. **Implicit Binding**: `obj.method()` → `this` = obj.
4. **Default Binding**: Standalone function call → `this` = global object (hoặc undefined trong strict mode).

#### **5. Modern JavaScript (ES6+ Features)**

**Key Features:**

- **`let/const`**: Block scope, TDZ, không hoisting như `var`.
- **Arrow Functions**: Lexical `this` (inherit từ outer scope), không có `arguments`, không dùng làm constructor.
- **Destructuring**: `const {name, age} = user`, `const [a, b] = arr`.
- **Spread/Rest**: `...` operator cho arrays/objects/function params.
- **Template Literals**: `` `Hello ${name}` `` (multi-line, interpolation).
- **Modules**: `import/export`, static analysis, tree-shaking.
- **Classes**: OOP syntax (syntactic sugar).
- **Promises & Async/Await**: Modern async programming.
- **Default Parameters**: `function fn(a = 1, b = 2)`.
- **Optional Chaining** (ES2020): `user?.address?.city` (safe navigation).
- **Nullish Coalescing** (ES2020): `value ?? 'default'` (chỉ check null/undefined, khác `||`).

### ✅ Best Practices (Thực hành tốt nhất):

1. **Luôn dùng `const` by default, chỉ dùng `let` khi cần reassign, tránh `var`**.

   - _Lý do_: `const` ngăn chặn reassignment vô tình, `let` có block scope an toàn hơn `var` (function scope).
   - _Khi nào dùng `let`_: Counters trong loops, biến cần reassign.

2. **Dùng `===` thay vì `==` để so sánh**.

   - _Lý do_: `===` strict equality không chuyển đổi kiểu tự động → tránh bugs.
   - _Exception_: `value == null` để check cả null và undefined cùng lúc.

3. **Cleanup event listeners và timers khi component unmount**.

   - _Lý do_: Tránh memory leaks (rò rỉ bộ nhớ).
   - _Cách làm_: Save reference → remove listener, clear timer.

4. **Dùng immutable methods cho arrays/objects** (spread, map, filter thay vì push, splice).

   - _Lý do_: Dễ debug, tránh side effects, phù hợp với React/Redux.
   - _Pattern_: `[...arr, item]` thay vì `arr.push(item)`.

5. **Dùng arrow functions cho callbacks** để giữ `this` context.

   - _Lý do_: Arrow function không tạo `this` riêng, inherit từ outer scope.
   - _Pattern_: `setTimeout(() => this.method(), 1000)`.

6. **Tránh blocking main thread** - dùng Web Workers cho heavy computation.

   - _Lý do_: Main thread bị block → UI freeze (đóng băng), UX tệ.
   - _Use case_: Image processing, data parsing, complex calculations.

7. **Dùng TypeScript** cho large projects để có type safety.

   - _Lý do_: Catch lỗi lúc compile time, không phải runtime → ít bugs production.
   - _Trade-off_: Learning curve, setup complexity.

8. **Enable strict mode** (`'use strict';`) ở đầu file/function.

   - _Lý do_: Bắt lỗi thường gặp sớm hơn (vd: gán giá trị cho undeclared variable).
   - _Benefit_: Prevent accidental globals, eliminate silent errors.

9. **Prefer declarative over imperative code**.

   - _Declarative_: `arr.map(x => x * 2)` (WHAT you want).
   - _Imperative_: `for` loop với mutations (HOW to do it).
   - _Lý do_: Easier to read, test, maintain.

10. **Use meaningful variable names** (không viết tắt quá mức).
    - ❌ `const d = new Date()`, `const u = getUser()`.
    - ✅ `const currentDate = new Date()`, `const currentUser = getUser()`.

### ❌ Common Mistakes (Lỗi thường gặp - Chi tiết):

1. **Mutate objects/arrays trực tiếp trong React state**.

   - ❌ **Sai**: `state.arr.push(item); setState(state);`
   - ✅ **Đúng**: `setState({arr: [...state.arr, item]});`
   - _Vì sao sai_: React compare reference, cùng reference → không re-render.

2. **Quên `return` trong arrow function khi dùng block `{}`**.

   - ❌ **Sai**: `const fn = () => { value }` (không return gì, return undefined).
   - ✅ **Đúng**: `const fn = () => value` hoặc `const fn = () => ({ value })`.
   - _Note_: Dùng `()` để return object literal.

3. **Closure memory leaks - không cleanup event listeners**.

   - ❌ **Sai**: `element.addEventListener('click', handler);` mà không remove.
   - ✅ **Đúng**: `element.removeEventListener('click', handler);` khi unmount.
   - _Pattern_: Save handler reference để remove sau.

4. **`this` mất context khi pass method làm callback**.

   - ❌ **Sai**: `setTimeout(obj.method, 1000);` → `this` = undefined/window.
   - ✅ **Đúng**: `setTimeout(() => obj.method(), 1000);` hoặc `obj.method.bind(obj)`.
   - _Lý do_: Method không còn context của object khi pass alone.

5. **Dùng `==` thay vì `===`**.

   - ❌ **Sai**: `"0" == 0` → true (type coercion), `null == undefined` → true.
   - ✅ **Đúng**: `"0" === 0` → false, `null === undefined` → false.
   - _Exception_: `value == null` để check cả null và undefined.

6. **Không hiểu falsy values**.

   - **Falsy**: `0`, `""`, `null`, `undefined`, `false`, `NaN`, `0n` (BigInt zero), `-0`.
   - **Truthy**: Tất cả giá trị khác (kể cả `"0"`, `"false"`, `[]`, `{}`).
   - ❌ **Sai**: `if (value)` → false khi value = 0 (nhưng 0 có thể là valid value).
   - ✅ **Đúng**: `if (value !== null && value !== undefined)` hoặc `if (value != null)`.

7. **Quên async functions luôn return Promise**.

   - ❌ **Sai**: `async function fn() { return 1; }; fn() === 1` → false.
   - ✅ **Đúng**: `async function fn() { return 1; }; await fn() === 1` → true.
   - _Note_: Phải `await` để lấy value, không await → nhận Promise object.

8. **Blocking Event Loop với synchronous heavy operations**.

   - ❌ **Sai**: Long-running loop trong main thread → UI freeze.
   - ✅ **Đúng**: Chia nhỏ task với `setTimeout` hoặc dùng Web Worker.

9. **Không handle Promise rejections**.

   - ❌ **Sai**: `fetch(url).then(...)` không có `.catch()` → unhandled rejection.
   - ✅ **Đúng**: `fetch(url).then(...).catch(err => handleError(err))`.

10. **Global variables pollution**.
    - ❌ **Sai**: Khai báo biến global không cần thiết.
    - ✅ **Đúng**: Wrap trong IIFE, modules, hoặc dùng `const/let` trong scope.

### 🔬 Deep Dive Insights (Kiến thức chuyên sâu):

#### **1. V8 Engine Optimization (Tối ưu hóa của V8):**

- **Hidden Classes (Lớp ẩn)**:

  - V8 tạo hidden class cho objects có cùng "shape" (cùng properties theo thứ tự).
  - Objects cùng hidden class → optimize property access.
  - _Tip_: Khởi tạo object properties theo thứ tự nhất quán để V8 optimize.

- **Inline Caching**:

  - Cache kết quả property lookups.
  - Lần sau access cùng property → dùng cached result (faster).

- **JIT Compilation (Just-In-Time Compilation)**:
  - Compile "hot code" (code chạy nhiều lần) thành machine code.
  - **Ignition** (interpreter) → **TurboFan** (optimizing compiler).
  - _Note_: Code run once → interpreted, code run nhiều → compiled.

#### **2. Memory Leaks Patterns (Mẫu rò rỉ bộ nhớ):**

- **Global variables không cần thiết**: Không bao giờ bị GC.
- **Detached DOM nodes**: DOM nodes removed khỏi document nhưng vẫn có reference trong JS.
- **Timers không clear**: `setInterval` không clear → callback giữ reference đến outer scope mãi.
- **Closures giữ large objects**: Closure reference toàn bộ outer scope (kể cả biến không dùng).
- **Event listeners không remove**: Giữ reference đến DOM nodes và handlers.

**Cách detect memory leaks:**

- Chrome DevTools → Memory tab → Take Heap Snapshot.
- So sánh snapshots trước/sau action → xem objects nào tăng.

#### **3. Performance Tips:**

- **Object property access**: Faster với primitives, slower với nested objects.
- **Array iteration**: `for` loop nhanh nhất, `for...of` readable, `forEach` chậm (function call overhead).
- **String concatenation**: Template literals optimize tốt trong modern browsers, tránh `+` trong loop.
- **Avoid `delete` operator**: Làm object deoptimize trong V8, prefer set `undefined`.

#### **4. Security Considerations (Bảo mật):**

- **XSS (Cross-Site Scripting)**:

  - Sanitize user inputs trước khi render (dùng DOMPurify library).
  - Không bao giờ dùng `innerHTML` với user input.

- **CSP (Content Security Policy)**:

  - HTTP headers hạn chế scripts được phép chạy.
  - Prevent inline scripts, eval(), unsafe sources.

- **eval() is evil**:
  - Không bao giờ dùng `eval()` với user input → code injection risk.
  - Alternatives: `JSON.parse()`, `Function()` constructor (safer).

#### **5. Module System Evolution:**

| System         | Year | Syntax                     | Load   | Browser | Use Case              |
| -------------- | ---- | -------------------------- | ------ | ------- | --------------------- |
| **IIFE**       | ES5  | `(function(){})()`         | Inline | ✅      | Private scope         |
| **CommonJS**   | 2009 | `require()/module.exports` | Sync   | ❌      | Node.js               |
| **AMD**        | 2010 | `define()/require()`       | Async  | ✅      | Browser (RequireJS)   |
| **ES Modules** | ES6  | `import/export`            | Async  | ✅      | Modern (tree-shaking) |

**ES Modules benefits:**

- Static analysis → tree-shaking (remove unused code).
- Native browser support (no bundler needed).
- Better developer experience (named exports, clear dependencies).

---

## Q02: Data Types & Memory Management - Kiểu Dữ Liệu & Quản Lý Bộ Nhớ

### 🎯 Trả Lời Ngắn Gọn:

**"JavaScript có 8 kiểu dữ liệu: 7 nguyên thủy (primitives - immutable/không thay đổi được) + 1 phức tạp (object - mutable/thay đổi được). Primitives lưu trong Stack theo giá trị (by value), Objects lưu trong Heap theo tham chiếu (by reference)."**

### 📖 Giải Thích Chi Tiết (Deep Dive):

JavaScript là **dynamically typed language** (ngôn ngữ kiểu động) - không cần khai báo kiểu, kiểu được xác định lúc runtime. Điều này linh hoạt nhưng dễ gây bugs → nên dùng TypeScript cho large projects.

#### **📦 Primitive vs Reference Types (Nguyên thủy vs Tham chiếu):**

**Primitive Types (7 loại - Immutable/Không thay đổi được):**

1. **`number`** (Số - 64-bit floating point IEEE 754):

   - Bao gồm: integers (42), floats (3.14), `NaN` (Not a Number), `Infinity`, `-Infinity`.
   - **Max safe integer**: `2^53 - 1` (9,007,199,254,740,991).
   - Access qua: `Number.MAX_SAFE_INTEGER`, `Number.MIN_SAFE_INTEGER`.
   - **Floating point precision issue**: `0.1 + 0.2 !== 0.3` (0.30000000000000004).
   - _Lý do_: Binary representation không represent chính xác một số decimals.

2. **`string`** (Chuỗi - immutable sequence of UTF-16 code units):

   - Strings KHÔNG thay đổi được → mọi string method return string mới.
   - _VD_: `str.toUpperCase()` không modify `str`, return string mới.
   - **Template literals** (ES6): `` `Hello ${name}` `` support multi-line và interpolation.

3. **`boolean`** (Đúng/Sai): `true` hoặc `false`.

   - Falsy values (convert to false): `0`, `""`, `null`, `undefined`, `false`, `NaN`, `0n`, `-0`.
   - Truthy values: Tất cả giá trị khác.

4. **`undefined`** (Chưa định nghĩa):

   - Biến đã khai báo nhưng chưa gán giá trị.
   - Default value của function parameters không truyền vào.
   - `void 0` luôn return `undefined` (safe way).

5. **`null`** (Rỗng có chủ đích):

   - Intentional absence of value (developer explicitly set).
   - `typeof null === "object"` là **bug legacy** của JavaScript (không fix được vì break backwards compatibility).

6. **`symbol`** (ES6 - Định danh duy nhất):

   - Mỗi Symbol là unique, không bao giờ trùng (kể cả `Symbol('a') !== Symbol('a')`).
   - **Use cases**:
     - Object property keys để tránh name collisions.
     - Private-like properties.
     - Well-known Symbols: `Symbol.iterator`, `Symbol.toStringTag`.

7. **`bigint`** (ES2020 - Số nguyên cực lớn):
   - Integers lớn hơn `Number.MAX_SAFE_INTEGER`.
   - **Syntax**: `100n`, `BigInt(100)`.
   - **Không thể** mix với Number: `100n + 50` → TypeError.

**Reference Type (1 loại - Mutable/Thay đổi được):**

- **`object`**: Objects, Arrays, Functions, Dates, RegExp, Maps, Sets, WeakMaps, WeakSets...
- Stored in Heap, biến chỉ lưu memory address (pointer/tham chiếu).
- Multiple variables có thể point to same object.

#### **💾 Memory Storage (Cách lưu trữ bộ nhớ):**

| Aspect         | Stack                    | Heap                  |
| -------------- | ------------------------ | --------------------- |
| **Lưu gì**     | Primitives, References   | Objects (actual data) |
| **Cấu trúc**   | LIFO (Last In First Out) | Unstructured          |
| **Tốc độ**     | Nhanh (O(1) access)      | Chậm hơn              |
| **Kích thước** | Cố định, limited (~1MB)  | Động, lớn hơn nhiều   |
| **Quản lý**    | Tự động (auto cleanup)   | Garbage Collector     |
| **Lifetime**   | Function scope           | Until no references   |

**Copy Behavior (Hành vi sao chép):**

- **Primitive**: Copy by value → 2 biến độc lập hoàn toàn.
  - _VD_: `let a = 5; let b = a; b = 10;` → `a` vẫn = 5.
- **Reference**: Copy by reference → 2 biến trỏ đến cùng object.
  - _VD_: `let a = {x:1}; let b = a; b.x = 2;` → `a.x` cũng = 2.

#### **🔑 Core Concepts (Khái niệm cốt lõi):**

**1. `==` vs `===` (So sánh lỏng vs nghiêm ngặt):**

| Operator | Name              | Type Coercion | Example             |
| -------- | ----------------- | ------------- | ------------------- |
| `==`     | Abstract Equality | ✅ Yes        | `"5" == 5` → true   |
| `===`    | Strict Equality   | ❌ No         | `"5" === 5` → false |

**Type coercion rules for `==`:**

- `null == undefined` → true (only these two).
- Number comparison: Convert to numbers → `"5" == 5` → `5 == 5`.
- Boolean comparison: `true` → 1, `false` → 0.
- Object to primitive: Call `valueOf()` or `toString()`.

**Best practice**: Luôn dùng `===` trừ khi check null/undefined: `value == null`.

**2. `null` vs `undefined` (So sánh chi tiết):**

| Aspect              | `undefined`                | `null`           |
| ------------------- | -------------------------- | ---------------- |
| **Ý nghĩa**         | Chưa gán giá trị           | Rỗng có chủ đích |
| **Typeof**          | "undefined"                | "object" (bug)   |
| **Default value**   | ✅ Yes                     | ❌ No            |
| **JSON.stringify**  | Omitted                    | "null"           |
| **Math operations** | NaN                        | 0                |
| **`==` comparison** | `null == undefined` → true | Same             |

**Best practice**:

- Dùng `undefined` cho default/uninitialized values.
- Dùng `null` khi muốn explicitly set "no value".

**3. Shallow Copy vs Deep Copy (Sao chép nông vs sâu):**

**Shallow Copy (Sao chép nông):**

- Copy top-level properties only.
- Nested objects/arrays vẫn shared reference.

**Methods:**

- Spread: `{...obj}`, `[...arr]`.
- `Object.assign({}, obj)`.
- `Array.from(arr)`, `arr.slice()`.

**Deep Copy (Sao chép sâu):**

- Copy recursively tất cả levels.
- Tạo independent clone hoàn toàn.

**Methods:**

- **`structuredClone(obj)`** (ES2022 - RECOMMENDED):

  - ✅ Support: Dates, RegExp, Maps, Sets, Typed Arrays, circular references.
  - ❌ Không support: Functions, Symbols, DOM nodes.

- **`JSON.parse(JSON.stringify(obj))`** (Hack):

  - ✅ Simple, widely supported.
  - ❌ Lose: Functions, Symbols, Dates (become strings), `undefined`, circular references.

- **Lodash `_.cloneDeep(obj)`** (Production-ready):
  - ✅ Handle tất cả edge cases.
  - ❌ Thêm dependency.

**4. Type Checking (Kiểm tra kiểu - Chi tiết):**

| Method                             | Use For    | Example               | Result           |
| ---------------------------------- | ---------- | --------------------- | ---------------- |
| `typeof`                           | Primitives | `typeof 42`           | "number"         |
| `instanceof`                       | Objects    | `[] instanceof Array` | true             |
| `Array.isArray()`                  | Arrays     | `Array.isArray([])`   | true             |
| `Object.prototype.toString.call()` | Everything | `.call([])`           | "[object Array]" |

**`typeof` quirks (Lỗi/Đặc điểm):**

- `typeof null` → "object" (bug).
- `typeof []` → "object" (không phân biệt array).
- `typeof function(){}` → "function" (technically objects nhưng có type riêng).

**Best practice type checking:**

- **Arrays**: `Array.isArray(value)`.
- **Objects**: `typeof value === 'object' && value !== null && !Array.isArray(value)`.
- **null**: `value === null`.
- **undefined**: `value === undefined` hoặc `typeof value === 'undefined'`.
- **Function**: `typeof value === 'function'`.

#### **♻️ Garbage Collection (Thu gom rác - Chi tiết):**

**Mark-and-Sweep Algorithm (Thuật toán đánh dấu và quét):**

**Phase 1 - Mark (Đánh dấu):**

1. Bắt đầu từ **roots** (global variables, call stack, active closures).
2. Traverse graph of references (theo tất cả references).
3. Mark tất cả reachable objects là "alive" (còn sống/đang dùng).

**Phase 2 - Sweep (Quét):**

1. Scan toàn bộ heap.
2. Free (giải phóng) memory của objects không được mark.
3. Compact memory (optional - giảm fragmentation).

**GC Generations (Thế hệ GC):**

- **Young Generation**: Objects mới tạo, GC thường xuyên (minor GC).
- **Old Generation**: Objects sống lâu, GC ít hơn (major GC).
- _Lý do_: Hầu hết objects die young → optimize cho case này.

**Memory Leak Patterns (Mẫu rò rỉ bộ nhớ - Chi tiết):**

1. **Accidental Global Variables**:

   - ❌ `function() { leakedVar = 'oops'; }` (không dùng `var/let/const`).
   - ✅ Enable strict mode: `'use strict';`.

2. **Forgotten Timers**:

   - ❌ `setInterval(callback, 1000);` không clear.
   - ✅ `const id = setInterval(...); clearInterval(id);`.

3. **Event Listeners không remove**:

   - ❌ `element.addEventListener('click', handler);` → keep reference forever.
   - ✅ `element.removeEventListener('click', handler);` when done.

4. **Closures giữ large objects**:

   - ❌ Closure reference toàn bộ outer scope (kể cả biến không dùng).
   - ✅ Limit closure scope, set unused vars = null.

5. **Detached DOM nodes**:

   - ❌ `const div = document.getElementById('x'); div.remove();` nhưng vẫn có reference trong JS.
   - ✅ Set `div = null` sau khi remove.

6. **Circular References** (ít gặp với modern GC):
   - Old IE issue: `objA.ref = objB; objB.ref = objA;`.
   - Modern GC handle được circular refs.

**How to detect memory leaks:**

1. Chrome DevTools → Memory tab.
2. Take Heap Snapshot trước action.
3. Perform action (vd: open/close modal 10 times).
4. Take Heap Snapshot sau.
5. Compare snapshots → xem objects nào tăng không giảm.

### ✅ Best Practices (Thực hành tốt nhất - Chi tiết):

1. **Prefer immutable operations** (spread, map, filter) thay vì mutate.

   - _Lý do_: Easier debugging, no side effects, Redux/React friendly, predictable.
   - _Pattern_: `const newArr = [...arr, item]` thay vì `arr.push(item)`.

2. **Dùng `===` mặc định, chỉ dùng `==` khi check null/undefined**.

   - _Pattern_: `if (value == null)` check cả null và undefined.
   - _Avoid_: `value == 0`, `value == false` (confusing).

3. **Always cleanup resources** (listeners, timers, subscriptions).

   - _Pattern_:
     ```
     useEffect(() => {
       const id = setInterval(...);
       return () => clearInterval(id); // Cleanup
     }, []);
     ```

4. **Dùng `structuredClone()` cho deep copy** (modern browsers).

   - _Fallback_: Lodash `_.cloneDeep()` cho production.
   - _Avoid_: `JSON.parse(JSON.stringify())` vì lose functions/dates/symbols.

5. **Check type carefully với proper methods**:

   - Arrays: `Array.isArray(value)`.
   - null: `value === null`.
   - undefined: `value === undefined`.
   - Objects: `typeof value === 'object' && value !== null && !Array.isArray(value)`.

6. **Dùng WeakMap/WeakSet** để store metadata cho objects.

   - _Use case_: Private data, caching, DOM node metadata.
   - _Benefit_: Auto GC khi keys không còn reference.

7. **Monitor memory usage** trong DevTools thường xuyên.

   - _Khi nào_: Sau implement features lớn, trước release.
   - _Tool_: Chrome DevTools → Memory → Heap Snapshot.

8. **Prefer primitives over objects** khi có thể.

   - _Lý do_: Primitives faster (stack vs heap), less memory.
   - _VD_: Dùng enum numbers thay vì objects cho state.

9. **Set large objects = null** khi done để hint GC.

   - _Pattern_: `let largeData = fetchData(); processData(largeData); largeData = null;`.

10. **Avoid creating many small objects trong hot paths**.
    - _Problem_: GC pressure (many allocations).
    - _Solution_: Object pooling, reuse objects.

### ❌ Common Mistakes (Lỗi thường gặp - Với ví dụ):

1. **Mutating objects/arrays thay vì tạo mới**.

   - ❌ **Sai**: `arr.push(item); setState(arr);` → React không re-render.
   - ✅ **Đúng**: `setState([...arr, item]);` → new reference.
   - _Vì sao sai_: React/Redux compare by reference, cùng reference = không có change.

2. **So sánh objects bằng `===`**.

   - ❌ **Sai**: `{a:1} === {a:1}` → false (khác reference).
   - ✅ **Đúng**: Dùng deep equality `_.isEqual(obj1, obj2)` hoặc `JSON.stringify()` (hack).
   - _Note_: `JSON.stringify()` không reliable (thứ tự keys, lose functions).

3. **Type coercion bugs**.

   - ❌ **Sai**: `"5" + 3` → "53" (string concat), `"5" - 3` → 2 (number subtract).
   - ✅ **Đúng**: Explicit convert `Number("5") + 3` → 8.
   - _Pattern_: Luôn convert explicit thay vì rely on coercion.

4. **Không hiểu falsy values**.

   - Falsy: `0`, `""`, `null`, `undefined`, `false`, `NaN`, `0n`, `-0`.
   - ❌ **Sai**: `if (count)` → false khi count = 0 (nhưng 0 là valid).
   - ✅ **Đúng**: `if (count !== null && count !== undefined)` hoặc `if (count != null)`.

5. **Floating point comparison trực tiếp**.

   - ❌ **Sai**: `0.1 + 0.2 === 0.3` → false (0.30000000000000004).
   - ✅ **Đúng**: `Math.abs((0.1 + 0.2) - 0.3) < Number.EPSILON` → true.
   - _Solution_: Dùng integers (cents) cho money, hoặc Decimal.js library.

6. **`typeof null === "object"` bug**.

   - ❌ **Sai**: `if (typeof value === "object")` → true cho cả null.
   - ✅ **Đúng**: `if (typeof value === "object" && value !== null)`.

7. **Shallow copy khi cần deep copy**.

   - ❌ **Sai**: `const copy = {...obj};` với nested objects → vẫn shared reference.
   - ✅ **Đúng**: `const copy = structuredClone(obj);`.

8. **Memory leaks với closures**.

   - ❌ **Sai**: Closure giữ reference đến large object không cần.
   - ✅ **Đúng**: Limit scope, set `largeObj = null` trong closure nếu không dùng nữa.

9. **Không cleanup event listeners**.

   - ❌ **Sai**: `element.addEventListener('click', handler);` → leak khi element removed.
   - ✅ **Đúng**: `element.removeEventListener('click', handler);` trong cleanup.

10. **Dùng `delete` operator trên objects**.
    - ❌ **Sai**: `delete obj.prop;` → deoptimize object trong V8.
    - ✅ **Đúng**: `obj.prop = undefined;` → giữ object shape.

### 🔬 Deep Dive Insights (Kiến thức chuyên sâu):

#### **1. IEEE 754 Floating Point Precision:**

- JavaScript numbers là **64-bit floats** (double precision).
- Structure: 1 bit sign + 11 bits exponent + 52 bits mantissa.
- Một số decimals không represent chính xác trong binary: `0.1`, `0.2`, `0.3`.
- **Solution**:
  - Store as integers (cents cho money): `$1.99` → `199` cents.
  - Libraries: `decimal.js`, `big.js`, `bignumber.js`.

#### **2. String Immutability Performance:**

- String concat trong loop (`str += char`) tạo nhiều temporary strings → slow O(n²).
- **Better**: Array join `arr.push(char); arr.join('')` → O(n).
- Modern engines optimize string concat (rope data structure) nhưng vẫn nên avoid trong hot loops.

#### **3. Object Property Deletion:**

- `delete obj.prop` làm object change "shape" → V8 deoptimize → slow.
- **Impact**: Property access chuyển từ optimized (inline cache) → dictionary mode.
- **Better**: Set `obj.prop = undefined` (giữ shape) hoặc dùng Map (optimized cho frequent add/delete).

#### **4. WeakMap/WeakSet Use Cases:**

**WeakMap:**

- **Private data**: Store private props mà không dùng closure/Symbol.
- **DOM metadata**: `weakMap.set(domNode, metadata)` → auto cleanup khi node removed.
- **Caching**: Cache computed values, auto cleanup khi keys GC'ed.

**WeakSet:**

- **Mark objects**: Track objects đã processed mà không prevent GC.
- **Private flags**: Check if object has been "tagged" without modifying it.

**Limitations:**

- Keys phải là objects (không được primitives).
- Không iterable (cannot loop over entries).
- Không có `.size` property (không đếm được entries).

#### **5. Memory Profiling Deep Dive:**

**Chrome DevTools Memory Tab:**

1. **Heap Snapshot**:

   - Capture state tại 1 thời điểm.
   - See: All objects, sizes, references.
   - **Use**: Find retained objects, compare snapshots.

2. **Allocation Timeline**:

   - Record allocations theo thời gian.
   - See: When objects allocated.
   - **Use**: Identify allocation spikes.

3. **Allocation Sampling**:
   - Lightweight profiling (low overhead).
   - See: Stack traces of allocations.
   - **Use**: Production profiling.

**Key Metrics:**

- **Shallow Size**: Memory của object itself.
- **Retained Size**: Memory sẽ được free nếu object bị GC (bao gồm references).
- **Distance**: Số bước từ root đến object (càng xa càng có thể leak).

---

> **💡 Tổng hợp**: Primitive (Stack, by value) vs Reference (Heap, by reference) | Falsy/Truthy values | `==` (coercion) vs `===` (strict) | `null` (intentional) vs `undefined` (default) | Immutable vs Mutable | Shallow (top-level) vs Deep Copy (recursive) | Type Checking methods | Mark-and-Sweep GC | Memory Leak patterns | WeakMap/WeakSet for auto cleanup

---

## Q03: ES5 vs ES6+ Features - Lịch Sử & Tiến Hóa JavaScript

### 🎯 Trả Lời Ngắn Gọn:

**"ES6 (ECMAScript 2015) là bản cập nhật lớn nhất của JavaScript, mang lại classes, modules, arrow functions, promises, và async/await. ES5 (2009) thiếu nhiều features hiện đại này, chỉ có `var`, function declarations, và callbacks."**

### 📖 Lịch Sử JavaScript (Để Hiểu Tại Sao ES6 Quan Trọng):

- **1995**: JavaScript được tạo bởi Brendan Eich trong 10 ngày (!).
- **1999**: ES3 - first stable version.
- **2009**: **ES5** - thêm strict mode, JSON support, array methods (map, filter, reduce).
- **2015**: **ES6 (ES2015)** - bản cập nhật KHỔNG LỒ (classes, modules, arrows, promises).
- **2016+**: **Yearly releases** - ES2016, ES2017... (small incremental updates).

### 📊 So Sánh ES5 vs ES6+ (Chi Tiết):

| Feature        | ES5 (2009)                 | ES6+ (2015+)                     | Why It Matters                           |
| -------------- | -------------------------- | -------------------------------- | ---------------------------------------- |
| **Variables**  | `var` (function scope)     | `let/const` (block scope)        | TDZ ngăn bugs, `const` immutable binding |
| **Functions**  | `function() {}`            | Arrow `() => {}`                 | Lexical `this`, concise                  |
| **Classes**    | Prototype + constructor    | `class` syntax                   | OOP readable, extends/super              |
| **Modules**    | IIFE/CommonJS/AMD          | `import/export`                  | Static analysis, tree-shaking            |
| **Strings**    | Concatenation `+`          | Template literals `` `${x}` ``   | Multi-line, interpolation                |
| **Objects**    | Manual copy, `for...in`    | Spread `{...obj}`, destructuring | Immutable patterns, clean                |
| **Async**      | Callbacks (hell)           | Promises → async/await           | Readable, error handling                 |
| **Loops**      | `for`, `while`, `for...in` | `for...of`, `.map()/.filter()`   | Iterate iterables, functional            |
| **Parameters** | `a = a \|\| default`       | Default params `fn(a=1)`         | Cleaner, handle falsy values             |
| **Scope**      | Function, Global           | + Block scope (`let/const`)      | Avoid hoisting bugs                      |

### 🔥 ES6+ Must-Know Features (Giải Thích Chi Tiết):

#### **1. `let/const` - Block Scope Variables:**

**Chú thích tiếng Việt:**

- **`let`**: Biến có thể reassign (gán lại), block scope, TDZ.
- **`const`**: Biến KHÔNG thể reassign, block scope, TDZ (nhưng object properties vẫn mutable).

**Khác `var`:**

- `var`: Function scope, hoisted + initialized = `undefined`, no TDZ.
- `let/const`: Block scope (`{}`), hoisted nhưng NOT initialized → TDZ.

**Best Practice:**

- Default dùng `const` → immutable bindings.
- Chỉ dùng `let` khi cần reassign (counters, accumulators).
- KHÔNG BAO GIỜ dùng `var` (except legacy code maintenance).

#### **2. Arrow Functions `() => {}` - Lexical `this`:**

**Khác Function Declarations:**

- **Lexical `this`**: Không có `this` riêng, inherit từ outer scope.
- **No `arguments`**: Dùng rest params `(...args)`.
- **Không dùng làm constructor**: `new arrow()` → TypeError.
- **Concise syntax**: `x => x * 2` (implicit return).

**Use Cases:**

- Callbacks: `arr.map(x => x * 2)`.
- Event handlers cần access outer `this`: `setTimeout(() => this.method(), 100)`.
- Functional programming: Clean, concise.

**Avoid:**

- Object methods: `{ method: () => {} }` → `this` không point to object.
- Prototypes: `Class.prototype.method = () => {}` → `this` sai.

#### **3. Destructuring - Extract Values:**

**Array Destructuring:**

- `const [a, b, ...rest] = [1, 2, 3, 4];` → `a=1, b=2, rest=[3,4]`.
- Swap: `[a, b] = [b, a]`.

**Object Destructuring:**

- `const {name, age} = user;` → extract properties.
- Rename: `const {name: userName} = user;`.
- Default values: `const {name = 'Anonymous'} = user;`.
- Nested: `const {address: {city}} = user;`.

#### **4. Spread/Rest `...` - Multi-Purpose Operator:**

**Spread (Mở rộng):**

- Arrays: `[...arr1, ...arr2]` (concat), `[...arr]` (shallow copy).
- Objects: `{...obj1, ...obj2}` (merge), `{...obj}` (shallow copy).
- Function args: `Math.max(...numbers)`.

**Rest (Thu gom):**

- Function params: `function fn(...args) {}` (all args thành array).
- Destructuring: `const [first, ...rest] = arr;`.

#### **5. Template Literals `` `${}` `` - String Interpolation:**

**Features:**

- **Interpolation**: `` `Hello ${name}` `` → embed expressions.
- **Multi-line**: Giữ nguyên line breaks, không cần `\n`.
- **Tagged templates**: `` styled`color: ${color}` `` (advanced - CSS-in-JS).

#### **6. Classes - OOP Syntax Sugar:**

**Syntax:**

- Constructor: `constructor(props) {}`.
- Methods: `method() {}` (prototype methods).
- Static: `static method() {}` (class methods).
- Inheritance: `extends`, `super()`.
- Private fields (ES2022): `#privateField`.

**Internally:**

- Classes vẫn dùng prototypes.
- `class` chỉ là cleaner syntax cho constructor functions.

#### **7. Modules `import/export` - Static Imports:**

**Benefits:**

- **Static analysis**: Bundlers (Webpack, Rollup) biết dependencies lúc build time.
- **Tree-shaking**: Remove unused code → smaller bundles.
- **Explicit dependencies**: Clear imports/exports.

**Types:**

- **Named exports**: `export const fn = () => {};`, `import {fn} from './module';`.
- **Default export**: `export default fn;`, `import fn from './module';`.
- **Namespace import**: `import * as utils from './utils';`.

#### **8. Promises & Async/Await - Modern Async:**

**Promises (ES6):**

- States: Pending → Fulfilled (resolved) / Rejected.
- Chaining: `.then(onSuccess, onError)` hoặc `.catch(onError)`.
- Combinators: `Promise.all()`, `Promise.race()`, `Promise.allSettled()`, `Promise.any()`.

**Async/Await (ES2017):**

- Syntax sugar cho Promises.
- `async function` luôn return Promise.
- `await` chỉ dùng trong `async function`.
- Error handling: `try/catch` blocks.

#### **9. Optional Chaining `?.` (ES2020) - Safe Navigation:**

**Use Cases:**

- `user?.address?.city` → undefined nếu bất kỳ level nào null/undefined.
- `fn?.()` → call function chỉ khi exists.
- `arr?.[index]` → access array element safely.

**Khác `&&` operator:**

- `?.` short-circuit tại null/undefined only.
- `&&` short-circuit tại falsy values (0, "", false...).

#### **10. Nullish Coalescing `??` (ES2020) - Default Values:**

**Syntax:**

- `value ?? 'default'` → return 'default' chỉ khi value = null/undefined.

**Khác `||` operator:**

- `||` fallback tại falsy values: `0 || 10` → 10 (sai nếu 0 là valid).
- `??` fallback chỉ tại null/undefined: `0 ?? 10` → 0 (đúng).

### ⚡ ES2016-ES2023 Highlights (Yearly Updates):

| Year     | Version | Key Features                                                                                                                                            |
| -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2016** | ES7     | `**` (exponentiation: `2**3` = 8), `Array.includes()`                                                                                                   |
| **2017** | ES8     | **`async/await`**, `Object.values/entries()`, `String.padStart/padEnd()`, shared memory, atomics                                                        |
| **2018** | ES9     | Rest/Spread for objects, **async iteration** (`for await...of`), Promise.finally(), RegExp improvements                                                 |
| **2019** | ES10    | `Array.flat/flatMap()`, `Object.fromEntries()`, `String.trimStart/trimEnd()`, optional catch binding                                                    |
| **2020** | ES11    | **Optional chaining `?.`**, **nullish coalescing `??`**, **`BigInt`**, `Promise.allSettled()`, dynamic `import()`, `globalThis`                         |
| **2021** | ES12    | `String.replaceAll()`, numeric separators (`1_000_000`), `Promise.any()`, logical assignment (`\|\|=`, `&&=`, `??=`), `WeakRef`, `FinalizationRegistry` |
| **2022** | ES13    | **Top-level `await`**, **private fields `#field`**, static blocks, `Array.at()`, `Object.hasOwn()`, `Error.cause`                                       |
| **2023** | ES14    | `Array.findLast/findLastIndex()`, **immutable array methods** (`toSorted()`, `toReversed()`, `toSpliced()`), `Array.with()`, Hashbang grammar           |

### ⚠️ Browser Compatibility & Transpilation:

**Browser Support:**

- **ES5**: Universal (IE9+, tất cả browsers).
- **ES6 (2015)**: Chrome 51+, Firefox 54+, Safari 10+, Edge 14+.
- **ES2020+**: Chrome 80+, Firefox 72+, Safari 13.1+ (>95% users).

**Transpilation Strategy (Chiến lược chuyển đổi):**

1. **Babel** - Compile ES6+ → ES5:

   - **@babel/preset-env**: Auto detect targets, compile only cần thiết.
   - Config: `.babelrc` with `targets: "> 0.25%, not dead"`.

2. **Polyfills** - Add missing runtime features:

   - **core-js**: Polyfills cho Promises, Array methods, etc.
   - Import: `import 'core-js/stable';` hoặc Babel auto-inject.

3. **TypeScript** - Compile TS → ES5/ES6:
   - `tsconfig.json` → `"target": "ES5"`.
   - Built-in transpilation, no Babel needed (nhưng có thể combine).

**Modern Build Strategy:**

- **Differential Loading**: Ship ES6 cho modern browsers, ES5 cho legacy.
  - `<script type="module">` → modern (smaller, faster).
  - `<script nomodule>` → legacy fallback.

### ✅ Best Practices (Thực hành tốt nhất):

1. **Write ES6+ code, transpile for production**.

   - _Lý do_: Clean code, readable, modern features.
   - _Setup_: Babel + Webpack/Vite.

2. **Dùng `const` by default, `let` khi cần, KHÔNG `var`**.

   - _Pattern_: `const` cho 90% cases.

3. **Arrow functions cho callbacks, regular cho methods**.

   - _Lý do_: Arrow inherit `this`, methods cần own `this`.

4. **Destructuring cho cleaner code**.

   - _VD_: `const {name, age} = user;` thay vì `const name = user.name;`.

5. **Spread cho immutable operations**.

   - _Pattern_: `{...obj, updated: true}` thay vì `obj.updated = true`.

6. **Optional chaining cho nested access**.

   - _Pattern_: `user?.address?.city` thay vì `user && user.address && user.address.city`.

7. **Nullish coalescing cho default values**.

   - _Pattern_: `value ?? 'default'` thay vì `value || 'default'` (vì 0, "" là valid).

8. **Async/await thay vì Promise chains**.

   - _Lý do_: Readable, easy error handling với `try/catch`.

9. **ES Modules (`import/export`) thay vì CommonJS**.

   - _Benefit_: Tree-shaking, static analysis, modern standard.

10. **Target modern browsers first, transpile nếu cần**.
    - _Tool_: Browserslist config → Babel auto-detect targets.

### ❌ Common Mistakes:

1. **Dùng arrow functions cho object methods**.

   - ❌ `{ method: () => this.value }` → `this` = outer scope.
   - ✅ `{ method() { return this.value; } }`.

2. **Quên `const` immutable chỉ là binding, không phải deep immutable**.

   - `const obj = {x:1}; obj.x = 2;` → OK (object mutable).
   - `const obj = {x:1}; obj = {};` → Error (binding immutable).

3. **Spread cho deep copy**.

   - ❌ `const copy = {...obj};` với nested objects → shallow copy.
   - ✅ `const copy = structuredClone(obj);`.

4. **Nullish coalescing với falsy values khác null**.

   - `0 ?? 10` → 0 (đúng), `0 || 10` → 10 (có thể sai).

5. **Optional chaining không replace validation**.

   - `user?.address?.city` → undefined (silent), có thể cần throw error hoặc default value.

6. **Async/await trong loops tuần tự mà không cần**.
   - ❌ `for (const id of ids) { await fetch(id); }` → slow sequential.
   - ✅ `await Promise.all(ids.map(id => fetch(id)));` → parallel.

### 🔬 Deep Dive Insights:

#### **1. Babel Transpilation Deep Dive:**

- Babel parse code → AST (Abstract Syntax Tree) → transform → generate code.
- Plugins transform specific features: `@babel/plugin-transform-arrow-functions`.
- Presets = bundle of plugins: `@babel/preset-env` (smart, target-based).

#### **2. Tree-Shaking Requires ES Modules:**

- CommonJS (`require()`) = dynamic imports → bundler không biết dependencies lúc build.
- ES Modules (`import`) = static imports → bundler analyze → remove unused exports.
- **Dead Code Elimination** (DCE): Webpack/Rollup remove unused imports.

#### **3. Polyfill Size Concerns:**

- `core-js` full = ~90KB minified.
- **Solution**: `@babel/preset-env` with `useBuiltIns: 'usage'` → chỉ import polyfills thực sự dùng.

#### **4. Performance: ES6+ vs ES5:**

- Modern engines (V8, SpiderMonkey) optimize ES6+ natively.
- Classes, arrow functions, destructuring = zero overhead (compile to optimized machine code).
- **Myth**: "ES5 faster vì simpler" → Sai, modern JS optimized tốt hơn.

---

> **💡 Tổng hợp**: ES5 (2009) → ES6 (2015 - major update) → Yearly releases (2016+) | Key features: `let/const`, arrows, classes, modules, Promises, async/await, optional chaining `?.`, nullish coalescing `??` | Transpilation: Babel → ES5 for legacy browsers | Tree-shaking requires ES Modules | Modern strategy: Write ES6+, transpile for production

---

## Q04: Hoisting & Temporal Dead Zone (TDZ) - Cơ Chế Nâng Khai Báo

### 🎯 Trả Lời Ngắn Gọn:

**"Hoisting là cơ chế JavaScript 'nâng' (hoist) khai báo lên đầu scope trước khi execute code. `var` được hoisted + initialized = `undefined`, còn `let/const` được hoisted nhưng KHÔNG initialized → Temporal Dead Zone (TDZ) → ReferenceError nếu access trước khai báo."**

### 📖 Giải Thích Chi Tiết - Cách JavaScript Engine Hoạt Động:

JavaScript engine thực thi code qua **2 phases** (2 giai đoạn):

**Phase 1 - Creation Phase (Giai đoạn khởi tạo):**

1. Scan toàn bộ code để tìm declarations (khai báo).
2. **Allocate memory** (cấp phát bộ nhớ) cho declarations.
3. `var` → initialized = `undefined`.
4. `let/const` → chỉ allocated, KHÔNG initialized (TDZ).
5. `function declarations` → entire function được stored.

**Phase 2 - Execution Phase (Giai đoạn thực thi):**

1. Execute code line-by-line từ trên xuống.
2. Assignments được thực hiện tại đúng dòng code.

### 🔑 Hoisting Behaviors (Hành vi hoisting - Bảng tổng hợp):

| Type                       | Hoisted?               | Initialized?             | Access Before Declaration   | Scope                 |
| -------------------------- | ---------------------- | ------------------------ | --------------------------- | --------------------- |
| **`var`**                  | ✅ Yes                 | ✅ Yes (`undefined`)     | ✅ OK (undefined)           | Function              |
| **`let`**                  | ✅ Yes                 | ❌ No (TDZ)              | ❌ ReferenceError           | Block                 |
| **`const`**                | ✅ Yes                 | ❌ No (TDZ)              | ❌ ReferenceError           | Block                 |
| **`function` declaration** | ✅ Yes                 | ✅ Yes (entire function) | ✅ OK (callable)            | Function/Block\*      |
| **`function` expression**  | ✅ Yes (var only)      | ❌ No                    | ❌ ReferenceError/undefined | Same as var           |
| **Arrow function**         | ✅ Yes (var/let/const) | ❌ No                    | ❌ ReferenceError/undefined | Same as var/let/const |
| **`class`**                | ✅ Yes                 | ❌ No (TDZ)              | ❌ ReferenceError           | Block                 |

\*Function declarations: function-scoped trong non-strict mode, block-scoped trong strict mode.

### 📊 Chi Tiết Từng Loại:

#### **1. `var` Hoisting - Hoisted + Initialized:**

**Chú thích tiếng Việt:**

- `var` được "nâng" lên đầu **function scope** (hoặc global nếu ngoài function).
- Initialized = `undefined` → access trước khai báo = `undefined` (KHÔNG error).

**Ví dụ conceptual (không phải code thật):**

```javascript
// Code bạn viết:
console.log(x); // undefined (không error)
var x = 5;
console.log(x); // 5

// JavaScript engine hiểu là:
var x; // Hoisted to top, initialized = undefined
console.log(x); // undefined
x = 5; // Assignment tại đúng dòng
console.log(x); // 5
```

**Vấn đề:**

- Dễ gây bugs vì access trước khai báo không throw error.
- Function scope (không phải block scope) → confusion trong loops/if blocks.

#### **2. `let/const` Hoisting + TDZ - Hoisted nhưng KHÔNG Initialized:**

**Temporal Dead Zone (TDZ - Vùng chết tạm thời):**

- **Định nghĩa**: Vùng từ **đầu block scope** đến **dòng khai báo `let/const`**.
- Trong TDZ: Biến exists (hoisted) nhưng KHÔNG thể access → `ReferenceError`.

**Chú thích tiếng Việt:**

- TDZ là "vùng cấm" - access biến trong vùng này → crash.
- Mục đích: **Force developers** khai báo trước khi dùng → catch bugs sớm.

**Ví dụ conceptual:**

```javascript
// Code:
{
  // --- TDZ starts here for 'x' ---
  console.log(x); // ReferenceError: Cannot access 'x' before initialization
  // --- TDZ ends here ---
  let x = 10;
  console.log(x); // 10 - OK, ngoài TDZ rồi
}

// Engine hiểu:
{
  // TDZ: x hoisted nhưng KHÔNG initialized
  // Any access to x → ReferenceError
  let x; // TDZ ends, x = undefined
  x = 10; // Assignment
}
```

**`const` đặc biệt:**

- Phải initialized ngay khi khai báo: `const x = 10;` (không được `const x;`).
- TDZ rules giống `let`.

#### **3. Function Declaration Hoisting - Hoisted Toàn Bộ:**

**Chú thích tiếng Việt:**

- **Entire function** được hoisted (cả khai báo lẫn implementation).
- Có thể gọi function trước khi khai báo → OK.

**Ví dụ:**

```javascript
// Code:
hello(); // "Hello!" - OK, function đã hoisted

function hello() {
  console.log('Hello!');
}

// Engine hiểu:
function hello() {
  // Hoisted to top
  console.log('Hello!');
}
hello(); // OK
```

**Strict mode caveat:**

- Non-strict: function-scoped.
- Strict mode: block-scoped (giống `let`).

#### **4. Function Expression Hoisting - Chỉ Variable Hoisted:**

**Chú thích tiếng Việt:**

- Variable (`var/let/const`) hoisted theo rules của nó.
- Function body KHÔNG hoisted.

**Ví dụ với `var`:**

```javascript
// Code:
hello(); // TypeError: hello is not a function (hello = undefined)

var hello = function () {
  console.log('Hello!');
};

// Engine hiểu:
var hello; // Hoisted, = undefined
hello(); // undefined() → TypeError
hello = function () {
  console.log('Hello!');
};
```

**Ví dụ với `const`:**

```javascript
// Code:
hello(); // ReferenceError: Cannot access 'hello' before initialization (TDZ)

const hello = function () {
  console.log('Hello!');
};
```

#### **5. Class Hoisting - Giống `let/const` (TDZ):**

**Chú thích tiếng Việt:**

- Classes hoisted nhưng KHÔNG initialized → TDZ.
- Access trước khai báo → `ReferenceError`.

**Ví dụ:**

```javascript
// Code:
const obj = new MyClass(); // ReferenceError: Cannot access 'MyClass' before initialization

class MyClass {
  constructor() {}
}
```

### ⚠️ Common Pitfalls (Lỗi thường gặp - Chi tiết):

#### **1. `typeof` Operator trong TDZ:**

**Ví dụ:**

```javascript
// With var (safe):
console.log(typeof x); // "undefined" - OK, không error
var x = 5;

// With let (NOT safe - TDZ):
console.log(typeof x); // ReferenceError: Cannot access 'x' before initialization
let x = 5;
```

**Giải thích:**

- `typeof` truyền thống safe với undeclared variables: `typeof neverDeclared` → "undefined".
- Nhưng với `let/const`: TDZ override behavior này → ReferenceError.

#### **2. Loop Variables - `var` vs `let` trong Closures:**

**Với `var` (function-scoped):**

```javascript
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// Output: 3, 3, 3 (tất cả closures share same 'i')
```

**Với `let` (block-scoped per iteration):**

```javascript
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// Output: 0, 1, 2 (mỗi iteration có 'i' riêng)
```

**Giải thích:**

- `var`: 1 biến `i` duy nhất cho toàn bộ loop → all closures reference same `i`.
- `let`: Mỗi iteration tạo **new binding** của `i` → each closure có `i` riêng.

#### **3. Hoisting trong Nested Scopes:**

**Ví dụ:**

```javascript
var x = 'outer';

function fn() {
  console.log(x); // undefined (NOT "outer")
  var x = 'inner';
  console.log(x); // "inner"
}

fn();
```

**Giải thích:**

- `var x = 'inner';` hoisted lên đầu function scope.
- First `console.log`: `x` exists (hoisted) nhưng = `undefined`.
- NOT access outer `x` vì inner `x` đã hoisted (shadowing).

### ✅ Best Practices (Thực hành tốt nhất - Chi tiết):

1. **KHÔNG BAO GIỜ dùng `var` - Dùng `const/let` only**.

   - _Lý do_: `var` gây confusion (function scope, hoisting, no TDZ).
   - _Exception_: Legacy code maintenance.

2. **Default `const`, chỉ dùng `let` khi cần reassign**.

   - _Lý do_: `const` ngăn accidental reassignment → fewer bugs.
   - _Pattern_: ~90% variables nên là `const`.

3. **Khai báo variables ở TOP của scope** (explicit hoisting).

   - _Lý do_: Easier to read, clear dependencies, mimic engine behavior.
   - _Pattern_: Declarations first, logic sau.

4. **ESLint rules để enforce**:

   - `no-var`: Ban `var` keyword.
   - `no-use-before-define`: Ban access trước khai báo.
   - `prefer-const`: Suggest `const` khi variable không reassign.

5. **Function declarations cho top-level functions**.

   - _Lý do_: Hoisting cho phép organize code tự nhiên (main logic trên, helpers dưới).
   - _Pattern_: `function declaration` cho named functions, arrow/expression cho callbacks.

6. **Avoid temporal coupling** (logic phụ thuộc thứ tự).
   - _Bad_: Code phụ thuộc hoisting behavior.
   - _Good_: Code works regardless of declaration order.

### 🔬 Deep Dive Insights (Kiến thức chuyên sâu):

#### **1. Why TDZ Exists - Design Decision:**

**Problems TDZ solves:**

- **Catch bugs early**: Access before declaration thường là bug → TDZ throw error ngay.
- **Consistent behavior**: `const` phải initialized khi khai báo → TDZ enforce điều này.
- **Block scope clarity**: Make block scope boundaries clear và predictable.

**Trade-off:**

- Less "forgiving" hơn `var` (stricter).
- Developers phải học thêm concept mới (TDZ).
- **Overall benefit**: Fewer bugs > convenience.

#### **2. Hoisting & Performance:**

**V8 Engine Optimization:**

- Hoisting là **compile-time behavior** (NOT runtime overhead).
- Engine analyze code → create execution contexts trước khi run.
- **Zero runtime cost** - hoisting chỉ là conceptual model.

**Myth busting:**

- _Myth_: "Hoisting slows code down".
- _Reality_: Hoisting không ảnh hưởng runtime performance (chỉ là parsing phase).

#### **3. Execution Context & Hoisting:**

**Execution Context Structure:**

```
ExecutionContext = {
  LexicalEnvironment: {
    EnvironmentRecord: {
      // let/const/function declarations
    },
    outer: <reference to parent scope>
  },
  VariableEnvironment: {
    EnvironmentRecord: {
      // var declarations
    }
  },
  ThisBinding: <value of 'this'>
}
```

**Hoisting mapping:**

- `let/const` → LexicalEnvironment (TDZ applies).
- `var` → VariableEnvironment (initialized = undefined).
- Function declarations → LexicalEnvironment (fully initialized).

#### **4. Strict Mode Impact:**

**Function declarations trong blocks:**

```javascript
// Non-strict mode:
if (true) {
  function fn() {} // Function-scoped (hoisted to enclosing function)
}
fn(); // OK

// Strict mode:
('use strict');
if (true) {
  function fn() {} // Block-scoped (NOT hoisted outside block)
}
fn(); // ReferenceError
```

**Best practice:**

- Luôn enable strict mode: `'use strict';` ở top file/function.
- Hoặc dùng ES modules (auto strict mode).

---

> **💡 Tổng hợp**: Hoisting = nâng khai báo lên top scope | `var`: hoisted + initialized = `undefined` | `let/const`: hoisted nhưng KHÔNG initialized → TDZ (ReferenceError) | Function declarations: hoisted toàn bộ | Function expressions: chỉ variable hoisted | TDZ: từ đầu block đến dòng khai báo | Best practice: Dùng `const/let`, khai báo ở top, ESLint rules

---

## Q05: Set/Map, WeakSet/WeakMap, WeakRef & FinalizationRegistry - Modern Collections

### 🎯 Trả Lời Ngắn Gọn:

**"Set lưu unique values (O(1) operations), Map lưu key-value pairs với keys bất kỳ type. WeakMap/WeakSet dùng weak references → không ngăn GC → prevent memory leaks. WeakRef/FinalizationRegistry cho advanced memory management (rarely needed)."**

### 📖 Giải Thích Chi Tiết:

#### **1. Set - Unique Values Collection (Tập hợp giá trị duy nhất):**

**Định nghĩa:**

- Collection chứa **unique values** (giá trị duy nhất, không trùng lặp).
- Values có thể là **bất kỳ type nào** (primitives, objects).
- **Maintain insertion order** (theo thứ tự thêm vào).

**API Methods:**

- `.add(value)`: Thêm value (return Set object → chainable).
- `.has(value)`: Check exists (return boolean) - **O(1)**.
- `.delete(value)`: Xóa value (return boolean) - **O(1)**.
- `.clear()`: Xóa tất cả.
- `.size`: Property (NOT method) → số lượng elements.
- `.forEach(callback)`, `.values()`, `.keys()` (alias), `.entries()`: Iteration.

**Set vs Array:**

| Aspect                        | Set                | Array                 |
| ----------------------------- | ------------------ | --------------------- |
| **Duplicates**                | ❌ Auto removed    | ✅ Allowed            |
| **`.has()` / `.includes()`**  | O(1) - hash table  | O(n) - linear search  |
| **`.add()` / `.push()`**      | O(1)               | O(1) amortized        |
| **`.delete()` / `.splice()`** | O(1)               | O(n) - shift elements |
| **Order**                     | ✅ Insertion order | ✅ Index order        |
| **Indexed access**            | ❌ No `set[0]`     | ✅ `arr[0]`           |

**Use Cases:**

- **Deduplicate arrays**: `[...new Set(arr)]`.
- **Fast membership check**: `set.has(value)` faster than `arr.includes(value)`.
- **Unique tags/IDs**: Lưu unique user IDs, tags, categories.
- **Remove duplicates from primitives**: Works với primitives và object references.

**Chú thích tiếng Việt:**

- Set = "tập hợp" (toán học) - không trùng lặp.
- Operations nhanh vì internally dùng **hash table** (bảng băm).

#### **2. Map - Key-Value Pairs với Keys Bất Kỳ:**

**Định nghĩa:**

- Collection chứa **key-value pairs**.
- Keys có thể là **bất kỳ type nào** (objects, functions, primitives) - khác Object (chỉ string/symbol).
- **Maintain insertion order** (iterate theo thứ tự thêm).

**API Methods:**

- `.set(key, value)`: Set key-value (return Map → chainable).
- `.get(key)`: Get value by key (return value hoặc `undefined`) - **O(1)**.
- `.has(key)`: Check key exists - **O(1)**.
- `.delete(key)`: Delete entry - **O(1)**.
- `.clear()`: Xóa tất cả.
- `.size`: Property → số lượng entries.
- `.forEach(callback)`, `.keys()`, `.values()`, `.entries()`: Iteration.

**Map vs Object:**

| Aspect          | Map                                       | Object                                          |
| --------------- | ----------------------------------------- | ----------------------------------------------- |
| **Key types**   | Any type (objects, functions, primitives) | String / Symbol only                            |
| **Key order**   | ✅ Insertion order (predictable)          | ⚠️ Complex (integer keys first, then insertion) |
| **Size**        | `.size` property (O(1))                   | `Object.keys(obj).length` (O(n))                |
| **Iteration**   | `.forEach()`, `for...of` (direct)         | `for...in`, `Object.keys()` (helpers needed)    |
| **Performance** | Optimized for frequent add/delete         | Better for static structure                     |
| **Prototype**   | ❌ No prototype pollution                 | ⚠️ Has `__proto__`, `constructor`               |
| **JSON**        | ❌ Not serializable                       | ✅ `JSON.stringify()` works                     |

**Use Cases:**

- **Cache với object keys**: `map.set(domElement, data)`.
- **Counting occurrences**: `map.set(item, (map.get(item) || 0) + 1)`.
- **Ordered data**: Iterate theo thứ tự insert (predictable).
- **Metadata storage**: Associate data với objects mà không modify objects.

**Chú thích tiếng Việt:**

- Map = "ánh xạ" (key → value).
- Mạnh hơn Object vì keys flexible (không bị coerce to string).

#### **3. WeakMap - Weak References cho Keys (Tham chiếu yếu):**

**Định nghĩa:**

- Giống Map nhưng:
  - **Keys PHẢI là objects** (không được primitives).
  - Keys là **weak references** → không ngăn GC.
  - **Không iterable** (không có `.forEach()`, `.keys()`, `.values()`).
  - **Không có `.size`** property.

**Why "Weak"?**

- Normal Map: Giữ **strong reference** → object không bị GC nếu còn trong Map.
- WeakMap: Giữ **weak reference** → object có thể bị GC nếu không có strong reference khác.

**API Methods (Limited):**

- `.set(key, value)`: Set key-value (key MUST be object).
- `.get(key)`: Get value.
- `.has(key)`: Check key exists.
- `.delete(key)`: Delete entry.
- ❌ NO `.clear()`, `.size`, `.forEach()`, iteration methods.

**Use Cases:**

1. **Private data pattern** (trước khi có `#private` fields):

```javascript
const privateData = new WeakMap();

class User {
  constructor(name) {
    privateData.set(this, { password: 'secret' });
    this.name = name;
  }

  getPassword() {
    return privateData.get(this).password; // Access private data
  }
}

// privateData auto cleanup khi User instance bị GC
```

2. **DOM node metadata** (auto cleanup khi node removed):

```javascript
const domMetadata = new WeakMap();

function attachMetadata(element, data) {
  domMetadata.set(element, data); // No memory leak!
}

// Khi element removed from DOM và không còn reference → GC → metadata tự xóa
```

3. **Caching** (prevent memory leaks):

```javascript
const cache = new WeakMap();

function expensiveOperation(obj) {
  if (cache.has(obj)) return cache.get(obj);

  const result = /* ... heavy computation ... */;
  cache.set(obj, result);
  return result;
}

// Cache auto cleanup khi obj không còn dùng
```

**Memory Leak Prevention:**

- Normal Map: `map.set(domNode, data)` → domNode không bị GC dù đã remove → **memory leak**.
- WeakMap: `weakMap.set(domNode, data)` → domNode bị GC khi remove → **no leak**.

#### **4. WeakSet - Weak References cho Values:**

**Định nghĩa:**

- Giống Set nhưng:
  - **Values PHẢI là objects**.
  - Values là **weak references**.
  - **Không iterable**, không có `.size`.

**API Methods:**

- `.add(value)`: Add object.
- `.has(value)`: Check exists.
- `.delete(value)`: Delete.
- ❌ NO `.clear()`, `.size`, iteration.

**Use Cases:**

1. **Mark objects** without preventing GC:

```javascript
const processedNodes = new WeakSet();

function processNode(node) {
  if (processedNodes.has(node)) return; // Already processed

  // Process node...
  processedNodes.add(node); // Mark as processed
}

// Auto cleanup khi nodes không còn reference
```

2. **Private flags** (check if object "tagged"):

```javascript
const validObjects = new WeakSet();

function validate(obj) {
  validObjects.add(obj); // Tag as valid
}

function isValid(obj) {
  return validObjects.has(obj);
}
```

#### **5. WeakRef (ES2021) - Weak Reference đến 1 Object Cụ Thể:**

**Định nghĩa:**

- Tạo **weak reference** trực tiếp đến 1 object.
- Object có thể bị GC ngay cả khi WeakRef còn tồn tại.
- `.deref()` method → return object hoặc `undefined` (nếu đã GC).

**⚠️ Non-Deterministic (Không xác định):**

- Không biết chính xác KHI NÀO object bị GC.
- Không rely on WeakRef cho core app logic.

**Use Case (Rare - Advanced):**

- Caching large objects mà không ngăn GC.
- Observer pattern với weak references.

**Ví dụ conceptual:**

```javascript
let obj = { data: 'large' };
const weakRef = new WeakRef(obj);

// Sometime later...
const deref = weakRef.deref();
if (deref) {
  console.log(deref.data); // 'large' - object still alive
} else {
  console.log("Object was GC'ed"); // object đã bị GC
}

obj = null; // Remove strong reference → obj có thể bị GC
```

#### **6. FinalizationRegistry (ES2021) - Callback Khi Object Bị GC:**

**Định nghĩa:**

- Registry chạy callback khi objects bị GC.
- Dùng để **cleanup external resources** (file handles, WebAssembly memory, native resources).

**⚠️ Caveats:**

- **Non-deterministic**: Callback có thể chạy bất cứ lúc nào (hoặc không chạy).
- **KHÔNG dùng cho app logic** - chỉ dùng cho cleanup.

**Ví dụ conceptual:**

```javascript
const registry = new FinalizationRegistry((heldValue) => {
  console.log(`Cleanup for ${heldValue}`);
  // Close file handle, free native memory, etc.
});

let obj = { data: 'something' };
registry.register(obj, 'my-object', obj); // Register với held value

obj = null; // Remove reference → eventually GC → callback fires
```

### ✅ Best Practices:

1. **Dùng Set để deduplicate arrays**: `[...new Set(arr)]` - simple, readable.
2. **Dùng Map khi keys không phải string**: `map.set(obj, value)` thay vì `obj[String(key)]`.
3. **WeakMap cho private data / DOM metadata**: Prevent memory leaks.
4. **WeakSet cho object tagging**: Mark objects without memory leaks.
5. **Avoid WeakRef/FinalizationRegistry** unless absolutely needed (advanced, rare use cases).
6. **Convert Map to Object khi cần JSON**: `Object.fromEntries(map)`.
7. **Prefer Map over Object cho dynamic data**: Add/delete frequent → Map optimized.

### ❌ Common Mistakes:

1. **Dùng Object khi cần Map**.

   - ❌ Keys bị convert to string → `obj[{a:1}]` = `obj["[object Object]"]`.
   - ✅ Map giữ nguyên object keys.

2. **Dùng WeakMap với primitive keys**.

   - ❌ `weakMap.set('key', value)` → TypeError.
   - ✅ Keys phải là objects.

3. **Expect WeakRef.deref() luôn return object**.

   - ❌ Assume `weakRef.deref()` always truthy.
   - ✅ Check `if (weakRef.deref())` trước khi dùng.

4. **Iterate WeakMap/WeakSet**.

   - ❌ Không có `.forEach()`, `.keys()`.
   - ✅ Không thể iterate (by design - entries có thể biến mất).

5. **Rely on FinalizationRegistry cho core logic**.
   - ❌ Callback non-deterministic, có thể không chạy.
   - ✅ Chỉ dùng cho cleanup, không cho business logic.

### 🔬 Deep Dive Insights:

#### **1. SameValueZero Algorithm:**

- Set/Map dùng **SameValueZero** để compare keys/values.
- Giống `===` NHƯNG: `NaN === NaN` trong Set/Map (khác `===` operator).
- `+0 === -0` (giống `===`).

**Ví dụ:**

```javascript
const set = new Set([NaN, NaN]);
console.log(set.size); // 1 (NaN chỉ được add 1 lần)

NaN === NaN; // false (với === operator)
```

#### **2. Performance - Set/Map vs Array/Object:**

**Benchmarks (typical):**

- Set `.has()`: ~O(1) - hash lookup.
- Array `.includes()`: O(n) - linear scan.
- Map `.get()`: ~O(1) - hash lookup.
- Object property access: ~O(1) - optimized in engines.

**When to use:**

- **Frequent lookups/inserts/deletes**: Set/Map (optimized).
- **Static data, rare changes**: Array/Object (simpler).
- **Large datasets**: Set/Map scale better.

#### **3. WeakMap Internal Mechanics:**

**How weak references work:**

- Engine track references: strong refs (normal) vs weak refs (WeakMap/WeakSet).
- GC mark phase: Chỉ follow strong refs.
- Objects chỉ có weak refs → marked for collection.
- WeakMap entries tự động removed (không cần cleanup code).

**Why không iterable:**

- Entries có thể biến mất bất cứ lúc nào (non-deterministic GC).
- Iteration không reliable → disabled by design.

#### **4. Memory Leaks với Event Listeners:**

**Problem với normal Map:**

```javascript
const listenerData = new Map();

function attachListener(element) {
  const handler = () => console.log('click');
  element.addEventListener('click', handler);
  listenerData.set(element, handler); // Strong reference → element không GC
}

// Element removed from DOM nhưng vẫn trong Map → MEMORY LEAK
```

**Solution với WeakMap:**

```javascript
const listenerData = new WeakMap();

function attachListener(element) {
  const handler = () => console.log('click');
  element.addEventListener('click', handler);
  listenerData.set(element, handler); // Weak reference → element có thể GC
}

// Element removed → GC → WeakMap entry tự xóa → NO LEAK
```

---

> **💡 Tổng hợp**: Set (unique values, O(1) operations) vs Array (indexed, duplicates OK) | Map (any keys, insertion order) vs Object (string keys, prototype) | WeakMap/WeakSet (weak refs, no iteration, prevent leaks) | WeakRef (direct weak ref to object) | FinalizationRegistry (cleanup callback, non-deterministic) | Use WeakMap cho DOM metadata, private data | SameValueZero: NaN === NaN trong Set/Map

---

## Q06: Event Loop - Cơ Chế Hoạt Động JavaScript (Technical Deep Dive)

### 🎯 Trả Lời Ngắn Gọn:

**"JavaScript là single-threaded (đơn luồng) với 1 Call Stack, nhưng xử lý async nhờ Event Loop phối hợp giữa Call Stack, Web APIs, Microtask Queue (Promise - ưu tiên cao), và Macrotask Queue (setTimeout - ưu tiên thấp). Thuật toán Event Loop: 1) Execute ALL sync code trong Call Stack, 2) Execute ALL microtasks, 3) UI Render (nếu cần - browser only), 4) Execute ONE macrotask, 5) Repeat vô hạn."**

### 📖 Giải Thích Chi Tiết - Cách JavaScript Engine Hoạt Động:

JavaScript được thiết kế để **single-threaded** (đơn luồng) vì ban đầu chỉ dùng cho manipulate DOM trong browser → tránh race conditions khi nhiều threads cùng modify DOM. Nhưng single-threaded không có nghĩa là không thể xử lý async - Event Loop giải quyết vấn đề này.

**Tại sao cần Event Loop?**

- Single thread → blocking operations (I/O, network, timers) sẽ freeze UI.
- Solution: Offload blocking operations ra Web APIs (browser threads) hoặc libuv (Node.js).
- Event Loop điều phối khi nào callbacks được đưa vào Call Stack để execute.

### 🏗️ Kiến Trúc Runtime JavaScript (5 Thành Phần Chính):

#### **1. Call Stack (Ngăn xếp gọi - LIFO):**

**Chú thích tiếng Việt:**

- **Call Stack** = "ngăn xếp gọi" - nơi JavaScript thực thi code đồng bộ.
- Cấu trúc: **LIFO** (Last In First Out - vào sau ra trước).
- **Single-threaded** → chỉ có 1 Call Stack → chỉ 1 function execute tại 1 thời điểm.

**Cách hoạt động:**

1. Gọi function → **push** execution context lên stack.
2. Function return → **pop** execution context ra khỏi stack.
3. Stack empty → Event Loop kiểm tra queues.

**Stack Overflow:**

- Xảy ra khi: Recursion không có base case → stack grow vô hạn.
- Browser limit: ~10,000-15,000 frames (depends on browser).
- Error: `Maximum call stack size exceeded`.

#### **2. Heap (Vùng nhớ động):**

**Chú thích tiếng Việt:**

- **Heap** = "đống" - vùng nhớ không cấu trúc để lưu objects, arrays, functions.
- Managed by Garbage Collector (GC).
- Khác Stack: Stack = structured (LIFO), Heap = unstructured (random access).

#### **3. Web APIs (Browser) / C++ APIs (Node.js):**

**Chú thích tiếng Việt:**

- **Web APIs** = các APIs browser cung cấp, chạy trên **threads riêng** (không phải main thread).
- Examples: `setTimeout`, `setInterval`, `fetch`, DOM events, `XMLHttpRequest`.
- **Node.js**: libuv (C++ library) cung cấp async I/O (file system, network, crypto).

**Cách hoạt động:**

1. Call async API (vd: `setTimeout(fn, 1000)`) → đăng ký callback với Web API.
2. Web API handle async operation trên thread riêng.
3. Khi done → push callback vào **Task Queue** (Macrotask hoặc Microtask).

#### **4. Microtask Queue (Hàng đợi vi nhiệm vụ - Ưu tiên cao):**

**Chú thích tiếng Việt:**

- **Microtask** = "vi nhiệm vụ" - tasks có priority cao hơn macrotasks.
- **FIFO** (First In First Out - vào trước ra trước).
- **Process ALL**: Event Loop chạy HẾT tất cả microtasks trong queue trước khi chuyển sang macrotask.

**Loại Microtasks:**

- `Promise.then()`, `Promise.catch()`, `Promise.finally()`.
- `queueMicrotask(callback)` (explicit microtask API).
- `MutationObserver` callbacks.
- `process.nextTick()` (Node.js - technically higher priority than microtasks).

**Tại sao Microtasks ưu tiên cao?**

- Promises cần **immediate execution** sau sync code để maintain predictable flow.
- React `setState` batching relies on microtasks.

#### **5. Macrotask Queue (Hàng đợi vĩ nhiệm vụ - Ưu tiên thấp):**

**Chú thích tiếng Việt:**

- **Macrotask** = "vĩ nhiệm vụ" - tasks priority thấp hơn microtasks.
- **FIFO** structure.
- **Process ONE**: Event Loop chỉ chạy 1 macrotask mỗi vòng lặp.

**Loại Macrotasks:**

- `setTimeout`, `setInterval`.
- `setImmediate` (Node.js only).
- I/O operations (network, file system).
- UI rendering events.
- `MessageChannel`, `postMessage`.

### ♻️ Thuật Toán Event Loop (Chi Tiết - Step by Step):

**Event Loop là vòng lặp vô hạn theo thuật toán sau:**

```
while (true) {
  // Step 1: Execute ALL sync code in Call Stack
  while (callStack.isNotEmpty()) {
    executeNextFunction();
  }

  // Step 2: Execute ALL Microtasks (IMPORTANT: ALL, not just one)
  while (microtaskQueue.isNotEmpty()) {
    const microtask = microtaskQueue.dequeue();
    callStack.push(microtask);
    executeNextFunction();
  }

  // Step 3: Render UI (Browser only, ~60fps = every 16ms)
  if (isTimeToRender()) {
    renderUI();
  }

  // Step 4: Execute ONE Macrotask
  if (macrotaskQueue.isNotEmpty()) {
    const macrotask = macrotaskQueue.dequeue();
    callStack.push(macrotask);
    executeNextFunction();
  }

  // Step 5: Repeat (back to Step 1)
}
```

**Detailed Explanation (Giải thích chi tiết từng bước):**

**Step 1 - Execute Synchronous Code:**

- Chạy tất cả code đồng bộ từ script ban đầu.
- Functions được push/pop từ Call Stack.
- Khi gặp async API → đăng ký callback với Web APIs, không block.

**Step 2 - Process ALL Microtasks:**

- **Critical**: Chạy HẾT tất cả microtasks, kể cả microtasks mới được add trong quá trình xử lý.
- **Starvation risk**: Nếu microtask liên tục add microtask mới → infinite loop → UI freeze.

**Step 3 - UI Rendering (Browser Only):**

- Browser cố gắng maintain 60fps → render every ~16ms.
- **Render steps**: Recalculate styles → Layout → Paint → Composite.
- **requestAnimationFrame** callbacks chạy TRƯỚC render step này.

**Step 4 - Execute ONE Macrotask:**

- Chỉ lấy 1 macrotask từ queue.
- Sau khi execute xong → quay lại Step 1 (check microtasks again).

**Step 5 - Repeat:**

- Vòng lặp tiếp tục mãi mãi (hoặc đến khi close tab/process).

### 🔑 Điểm Khác Biệt Quan Trọng:

#### **1. Microtask vs Macrotask (Bảng so sánh):**

| Aspect                | Microtask                                      | Macrotask                               |
| --------------------- | ---------------------------------------------- | --------------------------------------- |
| **Priority**          | Cao (run trước macrotask)                      | Thấp (run sau microtask)                |
| **Process per loop**  | **ALL** (hết tất cả)                           | **ONE** (chỉ 1 task)                    |
| **Examples**          | Promise.then, queueMicrotask, MutationObserver | setTimeout, setInterval, I/O, UI events |
| **Use case**          | Immediate follow-up after sync code            | Deferred tasks, timers, I/O             |
| **Starvation risk**   | ✅ High (infinite microtasks block macrotasks) | ❌ Low (chỉ 1 task per loop)            |
| **Browser rendering** | Block rendering nếu quá nhiều                  | Không block (render giữa macrotasks)    |

#### **2. Browser vs Node.js Event Loop:**

**Browser Event Loop:**

- Simple: Microtasks → Render → 1 Macrotask.
- Có UI rendering phase.
- `requestAnimationFrame` runs trước render.

**Node.js Event Loop (6 Phases):**

1. **Timers**: `setTimeout`, `setInterval` callbacks.
2. **Pending callbacks**: I/O callbacks deferred to next loop.
3. **Idle, prepare**: Internal use only.
4. **Poll**: Retrieve new I/O events, execute I/O callbacks.
5. **Check**: `setImmediate` callbacks.
6. **Close callbacks**: Socket close events.

**Special in Node.js:**

- `process.nextTick()`: **Higher priority** than microtasks (chạy trước cả Promise.then).
- `setImmediate` vs `setTimeout(fn, 0)`: `setImmediate` chạy trong check phase → faster trong I/O callbacks.

### ✅ Best Practices (Thực hành tốt nhất - Chi tiết):

1. **Avoid blocking main thread với heavy computation**.

   - _Lý do_: Main thread block → UI freeze → bad UX.
   - _Solution_: Web Workers (true parallelism) hoặc chunking với `setTimeout`.

2. **Chunking long-running tasks**.

   - _Pattern_:

   ```javascript
   function processLargeArray(arr, chunkSize = 100) {
     let index = 0;
     function processChunk() {
       const end = Math.min(index + chunkSize, arr.length);
       for (; index < end; index++) {
         // Process arr[index]
       }
       if (index < arr.length) {
         setTimeout(processChunk, 0); // Yield to browser
       }
     }
     processChunk();
   }
   ```

3. **Dùng `queueMicrotask()` thay vì `Promise.resolve().then()`**.

   - _Lý do_: `queueMicrotask` direct API, ít overhead hơn (không tạo Promise object).
   - _When_: Khi cần schedule immediate follow-up task sau sync code.

4. **Cleanup timers và intervals**.

   - _Pattern_: Save timer ID → `clearTimeout(id)`, `clearInterval(id)` khi done.
   - _Lý do_: Memory leaks, callbacks chạy sau khi component unmount.

5. **RequestAnimationFrame cho animations**.

   - _Lý do_: Sync với browser repaint cycle (60fps) → smoother animations.
   - _Not for_: Logic code (chỉ cho visual updates).

6. **Avoid infinite microtask loops**.

   - _Pattern_: Đặt limit hoặc convert sang macrotask sau N iterations.

7. **Understanding `setTimeout(fn, 0)` behavior**.
   - _Not instant_: Vẫn phải chờ: 1) Call Stack empty, 2) ALL microtasks done, 3) Then execute.
   - _Min delay_: Browser có min delay ~4ms (HTML5 spec).

### ❌ Common Mistakes (Lỗi thường gặp - Chi tiết):

1. **Microtask starvation (Làm đói macrotask/UI)**.

   - ❌ **Sai**: Recursive Promise không có điểm dừng.

   ```javascript
   function infiniteMicrotask() {
     Promise.resolve().then(infiniteMicrotask); // Infinite loop
   }
   infiniteMicrotask(); // UI freeze, macrotasks never run
   ```

   - ✅ **Đúng**: Limit iterations hoặc convert sang macrotask.

2. **Nghĩ `setTimeout(fn, 0)` execute ngay lập tức**.

   - ❌ **Sai**: `setTimeout(fn, 0)` → instant.
   - ✅ **Đúng**: Defer to macrotask queue → wait for microtasks.

3. **Race conditions với async callbacks**.

   - ❌ **Sai**: Assume callbacks execute theo thứ tự gọi API.
   - ✅ **Đúng**: APIs complete theo network speed, không phải call order → cần tracking (request IDs).

4. **Không hiểu `setInterval` behavior**.

   - ❌ **Sai**: Assume interval chạy chính xác mỗi Nms.
   - ✅ **Đúng**: Interval có thể drift (trôi) nếu callback execution time > interval time.
   - _Better_: Recursive `setTimeout` với calculated delay.

5. **Memory leaks với timers/listeners**.

   - ❌ **Sai**: `setInterval(fn, 1000)` mà không clear → callback run forever.
   - ✅ **Đúng**: Save ID → `clearInterval(id)` trong cleanup (vd: React useEffect cleanup).

6. **Blocking Event Loop trong Node.js**.
   - ❌ **Sai**: Sync file I/O (`fs.readFileSync`) trong production.
   - ✅ **Đúng**: Async I/O (`fs.readFile`, `fs.promises.readFile`).

### 🔬 Deep Dive Insights (Kiến thức chuyên sâu):

#### **1. Render Timing & `requestAnimationFrame`:**

**Browser Rendering Pipeline:**

```
Microtasks → requestAnimationFrame → Layout → Paint → Composite → Macrotask
```

**RequestAnimationFrame (rAF):**

- Chạy **trước** render step (optimal cho animations).
- Browser automatically throttle to screen refresh rate (usually 60fps).
- **Benefits**: Smooth animations, battery-friendly (paused when tab inactive).

**Comparison với setTimeout:**

- `setTimeout(fn, 16)`: Không sync với repaint → may miss frames → janky.
- `requestAnimationFrame(fn)`: Sync với repaint → smooth 60fps.

#### **2. V8 Engine Optimization - Inline Caching:**

**Event Loop không phải ảo:**

- V8 (Chrome) và SpiderMonkey (Firefox) implement Event Loop trong C++.
- Call Stack, Task Queues = actual data structures (stack, queue).
- Microtask checkpoint: After every function call, check microtask queue.

#### **3. Node.js `process.nextTick()` vs Microtasks:**

**Priority Order trong Node.js:**

```
process.nextTick > Microtasks (Promise.then) > Macrotasks
```

**Why `nextTick` exists:**

- Allow executing code **immediately after current operation** before I/O.
- Use case: Emit events after constructor completes.

**Warning:**

- `process.nextTick` có thể starve I/O → dùng cẩn thận.
- Prefer `queueMicrotask` nếu không cần highest priority.

#### **4. React's Batching & Event Loop:**

**React 17 (Legacy):**

- Batch updates chỉ trong React event handlers (onClick, onChange).
- Không batch trong `setTimeout`, `Promise.then` → multiple renders.

**React 18+ (Automatic Batching):**

- Batch updates trong **TẤT CẢ** contexts (setTimeout, Promise, native events).
- Mechanism: Schedule updates trong microtask queue → flush together.

#### **5. Memory Leaks & Event Loop:**

**Common Patterns:**

1. **Timers not cleared**: `setInterval` → callback references objects → objects không GC.
2. **Event listeners**: DOM listeners → giữ reference đến handlers/closures.
3. **Circular references**: Old IE issue (modern GC handle được).

**Detection:**

- Chrome DevTools → Performance tab → record → check "Main thread" for long tasks.
- Memory tab → Heap snapshot → compare before/after → find retained objects.

#### **6. Web Workers - True Parallelism:**

**Event Loop Limitations:**

- Single-threaded → CPU-intensive tasks block UI.

**Web Workers Solution:**

- Separate thread với own Event Loop.
- Communication: `postMessage` (serialize data → no shared memory issues).
- **Use case**: Image processing, data parsing, complex calculations.

**Limitations:**

- No DOM access (chạy trong separate context).
- Overhead: Worker creation + message passing cost.

---

> **💡 Tổng hợp**: JavaScript = single-threaded với Event Loop | Call Stack (sync code) → Microtask Queue (ALL - Promise.then, queueMicrotask) → UI Render (browser only, 60fps) → Macrotask Queue (ONE - setTimeout, I/O) | Browser Event Loop simple vs Node.js 6 phases | RequestAnimationFrame chạy trước render | `setTimeout(fn, 0)` không instant (defer to macrotask) | Web Workers cho true parallelism | Avoid microtask starvation

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

| Thao Tác    | Kích Hoạt                        | Chi Phí    | Ví Dụ                                             |
| ----------- | -------------------------------- | ---------- | ------------------------------------------------- |
| **Paint**   | Render lần đầu                   | Trung bình | Tải trang lần đầu                                 |
| **Repaint** | Thay đổi hình ảnh (không layout) | Thấp       | `color`, `background`, `visibility`               |
| **Reflow**  | Thay đổi bố cục                  | **Cao**    | `width`, `height`, `margin`, `padding`, `display` |

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

## Q20: Xử Lý Caching - HTTP Caching & Browser Cache Strategies

### 🎯 Trả Lời Ngắn Gọn (2-3 phút):

**"HTTP caching giảm thiểu số lượng requests xuống server bằng Cache-Control headers và ETag validation. Browser có hierarchy cache: Memory Cache (nhanh nhất nhưng mất khi đóng tab) → Disk Cache (lưu trên ổ cứng) → Service Worker Cache (hỗ trợ offline) → Network. Service Worker strategies: Cache First (cho static assets), Network First (cho dynamic data), Stale-While-Revalidate (cân bằng giữa tốc độ và độ mới)."**

### 📦 Phân Loại Cache:

**3 Tầng Cache trong Browser:**
- **Memory Cache** (Bộ nhớ RAM): Nhanh nhất, mất khi đóng tab, dùng cho session hiện tại
- **Disk Cache** (Ổ cứng): Persistent (giữ lại sau khi đóng browser), chậm hơn Memory nhưng lâu dài
- **Service Worker Cache**: Lập trình được, hỗ trợ offline, kiểm soát hoàn toàn chiến lược cache

### 🔑 HTTP Cache Headers (Quan Trọng):

| Header        | Mục Đích                              | Ví Dụ                       |
| ------------- | ------------------------------------- | --------------------------- |
| Cache-Control | Chỉ thị caching chính (ưu tiên cao)  | `max-age=3600, public`      |
| ETag          | Token kiểm tra nội dung có thay đổi | `"abc123"` (content hash)   |
| Last-Modified | Timestamp cập nhật lần cuối         | `Thu, 01 Jan 2024 00:00:00` |
| Expires       | Ngày hết hạn (cũ, ít dùng)          | `Thu, 01 Jan 2025 00:00:00` |

**Cache-Control directives (Chỉ thị chi tiết):**

- `max-age=3600`: Cache trong 1 giờ (3600 giây) - thời gian tối đa giữ cache
- `public`: Cho phép cache ở browser VÀ CDN (dùng cho public resources)
- `private`: Chỉ cache ở browser, không cache ở CDN (dữ liệu cá nhân user)
- `no-cache`: Phải revalidate với server trước khi dùng (server trả 304 nếu unchanged)
- `no-store`: KHÔNG BAO GIỜ cache (dữ liệu nhạy cảm: passwords, payment info)
- `immutable`: Không bao giờ revalidate (file có version hash như `app.abc123.js`)

### ♻️ Service Worker Caching Strategies (Chiến Lược Cache):

1. **Cache First** (Ưu tiên Cache trước):
   - Kiểm tra cache → trả về nếu có → fetch network nếu không có
   - **Dùng cho**: Static assets (fonts, images, CSS/JS có version)
   - **Ưu điểm**: Siêu nhanh, tiết kiệm bandwidth
   - **Nhược điểm**: Có thể serve nội dung cũ nếu không có versioning

2. **Network First** (Ưu tiên Network trước):
   - Fetch network → trả về data mới → fallback to cache nếu network fail
   - **Dùng cho**: Dynamic data (APIs, user-generated content)
   - **Ưu điểm**: Luôn có data mới nhất
   - **Nhược điểm**: Chậm nếu network chậm

3. **Stale-While-Revalidate** (Trả cache cũ + update background):
   - Trả cache ngay lập tức + fetch network ở background → update cache
   - **Dùng cho**: News feeds, social media, data thay đổi vừa phải
   - **Ưu điểm**: Nhanh + có data mới (best of both worlds)
   - **Nhược điểm**: User có thể thấy data cũ ngắn

4. **Network Only**: Luôn fetch network, không cache (analytics, real-time data)
5. **Cache Only**: Chỉ serve từ cache (PWA app shell đã download)

### ⚠️ Lỗi Thường Gặp (Common Mistakes):

- **Cache static assets không có version hash** → serve nội dung cũ cho users
  - ✅ **Giải pháp**: Dùng `app.abc123.js` content hash (webpack/vite tự động)
- **Cache quá nhiều sensitive data** (passwords, payment) → rủi ro bảo mật
  - ✅ **Giải pháp**: Dùng `Cache-Control: no-store` cho sensitive data
- **Không purge CDN cache khi deploy** → users thấy version cũ
  - ✅ **Giải pháp**: Invalidate CDN cache sau mỗi deploy (CloudFlare, Vercel)
- **Không implement ETag/Last-Modified** → lãng phí bandwidth
  - ✅ **Giải pháp**: Server trả 304 Not Modified nếu content unchanged

### 💡 Kiến Thức Senior (Deep Dive):

- **Versioning Strategy**: Content hash filenames → set `immutable` + long `max-age` (1 năm)
  - File `app.abc123.js` khác với `app.def456.js` → browser cache riêng biệt
- **HTML caching**: Luôn dùng `no-cache` + ETag → revalidate nhưng nhanh với 304
  - HTML thường thay đổi → phải kiểm tra server nhưng 304 response rất nhanh
- **Cache-Control > Expires**: Modern browsers ưu tiên `Cache-Control` (chuẩn HTTP/1.1)
- **Performance impact**: Caching đúng cách → 50-70% faster repeat visits, giảm TTFB (Time To First Byte)
- **Cache Busting**: Khi update static files → change filename hash → force browser download mới

---

## Q21: JavaScript Proxy - Metaprogramming & Reactivity (Lập Trình Meta)

### 🎯 Trả Lời Ngắn Gọn (2-3 phút):

**"Proxy chặn (intercept) các thao tác trên objects (get, set, delete, has...) thông qua traps (handlers). Use cases chính: Validation dữ liệu, Reactivity (Vue 3), Logging/Debugging, Access Control. Performance overhead khoảng ~10-20% chậm hơn direct access nhưng đổi lại là tính linh hoạt cao."**

### 🔑 Khái Niệm Cốt Lõi:

**Cú Pháp Proxy:**

- `new Proxy(target, handler)` - target = object gốc, handler = object chứa các traps
- **13 traps** (bẫy): `get`, `set`, `deleteProperty`, `has`, `apply`, `construct`, `getPrototypeOf`, v.v.
- **Trap = handler function** được gọi khi thao tác tương ứng xảy ra

**6 Use Cases Phổ Biến:**

1. **Validation (Xác thực dữ liệu)**:
   - Validate giá trị trước khi set vào property
   - Ví dụ: Kiểm tra `age` phải là số dương
   
2. **Reactivity (Tính phản ứng)**:
   - Tự động trigger UI updates khi data thay đổi
   - **Vue 3 reactivity system** dùng Proxy (thay thế `Object.defineProperty` của Vue 2)
   
3. **Logging/Debugging**:
   - Track property access (ai đọc property nào, khi nào)
   - Log mutations (thay đổi dữ liệu) cho debugging
   
4. **Access Control (Kiểm soát truy cập)**:
   - Restrict access to private properties (properties bắt đầu bằng `_`)
   - Throw error nếu access unauthorized
   
5. **Default Values (Giá trị mặc định)**:
   - Return defaults cho undefined properties thay vì `undefined`
   - Ví dụ: `obj.unknownKey` → trả về `null` thay vì `undefined`
   
6. **Type Coercion (Ép kiểu tự động)**:
   - Auto-convert types (strings → numbers, dates, etc.)

### ⚠️ Lỗi Thường Gặp:

- **`this` binding issues trong traps** → Dùng `Reflect` API để giữ correct `this`
  - Trap handler có thể làm mất context của `this`
- **Proxy deeply nested objects** → Cần recursive proxying cho mọi level
  - Chỉ proxy level đầu tiên không đủ, phải proxy các nested objects
- **Performance**: Proxy chậm hơn plain objects (~10-20%) → tránh dùng trong hot paths (loops, render)
- **Non-configurable properties** không thể proxy → TypeError
  - Properties của built-in objects (như Array prototype) không proxy được

### 💡 Kiến Thức Senior:

- **Reflect API**: API đồng hành với Proxy, proper `this` binding, code clean hơn
  - `Reflect.get(target, prop, receiver)` thay vì `target[prop]`
- **Vue 3 reactivity**: `reactive()` = Proxy-based → track dependencies tự động
  - Khác Vue 2: `Object.defineProperty` chỉ track properties có sẵn, Proxy track dynamic
- **MobX**: Dùng Proxy cho observable state (automatic dependency tracking)
- **Revocable Proxy**: `Proxy.revocable()` → disable proxy sau này (security, cleanup khi không dùng nữa)
  - Return `{ proxy, revoke }` → gọi `revoke()` để disable proxy

---

## Q22: JavaScript Classes - OOP Syntax & Patterns (Lập Trình Hướng Đối Tượng)

### 🎯 Trả Lời Ngắn Gọn (2-3 phút):

**"ES6 Classes = syntactic sugar trên prototypes (bản chất vẫn là prototype-based). Features: constructor (khởi tạo), methods (trên prototype), static methods (class-level), inheritance (`extends`/`super`), private fields (`#field` - ES2022). Bên trong vẫn là prototype-based, không phải class-based như Java/C++."**

### 🔑 Tính Năng Chính (Key Features):

- **Constructor**: `constructor(props) {}` - Hàm khởi tạo instance, tự động chạy khi `new Class()`
- **Methods**: `method() {}` - Methods được thêm vào prototype → share across instances (tiết kiệm memory)
- **Static Methods**: `static method() {}` - Methods gọi trên class, không phải instance (ví dụ: `Array.from()`)
- **Inheritance (Kế thừa)**: `extends` keyword, `super()` gọi constructor của parent
- **Private Fields**: `#privateField` (ES2022) - Truly private (không access được ngoài class)
- **Getters/Setters**: `get prop()`, `set prop(value)` - Computed properties với validation

### 🔄 So Sánh Classes vs Prototypes:

**ES6 Class (Modern):**
- Syntax clean, dễ đọc hơn
- Built-in inheritance với `extends`
- Private fields với `#` syntax

**ES5 Prototypes (Legacy):**
- Function constructors + `prototype`
- Manual inheritance phức tạp
- No true private (dùng closures)

### ⚠️ Lỗi Thường Gặp:

- **Quên `super()` trong child constructor** → ReferenceError
  - `super()` phải gọi ĐẦU TIÊN trong child constructor trước khi dùng `this`
- **Dùng arrow functions làm methods** → mất prototype, tăng memory
  - Arrow function được bind vào instance → mỗi instance có copy riêng (waste memory)
  - ✅ **Giải pháp**: Dùng regular method `method() {}`
- **So sánh classes với `===`** → always false (different references)
  - Classes là references, không phải primitive values
- **Access private fields outside class** → SyntaxError
  - Private fields với `#` chỉ access được trong class body

### 💡 Kiến Thức Senior:

- **Classes vs Factory Functions**:
  - Classes = OOP paradigm, dùng `new` keyword
  - Factories = functional approach, return objects, dùng closures cho privacy
  - Factories linh hoạt hơn nhưng Classes performance tốt hơn
- **Composition over Inheritance** (nguyên tắc thiết kế):
  - Prefer mixins, composition patterns (React Hooks pattern)
  - Deep inheritance hierarchies → fragile, hard to maintain
- **Private fields**: `#` syntax tốt hơn WeakMap/Symbol conventions (true privacy tại engine level)
- **Performance**: Classes optimize tốt trong modern engines (V8 hidden classes)
  - V8 tạo hidden classes để optimize property access → fast như C++ objects

---

## Q23: Generator Functions & Async Generators (Hàm Sinh & Async Iteration)

### 🎯 Trả Lời Ngắn Gọn (2-3 phút):

**"Generators = hàm có thể tạm dừng (pausable) với `yield` keyword. Syntax: `function*` (có dấu sao). Return iterator object. Use cases: lazy evaluation (tiết kiệm memory), async iteration (`for await...of`), state machines (máy trạng thái), infinite sequences (dãy vô hạn). Async generators = `async function*` cho async iteration với Promises."**

### 🔑 Khái Niệm Cốt Lõi:

**Generator Functions (Hàm Sinh):**

- `function* gen() { yield 1; yield 2; }` - Tạo iterator (không chạy ngay)
- `yield` tạm dừng (pause) execution, `next()` tiếp tục (resume)
- `return` kết thúc generator, `throw` gửi error vào generator
- **Lazy execution**: Code không chạy cho đến khi gọi `next()`

**4 Use Cases Chính:**

1. **Lazy Evaluation (Đánh giá lười)**:
   - Generate values theo nhu cầu → tiết kiệm memory
   - Ví dụ: Đọc file lớn từng chunk thay vì load hết vào RAM
   
2. **Infinite Sequences (Dãy vô hạn)**:
   - `function* fibonacci()` - không có điều kiện dừng
   - Tạo số Fibonacci vô hạn mà không crash memory
   
3. **State Machines (Máy trạng thái)**:
   - Maintain state giữa các lần yield (không cần biến global)
   - Ví dụ: Traffic light (red → yellow → green → red...)
   
4. **Async Iteration**:
   - `for await (const item of asyncGen())` - iterate async values
   - Stream processing: Xử lý data từng phần khi data đến

**Async Generators (Async Iteration):**

- `async function* asyncGen()` - Yield Promises
- Combine async/await + generators → powerful for streams
- **Use case**: Stream processing, pagination API (load từng trang), real-time data

### ⚠️ Lỗi Thường Gặp:

- **Quên `*` trong khai báo `function*`** → thành regular function (không có yield)
- **Không iterate generator** → function returns iterator object, không phải values
  - Phải gọi `.next()` hoặc dùng `for...of` để lấy values
- **Generator trong loop không cleanup** → memory leak
  - Phải `.return()` để cleanup generator nếu break sớm

### 💡 Kiến Thức Senior:

- **Generators vs Async/Await**:
  - Generators = **pull-based** (consumer controls khi nào lấy value)
  - Promises = **push-based** (producer push values khi ready)
- **Redux-Saga**: Dùng generators cho side effects management
  - `yield call(api)`, `yield put(action)` → testable, pausable side effects
- **Performance**: Generators tiết kiệm memory (lazy evaluation) nhưng có overhead nhỏ mỗi `yield` (~5-10%)
- **`yield*` delegation**: Delegate cho generator khác/iterable
  - `yield* anotherGenerator()` → yield tất cả values từ generator khác

---

## Q24: Advanced Array & Object Methods - Immutability (Bất Biến) & Modern APIs

### 🎯 Trả Lời Ngắn Gọn (2-3 phút):

**"Array methods: `map/filter/reduce` (functional, immutable - không thay đổi array gốc), `flat/flatMap` (flatten nested arrays), `find/findIndex` (tìm kiếm), `some/every` (test điều kiện). Object methods: `Object.keys/values/entries` (iterate object), `Object.assign` (shallow copy), `Object.freeze` (immutable). Spread operator (`...`) chỉ shallow copy (1 level)."**

### 🔑 Advanced Array Methods (Modern):

**Arrays (Mảng):**

- `Array.from()`: Convert iterable/array-like object → array thật
  - Ví dụ: `Array.from('hello')` → `['h', 'e', 'l', 'l', 'o']`
- `Array.of()`: Tạo array từ arguments (tốt hơn `new Array()`)
  - `Array.of(7)` → `[7]` (khác `new Array(7)` → array 7 empty slots)
- `.flatMap()`: Map + flatten trong 1 pass (hiệu quả hơn `.map().flat()`)
  - Ví dụ: `[[1,2],[3,4]].flatMap(x => x)` → `[1,2,3,4]`
- `.toSorted()` (ES2023): Sort IMMUTABLY (return array mới, không thay đổi gốc)
  - Khác `.sort()` mutate array gốc

**Objects (Đối tượng):**

- `Object.fromEntries()`: Convert entries → object (ngược lại của `.entries()`)
  - `Object.fromEntries([['a',1],['b',2]])` → `{a:1, b:2}`
- `Object.hasOwn()`: Tốt hơn `.hasOwnProperty()` (tránh prototype pollution)
  - Safe hơn khi object không có `.hasOwnProperty` method
- `Object.freeze()`: Immutable (chỉ top-level, nested objects vẫn mutable)
  - Không thể thêm/xóa/sửa properties
- `Object.seal()`: Ngăn thêm/xóa properties, cho phép modify values

### 🔄 Immutability Patterns (Patterns Bất Biến):

**Shallow Copy (Copy nông - 1 level):**
- Spread operator: `{...obj}`, `[...arr]`
- `Object.assign({}, obj)`
- ⚠️ **Chú ý**: Nested objects vẫn share reference

**Deep Copy (Copy sâu - all levels):**
- `structuredClone(obj)` (ES2022 - native, handle Date/RegExp/circular refs)
- `JSON.parse(JSON.stringify(obj))` (legacy, mất functions/undefined/Date)
- Immer library (simplify immutable updates)

### ⚠️ Lỗi Thường Gặp:

- **Mutate arrays với `.sort()`, `.reverse()`** → thay đổi array gốc
  - ✅ **Giải pháp**: Dùng `.toSorted()`, `.toReversed()` (ES2023) hoặc `[...arr].sort()`
- **Shallow copy nested objects** (`{...obj}`) → nested objects vẫn shared
  - Ví dụ: `{...user}` copy user nhưng `user.address` vẫn share reference
  - ✅ **Giải pháp**: `structuredClone(obj)` hoặc Immer
- **`Object.freeze()` chỉ shallow** → nested objects vẫn mutable
  - Phải recursive freeze nếu muốn deep immutable

### 💡 Kiến Thức Senior:

- **Immutable updates**: Immer library cho deep immutable updates (đơn giản hơn spread hell)
  - Immer dùng Proxy để track changes → produce new immutable state
- **Performance**: Functional methods chậm hơn `for` loops (~10-20%) nhưng readable hơn (acceptable trade-off)
- **`structuredClone()`**: Native deep clone (ES2022) - handles Date, RegExp, circular refs, Map, Set
  - Không handle functions (functions sẽ bị bỏ qua)
- **Method chaining**: `.filter().map().reduce()` tiện nhưng nhiều iterations
  - Mỗi method tạo array mới → có thể optimize bằng single loop nếu cần performance

---

## Q25: React Deep Dive - Lifecycle, Performance, Architecture (Kiến Trúc React Chuyên Sâu)

### 🎯 Trả Lời Ngắn Gọn (3-4 phút):

**"React Hooks thay thế Class lifecycle: `useEffect` (componentDidMount/Update/Unmount - quản lý side effects), `useMemo` (memoization - cache tính toán nặng), `useCallback` (stable function reference - tránh re-render con). Virtual DOM + Reconciliation (đối chiếu) = cập nhật DOM tối thiểu. Fiber architecture = rendering có thể ngắt quãng (interruptible). Optimization: `React.memo`, lazy loading, code splitting."**

### 🪝 Essential Hooks (6 Hooks Quan Trọng Nhất):

1. **useState** (Quản lý state cục bộ):
   - State management trong functional components
   - Functional updates: `setState(prev => prev + 1)` (dùng prev state)
   
2. **useEffect** (Side effects):
   - Side effects: API calls, subscriptions, DOM manipulation
   - Cleanup function ngăn memory leaks (return function chạy khi unmount)
   - Dependency array `[deps]` controls khi nào re-run
   
3. **useRef** (Mutable value không trigger re-render):
   - Mutable value không gây re-render khi thay đổi
   - DOM access: `ref.current` → DOM element
   - Store previous values (compare old vs new)
   
4. **useMemo** (Cache expensive computations):
   - Cache kết quả tính toán nặng
   - Chỉ recompute khi dependencies change
   - ⚠️ Chỉ dùng cho computations nặng (>50ms)
   
5. **useCallback** (Cache function reference):
   - Cache function reference → prevent child re-renders
   - Dùng khi pass callbacks cho child components được memoized
   
6. **useReducer** (Complex state logic):
   - Alternative to useState cho state phức tạp (nhiều sub-values)
   - Pattern giống Redux: `(state, action) => newState`

### 🔄 Lifecycle Mapping (Class → Hooks):

- **componentDidMount** (1 lần sau mount): `useEffect(() => {}, [])`
- **componentDidUpdate** (mỗi lần update): `useEffect(() => {}, [deps])`
- **componentWillUnmount** (cleanup trước unmount): `useEffect(() => { return cleanup }, [])`
- **shouldComponentUpdate** (skip re-render): `React.memo()` + `useMemo/useCallback`

### 🚀 Performance Optimization (6 Kỹ Thuật Chính):

1. **React.memo()** (Memoize component):
   - Shallow compare props → skip re-render nếu props unchanged
   - Dùng cho expensive components, list items
   
2. **useMemo()** (Cache calculations):
   - Cache kết quả expensive calculations (filtering lớn, computations phức tạp)
   
3. **useCallback()** (Cache functions):
   - Stable function references cho memoized child components
   
4. **Code Splitting** (Lazy loading):
   - `React.lazy(() => import('./Page'))` + Suspense
   - Route-based: Mỗi route 1 chunk riêng
   - Component-based: Split heavy components (charts, editors)
   
5. **Virtualization** (Render visible items only):
   - `react-window` / `react-virtualized` cho long lists
   - 1000 items → render ~30 visible → 97% faster
   
6. **Avoid inline functions/objects**:
   - Inline functions/objects tạo new references mỗi render → children re-render
   - ✅ Extract to constants/variables outside render

### ⚠️ Lỗi Thường Gặp:

- **Missing dependencies trong `useEffect`** → stale closures (đọc giá trị cũ), bugs
  - ESLint plugin `react-hooks/exhaustive-deps` cảnh báo
- **Infinite loops**: `useEffect` no deps + `setState` inside → re-render vô hạn
  - ✅ Thêm dependencies array hoặc conditional setState
- **Overuse `useMemo/useCallback`** → premature optimization, tăng complexity
  - Chỉ dùng khi measure thấy bottleneck (React Profiler)
- **Mutate state directly**: `state.value = 1` → React không detect
  - ✅ Luôn dùng `setState` để React track changes

### 💡 Kiến Thức Senior:

- **React 18 features**:
  - Concurrent rendering (rendering có thể ngắt quãng)
  - `useTransition` (mark low-priority updates → UI stays responsive)
  - `useDeferredValue` (debounce built-in cho search)
  - Automatic batching (batch multiple setState calls)
- **useLayoutEffect**: Runs synchronously AFTER render, BEFORE paint
  - Dùng cho DOM measurements (read layout), ngăn flicker
- **StrictMode**: Double-invokes effects trong dev mode
  - Catch side effects không clean (help phát hiện bugs sớm)
- **Profiler**: `<Profiler>` component + DevTools
  - Measure render performance, identify slow components
- **Keys trong lists**: Stable keys giúp reconciliation
  - NEVER dùng index cho dynamic lists (items add/remove/reorder)

---

## Q26: Next.js - React Framework for Production (Framework React Cho Sản Phẩm)

### 🎯 Trả Lời Ngắn Gọn (3-4 phút):

**"Next.js = React meta-framework với file-system routing (routing dựa trên cấu trúc thư mục), SSR/SSG/ISR rendering strategies (nhiều chiến lược render), API routes (serverless functions - backend ngay trong project), Image Optimization component (tối ưu ảnh tự động), automatic code splitting (tách code tự động). App Router (v13+) = React Server Components (zero JS), nested layouts (layouts lồng nhau), streaming SSR (render từng phần)."**

### 🔑 4 Rendering Strategies (Chiến Lược Render):

1. **SSR (Server-Side Rendering - Render phía server)**:
   - `getServerSideProps` - Fetch data mỗi request
   - **Dùng cho**: Dynamic content (user-specific data, real-time)
   - **Ưu**: SEO tốt, fresh data, **Nhược**: Chậm (wait server)
   
2. **SSG (Static Site Generation - Sinh tĩnh)**:
   - `getStaticProps` - Build-time generation (build 1 lần)
   - **Dùng cho**: Blog, documentation, marketing pages
   - **Ưu**: Blazing fast (serve static HTML), cacheable, **Nhược**: Data có thể cũ
   
3. **ISR (Incremental Static Regeneration - Regenerate dần dần)**:
   - `revalidate` option - Regenerate pages ở background sau N giây
   - **Dùng cho**: E-commerce products, news (balance giữa static + dynamic)
   - **Ưu**: Fast như SSG + fresh data như SSR
   
4. **CSR (Client-Side Rendering - Render phía client)**:
   - `useEffect` + `fetch` - Traditional SPA approach
   - **Dùng cho**: Admin dashboards, private pages (không cần SEO)

### 🚀 Key Features (Tính Năng Chính):

- **File-System Routing** (Routing dựa trên files):
  - `pages/about.js` → `/about` route
  - App Router: `app/about/page.js` → `/about`
  - Nested routes: `app/blog/[slug]/page.js` → `/blog/:slug`
  
- **API Routes** (Backend trong frontend project):
  - `pages/api/*.js` → serverless functions
  - Ví dụ: `pages/api/users.js` → `/api/users` endpoint
  
- **Image Optimization** (Tối ưu ảnh tự động):
  - `<Image>` component: Auto WebP/AVIF, lazy loading, responsive sizes
  - Resize on-demand, optimize quality
  
- **Code Splitting** (Tách code tự động):
  - Mỗi page = 1 chunk riêng → load on-demand
  - Shared chunks optimization (vendor, common code)
  
- **Zero Config** (Không cần config):
  - Fast Refresh (HMR - hot module reload)
  - TypeScript support built-in
  - CSS Modules out-of-box

### 📱 App Router - Next.js 13+ (Modern Architecture):

- **React Server Components** (RSC):
  - Server components = ZERO JS bundle gửi client
  - Chỉ HTML được gửi → faster, smaller bundle
  
- **Nested Layouts** (Layouts lồng nhau):
  - Shared layouts persist across page navigations
  - Layout không re-render khi navigate
  
- **Streaming SSR** (Progressive rendering):
  - Render từng phần với Suspense boundaries
  - User thấy content sớm hơn (không chờ toàn bộ page)
  
- **Server Actions** (Call server từ client):
  - Call server functions trực tiếp từ client (form actions)
  - Không cần viết API routes

### ⚠️ Lỗi Thường Gặp:

- **Fetch data trong component (CSR) khi cần SSR** → slow, no SEO
  - ✅ Dùng `getServerSideProps` hoặc Server Components
- **`getStaticProps` cho data thay đổi thường xuyên** → stale content
  - ✅ Dùng ISR với `revalidate`
- **Không dùng `<Image>` component** → miss optimizations
  - Regular `<img>` không có lazy load, format optimization
- **Mix Pages + App Router** → confusion
  - Stick to one (App Router là modern choice)

### 💡 Kiến Thức Senior:

- **Middleware** (Edge functions):
  - Chạy TRƯỚC request đến page (authentication, redirects, A/B testing)
  - Deploy to edge (CloudFlare, Vercel Edge) → ultra fast
- **Parallel Routes**: Render multiple pages simultaneously trong same layout
  - Ví dụ: Dashboard with sidebar + main content (independent loading)
- **Intercepting Routes**: Modal routes không navigation
  - Ví dụ: Photo lightbox (Instagram-style)
- **Performance**: Next.js optimize bundle tự động (~30% smaller than CRA)

---

## Q27: CommonJS vs ES Modules (ESM) & Bundling Deep Dive (Module Systems So Sánh)

### 🎯 Trả Lời Ngắn Gọn (3 phút):

**"CommonJS (`require`/`module.exports`) = synchronous (đồng bộ), Node.js legacy (cũ). ES Modules (`import`/`export`) = asynchronous (bất đồng bộ), static analysis (phân tích tĩnh) → cho phép tree-shaking. Bundlers: Webpack (config nhiều, mature), Rollup (ESM-first, cho libraries), Vite (dev speed nhanh, dùng esbuild). Tree-shaking loại bỏ unused code (dead code elimination - giảm 20-40% bundle)."**

### 📊 CommonJS vs ESM (So Sánh Chi Tiết):

| Aspect           | CommonJS                     | ES Modules                           |
| ---------------- | ---------------------------- | ------------------------------------ |
| **Syntax**       | `require()`/`module.exports` | `import`/`export`                    |
| **Loading**      | Synchronous (đồng bộ)        | Asynchronous (bất đồng bộ)           |
| **Analysis**     | Runtime (dynamic - lúc chạy) | **Static** (compile-time - lúc build) |
| **Tree-shaking** | ❌ Khó (dynamic requires)     | ✅ Có (biết dependencies trước)      |
| **Browser**      | ❌ Không (cần bundler)        | ✅ Native (`<script type="module">`) |
| **Ecosystem**    | Node.js legacy (cũ)          | Modern standard (chuẩn hiện đại)     |

### 🔑 Bundling Concepts (Khái Niệm Đóng Gói):

**Tree-Shaking (Loại Bỏ Code Không Dùng):**

- Static `import`/`export` → bundler biết dependencies lúc build time
- Loại bỏ unused exports → bundles nhỏ hơn (~20-40% reduction)
- **Yêu cầu ES Modules** (CommonJS không tree-shake được vì dynamic)
- **Ví dụ**: `import { add } from 'math'` → chỉ bundle hàm `add`, bỏ hàm khác

**Code Splitting (Tách Code Thành Chunks):**

- Split bundle thành chunks (vendor, app code, routes)
- Lazy load on-demand (`import()` dynamic imports)
- **Ưu điểm**: Parallel loading, faster initial load (load ít hơn lúc đầu)
- **Chiến lược**: Route-based (mỗi route 1 chunk), vendor splitting (React, lodash riêng)

### ⚠️ Lỗi Thường Gặp:

- **Mix CommonJS + ESM trong same project** → issues (dual package hazard)
  - ✅ Chọn 1 trong 2, hoặc dùng `.cjs`/`.mjs` extensions rõ ràng
- **Default imports từ CommonJS modules** → undefined behaviors
  - CommonJS không có true default export như ESM
- **Không enable tree-shaking** → ship unused code (bundle bloat)
  - ✅ Check bundler config, set `sideEffects: false` trong package.json
- **Large node_modules bundles** → không biết gì được bundle
  - ✅ Dùng `webpack-bundle-analyzer` để visualize

### 💡 Kiến Thức Senior:

- **Package.json "type"**: `"type": "module"` → Node.js treat `.js` files as ESM
  - Mặc định Node.js treat `.js` là CommonJS
- **Dual packages** (Ship cả 2 formats):
  - Ship both CommonJS + ESM (`.cjs` + `.mjs` extensions)
  - `package.json` "exports" field → specify entry points cho từng format
- **Webpack Module Federation**: Share modules at runtime (microfrontends)
  - Multiple apps share code dynamically (không cần rebuild)
- **Barrel exports** (`index.js` re-exports):
  - Có thể prevent tree-shaking (bundler không biết gì dùng)
  - ✅ Import directly từ modules thay vì barrel: `'lodash/get'` > `'lodash'`

---

## Q28: Cancellation, Concurrency & Retry - Advanced Async Patterns (Patterns Bất Đồng Bộ Nâng Cao)

### 🎯 Trả Lời Ngắn Gọn (2-3 phút):

**"AbortController hủy fetch requests (native API). Concurrency control (kiểm soát đồng thời): `Promise.all` (parallel - chạy song song), sequential (tuần tự với for-await-of), `p-limit` library (giới hạn N requests đồng thời). Retry strategies (chiến lược thử lại): exponential backoff (`2^n * delay` - tăng gấp đôi delay), max attempts (giới hạn số lần thử), jitter (random offset tránh thundering herd)."**

### 🔑 Cancellation Patterns (Patterns Hủy Request):

**AbortController (Native API - built-in):**

- `const controller = new AbortController()` - Tạo controller
- `fetch(url, { signal: controller.signal })` - Pass signal vào fetch
- `controller.abort()` - Hủy request → throw `AbortError`
- **Use cases**:
  - Cancel requests khi component unmount (cleanup)
  - Cancel previous request khi search input thay đổi (debounce)
  - Timeout pattern (race với timeout promise)

### 🔄 Concurrency Patterns (Patterns Đồng Thời):

1. **Parallel Unlimited** (Song song không giới hạn):
   - `Promise.all([...])` - Tất cả requests cùng lúc
   - **Ưu**: Nhanh nhất, **Nhược**: Có thể overwhelm server, rate limit
   
2. **Sequential** (Tuần tự - từng cái một):
   - `for await (const item of items) { await process(item); }`
   - **Ưu**: An toàn (không quá tải server), **Nhược**: Chậm nhất
   
3. **Limited Concurrency** (Giới hạn đồng thời):
   - `p-limit` library - Tối đa N requests đồng thời
   - **Balance**: Speed + server load (ví dụ: 5 concurrent)
   - **Best practice**: Cho batch processing nhiều items
   
4. **Race** (Ai về trước thắng):
   - `Promise.race([...])` - First to complete wins
   - **Use case**: Timeout pattern (race với delay promise)

### ♻️ Retry Strategies (Chiến Lược Thử Lại):

**Exponential Backoff (Tăng thời gian chờ theo cấp số nhân):**

- Wait `2^attempt * baseDelay` ms giữa các lần retry
  - Attempt 1: 1s, Attempt 2: 2s, Attempt 3: 4s, Attempt 4: 8s...
- **Add jitter** (random offset 0-500ms) → prevent thundering herd problem
  - Nhiều clients cùng retry cùng lúc → overwhelm server
- **Max attempts limit** (3-5 retries typical) → ngăn infinite loop

**Khi Nào Retry:**
- Network errors (connection failed)
- 5xx server errors (server có vấn đề tạm thời)
- 429 Too Many Requests (rate limit → wait longer)

**Khi KHÔNG Retry:**
- 4xx client errors (400 Bad Request, 401 Unauthorized - lỗi logic)
- Business logic errors (validation failed)

### ⚠️ Lỗi Thường Gặp:

- **Quên abort requests khi cleanup** → memory leaks, unnecessary network traffic
  - ✅ Always abort trong useEffect cleanup function
- **Unlimited parallel requests** → overwhelm server, rate limit errors (429)
  - ✅ Dùng `p-limit` để limit concurrent (5-10 requests)
- **Retry without backoff** → hammer server repeatedly, get banned/blocked
  - ✅ Exponential backoff + jitter
- **No max retry limit** → infinite loops khi persistent failures
  - ✅ Set max 3-5 retries, sau đó throw error

### 💡 Kiến Thức Senior:

- **p-limit pattern**:
  ```
  const limit = pLimit(5); 
  await Promise.all(urls.map(url => limit(() => fetch(url))))
  ```
  - Limit 5 concurrent fetches, queue phần còn lại
- **p-retry library**: Exponential backoff built-in, customizable
- **Circuit Breaker pattern**: Stop calling failing services sau N failures
  - Prevent cascade failures (1 service fail → không kéo theo cả hệ thống)
  - Open circuit → reject fast → save resources
- **Request deduplication**: Same request in-flight → reuse Promise
  - React Query làm điều này automatically (1 query key = 1 request)

---

## Q29: Web Workers, Service Worker & PWA Basics

### 🎯 Trả Lời Ngắn Gọn:

**"Web Workers = background threads for CPU-intensive tasks (no DOM access). Service Workers = proxy between app and network, enable offline, caching, push notifications (PWA). Shared Workers = shared across tabs/windows."**

### 🔑 Worker Types:

**1. Web Workers (Dedicated):**

- Offload heavy computation to background thread (image processing, data parsing)
- `new Worker('worker.js')` - create worker
- `postMessage()` / `onmessage` - communication (structured clone, no shared memory)
- **Limitation**: No DOM, no `window`, separate global scope

**2. Service Workers (PWA Core):**

- Intercept network requests → cache responses, offline support
- Lifecycle: Install → Activate → Fetch → Terminate (event-driven)
- Caching strategies: Cache First, Network First, Stale-While-Revalidate
- **Features**: Offline, push notifications, background sync

**3. Shared Workers:**

- Shared across multiple tabs/windows (same origin)
- Use case: Shared WebSocket connection, shared state
- Less common, limited browser support

### 📱 PWA (Progressive Web App):

**Requirements:**

- HTTPS (Service Worker requirement)
- Manifest file (`manifest.json`) - app metadata, icons, theme
- Service Worker for offline support

**Benefits:**

- Install to home screen (app-like experience)
- Offline functionality (cached assets + data)
- Push notifications (re-engagement)
- Fast, reliable, engaging

### ⚠️ Common Mistakes:

- Heavy computation on main thread → UI freeze (move to Web Worker)
- Service Worker không update → users see stale app (implement update logic)
- Aggressive caching → users never see updates (balance cache duration)
- Debug Service Worker issues → use Chrome DevTools Application tab

### 💡 Senior Insights:

- **Workbox**: Google library for Service Worker strategies (simplify caching)
- **Comlink**: RPC library for Workers (call functions like local, handles serialization)
- **Shared Array Buffer**: Shared memory between threads (requires COOP/COEP headers)
- **Performance**: Workers have overhead (~50-100ms startup), use for tasks >100ms

---

## Q30: Browser Storage - LocalStorage, SessionStorage, Cookie & IndexedDB

### 🎯 Trả Lời Ngắn Gọn:

**"Browser storage: Cookie (4KB, sent to server), LocalStorage (5-10MB, persistent), SessionStorage (5-10MB, tab-scoped), IndexedDB (50MB+, async database). Security: NEVER store sensitive data in localStorage (XSS risk), use HttpOnly cookies for tokens."**

### 🔑 Storage Comparison:

| Criteria    | Cookie        | LocalStorage  | SessionStorage | IndexedDB           |
| ----------- | ------------- | ------------- | -------------- | ------------------- |
| **Size**    | 4KB           | 5-10MB        | 5-10MB         | 50MB-unlimited      |
| **Persist** | Expiry date   | Forever       | Tab close      | Forever             |
| **API**     | Sync (string) | Sync (string) | Sync (string)  | **Async** (objects) |
| **Server**  | ✅ Auto-sent  | ❌            | ❌             | ❌                  |
| **Use**     | Auth tokens   | Settings      | Form data      | Large datasets      |

### 🔑 Details:

**Cookie:**

- Auto-sent with HTTP requests (authentication)
- Flags: `HttpOnly` (JS can't read - XSS protection), `Secure` (HTTPS only), `SameSite` (CSRF protection)
- Bandwidth cost (sent every request) → keep small

**LocalStorage:**

- Persistent (survives tab close), synchronous API
- Use case: User preferences, theme, language, cached data
- ⚠️ Never store sensitive data (tokens) - XSS vulnerable

**SessionStorage:**

- Tab-scoped (each tab separate), cleared on tab close
- Use case: Form wizards, temporary shopping cart, session-specific state
- Duplicate tab = duplicate storage

**IndexedDB:**

- Async database (transactions, indexes, queries)
- Store objects, files, blobs (not just strings)
- Use case: Offline apps, large datasets, binary files
- Libraries: Dexie.js, localForage (simplified API)

### ⚠️ Common Mistakes:

- Store tokens trong localStorage → XSS steals tokens (use HttpOnly cookies)
- Stringify/parse localStorage every access → performance hit (cache parsed value)
- No `QuotaExceededError` handling → app crash when storage full
- Synchronous IndexedDB API → use Promises/async (modern pattern)

### 💡 Senior Insights:

- **Security**: Access tokens → HttpOnly cookies, Refresh tokens → HttpOnly cookies
- **Storage events**: `window.addEventListener('storage')` → sync across tabs (localStorage only)
- **Quota API**: `navigator.storage.estimate()` → check available space
- **Cache API**: Different from localStorage, for HTTP response caching (Service Workers)

---

## Q31: Next.js Workflow & Version Comparison - Next.js 14 vs 15 vs 16

### 🎯 Trả Lời Ngắn Gọn:

**"Next.js evolution: Pages Router (v12-) → App Router (v13+). Next.js 14: Stable App Router, Server Actions, Turbopack beta. Next.js 15: Turbopack stable, Partial Pre-rendering (PPR), React 19 support. Version 16: TBD future features."**

### 📊 Version Comparison:

**Next.js 13 (Oct 2022):**

- App Router beta (React Server Components)
- Nested layouts, streaming SSR
- New `app/` directory structure

**Next.js 14 (Nov 2023):**

- Turbopack beta (Rust-based bundler, 5x faster HMR)
- Server Actions stable (call server from client)
- Partial Pre-rendering (PPR) experimental

**Next.js 15 (Oct 2024):**

- **Turbopack stable** (replace Webpack for dev)
- **React 19 support** (Actions, useActionState, use())
- PPR stable → hybrid static + dynamic rendering
- Improved caching strategies

### 🔑 Key Features:

**App Router Advantages:**

- **Server Components**: Zero JS bundle for non-interactive components
- **Streaming**: Progressive rendering, faster TTFB
- **Nested Layouts**: Shared UI persists across navigations
- **Parallel Routes**: Render multiple pages in same layout

**Pages Router (Legacy):**

- Simpler mental model
- Wider ecosystem (older tutorials)
- Migration path to App Router exists

### ⚠️ Common Mistakes:

- Mix Pages + App Router haphazardly → confusion (plan migration strategy)
- Use Client Components for everything → miss Server Component benefits
- Aggressive caching without revalidation → stale data
- Not understanding streaming → layout shifts (CLS issues)

### 💡 Senior Insights:

- **Turbopack**: 5-10x faster HMR than Webpack (large projects benefit most)
- **PPR (Partial Pre-rendering)**: Static shell + dynamic holes → best of both worlds
- **Migration**: Incremental (add `app/` alongside `pages/`), route-by-route
- **React 19 alignment**: Next.js 15+ optimized for React 19 features (Actions, Suspense)

---

## Q32: AG Grid - Enterprise Data Grid Performance & Best Practices

### 🎯 Trả Lời Ngắn Gọn:

**"AG Grid = enterprise React data grid với 1000+ features. Performance keys: Row virtualization (render visible rows only), `getRowId` (stable row IDs), `applyTransactionAsync` (batch updates), Column virtualization. Handle 100k+ rows smoothly."**

### 🚀 Performance Optimization:

**Core Patterns:**

1. **Row Virtualization**: Render only visible rows (~30-50 rows) instead of all (10k+ rows)
2. **`getRowId`**: Provide stable row IDs → efficient updates, no full re-render
3. **`applyTransactionAsync`**: Batch add/update/remove operations → single render
4. **Column Virtualization**: Render only visible columns (horizontal scrolling with 100+ cols)
5. **Suppress Animations**: Disable animations for bulk updates (`suppressAnimationFrame`)

**Real-Time Updates:**

- `applyTransaction({ add: [...], update: [...], remove: [...] })` - delta updates
- Cell flashing on value change (visual feedback)
- Server-Side Row Model for millions of rows (lazy loading chunks)

### 🔑 Advanced Features:

- **Row Grouping**: Group by categories, aggregates (sum, avg, min, max)
- **Pivot Mode**: Excel-like pivot tables
- **Master-Detail**: Expandable nested grids
- **Context Menu**: Custom right-click menus
- **Cell Rendering**: Custom components per cell (charts, buttons, badges)

### ⚠️ Common Mistakes:

- No `getRowId` → grid can't track rows → full re-render on updates (slow)
- Sync transactions in loop → multiple renders (use `applyTransactionAsync` batch)
- Heavy cell renderers → slow rendering (keep components lightweight)
- Not memoizing props → unnecessary grid re-initialization

### 💡 Senior Insights:

- **Server-Side Row Model**: Paginate + sort + filter on backend (handle millions of rows)
- **Immutable Data**: `immutableData: true` + `getRowId` → optimal updates
- **Memory**: AG Grid holds ~50-100 bytes per cell (10k rows × 10 cols = ~5-10MB)
- **Theming**: CSS variables for custom themes, dark mode support

---

## Q33: Frontend Tooling & Build Optimization - Bundling, Minify, Tree-Shaking

### 🎯 Trả Lời Ngắn Gọn:

**"Build optimization: Bundling (combine files), Minification (remove whitespace/comments), Tree-shaking (remove unused code), Code splitting (chunks), Transpiling (Babel/SWC - ES6+ → ES5). Tools: Webpack, Rollup, Vite, esbuild. Result: ~60-80% bundle size reduction."**

### 🔑 Optimization Techniques:

**1. Tree-Shaking (Dead Code Elimination):**

- Remove unused exports → smaller bundles
- Requires ES Modules (static `import`/`export`)
- Webpack `sideEffects: false` in package.json → aggressive shaking

**2. Code Splitting:**

- **Route-based**: Each route = separate chunk (lazy load on navigation)
- **Vendor splitting**: Separate vendor code (React, lodash) → cache separately
- **Dynamic imports**: `import()` loads on-demand

**3. Minification:**

- Remove whitespace, comments, shorten variable names
- Tools: Terser (JS), cssnano (CSS)
- ~30-40% size reduction

**4. Compression:**

- Gzip (standard, ~70% reduction)
- Brotli (better, ~75-80% reduction, modern browsers)
- Pre-compress at build time (serve `.br`, `.gz` files)

### ⚠️ Common Mistakes:

- Ship source maps to production publicly → expose source code (upload separately to error tracking)
- Not code splitting → large initial bundle (>500KB) → slow load
- Barrel exports (`index.js`) prevent tree-shaking → import directly from modules
- Not analyzing bundle → unknown bloat (use `webpack-bundle-analyzer`)

### 💡 Senior Insights:

- **Bundle analysis**: `webpack-bundle-analyzer`, `source-map-explorer` → visualize what's included
- **Polyfills**: Ship modern + legacy bundles (differential loading) → smaller for modern browsers
- **Performance budgets**: Fail builds if bundle exceeds thresholds (200KB JS, 3s LCP)
- **Lazy hydration**: Hydrate components on interaction (not immediately) → faster TTI

---

## Q34: Observer APIs - Intersection, Resize, Mutation Observer

### 🎯 Trả Lời Ngắn Gọn:

**"Browser Observer APIs: IntersectionObserver (element visibility - lazy loading), ResizeObserver (element size changes - responsive components), MutationObserver (DOM changes - custom elements, analytics). Performant alternative to scroll events polling."**

### 🔑 Three Observer APIs:

**1. IntersectionObserver (Visibility):**

- Detect when element enters/exits viewport
- Use case: Lazy load images, infinite scroll, analytics (track viewed items)
- **Better than scroll events**: Passive, async, performant (no layout thrashing)
- Options: `threshold` (0-1, when to trigger), `rootMargin` (expand viewport area)

**2. ResizeObserver (Size Changes):**

- Detect element size changes (not window resize)
- Use case: Responsive components, charts adjust to container, textarea auto-height
- **Better than window resize events**: Per-element, only fires when element resizes

**3. MutationObserver (DOM Changes):**

- Watch DOM mutations (attributes, children, subtree)
- Use case: Track third-party script changes, custom elements, undo/redo systems
- Options: `attributes`, `childList`, `subtree`, `characterData`

### ⚠️ Common Mistakes:

- IntersectionObserver không disconnect → memory leak (cleanup on component unmount)
- Excessive Mutation observations (entire document) → performance hit (narrow scope)
- Resize calculations trigger more resizes → infinite loop (guard conditions)
- Using scroll events when IntersectionObserver better → performance, battery drain

### 💡 Senior Insights:

- **Lazy loading pattern**: `<img loading="lazy">` native OR IntersectionObserver + placeholder
- **Performance**: Observers use async callback → don't block main thread (unlike scroll polling)
- **React integration**: Wrap in custom hooks (`useIntersectionObserver`, `useResizeObserver`)
- **Browser support**: Excellent modern support (95%+), polyfills available for legacy

---

## Q35: Độ Phức Tạp Thuật Toán (Big O) - Map, Set, Array, Object

### 🎯 Trả Lời Ngắn Gọn:

**"Big O notation đo time/space complexity. O(1) = constant (hash lookups), O(n) = linear (array search), O(n²) = quadratic (nested loops), O(log n) = logarithmic (binary search). Map/Set = O(1) lookups (hash table), Array = O(n) search, O(1) index access."**

### 📊 Data Structure Performance:

| Operation  | Array    | Object/Map | Set  |
| ---------- | -------- | ---------- | ---- |
| **Access** | O(1) idx | O(1) key   | -    |
| **Search** | O(n)     | O(1) key   | O(1) |
| **Insert** | O(n)\*   | O(1)       | O(1) |
| **Delete** | O(n)     | O(1)       | O(1) |

\*Array push = O(1) amortized, unshift/splice = O(n)

### 🔑 Common Complexities:

**O(1) - Constant:**

- Hash table lookup (Map.get, Set.has)
- Array index access (arr[5])
- Push/pop array end

**O(log n) - Logarithmic:**

- Binary search sorted array
- Balanced tree operations

**O(n) - Linear:**

- Array search (find, indexOf)
- Iterate array/object
- Filter, map array methods

**O(n²) - Quadratic:**

- Nested loops
- Bubble sort, insertion sort

### ⚠️ Common Mistakes:

- Use Array.includes() in loop → O(n²) (use Set.has() → O(n))
- Nested loops without optimization → quadratic complexity
- Deep object comparisons in render → slow (memoize)
- Not considering average vs worst case → hash collisions rare but possible

### 💡 Senior Insights:

- **Space-Time Tradeoff**: Map/Set use more memory but faster lookups
- **Amortized Analysis**: Array.push() = O(1) amortized (occasional resize = O(n))
- **Modern engines optimize**: V8 has hidden optimizations (small arrays = different strategy)
- **Practical**: O(n) vs O(n log n) matters at scale (>10k items), premature optimization below that

---

## Q36: Từ URL đến UI - Critical Rendering Path (Browser Render Process)

### 🎯 Trả Lời Ngắn Gọn:

**"Browser rendering: DNS lookup → TCP handshake → HTTP request → Parse HTML (DOM tree) → Parse CSS (CSSOM tree) → JavaScript execution → Render Tree → Layout (calculate positions) → Paint (pixels) → Composite (layers). Optimize: Minimize critical resources, defer non-critical JS/CSS, preload critical assets."**

### 🔄 Critical Rendering Path (9 Steps):

1. **DNS Resolution**: Domain → IP address (~20-120ms, cached)
2. **TCP Handshake**: 3-way handshake (SYN, SYN-ACK, ACK)
3. **TLS Negotiation**: HTTPS setup (~2 RTT)
4. **HTTP Request/Response**: Fetch HTML document
5. **Parse HTML → DOM**: Build DOM tree (incremental, can start before full download)
6. **Parse CSS → CSSOM**: Build CSSOM tree (blocks rendering)
7. **JavaScript Execution**: `<script>` blocks parsing (unless async/defer)
8. **Render Tree**: Combine DOM + CSSOM → visible elements only
9. **Layout → Paint → Composite**: Calculate positions → draw pixels → composite layers

### ⚡ Optimization Strategies:

**Minimize Critical Resources:**

- Inline critical CSS (~14KB) in `<head>` → fast first paint
- Defer non-critical CSS: `<link rel="preload" as="style" onload="this.rel='stylesheet'">`
- Async/defer JavaScript: Non-blocking parsing

**Optimize Resource Loading:**

- **Preload**: `<link rel="preload" href="font.woff2" as="font">` - critical assets
- **Prefetch**: `<link rel="prefetch" href="next-page.html">` - future navigation
- **Preconnect**: `<link rel="preconnect" href="https://api.example.com">` - early DNS+TCP

**Reduce Render Blocking:**

- Move `<script>` to end of `<body>` OR use `defer` attribute
- Split CSS: Critical inline, rest async
- Font loading strategy: `font-display: swap` (show text immediately)

### ⚠️ Common Mistakes:

- Large CSS files block rendering → inline critical CSS, defer rest
- Synchronous scripts in `<head>` → parser blocked (use `async`/`defer`)
- Many render-blocking resources → waterfall loading (parallelize với preload)
- Not measuring CRP → use Lighthouse, WebPageTest

### 💡 Senior Insights:

- **TTFB (Time to First Byte)**: Server response time (<600ms target), optimize với CDN
- **FCP (First Contentful Paint)**: First DOM content rendered (<1.8s target)
- **LCP (Largest Contentful Paint)**: Largest element visible (<2.5s target - Core Web Vital)
- **HTTP/2 Server Push**: Push critical resources before browser requests (experimental)

---

## Q37: OOP trong JavaScript - Classes, Inheritance, Encapsulation

### 🎯 Trả Lời Ngắn Gọn:

**"JavaScript OOP = prototype-based (not class-based like Java). ES6 Classes = syntactic sugar over prototypes. Core concepts: Encapsulation (private fields `#`), Inheritance (`extends`/`super`), Polymorphism (method overriding). Composition > Inheritance paradigm preferred in modern JS."**

### 🔑 OOP Pillars:

**1. Encapsulation (Data Hiding):**

- Private fields: `#privateField` (ES2022) - truly private
- Private methods: `#privateMethod()`
- Public API: Expose only necessary methods
- Alternative: WeakMap, Symbols (less elegant)

**2. Inheritance (Code Reuse):**

- `class Child extends Parent` - inherit properties/methods
- `super()` - call parent constructor
- `super.method()` - call parent methods
- Prototype chain: `Child.prototype.__proto__ === Parent.prototype`

**3. Polymorphism (Method Overriding):**

- Override parent methods in child class
- Duck typing: "If it walks like a duck..." (JS doesn't check types)
- Interfaces via TypeScript (runtime duck typing)

**4. Abstraction (Hide Complexity):**

- Public methods hide implementation details
- Abstract classes (TypeScript only - runtime JS doesn't enforce)

### ⚠️ Common Mistakes:

- Deep inheritance hierarchies → fragile, hard to maintain (prefer composition)
- Forget `super()` in constructor → ReferenceError
- Arrow functions as class methods → lose prototype, memory waste
- Mixing prototypes + classes → confusing code

### 💡 Senior Insights:

- **Composition > Inheritance**: Mixins, Higher-Order Functions, React Hooks pattern
- **SOLID principles**: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion
- **Factory functions**: Alternative to classes, use closures for privacy (no `new` keyword)
- **Performance**: Classes optimize well (V8 hidden classes), but factory functions acceptable

---

## Q38: Tối Ưu Performance React Web App

### 🎯 Trả Lời Ngắn Gọn:

**"React performance: Minimize re-renders (React.memo, useMemo, useCallback), Code splitting (React.lazy), Virtualization (react-window), Optimize images (WebP, lazy loading), Bundle analysis (webpack-bundle-analyzer), Measure (React Profiler, Lighthouse)."**

### 🚀 Top 10 Optimizations:

**1. React.memo():**

- Shallow compare props → skip re-render if unchanged
- Use for expensive components, list items

**2. useMemo / useCallback:**

- Cache expensive calculations / function references
- Prevent child re-renders from prop changes

**3. Code Splitting:**

- Route-based: `const Page = React.lazy(() => import('./Page'))`
- Component-based: Split heavy components (charts, editors)

**4. Virtualization (Long Lists):**

- `react-window` / `react-virtualized` - render only visible rows
- 1000 items → render ~30 → 97% faster

**5. Image Optimization:**

- Next.js `<Image>` component - auto WebP/AVIF, lazy load, responsive
- Set explicit width/height → prevent CLS

**6. Bundle Optimization:**

- Tree-shaking: Remove unused code
- Dynamic imports: Load on-demand
- Analyze: `webpack-bundle-analyzer`

**7. Avoid Inline Functions/Objects:**

- Create new references every render → children re-render
- Extract to variables/constants outside render

**8. Debounce Expensive Operations:**

- Search inputs, resize handlers
- Libraries: `lodash.debounce`, `use-debounce`

**9. Web Workers:**

- Offload heavy computation (data processing, image manipulation)
- Don't block main thread

**10. Measure & Monitor:**

- React Profiler DevTools → identify slow components
- Lighthouse CI → track Core Web Vitals
- Sentry Performance → real-user monitoring

### ⚠️ Common Mistakes:

- Premature optimization → measure first (React Profiler)
- Overuse memo → complexity, memory overhead (only for expensive components)
- Deep prop comparisons in memo → defeats purpose (shallow only)
- Not splitting bundles → 1MB initial load

### 💡 Senior Insights:

- **React 18 Concurrent Rendering**: `useTransition` marks low-priority updates → UI stays responsive
- **Suspense boundaries**: Wrap expensive components → progressive loading
- **Server Components** (Next.js): Zero JS for static components → smaller bundles
- **Keep bundle <200KB**: Target initial JS bundle, lazy load rest

---

## Q39: Bảo Mật Security trên Web Application

### 🎯 Trả Lời Ngắn Gọn:

**"Web security layers: HTTPS (encryption), XSS prevention (sanitize inputs, CSP headers), CSRF protection (CSRF tokens, SameSite cookies), Secure authentication (HttpOnly cookies, JWT rotation), Input validation, Security headers (CSP, HSTS, X-Frame-Options). Defense in depth = multiple layers."**

### 🛡️ Top 7 Security Threats & Solutions:

**1. XSS (Cross-Site Scripting):**

- **Attack**: Inject `<script>` → steal cookies, hijack session
- **Defense**: Sanitize user inputs (DOMPurify), React auto-escapes `{userInput}`, CSP headers

**2. CSRF (Cross-Site Request Forgery):**

- **Attack**: Trick user send malicious request (transfer money)
- **Defense**: CSRF tokens (unique per session), SameSite=Strict cookies

**3. SQL Injection:**

- **Attack**: Malicious SQL in inputs → access database
- **Defense**: Parameterized queries, ORMs (Prisma, Sequelize)

**4. Authentication Vulnerabilities:**

- **Attack**: Weak passwords, stolen tokens
- **Defense**: Strong passwords + MFA, HttpOnly cookies (XSS-proof), Token rotation

**5. Sensitive Data Exposure:**

- **Attack**: Unencrypted data, exposed API keys
- **Defense**: HTTPS everywhere, encrypt data at rest, environment variables (not hardcode)

**6. Broken Access Control:**

- **Attack**: Access unauthorized resources
- **Defense**: Server-side authorization checks, principle of least privilege

**7. Using Vulnerable Dependencies:**

- **Attack**: Exploit known CVEs
- **Defense**: Regular updates, `npm audit`, Snyk, Dependabot

### 🔒 Security Headers:

- **CSP**: `Content-Security-Policy: default-src 'self'` - block external scripts
- **HSTS**: `Strict-Transport-Security: max-age=31536000` - force HTTPS
- **X-Frame-Options**: `DENY` - prevent clickjacking
- **X-Content-Type-Options**: `nosniff` - prevent MIME sniffing

### ⚠️ Common Mistakes:

- Store tokens în localStorage → XSS steals tokens (use HttpOnly cookies)
- Trust client input → always validate server-side
- Hardcode API keys → Git history exposes (use .env + .gitignore)
- Not rate limiting → brute force attacks succeed

### 💡 Senior Insights:

- **Security Audits**: Regular penetration testing, bug bounty programs
- **OWASP Top 10**: Study annually updated list
- **helmet.js**: Express middleware → auto-set security headers
- **Security mindset**: Assume breach, defense in depth, least privilege

---

## Q40: Hashing, Encryption & Digital Signatures - Phân Biệt & Ứng Dụng

### 🎯 Trả Lời Ngắn Gọn:

**"Hashing (one-way, integrity check - bcrypt passwords), Encryption (two-way, confidentiality - AES-256 data), Digital Signatures (authenticity, non-repudiation - RSA verify sender). Use cases: Hash passwords, Encrypt sensitive data, Sign API tokens (JWT)."**

### 🔑 Three Concepts:

**1. Hashing (One-Way):**

- **Function**: `hash(input) → fixed-length digest`
- **Cannot reverse**: `hash(password)` but can't get password from hash
- **Use case**: Store passwords (bcrypt, argon2), file integrity (SHA-256)
- **Collision resistance**: Hard to find two inputs with same hash

**2. Encryption (Two-Way):**

- **Symmetric**: Same key encrypt + decrypt (AES-256 - fast, key distribution problem)
- **Asymmetric**: Public key encrypt, private key decrypt (RSA - slow, key exchange)
- **Use case**: Encrypt data in transit (HTTPS), at rest (database encryption)

**3. Digital Signatures (Verify Authenticity):**

- **Sign**: `sign(message, privateKey) → signature`
- **Verify**: `verify(message, signature, publicKey) → true/false`
- **Use case**: JWT tokens (verify not tampered), software downloads, emails

### 📊 Comparison:

| Aspect      | Hashing         | Symmetric Encryption | Asymmetric Encryption    |
| ----------- | --------------- | -------------------- | ------------------------ |
| **Purpose** | Integrity       | Confidentiality      | Key exchange, signatures |
| **Reverse** | ❌ One-way      | ✅ Decrypt           | ✅ Decrypt               |
| **Speed**   | Fast            | Fast                 | Slow                     |
| **Key**     | None            | Shared secret        | Public + Private pair    |
| **Example** | bcrypt, SHA-256 | AES-256              | RSA, ECDSA               |

### ⚠️ Common Mistakes:

- Hash passwords with MD5/SHA-1 → weak, use bcrypt/argon2 (slow = better for passwords)
- Encrypt passwords → over-engineering, hash is sufficient (encryption reversible)
- RSA for large data → slow, use hybrid (RSA exchange AES key, AES encrypt data)
- Store private keys in code → Git history exposes (use key management services)

### 💡 Senior Insights:

- **Salt + Hash**: Add random salt before hashing → prevent rainbow table attacks
- **PBKDF2, bcrypt, argon2**: Password hashing algorithms (intentionally slow ~100ms)
- **JWT structure**: `Header.Payload.Signature` - signature = HMAC SHA-256 (symmetric) OR RS256 (asymmetric)
- **Key rotation**: Periodically change encryption keys (compliance, security)

---

## Q41: Date & Time Handling - Xử Lý Múi Giờ Đúng Cách

### 🎯 Trả Lời Ngắn Gọn:

**"Date handling: JavaScript Date object (limited, timezone-naive), ISO 8601 format (`2024-01-01T12:00:00Z`), UTC for storage/transmission. Libraries: date-fns (lightweight, tree-shakeable), Luxon (Intl API, successor to Moment). Always store UTC, display in user's timezone."**

### 🔑 Best Practices:

**1. Storage & Transmission:**

- **Always store UTC** in database (timestamp or ISO 8601 with Z)
- **ISO 8601 format**: `2024-01-15T14:30:00.000Z` (unambiguous, sortable)
- Avoid storing local times without timezone info

**2. Display to User:**

- Convert UTC → user's local timezone
- `Intl.DateTimeFormat()` for localized display
- Libraries handle DST, leap seconds automatically

**3. Libraries Comparison:**

| Library  | Size  | Features                 | Tree-shake | Use Case         |
| -------- | ----- | ------------------------ | ---------- | ---------------- |
| date-fns | ~13KB | Functional, modular      | ✅ Yes     | Modern apps      |
| Luxon    | ~60KB | Timezone-aware, Intl API | ❌ No      | Complex timezone |
| Moment   | ~70KB | Legacy, mutable          | ❌ No      | Maintenance only |
| Day.js   | ~2KB  | Moment-like API, tiny    | ✅ Yes     | Bundle-conscious |

### ⚠️ Common Mistakes:

- Use `new Date()` without timezone → ambiguous, local machine dependent
- Compare dates with `===` → compare references, use `.getTime()` or `date-fns.isEqual()`
- Forget DST transitions → off by 1 hour errors (libraries handle automatically)
- Parse dates without format specification → unreliable (`new Date('2024-01-15')` behavior varies)

### 💡 Senior Insights:

- **Temporal API** (TC39 Stage 3): Future native solution (better than Date object)
- **Unix timestamp**: Milliseconds since 1970 UTC (`.getTime()`) - simple, timezone-agnostic
- **Backend responsibility**: Server should send UTC, frontend converts for display
- **Caching caveat**: Cache dates normalized (UTC) to avoid stale local-time data

---

## Q42: Client-Side Rendering (CSR) vs Server-Side Rendering (SSR) - Phân Biệt & Cách Hoạt Động Chi Tiết

### 🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):

CSR = browser render (SPA), SSR = server render HTML. CSR tốt cho interactive apps, SSR tốt cho SEO/performance. Modern: Hybrid (SSR first paint + CSR hydration).

### 🔑 So Sánh Chi Tiết:

| **Metric**       | **CSR**                      | **SSR**                    |
| ---------------- | ---------------------------- | -------------------------- |
| **Initial Load** | Chậm (download JS → execute) | Nhanh (HTML ready)         |
| **SEO**          | Kém (crawlers không chờ JS)  | Tốt (HTML đầy đủ)          |
| **Navigation**   | Nhanh (no reload)            | Chậm (full page reload)    |
| **Server Load**  | Thấp (static CDN)            | Cao (render mỗi request)   |
| **Complexity**   | Đơn giản (frontend only)     | Phức tạp (isomorphic code) |

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

| Aspect                   | Monolith              | Microfrontend                       |
| ------------------------ | --------------------- | ----------------------------------- |
| **Complexity**           | Low                   | High (orchestration, communication) |
| **Build Time**           | Slow (1 large app)    | Fast (parallel builds)              |
| **Deploy**               | All-or-nothing        | Independent per MFE                 |
| **Team Autonomy**        | Low (shared codebase) | High (own tech stack)               |
| **Bundle Size**          | Optimized             | Risk of duplication                 |
| **Developer Experience** | Simple                | Complex (tooling, debugging)        |

### 💡 Senior Insights:

- **When to use MFE**: Large teams (10+ devs), independent releases critical, different domains (e-commerce: catalog, checkout, profile).
- **When NOT to use**: Small teams, simple apps, tight coupling between features.
- **Module Federation vs Iframe**: MF = shared dependencies, better performance. Iframe = total isolation but clunky UX.
- **Styling Isolation**: CSS Modules, Shadow DOM, CSS-in-JS (styled-components) → prevent style conflicts.
- **Routing**: Each MFE handle own routes + Shell sync URL state.

---

## Q45: WebSocket & Real-Time Streaming - WebSocket, Socket.IO, Centrifuge

### 🎯 Trả Lời Ngắn Gọn:

**"WebSocket = persistent bidirectional TCP connection cho real-time data. Socket.IO = WebSocket wrapper với auto-reconnect + rooms. Centrifuge = scalable pub/sub với Redis for enterprise."**

### 🔑 3 Technologies Comparison:

**1. Native WebSocket API:**

- **Protocol**: `ws://` (unencrypted) hoặc `wss://` (SSL/TLS encrypted)
- **Persistent connection**: 1 handshake, reuse mãi (không phải reconnect mỗi request như HTTP)
- **Bidirectional**: Server push data bất cứ lúc nào, không cần client poll
- **Use case**: Trading platforms (real-time prices), chat, live notifications
- **Performance**: Low latency (~50ms), less bandwidth than polling (~90% reduction)

**2. Socket.IO (High-Level Library):**

- **Auto-reconnect**: Tự động kết nối lại khi connection lost
- **Fallback mechanisms**: WebSocket → HTTP long-polling (nếu WS blocked by firewall/proxy)
- **Rooms & Namespaces**: Organize connections (chat rooms, user-specific channels)
- **Broadcasting**: Send message to all/specific clients (to room, except sender...)
- **Event-based API**: `socket.emit('event', data)` - cleaner than raw WebSocket messages

**3. Centrifuge (Scalable Pub/Sub):**

- **Horizontal scaling**: Multiple server instances share state via **Redis Pub/Sub**
- **Channel subscriptions**: Client subscribe to channels, server publish to channels
- **Presence**: Track online users trong channels
- **History**: Replay missed messages (client offline → online recovery)
- **Use case**: Large-scale systems (>10k concurrent connections)

### 📊 So Sánh:

| Aspect               | WebSocket | Socket.IO                | Centrifuge        |
| -------------------- | --------- | ------------------------ | ----------------- |
| **Complexity**       | Low       | Medium                   | High              |
| **Fallback**         | ❌        | ✅ HTTP long-polling     | ✅ Multiple       |
| **Scalability**      | Manual    | Manual (sticky sessions) | ✅ Redis built-in |
| **Bundle size**      | Native    | ~60KB                    | ~30KB             |
| **Learning curve**   | Low       | Medium                   | Medium            |
| **Enterprise-ready** | ❌        | ⚡ Good                  | ✅ Best           |

### ⚠️ Common Mistakes:

- Không handle reconnection → connection lost = app broken, implement exponential backoff
- Send large payloads (>1MB) → slow, dùng binary frames (ArrayBuffer) thay JSON strings
- Không authenticate WS connections → security risk, validate tokens in handshake
- Memory leak: không cleanup event listeners khi disconnect
- Không implement heartbeat/ping-pong → dead connections accumulate

### 💡 Senior Insights:

- **WebSocket vs SSE**: SSE = server → client only (simpler, HTTP-based), WS = bidirectional
- **Heartbeat/Ping-Pong**: Detect dead connections (send ping every 30s, expect pong response)
- **Binary frames**: `ws.send(arrayBuffer)` nhanh hơn JSON strings (~40% bandwidth reduction)
- **Backpressure**: Client slow consume → buffer overflow, implement flow control (pause/resume)
- **Load balancing**: Sticky sessions (same client → same server) OR Redis pub/sub share state

---

## Q46: Build Tools - Vite vs Webpack vs Rollup, SWC vs Babel, Turbopack, esbuild

### 🎯 Trả Lời Ngắn Gọn:

**"Build tools hiện đại chia 2 nhóm: Bundlers (đóng gói - Webpack, Vite, Rollup, esbuild, Turbopack) và Transpilers (chuyển đổi code - Babel, SWC)."**

### 📦 Bundlers Comparison:

| Tool          | Language     | Speed       | Use Case                       | Bundle Size | Ecosystem |
| ------------- | ------------ | ----------- | ------------------------------ | ----------- | --------- |
| **esbuild**   | Go           | ⚡ Fastest  | Build only, simple configs     | Optimal     | Growing   |
| **Turbopack** | Rust         | ⚡⚡ Fast   | Next.js 13+, incremental cache | Optimal     | Young     |
| **Vite**      | JS + esbuild | ⚡ Fast dev | Modern apps, DX priority       | Good        | Large     |
| **Webpack**   | JavaScript   | Medium      | Enterprise, legacy support     | Good        | Huge      |
| **Rollup**    | JavaScript   | Medium      | Libraries, tree-shaking        | Best        | Medium    |

### ⚙️ Transpilers Comparison:

**Babel (JavaScript):**

- **Ecosystem**: Largest, tương thích tốt nhất
- **Speed**: Baseline (slow)
- **Features**: Plugins cho mọi thứ (experimental syntax, JSX, TypeScript)
- **Use case**: Complex transforms, custom plugins

**SWC (Rust):**

- **Speed**: ~20x faster than Babel
- **Features**: Drop-in Babel replacement (compatible với most plugins)
- **Adoption**: Next.js, Parcel, Deno đang dùng
- **Limitation**: Một số Babel plugins chưa support

### 🎯 Khi Nào Dùng Gì:

**Ứng dụng enterprise lớn:**

- Webpack (stability, mature) HOẶC Turbopack (speed + Next.js)

**Ứng dụng hiện đại/startup:**

- Vite (best DX, fast HMR)

**Thư viện/packages:**

- Rollup (best tree-shaking, ESM-first)

**Yêu cầu tốc độ cực cao:**

- esbuild (build) + SWC (transpile)

**Dùng Next.js 13+:**

- Turbopack (built-in, optimized)

### ⚠️ Trade-offs:

- **Tốc độ vs Ổn định**: esbuild/Turbopack nhanh nhưng ecosystem còn nhỏ, ít plugins
- **Dev vs Production**: Vite dev nhanh (ESM) nhưng production dùng Rollup (không nhất quán)
- **Plugin ecosystem**: Webpack > Rollup > Vite > esbuild (fewer plugins)

### 💡 Senior Insights:

- **Why native tools faster**: Go/Rust = multi-threading + no GC pauses + better memory model
- **Vite architecture**: Dev = ESM native (no bundle), Prod = Rollup (optimized bundle)
- **Turbopack incremental**: Cache persists across restarts (Rust + incremental computation)
- **Webpack still dominant**: 80% of enterprise apps, migration cost high
- **Future trend**: JavaScript tools → Native tools (Rust/Go) migration accelerating

---

## Q47: Git Workflow & Team Collaboration - Branching Strategy, Merge vs Rebase

### 🎯 Trả Lời Ngắn Gọn:

**"Git workflow tốt = ít conflicts + dễ review + dễ rollback. Git Flow cho dự án lớn (release theo version), GitHub Flow cho CI/CD (deploy liên tục). Rebase tạo clean history, Merge giữ context. Feature flags deploy code chưa xong mà không ảnh hưởng production."**

### 🔑 2 Branching Strategies:

**1. Git Flow (Enterprise/Mobile Apps):**

- **Branches**: `main` (production) + `develop` (integration) + `feature/*` + `release/*` + `hotfix/*`
- **Flow**: feature → develop → release → main
- **Hotfix**: main → hotfix → main + develop (fix bug khẩn cấp)
- **Use case**: Apps với versioned releases (v1.0, v2.0), mobile apps (App Store review)

**2. GitHub Flow (CI/CD/SaaS):**

- **Branches**: `main` (always deployable) + `feature/*`
- **Flow**: feature → PR → review → merge main → **auto deploy**
- **Simple**: Chỉ 2 loại branches, mỗi merge = deploy
- **Use case**: SaaS apps, web apps với frequent deployments (multiple times/day)

### 🔑 Merge vs Rebase:

| Aspect        | Merge                               | Rebase                                    |
| ------------- | ----------------------------------- | ----------------------------------------- |
| **History**   | Preserved (merge commits)           | **Clean (linear)** - easier to understand |
| **Context**   | Keeps timeline (when merged)        | Loses original timeline                   |
| **Conflicts** | Resolve once                        | Resolve per commit (multiple times)       |
| **Use case**  | **Public branches** (main, develop) | **Private feature branches**              |
| **Safety**    | Safe (non-destructive)              | Risky if done on shared branches          |

**Golden Rule**: **NEVER rebase public branches** (main, develop) - chỉ rebase local/feature branches trước khi merge

### 🚩 Feature Flags (LaunchDarkly, Unleash):

- **Deploy code OFF**: Push code với feature disabled (flag = false)
- **Gradual rollout**: Enable cho 10% users → 50% → 100%
- **A/B testing**: Test variants, measure metrics
- **Kill switch**: Instant disable nếu bug discovered

### ⚠️ Common Mistakes:

- Rebase shared branch + force push → team mất commits (disaster)
- Không pull trước merge → avoidable conflicts
- Commit trực tiếp vào main/develop → bypass reviews, low quality
- Large PRs (>500 lines) → rubber-stamp reviews, dùng feature flags để split

### 💡 Senior Insights:

- **Trunk-Based Development**: Mọi người commit main, feature flags control visibility (Google, Facebook practice)
- **Conventional Commits**: `feat:`, `fix:`, `docs:` format → auto-generate changelogs, semantic versioning
- **Git bisect**: Binary search tìm commit gây bug (tự động test mỗi commit - ~log(n) searches)
- **Squash merge**: Combine feature commits thành 1 commit khi merge main (clean history)

---

## Q48: React 19 Migration Guide - Upgrade từ React 18 sang 19

### 🎯 Trả Lời Ngắn Gọn:

**"React 19 thêm Actions (async transitions tự động handle pending/error), new hooks (useActionState, useOptimistic, use), ref as prop (no forwardRef). Breaking: PropTypes removed, createElement → jsx(), StrictMode double render. Migration: npx codemod + manual fixes."**

### 🔑 New Features:

**1. Actions - Async State Transitions:**

- **Auto-handle**: Pending states, error states, optimistic updates trong async operations
- **`useActionState(action, initialState)`**: All-in-one hook (replace useState + useTransition + error handling)
- **Form Actions**: `<form action={serverAction}>` - auto pending/error indicators
- **Pattern**: `useTransition` + async functions = Actions

**2. New Hooks:**

- **`useActionState`**: Combine useState + useTransition + error handling trong 1 hook
- **`useOptimistic`**: Optimistic UI updates (show immediately, rollback if fail)
- **`use(promise)`**: Read promises/context trong render (Suspense integration)

**3. Ref Simplification:**

- **`ref` as regular prop**: Không cần `forwardRef` wrapper nữa
- **Direct usage**: `<Component ref={myRef} />` works directly
- **Cleaner APIs**: Less boilerplate, clearer component interfaces

**4. Improved Suspense:**

- **Sibling boundaries**: Suspense boundaries không block nhau (parallel rendering)
- **Better error boundaries**: Improved integration với error handling

### 🔑 Breaking Changes:

**1. PropTypes Removed:**

- **Migrate to**: TypeScript HOẶC Zod/Yup runtime validation
- **Codemod**: `npx codemod react/19/remove-prop-types` (auto-remove PropTypes)

**2. StrictMode Double Render:**

- **Always**: Render 2 lần trong dev mode (even production builds)
- **Purpose**: Detect side effects, không ảnh hưởng production performance

**3. createElement → jsx():**

- **Internal change**: Build tools auto-handle (Babel, SWC)
- **Action**: Update Babel/SWC config nếu custom setup

**4. Context Changes:**

- `<Context.Provider>` deprecated → dùng `<Context>` directly
- `Context.Consumer` deprecated → dùng `useContext` hook

### ⚠️ Common Mistakes:

- Dùng PropTypes → runtime error, migrate sang TypeScript asap
- Rely on single render trong StrictMode → side effects leak (fix with useEffect cleanup)
- Forget `use()` chỉ call trong render (không trong conditions/loops - Rules of Hooks)
- `useOptimistic` không auto-rollback on error → phải manual handle

### 💡 Senior Insights:

- **Migration strategy**: Incremental (không cần rewrite all) - codemod → fix errors → adopt features gradually
- **Server Components**: React 19 stable support (Next.js App Router fully compatible)
- **React Compiler** (React Forget): Auto-memoization (experimental beta 2024, stable sớm 2025)
- **Actions vs Mutations**: Actions = client transitions, Server Actions = server mutations

---

## Q49: System Design - Thiết Kế Hệ Thống Frontend Architecture

### 🎯 Trả Lời Ngắn Gọn:

**"Frontend system design bao gồm: Architecture patterns (Microfrontends/Monorepo), API layer (BFF, GraphQL), State management (global/local/server), Performance (CDN, lazy load, code splitting), Resilience (error boundaries, circuit breakers, feature flags). Cần balance scalability vs complexity."**

### 🔑 5 Pillars của Frontend System Design:

**1. Architecture Patterns:**

- **Microfrontends**: Independent deployable apps share same domain (Module Federation)
  - Ưu: Teams tự chủ, tech diversity, independent deploy
  - Nhược: Complexity, bundle duplication, runtime overhead
- **Monorepo**: Single repo, multiple packages (Nx, Turborepo)
  - Ưu: Code sharing, atomic commits, unified tooling
  - Nhược: Build time, CI/CD complexity

**2. API Layer Design:**

- **BFF (Backend for Frontend)**: API gateway tailored cho frontend needs (aggregate services, transform data)
- **GraphQL**: Client-driven queries, avoid over/under-fetching
- **REST**: Simple, cacheable, well-understood, good for CRUD

**3. State Management:**

- **Server Cache**: React Query/SWR (API data, auto-refetch, optimistic updates)
- **Global State**: Redux/Zustand (auth, theme, user settings)
- **Local State**: useState/useReducer (forms, UI toggles)
- **URL State**: React Router (filters, pagination, search params)

**4. Performance Optimization:**

- **CDN**: Static assets + edge caching (CloudFlare, Vercel Edge)
- **Code Splitting**: Route-based (`React.lazy`), component-based lazy loading
- **Resource Hints**: `preload` (critical), `prefetch` (future), `preconnect` (DNS/TCP)
- **Image Optimization**: WebP/AVIF formats, responsive images, lazy loading

**5. Resilience & Monitoring:**

- **Error Boundaries**: Catch React errors, show fallback UI (prevent white screen)
- **Circuit Breaker**: Stop calling failing services (prevent cascade failures)
- **Feature Flags**: Gradual rollouts (10% → 50% → 100%), A/B testing
- **Monitoring**: Sentry (errors + breadcrumbs), DataDog/New Relic (performance), Analytics

### ⚠️ Common Mistakes:

- **Over-engineering**: Start simple monolith, migrate microfrontends when actually needed (>10 devs, independent releases)
- Không cache API responses → redundant requests, dùng React Query/SWR
- Single global store cho mọi state → complexity, dùng React Query cho server state
- Không error boundaries → 1 component crash = toàn app white screen

### 💡 Senior Insights:

- **CAP Theorem** (frontend): Trade-off giữa Consistency (data freshness) vs Availability (offline support)
- **Islands Architecture**: Static HTML + selective hydration (Astro) - best performance for content sites
- **Streaming SSR**: Progressive rendering (React 18 Suspense + Next.js)
- **Observability**: Distributed tracing (OpenTelemetry), RUM (Real User Monitoring), synthetic monitoring

---

## Q50: Testing Strategy - Unit, Integration, E2E Testing

### 🎯 Trả Lời Ngắn Gọn:

**"Test Pyramid: 60% Unit (fast, isolated - pure functions, hooks), 30% Integration (component interactions, API integration), 10% E2E (critical user flows only). Tools: Vitest/Jest (unit), React Testing Library (integration), Playwright/Cypress (E2E). TDD cho logic, BDD cho features."**

### 🔑 Test Pyramid:

```
      ╱╲
     ╱E2E╲      10% - Slow (~5-30s/test), expensive, critical paths only
    ╱─────╲
   ╱Integr.╲    30% - Medium (~50-200ms/test), component + API
  ╱─────────╲
 ╱   Unit    ╲  60% - Fast (~1ms/test), business logic, pure functions
╰───────────╯
```

### 🔑 3 Loại Tests:

**1. Unit Tests (Jest/Vitest):**

- **Test what**: Pure functions, utilities, custom hooks (isolated)
- **Speed**: ~1ms/test, chạy thousands trong vài giây
- **Mock**: External dependencies (APIs, modules, timers)
- **Coverage**: 80-90% cho business logic
- **Example**: `formatCurrency(1000)` → "$1,000.00"

**2. Integration Tests (React Testing Library):**

- **Test what**: Component interactions, user events, API integration
- **Speed**: ~50-200ms/test
- **Real DOM**: jsdom simulation, user-centric queries (`getByRole`, `getByText`)
- **Coverage**: 70-80% cho UI components
- **Example**: User clicks button → API call → show data/error

**3. E2E Tests (Playwright/Cypress):**

- **Test what**: Critical user flows (login → dashboard → action → verify)
- **Speed**: ~5-30s/test, chạy real browser (Chrome, Firefox, Safari)
- **Flaky**: Network issues, timing problems (use `waitFor`, retries)
- **Coverage**: Chỉ happy paths + critical error scenarios (checkout, payment)
- **Example**: Full e-commerce flow (browse → add cart → checkout → confirmation)

### 🔑 Best Practices:

- **AAA Pattern**: Arrange (setup) → Act (execute) → Assert (verify expected outcome)
- **Test behavior, not implementation**: Test user-visible outcomes, không test internal state/CSS classes
- **CI/CD Integration**: Unit+integration on PR (fast feedback), E2E on merge to main (pre-deploy)
- **TDD (Test-Driven Development)**: Write test → fail → implement → pass → refactor (red-green-refactor)

### ⚠️ Common Mistakes:

- Test implementation details (`.classList`, internal state) → brittle tests, dùng user behavior
- 100% coverage mọi thứ → waste time, focus critical logic + user paths
- Too many E2E tests → slow CI (20+ minutes), dùng integration tests thay vì
- Không test error cases → production bugs (network failures, validation errors)

### 💡 Senior Insights:

- **Visual Regression**: Chromatic, Percy - screenshot diff testing (catch UI regressions)
- **Performance Testing**: Lighthouse CI, WebPageTest - track Core Web Vitals over time
- **Contract Testing**: Pact - ensure frontend/backend API compatibility (schema validation)
- **Mutation Testing**: Stryker - test your tests (introduce bugs, check if tests catch them)
- **Parallel execution**: Playwright sharding, Jest workers - faster CI (~70% time reduction)

---

## Q51: Performance Monitoring & APM - Application Performance Monitoring

### 🎯 Trả Lời Ngắn Gọn:

**"Performance monitoring tracks Core Web Vitals (LCP, INP, CLS - Google ranking factors) + custom metrics. Tools: Sentry (error tracking + breadcrumbs), DataDog/New Relic (RUM - Real User Monitoring), Lighthouse CI (lab tests + budgets). Set performance budgets (JS < 200KB), alerts (LCP > 2.5s), optimize iteratively."**

### 🔑 Core Web Vitals (Google Ranking Factors):

**1. LCP (Largest Contentful Paint) - Tốc độ tải:**

- **Metric**: Thời gian phần tử lớn nhất hiển thị (hero image, heading)
- **Target**: ≤ 2.5s (good), 2.5-4s (needs improvement), > 4s (poor)
- **Optimize**: Preload critical images, CDN, optimize images (WebP/AVIF), fast server response (<600ms TTFB)

**2. INP (Interaction to Next Paint) - Responsiveness:**

- **Metric**: Thời gian từ user interaction (click/tap/keyboard) đến UI update
- **Target**: ≤ 200ms (good), 200-500ms (needs improvement), > 500ms (poor)
- **Optimize**: Debounce events, code splitting, avoid long tasks (>50ms), `requestIdleCallback`

**3. CLS (Cumulative Layout Shift) - Visual Stability:**

- **Metric**: Unexpected layout shifts (images, ads load → content jumps)
- **Target**: ≤ 0.1 (good), 0.1-0.25 (needs improvement), > 0.25 (poor)
- **Optimize**: Set explicit `width`/`height` cho images, reserve space cho ads, `font-display: swap`

### 🔑 APM Tools:

**1. Sentry - Error Tracking:**

- **Captures**: JS errors, unhandled Promise rejections, network errors
- **Context**: User info, breadcrumbs (user actions trước error), device/browser
- **Source maps**: Show original code trong production errors (upload maps securely)
- **Alerts**: Slack/email/PagerDuty khi error spike detected

**2. DataDog/New Relic - RUM (Real User Monitoring):**

- **Tracks**: Core Web Vitals, custom metrics (API latency, render time), user sessions
- **Distributed tracing**: Frontend request → API → Database (full stack visibility)
- **Dashboards**: Real-time metrics, historical trends, p50/p75/p95 percentiles
- **Synthetic monitoring**: Simulated user journeys (check uptime from multiple locations)

**3. Lighthouse CI:**

- **Lab tests**: Automated performance audits on every PR
- **Performance budgets**: Fail build nếu JS bundle > 200KB, LCP > 3s
- **Trend tracking**: Track performance regression over time (prevent gradual degradation)

### ⚠️ Common Mistakes:

- Ship source maps public → expose code to attackers, dùng `hidden-source-map` + upload riêng
- Không sample events → high APM costs (millions events/day), sample 10-20% traffic
- Ignore CLS → SEO penalty (-10% rankings), poor UX (accidental clicks)
- Không set performance budgets → gradual performance degradation (boiling frog syndrome)

### 💡 Senior Insights:

- **TTFB (Time to First Byte)**: Server response time, optimize với CDN/edge functions (<600ms target)
- **FID → INP**: Google replaced FID (First Input Delay) với INP vào 2024 (more comprehensive)
- **Custom metrics**: `performance.mark()`, `performance.measure()` cho business-critical flows
- **Session replay**: FullStory, LogRocket - replay user sessions cho debugging (video + console logs)
- **Alerting thresholds**: Set p75 thresholds (LCP p75 > 3s) → alerts → auto-escalate

---

## Q52: TypeScript Advanced Patterns - Generics, Utility Types, Advanced Patterns

### 🎯 Trả Lời Ngắn Gọn:

**"TypeScript advanced = Generics (type-safe reusable code), Utility Types (Partial, Pick, Omit, Record...), Mapped Types (transform types), Conditional Types (type-level if-else), Template Literal Types (string manipulation), Type Guards (runtime narrowing), Discriminated Unions (type-safe state machines)."**

### 🔧 Core Advanced Concepts:

**1. Generics - Type-safe Reusable Code:**

- **Purpose**: Functions/components work với multiple types mà vẫn type-safe
- **Constraints**: `<T extends Type>` → limit T to specific types
- **Example**: `function getProperty<T, K extends keyof T>(obj: T, key: K): T[K]` - type-safe property access

**2. Utility Types (Built-in Helpers):**

- **`Partial<T>`**: Tất cả properties → optional (dùng cho updates)
- **`Required<T>`**: Tất cả properties → required (strict validation)
- **`Pick<T, K>`**: Select subset properties (create DTO types)
- **`Omit<T, K>`**: Exclude properties (remove sensitive fields)
- **`Record<K, V>`**: Create object type với keys K, values V
- **`Readonly<T>`**: Immutable properties (prevent mutations)

**3. Mapped Types - Transform Existing Types:**

- **Pattern**: `{ [K in keyof T]: Transformation<T[K]> }`
- **Use case**: Create variations (readonly, optional, nullable versions)

**4. Conditional Types - Type-Level If-Else:**

- **Syntax**: `T extends U ? X : Y`
- **Use case**: Type inference, conditional return types
- **Example**: `type IsString<T> = T extends string ? true : false`

**5. Template Literal Types (TS 4.1+):**

- **Purpose**: String manipulation tại type level
- **Example**: `type EventName<T extends string> = \`on\${Capitalize<T>}\``→`"onClick"`, `"onSubmit"`

**6. Type Guards - Runtime Type Narrowing:**

- **Custom guards**: `function isString(value: unknown): value is string`
- **Use case**: Narrow `unknown`/`any` types safely trong runtime

**7. Discriminated Unions - Type-Safe State Machines:**

- **Pattern**: Common `type` property → TypeScript exhaustive checking
- **Use case**: API responses, Redux actions, state machines

### 🎯 Real-World Use Cases:

**1. API Response Typing:**

- `type ApiResponse<T> = { success: true; data: T } | { success: false; error: string }`

**2. Form State Management:**

- `type FormState<T> = { data: T; errors: Partial<Record<keyof T, string>>; isSubmitting: boolean }`

**3. Event Handlers:**

- `type EventHandlers<T> = { [K in keyof T as \`on\${Capitalize<K & string>}\`]: (value: T[K]) => void }`

### ⚠️ Common Mistakes:

- Over-use `any` → lose type safety, dùng `unknown` + type guards thay vì
- Không dùng Utility Types → duplicate type definitions manually
- Conditional types quá phức tạp → unreadable, split thành smaller types
- Forget `as const` cho literal types → types widened to general types

### 💡 Senior Insights:

- **`satisfies` operator** (TS 4.9+): Type-check mà không widen type
- **`infer` keyword**: Extract types from generic parameters trong conditional types
- **Branded Types**: Create nominal types (`type UserId = string & { __brand: 'UserId' }`) cho type safety
- **Template literal types + mapped types**: Generate typed CSS-in-JS, API routes

---

## Q53: CI/CD Pipeline - GitHub Actions, Deployment Automation

### 🎯 Trả Lời Ngắn Gọn:

**"CI/CD pipeline tự động hóa: Code quality checks (lint, test, type-check) → Build (bundle, optimize) → Deploy (staging/production). GitHub Actions: workflows YAML, matrix builds (test multi Node versions), caching (faster builds). Deploy strategies: Blue-Green (zero downtime), Canary (gradual rollout), Rolling (phased). Secrets management: GitHub Secrets + environment variables."**

### 🔑 CI/CD Stages:

**1. Code Quality (on Pull Request):**

- ESLint + Prettier check (code formatting, style rules)
- TypeScript type check (`tsc --noEmit`)
- Unit tests (Jest/Vitest - fast feedback)
- Integration tests (React Testing Library)
- Bundle size check (fail if exceeds budget - bundlesize, size-limit)

**2. Build (on Merge to Main):**

- Install dependencies (`npm ci` với cache - faster than `npm install`)
- Build production bundle (`npm run build` - minify, tree-shake)
- Generate source maps (upload to Sentry securely)
- Upload build artifacts (S3, Azure Blob, CDN)

**3. Deploy:**

- **Staging**: Auto-deploy on `develop` branch (QA testing environment)
- **Production**: Auto-deploy on `main` (or manual approval gate)
- **Deployment strategies**: Blue-Green, Canary, Rolling updates
- **Health checks**: Smoke tests post-deploy (critical endpoints responsive)

**4. Post-Deploy Monitoring:**

- Lighthouse CI (performance regression check)
- Sentry release tracking (link errors to releases)
- Slack/Discord notifications (team awareness)
- **Rollback** on failure (instant revert to previous version)

### 🔑 GitHub Actions Best Practices:

- **Matrix builds**: Test multiple Node versions (`18`, `20`, `22` in parallel)
- **Caching**: `actions/cache` cho `node_modules` - save 2-5 phút per build
- **Secrets management**: `${{ secrets.API_KEY }}` - never hardcode credentials
- **Conditional runs**: `if: github.event_name == 'push' && github.ref == 'refs/heads/main'`
- **Reusable workflows**: Share common workflows across repos (DRY principle)

### ⚠️ Common Mistakes:

- Không cache dependencies → mỗi build install lại từ đầu (waste 3-5 minutes)
- Hardcode secrets trong code/config → security breach, leaked credentials
- Deploy thẳng production không staging → no safety net, bugs in production
- Không implement rollback strategy → downtime khi deploy fails
- Ignore flaky tests → CI always red, lose trust in CI

### 💡 Senior Insights:

- **Docker multi-stage builds**: Build stage (dev deps) + production stage (only runtime deps) → smaller images (~70% size reduction)
- **Vercel/Netlify**: Zero-config CI/CD (auto-detect framework, instant previews on PR)
- **Deployment slots** (Azure App Service): Test production environment trước swap (blue-green pattern)
- **Feature flags integration**: Deploy code OFF (flag disabled), bật dần qua dashboard (LaunchDarkly, Unleash)
- **Infrastructure as Code**: Terraform, Pulumi - version control infrastructure

---

## Q54: Code Quality & Standards - ESLint, Prettier, Code Review

### 🎯 Trả Lời Ngắn Gọn:

**"Code quality stack: ESLint (catch bugs + enforce patterns), Prettier (auto-formatting), Husky (pre-commit hooks - run checks before commit), Commitlint (conventional commits - semantic versioning). Code review: Small PRs (<400 lines), clear descriptions (What/Why/How), constructive feedback (suggest alternatives), automated checks pass trước review."**

### 🔑 Tooling Stack:

**1. ESLint - Linting & Bug Detection:**

- **Find bugs**: Unused vars, missing React deps, potential errors
- **Enforce patterns**: `no-console`, `prefer-const`, React Hooks rules, a11y rules
- **Plugins**: `@typescript-eslint`, `eslint-plugin-react`, `eslint-plugin-jsx-a11y`, `eslint-plugin-import`
- **Config**: Extend popular configs (Airbnb, Standard) + customize rules

**2. Prettier - Auto-Formatting:**

- **Format**: Spacing, quotes (`'` vs `"`), semicolons, line breaks, trailing commas
- **Config**: `.prettierrc` - `printWidth: 100`, `singleQuote: true`, `trailingComma: 'es5'`
- **Integration**: ESLint plugin (`eslint-config-prettier` - disable conflicting rules)
- **IDE**: Format on save (VSCode `editor.formatOnSave: true`)

**3. Husky - Git Hooks Automation:**

- **Pre-commit**: Run lint-staged (lint + format only changed files) trước commit
- **Pre-push**: Run tests trước push (catch failures early)
- **Commit-msg**: Validate commit message format (conventional commits)
- **Setup**: `npx husky-init && npm install` + configure hooks

**4. Commitlint - Conventional Commits:**

- **Format**: `type(scope): subject` → `feat(auth): add JWT authentication`
- **Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`
- **Benefits**: Auto-generate changelogs (semantic-release), semantic versioning, clear history

### 🔑 Code Review Best Practices:

- **Small PRs**: < 400 lines (optimal ~200 lines) - dễ review, ít bugs slip through
- **Clear descriptions**: What changed, Why (context, ticket link), How (approach), Testing steps
- **Automated checks**: Lint, tests, bundle size, type check pass trước request review
- **Constructive feedback**: Suggest alternatives với reasoning (explain WHY, not just WHAT)
- **Timely reviews**: < 24 hours response time (avoid blocking teammates)
- **Approve + minor comments**: Approve if changes minor, trust author for small fixes

### ⚠️ Common Mistakes:

- ESLint warnings ignored → accumulate technical debt (broken windows theory)
- Không dùng Prettier → inconsistent formatting, merge conflicts on whitespace
- Large PRs (>1000 lines) → rubber-stamp reviews (too big to review properly)
- Blame culture trong reviews → team morale giảm, fear of feedback

### 💡 Senior Insights:

- **SonarQube**: Continuous code quality metrics (bugs, vulnerabilities, code smells, technical debt)
- **Bundle analysis**: `webpack-bundle-analyzer`, `source-map-explorer` - visualize bundle size, find bloat
- **Lighthouse CI**: Performance budgets trong CI/CD (fail if metrics degrade)
- **Danger.js**: Automate code review comments (warn big PRs, remind to add tests, check CHANGELOG)
- **Trunk-based development**: Short-lived branches (<1 day), frequent small merges

---

## Q55: GraphQL vs REST - API Design, Apollo Client

### 🎯 Trả Lời Ngắn Gọn:

**"GraphQL = single endpoint (`/graphql`), client-driven queries (chỉ lấy fields cần), exact data (no over/under-fetching). REST = multiple endpoints (`/users`, `/posts`), server-driven (backend quyết định response shape). Apollo Client: normalized caching (auto-dedupe), optimistic updates (instant UI), subscriptions (real-time WebSocket). GraphQL tốt cho complex/nested data, REST tốt cho simple CRUD + caching HTTP standard."**

### 🔑 GraphQL vs REST:

| Aspect             | REST                             | GraphQL                                      |
| ------------------ | -------------------------------- | -------------------------------------------- |
| **Endpoints**      | Multiple (`/users`, `/posts`)    | **Single** (`/graphql`)                      |
| **Data fetching**  | Server decides response shape    | **Client decides** (query fields)            |
| **Over-fetching**  | ✅ Common (get unnecessary data) | ❌ Exact fields requested                    |
| **Under-fetching** | ✅ Multiple requests (N+1)       | ❌ Single request (nested query)             |
| **Versioning**     | `/api/v1`, `/api/v2` URLs        | **No versions** (deprecate fields gradually) |
| **Caching**        | HTTP cache (simple, standard)    | Custom cache (Apollo InMemoryCache)          |
| **Learning curve** | Low (familiar)                   | Medium (new concepts)                        |

### 🔑 Apollo Client Features:

**1. Normalized Caching:**

- **Store objects by ID**: `User:123` cached once, referenced everywhere
- **Auto-dedupe**: Multiple components query same data → 1 network request
- **Cache policies**: `cache-first` (default - fast), `network-only` (always fresh), `cache-and-network` (fast + update)

**2. Queries & Mutations:**

- **`useQuery`**: Fetch data + automatic loading/error states
- **`useMutation`**: Modify data + optimistic updates + refetch affected queries
- **Fragments**: Reusable field selections (DRY principle)

**3. Subscriptions (Real-Time):**

- **WebSocket connection**: Listen to real-time updates từ server
- **Use case**: Chat messages, notifications, live dashboards, collaborative editing

**4. Optimistic Updates:**

- **Instant UI**: Update cache immediately (assume mutation succeeds)
- **Rollback**: Auto-revert if mutation fails (network error, validation failure)

### ⚠️ Common Mistakes:

- **N+1 query problem**: Backend issue (query User → query Posts for each User) - dùng DataLoader
- Không hiểu normalized cache → redundant network requests, manual `refetchQueries`
- Over-complicated queries → slow backend (too much nesting), split into multiple queries
- Public GraphQL endpoint không rate limiting → DoS risk (attackers craft expensive queries)

### 💡 Senior Insights:

- **Persisted Queries**: Pre-register queries on server (security + performance) - clients send query ID thay vì full query
- **Automatic Persisted Queries** (APQ): Client hash query → server caches → reduce bandwidth (~70%)
- **Federation**: Microservices architecture cho GraphQL (Apollo Federation - stitch multiple graphs)
- **Batching**: Combine multiple queries in 1 HTTP request (reduce network overhead)

---

## Q56: Web Accessibility (a11y) - WCAG 2.1, ARIA, Screen Readers

### 🎯 Trả Lời Ngắn Gọn:

**"Accessibility đảm bảo mọi người (disabilities, elderly, situational - broken arm) dùng được web. WCAG 2.1 levels: A (minimum), AA (legal requirement - ADA compliance), AAA (ideal). ARIA: roles, states, properties cho custom widgets. Keyboard navigation (Tab, Enter, Esc), color contrast (≥4.5:1), screen reader support (semantic HTML, alt text). Tools: axe, Lighthouse, NVDA/VoiceOver."**

### 🔑 WCAG 2.1 Compliance Levels:

**Level AA (Recommended - pháp lý nhiều nước):**

- **Color contrast**: ≥ 4.5:1 (normal text), ≥ 3:1 (large text 18pt+/24px+/bold 14pt+)
- **Keyboard accessible**: Tất cả functionality với keyboard only (no mouse-only traps)
- **Alt text**: Tất cả images có `alt` attribute (decorative images = `alt=""`)
- **Form labels**: `<label>` elements cho mọi `<input>` (explicit association)
- **Touch targets**: ≥ 44×44px clickable area (mobile WCAG 2.1 AAA = 44px minimum)
- **Focus indicators**: Visible focus outline (không `outline: none` without custom replacement)

### 🔑 ARIA Attributes:

**1. Roles (Define element purpose):**

- `role="button"` - Custom button behavior (div clickable → button semantics)
- `role="navigation"`, `role="main"`, `role="complementary"`, `role="search"`
- **First Rule of ARIA**: Dùng semantic HTML trước (`<button>` > `<div role="button">`)

**2. States (Dynamic properties):**

- `aria-expanded="true/false"` - Dropdown, accordion state
- `aria-checked="true/false/mixed"` - Custom checkbox/radio state
- `aria-disabled="true"` - Disabled state (còn trong tab order, khác `disabled` attribute)

**3. Properties (Relationships & labels):**

- `aria-label="Close dialog"` - Label cho icon buttons (no visible text)
- `aria-describedby="help-text-id"` - Link to help text (form fields + instructions)
- `aria-live="polite"` - Announce dynamic content (notifications, status messages)

### 🔑 Best Practices:

- **Semantic HTML first**: `<button>`, `<nav>`, `<main>`, `<header>` thay vì divs + ARIA
- **Keyboard navigation**: Logical Tab order, Enter/Space activate, Esc close modals/dropdowns
- **Screen reader testing**: NVDA (Windows free), VoiceOver (Mac/iOS built-in), TalkBack (Android)
- **Skip links**: "Skip to main content" link (hidden visually, visible on focus - bypass navigation)

### ⚠️ Common Mistakes:

- `outline: none` without custom focus indicator → keyboard users lost (không thấy focus ở đâu)
- Images không alt text → screen readers announce "image" (no context)
- Color-only information (red = error) → colorblind users miss (dùng icons + text)
- Auto-playing videos/carousels không pause → disorienting, WCAG violation

### 💡 Senior Insights:

- **Focus management**: Trap focus trong modals (Tab cycle within modal), restore focus sau close
- **Live regions**: `aria-live="polite"` (wait for pause), `aria-live="assertive"` (interrupt immediately)
- **Automated testing**: `axe-core` (library), `jest-axe` (Jest integration), Lighthouse CI (catch ~30-40% issues)
- **Manual testing essential**: Tab navigation walkthrough, zoom 200% test, screen reader test critical flows

---

## Q57: State Management Comparison - Redux vs Zustand vs Jotai

### 🎯 Trả Lời Ngắn Gọn:

**"State categories: Server state (React Query/SWR - cache, refetch), Global state (Redux/Zustand/Jotai - auth, theme), Local state (useState - forms, UI toggles), URL state (React Router - filters, pagination). Redux = mature + DevTools + middleware, Zustand = simple hooks-based (~1KB), Jotai = atomic granular (~3KB). Chọn based on app complexity + team experience."**

### 🔑 So Sánh 3 Libraries:

| Aspect             | Redux Toolkit         | Zustand       | Jotai              |
| ------------------ | --------------------- | ------------- | ------------------ |
| **Philosophy**     | Centralized store     | Simple hooks  | Atomic state       |
| **Boilerplate**    | Medium (RTK giảm)     | **Low**       | **Very low**       |
| **Bundle size**    | ~20KB                 | **~1KB**      | **~3KB**           |
| **Learning curve** | High (concepts many)  | **Low**       | Medium             |
| **DevTools**       | ✅ Best (time-travel) | ✅ Basic      | ✅ Basic           |
| **Async**          | createAsyncThunk      | Manual        | Async atoms        |
| **Use case**       | Large complex apps    | Simple global | Granular, Suspense |

### 🔑 Khi Nào Dùng Gì:

**1. Redux Toolkit (Large Apps, Complex Logic):**

- Large apps với complex state logic (multi-step flows, undo/redo)
- Cần **time-travel debugging**, state persistence (localStorage sync)
- Team quen Redux patterns (migration cost high)
- Need middleware (logging, analytics tracking, crash reporting)

**2. Zustand (Simple Global State):**

- **Simple global state** (theme, auth status, user preferences - ít interactions)
- Muốn **minimal boilerplate** + hooks-based API (no Provider wrapper)
- Small-medium apps (startups, MVPs)
- Easy migration từ Context API (drop-in replacement)

**3. Jotai (Atomic Updates, React Suspense):**

- **Atomic/granular updates** - chỉ re-render affected components (fine-grained reactivity)
- **React Suspense** integration (async atoms trigger Suspense boundaries)
- Derived state (computed values từ multiple atoms)
- Bottom-up approach (atoms compose, không cần define whole store upfront)

### ⚠️ Common Mistakes:

- Dùng Redux cho server state → duplication, stale data - dùng React Query/SWR thay vì
- Mọi state vào global store → over-centralization, dùng local state cho forms/UI toggles
- Không normalize Redux state → nested updates phức tạp (deep cloning), dùng `createEntityAdapter`
- Zustand mutate state trực tiếp → bugs (state not immutable), dùng `immer` middleware

### 💡 Senior Insights:

- **State categories strategy**: Server (React Query) | Global (Zustand/Redux) | Local (useState) | URL (React Router params)
- **Redux Toolkit Query** (RTK Query): Built-in data fetching (alternative to React Query, all-in-one solution)
- **Jotai atoms**: Work với React.lazy, Suspense boundaries (code splitting friendly)
- **Zustand middleware**: `persist` (localStorage sync), `immer` (immutable updates), `devtools` (Redux DevTools integration)

---

## Q58: Networking & Browser Internals - Mạng Nội Bộ Trình Duyệt

### 🎯 Trả Lời Ngắn Gọn:

**"Browser networking: DNS lookup → TCP handshake → TLS negotiation → HTTP request/response. HTTP/2: Multiplexing (parallel requests 1 connection), Server Push. HTTP/3: QUIC (UDP-based, faster handshake). Browser cache: Memory → Service Worker → HTTP cache → Network. Connection pooling: Reuse TCP connections (6 parallel/domain HTTP/1.1)."**

### 🔑 Request Lifecycle:

1. **DNS Resolution** (~20-120ms): Domain → IP address (cached by OS/browser)
2. **TCP Handshake** (~RTT): 3-way handshake (SYN, SYN-ACK, ACK)
3. **TLS Negotiation** (~2 RTT): HTTPS setup (certificate validation)
4. **HTTP Request**: Send request headers + body
5. **Server Processing**: Backend generates response
6. **HTTP Response**: Receive headers + body (chunked/streaming possible)

### 🔑 HTTP Versions:

**HTTP/1.1 (1999):**

- **Head-of-line blocking**: Sequential requests (1 request/response per connection)
- **Workarounds**: Domain sharding (multiple domains), connection pooling (6 connections/domain)

**HTTP/2 (2015):**

- **Multiplexing**: Multiple requests/responses parallel trên 1 connection
- **Header compression**: HPACK algorithm (reduce overhead ~70%)
- **Server Push**: Server gửi resources trước khi client request (preload critical assets)

**HTTP/3 (2022):**

- **QUIC protocol**: UDP-based (thay vì TCP) - faster connection setup (~1 RTT thay vì 3 RTT)
- **No head-of-line blocking**: TCP level (packet loss không block other streams)
- **Connection migration**: Switch networks (WiFi → 4G) without reconnect

### 🔑 Browser Cache Strategy:

1. **Memory Cache**: RAM cache (fastest, cleared on tab close)
2. **Service Worker Cache**: Programmatic cache (offline support, custom strategies)
3. **HTTP Cache**: Disk cache (Cache-Control headers, ETag validation)
4. **Network**: Fresh request nếu cache miss

### ⚠️ Common Mistakes:

- Không dùng HTTP/2 → waste (all modern browsers support, CDNs support)
- Incorrect Cache-Control headers → stale content hoặc too many requests
- Không preconnect to critical domains (`<link rel="preconnect">` - save DNS + TCP time)
- Large number of small requests → overhead (bundle hoặc HTTP/2 Server Push)

### 💡 Senior Insights:

- **Connection coalescing** (HTTP/2): Multiple domains same IP → reuse connection (save handshakes)
- **Early Hints** (103 status): Server hints critical resources while generating HTML (parallel loading)
- **Resource Hints**: `preconnect` (DNS + TCP ahead), `prefetch` (future navigation), `preload` (current page critical)
- **QUIC benefits**: Mobile users (frequent network switches) benefit most (~20-30% faster loads)

---

## Q59: CSS Architecture & Modern Styling Approaches

### 🎯 Trả Lời Ngắn Gọn:

**"CSS approaches: BEM (naming convention - `.block__element--modifier`), CSS Modules (scoped auto-generated classes), CSS-in-JS (Styled Components/Emotion - dynamic, colocated, runtime overhead), Tailwind (utility-first - fast dev, small bundle with PurgeCSS). Critical CSS = inline above-fold styles trong `<head>` để fast FCP. Chọn based on: team size, dynamic styling needs, performance priority."**

### 🔑 4 Modern Approaches:

**1. BEM (Block Element Modifier):**

- **Naming**: `.block__element--modifier` - `.card__title--highlighted`
- **Ưu**: Clear structure, no naming conflicts, team-friendly (easy onboarding)
- **Nhược**: Verbose (class names dài), manually maintain consistency
- **Use case**: Large teams, design systems, long-term maintenance projects

**2. CSS Modules:**

- **Scoped**: `import styles from './Button.module.css'` - classes auto-namespaced
- **Ưu**: Auto-scoped (no global pollution), works với existing CSS, gradual adoption
- **Nhược**: Không dynamic (can't compute styles based on props easily), separate files
- **Use case**: Component libraries, migration from traditional CSS, React/Vue apps

**3. CSS-in-JS (Styled Components, Emotion):**

- **Syntax**: `` const Button = styled.button`color: ${props => props.color}` ``
- **Ưu**: **Dynamic styles** (props/theme), colocated (component + styles), scoped, TypeScript support
- **Nhược**: Runtime overhead (~10-20ms SSR), bundle size (~15-20KB), requires build config
- **Use case**: Highly dynamic UIs, design tokens, theming systems (dark mode)

**4. Tailwind CSS (Utility-First):**

- **Syntax**: `className="bg-blue-500 hover:bg-blue-700 px-4 py-2 rounded"`
- **Ưu**: **Rapid development** (no context switching), small final bundle (PurgeCSS removes unused), consistent design (spacing scale, colors)
- **Nhược**: HTML "bloat" (many classes), learning curve (memorize utility names), custom designs harder
- **Use case**: Rapid prototyping, startups, landing pages, component libraries (Headless UI)

### 🔑 Critical CSS Optimization:

- **Inline above-fold CSS** trong `<head>` tag (hero section, navbar - instant paint)
- **Defer non-critical CSS**: `<link rel="preload" as="style" onload="this.rel='stylesheet'">` (async CSS)
- **Tools**: Critters (Next.js built-in), Critical (npm package - extract critical CSS automatically)
- **FCP improvement**: ~30-50% faster First Contentful Paint (largest benefit for users)

### ⚠️ Common Mistakes:

- CSS-in-JS trong SSR không extract styles → FOUC (Flash of Unstyled Content - blank then styled)
- Tailwind không configure PurgeCSS → 300KB+ CSS bundle (ship entire framework)
- BEM không consistent naming → teams use different conventions, lose benefits
- Global CSS specificity wars → `!important` hell, cascade issues

### 💡 Senior Insights:

- **Zero-runtime CSS-in-JS**: Linaria, Vanilla Extract - extract CSS at build time (no runtime cost)
- **Atomic CSS**: Tailwind, StyleX (Meta), Panda CSS - share utility classes across components
- **Design tokens**: CSS variables (`--color-primary`) cho themes, works với Tailwind/CSS-in-JS
- **Container queries** (CSS 2023): Style based on parent size (không phải viewport) - responsive components

---

## Q60: JavaScript Design Patterns for Frontend Development

### 🎯 Trả Lời Ngắn Gọn:

**"Essential design patterns: Singleton (1 instance - config, logger), Observer (subscribe changes - event listeners, state), Pub/Sub (decoupled events - analytics, cross-component), Factory (create objects - React.createElement), Module (encapsulation - ES6 modules), Dependency Injection (loose coupling - props, Context). Modern React: Hooks patterns (custom hooks), Compound Components (shared state), Render Props, HOCs."**

### 🔑 6 Essential Patterns:

**1. Singleton - Single Instance:**

- **Use case**: Database connection pool, global config object, logger service
- **JS implementation**: Module exports object (auto-singleton), class với static instance
- **Caution**: Global state (hard to test), avoid unless truly needed (dependency injection preferred)

**2. Observer - Subscribe to Changes:**

- **Pattern**: Subject maintains observers list → notify all on state change
- **Use case**: DOM event listeners, state management (Redux), reactive programming
- **Modern**: RxJS Observables, MobX reactivity, Vue reactivity system

**3. Pub/Sub (Publish-Subscribe):**

- **Khác Observer**: Decoupled (event bus mediates between publisher/subscriber - không direct reference)
- **Use case**: Cross-component communication, analytics events, logging
- **Implementation**: EventEmitter (Node.js), `window.postMessage`, Redux (action → reducers)

**4. Factory Pattern - Object Creation:**

- **Purpose**: Create objects without specifying exact class/constructor
- **Example**: `React.createElement()`, component factories, API client factories
- **Benefits**: Flexibility (swap implementations), hide complexity

**5. Module Pattern - Encapsulation:**

- **ES6 Modules**: `export/import` - native encapsulation (modern standard)
- **IIFE** (legacy): `(function(){ ... })()` - create private scope trước ES6 modules
- **Use case**: Libraries, utility functions, prevent global namespace pollution

**6. Dependency Injection - Loose Coupling:**

- **Pattern**: Pass dependencies as parameters (không hard-code/import directly)
- **Benefits**: Testable (mock dependencies), flexible (swap implementations)
- **React**: Props drilling, Context API, custom hooks inject dependencies

### 🔑 Modern React Patterns:

**1. Compound Components:**

- **Pattern**: Components share implicit state (parent → children via Context)
- **Example**: `<Select>` + `<Option>` - Option knows Select state without props
- **Benefits**: Flexible API, composition-friendly

**2. Render Props:**

- **Pattern**: `<DataProvider render={data => <UI data={data} />} />`
- **Use case**: Share stateful logic, inversion of control
- **Modern alternative**: Custom hooks (simpler, no wrapper components)

**3. Higher-Order Components (HOC):**

- **Pattern**: `withAuth(Component)` - wrap component, inject props
- **Use case**: Cross-cutting concerns (auth, logging, theming)
- **Limitations**: Props collision, wrapper hell → custom hooks preferred

**4. Custom Hooks:**

- **Pattern**: `useAuth()`, `useFetch()` - extract + reuse stateful logic
- **Benefits**: Composition, testable, no wrapper hell
- **Best practice**: Modern React preferred approach (over HOCs/Render Props)

### ⚠️ Common Mistakes:

- **Over-engineering**: Apply patterns không cần thiết → unnecessary complexity
- **Singleton abuse**: Everything global state → hard to test, tight coupling
- **Observer memory leaks**: Forget to unsubscribe → listeners accumulate
- **Pub/Sub không type-safe**: String event names → typos, dùng TypeScript typed events

### 💡 Senior Insights:

- **Strategy Pattern**: Interchangeable algorithms (sort strategies, payment methods, authentication providers)
- **Command Pattern**: Undo/redo functionality (Redux actions là Command pattern)
- **Proxy Pattern**: ES6 Proxy cho reactivity (Vue 3 reactivity system, MobX)
- **Facade Pattern**: Simplify complex APIs (Axios wraps fetch, jQuery wraps DOM, React Query wraps caching)

---

**🎯 Kết Luận Tổng Thể:**

Bản tóm tắt này bao gồm 60 câu hỏi Frontend Senior, từ JavaScript fundamentals (Q01-Q19), React/Modern frameworks (Q17, Q25, Q26, Q31, Q48), System design & Architecture (Q42-Q44, Q49), Testing & Quality (Q50, Q54), Performance & Monitoring (Q18, Q20, Q38, Q51), đến Advanced topics (TypeScript Q52, CI/CD Q53, GraphQL Q55, Accessibility Q56, State Management Q57, CSS Q59, Design Patterns Q60). Mỗi câu được tổng hợp ngắn gọn, tập trung vào khái niệm cốt lõi, so sánh, best practices, common mistakes và senior insights - format dễ scan, không code (chỉ concepts), phù hợp cho ôn tập phỏng vấn Senior/Staff level.
