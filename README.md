# Câu Hỏi Frontend  - Từ Cơ Bản Đến Senior

## Mục Lục
1. [Câu Hỏi Cơ Bản (Junior Level)](#câu-hỏi-cơ-bản-junior-level)
2. [Câu Hỏi Trung Cấp (Mid-Level)](#câu-hỏi-trung-cấp-mid-level)
3. [Câu Hỏi Nâng Cao (Senior Level)](#câu-hỏi-nâng-cao-senior-level)
4. [Performance Optimization](#performance-optimization)
5. [Security Best Practices](#security-best-practices)

---

## Câu Hỏi Cơ Bản (Junior Level)

### 1. JavaScript Core Fundamentals

#### Q1: Primitive Values vs Reference Values trong JavaScript?

**Trả lời:**

**Giải thích:**
- **Primitive Values (Kiểu nguyên thủy)**: Lưu trữ theo giá trị, không thể thay đổi (immutable)
- **Reference Values (Kiểu tham chiếu)**: Lưu trữ theo địa chỉ bộ nhớ, có thể thay đổi (mutable)

```typescript
// 1. Primitive Values (Kiểu nguyên thủy)
// Bao gồm: number, string, boolean, null, undefined, symbol, bigint
let a: number = 5;
let b: number = a; // Sao chép giá trị (không phải tham chiếu)
a = 10;
console.log(a, b); // 10, 5 - b không bị ảnh hưởng

let str1: string = "hello";
let str2: string = str1; // Sao chép giá trị
str1 = "world";
console.log(str1, str2); // "world", "hello" - str2 không đổi

// 2. Reference Values (Kiểu tham chiếu)
// Bao gồm: object, array, function, Date, RegExp...
interface User {
  name: string;
  age?: number;
}

let obj1: User = { name: "John" };
let obj2: User = obj1; // Sao chép tham chiếu (không phải giá trị)
obj1.name = "Jane";
console.log(obj1.name, obj2.name); // "Jane", "Jane" - cả 2 đều thay đổi

let arr1: number[] = [1, 2, 3];
let arr2: number[] = arr1; // Sao chép tham chiếu
arr1.push(4);
console.log(arr1, arr2); // [1,2,3,4], [1,2,3,4] - cả 2 đều thay đổi

// 3. Shallow Copy vs Deep Copy
// Shallow Copy (Sao chép nông) - chỉ sao chép cấp đầu tiên
interface Address {
  street: string;
  city: string;
}

interface UserProfile {
  name: string;
  address: Address;
  hobbies: string[];
}

const original: UserProfile = {
  name: "John",
  address: {
    street: "123 Main St",
    city: "NYC"
  },
  hobbies: ["reading", "coding"]
};

// Các cách Shallow Copy
const shallowCopy1: UserProfile = { ...original }; // Spread operator
const shallowCopy2: UserProfile = Object.assign({}, original);

shallowCopy1.name = "Jane"; // ✅ OK - không ảnh hưởng original
shallowCopy1.address.city = "LA"; // ❌ Vấn đề - ảnh hưởng original
console.log(original.address.city); // "LA" - đã bị thay đổi vì address là reference

// Deep Copy methods (Sao chép sâu)
// Method 1: JSON (hạn chế - không hoạt động với functions, dates, undefined...)
const deepCopy1: UserProfile = JSON.parse(JSON.stringify(original));

// Method 2: Custom recursive function
function deepCopy<T>(obj: T): T {
  if (obj === null || typeof obj !== "object") return obj;

  if (obj instanceof Date) return new Date(obj.getTime());
  if (obj instanceof Array) return obj.map(item => deepCopy(item));

  if (typeof obj === "object") {
    const copy = {};
    Object.keys(obj).forEach(key => {
      copy[key] = deepCopy(obj[key]);
    });
    return copy;
  }
}

const deepCopy2 = deepCopy(original);

// Method 3: Using Lodash
// const deepCopy3 = _.cloneDeep(original);

// Method 4: Using structuredClone (modern browsers)
const deepCopy4 = structuredClone(original);

// Test deep copy
deepCopy2.address.city = "Chicago";
console.log(original.address.city); // "NYC" - không bị ảnh hưởng

// 4. Spread Operator (...) Use Cases
// Array spreading
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const combined = [...arr1, ...arr2]; // [1,2,3,4,5,6]

// Object spreading
const obj1 = { a: 1, b: 2 };
const obj2 = { c: 3, d: 4 };
const combined = { ...obj1, ...obj2 }; // {a:1, b:2, c:3, d:4}

// Function arguments
function sum(a, b, c) {
  return a + b + c;
}
const numbers = [1, 2, 3];
console.log(sum(...numbers)); // 6

// Copying arrays/objects (shallow)
const originalArray = [1, 2, 3];
const copiedArray = [...originalArray];

// Rest parameters
function collectArgs(first, ...rest) {
  console.log(first); // 1
  console.log(rest);  // [2, 3, 4, 5]
}
collectArgs(1, 2, 3, 4, 5);

// Destructuring with rest
const [first, second, ...others] = [1, 2, 3, 4, 5];
console.log(others); // [3, 4, 5]

const { name, ...restProps } = { name: "John", age: 30, city: "NYC" };
console.log(restProps); // { age: 30, city: "NYC" }
```

#### Q2: Sự khác biệt giữa `var`, `let`, và `const`?

**Trả lời:**
- **`var`**: Function-scoped, có hoisting, có thể redeclare
- **`let`**: Block-scoped, có hoisting nhưng temporal dead zone, không thể redeclare
- **`const`**: Block-scoped, phải khởi tạo giá trị, không thể reassign

```javascript
// var example
function varExample() {
  console.log(x); // undefined (hoisted)
  var x = 1;
  if (true) {
    var x = 2; // same variable
  }
  console.log(x); // 2
}

// let example
function letExample() {
  // console.log(y); // ReferenceError: Cannot access 'y' before initialization
  let y = 1;
  if (true) {
    let y = 2; // different variable
    console.log(y); // 2
  }
  console.log(y); // 1
}

// const example
function constExample() {
  const z = { name: 'John' };
  // z = {}; // TypeError: Assignment to constant variable
  z.name = 'Jane'; // OK - object mutation allowed
  console.log(z); // { name: 'Jane' }
}
```

#### Q3: ES5 vs ES6+ features và modern JavaScript?

**Trả lời:**

```javascript
// ES5 Features (2009)
// 1. Array methods
var numbers = [1, 2, 3, 4, 5];
var doubled = numbers.map(function(n) { return n * 2; });
var evens = numbers.filter(function(n) { return n % 2 === 0; });
var sum = numbers.reduce(function(acc, n) { return acc + n; }, 0);

// 2. Object methods
var obj = { name: 'John', age: 30 };
var keys = Object.keys(obj);
var hasName = obj.hasOwnProperty('name');

// 3. Function bind
function greet() {
  console.log('Hello ' + this.name);
}
var boundGreet = greet.bind({ name: 'John' });

// ES6+ Features (2015+)
// 1. Let/Const và Block Scope
let x = 10;
const y = 20;

if (true) {
  let x = 30; // Different variable
  console.log(x); // 30
}
console.log(x); // 10

// 2. Arrow Functions
const add = (a, b) => a + b;
const square = x => x * x;
const greet = name => {
  console.log(`Hello ${name}`);
};

// 3. Template Literals
const name = 'John';
const message = `Hello ${name}, today is ${new Date().toDateString()}`;

// 4. Destructuring
const person = { name: 'John', age: 30, city: 'NYC' };
const { name, age } = person;
const { name: personName, age: personAge } = person; // Renaming

const numbers = [1, 2, 3, 4, 5];
const [first, second, ...rest] = numbers;

// 5. Default Parameters
function greet(name = 'Guest', greeting = 'Hello') {
  console.log(`${greeting}, ${name}!`);
}

// 6. Rest/Spread Operators
function sum(...numbers) {
  return numbers.reduce((a, b) => a + b, 0);
}

const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5]; // [1, 2, 3, 4, 5]

// 7. Enhanced Object Literals
const name = 'John';
const age = 30;

const person = {
  name, // Shorthand property
  age,
  greet() { // Method shorthand
    console.log(`Hello, I'm ${this.name}`);
  },
  [`dynamic_${age}`]: 'value' // Computed property names
};

// 8. Classes
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log(`Hello, I'm ${this.name}`);
  }

  static createAdult(name) {
    return new Person(name, 18);
  }
}

class Employee extends Person {
  constructor(name, age, position) {
    super(name, age);
    this.position = position;
  }

  work() {
    console.log(`${this.name} is working as ${this.position}`);
  }
}

// 9. Modules (ES6)
// export const PI = 3.14159;
// export default function calculate() {}
// import calculate, { PI } from './math.js';

// 10. Set và Map
const uniqueNumbers = new Set([1, 2, 2, 3, 3, 4]); // {1, 2, 3, 4}
uniqueNumbers.add(5);
uniqueNumbers.has(3); // true
uniqueNumbers.delete(2);

const userRoles = new Map();
userRoles.set('john', 'admin');
userRoles.set('jane', 'user');
userRoles.get('john'); // 'admin'
userRoles.has('jane'); // true

// 11. WeakSet và WeakMap (garbage collection friendly)
const weakSet = new WeakSet();
const obj1 = {};
const obj2 = {};
weakSet.add(obj1);
weakSet.add(obj2);
// Tự động remove khi objects bị garbage collected

const weakMap = new WeakMap();
const element = document.getElementById('myElement');
weakMap.set(element, { clickCount: 0 });
// Tự động cleanup khi element bị removed

// ES7+ Features
// 12. Async/Await (ES2017)
async function fetchUserData(userId) {
  try {
    const response = await fetch(`/api/users/${userId}`);
    const user = await response.json();
    return user;
  } catch (error) {
    console.error('Failed to fetch user:', error);
    throw error;
  }
}

// 13. Optional Chaining (ES2020)
const user = {
  profile: {
    social: {
      twitter: '@john'
    }
  }
};

const twitter = user?.profile?.social?.twitter; // Safe access
const followers = user?.profile?.social?.followers?.count; // undefined, no error

// 14. Nullish Coalescing (ES2020)
const username = user.name ?? 'Guest'; // Only null/undefined, not falsy
const port = process.env.PORT ?? 3000;

// 15. Private Class Fields (ES2022)
class Counter {
  #count = 0; // Private field

  increment() {
    this.#count++;
  }

  getCount() {
    return this.#count;
  }
}

const counter = new Counter();
// counter.#count; // SyntaxError - cannot access private field
```

#### Q4: Hoisting trong JavaScript - Cách hoạt động?

**Trả lời:**

```javascript
// 1. Variable Hoisting
console.log(x); // undefined (not ReferenceError)
var x = 5;

// Equivalent to:
var x; // hoisted to top, initialized with undefined
console.log(x); // undefined
x = 5;

// Let/Const Hoisting - Temporal Dead Zone
console.log(y); // ReferenceError: Cannot access 'y' before initialization
let y = 10;

console.log(z); // ReferenceError: Cannot access 'z' before initialization
const z = 20;

// 2. Function Hoisting
// Function declarations are fully hoisted
sayHello(); // "Hello!" - works!

function sayHello() {
  console.log("Hello!");
}

// Function expressions are NOT hoisted
sayGoodbye(); // TypeError: sayGoodbye is not a function

var sayGoodbye = function() {
  console.log("Goodbye!");
};

// 3. Class Hoisting - Temporal Dead Zone
const instance = new MyClass(); // ReferenceError

class MyClass {
  constructor() {
    this.name = 'MyClass';
  }
}

// 4. Advanced Hoisting Examples
function example() {
  console.log(typeof foo); // "function" - function hoisted
  console.log(typeof bar); // "undefined" - var hoisted, not assignment
  console.log(typeof baz); // ReferenceError - let in TDZ

  function foo() {
    return 'foo';
  }

  var bar = function() {
    return 'bar';
  };

  let baz = function() {
    return 'baz';
  };
}

// 5. Hoisting with Same Name
var myFunc = function() {
  console.log('Expression');
};

function myFunc() {
  console.log('Declaration');
}

myFunc(); // "Expression" - function expression overwrites declaration
```

#### Q5: Event Loop hoạt động như thế nào? (Giải thích đơn giản)

**Trả lời:**
Tưởng tượng Event Loop như một nhân viên văn phòng rất có tổ chức:

```javascript
// Event Loop giống như một nhân viên có 3 cái hộp:
// 1. Call Stack (ngăn xếp công việc) - làm ngay lập tức
// 2. Callback Queue (hàng đợi callback) - làm sau
// 3. Microtask Queue (hàng đợi ưu tiên) - làm trước callback

console.log('1. Bắt đầu'); // Call Stack - làm ngay

setTimeout(() => {
  console.log('3. Timeout'); // Callback Queue - đợi
}, 0);

Promise.resolve().then(() => {
  console.log('2. Promise'); // Microtask Queue - ưu tiên cao
});

console.log('1. Kết thúc'); // Call Stack - làm ngay

// Output: "1. Bắt đầu" → "1. Kết thúc" → "2. Promise" → "3. Timeout"

// Quy trình làm việc của Event Loop:
// 1. Làm hết việc trong Call Stack trước
// 2. Kiểm tra Microtask Queue, làm hết
// 3. Mới đến Callback Queue
// 4. Lặp lại

// Ví dụ phức tạp hơn:
console.log('Start');

setTimeout(() => console.log('Timeout 1'), 0);

Promise.resolve()
  .then(() => {
    console.log('Promise 1');
    return Promise.resolve();
  })
  .then(() => console.log('Promise 2'));

setTimeout(() => console.log('Timeout 2'), 0);

console.log('End');

// Output:
// "Start"
// "End"
// "Promise 1"
// "Promise 2"
// "Timeout 1"
// "Timeout 2"

// Web APIs trong Browser:
// - setTimeout/setInterval → Callback Queue
// - DOM Events → Callback Queue
// - Promise.then/catch/finally → Microtask Queue
// - async/await → Microtask Queue
// - queueMicrotask() → Microtask Queue

// Thực tế hoạt động:
function demonstrateEventLoop() {
  console.log('🏁 Start');

  // Callback Queue
  setTimeout(() => console.log('⏰ Timer'), 0);

  // Microtask Queue
  Promise.resolve().then(() => console.log('✅ Promise'));

  // Call Stack
  console.log('🏁 Sync code');

  // Microtask Queue
  queueMicrotask(() => console.log('⚡ Microtask'));
}

demonstrateEventLoop();
// Output:
// 🏁 Start
// 🏁 Sync code
// ✅ Promise
// ⚡ Microtask
// ⏰ Timer
```

#### Q6: Closure và Data Privacy trong JavaScript?

**Trả lời:**

```javascript
// 1. Closure cơ bản - Data Privacy
function createCounter() {
  let count = 0; // Private variable

  return {
    increment() {
      count++;
      return count;
    },
    decrement() {
      count--;
      return count;
    },
    getCount() {
      return count;
    }
    // count không thể access trực tiếp từ bên ngoài
  };
}

const counter = createCounter();
console.log(counter.increment()); // 1
console.log(counter.increment()); // 2
console.log(counter.getCount()); // 2
// console.log(counter.count); // undefined - private!

// 2. Module Pattern với IIFE
const CalculatorModule = (function() {
  let result = 0; // Private state

  function add(x) {
    result += x;
    return this;
  }

  function multiply(x) {
    result *= x;
    return this;
  }

  function getResult() {
    return result;
  }

  function reset() {
    result = 0;
    return this;
  }

  // Public API
  return {
    add,
    multiply,
    getResult,
    reset
  };
})();

CalculatorModule.add(5).multiply(2).add(3);
console.log(CalculatorModule.getResult()); // 13

// 3. Factory Functions với Closure
function createUser(name, email) {
  let isActive = true; // Private
  let loginAttempts = 0; // Private

  return {
    getName() {
      return name;
    },
    getEmail() {
      return email;
    },
    login(password) {
      if (loginAttempts >= 3) {
        isActive = false;
        throw new Error('Account locked');
      }

      if (password === 'correct') {
        loginAttempts = 0;
        return 'Login successful';
      } else {
        loginAttempts++;
        throw new Error('Invalid password');
      }
    },
    isAccountActive() {
      return isActive;
    }
  };
}

const user = createUser('John', 'john@email.com');
console.log(user.getName()); // 'John'
// console.log(user.isActive); // undefined - private!

// 4. Currying với Closure
function createMultiplier(multiplier) {
  return function(number) {
    return number * multiplier;
  };
}

const double = createMultiplier(2);
const triple = createMultiplier(3);

console.log(double(5)); // 10
console.log(triple(5)); // 15

// Advanced Currying
function curry(fn) {
  return function curried(...args) {
    if (args.length >= fn.length) {
      return fn.apply(this, args);
    } else {
      return function(...nextArgs) {
        return curried(...args, ...nextArgs);
      };
    }
  };
}

function add(a, b, c) {
  return a + b + c;
}

const curriedAdd = curry(add);
console.log(curriedAdd(1)(2)(3)); // 6
console.log(curriedAdd(1, 2)(3)); // 6
console.log(curriedAdd(1)(2, 3)); // 6

// 5. Event Handlers với Closure
function setupEventListeners() {
  const buttons = document.querySelectorAll('button');

  buttons.forEach((button, index) => {
    button.addEventListener('click', function() {
      // Closure captures 'index' and 'button'
      console.log(`Button ${index} clicked`);
    });
  });
}

// 6. Memoization với Closure
function memoize(fn) {
  const cache = new Map();

  return function(...args) {
    const key = JSON.stringify(args);

    if (cache.has(key)) {
      console.log('Cache hit!');
      return cache.get(key);
    }

    console.log('Computing...');
    const result = fn.apply(this, args);
    cache.set(key, result);
    return result;
  };
}

const expensiveOperation = memoize(function(n) {
  let result = 0;
  for (let i = 0; i < n; i++) {
    result += i;
  }
  return result;
});

console.log(expensiveOperation(1000)); // Computing... result
console.log(expensiveOperation(1000)); // Cache hit! result
```

#### Q7: DOM và Event Handling chi tiết?

**Trả lời:**

```javascript
// 1. Event Bubbling vs Event Capturing
/*
Event flow: Capturing → Target → Bubbling
         window
           ↓
        document
           ↓
         <html>
           ↓
         <body>
           ↓
        <div>      ← Event Capturing (từ trên xuống)
           ↓
       <button>    ← Target Element
           ↑
        <div>      ← Event Bubbling (từ dưới lên)
*/

// HTML:
// <div id="parent">
//   <button id="child">Click me</button>
// </div>

const parent = document.getElementById('parent');
const child = document.getElementById('child');

// Event Bubbling (default)
parent.addEventListener('click', () => {
  console.log('Parent clicked (bubbling)');
});

child.addEventListener('click', () => {
  console.log('Child clicked');
});

// Event Capturing
parent.addEventListener('click', () => {
  console.log('Parent clicked (capturing)');
}, true); // true = capturing phase

// Click child button → Output:
// "Parent clicked (capturing)"
// "Child clicked"
// "Parent clicked (bubbling)"

// 2. stopPropagation vs preventDefault
child.addEventListener('click', (event) => {
  event.stopPropagation(); // Stops event bubbling
  console.log('Child clicked - no bubbling');
});

// preventDefault - ngăn default behavior
const link = document.querySelector('a');
link.addEventListener('click', (event) => {
  event.preventDefault(); // Ngăn navigation
  console.log('Link clicked but no navigation');
});

const form = document.querySelector('form');
form.addEventListener('submit', (event) => {
  event.preventDefault(); // Ngăn form submission
  console.log('Form submitted via AJAX instead');
});

// 3. event.target vs event.currentTarget
const container = document.getElementById('container');

container.addEventListener('click', (event) => {
  console.log('target:', event.target.tagName); // Element được click
  console.log('currentTarget:', event.currentTarget.tagName); // Element có event listener
});

// Click <span> inside <div> container:
// target: SPAN (element actually clicked)
// currentTarget: DIV (element with listener)

// 4. Event Delegation
const todoList = document.getElementById('todoList');

// Thay vì add listener cho mỗi item
todoList.addEventListener('click', (event) => {
  if (event.target.classList.contains('delete-btn')) {
    // Handle delete
    event.target.closest('li').remove();
  } else if (event.target.classList.contains('edit-btn')) {
    // Handle edit
    const todoItem = event.target.closest('li');
    enableEdit(todoItem);
  }
});

// Advantages:
// - Performance: 1 listener instead of many
// - Dynamic content: works for newly added items
// - Memory efficient

// 5. DOM Query Methods
// Single element
const element = document.getElementById('myId');
const element2 = document.querySelector('.my-class');
const element3 = document.querySelector('div[data-id="123"]');

// Multiple elements
const elements = document.getElementsByClassName('my-class');
const elements2 = document.getElementsByTagName('div');
const elements3 = document.querySelectorAll('.my-class');

// Modern approach - querySelectorAll
const buttons = document.querySelectorAll('button[data-action]');
buttons.forEach(button => {
  const action = button.dataset.action;
  button.addEventListener('click', () => handleAction(action));
});

// 6. DOM Manipulation
// Creating elements
const newDiv = document.createElement('div');
newDiv.className = 'new-item';
newDiv.textContent = 'Hello World';
newDiv.setAttribute('data-id', '123');

// Adding elements
const parent = document.getElementById('parent');
parent.appendChild(newDiv);
parent.insertBefore(newDiv, parent.firstChild);

// Modern approach
parent.insertAdjacentHTML('beforeend', '<div>New content</div>');
parent.insertAdjacentElement('afterbegin', newDiv);

// Removing elements
element.remove(); // Modern
parent.removeChild(element); // Legacy

// 7. Event Performance Optimization
// Debouncing search input
function debounce(func, delay) {
  let timeoutId;
  return function(...args) {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => func.apply(this, args), delay);
  };
}

const searchInput = document.getElementById('search');
const debouncedSearch = debounce((event) => {
  console.log('Searching for:', event.target.value);
  // Perform search API call
}, 300);

searchInput.addEventListener('input', debouncedSearch);

// Throttling scroll events
function throttle(func, delay) {
  let inThrottle;
  return function(...args) {
    if (!inThrottle) {
      func.apply(this, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, delay);
    }
  };
}

const throttledScroll = throttle(() => {
  console.log('Scroll position:', window.scrollY);
}, 100);

window.addEventListener('scroll', throttledScroll);

// 8. Custom Events
// Creating custom events
const customEvent = new CustomEvent('userLogin', {
  detail: {
    userId: 123,
    username: 'john'
  },
  bubbles: true
});

// Listening for custom events
document.addEventListener('userLogin', (event) => {
  console.log('User logged in:', event.detail);
});

// Dispatching custom events
document.dispatchEvent(customEvent);

// Real-world example: Component communication
class TodoComponent {
  constructor(element) {
    this.element = element;
    this.setupEvents();
  }

  setupEvents() {
    this.element.addEventListener('click', (e) => {
      if (e.target.classList.contains('complete-btn')) {
        this.completeTodo(e.target.closest('[data-todo-id]'));
      }
    });
  }

  completeTodo(todoElement) {
    const todoId = todoElement.dataset.todoId;

    // Update UI
    todoElement.classList.add('completed');

    // Emit custom event
    const event = new CustomEvent('todoCompleted', {
      detail: { todoId },
      bubbles: true
    });

    this.element.dispatchEvent(event);
  }
}

// Listen for todo completion
document.addEventListener('todoCompleted', (event) => {
  console.log(`Todo ${event.detail.todoId} completed`);
  updateStats();
});
```

#### Q8: Falsy/Truthy, == vs ===, null vs undefined?

**Trả lời:**

```javascript
// 1. Falsy Values - chỉ có 8 giá trị falsy
const falsyValues = [
  false,        // Boolean false
  0,           // Number zero
  -0,          // Negative zero
  0n,          // BigInt zero
  "",          // Empty string
  null,        // null
  undefined,   // undefined
  NaN          // Not a Number
];

// Tất cả các giá trị khác đều là truthy
const truthyValues = [
  true,
  1,
  -1,
  "0",         // String "0" is truthy!
  "false",     // String "false" is truthy!
  [],          // Empty array is truthy!
  {},          // Empty object is truthy!
  function(){} // Functions are truthy
];

// 2. == vs === (Type Coercion)
// === (Strict equality) - không convert type
console.log(5 === "5");        // false
console.log(true === 1);       // false
console.log(null === undefined); // false

// == (Loose equality) - có type conversion
console.log(5 == "5");         // true (string "5" → number 5)
console.log(true == 1);        // true (boolean true → number 1)
console.log(false == 0);       // true (boolean false → number 0)
console.log(null == undefined); // true (special case)

// Weird cases với ==
console.log("" == 0);          // true
console.log("" == false);      // true
console.log(" " == 0);         // true
console.log("0" == false);     // true
console.log([] == 0);          // true
console.log([] == false);      // true
console.log([1] == 1);         // true
console.log([1, 2] == "1,2");  // true

// Recommendation: Always use ===
// Exception: checking for null/undefined
if (value == null) {
  // This checks for both null AND undefined
}
// Equivalent to:
if (value === null || value === undefined) {
  // More explicit
}

// 3. null vs undefined
let declaredButNotAssigned; // undefined
let explicitlyNull = null;   // null

console.log(typeof undefined); // "undefined"
console.log(typeof null);      // "object" (famous JS bug)

// When you get undefined:
console.log(obj.nonExistentProperty); // undefined
console.log(arr[999]);                // undefined
function noReturn() {}
console.log(noReturn());              // undefined

// When you get null:
document.getElementById('nonExistent'); // null
JSON.parse('{"key": null}').key;       // null
/regex/.exec('no match');              // null

// Best practices:
// - Use undefined for "not set" or "not initialized"
// - Use null for "intentionally empty" or "no value"

// 4. Optional Chaining với nullish values
const user = {
  profile: null
};

// Old way
const city = user && user.profile && user.profile.address && user.profile.address.city;

// New way - Optional Chaining
const city2 = user?.profile?.address?.city; // undefined

// With arrays
const firstHobby = user?.hobbies?.[0];

// With functions
const result = user?.calculateSomething?.();

// 5. Nullish Coalescing (??) vs OR (||)
const value1 = null ?? "default";     // "default"
const value2 = undefined ?? "default"; // "default"
const value3 = 0 ?? "default";        // 0 (not "default"!)
const value4 = "" ?? "default";       // "" (not "default"!)
const value5 = false ?? "default";    // false (not "default"!)

// Compare with OR operator
const value6 = null || "default";     // "default"
const value7 = undefined || "default"; // "default"
const value8 = 0 || "default";        // "default" (different!)
const value9 = "" || "default";       // "default" (different!)
const value10 = false || "default";   // "default" (different!)

// Use cases:
// ?? when you want to handle only null/undefined
const port = process.env.PORT ?? 3000; // 0 is valid port

// || when you want to handle all falsy values
const username = user.name || "Guest"; // empty string should become "Guest"

// 6. typeof operator detailed
console.log(typeof 42);           // "number"
console.log(typeof "hello");      // "string"
console.log(typeof true);         // "boolean"
console.log(typeof undefined);    // "undefined"
console.log(typeof null);         // "object" (bug!)
console.log(typeof {});           // "object"
console.log(typeof []);           // "object" (arrays are objects)
console.log(typeof function(){}); // "function"
console.log(typeof Symbol());     // "symbol"
console.log(typeof 123n);         // "bigint"

// Better type checking
function getType(value) {
  if (value === null) return 'null';
  if (Array.isArray(value)) return 'array';
  return typeof value;
}

console.log(getType(null));    // "null"
console.log(getType([]));      // "array"
console.log(getType({}));      // "object"

// Advanced type checking
function isObject(value) {
  return value !== null && typeof value === 'object' && !Array.isArray(value);
}

function isPrimitive(value) {
  return value == null || /^[sbn]/.test(typeof value);
  // s: string, b: boolean, n: number
}
```

#### Q10: Arrow Functions vs Regular Functions và `this` binding?

**Trả lời:**

```javascript
// 1. Regular Functions vs Arrow Functions
// Regular function
function regularFunction() {
  console.log('Regular function');
  console.log(this); // Dynamic this binding
}

// Arrow function
const arrowFunction = () => {
  console.log('Arrow function');
  console.log(this); // Lexical this binding
};

// 2. `this` binding differences
const obj = {
  name: 'Object',

  // Regular method
  regularMethod: function() {
    console.log(this.name); // "Object"

    // Nested regular function
    function nested() {
      console.log(this.name); // undefined (this = window/global)
    }
    nested();

    // Nested arrow function
    const nestedArrow = () => {
      console.log(this.name); // "Object" (inherits parent this)
    };
    nestedArrow();
  },

  // Arrow method (not recommended)
  arrowMethod: () => {
    console.log(this.name); // undefined (this = window/global)
  }
};

obj.regularMethod();
obj.arrowMethod();

// 3. call, apply, bind
function greet(greeting, punctuation) {
  return `${greeting} ${this.name}${punctuation}`;
}

const person = { name: 'John' };

// call - arguments individually
console.log(greet.call(person, 'Hello', '!')); // "Hello John!"

// apply - arguments as array
console.log(greet.apply(person, ['Hi', '.'])); // "Hi John."

// bind - creates new function with bound this
const boundGreet = greet.bind(person);
console.log(boundGreet('Hey', '?')); // "Hey John?"

// Partial application with bind
const sayHello = greet.bind(person, 'Hello');
console.log(sayHello('!')); // "Hello John!"

// 4. Real-world examples
class EventHandler {
  constructor(name) {
    this.name = name;
    this.count = 0;
  }

  // Problem with regular function
  setupRegularHandler() {
    document.getElementById('btn1').addEventListener('click', function() {
      this.count++; // Error: this is undefined
      console.log(`${this.name} clicked ${this.count} times`);
    });
  }

  // Solution 1: Arrow function
  setupArrowHandler() {
    document.getElementById('btn2').addEventListener('click', () => {
      this.count++; // Works: this refers to EventHandler instance
      console.log(`${this.name} clicked ${this.count} times`);
    });
  }

  // Solution 2: bind
  setupBoundHandler() {
    const handler = function() {
      this.count++;
      console.log(`${this.name} clicked ${this.count} times`);
    }.bind(this);

    document.getElementById('btn3').addEventListener('click', handler);
  }

  // Solution 3: Store reference
  setupReferenceHandler() {
    const self = this;
    document.getElementById('btn4').addEventListener('click', function() {
      self.count++;
      console.log(`${self.name} clicked ${self.count} times`);
    });
  }
}

// 5. React examples
class ReactComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };

    // Method needs binding
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    this.setState({ count: this.state.count + 1 });
  }

  // Arrow function method (automatically bound)
  handleClickArrow = () => {
    this.setState({ count: this.state.count + 1 });
  };

  render() {
    return (
      <div>
        {/* Need to bind in JSX */}
        <button onClick={this.handleClick.bind(this)}>Click 1</button>

        {/* Or use arrow function in JSX (creates new function each render) */}
        <button onClick={() => this.handleClick()}>Click 2</button>

        {/* Pre-bound method */}
        <button onClick={this.handleClick}>Click 3</button>

        {/* Arrow function method */}
        <button onClick={this.handleClickArrow}>Click 4</button>
      </div>
    );
  }
}

// 6. Advanced this binding
function Calculator() {
  this.result = 0;

  return {
    add: function(n) {
      this.result += n;
      return this;
    },

    multiply: function(n) {
      this.result *= n;
      return this;
    },

    getResult: function() {
      return this.result;
    }
  };
}

const calc = new Calculator();
// Method chaining works because 'this' refers to returned object
console.log(calc.add(5).multiply(2).getResult()); // 10

// 7. Arrow functions limitations
// Cannot be constructor
const ArrowConstructor = () => {};
// new ArrowConstructor(); // TypeError

// No arguments object
function regularFunc() {
  console.log(arguments); // [1, 2, 3]
}

const arrowFunc = (...args) => {
  console.log(args); // Use rest parameters instead
};

regularFunc(1, 2, 3);
arrowFunc(1, 2, 3);

// 8. Best practices
// Use arrow functions for:
// - Callbacks and higher-order functions
// - Lexical this binding needed
const numbers = [1, 2, 3];
const doubled = numbers.map(n => n * 2); // Arrow function appropriate

// Use regular functions for:
// - Object methods
// - Constructor functions
// - When you need dynamic this
const object = {
  value: 42,
  getValue: function() { // Regular function appropriate
    return this.value;
  }
};
```

#### Q11: Async/Await vs Promises vs Callbacks?

**Trả lời:**

```javascript
// 1. Callbacks (Old way)
function fetchUserCallback(id, callback) {
  setTimeout(() => {
    if (id > 0) {
      callback(null, { id, name: `User ${id}` });
    } else {
      callback(new Error('Invalid ID'));
    }
  }, 1000);
}

// Callback hell
fetchUserCallback(1, (err, user) => {
  if (err) {
    console.error(err);
    return;
  }

  fetchUserPosts(user.id, (err, posts) => {
    if (err) {
      console.error(err);
      return;
    }

    fetchPostComments(posts[0].id, (err, comments) => {
      if (err) {
        console.error(err);
        return;
      }

      console.log('Finally got comments:', comments);
    });
  });
});

// 2. Promises (Better)
function fetchUserPromise(id) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (id > 0) {
        resolve({ id, name: `User ${id}` });
      } else {
        reject(new Error('Invalid ID'));
      }
    }, 1000);
  });
}

function fetchUserPosts(userId) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve([{ id: 1, title: 'Post 1', userId }]);
    }, 1000);
  });
}

function fetchPostComments(postId) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve([{ id: 1, text: 'Comment 1', postId }]);
    }, 1000);
  });
}

// Promise chaining
fetchUserPromise(1)
  .then(user => {
    console.log('User:', user);
    return fetchUserPosts(user.id);
  })
  .then(posts => {
    console.log('Posts:', posts);
    return fetchPostComments(posts[0].id);
  })
  .then(comments => {
    console.log('Comments:', comments);
  })
  .catch(error => {
    console.error('Error:', error);
  });

// 3. Async/Await (Best)
async function fetchUserData(id) {
  try {
    const user = await fetchUserPromise(id);
    console.log('User:', user);

    const posts = await fetchUserPosts(user.id);
    console.log('Posts:', posts);

    const comments = await fetchPostComments(posts[0].id);
    console.log('Comments:', comments);

    return { user, posts, comments };
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
}

// Usage
fetchUserData(1)
  .then(data => console.log('All data:', data))
  .catch(error => console.error('Failed:', error));

// 4. Promise.all - Parallel execution
async function fetchMultipleUsers(ids) {
  try {
    // All requests happen in parallel
    const users = await Promise.all(
      ids.map(id => fetchUserPromise(id))
    );

    console.log('All users:', users);
    return users;
  } catch (error) {
    // If any fails, all fail
    console.error('One user fetch failed:', error);
  }
}

fetchMultipleUsers([1, 2, 3]);

// 5. Promise.allSettled - Don't fail fast
async function fetchMultipleUsersSettled(ids) {
  const results = await Promise.allSettled(
    ids.map(id => fetchUserPromise(id))
  );

  const successful = results
    .filter(result => result.status === 'fulfilled')
    .map(result => result.value);

  const failed = results
    .filter(result => result.status === 'rejected')
    .map(result => result.reason);

  console.log('Successful:', successful);
  console.log('Failed:', failed);

  return { successful, failed };
}

fetchMultipleUsersSettled([1, -1, 2, -2]);

// 6. Promise.race - First to complete
async function fetchWithTimeout(id, timeout = 5000) {
  const fetchPromise = fetchUserPromise(id);
  const timeoutPromise = new Promise((_, reject) => {
    setTimeout(() => reject(new Error('Timeout')), timeout);
  });

  try {
    const result = await Promise.race([fetchPromise, timeoutPromise]);
    return result;
  } catch (error) {
    console.error('Fetch failed or timed out:', error);
    throw error;
  }
}

// 7. Promise.any - First successful
async function fetchFromMultipleSources(id) {
  const sources = [
    fetch(`/api/v1/users/${id}`),
    fetch(`/api/v2/users/${id}`),
    fetch(`/backup/users/${id}`)
  ];

  try {
    const response = await Promise.any(sources);
    return await response.json();
  } catch (error) {
    console.error('All sources failed:', error);
  }
}

// 8. Advanced error handling
async function robustFetch(url, retries = 3) {
  for (let i = 0; i < retries; i++) {
    try {
      const response = await fetch(url);

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }

      return await response.json();
    } catch (error) {
      console.log(`Attempt ${i + 1} failed:`, error.message);

      if (i === retries - 1) {
        throw error;
      }

      // Exponential backoff
      await new Promise(resolve => setTimeout(resolve, Math.pow(2, i) * 1000));
    }
  }
}

// 9. Async generators
async function* fetchPaginatedData(baseUrl) {
  let page = 1;
  let hasMore = true;

  while (hasMore) {
    try {
      const response = await fetch(`${baseUrl}?page=${page}`);
      const data = await response.json();

      yield data.items;

      hasMore = data.hasNextPage;
      page++;
    } catch (error) {
      console.error('Failed to fetch page:', page, error);
      break;
    }
  }
}

// Usage
async function processAllData() {
  for await (const items of fetchPaginatedData('/api/items')) {
    console.log('Processing batch:', items.length);
    // Process items
  }
}

// 10. AbortController for cancellation
async function fetchWithAbort(url, timeoutMs = 5000) {
  const controller = new AbortController();

  // Set timeout
  const timeoutId = setTimeout(() => controller.abort(), timeoutMs);

  try {
    const response = await fetch(url, {
      signal: controller.signal
    });

    clearTimeout(timeoutId);
    return await response.json();
  } catch (error) {
    clearTimeout(timeoutId);

    if (error.name === 'AbortError') {
      console.log('Fetch was aborted');
    } else {
      console.error('Fetch failed:', error);
    }
    throw error;
  }
}

// Manual cancellation
const controller = new AbortController();
fetchWithAbort('/api/data', { signal: controller.signal });

// Cancel after 2 seconds
setTimeout(() => controller.abort(), 2000);
```

#### Q12: Cách remove property từ object và so sánh objects?

**Trả lời:**

```javascript
// 1. Remove property từ object
const user = {
  id: 1,
  name: 'John',
  email: 'john@example.com',
  password: 'secret',
  role: 'admin'
};

// Method 1: delete operator
delete user.password;
console.log(user); // { id: 1, name: 'John', email: 'john@example.com', role: 'admin' }

// Method 2: Destructuring + Rest (immutable)
const { password, ...userWithoutPassword } = user;
console.log(userWithoutPassword); // { id: 1, name: 'John', email: 'john@example.com', role: 'admin' }
console.log(user); // Original object unchanged

// Method 3: Omit function
function omit(obj, ...keys) {
  const result = { ...obj };
  keys.forEach(key => delete result[key]);
  return result;
}

const publicUser = omit(user, 'password', 'role');
console.log(publicUser); // { id: 1, name: 'John', email: 'john@example.com' }

// Method 4: Pick function (opposite of omit)
function pick(obj, ...keys) {
  return keys.reduce((result, key) => {
    if (key in obj) {
      result[key] = obj[key];
    }
    return result;
  }, {});
}

const basicUser = pick(user, 'id', 'name');
console.log(basicUser); // { id: 1, name: 'John' }

// Method 5: Using Object.fromEntries
function removeProperties(obj, ...propsToRemove) {
  return Object.fromEntries(
    Object.entries(obj).filter(([key]) => !propsToRemove.includes(key))
  );
}

const filteredUser = removeProperties(user, 'password', 'role');

// 2. So sánh objects
// Shallow comparison
function shallowEqual(obj1, obj2) {
  const keys1 = Object.keys(obj1);
  const keys2 = Object.keys(obj2);

  if (keys1.length !== keys2.length) {
    return false;
  }

  for (let key of keys1) {
    if (obj1[key] !== obj2[key]) {
      return false;
    }
  }

  return true;
}

const obj1 = { a: 1, b: 2 };
const obj2 = { a: 1, b: 2 };
const obj3 = { a: 1, b: { c: 3 } };
const obj4 = { a: 1, b: { c: 3 } };

console.log(shallowEqual(obj1, obj2)); // true
console.log(shallowEqual(obj3, obj4)); // false (different object references)

// Deep comparison
function deepEqual(obj1, obj2) {
  if (obj1 === obj2) {
    return true;
  }

  if (obj1 == null || obj2 == null) {
    return false;
  }

  if (typeof obj1 !== typeof obj2) {
    return false;
  }

  if (typeof obj1 !== 'object') {
    return obj1 === obj2;
  }

  if (Array.isArray(obj1) !== Array.isArray(obj2)) {
    return false;
  }

  const keys1 = Object.keys(obj1);
  const keys2 = Object.keys(obj2);

  if (keys1.length !== keys2.length) {
    return false;
  }

  for (let key of keys1) {
    if (!keys2.includes(key)) {
      return false;
    }

    if (!deepEqual(obj1[key], obj2[key])) {
      return false;
    }
  }

  return true;
}

console.log(deepEqual(obj3, obj4)); // true
console.log(deepEqual([1, [2, 3]], [1, [2, 3]])); // true

// 3. So sánh big numbers/decimals
// Problem với floating point
console.log(0.1 + 0.2 === 0.3); // false!
console.log(0.1 + 0.2); // 0.30000000000000004

// Solution 1: Number.EPSILON
function floatEqual(a, b, epsilon = Number.EPSILON) {
  return Math.abs(a - b) < epsilon;
}

console.log(floatEqual(0.1 + 0.2, 0.3)); // true

// Solution 2: toFixed
function compareDecimals(a, b, precision = 10) {
  return parseFloat(a.toFixed(precision)) === parseFloat(b.toFixed(precision));
}

console.log(compareDecimals(0.1 + 0.2, 0.3)); // true

// Solution 3: BigInt for large integers
const bigInt1 = BigInt("123456789012345678901234567890");
const bigInt2 = BigInt("123456789012345678901234567890");

console.log(bigInt1 === bigInt2); // true

// For decimal precision with BigInt
function decimalToBigInt(decimal, precision = 18) {
  const factor = BigInt(10 ** precision);
  return BigInt(Math.round(decimal * (10 ** precision)));
}

function compareBigDecimals(a, b, precision = 18) {
  return decimalToBigInt(a, precision) === decimalToBigInt(b, precision);
}

// 4. String combination methods
const firstName = 'John';
const lastName = 'Doe';
const age = 30;

// Method 1: Concatenation
const name1 = firstName + ' ' + lastName;

// Method 2: Template literals (recommended)
const greeting = `Hello, my name is ${firstName} ${lastName} and I'm ${age} years old.`;

// Method 3: join
const fullName = [firstName, lastName].join(' ');

// Method 4: concat
const name2 = firstName.concat(' ', lastName);

// Performance comparison for large operations
function combineStringsConcat(arr) {
  let result = '';
  for (let str of arr) {
    result += str;
  }
  return result;
}

function combineStringsJoin(arr) {
  return arr.join('');
}

// join() is generally faster for many strings
const manyStrings = new Array(10000).fill('test');
console.time('concat');
combineStringsConcat(manyStrings);
console.timeEnd('concat');

console.time('join');
combineStringsJoin(manyStrings);
console.timeEnd('join');

// 5. Advanced object operations
class ObjectUtils {
  static merge(target, ...sources) {
    return sources.reduce((acc, source) => {
      Object.keys(source).forEach(key => {
        if (source[key] && typeof source[key] === 'object' && !Array.isArray(source[key])) {
          acc[key] = this.merge(acc[key] || {}, source[key]);
        } else {
          acc[key] = source[key];
        }
      });
      return acc;
    }, { ...target });
  }

  static flatten(obj, prefix = '') {
    return Object.keys(obj).reduce((acc, key) => {
      const value = obj[key];
      const newKey = prefix ? `${prefix}.${key}` : key;

      if (value && typeof value === 'object' && !Array.isArray(value)) {
        Object.assign(acc, this.flatten(value, newKey));
      } else {
        acc[newKey] = value;
      }

      return acc;
    }, {});
  }

  static unflatten(obj) {
    const result = {};

    Object.keys(obj).forEach(key => {
      const keys = key.split('.');
      let current = result;

      keys.forEach((k, index) => {
        if (index === keys.length - 1) {
          current[k] = obj[key];
        } else {
          current[k] = current[k] || {};
          current = current[k];
        }
      });
    });

    return result;
  }
}

const nested = {
  user: {
    profile: {
      name: 'John',
      address: {
        city: 'New York'
      }
    }
  }
};

const flattened = ObjectUtils.flatten(nested);
console.log(flattened); // { 'user.profile.name': 'John', 'user.profile.address.city': 'New York' }

const restored = ObjectUtils.unflatten(flattened);
console.log(restored); // Original nested structure
```

#### Q14: Loop Performance và Browser Rendering (Paint, Repaint, Reflow)?

**Trả lời:**

```javascript
// 1. Loop Performance Comparison
const data = Array.from({ length: 100000 }, (_, i) => i);

// for loop - Fastest
console.time('for loop');
let sum1 = 0;
for (let i = 0; i < data.length; i++) {
  sum1 += data[i];
}
console.timeEnd('for loop');

// for...of - Good performance
console.time('for...of');
let sum2 = 0;
for (const item of data) {
  sum2 += item;
}
console.timeEnd('for...of');

// forEach - Slower due to function calls
console.time('forEach');
let sum3 = 0;
data.forEach(item => {
  sum3 += item;
});
console.timeEnd('forEach');

// for...in - Slowest (don't use for arrays)
console.time('for...in');
let sum4 = 0;
for (const index in data) {
  sum4 += data[index];
}
console.timeEnd('for...in');

// Performance ranking: for > for...of > forEach > for...in

// 2. Optimized Array Methods
// map - Creates new array
const doubled = data.map(x => x * 2);

// reduce - Single value
const total = data.reduce((acc, curr) => acc + curr, 0);

// filter - Filtered array
const evens = data.filter(x => x % 2 === 0);

// find - First match
const found = data.find(x => x > 50000);

// some/every - Boolean checks
const hasLarge = data.some(x => x > 90000);
const allPositive = data.every(x => x >= 0);

// 3. Paint, Repaint, Reflow trong trình duyệt
/*
Browser Rendering Process:
1. Parse HTML/CSS → DOM/CSSOM
2. Layout (Reflow) → Calculate positions
3. Paint → Fill pixels
4. Composite → Layer combination
*/

// REFLOW (Layout) - Most expensive
// Changes that affect layout/geometry
function causeReflow() {
  const element = document.getElementById('box');

  // These properties trigger reflow:
  element.style.width = '200px';     // Size changes
  element.style.height = '200px';
  element.style.margin = '10px';     // Spacing changes
  element.style.padding = '5px';
  element.style.border = '1px solid black';
  element.style.fontSize = '16px';   // Text size changes

  // Reading these properties also triggers reflow:
  console.log(element.offsetWidth);
  console.log(element.offsetHeight);
  console.log(element.scrollTop);
  console.log(element.clientWidth);
}

// REPAINT (Paint) - Medium cost
// Changes that affect appearance but not layout
function causeRepaint() {
  const element = document.getElementById('box');

  // These properties trigger repaint only:
  element.style.backgroundColor = 'red';
  element.style.color = 'white';
  element.style.borderColor = 'blue';
  element.style.visibility = 'hidden'; // vs display: none (reflow)
}

// COMPOSITE ONLY - Cheapest
// Changes that only affect compositing
function compositeOnly() {
  const element = document.getElementById('box');

  // These properties are GPU accelerated:
  element.style.transform = 'translateX(100px)'; // Use transform, not left/top
  element.style.opacity = '0.5';
  element.style.filter = 'blur(5px)';
}

// 4. Performance Optimization Techniques
// Batch DOM operations
function badPerformance() {
  const list = document.getElementById('list');

  // Bad: Causes multiple reflows
  for (let i = 0; i < 1000; i++) {
    const item = document.createElement('li');
    item.textContent = `Item ${i}`;
    list.appendChild(item); // Reflow on each append
  }
}

function goodPerformance() {
  const list = document.getElementById('list');
  const fragment = document.createDocumentFragment();

  // Good: Batch operations
  for (let i = 0; i < 1000; i++) {
    const item = document.createElement('li');
    item.textContent = `Item ${i}`;
    fragment.appendChild(item); // No reflow
  }

  list.appendChild(fragment); // Single reflow
}

// Use CSS classes instead of individual styles
function animateElement() {
  const element = document.getElementById('box');

  // Bad: Multiple style changes
  element.style.width = '200px';
  element.style.height = '200px';
  element.style.backgroundColor = 'red';
  element.style.transform = 'rotate(45deg)';

  // Good: Single class change
  element.className = 'animated-box';
}

// CSS for above:
/*
.animated-box {
  width: 200px;
  height: 200px;
  background-color: red;
  transform: rotate(45deg);
  transition: all 0.3s ease;
}
*/

// 5. Measuring Performance
function measureRenderPerformance() {
  // Performance API
  const observer = new PerformanceObserver((list) => {
    for (const entry of list.getEntries()) {
      console.log('Performance entry:', entry);
    }
  });

  observer.observe({ entryTypes: ['measure', 'navigation', 'paint'] });

  // Custom measurements
  performance.mark('start-operation');

  // Expensive operation
  for (let i = 0; i < 1000; i++) {
    document.getElementById('test').style.left = i + 'px';
  }

  performance.mark('end-operation');
  performance.measure('operation-duration', 'start-operation', 'end-operation');
}

// 6. RequestAnimationFrame for smooth animations
function smoothAnimation() {
  const element = document.getElementById('box');
  let position = 0;

  function animate() {
    position += 2;
    element.style.transform = `translateX(${position}px)`;

    if (position < 300) {
      requestAnimationFrame(animate); // 60fps
    }
  }

  requestAnimationFrame(animate);
}

// vs bad animation
function badAnimation() {
  const element = document.getElementById('box');
  let position = 0;

  const interval = setInterval(() => {
    position += 2;
    element.style.left = position + 'px'; // Causes reflow

    if (position >= 300) {
      clearInterval(interval);
    }
  }, 16); // Trying to match 60fps
}

// 7. Virtual Scrolling for large lists
class VirtualList {
  constructor(container, items, itemHeight = 50) {
    this.container = container;
    this.items = items;
    this.itemHeight = itemHeight;
    this.containerHeight = container.clientHeight;
    this.visibleCount = Math.ceil(this.containerHeight / itemHeight) + 1;
    this.startIndex = 0;

    this.setupContainer();
    this.render();
    this.bindEvents();
  }

  setupContainer() {
    this.container.style.overflowY = 'scroll';
    this.container.style.height = this.containerHeight + 'px';

    // Create spacer for total height
    this.spacer = document.createElement('div');
    this.spacer.style.height = (this.items.length * this.itemHeight) + 'px';
    this.container.appendChild(this.spacer);

    // Create visible items container
    this.visibleContainer = document.createElement('div');
    this.visibleContainer.style.position = 'absolute';
    this.visibleContainer.style.top = '0';
    this.visibleContainer.style.width = '100%';
    this.container.appendChild(this.visibleContainer);
  }

  render() {
    const fragment = document.createDocumentFragment();

    for (let i = 0; i < this.visibleCount && this.startIndex + i < this.items.length; i++) {
      const item = document.createElement('div');
      item.style.height = this.itemHeight + 'px';
      item.textContent = this.items[this.startIndex + i];
      fragment.appendChild(item);
    }

    this.visibleContainer.innerHTML = '';
    this.visibleContainer.appendChild(fragment);
    this.visibleContainer.style.transform = `translateY(${this.startIndex * this.itemHeight}px)`;
  }

  bindEvents() {
    this.container.addEventListener('scroll', () => {
      const newStartIndex = Math.floor(this.container.scrollTop / this.itemHeight);

      if (newStartIndex !== this.startIndex) {
        this.startIndex = newStartIndex;
        this.render();
      }
    });
  }
}

// Usage
const items = Array.from({ length: 10000 }, (_, i) => `Item ${i}`);
const virtualList = new VirtualList(document.getElementById('list'), items);
```

#### Q15: Axios Interceptors và Advanced Error Handling?

**Trả lời:**

```javascript
// 1. Basic Axios Interceptors
import axios from 'axios';

// Request Interceptor
axios.interceptors.request.use(
  (config) => {
    // Add auth token
    const token = localStorage.getItem('authToken');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }

    // Add request timestamp
    config.metadata = { startTime: new Date() };

    console.log('Request sent:', config);
    return config;
  },
  (error) => {
    console.error('Request error:', error);
    return Promise.reject(error);
  }
);

// Response Interceptor
axios.interceptors.response.use(
  (response) => {
    // Calculate request duration
    const endTime = new Date();
    const duration = endTime - response.config.metadata.startTime;
    console.log(`Request took ${duration}ms`);

    return response;
  },
  (error) => {
    // Handle common errors
    if (error.response?.status === 401) {
      // Redirect to login
      localStorage.removeItem('authToken');
      window.location.href = '/login';
    }

    return Promise.reject(error);
  }
);

// 2. Advanced Interceptor Setup
class ApiClient {
  constructor(baseURL) {
    this.client = axios.create({
      baseURL,
      timeout: 10000,
      headers: {
        'Content-Type': 'application/json'
      }
    });

    this.setupInterceptors();
  }

  setupInterceptors() {
    // Request interceptor
    this.client.interceptors.request.use(
      this.handleRequest.bind(this),
      this.handleRequestError.bind(this)
    );

    // Response interceptor
    this.client.interceptors.response.use(
      this.handleResponse.bind(this),
      this.handleResponseError.bind(this)
    );
  }

  handleRequest(config) {
    // Add loading state
    this.setLoading(true);

    // Add auth
    const token = this.getAuthToken();
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }

    // Add request ID for tracking
    config.headers['X-Request-ID'] = this.generateRequestId();

    // Add API version
    config.headers['X-API-Version'] = '1.0';

    return config;
  }

  handleRequestError(error) {
    this.setLoading(false);
    this.showError('Request failed to send');
    return Promise.reject(error);
  }

  handleResponse(response) {
    this.setLoading(false);

    // Log successful requests
    console.log('✅ API Success:', {
      url: response.config.url,
      method: response.config.method.toUpperCase(),
      status: response.status,
      data: response.data
    });

    return response;
  }

  async handleResponseError(error) {
    this.setLoading(false);

    const { response, request, message } = error;

    if (response) {
      // Server responded with error
      await this.handleServerError(response);
    } else if (request) {
      // Network error
      this.handleNetworkError();
    } else {
      // Other error
      this.handleGenericError(message);
    }

    return Promise.reject(error);
  }

  async handleServerError(response) {
    const { status, data } = response;

    switch (status) {
      case 400:
        this.showError('Invalid request data');
        break;

      case 401:
        await this.handleUnauthorized();
        break;

      case 403:
        this.showError('Access denied');
        break;

      case 404:
        this.showError('Resource not found');
        break;

      case 409:
        this.showError('Conflict: Resource already exists');
        break;

      case 422:
        this.handleValidationErrors(data.errors);
        break;

      case 429:
        this.handleRateLimit(response.headers);
        break;

      case 500:
        this.showError('Server error. Please try again later.');
        break;

      case 503:
        this.showError('Service temporarily unavailable');
        break;

      default:
        this.showError(`Unexpected error: ${status}`);
    }
  }

  async handleUnauthorized() {
    // Try to refresh token
    try {
      await this.refreshToken();
      // Retry original request
      return true;
    } catch (refreshError) {
      // Redirect to login
      this.logout();
      return false;
    }
  }

  handleNetworkError() {
    if (!navigator.onLine) {
      this.showError('No internet connection');
    } else {
      this.showError('Network error. Please check your connection.');
    }
  }

  handleValidationErrors(errors) {
    Object.keys(errors).forEach(field => {
      const messages = errors[field];
      this.showFieldError(field, messages.join(', '));
    });
  }

  handleRateLimit(headers) {
    const retryAfter = headers['retry-after'];
    this.showError(`Rate limit exceeded. Retry after ${retryAfter} seconds.`);
  }

  // Utility methods
  getAuthToken() {
    return localStorage.getItem('authToken');
  }

  generateRequestId() {
    return Math.random().toString(36).substr(2, 9);
  }

  setLoading(loading) {
    // Update global loading state
    window.dispatchEvent(new CustomEvent('loadingChange', { detail: loading }));
  }

  showError(message) {
    // Show toast/notification
    window.dispatchEvent(new CustomEvent('showError', { detail: message }));
  }

  showFieldError(field, message) {
    // Show field-specific error
    window.dispatchEvent(new CustomEvent('fieldError', {
      detail: { field, message }
    }));
  }

  async refreshToken() {
    const refreshToken = localStorage.getItem('refreshToken');
    const response = await axios.post('/auth/refresh', { refreshToken });
    localStorage.setItem('authToken', response.data.accessToken);
    return response.data;
  }

  logout() {
    localStorage.removeItem('authToken');
    localStorage.removeItem('refreshToken');
    window.location.href = '/login';
  }
}

// 3. Request/Response Transformation
const api = new ApiClient('/api/v1');

// Transform request data
api.client.interceptors.request.use((config) => {
  // Convert camelCase to snake_case for API
  if (config.data && typeof config.data === 'object') {
    config.data = transformKeys(config.data, camelToSnake);
  }

  // Convert query params
  if (config.params) {
    config.params = transformKeys(config.params, camelToSnake);
  }

  return config;
});

// Transform response data
api.client.interceptors.response.use((response) => {
  // Convert snake_case to camelCase
  if (response.data && typeof response.data === 'object') {
    response.data = transformKeys(response.data, snakeToCamel);
  }

  return response;
});

// Key transformation utilities
function transformKeys(obj, transformer) {
  if (Array.isArray(obj)) {
    return obj.map(item => transformKeys(item, transformer));
  }

  if (obj && typeof obj === 'object') {
    return Object.keys(obj).reduce((result, key) => {
      const transformedKey = transformer(key);
      result[transformedKey] = transformKeys(obj[key], transformer);
      return result;
    }, {});
  }

  return obj;
}

function camelToSnake(str) {
  return str.replace(/[A-Z]/g, letter => `_${letter.toLowerCase()}`);
}

function snakeToCamel(str) {
  return str.replace(/_([a-z])/g, (_, letter) => letter.toUpperCase());
}

// 4. Request Retry Logic
api.client.interceptors.response.use(null, async (error) => {
  const config = error.config;

  // Don't retry if already retried max times
  if (!config || !config.retry || config.retryCount >= config.retry) {
    return Promise.reject(error);
  }

  // Increment retry count
  config.retryCount = config.retryCount || 0;
  config.retryCount++;

  // Exponential backoff
  const delay = Math.pow(2, config.retryCount) * 1000;
  await new Promise(resolve => setTimeout(resolve, delay));

  // Retry request
  return api.client.request(config);
});

// 5. Request Caching
class CachedApiClient extends ApiClient {
  constructor(baseURL) {
    super(baseURL);
    this.cache = new Map();
    this.setupCaching();
  }

  setupCaching() {
    // Cache GET requests
    this.client.interceptors.request.use((config) => {
      if (config.method === 'get' && config.cache !== false) {
        const cacheKey = this.getCacheKey(config);
        const cached = this.cache.get(cacheKey);

        if (cached && !this.isCacheExpired(cached)) {
          // Return cached response
          config.adapter = () => Promise.resolve(cached.response);
        }
      }

      return config;
    });

    // Store responses in cache
    this.client.interceptors.response.use((response) => {
      if (response.config.method === 'get' && response.config.cache !== false) {
        const cacheKey = this.getCacheKey(response.config);
        const ttl = response.config.cacheTTL || 300000; // 5 minutes default

        this.cache.set(cacheKey, {
          response,
          timestamp: Date.now(),
          ttl
        });
      }

      return response;
    });
  }

  getCacheKey(config) {
    return `${config.method}:${config.url}:${JSON.stringify(config.params)}`;
  }

  isCacheExpired(cached) {
    return Date.now() - cached.timestamp > cached.ttl;
  }

  clearCache() {
    this.cache.clear();
  }
}

// 6. Usage Examples
const cachedApi = new CachedApiClient('/api/v1');

// Basic requests
async function fetchUser(id) {
  try {
    const response = await cachedApi.client.get(`/users/${id}`, {
      retry: 3,
      cache: true,
      cacheTTL: 600000 // 10 minutes
    });
    return response.data;
  } catch (error) {
    console.error('Failed to fetch user:', error);
    throw error;
  }
}

// Parallel requests
async function fetchUserData(userId) {
  try {
    const [user, posts, followers] = await Promise.all([
      cachedApi.client.get(`/users/${userId}`),
      cachedApi.client.get(`/users/${userId}/posts`),
      cachedApi.client.get(`/users/${userId}/followers`)
    ]);

    return {
      user: user.data,
      posts: posts.data,
      followers: followers.data
    };
  } catch (error) {
    console.error('Failed to fetch user data:', error);
    throw error;
  }
}
```

#### Q16: Strict Mode và JavaScript Classes?

**Trả lời:**

```javascript
// 1. Strict Mode trong JavaScript
'use strict'; // Global strict mode

function normalFunction() {
  // Non-strict mode behavior
  undeclaredVar = 10; // Creates global variable
  return undeclaredVar;
}

function strictFunction() {
  'use strict'; // Function-level strict mode

  // undeclaredVar = 10; // ReferenceError in strict mode

  // Other strict mode changes:

  // 1. 'this' is undefined in functions (not window)
  console.log(this); // undefined

  // 2. Can't delete variables, functions, or arguments
  var x = 10;
  // delete x; // SyntaxError

  // 3. Duplicate parameter names not allowed
  // function duplicate(a, a) {} // SyntaxError

  // 4. Octal literals not allowed
  // var octal = 077; // SyntaxError

  // 5. Can't assign to read-only properties
  var obj = {};
  Object.defineProperty(obj, 'prop', { value: 10, writable: false });
  // obj.prop = 20; // TypeError
}

// 2. ES6 Classes - Modern approach
class User {
  // Private fields (ES2022)
  #password;
  #loginAttempts = 0;

  // Public fields
  isActive = true;

  // Static field
  static maxLoginAttempts = 3;

  constructor(username, email, password) {
    this.username = username;
    this.email = email;
    this.#password = password;
    this.createdAt = new Date();
  }

  // Public method
  login(password) {
    if (this.#loginAttempts >= User.maxLoginAttempts) {
      throw new Error('Account locked');
    }

    if (this.#checkPassword(password)) {
      this.#loginAttempts = 0;
      this.lastLogin = new Date();
      return true;
    } else {
      this.#loginAttempts++;
      return false;
    }
  }

  // Private method
  #checkPassword(password) {
    return this.#password === password;
  }

  // Getter
  get profile() {
    return {
      username: this.username,
      email: this.email,
      isActive: this.isActive,
      createdAt: this.createdAt
    };
  }

  // Setter
  set email(newEmail) {
    if (this.#validateEmail(newEmail)) {
      this._email = newEmail;
    } else {
      throw new Error('Invalid email format');
    }
  }

  get email() {
    return this._email;
  }

  #validateEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  // Static method
  static createGuest() {
    return new User('guest', 'guest@example.com', 'temporary');
  }

  // Method override example
  toString() {
    return `User: ${this.username} (${this.email})`;
  }
}

// 3. Inheritance
class AdminUser extends User {
  constructor(username, email, password, permissions = []) {
    super(username, email, password); // Call parent constructor
    this.permissions = permissions;
    this.isAdmin = true;
  }

  // Override parent method
  login(password) {
    const success = super.login(password); // Call parent method

    if (success) {
      console.log(`Admin ${this.username} logged in`);
      this.auditLog('login');
    }

    return success;
  }

  // New method
  auditLog(action) {
    console.log(`[AUDIT] ${this.username} performed: ${action} at ${new Date()}`);
  }

  addPermission(permission) {
    if (!this.permissions.includes(permission)) {
      this.permissions.push(permission);
    }
  }

  hasPermission(permission) {
    return this.permissions.includes(permission);
  }
}

// 4. Mixins Pattern
const Serializable = {
  serialize() {
    return JSON.stringify(this);
  },

  deserialize(json) {
    const data = JSON.parse(json);
    Object.assign(this, data);
    return this;
  }
};

const Timestamped = {
  updateTimestamp() {
    this.updatedAt = new Date();
  },

  getAge() {
    return Date.now() - this.createdAt.getTime();
  }
};

// Apply mixins
Object.assign(User.prototype, Serializable, Timestamped);

// 5. Abstract Base Class Pattern
class Shape {
  constructor(color) {
    if (new.target === Shape) {
      throw new Error('Cannot instantiate abstract class');
    }
    this.color = color;
  }

  // Abstract method
  area() {
    throw new Error('Must implement area method');
  }

  // Concrete method
  describe() {
    return `A ${this.color} shape with area ${this.area()}`;
  }
}

class Circle extends Shape {
  constructor(color, radius) {
    super(color);
    this.radius = radius;
  }

  area() {
    return Math.PI * this.radius ** 2;
  }
}

class Rectangle extends Shape {
  constructor(color, width, height) {
    super(color);
    this.width = width;
    this.height = height;
  }

  area() {
    return this.width * this.height;
  }
}

// 6. Factory Pattern with Classes
class CarFactory {
  static types = {
    sedan: 'Sedan',
    suv: 'SUV',
    hatchback: 'Hatchback'
  };

  static create(type, options) {
    switch (type) {
      case CarFactory.types.sedan:
        return new Sedan(options);
      case CarFactory.types.suv:
        return new SUV(options);
      case CarFactory.types.hatchback:
        return new Hatchback(options);
      default:
        throw new Error(`Unknown car type: ${type}`);
    }
  }
}

class Car {
  constructor({ make, model, year, color }) {
    this.make = make;
    this.model = model;
    this.year = year;
    this.color = color;
    this.mileage = 0;
  }

  start() {
    console.log(`${this.make} ${this.model} started`);
  }

  drive(distance) {
    this.mileage += distance;
    console.log(`Drove ${distance} miles. Total: ${this.mileage} miles`);
  }
}

class Sedan extends Car {
  constructor(options) {
    super(options);
    this.type = 'sedan';
    this.fuelEfficiency = 30; // mpg
  }
}

class SUV extends Car {
  constructor(options) {
    super(options);
    this.type = 'suv';
    this.fuelEfficiency = 20; // mpg
    this.has4WD = true;
  }
}

class Hatchback extends Car {
  constructor(options) {
    super(options);
    this.type = 'hatchback';
    this.fuelEfficiency = 35; // mpg
  }
}

// 7. Performance Optimized Classes
class OptimizedDataProcessor {
  constructor() {
    this.cache = new Map();
    this.results = [];

    // Bind methods to avoid recreating functions
    this.process = this.process.bind(this);
    this.getResults = this.getResults.bind(this);
  }

  // Use static methods when no instance data needed
  static validateData(data) {
    return Array.isArray(data) && data.length > 0;
  }

  // Memoized method
  expensiveCalculation(input) {
    if (this.cache.has(input)) {
      return this.cache.get(input);
    }

    // Simulate expensive operation
    const result = input.split('').reverse().join('').repeat(1000);
    this.cache.set(input, result);

    return result;
  }

  // Batch processing
  process(dataArray) {
    if (!OptimizedDataProcessor.validateData(dataArray)) {
      throw new Error('Invalid data');
    }

    // Process in chunks to avoid blocking
    const chunkSize = 100;
    const chunks = this.createChunks(dataArray, chunkSize);

    return new Promise((resolve) => {
      this.processChunks(chunks, 0, resolve);
    });
  }

  createChunks(array, size) {
    const chunks = [];
    for (let i = 0; i < array.length; i += size) {
      chunks.push(array.slice(i, i + size));
    }
    return chunks;
  }

  processChunks(chunks, index, callback) {
    if (index >= chunks.length) {
      callback(this.results);
      return;
    }

    // Process chunk
    const chunk = chunks[index];
    chunk.forEach(item => {
      this.results.push(this.expensiveCalculation(item));
    });

    // Use setTimeout to yield control
    setTimeout(() => {
      this.processChunks(chunks, index + 1, callback);
    }, 0);
  }

  getResults() {
    return [...this.results]; // Return copy to prevent mutation
  }

  clear() {
    this.cache.clear();
    this.results.length = 0;
  }
}

// 8. Usage Examples
// Create instances
const user = new User('john', 'john@example.com', 'password123');
const admin = new AdminUser('admin', 'admin@example.com', 'admin123', ['read', 'write', 'delete']);

// Test functionality
console.log(user.login('password123')); // true
console.log(user.profile); // { username: 'john', ... }

admin.addPermission('manage_users');
console.log(admin.hasPermission('delete')); // true

// Serialization
const serialized = user.serialize();
const newUser = new User('', '', '').deserialize(serialized);

// Factory pattern
const sedan = CarFactory.create(CarFactory.types.sedan, {
  make: 'Toyota',
  model: 'Camry',
  year: 2023,
  color: 'blue'
});

sedan.start();
sedan.drive(100);

// Optimized processing
const processor = new OptimizedDataProcessor();
processor.process(['data1', 'data2', 'data3']).then(results => {
  console.log('Processing complete:', results.length);
});
```

### 2. React Fundamentals

#### Q17: React Hooks chi tiết - useState, useEffect, useRef?

**Trả lời:**

**Giải thích:**
- **useState**: Quản lý state trong functional component
- **useEffect**: Xử lý side effects (thay thế lifecycle methods)
- **useRef**: Tham chiếu DOM elements hoặc lưu giá trị mutable

```typescript
// 1. useState - Quản lý state trong functional component
import React, { useState, useCallback, useMemo, useEffect, useRef } from 'react';

// Interface định nghĩa kiểu dữ liệu cho user
interface User {
  name: string;
  age: number;
}

function Counter(): JSX.Element {
  // useState với kiểu number
  const [count, setCount] = useState<number>(0);

  // useState với kiểu object - cần interface
  const [user, setUser] = useState<User>({ name: '', age: 0 });

  // ❌ Cách sai - thay đổi state trực tiếp (mutate)
  const handleWrongUpdate = (): void => {
    user.name = 'John'; // ĐỪNG LÀM NHƯ VẦY - thay đổi trực tiếp object
    setUser(user); // React sẽ không detect được sự thay đổi
  };

  // ✅ Cách đúng - cập nhật immutable (không thay đổi object gốc)
  const handleCorrectUpdate = (): void => {
    setUser(prev => ({
      ...prev, // Sao chép tất cả properties cũ
      name: 'John' // Chỉ thay đổi property cần thiết
    }));
  };

  // Functional updates - tốt hơn cho performance
  const increment = useCallback((): void => {
    setCount(prev => prev + 1); // Tốt hơn setCount(count + 1) vì tránh stale closure
  }, []);

  // Lazy initial state - chỉ chạy 1 lần khi component mount
  const [expensiveValue] = useState<number>(() => {
    console.log('Chỉ chạy 1 lần khi component được tạo');
    return Array.from({ length: 1000 }, (_, i) => i).reduce((a, b) => a + b, 0);
  });

  return (
    <div>
      <p>Count: {count}</p>
      <p>Expensive value: {expensiveValue}</p>
      <button onClick={increment}>Increment</button>
      <button onClick={handleCorrectUpdate}>Update User</button>
    </div>
  );
}

// 2. useEffect - Xử lý side effects và cleanup
interface UserProfileProps {
  userId: number;
}

interface UserData {
  id: number;
  name: string;
  email: string;
}

function UserProfile({ userId }: UserProfileProps): JSX.Element {
  // State với kiểu union type (có thể null hoặc UserData)
  const [user, setUser] = useState<UserData | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  // useEffect với dependencies - chỉ chạy khi userId thay đổi
  useEffect(() => {
    let cancelled = false; // Flag để tránh memory leak khi component unmount

    async function fetchUser(): Promise<void> {
      try {
        setLoading(true);
        setError(null);

        const response = await fetch(`/api/users/${userId}`);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const userData: UserData = await response.json();

        // Kiểm tra component còn được mount không (tránh memory leak)
        if (!cancelled) {
          setUser(userData);
        }
      } catch (err) {
        if (!cancelled) {
          setError(err instanceof Error ? err.message : 'Có lỗi xảy ra');
        }
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    }

    // Chỉ fetch khi có userId
    if (userId) {
      fetchUser();
    }

    // Cleanup function - chạy khi component unmount hoặc trước effect tiếp theo
    return () => {
      cancelled = true; // Đánh dấu để hủy các async operations
    };
  }, [userId]); // Dependency array - effect chỉ chạy lại khi userId thay đổi

  // Effect với cleanup - subscriptions, timers
  useEffect(() => {
    const timer = setInterval(() => {
      console.log('Timer tick');
    }, 1000);

    const subscription = eventBus.subscribe('userUpdate', (data) => {
      setUser(data);
    });

    // Cleanup function runs on unmount or before next effect
    return () => {
      clearInterval(timer);
      subscription.unsubscribe();
    };
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h1>{user?.name}</h1>
      <p>{user?.email}</p>
    </div>
  );
}

// 3. useRef - Mutable references và DOM access
function TextInput() {
  const inputRef = useRef(null);
  const countRef = useRef(0); // Mutable value không trigger re-render
  const prevCountRef = useRef();
  const [count, setCount] = useState(0);

  // Store previous value
  useEffect(() => {
    prevCountRef.current = count;
  });

  const focusInput = () => {
    inputRef.current?.focus();
  };

  const handleClick = () => {
    countRef.current += 1; // Doesn't trigger re-render
    console.log('Clicked times:', countRef.current);

    setCount(prev => prev + 1); // Triggers re-render
  };

  return (
    <div>
      <input ref={inputRef} type="text" />
      <button onClick={focusInput}>Focus Input</button>

      <p>Current: {count}</p>
      <p>Previous: {prevCountRef.current}</p>
      <p>Click count (no re-render): {countRef.current}</p>
      <button onClick={handleClick}>Click</button>
    </div>
  );
}
```

#### Q18: Component Lifecycle và useEffect coverage?

**Trả lời:**

```javascript
// 1. Class Component Lifecycle Complete
class UserProfileClass extends React.Component {
  constructor(props) {
    super(props);
    this.state = { user: null, loading: true, error: null };
    console.log('1. Constructor - Component được khởi tạo');
  }

  static getDerivedStateFromProps(nextProps, prevState) {
    console.log('2. getDerivedStateFromProps - Sync state với props');
    if (nextProps.userId !== prevState.prevUserId) {
      return { prevUserId: nextProps.userId, user: null, loading: true };
    }
    return null;
  }

  componentDidMount() {
    console.log('3. componentDidMount - Component đã mount');
    this.fetchUser();
    this.timer = setInterval(() => console.log('Timer tick'), 1000);
  }

  shouldComponentUpdate(nextProps, nextState) {
    console.log('4. shouldComponentUpdate - Có nên update không?');
    return (
      nextProps.userId !== this.props.userId ||
      nextState.user !== this.state.user
    );
  }

  getSnapshotBeforeUpdate(prevProps, prevState) {
    console.log('5. getSnapshotBeforeUpdate - Trước khi DOM update');
    if (prevProps.userId !== this.props.userId) {
      return { scrollPosition: window.scrollY };
    }
    return null;
  }

  componentDidUpdate(prevProps, prevState, snapshot) {
    console.log('6. componentDidUpdate - Sau khi update');
    if (prevProps.userId !== this.props.userId) {
      this.fetchUser();
    }
    if (snapshot !== null) {
      window.scrollTo(0, snapshot.scrollPosition);
    }
  }

  componentWillUnmount() {
    console.log('7. componentWillUnmount - Component sắp unmount');
    if (this.timer) clearInterval(this.timer);
    if (this.abortController) this.abortController.abort();
  }

  componentDidCatch(error, errorInfo) {
    console.log('8. componentDidCatch - Bắt lỗi từ children');
    this.setState({ error: error.message });
  }

  fetchUser = async () => {
    try {
      this.abortController = new AbortController();
      const response = await fetch(`/api/users/${this.props.userId}`, {
        signal: this.abortController.signal
      });
      const user = await response.json();
      this.setState({ user, loading: false, error: null });
    } catch (error) {
      if (error.name !== 'AbortError') {
        this.setState({ error: error.message, loading: false });
      }
    }
  };

  render() {
    console.log('Render - Component đang render');
    const { user, loading, error } = this.state;

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;
    return <div><h1>{user?.name}</h1><p>{user?.email}</p></div>;
  }
}

// 2. Functional Component với Hooks (Lifecycle equivalent)
function UserProfileFunction({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const abortControllerRef = useRef();

  // ⚡ componentDidMount + componentDidUpdate equivalent
  useEffect(() => {
    console.log('Mount/Update effect');

    async function fetchUser() {
      try {
        setLoading(true);
        setError(null);

        if (abortControllerRef.current) {
          abortControllerRef.current.abort();
        }

        abortControllerRef.current = new AbortController();
        const response = await fetch(`/api/users/${userId}`, {
          signal: abortControllerRef.current.signal
        });

        const userData = await response.json();
        setUser(userData);
        setLoading(false);
      } catch (err) {
        if (err.name !== 'AbortError') {
          setError(err.message);
          setLoading(false);
        }
      }
    }

    if (userId) fetchUser();

    // ⚡ componentWillUnmount equivalent (cleanup)
    return () => {
      console.log('Cleanup function');
      if (abortControllerRef.current) {
        abortControllerRef.current.abort();
      }
    };
  }, [userId]); // Dependencies = shouldComponentUpdate logic

  // ⚡ componentDidMount only (empty dependency array)
  useEffect(() => {
    console.log('Mount only effect');
    const timer = setInterval(() => console.log('Timer tick'), 1000);
    return () => clearInterval(timer);
  }, []);

  // ⚡ componentDidUpdate only (skip first render)
  const isFirstRender = useRef(true);
  useEffect(() => {
    if (isFirstRender.current) {
      isFirstRender.current = false;
      return;
    }
    console.log('Update only effect');
    document.title = `User: ${user?.name || 'Loading...'}`;
  });

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  return <div><h1>{user?.name}</h1><p>{user?.email}</p></div>;
}

// 3. useEffect Lifecycle Coverage Summary
/*
✅ useEffect(() => {}, []) = componentDidMount
✅ useEffect(() => {}, [dep]) = componentDidUpdate (when dep changes)
✅ useEffect(() => { return () => {} }, []) = componentWillUnmount
✅ useEffect(() => {}) = componentDidMount + componentDidUpdate (every render)
❌ getSnapshotBeforeUpdate = Không có equivalent
❌ componentDidCatch = Chỉ có Error Boundary (Class only)
❌ getDerivedStateFromError = Chỉ có Error Boundary (Class only)
*/

// 4. When will cleanup function run?
function CleanupExample() {
  useEffect(() => {
    console.log('Effect runs');

    return () => {
      console.log('Cleanup runs:');
      console.log('1. Before next effect (if dependencies changed)');
      console.log('2. On component unmount');
    };
  }, [dependency]);

  // Multiple effects - each has its own cleanup
  useEffect(() => {
    const timer = setInterval(() => {}, 1000);
    return () => clearInterval(timer); // Cleanup timer
  }, []);

  useEffect(() => {
    const subscription = subscribe();
    return () => subscription.unsubscribe(); // Cleanup subscription
  }, []);
}

// 5. Error Boundary (Class Component only)
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Error caught:', error, errorInfo);
    this.setState({ error, errorInfo });

    // Send to error reporting service
    this.logErrorToService(error, errorInfo);
  }

  logErrorToService = (error, errorInfo) => {
    // Send to Sentry, LogRocket, etc.
    console.log('Sending to error service:', { error, errorInfo });
  };

  render() {
    if (this.state.hasError) {
      return (
        <div className="error-boundary">
          <h2>Something went wrong!</h2>
          <details style={{ whiteSpace: 'pre-wrap' }}>
            {this.state.error && this.state.error.toString()}
            <br />
            {this.state.errorInfo.componentStack}
          </details>
        </div>
      );
    }
    return this.props.children;
  }
}

// 6. Functional Components CAN'T handle all use cases
/*
❌ Error Boundaries - Chỉ Class Components có thể catch errors
❌ getSnapshotBeforeUpdate - Không có hook equivalent
❌ componentDidCatch - Chỉ có trong Class Components

✅ Mọi thứ khác đều có thể làm với Hooks
*/
```

#### Q19: PureComponent vs React.memo và optimization?

**Trả lời:**

```javascript
// 1. PureComponent - Class Component với shallow comparison
import React, { PureComponent, Component, memo, useState, useCallback, useMemo } from 'react';

// ❌ Regular Component - always re-renders
class RegularComponent extends Component {
  render() {
    console.log('RegularComponent rendered');
    return <div>{this.props.name} - {this.props.count}</div>;
  }
}

// ✅ PureComponent - shallow comparison of props and state
class PureComponentExample extends PureComponent {
  render() {
    console.log('PureComponent rendered');
    return <div>{this.props.name} - {this.props.count}</div>;
  }
}

// ✅ Manual shouldComponentUpdate
class ManualComponent extends Component {
  shouldComponentUpdate(nextProps, nextState) {
    return (
      nextProps.name !== this.props.name ||
      nextProps.count !== this.props.count
    );
  }

  render() {
    console.log('ManualComponent rendered');
    return <div>{this.props.name} - {this.props.count}</div>;
  }
}

// 2. React.memo - Functional Component equivalent
// ❌ Regular Functional Component - always re-renders
function RegularFunction({ name, count }) {
  console.log('RegularFunction rendered');
  return <div>{name} - {count}</div>;
}

// ✅ React.memo - shallow comparison
const MemoizedFunction = memo(function MemoizedFunction({ name, count }) {
  console.log('MemoizedFunction rendered');
  return <div>{name} - {count}</div>;
});

// ✅ React.memo with custom comparison
const CustomMemoFunction = memo(function CustomMemoFunction({ user, settings }) {
  console.log('CustomMemoFunction rendered');
  return <div>{user.name} - {settings.theme}</div>;
}, (prevProps, nextProps) => {
  // Return true if props are equal (DON'T re-render)
  // Return false if props are different (DO re-render)
  return (
    prevProps.user.id === nextProps.user.id &&
    prevProps.user.name === nextProps.user.name &&
    prevProps.settings.theme === nextProps.settings.theme
  );
});

// 3. Why we use PureComponent/React.memo?
function ParentComponent() {
  const [count, setCount] = useState(0);
  const [otherState, setOtherState] = useState('');

  // Expensive data
  const expensiveData = { name: 'John', age: 30 };

  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Count: {count}</button>
      <button onClick={() => setOtherState('changed')}>Change Other State</button>

      {/* ❌ Will re-render even when props haven't changed */}
      <RegularFunction name="John" count={100} />

      {/* ✅ Only re-renders when props actually change */}
      <MemoizedFunction name="John" count={100} />

      {/* ❌ Problem: new object reference every render */}
      <MemoizedFunction name={expensiveData.name} count={expensiveData.age} />
    </div>
  );
}

// 4. Common optimization pitfalls
function ProblematicParent() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Count: {count}</button>

      {/* ❌ New object every render - memo won't help */}
      <MemoizedFunction user={{ name: 'John' }} />

      {/* ❌ New function every render - memo won't help */}
      <MemoizedChild onUpdate={() => console.log('updated')} />

      {/* ❌ New array every render - memo won't help */}
      <MemoizedList items={['a', 'b', 'c']} />
    </div>
  );
}

// 5. Proper optimization techniques
function OptimizedParent() {
  const [count, setCount] = useState(0);
  const [items, setItems] = useState(['a', 'b', 'c']);

  // ✅ Stable object reference
  const user = useMemo(() => ({ name: 'John', id: 1 }), []);

  // ✅ Stable function reference
  const handleUpdate = useCallback(() => {
    console.log('updated');
  }, []);

  // ✅ Memoize expensive computations
  const expensiveValue = useMemo(() => {
    return items.map(item => item.toUpperCase()).join('-');
  }, [items]);

  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Count: {count}</button>

      {/* ✅ Won't re-render unnecessarily */}
      <MemoizedFunction user={user} />
      <MemoizedChild onUpdate={handleUpdate} />
      <MemoizedList items={items} />

      <div>Expensive value: {expensiveValue}</div>
    </div>
  );
}

// 6. When NOT to use memo
// ❌ Don't use memo if props change frequently
const FrequentlyChangingComponent = memo(function FrequentlyChangingComponent({ timestamp }) {
  return <div>Time: {timestamp}</div>; // timestamp changes every second
});

// ❌ Don't use memo for simple components
const SimpleComponent = memo(function SimpleComponent({ text }) {
  return <span>{text}</span>; // Too simple, memo overhead not worth it
});

// ❌ Don't use memo if parent always passes new props
function BadParent() {
  const [count, setCount] = useState(0);

  return (
    <div>
      {/* memo is useless here because data is always new */}
      <MemoizedFunction data={{ value: Math.random() }} />
    </div>
  );
}

// 7. Advanced optimization patterns
const ExpensiveChild = memo(function ExpensiveChild({ data, onProcess }) {
  console.log('ExpensiveChild rendering');

  // Expensive computation only when data changes
  const processedData = useMemo(() => {
    console.log('Processing data...');
    return data.map(item => ({
      ...item,
      processed: true,
      timestamp: Date.now()
    }));
  }, [data]);

  return (
    <div>
      <h3>Processed Items: {processedData.length}</h3>
      <button onClick={() => onProcess(processedData)}>Process</button>
      <ul>
        {processedData.map(item => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
});

function SmartParent() {
  const [items, setItems] = useState([
    { id: 1, name: 'Item 1' },
    { id: 2, name: 'Item 2' }
  ]);
  const [otherState, setOtherState] = useState(0);

  // ✅ Stable callback
  const handleProcess = useCallback((processedData) => {
    console.log('Processed:', processedData);
  }, []);

  // ✅ Add item without changing reference of existing items
  const addItem = useCallback(() => {
    setItems(prev => [...prev, {
      id: Date.now(),
      name: `Item ${prev.length + 1}`
    }]);
  }, []);

  return (
    <div>
      <button onClick={() => setOtherState(prev => prev + 1)}>
        Other State: {otherState}
      </button>
      <button onClick={addItem}>Add Item</button>

      {/* Won't re-render when otherState changes */}
      <ExpensiveChild data={items} onProcess={handleProcess} />
    </div>
  );
}

// 8. Performance measurement
function PerformanceExample() {
  const [count, setCount] = useState(0);

  // Measure component re-renders
  const renderCount = useRef(0);
  renderCount.current++;

  console.log(`Component rendered ${renderCount.current} times`);

  // Use React DevTools Profiler to measure:
  // - Render time
  // - Number of re-renders
  // - Props that caused re-render

  return (
    <div>
      <p>Render count: {renderCount.current}</p>
      <button onClick={() => setCount(count + 1)}>
        Count: {count}
      </button>
    </div>
  );
}
```

#### Q20: Virtual DOM và Key trong Lists?

**Trả lời:**

**Giải thích:**
- **Virtual DOM**: Bản sao ảo của Real DOM trong bộ nhớ, giúp React tối ưu việc cập nhật UI
- **Key trong Lists**: Giúp React nhận diện các item trong list để tối ưu quá trình re-render
- **Tại sao không dùng index**: Index có thể thay đổi khi thêm/xóa item, gây ra bugs

```typescript
// 1. Virtual DOM Concept (Khái niệm Virtual DOM)
/*
Real DOM vs Virtual DOM:

Real DOM:
- Browser's native API
- Heavy operations
- Triggers layout/paint on changes
- Expensive to manipulate

Virtual DOM:
- JavaScript representation of Real DOM
- Lightweight objects
- Fast comparisons (diffing)
- Batch updates to Real DOM
*/

// 2. Tại sao Keys quan trọng trong Lists
interface User {
  id: number;
  name: string;
  email: string;
}

function BadListExample(): JSX.Element {
  const [users, setUsers] = useState<User[]>([
    { id: 1, name: 'John', email: 'john@email.com' },
    { id: 2, name: 'Jane', email: 'jane@email.com' },
    { id: 3, name: 'Bob', email: 'bob@email.com' }
  ]);

  const addUser = (): void => {
    const newUser: User = {
      id: Date.now(),
      name: 'New User',
      email: 'new@email.com'
    };
    setUsers([newUser, ...users]); // Thêm vào đầu list
  };

  const removeUser = (id: number): void => {
    setUsers(users.filter(user => user.id !== id));
  };

  return (
    <div>
      <button onClick={addUser}>Add User</button>

      {/* ❌ BAD: Using index as key */}
      <h3>Bad Example (index as key):</h3>
      {users.map((user, index) => (
        <UserRow
          key={index} // ❌ WRONG: index changes when items are added/removed
          user={user}
          onRemove={removeUser}
        />
      ))}

      {/* ❌ BAD: No key at all */}
      <h3>Worse Example (no key):</h3>
      {users.map((user) => (
        <UserRow // ❌ WRONG: React will warn about missing key
          user={user}
          onRemove={removeUser}
        />
      ))}

      {/* ✅ GOOD: Using stable unique ID as key */}
      <h3>Good Example (stable ID as key):</h3>
      {users.map((user) => (
        <UserRow
          key={user.id} // ✅ CORRECT: stable, unique identifier
          user={user}
          onRemove={removeUser}
        />
      ))}
    </div>
  );
}

function UserRow({ user, onRemove }) {
  const [isEditing, setIsEditing] = useState(false);
  const [localName, setLocalName] = useState(user.name);

  // This component has internal state
  // Wrong keys can cause state to be associated with wrong items

  return (
    <div style={{ border: '1px solid #ccc', margin: '5px', padding: '10px' }}>
      {isEditing ? (
        <input
          value={localName}
          onChange={(e) => setLocalName(e.target.value)}
          onBlur={() => setIsEditing(false)}
        />
      ) : (
        <span onClick={() => setIsEditing(true)}>
          {user.name} - {user.email}
        </span>
      )}
      <button onClick={() => onRemove(user.id)}>Remove</button>
    </div>
  );
}

// 3. Virtual DOM Reconciliation Process
/*
Step 1: State Change
setUsers([newUser, ...users])

Step 2: Virtual DOM Creation
React creates new Virtual DOM tree

Step 3: Diffing Algorithm
React compares old Virtual DOM with new Virtual DOM

Step 4: Reconciliation
React identifies minimal changes needed

Step 5: Real DOM Update
React applies only necessary changes to Real DOM
*/

// 4. Key Reconciliation Examples
function ReconciliationExample() {
  const [items, setItems] = useState([
    { id: 'a', text: 'Item A' },
    { id: 'b', text: 'Item B' },
    { id: 'c', text: 'Item C' }
  ]);

  // Scenario 1: Add item to beginning
  const addToBeginning = () => {
    setItems([{ id: 'new', text: 'New Item' }, ...items]);
  };

  // With index keys: React thinks all items changed
  // key=0: 'New Item' (was 'Item A')
  // key=1: 'Item A' (was 'Item B')
  // key=2: 'Item B' (was 'Item C')
  // key=3: 'Item C' (new)
  // Result: ALL items re-rendered

  // With ID keys: React knows only one item added
  // key='new': 'New Item' (new)
  // key='a': 'Item A' (unchanged)
  // key='b': 'Item B' (unchanged)
  // key='c': 'Item C' (unchanged)
  // Result: Only ONE item rendered

  return (
    <div>
      <button onClick={addToBeginning}>Add to Beginning</button>

      {/* Performance comparison */}
      <div>
        <h4>With Index Keys (Bad Performance):</h4>
        {items.map((item, index) => (
          <ExpensiveComponent key={index} item={item} />
        ))}

        <h4>With ID Keys (Good Performance):</h4>
        {items.map((item) => (
          <ExpensiveComponent key={item.id} item={item} />
        ))}
      </div>
    </div>
  );
}

function ExpensiveComponent({ item }) {
  const renderCount = useRef(0);
  renderCount.current++;

  // Simulate expensive computation
  const expensiveValue = useMemo(() => {
    console.log(`Computing expensive value for ${item.text}`);
    let result = 0;
    for (let i = 0; i < 100000; i++) {
      result += i;
    }
    return result;
  }, [item.text]);

  return (
    <div style={{ background: renderCount.current > 1 ? 'red' : 'green' }}>
      {item.text} (Render #{renderCount.current}) - Expensive: {expensiveValue}
    </div>
  );
}

// 5. When Index Keys are Acceptable
function StaticListExample() {
  // ✅ OK to use index when:
  // - List is static (never changes)
  // - Items don't have unique IDs
  // - No reordering, adding, or removing

  const staticItems = ['Apple', 'Banana', 'Cherry']; // Never changes

  return (
    <ul>
      {staticItems.map((item, index) => (
        <li key={index}>{item}</li> // ✅ OK: list never changes
      ))}
    </ul>
  );
}

// 6. Complex Key Scenarios
function ComplexKeyExample() {
  const [todos, setTodos] = useState([
    { id: 1, text: 'Learn React', completed: false, category: 'learning' },
    { id: 2, text: 'Buy groceries', completed: true, category: 'personal' },
    { id: 3, text: 'Walk dog', completed: false, category: 'personal' }
  ]);

  // Grouped rendering
  const groupedTodos = useMemo(() => {
    return todos.reduce((groups, todo) => {
      if (!groups[todo.category]) {
        groups[todo.category] = [];
      }
      groups[todo.category].push(todo);
      return groups;
    }, {});
  }, [todos]);

  return (
    <div>
      {Object.entries(groupedTodos).map(([category, categoryTodos]) => (
        <div key={category}> {/* ✅ Category as key */}
          <h3>{category}</h3>
          {categoryTodos.map((todo) => (
            <div key={todo.id}> {/* ✅ Todo ID as key */}
              <input
                type="checkbox"
                checked={todo.completed}
                onChange={() => toggleTodo(todo.id)}
              />
              {todo.text}
            </div>
          ))}
        </div>
      ))}
    </div>
  );

  function toggleTodo(id) {
    setTodos(prev => prev.map(todo =>
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ));
  }
}

// 7. Virtual DOM Performance Tips
function PerformanceOptimizedList() {
  const [items, setItems] = useState([]);
  const [filter, setFilter] = useState('');

  // ✅ Memoize filtered items
  const filteredItems = useMemo(() => {
    return items.filter(item =>
      item.name.toLowerCase().includes(filter.toLowerCase())
    );
  }, [items, filter]);

  // ✅ Stable key generation
  const getItemKey = useCallback((item) => {
    // Use composite key if needed
    return `${item.id}-${item.version}`;
  }, []);

  return (
    <div>
      <input
        value={filter}
        onChange={(e) => setFilter(e.target.value)}
        placeholder="Filter items..."
      />

      <div>
        {filteredItems.map((item) => (
          <MemoizedItem
            key={getItemKey(item)} // ✅ Stable key function
            item={item}
          />
        ))}
      </div>
    </div>
  );
}

const MemoizedItem = memo(function Item({ item }) {
  return (
    <div>
      <h4>{item.name}</h4>
      <p>{item.description}</p>
    </div>
  );
});

// 8. Common Key Mistakes and Solutions
function KeyMistakesExample() {
  const [messages, setMessages] = useState([]);

  return (
    <div>
      {/* ❌ WRONG: Using random values */}
      {messages.map((msg) => (
        <div key={Math.random()}> {/* ❌ New key every render */}
          {msg.text}
        </div>
      ))}

      {/* ❌ WRONG: Using array index when order changes */}
      {messages.map((msg, index) => (
        <div key={index}> {/* ❌ Index changes when items move */}
          {msg.text}
        </div>
      ))}

      {/* ❌ WRONG: Non-unique keys */}
      {messages.map((msg) => (
        <div key={msg.type}> {/* ❌ Multiple messages of same type */}
          {msg.text}
        </div>
      ))}

      {/* ✅ CORRECT: Stable, unique identifiers */}
      {messages.map((msg) => (
        <div key={msg.id}> {/* ✅ Unique, stable ID */}
          {msg.text}
        </div>
      ))}
    </div>
  );
}
```

#### Q21: useRef vs useState, state vs props?

**Trả lời:**

```javascript
// 1. useRef vs useState - Fundamental Differences
import React, { useState, useRef, useEffect } from 'react';

function RefVsState() {
  // useState - triggers re-render when value changes
  const [count, setCount] = useState(0);

  // useRef - does NOT trigger re-render when value changes
  const countRef = useRef(0);
  const renderCount = useRef(0);

  // Track number of renders
  renderCount.current++;

  const incrementState = () => {
    setCount(prev => prev + 1); // ✅ Triggers re-render
    console.log('State updated, component will re-render');
  };

  const incrementRef = () => {
    countRef.current += 1; // ❌ No re-render triggered
    console.log('Ref updated, no re-render:', countRef.current);
  };

  console.log('Component rendered #', renderCount.current);

  return (
    <div>
      <h3>useState vs useRef</h3>
      <p>State count: {count}</p>
      <p>Ref count: {countRef.current}</p>
      <p>Render count: {renderCount.current}</p>

      <button onClick={incrementState}>Increment State (re-renders)</button>
      <button onClick={incrementRef}>Increment Ref (no re-render)</button>
    </div>
  );
}

// 2. useRef Use Cases
function RefUseCases() {
  // DOM references
  const inputRef = useRef(null);
  const divRef = useRef(null);

  // Previous values
  const [name, setName] = useState('');
  const prevNameRef = useRef('');

  // Mutable values that persist between renders
  const timerRef = useRef(null);
  const countRef = useRef(0);

  // Store previous value
  useEffect(() => {
    prevNameRef.current = name;
  });

  const focusInput = () => {
    inputRef.current?.focus();
  };

  const scrollToDiv = () => {
    divRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const startTimer = () => {
    if (timerRef.current) return; // Prevent multiple timers

    timerRef.current = setInterval(() => {
      countRef.current += 1;
      console.log('Timer count:', countRef.current);
    }, 1000);
  };

  const stopTimer = () => {
    if (timerRef.current) {
      clearInterval(timerRef.current);
      timerRef.current = null;
    }
  };

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      if (timerRef.current) {
        clearInterval(timerRef.current);
      }
    };
  }, []);

  return (
    <div>
      <h3>useRef Use Cases</h3>

      {/* DOM Reference */}
      <input
        ref={inputRef}
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Type your name"
      />
      <button onClick={focusInput}>Focus Input</button>

      {/* Previous Value */}
      <p>Current name: {name}</p>
      <p>Previous name: {prevNameRef.current}</p>

      {/* Timer Control */}
      <button onClick={startTimer}>Start Timer</button>
      <button onClick={stopTimer}>Stop Timer</button>
      <p>Timer count (check console): {countRef.current}</p>

      {/* Scroll Reference */}
      <div style={{ height: '200px', overflow: 'auto' }}>
        <div style={{ height: '500px' }}>Scroll content...</div>
        <div ref={divRef} style={{ background: 'yellow' }}>
          Target div for scrolling
        </div>
      </div>
      <button onClick={scrollToDiv}>Scroll to Yellow Div</button>
    </div>
  );
}

// 3. State vs Props - Complete Comparison
// Props (Properties) - Data passed from parent to child
function ParentComponent() {
  const [userRole, setUserRole] = useState('user');
  const [theme, setTheme] = useState('light');

  return (
    <div>
      <h3>Parent Component (manages state)</h3>
      <button onClick={() => setUserRole(userRole === 'user' ? 'admin' : 'user')}>
        Toggle Role: {userRole}
      </button>
      <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
        Toggle Theme: {theme}
      </button>

      {/* Pass state as props to child */}
      <ChildComponent
        role={userRole}        // ✅ Props: read-only in child
        theme={theme}          // ✅ Props: read-only in child
        onRoleChange={setUserRole}  // ✅ Function to update parent state
      />
    </div>
  );
}

function ChildComponent({ role, theme, onRoleChange }) {
  // ✅ Child has its own state
  const [message, setMessage] = useState('');
  const [isExpanded, setIsExpanded] = useState(false);

  // ❌ Can't directly modify props
  // role = 'admin'; // This won't work!

  // ✅ Can call parent function to update parent state
  const requestAdminAccess = () => {
    onRoleChange('admin');
  };

  return (
    <div style={{
      background: theme === 'light' ? '#fff' : '#333',
      color: theme === 'light' ? '#000' : '#fff',
      padding: '20px',
      margin: '20px'
    }}>
      <h4>Child Component (receives props)</h4>
      <p>Role from props: {role}</p>
      <p>Theme from props: {theme}</p>

      {/* Child's own state */}
      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Child's own message"
      />
      <p>Child's state: {message}</p>

      <button onClick={() => setIsExpanded(!isExpanded)}>
        {isExpanded ? 'Collapse' : 'Expand'} (Child State)
      </button>

      {isExpanded && (
        <div>
          <p>Expanded content controlled by child state</p>
          {role !== 'admin' && (
            <button onClick={requestAdminAccess}>
              Request Admin Access (Update Parent)
            </button>
          )}
        </div>
      )}
    </div>
  );
}

// 4. State Management Patterns
function StateManagementPatterns() {
  // Lifting state up example
  const [sharedData, setSharedData] = useState({
    cart: [],
    user: null,
    preferences: {}
  });

  // State that's local to this component
  const [localLoading, setLocalLoading] = useState(false);

  return (
    <div>
      <h3>State Management Patterns</h3>

      {/* Shared state passed as props */}
      <ShoppingCart
        cart={sharedData.cart}
        onUpdateCart={(newCart) => setSharedData(prev => ({ ...prev, cart: newCart }))}
      />

      <UserProfile
        user={sharedData.user}
        preferences={sharedData.preferences}
        onUpdateUser={(user) => setSharedData(prev => ({ ...prev, user }))}
      />

      {/* Local state not shared */}
      {localLoading && <div>Loading...</div>}
    </div>
  );
}

function ShoppingCart({ cart, onUpdateCart }) {
  // Local state for cart UI
  const [isMinimized, setIsMinimized] = useState(false);

  const addItem = (item) => {
    onUpdateCart([...cart, item]);
  };

  return (
    <div>
      <h4>Shopping Cart</h4>
      <button onClick={() => setIsMinimized(!isMinimized)}>
        {isMinimized ? 'Show' : 'Hide'} Cart
      </button>

      {!isMinimized && (
        <div>
          <p>Items: {cart.length}</p>
          <button onClick={() => addItem({ id: Date.now(), name: 'New Item' })}>
            Add Item
          </button>
        </div>
      )}
    </div>
  );
}

function UserProfile({ user, preferences, onUpdateUser }) {
  // Derived state from props
  const isLoggedIn = !!user;

  // Local form state
  const [formData, setFormData] = useState({
    name: user?.name || '',
    email: user?.email || ''
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    onUpdateUser({
      ...user,
      ...formData
    });
  };

  if (!isLoggedIn) {
    return <div>Please log in</div>;
  }

  return (
    <div>
      <h4>User Profile</h4>
      <form onSubmit={handleSubmit}>
        <input
          value={formData.name}
          onChange={(e) => setFormData(prev => ({ ...prev, name: e.target.value }))}
          placeholder="Name"
        />
        <input
          value={formData.email}
          onChange={(e) => setFormData(prev => ({ ...prev, email: e.target.value }))}
          placeholder="Email"
        />
        <button type="submit">Update Profile</button>
      </form>
    </div>
  );
}

// 5. When to use useState vs useRef
/*
Use useState when:
✅ Value changes should trigger re-renders
✅ Value is displayed in UI
✅ Value affects component appearance/behavior
✅ Need React to track changes for optimization

Use useRef when:
✅ Need to persist value between renders without re-rendering
✅ Storing DOM references
✅ Storing mutable values (timers, counters, flags)
✅ Storing previous values
✅ Caching expensive computations
✅ Preventing infinite loops in useEffect
*/

// 6. Anti-patterns and Best Practices
function AntiPatterns() {
  const [count, setCount] = useState(0);
  const badRef = useRef(0);

  // ❌ DON'T: Modify ref during render
  // badRef.current = count; // This can cause issues

  // ✅ DO: Modify ref in useEffect or event handlers
  useEffect(() => {
    badRef.current = count;
  });

  // ❌ DON'T: Use ref for values that should trigger re-renders
  const handleBadClick = () => {
    badRef.current += 1; // UI won't update
  };

  // ✅ DO: Use state for reactive values
  const handleGoodClick = () => {
    setCount(prev => prev + 1); // UI updates
  };

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={handleGoodClick}>Good: Use State</button>
      <button onClick={handleBadClick}>Bad: Use Ref</button>
    </div>
  );
}
```

#### Q22: useMemo vs useCallback chi tiết?

**Trả lời:**

**Giải thích:**
- **useMemo**: Cache kết quả của một phép tính (memoize value)
- **useCallback**: Cache một function (memoize function)
- **Mục đích**: Tối ưu performance bằng cách tránh tính toán/tạo function không cần thiết

```typescript
// 1. useMemo vs useCallback - Sự khác biệt cơ bản
import React, { useState, useMemo, useCallback, memo, ReactNode } from 'react';

interface MemoVsCallbackProps {}

function MemoVsCallback(): JSX.Element {
  const [count, setCount] = useState<number>(0);
  const [items, setItems] = useState<string[]>(['apple', 'banana', 'cherry']);
  const [multiplier, setMultiplier] = useState<number>(2);

  // ✅ useMemo - cache KẾT QUẢ của một phép tính
  const expensiveValue = useMemo<number>(() => {
    console.log('🔢 Đang tính toán giá trị đắt...');
    // Phép tính phức tạp - chỉ chạy lại khi dependencies thay đổi
    return items.reduce((sum, item) => sum + item.length, 0) * multiplier;
  }, [items, multiplier]); // Chỉ tính lại khi items hoặc multiplier thay đổi

  // ✅ useCallback - cache một FUNCTION
  const addItem = useCallback((): void => {
    console.log('🔧 Tạo function addItem...');
    setItems(prev => [...prev, `item-${Date.now()}`]);
  }, []); // Function reference không đổi qua các lần re-render

  // ❌ CÁCH SAI: Tạo function mới mỗi lần render
  const badAddItem = (): void => {
    console.log('❌ Tạo function mới mỗi lần render');
    setItems(prev => [...prev, `item-${Date.now()}`]);
  };

  console.log('🔄 Component rendered');

  return (
    <div>
      <h3>useMemo vs useCallback</h3>
      <p>Count: {count}</p>
      <p>Expensive Value: {expensiveValue}</p>
      <p>Items: {items.length}</p>

      <button onClick={() => setCount(count + 1)}>
        Increment Count (doesn't recompute expensive value)
      </button>
      <button onClick={() => setMultiplier(multiplier + 1)}>
        Change Multiplier (recomputes expensive value)
      </button>

      {/* Child components that receive callbacks */}
      <MemoizedChild
        onAddGood={addItem}     // ✅ Stable function reference
        onAddBad={badAddItem}   // ❌ New function every render
      />
    </div>
  );
}

// Child component with React.memo
const MemoizedChild = memo(function MemoizedChild({ onAddGood, onAddBad }) {
  console.log('👶 Child component rendered');

  return (
    <div style={{ background: '#f0f0f0', padding: '10px', margin: '10px' }}>
      <h4>Child Component</h4>
      <button onClick={onAddGood}>
        Add Item (Good - useCallback)
      </button>
      <button onClick={onAddBad}>
        Add Item (Bad - new function)
      </button>
    </div>
  );
});

// 2. Performance Comparison Examples
function PerformanceComparison() {
  const [filter, setFilter] = useState('');
  const [sortBy, setSortBy] = useState('name');
  const [users, setUsers] = useState([
    { id: 1, name: 'John Doe', age: 30, department: 'Engineering' },
    { id: 2, name: 'Jane Smith', age: 25, department: 'Design' },
    { id: 3, name: 'Bob Johnson', age: 35, department: 'Engineering' },
    { id: 4, name: 'Alice Brown', age: 28, department: 'Marketing' }
  ]);

  // ✅ GOOD: Memoized expensive computation
  const filteredAndSortedUsers = useMemo(() => {
    console.log('🔍 Filtering and sorting users...');

    let filtered = users.filter(user =>
      user.name.toLowerCase().includes(filter.toLowerCase()) ||
      user.department.toLowerCase().includes(filter.toLowerCase())
    );

    return filtered.sort((a, b) => {
      if (sortBy === 'name') return a.name.localeCompare(b.name);
      if (sortBy === 'age') return a.age - b.age;
      return a.department.localeCompare(b.department);
    });
  }, [users, filter, sortBy]); // Only recomputes when dependencies change

  // ✅ GOOD: Memoized callback functions
  const handleUserUpdate = useCallback((userId, updates) => {
    console.log('👥 Updating user...');
    setUsers(prev => prev.map(user =>
      user.id === userId ? { ...user, ...updates } : user
    ));
  }, []); // Stable function reference

  const handleUserDelete = useCallback((userId) => {
    console.log('🗑️ Deleting user...');
    setUsers(prev => prev.filter(user => user.id !== userId));
  }, []); // Stable function reference

  // ❌ BAD: Would recompute every render
  // const badFilteredUsers = users.filter(user =>
  //   user.name.toLowerCase().includes(filter.toLowerCase())
  // ).sort((a, b) => a.name.localeCompare(b.name));

  return (
    <div>
      <h3>Performance Comparison</h3>

      <input
        value={filter}
        onChange={(e) => setFilter(e.target.value)}
        placeholder="Filter users..."
      />

      <select value={sortBy} onChange={(e) => setSortBy(e.target.value)}>
        <option value="name">Sort by Name</option>
        <option value="age">Sort by Age</option>
        <option value="department">Sort by Department</option>
      </select>

      <div>
        <h4>Filtered Users ({filteredAndSortedUsers.length}):</h4>
        {filteredAndSortedUsers.map(user => (
          <UserCard
            key={user.id}
            user={user}
            onUpdate={handleUserUpdate}  // ✅ Stable callback
            onDelete={handleUserDelete}  // ✅ Stable callback
          />
        ))}
      </div>
    </div>
  );
}

const UserCard = memo(function UserCard({ user, onUpdate, onDelete }) {
  console.log(`👤 UserCard rendered for ${user.name}`);

  const handleAgeIncrement = useCallback(() => {
    onUpdate(user.id, { age: user.age + 1 });
  }, [user.id, user.age, onUpdate]);

  return (
    <div style={{
      border: '1px solid #ccc',
      padding: '10px',
      margin: '5px',
      background: '#fafafa'
    }}>
      <h5>{user.name}</h5>
      <p>Age: {user.age} | Department: {user.department}</p>
      <button onClick={handleAgeIncrement}>+1 Age</button>
      <button onClick={() => onDelete(user.id)}>Delete</button>
    </div>
  );
});

// 3. When to use useMemo
function UseMemoExamples() {
  const [searchTerm, setSearchTerm] = useState('');
  const [data, setData] = useState([]);
  const [threshold, setThreshold] = useState(10);

  // ✅ Expensive computation - good for useMemo
  const processedData = useMemo(() => {
    console.log('Processing large dataset...');
    return data
      .filter(item => item.value > threshold)
      .map(item => ({
        ...item,
        processed: true,
        score: item.value * 2.5,
        category: item.value > 50 ? 'high' : 'medium'
      }))
      .sort((a, b) => b.score - a.score);
  }, [data, threshold]);

  // ✅ Derived state - good for useMemo
  const statistics = useMemo(() => {
    if (processedData.length === 0) return null;

    return {
      total: processedData.length,
      average: processedData.reduce((sum, item) => sum + item.score, 0) / processedData.length,
      highest: Math.max(...processedData.map(item => item.score)),
      lowest: Math.min(...processedData.map(item => item.score))
    };
  }, [processedData]);

  // ✅ Complex object creation - good for useMemo
  const chartConfig = useMemo(() => ({
    type: 'bar',
    data: processedData.slice(0, 10),
    options: {
      responsive: true,
      scales: {
        y: { beginAtZero: true }
      }
    }
  }), [processedData]);

  // ❌ DON'T use useMemo for simple computations
  // const simpleComputation = useMemo(() => searchTerm.length, [searchTerm]);
  // ✅ DO this instead:
  const simpleComputation = searchTerm.length;

  return (
    <div>
      <h3>useMemo Examples</h3>
      <input
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        placeholder="Search..."
      />
      <input
        type="number"
        value={threshold}
        onChange={(e) => setThreshold(Number(e.target.value))}
      />

      <p>Simple computation: {simpleComputation}</p>
      <p>Processed items: {processedData.length}</p>

      {statistics && (
        <div>
          <h4>Statistics:</h4>
          <p>Average: {statistics.average.toFixed(2)}</p>
          <p>Range: {statistics.lowest} - {statistics.highest}</p>
        </div>
      )}
    </div>
  );
}

// 4. When to use useCallback
function UseCallbackExamples() {
  const [todos, setTodos] = useState([]);
  const [filter, setFilter] = useState('all');

  // ✅ Callback passed to child components - good for useCallback
  const addTodo = useCallback((text) => {
    const newTodo = {
      id: Date.now(),
      text,
      completed: false,
      createdAt: new Date()
    };
    setTodos(prev => [...prev, newTodo]);
  }, []); // No dependencies, function never changes

  const toggleTodo = useCallback((id) => {
    setTodos(prev => prev.map(todo =>
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ));
  }, []); // No dependencies, function never changes

  const deleteTodo = useCallback((id) => {
    setTodos(prev => prev.filter(todo => todo.id !== id));
  }, []); // No dependencies, function never changes

  // ✅ Callback with dependencies - good for useCallback
  const updateTodoText = useCallback((id, newText) => {
    setTodos(prev => prev.map(todo =>
      todo.id === id ? { ...todo, text: newText } : todo
    ));
  }, []); // Function recreated only when dependencies change

  // ✅ Event handler passed to multiple children - good for useCallback
  const handleBulkAction = useCallback((action) => {
    switch (action) {
      case 'complete-all':
        setTodos(prev => prev.map(todo => ({ ...todo, completed: true })));
        break;
      case 'delete-completed':
        setTodos(prev => prev.filter(todo => !todo.completed));
        break;
      case 'clear-all':
        setTodos([]);
        break;
    }
  }, []); // Stable function reference

  const filteredTodos = useMemo(() => {
    switch (filter) {
      case 'active': return todos.filter(todo => !todo.completed);
      case 'completed': return todos.filter(todo => todo.completed);
      default: return todos;
    }
  }, [todos, filter]);

  return (
    <div>
      <h3>useCallback Examples</h3>

      <TodoInput onAdd={addTodo} />
      <FilterButtons filter={filter} onFilterChange={setFilter} />
      <BulkActions onBulkAction={handleBulkAction} />

      <div>
        {filteredTodos.map(todo => (
          <TodoItem
            key={todo.id}
            todo={todo}
            onToggle={toggleTodo}
            onDelete={deleteTodo}
            onUpdate={updateTodoText}
          />
        ))}
      </div>
    </div>
  );
}

const TodoInput = memo(function TodoInput({ onAdd }) {
  const [text, setText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (text.trim()) {
      onAdd(text.trim());
      setText('');
    }
  };

  console.log('📝 TodoInput rendered');

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Add new todo..."
      />
      <button type="submit">Add</button>
    </form>
  );
});

const TodoItem = memo(function TodoItem({ todo, onToggle, onDelete, onUpdate }) {
  const [isEditing, setIsEditing] = useState(false);
  const [editText, setEditText] = useState(todo.text);

  console.log(`✅ TodoItem rendered for: ${todo.text}`);

  const handleSave = () => {
    onUpdate(todo.id, editText);
    setIsEditing(false);
  };

  return (
    <div style={{
      display: 'flex',
      alignItems: 'center',
      padding: '5px',
      background: todo.completed ? '#e8f5e8' : '#fff'
    }}>
      <input
        type="checkbox"
        checked={todo.completed}
        onChange={() => onToggle(todo.id)}
      />

      {isEditing ? (
        <input
          value={editText}
          onChange={(e) => setEditText(e.target.value)}
          onBlur={handleSave}
          onKeyPress={(e) => e.key === 'Enter' && handleSave()}
        />
      ) : (
        <span
          onClick={() => setIsEditing(true)}
          style={{
            textDecoration: todo.completed ? 'line-through' : 'none',
            cursor: 'pointer',
            flex: 1,
            padding: '5px'
          }}
        >
          {todo.text}
        </span>
      )}

      <button onClick={() => onDelete(todo.id)}>Delete</button>
    </div>
  );
});

// 5. Common Mistakes and Best Practices
function CommonMistakes() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');

  // ❌ MISTAKE: Unnecessary useMemo for simple values
  const badMemo = useMemo(() => count * 2, [count]); // Don't do this!

  // ✅ CORRECT: Simple computation, no memo needed
  const goodComputation = count * 2; // Do this instead

  // ❌ MISTAKE: useMemo with changing dependencies
  const badMemoWithFunction = useMemo(() => {
    return () => console.log('Hello'); // New function every time
  }, []); // Dependencies are wrong!

  // ✅ CORRECT: useCallback for function memoization
  const goodCallback = useCallback(() => {
    console.log('Hello');
  }, []);

  // ❌ MISTAKE: useCallback without memo child
  const unnecessaryCallback = useCallback(() => {
    console.log('This callback is not needed');
  }, []);

  return (
    <div>
      <h3>Common Mistakes</h3>
      <p>Count: {count}</p>
      <p>Simple computation: {goodComputation}</p>

      <button onClick={() => setCount(count + 1)}>Increment</button>

      {/* This child doesn't use memo, so useCallback is unnecessary */}
      <RegularChild onClick={unnecessaryCallback} />

      {/* This child uses memo, so useCallback is beneficial */}
      <MemoizedChildForCallback onClick={goodCallback} />
    </div>
  );
}

const RegularChild = ({ onClick }) => {
  console.log('Regular child rendered');
  return <button onClick={onClick}>Regular Child</button>;
};

const MemoizedChildForCallback = memo(({ onClick }) => {
  console.log('Memoized child rendered');
  return <button onClick={onClick}>Memoized Child</button>;
});

// 6. Performance Guidelines
/*
useMemo Guidelines:
✅ DO use for expensive computations
✅ DO use for derived state from props/state
✅ DO use for complex object creation
❌ DON'T use for simple calculations
❌ DON'T use if dependencies change every render
❌ DON'T use for primitive values

useCallback Guidelines:
✅ DO use for callbacks passed to memoized child components
✅ DO use for event handlers in dependency arrays
✅ DO use for functions that create closures
❌ DON'T use if child components aren't memoized
❌ DON'T use for functions that don't depend on props/state
❌ DON'T use if the function changes every render anyway
*/
```

#### Q23: Parent re-renders thì child có re-render? Cách optimize?

**Trả lời:**

```javascript
// 1. Default Behavior - Child ALWAYS re-renders when parent re-renders
import React, { useState, memo, useCallback, useMemo } from 'react';

function ParentWithAlwaysRerender() {
  const [parentCount, setParentCount] = useState(0);
  const [otherState, setOtherState] = useState('');

  console.log('🔄 Parent rendered');

  return (
    <div>
      <h3>Parent Component</h3>
      <p>Parent count: {parentCount}</p>
      <p>Other state: {otherState}</p>

      <button onClick={() => setParentCount(prev => prev + 1)}>
        Increment Parent Count
      </button>
      <button onClick={() => setOtherState('changed')}>
        Change Other State
      </button>

      {/* ❌ Child ALWAYS re-renders when parent re-renders */}
      <RegularChild value="static value" />
      <RegularChild value={parentCount} />
    </div>
  );
}

function RegularChild({ value }) {
  console.log('👶 Regular Child rendered with value:', value);

  return (
    <div style={{ background: '#ffeeee', padding: '10px', margin: '5px' }}>
      <p>Child value: {value}</p>
    </div>
  );
}

// 2. Optimization với React.memo
function ParentWithMemoization() {
  const [parentCount, setParentCount] = useState(0);
  const [otherState, setOtherState] = useState('');

  console.log('🔄 Parent rendered');

  return (
    <div>
      <h3>Parent with Memoized Children</h3>
      <p>Parent count: {parentCount}</p>
      <p>Other state: {otherState}</p>

      <button onClick={() => setParentCount(prev => prev + 1)}>
        Increment Parent Count
      </button>
      <button onClick={() => setOtherState('changed')}>
        Change Other State
      </button>

      {/* ✅ Only re-renders when value actually changes */}
      <MemoizedChild value="static value" />
      <MemoizedChild value={parentCount} />
    </div>
  );
}

const MemoizedChild = memo(function MemoizedChild({ value }) {
  console.log('👶 Memoized Child rendered with value:', value);

  return (
    <div style={{ background: '#eeffee', padding: '10px', margin: '5px' }}>
      <p>Memoized Child value: {value}</p>
    </div>
  );
});

// 3. Problem với Object/Array props
function ParentWithObjectProps() {
  const [count, setCount] = useState(0);

  // ❌ BAD: New object every render
  const badUserData = {
    name: 'John',
    age: 30
  };

  // ❌ BAD: New array every render
  const badItems = ['item1', 'item2', 'item3'];

  // ❌ BAD: New function every render
  const badCallback = () => {
    console.log('Button clicked');
  };

  console.log('🔄 Parent with objects rendered');

  return (
    <div>
      <h3>Parent with Object Props (Problem)</h3>
      <p>Count: {count}</p>
      <button onClick={() => setCount(prev => prev + 1)}>Increment</button>

      {/* ❌ Memo won't help - props are always "different" */}
      <MemoizedChildWithObjects
        user={badUserData}     // New object reference
        items={badItems}       // New array reference
        onClick={badCallback}  // New function reference
      />
    </div>
  );
}

const MemoizedChildWithObjects = memo(function MemoizedChildWithObjects({
  user,
  items,
  onClick
}) {
  console.log('👶 Child with objects rendered - memo didnt help!');

  return (
    <div style={{ background: '#ffeeaa', padding: '10px', margin: '5px' }}>
      <p>User: {user.name}, Age: {user.age}</p>
      <p>Items: {items.join(', ')}</p>
      <button onClick={onClick}>Click me</button>
    </div>
  );
});

// 4. Solution với useMemo và useCallback
function ParentWithOptimizedProps() {
  const [count, setCount] = useState(0);
  const [userName, setUserName] = useState('John');

  // ✅ GOOD: Stable object reference
  const userData = useMemo(() => ({
    name: userName,
    age: 30
  }), [userName]); // Only changes when userName changes

  // ✅ GOOD: Stable array reference
  const items = useMemo(() => ['item1', 'item2', 'item3'], []); // Never changes

  // ✅ GOOD: Stable function reference
  const handleClick = useCallback(() => {
    console.log('Button clicked');
  }, []); // Never changes

  console.log('🔄 Parent with optimized props rendered');

  return (
    <div>
      <h3>Parent with Optimized Props</h3>
      <p>Count: {count}</p>
      <button onClick={() => setCount(prev => prev + 1)}>
        Increment Count (child won't re-render)
      </button>
      <button onClick={() => setUserName(userName === 'John' ? 'Jane' : 'John')}>
        Change Name (child will re-render)
      </button>

      {/* ✅ Memo works properly now */}
      <MemoizedChildWithOptimizedProps
        user={userData}
        items={items}
        onClick={handleClick}
      />
    </div>
  );
}

const MemoizedChildWithOptimizedProps = memo(function MemoizedChildWithOptimizedProps({
  user,
  items,
  onClick
}) {
  console.log('👶 Optimized child rendered');

  return (
    <div style={{ background: '#aaffaa', padding: '10px', margin: '5px' }}>
      <p>User: {user.name}, Age: {user.age}</p>
      <p>Items: {items.join(', ')}</p>
      <button onClick={onClick}>Click me</button>
    </div>
  );
});

// 5. Advanced Optimization Patterns
function SmartParent() {
  const [globalCount, setGlobalCount] = useState(0);
  const [userFilter, setUserFilter] = useState('');
  const [users] = useState([
    { id: 1, name: 'John', department: 'Engineering' },
    { id: 2, name: 'Jane', department: 'Design' },
    { id: 3, name: 'Bob', department: 'Marketing' }
  ]);

  // ✅ Separate memoized computations
  const filteredUsers = useMemo(() => {
    console.log('🔍 Filtering users...');
    return users.filter(user =>
      user.name.toLowerCase().includes(userFilter.toLowerCase())
    );
  }, [users, userFilter]);

  const userStats = useMemo(() => {
    console.log('📊 Computing user stats...');
    return {
      total: users.length,
      engineering: users.filter(u => u.department === 'Engineering').length,
      design: users.filter(u => u.department === 'Design').length,
      marketing: users.filter(u => u.department === 'Marketing').length
    };
  }, [users]); // Independent of filter

  // ✅ Stable callbacks
  const handleUserSelect = useCallback((userId) => {
    console.log('User selected:', userId);
  }, []);

  console.log('🔄 Smart parent rendered');

  return (
    <div>
      <h3>Smart Parent with Optimizations</h3>

      <div>
        <p>Global count: {globalCount}</p>
        <button onClick={() => setGlobalCount(prev => prev + 1)}>
          Increment Global Count
        </button>
      </div>

      <div>
        <input
          value={userFilter}
          onChange={(e) => setUserFilter(e.target.value)}
          placeholder="Filter users..."
        />
      </div>

      {/* ✅ Independent components with different optimization strategies */}
      <UserList users={filteredUsers} onUserSelect={handleUserSelect} />
      <UserStats stats={userStats} />
      <GlobalCounter count={globalCount} />
    </div>
  );
}

// Component that depends on filtered data
const UserList = memo(function UserList({ users, onUserSelect }) {
  console.log('📋 UserList rendered with', users.length, 'users');

  return (
    <div style={{ background: '#e6f3ff', padding: '10px', margin: '5px' }}>
      <h4>User List ({users.length})</h4>
      {users.map(user => (
        <button
          key={user.id}
          onClick={() => onUserSelect(user.id)}
          style={{ margin: '2px', padding: '5px' }}
        >
          {user.name} - {user.department}
        </button>
      ))}
    </div>
  );
});

// Component that depends on stats (independent of filter)
const UserStats = memo(function UserStats({ stats }) {
  console.log('📊 UserStats rendered');

  return (
    <div style={{ background: '#fff3e6', padding: '10px', margin: '5px' }}>
      <h4>User Statistics</h4>
      <p>Total: {stats.total}</p>
      <p>Engineering: {stats.engineering}</p>
      <p>Design: {stats.design}</p>
      <p>Marketing: {stats.marketing}</p>
    </div>
  );
});

// Component that only depends on global state
const GlobalCounter = memo(function GlobalCounter({ count }) {
  console.log('🔢 GlobalCounter rendered');

  return (
    <div style={{ background: '#f0f0f0', padding: '10px', margin: '5px' }}>
      <h4>Global Counter: {count}</h4>
    </div>
  );
});

// 6. Custom memo with specific comparison
const ExpensiveChild = memo(function ExpensiveChild({ user, theme, data }) {
  console.log('💰 Expensive child rendered');

  // Simulate expensive computation
  const processedData = useMemo(() => {
    let result = 0;
    for (let i = 0; i < 100000; i++) {
      result += i;
    }
    return result + data.value;
  }, [data.value]);

  return (
    <div style={{
      background: theme === 'dark' ? '#333' : '#fff',
      color: theme === 'dark' ? '#fff' : '#000',
      padding: '10px',
      margin: '5px'
    }}>
      <h4>{user.name}</h4>
      <p>Processed: {processedData}</p>
    </div>
  );
}, (prevProps, nextProps) => {
  // Custom comparison function
  // Return true if props are equal (don't re-render)
  // Return false if props are different (do re-render)
  return (
    prevProps.user.id === nextProps.user.id &&
    prevProps.user.name === nextProps.user.name &&
    prevProps.theme === nextProps.theme &&
    prevProps.data.value === nextProps.data.value
  );
});

// 7. Summary of optimization strategies
/*
React Re-render Rules:
1. Parent re-renders → All children re-render (by default)
2. State change → Component re-renders
3. Props change → Component re-renders
4. Context change → All consumers re-render

Optimization Techniques:
✅ React.memo - Prevents re-render if props are the same
✅ useMemo - Memoizes expensive computations
✅ useCallback - Memoizes function references
✅ Split state - Separate fast-changing from slow-changing state
✅ Lift content up - Move static content to parent
✅ Custom comparison - memo with custom areEqual function

Performance Guidelines:
📝 Profile first, optimize second
📝 Don't optimize prematurely
📝 Measure the impact of optimizations
📝 Consider the cost of optimization vs benefit
📝 Sometimes re-rendering is fine and fast
*/
```

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
    </div>
  );
}
```

**Ưu điểm Functional Components:**
- Code ngắn gọn hơn
- Dễ test
- Performance tốt hơn
- Hooks cung cấp logic reuse tốt hơn

#### Q4: useState Hook hoạt động như thế nào?

**Trả lời:**
useState cho phép thêm state vào functional components.

```javascript
function Counter() {
  const [count, setCount] = useState(0);
  const [user, setUser] = useState({ name: '', email: '' });

  // Cập nhật đơn giản
  const increment = () => setCount(count + 1);

  // Cập nhật với function (tránh stale closure)
  const incrementCorrect = () => setCount(prevCount => prevCount + 1);

  // Cập nhật object state
  const updateUser = (field, value) => {
    setUser(prevUser => ({
      ...prevUser,
      [field]: value
    }));
  };

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>Increment</button>
      <button onClick={incrementCorrect}>Increment Correct</button>

      <input
        value={user.name}
        onChange={(e) => updateUser('name', e.target.value)}
        placeholder="Name"
      />
    </div>
  );
}
```

---

## Câu Hỏi Trung Cấp (Mid-Level)

### 3. Advanced React Concepts

#### Q5: useEffect Hook và lifecycle methods tương ứng?

**Trả lời:**

```javascript
function ComponentLifecycle() {
  const [count, setCount] = useState(0);
  const [user, setUser] = useState(null);

  // componentDidMount
  useEffect(() => {
    console.log('Component mounted');
    fetchUser();
  }, []); // Empty dependency array

  // componentDidUpdate cho count
  useEffect(() => {
    console.log('Count updated:', count);
    document.title = `Count: ${count}`;
  }, [count]); // Dependency array với count

  // componentWillUnmount
  useEffect(() => {
    const timer = setInterval(() => {
      console.log('Timer tick');
    }, 1000);

    return () => {
      console.log('Cleanup timer');
      clearInterval(timer);
    };
  }, []);

  // Combination của multiple effects
  useEffect(() => {
    if (user) {
      const subscription = subscribeToUserUpdates(user.id);
      return () => subscription.unsubscribe();
    }
  }, [user]);

  const fetchUser = async () => {
    try {
      const userData = await api.getUser();
      setUser(userData);
    } catch (error) {
      console.error('Failed to fetch user:', error);
    }
  };

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(c => c + 1)}>Increment</button>
      {user && <p>User: {user.name}</p>}
    </div>
  );
}
```

#### Q6: Custom Hooks - Cách tạo và sử dụng?

**Trả lời:**

```javascript
// Custom Hook: useLocalStorage
function useLocalStorage(key, initialValue) {
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error('Error reading localStorage:', error);
      return initialValue;
    }
  });

  const setValue = (value) => {
    try {
      const valueToStore = value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error('Error setting localStorage:', error);
    }
  };

  return [storedValue, setValue];
}

// Custom Hook: useFetch
function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const abortController = new AbortController();

    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await fetch(url, {
          signal: abortController.signal
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        setData(result);
        setError(null);
      } catch (err) {
        if (err.name !== 'AbortError') {
          setError(err.message);
        }
      } finally {
        setLoading(false);
      }
    };

    fetchData();

    return () => abortController.abort();
  }, [url]);

  return { data, loading, error };
}

// Sử dụng Custom Hooks
function UserProfile({ userId }) {
  const [preferences, setPreferences] = useLocalStorage('userPreferences', {});
  const { data: user, loading, error } = useFetch(`/api/users/${userId}`);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h1>{user.name}</h1>
      <p>Theme: {preferences.theme || 'light'}</p>
      <button
        onClick={() => setPreferences(prev => ({
          ...prev,
          theme: prev.theme === 'light' ? 'dark' : 'light'
        }))}
      >
        Toggle Theme
      </button>
    </div>
  );
}
```

#### Q7: Context API vs Redux - Khi nào nên sử dụng?

**Trả lời:**

```javascript
// Context API - Tốt cho state ít thay đổi
const ThemeContext = createContext();

function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');

  const value = {
    theme,
    toggleTheme: () => setTheme(prev => prev === 'light' ? 'dark' : 'light')
  };

  return (
    <ThemeContext.Provider value={value}>
      {children}
    </ThemeContext.Provider>
  );
}

function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within ThemeProvider');
  }
  return context;
}

// Redux - Tốt cho state phức tạp, nhiều thay đổi
const userSlice = createSlice({
  name: 'user',
  initialState: {
    profile: null,
    loading: false,
    error: null
  },
  reducers: {
    fetchUserStart: (state) => {
      state.loading = true;
      state.error = null;
    },
    fetchUserSuccess: (state, action) => {
      state.loading = false;
      state.profile = action.payload;
    },
    fetchUserFailure: (state, action) => {
      state.loading = false;
      state.error = action.payload;
    }
  }
});

// Async thunk
const fetchUser = createAsyncThunk(
  'user/fetchUser',
  async (userId, { rejectWithValue }) => {
    try {
      const response = await api.getUser(userId);
      return response.data;
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);
```

**Khi nào sử dụng:**
- **Context API**: Theme, user authentication, language settings
- **Redux**: Shopping cart, complex forms, real-time data updates

---

## Câu Hỏi Nâng Cao (Senior Level)

### 4. Performance & Optimization

#### Q8: React.memo, useMemo, useCallback - Khi nào và cách sử dụng?

**Trả lời:**

```javascript
// React.memo - Prevent unnecessary re-renders
const ExpensiveComponent = React.memo(({ data, onUpdate }) => {
  console.log('ExpensiveComponent rendered');

  return (
    <div>
      {data.map(item => (
        <div key={item.id} onClick={() => onUpdate(item.id)}>
          {item.name}
        </div>
      ))}
    </div>
  );
}, (prevProps, nextProps) => {
  // Custom comparison function (optional)
  return prevProps.data.length === nextProps.data.length &&
         prevProps.data.every((item, index) =>
           item.id === nextProps.data[index].id
         );
});

function ParentComponent() {
  const [count, setCount] = useState(0);
  const [items, setItems] = useState([
    { id: 1, name: 'Item 1' },
    { id: 2, name: 'Item 2' }
  ]);

  // useMemo - Memoize expensive calculations
  const expensiveValue = useMemo(() => {
    console.log('Calculating expensive value...');
    return items.reduce((sum, item) => sum + item.id, 0) * 1000;
  }, [items]);

  // useCallback - Memoize functions
  const handleUpdate = useCallback((itemId) => {
    setItems(prevItems =>
      prevItems.map(item =>
        item.id === itemId
          ? { ...item, name: `Updated ${item.name}` }
          : item
      )
    );
  }, []); // No dependencies needed since we use functional update

  // Without useCallback, this function is recreated on every render
  const handleUpdateBad = (itemId) => {
    setItems(prevItems =>
      prevItems.map(item =>
        item.id === itemId
          ? { ...item, name: `Updated ${item.name}` }
          : item
      )
    );
  };

  return (
    <div>
      <p>Count: {count}</p>
      <p>Expensive Value: {expensiveValue}</p>
      <button onClick={() => setCount(c => c + 1)}>
        Increment Count
      </button>

      <ExpensiveComponent
        data={items}
        onUpdate={handleUpdate}
      />
    </div>
  );
}
```

#### Q9: Code Splitting và Lazy Loading trong React?

**Trả lời:**

```javascript
import { lazy, Suspense } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

// Dynamic imports với React.lazy
const Home = lazy(() => import('./pages/Home'));
const Dashboard = lazy(() => import('./pages/Dashboard'));
const Profile = lazy(() =>
  import('./pages/Profile').then(module => ({
    default: module.Profile // Named export
  }))
);

// Component-level splitting
const HeavyChart = lazy(() =>
  import('./components/HeavyChart').then(module => {
    // Pre-load dependencies
    return Promise.all([
      module.default,
      import('./utils/chartHelpers')
    ]).then(([Component]) => ({ default: Component }));
  })
);

// Loading component
function LoadingSpinner() {
  return (
    <div className="loading-container">
      <div className="spinner">Loading...</div>
    </div>
  );
}

// Error Boundary cho lazy loading
class LazyLoadErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Lazy loading error:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div>
          <h2>Something went wrong loading this component.</h2>
          <button onClick={() => window.location.reload()}>
            Reload Page
          </button>
        </div>
      );
    }

    return this.props.children;
  }
}

// Main App với code splitting
function App() {
  return (
    <Router>
      <LazyLoadErrorBoundary>
        <Suspense fallback={<LoadingSpinner />}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/profile" element={<Profile />} />
          </Routes>
        </Suspense>
      </LazyLoadErrorBoundary>
    </Router>
  );
}

// Advanced: Dynamic import với conditions
function DynamicComponentLoader({ type, data }) {
  const [Component, setComponent] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadComponent = async () => {
      try {
        let module;
        switch (type) {
          case 'chart':
            module = await import('./components/Chart');
            break;
          case 'table':
            module = await import('./components/Table');
            break;
          case 'graph':
            module = await import('./components/Graph');
            break;
          default:
            module = await import('./components/Default');
        }
        setComponent(() => module.default);
      } catch (error) {
        console.error('Failed to load component:', error);
      } finally {
        setLoading(false);
      }
    };

    loadComponent();
  }, [type]);

  if (loading) return <LoadingSpinner />;
  if (!Component) return <div>Failed to load component</div>;

  return <Component data={data} />;
}
```

### 5. Advanced Patterns

#### Q10: Higher-Order Components (HOC) vs Render Props vs Custom Hooks?

**Trả lời:**

```javascript
// 1. Higher-Order Component (HOC)
function withAuth(WrappedComponent) {
  return function WithAuthComponent(props) {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
      const checkAuth = async () => {
        try {
          const userData = await authService.getCurrentUser();
          setUser(userData);
        } catch (error) {
          console.error('Auth check failed:', error);
        } finally {
          setLoading(false);
        }
      };

      checkAuth();
    }, []);

    if (loading) return <div>Checking authentication...</div>;
    if (!user) return <div>Please log in</div>;

    return <WrappedComponent {...props} user={user} />;
  };
}

// Sử dụng HOC
const ProtectedDashboard = withAuth(Dashboard);

// 2. Render Props Pattern
class AuthProvider extends React.Component {
  state = {
    user: null,
    loading: true,
    error: null
  };

  componentDidMount() {
    this.checkAuth();
  }

  checkAuth = async () => {
    try {
      const user = await authService.getCurrentUser();
      this.setState({ user, loading: false });
    } catch (error) {
      this.setState({ error: error.message, loading: false });
    }
  };

  render() {
    return this.props.children(this.state);
  }
}

// Sử dụng Render Props
function App() {
  return (
    <AuthProvider>
      {({ user, loading, error }) => {
        if (loading) return <div>Loading...</div>;
        if (error) return <div>Error: {error}</div>;
        if (!user) return <LoginForm />;

        return <Dashboard user={user} />;
      }}
    </AuthProvider>
  );
}

// 3. Custom Hook (Modern approach)
function useAuth() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let isMounted = true;

    const checkAuth = async () => {
      try {
        const userData = await authService.getCurrentUser();
        if (isMounted) {
          setUser(userData);
          setError(null);
        }
      } catch (err) {
        if (isMounted) {
          setError(err.message);
          setUser(null);
        }
      } finally {
        if (isMounted) {
          setLoading(false);
        }
      }
    };

    checkAuth();

    return () => {
      isMounted = false;
    };
  }, []);

  const login = async (credentials) => {
    setLoading(true);
    try {
      const userData = await authService.login(credentials);
      setUser(userData);
      setError(null);
      return userData;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  };

  const logout = async () => {
    try {
      await authService.logout();
      setUser(null);
    } catch (err) {
      setError(err.message);
    }
  };

  return {
    user,
    loading,
    error,
    login,
    logout,
    isAuthenticated: !!user
  };
}

// Sử dụng Custom Hook
function ProtectedRoute({ children }) {
  const { user, loading } = useAuth();

  if (loading) return <div>Loading...</div>;
  if (!user) return <Navigate to="/login" />;

  return children;
}
```

---

## Performance Optimization

### Q11: Virtual DOM vs Real DOM - Performance implications?

**Trả lời:**

```javascript
// Vấn đề với Direct DOM manipulation
function updateListBadly(items) {
  const container = document.getElementById('list-container');

  // Xóa tất cả elements (expensive)
  container.innerHTML = '';

  // Tạo lại tất cả elements (expensive)
  items.forEach(item => {
    const div = document.createElement('div');
    div.textContent = item.name;
    div.onclick = () => handleClick(item.id);
    container.appendChild(div); // Reflow/repaint cho mỗi append
  });
}

// React Virtual DOM approach
function OptimizedList({ items, onItemClick }) {
  return (
    <div>
      {items.map(item => (
        <ListItem
          key={item.id}
          item={item}
          onClick={onItemClick}
        />
      ))}
    </div>
  );
}

// Tối ưu hóa với React.memo và key props
const ListItem = React.memo(({ item, onClick }) => {
  return (
    <div
      className="list-item"
      onClick={() => onClick(item.id)}
    >
      {item.name}
    </div>
  );
});

// Advanced: Virtualization cho large lists
import { FixedSizeList as List } from 'react-window';

function VirtualizedList({ items, onItemClick }) {
  const Row = ({ index, style }) => (
    <div style={style}>
      <ListItem
        item={items[index]}
        onClick={onItemClick}
      />
    </div>
  );

  return (
    <List
      height={600}
      itemCount={items.length}
      itemSize={50}
      width="100%"
    >
      {Row}
    </List>
  );
}
```

### Q12: Bundle Optimization và Tree Shaking?

**Trả lời:**

```javascript
// Bad: Import entire library
import _ from 'lodash'; // Imports entire lodash (~70KB)
import * as MUI from '@mui/material'; // Imports everything

// Good: Import only needed functions
import { debounce, throttle } from 'lodash';
import { Button, TextField } from '@mui/material';

// Better: Use babel plugins for automatic optimization
// babel-plugin-lodash
import { debounce } from 'lodash'; // Automatically optimized to lodash/debounce

// Webpack Bundle Analyzer để identify large bundles
// npm install --save-dev webpack-bundle-analyzer

// Dynamic imports cho conditional loading
async function loadChartLibrary() {
  if (window.innerWidth > 768) {
    // Load full-featured chart for desktop
    const { Chart } = await import('./AdvancedChart');
    return Chart;
  } else {
    // Load lightweight chart for mobile
    const { SimpleChart } = await import('./SimpleChart');
    return SimpleChart;
  }
}

// Tree shaking friendly module structure
// utils/index.js
export { debounce } from './debounce';
export { throttle } from './throttle';
export { formatDate } from './formatDate';

// utils/debounce.js
export function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

// Webpack config cho production optimization
module.exports = {
  optimization: {
    usedExports: true, // Enable tree shaking
    sideEffects: false, // No side effects in modules
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all',
        },
        common: {
          name: 'common',
          minChunks: 2,
          chunks: 'all',
          enforce: true,
        },
      },
    },
  },
};
```

---

## Security Best Practices

### Q13: XSS Prevention trong React?

**Trả lời:**

```javascript
// React tự động escape JSX content, nhưng có exceptions:

// Safe: React automatically escapes
function SafeComponent({ userInput }) {
  return <div>{userInput}</div>; // Automatically escaped
}

// Dangerous: dangerouslySetInnerHTML
function DangerousComponent({ htmlContent }) {
  // NEVER do this with untrusted content
  return <div dangerouslySetInnerHTML={{ __html: htmlContent }} />;
}

// Safe approach: Sanitize HTML content
import DOMPurify from 'dompurify';

function SafeHTMLComponent({ htmlContent }) {
  const sanitizedHTML = DOMPurify.sanitize(htmlContent, {
    ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'p', 'br'],
    ALLOWED_ATTR: []
  });

  return <div dangerouslySetInnerHTML={{ __html: sanitizedHTML }} />;
}

// URL sanitization
function SafeLink({ href, children }) {
  const sanitizeURL = (url) => {
    try {
      const parsed = new URL(url);
      // Only allow http and https protocols
      if (!['http:', 'https:'].includes(parsed.protocol)) {
        return '#';
      }
      return url;
    } catch {
      return '#';
    }
  };

  return (
    <a
      href={sanitizeURL(href)}
      rel="noopener noreferrer"
      target="_blank"
    >
      {children}
    </a>
  );
}

// Input validation and sanitization
function SecureForm() {
  const [formData, setFormData] = useState({
    email: '',
    message: ''
  });
  const [errors, setErrors] = useState({});

  const validateInput = (field, value) => {
    const validators = {
      email: (val) => {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(val) ? null : 'Invalid email format';
      },
      message: (val) => {
        // Remove potentially dangerous characters
        const sanitized = val.replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '');
        return sanitized.length > 500 ? 'Message too long' : null;
      }
    };

    return validators[field] ? validators[field](value) : null;
  };

  const handleInputChange = (field, value) => {
    // Validate on change
    const error = validateInput(field, value);

    setFormData(prev => ({ ...prev, [field]: value }));
    setErrors(prev => ({ ...prev, [field]: error }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Final validation
    const newErrors = {};
    Object.keys(formData).forEach(field => {
      const error = validateInput(field, formData[field]);
      if (error) newErrors[field] = error;
    });

    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }

    // Submit with additional server-side validation
    try {
      await api.submitForm(formData);
    } catch (error) {
      console.error('Form submission failed:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="email"
        value={formData.email}
        onChange={(e) => handleInputChange('email', e.target.value)}
        placeholder="Email"
      />
      {errors.email && <span className="error">{errors.email}</span>}

      <textarea
        value={formData.message}
        onChange={(e) => handleInputChange('message', e.target.value)}
        placeholder="Message"
        maxLength={500}
      />
      {errors.message && <span className="error">{errors.message}</span>}

      <button type="submit">Submit</button>
    </form>
  );
}
```

### Q14: CSRF Protection và Secure API Calls?

**Trả lời:**

```javascript
// API service với security headers
class SecureAPIService {
  constructor() {
    this.baseURL = process.env.REACT_APP_API_URL;
    this.csrfToken = null;
  }

  async getCSRFToken() {
    if (!this.csrfToken) {
      const response = await fetch(`${this.baseURL}/csrf-token`, {
        credentials: 'include' // Include cookies
      });
      const data = await response.json();
      this.csrfToken = data.token;
    }
    return this.csrfToken;
  }

  async makeSecureRequest(endpoint, options = {}) {
    const token = await this.getCSRFToken();

    const defaultOptions = {
      credentials: 'include', // Include cookies for session
      headers: {
        'Content-Type': 'application/json',
        'X-CSRF-Token': token,
        'X-Requested-With': 'XMLHttpRequest', // CSRF protection
        ...options.headers
      }
    };

    const response = await fetch(`${this.baseURL}${endpoint}`, {
      ...defaultOptions,
      ...options
    });

    if (response.status === 403) {
      // CSRF token might be expired, refresh and retry
      this.csrfToken = null;
      return this.makeSecureRequest(endpoint, options);
    }

    if (!response.ok) {
      throw new Error(`API Error: ${response.status}`);
    }

    return response.json();
  }

  async post(endpoint, data) {
    return this.makeSecureRequest(endpoint, {
      method: 'POST',
      body: JSON.stringify(data)
    });
  }

  async put(endpoint, data) {
    return this.makeSecureRequest(endpoint, {
      method: 'PUT',
      body: JSON.stringify(data)
    });
  }

  async delete(endpoint) {
    return this.makeSecureRequest(endpoint, {
      method: 'DELETE'
    });
  }
}

// Secure authentication hook
function useSecureAuth() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Check authentication status on mount
    checkAuthStatus();

    // Set up token refresh interval
    const refreshInterval = setInterval(refreshToken, 15 * 60 * 1000); // 15 minutes

    return () => clearInterval(refreshInterval);
  }, []);

  const checkAuthStatus = async () => {
    try {
      const userData = await api.makeSecureRequest('/auth/me');
      setUser(userData);
    } catch (error) {
      setUser(null);
    } finally {
      setLoading(false);
    }
  };

  const refreshToken = async () => {
    try {
      await api.makeSecureRequest('/auth/refresh', { method: 'POST' });
    } catch (error) {
      // Refresh failed, redirect to login
      setUser(null);
      window.location.href = '/login';
    }
  };

  const login = async (credentials) => {
    try {
      const userData = await api.post('/auth/login', credentials);
      setUser(userData);
      return userData;
    } catch (error) {
      throw new Error('Login failed');
    }
  };

  const logout = async () => {
    try {
      await api.post('/auth/logout');
    } catch (error) {
      console.error('Logout error:', error);
    } finally {
      setUser(null);
      // Clear any sensitive data from localStorage
      localStorage.removeItem('userPreferences');
    }
  };

  return { user, loading, login, logout };
}

// Content Security Policy helper
function useCSP() {
  useEffect(() => {
    // Set CSP meta tag if not already set by server
    if (!document.querySelector('meta[http-equiv="Content-Security-Policy"]')) {
      const meta = document.createElement('meta');
      meta.httpEquiv = 'Content-Security-Policy';
      meta.content = `
        default-src 'self';
        script-src 'self' 'unsafe-inline' https://trusted-cdn.com;
        style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;
        img-src 'self' data: https://trusted-images.com;
        connect-src 'self' https://api.yourapp.com;
        font-src 'self' https://fonts.gstatic.com;
      `.replace(/\s+/g, ' ').trim();

      document.head.appendChild(meta);
    }
  }, []);
}
```

### Q15: Secure Data Storage và Privacy?

**Trả lời:**

```javascript
// Secure storage utility
class SecureStorage {
  static encrypt(data, key) {
    // Simple encryption (use proper library in production)
    const encoded = btoa(JSON.stringify(data));
    return encoded;
  }

  static decrypt(encryptedData, key) {
    try {
      const decoded = atob(encryptedData);
      return JSON.parse(decoded);
    } catch (error) {
      console.error('Decryption failed:', error);
      return null;
    }
  }

  static setSecureItem(key, value, options = {}) {
    try {
      const data = {
        value,
        timestamp: Date.now(),
        expires: options.expires ? Date.now() + options.expires : null
      };

      const encrypted = this.encrypt(data, key);

      if (options.session) {
        sessionStorage.setItem(key, encrypted);
      } else {
        localStorage.setItem(key, encrypted);
      }
    } catch (error) {
      console.error('Failed to store data:', error);
    }
  }

  static getSecureItem(key, options = {}) {
    try {
      const storage = options.session ? sessionStorage : localStorage;
      const encrypted = storage.getItem(key);

      if (!encrypted) return null;

      const data = this.decrypt(encrypted, key);

      if (!data) return null;

      // Check expiration
      if (data.expires && Date.now() > data.expires) {
        storage.removeItem(key);
        return null;
      }

      return data.value;
    } catch (error) {
      console.error('Failed to retrieve data:', error);
      return null;
    }
  }

  static removeSecureItem(key, options = {}) {
    const storage = options.session ? sessionStorage : localStorage;
    storage.removeItem(key);
  }

  static clearExpiredItems() {
    const checkStorage = (storage) => {
      const keys = Object.keys(storage);
      keys.forEach(key => {
        try {
          const encrypted = storage.getItem(key);
          const data = this.decrypt(encrypted, key);

          if (data && data.expires && Date.now() > data.expires) {
            storage.removeItem(key);
          }
        } catch (error) {
          // Invalid data, remove it
          storage.removeItem(key);
        }
      });
    };

    checkStorage(localStorage);
    checkStorage(sessionStorage);
  }
}

// Privacy-compliant data handling
function usePrivacyCompliantData() {
  const [consent, setConsent] = useState(null);
  const [userData, setUserData] = useState(null);

  useEffect(() => {
    // Check existing consent
    const existingConsent = SecureStorage.getSecureItem('user-consent');
    setConsent(existingConsent);

    // Clear expired items periodically
    const cleanup = setInterval(() => {
      SecureStorage.clearExpiredItems();
    }, 60 * 60 * 1000); // Every hour

    return () => clearInterval(cleanup);
  }, []);

  const requestConsent = async (purposes) => {
    // Show consent dialog
    const userConsent = await showConsentDialog(purposes);

    if (userConsent.analytics) {
      // Only store analytics data if consented
      setConsent(userConsent);
      SecureStorage.setSecureItem('user-consent', userConsent, {
        expires: 365 * 24 * 60 * 60 * 1000 // 1 year
      });
    }

    return userConsent;
  };

  const storeUserData = (data, sensitive = false) => {
    if (!consent?.necessary) {
      console.warn('Cannot store data without consent');
      return;
    }

    const options = sensitive ? { session: true } : {};
    SecureStorage.setSecureItem('user-data', data, options);
    setUserData(data);
  };

  const anonymizeData = (data) => {
    // Remove PII
    const anonymized = { ...data };
    delete anonymized.email;
    delete anonymized.phone;
    delete anonymized.address;

    // Hash sensitive identifiers
    if (anonymized.userId) {
      anonymized.userId = btoa(anonymized.userId).slice(0, 8);
    }

    return anonymized;
  };

  const clearUserData = () => {
    SecureStorage.removeSecureItem('user-data');
    SecureStorage.removeSecureItem('user-data', { session: true });
    SecureStorage.removeSecureItem('user-consent');
    setUserData(null);
    setConsent(null);
  };

  return {
    consent,
    userData,
    requestConsent,
    storeUserData,
    anonymizeData,
    clearUserData
  };
}

// Secure form handling with PII protection
function SecureUserForm() {
  const { consent, storeUserData, anonymizeData } = usePrivacyCompliantData();
  const [formData, setFormData] = useState({
    email: '',
    phone: '',
    preferences: {}
  });

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Validate consent for data processing
    if (!consent?.necessary) {
      alert('Please accept necessary cookies to proceed');
      return;
    }

    try {
      // Send full data to server (with encryption in transit)
      await api.post('/user/profile', formData);

      // Store only necessary data locally
      const localData = anonymizeData(formData);
      storeUserData(localData);

      // Store sensitive data in session only if needed
      if (consent.functionality) {
        storeUserData({ email: formData.email }, true);
      }

    } catch (error) {
      console.error('Form submission failed:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="email"
        value={formData.email}
        onChange={(e) => setFormData(prev => ({
          ...prev,
          email: e.target.value
        }))}
        placeholder="Email"
      />

      <input
        type="tel"
        value={formData.phone}
        onChange={(e) => setFormData(prev => ({
          ...prev,
          phone: e.target.value
        }))}
        placeholder="Phone"
      />

      <button type="submit">Submit</button>

      {!consent && (
        <div className="consent-notice">
          We need your consent to process this data.
          <button onClick={() => requestConsent(['necessary', 'functionality'])}>
            Manage Preferences
          </button>
        </div>
      )}
    </form>
  );
}
```

---

## Expert Level (Lead/Architect)

### 6. System Design & Architecture

#### Q16: Thiết kế kiến trúc Micro-frontend cho ứng dụng scale lớn?

**Trả lời:**

```javascript
// 1. Module Federation với Webpack 5
// Host Application (Shell)
const ModuleFederationPlugin = require('@module-federation/webpack');

module.exports = {
  mode: 'development',
  devServer: { port: 3000 },
  plugins: [
    new ModuleFederationPlugin({
      name: 'shell',
      remotes: {
        userModule: 'userModule@http://localhost:3001/remoteEntry.js',
        orderModule: 'orderModule@http://localhost:3002/remoteEntry.js',
        paymentModule: 'paymentModule@http://localhost:3003/remoteEntry.js',
      },
      shared: {
        react: { singleton: true, eager: true },
        'react-dom': { singleton: true, eager: true },
        '@reduxjs/toolkit': { singleton: true },
      },
    }),
  ],
};

// Shell App Component
function ShellApp() {
  const [currentModule, setCurrentModule] = useState('user');
  const [moduleError, setModuleError] = useState(null);

  // Dynamic module loading với error handling
  const loadModule = async (moduleName) => {
    try {
      setModuleError(null);

      const moduleMap = {
        user: () => import('userModule/UserApp'),
        order: () => import('orderModule/OrderApp'),
        payment: () => import('paymentModule/PaymentApp'),
      };

      const Module = await moduleMap[moduleName]();
      return Module.default;
    } catch (error) {
      console.error(`Failed to load module: ${moduleName}`, error);
      setModuleError(error.message);
      return () => <div>Module failed to load: {error.message}</div>;
    }
  };

  return (
    <ErrorBoundary>
      <div className="shell-app">
        <GlobalNavigation onModuleChange={setCurrentModule} />
        <Suspense fallback={<ModuleLoadingSpinner />}>
          <ModuleContainer
            moduleName={currentModule}
            loadModule={loadModule}
            error={moduleError}
          />
        </Suspense>
      </div>
    </ErrorBoundary>
  );
}

// 2. Event-driven communication giữa micro-frontends
class MicroFrontendEventBus {
  constructor() {
    this.events = new Map();
    this.middleware = [];
  }

  // Middleware cho logging, validation, etc.
  use(middleware) {
    this.middleware.push(middleware);
  }

  subscribe(eventName, callback, options = {}) {
    if (!this.events.has(eventName)) {
      this.events.set(eventName, new Set());
    }

    const wrappedCallback = (data) => {
      // Apply middleware
      let processedData = data;
      for (const middleware of this.middleware) {
        processedData = middleware(eventName, processedData, 'subscribe');
      }

      if (options.once) {
        this.events.get(eventName).delete(wrappedCallback);
      }

      callback(processedData);
    };

    this.events.get(eventName).add(wrappedCallback);

    return () => this.events.get(eventName)?.delete(wrappedCallback);
  }

  emit(eventName, data, options = {}) {
    // Apply middleware
    let processedData = data;
    for (const middleware of this.middleware) {
      processedData = middleware(eventName, processedData, 'emit');
    }

    const callbacks = this.events.get(eventName);
    if (callbacks) {
      if (options.async) {
        setTimeout(() => {
          callbacks.forEach(callback => callback(processedData));
        }, 0);
      } else {
        callbacks.forEach(callback => callback(processedData));
      }
    }
  }

  // Cross-domain messaging cho isolated micro-frontends
  emitCrossDomain(targetOrigin, eventName, data) {
    window.postMessage({
      type: 'MICRO_FRONTEND_EVENT',
      eventName,
      data,
      timestamp: Date.now(),
      source: window.location.origin
    }, targetOrigin);
  }
}

// Global event bus instance
window.MFEventBus = new MicroFrontendEventBus();

// Logging middleware
window.MFEventBus.use((eventName, data, type) => {
  console.log(`[MF EventBus] ${type}: ${eventName}`, data);
  return data;
});

// 3. Shared state management across micro-frontends
class SharedStateManager {
  constructor() {
    this.stores = new Map();
    this.subscribers = new Map();
  }

  createStore(storeId, initialState, reducer) {
    const store = {
      state: initialState,
      reducer,
      dispatch: (action) => {
        const newState = reducer(store.state, action);
        if (newState !== store.state) {
          store.state = newState;
          this.notifySubscribers(storeId, newState);

          // Persist critical state
          if (action.type.includes('PERSIST')) {
            localStorage.setItem(`mf_state_${storeId}`, JSON.stringify(newState));
          }
        }
      }
    };

    this.stores.set(storeId, store);
    return store;
  }

  subscribe(storeId, callback) {
    if (!this.subscribers.has(storeId)) {
      this.subscribers.set(storeId, new Set());
    }
    this.subscribers.get(storeId).add(callback);

    return () => this.subscribers.get(storeId)?.delete(callback);
  }

  getState(storeId) {
    return this.stores.get(storeId)?.state;
  }

  notifySubscribers(storeId, newState) {
    const callbacks = this.subscribers.get(storeId);
    if (callbacks) {
      callbacks.forEach(callback => callback(newState));
    }
  }

  // Cross-micro-frontend state sync
  syncState(storeId, targetOrigins) {
    const state = this.getState(storeId);
    targetOrigins.forEach(origin => {
      window.MFEventBus.emitCrossDomain(origin, 'STATE_SYNC', {
        storeId,
        state
      });
    });
  }
}

// Usage trong micro-frontend
function useSharedState(storeId) {
  const [state, setState] = useState(() =>
    window.SharedStateManager.getState(storeId)
  );

  useEffect(() => {
    const unsubscribe = window.SharedStateManager.subscribe(storeId, setState);
    return unsubscribe;
  }, [storeId]);

  const dispatch = useCallback((action) => {
    const store = window.SharedStateManager.stores.get(storeId);
    store?.dispatch(action);
  }, [storeId]);

  return [state, dispatch];
}
```

#### Q17: Implement advanced caching strategies cho production apps?

**Trả lời:**

```javascript
// 1. Multi-layer caching system
class AdvancedCacheManager {
  constructor() {
    this.memoryCache = new Map();
    this.browserCache = new Map();
    this.networkCache = new Map();
    this.cacheStats = {
      hits: 0,
      misses: 0,
      evictions: 0
    };

    // Cache configuration
    this.config = {
      memoryLimit: 50 * 1024 * 1024, // 50MB
      ttl: {
        short: 5 * 60 * 1000,     // 5 minutes
        medium: 30 * 60 * 1000,   // 30 minutes
        long: 24 * 60 * 60 * 1000  // 24 hours
      },
      maxEntries: 1000
    };

    this.setupPerformanceMonitoring();
    this.setupAutomaticCleanup();
  }

  async get(key, fetchFn, options = {}) {
    const startTime = performance.now();

    try {
      // 1. Try memory cache first (fastest)
      const memoryResult = this.getFromMemory(key);
      if (memoryResult) {
        this.recordCacheHit('memory', performance.now() - startTime);
        return memoryResult.data;
      }

      // 2. Try browser cache (IndexedDB/localStorage)
      const browserResult = await this.getFromBrowserCache(key);
      if (browserResult && !this.isExpired(browserResult)) {
        // Promote to memory cache
        this.setInMemory(key, browserResult.data, options);
        this.recordCacheHit('browser', performance.now() - startTime);
        return browserResult.data;
      }

      // 3. Try network cache (with stale-while-revalidate)
      const networkResult = await this.getFromNetworkCache(key);
      if (networkResult && options.staleWhileRevalidate) {
        // Serve stale data while fetching fresh
        this.revalidateInBackground(key, fetchFn, options);
        this.recordCacheHit('network-stale', performance.now() - startTime);
        return networkResult.data;
      }

      // 4. Fetch fresh data
      this.recordCacheMiss(performance.now() - startTime);
      const freshData = await this.fetchWithRetry(fetchFn, options);

      // Store in all cache layers
      await this.setMultiLayer(key, freshData, options);

      return freshData;

    } catch (error) {
      // Fallback to any available cached data
      const fallbackData = await this.getFallbackData(key);
      if (fallbackData) {
        console.warn('Using fallback cache data due to error:', error);
        return fallbackData;
      }
      throw error;
    }
  }

  setMultiLayer(key, data, options = {}) {
    const cacheEntry = {
      data,
      timestamp: Date.now(),
      ttl: options.ttl || this.config.ttl.medium,
      tags: options.tags || [],
      size: this.calculateSize(data)
    };

    // Memory cache
    this.setInMemory(key, cacheEntry, options);

    // Browser cache (async)
    this.setInBrowserCache(key, cacheEntry);

    // Network cache headers
    if (options.networkCache) {
      this.setNetworkCacheHeaders(options.networkCache);
    }
  }

  // LRU eviction with memory pressure awareness
  setInMemory(key, entry, options = {}) {
    if (this.shouldEvictMemory()) {
      this.evictLRU();
    }

    this.memoryCache.set(key, {
      ...entry,
      lastAccessed: Date.now(),
      accessCount: 0
    });
  }

  shouldEvictMemory() {
    const currentSize = this.calculateTotalMemorySize();
    const memoryPressure = this.getMemoryPressure();

    return (
      currentSize > this.config.memoryLimit ||
      this.memoryCache.size > this.config.maxEntries ||
      memoryPressure > 0.8
    );
  }

  evictLRU() {
    const entries = Array.from(this.memoryCache.entries())
      .sort((a, b) => {
        // Smart eviction: consider access frequency and recency
        const scoreA = a[1].accessCount / (Date.now() - a[1].lastAccessed);
        const scoreB = b[1].accessCount / (Date.now() - b[1].lastAccessed);
        return scoreA - scoreB;
      });

    const toEvict = Math.ceil(entries.length * 0.2); // Evict 20%
    for (let i = 0; i < toEvict; i++) {
      this.memoryCache.delete(entries[i][0]);
      this.cacheStats.evictions++;
    }
  }

  // Intelligent prefetching
  async prefetch(keys, fetchFns, options = {}) {
    const prefetchPromises = keys.map(async (key, index) => {
      try {
        // Only prefetch if not in cache and browser is idle
        if (!this.memoryCache.has(key) && this.isBrowserIdle()) {
          const data = await fetchFns[index]();
          await this.setMultiLayer(key, data, {
            ...options,
            ttl: this.config.ttl.long
          });
        }
      } catch (error) {
        console.warn(`Prefetch failed for ${key}:`, error);
      }
    });

    return Promise.allSettled(prefetchPromises);
  }

  // Cache invalidation với tags
  invalidateByTags(tags) {
    const toInvalidate = [];

    for (const [key, entry] of this.memoryCache.entries()) {
      if (entry.tags?.some(tag => tags.includes(tag))) {
        toInvalidate.push(key);
      }
    }

    toInvalidate.forEach(key => {
      this.memoryCache.delete(key);
      this.invalidateBrowserCache(key);
    });

    return toInvalidate.length;
  }

  // Performance monitoring
  setupPerformanceMonitoring() {
    setInterval(() => {
      const stats = this.getCacheStats();

      // Report metrics to analytics
      if (window.analytics) {
        window.analytics.track('Cache Performance', stats);
      }

      // Auto-tune cache based on performance
      this.autoTuneCache(stats);
    }, 60000); // Every minute
  }

  getCacheStats() {
    const hitRate = this.cacheStats.hits / (this.cacheStats.hits + this.cacheStats.misses);

    return {
      hitRate,
      memoryUsage: this.calculateTotalMemorySize(),
      entryCount: this.memoryCache.size,
      evictionRate: this.cacheStats.evictions / this.cacheStats.hits,
      averageAccessTime: this.averageAccessTime
    };
  }
}

// 2. Service Worker caching với advanced strategies
// sw.js
class ServiceWorkerCacheStrategy {
  constructor() {
    this.caches = {
      static: 'static-v1',
      dynamic: 'dynamic-v1',
      api: 'api-v1'
    };

    this.strategies = {
      staleWhileRevalidate: this.staleWhileRevalidate.bind(this),
      cacheFirst: this.cacheFirst.bind(this),
      networkFirst: this.networkFirst.bind(this),
      networkOnly: this.networkOnly.bind(this),
      cacheOnly: this.cacheOnly.bind(this)
    };
  }

  async handleRequest(event) {
    const { request } = event;
    const url = new URL(request.url);

    // Route-based caching strategy
    if (url.pathname.startsWith('/api/')) {
      return this.handleAPIRequest(request);
    } else if (url.pathname.match(/\.(js|css|png|jpg|jpeg|svg|woff2)$/)) {
      return this.strategies.cacheFirst(request, this.caches.static);
    } else {
      return this.strategies.staleWhileRevalidate(request, this.caches.dynamic);
    }
  }

  async handleAPIRequest(request) {
    const url = new URL(request.url);

    // Different strategies for different API endpoints
    if (url.pathname.includes('/user/profile')) {
      return this.strategies.staleWhileRevalidate(request, this.caches.api);
    } else if (url.pathname.includes('/static-data')) {
      return this.strategies.cacheFirst(request, this.caches.api);
    } else if (url.pathname.includes('/real-time')) {
      return this.strategies.networkFirst(request, this.caches.api);
    } else {
      return this.strategies.networkOnly(request);
    }
  }

  async staleWhileRevalidate(request, cacheName) {
    const cache = await caches.open(cacheName);
    const cachedResponse = await cache.match(request);

    const fetchPromise = fetch(request).then(async (response) => {
      if (response.ok) {
        // Clone before caching
        const responseClone = response.clone();
        await cache.put(request, responseClone);
      }
      return response;
    });

    // Return cached version immediately if available
    return cachedResponse || fetchPromise;
  }

  async cacheFirst(request, cacheName) {
    const cache = await caches.open(cacheName);
    const cachedResponse = await cache.match(request);

    if (cachedResponse) {
      return cachedResponse;
    }

    const response = await fetch(request);
    if (response.ok) {
      await cache.put(request, response.clone());
    }

    return response;
  }

  async networkFirst(request, cacheName) {
    try {
      const response = await fetch(request);

      if (response.ok) {
        const cache = await caches.open(cacheName);
        await cache.put(request, response.clone());
      }

      return response;
    } catch (error) {
      const cache = await caches.open(cacheName);
      const cachedResponse = await cache.match(request);

      if (cachedResponse) {
        return cachedResponse;
      }

      throw error;
    }
  }
}

// 3. React Query với advanced configuration
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 5 * 60 * 1000, // 5 minutes
      cacheTime: 30 * 60 * 1000, // 30 minutes
      refetchOnWindowFocus: false,
      refetchOnReconnect: true,
      retry: (failureCount, error) => {
        // Custom retry logic
        if (error.status === 404) return false;
        return failureCount < 3;
      },
      retryDelay: (attemptIndex) => Math.min(1000 * 2 ** attemptIndex, 30000),
    },
    mutations: {
      retry: 1,
      onError: (error) => {
        // Global error handling
        console.error('Mutation error:', error);
      }
    }
  }
});

// Custom hook với intelligent caching
function useAdvancedQuery(key, fetcher, options = {}) {
  const [isOnline, setIsOnline] = useState(navigator.onLine);

  useEffect(() => {
    const handleOnline = () => setIsOnline(true);
    const handleOffline = () => setIsOnline(false);

    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);

    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, []);

  return useQuery({
    queryKey: key,
    queryFn: fetcher,
    enabled: isOnline,
    ...options,
    staleTime: options.staleTime || (isOnline ? 5 * 60 * 1000 : Infinity),
    cacheTime: options.cacheTime || 30 * 60 * 1000,
  });
}
```

#### Q18: Design Pattern cho large-scale React applications?

**Trả lời:**

```javascript
// 1. Feature-Slice Design Architecture
// features/user/model/store.js
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

export const fetchUser = createAsyncThunk(
  'user/fetchUser',
  async (userId, { rejectWithValue, getState, dispatch }) => {
    try {
      const response = await userAPI.getUser(userId);

      // Side effects - update related features
      dispatch(notificationsModel.actions.markAsRead({
        userId: response.id
      }));

      return response;
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

const userSlice = createSlice({
  name: 'user',
  initialState: {
    entities: {},
    loading: false,
    error: null,
    currentUserId: null
  },
  reducers: {
    setCurrentUser: (state, action) => {
      state.currentUserId = action.payload;
    },
    updateUserProfile: (state, action) => {
      const { userId, updates } = action.payload;
      if (state.entities[userId]) {
        Object.assign(state.entities[userId], updates);
      }
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchUser.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchUser.fulfilled, (state, action) => {
        state.loading = false;
        state.entities[action.payload.id] = action.payload;
      })
      .addCase(fetchUser.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      });
  }
});

export const userModel = {
  actions: userSlice.actions,
  reducer: userSlice.reducer,
  selectors: {
    selectUser: (state, userId) => state.user.entities[userId],
    selectCurrentUser: (state) =>
      state.user.entities[state.user.currentUserId],
    selectIsLoading: (state) => state.user.loading,
    selectError: (state) => state.user.error
  },
  thunks: { fetchUser }
};

// 2. Advanced Component Composition Patterns
// Compound Components với Context
const AccordionContext = createContext();

function useAccordion() {
  const context = useContext(AccordionContext);
  if (!context) {
    throw new Error('Accordion components must be used within Accordion');
  }
  return context;
}

function Accordion({ children, allowMultiple = false, defaultOpenItems = [] }) {
  const [openItems, setOpenItems] = useState(new Set(defaultOpenItems));

  const toggleItem = useCallback((itemId) => {
    setOpenItems(prev => {
      const newSet = new Set(prev);

      if (newSet.has(itemId)) {
        newSet.delete(itemId);
      } else {
        if (!allowMultiple) {
          newSet.clear();
        }
        newSet.add(itemId);
      }

      return newSet;
    });
  }, [allowMultiple]);

  const contextValue = useMemo(() => ({
    openItems,
    toggleItem,
    allowMultiple
  }), [openItems, toggleItem, allowMultiple]);

  return (
    <AccordionContext.Provider value={contextValue}>
      <div className="accordion">{children}</div>
    </AccordionContext.Provider>
  );
}

Accordion.Item = function AccordionItem({ id, children }) {
  const { openItems } = useAccordion();
  const isOpen = openItems.has(id);

  return (
    <div className={`accordion-item ${isOpen ? 'open' : ''}`}>
      {typeof children === 'function' ? children({ isOpen }) : children}
    </div>
  );
};

Accordion.Trigger = function AccordionTrigger({ itemId, children }) {
  const { toggleItem } = useAccordion();

  return (
    <button
      className="accordion-trigger"
      onClick={() => toggleItem(itemId)}
      aria-expanded={openItems.has(itemId)}
    >
      {children}
    </button>
  );
};

Accordion.Content = function AccordionContent({ itemId, children }) {
  const { openItems } = useAccordion();
  const isOpen = openItems.has(itemId);

  return (
    <div
      className="accordion-content"
      style={{ display: isOpen ? 'block' : 'none' }}
    >
      {children}
    </div>
  );
};

// Usage
function FAQSection() {
  return (
    <Accordion allowMultiple>
      <Accordion.Item id="item1">
        {({ isOpen }) => (
          <>
            <Accordion.Trigger itemId="item1">
              What is React? {isOpen ? '−' : '+'}
            </Accordion.Trigger>
            <Accordion.Content itemId="item1">
              React is a JavaScript library...
            </Accordion.Content>
          </>
        )}
      </Accordion.Item>
    </Accordion>
  );
}

// 3. Advanced State Management Pattern - Event Sourcing
class EventStore {
  constructor() {
    this.events = [];
    this.snapshots = new Map();
    this.projections = new Map();
    this.subscribers = new Set();
  }

  append(event) {
    const eventWithMeta = {
      ...event,
      id: generateUUID(),
      timestamp: Date.now(),
      version: this.events.length + 1
    };

    this.events.push(eventWithMeta);
    this.notifySubscribers(eventWithMeta);

    // Create snapshot every N events for performance
    if (this.events.length % 100 === 0) {
      this.createSnapshot();
    }

    return eventWithMeta;
  }

  replay(fromVersion = 0) {
    const eventsToReplay = this.events.slice(fromVersion);

    // Start from latest snapshot if available
    const latestSnapshot = this.getLatestSnapshot(fromVersion);
    let state = latestSnapshot?.state || this.getInitialState();

    return eventsToReplay.reduce((currentState, event) => {
      return this.applyEvent(currentState, event);
    }, state);
  }

  createProjection(name, reducer, fromVersion = 0) {
    const initialState = this.getInitialProjectionState(name);
    const state = this.events
      .slice(fromVersion)
      .reduce(reducer, initialState);

    this.projections.set(name, state);
    return state;
  }

  subscribe(callback) {
    this.subscribers.add(callback);
    return () => this.subscribers.delete(callback);
  }

  notifySubscribers(event) {
    this.subscribers.forEach(callback => callback(event));
  }
}

// Event-sourced User aggregate
class UserAggregate {
  constructor(eventStore) {
    this.eventStore = eventStore;
    this.state = {
      users: {},
      currentUserId: null
    };
  }

  // Commands (intent to change state)
  createUser(userData) {
    const event = {
      type: 'USER_CREATED',
      payload: {
        userId: generateUUID(),
        ...userData,
        createdAt: Date.now()
      }
    };

    this.eventStore.append(event);
    return event.payload.userId;
  }

  updateUserProfile(userId, updates) {
    if (!this.state.users[userId]) {
      throw new Error('User not found');
    }

    const event = {
      type: 'USER_PROFILE_UPDATED',
      payload: {
        userId,
        updates,
        updatedAt: Date.now()
      }
    };

    this.eventStore.append(event);
  }

  // Event handlers (how state changes)
  applyEvent(state, event) {
    switch (event.type) {
      case 'USER_CREATED':
        return {
          ...state,
          users: {
            ...state.users,
            [event.payload.userId]: event.payload
          }
        };

      case 'USER_PROFILE_UPDATED':
        return {
          ...state,
          users: {
            ...state.users,
            [event.payload.userId]: {
              ...state.users[event.payload.userId],
              ...event.payload.updates
            }
          }
        };

      default:
        return state;
    }
  }

  // Query current state
  getUser(userId) {
    return this.state.users[userId];
  }

  getAllUsers() {
    return Object.values(this.state.users);
  }
}

// React integration
function useEventSourcingState(aggregate) {
  const [state, setState] = useState(aggregate.state);

  useEffect(() => {
    const unsubscribe = aggregate.eventStore.subscribe((event) => {
      setState(prevState => aggregate.applyEvent(prevState, event));
    });

    return unsubscribe;
  }, [aggregate]);

  return state;
}

// 4. Advanced Error Boundary với Recovery Strategies
class AdvancedErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      hasError: false,
      error: null,
      errorInfo: null,
      retryCount: 0,
      errorId: null
    };
  }

  static getDerivedStateFromError(error) {
    return {
      hasError: true,
      error,
      errorId: generateUUID()
    };
  }

  componentDidCatch(error, errorInfo) {
    this.setState({ errorInfo });

    // Advanced error reporting
    this.reportError(error, errorInfo);

    // Attempt automatic recovery for certain error types
    this.attemptRecovery(error);
  }

  reportError(error, errorInfo) {
    const errorReport = {
      message: error.message,
      stack: error.stack,
      componentStack: errorInfo.componentStack,
      timestamp: Date.now(),
      url: window.location.href,
      userAgent: navigator.userAgent,
      userId: this.props.userId,
      sessionId: this.props.sessionId,
      buildVersion: process.env.REACT_APP_VERSION
    };

    // Send to error reporting service
    if (window.errorReporter) {
      window.errorReporter.captureException(error, {
        extra: errorReport,
        tags: {
          component: this.props.name || 'UnknownComponent',
          severity: this.getErrorSeverity(error)
        }
      });
    }

    // Store locally for offline scenarios
    this.storeErrorLocally(errorReport);
  }

  getErrorSeverity(error) {
    if (error.message.includes('ChunkLoadError')) return 'medium';
    if (error.name === 'NetworkError') return 'low';
    return 'high';
  }

  attemptRecovery(error) {
    const recoveryStrategies = {
      ChunkLoadError: () => this.handleChunkLoadError(),
      NetworkError: () => this.handleNetworkError(),
      ReferenceError: () => this.handleReferenceError()
    };

    const strategy = recoveryStrategies[error.name];
    if (strategy && this.state.retryCount < 3) {
      setTimeout(() => {
        strategy();
        this.setState(prevState => ({
          retryCount: prevState.retryCount + 1
        }));
      }, 1000 * Math.pow(2, this.state.retryCount)); // Exponential backoff
    }
  }

  handleChunkLoadError() {
    // Clear module cache and reload
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.getRegistrations().then(registrations => {
        registrations.forEach(registration => registration.unregister());
      });
    }
    window.location.reload();
  }

  handleNetworkError() {
    // Retry with cache-first strategy
    this.setState({ hasError: false, error: null });
  }

  handleReferenceError() {
    // Reset component state
    this.setState({ hasError: false, error: null });
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback ? (
        this.props.fallback(this.state.error, () => this.setState({ hasError: false }))
      ) : (
        <ErrorFallbackComponent
          error={this.state.error}
          errorId={this.state.errorId}
          onRetry={() => this.setState({ hasError: false })}
          onReport={() => this.reportError(this.state.error, this.state.errorInfo)}
        />
      );
    }

    return this.props.children;
  }
}

// Usage
function App() {
  return (
    <AdvancedErrorBoundary
      name="App"
      fallback={(error, retry) => (
        <div>
          <h2>Something went wrong</h2>
          <details>
            <summary>Error details</summary>
            <pre>{error.message}</pre>
          </details>
          <button onClick={retry}>Retry</button>
        </div>
      )}
    >
      <Routes />
    </AdvancedErrorBoundary>
  );
}
```

### 7. Advanced Performance & Profiling

#### Q19: Memory leaks detection và optimization trong React apps?

**Trả lời:**

```javascript
// 1. Advanced Memory Leak Detection
class MemoryLeakDetector {
  constructor() {
    this.components = new Map();
    this.subscriptions = new Map();
    this.timers = new Map();
    this.observers = new Map();

    this.setupPerformanceObserver();
    this.setupMemoryMonitoring();
  }

  setupPerformanceObserver() {
    if ('PerformanceObserver' in window) {
      const observer = new PerformanceObserver((list) => {
        for (const entry of list.getEntries()) {
          if (entry.entryType === 'measure') {
            this.analyzePerformanceEntry(entry);
          }
        }
      });

      observer.observe({ entryTypes: ['measure', 'navigation', 'resource'] });
    }
  }

  setupMemoryMonitoring() {
    if ('memory' in performance) {
      setInterval(() => {
        const memInfo = performance.memory;
        const memoryUsage = {
          used: memInfo.usedJSHeapSize,
          total: memInfo.totalJSHeapSize,
          limit: memInfo.jsHeapSizeLimit,
          timestamp: Date.now()
        };

        this.analyzeMemoryUsage(memoryUsage);
      }, 5000); // Check every 5 seconds
    }
  }

  analyzeMemoryUsage(memoryUsage) {
    const memoryGrowthRate = this.calculateGrowthRate(memoryUsage);

    if (memoryGrowthRate > 0.1) { // 10% growth per check
      console.warn('Potential memory leak detected', {
        growthRate: memoryGrowthRate,
        currentUsage: memoryUsage
      });

      // Trigger garbage collection if available
      if (window.gc) {
        window.gc();
      }

      // Report to monitoring service
      this.reportMemoryLeak(memoryUsage);
    }
  }

  // Component lifecycle tracking
  trackComponent(componentName, instanceId) {
    const tracking = {
      mountTime: Date.now(),
      renders: 0,
      subscriptions: new Set(),
      timers: new Set(),
      observers: new Set()
    };

    this.components.set(`${componentName}_${instanceId}`, tracking);
    return tracking;
  }

  trackSubscription(componentKey, subscription) {
    const tracking = this.components.get(componentKey);
    if (tracking) {
      tracking.subscriptions.add(subscription);
    }
  }

  trackTimer(componentKey, timerId) {
    const tracking = this.components.get(componentKey);
    if (tracking) {
      tracking.timers.add(timerId);
    }
  }

  untrackComponent(componentKey) {
    const tracking = this.components.get(componentKey);
    if (tracking) {
      // Check for potential leaks
      if (tracking.subscriptions.size > 0) {
        console.warn(`Component ${componentKey} unmounted with active subscriptions`,
          tracking.subscriptions);
      }

      if (tracking.timers.size > 0) {
        console.warn(`Component ${componentKey} unmounted with active timers`,
          tracking.timers);
      }

      this.components.delete(componentKey);
    }
  }
}

// Global instance
window.MemoryLeakDetector = new MemoryLeakDetector();

// 2. Custom Hook với automatic cleanup tracking
function useTrackedEffect(effect, deps, componentName) {
  const componentId = useRef(generateUUID());
  const trackingKey = `${componentName}_${componentId.current}`;

  useEffect(() => {
    // Track component mount
    window.MemoryLeakDetector.trackComponent(componentName, componentId.current);

    const cleanup = effect();

    return () => {
      if (cleanup) cleanup();
      // Track component unmount
      window.MemoryLeakDetector.untrackComponent(trackingKey);
    };
  }, deps);
}

function useTrackedSubscription(subscribe, componentName) {
  const componentId = useRef(generateUUID());
  const trackingKey = `${componentName}_${componentId.current}`;

  useEffect(() => {
    const subscription = subscribe();

    // Track subscription
    window.MemoryLeakDetector.trackSubscription(trackingKey, subscription);

    return () => {
      if (subscription && typeof subscription.unsubscribe === 'function') {
        subscription.unsubscribe();
      } else if (typeof subscription === 'function') {
        subscription();
      }
    };
  }, [subscribe, trackingKey]);
}

// 3. Advanced Performance Profiling
class ReactPerformanceProfiler {
  constructor() {
    this.profiles = new Map();
    this.renderTimes = new Map();
    this.componentMetrics = new Map();
  }

  startProfiling(sessionId) {
    if (React.Profiler) {
      this.profiles.set(sessionId, {
        startTime: Date.now(),
        interactions: [],
        renders: []
      });
    }
  }

  onRender(id, phase, actualDuration, baseDuration, startTime, commitTime, interactions) {
    const profile = this.profiles.get('current') || this.profiles.get('default');

    if (profile) {
      const renderData = {
        id,
        phase,
        actualDuration,
        baseDuration,
        startTime,
        commitTime,
        interactions: Array.from(interactions),
        timestamp: Date.now()
      };

      profile.renders.push(renderData);

      // Analyze for performance issues
      this.analyzeRenderPerformance(renderData);
    }
  }

  analyzeRenderPerformance(renderData) {
    const { id, actualDuration, baseDuration, phase } = renderData;

    // Detect slow renders
    if (actualDuration > 16.67) { // More than one frame at 60fps
      console.warn(`Slow render detected in ${id}`, {
        duration: actualDuration,
        phase,
        recommendation: this.getOptimizationRecommendation(renderData)
      });
    }

    // Detect unnecessary re-renders
    if (phase === 'update' && actualDuration > baseDuration * 2) {
      console.warn(`Inefficient update in ${id}`, {
        actualDuration,
        baseDuration,
        efficiency: baseDuration / actualDuration
      });
    }

    // Track component performance over time
    this.updateComponentMetrics(id, renderData);
  }

  getOptimizationRecommendation(renderData) {
    const recommendations = [];

    if (renderData.actualDuration > 50) {
      recommendations.push('Consider using React.memo() or useMemo()');
    }

    if (renderData.interactions.length > 5) {
      recommendations.push('Too many interactions, consider debouncing');
    }

    return recommendations;
  }

  generatePerformanceReport() {
    const report = {
      totalComponents: this.componentMetrics.size,
      slowComponents: Array.from(this.componentMetrics.entries())
        .filter(([_, metrics]) => metrics.averageDuration > 16.67)
        .map(([id, metrics]) => ({ id, ...metrics })),

      recommendations: this.generateRecommendations(),
      memoryUsage: performance.memory ? {
        used: performance.memory.usedJSHeapSize,
        total: performance.memory.totalJSHeapSize
      } : null
    };

    return report;
  }
}

// 4. Bundle size analysis và optimization
class BundleAnalyzer {
  constructor() {
    this.moduleMap = new Map();
    this.importCosts = new Map();
    this.unusedCode = new Set();
  }

  async analyzeBundleSize() {
    // Analyze loaded modules
    if (window.webpackChunkName) {
      const chunks = await this.getLoadedChunks();
      const analysis = await this.analyzeChunks(chunks);

      return {
        totalSize: analysis.totalSize,
        chunkSizes: analysis.chunkSizes,
        recommendations: this.generateSizeRecommendations(analysis)
      };
    }
  }

  trackImportCost(moduleName, size, loadTime) {
    this.importCosts.set(moduleName, {
      size,
      loadTime,
      timestamp: Date.now()
    });
  }

  detectUnusedCode() {
    // Use intersection observer to track which components are actually rendered
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const componentName = entry.target.dataset.component;
          if (componentName) {
            this.unusedCode.delete(componentName);
          }
        }
      });
    });

    // Track all components initially as unused
    document.querySelectorAll('[data-component]').forEach(element => {
      const componentName = element.dataset.component;
      this.unusedCode.add(componentName);
      observer.observe(element);
    });

    return observer;
  }

  generateSizeRecommendations(analysis) {
    const recommendations = [];

    // Large chunks
    const largeChunks = analysis.chunkSizes
      .filter(chunk => chunk.size > 250 * 1024) // 250KB
      .map(chunk => chunk.name);

    if (largeChunks.length > 0) {
      recommendations.push({
        type: 'code-splitting',
        message: `Consider splitting large chunks: ${largeChunks.join(', ')}`,
        impact: 'high'
      });
    }

    // Expensive imports
    const expensiveImports = Array.from(this.importCosts.entries())
      .filter(([_, cost]) => cost.loadTime > 100)
      .map(([name]) => name);

    if (expensiveImports.length > 0) {
      recommendations.push({
        type: 'lazy-loading',
        message: `Consider lazy loading: ${expensiveImports.join(', ')}`,
        impact: 'medium'
      });
    }

    return recommendations;
  }
}

// 5. Component usage with performance tracking
function withPerformanceTracking(WrappedComponent, componentName) {
  return React.forwardRef((props, ref) => {
    const renderCount = useRef(0);
    const mountTime = useRef(Date.now());
    const lastRenderTime = useRef(Date.now());

    useEffect(() => {
      renderCount.current++;

      const now = Date.now();
      const renderDuration = now - lastRenderTime.current;
      lastRenderTime.current = now;

      // Track performance metrics
      window.ReactPerformanceProfiler?.trackComponentRender(componentName, {
        renderCount: renderCount.current,
        renderDuration,
        totalLifetime: now - mountTime.current
      });

      return () => {
        // Track unmount
        window.ReactPerformanceProfiler?.trackComponentUnmount(componentName, {
          totalRenders: renderCount.current,
          totalLifetime: Date.now() - mountTime.current
        });
      };
    });

    return (
      <React.Profiler
        id={componentName}
        onRender={window.ReactPerformanceProfiler?.onRender}
      >
        <div data-component={componentName}>
          <WrappedComponent {...props} ref={ref} />
        </div>
      </React.Profiler>
    );
  });
}

// Usage
const OptimizedUserProfile = withPerformanceTracking(UserProfile, 'UserProfile');
```

### 8. Advanced Security & Penetration Testing

#### Q20: Implement comprehensive security measures cho frontend apps?

**Trả lời:**

```javascript
// 1. Advanced Security Headers Implementation
class SecurityHeadersManager {
  constructor() {
    this.policies = {
      csp: {
        'default-src': ["'self'"],
        'script-src': ["'self'", "'unsafe-inline'", 'https://trusted-scripts.com'],
        'style-src': ["'self'", "'unsafe-inline'", 'https://fonts.googleapis.com'],
        'img-src': ["'self'", 'data:', 'https://trusted-images.com'],
        'connect-src': ["'self'", 'https://api.yourapp.com', 'wss://ws.yourapp.com'],
        'font-src': ["'self'", 'https://fonts.gstatic.com'],
        'frame-ancestors': ["'none'"],
        'base-uri': ["'self'"],
        'form-action': ["'self'"]
      },
      permissions: {
        camera: [],
        microphone: [],
        geolocation: ['self'],
        notifications: ['self'],
        push: ['self'],
        midi: [],
        accelerometer: [],
        gyroscope: [],
        magnetometer: []
      }
    };
  }

  applySecurityHeaders() {
    // Content Security Policy
    const cspString = Object.entries(this.policies.csp)
      .map(([directive, sources]) => `${directive} ${sources.join(' ')}`)
      .join('; ');

    this.setMetaTag('Content-Security-Policy', cspString);

    // Permissions Policy
    const permissionsString = Object.entries(this.policies.permissions)
      .map(([feature, origins]) => `${feature}=(${origins.join(' ')})`)
      .join(', ');

    this.setMetaTag('Permissions-Policy', permissionsString);

    // Additional security headers
    this.setMetaTag('X-Content-Type-Options', 'nosniff');
    this.setMetaTag('X-Frame-Options', 'DENY');
    this.setMetaTag('X-XSS-Protection', '1; mode=block');
    this.setMetaTag('Referrer-Policy', 'strict-origin-when-cross-origin');
    this.setMetaTag('Strict-Transport-Security', 'max-age=31536000; includeSubDomains');
  }

  setMetaTag(name, content) {
    let meta = document.querySelector(`meta[http-equiv="${name}"]`);
    if (!meta) {
      meta = document.createElement('meta');
      meta.httpEquiv = name;
      document.head.appendChild(meta);
    }
    meta.content = content;
  }

  // Runtime CSP violation detection
  setupCSPViolationReporting() {
    document.addEventListener('securitypolicyviolation', (event) => {
      const violation = {
        blockedURI: event.blockedURI,
        violatedDirective: event.violatedDirective,
        originalPolicy: event.originalPolicy,
        sourceFile: event.sourceFile,
        lineNumber: event.lineNumber,
        timestamp: Date.now()
      };

      // Report violation to security monitoring
      this.reportSecurityViolation('csp', violation);

      // Auto-adjust policy for development
      if (process.env.NODE_ENV === 'development') {
        this.suggestPolicyUpdate(violation);
      }
    });
  }

  reportSecurityViolation(type, details) {
    if (window.securityMonitor) {
      window.securityMonitor.reportViolation(type, details);
    }

    // Store locally for analysis
    const violations = JSON.parse(localStorage.getItem('security_violations') || '[]');
    violations.push({ type, details, timestamp: Date.now() });
    localStorage.setItem('security_violations', JSON.stringify(violations.slice(-100))); // Keep last 100
  }
}

// 2. Advanced Input Validation và Sanitization
class AdvancedValidator {
  constructor() {
    this.rules = new Map();
    this.sanitizers = new Map();
    this.patterns = {
      email: /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/,
      phone: /^\+?[\d\s-()]{10,15}$/,
      url: /^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$/,
      creditCard: /^\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}$/,
      ssn: /^\d{3}-\d{2}-\d{4}$/
    };
  }

  addRule(fieldName, validator) {
    this.rules.set(fieldName, validator);
  }

  addSanitizer(fieldName, sanitizer) {
    this.sanitizers.set(fieldName, sanitizer);
  }

  // Advanced validation with context awareness
  validate(data, context = {}) {
    const results = {
      isValid: true,
      errors: {},
      warnings: {},
      sanitized: {}
    };

    for (const [field, value] of Object.entries(data)) {
      // Sanitize first
      const sanitized = this.sanitizeField(field, value, context);
      results.sanitized[field] = sanitized;

      // Then validate
      const validation = this.validateField(field, sanitized, context);

      if (!validation.isValid) {
        results.isValid = false;
        results.errors[field] = validation.errors;
      }

      if (validation.warnings?.length > 0) {
        results.warnings[field] = validation.warnings;
      }
    }

    return results;
  }

  sanitizeField(fieldName, value, context) {
    if (typeof value !== 'string') return value;

    // Apply field-specific sanitization
    const sanitizer = this.sanitizers.get(fieldName);
    if (sanitizer) {
      value = sanitizer(value, context);
    }

    // Universal sanitization
    return this.applySafeSanitization(value);
  }

  applySafeSanitization(value) {
    return value
      // Remove null bytes
      .replace(/\0/g, '')
      // Remove or escape dangerous HTML
      .replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '')
      .replace(/<iframe\b[^<]*(?:(?!<\/iframe>)<[^<]*)*<\/iframe>/gi, '')
      // Normalize whitespace
      .replace(/\s+/g, ' ')
      .trim();
  }

  validateField(fieldName, value, context) {
    const result = {
      isValid: true,
      errors: [],
      warnings: []
    };

    // Check for common attack patterns
    this.checkForAttackPatterns(value, result);

    // Apply field-specific validation
    const rule = this.rules.get(fieldName);
    if (rule) {
      const ruleResult = rule(value, context);
      if (!ruleResult.isValid) {
        result.isValid = false;
        result.errors.push(...ruleResult.errors);
      }
    }

    // Pattern validation
    if (this.patterns[fieldName] && !this.patterns[fieldName].test(value)) {
      result.isValid = false;
      result.errors.push(`Invalid ${fieldName} format`);
    }

    return result;
  }

  checkForAttackPatterns(value, result) {
    const attackPatterns = [
      { pattern: /<script|javascript:|vbscript:|onload=|onerror=/i, type: 'XSS' },
      { pattern: /union.*select|select.*from|insert.*into|delete.*from/i, type: 'SQL Injection' },
      { pattern: /\.\.|\/etc\/|\/proc\/|\/var\/|\/tmp\//i, type: 'Path Traversal' },
      { pattern: /eval\s*\(|Function\s*\(|setTimeout\s*\(.*script/i, type: 'Code Injection' }
    ];

    for (const { pattern, type } of attackPatterns) {
      if (pattern.test(value)) {
        result.warnings.push(`Potential ${type} attack detected`);

        // Report to security monitoring
        window.SecurityHeadersManager?.reportSecurityViolation('input_attack', {
          type,
          value: value.substring(0, 100), // Truncate for privacy
          pattern: pattern.toString()
        });
      }
    }
  }
}

// 3. Runtime Security Monitoring
class SecurityMonitor {
  constructor() {
    this.threats = new Map();
    this.metrics = {
      requestCount: 0,
      suspiciousRequests: 0,
      blockedRequests: 0,
      xssAttempts: 0,
      csrfAttempts: 0
    };

    this.setupGlobalErrorHandler();
    this.setupNetworkMonitoring();
    this.setupDOMTamperingDetection();
  }

  setupGlobalErrorHandler() {
    window.addEventListener('error', (event) => {
      // Check for suspicious errors that might indicate attacks
      if (this.isSuspiciousError(event.error)) {
        this.reportThreat('suspicious_error', {
          message: event.error.message,
          stack: event.error.stack,
          filename: event.filename,
          lineno: event.lineno
        });
      }
    });

    window.addEventListener('unhandledrejection', (event) => {
      if (this.isSuspiciousPromiseRejection(event.reason)) {
        this.reportThreat('suspicious_rejection', {
          reason: event.reason.toString()
        });
      }
    });
  }

  setupNetworkMonitoring() {
    // Intercept fetch requests
    const originalFetch = window.fetch;
    window.fetch = async (...args) => {
      const [url, options] = args;

      this.metrics.requestCount++;

      // Analyze request for suspicious patterns
      if (this.isSuspiciousRequest(url, options)) {
        this.metrics.suspiciousRequests++;
        this.reportThreat('suspicious_request', { url, options });
      }

      try {
        const response = await originalFetch(...args);

        // Analyze response headers for security issues
        this.analyzeResponseSecurity(response);

        return response;
      } catch (error) {
        this.reportThreat('network_error', { error: error.message, url });
        throw error;
      }
    };
  }

  setupDOMTamperingDetection() {
    // Monitor for unauthorized DOM modifications
    const observer = new MutationObserver((mutations) => {
      mutations.forEach((mutation) => {
        if (mutation.type === 'childList') {
          mutation.addedNodes.forEach((node) => {
            if (node.nodeType === Node.ELEMENT_NODE) {
              this.checkForMaliciousElement(node);
            }
          });
        }
      });
    });

    observer.observe(document.body, {
      childList: true,
      subtree: true,
      attributes: true,
      attributeFilter: ['src', 'href', 'onclick', 'onload']
    });
  }

  isSuspiciousError(error) {
    const suspiciousPatterns = [
      /script error/i,
      /permission denied/i,
      /access denied/i,
      /unauthorized/i
    ];

    return suspiciousPatterns.some(pattern =>
      pattern.test(error.message || error.toString())
    );
  }

  isSuspiciousRequest(url, options = {}) {
    // Check for suspicious URL patterns
    const suspiciousUrlPatterns = [
      /\.\.|\/etc\/|\/proc\/|\/var\//,
      /<script|javascript:|data:/i,
      /\?(.*&){20,}/, // Too many parameters
    ];

    if (suspiciousUrlPatterns.some(pattern => pattern.test(url))) {
      return true;
    }

    // Check for suspicious headers
    const headers = options.headers || {};
    if (headers['User-Agent']?.includes('curl') ||
        headers['User-Agent']?.includes('wget')) {
      return true;
    }

    return false;
  }

  checkForMaliciousElement(element) {
    // Check for suspicious scripts
    if (element.tagName === 'SCRIPT') {
      const src = element.getAttribute('src');
      const content = element.textContent;

      if (src && !this.isAllowedScriptSource(src)) {
        this.reportThreat('unauthorized_script', { src });
        element.remove();
        this.metrics.blockedRequests++;
      }

      if (content && this.containsMaliciousCode(content)) {
        this.reportThreat('malicious_inline_script', { content });
        element.remove();
        this.metrics.blockedRequests++;
      }
    }

    // Check for suspicious iframes
    if (element.tagName === 'IFRAME') {
      const src = element.getAttribute('src');
      if (src && !this.isAllowedFrameSource(src)) {
        this.reportThreat('unauthorized_iframe', { src });
        element.remove();
        this.metrics.blockedRequests++;
      }
    }
  }

  reportThreat(type, details) {
    const threat = {
      type,
      details,
      timestamp: Date.now(),
      url: window.location.href,
      userAgent: navigator.userAgent,
      sessionId: this.getSessionId()
    };

    this.threats.set(Date.now(), threat);

    // Send to security endpoint
    this.sendSecurityAlert(threat);

    // Log locally for analysis
    console.warn('[Security Monitor] Threat detected:', threat);
  }

  generateSecurityReport() {
    return {
      threats: Array.from(this.threats.values()),
      metrics: this.metrics,
      timestamp: Date.now(),
      recommendations: this.generateRecommendations()
    };
  }

  generateRecommendations() {
    const recommendations = [];

    if (this.metrics.xssAttempts > 0) {
      recommendations.push({
        type: 'XSS_PROTECTION',
        message: 'Implement stricter input validation and output encoding',
        priority: 'high'
      });
    }

    if (this.metrics.suspiciousRequests / this.metrics.requestCount > 0.1) {
      recommendations.push({
        type: 'RATE_LIMITING',
        message: 'Consider implementing rate limiting',
        priority: 'medium'
      });
    }

    return recommendations;
  }
}
```

#### Q21: Advanced debugging và production monitoring?

**Trả lời:**

```javascript
// 1. Advanced Error Tracking và Debugging
class AdvancedErrorTracker {
  constructor() {
    this.errorQueue = [];
    this.userSessions = new Map();
    this.performanceMetrics = new Map();
    this.breadcrumbs = [];
    this.maxBreadcrumbs = 50;

    this.setupErrorHandlers();
    this.setupPerformanceMonitoring();
    this.setupUserSessionTracking();
  }

  setupErrorHandlers() {
    // Global error handler
    window.addEventListener('error', (event) => {
      this.captureError({
        type: 'javascript',
        message: event.message,
        filename: event.filename,
        lineno: event.lineno,
        colno: event.colno,
        stack: event.error?.stack,
        timestamp: Date.now()
      });
    });

    // Unhandled promise rejections
    window.addEventListener('unhandledrejection', (event) => {
      this.captureError({
        type: 'unhandled_promise',
        message: event.reason?.message || event.reason,
        stack: event.reason?.stack,
        timestamp: Date.now()
      });
    });

    // Resource loading errors
    window.addEventListener('error', (event) => {
      if (event.target !== window) {
        this.captureError({
          type: 'resource',
          message: `Failed to load ${event.target.tagName}: ${event.target.src || event.target.href}`,
          element: event.target.outerHTML,
          timestamp: Date.now()
        });
      }
    }, true);
  }

  captureError(errorData) {
    const enhancedError = {
      ...errorData,
      id: this.generateErrorId(),
      url: window.location.href,
      userAgent: navigator.userAgent,
      viewport: {
        width: window.innerWidth,
        height: window.innerHeight
      },
      sessionId: this.getCurrentSessionId(),
      breadcrumbs: [...this.breadcrumbs],
      user: this.getCurrentUserContext(),
      environment: {
        timestamp: Date.now(),
        timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
        language: navigator.language,
        online: navigator.onLine,
        memory: performance.memory ? {
          used: performance.memory.usedJSHeapSize,
          total: performance.memory.totalJSHeapSize,
          limit: performance.memory.jsHeapSizeLimit
        } : null
      }
    };

    // Add React component stack if available
    if (window.React && window.React.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED) {
      enhancedError.componentStack = this.getReactComponentStack();
    }

    this.errorQueue.push(enhancedError);
    this.processError(enhancedError);
    this.sendErrorToMonitoring(enhancedError);
  }

  addBreadcrumb(message, category = 'default', level = 'info', data = {}) {
    const breadcrumb = {
      message,
      category,
      level,
      data,
      timestamp: Date.now()
    };

    this.breadcrumbs.push(breadcrumb);

    if (this.breadcrumbs.length > this.maxBreadcrumbs) {
      this.breadcrumbs.shift();
    }
  }

  // Advanced source map support for production debugging
  async resolveSourceLocation(filename, lineno, colno) {
    try {
      if (!filename.includes('.min.') && !filename.includes('.prod.')) {
        return { filename, lineno, colno };
      }

      const sourceMapUrl = await this.getSourceMapUrl(filename);
      if (!sourceMapUrl) return { filename, lineno, colno };

      const sourceMap = await this.loadSourceMap(sourceMapUrl);
      const originalPosition = this.resolveOriginalPosition(sourceMap, lineno, colno);

      return {
        filename: originalPosition.source,
        lineno: originalPosition.line,
        colno: originalPosition.column,
        originalFilename: filename
      };
    } catch (error) {
      console.warn('Failed to resolve source location:', error);
      return { filename, lineno, colno };
    }
  }

  // React component stack extraction
  getReactComponentStack() {
    try {
      const fiber = this.findReactFiberNode(document.body);
      if (!fiber) return null;

      const stack = [];
      let current = fiber;

      while (current) {
        if (current.type && typeof current.type === 'function') {
          stack.push({
            name: current.type.name || current.type.displayName || 'Anonymous',
            props: this.sanitizeProps(current.memoizedProps),
            state: this.sanitizeState(current.memoizedState)
          });
        }
        current = current.return;
      }

      return stack;
    } catch (error) {
      return null;
    }
  }

  // Performance monitoring integration
  setupPerformanceMonitoring() {
    // Web Vitals tracking
    this.trackWebVitals();

    // Long task monitoring
    if ('PerformanceObserver' in window) {
      const observer = new PerformanceObserver((list) => {
        for (const entry of list.getEntries()) {
          if (entry.duration > 50) { // Tasks longer than 50ms
            this.addBreadcrumb(
              `Long task detected: ${entry.duration}ms`,
              'performance',
              'warning',
              {
                duration: entry.duration,
                startTime: entry.startTime,
                name: entry.name
              }
            );
          }
        }
      });

      observer.observe({ entryTypes: ['longtask'] });
    }

    // Resource timing
    this.monitorResourceTiming();
  }

  trackWebVitals() {
    // First Contentful Paint
    this.observePerformanceEntry('paint', (entry) => {
      if (entry.name === 'first-contentful-paint') {
        this.recordMetric('FCP', entry.startTime);
      }
    });

    // Largest Contentful Paint
    this.observePerformanceEntry('largest-contentful-paint', (entry) => {
      this.recordMetric('LCP', entry.startTime);
    });

    // First Input Delay
    this.observePerformanceEntry('first-input', (entry) => {
      this.recordMetric('FID', entry.processingStart - entry.startTime);
    });

    // Cumulative Layout Shift
    let clsValue = 0;
    this.observePerformanceEntry('layout-shift', (entry) => {
      if (!entry.hadRecentInput) {
        clsValue += entry.value;
        this.recordMetric('CLS', clsValue);
      }
    });
  }

  // Real-time monitoring dashboard
  createMonitoringDashboard() {
    if (process.env.NODE_ENV !== 'development') return;

    const dashboard = document.createElement('div');
    dashboard.style.cssText = `
      position: fixed;
      top: 10px;
      right: 10px;
      width: 300px;
      background: rgba(0, 0, 0, 0.9);
      color: white;
      padding: 10px;
      border-radius: 5px;
      font-family: monospace;
      font-size: 12px;
      z-index: 10000;
      max-height: 400px;
      overflow-y: auto;
    `;

    this.updateDashboard(dashboard);

    setInterval(() => {
      this.updateDashboard(dashboard);
    }, 1000);

    document.body.appendChild(dashboard);
  }

  updateDashboard(dashboard) {
    const metrics = this.getMetricsSummary();
    const recentErrors = this.errorQueue.slice(-5);

    dashboard.innerHTML = `
      <h4>🔍 Debug Monitor</h4>
      <div>Errors: ${this.errorQueue.length}</div>
      <div>Memory: ${this.formatBytes(performance.memory?.usedJSHeapSize || 0)}</div>
      <div>FCP: ${metrics.FCP?.toFixed(2) || 'N/A'}ms</div>
      <div>LCP: ${metrics.LCP?.toFixed(2) || 'N/A'}ms</div>

      <h5>Recent Errors:</h5>
      ${recentErrors.map(error => `
        <div style="margin: 5px 0; padding: 5px; background: rgba(255,0,0,0.2);">
          <div>${error.type}: ${error.message}</div>
          <div style="font-size: 10px; opacity: 0.7;">
            ${new Date(error.timestamp).toLocaleTimeString()}
          </div>
        </div>
      `).join('')}

      <h5>Recent Breadcrumbs:</h5>
      ${this.breadcrumbs.slice(-3).map(crumb => `
        <div style="margin: 2px 0; font-size: 10px;">
          [${crumb.category}] ${crumb.message}
        </div>
      `).join('')}
    `;
  }
}

// 2. Advanced React DevTools Integration
class ReactDevToolsIntegration {
  constructor() {
    this.componentProfiles = new Map();
    this.renderCounts = new Map();
    this.setupReactDevToolsHooks();
  }

  setupReactDevToolsHooks() {
    if (window.__REACT_DEVTOOLS_GLOBAL_HOOK__) {
      const hook = window.__REACT_DEVTOOLS_GLOBAL_HOOK__;

      // Intercept fiber commits
      hook.onCommitFiberRoot = (id, root, priorityLevel) => {
        this.analyzeCommit(root, priorityLevel);
      };

      // Track component updates
      hook.onCommitFiberUnmount = (id, fiber) => {
        this.trackComponentUnmount(fiber);
      };
    }
  }

  analyzeCommit(root, priorityLevel) {
    const commitTime = performance.now();

    this.traverseFiber(root.current, (fiber) => {
      if (fiber.actualDuration > 0) {
        const componentName = this.getComponentName(fiber);

        if (!this.componentProfiles.has(componentName)) {
          this.componentProfiles.set(componentName, {
            renderCount: 0,
            totalTime: 0,
            averageTime: 0,
            maxTime: 0,
            minTime: Infinity
          });
        }

        const profile = this.componentProfiles.get(componentName);
        profile.renderCount++;
        profile.totalTime += fiber.actualDuration;
        profile.averageTime = profile.totalTime / profile.renderCount;
        profile.maxTime = Math.max(profile.maxTime, fiber.actualDuration);
        profile.minTime = Math.min(profile.minTime, fiber.actualDuration);

        // Warn about slow components
        if (fiber.actualDuration > 16.67) { // More than one frame
          console.warn(`Slow render: ${componentName} took ${fiber.actualDuration.toFixed(2)}ms`);
        }
      }
    });
  }

  // Component dependency analysis
  analyzeComponentDependencies(component) {
    const dependencies = {
      props: new Set(),
      context: new Set(),
      hooks: new Set(),
      state: new Set()
    };

    // Analyze props
    if (component.memoizedProps) {
      Object.keys(component.memoizedProps).forEach(prop => {
        dependencies.props.add(prop);
      });
    }

    // Analyze hooks
    let hook = component.memoizedState;
    while (hook) {
      if (hook.queue) {
        dependencies.hooks.add(this.getHookType(hook));
      }
      hook = hook.next;
    }

    return dependencies;
  }

  generatePerformanceReport() {
    const report = {
      timestamp: Date.now(),
      components: Array.from(this.componentProfiles.entries()).map(([name, profile]) => ({
        name,
        ...profile,
        efficiency: profile.minTime / profile.maxTime // Closer to 1 is better
      })),
      recommendations: this.generateOptimizationRecommendations()
    };

    return report;
  }

  generateOptimizationRecommendations() {
    const recommendations = [];

    for (const [name, profile] of this.componentProfiles.entries()) {
      if (profile.averageTime > 10) {
        recommendations.push({
          component: name,
          issue: 'Slow average render time',
          suggestion: 'Consider using React.memo() or optimizing render logic',
          priority: profile.averageTime > 20 ? 'high' : 'medium'
        });
      }

      if (profile.renderCount > 100 && profile.efficiency < 0.5) {
        recommendations.push({
          component: name,
          issue: 'Inconsistent render performance',
          suggestion: 'Check for expensive operations or unnecessary re-renders',
          priority: 'medium'
        });
      }
    }

    return recommendations;
  }
}

// 3. Production monitoring integration
class ProductionMonitor {
  constructor() {
    this.config = {
      sampleRate: 0.1, // Sample 10% of sessions
      maxErrors: 50,
      batchSize: 10,
      flushInterval: 30000 // 30 seconds
    };

    this.initializeMonitoring();
  }

  initializeMonitoring() {
    // Only monitor in production
    if (process.env.NODE_ENV !== 'production') return;

    // Sample sessions
    if (Math.random() > this.config.sampleRate) return;

    this.errorTracker = new AdvancedErrorTracker();
    this.performanceMonitor = new ReactDevToolsIntegration();

    this.setupBatchedReporting();
    this.setupVisibilityTracking();
  }

  setupBatchedReporting() {
    setInterval(() => {
      this.flushPendingData();
    }, this.config.flushInterval);

    // Flush on page unload
    window.addEventListener('beforeunload', () => {
      this.flushPendingData(true);
    });
  }

  setupVisibilityTracking() {
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        this.flushPendingData();
      }
    });
  }

  flushPendingData(immediate = false) {
    const data = {
      errors: this.errorTracker.errorQueue.splice(0),
      performance: this.performanceMonitor.generatePerformanceReport(),
      session: {
        id: this.getSessionId(),
        duration: Date.now() - this.sessionStartTime,
        pageViews: this.pageViewCount,
        interactions: this.interactionCount
      }
    };

    if (data.errors.length > 0 || immediate) {
      this.sendToMonitoringService(data, immediate);
    }
  }

  sendToMonitoringService(data, immediate = false) {
    const url = '/api/monitoring/events';
    const payload = JSON.stringify(data);

    if (immediate && navigator.sendBeacon) {
      // Use sendBeacon for reliable delivery during page unload
      navigator.sendBeacon(url, payload);
    } else {
      // Use fetch with keepalive for regular sends
      fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: payload,
        keepalive: true
      }).catch(error => {
        console.warn('Failed to send monitoring data:', error);
        // Store locally for retry
        this.storeForRetry(data);
      });
    }
  }
}

// Global initialization
if (typeof window !== 'undefined') {
  window.AdvancedErrorTracker = new AdvancedErrorTracker();
  window.ReactDevTools = new ReactDevToolsIntegration();
  window.ProductionMonitor = new ProductionMonitor();

  // Create debug dashboard in development
  if (process.env.NODE_ENV === 'development') {
    window.AdvancedErrorTracker.createMonitoringDashboard();
  }
}
```

---

## Conclusion

Đây là bộ câu hỏi phỏng vấn toàn diện từ cơ bản đến Expert level, bao gồm:

### **Junior Level:**
1. **JavaScript Fundamentals**: Event Loop, Closures, Hoisting
2. **React Core Concepts**: Hooks, Components, State Management

### **Mid-Level:**
3. **Advanced React Concepts**: Custom Hooks, Context API vs Redux
4. **Performance Optimization**: Memoization, Code Splitting

### **Senior Level:**
5. **Advanced Patterns**: HOC, Render Props, Custom Hooks
6. **Security Best Practices**: XSS Prevention, CSRF Protection, Data Privacy

### **Expert/Lead Level:**
7. **System Design & Architecture**: Micro-frontends, Advanced Caching
8. **Advanced Performance & Profiling**: Memory Leak Detection, Bundle Analysis
9. **Enterprise Patterns**: Event Sourcing, Advanced Error Boundaries
10. **React Advanced Topics**: Concurrent Mode, Suspense, Server Components
11. **Clean Code & Best Practices**: SOLID principles, Code organization
12. **Performance Optimization**: Advanced React optimization techniques
13. **Testing Strategies**: Unit, Integration, E2E, Performance, A11y Testing
14. **Accessibility (A11y)**: ARIA patterns, Screen readers, Semantic HTML

## **Tóm Tắt Bộ Câu Hỏi Hoàn Chỉnh**

### 📊 **Thống Kê:**
- **Tổng cộng: 28 câu hỏi chuyên sâu**
- **6,900+ dòng code examples**
- **14 chủ đề chính từ cơ bản đến Expert**
- **Production-ready solutions với real-world scenarios**

### 🎯 **Phân Cấp Câu Hỏi:**

**Junior Level (4 câu):**
- Q1-Q4: JavaScript fundamentals, React basics, useState, useEffect

**Mid-Level (3 câu):**
- Q5-Q7: Advanced React concepts, Custom Hooks, Context vs Redux

**Senior Level (8 câu):**
- Q8-Q15: Performance optimization, Security best practices, HOC/Render Props

**Expert/Lead Level (13 câu):**
- Q16-Q28: System design, Advanced debugging, Clean code, Testing, A11y

### 🚀 **Điểm Nổi Bật:**

✅ **React 18 Features**: Concurrent Mode, Suspense, useTransition, useDeferredValue
✅ **Modern Patterns**: Server Components, Micro-frontends, Event Sourcing
✅ **Performance**: Memory leak detection, Bundle optimization, Virtualization
✅ **Security**: XSS prevention, CSRF protection, Runtime monitoring
✅ **Testing**: Unit, Integration, E2E, Performance, Visual regression
✅ **Accessibility**: ARIA patterns, Screen readers, Focus management
✅ **Clean Code**: SOLID principles, Feature-based architecture
✅ **Production Ready**: Error boundaries, Monitoring, Debugging tools

### 🔧 **Advanced Topics Covered:**

**System Architecture:**
- Module Federation với Webpack 5
- Event-driven communication
- Cross-domain state management
- Multi-layer caching strategies

**Performance Engineering:**
- Advanced memoization techniques
- Component splitting và lazy loading
- Memory management và cleanup
- Bundle size optimization

**Security Engineering:**
- Runtime security monitoring
- Input validation và sanitization
- Content Security Policy implementation
- Threat detection patterns

**Testing Engineering:**
- Comprehensive testing strategies
- Performance regression testing
- Accessibility compliance testing
- Visual regression với Storybook

Mỗi câu hỏi đều có ví dụ code production-ready và giải thích chi tiết về architectural decisions, performance implications, và best practices cho enterprise applications.

### 9. React Advanced Topics & Modern Features

#### Q22: React Concurrent Mode và Suspense - Cách hoạt động và ứng dụng?

**Trả lời:**

```javascript
// 1. React Concurrent Mode - Time Slicing và Interruptible Rendering
function App() {
  const [isPending, startTransition] = useTransition();
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const deferredQuery = useDeferredValue(query);

  // High priority update - user input
  const handleInputChange = (e) => {
    const value = e.target.value;
    setQuery(value); // Immediate update

    // Low priority update - search results
    startTransition(() => {
      performSearch(value).then(setResults);
    });
  };

  return (
    <div>
      <input
        value={query}
        onChange={handleInputChange}
        placeholder="Search..."
      />

      {isPending && <div>Searching...</div>}

      <Suspense fallback={<SearchResultsSkeleton />}>
        <SearchResults query={deferredQuery} results={results} />
      </Suspense>
    </div>
  );
}

// 2. Advanced Suspense Patterns
const SearchResults = React.lazy(() =>
  import('./SearchResults').then(module => {
    // Simulate slow component
    return new Promise(resolve => {
      setTimeout(() => resolve(module), 1000);
    });
  })
);

// Suspense với Error Boundary
function SuspenseWrapper({ children, fallback }) {
  return (
    <ErrorBoundary
      fallback={<ErrorFallback />}
      onError={(error, errorInfo) => {
        console.error('Suspense error:', error);
        // Report to monitoring service
      }}
    >
      <Suspense fallback={fallback}>
        {children}
      </Suspense>
    </ErrorBoundary>
  );
}

// 3. Data Fetching với Suspense
function createSuspenseResource(promise) {
  let status = 'pending';
  let result;

  const suspender = promise.then(
    response => {
      status = 'success';
      result = response;
    },
    error => {
      status = 'error';
      result = error;
    }
  );

  return {
    read() {
      if (status === 'pending') {
        throw suspender; // Suspend component
      } else if (status === 'error') {
        throw result; // Trigger error boundary
      } else if (status === 'success') {
        return result;
      }
    }
  };
}

// Advanced data fetching hook với Suspense
function useSuspenseQuery(queryKey, queryFn, options = {}) {
  const [resource, setResource] = useState(() => {
    const cachedData = getCachedData(queryKey);
    if (cachedData && !isStale(cachedData, options.staleTime)) {
      return createSuspenseResource(Promise.resolve(cachedData));
    }
    return createSuspenseResource(queryFn());
  });

  useEffect(() => {
    const shouldRefetch = options.refetchOnMount ||
                         (options.refetchOnWindowFocus && document.hasFocus());

    if (shouldRefetch) {
      const newResource = createSuspenseResource(queryFn());
      setResource(newResource);
    }
  }, [queryKey]);

  return resource.read();
}

// Usage với Suspense
function UserProfile({ userId }) {
  const user = useSuspenseQuery(
    ['user', userId],
    () => fetchUser(userId),
    {
      staleTime: 5 * 60 * 1000,
      refetchOnWindowFocus: true
    }
  );

  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </div>
  );
}

// 4. Concurrent Features với useTransition
function FilterableList({ items }) {
  const [filter, setFilter] = useState('');
  const [isPending, startTransition] = useTransition();
  const [filteredItems, setFilteredItems] = useState(items);

  const handleFilterChange = (value) => {
    setFilter(value); // High priority - immediate UI update

    // Low priority - expensive filtering operation
    startTransition(() => {
      const filtered = items.filter(item =>
        item.name.toLowerCase().includes(value.toLowerCase()) ||
        item.description.toLowerCase().includes(value.toLowerCase())
      );
      setFilteredItems(filtered);
    });
  };

  return (
    <div>
      <input
        value={filter}
        onChange={(e) => handleFilterChange(e.target.value)}
        placeholder="Filter items..."
      />

      <div style={{ opacity: isPending ? 0.7 : 1 }}>
        {filteredItems.map(item => (
          <ListItem key={item.id} item={item} />
        ))}
      </div>
    </div>
  );
}

// 5. Server Components Integration (Next.js 13+)
// app/dashboard/page.tsx - Server Component
async function DashboardPage() {
  // This runs on the server
  const user = await fetchUser();
  const stats = await fetchDashboardStats();

  return (
    <div>
      <h1>Dashboard</h1>
      <UserGreeting user={user} />

      <Suspense fallback={<StatsLoading />}>
        <DashboardStats stats={stats} />
      </Suspense>

      {/* Client Component */}
      <InteractiveChart />
    </div>
  );
}

// Client Component với 'use client' directive
'use client';
function InteractiveChart() {
  const [data, setData] = useState([]);

  useEffect(() => {
    // Client-side data fetching
    fetchChartData().then(setData);
  }, []);

  return (
    <div>
      <canvas ref={chartRef} />
      <button onClick={refreshData}>Refresh</button>
    </div>
  );
}
```

#### Q23: React 18 features và migration strategies?

**Trả lời:**

```javascript
// 1. Migration từ React 17 to React 18
// Before (React 17)
import ReactDOM from 'react-dom';
ReactDOM.render(<App />, document.getElementById('root'));

// After (React 18)
import { createRoot } from 'react-dom/client';
const root = createRoot(document.getElementById('root'));
root.render(<App />);

// 2. Automatic Batching
function BatchingExample() {
  const [count, setCount] = useState(0);
  const [flag, setFlag] = useState(false);

  // React 18: These updates are automatically batched
  const handleClick = () => {
    setCount(c => c + 1);
    setFlag(f => !f);
    // Only one re-render in React 18
  };

  // Even in async operations
  const handleAsyncClick = async () => {
    await fetch('/api/data');
    setCount(c => c + 1); // Batched
    setFlag(f => !f);     // Batched
  };

  // Opt-out of batching if needed
  const handleNoBatching = () => {
    flushSync(() => {
      setCount(c => c + 1);
    });
    // This will re-render immediately
    setFlag(f => !f);
  };

  return (
    <div>
      <p>Count: {count}</p>
      <p>Flag: {flag.toString()}</p>
      <button onClick={handleClick}>Update State</button>
      <button onClick={handleAsyncClick}>Async Update</button>
      <button onClick={handleNoBatching}>No Batching</button>
    </div>
  );
}

// 3. Strict Mode Changes và Development Warnings
function StrictModeApp() {
  return (
    <StrictMode>
      <App />
    </StrictMode>
  );
}

// React 18 Strict Mode: Effects run twice in development
function EffectExample() {
  const [data, setData] = useState(null);

  useEffect(() => {
    let cancelled = false;

    const fetchData = async () => {
      try {
        const response = await fetch('/api/data');
        const result = await response.json();

        if (!cancelled) {
          setData(result);
        }
      } catch (error) {
        if (!cancelled) {
          console.error('Fetch error:', error);
        }
      }
    };

    fetchData();

    // Cleanup function - important for React 18 Strict Mode
    return () => {
      cancelled = true;
    };
  }, []);

  return <div>{data ? JSON.stringify(data) : 'Loading...'}</div>;
}

// 4. New Hooks trong React 18
function NewHooksExample() {
  // useId - for generating unique IDs
  const id = useId();
  const emailId = `${id}-email`;
  const passwordId = `${id}-password`;

  // useSyncExternalStore - for external state
  const isOnline = useSyncExternalStore(
    (callback) => {
      window.addEventListener('online', callback);
      window.addEventListener('offline', callback);
      return () => {
        window.removeEventListener('online', callback);
        window.removeEventListener('offline', callback);
      };
    },
    () => navigator.onLine,
    () => true // Server-side value
  );

  // useInsertionEffect - for CSS-in-JS libraries
  useInsertionEffect(() => {
    const style = document.createElement('style');
    style.textContent = `
      .dynamic-${id} {
        color: blue;
        font-weight: bold;
      }
    `;
    document.head.appendChild(style);

    return () => {
      document.head.removeChild(style);
    };
  }, [id]);

  return (
    <form>
      <div>
        <label htmlFor={emailId}>Email:</label>
        <input id={emailId} type="email" />
      </div>

      <div>
        <label htmlFor={passwordId}>Password:</label>
        <input id={passwordId} type="password" />
      </div>

      <div className={`dynamic-${id}`}>
        Status: {isOnline ? 'Online' : 'Offline'}
      </div>
    </form>
  );
}

// 5. Error Handling Improvements
class AdvancedErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    // React 18: Better error reporting
    console.error('Error boundary caught:', {
      error,
      errorInfo,
      componentStack: errorInfo.componentStack,
      errorBoundary: this.constructor.name
    });

    // Report to error tracking service
    if (window.errorReporter) {
      window.errorReporter.captureException(error, {
        contexts: {
          react: {
            componentStack: errorInfo.componentStack
          }
        }
      });
    }
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback ? (
        this.props.fallback(this.state.error)
      ) : (
        <div>
          <h2>Something went wrong.</h2>
          <details style={{ whiteSpace: 'pre-wrap' }}>
            {this.state.error && this.state.error.toString()}
          </details>
        </div>
      );
    }

    return this.props.children;
  }
}

// 6. Migration Best Practices
function MigrationChecklist() {
  /*
  React 18 Migration Checklist:

  1. Update React and ReactDOM
     npm install react@18 react-dom@18

  2. Replace ReactDOM.render with createRoot
     - ReactDOM.render(<App />, container)
     + const root = createRoot(container); root.render(<App />)

  3. Update TypeScript types
     npm install @types/react@18 @types/react-dom@18

  4. Test with Strict Mode
     - Enable <StrictMode> in development
     - Fix any double-effect issues

  5. Review third-party dependencies
     - Check compatibility with React 18
     - Update libraries that use ReactDOM.render

  6. Test Suspense boundaries
     - Ensure error boundaries wrap Suspense
     - Test loading states thoroughly

  7. Performance testing
     - Measure before/after migration
     - Test concurrent features gradually
  */

  return null;
}

// 7. Advanced Concurrent Patterns
function AdvancedConcurrentApp() {
  const [tab, setTab] = useState('posts');
  const [isPending, startTransition] = useTransition();

  const handleTabChange = (newTab) => {
    startTransition(() => {
      setTab(newTab);
    });
  };

  return (
    <div>
      <TabBar
        activeTab={tab}
        onTabChange={handleTabChange}
        isPending={isPending}
      />

      <Suspense fallback={<TabContentSkeleton />}>
        <TabContent tab={tab} />
      </Suspense>
    </div>
  );
}

function TabContent({ tab }) {
  const data = useSuspenseQuery(['tab', tab], () => fetchTabData(tab));

  return <div>{renderTabContent(tab, data)}</div>;
}
```

### 10. Clean Code Principles & Best Practices

#### Q24: SOLID principles áp dụng trong React components?

**Trả lời:**

```javascript
// 1. Single Responsibility Principle (SRP)
// ❌ Bad: Component làm quá nhiều việc
function BadUserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [posts, setPosts] = useState([]);
  const [followers, setFollowers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetching user data
    fetch(`/api/users/${userId}`)
      .then(res => res.json())
      .then(setUser);

    // Fetching posts
    fetch(`/api/users/${userId}/posts`)
      .then(res => res.json())
      .then(setPosts);

    // Fetching followers
    fetch(`/api/users/${userId}/followers`)
      .then(res => res.json())
      .then(setFollowers);

    setLoading(false);
  }, [userId]);

  const handleFollow = () => {
    // Follow logic
  };

  const handleLike = (postId) => {
    // Like logic
  };

  return (
    <div>
      {/* Complex rendering logic */}
      <UserHeader user={user} onFollow={handleFollow} />
      <UserPosts posts={posts} onLike={handleLike} />
      <UserFollowers followers={followers} />
    </div>
  );
}

// ✅ Good: Tách thành các components có trách nhiệm đơn lẻ
function UserProfile({ userId }) {
  return (
    <div>
      <UserProfileHeader userId={userId} />
      <UserProfileContent userId={userId} />
    </div>
  );
}

function UserProfileHeader({ userId }) {
  const { data: user, loading } = useUser(userId);

  if (loading) return <UserHeaderSkeleton />;

  return (
    <div>
      <Avatar src={user.avatar} alt={user.name} />
      <h1>{user.name}</h1>
      <FollowButton userId={userId} />
    </div>
  );
}

function UserProfileContent({ userId }) {
  return (
    <div>
      <UserPosts userId={userId} />
      <UserFollowers userId={userId} />
    </div>
  );
}

// 2. Open/Closed Principle (OCP)
// ✅ Component mở cho extension, đóng cho modification
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'danger';
  size?: 'small' | 'medium' | 'large';
  children: React.ReactNode;
  onClick?: () => void;
}

const buttonVariants = {
  primary: 'bg-blue-500 text-white hover:bg-blue-600',
  secondary: 'bg-gray-200 text-gray-800 hover:bg-gray-300',
  danger: 'bg-red-500 text-white hover:bg-red-600',
};

const buttonSizes = {
  small: 'px-2 py-1 text-sm',
  medium: 'px-4 py-2',
  large: 'px-6 py-3 text-lg',
};

function Button({
  variant = 'primary',
  size = 'medium',
  children,
  className = '',
  ...props
}: ButtonProps) {
  const baseClasses = 'rounded font-medium transition-colors';
  const variantClasses = buttonVariants[variant];
  const sizeClasses = buttonSizes[size];

  const classes = `${baseClasses} ${variantClasses} ${sizeClasses} ${className}`;

  return (
    <button className={classes} {...props}>
      {children}
    </button>
  );
}

// Extension through composition
function IconButton({ icon, ...props }: ButtonProps & { icon: React.ReactNode }) {
  return (
    <Button {...props}>
      <span className="mr-2">{icon}</span>
      {props.children}
    </Button>
  );
}

function LoadingButton({
  loading,
  loadingText = 'Loading...',
  ...props
}: ButtonProps & { loading: boolean; loadingText?: string }) {
  return (
    <Button {...props} disabled={loading || props.disabled}>
      {loading ? (
        <>
          <Spinner className="mr-2" />
          {loadingText}
        </>
      ) : (
        props.children
      )}
    </Button>
  );
}

// 3. Liskov Substitution Principle (LSP)
// ✅ Subcomponents có thể thay thế base component
interface InputProps {
  value: string;
  onChange: (value: string) => void;
  placeholder?: string;
  disabled?: boolean;
}

function TextInput({ value, onChange, ...props }: InputProps) {
  return (
    <input
      type="text"
      value={value}
      onChange={(e) => onChange(e.target.value)}
      {...props}
    />
  );
}

function EmailInput({ value, onChange, ...props }: InputProps) {
  const handleChange = (newValue: string) => {
    // Additional email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (emailRegex.test(newValue) || newValue === '') {
      onChange(newValue);
    }
  };

  return (
    <input
      type="email"
      value={value}
      onChange={(e) => handleChange(e.target.value)}
      {...props}
    />
  );
}

function PasswordInput({ value, onChange, ...props }: InputProps) {
  const [showPassword, setShowPassword] = useState(false);

  return (
    <div className="relative">
      <input
        type={showPassword ? 'text' : 'password'}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        {...props}
      />
      <button
        type="button"
        onClick={() => setShowPassword(!showPassword)}
        className="absolute right-2 top-1/2 transform -translate-y-1/2"
      >
        {showPassword ? <EyeOffIcon /> : <EyeIcon />}
      </button>
    </div>
  );
}

// Có thể sử dụng interchangeably
function Form() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');

  return (
    <form>
      <TextInput
        value={name}
        onChange={setName}
        placeholder="Full Name"
      />
      <EmailInput
        value={email}
        onChange={setEmail}
        placeholder="Email"
      />
      <PasswordInput
        value={password}
        onChange={setPassword}
        placeholder="Password"
      />
    </form>
  );
}

// 4. Interface Segregation Principle (ISP)
// ✅ Chia interfaces thành các phần nhỏ, specific
interface UserData {
  id: string;
  name: string;
  email: string;
  avatar: string;
}

interface UserActions {
  onFollow: () => void;
  onMessage: () => void;
  onBlock: () => void;
}

interface UserPreferences {
  theme: 'light' | 'dark';
  notifications: boolean;
  language: string;
}

// Components chỉ nhận props cần thiết
function UserAvatar({ user }: { user: Pick<UserData, 'name' | 'avatar'> }) {
  return (
    <img
      src={user.avatar}
      alt={user.name}
      className="w-10 h-10 rounded-full"
    />
  );
}

function UserActions({ actions }: { actions: UserActions }) {
  return (
    <div>
      <button onClick={actions.onFollow}>Follow</button>
      <button onClick={actions.onMessage}>Message</button>
      <button onClick={actions.onBlock}>Block</button>
    </div>
  );
}

function UserSettings({
  preferences,
  onUpdate
}: {
  preferences: UserPreferences;
  onUpdate: (prefs: Partial<UserPreferences>) => void;
}) {
  return (
    <div>
      <select
        value={preferences.theme}
        onChange={(e) => onUpdate({ theme: e.target.value as 'light' | 'dark' })}
      >
        <option value="light">Light</option>
        <option value="dark">Dark</option>
      </select>
    </div>
  );
}

// 5. Dependency Inversion Principle (DIP)
// ✅ Depend on abstractions, not concretions
interface DataService {
  fetchUser(id: string): Promise<UserData>;
  updateUser(id: string, data: Partial<UserData>): Promise<UserData>;
}

// Concrete implementations
class APIDataService implements DataService {
  async fetchUser(id: string): Promise<UserData> {
    const response = await fetch(`/api/users/${id}`);
    return response.json();
  }

  async updateUser(id: string, data: Partial<UserData>): Promise<UserData> {
    const response = await fetch(`/api/users/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    });
    return response.json();
  }
}

class MockDataService implements DataService {
  private users: Map<string, UserData> = new Map();

  async fetchUser(id: string): Promise<UserData> {
    return this.users.get(id) || {
      id,
      name: 'Mock User',
      email: 'mock@example.com',
      avatar: '/mock-avatar.jpg'
    };
  }

  async updateUser(id: string, data: Partial<UserData>): Promise<UserData> {
    const existing = await this.fetchUser(id);
    const updated = { ...existing, ...data };
    this.users.set(id, updated);
    return updated;
  }
}

// Component depends on abstraction
function useUserService(service: DataService) {
  return {
    fetchUser: service.fetchUser.bind(service),
    updateUser: service.updateUser.bind(service),
  };
}

function UserProfile({ userId, dataService }: {
  userId: string;
  dataService: DataService;
}) {
  const [user, setUser] = useState<UserData | null>(null);
  const { fetchUser, updateUser } = useUserService(dataService);

  useEffect(() => {
    fetchUser(userId).then(setUser);
  }, [userId, fetchUser]);

  const handleUpdate = async (updates: Partial<UserData>) => {
    if (user) {
      const updated = await updateUser(user.id, updates);
      setUser(updated);
    }
  };

  if (!user) return <div>Loading...</div>;

  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
      <button onClick={() => handleUpdate({ name: 'Updated Name' })}>
        Update Name
      </button>
    </div>
  );
}

// Usage with dependency injection
function App() {
  const dataService = process.env.NODE_ENV === 'test'
    ? new MockDataService()
    : new APIDataService();

  return (
    <UserProfile userId="123" dataService={dataService} />
  );
}
```

#### Q25: Code organization và folder structure cho large React apps?

**Trả lời:**

```javascript
// 1. Feature-based Architecture
/*
src/
├── shared/                    # Shared utilities và components
│   ├── components/           # Reusable UI components
│   │   ├── Button/
│   │   │   ├── Button.tsx
│   │   │   ├── Button.test.tsx
│   │   │   ├── Button.stories.tsx
│   │   │   └── index.ts
│   │   └── index.ts
│   ├── hooks/               # Custom hooks
│   │   ├── useLocalStorage.ts
│   │   ├── useDebounce.ts
│   │   └── index.ts
│   ├── utils/               # Utility functions
│   │   ├── format.ts
│   │   ├── validation.ts
│   │   └── index.ts
│   └── types/               # TypeScript types
│       ├── api.ts
│       ├── user.ts
│       └── index.ts
├── features/                 # Feature modules
│   ├── authentication/
│   │   ├── components/
│   │   │   ├── LoginForm/
│   │   │   ├── SignupForm/
│   │   │   └── index.ts
│   │   ├── hooks/
│   │   │   ├── useAuth.ts
│   │   │   └── index.ts
│   │   ├── services/
│   │   │   ├── authAPI.ts
│   │   │   └── index.ts
│   │   ├── store/
│   │   │   ├── authSlice.ts
│   │   │   └── index.ts
│   │   ├── types/
│   │   │   ├── auth.ts
│   │   │   └── index.ts
│   │   └── index.ts
│   ├── dashboard/
│   ├── user-management/
│   └── index.ts
├── pages/                   # Page components (routing)
│   ├── LoginPage/
│   ├── DashboardPage/
│   └── index.ts
├── store/                   # Global state management
│   ├── index.ts
│   ├── rootReducer.ts
│   └── middleware.ts
└── App.tsx
*/

// 2. Barrel Exports Pattern
// shared/components/index.ts
export { Button } from './Button';
export { Modal } from './Modal';
export { Input } from './Input';
export type { ButtonProps } from './Button';
export type { ModalProps } from './Modal';

// features/authentication/index.ts
export { LoginForm, SignupForm } from './components';
export { useAuth } from './hooks';
export { authAPI } from './services';
export { authSlice } from './store';
export type { AuthUser, LoginCredentials } from './types';

// 3. Clean Component Structure
// features/user-management/components/UserCard/UserCard.tsx
import React from 'react';
import { User } from '../../types';
import { useUserActions } from '../../hooks';
import { Avatar, Button } from '@/shared/components';
import styles from './UserCard.module.css';

interface UserCardProps {
  user: User;
  onEdit?: (user: User) => void;
  onDelete?: (userId: string) => void;
  className?: string;
}

export function UserCard({
  user,
  onEdit,
  onDelete,
  className = ''
}: UserCardProps) {
  const { deleteUser, isDeleting } = useUserActions();

  const handleEdit = () => {
    onEdit?.(user);
  };

  const handleDelete = async () => {
    if (window.confirm('Are you sure?')) {
      await deleteUser(user.id);
      onDelete?.(user.id);
    }
  };

  return (
    <div className={`${styles.userCard} ${className}`}>
      <div className={styles.header}>
        <Avatar src={user.avatar} alt={user.name} />
        <div className={styles.info}>
          <h3 className={styles.name}>{user.name}</h3>
          <p className={styles.email}>{user.email}</p>
        </div>
      </div>

      <div className={styles.actions}>
        <Button
          variant="secondary"
          size="small"
          onClick={handleEdit}
        >
          Edit
        </Button>
        <Button
          variant="danger"
          size="small"
          onClick={handleDelete}
          loading={isDeleting}
        >
          Delete
        </Button>
      </div>
    </div>
  );
}

// 4. Custom Hooks Organization
// features/user-management/hooks/useUserActions.ts
import { useMutation, useQueryClient } from '@tanstack/react-query';
import { userAPI } from '../services';
import { User } from '../types';

export function useUserActions() {
  const queryClient = useQueryClient();

  const deleteUserMutation = useMutation({
    mutationFn: userAPI.deleteUser,
    onSuccess: (_, userId) => {
      // Optimistic update
      queryClient.setQueryData<User[]>(['users'], (old) =>
        old?.filter(user => user.id !== userId) ?? []
      );

      // Invalidate related queries
      queryClient.invalidateQueries({ queryKey: ['users'] });
      queryClient.invalidateQueries({ queryKey: ['user-stats'] });
    },
    onError: (error) => {
      console.error('Failed to delete user:', error);
      // Show error notification
    },
  });

  const updateUserMutation = useMutation({
    mutationFn: ({ id, data }: { id: string; data: Partial<User> }) =>
      userAPI.updateUser(id, data),
    onSuccess: (updatedUser) => {
      // Update cache
      queryClient.setQueryData<User>(['user', updatedUser.id], updatedUser);
      queryClient.invalidateQueries({ queryKey: ['users'] });
    },
  });

  return {
    deleteUser: deleteUserMutation.mutate,
    isDeleting: deleteUserMutation.isPending,
    updateUser: updateUserMutation.mutate,
    isUpdating: updateUserMutation.isPending,
  };
}

// 5. Service Layer Pattern
// features/user-management/services/userAPI.ts
import { apiClient } from '@/shared/services/apiClient';
import { User, CreateUserData, UpdateUserData } from '../types';

export const userAPI = {
  async getUsers(): Promise<User[]> {
    const response = await apiClient.get('/users');
    return response.data;
  },

  async getUser(id: string): Promise<User> {
    const response = await apiClient.get(`/users/${id}`);
    return response.data;
  },

  async createUser(data: CreateUserData): Promise<User> {
    const response = await apiClient.post('/users', data);
    return response.data;
  },

  async updateUser(id: string, data: UpdateUserData): Promise<User> {
    const response = await apiClient.put(`/users/${id}`, data);
    return response.data;
  },

  async deleteUser(id: string): Promise<void> {
    await apiClient.delete(`/users/${id}`);
  },

  async searchUsers(query: string): Promise<User[]> {
    const response = await apiClient.get('/users/search', {
      params: { q: query }
    });
    return response.data;
  },
};

// 6. State Management Organization
// features/user-management/store/userSlice.ts
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { userAPI } from '../services';
import { User } from '../types';

interface UserState {
  users: User[];
  selectedUser: User | null;
  loading: boolean;
  error: string | null;
  filters: {
    search: string;
    role: string;
    status: string;
  };
}

const initialState: UserState = {
  users: [],
  selectedUser: null,
  loading: false,
  error: null,
  filters: {
    search: '',
    role: '',
    status: '',
  },
};

// Async thunks
export const fetchUsers = createAsyncThunk(
  'users/fetchUsers',
  async (_, { rejectWithValue }) => {
    try {
      return await userAPI.getUsers();
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

export const searchUsers = createAsyncThunk(
  'users/searchUsers',
  async (query: string, { rejectWithValue }) => {
    try {
      return await userAPI.searchUsers(query);
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

const userSlice = createSlice({
  name: 'users',
  initialState,
  reducers: {
    setSelectedUser: (state, action) => {
      state.selectedUser = action.payload;
    },
    clearSelectedUser: (state) => {
      state.selectedUser = null;
    },
    updateFilters: (state, action) => {
      state.filters = { ...state.filters, ...action.payload };
    },
    clearError: (state) => {
      state.error = null;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchUsers.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchUsers.fulfilled, (state, action) => {
        state.loading = false;
        state.users = action.payload;
      })
      .addCase(fetchUsers.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload as string;
      })
      .addCase(searchUsers.fulfilled, (state, action) => {
        state.users = action.payload;
      });
  },
});

export const {
  setSelectedUser,
  clearSelectedUser,
  updateFilters,
  clearError
} = userSlice.actions;

export default userSlice.reducer;

// Selectors
export const selectUsers = (state: RootState) => state.users.users;
export const selectSelectedUser = (state: RootState) => state.users.selectedUser;
export const selectUsersLoading = (state: RootState) => state.users.loading;
export const selectUsersError = (state: RootState) => state.users.error;
export const selectUserFilters = (state: RootState) => state.users.filters;

// 7. Type Definitions Organization
// features/user-management/types/user.ts
export interface User {
  id: string;
  name: string;
  email: string;
  avatar?: string;
  role: UserRole;
  status: UserStatus;
  createdAt: string;
  updatedAt: string;
}

export type UserRole = 'admin' | 'user' | 'moderator';
export type UserStatus = 'active' | 'inactive' | 'pending';

export interface CreateUserData {
  name: string;
  email: string;
  role: UserRole;
  password: string;
}

export interface UpdateUserData {
  name?: string;
  email?: string;
  role?: UserRole;
  status?: UserStatus;
}

export interface UserFilters {
  search?: string;
  role?: UserRole;
  status?: UserStatus;
  page?: number;
  limit?: number;
}

// features/user-management/types/index.ts
export type {
  User,
  UserRole,
  UserStatus,
  CreateUserData,
  UpdateUserData,
  UserFilters
} from './user';

// 8. Testing Organization
// features/user-management/components/UserCard/UserCard.test.tsx
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { UserCard } from './UserCard';
import { mockUser } from '../../__mocks__/userData';

const createWrapper = () => {
  const queryClient = new QueryClient({
    defaultOptions: { queries: { retry: false } },
  });

  return ({ children }: { children: React.ReactNode }) => (
    <QueryClientProvider client={queryClient}>
      {children}
    </QueryClientProvider>
  );
};

describe('UserCard', () => {
  it('renders user information correctly', () => {
    render(<UserCard user={mockUser} />, { wrapper: createWrapper() });

    expect(screen.getByText(mockUser.name)).toBeInTheDocument();
    expect(screen.getByText(mockUser.email)).toBeInTheDocument();
  });

  it('calls onEdit when edit button is clicked', () => {
    const onEdit = jest.fn();
    render(
      <UserCard user={mockUser} onEdit={onEdit} />,
      { wrapper: createWrapper() }
    );

    fireEvent.click(screen.getByText('Edit'));
    expect(onEdit).toHaveBeenCalledWith(mockUser);
  });

  it('shows confirmation dialog when delete is clicked', async () => {
    const onDelete = jest.fn();
    window.confirm = jest.fn(() => true);

    render(
      <UserCard user={mockUser} onDelete={onDelete} />,
      { wrapper: createWrapper() }
    );

    fireEvent.click(screen.getByText('Delete'));

    expect(window.confirm).toHaveBeenCalled();
  });
});
```

### 11. Advanced React Performance Optimization

#### Q26: Deep dive React performance optimization techniques?

**Trả lời:**

```javascript
// 1. Advanced Memoization Strategies
// ✅ Smart memoization với selective dependencies
function ExpensiveCalculation({ data, filters, config }) {
  // Memoize expensive calculations với selective dependencies
  const processedData = useMemo(() => {
    console.log('Processing data...'); // Should only log when data changes

    return data
      .filter(item => filters.includes(item.category))
      .map(item => ({
        ...item,
        score: calculateComplexScore(item, config.weights),
        trend: calculateTrend(item.history)
      }))
      .sort((a, b) => b.score - a.score);
  }, [data, filters]); // config intentionally excluded for performance

  // Separate memoization cho independent calculations
  const aggregatedStats = useMemo(() => {
    return {
      total: processedData.length,
      averageScore: processedData.reduce((sum, item) => sum + item.score, 0) / processedData.length,
      topPerformers: processedData.slice(0, 10)
    };
  }, [processedData]);

  // Memoize callbacks với stable references
  const handleItemClick = useCallback((itemId) => {
    // Use functional update to avoid dependencies
    setSelectedItems(prev =>
      prev.includes(itemId)
        ? prev.filter(id => id !== itemId)
        : [...prev, itemId]
    );
  }, []); // No dependencies needed

  return (
    <div>
      <StatsDisplay stats={aggregatedStats} />
      <ItemList
        items={processedData}
        onItemClick={handleItemClick}
      />
    </div>
  );
}

// 2. Component Splitting và Virtualization
// ✅ Split heavy components into lighter ones
function HeavyDashboard({ data }) {
  const [activeTab, setActiveTab] = useState('overview');

  return (
    <div>
      <TabNavigation activeTab={activeTab} onTabChange={setActiveTab} />

      {/* Only render active tab content */}
      <Suspense fallback={<TabSkeleton />}>
        {activeTab === 'overview' && <OverviewTab data={data} />}
        {activeTab === 'analytics' && <AnalyticsTab data={data} />}
        {activeTab === 'reports' && <ReportsTab data={data} />}
      </Suspense>
    </div>
  );
}

// Advanced virtualization với dynamic heights
function AdvancedVirtualList({ items, estimatedItemSize = 50 }) {
  const parentRef = useRef();
  const rowVirtualizer = useVirtualizer({
    count: items.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => estimatedItemSize,
    overscan: 5, // Render 5 extra items for smooth scrolling
  });

  return (
    <div
      ref={parentRef}
      style={{
        height: 400,
        overflow: 'auto',
      }}
    >
      <div
        style={{
          height: rowVirtualizer.getTotalSize(),
          width: '100%',
          position: 'relative',
        }}
      >
        {rowVirtualizer.getVirtualItems().map((virtualRow) => {
          const item = items[virtualRow.index];

          return (
            <div
              key={virtualRow.index}
              style={{
                position: 'absolute',
                top: 0,
                left: 0,
                width: '100%',
                height: virtualRow.size,
                transform: `translateY(${virtualRow.start}px)`,
              }}
            >
              <ComplexListItem
                item={item}
                onHeightChange={(height) => {
                  rowVirtualizer.measureElement(virtualRow.index, height);
                }}
              />
            </div>
          );
        })}
      </div>
    </div>
  );
}

// 3. State Management Optimization
// ✅ Optimized state updates với batching
function OptimizedStateManager() {
  const [state, setState] = useState({
    users: [],
    filters: { search: '', category: 'all' },
    pagination: { page: 1, limit: 20 },
    loading: false,
    error: null
  });

  // Batch multiple state updates
  const updateMultipleStates = useCallback((updates) => {
    setState(prevState => ({
      ...prevState,
      ...updates
    }));
  }, []);

  // Optimized search with debouncing
  const debouncedSearch = useMemo(
    () => debounce((searchTerm) => {
      updateMultipleStates({
        filters: { ...state.filters, search: searchTerm },
        pagination: { ...state.pagination, page: 1 },
        loading: true
      });
    }, 300),
    [state.filters, state.pagination, updateMultipleStates]
  );

  // Cleanup debounced function
  useEffect(() => {
    return () => {
      debouncedSearch.cancel();
    };
  }, [debouncedSearch]);

  return {
    state,
    updateMultipleStates,
    debouncedSearch
  };
}

// 4. Render Optimization Patterns
// ✅ Prevent unnecessary re-renders
const OptimizedParent = React.memo(function OptimizedParent({
  data,
  config,
  onAction
}) {
  // Split state to minimize re-renders
  const [uiState, setUiState] = useState({ expanded: false, selected: null });
  const [dataState, setDataState] = useState({ processed: null, loading: false });

  // Stable callback references
  const handleToggle = useCallback(() => {
    setUiState(prev => ({ ...prev, expanded: !prev.expanded }));
  }, []);

  const handleSelection = useCallback((id) => {
    setUiState(prev => ({ ...prev, selected: id }));
  }, []);

  // Memoize expensive operations
  const processedData = useMemo(() => {
    if (!data) return [];

    return data.map(item => ({
      ...item,
      calculated: expensiveCalculation(item, config)
    }));
  }, [data, config]);

  return (
    <div>
      {/* UI-only state doesn't affect data processing */}
      <Header
        expanded={uiState.expanded}
        onToggle={handleToggle}
      />

      {/* Data changes don't affect UI state */}
      <DataDisplay
        data={processedData}
        selected={uiState.selected}
        onSelect={handleSelection}
        onAction={onAction}
      />
    </div>
  );
}, (prevProps, nextProps) => {
  // Custom comparison for complex props
  return (
    prevProps.data.length === nextProps.data.length &&
    prevProps.config.version === nextProps.config.version &&
    prevProps.onAction === nextProps.onAction
  );
});

// 5. Bundle Size Optimization
// ✅ Code splitting với strategic loading
const LazyLoadedComponents = {
  // Critical components - load immediately
  Dashboard: React.lazy(() => import('./Dashboard')),

  // Secondary components - load on demand
  Reports: React.lazy(() =>
    import(/* webpackChunkName: "reports" */ './Reports')
  ),

  // Heavy components - load with preload strategy
  DataVisualization: React.lazy(() =>
    import(/* webpackChunkName: "viz", webpackPreload: true */ './DataVisualization')
  ),
};

// Smart preloading strategy
function usePreloader() {
  const [preloadedComponents, setPreloadedComponents] = useState(new Set());

  const preloadComponent = useCallback((componentName) => {
    if (preloadedComponents.has(componentName)) return;

    // Use requestIdleCallback for non-critical preloading
    requestIdleCallback(() => {
      LazyLoadedComponents[componentName];
      setPreloadedComponents(prev => new Set([...prev, componentName]));
    });
  }, [preloadedComponents]);

  // Preload on hover
  const preloadOnHover = useCallback((componentName) => ({
    onMouseEnter: () => preloadComponent(componentName),
    onFocus: () => preloadComponent(componentName),
  }), [preloadComponent]);

  return { preloadComponent, preloadOnHover };
}

// 6. Memory Management & Cleanup
// ✅ Advanced cleanup patterns
function useResourceCleanup() {
  const subscriptionsRef = useRef(new Set());
  const timeoutsRef = useRef(new Set());
  const intervalsRef = useRef(new Set());

  const addSubscription = useCallback((subscription) => {
    subscriptionsRef.current.add(subscription);
    return () => subscriptionsRef.current.delete(subscription);
  }, []);

  const addTimeout = useCallback((timeoutId) => {
    timeoutsRef.current.add(timeoutId);
    return () => {
      clearTimeout(timeoutId);
      timeoutsRef.current.delete(timeoutId);
    };
  }, []);

  const addInterval = useCallback((intervalId) => {
    intervalsRef.current.add(intervalId);
    return () => {
      clearInterval(intervalId);
      intervalsRef.current.delete(intervalId);
    };
  }, []);

  // Cleanup all resources
  useEffect(() => {
    return () => {
      // Cleanup subscriptions
      subscriptionsRef.current.forEach(subscription => {
        if (typeof subscription.unsubscribe === 'function') {
          subscription.unsubscribe();
        } else if (typeof subscription === 'function') {
          subscription();
        }
      });

      // Cleanup timeouts
      timeoutsRef.current.forEach(clearTimeout);

      // Cleanup intervals
      intervalsRef.current.forEach(clearInterval);

      // Clear all refs
      subscriptionsRef.current.clear();
      timeoutsRef.current.clear();
      intervalsRef.current.clear();
    };
  }, []);

  return { addSubscription, addTimeout, addInterval };
}

// 7. Performance Monitoring Integration
function usePerformanceMonitoring(componentName) {
  const renderCountRef = useRef(0);
  const mountTimeRef = useRef(Date.now());

  useEffect(() => {
    renderCountRef.current++;

    // Track render performance
    const renderTime = Date.now() - mountTimeRef.current;

    if (renderTime > 100) { // Slow render threshold
      console.warn(`Slow render detected in ${componentName}: ${renderTime}ms`);

      // Report to analytics
      if (window.analytics) {
        window.analytics.track('Slow Render', {
          component: componentName,
          renderTime,
          renderCount: renderCountRef.current
        });
      }
    }
  });

  // Track component lifecycle
  useEffect(() => {
    const mountTime = Date.now();

    return () => {
      const unmountTime = Date.now();
      const componentLifetime = unmountTime - mountTime;

      // Report component metrics
      if (window.analytics) {
        window.analytics.track('Component Unmount', {
          component: componentName,
          lifetime: componentLifetime,
          totalRenders: renderCountRef.current
        });
      }
    };
  }, [componentName]);
}

// 8. Network Optimization
function useOptimizedFetching() {
  const [cache, setCache] = useState(new Map());
  const abortControllersRef = useRef(new Map());

  const fetchWithOptimization = useCallback(async (url, options = {}) => {
    // Check cache first
    const cacheKey = `${url}${JSON.stringify(options)}`;
    const cached = cache.get(cacheKey);

    if (cached && Date.now() - cached.timestamp < 5 * 60 * 1000) { // 5 min cache
      return cached.data;
    }

    // Cancel previous request for same URL
    const existingController = abortControllersRef.current.get(url);
    if (existingController) {
      existingController.abort();
    }

    // Create new abort controller
    const controller = new AbortController();
    abortControllersRef.current.set(url, controller);

    try {
      const response = await fetch(url, {
        ...options,
        signal: controller.signal,
      });

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }

      const data = await response.json();

      // Update cache
      setCache(prev => new Map(prev.set(cacheKey, {
        data,
        timestamp: Date.now()
      })));

      return data;
    } finally {
      abortControllersRef.current.delete(url);
    }
  }, [cache]);

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      abortControllersRef.current.forEach(controller => controller.abort());
      abortControllersRef.current.clear();
    };
  }, []);

  return { fetchWithOptimization, clearCache: () => setCache(new Map()) };
}

// Usage example combining all optimizations
function HighPerformanceApp() {
  const { preloadOnHover } = usePreloader();
  const { addSubscription, addTimeout } = useResourceCleanup();
  const { fetchWithOptimization } = useOptimizedFetching();

  usePerformanceMonitoring('HighPerformanceApp');

  return (
    <div>
      <nav>
        <button {...preloadOnHover('Reports')}>
          Reports
        </button>
        <button {...preloadOnHover('DataVisualization')}>
          Analytics
        </button>
      </nav>

      <Suspense fallback={<LoadingSkeleton />}>
        <Routes>
          <Route path="/reports" element={<LazyLoadedComponents.Reports />} />
          <Route path="/analytics" element={<LazyLoadedComponents.DataVisualization />} />
        </Routes>
      </Suspense>
    </div>
  );
}
```

#### Q27: Testing strategies cho React applications?

**Trả lời:**

```javascript
// 1. Unit Testing với React Testing Library
// ✅ Component testing với best practices
import { render, screen, fireEvent, waitFor, within } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { BrowserRouter } from 'react-router-dom';
import { UserProfile } from './UserProfile';
import { mockUser, mockUserPosts } from '../__mocks__/userData';

// Test utilities
const createTestWrapper = () => {
  const queryClient = new QueryClient({
    defaultOptions: {
      queries: { retry: false },
      mutations: { retry: false },
    },
  });

  return function TestWrapper({ children }) {
    return (
      <QueryClientProvider client={queryClient}>
        <BrowserRouter>
          {children}
        </BrowserRouter>
      </QueryClientProvider>
    );
  };
};

// Mock API calls
jest.mock('../services/userAPI', () => ({
  userAPI: {
    getUser: jest.fn(),
    getUserPosts: jest.fn(),
    followUser: jest.fn(),
  },
}));

describe('UserProfile Component', () => {
  const user = userEvent.setup();
  let mockGetUser, mockGetUserPosts, mockFollowUser;

  beforeEach(() => {
    mockGetUser = require('../services/userAPI').userAPI.getUser;
    mockGetUserPosts = require('../services/userAPI').userAPI.getUserPosts;
    mockFollowUser = require('../services/userAPI').userAPI.followUser;

    // Reset mocks
    jest.clearAllMocks();
  });

  it('renders user information correctly', async () => {
    mockGetUser.mockResolvedValue(mockUser);
    mockGetUserPosts.mockResolvedValue(mockUserPosts);

    render(<UserProfile userId="123" />, { wrapper: createTestWrapper() });

    // Test loading state
    expect(screen.getByText('Loading...')).toBeInTheDocument();

    // Wait for data to load
    await waitFor(() => {
      expect(screen.getByText(mockUser.name)).toBeInTheDocument();
    });

    // Test rendered content
    expect(screen.getByText(mockUser.email)).toBeInTheDocument();
    expect(screen.getByAltText(`${mockUser.name}'s avatar`)).toBeInTheDocument();
    expect(screen.getByText(`${mockUser.followersCount} followers`)).toBeInTheDocument();
  });

  it('handles follow/unfollow functionality', async () => {
    mockGetUser.mockResolvedValue({ ...mockUser, isFollowing: false });
    mockFollowUser.mockResolvedValue({ ...mockUser, isFollowing: true });

    render(<UserProfile userId="123" />, { wrapper: createTestWrapper() });

    await waitFor(() => {
      expect(screen.getByText(mockUser.name)).toBeInTheDocument();
    });

    const followButton = screen.getByRole('button', { name: /follow/i });
    await user.click(followButton);

    expect(mockFollowUser).toHaveBeenCalledWith('123');

    await waitFor(() => {
      expect(screen.getByRole('button', { name: /unfollow/i })).toBeInTheDocument();
    });
  });

  it('displays error state when user fetch fails', async () => {
    const errorMessage = 'User not found';
    mockGetUser.mockRejectedValue(new Error(errorMessage));

    render(<UserProfile userId="invalid" />, { wrapper: createTestWrapper() });

    await waitFor(() => {
      expect(screen.getByText(/error loading user/i)).toBeInTheDocument();
      expect(screen.getByText(errorMessage)).toBeInTheDocument();
    });
  });

  it('filters posts when search term is entered', async () => {
    mockGetUser.mockResolvedValue(mockUser);
    mockGetUserPosts.mockResolvedValue(mockUserPosts);

    render(<UserProfile userId="123" />, { wrapper: createTestWrapper() });

    await waitFor(() => {
      expect(screen.getByText(mockUser.name)).toBeInTheDocument();
    });

    // All posts should be visible initially
    expect(screen.getAllByTestId('post-item')).toHaveLength(mockUserPosts.length);

    // Search for specific post
    const searchInput = screen.getByPlaceholderText('Search posts...');
    await user.type(searchInput, 'react');

    // Only posts containing 'react' should be visible
    await waitFor(() => {
      const visiblePosts = screen.getAllByTestId('post-item');
      expect(visiblePosts.length).toBeLessThan(mockUserPosts.length);
    });
  });
});

// 2. Integration Testing
// ✅ Multi-component integration tests
describe('UserProfile Integration', () => {
  it('loads user profile and allows interaction with posts', async () => {
    const user = userEvent.setup();

    // Mock complete user flow
    mockGetUser.mockResolvedValue(mockUser);
    mockGetUserPosts.mockResolvedValue(mockUserPosts);

    render(<UserProfile userId="123" />, { wrapper: createTestWrapper() });

    // Wait for profile to load
    await waitFor(() => {
      expect(screen.getByText(mockUser.name)).toBeInTheDocument();
    });

    // Test posts section
    const postsSection = screen.getByTestId('user-posts');
    expect(postsSection).toBeInTheDocument();

    // Test post interaction
    const firstPost = within(postsSection).getAllByTestId('post-item')[0];
    const likeButton = within(firstPost).getByRole('button', { name: /like/i });

    await user.click(likeButton);

    // Verify like action
    expect(within(firstPost).getByText(/liked/i)).toBeInTheDocument();
  });
});

// 3. Custom Hooks Testing
// ✅ Testing custom hooks in isolation
import { renderHook, act } from '@testing-library/react';
import { useUserActions } from '../hooks/useUserActions';

describe('useUserActions Hook', () => {
  const wrapper = createTestWrapper();

  it('provides user action functions', () => {
    const { result } = renderHook(() => useUserActions(), { wrapper });

    expect(result.current.followUser).toBeInstanceOf(Function);
    expect(result.current.unfollowUser).toBeInstanceOf(Function);
    expect(result.current.isFollowing).toBe(false);
    expect(result.current.isLoading).toBe(false);
  });

  it('handles follow user action', async () => {
    mockFollowUser.mockResolvedValue({ success: true });

    const { result } = renderHook(() => useUserActions(), { wrapper });

    await act(async () => {
      await result.current.followUser('123');
    });

    expect(mockFollowUser).toHaveBeenCalledWith('123');
    expect(result.current.isFollowing).toBe(true);
  });

  it('handles follow error gracefully', async () => {
    const errorMessage = 'Failed to follow user';
    mockFollowUser.mockRejectedValue(new Error(errorMessage));

    const { result } = renderHook(() => useUserActions(), { wrapper });

    await act(async () => {
      try {
        await result.current.followUser('123');
      } catch (error) {
        expect(error.message).toBe(errorMessage);
      }
    });

    expect(result.current.isFollowing).toBe(false);
    expect(result.current.error).toBe(errorMessage);
  });
});

// 4. E2E Testing với Cypress
// ✅ End-to-end user flows
// cypress/integration/user-profile.spec.js
describe('User Profile E2E', () => {
  beforeEach(() => {
    // Mock API responses
    cy.intercept('GET', '/api/users/123', { fixture: 'user.json' }).as('getUser');
    cy.intercept('GET', '/api/users/123/posts', { fixture: 'userPosts.json' }).as('getPosts');
    cy.intercept('POST', '/api/users/123/follow', { success: true }).as('followUser');

    cy.visit('/users/123');
  });

  it('displays user profile and allows following', () => {
    // Wait for data to load
    cy.wait(['@getUser', '@getPosts']);

    // Verify profile information
    cy.get('[data-testid="user-name"]').should('contain', 'John Doe');
    cy.get('[data-testid="user-email"]').should('contain', 'john@example.com');
    cy.get('[data-testid="followers-count"]').should('contain', '1,234 followers');

    // Test follow functionality
    cy.get('[data-testid="follow-button"]').click();
    cy.wait('@followUser');

    cy.get('[data-testid="follow-button"]')
      .should('contain', 'Unfollow')
      .and('have.class', 'following');

    // Verify follower count updated
    cy.get('[data-testid="followers-count"]').should('contain', '1,235 followers');
  });

  it('filters posts by search term', () => {
    cy.wait(['@getUser', '@getPosts']);

    // Count total posts
    cy.get('[data-testid="post-item"]').should('have.length.greaterThan', 0);
    cy.get('[data-testid="post-item"]').its('length').as('totalPosts');

    // Search for specific posts
    cy.get('[data-testid="search-posts"]').type('react');

    // Verify filtered results
    cy.get('[data-testid="post-item"]').should('have.length.lessThan', '@totalPosts');
    cy.get('[data-testid="post-item"]').each(($post) => {
      cy.wrap($post).should('contain.text', 'react');
    });
  });

  it('handles navigation between user sections', () => {
    cy.wait(['@getUser', '@getPosts']);

    // Test tab navigation
    cy.get('[data-testid="posts-tab"]').should('have.class', 'active');

    cy.get('[data-testid="followers-tab"]').click();
    cy.get('[data-testid="followers-tab"]').should('have.class', 'active');
    cy.get('[data-testid="followers-list"]').should('be.visible');

    cy.get('[data-testid="following-tab"]').click();
    cy.get('[data-testid="following-tab"]').should('have.class', 'active');
    cy.get('[data-testid="following-list"]').should('be.visible');
  });
});

// 5. Performance Testing
// ✅ Performance regression testing
describe('Performance Tests', () => {
  it('renders large user list efficiently', async () => {
    const largeUserList = Array.from({ length: 1000 }, (_, i) => ({
      id: i,
      name: `User ${i}`,
      email: `user${i}@example.com`,
    }));

    const startTime = performance.now();

    render(<UserList users={largeUserList} />, { wrapper: createTestWrapper() });

    await waitFor(() => {
      expect(screen.getByTestId('user-list')).toBeInTheDocument();
    });

    const renderTime = performance.now() - startTime;

    // Assert render time is under threshold
    expect(renderTime).toBeLessThan(100); // 100ms threshold
  });

  it('handles rapid state updates without performance degradation', async () => {
    const user = userEvent.setup();

    render(<SearchableUserList />, { wrapper: createTestWrapper() });

    const searchInput = screen.getByPlaceholderText('Search users...');

    const startTime = performance.now();

    // Simulate rapid typing
    await user.type(searchInput, 'john doe test search');

    const typingTime = performance.now() - startTime;

    // Verify responsive typing
    expect(typingTime).toBeLessThan(500); // 500ms for full typing sequence

    // Verify final results
    await waitFor(() => {
      expect(screen.getByDisplayValue('john doe test search')).toBeInTheDocument();
    });
  });
});

// 6. Accessibility Testing
// ✅ A11y testing with jest-axe
import { axe, toHaveNoViolations } from 'jest-axe';

expect.extend(toHaveNoViolations);

describe('Accessibility Tests', () => {
  it('has no accessibility violations', async () => {
    mockGetUser.mockResolvedValue(mockUser);

    const { container } = render(
      <UserProfile userId="123" />,
      { wrapper: createTestWrapper() }
    );

    await waitFor(() => {
      expect(screen.getByText(mockUser.name)).toBeInTheDocument();
    });

    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });

  it('supports keyboard navigation', async () => {
    mockGetUser.mockResolvedValue(mockUser);

    render(<UserProfile userId="123" />, { wrapper: createTestWrapper() });

    await waitFor(() => {
      expect(screen.getByText(mockUser.name)).toBeInTheDocument();
    });

    // Test tab navigation
    const followButton = screen.getByRole('button', { name: /follow/i });

    followButton.focus();
    expect(followButton).toHaveFocus();

    // Test Enter key activation
    fireEvent.keyDown(followButton, { key: 'Enter', code: 'Enter' });
    expect(mockFollowUser).toHaveBeenCalled();
  });
});

// 7. Visual Regression Testing
// ✅ Screenshot testing với Storybook
// UserProfile.stories.js
export default {
  title: 'Components/UserProfile',
  component: UserProfile,
  parameters: {
    docs: {
      description: {
        component: 'User profile component with follow functionality'
      }
    }
  }
};

export const Default = {
  args: {
    userId: '123'
  },
  parameters: {
    mockData: [
      {
        url: '/api/users/123',
        method: 'GET',
        status: 200,
        response: mockUser
      }
    ]
  }
};

export const LoadingState = {
  args: {
    userId: '123'
  },
  parameters: {
    mockData: [
      {
        url: '/api/users/123',
        method: 'GET',
        status: 200,
        response: mockUser,
        delay: 2000 // Simulate slow loading
      }
    ]
  }
};

export const ErrorState = {
  args: {
    userId: 'invalid'
  },
  parameters: {
    mockData: [
      {
        url: '/api/users/invalid',
        method: 'GET',
        status: 404,
        response: { error: 'User not found' }
      }
    ]
  }
};

// Chromatic configuration for visual testing
// .storybook/main.js
module.exports = {
  addons: ['@storybook/addon-essentials'],
  features: {
    buildStoriesJson: true
  }
};
```

#### Q28: Accessibility (A11y) best practices trong React?

**Trả lời:**

```javascript
// 1. Semantic HTML và ARIA Attributes
// ✅ Proper semantic structure
function AccessibleForm() {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    confirmPassword: '',
    agreeToTerms: false
  });
  const [errors, setErrors] = useState({});
  const [isSubmitting, setIsSubmitting] = useState(false);

  const validateForm = () => {
    const newErrors = {};

    if (!formData.email) {
      newErrors.email = 'Email is required';
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
      newErrors.email = 'Please enter a valid email address';
    }

    if (!formData.password) {
      newErrors.password = 'Password is required';
    } else if (formData.password.length < 8) {
      newErrors.password = 'Password must be at least 8 characters';
    }

    if (formData.password !== formData.confirmPassword) {
      newErrors.confirmPassword = 'Passwords do not match';
    }

    if (!formData.agreeToTerms) {
      newErrors.agreeToTerms = 'You must agree to the terms';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!validateForm()) {
      // Focus first error field
      const firstErrorField = Object.keys(errors)[0];
      document.getElementById(firstErrorField)?.focus();
      return;
    }

    setIsSubmitting(true);
    try {
      await submitForm(formData);
    } catch (error) {
      setErrors({ submit: 'Submission failed. Please try again.' });
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} noValidate>
      {/* Form heading */}
      <h1 id="form-title">Create Account</h1>

      {/* Form description */}
      <p id="form-description">
        Fill out the form below to create your new account.
      </p>

      {/* Global form error */}
      {errors.submit && (
        <div
          role="alert"
          aria-live="polite"
          className="error-message global-error"
        >
          {errors.submit}
        </div>
      )}

      {/* Email field */}
      <div className="form-group">
        <label htmlFor="email" className="required">
          Email Address
        </label>
        <input
          id="email"
          type="email"
          value={formData.email}
          onChange={(e) => setFormData(prev => ({
            ...prev,
            email: e.target.value
          }))}
          aria-invalid={errors.email ? 'true' : 'false'}
          aria-describedby={errors.email ? 'email-error' : 'email-help'}
          aria-required="true"
          autoComplete="email"
        />
        <div id="email-help" className="help-text">
          We'll never share your email with anyone else.
        </div>
        {errors.email && (
          <div
            id="email-error"
            role="alert"
            className="error-message"
            aria-live="polite"
          >
            {errors.email}
          </div>
        )}
      </div>

      {/* Password field with strength indicator */}
      <div className="form-group">
        <label htmlFor="password" className="required">
          Password
        </label>
        <div className="password-container">
          <input
            id="password"
            type="password"
            value={formData.password}
            onChange={(e) => setFormData(prev => ({
              ...prev,
              password: e.target.value
            }))}
            aria-invalid={errors.password ? 'true' : 'false'}
            aria-describedby="password-requirements password-strength"
            aria-required="true"
            autoComplete="new-password"
          />
          <PasswordStrengthIndicator password={formData.password} />
        </div>

        <div id="password-requirements" className="help-text">
          Password must be at least 8 characters long.
        </div>

        {errors.password && (
          <div
            id="password-error"
            role="alert"
            className="error-message"
          >
            {errors.password}
          </div>
        )}
      </div>

      {/* Confirm password */}
      <div className="form-group">
        <label htmlFor="confirmPassword" className="required">
          Confirm Password
        </label>
        <input
          id="confirmPassword"
          type="password"
          value={formData.confirmPassword}
          onChange={(e) => setFormData(prev => ({
            ...prev,
            confirmPassword: e.target.value
          }))}
          aria-invalid={errors.confirmPassword ? 'true' : 'false'}
          aria-describedby={errors.confirmPassword ? 'confirm-password-error' : undefined}
          aria-required="true"
          autoComplete="new-password"
        />
        {errors.confirmPassword && (
          <div
            id="confirm-password-error"
            role="alert"
            className="error-message"
          >
            {errors.confirmPassword}
          </div>
        )}
      </div>

      {/* Checkbox with proper ARIA */}
      <div className="form-group">
        <label className="checkbox-label">
          <input
            id="agreeToTerms"
            type="checkbox"
            checked={formData.agreeToTerms}
            onChange={(e) => setFormData(prev => ({
              ...prev,
              agreeToTerms: e.target.checked
            }))}
            aria-invalid={errors.agreeToTerms ? 'true' : 'false'}
            aria-describedby={errors.agreeToTerms ? 'terms-error' : undefined}
            aria-required="true"
          />
          <span className="checkmark" aria-hidden="true"></span>
          I agree to the{' '}
          <a href="/terms" target="_blank" rel="noopener noreferrer">
            Terms of Service
            <span className="sr-only"> (opens in new tab)</span>
          </a>
        </label>
        {errors.agreeToTerms && (
          <div
            id="terms-error"
            role="alert"
            className="error-message"
          >
            {errors.agreeToTerms}
          </div>
        )}
      </div>

      {/* Submit button */}
      <button
        type="submit"
        disabled={isSubmitting}
        aria-describedby="submit-status"
      >
        {isSubmitting ? 'Creating Account...' : 'Create Account'}
      </button>

      {/* Screen reader status */}
      <div
        id="submit-status"
        aria-live="polite"
        aria-atomic="true"
        className="sr-only"
      >
        {isSubmitting ? 'Form is being submitted' : ''}
      </div>
    </form>
  );
}

// 2. Advanced ARIA Patterns
// ✅ Accessible Modal Dialog
function AccessibleModal({
  isOpen,
  onClose,
  title,
  children,
  initialFocus
}) {
  const modalRef = useRef(null);
  const previousFocusRef = useRef(null);

  // Focus management
  useEffect(() => {
    if (isOpen) {
      // Store previously focused element
      previousFocusRef.current = document.activeElement;

      // Focus modal or initial focus element
      setTimeout(() => {
        if (initialFocus) {
          initialFocus.current?.focus();
        } else {
          modalRef.current?.focus();
        }
      }, 0);

      // Trap focus within modal
      const handleTabKey = (e) => {
        if (e.key !== 'Tab') return;

        const focusableElements = modalRef.current?.querySelectorAll(
          'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
        );

        const firstElement = focusableElements?.[0];
        const lastElement = focusableElements?.[focusableElements.length - 1];

        if (e.shiftKey) {
          if (document.activeElement === firstElement) {
            e.preventDefault();
            lastElement?.focus();
          }
        } else {
          if (document.activeElement === lastElement) {
            e.preventDefault();
            firstElement?.focus();
          }
        }
      };

      document.addEventListener('keydown', handleTabKey);
      return () => document.removeEventListener('keydown', handleTabKey);
    } else {
      // Return focus to previously focused element
      previousFocusRef.current?.focus();
    }
  }, [isOpen, initialFocus]);

  // Escape key handler
  useEffect(() => {
    const handleEscape = (e) => {
      if (e.key === 'Escape' && isOpen) {
        onClose();
      }
    };

    document.addEventListener('keydown', handleEscape);
    return () => document.removeEventListener('keydown', handleEscape);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  return (
    <>
      {/* Backdrop */}
      <div
        className="modal-backdrop"
        onClick={onClose}
        aria-hidden="true"
      />

      {/* Modal */}
      <div
        ref={modalRef}
        role="dialog"
        aria-modal="true"
        aria-labelledby="modal-title"
        aria-describedby="modal-description"
        className="modal"
        tabIndex={-1}
      >
        <div className="modal-content">
          {/* Header */}
          <div className="modal-header">
            <h2 id="modal-title">{title}</h2>
            <button
              onClick={onClose}
              aria-label="Close dialog"
              className="modal-close"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </div>

          {/* Body */}
          <div id="modal-description" className="modal-body">
            {children}
          </div>
        </div>
      </div>
    </>
  );
}

// 3. Accessible Data Tables
// ✅ Complex data table with sorting and filtering
function AccessibleDataTable({ data, columns, caption }) {
  const [sortConfig, setSortConfig] = useState({ key: null, direction: 'asc' });
  const [filter, setFilter] = useState('');
  const [currentPage, setCurrentPage] = useState(1);
  const [announceSort, setAnnounceSort] = useState('');

  const filteredData = useMemo(() => {
    return data.filter(item =>
      Object.values(item).some(value =>
        value.toString().toLowerCase().includes(filter.toLowerCase())
      )
    );
  }, [data, filter]);

  const sortedData = useMemo(() => {
    if (!sortConfig.key) return filteredData;

    return [...filteredData].sort((a, b) => {
      const aVal = a[sortConfig.key];
      const bVal = b[sortConfig.key];

      if (aVal < bVal) return sortConfig.direction === 'asc' ? -1 : 1;
      if (aVal > bVal) return sortConfig.direction === 'asc' ? 1 : -1;
      return 0;
    });
  }, [filteredData, sortConfig]);

  const handleSort = (key) => {
    const direction =
      sortConfig.key === key && sortConfig.direction === 'asc'
        ? 'desc'
        : 'asc';

    setSortConfig({ key, direction });

    // Announce sort change to screen readers
    const column = columns.find(col => col.key === key);
    setAnnounceSort(
      `Table sorted by ${column.label} in ${direction}ending order`
    );
  };

  return (
    <div className="table-container">
      {/* Table controls */}
      <div className="table-controls">
        <label htmlFor="table-search">
          Search table:
        </label>
        <input
          id="table-search"
          type="search"
          value={filter}
          onChange={(e) => setFilter(e.target.value)}
          aria-describedby="search-help"
        />
        <div id="search-help" className="help-text">
          Search across all table columns
        </div>
      </div>

      {/* Live region for announcements */}
      <div
        aria-live="polite"
        aria-atomic="true"
        className="sr-only"
      >
        {announceSort}
      </div>

      {/* Table */}
      <table
        role="table"
        aria-label={caption}
        aria-rowcount={sortedData.length + 1} // +1 for header
      >
        <caption>{caption}</caption>

        <thead>
          <tr role="row" aria-rowindex={1}>
            {columns.map((column, index) => (
              <th
                key={column.key}
                role="columnheader"
                aria-colindex={index + 1}
                aria-sort={
                  sortConfig.key === column.key
                    ? sortConfig.direction === 'asc' ? 'ascending' : 'descending'
                    : 'none'
                }
                tabIndex={0}
                onClick={() => handleSort(column.key)}
                onKeyDown={(e) => {
                  if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    handleSort(column.key);
                  }
                }}
                className={`sortable ${sortConfig.key === column.key ? 'sorted' : ''}`}
              >
                {column.label}
                <span className="sort-indicator" aria-hidden="true">
                  {sortConfig.key === column.key
                    ? (sortConfig.direction === 'asc' ? ' ↑' : ' ↓')
                    : ' ↕'
                  }
                </span>
              </th>
            ))}
          </tr>
        </thead>

        <tbody>
          {sortedData.map((row, rowIndex) => (
            <tr
              key={row.id}
              role="row"
              aria-rowindex={rowIndex + 2}
            >
              {columns.map((column, colIndex) => (
                <td
                  key={column.key}
                  role="gridcell"
                  aria-colindex={colIndex + 1}
                >
                  {column.render ? column.render(row[column.key], row) : row[column.key]}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>

      {/* Table summary for screen readers */}
      <div className="sr-only">
        Showing {sortedData.length} of {data.length} rows
        {filter && ` filtered by "${filter}"`}
        {sortConfig.key && ` sorted by ${columns.find(c => c.key === sortConfig.key)?.label}`}
      </div>
    </div>
  );
}

// 4. Accessible Navigation
// ✅ Skip links and navigation landmarks
function AccessibleLayout({ children }) {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const menuButtonRef = useRef(null);

  return (
    <>
      {/* Skip links */}
      <div className="skip-links">
        <a href="#main-content" className="skip-link">
          Skip to main content
        </a>
        <a href="#main-navigation" className="skip-link">
          Skip to navigation
        </a>
        <a href="#footer" className="skip-link">
          Skip to footer
        </a>
      </div>

      {/* Header */}
      <header role="banner">
        <div className="header-content">
          <div className="logo">
            <a href="/" aria-label="Company name - Home">
              <img src="/logo.png" alt="Company Logo" />
            </a>
          </div>

          {/* Mobile menu button */}
          <button
            ref={menuButtonRef}
            className="menu-toggle"
            aria-expanded={isMenuOpen}
            aria-controls="main-navigation"
            aria-label="Toggle navigation menu"
            onClick={() => setIsMenuOpen(!isMenuOpen)}
          >
            <span className="hamburger" aria-hidden="true">
              <span></span>
              <span></span>
              <span></span>
            </span>
          </button>

          {/* Navigation */}
          <nav
            id="main-navigation"
            role="navigation"
            aria-label="Main navigation"
            className={isMenuOpen ? 'open' : ''}
          >
            <ul className="nav-list">
              <li>
                <a href="/products" aria-current="page">
                  Products
                </a>
              </li>
              <li>
                <a href="/services">Services</a>
              </li>
              <li>
                <a href="/about">About</a>
              </li>
              <li>
                <a href="/contact">Contact</a>
              </li>
            </ul>
          </nav>
        </div>
      </header>

      {/* Main content */}
      <main id="main-content" role="main">
        {children}
      </main>

      {/* Footer */}
      <footer id="footer" role="contentinfo">
        <div className="footer-content">
          <nav aria-label="Footer navigation">
            <ul>
              <li><a href="/privacy">Privacy Policy</a></li>
              <li><a href="/terms">Terms of Service</a></li>
              <li><a href="/accessibility">Accessibility</a></li>
            </ul>
          </nav>
          <p>&copy; 2024 Company Name. All rights reserved.</p>
        </div>
      </footer>
    </>
  );
}

// 5. Accessible Form Controls
// ✅ Custom accessible components
function AccessibleSelect({
  label,
  options,
  value,
  onChange,
  error,
  required = false,
  ...props
}) {
  const [isOpen, setIsOpen] = useState(false);
  const [focusedIndex, setFocusedIndex] = useState(-1);
  const selectRef = useRef(null);
  const optionsRef = useRef([]);

  const selectedOption = options.find(opt => opt.value === value);

  const handleKeyDown = (e) => {
    switch (e.key) {
      case 'ArrowDown':
        e.preventDefault();
        if (!isOpen) {
          setIsOpen(true);
        } else {
          setFocusedIndex(prev =>
            prev < options.length - 1 ? prev + 1 : 0
          );
        }
        break;

      case 'ArrowUp':
        e.preventDefault();
        if (isOpen) {
          setFocusedIndex(prev =>
            prev > 0 ? prev - 1 : options.length - 1
          );
        }
        break;

      case 'Enter':
      case ' ':
        e.preventDefault();
        if (!isOpen) {
          setIsOpen(true);
        } else if (focusedIndex >= 0) {
          onChange(options[focusedIndex].value);
          setIsOpen(false);
        }
        break;

      case 'Escape':
        setIsOpen(false);
        selectRef.current?.focus();
        break;

      case 'Tab':
        setIsOpen(false);
        break;
    }
  };

  return (
    <div className="select-container">
      <label htmlFor={props.id} className={required ? 'required' : ''}>
        {label}
      </label>

      <div className="custom-select">
        <button
          ref={selectRef}
          id={props.id}
          type="button"
          className="select-trigger"
          aria-expanded={isOpen}
          aria-haspopup="listbox"
          aria-labelledby={`${props.id}-label`}
          aria-invalid={error ? 'true' : 'false'}
          aria-describedby={error ? `${props.id}-error` : undefined}
          onClick={() => setIsOpen(!isOpen)}
          onKeyDown={handleKeyDown}
        >
          {selectedOption ? selectedOption.label : 'Select an option'}
          <span className="select-arrow" aria-hidden="true">▼</span>
        </button>

        {isOpen && (
          <ul
            role="listbox"
            aria-labelledby={`${props.id}-label`}
            className="select-options"
          >
            {options.map((option, index) => (
              <li
                key={option.value}
                ref={el => optionsRef.current[index] = el}
                role="option"
                aria-selected={value === option.value}
                className={`select-option ${
                  index === focusedIndex ? 'focused' : ''
                } ${value === option.value ? 'selected' : ''}`}
                onClick={() => {
                  onChange(option.value);
                  setIsOpen(false);
                }}
                onMouseEnter={() => setFocusedIndex(index)}
              >
                {option.label}
              </li>
            ))}
          </ul>
        )}
      </div>

      {error && (
        <div
          id={`${props.id}-error`}
          role="alert"
          className="error-message"
        >
          {error}
        </div>
      )}
    </div>
  );
}

// 6. Screen Reader Utilities
// ✅ Screen reader only content and live regions
function useAnnouncements() {
  const [announcement, setAnnouncement] = useState('');

  const announce = useCallback((message, priority = 'polite') => {
    setAnnouncement(''); // Clear first to ensure announcement
    setTimeout(() => {
      setAnnouncement(message);
    }, 10);
  }, []);

  const LiveRegion = useMemo(() =>
    function LiveRegion({ priority = 'polite' }) {
      return (
        <div
          aria-live={priority}
          aria-atomic="true"
          className="sr-only"
        >
          {announcement}
        </div>
      );
    }, [announcement]
  );

  return { announce, LiveRegion };
}

// Usage example
function NotificationSystem() {
  const { announce, LiveRegion } = useAnnouncements();
  const [notifications, setNotifications] = useState([]);

  const addNotification = (message, type = 'info') => {
    const id = Date.now();
    const notification = { id, message, type };

    setNotifications(prev => [...prev, notification]);

    // Announce to screen readers
    announce(`${type} notification: ${message}`);

    // Auto-remove after 5 seconds
    setTimeout(() => {
      removeNotification(id);
    }, 5000);
  };

  const removeNotification = (id) => {
    setNotifications(prev => prev.filter(n => n.id !== id));
    announce('Notification dismissed');
  };

  return (
    <div>
      {/* Notifications container */}
      <div
        className="notifications"
        role="region"
        aria-label="Notifications"
        aria-live="polite"
      >
        {notifications.map(notification => (
          <div
            key={notification.id}
            className={`notification ${notification.type}`}
            role="alert"
          >
            <span>{notification.message}</span>
            <button
              onClick={() => removeNotification(notification.id)}
              aria-label={`Dismiss ${notification.type} notification`}
            >
              ×
            </button>
          </div>
        ))}
      </div>

      {/* Live region for announcements */}
      <LiveRegion priority="polite" />

      {/* Test buttons */}
      <div>
        <button onClick={() => addNotification('Success message', 'success')}>
          Show Success
        </button>
        <button onClick={() => addNotification('Error message', 'error')}>
          Show Error
        </button>
      </div>
    </div>
  );
}

// 7. CSS Classes for Screen Readers
/*
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

.skip-link {
  position: absolute;
  top: -40px;
  left: 6px;
  background: #000;
  color: #fff;
  padding: 8px;
  text-decoration: none;
  z-index: 1000;
}

.skip-link:focus {
  top: 6px;
}
*/
```
