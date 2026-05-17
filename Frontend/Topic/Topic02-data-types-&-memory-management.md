# 🎯 Topic02: Data Types & Memory Management

## ⭐ Senior/Staff Summary

> **Muốn viết JavaScript/Frontend chắc, phải hiểu 3 trục: value vs reference, equality/coercion, và object lifetime trong memory.**

- 📦 JavaScript có **8 kiểu dữ liệu**: 7 primitive + 1 object type.
- 🔒 **Primitive** immutable, copy theo value: `number`, `string`, `boolean`, `undefined`, `null`, `symbol`, `bigint`.
- 🔗 **Object/reference types** mutable, copy theo reference: object, array, function, Date, Map, Set...
- ⚠️ `typeof null === "object"` là bug legacy; `typeof [] === "object"` nên dùng `Array.isArray`.
- ✅ Ưu tiên `===`; chỉ dùng `value == null` khi muốn check cả `null` và `undefined`.
- 🧠 Shallow copy chỉ copy tầng đầu; nested object vẫn share reference.
- 🧬 Deep copy nên dùng `structuredClone` khi dữ liệu phù hợp; JSON clone có nhiều mất mát.
- ♻️ Memory được GC tự động bằng reachability/mark-and-sweep, nhưng leak vẫn xảy ra nếu còn reference.
- ⚛️ Trong React, reference equality quyết định render/memo; mutate state trực tiếp là nguồn bug lớn.

## 🧠 Key Mental Model

### 1. Primitive là value, object là reference

| Nhóm | Lưu/copy | Mutability | Ví dụ |
|---|---|---|---|
| Primitive | Copy giá trị | Immutable | `42`, `"hi"`, `true`, `null`, `undefined`, `Symbol()`, `123n` |
| Reference | Copy địa chỉ/reference | Mutable | `{}`, `[]`, `function`, `Date`, `Map`, `Set` |

```ts
let a = 10;
let b = a;
b = 20;

console.log(a); // 10

const user1 = { name: "An" };
const user2 = user1;
user2.name = "Binh";

console.log(user1.name); // "Binh" ⚠️ cùng reference
```

### 2. Stack/Heap là mental model, không phải spec chi tiết

- **Stack**: function calls, local bindings, primitive-like values trong mental model; nhanh, theo LIFO.
- **Heap**: objects/arrays/functions; GC quản lý lifetime.
- JS engine có tối ưu riêng, nhưng mental model này đủ để hiểu reference, mutation và leak.

### 3. React quan tâm reference equality

```tsx
// ❌ Mutate cùng reference -> React/memo có thể không nhận ra thay đổi đúng cách
user.settings.theme = "dark";
setUser(user);

// ✅ Tạo reference mới ở path thay đổi
setUser({
  ...user,
  settings: {
    ...user.settings,
    theme: "dark",
  },
});
```

💡 **Senior rule**: update immutable theo đúng depth cần thay đổi, đừng deep clone toàn bộ state lớn nếu chỉ đổi một field nhỏ.

## 📚 Main Concepts

### 📦 8 JavaScript data types

```ts
const num = 42; // number
const str = "hello"; // string
const bool = true; // boolean
const undef = undefined; // undefined
const empty = null; // null
const sym = Symbol("id"); // symbol
const big = 123456789n; // bigint

const obj = { name: "An" }; // object
const arr = [1, 2, 3]; // object subtype
const fn = () => {}; // function object
```

**Primitive types:**

- `number`: double-precision floating point, gồm `NaN`, `Infinity`, `-0`.
- `string`: immutable text.
- `boolean`: `true/false`.
- `undefined`: chưa gán hoặc property không tồn tại.
- `null`: cố ý rỗng.
- `symbol`: unique identifier.
- `bigint`: số nguyên lớn hơn giới hạn safe integer của `number`.

**Object type:**

- Plain object, array, function, Date, RegExp, Map, Set, WeakMap, WeakSet, Promise...

### ⚖️ Falsy vs Truthy

Chỉ có các giá trị này là falsy:

- `false`
- `0`
- `-0`
- `0n`
- `""`
- `null`
- `undefined`
- `NaN`

```ts
Boolean([]); // true ⚠️
Boolean({}); // true ⚠️
Boolean("0"); // true ⚠️
Boolean("false"); // true ⚠️
```

⚠️ Tránh dùng truthy/falsy khi `0` hoặc `""` là giá trị hợp lệ.

```ts
function getDisplayName(name: string | null | undefined) {
  return name ?? "Guest"; // chỉ fallback khi null/undefined
}

getDisplayName(""); // "" giữ nguyên
```

### 🔍 `==` vs `===`

```ts
5 === "5"; // false
5 == "5"; // true
0 == false; // true
"" == 0; // true
[] == 0; // true
null == undefined; // true
```

✅ Rule production:

- Dùng `===` mặc định.
- Dùng `value == null` nếu cố ý check cả `null` và `undefined`.
- Tránh `==` trong business logic vì coercion khó đọc.

```ts
function isEmpty(value: unknown) {
  return value == null; // true cho null hoặc undefined
}
```

### 🕳️ `null` vs `undefined`

| Value | Ý nghĩa | Nên dùng khi |
|---|---|---|
| `undefined` | chưa có value, optional/missing | optional param/property |
| `null` | cố ý không có value | API/domain muốn biểu diễn empty rõ |

```ts
type User = {
  id: string;
  email?: string; // có thể undefined
  deletedAt: Date | null; // cố ý chưa bị xóa
};
```

Pitfall:

```ts
typeof null; // "object" ⚠️
```

### 🧪 Type checking methods

| Method | Dùng cho | Pitfall |
|---|---|---|
| `typeof` | primitive/function | `typeof null` và `typeof []` đều `"object"` |
| `Array.isArray` | array | tốt nhất cho array |
| `instanceof` | class/prototype | không work với primitive; có vấn đề cross-realm |
| `Object.prototype.toString.call` | built-in object type | verbose nhưng chính xác hơn |
| `Number.isNaN` | check `NaN` | tốt hơn global `isNaN` vì không coerce |

```ts
function getType(value: unknown) {
  if (value === null) return "null";
  if (Array.isArray(value)) return "array";
  return typeof value;
}

Number.isNaN(NaN); // true
Number.isNaN("hello"); // false
isNaN("hello"); // true ⚠️ coercion
```

Advanced helper:

```ts
function getObjectTag(value: unknown) {
  return Object.prototype.toString.call(value).slice(8, -1).toLowerCase();
}

getObjectTag(new Date()); // "date"
getObjectTag(new Map()); // "map"
getObjectTag(/a/); // "regexp"
```

### 🔒 Immutable vs Mutable

Primitive immutable:

```ts
const text = "hello";
const upper = text.toUpperCase();

console.log(text); // "hello"
console.log(upper); // "HELLO"
```

Object/array mutable:

```ts
const items = [1, 2, 3];
items.push(4); // mutate original

const user = { name: "An" };
user.name = "Binh"; // mutate original
```

Immutable patterns:

```ts
const added = [...items, 5];
const updated = items.map((item) => item * 2);
const filtered = items.filter((item) => item > 1);

const updatedUser = {
  ...user,
  name: "Chi",
};
```

### 🧬 Shallow copy vs Deep copy

#### Shallow copy

Copy tầng đầu, nested object vẫn share reference.

```ts
const original = {
  name: "An",
  address: {
    city: "HCM",
  },
};

const copy = { ...original };
copy.name = "Binh";
copy.address.city = "Ha Noi";

console.log(original.name); // "An"
console.log(original.address.city); // "Ha Noi" ⚠️ nested bị đổi
```

Shallow copy methods:

- Object: `{ ...obj }`, `Object.assign({}, obj)`.
- Array: `[...arr]`, `arr.slice()`.

#### Deep copy

Copy cả nested objects/arrays.

```ts
const deep = structuredClone(original);
deep.address.city = "Da Nang";

console.log(original.address.city); // "Ha Noi"
```

So sánh nhanh:

| Method | Nested | Date/Map/Set | Function | Circular | Nên dùng |
|---|---|---|---|---|---|
| Spread/Object.assign | ❌ | share ref | share ref | N/A | object 1 tầng |
| JSON stringify/parse | ✅ plain only | ❌ mất type | ❌ mất | ❌ lỗi | plain data đơn giản |
| `structuredClone` | ✅ | ✅ | ❌ | ✅ | deep clone hiện đại |
| `_.cloneDeep` | ✅ | ✅ | thường giữ ref/function | ✅ | production edge cases |
| Custom clone | tùy | tùy | tùy | tùy | chỉ khi có nhu cầu đặc biệt |

⚠️ JSON clone mất dữ liệu:

```ts
const data = {
  date: new Date(),
  value: NaN,
  regex: /abc/g,
  greet() {
    return "hi";
  },
  empty: undefined,
};

JSON.parse(JSON.stringify(data));
// date -> string
// NaN -> null
// RegExp -> {}
// function/undefined -> bị bỏ
```

### 🧠 Pass by value / reference trong function

Primitive:

```ts
function increment(value: number) {
  value += 1;
  return value;
}

const x = 1;
increment(x);
console.log(x); // 1
```

Object:

```ts
function updateAge(user: { age: number }) {
  user.age += 1; // mutate object gốc
}

const user = { age: 20 };
updateAge(user);
console.log(user.age); // 21
```

Safe version:

```ts
function updateAgeImmutable(user: { age: number }) {
  return {
    ...user,
    age: user.age + 1,
  };
}
```

### ♻️ Memory lifecycle & Garbage Collection

Memory lifecycle:

```text
Allocate -> Use -> Release/Unreachable -> Garbage Collection
```

JS engine dùng reachability:

- Bắt đầu từ **GC roots**: global object, current call stack, closures còn reachable.
- Mark các object còn reachable.
- Sweep object không reachable.

```ts
let user: { name: string } | null = { name: "An" };

user = null;
// Nếu không còn reference khác, object có thể được GC
```

### 🧯 Common memory leaks

#### 1. Event listener không cleanup

```ts
class Component {
  private controller = new AbortController();

  constructor(private element: HTMLElement) {
    this.element.addEventListener("click", this.handleClick, {
      signal: this.controller.signal,
    });
  }

  handleClick = () => {
    console.log("clicked");
  };

  destroy() {
    this.controller.abort(); // ✅ auto remove listeners
  }
}
```

⚠️ Tránh:

```ts
el.addEventListener("click", handler.bind(this));
el.removeEventListener("click", handler.bind(this)); // ❌ function khác
```

#### 2. Timer không clear

```ts
const intervalId = window.setInterval(() => {
  console.log("tick");
}, 1000);

window.clearInterval(intervalId);
```

#### 3. Closure giữ large object

```ts
function createHandler() {
  let largeData: string[] | null = new Array(1_000_000).fill("data");

  const count = largeData.length;
  largeData = null; // ✅ không giữ array lớn

  return () => count;
}
```

#### 4. Detached DOM nodes

```ts
const nodes: HTMLElement[] = [];

function removeNode() {
  const node = nodes.pop();
  node?.remove(); // ✅ remove DOM + remove reference khỏi array
}
```

#### 5. Cache/global variables tăng mãi

```ts
class LRUCache<K, V> {
  private cache = new Map<K, V>();

  constructor(private maxSize = 100) {}

  set(key: K, value: V) {
    if (this.cache.size >= this.maxSize) {
      const firstKey = this.cache.keys().next().value;
      this.cache.delete(firstKey);
    }

    this.cache.set(key, value);
  }
}
```

### 🧷 WeakMap & WeakSet

`WeakMap`/`WeakSet` giữ weak reference, không ngăn key object bị GC.

```ts
const normalMap = new Map<object, string>();
let obj: object | null = {};

normalMap.set(obj, "metadata");
obj = null;
// object vẫn có thể bị giữ bởi normalMap
```

```ts
const weakMap = new WeakMap<object, string>();
let key: object | null = {};

weakMap.set(key, "metadata");
key = null;
// nếu không còn strong reference khác, object có thể GC
```

Use cases:

- Metadata cho object/DOM node.
- Cache theo object key.
- Private data cho instance.
- Tránh leak khi object lifecycle nằm ngoài quyền kiểm soát của mình.

## 🧪 Practical TypeScript/JavaScript Examples

### ✅ 1. React state update đúng reference

```tsx
type User = {
  id: string;
  name: string;
  settings: {
    theme: "light" | "dark";
    notifications: boolean;
  };
};

function updateTheme(user: User, theme: "light" | "dark"): User {
  return {
    ...user,
    settings: {
      ...user.settings,
      theme,
    },
  };
}
```

### ✅ 2. Array update immutable

```ts
type Todo = {
  id: string;
  title: string;
  done: boolean;
};

function toggleTodo(todos: Todo[], id: string) {
  return todos.map((todo) =>
    todo.id === id ? { ...todo, done: !todo.done } : todo
  );
}

function addTodo(todos: Todo[], title: string) {
  return [
    ...todos,
    {
      id: crypto.randomUUID(),
      title,
      done: false,
    },
  ];
}
```

### ✅ 3. Clone API response trước khi mutate local draft

```ts
type ApiResponse = {
  data: {
    items: Array<{ id: string; name: string }>;
    meta: { total: number };
  };
};

async function loadDraft(): Promise<ApiResponse> {
  const response = await fetch("/api/items");
  const data = (await response.json()) as ApiResponse;

  return structuredClone(data);
}
```

### ✅ 4. Type guard cho API data

```ts
type Product = {
  id: string;
  price: number;
};

function isProduct(value: unknown): value is Product {
  if (value === null || typeof value !== "object") return false;

  const item = value as Record<string, unknown>;

  return (
    typeof item.id === "string" &&
    typeof item.price === "number" &&
    Number.isFinite(item.price)
  );
}
```

### ✅ 5. WeakMap cache theo object key

```ts
const fullNameCache = new WeakMap<object, string>();

function getFullName(user: { firstName: string; lastName: string }) {
  if (fullNameCache.has(user)) {
    return fullNameCache.get(user);
  }

  const fullName = `${user.firstName} ${user.lastName}`;
  fullNameCache.set(user, fullName);
  return fullName;
}
```

## ⚛️ Production Notes / React Implications

### 🔁 Reference equality & rendering

React state, props, `memo`, `useMemo`, `useCallback`, Zustand selectors, Redux selectors đều phụ thuộc nhiều vào reference equality.

```tsx
const visibleItems = React.useMemo(
  () => items.filter((item) => item.visible),
  [items]
);
```

Nếu `items` bị mutate nhưng reference không đổi, memo/cache có thể stale.

### 🧱 Structural sharing

Thay vì deep clone toàn bộ state:

```ts
const nextState = {
  ...state,
  users: state.users.map((user) =>
    user.id === targetId
      ? {
          ...user,
          settings: {
            ...user.settings,
            theme: "dark",
          },
        }
      : user
  ),
};
```

Chỉ tạo object mới ở path thay đổi, giữ reference cũ cho phần không đổi. Đây là nền tảng của performance trong React/Redux.

### 🚀 Performance

- Primitive operations thường rẻ hơn object allocation, nhưng bottleneck thật thường là render, network, layout, algorithm.
- Deep clone object lớn trong render là anti-pattern.
- `structuredClone` tiện nhưng vẫn tốn CPU/memory với data lớn.
- Dùng profiler trước khi optimize.
- Normalize data lớn bằng `Map`/object để update nhanh hơn.

### 🧪 Testing/debugging

- Test immutable updates: object cũ không bị mutate.
- Freeze fixture trong test để bắt mutation.
- Dùng React DevTools/Profiler để xem re-render.
- Dùng browser Memory tab để tìm detached DOM nodes/listeners.

```ts
const frozenUser = Object.freeze({
  id: "u1",
  settings: Object.freeze({
    theme: "light",
  }),
});
```

## ⚠️ Common Pitfalls

- ❌ Nghĩ spread là deep copy.
- ❌ Mutate React state bằng `push`, `sort`, direct assignment.
- ❌ Dùng JSON clone cho object có `Date`, `Map`, `Set`, `RegExp`, `NaN`, `undefined`, function.
- ❌ So sánh object bằng `===` rồi kỳ vọng deep equality.
- ❌ Dùng `typeof null` hoặc `typeof []` để check type.
- ❌ Dùng global `isNaN` thay vì `Number.isNaN`.
- ❌ Dùng `||` default khiến `0`/`""` bị fallback sai.
- ❌ Quên cleanup event listener, timer, subscription.
- ❌ Closure giữ data lớn không cần thiết.
- ❌ Cache/global map tăng không giới hạn.

## ✅ Decision Guide / Checklist

**Type checking:**

- Primitive? -> `typeof`.
- Array? -> `Array.isArray`.
- `NaN`? -> `Number.isNaN`.
- Built-in object như Date/Map/RegExp? -> `Object.prototype.toString.call` hoặc `instanceof` nếu cùng realm.
- Runtime API data? -> viết type guard hoặc dùng schema validation.

**Copying:**

- Object/array 1 tầng -> spread/slice.
- Nested plain data đơn giản -> cân nhắc `structuredClone`.
- Có Date/Map/Set/circular -> `structuredClone`.
- Có function/prototype/custom class -> cần custom logic hoặc library.
- React state -> structural sharing, copy đúng path thay đổi.

**Memory:**

- Có listener/subscription/timer? -> cleanup.
- Có cache? -> giới hạn size hoặc dùng WeakMap nếu key là object.
- Có DOM node lưu trong array/map? -> remove reference khi remove DOM.
- Có closure giữ data lớn? -> chỉ giữ value cần thiết.
- Component unmount? -> abort request/cleanup effect.

## 🗣️ Short Interview Answer

Em nghĩ phần quan trọng nhất của data types trong JavaScript là phân biệt primitive và reference. Primitive như `number`, `string`, `boolean`, `null`, `undefined`, `symbol`, `bigint` là immutable và copy theo value. Còn object, array, function là reference type, copy biến chỉ copy địa chỉ nên mutate qua một biến có thể ảnh hưởng biến khác.

Theo em, trong frontend production, lỗi hay gặp nhất là mutation và equality. Em thường dùng `===`, chỉ dùng `value == null` khi muốn check cả `null` và `undefined`. Với object/array state trong React, em update immutable bằng spread/map/filter và structural sharing để React nhận ra reference mới, thay vì mutate trực tiếp.

Về memory, JavaScript có garbage collector nhưng không có nghĩa là không leak. Nếu còn reference từ event listener, timer, closure, global cache hoặc detached DOM node thì object vẫn không được thu hồi. Em thường cleanup trong effect, dùng `AbortController`, clear timer, giới hạn cache và dùng `WeakMap` khi cần metadata/cache theo object key.

## 🧠 Ghi nhớ nhanh

- **8 types**: 7 primitive + object.
- **Primitive**: immutable, copy value.
- **Object/Array/Function**: mutable, copy reference.
- **Falsy**: `false`, `0`, `-0`, `0n`, `""`, `null`, `undefined`, `NaN`.
- **Dùng `===`**, ngoại lệ phổ biến: `value == null`.
- **`typeof null` là `"object"`**, array cũng là object.
- **Spread là shallow copy**, không phải deep copy.
- **`structuredClone` deep clone tốt**, nhưng không clone function/symbol/prototype.
- **React cần reference mới** để update/memo đúng.
- **GC dựa trên reachability**, còn reference là còn sống.
- **WeakMap/WeakSet** không ngăn object key bị GC.

## 📖 Giải thích các thuật ngữ trong topic

| Thuật ngữ | Giải thích ngắn |
|---|---|
| Primitive | Kiểu dữ liệu nguyên thủy, immutable, copy theo value |
| Reference type | Object/array/function được truy cập qua reference |
| Stack | Vùng nhớ cho call stack/local bindings trong mental model |
| Heap | Vùng nhớ chứa objects/functions/arrays |
| Mutability | Khả năng thay đổi dữ liệu sau khi tạo |
| Immutability | Không thay đổi dữ liệu gốc, tạo value/object mới |
| Shallow copy | Copy tầng đầu, nested object vẫn share reference |
| Deep copy | Copy toàn bộ nested structure |
| `structuredClone` | API native để deep clone nhiều loại dữ liệu hiện đại |
| Type coercion | JS tự chuyển kiểu khi so sánh/tính toán |
| Falsy | Giá trị bị xem là false trong boolean context |
| Truthy | Giá trị bị xem là true trong boolean context |
| `typeof` | Operator kiểm tra type cơ bản |
| `instanceof` | Kiểm tra prototype chain |
| `NaN` | Not-a-Number, vẫn thuộc type `number` |
| `Object.is` | So sánh giống strict hơn cho case `NaN` và `-0` |
| Garbage Collection | Cơ chế tự thu hồi memory không còn reachable |
| GC root | Điểm bắt đầu để GC tìm object còn sống |
| Mark-and-sweep | Thuật toán đánh dấu object reachable rồi quét object chết |
| Memory leak | Object không còn cần nhưng vẫn còn reference nên không được GC |
| WeakMap | Map có key là weak reference, không ngăn GC |
| WeakSet | Set giữ weak reference đến object |
| Structural sharing | Chỉ tạo object mới ở phần thay đổi, giữ reference cũ cho phần không đổi |
