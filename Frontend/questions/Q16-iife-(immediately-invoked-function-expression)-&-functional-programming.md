# 🎯 Q16: IIFE (Immediately Invoked Function Expression) & Functional Programming

<details>
<summary><span style="font-size:1.25em;font-weight:bold;">🎯 Q16: IIFE (Immediately Invoked Function Expression) & Functional Programming</span></summary>


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
// 1️⃣ Module Pattern - Tạo private state
const calculator = (function () {
  let result = 0; // ⚠️ Private variable - không thể access từ bên ngoài

  return {
    add(x: number): number {
      result += x; // Chỉ thay đổi được qua method này
      return result;
    },
    subtract(x: number): number {
      result -= x;
      return result;
    },
    getResult(): number {
      return result; // Chỉ đọc được qua method này
    },
  };
})();

calculator.add(10); // 10
calculator.subtract(3); // 7
console.log(calculator.result); // undefined - ❌ Không access được private variable
console.log(calculator.getResult()); // 7 - ✅ Phải dùng method

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
// ✅ Pure Function - Hoàn hảo!
function add(a: number, b: number): number {
  return a + b; // ✅ Chỉ tính toán, không side effects
}

console.log(add(2, 3)); // 5 - Gọi 1000 lần vẫn trả về 5
console.log(add(2, 3)); // 5 - Predictable (dự đoán được)

// ❌ Impure Function - Có side effects
let counter = 0; // ⚠️ External state

function increment(): number {
  counter++; // ❌ Side effect - thay đổi biến bên ngoài
  return counter;
}

console.log(increment()); // 1
console.log(increment()); // 2 - ❌ Cùng input (không có), khác output!

// ✅ Chuyển thành Pure Function
function increment(counter: number): number {
  return counter + 1; // ✅ Không thay đổi state, return giá trị mới
}

let myCounter = 0;
myCounter = increment(myCounter); // 1 - Rõ ràng, dễ test
myCounter = increment(myCounter); // 2
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
  return a + b;
}
console.log(add(2, 3)); // 5 - Phải truyền cả 2 số

// ✅ Currying - Nhận từng tham số một
const add = (a: number) => (b: number) => a + b;
//            ↑ nhận a    ↑ trả về function nhận b

const add2 = add(2); // add2 là function: (b) => 2 + b
console.log(add2(3)); // 5 - Giống kết quả trên
console.log(add2(10)); // 12 - Có thể tái sử dụng add2
console.log(add(2)(3)); // 5 - Hoặc gọi luôn
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
// 1️⃣ HOF nhận function làm argument
function withLogging<T extends (...args: any[]) => any>(
  fn: T // ⚠️ Nhận function làm tham số
): (...args: Parameters<T>) => ReturnType<T> {
  return (...args: Parameters<T>) => {
    console.log('🔍 Gọi function với:', args);
    const result = fn(...args); // Gọi function gốc
    console.log('✅ Kết quả:', result);
    return result;
  };
}

const add = (a: number, b: number) => a + b;
const loggedAdd = withLogging(add); // Bọc add với logging

loggedAdd(2, 3);
// Output:
// 🔍 Gọi function với: [2, 3]
// ✅ Kết quả: 5

// 2️⃣ HOF trả về function
function createGreeter(greeting: string) {
  return (name: string) => `${greeting}, ${name}!`; // ⚠️ Return function
}

const sayHello = createGreeter('Xin chào'); // Tạo function chào hỏi
const sayHi = createGreeter('Hi'); // Tạo function chào hỏi khác

console.log(sayHello('John')); // "Xin chào, John!"
console.log(sayHi('Jane')); // "Hi, Jane!"

// 3️⃣ Array methods đều là HOF
const numbers = [1, 2, 3, 4, 5];

const doubled = numbers.map((x) => x * 2); // [2, 4, 6, 8, 10]
//                          ↑ nhận function làm argument

const evens = numbers.filter((x) => x % 2 === 0); // [2, 4]
//                           ↑ nhận function làm argument

const sum = numbers.reduce((acc, x) => acc + x, 0); // 15
//                         ↑ nhận function làm argument
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

## **Phần 5: DOM & Events**

