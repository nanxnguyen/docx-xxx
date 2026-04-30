# ⎫ Q04: Hoisting & Temporal Dead Zone

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (1-2 phút):**

**"Hoisting = khai báo được đưa lên đầu scope. TDZ = vùng không thể truy cập let/const trước khi khai báo.**

**🔑 Hoisting Behaviors:**

| Type | Hoisted? | Initialized? | Access Before Declaration |
|------|----------|--------------|---------------------------|
| **`var`** | ✅ Yes | ✅ Yes (`undefined`) | ✅ OK (undefined) |
| **`let`** | ✅ Yes | ❌ No (TDZ) | ❌ ReferenceError |
| **`const`** | ✅ Yes | ❌ No (TDZ) | ❌ ReferenceError |
| **`function` declaration** | ✅ Yes | ✅ Yes (entire function) | ✅ OK (callable) |
| **`function` expression** | ✅ Yes (variable only) | ❌ No | ❌ ReferenceError/undefined |
| **`class`** | ✅ Yes | ❌ No (TDZ) | ❌ ReferenceError |

**📊 Detailed Explanation:**

1. **`var` Hoisting**:
   - Hoisted + initialized với `undefined`.
   - Access trước khai báo → `undefined` (không error).
   ```js
   console.log(x); // undefined
   var x = 5;
   // Engine sees: var x = undefined; console.log(x); x = 5;
   ```

2. **`let/const` Hoisting + TDZ**:
   - Hoisted nhưng NOT initialized → Temporal Dead Zone.
   - Access trong TDZ → `ReferenceError`.
   - TDZ = từ đầu block scope đến dòng khai báo.
   ```js
   // TDZ starts
   console.log(y); // ReferenceError
   let y = 10; // TDZ ends
   ```

3. **Function Declaration Hoisting**:
   - Entire function hoisted → gọi trước khai báo OK.
   ```js
   hello(); // "Hello!" ✅
   function hello() { console.log("Hello!"); }
   ```

4. **Function Expression**:
   - Variable hoisted nhưng function không.
   ```js
   hello(); // TypeError: hello is not a function
   var hello = function() { console.log("Hello!"); };
   ```

**⚠️ Common Pitfalls:**
- **`typeof` trong TDZ**: `typeof x` với `let x` → ReferenceError (không safe như `var`).
- **Loop variables**: `var` trong loop → function scope, `let` → block scope per iteration.
  ```js
  for (var i = 0; i < 3; i++) {
    setTimeout(() => console.log(i)); // 3, 3, 3 (same i)
  }
  for (let i = 0; i < 3; i++) {
    setTimeout(() => console.log(i)); // 0, 1, 2 (different i per iteration)
  }
  ```

**💡 Senior Insights:**
- **Why TDZ exists**: Force developers khai báo trước khi dùng → catch bugs sớm.
- **Hoisting mechanism**: JavaScript engine scans code 2 passes:
  1. **Creation phase**: Allocate memory cho declarations.
  2. **Execution phase**: Execute code line-by-line.
- **Best Practice**: 
  - Dùng `const` by default, `let` nếu cần reassign, avoid `var`.
  - Khai báo biến ở top của scope → explicit, tránh confusion.
  - Dùng ESLint rule `no-use-before-define`.

---

**⚡ Quick Summary:**
> Hoisting = Khai báo được đưa lên đầu scope. `var` = undefined, `let/const` = TDZ → ReferenceError

**💡 Ghi Nhớ:**
- 🔥 **var**: Hoisted + initialized = undefined → dùng trước khai báo OK (nhưng undefined)
- ⚡ **let/const**: Hoisted nhưng NOT initialized → TDZ → ReferenceError
- 🎯 **function declaration**: Hoisted toàn bộ → gọi trước khai báo OK
- ⏰ **TDZ**: Vùng từ đầu scope đến dòng khai báo - biến tồn tại nhưng không access được


**Trả lời:**

- **Hoisting**: Cơ chế đưa declarations lên đầu scope trước khi code execute
- **TDZ (Temporal Dead Zone)**: Vùng từ đầu block scope đến dòng khai báo let/const - không thể access biến
- **Ưu điểm**: Function hoisting cho phép tổ chức code linh hoạt
- **Nhược điểm**: var hoisting gây confusion, TDZ errors khó debug

**Code Example:**

```typescript
// ═══════════════════════════════════════════════════════════
// 1. FUNCTION HOISTING
// ═══════════════════════════════════════════════════════════

// ✅ Function Declaration - hoisted hoàn toàn
console.log(sayHello('World')); // "Hello World" ✅
function sayHello(name: string): string {
  return `Hello ${name}`;
}

// ❌ Function Expression - không hoisted
// console.log(sayGoodbye("World")); // ReferenceError
const sayGoodbye = (name: string) => `Goodbye ${name}`;

// ═══════════════════════════════════════════════════════════
// 2. VAR HOISTING (không có TDZ)
// ═══════════════════════════════════════════════════════════

console.log(x); // undefined ✅ (không lỗi)
var x = 5;
console.log(x); // 5

// JavaScript "nhìn" code như:
// var x = undefined;
// console.log(x);
// x = 5;

// ═══════════════════════════════════════════════════════════
// 3. LET/CONST - TEMPORAL DEAD ZONE (TDZ)
// ═══════════════════════════════════════════════════════════

{
  // ← TDZ BẮT ĐẦU cho biến y
  
  // console.log(y); // ❌ ReferenceError - đang trong TDZ!
  // console.log(typeof y); // ❌ ReferenceError - typeof cũng không safe!
  
  let y = 10; // ← TDZ KẾT THÚC
  console.log(y); // ✅ 10
}

// So sánh var vs let
function compare() {
  console.log(a); // undefined ✅ - var không có TDZ
  var a = 1;
  
  // console.log(b); // ❌ ReferenceError - let có TDZ
  let b = 2;
}

// ═══════════════════════════════════════════════════════════
// 4. TDZ PITFALLS - Những cái bẫy
// ═══════════════════════════════════════════════════════════

// Pitfall 1: typeof trong TDZ
{
  // typeof x; // ❌ ReferenceError
  let x = 1;
}

// Pitfall 2: Nested scopes
let outer = 'outer';
{
  // console.log(outer); // ❌ ReferenceError!
  // Inner scope đã "claim" biến outer → TDZ
  let outer = 'inner';
}

// Pitfall 3: Default parameters
// function fn(a = b, b = 1) {} // ❌ ReferenceError - b trong TDZ
function fn(a = 1, b = a) {} // ✅ OK - a đã initialize

// Pitfall 4: Class hoisting
// const p = new Person(); // ❌ ReferenceError - class có TDZ
class Person {}
```

**Best Practices:**

```typescript
// ✅ Khai báo variables ở đầu scope
function good() {
  const a = 1;
  let b = 2;
  // ... logic
}

// ✅ Dùng const/let, tránh var
const API_URL = 'https://api.com'; // const cho values không đổi
let count = 0; // let khi cần re-assign

// ✅ Function declarations khi cần hoisting
helper(); // ✅ OK
function helper() {}

// ✅ Arrow/const cho callbacks
const process = (data) => data.map(x => x * 2);
```

**Common Mistakes:**

```typescript
// ❌ Mistake 1: var trong loops
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100); // 3, 3, 3 ❌
}

// ✅ Fix: let trong loops
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100); // 0, 1, 2 ✅
}

// ❌ Mistake 2: Access let/const trong TDZ
{
  // console.log(value); // ❌ ReferenceError
  let value = 10;
}

// ✅ Fix: Khai báo trước khi dùng
{
  let value = 10;
  console.log(value); // ✅ 10
}
```

**So Sánh:**

| Feature | var | let/const |
|---------|-----|-----------|
| Hoisted? | ✅ Có | ✅ Có |
| Initialized? | ✅ undefined | ❌ Không |
| TDZ? | ❌ Không | ✅ Có |
| Access trước khai báo | undefined | ReferenceError |
| Scope | Function | Block |

**💡 Key Takeaways:**

- **var**: Hoisted + undefined → access trước OK (nhưng undefined)
- **let/const**: Hoisted → TDZ → ReferenceError nếu access trước
- **function declaration**: Hoisted hoàn toàn → gọi trước OK
- **TDZ**: Từ đầu scope đến dòng khai báo - biến tồn tại nhưng không access được
- **typeof không safe** trong TDZ!
- **Luôn dùng const/let**, tránh var

