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

## **🎯 10 BEST ASYNC SCENARIOS FOR PRODUCTION**
## **10 Kịch Bản Xử Lý Bất Đồng Bộ Hay Nhất Trong Production**

### **Scenario 1: Parallel Data Fetching với Error Isolation**
### **Kịch Bản 1: Tải Dữ Liệu Song Song với Cách Ly Lỗi**

```typescript
// 💡 Problem: Cần load nhiều data sources, nhưng 1 source fail không nên crash toàn bộ page
// 💡 Solution: Promise.allSettled + fallback values

interface DashboardData {
  user: User | null;
  stats: Stats | null;
  notifications: Notification[] | null;
  recentActivity: Activity[] | null;
}

async function loadDashboard(userId: string): Promise<DashboardData> {
  // 💡 Promise.allSettled: Đợi TẤT CẢ xong, không fail-fast như Promise.all
  const results = await Promise.allSettled([
    fetchUser(userId),           // 💡 Request 1: Lấy user data
    fetchStats(userId),          // 💡 Request 2: Lấy stats (chạy song song)
    fetchNotifications(userId),  // 💡 Request 3: Lấy notifications (song song)
    fetchRecentActivity(userId), // 💡 Request 4: Lấy recent activity (song song)
  ]);

  // 💡 Extract results với type-safe checking
  const dashboard: DashboardData = {
    // 💡 results[0]: User result
    user: results[0].status === 'fulfilled' ? results[0].value : null,
    
    // 💡 results[1]: Stats result - Nếu fail, dùng fallback empty stats
    stats: results[1].status === 'fulfilled' 
      ? results[1].value 
      : { views: 0, likes: 0, shares: 0 }, // ✅ Fallback values
    
    // 💡 results[2]: Notifications - Nếu fail, show empty array
    notifications: results[2].status === 'fulfilled' 
      ? results[2].value 
      : [], // ✅ Empty array thay vì null → Không cần null check khi render
    
    // 💡 results[3]: Activity - Tương tự notifications
    recentActivity: results[3].status === 'fulfilled' 
      ? results[3].value 
      : [],
  };

  // 💡 Log errors cho debugging (không crash app)
  results.forEach((result, index) => {
    if (result.status === 'rejected') {
      const sources = ['User', 'Stats', 'Notifications', 'Activity'];
      console.error(`Failed to load ${sources[index]}:`, result.reason);
      // ✅ Report to monitoring service (Sentry, DataDog)
      analytics.trackError('DashboardLoadFailure', {
        source: sources[index],
        error: result.reason,
      });
    }
  });

  return dashboard;
}

// 💡 Usage trong React component
function DashboardPage() {
  const [data, setData] = useState<DashboardData | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    loadDashboard('user-123')
      .then(setData)
      .finally(() => setIsLoading(false)); // ✅ Luôn set loading = false
  }, []);

  if (isLoading) return <Spinner />;

  // ✅ Partial data rendering: Show những gì có, hide những gì null
  return (
    <div>
      {data?.user && <UserProfile user={data.user} />}
      {data?.stats && <StatsWidget stats={data.stats} />}
      {data?.notifications && <NotificationList items={data.notifications} />}
      {data?.recentActivity && <ActivityFeed items={data.recentActivity} />}
    </div>
  );
}
```

**🎯 Ưu điểm:**
- ✅ 4 requests chạy song song → Total time = max(requests) thay vì sum
- ✅ 1 request fail không làm crash toàn bộ dashboard
- ✅ Fallback values → UI luôn có data để render
- ✅ Error tracking → Biết chính xác request nào fail

---

### **Scenario 2: Smart Retry với Exponential Backoff**
### **Kịch Bản 2: Thử Lại Thông Minh với Exponential Backoff**

```typescript
// 💡 Problem: API đôi khi fail tạm thời (network glitch, server restart)
// 💡 Solution: Retry với exponential backoff + jitter

interface RetryOptions {
  maxRetries: number;      // 💡 Số lần retry tối đa
  initialDelay: number;    // 💡 Delay ban đầu (ms)
  maxDelay: number;        // 💡 Delay tối đa (ms)
  backoffMultiplier: number; // 💡 Hệ số nhân (thường 2)
  shouldRetry?: (error: any) => boolean; // 💡 Check xem có nên retry không
}

async function fetchWithRetry<T>(
  fn: () => Promise<T>,
  options: RetryOptions
): Promise<T> {
  const {
    maxRetries,
    initialDelay,
    maxDelay,
    backoffMultiplier = 2,
    shouldRetry = (error) => {
      // 💡 Default: Chỉ retry nếu network error hoặc 5xx server error
      return error.code === 'NETWORK_ERROR' || 
             (error.status >= 500 && error.status < 600);
    }
  } = options;

  let lastError: any;
  let currentDelay = initialDelay;

  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      // 💡 Attempt 0: First try (no delay)
      // 💡 Attempt 1+: Retry với delay
      if (attempt > 0) {
        // 💡 Exponential backoff: delay = initialDelay * (multiplier ^ attempt)
        // 💡 Ví dụ: 1s → 2s → 4s → 8s → 16s
        const delay = Math.min(currentDelay, maxDelay);
        
        // 💡 Jitter: Thêm random -25% → +25% để tránh thundering herd
        // (nhiều clients retry cùng lúc → overload server)
        const jitter = delay * 0.25 * (Math.random() * 2 - 1);
        const delayWithJitter = delay + jitter;

        console.log(`⏳ Retry attempt ${attempt}/${maxRetries} sau ${delayWithJitter}ms`);
        await sleep(delayWithJitter);
        
        // 💡 Tăng delay cho lần retry tiếp theo
        currentDelay *= backoffMultiplier;
      }

      // 💡 Execute function
      const result = await fn();
      
      // ✅ Success! Return result
      if (attempt > 0) {
        console.log(`✅ Retry thành công sau ${attempt} attempts`);
      }
      return result;

    } catch (error) {
      lastError = error;
      
      // 💡 Check xem có nên retry không
      if (!shouldRetry(error)) {
        console.error(`❌ Error không thể retry:`, error);
        throw error; // ❌ 4xx client errors → Không retry
      }

      // 💡 Nếu đã hết số lần retry → throw error
      if (attempt === maxRetries) {
        console.error(`❌ Retry thất bại sau ${maxRetries} attempts`);
        throw new Error(`Failed after ${maxRetries} retries: ${lastError.message}`);
      }

      // 💡 Còn retry → Log và continue loop
      console.warn(`⚠️ Attempt ${attempt + 1} failed, retrying...`, error);
    }
  }

  // 💡 Không bao giờ reach đây (throw ở trên)
  throw lastError;
}

// 💡 Helper: Sleep function
const sleep = (ms: number) => new Promise(resolve => setTimeout(resolve, ms));

// ✅ Usage Example 1: Retry API call
async function fetchUserWithRetry(userId: string) {
  return fetchWithRetry(
    () => fetch(`/api/users/${userId}`).then(r => {
      if (!r.ok) throw { status: r.status, message: r.statusText };
      return r.json();
    }),
    {
      maxRetries: 3,           // 💡 Retry tối đa 3 lần
      initialDelay: 1000,      // 💡 Bắt đầu với 1s
      maxDelay: 10000,         // 💡 Tối đa 10s
      backoffMultiplier: 2,    // 💡 Nhân đôi mỗi lần: 1s → 2s → 4s
      shouldRetry: (error) => {
        // ❌ Không retry 4xx client errors (bad request, not found, etc.)
        if (error.status >= 400 && error.status < 500) return false;
        // ✅ Retry network errors và 5xx server errors
        return true;
      }
    }
  );
}

// ✅ Usage Example 2: Retry với custom logic
async function sendAnalytics(event: AnalyticsEvent) {
  return fetchWithRetry(
    () => fetch('/api/analytics', {
      method: 'POST',
      body: JSON.stringify(event),
    }),
    {
      maxRetries: 5,           // 💡 Analytics không critical → Retry nhiều hơn
      initialDelay: 500,       // 💡 Delay ngắn hơn
      maxDelay: 30000,         // 💡 Max 30s
      backoffMultiplier: 2,
      shouldRetry: (error) => {
        // ✅ Analytics luôn retry (trừ khi explicitly cancelled)
        return error.name !== 'AbortError';
      }
    }
  );
}
```

**🎯 Timeline của Retry:**
```
Attempt 0: Execute immediately                → Fail
Delay: 1s + jitter (-250ms to +250ms)         = ~1s
Attempt 1: Execute after ~1s                   → Fail  
Delay: 2s + jitter (-500ms to +500ms)         = ~2s
Attempt 2: Execute after ~2s                   → Fail
Delay: 4s + jitter (-1s to +1s)               = ~4s
Attempt 3: Execute after ~4s                   → Success ✅

Total time: ~7s (thay vì fail ngay lập tức)
```

**🎯 Ưu điểm:**
- ✅ Exponential backoff → Không spam server
- ✅ Jitter → Tránh thundering herd (nhiều clients retry cùng lúc)
- ✅ Max delay → Không đợi quá lâu
- ✅ Selective retry → Không retry 4xx errors (vô nghĩa)
- ✅ Configurable → Dễ tune cho từng use case

---

### **Scenario 3: Request Deduplication (Cache-While-Revalidate)**
### **Kịch Bản 3: Loại Bỏ Request Trùng Lặp**

```typescript
// 💡 Problem: Nhiều components cùng fetch data → Tạo duplicate requests
// 💡 Solution: Request deduplication với in-flight cache

class RequestDeduplicator {
  // 💡 Map: key → Promise đang chạy
  private inFlightRequests = new Map<string, Promise<any>>();
  
  // 💡 Map: key → cached result + timestamp
  private cache = new Map<string, { data: any; timestamp: number }>();

  constructor(
    private cacheTTL: number = 5000 // 💡 Cache TTL (ms) - mặc định 5s
  ) {}

  async fetch<T>(
    key: string,
    fetcher: () => Promise<T>,
    options?: {
      ttl?: number;           // 💡 Override TTL cho request này
      forceRefresh?: boolean; // 💡 Bỏ qua cache, force fetch mới
    }
  ): Promise<T> {
    const ttl = options?.ttl ?? this.cacheTTL;

    // 💡 Step 1: Check cache (nếu không force refresh)
    if (!options?.forceRefresh) {
      const cached = this.cache.get(key);
      if (cached) {
        const age = Date.now() - cached.timestamp;
        if (age < ttl) {
          console.log(`✅ Cache hit: ${key} (age: ${age}ms)`);
          return cached.data as T;
        }
        // 💡 Cache expired → Remove
        console.log(`⏰ Cache expired: ${key} (age: ${age}ms > ${ttl}ms)`);
        this.cache.delete(key);
      }
    }

    // 💡 Step 2: Check nếu request đang chạy (in-flight)
    const inFlight = this.inFlightRequests.get(key);
    if (inFlight) {
      console.log(`⏳ Reusing in-flight request: ${key}`);
      return inFlight as Promise<T>; // ✅ Reuse promise đang chạy
    }

    // 💡 Step 3: Create new request
    console.log(`🚀 New request: ${key}`);
    const promise = fetcher()
      .then(result => {
        // ✅ Success → Cache result
        this.cache.set(key, {
          data: result,
          timestamp: Date.now(),
        });
        return result;
      })
      .finally(() => {
        // 💡 Cleanup: Remove from in-flight (dù success hay fail)
        this.inFlightRequests.delete(key);
      });

    // 💡 Store promise vào in-flight map
    this.inFlightRequests.set(key, promise);

    return promise;
  }

  // 💡 Invalidate cache cho key cụ thể
  invalidate(key: string) {
    this.cache.delete(key);
    console.log(`🗑️ Cache invalidated: ${key}`);
  }

  // 💡 Clear toàn bộ cache
  clearAll() {
    this.cache.clear();
    this.inFlightRequests.clear();
    console.log(`🗑️ All cache cleared`);
  }

  // 💡 Get cache stats
  getStats() {
    return {
      cacheSize: this.cache.size,
      inFlightCount: this.inFlightRequests.size,
    };
  }
}

// 💡 Global instance
const apiCache = new RequestDeduplicator(5000); // 5s TTL

// ✅ Usage trong API client
async function fetchUser(userId: string) {
  return apiCache.fetch(
    `user:${userId}`, // 💡 Unique key
    () => fetch(`/api/users/${userId}`).then(r => r.json()),
    { ttl: 10000 } // 💡 User data cache 10s
  );
}

// ✅ Usage trong React components
function UserProfile({ userId }: { userId: string }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    // 💡 Nếu nhiều components mount cùng lúc → Chỉ 1 request thực sự được gửi
    fetchUser(userId).then(setUser);
  }, [userId]);

  return <div>{user?.name}</div>;
}

function UserAvatar({ userId }: { userId: string }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    // 💡 Reuse request từ UserProfile (nếu đang chạy) hoặc cache (nếu đã có)
    fetchUser(userId).then(setUser);
  }, [userId]);

  return <img src={user?.avatar} />;
}

// ✅ Manual invalidation sau khi update
async function updateUser(userId: string, data: Partial<User>) {
  await fetch(`/api/users/${userId}`, {
    method: 'PATCH',
    body: JSON.stringify(data),
  });

  // 💡 Invalidate cache → Next fetch sẽ lấy data mới
  apiCache.invalidate(`user:${userId}`);
}
```

**🎯 Scenarios:**

**Scenario A: Parallel Components (Cùng mount lúc)**
```
Time 0ms:  UserProfile mounts → fetchUser('123') → Start request
Time 1ms:  UserAvatar mounts → fetchUser('123') → Reuse in-flight request ✅
Time 100ms: Request completes → Both components receive data
Result: 1 request thay vì 2
```

**Scenario B: Sequential Components (Mount lần lượt)**
```
Time 0ms:    UserProfile mounts → fetchUser('123') → Start request
Time 100ms:  Request completes → Cache stored
Time 200ms:  UserAvatar mounts → fetchUser('123') → Return from cache ✅
Result: 0 additional requests (cache hit)
```

**Scenario C: Cache Expiration**
```
Time 0ms:     fetchUser('123') → Cache result (TTL=5000ms)
Time 3000ms:  fetchUser('123') → Cache hit (age=3s < 5s) ✅
Time 6000ms:  fetchUser('123') → Cache expired → New request 🚀
```

**🎯 Ưu điểm:**
- ✅ Reduce duplicate requests → Save bandwidth, server load
- ✅ In-flight deduplication → Nhiều components cùng fetch → 1 request
- ✅ Cache với TTL → Reduce requests cho data ít thay đổi
- ✅ Manual invalidation → Control cache freshness

---

### **Scenario 4: Timeout với Cleanup**
### **Kịch Bản 4: Timeout với Dọn Dẹp Resources**

```typescript
// 💡 Problem: Long-running requests block UI, cần timeout + cleanup
// 💡 Solution: AbortController + timeout + resource cleanup

interface FetchOptions {
  timeout?: number;                    // 💡 Timeout (ms)
  onProgress?: (progress: number) => void; // 💡 Progress callback
  signal?: AbortSignal;                // 💡 External abort signal
}

class TimeoutError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'TimeoutError';
  }
}

async function fetchWithTimeout<T>(
  url: string,
  options: FetchOptions = {}
): Promise<T> {
  const {
    timeout = 30000, // 💡 Default 30s timeout
    onProgress,
    signal: externalSignal,
  } = options;

  // 💡 Create AbortController for timeout
  const timeoutController = new AbortController();
  
  // 💡 Combine external signal (nếu có) với timeout signal
  const signals = [timeoutController.signal];
  if (externalSignal) signals.push(externalSignal);

  // 💡 Merged signal: Abort nếu BẤT KỲ signal nào abort
  const mergedSignal = AbortSignal.any
    ? AbortSignal.any(signals) // ✅ Native API (Chrome 116+)
    : timeoutController.signal; // ⚠️ Fallback (không support external signal)

  // 💡 Setup timeout
  const timeoutId = setTimeout(() => {
    console.warn(`⏰ Request timeout sau ${timeout}ms: ${url}`);
    timeoutController.abort(new TimeoutError(`Request timeout sau ${timeout}ms`));
  }, timeout);

  try {
    // 💡 Fetch với abort signal
    const response = await fetch(url, {
      signal: mergedSignal, // ✅ Request sẽ bị abort nếu timeout hoặc external abort
    });

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    // 💡 Handle progress (nếu có onProgress callback)
    if (onProgress && response.body) {
      const reader = response.body.getReader();
      const contentLength = +(response.headers.get('Content-Length') ?? 0);
      
      let receivedLength = 0;
      const chunks: Uint8Array[] = [];

      while (true) {
        const { done, value } = await reader.read();
        
        if (done) break;

        chunks.push(value);
        receivedLength += value.length;

        // 💡 Report progress
        if (contentLength > 0) {
          const progress = (receivedLength / contentLength) * 100;
          onProgress(progress);
        }
      }

      // 💡 Combine chunks
      const allChunks = new Uint8Array(receivedLength);
      let position = 0;
      for (const chunk of chunks) {
        allChunks.set(chunk, position);
        position += chunk.length;
      }

      // 💡 Decode to text và parse JSON
      const text = new TextDecoder().decode(allChunks);
      return JSON.parse(text) as T;
    }

    // 💡 No progress tracking → Simple json()
    return await response.json();

  } catch (error: any) {
    // 💡 Handle different error types
    if (error.name === 'AbortError') {
      if (timeoutController.signal.aborted) {
        throw new TimeoutError(`Request timeout sau ${timeout}ms`);
      }
      throw new Error('Request bị cancel');
    }
    throw error;

  } finally {
    // ✅ CLEANUP: Clear timeout (quan trọng để tránh memory leak)
    clearTimeout(timeoutId);
  }
}

// ✅ Usage Example 1: Simple timeout
try {
  const data = await fetchWithTimeout('/api/large-dataset', {
    timeout: 5000, // 💡 5s timeout
  });
  console.log('Data loaded:', data);
} catch (error) {
  if (error instanceof TimeoutError) {
    console.error('⏰ Request quá chậm, đã timeout');
  } else {
    console.error('❌ Error:', error);
  }
}

// ✅ Usage Example 2: Progress tracking
const [progress, setProgress] = useState(0);

async function downloadFile() {
  try {
    const file = await fetchWithTimeout('/api/large-file', {
      timeout: 60000, // 💡 60s timeout cho large file
      onProgress: (p) => {
        setProgress(p); // 💡 Update progress bar
        console.log(`📥 Downloaded: ${p.toFixed(1)}%`);
      },
    });
    console.log('✅ File downloaded:', file);
  } catch (error) {
    if (error instanceof TimeoutError) {
      alert('Download quá chậm, vui lòng thử lại');
    }
  }
}

// ✅ Usage Example 3: Manual cancellation
function FileDownloader() {
  const [isDownloading, setIsDownloading] = useState(false);
  const abortControllerRef = useRef<AbortController>();

  const startDownload = async () => {
    setIsDownloading(true);
    abortControllerRef.current = new AbortController();

    try {
      const file = await fetchWithTimeout('/api/large-file', {
        timeout: 60000,
        signal: abortControllerRef.current.signal, // ✅ External signal
      });
      console.log('✅ Downloaded:', file);
    } catch (error) {
      if (error.message.includes('cancel')) {
        console.log('🛑 Download cancelled by user');
      }
    } finally {
      setIsDownloading(false);
    }
  };

  const cancelDownload = () => {
    abortControllerRef.current?.abort(); // ✅ Manual abort
    console.log('🛑 Cancelling download...');
  };

  return (
    <div>
      <button onClick={startDownload} disabled={isDownloading}>
        Download
      </button>
      {isDownloading && (
        <button onClick={cancelDownload}>Cancel</button>
      )}
    </div>
  );
}
```

**🎯 Ưu điểm:**
- ✅ Timeout protection → Không để request chạy mãi
- ✅ Manual cancellation → User có thể cancel operation
- ✅ Progress tracking → Better UX với progress bar
- ✅ Resource cleanup → Clear timeout để tránh memory leak
- ✅ Type-safe errors → TimeoutError vs AbortError vs network errors

---

### **Scenario 5: Batching Requests (Debounce + Queue)**
### **Kịch Bản 5: Gộp Requests (Debounce + Hàng Đợi)**

```typescript
// 💡 Problem: User typing → Mỗi keystroke tạo 1 API call → Spam server
// 💡 Solution: Batch requests với debounce + flush queue

class RequestBatcher<T, R> {
  private queue: Array<{
    input: T;
    resolve: (value: R) => void;
    reject: (error: any) => void;
  }> = [];
  
  private debounceTimer: NodeJS.Timeout | null = null;
  private isProcessing = false;

  constructor(
    private batchFn: (inputs: T[]) => Promise<R[]>, // 💡 Function xử lý batch
    private options: {
      debounceMs: number;    // 💡 Đợi bao lâu trước khi flush
      maxBatchSize?: number; // 💡 Max items per batch
      maxWaitMs?: number;    // 💡 Max time chờ (force flush)
    }
  ) {}

  async add(input: T): Promise<R> {
    // 💡 Create promise cho item này
    return new Promise<R>((resolve, reject) => {
      // 💡 Add vào queue
      this.queue.push({ input, resolve, reject });

      // 💡 Check nếu queue đầy → Force flush ngay
      if (this.options.maxBatchSize && this.queue.length >= this.options.maxBatchSize) {
        console.log(`📦 Batch size reached (${this.queue.length}), flushing...`);
        this.flush();
        return;
      }

      // 💡 Reset debounce timer
      if (this.debounceTimer) {
        clearTimeout(this.debounceTimer);
      }

      // 💡 Setup debounce: Flush sau debounceMs
      this.debounceTimer = setTimeout(() => {
        console.log(`⏰ Debounce timeout, flushing ${this.queue.length} items...`);
        this.flush();
      }, this.options.debounceMs);

      // 💡 Setup max wait timer (nếu có)
      if (this.options.maxWaitMs) {
        setTimeout(() => {
          if (this.queue.length > 0) {
            console.log(`⏰ Max wait time reached, flushing ${this.queue.length} items...`);
            this.flush();
          }
        }, this.options.maxWaitMs);
      }
    });
  }

  private async flush() {
    // 💡 Clear debounce timer
    if (this.debounceTimer) {
      clearTimeout(this.debounceTimer);
      this.debounceTimer = null;
    }

    // 💡 Skip nếu queue rỗng hoặc đang process
    if (this.queue.length === 0 || this.isProcessing) {
      return;
    }

    // 💡 Take items from queue
    const batch = this.queue.splice(0, this.queue.length);
    const inputs = batch.map(item => item.input);

    this.isProcessing = true;

    try {
      console.log(`🚀 Processing batch of ${inputs.length} items...`);
      
      // 💡 Execute batch function
      const results = await this.batchFn(inputs);

      // ✅ Resolve all promises với results
      batch.forEach((item, index) => {
        item.resolve(results[index]);
      });

      console.log(`✅ Batch processed successfully`);

    } catch (error) {
      // ❌ Reject all promises với same error
      console.error(`❌ Batch failed:`, error);
      batch.forEach(item => {
        item.reject(error);
      });

    } finally {
      this.isProcessing = false;

      // 💡 Check nếu có items mới trong queue → Process tiếp
      if (this.queue.length > 0) {
        console.log(`📦 Queue has ${this.queue.length} new items, processing...`);
        setTimeout(() => this.flush(), 0);
      }
    }
  }

  // 💡 Manual flush (force process queue ngay)
  async flushNow() {
    return this.flush();
  }

  // 💡 Get queue size
  getQueueSize() {
    return this.queue.length;
  }
}

// ✅ Example 1: Search suggestions với debounce
interface SearchResult {
  id: string;
  title: string;
}

// 💡 Batch function: Gửi 1 request với multiple queries
async function batchSearch(queries: string[]): Promise<SearchResult[][]> {
  const response = await fetch('/api/search/batch', {
    method: 'POST',
    body: JSON.stringify({ queries }),
  });
  return response.json();
}

// 💡 Create batcher
const searchBatcher = new RequestBatcher(batchSearch, {
  debounceMs: 300,      // 💡 Đợi 300ms sau keystroke cuối
  maxBatchSize: 10,     // 💡 Max 10 queries per request
  maxWaitMs: 1000,      // 💡 Flush sau max 1s (dù user vẫn đang type)
});

// ✅ Usage trong search component
function SearchBox() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<SearchResult[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleSearch = async (searchQuery: string) => {
    if (!searchQuery.trim()) {
      setResults([]);
      return;
    }

    setIsLoading(true);
    try {
      // 💡 Add to batch queue
      // 💡 Nếu user type nhiều ký tự liên tiếp → Gộp thành 1 request
      const searchResults = await searchBatcher.add(searchQuery);
      setResults(searchResults);
    } catch (error) {
      console.error('Search failed:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div>
      <input
        value={query}
        onChange={(e) => {
          const value = e.target.value;
          setQuery(value);
          handleSearch(value); // 💡 Gọi mỗi keystroke, nhưng sẽ được batch
        }}
        placeholder="Search..."
      />
      {isLoading && <div>Loading...</div>}
      <ul>
        {results.map(item => (
          <li key={item.id}>{item.title}</li>
        ))}
      </ul>
    </div>
  );
}
```

**🎯 Timeline Example:**
```
Time 0ms:    User types 'h'   → Add to queue → Start debounce timer (300ms)
Time 50ms:   User types 'e'   → Add to queue → Reset timer
Time 100ms:  User types 'l'   → Add to queue → Reset timer
Time 150ms:  User types 'l'   → Add to queue → Reset timer
Time 200ms:  User types 'o'   → Add to queue → Reset timer
Time 250ms:  User stops typing
Time 550ms:  Debounce timer fires → Flush queue
             → Send 1 request với queries: ['h', 'he', 'hel', 'hell', 'hello']
             → Thay vì 5 requests riêng lẻ!
```

**✅ Example 2: Analytics batching**
```typescript
interface AnalyticsEvent {
  type: string;
  data: any;
  timestamp: number;
}

async function batchAnalytics(events: AnalyticsEvent[]): Promise<void[]> {
  await fetch('/api/analytics/batch', {
    method: 'POST',
    body: JSON.stringify({ events }),
  });
  return events.map(() => undefined); // ✅ Return empty array
}

const analyticsBatcher = new RequestBatcher(batchAnalytics, {
  debounceMs: 5000,     // 💡 Gộp events trong 5s
  maxBatchSize: 50,     // 💡 Max 50 events per batch
  maxWaitMs: 10000,     // 💡 Force flush mỗi 10s
});

// 💡 Track event
async function trackEvent(type: string, data: any) {
  await analyticsBatcher.add({
    type,
    data,
    timestamp: Date.now(),
  });
}

// ✅ Usage: Tất cả events trong 5s được gộp thành 1 request
trackEvent('page_view', { page: '/home' });
trackEvent('button_click', { button: 'signup' });
trackEvent('form_submit', { form: 'newsletter' });
// → 1 request với 3 events thay vì 3 requests!
```

**🎯 Ưu điểm:**
- ✅ Reduce API calls → Save bandwidth, server load
- ✅ Debounce → Không spam server khi user type liên tục
- ✅ Max batch size → Control request payload size
- ✅ Max wait time → Ensure timely processing
- ✅ Auto-retry → Nếu có items mới trong queue khi processing

---

### **Scenario 6: Concurrent Limit với Priority Queue**
### **Kịch Bản 6: Giới Hạn Đồng Thời với Hàng Đợi Ưu Tiên**

```typescript
// 💡 Problem: Download nhiều files → Overwhelming browser/server
// 💡 Solution: Concurrency limit + priority queue

interface QueueItem<T> {
  id: string;
  priority: number;  // 💡 Higher = more important
  fn: () => Promise<T>;
  resolve: (value: T) => void;
  reject: (error: any) => void;
}

class PriorityQueue<T> {
  private queue: QueueItem<T>[] = [];
  private running = 0;

  constructor(
    private maxConcurrent: number // 💡 Max concurrent operations
  ) {}

  async add<R>(
    fn: () => Promise<R>,
    options?: {
      priority?: number;  // 💡 Priority (default: 0)
      id?: string;        // 💡 Unique ID cho logging
    }
  ): Promise<R> {
    return new Promise<R>((resolve, reject) => {
      const item: QueueItem<R> = {
        id: options?.id ?? `task-${Date.now()}`,
        priority: options?.priority ?? 0,
        fn: fn as () => Promise<any>,
        resolve: resolve as (value: any) => void,
        reject,
      };

      // 💡 Add to queue
      this.queue.push(item as any);

      // 💡 Sort by priority (higher first)
      this.queue.sort((a, b) => b.priority - a.priority);

      console.log(`📥 Queued: ${item.id} (priority: ${item.priority}, queue size: ${this.queue.length})`);

      // 💡 Try to process
      this.process();
    });
  }

  private async process() {
    // 💡 Check nếu đã đủ concurrent hoặc queue rỗng
    if (this.running >= this.maxConcurrent || this.queue.length === 0) {
      return;
    }

    // 💡 Take highest priority item
    const item = this.queue.shift()!;
    this.running++;

    console.log(`🚀 Executing: ${item.id} (running: ${this.running}/${this.maxConcurrent})`);

    try {
      const result = await item.fn();
      item.resolve(result);
      console.log(`✅ Completed: ${item.id}`);
    } catch (error) {
      item.reject(error);
      console.error(`❌ Failed: ${item.id}`, error);
    } finally {
      this.running--;
      console.log(`📊 Stats: running=${this.running}, queued=${this.queue.length}`);

      // 💡 Process next item
      this.process();
    }
  }

  getStats() {
    return {
      running: this.running,
      queued: this.queue.length,
    };
  }
}

// ✅ Example: File download manager
interface DownloadTask {
  url: string;
  filename: string;
  priority?: number;
}

class DownloadManager {
  private queue = new PriorityQueue<Blob>(3); // 💡 Max 3 concurrent downloads

  async download(task: DownloadTask): Promise<Blob> {
    return this.queue.add(
      async () => {
        console.log(`⬇️ Downloading: ${task.filename}`);
        
        const response = await fetch(task.url);
        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`);
        }

        const blob = await response.blob();
        console.log(`✅ Downloaded: ${task.filename} (${blob.size} bytes)`);
        
        return blob;
      },
      {
        id: task.filename,
        priority: task.priority ?? 0,
      }
    );
  }

  async downloadMultiple(tasks: DownloadTask[]): Promise<Blob[]> {
    // 💡 Queue all tasks
    const promises = tasks.map(task => this.download(task));
    
    // 💡 Wait for all
    return Promise.all(promises);
  }

  getStats() {
    return this.queue.getStats();
  }
}

// ✅ Usage
const downloadManager = new DownloadManager();

async function downloadFiles() {
  const files = [
    { url: '/files/doc1.pdf', filename: 'doc1.pdf', priority: 1 },      // Low priority
    { url: '/files/doc2.pdf', filename: 'doc2.pdf', priority: 5 },      // Normal priority
    { url: '/files/urgent.pdf', filename: 'urgent.pdf', priority: 10 }, // High priority
    { url: '/files/doc3.pdf', filename: 'doc3.pdf', priority: 3 },
    { url: '/files/doc4.pdf', filename: 'doc4.pdf', priority: 2 },
  ];

  // 💡 Queue all files
  // 💡 Order: urgent.pdf (10) → doc2.pdf (5) → doc3.pdf (3) → doc4.pdf (2) → doc1.pdf (1)
  // 💡 Max 3 concurrent → First 3 start immediately
  const blobs = await downloadManager.downloadMultiple(files);
  
  console.log('✅ All files downloaded:', blobs.length);
}
```

**🎯 Execution Timeline:**
```
Time 0ms:   Queue: [urgent(10), doc2(5), doc3(3), doc4(2), doc1(1)]
            Start: urgent, doc2, doc3 (max 3 concurrent)
            
Time 100ms: urgent completes → Start doc4 (next in queue)
            Running: doc2, doc3, doc4
            
Time 200ms: doc2 completes → Start doc1
            Running: doc3, doc4, doc1
            
Time 300ms: doc3 completes
            Running: doc4, doc1
            
Time 400ms: doc4, doc1 complete
            Done! ✅
```

**🎯 Ưu điểm:**
- ✅ Concurrency limit → Không overwhelming browser/network
- ✅ Priority queue → Important tasks execute first
- ✅ Fair scheduling → Không để low-priority tasks starved
- ✅ Backpressure → Queue grows nếu tasks come faster than processing

---

### **Scenario 7: Stream Processing với Async Iterators**
### **Kịch Bản 7: Xử Lý Stream với Async Iterators**

```typescript
// 💡 Problem: Large dataset không thể load hết vào memory
// 💡 Solution: Async generators cho streaming data

// ✅ Async generator: Fetch data page by page
async function* fetchUsersStream(
  pageSize: number = 100
): AsyncGenerator<User[], void, undefined> {
  let page = 1;
  let hasMore = true;

  while (hasMore) {
    console.log(`📥 Fetching page ${page}...`);
    
    // 💡 Fetch 1 page
    const response = await fetch(`/api/users?page=${page}&limit=${pageSize}`);
    const data = await response.json();

    // 💡 Yield page data (pause here, resume khi next() được gọi)
    yield data.users;

    // 💡 Check nếu còn pages
    hasMore = data.hasMore;
    page++;

    // 💡 Small delay để không spam server
    if (hasMore) {
      await new Promise(resolve => setTimeout(resolve, 100));
    }
  }

  console.log(`✅ Stream completed: ${page - 1} pages`);
}

// ✅ Usage Example 1: Process stream với for-await-of
async function processAllUsers() {
  let totalProcessed = 0;

  // 💡 for await...of: Iterate async generator
  for await (const users of fetchUsersStream(100)) {
    // 💡 Process current page
    console.log(`Processing ${users.length} users...`);
    
    // 💡 Do something với users (không hold toàn bộ dataset)
    await processUserBatch(users);
    
    totalProcessed += users.length;
    console.log(`Progress: ${totalProcessed} users processed`);
  }

  console.log(`✅ Total: ${totalProcessed} users processed`);
}

// ✅ Usage Example 2: Search trong large dataset
async function findUserByEmail(email: string): Promise<User | null> {
  // 💡 Stream qua pages cho đến khi tìm thấy
  for await (const users of fetchUsersStream(1000)) {
    const found = users.find(u => u.email === email);
    if (found) {
      console.log(`✅ Found user on page, stopping stream`);
      return found; // ✅ Tìm thấy → Stop stream ngay (không fetch pages còn lại)
    }
  }

  return null; // ❌ Không tìm thấy sau khi traverse hết
}

// ✅ Usage Example 3: Transform stream với async generator pipeline
async function* filterActiveUsers(
  stream: AsyncGenerator<User[]>
): AsyncGenerator<User[], void, undefined> {
  for await (const users of stream) {
    // 💡 Filter active users only
    const activeUsers = users.filter(u => u.isActive);
    if (activeUsers.length > 0) {
      yield activeUsers; // ✅ Chỉ yield nếu có active users
    }
  }
}

async function* mapUserNames(
  stream: AsyncGenerator<User[]>
): AsyncGenerator<string[], void, undefined> {
  for await (const users of stream) {
    // 💡 Extract names
    yield users.map(u => u.name);
  }
}

// 💡 Compose generators (pipeline pattern)
async function getUserNamesStream() {
  const userStream = fetchUsersStream(100);
  const activeStream = filterActiveUsers(userStream);
  const nameStream = mapUserNames(activeStream);
  return nameStream;
}

// ✅ Usage pipeline
async function printActiveUserNames() {
  const nameStream = await getUserNamesStream();
  
  for await (const names of nameStream) {
    console.log('Active users:', names.join(', '));
  }
}

// ✅ Usage Example 4: React component với streaming
function UserListStream() {
  const [users, setUsers] = useState<User[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    let totalFetched = 0;

    (async () => {
      // 💡 Stream users và append dần vào state
      for await (const batch of fetchUsersStream(50)) {
        setUsers(prev => [...prev, ...batch]); // ✅ Append batch
        totalFetched += batch.length;
        setProgress(totalFetched);
      }
      setIsLoading(false);
    })();
  }, []);

  return (
    <div>
      {isLoading && <div>Loading... ({progress} users loaded)</div>}
      <ul>
        {users.map(user => (
          <li key={user.id}>{user.name}</li>
        ))}
      </ul>
    </div>
  );
}
```

**🎯 Ưu điểm:**
- ✅ Memory efficient → Không load toàn bộ dataset
- ✅ Progressive rendering → Show data as it arrives
- ✅ Early termination → Stop stream khi tìm thấy (không fetch hết)
- ✅ Composable → Pipeline pattern với multiple transformations
- ✅ Backpressure → Consumer control flow (không fetch page mới cho đến khi process xong)

---

### **Scenario 8: Race Condition Protection với Request ID**
### **Kịch Bản 8: Bảo Vệ Race Condition với Request ID**

```typescript
// 💡 Problem: User type nhanh → Multiple requests → Response về không đúng thứ tự
// 💡 Example: User types "hello" → Requests: 'h', 'he', 'hel', 'hell', 'hello'
//             Response order: 'he', 'h', 'hello', 'hell', 'hel' (out of order!)
// 💡 Solution: Track latest request ID, discard outdated responses

class RaceConditionSafeAPI {
  private latestRequestId = 0;
  private pendingRequests = new Map<number, AbortController>();

  async fetch<T>(
    url: string,
    options?: {
      cancelPrevious?: boolean; // 💡 Cancel previous requests? (default: true)
    }
  ): Promise<T> {
    const cancelPrevious = options?.cancelPrevious ?? true;

    // 💡 Generate request ID
    const requestId = ++this.latestRequestId;
    console.log(`🚀 Request #${requestId}: ${url}`);

    // 💡 Cancel previous requests (nếu enabled)
    if (cancelPrevious) {
      this.pendingRequests.forEach((controller, id) => {
        if (id < requestId) {
          console.log(`🛑 Cancelling outdated request #${id}`);
          controller.abort();
          this.pendingRequests.delete(id);
        }
      });
    }

    // 💡 Create AbortController cho request này
    const abortController = new AbortController();
    this.pendingRequests.set(requestId, abortController);

    try {
      const response = await fetch(url, {
        signal: abortController.signal,
      });

      // 💡 Check nếu request này vẫn là latest
      if (requestId !== this.latestRequestId) {
        console.log(`⚠️ Request #${requestId} outdated, discarding response`);
        throw new Error('Outdated request');
      }

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }

      const data = await response.json();
      console.log(`✅ Request #${requestId} completed successfully`);
      
      return data;

    } catch (error: any) {
      if (error.name === 'AbortError') {
        console.log(`🛑 Request #${requestId} aborted`);
      }
      throw error;

    } finally {
      // 💡 Cleanup
      this.pendingRequests.delete(requestId);
    }
  }

  // 💡 Cancel all pending requests
  cancelAll() {
    console.log(`🛑 Cancelling ${this.pendingRequests.size} pending requests`);
    this.pendingRequests.forEach(controller => controller.abort());
    this.pendingRequests.clear();
  }

  // 💡 Get stats
  getPendingCount() {
    return this.pendingRequests.size;
  }
}

// ✅ Usage Example 1: Search với race condition protection
const searchAPI = new RaceConditionSafeAPI();

function SearchBox() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleSearch = async (searchQuery: string) => {
    if (!searchQuery) {
      setResults([]);
      return;
    }

    setIsLoading(true);
    try {
      // 💡 Tự động cancel previous requests
      // 💡 Chỉ response mới nhất được accept
      const data = await searchAPI.fetch(`/api/search?q=${searchQuery}`, {
        cancelPrevious: true, // ✅ Cancel outdated requests
      });
      
      setResults(data.results);
      console.log(`✅ Updated results for: ${searchQuery}`);

    } catch (error: any) {
      if (error.message !== 'Outdated request') {
        console.error('Search error:', error);
      }
    } finally {
      setIsLoading(false);
    }
  };

  // 💡 Debounce search
  const debouncedSearch = useMemo(
    () => debounce(handleSearch, 300),
    []
  );

  return (
    <div>
      <input
        value={query}
        onChange={(e) => {
          setQuery(e.target.value);
          debouncedSearch(e.target.value);
        }}
      />
      {isLoading && <div>Searching...</div>}
      <ul>
        {results.map(item => <li key={item.id}>{item.title}</li>)}
      </ul>
    </div>
  );
}

// ✅ Usage Example 2: Tab navigation với race protection
function UserProfile({ userId }: { userId: string }) {
  const [activeTab, setActiveTab] = useState<'posts' | 'likes' | 'followers'>('posts');
  const [data, setData] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  
  const tabAPI = useRef(new RaceConditionSafeAPI()).current;

  const loadTabData = async (tab: string) => {
    setIsLoading(true);
    try {
      // 💡 User click tabs nhanh → Previous requests bị cancel
      const tabData = await tabAPI.fetch(`/api/users/${userId}/${tab}`);
      setData(tabData);
    } catch (error) {
      if (error.message !== 'Outdated request') {
        console.error('Load tab error:', error);
      }
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    loadTabData(activeTab);
  }, [activeTab, userId]);

  // 💡 Cleanup: Cancel pending requests khi unmount
  useEffect(() => {
    return () => {
      tabAPI.cancelAll();
    };
  }, []);

  return (
    <div>
      <div>
        <button onClick={() => setActiveTab('posts')}>Posts</button>
        <button onClick={() => setActiveTab('likes')}>Likes</button>
        <button onClick={() => setActiveTab('followers')}>Followers</button>
      </div>
      {isLoading ? <Spinner /> : <TabContent data={data} />}
    </div>
  );
}
```

**🎯 Timeline Example:**
```
Time 0ms:   User types 'h'    → Request #1 starts
Time 50ms:  User types 'e'    → Request #2 starts, #1 cancelled
Time 100ms: User types 'l'    → Request #3 starts, #2 cancelled
Time 150ms: User types 'l'    → Request #4 starts, #3 cancelled
Time 200ms: User types 'o'    → Request #5 starts, #4 cancelled
Time 300ms: Request #5 completes → Update UI ✅

Result: Chỉ request cuối cùng update UI, rest bị cancel
```

**🎯 Ưu điểm:**
- ✅ No race conditions → Chỉ latest response update UI
- ✅ Auto-cancel outdated requests → Save bandwidth
- ✅ Request ID tracking → Deterministic behavior
- ✅ Cleanup on unmount → No memory leaks
- ✅ Works với any async operation (không chỉ fetch)

---

### **Scenario 9: Async State Machine**
### **Kịch Bản 9: State Machine Bất Đồng Bộ**

```typescript
// 💡 Problem: Complex async flows với multiple states và transitions
// 💡 Solution: State machine pattern cho async operations

type FileUploadState =
  | { status: 'idle' }
  | { status: 'validating'; file: File }
  | { status: 'uploading'; file: File; progress: number }
  | { status: 'processing'; uploadId: string }
  | { status: 'completed'; url: string }
  | { status: 'error'; error: string };

type FileUploadEvent =
  | { type: 'SELECT_FILE'; file: File }
  | { type: 'VALIDATION_SUCCESS' }
  | { type: 'VALIDATION_ERROR'; error: string }
  | { type: 'UPLOAD_PROGRESS'; progress: number }
  | { type: 'UPLOAD_SUCCESS'; uploadId: string }
  | { type: 'UPLOAD_ERROR'; error: string }
  | { type: 'PROCESSING_COMPLETE'; url: string }
  | { type: 'PROCESSING_ERROR'; error: string }
  | { type: 'RETRY' }
  | { type: 'CANCEL' };

class FileUploadStateMachine {
  private state: FileUploadState = { status: 'idle' };
  private listeners: Array<(state: FileUploadState) => void> = [];
  private abortController: AbortController | null = null;

  constructor() {}

  // 💡 Get current state
  getState(): FileUploadState {
    return this.state;
  }

  // 💡 Subscribe to state changes
  subscribe(listener: (state: FileUploadState) => void) {
    this.listeners.push(listener);
    return () => {
      this.listeners = this.listeners.filter(l => l !== listener);
    };
  }

  // 💡 Transition to new state
  private transition(newState: FileUploadState) {
    console.log(`State: ${this.state.status} → ${newState.status}`);
    this.state = newState;
    this.listeners.forEach(listener => listener(newState));
  }

  // 💡 Send event to state machine
  async send(event: FileUploadEvent) {
    console.log(`Event: ${event.type} (current state: ${this.state.status})`);

    // 💡 State transitions based on current state + event
    switch (this.state.status) {
      case 'idle':
        if (event.type === 'SELECT_FILE') {
          await this.handleFileSelected(event.file);
        }
        break;

      case 'validating':
        if (event.type === 'VALIDATION_SUCCESS') {
          await this.handleValidationSuccess();
        } else if (event.type === 'VALIDATION_ERROR') {
          this.transition({ status: 'error', error: event.error });
        }
        break;

      case 'uploading':
        if (event.type === 'UPLOAD_PROGRESS') {
          this.transition({
            ...this.state,
            progress: event.progress,
          });
        } else if (event.type === 'UPLOAD_SUCCESS') {
          await this.handleUploadSuccess(event.uploadId);
        } else if (event.type === 'UPLOAD_ERROR') {
          this.transition({ status: 'error', error: event.error });
        } else if (event.type === 'CANCEL') {
          this.handleCancel();
        }
        break;

      case 'processing':
        if (event.type === 'PROCESSING_COMPLETE') {
          this.transition({ status: 'completed', url: event.url });
        } else if (event.type === 'PROCESSING_ERROR') {
          this.transition({ status: 'error', error: event.error });
        }
        break;

      case 'error':
        if (event.type === 'RETRY') {
          this.transition({ status: 'idle' });
        }
        break;

      case 'completed':
        // 💡 Terminal state: Không có transitions
        break;
    }
  }

  // 💡 Handle file selection → Start validation
  private async handleFileSelected(file: File) {
    this.transition({ status: 'validating', file });

    try {
      // 💡 Validate file (size, type, etc.)
      if (file.size > 10 * 1024 * 1024) { // 10MB
        throw new Error('File quá lớn (max 10MB)');
      }
      
      const allowedTypes = ['image/jpeg', 'image/png', 'application/pdf'];
      if (!allowedTypes.includes(file.type)) {
        throw new Error('File type không hợp lệ');
      }

      // ✅ Validation success
      await this.send({ type: 'VALIDATION_SUCCESS' });

    } catch (error: any) {
      await this.send({ type: 'VALIDATION_ERROR', error: error.message });
    }
  }

  // 💡 Handle validation success → Start upload
  private async handleValidationSuccess() {
    const file = (this.state as any).file;
    this.transition({ status: 'uploading', file, progress: 0 });

    this.abortController = new AbortController();

    try {
      // 💡 Upload file với progress tracking
      const formData = new FormData();
      formData.append('file', file);

      const xhr = new XMLHttpRequest();

      // 💡 Track upload progress
      xhr.upload.addEventListener('progress', (e) => {
        if (e.lengthComputable) {
          const progress = (e.loaded / e.total) * 100;
          this.send({ type: 'UPLOAD_PROGRESS', progress });
        }
      });

      // 💡 Upload complete
      xhr.addEventListener('load', () => {
        if (xhr.status === 200) {
          const response = JSON.parse(xhr.responseText);
          this.send({ type: 'UPLOAD_SUCCESS', uploadId: response.uploadId });
        } else {
          this.send({ type: 'UPLOAD_ERROR', error: `HTTP ${xhr.status}` });
        }
      });

      // 💡 Upload error
      xhr.addEventListener('error', () => {
        this.send({ type: 'UPLOAD_ERROR', error: 'Network error' });
      });

      // 💡 Handle abort
      this.abortController.signal.addEventListener('abort', () => {
        xhr.abort();
        this.transition({ status: 'idle' });
      });

      xhr.open('POST', '/api/upload');
      xhr.send(formData);

    } catch (error: any) {
      await this.send({ type: 'UPLOAD_ERROR', error: error.message });
    }
  }

  // 💡 Handle upload success → Start processing
  private async handleUploadSuccess(uploadId: string) {
    this.transition({ status: 'processing', uploadId });

    try {
      // 💡 Poll processing status
      const result = await this.pollProcessingStatus(uploadId);
      await this.send({ type: 'PROCESSING_COMPLETE', url: result.url });

    } catch (error: any) {
      await this.send({ type: 'PROCESSING_ERROR', error: error.message });
    }
  }

  // 💡 Poll processing status (với timeout)
  private async pollProcessingStatus(uploadId: string): Promise<{ url: string }> {
    const maxAttempts = 30;
    const pollInterval = 2000; // 2s

    for (let i = 0; i < maxAttempts; i++) {
      const response = await fetch(`/api/upload/${uploadId}/status`);
      const data = await response.json();

      if (data.status === 'completed') {
        return { url: data.url };
      }

      if (data.status === 'failed') {
        throw new Error('Processing failed');
      }

      // 💡 Still processing → Wait và retry
      await new Promise(resolve => setTimeout(resolve, pollInterval));
    }

    throw new Error('Processing timeout');
  }

  // 💡 Cancel upload
  private handleCancel() {
    this.abortController?.abort();
    this.transition({ status: 'idle' });
  }
}

// ✅ Usage trong React component
function FileUploader() {
  const [state, setState] = useState<FileUploadState>({ status: 'idle' });
  const stateMachine = useRef(new FileUploadStateMachine()).current;

  useEffect(() => {
    // 💡 Subscribe to state changes
    const unsubscribe = stateMachine.subscribe(setState);
    return unsubscribe;
  }, []);

  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      stateMachine.send({ type: 'SELECT_FILE', file });
    }
  };

  const handleCancel = () => {
    stateMachine.send({ type: 'CANCEL' });
  };

  const handleRetry = () => {
    stateMachine.send({ type: 'RETRY' });
  };

  // 💡 Render based on state
  return (
    <div>
      {state.status === 'idle' && (
        <input type="file" onChange={handleFileSelect} />
      )}

      {state.status === 'validating' && (
        <div>Validating file...</div>
      )}

      {state.status === 'uploading' && (
        <div>
          <div>Uploading... {state.progress.toFixed(0)}%</div>
          <progress value={state.progress} max={100} />
          <button onClick={handleCancel}>Cancel</button>
        </div>
      )}

      {state.status === 'processing' && (
        <div>Processing file...</div>
      )}

      {state.status === 'completed' && (
        <div>
          ✅ Upload completed!
          <a href={state.url} target="_blank">View file</a>
        </div>
      )}

      {state.status === 'error' && (
        <div>
          ❌ Error: {state.error}
          <button onClick={handleRetry}>Retry</button>
        </div>
      )}
    </div>
  );
}
```

**🎯 State Flow:**
```
idle 
  → SELECT_FILE 
  → validating 
  → VALIDATION_SUCCESS 
  → uploading (0% → 100%) 
  → UPLOAD_SUCCESS 
  → processing 
  → PROCESSING_COMPLETE 
  → completed ✅

Alternative paths:
- validating → VALIDATION_ERROR → error
- uploading → UPLOAD_ERROR → error
- uploading → CANCEL → idle
- processing → PROCESSING_ERROR → error
- error → RETRY → idle
```

**🎯 Ưu điểm:**
- ✅ Predictable state transitions → Không có invalid states
- ✅ Type-safe với TypeScript discriminated unions
- ✅ Testable → Easy to test state transitions
- ✅ Debuggable → Clear state history
- ✅ Cancellable → Support abort at any stage
- ✅ Retryable → Support retry from error state

---

### **Scenario 10: Circuit Breaker Pattern**
### **Kịch Bản 10: Circuit Breaker Pattern**

```typescript
// 💡 Problem: Service down → App spam failed requests → Waste resources
// 💡 Solution: Circuit breaker → Fail fast khi service unhealthy

type CircuitState = 'CLOSED' | 'OPEN' | 'HALF_OPEN';

interface CircuitBreakerOptions {
  failureThreshold: number;    // 💡 Số failures trước khi open circuit
  successThreshold: number;    // 💡 Số successes để close circuit (từ half-open)
  timeout: number;             // 💡 Thời gian circuit open (ms)
  minimumRequests: number;     // 💡 Minimum requests trước khi evaluate
}

class CircuitBreaker {
  private state: CircuitState = 'CLOSED'; // 💡 Initial: CLOSED (normal operation)
  private failureCount = 0;
  private successCount = 0;
  private requestCount = 0;
  private nextAttempt = Date.now();

  constructor(
    private name: string,
    private options: CircuitBreakerOptions
  ) {}

  async execute<T>(fn: () => Promise<T>): Promise<T> {
    // 💡 Check circuit state
    if (this.state === 'OPEN') {
      // 💡 Check nếu đã đủ timeout → Chuyển sang HALF_OPEN
      if (Date.now() >= this.nextAttempt) {
        console.log(`[${this.name}] Circuit OPEN → HALF_OPEN (trying recovery)`);
        this.state = 'HALF_OPEN';
        this.successCount = 0;
        this.failureCount = 0;
      } else {
        // ❌ Circuit vẫn OPEN → Fail fast (không execute function)
        const waitTime = Math.ceil((this.nextAttempt - Date.now()) / 1000);
        throw new Error(
          `[${this.name}] Circuit OPEN - Service unavailable (retry sau ${waitTime}s)`
        );
      }
    }

    this.requestCount++;

    try {
      // 💡 Execute function
      const result = await fn();

      // ✅ Success
      this.onSuccess();
      return result;

    } catch (error) {
      // ❌ Failure
      this.onFailure();
      throw error;
    }
  }

  private onSuccess() {
    this.failureCount = 0; // Reset failure count

    if (this.state === 'HALF_OPEN') {
      this.successCount++;
      console.log(
        `[${this.name}] Success in HALF_OPEN (${this.successCount}/${this.options.successThreshold})`
      );

      // 💡 Check nếu đủ success threshold → Close circuit
      if (this.successCount >= this.options.successThreshold) {
        console.log(`[${this.name}] Circuit HALF_OPEN → CLOSED (service recovered) ✅`);
        this.state = 'CLOSED';
        this.successCount = 0;
        this.requestCount = 0;
      }
    }
  }

  private onFailure() {
    this.failureCount++;
    this.successCount = 0; // Reset success count

    console.log(
      `[${this.name}] Failure (${this.failureCount}/${this.options.failureThreshold}, ` +
      `requests: ${this.requestCount}/${this.options.minimumRequests})`
    );

    // 💡 Check nếu đủ minimum requests để evaluate
    if (this.requestCount < this.options.minimumRequests) {
      return; // Chưa đủ data để decide
    }

    // 💡 Check failure threshold
    const failureRate = this.failureCount / this.requestCount;
    const threshold = this.options.failureThreshold / 100; // Convert to percentage

    if (failureRate >= threshold) {
      // ❌ Quá nhiều failures → Open circuit
      console.log(
        `[${this.name}] Circuit CLOSED → OPEN ` +
        `(failure rate: ${(failureRate * 100).toFixed(1)}% >= ${threshold * 100}%) ⚠️`
      );
      
      this.state = 'OPEN';
      this.nextAttempt = Date.now() + this.options.timeout;
      this.failureCount = 0;
      this.requestCount = 0;

      const waitTime = Math.ceil(this.options.timeout / 1000);
      console.log(`[${this.name}] Will retry after ${waitTime}s`);
    }
  }

  // 💡 Get current state
  getState() {
    return {
      state: this.state,
      failureCount: this.failureCount,
      successCount: this.successCount,
      requestCount: this.requestCount,
      nextAttempt: this.state === 'OPEN' 
        ? new Date(this.nextAttempt).toISOString()
        : null,
    };
  }

  // 💡 Reset circuit (manual)
  reset() {
    console.log(`[${this.name}] Circuit reset manually`);
    this.state = 'CLOSED';
    this.failureCount = 0;
    this.successCount = 0;
    this.requestCount = 0;
  }
}

// ✅ Usage Example 1: Wrap API calls
const paymentServiceBreaker = new CircuitBreaker('PaymentService', {
  failureThreshold: 50,     // 💡 50% failures
  successThreshold: 3,      // 💡 3 consecutive successes untuk close
  timeout: 30000,           // 💡 30s timeout khi OPEN
  minimumRequests: 5,       // 💡 Cần ít nhất 5 requests để evaluate
});

async function processPayment(amount: number) {
  return paymentServiceBreaker.execute(async () => {
    // 💡 Actual payment API call
    const response = await fetch('/api/payment', {
      method: 'POST',
      body: JSON.stringify({ amount }),
    });

    if (!response.ok) {
      throw new Error(`Payment failed: ${response.status}`);
    }

    return response.json();
  });
}

// ✅ Usage Example 2: Multiple services với different configs
const userServiceBreaker = new CircuitBreaker('UserService', {
  failureThreshold: 30,     // 💡 More tolerant (30%)
  successThreshold: 2,
  timeout: 15000,           // 💡 Shorter timeout (15s)
  minimumRequests: 10,
});

const analyticsBreaker = new CircuitBreaker('Analytics', {
  failureThreshold: 80,     // 💡 Very tolerant (analytics not critical)
  successThreshold: 5,
  timeout: 60000,           // 💡 Longer timeout (1 minute)
  minimumRequests: 20,
});

// ✅ Usage Example 3: React component với circuit breaker
function PaymentForm() {
  const [amount, setAmount] = useState('');
  const [status, setStatus] = useState<'idle' | 'processing' | 'success' | 'error'>('idle');
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setStatus('processing');
    setError('');

    try {
      await processPayment(parseFloat(amount));
      setStatus('success');
      alert('Payment successful!');

    } catch (error: any) {
      setStatus('error');
      
      // 💡 Check nếu circuit breaker error
      if (error.message.includes('Circuit OPEN')) {
        setError('Payment service hiện không khả dụng. Vui lòng thử lại sau.');
      } else {
        setError(error.message);
      }
    }
  };

  // 💡 Show circuit breaker status
  const circuitStatus = paymentServiceBreaker.getState();

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="number"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
        placeholder="Amount"
      />
      
      <button type="submit" disabled={status === 'processing' || circuitStatus.state === 'OPEN'}>
        {status === 'processing' ? 'Processing...' : 'Pay'}
      </button>

      {error && <div className="error">{error}</div>}

      {/* Debug: Show circuit status */}
      <div className="circuit-status">
        Circuit: {circuitStatus.state} 
        {circuitStatus.state === 'OPEN' && ` (retry at ${circuitStatus.nextAttempt})`}
      </div>
    </form>
  );
}
```

**🎯 State Transitions:**
```
CLOSED (Normal operation)
  → 50% failures trong 5+ requests
  → OPEN (Fail fast for 30s)
  → After 30s timeout
  → HALF_OPEN (Try recovery)
  → 3 consecutive successes
  → CLOSED ✅

Alternative:
  HALF_OPEN → 1 failure → OPEN (back to fail fast)
```

**🎯 Example Timeline:**
```
Time 0s:     CLOSED - 10 requests
Time 1s:     5 success, 5 failures → 50% failure rate
             → Circuit OPEN ⚠️
             
Time 1-30s:  All requests fail fast (không hit API)
             "Circuit OPEN - retry sau Xs"
             
Time 30s:    Circuit → HALF_OPEN
             Next request → Execute normall
             
Time 31s:    Success #1 (1/3)
Time 32s:    Success #2 (2/3)
Time 33s:    Success #3 (3/3)
             → Circuit CLOSED ✅
             
Time 34s+:   Normal operation resumed
```

**🎯 Ưu điểm:**
- ✅ Fail fast → Không waste resources trên failing service
- ✅ Auto recovery → Tự động try lại sau timeout
- ✅ Configurable → Tune cho từng service (critical vs non-critical)
- ✅ Observability → Track circuit state, failure rates
- ✅ Prevent cascade failures → Service A down không làm crash toàn bộ system
- ✅ Better UX → User biết service unavailable thay vì infinite loading

---

## **📊 Summary: 10 Best Async Scenarios**
## **Tổng Kết: 10 Kịch Bản Bất Đồng Bộ Hay Nhất**

| # | Scenario | Use Case | Key Benefits |
|---|----------|----------|--------------|
| **1** | **Parallel Data Fetching với Error Isolation** | Dashboard load nhiều data sources | ✅ Song song (nhanh)<br>✅ 1 fail không crash all<br>✅ Fallback values |
| **2** | **Smart Retry với Exponential Backoff** | API calls có thể fail tạm thời | ✅ Auto-retry<br>✅ Không spam server<br>✅ Jitter tránh thundering herd |
| **3** | **Request Deduplication** | Nhiều components fetch same data | ✅ 1 request thay vì N<br>✅ Cache với TTL<br>✅ In-flight deduplication |
| **4** | **Timeout với Cleanup** | Long-running requests | ✅ Timeout protection<br>✅ Manual cancel<br>✅ Progress tracking<br>✅ No memory leaks |
| **5** | **Batching Requests** | User typing → Spam API calls | ✅ Debounce<br>✅ Gộp nhiều requests<br>✅ Reduce API calls 10x+ |
| **6** | **Concurrent Limit với Priority Queue** | Download nhiều files | ✅ Limit concurrent<br>✅ Priority scheduling<br>✅ Không overwhelm |
| **7** | **Stream Processing với Async Iterators** | Large datasets | ✅ Memory efficient<br>✅ Progressive rendering<br>✅ Early termination |
| **8** | **Race Condition Protection** | Search, tab navigation | ✅ No out-of-order updates<br>✅ Auto-cancel old requests<br>✅ Deterministic |
| **9** | **Async State Machine** | Complex workflows (upload, checkout) | ✅ Predictable states<br>✅ Type-safe transitions<br>✅ Testable |
| **10** | **Circuit Breaker Pattern** | External services có thể down | ✅ Fail fast<br>✅ Auto recovery<br>✅ Prevent cascade failures |

---

### **🎯 Khi nào dùng Scenario nào:**

**📥 Data Loading:**
- **Scenario 1** (Parallel + Error Isolation): Dashboard, multi-source data
- **Scenario 3** (Deduplication): Shared data across components
- **Scenario 7** (Streaming): Large datasets (thousands of items)

**⚡ Performance:**
- **Scenario 2** (Retry): Unstable network, transient errors
- **Scenario 5** (Batching): High-frequency operations (typing, analytics)
- **Scenario 6** (Concurrency Limit): Bulk operations (downloads, uploads)

**🛡️ Reliability:**
- **Scenario 4** (Timeout): External APIs, slow services
- **Scenario 8** (Race Protection): User interactions (search, navigation)
- **Scenario 10** (Circuit Breaker): Critical services, payment gateways

**🔄 Complex Flows:**
- **Scenario 9** (State Machine): Multi-step workflows, wizards

---

### **💡 Best Practices Tổng Hợp:**

**✅ DO:**
1. **Always handle errors** với try-catch hoặc .catch()
2. **Set timeouts** để prevent hanging requests
3. **Use Promise.allSettled** khi muốn wait all (không fail-fast)
4. **Cancel outdated requests** để save bandwidth
5. **Deduplicate requests** khi nhiều components fetch same data
6. **Stream large data** thay vì load all vào memory
7. **Implement retry** cho transient failures
8. **Use circuit breaker** cho external services
9. **Track request state** với state machines cho complex flows
10. **Monitor performance** với analytics

**❌ DON'T:**
1. **Forget cleanup** (timeouts, abort controllers) → Memory leaks
2. **Sequential await in loops** khi có thể parallel → Slow
3. **Unhandled promise rejections** → Silent failures
4. **Unlimited retries** → Infinite loops
5. **No timeout** → Hanging forever
6. **Race conditions** → Out-of-order updates
7. **Memory leaks** với large datasets → Use streaming
8. **Spam server** khi service down → Use circuit breaker

---

### **🚀 Production Checklist:**

Trước khi deploy async code:

- [ ] **Error handling**: Tất cả promises có .catch() hoặc try-catch
- [ ] **Timeouts**: Set reasonable timeouts cho all API calls
- [ ] **Cleanup**: Clear timers, cancel requests on unmount
- [ ] **Loading states**: Show loading indicators cho better UX
- [ ] **Race conditions**: Protected với request IDs hoặc AbortControllers
- [ ] **Retry logic**: Implement retry cho critical operations
- [ ] **Circuit breaker**: Protect external service calls
- [ ] **Monitoring**: Log errors, track performance metrics
- [ ] **Testing**: Unit tests cho async flows, edge cases
- [ ] **Documentation**: Document async behavior, gotchas

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
