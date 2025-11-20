# 🔄 Q12: Event Loop - Cơ Chế Hoạt Động JavaScript (Technical Deep Dive)

<details>
<summary><span style="font-size:1.25em;font-weight:bold;">🔄 Q12: Event Loop - Cơ Chế Hoạt Động JavaScript (Technical Deep Dive)</span></summary>


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
</details>