# 🛠️ Chrome DevTools Mastery - Hướng Dẫn Chi Tiết Tiếng Việt

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"Chrome DevTools có 5 tab chính: Network (phân tích request), Performance (kiểm tra rendering & Core Web Vitals), Sources (debug code), Application (kiểm tra storage & Service Workers), Memory (tìm memory leaks). Tôi từng optimize app từ score 45 → 92 bằng cách: identify bundle 3MB → split code thành 900KB, detect layout thrashing → batch DOM changes, find memory leaks → clean event listeners, setup Service Worker caching. Result: Lighthouse 92, 99% users interactive < 2.5s"**

**Key tools:** 
- Lighthouse (kiểm tra tự động)
- Performance recording (ghi lại performance)
- Network throttling (mô phỏng mạng chậm)
- Memory profiler (phân tích bộ nhớ)
- Coverage tab (tìm code không dùng)
- React DevTools Profiler (phân tích React)

---

## **1. NETWORK TAB - Phân Tích Request & Response**

### **Mục đích:**
- Chẩn đoán hiệu suất mạng, tìm các request chậm
- Xác định các file nào load chậm nhất
- Tối ưu chiến lược cache để tăng tốc độ tải

### **1.1 Waterfall Analysis - Biểu Đồ Thác Nước**

Mỗi request được chia thành các giai đoạn:

```
┌──────────────────────────────────────────────────────┐
│ File         │ Status │ Type │ Size    │ Thời gian  │
├──────────────────────────────────────────────────────┤
│ index.html   │ 200    │ doc  │ 45KB    │ 280ms      │
│  ├─ Stalled  │        │      │         │ 50ms ⚠️    │ ← Chờ connection
│  ├─ DNS      │        │      │         │ 30ms       │ ← Lookup tên miền
│  ├─ Connect  │        │      │         │ 50ms       │ ← Kết nối TCP
│  ├─ TLS      │        │      │         │ 80ms       │ ← SSL handshake
│  ├─ Request  │        │      │         │ 10ms       │ ← Gửi request
│  └─ Download │        │      │         │ 60ms       │ ← Download file
│
│ bundle.js    │ 200    │ js   │ 1.2MB   │ 1.2s ⚠️⚠️ │ ← File quá lớn!
│  ├─ Stalled  │        │      │         │ 20ms       │
│  └─ Download │        │      │         │ 1.18s      │ ← Mất lâu!
│
│ api/users    │ 200    │ xhr  │ 50KB    │ 450ms      │
│  ├─ TTFB     │        │      │         │ 400ms ⚠️   │ ← Server chậm
│  └─ Download │        │      │         │ 50ms       │
│
│ favicon.ico  │ 304    │ img  │ 0B      │ 100ms      │
│  └─ Cache hit│        │      │         │            │ ← Dùng cache (tốt!)
└──────────────────────────────────────────────────────┘
```

**Các giai đoạn quan trọng:**

| Giai đoạn | Ý nghĩa | Giải pháp |
|-----------|---------|----------|
| **Stalled** | Chờ connection slot (trình duyệt busy) | Tối ưu concurrent connections |
| **DNS** | Phân giải tên miền → IP | Dùng DNS caching, prefetch DNS |
| **Connect** | Thiết lập kết nối TCP | Tối ưu network latency, CDN |
| **TLS** | SSL handshake (HTTPS overhead) | Dùng HTTP/2, TLS 1.3 |
| **Request** | Gửi request (thường rất nhanh) | Thường không cần optimize |
| **TTFB** | Time To First Byte - server phản hồi | Tối ưu server-side, caching, database |
| **Download** | Tải file | Nén file (gzip/brotli), giảm kích thước |

### **1.2 Phát Hiện & Giải Quyết Vấn Đề**

```js
// ❌ VẤN ĐỀ 1: Bundle JavaScript quá lớn (1.2MB)
// 💡 Ảnh hưởng: User phải chờ 1.2 giây, đặc biệt trên 3G/4G

// ✅ GIẢI PHÁP:
// 1. Code Splitting - Chia code thành chunks nhỏ
//    → Load chỉ code cần thiết, không load hết lúc đầu
//    → Giảm bundle từ 1.2MB → 900KB
//    
// 2. Tree Shaking - Loại bỏ dead code
//    → Chỉ giữ code được import/dùng
//    → Webpack/Vite tự động làm
//    
// 3. Minify - Nén code
//    → Xóa whitespace, xuống dòng
//    → Ví dụ: function hello() {} → function hello(){}
//    
// 4. Server-side Compression (gzip/brotli)
//    → Server nén file trước khi gửi
//    → 1.2MB → ~300KB sau nén

// ❌ VẤN ĐỀ 2: TTFB cao (400ms)
// 💡 Ảnh hưởng: Server chậm → user cảm thấy app không responsive

// ✅ GIẢI PHÁP:
// 1. Optimize Database
//    → Tạo indexes, tối ưu queries
//    → Tránh N+1 queries
//    → 400ms → 50ms
//    
// 2. Caching với Redis
//    → In-memory database, cực kỳ nhanh
//    → Cache query results
//    → 400ms → 10ms (cache hit)
//    
// 3. CDN cho Static Assets
//    → Servers gần user hơn
//    → Download nhanh hơn
//    
// 4. HTTP/2 hoặc HTTP/3
//    → Protocol nhanh hơn HTTP/1.1
//    → Multiplexing, server push
```

### **1.3 Kiểm Tra Timing Của Resources**

```js
// API của browser để lấy timing chi tiết
performance.getEntriesByType('resource').forEach((entry) => {
  // entry.name: URL của resource
  // entry.duration: Tổng thời gian (milliseconds)
  console.log(`${entry.name}: ${entry.duration.toFixed(2)}ms`);
});

// Output ví dụ:
// bundle.js: 1245.50ms  ← File này load chậm nhất → cần optimize
// api/users: 450.25ms
// image.png: 125.60ms
```

**Mẹo:** Check Network tab với throttling (giả lập 3G/4G) để test realistic performance

---

## **2. PERFORMANCE TAB - Phân Tích Rendering & Core Web Vitals**

### **Mục đích:**
- Tìm điểm tắc nghẽn (bottlenecks) trong quá trình render
- Phát hiện jank (giật, lag khi scroll/animate)
- Đo Core Web Vitals: FCP, LCP, CLS, INP

### **2.1 Flame Chart - Biểu Đồ Lửa**

Flame chart hiển thị timeline của mọi thứ xảy ra khi load page:

```
Thời gian: 0ms ──────── 1000ms ──────── 2000ms
                │
Parse HTML  ▓▓▓▓ (200ms) ← Parse HTML
                │
Eval Script ░░░░░░░░ (400ms) ← JavaScript execution (tốn kém!)
                │
Layout      ████ (100ms) ← Tính toán layout (reflow)
                │
Paint       ██████ (120ms) ← Vẽ lại pixels (rẻ hơn layout)
                │
Composite   ██ (20ms) ← Ghép layers ✅ (nhanh nhất!)
                │
FCP         ════════════════════════════════
            ↑ First Contentful Paint (1100ms)
            Lúc đầu tiên nội dung xuất hiện
                │
LCP         ════════════════════════════════════
            ↑ Largest Contentful Paint (1450ms)
            Lúc element lớn nhất render xong
                │
CLS         ═══════════════════════════════════
            Cumulative Layout Shift (0.05)
            Có bao nhiêu layout shift không mong muốn
```

### **2.2 Core Web Vitals - Các Chỉ Số Quan Trọng**

| Chỉ số | Định nghĩa | Mục tiêu | Cải thiện |
|--------|-----------|---------|----------|
| **FCP** | Thời điểm đầu tiên nội dung xuất hiện | < 1.8s | Loại bỏ blocking CSS, defer JS |
| **LCP** | Thời điểm element lớn nhất render xong | < 2.5s | Code splitting, lazy loading, image optimization |
| **CLS** | Layout shift không mong muốn (0-1 scale) | < 0.1 | Đặt width/height cho images, fonts |
| **INP** | Thời gian từ user click → browser phản hồi | < 200ms | Optimize JavaScript, batch DOM |

### **2.3 Phát Hiện & Giải Quyết Jank**

**Jank** = Hiện tượng UI bị giật, lag, không mượt mà

```js
// ❌ VẤN ĐỀ 1: JavaScript chạy quá lâu (> 50ms)
// 💡 Nguyên tắc: Browser render 60fps = 16.67ms/frame
//    Nếu JS chạy > 50ms → bỏ lỡ 3 frames → user thấy lag

function heavyComputation() {
  let sum = 0;
  for (let i = 0; i < 1_000_000_000; i++) {
    // ❌ VẤN ĐỀ: Loop 1 tỷ lần block main thread 500ms+
    // → Browser không render → UI freeze
    sum += i;
  }
  return sum;
}

// ✅ GIẢI PHÁP 1: Chia nhỏ thành chunks
function optimized() {
  let sum = 0, i = 0;
  const chunkSize = 1_000_000;
  
  function chunk() {
    for (let end = Math.min(i + chunkSize, 1_000_000_000); i < end; i++) {
      sum += i;
    }
    
    if (i < 1_000_000_000) {
      setTimeout(chunk, 0); // ✅ Nhường quyền cho browser render
    }
  }
  chunk();
}

// ✅ GIẢI PHÁP 2: Web Workers (chạy background)
const worker = new Worker('computation.js');
worker.postMessage({ data: 1_000_000_000 });
worker.onmessage = (e) => {
  console.log('Result:', e.data);
  // Main thread vẫn có thể render, không bị block
};

// ❌ VẤN ĐỀ 2: Layout Thrashing (đọc/ghi DOM trong loop)
// ❌ CODE TỆ:
for (let i = 0; i < 100; i++) {
  el.style.height = el.offsetHeight + 10 + 'px';
  // VẤN ĐỀ: Mỗi lần → 2 reflows (read + write)
  // 100 lần × 2 = 200 reflows → cực chậm!
}

// ✅ CODE TỐT: Batch operations
const height = el.offsetHeight; // Read 1 lần
el.style.height = (height + 1000) + 'px'; // Write 1 lần
// Tổng: 2 reflows thay vì 200 → nhanh 100 lần!

// ❌ VẤN ĐỀ 3: Expensive Paint (vẽ lại tốn kém)
// ❌ boxShadow expensive (tốn kém khi animate)
el.style.boxShadow = '0 0 20px rgba(0,0,0,0.5)';

// ✅ Dùng filter (browser có thể optimize)
el.style.filter = 'drop-shadow(0 0 20px rgba(0,0,0,0.5))';

// ✅ GPU acceleration (dùng GPU thay CPU)
el.style.willChange = 'transform'; // Hint cho browser
el.style.transform = 'translateZ(0)'; // Force GPU layer
// GPU nhanh hơn CPU rất nhiều cho graphics
```

---

## **3. SOURCES TAB - Debug Code**

### **Mục đích:**
- Tìm và sửa lỗi trong code
- Dừng code tại điểm cụ thể để kiểm tra (breakpoints)
- Xem giá trị biến, call stack

### **3.1 Các Loại Breakpoint**

```js
// 1️⃣ LINE BREAKPOINT (đơn giản nhất)
// Cách: Click vào số dòng trong Sources tab
// Khi code đến dòng đó → tự động pause

function calculateTotal(items) {
  let total = 0;
  // ← Click vào dòng này để set breakpoint
  for (let item of items) {
    total += item.price;
  }
  return total;
}

// 2️⃣ CONDITIONAL BREAKPOINT (chỉ dừng khi điều kiện đúng)
// Cách: Right-click số dòng → "Add conditional breakpoint"
// Nhập điều kiện: user.id === 123

function processUser(user) {
  console.log(user.name); // ← Pause chỉ khi user.id === 123
}

// 3️⃣ DOM BREAKPOINT (dừng khi DOM thay đổi)
// Cách: Right-click element → "Break on" → chọn loại:
//   - "Subtree modifications" → khi children thay đổi
//   - "Attribute modifications" → khi attributes thay đổi
//   - "Node removal" → khi element bị xóa

// 4️⃣ EVENT LISTENER BREAKPOINT (dừng khi event trigger)
// Cách: Sources → "Event Listener Breakpoints" → chọn events:
//   - Mouse: click, mousemove
//   - Keyboard: keydown, keyup
//   - Network: fetch, XHR
//   - Timer: setTimeout, setInterval

// 5️⃣ EXCEPTION BREAKPOINT (dừng khi có lỗi)
// Cách: Ctrl+Shift+E hoặc click icon "Pause on exceptions"
// Code pause tại uncaught error → dễ debug

function divide(a, b) {
  return a / b; // Pause khi b = 0 → error
}
```

### **3.2 Call Stack & Scope**

**Call Stack** = Danh sách functions đã gọi để đến điểm này

```
Call Stack (bottom → top):
├─ funcC() ← Current function (Có thể inspect local variables)
├─ funcB() ← Parent function (Caller của funcC)
├─ funcA() ← Grandparent function
└─ Global ← Root (global variables: window, document)

Scope Panel:
├─ Local: Variables của function hiện tại
├─ Closure: Variables từ outer functions
└─ Global: Global variables
```

Ví dụ:
```js
function funcA() {
  funcB(); // funcB gọi từ đây
}

function funcB() {
  funcC(); // funcC gọi từ đây
}

function funcC() {
  debugger; // Pause tại đây
  let localVar = 'C';
  // Call Stack sẽ show: funcC → funcB → funcA → Global
}
```

---

## **4. APPLICATION TAB - Storage & PWA**

### **Mục đích:**
- Xem & chỉnh sửa localStorage, cookies, IndexedDB
- Debug Service Workers & PWA

### **4.1 Storage Types**

| Storage | Giới hạn | Tồn tại | Dùng cho |
|---------|---------|---------|----------|
| **localStorage** | 5-10MB | Mãi mãi | User preferences, settings |
| **sessionStorage** | 5-10MB | Đóng tab | Temporary data |
| **Cookies** | 4KB | Tuỳ expires | Auth tokens, preferences |
| **IndexedDB** | 50% disk | Tuỳ | Large files, complex data |

```js
// localStorage - Persistent
localStorage.setItem('user', JSON.stringify({ id: 1, name: 'John' }));
// DevTools → Application → Local Storage → xem/edit/delete

// sessionStorage - Temporary (xóa khi đóng tab)
sessionStorage.setItem('temp', 'data');

// Cookies (tự động gửi với requests)
// DevTools → Application → Cookies → xem tất cả cookies

// IndexedDB - Large-scale database
const db = await new Promise((resolve) => {
  const req = indexedDB.open('myDB', 1);
  req.onsuccess = () => resolve(req.result);
});
// DevTools → Application → IndexedDB → xem databases
```

### **4.2 Service Workers - PWA Debugging**

```js
// Register Service Worker
navigator.serviceWorker.register('/sw.js');

// DevTools → Application → Service Workers:
// - Xem status: "running" hoặc "stopped"
// - Test offline: Toggle offline → app vẫn work?
// - Xem cache: Application → Cache Storage

// sw.js example: Cache-first strategy
self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open('v1').then((cache) => {
      return cache.addAll(['/index.html', '/styles.css', '/app.js']);
    })
  );
});

self.addEventListener('fetch', (e) => {
  e.respondWith(
    caches.match(e.request).then((response) => {
      return response || fetch(e.request); // Cache first, then network
    })
  );
});
```

---

## **5. MEMORY TAB - Detect Memory Leaks**

### **Mục đích:**
- Phát hiện rò rỉ bộ nhớ (memory không được giải phóng)
- Tìm objects chiếm nhiều memory
- Analyze heap snapshots

### **5.1 Memory Leak Patterns (Các Mẫu Rò Rỉ)**

```js
// ❌ PATTERN 1: Event listeners không unsubscribe
class Modal {
  constructor(element) {
    this.element = element;
    this.element.addEventListener('click', this.handleClick);
    // ❌ VẤN ĐỀ: Listener không được remove
    // → Khi Modal destroy, listener vẫn giữ reference
  }

  destroy() {
    // Quên cleanup!
  }
}

// ✅ GIẢI PHÁP: Remove event listener
class ModalFixed {
  constructor(element) {
    this.element = element;
    this.handleClick = this.handleClick.bind(this);
    this.element.addEventListener('click', this.handleClick);
  }

  destroy() {
    this.element.removeEventListener('click', this.handleClick);
    // ✅ Cleanup: Memory được giải phóng
  }
}

// ❌ PATTERN 2: setTimeout/setInterval không clear
setInterval(() => {
  console.log('running');
}, 1000);
// ❌ VẤN ĐỀ: Timer chạy mãi mãi

// ✅ GIẢI PHÁP: Lưu ID và clear
const id = setInterval(() => {
  console.log('running');
}, 1000);
clearInterval(id); // ✅ Clear timer

// ❌ PATTERN 3: Detached DOM nodes giữ reference
let detachedNode = null;
const node = document.createElement('div');
document.body.appendChild(node);
detachedNode = node;
node.remove();
// ❌ VẤN ĐỀ: node bị xóa khỏi DOM nhưng biến vẫn giữ reference

// ✅ GIẢI PHÁP: Clear reference
node.remove();
detachedNode = null; // ✅ Giải phóng

// ❌ PATTERN 4: Closure giữ large objects
function getData() {
  const largeArray = new Array(1_000_000).fill('data');
  return () => {
    console.log('callback');
    // ❌ Closure giữ reference đến largeArray
  };
}

// ✅ GIẢI PHÁP: Tách biệt
function getDataFixed() {
  const largeArray = new Array(1_000_000).fill('data');
  const callback = () => {
    console.log('callback');
    // ✅ Không reference largeArray
  };
  return callback;
}
```

### **5.2 Heap Snapshot Analysis**

**Cách dùng:**
1. DevTools → Memory → Take snapshot
2. Tương tác với app
3. Take snapshot thứ 2
4. Compare → xem objects nào tăng
5. Kiểm tra "Detached DOM Nodes"
6. Inspect "Retain Path" để tìm root cause

```
📊 Heap Snapshot Report:
├─ Total memory: 145 MB
├─ ⚠️ Detached DOM Nodes: 523 (should be < 10)
│   → Issue: 523 DOM nodes bị xóa nhưng vẫn giữ reference
│   → Solution: Clear all references to removed elements
│
├─ Objects holding most memory:
│  ├─ Array: 45MB (large arrays not cleared)
│  ├─ Object: 32MB (accumulated objects)
│  ├─ String: 28MB (retained strings)
│  └─ Detached DOM: 15MB (removed elements)
│
└─ Retain Path (đường dẫn giữ memory):
   window → myGlobalVar → largeArray[0] → Detached div ← HERE!
   Solution: Clear myGlobalVar
```

---

## **6. COVERAGE TAB - Unused Code Detection**

### **Mục đích:**
- Tìm JavaScript & CSS không được sử dụng
- Giảm kích thước bundle

### **Cách dùng:**

```
1. DevTools → Coverage → Click record
2. Tương tác với app (click buttons, navigate pages)
3. DevTools ghi lại code được execute
4. Xem % code used vs unused

📊 Report:
├─ bundle.js: 45% used (55% unused - 550KB wasted!)
├─ styles.css: 78% used (22% unused)
└─ vendor.js: 20% used (80% unused - old dependencies?)
```

### **Optimization strategies:**

1. **Code Splitting** - Chia code thành chunks nhỏ
   ```js
   // Chỉ load code cần thiết cho mỗi route
   import('route-home.js'); // Load khi cần
   ```

2. **Tree Shaking** - Loại bỏ code không export/import
   ```js
   // Webpack/Vite tự động remove dead code
   ```

3. **Lazy Loading** - Load libraries on-demand
   ```js
   // Chỉ load chart library khi user click "Show Chart"
   import('./chart.js');
   ```

4. **Dependency Audit** - Xóa unused packages
   ```bash
   npm-check # Kiểm tra unused packages
   depcheck # Detect unused dependencies
   ```

---

## **7. Quy Trình Tối Ưu Performance (Systematic Approach)**

### **📊 BƯỚC 1: MEASURE - Đo Lường**

```js
// Tools để đo lường:
// 1. Lighthouse → overall score
// 2. Performance tab → flame chart
// 3. Network tab → waterfall, request timings
// 4. Memory tab → memory leaks
```

**Metrics cần check:**
- Lighthouse Score (0-100)
- Core Web Vitals: FCP, LCP, CLS, INP
- Bundle size, TTFB, FID
- Memory usage

### **🔍 BƯỚC 2: DIAGNOSE - Chẩn Đoán**

Xác định vấn đề ở đâu:

```
❓ JavaScript chạy lâu?
   → Performance tab → xem long tasks (>50ms)
   → Giải pháp: Code splitting, Web Workers

❓ Network chậm?
   → Network tab → xem TTFB, download time
   → Giải pháp: Compression, CDN, HTTP/2

❓ Memory rò rỉ?
   → Memory tab → heap snapshots
   → Giải pháp: Clean listeners, clear timers

❓ Layout thrashing?
   → Performance tab → xem Layout operations
   → Giải pháp: Batch DOM operations, use transform
```

### **🔧 BƯỚC 3: FIX - Sửa**

Implement giải pháp dựa trên vấn đề:

```
📦 Bundle Size
   ├─ Code splitting (dynamic imports)
   ├─ Tree shaking (remove dead code)
   ├─ Minification (compress)
   └─ gzip/brotli compression

🌐 Network
   ├─ Compression (gzip/brotli)
   ├─ CDN (phân phối từ server gần user)
   ├─ HTTP/2 (protocol nhanh hơn)
   └─ Service Workers (offline support)

🎨 Rendering
   ├─ Batch DOM operations
   ├─ Use GPU (transform, translateZ)
   ├─ Remove jank (split long tasks)
   └─ Lazy load images

💾 Memory
   ├─ Clean event listeners (removeEventListener)
   ├─ Clear timers (clearInterval, clearTimeout)
   └─ Break closures (don't hold large objects)
```

### **✅ BƯỚC 4: VERIFY - Xác Minh**

```js
// So sánh metrics trước/sau:
// Before → After
// FCP: 3s → 1.5s ✅
// LCP: 4s → 2s ✅
// Bundle: 1.2MB → 900KB ✅
// Lighthouse: 45 → 92 ✅
```

---

## **8. Console Tricks - Các Mẹo Hữu Ích**

```js
// 1. Styled console output (in có màu)
console.log('%cWarning', 'color: red; font-size: 20px; font-weight: bold');

// 2. $0, $1, $2 = Last selected elements
$0.style.border = '2px solid red'; // Highlight selected element

// 3. copy() - Copy to clipboard
copy(document.body.innerText);

// 4. monitorEvents() - Log all events
monitorEvents(document, 'click'); // Log tất cả clicks
unmonitorEvents(document, 'click'); // Stop logging
```

---

## **9. Interview Tips - Khi Phỏng Vấn**

### **Luôn Follow Systematic Approach:**

```
1. 📊 Measure First
   "Tôi chạy Lighthouse và Performance tab trước"
   "Xác định metrics: FCP, LCP, CLS, bundle size..."

2. 🔍 Diagnose Root Cause
   "Phân tích network waterfall, flame chart, memory usage"
   "Tìm được bottleneck cụ thể: JS? Network? Memory?"

3. 🔧 Implement Fix
   "Fix dựa trên root cause"
   "Code splitting, caching, compression, batch DOM..."

4. ✅ Verify Improvement
   "Chạy lại Lighthouse, so sánh metrics"
   "Ví dụ: Score 45 → 92, FCP 3s → 1.5s"
```

### **Example Answer:**

> "Tôi bắt đầu bằng việc chạy Lighthouse, nhận được score 45. Mở Performance tab thấy JavaScript bundle quá lớn (1.2MB), mất 1.2 giây download. Xem Network tab → chính xác là bundle.js là bottleneck. Tôi implement code splitting dùng dynamic imports, giảm bundle từ 1.2MB → 900KB. Sau đó phát hiện TTFB cao (400ms) → optimize database, thêm Redis caching. Cuối cùng tìm được memory leak từ event listeners không được cleanup → fix. Re-run Lighthouse → score 92, FCP 1.5s, LCP 2s. Kết quả: 99% users interactive < 2.5s."

---

## **⚠️ Common Mistakes (Lỗi Thường Gặp)**

```js
// ❌ Mistake 1: Không clear timers/intervals
setInterval(() => {}, 1000); // Chạy mãi mãi → memory leak

// ✅ Fix:
const id = setInterval(() => {}, 1000);
clearInterval(id);

// ❌ Mistake 2: Giữ reference đến removed DOM
const el = document.getElementById('removed');
el.remove();
// el vẫn giữ reference → memory leak

// ✅ Fix:
el.remove();
el = null; // Clear reference

// ❌ Mistake 3: Chỉ test trên WiFi nhanh
// Không biết performance trên 3G/4G sẽ như thế nào

// ✅ Fix:
// DevTools → Network → Throttling → "Slow 3G"
// Test app trên slow network

// ❌ Mistake 4: Ignore Lighthouse warnings
// Chỉ focus vào Performance, bỏ qua Accessibility, SEO

// ✅ Fix:
// Fix tất cả categories: Performance, Accessibility, SEO, Best Practices
```

---

## **🎯 Cheat Sheet - Các Tính Năng Phải Biết**

| Feature | Cách Dùng | Dùng Khi |
|---------|-----------|---------|
| **Lighthouse** | Ctrl+Shift+I → Lighthouse | Muốn overall performance score |
| **Performance** | Record → interact → stop | Phân tích rendering, find jank |
| **Network** | xem waterfall, request timings | Tìm slow requests, optimize assets |
| **Sources** | Set breakpoints, step through | Debug code |
| **Application** | Xem storage, Service Workers | Debug PWA, test offline |
| **Memory** | Take heap snapshot | Find memory leaks |
| **Coverage** | Record → interact → report | Find unused code |
| **React DevTools** | Profiler tab | Phân tích React component performance |

---

**🚀 Tóm lại:** Chrome DevTools là công cụ không thể thiếu để optimize web performance. Hãy luôn follow systematic approach: Measure → Diagnose → Fix → Verify. Không bao giờ guess, luôn dựa trên data!
