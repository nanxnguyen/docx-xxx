# ⏹️ Q28: Cancellation, Concurrency & Retry




**Trả lời:**

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

