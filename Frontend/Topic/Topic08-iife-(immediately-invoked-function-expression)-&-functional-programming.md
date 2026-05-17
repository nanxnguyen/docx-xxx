# 🎯 Topic 08 — IIFE & Functional Programming

> Scope: IIFE, pure functions, immutability, HOF, currying, function composition, memoization, recursion, composition vs inheritance, Ramda / lodash-fp.

## ⭐ 1. Senior/Staff Summary

> **IIFE** = function tự gọi ngay sau khi định nghĩa, ngày xưa dùng để tạo private scope khi chưa có `let`/ES modules. Bây giờ gần như chỉ còn thấy trong **bundler output (UMD wrapper)**, **async top-level workaround**, hoặc **one-shot init**.
>
> **Functional Programming** trên FE là một bộ nguyên tắc, không phải một paradigm "all or nothing": pure function + immutability + composition. Trên React/Redux, FP là *điều kiện cần* để memoization, `React.memo`, reference equality, time-travel debug hoạt động đúng.

Senior cần phân biệt được: (1) immutability ở mức reference (đủ cho React) vs deep immutability (đủ cho audit), (2) currying ≠ partial application, (3) `useMemo` ≠ `memoize`, (4) `Object.freeze` chỉ shallow, (5) recursion trong V8 không có tail-call optimization — deep recursion vẫn stack overflow.

---

## 🧠 2. Key Mental Model

- **IIFE** = `(function(){})()` hoặc `(() => {})()`. Output là *giá trị return*, không phải function. Nó là "callsite gắn liền expression".
- **Pure function** = **referential transparency**: thay call bằng giá trị return không đổi ngữ nghĩa chương trình. Cần 2 thứ — same input → same output, **không side effect** (không mutate ngoài, không I/O, không Date.now/Math.random).
- **Immutability** không phải "không bao giờ thay đổi", mà là "thay đổi → tạo reference mới". Đó là lý do `React.memo` / `useMemo` / `Object.is` so sánh bằng reference hoạt động.
- **HOF** = function nhận function hoặc trả function. `map`/`filter`/`reduce`/`debounce`/`memoize` đều là HOF.
- **Currying** ≠ **Partial application**:
  - Currying: `f(a, b, c)` → `f(a)(b)(c)` — luôn unary.
  - Partial: cố định một số args trước, return function nhận args còn lại — không bắt buộc unary.
- **Composition**: `compose(f,g,h)(x) = f(g(h(x)))` (phải→trái). `pipe(f,g,h)(x) = h(g(f(x)))` (trái→phải, dễ đọc cho data flow).
- **Memoization**: cache `args → result` cho pure function. Có 3 trap: key serialization, cache không giới hạn (memory leak), invalidation.
- **Recursion**: thay vòng lặp + mutable accumulator bằng base case + recursive case. JS không có TCO → deep recursion ≈ 10k call là vỡ stack.

---

## 📚 3. Main Concepts

### 3.1. IIFE — vì sao trước cần, giờ ít cần

```ts
// Trước ES6: scope-leak vì var không có block scope
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0); // 3, 3, 3
}
// IIFE giải quyết → mỗi vòng có scope riêng
for (var i = 0; i < 3; i++) {
  (function (j) { setTimeout(() => console.log(j), 0); })(i); // 0, 1, 2
}

// ES6+: dùng let, không cần IIFE
for (let i = 0; i < 3; i++) setTimeout(() => console.log(i), 0); // 0, 1, 2
```

**Use cases còn thấy ngày nay:**

- 📦 **Bundler output (UMD/IIFE)** — Webpack/Rollup wrap toàn bộ bundle trong IIFE để không leak ra global.
- ⚡ **Async IIFE** ở target chưa support top-level await:
  ```ts
  (async () => {
    const data = await fetch('/api/init').then(r => r.json());
    bootstrap(data);
  })();
  ```
- 🔒 **One-shot init** trong script tag inline (analytics, feature flag).

> 💡 Trong app code TypeScript hiện đại, **ES modules + `const`** đã thay thế 95% use case của IIFE. Nếu thấy IIFE trong PR mới, hỏi tại sao.

### 3.2. Pure functions — chuẩn referential transparency

| Yêu cầu | Pure | Impure |
|---|---|---|
| Same input → same output | ✅ | `Math.random()`, `Date.now()`, `fetch()` |
| Không side effect | ✅ | `console.log`, mutate arg, write DB, dispatch Redux |
| Không phụ thuộc state ngoài | ✅ | đọc biến module-level mutable |

```ts
// ✅ Pure: chỉ tính từ input
const add = (a: number, b: number) => a + b;

// ❌ Impure: phụ thuộc state ngoài
let rate = 0.1;
const withTax = (amount: number) => amount * (1 + rate);

// ✅ Sửa: đưa rate vào input
const withTaxPure = (amount: number, rate: number) => amount * (1 + rate);
```

### 3.3. Immutability — shallow đủ cho React, đôi khi cần deep

```ts
// ✅ Update immutable bằng spread
const next = { ...user, age: 26 };
const arrNext = [...arr, item];
const arrFiltered = arr.filter(x => x.id !== id);

// ⚠️ Spread chỉ shallow — nested reference vẫn share
const next = { ...state, user: { ...state.user, age: 26 } };

// 🔥 Với deep nested: dùng Immer (Proxy + structural sharing)
import { produce } from 'immer';
const next = produce(state, draft => {
  draft.user.profile.address.city = 'HCM'; // viết mutable, ra immutable
});
```

**`Object.freeze` không thay được Immer:**

- Shallow only → nested object vẫn mutate được.
- Strict mode: mutate throw `TypeError`. Sloppy mode: silent fail.
- Có cost runtime → không freeze hot path / large state.

**Structural sharing** (Immer, Immutable.js): chỉ clone path bị thay đổi, các nhánh khác share reference cũ → tiết kiệm memory + giữ reference equality cho `React.memo`.

### 3.4. Higher-Order Functions — pattern phổ biến trên FE

```ts
// HOF nhận function → trả function (wrapper / decorator)
const withRetry = <A extends unknown[], R>(
  fn: (...a: A) => Promise<R>,
  max = 3,
) => async (...args: A): Promise<R> => {
  let lastErr: unknown;
  for (let i = 0; i < max; i++) {
    try { return await fn(...args); }
    catch (e) { lastErr = e; }
  }
  throw lastErr;
};

const fetchUserSafe = withRetry(fetchUser, 3);
```

Array HOF (`map`/`filter`/`reduce`/`flatMap`/`some`/`every`) là cách viết FE phổ biến nhất — trả về array mới, immutable.

### 3.5. Currying vs Partial application

```ts
// Curry: luôn unary
const curriedAdd = (a: number) => (b: number) => (c: number) => a + b + c;
curriedAdd(1)(2)(3); // 6

// Partial: cố định một số args (không bắt buộc unary)
const add = (a: number, b: number, c: number) => a + b + c;
const addOneTwo = add.bind(null, 1, 2); // partial qua bind
addOneTwo(3); // 6

// Use case thực tế: tạo handler "đóng" config
const trackEvent = (category: string) => (action: string) => (payload: object) =>
  analytics.track({ category, action, payload });
const trackOrder = trackEvent('order');
trackOrder('submit')({ amount: 100 });
trackOrder('cancel')({ reason: 'timeout' });
```

> 💡 Trên FE thực tế, **closure thường rõ ràng hơn currying**. Curry chỉ thắng khi cần compose nhiều function ở style point-free (Ramda).

### 3.6. Composition — `pipe` thường dễ đọc hơn `compose`

```ts
type Fn<A, B> = (a: A) => B;

// pipe: trái → phải (đọc theo thứ tự data flow)
const pipe = <T>(...fns: Fn<T, T>[]) =>
  (x: T) => fns.reduce((acc, fn) => fn(acc), x);

const slug = pipe<string>(
  s => s.trim(),
  s => s.toLowerCase(),
  s => s.replace(/\s+/g, '-'),
);
slug('  Hello World  '); // 'hello-world'
```

`compose` (phải→trái) phù hợp khi viết theo style toán học `f ∘ g`. Trong code FE, `pipe` đọc tự nhiên hơn vì khớp với thứ tự đọc.

### 3.7. Memoization — cẩn thận key và bộ nhớ

```ts
function memoize<A extends unknown[], R>(fn: (...a: A) => R) {
  const cache = new Map<string, R>();
  return (...args: A): R => {
    const key = JSON.stringify(args);   // ⚠️ Xem trap ở Pitfalls
    if (cache.has(key)) return cache.get(key)!;
    const r = fn(...args);
    cache.set(key, r);
    return r;
  };
}
```

**Memo trên React:** `useMemo(fn, deps)` **không** giống `memoize(fn)`. `useMemo` chỉ cache 1 giá trị giữa các render (cache size = 1), không phải `args → result` map. Để cache đa-key, kết hợp `useMemo` với `Map` hoặc dùng `react-query`/`memoize-one`.

### 3.8. Recursion — cẩn thận stack

```ts
// Recursion thuần
const sum = (xs: number[]): number =>
  xs.length === 0 ? 0 : xs[0] + sum(xs.slice(1));

// Tail recursion (JS engines hiện không TCO → vẫn có thể overflow)
const sumTail = (xs: number[], acc = 0): number =>
  xs.length === 0 ? acc : sumTail(xs.slice(1), acc + xs[0]);

// Trampoline: tránh stack overflow cho deep recursion
function trampoline<T>(fn: () => T | (() => unknown)): T {
  let result: any = fn;
  while (typeof result === 'function') result = result();
  return result;
}
```

> ⚠️ V8/SpiderMonkey **không** implement TCO (chỉ Safari/JSC bật ở strict mode). Đừng tin tail call sẽ tự tối ưu.

### 3.9. Composition vs Inheritance

| Aspect | Inheritance (IS-A) | Composition (HAS-A) |
|---|---|---|
| Coupling | Tight — đổi base ảnh hưởng child | Loose — mix behaviors độc lập |
| Reuse | Hierarchy cứng | Combinator linh hoạt |
| React | HOC/render props/hooks | ✅ Hooks chính là composition |
| Khi dùng | Strict IS-A (hiếm trên FE) | Hầu hết case còn lại |

> "Favor composition over inheritance" — đặc biệt đúng với React: **custom hooks** thay HOC, **slots/children** thay subclassing.

### 3.10. Ramda / lodash-fp

- Cả 2 đều **auto-curried + data-last** → tối ưu cho `pipe`.
- Ramda có **Lens** (view/set/over) — đẹp cho deep update kiểu functional thuần.
- lodash-fp: API quen, bundle nhỏ hơn, nhưng yếu hơn về functional features.
- **Tree-shaking trap**: import `'ramda'` whole có thể kéo cả thư viện. Dùng `import map from 'ramda/src/map'` hoặc babel plugin.
- **Lựa chọn hiện đại**: với TypeScript-heavy code, nhiều team thay Ramda bằng inline `pipe` + native methods vì type-safe hơn.

```ts
import * as R from 'ramda';
const getActiveNames = R.pipe(
  R.filter(R.propEq('active', true)),
  R.map(R.prop('name')),
  R.map(R.toUpper),
);
getActiveNames([{ name: 'a', active: true }, { name: 'b', active: false }]); // ['A']
```

---

## 🛠 4. Practical TypeScript Examples

### 4.1. IIFE — async bootstrap

```ts
// Bootstrap app, top-level await chưa hỗ trợ (target ES2017)
(async () => {
  const config = await fetch('/config.json').then(r => r.json());
  ReactDOM.createRoot(document.getElementById('root')!).render(<App config={config} />);
})();
```

### 4.2. Pure data pipeline cho table

```ts
type Order = { id: string; status: 'pending' | 'paid' | 'cancelled'; amount: number };

const summary = (orders: Order[]) =>
  orders
    .filter(o => o.status === 'paid')         // pure
    .map(o => ({ id: o.id, amount: o.amount })) // pure
    .reduce((acc, o) => acc + o.amount, 0);    // pure
```

→ Test chỉ cần input/output, không mock, không spy.

### 4.3. HOF — debounce với type-safe wrapper

```ts
function debounce<A extends unknown[]>(
  fn: (...a: A) => void,
  ms: number,
) {
  let t: ReturnType<typeof setTimeout> | undefined;
  return (...args: A) => {
    if (t) clearTimeout(t);
    t = setTimeout(() => fn(...args), ms);
  };
}

const onSearch = debounce((q: string) => api.search(q), 300);
```

### 4.4. Memoized selector kiểu Reselect

```ts
function memoizeOne<A extends unknown[], R>(fn: (...a: A) => R) {
  let lastArgs: A | undefined;
  let lastResult: R;
  return (...args: A) => {
    if (lastArgs && args.every((v, i) => Object.is(v, lastArgs![i]))) return lastResult;
    lastArgs = args;
    lastResult = fn(...args);
    return lastResult;
  };
}

const selectVisibleTodos = memoizeOne(
  (todos: Todo[], filter: string) =>
    todos.filter(t => filter === 'all' || t.status === filter),
);
```

### 4.5. Composition cho data transform

```ts
const normalizeUser = pipe<RawUser>(
  raw => ({ ...raw, name: raw.name.trim() }),
  u => ({ ...u, email: u.email.toLowerCase() }),
  u => ({ ...u, displayName: u.nickname ?? u.name }),
);
```

---

## ⚛️ 5. Production Notes / React Implications

- **Reference equality là currency của React.** Pure update + immutable spread giữ reference ổn định ở subtree không đổi → `React.memo` hoạt động.
- `useMemo` / `useCallback` chỉ giúp **giữ reference**, không phải để "tăng tốc". Nếu downstream không memoize, đừng dùng — chỉ tốn cost.
- **Selector pattern** (Redux/Zustand): combine `memoizeOne` + pure selector → tránh re-compute khi state phần khác thay đổi.
- **Immer trong Redux Toolkit** đã là default cho `createSlice` → viết mutable, ra immutable. Trade-off: bundle ~3KB gzipped + một lớp Proxy.
- **`Object.freeze` ở dev mode** giúp catch accidental mutation (Redux Toolkit có `freezeOptions`). Production tắt vì cost.
- **Strict mode (React)** gọi reducer/initializer/effect 2 lần để phát hiện impurity → pure function là *điều kiện cần*.
- **Suspense + cache**: React Server Component fetcher cần pure để cache deduplicate hoạt động.
- **HOC vs hooks**: hooks là composition tốt hơn HOC vì không bị wrapper hell và ref forwarding.

---

## ⚠️ 6. Common Pitfalls

- ❌ **IIFE trong code app hiện đại** — gần như luôn có cách viết tốt hơn bằng module + `const`.
- ❌ **Quên `()` cuối IIFE**: `(function () {})` chỉ là expression, không gọi.
- ❌ **"Pure function" nhưng vẫn `console.log`**: log là side effect — chấp nhận được khi debug, không ổn trong production hot path.
- ❌ **`Object.freeze` rồi tưởng là deep immutable** — chỉ freeze level 1.
- ❌ **Spread shallow rồi mutate nested**: `{ ...state, user: state.user }` rồi `state.user.age = 26` → vẫn mutate gốc.
- ❌ **`JSON.stringify(args)` làm cache key**: function args, `Symbol`, `Map`/`Set`, `Date`, `undefined`, `NaN`, circular ref → hoặc throw hoặc tạo key trùng → cache sai. Cho complex args, dùng `WeakMap` theo từng arg object.
- ❌ **Memoize mãi mãi → memory leak**: cache không evict. Dùng `WeakMap` (auto-GC theo object) hoặc LRU (`lru-cache`, `quick-lru`).
- ❌ **`useMemo` cho mọi thứ**: cost deps compare > giá trị compute nhỏ → âm tính.
- ❌ **Tin tail-call optimization**: V8 chưa support. Recursion > ~10k call vẫn vỡ stack.
- ❌ **Currying làm "đẹp"** nhưng giết TypeScript inference. Closure trực tiếp thường type-safe hơn.
- ❌ **Import cả Ramda** `import * as R from 'ramda'` → bundle phình. Dùng named import + tree-shakable build.
- ⚠️ **Reduce thay thế for-loop mọi nơi**: với array lớn + transform nặng, vòng `for` thường nhanh hơn 2-3x. Tối ưu khi profile chỉ ra hot path.
- ⚠️ **Immer trong cực-hot path** (60fps animation): proxy có cost — đo trước khi áp.

---

## ✅ 7. Decision Guide

**Khi nào dùng IIFE?**

- ✅ Bundler output / UMD wrapper.
- ✅ Async init khi target chưa có top-level await.
- ❌ Tạo private scope trong app code → dùng module + `const`.

**Khi nào dùng FP style?**

- ✅ Data transform (selector, normalizer, formatter).
- ✅ State update (Redux, Zustand).
- ✅ Test-heavy business logic.
- ⚠️ Hot path 60fps / 10k+ items → cân nhắc imperative + measure.

**Memoization checklist:**

- [ ] Function thực sự **pure**?
- [ ] Args **stable reference** (không re-create mỗi render)?
- [ ] Cache có **size limit** hoặc dùng `WeakMap`?
- [ ] Key serialization an toàn (không function/Date/circular)?
- [ ] Profile xác nhận có win — không "tối ưu vì cảm tính"?

**Immutability checklist:**

- [ ] Update tạo reference mới ở **mọi level bị thay đổi**?
- [ ] Reference của subtree không đổi giữ nguyên (structural sharing)?
- [ ] Test có check identity (`===`) chứ không chỉ deep equal?
- [ ] Dev mode freeze để catch mutation?

**Composition vs Inheritance:**

- Cần share behavior → composition (hook / mixin / function).
- IS-A rõ ràng + ổn định → inheritance OK.
- React: gần như luôn composition (hooks, slots).

---

## 💬 8. Short Interview Answer

> Em nghĩ IIFE giờ trên app code mới không còn cần nhiều, vì ES modules với `const`/`let` đã thay được hầu hết use case private scope. Em chỉ còn thấy IIFE trong **output của bundler** (Webpack/Rollup wrap bundle trong IIFE để không leak global), trong **async bootstrap** khi target chưa có top-level await, hoặc trong **inline script** kiểu analytics.
>
> Còn Functional Programming trên FE thì em coi như một bộ nguyên tắc: **pure function + immutability + composition**. Cái nó cho mình quan trọng nhất là **reference equality** — nó là cách `React.memo`, `useMemo`, `Object.is` hoạt động. Em hay phân biệt 2 thứ hay bị nhầm: một là `useMemo` không phải `memoize` — nó chỉ cache 1 giá trị giữa các render thôi, không phải `args → result` map. Hai là currying và partial application khác nhau — currying luôn unary, partial chỉ cố định một số args.
>
> Em ưu tiên `pipe` hơn `compose` vì đọc theo thứ tự data flow tự nhiên hơn. Với deep nested state, em chọn **Immer** thay spread tay vì code rõ hơn, lại có structural sharing giữ reference equality cho subtree không đổi. Còn memoization thì em luôn để ý 3 thứ: key serialization, cache eviction, và là profile xác nhận có win — không tối ưu vì cảm tính. Với recursion, em nhớ V8 không có tail-call optimization nên deep recursion ~10k call là vỡ stack, lúc đó em đổi sang iterative hoặc trampoline.

---

**📌 Ghi nhớ nhanh:**

- 🎯 **IIFE**: `(fn)()` — giờ chủ yếu là pattern cho bundler/async init, không cho app code.
- 🔥 **Pure**: referential transparency — same input → same output, no side effect.
- 🛡️ **Immutable**: tạo reference mới ở path thay đổi → React.memo / Object.is hoạt động.
- 🔄 **HOF / curry / partial**: tách config khỏi data; curry luôn unary, partial thì không.
- 🔗 **Compose vs Pipe**: pipe đọc theo data flow, ưu tiên trong code app.
- 💾 **Memoize**: nhớ key + eviction + profile. `useMemo` ≠ `memoize`.
- 🔁 **Recursion**: JS không TCO — deep recursion stack overflow.
- ⚛️ **Composition over inheritance**: hooks/slots > HOC/subclass.
- 📚 **Ramda / lodash-fp**: auto-curry + data-last; cẩn thận tree-shaking.
