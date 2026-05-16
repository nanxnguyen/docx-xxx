# ⏹️ Q28: Cancellation, Concurrency & Retry, Race-condition

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"Cancellation dùng AbortController để hủy requests, Concurrency control giới hạn parallel tasks, Retry implement exponential backoff cho failed requests, Race condition guard đảm bảo response cũ không ghi đè state mới."**

**🔑 4 Pattern Chính:**
  
**1. Cancellation - AbortController:**

- `const controller = new AbortController(); fetch(url, {signal: controller.signal})`
- **`controller.abort()`** hủy request → throw `AbortError`
- Use case: User navigate away, timeout, duplicate requests
- Best practice: Lan truyền `signal` xuyên suốt async chain

**2. Concurrency Control - Semaphore Pattern:**

- **Giới hạn số tasks chạy đồng thời** (ví dụ: max 5 parallel requests)
- Pattern: Queue + counter, chờ slot trống để chạy task tiếp
- Use case: Rate limiting, prevent overload server/browser
- Libraries: `p-limit`, `p-queue` (production-ready)

**3. Retry - Exponential Backoff + Jitter:**

- **Retry lỗi tạm thời** (5xx, network errors), không retry 4xx
- Exponential backoff: `delay = baseDelay * 2^attempt` (100ms, 200ms, 400ms...)
- **Jitter** (random noise): tránh "thundering herd" (nhiều clients retry cùng lúc)
- Max attempts + total timeout để không retry vô hạn

**4. Race Condition - Last Request Wins / Ignore Stale Result:**

- Race condition xảy ra khi **nhiều async operations cùng cập nhật một state/resource**, nhưng thứ tự hoàn thành không giống thứ tự bắt đầu
- Ví dụ search: request `q=a` chậm hơn request `q=ab`, nhưng `q=a` về sau và ghi đè kết quả mới
- Cách xử lý: cancel request cũ, dùng `requestId/sequence`, check `signal.aborted`, hoặc để library như React Query/SWR quản lý stale data
- Nguyên tắc: chỉ request mới nhất được quyền commit state

**⚠️ Lỗi Thường Gặp:**

- Không cleanup AbortController khi unmount → memory leak
- Retry **mọi lỗi** (kể cả 4xx) → spam server, waste resources
- Concurrency limit quá thấp → chậm, quá cao → overload
- Không cancel previous search request → race condition (results out of order)
- Chỉ debounce nhưng không guard stale response → vẫn có thể bị request cũ ghi đè

**💡 Kiến Thức Senior:**

- **Idempotent requests**: Retry an toàn cho GET/PUT, cẩn thận với POST (dùng idempotency keys)
- **Circuit Breaker pattern**: Dừng hẳn requests sau N failures liên tiếp, chờ recover
- **`AbortSignal.timeout(ms)`** (native) thay `setTimeout + abort`
- **Stale-While-Revalidate**: Return cached data ngay, fetch mới background, update sau
- **Last-write-wins vs last-request-wins**: Với UI search/filter thường cần last-request-wins, không phải request nào về sau thì thắng
- React Query/SWR **built-in** retry + cancellation + concurrency control

**Trả lời:**

- Hủy bỏ: `AbortController/AbortSignal` cho fetch/task dài; truyền `signal` xuyên suốt để hủy chuỗi async.
- Giới hạn đồng thời: dùng semaphore/pool để kiểm soát số tác vụ chạy song song, tránh nghẽn băng thông hay quota.
- Retry: áp dụng backoff + jitter cho lỗi tạm thời, kèm tổng timeout để không treo vô hạn.
- Race condition: bảo đảm chỉ async result còn hợp lệ mới được cập nhật state, thường bằng cancel request cũ hoặc request id.

Hoạt động:

- Abort: `controller.abort()` phát tín hiệu; fetch/reader/listener có `signal` sẽ throw DOMException('AbortError') và dừng sớm.
- Concurrency: hàng đợi đợi slot trống; xong 1 tác vụ thì phát tín hiệu cho tác vụ kế.
- Retry: vòng lặp bắt lỗi, đợi theo backoff (exponential + jitter), dừng khi đạt số lần tối đa.
- Race condition: mỗi request có "phiên bản"; khi response về, so với phiên bản hiện tại trước khi commit state.

Ưu điểm:

- Chủ động dừng tác vụ thừa (chuyển trang, đóng modal).
- Giảm tải server/trình duyệt, tránh bão request.
- Tăng độ tin cậy khi mạng không ổn định.
- Tránh UI hiển thị dữ liệu cũ dù user đã chọn filter/query mới.

Nhược điểm:

- Cần lan truyền `signal` qua nhiều lớp API.
- Retry sai loại lỗi có thể tệ hơn (spam server).
- Tối ưu concurrency không đúng ngữ cảnh vẫn có thể nghẽn.
- Guard race condition bằng flag/request id không giảm tải network nếu không cancel request cũ.

Chú thích: Chỉ retry lỗi tạm thời (5xx, ECONNRESET); không retry 4xx trừ khi có lý do rõ ràng.

**Code Example:**

```ts
// ===================================================
// 1) Abort fetch với timeout (Hủy request sau thời gian chờ)
// ===================================================
function fetchWithTimeout(url: string, ms = 5000) {
  // ✅ Tạo AbortController để có thể hủy request
  const ctrl = new AbortController();

  // ⏱️ Set timeout: sau ms milliseconds → tự động hủy request
  const t = setTimeout(() => ctrl.abort(), ms);

  // 📡 Fetch với signal → có thể bị hủy
  // 🧹 finally: luôn clear timeout để tránh memory leak
  return fetch(url, { signal: ctrl.signal }).finally(() => clearTimeout(t));
}

// ===================================================
// 2) Concurrency limit (Giới hạn số tác vụ chạy đồng thời)
// ===================================================
function createLimiter(max: number) {
  let active = 0; // 📊 Đếm số tác vụ đang chạy
  const queue: Array<() => void> = []; // 📋 Hàng đợi chờ slot trống

  // 🔄 Hàm giải phóng slot khi task xong
  const next = () => {
    active--; // Giảm số task đang chạy
    queue.shift()?.(); // Đánh thức task tiếp theo trong queue
  };

  // 🎯 Hàm wrapper để giới hạn concurrency
  return async function run<T>(fn: () => Promise<T>): Promise<T> {
    // ⏳ Nếu đã đạt max → chờ slot trống
    if (active >= max) {
      // Tạo Promise và đưa resolver vào queue
      await new Promise<void>((res) => queue.push(res));
    }

    active++; // Tăng số task đang chạy
    try {
      return await fn(); // Chạy task thực sự
    } finally {
      next(); // Luôn giải phóng slot (dù thành công hay lỗi)
    }
  };
}

// ===================================================
// 3) Retry + Exponential Backoff + Jitter
// (Thử lại với thời gian chờ tăng dần + nhiễu ngẫu nhiên)
// ===================================================
async function retry<T>(op: () => Promise<T>, tries = 3) {
  let attempt = 0; // 📊 Đếm số lần đã thử

  while (true) {
    try {
      return await op(); // ✅ Thử chạy operation
    } catch (e) {
      // ❌ Nếu đã hết số lần thử → throw lỗi
      if (++attempt >= tries) throw e;

      // 📈 Exponential backoff: delay tăng theo lũy thừa 2
      // attempt=1 → 2^1 * 100 = 200ms
      // attempt=2 → 2^2 * 100 = 400ms
      // attempt=3 → 2^3 * 100 = 800ms
      const base = 2 ** attempt * 100;

      // 🎲 Jitter: thêm random 0-100ms để tránh "thundering herd"
      // (nhiều clients cùng retry cùng lúc)
      const jitter = Math.random() * 100;

      // ⏳ Đợi trước khi retry
      await new Promise((r) => setTimeout(r, base + jitter));
    }
  }
}

// ===================================================
// 4) Race condition guard - chỉ response mới nhất được cập nhật state
// ===================================================
let latestRequestId = 0;

async function search(query: string) {
  // Mỗi lần search tăng version/requestId
  const requestId = ++latestRequestId;

  const res = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
  const data = await res.json();

  // Nếu trong lúc chờ đã có request mới hơn, bỏ qua response cũ
  if (requestId !== latestRequestId) return;

  // Chỉ request mới nhất được quyền update UI/state
  setResults(data);
}
```

**Best Practices:**

- Truyền `signal` xuyên suốt chain APIs để hủy gọn
- Đặt timeout tổng; đo và điều chỉnh max concurrency theo tài nguyên
- Chỉ retry cho lỗi tạm thời (5xx, network)
- Với search/filter, kết hợp debounce + cancel request cũ + guard requestId để chống stale response

**Mistakes (Lỗi Thường Gặp):**

```ts
// ===================================================
// ❌ SAI LẦM 1: Retry vô hạn, không jitter
// ===================================================
async function badRetry() {
  while (true) {
    // ❌ Vòng lặp vô hạn
    try {
      return await fetch('/api/data');
    } catch (e) {
      await new Promise((r) => setTimeout(r, 100)); // ❌ Không có jitter
      // → Nếu 1000 clients cùng retry → server crash
    }
  }
}

// ✅ ĐÚNG: Có max attempts và jitter
async function goodRetry() {
  let attempt = 0;
  while (attempt < 3) {
    // ✅ Giới hạn số lần
    try {
      return await fetch('/api/data');
    } catch (e) {
      const jitter = Math.random() * 100; // ✅ Có jitter
      await new Promise((r) => setTimeout(r, 100 + jitter));
      attempt++;
    }
  }
}

// ===================================================
// ❌ SAI LẦM 2: Retry mọi lỗi (kể cả 4xx)
// ===================================================
async function badRetryAll() {
  return retry(async () => {
    const res = await fetch('/api/data');
    if (!res.ok) throw new Error('Error'); // ❌ Retry cả 404, 403...
    return res.json();
  }, 5);
  // → Spam server với requests không hợp lệ
}

// ✅ ĐÚNG: Chỉ retry lỗi tạm thời
async function goodRetry() {
  return retry(async () => {
    const res = await fetch('/api/data');
    if (res.status >= 500) throw new Error('Retry'); // ✅ Chỉ retry 5xx
    if (res.status >= 400) throw new Error('No retry'); // ❌ Không retry 4xx
    return res.json();
  }, 3);
}

// ===================================================
// ❌ SAI LẦM 3: Không cleanup AbortController
// ===================================================
function BadComponent() {
  useEffect(() => {
    const controller = new AbortController();
    fetch('/api/data', { signal: controller.signal });
    // ❌ Không có cleanup → memory leak khi unmount
  }, []);
}

// ✅ ĐÚNG: Cleanup trong useEffect
function GoodComponent() {
  useEffect(() => {
    const controller = new AbortController();
    fetch('/api/data', { signal: controller.signal });
    return () => controller.abort(); // ✅ Cleanup
  }, []);
}

// ===================================================
// ❌ SAI LẦM 4: Race condition - response cũ ghi đè response mới
// ===================================================
function BadSearch({ query }) {
  const [results, setResults] = useState([]);

  useEffect(() => {
    fetch(`/api/search?q=${query}`)
      .then((r) => r.json())
      .then(setResults); // ❌ Request cũ về sau vẫn update state
  }, [query]);
}

// ✅ ĐÚNG: Hủy request cũ khi query đổi
function GoodSearch({ query }) {
  const [results, setResults] = useState([]);

  useEffect(() => {
    const controller = new AbortController();

    fetch(`/api/search?q=${query}`, { signal: controller.signal })
      .then((r) => r.json())
      .then(setResults)
      .catch((err) => {
        if (err.name !== 'AbortError') console.error(err);
      });

    return () => controller.abort(); // ✅ query đổi → hủy request cũ
  }, [query]);
}
```

---

## 🔍 Giải Thích Chi Tiết (Dễ Hiểu)

### 1. Cancellation – Hủy bỏ tác vụ với `AbortController`

**Vấn đề:**

- Trong web/app hiện đại, ta hay có các request dài: fetch API, đọc stream, xử lý file, long-polling,...
- Nếu user **đổi trang**, **đổi filter**, **đóng modal**, request cũ thường **không còn cần thiết** nữa.
- Nếu ta không hủy, sẽ:
  - Tốn băng thông, CPU.
  - Dễ gây **race condition** (kết quả cũ ghi đè kết quả mới).

**Giải pháp:** dùng `AbortController` + `AbortSignal`.

**Cách hoạt động:**

- Tạo controller: `const controller = new AbortController();`
- Lấy signal: `const { signal } = controller;`
- Truyền `signal` vào các API support cancellation (như `fetch`, đôi khi là lib khác):

```ts
// 📡 Hàm fetch có thể hủy được
function fetchWithCancel(url: string, signal: AbortSignal) {
  // ✅ Truyền signal vào fetch → có thể hủy request này
  return fetch(url, { signal });
}

// 🎮 Tạo controller để điều khiển việc hủy
const controller = new AbortController();

// 📥 Gọi API với signal
fetchWithCancel('/api/data', controller.signal)
  .then((res) => res.json()) // ✅ Thành công → parse JSON
  .catch((err) => {
    // 🔍 Kiểm tra loại lỗi
    if (err.name === 'AbortError') {
      // ⏹️ Request bị hủy (không phải lỗi thật)
      console.log('Request bị hủy');
    } else {
      // ❌ Lỗi thật (network, server error...)
      console.error('Lỗi khác:', err);
    }
  });

// 🛑 Khi không cần request nữa (user đổi trang, đóng modal...)
controller.abort();
```

- Khi `controller.abort()` được gọi:
  - `fetch` sẽ **ngừng** request ngay lập tức (không đợi response).
  - Promise sẽ reject với `DOMException` tên `'AbortError'`.
  - Browser sẽ cancel network request (tiết kiệm bandwidth).

**Lan truyền signal xuyên suốt:**

- Trong code thực tế, bạn không chỉ có 1 hàm `fetch`, mà cả 1 chain:
  - UI → service → repository → http client.
- Để hủy gọn, ta truyền `signal` xuyên suốt:

```ts
// 📥 Layer 1: Service layer - nhận signal và truyền xuống
async function getUser(id: string, signal: AbortSignal) {
  // ✅ Truyền signal xuống fetch
  return fetch(`/api/users/${id}`, { signal }).then((r) => r.json());
}

// 📥 Layer 2: Business logic layer - nhận signal và truyền xuống service
async function loadUserProfile(id: string, signal: AbortSignal) {
  // ✅ Truyền signal xuống getUser
  const user = await getUser(id, signal);
  // ... logic tiếp (có thể gọi thêm API khác với cùng signal)
  return user;
}

// 🎮 Tạo controller ở UI layer
const controller = new AbortController();

// 🚀 Gọi function với signal
loadUserProfile('123', controller.signal);

// 🛑 Khi user navigate đi nơi khác → hủy toàn bộ chain
// → getUser() sẽ bị hủy → fetch() sẽ bị hủy → tiết kiệm tài nguyên
controller.abort();
```

**React / UI integration (pattern hay dùng):**

- Trong `useEffect`, tạo `AbortController` và hủy trong cleanup để tránh memory leak:

```ts
useEffect(() => {
  // 🎮 Tạo controller mới mỗi khi query thay đổi
  const controller = new AbortController();

  // 📡 Fetch với signal → có thể hủy
  fetch('/api/search?q=' + query, { signal: controller.signal })
    .then((r) => r.json())
    .then(setData) // ✅ Cập nhật state với kết quả
    .catch((err) => {
      // 🔍 Chỉ log lỗi thật, bỏ qua AbortError (request bị hủy là bình thường)
      if (err.name !== 'AbortError') console.error(err);
    });

  // 🧹 Cleanup function: chạy khi:
  // - Component unmount (user rời trang)
  // - query thay đổi (user gõ tiếp → hủy request cũ)
  return () => controller.abort();
}, [query]);
// ⚠️ Dependency [query]: mỗi khi query đổi → cleanup cũ → tạo controller mới
```

**`AbortSignal.timeout(ms)`:**

- Trình duyệt mới hỗ trợ: `AbortSignal.timeout(5000)` để auto abort sau 5s, không phải tự setTimeout.

```ts
// ⏱️ AbortSignal.timeout() - Cách đơn giản hơn để set timeout
// ✅ Tự động hủy sau 5 giây (không cần tạo controller thủ công)
fetch('/api/data', { signal: AbortSignal.timeout(5000) });

// 💡 So sánh với cách cũ:
// ❌ Cách cũ (phức tạp hơn):
// const ctrl = new AbortController();
// setTimeout(() => ctrl.abort(), 5000);
// fetch('/api/data', { signal: ctrl.signal });

// ✅ Cách mới (đơn giản hơn):
// fetch('/api/data', { signal: AbortSignal.timeout(5000) });
```

**Sai lầm thường gặp:**

- Không hủy controller khi component unmount → request cũ vẫn chạy.
- Không phân biệt `AbortError` với lỗi thật → log lỗi lung tung.
- Không truyền `signal` xuống sâu → chỉ hủy được một phần, không triệt để.

---

### 2. Concurrency – Giới hạn số tác vụ chạy đồng thời

**Vấn đề:**

- Nếu bạn loop gọi 100 `fetch` cùng lúc:
  - Trình duyệt có giới hạn connection, server dễ bị quá tải.
  - User thấy chậm vì mọi thứ tranh tài nguyên.

**Mục tiêu:**

- Cho phép chạy **song song**, nhưng **giới hạn số lượng tối đa** (ví dụ max 5 request cùng lúc).

Đây chính là **Semaphore / Pool Pattern**.

**Ý tưởng cơ bản:**

- Bạn có `max` slot (ví dụ 5).
- Nếu còn slot trống → cho chạy ngay.
- Nếu hết slot → đưa vào queue, chờ slot trống.

**Ví dụ semaphore đơn giản (từ đoạn code trong file):**

```ts
// ===================================================
// 🎯 SEMAPHORE PATTERN - Giới hạn số tác vụ chạy đồng thời
// ===================================================
function createLimiter(max: number) {
  let active = 0; // 📊 Đếm số tác vụ đang chạy (0 → max)
  const queue: Array<() => void> = []; // 📋 Hàng đợi: các task đang chờ slot

  // 🔄 Hàm giải phóng slot và đánh thức task tiếp theo
  const next = () => {
    active--; // Giảm số task đang chạy
    queue.shift()?.(); // Lấy task đầu queue và đánh thức (gọi resolver)
  };

  // 🎯 Hàm wrapper: giới hạn concurrency của bất kỳ async function nào
  return async function run<T>(fn: () => Promise<T>): Promise<T> {
    // ⏳ Nếu đã đạt max → phải chờ
    if (active >= max) {
      // Tạo Promise và đưa resolver vào queue
      // Promise này sẽ resolve khi có slot trống (được gọi trong next())
      await new Promise<void>((res) => queue.push(res));
    }

    active++; // Tăng số task đang chạy
    try {
      return await fn(); // ✅ Chạy task thực sự
    } finally {
      // 🧹 Luôn giải phóng slot (dù thành công hay lỗi)
      next();
    }
  };
}

// ===================================================
// 💻 CÁCH SỬ DỤNG
// ===================================================
// Tạo limiter với max 5 tasks cùng lúc
const limit = createLimiter(5);

// Load nhiều URLs nhưng chỉ tối đa 5 requests cùng lúc
async function loadMany(urls: string[]) {
  return Promise.all(
    urls.map((u) =>
      // ✅ Wrap mỗi fetch trong limit() → chỉ tối đa 5 chạy cùng lúc
      limit(() => fetch(u).then((r) => r.text()))
    )
  );
}

// 📊 Ví dụ: 20 URLs, max 5 concurrent
// - Requests 1-5: chạy ngay
// - Requests 6-10: chờ trong queue
// - Request 1 xong → Request 6 chạy
// - Request 2 xong → Request 7 chạy
// - ... và cứ thế tiếp tục
```

**Khi nào cần concurrency control:**

- Gọi API hàng loạt (import data, sync).
- Tải nhiều ảnh/file lớn.
- Tương tác với API có rate limit (ví dụ: 429 Too Many Requests).

**Thư viện hữu ích:**

- `p-limit`, `p-queue` (Sindre Sorhus) – rất phổ biến trong Node/JS.
- Một số HTTP client hoặc data-fetching lib có built-in concurrency.

**Sai lầm thường gặp:**

- Đặt limit **quá thấp** → hệ thống nhàn rỗi, chậm hơn cần thiết.
- Đặt limit **quá cao** → gần như không khác gì không giới hạn, dễ nghẽn.
- Không phân biệt I/O-bound vs CPU-bound khi chọn limit.

---

### 3. Retry – Thử lại với Exponential Backoff + Jitter

**Vấn đề:**

- Mạng không ổn định, server đôi lúc **lỗi tạm thời** (5xx, timeouts).
- Nếu chỉ gọi đúng 1 lần, UX kém; nếu **spam retry liên tục**, server càng nghẽn.

**Mục tiêu:**

- Retry một số lần giới hạn, với **khoảng chờ tăng dần (exponential backoff)**, cộng **jitter** để tránh mọi client cùng retry cùng lúc.

**Khái niệm:**

- **Exponential backoff:**
  - Mỗi lần fail, delay tăng theo lũy thừa 2.
  - Ví dụ: base 100ms → 100, 200, 400, 800, ...
- **Jitter:**
  - Thêm một chút random để **không phải tất cả clients đợi cùng 1 thời gian rồi cùng retry một lúc**.

**Ví dụ hàm retry (trong file):**

```ts
// ===================================================
// 🔄 RETRY VỚI EXPONENTIAL BACKOFF + JITTER
// ===================================================
async function retry<T>(op: () => Promise<T>, tries = 3) {
  let attempt = 0; // 📊 Đếm số lần đã thử (0, 1, 2, ...)

  while (true) {
    try {
      // ✅ Thử chạy operation
      return await op();
    } catch (e) {
      // ❌ Lỗi xảy ra
      attempt++; // Tăng số lần thử

      // 🛑 Nếu đã hết số lần thử → throw lỗi (không retry nữa)
      if (attempt >= tries) throw e;

      // 📈 EXPONENTIAL BACKOFF: delay tăng theo lũy thừa 2
      // attempt=1 → 2^1 * 100 = 200ms
      // attempt=2 → 2^2 * 100 = 400ms
      // attempt=3 → 2^3 * 100 = 800ms
      // → Mỗi lần retry đợi lâu hơn (cho server thời gian recover)
      const base = 2 ** attempt * 100;

      // 🎲 JITTER: thêm random 0-100ms
      // → Tránh "thundering herd": nhiều clients cùng retry cùng lúc
      // VD: 1000 clients retry cùng lúc → server crash
      //     Có jitter → retry rải rác → server không bị quá tải
      const jitter = Math.random() * 100;

      // ⏳ Đợi trước khi retry lần tiếp theo
      await new Promise((r) => setTimeout(r, base + jitter));
    }
  }
}

// 📊 Ví dụ timeline với tries=3:
// T=0ms:   Thử lần 1 → ❌ Lỗi
// T=200ms: Đợi 200ms (base) + jitter
// T=250ms: Thử lần 2 → ❌ Lỗi
// T=650ms: Đợi 400ms (base) + jitter
// T=700ms: Thử lần 3 → ❌ Lỗi → throw (hết số lần)
```

**Quan trọng:**

- **Không retry mọi lỗi**:
  - Nên retry **lỗi tạm thời**: HTTP 5xx, lỗi network (ECONNRESET,...).
  - Không retry 4xx (400, 401, 403, 404, 422,...) trừ khi có logic đặc biệt (ví dụ: refresh token rồi retry 401 đúng 1 lần).

```ts
// ===================================================
// ✅ RETRY AN TOÀN - Chỉ retry lỗi tạm thời
// ===================================================
async function safeFetchWithRetry(url: string) {
  return retry(async () => {
    const res = await fetch(url);

    // 🔴 HTTP 5xx: Server Error (lỗi tạm thời)
    // ✅ NÊN RETRY: Server có thể recover sau vài giây
    // VD: 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable
    if (res.status >= 500) {
      throw new Error('Server error, sẽ retry');
    }

    // 🔴 HTTP 4xx: Client Error (lỗi vĩnh viễn)
    // ❌ KHÔNG NÊN RETRY: Lỗi từ phía client, retry không giải quyết được
    // VD: 400 Bad Request (sai format), 401 Unauthorized (thiếu token),
    //     403 Forbidden (không có quyền), 404 Not Found (URL sai)
    if (res.status >= 400) {
      // ⚠️ Exception: 401 có thể retry 1 lần sau khi refresh token
      throw new Error('Client error, không retry');
    }

    // ✅ HTTP 2xx: Success → return data
    return res.json();
  }, 3);
}

// 📊 Phân loại HTTP status codes:
// 2xx: Success → Không cần retry
// 4xx: Client Error → Không retry (trừ 401 với refresh token)
// 5xx: Server Error → Retry với backoff
// Network errors (ECONNRESET, ETIMEDOUT): Retry với backoff
```

**Idempotent requests (Requests An Toàn Khi Retry):**

- **Idempotent** = Gọi nhiều lần → kết quả giống nhau (không tạo duplicate)
- Retry an toàn nhất với **GET**, **PUT**, **DELETE**:
  - **GET**: Đọc data → retry không tạo duplicate
  - **PUT**: Update data → retry cùng data → kết quả giống nhau
  - **DELETE**: Xóa data → retry → vẫn xóa (idempotent)
- Với **POST**, cần cẩn thận vì có thể tạo **nhiều bản ghi** trùng lặp:

  ```ts
  // ❌ NGUY HIỂM: Retry POST có thể tạo duplicate
  POST /api/orders → Retry → Tạo 2 orders giống nhau

  // ✅ AN TOÀN: Dùng idempotency key
  POST /api/orders
  Headers: { 'Idempotency-Key': 'unique-key-123' }
  → Server check key → Nếu đã xử lý → return kết quả cũ
  → Nếu chưa → xử lý mới
  ```

**Circuit Breaker Pattern (Nâng Cao - Ngắt Mạch):**

- **Vấn đề**: Nếu server down hoàn toàn → retry liên tục → waste resources
- **Giải pháp**: Circuit Breaker = Tự động ngắt kết nối khi server lỗi quá nhiều

```ts
// 🎯 3 TRẠNG THÁI CỦA CIRCUIT BREAKER:

// 1️⃣ CLOSED (Đóng - Bình thường)
// → Requests đi qua bình thường
// → Đếm số lỗi liên tiếp

// 2️⃣ OPEN (Mở - Ngắt)
// → Server lỗi quá nhiều (VD: 50 lỗi liên tiếp)
// → CHẶN HẲN requests mới trong 30s
// → Trả lỗi ngay (không retry) → tiết kiệm tài nguyên
// → Sau 30s → chuyển sang HALF-OPEN

// 3️⃣ HALF-OPEN (Nửa mở - Thử nghiệm)
// → Cho phép 1 vài requests đi qua để test
// → Nếu thành công → chuyển về CLOSED
// → Nếu vẫn lỗi → quay lại OPEN (đợi thêm 30s)
```

**Ví dụ thực tế:**

```ts
// 📊 Timeline khi server down:
// T=0s:   Server down → Retry → Lỗi (x50)
// T=10s:  Circuit OPEN → Chặn requests → Trả lỗi ngay
// T=40s:  Circuit HALF-OPEN → Test 1 request
// T=40s:  Request fail → Circuit OPEN lại (đợi thêm 30s)
// T=70s:  Circuit HALF-OPEN → Test 1 request
// T=70s:  Request success → Circuit CLOSED → Hoạt động bình thường
```

---

### 4. Race Condition – Kết quả cũ ghi đè kết quả mới

**Vấn đề:**

- Race condition xảy ra khi **nhiều async operations cùng chạy**, nhưng **thứ tự hoàn thành không đoán trước được**.
- Trong frontend, case phổ biến nhất là search/filter/detail page:
  - User chọn/gõ giá trị mới.
  - Request mới được gửi.
  - Request cũ vẫn đang chạy.
  - Request cũ về sau và ghi đè state mới.

**Ví dụ timeline lỗi:**

```ts
// T=0ms:   User gõ "r"     → request A: /api/search?q=r
// T=50ms:  User gõ "react" → request B: /api/search?q=react
// T=120ms: Request B về trước → UI hiển thị kết quả "react" ✅
// T=500ms: Request A về sau  → UI bị ghi đè thành kết quả "r" ❌
```

**Sai ở đâu?**

- Code chỉ quan tâm "request nào vừa resolve" chứ không kiểm tra "request đó còn hợp lệ không".
- `Promise` resolve theo tốc độ network/server, không theo thứ tự user action.
- Debounce chỉ giảm số request, **không đảm bảo** response cũ không về sau.

```ts
// ===================================================
// ❌ RACE CONDITION: response nào về sau thì thắng
// ===================================================
function SearchBox({ query }: { query: string }) {
  const [results, setResults] = useState([]);

  useEffect(() => {
    fetch(`/api/search?q=${encodeURIComponent(query)}`)
      .then((r) => r.json())
      .then(setResults); // ❌ Không biết query này còn là query mới nhất không
  }, [query]);
}
```

**Cách xử lý 1: Cancel request cũ bằng `AbortController`**

- Đây là cách tốt nhất khi API hỗ trợ cancellation vì vừa tránh stale update, vừa tiết kiệm network.
- Khi `query` đổi, cleanup của effect cũ chạy và abort request cũ.

```ts
// ===================================================
// ✅ CÁCH 1: Abort request cũ khi query đổi
// ===================================================
function SearchBox({ query }: { query: string }) {
  const [results, setResults] = useState([]);

  useEffect(() => {
    if (!query) {
      setResults([]);
      return;
    }

    const controller = new AbortController();

    async function load() {
      try {
        const res = await fetch(`/api/search?q=${encodeURIComponent(query)}`, {
          signal: controller.signal,
        });
        const data = await res.json();

        // ✅ Nếu đã abort sau khi fetch xong nhưng trước khi parse/update, bỏ qua
        if (controller.signal.aborted) return;

        setResults(data);
      } catch (err) {
        if (err instanceof DOMException && err.name === 'AbortError') return;
        console.error(err);
      }
    }

    load();

    return () => controller.abort();
  }, [query]);
}
```

**Cách xử lý 2: Request ID / Sequence number**

- Dùng khi không thể hủy request thật sự, ví dụ library không nhận `AbortSignal`, hoặc task async không cancel được.
- Ý tưởng: mỗi request có `requestId`; response chỉ được update nếu id của nó vẫn là id mới nhất.

```ts
// ===================================================
// ✅ CÁCH 2: Last request wins bằng requestId
// ===================================================
function SearchBox({ query }: { query: string }) {
  const [results, setResults] = useState([]);
  const latestRequestId = useRef(0);

  useEffect(() => {
    if (!query) {
      setResults([]);
      return;
    }

    const requestId = ++latestRequestId.current;

    async function load() {
      const res = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
      const data = await res.json();

      // ✅ Có request mới hơn rồi → bỏ qua response cũ
      if (requestId !== latestRequestId.current) return;

      setResults(data);
    }

    load().catch(console.error);
  }, [query]);
}
```

**Cách xử lý 3: Ignore flag trong `useEffect`**

- Pattern đơn giản, dễ giải thích khi phỏng vấn.
- Cleanup đổi flag thành `true`; async callback cũ kiểm tra flag trước khi set state.
- Cách này **không hủy network**, chỉ chặn state update.

```ts
// ===================================================
// ✅ CÁCH 3: Ignore stale result bằng cleanup flag
// ===================================================
useEffect(() => {
  let ignore = false;

  async function load() {
    const res = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
    const data = await res.json();

    if (ignore) return; // ✅ Effect cũ đã bị cleanup
    setResults(data);
  }

  load().catch(console.error);

  return () => {
    ignore = true;
  };
}, [query]);
```

**Cách xử lý 4: Data-fetching library**

- React Query/SWR thường đã xử lý nhiều vấn đề liên quan:
  - Cache theo key (`['search', query]`).
  - Dedupe request trùng.
  - Stale-while-revalidate.
  - Retry/backoff.
  - Không update nhầm view nếu query key đã đổi.

```ts
// Ý tưởng với React Query:
const { data, isFetching } = useQuery({
  queryKey: ['search', query],
  queryFn: ({ signal }) =>
    fetch(`/api/search?q=${encodeURIComponent(query)}`, { signal }).then((r) =>
      r.json()
    ),
  enabled: query.length > 0,
});
```

**Khi nào dùng cách nào?**

- **AbortController**: ưu tiên cho `fetch`, search, filter, autocomplete, route change.
- **Request ID**: dùng khi task không cancel được nhưng cần đảm bảo last-request-wins.
- **Ignore flag**: phù hợp cho effect nhỏ, demo/phỏng vấn, hoặc code đơn giản.
- **React Query/SWR**: dùng trong app production có cache, retry, refetch, loading/error state phức tạp.

**Điểm senior cần nói rõ:**

- Race condition không chỉ là "multi-thread bug"; trong JS single-thread vẫn xảy ra vì async completion order không deterministic.
- `await` không làm request chạy theo thứ tự mong muốn nếu bạn tạo nhiều async flow độc lập.
- Cần phân biệt:
  - **Last response wins**: response nào về cuối thì update UI. Đây thường là bug.
  - **Last request wins**: request mới nhất theo ý định user mới được update UI. Đây thường là đúng.
- Cancellation là giải pháp tốt hơn ignore-only vì giảm cả stale update lẫn tài nguyên lãng phí.

---

### 5. Kết hợp Cancellation + Concurrency + Retry + Race Condition trong thực tế

- Một flow thực tế thường gồm:
  - **Giới hạn concurrency** để bảo vệ client/server.
  - **Retry có kiểm soát** cho lỗi tạm thời.
  - **Cancellation** để dừng những thứ không còn cần.
  - **Race condition guard** để response cũ không ghi đè state mới.

**Ví dụ kịch bản thực tế:** User gõ search liên tục:

```ts
// 🎯 KỊCH BẢN: Search box với debounce + cancellation + retry + concurrency

function SearchComponent() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const latestRequestId = useRef(0);

  useEffect(() => {
    if (!query) return;

    // 🎮 Tạo controller mới mỗi lần query đổi
    const controller = new AbortController();
    const requestId = ++latestRequestId.current;

    // ⏱️ Debounce: Đợi 300ms sau khi user ngừng gõ
    const timeoutId = setTimeout(async () => {
      try {
        // 🔄 Retry cả fetch nếu lỗi tạm thời
        const data = await retry(async () => {
          // 📡 Fetch với signal → có thể hủy
          const res = await fetch(`/api/search?q=${query}`, {
            signal: controller.signal,
          });

          if (!res.ok && res.status >= 500) {
            throw new Error('Server error');
          }

          return res.json();
        }, 2);

        // 🧯 Race guard: nếu đã có request mới hơn, bỏ qua response cũ
        if (requestId !== latestRequestId.current) return;

        setResults(data);
      } catch (err) {
        if (!(err instanceof DOMException && err.name === 'AbortError')) {
          console.error('Search error:', err);
        }
      }
    }, 300);

    // 🧹 Cleanup: Hủy timeout và request khi query đổi
    return () => {
      clearTimeout(timeoutId);
      controller.abort(); // ✅ Hủy request cũ khi có request mới
    };
  }, [query]);

  return <input value={query} onChange={(e) => setQuery(e.target.value)} />;
}

// 📊 Timeline khi user gõ "react":
// T=0ms:   User gõ "r" → Set timeout 300ms
// T=100ms: User gõ "re" → Clear timeout cũ → Set timeout mới
// T=200ms: User gõ "rea" → Clear timeout cũ → Set timeout mới
// T=300ms: User gõ "reac" → Clear timeout cũ → Set timeout mới
// T=400ms: User gõ "react" → Clear timeout cũ → Set timeout mới
// T=700ms: Timeout trigger → Fetch "/api/search?q=react"
//          → Nếu user gõ tiếp → Request này bị hủy (controller.abort())
```

**Kết hợp 4 pattern:**

1. **Cancellation**: Hủy request cũ khi user gõ tiếp → Tránh race condition
2. **Retry**: Retry 1-2 lần nếu backend 502 → Tăng độ tin cậy
3. **Concurrency**: Nếu user mở 20 tab → Giới hạn max 5 requests cùng lúc → Bảo vệ server
4. **Race condition guard**: Nếu không cancel được request, dùng requestId để chỉ commit response mới nhất

---

### 6. Tóm tắt để ôn phỏng vấn

- **Cancellation:**

  - Dùng `AbortController/AbortSignal` cho `fetch` và các API hỗ trợ.
  - Truyền `signal` xuyên suốt chain async; cleanup ở React `useEffect`.

- **Concurrency:**

  - Dùng semaphore/pool để giới hạn số tác vụ chạy song song.
  - Điều chỉnh `max` theo thực tế (đo, không đoán mò).

- **Retry:**
  - Chỉ retry lỗi tạm thời; dùng **exponential backoff + jitter**.
  - Thiết lập số lần tối đa + timeout tổng, cân nhắc circuit breaker.

- **Race condition:**
  - Xảy ra khi async result cũ về sau và ghi đè state mới.
  - Ưu tiên cancel request cũ; nếu không cancel được thì dùng requestId/ignore flag.
  - Với UI tương tác nhanh, mục tiêu thường là **last-request-wins**, không phải **last-response-wins**.
