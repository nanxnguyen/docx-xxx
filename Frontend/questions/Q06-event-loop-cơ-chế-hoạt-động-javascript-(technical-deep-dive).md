# 🔄 Q06: Event Loop - Cơ Chế Hoạt Động JavaScript (Technical Deep Dive)

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"JavaScript chạy đơn luồng với Event Loop để xử lý các thao tác bất đồng bộ.**

**🏗️ Kiến Trúc (5 Thành Phần):**
1. **Call Stack (Ngăn xếp gọi - LIFO)**: Nơi thực thi code đồng bộ. Đơn luồng → chỉ 1 hàm chạy tại 1 thời điểm.
2. **Heap (Vùng nhớ)**: Cấp phát bộ nhớ cho objects, arrays, functions.
3. **Web APIs (Trình duyệt) / C++ APIs (Node.js)**: Xử lý thao tác bất đồng bộ (setTimeout, fetch, fs.readFile) → chạy trên luồng riêng.
4. **Microtask Queue (Hàng đợi ưu tiên cao)**: Promise callbacks, queueMicrotask, MutationObserver.
5. **Macrotask Queue (Hàng đợi ưu tiên thấp)**: setTimeout, setInterval, I/O, UI rendering.

**♻️ Luồng Hoạt Động Event Loop (Chi Tiết):**
```
while (true) {
  1. Thực thi TẤT CẢ code đồng bộ trong Call Stack (cho đến khi trống)
  2. Thực thi TẤT CẢ Microtasks (Promise.then, queueMicrotask)
     → Làm trống hoàn toàn Microtask Queue
  3. Render UI (Chỉ trình duyệt - 60fps = 16ms/frame)
  4. Thực thi MỘT Macrotask (setTimeout callback)
  5. Quay lại bước 2 (kiểm tra Microtasks lại)
}
```

**🔑 Điểm Khác Biệt Quan Trọng:**
- **Microtask vs Macrotask**:
  - Microtask chạy TẤT CẢ trước khi Event Loop tiếp tục.
  - Macrotask chỉ chạy 1 task mỗi vòng lặp.
  - Ưu tiên: Microtask > UI Render > Macrotask.
- **Trình duyệt vs Node.js**:
  - Trình duyệt: Có giai đoạn render UI.
  - Node.js: Có `process.nextTick()` (ưu tiên cao hơn Microtask) + 6 giai đoạn (timers, I/O, idle, poll, check, close).

**⚠️ Lỗi Thường Gặp:**
- **Làm đói UI**: Microtasks vô hạn chặn rendering → UI đóng băng.
  ```js
  function loop() {
    Promise.resolve().then(loop); // ❌ Chặn UI mãi mãi
  }
  ```
- **setTimeout(fn, 0) ≠ Tức thì**: Vẫn phải chờ Call Stack trống + Microtasks hoàn thành.
- **Race Conditions**: Callbacks bất đồng bộ có thể thực thi không theo thứ tự mong đợi.

**🎯 Ví Dụ Thực Tế:**
```js
console.log('1'); // Đồng bộ → Call Stack
setTimeout(() => console.log('2'), 0); // Macrotask Queue
Promise.resolve().then(() => console.log('3')); // Microtask Queue
console.log('4'); // Đồng bộ → Call Stack

// Kết quả: 1, 4, 3, 2
// Lý do:
// 1. Thực thi đồng bộ: log '1', '4'
// 2. Call Stack trống → Kiểm tra Microtask → log '3'
// 3. Kiểm tra Macrotask → log '2'
```

**💡 Kiến Thức Senior:**
- **Hiệu năng**: Tránh chặn Call Stack với tính toán nặng → dùng Web Workers hoặc chia thành chunks với `setTimeout`.
- **Debugging**: Hiểu Event Loop → debug lỗi bất đồng bộ (race conditions, callback hell).
- **React**: `setState` batching dùng Microtask → nhiều lời gọi setState gộp thành 1 lần render lại.
- **Node.js**: `setImmediate()` vs `setTimeout(fn, 0)` → `setImmediate` chạy trong giai đoạn check, nhanh hơn trong I/O callbacks.
- **requestAnimationFrame**: Chạy TRƯỚC render (Chỉ trình duyệt) → animation mượt hơn setTimeout.

**🔧 Kỹ Thuật Tối Ưu:**
- **Chunking (Chia nhỏ)**: Chia tasks dài thành chunks nhỏ với `setTimeout` → không chặn UI.
- **queueMicrotask()**: Nhanh hơn `Promise.resolve().then()` → ít chi phí hơn.
- **Web Workers**: Offload tính toán nặng → luồng riêng (song song thật sự).

---

**❓ Câu Hỏi:**

Giải thích chi tiết cơ chế hoạt động của JavaScript Engine với Event Loop, Call Stack, Web APIs, Microtask/Macrotask Queues, và Single Thread.



**✅ Đáp Án Chi Tiết:**

**🏗️ KIẾN TRÚC TỔNG QUAN:**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    JAVASCRIPT RUNTIME ENVIRONMENT                    │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌────────────────────────────────────────────────────────────┐    │
│  │              JAVASCRIPT ENGINE (V8, SpiderMonkey)           │    │
│  ├────────────────────────────────────────────────────────────┤    │
│  │                                                             │    │
│  │  ┌─────────────────────────────────────────────────────┐  │    │
│  │  │  🔥 CALL STACK (LIFO)                               │  │    │
│  │  │  ────────────────────────────────────────────       │  │    │
│  │  │  │ function3() │ ← Top (đang thực thi)              │  │    │
│  │  │  │ function2() │                                     │  │    │
│  │  │  │ function1() │                                     │  │    │
│  │  │  │   main()    │ ← Bottom                            │  │    │
│  │  │  └─────────────┘                                     │  │    │
│  │  │                                                       │  │    │
│  │  │  📦 HEAP (Memory Allocation)                         │  │    │
│  │  │  • Objects, Arrays, Functions                        │  │    │
│  │  └─────────────────────────────────────────────────────┘  │    │
│  └────────────────────────────────────────────────────────────┘    │
│                                                                      │
│  ┌────────────────────────────────────────────────────────────┐    │
│  │  🌐 WEB APIs (Browser/Node.js)                            │    │
│  ├────────────────────────────────────────────────────────────┤    │
│  │  • setTimeout() / setInterval()                            │    │
│  │  • DOM Events (click, scroll, etc.)                        │    │
│  │  • fetch() / XMLHttpRequest                                │    │
│  │  • FileReader / Web Workers                                │    │
│  │  • Geolocation / Notification                              │    │
│  │  • IndexedDB / LocalStorage                                │    │
│  └────────────────────────────────────────────────────────────┘    │
│                             ↓ callbacks                             │
│  ┌────────────────────────────────────────────────────────────┐    │
│  │  ⚡ MICROTASK QUEUE (High Priority)                        │    │
│  ├────────────────────────────────────────────────────────────┤    │
│  │  • Promise.then() / Promise.catch()                        │    │
│  │  • queueMicrotask()                                        │    │
│  │  • MutationObserver                                        │    │
│  │  • process.nextTick() (Node.js only - highest priority)   │    │
│  └────────────────────────────────────────────────────────────┘    │
│                                                                      │
│  ┌────────────────────────────────────────────────────────────┐    │
│  │  🎯 MACROTASK QUEUE (Task Queue - Low Priority)           │    │
│  ├────────────────────────────────────────────────────────────┤    │
│  │  • setTimeout() / setInterval()                            │    │
│  │  • setImmediate() (Node.js only)                           │    │
│  │  • I/O operations (fs, network)                            │    │
│  │  • UI rendering (Browser only)                             │    │
│  │  • requestAnimationFrame() (Browser only)                  │    │
│  └────────────────────────────────────────────────────────────┘    │
│                                                                      │
│                          ↑                                           │
│  ┌────────────────────────────────────────────────────────────┐    │
│  │  🔄 EVENT LOOP (Infinite Loop)                             │    │
│  ├────────────────────────────────────────────────────────────┤    │
│  │  while (true) {                                            │    │
│  │    1. Check Call Stack → Execute sync code                │    │
│  │    2. Check Microtask Queue → Execute ALL                 │    │
│  │    3. Render UI (if needed - browser only)                │    │
│  │    4. Check Macrotask Queue → Execute ONE                 │    │
│  │    5. Go back to step 1                                   │    │
│  │  }                                                         │    │
│  └────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────┘
```

---

**🧵 1. SINGLE THREAD (Đơn Luồng)**

**Khái niệm:**
- JavaScript Engine chỉ có **1 Call Stack** duy nhất
- Chỉ thực thi **1 function tại 1 thời điểm**
- Không thể chạy đồng thời nhiều tasks như multi-threaded languages (Java, C++)

**Ưu điểm:**
- ✅ Đơn giản, không có race conditions
- ✅ Không cần lock/semaphore
- ✅ Dễ debug hơn multi-threaded

**Nhược điểm:**
- ⚠️ Blocking operations (heavy computation) đóng băng toàn bộ app
- ⚠️ Không tận dụng được multi-core CPUs

---

**🔥 2. CALL STACK**

**Khái niệm:**
- LIFO stack (Last In First Out) chứa execution contexts
- Mỗi function call được push vào stack
- Khi function return, nó được pop ra khỏi stack

**Hoạt động:**
```typescript
function multiply(a: number, b: number): number {
  return a * b; // ③ Pop
}

function square(n: number): number {
  return multiply(n, n); // ② Push multiply → Pop
}

function printSquare(n: number): void {
  const result = square(n); // ① Push square
  console.log(result);
}

printSquare(5);

// Call Stack Timeline:
// → main() 
// → main() → printSquare(5)
// → main() → printSquare(5) → square(5)
// → main() → printSquare(5) → square(5) → multiply(5, 5)
// → main() → printSquare(5) → square(5)  [multiply returns]
// → main() → printSquare(5)  [square returns]
// → main()  [printSquare returns]
// → [empty]
```

**Stack Overflow:**
```typescript
// ❌ Recursive function không có điều kiện dừng
function recursiveFunction() {
  recursiveFunction(); // Tạo vô hạn stack frames
}

recursiveFunction(); // RangeError: Maximum call stack size exceeded
```

---

**🌐 3. WEB APIs**

**Khái niệm:**
- APIs được cung cấp bởi **Browser** (hoặc Node.js runtime), KHÔNG phải JavaScript Engine
- Chạy **bên ngoài** Call Stack → không block main thread
- Khi hoàn thành, callbacks được đưa vào Queues

**Các Web APIs phổ biến:**

```typescript
// A. Timers
setTimeout(() => console.log('Timer done'), 1000);
setInterval(() => console.log('Tick'), 1000);

// B. DOM Events
document.getElementById('btn').addEventListener('click', () => {
  console.log('Button clicked');
});

// C. Network Requests
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => console.log(data));

// D. File APIs
const reader = new FileReader();
reader.onload = (e) => console.log(e.target.result);
reader.readAsText(file);

// E. Observers
const observer = new IntersectionObserver((entries) => {
  console.log('Element intersected');
});

// F. Geolocation
navigator.geolocation.getCurrentPosition(
  (position) => console.log(position.coords),
  (error) => console.error(error)
);
```

---

**⚡ 4. MICROTASK QUEUE (Job Queue)**

**Khái niệm:**
- Hàng đợi chứa **microtasks** (priority cao)
- **Xử lý TẤT CẢ** microtasks trước khi chuyển sang macrotask
- Ưu tiên: **process.nextTick()** > **Promise** > **queueMicrotask**

**Các Microtasks:**
```typescript
// 1. Promise.then/catch/finally
Promise.resolve().then(() => console.log('Microtask 1'));

// 2. queueMicrotask()
queueMicrotask(() => console.log('Microtask 2'));

// 3. MutationObserver
const observer = new MutationObserver(() => {
  console.log('DOM mutated - Microtask 3');
});

// 4. process.nextTick() - Node.js only (highest priority)
process.nextTick(() => console.log('NextTick - Microtask 0'));
```

---

**🎯 5. MACROTASK QUEUE (Task Queue / Callback Queue)**

**Khái niệm:**
- Hàng đợi chứa **macrotasks** (priority thấp hơn microtask)
- Event Loop chỉ lấy **MỘT macrotask** mỗi lần
- Sau mỗi macrotask, xử lý ALL microtasks

**Các Macrotasks:**
```typescript
// 1. setTimeout / setInterval
setTimeout(() => console.log('Macrotask 1'), 0);
setInterval(() => console.log('Macrotask 2'), 1000);

// 2. setImmediate - Node.js only
setImmediate(() => console.log('Macrotask 3'));

// 3. I/O operations
fs.readFile('file.txt', (err, data) => {
  console.log('File read - Macrotask 4');
});

// 4. UI rendering events (Browser)
requestAnimationFrame(() => console.log('RAF - Macrotask 5'));
```

---

**🔄 6. EVENT LOOP - QUY TRÌNH HOẠT ĐỘNG**

**Thuật toán Event Loop:**

```
┌───────────────────────────┐
│    1. Execute Call Stack  │  → Chạy hết synchronous code
│       (synchronous code)  │
└──────────┬────────────────┘
           │
           ↓
┌───────────────────────────┐
│  2. Check Microtask Queue │  → Xử lý HẾT TẤT CẢ microtasks
│     - process.nextTick()  │     (bao gồm cả microtasks mới tạo)
│     - Promise callbacks   │
│     - queueMicrotask()    │
└──────────┬────────────────┘
           │
           ↓
┌───────────────────────────┐
│   3. Render UI (Browser)  │  → Update DOM, paint, reflow
│      (if needed)          │     (chỉ browser, không phải Node.js)
└──────────┬────────────────┘
           │
           ↓
┌───────────────────────────┐
│  4. Check Macrotask Queue │  → Lấy MỘT macrotask
│     - setTimeout()        │     (chỉ 1 cái duy nhất)
│     - setImmediate()      │
│     - I/O callbacks       │
└──────────┬────────────────┘
           │
           ↓
┌───────────────────────────┐
│   5. Go back to Step 1    │  → Lặp lại vô hạn
└───────────────────────────┘
```

---

**🔢 THỨ TỰ ƯU TIÊN:**

```
1️⃣ Call Stack (Synchronous code)         - Cao nhất
2️⃣ process.nextTick() (Node.js)          - Rất cao
3️⃣ Promise microtasks                    - Cao
4️⃣ queueMicrotask()                      - Cao
5️⃣ setTimeout(fn, 0) / setInterval()     - Thấp
6️⃣ setImmediate() (Node.js)              - Thấp hơn
7️⃣ I/O operations                        - Thấp nhất
```

---

**✅ Ưu điểm của cơ chế này:**
- Non-blocking I/O → ứng dụng responsive
- Không bị đóng băng khi chờ API/database
- Microtask giúp xử lý Promise nhanh hơn setTimeout
- UI luôn mượt mà vì rendering được ưu tiên

**⚠️ Nhược điểm:**
- **Microtask starvation**: Vô hạn microtasks → macrotask không chạy
- **Callback hell**: Lồng nhiều callbacks → khó đọc
- **Khó debug**: Thứ tự thực thi phức tạp hơn synchronous
- **Heavy computation block UI**: Vì single-threaded

**Code Example:**

**🔍 Ví dụ 1: Phân biệt Microtask vs Macrotask**

```typescript
console.log('1: Sync code start'); // ① Call Stack

setTimeout(() => console.log('2: Macrotask 1'), 0); // ④ Macrotask Queue
setTimeout(() => console.log('3: Macrotask 2'), 0); // ④ Macrotask Queue

Promise.resolve()
  .then(() => console.log('4: Microtask 1')) // ② Microtask Queue
  .then(() => console.log('5: Microtask 2')); // ② Microtask Queue (chained)

Promise.resolve().then(() => {
  console.log('6: Microtask 3');

  // ⚠️ Tạo thêm microtask TRONG microtask
  queueMicrotask(() => console.log('7: Microtask 4'));
});

console.log('8: Sync code end'); // ① Call Stack

/* 🎯 OUTPUT (theo thứ tự Event Loop):
1: Sync code start          // ① Call Stack: đồng bộ
8: Sync code end            // ① Call Stack: đồng bộ
4: Microtask 1              // ② ALL Microtasks (xử lý HẾT)
6: Microtask 3              // ② ALL Microtasks
7: Microtask 4              // ② ALL Microtasks (tạo thêm trong microtask)
5: Microtask 2              // ② ALL Microtasks (chained promise)
2: Macrotask 1              // ④ ONE Macrotask (chỉ lấy 1 cái)
3: Macrotask 2              // ④ ONE Macrotask (chu kỳ Event Loop tiếp theo)

📋 Giải thích từng bước:
1. Call Stack chạy hết code đồng bộ (1, 8)
2. Event Loop xử lý HẾT TẤT CẢ microtasks (4, 6, 7, 5)
3. Browser có thể render UI (nếu cần)
4. Event Loop lấy MỘT macrotask (2)
5. Quay lại bước 1, xử lý microtasks rồi lấy macrotask tiếp theo (3)
*/
```

**🔍 Ví dụ 2: Microtask Starvation (Đói macrotask)**

```typescript
console.log('Start');

setTimeout(() => {
  console.log('❌ Macrotask: Tôi sẽ KHÔNG BAO GIỜ chạy!');
}, 0);

// ⚠️ VÔ HẠN microtasks - CHẶN tất cả macrotasks
function infiniteMicrotasks() {
  Promise.resolve().then(() => {
    console.log('✅ Microtask: Chạy mãi không dừng...');
    infiniteMicrotasks(); // Tạo thêm microtask liên tục
  });
}

infiniteMicrotasks();

/*
⚠️ KẾT QUẢ:
- "Start" in ra
- Microtask in ra vô hạn lần
- setTimeout KHÔNG BAO GIỜ chạy vì Event Loop mắc kẹt ở Microtask Queue!

💡 Bài học: Phải cẩn thận khi tạo microtask trong microtask
*/
```

**🔍 Ví dụ 3: Call Stack với Async/Await**

```typescript
async function asyncFunction() {
  console.log('2: Inside async - before await');

  await Promise.resolve(); // ⚡ await tạo microtask

  console.log('5: After await (microtask)');
}

console.log('1: Start');
asyncFunction();
console.log('3: After calling async');

Promise.resolve().then(() => console.log('4: Promise.then (microtask)'));

setTimeout(() => console.log('6: setTimeout (macrotask)'), 0);

/* OUTPUT:
1: Start
2: Inside async - before await
3: After calling async
4: Promise.then (microtask)
5: After await (microtask)
6: setTimeout (macrotask)

📋 Giải thích:
- `await` biến code phía sau thành microtask
- Tất cả microtasks (4, 5) chạy trước macrotask (6)
*/
```

**🔍 Ví dụ 4: Thực Tế trong Trading App**

```typescript
interface OrderUpdate {
  orderId: string;
  status: 'pending' | 'filled';
  price: number;
}

class TradingUI {
  private pendingUpdates: OrderUpdate[] = [];

  // ❌ BAD: Mỗi update render ngay (gây lag)
  updateOrderBad(order: OrderUpdate) {
    this.renderOrder(order); // Render ngay lập tức
  }

  // ✅ GOOD: Batch updates với microtask
  updateOrderGood(order: OrderUpdate) {
    this.pendingUpdates.push(order);

    // queueMicrotask: Batch tất cả updates trong cùng 1 tick
    queueMicrotask(() => {
      if (this.pendingUpdates.length > 0) {
        this.renderBatch(this.pendingUpdates);
        this.pendingUpdates = [];
      }
    });
  }

  private renderOrder(order: OrderUpdate) {
    console.log(`Render single order: ${order.orderId}`);
    // DOM update expensive
  }

  private renderBatch(orders: OrderUpdate[]) {
    console.log(`Render ${orders.length} orders in 1 batch`);
    // DOM update once - HIỆU QUẢ HƠN!
  }
}

// Test
const ui = new TradingUI();

// Giả sử nhận 100 updates cùng lúc từ WebSocket
for (let i = 0; i < 100; i++) {
  ui.updateOrderGood({
    orderId: `ORD-${i}`,
    status: 'filled',
    price: 100 + i,
  });
}

/* 🎯 KẾT QUẢ:
❌ updateOrderBad: Render 100 lần → LAG UI
✅ updateOrderGood: Render 1 lần với 100 items → SMOOTH UI

💡 Microtask giúp batch operations trong cùng 1 Event Loop tick
*/
```

**Best Practices:**

```typescript
// ✅ DO: Sử dụng microtask cho batch operations
class StateManager {
  private updates: Set<() => void> = new Set();
  private scheduled = false;

  scheduleUpdate(callback: () => void) {
    this.updates.add(callback);

    if (!this.scheduled) {
      this.scheduled = true;
      queueMicrotask(() => {
        this.updates.forEach((cb) => cb());
        this.updates.clear();
        this.scheduled = false;
      });
    }
  }
}

// ✅ DO: Sử dụng macrotask cho defer work
function deferExpensiveWork(work: () => void) {
  setTimeout(work, 0); // Chạy sau khi UI render
}

// ❌ DON'T: Tạo vô hạn microtasks
function badInfiniteMicrotask() {
  Promise.resolve().then(() => badInfiniteMicrotask()); // CHẶN macrotasks!
}

// ✅ DO: Break vòng lặp với macrotask
function goodDeferWork(count: number) {
  if (count > 0) {
    setTimeout(() => goodDeferWork(count - 1), 0); // Cho phép UI render
  }
}

// ✅ DO: Hiểu thứ tự execution để debug
async function debugEventLoop() {
  console.log('1: Sync');

  queueMicrotask(() => console.log('3: Microtask'));

  await Promise.resolve();
  console.log('4: After await (microtask)');

  setTimeout(() => console.log('5: Macrotask'), 0);

  console.log('2: Sync end');
}
```

**📋 Tóm tắt Best Practices:**

1. **Microtask (`Promise`, `queueMicrotask`)**: Dùng cho state updates, batch operations cần xử lý ngay
2. **Macrotask (`setTimeout`)**: Dùng cho defer work, animations, cho phép UI render giữa các tasks
3. **Tránh Microtask Starvation**: Không tạo vô hạn microtasks, phải có điều kiện dừng
4. **Async/await**: Hiểu rằng code sau `await` là microtask
5. **Debugging**: Luôn nhớ thứ tự: `Call Stack → All Microtasks → Render → One Macrotask`

**Common Mistakes:**

```typescript
// ❌ MISTAKE 1: Nghĩ setTimeout(fn, 0) chạy ngay lập tức
console.log('1');
setTimeout(() => console.log('2'), 0);
console.log('3');
// Output: 1, 3, 2 (KHÔNG phải 1, 2, 3!)
// ⚠️ setTimeout là macrotask, chạy sau tất cả microtasks

// ❌ MISTAKE 2: Quên Promise.then là microtask
setTimeout(() => console.log('1: Macro'), 0);
Promise.resolve().then(() => console.log('2: Micro'));
// Output: 2, 1 (microtask chạy TRƯỚC macrotask!)

// ❌ MISTAKE 3: Blocking Event Loop với synchronous heavy work
function heavyCalculation() {
  const start = Date.now();
  while (Date.now() - start < 5000) {} // Block 5 giây!
  console.log('Done');
}

heavyCalculation(); // UI đóng băng 5 giây!

// ✅ FIX: Break thành chunks với setTimeout
function heavyCalculationFixed(iterations: number, callback: () => void) {
  const chunkSize = 100;
  let current = 0;

  function processChunk() {
    const end = Math.min(current + chunkSize, iterations);

    for (let i = current; i < end; i++) {
      // Do heavy work
    }

    current = end;

    if (current < iterations) {
      setTimeout(processChunk, 0); // Cho UI render
    } else {
      callback();
    }
  }

  processChunk();
}

// ❌ MISTAKE 4: Microtask starvation
let count = 0;
function addMicrotask() {
  if (count++ < 1000000) {
    Promise.resolve().then(addMicrotask); // Vô hạn microtasks!
  }
}
addMicrotask(); // Macrotasks bị chặn!

// ✅ FIX: Giới hạn hoặc dùng macrotask
function addMicrotaskFixed() {
  if (count++ < 1000000) {
    setTimeout(() => addMicrotaskFixed(), 0); // Cho phép macrotasks khác chạy
  }
}
```

**📋 Chú thích về các lỗi thường gặp:**

1. **setTimeout(fn, 0) ≠ chạy ngay**: Nó là macrotask, chạy sau tất cả microtasks và code đồng bộ
2. **Promise.then chạy trước setTimeout**: Microtask luôn ưu tiên cao hơn macrotask
3. **Blocking code làm đóng băng UI**: Phải break heavy work thành chunks với setTimeout
4. **Microtask starvation**: Tạo vô hạn microtasks sẽ chặn macrotasks → UI không render được

---

## 🎨 EVENT LOOP DEEP DIVE - BROWSER RENDERING PIPELINE

### **7. Browser Rendering Cycle**

**🔍 Vị trí Rendering trong Event Loop:**

```
┌─────────────────────────────────────────────────────────────┐
│              BROWSER EVENT LOOP CYCLE (Chi tiết)            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1️⃣ Execute JavaScript (Call Stack)                        │
│     └─ Run all synchronous code                            │
│                                                             │
│  2️⃣ Process ALL Microtasks                                 │
│     ├─ process.nextTick() (Node.js)                        │
│     ├─ Promise callbacks                                   │
│     └─ queueMicrotask()                                    │
│                                                             │
│  3️⃣ Render Pipeline (60fps = ~16.67ms budget)             │
│     ├─ requestAnimationFrame callbacks                     │
│     ├─ Recalculate Styles (CSSOM)                          │
│     ├─ Layout (Reflow) - tính vị trí/kích thước           │
│     ├─ Paint - tạo draw commands                           │
│     └─ Composite - GPU render layers                       │
│                                                             │
│  4️⃣ requestIdleCallback (if time remains)                  │
│     └─ Low priority work khi browser rảnh                  │
│                                                             │
│  5️⃣ Process ONE Macrotask                                  │
│     ├─ setTimeout/setInterval                              │
│     ├─ Event callbacks (click, scroll...)                  │
│     └─ I/O callbacks                                       │
│                                                             │
│  ↻ Repeat (typically 60 times/second)                      │
└─────────────────────────────────────────────────────────────┘
```

---

### **8. requestAnimationFrame (RAF) - Timing Chi Tiết**

**🎯 Khi nào RAF callbacks chạy:**

```typescript
// ===================================================
// 🎬 RAF vs setTimeout - TIMING COMPARISON
// ===================================================

console.log('1: Start');

// ❌ setTimeout: Không đồng bộ với frame
setTimeout(() => {
  console.log('4: setTimeout - có thể chạy GIỮA frame → janky animation');
  document.body.style.transform = 'translateX(100px)';
}, 16); // ~16ms ≈ 1 frame, nhưng không chính xác

// ✅ RAF: Chạy ĐÚNG TRƯỚC KHI browser paint
requestAnimationFrame(() => {
  console.log('3: RAF - chạy NGAY TRƯỚC khi paint → smooth animation');
  document.body.style.transform = 'translateX(100px)';
});

console.log('2: Sync end');

/* OUTPUT TIMELINE:
0ms    → "1: Start"
0ms    → "2: Sync end"
~16ms  → "3: RAF" (chạy đúng trước next paint)
~16ms  → Browser paint frame
~16ms  → "4: setTimeout" (có thể chạy sau paint → wasted work)
*/

// ===================================================
// 🎨 SMOOTH ANIMATION với RAF
// ===================================================

class SmoothAnimation {
  private startTime: number | null = null;
  private duration = 1000; // 1 giây

  animate(element: HTMLElement) {
    const step = (timestamp: number) => {
      // ① Khởi tạo startTime
      if (!this.startTime) this.startTime = timestamp;

      // ② Tính progress (0 → 1)
      const elapsed = timestamp - this.startTime;
      const progress = Math.min(elapsed / this.duration, 1);

      // ③ Apply easing function
      const eased = this.easeOutCubic(progress);

      // ④ Update DOM
      element.style.transform = `translateX(${eased * 500}px)`;

      // ⑤ Continue nếu chưa xong
      if (progress < 1) {
        requestAnimationFrame(step);
      }
    };

    requestAnimationFrame(step);
  }

  private easeOutCubic(t: number): number {
    return 1 - Math.pow(1 - t, 3);
  }
}

// Usage
const animator = new SmoothAnimation();
animator.animate(document.getElementById('box')!);

// ===================================================
// ⚡ RAF + BATCH DOM READS/WRITES (FastDOM pattern)
// ===================================================

class FastDOM {
  private reads: Array<() => void> = [];
  private writes: Array<() => void> = [];
  private scheduled = false;

  // ✅ Schedule read (measure)
  measure(callback: () => void) {
    this.reads.push(callback);
    this.scheduleFlush();
  }

  // ✅ Schedule write (mutate)
  mutate(callback: () => void) {
    this.writes.push(callback);
    this.scheduleFlush();
  }

  private scheduleFlush() {
    if (this.scheduled) return;
    this.scheduled = true;

    requestAnimationFrame(() => {
      // ① Execute ALL reads first (prevent layout thrashing)
      this.reads.forEach((fn) => fn());
      this.reads = [];

      // ② Then execute ALL writes
      this.writes.forEach((fn) => fn());
      this.writes = [];

      this.scheduled = false;
    });
  }
}

// Usage - Tránh layout thrashing
const fastdom = new FastDOM();

// ❌ BAD: Interleaved read/write → layout thrashing
for (let i = 0; i < 100; i++) {
  const height = element.offsetHeight; // READ → force layout
  element.style.height = height + 10 + 'px'; // WRITE → invalidate layout
} // 100 layouts! 🐌

// ✅ GOOD: Batch reads, then writes
for (let i = 0; i < 100; i++) {
  fastdom.measure(() => {
    const height = element.offsetHeight; // READ
    fastdom.mutate(() => {
      element.style.height = height + 10 + 'px'; // WRITE
    });
  });
} // 1 layout only! ⚡
```

---

### **9. requestIdleCallback - Low Priority Work**

**🔍 Khi nào dùng requestIdleCallback:**

```typescript
// ===================================================
// 🕐 requestIdleCallback - DEFERRED WORK
// ===================================================

interface IdleDeadline {
  didTimeout: boolean;
  timeRemaining(): number; // ms còn lại trong frame
}

// ✅ Analytics tracking (không urgent)
requestIdleCallback((deadline: IdleDeadline) => {
  while (deadline.timeRemaining() > 0 && analyticsQueue.length > 0) {
    const event = analyticsQueue.shift();
    sendAnalytics(event);
  }

  // ⚠️ Nếu còn events, schedule lại
  if (analyticsQueue.length > 0) {
    requestIdleCallback(processAnalytics);
  }
});

// ===================================================
// 🎯 PRELOAD IMAGES khi browser rảnh
// ===================================================

const imagesToPreload = [
  '/img1.jpg',
  '/img2.jpg',
  '/img3.jpg',
  // ... 100 images
];

function preloadImages(deadline: IdleDeadline) {
  while (
    deadline.timeRemaining() > 0 && // Còn thời gian
    imagesToPreload.length > 0
  ) {
    const img = new Image();
    img.src = imagesToPreload.shift()!;
  }

  // Continue nếu còn images
  if (imagesToPreload.length > 0) {
    requestIdleCallback(preloadImages);
  }
}

requestIdleCallback(preloadImages, { timeout: 2000 }); // Force sau 2s nếu không rảnh

// ===================================================
// 🧹 CLEANUP old cache entries
// ===================================================

class CacheCleanup {
  private cacheEntries = new Map<string, { data: any; timestamp: number }>();

  scheduleCleanup() {
    requestIdleCallback((deadline) => {
      const now = Date.now();
      const maxAge = 1000 * 60 * 60; // 1 hour

      for (const [key, entry] of this.cacheEntries) {
        // ⚠️ Kiểm tra còn thời gian không
        if (deadline.timeRemaining() < 1) {
          // Reschedule
          this.scheduleCleanup();
          return;
        }

        // Xóa entries cũ
        if (now - entry.timestamp > maxAge) {
          this.cacheEntries.delete(key);
        }
      }
    });
  }
}
```

---

## 🔧 NODE.JS EVENT LOOP - PHASES DEEP DIVE

### **10. Node.js Event Loop Architecture**

**🔍 6 Phases của Node.js Event Loop:**

```
┌───────────────────────────────────────────────────────────┐
│              NODE.JS EVENT LOOP PHASES                    │
├───────────────────────────────────────────────────────────┤
│                                                           │
│   ┌─────────────────────────────────────────┐            │
│   │  1️⃣ TIMERS PHASE                        │            │
│   │  Execute setTimeout() / setInterval()   │            │
│   └──────────────┬──────────────────────────┘            │
│                  │                                        │
│   ┌──────────────▼──────────────────────────┐            │
│   │  2️⃣ PENDING CALLBACKS PHASE             │            │
│   │  I/O callbacks deferred từ phase trước  │            │
│   └──────────────┬──────────────────────────┘            │
│                  │                                        │
│   ┌──────────────▼──────────────────────────┐            │
│   │  3️⃣ IDLE, PREPARE PHASE                 │            │
│   │  Internal use only                      │            │
│   └──────────────┬──────────────────────────┘            │
│                  │                                        │
│   ┌──────────────▼──────────────────────────┐            │
│   │  4️⃣ POLL PHASE ⭐ (QUAN TRỌNG NHẤT)    │            │
│   │  ├─ Retrieve new I/O events             │            │
│   │  ├─ Execute I/O callbacks               │            │
│   │  └─ Block here khi không có pending     │            │
│   │     timers/setImmediate                 │            │
│   └──────────────┬──────────────────────────┘            │
│                  │                                        │
│   ┌──────────────▼──────────────────────────┐            │
│   │  5️⃣ CHECK PHASE                         │            │
│   │  Execute setImmediate() callbacks       │            │
│   └──────────────┬──────────────────────────┘            │
│                  │                                        │
│   ┌──────────────▼──────────────────────────┐            │
│   │  6️⃣ CLOSE CALLBACKS PHASE               │            │
│   │  socket.on('close', ...) callbacks      │            │
│   └──────────────┬──────────────────────────┘            │
│                  │                                        │
│                  └──────────────┐                         │
│                                 │                         │
│   ⚡ MICROTASK QUEUES (giữa các phases):                 │
│   ├─ process.nextTick() queue (highest priority)        │
│   └─ Promise microtask queue                            │
│                                 │                         │
│                  ┌──────────────┘                         │
│                  │                                        │
│                  └──→ Loop back to Phase 1               │
│                                                           │
└───────────────────────────────────────────────────────────┘
```

---

### **11. Node.js: setTimeout vs setImmediate**

**🎯 THỨ TỰ PHỤ THUỘC CONTEXT:**

```typescript
// ===================================================
// 🔀 CASE 1: Main module (non-I/O context)
// ===================================================

// THỨ TỰ KHÔNG DETERMINISTIC (phụ thuộc timing)
setTimeout(() => console.log('setTimeout'), 0);
setImmediate(() => console.log('setImmediate'));

/* OUTPUT: CÓ THỂ LÀ:
setTimeout
setImmediate

HOẶC:

setImmediate
setTimeout

🔍 LÝ DO:
- setTimeout(fn, 0) thực tế là setTimeout(fn, 1) (minimum 1ms)
- Nếu Event Loop vào Timers phase SAU 1ms → setTimeout chạy trước
- Nếu Event Loop vào Timers phase TRƯỚC 1ms → skip, setImmediate chạy trước
*/

// ===================================================
// 🔀 CASE 2: I/O cycle context
// ===================================================

const fs = require('fs');

fs.readFile('file.txt', () => {
  // ✅ TRONG I/O callback, thứ tự LUÔN deterministic
  setTimeout(() => console.log('setTimeout'), 0);
  setImmediate(() => console.log('setImmediate'));
});

/* OUTPUT: LUÔN LUÔN:
setImmediate
setTimeout

🔍 LÝ DO:
- I/O callback chạy ở POLL phase
- Sau POLL phase → CHECK phase (setImmediate)
- Rồi mới loop về TIMERS phase (setTimeout)
→ setImmediate LUÔN chạy trước setTimeout trong I/O callbacks
*/

// ===================================================
// 🎯 process.nextTick() - HIGHEST PRIORITY
// ===================================================

setImmediate(() => console.log('1: setImmediate'));

Promise.resolve().then(() => console.log('2: Promise'));

process.nextTick(() => console.log('3: nextTick'));

/* OUTPUT:
3: nextTick         ← nextTick queue (highest)
2: Promise          ← Promise microtask queue
1: setImmediate     ← Check phase

🔍 THỨ TỰ trong Node.js:
1. process.nextTick() queue
2. Promise microtask queue
3. Macrotasks (timers, setImmediate...)
*/

// ===================================================
// ⚠️  NGUY HIỂM: nextTick starvation
// ===================================================

// ❌ BAD: Block Event Loop
function dangerousRecursion() {
  process.nextTick(dangerousRecursion);
}
dangerousRecursion();

/* ⚠️ KẾT QUẢ:
- nextTick queue không bao giờ trống
- Event Loop không bao giờ tiến tới các phases khác
- I/O callbacks, timers, setImmediate KHÔNG BAO GIỜ chạy
- Server treo hoàn toàn!
*/

// ✅ GOOD: Giới hạn hoặc dùng setImmediate
function safeRecursion(count: number) {
  if (count > 0) {
    setImmediate(() => safeRecursion(count - 1)); // Cho phép I/O xử lý
  }
}
safeRecursion(1000000); // OK, không block I/O
```

---

### **12. Performance Optimization Patterns**

**🚀 Patterns tối ưu Event Loop:**

```typescript
// ===================================================
// Pattern 1: DEBOUNCE (Giảm tần suất execution)
// ===================================================

function debounce<T extends (...args: any[]) => void>(
  fn: T,
  delay: number
): (...args: Parameters<T>) => void {
  let timeoutId: NodeJS.Timeout | null = null;

  return function (...args: Parameters<T>) {
    // Clear timeout cũ
    if (timeoutId) clearTimeout(timeoutId);

    // Set timeout mới
    timeoutId = setTimeout(() => {
      fn(...args);
      timeoutId = null;
    }, delay);
  };
}

// Usage: Search input
const searchInput = document.getElementById('search') as HTMLInputElement;
const debouncedSearch = debounce((query: string) => {
  console.log('API call:', query);
  fetch(`/api/search?q=${query}`);
}, 300); // Chỉ call API sau 300ms user NGƯNG gõ

searchInput.addEventListener('input', (e) => {
  debouncedSearch((e.target as HTMLInputElement).value);
});

// ===================================================
// Pattern 2: THROTTLE (Giới hạn execution rate)
// ===================================================

function throttle<T extends (...args: any[]) => void>(
  fn: T,
  limit: number
): (...args: Parameters<T>) => void {
  let inThrottle = false;

  return function (...args: Parameters<T>) {
    if (inThrottle) return;

    fn(...args);
    inThrottle = true;

    setTimeout(() => {
      inThrottle = false;
    }, limit);
  };
}

// Usage: Scroll event
const throttledScroll = throttle(() => {
  console.log('Scroll position:', window.scrollY);
}, 100); // Tối đa 10 lần/giây (100ms interval)

window.addEventListener('scroll', throttledScroll);

// ===================================================
// Pattern 3: TIME SLICING (Chia nhỏ heavy tasks)
// ===================================================

class TimeSlicing {
  async processLargeArray<T, R>(
    items: T[],
    processor: (item: T) => R,
    options: {
      chunkSize?: number;
      onProgress?: (progress: number) => void;
    } = {}
  ): Promise<R[]> {
    const { chunkSize = 100, onProgress } = options;
    const results: R[] = [];
    let processed = 0;

    for (let i = 0; i < items.length; i += chunkSize) {
      // ① Process chunk
      const chunk = items.slice(i, i + chunkSize);
      const chunkResults = chunk.map(processor);
      results.push(...chunkResults);

      processed += chunk.length;

      // ② Report progress
      if (onProgress) {
        onProgress((processed / items.length) * 100);
      }

      // ③ Yield to Event Loop (cho UI render)
      await new Promise((resolve) => setTimeout(resolve, 0));
    }

    return results;
  }
}

// Usage
const slicer = new TimeSlicing();
const largeData = Array.from({ length: 100000 }, (_, i) => i);

slicer
  .processLargeArray(
    largeData,
    (n) => n * 2, // Heavy calculation
    {
      chunkSize: 1000,
      onProgress: (progress) => {
        console.log(`Progress: ${progress.toFixed(1)}%`);
        // Update UI progress bar
        progressBar.style.width = `${progress}%`;
      },
    }
  )
  .then((results) => console.log('Done:', results.length));

// ===================================================
// Pattern 4: IDLE CALLBACK QUEUE (Low priority work)
// ===================================================

class IdleQueue {
  private queue: Array<() => void> = [];
  private processing = false;

  add(task: () => void) {
    this.queue.push(task);
    this.scheduleProcessing();
  }

  private scheduleProcessing() {
    if (this.processing) return;
    this.processing = true;

    requestIdleCallback((deadline) => {
      while (deadline.timeRemaining() > 0 && this.queue.length > 0) {
        const task = this.queue.shift()!;
        task();
      }

      this.processing = false;

      // Reschedule nếu còn tasks
      if (this.queue.length > 0) {
        this.scheduleProcessing();
      }
    });
  }
}

// Usage
const idleQueue = new IdleQueue();

// Thêm 1000 low-priority tasks
for (let i = 0; i < 1000; i++) {
  idleQueue.add(() => {
    localStorage.setItem(`cache_${i}`, JSON.stringify({ data: i }));
  });
}
// Tasks chỉ chạy khi browser RẢNH, không ảnh hưởng scrolling/animation
```

---

### **13. Real-World Debugging Scenarios**

**🐛 Scenario 1: Jank trong Animation**

```typescript
// ===================================================
// 🐌 PROBLEM: Janky animation (dropped frames)
// ===================================================

// ❌ BAD: Force sync layout trong animation
function animateBad(element: HTMLElement) {
  let position = 0;

  function frame() {
    position += 5;

    // ⚠️ READ: Force layout calculation
    const currentHeight = element.offsetHeight;

    // ⚠️ WRITE: Invalidate layout
    element.style.transform = `translateX(${position}px)`;

    // ⚠️ READ AGAIN: Another forced layout!
    const newHeight = element.offsetHeight;

    if (position < 500) {
      requestAnimationFrame(frame);
    }
  }

  requestAnimationFrame(frame);
}

// ✅ GOOD: Separate reads and writes
function animateGood(element: HTMLElement) {
  let position = 0;
  let height: number;

  function frame() {
    // ① READ phase (before any writes)
    height = element.offsetHeight;

    // ② WRITE phase
    position += 5;
    element.style.transform = `translateX(${position}px)`;

    if (position < 500) {
      requestAnimationFrame(frame);
    }
  }

  requestAnimationFrame(frame);
}

// ===================================================
// 🔍 DEBUGGING: Performance DevTools
// ===================================================

/*
Chrome DevTools → Performance Tab:

❌ BAD animation shows:
  - Yellow warnings: "Forced reflow"
  - FPS drops < 60
  - Long "Recalculate Style" bars

✅ GOOD animation shows:
  - Green 60fps line
  - No forced reflows
  - Short frame times (~16ms)
*/
```

---

**🐛 Scenario 2: Memory Leak với Timers**

```typescript
// ===================================================
// 💧 PROBLEM: Memory leak với setInterval
// ===================================================

// ❌ BAD: Không cleanup interval
class BadComponent {
  private data: number[] = [];

  mount() {
    setInterval(() => {
      this.data.push(Math.random()); // Memory leak!
    }, 1000);
  }

  unmount() {
    // ⚠️ setInterval vẫn chạy → this.data vẫn tăng → memory leak
  }
}

// ✅ GOOD: Cleanup trong unmount
class GoodComponent {
  private data: number[] = [];
  private intervalId: NodeJS.Timeout | null = null;

  mount() {
    this.intervalId = setInterval(() => {
      this.data.push(Math.random());
    }, 1000);
  }

  unmount() {
    if (this.intervalId) {
      clearInterval(this.intervalId);
      this.intervalId = null;
    }
    this.data = []; // Clear data
  }
}

// ===================================================
// 🔍 DEBUGGING: Memory Profiler
// ===================================================

/*
Chrome DevTools → Memory Tab → Take heap snapshot:

❌ BAD: Heap size tăng liên tục mỗi giây
✅ GOOD: Heap size stable

Detached DOM nodes:
❌ BAD: Số lượng detached nodes tăng
✅ GOOD: Số lượng stable hoặc giảm sau GC
*/
```

---

**🐛 Scenario 3: Race Condition với Async Code**

```typescript
// ===================================================
// 🏁 PROBLEM: Race condition với multiple API calls
// ===================================================

// ❌ BAD: Không handle concurrent requests
class BadSearchComponent {
  private results: any[] = [];

  async search(query: string) {
    const data = await fetch(`/api/search?q=${query}`).then((r) => r.json());
    this.results = data; // ⚠️ Có thể bị overwrite bởi request cũ!
  }
}

/*
Timeline:
0ms   → User types "react"
100ms → User types "react hooks"
      → API call 1: "/api/search?q=react" started
      → API call 2: "/api/search?q=react hooks" started
300ms → API call 2 returns → this.results = [hooks results]
500ms → API call 1 returns → this.results = [react results] ⚠️ WRONG!

User sees results for "react" instead of "react hooks"!
*/

// ✅ GOOD: Abort previous requests
class GoodSearchComponent {
  private results: any[] = [];
  private abortController: AbortController | null = null;

  async search(query: string) {
    // ① Abort previous request
    if (this.abortController) {
      this.abortController.abort();
    }

    // ② Create new controller
    this.abortController = new AbortController();

    try {
      const data = await fetch(`/api/search?q=${query}`, {
        signal: this.abortController.signal,
      }).then((r) => r.json());

      this.results = data; // ✅ Only latest request updates results
    } catch (err) {
      if (err.name === 'AbortError') {
        console.log('Request aborted');
      }
    }
  }
}

// ===================================================
// ✅ ALTERNATIVE: Request ID tracking
// ===================================================

class RequestIdSearchComponent {
  private results: any[] = [];
  private latestRequestId = 0;

  async search(query: string) {
    const requestId = ++this.latestRequestId;

    const data = await fetch(`/api/search?q=${query}`).then((r) => r.json());

    // ✅ Only update if this is still the latest request
    if (requestId === this.latestRequestId) {
      this.results = data;
    } else {
      console.log('Stale request, ignoring');
    }
  }
}
```

---

## 📊 PERFORMANCE MONITORING & PROFILING

### **14. Long Task API - Detect Blocking Code**

```typescript
// ===================================================
// 🔍 DETECT LONG TASKS (> 50ms)
// ===================================================

// Browser API để track long tasks
const observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    // ⚠️ Task > 50ms detected!
    console.warn('Long task detected:', {
      duration: entry.duration,
      startTime: entry.startTime,
      name: entry.name,
    });

    // Send to analytics
    sendToAnalytics({
      type: 'long-task',
      duration: entry.duration,
      url: window.location.href,
    });
  }
});

observer.observe({ entryTypes: ['longtask'] });

// ===================================================
// 📊 USER TIMING API - Custom metrics
// ===================================================

// Mark start
performance.mark('search-start');

// ... do work
await performSearch(query);

// Mark end
performance.mark('search-end');

// Measure duration
performance.measure('search-duration', 'search-start', 'search-end');

// Get results
const measure = performance.getEntriesByName('search-duration')[0];
console.log(`Search took ${measure.duration}ms`);

// Send to analytics
sendToAnalytics({
  metric: 'search-duration',
  value: measure.duration,
});
```

---

## 🎯 BEST PRACTICES CHECKLIST

```
✅ EVENT LOOP OPTIMIZATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
☑️  Dùng RAF cho animations (không dùng setTimeout)
☑️  Batch DOM reads/writes (FastDOM pattern)
☑️  Debounce/throttle high-frequency events
☑️  Time-slice heavy computations (yield mỗi 16ms)
☑️  Dùng requestIdleCallback cho low-priority work
☑️  Cleanup timers/intervals trong unmount
☑️  Abort stale requests (AbortController)
☑️  Monitor long tasks (> 50ms)
☑️  Profile với Chrome DevTools Performance tab
☑️  Tránh microtask starvation (giới hạn recursion)

✅ NODE.JS SPECIFIC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
☑️  Prefer setImmediate over setTimeout(fn, 0) trong I/O
☑️  Tránh process.nextTick recursion vô hạn
☑️  Dùng worker_threads cho CPU-intensive tasks
☑️  Monitor Event Loop lag với libraries (loopbench)
☑️  Cluster mode cho multi-core utilization

✅ DEBUGGING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
☑️  Chrome DevTools → Performance tab (timeline)
☑️  Memory profiler (heap snapshots)
☑️  Long Task API monitoring
☑️  User Timing API cho custom metrics
☑️  Lighthouse performance audit
```
