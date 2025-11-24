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
