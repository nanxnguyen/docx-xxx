# 🧠 BACKEND DEVELOPER (SENIOR) KNOWLEDGE MINDMAP
## Node.js | Express | NestJS | TypeScript
<!-- 🇻🇳 Bản đồ kiến thức toàn diện cho Backend Developer cấp Senior -->
<!-- Tập trung vào: Node.js runtime, Express patterns, NestJS architecture, TypeORM/Prisma ORM -->

> **Specialized for Node.js Ecosystem**  
> Focus: Production-grade Node.js, Express patterns, NestJS architecture, TypeORM/Prisma
<!-- 🇻🇳 Chuyên sâu về hệ sinh thái Node.js -->
<!-- Bao gồm: Production-ready practices, design patterns, và best practices thực tế -->

## 📌 **INTERVIEW STRUCTURE (Backend Senior)**
<!-- 🇻🇳 CẤU TRÚC PHỎNG VẤN BACKEND SENIOR -->

- **Lý thuyết nâng cao**: ~30% — Runtime internals, DB, cache
  <!-- Kiến thức sâu về Event Loop, V8 engine, optimization, database indexing, caching strategies -->
- **Scenario production**: ~40% — Performance, bug, scale, incident
  <!-- Xử lý tình huống thực tế: tối ưu hiệu suất, debug lỗi production, scale hệ thống, xử lý sự cố -->
- **System design**: ~20% — API, data model, scale out
  <!-- Thiết kế hệ thống: kiến trúc API, data modeling, horizontal scaling, distributed systems -->
- **Troubleshooting**: ~10% — Debug, profiling
  <!-- Kỹ năng debug: memory leak detection, CPU profiling, performance analysis -->

**Level:**
<!-- 🇻🇳 CÁC CẤP ĐỘ KIẾN THỨC -->
🟢 Junior: CRUD, routes, SQL cơ bản · 🟡 Mid: API design, ORM, cache, test · 🔴 Senior: Architecture, perf, production debug, system design
<!-- Junior: Làm được CRUD cơ bản, routing, SQL queries đơn giản -->
<!-- Mid: Thiết kế API RESTful, sử dụng ORM thành thạo, implement caching, viết tests -->
<!-- Senior: Thiết kế kiến trúc, tối ưu performance, debug production issues, system design -->

---

## 📊 **VISUAL MINDMAP**
<!-- 🇻🇳 BẢN ĐỒ TƯ DUY TRỰC QUAN - 6 TRỤ CỘT CHÍNH CỦA NODE.JS BACKEND -->

```
                                    ┌─────────────────────────────────────┐
                                    │    🎯 NODE.JS BACKEND DEVELOPER     │
                                    │   Express | NestJS | TypeScript     │
                                    └─────────────────────────────────────┘
                                                      │
    ┌──────────────┬──────────────┬──────────────────┼───────────────────┬──────────────┬──────────────┐
    │              │              │                  │                   │              │              │
    ▼              ▼              ▼                  ▼                   ▼              ▼              ▼
┌───────────┐  ┌───────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│1.NODE.JS  │  │2.EXPRESS  │  │3.NESTJS      │  │4.DATA LAYER  │  │5.CACHE &     │  │6.PRODUCTION  │
│CORE       │  │& API      │  │ARCHITECTURE  │  │TypeORM/Prisma│  │MESSAGING     │  │ENGINEERING   │
└───────────┘  └───────────┘  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘
<!-- 🇻🇳 -->
<!-- 1. NODE.JS CORE: Nền tảng runtime - Event Loop, V8, memory, streams -->
<!-- 2. EXPRESS & API: Web framework - middleware, routing, validation -->
<!-- 3. NESTJS: Enterprise framework - DI, Guards, Interceptors, Pipes -->
<!-- 4. DATA LAYER: ORM patterns - TypeORM (decorator) vs Prisma (schema-first) -->
<!-- 5. CACHE & MESSAGING: Redis caching, Kafka/Bull queue, event-driven -->
<!-- 6. PRODUCTION: Deployment, monitoring, debugging, Docker/K8s, PM2 -->
     │              │                │                 │                 │                 │
     ▼              ▼                ▼                 ▼                 ▼                 ▼
───────────    ───────────    ─────────────     ─────────────     ─────────────     ─────────────
Event Loop    Middleware      Guards/Pipes      TypeORM           Redis/Cache       Observability
Streams       Routes/Ctrl     Interceptors      Prisma            Kafka/Bull        Debug/Profiling
Worker Thread Error handling  DI Container      Migrations        Event-driven      Docker/K8s
Memory/GC     Validation      Modules           Query Builder     Idempotency       PM2/Cluster
───────────    ───────────    ─────────────     ─────────────     ─────────────     ─────────────
```

---

## 🌳 **MINDMAP CHI TIẾT (Node.js Focus)**
<!-- 🇻🇳 NỘI DUNG CHI TIẾT - BẮT ĐẦU TỪ CÁC KHÁI NIỆM CỐT LÕI NODEJS -->

---

## 🟦 **1. NODE.JS CORE FUNDAMENTALS**
<!-- 🇻🇳 NỀN TẢNG CỐT LÕI CỦA NODE.JS -->
<!-- Bao gồm: V8 engine, Event Loop, memory management, streams, concurrency -->

### **1.1 Node.js Runtime & V8 Engine** ⭐⭐⭐⭐⭐
<!-- 🇻🇳 RUNTIME VÀ ENGINE - CÁCH NODE.JS CHẠY CODE JAVASCRIPT -->
<!-- Đây là nền tảng cơ bản nhất, hiểu rõ phần này sẽ giúp optimize và debug hiệu quả hơn -->

```
🧩 NODE.JS RUNTIME
<!-- 🇻🇳 KIẾN TRÚC NODE.JS - CÁC LAYER TỪ JAVASCRIPT ĐẾN MÁY -->
├── V8 Engine
│   <!-- 🇻🇳 ENGINE JAVASCRIPT CỦA GOOGLE - BIÊN CODE JS THÀNH MÁ MÁY -->
│   ├── JIT compilation: bytecode → machine code
│   │   <!-- JIT (Just-In-Time): biên dịch code JS thành bytecode, rồi tối ưu thành mã máy khi chạy -->
│   │   <!-- Ví dụ: function gọi nhiều lần sẽ được tối ưu hóa cao hơn -->
│   ├── Hidden classes: optimize property access
│   │   <!-- V8 tạo "hidden class" để truy cập thuộc tính nhanh như C++ struct -->
│   │   <!-- ⚠️ Lưu ý: Thêm thuộc tính động (obj.newProp = 1) làm chậm trải! -->
│   ├── Inline caching: speed up method calls
│   │   <!-- Cache kết quả gọi method để lần sau nhanh hơn -->
│   │   <!-- Ví dụ: obj.method() gọi nhiều lần sẽ cache vị trí method -->
│   └── Garbage Collection: Minor GC (Scavenger) + Major GC (Mark-Sweep-Compact)
│       <!-- 🇻🇳 DỌN RÁC TỰ ĐỘNG - GIẢI PHÓNG BỘ NHớ KHÔNG DÙNG -->
│       <!-- Minor GC: dọc vùng Young Gen (nhanh, thường xuyên ~1-2ms) -->
│       <!-- Major GC: dọc vùng Old Gen (chậm, hiếm khi ~50-100ms) -->
├── Node.js Architecture
│   <!-- 🇻ệt NÀM LAYER CỐT LÕI CỦA NODE.JS -->
│   ├── V8: JavaScript engine
│   │   <!-- Engine chạy JavaScript (Google Chrome dùng chính V8 này) -->
│   ├── libuv: async I/O, event loop (C library)
│   │   <!-- 🇻🇳 THƯ VIỆN C QUAN TRỌNG NHẤT - XỬ LÝ BẤT ĐỐNG BỘ -->
│   │   <!-- Quản lý: file I/O, network, timers, event loop -->
│   │   <!-- Cross-platform: chạy được trên Windows, Linux, macOS -->
│   ├── Node.js bindings: bridge between JS and C++
│   │   <!-- Cầu nối giữa JavaScript và thư viện C++ -->
│   │   <!-- Ví dụ: fs.readFile() (JS) → uv_fs_read() (C) -->
│   └── Node.js APIs: fs, http, crypto, etc.
│       <!-- API JavaScript cấp cao cho developers -->
├── Event Loop (Single-threaded, Non-blocking)
│   <!-- 🇻🇳 TIM ĐậP CỦA NODE.JS - VÒNG LẶP SỰ KIỆN -->
│   <!-- CHỈ 1 THREAD NHƯNG XỬ LÝ NHIỀU REQUEST ĐồNG THỜI (non-blocking I/O) -->
│   ├── Phases (in order):
│   │   <!-- 🇻🇳 6 GIẢI ĐOẠN CỦA MỘT VÒNG LẶP - THỨ TỰ RẤT QUAN TRỌNG! -->
│   │   ├── 1. Timers: setTimeout, setInterval callbacks
│   │   │   <!-- Chạy các callback của setTimeout / setInterval đã đến hạn -->
│   │   ├── 2. Pending callbacks: I/O callbacks deferred
│   │   │   <!-- Callback I/O trì hoãn từ vòng lặp trước -->
│   │   ├── 3. Idle, prepare: internal use
│   │   │   <!-- Chỉ dùng nội bộ, không cần quan tâm -->
│   │   ├── 4. Poll: retrieve I/O events, execute callbacks
│   │   │   <!-- 🇻🇳 PHẦN QUAN TRỌNG NHẤT! -->
│   │   │   <!-- Lấy sự kiện I/O mới (network, file), chạy callback -->
│   │   │   <!-- Nếu không có sự kiện, chờ ở đây (hoặc chuyển sang check) -->
│   │   ├── 5. Check: setImmediate callbacks
│   │   │   <!-- Chạy callback của setImmediate() -->
│   │   │   <!-- 👉 setImmediate() luôn chạy SAU poll phase -->
│   │   └── 6. Close callbacks: socket.on('close')
│   │       <!-- Callback đóng kết nối (VD: socket close, server close) -->
│   ├── Microtasks (between phases):
│   │   <!-- 🇻🇳 MICROTASKS - ƯU TIÊN CAO NHẤT, CHẠY GIỮA CÁC PHASE -->
│   │   ├── process.nextTick (highest priority)
│   │   │   <!-- 👉 ƯU TIÊN CAO NHẤT! Chạy ngay sau operation hiện tại -->
│   │   │   <!-- ⚠️ Cẩn thận: Quá nhiều nextTick có thể block event loop! -->
│   │   └── Promise callbacks
│   │       <!-- Chạy sau nextTick, trước khi chuyển sang phase tiếp theo -->
│   └── Rule: Microtasks run AFTER each phase
│       <!-- 👉 Sau mỗi phase, Node.js dọc hết Microtask queue trước khi qua phase khác -->
├── Concurrency in Node.js
│   <!-- 🇻🇳 XỬ LÝ ĐỒNG THỜI TRONG NODE.JS - 4 CÁCH CHÍNH -->
│   ├── Single-threaded: only 1 JavaScript thread
│   │   <!-- Chỉ 1 thread chạy code JavaScript -->
│   │   <!-- ⚠️ Nếu code chạy lâu (VD: loop 1 triệu records), tất cả request bị chặn! -->
│   ├── Non-blocking I/O: libuv handles I/O asynchronously
│   │   <!-- I/O không chặn thread: đọc file, gọi API, query DB --> async -->
│   │   <!-- Đây là lý do Node.js xử lý được nhiều request cùng lúc! -->
│   ├── Worker Threads: CPU-intensive tasks (require('worker_threads'))
│   │   <!-- 🇻🇳 TRÍNH DỖNG CHO TÁC VỤ NẶNG CPU -->
│   │   <!-- Ví dụ: xử lý ảnh, mã hóa, tính toán phức tạp -->
│   │   <!-- Chia sẻ memory, nhẹ hơn Child Process -->
│   ├── Cluster Mode: multiple processes (PM2, node:cluster)
│   │   <!-- Tạo nhiều process (1 process / CPU core) -->
│   │   <!-- Mỗi process có memory riêng biệt -->
│   │   <!-- 👉 Dùng PM2 cho production: pm2 start app.js -i max -->
│   └── Child Processes: spawn external programs
│       <!-- Chạy chương trình ngoài (VD: ffmpeg, python script) -->
│       <!-- Memory tách biệt hoàn toàn -->
├── Memory Management (V8 Heap)
│   <!-- 🇻🇳 QUẢN LÝ BỘ NHớ - HIỂU RÕ ĐỂ TRÁNH MEMORY LEAK! -->
│   ├── Stack: function calls, primitives (fast, limited ~1MB)
│   │   <!-- Stack: lưu biến tạm, tham số function, primitive types (number, string) -->
│   │   <!-- Nhanh nhưng nhỏ (~1MB), tự động giải phóng khi function kết thúc -->
│   ├── Heap Structure:
│   │   <!-- 🇻🇳 CẤU TRÚC HEAP - NƠI LƯU OBJECTS -->
│   │   ├── New Space (Young Generation): 1-8MB, short-lived objects
│   │   │   <!-- Vùng cho object mới tạo, sống ngắn -->
│   │   │   ├── From-space & To-space (semi-space)
│   │   │   │   <!-- 2 vùng: From (chứa objects), To (khi GC copy qua) -->
│   │   │   └── Fast allocation, frequent GC (Scavenger)
│   │   │       <!-- Tạo object nhanh, GC thường xuyên (1-2ms) -->
│   │   │       <!-- Object sống sót 2 lần GC → chuyển sang Old Space -->
│   │   ├── Old Space (Old Generation): long-lived objects
│   │   │   <!-- 🇻🇳 Vùng cho object sống lâu -->
│   │   │   ├── Default: 1.4GB (64-bit), configurable
│   │   │   │   <!-- 👉 Heap mặc định 1.4GB, có thể tăng bằng --max-old-space-size=4096 -->
│   │   │   └── Major GC: Mark-Sweep-Compact (slow)
│   │   │       <!-- 🇻🇳 GC CHẬM - DỌN RÁC Ở OLD SPACE (50-100ms) -->
│   │   │       <!-- Mark: đánh dấu objects còn dùng -->
│   │   │       <!-- Sweep: xóa objects không dùng -->
│   │   │       <!-- Compact: sắp xếp lại memory (chống phân mảnh) -->
│   │   ├── Large Object Space: objects > 1MB
│   │   │   <!-- Khu vực riêng cho object lớn (VD: Buffer 10MB) -->
│   │   │   <!-- Không đi qua Young Gen, vào thẳng Old Gen -->
│   │   └── Code Space: JIT compiled code
│   │       <!-- Code đã được JIT biên dịch -->
│   ├── Memory Leaks (Common in Node.js):
│   │   <!-- 🇻🇳 CÁC LOẠI MEMORY LEAK PHỔ BIẾN TRONG NODE.JS -->
│   │   <!-- ⚠️ Memory leak = bộ nhớ tăng dần, không giải phóng → server crash! -->
│   │   ├── Global variables: `global.cache = []` never cleared
│   │   │   <!-- Biến global (hoặc module-level) luôn tồn tại, không GC được -->
│   │   │   <!-- 👉 Giải pháp: sử dụng LRU cache với TTL -->
│   │   ├── Event listeners: `emitter.on()` without `.off()`
│   │   │   <!-- 🇻🇳 LỖI RẤT PHỔ BIẾN! -->
│   │   │   <!-- Đăng ký listener nhưng không hủy → giữ reference mãi mãi -->
│   │   │   <!-- 👉 Luôn .off() hoặc .removeListener() khi không dùng -->
│   │   ├── Closures: holding large objects in scope
│   │   │   <!-- Closure giữ reference tới biến ngoài → không giải phóng được -->
│   │   │   <!-- Ví dụ: function trả về giữ largeArray trong scope -->
│   │   ├── Timers: `setInterval()` never cleared
│   │   │   <!-- setInterval chạy mãi, giữ reference -->
│   │   │   <!-- 👉 Luôn clearInterval() khi không cần -->
│   │   └── Mongoose models: creating model per request
│   │       <!-- Tạo Mongoose model trong request handler → không giải phóng -->
│   │       <!-- 👉 Tạo model 1 lần ở module level -->
│   └── Tools:
│       <!-- 🇻🇳 CÔNG CỤ PHÁT HIỆN MEMORY LEAK -->
│       ├── Chrome DevTools: heap snapshots, memory profiling
│       │   <!-- Chụp snapshot heap, so sánh 2 thời điểm để tìm leak -->
│       │   <!-- node --inspect → mở chrome://inspect -->
│       ├── node --inspect: enable debugging
│       │   <!-- Bật debug mode, kết nối với Chrome DevTools -->
│       ├── clinic.js: detect memory leaks, event loop lag
│       │   <!-- Tool mạnh để profile production: clinic doctor / clinic flame -->
│       ├── 0x: flamegraphs for profiling
│       │   <!-- Tạo flamegraph để xem function nào thời gian CPU nhiều nhất -->
│       └── --max-old-space-size=4096: increase heap size
│           <!-- Tăng heap size từ 1.4GB lên 4GB (cho server RAM lớn) -->
│           <!-- 👉 node --max-old-space-size=4096 app.js -->
├── Streams API (Node.js)
│   <!-- 🇻🇳 STREAMS - XỬ LÝ DỮ LIỆU LỚN THÀNH TỮNG CHUNK NHỏ -->
│   <!-- Tại sao dùng streams? Memory efficient (không load tất cả vào RAM) -->
│   ├── Types:
│   │   ├── Readable: fs.createReadStream, http.IncomingMessage
│   │   │   <!-- Stream đọc dữ liệu (file, HTTP request body) -->
│   │   │   <!-- Ví dụ: đọc file 1GB chỉ dùng 64KB RAM -->
│   │   ├── Writable: fs.createWriteStream, http.ServerResponse
│   │   │   <!-- Stream ghi dữ liệu (file, HTTP response) -->
│   │   ├── Duplex: net.Socket (both readable & writable)
│   │   │   <!-- Vừa đọc vừa ghi (VD: TCP socket) -->
│   │   └── Transform: zlib.createGzip, crypto streams
│   │       <!-- Biến đổi dữ liệu (VD: gzip, encryption) -->
│   ├── Backpressure:
│   │   <!-- 🇻🇳 ÁP LỰC NGƯC - KHI CONSUMER CHẬM HƠN PRODUCER -->
│   │   ├── Problem: producer faster than consumer → memory overflow
│   │   │   <!-- Nếu đọc file nhanh hơn ghi → buffer tăng → tràn RAM -->
│   │   ├── Solution: .pipe() or pipeline() handles automatically
│   │   │   <!-- 👉 Dùng .pipe() hoặc pipeline() - tự động xử lý backpressure! -->
│   │   └── Manual: check writable.write() return value
│   │       <!-- Nếu writable.write() trả false → buffer đầy, tạm dừng đọc -->
│   ├── Buffer Management:
│   │   ├── highWaterMark: buffer size (default 16KB)
│   │   │   <!-- Kích thước buffer nội bộ (mặc định 16KB) -->
│   │   │   <!-- Có thể tăng cho file lớn: { highWaterMark: 64 * 1024 } -->
│   │   └── Large files: stream instead of Buffer.toString()
│   │       <!-- 🇻🇳 FILE LỚN: LUÔN DÙNG STREAM! -->
│   │       <!-- ❌ Không: fs.readFileSync() → load tất cả vào RAM -->
│   │       <!-- ✅ Nên: fs.createReadStream() → chỉ dùng 16-64KB RAM -->
│   └── Best practice: use pipeline() (error handling + cleanup)
│       <!-- 👉 pipeline() tốt hơn .pipe() - tự động close stream khi lỗi -->
├── CPU-bound vs I/O-bound
│   <!-- 🇻🇳 PHÂN BIỆT 2 LOẠI TÁC VỤ - QUAN TRỌNG ĐỂ TỐI ƯU! -->
│   ├── I/O-bound (95% of Node.js): network, DB, file system
│   │   <!-- Tác vụ chờ I/O: gọi API, query DB, đọc file -->
│   │   <!-- Node.js GIỊI NHẤT cho loại này! (event loop + non-blocking I/O) -->
│   │   └── Solution: async/await, event loop (Node.js excels here)
│   │       <!-- Dùng async/await, event loop tự động xử lý -->
│   ├── CPU-bound (5%): image processing, encryption, heavy computation
│   │   <!-- 🇻🇳 TÁC VỤ NẶNG CPU - ĐIỂM YẾU CỦA NODE.JS! -->
│   │   ├── Problem: blocks event loop → all requests slow
│   │   │   <!-- Nếu chạy tính toán nặng → block event loop → tất cả request chậm! -->
│   │   └── Solutions:
│   │       ├── Worker Threads: parallel computation (share memory)
│   │       │   <!-- Chạy song song, chia sẻ memory (SharedArrayBuffer) -->
│   │       │   <!-- Ví dụ: xử lý 100k images trong worker pool -->
│   │       ├── Child Process: separate process (isolated memory)
│   │       │   <!-- Process riêng biệt, memory tách biệt -->
│   │       ├── Job Queue (Bull/BullMQ): defer to background workers
│   │       │   <!-- 👉 GIẢI PHÁP TỐT NHẤT CHO PRODUCTION! -->
│   │       │   <!-- Đẩy job vào queue (Redis), worker xử lý background -->
│   │       │   <!-- Ví dụ: send email, generate report, video encoding -->
│   │       └── Native addons (C++): extreme performance
│   │           <!-- Viết module C++ cho performance cực kỳ (hiếm dùng) -->
│   └── Rule: operation > 10ms → offload to worker
│       <!-- 👉 QUY TẮC VÀNG: Nếu operation > 10ms → chuyển sang worker! -->
└── Performance Tuning (Node.js)
    <!-- 🇻🇳 TỐI ƯU HIỆU SUẤT NODE.JS -->
    ├── Event Loop Monitoring:
    │   <!-- Đo lường event loop lag để phát hiện blocking code -->
    │   ├── perf_hooks.monitorEventLoopDelay(): measure lag
    │   │   <!-- API đo event loop delay tích hợp sẵn trong Node.js -->
    │   ├── Target: < 10ms lag (p95)
    │   │   <!-- Mục tiêu: 95% request có lag < 10ms -->
    │   └── Alert: lag > 50ms indicates blocking
    │       <!-- Nếu lag > 50ms → có code blocking event loop! -->
    ├── V8 Flags:
    │   <!-- Cờ Node.js chạy với các tùy chọn V8 đặc biệt -->
    │   ├── --max-old-space-size=4096: increase heap (default 1.4GB)
    │   │   <!-- Tăng heap cho server RAM lớn -->
    │   ├── --expose-gc: manual GC trigger (testing only)
    │   │   <!-- Cho phép gọi global.gc() thủ công (chỉ dùng test) -->
    │   └── --trace-gc: log GC events
    │       <!-- Log mỗi lần GC chạy (debug memory issues) -->
    ├── Connection Pooling:
    │   <!-- 🇻🇳 TÁI SỞ DỤNG KẾT NỐI - QUAN TRỌNG! -->
    │   ├── Database: pg.Pool({ min: 2, max: 10 })
    │   │   <!-- Tạo pool 2-10 connections, tái sử dụng thay vì tạo mới -->
    │   ├── Redis: ioredis connection pool
    │   │   <!-- ioredis tự động dùng connection pool -->
    │   └── HTTP clients: use keep-alive
    │       <!-- Dùng keep-alive để tái sử dụng TCP connection -->
    ├── Node.js Versions:
    │   ├── LTS versions: 18.x, 20.x (production)
    │   │   <!-- Dùng LTS (Long Term Support) cho production -->
    │   ├── Current: 21.x (latest features)
    │   │   <!-- Phiên bản mới nhất (chỉ test, không dùng production) -->
    │   └── Update strategy: test in staging first
    │       <!-- Luôn test kỹ ở staging trước khi nâng cấp production -->
    └── Cluster Mode (PM2):
        <!-- 🇻🇳 CHẠY ĐA TIẾÊN TRÌNH ĐỂ DÙNG HẾT CPU CORES -->
        ├── Use all CPU cores: pm2 start app.js -i max
        │   <!-- Tạo process bằng số CPU cores (VD: 4 cores = 4 processes) -->
        ├── Zero-downtime reload: pm2 reload app
        │   <!-- Reload không downtime: restart từng process một -->
        └── Auto-restart on crash: pm2 resurrect
            <!-- Tự động khởi động lại khi crash -->
```

**🔍 Deep Dive: Node.js Event Loop**
<!-- 🇻🇳 VÍ DỤ CHI TIẾT VỀ EVENT LOOP - SO SÁNH CODE TỐT VÀ XẤU -->
```javascript
// ❌ BAD: Blocking event loop
app.get('/process', async (req, res) => {
  const data = await getData(); // 100k records
  const result = data.map(item => expensiveSync(item)); // Blocks!
  res.json(result);
});

// ✅ GOOD: Offload to Worker Thread
const { Worker } = require('worker_threads');
app.get('/process', async (req, res) => {
  const data = await getData();
  const worker = new Worker('./worker.js', { workerData: data });
  worker.on('message', result => res.json(result));
});
```

**📊 Performance Comparison:**
| Approach | Latency | Throughput | Memory |
|----------|---------|------------|--------|
| Blocking | 1000ms | 10 req/s | Low |
| Async I/O | 50ms | 1000 req/s | Low |
| Worker Thread | 100ms | 500 req/s | Medium |
| Child Process | 150ms | 200 req/s | High |

### **1.2 Error Handling, Resilience Patterns** ⭐⭐⭐⭐

```
🛡️ RESILIENCE
├── Error model
│   ├── Typed errors: operational vs programmer errors
│   ├── Error codes: machine-readable (ERR_INVALID_INPUT)
│   ├── Error propagation: throw vs return error
│   └── Error context: stack trace, correlation ID
├── Timeouts & Retries
│   ├── Timeouts: connection, request, query (fail fast)
│   ├── Exponential backoff: 100ms → 200ms → 400ms → 800ms
│   ├── Jitter: random delay to prevent thundering herd
│   └── Max retries: 3-5 attempts (idempotent operations only)
├── Circuit Breaker
│   ├── States: Closed (normal) → Open (failing) → Half-Open (testing)
│   ├── Trip condition: 50% error rate over 10 requests
│   ├── Timeout: 30s-60s before half-open
│   └── Use case: prevent cascading failures
├── Bulkhead
│   ├── Isolate resources: separate thread pools per service
│   ├── Limit concurrent requests: max 100 per user
│   └── Prevent: one slow service affecting others
├── Rate Limiting
│   ├── Token bucket: smooth traffic, allow bursts
│   ├── Leaky bucket: constant rate, drop excess
│   ├── Fixed window: simple but boundary issues
│   └── Sliding window: accurate but complex
├── Idempotency
│   ├── Idempotency key: UUID per request (24h TTL)
│   ├── Storage: Redis/DB with unique constraint
│   ├── Check before execution: if exists → return cached result
│   └── Critical for: payments, orders, emails
└── Graceful Degradation
    ├── Fallback: cache, default values, static content
    ├── Feature flags: disable non-critical features
    └── Priority: serve critical paths first
```

**💡 Code Example: Circuit Breaker**
```javascript
class CircuitBreaker {
  constructor(threshold = 0.5, timeout = 60000) {
    this.state = 'CLOSED';
    this.failures = 0;
    this.successes = 0;
    this.threshold = threshold;
    this.timeout = timeout;
  }

  async execute(fn) {
    if (this.state === 'OPEN') {
      if (Date.now() - this.openedAt > this.timeout) {
        this.state = 'HALF_OPEN';
      } else {
        throw new Error('Circuit breaker is OPEN');
      }
    }

    try {
      const result = await fn();
      this.onSuccess();
      return result;
    } catch (error) {
      this.onFailure();
      throw error;
    }
  }

  onSuccess() {
    this.failures = 0;
    if (this.state === 'HALF_OPEN') this.state = 'CLOSED';
  }

  onFailure() {
    this.failures++;
    const total = this.failures + this.successes;
    if (this.failures / total > this.threshold) {
      this.state = 'OPEN';
      this.openedAt = Date.now();
    }
  }
}
```

**🚨 Common Mistakes:**
- ❌ Retry non-idempotent operations (POST payment)
- ❌ No timeout → hanging requests forever
- ❌ Retry immediately without backoff → amplify load
- ❌ No circuit breaker → cascading failures

### **1.3 Code Quality & Architecture Hygiene** ⭐⭐⭐⭐

```
🏗️ ENGINEERING HYGIENE
├── Layering Architecture
│   ├── Controller: HTTP handling, validation, auth
│   ├── Service: business logic, orchestration
│   ├── Repository: data access, queries
│   └── Boundaries: no skip layers, clear interfaces
├── Clean Architecture / Hexagonal
│   ├── Core: domain entities, business rules (no deps)
│   ├── Ports: interfaces for external systems
│   ├── Adapters: HTTP controllers, DB repositories, external APIs
│   └── Dependency rule: inner layers don't depend on outer
├── SOLID Principles
│   ├── S: Single Responsibility (one reason to change)
│   ├── O: Open/Closed (extend, not modify)
│   ├── L: Liskov Substitution (subtype replaceable)
│   ├── I: Interface Segregation (small, focused interfaces)
│   └── D: Dependency Inversion (depend on abstractions)
├── Design Principles
│   ├── DRY: Don't Repeat Yourself (but avoid wrong abstractions)
│   ├── KISS: Keep It Simple, Stupid (simplest solution first)
│   ├── YAGNI: You Aren't Gonna Need It (no premature optimization)
│   └── Composition > Inheritance
├── Dependency Injection
│   ├── Constructor injection (preferred, testable)
│   ├── Property injection (optional dependencies)
│   ├── DI containers: NestJS, .NET, Spring
│   └── Avoid service locator anti-pattern
├── Configuration Management
│   ├── 12-factor app: config in env variables
│   ├── Secrets: external vault (AWS Secrets, HashiCorp)
│   ├── Environment: dev / staging / production
│   └── Feature flags: runtime behavior control
└── Refactoring Patterns
    ├── Strangler Fig: gradually replace legacy system
    ├── Anti-corruption Layer: translate legacy → new domain
    ├── Extract Service: split monolith incrementally
    └── Branch by Abstraction: safe large refactors
```

**💡 Code Example: Layered Architecture**
```typescript
// ❌ BAD: Business logic in controller
@Controller('orders')
class OrderController {
  @Post()
  async create(@Body() dto: CreateOrderDto) {
    // ⚠️ Direct DB access in controller!
    const product = await db.products.findOne(dto.productId);
    if (product.stock < dto.quantity) throw new Error('Out of stock');
    product.stock -= dto.quantity;
    await db.products.save(product);
    const order = await db.orders.create({ ...dto, status: 'PENDING' });
    await emailService.send(user.email, 'Order confirmation');
    return order;
  }
}

// ✅ GOOD: Proper layering
@Controller('orders')
class OrderController {
  constructor(private orderService: OrderService) {}
  
  @Post()
  async create(@Body() dto: CreateOrderDto) {
    return this.orderService.createOrder(dto);
  }
}

@Injectable()
class OrderService {
  constructor(
    private orderRepo: OrderRepository,
    private productRepo: ProductRepository,
    private emailService: EmailService
  ) {}
  
  async createOrder(dto: CreateOrderDto) {
    // Business logic here
    const product = await this.productRepo.findById(dto.productId);
    if (product.stock < dto.quantity) {
      throw new BusinessError('OUT_OF_STOCK');
    }
    
    await this.productRepo.decrementStock(dto.productId, dto.quantity);
    const order = await this.orderRepo.create(dto);
    await this.emailService.sendOrderConfirmation(order);
    
    return order;
  }
}
```

**⚖️ Trade-offs:**
| Pattern | Pros | Cons | When to Use |
|---------|------|------|-------------|
| **Layered** | Simple, clear separation | Can be over-engineered | Most web apps |
| **Hexagonal** | Highly testable, flexible | More boilerplate | Complex domains |
| **Monolith** | Simple deploy, no network | Scaling limits | Early stage, small team |
| **Microservices** | Independent scaling | Complexity, latency | Large teams, clear boundaries |

---

## 🟩 **2. EXPRESS.JS & API PATTERNS**
<!-- 🇻🇳 EXPRESS.JS - WEB FRAMEWORK PHỔ BIẾN NHẤT CỦA NODE.JS -->
<!-- Nội dung: Middleware, routing, validation, error handling -->

### **2.1 Express Middleware Architecture** ⭐⭐⭐⭐⭐
<!-- 🇻🇳 KIẾN TRÚC MIDDLEWARE - TIM ĐậP CỦA EXPRESS -->
<!-- Middleware = function chạy giữa request và response -->

```
🌐 EXPRESS MIDDLEWARE
<!-- 🇻🇳 MỖC XICH XỬ LÝ REQUEST - THỨ TỰ RẤT QUAN TRỌNG! -->
├── Middleware Execution Flow
│   <!-- Luồng chảy: top → bottom (app.use đầu tiên chạy trước) -->
│   ├── Order matters: top to bottom execution
│   │   <!-- 👉 THỨ TỰ QUẢN TRỌNG! Middleware ở trên chạy trước -->
│   │   <!-- Ví dụ: logger → parser → auth → business logic -->
│   ├── app.use(): applies to all routes
│   │   <!-- Áp dụng cho tất cả routes (VD: body parser, logger) -->
│   ├── router.use(): applies to specific router
│   │   <!-- Áp dụng cho 1 router cụ thể (VD: /api/admin router) -->
│   └── Route-level: app.get('/api', middleware, handler)
│       <!-- Áp dụng cho 1 route cụ thể: app.get('/admin', auth, handler) -->
├── Built-in Middleware
│   <!-- 🇻🇳 MIDDLEWARE TÍCH HỢP SẴN TRONG EXPRESS -->
│   ├── express.json(): parse JSON body
│   │   <!-- Parse request body dạng JSON: { "name": "John" } -->
│   │   <!-- 👉 Phải dùng trước khi truy cập req.body! -->
│   ├── express.urlencoded(): parse URL-encoded
│   │   <!-- Parse form data: name=John&age=25 -->
│   ├── express.static(): serve static files
│   │   <!-- Phục vụ file tĩnh (.html, .css, .js, images) -->
│   │   <!-- Ví dụ: app.use(express.static('public')) -->
│   └── express.Router(): modular routes
│       <!-- Tạo router module riêng (tổ chức code tốt hơn) -->
├── Popular Third-party Middleware
│   <!-- 🇻🇳 MIDDLEWARE PHỔ BIẾN TỪ NPM - NÊN DÙNG CHO PRODUCTION! -->
│   ├── helmet: security headers
│   │   <!-- Bảo mật: set headers chống XSS, clickjacking, etc. -->
│   │   <!-- 👉 LUÔN DÙNG TRONG PRODUCTION! -->
│   ├── cors: Cross-Origin Resource Sharing
│   │   <!-- Cho phép frontend khác domain gọi API -->
│   │   <!-- Ví dụ: frontend localhost:3000 gọi backend localhost:5000 -->
│   ├── morgan: HTTP request logger
│   │   <!-- Log mỗi request: GET /api/users 200 15ms -->
│   ├── compression: gzip compression
│   │   <!-- Nén response (giảm 70-80% size) -->
│   ├── express-rate-limit: rate limiting
│   │   <!-- Giới hạn số request (chống spam, DDoS) -->
│   │   <!-- Ví dụ: tối đa 100 request / 15 phút / IP -->
│   ├── express-validator: request validation
│   │   <!-- Validate input: kiểm tra email, phone, length, etc. -->
│   └── multer: file upload handling
│       <!-- Xử lý upload file (images, documents) -->
├── Middleware Patterns
│   <!-- 🇻🇳 CÁC MẪU MIDDLEWARE THƯỜNG DÙNG -->
│   ├── Error-handling middleware: 4 params (err, req, res, next)
│   │   <!-- 👉 ĐẶC BIỆT: PHẢI CÓ 4 THAM SỐ ĐỂ EXPRESS NHẬN DIỆN LÀ ERROR HANDLER! -->
│   │   <!-- function (err, req, res, next) { ... } -->
│   ├── Async middleware: use express-async-handler or try/catch
│   │   <!-- Xử lý async/await trong middleware -->
│   │   <!-- Phải bắc lỗi (catch) và gọi next(error) -->
│   ├── HOF middleware: middleware factory functions
│   │   <!-- Higher-Order Function: hàm trả về middleware -->
│   │   <!-- Ví dụ: authorize(roles: string[]) => middleware -->
│   └── Conditional middleware: based on env or config
│       <!-- Chạy middleware theo điều kiện -->
│       <!-- Ví dụ: chỉ enable morgan trong development -->
└── Best Practices
    <!-- 🇻🇳 QUY TẮC VÀNG KHI DÙNG MIDDLEWARE -->
    ├── Order: logging → parsing → rate limit → auth → business logic
    │   <!-- 👉 THỨ TỰ KHUYẾN NGHỊ CỦA EXPRESS -->
    │   <!-- 1. Log (morgan) 2. Parse body 3. Rate limit 4. Auth 5. Logic -->
    ├── Error handling: always use error middleware at end
    │   <!-- Error middleware LUÔN Ở CUỐI CÙNG! (sau tất cả routes) -->
    ├── next() vs next(err): continue vs error
    │   <!-- next(): tiếp tục middleware tiếp theo -->
    │   <!-- next(err): nhảy thẳng tới error handler -->
    └── Avoid blocking: async operations only
        <!-- ⚠️ KHÔNG chạy blocking code (VD: while(true), heavy sync computation) -->
```

**💡 Express Middleware Example:**
<!-- 🇻🇳 VÍ DỤ MIDDLEWARE THỰC TẾN -->
```typescript
// 1. Request ID middleware
// 🇻🇳 Tạo ID cho mỗi request để trace logs
import { v4 as uuid } from 'uuid';

const requestId = (req: Request, res: Response, next: NextFunction) => {
  // Sử dụng ID từ header hoặc tạo mới
  req.id = req.headers['x-request-id'] || uuid();
  // Trả ID về client trong response header
  res.setHeader('X-Request-ID', req.id);
  next(); // Tiếp tục middleware tiếp theo
};

// 2. Async error wrapper
// 🇻🇳 Wrapper để tự động catch lỗi async/await
const asyncHandler = (fn: Function) => {
  return (req: Request, res: Response, next: NextFunction) => {
    // Tự động catch error và chuyển đến error handler
    Promise.resolve(fn(req, res, next)).catch(next);
  };
};
// 👉 Dùng: app.get('/api/users', asyncHandler(async (req, res) => { ... }))

// 3. Authentication middleware
// 🇻🇳 Kiểm tra JWT token, load thông tin user
const authenticate = async (req: Request, res: Response, next: NextFunction) => {
  try {
    // Lấy token từ header: "Authorization: Bearer <token>"
    const token = req.headers.authorization?.split(' ')[1];
    if (!token) throw new UnauthorizedError('No token provided');
    
    // Verify token và giải mã
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    // Load user từ DB, gắn vào req.user
    req.user = await userService.findById(decoded.userId);
    next(); // Token hợp lệ, tiếp tục
  } catch (error) {
    next(error); // Token không hợp lệ, chuyển tới error handler
  }
};

// 4. Authorization middleware (HOF)
// 🇻🇳 Kiểm tra quyền (roles) - Higher Order Function
const authorize = (...roles: string[]) => {
  // Trả về middleware function
  return (req: Request, res: Response, next: NextFunction) => {
    // Kiểm tra đã authenticated chưa
    if (!req.user) {
      return next(new UnauthorizedError('Not authenticated'));
    }
    // Kiểm tra user có role phù hợp không
    if (!roles.includes(req.user.role)) {
      return next(new ForbiddenError('Insufficient permissions'));
    }
    next(); // Có quyền, tiếp tục
  };
};
// 👉 Dùng: app.delete('/admin/users', authenticate, authorize('ADMIN'), handler)

// 5. Error handling middleware
// 🇻🇳 Xử lý lỗi tập trung - ĐặT Ở CUỐI APP!
const errorHandler = (
  err: Error,        // 👉 4 tham số để Express nhận diện là error handler!
  req: Request,
  res: Response,
  next: NextFunction
) => {
  // Log lỗi với requestId để trace
  logger.error('Request failed', {
    error: err.message,
    stack: err.stack,
    requestId: req.id,
    path: req.path
  });

  // Trả lỗi về client
  const statusCode = err.statusCode || 500;
  res.status(statusCode).json({
    error: {
      message: err.message,
      code: err.code || 'INTERNAL_ERROR',
      requestId: req.id
    }
  });
};

// Application setup
const app = express();

// Middleware stack (order matters!)
app.use(requestId);                          // 1. Request context
app.use(morgan('combined'));                 // 2. Logging
app.use(helmet());                           // 3. Security headers
app.use(cors({ origin: ['https://app.com'] })); // 4. CORS
app.use(express.json({ limit: '10mb' }));   // 5. Body parsing
app.use(rateLimit({ max: 100, windowMs: 60000 })); // 6. Rate limiting

// Routes
app.get('/api/admin', 
  authenticate, 
  authorize('admin'), 
  asyncHandler(adminController.getData)
);

// Error handling (must be last!)
app.use(errorHandler);
```

### **2.2 Express Router & Controllers** ⭐⭐⭐⭐

```
🗂️ ROUTING & CONTROLLERS
├── Router Organization
│   ├── Feature-based: /routes/users.ts, /routes/orders.ts
│   ├── Version-based: /v1/users, /v2/users
│   └── Modular: express.Router() per domain
├── Controller Pattern
│   ├── Separation: routes handle routing, controllers handle logic
│   ├── Service layer: controllers call services (not DB directly)
│   └── Thin controllers: validation + call service + return response
├── Route Parameters
│   ├── Path params: /users/:id
│   ├── Query params: /users?page=1&limit=10
│   ├── Body: req.body (requires body parser)
│   └── Headers: req.headers
├── Response Patterns
│   ├── Success: res.status(200).json({ data })
│   ├── Created: res.status(201).json({ data })
│   ├── No content: res.status(204).send()
│   ├── Error: next(error) → error handler
│   └── Consistent envelope: { data, meta, error }
└── Validation
    ├── express-validator: chain validators
    ├── Zod: schema-based validation
    ├── Joi: alternative schema validator
    └── class-validator: decorator-based (TypeScript)
```

**💡 Express Router Example:**
```typescript
// routes/users.ts
import { Router } from 'express';
import { UserController } from '../controllers/user.controller';
import { authenticate, authorize } from '../middleware/auth';
import { validate } from '../middleware/validation';
import { createUserSchema, updateUserSchema } from '../schemas/user.schema';

const router = Router();
const userController = new UserController();

// GET /api/users
router.get('/', 
  authenticate,
  userController.getUsers
);

// POST /api/users
router.post('/',
  authenticate,
  authorize('admin'),
  validate(createUserSchema),
  userController.createUser
);

// GET /api/users/:id
router.get('/:id',
  authenticate,
  userController.getUserById
);

// PATCH /api/users/:id
router.patch('/:id',
  authenticate,
  validate(updateUserSchema),
  userController.updateUser
);

// DELETE /api/users/:id
router.delete('/:id',
  authenticate,
  authorize('admin'),
  userController.deleteUser
);

export default router;

// controllers/user.controller.ts
export class UserController {
  constructor(private userService: UserService) {}

  getUsers = asyncHandler(async (req: Request, res: Response) => {
    const { page = 1, limit = 10 } = req.query;
    const result = await this.userService.getUsers({ 
      page: Number(page), 
      limit: Number(limit) 
    });
    
    res.json({
      data: result.users,
      meta: {
        page: result.page,
        limit: result.limit,
        total: result.total
      }
    });
  });

  createUser = asyncHandler(async (req: Request, res: Response) => {
    const user = await this.userService.createUser(req.body);
    res.status(201).json({ data: user });
  });
  
  // ... other methods
}

// Validation with Zod
import { z } from 'zod';

const createUserSchema = z.object({
  body: z.object({
    email: z.string().email(),
    name: z.string().min(2).max(100),
    password: z.string().min(8),
    role: z.enum(['user', 'admin']).optional()
  })
});

const validate = (schema: ZodSchema) => {
  return (req: Request, res: Response, next: NextFunction) => {
    try {
      schema.parse({ body: req.body, query: req.query, params: req.params });
      next();
    } catch (error) {
      if (error instanceof z.ZodError) {
        res.status(400).json({
          error: {
            message: 'Validation failed',
            details: error.errors
          }
        });
      } else {
        next(error);
      }
    }
  };
};
```

---

## 🟦 **3. NESTJS ARCHITECTURE** ⭐⭐⭐⭐⭐
<!-- 🇻🇳 NESTJS - FRAMEWORK ENTERPRISE CHO NODE.JS -->
<!-- Opinionated framework: Angular-inspired, TypeScript-first, DI container mạnh mẽ -->

### **3.1 NestJS Core Concepts** ⭐⭐⭐⭐⭐
<!-- 🇻🇳 CÁC KHÁI NIỆM CỐT LÕI - NỀN TẢNG NESTJS -->

```
🎯 NESTJS FUNDAMENTALS
<!-- 🇻🇳 CƠ BẢN VỀ NESTJS - KIẾN TRÚC MODULAR VỚI DI -->
├── Architecture
│   <!-- Kiến trúc tổng quan -->
│   ├── Modular: @Module decorators organize code
│   │   <!-- 👉 Modular: Tổ chức code theo modules (UsersModule, OrdersModule) -->
│   │   <!-- Mỗi module quản lý 1 domain cụ thể -->
│   ├── DI Container: automatic dependency injection
│   │   <!-- 🇻🇳 DEPENDENCY INJECTION TỰ ĐỘNG - CORE CỦA NESTJS! -->
│   │   <!-- Tự động inject dependencies vào constructor -->
│   │   <!-- Ví dụ: constructor(private userService: UserService) {} -->
│   ├── Decorators: TypeScript decorators for metadata
│   │   <!-- Sử dụng decorators (@Controller, @Get, @Injectable) để metadata -->
│   └── Opinionated: enforces best practices
│       <!-- Opinionated: đưa ra cách làm chuẩn, bắt tuân theo patterns -->
│       <!-- Tốt cho teams lớn: mọi người code giống nhau -->
├── Building Blocks
│   <!-- 🇻🇳 7 THÀNH PHẦN CHÍNH CỦA NESTJS -->
│   ├── Controllers: handle HTTP requests (@Controller)
│   │   <!-- Nhận HTTP requests, gọi service, trả response -->
│   │   <!-- Ví dụ: @Controller('users') class UsersController {} -->
│   ├── Providers: services, repositories (@Injectable)
│   │   <!-- Business logic, data access -->
│   │   <!-- @Injectable() làm cho class có thể inject được -->
│   ├── Modules: organize related code (@Module)
│   │   <!-- Gộm controllers, providers lại thành module -->
│   ├── Middleware: Express-like middleware
│   │   <!-- Giống Express middleware (chạy trước Guards) -->
│   ├── Guards: authentication/authorization (@UseGuards)
│   │   <!-- 🇻🇳 BẢO VỆ ROUTES - KIỂM TRA AUTH, ROLES -->
│   │   <!-- Ví dụ: @UseGuards(JwtAuthGuard, RolesGuard) -->
│   ├── Interceptors: transform requests/responses (@UseInterceptors)
│   │   <!-- 🇻🇳 BIẾN ĐỔI REQUEST/RESPONSE -->
│   │   <!-- Ví dụ: logging, caching, transform response -->
│   ├── Pipes: validation/transformation (@UsePipes)
│   │   <!-- 🇻🇳 VALIDATE INPUT, BIẾN ĐỔI DATA -->
│   │   <!-- Ví dụ: ValidationPipe (class-validator), ParseIntPipe -->
│   └── Exception Filters: custom error handling (@Catch)
│       <!-- Xử lý lỗi tùy chỉnh -->
├── Execution Order
│   <!-- 🇻🇳 THỨ TỰ THỰC THI 7 BƯỚC - RẤT QUAN TRỌNG! -->
│   <!-- 👉 NHớ THỨ TỰ NÀY ĐỂ DEBUG VÀ DESIGN! -->
│   1. Middleware → 2. Guards → 3. Interceptors (before)
│   <!-- Bước 1-3: Xử lý TRƯỚC KHI vào controller -->
│   4. Pipes → 5. Controller Handler → 6. Interceptors (after)
│   <!-- Bước 4-6: Validate, xử lý, transform response -->
│   7. Exception Filters (if error)
│   <!-- Bước 7: Nếu có lỗi ở bất kỳ bước nào -->
│   <!-- Ví dụ: Request → LogMiddleware → AuthGuard → LogInterceptor → ValidationPipe → Controller → TransformInterceptor → Response -->
├── Dependency Injection
│   <!-- 🇻🇳 HỆ THỐNG DI - CORE CỦA NESTJS -->
│   ├── Scopes: SINGLETON (default), REQUEST, TRANSIENT
│   │   <!-- SINGLETON: 1 instance cho toàn app (mặc định, nhanh) -->
│   │   <!-- REQUEST: tạo instance mới mỗi request (cho request-specific data) -->
│   │   <!-- TRANSIENT: tạo instance mới mỗi lần inject (hiếm dùng) -->
│   ├── Custom providers: useClass, useValue, useFactory
│   ├── Injection tokens: string/symbol identifiers
│   └── Circular dependencies: forwardRef()
└── Module System
    ├── Feature modules: domain-specific (UsersModule)
    ├── Shared modules: reusable (DatabaseModule)
    ├── Dynamic modules: runtime configuration (forRoot, forFeature)
    └── Global modules: @Global() decorator
```

**💡 NestJS Module Example:**
```typescript
// users.module.ts
@Module({
  imports: [
    TypeOrmModule.forFeature([User]),  // Import User repository
    forwardRef(() => OrdersModule)     // Handle circular dependency
  ],
  controllers: [UsersController],
  providers: [
    UsersService,
    UsersRepository,
    {
      provide: 'USER_CACHE',
      useFactory: (redis: Redis) => new LRU({ max: 1000 }),
      inject: [Redis]
    }
  ],
  exports: [UsersService]  // Make available to other modules
})
export class UsersModule {}

// users.controller.ts
@Controller('users')
@UseGuards(JwtAuthGuard)              // Apply guard to all routes
@UseInterceptors(LoggingInterceptor)  // Log all requests
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  @Get()
  @UseGuards(RolesGuard)
  @Roles('admin')
  async findAll(@Query() query: PaginationDto) {
    return this.usersService.findAll(query);
  }

  @Post()
  @UsePipes(ValidationPipe)
  async create(@Body() createUserDto: CreateUserDto) {
    return this.usersService.create(createUserDto);
  }

  @Get(':id')
  async findOne(@Param('id', ParseIntPipe) id: number) {
    const user = await this.usersService.findOne(id);
    if (!user) throw new NotFoundException(`User ${id} not found`);
    return user;
  }
}

// users.service.ts
@Injectable()
export class UsersService {
  constructor(
    @InjectRepository(User)
    private usersRepository: Repository<User>,
    @Inject('USER_CACHE')
    private cache: LRU<number, User>
  ) {}

  async findAll(query: PaginationDto): Promise<PaginatedResult<User>> {
    const [users, total] = await this.usersRepository.findAndCount({
      skip: (query.page - 1) * query.limit,
      take: query.limit
    });

    return { users, total, page: query.page, limit: query.limit };
  }

  async findOne(id: number): Promise<User> {
    // Check cache
    const cached = this.cache.get(id);
    if (cached) return cached;

    // Query database
    const user = await this.usersRepository.findOne({ where: { id } });
    if (user) this.cache.set(id, user);
    
    return user;
  }
}
```

### **3.2 NestJS Guards & Authorization** ⭐⭐⭐⭐⭐

```
🛡️ GUARDS & AUTHORIZATION
├── Guards (CanActivate interface)
│   ├── Purpose: determine if request should be handled
│   ├── Use cases: authentication, authorization, feature flags
│   ├── Return: boolean or Promise<boolean>
│   └── Applied: @UseGuards(), globally, or per controller/route
├── Common Guard Patterns
│   ├── JWT Auth Guard: verify token, attach user to request
│   ├── Roles Guard: check user.role against @Roles()
│   ├── API Key Guard: validate X-API-Key header
│   └── Rate Limit Guard: throttle requests per user/IP
├── Execution Context
│   ├── Access request: context.switchToHttp().getRequest()
│   ├── Access handler: context.getHandler()
│   ├── Metadata: Reflector service reads decorator metadata
│   └── Works with: HTTP, WebSocket, Microservices
└── Best Practices
    ├── Guard order: Auth → Authorization → Business logic
    ├── Global guards: apply to all routes
    ├── Skip guards: use @Public() decorator pattern
    └── Throw exceptions: UnauthorizedException, ForbiddenException
```

**💡 NestJS Guards Example:**
```typescript
// auth.guard.ts (JWT Authentication)
@Injectable()
export class JwtAuthGuard implements CanActivate {
  constructor(
    private readonly jwtService: JwtService,
    private readonly userService: UserService
  ) {}

  async canActivate(context: ExecutionContext): Promise<boolean> {
    const request = context.switchToHttp().getRequest();
    const token = this.extractToken(request);

    if (!token) {
      throw new UnauthorizedException('No token provided');
    }

    try {
      const payload = await this.jwtService.verifyAsync(token);
      const user = await this.userService.findById(payload.sub);
      
      if (!user) {
        throw new UnauthorizedException('User not found');
      }

      request.user = user;  // Attach user to request
      return true;
    } catch (error) {
      throw new UnauthorizedException('Invalid token');
    }
  }

  private extractToken(request: Request): string | undefined {
    const [type, token] = request.headers.authorization?.split(' ') ?? [];
    return type === 'Bearer' ? token : undefined;
  }
}

// roles.guard.ts (Authorization)
@Injectable()
export class RolesGuard implements CanActivate {
  constructor(private reflector: Reflector) {}

  canActivate(context: ExecutionContext): boolean {
    // Get required roles from @Roles() decorator
    const requiredRoles = this.reflector.getAllAndOverride<string[]>('roles', [
      context.getHandler(),
      context.getClass()
    ]);

    if (!requiredRoles) {
      return true;  // No roles required
    }

    const request = context.switchToHttp().getRequest();
    const user = request.user;

    if (!user) {
      throw new UnauthorizedException('User not authenticated');
    }

    const hasRole = requiredRoles.some(role => user.role === role);
    if (!hasRole) {
      throw new ForbiddenException('Insufficient permissions');
    }

    return true;
  }
}

// Decorator for specifying required roles
export const Roles = (...roles: string[]) => SetMetadata('roles', roles);

// Public decorator (skip guards)
export const IS_PUBLIC_KEY = 'isPublic';
export const Public = () => SetMetadata(IS_PUBLIC_KEY, true);

// Usage in controller
@Controller('admin')
@UseGuards(JwtAuthGuard, RolesGuard)
export class AdminController {
  @Get('dashboard')
  @Roles('admin')
  getDashboard() {
    return { message: 'Admin dashboard' };
  }

  @Get('settings')
  @Roles('admin', 'superadmin')
  getSettings() {
    return { message: 'Settings' };
  }
}

// Global guard application (main.ts)
const app = await NestFactory.create(AppModule);
app.useGlobalGuards(
  new JwtAuthGuard(app.get(JwtService), app.get(UserService))
);
```

```
🌐 HTTP
├── Methods, status codes, headers (Cache-Control, ETag, CORS)
├── Keep-alive, connection reuse, timeouts
├── Compression (gzip/br), streaming, chunked encoding
├── Pagination: offset vs cursor; sorting/filtering
└── Error responses: problem+json, consistent envelopes
### **3.3 NestJS Interceptors & Pipes** ⭐⭐⭐⭐

```
🔄 INTERCEPTORS
├── Purpose
│   ├── Transform response/request data
│   ├── Add extra logic (logging, caching, timing)
│   ├── Handle errors
│   └── Override returned value
├── Execution
│   ├── Before handler: transform input
│   ├── After handler: transform output (Observable/Promise)
│   └── Error handling: catch and transform errors
├── Common Use Cases
│   ├── Response transformation: wrap in { data, meta }
│   ├── Logging: log request/response
│   ├── Caching: cache-aside pattern
│   ├── Timeout: abort slow requests
│   └── Performance: measure execution time
└── RxJS Integration
    ├── Uses Observable/pipe
    ├── Operators: map, catchError, timeout, tap
    └── Composition: chain multiple interceptors
```

**💡 NestJS Interceptors Example:**
```typescript
// logging.interceptor.ts
@Injectable()
export class LoggingInterceptor implements NestInterceptor {
  constructor(private readonly logger: Logger) {}

  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    const request = context.switchToHttp().getRequest();
    const { method, url } = request;
    const start = Date.now();

    return next.handle().pipe(
      tap(() => {
        const duration = Date.now() - start;
        this.logger.log(`${method} ${url} ${duration}ms`);
      }),
      catchError(err => {
        const duration = Date.now() - start;
        this.logger.error(`${method} ${url} ${duration}ms - Error: ${err.message}`);
        throw err;
      })
    );
  }
}

// transform.interceptor.ts (Wrap response)
@Injectable()
export class TransformInterceptor<T> implements NestInterceptor<T, Response<T>> {
  intercept(context: ExecutionContext, next: CallHandler): Observable<Response<T>> {
    return next.handle().pipe(
      map(data => ({
        data,
        meta: {
          timestamp: new Date().toISOString(),
          path: context.switchToHttp().getRequest().url
        }
      }))
    );
  }
}

// cache.interceptor.ts (Caching)
@Injectable()
export class CacheInterceptor implements NestInterceptor {
  constructor(@Inject(CACHE_MANAGER) private cacheManager: Cache) {}

  async intercept(context: ExecutionContext, next: CallHandler): Promise<Observable<any>> {
    const request = context.switchToHttp().getRequest();
    const cacheKey = `cache:${request.url}`;

    // Check cache
    const cached = await this.cacheManager.get(cacheKey);
    if (cached) {
      return of(cached);  // Return cached value
    }

    // Call handler and cache result
    return next.handle().pipe(
      tap(async (data) => {
        await this.cacheManager.set(cacheKey, data, 300); // 5 min TTL
      })
    );
  }
}

// timeout.interceptor.ts (Abort slow requests)
@Injectable()
export class TimeoutInterceptor implements NestInterceptor {
  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    return next.handle().pipe(
      timeout(5000),  // 5 second timeout
      catchError(err => {
        if (err.name === 'TimeoutError') {
          throw new RequestTimeoutException('Request timeout');
        }
        throw err;
      })
    );
  }
}

// Apply globally
app.useGlobalInterceptors(
  new LoggingInterceptor(logger),
  new TransformInterceptor(),
  new TimeoutInterceptor()
);
```

```
🔧 PIPES
├── Purpose
│   ├── Transformation: convert input data types
│   ├── Validation: validate input format/values
│   └── Throw exception if validation fails
├── Built-in Pipes
│   ├── ValidationPipe: validate DTOs with class-validator
│   ├── ParseIntPipe: convert string to number
│   ├── ParseBoolPipe: convert string to boolean
│   ├── ParseUUIDPipe: validate UUID format
│   └── DefaultValuePipe: set default if undefined
├── Scope
│   ├── Global: app.useGlobalPipes()
│   ├── Controller: @UsePipes() at class level
│   ├── Route: @UsePipes() at method level
│   └── Param: @Param('id', ParseIntPipe)
├── ValidationPipe Options
│   ├── whitelist: strip unknown properties
│   ├── forbidNonWhitelisted: throw error on unknown props
│   ├── transform: auto-transform to DTO class
│   └── transformOptions: class-transformer options
└── Custom Pipes
    ├── Implement PipeTransform interface
    ├── transform(value, metadata): perform logic
    └── Use cases: custom validation, sanitization
```

**💡 NestJS Pipes Example:**
```typescript
// DTOs with validation (class-validator)
import { IsEmail, IsString, MinLength, IsEnum } from 'class-validator';

export class CreateUserDto {
  @IsEmail()
  email: string;

  @IsString()
  @MinLength(2)
  name: string;

  @IsString()
  @MinLength(8)
  password: string;

  @IsEnum(['user', 'admin'])
  role: string;
}

// Controller with ValidationPipe
@Controller('users')
export class UsersController {
  @Post()
  @UsePipes(new ValidationPipe({ whitelist: true, forbidNonWhitelisted: true }))
  create(@Body() createUserDto: CreateUserDto) {
    // DTO is validated and transformed
    return this.usersService.create(createUserDto);
  }

  @Get(':id')
  findOne(@Param('id', ParseIntPipe) id: number) {
    // 'id' is automatically converted to number
    return this.usersService.findOne(id);
  }
}

// Custom validation pipe
@Injectable()
export class ParseObjectIdPipe implements PipeTransform<string, ObjectId> {
  transform(value: string, metadata: ArgumentMetadata): ObjectId {
    if (!ObjectId.isValid(value)) {
      throw new BadRequestException('Invalid ObjectId');
    }
    return new ObjectId(value);
  }
}

// Usage
@Get(':id')
findOne(@Param('id', ParseObjectIdPipe) id: ObjectId) {
  return this.usersService.findOne(id);
}

// Global ValidationPipe setup (main.ts)
app.useGlobalPipes(
  new ValidationPipe({
    whitelist: true,              // Remove unknown properties
    forbidNonWhitelisted: true,   // Throw error on unknown props
    transform: true,              // Auto-transform to DTO class
    transformOptions: {
      enableImplicitConversion: true  // Convert types automatically
    }
  })
);
```

---

## 🟨 **4. DATA LAYER - TypeORM & Prisma**

### **4.1 TypeORM Patterns** ⭐⭐⭐⭐⭐

```
🧾 API DESIGN
├── Resource modeling: nouns, relations
├── Versioning strategies (URI/header/compat)
├── Backward compatibility & deprecation
├── OpenAPI/Swagger, schema evolution
└── Contract testing (consumer-driven)
```

### **2.3 Networking Basics (DNS/TLS/TCP) cho Production** ⭐⭐⭐⭐

```
🔐 NETWORKING
├── DNS resolution & caching
├── TLS handshake, certs, mTLS, pinning (concept)
├── TCP basics: congestion, retries, time-wait
└── Load balancers: L4 vs L7, sticky sessions
```

### **2.4 AuthN/AuthZ** ⭐⭐⭐⭐⭐

```
🔑 AUTH
├── Sessions vs JWT; refresh token rotation
├── OAuth2/OIDC: auth code flow, PKCE
├── RBAC/ABAC, scopes/permissions
├── API keys, HMAC signatures, request signing
└── Multi-tenant patterns & data isolation
```

---

## 🟨 **3. DATA LAYER & CONSISTENCY**

### **4.1 TypeORM Patterns** ⭐⭐⭐⭐⭐

```
🗄️ TYPEORM
├── Entity Definition
│   ├── @Entity(): define table
│   ├── @Column(): table columns with types
│   ├── @PrimaryGeneratedColumn(): auto-increment ID
│   ├── @CreateDateColumn(), @UpdateDateColumn(): auto timestamps
│   ├── @Index(): database indexes
│   └── @VersionColumn(): optimistic locking
├── Relationships
│   ├── @OneToOne(): user ↔ profile
│   ├── @OneToMany() / @ManyToOne(): user → posts
│   ├── @ManyToMany(): posts ↔ tags (join table)
│   ├── Eager loading: { eager: true }
│   └── Lazy loading: Promise<Relation[]>
├── Repository Pattern
│   ├── Repository<Entity>: basic CRUD
│   ├── Custom repository: @EntityRepository() (deprecated)
│   ├── QueryBuilder: complex queries
│   ├── Raw SQL: manager.query() when needed
│   └── Transactions: manager.transaction()
├── Query Optimization
│   ├── Eager loading: avoid N+1 (find with relations)
│   ├── QueryBuilder: fine-grained control
│   ├── Select specific columns: .select(['field1', 'field2'])
│   ├── Indexes: @Index() on frequently queried columns
│   └── Explain queries: enable logging
├── Migrations
│   ├── Generate: typeorm migration:generate
│   ├── Run: typeorm migration:run
│   ├── Revert: typeorm migration:revert
│   └── Zero-downtime: add column (nullable) → backfill → NOT NULL
└── Best Practices
    ├── Use transactions for multi-table writes
    ├── Avoid circular dependencies in relations
    ├── Index foreign keys
    └── Paginate large queries
```

**💡 TypeORM Entity Example:**
```typescript
// entities/user.entity.ts
@Entity('users')
@Index(['email'])  // Index on email for fast lookups
export class User {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ unique: true })
  email: string;

  @Column()
  name: string;

  @Column({ select: false })  // Exclude from default queries
  password: string;

  @Column({ type: 'enum', enum: ['user', 'admin'], default: 'user' })
  role: string;

  @CreateDateColumn()
  createdAt: Date;

  @UpdateDateColumn()
  updatedAt: Date;

  @VersionColumn()  // Optimistic locking
  version: number;

  // Relations
  @OneToMany(() => Post, post => post.author)
  posts: Post[];

  @OneToOne(() => Profile, profile => profile.user, { cascade: true })
  @JoinColumn()
  profile: Profile;
}

// entities/post.entity.ts
@Entity('posts')
@Index(['authorId', 'status'])  // Composite index
export class Post {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  title: string;

  @Column('text')
  content: string;

  @Column({ type: 'enum', enum: ['draft', 'published'], default: 'draft' })
  status: string;

  @ManyToOne(() => User, user => user.posts, { onDelete: 'CASCADE' })
  author: User;

  @Column()
  authorId: number;

  @ManyToMany(() => Tag, tag => tag.posts)
  @JoinTable()
  tags: Tag[];

  @CreateDateColumn()
  createdAt: Date;
}

// NestJS TypeORM Module setup
@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'postgres',
      host: process.env.DB_HOST,
      port: 5432,
      username: process.env.DB_USER,
      password: process.env.DB_PASSWORD,
      database: process.env.DB_NAME,
      entities: [__dirname + '/**/*.entity{.ts,.js}'],
      synchronize: false,  // Never true in production!
      logging: process.env.NODE_ENV === 'development',
      migrations: [__dirname + '/migrations/**/*{.ts,.js}'],
      migrationsRun: true
    }),
    TypeOrmModule.forFeature([User, Post, Tag])
  ]
})
export class AppModule {}

// Repository usage in service
@Injectable()
export class UsersService {
  constructor(
    @InjectRepository(User)
    private usersRepository: Repository<User>
  ) {}

  // ❌ N+1 Problem
  async getUsersWithPosts_Bad() {
    const users = await this.usersRepository.find();  // 1 query
    for (const user of users) {
      user.posts = await this.postsRepository.find({ where: { authorId: user.id } });  // N queries!
    }
    return users;
  }

  // ✅ Eager loading with relations
  async getUsersWithPosts_Good() {
    return this.usersRepository.find({
      relations: ['posts', 'profile']  // JOIN in single query
    });
  }

  // ✅ QueryBuilder for complex queries
  async searchUsers(query: string) {
    return this.usersRepository
      .createQueryBuilder('user')
      .leftJoinAndSelect('user.posts', 'posts')
      .where('user.name ILIKE :query', { query: `%${query}%` })
      .orWhere('user.email ILIKE :query', { query: `%${query}%` })
      .orderBy('user.createdAt', 'DESC')
      .take(20)
      .getMany();
  }

  // ✅ Transaction example
  async createUserWithProfile(data: CreateUserDto) {
    return this.usersRepository.manager.transaction(async manager => {
      const user = manager.create(User, {
        email: data.email,
        name: data.name,
        password: await bcrypt.hash(data.password, 10)
      });
      await manager.save(user);

      const profile = manager.create(Profile, {
        userId: user.id,
        bio: data.bio
      });
      await manager.save(profile);

      return user;
    });
  }

  // ✅ Optimistic locking
  async updateUser(id: number, data: UpdateUserDto, version: number) {
    const result = await this.usersRepository.update(
      { id, version },  // Check version
      { ...data }
    );

    if (result.affected === 0) {
      throw new ConflictException('User was modified by another request');
    }

    return this.usersRepository.findOne({ where: { id } });
  }
}
```

### **4.2 Prisma ORM (Modern Alternative)** ⭐⭐⭐⭐

```
💎 PRISMA
├── Schema-first Design
│   ├── schema.prisma: define models in Prisma Schema Language
│   ├── Prisma Client: auto-generated, type-safe client
│   ├── Migrations: prisma migrate dev
│   └── Introspection: reverse engineer from DB
├── Prisma Client Features
│   ├── Type-safe queries: full TypeScript support
│   ├── Auto-completion: IDE support
│   ├── Relation queries: nested reads/writes
│   ├── Transactions: $transaction() API
│   └── Middleware: intercept queries
├── Advantages over TypeORM
│   ├── Better DX: schema in one file, instant type updates
│   ├── Faster: optimized queries
│   ├── Type-safe: compile-time errors
│   └── Modern: active development, good docs
├── Prisma vs TypeORM
│   ├── Prisma: schema-first, newer, better DX
│   ├── TypeORM: code-first, mature, more features
│   └── Choice: Prisma for new projects, TypeORM if existing
└── Best Practices
    ├── Use Prisma Studio for data exploration
    ├── Enable query logging in development
    ├── Use $queryRaw for complex queries
    └── Batch operations with createMany()
```

**💡 Prisma Example:**
```prisma
// prisma/schema.prisma
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

generator client {
  provider = "prisma-client-js"
}

model User {
  id        Int      @id @default(autoincrement())
  email     String   @unique
  name      String
  password  String
  role      Role     @default(USER)
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt

  posts   Post[]
  profile Profile?

  @@index([email])
}

model Post {
  id        Int      @id @default(autoincrement())
  title     String
  content   String
  status    PostStatus @default(DRAFT)
  authorId  Int
  createdAt DateTime @default(now())

  author User   @relation(fields: [authorId], references: [id], onDelete: Cascade)
  tags   Tag[]

  @@index([authorId, status])
}

model Profile {
  id     Int    @id @default(autoincrement())
  bio    String?
  userId Int    @unique
  user   User   @relation(fields: [userId], references: [id])
}

model Tag {
  id    Int    @id @default(autoincrement())
  name  String @unique
  posts Post[]
}

enum Role {
  USER
  ADMIN
}

enum PostStatus {
  DRAFT
  PUBLISHED
}
```

```typescript
// NestJS Prisma Service
@Injectable()
export class PrismaService extends PrismaClient implements OnModuleInit {
  async onModuleInit() {
    await this.$connect();
  }

  async enableShutdownHooks(app: INestApplication) {
    this.$on('beforeExit', async () => {
      await app.close();
    });
  }
}

// Usage in service
@Injectable()
export class UsersService {
  constructor(private prisma: PrismaService) {}

  // ✅ Type-safe query with relations
  async getUsersWithPosts() {
    return this.prisma.user.findMany({
      include: {
        posts: true,
        profile: true
      }
    });
  }

  // ✅ Nested writes
  async createUserWithProfile(data: CreateUserDto) {
    return this.prisma.user.create({
      data: {
        email: data.email,
        name: data.name,
        password: await bcrypt.hash(data.password, 10),
        profile: {
          create: {
            bio: data.bio
          }
        }
      },
      include: {
        profile: true
      }
    });
  }

  // ✅ Transaction
  async transferPost(postId: number, newAuthorId: number) {
    return this.prisma.$transaction(async (tx) => {
      const post = await tx.post.findUnique({ where: { id: postId } });
      if (!post) throw new NotFoundException();

      await tx.post.update({
        where: { id: postId },
        data: { authorId: newAuthorId }
      });

      await tx.user.update({
        where: { id: newAuthorId },
        data: { /* ... */ }
      });
    });
  }

  // ✅ Raw SQL when needed
  async complexQuery(params: any) {
    return this.prisma.$queryRaw`
      SELECT u.*, COUNT(p.id) as post_count
      FROM "User" u
      LEFT JOIN "Post" p ON p."authorId" = u.id
      WHERE u.role = ${params.role}
      GROUP BY u.id
      HAVING COUNT(p.id) > ${params.minPosts}
    `;
  }

  // ✅ Batch operations
  async createManyUsers(users: CreateUserDto[]) {
    return this.prisma.user.createMany({
      data: users,
      skipDuplicates: true  // Skip on unique constraint violation
    });
  }
}
```

**⚖️ TypeORM vs Prisma Comparison:**
| Feature | TypeORM | Prisma |
|---------|---------|--------|
| **Approach** | Code-first (decorators) | Schema-first (schema.prisma) |
| **Type Safety** | Good (manual typing) | Excellent (auto-generated) |
| **DX** | Moderate | Excellent |
| **Performance** | Good | Excellent (optimized) |
| **Migrations** | Auto-generate or manual | Declarative migrations |
| **Learning Curve** | Steeper | Easier |
| **Maturity** | Mature (since 2016) | Newer (since 2019) |
| **Community** | Large | Growing fast |
| **Best For** | Existing projects, complex queries | New projects, fast development |

```
🗄️ SQL
├── Data Modeling
│   ├── Normalization: 1NF, 2NF, 3NF (eliminate redundancy)
│   ├── Denormalization: when read >> write (trade-off)
│   ├── Constraints: PK, FK, UNIQUE, CHECK, NOT NULL
│   └── Data types: size matters (int vs bigint, varchar length)
├── Indexes
│   ├── B-tree: default, range queries, sorting (95% use case)
│   ├── Hash: equality only (WHERE id = 123)
│   ├── GIN/GiST: full-text search, JSON, arrays
│   ├── Composite index: (col1, col2) → leftmost prefix rule
│   ├── Covering index: include all query columns → no table lookup
│   ├── Partial index: WHERE condition (filtered)
│   ├── Selectivity: high selectivity → better index
│   └── Trade-offs: faster reads, slower writes, storage cost
├── Query Optimization
│   ├── EXPLAIN ANALYZE: actual execution time
│   ├── Seq Scan vs Index Scan: small table → seq scan faster
│   ├── Index Scan vs Bitmap Scan: multiple conditions
│   ├── Hotspots: identify slow queries (pg_stat_statements)
│   └── Query hints: force index (USE INDEX, FORCE INDEX)
├── N+1 Problem
│   ├── Symptom: 1 query + N queries per row
│   ├── Solution 1: Eager loading (JOIN)
│   ├── Solution 2: Batch loading (WHERE id IN (...))
│   ├── Solution 3: DataLoader (GraphQL)
│   └── Always check: query count in logs
├── Joins
│   ├── INNER JOIN: only matching rows
│   ├── LEFT JOIN: all left + matching right
│   ├── Subquery vs JOIN: usually JOIN faster
│   └── Join order: optimizer decides, but can hint
├── Pagination
│   ├── Offset-based: LIMIT 20 OFFSET 1000 → slow for large offset
│   ├── Cursor-based: WHERE id > last_id LIMIT 20 → fast, consistent
│   ├── Keyset pagination: ORDER BY created_at, id
│   └── Problem: offset deep pages → full table scan
└── Migrations
    ├── Zero-downtime: add column (nullable) → deploy → backfill → make NOT NULL
    ├── Backward compatible: old code works during deploy
    ├── Rename column: add new → copy data → remove old (multi-step)
    └── Tools: Flyway, Liquibase, TypeORM migrations
```

**💡 N+1 Problem Example:**
```typescript
// ❌ BAD: N+1 queries (1 + 100 = 101 queries)
async getPosts() {
  const posts = await db.posts.findAll(); // 1 query
  for (const post of posts) {
    post.author = await db.users.findOne(post.authorId); // N queries!
  }
  return posts;
}

// ✅ SOLUTION 1: JOIN (1 query)
async getPosts() {
  return db.posts.findAll({
    include: [{ model: User, as: 'author' }]
  });
}
// SQL: SELECT posts.*, users.* FROM posts LEFT JOIN users ON posts.author_id = users.id

// ✅ SOLUTION 2: Batch load (2 queries)
async getPosts() {
  const posts = await db.posts.findAll();
  const authorIds = posts.map(p => p.authorId);
  const authors = await db.users.findAll({ where: { id: authorIds } });
  const authorMap = new Map(authors.map(a => [a.id, a]));
  posts.forEach(p => p.author = authorMap.get(p.authorId));
  return posts;
}
```

**📊 Index Performance:**
```sql
-- Without index: 2000ms (full table scan)
SELECT * FROM products WHERE category_id = 5 AND price < 100;

-- With index on category_id: 500ms
CREATE INDEX idx_category ON products (category_id);

-- With composite index: 10ms ✅
CREATE INDEX idx_category_price ON products (category_id, price);

-- Query plan:
EXPLAIN ANALYZE
SELECT * FROM products WHERE category_id = 5 AND price < 100;
-- Index Scan using idx_category_price (cost=0.42..8.44 rows=1 width=100)
```

**🚨 Common Mistakes:**
- ❌ No indexes on foreign keys → slow JOINs
- ❌ SELECT * → fetch unnecessary columns
- ❌ Too many indexes → slow INSERT/UPDATE
- ❌ Function in WHERE → index not used: WHERE LOWER(email) = 'test@example.com'
- ✅ Fix: CREATE INDEX idx_email_lower ON users (LOWER(email));

### **3.2 Transactions, Isolation, Locks, Deadlocks** ⭐⭐⭐⭐⭐

```
🔒 CONSISTENCY
├── ACID Properties
│   ├── Atomicity: all or nothing (rollback on failure)
│   ├── Consistency: valid state transitions (constraints)
│   ├── Isolation: concurrent txs don't interfere
│   └── Durability: committed data persists (WAL)
├── Isolation Levels (low → high)
│   ├── READ UNCOMMITTED: dirty reads possible (rarely used)
│   ├── READ COMMITTED: default in Postgres, prevents dirty reads
│   ├── REPEATABLE READ: default in MySQL, prevents non-repeatable reads
│   ├── SERIALIZABLE: strongest, prevents all anomalies (slow)
│   └── Trade-off: higher isolation = lower concurrency
├── Anomalies
│   ├── Dirty Read: read uncommitted data
│   ├── Non-repeatable Read: data changes between reads in same tx
│   ├── Phantom Read: new rows appear in same query
│   └── Lost Update: concurrent updates overwrite each other
├── Locking Strategies
│   ├── Pessimistic Lock: lock before read (SELECT FOR UPDATE)
│   │   ├── Pros: prevents conflicts
│   │   └── Cons: blocking, deadlock risk
│   ├── Optimistic Lock: version column, check before commit
│   │   ├── Pros: high concurrency, no blocking
│   │   └── Cons: retry logic needed, wasted work
│   ├── Row-level Lock: lock specific rows (default in Postgres)
│   └── Table-level Lock: lock entire table (rare, DDL operations)
├── Deadlocks
│   ├── Cause: circular wait (tx1 locks A → tx2 locks B → tx1 waits B → tx2 waits A)
│   ├── Detection: DB automatically detects, aborts one tx
│   ├── Prevention: always acquire locks in same order
│   └── Mitigation: retry with exponential backoff
├── Distributed Transactions
│   ├── 2PC (Two-Phase Commit): coordinator + participants
│   │   ├── Pros: ACID guarantees
│   │   └── Cons: blocking, single point of failure
│   ├── Saga Pattern: sequence of local transactions + compensations
│   │   ├── Choreography: event-driven, no coordinator
│   │   ├── Orchestration: central coordinator
│   │   └── Trade-off: eventual consistency
│   └── Outbox Pattern: transactional messaging
│       ├── Insert to DB + outbox table in same tx
│       ├── Background job polls outbox → publish event
│       └── Guarantees: at-least-once delivery
└── Eventual Consistency
    ├── Definition: system eventually reaches consistent state
    ├── Use case: distributed systems, high availability
    ├── Conflict resolution: last-write-wins, CRDT
    └── Trade-off: CAP theorem (choose 2 of 3: C, A, P)
```

**💡 Pessimistic vs Optimistic Locking:**
```typescript
// ❌ RACE CONDITION: Two users buy last item (stock = 1)
async checkout(productId: number) {
  const product = await db.products.findOne(productId);
  if (product.stock < 1) throw new Error('Out of stock');
  product.stock -= 1;
  await db.products.save(product);
}
// Result: Both pass check, stock = -1 (oversold!)

// ✅ PESSIMISTIC LOCK: Block other transactions
async checkout(productId: number) {
  return db.transaction(async (tx) => {
    const product = await tx.products.findOne({
      where: { id: productId },
      lock: 'FOR UPDATE' // ← Locks row
    });
    if (product.stock < 1) throw new Error('Out of stock');
    product.stock -= 1;
    await tx.products.save(product);
  });
}

// ✅ OPTIMISTIC LOCK: Version check
@Entity()
class Product {
  @Column() stock: number;
  @Version() version: number; // ← Auto-incremented
}

async checkout(productId: number) {
  const product = await db.products.findOne(productId);
  if (product.stock < 1) throw new Error('Out of stock');
  product.stock -= 1;
  try {
    await db.products.save(product); // Checks version automatically
  } catch (error) {
    if (error.name === 'OptimisticLockError') {
      // Retry with fresh data
      return this.checkout(productId);
    }
    throw error;
  }
}

// ✅ ATOMIC UPDATE: Best for high concurrency
async checkout(productId: number) {
  const result = await db.query(
    'UPDATE products SET stock = stock - 1 WHERE id = $1 AND stock > 0 RETURNING *',
    [productId]
  );
  if (result.rows.length === 0) throw new Error('Out of stock');
  return result.rows[0];
}
```

**📊 Isolation Level Comparison:**
| Level | Dirty Read | Non-repeatable | Phantom | Performance |
|-------|------------|----------------|---------|-------------|
| READ UNCOMMITTED | ✗ | ✗ | ✗ | Highest |
| READ COMMITTED | ✓ | ✗ | ✗ | High |
| REPEATABLE READ | ✓ | ✓ | ✗ | Medium |
| SERIALIZABLE | ✓ | ✓ | ✓ | Lowest |

### **3.3 NoSQL & Specialized Storage** ⭐⭐⭐⭐

```
📦 NOSQL & STORAGE
├── Key-value (Redis), document (Mongo), wide-column (Cassandra)
├── Search (Elasticsearch/OpenSearch)
├── Time-series (Prometheus/Timescale), OLAP (ClickHouse/BigQuery)
└── Khi nào dùng gì: trade-offs & failure modes
```

### **3.4 Replication, Sharding, Backup/Restore** ⭐⭐⭐⭐

```
🧬 SCALE DATA
├── Replication (sync/async), read replicas
├── Sharding strategies & rebalancing
├── PITR, backup strategy, DR (RPO/RTO)
└── Data retention & archival
```

---

## 🟧 **4. CACHE & MESSAGING**

### **4.1 Caching (Redis) & Cache Invalidation** ⭐⭐⭐⭐⭐

```
⚡ CACHE
├── Caching Strategies
│   ├── Cache-Aside (Lazy Loading)
│   │   ├── Read: check cache → miss → query DB → save to cache
│   │   ├── Write: update DB → invalidate cache
│   │   ├── Pros: only cache accessed data
│   │   └── Cons: cache miss penalty, stale data
│   ├── Read-Through
│   │   ├── Cache library handles DB read automatically
│   │   └── Pros: simplified code
│   ├── Write-Through
│   │   ├── Write: update cache + DB synchronously
│   │   ├── Pros: cache always fresh
│   │   └── Cons: write latency, unnecessary cache writes
│   ├── Write-Behind (Write-Back)
│   │   ├── Write: update cache → async write to DB
│   │   ├── Pros: fast writes, batch DB updates
│   │   └── Cons: data loss risk if cache fails
│   └── Refresh-Ahead
│       ├── Proactively refresh cache before expiration
│       └── Use case: predictable access patterns
├── Cache Eviction Policies
│   ├── LRU (Least Recently Used): evict oldest access
│   ├── LFU (Least Frequently Used): evict least accessed
│   ├── TTL (Time To Live): expire after duration
│   └── Redis default: noeviction, allkeys-lru, volatile-lru
├── Cache Invalidation
│   ├── TTL-based: simple but stale data possible
│   ├── Event-based: DB trigger → invalidate on write
│   ├── Cache tagging: group related keys, invalidate together
│   ├── Versioning: cache_v2:product:123 (force invalidate all)
│   └── Manual: DEL key on update (most common)
├── Cache Problems
│   ├── Cache Stampede (Thundering Herd)
│   │   ├── Problem: cache expires → 1000 requests hit DB simultaneously
│   │   ├── Solution 1: Distributed lock (Redlock)
│   │   ├── Solution 2: Probabilistic early expiration
│   │   └── Solution 3: Stale-While-Revalidate (serve stale + async refresh)
│   ├── Hot Key
│   │   ├── Problem: single key → 1M req/s → single Redis node bottleneck
│   │   ├── Solution 1: Local memory cache (app-level)
│   │   ├── Solution 2: Key sharding (add suffix: key:1, key:2)
│   │   └── Solution 3: Read replicas
│   └── Cache Penetration
│       ├── Problem: query non-existent keys → always miss → DB load
│       ├── Solution 1: Cache null values (short TTL)
│       └── Solution 2: Bloom filter (check existence before query)
├── Multi-layer Caching
│   ├── L1: In-memory cache (< 1ms, 100MB)
│   ├── L2: Redis (1-5ms, 10GB)
│   ├── L3: Database (50ms+)
│   └── Strategy: check L1 → L2 → L3, backfill upper layers
├── Stale-While-Revalidate (SWR)
│   ├── Serve stale cache immediately (fast response)
│   ├── Async refresh cache in background
│   ├── Pros: always fast, no stampede
│   └── Cons: slightly stale data acceptable
└── Redis Best Practices
    ├── Key naming: namespace:entity:id (user:profile:123)
    ├── TTL: always set (prevent memory leak)
    ├── Data structures: STRING, HASH, LIST, SET, ZSET (choose right one)
    ├── Pipeline: batch commands (reduce network RTT)
    ├── Connection pool: reuse connections
    └── Monitoring: hit rate, eviction rate, memory usage
```

**💡 Multi-layer Cache Example:**
```typescript
@Injectable()
export class ProductService {
  constructor(
    @Inject(CACHE_MANAGER) private memCache: Cache, // L1: Memory
    private redis: Redis, // L2: Redis
    private productRepo: ProductRepository // L3: Database
  ) {}

  async getProduct(id: number): Promise<Product> {
    // L1: Memory cache (0.5ms)
    const memKey = `product:${id}`;
    let product = await this.memCache.get<Product>(memKey);
    if (product) return product;

    // L2: Redis cache (3ms)
    const redisKey = `product:${id}`;
    const cached = await this.redis.get(redisKey);
    if (cached) {
      product = JSON.parse(cached);
      await this.memCache.set(memKey, product, 60); // Backfill L1
      return product;
    }

    // L3: Database (50ms)
    product = await this.productRepo.findOne({ where: { id } });
    if (!product) throw new NotFoundException();

    // Save to both caches
    await Promise.all([
      this.memCache.set(memKey, product, 60), // 1 min
      this.redis.setex(redisKey, 3600, JSON.stringify(product)) // 1 hour
    ]);

    return product;
  }

  async updateProduct(id: number, dto: UpdateProductDto) {
    const product = await this.productRepo.save({ id, ...dto });

    // Invalidate all cache layers
    await Promise.all([
      this.memCache.del(`product:${id}`),
      this.redis.del(`product:${id}`)
    ]);

    return product;
  }
}
```

**🔥 Cache Stampede Prevention:**
```typescript
import Redlock from 'redlock';

async getProduct(id: number) {
  const cacheKey = `product:${id}`;
  const lockKey = `lock:${cacheKey}`;

  // Check cache
  let product = await this.redis.get(cacheKey);
  if (product) return JSON.parse(product);

  // Acquire distributed lock
  const lock = await this.redlock.acquire([lockKey], 5000);

  try {
    // Double-check cache (another request might have filled it)
    product = await this.redis.get(cacheKey);
    if (product) return JSON.parse(product);

    // Only 1 request queries DB
    product = await this.productRepo.findOne(id);
    await this.redis.setex(cacheKey, 3600, JSON.stringify(product));

    return product;
  } finally {
    await lock.release();
  }
}
```

**📊 Cache Performance:**
| Layer | Latency | Capacity | Hit Rate | Cost |
|-------|---------|----------|----------|------|
| Memory | 0.5ms | 100MB | 80% | App RAM |
| Redis | 3ms | 10GB | 15% | $50/month |
| DB | 50ms | 1TB | 5% | $200/month |

**🚨 Common Mistakes:**
- ❌ No TTL → memory leak
- ❌ Cache entire response → large payload, compression needed
- ❌ No cache versioning → can't force invalidate
- ❌ Caching mutable data without invalidation → stale data
- ✅ Monitor: cache hit rate (target: 80%+), eviction rate

### **4.2 Messaging (Kafka/RabbitMQ/SQS) & Event-driven** ⭐⭐⭐⭐⭐

```
📨 MESSAGING
├── Messaging Patterns
│   ├── Queue (Point-to-Point): 1 producer → N workers, load balancing
│   │   ├── Use case: background jobs, task distribution
│   │   └── Example: SQS, RabbitMQ queues
│   ├── Pub/Sub: 1 publisher → N subscribers, broadcast
│   │   ├── Use case: event notifications, fan-out
│   │   └── Example: SNS, RabbitMQ exchanges
│   └── Event Log (Kafka): immutable, ordered, replayable
│       ├── Use case: event sourcing, stream processing
│       └── Retention: days/weeks (configurable)
├── Delivery Semantics
│   ├── At-Most-Once: fire-and-forget, message loss possible
│   │   └── Use case: metrics, logs (non-critical)
│   ├── At-Least-Once: retry until ack, duplicates possible
│   │   ├── Most common, require idempotent consumers
│   │   └── Use case: orders, payments
│   └── Exactly-Once: complex, expensive, rare in practice
│       ├── Kafka: transactional producer + consumer
│       └── Trade-off: performance vs correctness
├── Ordering Guarantees
│   ├── Per-partition ordering (Kafka): same key → same partition
│   ├── Global ordering: single partition (low throughput)
│   ├── No ordering: parallel processing (high throughput)
│   └── Design: partition by user_id, order_id for ordering
├── Kafka Specifics
│   ├── Topics & Partitions: topic split into partitions for parallelism
│   ├── Consumer Groups: each partition → 1 consumer in group
│   ├── Offset: consumer position in partition (stored in __consumer_offsets)
│   ├── Replication: fault tolerance (3 replicas typical)
│   └── Retention: time-based (7 days) or size-based
├── Idempotent Consumers
│   ├── Problem: at-least-once → message processed multiple times
│   ├── Solution 1: Idempotency key (message ID in DB, unique constraint)
│   ├── Solution 2: Natural idempotency (SET operations, upserts)
│   └── Pattern: check if processed → skip if duplicate
├── Deduplication
│   ├── Message ID: UUID per message
│   ├── Storage: Redis (TTL = retention period) or DB
│   ├── Check: if EXISTS(message_id) skip, else process + save ID
│   └── Trade-off: storage cost vs correctness
├── Error Handling
│   ├── Retry: exponential backoff (3-5 attempts)
│   ├── DLQ (Dead Letter Queue): failed messages after max retries
│   │   ├── Manual review, replay, or discard
│   │   └── Alert on DLQ depth > threshold
│   ├── Poison Message: malformed message → always fails
│   │   └── Solution: validate schema, skip + log
│   └── Circuit breaker: if downstream fails → stop consuming
└── Best Practices
    ├── Schema evolution: backward compatible (Avro, Protobuf)
    ├── Message size: < 1MB (large payloads → S3 + URL)
    ├── Observability: consumer lag, processing time, errors
    ├── Backpressure: slow consumers → pause, scale horizontally
    └── Testing: use test containers, simulate failures
```

**💡 Idempotent Consumer Pattern:**
```typescript
@Injectable()
export class OrderConsumer {
  constructor(
    private orderService: OrderService,
    private redis: Redis
  ) {}

  @EventPattern('order.created')
  async handleOrderCreated(message: OrderCreatedEvent) {
    const messageId = message.id; // UUID
    const dedupKey = `processed:order:${messageId}`;

    // Check if already processed
    const exists = await this.redis.exists(dedupKey);
    if (exists) {
      console.log(`Message ${messageId} already processed, skipping`);
      return; // Idempotent! ✅
    }

    try {
      // Process message
      await this.orderService.createOrder(message.data);

      // Mark as processed (TTL = 7 days)
      await this.redis.setex(dedupKey, 7 * 24 * 3600, '1');
    } catch (error) {
      // Log error, message will be retried
      console.error(`Failed to process message ${messageId}`, error);
      throw error; // Trigger retry
    }
  }
}
```

**🔄 Event-Driven Architecture:**
```typescript
// Order Service: Publishes events
@Injectable()
export class OrderService {
  constructor(private eventBus: EventBus) {}

  async createOrder(dto: CreateOrderDto) {
    const order = await this.orderRepo.save(dto);
    
    // Publish event
    await this.eventBus.publish('order.created', {
      id: uuid(),
      timestamp: Date.now(),
      data: { orderId: order.id, userId: order.userId, total: order.total }
    });
    
    return order;
  }
}

// Inventory Service: Subscribes to events
@Injectable()
export class InventoryConsumer {
  @EventPattern('order.created')
  async handleOrderCreated(event: OrderCreatedEvent) {
    // Reserve inventory
    await this.inventoryService.reserve(event.data.orderId);
  }
}

// Notification Service: Subscribes to events
@Injectable()
export class NotificationConsumer {
  @EventPattern('order.created')
  async handleOrderCreated(event: OrderCreatedEvent) {
    // Send confirmation email
    await this.emailService.sendOrderConfirmation(event.data);
  }
}
```

**⚖️ Messaging Systems Comparison:**
| System | Pattern | Ordering | Latency | Throughput | Use Case |
|--------|---------|----------|---------|------------|-----------|
| **RabbitMQ** | Queue, Pub/Sub | Per-queue | Low (ms) | Medium | Task queues, RPC |
| **Kafka** | Event Log | Per-partition | Medium (10ms) | Very High | Event streaming, logs |
| **SQS** | Queue | FIFO optional | Medium (10ms) | High | AWS workloads |
| **Redis Streams** | Event Log | Per-stream | Very Low (< 1ms) | High | Real-time, caching |

### **4.3 Background Jobs & Scheduling** ⭐⭐⭐⭐

```
⏱️ JOBS
├── Cron, delayed jobs, rate-controlled workers
├── Worker concurrency, backpressure, visibility timeout
└── Job observability: retries, dead letter, metrics
```

---

## � **7. NODE.JS ECOSYSTEM & TOOLS**

### **7.1 Essential npm Packages** ⭐⭐⭐⭐⭐

```
📦 NPM ECOSYSTEM
├── HTTP/API
│   ├── express: minimalist web framework
│   ├── @nestjs/core: progressive Node.js framework
│   ├── fastify: fast alternative to Express
│   ├── axios / got: HTTP client
│   ├── node-fetch: fetch API for Node
│   └── ws / socket.io: WebSocket libraries
├── Database & ORM
│   ├── typeorm: ORM with decorator-based entities
│   ├── prisma: modern schema-first ORM
│   ├── pg / mysql2: raw database drivers
│   ├── mongoose: MongoDB ODM
│   └── sequelize: alternative ORM
├── Validation
│   ├── class-validator: decorator-based validation
│   ├── class-transformer: transform plain objects to classes
│   ├── zod: TypeScript-first schema validation
│   ├── joi: schema validation
│   └── ajv: fastest JSON schema validator
├── Authentication
│   ├── passport: authentication middleware (20+ strategies)
│   ├── @nestjs/jwt: JWT utilities
│   ├── bcrypt / argon2: password hashing
│   ├── jsonwebtoken: JWT implementation
│   └── otplib: 2FA/TOTP library
├── Caching & Queue
│   ├── ioredis: Redis client
│   ├── bull / bullmq: Redis-based job queue
│   ├── node-cache: in-memory cache
│   └── cache-manager: multi-layer cache abstraction
├── Testing
│   ├── jest: testing framework (default NestJS)
│   ├── supertest: HTTP assertions
│   ├── @faker-js/faker: generate fake data
│   ├── @testcontainers/testcontainers: ephemeral Docker containers
│   └── nock: HTTP mocking
├── Logging & Monitoring
│   ├── winston: versatile logging
│   ├── pino: super fast JSON logger
│   ├── morgan: HTTP request logger (Express)
│   ├── @nestjs/terminus: health checks
│   └── prom-client: Prometheus metrics
├── Utilities
│   ├── dayjs / date-fns: date manipulation
│   ├── lodash: utility functions
│   ├── uuid: UUID generation
│   ├── dotenv: environment variables
│   └── config / @nestjs/config: configuration management
├── Validation & Sanitization
│   ├── validator: string validation library
│   ├── sanitize-html: XSS prevention
│   ├── helmet: security headers
│   └── express-rate-limit: rate limiting
└── Development Tools
    ├── nodemon: auto-restart on file changes
    ├── ts-node: TypeScript execution
    ├── tsx: modern ts-node alternative
    ├── eslint / prettier: code quality
    └── husky: git hooks
```

**💡 Package.json Example (NestJS Project):**
```json
{
  "name": "nestjs-api",
  "version": "1.0.0",
  "scripts": {
    "start": "nest start",
    "start:dev": "nest start --watch",
    "start:prod": "node dist/main",
    "build": "nest build",
    "test": "jest",
    "test:e2e": "jest --config ./test/jest-e2e.json",
    "typeorm": "typeorm-ts-node-commonjs"
  },
  "dependencies": {
    "@nestjs/common": "^10.0.0",
    "@nestjs/core": "^10.0.0",
    "@nestjs/platform-express": "^10.0.0",
    "@nestjs/typeorm": "^10.0.0",
    "@nestjs/config": "^3.0.0",
    "@nestjs/jwt": "^10.0.0",
    "@nestjs/passport": "^10.0.0",
    "@nestjs/swagger": "^7.0.0",
    "@nestjs/cache-manager": "^2.0.0",
    "typeorm": "^0.3.17",
    "pg": "^8.11.0",
    "class-validator": "^0.14.0",
    "class-transformer": "^0.5.1",
    "bcrypt": "^5.1.1",
    "passport": "^0.6.0",
    "passport-jwt": "^4.0.1",
    "ioredis": "^5.3.2",
    "bullmq": "^4.0.0",
    "helmet": "^7.0.0",
    "compression": "^1.7.4",
    "express-rate-limit": "^6.10.0",
    "pino": "^8.15.0",
    "pino-http": "^8.3.0",
    "zod": "^3.22.0"
  },
  "devDependencies": {
    "@nestjs/cli": "^10.0.0",
    "@nestjs/testing": "^10.0.0",
    "@types/node": "^20.0.0",
    "@types/express": "^4.17.17",
    "@types/bcrypt": "^5.0.0",
    "@types/passport-jwt": "^3.0.9",
    "typescript": "^5.1.0",
    "jest": "^29.5.0",
    "supertest": "^6.3.3",
    "@testcontainers/postgresql": "^10.0.0",
    "eslint": "^8.42.0",
    "prettier": "^3.0.0"
  }
}
```

### **7.2 Node.js Process Management** ⭐⭐⭐⭐

```
🔧 PROCESS MANAGEMENT
├── PM2 (Production Process Manager)
│   ├── Cluster mode: pm2 start app.js -i max (use all CPUs)
│   ├── Zero-downtime reload: pm2 reload app
│   ├── Auto-restart: pm2 start app.js --watch
│   ├── Monitoring: pm2 monit, pm2 logs
│   ├── Startup script: pm2 startup, pm2 save
│   └── Ecosystem file: pm2.config.js for multi-app
├── Docker (Containerization)
│   ├── Dockerfile: multi-stage builds for Node
│   ├── .dockerignore: exclude node_modules, .git
│   ├── Security: run as non-root user
│   └── Health checks: HEALTHCHECK instruction
├── Cluster Module (Built-in)
│   ├── require('cluster'): spawn worker processes
│   ├── Master-worker pattern: master listens, workers handle requests
│   └── Use case: maximize CPU utilization
├── Graceful Shutdown
│   ├── SIGTERM handler: close connections, finish requests
│   ├── Drain connections: no new requests
│   ├── Timeout: force kill after 30s
│   └── Kubernetes: terminationGracePeriodSeconds
└── Health Checks
    ├── Liveness: /health/live (is app running?)
    ├── Readiness: /health/ready (can accept traffic?)
    ├── Check: DB connection, Redis, dependencies
    └── @nestjs/terminus: health check library
```

**💡 PM2 Ecosystem Example:**
```javascript
// pm2.config.js
module.exports = {
  apps: [{
    name: 'api-server',
    script: './dist/main.js',
    instances: 'max',  // Use all CPU cores
    exec_mode: 'cluster',
    watch: false,
    max_memory_restart: '1G',
    env: {
      NODE_ENV: 'production',
      PORT: 3000
    },
    error_file: './logs/err.log',
    out_file: './logs/out.log',
    log_date_format: 'YYYY-MM-DD HH:mm:ss Z',
    merge_logs: true,
    autorestart: true,
    max_restarts: 10,
    min_uptime: '10s'
  }, {
    name: 'worker',
    script: './dist/worker.js',
    instances: 2,
    exec_mode: 'cluster',
    cron_restart: '0 0 * * *',  // Restart daily at midnight
    env: {
      NODE_ENV: 'production',
      WORKER_TYPE: 'background'
    }
  }]
};

// Start: pm2 start pm2.config.js
// Reload: pm2 reload all
// Monitor: pm2 monit
```

**💡 Dockerfile Example (Multi-stage):**
```dockerfile
# Stage 1: Build
FROM node:20-alpine AS builder

WORKDIR /app

# Copy package files
COPY package*.json ./
COPY tsconfig*.json ./

# Install dependencies
RUN npm ci --only=production && \
    npm cache clean --force

# Copy source code
COPY src ./src

# Build TypeScript
RUN npm run build

# Stage 2: Production
FROM node:20-alpine AS production

WORKDIR /app

# Security: run as non-root
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nestjs -u 1001

# Copy dependencies and build
COPY --from=builder --chown=nestjs:nodejs /app/node_modules ./node_modules
COPY --from=builder --chown=nestjs:nodejs /app/dist ./dist
COPY --chown=nestjs:nodejs package*.json ./

# Switch to non-root user
USER nestjs

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=40s \
  CMD node -e "require('http').get('http://localhost:3000/health', (r) => process.exit(r.statusCode === 200 ? 0 : 1))"

# Start app
CMD ["node", "dist/main"]
```

**💡 Graceful Shutdown (NestJS):**
```typescript
// main.ts
async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  // Enable shutdown hooks
  app.enableShutdownHooks();

  // Graceful shutdown
  const gracefulShutdown = async () => {
    console.log('Received shutdown signal, closing gracefully...');
    
    // Stop accepting new requests
    await app.close();
    
    // Close database connections
    // Close Redis connections
    // Finish in-flight requests
    
    console.log('Server closed');
    process.exit(0);
  };

  process.on('SIGTERM', gracefulShutdown);
  process.on('SIGINT', gracefulShutdown);

  await app.listen(3000);
  console.log(`Application is running on: ${await app.getUrl()}`);
}

bootstrap();

// Health check controller
@Controller('health')
export class HealthController {
  constructor(
    private health: HealthCheckService,
    private db: TypeOrmHealthIndicator,
    private redis: RedisHealthIndicator
  ) {}

  @Get('live')
  @HealthCheck()
  liveness() {
    return this.health.check([]);  // Simple "is running?" check
  }

  @Get('ready')
  @HealthCheck()
  readiness() {
    return this.health.check([
      () => this.db.pingCheck('database'),
      () => this.redis.pingCheck('redis')
    ]);
  }
}
```

### **7.3 Node.js Performance & Debugging Tools** ⭐⭐⭐⭐

```
🛠️ DEBUGGING & PROFILING
├── Built-in Debugger
│   ├── node --inspect: enable Chrome DevTools
│   ├── debugger; statement: set breakpoints
│   └── chrome://inspect: connect debugger
├── Profiling Tools
│   ├── clinic.js: detect performance issues
│   │   ├── clinic doctor: diagnose problems
│   │   ├── clinic flame: flamegraphs
│   │   └── clinic bubbleprof: async profiling
│   ├── 0x: flamegraphs for CPU profiling
│   ├── autocannon: HTTP benchmarking
│   └── loadtest: load testing tool
├── Memory Debugging
│   ├── node --inspect --expose-gc: manual GC trigger
│   ├── Chrome DevTools: heap snapshots
│   ├── @memlab/cli: find memory leaks
│   └── heapdump: programmatic heap dumps
├── Logging & APM
│   ├── Winston / Pino: structured logging
│   ├── New Relic / Datadog: APM monitoring
│   ├── Sentry: error tracking
│   └── OpenTelemetry: distributed tracing
└── Best Practices
    ├── Use source maps in production (for stack traces)
    ├── Enable logging with correlation IDs
    ├── Monitor event loop lag
    └── Set up alerts for errors/performance
```

**💡 Debugging Commands:**
```bash
# Start with debugger
node --inspect dist/main.js

# Enable GC logging
node --trace-gc dist/main.js

# Increase heap size
node --max-old-space-size=4096 dist/main.js

# CPU profiling with clinic.js
npx clinic doctor -- node dist/main.js
npx clinic flame -- node dist/main.js

# Generate flamegraph with 0x
npx 0x dist/main.js

# Heap snapshot
node --inspect --expose-gc dist/main.js
# Then in Chrome DevTools: take heap snapshot

# Load testing
npx autocannon -c 100 -d 30 http://localhost:3000/api/users
```

---

### **5.1 System Design Fundamentals** ⭐⭐⭐⭐⭐

```
🧠 SYSTEM DESIGN
├── Requirements: functional + non-functional (SLOs)
├── Data model first; read/write paths
├── Bottlenecks: DB, network, CPU, lock contention
├── Trade-offs: consistency vs availability vs latency
└── Capacity planning: QPS, p95/p99, storage growth
```

### **5.2 Architecture Styles** ⭐⭐⭐⭐

```
🏛️ ARCHITECTURE
├── Monolith vs modular monolith vs microservices
├── DDD: bounded contexts, aggregates
├── BFF, API gateway, service mesh (concept)
├── CQRS, event sourcing (when/why)
└── Multi-region, active-active vs active-passive
```

### **5.3 Common “Design a …” Questions (Backbone)** ⭐⭐⭐⭐

```
🧪 DESIGN EXERCISES
├── Auth service (login/refresh/logout, revoke)
├── Rate limiter (token bucket/leaky bucket)
├── Notification system (email/sms/push)
├── File upload service (multipart, signed URLs, antivirus)
├── Real-time updates (WebSocket/SSE), presence
└── Payment flow (idempotency, retries, reconciliation)
```

---

## 🟪 **6. PRODUCTION ENGINEERING (Senior)**

### **6.1 Observability (Logs/Metrics/Tracing) & SLOs** ⭐⭐⭐⭐⭐

```
📈 OBSERVABILITY
├── Structured logging, correlation IDs, redaction
├── Metrics: RED/USE, golden signals
├── Tracing: distributed tracing, spans, sampling
├── Dashboards & alerting; alert fatigue
└── SLO/SLI, error budgets
```

### **6.2 Debugging & Profiling in Production** ⭐⭐⭐⭐⭐

```
🧰 TROUBLESHOOTING
├── Reproduce vs isolate; feature flags; canary
├── Profiling CPU/memory, heap dumps (concept)
├── DB debugging: slow queries, lock waits
├── Network: packet loss, DNS issues, TLS expiry
└── Postmortem: timeline, root cause, follow-ups
```

### **6.3 Performance & Scalability** ⭐⭐⭐⭐⭐

```
🚀 PERFORMANCE
├── Latency budgets: p50/p95/p99; tail latency
├── Connection pools, thread pools, queue depth
├── N+1, batching, streaming, pagination
├── Hot keys, hot partitions
└── Load tests, soak tests, capacity tests
```

### **6.4 Security (AppSec) for Backend** ⭐⭐⭐⭐⭐

```
🔒 SECURITY
├── OWASP Top 10: injection, auth issues, SSRF, deserialization
├── Secrets management, rotation, least privilege
├── Data protection: encryption at rest/in transit, PII handling
├── Auditing, immutable logs (concept)
└── Secure SDLC: threat modeling, dependency scanning
```

### **6.5 Testing Strategy** ⭐⭐⭐⭐

```
🧪 TESTING
├── Unit vs integration vs contract vs E2E
├── Testcontainers, ephemeral DBs
├── Mocks vs fakes vs stubs (khi nào dùng gì)
└── Load/perf tests như “first-class tests”
```

### **6.6 CI/CD, Deployments, Infra Basics** ⭐⭐⭐⭐

```
🚢 DELIVERY
├── Build pipelines, caching, artifact promotion
├── Deploy strategies: rolling, blue/green, canary
├── Containers: Docker, images, multi-stage builds
├── K8s basics: pods, services, ingress (concept)
└── Config: env, secrets, feature flags
```

---

## 🎯 **LEARNING PATH BY EXPERIENCE (Lộ trình sườn)**

### **🌱 Junior (0–1 năm)**

- [ ] HTTP basics: methods/status/headers
- [ ] CRUD API, validation, error handling
- [ ] SQL basics: select/join/index basics
- [ ] Auth basics: sessions/JWT (dùng đúng, không cần “deep”)
- [ ] Logging cơ bản, đọc logs

### **🚀 Mid-Level (1–3 năm)**

- [ ] API design: pagination, versioning, OpenAPI
- [ ] Transactions, isolation, deadlocks (nắm được hiện tượng)
- [ ] Caching (Redis): cache-aside, TTL, invalidation
- [ ] Testing: unit + integration, contract testing cơ bản
- [ ] Deploy basics: Docker, CI pipeline, rollback

### **🔥 Senior (3+ năm)**

- [ ] System design: trade-offs, capacity planning, SLOs
- [ ] Production debugging: profiling, incident response
- [ ] Data scalability: replication/sharding/backup/DR
- [ ] Messaging/event-driven: ordering, idempotency, DLQ
- [ ] Security-by-default: threat modeling, secrets, PII

### **🧭 Tech Lead / Architect**

- [ ] Architecture evolution: monolith → modular → microservices (khi nào)
- [ ] Platform thinking: developer experience, standards, golden paths
- [ ] Reliability engineering: error budgets, chaos/DR drills (concept)
- [ ] Governance: APIs, schemas, data contracts, observability baseline

---

## 📝 **INTERVIEW PREPARATION CHECKLIST (Sườn)**

_Đối chiếu với Mind Map: Nhánh 1–6. Đánh dấu [x] khi đã nắm vững._

### **✅ Must-Know (Tất cả cấp) — Nền tảng**

- [ ] **HTTP fundamentals** (2.1): status codes, headers, pagination, errors
- [ ] **SQL core** (3.1): indexes, joins, query plans (basic)
- [ ] **Auth basics** (2.4): JWT/session, refresh tokens (concept)
- [ ] **Error handling** (1.2): timeouts, retries, idempotency

### **✅ Mid-Level**

- [ ] **API design** (2.2): versioning, OpenAPI, backward compatibility
- [ ] **Cache** (4.1): cache-aside, invalidation, stampede
- [ ] **Testing** (6.5): integration tests, DB in tests
- [ ] **Delivery** (6.6): docker, deploy strategy basics

### **✅ Senior**

- [ ] **System design** (5.1–5.3): requirements → design → trade-offs
- [ ] **Observability** (6.1): logs/metrics/traces, SLO mindset
- [ ] **Messaging** (4.2): idempotent consumers, DLQ, ordering
- [ ] **Production debugging** (6.2): profiling, slow queries, lock contention
- [ ] **Security** (6.4): OWASP, secrets, PII, least privilege

---

## 📊 **INTERVIEW QUESTION FREQUENCY (Gợi ý)**

| Topic                            | Junior | Mid | Senior | Frequency |
| -------------------------------- | ------ | --- | ------ | --------- |
| HTTP fundamentals                | ✅     | ✅  | ✅     | 90%       |
| SQL / Indexing                   | ✅     | ✅  | ✅     | 85%       |
| Cache (Redis)                    | ❌     | ✅  | ✅     | 75%       |
| Messaging / Event-driven         | ❌     | ✅  | ✅     | 70%       |
| System design                    | ❌     | ❌  | ✅     | 80%       |
| Observability / Debug production | ❌     | ✅  | ✅     | 75%       |
| Security                         | ❌     | ✅  | ✅     | 70%       |

---

## 🔗 **QUICK REFERENCE LINKS**

| Topic            | Resource |
| ---------------- | -------- |
| HTTP             | [MDN - HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP) |
| API Spec         | [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) |
| Security         | [OWASP](https://owasp.org/) |
| Observability    | [OpenTelemetry](https://opentelemetry.io/) |
| Postgres         | [PostgreSQL Docs](https://www.postgresql.org/docs/) |
| Redis            | [Redis Docs](https://redis.io/docs/latest/) |
| Kafka            | [Apache Kafka Docs](https://kafka.apache.org/documentation/) |

---

---

## 🎤 **TYPICAL INTERVIEW QUESTIONS BY TOPIC**

### **🧩 Node.js Runtime (Senior Level)**

**Q1: Explain the Event Loop. What happens when you have blocking code?**
<details>
<summary>Expected Answer</summary>

Event Loop phases: timers → I/O callbacks → idle → poll → check → close callbacks. Microtasks (process.nextTick, Promise) run between phases.

Blocking code (sync operations > 10ms) stops the event loop, preventing other requests from being processed. Solution: Worker Threads, cluster mode, or job queues.

```javascript
// Bad: blocks event loop
app.get('/api', (req, res) => {
  const result = hugeArray.map(expensiveSync); // Blocks!
  res.json(result);
});

// Good: offload to worker
const worker = new Worker('./worker.js', { workerData });
```
</details>

**Q2: How do you detect and fix memory leaks in production?**
<details>
<summary>Expected Answer</summary>

Tools: heap snapshots (Chrome DevTools), `node --inspect`, `node-memwatch`.

Common causes:
- Global variables accumulating
- Event listeners not removed
- Closures holding references
- Mongoose models recreated per request

Fix: Use LRU cache with size limits, remove event listeners, clear references, define models globally.
</details>

---

### **🗄️ Database & SQL (All Levels)**

**Q3: What is the N+1 query problem? How do you fix it?**
<details>
<summary>Expected Answer</summary>

N+1: 1 query to fetch parents + N queries for each parent's child (e.g., posts + authors).

**Solutions:**
1. **Eager loading (JOIN)**: `SELECT posts.*, users.* FROM posts LEFT JOIN users`
2. **Batch loading**: `SELECT * FROM users WHERE id IN (1,2,3...)`
3. **DataLoader**: Batches requests in single tick (GraphQL)

Always monitor query count in logs.
</details>

**Q4: Explain transaction isolation levels. When would you use SERIALIZABLE?**
<details>
<summary>Expected Answer</summary>

| Level | Prevents | Use Case |
|-------|----------|----------|
| READ COMMITTED | Dirty reads | Default, most cases |
| REPEATABLE READ | Non-repeatable reads | Reports, consistency |
| SERIALIZABLE | All anomalies | Financial transactions |

SERIALIZABLE: Prevents phantom reads, lost updates. Use for: payment processing, account transfers, critical inventory updates. Trade-off: lowest performance, potential deadlocks.
</details>

---

### **⚡ Caching & Performance (Mid-Senior)**

**Q5: How do you prevent cache stampede (thundering herd)?**
<details>
<summary>Expected Answer</summary>

Problem: Cache expires → 1000 concurrent requests hit DB.

**Solutions:**
1. **Distributed lock (Redlock)**: Only 1 request queries DB
2. **Probabilistic early expiration**: Refresh before expiration
3. **Stale-While-Revalidate**: Serve stale, async refresh

```javascript
// Distributed lock approach
const lock = await redlock.acquire([`lock:${key}`], 5000);
try {
  product = await db.query();
  await cache.set(key, product);
} finally {
  await lock.release();
}
```
</details>

**Q6: Multi-layer caching architecture: Memory → Redis → DB. Explain the strategy.**
<details>
<summary>Expected Answer</summary>

**Layers:**
- L1 (Memory): 0.5ms, 100MB, 80% hit rate
- L2 (Redis): 3ms, 10GB, 15% hit rate
- L3 (DB): 50ms, unlimited

**Strategy:**
1. Check memory → if hit, return
2. Check Redis → if hit, backfill memory, return
3. Query DB → save to Redis + memory

**Invalidation:** Clear all layers on write. Use TTL: short for L1 (1 min), longer for L2 (1 hour).
</details>

---

### **📨 Messaging & Event-Driven (Senior)**

**Q7: How do you ensure exactly-once processing in an event-driven system?**
<details>
<summary>Expected Answer</summary>

Reality: **Exactly-once is hard**, most systems use **at-least-once + idempotency**.

**Idempotent Consumer Pattern:**
```typescript
// Store message ID in DB/Redis
const exists = await redis.exists(`processed:${messageId}`);
if (exists) return; // Already processed

await processMessage(message);
await redis.setex(`processed:${messageId}`, 86400, '1'); // 24h TTL
```

**Kafka Transactions** (true exactly-once):
- Transactional producer + consumer
- Trade-off: performance cost, complexity
</details>

**Q8: Design a distributed transaction: Order → Reserve Inventory → Process Payment. If payment fails, how do you rollback?**
<details>
<summary>Expected Answer</summary>

**Saga Pattern (Choreography):**

```
Order Service: Create order (PENDING)
  ↓ event: order.created
Inventory Service: Reserve inventory
  ↓ event: inventory.reserved
Payment Service: Charge card
  ↓ success: order.confirmed
  ↓ failure: payment.failed
  
On payment.failed:
  → Inventory: Release reservation (compensating transaction)
  → Order: Mark as CANCELLED
```

**Outbox Pattern** (transactional messaging):
- Insert order + outbox event in same DB transaction
- Background job polls outbox → publish to message queue
- Guarantees: at-least-once delivery
</details>

---

### **🏗️ System Design (Senior)**

**Q9: Design a Rate Limiter (token bucket). How do you implement it with Redis?**
<details>
<summary>Expected Answer</summary>

**Token Bucket Algorithm:**
- Tokens added at constant rate (e.g., 100/min)
- Each request consumes 1 token
- Bucket capacity: max burst (e.g., 10)

**Redis Implementation:**
```lua
-- Lua script (atomic)
local key = KEYS[1]
local limit = tonumber(ARGV[1])
local ttl = tonumber(ARGV[2])

local current = redis.call('INCR', key)
if current == 1 then
  redis.call('EXPIRE', key, ttl)
end

if current > limit then
  return 0 -- Rate limited
end

return 1 -- Allowed
```

**Distributed:** Use Redis for shared state across servers.
</details>

**Q10: You have 10,000 req/s. Database can handle 100 req/s. How do you scale?**
<details>
<summary>Expected Answer</summary>

**Multi-pronged approach:**

1. **Caching** (Redis): 95% cache hit → 500 req/s to DB ✅
2. **Read Replicas**: Route reads to replicas (5 replicas → 500 req/s capacity)
3. **Connection Pooling**: Reuse connections (reduce overhead)
4. **Vertical Scaling**: Bigger DB instance
5. **Horizontal Sharding**: Split data by user_id % 10
6. **CDN**: Static assets offloaded
7. **Async Processing**: Write to queue, process later

**Numbers:**
- 10,000 req/s
- 95% cache hit = 9,500 from cache
- 5% DB = 500 req/s
- 5 read replicas = 100 req/s each ✅
</details>

---

### **🔒 Security (Mid-Senior)**

**Q11: How do you secure API endpoints? Mention 5 techniques.**
<details>
<summary>Expected Answer</summary>

1. **Authentication**: JWT with refresh tokens, OAuth2
2. **Authorization**: RBAC (role-based), check permissions per endpoint
3. **Rate Limiting**: Per user/IP (prevent abuse)
4. **Input Validation**: Schema validation (Zod, Joi), sanitize
5. **HTTPS Only**: TLS 1.3, HSTS header
6. **CORS**: Whitelist allowed origins
7. **CSRF Protection**: Token, SameSite cookies
8. **SQL Injection**: Parameterized queries, ORM
9. **Secrets Management**: Vault (AWS Secrets Manager)
10. **Audit Logs**: Log all access (who, what, when)
</details>

**Q12: User uploads 100MB file with malware. How do you handle it?**
<details>
<summary>Expected Answer</summary>

**Security Layers:**
1. **File Size Limit**: Max 10MB (reject early)
2. **File Type Validation**: Check MIME type + extension
3. **Scan with Antivirus**: ClamAV, AWS S3 scanning
4. **Sandbox Execution**: Test file in isolated env
5. **Signed URLs**: Generate presigned S3 URL, upload direct to S3
6. **Async Processing**: Upload to temp location → scan → move to permanent
7. **Rate Limit**: Max 10 uploads per user per day

**Flow:**
```
Client → Generate signed S3 URL → Upload to S3
  → Lambda trigger → Scan with ClamAV
  → If clean: move to public bucket
  → If malware: delete + alert
```
</details>

---

### **🧰 Production & Debugging (Senior)**

**Q13: Production API latency suddenly increased from 50ms to 2s. How do you debug?**
<details>
<summary>Expected Answer</summary>

**Systematic Approach:**

1. **Check Metrics**:
   - CPU, memory, disk I/O (normal?)
   - Database connections pool (exhausted?)
   - Cache hit rate (dropped?)
   
2. **Check Logs**:
   - Recent deployments?
   - Error spike?
   - Slow query logs
   
3. **Distributed Tracing**:
   - Identify slowest span (DB query? External API?)
   
4. **Database**:
   - `SHOW PROCESSLIST` (MySQL)
   - `pg_stat_activity` (Postgres)
   - Lock waits? Long-running queries?
   
5. **Network**:
   - DNS resolution issues?
   - Increased latency to dependencies?
   
6. **Code**:
   - N+1 query introduced?
   - Blocking operation in event loop?

**Common Causes:**
- Database lock contention
- Cache expiration (stampede)
- External API timeout
- Recent code change (N+1 query)
</details>

**Q14: Memory leak in Node.js production. Memory grows from 200MB → 4GB over 3 days. How do you find the leak?**
<details>
<summary>Expected Answer</summary>

**Tools:**
1. **Heap Snapshot** (Chrome DevTools):
   - Take 2 snapshots 10 minutes apart
   - Compare → identify growing objects
   
2. **Profiling**:
   ```bash
   node --inspect server.js
   # Chrome: chrome://inspect
   ```

**Common Patterns:**
```javascript
// ❌ Leak 1: Global array grows
let cachedUsers = []; // Never cleared!

// ❌ Leak 2: Event listeners
eventEmitter.on('data', handler); // Never .off()

// ❌ Leak 3: Closures
app.get('/api', (req, res) => {
  const largeData = Buffer.alloc(10 * 1024 * 1024);
  setTimeout(() => {
    console.log(largeData.length); // Holds reference!
  }, 60000);
});

// ✅ Fix: LRU cache, remove listeners, clear references
```

**Monitoring:**
- Track heap size over time
- Alert on continuous growth
- Use `--max-old-space-size` as temporary mitigation
</details>

---

## 📚 **STUDY GUIDE & RESOURCES (Node.js Focus)**

### **🎯 Priority Topics (80/20 Rule)**

Focus on these topics for maximum interview ROI:

**Must Master (70% of questions):**
1. ✅ **Node.js Event Loop** → Node.js docs, Understanding the Node.js Event Loop
2. ✅ **Express middleware** → Express.js documentation
3. ✅ **NestJS architecture** → NestJS docs (Guards, Interceptors, Pipes)
4. ✅ **TypeORM/Prisma** → Official documentation
5. ✅ **SQL optimization** → Use The Index, Luke

**Important (20% of questions):**
6. ✅ **Authentication** → Passport.js, JWT
7. ✅ **Caching patterns** → Redis + ioredis docs
8. ✅ **Messaging** → Bull/BullMQ documentation
9. ✅ **Testing** → Jest + Supertest
10. ✅ **Docker & PM2** → Process management

**Advanced (10% of questions):**
11. ✅ **System design** → System Design Primer (GitHub)
12. ✅ **Performance tuning** → Node.js best practices

---

### **📖 Recommended Books (Node.js Stack)**

| Book | Level | Focus | Priority |
|------|-------|-------|----------|
| **Node.js Design Patterns** (Mario Casciaro) | Mid-Senior | Node.js patterns, async | ⭐⭐⭐⭐⭐ |
| **Designing Data-Intensive Applications** | Senior | System design, distributed | ⭐⭐⭐⭐⭐ |
| **Node.js Best Practices** (Goldberger) | Mid | Production Node.js | ⭐⭐⭐⭐ |
| **High Performance MySQL** | Mid-Senior | Database optimization | ⭐⭐⭐⭐ |
| **Release It!** | Senior | Production resilience | ⭐⭐⭐⭐ |

---

### **🛠️ Hands-on Practice (Node.js Projects)**

**Build These Projects:**

1. **RESTful API with Express** (Junior)
   - Skills: Express middleware, routing, validation
   - Stack: Express + PostgreSQL + Redis
   - Features: CRUD, pagination, auth (JWT), rate limiting
   - Scale: 1k QPS

2. **NestJS Microservice** (Mid)
   - Skills: NestJS modules, Guards, Interceptors, TypeORM
   - Stack: NestJS + TypeORM + Redis + Bull Queue
   - Features: authentication, authorization, background jobs
   - Scale: 5k QPS

3. **E-commerce API** (Senior)
   - Skills: transactions, event-driven, saga pattern
   - Stack: NestJS + Prisma + Kafka + Redis
   - Features: checkout, inventory, payments, notifications
   - Scale: Handle concurrent purchases, idempotency
   - Patterns: Saga, Outbox, CQRS

4. **Real-time Chat API** (Senior)
   - Skills: WebSockets, message queues, caching
   - Stack: NestJS + Socket.io + Redis + PostgreSQL
   - Features: presence, typing, message history, rooms
   - Scale: 10k concurrent connections

---

### **🌐 Essential Resources**

#### **Official Documentation:**
- **Node.js**: https://nodejs.org/docs/latest/api/
- **Express**: https://expressjs.com/
- **NestJS**: https://docs.nestjs.com/
- **TypeORM**: https://typeorm.io/
- **Prisma**: https://www.prisma.io/docs/

#### **Node.js Specific:**
- **Node.js Best Practices**: https://github.com/goldbergyoni/nodebestpractices
- **Awesome Node.js**: https://github.com/sindresorhus/awesome-nodejs
- **Node.js Event Loop**: https://nodejs.org/en/guides/event-loop-timers-and-nexttick/
- **V8 Blog**: https://v8.dev/blog

#### **Tools & Libraries:**
- **npm trends**: https://npmtrends.com/ (compare packages)
- **Snyk**: https://snyk.io/ (security vulnerabilities)
- **bundlephobia**: https://bundlephobia.com/ (package size)
- **TypeScript Playground**: https://www.typescriptlang.org/play

#### **Video Courses:**
- **NestJS Zero to Hero** (Udemy) - Ariel Weinberger
- **Node.js: The Complete Guide** (Udemy) - Maximilian Schwarzmüller
- **Advanced Node.js** (Frontend Masters) - Scott Moss

---

### **⏱️ Study Schedule (4 weeks) - Node.js Focus**

**Week 1: Node.js Fundamentals**
- Day 1-2: Event Loop, V8 engine, memory management
- Day 3-4: Streams, Worker Threads, Cluster mode
- Day 5-6: Express middleware patterns
- Day 7: Build: Express REST API with auth

**Week 2: NestJS Architecture**
- Day 8-9: NestJS modules, DI, Controllers
- Day 10-11: Guards, Interceptors, Pipes
- Day 12-13: TypeORM entities, relations, transactions
- Day 14: Build: NestJS CRUD API with TypeORM

**Week 3: Data & Caching**
- Day 15-16: SQL optimization, N+1 problem, indexing
- Day 17-18: Redis caching patterns, Bull queue
- Day 19-20: Prisma ORM (alternative to TypeORM)
- Day 21: Build: E-commerce checkout with saga pattern

**Week 4: Production & System Design**
- Day 22-23: Docker, PM2, graceful shutdown
- Day 24-25: Observability (logging, metrics, tracing)
- Day 26-27: System design patterns (rate limiter, URL shortener)
- Day 28: Mock interviews (focus on Node.js)

---

## 📊 **SELF-ASSESSMENT CHECKLIST (Node.js)**

Rate yourself: ❌ Never heard of it | 🟡 Aware, need practice | ✅ Confident, can explain

### **Node.js Core**
- [ ] Event Loop phases & execution order
- [ ] V8 garbage collection (Scavenger, Mark-Sweep-Compact)
- [ ] Memory leak detection & heap snapshots
- [ ] Streams & backpressure handling
- [ ] Worker Threads vs Child Process vs Cluster
- [ ] process.nextTick vs setImmediate vs Promise

### **Express**
- [ ] Middleware execution order
- [ ] Error handling middleware (4 params)
- [ ] Router organization & controller pattern
- [ ] Request validation (Zod, Joi, express-validator)
- [ ] Rate limiting & security (helmet, cors)

### **NestJS**
- [ ] Module system & dependency injection
- [ ] Guards (authentication/authorization)
- [ ] Interceptors (logging, caching, transformation)
- [ ] Pipes (validation with class-validator)
- [ ] Exception filters
- [ ] Execution order: Middleware → Guards → Interceptors → Pipes

### **TypeORM**
- [ ] Entity decorators (@Entity, @Column, @OneToMany)
- [ ] Repository pattern vs QueryBuilder
- [ ] N+1 query problem & eager loading
- [ ] Transactions with manager.transaction()
- [ ] Optimistic locking with @VersionColumn()
- [ ] Migrations (generate, run, revert)

### **Prisma**
- [ ] Schema definition (schema.prisma)
- [ ] Prisma Client queries (findMany, create, update)
- [ ] Nested reads/writes (include, create)
- [ ] Transactions with $transaction()
- [ ] Raw SQL with $queryRaw
- [ ] TypeORM vs Prisma trade-offs

### **Caching & Queue**
- [ ] Redis with ioredis
- [ ] Cache strategies (cache-aside, write-through)
- [ ] Cache stampede prevention
- [ ] Bull/BullMQ job queues
- [ ] Idempotent consumers
- [ ] Dead letter queues

### **Production**
- [ ] PM2 cluster mode & zero-downtime reload
- [ ] Docker multi-stage builds
- [ ] Graceful shutdown (SIGTERM, SIGINT)
- [ ] Health checks (liveness, readiness)
- [ ] Logging with Pino/Winston
- [ ] APM monitoring (New Relic, Datadog)

### **Testing**
- [ ] Jest unit tests
- [ ] Supertest for API testing
- [ ] Test containers (ephemeral databases)
- [ ] Mocking with jest.fn() and jest.mock()
- [ ] E2E tests in NestJS
- [ ] Code coverage with Istanbul

**Target:** ✅ on 80% topics for senior level.

---

## 🔗 **QUICK REFERENCE LINKS (Node.js)**

| Topic | Resource |
| ----- | -------- |
| **Node.js** | [Node.js Docs](https://nodejs.org/docs/latest/api/) |
| **Express** | [Express Guide](https://expressjs.com/en/guide/routing.html) |
| **NestJS** | [NestJS Documentation](https://docs.nestjs.com/) |
| **TypeORM** | [TypeORM Guide](https://typeorm.io/) |
| **Prisma** | [Prisma Docs](https://www.prisma.io/docs/) |
| **Redis** | [ioredis](https://github.com/redis/ioredis) |
| **Bull Queue** | [Bull Documentation](https://docs.bullmq.io/) |
| **Passport** | [Passport Strategies](http://www.passportjs.org/) |
| **Jest** | [Jest Documentation](https://jestjs.io/docs/getting-started) |
| **Docker** | [Node.js Docker Best Practices](https://github.com/nodejs/docker-node/blob/main/docs/BestPractices.md) |

---

## 📦 **NPM PACKAGE QUICK REFERENCE**

### **Core Framework:**
```bash
npm i @nestjs/core @nestjs/common @nestjs/platform-express
npm i express
```

### **Database:**
```bash
# TypeORM
npm i @nestjs/typeorm typeorm pg

# Prisma
npm i @prisma/client && npx prisma init
npm i -D prisma
```

### **Validation:**
```bash
npm i class-validator class-transformer zod joi
```

### **Authentication:**
```bash
npm i @nestjs/jwt @nestjs/passport passport passport-jwt bcrypt
```

### **Caching & Queue:**
```bash
npm i @nestjs/cache-manager cache-manager ioredis bullmq
```

### **Logging & Monitoring:**
```bash
npm i pino pino-http pino-pretty
npm i @nestjs/terminus  # Health checks
```

### **Testing:**
```bash
npm i -D jest @nestjs/testing supertest @faker-js/faker
npm i -D @testcontainers/postgresql
```

### **Security:**
```bash
npm i helmet express-rate-limit cors
```

---

## 📅 **CHANGELOG**

- **v1.0** - Complete mindmap với chi tiết:
  - Code examples cho các patterns quan trọng
  - Trade-offs comparisons
  - Common mistakes & anti-patterns
  - Typical interview questions + answers
  - Study guide & resources
  - Self-assessment checklist

