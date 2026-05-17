# Topic13: Advanced Array/Object Methods, Object Concepts & Immutability

## ⭐ Senior/Staff Summary

> Array/Object APIs không chỉ để viết code ngắn hơn. Ở frontend lớn, chúng ảnh hưởng trực tiếp tới **data transformation**, **React rendering**, **immutability**, **reference equality**, và **performance**.

### 🔑 Key Mental Model

| Nhóm | Ý chính | Senior takeaway |
|---|---|---|
| 🔁 Array methods | Transform/search/group data | Chọn method theo intent, tránh chain quá đắt trong hot path |
| 🧱 Object methods | Inspect/merge/transform object | Hiểu own property, enumerable, shallow copy |
| 🧬 Object concepts | Prototype, descriptor, ownership | Biết cơ chế thấp hơn để debug/library code |
| 🧊 Immutability | Copy đúng cấp thay đổi | React phụ thuộc reference equality, không deep compare |

> ✅ Rule of thumb: `map` để transform, `filter` để lọc, `find/some/every` để short-circuit, `reduce` để aggregate/index, `flatMap` để map rồi flatten một cấp, `Object.entries/fromEntries` để transform object rõ ràng.

---

## 1. 🔁 Advanced Array Methods

### Method Selection

| Method | Dùng khi | Tránh |
|---|---|---|
| `map` | Đổi từng item, giữ nguyên length | Dùng cho side effect |
| `filter` | Lọc item | `filter(...)[0]` khi chỉ cần 1 item |
| `find` | Tìm item đầu tiên | Loop hết array không cần thiết |
| `some` / `every` | Check điều kiện có/đủ | `filter().length > 0` |
| `reduce` | Group, index, sum, derive object | Accumulator type mơ hồ |
| `flat(depth)` | Flatten nested array | Quên default `depth = 1` |
| `flatMap` | `map` + flatten 1 cấp | Dùng cho flatten sâu |
| `Array.from` | Convert iterable/array-like, tạo range | `new Array(n).map(...)` |

### Ví dụ dễ hiểu

```ts
type Order = {
  id: string;
  status: "paid" | "pending" | "cancelled";
  items: Array<{ sku: string; quantity: number }>;
};

const orders: Order[] = [
  { id: "o1", status: "paid", items: [{ sku: "A", quantity: 2 }] },
  { id: "o2", status: "pending", items: [{ sku: "B", quantity: 1 }] },
];

// ✅ flatMap: lấy line items của paid orders
const paidItems = orders.flatMap((order) =>
  order.status === "paid" ? order.items : []
);

// ✅ reduce: tạo lookup table cho O(1) access
const ordersById = orders.reduce<Record<string, Order>>((acc, order) => {
  acc[order.id] = order;
  return acc;
}, {});

// ✅ Array.from: tạo pagination range
const pages = Array.from({ length: 5 }, (_, index) => index + 1);
```

### ⚠️ Pitfalls

```ts
// ❌ map cho side effect: tạo array thừa, sai intent
orders.map((order) => console.log(order.id));

// ✅ side effect dùng for...of hoặc forEach
for (const order of orders) {
  console.log(order.id);
}

// ❌ filter()[0] loop hết array
const paid = orders.filter((order) => order.status === "paid")[0];

// ✅ find short-circuit
const firstPaid = orders.find((order) => order.status === "paid");

// ❌ flat default chỉ flatten 1 level
[1, [2, [3]]].flat(); // [1, 2, [3]]

// ✅ chọn depth theo data contract
[1, [2, [3]]].flat(2); // [1, 2, 3]
```

> 💡 Staff note: array chaining dễ đọc nhưng có thể tạo nhiều intermediate arrays. Nếu profiling chỉ ra bottleneck trong render/hot path, dùng một vòng `for...of` rõ ràng có thể tốt hơn.

---

## 2. 🧱 Advanced Object Methods

### Core APIs

| API | Dùng khi | Key point |
|---|---|---|
| `Object.keys(obj)` | Lấy own enumerable keys | Key luôn là string |
| `Object.values(obj)` | Chỉ cần values | Mất context key |
| `Object.entries(obj)` | Transform object | Hợp với `map/filter/reduce` |
| `Object.fromEntries(entries)` | Entries về object | Cặp tốt với `Object.entries` |
| `Object.assign(target, source)` | Shallow merge/copy | **Mutates target** |
| `{ ...obj }` | Shallow immutable copy | Không copy prototype/descriptors |
| `Object.hasOwn(obj, key)` | Check own property | An toàn hơn `obj.hasOwnProperty` |

### Transform object rõ ràng

```ts
type FeatureFlags = Record<string, boolean>;

const flags: FeatureFlags = {
  newCheckout: true,
  legacySearch: false,
  betaProfile: true,
};

// ✅ filter object bằng entries/fromEntries
const enabledFlags = Object.fromEntries(
  Object.entries(flags).filter(([, enabled]) => enabled)
) satisfies Record<string, boolean>;

// ✅ immutable shallow merge
const nextFlags = {
  ...flags,
  betaProfile: false,
};

// ⚠️ Object.assign mutate target
const sameRef = Object.assign(flags, { betaProfile: false });
sameRef === flags; // true
```

### Own property vs prototype chain

```ts
const config = Object.create({ inherited: true });
config.theme = "dark";

Object.keys(config); // ["theme"]
"inherited" in config; // true - có thể nằm trên prototype
Object.hasOwn(config, "inherited"); // false - chỉ own property
```

> ⚠️ Với object từ API/user input, dùng `Object.hasOwn(obj, key)`. Đừng gọi trực tiếp `obj.hasOwnProperty(...)` vì object có thể được tạo bằng `Object.create(null)` hoặc override method này.

---

## 3. 🧬 Object Concepts Cần Biết

### Prototype Chain

JavaScript inheritance dựa trên **prototype chain**. Khi đọc property, engine tìm trên object trước, sau đó đi lên prototype.

```ts
const userMethods = {
  displayName(this: { firstName: string; lastName: string }) {
    return `${this.firstName} ${this.lastName}`;
  },
};

const user = Object.create(userMethods) as {
  firstName: string;
  lastName: string;
  displayName(): string;
};

user.firstName = "Linh";
user.lastName = "Tran";

user.displayName(); // "Linh Tran"
Object.getPrototypeOf(user) === userMethods; // true
```

✅ Nên nhớ:

- Dùng `Object.getPrototypeOf(obj)`, tránh `obj.__proto__`.
- `Object.create(null)` tạo dictionary object không có `Object.prototype`.
- App hiện đại thường ưu tiên class/composition; prototype manipulation thủ công chủ yếu gặp trong library/internal code.

### Property Descriptors

Mỗi property có metadata: `writable`, `enumerable`, `configurable`, hoặc getter/setter.

```ts
const model = {};

Object.defineProperty(model, "id", {
  value: "u_123",
  writable: false,
  enumerable: true,
  configurable: false,
});

Object.keys(model); // ["id"]
Object.getOwnPropertyDescriptor(model, "id");
```

Use cases:

- Non-enumerable metadata.
- Read-only ID/config.
- Library/framework internals cần kiểm soát behavior.

---

## 4. 🧊 Immutability: Shallow, Deep, Structural Sharing

### `freeze`, `seal`, `preventExtensions`

| API | Add | Delete | Modify existing | Ghi nhớ |
|---|---:|---:|---:|---|
| `Object.preventExtensions` | ❌ | ✅ | ✅ | Chỉ chặn thêm key mới |
| `Object.seal` | ❌ | ❌ | ✅ | Vẫn sửa value nếu writable |
| `Object.freeze` | ❌ | ❌ | ❌ | **Shallow freeze** |

```ts
"use strict";

const frozen = Object.freeze({
  name: "Checkout",
  settings: { retry: 3 },
});

// frozen.name = "Cart"; // TypeError trong strict mode
frozen.settings.retry = 5; // ⚠️ vẫn đổi được vì freeze chỉ shallow
```

> 🔥 Key correction: `Object.freeze()` không phải deep immutable. Nested object vẫn mutable nếu chưa freeze riêng.

### Shallow copy vs Deep copy

```ts
const state = {
  user: { name: "An", address: { city: "HCM" } },
  theme: "light",
};

const nextState = {
  ...state,
  user: {
    ...state.user,
    name: "Binh",
  },
};

state === nextState; // false
state.user === nextState.user; // false
state.user.address === nextState.user.address; // true - structural sharing
```

Deep copy chỉ dùng khi thật sự cần:

- `structuredClone(value)`: copy sâu nhiều kiểu dữ liệu phổ biến, nhưng không phù hợp cho function/class instance.
- `JSON.parse(JSON.stringify(value))`: mất `Date`, `Map`, `Set`, `undefined`, `NaN`, method.
- Deep clone lớn tốn CPU/memory và phá **referential stability**.

---

## 5. ⚛️ React Implications

React chủ yếu dựa vào **reference equality**. State/props bị mutate tại chỗ có thể làm UI không update hoặc memo/cache sai.

```tsx
type Todo = { id: string; text: string; done: boolean };

// ✅ immutable update: chỉ item đổi có reference mới
function toggleTodo(todos: Todo[], id: string): Todo[] {
  return todos.map((todo) =>
    todo.id === id ? { ...todo, done: !todo.done } : todo
  );
}
```

```ts
// ❌ mutation: array reference không đổi
todos[0].done = true;
setTodos(todos);

// ✅ immutable: array mới, object cần đổi mới
setTodos((prev) =>
  prev.map((todo) =>
    todo.id === "t1" ? { ...todo, done: true } : todo
  )
);
```

### Khi nào dùng Immer?

Dùng **Immer** khi nested update dài và dễ sai:

```ts
import { produce } from "immer";

const next = produce(state, (draft) => {
  draft.user.address.city = "Da Nang";
});
```

> 💡 Immer giúp code mutation-style nhưng output vẫn immutable bằng structural sharing. Nếu state quá sâu và update thường xuyên, cân nhắc normalize data thay vì chỉ thêm Immer.

---

## 6. 🧭 Decision Guide

| Cần làm | Nên dùng |
|---|---|
| Transform list | `map` |
| Lọc list | `filter` |
| Tìm 1 item | `find` |
| Check tồn tại | `some` |
| Check tất cả | `every` |
| Group/index/sum | `reduce` |
| Flatten 1 cấp sau transform | `flatMap` |
| Transform object | `Object.entries` + `Object.fromEntries` |
| Merge immutable object | `{ ...obj, key: value }` |
| Check own key | `Object.hasOwn(obj, key)` |
| Nested React update | Copy đúng cấp hoặc Immer |
| Data lớn nhiều entity | Normalize: `{ ids, entities }` |

---

## 7. 🚫 Common Mistakes

```ts
// ❌ Copy root nhưng mutate nested
const next = { ...state };
next.user.name = "Changed"; // state.user cũng bị đổi

// ✅ Copy đến đúng cấp cần update
const safeNext = {
  ...state,
  user: { ...state.user, name: "Changed" },
};
```

```ts
// ❌ delete trực tiếp trên object state/config
delete config.obsoleteKey;

// ✅ immutable omit
const { obsoleteKey, ...cleanConfig } = config;
```

```ts
// ❌ mutate external object trong reduce
const external: Record<string, Order> = {};
orders.reduce((acc, order) => {
  acc[order.id] = order;
  return acc;
}, external);

// ✅ accumulator local, side effect không leak ra ngoài
const byId = orders.reduce<Record<string, Order>>((acc, order) => {
  acc[order.id] = order;
  return acc;
}, {});
```

---

## 8. ✅ Production Checklist

- ✅ Chọn array method theo intent: transform, filter, search, aggregate.
- ✅ Không mutate source data, props, React state.
- ✅ Biết copy hiện tại là shallow hay deep.
- ✅ Copy nested object/array đến đúng cấp cần update.
- ✅ React update tạo reference mới ở cấp React đang theo dõi.
- ✅ Object iteration chỉ lấy own properties khi cần.
- ✅ Không dùng `Object.assign` với target là object cần giữ immutable.
- ✅ Dùng structural sharing/Immer/normalized state thay vì deep clone bừa bãi.
- ✅ Chỉ tối ưu loop thủ công sau khi profiling.

---

## 9. 🎯 Short Interview Answer

> Advanced Array/Object methods giúp transform data rõ intent: `map/filter/find/reduce` cho pipeline cơ bản, `flat/flatMap` cho nested arrays, `Array.from` cho iterable/range, `Object.entries/fromEntries` cho object transformation. Điểm senior là hiểu tradeoff: các method này thường tạo array/object mới, tốt cho immutability và React reference equality, nhưng có thể tốn memory trong hot path.
>
> Với object concepts, JavaScript dùng prototype chain; cần biết `Object.create`, `Object.getPrototypeOf`, property descriptors, own property vs inherited property để debug đúng. Về immutability, spread, `Object.assign`, và `Object.freeze` đều quan trọng nhưng chủ yếu là shallow ở cấp object hiện tại. Trong React, update state nên copy đúng cấp thay đổi để tạo reference mới, giữ structural sharing cho phần không đổi, và dùng Immer hoặc normalized state khi nested update phức tạp.
