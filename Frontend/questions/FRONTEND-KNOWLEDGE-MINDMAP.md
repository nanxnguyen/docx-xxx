# 🧠 FRONTEND DEVELOPER KNOWLEDGE MINDMAP

> **Tổng hợp kiến thức Frontend từ Junior đến Senior/Tech Lead**
> Dựa trên 63+ câu hỏi phỏng vấn thực tế

---

## 📊 **VISUAL MINDMAP**

```
                                    ┌─────────────────────────────────────┐
                                    │     🎯 FRONTEND DEVELOPER          │
                                    │         KNOWLEDGE MAP              │
                                    │      (63+ Topics Covered)          │
                                    └─────────────────────────────────────┘
                                                      │
    ┌──────────────┬──────────────┬─────────────────┼─────────────────┬──────────────┬──────────────┐
    │              │              │                 │                 │              │              │
    ▼              ▼              ▼                 ▼                 ▼              ▼              ▼
┌────────┐   ┌────────┐   ┌────────────┐   ┌────────────┐   ┌────────────┐   ┌────────────┐
│1.CORE  │   │2.ASYNC │   │ 3.REACT &  │   │ 4.BUILD &  │   │ 5.SENIOR   │   │ 6.EXTRA    │
│  JS    │   │& PERF  │   │ FRAMEWORKS │   │   TOOLS    │   │  TOPICS    │   │  TOPICS    │
└────────┘   └────────┘   └────────────┘   └────────────┘   └────────────┘   └────────────┘
    │              │              │                 │                 │              │
    ▼              ▼              ▼                 ▼                 ▼              ▼
─────────    ─────────    ─────────────    ─────────────    ─────────────    ─────────────
Data Types   Event Loop   React Hooks      Vite/Webpack     System Design    WebSocket
Memory       Promises     State Mgmt       Turbopack        Security         Browser APIs
Closures     Async/Await  Next.js 16       ESM vs CJS       Testing          CSS Arch
this Bind    Caching      Server Comp      TypeScript       CI/CD            Git Workflow
ES6+         Web Workers  React Query      Tree Shaking     APM Monitor      Accessibility
Prototypes   Performance  React Patterns   Code Split       Architecture     GraphQL
                                            Docker/K8s
─────────    ─────────    ─────────────    ─────────────    ─────────────    ─────────────
```

---

## 🌳 **MINDMAP CHI TIẾT**

---

## 🟦 **1. JAVASCRIPT CORE FUNDAMENTALS**

### **1.1 Data Types & Memory** ⭐⭐⭐

```
📦 DATA TYPES (8 loại - 8 Types)
├── 🔷 Primitives (7 - Immutable - Bất Biến)
│   ├── number (64-bit float, MAX_SAFE_INTEGER) // Số thực 64-bit
│   ├── string (UTF-16, immutable) // Chuỗi UTF-16, không thể thay đổi
│   ├── boolean (true/false) // Giá trị logic
│   ├── null (intentional empty) // Rỗng có chủ ý
│   ├── undefined (uninitialized) // Chưa khởi tạo
│   ├── symbol (unique identifier) // Định danh duy nhất
│   └── bigint (arbitrary precision) // Số nguyên lớn, độ chính xác tùy ý
│
├── 🔶 Reference Type (1 - Mutable - Có Thể Thay Đổi)
│   └── object (arrays, functions, dates, maps, sets...) // Mảng, hàm, ngày, Map, Set...
│
└── 💾 MEMORY MANAGEMENT (Quản Lý Bộ Nhớ)
    ├── Stack: primitives, references (fast, LIFO) // Nhanh, LIFO (Last In First Out)
    ├── Heap: objects (larger, GC managed) // Lớn hơn, quản lý bởi Garbage Collector
    └── Garbage Collection: mark-and-sweep algorithm // Thuật toán đánh dấu và quét
```

**🔑 Key Points (Điểm Quan Trọng):**

- ⚖️ `==` vs `===` (type coercion vs strict) // So sánh ép kiểu vs so sánh nghiêm ngặt

  - 💡 `==`: Tự động ép kiểu (1 == '1' → true)
  - 💡 `===`: Không ép kiểu (1 === '1' → false)

- 📋 Shallow vs Deep copy (`structuredClone()`) // Copy nông vs Copy sâu

  - 💡 Shallow: Chỉ copy reference (thay đổi ảnh hưởng bản gốc)
  - 💡 Deep: Copy toàn bộ (thay đổi không ảnh hưởng bản gốc)

- ❌ Falsy values: `0, "", null, undefined, false, NaN` // Các giá trị falsy

  - 💡 Tất cả giá trị này đều được coi là `false` trong boolean context

- 🐛 `typeof null === "object"` (legacy bug) // Lỗi cũ của JavaScript
  - 💡 Đây là bug từ phiên bản đầu, vẫn giữ để tương thích ngược

---

### **1.2 Scope, Hoisting & Closures** ⭐⭐⭐⭐

```
🔒 SCOPE & HOISTING (Phạm Vi & Nâng Lên)
├── Scope Chain (Chuỗi Phạm Vi)
│   ├── Global Scope // Phạm vi toàn cục
│   ├── Function Scope // Phạm vi hàm
│   └── Block Scope (let/const) // Phạm vi khối (let/const)
│
├── Hoisting (Nâng Lên)
│   ├── var: hoisted + undefined // Nâng lên và gán undefined
│   ├── let/const: hoisted + TDZ (Temporal Dead Zone) // Nâng lên nhưng không truy cập được (vùng chết tạm thời)
│   └── function declaration: fully hoisted // Nâng lên hoàn toàn (có thể gọi trước khi khai báo)
│
└── Closures (Đóng Gói)
    ├── Function remembers outer scope // Hàm nhớ phạm vi bên ngoài
    ├── Private variables pattern // Mẫu biến riêng tư
    ├── Factory functions // Hàm tạo đối tượng
    └── ⚠️ Memory leak potential // Có thể gây rò rỉ bộ nhớ
```

**💡 Interview Tips (Mẹo Phỏng Vấn):**

- 🔗 Closure = function + lexical environment // Đóng gói = hàm + môi trường từ vựng

  - 💡 Hàm có thể truy cập biến từ scope bên ngoài, ngay cả khi scope đó đã kết thúc

- ⏳ TDZ = zone from start of block to declaration // Vùng chết tạm thời = từ đầu khối đến khai báo

  - 💡 `let/const` được hoisted nhưng không thể truy cập cho đến khi khai báo

- 📌 `var` là function-scoped, `let/const` là block-scoped
  - 💡 `var`: Phạm vi theo hàm (có thể truy cập trong toàn bộ hàm)
  - 💡 `let/const`: Phạm vi theo khối (chỉ trong `{}`)

---

### **1.3 ES6+ Modern Features** ⭐⭐⭐

```
🚀 ES6+ FEATURES (Tính Năng ES6+)
├── 📦 Variables (Biến)
│   ├── let/const (block scope) // Phạm vi khối
│   │   └── 💡 let: Có thể thay đổi, const: Không thể thay đổi (nhưng object/array bên trong có thể)
│   │   └── 💡 Block scope: Chỉ tồn tại trong {} (khác var là function scope)
│   └── Destructuring (object/array) // Phân rã object/mảng
│       └── 💡 const { name, age } = user; // Lấy name, age từ user
│       └── 💡 const [first, second] = arr; // Lấy phần tử đầu, thứ 2 từ mảng
│
├── 🔧 Functions (Hàm)
│   ├── Arrow functions (lexical this) // Hàm mũi tên (this từ vựng)
│   │   └── 💡 const fn = () => {}; // Ngắn gọn, this = this của scope bên ngoài
│   │   └── 💡 Không có arguments, không thể dùng làm constructor
│   ├── Default parameters // Tham số mặc định
│   │   └── 💡 function greet(name = 'Guest') {} // name mặc định là 'Guest'
│   └── Rest/Spread operators // Toán tử Rest/Spread
│       └── 💡 Rest: function(...args) {} // Gom tất cả arguments thành mảng
│       └── 💡 Spread: [...arr1, ...arr2] // Trải mảng thành các phần tử riêng lẻ
│
├── 🏛️ OOP (Object-Oriented Programming - Lập Trình Hướng Đối Tượng)
│   ├── Classes (syntactic sugar) // Lớp (đường cú pháp)
│   │   └── 💡 Cú pháp đẹp hơn, nhưng vẫn là prototype-based bên dưới
│   ├── Inheritance (extends) // Kế thừa
│   │   └── 💡 class Child extends Parent {} // Child kế thừa từ Parent
│   └── Static methods // Phương thức tĩnh
│       └── 💡 class Math { static add(a, b) {} } // Gọi: Math.add(), không cần instance
│
├── 📊 Data Structures (Cấu Trúc Dữ Liệu)
│   ├── Map/Set // Bản đồ/Tập hợp
│   │   └── 💡 Map: Key-value (key có thể là object), Set: Giá trị duy nhất
│   │   └── 💡 Map: new Map([['key', 'value']]), Set: new Set([1, 2, 3])
│   ├── WeakMap/WeakSet // Bản đồ/Tập hợp yếu
│   │   └── 💡 Key phải là object, không thể iterate, tự động GC khi object bị xóa
│   │   └── 💡 Dùng khi: Cache metadata, private data, không muốn giữ reference
│   └── Symbol // Ký hiệu
│       └── 💡 Giá trị duy nhất, dùng làm key cho object (tránh conflict)
│       └── 💡 const sym = Symbol('description'); // Mỗi Symbol là unique
│
└── ✨ Syntax (Cú Pháp)
    ├── Template literals // Chuỗi mẫu
    │   └── 💡 `Hello ${name}!` // Thay vì 'Hello ' + name + '!'
    │   └── 💡 Hỗ trợ multi-line, expression interpolation
    ├── Optional chaining (?.) // Chuỗi tùy chọn
    │   └── 💡 user?.address?.city // Trả về undefined nếu user hoặc address là null/undefined
    │   └── 💡 Tránh lỗi: Cannot read property 'city' of undefined
    └── Nullish coalescing (??) // Hợp nhất nullish
        └── 💡 value ?? 'default' // Chỉ dùng default nếu value là null hoặc undefined
        └── 💡 Khác ||: || dùng cho falsy (0, '', false), ?? chỉ cho null/undefined
```

---

### **1.4 `this` Binding & Functions** ⭐⭐⭐⭐

```
🎯 THIS BINDING (Thứ Tự Ưu Tiên - Priority Order)
1. new binding       → this = new object // Tạo object mới
   └── 💡 const obj = new MyClass(); // this = obj
2. explicit binding  → call/apply/bind // Ràng buộc rõ ràng
   └── 💡 fn.call(obj), fn.apply(obj), fn.bind(obj)
3. implicit binding  → obj.method() // Ràng buộc ngầm
   └── 💡 this = obj (object gọi method)
4. default binding   → global / undefined (strict) // Ràng buộc mặc định
   └── 💡 this = window (non-strict) hoặc undefined (strict)

📌 Arrow vs Regular Functions (So Sánh Hàm Mũi Tên vs Hàm Thường)
├── ➡️ Arrow: lexical this, no arguments, no constructor
│   └── 💡 this = this của scope bên ngoài (không thay đổi)
│   └── 💡 Không có arguments object, không thể dùng làm constructor
└── 🔧 Regular: dynamic this, has arguments, can be constructor
    └── 💡 this thay đổi tùy cách gọi (dynamic)
    └── 💡 Có arguments object, có thể dùng làm constructor
```

---

## 🟩 **2. ASYNC & PERFORMANCE**

### **2.1 Event Loop** ⭐⭐⭐⭐⭐ (MUST KNOW!)

```
♻️ EVENT LOOP FLOW (Luồng Vòng Lặp Sự Kiện)
┌─────────────────────────────────────────────────────────┐
│  Call Stack  →  Microtasks  →  Render  →  1 Macrotask  │
│      ↑__________________________________________________|
└─────────────────────────────────────────────────────────┘
💡 Thứ tự thực thi: Call Stack → Tất cả Microtasks → Render → 1 Macrotask → Lặp lại

📋 TASK QUEUES (Hàng Đợi Tác Vụ)
├── ⚡ Microtask Queue (HIGH PRIORITY - Ưu Tiên Cao)
│   ├── Promise.then/catch/finally // Callback của Promise
│   ├── queueMicrotask() // Hàm tạo microtask
│   └── MutationObserver // Quan sát thay đổi DOM
│   → 🔥 Chạy HẾT trước khi render (ưu tiên cao nhất)
│   → 💡 Phải xử lý hết microtasks mới render UI
│
└── 🐌 Macrotask Queue (LOW PRIORITY - Ưu Tiên Thấp)
    ├── setTimeout/setInterval // Hẹn giờ
    ├── I/O operations // Thao tác nhập/xuất
    └── requestAnimationFrame // Khung hình animation
    → ⏳ Chạy 1 task mỗi vòng (sau khi render)
    → 💡 Chỉ xử lý 1 macrotask rồi quay lại kiểm tra microtasks
```

---

### **2.2 Async Patterns** ⭐⭐⭐⭐

```
⚡ ASYNC EVOLUTION (Tiến Hóa Bất Đồng Bộ)
├── 📞 Callbacks (ES5) → Callback Hell // Địa ngục callback
│   └── 💡 Vấn đề: Code lồng nhau nhiều tầng, khó đọc
│
├── 🤝 Promises (ES6) // Lời hứa
│   ├── Promise.all() - Parallel, fail-fast // Song song, dừng khi 1 promise lỗi
│   │   └── 💡 Dùng khi: Cần tất cả promises thành công
│   ├── Promise.allSettled() - Wait all, no fail // Đợi tất cả, không dừng khi lỗi
│   │   └── 💡 Dùng khi: Cần kết quả tất cả promises (kể cả lỗi)
│   ├── Promise.race() - First settled // Promise nào xong trước (thành công hoặc lỗi)
│   │   └── 💡 Dùng khi: Timeout hoặc lấy kết quả nhanh nhất
│   └── Promise.any() - First fulfilled // Promise nào thành công trước
│       └── 💡 Dùng khi: Có nhiều nguồn dữ liệu, lấy cái nào có trước
│
├── ⏳ Async/Await (ES2017) // Cú pháp đồng bộ cho code bất đồng bộ
│   ├── Sequential: await a; await b; // Tuần tự (chậm hơn)
│   │   └── 💡 Dùng khi: b phụ thuộc vào kết quả của a
│   └── Parallel: await Promise.all([a, b]) // Song song (nhanh hơn)
│       └── 💡 Dùng khi: a và b độc lập, muốn chạy cùng lúc
│
└── 🚀 Advanced (Nâng Cao)
    ├── AbortController (Cancellation) // Hủy request đang chạy
    │   └── 💡 Dùng khi: User navigate away, component unmount
    ├── p-limit (Concurrency control) // Giới hạn số lượng request đồng thời
    │   └── 💡 Dùng khi: Tránh quá tải server (VD: chỉ 5 requests cùng lúc)
    └── Retry strategies (exponential backoff) // Chiến lược thử lại với backoff mũ
        └── 💡 Dùng khi: Network không ổn định, tăng dần thời gian chờ
```

---

### **2.3 Caching & Performance** ⭐⭐⭐⭐

```
🗄️ CACHING STRATEGIES (Chiến Lược Cache)
├── 🌐 HTTP Caching (Cache HTTP)
│   ├── Cache-Control (max-age, no-cache, no-store) // Điều khiển cache
│   │   └── 💡 max-age: Thời gian cache (VD: 3600 = 1 giờ)
│   ├── ETag / If-None-Match // Kiểm tra file có thay đổi không
│   │   └── 💡 Server trả 304 Not Modified nếu không đổi → tiết kiệm bandwidth
│   └── Last-Modified / If-Modified-Since // Kiểm tra theo ngày sửa
│
├── 💻 Browser Caching (Cache Trình Duyệt)
│   ├── Memory Cache (fastest, tab-specific) // Nhanh nhất, chỉ trong tab hiện tại
│   ├── Disk Cache (persistent) // Lưu trên ổ cứng, tồn tại sau khi đóng browser
│   └── Service Worker Cache (offline) // Cache cho offline, PWA
│
└── 📱 Application Caching (Cache Ứng Dụng)
    ├── React Query (stale-while-revalidate) // Hiển thị data cũ, fetch data mới ở background
    ├── SWR (stale-while-revalidate) // Tương tự React Query
    └── Apollo Cache (GraphQL) // Cache cho GraphQL queries

🎨 BROWSER RENDERING (Render Trình Duyệt)
├── 🛣️ Critical Rendering Path (Đường Dẫn Render Quan Trọng)
│   DOM → CSSOM → Render Tree → Layout → Paint → Composite
│   └── 💡 Quá trình browser chuyển HTML/CSS thành pixels trên màn hình
│
├── 📊 Performance Metrics (Chỉ Số Hiệu Suất)
│   ├── LCP (Largest Contentful Paint) < 2.5s // Thời gian render phần tử lớn nhất
│   ├── FID (First Input Delay) < 100ms // Độ trễ phản hồi tương tác đầu tiên
│   ├── CLS (Cumulative Layout Shift) < 0.1 // Độ dịch chuyển layout tích lũy
│   └── TTFB (Time To First Byte) < 800ms // Thời gian nhận byte đầu tiên từ server
│
└── ⚡ Optimization (Tối Ưu)
    ├── Avoid forced synchronous layout // Tránh layout đồng bộ bắt buộc
    │   └── 💡 Đọc offsetHeight → trigger layout → chậm!
    ├── Batch DOM reads/writes // Gộp đọc/ghi DOM
    │   └── 💡 Đọc tất cả → ghi tất cả (không xen kẽ)
    └── Use requestAnimationFrame for animations // Dùng cho animation
        └── 💡 Đồng bộ với refresh rate (60fps)
```

---

## 🟨 **3. REACT & FRAMEWORKS**

### **3.1 React Deep Dive** ⭐⭐⭐⭐⭐

```
⚛️ REACT CORE CONCEPTS (Khái Niệm Cốt Lõi React)
├── 🧩 Component Types (Loại Component)
│   ├── Functional Components (hooks) // Component hàm với hooks (khuyến nghị)
│   └── Class Components (legacy) // Component class (cũ, ít dùng)
│
├── 🪝 Hooks (Móc)
│   ├── 📊 State: useState, useReducer // Quản lý state
│   │   └── 💡 useState: State đơn giản, useReducer: State phức tạp
│   ├── ⚡ Effects: useEffect, useLayoutEffect // Side effects
│   │   └── 💡 useEffect: Sau render, useLayoutEffect: Trước paint
│   ├── 💾 Memoization: useMemo, useCallback // Ghi nhớ giá trị/hàm
│   │   └── 💡 Tránh tính toán lại không cần thiết
│   ├── 🔗 Refs: useRef, useImperativeHandle // Tham chiếu DOM
│   ├── 🌐 Context: useContext // Đọc Context
│   └── 🆕 New (React 19): useOptimistic, useFormStatus, use
│       └── 💡 useOptimistic: UI lạc quan, useFormStatus: Form status, use: Đọc promise/context
│
├── 🔄 State Management (Quản Lý State)
│   ├── 📍 Local: useState // State cục bộ trong component
│   ├── 🌍 Global: Context, Redux, Zustand, Jotai // State toàn cục
│   └── 🌐 Server: React Query, SWR // State từ server (API data)
│
├── ⚡ Performance (Hiệu Suất)
│   ├── React.memo (prevent re-renders) // Ngăn re-render không cần thiết
│   ├── useMemo (memoize values) // Ghi nhớ giá trị tính toán
│   ├── useCallback (memoize functions) // Ghi nhớ hàm
│   ├── Code splitting (React.lazy) // Chia nhỏ code, load khi cần
│   └── Virtualization (react-window) // Chỉ render phần tử visible
│
└── 🎨 Patterns (Mẫu Thiết Kế)
    ├── Compound Components // Component ghép (VD: <Tabs><Tab/></Tabs>)
    ├── Render Props // Truyền render function qua props
    ├── Higher-Order Components (HOC) // Component bọc component
    ├── Custom Hooks // Hooks tùy chỉnh (tái sử dụng logic)
    └── Container/Presentational // Tách logic và UI
```

---

### **3.2 Next.js 14/15/16** ⭐⭐⭐⭐⭐

```
🔺 NEXT.JS CONCEPTS (Khái Niệm Next.js)
├── 🎨 Rendering Strategies (Chiến Lược Render)
│   ├── SSR (Server-Side Rendering) - cache: 'no-store' // Render trên server mỗi request
│   │   └── 💡 Dùng khi: Data thay đổi thường xuyên, cần SEO
│   ├── SSG (Static Site Generation) - cache: 'force-cache' // Tạo tĩnh lúc build
│   │   └── 💡 Dùng khi: Data ít thay đổi, tốc độ cao nhất
│   ├── ISR (Incremental Static Regen) - revalidate: N // Tạo tĩnh, làm mới sau N giây
│   │   └── 💡 Dùng khi: Cần balance giữa tốc độ và data mới
│   └── CSR (Client-Side Rendering) // Render trên client
│       └── 💡 Dùng khi: Không cần SEO, tương tác nhiều
│
├── 🗂️ App Router (Next.js 13+) // Router mới dựa trên file system
│   ├── Server Components (default) // Component chạy trên server (mặc định)
│   │   └── 💡 Không gửi JS xuống client → bundle nhỏ hơn
│   ├── Client Components ('use client') // Component chạy trên client
│   │   └── 💡 Dùng khi: Cần interactivity (onClick, useState...)
│   ├── Server Actions ('use server') // Hàm chạy trên server
│   │   └── 💡 Gọi trực tiếp từ client, không cần API route
│   ├── Route Handlers (API Routes) // API endpoints
│   └── Streaming & Suspense // Streaming data, hiển thị từng phần
│
├── 📥 Data Fetching (Lấy Dữ Liệu)
│   ├── fetch() with caching options // fetch với tùy chọn cache
│   │   └── 💡 cache: 'force-cache' | 'no-store' | 'revalidate'
│   ├── Parallel fetching (Promise.all) // Lấy song song nhiều data
│   └── revalidatePath / revalidateTag // Làm mới cache theo path/tag
│
├── 📁 File-based Features (Tính Năng Dựa Trên File)
│   ├── page.tsx (routes) // Định nghĩa route
│   ├── layout.tsx (shared UI) // UI dùng chung (header, footer...)
│   ├── loading.tsx (loading UI) // UI khi đang tải
│   ├── error.tsx (error boundary) // UI khi có lỗi
│   └── not-found.tsx (404) // UI trang không tìm thấy
│
└── 🆕 Next.js 16 (MỚI!)
    ├── Turbopack (default bundler) // Bundler mặc định (nhanh hơn Webpack)
    ├── React 19 support // Hỗ trợ React 19
    └── Enhanced Server Actions // Server Actions cải tiến
```

---

### **3.3 State Management Comparison** ⭐⭐⭐⭐

```
🔄 STATE MANAGEMENT LIBRARIES (Thư Viện Quản Lý State)

┌─────────────┬────────────┬───────────┬─────────────┐
│   Feature   │   Redux    │  Zustand  │   Jotai     │
│   Tính Năng │            │           │             │
├─────────────┼────────────┼───────────┼─────────────┤
│ 📦 Bundle   │   ~8KB     │   ~2KB    │   ~3KB      │
│   Size      │   Lớn      │   Nhỏ     │   Nhỏ       │
│             │            │           │             │
│ 📝 Boiler-  │   High     │   Low     │   Minimal   │
│   plate     │   Nhiều    │   Ít      │   Tối thiểu  │
│             │            │           │             │
│ 🛠️ DevTools│   ✅ Rich  │   ✅ Good │   ✅ Good   │
│             │   Phong phú│   Tốt     │   Tốt       │
│             │            │           │             │
│ 📚 Learning │   Steep    │   Easy    │   Easy      │
│   Curve     │   Dốc      │   Dễ      │   Dễ        │
│             │            │           │             │
│ 🎯 Best For │ Enterprise │ Mid-size  │ Fine-grain  │
│             │   Doanh nghiệp│ Ứng dụng vừa│ Phản ứng chi tiết│
└─────────────┴────────────┴───────────┴─────────────┘

📌 When to use (Khi Nào Dùng):
├── 🔴 Redux: Large apps, complex state, middleware needs
│   └── 💡 App lớn, state phức tạp, cần middleware (logging, thunk...)
├── 🟢 Zustand: Most apps, simple API, small bundle
│   └── 💡 Hầu hết apps, API đơn giản, bundle nhỏ (khuyến nghị)
├── 🟡 Jotai: Fine-grained reactivity, atom-based
│   └── 💡 Phản ứng chi tiết, dựa trên atom (như Recoil)
└── 🔵 Context: Small apps, prop drilling solution
    └── 💡 App nhỏ, giải quyết prop drilling (không dùng cho state lớn)
```

---

## 🟧 **4. BUILD TOOLS & DEVOPS**

### **4.1 Build Tools Comparison** ⭐⭐⭐⭐

```
🔧 BUILD TOOLS ECOSYSTEM (Hệ Sinh Thái Công Cụ Build)

┌─────────────┬──────────────┬──────────────┬──────────────┐
│   Tool      │  Dev Speed   │  Build Speed │  Use Case    │
├─────────────┼──────────────┼──────────────┼──────────────┤
│ ⚡ Vite     │  ⚡⚡⚡⚡⚡    │  ⚡⚡⚡⚡     │  Modern apps │
│   └── 💡 ESM native, HMR cực nhanh                      │
│                                                           │
│ 🚀 Turbopack│  ⚡⚡⚡⚡⚡    │  ⚡⚡⚡⚡⚡   │  Next.js 16  │
│   └── 💡 Rust-based, nhanh nhất                          │
│                                                           │
│ 📦 Webpack  │  ⚡⚡        │  ⚡⚡⚡      │  Legacy/Complex│
│   └── 💡 Mạnh mẽ, nhiều plugin, nhưng chậm              │
│                                                           │
│ ⚙️ esbuild  │  ⚡⚡⚡⚡⚡    │  ⚡⚡⚡⚡⚡   │  Bundler/Minify│
│   └── 💡 Go-based, nhanh, dùng để minify                │
│                                                           │
│ 📚 Rollup   │  ⚡⚡⚡      │  ⚡⚡⚡⚡     │  Libraries   │
│   └── 💡 Tối ưu cho thư viện, tree-shaking tốt          │
└─────────────┴──────────────┴──────────────┴──────────────┘

📦 BUNDLER CONCEPTS (Khái Niệm Bundler)
├── 🌳 Tree Shaking (remove dead code) // Loại bỏ code không dùng
│   └── 💡 Giảm bundle size, chỉ bundle code thực sự dùng
├── ✂️ Code Splitting (lazy loading) // Chia nhỏ code, load khi cần
│   └── 💡 Giảm initial bundle, tăng tốc độ load trang
├── 🗜️ Minification (uglify/terser) // Nén code (xóa comment, rút gọn tên biến)
│   └── 💡 Giảm kích thước file, tăng tốc độ tải
├── 🗺️ Source Maps (debugging) // Bản đồ source code để debug
│   └── 💡 Map code đã minify về code gốc để debug dễ hơn
└── 🔥 Hot Module Replacement (HMR) // Thay thế module nóng
    └── 💡 Update code mà không reload trang (dev experience tốt)
```

---

### **4.2 Module Systems** ⭐⭐⭐

```
📦 ESM vs CommonJS (So Sánh Module Systems)

┌───────────────┬──────────────────┬──────────────────┐
│   Feature     │      ESM         │    CommonJS      │
│               │  (ES Modules)    │  (Node.js cũ)    │
├───────────────┼──────────────────┼──────────────────┤
│ 📝 Syntax     │ import/export    │ require/exports  │
│   └── 💡 ESM: import { x } from 'y'                │
│   └── 💡 CJS: const x = require('y')               │
│                                                      │
│ ⏳ Loading    │ Async (static)   │ Sync (dynamic)   │
│   └── 💡 ESM: Tải bất đồng bộ, phân tích tĩnh      │
│   └── 💡 CJS: Tải đồng bộ, có thể require động     │
│                                                      │
│ 🌳 Tree Shaking│ ✅ Yes           │ ❌ Limited       │
│   └── 💡 ESM: Loại bỏ code không dùng tốt          │
│   └── 💡 CJS: Khó tree-shake vì require động      │
│                                                      │
│ ⏸️ Top-level  │ ✅ await         │ ❌ No            │
│   └── 💡 ESM: Có thể dùng await ở top-level        │
│   └── 💡 CJS: Không hỗ trợ top-level await         │
│                                                      │
│ 🌐 Browser    │ ✅ Native        │ ❌ Bundler       │
│   └── 💡 ESM: Browser hỗ trợ native                │
│   └── 💡 CJS: Cần bundler (Webpack, Vite...)       │
│                                                      │
│ 🎯 this value │ undefined        │ module.exports   │
│   └── 💡 ESM: this = undefined (strict mode)      │
│   └── 💡 CJS: this = module.exports                │
└───────────────┴──────────────────┴──────────────────┘
```

---

### **4.3 TypeScript Advanced** ⭐⭐⭐⭐⭐

```
📘 TYPESCRIPT PATTERNS (Mẫu TypeScript)
├── 🔀 Generics (Kiểu Tổng Quát)
│   ├── Generic Functions // Hàm tổng quát
│   │   └── 💡 function identity<T>(arg: T): T { return arg; }
│   ├── Generic Constraints (extends) // Ràng buộc kiểu tổng quát
│   │   └── 💡 function getLength<T extends { length: number }>(obj: T)
│   └── Generic Utilities // Tiện ích tổng quát
│       └── 💡 type ApiResponse<T> = { data: T; error?: string; }
│
├── 🛠️ Utility Types (Kiểu Tiện Ích)
│   ├── Partial<T>, Required<T> // Một phần, Bắt buộc
│   │   └── 💡 Partial: Tất cả properties optional, Required: Tất cả required
│   ├── Pick<T, K>, Omit<T, K> // Chọn, Bỏ qua
│   │   └── 💡 Pick: Chọn properties, Omit: Bỏ qua properties
│   ├── Record<K, V> // Bản ghi
│   │   └── 💡 Record<string, number> = { [key: string]: number }
│   └── ReturnType<T>, Parameters<T> // Kiểu trả về, Tham số
│       └── 💡 ReturnType<typeof fn>: Kiểu giá trị trả về của hàm
│
├── 🚀 Advanced (Nâng Cao)
│   ├── Mapped Types // Kiểu ánh xạ
│   │   └── 💡 type Readonly<T> = { readonly [P in keyof T]: T[P] }
│   ├── Conditional Types // Kiểu điều kiện
│   │   └── 💡 type NonNullable<T> = T extends null | undefined ? never : T
│   ├── Type Guards (is, in) // Bảo vệ kiểu
│   │   └── 💡 function isString(x: unknown): x is string { return typeof x === 'string' }
│   ├── Branded Types // Kiểu có nhãn
│   │   └── 💡 type UserId = string & { __brand: 'UserId' } // Tránh nhầm lẫn
│   └── Template Literal Types // Kiểu chuỗi mẫu
│       └── 💡 type EventName = `on${Capitalize<string>}` // 'onClick', 'onSubmit'...
│
└── ✅ Best Practices (Thực Hành Tốt)
    ├── Prefer interfaces for objects // Ưu tiên interface cho object
    │   └── 💡 Interface: Có thể extend, merge declaration
    ├── Use type for unions/intersections // Dùng type cho union/intersection
    │   └── 💡 type Status = 'pending' | 'success' | 'error'
    └── Avoid any, use unknown // Tránh any, dùng unknown
        └── 💡 unknown: An toàn hơn, phải type check trước khi dùng
```

---

## 🟥 **5. SENIOR-LEVEL TOPICS**

### **5.1 System Design & Architecture** ⭐⭐⭐⭐⭐

```
🏗️ FRONTEND ARCHITECTURE (Kiến Trúc Frontend)
├── 🧩 Micro-Frontends (Vi Frontend)
│   ├── Module Federation // Chia sẻ code runtime
│   │   └── 💡 Webpack 5 / Vite Federation
│   ├── Multi-framework support // Hỗ trợ đa framework
│   │   └── 💡 React + Vue + Angular trong 1 app
│   └── Communication patterns (Events, SharedState) // Mẫu giao tiếp
│       └── 💡 Event Bus, Shared Store (Zustand/Redux)
│
├── 📦 Monorepo (Một Repo Nhiều Projects)
│   ├── Nx (recommended) // Khuyến nghị (Angular ecosystem)
│   │   └── 💡 Mạnh mẽ, có caching, dependency graph
│   ├── Turborepo // Vercel (nhanh, dễ setup)
│   └── Lerna (legacy) // Cũ, ít dùng
│
├── 🎨 Patterns (Mẫu Thiết Kế)
│   ├── BFF (Backend For Frontend) // Backend riêng cho frontend
│   │   └── 💡 Tối ưu API cho frontend, giảm số request
│   ├── Feature Flags // Cờ tính năng (bật/tắt feature)
│   │   └── 💡 Deploy code nhưng chưa bật, test từng phần
│   ├── A/B Testing // Test 2 phiên bản
│   │   └── 💡 So sánh hiệu quả 2 version
│   └── Error Boundaries // Ranh giới lỗi
│       └── 💡 Bắt lỗi, hiển thị fallback UI
│
└── 📈 Scalability (Khả Năng Mở Rộng)
    ├── Lazy loading // Tải chậm (load khi cần)
    ├── CDN optimization // Tối ưu CDN (phân phối nội dung)
    ├── Edge computing // Tính toán ở edge (gần user hơn)
    └── Server-side caching // Cache phía server
```

---

### **5.2 Security** ⭐⭐⭐⭐⭐

```
🔐 WEB SECURITY (7 LAYERS - 7 Tầng Bảo Mật)
├── 1. 🔒 HTTPS & TLS (Bảo Mật Kết Nối)
│   └── Certificate pinning, HSTS // Ghim chứng chỉ, HSTS
│       └── 💡 Mã hóa dữ liệu truyền tải, chống man-in-the-middle
│
├── 2. 🛡️ XSS Prevention (Ngăn Chặn XSS)
│   ├── Input sanitization (DOMPurify) // Làm sạch input
│   │   └── 💡 Loại bỏ script tags, event handlers độc hại
│   ├── Output encoding // Mã hóa output
│   │   └── 💡 Escape HTML entities (< → &lt;)
│   └── CSP headers // Content Security Policy
│       └── 💡 Chỉ cho phép script từ domain được phép
│
├── 3. 🔐 CSRF Protection (Bảo Vệ CSRF)
│   ├── CSRF tokens // Token chống CSRF
│   │   └── 💡 Token unique mỗi request, server verify
│   └── SameSite cookies // Cookie SameSite
│       └── 💡 Chống gửi cookie từ domain khác
│
├── 4. 🔑 Authentication (Xác Thực)
│   ├── Access Token (JWT - 15min) // Token truy cập (ngắn hạn)
│   │   └── 💡 Dùng để gọi API, hết hạn nhanh
│   ├── Refresh Token (7-30 days) // Token làm mới (dài hạn)
│   │   └── 💡 Dùng để lấy access token mới
│   └── Token rotation strategy // Chiến lược xoay token
│       └── 💡 Đổi refresh token mỗi lần dùng (bảo mật hơn)
│
├── 5. 💾 Secure Storage (Lưu Trữ An Toàn)
│   ├── httpOnly cookies (tokens) // Cookie httpOnly (token)
│   │   └── 💡 JavaScript không đọc được → chống XSS
│   ├── localStorage (non-sensitive) // localStorage (dữ liệu không nhạy cảm)
│   │   └── 💡 Theme, language, không lưu password/token
│   └── Avoid sessionStorage for auth // Tránh sessionStorage cho auth
│       └── 💡 Mất khi đóng tab, không phù hợp cho auth
│
├── 6. 🌐 API Security (Bảo Mật API)
│   ├── Rate limiting // Giới hạn số request
│   │   └── 💡 Chống DDoS, brute force
│   ├── Request validation // Xác thực request
│   │   └── 💡 Validate input, chống injection
│   └── CORS configuration // Cấu hình CORS
│       └── 💡 Chỉ cho phép domain được phép gọi API
│
└── 7. 📋 Headers (Tiêu Đề HTTP)
    ├── Content-Security-Policy // Chính sách bảo mật nội dung
    ├── X-Frame-Options // Chống clickjacking
    ├── X-Content-Type-Options // Chống MIME sniffing
    └── Referrer-Policy // Chính sách referrer
```

---

### **5.3 Testing Strategy** ⭐⭐⭐⭐⭐

```
🧪 TEST PYRAMID (Kim Tự Tháp Kiểm Thử)
         /\
        /E2E\       ← Playwright/Cypress (10%) // Test toàn bộ flow
       /------\
      /  INT   \    ← React Testing Library (20%) // Test component + logic
     /----------\
    /    UNIT    \  ← Jest/Vitest (70%) // Test hàm/component đơn lẻ
   /--------------\
💡 Nguyên tắc: Nhiều unit tests, ít E2E tests (nhanh hơn, rẻ hơn)

📋 TESTING TOOLS (Công Cụ Kiểm Thử)
├── 🔬 Unit Tests (Kiểm Thử Đơn Vị)
│   ├── Jest / Vitest // Framework test
│   │   └── 💡 Jest: Phổ biến, Vitest: Nhanh hơn (Vite-based)
│   └── Testing coverage (istanbul) // Độ phủ test
│       └── 💡 Mục tiêu: >80% coverage
│
├── 🔗 Integration Tests (Kiểm Thử Tích Hợp)
│   ├── React Testing Library // Test component như user dùng
│   │   └── 💡 Test behavior, không test implementation
│   └── MSW (Mock Service Worker) // Mock API calls
│       └── 💡 Mock network requests, không cần server thật
│
├── 🌐 E2E Tests (Kiểm Thử End-to-End)
│   ├── Playwright (recommended) // Khuyến nghị
│   │   └── 💡 Hỗ trợ nhiều browser, nhanh, stable
│   └── Cypress // Phổ biến, dễ dùng
│       └── 💡 Good DX, nhưng chỉ chạy trong Chrome
│
└── 🎨 Visual Regression (Kiểm Thử Hồi Quy Hình Ảnh)
    └── Chromatic / Percy // So sánh screenshot
        └── 💡 Phát hiện thay đổi UI không mong muốn
```

---

### **5.4 CI/CD & DevOps** ⭐⭐⭐⭐

```
🚀 CI/CD PIPELINE (Quy Trình CI/CD)
├── 🔨 Build Stage (Giai Đoạn Build)
│   ├── Install dependencies (cached) // Cài đặt dependencies (có cache)
│   │   └── 💡 Cache node_modules để tăng tốc
│   ├── Lint & Type check // Kiểm tra lint và type
│   │   └── 💡 ESLint, Prettier, TypeScript check
│   ├── Unit tests // Kiểm thử đơn vị
│   │   └── 💡 Jest/Vitest chạy nhanh, phát hiện lỗi sớm
│   └── Build artifacts // Tạo sản phẩm build
│       └── 💡 Tạo production bundle (dist/)
│
├── 🧪 Test Stage (Giai Đoạn Test)
│   ├── Integration tests // Kiểm thử tích hợp
│   │   └── 💡 Test component + logic cùng nhau
│   ├── E2E tests // Kiểm thử end-to-end
│   │   └── 💡 Playwright/Cypress test toàn bộ flow
│   └── Visual regression // Kiểm thử hồi quy hình ảnh
│       └── 💡 So sánh screenshot, phát hiện thay đổi UI
│
├── 🚢 Deploy Stage (Giai Đoạn Deploy)
│   ├── Preview deployments (PR) // Deploy preview cho PR
│   │   └── 💡 Mỗi PR có URL riêng để test
│   ├── Staging environment // Môi trường staging
│   │   └── 💡 Test trước khi lên production
│   └── Production (Blue-Green/Canary) // Production
│       └── 💡 Blue-Green: 2 môi trường, Canary: Deploy từng phần
│
└── 🛠️ Tools (Công Cụ)
    ├── GitHub Actions // CI/CD của GitHub
    │   └── 💡 Miễn phí cho public repo, dễ setup
    ├── GitLab CI // CI/CD của GitLab
    │   └── 💡 Tích hợp sẵn với GitLab
    ├── Vercel / Netlify // Platform tự động deploy
    │   └── 💡 Deploy tự động từ Git, preview cho PR
    └── 🐳 Docker & Containerization // Container hóa
        ├── Multi-stage builds (build + production) // Build nhiều giai đoạn
        │   └── 💡 Stage 1: Build app, Stage 2: Nginx serve static files
        ├── Docker Compose (local dev) // Docker Compose (phát triển cục bộ)
        │   └── 💡 Orchestrate frontend + backend + database
        ├── Layer caching (optimize build time) // Cache lớp (tối ưu thời gian build)
        │   └── 💡 Copy package.json trước → cache dependencies
        ├── Security hardening (non-root user) // Tăng cường bảo mật (user không phải root)
        │   └── 💡 Chạy container với user không phải root → giảm attack surface
        └── Kubernetes basics (production scale) // Kubernetes cơ bản (scale production)
            └── 💡 Container orchestration cho production, auto-scaling
```

---

### **5.5 Performance Monitoring** ⭐⭐⭐⭐

```
📊 APM (Application Performance Monitoring - Giám Sát Hiệu Suất Ứng Dụng)
├── 📈 Core Web Vitals (Chỉ Số Web Cốt Lõi)
│   ├── LCP < 2.5s (Largest Contentful Paint) // Thời gian render phần tử lớn nhất
│   │   └── 💡 Phần tử lớn nhất hiển thị trong < 2.5s → Tốt
│   ├── FID < 100ms (First Input Delay) // Độ trễ tương tác đầu tiên
│   │   └── 💡 User click → phản hồi trong < 100ms → Tốt
│   ├── CLS < 0.1 (Cumulative Layout Shift) // Độ dịch chuyển layout tích lũy
│   │   └── 💡 Layout không nhảy < 0.1 → Tốt (tránh layout shift)
│   └── INP < 200ms (Interaction to Next Paint) // Tương tác đến vẽ tiếp theo
│       └── 💡 Tương tác phản hồi trong < 200ms → Tốt (thay thế FID)
│
├── 🔍 Monitoring Tools (Công Cụ Giám Sát)
│   ├── Sentry (Error tracking) // Theo dõi lỗi
│   │   └── 💡 Bắt lỗi JS, stack trace, user context
│   ├── DataDog (Full APM) // APM đầy đủ
│   │   └── 💡 Performance, logs, traces, metrics (trả phí)
│   ├── LogRocket (Session replay) // Ghi lại phiên
│   │   └── 💡 Ghi lại màn hình user, debug dễ hơn
│   └── Lighthouse (Audits) // Kiểm tra
│       └── 💡 Performance, SEO, Accessibility, Best Practices
│
└── ⚡ Optimization (Tối Ưu)
    ├── Performance budgets // Ngân sách hiệu suất
    │   └── 💡 Giới hạn bundle size, số requests (VD: bundle < 200KB)
    ├── Bundle analysis // Phân tích bundle
    │   └── 💡 webpack-bundle-analyzer, source-map-explorer
    └── Real User Monitoring (RUM) // Giám sát người dùng thật
        └── 💡 Thu thập metrics từ user thật (khác lab testing)
```

---

## 🟪 **6. BỔ SUNG - TOPICS QUAN TRỌNG KHÁC**

### **6.1 React Query (TanStack Query)** ⭐⭐⭐⭐⭐

```
🔄 REACT QUERY (TanStack Query) - DATA FETCHING & CACHING LIBRARY
// Thư viện lấy dữ liệu & cache

├── 🎯 Core Concepts (Khái Niệm Cốt Lõi)
│   ├── Server State Management (khác Redux/Zustand) // Quản lý state từ server
│   │   └── 💡 Redux/Zustand: Client state, React Query: Server state
│   ├── Automatic Background Refetching // Tự động làm mới dữ liệu nền
│   │   └── 💡 Tự động fetch lại khi data stale, window focus...
│   ├── Caching & Deduplication // Cache và loại bỏ trùng lặp
│   │   └── 💡 Cùng query key → chỉ fetch 1 lần, share kết quả
│   └── Optimistic Updates // Cập nhật lạc quan (UI update trước, gọi API sau)
│       └── 💡 UI update ngay → Better UX → Rollback nếu lỗi
│
├── ⚡ Key Features (Tính Năng Chính)
│   ├── 📥 useQuery (GET data) // Hook lấy dữ liệu
│   │   ├── staleTime: 0 (data immediately stale) // Thời gian data cũ (0 = cũ ngay)
│   │   │   └── 💡 0 = luôn fetch lại, 5min = coi là mới trong 5 phút
│   │   ├── cacheTime: 5 min (garbage collection) // Thời gian giữ cache
│   │   │   └── 💡 Sau 5 phút không dùng → xóa khỏi cache
│   │   ├── refetchOnWindowFocus: true // Làm mới khi focus vào tab
│   │   │   └── 💡 User quay lại tab → tự động fetch data mới
│   │   └── retry: 3 lần // Thử lại 3 lần khi lỗi
│   │       └── 💡 Tự động retry với exponential backoff
│   │
│   ├── ✏️ useMutation (POST/PUT/DELETE) // Hook thay đổi dữ liệu
│   │   ├── onSuccess/onError callbacks // Callback khi thành công/lỗi
│   │   ├── Invalidate queries after success // Xóa cache sau khi thành công
│   │   │   └── 💡 Đảm bảo data luôn mới sau khi mutate
│   │   └── Optimistic updates // Cập nhật UI trước, call API sau
│   │       └── 💡 UI update ngay → Better UX
│   │
│   ├── ♾️ useInfiniteQuery (Pagination/Infinite scroll) // Hook phân trang vô hạn
│   │   ├── getNextPageParam // Lấy tham số trang tiếp theo
│   │   │   └── 💡 VD: return page + 1 hoặc cursor từ response
│   │   └── fetchNextPage() // Hàm load thêm dữ liệu
│   │       └── 💡 Gọi khi user scroll đến cuối
│   │
│   └── 🚀 Advanced (Nâng Cao)
│       ├── Prefetching (queryClient.prefetchQuery) // Tải trước dữ liệu
│       │   └── 💡 Prefetch khi hover link → load nhanh hơn
│       ├── Query Invalidation // Xóa cache query
│       │   └── 💡 invalidateQueries(['users']) → xóa tất cả queries có key 'users'
│       ├── Query Cancellation // Hủy request đang chạy
│       │   └── 💡 Component unmount → tự động cancel request
│       └── Dependent Queries (enabled based on condition) // Query phụ thuộc điều kiện
│           └── 💡 enabled: false → không fetch cho đến khi điều kiện đúng
│
├── ✅ Best Practices (Thực Hành Tốt)
│   ├── Use query keys properly ['users', userId] // Dùng query key đúng cách
│   │   └── 💡 Key phải unique, dễ invalidate
│   ├── Set appropriate staleTime & cacheTime // Đặt thời gian stale/cache phù hợp
│   │   └── 💡 Data ít đổi → staleTime cao, data thường đổi → staleTime thấp
│   ├── Handle loading/error states // Xử lý trạng thái loading/lỗi
│   │   └── 💡 Luôn hiển thị loading/error UI
│   └── Invalidate queries after mutations // Xóa cache sau khi mutation
│       └── 💡 Đảm bảo data sync sau khi thay đổi
│
└── 🎯 Use Cases (Trường Hợp Sử Dụng)
    ├── ✅ API calls, data fetching // Gọi API, lấy dữ liệu
    ├── ✅ Real-time updates (polling/SSE) // Cập nhật real-time
    ├── ✅ Offline support with cache // Hỗ trợ offline với cache
    └── ❌ Client state (use Zustand/Redux) // KHÔNG dùng cho state client
        └── 💡 Client state: UI state, form state → dùng Zustand/Redux

📝 EXAMPLE
const { data, isLoading, error } = useQuery({
  queryKey: ['todos'],
  queryFn: fetchTodos,
  staleTime: 5 * 60 * 1000, // 5 minutes
  cacheTime: 10 * 60 * 1000 // 10 minutes
});

const mutation = useMutation({
  mutationFn: createTodo,
  onSuccess: () => {
    queryClient.invalidateQueries(['todos']);
  }
});
```

---

### **6.2 AG Grid** ⭐⭐⭐⭐⭐

```
📊 AG GRID - ENTERPRISE DATA GRID (Best for Complex Tables)
// Bảng dữ liệu doanh nghiệp (Tốt nhất cho bảng phức tạp)

├── ⚡ Core Features (Tính Năng Cốt Lõi)
│   ├── Virtual Scrolling (handle millions of rows) // Cuộn ảo (xử lý hàng triệu dòng)
│   │   └── 💡 Chỉ render rows visible → performance tốt với 100k+ rows
│   ├── Column Pinning (left/right) // Ghim cột (trái/phải)
│   │   └── 💡 Giữ cột quan trọng luôn hiển thị khi scroll ngang
│   ├── Row Grouping & Aggregation // Nhóm dòng & tổng hợp
│   │   └── 💡 Nhóm theo category, tính tổng, trung bình...
│   ├── Sorting & Filtering (client & server-side) // Sắp xếp & lọc
│   │   └── 💡 Client: Nhanh cho data nhỏ, Server: Cần cho data lớn
│   ├── Cell Editing (inline & popup) // Sửa ô (trực tiếp/popup)
│   │   └── 💡 Sửa trực tiếp trong cell hoặc popup editor
│   └── CSV/Excel Export // Xuất CSV/Excel
│       └── 💡 Export toàn bộ data hoặc filtered data
│
├── 🚀 Advanced Features (Tính Năng Nâng Cao)
│   ├── Master-Detail (expandable rows) // Dòng mở rộng (chi tiết)
│   │   └── 💡 Click row → expand hiển thị chi tiết
│   ├── Tree Data // Dữ liệu dạng cây
│   │   └── 💡 Hiển thị hierarchical data (parent-child)
│   ├── Pivot Mode // Chế độ pivot (xoay bảng)
│   │   └── 💡 Chuyển rows thành columns (Excel pivot table)
│   ├── Charting Integration // Tích hợp biểu đồ
│   │   └── 💡 Vẽ chart từ grid data
│   ├── Server-Side Row Model (lazy loading) // Model server (load từ từ)
│   │   └── 💡 Load data từng phần từ server → handle data cực lớn
│   └── Custom Cell Renderers/Editors // Tùy chỉnh hiển thị/sửa ô
│       └── 💡 Render React component trong cell
│
├── ⚡ Performance (Hiệu Suất)
│   ├── Row Virtualization (only render visible rows) // Chỉ render dòng hiển thị
│   │   └── 💡 10k rows → chỉ render ~20 rows visible
│   ├── Column Virtualization // Ảo hóa cột
│   │   └── 💡 100 columns → chỉ render columns visible
│   ├── Debounced Filtering // Lọc với debounce
│   │   └── 💡 Tránh filter quá nhiều lần khi user đang gõ
│   └── Delta Updates (updateRowData) // Cập nhật từng phần
│       └── 💡 Chỉ update rows thay đổi → nhanh hơn update toàn bộ
│
├── 📊 Comparison (So Sánh)
│   ├── AG Grid vs TanStack Table
│   │   ├── AG Grid: Enterprise, full-featured, paid license
│   │   │   └── 💡 Đầy đủ tính năng, phải trả phí cho commercial
│   │   └── TanStack Table: Headless, free, more flexible
│   │       └── 💡 Chỉ logic, tự style, miễn phí, linh hoạt hơn
│   │
│   └── AG Grid vs MUI DataGrid
│       ├── AG Grid: Better performance, more features
│       │   └── 💡 Nhanh hơn, nhiều tính năng hơn
│       └── MUI DataGrid: Better UI, Material Design
│           └── 💡 UI đẹp hơn, Material Design
│
└── ✅ Best Practices (Thực Hành Tốt)
    ├── Use suppressColumnVirtualisation: false // Bật column virtualization
    ├── Enable pagination for >10k rows // Bật phân trang cho >10k dòng
    ├── Use getRowId for stable row references // Dùng getRowId cho row ổn định
    └── Debounce filter changes // Debounce khi filter thay đổi
```

📝 KEY CONFIG
const gridOptions = {
rowModelType: 'serverSide',
pagination: true,
paginationPageSize: 100,
cacheBlockSize: 100,
enableRangeSelection: true,
suppressColumnVirtualisation: false,
animateRows: true
};

```

---

### **6.3 Material-UI (MUI)** ⭐⭐⭐⭐⭐

```

🎨 REACT UI COMPONENT LIBRARY // Thư viện UI component React
├── Core Components // Component cốt lõi
│ ├── Layout // Bố cục
│ │ ├── Box (base component với sx prop) // Component cơ bản nhất
│ │ ├── Container, Grid, Stack // Container, lưới, stack
│ │ └── Paper, Card // Giấy, thẻ
│ │
│ ├── Inputs // Đầu vào
│ │ ├── TextField, Select, Autocomplete // Ô nhập, chọn, tự động hoàn thành
│ │ ├── Checkbox, Radio, Switch // Hộp kiểm, nút radio, công tắc
│ │ └── DatePicker, TimePicker // Chọn ngày, chọn giờ
│ │
│ ├── Navigation // Điều hướng
│ │ ├── AppBar, Toolbar, Drawer // Thanh app, thanh công cụ, ngăn kéo
│ │ ├── Tabs, Breadcrumbs // Tab, đường dẫn breadcrumb
│ │ └── BottomNavigation // Điều hướng dưới
│ │
│ └── Feedback // Phản hồi
│ ├── Dialog, Snackbar, Alert // Hộp thoại, thông báo nhỏ, cảnh báo
│ ├── Progress (Linear/Circular) // Tiến trình (dạng thanh/tròn)
│ └── Skeleton // Khung xương (loading placeholder)
│
├── Theming System // Hệ thống theme
│ ├── createTheme() // Tạo theme
│ │ ├── palette (primary, secondary, error...) // Bảng màu
│ │ ├── typography (h1-h6, body1-2...) // Kiểu chữ
│ │ ├── spacing (8px base unit) // Khoảng cách (đơn vị 8px)
│ │ └── breakpoints (xs, sm, md, lg, xl) // Điểm breakpoint responsive
│ │
│ ├── ThemeProvider // Provider cung cấp theme
│ ├── Dark Mode (mode: 'light' | 'dark') // Chế độ tối
│ └── Custom Theme Variables // Biến theme tùy chỉnh
│
├── Styling Solutions // Giải pháp styling
│ ├── sx prop (recommended) // Prop sx (khuyến nghị)
│ ├── styled() utility // Hàm styled
│ ├── makeStyles (deprecated in v5) // makeStyles (đã bỏ v5)
│ └── Emotion (CSS-in-JS engine) // Engine CSS-in-JS
│
├── Data Display // Hiển thị dữ liệu
│ ├── DataGrid (basic - free) // Bảng dữ liệu cơ bản (miễn phí)
│ ├── DataGridPro (advanced - paid) // Bảng nâng cao (trả phí)
│ ├── Table (native HTML table) // Bảng HTML thuần
│ └── List, Accordion // Danh sách, Accordion
│
└── Best Practices
├── Use sx prop over makeStyles
├── Leverage theme.spacing()
├── Customize via theme overrides
└── Use component prop for polymorphism

📝 THEMING EXAMPLE
const theme = createTheme({
palette: {
primary: { main: '#1976d2' },
secondary: { main: '#dc004e' }
},
typography: {
fontFamily: 'Roboto, Arial, sans-serif'
},
components: {
MuiButton: {
styleOverrides: {
root: { textTransform: 'none' }
}
}
}
});

```

---

### **6.4 Broadcast Channel API** ⭐⭐⭐

```

📡 CROSS-TAB COMMUNICATION // Giao tiếp giữa các tab
├── Overview // Tổng quan
│ ├── Browser API for tab-to-tab messaging // API gửi tin nhắn giữa các tab
│ ├── Same origin only // Chỉ cùng origin
│ ├── Faster than localStorage events // Nhanh hơn localStorage events
│ └── Use: Sync state across tabs // Dùng để: Đồng bộ state giữa tabs
│
├── API
│ ├── new BroadcastChannel(name) // Tạo kênh broadcast
│ ├── channel.postMessage(data) // Gửi tin nhắn
│ ├── channel.onmessage = (event) => {} // Lắng nghe tin nhắn
│ └── channel.close() // Đóng kênh
│
├── Use Cases // Trường hợp sử dụng
│ ├── Logout all tabs when user logs out // Logout tất cả tab khi user logout
│ ├── Sync shopping cart across tabs // Đồng bộ giỏ hàng giữa các tab
│ ├── Real-time notifications // Thông báo real-time
│ └── Multi-tab collaboration // Cộng tác đa tab
│
└── Alternative: localStorage events // Giải pháp thay thế
└── Less efficient, but universal support // Kém hiệu quả hơn, nhưng hỗ trợ rộng

📝 EXAMPLE
const channel = new BroadcastChannel('auth');

// Tab 1: Broadcast logout
channel.postMessage({ type: 'logout' });

// Tab 2: Listen for logout
channel.onmessage = (event) => {
if (event.data.type === 'logout') {
// Logout current tab
}
};

```

---

### **6.5 IndexedDB** ⭐⭐⭐⭐

```

💾 CLIENT-SIDE DATABASE // Database phía client
├── Features // Tính năng
│ ├── NoSQL key-value store // Lưu trữ key-value NoSQL
│ ├── Store large amounts of data (>250MB) // Lưu dữ liệu lớn (>250MB)
│ ├── Transactional (ACID) // Hỗ trợ giao dịch ACID
│ ├── Asynchronous API // API bất đồng bộ
│ └── Indexes for fast queries // Index để query nhanh
│
├── Use Cases // Trường hợp sử dụng
│ ├── ✅ Offline-first apps (PWA) // App offline-first (PWA)
│ ├── ✅ Caching API responses // Cache response API
│ ├── ✅ Store files/blobs // Lưu file/blob
│ └── ❌ Simple key-value (use localStorage) // Key-value đơn giản (dùng localStorage)
│
├── API (Low-level) // API cấp thấp
│ ├── indexedDB.open(dbName, version) // Mở database
│ ├── objectStore.add/put/get/delete // Thêm/sửa/lấy/xóa
│ ├── Indexes (createIndex) // Tạo index
│ └── Transactions // Giao dịch
│
├── Wrappers (Recommended) // Thư viện wrapper (khuyến nghị)
│ ├── Dexie.js (most popular) // Phổ biến nhất
│ ├── localForage (simple API) // API đơn giản
│ └── idb (Google's wrapper) // Wrapper của Google
│
└── Best Practices // Thực hành tốt
├── Use Dexie.js to avoid callback hell // Dùng Dexie tránh callback hell
├── Version your schema // Đánh version schema
└── Handle quota exceeded errors // Xử lý lỗi hết dung lượng

📝 DEXIE.JS EXAMPLE
const db = new Dexie('MyDatabase');
db.version(1).stores({
todos: '++id, text, completed'
});

await db.todos.add({ text: 'Learn IndexedDB' });
const todos = await db.todos.toArray();

```

---

### **6.6 WebSocket & Real-time** ⭐⭐⭐⭐

```

🔌 REAL-TIME COMMUNICATION // Giao tiếp thời gian thực
├── WebSocket
│ ├── Persistent bidirectional TCP connection // Kết nối TCP 2 chiều liên tục
│ ├── Protocol: ws:// (unsecure) / wss:// (SSL) // Giao thức ws/wss
│ ├── Lower latency than polling (~50ms) // Độ trễ thấp hơn polling
│ └── Use: Trading, Chat, Live notifications // Dùng: Giao dịch, chat, thông báo
│
├── Socket.IO
│ ├── WebSocket wrapper + fallback to polling // Wrapper WebSocket + dự phòng polling
│ ├── Auto-reconnect // Tự động kết nối lại
│ ├── Rooms & Namespaces // Phòng & không gian tên
│ └── Event-based API: socket.emit() // API dựa trên sự kiện
│
├── Server-Sent Events (SSE)
│ ├── Server → Client only (unidirectional) // Chỉ 1 chiều Server → Client
│ ├── Auto-reconnect built-in // Tự động kết nối lại có sẵn
│ └── Simpler than WebSocket // Đơn giản hơn WebSocket
│
└── Patterns // Mẫu thiết kế
├── Heartbeat/Ping-Pong (detect dead connections) // Nhịp tim (phát hiện kết nối chết)
├── Reconnection with exponential backoff // Kết nối lại với backoff mũ
└── Binary frames (faster than JSON) // Frame nhị phân (nhanh hơn JSON)

📊 COMPARISON
┌─────────────┬───────────┬───────────┬─────────────┐
│ Feature │ WebSocket │ Socket.IO │ SSE │
├─────────────┼───────────┼───────────┼─────────────┤
│ Direction │ Bi-direct │ Bi-direct │ Server→Client│
│ Reconnect │ Manual │ Auto │ Auto │
│ Fallback │ No │ Yes │ No │
│ Binary │ Yes │ Yes │ No │
│ Use Case │ Trading │ Chat │ Notifications│
└─────────────┴───────────┴───────────┴─────────────┘

```

---

### **6.2 Browser APIs & DOM** ⭐⭐⭐⭐

```

🌐 BROWSER APIs (API Trình Duyệt)
├── 👁️ Observer APIs (API Quan Sát)
│ ├── IntersectionObserver (lazy load, infinite scroll) // Quan sát giao nhau
│ │ └── 💡 Phát hiện element vào/ra viewport → lazy load images, infinite scroll
│ ├── ResizeObserver (element size changes) // Quan sát thay đổi kích thước
│ │ └── 💡 Phát hiện element thay đổi size → responsive layout
│ ├── MutationObserver (DOM changes) // Quan sát thay đổi DOM
│ │ └── 💡 Phát hiện DOM thay đổi → sync với external library
│ └── PerformanceObserver (performance metrics) // Quan sát hiệu suất
│ └── 💡 Thu thập metrics hiệu suất (LCP, FID, CLS...)
│
├── 💾 Storage APIs (API Lưu Trữ)
│ ├── localStorage (5MB, persistent) // Lưu trữ cục bộ (5MB, bền vững)
│ │ └── 💡 Tồn tại sau khi đóng browser, dùng cho theme, settings
│ ├── sessionStorage (5MB, tab-specific) // Lưu trữ phiên (5MB, theo tab)
│ │ └── 💡 Mất khi đóng tab, dùng cho form data tạm thời
│ ├── IndexedDB (large data, async) // Database lớn, bất đồng bộ
│ │ └── 💡 >250MB, dùng cho PWA, offline data
│ ├── Cookies (4KB, sent with requests) // Cookie (4KB, gửi với request)
│ │ └── 💡 Nhỏ, tự động gửi với HTTP request → dùng cho auth token
│ └── Cache API (Service Worker caching) // API Cache
│ └── 💡 Service Worker cache → offline support, PWA
│
├── 🎯 DOM Events (Sự Kiện DOM)
│ ├── Event Flow: Capturing → Target → Bubbling // Luồng sự kiện
│ │ └── 💡 Capturing: Từ root → target, Bubbling: Từ target → root
│ ├── Event Delegation (attach to parent) // Ủy quyền sự kiện
│ │ └── 💡 Attach listener ở parent → xử lý events từ children (hiệu quả hơn)
│ ├── stopPropagation() vs preventDefault() // Dừng lan truyền vs Ngăn mặc định
│ │ └── 💡 stopPropagation: Dừng bubbling, preventDefault: Ngăn hành vi mặc định
│ └── Passive listeners (improve scroll perf) // Listener thụ động
│ └── 💡 { passive: true } → browser không đợi preventDefault → scroll mượt hơn
│
└── 👷 Web Workers (Công Nhân Web)
├── Dedicated Worker (single script) // Worker chuyên dụng
│ └── 💡 1 script, 1 tab → xử lý heavy computation, không block UI
├── Shared Worker (shared across tabs) // Worker chia sẻ
│ └── 💡 Chia sẻ giữa nhiều tabs → sync state across tabs
└── Service Worker (offline, push notifications) // Worker dịch vụ
└── 💡 Proxy network requests → offline, push notifications, PWA

```

---

### **6.3 JavaScript Advanced Patterns** ⭐⭐⭐⭐⭐

```

🎨 DESIGN PATTERNS (Mẫu Thiết Kế)
├── 🏭 Creational (Tạo Đối Tượng)
│ ├── Singleton (one instance only) // Chỉ 1 instance
│ │ └── 💡 Đảm bảo chỉ có 1 instance (VD: Database connection)
│ ├── Factory (create objects) // Nhà máy tạo đối tượng
│ │ └── 💡 Hàm tạo object, ẩn logic tạo (VD: createUser(), createProduct())
│ └── Builder (step-by-step construction) // Xây dựng từng bước
│ └── 💡 Xây dựng object phức tạp từng bước (VD: query builder)
│
├── 🏗️ Structural (Cấu Trúc)
│ ├── Module (encapsulation) // Module (đóng gói)
│ │ └── 💡 Đóng gói code, export/import (ES6 modules)
│ ├── Facade (simplified interface) // Mặt tiền (giao diện đơn giản)
│ │ └── 💡 Đơn giản hóa API phức tạp (VD: jQuery)
│ └── Decorator (extend behavior) // Trang trí (mở rộng hành vi)
│ └── 💡 Thêm tính năng vào object mà không thay đổi cấu trúc
│
├── 🎭 Behavioral (Hành Vi)
│ ├── Observer/PubSub (event handling) // Quan sát/Phát hành-Đăng ký
│ │ └── 💡 Object thông báo thay đổi cho các observers (Event Bus)
│ ├── Strategy (interchangeable algorithms) // Chiến lược (thuật toán thay thế)
│ │ └── 💡 Chọn thuật toán lúc runtime (VD: payment methods)
│ └── Command (encapsulate actions) // Lệnh (đóng gói hành động)
│ └── 💡 Đóng gói request thành object → undo/redo, queue
│
└── 🚀 Advanced JS Features (Tính Năng JS Nâng Cao)
├── Proxy (intercept operations) // Proxy (chặn thao tác)
│ └── 💡 Use: Validation, logging, reactivity (Vue)
│ └── 💡 Chặn get/set operations → validation, logging, Vue reactivity
├── Generators (yield, iterators) // Generator (yield, iterator)
│ └── 💡 Use: Async iteration, infinite sequences
│ └── 💡 function\* gen() { yield 1; } → Lazy evaluation, async iteration
├── Reflect API // API Phản Chiếu
│ └── 💡 Reflect.get(), Reflect.set() → Meta programming
└── WeakRef & FinalizationRegistry // Tham Chiếu Yếu & Đăng Ký Hoàn Tất
└── 💡 WeakRef: Reference yếu, FinalizationRegistry: Cleanup khi GC

📦 REACT DESIGN PATTERNS (Mẫu Thiết Kế React)
├── 🧩 Compound Components (Component Ghép)
│ └── <Tabs><Tab/><TabPanel/></Tabs>
│ └── 💡 Components làm việc cùng nhau, share state ngầm
├── 🎨 Render Props (Props Render)
│ └── <DataProvider render={(data) => ...}/>
│ └── 💡 Truyền render function qua props → flexible, reusable
├── 🔄 Higher-Order Components (HOC) // Component Bậc Cao
│ └── withAuth(Component)
│ └── 💡 Component bọc component → thêm logic (auth, logging...)
├── 🪝 Custom Hooks (Hooks Tùy Chỉnh)
│ └── useLocalStorage, useDebounce
│ └── 💡 Tái sử dụng logic giữa components
├── 📦 Container/Presentational (Container/Presentational)
│ └── Logic vs UI separation
│ └── 💡 Container: Logic, Presentational: UI (tách biệt concerns)
└── 🎛️ Controlled vs Uncontrolled (Điều Khiển vs Không Điều Khiển)
└── Form components
└── 💡 Controlled: React quản lý state, Uncontrolled: DOM quản lý

```

---

### **6.4 CSS Architecture & Styling** ⭐⭐⭐⭐

```

🎨 CSS METHODOLOGIES (Phương Pháp CSS)
├── 🏷️ BEM (Block Element Modifier) // Khối Phần Tử Bổ Sung
│ └── .block\_\_element--modifier
│ └── 💡 .card\_\_title--large → Block: card, Element: title, Modifier: large
│ └── 💡 Quy ước đặt tên rõ ràng, tránh conflict
│
├── 📦 CSS Modules (Module CSS)
│ └── Scoped styles, no conflicts // Style có phạm vi, không conflict
│ └── 💡 Tự động hash class name → .Button_abc123 → tránh conflict
│
├── 💅 CSS-in-JS (CSS Trong JS)
│ ├── styled-components // Component có style
│ │ └── 💡 const Button = styled.button`color: red;`
│ ├── Emotion // Thư viện CSS-in-JS
│ │ └── 💡 Tương tự styled-components, performance tốt hơn
│ └── Pros: Dynamic, scoped / Cons: Runtime cost
│ └── 💡 Ưu: Dynamic, scoped, theme. Nhược: Runtime cost, bundle lớn
│
├── ⚡ Utility-First (Tailwind CSS) // Tiện Ích Đầu Tiên
│ └── Pros: Fast, consistent / Cons: Verbose HTML
│ └── 💡 Ưu: Nhanh, nhất quán, không cần viết CSS. Nhược: HTML dài
│
└── 🆕 Modern CSS (CSS Hiện Đại)
├── CSS Variables (Custom Properties) // Biến CSS
│ └── 💡 --primary-color: blue; → var(--primary-color) → Dynamic theming
├── Container Queries // Truy Vấn Container
│ └── 💡 @container (min-width: 300px) → Responsive theo container, không phải viewport
├── CSS Grid & Flexbox // Lưới & Hộp Linh Hoạt
│ └── 💡 Grid: 2D layout, Flexbox: 1D layout
├── CSS Layers (@layer) // Lớp CSS
│ └── 💡 @layer base, components, utilities → Kiểm soát cascade
└── CSS Nesting (native) // Lồng CSS (native)
└── 💡 .card { .title { color: red; } } → Lồng như SCSS, không cần preprocessor

📐 RESPONSIVE DESIGN (Thiết Kế Phản Hồi)
├── 📱 Mobile-First approach // Tiếp Cận Mobile Trước
│ └── 💡 Thiết kế cho mobile trước → mở rộng lên desktop (min-width)
├── 📏 Breakpoints strategy // Chiến Lược Điểm Ngắt
│ └── 💡 320px, 768px, 1024px, 1440px → Điểm ngắt chuẩn
├── 🌊 Fluid typography (clamp()) // Typography Lưu Động
│ └── 💡 font-size: clamp(1rem, 2vw, 2rem) → Tự động scale theo viewport
└── 📦 Container queries vs Media queries // Truy Vấn Container vs Truy Vấn Media
└── 💡 Container: Responsive theo container, Media: Responsive theo viewport

```

---

### **6.5 Git Workflow & Collaboration** ⭐⭐⭐

```

🔀 GIT STRATEGIES (Chiến Lược Git)
├── 🌿 Branching Models (Mô Hình Nhánh)
│ ├── Git Flow (feature/develop/release/hotfix) // Luồng Git
│ │ └── 💡 Nhiều nhánh: feature → develop → release → main (phức tạp, ít dùng)
│ ├── GitHub Flow (main + feature branches) // Luồng GitHub
│ │ └── 💡 Đơn giản: feature branch → PR → main (khuyến nghị)
│ └── Trunk-Based (small PRs to main) // Dựa Trên Thân
│ └── 💡 PR nhỏ, merge nhanh vào main → ít conflict, deploy nhanh
│
├── 🔀 Merge Strategies (Chiến Lược Merge)
│ ├── Merge commit (preserve history) // Commit merge (giữ lịch sử)
│ │ └── 💡 Tạo merge commit → giữ toàn bộ history, nhưng lịch sử phức tạp
│ ├── Squash merge (clean history) // Merge nén (lịch sử sạch)
│ │ └── 💡 Gộp tất cả commits thành 1 → lịch sử sạch, dễ đọc
│ └── Rebase (linear history) // Rebase (lịch sử tuyến tính)
│ └── 💡 Rebase feature branch lên main → lịch sử tuyến tính, nhưng rewrite history
│
├── ✅ Best Practices (Thực Hành Tốt)
│ ├── Conventional Commits (feat:, fix:, docs:) // Commit Chuẩn
│ │ └── 💡 feat: add login, fix: bug in auth, docs: update README
│ ├── Small, focused PRs // PR Nhỏ, Tập Trung
│ │ └── 💡 1 PR = 1 feature/fix → dễ review, dễ revert
│ ├── Code review culture // Văn Hóa Review Code
│ │ └── 💡 Review kỹ, comment constructive, approve khi sẵn sàng
│ └── Pre-commit hooks (Husky) // Hook Trước Commit
│ └── 💡 Tự động chạy lint, test trước khi commit → đảm bảo chất lượng
│
└── 🔧 Conflict Resolution (Giải Quyết Xung Đột)
├── git rebase --continue // Tiếp tục rebase
│ └── 💡 Sau khi resolve conflict, tiếp tục rebase
├── git merge --abort // Hủy merge
│ └── 💡 Hủy merge khi conflict quá phức tạp
└── Resolve in IDE (VS Code, JetBrains) // Giải quyết trong IDE
└── 💡 IDE có tool resolve conflict trực quan, dễ dùng

```

---

### **6.6 Accessibility (a11y)** ⭐⭐⭐⭐

```

♿ WEB ACCESSIBILITY (Khả Năng Truy Cập Web - a11y)
├── 📋 WCAG 2.1 Guidelines (Hướng Dẫn WCAG 2.1)
│ ├── 👁️ Perceivable (alt text, contrast) // Có Thể Nhận Biết
│ │ └── 💡 Alt text cho images, contrast ratio ≥ 4.5:1 cho text
│ ├── 🎮 Operable (keyboard nav, focus) // Có Thể Vận Hành
│ │ └── 💡 Điều hướng bằng keyboard, focus rõ ràng, không trap focus
│ ├── 📖 Understandable (clear labels) // Có Thể Hiểu
│ │ └── 💡 Label rõ ràng, error messages dễ hiểu, ngôn ngữ đơn giản
│ └── 🛡️ Robust (valid HTML, ARIA) // Mạnh Mẽ
│ └── 💡 HTML hợp lệ, ARIA đúng cách, tương thích screen reader
│
├── 🏷️ ARIA Attributes (Thuộc Tính ARIA)
│ ├── role="button", role="dialog" // Vai trò
│ │ └── 💡 role: Định nghĩa vai trò element (button, dialog, navigation...)
│ ├── aria-label, aria-labelledby // Nhãn
│ │ └── 💡 aria-label: Nhãn trực tiếp, aria-labelledby: Tham chiếu element khác
│ ├── aria-expanded, aria-hidden // Trạng thái
│ │ └── 💡 aria-expanded: Mở/đóng, aria-hidden: Ẩn khỏi screen reader
│ └── aria-live (announcements) // Thông báo
│ └── 💡 aria-live="polite": Thông báo thay đổi cho screen reader
│
├── ⌨️ Keyboard Navigation (Điều Hướng Bàn Phím)
│ ├── Tab order (tabindex) // Thứ Tự Tab
│ │ └── 💡 tabindex: 0 (bình thường), -1 (không tab), >0 (không khuyến nghị)
│ ├── Focus management // Quản Lý Focus
│ │ └── 💡 Focus vào modal khi mở, return focus khi đóng
│ └── Skip links // Liên Kết Bỏ Qua
│ └── 💡 Link bỏ qua navigation → jump đến main content
│
├── 🧪 Testing Tools (Công Cụ Kiểm Thử)
│ ├── axe-core / axe DevTools // Core Axe / DevTools Axe
│ │ └── 💡 Tự động phát hiện lỗi a11y, tích hợp vào CI/CD
│ ├── Lighthouse accessibility // Khả Năng Truy Cập Lighthouse
│ │ └── 💡 Audit a11y trong Chrome DevTools
│ └── Screen reader testing (NVDA, VoiceOver) // Kiểm Thử Screen Reader
│ └── 💡 Test với NVDA (Windows), VoiceOver (Mac) → trải nghiệm thật
│
└── ⚠️ Common Issues (Vấn Đề Thường Gặp)
├── Missing alt text // Thiếu văn bản thay thế
│ └── 💡 <img> không có alt → screen reader không biết image là gì
├── Low color contrast // Độ Tương Phản Màu Thấp
│ └── 💡 Text màu nhạt trên nền sáng → khó đọc
├── No focus indicators // Không Có Chỉ Báo Focus
│ └── 💡 Không thấy focus → user không biết đang ở đâu
└── Missing form labels // Thiếu Nhãn Form
└── 💡 <input> không có <label> → screen reader không biết input là gì

```

---

### **6.7 API Design & GraphQL** ⭐⭐⭐⭐

```

🔌 API PATTERNS (Mẫu API)
├── 🌐 REST API (API REST)
│ ├── Resources & HTTP methods // Tài Nguyên & Phương Thức HTTP
│ │ └── 💡 GET /users, POST /users, PUT /users/:id, DELETE /users/:id
│ ├── Status codes (200, 400, 401, 404, 500) // Mã Trạng Thái
│ │ └── 💡 200: OK, 400: Bad Request, 401: Unauthorized, 404: Not Found, 500: Server Error
│ ├── Pagination (offset, cursor) // Phân Trang
│ │ └── 💡 Offset: ?page=1&limit=10, Cursor: ?cursor=abc123 (tốt hơn cho large data)
│ └── Rate limiting // Giới Hạn Tỷ Lệ
│ └── 💡 Giới hạn số request/giờ → chống abuse, DDoS
│
├── 🔷 GraphQL (GraphQL)
│ ├── Query (read), Mutation (write) // Truy Vấn (đọc), Đột Biến (ghi)
│ │ └── 💡 Query: GET data, Mutation: POST/PUT/DELETE data
│ ├── Fragments (reusable fields) // Mảnh (trường tái sử dụng)
│ │ └── 💡 Tái sử dụng fields → DRY, dễ maintain
│ ├── Subscriptions (real-time) // Đăng Ký (thời gian thực)
│ │ └── 💡 WebSocket-based → real-time updates (chat, notifications)
│ └── Apollo Client (caching, state) // Client Apollo
│ └── 💡 Cache queries, normalize data, optimistic updates
│
├── 📊 GraphQL vs REST (So Sánh GraphQL vs REST)
│ ┌─────────────┬──────────────┬──────────────┐
│ │ Feature │ REST │ GraphQL │
│ │ Tính Năng │ │ │
│ ├─────────────┼──────────────┼──────────────┤
│ │ Data fetch │ Over/Under │ Exact data │
│ │ Lấy dữ liệu │ Thừa/Thiếu │ Chính xác │
│ │ │ │ │
│ │ Endpoints │ Multiple │ Single │
│ │ Điểm cuối │ Nhiều │ Một │
│ │ │ │ │
│ │ Versioning │ /v1, /v2 │ Schema evolution│
│ │ Phiên bản │ URL version │ Tiến hóa schema│
│ │ │ │ │
│ │ Caching │ HTTP cache │ Apollo/Relay │
│ │ Cache │ Cache HTTP │ Cache client │
│ │ │ │ │
│ │ Learning │ Easy │ Steeper │
│ │ Học │ Dễ │ Khó hơn │
│ └─────────────┴──────────────┴──────────────┘
│
└── ✅ HTTP Client Best Practices (Thực Hành Tốt Client HTTP)
├── Axios interceptors (auth, error handling) // Interceptor Axios
│ └── 💡 Tự động thêm token, xử lý lỗi global
├── Request/Response transformation // Chuyển Đổi Request/Response
│ └── 💡 Transform data trước khi gửi/nhận
├── Retry strategies // Chiến Lược Thử Lại
│ └── 💡 Retry với exponential backoff khi network lỗi
└── Request cancellation (AbortController) // Hủy Request
└── 💡 Hủy request khi component unmount → tránh memory leak

```

---

### **6.8 Date & Time Handling** ⭐⭐⭐

```

📅 DATE/TIME IN JAVASCRIPT (Ngày/Giờ Trong JavaScript)
├── 🆕 Native APIs (API Gốc)
│ ├── Date object (mutable, quirky) // Đối Tượng Ngày (có thể thay đổi, kỳ lạ)
│ │ └── 💡 Có thể thay đổi, month 0-indexed, parsing không nhất quán
│ ├── Intl.DateTimeFormat (localization) // Định Dạng Ngày/Giờ Quốc Tế
│ │ └── 💡 Format theo locale: 'en-US', 'vi-VN' → dễ dàng
│ └── Temporal API (upcoming standard) // API Thời Gian (sắp ra mắt)
│ └── 💡 API mới, immutable, timezone-aware (sẽ thay thế Date)
│
├── 📚 Libraries (Thư Viện)
│ ├── date-fns (functional, tree-shakeable) // Hàm, Có Thể Tree-Shake
│ │ └── 💡 Functional, tree-shakeable → bundle nhỏ, khuyến nghị
│ ├── Day.js (lightweight Moment alternative) // Nhẹ, Thay Thế Moment
│ │ └── 💡 2KB, API giống Moment → migration dễ
│ └── Luxon (Moment successor, immutable) // Kế Thừa Moment, Bất Biến
│ └── 💡 Immutable, timezone tốt hơn Moment
│
├── 🌍 Timezone Handling (Xử Lý Múi Giờ)
│ ├── Store in UTC, display in local // Lưu UTC, Hiển Thị Local
│ │ └── 💡 Luôn lưu UTC trong DB → convert sang local khi hiển thị
│ ├── ISO 8601 format (2024-01-15T10:30:00Z) // Định Dạng ISO 8601
│ │ └── 💡 Format chuẩn: YYYY-MM-DDTHH:mm:ssZ → parse dễ, không ambiguous
│ └── Intl.DateTimeFormat with timeZone option // Định Dạng Với Múi Giờ
│ └── 💡 new Intl.DateTimeFormat('en-US', { timeZone: 'Asia/Ho_Chi_Minh' })
│
└── ⚠️ Common Pitfalls (Cạm Bẫy Thường Gặp)
├── Month is 0-indexed (0 = January) // Tháng Bắt Đầu Từ 0
│ └── 💡 new Date(2024, 0, 15) → January 15, 2024 (0 = Jan, 11 = Dec)
├── Date parsing inconsistency across browsers // Parsing Không Nhất Quán
│ └── 💡 '2024-01-15' parse khác nhau → dùng ISO 8601 hoặc library
├── Daylight Saving Time edge cases // Trường Hợp Biên Giờ Tiết Kiệm Ánh Sáng
│ └── 💡 DST transition → 1 giờ có thể bị duplicate hoặc missing
└── Comparing dates (use timestamps) // So Sánh Ngày (Dùng Timestamp)
└── 💡 date1.getTime() === date2.getTime() → so sánh timestamp, không so object

```

---

### **6.9 Enterprise Data Grids (AG Grid)** ⭐⭐⭐⭐

```

📊 AG GRID (Enterprise) // Bảng Dữ Liệu Doanh Nghiệp
├── 🎯 Core Concepts (Khái Niệm Cốt Lõi)
│ ├── Column Definitions // Định Nghĩa Cột
│ │ └── 💡 Định nghĩa columns: field, headerName, width, sortable, filterable...
│ ├── Row Data (client-side / server-side) // Dữ Liệu Dòng
│ │ └── 💡 Client: Load tất cả, Server: Load từng phần (lazy loading)
│ ├── Cell Renderers & Editors // Renderer & Editor Ô
│ │ └── 💡 Custom component để render/edit cell (VD: React component)
│ └── Row Models (Client, Server, Infinite, Viewport) // Mô Hình Dòng
│ └── 💡 Client: Tất cả data, Server: Lazy load, Infinite: Scroll vô hạn, Viewport: Chỉ visible
│
├── ⚡ Performance Optimization (Tối Ưu Hiệu Suất)
│ ├── getRowId (stable row identity) // ID Dòng Ổn Định
│ │ └── 💡 getRowId: (params) => params.data.id → row ổn định, không re-render không cần thiết
│ ├── deltaRowDataMode (update only changes) // Chế Độ Cập Nhật Delta
│ │ └── 💡 Chỉ update rows thay đổi → nhanh hơn update toàn bộ
│ ├── applyTransactionAsync (batch updates) // Áp Dụng Giao Dịch Bất Đồng Bộ
│ │ └── 💡 Batch nhiều updates → render 1 lần → performance tốt hơn
│ └── Column virtualization // Ảo Hóa Cột
│ └── 💡 Chỉ render columns visible → handle 100+ columns
│
├── ✨ Features (Tính Năng)
│ ├── Sorting, Filtering, Grouping // Sắp Xếp, Lọc, Nhóm
│ │ └── 💡 Client-side: Nhanh cho data nhỏ, Server-side: Cần cho data lớn
│ ├── Row selection (single, multi) // Chọn Dòng
│ │ └── 💡 Chọn 1 dòng hoặc nhiều dòng → checkbox, keyboard selection
│ ├── Excel export // Xuất Excel
│ │ └── 💡 Export toàn bộ hoặc filtered data → Excel file
│ └── Master-Detail views // Xem Chủ-Chi Tiết
│ └── 💡 Expand row → hiển thị detail component
│
└── 🔄 Real-time Updates (Cập Nhật Thời Gian Thực)
├── WebSocket integration // Tích Hợp WebSocket
│ └── 💡 Kết nối WebSocket → update data real-time (trading, chat...)
├── Async transaction updates // Cập Nhật Giao Dịch Bất Đồng Bộ
│ └── 💡 applyTransactionAsync() → update không block UI
└── Cell flash on value change // Nhấp Nháy Ô Khi Giá Trị Thay Đổi
└── 💡 Cell flash màu khi value thay đổi → user thấy thay đổi ngay

```

---

## 🎯 **LEARNING PATH BY EXPERIENCE**

### **🌱 Junior (0-1 năm)**

```

Week 1-2: JS Fundamentals (Q01-Q08)
Week 3-4: ES6+ Features (Q09-Q10)
Week 5-6: DOM & Events (Q11-Q12)
Week 7-8: Async/Promises (Q13, Q19)
Week 9-10: React Hooks Basic (Q35)
Week 11-12: CSS Architecture (Q59)

```

### **🚀 Mid-Level (1-3 năm)**

```

Month 1: Event Loop Deep (Q06), Closures (Q08)
Month 2: React Query (Q17), Performance (Q38)
Month 3: Next.js (Q26, Q31), TypeScript (Q52)
Month 4: Testing (Q50), State Management (Q57)

```

### **🔥 Senior (3+ năm)**

```

Focus Areas:
├── System Design (Q49)
├── Security (Q39, Q43)
├── CI/CD (Q53)
├── Docker & Containerization (Q63)
├── Micro-frontends (Q44)
├── Performance Monitoring (Q51)
└── Design Patterns (Q60)

```

---

## 📝 **INTERVIEW PREPARATION CHECKLIST**

### **✅ Must-Know (All Levels) - Foundation**

- [ ] Event Loop & Microtask/Macrotask
- [ ] Closures & Scope Chain
- [ ] Async/Await & Promises (Promise.all, race, allSettled)
- [ ] React Hooks (useState, useEffect, useMemo, useCallback)
- [ ] `this` Binding (4 rules)
- [ ] ES6+ Features (destructuring, spread, arrow functions)
- [ ] Shallow vs Deep Copy
- [ ] DOM Events (bubbling, delegation)

### **✅ Mid-Level Add-ons (1-3 years)**

- [ ] React Query / SWR (data fetching & caching)
- [ ] Next.js App Router (SSR/SSG/ISR/Server Components)
- [ ] Performance Optimization (memo, lazy loading)
- [ ] TypeScript Generics & Utility Types
- [ ] State Management (Redux/Zustand comparison)
- [ ] Browser Storage APIs
- [ ] Observer APIs (Intersection, Resize, Mutation)
- [ ] HTTP Caching strategies

### **✅ Senior Requirements (3+ years)**

- [ ] System Design & Frontend Architecture
- [ ] Security (XSS, CSRF, Auth Flow, CSP)
- [ ] Testing Strategy (Unit/Integration/E2E)
- [ ] CI/CD Pipeline & DevOps
- [ ] Docker & Containerization (Multi-stage builds, Docker Compose, K8s basics)
- [ ] Micro-frontends & Module Federation
- [ ] WebSocket & Real-time communication
- [ ] Performance Monitoring (Core Web Vitals, APM)
- [ ] Code Review & Team Leadership
- [ ] Accessibility (WCAG, ARIA)
- [ ] JavaScript Design Patterns

### **✅ Tech Lead / Architect**

- [ ] Large-scale System Design
- [ ] Build Tool Deep Knowledge (Vite/Webpack internals)
- [ ] Monorepo Management (Nx/Turborepo)
- [ ] Docker & Kubernetes (Container orchestration, production deployment)
- [ ] API Design (REST vs GraphQL trade-offs)
- [ ] Performance Budgets & Optimization strategies
- [ ] Team processes & Documentation

---

## 📊 **INTERVIEW QUESTION FREQUENCY**

| Topic          | Junior | Mid | Senior | Frequency |
| -------------- | ------ | --- | ------ | --------- |
| Event Loop     | ✅     | ✅  | ✅     | 95%       |
| Closures       | ✅     | ✅  | ✅     | 90%       |
| React Hooks    | ✅     | ✅  | ✅     | 95%       |
| Async/Promises | ✅     | ✅  | ✅     | 90%       |
| TypeScript     | ❌     | ✅  | ✅     | 85%       |
| Next.js        | ❌     | ✅  | ✅     | 80%       |
| System Design  | ❌     | ❌  | ✅     | 75%       |
| Security       | ❌     | ❌  | ✅     | 70%       |
| Testing        | ❌     | ✅  | ✅     | 65%       |
| Performance    | ❌     | ✅  | ✅     | 75%       |

---

## 🔗 **QUICK REFERENCE LINKS**

| Topic         | Resource                                            |
| ------------- | --------------------------------------------------- |
| JavaScript    | [MDN Web Docs](https://developer.mozilla.org/)      |
| React         | [React.dev](https://react.dev/)                     |
| Next.js       | [Next.js Docs](https://nextjs.org/docs)             |
| TypeScript    | [TS Handbook](https://www.typescriptlang.org/docs/) |
| Testing       | [Testing Library](https://testing-library.com/)     |
| Accessibility | [WebAIM](https://webaim.org/)                       |
| Performance   | [web.dev/performance](https://web.dev/performance/) |
| Security      | [OWASP](https://owasp.org/)                         |

---

## 💡 **BONUS: COMMON INTERVIEW PATTERNS**

```

📍 Câu hỏi theo combo thường gặp:

🟢 Junior Interview (0-2 years):
Q: "Event Loop là gì?" → "Closures?" → "var vs let?" → "React hooks?"

🟡 Mid-level Interview (2-4 years):
Q: "Optimize React app?" → "SSR vs CSR?" → "Handle API errors?"
→ "TypeScript generics?" → "Testing approach?"

🔴 Senior Interview (4+ years):
Q: "Design chat system?" → "Micro-frontend architecture?"
→ "Security in banking app?" → "CI/CD pipeline?"
→ "Lead code review process?"

🟣 System Design Round:

- "Design infinite scroll feed"
- "Build real-time stock trading dashboard"
- "Architect e-commerce checkout flow"
- "Design collaborative document editor"

```

---

**Happy Learning! 🚀**

> _"The best way to predict the future is to implement it."_ - David Heinemeier Hansson

---

## 📅 **CHANGELOG**

- **v1.0** - Initial mindmap với 5 sections chính
- **v2.0** - Bổ sung Section 6: WebSocket, Browser APIs, CSS Architecture, Git Workflow, Accessibility, GraphQL, AG Grid, Design Patterns
- **v2.1** - Bổ sung Q63: Docker & Containerization for Frontend (Multi-stage builds, Docker Compose, Kubernetes basics)
- **Topics covered**: 63+ câu hỏi từ Junior đến Tech Lead
```
