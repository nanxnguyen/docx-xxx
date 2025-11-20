# 🧪 Q8: Type Checking - Kiểm Tra Kiểu Dữ Liệu




**⚡ Quick Summary:**
> `typeof` nhanh nhưng có bugs (null, array). Dùng `Object.prototype.toString.call()` cho chính xác 100%

**💡 Ghi Nhớ:**
- ⚡ **typeof**: Nhanh, nhưng `typeof null === 'object'` ❌, `typeof [] === 'object'` ❌
- ✅ **Array.isArray()**: Best cho array check
- 🎯 **Number.isNaN()**: Không coerce (khác với `isNaN()`)
- 📦 **Object.prototype.toString.call()**: Chính xác nhất cho mọi type

**Trả lời:**

- **Khái niệm**: JavaScript có **7 primitive types** (number, string, boolean, undefined, null, symbol, bigint) và **1 complex type** (object). Kiểm tra đúng type là critical để tránh bugs.
- **Vấn đề với `typeof`**: Không chính xác 100% (typeof null === 'object', typeof [] === 'object', typeof NaN === 'number')
- **Kỹ thuật nâng cao**: `Object.prototype.toString.call()`, `Array.isArray()`, `instanceof`, Custom type guards
- **Ưu điểm**: Tránh runtime errors, type-safe code, dễ debug
- **Nhược điểm**: Cần biết edge cases của `typeof`, `instanceof` không work với primitives

**Tất Cả Kiểu Dữ Liệu Trong JavaScript:**

```
┌─────────────────────────────────────────────────────────────┐
│                   JAVASCRIPT DATA TYPES                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  🔹 PRIMITIVE TYPES (7 loại - Immutable)                    │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ 1. number      → 42, 3.14, NaN, Infinity             │  │
│  │ 2. string      → "hello", 'world', \`template\`      │  │
│  │ 3. boolean     → true, false                         │  │
│  │ 4. undefined   → undefined (chưa gán giá trị)        │  │
│  │ 5. null        → null (intentionally empty)          │  │
│  │ 6. symbol      → Symbol('id') (unique identifier)    │  │
│  │ 7. bigint      → 123456789n (số lớn hơn 2^53-1)     │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  🔸 COMPLEX TYPE (1 loại - Mutable)                         │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ 8. object      → {}, [], new Date(), new Map(), ...  │  │
│  │                                                       │  │
│  │    Subtypes:                                         │  │
│  │    • Plain Object    → { name: "John" }             │  │
│  │    • Array           → [1, 2, 3]                    │  │
│  │    • Function        → function() {}                │  │
│  │    • Date            → new Date()                   │  │
│  │    • RegExp          → /abc/g                       │  │
│  │    • Map/Set         → new Map(), new Set()         │  │
│  │    • Error           → new Error()                  │  │
│  │    • Promise         → new Promise()                │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

**Code Examples:**

```typescript
// 1. TYPEOF - Fast but có bugs
typeof 42 // 'number'
typeof 'hi' // 'string'
typeof true // 'boolean'
typeof null // 'object' ⚠️ BUG!
typeof [] // 'object' ⚠️ không phân biệt array
typeof NaN // 'number' ⚠️
typeof function(){} // 'function' ✅

// 2. Object.prototype.toString.call() - CHÍNH XÁC NHẤT
Object.prototype.toString.call(null) // '[object Null]' ✅
Object.prototype.toString.call([]) // '[object Array]' ✅
Object.prototype.toString.call(new Date()) // '[object Date]'

// 3. Helper function
function getType(v: any): string {
  return Object.prototype.toString.call(v).slice(8, -1).toLowerCase();
}
getType(null) // 'null' ✅
getType([]) // 'array' ✅
getType(NaN) // 'number'

// 4. Specific checks
Array.isArray([]) // true ✅ Best cho array
Number.isNaN(NaN) // true ✅ Không coerce (isNaN('hi') = true ❌)
Number.isFinite(42) // true ✅
Number.isInteger(42) // true
value === null // ✅ Strict check
value == null // ✅ Check cả null VÀ undefined

// 5. instanceof - Check prototype chain
class Person {}
const p = new Person()
p instanceof Person // true
[] instanceof Array // true
{} instanceof Object // true

// ⚠️ instanceof KHÔNG work với primitives:
'hi' instanceof String // false
42 instanceof Number // false

// 6. Safe conversion helpers
function safeNumber(v: any, def = 0): number {
  if (typeof v === 'number' && !isNaN(v)) return v;
  const n = Number(v);
  return !isNaN(n) ? n : def;
}

function safeBoolean(v: any, def = false): boolean {
  if (typeof v === 'boolean') return v;
  if (typeof v === 'string') {
    const s = v.toLowerCase();
    if (['true','1','yes'].includes(s)) return true;
    if (['false','0','no',''].includes(s)) return false;
  }
  return def;
}

// Usage
safeNumber('123') // 123
safeNumber('abc') // 0
safeBoolean('yes') // true
safeBoolean('no') // false
```

**✅ Summary:**
- `typeof`: Nhanh, dùng cho primitives (trừ null)
- `Object.prototype.toString.call()`: Chính xác nhất
- `Array.isArray()`: Best cho array
- `Number.isNaN()`: Best cho NaN
- `instanceof`: Dùng cho objects (không dùng cho primitives)


**Best Practices (Thực Hành Tốt):**

1. **✅ Dùng `Array.isArray()` để check array** (không dùng `typeof`)
2. **✅ Dùng `Number.isNaN()` thay vì `isNaN()`** (không coerce)
3. **✅ Dùng `Number.isFinite()` thay vì `isFinite()`** (không coerce)
4. **✅ Dùng `Object.prototype.toString.call()` cho chính xác nhất**
5. **✅ Dùng `===` thay vì `==`** (strict equality)
6. **✅ Tạo type guard functions** cho TypeScript type narrowing
7. **✅ Check `null` và `undefined` với `== null`** (check cả 2)

**Common Mistakes (Lỗi Thường Gặp):**

```typescript
// ❌ LỖI 1: Dùng typeof để check null
if (typeof value === 'null') { } // ❌ typeof null === 'object'

// ✅ ĐÚNG: Check trực tiếp
if (value === null) { } // ✅

// ❌ LỖI 2: Dùng typeof để check array
if (typeof arr === 'array') { } // ❌ typeof [] === 'object'

// ✅ ĐÚNG: Dùng Array.isArray
if (Array.isArray(arr)) { } // ✅

// ❌ LỖI 3: Dùng isNaN() thay vì Number.isNaN()
console.log(isNaN('hello')); // true - ❌ Coerce thành NaN

// ✅ ĐÚNG: Dùng Number.isNaN()
console.log(Number.isNaN('hello')); // false - ✅

// ❌ LỖI 4: Dùng instanceof với primitives
console.log('hello' instanceof String); // false - ❌

// ✅ ĐÚNG: Dùng typeof
console.log(typeof 'hello' === 'string'); // true - ✅

// ❌ LỖI 5: Quên check NaN trong số
function isValidNumber(value: any): boolean {
  return typeof value === 'number'; // ❌ NaN pass qua!
}

// ✅ ĐÚNG: Check cả NaN
function isValidNumber(value: any): boolean {
  return typeof value === 'number' && !isNaN(value); // ✅
}

// ❌ LỖI 6: Confuse null với undefined
let value = null;
console.log(typeof value === 'undefined'); // false - ❌

// ✅ ĐÚNG: Check đúng type
console.log(value === null); // true - ✅
console.log(value == null); // true - ✅ Check cả null và undefined

// ❌ LỖI 7: Check plain object không đúng
function isObject(value: any): boolean {
  return typeof value === 'object'; // ❌ null, array, date đều pass!
}

// ✅ ĐÚNG: Check plain object
function isPlainObject(value: any): boolean {
  return Object.prototype.toString.call(value) === '[object Object]';
}
```

**📊 So Sánh Các Phương Pháp:**

```
┌────────────────────────────┬─────────┬──────────┬──────────────┬──────────────┐
│ Phương Pháp                │ Speed   │ Accuracy │ Primitives   │ Objects      │
├────────────────────────────┼─────────┼──────────┼──────────────┼──────────────┤
│ typeof                     │ ⚡⚡⚡⚡⚡ │ ⭐⭐       │ ✅ (trừ null)│ ❌ (all 'obj')│
│ instanceof                 │ ⚡⚡⚡⚡   │ ⭐⭐⭐     │ ❌           │ ✅           │
│ Array.isArray()            │ ⚡⚡⚡⚡⚡ │ ⭐⭐⭐⭐⭐  │ N/A          │ ✅ (array)   │
│ Object.prototype.toString  │ ⚡⚡⚡⚡   │ ⭐⭐⭐⭐⭐  │ ✅           │ ✅           │
│ Number.isNaN()             │ ⚡⚡⚡⚡⚡ │ ⭐⭐⭐⭐⭐  │ ✅ (NaN)     │ N/A          │
│ Custom type guards         │ ⚡⚡⚡    │ ⭐⭐⭐⭐⭐  │ ✅           │ ✅           │
└────────────────────────────┴─────────┴──────────┴──────────────┴──────────────┘
```

**✅ Tổng Kết:**

- **typeof**: Nhanh nhưng có bug (null, array)
- **instanceof**: Tốt cho objects, không work với primitives
- **Array.isArray()**: Tốt nhất cho array
- **Number.isNaN()**: Tốt nhất cho NaN (không coerce)
- **Object.prototype.toString.call()**: Chính xác nhất cho mọi type
- **Custom type guards**: Tốt nhất cho TypeScript type narrowing

---

**🛡️ BONUS: Safe Type Conversion Helpers**

Khi làm việc với data từ API/user input, cần convert và validate data an toàn:

```typescript
// 1. Safe Number - Convert số an toàn
function safeNumber(value: any, defaultValue: number = 0): number {
  if (typeof value === 'number' && !isNaN(value) && isFinite(value)) return value;
  if (typeof value === 'string') {
    const parsed = Number(value.trim());
    if (!isNaN(parsed) && isFinite(parsed)) return parsed;
  }
  return defaultValue;
}

// Usage: safeNumber('123') → 123, safeNumber('abc') → 0

// 2. Safe String - Convert string an toàn
function safeString(value: any, defaultValue: string = ''): string {
  if (value == null) return defaultValue;
  if (typeof value === 'string') return value.trim();
  return String(value);
}

// Usage: safeString(null) → '', safeString(123) → '123'

// 3. Safe Boolean - Parse boolean từ nhiều format
function safeBoolean(value: any, defaultValue: boolean = false): boolean {
  if (value == null) return defaultValue;
  if (typeof value === 'boolean') return value;
  if (typeof value === 'number') return value === 1;
  if (typeof value === 'string') {
    const lower = value.toLowerCase().trim();
    if (['true', '1', 'yes', 'on'].includes(lower)) return true;
    if (['false', '0', 'no', 'off', ''].includes(lower)) return false;
  }
  return defaultValue;
}

// Usage: safeBoolean('yes') → true, safeBoolean('no') → false

// 4. Safe Array - Convert thành array
function safeArray<T>(value: any, defaultValue: T[] = []): T[] {
  if (Array.isArray(value)) return value;
  if (value == null) return defaultValue;
  if (value instanceof Set || value instanceof Map) return Array.from(value);
  if (typeof value === 'string') return value.split(',').map(s => s.trim()) as T[];
  return [value];
}

// Usage: safeArray('a,b,c') → ['a','b','c'], safeArray(null) → []

// 5. Safe Object - Convert thành object
function safeObject<T = any>(value: any, defaultValue: T = {} as T): T {
  if (value == null) return defaultValue;
  if (typeof value === 'object' && !Array.isArray(value)) return value;
  if (typeof value === 'string') {
    try { return JSON.parse(value); } catch { return defaultValue; }
  }
  return defaultValue;
}

// Usage: safeObject('{"a":1}') → {a:1}, safeObject(null) → {}

// Universal Safe Parser
const safe = {
  number: safeNumber,
  string: safeString,
  boolean: safeBoolean,
  array: safeArray,
  object: safeObject,
};

// Practical: Parse API Response
interface UserAPI { id: any; name: any; age: any; isActive: any; }
interface User { id: number; name: string; age: number; isActive: boolean; }

function parseUser(api: UserAPI): User {
  return {
    id: safe.number(api.id, 0),
    name: safe.string(api.name, 'Unknown'),
    age: safe.number(api.age, 0),
    isActive: safe.boolean(api.isActive, false),
  };
}
```

**Use Cases:** Parse API responses, validate user input, convert data formats, safe defaults
---
