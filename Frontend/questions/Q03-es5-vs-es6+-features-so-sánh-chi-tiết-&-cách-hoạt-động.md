# ⚡ Q03: ES5 vs ES6+ Features - So Sánh Chi Tiết & Cách Hoạt Động

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

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

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    JAVASCRIPT EVOLUTION TIMELINE                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  📅 ES5 (2009) - Stable, Universal Support                              │
│     ✅ All browsers (IE9+)                                              │
│     ✅ No transpilation needed                                          │
│     ❌ Verbose syntax, limited features                                 │
│                                                                          │
│  📅 ES6/ES2015 (2015) - Major Update                                    │
│     • Classes, Modules, Arrow Functions                                 │
│     • let/const, Template Literals                                      │
│     • Destructuring, Spread/Rest                                        │
│     • Promises, Symbols, Iterators                                      │
│     ✅ Modern browsers (Chrome 51+, Firefox 54+, Safari 10+)           │
│     ⚠️  Needs Babel for IE11                                            │
│                                                                          │
│  📅 ES2016-ES2023 (Yearly Updates)                                      │
│     • Async/Await (ES2017)                                              │
│     • Optional Chaining ?. (ES2020)                                     │
│     • Nullish Coalescing ?? (ES2020)                                    │
│     • BigInt, Dynamic Import                                            │
│     • Private Fields, Top-level await                                   │
│     ✅ Evergreen browsers auto-update                                   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

**Code Example - Comprehensive Comparison:**

```typescript
// ============================================
// 1. VARIABLES - var vs let/const
// ============================================

// 🔴 ES5 - var (Function Scoped, Hoisted)
// Cách hoạt động: var được hoist lên đầu function scope
function es5Variables() {
  console.log(x); // undefined (hoisted nhưng chưa gán giá trị)
  var x = 10; // Function scoped - accessible trong toàn bộ function

  if (true) {
    var x = 20; // CÙNG biến x (không tạo scope mới)
  }

  console.log(x); // 20 (bị ghi đè bởi if block)

  // var có thể redeclare
  var x = 30; // ✅ OK - không error
  console.log(x); // 30
}

// 🟢 ES6+ - let/const (Block Scoped, Temporal Dead Zone)
// Cách hoạt động: let/const chỉ tồn tại trong {} block, có TDZ
function es6Variables() {
  // console.log(y); // ❌ ReferenceError: Cannot access before initialization
  // Temporal Dead Zone (TDZ) - từ đầu block đến khi declare

  let y = 10; // Block scoped - chỉ trong function này
  const z = 100; // Immutable reference - không thể reassign

  if (true) {
    let y = 20; // BIẾN MỚI - scope riêng trong if block
    const z = 200; // BIẾN MỚI - scope riêng

    console.log(y); // 20 (biến local của if)
    console.log(z); // 200
  }

  console.log(y); // 10 (biến của function scope, không bị ảnh hưởng)
  console.log(z); // 100

  // let y = 30;  // ❌ SyntaxError: Identifier 'y' has already been declared
  // z = 300;     // ❌ TypeError: Assignment to constant variable

  // const cho objects - reference immutable, nhưng properties mutable
  const obj = { name: 'John' };
  obj.name = 'Jane'; // ✅ OK - thay đổi property
  // obj = {};      // ❌ Error - không thể reassign reference
}

// Hoisting Comparison (Cách hoạt động của hoisting)
console.log('=== VAR HOISTING ===');
console.log(varVariable); // undefined - hoisted, chưa assigned
var varVariable = 'ES5';

console.log('=== LET/CONST HOISTING ===');
// console.log(letVariable); // ❌ ReferenceError - TDZ
let letVariable = 'ES6';
// const constVariable; // ❌ SyntaxError - const phải init ngay

// ============================================
// 2. FUNCTIONS - Regular vs Arrow
// ============================================

// 🔴 ES5 - Regular Functions (có own this binding)
// Cách hoạt động: this binding dynamic, phụ thuộc vào cách gọi
var Calculator = {
  value: 0,

  // Method với regular function
  add: function (num) {
    this.value += num; // this = Calculator object
    return this.value;
  },

  // Callback problem
  delayedAdd: function (num) {
    setTimeout(function () {
      // this ở đây = window (hoặc undefined trong strict mode)
      // Không phải Calculator object!
      console.log(this); // window/undefined
      // this.value += num; // ❌ Error hoặc NaN
    }, 1000);
  },

  // ES5 solution: bind hoặc that = this
  delayedAddFixed: function (num) {
    var that = this; // Lưu reference
    setTimeout(function () {
      that.value += num; // ✅ Hoạt động
    }, 1000);
  },

  // Hoặc dùng bind
  delayedAddBind: function (num) {
    setTimeout(
      function () {
        this.value += num; // ✅ Hoạt động vì đã bind
      }.bind(this),
      1000
    );
  },
};

// 🟢 ES6+ - Arrow Functions (lexical this binding)
// Cách hoạt động: Arrow function KHÔNG có own this, inherit từ parent scope
const ModernCalculator = {
  value: 0,

  // Method shorthand syntax
  add(num: number) {
    this.value += num;
    return this.value;
  },

  // Arrow function trong callback - this tự động đúng
  delayedAdd(num: number) {
    setTimeout(() => {
      // this = ModernCalculator (inherit từ delayedAdd method)
      this.value += num; // ✅ Hoạt động perfect
    }, 1000);
  },

  // Arrow function không thể dùng làm constructor
  // MyClass: () => { } // ❌ Không có prototype, không thể new
};

// Arrow function syntax variations
const simple = (x: number) => x * 2; // Implicit return (1 expression)
const withBlock = (x: number) => {
  const result = x * 2;
  return result; // Explicit return (multiple statements)
};
const noParams = () => console.log('Hello'); // No parameters
const oneParam = (x) => x * 2; // Single param - có thể bỏ ()
const multiParams = (x: number, y: number) => x + y; // Multiple params - cần ()
const returnObject = () => ({ name: 'John' }); // Return object - cần wrap ()

// ============================================
// 3. CLASSES - Prototype vs Class Syntax
// ============================================

// 🔴 ES5 - Prototype-based Inheritance
// Cách hoạt động: Constructor function + prototype chain
function Animal(name) {
  // Constructor function (phải gọi với new)
  this.name = name; // Instance property
}

// Methods trên prototype (share giữa instances)
Animal.prototype.speak = function () {
  console.log(this.name + ' makes a sound');
};

// Static methods
Animal.createAnimal = function (name) {
  return new Animal(name);
};

// Inheritance qua prototype chain
function Dog(name, breed) {
  Animal.call(this, name); // Gọi parent constructor
  this.breed = breed;
}

// Set up prototype chain (inheritance)
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog; // Fix constructor reference

// Override method
Dog.prototype.speak = function () {
  console.log(this.name + ' barks!');
};

const dog = new Dog('Rex', 'Labrador');
dog.speak(); // "Rex barks!"

// 🟢 ES6+ - Class Syntax (Syntactic Sugar)
// Cách hoạt động: Bên trong vẫn là prototype, nhưng syntax dễ đọc hơn
class ModernAnimal {
  // Class fields (ES2022)
  species = 'Unknown'; // Public field

  // Constructor
  constructor(public name: string) {
    // Parameter properties (TypeScript)
    // Tự động tạo this.name = name
  }

  // Instance method (trên prototype)
  speak() {
    console.log(`${this.name} makes a sound`);
  }

  // Static method (trên class itself)
  static createAnimal(name: string) {
    return new ModernAnimal(name);
  }

  // Getter
  get info() {
    return `Animal: ${this.name}`;
  }

  // Setter
  set info(value: string) {
    this.name = value.replace('Animal: ', '');
  }
}

// Inheritance với extends
class ModernDog extends ModernAnimal {
  constructor(name: string, public breed: string) {
    super(name); // Gọi parent constructor - BẮT BUỘC
    // Phải call super() trước khi dùng this
  }

  // Override method
  speak() {
    console.log(`${this.name} barks!`);
  }

  // Call parent method
  speakLikeParent() {
    super.speak(); // Gọi Animal.speak()
  }

  // Private fields (ES2022)
  #privateField = 'secret'; // Chỉ accessible trong class

  getPrivate() {
    return this.#privateField; // ✅ OK
  }
}

const modernDog = new ModernDog('Rex', 'Labrador');
modernDog.speak(); // "Rex barks!"
// console.log(modernDog.#privateField); // ❌ SyntaxError: Private field

// ============================================
// 4. TEMPLATE LITERALS vs String Concatenation
// ============================================

// 🔴 ES5 - String Concatenation (verbose, error-prone)
var name = 'John';
var age = 25;
var city = 'Ha Noi';

// Single line
var message = 'Hello ' + name + ', you are ' + age + ' years old';

// Multi-line (phải dùng \n và +)
var multiLine =
  'Name: ' +
  name +
  '\n' +
  'Age: ' +
  age +
  '\n' +
  'City: ' +
  city;

// HTML generation (nightmare)
var html =
  '<div class="user">' +
  '<h2>' +
  name +
  '</h2>' +
  '<p>Age: ' +
  age +
  '</p>' +
  '<p>City: ' +
  city +
  '</p>' +
  '</div>';

// 🟢 ES6+ - Template Literals (clean, readable)
// Cách hoạt động: Backticks `` cho phép embedded expressions ${} và multi-line
const modernMessage = `Hello ${name}, you are ${age} years old`;

// Multi-line (tự nhiên, giữ nguyên indentation)
const modernMultiLine = `
  Name: ${name}
  Age: ${age}
  City: ${city}
`;

// Expression trong template (không chỉ variables)
const calculation = `2 + 2 = ${2 + 2}`; // "2 + 2 = 4"
const conditional = `Status: ${age >= 18 ? 'Adult' : 'Minor'}`; // Ternary
const methodCall = `Upper: ${name.toUpperCase()}`; // Method call

// HTML generation (dễ đọc hơn nhiều)
const modernHtml = `
  <div class="user">
    <h2>${name}</h2>
    <p>Age: ${age}</p>
    <p>City: ${city}</p>
  </div>
`;

// Tagged Templates (advanced feature)
function highlight(strings: TemplateStringsArray, ...values: any[]) {
  return strings.reduce((result, str, i) => {
    return result + str + (values[i] ? `<mark>${values[i]}</mark>` : '');
  }, '');
}

const highlighted = highlight`Hello ${name}, you are ${age} years old`;
// "Hello <mark>John</mark>, you are <mark>25</mark> years old"

// ============================================
// 5. DESTRUCTURING - Elegant Data Extraction
// ============================================

const user = {
  name: 'John Doe',
  age: 30,
  address: {
    city: 'Ha Noi',
    country: 'Vietnam',
  },
  hobbies: ['coding', 'reading'],
};

// 🔴 ES5 - Manual Assignment (verbose, repetitive)
var userName = user.name;
var userAge = user.age;
var userCity = user.address.city;
var userCountry = user.address.country;
var firstHobby = user.hobbies[0];
var secondHobby = user.hobbies[1];

// 🟢 ES6+ - Destructuring (concise, readable)
// Object destructuring
const { name: userName2, age: userAge2 } = user; // Rename variables

// Nested destructuring
const {
  address: { city, country },
} = user;

// Array destructuring
const [firstHobby2, secondHobby2] = user.hobbies;

// Default values
const { email = 'no-email@example.com' } = user; // email không tồn tại → dùng default

// Rest properties (lấy phần còn lại)
const { name: n, ...rest } = user; // rest = { age, address, hobbies }

// Function parameter destructuring
function greetUser({ name, age }: { name: string; age: number }) {
  console.log(`Hello ${name}, ${age} years old`);
}

greetUser(user); // Truyền object, tự động destructure

// Array destructuring với skip
const numbers = [1, 2, 3, 4, 5];
const [first, , third] = numbers; // Skip second element

// Swap variables (elegant)
let a = 1,
  b = 2;
[a, b] = [b, a]; // a=2, b=1 (không cần temp variable)

// ============================================
// 6. SPREAD & REST OPERATORS
// ============================================

// 🔴 ES5 - Array/Object Operations (cumbersome)
var arr1 = [1, 2, 3];
var arr2 = [4, 5, 6];

// Concatenate arrays
var combined = arr1.concat(arr2); // [1,2,3,4,5,6]

// Copy array
var copy = arr1.slice(); // [1,2,3]

// Copy object
var obj1 = { a: 1, b: 2 };
var obj2 = Object.assign({}, obj1); // { a: 1, b: 2 }

// Function với variable arguments
function sum() {
  var args = Array.prototype.slice.call(arguments); // Convert arguments to array
  return args.reduce(function (total, num) {
    return total + num;
  }, 0);
}

// 🟢 ES6+ - Spread & Rest (intuitive, powerful)
// Cách hoạt động: ... operator "spreads" iterable elements

// Spread arrays (phân rã array thành individual elements)
const spreadArr1 = [1, 2, 3];
const spreadArr2 = [4, 5, 6];
const spreadCombined = [...spreadArr1, ...spreadArr2]; // [1,2,3,4,5,6]

// Copy array (shallow)
const spreadCopy = [...spreadArr1]; // [1,2,3]

// Add elements
const withExtra = [...spreadArr1, 4, 5]; // [1,2,3,4,5]
const atBeginning = [0, ...spreadArr1]; // [0,1,2,3]

// Spread objects (phân rã object properties)
const spreadObj1 = { a: 1, b: 2 };
const spreadObj2 = { c: 3, d: 4 };
const spreadObjCombined = { ...spreadObj1, ...spreadObj2 }; // {a:1, b:2, c:3, d:4}

// Override properties
const overridden = { ...spreadObj1, b: 99 }; // {a:1, b:99} - b bị ghi đè

// Spread trong function calls
const maxNum = Math.max(...spreadArr1); // Math.max(1, 2, 3) = 3

// Rest parameters (thu thập remaining arguments vào array)
function modernSum(...numbers: number[]) {
  // numbers là array [1,2,3,...]
  return numbers.reduce((total, num) => total + num, 0);
}

modernSum(1, 2, 3, 4, 5); // 15

// Rest in destructuring
const [head, ...tail] = [1, 2, 3, 4]; // head=1, tail=[2,3,4]
const { x, ...others } = { x: 1, y: 2, z: 3 }; // x=1, others={y:2, z:3}

// ============================================
// 7. DEFAULT PARAMETERS
// ============================================

// 🔴 ES5 - Manual Default Values
function greetES5(name, greeting) {
  // Check và assign default
  name = name || 'Guest'; // ⚠️ Falsy values (0, '', false) cũng bị replace
  greeting = typeof greeting !== 'undefined' ? greeting : 'Hello';

  return greeting + ' ' + name;
}

// 🟢 ES6+ - Native Default Parameters
// Cách hoạt động: Default chỉ apply khi argument là undefined
function greetES6(name = 'Guest', greeting = 'Hello') {
  return `${greeting} ${name}`;
}

greetES6(); // "Hello Guest"
greetES6('John'); // "Hello John"
greetES6('John', 'Hi'); // "Hi John"
greetES6(undefined, 'Hey'); // "Hey Guest" - name dùng default

// Default với expressions
function createUser(name = 'User', id = generateId()) {
  // generateId() chỉ chạy khi id undefined
  return { name, id };
}

// Default destructured parameters
function configAPI({
  url = 'https://api.example.com',
  timeout = 5000,
  retries = 3,
} = {}) {
  // = {} để tránh error khi không truyền argument
  console.log({ url, timeout, retries });
}

// ============================================
// 8. PROMISES vs CALLBACKS
// ============================================

// 🔴 ES5 - Callback Hell (pyramid of doom)
function fetchUserES5(userId, callback) {
  setTimeout(function () {
    // Simulate API call
    var user = { id: userId, name: 'John' };

    // Nested callbacks
    fetchPostsES5(userId, function (posts) {
      fetchCommentsES5(posts[0].id, function (comments) {
        fetchLikesES5(comments[0].id, function (likes) {
          // 😱 Callback hell - hard to read, maintain, error handle
          callback({ user, posts, comments, likes });
        });
      });
    });
  }, 100);
}

// Error handling với callbacks (phức tạp)
function fetchDataES5(callback) {
  setTimeout(function () {
    var error = Math.random() > 0.5 ? new Error('Failed') : null;
    var data = error ? null : { value: 42 };
    callback(error, data); // Node.js style: error-first callback
  }, 100);
}

// 🟢 ES6+ - Promises (chainable, readable)
// Cách hoạt động: Promise là object đại diện cho eventual completion/failure
function fetchUserES6(userId: string): Promise<any> {
  return new Promise((resolve, reject) => {
    // executor function chạy immediately
    setTimeout(() => {
      const user = { id: userId, name: 'John' };
      resolve(user); // Success
      // reject(new Error('Failed')); // Failure
    }, 100);
  });
}

// Promise chaining (flat, readable)
fetchUserES6('123')
  .then((user) => {
    console.log('User:', user);
    return fetchPosts(user.id); // Return promise → chain tiếp
  })
  .then((posts) => {
    console.log('Posts:', posts);
    return fetchComments(posts[0].id);
  })
  .then((comments) => {
    console.log('Comments:', comments);
    return fetchLikes(comments[0].id);
  })
  .then((likes) => {
    console.log('Likes:', likes);
  })
  .catch((error) => {
    // Single catch cho tất cả errors
    console.error('Error:', error);
  })
  .finally(() => {
    // Chạy dù thành công hay fail
    console.log('Cleanup');
  });

// Promise combinators
const promise1 = fetchUserES6('1');
const promise2 = fetchUserES6('2');
const promise3 = fetchUserES6('3');

// Promise.all - chờ tất cả resolve (hoặc 1 reject)
Promise.all([promise1, promise2, promise3]).then((results) => {
  console.log('All users:', results); // [user1, user2, user3]
});

// Promise.race - lấy kết quả của promise nhanh nhất
Promise.race([promise1, promise2, promise3]).then((result) => {
  console.log('First user:', result); // user nào resolve trước
});

// Promise.allSettled - chờ tất cả settle (resolve hoặc reject)
Promise.allSettled([promise1, promise2, promise3]).then((results) => {
  results.forEach((result) => {
    if (result.status === 'fulfilled') {
      console.log('Success:', result.value);
    } else {
      console.log('Failed:', result.reason);
    }
  });
});

// Promise.any - lấy promise fulfilled đầu tiên
Promise.any([promise1, promise2, promise3]).then((result) => {
  console.log('First successful:', result);
});

// ============================================
// 9. ASYNC/AWAIT - Promise Syntax Sugar
// ============================================

// 🟢 ES2017 - Async/Await (looks synchronous, actually async)
// Cách hoạt động: async function tự động return Promise, await pause execution
async function fetchAllData() {
  try {
    // await "pauses" execution until promise resolves
    const user = await fetchUserES6('123'); // Looks synchronous!
    console.log('User:', user);

    const posts = await fetchPosts(user.id); // Wait for user first
    console.log('Posts:', posts);

    const comments = await fetchComments(posts[0].id);
    console.log('Comments:', comments);

    const likes = await fetchLikes(comments[0].id);
    console.log('Likes:', likes);

    return { user, posts, comments, likes };
  } catch (error) {
    // Try-catch cho error handling (như synchronous code)
    console.error('Error:', error);
    throw error; // Re-throw nếu cần
  } finally {
    console.log('Cleanup');
  }
}

// Parallel execution với Promise.all
async function fetchMultipleUsers() {
  // ❌ Sequential (slow) - mỗi request đợi previous
  const user1 = await fetchUserES6('1'); // Wait 100ms
  const user2 = await fetchUserES6('2'); // Wait thêm 100ms
  const user3 = await fetchUserES6('3'); // Wait thêm 100ms
  // Total: 300ms

  // ✅ Parallel (fast) - tất cả requests cùng lúc
  const [user1, user2, user3] = await Promise.all([
    fetchUserES6('1'),
    fetchUserES6('2'),
    fetchUserES6('3'),
  ]);
  // Total: 100ms (chỉ chờ slowest request)
}

// Top-level await (ES2022) - await ngoài async function
// const config = await fetch('/api/config').then(r => r.json());
// console.log(config); // ✅ OK trong module scope

// ============================================
// 10. MODULES - Import/Export
// ============================================

// 🔴 ES5 - No Native Modules
// Phải dùng patterns như IIFE, CommonJS (Node.js), AMD (RequireJS)

// IIFE Pattern (Immediately Invoked Function Expression)
var MyModule = (function () {
  var privateVar = 'secret';

  function privateMethod() {
    console.log(privateVar);
  }

  return {
    publicMethod: function () {
      privateMethod();
    },
  };
})();

// CommonJS (Node.js)
// module.exports = { name: 'John', greet: function() {} };
// const user = require('./user');

// 🟢 ES6+ - Native Modules (static analysis, tree-shaking)
// Cách hoạt động: Import/export statements, module scope riêng biệt

// Named exports (có thể nhiều per file)
export const PI = 3.14159;
export function calculateArea(radius: number) {
  return PI * radius * radius;
}
export class Circle {
  constructor(public radius: number) {}
}

// Default export (chỉ 1 per file)
export default class User {
  constructor(public name: string) {}
}

// Import named exports
import { PI, calculateArea, Circle } from './math';

// Import default export
import User from './user';

// Import both
import User, { PI, calculateArea } from './combined';

// Rename imports
import { PI as PIValue } from './math';

// Import all
import * as MathUtils from './math';
MathUtils.PI; // 3.14159
MathUtils.calculateArea(5);

// Re-export (module aggregation)
export { PI, calculateArea } from './math';
export { default as User } from './user';

// Dynamic imports (code splitting)
const module = await import('./heavy-module'); // Lazy load
module.doSomething();

// Conditional imports
if (condition) {
  const { feature } = await import('./feature');
  feature();
}
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

```typescript
// ❌ LỖI 1: Dùng var trong modern code
var name = 'John'; // ❌ Function scoped, có thể gây bugs

// ✅ ĐÚNG: Dùng const/let
const name = 'John'; // ✅ Block scoped, immutable
let age = 25; // ✅ Block scoped, mutable

// ❌ LỖI 2: Arrow function làm method (lose this binding)
const obj = {
  value: 42,
  getValue: () => this.value, // ❌ this = window, không phải obj
};

// ✅ ĐÚNG: Regular function cho methods
const obj = {
  value: 42,
  getValue() {
    return this.value; // ✅ this = obj
  },
};

// ❌ LỖI 3: Quên await trong async function
async function fetchData() {
  const data = fetchUserES6('123'); // ❌ data là Promise, không phải value
  console.log(data.name); // undefined
}

// ✅ ĐÚNG: Await promise
async function fetchData() {
  const data = await fetchUserES6('123'); // ✅ Chờ promise resolve
  console.log(data.name); // "John"
}

// ❌ LỖI 4: Sequential await khi có thể parallel
async function slow() {
  const user1 = await fetchUser('1'); // 100ms
  const user2 = await fetchUser('2'); // 100ms
  const user3 = await fetchUser('3'); // 100ms
  // Total: 300ms
}

// ✅ ĐÚNG: Parallel với Promise.all
async function fast() {
  const [user1, user2, user3] = await Promise.all([
    fetchUser('1'),
    fetchUser('2'),
    fetchUser('3'),
  ]);
  // Total: 100ms
}

// ❌ LỖI 5: Spread shallow copy cho nested objects
const original = { a: 1, nested: { b: 2 } };
const copied = { ...original };
copied.nested.b = 99; // ❌ original.nested.b cũng = 99!

// ✅ ĐÚNG: Deep copy cho nested structures
const copied = JSON.parse(JSON.stringify(original)); // Simple way
// Hoặc dùng lodash cloneDeep, structuredClone

// ❌ LỖI 6: Destructuring với missing properties (no default)
const { email } = user; // ❌ email = undefined nếu không tồn tại

// ✅ ĐÚNG: Provide default values
const { email = 'no-email@example.com' } = user; // ✅

// ❌ LỖI 7: Confuse default export vs named export
import User from './user'; // ❌ Nếu file export named, không phải default

// ✅ ĐÚNG: Match export type
import { User } from './user'; // ✅ Named export
import User from './user'; // ✅ Default export
```

**📊 Performance Comparison:**

```
┌─────────────────────────────────────────────────────────────┐
│              ES5 vs ES6+ PERFORMANCE IMPACT                  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Feature                    ES5 Speed    ES6+ Speed  Winner │
│  ────────────────────────── ──────────── ────────── ────── │
│  Variable access (var)      ⚡⚡⚡⚡⚡      -          ES5   │
│  Variable access (let)      -            ⚡⚡⚡⚡      ES6   │
│  Function call (regular)    ⚡⚡⚡⚡⚡      -          ES5   │
│  Function call (arrow)      -            ⚡⚡⚡⚡⚡     ES6   │
│  String concat (+)          ⚡⚡⚡⚡       -          ES5   │
│  Template literals (``)     -            ⚡⚡⚡⚡⚡     ES6   │
│  Object creation            ⚡⚡⚡⚡       -          ES5   │
│  Class instantiation        -            ⚡⚡⚡⚡      ES6   │
│  Array iteration (.map)     ⚡⚡⚡⚡       -          ES5   │
│  For-of loop                -            ⚡⚡⚡⚡⚡     ES6   │
│  Promise                    N/A          ⚡⚡⚡        ES6   │
│  Async/Await                N/A          ⚡⚡⚡        ES6   │
│                                                              │
│  💡 Note: Performance khác biệt minimal trong most cases    │
│     Code readability & maintainability quan trọng hơn!      │
└─────────────────────────────────────────────────────────────┘
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

