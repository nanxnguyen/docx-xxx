# 🎯 Q10: IIFE (Immediately Invoked Function Expression) & Functional Programming - Pure Functions, Immutability, Currying, Higher-Order Functions, Composition, Ramda/Lodash

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"IIFE là function execute ngay sau khi define để tạo private scope. Functional Programming bao gồm pure functions (same input → same output, no side effects), immutability (không thay đổi dữ liệu gốc), currying (partial application), higher-order functions (nhận/trả về functions), composition (kết hợp functions), memoization (cache kết quả), recursion (function gọi lại chính nó) và các libraries như Ramda/Lodash-fp hỗ trợ FP với auto-curry và data-last parameters."**

**🔑 10 Khái Niệm Chính:**

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
- **Reusable functions** với preset arguments: `const add5 = add(5); add5(10) // 15`
- Use case: event handlers, middleware, configuration functions

**4. Higher-Order Functions:**

- Functions nhận/return functions: `.map()`, `.filter()`, `.reduce()`
- **Composition**: kết hợp nhiều functions `compose(f, g, h)(x) = f(g(h(x)))`
- Use case: middleware stack, decorators, memoization

**5. Immutability:**

- **Không thay đổi dữ liệu gốc**, tạo bản sao mới với spread operator
- Use case: React state, Redux, functional updates
- Ví dụ: `const newArr = [...arr, item]` (immutable) vs `arr.push(item)` (mutable)

**6. Composition vs Inheritance:**

- **Composition**: Kết hợp behaviors (HAS-A) → Flexible, testable
- **Inheritance**: Kế thừa từ class (IS-A) → Tight coupling
- Best practice: "Favor composition over inheritance"

**7. Memoization:**

- **Cache kết quả** function calls để tránh tính toán lại
- Use case: Expensive computations, performance optimization
- Ví dụ: `const memoizedFib = memoize(fibonacci)`

**8. Function Composition:**

- **Kết hợp nhiều functions** nhỏ thành function lớn
- `compose(f, g, h)(x) = f(g(h(x)))` hoặc `pipe(f, g, h)(x) = h(g(f(x)))`
- Use case: Data transformations, pipeline processing

**9. Recursion:**

- Function **gọi lại chính nó** để giải quyết vấn đề
- Use case: Tree traversal, recursive data structures
- Best practice: Tail recursion, memoization

**10. Ramda & Lodash/fp:**

- **Functional Programming libraries** với auto-curry, data-last
- Ramda: Lens, functional programming thuần túy
- Lodash/fp: Smaller bundle, familiar API

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
- 🔄 **HOF**: Function nhận/trả về function
- 🛡️ **Immutability**: Không thay đổi dữ liệu gốc, tạo bản sao mới
- 🔗 **Composition**: Kết hợp behaviors thay vì kế thừa
- 💾 **Memoization**: Cache kết quả function calls
- 🔁 **Recursion**: Function gọi lại chính nó
- 📚 **Ramda/Lodash-fp**: FP libraries với auto-curry, data-last

**❓ Câu Hỏi:**

Giải thích IIFE, Pure Functions, Immutability, Currying, Higher-Order Functions, Composition, Memoization, Recursion và các Functional Programming libraries (Ramda, Lodash/fp) trong JavaScript. Bao gồm cách hoạt động, ưu nhược điểm và ứng dụng thực tế.

---

**📚 Phần 1: IIFE (Immediately Invoked Function Expression)**

**💡 IIFE Là Gì?**

IIFE (đọc là "iffy") là một function được **gọi ngay lập tức** sau khi được định nghĩa. Nó tạo ra một **scope riêng biệt**, giúp tránh ô nhiễm global namespace.

**🔥 Cú Pháp:**

```typescript
// Cách 1: Bọc function trong ()
(function () {
  // Code ở đây chạy ngay lập tức
})();

// Cách 2: Bọc toàn bộ trong ()
(function () {
  // Code ở đây chạy ngay lập tức
})();
```

**💡 Tại Sao Cần IIFE?**

```typescript
// ❌ KHÔNG dùng IIFE - Biến x, y "rò rỉ" ra global scope
let x = 10;
let y = 20;
console.log(window.x); // 10 - Ô nhiễm global scope! ❌

// ✅ Dùng IIFE - Biến x, y KHÔNG rò rỉ
(function () {
  let x = 10; // Private variable - chỉ tồn tại trong scope này
  let y = 20;
  console.log(x + y); // 30
})();

console.log(typeof x); // "undefined" - x KHÔNG tồn tại bên ngoài ✅
```

**🎯 Use Cases của IIFE:**

```typescript
// 1️⃣ Module Pattern - Tạo private state (Pattern Module - Tạo State Riêng Tư)
const calculator = (function () {
  // 💡 IIFE: Function tự gọi ngay → Tạo scope riêng
  // 💡 calculator: Nhận return value từ IIFE

  let result = 0; // ⚠️ Private variable - không thể access từ bên ngoài
  // 💡 result: Biến private trong IIFE scope
  // 💡 Chỉ có thể access từ bên trong IIFE
  // 💡 Bên ngoài không thể access trực tiếp → Data privacy

  return {
    // 💡 Return object với public methods
    // 💡 Public API: Chỉ expose methods cần thiết
    // 💡 result: Private → Không expose

    add(x: number): number {
      // 💡 add: Public method để thay đổi result
      result += x; // ✅ Chỉ thay đổi được qua method này
      // 💡 Access private variable result → Closure
      // 💡 Chỉ có thể thay đổi qua public method → Controlled access
      return result;
    },
    subtract(x: number): number {
      // 💡 subtract: Public method để thay đổi result
      result -= x; // ✅ Chỉ thay đổi được qua method này
      return result;
    },
    getResult(): number {
      // 💡 getResult: Public method để đọc result
      return result; // ✅ Chỉ đọc được qua method này
      // 💡 Không thể đọc trực tiếp → Controlled access
    },
  };
})(); // 💡 () : Gọi function ngay → Execute IIFE
// 💡 calculator: Nhận object với public methods
// 💡 result: Vẫn tồn tại trong closure → Private state

calculator.add(10); // 10
// 💡 add(10): Gọi public method → result = 0 + 10 = 10
calculator.subtract(3); // 7
// 💡 subtract(3): Gọi public method → result = 10 - 3 = 7
console.log(calculator.result); // undefined - ❌ Không access được private variable
// 💡 calculator.result: undefined → result là private
// 💡 Không thể access trực tiếp → Data privacy
console.log(calculator.getResult()); // 7 - ✅ Phải dùng method
// 💡 getResult(): Public method → Return result = 7
// 💡 Phải dùng public method → Controlled access

// 2️⃣ IIFE với Parameters - Truyền arguments vào
(function (name: string, age: number) {
  console.log(`Xin chào ${name}, ${age} tuổi`);
})('John', 25); // "Xin chào John, 25 tuổi"

// 3️⃣ IIFE với Return Value - Trả về kết quả
const sum = (function (a: number, b: number): number {
  return a + b; // Tính toán và trả về ngay lập tức
})(5, 10);
console.log(sum); // 15

// 4️⃣ IIFE với Async/Await - Xử lý bất đồng bộ
(async function () {
  try {
    const response = await fetch('/api/users');
    const users = await response.json();
    console.log(users);
  } catch (error) {
    console.error('Lỗi:', error);
  }
})();
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

```typescript
// ✅ Pure Function - Hoàn hảo! (Hàm Thuần Túy)
function add(a: number, b: number): number {
  // 💡 add: Pure function - Same input → same output, no side effects
  // 💡 a, b: Input parameters
  // 💡 Return: Sum of a and b

  return a + b; // ✅ Chỉ tính toán, không side effects
  // 💡 Không thay đổi biến bên ngoài
  // 💡 Không gọi API, không log, không mutate data
  // 💡 Chỉ tính toán và return kết quả
}

console.log(add(2, 3)); // 5 - Gọi 1000 lần vẫn trả về 5
// 💡 add(2, 3): Luôn trả về 5 → Predictable
console.log(add(2, 3)); // 5 - Predictable (dự đoán được)
// 💡 Gọi nhiều lần với cùng input → Cùng output

// ❌ Impure Function - Có side effects (Hàm Không Thuần Túy)
let counter = 0; // ⚠️ External state (State bên ngoài)
// 💡 counter: Biến global → Có thể bị thay đổi bởi bất kỳ function nào
// 💡 → Không predictable → Khó test, khó debug

function increment(): number {
  // 💡 increment: Impure function - Có side effect
  // 💡 Không có input → Không thể predict output

  counter++; // ❌ Side effect - thay đổi biến bên ngoài
  // 💡 Thay đổi counter → Side effect
  // 💡 Output phụ thuộc vào state bên ngoài → Không predictable

  return counter;
}

console.log(increment()); // 1
// 💡 Lần 1: counter = 0 → increment → counter = 1 → return 1
console.log(increment()); // 2 - ❌ Cùng input (không có), khác output!
// 💡 Lần 2: counter = 1 → increment → counter = 2 → return 2
// 💡 ❌ Cùng input (không có input) nhưng output khác → Impure!

// ✅ Chuyển thành Pure Function (Chuyển thành Hàm Thuần Túy)
function increment(counter: number): number {
  // 💡 increment: Pure function - Nhận counter làm input
  // 💡 Same input → same output → Predictable

  return counter + 1; // ✅ Không thay đổi state, return giá trị mới
  // 💡 Không mutate counter → Tạo giá trị mới
  // 💡 Predictable: increment(0) luôn = 1, increment(1) luôn = 2
}

let myCounter = 0;
myCounter = increment(myCounter); // 1 - Rõ ràng, dễ test
// 💡 increment(0) → return 1 → myCounter = 1
// 💡 Rõ ràng: Input là 0, output là 1 → Dễ test
myCounter = increment(myCounter); // 2
// 💡 increment(1) → return 2 → myCounter = 2
// 💡 Predictable: increment(1) luôn = 2
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

```typescript
// ❌ Function thông thường - Nhận tất cả tham số cùng lúc
function add(a: number, b: number): number {
  // 💡 add: Function thông thường nhận 2 parameters
  // 💡 Phải truyền cả 2 số cùng lúc → Không thể partial application
  return a + b;
}
console.log(add(2, 3)); // 5 - Phải truyền cả 2 số
// 💡 add(2, 3): Phải truyền cả a và b → Không linh hoạt

// ✅ Currying - Nhận từng tham số một (Currying - Nhận Từng Tham Số)
const add = (a: number) => (b: number) => a + b;
//            ↑ nhận a    ↑ trả về function nhận b
// 💡 add: Curried function
// 💡 (a: number) => : Nhận parameter a → Return function
// 💡 (b: number) => a + b: Function nhận b → Return a + b
// 💡 Currying: Transform function nhiều params → Chuỗi functions 1 param

const add2 = add(2); // add2 là function: (b) => 2 + b
// 💡 add(2): Partial application → Tạo function mới với a = 2
// 💡 add2: Function nhận b → Return 2 + b
// 💡 Reusable: Có thể dùng add2 nhiều lần

console.log(add2(3)); // 5 - Giống kết quả trên
// 💡 add2(3): (b) => 2 + b với b = 3 → 2 + 3 = 5
console.log(add2(10)); // 12 - Có thể tái sử dụng add2
// 💡 add2(10): (b) => 2 + b với b = 10 → 2 + 10 = 12
// 💡 Reusable: Dùng lại add2 với values khác nhau
console.log(add(2)(3)); // 5 - Hoặc gọi luôn
// 💡 add(2)(3): Gọi curried function trực tiếp
// 💡 add(2) → return function (b) => 2 + b
// 💡 (3) → call function với b = 3 → 2 + 3 = 5
```

**🎯 Use Cases của Currying:**

```typescript
// 1️⃣ Tạo specialized functions (hàm chuyên dụng)
const multiply = (a: number) => (b: number) => a * b;

const double = multiply(2); // Hàm nhân đôi
const triple = multiply(3); // Hàm nhân ba

console.log(double(5)); // 10 - double tái sử dụng được
console.log(triple(5)); // 15

// 2️⃣ Partial Application - Áp dụng một phần tham số
const calculateTax = (rate: number) => (amount: number) => amount * rate;

const calculateVAT = calculateTax(0.1); // VAT 10%
const calculateLuxuryTax = calculateTax(0.2); // Luxury tax 20%

console.log(calculateVAT(1000)); // 100 - 10% của 1000
console.log(calculateLuxuryTax(1000)); // 200 - 20% của 1000

// 3️⃣ Currying với nhiều tham số
const volume = (length: number) => (width: number) => (height: number) =>
  length * width * height;

const boxVolume = volume(10)(5); // length=10, width=5, height=?
console.log(boxVolume(2)); // 10 * 5 * 2 = 100
console.log(boxVolume(3)); // 10 * 5 * 3 = 150
```

---

**🔥 3. Higher-Order Functions (HOF - Hàm Bậc Cao)**

**💡 HOF Là Gì?**

HOF là function thỏa mãn 1 trong 2 điều kiện:

1. **Nhận function làm argument** (tham số)
2. **Trả về function** (return function)

```typescript
// 1️⃣ HOF nhận function làm argument (HOF Nhận Function Làm Tham Số)
function withLogging<T extends (...args: any[]) => any>(
  // 💡 withLogging: Higher-Order Function
  // 💡 <T extends (...args: any[]) => any>: Generic type cho function
  // 💡 T: Type của function được wrap

  fn: T // ⚠️ Nhận function làm tham số
  // 💡 fn: Function được wrap với logging
  // 💡 HOF: Nhận function làm argument → Higher-Order Function
): (...args: Parameters<T>) => ReturnType<T> {
  // 💡 Return type: Function có cùng signature với fn
  // 💡 Parameters<T>: Extract parameters từ T
  // 💡 ReturnType<T>: Extract return type từ T

  return (...args: Parameters<T>) => {
    // 💡 Return function mới → HOF trả về function
    // 💡 ...args: Spread parameters từ function gốc

    console.log('🔍 Gọi function với:', args); // 📝 Log input
    // 💡 Log arguments → Debug dễ dàng

    const result = fn(...args); // 🔧 Gọi function gốc
    // 💡 fn(...args): Gọi function gốc với arguments
    // 💡 result: Kết quả từ function gốc

    console.log('✅ Kết quả:', result); // 📝 Log output
    // 💡 Log result → Debug dễ dàng

    return result; // 📤 Trả về kết quả
    // 💡 Return result từ function gốc → Transparent wrapper
  };
}

const add = (a: number, b: number) => a + b; // ➕ Function cộng
const loggedAdd = withLogging(add); // 🔧 Bọc add với logging
// 💡 withLogging: HOF nhận add → Trả về function mới có logging
// 💡 loggedAdd: Function mới có logging + behavior của add

loggedAdd(2, 3);
// 💡 Gọi loggedAdd → Log input → Gọi add → Log output → Return result
// Output:
// 🔍 Gọi function với: [2, 3]
// ✅ Kết quả: 5

// 2️⃣ HOF trả về function (HOF Trả Về Function)
function createGreeter(greeting: string) {
  // 💡 createGreeter: Higher-Order Function
  // 💡 greeting: Parameter để tạo function mới

  return (name: string) => `${greeting}, ${name}!`; // ⚠️ Return function
  // 💡 Return function mới → HOF trả về function
  // 💡 Function mới: Nhận name, return greeting message
  // 💡 Closure: Function mới có access đến greeting
}

const sayHello = createGreeter('Xin chào'); // 🔧 Tạo function chào hỏi
// 💡 createGreeter('Xin chào'): HOF trả về function
// 💡 sayHello: Function (name) => `Xin chào, ${name}!`
// 💡 Closure: sayHello có access đến 'Xin chào'

const sayHi = createGreeter('Hi'); // 🔧 Tạo function chào hỏi khác
// 💡 createGreeter('Hi'): HOF trả về function khác
// 💡 sayHi: Function (name) => `Hi, ${name}!`
// 💡 Closure: sayHi có access đến 'Hi'

console.log(sayHello('John')); // "Xin chào, John!"
// 💡 sayHello('John'): Gọi function → `Xin chào, John!`
console.log(sayHi('Jane')); // "Hi, Jane!"
// 💡 sayHi('Jane'): Gọi function → `Hi, Jane!`

// 3️⃣ Array methods đều là HOF (Array Methods Là HOF)
const numbers = [1, 2, 3, 4, 5]; // 📦 Array numbers

const doubled = numbers.map((x) => x * 2); // [2, 4, 6, 8, 10]
//                          ↑ nhận function làm argument
// 💡 map: HOF nhận function làm argument
// 💡 (x) => x * 2: Function transform mỗi phần tử
// 💡 map: Apply function cho mỗi phần tử → Tạo array mới

const evens = numbers.filter((x) => x % 2 === 0); // [2, 4]
//                           ↑ nhận function làm argument
// 💡 filter: HOF nhận function làm argument
// 💡 (x) => x % 2 === 0: Function predicate (điều kiện)
// 💡 filter: Lọc phần tử thỏa điều kiện → Tạo array mới

const sum = numbers.reduce((acc, x) => acc + x, 0); // 15
//                         ↑ nhận function làm argument
// 💡 reduce: HOF nhận function làm argument
// 💡 (acc, x) => acc + x: Function accumulator
// 💡 reduce: Accumulate values → Return single value
// 💡 0: Initial value cho accumulator
```

**🎯 Practical Example - Data Processing:**

```typescript
// Xử lý danh sách users
const users = [
  { name: 'John', age: 25, active: true },
  { name: 'Jane', age: 30, active: false },
  { name: 'Bob', age: 35, active: true },
];

// ❌ Cách cũ - Imperative (mệnh lệnh)
const activeUserNames = [];
for (let i = 0; i < users.length; i++) {
  if (users[i].active) {
    activeUserNames.push(users[i].name.toUpperCase());
  }
}
activeUserNames.sort();

// ✅ Cách mới - Functional Programming
const activeUserNames2 = users
  .filter((user) => user.active) // 1. Lọc user active
  .map((user) => user.name.toUpperCase()) // 2. Chuyển tên thành UPPERCASE
  .sort(); // 3. Sắp xếp

console.log(activeUserNames2); // ['BOB', 'JOHN'] - Ngắn gọn, dễ đọc!
```

---

**✅ Best Practices:**

- ✅ **Ưu tiên Pure Functions**: Code predictable, dễ test
- ✅ **Dùng Currying cho reusable functions**: Tạo specialized functions
- ✅ **Dùng HOF thay vì loops**: `map`, `filter`, `reduce` ngắn gọn hơn
- ✅ **Function Composition**: Kết hợp functions nhỏ thành function lớn
- ✅ **IIFE cho module pattern**: Tạo private scope khi cần

**❌ Common Mistakes:**

```typescript
// ❌ Sai: Impure function với side effects
let total = 0;
function addToTotal(value: number): void {
  total += value; // ❌ Side effect - thay đổi biến global
}

// ✅ Đúng: Pure function
function add(total: number, value: number): number {
  return total + value; // ✅ Return giá trị mới, không thay đổi state
}

// ❌ Sai: Không dùng HOF khi có thể
const numbers = [1, 2, 3, 4, 5];
const doubled = [];
for (let i = 0; i < numbers.length; i++) {
  doubled.push(numbers[i] * 2); // ❌ Dài dòng, dễ lỗi
}

// ✅ Đúng: Dùng HOF
const doubled2 = numbers.map((x) => x * 2); // ✅ Ngắn gọn, rõ ràng

// ❌ Sai: Không dùng currying khi cần reuse
function calculateTax(rate: number, amount: number): number {
  return amount * rate;
}
const tax1 = calculateTax(0.1, 1000); // ❌ Lặp lại rate nhiều lần
const tax2 = calculateTax(0.1, 2000);

// ✅ Đúng: Dùng currying
const calculateTax2 = (rate: number) => (amount: number) => amount * rate;
const calculateVAT = calculateTax2(0.1); // ✅ Tạo function với rate cố định
const tax3 = calculateVAT(1000); // Gọn hơn, tái sử dụng được
const tax4 = calculateVAT(2000);
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

## **📚 PHẦN 3: IMMUTABILITY PATTERNS (Patterns Bất Biến)**

**💡 Immutability Là Gì?**

Immutability (Bất biến) là nguyên tắc **không thay đổi dữ liệu gốc**, thay vào đó tạo ra **bản sao mới** với dữ liệu đã được cập nhật.

```typescript
// ❌ MUTABLE (Có thể thay đổi) - Thay đổi dữ liệu gốc
const arr = [1, 2, 3];
arr.push(4); // ❌ Thay đổi arr gốc
console.log(arr); // [1, 2, 3, 4] - arr đã bị thay đổi

const obj = { name: 'John', age: 25 };
obj.age = 26; // ❌ Thay đổi obj gốc
console.log(obj); // { name: 'John', age: 26 } - obj đã bị thay đổi

// ✅ IMMUTABLE (Bất biến) - Tạo bản sao mới
const arr2 = [1, 2, 3];
const newArr = [...arr2, 4]; // ✅ Tạo array mới, không thay đổi arr2
console.log(arr2); // [1, 2, 3] - arr2 không đổi ✅
console.log(newArr); // [1, 2, 3, 4] - newArr là bản sao mới

const obj2 = { name: 'John', age: 25 };
const newObj = { ...obj2, age: 26 }; // ✅ Tạo object mới, không thay đổi obj2
console.log(obj2); // { name: 'John', age: 25 } - obj2 không đổi ✅
console.log(newObj); // { name: 'John', age: 26 } - newObj là bản sao mới
```

**🎯 Immutability Patterns trong JavaScript:**

```typescript
// 1️⃣ Array Immutability (Bất biến Array)
const numbers = [1, 2, 3, 4, 5];

// ❌ MUTABLE - Thay đổi array gốc
numbers.push(6); // ❌ Thay đổi numbers
numbers.pop(); // ❌ Thay đổi numbers
numbers.splice(0, 1); // ❌ Thay đổi numbers

// ✅ IMMUTABLE - Tạo array mới
const newNumbers1 = [...numbers, 6]; // ✅ Thêm phần tử (spread operator)
// 💡 [...numbers, 6]: Tạo array mới với tất cả phần tử của numbers + 6
// 💡 numbers không bị thay đổi

const newNumbers2 = numbers.slice(0, -1); // ✅ Xóa phần tử cuối
// 💡 slice(): Tạo array mới, không thay đổi array gốc

const newNumbers3 = numbers.filter((n) => n !== 3); // ✅ Xóa phần tử cụ thể
// 💡 filter(): Tạo array mới với các phần tử thỏa điều kiện

const newNumbers4 = numbers.map((n) => n * 2); // ✅ Transform phần tử
// 💡 map(): Tạo array mới với các phần tử đã transform

// 2️⃣ Object Immutability (Bất biến Object)
const user = { name: 'John', age: 25, city: 'Hanoi' };

// ❌ MUTABLE - Thay đổi object gốc
user.age = 26; // ❌ Thay đổi user
user.email = 'john@example.com'; // ❌ Thay đổi user
delete user.city; // ❌ Thay đổi user

// ✅ IMMUTABLE - Tạo object mới
const updatedUser1 = { ...user, age: 26 }; // ✅ Update property
// 💡 { ...user, age: 26 }: Tạo object mới với tất cả properties của user + age mới
// 💡 user không bị thay đổi

const updatedUser2 = { ...user, email: 'john@example.com' }; // ✅ Thêm property
// 💡 Spread operator copy tất cả properties + thêm property mới

const { city, ...updatedUser3 } = user; // ✅ Xóa property (destructuring)
// 💡 Destructuring: Tách city ra, giữ lại các properties khác
// 💡 updatedUser3 = { name: 'John', age: 25 } (không có city)

// 3️⃣ Nested Object Immutability (Bất biến Object Lồng Nhau)
const state = {
  user: {
    name: 'John',
    profile: {
      age: 25,
      address: {
        city: 'Hanoi',
        country: 'Vietnam',
      },
    },
  },
};

// ❌ MUTABLE - Thay đổi nested object
state.user.profile.age = 26; // ❌ Thay đổi state gốc

// ✅ IMMUTABLE - Tạo nested object mới
const newState = {
  ...state, // ✅ Copy level 1
  user: {
    ...state.user, // ✅ Copy level 2
    profile: {
      ...state.user.profile, // ✅ Copy level 3
      age: 26, // ✅ Update property
    },
  },
};
// 💡 Phải copy từng level → Tạo object mới ở mọi level
// 💡 state không bị thay đổi

// 4️⃣ Immutability với Immer (Thư viện hỗ trợ)
import produce from 'immer'; // 📦 Immer: Thư viện tạo immutable updates dễ dàng

const newState2 = produce(state, (draft) => {
  // 💡 produce: Function từ Immer
  // 💡 draft: Proxy object có thể mutate (nhưng không thay đổi state gốc)
  draft.user.profile.age = 26; // ✅ Có thể mutate draft
  draft.user.profile.address.city = 'Ho Chi Minh'; // ✅ Có thể mutate draft
});
// 💡 Immer tự động tạo immutable update → Không cần spread operator thủ công
// 💡 state không bị thay đổi, newState2 là object mới

// 5️⃣ Immutability với Object.freeze() (Đóng băng Object)
const frozenObj = Object.freeze({ name: 'John', age: 25 });
// 💡 Object.freeze(): Đóng băng object → Không thể thay đổi
// 💡 Shallow freeze: Chỉ freeze level 1, nested objects vẫn có thể thay đổi

frozenObj.age = 26; // ❌ Không có effect (trong strict mode sẽ throw error)
console.log(frozenObj.age); // 25 - Không đổi

// Deep freeze (Đóng băng sâu)
function deepFreeze<T>(obj: T): T {
  Object.freeze(obj); // ✅ Freeze object hiện tại
  Object.keys(obj).forEach((key) => {
    // 💡 Duyệt tất cả properties
    if (
      typeof obj[key as keyof T] === 'object' &&
      obj[key as keyof T] !== null
    ) {
      // 💡 Nếu property là object → Recursive freeze
      deepFreeze(obj[key as keyof T]);
    }
  });
  return obj;
}

const deepFrozen = deepFreeze({ user: { name: 'John', age: 25 } });
deepFrozen.user.age = 26; // ❌ Không có effect (deep frozen)
```

**✅ Ưu Điểm của Immutability:**

- ✅ **Predictable**: Dữ liệu không thay đổi → Dễ debug, dễ test
- ✅ **Time Travel**: Có thể lưu lại các version của state → Undo/Redo dễ dàng
- ✅ **Change Detection**: Dễ phát hiện thay đổi (so sánh reference)
- ✅ **Thread Safe**: An toàn khi chạy song song (không có race conditions)
- ✅ **React Optimization**: React có thể optimize re-render dựa trên reference equality

**❌ Nhược Điểm của Immutability:**

- ❌ **Memory Overhead**: Tạo nhiều bản sao → Tốn memory
- ❌ **Performance**: Copy object/array lớn có thể chậm
- ❌ **Complexity**: Code phức tạp hơn với nested objects

**💡 Best Practices:**

```typescript
// ✅ Dùng spread operator cho shallow copy
const newArr = [...arr];
const newObj = { ...obj };

// ✅ Dùng Immer cho deep nested updates
import produce from 'immer';
const newState = produce(state, (draft) => {
  draft.user.profile.age = 26;
});

// ✅ Dùng libraries: Immutable.js, Immer, Ramda
// 💡 Các thư viện này optimize performance cho immutable operations
```

---

## **📚 PHẦN 4: COMPOSITION VS INHERITANCE (Kết Hợp vs Kế Thừa)**

**💡 Composition vs Inheritance Là Gì?**

**Inheritance (Kế thừa)**: Tạo class mới dựa trên class cũ → "IS-A" relationship
**Composition (Kết hợp)**: Kết hợp nhiều objects/functions → "HAS-A" relationship

```typescript
// ❌ INHERITANCE (Kế thừa) - "IS-A" relationship
class Animal {
  name: string;
  constructor(name: string) {
    this.name = name;
  }
  eat() {
    console.log(`${this.name} is eating`);
  }
}

class Dog extends Animal {
  // 💡 Dog IS-A Animal (Dog là một loại Animal)
  bark() {
    console.log(`${this.name} is barking`);
  }
}

const dog = new Dog('Buddy');
dog.eat(); // "Buddy is eating"
dog.bark(); // "Buddy is barking"

// ⚠️ Vấn đề với Inheritance:
// - Tight coupling: Dog phụ thuộc chặt chẽ vào Animal
// - Fragile base class: Thay đổi Animal ảnh hưởng tất cả subclasses
// - Diamond problem: Multiple inheritance phức tạp
// - Khó test: Phải mock cả parent class

// ✅ COMPOSITION (Kết hợp) - "HAS-A" relationship
// 💡 Composition: Kết hợp nhiều behaviors thay vì kế thừa

// 1️⃣ Function Composition (Kết hợp Functions)
const add = (x: number) => x + 1; // ➕ Function cộng 1
const multiply = (x: number) => x * 2; // ✖️ Function nhân 2
const subtract = (x: number) => x - 1; // ➖ Function trừ 1

// ✅ Compose functions (Kết hợp functions)
const compose = <T>(...fns: Array<(x: T) => T>) => (value: T) =>
  fns.reduceRight((acc, fn) => fn(acc), value);
// 💡 compose: Function kết hợp nhiều functions
// 💡 reduceRight: Áp dụng functions từ phải sang trái
// 💡 compose(f, g, h)(x) = f(g(h(x)))

const composed = compose(add, multiply, subtract);
// 💡 composed: subtract → multiply → add
// 💡 x → subtract(x) → multiply(subtract(x)) → add(multiply(subtract(x)))

console.log(composed(5)); // 11
// 💡 5 → subtract(5) = 4 → multiply(4) = 8 → add(8) = 9
// 💡 Wait, let me recalculate: 5 → subtract(5) = 4 → multiply(4) = 8 → add(8) = 9
// 💡 Actually: compose applies right to left, so: add(multiply(subtract(5)))
// 💡 subtract(5) = 4, multiply(4) = 8, add(8) = 9

// ✅ Pipe functions (Pipe functions - Áp dụng từ trái sang phải)
const pipe = <T>(...fns: Array<(x: T) => T>) => (value: T) =>
  fns.reduce((acc, fn) => fn(acc), value);
// 💡 pipe: Function kết hợp nhiều functions (từ trái sang phải)
// 💡 reduce: Áp dụng functions từ trái sang phải
// 💡 pipe(f, g, h)(x) = h(g(f(x)))

const piped = pipe(subtract, multiply, add);
// 💡 piped: subtract → multiply → add
// 💡 x → subtract(x) → multiply(subtract(x)) → add(multiply(subtract(x)))

console.log(piped(5)); // 9
// 💡 5 → subtract(5) = 4 → multiply(4) = 8 → add(8) = 9

// 2️⃣ Object Composition (Kết hợp Objects)
// ✅ Composition với Mixins (Kết hợp với Mixins)
const canEat = {
  eat() {
    console.log(`${this.name} is eating`);
  },
};

const canBark = {
  bark() {
    console.log(`${this.name} is barking`);
  },
};

const canFly = {
  fly() {
    console.log(`${this.name} is flying`);
  },
};

// ✅ Compose behaviors (Kết hợp behaviors)
function createDog(name: string) {
  return {
    name,
    ...canEat, // ✅ Mixin canEat
    ...canBark, // ✅ Mixin canBark
  };
  // 💡 Dog HAS-A eat behavior, HAS-A bark behavior
  // 💡 Không phải IS-A Animal → Flexible hơn
}

function createBird(name: string) {
  return {
    name,
    ...canEat, // ✅ Mixin canEat
    ...canFly, // ✅ Mixin canFly
  };
  // 💡 Bird HAS-A eat behavior, HAS-A fly behavior
}

const dog = createDog('Buddy');
dog.eat(); // "Buddy is eating"
dog.bark(); // "Buddy is barking"

const bird = createBird('Tweety');
bird.eat(); // "Tweety is eating"
bird.fly(); // "Tweety is flying"

// 3️⃣ Higher-Order Component Composition (Kết hợp HOC)
// ✅ React HOC Composition
const withAuth = (Component: React.ComponentType) => {
  // 💡 withAuth: HOC thêm authentication logic
  return (props: any) => {
    const isAuthenticated = checkAuth(); // 🔐 Check authentication
    if (!isAuthenticated) return <LoginPage />;
    return <Component {...props} />;
  };
};

const withLogging = (Component: React.ComponentType) => {
  // 💡 withLogging: HOC thêm logging logic
  return (props: any) => {
    console.log('Component rendered:', Component.name);
    return <Component {...props} />;
  };
};

const withErrorBoundary = (Component: React.ComponentType) => {
  // 💡 withErrorBoundary: HOC thêm error handling
  return (props: any) => {
    return (
      <ErrorBoundary>
        <Component {...props} />
      </ErrorBoundary>
    );
  };
};

// ✅ Compose HOCs (Kết hợp HOCs)
const composeHOCs = (...hocs: Array<(C: any) => any>) => (Component: any) =>
  hocs.reduceRight((acc, hoc) => hoc(acc), Component);
// 💡 composeHOCs: Kết hợp nhiều HOCs
// 💡 reduceRight: Áp dụng HOCs từ phải sang trái

const EnhancedComponent = composeHOCs(
  withAuth, // 🔐 Auth check
  withLogging, // 📝 Logging
  withErrorBoundary // 🛡️ Error handling
)(MyComponent);
// 💡 EnhancedComponent: Component với auth + logging + error handling
// 💡 Composition: Kết hợp nhiều behaviors → Flexible, testable
```

**📊 So Sánh Composition vs Inheritance:**

| Aspect           | Inheritance            | Composition                    |
| ---------------- | ---------------------- | ------------------------------ |
| **Relationship** | IS-A (Dog IS-A Animal) | HAS-A (Dog HAS-A eat behavior) |
| **Coupling**     | ❌ Tight coupling      | ✅ Loose coupling              |
| **Flexibility**  | ❌ Khó thay đổi        | ✅ Dễ thay đổi                 |
| **Reusability**  | ❌ Phụ thuộc parent    | ✅ Tái sử dụng độc lập         |
| **Testing**      | ❌ Khó test            | ✅ Dễ test                     |
| **Complexity**   | ⚠️ Diamond problem     | ✅ Đơn giản hơn                |

**💡 Khi Nào Dùng Inheritance vs Composition?**

- ✅ **Dùng Composition khi**: Cần flexibility, reusability, testability
- ⚠️ **Dùng Inheritance khi**: Có "IS-A" relationship rõ ràng, shared behavior nhiều
- 💡 **Best Practice**: "Favor composition over inheritance" (Ưu tiên composition hơn inheritance)

---

## **📚 PHẦN 5: RAMDA & LODASH/FP (Functional Programming Libraries)**

**💡 Ramda & Lodash/fp Là Gì?**

**Ramda** và **Lodash/fp** là các thư viện JavaScript hỗ trợ Functional Programming với:

- **Auto-curried functions**: Tất cả functions đều được curry sẵn
- **Data-last**: Parameters được sắp xếp để dễ compose
- **Immutable operations**: Tất cả operations đều immutable

```typescript
// 📦 RAMDA - Functional Programming Library
import * as R from 'ramda';

// 1️⃣ Auto-curried Functions (Functions tự động curry)
// ✅ Ramda functions đều được curry sẵn
const add = R.add; // 💡 R.add: (a: number) => (b: number) => number
const add5 = R.add(5); // ✅ Partial application - Tạo function mới
console.log(add5(10)); // 15

const multiply = R.multiply; // 💡 R.multiply: (a: number) => (b: number) => number
const double = R.multiply(2); // ✅ Tạo function nhân đôi
console.log(double(5)); // 10

// 2️⃣ Data-Last Parameters (Tham số data đặt cuối)
const numbers = [1, 2, 3, 4, 5];

// ✅ Ramda: Data-last (data ở cuối) → Dễ compose
const doubled = R.map(R.multiply(2), numbers); // ✅ numbers ở cuối
// 💡 R.map: (fn, data) → Dễ compose vì data ở cuối
// 💡 R.multiply(2): Function nhân 2 (đã curry)

// ✅ Compose với Ramda
const processNumbers = R.pipe(
  R.map(R.multiply(2)), // ✖️ Nhân đôi
  R.filter(R.gt(R.__, 5)), // 🔍 Lọc > 5 (R.__ là placeholder)
  R.sum // ➕ Tổng
);
// 💡 R.pipe: Compose functions từ trái sang phải
// 💡 R.__: Placeholder cho tham số (R.gt(R.__, 5) = x => x > 5)

console.log(processNumbers(numbers)); // 24
// 💡 [1,2,3,4,5] → [2,4,6,8,10] → [6,8,10] → 24

// 3️⃣ Immutable Operations (Operations bất biến)
const users = [
  { name: 'John', age: 25 },
  { name: 'Jane', age: 30 },
  { name: 'Bob', age: 35 },
];

// ✅ Ramda: Tất cả operations đều immutable
const updatedUsers = R.map(
  R.when(
    R.propEq('name', 'John'), // 🔍 Nếu name === 'John'
    R.assoc('age', 26) // ✅ Update age = 26
  ),
  users
);
// 💡 R.map: Tạo array mới (immutable)
// 💡 R.when: Conditional update
// 💡 R.propEq: Check property equals
// 💡 R.assoc: Set property (immutable)
// 💡 users không bị thay đổi

console.log(users[0].age); // 25 - users không đổi ✅
console.log(updatedUsers[0].age); // 26 - updatedUsers là array mới

// 4️⃣ Function Composition với Ramda
const getActiveUserNames = R.pipe(
  R.filter(R.propEq('active', true)), // 🔍 Lọc active users
  R.map(R.prop('name')), // 📝 Lấy name
  R.map(R.toUpper) // 🔤 Uppercase
);
// 💡 R.pipe: Compose từ trái sang phải
// 💡 R.prop: Lấy property
// 💡 R.toUpper: Uppercase string

const users2 = [
  { name: 'John', active: true },
  { name: 'Jane', active: false },
  { name: 'Bob', active: true },
];

console.log(getActiveUserNames(users2)); // ['JOHN', 'BOB']

// 5️⃣ Lens (Lens - Cách truy cập/update nested data)
const userLens = R.lensPath(['user', 'profile', 'age']);
// 💡 R.lensPath: Tạo lens cho nested path
// 💡 Lens: Cách truy cập và update nested data immutable

const state = {
  user: {
    profile: {
      age: 25,
    },
  },
};

const newAge = R.view(userLens, state); // 👁️ View: Lấy giá trị
console.log(newAge); // 25

const updatedState = R.set(userLens, 26, state); // ✏️ Set: Update giá trị
// 💡 R.set: Update immutable (tạo object mới)
console.log(state.user.profile.age); // 25 - state không đổi ✅
console.log(updatedState.user.profile.age); // 26 - updatedState là object mới

const incrementedState = R.over(userLens, R.inc, state); // ➕ Over: Transform giá trị
// 💡 R.over: Transform giá trị với function (immutable)
// 💡 R.inc: Increment (x => x + 1)
console.log(incrementedState.user.profile.age); // 26

// 📦 LODASH/FP - Functional Programming version của Lodash
import * as _ from 'lodash/fp';
// 💡 lodash/fp: Functional Programming version
// 💡 Auto-curried, data-last, immutable

// ✅ Lodash/fp: Tương tự Ramda
const numbers2 = [1, 2, 3, 4, 5];

const doubled2 = _.map(_.multiply(2), numbers2); // ✅ Auto-curried, data-last
console.log(doubled2); // [2, 4, 6, 8, 10]

const sum = _.pipe(
  _.map(_.multiply(2)), // ✖️ Nhân đôi
  _.filter(_.gt(_.__, 5)), // 🔍 Lọc > 5
  _.sum() // ➕ Tổng
)(numbers2);
console.log(sum); // 24

// ✅ Lodash/fp: Một số functions khác với Ramda
const users3 = [
  { name: 'John', age: 25, active: true },
  { name: 'Jane', age: 30, active: false },
];

const activeUsers = _.filter(_.prop('active'), users3); // 🔍 Lọc active users
console.log(activeUsers); // [{ name: 'John', age: 25, active: true }]

const userNames = _.map(_.prop('name'), users3); // 📝 Lấy names
console.log(userNames); // ['John', 'Jane']
```

**📊 So Sánh Ramda vs Lodash/fp:**

| Aspect            | Ramda              | Lodash/fp          |
| ----------------- | ------------------ | ------------------ |
| **Size**          | ⚠️ Lớn hơn (~50KB) | ✅ Nhỏ hơn (~25KB) |
| **Currying**      | ✅ Auto-curried    | ✅ Auto-curried    |
| **Data-last**     | ✅ Data-last       | ✅ Data-last       |
| **Lens**          | ✅ Có Lens         | ❌ Không có        |
| **Documentation** | ✅ Tốt             | ✅ Tốt             |
| **Community**     | ✅ Active          | ✅ Very active     |

**💡 Khi Nào Dùng Ramda vs Lodash/fp?**

- ✅ **Dùng Ramda khi**: Cần Lens, functional programming thuần túy
- ✅ **Dùng Lodash/fp khi**: Cần size nhỏ, đã quen với Lodash
- 💡 **Best Practice**: Chọn 1 library và stick with it (chọn 1 và dùng nhất quán)

---

## **📚 PHẦN 6: MEMOIZATION (Ghi Nhớ Kết Quả)**

**💡 Memoization Là Gì?**

Memoization là kỹ thuật **cache kết quả** của function calls để tránh tính toán lại với cùng input. Đặc biệt hữu ích cho **pure functions** và **expensive computations**.

```typescript
// ❌ KHÔNG có Memoization - Tính toán lại mỗi lần
function fibonacci(n: number): number {
  // 💡 fibonacci: Function tính số Fibonacci
  // 💡 Không có cache → Tính toán lại mỗi lần gọi
  // 💡 Expensive: O(2^n) time complexity

  if (n <= 1) return n;
  return fibonacci(n - 1) + fibonacci(n - 2);
  // 💡 Recursive: Gọi lại chính nó
  // 💡 Tính toán lại nhiều lần với cùng n → Chậm
}

console.time('fibonacci');
fibonacci(40); // ⏱️ Rất chậm (tính toán lại nhiều lần)
console.timeEnd('fibonacci'); // ~1-2 giây

// ✅ CÓ Memoization - Cache kết quả
function memoize<T extends (...args: any[]) => any>(fn: T): T {
  // 💡 memoize: Higher-Order Function tạo memoized version
  // 💡 <T extends (...args: any[]) => any>: Generic type cho function
  // 💡 Return: Function cùng type nhưng có cache

  const cache = new Map<string, ReturnType<T>>();
  // 💡 cache: Map lưu kết quả đã tính toán
  // 💡 Key: String representation của arguments
  // 💡 Value: Kết quả đã tính toán

  return ((...args: Parameters<T>) => {
    // 💡 Return function mới với caching logic
    const key = JSON.stringify(args); // 🔑 Tạo key từ arguments
    // 💡 JSON.stringify: Convert arguments thành string key

    if (cache.has(key)) {
      // 💡 Check cache → Nếu đã có → Return cached result
      return cache.get(key)!; // ✅ Return từ cache → Nhanh
    }

    const result = fn(...args); // 🔧 Tính toán nếu chưa có trong cache
    cache.set(key, result); // 💾 Lưu kết quả vào cache
    return result; // 📤 Return kết quả
  }) as T;
}

const memoizedFibonacci = memoize(fibonacci);
// 💡 memoizedFibonacci: Fibonacci function với memoization
// 💡 Cache kết quả → Không tính toán lại với cùng input

console.time('memoizedFibonacci');
memoizedFibonacci(40); // ⚡ Nhanh hơn nhiều (dùng cache)
console.timeEnd('memoizedFibonacci'); // ~0.001 giây

// ✅ Memoization với React useMemo
import { useMemo } from 'react';

function ExpensiveComponent({ data }: { data: number[] }) {
  // 💡 ExpensiveComponent: Component với expensive computation

  const expensiveValue = useMemo(() => {
    // 💡 useMemo: React hook cho memoization
    // 💡 Chỉ tính toán lại khi data thay đổi
    return data.reduce((sum, n) => sum + n * n, 0);
    // 💡 Expensive: Tính tổng bình phương
  }, [data]); // 🔑 Dependencies: Chỉ tính lại khi data thay đổi
  // 💡 Memoization: Cache kết quả → Không tính lại mỗi render

  return <div>{expensiveValue}</div>;
}

// ✅ Memoization với Lodash
import { memoize } from 'lodash';

const expensiveFunction = (n: number) => {
  // 💡 expensiveFunction: Function tính toán phức tạp
  let result = 0;
  for (let i = 0; i < n * 1000000; i++) {
    result += i;
  }
  return result;
};

const memoizedExpensive = memoize(expensiveFunction);
// 💡 memoize: Lodash function tạo memoized version
// 💡 Cache kết quả → Không tính lại với cùng input

console.log(memoizedExpensive(1000)); // ⏱️ Tính toán lần đầu (chậm)
console.log(memoizedExpensive(1000)); // ⚡ Lần 2 (nhanh - dùng cache)
```

**✅ Ưu Điểm của Memoization:**

- ✅ **Performance**: Tránh tính toán lại → Nhanh hơn
- ✅ **Efficiency**: Giảm CPU usage cho expensive computations
- ✅ **Scalability**: Cải thiện performance khi có nhiều calls

**❌ Nhược Điểm của Memoization:**

- ❌ **Memory Overhead**: Tốn memory để lưu cache
- ❌ **Cache Invalidation**: Cần strategy để invalidate cache
- ❌ **Only for Pure Functions**: Chỉ work tốt với pure functions

---

## **📚 PHẦN 7: FUNCTION COMPOSITION CHI TIẾT (Kết Hợp Functions)**

**💡 Function Composition Là Gì?**

Function Composition là kỹ thuật **kết hợp nhiều functions nhỏ** thành **function lớn hơn**. Output của function này là input của function kia.

```typescript
// ✅ Basic Composition (Composition Cơ Bản)
const add = (x: number) => x + 1; // ➕ Cộng 1
const multiply = (x: number) => x * 2; // ✖️ Nhân 2
const subtract = (x: number) => x - 1; // ➖ Trừ 1

// ✅ Compose (Từ phải sang trái)
const compose =
  <T>(...fns: Array<(x: T) => T>) =>
  (value: T) =>
    fns.reduceRight((acc, fn) => fn(acc), value);
// 💡 compose: Function kết hợp nhiều functions
// 💡 reduceRight: Áp dụng từ phải sang trái
// 💡 compose(f, g, h)(x) = f(g(h(x)))

const composed = compose(add, multiply, subtract);
// 💡 composed: subtract → multiply → add
// 💡 x → subtract(x) → multiply(subtract(x)) → add(multiply(subtract(x)))

console.log(composed(5)); // 9
// 💡 5 → subtract(5) = 4 → multiply(4) = 8 → add(8) = 9

// ✅ Pipe (Từ trái sang phải - Dễ đọc hơn)
const pipe =
  <T>(...fns: Array<(x: T) => T>) =>
  (value: T) =>
    fns.reduce((acc, fn) => fn(acc), value);
// 💡 pipe: Function kết hợp nhiều functions (từ trái sang phải)
// 💡 reduce: Áp dụng từ trái sang phải
// 💡 pipe(f, g, h)(x) = h(g(f(x)))

const piped = pipe(subtract, multiply, add);
// 💡 piped: subtract → multiply → add
// 💡 x → subtract(x) → multiply(subtract(x)) → add(multiply(subtract(x)))

console.log(piped(5)); // 9
// 💡 5 → subtract(5) = 4 → multiply(4) = 8 → add(8) = 9

// ✅ Composition với Different Types (Composition với Types Khác Nhau)
const toUpperCase = (str: string) => str.toUpperCase(); // 🔤 Uppercase
const addExclamation = (str: string) => str + '!'; // ➕ Thêm dấu chấm than
const repeat = (str: string) => str.repeat(2); // 🔁 Lặp lại

const processString = pipe(toUpperCase, addExclamation, repeat);
// 💡 processString: Uppercase → Add exclamation → Repeat
// 💡 Type-safe: Tất cả functions đều nhận string → return string

console.log(processString('hello')); // "HELLO!HELLO!"
// 💡 'hello' → 'HELLO' → 'HELLO!' → 'HELLO!HELLO!'

// ✅ Composition với Array Operations (Composition với Array Operations)
const numbers = [1, 2, 3, 4, 5];

const processNumbers = pipe(
  (arr: number[]) => arr.filter((n) => n > 2), // 🔍 Lọc > 2
  (arr: number[]) => arr.map((n) => n * 2), // ✖️ Nhân đôi
  (arr: number[]) => arr.reduce((sum, n) => sum + n, 0) // ➕ Tổng
);
// 💡 processNumbers: Filter → Map → Reduce
// 💡 Type-safe: Tất cả functions nhận number[] → return number[]

console.log(processNumbers(numbers)); // 24
// 💡 [1,2,3,4,5] → [3,4,5] → [6,8,10] → 24

// ✅ Composition với Ramda
import * as R from 'ramda';

const processUsers = R.pipe(
  R.filter(R.propEq('active', true)), // 🔍 Lọc active users
  R.map(R.prop('name')), // 📝 Lấy name
  R.map(R.toUpper), // 🔤 Uppercase
  R.sortBy(R.identity) // 🔄 Sort
);
// 💡 R.pipe: Ramda pipe function
// 💡 Compose từ trái sang phải → Dễ đọc

const users = [
  { name: 'John', active: true },
  { name: 'Jane', active: false },
  { name: 'Bob', active: true },
];

console.log(processUsers(users)); // ['BOB', 'JOHN']
// 💡 Filter → Map names → Uppercase → Sort

// ✅ Composition với Error Handling (Composition với Xử Lý Lỗi)
type Result<T> = { success: true; data: T } | { success: false; error: string };
// 💡 Result: Type cho success/error handling

const safeParse = (str: string): Result<number> => {
  // 💡 safeParse: Parse string safely với error handling
  const num = Number(str);
  if (isNaN(num)) {
    return { success: false, error: 'Invalid number' };
  }
  return { success: true, data: num };
};

const safeMultiply =
  (x: number) =>
  (y: number): Result<number> => {
    // 💡 safeMultiply: Multiply với error handling
    if (x === 0 || y === 0) {
      return { success: false, error: 'Cannot multiply by zero' };
    }
    return { success: true, data: x * y };
  };

const composeWithErrorHandling =
  <T, U, V>(f: (x: T) => Result<U>, g: (x: U) => Result<V>) =>
  (x: T): Result<V> => {
    // 💡 composeWithErrorHandling: Compose với error handling
    const result1 = f(x); // 🔧 Gọi function đầu tiên
    if (!result1.success) {
      return result1; // ❌ Return error nếu fail
    }
    return g(result1.data); // ✅ Gọi function tiếp theo với data
  };
// 💡 Compose với error handling → Stop nếu có lỗi
```

**✅ Ưu Điểm của Function Composition:**

- ✅ **Reusability**: Tái sử dụng functions nhỏ
- ✅ **Readability**: Code dễ đọc, dễ hiểu
- ✅ **Testability**: Dễ test từng function nhỏ
- ✅ **Modularity**: Functions độc lập, dễ maintain

---

## **📚 PHẦN 8: RECURSION TRONG FUNCTIONAL PROGRAMMING (Đệ Quy)**

**💡 Recursion Là Gì?**

Recursion là kỹ thuật function **gọi lại chính nó** để giải quyết vấn đề. Trong Functional Programming, recursion thay thế loops.

```typescript
// ❌ Imperative với Loop (Mệnh Lệnh với Loop)
function sumArray(arr: number[]): number {
  // 💡 sumArray: Tính tổng array với loop
  let sum = 0; // ⚠️ Mutable variable
  for (let i = 0; i < arr.length; i++) {
    sum += arr[i]; // ❌ Mutate sum
  }
  return sum;
}

// ✅ Functional với Recursion (Functional với Đệ Quy)
function sumArrayRecursive(arr: number[]): number {
  // 💡 sumArrayRecursive: Tính tổng array với recursion
  // 💡 Base case: Array rỗng → return 0
  if (arr.length === 0) {
    return 0; // ✅ Base case: Stop recursion
  }

  // 💡 Recursive case: Tổng = phần tử đầu + tổng phần còn lại
  return arr[0] + sumArrayRecursive(arr.slice(1));
  // 💡 arr[0]: Phần tử đầu tiên
  // 💡 arr.slice(1): Phần còn lại (immutable)
  // 💡 Recursive: Gọi lại chính nó với array nhỏ hơn
}

console.log(sumArrayRecursive([1, 2, 3, 4, 5])); // 15
// 💡 sumArrayRecursive([1,2,3,4,5])
//    = 1 + sumArrayRecursive([2,3,4,5])
//    = 1 + 2 + sumArrayRecursive([3,4,5])
//    = 1 + 2 + 3 + sumArrayRecursive([4,5])
//    = 1 + 2 + 3 + 4 + sumArrayRecursive([5])
//    = 1 + 2 + 3 + 4 + 5 + sumArrayRecursive([])
//    = 1 + 2 + 3 + 4 + 5 + 0 = 15

// ✅ Tail Recursion (Đệ Quy Đuôi - Tối Ưu)
function sumArrayTailRecursive(arr: number[], accumulator: number = 0): number {
  // 💡 sumArrayTailRecursive: Tail recursion (tối ưu hơn)
  // 💡 accumulator: Tích lũy kết quả
  // 💡 Tail recursion: Recursive call là operation cuối cùng

  if (arr.length === 0) {
    return accumulator; // ✅ Base case: Return accumulator
  }

  return sumArrayTailRecursive(arr.slice(1), accumulator + arr[0]);
  // 💡 Tail recursion: Recursive call là operation cuối cùng
  // 💡 JavaScript engines có thể optimize tail recursion
  // 💡 → Không tạo nhiều stack frames → Hiệu quả hơn
}

console.log(sumArrayTailRecursive([1, 2, 3, 4, 5])); // 15

// ✅ Recursion với Tree Traversal (Đệ Quy với Duyệt Cây)
type TreeNode = {
  value: number;
  left?: TreeNode;
  right?: TreeNode;
};

function sumTree(node: TreeNode | undefined): number {
  // 💡 sumTree: Tính tổng cây nhị phân với recursion
  if (!node) {
    return 0; // ✅ Base case: Node null → return 0
  }

  return (
    node.value +
    sumTree(node.left) + // 🔄 Recursive: Sum left subtree
    sumTree(node.right) // 🔄 Recursive: Sum right subtree
  );
  // 💡 Recursion: Duyệt cây tự nhiên với recursion
}

const tree: TreeNode = {
  value: 1,
  left: {
    value: 2,
    left: { value: 4 },
    right: { value: 5 },
  },
  right: {
    value: 3,
    left: { value: 6 },
    right: { value: 7 },
  },
};

console.log(sumTree(tree)); // 28
// 💡 1 + (2 + 4 + 5) + (3 + 6 + 7) = 28

// ✅ Recursion với Array Operations (Đệ Quy với Array Operations)
function mapRecursive<T, U>(arr: T[], fn: (x: T) => U): U[] {
  // 💡 mapRecursive: Map với recursion
  if (arr.length === 0) {
    return []; // ✅ Base case: Array rỗng → return []
  }

  return [
    fn(arr[0]), // 🔧 Transform phần tử đầu
    ...mapRecursive(arr.slice(1), fn), // 🔄 Recursive: Map phần còn lại
  ];
  // 💡 Spread operator: Kết hợp phần tử đầu + array đã map
}

console.log(mapRecursive([1, 2, 3], (x) => x * 2)); // [2, 4, 6]

function filterRecursive<T>(arr: T[], predicate: (x: T) => boolean): T[] {
  // 💡 filterRecursive: Filter với recursion
  if (arr.length === 0) {
    return []; // ✅ Base case: Array rỗng → return []
  }

  const rest = filterRecursive(arr.slice(1), predicate); // 🔄 Recursive
  // 💡 Filter phần còn lại trước

  if (predicate(arr[0])) {
    return [arr[0], ...rest]; // ✅ Include nếu thỏa điều kiện
  }
  return rest; // ❌ Exclude nếu không thỏa điều kiện
}

console.log(filterRecursive([1, 2, 3, 4, 5], (x) => x % 2 === 0)); // [2, 4]

// ✅ Recursion với Memoization (Đệ Quy với Memoization)
const memoizedFibonacci = memoize((n: number): number => {
  // 💡 memoizedFibonacci: Fibonacci với memoization
  if (n <= 1) {
    return n; // ✅ Base case: n <= 1 → return n
  }

  return memoizedFibonacci(n - 1) + memoizedFibonacci(n - 2);
  // 💡 Recursive: Gọi lại với n-1 và n-2
  // 💡 Memoization: Cache kết quả → Không tính lại
});

console.log(memoizedFibonacci(40)); // ⚡ Nhanh (dùng cache)
```

**✅ Ưu Điểm của Recursion:**

- ✅ **Functional Style**: Phù hợp với Functional Programming
- ✅ **Readability**: Code dễ đọc, tự nhiên
- ✅ **Immutability**: Không cần mutable variables
- ✅ **Tree/Graph Traversal**: Tự nhiên cho recursive structures

**❌ Nhược Điểm của Recursion:**

- ❌ **Stack Overflow**: Có thể gây stack overflow với deep recursion
- ❌ **Performance**: Có thể chậm hơn loops (nhưng có thể optimize với tail recursion)
- ❌ **Memory**: Tốn memory cho call stack

**💡 Best Practices:**

- ✅ **Use Tail Recursion**: Tối ưu performance
- ✅ **Use Memoization**: Cache kết quả cho expensive recursive calls
- ✅ **Consider Iteration**: Đôi khi loops đơn giản hơn

---

**📝 Tóm Tắt Mở Rộng:**

| Concept            | Mô Tả                                       | Use Case                                              |
| ------------------ | ------------------------------------------- | ----------------------------------------------------- |
| **IIFE**           | Function tự gọi ngay, tạo scope riêng       | Module pattern, private state, avoid global pollution |
| **Pure Functions** | Same input → same output, no side effects   | Business logic, calculations, testable code           |
| **Currying**       | Function nhiều params → chuỗi functions     | Reusable functions, partial application               |
| **HOF**            | Function nhận/trả về function               | map, filter, reduce, decorators, middleware           |
| **Immutability**   | Không thay đổi dữ liệu gốc, tạo bản sao mới | React state, Redux, functional updates                |
| **Composition**    | Kết hợp behaviors thay vì kế thừa           | Flexible architecture, reusable code                  |
| **Memoization**    | Cache kết quả function calls                | Expensive computations, performance optimization      |
| **Recursion**      | Function gọi lại chính nó                   | Tree traversal, recursive data structures             |
| **Ramda**          | FP library với auto-curry, data-last        | Functional programming, data transformations          |
| **Lodash/fp**      | FP version của Lodash                       | Functional utilities, smaller bundle                  |
