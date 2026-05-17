# 🚀 Topic 05 — ES5 vs ES6+ Features (so sánh chi tiết & cách hoạt động)

> Scope: `let/const` + TDZ, arrow, class & prototype, destructuring, spread/rest, template literal, modules, Promise & async/await, optional chaining, nullish, Symbol/iterator/generator, Proxy/Reflect, Set/Map/WeakMap, transpilation vs polyfill, ES2020–ES2024 highlights.

## ⭐ 1. Senior/Staff Summary

> ES5 → ES6+ không chỉ là cú pháp đẹp hơn — nó **đổi cơ chế chạy**: block scope + TDZ thay vì hoist `undefined`, lexical `this` thay vì dynamic, ES Modules + live binding thay vì IIFE/CommonJS, Promise + microtask thay vì callback hell. Senior cần trả lời theo 5 lớp: **syntax → runtime behavior → architecture → compatibility → trade-off**.

Quan trọng nhất cần phân biệt: **transpile (Babel/TS) xử lý cú pháp** — **polyfill (core-js, runtime) xử lý API**. Một browser thiếu `Promise` không phải syntax issue — Babel không "fix" nó, phải polyfill. Browserslist + `@babel/preset-env` quyết định cái gì được transform và cái gì để nguyên.

---

## 🧠 2. Key Mental Model

- `var` hoist với value = `undefined` ngay từ creation phase. `let/const/class` cũng hoist binding nhưng nằm trong **TDZ** — đọc trước dòng khai báo → `ReferenceError` (kể cả `typeof`).
- **Arrow** không có `this`/`arguments`/`super`/`new.target` của riêng nó → lexical từ scope ngoài.
- **`class`** = syntactic sugar trên prototype chain. Method nằm trên `Constructor.prototype` (share giữa instance), không phải copy.
- **ES Modules** = strict mode by default + **live binding** (import là tham chiếu sống tới export, không phải copy) + static analysis → tree-shaking.
- **`async/await`** chỉ là syntactic sugar trên Promise. Phần sau `await` chạy ở **microtask queue** → trước macrotask (`setTimeout`).
- **`??` vs `||`**: `??` chỉ fallback khi `null/undefined`. `||` fallback cho mọi falsy (`0`, `''`, `false`, `NaN`).
- **Spread chỉ shallow copy**. Nested reference vẫn share.

---

## 📚 3. Main Concepts

### 3.1. Bảng so sánh nhanh ES5 ↔ ES6+

| Chủ đề | ES5 | ES6+ |
|---|---|---|
| Biến | `var` (function scope, hoist `undefined`) | `let/const` (block scope, TDZ) |
| Function | `function () {}` | Arrow `() => {}`, default params, rest |
| `this` | Dynamic | Arrow → lexical |
| OOP | Constructor + prototype | `class`, `extends`, `super`, `#private` |
| String | Nối bằng `+` | Template literal `` `${}` ``, tagged template |
| Destructure | Gán thủ công | Object/array destructuring |
| Copy/merge | `Object.assign` | Spread `{...}` / `[...]` |
| Async | Callback, callback hell | Promise, async/await, AsyncIterator |
| Module | IIFE / CJS / AMD | `import/export`, dynamic import, top-level await |
| Collections | Object/Array | `Map`, `Set`, `WeakMap`, `WeakSet`, `WeakRef` |
| Null-safe | `obj && obj.x && obj.x.y` | `?.`, `??`, `??=` |
| Meta | Hạn chế | `Symbol`, `Proxy`, `Reflect`, iterator, generator |

### 3.2. Hoisting & Temporal Dead Zone

| Khai báo | Hoisted | Initialized | Dùng trước dòng khai báo |
|---|---|---|---|
| `var` | ✅ | ✅ (`undefined`) | OK → `undefined` |
| `let` / `const` | ✅ | ❌ (TDZ) | `ReferenceError` |
| `function decl` | ✅ | ✅ (cả thân) | Gọi được |
| `function expr` (var) | Biến hoisted | `undefined` | `TypeError` khi gọi |
| `class` | ✅ | ❌ (TDZ) | `ReferenceError` |

```ts
console.log(typeof a); // 'undefined' — undeclared OK
{
  // console.log(typeof b); // ❌ ReferenceError — TDZ kể cả typeof
  let b = 1;
}
```

> 💡 TDZ tồn tại để bắt lỗi dùng biến trước khi khai báo. Đó là feature, không phải bug.

### 3.3. Arrow function — gọn nhưng đổi hành vi

```ts
const counter = {
  value: 0,
  inc() {
    setTimeout(() => { this.value++; }, 100);  // ✅ this = counter (lexical)
    setTimeout(function () { this.value++; }, 100); // ❌ this = undefined / globalThis
  },
};
```

- ✅ Dùng cho: callback, `map/filter`, handler ngắn, không cần `this`.
- ❌ Tránh: object method cần `this`, constructor (không `new` được), method cần `arguments`/`super`.
- Chi tiết: xem [Topic07](./Topic07-arrow-vs-regular-functions-&-this-binding-(call,-apply,-bind).md).

### 3.4. Class — syntactic sugar trên prototype

```ts
// ES5: prototype manual
function Animal(name) { this.name = name; }
Animal.prototype.speak = function () { return this.name + ' sound'; };

function Dog(name, breed) { Animal.call(this, name); this.breed = breed; }
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

// ES6+
class AnimalC { constructor(public name: string) {} speak() { return `${this.name} sound`; } }
class DogC extends AnimalC {
  #age = 0;                                              // private field (ES2022)
  static species = 'Canis';                              // static
  constructor(name: string, public breed: string) { super(name); }
  speak() { return `${this.name} barks`; }
}
```

**Cần nhớ:**

- Method share qua `Constructor.prototype`, không copy mỗi instance.
- `extends` set prototype chain. `super()` gọi parent constructor.
- `#field` là true private ở engine level — khác convention `_field`.

### 3.5. Destructuring + Spread/Rest

```ts
// Destructure object, alias, default, nested
const { name, age: years = 0, address: { city } } = user;

// Default chỉ áp dụng cho undefined, KHÔNG cho null
const { a = 'A', b = 'B' } = { a: null, b: undefined };
// a = null, b = 'B'

// Spread (trải) vs Rest (gom)
const merged = [...arr1, ...arr2];                       // spread
const updated = { ...user, age: 31 };                    // spread
function sum(...nums: number[]) { return nums.reduce((a,b)=>a+b, 0); } // rest
const [head, ...tail] = [1, 2, 3, 4];                    // rest

// ⚠️ Spread chỉ shallow
const copy = { ...original }; copy.nested.x = 99;        // mutate luôn original.nested.x
// Deep: structuredClone(original) — không hỗ trợ function/DOM/class instance
```

### 3.6. Template literal + tagged template

```ts
const html = `<p>Hello ${name}</p>`;                     // basic
const css = String.raw`C:\path\${x}`;                    // raw — không escape

// Tagged template — i18n, SQL builder, CSS-in-JS
function sql(strings: TemplateStringsArray, ...vals: unknown[]) {
  // Trả về { text, params } — KHÔNG concat string với value
  return {
    text: strings.reduce((acc, s, i) => acc + s + (i < vals.length ? `$${i + 1}` : ''), ''),
    params: vals,
  };
}
const q = sql`SELECT * FROM users WHERE id = ${userId} AND role = ${role}`;
// { text: 'SELECT * FROM users WHERE id = $1 AND role = $2', params: [userId, role] }
```

### 3.7. Modules — `import/export` + live binding

```ts
// math.ts
export const PI = 3.14159;
export function area(r: number) { return PI * r * r; }
export default class Circle { constructor(public r: number) {} }

// app.ts
import Circle, { area, PI } from './math';
import * as MathUtils from './math';
const heavy = await import('./heavy');                   // dynamic — code splitting
```

**Cần nhớ:**

- ES Modules **strict mode by default**, **module scope** riêng, **singleton** (cache theo URL).
- **Live binding**: `import` là tham chiếu sống tới export — export thay đổi, import thấy giá trị mới. Khác CJS (copy lúc require).
- **Static analysis** → tree-shaking. Đó là lý do `import * as X` có thể block tree-shake nếu bundler không phân tích được.
- **Top-level `await`** (ES2022) chạy được trong module — block đến khi resolve.

### 3.8. Promise & async/await

```ts
async function loadDashboard() {
  // ❌ Sequential khi không cần
  const user = await fetchUser();
  const posts = await fetchPosts();

  // ✅ Parallel khi độc lập
  const [user2, posts2, perms] = await Promise.all([
    fetchUser(), fetchPosts(), fetchPerms(),
  ]);
}
```

| API | Behavior | Use case |
|---|---|---|
| `Promise.all` | All fulfilled, 1 reject → reject ngay | Mọi task bắt buộc OK |
| `Promise.allSettled` | Chờ hết, không reject | Báo cáo từng task |
| `Promise.race` | Settle đầu tiên thắng | Timeout, fastest source |
| `Promise.any` | Fulfilled đầu tiên, bỏ qua reject | Fallback nguồn |
| `Promise.withResolvers` (ES2024) | Trả `{ promise, resolve, reject }` | Defer pattern |

**Microtask order:**

```ts
console.log('A');
setTimeout(() => console.log('B'), 0);
Promise.resolve().then(() => console.log('C'));
(async () => { await null; console.log('D'); })();
console.log('E');
// Output: A E C D B
```

→ Promise callback + phần sau `await` là microtask, chạy trước macrotask `setTimeout`.

### 3.9. Optional chaining `?.` & nullish coalescing `??`

```ts
const theme = user.profile?.settings?.theme;       // không throw nếu null/undefined
const size = input.pageSize ?? 20;                 // chỉ fallback null/undefined
const text = '' ?? 'default';                      // '' (giữ chuỗi rỗng)
const text2 = '' || 'default';                     // 'default' (bug nếu '' hợp lệ)

// Logical assignment (ES2021)
config.timeout ??= 5000;                           // chỉ set nếu null/undefined
flags.debug ||= false;
user.role &&= user.role.toUpperCase();
```

> ⚠️ `?.` **không thay validation**. Field bắt buộc thiếu vẫn phải báo lỗi rõ ràng — đừng để `?.` nuốt bug.

### 3.10. Set / Map / WeakMap / WeakSet

| API | Lưu | Key/Value | Iterable | Use case |
|---|---|---|---|---|
| `Set` | Unique values | Bất kỳ | ✅ | Dedupe, membership check |
| `Map` | Key→Value | Key bất kỳ type | ✅ | Cache, dictionary, ordered |
| `WeakMap` | Object key → value | Key chỉ object | ❌ | Metadata theo DOM/instance, private data |
| `WeakSet` | Object refs | Object only | ❌ | Track tạm không giữ sống |
| `WeakRef` (ES2021) | Weak ref → object | Object | ❌ | Soft cache |
| `FinalizationRegistry` | Callback khi GC | Object | ❌ | Cleanup phụ trợ, KHÔNG cho business logic |

```ts
// Dedupe
const unique = [...new Set([1, 2, 2, 3])];               // [1, 2, 3]

// Map với object key
const cache = new Map<object, string>();
cache.set(domNode, 'rendered');

// WeakMap — gắn metadata DOM, auto GC khi node bị remove
const meta = new WeakMap<HTMLElement, { clicks: number }>();
```

**Map vs Object:**

- Object key bị coerce sang string/symbol. Map giữ nguyên type (object, function, NaN).
- Map giữ insertion order rõ ràng, có `.size`, hot path add/delete nhanh hơn object.
- Equality: `Set`/`Map` dùng SameValueZero → `NaN === NaN` (khác `===`).

**Vì sao WeakMap/WeakSet không iterable, không `.size`?** Vì entry có thể biến mất sau GC bất kỳ lúc nào — iterate sẽ không deterministic.

### 3.11. Symbol, iterator, generator, Proxy/Reflect

```ts
// Symbol — unique key, không xuất hiện trong Object.keys/JSON
const id = Symbol('id');
const u = { name: 'A', [id]: 1 };

// Iterable protocol
const range = {
  [Symbol.iterator]() {
    let i = 0;
    return { next: () => i < 3 ? { value: i++, done: false } : { value: undefined, done: true } };
  },
};
for (const n of range) console.log(n);                   // 0 1 2

// Generator — iterator tự động + pause/resume
function* gen() { yield 1; yield 2; }

// Proxy + Reflect — intercept thao tác
const proxy = new Proxy({ count: 0 }, {
  get: (t, k, r) => (console.log('read', k), Reflect.get(t, k, r)),
  set: (t, k, v, r) => Reflect.set(t, k, v, r),
});
```

Vue 3 reactivity và Immer draft đều dùng Proxy. ⚠️ Proxy có overhead — không lạm dụng cho hot path.

### 3.12. ES2016 → ES2024 highlights

- **ES2016**: `Array.includes`, `**` (exponent).
- **ES2017**: `async/await`, `Object.values/entries`, `String.padStart`.
- **ES2018**: Object rest/spread, async iteration `for await...of`, RegExp lookbehind.
- **ES2019**: `Array.flat/flatMap`, `Object.fromEntries`, `String.trimStart/End`, optional catch binding.
- **ES2020**: `?.`, `??`, `BigInt`, dynamic `import()`, `globalThis`, `Promise.allSettled`, `String.matchAll`.
- **ES2021**: `String.replaceAll`, `Promise.any`, logical assignment `??=`/`||=`/`&&=`, numeric separator `1_000`, `WeakRef`/`FinalizationRegistry`.
- **ES2022**: Class fields + `#private` methods/static, top-level `await`, `Array.at`, `Object.hasOwn`, error `cause`.
- **ES2023**: `Array.findLast/findLastIndex`, immutable array methods `toSorted/toReversed/toSpliced/with`.
- **ES2024**: `Promise.withResolvers`, `Object.groupBy`, `Array.fromAsync`, `Atomics.waitAsync`.

### 3.13. Transpile vs Polyfill — câu hỏi senior kinh điển

| Khái niệm | Xử lý | Ví dụ |
|---|---|---|
| **Transpile** | Đổi cú pháp → cú pháp cũ | Arrow → function, `?.` → `&&` chain, class → prototype |
| **Polyfill** | Thêm API runtime còn thiếu | `Promise`, `Array.includes`, `Object.fromEntries` |
| **Ponyfill** | Function thay thế, KHÔNG patch global | Import helper rời thay vì sửa prototype |
| **Browserslist** | Khai báo target | `last 2 versions, > 0.5%, not dead` |

```ts
// Cần transpile nếu target cũ:
const city = user?.address?.city ?? 'Unknown';

// Cần polyfill nếu runtime cũ thiếu:
Object.fromEntries(entries);
[1, 2, 3].includes(2);
```

**Babel vs TypeScript:**

- TS focus type-check + downlevel emit theo `target`.
- Babel focus syntax transform + plugin ecosystem.
- Cả 2 đều **không** thêm polyfill — phải config `core-js` (Babel) hoặc import polyfill thủ công.

---

## 🛠 4. Practical TypeScript Examples

### 4.1. Sequential vs Parallel — production-grade

```ts
async function loadProfilePage(userId: string) {
  // Step 1 phải xong trước (user quyết định query khác)
  const user = await fetchUser(userId);

  // Step 2 song song — không phụ thuộc nhau
  const [posts, follows, perms] = await Promise.all([
    fetchPosts(user.id),
    fetchFollows(user.id),
    fetchPerms(user.role),
  ]);

  return { user, posts, follows, perms };
}
```

### 4.2. `Object.fromEntries` + spread cho immutable update

```ts
// Update value theo điều kiện, giữ immutable
const next = Object.fromEntries(
  Object.entries(users).map(([id, u]) =>
    [id, u.active ? { ...u, lastSeen: Date.now() } : u]
  )
);
```

### 4.3. ES2023 immutable array methods cho React state

```ts
// ❌ sort() mutate array — vỡ React.memo + Immer guard
setItems(items.sort(byDate));

// ✅ toSorted() trả array mới
setItems(items.toSorted(byDate));
setItems(items.toSpliced(idx, 1));                 // immutable splice
setItems(items.with(idx, newItem));                // immutable replace
```

### 4.4. Tagged template cho SQL parameter binding

```ts
type SqlQuery = { text: string; params: unknown[] };

const sql = (strings: TemplateStringsArray, ...vals: unknown[]): SqlQuery => ({
  text: strings.reduce((acc, s, i) => acc + s + (i < vals.length ? `$${i + 1}` : ''), ''),
  params: vals,
});

const q = sql`SELECT * FROM users WHERE id = ${userId} AND role = ${role}`;
// { text: 'SELECT * FROM users WHERE id = $1 AND role = $2', params: [userId, role] }
// → giá trị KHÔNG bao giờ ghép thẳng vào câu lệnh → tránh SQL injection
```

### 4.5. `WeakMap` cho DOM metadata

```ts
const meta = new WeakMap<HTMLElement, { clicks: number }>();
function track(el: HTMLElement) {
  if (!meta.has(el)) meta.set(el, { clicks: 0 });
  el.addEventListener('click', () => meta.get(el)!.clicks++);
}
// Khi el bị remove khỏi DOM, entry trong WeakMap tự GC.
```

---

## ⚛️ 5. Production Notes / React Implications

- **Block scope + `let`** giải quyết được loop-closure bug → giảm hẳn bug trong handler/setTimeout.
- **Spread shallow** trong setState: nested object phải spread từng level hoặc dùng Immer.
- **`async/await` trong `useEffect`**: không để function effect async trực tiếp (return value sẽ là Promise, không phải cleanup). Wrap inner async function.
- **Dynamic `import()`** = code splitting / lazy load route (`React.lazy`).
- **ES Modules live binding** + tree-shaking → tránh `export default` cho utility (named export tree-shake tốt hơn).
- **`Promise.allSettled`** thường hợp dashboard hơn `Promise.all` — 1 widget fail không nên đánh sập cả page.
- **`structuredClone()`** browser API — replace `JSON.parse(JSON.stringify())` cho deep clone, nhưng KHÔNG clone function/DOM/class instance.
- **`globalThis`** chuẩn cross-environment (browser `window`, Node `global`, worker `self`). Code SSR-safe nên dùng `globalThis`.
- **Top-level `await`** trong module: cẩn thận — sẽ block toàn bộ module graph phụ thuộc → tăng TTFB nếu dùng cho data fetching ở entry.
- **`#private` vs closure**: với class có nhiều method dùng chung state, `#field` modern hơn. Closure dùng cho factory.

---

## ⚠️ 6. Common Pitfalls

- ❌ **Dùng `var` trong code mới** — block scope mặc định cho an toàn.
- ❌ **Arrow làm object method cần `this`** — `this` thành scope ngoài.
- ❌ **Quên `await`** → `user` là Promise, `.name` là `undefined`.
- ❌ **Await tuần tự khi độc lập** → chậm gấp nhiều lần. Dùng `Promise.all`.
- ❌ **Nhầm shallow với deep copy**: `{ ...obj }` không clone nested. Dùng `structuredClone` hoặc Immer.
- ❌ **`||` cho default khi `0`/`''`/`false` hợp lệ** → dùng `??`.
- ❌ **`?.` thay validation**: business-required field thiếu vẫn phải fail rõ.
- ❌ **`JSON.stringify(JSON.parse())` cho deep clone**: mất function, Date thành string, throw với circular, không xử lý Map/Set.
- ❌ **Import toàn bộ `core-js`** vào bundle. Dùng `@babel/preset-env` + `useBuiltIns: 'usage'` để chỉ polyfill cái dùng.
- ❌ **Top-level `await` trong entry point dữ liệu nặng** → block bundle execution → TTFB tăng.
- ❌ **Class field arrow vs prototype method**: arrow class field tạo function riêng mỗi instance — list rất lớn cân nhắc prototype method.
- ❌ **`WeakRef` cho logic bắt buộc**: GC không deterministic, `.deref()` có thể `undefined` bất kỳ lúc nào.
- ❌ **`FinalizationRegistry` cho business logic**: callback có thể chạy muộn hoặc không chạy. Chỉ cho cleanup phụ trợ (WASM memory, file handle).
- ⚠️ **Object key bị coerce sang string** — dùng `Map` khi key là object/function/number giữ nguyên type.
- ⚠️ **TDZ với `typeof`**: không "safe" như `typeof` của undeclared variable.

---

## ✅ 7. Decision Guide / Checklist

**Khi nào dùng gì:**

- `const` mặc định → `let` khi reassign → tránh `var`.
- Arrow cho callback và class field handler giữ `this`; regular function cho object method / constructor / cần `arguments`/`super`.
- `??` cho default-when-nullish; `||` chỉ khi falsy thực sự là invalid.
- `Promise.all` cho task song song bắt buộc OK; `allSettled` cho dashboard chấp nhận partial fail.
- `Map`/`Set` thay object khi: key không phải string, cần `.size`, hot path add/delete, giữ insertion order.
- `WeakMap` cho metadata theo DOM/instance; `#field` cho private trong class; closure cho factory function.
- `structuredClone` thay `JSON.parse(JSON.stringify())` cho deep clone (data-only); Immer cho deep update có cấu trúc.
- Immutable array methods (`toSorted`/`toReversed`/`with`/`toSpliced`) cho React state — không mutate.

**Checklist build/compat:**

- [ ] Browserslist khai báo target rõ ràng.
- [ ] `@babel/preset-env` + `useBuiltIns: 'usage'` (hoặc `swc/tsc target` phù hợp).
- [ ] Polyfill cho API runtime cần thiết — không import all.
- [ ] Test trên target cũ nhất bạn cam kết support.
- [ ] Phân biệt rõ syntax vs API trong PR description khi đụng compat.

**Cấu trúc trả lời "ES5 vs ES6+ khác gì?" theo 5 lớp:**

1. **Syntax**: `let/const`, arrow, template, destructuring, spread/rest, class.
2. **Runtime**: block scope + TDZ, lexical `this`, prototype chain, microtask.
3. **Architecture**: ES Modules + live binding + tree-shaking + dynamic import.
4. **Compatibility**: transpile (syntax) vs polyfill (API) vs Browserslist target.
5. **Trade-off**: readability > micro-opt; cẩn thận shallow copy, await tuần tự, bundle size, top-level `await`.

---

## 💬 8. Short Interview Answer

> Em thường trả lời câu này theo 5 lớp để tránh sa đà liệt kê feature.
>
> Lớp đầu là **syntax**: `let/const`, arrow, template literal, destructuring, spread/rest, class — đẹp hơn và an toàn hơn. Lớp 2 là **runtime behavior**, đây mới là phần em nhấn — `var` hoist với `undefined`, còn `let/const/class` cũng được hoist nhưng nằm trong TDZ, đọc trước dòng khai báo là `ReferenceError` luôn kể cả `typeof`. Arrow thì lexical `this`, `class` là syntactic sugar trên prototype chain chứ không phải class thật như Java. Async/await là sugar trên Promise và phần sau `await` chạy ở microtask queue, trước macrotask.
>
> Lớp 3 là **architecture**: ES Modules đem lại **live binding** và **static analysis** cho tree-shaking. Em ưu tiên named export hơn default export vì tree-shake tốt hơn. Dynamic `import()` thì cho code splitting với `React.lazy`. Em cũng để ý top-level `await` (ES2022) có thể block module graph nên không lạm dụng ở entry point.
>
> Lớp 4 là **compatibility**, đây là chỗ hay bị nhầm: **Babel/TS chỉ xử lý syntax, polyfill mới xử lý API runtime**. Một browser thiếu `Promise` thì Babel không "fix" — phải polyfill `core-js`. Em hay config `@babel/preset-env` với `useBuiltIns: 'usage'` để chỉ polyfill cái thực sự dùng, theo Browserslist target.
>
> Lớp 5 là **trade-off** thực tế: `?.` không thay validation, `??` chứ đừng `||` khi `0` hợp lệ, spread chỉ shallow, await tuần tự là cái em hay catch trong code review. Còn ES2023+ thì em hay dùng `toSorted`/`with` cho React state immutable, và `structuredClone` thay `JSON.parse(JSON.stringify())` cho deep clone — nhưng nhớ nó không clone function với DOM.

---

**📌 Ghi nhớ nhanh:**

- 🔥 **Runtime đổi**: block scope + TDZ, lexical `this`, microtask, prototype.
- 📦 **Modules**: strict + live binding + tree-shake; dynamic import = code splitting.
- ⚡ **`async/await`**: sugar trên Promise; phần sau `await` = microtask.
- 🧪 **`??` vs `||`**: nullish vs mọi falsy.
- 🛡️ **Spread shallow**; deep dùng `structuredClone`/Immer.
- 🗺️ **`Map`/`WeakMap`**: key bất kỳ type / metadata theo object auto-GC.
- 🏗️ **Babel/TS = syntax**, **polyfill = API**. Hai chuyện khác nhau.
- 🆕 **ES2023+**: `toSorted/toReversed/with/toSpliced` cho immutable; `Promise.withResolvers`, `Object.groupBy` (ES2024).
