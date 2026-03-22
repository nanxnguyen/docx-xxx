# 🎯 Q02: Data Types & Memory Management - Tổng Hợp Toàn Diện

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"JavaScript có 8 kiểu dữ liệu: 7 nguyên thủy (không thay đổi được) + 1 phức tạp (object - thay đổi được).**

**📦 Nguyên Thủy vs Tham Chiếu:**

- **Nguyên thủy** (number, string, boolean, undefined, null, symbol, bigint):
  - Lưu theo GIÁ TRỊ trong stack.
  - Không thay đổi được → gán lại tạo giá trị mới.
  - Copy theo giá trị → các bản sao độc lập.
- **Tham chiếu** (object, array, function):
  - Lưu theo THAM CHIẾU trong heap.
  - Thay đổi được → sửa trực tiếp.
  - Copy theo tham chiếu → trỏ đến cùng object.

**🔑 Khái Niệm Cốt Lõi:**

1. **== vs ===**:
   - `==`: So sánh lỏng → chuyển đổi kiểu tự động (vd: `"5" == 5` → true).
   - `===`: So sánh nghiêm ngặt → không chuyển kiểu (vd: `"5" === 5` → false).
   - Thực hành tốt: Luôn dùng `===` trừ khi kiểm tra null/undefined.

2. **null vs undefined**:
   - `undefined`: Biến chưa được assign value (default).
   - `null`: Intentionally empty value (developer set).
   - `typeof null` → "object" (JavaScript bug legacy).

3. **Shallow Copy vs Deep Copy**:
   - **Shallow**: Copy top-level properties only → nested objects vẫn reference.
     ```js
     const shallow = { ...obj }; // Spread
     const shallow2 = Object.assign({}, obj);
     ```
   - **Deep**: Copy recursively tất cả levels → independent clone.
     ```js
     const deep = structuredClone(obj); // Native (modern)
     const deep2 = JSON.parse(JSON.stringify(obj)); // Hack (lose functions, dates)
     ```

4. **Type Checking**:
   - `typeof`: Check primitive types (`typeof "hello"` → "string").
   - `instanceof`: Check object types (`[] instanceof Array` → true).
   - `Array.isArray()`: Check arrays specifically.
   - `Object.prototype.toString.call()`: Most accurate (e.g., `[object Date]`).

**♻️ Memory Management & GC:**

- **Stack**: Primitive values, function calls (LIFO, fast, limited size).
- **Heap**: Objects, arrays (larger, slower, managed by GC).
- **Garbage Collection**: Mark-and-sweep algorithm → auto free unreachable objects.
- **Memory Leaks**:
  - Global variables không cleanup.
  - Event listeners không remove.
  - Closures giữ reference đến large objects.
  - Detached DOM nodes.

**⚠️ Common Pitfalls:**

- **Mutating objects**: `arr.push()` modify original → dùng immutable methods (`[...arr, item]`).
- **Reference comparison**: `{} === {}` → false (khác reference). Dùng deep equality libraries (lodash.isEqual).
- **Type coercion bugs**: `"5" + 3` → "53" (string concat), `"5" - 3` → 2 (number subtract).
- **Falsy values**: `0`, `""`, `null`, `undefined`, `false`, `NaN` → tất cả falsy nhưng khác nhau!

**💡 Senior Insights:**

- **Immutability**: Prefer immutable operations (spread, map, filter) → easier debugging, avoid side effects.
- **WeakMap/WeakSet**: Hold weak references → auto GC khi keys không còn reference → prevent memory leaks.
- **structuredClone()**: Modern deep clone (support Dates, RegExp, Typed Arrays), but lose functions/symbols.
- **Performance**: Primitive faster than objects (stack vs heap). Dùng primitives when possible.
- **TypeScript**: Eliminate runtime type errors → catch type mistakes at compile time.

---

> **Tổng hợp**: Primitive vs Reference, Falsy/Truthy, == vs ===, null vs undefined, Immutable vs Mutable, Deep/Shallow Copy, Type Checking, Memory Management & GC

---

## 📖 **Table of Contents**

- [I. Data Types Overview](#i-data-types-overview)
- [II. Primitive vs Reference Values](#ii-primitive-vs-reference-values)
- [III. Type Coercion & Comparison](#iii-type-coercion--comparison)
- [IV. Immutability & Copying](#iv-immutability--copying)
- [V. Type Checking Methods](#v-type-checking-methods)
- [VI. Memory Management & GC](#vi-memory-management--gc)
- [VII. Best Practices Summary](#vii-best-practices-summary)

---

## **I. Data Types Overview**

### **1.1. JavaScript Data Types (8 loại)**

```typescript
/**
 * ┌─────────────────────────────────────────────────────────────┐
 * │                   JAVASCRIPT DATA TYPES                      │
 * ├─────────────────────────────────────────────────────────────┤
 * │                                                              │
 * │  🔹 PRIMITIVE TYPES (7 loại - Immutable)                    │
 * │  ┌──────────────────────────────────────────────────────┐  │
 * │  │ 1. number      → 42, 3.14, NaN, Infinity             │  │
 * │  │ 2. string      → "hello", 'world', `template`        │  │
 * │  │ 3. boolean     → true, false                         │  │
 * │  │ 4. undefined   → undefined (chưa gán giá trị)        │  │
 * │  │ 5. null        → null (intentionally empty)          │  │
 * │  │ 6. symbol      → Symbol('id') (unique identifier)    │  │
 * │  │ 7. bigint      → 123456789n (số lớn hơn 2^53-1)     │  │
 * │  └──────────────────────────────────────────────────────┘  │
 * │                                                              │
 * │  🔸 COMPLEX TYPE (1 loại - Mutable)                         │
 * │  ┌──────────────────────────────────────────────────────┐  │
 * │  │ 8. object      → {}, [], Date, Map, Set, Function... │  │
 * │  └──────────────────────────────────────────────────────┘  │
 * └─────────────────────────────────────────────────────────────┘
 */

// Examples của từng type
const num: number = 42; // 1. number
const str: string = 'Hello'; // 2. string
const bool: boolean = true; // 3. boolean
const undef: undefined = undefined; // 4. undefined
const nul: null = null; // 5. null
const sym: symbol = Symbol('id'); // 6. symbol
const big: bigint = 123456789n; // 7. bigint
const obj: object = { name: 'John' }; // 8. object
const arr: number[] = [1, 2, 3]; // object subtype
const fn: Function = () => {}; // object subtype
```

### **1.2. Falsy vs Truthy Values**

```typescript
/**
 * ❌ 8 FALSY VALUES (Chỉ 8 giá trị này là falsy)
 */
console.log(Boolean(false)); // false
console.log(Boolean(0)); // false
console.log(Boolean(-0)); // false
console.log(Boolean(0n)); // false (BigInt zero)
console.log(Boolean('')); // false (empty string)
console.log(Boolean(null)); // false
console.log(Boolean(undefined)); // false
console.log(Boolean(NaN)); // false

/**
 * ✅ TRUTHY VALUES (Tất cả còn lại)
 */
console.log(Boolean([])); // true ⚠️ Empty array
console.log(Boolean({})); // true ⚠️ Empty object
console.log(Boolean('0')); // true ⚠️ String '0'
console.log(Boolean('false')); // true ⚠️ String 'false'
console.log(Boolean(-1)); // true
console.log(Boolean(Infinity)); // true

/**
 * 🎯 PRACTICAL USAGE
 */
// Filter falsy values
const numbers = [0, 1, 2, 3, '', null, 4];
const truthyNumbers = numbers.filter(Boolean); // [1, 2, 3, 4]

// Default values
function greet(name?: string) {
  return name ? `Hello ${name}` : 'Hello Guest';
}
```

---

## **II. Primitive vs Reference Values**

### **2.1. Memory Storage (Stack vs Heap)**

```typescript
/**
 * ┌──────────────────────────────────────────────────────────┐
 * │           STACK (Primitives)      HEAP (Objects)         │
 * ├──────────────────────────────────────────────────────────┤
 * │  📦 Lưu giá trị trực tiếp      📍 Lưu địa chỉ (pointer)  │
 * │  ⚡ Nhanh                       🐌 Chậm hơn              │
 * │  🔒 Immutable                  🔓 Mutable               │
 * │  📏 Kích thước cố định         📐 Kích thước động       │
 * │  ✂️ Copy = Clone giá trị       🔗 Copy = Share reference │
 * └──────────────────────────────────────────────────────────┘
 */

// PRIMITIVE (Stack) - Copy giá trị
let a: number = 10;
let b: number = a; // b = 10 (copy giá trị)
b = 20; // a vẫn = 10 ✅

console.log(a); // 10
console.log(b); // 20

// REFERENCE (Heap) - Copy địa chỉ
let obj1: { x: number } = { x: 10 };
let obj2 = obj1; // obj2 trỏ đến cùng địa chỉ
obj2.x = 20; // obj1.x cũng = 20 ⚠️

console.log(obj1.x); // 20 (bị thay đổi!)
console.log(obj2.x); // 20

/**
 * 🔍 VISUALIZE MEMORY:
 *
 * Stack:                    Heap:
 * ┌─────────┬─────┐        ┌──────────────┐
 * │ a       │ 10  │        │ { x: 10 }    │
 * │ b       │ 20  │        │    ↑         │
 * │ obj1    │ →   │────────┤    │         │
 * │ obj2    │ →   │────────┘ Cùng địa chỉ│
 * └─────────┴─────┘        └──────────────┘
 */
```

### **2.2. Pass by Value vs Pass by Reference**

```typescript
// PRIMITIVE - Pass by Value
function incrementNumber(num: number) {
  num = num + 1; // Chỉ thay đổi local copy
  return num;
}

let x = 10;
const result = incrementNumber(x);
console.log(x); // 10 (không đổi) ✅
console.log(result); // 11

// REFERENCE - Pass by Reference
function incrementAge(person: { age: number }) {
  person.age = person.age + 1; // Thay đổi object gốc!
  return person;
}

let user = { age: 25 };
const updatedUser = incrementAge(user);
console.log(user.age); // 26 (đã đổi!) ⚠️
console.log(updatedUser.age); // 26

/**
 * ✅ BEST PRACTICE: Return new object
 */
function incrementAgeImmutable(person: { age: number }) {
  return { ...person, age: person.age + 1 }; // Tạo object mới
}

let user2 = { age: 25 };
const updatedUser2 = incrementAgeImmutable(user2);
console.log(user2.age); // 25 (không đổi) ✅
console.log(updatedUser2.age); // 26
```

---

## **III. Type Coercion & Comparison**

### **3.1. == vs === (Loose vs Strict Equality)**

```typescript
/**
 * === (Strict Equality)
 * - So sánh type VÀ value
 * - KHÔNG type coercion
 * - ✅ Khuyến nghị dùng mặc định
 */
console.log(5 === 5); // true
console.log(5 === '5'); // false (khác type)
console.log(0 === false); // false (khác type)
console.log(null === undefined); // false

/**
 * == (Loose Equality)
 * - Tự động convert type (type coercion)
 * - ⚠️ Dễ gây bug, unpredictable
 */
console.log(5 == '5'); // true (string '5' → number 5)
console.log(0 == false); // true (false → 0)
console.log('' == 0); // true ('' → 0)
console.log([] == 0); // true ([] → '' → 0)
console.log([1] == 1); // true ([1] → '1' → 1)

/**
 * 🎯 EXCEPTION: null == undefined
 * Đây là cách NGẮN GỌN để check cả null VÀ undefined
 */
let value: string | null | undefined;

// ❌ Cách dài
if (value === null || value === undefined) {
}

// ✅ Cách ngắn (chỉ dùng == trong case này)
if (value == null) {
} // Check cả null VÀ undefined

/**
 * 📊 COERCION RULES:
 *
 * String + Number:  '5' == 5  → '5' to number → true
 * Boolean:          0 == false → false to 0 → true
 * Object:           [] == 0 → [] to '' to 0 → true
 * null/undefined:   null == undefined → true (special)
 */
```

### **3.2. null vs undefined**

```typescript
/**
 * null:
 * - Intentionally empty (lập trình viên set)
 * - typeof null === 'object' (historical bug)
 * - Dùng khi: Biến có giá trị nhưng đang empty
 */
let user: User | null = null; // Explicitly empty
function findUser(id: number): User | null {
  return database.find(id) || null; // Not found
}

/**
 * undefined:
 * - Unintentionally empty (chưa được gán)
 * - typeof undefined === 'undefined'
 * - Dùng khi: Biến chưa được khởi tạo, property không tồn tại
 */
let age: number; // undefined (chưa gán)
console.log(age); // undefined

const obj = { name: 'John' };
console.log(obj.email); // undefined (property không tồn tại)

function noReturn() {}
console.log(noReturn()); // undefined (không return)

/**
 * 🎯 BEST PRACTICES:
 */
// ✅ Dùng null cho intentional absence
let selectedUser: User | null = null;

// ✅ Dùng undefined cho optional parameters
function greet(name?: string) {
  console.log(name ?? 'Guest');
}

// ✅ Nullish coalescing (??) - chỉ check null/undefined
const age1 = 0 ?? 18; // 0 (không fallback)
const age2 = null ?? 18; // 18 (fallback)

// ✅ Optional chaining (?.)
const city = user?.address?.city; // Safe navigation
```

---

## **IV. Immutability & Copying**

### **4.1. Immutable vs Mutable**

```typescript
/**
 * 🔒 IMMUTABLE (Primitives)
 * - Không thể thay đổi sau khi tạo
 * - Mọi "thay đổi" đều tạo giá trị mới
 */
let str: string = 'Hello';
let newStr = str.toUpperCase(); // Tạo string mới
console.log(str); // 'Hello' (không đổi)
console.log(newStr); // 'HELLO'

let num: number = 10;
let doubled = num * 2; // Tạo number mới
console.log(num); // 10 (không đổi)
console.log(doubled); // 20

/**
 * 🔓 MUTABLE (Objects)
 * - Có thể thay đổi trực tiếp
 */
let arr: number[] = [1, 2, 3];
arr.push(4); // Modify array gốc
arr[0] = 10; // Modify phần tử
console.log(arr); // [10, 2, 3, 4] (đã thay đổi)

let obj: { name: string } = { name: 'John' };
obj.name = 'Jane'; // Modify object gốc
console.log(obj); // { name: 'Jane' }

/**
 * ✅ IMMUTABLE PATTERNS (Recommended)
 */
// Array - Tạo array mới thay vì mutate
const original = [1, 2, 3];
const added = [...original, 4]; // [1, 2, 3, 4]
const updated = original.map((x) => x * 2); // [2, 4, 6]
const filtered = original.filter((x) => x > 1); // [2, 3]

// Object - Tạo object mới
const user = { name: 'John', age: 25 };
const updatedUser = { ...user, age: 26 };
const withEmail = { ...user, email: 'john@example.com' };

// Object.freeze() - Làm object immutable
const frozen = Object.freeze({ x: 10 });
// frozen.x = 20; // ❌ Error in strict mode
```

### **4.2. Deep Copy vs Shallow Copy** 🎯

---

#### **📝 SHALLOW COPY (Sao Chép Nông)**

**💡 Định nghĩa:** Chỉ copy **cấp đầu tiên** (level 1), các nested objects/arrays vẫn **share reference** (dùng chung địa chỉ).

```typescript
/**
 * ════════════════════════════════════════════════════════════
 * 🔍 VÍ DỤ CỤ THỂ: Shallow Copy Object
 * ════════════════════════════════════════════════════════════
 */

const original = {
  name: 'John', // ← Primitive (string) - cấp 1
  age: 25, // ← Primitive (number) - cấp 1
  address: {
    // ← Object (nested) - cấp 2 ⚠️
    city: 'Ho Chi Minh',
    country: 'Vietnam',
  },
  hobbies: ['coding', 'reading'], // ← Array (nested) - cấp 2 ⚠️
};

/**
 * ┌────────────────────────────────────────────────────────┐
 * │ CÁCH 1: SPREAD OPERATOR {...obj}                      │
 * └────────────────────────────────────────────────────────┘
 * ✅ Ưu điểm: Ngắn gọn, modern syntax
 * ❌ Nhược điểm: Chỉ copy 1 tầng
 */
const shallow1 = { ...original };

/**
 * ┌────────────────────────────────────────────────────────┐
 * │ CÁCH 2: Object.assign({}, obj)                        │
 * └────────────────────────────────────────────────────────┘
 * ✅ Ưu điểm: Compatible với ES5+
 * ❌ Nhược điểm: Dài hơn spread
 */
const shallow2 = Object.assign({}, original);

/**
 * ┌────────────────────────────────────────────────────────┐
 * │ CÁCH 3: Array.slice() (CHỈ CHO ARRAYS)                │
 * └────────────────────────────────────────────────────────┘
 */
const arr = [1, 2, [3, 4]]; // Array với nested array
const shallowArr = arr.slice(); // Copy shallow

/**
 * ════════════════════════════════════════════════════════════
 * ⚠️ VẤN ĐỀ VỚI SHALLOW COPY: Nested Objects Bị Ảnh Hưởng!
 * ════════════════════════════════════════════════════════════
 */

// ✅ CẤP 1 (Primitives): OK - Tạo giá trị mới
shallow1.name = 'Jane';
shallow1.age = 30;

console.log(original.name); // 'John' ✅ KHÔNG đổi
console.log(shallow1.name); // 'Jane' ✅ Chỉ shallow1 đổi

// ❌ CẤP 2 (Nested Objects): NGUY HIỂM - Vẫn share reference!
shallow1.address.city = 'Ha Noi';
shallow1.hobbies.push('swimming');

console.log(original.address.city); // 'Ha Noi' ❌ ORIGINAL BỊ THAY ĐỔI!
console.log(original.hobbies); // ['coding', 'reading', 'swimming'] ❌

/**
 * 🔍 VISUALIZE MEMORY (Shallow Copy):
 *
 * ┌─────────────────────────────────────────────────────────┐
 * │                    STACK MEMORY                         │
 * ├─────────────────────────────────────────────────────────┤
 * │ original    →  { name: 'John', address: → [Heap #1] }  │
 * │ shallow1    →  { name: 'Jane', address: → [Heap #1] }  │ ← Cùng trỏ đến Heap #1
 * └─────────────────────────────────────────────────────────┘
 *
 * ┌─────────────────────────────────────────────────────────┐
 * │                    HEAP MEMORY                          │
 * ├─────────────────────────────────────────────────────────┤
 * │ [Heap #1]: { city: 'Ha Noi', country: 'Vietnam' }      │ ← Cả 2 dùng chung!
 * └─────────────────────────────────────────────────────────┘
 *
 * 💡 KẾT LUẬN:
 * - name, age (primitives) → Copy riêng biệt ✅
 * - address (object) → Share reference ❌
 */
```

---

#### **🔍 DEEP COPY (Sao Chép Sâu)**

**💡 Định nghĩa:** Copy **TOÀN BỘ** tất cả cấp (nested objects/arrays cũng được clone), tạo object **hoàn toàn độc lập**.

```typescript
/**
 * ════════════════════════════════════════════════════════════
 * ✅ CÁCH 1: structuredClone() (MODERN - KHUYẾN NGHỊ ⭐⭐⭐⭐⭐)
 * ════════════════════════════════════════════════════════════
 *
 * 📅 Browser support: Chrome 98+, Firefox 94+, Safari 15.4+
 * ✅ Ưu điểm:
 *    - Native API (không cần library)
 *    - Copy được: Date, Map, Set, RegExp, ArrayBuffer, TypedArrays
 *    - Xử lý circular references (tham chiếu vòng)
 * ❌ Nhược điểm:
 *    - KHÔNG copy functions
 *    - KHÔNG copy symbols
 *    - KHÔNG copy prototype chain
 */

const original = {
  name: 'John',
  address: {
    city: 'Ho Chi Minh',
    coords: { lat: 10.8, lng: 106.6 }, // Nested level 3
  },
  hobbies: ['coding', 'reading'],
  birthDate: new Date('1990-01-01'), // ✅ Date được copy đúng
};

const deep1 = structuredClone(original);

// Test: Thay đổi nested object level 3
deep1.address.coords.lat = 21.0; // Ha Noi latitude

console.log(original.address.coords.lat); // 10.8 ✅ KHÔNG đổi!
console.log(deep1.address.coords.lat); // 21.0 ✅ Chỉ deep1 đổi

/**
 * ════════════════════════════════════════════════════════════
 * ⚠️ CÁCH 2: JSON.parse(JSON.stringify()) (CÓ GIỚI HẠN)
 * ════════════════════════════════════════════════════════════
 *
 * ✅ Ưu điểm:
 *    - Đơn giản, 1 dòng code
 *    - Compatible mọi browser
 * ❌ Nhược điểm (MẤT DỮ LIỆU):
 *    - KHÔNG copy functions → Biến thành undefined
 *    - KHÔNG copy undefined → Biến thành null
 *    - KHÔNG copy symbols → Bị bỏ qua
 *    - Date → Thành string (phải parse lại)
 *    - RegExp → Thành empty object {}
 *    - Infinity/NaN → Thành null
 *    - Circular references → Throw error
 */

const objectWithFunctions = {
  name: 'John',
  greet: function () {
    return 'Hi';
  }, // ❌ Function
  age: undefined, // ❌ undefined
  symbol: Symbol('id'), // ❌ Symbol
  date: new Date(), // ⚠️ → String
  regex: /test/g, // ❌ → {}
  special: NaN, // ❌ → null
  address: { city: 'HCM' }, // ✅ OK
};

const deep2 = JSON.parse(JSON.stringify(objectWithFunctions));

console.log(deep2);
/**
 * 📤 OUTPUT:
 * {
 *   name: 'John',
 *   // greet: BIẾN MẤT! ❌
 *   // age: BIẾN MẤT! (undefined bị skip) ❌
 *   // symbol: BIẾN MẤT! ❌
 *   date: '2024-01-15T10:30:00.000Z', // ⚠️ String, không phải Date
 *   regex: {},                         // ❌ Empty object
 *   special: null,                     // ❌ NaN → null
 *   address: { city: 'HCM' }           // ✅ OK
 * }
 *
 * 💡 KẾT LUẬN: Chỉ dùng JSON method cho PLAIN OBJECTS (không có functions/Date/RegExp)
 */

/**
 * ════════════════════════════════════════════════════════════
 * 🛠️ CÁCH 3: CUSTOM RECURSIVE FUNCTION (LINH HOẠT NHẤT)
 * ════════════════════════════════════════════════════════════
 *
 * ✅ Ưu điểm:
 *    - Copy được MỌI THỨ (functions, Date, RegExp...)
 *    - Tùy chỉnh logic theo nhu cầu
 *    - Xử lý circular references (nếu implement thêm)
 * ❌ Nhược điểm:
 *    - Phức tạp, dễ có bug
 *    - Performance chậm hơn native methods
 *    - Phải maintain code
 */

function deepClone<T>(obj: T, hash = new WeakMap()): T {
  // ────────────────────────────────────────────────────────
  // BƯỚC 1: Base cases - Trả về ngay nếu không phải object
  // ────────────────────────────────────────────────────────

  // 1.1. null hoặc primitive → Trả về ngay
  if (obj === null || typeof obj !== 'object') {
    return obj; // null, number, string, boolean, undefined
  }

  // 1.2. Check circular reference (tránh infinite loop)
  if (hash.has(obj)) {
    return hash.get(obj); // Đã clone rồi, trả về bản clone cũ
  }

  // ────────────────────────────────────────────────────────
  // BƯỚC 2: Special cases - Xử lý built-in objects
  // ────────────────────────────────────────────────────────

  // 2.1. Date → Tạo Date mới với cùng timestamp
  if (obj instanceof Date) {
    return new Date(obj.getTime()) as any;
  }

  // 2.2. RegExp → Tạo RegExp mới với cùng pattern + flags
  if (obj instanceof RegExp) {
    return new RegExp(obj.source, obj.flags) as any;
  }

  // 2.3. Array → Clone từng phần tử (recursive)
  if (obj instanceof Array) {
    const arrCopy: any[] = [];
    hash.set(obj, arrCopy); // Lưu vào hash trước khi recursive

    obj.forEach((item, index) => {
      arrCopy[index] = deepClone(item, hash); // Recursive cho mỗi item
    });

    return arrCopy as any;
  }

  // 2.4. Map → Clone Map
  if (obj instanceof Map) {
    const mapCopy = new Map();
    hash.set(obj, mapCopy);

    obj.forEach((value, key) => {
      mapCopy.set(key, deepClone(value, hash));
    });

    return mapCopy as any;
  }

  // 2.5. Set → Clone Set
  if (obj instanceof Set) {
    const setCopy = new Set();
    hash.set(obj, setCopy);

    obj.forEach((value) => {
      setCopy.add(deepClone(value, hash));
    });

    return setCopy as any;
  }

  // ────────────────────────────────────────────────────────
  // BƯỚC 3: Plain Object - Clone properties
  // ────────────────────────────────────────────────────────

  if (typeof obj === 'object') {
    const objCopy: any = {};
    hash.set(obj, objCopy); // Lưu vào hash

    // Clone tất cả properties (kể cả non-enumerable nếu cần)
    Object.keys(obj).forEach((key) => {
      objCopy[key] = deepClone((obj as any)[key], hash); // Recursive
    });

    return objCopy;
  }

  return obj;
}

// ────────────────────────────────────────────────────────
// 🧪 TEST CUSTOM DEEP CLONE
// ────────────────────────────────────────────────────────

const complexObject = {
  name: 'John',
  greet: function () {
    return 'Hi';
  }, // ✅ Function
  date: new Date('2024-01-01'), // ✅ Date
  regex: /test/gi, // ✅ RegExp
  nested: {
    deep: {
      value: 42,
    },
  },
  arr: [1, [2, 3]], // ✅ Nested array
  map: new Map([['key', 'value']]), // ✅ Map
  set: new Set([1, 2, 3]), // ✅ Set
};

const cloned = deepClone(complexObject);

// Test 1: Function
console.log(cloned.greet()); // 'Hi' ✅

// Test 2: Date
console.log(cloned.date instanceof Date); // true ✅
cloned.date.setFullYear(2025);
console.log(complexObject.date.getFullYear()); // 2024 ✅ Không đổi

// Test 3: Nested object
cloned.nested.deep.value = 100;
console.log(complexObject.nested.deep.value); // 42 ✅ Không đổi

/**
 * ════════════════════════════════════════════════════════════
 * 📦 CÁCH 4: LODASH _.cloneDeep() (PRODUCTION-READY ⭐⭐⭐⭐⭐)
 * ════════════════════════════════════════════════════════════
 *
 * ✅ Ưu điểm:
 *    - Đã được test kỹ (millions of downloads)
 *    - Xử lý mọi edge cases
 *    - Performance tốt (optimized)
 *    - Copy được: functions, Date, RegExp, Map, Set, Buffer...
 *    - Xử lý circular references
 * ❌ Nhược điểm:
 *    - Cần install library (~24KB minified)
 *    - Overkill cho simple cases
 *
 * 📦 Install: npm install lodash
 */

import _ from 'lodash';

const deep3 = _.cloneDeep(complexObject);

// Test circular reference
const circular: any = { a: 1 };
circular.self = circular; // Tham chiếu vòng

const clonedCircular = _.cloneDeep(circular);
console.log(clonedCircular.self === clonedCircular); // true ✅
console.log(clonedCircular === circular); // false ✅
```

---

#### **📊 SO SÁNH CHI TIẾT: SHALLOW vs DEEP COPY**

```typescript
/**
 * ════════════════════════════════════════════════════════════════════════════
 * COMPARISON TABLE - Chọn Method Nào?
 * ════════════════════════════════════════════════════════════════════════════
 *
 * ┌─────────────────┬──────────┬──────────┬────────────┬──────────┬───────────┐
 * │ Method          │ Nested?  │ Functions│ Date/RegExp│ Circular │Performance│
 * ├─────────────────┼──────────┼──────────┼────────────┼──────────┼───────────┤
 * │ {...obj}        │ ❌       │ ✅       │ ⚠️ Ref     │ N/A      │ ⚡⚡⚡⚡   │
 * │ Object.assign   │ ❌       │ ✅       │ ⚠️ Ref     │ N/A      │ ⚡⚡⚡⚡   │
 * │ JSON            │ ✅       │ ❌ Lost  │ ❌ String  │ ❌ Error │ ⚡⚡⚡     │
 * │ structuredClone │ ✅       │ ❌ Lost  │ ✅ Clone   │ ✅       │ ⚡⚡⚡     │
 * │ Custom function │ ✅       │ ✅       │ ✅ Clone   │ ✅*      │ ⚡⚡       │
 * │ Lodash          │ ✅       │ ✅       │ ✅ Clone   │ ✅       │ ⚡⚡⚡     │
 * └─────────────────┴──────────┴──────────┴────────────┴──────────┴───────────┘
 *
 * * Custom function cần implement thêm logic xử lý circular refs
 *
 * ════════════════════════════════════════════════════════════════════════════
 * 🎯 DECISION TREE - Khi Nào Dùng Gì?
 * ════════════════════════════════════════════════════════════════════════════
 *
 *                    Cần clone object?
 *                           │
 *          ┌────────────────┴────────────────┐
 *          │                                 │
 *     Có nested?                         Không nested?
 *          │                                 │
 *    ┌─────┴─────┐                          ✅ Spread {...obj}
 *    │           │                          ✅ Object.assign()
 * Có Date/      Chỉ plain                  → Nhanh nhất!
 * RegExp/       objects?
 * Function?         │
 *    │              │
 *    │              ✅ JSON.parse(JSON.stringify())
 *    │              → Đơn giản, plain objects
 *    │
 * ┌──┴──┐
 * │     │
 * Modern  Production?
 * browser?    │
 *    │        │
 *    ✅       ✅ Lodash _.cloneDeep()
 * structuredClone()  → Battle-tested, full features
 * → Native, fast
 *
 * ════════════════════════════════════════════════════════════════════════════
 */
```

---

#### **🎓 REAL-WORLD EXAMPLES (Ví Dụ Thực Tế)**

```typescript
/**
 * ════════════════════════════════════════════════════════════
 * 📘 CASE 1: React State Update (Immutable Pattern)
 * ════════════════════════════════════════════════════════════
 */

interface User {
  id: number;
  name: string;
  settings: {
    theme: string;
    notifications: boolean;
  };
}

// ❌ WRONG: Mutate state
function updateThemeWrong(user: User, newTheme: string) {
  user.settings.theme = newTheme; // ❌ Mutate!
  return user;
}

// ✅ CORRECT: Shallow copy (đủ cho case này)
function updateThemeShallow(user: User, newTheme: string): User {
  return {
    ...user, // Copy level 1
    settings: {
      // ⚠️ Phải copy manual nested object
      ...user.settings,
      theme: newTheme,
    },
  };
}

// ✅ BETTER: Deep copy (an toàn hơn)
function updateThemeDeep(user: User, newTheme: string): User {
  const clonedUser = structuredClone(user); // Deep clone
  clonedUser.settings.theme = newTheme;
  return clonedUser;
}

/**
 * ════════════════════════════════════════════════════════════
 * 📘 CASE 2: Redux/Zustand Store Update
 * ════════════════════════════════════════════════════════════
 */

interface StoreState {
  users: User[];
  currentUser: User | null;
}

// ❌ WRONG: Mutate array
function addUserWrong(state: StoreState, newUser: User) {
  state.users.push(newUser); // ❌ Mutate!
  return state;
}

// ✅ CORRECT: Immutable update
function addUserCorrect(state: StoreState, newUser: User): StoreState {
  return {
    ...state,
    users: [...state.users, newUser], // ✅ Tạo array mới
  };
}

/**
 * ════════════════════════════════════════════════════════════
 * 📘 CASE 3: API Response Clone (Avoid Side Effects)
 * ════════════════════════════════════════════════════════════
 */

interface ApiResponse {
  data: {
    items: Array<{ id: number; name: string }>;
    metadata: {
      total: number;
      page: number;
    };
  };
}

async function fetchData(): Promise<ApiResponse> {
  const response = await fetch('/api/data');
  const original = await response.json();

  // ✅ Clone để tránh cache bị mutate
  return structuredClone(original);
}

// Usage
const data1 = await fetchData();
const data2 = data1; // ❌ Share reference!

data2.data.items[0].name = 'Modified'; // ❌ data1 cũng bị đổi!

// ✅ CORRECT:
const data3 = structuredClone(data1); // Deep clone
data3.data.items[0].name = 'Modified'; // ✅ data1 không đổi

/**
 * ════════════════════════════════════════════════════════════
 * 📘 CASE 4: Form Data Clone (với Date objects)
 * ════════════════════════════════════════════════════════════
 */

interface FormData {
  name: string;
  birthDate: Date;
  address: {
    street: string;
    city: string;
  };
}

const originalForm: FormData = {
  name: 'John',
  birthDate: new Date('1990-01-01'),
  address: {
    street: '123 Main St',
    city: 'HCM',
  },
};

// ❌ WRONG: JSON method (Date → string)
const wrongClone = JSON.parse(JSON.stringify(originalForm));
console.log(wrongClone.birthDate instanceof Date); // false ❌

// ✅ CORRECT: structuredClone (Date preserved)
const correctClone = structuredClone(originalForm);
console.log(correctClone.birthDate instanceof Date); // true ✅
correctClone.birthDate.setFullYear(2000);
console.log(originalForm.birthDate.getFullYear()); // 1990 ✅ Không đổi
```

---

#### **🚨 COMMON MISTAKES (Lỗi Thường Gặp)**

```typescript
/**
 * ════════════════════════════════════════════════════════════
 * ❌ MISTAKE 1: Nghĩ spread operator là deep copy
 * ════════════════════════════════════════════════════════════
 */

const user = {
  name: 'John',
  friends: ['Alice', 'Bob'],
};

const copy = { ...user }; // ⚠️ Shallow copy!
copy.friends.push('Charlie');

console.log(user.friends); // ['Alice', 'Bob', 'Charlie'] ❌ Bị đổi!

// ✅ FIX: Deep copy nested array
const correctCopy = {
  ...user,
  friends: [...user.friends], // Clone array riêng
};

/**
 * ════════════════════════════════════════════════════════════
 * ❌ MISTAKE 2: Dùng JSON cho objects có functions
 * ════════════════════════════════════════════════════════════
 */

const obj = {
  name: 'John',
  greet() {
    return 'Hi';
  },
};

const copy2 = JSON.parse(JSON.stringify(obj));
console.log(copy2.greet); // undefined ❌ Function bị mất!

// ✅ FIX: Dùng structuredClone hoặc Lodash
const correctCopy2 = _.cloneDeep(obj);
console.log(correctCopy2.greet()); // 'Hi' ✅

/**
 * ════════════════════════════════════════════════════════════
 * ❌ MISTAKE 3: Quên clone khi pass vào function
 * ════════════════════════════════════════════════════════════
 */

function processData(data: any[]) {
  data.sort(); // ❌ Mutate array gốc!
  return data;
}

const numbers = [3, 1, 2];
const sorted = processData(numbers);
console.log(numbers); // [1, 2, 3] ❌ Bị sort!

// ✅ FIX: Clone trước khi modify
function processDataCorrect(data: any[]) {
  const copy = [...data]; // Shallow copy (đủ cho array 1 tầng)
  copy.sort();
  return copy;
}

const numbers2 = [3, 1, 2];
const sorted2 = processDataCorrect(numbers2);
console.log(numbers2); // [3, 1, 2] ✅ Không đổi
```

---

#### **💡 BEST PRACTICES SUMMARY**

```typescript
/**
 * ✅ DO:
 *
 * 1. Dùng structuredClone() cho deep copy objects hiện đại
 * 2. Dùng spread {...obj} cho shallow copy objects đơn giản
 * 3. Dùng Lodash _.cloneDeep() trong production (battle-tested)
 * 4. Luôn clone trước khi mutate trong React/Redux
 * 5. Clone nested arrays/objects riêng khi dùng spread
 *
 * ❌ DON'T:
 *
 * 1. KHÔNG dùng JSON cho objects có Date/RegExp/Functions
 * 2. KHÔNG nghĩ spread operator là deep copy
 * 3. KHÔNG mutate objects trực tiếp trong React state
 * 4. KHÔNG quên clone khi pass objects vào functions
 * 5. KHÔNG dùng custom deep clone nếu không hiểu rõ edge cases
 */

/**
 * 🎯 CHEAT SHEET:
 *
 * Plain object, 1 tầng?          → {...obj}
 * Nested object, không có Date?  → JSON.parse(JSON.stringify())
 * Nested object, có Date/Map?    → structuredClone()
 * Production code?               → Lodash _.cloneDeep()
 * Custom types?                  → Custom recursive function
 * React state update?            → Spread + manual nested spread
 */
```

---

## **V. Type Checking Methods**

### **5.1. typeof (Primitives)**

```typescript
/**
 * ⚡ typeof - Nhanh nhưng có bugs
 */
console.log(typeof 42); // 'number' ✅
console.log(typeof 'hi'); // 'string' ✅
console.log(typeof true); // 'boolean' ✅
console.log(typeof undefined); // 'undefined' ✅
console.log(typeof Symbol('id')); // 'symbol' ✅
console.log(typeof 123n); // 'bigint' ✅
console.log(typeof function () {}); // 'function' ✅

/**
 * ⚠️ BUGS của typeof:
 */
console.log(typeof null); // 'object' ❌ (historical bug)
console.log(typeof []); // 'object' ❌ (không phân biệt array)
console.log(typeof NaN); // 'number' ❌ (NaN vẫn là number type)

/**
 * ✅ SAFE typeof helper:
 */
function safeTypeOf(value: any): string {
  if (value === null) return 'null';
  if (Array.isArray(value)) return 'array';
  return typeof value;
}

console.log(safeTypeOf(null)); // 'null' ✅
console.log(safeTypeOf([])); // 'array' ✅
```

### **5.2. Advanced Type Checking**

```typescript
/**
 * ✅ Array.isArray() - Best cho array
 */
console.log(Array.isArray([])); // true
console.log(Array.isArray([1, 2, 3])); // true
console.log(Array.isArray('not array')); // false

/**
 * ✅ Number.isNaN() - Không coerce (tốt hơn isNaN)
 */
console.log(Number.isNaN(NaN)); // true ✅
console.log(Number.isNaN('hello')); // false ✅

// ⚠️ isNaN() global - Có coercion
console.log(isNaN('hello')); // true ❌ (coerce thành NaN)

/**
 * ✅ Number.isFinite() - Check số hợp lệ
 */
console.log(Number.isFinite(42)); // true
console.log(Number.isFinite(Infinity)); // false
console.log(Number.isFinite(NaN)); // false

/**
 * ✅ Object.prototype.toString.call() - CHÍNH XÁC NHẤT
 */
function getType(value: any): string {
  return Object.prototype.toString.call(value).slice(8, -1).toLowerCase();
}

console.log(getType(null)); // 'null' ✅
console.log(getType([])); // 'array' ✅
console.log(getType(new Date())); // 'date' ✅
console.log(getType(/regex/)); // 'regexp' ✅
console.log(getType(new Map())); // 'map' ✅

/**
 * ✅ instanceof - Check prototype chain
 */
class Person {}
const p = new Person();

console.log(p instanceof Person); // true
console.log([] instanceof Array); // true
console.log({} instanceof Object); // true

// ⚠️ Không work với primitives:
console.log('hi' instanceof String); // false
console.log(42 instanceof Number); // false

/**
 * 🎯 COMPLETE TYPE CHECKER
 */
class TypeChecker {
  static isPrimitive(value: any): boolean {
    return value !== Object(value);
  }

  static isObject(value: any): boolean {
    return value !== null && typeof value === 'object' && !Array.isArray(value);
  }

  static isEmptyObject(value: any): boolean {
    return this.isObject(value) && Object.keys(value).length === 0;
  }

  static isEmptyArray(value: any): boolean {
    return Array.isArray(value) && value.length === 0;
  }

  static isNullOrUndefined(value: any): boolean {
    return value == null; // Check cả null VÀ undefined
  }

  static isValidNumber(value: any): boolean {
    return typeof value === 'number' && !isNaN(value) && isFinite(value);
  }
}

// Usage
console.log(TypeChecker.isPrimitive(42)); // true
console.log(TypeChecker.isObject({})); // true
console.log(TypeChecker.isEmptyObject({})); // true
console.log(TypeChecker.isValidNumber(NaN)); // false
console.log(TypeChecker.isNullOrUndefined(null)); // true
```

---

## **VI. Memory Management & GC**

### **6.1. Memory Lifecycle**

```typescript
/**
 * ═══════════════════════════════════════════════════════
 * MEMORY LIFECYCLE (Vòng đời bộ nhớ)
 * ═══════════════════════════════════════════════════════
 */

// BƯỚC 1: ALLOCATION (Cấp phát)
let user = { name: 'John', age: 30 };
// → JS tự động cấp phát memory cho object

// BƯỚC 2: USAGE (Sử dụng)
console.log(user.name); // Đọc/ghi memory

// BƯỚC 3: RELEASE (Giải phóng)
user = null; // Xóa reference
// → GC sẽ tự động thu hồi memory
```

### **6.2. Garbage Collection Algorithm**

```typescript
/**
 * 🧠 MARK & SWEEP ALGORITHM
 *
 * BƯỚC 1: MARK (Đánh dấu)
 * - Bắt đầu từ GC roots (global, stack)
 * - Traverse tất cả references
 * - Đánh dấu objects còn accessible
 *
 * BƯỚC 2: SWEEP (Quét)
 * - Duyệt heap memory
 * - Xóa objects không được mark
 * - Thu hồi memory
 */

// Example: GC roots
let globalVar = { x: 1 }; // Global scope = GC root
function example() {
  let local = { y: 2 }; // Stack = GC root
  return local;
}

// Khi function return và không còn reference → GC xóa local
```

### **6.3. Memory Leaks - 10 Trường Hợp**

```typescript
/**
 * ═══════════════════════════════════════════════════════
 * 1️⃣ EVENT LISTENERS không cleanup ⭐⭐⭐⭐⭐
 * ═══════════════════════════════════════════════════════
 */

// ❌ MEMORY LEAK
class BadComponent {
  private element: HTMLElement;

  constructor(el: HTMLElement) {
    this.element = el;
    // bind() tạo function mới → không remove được!
    this.element.addEventListener('click', this.handleClick.bind(this));
  }

  handleClick() {
    console.log('Clicked');
  }

  destroy() {
    // ❌ Không remove được vì bind() tạo function mới!
    this.element.removeEventListener('click', this.handleClick.bind(this));
  }
}

// ✅ FIXED - Lưu bound function
class GoodComponent {
  private element: HTMLElement;
  private boundHandler: () => void;

  constructor(el: HTMLElement) {
    this.element = el;
    this.boundHandler = this.handleClick.bind(this);
    this.element.addEventListener('click', this.boundHandler);
  }

  handleClick() {
    console.log('Clicked');
  }

  destroy() {
    this.element.removeEventListener('click', this.boundHandler); // ✅
  }
}

// ✅ MODERN - AbortController
class ModernComponent {
  private element: HTMLElement;
  private abortController = new AbortController();

  constructor(el: HTMLElement) {
    this.element = el;
    this.element.addEventListener('click', this.handleClick, {
      signal: this.abortController.signal,
    });
  }

  handleClick() {
    console.log('Clicked');
  }

  destroy() {
    this.abortController.abort(); // ✅ Auto remove tất cả listeners
  }
}

/**
 * ═══════════════════════════════════════════════════════
 * 2️⃣ TIMERS không clear ⭐⭐⭐⭐⭐
 * ═══════════════════════════════════════════════════════
 */

// ❌ MEMORY LEAK
class BadTimer {
  private intervalId?: number;

  start() {
    this.intervalId = window.setInterval(() => {
      console.log('Tick');
    }, 1000);
    // ❌ Không clear khi component destroy
  }
}

// ✅ FIXED
class GoodTimer {
  private intervalId?: number;

  start() {
    this.intervalId = window.setInterval(() => {
      console.log('Tick');
    }, 1000);
  }

  destroy() {
    if (this.intervalId) {
      clearInterval(this.intervalId); // ✅
    }
  }
}

/**
 * ═══════════════════════════════════════════════════════
 * 3️⃣ CLOSURES giữ large data ⭐⭐⭐⭐
 * ═══════════════════════════════════════════════════════
 */

// ❌ MEMORY LEAK
function createLeak() {
  const largeData = new Array(1000000).fill('data'); // 8MB

  return function () {
    console.log('Hello');
    // ❌ largeData nằm trong scope → không được GC!
  };
}

// ✅ FIXED - Nullify unused variables
function createFixed() {
  let largeData: any[] | null = new Array(1000000).fill('data');

  const result = largeData.length; // Lấy giá trị cần
  largeData = null; // ✅ Clear reference

  return function () {
    console.log(result); // Chỉ giữ result, không giữ largeData
  };
}

/**
 * ═══════════════════════════════════════════════════════
 * 4️⃣ DOM REFERENCES ⭐⭐⭐⭐⭐
 * ═══════════════════════════════════════════════════════
 */

// ❌ MEMORY LEAK
const elements: HTMLElement[] = [];

function addElement() {
  const div = document.createElement('div');
  document.body.appendChild(div);
  elements.push(div); // ❌ Giữ reference
}

function removeElement() {
  const div = elements[0];
  document.body.removeChild(div);
  // ❌ elements vẫn giữ reference → div không được GC!
}

// ✅ FIXED
function removeElementFixed() {
  const div = elements.shift(); // ✅ Remove từ array
  if (div) {
    document.body.removeChild(div);
  }
}

/**
 * ═══════════════════════════════════════════════════════
 * 5️⃣ GLOBAL VARIABLES ⭐⭐⭐
 * ═══════════════════════════════════════════════════════
 */

// ❌ MEMORY LEAK
var globalCache: any[] = []; // ❌ Global, không bao giờ GC

function addToCache(data: any) {
  globalCache.push(data); // ❌ Phình to mãi
}

// ✅ FIXED - LRU Cache
class LRUCache<K, V> {
  private cache = new Map<K, V>();
  private maxSize = 100;

  set(key: K, value: V) {
    if (this.cache.size >= this.maxSize) {
      const firstKey = this.cache.keys().next().value;
      this.cache.delete(firstKey); // ✅ Xóa cũ nhất
    }
    this.cache.set(key, value);
  }
}

/**
 * 📊 SUMMARY - Top 5 Leaks:
 *
 * 1. Event Listeners (⭐⭐⭐⭐⭐) - Dùng AbortController
 * 2. Timers (⭐⭐⭐⭐⭐) - Luôn clearInterval/clearTimeout
 * 3. Closures (⭐⭐⭐⭐) - Nullify unused vars
 * 4. DOM References (⭐⭐⭐⭐⭐) - Remove từ arrays/maps
 * 5. Global Variables (⭐⭐⭐) - Dùng LRU cache
 */
```

### **6.4. WeakMap & WeakSet**

```typescript
/**
 * 🔗 WEAK REFERENCES - Không ngăn GC
 */

// ❌ Normal Map - Strong reference
const normalMap = new Map();
let obj1 = { data: 'important' };

normalMap.set(obj1, 'metadata');
obj1 = null; // ❌ Object không được GC (normalMap giữ ref)

// ✅ WeakMap - Weak reference
const weakMap = new WeakMap();
let obj2 = { data: 'important' };

weakMap.set(obj2, 'metadata');
obj2 = null; // ✅ Object được GC ngay!

/**
 * 🎯 USE CASES:
 */

// 1. Cache with auto cleanup
const cache = new WeakMap<object, any>();

function expensiveOperation(obj: object) {
  if (cache.has(obj)) {
    return cache.get(obj); // Cache hit
  }

  const result = /* ... expensive computation ... */ {};
  cache.set(obj, result);
  return result;
}
// Khi obj được GC → cache entry tự động xóa ✅

// 2. Private data
const privateData = new WeakMap();

class User {
  constructor(name: string) {
    privateData.set(this, { ssn: '123-45-6789' });
  }

  getSSN() {
    return privateData.get(this).ssn;
  }
}
// Private data tự động cleanup khi instance GC
```

---

## **VII. Best Practices Summary**

### **7.1. Data Types**

```typescript
/**
 * ✅ DO:
 */
// 1. Dùng === thay vì == (trừ value == null)
if (value === 42) {
} // ✅
if (value == null) {
} // ✅ Check cả null & undefined

// 2. Dùng Array.isArray() để check array
if (Array.isArray(arr)) {
} // ✅

// 3. Dùng Number.isNaN() thay vì isNaN()
if (Number.isNaN(value)) {
} // ✅

// 4. Dùng typeof cho primitives
if (typeof value === 'string') {
} // ✅

// 5. Nullish coalescing (??) cho default values
const age = user?.age ?? 18; // ✅

/**
 * ❌ DON'T:
 */
// 1. Dùng == (loose equality)
if (value == 42) {
} // ❌

// 2. typeof null hoặc typeof []
if (typeof value === 'null') {
} // ❌ typeof null === 'object'
if (typeof arr === 'array') {
} // ❌ typeof [] === 'object'

// 3. isNaN() global
if (isNaN(value)) {
} // ❌ Coercion

// 4. instanceof cho primitives
if ('hi' instanceof String) {
} // ❌ false
```

### **7.2. Memory Management**

```typescript
/**
 * ✅ DO:
 */
// 1. Cleanup event listeners
element.removeEventListener('click', handler); // ✅

// 2. Clear timers
clearInterval(intervalId); // ✅
clearTimeout(timeoutId);   // ✅

// 3. Nullify large data in closures
let largeData: any[] | null = [...];
largeData = null; // ✅

// 4. Remove DOM references
elements.splice(index, 1); // ✅

// 5. Dùng WeakMap cho cache
const cache = new WeakMap(); // ✅

/**
 * ❌ DON'T:
 */
// 1. Bind trong addEventListener
el.addEventListener('click', fn.bind(this)); // ❌

// 2. Quên clear timers
setInterval(() => {}, 1000); // ❌

// 3. Giữ detached DOM nodes
const removed = document.getElementById('old');
document.body.removeChild(removed);
elements.push(removed); // ❌

// 4. Global variables vô hạn
var globalCache = []; // ❌
```

### **7.3. Immutability**

```typescript
/**
 * ✅ DO:
 */
// 1. Spread operator cho shallow copy
const copy = { ...original }; // ✅
const arrCopy = [...original]; // ✅

// 2. structuredClone() cho deep copy
const deep = structuredClone(original); // ✅

// 3. Immutable updates
const updated = { ...user, age: 26 }; // ✅
const added = [...arr, newItem]; // ✅

// 4. Array methods không mutate
const filtered = arr.filter((x) => x > 5); // ✅
const mapped = arr.map((x) => x * 2); // ✅

/**
 * ❌ DON'T:
 */
// 1. Mutate objects trực tiếp
user.age = 26; // ❌

// 2. Mutate arrays
arr.push(4); // ❌
arr[0] = 10; // ❌

// 3. JSON cho deep copy (mất functions)
const copy = JSON.parse(JSON.stringify(obj)); // ❌ Mất functions
```

---

## **📚 Quick Reference Card**

```typescript
/**
 * ┌──────────────────────────────────────────────────────────┐
 * │           JAVASCRIPT DATA TYPES CHEAT SHEET              │
 * ├──────────────────────────────────────────────────────────┤
 * │                                                          │
 * │  📌 8 TYPES:                                            │
 * │  • 7 Primitives: number, string, boolean, undefined,   │
 * │                  null, symbol, bigint                   │
 * │  • 1 Complex: object (array, function, date...)        │
 * │                                                          │
 * │  📌 8 FALSY: false, 0, -0, 0n, '', null, undefined, NaN│
 * │                                                          │
 * │  📌 COMPARISON:                                         │
 * │  • === (strict) - No coercion ✅                        │
 * │  • == (loose) - Coercion ❌ (chỉ dùng value == null)   │
 * │                                                          │
 * │  📌 TYPE CHECKING:                                      │
 * │  • typeof - Primitives (có bugs: null, array)          │
 * │  • Array.isArray() - Arrays ✅                          │
 * │  • Number.isNaN() - NaN ✅                              │
 * │  • instanceof - Objects (không dùng cho primitives)    │
 * │  • Object.prototype.toString.call() - Chính xác nhất  │
 * │                                                          │
 * │  📌 COPY:                                               │
 * │  • Shallow: {...obj}, [...arr], Object.assign()       │
 * │  • Deep: structuredClone(), lodash cloneDeep()         │
 * │                                                          │
 * │  📌 MEMORY:                                             │
 * │  • Cleanup: removeEventListener, clearInterval         │
 * │  • WeakMap/WeakSet: Auto GC                            │
 * │  • Nullify: largeData = null                           │
 * │                                                          │
 * └──────────────────────────────────────────────────────────┘
 */
```

---

**Happy Learning! 🚀**

> "Understanding data types and memory is fundamental to writing performant JavaScript code."
