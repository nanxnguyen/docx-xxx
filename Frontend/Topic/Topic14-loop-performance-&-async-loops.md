# 🔁 Topic14: Loop Performance & Async Loops

## ⭐ Senior/Staff Summary

> **Loop performance không chỉ là chọn syntax nhanh nhất. Senior cần nhìn theo 3 lớp: Big O, runtime behavior, và production constraints.**

- ⚡ **Ranking thường gặp**: `for` ≈ `while` > `for...of` > `forEach` / `map` / `filter` / `reduce` > `for...in`.
- 🧠 **Big O quan trọng hơn microbenchmark**: đổi `O(n²)` sang `Map` / `Set` thường đáng hơn tối ưu `for` vs `forEach`.
- ✅ `for` / `for...of`: hỗ trợ `break`, `continue`, `return`, phù hợp khi cần early exit hoặc control flow rõ.
- ⚠️ `forEach(async () => {})` là trap: callback async chạy nhưng outer function **không await**.
- 🚦 Async loop có 3 chiến lược chính: **sequential**, **parallel**, **batched/concurrency-limited**.
- 🧯 Production cần nghĩ thêm: error handling, rate limit, backpressure, cancellation, UI jank, React rendering, testing.

## 🧠 Key Mental Model

### 1. Đừng benchmark như chân lý tuyệt đối

Kết quả benchmark thay đổi theo:

- JavaScript engine: V8, SpiderMonkey, JavaScriptCore.
- Browser/device: desktop mạnh khác mobile yếu.
- Data shape: array đặc/sparse, object shape ổn định hay thay đổi.
- Workload thật: callback có I/O, allocation, DOM update, React render hay chỉ cộng số.
- JIT warm-up, GC, dev mode vs production mode.

💡 **Rule thực tế**: profile code thật trước. Nếu bottleneck là `O(n²)`, DOM reflow, network, hoặc React re-render thì đổi loop syntax thường không giải quyết đúng vấn đề.

### 2. Chọn loop theo control flow trước, performance sau

| Pattern | Nên dùng khi | Lưu ý |
|---|---|---|
| `for` | Hot path, cần index, large array, tối ưu allocation | Verbose hơn nhưng control tốt |
| `for...of` | Cần readable, iterate Array/Set/Map/String | Có iterator overhead nhỏ |
| `forEach` | Side effect đơn giản, không cần `break` | Không await outer flow, không early exit |
| `map/filter/reduce` | Transform immutable data | Tạo array/value mới, không dùng chỉ để side effect |
| `for...in` | Iterate object keys | Không dùng cho array |

### 3. Async loop là bài toán scheduling

- **Sequential**: chạy từng item, dễ kiểm soát order/rate/error.
- **Parallel**: chạy cùng lúc, nhanh nhưng dễ overload API/memory.
- **Batched / concurrency-limited**: cân bằng tốc độ và giới hạn tài nguyên.

## 📚 Main Concepts

### ⚡ Loop Performance & Ranking

**Ranking tham khảo, không tuyệt đối:**

1. `for`: thường nhanh nhất vì truy cập index trực tiếp, ít abstraction.
2. `for...of`: readable, hỗ trợ iterable, có iterator protocol overhead.
3. `forEach`: callback overhead mỗi item, không early exit.
4. `map/filter/reduce`: callback overhead + có thể tạo intermediate array.
5. `for...in`: duyệt enumerable keys, có thể đi qua prototype chain, chậm và sai mục đích với array.

```typescript
const prices = [101, 102, 103, 104];

// Hot path: cần index, có thể cache length nếu array không đổi trong loop.
for (let i = 0, len = prices.length; i < len; i++) {
  prices[i] = prices[i] * 1.01;
}

// Readable: tốt cho phần lớn business logic.
for (const price of prices) {
  console.log(price);
}

// Transform immutable data.
const adjustedPrices = prices.map((price) => price * 1.01);
```

⚠️ **Cache length** chỉ đáng quan tâm trong hot path lớn và array không bị mutate length trong loop. Trong code bình thường, readability và correctness quan trọng hơn.

### 🔀 `break`, `continue`, `return`

```typescript
function findFirstLargeOrder(orderIds: string[], limit: number): string | null {
  for (const id of orderIds) {
    if (id.startsWith("test_")) continue; // skip iteration hiện tại
    if (Number(id) > limit) return id; // thoát function
  }

  return null;
}

for (const id of ["1", "2", "3"]) {
  if (id === "2") break; // thoát loop
}
```

Với `forEach`, `return` chỉ thoát callback hiện tại, **không thoát outer function**:

```typescript
function hasBlockedSymbol(symbols: string[]): boolean {
  symbols.forEach((symbol) => {
    if (symbol === "GME") {
      return true; // ❌ chỉ return khỏi callback, function vẫn chạy tiếp
    }
  });

  return false;
}

function hasBlockedSymbolBetter(symbols: string[]): boolean {
  return symbols.some((symbol) => symbol === "GME"); // ✅ early exit semantic
}
```

### 🔑 `for...in` cho object, không cho array

```typescript
const config = { theme: "dark", locale: "vi" };

for (const key in config) {
  if (Object.prototype.hasOwnProperty.call(config, key)) {
    console.log(key, config[key as keyof typeof config]);
  }
}

const ids = ["a", "b"];

for (const index in ids) {
  console.log(index); // "0", "1" là string key, không phải value
}
```

✅ Với object hiện đại, thường rõ hơn khi dùng `Object.keys`, `Object.entries`, hoặc type-safe helper.

### 🧮 `map`, `filter`, `reduce`

Use đúng semantic:

- `map`: mỗi input tạo một output.
- `filter`: giữ/bỏ item.
- `reduce`: gom thành một value/object/map.
- `forEach`: side effect, không tạo value mới.

```typescript
type Order = {
  id: string;
  symbol: string;
  quantity: number;
  status: "open" | "filled" | "cancelled";
};

const openSymbols = orders
  .filter((order) => order.status === "open")
  .map((order) => order.symbol);

const totalQuantity = orders.reduce(
  (total, order) => total + order.quantity,
  0
);
```

⚠️ Tránh chain quá nhiều bước trên dataset lớn nếu tạo nhiều intermediate arrays. Có thể gom bằng `for...of` hoặc `reduce` khi đã profile thấy cần.

### 🔥 O(n²) -> `Map` / `Set`

Đây là tối ưu senior quan trọng hơn tranh luận `for` vs `forEach`.

```typescript
type User = { id: string; name: string };
type Position = { userId: string; symbol: string; quantity: number };

// ❌ O(users * positions)
function attachPositionsSlow(users: User[], positions: Position[]) {
  return users.map((user) => ({
    ...user,
    positions: positions.filter((position) => position.userId === user.id),
  }));
}

// ✅ O(users + positions)
function attachPositionsFast(users: User[], positions: Position[]) {
  const positionsByUser = new Map<string, Position[]>();

  for (const position of positions) {
    const group = positionsByUser.get(position.userId) ?? [];
    group.push(position);
    positionsByUser.set(position.userId, group);
  }

  return users.map((user) => ({
    ...user,
    positions: positionsByUser.get(user.id) ?? [],
  }));
}
```

Với membership check:

```typescript
const blockedSymbols = new Set(["GME", "AMC"]);
const safeOrders = orders.filter((order) => !blockedSymbols.has(order.symbol));
```

## 🧪 Practical Examples

### ⚠️ Async `forEach` trap

```typescript
async function fetchRiskScore(order: Order): Promise<number> {
  const response = await fetch(`/api/risk/${order.id}`);
  if (!response.ok) throw new Error(`Risk API failed: ${order.id}`);
  return response.json() as Promise<number>;
}

async function bad(orders: Order[]) {
  orders.forEach(async (order) => {
    await fetchRiskScore(order);
  });

  console.log("done"); // ❌ chạy trước khi các request hoàn tất
}
```

### ✅ Sequential: đúng khi có dependency hoặc cần rate control

```typescript
async function validateOrdersSequential(orders: Order[]) {
  const results: Array<{ orderId: string; score: number }> = [];

  for (const order of orders) {
    try {
      const score = await fetchRiskScore(order);
      results.push({ orderId: order.id, score });
    } catch (error) {
      console.error("Risk check failed", { orderId: order.id, error });
      continue;
    }
  }

  return results;
}
```

Use khi:

- Request sau phụ thuộc request trước.
- API có rate limit thấp.
- Cần stop/continue theo từng lỗi.
- Cần giữ order xử lý rõ ràng.

### 🚀 Parallel: `Promise.all`

```typescript
async function validateOrdersParallel(orders: Order[]) {
  const scores = await Promise.all(
    orders.map(async (order) => ({
      orderId: order.id,
      score: await fetchRiskScore(order),
    }))
  );

  return scores;
}
```

`Promise.all`:

- ✅ Nhanh cho các tác vụ độc lập.
- ✅ Kết quả trả về theo thứ tự input.
- ⚠️ Fail-fast: chỉ cần một promise reject thì `Promise.all` reject.
- ⚠️ Không phù hợp khi list rất lớn hoặc API có rate limit.

### 🛡️ Partial failure: `Promise.allSettled`

```typescript
async function validateOrdersSafe(orders: Order[]) {
  const settled = await Promise.allSettled(
    orders.map((order) => fetchRiskScore(order))
  );

  return settled.map((result, index) => {
    const order = orders[index];

    if (result.status === "fulfilled") {
      return { orderId: order.id, ok: true, score: result.value };
    }

    return { orderId: order.id, ok: false, reason: result.reason };
  });
}
```

Use khi UI cần hiển thị kết quả từng item: một order lỗi không làm mất toàn bộ danh sách.

### 🚦 Batched / concurrency-limited

Batch đơn giản:

```typescript
async function validateOrdersBatched(orders: Order[], batchSize = 5) {
  const results: Awaited<ReturnType<typeof validateOrdersSafe>> = [];

  for (let i = 0; i < orders.length; i += batchSize) {
    const batch = orders.slice(i, i + batchSize);
    const batchResults = await validateOrdersSafe(batch);
    results.push(...batchResults);
  }

  return results;
}
```

Concurrency limit tự viết gọn:

```typescript
async function mapWithConcurrency<T, R>(
  items: T[],
  limit: number,
  task: (item: T, index: number) => Promise<R>
): Promise<R[]> {
  const results = new Array<R>(items.length);
  let nextIndex = 0;

  async function worker() {
    while (nextIndex < items.length) {
      const currentIndex = nextIndex++;
      results[currentIndex] = await task(items[currentIndex], currentIndex);
    }
  }

  const workers = Array.from(
    { length: Math.min(limit, items.length) },
    () => worker()
  );

  await Promise.all(workers);
  return results;
}

const scores = await mapWithConcurrency(orders, 5, fetchRiskScore);
```

💡 Production thường dùng thư viện như `p-limit`, queue nội bộ, hoặc API client có rate limiter để xử lý retry/backoff/backpressure tốt hơn.

### 🧯 Cancellation với `AbortController`

```typescript
async function fetchRiskScoreWithSignal(
  order: Order,
  signal: AbortSignal
): Promise<number> {
  const response = await fetch(`/api/risk/${order.id}`, { signal });
  if (!response.ok) throw new Error(`Risk API failed: ${order.id}`);
  return response.json() as Promise<number>;
}

const controller = new AbortController();
const cancel = () => controller.abort();

try {
  const scores = await Promise.all(
    orders.map((order) => fetchRiskScoreWithSignal(order, controller.signal))
  );
  console.log(scores);
} catch (error) {
  if (error instanceof DOMException && error.name === "AbortError") {
    console.log("Request cancelled");
  } else {
    throw error;
  }
}

// UI event hoặc cleanup có thể gọi cancel().
```

Trong UI, cancellation giúp tránh update state sau khi component unmount hoặc query cũ về muộn hơn query mới.

### 🌊 Async iterable vs array of promises

```typescript
async function* streamOrders() {
  for (const id of ["1", "2", "3"]) {
    const response = await fetch(`/api/orders/${id}`);
    yield response.json() as Promise<Order>;
  }
}

for await (const order of streamOrders()) {
  console.log(order); // xử lý từng item khi stream yield
}
```

- `for await...of` hợp với `AsyncIterable`: stream, cursor pagination, generator, readable stream.
- `Promise.all(items.map(...))` hợp với array hữu hạn các tác vụ độc lập.
- `for await...of` trên array promise sẽ await theo iteration order; nếu muốn aggregate parallel rõ ràng, dùng `Promise.all`.

## ⚛️ Production / React Notes

### 🖥️ UI jank và main thread

Loop đồng bộ lớn có thể block main thread, làm UI lag, input delay, animation drop frame.

Giải pháp theo mức độ:

- ✅ Giảm complexity trước: `Map`, `Set`, index data, pagination, virtualization.
- ✅ Chia nhỏ việc: chunk bằng `setTimeout`, `requestIdleCallback` khi task không gấp.
- ✅ Dùng Web Worker cho CPU-heavy work: parsing lớn, risk calculation local, report generation.
- ✅ Tránh DOM read/write xen kẽ trong loop để không gây layout thrashing.

```typescript
async function processInChunks<T>(
  items: T[],
  chunkSize: number,
  process: (item: T) => void
) {
  for (let i = 0; i < items.length; i += chunkSize) {
    const chunk = items.slice(i, i + chunkSize);
    for (const item of chunk) process(item);

    await new Promise<void>((resolve) => {
      window.setTimeout(resolve, 0);
    });
  }
}
```

### ⚛️ React implications

- ❌ Tránh `setState` nhiều lần trong loop nếu có thể tính xong rồi set một lần.
- ✅ Với list lớn: normalize data bằng `Map`/object, dùng pagination hoặc virtualization.
- ✅ `useMemo` chỉ dùng khi computation thật sự đắt và dependency ổn định.
- ✅ Trong `useEffect`, luôn xử lý race condition/cancellation cho async loop.
- ⚠️ `map` trong JSX là bình thường; vấn đề thường là key không ổn định, item component render nặng, hoặc tạo handler/object mới quá nhiều.

```typescript
function PositionsView({ positions }: { positions: Position[] }) {
  const positionsBySymbol = React.useMemo(() => {
    const map = new Map<string, Position[]>();

    for (const position of positions) {
      const group = map.get(position.symbol) ?? [];
      group.push(position);
      map.set(position.symbol, group);
    }

    return map;
  }, [positions]);

  return <div>{positionsBySymbol.size} symbols</div>;
}
```

Async effect với cancellation:

```typescript
React.useEffect(() => {
  const controller = new AbortController();

  async function run() {
    try {
      const results = await Promise.all(
        orders.map((order) =>
          fetchRiskScoreWithSignal(order, controller.signal)
        )
      );
      setScores(results);
    } catch (error) {
      if (!(error instanceof DOMException && error.name === "AbortError")) {
        setError(error);
      }
    }
  }

  run();

  return () => controller.abort();
}, [orders]);
```

### 🧪 Testing strategy

- Unit test pure transform: `map/filter/reduce`, `Map` grouping, edge cases empty/sparse/duplicate IDs.
- Test async behavior: sequential order, parallel completion, batched limit.
- Mock API reject để kiểm tra `Promise.all` fail-fast và `Promise.allSettled` partial failure.
- Test cancellation với `AbortController` và assert không update state sau unmount.
- Với performance-sensitive code: benchmark trong môi trường gần production, có warm-up, input đại diện, và đo bằng profiler.

## ⚠️ Common Pitfalls

- ❌ Tin rằng "`for` luôn là câu trả lời đúng". Nếu bottleneck là network hoặc `O(n²)`, đổi loop syntax không giúp nhiều.
- ❌ Dùng `forEach` với `async/await` rồi tưởng outer function đã chờ xong.
- ❌ Dùng `Promise.all` cho hàng nghìn request cùng lúc, gây rate limit, memory spike, hoặc backend overload.
- ❌ Không handle partial failure: một item lỗi làm hỏng toàn bộ UI.
- ❌ Dùng `for...in` cho array, nhận index dạng string và có rủi ro prototype keys.
- ❌ Dùng `map` chỉ để side effect; nên dùng `for...of` hoặc `forEach`.
- ❌ Nested loops không cần thiết: `users.map(...orders.filter(...))` trên data lớn.
- ❌ Loop CPU-heavy trong render React, làm render chậm và UI jank.
- ❌ Không cancellation async request khi user đổi filter/search hoặc component unmount.

## ✅ Decision Guide / Checklist

**Chọn sync loop:**

- Cần fastest hot path, index, mutate in place có kiểm soát → `for`.
- Cần readable, early exit, iterate iterable → `for...of`.
- Cần transform immutable → `map/filter/reduce`.
- Cần side effect đơn giản, không early exit → `forEach`.
- Cần object keys → `Object.entries` hoặc `for...in` kèm own-property check.

**Chọn async strategy:**

- Task phụ thuộc nhau, cần order, cần stop/continue từng bước → `for...of` + `await`.
- Task độc lập, số lượng nhỏ/vừa, muốn fail-fast → `Promise.all`.
- Task độc lập nhưng cần partial result → `Promise.allSettled`.
- Task nhiều, có rate limit/backpressure → batch hoặc concurrency limit.
- Task có thể bị user hủy → `AbortController`.
- Data đến theo stream/cursor → `for await...of`.

**Trước khi tối ưu:**

- Đã biết Big O chưa?
- Có nested loop nào đổi được sang `Map`/`Set` không?
- Bottleneck là CPU, DOM, React render, network, hay backend?
- Có profile trên device/browser mục tiêu chưa?
- Có test lỗi, cancellation, retry/rate-limit chưa?

## 🗣️ Short Interview Answer

Em nghĩ với loop performance thì không nên trả lời kiểu "`for` luôn nhanh nhất" rồi dừng ở đó. Theo em, `for` thường nhanh nhất trong hot path vì ít overhead, `for...of` readable và vẫn có `break/continue`, còn `forEach`, `map`, `filter`, `reduce` hợp khi semantic rõ ràng như side effect hoặc transform data. `for...in` thì em chỉ dùng cho object keys, không dùng cho array.

Điểm quan trọng hơn là Big O và runtime behavior. Nếu đang có nested loop `O(n²)`, em sẽ ưu tiên đổi sang `Map` hoặc `Set` trước khi micro-optimize syntax. Với async loop, em tránh `forEach(async ...)` vì outer flow không await. Nếu cần chạy tuần tự thì dùng `for...of await`, nếu các task độc lập thì dùng `Promise.all`, nếu cần partial failure thì dùng `Promise.allSettled`, còn production thì thường cần batch hoặc concurrency limit để tránh rate limit và backpressure.

Trong frontend, em cũng nhìn thêm React và browser: loop lớn có thể block main thread, gây jank; request async cần cancellation bằng `AbortController`; computation nặng có thể cần chunking, virtualization, `useMemo` đúng chỗ hoặc Web Worker. Em thường chọn cách dễ đọc trước, đo bằng profiler khi có dấu hiệu bottleneck, rồi tối ưu đúng nguyên nhân.
