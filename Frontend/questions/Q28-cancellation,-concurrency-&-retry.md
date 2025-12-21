# ⏹️ Q28: Cancellation, Concurrency & Retry

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"Cancellation dùng AbortController để hủy requests, Concurrency control giới hạn parallel tasks, Retry implement exponential backoff cho failed requests."**

**🔑 3 Pattern Chính:**

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

**⚠️ Lỗi Thường Gặp:**
- Không cleanup AbortController khi unmount → memory leak
- Retry **mọi lỗi** (kể cả 4xx) → spam server, waste resources
- Concurrency limit quá thấp → chậm, quá cao → overload
- Không cancel previous search request → race condition (results out of order)

**💡 Kiến Thức Senior:**
- **Idempotent requests**: Retry an toàn cho GET/PUT, cẩn thận với POST (dùng idempotency keys)
- **Circuit Breaker pattern**: Dừng hẳn requests sau N failures liên tiếp, chờ recover
- **`AbortSignal.timeout(ms)`** (native) thay `setTimeout + abort`
- **Stale-While-Revalidate**: Return cached data ngay, fetch mới background, update sau
- React Query/SWR **built-in** retry + cancellation + concurrency control




**Trả lời:****

- Hủy bỏ: `AbortController/AbortSignal` cho fetch/task dài; truyền `signal` xuyên suốt để hủy chuỗi async.
- Giới hạn đồng thời: dùng semaphore/pool để kiểm soát số tác vụ chạy song song, tránh nghẽn băng thông hay quota.
- Retry: áp dụng backoff + jitter cho lỗi tạm thời, kèm tổng timeout để không treo vô hạn.

Hoạt động:

- Abort: `controller.abort()` phát tín hiệu; fetch/reader/listener có `signal` sẽ throw DOMException('AbortError') và dừng sớm.
- Concurrency: hàng đợi đợi slot trống; xong 1 tác vụ thì phát tín hiệu cho tác vụ kế.
- Retry: vòng lặp bắt lỗi, đợi theo backoff (exponential + jitter), dừng khi đạt số lần tối đa.

Ưu điểm:

- Chủ động dừng tác vụ thừa (chuyển trang, đóng modal).
- Giảm tải server/trình duyệt, tránh bão request.
- Tăng độ tin cậy khi mạng không ổn định.

Nhược điểm:

- Cần lan truyền `signal` qua nhiều lớp API.
- Retry sai loại lỗi có thể tệ hơn (spam server).
- Tối ưu concurrency không đúng ngữ cảnh vẫn có thể nghẽn.

Chú thích: Chỉ retry lỗi tạm thời (5xx, ECONNRESET); không retry 4xx trừ khi có lý do rõ ràng.

**Code Example:**

```ts
// 1) Abort fetch với timeout
function fetchWithTimeout(url: string, ms = 5000) {
  const ctrl = new AbortController();
  const t = setTimeout(() => ctrl.abort(), ms);
  return fetch(url, { signal: ctrl.signal }).finally(() => clearTimeout(t));
}

// 2) Concurrency limit (semaphore đơn giản)
function createLimiter(max: number) {
  let active = 0;
  const queue: Array<() => void> = [];
  const next = () => {
    active--;
    queue.shift()?.();
  };
  return async function run<T>(fn: () => Promise<T>): Promise<T> {
    if (active >= max) await new Promise<void>((res) => queue.push(res));
    active++;
    try {
      return await fn();
    } finally {
      next();
    }
  };
}

// 3) Retry + backoff + jitter
async function retry<T>(op: () => Promise<T>, tries = 3) {
  let attempt = 0;
  while (true) {
    try {
      return await op();
    } catch (e) {
      if (++attempt >= tries) throw e;
      const base = 2 ** attempt * 100;
      const jitter = Math.random() * 100;
      await new Promise((r) => setTimeout(r, base + jitter));
    }
  }
}
```

**Best Practices:**

- Truyền `signal` xuyên suốt chain APIs để hủy gọn
- Đặt timeout tổng; đo và điều chỉnh max concurrency theo tài nguyên
- Chỉ retry cho lỗi tạm thời (5xx, network)

**Mistakes:**

```ts
// ❌ Retry vô hạn, không jitter → dồn tải (thundering herd)
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
function fetchWithCancel(url: string, signal: AbortSignal) {
  return fetch(url, { signal });
}

const controller = new AbortController();
fetchWithCancel('/api/data', controller.signal)
  .then((res) => res.json())
  .catch((err) => {
    if (err.name === 'AbortError') {
      console.log('Request bị hủy');
    } else {
      console.error('Lỗi khác:', err);
    }
  });

// Khi không cần nữa
controller.abort();
```

- Khi `controller.abort()` được gọi:
  - `fetch` sẽ **ngừng** request.
  - Promise sẽ reject với `DOMException` tên `'AbortError'`.

**Lan truyền signal xuyên suốt:**

- Trong code thực tế, bạn không chỉ có 1 hàm `fetch`, mà cả 1 chain:
  - UI → service → repository → http client.
- Để hủy gọn, ta truyền `signal` xuyên suốt:

```ts
async function getUser(id: string, signal: AbortSignal) {
  return fetch(`/api/users/${id}`, { signal }).then((r) => r.json());
}

async function loadUserProfile(id: string, signal: AbortSignal) {
  const user = await getUser(id, signal);
  // ... logic tiếp
  return user;
}

const controller = new AbortController();
loadUserProfile('123', controller.signal);
// Khi user navigate đi nơi khác
controller.abort();
```

**React / UI integration (pattern hay dùng):**

- Trong `useEffect`, tạo `AbortController` và hủy trong cleanup để tránh memory leak:

```ts
useEffect(() => {
  const controller = new AbortController();

  fetch('/api/search?q=' + query, { signal: controller.signal })
    .then((r) => r.json())
    .then(setData)
    .catch((err) => {
      if (err.name !== 'AbortError') console.error(err);
    });

  return () => controller.abort();
}, [query]);
```

**`AbortSignal.timeout(ms)`:**

- Trình duyệt mới hỗ trợ: `AbortSignal.timeout(5000)` để auto abort sau 5s, không phải tự setTimeout.

```ts
fetch('/api/data', { signal: AbortSignal.timeout(5000) });
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
function createLimiter(max: number) {
  let active = 0; // số tác vụ đang chạy
  const queue: Array<() => void> = []; // hàng đợi chờ slot

  const next = () => {
    active--;
    queue.shift()?.(); // đánh thức tác vụ tiếp theo
  };

  return async function run<T>(fn: () => Promise<T>): Promise<T> {
    if (active >= max) {
      // Hết slot → chờ đến khi được đánh thức
      await new Promise<void>((res) => queue.push(res));
    }

    active++;
    try {
      return await fn();
    } finally {
      next();
    }
  };
}

// Dùng
const limit = createLimiter(5); // tối đa 5 task cùng lúc

async function loadMany(urls: string[]) {
  return Promise.all(
    urls.map((u) =>
      limit(() => fetch(u).then((r) => r.text()))
    )
  );
}
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
async function retry<T>(op: () => Promise<T>, tries = 3) {
  let attempt = 0;

  while (true) {
    try {
      return await op();
    } catch (e) {
      if (++attempt >= tries) throw e; // hết số lần → ném lỗi

      const base = 2 ** attempt * 100; // 200, 400, 800, ...
      const jitter = Math.random() * 100; // 0-100ms

      await new Promise((r) => setTimeout(r, base + jitter));
    }
  }
}
```

**Quan trọng:**

- **Không retry mọi lỗi**:
  - Nên retry **lỗi tạm thời**: HTTP 5xx, lỗi network (ECONNRESET,...).
  - Không retry 4xx (400, 401, 403, 404, 422,...) trừ khi có logic đặc biệt (ví dụ: refresh token rồi retry 401 đúng 1 lần).

```ts
async function safeFetchWithRetry(url: string) {
  return retry(async () => {
    const res = await fetch(url);

    if (res.status >= 500) {
      throw new Error('Server error, sẽ retry');
    }

    if (res.status >= 400) {
      // Lỗi phía client → không nên retry
      throw new Error('Client error, không retry');
    }

    return res.json();
  }, 3);
}
```

**Idempotent requests:**

- Retry an toàn nhất với **GET**, **PUT** (idempotent – gọi nhiều lần kết quả như nhau).
- Với **POST**, cần cẩn thận vì có thể tạo **nhiều bản ghi** trùng lặp.
  - Dùng **idempotency key**: server coi cùng một key → tính là 1 request logic.

**Circuit Breaker (nâng cao):**

- Nếu server lỗi liên tục (ví dụ 50 lần gần đây), thay vì tiếp tục retry hoài:
  - **Mở circuit**: tạm thời **chặn hẳn** request mới trong 30s, trả lỗi nhanh.
  - Sau một khoảng, thử lại một số request (half-open), nếu ổn mới đóng circuit.

---

### 4. Kết hợp Cancellation + Concurrency + Retry trong thực tế

- Một flow thực tế thường gồm:
  - **Giới hạn concurrency** để bảo vệ client/server.
  - **Retry có kiểm soát** cho lỗi tạm thời.
  - **Cancellation** để dừng những thứ không còn cần.

**Ví dụ kịch bản:** user gõ search liên tục:

- Mỗi lần user gõ, ta gọi API search.
- Request cũ nên bị **cancel** nếu có request mới để tránh kết quả cũ ghi đè mới.
- Backend có thể thỉnh thoảng 502 → ta **retry 1–2 lần** với backoff.
- Nếu user mở 20 tab search cùng lúc → dùng **concurrency limit** để không bắn quá nhiều request.

---

### 5. Tóm tắt để ôn phỏng vấn

- **Cancellation:**
  - Dùng `AbortController/AbortSignal` cho `fetch` và các API hỗ trợ.
  - Truyền `signal` xuyên suốt chain async; cleanup ở React `useEffect`.

- **Concurrency:**
  - Dùng semaphore/pool để giới hạn số tác vụ chạy song song.
  - Điều chỉnh `max` theo thực tế (đo, không đoán mò).

- **Retry:**
  - Chỉ retry lỗi tạm thời; dùng **exponential backoff + jitter**.
  - Thiết lập số lần tối đa + timeout tổng, cân nhắc circuit breaker.


