# 🔐 Topic 06 — Closure & Data Privacy

## ⭐ 1. Senior/Staff Summary

> **Closure** = `function + lexical environment` của scope nơi nó được định nghĩa. Inner function giữ **reference** (không phải copy) đến biến outer, ngay cả khi outer đã return.
>
> Closure là cơ chế nền cho rất nhiều pattern FE hằng ngày: **private state** (Zustand store, factory), **memoization / debounce / throttle**, **currying & partial application**, **event handler giữ ngữ cảnh**, và là nguồn gốc của **stale closure bug** trong React hooks.

Senior cần biết: closure giữ *reference*, không phải snapshot → đó là lý do hooks có dependency array, và là lý do `setInterval` + `useState` dễ bị stale. Closure cũng là một **nguồn rò rỉ bộ nhớ** thường gặp nếu giữ DOM/Array lớn sống ngoài vòng đời mong đợi.

---

## 🧠 2. Key Mental Model

- Closure không phải "biến private" — nó là **một function nhớ scope ngoài**. Data privacy là *use case*, không phải định nghĩa.
- Inner function giữ **`[[Environment]]`** trỏ tới lexical environment của outer. Khi outer return, environment vẫn được giữ sống nếu còn function nào reference nó.
- **Closure giữ reference**, không phải value snapshot → biến outer thay đổi sau khi closure tạo ra, closure đọc giá trị mới (đây là gốc rễ của stale closure trong React).
- 3 cách "private" data trên JS hiện đại:
  - 🔒 **Closure** — kinh điển, không runtime cost ngoài việc giữ env sống.
  - 🆕 **Class private field `#x`** (ES2022) — true private ở engine level.
  - 🗂️ **`WeakMap<instance, privateData>`** — auto GC khi instance không còn referenced.
- Closure không "chậm" — V8 tối ưu rất tốt. Vấn đề chỉ là **memory retention** (giữ env sống lâu hơn cần) và **stale value** trong async/React.

---

## 📚 3. Main Concepts

### 3.1. Closure = Function + Lexical Environment

```ts
function makeAdder(x: number) {
  return function (y: number) {
    return x + y;          // x sống trong closure environment
  };
}

const add5 = makeAdder(5);
add5(3);                   // 8 — makeAdder đã return, x vẫn được giữ
```

Mental model: `add5` mang theo một object `{ x: 5 }` ẩn — đó là lexical environment.

### 3.2. Data Privacy — 3 cách trên JS hiện đại

```ts
// 1️⃣ Closure (kinh điển)
function createCounter() {
  let count = 0;
  return {
    inc: () => ++count,
    get: () => count,
  };
}

// 2️⃣ Class private field — ES2022, true private ở engine level
class Counter {
  #count = 0;
  inc() { return ++this.#count; }
  get count() { return this.#count; }
}

// 3️⃣ WeakMap — private + auto GC theo instance
const _state = new WeakMap<Counter2, { count: number }>();
class Counter2 {
  constructor() { _state.set(this, { count: 0 }); }
  inc() { return ++_state.get(this)!.count; }
}
```

| Cách | Privacy | GC behavior | Trade-off |
|---|---|---|---|
| Closure | Bằng scope | Env sống đến khi không ai reference function | Mỗi instance một bản method (memory) |
| `#field` | Engine-level | GC theo instance | Modern, type-safe, native debugger inspect |
| `WeakMap` | Module-scope | Auto-GC theo key | Verbose, ngày nay ít dùng do `#field` |

### 3.3. Loop + `var` — closure share cùng binding

```ts
// ❌ var: 1 binding chia sẻ — in 3, 3, 3
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}

// ✅ let: mỗi vòng 1 binding mới — in 0, 1, 2
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}

// ✅ Trước ES6: IIFE để tạo scope riêng
for (var i = 0; i < 3; i++) {
  ((idx) => setTimeout(() => console.log(idx), 0))(i);
}
```

> 💡 Đây là *câu hỏi closure kinh điển nhất*. Hiểu được = hiểu reference vs snapshot.

### 3.4. Module Pattern — IIFE giờ chỉ thấy trong bundler

```ts
// Trước ES modules: IIFE + closure
const userModule = (() => {
  let users: string[] = [];
  return {
    add: (n: string) => users.push(n),
    list: () => [...users],   // ✅ Return copy, không expose ref
  };
})();
```

Ngày nay: ES modules + `const` thay được hoàn toàn. IIFE chủ yếu xuất hiện trong **bundler output** (Webpack/Rollup UMD wrap).

### 3.5. Closure trong store (Zustand-style)

```ts
type Listener<T> = (state: T, prev: T) => void;

function createStore<T>(
  initializer: (set: (p: Partial<T> | ((s: T) => Partial<T>)) => void, get: () => T) => T
) {
  let state: T;                               // 🔒 private
  const listeners = new Set<Listener<T>>();   // 🔒 private

  const get = () => state;
  const set = (patch: Partial<T> | ((s: T) => Partial<T>)) => {
    const prev = state;
    const next = typeof patch === 'function' ? patch(prev) : patch;
    state = { ...prev, ...next };
    listeners.forEach(l => l(state, prev));
  };

  state = initializer(set, get);
  return {
    getState: get,
    setState: set,
    subscribe: (l: Listener<T>) => (listeners.add(l), () => listeners.delete(l)),
  };
}
```

Closure giúp:

- 🔒 `state` / `listeners` không truy cập trực tiếp được — chỉ qua API.
- 🏗️ Mỗi `createStore()` ra **một scope mới** → multi-store, test isolation, SSR-safe.
- ⚡ Không cần `this` binding (khác class), không Proxy overhead.

### 3.6. Closure-based utilities

```ts
// once: chạy đúng 1 lần
function once<A extends unknown[], R>(fn: (...a: A) => R) {
  let called = false, value: R;
  return (...args: A) => {
    if (!called) { called = true; value = fn(...args); }
    return value;
  };
}

// debounce
function debounce<A extends unknown[]>(fn: (...a: A) => void, ms: number) {
  let t: ReturnType<typeof setTimeout> | undefined;
  return (...args: A) => {
    if (t) clearTimeout(t);
    t = setTimeout(() => fn(...args), ms);
  };
}

// memoize
function memoize<A extends unknown[], R>(fn: (...a: A) => R) {
  const cache = new Map<string, R>();
  return (...args: A) => {
    const key = JSON.stringify(args);
    if (!cache.has(key)) cache.set(key, fn(...args));
    return cache.get(key)!;
  };
}
```

Tất cả đều có cùng pattern: **HOF return inner function, inner function close over state riêng**.

---

## 🛠 4. Practical TypeScript Examples

### 4.1. Factory thay class cho simple service

```ts
function createApiClient(baseUrl: string, token: string) {
  const headers = { Authorization: `Bearer ${token}` };   // 🔒 closure

  return {
    get: <T>(path: string) =>
      fetch(`${baseUrl}${path}`, { headers }).then(r => r.json() as Promise<T>),
    post: <T>(path: string, body: unknown) =>
      fetch(`${baseUrl}${path}`, {
        method: 'POST',
        headers: { ...headers, 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
      }).then(r => r.json() as Promise<T>),
  };
}

const api = createApiClient('https://api.x', 'abc');
api.get<User>('/me');
```

Lợi ích: không lo `this` binding khi destructure (`const { get } = api`), test mock dễ.

### 4.2. Cleanup closure để tránh leak

```ts
function setupHeavyListener() {
  const huge = new Array(1_000_000).fill(0);     // ⚠️ ~8MB

  const onClick = () => console.log(huge.length); // closure giữ huge
  document.getElementById('btn')!.addEventListener('click', onClick);

  // ✅ Trả về dispose để cleanup
  return () => {
    document.getElementById('btn')!.removeEventListener('click', onClick);
    // huge sẽ được GC sau khi onClick không còn reference
  };
}
```

### 4.3. Stale closure — bug kinh điển trong React

```tsx
// ❌ count luôn là 0 — closure capture count tại render đầu tiên
function Counter() {
  const [count, setCount] = useState(0);
  useEffect(() => {
    const id = setInterval(() => {
      setCount(count + 1);            // stale: count đóng băng = 0
    }, 1000);
    return () => clearInterval(id);
  }, []);                              // deps rỗng → effect không chạy lại
  return <div>{count}</div>;
}

// ✅ Functional updater — không phụ thuộc closure
useEffect(() => {
  const id = setInterval(() => setCount(c => c + 1), 1000);
  return () => clearInterval(id);
}, []);

// ✅ Hoặc dùng useRef để giữ giá trị mới nhất
const countRef = useRef(count);
useEffect(() => { countRef.current = count; });
```

### 4.4. `WeakMap` để private + cho phép GC

```ts
const dom = new WeakMap<HTMLElement, { clicks: number }>();

function track(el: HTMLElement) {
  if (!dom.has(el)) dom.set(el, { clicks: 0 });
  el.addEventListener('click', () => dom.get(el)!.clicks++);
}
// Khi `el` bị remove khỏi DOM và không còn reference, entry trong WeakMap tự GC.
```

---

## ⚛️ 5. Production Notes / React Implications

- **Stale closure** = bug #1 với `useEffect`/`useCallback`/`useMemo` khi deps thiếu. Fix: functional updater (`setX(prev => …)`), `useRef`, hoặc thêm vào deps + accept re-run.
- **`useRef.current` không trigger render**, nhưng đọc nó luôn cho giá trị mới nhất → công cụ để "vượt qua" stale closure trong subscribe handler.
- **Event handler / timer / WebSocket subscriber** dễ giữ component đã unmount sống → leak. Luôn cleanup trong `useEffect` return.
- **`useCallback` thay đổi closure khi deps đổi** → child memo re-render. Đó là tính năng, không phải bug — nhưng nếu deps không stable, `useCallback` vô dụng.
- **Zustand / Jotai / Redux Toolkit** đều dùng closure để giữ store state. Hiểu pattern này giúp viết custom store / selector đúng.
- **Tree-shaking**: factory function (closure) thường tree-shake tốt hơn class với side-effect static init.
- **SSR safety**: closure-based factory tạo *instance per request* dễ hơn so với class singleton — tránh state leak giữa request.
- **DevTools**: Chrome → Memory → Heap Snapshot → "Retainers" — xem closure nào đang giữ object sống.

---

## ⚠️ 6. Common Pitfalls

- ❌ **Stale closure trong React**: `useEffect(() => setInterval(...), [])` đọc state cũ. Dùng functional updater hoặc `useRef`.
- ❌ **Loop + `var` + async callback**: closure share cùng binding → cùng giá trị cuối. Dùng `let` hoặc IIFE.
- ❌ **Closure giữ DOM/Array lớn sống lâu hơn cần**: chừng nào callback còn được tham chiếu (event listener, timer), data còn sống. Nhớ `removeEventListener` / `clearTimeout`.
- ❌ **Return reference của private data**: `return users` thay vì `return [...users]` → caller mutate được private state.
- ❌ **Tin closure là snapshot**: nó là *reference*. Outer thay đổi sau khi closure tạo, closure đọc giá trị mới.
- ❌ **Lạm dụng closure cho mọi private**: với class hiện đại, `#field` rõ ràng và type-safe hơn. Closure chỉ thắng khi cần factory/multi-instance không-`this`.
- ❌ **`JSON.stringify(args)` làm cache key** trong memoize-closure: function/Date/circular/`undefined`/`NaN` gây sai key.
- ❌ **`useCallback` với deps không stable**: tạo closure mới mỗi render → vô tác dụng. Dùng `useRef` để giữ deps stable.
- ⚠️ **Closure trong long-lived listener** (analytics, EventSource): nhớ unsubscribe khi navigation/unmount, không chỉ trông cậy "trang sẽ refresh".

---

## ✅ 7. Decision Guide

**Khi nào dùng closure cho private state?**

- ✅ Factory tạo *nhiều instance độc lập* (store, API client, debouncer).
- ✅ Không muốn dính `this` binding (hook, callback truyền đi xa).
- ✅ Tree-shakable utility (no class side-effects).

**Khi nào dùng `#field` (class private)?**

- ✅ Có inheritance / nhiều method dùng chung instance state.
- ✅ Muốn debugger inspect tự nhiên qua class.
- ✅ Type-safe + IDE support tốt hơn.

**Khi nào dùng `WeakMap`?**

- ✅ Cần associate data với external object mình không kiểm soát (DOM element).
- ✅ Muốn private + auto-GC theo key.

**Checklist trước khi merge:**

- [ ] Closure không vô tình giữ DOM/Array lớn sống ngoài vòng đời?
- [ ] Event listener / timer có `remove` / `clear` trong cleanup?
- [ ] Trong React: hooks không bị stale closure (functional updater / ref / đủ deps)?
- [ ] Private data return ra ngoài đều là *copy*, không expose reference gốc?
- [ ] Loop async callback dùng `let` / `const`, không `var`?
- [ ] Cân nhắc `#field` thay closure nếu là class có nhiều method?

**So sánh nhanh — vì sao closure thắng class/Proxy/global cho store:**

- 🆚 **Class + `this`**: dễ mất context khi destructure method.
- 🆚 **Proxy**: trap overhead + debug khó, không cần thiết cho pub/sub.
- 🆚 **Global singleton**: leak state giữa test/SSR, không tạo được multi-instance.

---

## 💬 8. Short Interview Answer

> Em định nghĩa closure là **function cộng với lexical environment** của scope nơi nó được định nghĩa — inner function giữ *reference* đến biến outer, không phải snapshot. Đó là điểm em hay nhấn vì nó giải thích được luôn cả stale closure trong React.
>
> Use case em hay dùng nhất là **private state qua factory function** — kiểu Zustand: mỗi lần gọi `createStore` ra một scope mới, `state` và `listeners` private trong closure, ngoài chỉ thấy `getState/setState/subscribe`. Em thích pattern này hơn class ở 3 điểm: không lo `this` binding khi destructure, dễ tạo nhiều instance độc lập cho SSR/test, và tree-shake tốt hơn.
>
> Ngày nay nếu là class có nhiều method dùng chung state, em sẽ chọn **`#field` (ES2022)** thay closure vì true private ở engine level, type-safe hơn, debugger inspect tự nhiên. Còn `WeakMap` em chỉ dùng khi cần gắn data với external object như DOM element và muốn auto-GC.
>
> Trap em luôn nhắc team là **stale closure trong hooks** — `useEffect` với deps rỗng + `setInterval` đọc `count` cũ vì closure capture render đầu. Em fix bằng functional updater `setCount(c => c + 1)` hoặc `useRef` để giữ giá trị mới nhất. Và đừng quên cleanup event listener / timer — closure giữ DOM/Array lớn sống là một nguồn leak rất phổ biến.

---

**📌 Ghi nhớ nhanh:**

- 🔥 **Closure** = function + lexical env; giữ *reference*, không snapshot.
- 🔒 **Privacy hiện đại**: closure (factory) | `#field` (class) | `WeakMap` (external object).
- ⚛️ **Stale closure**: functional updater / `useRef` / đủ deps.
- 🧹 **Leak**: event listener / timer / huge array trong closure → cleanup.
- 🔁 **Loop + var** = share binding → dùng `let`.
- 🏗️ **Zustand pattern**: closure cho state + listeners, multi-instance, SSR-safe.
