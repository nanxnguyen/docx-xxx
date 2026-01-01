# ⚙️ Q13: Async/Await vs Promises vs Callbacks & Promise.all/any/race/allsettled

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"JavaScript async tiến hóa: Callbacks → Promises → Async/Await. Mỗi mẫu giải quyết code bất đồng bộ với đánh đổi khác nhau.**

**📊 Tiến Hóa Mẫu Async:**

1. **Callbacks**: Hàm làm tham số → thực thi sau khi hoàn thành thao tác bất đồng bộ.

   - ❌ Callback Hell (kim tự tháp hủy diệt), xử lý lỗi khó.
   - ✅ Đơn giản, hỗ trợ phổ biến.

2. **Promises**: Object đại diện cho việc hoàn thành/thất bại trong tương lai.

   - ✅ Chuỗi (`.then()`), xử lý lỗi tốt hơn (`.catch()`), tránh callback hell.
   - ❌ Vẫn dài dòng, có thể `.then()` hell.
   - **Trạng thái**: Pending → Fulfilled (resolved) | Rejected.

3. **Async/Await**: Cú pháp đường cho Promises → code giống sync.
   - ✅ Dễ đọc (như code sync), `try/catch` cho lỗi.
   - ❌ Phải dùng `await` trong hàm `async`, tuần tự theo mặc định (không song song).

**🔧 Promise Combinators (4 Phương Thức):**

1. **`Promise.all([p1, p2, p3])`**:

   - Đợi TẤT CẢ promises resolve.
   - Reject ngay nếu 1 promise reject (thất bại nhanh).
   - Trả về mảng kết quả theo thứ tự.
   - ✅ Trường hợp: Lấy nhiều tài nguyên, tất cả đều cần.

2. **`Promise.allSettled([p1, p2, p3])`**:

   - Đợi TẤT CẢ promises hoàn thành (fulfilled hoặc rejected).
   - Không bao giờ reject.
   - Trả về mảng `{ status, value/reason }`.
   - ✅ Trường hợp: Thực thi tất cả, không quan tâm thành công/thất bại của từng cái.

3. **`Promise.race([p1, p2, p3])`**:

   - Resolve/reject với promise đầu tiên hoàn thành (nhanh nhất thắng).
   - ✅ Trường hợp: Cơ chế timeout, phản hồi server nhanh nhất.

4. **`Promise.any([p1, p2, p3])`**:
   - Resolve với promise đầu tiên fulfilled.
   - Reject nếu TẤT CẢ reject (AggregateError).
   - ✅ Trường hợp: Cơ chế dự phòng, phản hồi thành công đầu tiên.

**🎯 Practical Examples - Ví Dụ Thực Tế:**

```js
// ❌ Sequential (Tuần tự - Chậm - Tổng 3 giây)
// Chạy từng cái một, đợi cái trước xong mới chạy cái sau
async function sequential() {
  const user = await fetchUser(); // Đợi 1 giây để lấy user
  const posts = await fetchPosts(); // Đợi 1 giây để lấy posts (sau khi user xong)
  const comments = await fetchComments(); // Đợi 1 giây để lấy comments (sau khi posts xong)
  // Tổng: 1s + 1s + 1s = 3 giây
}

// ✅ Parallel (Song song - Nhanh - Tổng 1 giây)
// Chạy tất cả cùng lúc, không đợi nhau
async function parallel() {
  // Promise.all chạy TẤT CẢ 3 requests ĐỒNG THỜI
  const [user, posts, comments] = await Promise.all([
    fetchUser(), // Chạy ngay
    fetchPosts(), // Chạy ngay (không đợi user)
    fetchComments(), // Chạy ngay (không đợi posts)
  ]);
  // Tất cả chạy cùng lúc → Tổng chỉ mất 1 giây (thời gian của request lâu nhất)
}

// ⏱️ Timeout với Promise.race - Tạo timeout cho request
// Nếu request quá lâu (ví dụ 5 giây), sẽ báo lỗi timeout
const fetchWithTimeout = (url, timeout = 5000) => {
  return Promise.race([
    fetch(url), // Request thật
    // Promise timeout: nếu 5 giây chưa xong → reject với lỗi 'Timeout'
    new Promise((_, reject) =>
      setTimeout(() => reject(new Error('Timeout')), timeout)
    ),
  ]);
  // Promise.race: cái nào xong trước (request hoặc timeout) → dùng kết quả đó
};
```

**⚠️ Common Mistakes - Lỗi Thường Gặp:**

- **Quên `await`**:

  - Promise không được chờ → trả về Promise object, không phải giá trị thật
  - Ví dụ: `const data = fetchUser()` → `data` là Promise, không phải user data
  - Phải: `const data = await fetchUser()` → `data` mới là user data

- **Chạy tuần tự khi có thể chạy song song**:

  - Dùng `await` trong vòng lặp → chậm vì đợi từng cái
  - Nên dùng `Promise.all()` để chạy tất cả cùng lúc

  ```js
  // ❌ Chậm (tuần tự - đợi từng cái một)
  for (const id of ids) {
    await fetchUser(id); // Đợi user 1 xong mới lấy user 2, rất chậm!
  }
  // Nếu có 100 users, mỗi user mất 1s → tổng 100 giây!

  // ✅ Nhanh (song song - chạy tất cả cùng lúc)
  await Promise.all(ids.map((id) => fetchUser(id)));
  // Tất cả 100 users chạy cùng lúc → chỉ mất 1 giây!
  ```

- **Unhandled rejections (Lỗi không được xử lý)**:

  - Thiếu `.catch()` hoặc `try/catch` → lỗi im lặng, khó debug
  - Luôn phải xử lý lỗi: `try/catch` hoặc `.catch()`

- **Promise.all fail-fast (Thất bại nhanh)**:
  - Nếu 1 promise thất bại → tất cả thất bại ngay
  - Nếu cần đợi tất cả hoàn thành (kể cả thất bại) → dùng `Promise.allSettled()`

**💡 Senior Insights - Kiến Thức Nâng Cao:**

- **Error handling (Xử lý lỗi)**:

  - `try/catch` trong async function có thể bắt (catch) bất kỳ lỗi nào từ `await`
  - Ví dụ: `try { await fetch() } catch(e) { ... }` → Bắt được lỗi network, JSON parse, HTTP error...

- **Top-level await (Await ở cấp cao nhất)**:

  - ES2022 cho phép dùng `await` ngoài async function trong ES modules
  - Ví dụ: `const data = await fetch('/api/data')` → Không cần wrap trong async function

- **Microtask queue (Hàng đợi microtask)**:

  - Promises thực thi trong microtask queue → Ưu tiên cao hơn setTimeout
  - Thứ tự: Sync code → Microtasks (Promises) → Macrotasks (setTimeout)
  - Ví dụ: `Promise.resolve().then(() => console.log(1)); setTimeout(() => console.log(2)); console.log(3)`
  - Output: 3 → 1 → 2 (3 sync, 1 microtask, 2 macrotask)

- **Cancellation (Hủy bỏ)**:
  - Native promises không hỗ trợ cancel trực tiếp
  - Dùng `AbortController` cho fetch API hoặc thư viện như Bluebird
  - Ví dụ: `abortController.abort()` → Hủy request đang chạy

---

**⚡ Quick Summary:**

> Callbacks = nested hell. Promises = chaining. Async/await = sync-like code. Promise.all/any/race/allSettled = combine nhiều promises

**💡 Ghi Nhớ:**

- 🎯 **Callbacks**: Nested = hell, error handling khó
- 📌 **Promises**: Chaining với .then(), error với .catch()
- ⚡ **Async/Await**: Sync-like code, try/catch cho errors
- 🔥 **Combinators**: all (all success), any (first success), race (first done), allSettled (all done)

**Trả lời:**

**Phần 1: Async Patterns**

- **Callbacks**: Functions được pass vào other functions để execute sau
- **Promises**: Objects đại diện cho eventual completion/failure của async operation
- **Async/Await**: Syntactic sugar cho Promises, làm code dễ đọc hơn

**Phần 2: Promise Combinators**

- **Promise.all**: Đợi tất cả promises resolve, reject nếu có 1 promise reject
- **Promise.any**: Resolve khi có 1 promise resolve, reject nếu tất cả reject
- **Promise.race**: Resolve/reject với promise đầu tiên hoàn thành
- **Promise.allSettled**: Đợi tất cả promises complete (resolve hoặc reject)

**Code Example - Ví Dụ Code:**

```typescript
// ============================================
// 1. CALLBACKS - Cách cũ nhất
// ============================================
// Truyền hàm callback vào để xử lý kết quả sau khi xong
function fetchData(callback: (error: Error | null, data?: any) => void): void {
  // Giả lập API call mất 1 giây
  setTimeout(() => {
    const data = { message: 'Hello World' };
    // Gọi callback với kết quả (error = null nghĩa là thành công)
    callback(null, data);
  }, 1000);
}

// Sử dụng: Truyền hàm callback vào
fetchData((error, data) => {
  if (error) {
    console.error('Error:', error); // Nếu có lỗi
  } else {
    console.log('Data:', data); // Nếu thành công
  }
});
// ❌ Vấn đề: Nếu nhiều callbacks lồng nhau → Callback Hell (kim tự tháp hủy diệt)

// ============================================
// 2. PROMISES - Cách hiện đại hơn
// ============================================
// Trả về Promise object, có thể chain với .then() và .catch()
function fetchDataPromise(): Promise<any> {
  // Tạo Promise mới
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const data = { message: 'Hello World' };
      resolve(data); // Thành công → gọi resolve
      // Nếu lỗi → gọi reject(new Error('...'))
    }, 1000);
  });
}

// Sử dụng: Chain với .then() và .catch()
fetchDataPromise()
  .then((data) => console.log('Data:', data)) // Xử lý khi thành công
  .catch((error) => console.error('Error:', error)); // Xử lý khi lỗi
// ✅ Ưu điểm: Có thể chain nhiều .then(), tránh callback hell

// ============================================
// 3. ASYNC/AWAIT - Cách hiện đại nhất (dễ đọc nhất)
// ============================================
// Dùng async/await → code trông giống code đồng bộ (synchronous)
async function fetchDataAsync(): Promise<any> {
  try {
    // await: Đợi Promise resolve, lấy giá trị trực tiếp
    const data = await fetchDataPromise();
    console.log('Data:', data);
    return data;
  } catch (error) {
    // Xử lý lỗi giống như code đồng bộ
    console.error('Error:', error);
    throw error; // Ném lỗi lại để caller xử lý
  }
}
// ✅ Ưu điểm: Code dễ đọc, dễ hiểu, xử lý lỗi đơn giản với try/catch
```

**Best Practices:**

- Sử dụng async/await cho modern code
- Sử dụng proper error handling
- Tránh callback hell
- Sử dụng TypeScript cho type safety

#### **🔥 Advanced Async Patterns - Các Vấn Đề Bất Đồng Bộ Phức Tạp**

**💡 Sau khi hiểu cơ bản về Callbacks, Promises, Async/Await, hãy giải quyết các vấn đề thực tế phức tạp hơn!**

---

#### **1️⃣ Error Handling - Xử Lý Lỗi Nâng Cao**

**🔹 Problem: Async errors không bị catch - Lỗi bất đồng bộ không được bắt**

```typescript
// ❌ VẤN ĐỀ: Unhandled Promise Rejection (Promise bị reject nhưng không được xử lý)
// Khi Promise bị reject mà không có .catch() hoặc try/catch → lỗi im lặng, khó debug
async function fetchUser(id: string) {
  const response = await fetch(`/api/users/${id}`);
  // ⚠️ Nếu response.json() throw error → không có ai catch → unhandled rejection
  return response.json();
}

// Gọi hàm mà không có try-catch → Lỗi không được xử lý!
fetchUser('123'); // ❌ Nếu API fail → unhandled rejection → có thể crash app
```

`````typescript
// ✅ GIẢI PHÁP 1: Try-catch trong function - Bắt lỗi ngay trong hàm
async function fetchUserSafe(id: string) {
try {
// Thử gọi API
const response = await fetch(`/api/users/${id}`);

    // Kiểm tra response có OK không (status 200-299)
    if (!response.ok) {
      // Nếu không OK → throw error với thông tin chi tiết
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    // Parse JSON từ response
    return await response.json();

} catch (error) {
// Bắt mọi lỗi (network error, JSON parse error, HTTP error...)
console.error('Failed to fetch user:', error);
throw error; // Re-throw (ném lại) để caller (người gọi hàm) có thể xử lý
}
}

// ✅ GIẢI PHÁP 2: Global error handler - Xử lý lỗi toàn cục
// Bắt tất cả lỗi Promise không được xử lý trong toàn bộ app
window.addEventListener('unhandledrejection', (event) => {
console.error('Unhandled promise rejection:', event.reason);

// Gửi lỗi đến service theo dõi lỗi (Sentry, Datadog, LogRocket...)
sendToErrorTracking({
type: 'UNHANDLED_PROMISE_REJECTION',
error: event.reason,
timestamp: Date.now(),
});

// Ngăn browser hiển thị lỗi mặc định (tránh làm phiền user)
event.preventDefault();
});
// 💡 Dùng khi: Muốn log tất cả lỗi không được xử lý để debug

// ✅ GIẢI PHÁP 3: Wrapper function với automatic error handling
// Tạo hàm wrapper tự động xử lý lỗi, trả về giá trị mặc định nếu lỗi
async function safeAsync<T>(
fn: () => Promise<T>, // Hàm async cần chạy
fallback?: T // Giá trị mặc định nếu lỗi
): Promise<T | undefined> {
try {
return await fn(); // Chạy hàm
} catch (error) {
console.error('Async error:', error);
return fallback; // Trả về giá trị mặc định thay vì throw error
}
}

// Sử dụng: An toàn, không bao giờ throw error
const user = await safeAsync(
() => fetchUser('123'), // Hàm cần chạy
{ id: '123', name: 'Default' } // Giá trị mặc định nếu lỗi
);
// 💡 Dùng khi: Muốn app không crash, luôn có giá trị mặc định

```` ```typescript

**🔹 Problem: Mixed sync/async errors**

```typescript
// ❌ VẤN ĐỀ: Sync errors không được catch bởi try-catch async
async function processData(data: any[]) {
  try {
    const validated = validateData(data); // Sync function có thể throw
    const results = await Promise.all(
      validated.map(item => processItem(item)) // Async function
    );
    return results;
  } catch (error) {
    // ⚠️ Catch được cả sync VÀ async errors
    console.error('Process failed:', error);
    throw error;
  }
}

// ✅ BEST PRACTICE: Wrap sync code trong Promise nếu cần
async function processDataSafe(data: any[]) {
  try {
    // Wrap sync validation trong Promise
    const validated = await Promise.resolve(validateData(data));
    const results = await Promise.all(
      validated.map(item => processItem(item))
    );
    return results;
  } catch (error) {
    console.error('Process failed:', error);
    throw error;
  }
}
`````

---

#### **2️⃣ Race Conditions - Xử Lý Tình Huống Chạy Đua**

**🔹 Problem: Multiple concurrent requests - Nhiều request đồng thời**

```typescript
// ❌ VẤN ĐỀ: User search - requests về không đúng thứ tự (race condition)
// Khi user gõ nhanh, nhiều requests được gửi, nhưng về không đúng thứ tự
let searchTerm = '';

async function handleSearch(term: string) {
  searchTerm = term;

  // Request chậm (mất 200ms)
  const results = await fetch(`/api/search?q=${term}`).then((r) => r.json());

  // ⚠️ VẤN ĐỀ RACE CONDITION:
  // 1. User gõ "abc" → Gửi request "abc" (chậm, mất 200ms)
  // 2. User xóa về "ab" → Gửi request "ab" (nhanh, mất 50ms)
  // 3. Request "ab" về trước (50ms) → Hiển thị kết quả "ab" ✅
  // 4. Request "abc" về sau (200ms) → Ghi đè kết quả "ab" → Hiển thị "abc" ❌
  // → User đang gõ "ab" nhưng thấy kết quả "abc" → SAI!
  displayResults(results);
}

// ✅ GIẢI PHÁP 1: Track latest request với counter - Đánh dấu request mới nhất
// Mỗi request có ID riêng, chỉ hiển thị kết quả của request mới nhất
let requestId = 0; // Biến đếm toàn cục

async function handleSearchSafe(term: string) {
  // Tăng counter và lưu ID của request hiện tại
  const currentRequestId = ++requestId; // VD: request 1 → ID = 1, request 2 → ID = 2

  const results = await fetch(`/api/search?q=${term}`).then((r) => r.json());

  // Kiểm tra: Request này có phải là request mới nhất không?
  if (currentRequestId === requestId) {
    // Nếu đúng → Đây là request mới nhất → Hiển thị kết quả
    displayResults(results);
  } else {
    // Nếu sai → Đã có request mới hơn → Bỏ qua kết quả cũ
    console.log('Discarding stale result'); // Bỏ qua kết quả lỗi thời
  }
}
// 💡 Cách hoạt động:
// - Request "abc" (ID=1) gửi trước, nhưng về sau
// - Request "ab" (ID=2) gửi sau, về trước
// - Khi "ab" về: currentRequestId (2) === requestId (2) → Hiển thị ✅
// - Khi "abc" về: currentRequestId (1) !== requestId (2) → Bỏ qua ❌

// ✅ GIẢI PHÁP 2: AbortController để cancel previous requests - Hủy request cũ
// AbortController cho phép hủy request đang chạy → Tiết kiệm băng thông, tránh race condition
let abortController: AbortController | null = null;

async function handleSearchWithAbort(term: string) {
  // Hủy request trước đó (nếu có)
  if (abortController) {
    abortController.abort(); // Hủy request cũ → Không cần đợi nó về nữa
  }

  // Tạo controller mới cho request hiện tại
  abortController = new AbortController();

  try {
    // Gửi request với signal → Có thể hủy được
    const results = await fetch(`/api/search?q=${term}`, {
      signal: abortController.signal, // Signal để hủy request này
    }).then((r) => r.json());

    displayResults(results);
  } catch (error: any) {
    // Nếu lỗi là do hủy request → Không cần xử lý (bình thường)
    if (error.name === 'AbortError') {
      console.log('Request cancelled'); // Request đã bị hủy → OK
    } else {
      throw error; // Lỗi khác → Ném lại
    }
  }
}
// 💡 Cách hoạt động:
// - User gõ "abc" → Gửi request "abc" với signal
// - User xóa về "ab" → abort() request "abc" → Hủy request cũ
// - Gửi request "ab" mới → Chỉ request này chạy
// ✅ Không có race condition vì request cũ đã bị hủy

// ✅ GIẢI PHÁP 3: Debounce + Abort (Tốt nhất cho search) - Kết hợp debounce và hủy request
// Debounce: Chờ user ngừng gõ một lúc (300ms) mới gửi request → Giảm số lượng request
import { debounce } from 'lodash';

let searchAbortController: AbortController | null = null;

// Debounce: Chỉ gọi hàm sau khi user ngừng gõ 300ms
const debouncedSearch = debounce(async (term: string) => {
  // Hủy request trước đó (nếu có)
  if (searchAbortController) {
    searchAbortController.abort();
  }

  // Tạo controller mới
  searchAbortController = new AbortController();

  try {
    // Gửi request với signal
    const results = await fetch(`/api/search?q=${term}`, {
      signal: searchAbortController.signal,
    }).then((r) => r.json());

    displayResults(results);
  } catch (error: any) {
    // Bỏ qua lỗi AbortError (do hủy request)
    if (error.name !== 'AbortError') {
      console.error('Search failed:', error);
    }
  }
}, 300); // Đợi 300ms sau khi user ngừng gõ mới gửi request

// Sử dụng: Gọi mỗi khi user gõ (nhưng chỉ gửi request sau 300ms ngừng gõ)
inputElement.addEventListener('input', (e) => {
  debouncedSearch(e.target.value);
});
// 💡 Cách hoạt động:
// - User gõ "a" → Chờ 300ms
// - User gõ "b" (trong 300ms) → Reset timer, chờ lại 300ms
// - User gõ "c" (trong 300ms) → Reset timer, chờ lại 300ms
// - User ngừng gõ 300ms → Gửi request "abc" (chỉ 1 request!)
// ✅ Giảm số lượng request từ 3 xuống 1 → Tiết kiệm băng thông, server load
```

**🔹 Problem: Concurrent updates to shared state - Cập nhật đồng thời vào state dùng chung**

```typescript
// ❌ VẤN ĐỀ: Nhiều thao tác async cập nhật cùng một state → Race condition
// Ví dụ: Rút tiền từ tài khoản, nhưng 2 lần rút cùng lúc
let balance = 1000; // Số dư ban đầu: 1000

async function withdraw(amount: number) {
  // Giả lập gọi API (mất 100ms)
  await delay(100);

  // Kiểm tra số dư có đủ không
  if (balance >= amount) {
    balance -= amount; // ⚠️ Race condition! Cả 2 hàm cùng đọc balance = 1000
    console.log(`Withdrew ${amount}, balance: ${balance}`);
  }
}

// Gọi đồng thời 2 lần rút 600
withdraw(600); // T0: Đọc balance = 1000 ✅ (đủ)
withdraw(600); // T1: Đọc balance = 1000 ✅ (đủ) - NHƯNG đây là lỗi!
// T2: Cả 2 đều trừ 600 → Balance = 1000 - 600 - 600 = -200 ❌
// ❌ Lỗi: Nên từ chối lần rút thứ 2 vì không đủ tiền!

// ✅ GIẢI PHÁP 1: Mutex lock - Khóa để chỉ 1 thao tác chạy tại một thời điểm
// Mutex = Mutual Exclusion (Loại trừ lẫn nhau) → Đảm bảo chỉ 1 hàm chạy tại một thời điểm
class Mutex {
  private locked = false; // Đang bị khóa không?
  private waiting: Array<() => void> = []; // Hàng đợi các hàm đang chờ

  // Khóa: Nếu đã bị khóa → đợi, nếu chưa → khóa ngay
  async lock(): Promise<void> {
    if (!this.locked) {
      this.locked = true; // Khóa ngay
      return;
    }

    // Đã bị khóa → Thêm vào hàng đợi, đợi được unlock
    await new Promise<void>((resolve) => {
      this.waiting.push(resolve); // Thêm vào hàng đợi
    });
  }

  // Mở khóa: Cho hàm tiếp theo trong hàng đợi chạy
  unlock(): void {
    const next = this.waiting.shift(); // Lấy hàm đầu tiên trong hàng đợi
    if (next) {
      next(); // Cho hàm đó chạy
    } else {
      this.locked = false; // Không còn ai chờ → Mở khóa
    }
  }
}

const balanceMutex = new Mutex(); // Tạo 1 mutex cho balance

async function withdrawSafe(amount: number) {
  await balanceMutex.lock(); // Khóa → Chỉ hàm này được chạy

  try {
    await delay(100);

    // Kiểm tra và trừ tiền (an toàn vì đã khóa)
    if (balance >= amount) {
      balance -= amount;
      console.log(`Withdrew ${amount}, balance: ${balance}`);
    } else {
      console.log('Insufficient funds'); // Không đủ tiền
    }
  } finally {
    balanceMutex.unlock(); // Mở khóa → Cho hàm tiếp theo chạy
  }
}
// 💡 Cách hoạt động:
// - withdraw(600) gọi → lock() → Chạy → unlock()
// - withdraw(600) gọi lần 2 → lock() → Đợi (vì đã bị khóa) → Chạy sau khi unlock() → unlock()
// ✅ Đảm bảo chỉ 1 hàm chạy tại một thời điểm → Không có race condition

// ✅ GIẢI PHÁP 2: Queue pattern
class WithdrawalQueue {
  private queue: Array<() => Promise<void>> = [];
  private processing = false;

  async add(fn: () => Promise<void>) {
    this.queue.push(fn);

    if (!this.processing) {
      await this.process();
    }
  }

  private async process() {
    this.processing = true;

    while (this.queue.length > 0) {
      const fn = this.queue.shift()!;
      await fn();
    }

    this.processing = false;
  }
}

const withdrawalQueue = new WithdrawalQueue();

async function withdrawQueued(amount: number) {
  await withdrawalQueue.add(async () => {
    await delay(100);

    if (balance >= amount) {
      balance -= amount;
      console.log(`Withdrew ${amount}, balance: ${balance}`);
    } else {
      console.log('Insufficient funds');
    }
  });
}
```

---

#### **3️⃣ Timeout & Retry - Xử Lý Timeout & Thử Lại**

**🔹 Problem: Requests hang forever**

```typescript
// ❌ VẤN ĐỀ: Request không có timeout
async function fetchData() {
  const response = await fetch('/api/data'); // Hang forever nếu server không respond
  return response.json();
}

// ✅ GIẢI PHÁP 1: Promise.race với timeout - Tạo timeout cho Promise
// Nếu Promise quá lâu (ví dụ 5 giây) → Tự động reject với lỗi Timeout
async function fetchWithTimeout<T>(
  promise: Promise<T>, // Promise cần chờ
  timeoutMs: number // Thời gian timeout (ms)
): Promise<T> {
  // Tạo Promise timeout: Sau timeoutMs giây → reject với lỗi 'Timeout'
  const timeoutPromise = new Promise<never>((_, reject) => {
    setTimeout(() => reject(new Error('Timeout')), timeoutMs);
  });

  // Promise.race: Cái nào xong trước (promise thật hoặc timeout) → dùng kết quả đó
  return Promise.race([promise, timeoutPromise]);
  // - Nếu promise xong trước → Trả về kết quả ✅
  // - Nếu timeout xong trước → Reject với lỗi 'Timeout' ❌
}

// Usage
try {
  const data = await fetchWithTimeout(
    fetch('/api/data').then((r) => r.json()),
    5000 // 5 seconds timeout
  );
  console.log('Data:', data);
} catch (error) {
  console.error('Request failed or timed out:', error);
}

// ✅ GIẢI PHÁP 2: AbortController với timeout
async function fetchWithAbortTimeout(url: string, timeoutMs: number) {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), timeoutMs);

  try {
    const response = await fetch(url, { signal: controller.signal });
    clearTimeout(timeoutId);
    return await response.json();
  } catch (error: any) {
    clearTimeout(timeoutId);

    if (error.name === 'AbortError') {
      throw new Error('Request timeout');
    }
    throw error;
  }
}

// ✅ GIẢI PHÁP 3: Reusable timeout wrapper
function withTimeout<T>(
  promise: Promise<T>,
  timeoutMs: number,
  errorMessage = 'Operation timeout'
): Promise<T> {
  return new Promise((resolve, reject) => {
    const timeoutId = setTimeout(() => {
      reject(new Error(errorMessage));
    }, timeoutMs);

    promise
      .then((result) => {
        clearTimeout(timeoutId);
        resolve(result);
      })
      .catch((error) => {
        clearTimeout(timeoutId);
        reject(error);
      });
  });
}
```

**🔹 Problem: Network failures**

```typescript
// ❌ VẤN ĐỀ: Không có retry logic
async function fetchData() {
  const response = await fetch('/api/data');
  return response.json(); // Fail ngay nếu network error
}

// ✅ GIẢI PHÁP 1: Retry với exponential backoff - Thử lại với độ trễ tăng dần
// Exponential backoff: Đợi 1s, 2s, 4s, 8s... (tăng gấp đôi mỗi lần)
// → Giảm tải cho server, tăng khả năng thành công
async function fetchWithRetry<T>(
  fn: () => Promise<T>, // Hàm cần thử lại
  maxRetries = 3, // Số lần thử lại tối đa (tổng 4 lần: 1 lần đầu + 3 lần retry)
  delayMs = 1000 // Độ trễ ban đầu (1 giây)
): Promise<T> {
  let lastError: Error;

  // Thử từ lần 0 đến maxRetries (tổng maxRetries + 1 lần)
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      return await fn(); // Thử chạy hàm
    } catch (error) {
      lastError = error as Error; // Lưu lỗi

      // Nếu chưa hết số lần thử → Đợi rồi thử lại
      if (attempt < maxRetries) {
        // Exponential backoff: delay tăng gấp đôi mỗi lần
        // attempt 0 → delay = 1000ms (1s)
        // attempt 1 → delay = 2000ms (2s)
        // attempt 2 → delay = 4000ms (4s)
        const delay = delayMs * Math.pow(2, attempt);
        console.log(`Retry ${attempt + 1}/${maxRetries} after ${delay}ms`);
        await new Promise((resolve) => setTimeout(resolve, delay)); // Đợi
      }
    }
  }

  // Hết số lần thử → Throw lỗi cuối cùng
  throw lastError!;
}
// 💡 Tại sao exponential backoff?
// - Lần 1 fail → Có thể server tạm thời quá tải → Đợi 1s
// - Lần 2 fail → Server vẫn quá tải → Đợi 2s (cho server nghỉ lâu hơn)
// - Lần 3 fail → Server vẫn quá tải → Đợi 4s (cho server nghỉ lâu hơn nữa)
// → Tăng khả năng thành công, giảm tải server

// Usage
const data = await fetchWithRetry(
  () => fetch('/api/data').then((r) => r.json()),
  3,
  1000
);

// ✅ GIẢI PHÁP 2: Retry với condition check
async function fetchWithConditionalRetry<T>(
  fn: () => Promise<T>,
  shouldRetry: (error: Error) => boolean,
  maxRetries = 3,
  delayMs = 1000
): Promise<T> {
  let lastError: Error;

  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      return await fn();
    } catch (error) {
      lastError = error as Error;

      // Chỉ retry nếu error có thể recover (network error, 503, etc.)
      if (attempt < maxRetries && shouldRetry(lastError)) {
        const delay = delayMs * Math.pow(2, attempt);
        console.log(`Retrying after ${delay}ms...`);
        await new Promise((resolve) => setTimeout(resolve, delay));
      } else {
        break; // Không retry (4xx errors, etc.)
      }
    }
  }

  throw lastError!;
}

// Usage: Chỉ retry network errors và 5xx errors
const data = await fetchWithConditionalRetry(
  () => fetch('/api/data').then((r) => r.json()),
  (error) => {
    // Retry network errors
    if (error.message.includes('network')) return true;

    // Retry 5xx server errors
    if ('status' in error && (error as any).status >= 500) return true;

    // Don't retry 4xx client errors
    return false;
  },
  3,
  1000
);

// ✅ GIẢI PHÁP 3: Advanced retry với circuit breaker - Cầu chì tự động
// Circuit Breaker: Nếu fail quá nhiều → Tự động ngắt (không gọi API nữa) → Tránh làm quá tải server
// 3 trạng thái:
// - CLOSED: Bình thường, cho phép gọi API
// - OPEN: Đã fail quá nhiều → Ngắt, không gọi API (trả lỗi ngay)
// - HALF_OPEN: Sau một thời gian → Thử lại 1 lần để xem server đã OK chưa
class CircuitBreaker {
  private failures = 0; // Số lần fail liên tiếp
  private lastFailureTime = 0; // Thời gian fail cuối cùng
  private state: 'CLOSED' | 'OPEN' | 'HALF_OPEN' = 'CLOSED';

  constructor(
    private threshold = 5, // Ngưỡng: Fail 5 lần → Mở circuit (OPEN)
    private timeout = 60000 // Timeout: Sau 60s → Thử lại (HALF_OPEN)
  ) {}

  async execute<T>(fn: () => Promise<T>): Promise<T> {
    // Nếu đang OPEN (đã ngắt)
    if (this.state === 'OPEN') {
      // Kiểm tra: Đã đủ thời gian timeout chưa?
      if (Date.now() - this.lastFailureTime > this.timeout) {
        this.state = 'HALF_OPEN'; // Chuyển sang HALF_OPEN → Thử lại 1 lần
      } else {
        // Chưa đủ thời gian → Vẫn ngắt, không gọi API
        throw new Error('Circuit breaker is OPEN');
      }
    }

    try {
      const result = await fn(); // Gọi API

      // Thành công → Reset
      if (this.state === 'HALF_OPEN') {
        this.state = 'CLOSED'; // Server đã OK → Đóng circuit, hoạt động bình thường
      }
      this.failures = 0; // Reset số lần fail

      return result;
    } catch (error) {
      // Thất bại → Tăng counter
      this.failures++;
      this.lastFailureTime = Date.now();

      // Nếu fail quá nhiều → Mở circuit (ngắt)
      if (this.failures >= this.threshold) {
        this.state = 'OPEN';
        console.error('Circuit breaker opened!'); // Đã ngắt → Không gọi API nữa
      }

      throw error;
    }
  }
}
// 💡 Cách hoạt động:
// - CLOSED: Gọi API bình thường
// - Fail 5 lần liên tiếp → OPEN (ngắt) → Không gọi API nữa, trả lỗi ngay
// - Sau 60s → HALF_OPEN → Thử lại 1 lần
//   - Nếu thành công → CLOSED (hoạt động bình thường)
//   - Nếu fail → OPEN (ngắt lại)
// ✅ Bảo vệ server khỏi quá tải khi server đang down

const breaker = new CircuitBreaker(5, 60000);

async function fetchWithCircuitBreaker() {
  return breaker.execute(() => fetch('/api/data').then((r) => r.json()));
}
```

---

#### **4️⃣ Concurrency Control - Kiểm Soát Đồng Thời**

**🔹 Problem: Too many concurrent requests - Quá nhiều request đồng thời**

```typescript
// ❌ VẤN ĐỀ: Xử lý 1000 items cùng lúc → Quá tải server
async function processAllItems(items: any[]) {
  const results = await Promise.all(
    items.map((item) => processItem(item)) // 1000 requests cùng lúc! 💥
  );
  return results;
}
// ⚠️ Vấn đề:
// - 1000 requests cùng lúc → Server quá tải → Có thể crash
// - Browser có thể block (quá nhiều connections)
// - Có thể bị rate limit (giới hạn số request/giây)
// → Cần giới hạn số lượng request đồng thời

// ✅ GIẢI PHÁP 1: Batch processing - Xử lý theo lô
// Chia items thành các lô nhỏ, xử lý từng lô một (mỗi lô chạy song song)
async function processInBatches<T, R>(
  items: T[], // Danh sách items cần xử lý
  batchSize: number, // Số items mỗi lô (ví dụ: 100)
  processFn: (item: T) => Promise<R> // Hàm xử lý mỗi item
): Promise<R[]> {
  const results: R[] = [];

  // Chia items thành các lô, xử lý từng lô
  for (let i = 0; i < items.length; i += batchSize) {
    // Lấy 1 lô items (từ i đến i + batchSize)
    const batch = items.slice(i, i + batchSize);

    // Xử lý lô này song song (tất cả items trong lô chạy cùng lúc)
    const batchResults = await Promise.all(batch.map(processFn));
    results.push(...batchResults); // Thêm kết quả vào mảng

    // Log tiến độ
    console.log(
      `Processed ${Math.min(i + batchSize, items.length)}/${items.length}`
    );
  }

  return results;
}

// Sử dụng: Xử lý 100 items mỗi lô
const results = await processInBatches(items, 100, processItem);
// 💡 Cách hoạt động với 1000 items, batchSize = 100:
// - Lô 1: Items 0-99 → Xử lý song song (100 requests cùng lúc)
// - Lô 2: Items 100-199 → Xử lý song song (100 requests cùng lúc)
// - ...
// - Lô 10: Items 900-999 → Xử lý song song (100 requests cùng lúc)
// ✅ Chỉ có tối đa 100 requests cùng lúc → Không quá tải server

// ✅ GIẢI PHÁP 2: Concurrency limit với p-limit pattern
class ConcurrencyLimiter {
  private queue: Array<() => Promise<any>> = [];
  private running = 0;

  constructor(private limit: number) {}

  async run<T>(fn: () => Promise<T>): Promise<T> {
    while (this.running >= this.limit) {
      await new Promise((resolve) => setTimeout(resolve, 10));
    }

    this.running++;

    try {
      return await fn();
    } finally {
      this.running--;
    }
  }
}

const limiter = new ConcurrencyLimiter(10); // Max 10 concurrent

async function processAllItemsWithLimit(items: any[]) {
  const results = await Promise.all(
    items.map((item) => limiter.run(() => processItem(item)))
  );
  return results;
}

// ✅ GIẢI PHÁP 3: Queue với worker pool
class WorkerPool<T, R> {
  private queue: T[] = [];
  private workers: number = 0;
  private results: R[] = [];
  private resolvePromise?: (value: R[]) => void;

  constructor(
    private maxWorkers: number,
    private processFn: (item: T) => Promise<R>
  ) {}

  async process(items: T[]): Promise<R[]> {
    this.queue = [...items];
    this.results = [];

    return new Promise((resolve) => {
      this.resolvePromise = resolve;

      // Start workers
      for (let i = 0; i < Math.min(this.maxWorkers, items.length); i++) {
        this.startWorker();
      }
    });
  }

  private async startWorker() {
    this.workers++;

    while (this.queue.length > 0) {
      const item = this.queue.shift()!;

      try {
        const result = await this.processFn(item);
        this.results.push(result);
      } catch (error) {
        console.error('Worker error:', error);
      }
    }

    this.workers--;

    // All workers done?
    if (this.workers === 0 && this.resolvePromise) {
      this.resolvePromise(this.results);
    }
  }
}

// Usage
const pool = new WorkerPool(5, processItem); // 5 workers
const results = await pool.process(items);
```

---

#### **6️⃣ Sequential Execution - Chạy Promises Theo Thứ Tự**

**🔹 Problem: Promise.all chạy SONG SONG, không theo thứ tự**

```typescript
// ❌ Promise.all chạy ĐỒNG THỜI
const results = await Promise.all(items.map((item) => processItem(item)));
// ⚠️ TẤT CẢ chạy cùng lúc! Item 3 có thể xong trước item 1
// ⚠️ Server có thể quá tải (1000 requests cùng lúc)
```

---

### **✅ Giải Pháp: 4 Cách Chạy Sequential**

#### **1. For...of Loop (Đơn giản nhất - Khuyến nghị) ⭐**

```typescript
// ✅ Chạy TUẦN TỰ - Đợi xong mới chạy tiếp
// Mỗi item được xử lý một cách tuần tự, đợi item trước xong mới xử lý item sau
async function processSequential(items: string[]) {
  const results = [];

  // for...of loop: Lặp qua từng item, đợi xong mới tiếp tục
  for (const item of items) {
    const result = await processItem(item); // Đợi item này xong
    results.push(result); // Mới xử lý item tiếp theo
  }

  return results;
}
// 💡 Tại sao dùng for...of?
// - Đơn giản, dễ hiểu
// - Đảm bảo thứ tự (item 1 → item 2 → item 3)
// - Không quá tải server (chỉ 1 request tại một thời điểm)

// Ví dụ: Các bước API phụ thuộc nhau (phải chạy tuần tự)
// Bước 1: Validate → Lấy token
const step1 = await fetch('/api/validate').then((r) => r.json());
// Bước 2: Upload → Cần token từ step1
const step2 = await fetch('/api/upload', {
  headers: { token: step1.token }, // Phải đợi step1 xong mới có token
}).then((r) => r.json());
// Bước 3: Save → Cần fileId từ step2
const step3 = await fetch('/api/save', {
  body: JSON.stringify({ fileId: step2.fileId }), // Phải đợi step2 xong mới có fileId
}).then((r) => r.json());
// ✅ Phải chạy tuần tự vì mỗi bước cần kết quả của bước trước
```

#### **2. Reduce Pattern**

```typescript
// Functional programming style
const results = await items.reduce(async (prevPromise, item) => {
  const acc = await prevPromise; // Đợi promise trước
  const result = await processItem(item);
  return [...acc, result];
}, Promise.resolve([]));
```

#### **3. Generator Pattern - Pattern Generator**

```typescript
// Cập nhật real-time: Emit (phát ra) kết quả ngay khi xong từng item
// async function*: Async generator function → Có thể yield (phát ra) giá trị từng cái một
async function* processWithProgress(items: string[]) {
  for (const item of items) {
    const result = await processItem(item); // Xử lý item
    yield result; // Emit (phát ra) kết quả ngay khi xong → Không cần đợi tất cả
  }
}

// Sử dụng: Cập nhật UI từng kết quả (real-time progress)
for await (const result of processWithProgress(items)) {
  updateUI(result); // Cập nhật UI ngay khi có kết quả (không cần đợi tất cả)
  console.log('Progress:', result);
}
// 💡 Ưu điểm:
// - Hiển thị progress bar real-time (0% → 10% → 20% → ... → 100%)
// - User thấy tiến độ ngay, không phải đợi đến khi xong hết
// - Có thể cancel giữa chừng nếu cần
// ✅ Dùng khi: Cần hiển thị progress, xử lý dữ liệu lớn
```

#### **4. Batched (Cân bằng Speed + Server Load)**

```typescript
// Xử lý 10 items/lần (giữa parallel và sequential)
async function processBatched(items: string[], batchSize = 10) {
  const results = [];

  for (let i = 0; i < items.length; i += batchSize) {
    const batch = items.slice(i, i + batchSize);
    const batchResults = await Promise.all(
      batch.map((item) => processItem(item))
    );
    results.push(...batchResults);
  }

  return results;
}
```

---

### **📊 So Sánh Performance**

```typescript
// 5 items, mỗi item mất 1 giây

// Promise.all (Parallel): ~1s (tất cả cùng lúc)
await Promise.all(items.map(processItem));

// for...of (Sequential): ~5s (từng cái một)
for (const item of items) await processItem(item);

// Batched (2 items/batch): ~3s (cân bằng)
await processBatched(items, 2);
```

**Bảng So Sánh:**

```
┌──────────────┬────────┬────────┬─────────────┬──────────────────┐
│ Pattern      │ Speed  │ Order  │ Server Load │ Use Case         │
├──────────────┼────────┼────────┼─────────────┼──────────────────┤
│ Promise.all  │ ⚡⚡⚡⚡ │ ❌     │ 🔥🔥🔥🔥    │ Tasks độc lập    │
│ for...of     │ ⚡     │ ✅     │ ✅          │ Tasks phụ thuộc  │
│ generator    │ ⚡     │ ✅     │ ✅          │ Real-time update │
│ batched      │ ⚡⚡⚡  │ ⚠️     │ ⚡⚡        │ Cân bằng        │
└──────────────┴────────┴────────┴─────────────┴──────────────────┘
```

---

### **🎯 Real-World Examples**

```typescript
// Example 1: Multi-step Form (Phải theo thứ tự)
async function submitForm(data: any) {
  const validated = await fetch('/api/validate', { body: data });
  const uploaded = await fetch('/api/upload', {
    headers: { token: validated.token },
  });
  const saved = await fetch('/api/save', { body: { fileId: uploaded.fileId } });
  return saved;
}

// Example 2: Rate-Limited API (1 request/giây)
async function fetchWithRateLimit(urls: string[]) {
  const results = [];
  for (let i = 0; i < urls.length; i++) {
    results.push(await fetch(urls[i]).then((r) => r.json()));
    if (i < urls.length - 1) await new Promise((r) => setTimeout(r, 1000));
  }
  return results;
}

// Example 3: Database Migrations (Phải đúng thứ tự)
for (const migration of migrations) {
  await migration.up();
  await db.log({ name: migration.name, date: Date.now() });
}
```

---

### **🚨 Common Mistakes**

```typescript
// ❌ LỖI 1: forEach không đợi async
items.forEach(async (item) => {
  await processItem(item); // ❌ forEach không đợi!
});

// ✅ ĐÚNG: Dùng for...of
for (const item of items) {
  await processItem(item);
}

// ❌ LỖI 2: map tạo array of promises
const results = items.map(async (item) => await processItem(item));
// results = [Promise, Promise, ...] ❌

// ✅ ĐÚNG: Thêm Promise.all hoặc for...of
const results = await Promise.all(items.map(processItem));

// ❌ LỖI 3: reduce không await accumulator
const results = items.reduce(async (acc, item) => {
  acc.push(await processItem(item)); // ❌ acc là Promise!
  return acc;
}, []);

// ✅ ĐÚNG: Await accumulator
const results = await items.reduce(async (prevPromise, item) => {
  const acc = await prevPromise; // ✅
  return [...acc, await processItem(item)];
}, Promise.resolve([]));
```

---

### **💡 Best Practices**

**Khi nào dùng gì?**

```typescript
// ✅ Tasks ĐỘC LẬP → Promise.all (parallel)
const [users, posts, comments] = await Promise.all([
  fetchUsers(),
  fetchPosts(),
  fetchComments()
]);

// ✅ Tasks PHỤ THUỘC → for...of (sequential)
const token = await login();
const data = await fetchData(token);
const saved = await saveData(data);

// ✅ Rate Limit / Server Load → Batched
await processBatched(1000items, 50); // 50 items/lần

// ✅ Real-time Updates → Generator
for await (const progress of uploadFiles(files)) {
  updateProgressBar(progress);
}
```

---

#### **5️⃣ Async Iteration - Xử Lý Dữ Liệu Stream**

**🔹 Problem: Process large datasets - Xử lý dữ liệu lớn**

```typescript
// ❌ VẤN ĐỀ: Load tất cả dữ liệu vào memory → Có thể hết RAM
async function processAllUsers() {
  const users = await fetchAllUsers(); // 1 triệu users! 💥
  // ⚠️ Vấn đề:
  // - Load 1 triệu users vào memory → Có thể hết RAM
  // - Phải đợi tải hết mới bắt đầu xử lý → Chậm
  // - Nếu server chỉ trả về 1 triệu users → Response quá lớn

  for (const user of users) {
    await processUser(user);
  }
}
// ❌ Không hiệu quả với dữ liệu lớn → Cần xử lý từng phần (streaming/pagination)

// ✅ GIẢI PHÁP 1: Async Generator - Generator bất đồng bộ
// Async generator: Tải dữ liệu từng trang (page), yield từng user một
// → Không cần load tất cả vào memory, xử lý từng user một
async function* fetchUsersPaginated(pageSize = 100) {
  let page = 0; // Bắt đầu từ trang 0

  while (true) {
    // Tải 1 trang users (100 users mỗi trang)
    const users = await fetch(`/api/users?page=${page}&size=${pageSize}`).then(
      (r) => r.json()
    );

    // Nếu không còn users → Dừng
    if (users.length === 0) break;

    // yield*: Phát ra từng user trong mảng users
    // → Không cần load tất cả vào memory, chỉ xử lý từng user
    yield* users; // Yield each user (phát ra từng user một)
    page++; // Trang tiếp theo
  }
}

// Sử dụng: Xử lý từng user một (không cần load tất cả vào memory)
for await (const user of fetchUsersPaginated()) {
  await processUser(user); // Xử lý user này
  console.log(`Processed user ${user.id}`);
  // → Chỉ có 1 user trong memory tại một thời điểm
}
// 💡 Ưu điểm:
// - Không cần load tất cả 1 triệu users vào memory
// - Chỉ tải 100 users mỗi lần (pagination)
// - Xử lý từng user một → Tiết kiệm RAM
// - Có thể cancel giữa chừng nếu cần

// ✅ GIẢI PHÁP 2: Stream processing
async function processUsersStream() {
  const stream = fetchUsersPaginated();

  for await (const user of stream) {
    try {
      await processUser(user);
    } catch (error) {
      console.error(`Failed to process user ${user.id}:`, error);
      // Continue với user tiếp theo
    }
  }

  console.log('All users processed');
}

// ✅ GIẢI PHÁP 3: Transform stream
async function* transformUsers(
  source: AsyncIterable<User>,
  transformFn: (user: User) => Promise<TransformedUser>
) {
  for await (const user of source) {
    yield await transformFn(user);
  }
}

// Usage: Chain transformations
const userStream = fetchUsersPaginated();
const enrichedStream = transformUsers(userStream, enrichUser);
const validatedStream = transformUsers(enrichedStream, validateUser);

for await (const user of validatedStream) {
  console.log('Processed:', user);
}
```

---

#### **🎯 Advanced Patterns - Tổng Hợp**

```typescript
// =====================================
// ASYNC UTILS LIBRARY
// =====================================

class AsyncUtils {
  // 1. Retry với exponential backoff
  static async retry<T>(
    fn: () => Promise<T>,
    options = { maxRetries: 3, delay: 1000, backoff: 2 }
  ): Promise<T> {
    let lastError: Error;

    for (let attempt = 0; attempt <= options.maxRetries; attempt++) {
      try {
        return await fn();
      } catch (error) {
        lastError = error as Error;

        if (attempt < options.maxRetries) {
          const delay = options.delay * Math.pow(options.backoff, attempt);
          await new Promise((resolve) => setTimeout(resolve, delay));
        }
      }
    }

    throw lastError!;
  }

  // 2. Timeout wrapper
  static withTimeout<T>(promise: Promise<T>, timeoutMs: number): Promise<T> {
    return Promise.race([
      promise,
      new Promise<never>((_, reject) => {
        setTimeout(() => reject(new Error('Timeout')), timeoutMs);
      }),
    ]);
  }

  // 3. Debounced async function
  static debounce<T extends (...args: any[]) => Promise<any>>(
    fn: T,
    delayMs: number
  ): T {
    let timeoutId: NodeJS.Timeout | null = null;

    return ((...args: any[]) => {
      return new Promise((resolve, reject) => {
        if (timeoutId) clearTimeout(timeoutId);

        timeoutId = setTimeout(() => {
          fn(...args)
            .then(resolve)
            .catch(reject);
        }, delayMs);
      });
    }) as T;
  }

  // 4. Parallel với concurrency limit
  static async parallel<T, R>(
    items: T[],
    fn: (item: T) => Promise<R>,
    concurrency: number
  ): Promise<R[]> {
    const results: R[] = [];
    const executing: Promise<void>[] = [];

    for (const item of items) {
      const promise = fn(item).then((result) => {
        results.push(result);
      });

      executing.push(promise);

      if (executing.length >= concurrency) {
        await Promise.race(executing);
        executing.splice(
          executing.findIndex((p) => p === promise),
          1
        );
      }
    }

    await Promise.all(executing);
    return results;
  }

  // 5. Sleep utility
  static sleep(ms: number): Promise<void> {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }
}

// =====================================
// USAGE EXAMPLES
// =====================================

// Retry API call
const data = await AsyncUtils.retry(
  () => fetch('/api/data').then((r) => r.json()),
  { maxRetries: 3, delay: 1000, backoff: 2 }
);

// Timeout request
const user = await AsyncUtils.withTimeout(
  fetch('/api/user').then((r) => r.json()),
  5000
);

// Debounced search
const debouncedSearch = AsyncUtils.debounce(async (term: string) => {
  const results = await fetch(`/api/search?q=${term}`).then((r) => r.json());
  displayResults(results);
}, 300);

// Process với concurrency limit
const results = await AsyncUtils.parallel(
  items,
  processItem,
  10 // Max 10 concurrent
);
```

---

#### **💡 Best Practices - Tổng Hợp**

**✅ DO:**

1. **Always handle errors**: Try-catch trong async functions
2. **Set timeouts**: Prevent hanging requests
3. **Limit concurrency**: Avoid overwhelming server
4. **Use AbortController**: Cancel unnecessary requests
5. **Implement retry logic**: Handle transient failures
6. **Debounce user input**: Reduce API calls
7. **Stream large data**: Don't load all vào memory
8. **Monitor performance**: Track slow operations

**❌ DON'T:**

1. **Unhandled rejections**: Always catch errors
2. **Infinite retries**: Set max retry limit
3. **Unlimited concurrency**: Control parallel operations
4. **Ignore race conditions**: Handle out-of-order responses
5. **Block UI**: Break long operations into chunks
6. **Forget cleanup**: Cancel pending operations on unmount

---

**🎯 Kết Luận:**

Async programming phức tạp hơn sync nhiều do:

- **Error handling** khó hơn (unhandled rejections)
- **Race conditions** (out-of-order responses)
- **Timeout & retry** logic
- **Concurrency control** (avoid overwhelming)
- **Memory management** (streaming large data)

**📌 Promise Combinators Examples - Ví Dụ Các Phương Thức Kết Hợp Promise:**

```typescript
// ============================================
// 1. Promise.all - Tất cả phải thành công
// ============================================
// Chạy tất cả promises song song, đợi TẤT CẢ xong
// Nếu 1 promise fail → Tất cả fail (fail-fast)
const [users, posts, comments] = await Promise.all([
  fetch('/api/users').then((r) => r.json()), // Request 1
  fetch('/api/posts').then((r) => r.json()), // Request 2 (chạy song song)
  fetch('/api/comments').then((r) => r.json()), // Request 3 (chạy song song)
]);
// ✅ Dùng khi: Cần TẤT CẢ dữ liệu, không thể thiếu cái nào
// ❌ Nếu 1 request fail → Tất cả fail

// ============================================
// 2. Promise.any - 1 thành công là đủ (fallback)
// ============================================
// Chạy tất cả promises song song, chỉ cần 1 cái thành công
// Nếu TẤT CẢ fail → Reject với AggregateError
const data = await Promise.any([
  fetch('/api/primary'), // Server chính
  fetch('/api/backup1'), // Server dự phòng 1
  fetch('/api/backup2'), // Server dự phòng 2
]);
// ✅ Dùng khi: Có nhiều nguồn dữ liệu, chỉ cần 1 cái thành công
// → Tự động fallback sang server khác nếu server chính fail

// ============================================
// 3. Promise.race - Ai nhanh nhất thắng
// ============================================
// Chạy tất cả promises song song, lấy kết quả của cái xong TRƯỚC (nhanh nhất)
// Có thể là thành công hoặc thất bại (cái nào xong trước)
const result = await Promise.race([
  fetch('/api/data'), // Request thật
  new Promise((_, reject) => setTimeout(() => reject('Timeout'), 5000)), // Timeout
]);
// ✅ Dùng khi: Tạo timeout, lấy kết quả nhanh nhất
// → Nếu request quá 5s → Timeout thắng → Reject với 'Timeout'

// ============================================
// 4. Promise.allSettled - Đợi tất cả complete
// ============================================
// Chạy tất cả promises song song, đợi TẤT CẢ xong (thành công hoặc thất bại)
// KHÔNG BAO GIỜ reject → Luôn resolve với mảng kết quả
const results = await Promise.allSettled([
  fetch('/api/1'),
  fetch('/api/2'),
  fetch('/api/3'),
]);
// Kết quả: Mảng các object { status, value/reason }
// [
//   { status: 'fulfilled', value: ... },  // Thành công
//   { status: 'rejected', reason: ... },   // Thất bại
//   { status: 'fulfilled', value: ... }     // Thành công
// ]
// ✅ Dùng khi: Cần biết kết quả của TẤT CẢ, kể cả những cái fail
// → Không bị fail-fast như Promise.all
```

Nhưng với đúng patterns và tools, bạn có thể xử lý mọi tình huống async một cách hiệu quả! 🚀

---
