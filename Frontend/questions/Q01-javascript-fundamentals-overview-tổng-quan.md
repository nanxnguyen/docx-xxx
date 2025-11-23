# 🚀 Q01: JavaScript Fundamentals Overview - Tổng Quan Nền Tảng

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
 * ┌──────────────────────────────────────────────────────────┐
 * │              JAVASCRIPT - HIGH-LEVEL OVERVIEW            │
 * ├──────────────────────────────────────────────────────────┤
 * │                                                          │
 * │  🎯 ĐỊNH NGHĨA:                                         │
 * │  • High-level programming language                      │
 * │  • Interpreted (JIT compiled)                           │
 * │  • Single-threaded                                      │
 * │  • Non-blocking (Event Loop)                            │
 * │  • Prototype-based OOP                                  │
 * │  • First-class functions                                │
 * │                                                          │
 * │  🌐 RUN ENVIRONMENTS:                                   │
 * │  • Browser (V8, SpiderMonkey, JavaScriptCore)          │
 * │  • Node.js (Server-side)                               │
 * │  • Deno, Bun (Modern runtimes)                         │
 * │                                                          │
 * └──────────────────────────────────────────────────────────┘
 */

// JavaScript chạy ở đâu?
const environments = [
  'Browser: DOM manipulation, Events, Fetch API',
  'Node.js: File system, HTTP servers, CLI tools',
  'Mobile: React Native, Ionic',
  'Desktop: Electron, Tauri',
  'IoT: Johnny-Five, Espruino'
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
 * 🎯 Key Concepts:
 * • Stack vs Heap memory
 * • Pass by value vs reference
 * • Shallow vs deep copy
 * • Immutability patterns
 * 
 * 📚 Chi tiết: Q02-data-types-&-memory-management
 */
```

### **2.2. Type Coercion & Comparison**

```typescript
/**
 * ⚠️ Type Coercion
 */

// Implicit coercion
console.log(5 + '5');    // '55' (number → string)
console.log('5' - 2);    // 3 (string → number)
console.log(true + 1);   // 2 (boolean → number)

// Comparison
console.log(5 == '5');   // true (loose equality)
console.log(5 === '5');  // false (strict equality)

// Falsy values (8 values)
Boolean(false);      // false
Boolean(0);          // false
Boolean('');         // false
Boolean(null);       // false
Boolean(undefined);  // false
Boolean(NaN);        // false
Boolean(-0);         // false
Boolean(0n);         // false

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
function greet() { console.log('Hi'); }

/**
 * 📚 Chi tiết: Q04-hoisting-&-temporal-dead-zone
 */
```

### **3.2. Scope & Closures**

```typescript
/**
 * 🔒 CLOSURES
 */

function createCounter() {
  let count = 0; // Private variable
  
  return {
    increment: () => ++count,
    getCount: () => count
  };
}

const counter = createCounter();
console.log(counter.increment()); // 1
console.log(counter.getCount());  // 1

/**
 * 🎯 Use cases:
 * • Data privacy
 * • Factory functions
 * • Event handlers
 * • Callbacks
 * 
 * 📚 Chi tiết: Q08-closure-&-data-privacy
 */
```

### **3.3. Event Loop**

```typescript
/**
 * ⚡ EVENT LOOP
 */

console.log('1: Sync');

setTimeout(() => console.log('2: Macro task'), 0);

Promise.resolve().then(() => console.log('3: Micro task'));

console.log('4: Sync');

/**
 * Output:
 * 1: Sync
 * 4: Sync
 * 3: Micro task
 * 2: Macro task
 * 
 * 📚 Chi tiết:
 * • Q06-event-loop (Technical deep dive)
 * • Q07-event-loop (Giải thích đời thường)
 */
```

---

## **IV. Asynchronous JavaScript**

### **4.1. Callbacks → Promises → Async/Await**

```typescript
/**
 * 🔄 EVOLUTION OF ASYNC
 */

// 1. Callbacks (Callback hell)
getData((data) => {
  processData(data, (result) => {
    saveResult(result, () => {
      console.log('Done');
    });
  });
});

// 2. Promises (Better)
getData()
  .then(processData)
  .then(saveResult)
  .then(() => console.log('Done'))
  .catch(handleError);

// 3. Async/Await (Best)
async function workflow() {
  try {
    const data = await getData();
    const result = await processData(data);
    await saveResult(result);
    console.log('Done');
  } catch (error) {
    handleError(error);
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
  fetchComments()
]);

// Promise.race (First to resolve)
const fastest = await Promise.race([
  fetchFromServer1(),
  fetchFromServer2()
]);

// Promise.allSettled (All results, success or fail)
const results = await Promise.allSettled([
  fetchUsers(),
  fetchPosts()
]);

/**
 * 📚 Chi tiết: Q13, Q28-cancellation-concurrency-&-retry
 */
```

---

## **V. Object-Oriented & Functional**

### **5.1. Classes & Prototypes**

```typescript
/**
 * 🏗️ OOP in JavaScript
 */

// ES6 Classes
class Person {
  constructor(public name: string, private age: number) {}
  
  greet() {
    return `Hi, I'm ${this.name}`;
  }
}

const john = new Person('John', 30);

// Prototype chain
console.log(john.__proto__ === Person.prototype); // true
console.log(Person.prototype.__proto__ === Object.prototype); // true

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
const updated = users.map(u => ({ ...u, age: 30 })); // New array

// Higher-order functions
const withLogging = (fn: Function) => (...args: any[]) => {
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
 * ⚡ ESSENTIAL ES6+ FEATURES
 */

// Destructuring
const { name, age } = user;
const [first, second] = array;

// Spread/Rest
const merged = { ...obj1, ...obj2 };
const combined = [...arr1, ...arr2];

// Arrow functions
const multiply = (a, b) => a * b;

// Template literals
const greeting = `Hello, ${name}!`;

// Optional chaining
const city = user?.address?.city;

// Nullish coalescing
const theme = settings?.theme ?? 'light';

// Modules
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
  }
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
 * 🌐 BROWSER APIs
 */

// DOM manipulation
const element = document.querySelector('.container');
element?.addEventListener('click', handleClick);

// Event delegation
document.body.addEventListener('click', (e) => {
  if ((e.target as HTMLElement).matches('.button')) {
    console.log('Button clicked');
  }
});

// Fetch API
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
  'Q13: Async/Await & Promises'
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
  'Q25: React Hooks & Patterns'
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
  'Q46: Build Tools (Vite/Webpack)'
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

## **🎯 Quick Reference Card**

```typescript
/**
 * ┌──────────────────────────────────────────────────────────┐
 * │         JAVASCRIPT FUNDAMENTALS CHEAT SHEET              │
 * ├──────────────────────────────────────────────────────────┤
 * │                                                          │
 * │  📌 DATA TYPES:                                         │
 * │  • 7 Primitives + 1 Object                              │
 * │  • Stack (primitives) vs Heap (objects)                 │
 * │                                                          │
 * │  📌 EXECUTION:                                          │
 * │  • Hoisting: var (undefined), let/const (TDZ)          │
 * │  • Scope: Global, Function, Block                      │
 * │  • Closures: Functions remember outer scope            │
 * │                                                          │
 * │  📌 ASYNC:                                              │
 * │  • Event Loop: Call Stack → Micro → Macro             │
 * │  • Promises: then/catch chains                         │
 * │  • Async/Await: Syntactic sugar for promises          │
 * │                                                          │
 * │  📌 ES6+:                                               │
 * │  • Arrow functions, Destructuring, Spread              │
 * │  • Optional chaining (?.), Nullish coalescing (??)    │
 * │  • Modules (import/export)                             │
 * │                                                          │
 * │  📌 DOM:                                                │
 * │  • querySelector, addEventListener                      │
 * │  • Event bubbling/capturing                            │
 * │  • Fetch API, async requests                           │
 * │                                                          │
 * └──────────────────────────────────────────────────────────┘
 */
```

---

## **📚 Related Questions**

| Câu hỏi | Chủ đề | Mức độ |
|---------|--------|--------|
| [Q02](./Q02-data-types-&-memory-management-tổng-hợp.md) | Data Types & Memory | ⭐⭐⭐⭐ |
| [Q03](./Q03-es5-vs-es6+-features-so-sánh-chi-tiết-&-cách-hoạt-động.md) | ES6+ Features | ⭐⭐⭐ |
| [Q06](./Q06-event-loop-cơ-chế-hoạt-động-javascript-(technical-deep-dive).md) | Event Loop (Technical) | ⭐⭐⭐⭐⭐ |
| [Q08](./Q08-closure-&-data-privacy.md) | Closures | ⭐⭐⭐⭐ |
| [Q13](./Q13-asyncawait-vs-promises-vs-callbacks-&-promise.allanyrace.md) | Async/Await | ⭐⭐⭐⭐ |

---

**Happy Learning! 🚀**

> "JavaScript is the language of the web. Master it, and you master the frontend."
