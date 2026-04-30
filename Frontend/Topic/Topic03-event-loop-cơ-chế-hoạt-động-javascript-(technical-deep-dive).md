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
// 📚 CALL STACK - Minh họa cách thức hoạt động LIFO (Last In First Out)

// 🔢 Hàm nhân 2 số - Level 3 (sâu nhất)
function multiply(a: number, b: number): number {
  return a * b; // ③ 🔙 Tính toán xong → Pop ra khỏi stack
}

// 🔢 Hàm tính bình phương - Level 2
function square(n: number): number {
  return multiply(n, n); // ② ➡️ Push multiply lên stack → Gọi multiply(5, 5)
  // Sau khi multiply return → Pop square ra
}

// 📝 Hàm in kết quả - Level 1
function printSquare(n: number): void {
  const result = square(n); // ① ➡️ Push square lên stack → Gọi square(5)
  console.log(result); // 📤 In ra 25
}

// 🎬 Gọi hàm chính
printSquare(5);

/* 📊 CALL STACK TIMELINE (Theo thời gian):

   ⏰ Bước 1: Bắt đầu
   → main() ← 📌 Script chính đang chạy

   ⏰ Bước 2: Gọi printSquare(5)
   → main() → printSquare(5) ← 📌 Push printSquare lên stack

   ⏰ Bước 3: printSquare gọi square(5)
   → main() → printSquare(5) → square(5) ← 📌 Push square lên stack

   ⏰ Bước 4: square gọi multiply(5, 5)
   → main() → printSquare(5) → square(5) → multiply(5, 5) ← 📌 Stack cao nhất

   ⏰ Bước 5: multiply return 25
   → main() → printSquare(5) → square(5) ← 🔙 Pop multiply ra

   ⏰ Bước 6: square return 25
   → main() → printSquare(5) ← 🔙 Pop square ra

   ⏰ Bước 7: printSquare in 25 và return
   → main() ← 🔙 Pop printSquare ra

   ⏰ Bước 8: Hoàn thành
   → [empty] ← ✅ Stack rỗng, chương trình kết thúc
*/
```

**⚠️ Stack Overflow - Tràn Stack:**

```typescript
// ============================================
// ❌ LỖI NGUY HIỂM: Recursive không có base case
// ============================================

// 🔁 Hàm đệ quy VÔ HẠN - KHÔNG CÓ ĐIỀU KIỆN DỪNG!
function recursiveFunction() {
  recursiveFunction(); // 💀 Gọi chính nó liên tục → Stack tăng mãi
  // ⚠️ KHÔNG BAO GIỜ return → Stack không bao giờ giảm!
}

recursiveFunction();
// 💥 CRASH: RangeError: Maximum call stack size exceeded
// 📊 Chrome: ~10,000 calls
// 📊 Firefox: ~50,000 calls
// 📊 Node.js: ~15,000 calls

/* 📚 STACK TIMELINE KHI CRASH:
   recursiveFunction() ← Call 1
   → recursiveFunction() ← Call 2
   → → recursiveFunction() ← Call 3
   → → → recursiveFunction() ← Call 4
   ... (10,000+ calls)
   💥 BOOM! Stack overflow!
*/

// ============================================
// ✅ CÁCH SỬA: Thêm điều kiện dừng (base case)
// ============================================

function safeRecursive(n: number): number {
  // 🛑 BASE CASE: Điều kiện dừng
  if (n <= 0) {
    return 0; // 🔙 Dừng đệ quy, bắt đầu pop stack
  }

  // 🔄 RECURSIVE CASE: Gọi đệ quy với n nhỏ hơn
  return n + safeRecursive(n - 1); // ✅ Mỗi lần n giảm → cuối cùng sẽ = 0
}

console.log(safeRecursive(5)); // ✅ Output: 15 (5+4+3+2+1)
// 📊 Stack: Tối đa 6 calls (0→1→2→3→4→5) → an toàn!
```

---

**🌐 3. WEB APIs**

**Khái niệm:**

- APIs được cung cấp bởi **Browser** (hoặc Node.js runtime), KHÔNG phải JavaScript Engine
- Chạy **bên ngoài** Call Stack → không block main thread
- Khi hoàn thành, callbacks được đưa vào Queues

**Các Web APIs phổ biến:**

```typescript
// ============================================
// 🌐 WEB APIs - Chạy BÊN NGOÀI JavaScript Engine
// ============================================

// 💡 Tất cả APIs này đều:
// 1️⃣ Chạy ở background (không block main thread)
// 2️⃣ Callback được đưa vào Task Queue khi xong
// 3️⃣ Event Loop sẽ lấy callback vào Call Stack khi stack trống

// ============================================
// A. ⏰ TIMERS - Hẹn giờ thực thi
// ============================================

// 🕐 setTimeout: Chạy 1 LẦN sau delay
setTimeout(() => console.log('⏰ Timer done'), 1000);
// 📋 Cách hoạt động:
// 1. Browser đặt timer 1000ms ở background
// 2. Sau 1000ms → callback vào Macrotask Queue
// 3. Event Loop lấy callback vào Call Stack

// 🔄 setInterval: Chạy LẶP LẠI mỗi interval
setInterval(() => console.log('🔔 Tick'), 1000);
// ⚠️ Chú ý: Callback chạy MỖI 1000ms cho đến khi clearInterval()

// ============================================
// B. 🖱️ DOM EVENTS - Sự kiện người dùng
// ============================================

document.getElementById('btn').addEventListener('click', () => {
  console.log('🖱️ Button clicked');
});
// 📋 Cách hoạt động:
// 1. Browser lắng nghe click event ở background
// 2. User click → callback vào Macrotask Queue
// 3. Event Loop lấy callback vào Call Stack
// 💡 KHÔNG block code khác trong lúc chờ user click!

// ============================================
// C. 🌍 NETWORK REQUESTS - Gọi API
// ============================================

fetch('https://api.example.com/data')
  .then((response) => response.json()) // ⚡ Microtask
  .then((data) => console.log('📥 Data:', data)); // ⚡ Microtask
// 📋 Cách hoạt động:
// 1. Browser gửi HTTP request ở background (không block!)
// 2. Response về → .then() callback vào Microtask Queue
// 3. Event Loop xử lý Microtasks (priority cao)

// ============================================
// D. 📁 FILE APIs - Đọc file
// ============================================

const reader = new FileReader();
reader.onload = (e) => console.log('📄 File content:', e.target.result);
reader.readAsText(file);
// 📋 Cách hoạt động:
// 1. Browser đọc file ở background (I/O operation)
// 2. Đọc xong → onload callback vào Macrotask Queue
// 3. Event Loop lấy callback vào Call Stack
// 💡 Main thread KHÔNG BỊ BLOCK trong lúc đọc file!

// ============================================
// E. 👁️ OBSERVERS - Theo dõi thay đổi
// ============================================

const observer = new IntersectionObserver((entries) => {
  console.log('👁️ Element intersected:', entries);
});
observer.observe(document.querySelector('.target'));
// 📋 Cách hoạt động:
// 1. Browser theo dõi element position ở background
// 2. Element vào viewport → callback vào Macrotask Queue
// 💡 Dùng cho lazy loading, infinite scroll

// ============================================
// F. 📍 GEOLOCATION - Lấy vị trí GPS
// ============================================

navigator.geolocation.getCurrentPosition(
  (position) => console.log('📍 Location:', position.coords),
  (error) => console.error('❌ Error:', error)
);
// 📋 Cách hoạt động:
// 1. Browser request GPS data từ device (async!)
// 2. Lấy được location → success callback vào Macrotask Queue
// 3. Lỗi → error callback vào Macrotask Queue
// 💡 KHÔNG block trong lúc chờ GPS (có thể mất vài giây!)
```

---

**⚡ 4. MICROTASK QUEUE (Job Queue)**

**Khái niệm:**

- Hàng đợi chứa **microtasks** (priority cao)
- **Xử lý TẤT CẢ** microtasks trước khi chuyển sang macrotask
- Ưu tiên: **process.nextTick()** > **Promise** > **queueMicrotask**

**Các Microtasks:**

```typescript
// ============================================
// ⚡ MICROTASK QUEUE - Ưu tiên CAO NHẤT
// ============================================

// 💡 ĐẶC ĐIỂM QUAN TRỌNG:
// 1. Event Loop xử lý TẤT CẢ microtasks trước khi chuyển sang macrotask
// 2. Nếu microtask tạo thêm microtask → vẫn xử lý luôn (có thể gây starvation!)
// 3. Ưu tiên: nextTick > Promise > queueMicrotask

// ============================================
// 1️⃣ Promise.then/catch/finally - Phổ biến nhất
// ============================================

Promise.resolve().then(() => console.log('⚡ Microtask 1'));
// 📋 Khi resolve → callback vào Microtask Queue
// ✅ Chạy TRƯỚC tất cả setTimeout, setInterval

Promise.reject().catch(() => console.log('⚡ Microtask Error'));
// 📋 Khi reject → catch callback vào Microtask Queue

// 🔗 Promise chaining cũng là microtasks
Promise.resolve()
  .then(() => console.log('⚡ Step 1')) // Microtask 1
  .then(() => console.log('⚡ Step 2')) // Microtask 2 (tạo từ Step 1)
  .then(() => console.log('⚡ Step 3')); // Microtask 3 (tạo từ Step 2)
// 💡 TẤT CẢ đều chạy trong cùng 1 Event Loop cycle!

// ============================================
// 2️⃣ queueMicrotask() - API mới (modern)
// ============================================

queueMicrotask(() => console.log('⚡ Microtask 2'));
// 📋 Đưa callback trực tiếp vào Microtask Queue
// ✅ Nhanh hơn Promise.resolve().then() (ít overhead hơn)
// 💡 Dùng khi cần microtask thuần, không cần Promise

// ============================================
// 3️⃣ MutationObserver - Theo dõi DOM changes
// ============================================

const targetElement = document.querySelector('.target');
const observer = new MutationObserver((mutations) => {
  console.log('⚡ DOM mutated - Microtask 3:', mutations);
  // 📋 Callback này là Microtask!
  // 💡 React/Vue dùng pattern này để batch DOM updates
});

observer.observe(targetElement, {
  childList: true, // 👁️ Theo dõi children thay đổi
  attributes: true, // 👁️ Theo dõi attributes thay đổi
});

// Khi DOM thay đổi → callback vào Microtask Queue
targetElement.innerHTML = 'Changed!'; // 🔄 Trigger MutationObserver

// ============================================
// 4️⃣ process.nextTick() - Node.js ONLY (ƯU TIÊN CAO NHẤT!)
// ============================================

process.nextTick(() => console.log('🚀 NextTick - Microtask 0'));
// 📋 Chạy TRƯỚC TẤT CẢ microtasks khác (even Promise!)
// ⚠️ CHỈ có trong Node.js, KHÔNG có trong Browser!
// 💡 Dùng khi cần đảm bảo code chạy NGAY SAU Call Stack trống

/* 📊 THỨ TỰ ƯU TIÊN (từ cao → thấp):

   1. 🚀 process.nextTick() ← CAO NHẤT (Node.js only)
   2. ⚡ Promise microtasks
   3. ⚡ queueMicrotask()
   4. ⚡ MutationObserver
   5. 🎯 Macrotasks (setTimeout, etc.) ← THẤP NHẤT
*/

// ============================================
// ⚠️ NGUY HIỂM: Microtask Starvation
// ============================================

function dangerousMicrotask() {
  queueMicrotask(() => {
    console.log('⚡ Microtask running...');
    dangerousMicrotask(); // 🔁 Tạo thêm microtask liên tục!
  });
}

// dangerousMicrotask(); // ⚠️ ĐỪNG CHẠY!
// 💀 Kết quả: Microtask Queue không bao giờ trống
// 💀 Macrotasks (setTimeout, UI events) KHÔNG BAO GIỜ chạy!
// 💀 UI đóng băng, app treo!
```

---

**🎯 5. MACROTASK QUEUE (Task Queue / Callback Queue)**

**Khái niệm:**

- Hàng đợi chứa **macrotasks** (priority thấp hơn microtask)
- Event Loop chỉ lấy **MỘT macrotask** mỗi lần
- Sau mỗi macrotask, xử lý ALL microtasks

**Các Macrotasks:**

```typescript
// ============================================
// 🎯 MACROTASK QUEUE - Ưu tiên THẤP hơn Microtask
// ============================================

// 💡 ĐẶC ĐIỂM QUAN TRỌNG:
// 1. Event Loop chỉ lấy MỘT macrotask mỗi lần
// 2. Sau mỗi macrotask → xử lý HẾT TẤT CẢ microtasks
// 3. Browser có thể render UI giữa các macrotasks

// ============================================
// 1️⃣ setTimeout / setInterval - Timers
// ============================================

// ⏰ setTimeout: Chạy 1 LẦN sau delay
setTimeout(() => console.log('🎯 Macrotask 1'), 0);
// 📋 Delay 0ms KHÔNG có nghĩa là chạy ngay!
// ✅ Vẫn phải chờ:
//    - Call Stack trống
//    - TẤT CẢ Microtasks xong
// 💡 Thực tế: minimum ~4ms trong browser (HTML5 spec)

// 🔄 setInterval: Chạy LẶP LẠI mỗi interval
setInterval(() => console.log('🎯 Macrotask 2'), 1000);
// ⚠️ Chú ý: Nếu callback chạy lâu > interval
//          → callbacks có thể chồng chéo!
// 💡 Nên dùng setTimeout recursive thay vì setInterval

// ============================================
// 2️⃣ setImmediate() - Node.js ONLY
// ============================================

setImmediate(() => console.log('🎯 Macrotask 3 - Node.js'));
// 📋 Chạy trong CHECK phase của Node.js Event Loop
// 💡 Trong I/O callbacks: setImmediate chạy TRƯỚC setTimeout!
// ⚠️ CHỈ có trong Node.js, KHÔNG có trong Browser!

// ============================================
// 3️⃣ I/O Operations - File system, Network
// ============================================

const fs = require('fs'); // Node.js

fs.readFile('file.txt', (err, data) => {
  console.log('🎯 File read - Macrotask 4');
  // 📋 Callback vào Macrotask Queue sau khi đọc xong
  // 💡 Không block main thread trong lúc đọc file!
});

// ============================================
// 4️⃣ UI Rendering / requestAnimationFrame - Browser ONLY
// ============================================

requestAnimationFrame(() => console.log('🎯 RAF - Macrotask 5'));
// 📋 Chạy TRƯỚC KHI browser paint frame tiếp theo
// 💡 Tối ưu cho animation: đồng bộ với refresh rate (60fps)
// ✅ Dùng cho animation thay vì setTimeout → mượt hơn!

/* 📊 SỰ KHÁC BIỆT GIỮA CÁC MACROTASKS:

   🔹 setTimeout/setInterval:
      - Chạy trong TIMERS phase (Node.js)
      - Không đồng bộ với screen refresh

   🔹 setImmediate (Node.js):
      - Chạy trong CHECK phase
      - Thường nhanh hơn setTimeout trong I/O callbacks

   🔹 requestAnimationFrame (Browser):
      - Chạy TRƯỚC render
      - Đồng bộ với screen refresh (60fps)
      - Tối ưu cho animation
*/
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
// ============================================
// 🎯 VÍ DỤ KINH ĐIỂN - Phân biệt thứ tự thực thi
// ============================================

// 📢 Bước 1: Code đồng bộ chạy TRƯỚC TIÊN
console.log('1: Sync code start'); // ① Call Stack - chạy ngay lập tức

// 🎯 Đăng ký Macrotasks (thứ tự thấp)
setTimeout(() => console.log('2: Macrotask 1'), 0); // ④ Vào Macrotask Queue
setTimeout(() => console.log('3: Macrotask 2'), 0); // ④ Vào Macrotask Queue
// 💡 Delay 0ms KHÔNG có nghĩa chạy ngay! Vẫn phải chờ Microtasks xong

// ⚡ Đăng ký Microtasks (thứ tự cao)
Promise.resolve()
  .then(() => console.log('4: Microtask 1')) // ② Vào Microtask Queue
  .then(() => console.log('5: Microtask 2')); // ② Chained - cũng vào Microtask Queue
// 💡 .then() chaining tạo thêm microtasks, nhưng vẫn chạy TRONG cùng 1 cycle!

Promise.resolve().then(() => {
  console.log('6: Microtask 3');

  // ⚠️ Tạo thêm microtask BÊN TRONG microtask
  queueMicrotask(() => console.log('7: Microtask 4'));
  // 💡 Microtask này cũng sẽ chạy NGAY trong cùng cycle!
});

// 📢 Bước 2: Code đồng bộ tiếp theo
console.log('8: Sync code end'); // ① Call Stack - chạy ngay lập tức

/* 📊 OUTPUT (theo THỨ TỰ EVENT LOOP):

   🔵 GIAI ĐOẠN 1: THỰC THI CALL STACK (đồng bộ)
   ===============================================
   1: Sync code start          // ➡️ Chạy ngay, in ra đầu tiên
   8: Sync code end            // ➡️ Chạy ngay, in ra thứ 2

   ⚡ GIAI ĐOẠN 2: XỦ LÝ TẤT CẢ MICROTASKS
   ===============================================
   4: Microtask 1              // ➡️ Microtask đầu tiên
   6: Microtask 3              // ➡️ Microtask thứ 2
   7: Microtask 4              // ➡️ Microtask tạo từ bên trong Microtask 3
   5: Microtask 2              // ➡️ Chained .then() từ Microtask 1

   🎯 GIAI ĐOẠN 3: XỦ LÝ MỘT MACROTASK
   ===============================================
   2: Macrotask 1              // ➡️ Lấy 1 macrotask từ queue

   🔄 GIAI ĐOẠN 4: LẶP LẠI - Cycle mới
   ===============================================
   (Kiểm tra Microtasks - trống)
   (Lấy tiếp 1 Macrotask)
   3: Macrotask 2              // ➡️ Chu kỳ Event Loop tiếp theo
*/

/* 📚 GIẢI THÍCH TỬNG BƯỚC CHI TIẾT:

   🔹 Bước 1: Call Stack thực thi code đồng bộ
      - Chạy console.log('1...') → In ra "1: Sync code start"
      - setTimeout đăng ký → callback vào Macrotask Queue
      - Promise.then đăng ký → callback vào Microtask Queue
      - Chạy console.log('8...') → In ra "8: Sync code end"
      - Call Stack TRỐNG! → Event Loop bắt đầu

   🔹 Bước 2: Event Loop kiểm tra Microtask Queue
      - Có Microtasks! → Xử lý HẾT TẤT CẢ:
        • Chạy Microtask 1 → In "4"
        • Chạy Microtask 3 → In "6"
          • Tạo thêm Microtask 4 → Thêm vào queue
        • Chạy Microtask 4 → In "7"
        • Chạy Microtask 2 (chained) → In "5"
      - Microtask Queue TRỐNG! → Tiếp tục

   🔹 Bước 3: Browser có thể render UI (nếu cần)

   🔹 Bước 4: Event Loop kiểm tra Macrotask Queue
      - Có Macrotask! → Lấy MỘT cái:
        • Chạy Macrotask 1 → In "2"
      - Quay lại Bước 2 (kiểm tra Microtasks)

   🔹 Bước 5: Chu kỳ mới - Lặp lại
      - Microtask Queue trống → Skip
      - Lấy tiếp 1 Macrotask → In "3"
*/
```

````

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
````

**🔍 Ví dụ 3: Call Stack với Async/Await**

```typescript
// ============================================
// 🔄 ASYNC/AWAIT - Cách await hoạt động với Event Loop
// ============================================

// 📝 Async function - trả về Promise
async function asyncFunction() {
  console.log('2: Inside async - before await');
  // 📍 Code TRƯỚC await chạy ĐỒNG BỘ (trong Call Stack)

  await Promise.resolve(); // ⚡ await tạo microtask
  // 🔑 await làm 2 việc:
  //    1. Đợi Promise resolve
  //    2. Code phía SAU await → thành Microtask!

  console.log('5: After await (microtask)');
  // 📍 Code SAU await = Microtask (vào Microtask Queue)
}

// 🎬 BẮT ĐẦU EXECUTION
console.log('1: Start'); // ① Đồng bộ - in ngay

asyncFunction(); // ② Gọi async function
// 💡 asyncFunction() chạy ngay đến await, rồi tạm dừng

console.log('3: After calling async'); // ③ Đồng bộ - in ngay

// ⚡ Thêm 1 Microtask khác
Promise.resolve().then(() => console.log('4: Promise.then (microtask)'));

// 🎯 Thêm 1 Macrotask
setTimeout(() => console.log('6: setTimeout (macrotask)'), 0);

/* 📊 OUTPUT THEO THỨ TỰ:
   ===============================================

   🔵 GIAI ĐOẠN 1: CALL STACK (Đồng bộ)
   -----------------------------------------------
   1: Start                        // ① console.log đồng bộ
   2: Inside async - before await  // ② Code TRƯỚC await (đồng bộ)
   3: After calling async          // ③ console.log đồng bộ

   ⚡ GIAI ĐOẠN 2: MICROTASK QUEUE
   -----------------------------------------------
   4: Promise.then (microtask)     // ④ Microtask đăng ký trước
   5: After await (microtask)      // ⑤ Code SAU await (microtask)

   🎯 GIAI ĐOẠN 3: MACROTASK QUEUE
   -----------------------------------------------
   6: setTimeout (macrotask)       // ⑥ Macrotask cuối cùng
*/

/* 📚 GIẢI THÍCH CHI TIẾT:

   🔹 Tại sao "2" in TRƯỚC "3"?
      - asyncFunction() được gọi NGAY trong Call Stack
      - Code TRƯỚC await chạy đồng bộ
      - Gặp await → tạm dừng, tạo Microtask cho code sau await
      - Return về main flow → tiếp tục chạy "3"

   🔹 Tại sao "4" in TRƯỚC "5"?
      - Cả 2 đều là Microtasks
      - "4" đăng ký trước (Promise.resolve().then)
      - "5" đăng ký sau (code sau await)
      - Microtasks chạy theo thứ tự FIFO (First In First Out)

   🔹 Tại sao "6" in SAU CÙNG?
      - setTimeout là Macrotask (priority thấp)
      - Event Loop xử lý HẾT Microtasks trước
      - Sau đó mới lấy 1 Macrotask

   🎯 KEY TAKEAWAY:
      - Code TRƯỚC await = Đồng bộ (Call Stack)
      - Code SAU await = Microtask (Microtask Queue)
      - await Promise.resolve() = tạo Microtask ngay lập tức
*/
```

**🔍 Ví dụ 4: Thực Tế trong Trading App**

```typescript
// ============================================
// 📈 REAL-WORLD: Trading App Optimization
// ============================================
// 🎯 Bài toán: Nhận 100 order updates từ WebSocket cùng lúc
// ❌ Render từng order → 100 DOM updates → LAG!
// ✅ Batch tất cả → 1 DOM update → SMOOTH!

// 📦 Interface định nghĩa cấu trúc order
interface OrderUpdate {
  orderId: string; // 🆔 Mã lệnh: "ORD-001"
  status: 'pending' | 'filled'; // 📊 Trạng thái: chờ/khớp
  price: number; // 💰 Giá khớp
}

class TradingUI {
  // 🗂️ Mảng tạm chứa updates chờ render
  private pendingUpdates: OrderUpdate[] = [];

  // ============================================
  // ❌ CÁCH TỆ: Render từng update riêng lẻ
  // ============================================
  updateOrderBad(order: OrderUpdate) {
    this.renderOrder(order); // 🐌 Render NGAY LẬP TỨC!

    // 💀 VẤN ĐỀ:
    // - Mỗi render = 1 DOM update = 1 reflow/repaint
    // - 100 orders = 100 reflows = BLOCKING UI!
    // - User thấy UI giật lag, scroll không mượt
  }

  // ============================================
  // ✅ CÁCH TỐT: Batch updates với Microtask
  // ============================================
  updateOrderGood(order: OrderUpdate) {
    // ① Thêm order vào pending array (fast!)
    this.pendingUpdates.push(order);
    // 💡 KHÔNG render ngay → chỉ lưu vào array

    // ② Schedule render trong Microtask
    queueMicrotask(() => {
      // 🔍 Check xem còn pending updates không
      if (this.pendingUpdates.length > 0) {
        // 🎨 Render TẤT CẢ updates cùng lúc
        this.renderBatch(this.pendingUpdates);

        // 🧹 Clear pending array
        this.pendingUpdates = [];
      }
    });

    // 🎯 MAGIC:
    // - 100 calls updateOrderGood() → 100 queueMicrotask()
    // - NHƯNG: Microtasks chạy SAU Call Stack trống
    // - → pendingUpdates có 100 items
    // - → Chỉ render 1 LẦN với 100 items!
  }

  // 🐌 Render 1 order (chậm - nhiều DOM ops)
  private renderOrder(order: OrderUpdate) {
    console.log(`🔴 Render single order: ${order.orderId}`);
    // DOM operations:
    // - document.createElement()
    // - element.appendChild()
    // - Trigger reflow/repaint
    // ⏱️ ~5-10ms per render
  }

  // ⚡ Render nhiều orders cùng lúc (nhanh!)
  private renderBatch(orders: OrderUpdate[]) {
    console.log(`🟢 Render ${orders.length} orders in 1 batch`);
    // Batch DOM operations:
    // - DocumentFragment để tạo tất cả elements
    // - 1 appendChild duy nhất
    // - 1 reflow/repaint duy nhất
    // ⏱️ ~10-15ms cho 100 orders!
  }
}

// ============================================
// 🧪 TEST: So sánh performance
// ============================================

const ui = new TradingUI();

// 📡 Giả sử WebSocket nhận 100 updates CÙNG LÚC
for (let i = 0; i < 100; i++) {
  ui.updateOrderGood({
    orderId: `ORD-${i}`,
    status: 'filled',
    price: 100 + i,
  });
}

/* 📊 KẾT QUẢ SO SÁNH:

   ❌ updateOrderBad (render riêng lẻ):
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   🔴 Render single order: ORD-0
   🔴 Render single order: ORD-1
   🔴 Render single order: ORD-2
   ... (100 lần!)

   💀 Performance:
   - 100 DOM updates
   - 100 reflows/repaints
   - ⏱️ ~500-1000ms total
   - 🐌 UI bị LAG, scroll giật
   - ❌ FPS drop xuống 30-40

   ✅ updateOrderGood (batch render):
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   🟢 Render 100 orders in 1 batch

   ⚡ Performance:
   - 1 DOM update duy nhất
   - 1 reflow/repaint duy nhất
   - ⏱️ ~10-15ms total (NHANH GẤP 50 LẦN!)
   - 🎯 UI mượt mà, scroll buttery smooth
   - ✅ FPS stable 60

   🎯 TIMELINE:
   ───────────────────────────────────────
   0ms:  Call 100x updateOrderGood()
         → Thêm 100 items vào pendingUpdates
         → Đăng ký 100 microtasks (nhưng chỉ 1 chạy!)

   1ms:  Call Stack trống
         → Event Loop kiểm tra Microtask Queue
         → Chạy microtask → renderBatch(100 items)

   11ms: Render xong 100 items
         → UI update mượt mà
         → User vẫn scroll được!
*/

/* 💡 TẠI SAO LẠI HOẠT ĐỘNG?

   🔹 Key Insight:
      - queueMicrotask() chỉ ĐĂNG KÝ callback
      - Callback chưa chạy ngay
      - Chạy khi Call Stack TRỐNG

   🔹 Flow:
      1. Loop 100 lần: updateOrderGood()
         → 100 items vào pendingUpdates
         → 100 queueMicrotask() (nhưng chưa chạy!)

      2. Call Stack trống
         → Event Loop: "Aha! Có Microtasks!"
         → Chạy microtask đầu tiên
         → pendingUpdates.length = 100
         → renderBatch(100 items)
         → Clear pendingUpdates

      3. Microtasks còn lại chạy
         → pendingUpdates.length = 0
         → Skip render (đã render rồi!)

   🎯 Best Practice:
      - Dùng Microtask để BATCH operations
      - React, Vue dùng pattern này cho state updates
      - Giảm DOM operations → tăng performance
*/
```

**Best Practices:**

```typescript
// ============================================
// ✅ BEST PRACTICE 1: Microtask cho Batch Operations
// ============================================

class StateManager {
  // 🗂️ Set để tránh duplicate callbacks
  private updates: Set<() => void> = new Set();
  // 🚦 Flag check xem đã schedule chưa
  private scheduled = false;

  scheduleUpdate(callback: () => void) {
    // ① Thêm callback vào Set (auto dedupe)
    this.updates.add(callback);
    // 💡 Set tự động loại bỏ duplicate

    // ② Chỉ schedule 1 lần duy nhất
    if (!this.scheduled) {
      this.scheduled = true;

      // ③ Dùng queueMicrotask để batch
      queueMicrotask(() => {
        // ④ Chạy TẤT CẢ callbacks
        this.updates.forEach((cb) => cb());

        // ⑤ Reset state
        this.updates.clear();
        this.scheduled = false;
      });
    }

    // 🎯 KẾT QUẢ:
    // - Gọi 100 lần scheduleUpdate() → chỉ 1 microtask
    // - Tất cả callbacks chạy cùng lúc trong 1 batch
  }
}

// ============================================
// ✅ BEST PRACTICE 2: Macrotask cho Defer Work
// ============================================

// 💡 Dùng setTimeout để CHO PHÉP UI render
function deferExpensiveWork(work: () => void) {
  setTimeout(work, 0); // Chạy SAU khi UI render

  // 🔹 Lý do:
  // - setTimeout = Macrotask
  // - Browser render GIỮA các Macrotasks
  // - → UI có cơ hội update trước khi chạy work
}

// 🎯 Use case: Heavy calculation không urgent
function processLargeDataset(data: any[]) {
  console.log('🟢 Start processing...');

  // 💡 Defer heavy work để UI không freeze
  deferExpensiveWork(() => {
    // Heavy calculation here
    const result = data.map((item) => complexCalculation(item));
    console.log('✅ Done!', result.length);
  });

  console.log('🟢 UI vẫn responsive!');
}

// ============================================
// ❌ BAD PRACTICE: Vô hạn Microtasks (Starvation)
// ============================================

function badInfiniteMicrotask() {
  Promise.resolve().then(() => badInfiniteMicrotask());
  // 💀 CHẶN Macrotasks!

  // 🐎 VẤN ĐỀ:
  // - Tạo microtask mới vô hạn
  // - Microtask Queue không bao giờ trống
  // - Event Loop KHÔNG BAO GIỞ chuyển sang Macrotask
  // - → setTimeout, UI events, rendering BỊ CHẶN!
  // - → UI FREEZE hoàn toàn!
}

// ============================================
// ✅ GOOD PRACTICE: Break vòng lặp với Macrotask
// ============================================

function goodDeferWork(count: number) {
  if (count > 0) {
    // 💡 Dùng setTimeout thay vì Promise
    setTimeout(() => goodDeferWork(count - 1), 0);

    // 🎯 Lợi ích:
    // - Mỗi iteration = 1 Macrotask riêng
    // - Browser render GIỮA các iterations
    // - UI vẫn responsive!
    // - User vẫn scroll/click được!
  }
}

// ============================================
// ✅ BEST PRACTICE 3: Hiểu thứ tự execution
// ============================================

async function debugEventLoop() {
  // ① Sync code - chạy NGAY
  console.log('1: Sync');

  // ② Đăng ký Microtask
  queueMicrotask(() => console.log('3: Microtask'));

  // ③ Await = tạo Microtask cho code sau
  await Promise.resolve();
  console.log('4: After await (microtask)');

  // ④ Đăng ký Macrotask
  setTimeout(() => console.log('5: Macrotask'), 0);

  // ⑤ Sync code tiếp - chạy NGAY
  console.log('2: Sync end');

  /* 📊 OUTPUT:
     1: Sync              ← ① Đồng bộ
     2: Sync end          ← ⑤ Đồng bộ
     3: Microtask         ← ② Microtask (đăng ký trước)
     4: After await       ← ③ Microtask (await)
     5: Macrotask         ← ④ Macrotask (cuối cùng)
  */
}

// ============================================
// 📚 KEY TAKEAWAYS
// ============================================

/*
  ✅ KHI NÀO DÙNG MICROTASK?
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. State updates (React setState batching)
  2. Batch DOM operations (FastDOM pattern)
  3. Promise chains (data transformation)
  4. Việc CẦN xử lý NGAY trong cùng 1 tick

  🎯 KHI NÀO DÙNG MACROTASK?
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Defer work (không urgent)
  2. Animations (requestAnimationFrame)
  3. Break heavy work thành chunks
  4. Việc CẦN cho UI render giữa các tasks

  ⚠️ CẢNH BÁO:
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1. KHÔNG tạo vô hạn Microtasks
  2. Luôn có điều kiện dừng
  3. Monitor performance (DevTools)
  4. Hiểu thứ tự: Call Stack → Microtasks → Render → Macrotask
*/
```

**📋 Tóm tắt Best Practices:**

1. **Microtask (`Promise`, `queueMicrotask`)**: Dùng cho state updates, batch operations cần xử lý ngay
2. **Macrotask (`setTimeout`)**: Dùng cho defer work, animations, cho phép UI render giữa các tasks
3. **Tránh Microtask Starvation**: Không tạo vô hạn microtasks, phải có điều kiện dừng
4. **Async/await**: Hiểu rằng code sau `await` là microtask
5. **Debugging**: Luôn nhớ thứ tự: `Call Stack → All Microtasks → Render → One Macrotask`

**Common Mistakes:**

```typescript
// ============================================
// ❌ LỖI 1: Nghĩ setTimeout(fn, 0) chạy NGAY LẬP TỨC
// ============================================

console.log('1'); // ① Đồng bộ - in NGAY

setTimeout(() => console.log('2'), 0); // ② Macrotask - chờ
// 💡 Delay 0ms KHÔNG CÓ NGHĨA là chạy ngay!
// 🐎 Vẫn là Macrotask → vào Macrotask Queue

console.log('3'); // ③ Đồng bộ - in NGAY

// OUTPUT: 1, 3, 2 (KHÔNG PHẢI 1, 2, 3!)
// ⚠️ LÝ do: setTimeout là Macrotask, chạy SAU tất cả code đồng bộ!

/* 📚 GIẢI THÍCH CHI TIẾT:

   🔹 Thứ tự thực thi:
      0ms:  console.log('1')        ← Call Stack
      0ms:  setTimeout(...)         ← Đăng ký Macrotask (chưa chạy!)
      0ms:  console.log('3')        ← Call Stack
      1ms:  Call Stack trống      ← Check Microtask Queue (empty)
      1ms:  console.log('2')        ← Chạy Macrotask

   🎯 Lưu ý:
      - setTimeout(fn, 0) ≠ chạy ngay
      - Nó vẫn phải ĐỢI:
        1. Call Stack trống
        2. Microtask Queue trống
        3. Sau đó mới đến lượt
*/

// ============================================
// ❌ LỖI 2: Quên Promise.then là Microtask
// ============================================

setTimeout(() => console.log('1: Macro'), 0); // Macrotask
// 🎯 Macrotask Queue: [console.log('1: Macro')]

Promise.resolve().then(() => console.log('2: Micro')); // Microtask
// ⚡ Microtask Queue: [console.log('2: Micro')]

// OUTPUT: 2, 1 (microtask chạy TRƯỚC macrotask!)

/* 📊 TIMELINE:
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   0ms:  Đăng ký setTimeout  → Macrotask Queue
   0ms:  Đăng ký Promise.then  → Microtask Queue

   1ms:  Call Stack trống
   1ms:  Event Loop check:
         ① Microtask Queue có gì? → console.log('2: Micro')
         ② Microtask Queue trống chưa? → Rồi
         ③ Lấy 1 Macrotask → console.log('1: Macro')

   🎯 QUY TẮC VÀNG:
      - Microtasks LUÔN chạy trước Macrotasks
      - Dù Macrotask đăng ký trước!
*/

// ============================================
// ❌ LỖI 3: Blocking Event Loop với Heavy Work
// ============================================

function heavyCalculation() {
  const start = Date.now();

  // 💀 Vòng lặp block 5 giây!
  while (Date.now() - start < 5000) {
    // 🐎 Không làm gì, chỉ chờ thời gian trôi
  }

  console.log('Done');
}

heavyCalculation(); // 💀 UI đóng băng 5 GIÂY!

/* 🐎 VẤN ĐỀ:
   - Vòng while chạy ĐỒNG BỘ trong Call Stack
   - Call Stack KHÔNG BAO GIỞ trống trong 5 giây
   - Event Loop KHÔNG thể chạy Microtasks/Macrotasks
   - Browser KHÔNG thể render UI
   - → User không scroll/click được!
   - → UI FREEZE hoàn toàn!
*/

// ✅ FIX: Break thành chunks với setTimeout
function heavyCalculationFixed(iterations: number, callback: () => void) {
  const chunkSize = 100; // ① Xử lý 100 items mỗi lần
  let current = 0;

  function processChunk() {
    // ② Tính end cho chunk hiện tại
    const end = Math.min(current + chunkSize, iterations);

    // ③ Xử lý chunk
    for (let i = current; i < end; i++) {
      // Do heavy work here
      // 💡 Chỉ 100 iterations → ~16ms → OK!
    }

    current = end;

    // ④ Còn work chưa?
    if (current < iterations) {
      // 💡 Dùng setTimeout để cho UI render
      setTimeout(processChunk, 0); // ← Macrotask cho chunk tiếp theo
      // 🎯 UI có cơ hội render GIỮA các chunks!
    } else {
      // ⑤ Xong hết!
      callback();
    }
  }

  processChunk();
}

/* ✅ LỢI ÍCH:
   - Mỗi chunk = 1 Macrotask riêng
   - Browser render GIỮA các Macrotasks
   - UI vẫn responsive!
   - Progress bar có thể update!
*/

// ============================================
// ❌ LỖI 4: Microtask Starvation
// ============================================

let count = 0;

function addMicrotask() {
  if (count++ < 1000000) {
    // 💀 Tạo Microtask mới vô hạn!
    Promise.resolve().then(addMicrotask);
  }
}

addMicrotask(); // 💀 Macrotasks bị CHẶN!

/* 🐎 VẤN ĐỀ:

   🔹 Flow:
      1. addMicrotask() tạo Promise → Microtask Queue
      2. Microtask chạy → gọi addMicrotask() lại
      3. Lại tạo Microtask mới
      4. Lặp lại 1,000,000 lần!

   💀 Hậu quả:
      - Microtask Queue KHÔNG BAO GIỞ trống
      - Event Loop KHÔNG BAO GIỞ chuyển sang Macrotask
      - setTimeout, UI events, rendering BỊ CHẶN!
      - UI FREEZE!
*/

// ✅ FIX: Giới hạn hoặc dùng Macrotask
function addMicrotaskFixed() {
  if (count++ < 1000000) {
    // 💡 Dùng setTimeout thay vì Promise
    setTimeout(() => addMicrotaskFixed(), 0);

    // 🎯 Lợi ích:
    // - Mỗi iteration = 1 Macrotask
    // - Browser render GIỮA các Macrotasks
    // - Macrotasks khác (UI events) vẫn chạy được
  }
}

// ============================================
// 📚 TÓM TẮT CÁC LỐI THƯỜNG GẶP
// ============================================

/*
  ❌ LỐI 1: setTimeout(fn, 0) ≠ chạy ngay
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  - Nó là Macrotask, chạy sau:
    1. Tất cả code đồng bộ
    2. Tất cả Microtasks
    3. Browser rendering (nếu có)

  ❌ LỐI 2: Promise.then chạy TRƯỚC setTimeout
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  - Microtask LUÔN priority cao hơn Macrotask
  - Event Loop xử lý HẾT Microtasks trước

  ❌ LỐI 3: Blocking code làm đóng băng UI
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  - Phải break heavy work thành chunks
  - Dùng setTimeout giữa các chunks
  - Cho phép UI render

  ❌ LỐI 4: Microtask starvation
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  - KHÔNG tạo vô hạn Microtasks
  - Luôn có điều kiện dừng
  - Hoặc dùng Macrotask (setTimeout) cho recursion
*/
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
// 🎯 Bài toán: Làm sao để animation mượt 60fps?
// ❌ setTimeout: Không đồng bộ với frame → janky
// ✅ RAF: Chạy ĐÚNG TRƯỚC khi browser paint → smooth

console.log('1: Start'); // ① Đồng bộ

// ============================================
// ❌ setTimeout: KHÔNG đồng bộ với refresh rate
// ============================================
setTimeout(() => {
  console.log('4: setTimeout - có thể chạy GIỮA frame → janky animation');
  document.body.style.transform = 'translateX(100px)';
  // 🐎 VẤN ĐỀ:
  // - setTimeout chạy không đúng lúc browser paint
  // - Có thể chạy SAU khi paint → wasted work
  // - Có thể skip frame → animation giật
}, 16); // ~16ms ≈ 1 frame (60fps), nhưng không chính xác!

// ============================================
// ✅ RAF: Đồng bộ với browser refresh rate
// ============================================
requestAnimationFrame(() => {
  console.log('3: RAF - chạy NGAY TRƯỚC khi paint → smooth animation');
  document.body.style.transform = 'translateX(100px)';
  // 🎯 Lợi ích:
  // - Browser gọi RAF callbacks NGAY TRƯỚC khi paint
  // - Đảm bảo DOM changes được paint trong frame hiện tại
  // - Không wasted work, không skip frames
  // - → Animation mượt 60fps!
});

console.log('2: Sync end'); // ② Đồng bộ

/* 📊 OUTPUT TIMELINE:
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   0ms    → "1: Start"                  (Đồng bộ)
   0ms    → "2: Sync end"                (Đồng bộ)

   ~16ms  → "3: RAF"                    (CHẠY TRƯỚC PAINT)
   ~16ms  → Browser paint frame         (🎨 RENDER)
   ~16ms  → "4: setTimeout"             (Chạy SAU paint → wasted!)

   🎯 KEY INSIGHT:
      - RAF chạy trong Render Phase (giữa Microtask và Macrotask)
      - Browser tự động schedule RAF callbacks trước paint
      - → DOM changes được apply NGAY trong frame hiện tại
*/

// ===================================================
// 🎨 SMOOTH ANIMATION với RAF
// ===================================================

class SmoothAnimation {
  private startTime: number | null = null;
  private duration = 1000; // ⏱️ 1 giây

  animate(element: HTMLElement) {
    // 🔄 Recursive RAF pattern
    const step = (timestamp: number) => {
      // ① Khởi tạo startTime (chỉ 1 lần)
      if (!this.startTime) this.startTime = timestamp;
      // 💡 timestamp = thời gian hiện tại (DOMHighResTimeStamp)

      // ② Tính progress (0 → 1)
      const elapsed = timestamp - this.startTime; // Thời gian đã trôi
      const progress = Math.min(elapsed / this.duration, 1); // 0-1
      // 💡 Clamp ở 1 khi đạt duration

      // ③ Apply easing function (smooth curve)
      const eased = this.easeOutCubic(progress);
      // 🎯 easeOutCubic: Bắt đầu nhanh, cuối chậm lại

      // ④ Update DOM
      element.style.transform = `translateX(${eased * 500}px)`;
      // 🎯 Đi từ 0px → 500px mượt mà

      // ⑤ Continue nếu chưa xong
      if (progress < 1) {
        requestAnimationFrame(step); // 🔄 Recursive call
        // 💡 Browser tự động gọi step() mỗi frame
      }
    };

    // 🚀 Start animation
    requestAnimationFrame(step);
  }

  // 📊 Easing function: y = 1 - (1-x)^3
  private easeOutCubic(t: number): number {
    return 1 - Math.pow(1 - t, 3);
    // 🎯 Bắt đầu nhanh (curve dốc), cuối chậm (curve thoải)
  }
}

// 🎬 Usage
const animator = new SmoothAnimation();
animator.animate(document.getElementById('box')!);

/* 📊 TIMELINE (60fps):
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━
   0ms:    step(0)      → progress=0   → x=0px
   16ms:   step(16)     → progress=0.016 → x=8px
   32ms:   step(32)     → progress=0.032 → x=16px
   ...
   1000ms: step(1000)   → progress=1   → x=500px

   🎯 Kết quả: Animation chạy mượt 60fps!
*/

// ===================================================
// ⚡ RAF + BATCH DOM READS/WRITES (FastDOM pattern)
// ===================================================

class FastDOM {
  // 📏 Các callback đọc DOM (measure)
  private reads: Array<() => void> = [];
  // ✏️ Các callback ghi DOM (mutate)
  private writes: Array<() => void> = [];
  // 🚦 Flag check đã schedule chưa
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
    if (this.scheduled) return; // Đã schedule rồi
    this.scheduled = true;

    // 🎯 Dùng RAF để batch operations
    requestAnimationFrame(() => {
      // ① Execute ALL reads first (prevent layout thrashing)
      this.reads.forEach((fn) => fn());
      this.reads = [];
      // 💡 Đọc HẾT trước → chỉ 1 layout calculation!

      // ② Then execute ALL writes
      this.writes.forEach((fn) => fn());
      this.writes = [];
      // 💡 Ghi HẾT sau → chỉ 1 layout invalidation!

      this.scheduled = false;
    });
  }
}

// 🎬 Usage - Tránh layout thrashing
const fastdom = new FastDOM();
const element = document.getElementById('box')!;

// ============================================
// ❌ BAD: Interleaved read/write → layout thrashing
// ============================================
for (let i = 0; i < 100; i++) {
  const height = element.offsetHeight; // 📏 READ → force layout
  element.style.height = height + 10 + 'px'; // ✏️ WRITE → invalidate layout
  // 💀 VẤN ĐỀ:
  // - Mỗi READ sau WRITE → browser phải recalculate layout
  // - 100 iterations = 100 layouts!
  // - ⏱️ ~500-1000ms (CHẬM!)
} // 100 layouts! 🐌

// ============================================
// ✅ GOOD: Batch reads, then writes
// ============================================
for (let i = 0; i < 100; i++) {
  // 📏 Schedule READ
  fastdom.measure(() => {
    const height = element.offsetHeight; // READ

    // ✏️ Schedule WRITE
    fastdom.mutate(() => {
      element.style.height = height + 10 + 'px'; // WRITE
    });
  });
}

/* 🎯 MAGIC:
   ━━━━━━━━━━━━━━━━━━━━━━━━━
   RAF callback chạy:
   1. Execute 100 reads  → 1 layout calculation
   2. Execute 100 writes → 1 layout invalidation

   🎯 Kết quả: 1 layout only! ⚡
   ⏱️ ~10-20ms (NHANH GẤP 50 LẦN!)
*/
```

---

### **9. requestIdleCallback - Low Priority Work**

**🔍 Khi nào dùng requestIdleCallback:**

```typescript
// ===================================================
// 🕐 requestIdleCallback - DEFERRED WORK
// ===================================================
// 🎯 Muc đích: Chạy low-priority work khi browser RẢNH
// ⚠️ KHÔNG block main thread, UI rendering, high-priority tasks

// 📋 Interface của IdleDeadline
interface IdleDeadline {
  didTimeout: boolean; // 🕑 Có timeout không?
  timeRemaining(): number; // ⏱️ ms còn lại trong frame
  // 💡 Browser có ~16ms/frame (60fps)
  // 💡 Nếu main work < 16ms → còn idle time
}

// ============================================
// ✅ USE CASE 1: Analytics tracking (không urgent)
// ============================================

const analyticsQueue: any[] = [];

function sendAnalytics(event: any) {
  // Gửi event đến analytics server
  console.log('📡 Sending analytics:', event);
}

requestIdleCallback((deadline: IdleDeadline) => {
  // 🔄 Xử lý KHI còn thời gian VÀ còn events
  while (deadline.timeRemaining() > 0 && analyticsQueue.length > 0) {
    const event = analyticsQueue.shift();
    sendAnalytics(event);
    // 💡 Chỉ xử lý khi browser rảnh → không làm chậm UI
  }

  // ⚠️ Nếu còn events, schedule lại
  if (analyticsQueue.length > 0) {
    requestIdleCallback(processAnalytics); // 🔄 Recursive
    // 💡 Tiếp tục xử lý khi browser rảnh lần sau
  }
});

/* 🎯 TIMELINE:
   ━━━━━━━━━━━━━━━━━━━━━━━━━
   Frame 1 (16ms budget):
   0-10ms:  Main work (UI updates, animations)
   10-16ms: IDLE TIME (6ms) → idleCallback chạy!
            → Gửi 3-5 analytics events

   Frame 2 (16ms budget):
   0-15ms:  Heavy main work (user scrolling)
   15-16ms: IDLE TIME (1ms) → idleCallback chạy ngắn
            → Gửi 1 event

   Frame 3 (16ms budget):
   0-16ms:  Full main work (no idle time)
            → idleCallback KHÔNG chạy!
            → Chờ frame sau
*/

// ============================================
// ✅ USE CASE 2: PRELOAD IMAGES khi browser rảnh
// ============================================

const imagesToPreload = [
  '/img1.jpg',
  '/img2.jpg',
  '/img3.jpg',
  // ... 100 images
];

function preloadImages(deadline: IdleDeadline) {
  // 🔄 Xử lý trong khi còn thời gian VÀ còn images
  while (
    deadline.timeRemaining() > 0 && // 📍 Còn thời gian
    imagesToPreload.length > 0 // 📍 Còn images
  ) {
    // 🎯 Preload 1 image
    const img = new Image();
    img.src = imagesToPreload.shift()!;
    // 💡 Browser download image trong background
  }

  // ⚠️ Continue nếu còn images
  if (imagesToPreload.length > 0) {
    requestIdleCallback(preloadImages); // 🔄 Recursive
  }
}

// 🚀 Bắt đầu preload với timeout fallback
requestIdleCallback(preloadImages, { timeout: 2000 });
// 💡 timeout: Force chạy sau 2s nếu không rảnh
// 🎯 Đảm bảo images cuối cùng vẫn được load

/* 📊 BENEFITS:
   ✅ Images preload trong background
   ✅ Không block UI (scroll, click vẫn smooth)
   ✅ Tận dụng idle time (không lãng phí CPU)
   ✅ Timeout fallback đảm bảo complete
*/

// ============================================
// ✅ USE CASE 3: CLEANUP old cache entries
// ============================================

class CacheCleanup {
  // 🗂️ Cache entries với timestamp
  private cacheEntries = new Map<string, { data: any; timestamp: number }>();

  scheduleCleanup() {
    requestIdleCallback((deadline) => {
      const now = Date.now();
      const maxAge = 1000 * 60 * 60; // ⏱️ 1 hour

      // 🔄 Iterate qua cache entries
      for (const [key, entry] of this.cacheEntries) {
        // ⚠️ Kiệm tra còn thời gian không
        if (deadline.timeRemaining() < 1) {
          // 🕑 Hết thời gian → Reschedule
          this.scheduleCleanup();
          return;
          // 💡 Chờ frame sau tiếp tục
        }

        // 🧹 Xóa entries cũ (> 1 hour)
        if (now - entry.timestamp > maxAge) {
          this.cacheEntries.delete(key);
          console.log(`🧹 Cleaned cache: ${key}`);
        }
      }
    });
  }
}

// 🎬 Usage
const cacheManager = new CacheCleanup();
cacheManager.scheduleCleanup();
// 💡 Cleanup chạy khi browser rảnh, không ảnh hưởng user experience

// ============================================
// 📚 KEY CONCEPTS
// ============================================

/*
  🎯 KHI NÀO DÙNG requestIdleCallback?
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✅ Analytics tracking
  ✅ Logging, telemetry
  ✅ Preload resources (images, data)
  ✅ Cache cleanup
  ✅ Background data sync
  ✅ Non-critical DOM updates

  ❌ KHI NÀO KHÔNG DÙNG?
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ❌ Critical user-facing updates
  ❌ Animations (dùng RAF)
  ❌ Immediate response to user input
  ❌ Time-sensitive operations

  💡 SO SÁNH:
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  - Microtask:            Priority CAO NHẤT, chạy NGAY
  - RAF:                  Chạy TRƯỚC render (animations)
  - Macrotask:            Chạy SAU render (defer work)
  - requestIdleCallback:  Chạy khi browser RẢNH (lowest priority)

  ⚠️ LƯU Ý:
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  - Có thể KHÔNG chạy nếu browser luôn bận
  - Dùng timeout để đảm bảo complete
  - Check timeRemaining() trong loop
  - Reschedule nếu chưa xong
*/
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

# 💬 Q07: Event Loop - Giải Thích Theo Cách Nói Chuyện Đời Thường

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"Event Loop là cơ chế JavaScript xử lý async code trong môi trường single-threaded bằng cách liên tục kiểm tra Call Stack và Task Queues."**

**🔑 Ẩn Dụ Quán Cà Phê (dễ nhớ cho phỏng vấn):**

**"Như 1 người phục vụ (JS Engine single-thread) làm việc tại quầy (Call Stack). Khi có việc lâu (async), giao cho máy tự động (Web APIs) rồi ghi tên vào sổ chờ. Liên tục check: ① Quầy trống chưa? ② Có khách VIP chưa? (Microtasks) → Phục vụ hết VIP trước. ③ Có khách thường chưa? (Macrotasks) → Phục vụ 1 người. ④ Lặp lại."**

**🔑 3 Thành Phần Chính:**

**1. Call Stack (Quầy pha chế):**

- Xử lý **đồng bộ**, từng task một
- Empty → Event Loop mới chạy
- Stack overflow khi recursive không có base case

**2. Task Queues:**

- **Microtask Queue** (VIP): Promise `.then()`, `queueMicrotask()`, MutationObserver
  - **Chạy hết tất cả** trước khi sang Macrotask
- **Macrotask Queue** (thường): `setTimeout`, `setInterval`, I/O, UI rendering
  - **Chạy 1 task** rồi check Microtask lại

**3. Event Loop:**

- **Vòng lặp vô hạn** kiểm tra: Call Stack empty → Microtasks → 1 Macrotask → repeat
- Đảm bảo UI không bị block (rendering giữa các macrotasks)

**⚠️ Lỗi Thường Gặp:**

- Nghĩ `setTimeout(fn, 0)` chạy ngay → Sai! Vẫn phải chờ Call Stack empty + Microtasks xong
- Không hiểu Microtask **chạy hết tất cả** → Promise chains dài có thể block UI
- Dùng `setInterval` mà không clear → Memory leak + tasks chồng chéo

**💡 Kiến Thức Senior:**

- **Starvation**: Microtask queue dài vô hạn (recursive Promise) → Macrotasks không bao giờ chạy → UI freeze
- **Rendering timing**: Browser render giữa macrotasks (60fps = ~16ms/task), nếu task > 16ms → jank
- `requestAnimationFrame` chạy **trước render**, `setTimeout` chạy sau → dùng rAF cho animation mượt
- Node.js có **6 phases** trong Event Loop (timers, I/O, poll, check, close) khác Browser (chỉ có Micro + Macro)

**🎯 Mục Đích:**

Giải thích Event Loop theo cách dễ hiểu nhất, KHÔNG dùng thuật ngữ technical, giống như đang kể chuyện cho người không biết lập trình.

**📖 Câu Chuyện: Quán Cà Phê và Người Phục Vụ**

Tưởng tượng bạn mở một quán cà phê nhỏ:

**🏪 SETUP BAN ĐẦU:**

- **Bạn** = JavaScript Engine (chỉ có 1 người, làm single-threaded)
- **Quầy pha chế** = Call Stack (chỉ làm được 1 việc tại 1 thời điểm)
- **Danh sách chờ VIP** = Microtask Queue (ưu tiên cao - khách quen, khách VIP)
- **Danh sách chờ thường** = Macrotask Queue (ưu tiên thấp hơn - khách mới)
- **Bạn kiểm tra** = Event Loop (liên tục check xem có việc gì cần làm không)

---

**📋 QUY TRÌNH LÀM VIỆC:**

**Buổi sáng, quán mới mở cửa:**

1. **Khách A vào** → gọi "Cà phê đen nóng" (code đồng bộ)

   - Bạn: "OK, pha ngay!"
   - → Bạn pha xong, đưa cho khách A
   - → Khách A nhận và đi

2. **Khách B vào** → gọi "Cà phê phin" (setTimeout - mất 5 phút)

   - Bạn: "OK, cà phê phin phải đợi 5 phút nhé"
   - → Bạn để máy pha tự động (Web API)
   - → Ghi tên Khách B vào **Danh sách chờ thường**
   - → **KHÔNG đứng đợi**, làm việc khác tiếp

3. **Khách C vào** → gọi "Nước cam vắt" (code đồng bộ)

   - Bạn: "OK, vắt ngay!"
   - → Bạn vắt xong, đưa cho khách C
   - → Khách C nhận và đi

4. **Khách D vào** → gọi "Bánh mì" và hứa sẽ tip (Promise - Microtask)

   - Bạn: "OK, khách tip thì ưu tiên cao!"
   - → Ghi tên Khách D vào **Danh sách chờ VIP**
   - → Làm việc khác tiếp

5. **Khách E vào** → gọi "Trà đá" (code đồng bộ)
   - Bạn: "OK, pha ngay!"
   - → Bạn pha xong, đưa cho khách E

---

**⏰ SAU ĐÓ (Event Loop bắt đầu hoạt động):**

Bạn check xem:

**① Quầy pha chế có trống không?**

- ✅ Trống rồi (Call Stack empty)

**② Có khách VIP chờ không? (Microtask Queue)**

- ✅ Có! Khách D (bánh mì - khách tip)
- → Bạn phục vụ Khách D trước (Priority cao!)
- → Khách D nhận bánh mì, đi

**③ Vẫn còn khách VIP nữa không?**

- ❌ Không (Microtask Queue empty)

**④ Có khách thường chờ không? (Macrotask Queue)**

- ✅ Có! Khách B (cà phê phin đã pha xong sau 5 phút)
- → Bạn đưa cho Khách B
- → Khách B nhận, đi

**⑤ Quay lại bước ①** (lặp lại mãi - Event Loop)

---

**🎬 VÍ DỤ CỤ THỂ VỚI CODE:**

```javascript
// Khách A: Code đồng bộ
console.log('👤 Khách A: Cà phê đen nóng');
// → Bạn: Pha ngay! ☕ (thực hiện ngay lập tức)

// Khách B: setTimeout (Macrotask - chờ 0ms nhưng vào hàng chờ thường)
setTimeout(() => {
  console.log('👤 Khách B: Cà phê phin (đã chờ)');
}, 0);
// → Bạn: Ghi vào danh sách chờ thường 📋

// Khách C: Code đồng bộ
console.log('👤 Khách C: Nước cam vắt');
// → Bạn: Vắt ngay! 🍊

// Khách D: Promise (Microtask - khách VIP)
Promise.resolve().then(() => {
  console.log('👤 Khách D: Bánh mì (khách tip - VIP)');
});
// → Bạn: Ghi vào danh sách VIP ⭐

// Khách E: Code đồng bộ
console.log('👤 Khách E: Trà đá');
// → Bạn: Pha ngay! 🍵

// ===== KẾT QUẢ OUTPUT =====
// 👤 Khách A: Cà phê đen nóng     ← Đồng bộ (ngay lập tức)
// 👤 Khách C: Nước cam vắt         ← Đồng bộ (ngay lập tức)
// 👤 Khách E: Trà đá               ← Đồng bộ (ngay lập tức)
// 👤 Khách D: Bánh mì (VIP)        ← Microtask (ưu tiên cao)
// 👤 Khách B: Cà phê phin          ← Macrotask (ưu tiên thấp)
```

---

**🤔 TẠI SAO LẠI NHƯ VẬY?**

**Câu hỏi 1:** Tại sao Khách B (setTimeout 0ms) không được phục vụ ngay?

- **Trả lời:** Vì Khách B vào **Danh sách chờ thường** (Macrotask). Dù chờ 0ms, nhưng phải đợi hết việc đang làm + khách VIP mới đến lượt.

**Câu hỏi 2:** Tại sao Khách D (Promise) được phục vụ trước Khách B?

- **Trả lời:** Vì Khách D là **Khách VIP** (Microtask), có ưu tiên cao hơn Khách thường (Macrotask).

**Câu hỏi 3:** Nếu có 100 khách VIP liên tục, khách thường có được phục vụ không?

- **Trả lời:** KHÔNG! Đây gọi là **"Microtask Starvation"** (Đói khách thường). Bạn cứ phục vụ khách VIP mãi, khách thường chờ mãi không tới lượt.

---

**🍕 VÍ DỤ THỰC TẾ: ĐẶT PIZZA**

```javascript
console.log('🏠 Tôi đang ở nhà');

// Đặt pizza (setTimeout - Macrotask)
setTimeout(() => {
  console.log('🍕 Pizza giao đến, tôi mở cửa nhận');
}, 3000); // 3 giây sau

console.log('📺 Tôi xem TV trong lúc đợi');

// Hứa với bản thân (Promise - Microtask)
Promise.resolve().then(() => {
  console.log('💭 Nhắc bản thân: Nhớ lấy tiền tip cho shipper');
});

console.log('🍿 Tôi ăn bỏng ngô');

// ===== OUTPUT =====
// 🏠 Tôi đang ở nhà                      ← Ngay lập tức
// 📺 Tôi xem TV trong lúc đợi            ← Ngay lập tức
// 🍿 Tôi ăn bỏng ngô                     ← Ngay lập tức
// 💭 Nhắc bản thân: Nhớ lấy tiền tip     ← Microtask (ưu tiên cao)
// (chờ 3 giây...)
// 🍕 Pizza giao đến, tôi mở cửa nhận     ← Macrotask (sau cùng)
```

**Giải thích:**

1. Bạn làm hết việc đang làm (xem TV, ăn bỏng ngô)
2. Nhớ lấy tiền tip (Microtask - việc quan trọng)
3. Cuối cùng mới nhận pizza (Macrotask - đã hẹn trước 3 giây)

---

**🚗 VÍ DỤ: ĐI SIÊU THỊ**

```javascript
console.log('🚗 Tôi lái xe đến siêu thị');

// Đặt hẹn giờ báo thức xe (setTimeout)
setTimeout(() => {
  console.log('⏰ Báo thức: Đã 1 giờ, về nhà thôi!');
}, 3600000); // 1 giờ

console.log('🛒 Tôi lấy giỏ và đi mua sắm');

// Nhớ việc quan trọng (Promise)
Promise.resolve().then(() => {
  console.log('💡 Ồ nhớ rồi! Phải mua sữa cho con');
});

console.log('🥬 Tôi mua rau củ');

// ===== OUTPUT =====
// 🚗 Tôi lái xe đến siêu thị             ← Ngay lập tức
// 🛒 Tôi lấy giỏ và đi mua sắm           ← Ngay lập tức
// 🥬 Tôi mua rau củ                      ← Ngay lập tức
// 💡 Ồ nhớ rồi! Phải mua sữa cho con     ← Microtask (nhớ ngay)
// (chờ 1 giờ...)
// ⏰ Báo thức: Đã 1 giờ, về nhà thôi!    ← Macrotask (hẹn giờ)
```

---

**⚠️ TÌNH HUỐNG XẤU: KHÁCH VIP VÔ HẠN (Microtask Starvation)**

```javascript
console.log('🏪 Quán mở cửa');

// Khách thường đặt hàng
setTimeout(() => {
  console.log('😢 Khách thường: Tôi chờ mãi không tới lượt!');
}, 0);

// Khách VIP liên tục (VÔ HẠN!)
function khachVIPLienTuc() {
  Promise.resolve().then(() => {
    console.log('⭐ Khách VIP: Phục vụ tôi đi!');
    khachVIPLienTuc(); // Tạo thêm khách VIP mới!
  });
}

khachVIPLienTuc();

// ===== KẾT QUẢ =====
// 🏪 Quán mở cửa
// ⭐ Khách VIP: Phục vụ tôi đi!
// ⭐ Khách VIP: Phục vụ tôi đi!
// ⭐ Khách VIP: Phục vụ tôi đi!
// ... (vô hạn lần)
// 😢 Khách thường: KHÔNG BAO GIỜ được phục vụ!

// ⚠️ LỖI: Bạn chỉ phục vụ khách VIP mãi, khách thường đói chết!
```

---

**✅ NGUYÊN TẮC VÀNG (Không Technical):**

1. **Làm việc đang làm trước** (Code đồng bộ)
2. **Ưu tiên khách VIP** (Promise, Microtask)
3. **Sau đó mới đến khách thường** (setTimeout, Macrotask)
4. **Không tạo khách VIP vô hạn** (tránh Microtask Starvation)
5. **Luôn check lại** (Event Loop lặp mãi)

---

**🎯 TÓM TẮT BẰNG 1 CÂU:**

> **"Làm hết việc đang làm, ưu tiên khách VIP, rồi mới phục vụ khách thường, và cứ thế lặp lại mãi."**

---

**📝 SO SÁNH VỚI ĐỜI SỐNG THỰC:**

| Thuật Ngữ Technical | Ví Dụ Đời Thường                              |
| ------------------- | --------------------------------------------- |
| Call Stack          | Việc đang làm (pha cà phê, vắt cam)           |
| Microtask Queue     | Danh sách khách VIP (ưu tiên cao)             |
| Macrotask Queue     | Danh sách khách thường (chờ lâu hơn)          |
| Event Loop          | Bạn liên tục check xem còn việc gì chưa       |
| Web APIs            | Máy pha tự động, đồng hồ hẹn giờ              |
| Single Thread       | Chỉ có 1 bạn làm việc, không có nhân viên phụ |
| Non-blocking        | Không đứng đợi, làm việc khác trong lúc chờ   |
| Async               | Đặt hẹn giờ, chờ giao hàng                    |

---

**🎓 BÀI HỌC:**

- JavaScript chỉ có **1 người làm việc** (single-threaded)
- Nhưng **rất thông minh**: không đợi, làm nhiều việc cùng lúc nhờ **ưu tiên** và **hẹn giờ**
- **Khách VIP** (Microtask) luôn được ưu tiên hơn **khách thường** (Macrotask)
- Phải **cẩn thận** không tạo khách VIP vô hạn, nếu không khách thường đói chết!

**💡 Nhớ công thức:**

```
Làm xong việc đang làm
→ Phục vụ HẾT khách VIP
→ Phục vụ MỘT khách thường
→ Lặp lại
```

---

# ⏱️ Advanced Deferring Execution Techniques - Kỹ Thuật Trì Hoãn Thực Thi Nâng Cao

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"Deferring execution là kỹ thuật trì hoãn chạy code để optimize performance (tối ưu hiệu năng), bao gồm debounce, throttle, requestIdleCallback, và lazy loading."**

**💡 Giải thích đơn giản:**

**1. Debounce:**

- **Chờ user ngừng action** rồi mới execute (delay reset sau mỗi call)
- Use case: search input (chờ user gõ xong), window resize
- Ví dụ: `debounce(fn, 300)` → user gõ → chờ 300ms không gõ nữa → chạy

**🔑 5 Kỹ Thuật Chính - 5 Techniques Quan Trọng:**

**1. Debounce - Chờ Ngừng Hành Động:**

- **Chờ user ngừng action** rồi mới execute (delay reset sau mỗi call)

  - Mỗi lần user action → Reset timer → Đợi lại từ đầu
  - Chỉ chạy khi user ngừng action trong khoảng thời gian delay
  - 💡 Giống như: Đợi thang máy → Mỗi lần có người bấm → Reset timer → Đợi lại

- **Use case - Trường hợp sử dụng**:

  - Search input (chờ user gõ xong) → Tránh gọi API mỗi lần gõ
  - Window resize → Tránh tính toán layout mỗi lần resize

- **Ví dụ**: `debounce(fn, 300)`
  - User gõ "a" → Reset timer, đợi 300ms
  - User gõ "b" (trong 300ms) → Reset timer, đợi lại 300ms
  - User gõ "c" (trong 300ms) → Reset timer, đợi lại 300ms
  - User ngừng gõ 300ms → Chạy hàm `fn` với "abc"
  - → Chỉ chạy 1 lần thay vì 3 lần!

**2. Throttle - Giới Hạn Tần Suất:**

- **Execute tối đa 1 lần trong X ms**, bỏ qua calls giữa interval

  - Chạy ngay lần đầu → Bỏ qua tất cả calls trong X ms tiếp theo
  - Sau X ms → Cho phép chạy lại
  - 💡 Giống như: Đèn giao thông → Xanh → Đỏ → Xanh (cố định thời gian)

- **Use case - Trường hợp sử dụng**:

  - Scroll events → Tránh tính toán mỗi pixel scroll
  - Mouse move → Tránh update UI mỗi pixel di chuyển
  - API rate limiting → Giới hạn số requests/giây

- **Ví dụ**: `throttle(fn, 1000)`
  - Call 1: Chạy ngay → Bỏ qua calls trong 1s tiếp theo
  - Call 2 (0.5s sau): Bỏ qua
  - Call 3 (0.8s sau): Bỏ qua
  - Call 4 (1.2s sau): Chạy (đã qua 1s)
  - → Chỉ chạy 2 lần thay vì 4 lần!

**3. requestIdleCallback - Chạy Khi Browser Rảnh:**

- Chạy task khi browser **idle** (không busy với rendering/user input)

  - Browser đang render UI hoặc xử lý user input → Không chạy
  - Browser rảnh (không có gì làm) → Chạy task
  - 💡 Giống như: Làm việc phụ khi rảnh tay (không ảnh hưởng công việc chính)

- **Use case - Trường hợp sử dụng**:

  - Analytics (phân tích) → Gửi data tracking khi browser rảnh
  - Non-critical updates (cập nhật không quan trọng) → Update UI phụ
  - Prefetching data (tải trước dữ liệu) → Tải data cho trang tiếp theo

- **Fallback - Dự phòng**: `setTimeout(fn, 1)` cho browsers không support
  - Nếu browser không hỗ trợ → Dùng setTimeout với delay nhỏ (1ms)
  - → Tương tự nhưng không tối ưu bằng requestIdleCallback

**4. requestAnimationFrame - Đồng Bộ Với Browser:**

- Execute **trước next repaint** (~60fps = 16.67ms)

  - Chạy trước khi browser vẽ lại màn hình (repaint)
  - Tần suất: ~60 lần/giây (60fps) = Mỗi 16.67ms
  - 💡 Đồng bộ với refresh rate của màn hình → Animation mượt mà

- **Use case - Trường hợp sử dụng**:

  - Animations (hoạt hình) → Animation mượt, không giật
  - Smooth scrolling (cuộn mượt) → Scroll mượt mà
  - Visual updates (cập nhật giao diện) → Update UI mượt

- **Better than `setTimeout` vì sync với browser refresh rate**
  - setTimeout: Không đồng bộ → Có thể bỏ qua frame → Animation giật
  - requestAnimationFrame: Đồng bộ → Không bỏ qua frame → Animation mượt

**5. Lazy Loading / Code Splitting - Tải Khi Cần:**

- Load code/assets **only when needed** (dynamic import)

  - Không tải tất cả code ngay → Chỉ tải khi cần
  - Giảm bundle size ban đầu → App load nhanh hơn
  - 💡 Giống như: Mua đồ khi cần, không mua hết ngay

- **Use case - Trường hợp sử dụng**:

  - Route-based splitting (chia theo route) → Mỗi route tải code riêng
  - Below-fold images (ảnh dưới màn hình) → Tải khi user scroll xuống
  - Modals (hộp thoại) → Tải component khi user mở modal

- **React**: `React.lazy(() => import('./Component'))`
  - Component chỉ được tải khi render lần đầu
  - → Giảm bundle size ban đầu → Initial load nhanh hơn

**⚠️ Lỗi Thường Gặp - Common Mistakes:**

- **Debounce search mà không cancel previous request → race condition**

  - Vấn đề: User gõ "abc" → Request "abc" gửi đi (chậm)
  - User xóa về "ab" → Request "ab" gửi đi (nhanh)
  - Request "ab" về trước → Hiển thị "ab" ✅
  - Request "abc" về sau → Ghi đè "ab" → Hiển thị "abc" ❌ (sai!)
  - Giải pháp: Cancel request cũ trước khi gửi request mới (AbortController)

- **Throttle scroll mà không check `passive: true` → jank**

  - Vấn đề: Scroll event listener không passive → Browser phải đợi JS xử lý xong mới scroll
  - → Scroll bị giật (jank), không mượt
  - Giải pháp: Thêm `{ passive: true }` → Browser scroll ngay, không đợi JS

- **requestIdleCallback cho critical tasks → user thấy lag**

  - Vấn đề: Dùng requestIdleCallback cho task quan trọng (render UI, update state)
  - → Task chờ browser rảnh → User thấy lag, UI không responsive
  - Giải pháp: Chỉ dùng cho non-critical tasks (analytics, prefetching)

- **Không cleanup timers khi unmount → memory leak**
  - Vấn đề: Component unmount nhưng setTimeout/setInterval vẫn chạy
  - → Chiếm memory, có thể update state sau khi unmount → Error
  - Giải pháp: Cleanup trong useEffect: `return () => clearTimeout(timer)`

**💡 Kiến Thức Senior - Advanced Knowledge:**

- **Debounce vs Throttle - So Sánh:**

  - **Debounce** = "chờ xong hẳn" → Chạy sau khi user ngừng action
    - Ví dụ: Search → Chờ user ngừng gõ 300ms → Gọi API
  - **Throttle** = "giới hạn tần suất" → Chạy tối đa 1 lần trong X ms
    - Ví dụ: Scroll → Chạy ngay, bỏ qua trong 100ms tiếp theo

- **Leading vs Trailing edge - Cạnh Đầu vs Cạnh Cuối:**

  - **Leading edge**: Chạy ngay lần đầu → Sau đó bỏ qua trong delay
    - Ví dụ: Throttle leading → Click ngay → Bỏ qua clicks trong 1s
  - **Trailing edge**: Chạy sau delay → Đợi user ngừng action
    - Ví dụ: Debounce trailing → Chờ 300ms không action → Chạy

- **IntersectionObserver hiệu quả hơn scroll throttle cho lazy loading**

  - Scroll throttle: Vẫn phải lắng nghe mọi scroll event → Tốn tài nguyên
  - IntersectionObserver: Native API → Browser tự detect khi element vào viewport
  - → Hiệu quả hơn, không cần throttle scroll

- **Web Workers cho heavy computations không block main thread**

  - Main thread: Xử lý UI, user input → Nếu block → UI đơ, không responsive
  - Web Workers: Chạy code ở thread riêng → Không block main thread
  - → User vẫn tương tác được khi đang tính toán nặng

- **Priority scheduling: `scheduler.postTask()` API (Chrome)**
  - Cho phép đặt priority cho tasks:
    - `user-blocking`: Quan trọng, ảnh hưởng user → Chạy ngay
    - `user-visible`: Hiển thị cho user → Chạy sau user-blocking
    - `background`: Không quan trọng → Chạy cuối cùng
  - → Browser tự động sắp xếp thứ tự chạy theo priority

---

## **📚 PHẦN CHI TIẾT - CODE EXAMPLES & GIẢI THÍCH**

### **1. setTimeout(0) - Macrotask Queue**

```typescript
// ═══════════════════════════════════════════════════════════
// SETTIMEOUT(0) - Đưa code vào Macrotask Queue
// ═══════════════════════════════════════════════════════════

console.log('1. Sync code - Chạy ngay'); // 📝 Chạy ngay lập tức (synchronous)

setTimeout(() => {
  // ⏱️ setTimeout(0) → Đưa callback vào Macrotask Queue
  // 💡 Macrotask Queue: Hàng đợi các task lớn (setTimeout, setInterval, I/O...)
  // 💡 Chạy SAU khi tất cả sync code và microtasks xong
  console.log('3. setTimeout(0) - Chạy sau sync code và microtasks');
}, 0); // ⏱️ Delay = 0ms → Chạy ngay khi có thể (nhưng vẫn chờ sync code xong)

Promise.resolve().then(() => {
  // 🔄 Promise.resolve() → Đưa callback vào Microtask Queue
  // 💡 Microtask Queue: Hàng đợi các task nhỏ (Promises, queueMicrotask...)
  // 💡 Chạy TRƯỚC Macrotask Queue → Ưu tiên cao hơn
  console.log('2. Promise.resolve() - Chạy sau sync code, trước setTimeout');
});

console.log('1. Sync code tiếp tục - Vẫn chạy ngay'); // 📝 Vẫn chạy ngay

// 📊 Kết quả:
// 1. Sync code - Chạy ngay
// 1. Sync code tiếp tục - Vẫn chạy ngay
// 2. Promise.resolve() - Chạy sau sync code, trước setTimeout
// 3. setTimeout(0) - Chạy sau sync code và microtasks

// 💡 Thứ tự thực thi:
// 1. Sync code (Call Stack) → Chạy ngay
// 2. Microtasks (Promise, queueMicrotask) → Chạy sau sync code
// 3. Macrotasks (setTimeout, setInterval) → Chạy cuối cùng
```

**🔍 Tại sao setTimeout(0) không chạy ngay?**

```typescript
// ═══════════════════════════════════════════════════════════
// VÍ DỤ: setTimeout(0) vs Sync Code
// ═══════════════════════════════════════════════════════════

console.log('Bắt đầu'); // 📝 Chạy ngay

setTimeout(() => {
  console.log('setTimeout(0)'); // ⏱️ Chạy SAU khi tất cả sync code xong
}, 0);

// 🔄 Vòng lặp đồng bộ (blocking) - Chặn thread trong 100ms
const start = Date.now();
while (Date.now() - start < 100) {
  // ⏳ Chờ 100ms (giả lập công việc nặng)
}
console.log('Vòng lặp xong'); // 📝 Chạy sau 100ms

// 📊 Kết quả:
// Bắt đầu
// Vòng lặp xong (sau 100ms)
// setTimeout(0) (sau khi vòng lặp xong)

// 💡 Giải thích:
// - setTimeout(0) KHÔNG chạy ngay lập tức
// - Nó đưa callback vào Macrotask Queue
// - Chỉ chạy SAU khi tất cả sync code trong Call Stack xong
// - → Dù delay = 0ms, vẫn phải chờ sync code hoàn thành
```

**🎯 Use Case: Defer DOM Updates**

```typescript
// ═══════════════════════════════════════════════════════════
// USE CASE: Defer DOM Updates với setTimeout(0)
// ═══════════════════════════════════════════════════════════

function updateDOM() {
  // 📝 Sync code: Thay đổi DOM nhiều lần
  const element = document.getElementById('myDiv');

  element.style.color = 'red'; // 🔴 Thay đổi 1
  element.style.backgroundColor = 'blue'; // 🔵 Thay đổi 2
  element.style.fontSize = '20px'; // 📏 Thay đổi 3

  // ⚠️ Vấn đề: Browser phải reflow/repaint sau mỗi thay đổi
  // → 3 lần reflow/repaint → Chậm, tốn tài nguyên

  // ✅ Giải pháp: Defer với setTimeout(0)
  setTimeout(() => {
    // ⏱️ Tất cả thay đổi DOM được batch lại
    // → Browser chỉ reflow/repaint 1 lần → Nhanh hơn
    element.style.color = 'red';
    element.style.backgroundColor = 'blue';
    element.style.fontSize = '20px';
  }, 0);

  // 💡 Lợi ích:
  // - Batch DOM updates → Chỉ 1 lần reflow/repaint
  // - Không block main thread → UI vẫn responsive
  // - Tối ưu performance → App mượt mà hơn
}
```

---

### **2. Promise.resolve() - Microtask Queue**

```typescript
// ═══════════════════════════════════════════════════════════
// PROMISE.RESOLVE() - Đưa code vào Microtask Queue
// ═══════════════════════════════════════════════════════════

console.log('1. Sync code'); // 📝 Chạy ngay (Call Stack)

Promise.resolve().then(() => {
  // 🔄 Promise.resolve() → Tạo Promise đã resolve ngay
  // 💡 .then() → Đưa callback vào Microtask Queue
  // 💡 Microtask Queue: Ưu tiên cao hơn Macrotask Queue
  // 💡 Chạy SAU sync code, TRƯỚC setTimeout/setInterval
  console.log('2. Promise.resolve() - Microtask');
});

setTimeout(() => {
  // ⏱️ setTimeout → Đưa callback vào Macrotask Queue
  // 💡 Macrotask Queue: Ưu tiên thấp hơn Microtask Queue
  // 💡 Chạy SAU tất cả microtasks
  console.log('3. setTimeout - Macrotask');
}, 0);

console.log('1. Sync code tiếp tục'); // 📝 Vẫn chạy ngay

// 📊 Kết quả:
// 1. Sync code
// 1. Sync code tiếp tục
// 2. Promise.resolve() - Microtask
// 3. setTimeout - Macrotask

// 💡 Thứ tự ưu tiên:
// 1. Call Stack (sync code) → Cao nhất
// 2. Microtask Queue (Promise, queueMicrotask) → Trung bình
// 3. Macrotask Queue (setTimeout, setInterval) → Thấp nhất
```

**🔄 Promise Chain - Nhiều Microtasks**

```typescript
// ═══════════════════════════════════════════════════════════
// PROMISE CHAIN - Nhiều Microtasks
// ═══════════════════════════════════════════════════════════

console.log('1. Start'); // 📝 Sync code

Promise.resolve()
  .then(() => {
    // 🔄 Microtask 1 → Chạy sau sync code
    console.log('2. Promise 1');
    return Promise.resolve(); // 🔄 Trả về Promise đã resolve
  })
  .then(() => {
    // 🔄 Microtask 2 → Chạy sau Microtask 1
    console.log('3. Promise 2');
  });

setTimeout(() => {
  // ⏱️ Macrotask → Chạy SAU tất cả microtasks
  console.log('4. setTimeout');
}, 0);

Promise.resolve().then(() => {
  // 🔄 Microtask 3 → Chạy song song với Microtask 1, 2
  // 💡 Tất cả microtasks chạy TRƯỚC macrotasks
  console.log('2. Promise 3 (song song)');
});

console.log('1. End'); // 📝 Sync code

// 📊 Kết quả:
// 1. Start
// 1. End
// 2. Promise 1
// 2. Promise 3 (song song)
// 3. Promise 2
// 4. setTimeout

// 💡 Giải thích:
// - Tất cả sync code chạy trước
// - Tất cả microtasks (Promise) chạy trước macrotasks (setTimeout)
// - Microtasks chạy theo thứ tự (chain) hoặc song song
// - Macrotasks chạy cuối cùng
```

**🎯 Use Case: Defer State Updates**

```typescript
// ═══════════════════════════════════════════════════════════
// USE CASE: Defer State Updates với Promise.resolve()
// ═══════════════════════════════════════════════════════════

function updateState() {
  let state = { count: 0 }; // 📦 State ban đầu

  // ❌ Vấn đề: Update state nhiều lần sync → Re-render nhiều lần
  state.count++; // Update 1 → Re-render 1
  state.count++; // Update 2 → Re-render 2
  state.count++; // Update 3 → Re-render 3
  // → 3 lần re-render → Chậm, tốn tài nguyên

  // ✅ Giải pháp: Defer với Promise.resolve()
  Promise.resolve().then(() => {
    // 🔄 Batch tất cả state updates
    // → Chỉ re-render 1 lần sau khi tất cả updates xong
    state.count++;
    state.count++;
    state.count++;
    // → 1 lần re-render → Nhanh hơn, tối ưu hơn
  });

  // 💡 Lợi ích:
  // - Batch state updates → Chỉ 1 lần re-render
  // - Không block main thread → UI vẫn responsive
  // - Tối ưu performance → App mượt mà hơn
}

// ═══════════════════════════════════════════════════════════
// REACT EXAMPLE: Defer State Updates
// ═══════════════════════════════════════════════════════════

function Counter() {
  const [count, setCount] = useState(0);

  const handleClick = () => {
    // ❌ Vấn đề: 3 lần setState → 3 lần re-render
    setCount(count + 1);
    setCount(count + 1);
    setCount(count + 1);
    // → count chỉ tăng 1 (vì state chưa update)

    // ✅ Giải pháp 1: Functional update
    setCount((prev) => prev + 1);
    setCount((prev) => prev + 1);
    setCount((prev) => prev + 1);
    // → count tăng 3, nhưng vẫn 3 lần re-render

    // ✅ Giải pháp 2: Defer với Promise.resolve()
    Promise.resolve().then(() => {
      // 🔄 Batch updates → Chỉ 1 lần re-render
      setCount((prev) => prev + 3);
    });
  };

  return <button onClick={handleClick}>Count: {count}</button>;
}
```

---

### **3. queueMicrotask() - Microtask Queue (Native API)**

```typescript
// ═══════════════════════════════════════════════════════════
// QUEUEMICROTASK() - Native API cho Microtask Queue
// ═══════════════════════════════════════════════════════════

console.log('1. Sync code'); // 📝 Chạy ngay

queueMicrotask(() => {
  // 🔄 queueMicrotask() → Đưa callback vào Microtask Queue
  // 💡 Tương tự Promise.resolve().then()
  // 💡 Ưu tiên cao hơn Macrotask Queue
  console.log('2. queueMicrotask() - Microtask');
});

setTimeout(() => {
  // ⏱️ setTimeout → Macrotask Queue
  console.log('3. setTimeout - Macrotask');
}, 0);

Promise.resolve().then(() => {
  // 🔄 Promise.resolve() → Microtask Queue
  console.log('2. Promise.resolve() - Microtask');
});

console.log('1. Sync code tiếp tục'); // 📝 Vẫn chạy ngay

// 📊 Kết quả:
// 1. Sync code
// 1. Sync code tiếp tục
// 2. queueMicrotask() - Microtask
// 2. Promise.resolve() - Microtask
// 3. setTimeout - Macrotask

// 💡 queueMicrotask() vs Promise.resolve().then():
// - queueMicrotask(): Native API, không tạo Promise object
// - Promise.resolve().then(): Tạo Promise object (tốn memory hơn)
// - → queueMicrotask() hiệu quả hơn cho simple callbacks
```

**🎯 Use Case: Priority Task Scheduling**

```typescript
// ═══════════════════════════════════════════════════════════
// USE CASE: Priority Task Scheduling
// ═══════════════════════════════════════════════════════════

function processTasks() {
  // 🔴 Critical task - Quan trọng, cần chạy ngay
  console.log('Critical task');

  // 🟡 Important task - Quan trọng, chạy sau critical
  queueMicrotask(() => {
    console.log('Important task (microtask)');
  });

  // 🟢 Background task - Không quan trọng, chạy cuối cùng
  setTimeout(() => {
    console.log('Background task (macrotask)');
  }, 0);

  // 📊 Thứ tự thực thi:
  // 1. Critical task (sync)
  // 2. Important task (microtask)
  // 3. Background task (macrotask)
}
```

---

### **4. Event Loop - Thứ Tự Thực Thi Chi Tiết**

```typescript
// ═══════════════════════════════════════════════════════════
// EVENT LOOP - Thứ Tự Thực Thi Chi Tiết
// ═══════════════════════════════════════════════════════════

console.log('1. Sync code - Call Stack'); // 📝 Call Stack (ưu tiên cao nhất)

// 🔄 Microtask 1
Promise.resolve().then(() => {
  console.log('2. Promise 1 - Microtask Queue');

  // 🔄 Microtask trong Microtask → Vẫn chạy trước macrotasks
  Promise.resolve().then(() => {
    console.log('3. Promise nested - Microtask Queue');
  });
});

// ⏱️ Macrotask 1
setTimeout(() => {
  console.log('4. setTimeout 1 - Macrotask Queue');

  // 🔄 Microtask trong Macrotask → Chạy ngay sau macrotask này
  Promise.resolve().then(() => {
    console.log('5. Promise in setTimeout - Microtask Queue');
  });
}, 0);

// ⏱️ Macrotask 2
setTimeout(() => {
  console.log('6. setTimeout 2 - Macrotask Queue');
}, 0);

// 🔄 Microtask 2
queueMicrotask(() => {
  console.log('2. queueMicrotask - Microtask Queue');
});

console.log('1. Sync code tiếp tục - Call Stack'); // 📝 Call Stack

// 📊 Kết quả:
// 1. Sync code - Call Stack
// 1. Sync code tiếp tục - Call Stack
// 2. Promise 1 - Microtask Queue
// 2. queueMicrotask - Microtask Queue
// 3. Promise nested - Microtask Queue
// 4. setTimeout 1 - Macrotask Queue
// 5. Promise in setTimeout - Microtask Queue
// 6. setTimeout 2 - Macrotask Queue

// 💡 Quy tắc Event Loop:
// 1. Chạy tất cả sync code trong Call Stack
// 2. Chạy TẤT CẢ microtasks (Promise, queueMicrotask) → Lặp lại cho đến khi hết
// 3. Chạy 1 macrotask (setTimeout, setInterval)
// 4. Lặp lại từ bước 2
// → Microtasks có thể "chặn" macrotasks nếu có quá nhiều
```

---

### **5. Debounce - Implementation Chi Tiết**

```typescript
// ═══════════════════════════════════════════════════════════
// DEBOUNCE - Implementation Chi Tiết
// ═══════════════════════════════════════════════════════════

/**
 * Debounce function - Chờ user ngừng action rồi mới chạy
 * @param func - Hàm cần debounce
 * @param delay - Thời gian chờ (ms)
 * @returns Hàm đã được debounce
 */
function debounce<T extends (...args: any[]) => any>(
  func: T,
  delay: number
): (...args: Parameters<T>) => void {
  let timeoutId: NodeJS.Timeout | null = null; // ⏱️ Lưu ID của timer

  return function (this: any, ...args: Parameters<T>) {
    // 🗑️ Clear timer cũ nếu có (user action lại trước khi delay hết)
    if (timeoutId) {
      clearTimeout(timeoutId); // 🚫 Hủy timer cũ
      // 💡 Mỗi lần user action → Reset timer → Đợi lại từ đầu
    }

    // ⏱️ Tạo timer mới → Chạy hàm sau delay
    timeoutId = setTimeout(() => {
      func.apply(this, args); // ✅ Chạy hàm khi user ngừng action
      timeoutId = null; // 🧹 Clear timeoutId sau khi chạy
    }, delay);
  };
}

// ═══════════════════════════════════════════════════════════
// USE CASE: Search Input với Debounce
// ═══════════════════════════════════════════════════════════

function SearchInput() {
  const [query, setQuery] = useState('');

  // 🔍 Hàm search - Gọi API khi user ngừng gõ
  const searchAPI = async (searchQuery: string) => {
    console.log(`Searching for: ${searchQuery}`); // 📝 Log để debug
    // 📡 Gọi API search
    const response = await fetch(`/api/search?q=${searchQuery}`);
    const data = await response.json();
    return data;
  };

  // ✅ Debounce search function - Chờ 300ms không gõ nữa mới search
  const debouncedSearch = debounce(searchAPI, 300);
  // 💡 delay = 300ms → Chờ user ngừng gõ 300ms mới gọi API
  // 💡 Tránh gọi API mỗi lần user gõ → Tiết kiệm bandwidth, giảm server load

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    setQuery(value); // 📝 Update state ngay (UI responsive)
    debouncedSearch(value); // 🔍 Search sau 300ms (nếu user ngừng gõ)
  };

  return (
    <input
      type="text"
      value={query}
      onChange={handleInputChange}
      placeholder="Search..."
    />
  );
}

// ═══════════════════════════════════════════════════════════
// USE CASE: Window Resize với Debounce
// ═══════════════════════════════════════════════════════════

function handleResize() {
  // 📏 Tính toán layout khi window resize
  const width = window.innerWidth;
  const height = window.innerHeight;
  console.log(`Window size: ${width}x${height}`);
  // 💡 Resize event fire rất nhiều lần → Cần debounce để tránh tính toán quá nhiều
}

// ✅ Debounce resize handler - Chờ 250ms không resize nữa mới tính toán
const debouncedResize = debounce(handleResize, 250);

window.addEventListener('resize', debouncedResize);
// 💡 Chỉ tính toán layout 1 lần sau khi user ngừng resize
// 💡 Tránh tính toán layout mỗi pixel resize → Tối ưu performance
```

**🔄 Debounce với Leading Edge**

```typescript
// ═══════════════════════════════════════════════════════════
// DEBOUNCE LEADING EDGE - Chạy ngay lần đầu
// ═══════════════════════════════════════════════════════════

function debounceLeading<T extends (...args: any[]) => any>(
  func: T,
  delay: number
): (...args: Parameters<T>) => void {
  let timeoutId: NodeJS.Timeout | null = null;
  let hasRun = false; // 🏷️ Đánh dấu đã chạy lần đầu chưa

  return function (this: any, ...args: Parameters<T>) {
    if (!hasRun) {
      // ✅ Chạy ngay lần đầu (leading edge)
      func.apply(this, args);
      hasRun = true; // 🏷️ Đánh dấu đã chạy
    }

    // 🗑️ Clear timer cũ
    if (timeoutId) {
      clearTimeout(timeoutId);
    }

    // ⏱️ Reset timer → Sau delay, cho phép chạy lại
    timeoutId = setTimeout(() => {
      hasRun = false; // 🔄 Reset để cho phép chạy lại
      timeoutId = null;
    }, delay);
  };
}

// 💡 Use case: Button click → Chạy ngay lần đầu, bỏ qua clicks trong delay
const debouncedClick = debounceLeading(handleClick, 1000);
// → Click 1: Chạy ngay ✅
// → Click 2-10 (trong 1s): Bỏ qua ❌
// → Sau 1s: Cho phép chạy lại ✅
```

---

### **6. Throttle - Implementation Chi Tiết**

```typescript
// ═══════════════════════════════════════════════════════════
// THROTTLE - Implementation Chi Tiết
// ═══════════════════════════════════════════════════════════

/**
 * Throttle function - Giới hạn tần suất chạy (tối đa 1 lần trong X ms)
 * @param func - Hàm cần throttle
 * @param delay - Thời gian giới hạn (ms)
 * @returns Hàm đã được throttle
 */
function throttle<T extends (...args: any[]) => any>(
  func: T,
  delay: number
): (...args: Parameters<T>) => void {
  let lastRun = 0; // ⏰ Lưu thời điểm chạy lần cuối
  let timeoutId: NodeJS.Timeout | null = null; // ⏱️ Timer cho trailing edge

  return function (this: any, ...args: Parameters<T>) {
    const now = Date.now(); // ⏰ Thời điểm hiện tại
    const timeSinceLastRun = now - lastRun; // ⏱️ Thời gian từ lần chạy cuối

    if (timeSinceLastRun >= delay) {
      // ✅ Đã qua delay → Chạy ngay (leading edge)
      func.apply(this, args);
      lastRun = now; // ⏰ Cập nhật thời điểm chạy
    } else {
      // ⏱️ Chưa qua delay → Schedule chạy sau (trailing edge)
      if (timeoutId) {
        clearTimeout(timeoutId); // 🗑️ Clear timer cũ
      }

      timeoutId = setTimeout(() => {
        func.apply(this, args); // ✅ Chạy sau delay
        lastRun = Date.now(); // ⏰ Cập nhật thời điểm chạy
        timeoutId = null;
      }, delay - timeSinceLastRun); // ⏱️ Chờ phần còn lại của delay
    }
  };
}

// ═══════════════════════════════════════════════════════════
// USE CASE: Scroll Event với Throttle
// ═══════════════════════════════════════════════════════════

function handleScroll() {
  // 📜 Tính toán khi scroll (VD: update progress bar, lazy load images)
  const scrollTop = window.scrollY;
  const windowHeight = window.innerHeight;
  const documentHeight = document.documentElement.scrollHeight;

  const scrollPercent = (scrollTop / (documentHeight - windowHeight)) * 100;
  console.log(`Scroll: ${scrollPercent.toFixed(2)}%`);
  // 💡 Scroll event fire rất nhiều lần (mỗi pixel) → Cần throttle
}

// ✅ Throttle scroll handler - Tối đa 1 lần trong 100ms
const throttledScroll = throttle(handleScroll, 100);
// 💡 Scroll nhiều lần → Chỉ tính toán tối đa 10 lần/giây (100ms)
// 💡 Tránh tính toán mỗi pixel scroll → Tối ưu performance

window.addEventListener('scroll', throttledScroll, { passive: true });
// 💡 { passive: true } → Browser scroll ngay, không đợi JS xử lý
// 💡 → Scroll mượt mà hơn, không bị jank
```

**🔄 Throttle Leading vs Trailing**

```typescript
// ═══════════════════════════════════════════════════════════
// THROTTLE LEADING - Chạy ngay lần đầu
// ═══════════════════════════════════════════════════════════

function throttleLeading<T extends (...args: any[]) => any>(
  func: T,
  delay: number
): (...args: Parameters<T>) => void {
  let lastRun = 0;

  return function (this: any, ...args: Parameters<T>) {
    const now = Date.now();

    if (now - lastRun >= delay) {
      // ✅ Chạy ngay (leading edge)
      func.apply(this, args);
      lastRun = now;
    }
    // ❌ Bỏ qua nếu chưa qua delay (không có trailing edge)
  };
}

// ═══════════════════════════════════════════════════════════
// THROTTLE TRAILING - Chạy sau delay
// ═══════════════════════════════════════════════════════════

function throttleTrailing<T extends (...args: any[]) => any>(
  func: T,
  delay: number
): (...args: Parameters<T>) => void {
  let timeoutId: NodeJS.Timeout | null = null;

  return function (this: any, ...args: Parameters<T>) {
    if (!timeoutId) {
      // ⏱️ Schedule chạy sau delay (trailing edge)
      timeoutId = setTimeout(() => {
        func.apply(this, args);
        timeoutId = null;
      }, delay);
    }
    // ❌ Bỏ qua nếu đã có timer đang chạy
  };
}

// 💡 So sánh:
// - Leading: Chạy ngay lần đầu → Phù hợp cho immediate feedback
// - Trailing: Chạy sau delay → Phù hợp cho final state
// - Both: Chạy ngay lần đầu + chạy sau delay → Phù hợp cho cả 2
```

---

### **7. requestAnimationFrame - Animation Smooth**

```typescript
// ═══════════════════════════════════════════════════════════
// REQUESTANIMATIONFRAME - Đồng Bộ Với Browser Refresh Rate
// ═══════════════════════════════════════════════════════════

function animate() {
  // 🎬 Animation function - Chạy trước mỗi frame
  const element = document.getElementById('box');
  let position = 0; // 📍 Vị trí ban đầu

  function step() {
    position += 2; // ➡️ Di chuyển 2px mỗi frame
    element!.style.left = `${position}px`; // 📝 Update vị trí

    if (position < 500) {
      // 🔄 Chưa đến đích → Tiếp tục animation
      requestAnimationFrame(step); // ⏱️ Schedule frame tiếp theo
      // 💡 requestAnimationFrame: Đồng bộ với browser refresh rate (~60fps)
      // 💡 → Animation mượt mà, không bị giật
    }
  }

  requestAnimationFrame(step); // 🚀 Bắt đầu animation
}

// ═══════════════════════════════════════════════════════════
// REACT EXAMPLE: Smooth Animation với requestAnimationFrame
// ═══════════════════════════════════════════════════════════

function AnimatedBox() {
  const [position, setPosition] = useState(0);
  const animationRef = useRef<number | null>(null);

  useEffect(() => {
    function animate() {
      setPosition((prev) => {
        const newPos = prev + 2;
        if (newPos < 500) {
          // 🔄 Schedule frame tiếp theo
          animationRef.current = requestAnimationFrame(animate);
        }
        return newPos;
      });
    }

    // 🚀 Bắt đầu animation
    animationRef.current = requestAnimationFrame(animate);

    // 🧹 Cleanup: Cancel animation khi unmount
    return () => {
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current);
      }
    };
  }, []);

  return (
    <div
      style={{
        position: 'absolute',
        left: `${position}px`,
        transition: 'none', // ⚠️ Không dùng CSS transition với RAF
      }}
    >
      Box
    </div>
  );
}

// 💡 requestAnimationFrame vs setTimeout:
// - requestAnimationFrame: Đồng bộ với browser (~60fps) → Mượt mà
// - setTimeout: Không đồng bộ → Có thể bỏ qua frame → Giật
// → Luôn dùng requestAnimationFrame cho animations
```

---

### **8. requestIdleCallback - Chạy Khi Browser Rảnh**

```typescript
// ═══════════════════════════════════════════════════════════
// REQUESTIDLECALLBACK - Chạy Khi Browser Rảnh
// ═══════════════════════════════════════════════════════════

function doBackgroundWork() {
  // 🔧 Background task - Không quan trọng, có thể chờ
  console.log('Doing background work...');
  // 💡 VD: Analytics, prefetching, cleanup...
}

// ✅ Chạy khi browser rảnh (idle)
if ('requestIdleCallback' in window) {
  // 🌐 Browser hỗ trợ requestIdleCallback
  requestIdleCallback(
    (deadline) => {
      // ⏰ deadline: Thông tin về thời gian còn lại
      while (deadline.timeRemaining() > 0) {
        // ✅ Còn thời gian → Tiếp tục làm việc
        doBackgroundWork();
      }

      // ⏱️ Hết thời gian → Schedule lại nếu còn việc
      if (/* còn việc */) {
        requestIdleCallback(arguments.callee);
      }
    },
    { timeout: 5000 } // ⏱️ Tối đa đợi 5s → Chạy dù browser không rảnh
  );
} else {
  // 🔄 Fallback: Dùng setTimeout cho browsers không hỗ trợ
  setTimeout(doBackgroundWork, 1);
}

// ═══════════════════════════════════════════════════════════
// USE CASE: Prefetching Data với requestIdleCallback
// ═══════════════════════════════════════════════════════════

function prefetchNextPage() {
  // 📡 Tải trước data cho trang tiếp theo
  fetch('/api/next-page')
    .then((res) => res.json())
    .then((data) => {
      // 💾 Cache data để dùng sau
      cache.set('next-page', data);
    });
}

// ✅ Prefetch khi browser rảnh → Không ảnh hưởng UI
requestIdleCallback(prefetchNextPage, { timeout: 2000 });
// 💡 Chỉ prefetch khi browser không busy
// 💡 → User experience tốt hơn, không bị lag
```

---

### **9. MessageChannel - Macrotask với Priority**

```typescript
// ═══════════════════════════════════════════════════════════
// MESSAGECHANNEL - Macrotask với Priority Cao Hơn setTimeout
// ═══════════════════════════════════════════════════════════

const channel = new MessageChannel(); // 📡 Tạo message channel
const port1 = channel.port1; // 🔌 Port 1
const port2 = channel.port2; // 🔌 Port 2

port1.onmessage = () => {
  // 📨 Nhận message → Chạy trong Macrotask Queue
  console.log('MessageChannel - Macrotask');
  // 💡 MessageChannel có priority cao hơn setTimeout
  // 💡 → Chạy trước setTimeout trong cùng event loop cycle
};

console.log('1. Sync code');

setTimeout(() => {
  console.log('3. setTimeout - Macrotask');
}, 0);

// 📤 Gửi message → Đưa vào Macrotask Queue
port2.postMessage(null);

Promise.resolve().then(() => {
  console.log('2. Promise - Microtask');
});

console.log('1. Sync code tiếp tục');

// 📊 Kết quả:
// 1. Sync code
// 1. Sync code tiếp tục
// 2. Promise - Microtask
// MessageChannel - Macrotask (trước setTimeout)
// 3. setTimeout - Macrotask

// 💡 Thứ tự Macrotasks:
// 1. MessageChannel
// 2. setTimeout/setInterval
// → MessageChannel có priority cao hơn setTimeout
```

---

### **10. So Sánh Tất Cả Kỹ Thuật**

```typescript
// ═══════════════════════════════════════════════════════════
// SO SÁNH TẤT CẢ KỸ THUẬT - Execution Order
// ═══════════════════════════════════════════════════════════

console.log('1. Sync code - Call Stack');

// 🔄 Microtasks (ưu tiên cao)
Promise.resolve().then(() => console.log('2. Promise - Microtask'));
queueMicrotask(() => console.log('2. queueMicrotask - Microtask'));

// ⏱️ Macrotasks (ưu tiên thấp)
setTimeout(() => console.log('4. setTimeout - Macrotask'), 0);
setInterval(() => {}, 0); // ⏱️ setInterval cũng là macrotask

const channel = new MessageChannel();
channel.port2.onmessage = () => console.log('3. MessageChannel - Macrotask');
channel.port1.postMessage(null); // 📤 MessageChannel (priority cao hơn setTimeout)

requestAnimationFrame(() =>
  console.log('3. requestAnimationFrame - Before Paint')
);
// 💡 requestAnimationFrame: Chạy trước browser repaint

requestIdleCallback(() => console.log('5. requestIdleCallback - When Idle'));
// 💡 requestIdleCallback: Chạy khi browser rảnh (sau tất cả)

console.log('1. Sync code tiếp tục');

// 📊 Kết quả (thứ tự):
// 1. Sync code - Call Stack
// 1. Sync code tiếp tục - Call Stack
// 2. Promise - Microtask
// 2. queueMicrotask - Microtask
// 3. MessageChannel - Macrotask (priority cao)
// 3. requestAnimationFrame - Before Paint
// 4. setTimeout - Macrotask (priority thấp)
// 5. requestIdleCallback - When Idle (cuối cùng)

// 💡 Tóm tắt thứ tự ưu tiên:
// 1. Call Stack (sync code) → Cao nhất
// 2. Microtask Queue (Promise, queueMicrotask) → Trung bình
// 3. Macrotask Queue (MessageChannel > requestAnimationFrame > setTimeout) → Thấp
// 4. requestIdleCallback → Thấp nhất (khi browser rảnh)
```

---

### **💡 Best Practices - Tối Ưu Hóa**

```typescript
// ✅ 1. Dùng debounce cho search input
const debouncedSearch = debounce(searchAPI, 300);

// ✅ 2. Dùng throttle cho scroll/resize events
const throttledScroll = throttle(handleScroll, 100);

// ✅ 3. Dùng requestAnimationFrame cho animations
requestAnimationFrame(animate);

// ✅ 4. Dùng requestIdleCallback cho background tasks
requestIdleCallback(doBackgroundWork);

// ✅ 5. Dùng Promise.resolve() để defer state updates
Promise.resolve().then(() => {
  // Batch state updates
});

// ✅ 6. Cleanup timers khi component unmount
useEffect(() => {
  const timer = setTimeout(() => {}, 1000);
  return () => clearTimeout(timer);
}, []);

// ✅ 7. Dùng { passive: true } cho scroll listeners
window.addEventListener('scroll', handler, { passive: true });

// ✅ 8. Cancel requests với AbortController
const controller = new AbortController();
fetch(url, { signal: controller.signal });
controller.abort(); // Cancel khi cần
```
