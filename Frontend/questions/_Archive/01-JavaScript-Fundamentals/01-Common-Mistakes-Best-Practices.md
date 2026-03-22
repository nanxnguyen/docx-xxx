# 🚀 Q01: JavaScript Fundamentals Overview - Tổng Quan Nền Tảng

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-5 phút):**

**"JavaScript là ngôn ngữ lập trình đơn luồng, bất đồng bộ, chạy trên V8 engine với Event Loop để xử lý I/O không chặn.**

**🔑 5 Trụ Cột Nền Tảng:**

1. **Kiểu Dữ Liệu & Bộ Nhớ**:
   - 7 kiểu nguyên thủy (number, string, boolean, null, undefined, symbol, bigint) + Object
   - Primitive = stack (theo giá trị), Reference = heap (theo tham chiếu)
   - GC tự động dọn bộ nhớ (Mark-and-Sweep algorithm)

2. **Execution Context & Scope**:
   - Call Stack thực thi code đồng bộ (LIFO)
   - Scope chain: Global → Function → Block scope
   - Hoisting: `var` khởi tạo undefined, `let/const` trong TDZ
   - Closure = hàm + môi trường từ vựng xung quanh

3. **Bất Đồng Bộ (Event Loop)**:
   - **Microtask Queue** (ưu tiên cao): Promise.then, queueMicrotask
   - **Macrotask Queue** (ưu tiên thấp): setTimeout, setInterval
   - Event Loop: Call Stack → Microtasks → UI Render → 1 Macrotask
   - Async patterns: Callbacks → Promises → Async/Await

4. **OOP & Prototypes**:
   - Prototype chain: mỗi object có `__proto__` trỏ đến prototype
   - Class = syntactic sugar cho prototype-based inheritance
   - `this` binding: new → explicit (call/apply/bind) → implicit → default

5. **Modern JavaScript (ES6+)**:
   - `let/const` block scope thay `var`
   - Arrow functions = lexical `this`
   - Destructuring, spread/rest operators
   - Modules (import/export), classes
   - Promise, async/await cho async code

**⚠️ Lỗi Thường Gặp:**

- Mutate objects/arrays trực tiếp → dùng spread hoặc immutable methods
- Quên `return` trong arrow function `() => { value }` → phải `() => value` hoặc `() => ({ value })`
- `==` vs `===`: luôn dùng `===` (strict equality)
- Closure memory leaks: event listeners không cleanup
- `this` mất context khi pass method: dùng arrow function hoặc bind

**💡 Kiến Thức Senior:**

- **Performance**: Tránh blocking main thread, dùng Web Workers cho heavy computation
- **Memory**: WeakMap/WeakSet cho weak references tránh leaks
- **Security**: XSS prevention (sanitize inputs), CSP headers
- **Tooling**: TypeScript cho type safety, ESLint cho code quality
- **Patterns**: Module pattern, Observer, Factory, Singleton

---

> **Câu hỏi tổng quan**: Giới thiệu các khái niệm nền tảng JavaScript mà mọi Frontend Developer cần nắm vững

---

## 📖 **Mục Lục**

- [I. Giới Thiệu](#i-giới-thiệu)
- [II. Data Types & Type System](#ii-data-types--type-system)
- [III. Execution Context & Scope](#iii-execution-context--scope)
- [IV. Asynchronous JavaScript](#iv-asynchronous-javascript)
- [V. Object-Oriented & Functional](#v-object-oriented--functional)
- [VI. Modern JavaScript (ES6+)](#vi-modern-javascript-es6)
- [VII. Browser APIs & Performance](#vii-browser-apis--performance)
- [VIII. Learning Roadmap](#viii-learning-roadmap)

---

## **I. Giới Thiệu**

### **1.1. JavaScript Là Gì?**

```typescript
/**
 * ┌──────────────────────────────────┐
 * │ JAVASCRIPT - TỔNG QUAN NỀN TẢNG │
 * ├──────────────────────────────────┤
 * │                                  │
 * │ 🎯 ĐỊNH NGHĨA SIÊU DỄ HIỂU:      │
 * │ • High-level: Ngôn ngữ "sang     │
 * │   chảnh", gần gũi tiếng người.   │
 * │   Bạn viết code, JS tự dọn rác   │
 * │   bộ nhớ (Garbage Collection).  │
 * │                                  │
 * │ • Interpreted (JIT): Code chạy   │
 * │   "nóng" luôn, không cần biên    │
 * │   dịch. Engine vừa đọc vừa tối  │
 * │   ưu code cực nhanh.             │
 * │                                  │
 * │ • Single-threaded: Giống quán ăn │
 * │   chỉ có MỘT đầu bếp. Một lúc   │
 * │   chỉ xào một chảo, nhưng cực   │
 * │   nhanh tay (Event Loop).        │
 * │                                  │
 * │ • Non-blocking: Không "đứng      │
 * │   hình" khi chờ I/O. Chờ món    │
 * │   hầm thì đi thái hành, nhặt    │
 * │   rau chứ không đứng nhìn nồi.  │
 * │                                  │
 * │ • Prototype-based OOP: Kế thừa   │
 * │   kiểu "cha truyền con nối" bằng │
 * │   cách mượn "vật mẫu". Object cũ │
 * │   là khuôn đúc cho object mới.  │
 * │                                  │
 * │ • First-class functions: Hàm là  │
 * │   "VIP". Hàm có thể gán vào biến,│
 * │   truyền đi khắp nơi như dự tiệc.│
 * │                                  │
 * │ 🌐 MÔI TRƯỜNG CHẠY:              │
 * │ • Browser: Chrome, Safari,       │
 * │   Firefox (Client-side)          │
 * │ • Node.js: Server backend        │
 * │ • Deno, Bun: Modern runtime      │
 * │                                  │
 * └──────────────────────────────────┘
 */

// JavaScript chạy ở đâu?
const environments = [
  'Browser: DOM manipulation, Events, Fetch API',
  'Node.js: File system, HTTP servers, CLI tools',
  'Mobile: React Native, Ionic',
  'Desktop: Electron, Tauri',
  'IoT: Johnny-Five, Espruino',
];
```

### **1.2. Tại Sao JavaScript Quan Trọng?**

```typescript
/**
 * 🔥 JavaScript Statistics (2024):
 *
 * ✅ #1 Programming language (GitHub, Stack Overflow)
 * ✅ 98% websites sử dụng JS
 * ✅ 14M+ developers worldwide
 * ✅ Full-stack capable (Frontend + Backend)
 * ✅ Massive ecosystem (npm: 2M+ packages)
 *
 * 💼 Career Impact:
 * • Frontend: React, Vue, Angular, Svelte
 * • Backend: Node.js, Express, NestJS
 * • Mobile: React Native, Ionic
 * • Desktop: Electron
 * • DevOps: Build tools (Webpack, Vite)
 */
```

---

## **II. Data Types & Type System**

### **2.1. Primitive vs Reference Types**

```typescript
/**
 * 📦 8 DATA TYPES
 */

// 7 Primitives (Immutable)
const num: number = 42;
const str: string = 'Hello';
const bool: boolean = true;
const undef: undefined = undefined;
const nul: null = null;
const sym: symbol = Symbol('id');
const big: bigint = 9007199254740991n;

// 1 Complex (Mutable)
const obj: object = { name: 'John' };

/**
 * 🎯 CÁC KHÁI NIỆM "SỐNG CÒN":
 * • Stack (Ngăn xếp): Lưu các biến đơn giản như Number, String.
 *   Hãy tưởng tượng nó như các ô tủ nhỏ, mở ra là thấy đồ ngay.
 * • Heap (Bộ nhớ đống): Lưu Object, Array. Nó như một kho bãi
 *   khổng lồ, ta phải có "địa chỉ" (Reference) mới tìm được đồ.
 * • Pass by value: Copy hẳn một giá trị mới (Nhà ai nấy ở).
 * • Pass by reference: Dùng chung một địa chỉ (Sửa một nơi,
 *   tất cả những ai cầm chìa khóa địa chỉ đó đều thấy thay đổi).
 * • Shallow copy: Copy "lớp vỏ" bên ngoài, ruột bên trong vẫn
 *   dùng chung (Nguy hiểm!).
 * • Deep copy: Nhân bản vô tính hoàn toàn, độc lập 100%.
 * • Immutability: Không sửa cái cũ, luôn đẻ ra cái mới. Giúp
 *   code sạch, dễ debug và tránh lỗi "phản ứng dây chuyền".
 *
 * 📚 Chi tiết: Q02-data-types-&-memory-management
 */
```

### **2.2. Type Coercion & Comparison**

```typescript
/**
 * ⚠️ Type Coercion (Ép kiểu tự động)
 */

// Ép kiểu ngầm định (Implicit)
console.log(5 + '5'); // '55' (số cộng chuỗi → chuỗi)
console.log('5' - 2); // 3 (số trừ chuỗi → số)
console.log(true + 1); // 2 (true coi là 1, false coi là 0)

// So sánh (Comparison)
console.log(5 == '5'); // true (Loại bỏ kiểu dữ liệu, chỉ so giá trị)
console.log(5 === '5'); // false (So sánh cả giá trị VÀ kiểu dữ liệu - LUÔN DÙNG)

// Falsy values (8 giá trị JS coi là "Sai")
Boolean(false); // false
Boolean(0); // false
Boolean(''); // rỗng -> false
Boolean(null); // rỗng -> false
Boolean(undefined); // chưa xác định -> false
Boolean(NaN); // Không phải số -> false
Boolean(-0); // false
Boolean(0n); // BigInt 0 -> false

/**
 * 📚 Chi tiết: Q02 (Falsy/Truthy, == vs ===, null vs undefined)
 */
```

---

## **III. Execution Context & Scope**

### **3.1. Hoisting**

```typescript
/**
 * 🔼 HOISTING
 */

// var: hoisted + initialized undefined
console.log(x); // undefined
var x = 5;

// let/const: hoisted but TDZ
console.log(y); // ❌ ReferenceError: Cannot access before initialization
let y = 10;

// Functions: fully hoisted
greet(); // ✅ Works!
function greet() {
  console.log('Hi');
}

/**
 * 📚 Chi tiết: Q04-hoisting-&-temporal-dead-zone
 */
```

### **3.2. Scope & Closures**

```typescript
/**
 * 🔒 CLOSURES (Phép thuật "Bao đóng")
 * Hiểu đơn giản: Một hàm có khả năng mang theo một cái "ba lô" chứa
 * toàn bộ các biến ở môi trường xung quanh nó, ngay cả khi nó được
 * gọi ở một nơi xa lắc xa lơ.
 */

function createCounter() {
  let count = 0; // Biến này nằm trong "ba lô" của counter

  return {
    increment: () => ++count, // Luôn nhớ được 'count' là bao nhiêu
    getCount: () => count,
  };
}

const counter = createCounter();
console.log(counter.increment()); // 1
console.log(counter.getCount()); // 1

/**
 * 🎯 Tại sao phải dùng?
 * • Bảo mật (Private variables): Không cho ai sờ vào 'count' trực tiếp.
 * • Lưu trạng thái (State memory): Ghi nhớ dữ liệu qua nhiều lần gọi.
 * • Module pattern: Tạo ra các bộ công cụ riêng biệt, không đụng hàng.
 *
 * 📚 Chi tiết: Q08-closure-&-data-privacy
 */
```

### **3.3. Event Loop**

```typescript
/**
 * ⚡ EVENT LOOP (Vòng lặp sự kiện)
 * Hiểu đơn giản: JS là đơn luồng (một tay), Event Loop là cách nó
 * sắp xếp công việc để không bị rảnh tay nào.
 */

console.log('1: Sync'); // Tức thì (Call Stack)

setTimeout(() => console.log('2: Macro task'), 0); // Đợi sau cùng (Macrotask)

Promise.resolve().then(() => console.log('3: Micro task')); // Ưu tiên cao hơn setTimeout (Microtask)

console.log('4: Sync'); // Tức thì (Call Stack)

/**
 * Thứ tự chạy (Output):
 * 1: Sync (Đồng bộ chạy trước)
 * 4: Sync (Đồng bộ chạy tiếp)
 * 3: Micro task (Lời hứa Promise được ưu tiên xử lý trước)
 * 2: Macro task (setTimeout dù là 0ms vẫn phải đợi sau cùng)
 *
 * 📚 Chi tiết:
 * • Q06-event-loop (Đi sâu kỹ thuật)
 * • Q07-event-loop (Giải thích bằng ví dụ đời thực)
 */
```

---

## **IV. Asynchronous JavaScript**

### **4.1. Callbacks → Promises → Async/Await**

```typescript
/**
 * 🔄 SỰ TIẾN HÓA CỦA BẤT ĐỒNG BỘ
 */

// 1. Callbacks (Gây ra "Callback hell" - lồng nhau sâu hoắm, khó đọc)
getData((data) => {
  processData(data, (result) => {
    saveResult(result, () => {
      console.log('Done');
    });
  });
});

// 2. Promises (Đỡ hơn, dùng chuỗi .then để dàn phẳng code)
getData()
  .then(processData)
  .then(saveResult)
  .then(() => console.log('Done'))
  .catch(handleError);

// 3. Async/Await (Tốt nhất: Code bất đồng bộ nhìn như code đồng bộ, cực kỳ dễ đọc)
async function workflow() {
  try {
    const data = await getData(); // "Chờ" lấy dữ liệu
    const result = await processData(data); // "Chờ" xử lý
    await saveResult(result); // "Chờ" lưu
    console.log('Done');
  } catch (error) {
    handleError(error); // Bắt lỗi gọn gàng bằng try/catch
  }
}

/**
 * 📚 Chi tiết: Q13-asyncawait-vs-promises-vs-callbacks
 */
```

### **4.2. Parallel & Concurrent**

```typescript
/**
 * ⚡ CONCURRENT PATTERNS
 */

// Promise.all (Parallel)
const [users, posts, comments] = await Promise.all([
  fetchUsers(),
  fetchPosts(),
  fetchComments(),
]);

// Promise.race (First to resolve)
const fastest = await Promise.race([fetchFromServer1(), fetchFromServer2()]);

// Promise.allSettled (All results, success or fail)
const results = await Promise.allSettled([fetchUsers(), fetchPosts()]);

/**
 * 📚 Chi tiết: Q13, Q28-cancellation-concurrency-&-retry
 */
```

---

## **V. Object-Oriented & Functional**

### **5.1. Classes & Prototypes**

```typescript
/**
 * 🏗️ LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG (OOP) TRONG JS
 */

// ES6 Classes (Cách viết hiện đại, giống các ngôn ngữ như Java/C#)
class Person {
  constructor(
    public name: string,
    private age: number,
  ) {}

  greet() {
    return `Hi, I'm ${this.name}`;
  }
}

const john = new Person('John', 30);

// Prototype chain (Bản chất bên dưới của JS: Mọi thứ đều kế thừa qua "Vật mẫu")
console.log(john.__proto__ === Person.prototype); // true (John lấy mẫu từ Person)
console.log(Person.prototype.__proto__ === Object.prototype); // true (Person lấy mẫu từ Object gốc)

/**
 * 📚 Chi tiết:
 * • Q22-javascript-classes
 * • Q37-oop-trong-javascript
 */
```

### **5.2. Functional Programming**

```typescript
/**
 * 🔧 FUNCTIONAL PATTERNS
 */

// Pure functions
const add = (a: number, b: number) => a + b;

// Immutability
const users = [{ name: 'John' }];
const updated = users.map((u) => ({ ...u, age: 30 })); // New array

// Higher-order functions
const withLogging =
  (fn: Function) =>
  (...args: any[]) => {
    console.log('Called with:', args);
    return fn(...args);
  };

const loggedAdd = withLogging(add);

/**
 * 📚 Chi tiết: Q10-iife-&-functional-programming
 */
```

---

## **VI. Modern JavaScript (ES6+)**

### **6.1. ES6+ Features**

```typescript
/**
 * ⚡ CÁC TÍNH NĂNG ES6+ QUAN TRỌNG
 */

// Destructuring (Phá vỡ cấu trúc để lấy giá trị nhanh)
const { name, age } = user;
const [first, second] = array;

// Spread/Rest (Toán tử rải/gom)
const merged = { ...obj1, ...obj2 }; // Gộp object
const combined = [...arr1, ...arr2]; // Gộp mảng

// Arrow functions (Hàm mũi tên - ngắn gọn, giữ nguyên ngữ cảnh 'this')
const multiply = (a, b) => a * b;

// Template literals (Dùng dấu huyền ` để chèn biến vào chuỗi)
const greeting = `Hello, ${name}!`;

// Optional chaining (Dấu ?. giúp tránh lỗi "undefined" khi truy cập sâu)
const city = user?.address?.city;

// Nullish coalescing (Dấu ?? lấy giá trị mặc định nếu là null hoặc undefined)
const theme = settings?.theme ?? 'light';

// Modules (Chia nhỏ code ra nhiều file)
import { feature } from './module';
export default MyComponent;

/**
 * 📚 Chi tiết: Q03-es5-vs-es6+-features
 */
```

### **6.2. Advanced Features**

```typescript
/**
 * 🚀 ADVANCED ES6+
 */

// Generators
function* counter() {
  let i = 0;
  while (true) yield i++;
}

// Proxy
const proxy = new Proxy(target, {
  get: (obj, prop) => {
    console.log(`Accessing ${String(prop)}`);
    return obj[prop];
  },
});

// WeakMap/WeakSet
const privateData = new WeakMap();
class User {
  constructor(ssn: string) {
    privateData.set(this, { ssn });
  }
}

/**
 * 📚 Chi tiết:
 * • Q21-javascript-proxy
 * • Q23-generator-functions
 * • Q05-setmap-weaksetweakmap
 */
```

---

## **VII. Browser APIs & Performance**

### **7.1. DOM & Events**

```typescript
/**
 * 🌐 CÁC API CỦA TRÌNH DUYỆT (BROWSER APIs)
 */

// Thao tác với DOM (Cây thư mục HTML)
const element = document.querySelector('.container');
element?.addEventListener('click', handleClick);

// Event delegation (Ủy quyền sự kiện) - Gắn 1 sự kiện ở cha để quản lý tất cả con
document.body.addEventListener('click', (e) => {
  if ((e.target as HTMLElement).matches('.button')) {
    console.log('Button clicked');
  }
});

// Fetch API (Gọi dữ liệu từ Server)
const response = await fetch('/api/users');
const data = await response.json();

/**
 * 📚 Chi tiết:
 * • Q11-dom-events (Bubbling, Capturing, Delegation)
 * • Q12-dom-api-&-query-methods
 */
```

### **7.2. Performance**

```typescript
/**
 * ⚡ PERFORMANCE OPTIMIZATION
 */

// Debounce
const debounce = (fn: Function, delay: number) => {
  let timer: number;
  return (...args: any[]) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
};

// Memoization
const memo = new Map();
const fibonacci = (n: number): number => {
  if (memo.has(n)) return memo.get(n);
  if (n <= 1) return n;
  const result = fibonacci(n - 1) + fibonacci(n - 2);
  memo.set(n, result);
  return result;
};

// Web Workers
const worker = new Worker('worker.js');
worker.postMessage({ data: 'process this' });

/**
 * 📚 Chi tiết:
 * • Q15-advanced-deferring-execution
 * • Q19-loop-performance
 * • Q29-web-workers-service-worker
 * • Q38-tối-ưu-performance-của-react
 */
```

---

## **VIII. Learning Roadmap**

### **8.1. Beginner Level (0-6 months)**

```typescript
/**
 * 🎯 FUNDAMENTALS
 */

// Must learn:
const beginnerTopics = [
  'Q02: Data Types & Memory',
  'Q03: ES6+ Features',
  'Q04: Hoisting & TDZ',
  'Q08: Closures',
  'Q11: DOM Events',
  'Q12: DOM API',
  'Q13: Async/Await & Promises',
];

/**
 * Practice:
 * ✅ Variables, functions, arrays, objects
 * ✅ DOM manipulation (CRUD operations)
 * ✅ Event handling
 * ✅ Fetch API, async/await
 * ✅ ES6+ syntax (arrow functions, destructuring)
 */
```

### **8.2. Intermediate Level (6-18 months)**

```typescript
/**
 * 🚀 ADVANCED CONCEPTS
 */

const intermediateTopics = [
  'Q06/Q07: Event Loop',
  'Q14: Axios Interceptors',
  'Q17: React Query',
  'Q18: Browser Rendering',
  'Q20: HTTP Caching',
  'Q21: JavaScript Proxy',
  'Q22: Classes',
  'Q25: React Hooks & Patterns',
];

/**
 * Practice:
 * ✅ State management (Redux, Zustand)
 * ✅ Performance optimization
 * ✅ API integration patterns
 * ✅ Error handling
 * ✅ Testing (Jest, React Testing Library)
 */
```

### **8.3. Advanced Level (18+ months)**

```typescript
/**
 * 🏆 EXPERT TOPICS
 */

const advancedTopics = [
  'Q23: Generators & Async Generators',
  'Q27: CommonJS vs ESM',
  'Q28: Cancellation & Concurrency',
  'Q32: AG Grid (Enterprise)',
  'Q36: Browser Rendering (Critical Path)',
  'Q39: Security',
  'Q43: Authentication Flow',
  'Q44: Microfrontend & Monorepo',
  'Q46: Build Tools (Vite/Webpack)',
];

/**
 * Practice:
 * ✅ Architecture design (Microfrontend)
 * ✅ Build optimization (Tree shaking, Code splitting)
 * ✅ Security (XSS, CSRF, Auth)
 * ✅ Performance monitoring (Lighthouse, Web Vitals)
 * ✅ CI/CD pipelines
 */
```

---

## **IX. JavaScript Core Deep Dive & Best Practices**

### **9.1. This Keyword - Context Binding**

```typescript
/**
 * 🎯 TỪ KHÓA 'this' - 4 QUY TẮC RÀNG BUỘC (Dễ nhớ)
 */

// ══════════════════════════════════════════════════════════
// 1. RÀNG BUỘC MẶC ĐỊNH (Ngữ cảnh toàn cục)
// ══════════════════════════════════════════════════════════

function showThis() {
  console.log(this); // Window (trình duyệt) hoặc undefined (nếu dùng strict mode)
}

showThis();

// Strict mode (Chế độ nghiêm ngặt)
('use strict');
function strictThis() {
  console.log(this); // undefined (Bảo mật hơn, tránh sờ vào Window)
}

// ══════════════════════════════════════════════════════════
// 2. RÀNG BUỘC NGẦM ĐỊNH (Hàm thuộc về một Object)
// ══════════════════════════════════════════════════════════

const person = {
  name: 'John',
  greet() {
    console.log(this.name); // 'John' (this chính là person)
  },
};

person.greet(); // ✅ 'John'

// ❌ Bị mất ràng buộc (Lost binding)
const greetFn = person.greet;
greetFn(); // undefined (this bây giờ trỏ về window/undefined)

// ══════════════════════════════════════════════════════════
// 3. RÀNG BUỘC TƯỜNG MINH (call, apply, bind) - Ép 'this' phải là ai đó
// ══════════════════════════════════════════════════════════

function introduce(age: number, city: string) {
  console.log(`${this.name}, ${age}, ${city}`);
}

const user = { name: 'Alice' };

// call: Gọi hàm ngay lập tức, truyền tham số rời rạc
introduce.call(user, 25, 'NYC'); // Alice, 25, NYC

// apply: Gọi hàm ngay lập tức, truyền tham số dưới dạng MẢNG
introduce.apply(user, [25, 'NYC']); // Alice, 25, NYC

// bind: Không gọi ngay, trả về một HÀM MỚI với 'this' đã được gắn chặt
const boundIntroduce = introduce.bind(user);
boundIntroduce(25, 'NYC'); // Alice, 25, NYC

// ══════════════════════════════════════════════════════════
// 4. NEW BINDING (Constructor)
// ══════════════════════════════════════════════════════════

function Person(name: string) {
  this.name = name;
}

const john = new Person('John'); // this = new object

/**
 * 🎯 PRECEDENCE (Highest to Lowest):
 * 1. new binding
 * 2. Explicit binding (call/apply/bind)
 * 3. Implicit binding (object method)
 * 4. Default binding (global)
 */

// ══════════════════════════════════════════════════════════
// 5. ARROW FUNCTIONS (Lexical this)
// ══════════════════════════════════════════════════════════

const obj = {
  name: 'Object',

  // Regular function
  regular() {
    setTimeout(function () {
      console.log(this.name); // undefined (this = window)
    }, 100);
  },

  // Arrow function (inherits this from parent)
  arrow() {
    setTimeout(() => {
      console.log(this.name); // 'Object' (this = obj)
    }, 100);
  },
};

/**
 * ✅ Arrow function use cases:
 * • Event handlers
 * • Callbacks (setTimeout, map, filter)
 * • React class methods
 *
 * ❌ Don't use arrow functions:
 * • Object methods (no own 'this')
 * • Constructors (can't use 'new')
 * • Methods needing dynamic 'this'
 */
```

---

### **9.2. Prototype Chain & Inheritance**

```typescript
/**
 * 🧬 PROTOTYPE CHAIN
 */

// ══════════════════════════════════════════════════════════
// PROTOTYPE BASICS
// ══════════════════════════════════════════════════════════

function Animal(name: string) {
  this.name = name;
}

// Thêm phương thức vào prototype (chia sẻ chung cho mọi instance để tiết kiệm bộ nhớ)
Animal.prototype.speak = function () {
  return `${this.name} makes a sound`;
};

const dog = new Animal('Dog');

console.log(dog.speak()); // 'Dog makes a sound'
console.log(dog.__proto__ === Animal.prototype); // true (dog được tạo ra từ khuôn Animal)
console.log(Animal.prototype.constructor === Animal); // true

/**
 * Chuỗi Prototype (Prototype chain):
 * dog (tìm speak k thấy) → Animal.prototype (thấy speak) → Object.prototype → null
 */

// ══════════════════════════════════════════════════════════
// PROTOTYPAL INHERITANCE (ES5)
// ══════════════════════════════════════════════════════════

function Dog(name: string, breed: string) {
  Animal.call(this, name); // Gọi constructor của cha (kế thừa thuộc tính)
  this.breed = breed;
}

// Thiết lập kế thừa prototype
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

// Ghi đè phương thức (Override)
Dog.prototype.speak = function () {
  return `${this.name} barks`;
};

const husky = new Dog('Husky', 'Siberian');
console.log(husky.speak()); // 'Husky barks'
console.log(husky instanceof Dog); // true
console.log(husky instanceof Animal); // true

// ══════════════════════════════════════════════════════════
// CLASS SYNTAX (ES6) - Syntactic Sugar
// ══════════════════════════════════════════════════════════

class Person {
  constructor(
    public name: string,
    private age: number,
  ) {}

  greet() {
    return `Hi, I'm ${this.name}`;
  }

  // Getter
  get info() {
    return `${this.name}, ${this.age}`;
  }

  // Static method
  static create(name: string) {
    return new Person(name, 0);
  }
}

class Employee extends Person {
  constructor(
    name: string,
    age: number,
    public role: string,
  ) {
    super(name, age); // Gọi constructor của lớp cha
  }

  // Ghi đè phương thức (Override)
  greet() {
    return `${super.greet()}, I'm a ${this.role}`;
  }
}

const emp = new Employee('Alice', 30, 'Developer');
console.log(emp.greet()); // "Hi, I'm Alice, I'm a Developer"

/**
 * 🎯 Các khái niệm chính:
 * • Prototype chain: object → prototype → Object.prototype → null
 * • Shared methods: Định nghĩa ở prototype (tiết kiệm bộ nhớ)
 * • Own properties: Định nghĩa trong constructor (riêng biệt cho từng object)
 * • Inheritance: Dùng Object.create() hoặc từ khóa extends
 */
```

---

### **9.3. Memory Management & Garbage Collection**

```typescript
/**
 * 🗑️ GARBAGE COLLECTION
 */

// ══════════════════════════════════════════════════════════
// REACHABILITY
// ══════════════════════════════════════════════════════════

let user = { name: 'John' }; // Reachable (has reference)

user = null; // No longer reachable → garbage collected

// ══════════════════════════════════════════════════════════
// MEMORY LEAKS (Common Patterns)
// ══════════════════════════════════════════════════════════

// ❌ 1. Biến toàn cục (Global variables)
window.leakedData = new Array(1000000); // Không bao giờ được dọn dẹp

// ❌ 2. Quên dọn dẹp timer
setInterval(() => {
  // Tham chiếu cứ tăng dần mãi
  const data = fetchData();
}, 1000);

// ✅ Fix: Xóa timer khi không dùng
const timerId = setInterval(/* ... */);
clearInterval(timerId);

// ❌ 3. Closures giữ tham chiếu lớn
function createLeak() {
  const largeData = new Array(1000000);

  return function () {
    console.log(largeData.length); // Vô tình giữ cả mảng largeData trong bộ nhớ
  };
}

// ❌ 4. Tham chiếu DOM
const elements = [];
for (let i = 0; i < 1000; i++) {
  const el = document.createElement('div');
  elements.push(el); // Giữ lỳ element trong mảng dù có thể đã xóa khỏi DOM
}

// ✅ Fix: Xóa tham chiếu khi xong việc
elements.length = 0;

// ❌ 5. Event listeners (Sự kiện)
const button = document.querySelector('button');
button?.addEventListener('click', handleClick); // Button bị giữ trong bộ nhớ bởi listener

// ✅ Fix: Gỡ bỏ sự kiện (removeEventListener)
button?.removeEventListener('click', handleClick);

// ══════════════════════════════════════════════════════════
// WEAKMAP/WEAKSET (Tự động dọn rác)
// ══════════════════════════════════════════════════════════

// ✅ WeakMap: Key là object yếu, nếu không ai dùng sẽ tự biến mất
const privateData = new WeakMap();

class User {
  constructor(name: string, ssn: string) {
    privateData.set(this, { ssn }); // SSN stored privately
    this.name = name;
  }
}

let user1 = new User('John', '123-45-6789');
user1 = null; // privateData entry auto-removed

/**
 * 🎯 Best Practices:
 * • Nullify references when done
 * • Clear timers/intervals
 * • Remove event listeners
 * • Use WeakMap/WeakSet for caches
 * • Avoid global variables
 * • Profile memory (Chrome DevTools)
 */
```

---

### **9.4. Error Handling Best Practices**

```typescript
/**
 * ⚠️ ERROR HANDLING
 */

// ══════════════════════════════════════════════════════════
// TRY/CATCH/FINALLY
// ══════════════════════════════════════════════════════════

async function fetchUser(id: number) {
  try {
    const response = await fetch(`/api/users/${id}`);

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    return await response.json();
  } catch (error) {
    // Handle error
    console.error('Failed to fetch user:', error);

    // Re-throw with context
    throw new Error(`User fetch failed: ${error.message}`);
  } finally {
    // Always runs (cleanup)
    console.log('Request completed');
  }
}

// ══════════════════════════════════════════════════════════
// CUSTOM ERROR CLASSES
// ══════════════════════════════════════════════════════════

class ApiError extends Error {
  constructor(
    message: string,
    public statusCode: number,
    public response?: any
  ) {
    super(message);
    this.name = 'ApiError';
  }
}

class ValidationError extends Error {
  constructor(message: string, public field: string) {
    super(message);
    this.name = 'ValidationError';
  }
}

// Usage
function validateUser(user: any) {
  if (!user.email) {
    throw new ValidationError('Email is required', 'email');
  }
}

try {
  validateUser({ name: 'John' });
} catch (error) {
  if (error instanceof ValidationError) {
    console.log(`Field ${error.field}: ${error.message}`);
  }
}

// ══════════════════════════════════════════════════════════
// ERROR BOUNDARY PATTERN (React)
// ══════════════════════════════════════════════════════════

class ErrorBoundary extends React.Component {
  state = { hasError: false, error: null };

  static getDerivedStateFromError(error: Error) {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: any) {
    // Log to error reporting service
    logErrorToService(error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return <ErrorFallback error={this.state.error} />;
    }

    return this.props.children;
  }
}

// ══════════════════════════════════════════════════════════
// PROMISE ERROR HANDLING
// ══════════════════════════════════════════════════════════

// ❌ Unhandled promise rejection
fetchData(); // If rejects, crashes in production

// ✅ Always handle rejections
fetchData().catch((error) => {
  console.error('Failed:', error);
});

// ✅ Global handler (last resort)
window.addEventListener('unhandledrejection', (event) => {
  console.error('Unhandled promise rejection:', event.reason);
});

/**
 * 🎯 Best Practices:
 * • Use try/catch for async/await
 * • Create custom error classes
 * • Add context to errors
 * • Log errors to monitoring service
 * • Handle promise rejections
 * • Use Error Boundaries in React
 * • Never swallow errors silently
 */
```

---

### **9.5. Performance Best Practices**

```typescript
/**
 * ⚡ PERFORMANCE OPTIMIZATION
 */

// ══════════════════════════════════════════════════════════
// 1. AVOID EXPENSIVE OPERATIONS IN LOOPS
// ══════════════════════════════════════════════════════════

// ❌ Bad: DOM query in loop
for (let i = 0; i < 1000; i++) {
  document.querySelector('.container')?.appendChild(createNode());
}

// ✅ Good: Cache DOM reference
const container = document.querySelector('.container');
for (let i = 0; i < 1000; i++) {
  container?.appendChild(createNode());
}

// ✅ Better: Use DocumentFragment
const fragment = document.createDocumentFragment();
for (let i = 0; i < 1000; i++) {
  fragment.appendChild(createNode());
}
container?.appendChild(fragment);

// ══════════════════════════════════════════════════════════
// 2. DEBOUNCE & THROTTLE
// ══════════════════════════════════════════════════════════

// Debounce: Wait until user stops typing
function debounce<T extends (...args: any[]) => any>(
  fn: T,
  delay: number
): (...args: Parameters<T>) => void {
  let timer: number;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
}

// Usage: Search input
const searchInput = document.querySelector('input');
searchInput?.addEventListener(
  'input',
  debounce((e) => {
    search(e.target.value);
  }, 300)
);

// Throttle: Execute at most once per interval
function throttle<T extends (...args: any[]) => any>(
  fn: T,
  limit: number
): (...args: Parameters<T>) => void {
  let inThrottle: boolean;
  return (...args) => {
    if (!inThrottle) {
      fn(...args);
      inThrottle = true;
      setTimeout(() => (inThrottle = false), limit);
    }
  };
}

// Usage: Scroll event
window.addEventListener(
  'scroll',
  throttle(() => {
    console.log('Scrolled');
  }, 100)
);

// ══════════════════════════════════════════════════════════
// 3. LAZY LOADING & CODE SPLITTING
// ══════════════════════════════════════════════════════════

// Dynamic import
const loadModule = async () => {
  const module = await import('./heavy-module.js');
  module.init();
};

// React lazy loading
const HeavyComponent = React.lazy(() => import('./HeavyComponent'));

function App() {
  return (
    <Suspense fallback={<Loading />}>
      <HeavyComponent />
    </Suspense>
  );
}

// ══════════════════════════════════════════════════════════
// 4. MEMOIZATION
// ══════════════════════════════════════════════════════════

// Cache expensive calculations
const memoize = <T extends (...args: any[]) => any>(fn: T) => {
  const cache = new Map();

  return (...args: Parameters<T>): ReturnType<T> => {
    const key = JSON.stringify(args);

    if (cache.has(key)) {
      return cache.get(key);
    }

    const result = fn(...args);
    cache.set(key, result);
    return result;
  };
};

// Usage
const fibonacci = memoize((n: number): number => {
  if (n <= 1) return n;
  return fibonacci(n - 1) + fibonacci(n - 2);
});

console.log(fibonacci(40)); // Fast!

// ══════════════════════════════════════════════════════════
// 5. OBJECT/ARRAY OPERATIONS
// ══════════════════════════════════════════════════════════

// ❌ Slow: Array.includes for large arrays
const largeArray = Array.from({ length: 10000 }, (_, i) => i);
largeArray.includes(9999); // O(n)

// ✅ Fast: Set.has
const largeSet = new Set(largeArray);
largeSet.has(9999); // O(1)

// ❌ Slow: Object property lookup
const obj = { a: 1, b: 2 /* ...1000 props */ };
obj.hasOwnProperty('z'); // O(n) in worst case

// ✅ Fast: Map
const map = new Map(Object.entries(obj));
map.has('z'); // O(1)

// ══════════════════════════════════════════════════════════
// 6. AVOID LAYOUT THRASHING
// ══════════════════════════════════════════════════════════

// ❌ Layout thrashing (read/write interleaved)
elements.forEach((el) => {
  const width = el.offsetWidth; // Read (forces layout)
  el.style.width = width + 10 + 'px'; // Write
});

// ✅ Batch reads, then batch writes
const widths = elements.map((el) => el.offsetWidth); // Batch reads
elements.forEach((el, i) => {
  el.style.width = widths[i] + 10 + 'px'; // Batch writes
});

/**
 * 🎯 Performance Checklist:
 * ✅ Cache DOM references
 * ✅ Use event delegation
 * ✅ Debounce/throttle events
 * ✅ Lazy load heavy modules
 * ✅ Use Set/Map for lookups
 * ✅ Avoid layout thrashing
 * ✅ Memoize expensive functions
 * ✅ Use Web Workers for heavy tasks
 * ✅ Profile with DevTools (Performance tab)
 * ✅ Monitor with Lighthouse
 */
```

---

### **9.6. Code Quality Best Practices**

```typescript
/**
 * 📝 CODE QUALITY
 */

// ══════════════════════════════════════════════════════════
// 1. IMMUTABILITY
// ══════════════════════════════════════════════════════════

// ❌ Mutation
const user = { name: 'John', age: 30 };
user.age = 31; // Mutates original

// ✅ Immutability
const updatedUser = { ...user, age: 31 }; // New object

// Array operations
const numbers = [1, 2, 3];

// ❌ Mutating
numbers.push(4);

// ✅ Immutable
const newNumbers = [...numbers, 4];

// ══════════════════════════════════════════════════════════
// 2. PURE FUNCTIONS
// ══════════════════════════════════════════════════════════

// ✅ Pure: Same input → Same output, No side effects
const add = (a: number, b: number) => a + b;

// ❌ Impure: Side effects
let total = 0;
const addToTotal = (n: number) => {
  total += n; // Modifies external state
  return total;
};

// ✅ Pure version
const addToTotal = (total: number, n: number) => total + n;

// ══════════════════════════════════════════════════════════
// 3. SINGLE RESPONSIBILITY PRINCIPLE
// ══════════════════════════════════════════════════════════

// ❌ Does too much
function processUserData(data: any) {
  const validated = validate(data);
  const transformed = transform(validated);
  const saved = save(transformed);
  sendEmail(saved);
  logActivity(saved);
  return saved;
}

// ✅ Single responsibility
function validateUser(data: any) {
  /* ... */
}
function transformUser(data: any) {
  /* ... */
}
function saveUser(data: any) {
  /* ... */
}
function notifyUser(data: any) {
  /* ... */
}

// Compose functions
const processUser = (data: any) => {
  const validated = validateUser(data);
  const transformed = transformUser(validated);
  const saved = saveUser(transformed);
  notifyUser(saved);
  return saved;
};

// ══════════════════════════════════════════════════════════
// 4. EARLY RETURNS
// ══════════════════════════════════════════════════════════

// ❌ Nested conditions
function processUser(user: User) {
  if (user) {
    if (user.active) {
      if (user.email) {
        return sendEmail(user.email);
      } else {
        return 'No email';
      }
    } else {
      return 'Inactive';
    }
  } else {
    return 'No user';
  }
}

// ✅ Early returns (guard clauses)
function processUser(user: User) {
  if (!user) return 'No user';
  if (!user.active) return 'Inactive';
  if (!user.email) return 'No email';

  return sendEmail(user.email);
}

// ══════════════════════════════════════════════════════════
// 5. DESCRIPTIVE NAMING
// ══════════════════════════════════════════════════════════

// ❌ Bad names
const d = new Date();
const u = getU();
function calc(a, b) {
  return a * b;
}

// ✅ Descriptive names
const currentDate = new Date();
const activeUser = getActiveUser();
function calculateTotal(price: number, quantity: number) {
  return price * quantity;
}

// ══════════════════════════════════════════════════════════
// 6. AVOID MAGIC NUMBERS
// ══════════════════════════════════════════════════════════

// ❌ Magic numbers
if (user.age >= 18 && user.accountBalance > 1000) {
  approveApplication();
}

// ✅ Named constants
const MINIMUM_AGE = 18;
const MINIMUM_BALANCE = 1000;

if (user.age >= MINIMUM_AGE && user.accountBalance > MINIMUM_BALANCE) {
  approveApplication();
}

/**
 * 🎯 Checklist chất lượng code:
 * ✅ Dùng cấu trúc dữ liệu bất biến (Immutable)
 * ✅ Viết hàm thuần khiết (Pure functions - không side effect)
 * ✅ Mỗi hàm chỉ làm 1 việc (Single responsibility)
 * ✅ Return sớm để tránh if/else lồng nhau (Guard clauses)
 * ✅ Đặt tên biến/hàm môt tả rõ nghĩa (Descriptive naming)
 * ✅ Tránh "con số ma thuật" (Magic numbers) -> dùng hằng số (CONSTANTS)
 * ✅ Giữ hàm ngắn gọn (<20 dòng)
 * ✅ Dùng TypeScript để bắt lỗi kiểu dữ liệu
 * ✅ Comment giải thích các logic phức tạp
 * ✅ Viết test đầy đủ (Unit, Integration)
 */
```

---

### **9.7. Security Best Practices**

```typescript
/**
 * 🔒 SECURITY
 */

// ══════════════════════════════════════════════════════════
// 1. XSS PREVENTION
// ══════════════════════════════════════════════════════════

// ❌ Dangerous: innerHTML with user input
const userInput = '<img src=x onerror="alert(1)">';
element.innerHTML = userInput; // XSS vulnerability!

// ✅ Safe: textContent or sanitize
element.textContent = userInput; // Escaped automatically

// ✅ Sanitize HTML
import DOMPurify from 'dompurify';
element.innerHTML = DOMPurify.sanitize(userInput);

// ══════════════════════════════════════════════════════════
// 2. CSRF PROTECTION
// ══════════════════════════════════════════════════════════

// ✅ Include CSRF token in requests
fetch('/api/transfer', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-CSRF-Token': getCsrfToken(),
  },
  body: JSON.stringify({ amount: 100 }),
});

// ══════════════════════════════════════════════════════════
// 3. SENSITIVE DATA
// ══════════════════════════════════════════════════════════

// ❌ Storing sensitive data in localStorage
localStorage.setItem('password', 'secret123'); // Accessible via XSS

// ✅ Use httpOnly cookies (server-side only)
// Set-Cookie: session=abc123; HttpOnly; Secure; SameSite=Strict

// ❌ Logging sensitive data
console.log('User password:', user.password);

// ✅ Sanitize logs
console.log('User:', { ...user, password: '[REDACTED]' });

// ══════════════════════════════════════════════════════════
// 4. INPUT VALIDATION
// ══════════════════════════════════════════════════════════

// ❌ No validation
function transferMoney(amount: number) {
  // What if amount is negative?
  processTransfer(amount);
}

// ✅ Validate inputs
function transferMoney(amount: number) {
  if (typeof amount !== 'number') {
    throw new ValidationError('Amount must be a number');
  }

  if (amount <= 0) {
    throw new ValidationError('Amount must be positive');
  }

  if (amount > MAX_TRANSFER_AMOUNT) {
    throw new ValidationError('Amount exceeds limit');
  }

  processTransfer(amount);
}

/**
 * 🎯 Security Checklist:
 * ✅ Sanitize user input (XSS)
 * ✅ Use CSRF tokens
 * ✅ Validate all inputs
 * ✅ Use HTTPS only
 * ✅ Set secure headers (CSP, HSTS)
 * ✅ Never store secrets in code
 * ✅ Use httpOnly cookies
 * ✅ Implement rate limiting
 * ✅ Keep dependencies updated
 * ✅ Use Content Security Policy
 *
 * 📚 Chi tiết: Q39-bảo-mật-security
 */
```

---

## **🎯 Quick Reference Card**

```typescript
/**
 * ┌──────────────────────────────────┐
 * │ JAVASCRIPT FUNDAMENTALS CHEAT    │
 * ├──────────────────────────────────┤
 * │                                  │
 * │ 📌 DATA TYPES:                   │
 * │ • 7 Primitives + 1 Object        │
 * │ • Stack (primitives) vs Heap     │
 * │                                  │
 * │ 📌 EXECUTION:                    │
 * │ • Hoisting: var (undefined),     │
 * │   let/const (TDZ)                │
 * │ • Scope: Global, Function, Block │
 * │ • Closures: Functions remember   │
 * │   outer scope                    │
 * │                                  │
 * │ 📌 ASYNC:                        │
 * │ • Event Loop: Call Stack →       │
 * │   Micro → Macro                  │
 * │ • Promises: then/catch chains    │
 * │ • Async/Await: Syntactic sugar   │
 * │                                  │
 * │ 📌 ES6+:                         │
 * │ • Arrow functions, Destructuring │
 * │ • Optional chaining (?.)         │
 * │ • Nullish coalescing (??)        │
 * │ • Modules (import/export)        │
 * │                                  │
 * │ 📌 DOM:                          │
 * │ • querySelector                  │
 * │ • addEventListener               │
 * │ • Event bubbling/capturing       │
 * │ • Fetch API, async requests      │
 * │                                  │
 * └──────────────────────────────────┘
 */
```

---

## **X. Common Frontend Mistakes & Optimizations**

### **10.1. Array Operations - O(n²) → O(n)**

```typescript
/**
 * 🐌 SLOW: Multiple iterations (filter + map)
 */

// ══════════════════════════════════════════════════════════
// MISTAKE 1: Chaining filter + map
// ══════════════════════════════════════════════════════════

const users = [
  { id: 1, name: 'John', age: 25, active: true },
  { id: 2, name: 'Jane', age: 30, active: false },
  { id: 3, name: 'Bob', age: 35, active: true },
  // ... 10,000 users
];

// ❌ Tệ: Chạy 2 vòng lặp (O(2n) = O(n))
const activeUserNames = users
  .filter((u) => u.active) // Vòng lặp 1: Lọc
  .map((u) => u.name); // Vòng lặp 2: Lấy tên

// ✅ Tốt: Chạy 1 vòng lặp với reduce (O(n))
const activeUserNames = users.reduce((acc, user) => {
  if (user.active) {
    acc.push(user.name);
  }
  return acc;
}, [] as string[]);

// ✅ Better: Using for loop (fastest)
const activeUserNames: string[] = [];
for (let i = 0; i < users.length; i++) {
  if (users[i].active) {
    activeUserNames.push(users[i].name);
  }
}

/**
 * 📊 SO SÁNH TỐC ĐỘ (Với 10.000 phần tử):
 * • filter + map: ~2ms (Chạy 2 vòng lặp riêng biệt - O(2n))
 * • reduce: ~1.2ms (Gộp lại chạy 1 vòng duy nhất - O(n)) - Nhanh hơn 40%
 * • for loop: ~0.8ms (Tốc độ "bàn thờ", tối ưu nhất vì không tốn công gọi hàm callback liên tục)
 *
 * 💡 LỜI KHUYÊN: Nếu data ít thì dùng filter+map cho code đẹp.
 * Nếu data lớn (hàng chục nghìn dòng), hãy dùng reduce hoặc for-loop.
 */

// ══════════════════════════════════════════════════════════
// MISTAKE 2: Multiple filter/map/reduce chains
// ══════════════════════════════════════════════════════════

// ❌ Tệ: Chạy đến 4 vòng lặp
const result = data
  .filter((x) => x.age > 18) // Vòng lặp 1
  .map((x) => ({ ...x, adult: true })) // Vòng lặp 2
  .filter((x) => x.active) // Vòng lặp 3
  .map((x) => x.name); // Vòng lặp 4

// ✅ Tốt: Chỉ 1 vòng lặp duy nhất
const result = data.reduce((acc, x) => {
  if (x.age > 18 && x.active) {
    acc.push(x.name);
  }
  return acc;
}, [] as string[]);

// ══════════════════════════════════════════════════════════
// MISTAKE 3: find() trong loop
// ══════════════════════════════════════════════════════════

const orders = [
  /* 1000 orders */
];
const products = [
  /* 1000 products */
];

// ❌ Bad: O(n²) - 1,000,000 operations!
const enrichedOrders = orders.map((order) => ({
  ...order,
  product: products.find((p) => p.id === order.productId), // O(n) inside O(n)
}));

// ✅ Good: O(n) - 2,000 operations
const productMap = new Map(products.map((p) => [p.id, p])); // O(n)
const enrichedOrders = orders.map((order) => ({
  ...order,
  product: productMap.get(order.productId), // O(1)
})); // O(n)

/**
 * 🚀 TẠI SAO LẠI NHANH HƠN 250 LẦN?
 * • find in loop: Giống như bạn đi tìm chìa khóa trong 1000 cái túi,
 *   mỗi lần tìm một túi lại phải bới tung cả 1000 túi khác (O(n²)).
 * • Map lookup: Giống như bạn đánh số thứ tự cho 1000 cái túi.
 *   Cần túi số 5? Bạn bốc ngay lập tức vì đã biết vị trí (O(n + 1)).
 *
 * 📊 KẾT QUẢ (1,000 items):
 * • Cách cũ: ~500ms (Máy bắt đầu lag)
 * • Cách mới (Map): ~2ms (Nhanh như chớp)
 */

// ══════════════════════════════════════════════════════════
// MISTAKE 4: includes() trong loop
// ══════════════════════════════════════════════════════════

const selectedIds = [1, 2, 3 /* ... 1000 ids */];
const allItems = [
  /* ... 10000 items */
];

// ❌ Tệ: Độ phức tạp O(n²) - Chạy cực chậm
const selectedItems = allItems.filter(
  (item) => selectedIds.includes(item.id), // O(n) lồng trong O(n)
);

// ✅ Tốt: Độ phức tạp O(n) - Nhanh hơn nhiều
const selectedIdsSet = new Set(selectedIds); // O(n) để tạo Set
const selectedItems = allItems.filter(
  (item) => selectedIdsSet.has(item.id), // O(1) để kiểm tra
);
```

---

### **10.1.5. Code Refactoring Examples - Giải Pháp A → Giải Pháp B**

```typescript
/**
 * 📚 NHIỀU VÍ DỤ REFACTORING TỪ GIẢI PHÁP KHÔNG TỐI ƯU SANG TỐI ƯU
 * Mục đích: Cung cấp nhiều pattern thực tế để áp dụng trong dự án
 */

// ══════════════════════════════════════════════════════════
// PATTERN 1: map + filter → reduce (Nhiều ví dụ)
// ══════════════════════════════════════════════════════════

// 📌 Ví dụ 1: Lọc và transform users
const users = [
  { id: 1, name: 'John', age: 25, active: true, role: 'admin' },
  { id: 2, name: 'Jane', age: 30, active: false, role: 'user' },
  { id: 3, name: 'Bob', age: 35, active: true, role: 'user' },
  // ... 10,000 users
];

// ❌ Giải pháp A: map + filter (Duyệt 2 lần)
const activeAdminNames = users
  .filter((u) => u.active && u.role === 'admin') // Duyệt lần 1: O(n)
  .map((u) => u.name); // Duyệt lần 2: O(m) với m ≤ n

// ✅ Giải pháp B: reduce (Duyệt 1 lần duy nhất)
const activeAdminNames = users.reduce((acc, user) => {
  if (user.active && user.role === 'admin') {
    acc.push(user.name);
  }
  return acc;
}, [] as string[]);
// 💡 Chỉ duyệt 1 lần: O(n) - nhanh hơn ~40-50%

// 📌 Ví dụ 2: Tính tổng giá trị sau khi filter
const orders = [
  { id: 1, amount: 100, status: 'completed', discount: 10 },
  { id: 2, amount: 200, status: 'pending', discount: 20 },
  { id: 3, amount: 150, status: 'completed', discount: 15 },
  // ... 5,000 orders
];

// ❌ Giải pháp A: filter + map + reduce (3 lần duyệt)
const totalCompleted = orders
  .filter((o) => o.status === 'completed') // Duyệt lần 1: O(n)
  .map((o) => o.amount - o.discount) // Duyệt lần 2: O(m)
  .reduce((sum, amount) => sum + amount, 0); // Duyệt lần 3: O(m)

// ✅ Giải pháp B: reduce (1 lần duyệt)
const totalCompleted = orders.reduce((sum, order) => {
  if (order.status === 'completed') {
    return sum + (order.amount - order.discount);
  }
  return sum;
}, 0);
// 💡 Chỉ duyệt 1 lần: O(n) - nhanh hơn ~66%

// 📌 Ví dụ 3: Group và transform data
const products = [
  { id: 1, category: 'electronics', price: 100, inStock: true },
  { id: 2, category: 'clothing', price: 50, inStock: false },
  { id: 3, category: 'electronics', price: 200, inStock: true },
  // ... 20,000 products
];

// ❌ Giải pháp A: filter + map (nhiều lần duyệt)
const electronicsInStock = products
  .filter((p) => p.category === 'electronics') // Duyệt lần 1: O(n)
  .filter((p) => p.inStock) // Duyệt lần 2: O(m)
  .map((p) => ({ id: p.id, price: p.price })); // Duyệt lần 3: O(k)

// ✅ Giải pháp B: reduce (1 lần duyệt)
const electronicsInStock = products.reduce(
  (acc, product) => {
    if (product.category === 'electronics' && product.inStock) {
      acc.push({ id: product.id, price: product.price });
    }
    return acc;
  },
  [] as Array<{ id: number; price: number }>,
);
// 💡 Chỉ duyệt 1 lần: O(n) - nhanh hơn ~66%

// 📌 Ví dụ 4: Tạo object từ array với điều kiện
const items = [
  { id: 1, name: 'Item 1', type: 'A', value: 10 },
  { id: 2, name: 'Item 2', type: 'B', value: 20 },
  { id: 3, name: 'Item 3', type: 'A', value: 30 },
  // ... 15,000 items
];

// ❌ Giải pháp A: filter + reduce (2 lần duyệt)
const typeAItems = items
  .filter((item) => item.type === 'A') // Duyệt lần 1: O(n)
  .reduce(
    (acc, item) => {
      acc[item.id] = item.name;
      return acc;
    },
    {} as Record<number, string>,
  ); // Duyệt lần 2: O(m)

// ✅ Giải pháp B: reduce (1 lần duyệt)
const typeAItems = items.reduce(
  (acc, item) => {
    if (item.type === 'A') {
      acc[item.id] = item.name;
    }
    return acc;
  },
  {} as Record<number, string>,
);
// 💡 Chỉ duyệt 1 lần: O(n) - nhanh hơn ~50%

// ══════════════════════════════════════════════════════════
// PATTERN 2: includes() → Set.has() (Nhiều ví dụ)
// ══════════════════════════════════════════════════════════

// 📌 Ví dụ 1: Check existence trong filter
const allowedRoles = ['admin', 'moderator', 'editor'];
const users = [
  { id: 1, name: 'John', role: 'admin' },
  { id: 2, name: 'Jane', role: 'user' },
  { id: 3, name: 'Bob', role: 'moderator' },
  // ... 50,000 users
];

// ❌ Giải pháp A: includes() trong filter (O(n²))
const authorizedUsers = users.filter(
  (user) => allowedRoles.includes(user.role), // O(m) mỗi lần, với m = allowedRoles.length
);
// 💡 Tổng: O(n × m) - với n = 50,000, m = 3 → 150,000 operations

// ✅ Giải pháp B: Set.has() (O(n))
const allowedRolesSet = new Set(allowedRoles); // O(m) - chỉ làm 1 lần
const authorizedUsers = users.filter(
  (user) => allowedRolesSet.has(user.role), // O(1) mỗi lần
);
// 💡 Tổng: O(m) + O(n) = O(n) - chỉ 50,003 operations
// 💡 Nhanh hơn ~3 lần với m = 3, và càng nhiều hơn khi m tăng!

// 📌 Ví dụ 2: Loại bỏ duplicates
const numbers = [1, 2, 3, 2, 4, 3, 5, 1, 6, 2, 7, 3];
// ... có thể có 100,000 số với nhiều duplicates

// ❌ Giải pháp A: filter + indexOf (O(n²))
const uniqueNumbers = numbers.filter(
  (num, index) => numbers.indexOf(num) === index, // O(n) mỗi lần
);
// 💡 Tổng: O(n²) - với n = 100,000 → 10 TỶ operations!

// ✅ Giải pháp B: Set (O(n))
const uniqueNumbers = [...new Set(numbers)];
// 💡 Tổng: O(n) - chỉ 100,000 operations
// 💡 Nhanh hơn ~100,000 lần với n = 100,000!

// 📌 Ví dụ 3: Check nhiều điều kiện
const blacklistedEmails = [
  'spam@example.com',
  'test@example.com',
  'admin@example.com',
  // ... 1,000 emails
];
const incomingEmails = [
  { id: 1, from: 'user@example.com', subject: 'Hello' },
  { id: 2, from: 'spam@example.com', subject: 'Buy now!' },
  // ... 100,000 emails
];

// ❌ Giải pháp A: includes() trong filter (O(n × m))
const validEmails = incomingEmails.filter(
  (email) => !blacklistedEmails.includes(email.from), // O(m) mỗi lần
);
// 💡 Tổng: O(n × m) - với n = 100,000, m = 1,000 → 100 TRIỆU operations!

// ✅ Giải pháp B: Set.has() (O(n))
const blacklistedSet = new Set(blacklistedEmails); // O(m) - chỉ làm 1 lần
const validEmails = incomingEmails.filter(
  (email) => !blacklistedSet.has(email.from), // O(1) mỗi lần
);
// 💡 Tổng: O(m) + O(n) = O(n) - chỉ 101,000 operations
// 💡 Nhanh hơn ~990 lần!

// 📌 Ví dụ 4: Tìm intersection của 2 arrays
const array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const array2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14];
// ... có thể có 10,000 phần tử mỗi array

// ❌ Giải pháp A: filter + includes() (O(n × m))
const intersection = array1.filter(
  (item) => array2.includes(item), // O(m) mỗi lần
);
// 💡 Tổng: O(n × m) - với n = 10,000, m = 10,000 → 100 TRIỆU operations!

// ✅ Giải pháp B: Set.has() (O(n + m))
const array2Set = new Set(array2); // O(m)
const intersection = array1.filter(
  (item) => array2Set.has(item), // O(1) mỗi lần
);
// 💡 Tổng: O(m) + O(n) = O(n + m) - chỉ 20,000 operations
// 💡 Nhanh hơn ~5,000 lần!

// ══════════════════════════════════════════════════════════
// PATTERN 3: find() trong loop → Map.get()
// ══════════════════════════════════════════════════════════

// 📌 Ví dụ 1: Enrich data với lookup
const orders = [
  { id: 1, userId: 101, productId: 201, quantity: 2 },
  { id: 2, userId: 102, productId: 202, quantity: 1 },
  // ... 10,000 orders
];
const users = [
  { id: 101, name: 'John', email: 'john@example.com' },
  { id: 102, name: 'Jane', email: 'jane@example.com' },
  // ... 5,000 users
];
const products = [
  { id: 201, name: 'Product A', price: 100 },
  { id: 202, name: 'Product B', price: 200 },
  // ... 3,000 products
];

// ❌ Giải pháp A: find() trong map (O(n²))
const enrichedOrders = orders.map((order) => ({
  ...order,
  user: users.find((u) => u.id === order.userId), // O(m) mỗi lần
  product: products.find((p) => p.id === order.productId), // O(k) mỗi lần
}));
// 💡 Tổng: O(n × (m + k)) - với n = 10,000, m = 5,000, k = 3,000
// 💡 → 80 TRIỆU operations!

// ✅ Giải pháp B: Map.get() (O(n + m + k))
const userMap = new Map(users.map((u) => [u.id, u])); // O(m)
const productMap = new Map(products.map((p) => [p.id, p])); // O(k)
const enrichedOrders = orders.map((order) => ({
  ...order,
  user: userMap.get(order.userId), // O(1) mỗi lần
  product: productMap.get(order.productId), // O(1) mỗi lần
}));
// 💡 Tổng: O(m) + O(k) + O(n) = O(n + m + k) - chỉ 18,000 operations
// 💡 Nhanh hơn ~4,444 lần!

// 📌 Ví dụ 2: Aggregate data với lookup
const transactions = [
  { id: 1, accountId: 101, amount: 100, type: 'deposit' },
  { id: 2, accountId: 102, amount: 50, type: 'withdrawal' },
  // ... 50,000 transactions
];
const accounts = [
  { id: 101, name: 'Account A', owner: 'John' },
  { id: 102, name: 'Account B', owner: 'Jane' },
  // ... 1,000 accounts
];

// ❌ Giải pháp A: find() trong reduce (O(n²))
const accountTotals = transactions.reduce(
  (acc, transaction) => {
    const account = accounts.find((a) => a.id === transaction.accountId); // O(m) mỗi lần
    if (!acc[account.id]) {
      acc[account.id] = { name: account.name, total: 0 };
    }
    acc[account.id].total += transaction.amount;
    return acc;
  },
  {} as Record<number, { name: string; total: number }>,
);
// 💡 Tổng: O(n × m) - với n = 50,000, m = 1,000 → 50 TRIỆU operations!

// ✅ Giải pháp B: Map.get() (O(n + m))
const accountMap = new Map(accounts.map((a) => [a.id, a])); // O(m)
const accountTotals = transactions.reduce(
  (acc, transaction) => {
    const account = accountMap.get(transaction.accountId); // O(1) mỗi lần
    if (!acc[account.id]) {
      acc[account.id] = { name: account.name, total: 0 };
    }
    acc[account.id].total += transaction.amount;
    return acc;
  },
  {} as Record<number, { name: string; total: number }>,
);
// 💡 Tổng: O(m) + O(n) = O(n + m) - chỉ 51,000 operations
// 💡 Nhanh hơn ~980 lần!

// ══════════════════════════════════════════════════════════
// PATTERN 4: Multiple chains → Single reduce
// ══════════════════════════════════════════════════════════

// 📌 Ví dụ 1: Filter + map + filter + map
const data = [
  { id: 1, age: 25, active: true, category: 'A', score: 80 },
  { id: 2, age: 30, active: false, category: 'B', score: 90 },
  { id: 3, age: 35, active: true, category: 'A', score: 85 },
  // ... 20,000 items
];

// ❌ Giải pháp A: 4 lần duyệt
const result = data
  .filter((x) => x.age > 18) // Duyệt lần 1: O(n)
  .map((x) => ({ ...x, adult: true })) // Duyệt lần 2: O(m)
  .filter((x) => x.active) // Duyệt lần 3: O(m)
  .map((x) => ({ name: `User ${x.id}`, score: x.score })); // Duyệt lần 4: O(k)

// ✅ Giải pháp B: 1 lần duyệt với reduce
const result = data.reduce(
  (acc, x) => {
    if (x.age > 18 && x.active) {
      acc.push({
        name: `User ${x.id}`,
        score: x.score,
      });
    }
    return acc;
  },
  [] as Array<{ name: string; score: number }>,
);
// 💡 Chỉ duyệt 1 lần: O(n) - nhanh hơn ~75%

// 📌 Ví dụ 2: Filter + map + sort
const items = [
  { id: 1, price: 100, inStock: true, rating: 4.5 },
  { id: 2, price: 200, inStock: false, rating: 4.0 },
  { id: 3, price: 150, inStock: true, rating: 5.0 },
  // ... 30,000 items
];

// ❌ Giải pháp A: 3 lần duyệt
const topRatedInStock = items
  .filter((item) => item.inStock) // Duyệt lần 1: O(n)
  .map((item) => ({ id: item.id, price: item.price, rating: item.rating })) // Duyệt lần 2: O(m)
  .sort((a, b) => b.rating - a.rating) // Sort: O(m log m)
  .slice(0, 10); // Slice: O(1)

// ✅ Giải pháp B: 1 lần duyệt + sort chỉ top items
const topRatedInStock = items
  .reduce(
    (acc, item) => {
      if (item.inStock) {
        acc.push({ id: item.id, price: item.price, rating: item.rating });
      }
      return acc;
    },
    [] as Array<{ id: number; price: number; rating: number }>,
  )
  .sort((a, b) => b.rating - a.rating)
  .slice(0, 10);
// 💡 Vẫn phải sort, nhưng giảm số lần duyệt từ 2 → 1
// 💡 Nhanh hơn ~33% (không tính sort time)

// ══════════════════════════════════════════════════════════
// PATTERN 5: indexOf() trong loop → Set/Map
// ══════════════════════════════════════════════════════════

// 📌 Ví dụ 1: Check duplicate với indexOf
const numbers = [1, 2, 3, 2, 4, 3, 5, 1, 6, 2, 7, 3];
// ... có thể có 100,000 số

// ❌ Giải pháp A: filter + indexOf (O(n²))
const unique = numbers.filter(
  (num, index) => numbers.indexOf(num) === index, // O(n) mỗi lần
);
// 💡 Tổng: O(n²) - với n = 100,000 → 10 TỶ operations!

// ✅ Giải pháp B: Set (O(n))
const unique = [...new Set(numbers)];
// 💡 Tổng: O(n) - chỉ 100,000 operations
// 💡 Nhanh hơn ~100,000 lần!

// 📌 Ví dụ 2: Remove items từ array
const allItems = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const itemsToRemove = [2, 4, 6, 8];
// ... có thể có 50,000 items và 10,000 items to remove

// ❌ Giải pháp A: filter + indexOf (O(n × m))
const remainingItems = allItems.filter(
  (item) => itemsToRemove.indexOf(item) === -1, // O(m) mỗi lần
);
// 💡 Tổng: O(n × m) - với n = 50,000, m = 10,000 → 500 TRIỆU operations!

// ✅ Giải pháp B: Set.has() (O(n + m))
const itemsToRemoveSet = new Set(itemsToRemove); // O(m)
const remainingItems = allItems.filter(
  (item) => !itemsToRemoveSet.has(item), // O(1) mỗi lần
);
// 💡 Tổng: O(m) + O(n) = O(n + m) - chỉ 60,000 operations
// 💡 Nhanh hơn ~8,333 lần!

// ══════════════════════════════════════════════════════════
// PATTERN 6: Tổng hợp các pattern trên
// ══════════════════════════════════════════════════════════

// 📌 Ví dụ thực tế: Process orders với nhiều lookups
const orders = [
  { id: 1, userId: 101, productIds: [201, 202], status: 'pending' },
  { id: 2, userId: 102, productIds: [203], status: 'completed' },
  // ... 10,000 orders
];
const users = [
  { id: 101, name: 'John', email: 'john@example.com', vip: true },
  { id: 102, name: 'Jane', email: 'jane@example.com', vip: false },
  // ... 5,000 users
];
const products = [
  { id: 201, name: 'Product A', price: 100, inStock: true },
  { id: 202, name: 'Product B', price: 200, inStock: false },
  { id: 203, name: 'Product C', price: 150, inStock: true },
  // ... 3,000 products
];
const allowedStatuses = ['pending', 'processing'];

// ❌ Giải pháp A: Nhiều chains + find() + includes() (RẤT CHẬM!)
const processedOrders = orders
  .filter((order) => allowedStatuses.includes(order.status)) // O(n × m)
  .map((order) => ({
    ...order,
    user: users.find((u) => u.id === order.userId), // O(n × k)
    products: order.productIds
      .map((pid) => products.find((p) => p.id === pid)) // O(n × l × j)
      .filter((p) => p && p.inStock), // O(n × l)
  }))
  .filter((order) => order.user && order.user.vip) // O(n)
  .map((order) => ({
    orderId: order.id,
    userName: order.user.name,
    productNames: order.products.map((p) => p.name), // O(n × l)
  }));
// 💡 Tổng: O(n × (m + k + l × j + l)) = O(n²) hoặc O(n³) - CỰC CHẬM!

// ✅ Giải pháp B: Map + Set + reduce (NHANH!)
const allowedStatusesSet = new Set(allowedStatuses); // O(m)
const userMap = new Map(users.map((u) => [u.id, u])); // O(k)
const productMap = new Map(products.map((p) => [p.id, p])); // O(j)

const processedOrders = orders.reduce(
  (acc, order) => {
    // Check status với Set: O(1)
    if (!allowedStatusesSet.has(order.status)) return acc;

    // Lookup user với Map: O(1)
    const user = userMap.get(order.userId);
    if (!user || !user.vip) return acc;

    // Lookup products với Map: O(l) với l = số products trong order
    const orderProducts = order.productIds
      .map((pid) => productMap.get(pid))
      .filter((p): p is NonNullable<typeof p> => p !== undefined && p.inStock);

    if (orderProducts.length === 0) return acc;

    acc.push({
      orderId: order.id,
      userName: user.name,
      productNames: orderProducts.map((p) => p.name),
    });

    return acc;
  },
  [] as Array<{ orderId: number; userName: string; productNames: string[] }>,
);
// 💡 Tổng: O(m + k + j + n × l) = O(n × l) - NHANH HƠN RẤT NHIỀU!
// 💡 Với n = 10,000, l trung bình = 2 → chỉ ~20,000 operations
// 💡 So với giải pháp A có thể lên đến hàng trăm triệu operations!

/**
 * 📊 BẢNG TỔNG KẾT TỐI ƯU HÓA:
 *
 * Tên kỹ thuật               | Cách làm cũ (Chậm) | Cách làm mới (Nhanh) | Tốc độ cải thiện
 * --------------------------|-------------------|--------------------|------------
 * Duyệt mảng                | Chạy nhiều lần    | Gộp vào 1 lần       | ~50%
 * Tìm đồ trong túi          | includes()        | Set.has()           | Cực nhiều (m lần)
 * Tra cứu thông tin         | find()            | Map.get()           | Cực nhiều (m lần)
 * Chuỗi hàm lồng nhau       | Filter + Map +... | Single reduce       | ~75%
 * Tìm trùng lặp             | indexOf()         | Dùng Set            | Nhanh gấp tỷ lần
 *
 * ✅ LƯU Ý CHO SENIOR:
 *   1. Đừng tối ưu quá sớm (Premature Optimization), chỉ làm khi thấy lag.
 *   2. Ưu tiên những đoạn code chạy trong vòng lặp lớn hoặc gọi API liên tục.
 *   3. Giữ code dễ đọc là số 1, hiệu năng là số 2 (trừ khi cần xử lý data khủng).
 */
```

---

### **10.2. Object/Array Lookups - O(n) → O(1)**

```typescript
/**
 * 🔍 LOOKUP OPTIMIZATION
 */

// ══════════════════════════════════════════════════════════
// MISTAKE 5: Array.find() for repeated lookups
// ══════════════════════════════════════════════════════════

const users = [
  { id: 1, name: 'John' },
  { id: 2, name: 'Jane' },
  // ... 10,000 users
];

// ❌ Tệ: Tốn O(n) cho mỗi lần tìm kiếm
function getUserName(userId: number) {
  const user = users.find((u) => u.id === userId); // Phải duyệt qua cả mảng
  return user?.name;
}

// Called 1000 times = O(n × m) = 10,000,000 operations!
for (let i = 0; i < 1000; i++) {
  getUserName(randomId());
}

// ✅ Good: O(1) per lookup
const userMap = new Map(users.map((u) => [u.id, u]));

function getUserName(userId: number) {
  return userMap.get(userId)?.name; // Constant time
}

// Called 1000 times = O(1 × m) = 1,000 operations
// → 10,000x faster!

// ══════════════════════════════════════════════════════════
// MISTAKE 6: Duplicate detection với includes
// ══════════════════════════════════════════════════════════

const numbers = [1, 2, 3, 2, 4, 3, 5];

// ❌ Bad: O(n²)
const unique = numbers.filter(
  (num, index) => numbers.indexOf(num) === index, // O(n) inside O(n)
);

// ✅ Good: O(n) with Set
const unique = [...new Set(numbers)];

// ✅ Alternative: O(n) with object
const unique = numbers.reduce(
  (acc, num) => {
    if (!acc.seen[num]) {
      acc.seen[num] = true;
      acc.result.push(num);
    }
    return acc;
  },
  { seen: {}, result: [] as number[] },
).result;

// ══════════════════════════════════════════════════════════
// MISTAKE 7: Object key checking
// ══════════════════════════════════════════════════════════

const config = {
  apiUrl: 'https://api.example.com',
  timeout: 5000,
  // ... 1000 properties
};

// ❌ Slow: hasOwnProperty in hot path
for (let i = 0; i < 100000; i++) {
  if (config.hasOwnProperty('apiUrl')) {
    // ...
  }
}

// ✅ Tốt: Truy cập trực tiếp (Optional chaining) - Nhanh
for (let i = 0; i < 100000; i++) {
  if (config.apiUrl !== undefined) {
    // ...
  }
}

// ✅ Tốt nhất: Dùng Map nếu key không cố định
const configMap = new Map(Object.entries(config));
configMap.has('apiUrl'); // Faster than hasOwnProperty
```

---

### **10.3. DOM Manipulation Mistakes**

```typescript
/**
 * 🌳 DOM PERFORMANCE
 */

// ══════════════════════════════════════════════════════════
// MISTAKE 8: DOM manipulation in loop
// ══════════════════════════════════════════════════════════

const items = Array.from({ length: 1000 }, (_, i) => `Item ${i}`);

// ❌ Bad: 1000 reflows/repaints
const container = document.querySelector('.container');
items.forEach((item) => {
  const div = document.createElement('div');
  div.textContent = item;
  container.appendChild(div); // Triggers reflow each time!
});

// ✅ Good: 1 reflow with DocumentFragment
const fragment = document.createDocumentFragment();
items.forEach((item) => {
  const div = document.createElement('div');
  div.textContent = item;
  fragment.appendChild(div); // No reflow
});
container.appendChild(fragment); // Single reflow

// ✅ Better: innerHTML (fastest for large lists)
container.innerHTML = items.map((item) => `<div>${item}</div>`).join('');

/**
 * Performance (1000 items):
 * • Loop + appendChild: ~150ms (1000 reflows)
 * • DocumentFragment: ~5ms (1 reflow)
 * • innerHTML: ~2ms (1 reflow)
 */

// ══════════════════════════════════════════════════════════
// MISTAKE 9: Reading layout properties in loop
// ══════════════════════════════════════════════════════════

const elements = document.querySelectorAll('.box');

// ❌ Bad: Layout thrashing (read/write interleaved)
elements.forEach((el) => {
  const height = el.offsetHeight; // Read (forces layout)
  el.style.height = height * 2 + 'px'; // Write
  // Each read forces browser to recalculate layout!
});

// ✅ Good: Batch reads, then batch writes
const heights = Array.from(elements).map((el) => el.offsetHeight); // Batch reads
elements.forEach((el, i) => {
  el.style.height = heights[i] * 2 + 'px'; // Batch writes
});

// ══════════════════════════════════════════════════════════
// MISTAKE 10: querySelector in loops
// ══════════════════════════════════════════════════════════

// ❌ Tệ: Truy vấn lại DOM ở mỗi vòng lặp (Cực chậm)
for (let i = 0; i < 1000; i++) {
  const container = document.querySelector('.container'); // Truy vấn 1000 lần!
  container.innerHTML += `<div>Item ${i}</div>`;
}

// ✅ Tốt: Lưu tham chiếu ra ngoài vòng lặp
const container = document.querySelector('.container');
let html = '';
for (let i = 0; i < 1000; i++) {
  html += `<div>Item ${i}</div>`;
}
container.innerHTML = html;
```

---

### **10.4. React-Specific Mistakes**

```typescript
/**
 * ⚛️ REACT PERFORMANCE
 */

// ══════════════════════════════════════════════════════════
// MISTAKE 11: Creating objects/arrays in render
// ══════════════════════════════════════════════════════════

// ❌ Bad: New object every render (breaks memoization)
function UserList() {
  const users = getUsers();

  return (
    <ExpensiveChild
      config={{ theme: 'dark', locale: 'en' }} // New object!
      filters={['active', 'verified']} // New array!
    />
  );
}

// ✅ Tốt: Tạo biến ở ngoài Component (Chỉ tạo 1 lần duy nhất)
const CONFIG = { theme: 'dark', locale: 'en' };
const FILTERS = ['active', 'verified'];

function UserList() {
  // Vì biến nằm ở ngoài, React thấy "đồ cũ" nên không render lại con một cách vô ích.
  return <ExpensiveChild config={CONFIG} filters={FILTERS} />;
}

// ✅ Better: useMemo for dynamic values
function UserList({ theme, showActive }) {
  const config = useMemo(() => ({ theme, locale: 'en' }), [theme]);

  const filters = useMemo(
    () => (showActive ? ['active', 'verified'] : ['verified']),
    [showActive]
  );

  return <ExpensiveChild config={config} filters={filters} />;
}

// ══════════════════════════════════════════════════════════
// MISTAKE 12: Inline functions as props
// ══════════════════════════════════════════════════════════

// ❌ Tệ: Tạo hàm mới ở mỗi lần render (Gây re-render con không cần thiết)
function TodoList({ todos }) {
  return (
    <div>
      {todos.map((todo) => (
        <TodoItem
          key={todo.id}
          todo={todo}
          onDelete={() => deleteTodo(todo.id)} // Hàm mới được tạo ra liên tục!
        />
      ))}
    </div>
  );
}

// ✅ Tốt: Dùng useCallback hoặc truyền ID xuống dưới
function TodoList({ todos }) {
  const handleDelete = useCallback((id: number) => {
    deleteTodo(id);
  }, []);

  return (
    <div>
      {todos.map((todo) => (
        <TodoItem
          key={todo.id}
          todo={todo}
          onDelete={handleDelete}
          todoId={todo.id}
        />
      ))}
    </div>
  );
}

// ══════════════════════════════════════════════════════════
// MISTAKE 13: Index as key in dynamic lists
// ══════════════════════════════════════════════════════════

const [items, setItems] = useState(['A', 'B', 'C']);

// ❌ Bad: Index as key (breaks when reordering/removing)
items.map((item, index) => (
  <div key={index}>{item}</div> // React can't track items properly!
));

// When item removed:
// Before: [0: 'A', 1: 'B', 2: 'C']
// After:  [0: 'A', 1: 'C']
// React thinks item at index 2 was removed, but it was 'B'!

// ✅ Tốt: Dùng ID duy nhất và cố định (như số CMND)
// Dù có xóa hay đảo lộn, 'B' vẫn là 'B', React biết chính xác cái nào vừa biến mất.
items.map((item) => <div key={item.id}>{item.name}</div>);

// ══════════════════════════════════════════════════════════
// MISTAKE 14: Not memoizing expensive calculations
// ══════════════════════════════════════════════════════════

function DataTable({ data, filter }) {
  // ❌ Bad: Recalculates every render (even when data unchanged)
  const sortedData = data
    .filter((item) => item.status === filter)
    .sort((a, b) => a.name.localeCompare(b.name));

  return <Table data={sortedData} />;
}

// ✅ Tốt: Memoize tính toán (Ghi nhớ kết quả)
function DataTable({ data, filter }) {
  const sortedData = useMemo(() => {
    return data
      .filter((item) => item.status === filter)
      .sort((a, b) => a.name.localeCompare(b.name));
  }, [data, filter]); // Chỉ tính lại khi data hoặc filter thay đổi

  return <Table data={sortedData} />;
}
```

---

### **10.5. State Management Mistakes**

```typescript
/**
 * 📦 STATE MANAGEMENT
 */

// ══════════════════════════════════════════════════════════
// MISTAKE 15: Derived state instead of computation
// ══════════════════════════════════════════════════════════

// ❌ Tệ: Sao chép state (Dư thừa, dễ lỗi khi user thay đổi)
function UserProfile({ user }) {
  const [fullName, setFullName] = useState('');

  useEffect(() => {
    setFullName(`${user.firstName} ${user.lastName}`);
  }, [user]);

  return <div>{fullName}</div>;
}

// ✅ Tốt: Tính toán trực tiếp khi render (Derived state)
function UserProfile({ user }) {
  const fullName = `${user.firstName} ${user.lastName}`;
  return <div>{fullName}</div>;
}

// ✅ With memoization if expensive
function UserProfile({ user }) {
  const fullName = useMemo(
    () => `${user.firstName} ${user.lastName}`,
    [user.firstName, user.lastName]
  );
  return <div>{fullName}</div>;
}

// ══════════════════════════════════════════════════════════
// MISTAKE 16: Unnecessary state updates
// ══════════════════════════════════════════════════════════

// ❌ Bad: Updates state even when value unchanged
function Counter() {
  const [count, setCount] = useState(0);

  const increment = () => {
    setCount(count + 1); // Always triggers re-render
  };

  return <button onClick={increment}>{count}</button>;
}

// Nếu count đang là 5 và bạn set lại là 5, React vẫn re-render!

// ✅ Tốt: Dùng functional update hoặc kiểm tra trước khi set
function Counter() {
  const [count, setCount] = useState(0);

  const increment = () => {
    setCount((prev) => prev + 1); // Functional update
  };

  const setValue = (newValue: number) => {
    setCount((prev) => {
      if (prev === newValue) return prev; // Bail out
      return newValue;
    });
  };

  return <button onClick={increment}>{count}</button>;
}

// ══════════════════════════════════════════════════════════
// MISTAKE 17: Deep object updates (mutation)
// ══════════════════════════════════════════════════════════

const [user, setUser] = useState({
  profile: { name: 'John', address: { city: 'NYC' } },
});

// ❌ Tệ: Đột biến trực tiếp (Mutation) -> React không biết để re-render
const updateCity = (city: string) => {
  user.profile.address.city = city; // Sai lầm tai hại!
  setUser(user); // Cùng tham chiếu object cũ, React sẽ lờ đi
};

// ✅ Tốt: Cập nhật bất biến (Immutable update)
const updateCity = (city: string) => {
  setUser((prev) => ({
    ...prev,
    profile: {
      ...prev.profile,
      address: {
        ...prev.profile.address,
        city,
      },
    },
  }));
};

// ✅ Better: Use Immer
import { produce } from 'immer';

const updateCity = (city: string) => {
  setUser(
    produce((draft) => {
      draft.profile.address.city = city; // Looks like mutation, but immutable!
    })
  );
};
```

---

### **10.6. Async/Promise Mistakes**

```typescript
/**
 * ⏳ ASYNC OPERATIONS
 */

// ══════════════════════════════════════════════════════════
// MISTAKE 18: Sequential awaits (should be parallel)
// ══════════════════════════════════════════════════════════

// ❌ Tệ: Chạy tuần tự (Mất tổng cộng 3 giây)
async function fetchData() {
  const users = await fetchUsers(); // Đợi 1s
  const posts = await fetchPosts(); // Đợi thêm 1s
  const comments = await fetchComments(); // Đợi thêm 1s nữa -> Tổng 3s

  return { users, posts, comments };
}

// ✅ Tốt: Chạy song song (Chỉ mất 1 giây cho cả 3)
async function fetchData() {
  const [users, posts, comments] = await Promise.all([
    fetchUsers(), // All start together
    fetchPosts(),
    fetchComments(),
  ]);

  return { users, posts, comments };
}

/**
 * 📊 SO SÁNH HIỆU NĂNG:
 * • Chạy tuần tự (Sequential): 3 giây (Đợi xong món này mới nấu món kia)
 * • Chạy song song (Parallel): Chỉ mất 1 giây (Bật 3 bếp nấu cùng lúc)
 * → Tốc độ nhanh gấp 3 lần!
 */

// ══════════════════════════════════════════════════════════
// MISTAKE 19: Promise in loop (sequential)
// ══════════════════════════════════════════════════════════

const userIds = [1, 2, 3, 4, 5];

// ❌ Tệ: Lại chạy tuần tự trong vòng lặp (5 giây)
const users = [];
for (const id of userIds) {
  const user = await fetchUser(id); // Chờ từng người một
  users.push(user);
}

// ✅ Tốt: Chạy song song tất cả (1 giây)
const users = await Promise.all(userIds.map((id) => fetchUser(id)));

// ══════════════════════════════════════════════════════════
// MISTAKE 20: Not handling promise rejections
// ══════════════════════════════════════════════════════════

// ❌ Bad: Unhandled rejection crashes app
fetchData(); // If rejects, app crashes in production!

// ✅ Good: Always handle errors
fetchData()
  .then((data) => console.log(data))
  .catch((error) => console.error('Failed:', error));

// ✅ Better: Try/catch with async/await
async function loadData() {
  try {
    const data = await fetchData();
    console.log(data);
  } catch (error) {
    console.error('Failed:', error);
    // Show error UI, retry, etc.
  }
}

// ✅ Global handler (last resort)
window.addEventListener('unhandledrejection', (event) => {
  console.error('Unhandled rejection:', event.reason);
  logToErrorService(event.reason);
});
```

---

### **10.7. Memory Leak Patterns**

```typescript
/**
 * 💧 MEMORY LEAKS
 */

// ══════════════════════════════════════════════════════════
// MISTAKE 21: Not cleaning up event listeners
// ══════════════════════════════════════════════════════════

// ❌ Bad: Memory leak in React
function Component() {
  useEffect(() => {
    const handleScroll = () => console.log('Scrolled');

    window.addEventListener('scroll', handleScroll);
    // Missing cleanup! Listener persists after unmount
  }, []);

  return <div>Content</div>;
}

// ✅ Good: Clean up on unmount
function Component() {
  useEffect(() => {
    const handleScroll = () => console.log('Scrolled');

    window.addEventListener('scroll', handleScroll);

    // Dọn dẹp trả lại bộ nhớ khi component bị hủy
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  return <div>Content</div>;
}

// ══════════════════════════════════════════════════════════
// MISTAKE 22: Uncanceled timers/intervals
// ══════════════════════════════════════════════════════════

// ❌ Bad: Timer keeps running after unmount
function Component() {
  useEffect(() => {
    setInterval(() => {
      console.log('Tick');
    }, 1000);
    // Interval never cleared!
  }, []);

  return <div>Content</div>;
}

// ✅ Good: Clear on unmount
function Component() {
  useEffect(() => {
    const intervalId = setInterval(() => {
      console.log('Tick');
    }, 1000);

    return () => clearInterval(intervalId);
  }, []);

  return <div>Content</div>;
}

// ══════════════════════════════════════════════════════════
// MISTAKE 23: Closures holding large objects
// ══════════════════════════════════════════════════════════

// ❌ Bad: Closure keeps entire array in memory
function createHandler(items: LargeObject[]) {
  return () => {
    console.log(items.length); // Only needs length, but keeps all items!
  };
}

// ✅ Tốt: Chỉ lấy những gì cần thiết
function createHandler(items: LargeObject[]) {
  const length = items.length; // Chỉ lưu số lượng

  return () => {
    console.log(length);
  };
}
```

---

### **10.8. Bundle Size Mistakes**

```typescript
/**
 * 📦 BUNDLE OPTIMIZATION
 */

// ══════════════════════════════════════════════════════════
// MISTAKE 24: Importing entire library
// ══════════════════════════════════════════════════════════

// ❌ Bad: Imports entire lodash (~70KB)
import _ from 'lodash';
_.debounce(fn, 300);

// ✅ Good: Import only what you need
import debounce from 'lodash/debounce'; // ~2KB

// ✅ Better: Use tree-shakeable library
import { debounce } from 'lodash-es'; // Tree-shaking works

// ══════════════════════════════════════════════════════════
// MISTAKE 25: Not using dynamic imports
// ══════════════════════════════════════════════════════════

// ❌ Bad: Heavy chart library loaded upfront
import { Chart } from 'heavy-chart-library'; // 500KB

function Dashboard() {
  const [showChart, setShowChart] = useState(false);

  return (
    <div>
      <button onClick={() => setShowChart(true)}>Show Chart</button>
      {showChart && <Chart data={data} />}
    </div>
  );
}

// ✅ Tốt: Lazy load (Chỉ tải khi cần dùng tới)
const Chart = lazy(() => import('heavy-chart-library'));

function Dashboard() {
  const [showChart, setShowChart] = useState(false);

  return (
    <div>
      <button onClick={() => setShowChart(true)}>Show Chart</button>
      {showChart && (
        <Suspense fallback={<Loading />}>
          <Chart data={data} />
        </Suspense>
      )}
    </div>
  );
}

/**
 * 📦 TỐI ƯU KÍCH THƯỚC FILE:
 * • Trước: Tải cả cục 500KB ngay từ đầu (Dù chưa chắc user có xem biểu đồ không)
 * • Sau: Chỉ tải 500KB đó KHI NÀO user bấm nút "Show Chart".
 * → Trang web hiện lên nhanh hơn hẳn vì bớt được 500KB "nặng nợ".
 */

// ══════════════════════════════════════════════════════════
// MISTAKE 26: Moment.js (huge bundle)
// ══════════════════════════════════════════════════════════

// ❌ Bad: Moment.js is 230KB (with locales)
import moment from 'moment';
moment().format('YYYY-MM-DD');

// ✅ Good: date-fns (tree-shakeable, 2-5KB)
import { format } from 'date-fns';
format(new Date(), 'yyyy-MM-dd');

// ✅ Alternative: Day.js (2KB, moment-compatible API)
import dayjs from 'dayjs';
dayjs().format('YYYY-MM-DD');
```

---

### **10.9. Performance Checklist**

```typescript
/**
 * ✅ PERFORMANCE OPTIMIZATION CHECKLIST
 */

const performanceChecklist = {
  // Array Operations
  '❌ filter + map': 'Use reduce or for loop',
  '❌ find in loop': 'Use Map for O(1) lookup',
  '❌ includes in loop': 'Use Set for O(1) lookup',
  '❌ Multiple iterations': 'Combine into single reduce',

  // DOM Manipulation
  '❌ DOM query in loop': 'Cache reference outside loop',
  '❌ appendChild in loop': 'Use DocumentFragment or innerHTML',
  '❌ Layout thrashing': 'Batch reads, then batch writes',
  '❌ querySelector repeatedly': 'Cache elements',

  // React
  '❌ Object/array in render': 'useMemo or move outside',
  '❌ Inline functions': 'useCallback for memoized children',
  '❌ Index as key': 'Use stable unique ID',
  '❌ Expensive calc in render': 'useMemo',
  '❌ Derived state': 'Compute during render',

  // Async
  '❌ Sequential awaits': 'Promise.all for parallel',
  '❌ await in loop': 'Promise.all + map',
  '❌ Unhandled rejections': 'Always .catch() or try/catch',

  // Memory
  '❌ Event listeners': 'Clean up in useEffect return',
  '❌ Timers/intervals': 'Clear on unmount',
  '❌ Large closures': 'Extract only needed values',

  // Bundle
  '❌ Import entire library': 'Import specific functions',
  '❌ Heavy components upfront': 'React.lazy() + Suspense',
  '❌ Moment.js': 'Use date-fns or dayjs',

  // General
  '❌ O(n²) algorithms': 'Use Map/Set for O(n)',
  '❌ Premature optimization': 'Profile first, then optimize',
  '❌ No monitoring': 'Use Lighthouse, Web Vitals',
};

/**
 * 🎯 Quick Wins (High Impact, Low Effort):
 *
 * 1. Replace filter + map with reduce
 * 2. Use Map/Set instead of find/includes in loops
 * 3. Cache DOM references
 * 4. Add React.memo to expensive components
 * 5. Use Promise.all instead of sequential awaits
 * 6. Lazy load heavy libraries
 * 7. Clean up event listeners/timers
 * 8. Replace moment.js with date-fns
 *
 * Before optimizing:
 * • Profile with Chrome DevTools
 * • Measure with Lighthouse
 * • Monitor with Web Vitals
 * • Don't guess, measure!
 */
```

---

## **XI. CSS Architecture & Modern Patterns**

### **11.1. CSS-in-JS vs CSS Modules vs Tailwind**

```typescript
/**
 * 🎨 CSS APPROACHES COMPARISON
 */

// ══════════════════════════════════════════════════════════
// 1. STYLED COMPONENTS (CSS-in-JS)
// ══════════════════════════════════════════════════════════

import styled from 'styled-components';

// ✅ Pros: Scoped, dynamic, TypeScript support
const Button = styled.button<{ $primary?: boolean }>`
  background: ${props => props.$primary ? '#007bff' : '#6c757d'};
  color: white;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;

  &:hover {
    opacity: 0.9;
  }

  @media (max-width: 768px) {
    padding: 0.25rem 0.5rem;
  }
`;

// Usage
<Button $primary>Click me</Button>

// ❌ Cons: Runtime overhead, larger bundle, no static extraction

// ══════════════════════════════════════════════════════════
// 2. CSS MODULES
// ══════════════════════════════════════════════════════════

// styles.module.css
.button {
  background: #6c757d;
  color: white;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
}

.button:hover {
  opacity: 0.9;
}

.button.primary {
  background: #007bff;
}

// Component.tsx
import styles from './styles.module.css';

function Component() {
  return (
    <button className={`${styles.button} ${styles.primary}`}>
      Click me
    </button>
  );
}

// ✅ Pros: Zero runtime, scoped, familiar CSS syntax
// ❌ Cons: No dynamic styles, separate file, limited TypeScript

// ══════════════════════════════════════════════════════════
// 3. TAILWIND CSS
// ══════════════════════════════════════════════════════════

// ✅ Pros: Utility-first, fast development, tiny bundle (with PurgeCSS)
function Component() {
  return (
    <button className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded">
      Click me
    </button>
  );
}

// Dynamic styles with template literals
function Component({ isPrimary }) {
  return (
    <button className={`
      px-4 py-2 rounded text-white
      ${isPrimary ? 'bg-blue-500 hover:bg-blue-600' : 'bg-gray-500 hover:bg-gray-600'}
    `}>
      Click me
    </button>
  );
}

// ❌ Cons: HTML becomes cluttered, learning curve, not semantic

// ══════════════════════════════════════════════════════════
// DECISION MATRIX
// ══════════════════════════════════════════════════════════

/**
 * Use Styled Components when:
 * • Need dynamic theming
 * • Complex component variants
 * • TypeScript-first project
 * • Don't care about bundle size
 *
 * Use CSS Modules when:
 * • Want familiar CSS syntax
 * • Zero runtime overhead needed
 * • Migrating from traditional CSS
 * • Server-side rendering (SSR)
 *
 * Use Tailwind when:
 * • Rapid prototyping
 * • Design system consistency
 * • Small bundle size critical
 * • Team prefers utility-first
 */
```

---

### **11.2. CSS Performance Patterns**

```typescript
/**
 * ⚡ CSS OPTIMIZATION
 */

// ══════════════════════════════════════════════════════════
// CRITICAL CSS (Above-the-fold)
// ══════════════════════════════════════════════════════════

// Inline critical CSS in <head>
<head>
  <style>
    /* Only styles for above-the-fold content */
    .header { /* ... */ }
    .hero { /* ... */ }
  </style>

  {/* Load full CSS asynchronously */}
  <link
    rel="preload"
    href="/styles.css"
    as="style"
    onLoad="this.onload=null;this.rel='stylesheet'"
  />
</head>

// ══════════════════════════════════════════════════════════
// AVOID EXPENSIVE CSS SELECTORS
// ══════════════════════════════════════════════════════════

/* ❌ Slow: Universal selector */
* {
  box-sizing: border-box;
}

/* ✅ Better: Scoped */
.container * {
  box-sizing: border-box;
}

/* ❌ Slow: Deep nesting */
.header .nav ul li a span {
  color: blue;
}

/* ✅ Fast: Flat selectors with BEM */
.nav__link-text {
  color: blue;
}

/* ❌ Slow: Attribute selectors */
[class*="col-"] {
  float: left;
}

/* ✅ Fast: Class selectors */
.col {
  float: left;
}

// ══════════════════════════════════════════════════════════
// CSS CONTAINMENT
// ══════════════════════════════════════════════════════════

.widget {
  /* Isolate this element's layout/paint from rest of page */
  contain: layout paint;
}

.sidebar {
  /* Even stronger isolation */
  contain: strict;
}

/* Performance gain: Browser doesn't recalculate entire page */

// ══════════════════════════════════════════════════════════
// CONTENT-VISIBILITY (Lazy render)
// ══════════════════════════════════════════════════════════

.lazy-section {
  /* Don't render until scrolled into view */
  content-visibility: auto;
  /* Reserve space to avoid layout shift */
  contain-intrinsic-size: 0 500px;
}

/**
 * Performance comparison (10 sections):
 * • Without content-visibility: ~200ms initial render
 * • With content-visibility: ~50ms initial render
 * → 4x faster initial load!
 */
```

---

## **XII. Web Security Deep Dive**

### **12.1. XSS Prevention Strategies**

```typescript
/**
 * 🛡️ XSS ATTACK VECTORS & PREVENTION
 */

// ══════════════════════════════════════════════════════════
// REFLECTED XSS
// ══════════════════════════════════════════════════════════

// ❌ Nguy hiểm: Chèn trực tiếp input của user vào HTML
// Nếu user nhập: <script>alert('Bị hack rồi!')</script> -> Web bạn sẽ chạy script đó ngay!
document.body.innerHTML = `<h1>Results for: ${searchQuery}</h1>`;

// ✅ Fix 1: Use textContent
document.querySelector('h1').textContent = `Results for: ${searchQuery}`;

// ✅ Fix 2: Sanitize with DOMPurify
import DOMPurify from 'dompurify';
document.body.innerHTML = DOMPurify.sanitize(
  `<h1>Results for: ${searchQuery}</h1>`
);

// ══════════════════════════════════════════════════════════
// STORED XSS
// ══════════════════════════════════════════════════════════

// ❌ Lỗ hổng: Input của user được lưu và render lại mà không qua xử lý
const comment = await fetchComment(); // Lấy từ database
element.innerHTML = comment.text; // XSS nếu comment chứa thẻ <script>

// ✅ Fix: Sanitize (làm sạch) trước khi hiển thị
element.innerHTML = DOMPurify.sanitize(comment.text);

// ✅ Tốt hơn: Sanitize ngay từ server trước khi lưu
// Validate ở Backend + Sanitize

// ══════════════════════════════════════════════════════════
// DOM-BASED XSS
// ══════════════════════════════════════════════════════════

// ❌ Lỗ hổng: Sử dụng eval() hoặc Function() (Cấm kỵ!)
const userCode = getUserInput();
eval(userCode); // Đừng bao giờ làm thế này!

// ❌ Lỗ hổng: innerHTML với dữ liệu từ user
const name = location.hash.slice(1);
element.innerHTML = `<div>Hello ${name}</div>`;

// ✅ Fix: Sử dụng các phương thức DOM an toàn
const div = document.createElement('div');
div.textContent = `Hello ${name}`;
element.appendChild(div);

// ══════════════════════════════════════════════════════════
// CSP (Content Security Policy)
// ══════════════════════════════════════════════════════════

// Set CSP headers on server
// Content-Security-Policy:
//   default-src 'self';
//   script-src 'self' https://trusted-cdn.com;
//   style-src 'self' 'unsafe-inline';
//   img-src 'self' data: https:;
//   connect-src 'self' https://api.example.com;

// React Helmet for CSP meta tag
<Helmet>
  <meta
    http-equiv="Content-Security-Policy"
    content="default-src 'self'; script-src 'self' https://trusted-cdn.com"
  />
</Helmet>;
```

---

### **12.2. CSRF Protection**

```typescript
/**
 * 🔐 CSRF ATTACK & PREVENTION
 */

// ══════════════════════════════════════════════════════════
// ATTACK SCENARIO
// ══════════════════════════════════════════════════════════

/**
 * KỊCH BẢN TẤN CÔNG:
 * User đang đăng nhập bank.com.
 * Kẻ xấu gửi email chứa một tấm ảnh "ma ma":
 * <img src="https://bank.com/transfer?to=ke-xau&amount=1000">
 *
 * Trình duyệt tự động gửi kèm Cookie đăng nhập -> Tiền bay màu!
 */

// ══════════════════════════════════════════════════════════
// PREVENTION 1: CSRF Token
// ══════════════════════════════════════════════════════════

// Server generates token per session/request
// Backend sets token in cookie or meta tag

// ✅ Gửi kèm token trong mọi request thay đổi dữ liệu (POST, PUT, DELETE)
const csrfToken = document.querySelector('meta[name="csrf-token"]')?.content;

fetch('/api/transfer', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-CSRF-Token': csrfToken,
  },
  body: JSON.stringify({ to: 'recipient', amount: 1000 }),
});

// Server sẽ kiểm tra token có khớp với session của user không

// ══════════════════════════════════════════════════════════
// PREVENTION 2: SameSite Cookies
// ══════════════════════════════════════════════════════════

// Set-Cookie: session=abc123; SameSite=Strict; Secure; HttpOnly

/**
 * SameSite values:
 * • Strict: Cookie only sent on same-site requests
 * • Lax: Cookie sent on top-level navigation (default)
 * • None: Cookie sent on all requests (requires Secure)
 */

// ══════════════════════════════════════════════════════════
// PREVENTION 3: Custom Headers
// ══════════════════════════════════════════════════════════

// Các request đơn giản (GET, POST dạng form) tự động gửi cookie
// Nhưng custom headers yêu cầu preflight (CORS), hacker không thể giả mạo dễ dàng

fetch('/api/transfer', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest', // Header tự chế
  },
  body: JSON.stringify({ to: 'recipient', amount: 1000 }),
});

// Server kiểm tra sự tồn tại của header này
```

---

### **12.3. Authentication Best Practices**

```typescript
/**
 * 🔑 SECURE AUTHENTICATION
 */

// ══════════════════════════════════════════════════════════
// JWT vs SESSION COOKIES
// ══════════════════════════════════════════════════════════

// ❌ JWT lưu trong localStorage (Dễ bị XSS đánh cắp)
localStorage.setItem('token', jwt);

fetch('/api/protected', {
  headers: {
    Authorization: `Bearer ${localStorage.getItem('token')}`,
  },
});

// ✅ HttpOnly cookies (An toàn với XSS vì JS không đọc được)
// Server set: Set-Cookie: session=abc123; HttpOnly; Secure; SameSite=Strict

fetch('/api/protected', {
  credentials: 'include', // Tự động gửi cookie đi kèm
});

// ══════════════════════════════════════════════════════════
// REFRESH TOKEN PATTERN
// ══════════════════════════════════════════════════════════

// Access token: Short-lived (15 minutes), in memory
// Refresh token: Long-lived (7 days), HttpOnly cookie

let accessToken: string | null = null;

async function refreshAccessToken() {
  const response = await fetch('/api/refresh', {
    method: 'POST',
    credentials: 'include', // Sends refresh token cookie
  });

  const { accessToken: newToken } = await response.json();
  accessToken = newToken;
  return newToken;
}

// Axios interceptor for auto-refresh
axios.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      try {
        const token = await refreshAccessToken();
        originalRequest.headers.Authorization = `Bearer ${token}`;
        return axios(originalRequest);
      } catch (refreshError) {
        // Redirect to login
        window.location.href = '/login';
        return Promise.reject(refreshError);
      }
    }

    return Promise.reject(error);
  },
);

// ══════════════════════════════════════════════════════════
// PASSWORD SECURITY
// ══════════════════════════════════════════════════════════

// ✅ Validate ở phía Client (Tăng trải nghiệm UX)
function validatePassword(password: string) {
  const errors = [];

  if (password.length < 12) {
    errors.push('Minimum 12 characters');
  }

  if (!/[A-Z]/.test(password)) {
    errors.push('At least one uppercase letter');
  }

  if (!/[a-z]/.test(password)) {
    errors.push('At least one lowercase letter');
  }

  if (!/[0-9]/.test(password)) {
    errors.push('At least one number');
  }

  if (!/[^A-Za-z0-9]/.test(password)) {
    errors.push('At least one special character');
  }

  // Check against common passwords
  if (commonPasswords.includes(password.toLowerCase())) {
    errors.push('Password too common');
  }

  return errors;
}

// ✅ Hash mật khẩu ở Backend (TUYỆT ĐỐI không lưu mật khẩu dạng chữ rõ!)
// Dùng thư viện như bcrypt để "mã hóa" mật khẩu thành một chuỗi không ai đọc được.
// const hash = await bcrypt.hash(password, 12);
```

---

## **XIII. React Performance Patterns**

### **13.1. Virtual Scrolling (Large Lists)**

```typescript
/**
 * 📜 VIRTUAL SCROLLING
 */

// ❌ Vấn đề: Render 10.000 items = Rất chậm
function BadList({ items }) {
  return (
    <div>
      {items.map((item) => (
        <div key={item.id} style={{ height: 50 }}>
          {item.name}
        </div>
      ))}
    </div>
  );
}

// ✅ Solution: react-window (virtual scrolling)
import { FixedSizeList } from 'react-window';

function VirtualList({ items }) {
  const Row = ({ index, style }) => (
    <div style={style}>{items[index].name}</div>
  );

  return (
    <FixedSizeList
      height={600}
      itemCount={items.length}
      itemSize={50}
      width="100%"
    >
      {Row}
    </FixedSizeList>
  );
}

/**
 * HIỆU NĂNG (Ghi chú Senior):
 * • Render kiểu cũ: Mất 500ms, tạo 10.000 thẻ div (Làm trình duyệt đuối sức).
 * • Virtual scroll: Chỉ mất 50ms, chỉ tạo ~15 thẻ div (Chỉ hiện cái user thấy).
 * → Tiết kiệm 99% tài nguyên, web mượt như lụa!
 */
```

---

### **13.2. Code Splitting Strategies**

```typescript
/**
 * 📦 CODE SPLITTING
 */

// ══════════════════════════════════════════════════════════
// 1. ROUTE-BASED SPLITTING
// ══════════════════════════════════════════════════════════

import { lazy, Suspense } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

// Lazy load routes
const Home = lazy(() => import('./pages/Home'));
const Dashboard = lazy(() => import('./pages/Dashboard'));
const Settings = lazy(() => import('./pages/Settings'));

function App() {
  return (
    <BrowserRouter>
      <Suspense fallback={<LoadingSpinner />}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/settings" element={<Settings />} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
}

// ══════════════════════════════════════════════════════════
// 2. COMPONENT-BASED SPLITTING
// ══════════════════════════════════════════════════════════

const HeavyChart = lazy(() => import('./components/HeavyChart'));

function Dashboard() {
  const [showChart, setShowChart] = useState(false);

  return (
    <div>
      <button onClick={() => setShowChart(true)}>Show Chart</button>

      {showChart && (
        <Suspense fallback={<ChartSkeleton />}>
          <HeavyChart data={data} />
        </Suspense>
      )}
    </div>
  );
}

// ══════════════════════════════════════════════════════════
// 3. LIBRARY SPLITTING
// ══════════════════════════════════════════════════════════

// ❌ Bad: Import everything
import moment from 'moment';
import 'moment/locale/vi';

// ✅ Good: Dynamic import when needed
async function formatDate(date: Date, locale: string) {
  const moment = await import('moment');

  if (locale !== 'en') {
    await import(`moment/locale/${locale}`);
  }

  return moment.default(date).locale(locale).format('LL');
}
```

---

### **13.3. Web Workers for Heavy Computation**

```typescript
/**
 * 👷 WEB WORKERS
 */

// ══════════════════════════════════════════════════════════
// PROBLEM: Heavy computation blocks UI
// ══════════════════════════════════════════════════════════

function Component() {
  const [result, setResult] = useState(null);

  const handleCalculate = () => {
    // ❌ Làm treo UI thread trong 5 giây (User không bấm gì được)
    const result = heavyComputation(largeDataset);
    setResult(result);
  };

  return <button onClick={handleCalculate}>Calculate</button>;
}

// ══════════════════════════════════════════════════════════
// SOLUTION: Offload to Web Worker
// ══════════════════════════════════════════════════════════

// worker.ts
self.addEventListener('message', (e) => {
  const result = heavyComputation(e.data);
  self.postMessage(result);
});

// Component.tsx
function Component() {
  const [result, setResult] = useState(null);
  const workerRef = useRef<Worker>();

  useEffect(() => {
    workerRef.current = new Worker(new URL('./worker.ts', import.meta.url));

    workerRef.current.onmessage = (e) => {
      setResult(e.data);
    };

    return () => workerRef.current?.terminate();
  }, []);

  const handleCalculate = () => {
    // ✅ Không chặn UI: Giao diện vẫn mượt mà
    workerRef.current?.postMessage(largeDataset);
  };

  return <button onClick={handleCalculate}>Calculate</button>;
}

// ══════════════════════════════════════════════════════════
// COMLINK (Easier API)
// ══════════════════════════════════════════════════════════

import { wrap } from 'comlink';

// worker.ts
import { expose } from 'comlink';

const api = {
  async processData(data: any[]) {
    return heavyComputation(data);
  },
};

expose(api);

// Component.tsx
const worker = wrap<typeof api>(
  new Worker(new URL('./worker.ts', import.meta.url))
);

async function handleCalculate() {
  const result = await worker.processData(largeDataset);
  setResult(result);
}
```

---

## **XIV. Testing Strategies**

### **14.1. Unit Testing Best Practices**

```typescript
/**
 * 🧪 UNIT TESTING
 */

// ══════════════════════════════════════════════════════════
// REACT TESTING LIBRARY
// ══════════════════════════════════════════════════════════

import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

// ✅ Good: Test behavior, not implementation
describe('LoginForm', () => {
  it('submits form with user credentials', async () => {
    const handleSubmit = jest.fn();
    const user = userEvent.setup();

    render(<LoginForm onSubmit={handleSubmit} />);

    // Tìm element bằng role/label (giống cách user dùng)
    await user.type(screen.getByLabelText(/email/i), 'user@example.com');
    await user.type(screen.getByLabelText(/password/i), 'password123');
    await user.click(screen.getByRole('button', { name: /login/i }));

    // Khẳng định hành vi (Assert behavior)
    await waitFor(() => {
      expect(handleSubmit).toHaveBeenCalledWith({
        email: 'user@example.com',
        password: 'password123',
      });
    });
  });

  it('shows validation errors', async () => {
    render(<LoginForm />);

    const user = userEvent.setup();
    await user.click(screen.getByRole('button', { name: /login/i }));

    expect(screen.getByText(/email is required/i)).toBeInTheDocument();
    expect(screen.getByText(/password is required/i)).toBeInTheDocument();
  });
});

// ❌ Tệ: Test chi tiết cài đặt (Implementation details)
it('updates state on input change', () => {
  const { container } = render(<LoginForm />);
  const input = container.querySelector('input[name="email"]');

  fireEvent.change(input, { target: { value: 'test@example.com' } });

  // Đừng test state trực tiếp! Nếu đổi tên state test sẽ tạch
  expect(wrapper.state('email')).toBe('test@example.com');
});

// ══════════════════════════════════════════════════════════
// MOCKING API CALLS
// ══════════════════════════════════════════════════════════

import { rest } from 'msw';
import { setupServer } from 'msw/node';

const server = setupServer(
  rest.get('/api/users', (req, res, ctx) => {
    return res(
      ctx.json([
        { id: 1, name: 'John' },
        { id: 2, name: 'Jane' },
      ])
    );
  })
);

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

it('fetches and displays users', async () => {
  render(<UserList />);

  expect(screen.getByText(/loading/i)).toBeInTheDocument();

  await waitFor(() => {
    expect(screen.getByText('John')).toBeInTheDocument();
    expect(screen.getByText('Jane')).toBeInTheDocument();
  });
});

// ══════════════════════════════════════════════════════════
// SNAPSHOT TESTING
// ══════════════════════════════════════════════════════════

it('renders correctly', () => {
  const { container } = render(<Button>Click me</Button>);
  expect(container.firstChild).toMatchSnapshot();
});

// ✅ Dùng cho: Component tĩnh, UI phức tạp ít thay đổi
// ❌ Tránh dùng cho: Nội dung động, thay đổi thường xuyên
```

---

### **14.2. E2E Testing with Playwright**

```typescript
/**
 * 🎭 E2E TESTING
 */

import { test, expect } from '@playwright/test';

// ══════════════════════════════════════════════════════════
// BASIC E2E TEST
// ══════════════════════════════════════════════════════════

test('user can login and view dashboard', async ({ page }) => {
  // Navigate
  await page.goto('https://app.example.com');

  // Fill login form
  await page.fill('input[name="email"]', 'user@example.com');
  await page.fill('input[name="password"]', 'password123');
  await page.click('button[type="submit"]');

  // Wait for navigation
  await page.waitForURL('**/dashboard');

  // Assert
  await expect(page.locator('h1')).toHaveText('Dashboard');
  await expect(page.locator('.user-name')).toHaveText('John Doe');
});

// ══════════════════════════════════════════════════════════
// VISUAL REGRESSION TESTING
// ══════════════════════════════════════════════════════════

test('homepage looks correct', async ({ page }) => {
  await page.goto('https://app.example.com');

  // Take screenshot and compare with baseline
  await expect(page).toHaveScreenshot('homepage.png');
});

// ══════════════════════════════════════════════════════════
// NETWORK INTERCEPTION
// ══════════════════════════════════════════════════════════

test('handles API errors gracefully', async ({ page }) => {
  // Mock API to return error
  await page.route('**/api/users', (route) => {
    route.fulfill({
      status: 500,
      body: JSON.stringify({ error: 'Internal Server Error' }),
    });
  });

  await page.goto('https://app.example.com/users');

  // Assert error message shown
  await expect(page.locator('.error-message')).toHaveText(
    'Failed to load users',
  );
});
```

---

## **XV. Senior Developer Handbook Summary**

### **15.1. Complete Checklist**

```typescript
/**
 * 📋 BẢNG KIỂM TRA CHO SENIOR FRONTEND (Mọi lúc mọi nơi)
 */

const seniorDevHandbook = {
  // ═══════════════════════════════════════════════════════
  // CORE JAVASCRIPT
  // ══════════════════════════════════════════════ ═════════
  javascript: {
    fundamentals: [
      '✅ Closures, hoisting, scope chain (Chuỗi phạm vi)',
      '✅ Prototypes & inheritance (Kế thừa)',
      '✅ this binding (4 quy tắc)',
      '✅ Event loop (microtasks, macrotasks)',
      '✅ Promises, async/await',
      '✅ ES6+ features (destructuring, spread, optional chaining)',
    ],
    advanced: [
      '✅ Generators & iterators',
      '✅ Proxy & Reflect',
      '✅ WeakMap/WeakSet (Quản lý bộ nhớ)',
      '✅ Symbol (Thuộc tính ẩn)',
      '✅ Temporal Dead Zone (TDZ)',
      '✅ Module systems (ESM vs CommonJS)',
    ],
    performance: [
      '✅ Tối ưu O(n²) → O(n)',
      '✅ Dùng Map/Set để tra cứu nhanh',
      '✅ Memoization patterns (Ghi nhớ kết quả)',
      '✅ Debounce/throttle (Điều tiết sự kiện)',
      '✅ Web Workers cho tác vụ nặng',
    ],
  },

  // ═══════════════════════════════════════════════════════
  // REACT ECOSYSTEM
  // ═══════════════════════════════════════════════════════
  react: {
    fundamentals: [
      '✅ All hooks (useState, useEffect, useContext, etc.)',
      '✅ Component lifecycle',
      '✅ Virtual DOM & reconciliation',
      '✅ Keys in lists (why not index)',
    ],
    patterns: [
      '✅ Compound Components',
      '✅ Render Props (legacy)',
      '✅ HOC (deprecated → use hooks)',
      '✅ Container/Presentational',
      '✅ Controlled vs Uncontrolled',
    ],
    performance: [
      '✅ React.memo for expensive components',
      '✅ useMemo for expensive calculations',
      '✅ useCallback for stable functions',
      '✅ Code splitting (React.lazy)',
      '✅ Virtual scrolling (react-window)',
      '✅ Avoid inline objects/arrays',
      '✅ Profiler API for bottlenecks',
    ],
    stateManagement: [
      '✅ Context API limitations',
      '✅ Redux (actions, reducers, middleware)',
      '✅ Zustand (simpler alternative)',
      '✅ React Query (server state)',
      '✅ Recoil/Jotai (atomic state)',
    ],
  },

  // ═══════════════════════════════════════════════════════
  // CSS & STYLING
  // ═══════════════════════════════════════════════════════
  css: {
    modern: [
      '✅ CSS Grid & Flexbox',
      '✅ CSS Variables (custom properties)',
      '✅ Container queries',
      '✅ CSS layers (@layer)',
      '✅ content-visibility for lazy render',
    ],
    architecture: [
      '✅ BEM methodology',
      '✅ CSS Modules',
      '✅ Styled Components',
      '✅ Tailwind CSS',
      '✅ Critical CSS extraction',
    ],
    performance: [
      '✅ Avoid expensive selectors',
      '✅ CSS containment',
      '✅ will-change for animations',
      '✅ Reduce reflows/repaints',
    ],
  },

  // ═══════════════════════════════════════════════════════
  // SECURITY
  // ═══════════════════════════════════════════════════════
  security: {
    xss: [
      '✅ Sanitize user input (DOMPurify)',
      '✅ Use textContent over innerHTML',
      '✅ Content Security Policy (CSP)',
      '✅ Never use eval() or Function()',
    ],
    csrf: [
      '✅ CSRF tokens in forms',
      '✅ SameSite cookies',
      '✅ Custom headers for AJAX',
    ],
    auth: [
      '✅ HttpOnly cookies (not localStorage)',
      '✅ Refresh token pattern',
      '✅ Password validation (length, complexity)',
      '✅ bcrypt with salt >= 12',
    ],
    general: [
      '✅ HTTPS only',
      '✅ Secure headers (HSTS, X-Frame-Options)',
      '✅ Rate limiting',
      '✅ Input validation (client + server)',
      '✅ Dependency audits (npm audit)',
    ],
  },

  // ═══════════════════════════════════════════════════════
  // PERFORMANCE
  // ═══════════════════════════════════════════════════════
  performance: {
    metrics: [
      '✅ Core Web Vitals (LCP, FID, CLS)',
      '✅ Lighthouse score > 90',
      '✅ Time to Interactive < 3s',
      '✅ Bundle size < 200KB (gzipped)',
    ],
    optimization: [
      '✅ Code splitting by route',
      '✅ Lazy load images (loading="lazy")',
      '✅ Tree shaking (unused code)',
      '✅ Compression (gzip/brotli)',
      '✅ CDN for static assets',
      '✅ Service Worker for offline',
    ],
    monitoring: [
      '✅ Performance API',
      '✅ Chrome DevTools Profiler',
      '✅ React DevTools Profiler',
      '✅ Sentry for errors',
      '✅ Web Vitals tracking',
    ],
  },

  // ═══════════════════════════════════════════════════════
  // TESTING
  // ═══════════════════════════════════════════════════════
  testing: {
    unit: [
      '✅ Jest for test runner',
      '✅ React Testing Library',
      '✅ Test behavior, not implementation',
      '✅ Mock API calls (MSW)',
      '✅ Code coverage > 80%',
    ],
    integration: [
      '✅ Test user flows',
      '✅ Test error handling',
      '✅ Test edge cases',
    ],
    e2e: [
      '✅ Playwright/Cypress',
      '✅ Critical user paths',
      '✅ Visual regression testing',
    ],
  },

  // ═══════════════════════════════════════════════════════
  // BUILD & DEPLOYMENT
  // ═══════════════════════════════════════════════════════
  build: {
    tools: [
      '✅ Vite (fast dev server)',
      '✅ Webpack (production builds)',
      '✅ esbuild (fast bundler)',
      '✅ SWC (Babel alternative)',
    ],
    cicd: [
      '✅ GitHub Actions / GitLab CI',
      '✅ Automated tests',
      '✅ Linting (ESLint, Prettier)',
      '✅ Type checking (TypeScript)',
      '✅ Preview deployments',
    ],
    deployment: [
      '✅ Vercel/Netlify for static',
      '✅ Docker for containers',
      '✅ CloudFront for CDN',
      '✅ Environment variables',
      '✅ Health checks',
    ],
  },

  // ═══════════════════════════════════════════════════════
  // SOFT SKILLS
  // ═══════════════════════════════════════════════════════
  softSkills: [
    '✅ Code reviews (constructive feedback)',
    '✅ Technical documentation',
    '✅ Mentoring juniors',
    '✅ System design discussions',
    '✅ Performance debugging',
    '✅ Cross-team collaboration',
    '✅ Technical debt management',
    '✅ Estimation & planning',
  ],
};

/**
 * 🎯 INTERVIEW PREPARATION
 */
const interviewTopics = {
  // Must know cold
  critical: [
    'Closures & scope',
    'Promises & async/await',
    'React hooks (all)',
    'Virtual DOM & reconciliation',
    'Event loop',
    'XSS/CSRF prevention',
    'Performance optimization (O(n²) → O(n))',
    'CSS specificity & BEM',
  ],

  // Should be able to explain
  important: [
    'Prototype chain',
    'this binding',
    'React patterns (Compound, HOC)',
    'State management (Redux, Context)',
    'Code splitting',
    'Web Workers',
    'CSP & security headers',
    'Testing strategies',
  ],

  // Good to know
  bonus: [
    'Generators',
    'Proxy/Reflect',
    'Microfrontends',
    'SSR/SSG',
    'GraphQL',
    'WebAssembly',
    'Progressive Web Apps',
  ],
};

/**
 * 📚 LEARNING PATH
 */
const learningRoadmap = {
  month1_3: [
    'Master all React hooks',
    'Build 3 projects with different patterns',
    'Learn testing (RTL + Jest)',
    'Understand bundlers (Vite/Webpack)',
  ],

  month4_6: [
    'Deep dive Event Loop',
    'Master performance optimization',
    'Learn security (XSS, CSRF, Auth)',
    'Contribute to open source',
  ],

  month7_12: [
    'System design practice',
    'Mentor junior developers',
    'Learn architecture patterns',
    'Build production-grade apps',
  ],
};

export default seniorDevHandbook;
```

---

## **XVI. Advanced Browser APIs & Features**

### **16.1. Intersection Observer (Lazy Loading)**

```typescript
/**
 * 👁️ INTERSECTION OBSERVER
 */

// ══════════════════════════════════════════════════════════
// LAZY LOAD IMAGES
// ══════════════════════════════════════════════════════════

// ❌ Cách cũ: Tải tất cả ảnh ngay lập tức
<img src="heavy-image.jpg" alt="..." />

// ✅ Cách mới: Chỉ tải khi user cuộn tới (Lazy loading)
<img data-src="heavy-image.jpg" alt="..." loading="lazy" />

const lazyLoadImages = () => {
  const images = document.querySelectorAll('img[data-src]');

  const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target as HTMLImageElement;
        img.src = img.dataset.src!;
        img.removeAttribute('data-src');
        observer.unobserve(img);
      }
    });
  }, {
    rootMargin: '50px' // Tải trước khi xuất hiện 50px
  });

  images.forEach(img => imageObserver.observe(img));
};

// ══════════════════════════════════════════════════════════
// INFINITE SCROLL
// ══════════════════════════════════════════════════════════

function InfiniteScroll() {
  const [items, setItems] = useState<Item[]>([]);
  const [page, setPage] = useState(1);
  const loaderRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting) {
          setPage(prev => prev + 1);
        }
      },
      { threshold: 1.0 }
    );

    if (loaderRef.current) {
      observer.observe(loaderRef.current);
    }

    return () => observer.disconnect();
  }, []);

  useEffect(() => {
    fetchItems(page).then(newItems => {
      setItems(prev => [...prev, ...newItems]);
    });
  }, [page]);

  return (
    <div>
      {items.map(item => <ItemCard key={item.id} {...item} />)}
      <div ref={loaderRef}>Loading...</div>
    </div>
  );
}

// ══════════════════════════════════════════════════════════
// TRACK VISIBILITY FOR ANALYTICS
// ══════════════════════════════════════════════════════════

const trackElementVisibility = (selector: string, callback: () => void) => {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.intersectionRatio >= 0.5) { // 50% visible
          callback();
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.5 }
  );

  document.querySelectorAll(selector).forEach(el => observer.observe(el));
};

// Track ad impressions
trackElementVisibility('.ad-banner', () => {
  analytics.track('Ad Impression');
});
```

---

### **16.2. Service Workers & PWA**

```typescript
/**
 * 👷 SERVICE WORKERS
 */

// ══════════════════════════════════════════════════════════
// REGISTER SERVICE WORKER
// ══════════════════════════════════════════════════════════

// main.ts
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker
      .register('/sw.js')
      .then((registration) => {
        console.log('SW registered:', registration.scope);
      })
      .catch((error) => {
        console.error('SW registration failed:', error);
      });
  });
}

// ══════════════════════════════════════════════════════════
// SERVICE WORKER (sw.js)
// ══════════════════════════════════════════════════════════

const CACHE_NAME = 'v1';
const STATIC_ASSETS = [
  '/',
  '/',
  '/index.html',
  '/styles.css',
  '/app.js',
  '/logo.png',
];

// Install: Cache các tài nguyên tĩnh
self.addEventListener('install', (event: ExtendableEvent) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(STATIC_ASSETS)),
  );
});

// Activate: Dọn dẹp cache cũ
self.addEventListener('activate', (event: ExtendableEvent) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames
          .filter((name) => name !== CACHE_NAME)
          .map((name) => caches.delete(name)),
      );
    }),
  );
});

// Fetch: Ưu tiên Network, fallback về Cache (Network-first)
self.addEventListener('fetch', (event: FetchEvent) => {
  event.respondWith(
    fetch(event.request)
      .then((response) => {
        // Clone and cache successful responses
        if (response.status === 200) {
          const responseClone = response.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, responseClone);
          });
        }
        return response;
      })
      .catch(() => {
        // Network failed, try cache
        return caches.match(event.request);
      }),
  );
});

// ══════════════════════════════════════════════════════════
// OFFLINE FALLBACK PAGE
// ══════════════════════════════════════════════════════════

self.addEventListener('fetch', (event: FetchEvent) => {
  event.respondWith(
    fetch(event.request).catch(() => {
      return caches.match(event.request).then((response) => {
        return response || caches.match('/offline.html');
      });
    }),
  );
});

// ══════════════════════════════════════════════════════════
// BACKGROUND SYNC
// ══════════════════════════════════════════════════════════

// Register sync when online
navigator.serviceWorker.ready.then((registration) => {
  return registration.sync.register('sync-posts');
});

// Service worker handles sync
self.addEventListener('sync', (event: SyncEvent) => {
  if (event.tag === 'sync-posts') {
    event.waitUntil(syncPendingPosts());
  }
});

async function syncPendingPosts() {
  const posts = await getPostsFromIndexedDB();

  for (const post of posts) {
    try {
      await fetch('/api/posts', {
        method: 'POST',
        body: JSON.stringify(post),
      });
      await deletePostFromIndexedDB(post.id);
    } catch (error) {
      console.error('Sync failed:', error);
    }
  }
}

// ══════════════════════════════════════════════════════════
// PUSH NOTIFICATIONS
// ══════════════════════════════════════════════════════════

// Request permission
async function requestNotificationPermission() {
  const permission = await Notification.requestPermission();

  if (permission === 'granted') {
    const registration = await navigator.serviceWorker.ready;
    const subscription = await registration.pushManager.subscribe({
      userVisibleOnly: true,
      applicationServerKey: urlBase64ToUint8Array(PUBLIC_VAPID_KEY),
    });

    // Send subscription to server
    await fetch('/api/subscribe', {
      method: 'POST',
      body: JSON.stringify(subscription),
      headers: { 'Content-Type': 'application/json' },
    });
  }
}

// Service worker shows notification
self.addEventListener('push', (event: PushEvent) => {
  const data = event.data?.json();

  event.waitUntil(
    self.registration.showNotification(data.title, {
      body: data.body,
      icon: '/icon.png',
      badge: '/badge.png',
      actions: [
        { action: 'open', title: 'Open App' },
        { action: 'close', title: 'Close' },
      ],
    }),
  );
});

// Handle notification click
self.addEventListener('notificationclick', (event: NotificationEvent) => {
  event.notification.close();

  if (event.action === 'open') {
    event.waitUntil(clients.openWindow('/'));
  }
});
```

---

### **16.3. IndexedDB (Client-Side Database)**

```typescript
/**
 * 💾 INDEXEDDB
 */

// ══════════════════════════════════════════════════════════
// OPEN DATABASE
// ══════════════════════════════════════════════════════════

function openDB(): Promise<IDBDatabase> {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open('MyDatabase', 1);

    request.onerror = () => reject(request.error);
    request.onsuccess = () => resolve(request.result);

    request.onupgradeneeded = (event) => {
      const db = (event.target as IDBOpenDBRequest).result;

      // Create object store
      if (!db.objectStoreNames.contains('posts')) {
        const objectStore = db.createObjectStore('posts', {
          keyPath: 'id',
          autoIncrement: true,
        });
        objectStore.createIndex('timestamp', 'timestamp', { unique: false });
        objectStore.createIndex('status', 'status', { unique: false });
      }
    };
  });
}

// ══════════════════════════════════════════════════════════
// CRUD OPERATIONS
// ══════════════════════════════════════════════════════════

class PostDB {
  private db: IDBDatabase | null = null;

  async init() {
    this.db = await openDB();
  }

  async add(post: Post): Promise<number> {
    const tx = this.db!.transaction('posts', 'readwrite');
    const store = tx.objectStore('posts');
    const request = store.add(post);

    return new Promise((resolve, reject) => {
      request.onsuccess = () => resolve(request.result as number);
      request.onerror = () => reject(request.error);
    });
  }

  async getAll(): Promise<Post[]> {
    const tx = this.db!.transaction('posts', 'readonly');
    const store = tx.objectStore('posts');
    const request = store.getAll();

    return new Promise((resolve, reject) => {
      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error);
    });
  }

  async getByStatus(status: string): Promise<Post[]> {
    const tx = this.db!.transaction('posts', 'readonly');
    const store = tx.objectStore('posts');
    const index = store.index('status');
    const request = index.getAll(status);

    return new Promise((resolve, reject) => {
      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error);
    });
  }

  async update(id: number, data: Partial<Post>): Promise<void> {
    const tx = this.db!.transaction('posts', 'readwrite');
    const store = tx.objectStore('posts');
    const getRequest = store.get(id);

    return new Promise((resolve, reject) => {
      getRequest.onsuccess = () => {
        const post = { ...getRequest.result, ...data };
        const updateRequest = store.put(post);

        updateRequest.onsuccess = () => resolve();
        updateRequest.onerror = () => reject(updateRequest.error);
      };
      getRequest.onerror = () => reject(getRequest.error);
    });
  }

  async delete(id: number): Promise<void> {
    const tx = this.db!.transaction('posts', 'readwrite');
    const store = tx.objectStore('posts');
    const request = store.delete(id);

    return new Promise((resolve, reject) => {
      request.onsuccess = () => resolve();
      request.onerror = () => reject(request.error);
    });
  }
}

// Usage
const postDB = new PostDB();
await postDB.init();

await postDB.add({ title: 'Post 1', status: 'draft', timestamp: Date.now() });
const allPosts = await postDB.getAll();
const drafts = await postDB.getByStatus('draft');
```

---

### **16.4. Web Storage API (localStorage, sessionStorage)**

```typescript
/**
 * 💿 WEB STORAGE
 */

// ══════════════════════════════════════════════════════════
// TYPE-SAFE STORAGE WRAPPER
// ══════════════════════════════════════════════════════════

class TypedStorage<T extends Record<string, any>> {
  constructor(private storage: Storage = localStorage) {}

  set<K extends keyof T>(key: K, value: T[K]): void {
    try {
      this.storage.setItem(key as string, JSON.stringify(value));
    } catch (error) {
      if (error instanceof Error && error.name === 'QuotaExceededError') {
        console.error('Storage quota exceeded');
        this.cleanup();
      }
    }
  }

  get<K extends keyof T>(key: K): T[K] | null {
    const item = this.storage.getItem(key as string);
    if (!item) return null;

    try {
      return JSON.parse(item);
    } catch {
      return item as T[K];
    }
  }

  remove<K extends keyof T>(key: K): void {
    this.storage.removeItem(key as string);
  }

  clear(): void {
    this.storage.clear();
  }

  private cleanup(): void {
    // Remove oldest items
    const items = Object.entries(this.storage)
      .map(([key, value]) => {
        try {
          const parsed = JSON.parse(value);
          return { key, timestamp: parsed.timestamp || 0 };
        } catch {
          return { key, timestamp: 0 };
        }
      })
      .sort((a, b) => a.timestamp - b.timestamp);

    // Remove oldest 10%
    const toRemove = Math.ceil(items.length * 0.1);
    items.slice(0, toRemove).forEach((item) => {
      this.storage.removeItem(item.key);
    });
  }
}

// Usage
interface AppStorage {
  user: { id: string; name: string };
  token: string;
  preferences: { theme: 'light' | 'dark' };
}

const storage = new TypedStorage<AppStorage>();

storage.set('user', { id: '123', name: 'John' });
const user = storage.get('user'); // Typed as { id: string; name: string; } | null

// ══════════════════════════════════════════════════════════
// STORAGE EVENTS (Cross-tab communication)
// ══════════════════════════════════════════════════════════

// Tab 1: Listen for changes
window.addEventListener('storage', (event) => {
  if (event.key === 'user') {
    console.log('User changed in another tab:', event.newValue);
    // Update UI
  }
});

// Tab 2: Change storage
localStorage.setItem('user', JSON.stringify({ id: '456', name: 'Jane' }));
// Tab 1 receives event!

// ══════════════════════════════════════════════════════════
// STORAGE LIMITS
// ══════════════════════════════════════════════════════════

/**
 * Storage Limits:
 * • localStorage: ~5-10MB (varies by browser)
 * • sessionStorage: ~5-10MB
 * • IndexedDB: ~50MB-unlimited (user can allow more)
 * • Cache API: ~50MB-unlimited
 */

// Check quota
if ('storage' in navigator && 'estimate' in navigator.storage) {
  navigator.storage.estimate().then((estimate) => {
    console.log(`Using ${estimate.usage} of ${estimate.quota} bytes`);
    console.log(
      `${((estimate.usage! / estimate.quota!) * 100).toFixed(2)}% used`,
    );
  });
}
```

---

## **XVII. Build Optimization & Bundle Analysis**

### **17.1. Webpack Bundle Analysis**

```typescript
/**
 * 📦 BUNDLE OPTIMIZATION
 */

// ══════════════════════════════════════════════════════════
// WEBPACK BUNDLE ANALYZER
// ══════════════════════════════════════════════════════════

// webpack.config.js
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

module.exports = {
  plugins: [
    new BundleAnalyzerPlugin({
      analyzerMode: 'static',
      openAnalyzer: false,
      reportFilename: 'bundle-report.html'
    })
  ]
};

// Run: npm run build
// Opens interactive treemap showing bundle composition

// ══════════════════════════════════════════════════════════
// COMMON BUNDLE BLOAT & FIXES
// ══════════════════════════════════════════════════════════

// ❌ Vấn đề: Import toàn bộ thư viện (Nặng)
import _ from 'lodash'; // 70KB
import moment from 'moment'; // 230KB

// ✅ Giải pháp 1: Chỉ import hàm cần dùng
import debounce from 'lodash/debounce'; // 2KB
import format from 'date-fns/format'; // 2KB

// ✅ Giải pháp 2: Dùng plugin babel-plugin-lodash
// .babelrc
{
  "plugins": ["lodash"]
}

// Now this tree-shakes automatically:
import { debounce, throttle } from 'lodash';

// ══════════════════════════════════════════════════════════
// DYNAMIC IMPORTS
// ══════════════════════════════════════════════════════════

// ❌ Import tĩnh (Luôn tải về ngay từ đầu)
import Chart from 'chart.js';

// ✅ Import động (Chỉ tải khi cần)
button.addEventListener('click', async () => {
  const Chart = await import('chart.js');
  new Chart.default(ctx, config);
});

// React lazy + Suspense
const HeavyComponent = lazy(() => import('./HeavyComponent'));

function App() {
  return (
    <Suspense fallback={<Loading />}>
      <HeavyComponent />
    </Suspense>
  );
}

// ══════════════════════════════════════════════════════════
// TREE SHAKING
// ══════════════════════════════════════════════════════════

// package.json
{
  "sideEffects": false // Enables aggressive tree shaking
}

// Or specify files with side effects:
{
  "sideEffects": ["*.css", "*.scss"]
}

// ❌ CommonJS (can't tree shake)
const utils = require('./utils');
module.exports = { foo, bar };

// ✅ ESM (tree shakes unused exports)
export { foo, bar };

// ══════════════════════════════════════════════════════════
// CODE SPLITTING STRATEGIES
// ══════════════════════════════════════════════════════════

// webpack.config.js
module.exports = {
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        // Vendor bundle (node_modules)
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          priority: 10
        },
        // Common code (used in 2+ chunks)
        common: {
          minChunks: 2,
          name: 'common',
          priority: 5,
          reuseExistingChunk: true
        },
        // React vendor
        react: {
          test: /[\\/]node_modules[\\/](react|react-dom)[\\/]/,
          name: 'react',
          priority: 20
        }
      }
    }
  }
};

    }
  }
};

/**
 * Trước khi tối ưu: 1 file duy nhất (500KB)
 * Sau khi tối ưu:
 * • main.js: 50KB
 * • react.js: 120KB (được cache lâu dài)
 * • vendors.js: 200KB (được cache)
 * • common.js: 30KB (được cache)
 *
 * Tổng: 400KB (nhẹ hơn 20%)
 * Các lần tải sau: Chỉ cần tải 50KB main.js! (90% đã có trong cache)
 */
```

---

### **17.2. Vite Optimization**

```typescript
/**
 * ⚡ VITE OPTIMIZATION
 */

// vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { visualizer } from 'rollup-plugin-visualizer';

export default defineConfig({
  plugins: [
    react(),
    visualizer({
      open: true,
      gzipSize: true,
      brotliSize: true
    })
  ],

  build: {
    // Target modern browsers (smaller output)
    target: 'esnext',

    // Chunk size warnings
    chunkSizeWarningLimit: 500,

    rollupOptions: {
      output: {
        // Manual chunks
        manualChunks: {
          'react-vendor': ['react', 'react-dom', 'react-router-dom'],
          'ui-vendor': ['antd', '@mui/material'],
          'chart-vendor': ['recharts', 'd3']
        }
      }
    },

    // Minification
    minify: 'terser',
    terserOptions: {
      compress: {
        drop_console: true, // Remove console.log in production
        drop_debugger: true
      }
    }
  },

  // Optimize deps
  optimizeDeps: {
    include: ['react', 'react-dom'],
    exclude: ['@vite/client', '@vite/env']
  }
});

// ══════════════════════════════════════════════════════════
// PRELOAD CRITICAL RESOURCES
// ══════════════════════════════════════════════════════════

// index.html
<head>
  <!-- Preload fonts -->
  <link rel="preload" href="/fonts/main.woff2" as="font" type="font/woff2" crossorigin>

  <!-- Preconnect to API -->
  <link rel="preconnect" href="https://api.example.com">
  <link rel="dns-prefetch" href="https://api.example.com">

  <!-- Prefetch next route -->
  <link rel="prefetch" href="/dashboard.js">
</head>

// ══════════════════════════════════════════════════════════
// COMPRESSION
// ══════════════════════════════════════════════════════════

// vite-plugin-compression
import compression from 'vite-plugin-compression';

export default defineConfig({
  plugins: [
    compression({
      algorithm: 'brotliCompress',
      ext: '.br',
      threshold: 1024, // Only compress files > 1KB
      deleteOriginFile: false
    })
  ]
});

/**
 * Compression comparison (500KB bundle):
 * • Uncompressed: 500KB
 * • gzip: 150KB (70% smaller)
 * • brotli: 120KB (76% smaller)
 */
```

---

## **XVIII. Accessibility (a11y) Best Practices**

### **18.1. Semantic HTML & ARIA**

```typescript
/**
 * ♿ ACCESSIBILITY
 */

// ══════════════════════════════════════════════════════════
// SEMANTIC HTML
// ══════════════════════════════════════════════════════════

// ❌ Bad: Div soup
<div class="header">
  <div class="nav">
    <div class="nav-item" onclick="navigate()">Home</div>
  </div>
</div>

// ✅ Good: Semantic HTML
<header>
  <nav aria-label="Main navigation">
    <a href="/">Home</a>
  </nav>
</header>

// ══════════════════════════════════════════════════════════
// ARIA LABELS
// ══════════════════════════════════════════════════════════

// ❌ Bad: No label
<button onClick={handleClose}>×</button>

// ✅ Good: aria-label
<button onClick={handleClose} aria-label="Close dialog">
  ×
</button>

// Form with proper labels
<form>
  <label htmlFor="email">Email</label>
  <input
    id="email"
    type="email"
    aria-required="true"
    aria-invalid={errors.email ? 'true' : 'false'}
    aria-describedby={errors.email ? 'email-error' : undefined}
  />
  {errors.email && (
    <span id="email-error" role="alert">
      {errors.email}
    </span>
  )}
</form>

// ══════════════════════════════════════════════════════════
// KEYBOARD NAVIGATION
// ══════════════════════════════════════════════════════════

function Dropdown() {
  const [isOpen, setIsOpen] = useState(false);
  const buttonRef = useRef<HTMLButtonElement>(null);

  const handleKeyDown = (e: KeyboardEvent) => {
    switch (e.key) {
      case 'Escape':
        setIsOpen(false);
        buttonRef.current?.focus();
        break;
      case 'ArrowDown':
        e.preventDefault();
        // Focus next item
        break;
      case 'ArrowUp':
        e.preventDefault();
        // Focus previous item
        break;
    }
  };

  return (
    <div>
      <button
        ref={buttonRef}
        onClick={() => setIsOpen(!isOpen)}
        aria-haspopup="true"
        aria-expanded={isOpen}
      >
        Menu
      </button>

      {isOpen && (
        <ul
          role="menu"
          onKeyDown={handleKeyDown}
        >
          <li role="menuitem" tabIndex={0}>Item 1</li>
          <li role="menuitem" tabIndex={0}>Item 2</li>
        </ul>
      )}
    </div>
  );
}

// ══════════════════════════════════════════════════════════
// FOCUS MANAGEMENT
// ══════════════════════════════════════════════════════════

function Modal({ isOpen, onClose, children }) {
  const modalRef = useRef<HTMLDivElement>(null);
  const previousFocusRef = useRef<HTMLElement | null>(null);

  useEffect(() => {
    if (isOpen) {
      // Save current focus
      previousFocusRef.current = document.activeElement as HTMLElement;

      // Focus first focusable element in modal
      const focusable = modalRef.current?.querySelector<HTMLElement>(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
      );
      focusable?.focus();

      // Trap focus in modal
      const handleTab = (e: KeyboardEvent) => {
        const focusableElements = modalRef.current?.querySelectorAll<HTMLElement>(
          'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
        );

        if (!focusableElements) return;

        const first = focusableElements[0];
        const last = focusableElements[focusableElements.length - 1];

        if (e.key === 'Tab') {
          if (e.shiftKey && document.activeElement === first) {
            e.preventDefault();
            last.focus();
          } else if (!e.shiftKey && document.activeElement === last) {
            e.preventDefault();
            first.focus();
          }
        }
      };

      document.addEventListener('keydown', handleTab);

      return () => {
        document.removeEventListener('keydown', handleTab);
        // Restore focus
        previousFocusRef.current?.focus();
      };
    }
  }, [isOpen]);

  if (!isOpen) return null;

  return (
    <div
      ref={modalRef}
      role="dialog"
      aria-modal="true"
      aria-labelledby="modal-title"
    >
      <h2 id="modal-title">Modal Title</h2>
      {children}
      <button onClick={onClose}>Close</button>
    </div>
  );
}

// ══════════════════════════════════════════════════════════
// SCREEN READER ANNOUNCEMENTS
// ══════════════════════════════════════════════════════════

function LiveRegion() {
  const [message, setMessage] = useState('');

  const announce = (text: string) => {
    setMessage(text);
    setTimeout(() => setMessage(''), 1000);
  };

  return (
    <>
      <button onClick={() => announce('Item added to cart')}>
        Add to Cart
      </button>

      {/* Screen reader will announce this */}
      <div
        role="status"
        aria-live="polite"
        aria-atomic="true"
        className="sr-only"
      >
        {message}
      </div>
    </>
  );
}

// CSS for screen-reader only
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}
```

---

### **18.2. Color Contrast & Visual Accessibility**

```typescript
/**
 * 🎨 VISUAL ACCESSIBILITY
 */

// ══════════════════════════════════════════════════════════
// COLOR CONTRAST (WCAG AA: 4.5:1, AAA: 7:1)
// ══════════════════════════════════════════════════════════

// ❌ Bad: Low contrast (2:1)
.text {
  color: #777; /* on white background */
}

// ✅ Good: High contrast (7:1)
.text {
  color: #333; /* on white background */
}

// Check contrast programmatically
function getContrastRatio(color1: string, color2: string): number {
  const lum1 = getLuminance(color1);
  const lum2 = getLuminance(color2);

  const lighter = Math.max(lum1, lum2);
  const darker = Math.min(lum1, lum2);

  return (lighter + 0.05) / (darker + 0.05);
}

function getLuminance(color: string): number {
  const rgb = hexToRgb(color);
  const [r, g, b] = rgb.map(val => {
    val = val / 255;
    return val <= 0.03928
      ? val / 12.92
      : Math.pow((val + 0.055) / 1.055, 2.4);
  });

  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}

// ══════════════════════════════════════════════════════════
// REDUCED MOTION
// ══════════════════════════════════════════════════════════

// CSS: Respect prefers-reduced-motion
.animated {
  transition: transform 0.3s ease;
}

@media (prefers-reduced-motion: reduce) {
  .animated {
    transition: none;
  }
}

// React: Check preference
function useReducedMotion() {
  const [prefersReducedMotion, setPrefersReducedMotion] = useState(false);

  useEffect(() => {
    const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    setPrefersReducedMotion(mediaQuery.matches);

    const listener = (e: MediaQueryListEvent) => {
      setPrefersReducedMotion(e.matches);
    };

    mediaQuery.addEventListener('change', listener);
    return () => mediaQuery.removeEventListener('change', listener);
  }, []);

  return prefersReducedMotion;
}

// Usage
function AnimatedComponent() {
  const prefersReducedMotion = useReducedMotion();

  return (
    <motion.div
      animate={{ x: 100 }}
      transition={{
        duration: prefersReducedMotion ? 0 : 0.3
      }}
    />
  );
}

// ══════════════════════════════════════════════════════════
// TEXT ALTERNATIVES
// ══════════════════════════════════════════════════════════

// Images
<img src="chart.png" alt="Bar chart showing sales increased 30% in Q4" />

// Decorative images
<img src="divider.png" alt="" role="presentation" />

// Icon buttons
<button aria-label="Search">
  <SearchIcon aria-hidden="true" />
</button>

// Complex charts
<figure role="img" aria-labelledby="chart-title chart-desc">
  <figcaption>
    <div id="chart-title">Quarterly Sales</div>
    <div id="chart-desc">
      Sales grew from $1M in Q1 to $1.3M in Q4,
      with Q3 showing the highest growth at 20%.
    </div>
  </figcaption>
  <ChartComponent />
</figure>
```

---

## **XIX. Internationalization (i18n)**

### **19.1. react-i18next Setup**

```typescript
/**
 * 🌍 INTERNATIONALIZATION
 */

// ══════════════════════════════════════════════════════════
// i18n SETUP
// ══════════════════════════════════════════════════════════

// i18n.ts
import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import LanguageDetector from 'i18next-browser-languagedetector';

i18n
  .use(LanguageDetector)
  .use(initReactI18next)
  .init({
    resources: {
      en: {
        translation: {
          welcome: 'Welcome',
          greeting: 'Hello, {{name}}!',
          itemCount: '{{count}} item',
          itemCount_plural: '{{count}} items'
        }
      },
      vi: {
        translation: {
          welcome: 'Chào mừng',
          greeting: 'Xin chào, {{name}}!',
          itemCount: '{{count}} mục'
        }
      }
    },
    fallbackLng: 'en',
    interpolation: {
      escapeValue: false // React already escapes
    }
  });

export default i18n;

// ══════════════════════════════════════════════════════════
// USAGE IN COMPONENTS
// ══════════════════════════════════════════════════════════

import { useTranslation } from 'react-i18next';

function Component() {
  const { t, i18n } = useTranslation();

  const changeLanguage = (lng: string) => {
    i18n.changeLanguage(lng);
  };

  return (
    <div>
      <h1>{t('welcome')}</h1>
      <p>{t('greeting', { name: 'John' })}</p>
      <p>{t('itemCount', { count: 5 })}</p>

      <button onClick={() => changeLanguage('en')}>English</button>
      <button onClick={() => changeLanguage('vi')}>Tiếng Việt</button>
    </div>
  );
}

// ══════════════════════════════════════════════════════════
// LAZY LOADING TRANSLATIONS
// ══════════════════════════════════════════════════════════

import i18n from 'i18next';
import Backend from 'i18next-http-backend';

i18n
  .use(Backend)
  .use(initReactI18next)
  .init({
    backend: {
      loadPath: '/locales/{{lng}}/{{ns}}.json'
    },
    fallbackLng: 'en',
    ns: ['common', 'dashboard', 'settings'],
    defaultNS: 'common'
  });

// File structure:
// /locales/en/common.json
// /locales/en/dashboard.json
// /locales/vi/common.json
// /locales/vi/dashboard.json

// ══════════════════════════════════════════════════════════
// DATE & NUMBER FORMATTING
// ══════════════════════════════════════════════════════════

import { useTranslation } from 'react-i18next';

function PriceDisplay({ amount }: { amount: number }) {
  const { i18n } = useTranslation();

  const formatter = new Intl.NumberFormat(i18n.language, {
    style: 'currency',
    currency: 'USD'
  });

  return <span>{formatter.format(amount)}</span>;
  // en: $1,234.56
  // vi: US$1.234,56
}

function DateDisplay({ date }: { date: Date }) {
  const { i18n } = useTranslation();

  const formatter = new Intl.DateTimeFormat(i18n.language, {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  });

  return <span>{formatter.format(date)}</span>;
  // en: December 25, 2023
  // vi: 25 tháng 12, 2023
}

// ══════════════════════════════════════════════════════════
// RTL (Right-to-Left) SUPPORT
// ══════════════════════════════════════════════════════════

function App() {
  const { i18n } = useTranslation();
  const isRTL = ['ar', 'he', 'fa'].includes(i18n.language);

  useEffect(() => {
    document.dir = isRTL ? 'rtl' : 'ltr';
    document.documentElement.lang = i18n.language;
  }, [i18n.language, isRTL]);

  return <div>{/* app content */}</div>;
}

// CSS for RTL
.button {
  margin-left: 10px;
}

/* RTL override */
[dir="rtl"] .button {
  margin-left: 0;
  margin-right: 10px;
}

// Or use logical properties
.button {
  margin-inline-start: 10px; /* Auto RTL support! */
}
```

---

## **XX. Monitoring & Observability**

### **20.1. Error Tracking with Sentry**

```typescript
/**
 * 🔍 ERROR TRACKING
 */

// ══════════════════════════════════════════════════════════
// SENTRY SETUP
// ══════════════════════════════════════════════════════════

import * as Sentry from '@sentry/react';
import { BrowserTracing } from '@sentry/tracing';

Sentry.init({
  dsn: 'YOUR_SENTRY_DSN',
  environment: process.env.NODE_ENV,

  // Performance monitoring
  integrations: [
    new BrowserTracing({
      tracingOrigins: ['localhost', 'https://api.example.com'],
    }),
  ],

  tracesSampleRate: 0.1, // 10% of transactions

  // Filter errors
  beforeSend(event, hint) {
    // Don't send local errors
    if (window.location.hostname === 'localhost') {
      return null;
    }

    // Filter out known errors
    const error = hint.originalException as Error;
    if (error?.message?.includes('ResizeObserver')) {
      return null;
    }

    return event;
  },

  // Add user context
  beforeBreadcrumb(breadcrumb) {
    if (breadcrumb.category === 'console') {
      return null; // Don't log console breadcrumbs
    }
    return breadcrumb;
  },
});

// ══════════════════════════════════════════════════════════
// ERROR BOUNDARIES
// ══════════════════════════════════════════════════════════

import { ErrorBoundary } from '@sentry/react';

function App() {
  return (
    <ErrorBoundary
      fallback={({ error, resetError }) => (
        <div>
          <h1>Something went wrong</h1>
          <p>{error.message}</p>
          <button onClick={resetError}>Try again</button>
        </div>
      )}
      beforeCapture={(scope) => {
        scope.setTag('location', 'App');
      }}
    >
      <AppContent />
    </ErrorBoundary>
  );
}

// ══════════════════════════════════════════════════════════
// CUSTOM ERROR TRACKING
// ══════════════════════════════════════════════════════════

// Set user context
Sentry.setUser({
  id: user.id,
  email: user.email,
  username: user.username,
});

// Add breadcrumbs
Sentry.addBreadcrumb({
  category: 'api',
  message: 'Fetched user data',
  level: 'info',
  data: { userId: '123' },
});

// Capture custom errors
try {
  riskyOperation();
} catch (error) {
  Sentry.captureException(error, {
    tags: {
      section: 'payment',
    },
    extra: {
      paymentAmount: 100,
      currency: 'USD',
    },
  });
}

// Performance monitoring
const transaction = Sentry.startTransaction({
  name: 'CheckoutFlow',
  op: 'user-flow',
});

const span = transaction.startChild({
  op: 'payment',
  description: 'Process payment',
});

await processPayment();

span.finish();
transaction.finish();

// ══════════════════════════════════════════════════════════
// AXIOS INTERCEPTOR FOR API ERRORS
// ══════════════════════════════════════════════════════════

axios.interceptors.response.use(
  (response) => response,
  (error) => {
    Sentry.captureException(error, {
      tags: {
        type: 'api-error',
        endpoint: error.config?.url,
      },
      extra: {
        status: error.response?.status,
        data: error.response?.data,
      },
    });

    return Promise.reject(error);
  }
);
```

---

### **20.2. Performance Monitoring**

```typescript
/**
 * ⚡ PERFORMANCE MONITORING
 */

// ══════════════════════════════════════════════════════════
// WEB VITALS
// ══════════════════════════════════════════════════════════

import { onCLS, onFID, onLCP, onFCP, onTTFB } from 'web-vitals';

function sendToAnalytics(metric: Metric) {
  // Send to analytics service
  fetch('/api/analytics', {
    method: 'POST',
    body: JSON.stringify({
      name: metric.name,
      value: metric.value,
      delta: metric.delta,
      id: metric.id,
      navigationType: metric.navigationType,
    }),
  });

  // Also log to console in dev
  console.log(metric.name, metric.value);
}

// Track Core Web Vitals
onCLS(sendToAnalytics); // Cumulative Layout Shift
onFID(sendToAnalytics); // First Input Delay
onLCP(sendToAnalytics); // Largest Contentful Paint
onFCP(sendToAnalytics); // First Contentful Paint
onTTFB(sendToAnalytics); // Time to First Byte

/**
 * Good scores:
 * • LCP: < 2.5s
 * • FID: < 100ms
 * • CLS: < 0.1
 */

// ══════════════════════════════════════════════════════════
// CUSTOM PERFORMANCE MARKS
// ══════════════════════════════════════════════════════════

// Mark important events
performance.mark('data-fetch-start');

await fetchData();

performance.mark('data-fetch-end');

// Measure duration
performance.measure('data-fetch', 'data-fetch-start', 'data-fetch-end');

// Get all measures
const measures = performance.getEntriesByType('measure');
measures.forEach((measure) => {
  console.log(`${measure.name}: ${measure.duration}ms`);
});

// ══════════════════════════════════════════════════════════
// REACT PROFILER
// ══════════════════════════════════════════════════════════

import { Profiler } from 'react';

function onRenderCallback(
  id: string,
  phase: 'mount' | 'update',
  actualDuration: number,
  baseDuration: number,
  startTime: number,
  commitTime: number
) {
  console.log({
    id,
    phase,
    actualDuration, // Time spent rendering
    baseDuration, // Estimated time without memoization
    startTime,
    commitTime,
  });

  // Send to analytics if slow
  if (actualDuration > 16) {
    // > 1 frame (60fps)
    sendToAnalytics({
      type: 'slow-render',
      component: id,
      duration: actualDuration,
    });
  }
}

function App() {
  return (
    <Profiler id="App" onRender={onRenderCallback}>
      <SlowComponent />
    </Profiler>
  );
}

// ══════════════════════════════════════════════════════════
// LONG TASK OBSERVER
// ══════════════════════════════════════════════════════════

const observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    console.warn('Long task detected:', {
      duration: entry.duration,
      startTime: entry.startTime,
    });

    // Send to analytics
    if (entry.duration > 50) {
      // > 50ms blocks UI
      sendToAnalytics({
        type: 'long-task',
        duration: entry.duration,
      });
    }
  }
});

observer.observe({ entryTypes: ['longtask'] });

// ══════════════════════════════════════════════════════════
// RESOURCE TIMING
// ══════════════════════════════════════════════════════════

// Track slow resources
const resources = performance.getEntriesByType('resource');

resources.forEach((resource: PerformanceResourceTiming) => {
  const duration = resource.responseEnd - resource.startTime;

  if (duration > 1000) {
    // > 1 second
    console.warn('Slow resource:', {
      name: resource.name,
      duration,
      size: resource.transferSize,
      type: resource.initiatorType,
    });
  }
});

// ══════════════════════════════════════════════════════════
// CUSTOM HOOK FOR PERFORMANCE
// ══════════════════════════════════════════════════════════

function usePerformance(componentName: string) {
  useEffect(() => {
    const startTime = performance.now();

    return () => {
      const endTime = performance.now();
      const duration = endTime - startTime;

      console.log(`${componentName} mounted for ${duration}ms`);

      if (duration > 1000) {
        sendToAnalytics({
          type: 'slow-component',
          component: componentName,
          duration,
        });
      }
    };
  }, [componentName]);
}

// Usage
function SlowComponent() {
  usePerformance('SlowComponent');

  return <div>{/* content */}</div>;
}
```

---

## **XXI. React-Specific Mistakes & Anti-Patterns**

### **21.1 🪝 React Hooks - Lỗi Phổ Biến**

```typescript
/**
 * ❌ MISTAKE 1: Missing dependencies in useEffect (Infinite loop)
 */

// ❌ BAD: userId dependency missing → stale data
function UserProfile({ userId }) {
  useEffect(() => {
    fetchUser(userId); // Runs only once!
  }, []); // ⚠️ No userId!
}

// ✅ GOOD: Include all dependencies
function UserProfile({ userId }) {
  useEffect(() => {
    fetchUser(userId);
  }, [userId]); // ✅ Runs when userId changes
}

/**
 * ❌ MISTAKE 2: Stale closures in setInterval
 */

// ❌ BAD: count always stays 0
function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setCount(count + 1); // ⚠️ count closure is always 0!
    }, 1000);
    return () => clearInterval(interval);
  }, []); // Empty deps
}

// ✅ GOOD 1: Functional update
function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setCount((prev) => prev + 1); // ✅ Uses previous state
    }, 1000);
    return () => clearInterval(interval);
  }, []);
}

// ✅ GOOD 2: Include dependency
function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const timeout = setTimeout(() => setCount(count + 1), 1000);
    return () => clearTimeout(timeout);
  }, [count]); // ✅ Runs when count changes
}

/**
 * ❌ MISTAKE 3: Calling hooks conditionally (breaks rules)
 */

// ❌ BAD: Hook inside condition
function Component({ isAdmin }) {
  if (isAdmin) {
    useEffect(() => {}); // ⚠️ Hook call order changes!
  }
}

// ✅ GOOD: Logic inside hook
function Component({ isAdmin }) {
  useEffect(() => {
    if (isAdmin) {
      // Logic here
    }
  }, [isAdmin]);
}

/**
 * ❌ MISTAKE 4: useMemo/useCallback overuse (premature optimization)
 */

// ❌ BAD: Memoizing simple operations
function List({ items }) {
  const sorted = useMemo(
    () => items.sort((a, b) => a - b), // Simple! Overhead > benefit
    [items]
  );
  return items.map((i) => <Item key={i} value={i} />);
}

// ✅ GOOD: Only memoize expensive operations
function List({ items }) {
  const sorted = useMemo(
    () => expensiveAlgorithm(items), // Complex! Worth memoizing
    [items]
  );
  return sorted.map((i) => <MemoItem key={i} value={i} />);
}

/**
 * ❌ MISTAKE 5: useRef for state (won't re-render)
 */

// ❌ BAD: Using ref for values that need re-render
function Counter() {
  const countRef = useRef(0);

  return (
    <button onClick={() => countRef.current++}>
      Count: {countRef.current} {/* Never updates! */}
    </button>
  );
}

// ✅ GOOD: Use state for values needing re-render
function Counter() {
  const [count, setCount] = useState(0);

  return (
    <button onClick={() => setCount((c) => c + 1)}>
      Count: {count} {/* Updates! */}
    </button>
  );
}

// ✅ GOOD: Use ref for DOM access
function TextInput() {
  const inputRef = useRef(null);

  return (
    <>
      <input ref={inputRef} />
      <button onClick={() => inputRef.current?.focus()}>Focus</button>
    </>
  );
}
```

### **21.2 ⚛️ Component Re-render Issues**

```typescript
/**
 * ❌ MISTAKE 6: All children re-render on parent state change
 */

// ❌ BAD: Filter input causes all 10,000 items to re-render
function UserList() {
  const [filter, setFilter] = useState('');
  const [users] = useState(generateMillionUsers()); // Large list

  const filteredUsers = users.filter(u => u.name.includes(filter));

  return (
    <div>
      <input
        value={filter}
        onChange={(e) => setFilter(e.target.value)}
      />
      {filteredUsers.map(u => (
        <UserCard key={u.id} user={u} /> {/* All re-render! */}
      ))}
    </div>
  );
}

// ✅ GOOD 1: Split state into components (separation of concerns)
function UserListContainer() {
  const [users] = useState(generateMillionUsers());

  return (
    <div>
      <FilterInput /> {/* Only this component updates */}
      <UserListDisplay users={users} /> {/* Stable, no re-render */}
    </div>
  );
}

function FilterInput() {
  const [filter, setFilter] = useState('');
  const users = useContext(UsersContext);
  const filtered = useMemo(() =>
    users.filter(u => u.name.includes(filter)),
    [users, filter]
  );
  return (
    <>
      <input value={filter} onChange={(e) => setFilter(e.target.value)} />
      <UserList users={filtered} />
    </>
  );
}

// ✅ GOOD 2: Memoize children
const UserCard = memo(({ user }) => (
  <div>{user.name}</div>
));

function UserList({ users }) {
  return users.map(u => <UserCard key={u.id} user={u} />);
}

/**
 * ❌ MISTAKE 7: Props objects created inline (always new reference)
 */

// ❌ BAD: Props recreated every render
function Parent() {
  return (
    <Child
      config={{ theme: 'dark', size: 'lg' }} {/* New object every render! */}
      handler={() => doSomething()} {/* New function every render! */}
    />
  );
}

const Child = memo(({ config, handler }) => (
  <div>{config.theme}</div> {/* Re-renders every parent render */}
));

// ✅ GOOD: Memoize values & callbacks
function Parent() {
  const config = useMemo(() => ({ theme: 'dark', size: 'lg' }), []);
  const handler = useCallback(() => doSomething(), []);

  return <Child config={config} handler={handler} />;
}

/**
 * ❌ MISTAKE 8: Index as key (breaks component state)
 */

// ❌ BAD: Using array index as key
function ItemList({ items }) {
  return items.map((item, index) => (
    <Item key={index} value={item} /> {/* ⚠️ Key changes when list reorders! */}
  ));
}

// Scenario: User has form input in Item, delete first item
// Before: Item[0]="Apple", Item[1]="Banana" with input "Hello"
// After delete: Item[0]="Banana", Item[1] removed
// Problem: "Banana" still has input "Hello" (component state attached to index!)

// ✅ GOOD: Use unique ID
function ItemList({ items }) {
  return items.map(item => (
    <Item key={item.id} value={item} /> {/* ✅ Stable key */}
  ));
}
```

### **21.3 📊 State Management Mistakes**

```typescript
/**
 * ❌ MISTAKE 9: Direct state mutation (React doesn't detect)
 */

// ❌ BAD: Mutating state directly
function UserProfile() {
  const [user, setUser] = useState({ name: 'John', age: 30 });

  const updateAge = () => {
    user.age = 31; // ⚠️ Mutate object
    setUser(user); // React doesn't detect change (same reference!)
  };

  return <div>Age: {user.age}</div>; // Never updates!
}

// ✅ GOOD: Create new object
function UserProfile() {
  const [user, setUser] = useState({ name: 'John', age: 30 });

  const updateAge = () => {
    setUser({ ...user, age: 31 }); // ✅ New object
  };

  return <div>Age: {user.age}</div>;
}

/**
 * ❌ MISTAKE 10: useState with expensive initialization
 */

// ❌ BAD: Expensive function runs every render
function Component() {
  const [data, setData] = useState(expensiveCalculation()); // Runs every render!
}

// ✅ GOOD: Use init function (runs once)
function Component() {
  const [data, setData] = useState(() => expensiveCalculation());
}

/**
 * ❌ MISTAKE 11: Too many useState calls (state explosion)
 */

// ❌ BAD: 10+ useState for related data
function Form() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [address, setAddress] = useState('');
  // ... 6 more useState

  // Hard to manage, easy to miss dependencies in useEffect
}

// ✅ GOOD: Group related state
function Form() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    address: '',
  });

  const handleChange = (field, value) => {
    setFormData((prev) => ({ ...prev, [field]: value }));
  };
}

// ✅ BETTER: useReducer for complex logic
function Form() {
  const [formData, dispatch] = useReducer(formReducer, initialState);

  const handleChange = (field, value) => {
    dispatch({ type: 'UPDATE_FIELD', payload: { field, value } });
  };
}
```

---

## **XXII. Library Integration Mistakes**

### **22.1 🔗 Context API Misuse**

```typescript
/**
 * ❌ MISTAKE 12: Context causes all consumers to re-render
 */

// ❌ BAD: Theme context causes all children to re-render
function App() {
  const [theme, setTheme] = useState('light');

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <Header /> {/* Re-renders on theme change */}
      <Sidebar /> {/* Re-renders on theme change */}
      <MainContent /> {/* Re-renders on theme change */}
    </ThemeContext.Provider>
  );
}

// ✅ GOOD: Split contexts by frequency
function App() {
  const [theme, setTheme] = useState('light');
  const [user, setUser] = useState(null);

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <UserContext.Provider value={{ user, setUser }}>
        <Header /> {/* Only theme context re-renders */}
        <MainContent /> {/* Gets both from separate contexts */}
      </UserContext.Provider>
    </ThemeContext.Provider>
  );
}

/**
 * ❌ MISTAKE 13: Creating context object inline (always new reference)
 */

// ❌ BAD: Value object recreated every render
function App() {
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {' '}
      {/* New object! */}
      <Children />
    </ThemeContext.Provider>
  );
}

// ✅ GOOD: Memoize context value
function App() {
  const [theme, setTheme] = useState('light');
  const value = useMemo(() => ({ theme, setTheme }), [theme]);

  return (
    <ThemeContext.Provider value={value}>
      <Children />
    </ThemeContext.Provider>
  );
}
```

### **22.2 ⚙️ Third-Party Library Issues**

```typescript
/**
 * ❌ MISTAKE 14: Redux/Zustand selector not memoized
 */

// ❌ BAD: New selector object every render → re-subscribe
function Counter() {
  const count = useSelector((state) => ({
    value: state.counter.value,
    doubled: state.counter.value * 2,
  })); // New object every render!

  return <div>{count.value}</div>;
}

// ✅ GOOD: Memoize selector
const selectCounter = (state) => ({
  value: state.counter.value,
  doubled: state.counter.value * 2,
});

function Counter() {
  const count = useSelector(selectCounter); // Stable selector
  return <div>{count.value}</div>;
}

/**
 * ❌ MISTAKE 15: React Router navigation in event (race condition)
 */

// ❌ BAD: Cancel requests but navigate anyway
function LoginForm() {
  const navigate = useNavigate();
  const abortRef = useRef(null);

  const handleLogin = async (credentials) => {
    abortRef.current = new AbortController();

    try {
      await loginAPI(credentials, { signal: abortRef.current.signal });
      navigate('/dashboard'); // Still navigates even if aborted!
    } catch (error) {
      // Handle error
    }
  };

  useEffect(() => {
    return () => abortRef.current?.abort();
  }, []);
}

// ✅ GOOD: Check if still mounted
function LoginForm() {
  const navigate = useNavigate();
  const isMountedRef = useRef(true);

  const handleLogin = async (credentials) => {
    try {
      await loginAPI(credentials);
      if (isMountedRef.current) {
        navigate('/dashboard');
      }
    } catch (error) {
      if (isMountedRef.current) {
        showError(error);
      }
    }
  };

  useEffect(() => {
    return () => {
      isMountedRef.current = false;
    };
  }, []);
}
```

---

## **XXIII. Frontend Performance Best Practices**

### **23.1 📈 Performance Optimization**

```typescript
/**
 * ✅ BEST PRACTICE 1: Code Splitting & Lazy Loading
 */

// ❌ BAD: Entire app in one bundle
import Dashboard from './pages/Dashboard';
import Admin from './pages/Admin';
import Settings from './pages/Settings';

// ✅ GOOD: Split by route
const Dashboard = lazy(() => import('./pages/Dashboard'));
const Admin = lazy(() => import('./pages/Admin'));
const Settings = lazy(() => import('./pages/Settings'));

function App() {
  return (
    <Suspense fallback={<Loading />}>
      <Routes>
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/admin" element={<Admin />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </Suspense>
  );
}

/**
 * ✅ BEST PRACTICE 2: Image Optimization
 */

// ❌ BAD: Full-size image for thumbnail
function ProductGrid({ products }) {
  return products.map((p) => <img src={p.image} alt={p.name} />);
}

// ✅ GOOD: Lazy load with placeholder
function ProductGrid({ products }) {
  return products.map((p) => (
    <img
      src={p.thumbnail}
      loading="lazy" // ✅ Browser lazy loads
      alt={p.name}
      width={200}
      height={200}
    />
  ));
}

/**
 * ✅ BEST PRACTICE 3: Virtualization for large lists
 */

// ❌ BAD: Render all 10,000 items (DOM bloat)
function VirtualList({ items }) {
  return (
    <div>
      {items.map((item) => (
        <Item key={item.id} {...item} />
      ))}
    </div>
  );
}

// ✅ GOOD: Only render visible items
import { FixedSizeList } from 'react-window';

function VirtualList({ items }) {
  return (
    <FixedSizeList
      height={600}
      itemCount={items.length}
      itemSize={50}
      width="100%"
    >
      {({ index, style }) => (
        <div style={style}>
          <Item {...items[index]} />
        </div>
      )}
    </FixedSizeList>
  );
}

/**
 * ✅ BEST PRACTICE 4: Memoize expensive computations
 */

// ✅ Cache API responses
const cache = new Map();

async function fetchUser(id) {
  if (cache.has(id)) return cache.get(id);

  const data = await fetch(`/api/users/${id}`).then((r) => r.json());
  cache.set(id, data);
  return data;
}

// ✅ Debounce search input
const debouncedSearch = debounce(async (query) => {
  const results = await searchAPI(query);
  setResults(results);
}, 300);
```

### **23.2 🔍 Testing Best Practices**

```typescript
/**
 * ❌ MISTAKE 16: Testing implementation details instead of behavior
 */

// ❌ BAD: Testing internal state/functions
function Counter() {
  const [count, setCount] = useState(0);

  return <button onClick={() => setCount((c) => c + 1)}>Count: {count}</button>;
}

test('Counter', () => {
  const { getByText } = render(<Counter />);
  const state = getByText(/Count/).textContent; // Testing UI, not behavior
  expect(state).toBe('Count: 0');
});

// ✅ GOOD: Test user behavior
test('Counter increments on click', () => {
  render(<Counter />);
  const button = screen.getByRole('button');

  expect(button).toHaveTextContent('Count: 0');

  userEvent.click(button);

  expect(button).toHaveTextContent('Count: 1');
});

/**
 * ✅ BEST PRACTICE 5: Use react-testing-library
 */

// ✅ Test what users see and do
import { render, screen, userEvent } from '@testing-library/react';

test('Login form', async () => {
  render(<LoginForm />);

  const emailInput = screen.getByLabelText(/email/i);
  const submitButton = screen.getByRole('button', { name: /login/i });

  userEvent.type(emailInput, 'user@test.com');
  userEvent.click(submitButton);

  // Wait for success message
  await screen.findByText(/login successful/i);
});

/**
 * ✅ BEST PRACTICE 6: Mock API calls, not components
 */

// ✅ Good: Mock API
import { rest } from 'msw';
import { server } from './mocks/server';

test('Fetch users', async () => {
  server.use(
    rest.get('/api/users', (req, res, ctx) => {
      return res(ctx.json([{ id: 1, name: 'John' }]));
    })
  );

  render(<UserList />);

  await screen.findByText('John');
});
```

### **23.3 ♿ Accessibility Best Practices**

```typescript
/**
 * ✅ BEST PRACTICE 7: Semantic HTML & ARIA
 */

// ❌ BAD: div's for everything
function Dialog() {
  return (
    <div onClick={onClose}>
      <div>Title</div>
      <div>Content</div>
      <button>Close</button>
    </div>
  );
}

// ✅ GOOD: Semantic elements & ARIA
function Dialog() {
  return (
    <div role="dialog" aria-labelledby="title">
      <h2 id="title">Title</h2>
      <p>Content</p>
      <button onClick={onClose}>Close</button>
    </div>
  );
}

/**
 * ✅ BEST PRACTICE 8: Keyboard navigation
 */

// ✅ Use semantic buttons
<button onClick={handleClick}>Action</button>

// ❌ DON'T: Use divs as buttons
<div onClick={handleClick}>Action</div>

/**
 * ✅ BEST PRACTICE 9: Focus management
 */

function Modal() {
  const closeButtonRef = useRef(null);

  useEffect(() => {
    closeButtonRef.current?.focus(); // Focus trap
  }, []);

  return (
    <div role="dialog">
      <button ref={closeButtonRef}>Close</button>
    </div>
  );
}
```

---

## **XXIV. TypeScript with React**

### **24.1 💪 Type Safety**

```typescript
/**
 * ✅ BEST PRACTICE 10: Strong typing for props & state
 */

// ✅ Define component props
interface UserCardProps {
  user: User;
  onDelete?: (id: string) => void;
  loading?: boolean;
}

function UserCard({ user, onDelete, loading }: UserCardProps) {
  return (
    <div>
      <h3>{user.name}</h3>
      {onDelete && <button onClick={() => onDelete(user.id)}>Delete</button>}
    </div>
  );
}

/**
 * ✅ BEST PRACTICE 11: Generic components for reusability
 */

// Generic List component
interface ListProps<T> {
  items: T[];
  renderItem: (item: T) => ReactNode;
  keyExtractor: (item: T) => string | number;
}

function List<T>({ items, renderItem, keyExtractor }: ListProps<T>) {
  return (
    <ul>
      {items.map((item) => (
        <li key={keyExtractor(item)}>{renderItem(item)}</li>
      ))}
    </ul>
  );
}

// Usage
<List<User>
  items={users}
  renderItem={(user) => <UserCard user={user} />}
  keyExtractor={(user) => user.id}
/>;
```

---

## **XXV. 🔥 10 Trường Hợp Xử Lý Frontend Khó & Tâm Đắc Nhất**

> **"Đây là 10 bài toán thực tế mà Senior Frontend Developer thường gặp — mỗi case đều có thể trở thành 'bẫy' nếu không hiểu sâu bản chất."**

---

### **25.1. 🏎️ Race Condition Trong Search/Autocomplete API Calls**

**Vấn đề:** User gõ nhanh trong search input → nhiều request bắn liên tục → response cũ đến SAU response mới → UI hiển thị kết quả sai (stale data).

```
User gõ: "r" → "re" → "rea" → "reac" → "react"
API calls:  ①    ②     ③      ④       ⑤

Response order thực tế (network không đảm bảo thứ tự):
⑤ "react" → trả về trước (nhanh)
③ "rea"   → trả về SAU   (chậm) ← 💥 GHI ĐÈ kết quả đúng!
```

```typescript
// ❌ SAI: Không xử lý race condition
function useSearch(query: string) {
  const [results, setResults] = useState([]);

  useEffect(() => {
    fetch(`/api/search?q=${query}`)
      .then((res) => res.json())
      .then((data) => setResults(data)); // Response cũ có thể ghi đè response mới!
  }, [query]);

  return results;
}

// ✅ ĐÚNG - Cách 1: AbortController (Native, Recommended)
function useSearch(query: string) {
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    if (!query.trim()) {
      setResults([]);
      return;
    }

    const controller = new AbortController();
    setLoading(true);
    setError(null);

    fetch(`/api/search?q=${encodeURIComponent(query)}`, {
      signal: controller.signal,
    })
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
      })
      .then((data) => {
        setResults(data);
        setLoading(false);
      })
      .catch((err) => {
        if (err.name !== 'AbortError') {
          setError(err);
          setLoading(false);
        }
        // AbortError = request bị cancel → KHÔNG update state (đây là key!)
      });

    // Cleanup: Hủy request cũ khi query thay đổi hoặc component unmount
    return () => controller.abort();
  }, [query]);

  return { results, loading, error };
}

// ✅ ĐÚNG - Cách 2: Request ID tracking (cho trường hợp không dùng được AbortController)
function useSearchWithId(query: string) {
  const [results, setResults] = useState([]);
  const latestRequestId = useRef(0);

  useEffect(() => {
    const requestId = ++latestRequestId.current; // Tăng ID mỗi lần gọi

    fetch(`/api/search?q=${query}`)
      .then((res) => res.json())
      .then((data) => {
        // Chỉ update nếu đây là request MỚI NHẤT
        if (requestId === latestRequestId.current) {
          setResults(data);
        }
        // Nếu không → bỏ qua response cũ (stale)
      });
  }, [query]);

  return results;
}

// ✅ ĐÚNG - Cách 3: Kết hợp Debounce + AbortController (Production-grade)
function useDebouncedSearch(query: string, delay = 300) {
  const [results, setResults] = useState([]);
  const [debouncedQuery, setDebouncedQuery] = useState(query);

  // Bước 1: Debounce input (giảm số lượng API calls)
  useEffect(() => {
    const timer = setTimeout(() => setDebouncedQuery(query), delay);
    return () => clearTimeout(timer);
  }, [query, delay]);

  // Bước 2: Fetch với AbortController (xử lý race condition)
  useEffect(() => {
    if (!debouncedQuery) return;
    const controller = new AbortController();

    fetch(`/api/search?q=${debouncedQuery}`, { signal: controller.signal })
      .then((res) => res.json())
      .then(setResults)
      .catch((err) => {
        if (err.name !== 'AbortError') console.error(err);
      });

    return () => controller.abort();
  }, [debouncedQuery]);

  return results;
}
```

**🧠 Bài học:**
- **AbortController** là giải pháp native tốt nhất — hủy cả network request thật sự (tiết kiệm bandwidth)
- **Request ID** là fallback khi API không support abort (WebSocket, GraphQL subscription)
- **Debounce + Abort** là combo tối ưu cho production: giảm calls VÀ đúng thứ tự

---

### **25.2. 🧟 Memory Leak Trong SPA — "Sát Thủ Thầm Lặng"**

**Vấn đề:** SPA không reload trang → memory tích lũy liên tục → app chậm dần → crash sau vài giờ sử dụng.

```typescript
/**
 * 🔴 CÁC NGUỒN MEMORY LEAK PHỔ BIẾN:
 *
 * 1. Event listeners không remove
 * 2. setInterval/setTimeout không clear
 * 3. WebSocket/EventSource không close
 * 4. Closure giữ reference đến DOM đã bị remove
 * 5. Global variables tích lũy data
 * 6. Detached DOM nodes (DOM zombie)
 * 7. IntersectionObserver/MutationObserver không disconnect
 * 8. Large object trong React state không cleanup
 */

// ❌ SAI: Leak ở KHẮP NƠI
function LeakyComponent() {
  const [data, setData] = useState([]);

  useEffect(() => {
    // Leak 1: Event listener trên window không remove
    window.addEventListener('resize', handleResize);

    // Leak 2: setInterval chạy mãi
    setInterval(() => {
      fetch('/api/data').then((r) => r.json()).then(setData);
    }, 5000);

    // Leak 3: WebSocket không close
    const ws = new WebSocket('ws://localhost:3000');
    ws.onmessage = (e) => setData(JSON.parse(e.data));

    // Leak 4: Subscription không unsubscribe
    const subscription = eventBus.on('update', (newData) => {
      setData(newData);
    });

    // Không return cleanup function! 💀
  }, []);

  return <div>{data.length} items</div>;
}

// ✅ ĐÚNG: Cleanup TRIỆT ĐỂ
function CleanComponent() {
  const [data, setData] = useState([]);
  const wsRef = useRef<WebSocket | null>(null);
  const isMountedRef = useRef(true);

  useEffect(() => {
    isMountedRef.current = true;

    // 1. Event listener — lưu reference để remove chính xác
    const handleResize = debounce(() => {
      if (isMountedRef.current) {
        console.log('Resized:', window.innerWidth);
      }
    }, 250);
    window.addEventListener('resize', handleResize);

    // 2. Interval — lưu ID để clear
    const intervalId = setInterval(async () => {
      try {
        const res = await fetch('/api/data');
        const json = await res.json();
        if (isMountedRef.current) setData(json); // Guard: chỉ setState khi còn mount
      } catch (e) {
        console.error('Fetch failed:', e);
      }
    }, 5000);

    // 3. WebSocket — lưu ref để close
    const ws = new WebSocket('ws://localhost:3000');
    wsRef.current = ws;
    ws.onmessage = (e) => {
      if (isMountedRef.current) {
        setData(JSON.parse(e.data));
      }
    };

    // 4. Subscription — lưu unsubscribe function
    const unsubscribe = eventBus.on('update', (newData) => {
      if (isMountedRef.current) setData(newData);
    });

    // ✅ CLEANUP: Dọn dẹp TẤT CẢ khi unmount
    return () => {
      isMountedRef.current = false;
      window.removeEventListener('resize', handleResize);
      handleResize.cancel?.(); // Cancel debounce pending
      clearInterval(intervalId);
      ws.close();
      wsRef.current = null;
      unsubscribe();
    };
  }, []);

  return <div>{data.length} items</div>;
}

// ✅ ADVANCED: Custom hook tái sử dụng cho cleanup pattern
function useCleanup() {
  const cleanups = useRef<Array<() => void>>([]);

  const addCleanup = useCallback((fn: () => void) => {
    cleanups.current.push(fn);
  }, []);

  useEffect(() => {
    return () => {
      cleanups.current.forEach((fn) => fn());
      cleanups.current = [];
    };
  }, []);

  return addCleanup;
}

// Sử dụng:
function MyComponent() {
  const addCleanup = useCleanup();

  useEffect(() => {
    const handler = () => console.log('scroll');
    window.addEventListener('scroll', handler);
    addCleanup(() => window.removeEventListener('scroll', handler));

    const id = setInterval(() => console.log('tick'), 1000);
    addCleanup(() => clearInterval(id));
  }, [addCleanup]);
}
```

**🧠 Bài học:**
- **Quy tắc vàng:** Mỗi `addEventListener` phải có `removeEventListener`, mỗi `setInterval` phải có `clearInterval`
- Dùng `isMountedRef` guard cho async operations để tránh "setState on unmounted component"
- Kiểm tra memory leak bằng Chrome DevTools → Memory tab → Heap Snapshot → Compare

---

### **25.3. 👻 Stale Closure Trong React Hooks — "Bóng Ma Giá Trị Cũ"**

**Vấn đề:** Closure trong useEffect/useCallback/setTimeout capture giá trị tại thời điểm tạo → dùng giá trị cũ (stale) thay vì giá trị mới nhất.

```typescript
// ❌ SAI: Count luôn là 0 trong setInterval (Classic stale closure)
function StaleCounter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const id = setInterval(() => {
      // ⚠️ count ở đây LUÔN = 0 (giá trị lúc useEffect chạy lần đầu)
      // Vì closure "đóng băng" giá trị count = 0
      console.log('Current count:', count); // Luôn log: 0
      setCount(count + 1); // Luôn set: 0 + 1 = 1 → count "đứng yên" ở 1
    }, 1000);
    return () => clearInterval(id);
  }, []); // deps rỗng = chỉ chạy 1 lần = closure chỉ capture count = 0

  return <div>{count}</div>; // Hiển thị: luôn là 1
}

// ✅ ĐÚNG - Cách 1: Functional updater (đơn giản nhất)
function CorrectCounter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const id = setInterval(() => {
      // Functional updater: nhận giá trị HIỆN TẠI (prev), không phụ thuộc closure
      setCount((prev) => prev + 1); // prev luôn là giá trị mới nhất
    }, 1000);
    return () => clearInterval(id);
  }, []);

  return <div>{count}</div>; // Hoạt động đúng: 1, 2, 3, 4...
}

// ✅ ĐÚNG - Cách 2: useRef cho giá trị luôn "tươi mới" (khi cần ĐỌC, không chỉ SET)
function CounterWithRef() {
  const [count, setCount] = useState(0);
  const countRef = useRef(count);
  countRef.current = count; // Luôn sync ref với state mới nhất

  useEffect(() => {
    const id = setInterval(() => {
      // Ref luôn trỏ đến giá trị mới nhất (không bị closure "đóng băng")
      console.log('Current count:', countRef.current); // Giá trị đúng!
      setCount((prev) => prev + 1);
    }, 1000);
    return () => clearInterval(id);
  }, []);

  return <div>{count}</div>;
}

// ✅ ĐÚNG - Cách 3: useEvent pattern (React RFC, tự implement)
// Giải quyết triệt để: callback luôn "tươi" mà ref stable (không trigger re-render)
function useEvent<T extends (...args: any[]) => any>(handler: T): T {
  const handlerRef = useRef(handler);

  // Luôn cập nhật ref khi handler thay đổi (mỗi render)
  useLayoutEffect(() => {
    handlerRef.current = handler;
  });

  // Return stable function (reference không đổi giữa các render)
  return useCallback((...args: any[]) => {
    return handlerRef.current(...args);
  }, []) as T;
}

// Sử dụng useEvent:
function ChatRoom({ roomId, onMessage }) {
  // onSend luôn "thấy" roomId mới nhất, nhưng reference stable
  const onSend = useEvent((text: string) => {
    sendMessage(roomId, text); // roomId luôn mới nhất, không stale!
  });

  useEffect(() => {
    const ws = connectToRoom(roomId);
    ws.on('message', onSend); // Không cần onSend trong deps!
    return () => ws.disconnect();
  }, [roomId]); // Chỉ reconnect khi roomId đổi, không khi onSend đổi
}
```

**🧠 Bài học:**
- **Functional updater** (`setCount(prev => prev + 1)`) giải quyết 80% stale closure khi chỉ cần SET
- **useRef** khi cần ĐỌC giá trị mới nhất trong async code (timer, event handler, WebSocket)
- **useEvent** pattern khi cần callback stable nhưng luôn "thấy" props/state mới nhất
- **Nguyên tắc:** Nếu closure cần giá trị "sống", hãy dùng ref. Nếu chỉ cần update state, dùng functional updater.

---

### **25.4. 🎭 Optimistic UI Updates Với Rollback — "Update Trước, Hỏi Sau"**

**Vấn đề:** Chờ API response rồi mới update UI → UX chậm. Optimistic update UI ngay nhưng phải rollback nếu API fail → phức tạp khi có nhiều concurrent operations.

```typescript
// ❌ SAI: Chờ API xong mới update → UX "lag" 200-2000ms
function PessimisticLike({ postId, initialLikes }) {
  const [likes, setLikes] = useState(initialLikes);
  const [loading, setLoading] = useState(false);

  const handleLike = async () => {
    setLoading(true);
    try {
      const result = await api.likePost(postId); // Chờ 200-2000ms
      setLikes(result.likes); // Mới update UI → user cảm thấy "lag"
    } finally {
      setLoading(false);
    }
  };

  return (
    <button disabled={loading} onClick={handleLike}>
      ❤️ {likes} {loading && '...'}
    </button>
  );
}

// ✅ ĐÚNG: Optimistic Update + Rollback + Error Recovery
function useOptimisticMutation<TData, TVariables>({
  mutationFn,
  onMutate,   // Chạy TRƯỚC API call → update UI optimistic
  onError,    // Rollback khi fail
  onSuccess,  // Sync với server data
  onSettled,  // Chạy cuối cùng (invalidate cache, v.v.)
}: {
  mutationFn: (variables: TVariables) => Promise<TData>;
  onMutate?: (variables: TVariables) => any; // return context for rollback
  onError?: (error: Error, variables: TVariables, context: any) => void;
  onSuccess?: (data: TData, variables: TVariables) => void;
  onSettled?: () => void;
}) {
  const [status, setStatus] = useState<'idle' | 'pending' | 'error'>('idle');
  const contextRef = useRef<any>(null);

  const mutate = useCallback(
    async (variables: TVariables) => {
      setStatus('pending');

      // Bước 1: Lưu snapshot + update UI optimistic
      const context = onMutate?.(variables);
      contextRef.current = context;

      try {
        // Bước 2: Gọi API thật
        const data = await mutationFn(variables);

        // Bước 3: Thành công → sync server data
        onSuccess?.(data, variables);
        setStatus('idle');
      } catch (error) {
        // Bước 4: Thất bại → ROLLBACK về snapshot
        onError?.(error as Error, variables, contextRef.current);
        setStatus('error');
      } finally {
        onSettled?.();
      }
    },
    [mutationFn, onMutate, onError, onSuccess, onSettled]
  );

  return { mutate, status };
}

// ✅ Sử dụng trong component:
function OptimisticLike({ postId, initialLikes, isLiked: initialIsLiked }) {
  const [likes, setLikes] = useState(initialLikes);
  const [isLiked, setIsLiked] = useState(initialIsLiked);

  const { mutate: toggleLike, status } = useOptimisticMutation({
    mutationFn: (variables: { postId: string }) =>
      api.toggleLike(variables.postId),

    onMutate: () => {
      // Lưu snapshot TRƯỚC khi thay đổi
      const snapshot = { likes, isLiked };

      // Update UI NGAY LẬP TỨC (0ms delay!)
      setIsLiked((prev) => !prev);
      setLikes((prev) => (isLiked ? prev - 1 : prev + 1));

      return snapshot; // Return context cho rollback
    },

    onError: (_error, _variables, snapshot) => {
      // API lỗi → ROLLBACK về trạng thái cũ
      setLikes(snapshot.likes);
      setIsLiked(snapshot.isLiked);
      toast.error('Không thể thực hiện. Vui lòng thử lại.');
    },

    onSuccess: (serverData) => {
      // Sync chính xác từ server (source of truth)
      setLikes(serverData.likes);
      setIsLiked(serverData.isLiked);
    },
  });

  return (
    <button
      onClick={() => toggleLike({ postId })}
      className={isLiked ? 'liked' : ''}
      disabled={status === 'pending'}
    >
      {isLiked ? '❤️' : '🤍'} {likes}
    </button>
  );
}

// ✅ ADVANCED: Optimistic update cho TODO list (thêm/xóa/sửa)
function useTodosOptimistic() {
  const [todos, setTodos] = useState<Todo[]>([]);

  const addTodo = useOptimisticMutation({
    mutationFn: (newTodo: Omit<Todo, 'id'>) => api.createTodo(newTodo),

    onMutate: (newTodo) => {
      const tempId = `temp-${Date.now()}`; // ID tạm
      const optimisticTodo = { ...newTodo, id: tempId, _isOptimistic: true };
      const snapshot = [...todos];

      setTodos((prev) => [...prev, optimisticTodo]);
      return { snapshot, tempId };
    },

    onError: (_err, _vars, ctx) => {
      setTodos(ctx.snapshot); // Rollback toàn bộ list
    },

    onSuccess: (serverTodo, _vars) => {
      // Thay thế todo tạm bằng todo thật từ server
      setTodos((prev) =>
        prev.map((t) => (t._isOptimistic ? serverTodo : t))
      );
    },
  });

  return { todos, addTodo: addTodo.mutate };
}
```

**🧠 Bài học:**
- **Optimistic UI** = update ngay → rollback nếu fail. Instagram, Twitter, Facebook đều dùng pattern này
- Key: Luôn lưu **snapshot** trước khi optimistic update để có thể rollback chính xác
- Dùng **tempId** cho item mới, replace bằng server ID khi success
- TanStack Query (`useMutation` với `onMutate`) implement pattern này sẵn — nên dùng trong production

---

### **25.5. 📜 Virtualized List — Render 100K Items Mà Không Chết Browser**

**Vấn đề:** Render danh sách lớn (10K-1M items) → tạo hàng nghìn DOM nodes → layout/paint chậm → scroll giật → browser freeze.

```typescript
/**
 * 🔴 VẤN ĐỀ:
 * - 10,000 items × ~10 DOM nodes/item = 100,000 DOM nodes
 * - Browser phải layout, paint, composite TẤT CẢ
 * - Scroll handler fire 60+ lần/giây
 * - Memory: ~500MB cho 100K DOM nodes
 *
 * ✅ GIẢI PHÁP: Chỉ render items ĐANG THẤY trên màn hình
 * - Viewport hiển thị ~20 items → chỉ tạo ~25 DOM nodes (có buffer)
 * - Scroll → recycle DOM nodes (thay data, không tạo mới)
 */

// ✅ Custom Virtual List từ đầu (hiểu bản chất)
function useVirtualList<T>({
  items,
  itemHeight,
  containerHeight,
  overscan = 5, // Số items render thêm bên trên/dưới viewport (smooth scroll)
}: {
  items: T[];
  itemHeight: number;
  containerHeight: number;
  overscan?: number;
}) {
  const [scrollTop, setScrollTop] = useState(0);

  // Tính toán items nào đang visible
  const totalHeight = items.length * itemHeight; // Tổng chiều cao ảo
  const startIndex = Math.max(0, Math.floor(scrollTop / itemHeight) - overscan);
  const endIndex = Math.min(
    items.length - 1,
    Math.ceil((scrollTop + containerHeight) / itemHeight) + overscan
  );

  const visibleItems = items.slice(startIndex, endIndex + 1).map((item, i) => ({
    item,
    index: startIndex + i,
    style: {
      position: 'absolute' as const,
      top: (startIndex + i) * itemHeight,
      height: itemHeight,
      width: '100%',
    },
  }));

  const onScroll = useCallback((e: React.UIEvent<HTMLDivElement>) => {
    // requestAnimationFrame để batch scroll events → smooth
    requestAnimationFrame(() => {
      setScrollTop(e.currentTarget.scrollTop);
    });
  }, []);

  return { visibleItems, totalHeight, onScroll };
}

// Sử dụng:
function VirtualizedTable({ data }: { data: User[] }) {
  const containerRef = useRef<HTMLDivElement>(null);
  const { visibleItems, totalHeight, onScroll } = useVirtualList({
    items: data,
    itemHeight: 50,
    containerHeight: 600,
    overscan: 10,
  });

  return (
    <div
      ref={containerRef}
      onScroll={onScroll}
      style={{ height: 600, overflow: 'auto', position: 'relative' }}
    >
      {/* Spacer tạo scrollbar đúng kích thước */}
      <div style={{ height: totalHeight, position: 'relative' }}>
        {visibleItems.map(({ item, index, style }) => (
          <div key={index} style={style}>
            <UserRow user={item} />
          </div>
        ))}
      </div>
    </div>
  );
}

// ✅ ADVANCED: Virtual List với DYNAMIC item height (khó hơn rất nhiều)
function useDynamicVirtualList<T>({
  items,
  estimatedItemHeight,
  containerHeight,
  overscan = 5,
}: {
  items: T[];
  estimatedItemHeight: number;
  containerHeight: number;
  overscan?: number;
}) {
  const [scrollTop, setScrollTop] = useState(0);
  // Cache chiều cao thực của mỗi item sau khi render
  const measuredHeights = useRef<Map<number, number>>(new Map());

  // Tính vị trí Top của mỗi item dựa trên chiều cao đã measure
  const getItemOffset = useCallback(
    (index: number) => {
      let offset = 0;
      for (let i = 0; i < index; i++) {
        offset += measuredHeights.current.get(i) ?? estimatedItemHeight;
      }
      return offset;
    },
    [estimatedItemHeight]
  );

  // Tìm item đầu tiên visible bằng binary search (O(log n) thay vì O(n))
  const findStartIndex = useCallback(
    (scrollPos: number) => {
      let low = 0,
        high = items.length - 1;
      while (low <= high) {
        const mid = Math.floor((low + high) / 2);
        const offset = getItemOffset(mid);
        if (offset < scrollPos) low = mid + 1;
        else high = mid - 1;
      }
      return Math.max(0, low - 1);
    },
    [items.length, getItemOffset]
  );

  // Measure item sau khi render
  const measureItem = useCallback(
    (index: number, element: HTMLElement | null) => {
      if (element) {
        const height = element.getBoundingClientRect().height;
        if (measuredHeights.current.get(index) !== height) {
          measuredHeights.current.set(index, height);
        }
      }
    },
    []
  );

  const startIndex = Math.max(0, findStartIndex(scrollTop) - overscan);
  // ... tương tự tính endIndex

  return { startIndex, measureItem /* ... */ };
}
```

**🧠 Bài học:**
- **Fixed height:** Dùng `react-window` hoặc `@tanstack/react-virtual` — đơn giản, hiệu quả
- **Dynamic height:** Dùng `react-virtuoso` hoặc tự implement với ResizeObserver + height cache
- Key insight: Không tạo DOM node cho item không visible → O(viewport) thay vì O(n)
- Production: Luôn dùng thư viện đã battle-tested, chỉ tự implement khi cần custom đặc biệt

---

### **25.6. 🔌 WebSocket Reconnection Với Exponential Backoff**

**Vấn đề:** WebSocket disconnect do mất mạng/server restart → cần auto-reconnect thông minh, không flood server, queue messages offline, sync state khi reconnect.

```typescript
/**
 * 🔴 THỰC TẾ:
 * - Mobile user vào tunnel → mất mạng 30 giây → cần auto reconnect
 * - Server deploy mới → tất cả connections bị drop → 10K users reconnect cùng lúc
 * - Nếu reconnect ngay lập tức → DDoS chính server của mình!
 *
 * ✅ GIẢI PHÁP: Exponential Backoff + Jitter + Message Queue
 */

type ConnectionState = 'connecting' | 'connected' | 'disconnected' | 'reconnecting';

class ResilientWebSocket {
  private ws: WebSocket | null = null;
  private url: string;
  private reconnectAttempts = 0;
  private maxReconnectAttempts = 10;
  private messageQueue: string[] = []; // Queue messages khi offline
  private listeners = new Map<string, Set<Function>>();
  private state: ConnectionState = 'disconnected';
  private reconnectTimer: ReturnType<typeof setTimeout> | null = null;
  private heartbeatTimer: ReturnType<typeof setInterval> | null = null;

  constructor(url: string) {
    this.url = url;
    this.connect();
  }

  private connect() {
    this.setState('connecting');

    try {
      this.ws = new WebSocket(this.url);

      this.ws.onopen = () => {
        console.log(`✅ WebSocket connected (attempt ${this.reconnectAttempts})`);
        this.setState('connected');
        this.reconnectAttempts = 0; // Reset counter on success

        // Flush queued messages
        this.flushMessageQueue();

        // Start heartbeat (detect dead connections)
        this.startHeartbeat();
      };

      this.ws.onmessage = (event) => {
        const data = JSON.parse(event.data);

        if (data.type === 'pong') return; // Heartbeat response

        // Emit to listeners
        this.listeners.get(data.type)?.forEach((fn) => fn(data.payload));
        this.listeners.get('*')?.forEach((fn) => fn(data)); // Wildcard
      };

      this.ws.onclose = (event) => {
        console.log(`❌ WebSocket closed: code=${event.code} reason=${event.reason}`);
        this.stopHeartbeat();

        // 1000 = normal close (user navigated away) → don't reconnect
        // 1001 = going away → don't reconnect
        if (event.code !== 1000 && event.code !== 1001) {
          this.scheduleReconnect();
        } else {
          this.setState('disconnected');
        }
      };

      this.ws.onerror = (error) => {
        console.error('WebSocket error:', error);
        // onclose sẽ fire sau onerror → reconnect logic ở onclose
      };
    } catch (error) {
      console.error('WebSocket connection failed:', error);
      this.scheduleReconnect();
    }
  }

  // ⭐ EXPONENTIAL BACKOFF + JITTER
  private getReconnectDelay(): number {
    // Base delay: 1s, 2s, 4s, 8s, 16s, 32s (cap at 30s)
    const baseDelay = Math.min(
      1000 * Math.pow(2, this.reconnectAttempts),
      30000
    );

    // Add jitter: ±30% randomness (tránh tất cả clients reconnect cùng lúc)
    const jitter = baseDelay * 0.3 * (Math.random() * 2 - 1);

    return Math.max(1000, baseDelay + jitter);
  }

  private scheduleReconnect() {
    if (this.reconnectAttempts >= this.maxReconnectAttempts) {
      console.error('❌ Max reconnect attempts reached. Giving up.');
      this.setState('disconnected');
      this.emit('max_retries_reached', null);
      return;
    }

    const delay = this.getReconnectDelay();
    this.reconnectAttempts++;
    this.setState('reconnecting');

    console.log(
      `🔄 Reconnect attempt ${this.reconnectAttempts}/${this.maxReconnectAttempts} in ${delay}ms`
    );

    this.reconnectTimer = setTimeout(() => this.connect(), delay);
  }

  // Queue messages khi offline → flush khi reconnect
  send(type: string, payload: any) {
    const message = JSON.stringify({ type, payload });

    if (this.ws?.readyState === WebSocket.OPEN) {
      this.ws.send(message);
    } else {
      console.log('📦 Queuing message (offline):', type);
      this.messageQueue.push(message);
    }
  }

  private flushMessageQueue() {
    console.log(`📤 Flushing ${this.messageQueue.length} queued messages`);
    while (this.messageQueue.length > 0) {
      const msg = this.messageQueue.shift()!;
      this.ws?.send(msg);
    }
  }

  // Heartbeat: detect zombie connections (connected but not actually working)
  private startHeartbeat() {
    this.heartbeatTimer = setInterval(() => {
      if (this.ws?.readyState === WebSocket.OPEN) {
        this.ws.send(JSON.stringify({ type: 'ping' }));
      }
    }, 30000); // Ping mỗi 30s
  }

  private stopHeartbeat() {
    if (this.heartbeatTimer) {
      clearInterval(this.heartbeatTimer);
      this.heartbeatTimer = null;
    }
  }

  // Event system
  on(event: string, callback: Function) {
    if (!this.listeners.has(event)) this.listeners.set(event, new Set());
    this.listeners.get(event)!.add(callback);
    return () => this.listeners.get(event)?.delete(callback); // Unsubscribe fn
  }

  private emit(event: string, data: any) {
    this.listeners.get(event)?.forEach((fn) => fn(data));
  }

  private setState(state: ConnectionState) {
    this.state = state;
    this.emit('connection_state', state);
  }

  destroy() {
    this.reconnectTimer && clearTimeout(this.reconnectTimer);
    this.stopHeartbeat();
    this.ws?.close(1000, 'Client closing');
    this.listeners.clear();
    this.messageQueue = [];
  }
}

// ✅ React Hook wrapper
function useWebSocket(url: string) {
  const wsRef = useRef<ResilientWebSocket | null>(null);
  const [connectionState, setConnectionState] = useState<ConnectionState>('disconnected');

  useEffect(() => {
    const ws = new ResilientWebSocket(url);
    wsRef.current = ws;

    const unsub = ws.on('connection_state', setConnectionState);

    return () => {
      unsub();
      ws.destroy();
      wsRef.current = null;
    };
  }, [url]);

  const send = useCallback((type: string, payload: any) => {
    wsRef.current?.send(type, payload);
  }, []);

  const subscribe = useCallback((event: string, callback: Function) => {
    return wsRef.current?.on(event, callback);
  }, []);

  return { send, subscribe, connectionState };
}
```

**🧠 Bài học:**
- **Exponential Backoff** tránh flood server: 1s → 2s → 4s → 8s → ... (cap at 30s)
- **Jitter** (random delay) tránh "thundering herd" khi 10K clients reconnect cùng lúc
- **Message Queue** không mất data khi offline
- **Heartbeat** phát hiện "zombie connections" (TCP connected nhưng thực tế đã chết)

---

### **25.7. 🔄 Cross-Tab State Synchronization — Đồng Bộ Giữa Nhiều Tab**

**Vấn đề:** User mở app trên nhiều tab → login/logout ở 1 tab nhưng tab khác không biết → inconsistent state, security risk (logout ở tab A nhưng tab B vẫn truy cập được).

```typescript
/**
 * 🔴 THỰC TẾ:
 * - User logout ở tab 1 → tab 2, 3 vẫn "logged in" → security risk
 * - User thay đổi theme/language ở tab 1 → tab khác không đổi → UX không nhất quán
 * - User thêm item vào cart ở tab 1 → tab 2 không thấy → data mismatch
 *
 * ✅ GIẢI PHÁP: BroadcastChannel API + Storage Event + Fallback
 */

// ✅ Cross-Tab Communication Service
class CrossTabSync {
  private channel: BroadcastChannel | null = null;
  private listeners = new Map<string, Set<(data: any) => void>>();
  private instanceId = crypto.randomUUID(); // Identify this tab

  constructor(channelName = 'app-sync') {
    // BroadcastChannel: Modern API, đáng tin cậy hơn storage event
    if ('BroadcastChannel' in window) {
      this.channel = new BroadcastChannel(channelName);
      this.channel.onmessage = (event) => this.handleMessage(event.data);
    }

    // Fallback: localStorage event (hỗ trợ IE11+)
    // Lưu ý: storage event chỉ fire ở TAB KHÁC, không ở tab hiện tại
    window.addEventListener('storage', (event) => {
      if (event.key === `__sync_${channelName}` && event.newValue) {
        try {
          this.handleMessage(JSON.parse(event.newValue));
        } catch {}
      }
    });
  }

  // Broadcast message đến TẤT CẢ tab khác
  broadcast(type: string, payload: any) {
    const message = {
      type,
      payload,
      senderId: this.instanceId,
      timestamp: Date.now(),
    };

    // BroadcastChannel
    this.channel?.postMessage(message);

    // Fallback: localStorage (trigger storage event ở tab khác)
    try {
      localStorage.setItem(
        '__sync_cross_tab',
        JSON.stringify(message)
      );
      // Xóa ngay để có thể gửi cùng message lại
      localStorage.removeItem('__sync_cross_tab');
    } catch {}
  }

  private handleMessage(message: { type: string; payload: any; senderId: string }) {
    // Ignore messages from self
    if (message.senderId === this.instanceId) return;

    this.listeners.get(message.type)?.forEach((fn) => fn(message.payload));
    this.listeners.get('*')?.forEach((fn) => fn(message));
  }

  on(type: string, callback: (data: any) => void) {
    if (!this.listeners.has(type)) this.listeners.set(type, new Set());
    this.listeners.get(type)!.add(callback);
    return () => this.listeners.get(type)?.delete(callback);
  }

  destroy() {
    this.channel?.close();
    this.listeners.clear();
  }
}

// ✅ React Hook
function useCrossTabSync() {
  const syncRef = useRef<CrossTabSync | null>(null);

  useEffect(() => {
    syncRef.current = new CrossTabSync();
    return () => syncRef.current?.destroy();
  }, []);

  return syncRef.current;
}

// ✅ SỬ DỤNG THỰC TẾ: Sync Auth State
function useAuthSync() {
  const sync = useCrossTabSync();
  const { logout, setUser } = useAuth();

  useEffect(() => {
    if (!sync) return;

    // Khi tab khác logout → tab này cũng logout
    const unsubLogout = sync.on('AUTH_LOGOUT', () => {
      console.log('🔒 Another tab logged out. Syncing...');
      logout(); // Clear token, redirect to login
    });

    // Khi tab khác login → tab này cập nhật user
    const unsubLogin = sync.on('AUTH_LOGIN', (user) => {
      console.log('🔓 Another tab logged in:', user.email);
      setUser(user);
    });

    // Khi tab khác refresh token → tab này dùng token mới
    const unsubToken = sync.on('TOKEN_REFRESHED', (newToken) => {
      localStorage.setItem('access_token', newToken);
    });

    return () => {
      unsubLogout();
      unsubLogin();
      unsubToken();
    };
  }, [sync, logout, setUser]);

  // Broadcast khi tab này thay đổi auth state
  const broadcastLogout = useCallback(() => {
    sync?.broadcast('AUTH_LOGOUT', null);
  }, [sync]);

  const broadcastLogin = useCallback(
    (user: User) => {
      sync?.broadcast('AUTH_LOGIN', user);
    },
    [sync]
  );

  return { broadcastLogout, broadcastLogin };
}

// ✅ SỬ DỤNG: Sync Theme/Language
function useThemeSync() {
  const [theme, setTheme] = useState(localStorage.getItem('theme') || 'light');
  const sync = useCrossTabSync();

  useEffect(() => {
    if (!sync) return;
    return sync.on('THEME_CHANGED', (newTheme) => {
      setTheme(newTheme);
      document.documentElement.setAttribute('data-theme', newTheme);
    });
  }, [sync]);

  const changeTheme = useCallback(
    (newTheme: string) => {
      setTheme(newTheme);
      localStorage.setItem('theme', newTheme);
      document.documentElement.setAttribute('data-theme', newTheme);
      sync?.broadcast('THEME_CHANGED', newTheme);
    },
    [sync]
  );

  return { theme, changeTheme };
}
```

**🧠 Bài học:**
- **BroadcastChannel** > **localStorage event** > **SharedWorker** (theo thứ tự dễ dùng)
- **Auth sync** là use case quan trọng nhất — logout phải sync ngay lập tức (security)
- Luôn ignore messages từ tab `self` (senderId check) để tránh infinite loop
- **Leader Election** (chọn 1 tab làm "master") hữu ích cho single-connection resources (WebSocket, polling)

---

### **25.8. 🛡️ XSS Prevention Trong Rich Text Editor — "Sanitize Mà Không Phá Layout"**

**Vấn đề:** Rich text editor cho user nhập HTML → phải cho phép `<b>`, `<i>`, `<img>` nhưng chặn `<script>`, `onerror`, `javascript:` → sanitize quá chặt thì mất formatting, quá lỏng thì bị XSS.

```typescript
/**
 * 🔴 XSS ATTACK VECTORS TRONG RICH TEXT:
 *
 * 1. <script>alert('XSS')</script>                    ← Classic
 * 2. <img src=x onerror="alert('XSS')">               ← Event handler
 * 3. <a href="javascript:alert('XSS')">Click</a>      ← Protocol
 * 4. <div style="background:url(javascript:alert(1))"> ← CSS expression
 * 5. <svg onload="alert('XSS')">                       ← SVG events
 * 6. <math><mi href="javascript:alert(1)">click</mi>   ← MathML
 * 7. <details open ontoggle="alert('XSS')">            ← Attribute event
 * 8. &#x3C;script&#x3E;alert(1)&#x3C;/script&#x3E;    ← HTML entities
 */

// ❌ SAI: innerHTML không sanitize
function DangerousRenderer({ html }: { html: string }) {
  return <div dangerouslySetInnerHTML={{ __html: html }} />; // 💀 XSS!
}

// ❌ SAI: Regex sanitize (LUÔN bị bypass)
function naiveSanitize(html: string): string {
  // Hacker bypass dễ dàng: <scr<script>ipt>, <SCRIPT>, <img src=x onerror=alert(1)>
  return html.replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '');
}

// ✅ ĐÚNG: Whitelist-based sanitization với DOMPurify
import DOMPurify from 'dompurify';

// Cấu hình whitelist chặt chẽ
const SANITIZE_CONFIG: DOMPurify.Config = {
  // Chỉ cho phép các tag an toàn
  ALLOWED_TAGS: [
    'p', 'br', 'b', 'i', 'u', 'strong', 'em', 'strike', 's',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'ul', 'ol', 'li',
    'a', 'img',
    'blockquote', 'pre', 'code',
    'table', 'thead', 'tbody', 'tr', 'th', 'td',
    'span', 'div', 'sub', 'sup',
  ],
  // Chỉ cho phép attributes an toàn
  ALLOWED_ATTR: [
    'href', 'src', 'alt', 'title', 'width', 'height',
    'class', 'id', 'target', 'rel',
    'colspan', 'rowspan',
    'style', // Cẩn thận với style — cần thêm CSS sanitizer
  ],
  // Chỉ cho phép protocol an toàn
  ALLOWED_URI_REGEXP: /^(?:(?:https?|mailto|tel):|[^a-z]|[a-z+.-]+(?:[^a-z+.\-:]|$))/i,

  // Thêm rel="noopener noreferrer" cho tất cả links (chống tab-napping)
  ADD_ATTR: ['target'],
  FORBID_ATTR: ['onerror', 'onload', 'onclick', 'onmouseover'], // Block event handlers
  FORBID_TAGS: ['script', 'style', 'iframe', 'object', 'embed', 'form', 'input'],
};

// Hook: afterSanitizeAttributes — thêm security attributes
DOMPurify.addHook('afterSanitizeAttributes', (node) => {
  // Force all links to open in new tab safely
  if (node.tagName === 'A') {
    node.setAttribute('target', '_blank');
    node.setAttribute('rel', 'noopener noreferrer');
  }

  // Remove dangerous CSS properties
  if (node.hasAttribute('style')) {
    const style = node.getAttribute('style') || '';
    const dangerousPatterns = [
      /expression\s*\(/gi,      // IE CSS expression
      /javascript\s*:/gi,       // javascript protocol in CSS
      /url\s*\(\s*['"]*\s*javascript/gi, // url(javascript:...)
      /behavior\s*:/gi,         // IE behavior
      /-moz-binding/gi,         // Firefox binding
    ];
    const isDangerous = dangerousPatterns.some((p) => p.test(style));
    if (isDangerous) {
      node.removeAttribute('style');
    }
  }
});

// ✅ Safe Rich Text Renderer
function SafeRichTextRenderer({ html }: { html: string }) {
  const sanitizedHtml = useMemo(
    () => DOMPurify.sanitize(html, SANITIZE_CONFIG),
    [html]
  );

  return (
    <div
      className="rich-text-content"
      dangerouslySetInnerHTML={{ __html: sanitizedHtml }}
    />
  );
}

// ✅ ADVANCED: CSP (Content Security Policy) Headers
/**
 * Server-side headers (thêm vào nginx/express):
 *
 * Content-Security-Policy:
 *   default-src 'self';
 *   script-src 'self' 'nonce-abc123';     ← Chỉ chạy script có nonce
 *   style-src 'self' 'unsafe-inline';     ← Cho phép inline CSS
 *   img-src 'self' https: data:;          ← Images từ HTTPS + data URI
 *   connect-src 'self' https://api.myapp.com; ← API calls chỉ đến domain tin cậy
 *   frame-src 'none';                     ← Không cho phép iframe
 *   object-src 'none';                    ← Chặn Flash/plugins
 */
```

**🧠 Bài học:**
- **KHÔNG BAO GIỜ** dùng regex để sanitize HTML — luôn bị bypass
- **DOMPurify** là gold standard cho client-side HTML sanitization
- **Whitelist** > **Blacklist**: Cho phép những gì cần, chặn mọi thứ khác
- **Defense in Depth**: DOMPurify (client) + CSP headers (server) + HttpOnly cookies

---

### **25.9. ⚡ Concurrent Data Fetching Với Error Boundaries & Suspense**

**Vấn đề:** Component cần data từ nhiều API → fetch tuần tự (waterfall) → chậm. Fetch song song nhưng phải xử lý: partial failure, loading states riêng biệt, error recovery cho từng phần.

```typescript
/**
 * 🔴 WATERFALL PROBLEM:
 *
 * ❌ Tuần tự (3000ms total):
 * ──[User API 1000ms]──[Posts API 1000ms]──[Comments API 1000ms]──
 *
 * ✅ Song song (1000ms total — nhanh gấp 3!):
 * ──[User API    1000ms]──
 * ──[Posts API   1000ms]──
 * ──[Comments API 1000ms]──
 */

// ❌ SAI: Waterfall pattern (rất phổ biến ở Junior developers)
function ProfilePage({ userId }) {
  const [user, setUser] = useState(null);
  const [posts, setPosts] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      const userData = await fetchUser(userId);     // 1000ms
      setUser(userData);
      const postsData = await fetchPosts(userId);   // + 1000ms (chờ user xong)
      setPosts(postsData);
      setLoading(false);                             // Total: 2000ms 😫
    }
    fetchData();
  }, [userId]);
  // ...
}

// ✅ ĐÚNG - Cách 1: Promise.allSettled (Song song + Partial failure handling)
function useParallelFetch<T extends Record<string, () => Promise<any>>>(
  fetchers: T
): {
  data: { [K in keyof T]: Awaited<ReturnType<T[K]>> | null };
  errors: { [K in keyof T]: Error | null };
  loading: boolean;
  retry: (key: keyof T) => void;
} {
  type DataMap = { [K in keyof T]: any };

  const [data, setData] = useState<DataMap>({} as DataMap);
  const [errors, setErrors] = useState<{ [K in keyof T]: Error | null }>(
    {} as any
  );
  const [loading, setLoading] = useState(true);
  const fetchersRef = useRef(fetchers);
  fetchersRef.current = fetchers;

  const fetchAll = useCallback(async () => {
    setLoading(true);
    const keys = Object.keys(fetchersRef.current) as Array<keyof T>;

    // Tất cả API gọi CÙNG LÚC
    const results = await Promise.allSettled(
      keys.map((key) => fetchersRef.current[key]())
    );

    const newData: any = {};
    const newErrors: any = {};

    results.forEach((result, index) => {
      const key = keys[index];
      if (result.status === 'fulfilled') {
        newData[key] = result.value;
        newErrors[key] = null;
      } else {
        newData[key] = null;
        newErrors[key] = result.reason;
      }
    });

    setData(newData);
    setErrors(newErrors);
    setLoading(false);
  }, []);

  // Retry individual failed request
  const retry = useCallback(async (key: keyof T) => {
    try {
      const result = await fetchersRef.current[key]();
      setData((prev) => ({ ...prev, [key]: result }));
      setErrors((prev) => ({ ...prev, [key]: null }));
    } catch (err) {
      setErrors((prev) => ({ ...prev, [key]: err as Error }));
    }
  }, []);

  useEffect(() => {
    fetchAll();
  }, [fetchAll]);

  return { data, errors, loading, retry };
}

// Sử dụng:
function ProfilePage({ userId }: { userId: string }) {
  const { data, errors, loading, retry } = useParallelFetch({
    user: () => fetchUser(userId),
    posts: () => fetchPosts(userId),
    comments: () => fetchComments(userId),
    notifications: () => fetchNotifications(userId),
  });

  if (loading) return <FullPageSkeleton />;

  return (
    <div>
      {/* User section - critical, show error prominently */}
      {errors.user ? (
        <ErrorCard
          message="Không tải được thông tin user"
          onRetry={() => retry('user')}
        />
      ) : (
        <UserProfile user={data.user} />
      )}

      {/* Posts section - degrade gracefully */}
      {errors.posts ? (
        <InlineError onRetry={() => retry('posts')}>
          Không tải được bài viết
        </InlineError>
      ) : (
        <PostList posts={data.posts} />
      )}

      {/* Notifications - optional, hide on error */}
      {data.notifications && (
        <NotificationBadge count={data.notifications.length} />
      )}
    </div>
  );
}

// ✅ ĐÚNG - Cách 2: React Suspense + Error Boundary (Declarative)
// Tạo resource cho Suspense (React 18+)
function createResource<T>(promise: Promise<T>) {
  let status: 'pending' | 'success' | 'error' = 'pending';
  let result: T;
  let error: Error;

  const suspender = promise.then(
    (data) => {
      status = 'success';
      result = data;
    },
    (err) => {
      status = 'error';
      error = err;
    }
  );

  return {
    read(): T {
      switch (status) {
        case 'pending':
          throw suspender; // Suspense catches this!
        case 'error':
          throw error; // Error Boundary catches this!
        case 'success':
          return result;
      }
    },
  };
}

// Error Boundary component
class ErrorBoundary extends React.Component<
  { fallback: React.ComponentType<{ error: Error; retry: () => void }>; children: React.ReactNode },
  { error: Error | null }
> {
  state = { error: null as Error | null };

  static getDerivedStateFromError(error: Error) {
    return { error };
  }

  retry = () => this.setState({ error: null });

  render() {
    if (this.state.error) {
      const Fallback = this.props.fallback;
      return <Fallback error={this.state.error} retry={this.retry} />;
    }
    return this.props.children;
  }
}

// Declarative data fetching:
function ProfilePageSuspense({ userId }) {
  const userResource = useMemo(() => createResource(fetchUser(userId)), [userId]);
  const postsResource = useMemo(() => createResource(fetchPosts(userId)), [userId]);

  return (
    <div>
      <ErrorBoundary fallback={UserError}>
        <Suspense fallback={<UserSkeleton />}>
          <UserSection resource={userResource} />
        </Suspense>
      </ErrorBoundary>

      <ErrorBoundary fallback={PostsError}>
        <Suspense fallback={<PostsSkeleton />}>
          <PostsSection resource={postsResource} />
        </Suspense>
      </ErrorBoundary>
    </div>
  );
}

function UserSection({ resource }) {
  const user = resource.read(); // Suspense "pauses" render until data ready
  return <UserProfile user={user} />;
}
```

**🧠 Bài học:**
- **Promise.allSettled** > **Promise.all** cho UI: allSettled không fail-fast, từng phần có thể thất bại độc lập
- **Partial failure**: UI degrade gracefully — phần nào lỗi thì hiện error + retry, phần khác vẫn hoạt động
- **Suspense** model: Declarative, clean code. Data fetching trở thành "synchronous-looking"
- **Error Boundary** per section: Lỗi 1 phần không crash toàn bộ page

---

### **25.10. 🎨 Layout Shift Prevention & Skeleton UI — "Chống Nhảy Giao Diện"**

**Vấn đề:** Content load không đều → layout nhảy lung tung (CLS — Cumulative Layout Shift) → user click nhầm button, UX tệ, Google SEO penalty.

```typescript
/**
 * 🔴 CLS (Cumulative Layout Shift) — Core Web Vital:
 * - Điểm CLS > 0.1 → Google coi là "poor experience" → giảm SEO ranking
 * - Nguyên nhân phổ biến:
 *   1. Image/video không có width/height → load xong mới biết kích thước → đẩy content
 *   2. Font load muộn (FOUT/FOIT) → text nhảy khi font swap
 *   3. Dynamic content inject (ads, banners) → đẩy content xuống
 *   4. Async data load → skeleton → real content (height khác nhau)
 */

// ❌ SAI: Image không có kích thước → CLS khi load
function BadImage() {
  return <img src="/hero.jpg" />; // Browser không biết size → layout shift khi load xong
}

// ✅ ĐÚNG: Luôn specify dimensions hoặc aspect-ratio
function GoodImage() {
  return (
    <img
      src="/hero.jpg"
      width={1200}
      height={600}
      alt="Hero banner"
      loading="lazy"
      decoding="async"
      style={{ aspectRatio: '2/1', width: '100%', height: 'auto' }}
    />
  );
}

// ✅ Smart Skeleton component — Match kích thước thật để tránh CLS
interface SkeletonProps {
  width?: string | number;
  height?: string | number;
  variant?: 'text' | 'circular' | 'rectangular' | 'rounded';
  lines?: number; // Số dòng text skeleton
  animation?: 'pulse' | 'wave' | 'none';
}

function Skeleton({
  width = '100%',
  height = 20,
  variant = 'text',
  lines = 1,
  animation = 'wave',
}: SkeletonProps) {
  const baseStyle: React.CSSProperties = {
    backgroundColor: '#e0e0e0',
    borderRadius:
      variant === 'circular' ? '50%' : variant === 'rounded' ? 8 : 4,
    width,
    height,
    display: 'block',
  };

  if (lines > 1) {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
        {Array.from({ length: lines }).map((_, i) => (
          <div
            key={i}
            className={`skeleton-${animation}`}
            style={{
              ...baseStyle,
              // Dòng cuối ngắn hơn → trông tự nhiên hơn
              width: i === lines - 1 ? '60%' : width,
            }}
          />
        ))}
      </div>
    );
  }

  return <div className={`skeleton-${animation}`} style={baseStyle} />;
}

// ✅ Content-Aware Skeleton: Match layout thật CHÍNH XÁC
function PostCardSkeleton() {
  return (
    <div style={{ padding: 16, border: '1px solid #eee', borderRadius: 8 }}>
      {/* Avatar + Name row */}
      <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
        <Skeleton variant="circular" width={40} height={40} />
        <div style={{ flex: 1 }}>
          <Skeleton width="30%" height={16} />
          <Skeleton width="20%" height={12} style={{ marginTop: 4 }} />
        </div>
      </div>

      {/* Content */}
      <div style={{ marginTop: 12 }}>
        <Skeleton lines={3} height={14} />
      </div>

      {/* Image placeholder — SAME aspect ratio as real image */}
      <Skeleton
        variant="rounded"
        width="100%"
        height={200}
        style={{ marginTop: 12 }}
      />

      {/* Actions row */}
      <div style={{ display: 'flex', gap: 16, marginTop: 12 }}>
        <Skeleton width={60} height={32} variant="rounded" />
        <Skeleton width={60} height={32} variant="rounded" />
        <Skeleton width={60} height={32} variant="rounded" />
      </div>
    </div>
  );
}

// ✅ Smooth transition: Skeleton → Real Content (no jump)
function PostCard({ post }: { post: Post | null }) {
  if (!post) return <PostCardSkeleton />;

  return (
    <div style={{ padding: 16, border: '1px solid #eee', borderRadius: 8 }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
        <img
          src={post.author.avatar}
          width={40}
          height={40}
          style={{ borderRadius: '50%' }}
          alt={post.author.name}
        />
        <div>
          <strong>{post.author.name}</strong>
          <div style={{ fontSize: 12, color: '#666' }}>{post.createdAt}</div>
        </div>
      </div>
      <p style={{ marginTop: 12 }}>{post.content}</p>
      {post.image && (
        <img
          src={post.image}
          width={600}
          height={200}
          style={{ aspectRatio: '3/1', width: '100%', height: 'auto', borderRadius: 8 }}
          alt=""
          loading="lazy"
        />
      )}
    </div>
  );
}

// ✅ ADVANCED: Font Loading Strategy — Chống FOUT/FOIT
/**
 * CSS:
 * @font-face {
 *   font-family: 'CustomFont';
 *   src: url('/fonts/custom.woff2') format('woff2');
 *   font-display: swap;  ← Hiển thị fallback font ngay, swap khi custom font load xong
 *                           (FOUT — Flash of Unstyled Text, tốt hơn FOIT — invisible text)
 * }
 *
 * // Preload critical fonts
 * <link rel="preload" href="/fonts/custom.woff2" as="font" type="font/woff2" crossorigin>
 */

// ✅ ADVANCED: Chống CLS cho dynamic content (ads, banners)
function AdSlot({ width, height }: { width: number; height: number }) {
  const [adLoaded, setAdLoaded] = useState(false);

  return (
    // Container có kích thước CỐ ĐỊNH trước → không shift khi ad load
    <div
      style={{
        width,
        height,
        minHeight: height, // Guarantee minimum height
        backgroundColor: adLoaded ? 'transparent' : '#f5f5f5',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        overflow: 'hidden',
        contain: 'layout size', // CSS Containment — isolate layout calculations
      }}
    >
      {!adLoaded && (
        <span style={{ color: '#999', fontSize: 12 }}>Advertisement</span>
      )}
      <AdComponent onLoad={() => setAdLoaded(true)} />
    </div>
  );
}

// ✅ CSS contain property — Giới hạn phạm vi layout recalculation
/**
 * .card {
 *   contain: layout style paint;  ← Thay đổi bên trong card KHÔNG ảnh hưởng bên ngoài
 *                                    → Performance tốt hơn khi render nhiều cards
 * }
 *
 * .virtual-list-item {
 *   contain: strict;  ← Cô lập hoàn toàn (layout + size + paint + style)
 *                       → Tối ưu cho virtual list
 * }
 */
```

**🧠 Bài học:**
- **Skeleton phải match layout thật** — cùng width, height, spacing → transition smooth, CLS = 0
- **Image**: Luôn set `width`/`height` hoặc `aspect-ratio` → browser reserve space trước khi load
- **Font**: `font-display: swap` + `<link rel="preload">` cho critical fonts
- **Dynamic content**: Container cố định kích thước + `CSS contain` property
- **Đo lường**: Chrome DevTools → Performance → Layout Shift regions, hoặc Web Vitals extension

---

### **25.11. 🔀 Drag & Drop Với Reorder, Nested Lists & Touch Support**

**Vấn đề:** Implement drag & drop cho Kanban board, sortable list, nested categories — phải hoạt động smooth trên cả desktop (mouse) lẫn mobile (touch), xử lý auto-scroll khi drag gần edge, visual feedback, và data persistence.

```typescript
/**
 * 🔴 ĐỘ KHÓ CỦA DRAG & DROP:
 *
 * 1. Mouse events ≠ Touch events (khác API hoàn toàn)
 * 2. Touch: phải phân biệt scroll vs drag (cùng gesture!)
 * 3. Nested sortable: drag item từ list A sang list B
 * 4. Auto-scroll khi drag gần edge viewport
 * 5. Performance: drag 60fps, không jank
 * 6. Accessibility: keyboard navigation cho drag & drop
 */

// ✅ Custom useDragAndDrop hook — Unified mouse + touch
interface DragState<T> {
  isDragging: boolean;
  draggedItem: T | null;
  draggedIndex: number;
  overIndex: number;
  sourceList: string;
  targetList: string;
}

function useSortableList<T extends { id: string }>({
  items,
  onReorder,
  listId,
  direction = 'vertical',
}: {
  items: T[];
  onReorder: (items: T[], sourceListId: string, targetListId?: string) => void;
  listId: string;
  direction?: 'vertical' | 'horizontal';
}) {
  const [dragState, setDragState] = useState<DragState<T>>({
    isDragging: false,
    draggedItem: null,
    draggedIndex: -1,
    overIndex: -1,
    sourceList: '',
    targetList: '',
  });

  const dragNodeRef = useRef<HTMLElement | null>(null);
  const autoScrollRef = useRef<number | null>(null);
  const itemRefs = useRef<Map<number, HTMLElement>>(new Map());

  // ⭐ Unified pointer handler (mouse + touch)
  const handleDragStart = useCallback(
    (index: number) => (e: React.PointerEvent) => {
      // Capture pointer for smooth tracking across elements
      (e.target as HTMLElement).setPointerCapture(e.pointerId);

      dragNodeRef.current = e.currentTarget as HTMLElement;
      setDragState({
        isDragging: true,
        draggedItem: items[index],
        draggedIndex: index,
        overIndex: index,
        sourceList: listId,
        targetList: listId,
      });

      // Visual feedback
      dragNodeRef.current.style.opacity = '0.5';
      dragNodeRef.current.style.transform = 'scale(1.02)';
      document.body.style.cursor = 'grabbing';
      document.body.style.userSelect = 'none'; // Prevent text selection during drag
    },
    [items, listId]
  );

  const handleDragOver = useCallback(
    (index: number) => (e: React.PointerEvent) => {
      e.preventDefault();
      if (!dragState.isDragging) return;

      // Tính toán vị trí drop dựa trên pointer position vs element center
      const element = e.currentTarget as HTMLElement;
      const rect = element.getBoundingClientRect();
      const midPoint =
        direction === 'vertical'
          ? rect.top + rect.height / 2
          : rect.left + rect.width / 2;
      const pointerPos =
        direction === 'vertical' ? e.clientY : e.clientX;

      // Nếu pointer ở nửa trên → insert trước, nửa dưới → insert sau
      const adjustedIndex = pointerPos < midPoint ? index : index + 1;

      if (adjustedIndex !== dragState.overIndex) {
        setDragState((prev) => ({ ...prev, overIndex: adjustedIndex }));
      }

      // ⭐ Auto-scroll khi drag gần edge
      startAutoScroll(e.clientY);
    },
    [dragState.isDragging, dragState.overIndex, direction]
  );

  const handleDrop = useCallback(() => {
    if (!dragState.isDragging || dragState.draggedIndex === dragState.overIndex) {
      resetDragState();
      return;
    }

    // Reorder items
    const newItems = [...items];
    const [removed] = newItems.splice(dragState.draggedIndex, 1);
    const insertIndex =
      dragState.overIndex > dragState.draggedIndex
        ? dragState.overIndex - 1
        : dragState.overIndex;
    newItems.splice(insertIndex, 0, removed);

    onReorder(newItems, listId);
    resetDragState();
  }, [dragState, items, onReorder, listId]);

  // Auto-scroll khi drag gần edge viewport
  const startAutoScroll = useCallback((clientY: number) => {
    const SCROLL_ZONE = 80; // pixels from edge
    const SCROLL_SPEED = 10;

    if (autoScrollRef.current) cancelAnimationFrame(autoScrollRef.current);

    const scroll = () => {
      if (clientY < SCROLL_ZONE) {
        window.scrollBy(0, -SCROLL_SPEED);
        autoScrollRef.current = requestAnimationFrame(scroll);
      } else if (clientY > window.innerHeight - SCROLL_ZONE) {
        window.scrollBy(0, SCROLL_SPEED);
        autoScrollRef.current = requestAnimationFrame(scroll);
      }
    };
    scroll();
  }, []);

  const resetDragState = useCallback(() => {
    if (dragNodeRef.current) {
      dragNodeRef.current.style.opacity = '1';
      dragNodeRef.current.style.transform = '';
    }
    document.body.style.cursor = '';
    document.body.style.userSelect = '';
    if (autoScrollRef.current) cancelAnimationFrame(autoScrollRef.current);

    setDragState({
      isDragging: false,
      draggedItem: null,
      draggedIndex: -1,
      overIndex: -1,
      sourceList: '',
      targetList: '',
    });
  }, []);

  // ✅ Accessibility: Keyboard drag
  const handleKeyDown = useCallback(
    (index: number) => (e: React.KeyboardEvent) => {
      if (e.key === ' ' || e.key === 'Enter') {
        e.preventDefault();
        // Toggle drag mode
        if (!dragState.isDragging) {
          setDragState({
            isDragging: true,
            draggedItem: items[index],
            draggedIndex: index,
            overIndex: index,
            sourceList: listId,
            targetList: listId,
          });
        } else {
          handleDrop();
        }
      } else if (dragState.isDragging) {
        if (e.key === 'ArrowDown' || e.key === 'ArrowRight') {
          e.preventDefault();
          setDragState((prev) => ({
            ...prev,
            overIndex: Math.min(prev.overIndex + 1, items.length - 1),
          }));
        } else if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') {
          e.preventDefault();
          setDragState((prev) => ({
            ...prev,
            overIndex: Math.max(prev.overIndex - 1, 0),
          }));
        } else if (e.key === 'Escape') {
          resetDragState();
        }
      }
    },
    [dragState, items, listId, handleDrop, resetDragState]
  );

  return {
    dragState,
    getItemProps: (index: number) => ({
      onPointerDown: handleDragStart(index),
      onPointerMove: handleDragOver(index),
      onPointerUp: handleDrop,
      onKeyDown: handleKeyDown(index),
      tabIndex: 0,
      role: 'listitem',
      'aria-grabbed': dragState.isDragging && dragState.draggedIndex === index,
      'aria-dropeffect': dragState.isDragging ? 'move' : 'none',
      style: {
        cursor: dragState.isDragging ? 'grabbing' : 'grab',
        transition: 'transform 200ms ease',
        transform:
          dragState.isDragging && dragState.overIndex === index
            ? `translateY(${direction === 'vertical' ? '40px' : '0'})`
            : '',
      },
    }),
  };
}

// Sử dụng:
function KanbanColumn({ columnId, tasks, onReorder }) {
  const { dragState, getItemProps } = useSortableList({
    items: tasks,
    onReorder,
    listId: columnId,
  });

  return (
    <div className="kanban-column" role="list" aria-label={`Column ${columnId}`}>
      {tasks.map((task, index) => (
        <div
          key={task.id}
          {...getItemProps(index)}
          className={`task-card ${
            dragState.isDragging && dragState.draggedIndex === index
              ? 'dragging'
              : ''
          }`}
        >
          {task.title}
        </div>
      ))}
    </div>
  );
}
```

**🧠 Bài học:**
- **Pointer Events** API unify mouse + touch + pen — dùng thay vì viết riêng mouse/touch handlers
- **setPointerCapture** giữ tracking pointer ngay cả khi di chuột ra ngoài element
- **Auto-scroll** gần edge viewport là detail nhỏ nhưng UX impact rất lớn
- Production: Dùng `@dnd-kit/core` hoặc `react-beautiful-dnd` — đã handle edge cases + a11y

---

### **25.12. 🌊 Infinite Scroll Với Bidirectional Loading & Scroll Restoration**

**Vấn đề:** Chat app/feed cần scroll vô hạn cả 2 chiều (load tin cũ phía trên + tin mới phía dưới) → prepend items phía trên gây "scroll jump", quay lại trang phải restore đúng vị trí scroll cũ.

```typescript
/**
 * 🔴 CÁC VẤN ĐỀ:
 * 1. Prepend items phía trên → scrollTop bị đẩy → content nhảy
 * 2. User quay lại (Back button) → mất vị trí scroll → phải load lại từ đầu
 * 3. Append + Prepend cùng lúc → race condition
 * 4. Memory: load 10K items → browser lag
 */

// ✅ Bidirectional Infinite Scroll với Scroll Anchoring
function useBidirectionalScroll<T extends { id: string }>({
  fetchOlder,     // Load items cũ hơn (prepend)
  fetchNewer,     // Load items mới hơn (append)
  pageSize = 20,
  maxItems = 500, // Giới hạn items trong DOM (memory management)
}: {
  fetchOlder: (beforeId: string) => Promise<T[]>;
  fetchNewer: (afterId: string) => Promise<T[]>;
  pageSize?: number;
  maxItems?: number;
}) {
  const [items, setItems] = useState<T[]>([]);
  const [loadingOlder, setLoadingOlder] = useState(false);
  const [loadingNewer, setLoadingNewer] = useState(false);
  const [hasOlder, setHasOlder] = useState(true);
  const [hasNewer, setHasNewer] = useState(true);

  const containerRef = useRef<HTMLDivElement>(null);
  const topSentinelRef = useRef<HTMLDivElement>(null);
  const bottomSentinelRef = useRef<HTMLDivElement>(null);

  // ⭐ KEY: Preserve scroll position khi prepend
  const loadOlderItems = useCallback(async () => {
    if (loadingOlder || !hasOlder || items.length === 0) return;
    setLoadingOlder(true);

    const container = containerRef.current!;
    const oldScrollHeight = container.scrollHeight;
    const oldScrollTop = container.scrollTop;

    try {
      const olderItems = await fetchOlder(items[0].id);

      if (olderItems.length < pageSize) setHasOlder(false);
      if (olderItems.length === 0) {
        setLoadingOlder(false);
        return;
      }

      setItems((prev) => {
        const merged = [...olderItems, ...prev];
        // Trim từ dưới nếu vượt maxItems (memory management)
        if (merged.length > maxItems) {
          setHasNewer(true); // Items bị trim → có thể load lại
          return merged.slice(0, maxItems);
        }
        return merged;
      });

      // ⭐ Restore scroll position sau prepend
      // requestAnimationFrame đợi DOM update xong
      requestAnimationFrame(() => {
        const newScrollHeight = container.scrollHeight;
        const heightDifference = newScrollHeight - oldScrollHeight;
        container.scrollTop = oldScrollTop + heightDifference;
      });
    } catch (error) {
      console.error('Failed to load older items:', error);
    } finally {
      setLoadingOlder(false);
    }
  }, [loadingOlder, hasOlder, items, fetchOlder, pageSize, maxItems]);

  // Load newer items (append — đơn giản hơn, không cần scroll fix)
  const loadNewerItems = useCallback(async () => {
    if (loadingNewer || !hasNewer || items.length === 0) return;
    setLoadingNewer(true);

    try {
      const newerItems = await fetchNewer(items[items.length - 1].id);

      if (newerItems.length < pageSize) setHasNewer(false);

      setItems((prev) => {
        const merged = [...prev, ...newerItems];
        // Trim từ trên nếu vượt maxItems
        if (merged.length > maxItems) {
          setHasOlder(true);
          return merged.slice(-maxItems);
        }
        return merged;
      });
    } catch (error) {
      console.error('Failed to load newer items:', error);
    } finally {
      setLoadingNewer(false);
    }
  }, [loadingNewer, hasNewer, items, fetchNewer, pageSize, maxItems]);

  // IntersectionObserver: Auto-trigger load khi sentinel vào viewport
  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          if (entry.target === topSentinelRef.current) loadOlderItems();
          if (entry.target === bottomSentinelRef.current) loadNewerItems();
        });
      },
      { root: containerRef.current, rootMargin: '200px', threshold: 0 }
    );

    if (topSentinelRef.current) observer.observe(topSentinelRef.current);
    if (bottomSentinelRef.current) observer.observe(bottomSentinelRef.current);

    return () => observer.disconnect();
  }, [loadOlderItems, loadNewerItems]);

  return {
    items,
    containerRef,
    topSentinelRef,
    bottomSentinelRef,
    loadingOlder,
    loadingNewer,
    hasOlder,
    hasNewer,
  };
}

// ✅ Scroll Restoration khi navigate back
function useScrollRestoration(key: string) {
  const scrollPositions = useRef<Map<string, number>>(new Map());

  useEffect(() => {
    // Restore scroll position khi mount
    const savedPosition = sessionStorage.getItem(`scroll_${key}`);
    if (savedPosition) {
      requestAnimationFrame(() => {
        window.scrollTo(0, parseInt(savedPosition, 10));
      });
    }

    // Save scroll position khi unmount hoặc navigate
    const savePosition = () => {
      sessionStorage.setItem(`scroll_${key}`, String(window.scrollY));
    };

    window.addEventListener('beforeunload', savePosition);
    return () => {
      savePosition(); // Save khi unmount (navigate away)
      window.removeEventListener('beforeunload', savePosition);
    };
  }, [key]);
}

// Sử dụng:
function ChatRoom({ roomId }) {
  const {
    items: messages,
    containerRef,
    topSentinelRef,
    bottomSentinelRef,
    loadingOlder,
    loadingNewer,
  } = useBidirectionalScroll({
    fetchOlder: (beforeId) => api.getMessages(roomId, { before: beforeId }),
    fetchNewer: (afterId) => api.getMessages(roomId, { after: afterId }),
    maxItems: 200,
  });

  useScrollRestoration(`chat-${roomId}`);

  return (
    <div ref={containerRef} style={{ height: '100vh', overflowY: 'auto' }}>
      {/* Top sentinel → triggers load older */}
      <div ref={topSentinelRef}>
        {loadingOlder && <Spinner />}
      </div>

      {messages.map((msg) => (
        <MessageBubble key={msg.id} message={msg} />
      ))}

      {/* Bottom sentinel → triggers load newer */}
      <div ref={bottomSentinelRef}>
        {loadingNewer && <Spinner />}
      </div>
    </div>
  );
}
```

**🧠 Bài học:**
- **Prepend scroll fix**: Đo `scrollHeight` trước và sau prepend → adjust `scrollTop` bằng delta
- **Memory management**: Giới hạn max items trong DOM, trim từ đầu/cuối khi vượt limit
- **IntersectionObserver** > scroll event listener: performance tốt hơn, không cần debounce
- **Scroll restoration**: `sessionStorage` + `beforeunload` cho SPA navigation

---

### **25.13. 🧩 Micro-Frontend Communication — Independently Deployed Apps Talking**

**Vấn đề:** Nhiều team build các micro-frontend apps riêng biệt, deploy độc lập → cần communicate giữa các apps mà không tạo tight coupling, share state mà không share code.

```typescript
/**
 * 🔴 THÁCH THỨC:
 * 1. App A (React 18) cần data từ App B (Vue 3) → khác framework!
 * 2. Shared state (user info) phải sync across apps
 * 3. Routing: navigate từ app A sang app B seamlessly
 * 4. CSS isolation: styles không leak giữa các apps
 * 5. Versioning: App A deploy v2 nhưng App B vẫn ở v1
 */

// ✅ Event Bus Pattern — Framework-agnostic communication
class MicroFrontendBus {
  private static instance: MicroFrontendBus;
  private events = new Map<string, Set<Function>>();
  private stateStore = new Map<string, any>();
  private stateListeners = new Map<string, Set<(value: any) => void>>();

  static getInstance(): MicroFrontendBus {
    if (!MicroFrontendBus.instance) {
      MicroFrontendBus.instance = new MicroFrontendBus();
      // Expose globally for different framework apps
      (window as any).__MFE_BUS__ = MicroFrontendBus.instance;
    }
    return MicroFrontendBus.instance;
  }

  // ── Event-based communication ──
  emit(event: string, payload?: any) {
    // Local listeners
    this.events.get(event)?.forEach((fn) => fn(payload));

    // Custom DOM Event (cho apps trong iframe hoặc Shadow DOM)
    window.dispatchEvent(
      new CustomEvent(`mfe:${event}`, {
        detail: payload,
        bubbles: true,
        composed: true, // Cross Shadow DOM boundary
      })
    );
  }

  on(event: string, callback: Function): () => void {
    if (!this.events.has(event)) this.events.set(event, new Set());
    this.events.get(event)!.add(callback);

    // Also listen for DOM custom events (from iframes/Shadow DOM)
    const domHandler = (e: Event) => callback((e as CustomEvent).detail);
    window.addEventListener(`mfe:${event}`, domHandler);

    return () => {
      this.events.get(event)?.delete(callback);
      window.removeEventListener(`mfe:${event}`, domHandler);
    };
  }

  // ── Shared State (Observable) ──
  setState(key: string, value: any) {
    const oldValue = this.stateStore.get(key);
    this.stateStore.set(key, value);

    // Notify only if value actually changed
    if (!Object.is(oldValue, value)) {
      this.stateListeners.get(key)?.forEach((fn) => fn(value));
    }
  }

  getState<T>(key: string): T | undefined {
    return this.stateStore.get(key);
  }

  subscribe(key: string, callback: (value: any) => void): () => void {
    if (!this.stateListeners.has(key)) {
      this.stateListeners.set(key, new Set());
    }
    this.stateListeners.get(key)!.add(callback);

    // Emit current value immediately (like BehaviorSubject)
    if (this.stateStore.has(key)) {
      callback(this.stateStore.get(key));
    }

    return () => this.stateListeners.get(key)?.delete(callback);
  }
}

// ✅ React Hook wrapper
function useMFEState<T>(key: string, initialValue?: T): [T, (value: T) => void] {
  const bus = MicroFrontendBus.getInstance();
  const [value, setValue] = useState<T>(
    () => bus.getState<T>(key) ?? initialValue!
  );

  useEffect(() => {
    return bus.subscribe(key, setValue);
  }, [key]);

  const updateValue = useCallback(
    (newValue: T) => {
      bus.setState(key, newValue);
    },
    [key]
  );

  return [value, updateValue];
}

function useMFEEvent(event: string, handler: (payload: any) => void) {
  useEffect(() => {
    const bus = MicroFrontendBus.getInstance();
    return bus.on(event, handler);
  }, [event, handler]);
}

// ✅ SỬ DỤNG: App A (Header — React) share user data
function HeaderApp() {
  const [user, setUser] = useMFEState<User | null>('currentUser', null);

  const handleLogin = async () => {
    const user = await authService.login();
    setUser(user); // All micro-frontends sẽ nhận được user data

    // Emit event cho apps cần biết
    MicroFrontendBus.getInstance().emit('user:login', user);
  };

  const handleLogout = () => {
    setUser(null);
    MicroFrontendBus.getInstance().emit('user:logout');
  };

  return <header>{user ? `Hi ${user.name}` : <LoginButton onClick={handleLogin} />}</header>;
}

// ✅ SỬ DỤNG: App B (Dashboard — Vue hoặc bất kỳ framework nào)
// Trong Vue:
// const bus = window.__MFE_BUS__;
// const user = ref(bus.getState('currentUser'));
// bus.subscribe('currentUser', (newUser) => { user.value = newUser; });

// ✅ CSS Isolation với Shadow DOM
class MicroFrontendContainer extends HTMLElement {
  connectedCallback() {
    // Shadow DOM isolate CSS hoàn toàn
    const shadow = this.attachShadow({ mode: 'open' });

    // Load app CSS vào Shadow DOM (không leak ra ngoài)
    const style = document.createElement('link');
    style.rel = 'stylesheet';
    style.href = '/apps/dashboard/styles.css';
    shadow.appendChild(style);

    // Mount React app vào Shadow DOM
    const mountPoint = document.createElement('div');
    shadow.appendChild(mountPoint);

    import('/apps/dashboard/main.js').then((module) => {
      module.mount(mountPoint);
    });
  }

  disconnectedCallback() {
    // Cleanup khi element bị remove
    import('/apps/dashboard/main.js').then((module) => {
      module.unmount();
    });
  }
}

customElements.define('mfe-dashboard', MicroFrontendContainer);
```

**🧠 Bài học:**
- **Event Bus** là pattern đơn giản nhất cho micro-frontend communication
- **Shared Observable State** (subset of Redux) cho data cần sync realtime
- **Custom Elements + Shadow DOM** cho CSS isolation hoàn hảo
- **Module Federation** (Webpack 5) hoặc **Import Maps** cho code sharing ở build level

---

### **25.14. 🔐 Token Refresh Queue — Xử Lý 401 Khi Nhiều Request Cùng Lúc**

**Vấn đề:** Access token hết hạn → nhiều API requests cùng nhận 401 → tất cả đều trigger refresh token → gửi N refresh requests → server reject duplicate refresh → user bị force logout.

```typescript
/**
 * 🔴 THỰC TẾ:
 *
 * Trang dashboard gọi 5 API cùng lúc:
 * GET /user       → 401 → refresh token → ✅
 * GET /posts      → 401 → refresh token → ❌ (token đã dùng rồi!)
 * GET /comments   → 401 → refresh token → ❌
 * GET /stats      → 401 → refresh token → ❌
 * GET /notif      → 401 → refresh token → ❌
 *
 * → 4/5 requests fail! User bị logout!
 */

// ✅ ĐÚNG: Token Refresh Queue — Chỉ 1 refresh, tất cả chờ
class AuthInterceptor {
  private isRefreshing = false;
  private failedQueue: Array<{
    resolve: (token: string) => void;
    reject: (error: Error) => void;
  }> = [];

  constructor(private httpClient: typeof fetch) {}

  // Process tất cả queued requests sau khi refresh xong
  private processQueue(error: Error | null, token: string | null) {
    this.failedQueue.forEach(({ resolve, reject }) => {
      if (error) {
        reject(error);
      } else {
        resolve(token!);
      }
    });
    this.failedQueue = [];
  }

  async request(url: string, options: RequestInit = {}): Promise<Response> {
    // Attach current access token
    const accessToken = this.getAccessToken();
    const headers = new Headers(options.headers);
    if (accessToken) {
      headers.set('Authorization', `Bearer ${accessToken}`);
    }

    const response = await this.httpClient(url, { ...options, headers });

    // Nếu KHÔNG phải 401 → return bình thường
    if (response.status !== 401) return response;

    // ── 401 Handling ──

    // Nếu ĐANG refresh → queue request này, chờ refresh xong
    if (this.isRefreshing) {
      return new Promise<Response>((resolve, reject) => {
        this.failedQueue.push({
          resolve: (newToken: string) => {
            // Retry request với token mới
            headers.set('Authorization', `Bearer ${newToken}`);
            resolve(this.httpClient(url, { ...options, headers }));
          },
          reject,
        });
      });
    }

    // ⭐ Request ĐẦU TIÊN bị 401 → bắt đầu refresh
    this.isRefreshing = true;

    try {
      const refreshToken = this.getRefreshToken();
      if (!refreshToken) throw new Error('No refresh token');

      const refreshResponse = await this.httpClient('/api/auth/refresh', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ refreshToken }),
      });

      if (!refreshResponse.ok) {
        throw new Error('Refresh token expired');
      }

      const { accessToken: newToken, refreshToken: newRefreshToken } =
        await refreshResponse.json();

      // Lưu tokens mới
      this.setAccessToken(newToken);
      this.setRefreshToken(newRefreshToken);

      // ⭐ Process tất cả queued requests với token mới
      this.processQueue(null, newToken);

      // Retry request gốc
      headers.set('Authorization', `Bearer ${newToken}`);
      return this.httpClient(url, { ...options, headers });
    } catch (error) {
      // Refresh failed → reject TẤT CẢ queued requests
      this.processQueue(error as Error, null);

      // Force logout
      this.clearTokens();
      window.location.href = '/login';

      throw error;
    } finally {
      this.isRefreshing = false;
    }
  }

  private getAccessToken(): string | null {
    return localStorage.getItem('access_token');
  }
  private getRefreshToken(): string | null {
    return localStorage.getItem('refresh_token');
  }
  private setAccessToken(token: string) {
    localStorage.setItem('access_token', token);
  }
  private setRefreshToken(token: string) {
    localStorage.setItem('refresh_token', token);
  }
  private clearTokens() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
  }
}

// ✅ Axios Interceptor version (phổ biến trong production)
import axios from 'axios';

let isRefreshing = false;
let failedQueue: Array<{ resolve: Function; reject: Function }> = [];

function processQueue(error: any, token: string | null) {
  failedQueue.forEach(({ resolve, reject }) => {
    error ? reject(error) : resolve(token);
  });
  failedQueue = [];
}

axios.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    if (error.response?.status !== 401 || originalRequest._retry) {
      return Promise.reject(error);
    }

    if (isRefreshing) {
      // Queue request → chờ refresh xong
      return new Promise((resolve, reject) => {
        failedQueue.push({
          resolve: (token: string) => {
            originalRequest.headers.Authorization = `Bearer ${token}`;
            resolve(axios(originalRequest));
          },
          reject,
        });
      });
    }

    originalRequest._retry = true;
    isRefreshing = true;

    try {
      const { data } = await axios.post('/api/auth/refresh', {
        refreshToken: localStorage.getItem('refresh_token'),
      });

      localStorage.setItem('access_token', data.accessToken);
      localStorage.setItem('refresh_token', data.refreshToken);

      axios.defaults.headers.common.Authorization = `Bearer ${data.accessToken}`;
      processQueue(null, data.accessToken);

      originalRequest.headers.Authorization = `Bearer ${data.accessToken}`;
      return axios(originalRequest);
    } catch (err) {
      processQueue(err, null);
      localStorage.clear();
      window.location.href = '/login';
      return Promise.reject(err);
    } finally {
      isRefreshing = false;
    }
  }
);
```

**🧠 Bài học:**
- **Singleton refresh**: Chỉ 1 refresh request tại một thời điểm, tất cả 401 khác queue lại
- **Queue pattern**: Failed requests chờ trong Promise queue → resolve khi có token mới
- **Retry original**: Sau refresh thành công, tự động retry request gốc với token mới
- **Cross-tab sync** refresh token (kết hợp Case 7) để tránh nhiều tab refresh cùng lúc

---

### **25.15. 📸 Image Upload Với Preview, Compression, Crop & Progress**

**Vấn đề:** Upload ảnh cần: preview ngay (trước khi upload), resize/compress client-side (giảm bandwidth), crop interactively, show progress %, handle retry, validate file type/size.

```typescript
/**
 * 🔴 THỰC TẾ:
 * - User chọn ảnh 15MB từ iPhone → upload chậm, tốn bandwidth
 * - Server limit 5MB → phải compress client-side
 * - Cần preview ngay khi chọn (không chờ upload)
 * - Multiple files → parallel upload với individual progress
 */

// ✅ Image compression + preview hook
function useImageUpload({
  maxSizeMB = 5,
  maxWidthOrHeight = 1920,
  quality = 0.8,
  allowedTypes = ['image/jpeg', 'image/png', 'image/webp'],
}: {
  maxSizeMB?: number;
  maxWidthOrHeight?: number;
  quality?: number;
  allowedTypes?: string[];
} = {}) {
  const [files, setFiles] = useState<UploadFile[]>([]);

  interface UploadFile {
    id: string;
    file: File;
    preview: string;       // Object URL cho preview
    compressed: Blob | null;
    progress: number;       // 0-100
    status: 'pending' | 'compressing' | 'uploading' | 'success' | 'error';
    error: string | null;
  }

  // Validate file
  const validateFile = useCallback(
    (file: File): string | null => {
      if (!allowedTypes.includes(file.type)) {
        return `Chỉ chấp nhận: ${allowedTypes.join(', ')}`;
      }
      if (file.size > maxSizeMB * 1024 * 1024 * 3) {
        // Allow 3x before compression
        return `File quá lớn (max ${maxSizeMB * 3}MB trước khi nén)`;
      }
      return null;
    },
    [allowedTypes, maxSizeMB]
  );

  // ⭐ Compress image client-side using Canvas API
  const compressImage = useCallback(
    async (file: File): Promise<Blob> => {
      return new Promise((resolve, reject) => {
        const img = new Image();
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d')!;

        img.onload = () => {
          // Calculate new dimensions (maintain aspect ratio)
          let { width, height } = img;
          if (width > maxWidthOrHeight || height > maxWidthOrHeight) {
            const ratio = Math.min(
              maxWidthOrHeight / width,
              maxWidthOrHeight / height
            );
            width *= ratio;
            height *= ratio;
          }

          canvas.width = width;
          canvas.height = height;

          // Draw và compress
          ctx.drawImage(img, 0, 0, width, height);
          canvas.toBlob(
            (blob) => {
              if (blob) {
                console.log(
                  `📦 Compressed: ${(file.size / 1024 / 1024).toFixed(1)}MB → ${(blob.size / 1024 / 1024).toFixed(1)}MB`
                );
                resolve(blob);
              } else {
                reject(new Error('Compression failed'));
              }
            },
            'image/jpeg', // Output format
            quality       // Quality: 0.8 = 80%
          );

          // Cleanup
          URL.revokeObjectURL(img.src);
        };

        img.onerror = () => reject(new Error('Invalid image'));
        img.src = URL.createObjectURL(file);
      });
    },
    [maxWidthOrHeight, quality]
  );

  // ⭐ Upload with progress tracking
  const uploadFile = useCallback(
    async (uploadFile: UploadFile): Promise<string> => {
      return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        const formData = new FormData();
        formData.append(
          'file',
          uploadFile.compressed || uploadFile.file,
          uploadFile.file.name
        );

        // Track upload progress
        xhr.upload.onprogress = (event) => {
          if (event.lengthComputable) {
            const progress = Math.round((event.loaded / event.total) * 100);
            setFiles((prev) =>
              prev.map((f) =>
                f.id === uploadFile.id ? { ...f, progress } : f
              )
            );
          }
        };

        xhr.onload = () => {
          if (xhr.status >= 200 && xhr.status < 300) {
            const { url } = JSON.parse(xhr.responseText);
            resolve(url);
          } else {
            reject(new Error(`Upload failed: ${xhr.status}`));
          }
        };

        xhr.onerror = () => reject(new Error('Network error'));

        xhr.open('POST', '/api/upload');
        xhr.setRequestHeader('Authorization', `Bearer ${getToken()}`);
        xhr.send(formData);
      });
    },
    []
  );

  // Main handler: select → validate → preview → compress → upload
  const handleFiles = useCallback(
    async (fileList: FileList) => {
      const newFiles: UploadFile[] = Array.from(fileList).map((file) => ({
        id: crypto.randomUUID(),
        file,
        preview: URL.createObjectURL(file), // Preview NGAY (0ms!)
        compressed: null,
        progress: 0,
        status: 'pending' as const,
        error: validateFile(file),
      }));

      setFiles((prev) => [...prev, ...newFiles]);

      // Process each file: compress → upload (parallel)
      await Promise.allSettled(
        newFiles
          .filter((f) => !f.error)
          .map(async (f) => {
            try {
              // Compress
              updateStatus(f.id, 'compressing');
              const compressed = await compressImage(f.file);
              setFiles((prev) =>
                prev.map((pf) =>
                  pf.id === f.id ? { ...pf, compressed } : pf
                )
              );

              // Upload
              updateStatus(f.id, 'uploading');
              await uploadFile({ ...f, compressed });
              updateStatus(f.id, 'success');
            } catch (err) {
              updateStatus(f.id, 'error', (err as Error).message);
            }
          })
      );
    },
    [validateFile, compressImage, uploadFile]
  );

  const updateStatus = (id: string, status: UploadFile['status'], error?: string) => {
    setFiles((prev) =>
      prev.map((f) => (f.id === id ? { ...f, status, error: error ?? null } : f))
    );
  };

  // Retry failed upload
  const retry = useCallback(
    (id: string) => {
      const file = files.find((f) => f.id === id);
      if (file) {
        updateStatus(id, 'uploading');
        uploadFile(file)
          .then(() => updateStatus(id, 'success'))
          .catch((err) => updateStatus(id, 'error', err.message));
      }
    },
    [files, uploadFile]
  );

  // Cleanup preview URLs on unmount
  useEffect(() => {
    return () => files.forEach((f) => URL.revokeObjectURL(f.preview));
  }, []); // eslint-disable-line

  const removeFile = (id: string) => {
    setFiles((prev) => {
      const file = prev.find((f) => f.id === id);
      if (file) URL.revokeObjectURL(file.preview);
      return prev.filter((f) => f.id !== id);
    });
  };

  return { files, handleFiles, retry, removeFile };
}

// Sử dụng:
function AvatarUpload() {
  const { files, handleFiles, retry, removeFile } = useImageUpload({
    maxSizeMB: 2,
    maxWidthOrHeight: 800,
    quality: 0.85,
  });

  return (
    <div>
      <input
        type="file"
        accept="image/*"
        multiple
        onChange={(e) => e.target.files && handleFiles(e.target.files)}
      />

      {files.map((f) => (
        <div key={f.id} style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <img src={f.preview} width={60} height={60} style={{ objectFit: 'cover' }} />
          <div style={{ flex: 1 }}>
            <div>{f.file.name}</div>
            {f.status === 'compressing' && <div>🔧 Đang nén...</div>}
            {f.status === 'uploading' && (
              <progress value={f.progress} max={100} style={{ width: '100%' }} />
            )}
            {f.status === 'success' && <div>✅ Hoàn tất</div>}
            {f.status === 'error' && (
              <div>
                ❌ {f.error} <button onClick={() => retry(f.id)}>Retry</button>
              </div>
            )}
          </div>
          <button onClick={() => removeFile(f.id)}>✕</button>
        </div>
      ))}
    </div>
  );
}
```

**🧠 Bài học:**
- **`URL.createObjectURL()`** cho preview NGAY (0ms) mà không cần upload trước
- **Canvas API** compress ảnh client-side: 15MB → 1MB, giảm 90% bandwidth
- **XMLHttpRequest** (`xhr.upload.onprogress`) cho progress tracking (fetch API chưa hỗ trợ upload progress)
- **Cleanup**: Luôn `URL.revokeObjectURL()` khi không cần preview nữa (tránh memory leak)

---

### **25.16. ⌨️ Undo/Redo System Với Command Pattern**

**Vấn đề:** Rich editor, design tool, form builder cần undo/redo → phải track mọi thay đổi, support batch undo (gộp nhiều thay đổi vào 1 undo step), handle branching (undo rồi thay đổi mới → redo history bị xóa).

```typescript
/**
 * 🔴 ĐỘ KHÓ:
 * - Mỗi action cần biết cách "undo" chính nó
 * - Batch actions: drag + drop = 1 undo step (không phải 2)
 * - Branching: undo 3 bước → thay đổi mới → redo stack bị clear
 * - Memory: không lưu vô hạn snapshots → limit history size
 */

// ✅ Command Pattern: Mỗi action là 1 object biết cách do/undo
interface Command {
  id: string;
  description: string;
  execute: () => void;   // Do the action
  undo: () => void;      // Reverse the action
  timestamp: number;
}

class UndoRedoManager {
  private undoStack: Command[] = [];
  private redoStack: Command[] = [];
  private maxHistory: number;
  private batchCommands: Command[] | null = null; // Cho batch mode
  private listeners = new Set<() => void>();

  constructor(maxHistory = 100) {
    this.maxHistory = maxHistory;
  }

  // Execute command và push vào undo stack
  execute(command: Command) {
    command.execute();

    if (this.batchCommands) {
      // Batch mode: gom commands
      this.batchCommands.push(command);
    } else {
      this.undoStack.push(command);
      this.redoStack = []; // ⭐ Clear redo khi có action mới (branching)

      // Trim history nếu vượt limit
      if (this.undoStack.length > this.maxHistory) {
        this.undoStack.shift();
      }
    }

    this.notify();
  }

  // ⭐ Batch: Gom nhiều commands thành 1 undo step
  startBatch(description: string) {
    this.batchCommands = [];
  }

  endBatch(description: string) {
    if (!this.batchCommands || this.batchCommands.length === 0) {
      this.batchCommands = null;
      return;
    }

    const commands = [...this.batchCommands];
    this.batchCommands = null;

    // Tạo 1 composite command từ nhiều commands
    const batchCommand: Command = {
      id: crypto.randomUUID(),
      description,
      execute: () => commands.forEach((cmd) => cmd.execute()),
      undo: () => [...commands].reverse().forEach((cmd) => cmd.undo()), // Undo theo thứ tự ngược
      timestamp: Date.now(),
    };

    this.undoStack.push(batchCommand);
    this.redoStack = [];
    this.notify();
  }

  undo(): boolean {
    const command = this.undoStack.pop();
    if (!command) return false;

    command.undo();
    this.redoStack.push(command);
    this.notify();
    return true;
  }

  redo(): boolean {
    const command = this.redoStack.pop();
    if (!command) return false;

    command.execute();
    this.undoStack.push(command);
    this.notify();
    return true;
  }

  get canUndo() {
    return this.undoStack.length > 0;
  }
  get canRedo() {
    return this.redoStack.length > 0;
  }
  get history() {
    return this.undoStack.map((cmd) => ({
      id: cmd.id,
      description: cmd.description,
      timestamp: cmd.timestamp,
    }));
  }

  subscribe(listener: () => void): () => void {
    this.listeners.add(listener);
    return () => this.listeners.delete(listener);
  }

  private notify() {
    this.listeners.forEach((fn) => fn());
  }

  clear() {
    this.undoStack = [];
    this.redoStack = [];
    this.notify();
  }
}

// ✅ React Hook
function useUndoRedo() {
  const managerRef = useRef(new UndoRedoManager(50));
  const [, forceUpdate] = useState({});

  useEffect(() => {
    return managerRef.current.subscribe(() => forceUpdate({}));
  }, []);

  // Keyboard shortcuts
  useEffect(() => {
    const handler = (e: KeyboardEvent) => {
      const isMac = navigator.platform.includes('Mac');
      const modifier = isMac ? e.metaKey : e.ctrlKey;

      if (modifier && e.key === 'z' && !e.shiftKey) {
        e.preventDefault();
        managerRef.current.undo();
      } else if (
        (modifier && e.key === 'z' && e.shiftKey) || // Cmd+Shift+Z (Mac)
        (modifier && e.key === 'y')                   // Ctrl+Y (Windows)
      ) {
        e.preventDefault();
        managerRef.current.redo();
      }
    };

    window.addEventListener('keydown', handler);
    return () => window.removeEventListener('keydown', handler);
  }, []);

  return managerRef.current;
}

// ✅ SỬ DỤNG: Canvas drawing app
function DrawingApp() {
  const undoRedo = useUndoRedo();
  const [shapes, setShapes] = useState<Shape[]>([]);

  const addShape = (shape: Shape) => {
    undoRedo.execute({
      id: crypto.randomUUID(),
      description: `Add ${shape.type}`,
      execute: () => setShapes((prev) => [...prev, shape]),
      undo: () => setShapes((prev) => prev.filter((s) => s.id !== shape.id)),
      timestamp: Date.now(),
    });
  };

  const moveShape = (shapeId: string, from: Point, to: Point) => {
    undoRedo.execute({
      id: crypto.randomUUID(),
      description: `Move shape`,
      execute: () =>
        setShapes((prev) =>
          prev.map((s) => (s.id === shapeId ? { ...s, x: to.x, y: to.y } : s))
        ),
      undo: () =>
        setShapes((prev) =>
          prev.map((s) => (s.id === shapeId ? { ...s, x: from.x, y: from.y } : s))
        ),
      timestamp: Date.now(),
    });
  };

  // Batch example: Align tất cả shapes (1 undo step)
  const alignAllLeft = () => {
    undoRedo.startBatch('Align all left');
    shapes.forEach((shape) => {
      const oldX = shape.x;
      undoRedo.execute({
        id: crypto.randomUUID(),
        description: `Align ${shape.id}`,
        execute: () =>
          setShapes((prev) =>
            prev.map((s) => (s.id === shape.id ? { ...s, x: 0 } : s))
          ),
        undo: () =>
          setShapes((prev) =>
            prev.map((s) => (s.id === shape.id ? { ...s, x: oldX } : s))
          ),
        timestamp: Date.now(),
      });
    });
    undoRedo.endBatch('Align all shapes left');
  };

  return (
    <div>
      <div>
        <button disabled={!undoRedo.canUndo} onClick={() => undoRedo.undo()}>
          ↩️ Undo
        </button>
        <button disabled={!undoRedo.canRedo} onClick={() => undoRedo.redo()}>
          ↪️ Redo
        </button>
      </div>
      <Canvas shapes={shapes} />
    </div>
  );
}
```

**🧠 Bài học:**
- **Command Pattern** = mỗi action là object có `execute()` và `undo()` → flexible, extensible
- **Batch commands** gộp nhiều thay đổi thành 1 undo step (undo ngược thứ tự)
- **Branching**: Khi user undo rồi thay đổi mới → redo stack PHẢI bị clear
- **Keyboard shortcut**: Cmd+Z / Ctrl+Z cho undo, Cmd+Shift+Z / Ctrl+Y cho redo

---

### **25.17. 🌐 Offline-First App Với Service Worker & IndexedDB**

**Vấn đề:** App cần hoạt động khi mất mạng (offline-first) → cache assets + API responses, queue mutations offline, sync khi có mạng trở lại, handle conflict resolution.

```typescript
/**
 * 🔴 OFFLINE CHALLENGES:
 * 1. Cache trang nào? Bao lâu? Khi nào invalidate?
 * 2. User thay đổi data offline → sync lên server khi online → conflict!
 * 3. Network chập chờn (3G/tunnel) → request timeout, retry
 * 4. Background sync khi app đóng
 */

// ✅ Service Worker: Cache Strategy
// service-worker.js
const CACHE_NAME = 'app-v1';
const STATIC_ASSETS = ['/', '/index.html', '/main.js', '/styles.css'];

// Install: Pre-cache static assets
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(STATIC_ASSETS))
  );
  self.skipWaiting(); // Activate immediately
});

// Activate: Clean old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys
          .filter((key) => key !== CACHE_NAME)
          .map((key) => caches.delete(key))
      )
    )
  );
  self.clients.claim(); // Take control immediately
});

// Fetch: Strategy per request type
self.addEventListener('fetch', (event) => {
  const { request } = event;
  const url = new URL(request.url);

  if (request.method !== 'GET') {
    // Non-GET → network only (mutations go through sync queue)
    return;
  }

  if (STATIC_ASSETS.includes(url.pathname)) {
    // Static assets: Cache First (fast, use cached version)
    event.respondWith(cacheFirst(request));
  } else if (url.pathname.startsWith('/api/')) {
    // API calls: Network First (fresh data, fallback to cache)
    event.respondWith(networkFirst(request));
  } else {
    // Other: Stale While Revalidate (show cached, update in background)
    event.respondWith(staleWhileRevalidate(request));
  }
});

async function cacheFirst(request) {
  const cached = await caches.match(request);
  return cached || fetch(request).then((response) => {
    const clone = response.clone();
    caches.open(CACHE_NAME).then((cache) => cache.put(request, clone));
    return response;
  });
}

async function networkFirst(request) {
  try {
    const response = await fetch(request);
    const clone = response.clone();
    caches.open(CACHE_NAME).then((cache) => cache.put(request, clone));
    return response;
  } catch {
    const cached = await caches.match(request);
    return cached || new Response(JSON.stringify({ error: 'Offline' }), {
      status: 503,
      headers: { 'Content-Type': 'application/json' },
    });
  }
}

async function staleWhileRevalidate(request) {
  const cached = await caches.match(request);
  const networkPromise = fetch(request).then((response) => {
    caches.open(CACHE_NAME).then((cache) => cache.put(request, response.clone()));
    return response;
  });
  return cached || networkPromise;
}

// ✅ IndexedDB: Offline Mutation Queue
class OfflineSyncQueue {
  private dbName = 'offline-sync';
  private storeName = 'mutations';

  private async getDB(): Promise<IDBDatabase> {
    return new Promise((resolve, reject) => {
      const request = indexedDB.open(this.dbName, 1);
      request.onupgradeneeded = () => {
        const db = request.result;
        if (!db.objectStoreNames.contains(this.storeName)) {
          db.createObjectStore(this.storeName, { keyPath: 'id', autoIncrement: true });
        }
      };
      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error);
    });
  }

  // Queue một mutation khi offline
  async enqueue(mutation: {
    url: string;
    method: string;
    body: any;
    timestamp: number;
  }) {
    const db = await this.getDB();
    const tx = db.transaction(this.storeName, 'readwrite');
    tx.objectStore(this.storeName).add(mutation);
    return new Promise((resolve) => (tx.oncomplete = resolve));
  }

  // Get tất cả mutations đang chờ
  async getAll(): Promise<any[]> {
    const db = await this.getDB();
    const tx = db.transaction(this.storeName, 'readonly');
    const request = tx.objectStore(this.storeName).getAll();
    return new Promise((resolve) => (request.onsuccess = () => resolve(request.result)));
  }

  // Xóa mutation đã sync thành công
  async remove(id: number) {
    const db = await this.getDB();
    const tx = db.transaction(this.storeName, 'readwrite');
    tx.objectStore(this.storeName).delete(id);
  }

  // ⭐ Sync tất cả queued mutations khi online
  async syncAll(): Promise<{ synced: number; failed: number }> {
    const mutations = await this.getAll();
    let synced = 0, failed = 0;

    for (const mutation of mutations) {
      try {
        const response = await fetch(mutation.url, {
          method: mutation.method,
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(mutation.body),
        });

        if (response.ok) {
          await this.remove(mutation.id);
          synced++;
        } else if (response.status === 409) {
          // ⭐ Conflict! Server data đã thay đổi
          console.warn('Conflict detected, needs manual resolution:', mutation);
          // Handle conflict: last-write-wins, merge, hoặc prompt user
          failed++;
        } else {
          failed++;
        }
      } catch {
        failed++;
        break; // Still offline, stop trying
      }
    }

    return { synced, failed };
  }
}

// ✅ React Hook: Online status + Auto sync
function useOfflineSync() {
  const [isOnline, setIsOnline] = useState(navigator.onLine);
  const [pendingCount, setPendingCount] = useState(0);
  const queueRef = useRef(new OfflineSyncQueue());

  // Track online/offline status
  useEffect(() => {
    const handleOnline = async () => {
      setIsOnline(true);
      // Auto sync khi có mạng trở lại
      const result = await queueRef.current.syncAll();
      console.log(`🔄 Synced: ${result.synced}, Failed: ${result.failed}`);
      updatePendingCount();
    };
    const handleOffline = () => setIsOnline(false);

    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);
    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, []);

  const updatePendingCount = async () => {
    const mutations = await queueRef.current.getAll();
    setPendingCount(mutations.length);
  };

  // Smart fetch: online → network, offline → queue
  const smartFetch = useCallback(
    async (url: string, options: RequestInit = {}) => {
      if (navigator.onLine) {
        return fetch(url, options);
      }

      // Offline: queue non-GET requests
      if (options.method && options.method !== 'GET') {
        await queueRef.current.enqueue({
          url,
          method: options.method,
          body: options.body ? JSON.parse(options.body as string) : null,
          timestamp: Date.now(),
        });
        updatePendingCount();

        // Return fake success response (optimistic)
        return new Response(JSON.stringify({ queued: true }), { status: 202 });
      }

      // GET requests: try cache
      return caches.match(url).then(
        (cached) => cached || new Response('Offline', { status: 503 })
      );
    },
    []
  );

  return { isOnline, pendingCount, smartFetch };
}
```

**🧠 Bài học:**
- **Cache strategies**: Cache First (static), Network First (API), Stale While Revalidate (hybrid)
- **IndexedDB** cho offline mutation queue — persistent storage, không bị clear khi close tab
- **Background Sync API** (`self.registration.sync.register`) để sync khi app đóng
- **Conflict resolution**: Last-write-wins (đơn giản), CRDT (phức tạp), hoặc prompt user

---

### **25.18. 🎯 Form Validation Complex — Async, Cross-Field & Dynamic Rules**

**Vấn đề:** Form phức tạp cần: async validation (check username trùng), cross-field validation (password confirm), dynamic rules (field B required nếu field A = "other"), debounced validation, và UX tốt (validate on blur, validate on submit).

```typescript
/**
 * 🔴 ĐÂU LÀ PHẦN KHÓ:
 * 1. Async validation: check email trùng → debounce → show pending state
 * 2. Cross-field: confirmPassword phải match password → re-validate khi password đổi
 * 3. Dynamic rules: "Nhập lý do khác" chỉ required khi chọn "Khác"
 * 4. Nested objects: address.city, items[0].name
 * 5. UX: validate on blur (first touch) → validate on change (after first error)
 */

// ✅ Custom validation engine
type ValidationRule<T> = {
  validate: (value: any, formValues: T) => boolean | Promise<boolean>;
  message: string | ((value: any, formValues: T) => string);
  debounceMs?: number; // Cho async validations
};

type FieldConfig<T> = {
  rules: ValidationRule<T>[];
  dependencies?: Array<keyof T>; // Re-validate khi dependencies thay đổi
};

type FormConfig<T> = {
  [K in keyof T]?: FieldConfig<T>;
};

interface FieldState {
  value: any;
  error: string | null;
  touched: boolean;
  validating: boolean; // Async validation in progress
  dirty: boolean;
}

function useFormValidation<T extends Record<string, any>>(
  initialValues: T,
  config: FormConfig<T>
) {
  const [values, setValues] = useState<T>(initialValues);
  const [fields, setFields] = useState<Record<keyof T, FieldState>>(() => {
    const initial: any = {};
    for (const key of Object.keys(initialValues)) {
      initial[key] = {
        value: initialValues[key],
        error: null,
        touched: false,
        validating: false,
        dirty: false,
      };
    }
    return initial;
  });

  const debounceTimers = useRef<Map<string, ReturnType<typeof setTimeout>>>(new Map());

  // Validate single field
  const validateField = useCallback(
    async (name: keyof T, value: any, allValues: T): Promise<string | null> => {
      const fieldConfig = config[name];
      if (!fieldConfig) return null;

      for (const rule of fieldConfig.rules) {
        try {
          if (rule.debounceMs) {
            // Mark as validating (show spinner)
            setFields((prev) => ({
              ...prev,
              [name]: { ...prev[name], validating: true },
            }));
          }

          const isValid = await rule.validate(value, allValues);

          if (!isValid) {
            const message =
              typeof rule.message === 'function'
                ? rule.message(value, allValues)
                : rule.message;
            return message;
          }
        } catch {
          return 'Validation error';
        }
      }

      return null;
    },
    [config]
  );

  // Handle field change
  const handleChange = useCallback(
    (name: keyof T) => (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
      const value = e.target.type === 'checkbox'
        ? (e.target as HTMLInputElement).checked
        : e.target.value;

      setValues((prev) => ({ ...prev, [name]: value }));
      setFields((prev) => ({
        ...prev,
        [name]: { ...prev[name], value, dirty: true },
      }));

      // Validate on change ONLY if field was already touched (UX pattern)
      if (fields[name]?.touched) {
        const debounceMs = config[name]?.rules.find((r) => r.debounceMs)?.debounceMs;

        if (debounceMs) {
          // Debounced validation (async checks)
          const existingTimer = debounceTimers.current.get(name as string);
          if (existingTimer) clearTimeout(existingTimer);

          debounceTimers.current.set(
            name as string,
            setTimeout(async () => {
              const newValues = { ...values, [name]: value } as T;
              const error = await validateField(name, value, newValues);
              setFields((prev) => ({
                ...prev,
                [name]: { ...prev[name], error, validating: false },
              }));
            }, debounceMs)
          );
        } else {
          // Instant validation
          const newValues = { ...values, [name]: value } as T;
          validateField(name, value, newValues).then((error) => {
            setFields((prev) => ({
              ...prev,
              [name]: { ...prev[name], error, validating: false },
            }));
          });
        }
      }

      // ⭐ Re-validate dependent fields
      for (const [fieldName, fieldConfig] of Object.entries(config)) {
        if (fieldConfig?.dependencies?.includes(name)) {
          const newValues = { ...values, [name]: value } as T;
          validateField(fieldName as keyof T, newValues[fieldName as keyof T], newValues).then(
            (error) => {
              setFields((prev) => ({
                ...prev,
                [fieldName]: { ...prev[fieldName as keyof T], error, validating: false },
              }));
            }
          );
        }
      }
    },
    [values, fields, config, validateField]
  );

  // Handle blur → first validation
  const handleBlur = useCallback(
    (name: keyof T) => async () => {
      setFields((prev) => ({
        ...prev,
        [name]: { ...prev[name], touched: true },
      }));

      const error = await validateField(name, values[name], values);
      setFields((prev) => ({
        ...prev,
        [name]: { ...prev[name], error, validating: false },
      }));
    },
    [values, validateField]
  );

  // Validate ALL fields (on submit)
  const validateAll = useCallback(async (): Promise<boolean> => {
    const errors: Partial<Record<keyof T, string | null>> = {};
    let isValid = true;

    await Promise.all(
      Object.keys(values).map(async (name) => {
        const error = await validateField(name as keyof T, values[name as keyof T], values);
        errors[name as keyof T] = error;
        if (error) isValid = false;
      })
    );

    // Mark all fields as touched + set errors
    setFields((prev) => {
      const updated = { ...prev };
      for (const [name, error] of Object.entries(errors)) {
        updated[name as keyof T] = {
          ...updated[name as keyof T],
          touched: true,
          error: error as string | null,
          validating: false,
        };
      }
      return updated;
    });

    return isValid;
  }, [values, validateField]);

  // Handle submit
  const handleSubmit = useCallback(
    (onSubmit: (values: T) => void | Promise<void>) =>
      async (e: React.FormEvent) => {
        e.preventDefault();
        const isValid = await validateAll();
        if (isValid) await onSubmit(values);
      },
    [values, validateAll]
  );

  // Helper: get field props
  const getFieldProps = (name: keyof T) => ({
    value: values[name],
    onChange: handleChange(name),
    onBlur: handleBlur(name),
    'aria-invalid': !!fields[name]?.error,
    'aria-describedby': fields[name]?.error ? `${String(name)}-error` : undefined,
  });

  const getFieldState = (name: keyof T) => fields[name];

  return {
    values,
    getFieldProps,
    getFieldState,
    handleSubmit,
    validateAll,
    isValid: Object.values(fields).every((f) => !f.error),
    isDirty: Object.values(fields).some((f) => f.dirty),
  };
}

// ✅ SỬ DỤNG:
function RegistrationForm() {
  const form = useFormValidation(
    { username: '', email: '', password: '', confirmPassword: '', reason: '', otherReason: '' },
    {
      username: {
        rules: [
          { validate: (v) => v.length >= 3, message: 'Tối thiểu 3 ký tự' },
          { validate: (v) => /^[a-zA-Z0-9_]+$/.test(v), message: 'Chỉ chữ, số và _' },
          {
            // ⭐ Async validation + debounce
            validate: async (v) => {
              const res = await fetch(`/api/check-username?u=${v}`);
              const { available } = await res.json();
              return available;
            },
            message: 'Username đã tồn tại',
            debounceMs: 500,
          },
        ],
      },
      email: {
        rules: [
          { validate: (v) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v), message: 'Email không hợp lệ' },
        ],
      },
      password: {
        rules: [
          { validate: (v) => v.length >= 8, message: 'Tối thiểu 8 ký tự' },
          { validate: (v) => /(?=.*[A-Z])(?=.*[0-9])/.test(v), message: 'Cần chữ hoa và số' },
        ],
      },
      confirmPassword: {
        rules: [
          {
            // ⭐ Cross-field validation
            validate: (v, form) => v === form.password,
            message: 'Mật khẩu không khớp',
          },
        ],
        dependencies: ['password'], // Re-validate khi password đổi
      },
      otherReason: {
        rules: [
          {
            // ⭐ Dynamic required: chỉ required khi reason = 'other'
            validate: (v, form) => form.reason !== 'other' || v.length > 0,
            message: 'Vui lòng nhập lý do',
          },
        ],
        dependencies: ['reason'],
      },
    }
  );

  return (
    <form onSubmit={form.handleSubmit(async (values) => {
      await api.register(values);
    })}>
      <div>
        <input placeholder="Username" {...form.getFieldProps('username')} />
        {form.getFieldState('username')?.validating && <span>⏳ Checking...</span>}
        {form.getFieldState('username')?.error && (
          <span className="error">{form.getFieldState('username')!.error}</span>
        )}
      </div>
      {/* ... other fields ... */}
      <button type="submit" disabled={!form.isValid}>Đăng ký</button>
    </form>
  );
}
```

**🧠 Bài học:**
- **Validate on blur first, then on change** — UX pattern tốt nhất (không spam errors khi user đang gõ)
- **Cross-field dependencies** phải tự re-validate khi dependency thay đổi
- **Async validation** cần debounce + loading state + abort previous
- Production: React Hook Form + Zod schema — đã optimize performance + handle edge cases

---

### **25.19. 📊 Real-time Dashboard Với WebSocket + Throttled UI Updates**

**Vấn đề:** Dashboard nhận 100+ messages/giây qua WebSocket → update UI mỗi message → React re-render 100 lần/giây → browser freeze. Cần buffer data + throttle renders mà không mất precision.

```typescript
/**
 * 🔴 VẤN ĐỀ PERFORMANCE:
 * - WebSocket: 100-500 messages/giây (stock prices, sensor data, logs)
 * - React setState mỗi message → 100-500 re-renders/giây
 * - Browser chỉ paint 60fps → 440 renders/giây LÃNG PHÍ
 * - GC pressure: tạo 100 state objects/giây → frequent GC pauses
 *
 * ✅ GIẢI PHÁP: Buffer messages + RAF-throttled renders
 */

// ✅ Custom hook: Buffer WebSocket data + Throttle UI updates
function useRealtimeData<T>({
  wsUrl,
  transform,
  maxDataPoints = 1000,
  throttleMs = 100, // Update UI tối đa mỗi 100ms (10fps — đủ cho dashboard)
}: {
  wsUrl: string;
  transform: (raw: any) => T;
  maxDataPoints?: number;
  throttleMs?: number;
}) {
  // ⭐ useRef cho data buffer — KHÔNG trigger re-render khi nhận message
  const bufferRef = useRef<T[]>([]);
  const dataRef = useRef<T[]>([]);

  // State chỉ update theo throttle schedule
  const [displayData, setDisplayData] = useState<T[]>([]);
  const [stats, setStats] = useState({ messagesPerSec: 0, lastUpdate: 0 });

  const messageCountRef = useRef(0);
  const rafRef = useRef<number | null>(null);
  const lastFlushRef = useRef(Date.now());

  // ⭐ Flush buffer → state (throttled)
  const flushBuffer = useCallback(() => {
    const now = Date.now();

    if (bufferRef.current.length === 0) return;
    if (now - lastFlushRef.current < throttleMs) {
      // Too soon → schedule next flush
      if (!rafRef.current) {
        rafRef.current = requestAnimationFrame(() => {
          rafRef.current = null;
          flushBuffer();
        });
      }
      return;
    }

    // Merge buffer vào main data
    const newData = [...dataRef.current, ...bufferRef.current];

    // Trim nếu vượt maxDataPoints (sliding window)
    const trimmed =
      newData.length > maxDataPoints
        ? newData.slice(-maxDataPoints)
        : newData;

    dataRef.current = trimmed;
    bufferRef.current = []; // Clear buffer
    lastFlushRef.current = now;

    // ⭐ CHỈ setState ở đây — 1 lần mỗi throttleMs
    setDisplayData(trimmed);
    setStats({
      messagesPerSec: messageCountRef.current,
      lastUpdate: now,
    });
    messageCountRef.current = 0;
  }, [throttleMs, maxDataPoints]);

  // WebSocket connection
  useEffect(() => {
    const ws = new WebSocket(wsUrl);

    ws.onmessage = (event) => {
      const data = transform(JSON.parse(event.data));

      // ⭐ Push to buffer (NO re-render!)
      bufferRef.current.push(data);
      messageCountRef.current++;

      // Schedule flush
      flushBuffer();
    };

    // Message rate counter (reset every second)
    const rateInterval = setInterval(() => {
      if (messageCountRef.current > 0) {
        setStats((prev) => ({
          ...prev,
          messagesPerSec: messageCountRef.current,
        }));
        messageCountRef.current = 0;
      }
    }, 1000);

    return () => {
      ws.close();
      clearInterval(rateInterval);
      if (rafRef.current) cancelAnimationFrame(rafRef.current);
    };
  }, [wsUrl, transform, flushBuffer]);

  return { data: displayData, stats };
}

// ✅ ADVANCED: Ring Buffer cho fixed-size data (zero allocation)
class RingBuffer<T> {
  private buffer: (T | undefined)[];
  private head = 0;
  private _size = 0;

  constructor(private capacity: number) {
    this.buffer = new Array(capacity);
  }

  push(item: T): void {
    this.buffer[this.head] = item;
    this.head = (this.head + 1) % this.capacity;
    if (this._size < this.capacity) this._size++;
  }

  toArray(): T[] {
    if (this._size < this.capacity) {
      return this.buffer.slice(0, this._size) as T[];
    }
    // Wrap around: [head...end, start...head-1]
    return [
      ...this.buffer.slice(this.head),
      ...this.buffer.slice(0, this.head),
    ] as T[];
  }

  get size() {
    return this._size;
  }
  get latest(): T | undefined {
    return this.buffer[(this.head - 1 + this.capacity) % this.capacity];
  }
}

// ✅ SỬ DỤNG: Stock price dashboard
function StockDashboard() {
  const { data: prices, stats } = useRealtimeData<StockPrice>({
    wsUrl: 'wss://stream.example.com/stocks',
    transform: (raw) => ({
      symbol: raw.s,
      price: parseFloat(raw.p),
      volume: parseInt(raw.v),
      timestamp: raw.t,
    }),
    maxDataPoints: 500,
    throttleMs: 200, // Update chart 5 lần/giây (đủ smooth)
  });

  return (
    <div>
      <div className="stats-bar">
        📡 {stats.messagesPerSec} msg/s | 📊 {prices.length} data points
      </div>

      {/* Chart chỉ re-render 5 lần/giây thay vì 500 lần */}
      <PriceChart data={prices} />

      {/* Latest prices — cũng throttled */}
      <PriceTable data={prices.slice(-20)} />
    </div>
  );
}

// ✅ Memoize heavy chart component
const PriceChart = React.memo(({ data }: { data: StockPrice[] }) => {
  // Chart library chỉ nhận data mới 5 lần/giây
  return <LineChart data={data} />;
});
```

**🧠 Bài học:**
- **useRef buffer** nhận data KHÔNG re-render → flush với throttle/RAF → setState 1 lần
- **Throttle renders** ở 5-10fps cho dashboard là đủ smooth (mắt người không phân biệt > 10fps cho number/chart)
- **Ring Buffer** (circular buffer) cho fixed-size data — zero memory allocation sau init
- **React.memo** cho chart component — skip re-render nếu data reference giống

---

### **25.20. 🏗️ Complex State Machine Với useReducer + Context — "Quản Lý Multi-Step Wizard"**

**Vấn đề:** Wizard/checkout flow có nhiều steps, mỗi step có validation riêng, navigation rules phức tạp (step 3 chỉ accessible nếu step 1+2 valid), async actions giữa steps, branching logic (different flows based on choices).

```typescript
/**
 * 🔴 ĐỘ PHỨC TẠP:
 * - 5+ steps, mỗi step có state riêng
 * - Navigation rules: step 3 không accessible nếu step 2 chưa complete
 * - Branching: chọn "doanh nghiệp" ở step 1 → hiện thêm step 2b "Thông tin công ty"
 * - Async: step 2 submit → validate server → mới cho qua step 3
 * - Persistence: user đóng tab → quay lại resume từ step cuối
 */

// ✅ State Machine approach
type WizardStep =
  | 'accountType'
  | 'personalInfo'
  | 'companyInfo'    // Chỉ hiện cho business accounts
  | 'verification'
  | 'payment'
  | 'review'
  | 'complete';

type WizardEvent =
  | { type: 'NEXT' }
  | { type: 'BACK' }
  | { type: 'GOTO'; step: WizardStep }
  | { type: 'UPDATE_FIELD'; step: WizardStep; field: string; value: any }
  | { type: 'VALIDATE_STEP'; step: WizardStep; errors: Record<string, string> }
  | { type: 'ASYNC_START' }
  | { type: 'ASYNC_SUCCESS'; data?: any }
  | { type: 'ASYNC_ERROR'; error: string }
  | { type: 'RESTORE'; state: WizardState };

interface StepState {
  data: Record<string, any>;
  errors: Record<string, string>;
  isValid: boolean;
  isComplete: boolean;
  visited: boolean;
}

interface WizardState {
  currentStep: WizardStep;
  steps: Record<WizardStep, StepState>;
  accountType: 'personal' | 'business' | null;
  isSubmitting: boolean;
  asyncError: string | null;
}

// ⭐ Step flow definition — defines valid transitions
const STEP_FLOW: Record<string, { next: (state: WizardState) => WizardStep | null; prev: WizardStep | null }> = {
  accountType: {
    next: (state) =>  'personalInfo',
    prev: null,
  },
  personalInfo: {
    next: (state) =>
      state.accountType === 'business' ? 'companyInfo' : 'verification',
    prev: 'accountType',
  },
  companyInfo: {
    next: () => 'verification',
    prev: 'personalInfo',
  },
  verification: {
    next: () => 'payment',
    prev: null, // Dynamically determined
  },
  payment: {
    next: () => 'review',
    prev: 'verification',
  },
  review: {
    next: () => 'complete',
    prev: 'payment',
  },
};

// ✅ Reducer — Pure state transitions
function wizardReducer(state: WizardState, event: WizardEvent): WizardState {
  switch (event.type) {
    case 'NEXT': {
      const flow = STEP_FLOW[state.currentStep];
      const nextStep = flow?.next(state);
      if (!nextStep) return state;

      // Guard: current step must be valid
      if (!state.steps[state.currentStep].isValid) return state;

      return {
        ...state,
        currentStep: nextStep,
        steps: {
          ...state.steps,
          [state.currentStep]: {
            ...state.steps[state.currentStep],
            isComplete: true,
          },
          [nextStep]: {
            ...state.steps[nextStep],
            visited: true,
          },
        },
      };
    }

    case 'BACK': {
      const flow = STEP_FLOW[state.currentStep];
      const prevStep = flow?.prev;
      if (!prevStep) return state;
      return { ...state, currentStep: prevStep };
    }

    case 'GOTO': {
      // Guard: can only go to visited steps or previous steps
      if (!state.steps[event.step]?.visited) return state;
      return { ...state, currentStep: event.step };
    }

    case 'UPDATE_FIELD': {
      const stepState = state.steps[event.step];
      const newData = { ...stepState.data, [event.field]: event.value };
      const newErrors = { ...stepState.errors };
      delete newErrors[event.field]; // Clear error on change

      return {
        ...state,
        accountType:
          event.step === 'accountType' && event.field === 'type'
            ? event.value
            : state.accountType,
        steps: {
          ...state.steps,
          [event.step]: {
            ...stepState,
            data: newData,
            errors: newErrors,
            isValid: Object.keys(newErrors).length === 0,
          },
        },
      };
    }

    case 'VALIDATE_STEP': {
      const hasErrors = Object.keys(event.errors).length > 0;
      return {
        ...state,
        steps: {
          ...state.steps,
          [event.step]: {
            ...state.steps[event.step],
            errors: event.errors,
            isValid: !hasErrors,
          },
        },
      };
    }

    case 'ASYNC_START':
      return { ...state, isSubmitting: true, asyncError: null };

    case 'ASYNC_SUCCESS':
      return { ...state, isSubmitting: false };

    case 'ASYNC_ERROR':
      return { ...state, isSubmitting: false, asyncError: event.error };

    case 'RESTORE':
      return event.state;

    default:
      return state;
  }
}

// ✅ Context + Hook
const WizardContext = createContext<{
  state: WizardState;
  dispatch: React.Dispatch<WizardEvent>;
  next: () => Promise<boolean>;
  back: () => void;
  goTo: (step: WizardStep) => void;
  updateField: (field: string, value: any) => void;
} | null>(null);

function WizardProvider({ children }: { children: React.ReactNode }) {
  // Restore from sessionStorage
  const savedState = sessionStorage.getItem('wizard_state');
  const initialState: WizardState = savedState
    ? JSON.parse(savedState)
    : createInitialState();

  const [state, dispatch] = useReducer(wizardReducer, initialState);

  // ⭐ Auto-save to sessionStorage (persistence)
  useEffect(() => {
    sessionStorage.setItem('wizard_state', JSON.stringify(state));
  }, [state]);

  // Actions
  const next = useCallback(async () => {
    // Validate current step
    const errors = await validateStep(state.currentStep, state.steps[state.currentStep].data);
    dispatch({ type: 'VALIDATE_STEP', step: state.currentStep, errors });

    if (Object.keys(errors).length > 0) return false;

    // Async validation (e.g., server check)
    if (state.currentStep === 'verification') {
      dispatch({ type: 'ASYNC_START' });
      try {
        await api.verifyIdentity(state.steps.verification.data);
        dispatch({ type: 'ASYNC_SUCCESS' });
      } catch (err) {
        dispatch({ type: 'ASYNC_ERROR', error: (err as Error).message });
        return false;
      }
    }

    dispatch({ type: 'NEXT' });
    return true;
  }, [state]);

  const back = useCallback(() => dispatch({ type: 'BACK' }), []);
  const goTo = useCallback((step: WizardStep) => dispatch({ type: 'GOTO', step }), []);
  const updateField = useCallback(
    (field: string, value: any) =>
      dispatch({ type: 'UPDATE_FIELD', step: state.currentStep, field, value }),
    [state.currentStep]
  );

  return (
    <WizardContext.Provider value={{ state, dispatch, next, back, goTo, updateField }}>
      {children}
    </WizardContext.Provider>
  );
}

function useWizard() {
  const ctx = useContext(WizardContext);
  if (!ctx) throw new Error('useWizard must be used within WizardProvider');
  return ctx;
}

// ✅ Step indicators with navigation
function StepIndicator() {
  const { state, goTo } = useWizard();

  const visibleSteps = getVisibleSteps(state); // Filter based on accountType

  return (
    <nav aria-label="Wizard steps">
      <ol style={{ display: 'flex', gap: 16 }}>
        {visibleSteps.map((step, i) => {
          const stepState = state.steps[step];
          const isCurrent = state.currentStep === step;

          return (
            <li key={step}>
              <button
                onClick={() => goTo(step)}
                disabled={!stepState.visited}
                aria-current={isCurrent ? 'step' : undefined}
                style={{
                  fontWeight: isCurrent ? 'bold' : 'normal',
                  color: stepState.isComplete
                    ? 'green'
                    : isCurrent
                      ? 'blue'
                      : '#999',
                }}
              >
                {stepState.isComplete ? '✅' : `${i + 1}.`} {getStepTitle(step)}
              </button>
            </li>
          );
        })}
      </ol>
    </nav>
  );
}

// ✅ Step content renderer
function WizardContent() {
  const { state } = useWizard();

  const StepComponent = STEP_COMPONENTS[state.currentStep];
  return <StepComponent />;
}

// ✅ Navigation buttons
function WizardNavigation() {
  const { state, next, back } = useWizard();
  const flow = STEP_FLOW[state.currentStep];

  return (
    <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: 24 }}>
      {flow?.prev && (
        <button onClick={back} disabled={state.isSubmitting}>
          ← Quay lại
        </button>
      )}
      <button
        onClick={next}
        disabled={state.isSubmitting || !state.steps[state.currentStep].isValid}
      >
        {state.isSubmitting
          ? '⏳ Đang xử lý...'
          : state.currentStep === 'review'
            ? '✅ Hoàn tất'
            : 'Tiếp theo →'}
      </button>
    </div>
  );
}
```

**🧠 Bài học:**
- **State Machine** (finite states + transitions) cho wizard → không thể ở state "bất hợp lệ"
- **useReducer** > useState cho complex state với nhiều transitions liên quan nhau
- **Branching flow**: Step flow dựa trên state (personal vs business → khác steps)
- **Persistence**: `sessionStorage` auto-save → user quay lại resume đúng step
- **Guards**: Mỗi transition có điều kiện (step phải valid mới cho next)
- Production: XState library cho full state machine với visualization + testing

---

### **📊 Tổng Kết 20 Cases**

| # | Case | Độ Khó | Keyword |
|---|------|--------|---------|
| 1 | Race Condition API | ⭐⭐⭐ | AbortController, Request ID, Debounce |
| 2 | Memory Leak SPA | ⭐⭐⭐⭐ | Cleanup, WeakRef, isMountedRef |
| 3 | Stale Closure Hooks | ⭐⭐⭐⭐ | Functional updater, useRef, useEvent |
| 4 | Optimistic UI | ⭐⭐⭐⭐ | Snapshot, Rollback, TempId |
| 5 | Virtualized List | ⭐⭐⭐⭐⭐ | Window rendering, Dynamic height, Binary search |
| 6 | WebSocket Reconnect | ⭐⭐⭐⭐ | Exponential Backoff, Jitter, Heartbeat |
| 7 | Cross-Tab Sync | ⭐⭐⭐ | BroadcastChannel, Storage Event |
| 8 | XSS in Rich Text | ⭐⭐⭐⭐⭐ | DOMPurify, Whitelist, CSP |
| 9 | Concurrent Fetching | ⭐⭐⭐⭐ | Promise.allSettled, Suspense, Error Boundary |
| 10 | Layout Shift (CLS) | ⭐⭐⭐ | Skeleton, aspect-ratio, font-display, contain |
| 11 | Drag & Drop Reorder | ⭐⭐⭐⭐ | Pointer Events, setPointerCapture, Auto-scroll, a11y |
| 12 | Bidirectional Infinite Scroll | ⭐⭐⭐⭐⭐ | Scroll anchoring, IntersectionObserver, Memory trim |
| 13 | Micro-Frontend Communication | ⭐⭐⭐⭐ | Event Bus, Custom Elements, Shadow DOM, Module Federation |
| 14 | Token Refresh Queue | ⭐⭐⭐⭐ | Singleton refresh, Promise queue, Axios interceptor |
| 15 | Image Upload Pipeline | ⭐⭐⭐ | Canvas compress, XHR progress, URL.createObjectURL |
| 16 | Undo/Redo System | ⭐⭐⭐⭐⭐ | Command Pattern, Batch undo, Branching history |
| 17 | Offline-First App | ⭐⭐⭐⭐⭐ | Service Worker, IndexedDB, Cache strategies, Conflict |
| 18 | Complex Form Validation | ⭐⭐⭐⭐ | Async validate, Cross-field deps, Dynamic rules, Debounce |
| 19 | Real-time Dashboard | ⭐⭐⭐⭐ | Ref buffer, RAF throttle, Ring buffer, React.memo |
| 20 | Multi-Step Wizard State Machine | ⭐⭐⭐⭐⭐ | useReducer, Branching flow, Guards, sessionStorage |

> **"Một Senior Frontend Developer không chỉ biết code chạy đúng, mà phải biết code chạy đúng TRONG MỌI ĐIỀU KIỆN — mất mạng, data lỗi, user thao tác bất thường, và performance scale."**

---

## **📚 Related Questions**

| File | Chủ đề | Mức độ |
| ---- | ------ | ------ |
| [Q02](./Q02-data-types-&-memory-management-tổng-hợp.md) | Data Types & Memory | ⭐⭐⭐⭐ |
| [Q03](./Q03-es5-vs-es6+-features-so-sánh-chi-tiết-&-cách-hoạt-động.md) | ES6+ Features | ⭐⭐⭐ |
| [Q06](<./Q06-event-loop-cơ-chế-hoạt-động-javascript-(technical-deep-dive).md>) | Event Loop | ⭐⭐⭐⭐⭐ |
| [Q08](./Q08-closure-&-data-privacy.md) | Closures | ⭐⭐⭐⭐ |
| [Q13](./Q13-asyncawait-vs-promises-vs-callbacks-&-promise.allanyrace.md) | Async/Await | ⭐⭐⭐⭐ |

---

**Happy Learning! 🚀**

> "JavaScript is the language of the web. Master it, and you master the frontend."
