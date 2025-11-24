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

## **IX. JavaScript Core Deep Dive & Best Practices**

### **9.1. This Keyword - Context Binding**

```typescript
/**
 * 🎯 'this' KEYWORD - 4 BINDING RULES
 */

// ══════════════════════════════════════════════════════════
// 1. DEFAULT BINDING (Global context)
// ══════════════════════════════════════════════════════════

function showThis() {
  console.log(this); // Window (browser) or undefined (strict mode)
}

showThis();

// Strict mode
'use strict';
function strictThis() {
  console.log(this); // undefined
}

// ══════════════════════════════════════════════════════════
// 2. IMPLICIT BINDING (Object method)
// ══════════════════════════════════════════════════════════

const person = {
  name: 'John',
  greet() {
    console.log(this.name); // 'John' (this = person)
  }
};

person.greet(); // ✅ 'John'

// ❌ Lost binding
const greetFn = person.greet;
greetFn(); // undefined (this = window/undefined)

// ══════════════════════════════════════════════════════════
// 3. EXPLICIT BINDING (call, apply, bind)
// ══════════════════════════════════════════════════════════

function introduce(age: number, city: string) {
  console.log(`${this.name}, ${age}, ${city}`);
}

const user = { name: 'Alice' };

// call: immediate invocation
introduce.call(user, 25, 'NYC'); // Alice, 25, NYC

// apply: arguments as array
introduce.apply(user, [25, 'NYC']); // Alice, 25, NYC

// bind: returns new function
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
    setTimeout(function() {
      console.log(this.name); // undefined (this = window)
    }, 100);
  },
  
  // Arrow function (inherits this from parent)
  arrow() {
    setTimeout(() => {
      console.log(this.name); // 'Object' (this = obj)
    }, 100);
  }
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

// Add method to prototype (shared across instances)
Animal.prototype.speak = function() {
  return `${this.name} makes a sound`;
};

const dog = new Animal('Dog');

console.log(dog.speak()); // 'Dog makes a sound'
console.log(dog.__proto__ === Animal.prototype); // true
console.log(Animal.prototype.constructor === Animal); // true

/**
 * Prototype chain:
 * dog → Animal.prototype → Object.prototype → null
 */

// ══════════════════════════════════════════════════════════
// PROTOTYPAL INHERITANCE (ES5)
// ══════════════════════════════════════════════════════════

function Dog(name: string, breed: string) {
  Animal.call(this, name); // Call parent constructor
  this.breed = breed;
}

// Set up inheritance
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

// Override method
Dog.prototype.speak = function() {
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
  constructor(public name: string, private age: number) {}
  
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
  constructor(name: string, age: number, public role: string) {
    super(name, age); // Call parent constructor
  }
  
  // Override method
  greet() {
    return `${super.greet()}, I'm a ${this.role}`;
  }
}

const emp = new Employee('Alice', 30, 'Developer');
console.log(emp.greet()); // "Hi, I'm Alice, I'm a Developer"

/**
 * 🎯 Key Concepts:
 * • Prototype chain: object → prototype → Object.prototype → null
 * • Shared methods: Define on prototype (memory efficient)
 * • Own properties: Define in constructor
 * • Inheritance: Object.create() or extends keyword
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

// ❌ 1. Global variables
window.leakedData = new Array(1000000); // Never collected

// ❌ 2. Forgotten timers
setInterval(() => {
  // References keep growing
  const data = fetchData();
}, 1000);

// ✅ Fix: Clear timer
const timerId = setInterval(/* ... */);
clearInterval(timerId);

// ❌ 3. Closures holding references
function createLeak() {
  const largeData = new Array(1000000);
  
  return function() {
    console.log(largeData.length); // Keeps largeData in memory
  };
}

// ❌ 4. DOM references
const elements = [];
for (let i = 0; i < 1000; i++) {
  const el = document.createElement('div');
  elements.push(el); // Keeps all elements in memory
}

// ✅ Fix: Remove references when done
elements.length = 0;

// ❌ 5. Event listeners
const button = document.querySelector('button');
button?.addEventListener('click', handleClick); // Keeps button in memory

// ✅ Fix: Remove listener
button?.removeEventListener('click', handleClick);

// ══════════════════════════════════════════════════════════
// WEAKMAP/WEAKSET (Auto garbage collection)
// ══════════════════════════════════════════════════════════

// ✅ WeakMap: Keys can be garbage collected
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
  constructor(
    message: string,
    public field: string
  ) {
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
fetchData().catch(error => {
  console.error('Failed:', error);
});

// ✅ Global handler (last resort)
window.addEventListener('unhandledrejection', event => {
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
searchInput?.addEventListener('input', debounce((e) => {
  search(e.target.value);
}, 300));

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
      setTimeout(() => inThrottle = false, limit);
    }
  };
}

// Usage: Scroll event
window.addEventListener('scroll', throttle(() => {
  console.log('Scrolled');
}, 100));

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
const obj = { a: 1, b: 2, /* ...1000 props */ };
obj.hasOwnProperty('z'); // O(n) in worst case

// ✅ Fast: Map
const map = new Map(Object.entries(obj));
map.has('z'); // O(1)

// ══════════════════════════════════════════════════════════
// 6. AVOID LAYOUT THRASHING
// ══════════════════════════════════════════════════════════

// ❌ Layout thrashing (read/write interleaved)
elements.forEach(el => {
  const width = el.offsetWidth; // Read (forces layout)
  el.style.width = width + 10 + 'px'; // Write
});

// ✅ Batch reads, then batch writes
const widths = elements.map(el => el.offsetWidth); // Batch reads
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
function validateUser(data: any) { /* ... */ }
function transformUser(data: any) { /* ... */ }
function saveUser(data: any) { /* ... */ }
function notifyUser(data: any) { /* ... */ }

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
function calc(a, b) { return a * b; }

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
 * 🎯 Code Quality Checklist:
 * ✅ Use immutable data structures
 * ✅ Write pure functions (no side effects)
 * ✅ Single responsibility per function
 * ✅ Early returns (guard clauses)
 * ✅ Descriptive variable/function names
 * ✅ Avoid magic numbers (use constants)
 * ✅ Keep functions small (<20 lines)
 * ✅ Use TypeScript for type safety
 * ✅ Comment complex logic
 * ✅ Write tests (unit, integration)
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
    'X-CSRF-Token': getCsrfToken()
  },
  body: JSON.stringify({ amount: 100 })
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

// ❌ Bad: 2 iterations (O(2n) = O(n))
const activeUserNames = users
  .filter(u => u.active)      // Iteration 1
  .map(u => u.name);          // Iteration 2

// ✅ Good: 1 iteration with reduce (O(n))
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
 * Performance comparison (10,000 items):
 * • filter + map: ~2ms
 * • reduce: ~1.2ms (40% faster)
 * • for loop: ~0.8ms (60% faster)
 */

// ══════════════════════════════════════════════════════════
// MISTAKE 2: Multiple filter/map/reduce chains
// ══════════════════════════════════════════════════════════

// ❌ Bad: 4 iterations
const result = data
  .filter(x => x.age > 18)       // Iteration 1
  .map(x => ({ ...x, adult: true })) // Iteration 2
  .filter(x => x.active)         // Iteration 3
  .map(x => x.name);             // Iteration 4

// ✅ Good: 1 iteration
const result = data.reduce((acc, x) => {
  if (x.age > 18 && x.active) {
    acc.push(x.name);
  }
  return acc;
}, [] as string[]);

// ══════════════════════════════════════════════════════════
// MISTAKE 3: find() trong loop
// ══════════════════════════════════════════════════════════

const orders = [/* 1000 orders */];
const products = [/* 1000 products */];

// ❌ Bad: O(n²) - 1,000,000 operations!
const enrichedOrders = orders.map(order => ({
  ...order,
  product: products.find(p => p.id === order.productId) // O(n) inside O(n)
}));

// ✅ Good: O(n) - 2,000 operations
const productMap = new Map(products.map(p => [p.id, p])); // O(n)
const enrichedOrders = orders.map(order => ({
  ...order,
  product: productMap.get(order.productId) // O(1)
})); // O(n)

/**
 * Performance comparison (1,000 items):
 * • find in loop: ~500ms (O(n²))
 * • Map lookup: ~2ms (O(n))
 * → 250x faster!
 */

// ══════════════════════════════════════════════════════════
// MISTAKE 4: includes() trong loop
// ══════════════════════════════════════════════════════════

const selectedIds = [1, 2, 3, /* ... 1000 ids */];
const allItems = [/* ... 10000 items */];

// ❌ Bad: O(n²)
const selectedItems = allItems.filter(item => 
  selectedIds.includes(item.id) // O(n) inside O(n)
);

// ✅ Good: O(n)
const selectedIdsSet = new Set(selectedIds); // O(n)
const selectedItems = allItems.filter(item => 
  selectedIdsSet.has(item.id) // O(1)
);
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

// ❌ Bad: O(n) per lookup
function getUserName(userId: number) {
  const user = users.find(u => u.id === userId); // Linear search
  return user?.name;
}

// Called 1000 times = O(n × m) = 10,000,000 operations!
for (let i = 0; i < 1000; i++) {
  getUserName(randomId());
}

// ✅ Good: O(1) per lookup
const userMap = new Map(users.map(u => [u.id, u]));

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
const unique = numbers.filter((num, index) => 
  numbers.indexOf(num) === index // O(n) inside O(n)
);

// ✅ Good: O(n) with Set
const unique = [...new Set(numbers)];

// ✅ Alternative: O(n) with object
const unique = numbers.reduce((acc, num) => {
  if (!acc.seen[num]) {
    acc.seen[num] = true;
    acc.result.push(num);
  }
  return acc;
}, { seen: {}, result: [] as number[] }).result;

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

// ✅ Fast: Direct property access with optional chaining
for (let i = 0; i < 100000; i++) {
  if (config.apiUrl !== undefined) {
    // ...
  }
}

// ✅ Best: Use Map for dynamic keys
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
items.forEach(item => {
  const div = document.createElement('div');
  div.textContent = item;
  container.appendChild(div); // Triggers reflow each time!
});

// ✅ Good: 1 reflow with DocumentFragment
const fragment = document.createDocumentFragment();
items.forEach(item => {
  const div = document.createElement('div');
  div.textContent = item;
  fragment.appendChild(div); // No reflow
});
container.appendChild(fragment); // Single reflow

// ✅ Better: innerHTML (fastest for large lists)
container.innerHTML = items
  .map(item => `<div>${item}</div>`)
  .join('');

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
elements.forEach(el => {
  const height = el.offsetHeight; // Read (forces layout)
  el.style.height = height * 2 + 'px'; // Write
  // Each read forces browser to recalculate layout!
});

// ✅ Good: Batch reads, then batch writes
const heights = Array.from(elements).map(el => el.offsetHeight); // Batch reads
elements.forEach((el, i) => {
  el.style.height = heights[i] * 2 + 'px'; // Batch writes
});

// ══════════════════════════════════════════════════════════
// MISTAKE 10: querySelector in loops
// ══════════════════════════════════════════════════════════

// ❌ Bad: Re-query DOM every iteration
for (let i = 0; i < 1000; i++) {
  const container = document.querySelector('.container'); // Query 1000 times!
  container.innerHTML += `<div>Item ${i}</div>`;
}

// ✅ Good: Cache reference
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

// ✅ Good: Memoize or move outside component
const CONFIG = { theme: 'dark', locale: 'en' };
const FILTERS = ['active', 'verified'];

function UserList() {
  return (
    <ExpensiveChild
      config={CONFIG}
      filters={FILTERS}
    />
  );
}

// ✅ Better: useMemo for dynamic values
function UserList({ theme, showActive }) {
  const config = useMemo(
    () => ({ theme, locale: 'en' }),
    [theme]
  );
  
  const filters = useMemo(
    () => showActive ? ['active', 'verified'] : ['verified'],
    [showActive]
  );
  
  return <ExpensiveChild config={config} filters={filters} />;
}

// ══════════════════════════════════════════════════════════
// MISTAKE 12: Inline functions as props
// ══════════════════════════════════════════════════════════

// ❌ Bad: New function every render
function TodoList({ todos }) {
  return (
    <div>
      {todos.map(todo => (
        <TodoItem
          key={todo.id}
          todo={todo}
          onDelete={() => deleteTodo(todo.id)} // New function!
        />
      ))}
    </div>
  );
}

// ✅ Good: useCallback or pass ID
function TodoList({ todos }) {
  const handleDelete = useCallback((id: number) => {
    deleteTodo(id);
  }, []);
  
  return (
    <div>
      {todos.map(todo => (
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

// ✅ Good: Stable unique ID
items.map(item => (
  <div key={item.id}>{item.name}</div>
));

// ══════════════════════════════════════════════════════════
// MISTAKE 14: Not memoizing expensive calculations
// ══════════════════════════════════════════════════════════

function DataTable({ data, filter }) {
  // ❌ Bad: Recalculates every render (even when data unchanged)
  const sortedData = data
    .filter(item => item.status === filter)
    .sort((a, b) => a.name.localeCompare(b.name));
  
  return <Table data={sortedData} />;
}

// ✅ Good: Memoize calculation
function DataTable({ data, filter }) {
  const sortedData = useMemo(() => {
    return data
      .filter(item => item.status === filter)
      .sort((a, b) => a.name.localeCompare(b.name));
  }, [data, filter]); // Only recalculate when dependencies change
  
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

// ❌ Bad: Duplicate source of truth
function UserProfile({ user }) {
  const [fullName, setFullName] = useState('');
  
  useEffect(() => {
    setFullName(`${user.firstName} ${user.lastName}`);
  }, [user]);
  
  return <div>{fullName}</div>;
}

// ✅ Good: Compute during render
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

// If count is already 5 and you set it to 5, React still re-renders!

// ✅ Good: Use functional update or check before setting
function Counter() {
  const [count, setCount] = useState(0);
  
  const increment = () => {
    setCount(prev => prev + 1); // Functional update
  };
  
  const setValue = (newValue: number) => {
    setCount(prev => {
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
  profile: { name: 'John', address: { city: 'NYC' } }
});

// ❌ Bad: Mutation (doesn't trigger re-render)
const updateCity = (city: string) => {
  user.profile.address.city = city; // Mutation!
  setUser(user); // Same reference, no re-render
};

// ✅ Good: Immutable update
const updateCity = (city: string) => {
  setUser(prev => ({
    ...prev,
    profile: {
      ...prev.profile,
      address: {
        ...prev.profile.address,
        city
      }
    }
  }));
};

// ✅ Better: Use Immer
import { produce } from 'immer';

const updateCity = (city: string) => {
  setUser(produce(draft => {
    draft.profile.address.city = city; // Looks like mutation, but immutable!
  }));
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

// ❌ Bad: Sequential (3 seconds total)
async function fetchData() {
  const users = await fetchUsers();      // 1s
  const posts = await fetchPosts();      // 1s
  const comments = await fetchComments(); // 1s
  
  return { users, posts, comments };
}

// ✅ Good: Parallel (1 second total)
async function fetchData() {
  const [users, posts, comments] = await Promise.all([
    fetchUsers(),      // All start together
    fetchPosts(),
    fetchComments()
  ]);
  
  return { users, posts, comments };
}

/**
 * Performance:
 * • Sequential: 3s (1s + 1s + 1s)
 * • Parallel: 1s (max of all)
 * → 3x faster!
 */

// ══════════════════════════════════════════════════════════
// MISTAKE 19: Promise in loop (sequential)
// ══════════════════════════════════════════════════════════

const userIds = [1, 2, 3, 4, 5];

// ❌ Bad: Sequential (5 seconds)
const users = [];
for (const id of userIds) {
  const user = await fetchUser(id); // Wait for each!
  users.push(user);
}

// ✅ Good: Parallel (1 second)
const users = await Promise.all(
  userIds.map(id => fetchUser(id))
);

// ══════════════════════════════════════════════════════════
// MISTAKE 20: Not handling promise rejections
// ══════════════════════════════════════════════════════════

// ❌ Bad: Unhandled rejection crashes app
fetchData(); // If rejects, app crashes in production!

// ✅ Good: Always handle errors
fetchData()
  .then(data => console.log(data))
  .catch(error => console.error('Failed:', error));

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
window.addEventListener('unhandledrejection', event => {
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

// ✅ Good: Extract only what you need
function createHandler(items: LargeObject[]) {
  const length = items.length; // Only store length
  
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

// ✅ Good: Lazy load when needed
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
 * Bundle size:
 * • Before: 500KB loaded upfront
 * • After: 500KB loaded only when needed
 * → Initial load 500KB smaller!
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
  '❌ No monitoring': 'Use Lighthouse, Web Vitals'
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

// ❌ Vulnerable: URL parameter directly in HTML
const searchQuery = new URLSearchParams(location.search).get('q');
document.body.innerHTML = `<h1>Results for: ${searchQuery}</h1>`;

// Attack: ?q=<script>alert(document.cookie)</script>

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

// ❌ Vulnerable: User input stored and rendered
const comment = await fetchComment(); // From database
element.innerHTML = comment.text; // XSS if comment contains <script>

// ✅ Fix: Sanitize on display
element.innerHTML = DOMPurify.sanitize(comment.text);

// ✅ Better: Sanitize on server before storing
// Backend validation + sanitization

// ══════════════════════════════════════════════════════════
// DOM-BASED XSS
// ══════════════════════════════════════════════════════════

// ❌ Vulnerable: eval() or Function()
const userCode = getUserInput();
eval(userCode); // Never do this!

// ❌ Vulnerable: innerHTML with user data
const name = location.hash.slice(1);
element.innerHTML = `<div>Hello ${name}</div>`;

// ✅ Fix: Use safe DOM methods
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
</Helmet>
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
 * User logged into bank.com
 * Attacker sends email with:
 * <img src="https://bank.com/transfer?to=attacker&amount=1000">
 * 
 * Browser automatically sends cookies → Money transferred!
 */

// ══════════════════════════════════════════════════════════
// PREVENTION 1: CSRF Token
// ══════════════════════════════════════════════════════════

// Server generates token per session/request
// Backend sets token in cookie or meta tag

// ✅ Include token in all state-changing requests
const csrfToken = document.querySelector('meta[name="csrf-token"]')?.content;

fetch('/api/transfer', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-CSRF-Token': csrfToken
  },
  body: JSON.stringify({ to: 'recipient', amount: 1000 })
});

// Server validates token matches session

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

// Simple requests (GET, POST with simple content-type) auto-send cookies
// But custom headers require preflight (CORS), which attacker can't do

fetch('/api/transfer', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest' // Custom header
  },
  body: JSON.stringify({ to: 'recipient', amount: 1000 })
});

// Server checks for custom header presence
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

// ❌ JWT in localStorage (Vulnerable to XSS)
localStorage.setItem('token', jwt);

fetch('/api/protected', {
  headers: {
    Authorization: `Bearer ${localStorage.getItem('token')}`
  }
});

// ✅ HttpOnly cookies (Safe from XSS)
// Server sets: Set-Cookie: session=abc123; HttpOnly; Secure; SameSite=Strict

fetch('/api/protected', {
  credentials: 'include' // Send cookies automatically
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
    credentials: 'include' // Sends refresh token cookie
  });
  
  const { accessToken: newToken } = await response.json();
  accessToken = newToken;
  return newToken;
}

// Axios interceptor for auto-refresh
axios.interceptors.response.use(
  response => response,
  async error => {
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
  }
);

// ══════════════════════════════════════════════════════════
// PASSWORD SECURITY
// ══════════════════════════════════════════════════════════

// ✅ Client-side validation (UX)
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

// ✅ Backend hashing (NEVER store plaintext!)
// bcrypt with salt rounds >= 12
// const hash = await bcrypt.hash(password, 12);
```

---

## **XIII. React Performance Patterns**

### **13.1. Virtual Scrolling (Large Lists)**

```typescript
/**
 * 📜 VIRTUAL SCROLLING
 */

// ❌ Problem: Rendering 10,000 items = slow
function BadList({ items }) {
  return (
    <div>
      {items.map(item => (
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
    <div style={style}>
      {items[index].name}
    </div>
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
 * Performance (10,000 items):
 * • Full render: ~500ms, 10,000 DOM nodes
 * • Virtual scroll: ~50ms, ~15 DOM nodes (only visible)
 * → 10x faster, 99% fewer DOM nodes!
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
    // ❌ Blocks UI thread for 5 seconds
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
    // ✅ Non-blocking: UI remains responsive
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
  }
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
    
    // Find by role/label (accessible)
    await user.type(screen.getByLabelText(/email/i), 'user@example.com');
    await user.type(screen.getByLabelText(/password/i), 'password123');
    await user.click(screen.getByRole('button', { name: /login/i }));
    
    // Assert behavior
    await waitFor(() => {
      expect(handleSubmit).toHaveBeenCalledWith({
        email: 'user@example.com',
        password: 'password123'
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

// ❌ Bad: Testing implementation details
it('updates state on input change', () => {
  const { container } = render(<LoginForm />);
  const input = container.querySelector('input[name="email"]');
  
  fireEvent.change(input, { target: { value: 'test@example.com' } });
  
  // Don't test state directly!
  expect(wrapper.state('email')).toBe('test@example.com');
});

// ══════════════════════════════════════════════════════════
// MOCKING API CALLS
// ══════════════════════════════════════════════════════════

import { rest } from 'msw';
import { setupServer } from 'msw/node';

const server = setupServer(
  rest.get('/api/users', (req, res, ctx) => {
    return res(ctx.json([
      { id: 1, name: 'John' },
      { id: 2, name: 'Jane' }
    ]));
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

// ✅ Use for: Static components, complex UI
// ❌ Avoid for: Dynamic content, frequently changing
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
  await page.route('**/api/users', route => {
    route.fulfill({
      status: 500,
      body: JSON.stringify({ error: 'Internal Server Error' })
    });
  });
  
  await page.goto('https://app.example.com/users');
  
  // Assert error message shown
  await expect(page.locator('.error-message')).toHaveText(
    'Failed to load users'
  );
});
```

---

## **XV. Senior Developer Handbook Summary**

### **15.1. Complete Checklist**

```typescript
/**
 * 📋 SENIOR FRONTEND DEVELOPER CHECKLIST
 */

const seniorDevHandbook = {
  
  // ═══════════════════════════════════════════════════════
  // CORE JAVASCRIPT
  // ═══════════════════════════════════════════════════════
  javascript: {
    fundamentals: [
      '✅ Closures, hoisting, scope chain',
      '✅ Prototypes & inheritance',
      '✅ this binding (4 rules)',
      '✅ Event loop (microtasks, macrotasks)',
      '✅ Promises, async/await',
      '✅ ES6+ features (destructuring, spread, optional chaining)'
    ],
    advanced: [
      '✅ Generators & iterators',
      '✅ Proxy & Reflect',
      '✅ WeakMap/WeakSet for memory management',
      '✅ Symbol for private properties',
      '✅ Temporal Dead Zone (TDZ)',
      '✅ Module systems (ESM vs CommonJS)'
    ],
    performance: [
      '✅ O(n²) → O(n) optimizations',
      '✅ Map/Set for lookups',
      '✅ Memoization patterns',
      '✅ Debounce/throttle',
      '✅ Web Workers for heavy tasks'
    ]
  },
  
  // ═══════════════════════════════════════════════════════
  // REACT ECOSYSTEM
  // ═══════════════════════════════════════════════════════
  react: {
    fundamentals: [
      '✅ All hooks (useState, useEffect, useContext, etc.)',
      '✅ Component lifecycle',
      '✅ Virtual DOM & reconciliation',
      '✅ Keys in lists (why not index)'
    ],
    patterns: [
      '✅ Compound Components',
      '✅ Render Props (legacy)',
      '✅ HOC (deprecated → use hooks)',
      '✅ Container/Presentational',
      '✅ Controlled vs Uncontrolled'
    ],
    performance: [
      '✅ React.memo for expensive components',
      '✅ useMemo for expensive calculations',
      '✅ useCallback for stable functions',
      '✅ Code splitting (React.lazy)',
      '✅ Virtual scrolling (react-window)',
      '✅ Avoid inline objects/arrays',
      '✅ Profiler API for bottlenecks'
    ],
    stateManagement: [
      '✅ Context API limitations',
      '✅ Redux (actions, reducers, middleware)',
      '✅ Zustand (simpler alternative)',
      '✅ React Query (server state)',
      '✅ Recoil/Jotai (atomic state)'
    ]
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
      '✅ content-visibility for lazy render'
    ],
    architecture: [
      '✅ BEM methodology',
      '✅ CSS Modules',
      '✅ Styled Components',
      '✅ Tailwind CSS',
      '✅ Critical CSS extraction'
    ],
    performance: [
      '✅ Avoid expensive selectors',
      '✅ CSS containment',
      '✅ will-change for animations',
      '✅ Reduce reflows/repaints'
    ]
  },
  
  // ═══════════════════════════════════════════════════════
  // SECURITY
  // ═══════════════════════════════════════════════════════
  security: {
    xss: [
      '✅ Sanitize user input (DOMPurify)',
      '✅ Use textContent over innerHTML',
      '✅ Content Security Policy (CSP)',
      '✅ Never use eval() or Function()'
    ],
    csrf: [
      '✅ CSRF tokens in forms',
      '✅ SameSite cookies',
      '✅ Custom headers for AJAX'
    ],
    auth: [
      '✅ HttpOnly cookies (not localStorage)',
      '✅ Refresh token pattern',
      '✅ Password validation (length, complexity)',
      '✅ bcrypt with salt >= 12'
    ],
    general: [
      '✅ HTTPS only',
      '✅ Secure headers (HSTS, X-Frame-Options)',
      '✅ Rate limiting',
      '✅ Input validation (client + server)',
      '✅ Dependency audits (npm audit)'
    ]
  },
  
  // ═══════════════════════════════════════════════════════
  // PERFORMANCE
  // ═══════════════════════════════════════════════════════
  performance: {
    metrics: [
      '✅ Core Web Vitals (LCP, FID, CLS)',
      '✅ Lighthouse score > 90',
      '✅ Time to Interactive < 3s',
      '✅ Bundle size < 200KB (gzipped)'
    ],
    optimization: [
      '✅ Code splitting by route',
      '✅ Lazy load images (loading="lazy")',
      '✅ Tree shaking (unused code)',
      '✅ Compression (gzip/brotli)',
      '✅ CDN for static assets',
      '✅ Service Worker for offline'
    ],
    monitoring: [
      '✅ Performance API',
      '✅ Chrome DevTools Profiler',
      '✅ React DevTools Profiler',
      '✅ Sentry for errors',
      '✅ Web Vitals tracking'
    ]
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
      '✅ Code coverage > 80%'
    ],
    integration: [
      '✅ Test user flows',
      '✅ Test error handling',
      '✅ Test edge cases'
    ],
    e2e: [
      '✅ Playwright/Cypress',
      '✅ Critical user paths',
      '✅ Visual regression testing'
    ]
  },
  
  // ═══════════════════════════════════════════════════════
  // BUILD & DEPLOYMENT
  // ═══════════════════════════════════════════════════════
  build: {
    tools: [
      '✅ Vite (fast dev server)',
      '✅ Webpack (production builds)',
      '✅ esbuild (fast bundler)',
      '✅ SWC (Babel alternative)'
    ],
    cicd: [
      '✅ GitHub Actions / GitLab CI',
      '✅ Automated tests',
      '✅ Linting (ESLint, Prettier)',
      '✅ Type checking (TypeScript)',
      '✅ Preview deployments'
    ],
    deployment: [
      '✅ Vercel/Netlify for static',
      '✅ Docker for containers',
      '✅ CloudFront for CDN',
      '✅ Environment variables',
      '✅ Health checks'
    ]
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
    '✅ Estimation & planning'
  ]
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
    'CSS specificity & BEM'
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
    'Testing strategies'
  ],
  
  // Good to know
  bonus: [
    'Generators',
    'Proxy/Reflect',
    'Microfrontends',
    'SSR/SSG',
    'GraphQL',
    'WebAssembly',
    'Progressive Web Apps'
  ]
};

/**
 * 📚 LEARNING PATH
 */
const learningRoadmap = {
  
  month1_3: [
    'Master all React hooks',
    'Build 3 projects with different patterns',
    'Learn testing (RTL + Jest)',
    'Understand bundlers (Vite/Webpack)'
  ],
  
  month4_6: [
    'Deep dive Event Loop',
    'Master performance optimization',
    'Learn security (XSS, CSRF, Auth)',
    'Contribute to open source'
  ],
  
  month7_12: [
    'System design practice',
    'Mentor junior developers',
    'Learn architecture patterns',
    'Build production-grade apps'
  ]
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

// ❌ Old way: Load all images immediately
<img src="heavy-image.jpg" alt="..." />

// ✅ New way: Load when visible
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
    rootMargin: '50px' // Load 50px before visible
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
    navigator.serviceWorker.register('/sw.js')
      .then(registration => {
        console.log('SW registered:', registration.scope);
      })
      .catch(error => {
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
  '/index.html',
  '/styles.css',
  '/app.js',
  '/logo.png'
];

// Install: Cache static assets
self.addEventListener('install', (event: ExtendableEvent) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(STATIC_ASSETS))
  );
});

// Activate: Clean old caches
self.addEventListener('activate', (event: ExtendableEvent) => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames
          .filter(name => name !== CACHE_NAME)
          .map(name => caches.delete(name))
      );
    })
  );
});

// Fetch: Network-first, fallback to cache
self.addEventListener('fetch', (event: FetchEvent) => {
  event.respondWith(
    fetch(event.request)
      .then(response => {
        // Clone and cache successful responses
        if (response.status === 200) {
          const responseClone = response.clone();
          caches.open(CACHE_NAME).then(cache => {
            cache.put(event.request, responseClone);
          });
        }
        return response;
      })
      .catch(() => {
        // Network failed, try cache
        return caches.match(event.request);
      })
  );
});

// ══════════════════════════════════════════════════════════
// OFFLINE FALLBACK PAGE
// ══════════════════════════════════════════════════════════

self.addEventListener('fetch', (event: FetchEvent) => {
  event.respondWith(
    fetch(event.request)
      .catch(() => {
        return caches.match(event.request)
          .then(response => {
            return response || caches.match('/offline.html');
          });
      })
  );
});

// ══════════════════════════════════════════════════════════
// BACKGROUND SYNC
// ══════════════════════════════════════════════════════════

// Register sync when online
navigator.serviceWorker.ready.then(registration => {
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
        body: JSON.stringify(post)
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
      applicationServerKey: urlBase64ToUint8Array(PUBLIC_VAPID_KEY)
    });
    
    // Send subscription to server
    await fetch('/api/subscribe', {
      method: 'POST',
      body: JSON.stringify(subscription),
      headers: { 'Content-Type': 'application/json' }
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
        { action: 'close', title: 'Close' }
      ]
    })
  );
});

// Handle notification click
self.addEventListener('notificationclick', (event: NotificationEvent) => {
  event.notification.close();
  
  if (event.action === 'open') {
    event.waitUntil(
      clients.openWindow('/')
    );
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
        const objectStore = db.createObjectStore('posts', { keyPath: 'id', autoIncrement: true });
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
    items.slice(0, toRemove).forEach(item => {
      this.storage.removeItem(item.key);
    });
  }
}

// Usage
interface AppStorage {
  user: { id: string; name: string; };
  token: string;
  preferences: { theme: 'light' | 'dark'; };
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
  navigator.storage.estimate().then(estimate => {
    console.log(`Using ${estimate.usage} of ${estimate.quota} bytes`);
    console.log(`${((estimate.usage! / estimate.quota!) * 100).toFixed(2)}% used`);
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

// ❌ Problem: Importing entire library
import _ from 'lodash'; // 70KB
import moment from 'moment'; // 230KB

// ✅ Solution 1: Import specific functions
import debounce from 'lodash/debounce'; // 2KB
import format from 'date-fns/format'; // 2KB

// ✅ Solution 2: Use babel-plugin-lodash
// .babelrc
{
  "plugins": ["lodash"]
}

// Now this tree-shakes automatically:
import { debounce, throttle } from 'lodash';

// ══════════════════════════════════════════════════════════
// DYNAMIC IMPORTS
// ══════════════════════════════════════════════════════════

// ❌ Static import (always loaded)
import Chart from 'chart.js';

// ✅ Dynamic import (loaded when needed)
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

/**
 * Before optimization: 1 file (500KB)
 * After optimization:
 * • main.js: 50KB
 * • react.js: 120KB (cached)
 * • vendors.js: 200KB (cached)
 * • common.js: 30KB (cached)
 * 
 * Total: 400KB (20% smaller)
 * Subsequent loads: 50KB only! (90% cached)
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
      tracingOrigins: ['localhost', 'https://api.example.com']
    })
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
  }
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
  username: user.username
});

// Add breadcrumbs
Sentry.addBreadcrumb({
  category: 'api',
  message: 'Fetched user data',
  level: 'info',
  data: { userId: '123' }
});

// Capture custom errors
try {
  riskyOperation();
} catch (error) {
  Sentry.captureException(error, {
    tags: {
      section: 'payment'
    },
    extra: {
      paymentAmount: 100,
      currency: 'USD'
    }
  });
}

// Performance monitoring
const transaction = Sentry.startTransaction({
  name: 'CheckoutFlow',
  op: 'user-flow'
});

const span = transaction.startChild({
  op: 'payment',
  description: 'Process payment'
});

await processPayment();

span.finish();
transaction.finish();

// ══════════════════════════════════════════════════════════
// AXIOS INTERCEPTOR FOR API ERRORS
// ══════════════════════════════════════════════════════════

axios.interceptors.response.use(
  response => response,
  error => {
    Sentry.captureException(error, {
      tags: {
        type: 'api-error',
        endpoint: error.config?.url
      },
      extra: {
        status: error.response?.status,
        data: error.response?.data
      }
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
      navigationType: metric.navigationType
    })
  });
  
  // Also log to console in dev
  console.log(metric.name, metric.value);
}

// Track Core Web Vitals
onCLS(sendToAnalytics);  // Cumulative Layout Shift
onFID(sendToAnalytics);  // First Input Delay
onLCP(sendToAnalytics);  // Largest Contentful Paint
onFCP(sendToAnalytics);  // First Contentful Paint
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
measures.forEach(measure => {
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
    baseDuration,   // Estimated time without memoization
    startTime,
    commitTime
  });
  
  // Send to analytics if slow
  if (actualDuration > 16) { // > 1 frame (60fps)
    sendToAnalytics({
      type: 'slow-render',
      component: id,
      duration: actualDuration
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
      startTime: entry.startTime
    });
    
    // Send to analytics
    if (entry.duration > 50) { // > 50ms blocks UI
      sendToAnalytics({
        type: 'long-task',
        duration: entry.duration
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
  
  if (duration > 1000) { // > 1 second
    console.warn('Slow resource:', {
      name: resource.name,
      duration,
      size: resource.transferSize,
      type: resource.initiatorType
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
          duration
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
