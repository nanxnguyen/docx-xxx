# ⚙️ Topic 04 — Async/Await vs Promises vs Callbacks & Promise.all/any/race/allSettled

> Scope: tiến hoá async (callback → Promise → async/await), 4 combinator, microtask, cancellation, retry/backoff, circuit breaker, concurrency control, sequential vs parallel, async iterator, race condition.

## ⭐ 1. Senior/Staff Summary

> 3 model async: **callback → Promise → async/await**. Mỗi bước giải quyết vấn đề của bước trước: callback hell → `.then()` chain → sync-like flow với `try/catch`. `async/await` chỉ là **syntactic sugar trên Promise**, chạy ở **microtask queue** → trước macrotask (`setTimeout`).

Senior cần phân biệt được **fail-fast vs partial fail** (all vs allSettled), biết khi nào dùng **AbortController** (cancellation chuẩn web hiện đại), biết **race condition** xảy ra khi response về không đúng thứ tự (search box kinh điển), và biết **concurrency control** quan trọng hơn `Promise.all` raw cho large batch — không thì DDoS server của mình.

---

## 🧠 2. Key Mental Model

- **`async` function luôn return `Promise`**. Throw bên trong = `Promise.reject`. Return bên trong = `Promise.resolve`.
- **`await` pause function** đó, không phải toàn bộ thread. Phần code sau `await` đưa vào microtask queue khi Promise settle.
- **Microtask > Macrotask**: Promise callback + phần sau `await` chạy **trước** mọi `setTimeout`.
- **Promise có 3 state, settle 1 lần**: pending → fulfilled | rejected. Không reverse, không đổi value.
- **Combinator chia 2 cặp**: `all`/`allSettled` chờ hết; `race`/`any` chờ 1.
  - `all`: 1 reject → reject ngay (fail-fast). `allSettled`: không bao giờ reject.
  - `race`: settle đầu tiên thắng (kể cả reject). `any`: fulfilled đầu tiên thắng, all reject → `AggregateError`.
- **Promise không cancel được native**. Cancel = AbortController + signal (fetch/axios) hoặc cờ "stale request" ngoài Promise.
- **Race condition** không phải Promise issue — là issue **thứ tự response**. Fix bằng request ID guard hoặc AbortController.

---

## 📚 3. Main Concepts

### 3.1. Tiến hoá: Callback → Promise → async/await

```ts
// Callback — hell
fetchUser(id, (err, user) => {
  if (err) return handleError(err);
  fetchPosts(user.id, (err, posts) => {
    if (err) return handleError(err);
    fetchComments(posts[0].id, (err, comments) => { /* deep nested */ });
  });
});

// Promise — chain
fetchUser(id)
  .then(user => fetchPosts(user.id))
  .then(posts => fetchComments(posts[0].id))
  .catch(handleError);

// async/await — sync-like
try {
  const user = await fetchUser(id);
  const posts = await fetchPosts(user.id);
  const comments = await fetchComments(posts[0].id);
} catch (err) { handleError(err); }
```

| | Callback | Promise | async/await |
|---|---|---|---|
| Composition | Nested | `.then` chain | Linear |
| Error | If/else mỗi tầng | `.catch()` | `try/catch` |
| Loop / branch | Phức tạp | Vẫn khá phức tạp | Tự nhiên |
| Lịch sử | Pre-ES6 | ES6 | ES2017+ |

### 3.2. Promise — 3 state, settle once

```ts
const p = new Promise<number>((resolve, reject) => {
  setTimeout(() => resolve(42), 1000);
});
// pending → fulfilled (resolve) | rejected (reject)
// Settle 1 lần, sau đó immutable
```

⚠️ Anti-pattern: **Promise constructor wrapper** quanh Promise đã có:

```ts
// ❌ Vô nghĩa, mất stack trace, dễ nuốt lỗi
return new Promise((res, rej) => fetch(url).then(res).catch(rej));
// ✅ Chỉ return Promise
return fetch(url);
```

### 3.3. async/await — sync-like nhưng KHÔNG block thread

```ts
async function loadUser(id: string) {
  const user = await fetchUser(id);   // pause loadUser, không block event loop
  return user;                         // tự wrap thành Promise.resolve(user)
}
// Throw trong async function = Promise.reject
```

**Top-level await (ES2022, ES Modules):**

```ts
// ES modules
const config = await fetch('/config.json').then(r => r.json());
// ⚠️ Block module graph phụ thuộc → cẩn thận ở entry point
```

### 3.4. Microtask order

```ts
console.log('A');
setTimeout(() => console.log('B'), 0);
Promise.resolve().then(() => console.log('C'));
(async () => { await null; console.log('D'); })();
console.log('E');
// Output: A E C D B
```

→ Promise `.then` + phần sau `await` là **microtask**, drain hết trước macrotask `setTimeout`.

### 3.5. 4 Promise combinators

| API | Kết quả | Khi reject | Use case |
|---|---|---|---|
| `Promise.all` | Array kết quả theo thứ tự input | 1 reject → reject ngay (fail-fast) | Mọi task bắt buộc OK |
| `Promise.allSettled` | Array `{status, value/reason}` | Không bao giờ | Dashboard chấp nhận partial fail |
| `Promise.race` | Settle đầu tiên (fulfilled hoặc rejected) | Reject nếu đầu tiên reject | Timeout, fastest source |
| `Promise.any` | Fulfilled đầu tiên | All reject → `AggregateError` | Fallback nhiều nguồn |
| `Promise.withResolvers` (ES2024) | `{promise, resolve, reject}` | — | Defer pattern, manual settle |

```ts
// allSettled cho dashboard
const [posts, follows, perms] = await Promise.allSettled([
  fetchPosts(), fetchFollows(), fetchPerms(),
]);
posts.status === 'fulfilled' ? renderPosts(posts.value) : showWidgetError();

// any — fallback CDN
const data = await Promise.any([
  fetch('https://cdn1/data'),
  fetch('https://cdn2/data'),
  fetch('https://cdn3/data'),
]);
```

### 3.6. Sequential vs Parallel

```ts
// ❌ Sequential khi không cần phụ thuộc — chậm gấp nhiều lần
const user = await fetchUser();
const posts = await fetchPosts();
const perms = await fetchPerms();

// ✅ Parallel khi độc lập
const [user, posts, perms] = await Promise.all([
  fetchUser(), fetchPosts(), fetchPerms(),
]);

// ✅ Mixed — bước 1 phụ thuộc, bước 2 song song
const user = await fetchUser();
const [posts, follows] = await Promise.all([
  fetchPosts(user.id), fetchFollows(user.id),
]);
```

### 3.7. Cancellation — AbortController

```ts
const controller = new AbortController();
const data = await fetch('/api/data', { signal: controller.signal });
controller.abort();                    // throw AbortError ở fetch đang chờ

// Timeout chuẩn web hiện đại (Node 17.3+, browser modern)
const data2 = await fetch('/api/data', { signal: AbortSignal.timeout(5000) });

// Combine signals (Node 20+, browser 2023+)
const combined = AbortSignal.any([userController.signal, AbortSignal.timeout(5000)]);
```

> 💡 Promise native **không có cancel**. AbortController là chuẩn web cho cancel. Axios, React Query, fetch đều support.

### 3.8. Race condition trong search/autocomplete

```ts
// ❌ Response về không đúng thứ tự → stale result ghi đè current
async function onSearch(term: string) {
  const results = await fetch(`/api/search?q=${term}`).then(r => r.json());
  setResults(results);                 // có thể là kết quả của term cũ
}

// ✅ Fix 1: request ID guard
let reqId = 0;
async function onSearch(term: string) {
  const id = ++reqId;
  const results = await fetch(`/api/search?q=${term}`).then(r => r.json());
  if (id === reqId) setResults(results);
}

// ✅ Fix 2: AbortController — tốt hơn vì hủy luôn request cũ (tiết kiệm bandwidth)
let controller: AbortController | undefined;
async function onSearch(term: string) {
  controller?.abort();
  controller = new AbortController();
  try {
    const r = await fetch(`/api/search?q=${term}`, { signal: controller.signal });
    setResults(await r.json());
  } catch (e: any) {
    if (e.name !== 'AbortError') throw e;
  }
}
```

> 🔥 Trong React: dùng React Query / SWR — chúng tự handle stale request, cancellation, retry.

### 3.9. Retry với exponential backoff + jitter

```ts
async function retry<T>(
  fn: () => Promise<T>,
  { max = 3, baseMs = 500, shouldRetry = () => true } = {},
): Promise<T> {
  let lastErr: unknown;
  for (let i = 0; i <= max; i++) {
    try { return await fn(); }
    catch (e) {
      lastErr = e;
      if (i === max || !shouldRetry(e)) break;
      const delay = baseMs * 2 ** i * (0.5 + Math.random()); // jitter để tránh thundering herd
      await new Promise(r => setTimeout(r, delay));
    }
  }
  throw lastErr;
}

// Chỉ retry network / 5xx, KHÔNG retry 4xx
const data = await retry(
  () => fetch('/api/data').then(r => { if (!r.ok) throw r; return r.json(); }),
  { shouldRetry: (e: any) => e.status === undefined || e.status >= 500 },
);
```

> 💡 **Jitter** quan trọng — exponential backoff thuần khiến tất cả client retry đồng bộ → thundering herd làm server gãy thêm.

### 3.10. Concurrency limit (KHÔNG dùng `Promise.all` raw cho 1000 task)

```ts
// ❌ Promise.all 1000 task = 1000 connection đồng thời → DDoS chính mình
await Promise.all(items.map(processItem));

// ✅ Pattern p-limit / pool
async function pLimit<T, R>(items: T[], limit: number, fn: (t: T) => Promise<R>) {
  const results: R[] = new Array(items.length);
  let i = 0;
  const workers = Array.from({ length: limit }, async () => {
    while (i < items.length) {
      const idx = i++;
      results[idx] = await fn(items[idx]);
    }
  });
  await Promise.all(workers);
  return results;
}

await pLimit(items, 10, processItem);  // tối đa 10 concurrent
```

Thư viện: **`p-limit`**, **`p-queue`**, **`p-map`** (Sindre Sorhus). Đáng dùng hơn tự code.

### 3.11. Circuit Breaker (ý tưởng)

3 state: **CLOSED** (bình thường) → **OPEN** (đã ngắt sau N fail) → **HALF_OPEN** (sau timeout, thử lại 1 call).

> 💡 Trên FE ít tự implement — thường để API gateway / backend handle. Hữu ích khi client gọi nhiều micro-service trực tiếp (BFF pattern). Lib: `opossum`, `cockatiel`.

### 3.12. Async Iterator — stream large data

```ts
async function* paginate<T>(url: string, size = 100) {
  for (let page = 0; ; page++) {
    const res = await fetch(`${url}?page=${page}&size=${size}`);
    const items: T[] = await res.json();
    if (items.length === 0) return;
    yield* items;
  }
}

for await (const user of paginate<User>('/api/users')) {
  await processUser(user);            // chỉ 1 user trong memory tại một thời điểm
}
```

Phù hợp khi: pagination, streaming response, log tail, file chunks, server-sent events.

### 3.13. forEach + async — pitfall #1

```ts
// ❌ forEach KHÔNG await — items.forEach trả undefined, không phải Promise
items.forEach(async item => { await processItem(item); });
// → function trả về undefined ngay, các Promise inner chạy parallel không kiểm soát

// ✅ Sequential
for (const item of items) await processItem(item);

// ✅ Parallel (cẩn thận concurrency)
await Promise.all(items.map(processItem));
```

---

## 🛠 4. Practical TypeScript Examples

### 4.1. Timeout wrapper tái sử dụng

```ts
async function withTimeout<T>(p: Promise<T>, ms: number, message = 'Timeout'): Promise<T> {
  return Promise.race([
    p,
    new Promise<never>((_, rej) => setTimeout(() => rej(new Error(message)), ms)),
  ]);
}
// Hoặc tốt hơn — AbortSignal.timeout cho fetch
fetch('/api/data', { signal: AbortSignal.timeout(5000) });
```

### 4.2. `Promise.allSettled` cho dashboard chấp nhận partial fail

```ts
type WidgetData = { posts: Post[]; perms: Perm[]; followers: number };

async function loadDashboard(uid: string): Promise<Partial<WidgetData>> {
  const [posts, perms, followers] = await Promise.allSettled([
    fetchPosts(uid), fetchPerms(uid), fetchFollowers(uid),
  ]);
  return {
    posts:     posts.status     === 'fulfilled' ? posts.value     : undefined,
    perms:     perms.status     === 'fulfilled' ? perms.value     : undefined,
    followers: followers.status === 'fulfilled' ? followers.value : undefined,
  };
}
```

### 4.3. AbortController + React `useEffect`

```ts
useEffect(() => {
  const controller = new AbortController();
  fetch(`/api/users/${id}`, { signal: controller.signal })
    .then(r => r.json())
    .then(setUser)
    .catch(e => { if (e.name !== 'AbortError') setError(e); });
  return () => controller.abort();   // ✅ cleanup khi unmount / id đổi
}, [id]);
```

### 4.4. `error.cause` (ES2022) — preserve stack

```ts
async function fetchJSON(url: string) {
  try { return await fetch(url).then(r => r.json()); }
  catch (cause) {
    throw new Error(`fetchJSON failed: ${url}`, { cause });   // giữ original error
  }
}
```

### 4.5. `Promise.withResolvers` (ES2024) — defer pattern

```ts
const { promise, resolve, reject } = Promise.withResolvers<User>();
// Trao resolve/reject cho code khác (event handler, callback)
button.addEventListener('click', () => resolve(currentUser), { once: true });
const user = await promise;
```

---

## ⚛️ 5. Production Notes / React Implications

- **Trong `useEffect`**: KHÔNG truyền function async trực tiếp — return value của effect phải là cleanup function, không phải Promise. Wrap inner async function.
- **AbortController trong cleanup**: hủy fetch khi component unmount / deps đổi — tránh "set state on unmounted component" warning + memory leak.
- **React Query / SWR / TanStack Query**: giải quyết hầu hết case async trên FE — cache, dedupe, race condition guard, retry, refetch on focus. Tự code chỉ khi không thể.
- **Suspense + React 19 `use()`**: framework-level pattern cho async data — pause render đến khi data sẵn sàng.
- **`Promise.allSettled` thường hợp dashboard hơn `Promise.all`** — 1 widget fail không nên đánh sập cả page.
- **Top-level `await`** trong route module có thể block bundle execution → tăng TTFB. Cẩn thận ở entry point.
- **Server Components**: async function = component có `await` trực tiếp, không cần `useEffect` cho data fetching.
- **WebSocket / EventSource**: cleanup chính là `close()` trong return của effect — quên = memory leak + zombie connection.
- **Form submit double-click**: disable button hoặc dedupe Promise (ref tới in-flight Promise).

---

## ⚠️ 6. Common Pitfalls

- ❌ **Quên `await`**: `const user = fetchUser()` → `user` là `Promise`, `.name` = `undefined`.
- ❌ **`forEach(async ...)`**: forEach trả `undefined`, không đợi gì → các Promise inner chạy không kiểm soát.
- ❌ **`Promise.all` cho 1000+ task**: DDoS chính server mình. Dùng `p-limit` / pool / batch.
- ❌ **Promise constructor wrapper**: `new Promise((res, rej) => fetch().then(res).catch(rej))` — vô nghĩa, mất stack, dễ nuốt lỗi.
- ❌ **Mất `await` trong `try`**: `try { return fetchUser(); } catch...` → catch KHÔNG bắt được reject. Phải `return await`.
- ❌ **Unhandled promise rejection**: `.catch()` hoặc `try/catch` mọi async path. Log `unhandledrejection` event ở global.
- ❌ **`||` cho default trong async chain** khi `0`/`''`/`false` hợp lệ — dùng `??`.
- ❌ **Race condition trong search**: response cũ ghi đè current. Dùng request ID guard hoặc AbortController.
- ❌ **Retry mọi error**: 4xx không nên retry (client lỗi). Chỉ retry network / 5xx / timeout.
- ❌ **Retry không có jitter**: thundering herd. Luôn `+ random()`.
- ❌ **Retry vô hạn**: set max — không thì DDoS server đang gãy.
- ❌ **Quên cleanup `setTimeout`/`setInterval`/`AbortController`** khi unmount/deps đổi → leak + bug logic.
- ❌ **`async` trong `useEffect` callback trực tiếp** → return value thành Promise, không phải cleanup function.
- ❌ **Async iterator + parallel processing**: `for await...of` là sequential. Muốn parallel thì combine với `pLimit`.
- ❌ **Top-level await trong entry data fetcher** → block module graph → TTFB tăng.
- ⚠️ **`Promise.race` reject khi đầu tiên reject** — dùng `Promise.any` nếu muốn "fulfilled đầu tiên thắng, bỏ qua reject".
- ⚠️ **Settle 1 lần**: gọi `resolve` lần 2 trong Promise constructor là no-op, không throw — silent bug.

---

## ✅ 7. Decision Guide / Checklist

**Chọn pattern theo phụ thuộc:**

- Tasks độc lập, đều phải OK → `Promise.all`.
- Tasks độc lập, chấp nhận partial fail → `Promise.allSettled`.
- Cần kết quả nhanh nhất (timeout / fastest source) → `Promise.race`.
- Có nhiều fallback, 1 cái OK là đủ → `Promise.any`.
- Tasks phụ thuộc nhau → sequential `await` hoặc `for...of`.
- Batch lớn → `pLimit` / `p-queue` / batched (10–50 concurrent).
- Stream / pagination → async iterator + `for await...of`.

**Checklist cho mọi async code path:**

- [ ] Có `try/catch` hoặc `.catch()` ở mỗi entry point?
- [ ] Có timeout (AbortSignal.timeout hoặc Promise.race)?
- [ ] Có retry logic cho transient failure (network/5xx) với jitter?
- [ ] Có giới hạn concurrency khi loop?
- [ ] Có cancellation khi user navigate đi / unmount?
- [ ] Có race condition guard cho search / autocomplete?
- [ ] Có cleanup cho `setTimeout`/`setInterval`/`AbortController`?
- [ ] React: dùng React Query / SWR thay vì tự code?
- [ ] Log `unhandledrejection` global cho monitoring?

**Sequential vs Parallel speed test (5 items × 1s):**

| Pattern | Speed | Server load | Order | Use case |
|---|---|---|---|---|
| `Promise.all` | ~1s | 🔥🔥🔥 (5 concurrent) | ❌ | Tasks độc lập, ít task |
| `for...of` | ~5s | ✅ (1 concurrent) | ✅ | Tasks phụ thuộc, rate-limited |
| `pLimit(2)` | ~3s | ⚡⚡ (2 concurrent) | Tuỳ impl | Cân bằng |
| Async iterator | ~5s | ✅ | ✅ | Stream, memory-bound |

---

## 💬 8. Short Interview Answer

> Em coi async/await là **syntactic sugar trên Promise** — không phải pattern khác. Function `async` luôn return Promise, `throw` trong đó tự thành reject, và phần code sau `await` chạy ở **microtask queue** nên luôn trước `setTimeout` macrotask.
>
> 4 combinator em chia 2 cặp: **`all`/`allSettled` chờ hết** — `all` fail-fast, `allSettled` không bao giờ reject; **`race`/`any` chờ 1** — `race` lấy cái settle đầu tiên kể cả reject, `any` lấy fulfilled đầu tiên. Trên dashboard em hay ưu tiên `allSettled` hơn `all` vì 1 widget fail không nên đánh sập cả page.
>
> Trên FE em luôn để ý 3 thứ: **cancellation** — Promise native không cancel được, em dùng AbortController với `fetch` và cleanup trong `useEffect`. **Race condition** — search/autocomplete dễ bị response cũ ghi đè current, fix bằng request ID guard hoặc AbortController. **Concurrency control** — `Promise.all` cho 1000 task là DDoS chính mình, em dùng `p-limit` hoặc batch 10–50 concurrent.
>
> Retry em luôn kèm **exponential backoff + jitter** để tránh thundering herd, và chỉ retry network/5xx chứ không retry 4xx. Pitfall em hay catch trong code review là `forEach(async)` — `forEach` không đợi gì cả nên các Promise chạy không kiểm soát; phải đổi sang `for...of` hoặc `Promise.all` tuỳ ý.
>
> Trong React em mặc định dùng **React Query / TanStack Query** — nó giải quyết cache, dedupe, race condition, retry, refetch on focus sẵn. Self-implement chỉ khi thực sự cần.

---

**📌 Ghi nhớ nhanh:**

- 🔥 **async/await** = sugar trên Promise; phần sau `await` = microtask.
- 📊 **Combinator**: `all` fail-fast | `allSettled` chờ hết | `race` đầu tiên | `any` fulfilled đầu tiên.
- 🛑 **Cancel** = AbortController + signal; React cleanup luôn dùng pattern này.
- 🏁 **Race condition** search/autocomplete → request ID guard hoặc AbortController.
- 🔁 **Retry**: exponential backoff + **jitter**, chỉ retry network/5xx, có max.
- ⛔ **Concurrency limit**: `pLimit` / `p-queue` cho large batch — không `Promise.all` raw.
- 🌊 **Stream lớn** → async iterator `for await...of`.
- 🚫 **forEach + async** không đợi gì → dùng `for...of` hoặc `Promise.all`.
- ⚛️ **React**: dùng React Query / SWR; `useEffect` cleanup với AbortController.
