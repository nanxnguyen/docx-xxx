# ⚙️ Q13: Async/Await vs Promises vs Callbacks & Promise.all/any/race




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

**Code Example:**

```typescript
// Callbacks
function fetchData(callback: (error: Error | null, data?: any) => void): void {
  setTimeout(() => {
    const data = { message: 'Hello World' };
    callback(null, data);
  }, 1000);
}

fetchData((error, data) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log('Data:', data);
  }
});

// Promises
function fetchDataPromise(): Promise<any> {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const data = { message: 'Hello World' };
      resolve(data);
    }, 1000);
  });
}

fetchDataPromise()
  .then((data) => console.log('Data:', data))
  .catch((error) => console.error('Error:', error));

// Async/Await
async function fetchDataAsync(): Promise<any> {
  try {
    const data = await fetchDataPromise();
    console.log('Data:', data);
    return data;
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
}
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

**🔹 Problem: Async errors không bị catch**

```typescript
// ❌ VẤN ĐỀ: Unhandled Promise Rejection
async function fetchUser(id: string) {
  const response = await fetch(`/api/users/${id}`);
  return response.json(); // Nếu response.json() throw error?
}

// Calling without try-catch → Unhandled rejection!
fetchUser('123'); // ❌ Nếu API fail → unhandled rejection

// ✅ GIẢI PHÁP 1: Try-catch trong function
async function fetchUserSafe(id: string) {
  try {
    const response = await fetch(`/api/users/${id}`);
    
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('Failed to fetch user:', error);
    throw error; // Re-throw để caller handle
  }
}

// ✅ GIẢI PHÁP 2: Global error handler
window.addEventListener('unhandledrejection', (event) => {
  console.error('Unhandled promise rejection:', event.reason);
  
  // Send to error tracking service (Sentry, Datadog)
  sendToErrorTracking({
    type: 'UNHANDLED_PROMISE_REJECTION',
    error: event.reason,
    timestamp: Date.now(),
  });
  
  // Prevent default browser behavior
  event.preventDefault();
});

// ✅ GIẢI PHÁP 3: Wrapper function với automatic error handling
async function safeAsync<T>(
  fn: () => Promise<T>,
  fallback?: T
): Promise<T | undefined> {
  try {
    return await fn();
  } catch (error) {
    console.error('Async error:', error);
    return fallback;
  }
}

// Usage
const user = await safeAsync(() => fetchUser('123'), { id: '123', name: 'Default' });
```

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
```

---

#### **2️⃣ Race Conditions - Xử Lý Tình Huống Chạy Đua**

**🔹 Problem: Multiple concurrent requests**

```typescript
// ❌ VẤN ĐỀ: User search - requests out of order
let searchTerm = '';

async function handleSearch(term: string) {
  searchTerm = term;
  
  // Slow request (200ms)
  const results = await fetch(`/api/search?q=${term}`).then(r => r.json());
  
  // ⚠️ VẤN ĐỀ: Nếu user type "abc" rồi xóa về "ab":
  // Request "ab" gửi trước, nhưng "abc" về sau
  // → Hiển thị sai kết quả!
  displayResults(results);
}

// ✅ GIẢI PHÁP 1: Track latest request với counter
let requestId = 0;

async function handleSearchSafe(term: string) {
  const currentRequestId = ++requestId;
  
  const results = await fetch(`/api/search?q=${term}`).then(r => r.json());
  
  // Chỉ hiển thị nếu là request mới nhất
  if (currentRequestId === requestId) {
    displayResults(results);
  } else {
    console.log('Discarding stale result');
  }
}

// ✅ GIẢI PHÁP 2: AbortController để cancel previous requests
let abortController: AbortController | null = null;

async function handleSearchWithAbort(term: string) {
  // Cancel previous request
  if (abortController) {
    abortController.abort();
  }
  
  // Create new controller
  abortController = new AbortController();
  
  try {
    const results = await fetch(`/api/search?q=${term}`, {
      signal: abortController.signal,
    }).then(r => r.json());
    
    displayResults(results);
  } catch (error: any) {
    if (error.name === 'AbortError') {
      console.log('Request cancelled');
    } else {
      throw error;
    }
  }
}

// ✅ GIẢI PHÁP 3: Debounce + Abort (Best for search)
import { debounce } from 'lodash';

let searchAbortController: AbortController | null = null;

const debouncedSearch = debounce(async (term: string) => {
  if (searchAbortController) {
    searchAbortController.abort();
  }
  
  searchAbortController = new AbortController();
  
  try {
    const results = await fetch(`/api/search?q=${term}`, {
      signal: searchAbortController.signal,
    }).then(r => r.json());
    
    displayResults(results);
  } catch (error: any) {
    if (error.name !== 'AbortError') {
      console.error('Search failed:', error);
    }
  }
}, 300); // Wait 300ms sau khi user ngừng typing

// Usage: Gọi mỗi khi user type
inputElement.addEventListener('input', (e) => {
  debouncedSearch(e.target.value);
});
```

**🔹 Problem: Concurrent updates to shared state**

```typescript
// ❌ VẤN ĐỀ: Multiple async operations update same state
let balance = 1000;

async function withdraw(amount: number) {
  // Simulate API call
  await delay(100);
  
  if (balance >= amount) {
    balance -= amount; // ⚠️ Race condition!
    console.log(`Withdrew ${amount}, balance: ${balance}`);
  }
}

// Gọi đồng thời
withdraw(600); // T0: Check balance = 1000 ✅
withdraw(600); // T1: Check balance = 1000 ✅
// T2: Balance = 400 ❌ (Should be rejected!)

// ✅ GIẢI PHÁP 1: Mutex lock
class Mutex {
  private locked = false;
  private waiting: Array<() => void> = [];
  
  async lock(): Promise<void> {
    if (!this.locked) {
      this.locked = true;
      return;
    }
    
    // Wait for unlock
    await new Promise<void>(resolve => {
      this.waiting.push(resolve);
    });
  }
  
  unlock(): void {
    const next = this.waiting.shift();
    if (next) {
      next();
    } else {
      this.locked = false;
    }
  }
}

const balanceMutex = new Mutex();

async function withdrawSafe(amount: number) {
  await balanceMutex.lock();
  
  try {
    await delay(100);
    
    if (balance >= amount) {
      balance -= amount;
      console.log(`Withdrew ${amount}, balance: ${balance}`);
    } else {
      console.log('Insufficient funds');
    }
  } finally {
    balanceMutex.unlock();
  }
}

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

// ✅ GIẢI PHÁP 1: Promise.race với timeout
async function fetchWithTimeout<T>(
  promise: Promise<T>,
  timeoutMs: number
): Promise<T> {
  const timeoutPromise = new Promise<never>((_, reject) => {
    setTimeout(() => reject(new Error('Timeout')), timeoutMs);
  });
  
  return Promise.race([promise, timeoutPromise]);
}

// Usage
try {
  const data = await fetchWithTimeout(
    fetch('/api/data').then(r => r.json()),
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
      .then(result => {
        clearTimeout(timeoutId);
        resolve(result);
      })
      .catch(error => {
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

// ✅ GIẢI PHÁP 1: Retry với exponential backoff
async function fetchWithRetry<T>(
  fn: () => Promise<T>,
  maxRetries = 3,
  delayMs = 1000
): Promise<T> {
  let lastError: Error;
  
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      return await fn();
    } catch (error) {
      lastError = error as Error;
      
      if (attempt < maxRetries) {
        // Exponential backoff: 1s, 2s, 4s, 8s...
        const delay = delayMs * Math.pow(2, attempt);
        console.log(`Retry ${attempt + 1}/${maxRetries} after ${delay}ms`);
        await new Promise(resolve => setTimeout(resolve, delay));
      }
    }
  }
  
  throw lastError!;
}

// Usage
const data = await fetchWithRetry(
  () => fetch('/api/data').then(r => r.json()),
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
        await new Promise(resolve => setTimeout(resolve, delay));
      } else {
        break; // Không retry (4xx errors, etc.)
      }
    }
  }
  
  throw lastError!;
}

// Usage: Chỉ retry network errors và 5xx errors
const data = await fetchWithConditionalRetry(
  () => fetch('/api/data').then(r => r.json()),
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

// ✅ GIẢI PHÁP 3: Advanced retry với circuit breaker
class CircuitBreaker {
  private failures = 0;
  private lastFailureTime = 0;
  private state: 'CLOSED' | 'OPEN' | 'HALF_OPEN' = 'CLOSED';
  
  constructor(
    private threshold = 5,
    private timeout = 60000 // 60s
  ) {}
  
  async execute<T>(fn: () => Promise<T>): Promise<T> {
    if (this.state === 'OPEN') {
      // Check if timeout passed
      if (Date.now() - this.lastFailureTime > this.timeout) {
        this.state = 'HALF_OPEN';
      } else {
        throw new Error('Circuit breaker is OPEN');
      }
    }
    
    try {
      const result = await fn();
      
      // Success → reset
      if (this.state === 'HALF_OPEN') {
        this.state = 'CLOSED';
      }
      this.failures = 0;
      
      return result;
    } catch (error) {
      this.failures++;
      this.lastFailureTime = Date.now();
      
      if (this.failures >= this.threshold) {
        this.state = 'OPEN';
        console.error('Circuit breaker opened!');
      }
      
      throw error;
    }
  }
}

const breaker = new CircuitBreaker(5, 60000);

async function fetchWithCircuitBreaker() {
  return breaker.execute(() => fetch('/api/data').then(r => r.json()));
}
```

---

#### **4️⃣ Concurrency Control - Kiểm Soát Đồng Thời**

**🔹 Problem: Too many concurrent requests**

```typescript
// ❌ VẤN ĐỀ: Process 1000 items concurrently
async function processAllItems(items: any[]) {
  const results = await Promise.all(
    items.map(item => processItem(item)) // 1000 concurrent requests! 💥
  );
  return results;
}

// ✅ GIẢI PHÁP 1: Batch processing
async function processInBatches<T, R>(
  items: T[],
  batchSize: number,
  processFn: (item: T) => Promise<R>
): Promise<R[]> {
  const results: R[] = [];
  
  for (let i = 0; i < items.length; i += batchSize) {
    const batch = items.slice(i, i + batchSize);
    const batchResults = await Promise.all(batch.map(processFn));
    results.push(...batchResults);
    
    console.log(`Processed ${Math.min(i + batchSize, items.length)}/${items.length}`);
  }
  
  return results;
}

// Usage: Process 100 items per batch
const results = await processInBatches(items, 100, processItem);

// ✅ GIẢI PHÁP 2: Concurrency limit với p-limit pattern
class ConcurrencyLimiter {
  private queue: Array<() => Promise<any>> = [];
  private running = 0;
  
  constructor(private limit: number) {}
  
  async run<T>(fn: () => Promise<T>): Promise<T> {
    while (this.running >= this.limit) {
      await new Promise(resolve => setTimeout(resolve, 10));
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
    items.map(item => limiter.run(() => processItem(item)))
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
const results = await Promise.all(
  items.map(item => processItem(item))
);
// ⚠️ TẤT CẢ chạy cùng lúc! Item 3 có thể xong trước item 1
// ⚠️ Server có thể quá tải (1000 requests cùng lúc)
```

---

### **✅ Giải Pháp: 4 Cách Chạy Sequential**

#### **1. For...of Loop (Đơn giản nhất - Khuyến nghị) ⭐**

```typescript
// ✅ Chạy TUẦN TỰ - Đợi xong mới chạy tiếp
async function processSequential(items: string[]) {
  const results = [];
  
  for (const item of items) {
    const result = await processItem(item);
    results.push(result);
  }
  
  return results;
}

// Example: API steps phụ thuộc nhau
const step1 = await fetch('/api/validate').then(r => r.json());
const step2 = await fetch('/api/upload', { 
  headers: { token: step1.token } // Cần token từ step1
}).then(r => r.json());
const step3 = await fetch('/api/save', {
  body: JSON.stringify({ fileId: step2.fileId }) // Cần fileId từ step2
}).then(r => r.json());
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

#### **3. Generator Pattern**

```typescript
// Real-time updates
async function* processWithProgress(items: string[]) {
  for (const item of items) {
    const result = await processItem(item);
    yield result; // Emit ngay khi xong
  }
}

// Usage: Update UI từng kết quả
for await (const result of processWithProgress(items)) {
  updateUI(result); // Cập nhật ngay
  console.log('Progress:', result);
}
```

#### **4. Batched (Cân bằng Speed + Server Load)**

```typescript
// Xử lý 10 items/lần (giữa parallel và sequential)
async function processBatched(items: string[], batchSize = 10) {
  const results = [];
  
  for (let i = 0; i < items.length; i += batchSize) {
    const batch = items.slice(i, i + batchSize);
    const batchResults = await Promise.all(
      batch.map(item => processItem(item))
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
  const uploaded = await fetch('/api/upload', { headers: { token: validated.token } });
  const saved = await fetch('/api/save', { body: { fileId: uploaded.fileId } });
  return saved;
}

// Example 2: Rate-Limited API (1 request/giây)
async function fetchWithRateLimit(urls: string[]) {
  const results = [];
  for (let i = 0; i < urls.length; i++) {
    results.push(await fetch(urls[i]).then(r => r.json()));
    if (i < urls.length - 1) await new Promise(r => setTimeout(r, 1000));
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

**🔹 Problem: Process large datasets**

```typescript
// ❌ VẤN ĐỀ: Load all data vào memory
async function processAllUsers() {
  const users = await fetchAllUsers(); // 1 million users! 💥
  
  for (const user of users) {
    await processUser(user);
  }
}

// ✅ GIẢI PHÁP 1: Async Generator
async function* fetchUsersPaginated(pageSize = 100) {
  let page = 0;
  
  while (true) {
    const users = await fetch(`/api/users?page=${page}&size=${pageSize}`)
      .then(r => r.json());
    
    if (users.length === 0) break;
    
    yield* users; // Yield each user
    page++;
  }
}

// Usage: Process one user at a time
for await (const user of fetchUsersPaginated()) {
  await processUser(user);
  console.log(`Processed user ${user.id}`);
}

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
          await new Promise(resolve => setTimeout(resolve, delay));
        }
      }
    }
    
    throw lastError!;
  }
  
  // 2. Timeout wrapper
  static withTimeout<T>(
    promise: Promise<T>,
    timeoutMs: number
  ): Promise<T> {
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
          fn(...args).then(resolve).catch(reject);
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
      const promise = fn(item).then(result => {
        results.push(result);
      });
      
      executing.push(promise);
      
      if (executing.length >= concurrency) {
        await Promise.race(executing);
        executing.splice(executing.findIndex(p => p === promise), 1);
      }
    }
    
    await Promise.all(executing);
    return results;
  }
  
  // 5. Sleep utility
  static sleep(ms: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
}

// =====================================
// USAGE EXAMPLES
// =====================================

// Retry API call
const data = await AsyncUtils.retry(
  () => fetch('/api/data').then(r => r.json()),
  { maxRetries: 3, delay: 1000, backoff: 2 }
);

// Timeout request
const user = await AsyncUtils.withTimeout(
  fetch('/api/user').then(r => r.json()),
  5000
);

// Debounced search
const debouncedSearch = AsyncUtils.debounce(
  async (term: string) => {
    const results = await fetch(`/api/search?q=${term}`).then(r => r.json());
    displayResults(results);
  },
  300
);

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

**📌 Promise Combinators Examples:**

```typescript
// Promise.all - tất cả phải thành công
const [users, posts, comments] = await Promise.all([
  fetch('/api/users').then(r => r.json()),
  fetch('/api/posts').then(r => r.json()),
  fetch('/api/comments').then(r => r.json())
]);

// Promise.any - 1 thành công là đủ (fallback)
const data = await Promise.any([
  fetch('/api/primary'),
  fetch('/api/backup1'),
  fetch('/api/backup2')
]);

// Promise.race - ai nhanh nhất
const result = await Promise.race([
  fetch('/api/data'),
  new Promise((_, reject) => setTimeout(() => reject('Timeout'), 5000))
]);

// Promise.allSettled - đợi tất cả complete
const results = await Promise.allSettled([
  fetch('/api/1'),
  fetch('/api/2'),
  fetch('/api/3')
]);
// results = [{ status: 'fulfilled', value: ... }, { status: 'rejected', reason: ... }]
```

Nhưng với đúng patterns và tools, bạn có thể xử lý mọi tình huống async một cách hiệu quả! 🚀

---
