  Bạn là senior/Stafff Fronteend Hãy gíup tôi trả lời các câu hỏi theo format

🧭 Điểm interviewer đang muốn nghe

━━━━━━━━━━━━━━
✅ Trả lời mẫu ngắn tự nhiên dễ hiểu
Em ...
━━━━━━━━━━━━━━
🔬 Trả lời sâu hơn và trade off
━━━━━━━━━━━━━━
🔁 Các câu hỏi liên quan đến chủ đề kèm câu trả lời 

🔎 Giải thích thuật ngữ của topic đó
  
  
  # 🧠 FRONTEND DEVELOPER KNOWLEDGE MINDMAP

  ## 📊 **VISUAL MINDMAP**

  ```
                                      ┌─────────────────────────────────────┐
                                      │     🎯 FRONTEND DEVELOPER          │
                                      │         KNOWLEDGE MAP              │
                                    │
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
                                              Docker/K8s                          OpenClaw / n8n
  ─────────    ─────────    ─────────────    ─────────────    ─────────────    ─────────────
  ```

  ---

  ## 🌳 **MINDMAP CHI TIẾT**

  ---

  ## 🟦 **1. JAVASCRIPT CORE FUNDAMENTALS**

  ### **1.1 Data Types & Memory** ⭐⭐⭐

  ```
  📦 DATA TYPES (Kiểu dữ liệu - 8 loại)
  ├── 🔷 Primitives (Kiểu nguyên thủy - 7 loại, Immutable/Bất biến)
  │   ├── number (số - số thực 64-bit, MAX_SAFE_INTEGER) // Số thực 64-bit; số nguyên an toàn trong khoảng ±2^53
  │   ├── string (chuỗi - UTF-16, immutable/bất biến) // Chuỗi ký tự UTF-16; mỗi lần "sửa" là tạo chuỗi mới
  │   ├── boolean (logic - true/false) // Chỉ có hai giá trị: đúng hoặc sai
  │   ├── null (rỗng có chủ ý - intentional empty) // Dùng khi cố ý gán "không có giá trị"
  │   ├── undefined (chưa khởi tạo - uninitialized) // Biến khai báo chưa gán, hoặc thuộc tính không tồn tại
  │   ├── symbol (ký hiệu - unique identifier) // Định danh duy nhất, thường dùng làm key object ẩn
  │   └── bigint (số nguyên lớn - arbitrary precision) // Số nguyên độ chính xác tùy ý, hậu tố n
  │
  ├── 🔶 Reference Type (Kiểu tham chiếu - 1 nhóm, Mutable/Có thể thay đổi)
  │   └── object (đối tượng: mảng, hàm, ngày, Map, Set...) // Mảng, hàm, Date, Map, Set đều là object
  │
  └── 💾 MEMORY MANAGEMENT (Quản lý bộ nhớ)
      ├── Stack (ngăn xếp - vùng nhớ nhanh, cố định): primitives, references // Lưu giá trị nguyên thủy và địa chỉ; LIFO (Vào sau ra trước)
      ├── Heap (vùng heap - vùng nhớ động, lớn): objects // Lưu object thật; kích thước linh hoạt, do GC quản lý
      └── Garbage Collection (thu gom rác - tự động giải phóng bộ nhớ): mark-and-sweep // Thuật toán đánh dấu rồi quét, xóa vùng không còn tham chiếu
  ```

  **🔑 Key Points (Điểm quan trọng):**

  - ⚖️ `==` vs `===` (so sánh ép kiểu vs so sánh nghiêm ngặt) // `==` tự ép kiểu hai bên rồi so; `===` so cả giá trị và kiểu
    - 💡 `==`: Tự động ép kiểu (1 == '1' → true) // Dễ gây bug, nên hạn chế dùng
    - 💡 `===`: Không ép kiểu (1 === '1' → false) // Nên dùng mặc định khi so sánh

  - 📋 Shallow copy (sao chép nông) vs Deep copy (sao chép sâu) — dùng `structuredClone()` để copy sâu // Copy nông chỉ copy "lớp ngoài", object lồng nhau vẫn trỏ chung
    - 💡 Shallow: Chỉ copy reference (tham chiếu) — sửa bản copy có thể ảnh hưởng bản gốc
    - 💡 Deep: Copy toàn bộ cây đối tượng — sửa bản copy không ảnh hưởng bản gốc

  - ❌ Falsy values (giá trị falsy): `0, "", null, undefined, false, NaN` // Trong điều kiện if/boolean được coi là false
    - 💡 Tất cả giá trị này trong ngữ cảnh boolean đều được coi là `false` // VD: if(0) không chạy

  - 🐛 `typeof null === "object"` (lỗi lịch sử của JS - legacy bug) // Bug từ phiên bản đầu, giữ lại để tương thích ngược
    - 💡 Cần kiểm tra null riêng: `value === null` hoặc `value == null` (bắt cả null và undefined)

  ---

  ### **1.2 Scope, Hoisting & Closures** ⭐⭐⭐⭐

  ```
  🔒 SCOPE & HOISTING (Phạm vi & Nâng khai báo)
  ├── Scope Chain (Chuỗi phạm vi - thứ tự tìm biến từ trong ra ngoài)
  │   ├── Global Scope (phạm vi toàn cục) // Biến khai báo ngoài mọi hàm, mọi file đều truy cập được
  │   ├── Function Scope (phạm vi hàm) // Biến chỉ tồn tại trong thân hàm đó
  │   └── Block Scope (phạm vi khối - let/const) // Biến trong {} chỉ sống trong cặp ngoặc đó
  │
  ├── Hoisting (nâng khai báo - engine "kéo" khai báo lên đầu scope trước khi chạy)
  │   ├── var: hoisted + gán undefined // Có thể dùng trước dòng khai báo, giá trị là undefined
  │   ├── let/const: hoisted + TDZ (Temporal Dead Zone - vùng chết tạm thời) // Nâng lên nhưng không truy cập được đến khi gặp dòng khai báo
  │   └── function declaration: fully hoisted (nâng hoàn toàn) // Có thể gọi hàm trước dòng khai báo
  │
  └── Closures (bao đóng - hàm "nhớ" biến của scope bên ngoài)
      ├── Function remembers outer scope (lexical environment - môi trường từ vựng) // Hàm giữ tham chiếu tới biến ngoài dù scope ngoài đã chạy xong
      ├── Private variables pattern (mẫu biến riêng tư) // Dùng closure để tạo biến không cho truy cập trực tiếp từ ngoài
      ├── Factory functions (hàm tạo đối tượng) // Hàm trả về hàm/object, mỗi lần gọi có closure riêng
      └── ⚠️ Memory leak potential (nguy cơ rò rỉ bộ nhớ) // Giữ reference quá lâu khiến GC không thu hồi được
  ```

  **💡 Interview Tips (Mẹo phỏng vấn):**

  - 🔗 Closure (bao đóng) = function + lexical environment (hàm + môi trường từ vựng) // Định nghĩa ngắn gọn để trả lời phỏng vấn
    - 💡 Hàm có thể truy cập biến từ scope bên ngoài, ngay cả khi scope đó đã kết thúc

  - ⏳ TDZ (Temporal Dead Zone - vùng chết tạm thời) = từ đầu block đến dòng khai báo // Khoảng không thể truy cập biến let/const
    - 💡 `let/const` được hoisted nhưng không thể truy cập cho đến khi gặp dòng khai báo

  - 📌 `var` là function-scoped (phạm vi hàm), `let/const` là block-scoped (phạm vi khối)
    - 💡 `var`: Phạm vi theo hàm (có thể truy cập trong toàn bộ hàm)
    - 💡 `let/const`: Phạm vi theo khối (chỉ trong `{}`)

  ---

  ### **1.3 ES6+ Modern Features** ⭐⭐⭐

  ```
  🚀 ES6+ FEATURES (Tính năng ES6+)
  ├── 📦 Variables (Biến)
  │   ├── let/const (block scope - phạm vi khối) // Chỉ tồn tại trong {}
  │   │   └── 💡 let: Có thể gán lại; const: Không gán lại (object/array bên trong vẫn sửa được)
  │   │   └── 💡 Block scope: Khác var (function scope - phạm vi hàm)
  │   └── Destructuring (phân rã - object/array) // Lấy thuộc tính/phần tử ra biến riêng
  │       └── 💡 const { name, age } = user; const [first, second] = arr;
  │
  ├── 🔧 Functions (Hàm)
  │   ├── Arrow functions (hàm mũi tên - lexical this) // this lấy từ scope bên ngoài
  │   │   └── 💡 const fn = () => {}; Không có arguments, không dùng làm constructor
  │   ├── Default parameters (tham số mặc định) // Giá trị mặc định khi không truyền
  │   │   └── 💡 function greet(name = 'Guest') {}
  │   └── Rest/Spread (gom phần còn lại / trải phần tử) // Rest: ...args; Spread: [...arr]
  │       └── 💡 Rest: gom arguments thành mảng; Spread: trải mảng/object
  │
  ├── 🏛️ OOP (Object-Oriented Programming - Lập trình hướng đối tượng)
  │   ├── Classes (lớp - syntactic sugar/đường cú pháp) // Cú pháp đẹp, bên dưới vẫn prototype
  │   ├── Inheritance (kế thừa - extends) // class Child extends Parent {}
  │   └── Static methods (phương thức tĩnh) // Gọi qua class, không cần instance
  │       └── 💡 Math.add(a, b) — không cần new Math()
  │
  ├── 📊 Data Structures (Cấu trúc dữ liệu)
  │   ├── Map/Set (bản đồ / tập hợp) // Map: key-value (key có thể object); Set: giá trị duy nhất
  │   ├── WeakMap/WeakSet (bản đồ/tập hợp yếu) // Key phải object; GC tự thu khi không còn tham chiếu
  │   │   └── 💡 Dùng: cache metadata, dữ liệu riêng tư, tránh giữ reference lâu
  │   └── Symbol (ký hiệu) // Giá trị duy nhất, dùng làm key object (tránh trùng tên)
  │
  └── ✨ Syntax (Cú pháp)
      ├── Template literals (chuỗi mẫu) // `Hello ${name}!`, multi-line, expression
      ├── Optional chaining (?.) (chuỗi tùy chọn) // user?.address?.city → undefined nếu null/undefined
      └── Nullish coalescing (??) (gộp nullish) // value ?? 'default' — chỉ với null/undefined (khác ||)
  ```

  ---

  ### **1.4 `this` Binding & Functions** ⭐⭐⭐⭐

  ```
  🎯 THIS BINDING (Ràng buộc this - thứ tự ưu tiên)
  1. new binding (ràng buộc new)       → this = object mới tạo
    └── 💡 const obj = new MyClass(); // this = obj
  2. explicit binding (ràng buộc tường minh)  → call/apply/bind
    └── 💡 fn.call(obj), fn.apply(obj), fn.bind(obj) — truyền this bằng tay
  3. implicit binding (ràng buộc ngầm)  → obj.method()
    └── 💡 this = obj (object gọi method)
  4. default binding (ràng buộc mặc định)   → global / undefined (strict)
    └── 💡 this = window (non-strict) hoặc undefined (strict mode)

  📌 Arrow vs Regular Functions (Hàm mũi tên vs Hàm thường)
  ├── ➡️ Arrow: lexical this (this từ vựng), không có arguments, không làm constructor
  │   └── 💡 this “mượn” từ scope ngoài; không có arguments object
  └── 🔧 Regular: dynamic this (this động), có arguments, có thể làm constructor
      └── 💡 this phụ thuộc cách gọi; có arguments; dùng new được
  ```

  ---

  ## 🟩 **2. ASYNC & PERFORMANCE**

  ### **2.1 Event Loop (Vòng Lặp Sự Kiện - cơ chế xử lý code bất đồng bộ)** ⭐⭐⭐⭐⭐ (MUST KNOW!)

  ```
  ♻️ EVENT LOOP FLOW (Luồng vòng lặp sự kiện)
  ┌─────────────────────────────────────────────────────────┐
  │  Call Stack  →  Microtasks  →  Render  →  1 Macrotask  │
  │  (Ngăn xếp   (Nhiệm vụ vi   (Vẽ frame)  (1 nhiệm vụ   │
  │   gọi hàm)    mô)                       vĩ mô)        │
  │      ↑__________________________________________________|
  └─────────────────────────────────────────────────────────┘
  💡 Thứ tự: Call Stack (ngăn xếp gọi) → hết Microtasks → Render (vẽ) → 1 Macrotask → lặp lại

  📋 TASK QUEUES (Hàng đợi tác vụ)
  ├── ⚡ Microtask Queue (hàng đợi vi nhiệm vụ - ưu tiên cao nhất)
  │   ├── Promise.then/catch/finally // Callback của Promise
  │   ├── queueMicrotask() // Hàm đưa callback vào hàng microtask
  │   └── MutationObserver (quan sát thay đổi DOM) // API quan sát DOM
  │   → 🔥 Chạy hết microtasks trước khi browser vẽ frame
  │
  └── 🐌 Macrotask Queue (hàng đợi vĩ nhiệm vụ - ưu tiên thấp hơn)
      ├── setTimeout/setInterval (hẹn giờ) // Gọi lại sau N ms
      ├── I/O operations (thao tác nhập/xuất) // Đọc file, network...
      └── requestAnimationFrame (khung hình animation) // Đồng bộ với refresh rate
      → ⏳ Mỗi vòng chỉ lấy 1 macrotask, xong lại xử lý hết microtasks
  ```

  ---

  ### **2.2 Async Patterns** ⭐⭐⭐⭐

  ```
  ⚡ ASYNC EVOLUTION (Tiến hóa bất đồng bộ)
  ├── 📞 Callbacks (ES5) → Callback Hell (địa ngục callback) // Code lồng nhau nhiều tầng, khó đọc
  │
  ├── 🤝 Promises (ES6 - lời hứa)
  │   ├── Promise.all() - Parallel (song song), fail-fast (dừng khi 1 lỗi) // Cần tất cả thành công
  │   ├── Promise.allSettled() - Wait all (đợi hết), không fail-fast // Cần kết quả cả thành công lẫn lỗi
  │   ├── Promise.race() - First settled (cái xong trước) // Timeout hoặc lấy nhanh nhất
  │   └── Promise.any() - First fulfilled (cái thành công trước) // Nhiều nguồn, lấy cái có trước
  │
  ├── ⏳ Async/Await (ES2017 - cú pháp đồng bộ cho code bất đồng bộ)
  │   ├── Sequential (tuần tự): await a; await b; // b chờ a xong
  │   └── Parallel (song song): await Promise.all([a, b]) // a, b chạy cùng lúc
  │
  └── 🚀 Advanced (Nâng cao)
      ├── AbortController (hủy request) // Hủy fetch khi navigate away hoặc unmount
      ├── p-limit (giới hạn đồng thời - concurrency control) // VD: tối đa 5 request cùng lúc
      └── Retry strategies (chiến lược thử lại) - exponential backoff (tăng dần thời gian chờ) // Network không ổn định
  ```

  ---

  ### **2.3 Caching & Performance** ⭐⭐⭐⭐

  ```
  🗄️ CACHING STRATEGIES (Chiến lược cache)
  ├── 🌐 HTTP Caching (Cache HTTP)
  │   ├── Cache-Control (điều khiển cache: max-age, no-cache, no-store) // max-age: thời gian giữ cache (VD: 3600 = 1h)
  │   ├── ETag / If-None-Match (nhãn phiên bản / kiểm tra bản mới) // Server trả 304 Not Modified → tiết kiệm băng thông
  │   └── Last-Modified / If-Modified-Since (ngày sửa / kiểm tra theo ngày) // Validator kiểu ngày
  │
  ├── 💻 Browser Caching (Cache trình duyệt)
  │   ├── Memory Cache (cache bộ nhớ - nhanh nhất, theo tab) // Chỉ trong tab hiện tại
  │   ├── Disk Cache (cache đĩa - bền vững) // Lưu ổ cứng, còn sau khi đóng browser
  │   └── Service Worker Cache (cache offline - PWA) // Cache cho offline, Progressive Web App
  │
  └── 📱 Application Caching (Cache ứng dụng)
      ├── React Query / SWR (stale-while-revalidate - cũ trong khi làm mới) // Hiển thị data cũ, fetch mới nền
      └── Apollo Cache (cache GraphQL) // Cache cho query GraphQL

  🎨 BROWSER RENDERING (Render trình duyệt)
  ├── 🛣️ Critical Rendering Path (đường dẫn render quan trọng)
  │   DOM → CSSOM → Render Tree → Layout → Paint → Composite
  │   └── 💡 DOM (cây HTML), CSSOM (cây CSS), Render Tree (kết hợp), Layout (vị trí), Paint (vẽ), Composite (ghép lớp)
  │
  ├── 📊 Performance Metrics (Chỉ số hiệu suất - Core Web Vitals)
  │   ├── LCP (Largest Contentful Paint - thời gian nội dung lớn nhất hiển thị) < 2.5s
  │   ├── FID (First Input Delay - độ trễ tương tác đầu tiên) < 100ms
  │   ├── CLS (Cumulative Layout Shift - độ nhảy layout tích lũy) < 0.1
  │   └── TTFB (Time To First Byte - thời gian byte đầu từ server) < 800ms
  │
  └── ⚡ Optimization (Tối ưu)
      ├── Avoid forced synchronous layout (tránh layout đồng bộ cưỡng bức) // Đọc offsetHeight giữa frame → trigger layout → chậm
      ├── Batch DOM reads/writes (gộp đọc/ghi DOM) // Đọc hết rồi ghi hết, không xen kẽ
      └── requestAnimationFrame for animations (khung hình animation) // Đồng bộ 60fps
  ```

  ---

  ## 🟨 **3. REACT & FRAMEWORKS**

  ### **3.1 React Deep Dive** ⭐⭐⭐⭐⭐

  ```
  ⚛️ REACT CORE CONCEPTS (Khái niệm cốt lõi React)
  ├── 🧩 Component Types (Loại component)
  │   ├── Functional Components (component hàm - dùng hooks) // Khuyến nghị, viết function
  │   └── Class Components (component class - legacy/cũ) // Ít dùng, viết class
  │
  ├── 🪝 Hooks (Móc)
  │   ├── 📊 State: useState, useReducer (quản lý state) // useState: đơn giản; useReducer: phức tạp
  │   ├── ⚡ Effects: useEffect, useLayoutEffect (side effect) // useEffect: sau render; useLayoutEffect: trước paint
  │   ├── 💾 Memoization (ghi nhớ): useMemo, useCallback // useMemo: nhớ giá trị; useCallback: nhớ hàm
  │   ├── 🔗 Refs: useRef, useImperativeHandle (tham chiếu DOM/instance) // Trỏ tới DOM hoặc giá trị giữ qua re-render
  │   ├── 🌐 Context: useContext (đọc Context) // Lấy giá trị từ Provider
  │   └── 🆕 React 19: useOptimistic (UI lạc quan), useFormStatus (trạng thái form), use (đọc promise/context)
  │
  ├── 🔄 State Management (Quản lý state)
  │   ├── 📍 Local: useState (state cục bộ) // Trong một component
  │   ├── 🌍 Global: Context, Redux, Zustand, Jotai (state toàn cục) // Nhiều component dùng chung
  │   └── 🌐 Server: React Query, SWR (state từ server) // Dữ liệu API, cache, refetch
  │
  ├── ⚡ Performance (Hiệu suất)
  │   ├── React.memo (ngăn re-render) // So sánh props, không re-render nếu giống
  │   ├── useMemo (ghi nhớ giá trị) // Chỉ tính lại khi deps thay đổi
  │   ├── useCallback (ghi nhớ hàm) // Tránh tạo hàm mới mỗi lần render
  │   ├── Code splitting (tách code - React.lazy) // Load component khi cần
  │   └── Virtualization (ảo hóa - react-window) // Chỉ render phần tử trong viewport
  │
  └── 🎨 Patterns (Mẫu thiết kế)
      ├── Compound Components (component ghép) // VD: <Tabs><Tab/><TabPanel/></Tabs> — share state ngầm
      ├── Render Props (truyền hàm render qua props) // Linh hoạt, tái sử dụng
      ├── HOC - Higher-Order Components (component bọc component) // withAuth(Page)
      ├── Custom Hooks (hooks tùy chỉnh) // Tái sử dụng logic (useLocalStorage, useDebounce)
      └── Container/Presentational (tách logic và UI) // Container: logic; Presentational: chỉ hiển thị
  ```

  ---

  ### **3.2 Next.js 14/15/16** ⭐⭐⭐⭐⭐

  ```
  🔺 NEXT.JS CONCEPTS (Khái Niệm Next.js)
  ├── 🎨 Rendering Strategies (Chiến Lược Render)
  │   ├── SSR (Server-Side Rendering - render phía server mỗi request) - cache: 'no-store' // Render trên server mỗi request
  │   │   └── 💡 Dùng khi: Data thay đổi thường xuyên, cần SEO
  │   ├── SSG (Static Site Generation - tạo trang tĩnh lúc build) - cache: 'force-cache' // Tạo tĩnh lúc build
  │   │   └── 💡 Dùng khi: Data ít thay đổi, tốc độ cao nhất
  │   ├── ISR (Incremental Static Regeneration - tạo tĩnh tăng dần) - revalidate: N // Tạo tĩnh, làm mới sau N giây
  │   │   └── 💡 Dùng khi: Cần balance giữa tốc độ và data mới
  │   └── CSR (Client-Side Rendering - render phía client) // Render trên client
  │       └── 💡 Dùng khi: Không cần SEO, tương tác nhiều
  │
  ├── 🗂️ App Router (Next.js 13+) // Router mới dựa trên file system
  │   ├── Server Components (component phía server - không gửi JS xuống client) (default) // Component chạy trên server (mặc định)
  │   │   └── 💡 Không gửi JS xuống client → bundle nhỏ hơn
  │   ├── Client Components (component phía client - có tương tác) ('use client') // Component chạy trên client
  │   │   └── 💡 Dùng khi: Cần interactivity (onClick, useState...)
  │   ├── Server Actions ('use server') // Hàm chạy trên server
  │   │   └── 💡 Gọi trực tiếp từ client, không cần API route
  │   ├── Route Handlers (API Routes) // API endpoints
  │   └── Streaming & Suspense (truyền dữ liệu từng phần) // Streaming data, hiển thị từng phần
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
  │   └──
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

  📌 When to use (Khi nào dùng):
  ├── 🔴 Redux: Ứng dụng lớn, state phức tạp, cần middleware (logging, thunk...)
  │   └── 💡 Boilerplate nhiều, learning curve dốc, phù hợp enterprise
  ├── 🟢 Zustand: Hầu hết app, API đơn giản, bundle nhỏ (khuyến nghị)
  │   └── 💡 Ít boilerplate, dễ học
  ├── 🟡 Jotai: Fine-grained reactivity (phản ứng hạt nhỏ), atom-based (theo nguyên tử)
  │   └── 💡 Mỗi “atom” là một mảnh state, component chỉ subscribe đúng cái cần
  └── 🔵 Context: App nhỏ, giải quyết prop drilling (truyền props qua nhiều tầng)
      └── 💡 Không nên dùng cho state lớn hay thay đổi thường xuyên (re-render nhiều)
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

  📦 BUNDLER CONCEPTS (Khái niệm bundler)
  ├── 🌳 Tree Shaking (loại bỏ code chết) // Chỉ bundle code được import, bỏ code không dùng
  │   └── 💡 Hiệu quả với ESM + named import; giảm bundle size
  ├── ✂️ Code Splitting (tách code - lazy loading) // Chia bundle, load từng phần khi cần (VD theo route)
  │   └── 💡 Giảm initial load, tăng tốc FCP
  ├── 🗜️ Minification (nén code - uglify/terser) // Xóa comment, khoảng trắng, rút gọn tên biến
  │   └── 💡 Giảm kích thước file production
  ├── 🗺️ Source Maps (bản đồ mã nguồn) // Map file đã nén về code gốc để debug
  └── 🔥 HMR - Hot Module Replacement // Sửa code → cập nhật trình duyệt không reload, giữ state
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
  ├── 🔀 Generics (kiểu tổng quát)
  │   ├── Generic Functions (hàm tổng quát) // function identity<T>(arg: T): T
  │   ├── Generic Constraints - extends (ràng buộc kiểu) // T extends { length: number }
  │   └── Generic Utilities (tiện ích tổng quát) // type ApiResponse<T> = { data: T; error?: string }
  │
  ├── 🛠️ Utility Types (kiểu tiện ích)
  │   ├── Partial<T> (một phần - tất cả optional), Required<T> (bắt buộc)
  │   ├── Pick<T, K> (chọn thuộc tính), Omit<T, K> (bỏ thuộc tính)
  │   ├── Record<K, V> (bản ghi key-value) // Record<string, number>
  │   └── ReturnType<T>, Parameters<T> (kiểu trả về / tham số của hàm)
  │
  ├── 🚀 Advanced (Nâng cao)
  │   ├── Mapped Types (kiểu ánh xạ) // { readonly [P in keyof T]: T[P] }
  │   ├── Conditional Types (kiểu điều kiện) // T extends X ? A : B
  │   ├── Type Guards (bảo vệ kiểu - is, in) // function isString(x): x is string
  │   ├── Branded Types (kiểu có nhãn) // string & { __brand: 'UserId' } — tránh nhầm string thường
  │   └── Template Literal Types (kiểu chuỗi mẫu) // `on${Capitalize<string>}` → 'onClick', 'onSubmit'...
  │
  └── ✅ Best Practices (Thực hành tốt)
      ├── Prefer interfaces for objects (ưu tiên interface cho object) // Có thể extend, merge
      ├── Use type for unions/intersections (dùng type cho union/intersection) // type Status = 'a' | 'b'
      └── Avoid any, use unknown (tránh any, dùng unknown) // unknown bắt phải check kiểu trước khi dùng
  ```

  ---

  ## 🟥 **5. SENIOR-LEVEL TOPICS**

  ### **5.1 System Design & Architecture** ⭐⭐⭐⭐⭐

  ```
  🏗️ FRONTEND ARCHITECTURE (Kiến Trúc Frontend)
  ├── 🧩 Micro-Frontends (vi frontend - chia nhỏ ứng dụng thành các phần độc lập) (Vi Frontend)
  │   ├── Module Federation (liên kết module - chia sẻ code runtime giữa các app) // Chia sẻ code runtime
  │   │   └── 💡 Webpack 5 / Vite Federation
  │   ├── Multi-framework support // Hỗ trợ đa framework
  │   │   └── 💡 React + Vue + Angular trong 1 app
  │   └── Communication patterns (Events, SharedState) // Mẫu giao tiếp
  │       └── 💡 Event Bus, Shared Store (Zustand/Redux)
  │
  ├── 📦 Monorepo (một repo nhiều dự án - quản lý nhiều app/lib trong 1 repo) (Một Repo Nhiều Projects)
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
  ├── 2. 🛡️ XSS (Cross-Site Scripting - tấn công chèn mã độc) Prevention (Ngăn Chặn XSS)
  │   ├── Input sanitization (làm sạch input - loại bỏ mã độc) (DOMPurify) // Làm sạch input
  │   │   └── 💡 Loại bỏ script tags, event handlers độc hại
  │   ├── Output encoding // Mã hóa output
  │   │   └── 💡 Escape HTML entities (< → &lt;)
  │   └── CSP (Content Security Policy - chính sách bảo mật nội dung) headers // Content Security Policy
  │       └── 💡 Chỉ cho phép script từ domain được phép
  │
  ├── 3. 🔐 CSRF (Cross-Site Request Forgery - giả mạo request từ trang khác) Protection (Bảo Vệ CSRF)
  │   ├── CSRF tokens (token chống CSRF - xác minh request hợp lệ) // Token chống CSRF
  │   │   └── 💡 Token unique mỗi request, server verify
  │   └── SameSite cookies (cookie SameSite - không gửi từ domain khác) // Cookie SameSite
  │       └── 💡 Chống gửi cookie từ domain khác
  │
  ├── 4. 🔑 Authentication (Xác Thực)
  │   ├── Access Token (JWT - JSON Web Token - token truy cập ngắn hạn 15min) // Token truy cập (ngắn hạn)
  │   │   └── 💡 Dùng để gọi API, hết hạn nhanh
  │   ├── Refresh Token (token làm mới - dài hạn 7-30 ngày) (7-30 days) // Token làm mới (dài hạn)
  │   │   └── 💡 Dùng để lấy access token mới
  │   └── Token rotation strategy (chiến lược xoay token - thay token mỗi lần dùng) // Chiến lược xoay token
  │       └── 💡 Đổi refresh token mỗi lần dùng (bảo mật hơn)
  │
  ├── 5. 💾 Secure Storage (Lưu Trữ An Toàn)
  │   ├── httpOnly cookies (cookie chỉ server đọc được - chống XSS) (tokens) // Cookie httpOnly (token)
  │   │   └── 💡 JavaScript không đọc được → chống XSS
  │   ├── localStorage (non-sensitive) // localStorage (dữ liệu không nhạy cảm)
  │   │   └── 💡 Theme, language, không lưu password/token
  │   └── Avoid sessionStorage for auth // Tránh sessionStorage cho auth
  │       └── 💡 Mất khi đóng tab, không phù hợp cho auth
  │
  ├── 6. 🌐 API Security (Bảo Mật API)
  │   ├── Rate limiting (giới hạn tốc độ request - chống DDoS) // Giới hạn số request
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
  🧪 TEST PYRAMID (Kim tự tháp kiểm thử)
          /\
          /E2E\       ← Playwright/Cypress (10%) - End-to-End (test toàn bộ luồng)
        /------\
        /  INT   \    ← React Testing Library (20%) - Integration (component + logic)
      /----------\
      /    UNIT    \  ← Jest/Vitest (70%) - Unit (hàm/component đơn lẻ)
    /--------------\
  💡 Nguyên tắc: Nhiều unit (nhanh, rẻ), ít E2E (chậm, đắt)

  📋 TESTING TOOLS (Công cụ kiểm thử)
  ├── 🔬 Unit Tests (Kiểm thử đơn vị): Jest/Vitest; coverage (độ phủ) mục tiêu >80%
  ├── 🔗 Integration Tests (Kiểm thử tích hợp): React Testing Library (test behavior); MSW (Mock Service Worker - mock API)
  ├── 🌐 E2E Tests (Kiểm thử end-to-end): Playwright (khuyến nghị), Cypress
  └── 🎨 Visual Regression (Hồi quy hình ảnh): Chromatic/Percy — so sánh screenshot, phát hiện thay đổi UI
  ```

  ---

  ### **5.4 CI/CD & DevOps** ⭐⭐⭐⭐

  ```
  🚀 CI/CD PIPELINE (Quy trình tích hợp & triển khai liên tục)
  ├── 🔨 Build Stage (Giai đoạn build): Install deps (cache), Lint & Type check, Unit tests, Build artifacts (dist/)
  ├── 🧪 Test Stage (Giai đoạn test): Integration tests, E2E tests, Visual regression (screenshot)
  ├── 🚢 Deploy Stage (Giai đoạn deploy): Preview (mỗi PR có URL), Staging (test trước prod), Production (Blue-Green/Canary — 2 môi trường / deploy từng phần)
  └── 🛠️ Tools: GitHub Actions, GitLab CI, Vercel/Netlify; Docker (Multi-stage builds, Docker Compose, layer caching, security hardening non-root); Kubernetes basics (container orchestration, auto-scaling)
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

  ├── 🎯 Core Concepts (Khái niệm cốt lõi)
  │   ├── Server State Management (quản lý state từ server - khác Redux/Zustand) // Redux/Zustand: client state; RQ: server state
  │   ├── Automatic Background Refetching (tự động làm mới nền) // Khi data stale, window focus...
  │   ├── Caching & Deduplication (cache và bỏ trùng) // Cùng query key → chỉ fetch 1 lần, share kết quả
  │   └── Optimistic Updates (cập nhật lạc quan) // Cập nhật UI trước, gọi API sau; rollback nếu lỗi
  │
  ├── ⚡ Key Features (Tính năng chính)
  │   ├── 📥 useQuery (GET data - hook lấy dữ liệu)
  │   │   ├── staleTime (thời gian coi là “mới”) // 0 = cũ ngay; 5min = trong 5 phút không refetch
  │   │   ├── cacheTime (thời gian giữ trong cache) // Hết thời gian không dùng → GC xóa
  │   │   ├── refetchOnWindowFocus (làm mới khi focus tab) // User quay lại tab → fetch mới
  │   │   └── retry (số lần thử lại khi lỗi) // Mặc định 3, có exponential backoff
  │   ├── ✏️ useMutation (POST/PUT/DELETE - hook thay đổi dữ liệu) // onSuccess/onError; invalidate queries; optimistic update
  │   ├── ♾️ useInfiniteQuery (phân trang / infinite scroll) // getNextPageParam, fetchNextPage()
  │   └── 🚀 Advanced: Prefetching (tải trước), Query Invalidation (xóa cache), Query Cancellation (hủy request), Dependent Queries (enabled: false)
  │
  ├── ✅ Best Practices (Thực hành tốt)
  │   ├── Query key rõ ràng ['users', userId] // Unique, dễ invalidate
  │   ├── staleTime/cacheTime phù hợp // Data ít đổi → staleTime cao
  │   ├── Luôn xử lý loading/error UI
  │   └── Invalidate sau mutation // Đảm bảo data đồng bộ
  │
  └── 🎯 Use Cases (Trường hợp sử dụng)
      ├── ✅ API calls, data fetching, real-time (polling/SSE), offline với cache
      └── ❌ Client state (UI state, form state) → dùng Zustand/Redux
  ```



  ### **6.2 AG Grid** ⭐⭐⭐⭐⭐

  ```
  📊 AG GRID - ENTERPRISE DATA GRID (Bảng dữ liệu doanh nghiệp - tốt cho bảng phức tạp)

  ├── ⚡ Core Features (Tính năng cốt lõi)
  │   ├── Virtual Scrolling (cuộn ảo - chỉ render dòng nhìn thấy) // Hàng triệu dòng vẫn mượt
  │   ├── Column Pinning (ghim cột trái/phải) // Cột quan trọng luôn hiển thị khi scroll ngang
  │   ├── Row Grouping & Aggregation (nhóm dòng & tổng hợp) // Nhóm theo category, sum, avg...
  │   ├── Sorting & Filtering (sắp xếp & lọc - client hoặc server-side) // Client: data nhỏ; Server: data lớn
  │   ├── Cell Editing (sửa ô - inline hoặc popup) // Sửa trong ô hoặc popup
  │   └── CSV/Excel Export (xuất CSV/Excel) // Export toàn bộ hoặc đã lọc
  │
  ├── 🚀 Advanced (Tính năng nâng cao)
  │   ├── Master-Detail (dòng mở rộng chi tiết) // Click row → expand
  │   ├── Tree Data (dữ liệu cây - parent-child) // Hierarchical
  │   ├── Pivot Mode (chế độ pivot - xoay bảng) // Rows thành columns
  │   ├── Server-Side Row Model (mô hình dòng phía server - lazy load) // Load từng phần từ server
  │   └── Custom Cell Renderers/Editors (tùy chỉnh hiển thị/sửa ô) // React component trong cell
  │
  ├── ⚡ Performance (Hiệu suất)
  │   ├── Row/Column Virtualization (ảo hóa dòng/cột) // Chỉ render phần visible
  │   ├── Debounced Filtering (lọc có debounce) // Tránh filter liên tục khi gõ
  │   └── Delta Updates (cập nhật từng phần - updateRowData) // Chỉ update dòng thay đổi
  │
  ├── 📊 So sánh: AG Grid (enterprise, trả phí) vs TanStack Table (headless, free) vs MUI DataGrid (UI đẹp, Material)
  └── ✅ Best Practices: Bật column virtualization, phân trang >10k rows, getRowId ổn định, debounce filter
  ```

  **📝 KEY CONFIG:**

  ```javascript
  const gridOptions = {
    rowModelType: 'serverSide',
    pagination: true,
    paginationPageSize: 100,
    cacheBlockSize: 100,
    enableRangeSelection: true,
    suppressColumnVirtualisation: false,
    animateRows: true,
  };
  ```

  ---

  ### **6.3 Material-UI (MUI)** ⭐⭐⭐⭐⭐

  ```
  🎨 MUI - REACT UI COMPONENT LIBRARY (Thư viện component UI React)
  ├── Core Components (Component cốt lõi): Layout (Box, Container, Grid, Stack, Paper, Card), Inputs (TextField, Select, Autocomplete, Checkbox, Radio, Switch, DatePicker), Navigation (AppBar, Toolbar, Drawer, Tabs, Breadcrumbs), Feedback (Dialog, Snackbar, Alert, Progress, Skeleton)
  ├── Theming System (Hệ thống theme): createTheme() — palette (bảng màu), typography (kiểu chữ), spacing (8px base), breakpoints (xs→xl); ThemeProvider; Dark Mode; Custom variables
  ├── Styling: sx prop (khuyến nghị), styled(), makeStyles (deprecated v5), Emotion (CSS-in-JS)
  ├── Data Display: DataGrid (cơ bản, free), DataGridPro (nâng cao, paid), Table, List, Accordion
  └── Best Practices: Ưu tiên sx prop, dùng theme.spacing(), tùy chỉnh qua theme overrides, component prop cho polymorphism (đa hình)
  ```

  **📝 THEMING EXAMPLE:**

  ```javascript
  const theme = createTheme({
    palette: {
      primary: { main: '#1976d2' },
      secondary: { main: '#dc004e' },
    },
    typography: {
      fontFamily: 'Roboto, Arial, sans-serif',
    },
    components: {
      MuiButton: {
        styleOverrides: {
          root: { textTransform: 'none' },
        },
      },
    },
  });
  ```

  ---

  ### **6.4 Broadcast Channel API** ⭐⭐⭐

  ```
  📡 BROADCAST CHANNEL API (Giao tiếp giữa các tab)
  ├── Overview (Tổng quan): Browser API gửi tin nhắn tab-to-tab; same origin only (chỉ cùng nguồn); nhanh hơn localStorage events
  ├── API: new BroadcastChannel(name) (tạo kênh), postMessage(data) (gửi), onmessage (lắng nghe), close() (đóng)
  ├── Use Cases (Trường hợp dùng): Logout tất cả tab, đồng bộ giỏ hàng, thông báo real-time, cộng tác đa tab
  └── Alternative (Thay thế): localStorage + event storage — kém hiệu quả hơn nhưng hỗ trợ rộng
  ```

  **📝 EXAMPLE:**

  ```javascript
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

  ### **6.5 IndexedDB (database NoSQL phía client)** ⭐⭐⭐⭐

  ```
  💾 INDEXEDDB (Database phía client - NoSQL key-value)
  ├── Features (Tính năng): NoSQL key-value store (lưu key-value); >250MB; Transactional ACID (giao dịch ACID); API bất đồng bộ; Indexes (chỉ mục) cho query nhanh
  ├── Use Cases: ✅ Offline-first/PWA, cache API, lưu file/blob; ❌ Key-value đơn giản → dùng localStorage
  ├── API (cấp thấp): indexedDB.open(), objectStore.add/put/get/delete, createIndex, Transactions (giao dịch)
  ├── Wrappers (Khuyến nghị): Dexie.js (phổ biến), localForage (API đơn giản), idb (Google)
  └── Best Practices: Dùng Dexie tránh callback hell; version schema; xử lý quota exceeded (hết dung lượng)
  ```

  **📝 DEXIE.JS EXAMPLE:**

  ```javascript
  const db = new Dexie('MyDatabase');
  db.version(1).stores({
    todos: '++id, text, completed',
  });

  await db.todos.add({ text: 'Learn IndexedDB' });
  const todos = await db.todos.toArray();
  ```

  ---

  ### **6.6 WebSocket (kết nối 2 chiều real-time) & Real-time** ⭐⭐⭐⭐

  ```

  🔌 REAL-TIME COMMUNICATION // Giao tiếp thời gian thực
  ├── WebSocket (giao thức kết nối 2 chiều liên tục qua TCP)
  │ ├── Persistent bidirectional TCP connection // Kết nối TCP 2 chiều liên tục
  │ ├── Protocol: ws:// (unsecure) / wss:// (SSL) // Giao thức ws/wss
  │ ├── Lower latency than polling (~50ms) // Độ trễ thấp hơn polling
  │ └── Use: Trading, Chat, Live notifications // Dùng: Giao dịch, chat, thông báo
  │
  ├── Socket.IO (thư viện WebSocket với fallback)
  │ ├── WebSocket wrapper + fallback to polling // Wrapper WebSocket + dự phòng polling
  │ ├── Auto-reconnect // Tự động kết nối lại
  │ ├── Rooms & Namespaces // Phòng & không gian tên
  │ └── Event-based API: socket.emit() // API dựa trên sự kiện
  │
  ├── Server-Sent Events - SSE (sự kiện từ server, 1 chiều)
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
  └── Service Worker (worker dịch vụ - proxy network, hỗ trợ offline, push notifications) (offline, push notifications) // Worker dịch vụ
  └── 💡 Proxy network requests → offline, push notifications, PWA (Progressive Web App - ứng dụng web tiến bộ)

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
  ├── 🎭 Behavioral (Hành Vi - mẫu điều khiển luồng/tương tác giữa các object)
  │ ├── Observer/PubSub (event handling) // Quan sát / Phát hành–Đăng ký (xử lý sự kiện)
  │ │ └── 💡 Một object (Subject/Publisher) giữ danh sách các listener (Observer/Subscriber). Khi có thay đổi, nó gửi thông báo cho tất cả listener. Dùng cho: Event Bus, React state, DOM events. VD: button click → nhiều component lắng nghe.
  │ ├── Strategy (interchangeable algorithms) // Chiến lược (thuật toán có thể thay thế nhau)
  │ │ └── 💡 Chọn thuật toán lúc runtime (VD: payment methods: credit card, PayPal, Momo — cùng interface, khác implementation)
  │ └── Command (encapsulate actions) // Lệnh (đóng gói hành động thành object)
  │ └── 💡 Đóng gói request thành object → dễ undo/redo, queue, log (VD: mỗi thao tác là một command object)
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

  ### **6.6 Accessibility (a11y - khả năng truy cập cho người khuyết tật)** ⭐⭐⭐⭐

  ```

  ♿ WEB ACCESSIBILITY (Khả Năng Truy Cập Web - a11y)
  ├── 📋 WCAG (Web Content Accessibility Guidelines - hướng dẫn truy cập nội dung web) 2.1 Guidelines (Hướng Dẫn WCAG 2.1)
  │ ├── 👁️ Perceivable (alt text, contrast) // Có Thể Nhận Biết
  │ │ └── 💡 Alt text cho images, contrast ratio ≥ 4.5:1 cho text
  │ ├── 🎮 Operable (keyboard nav, focus) // Có Thể Vận Hành
  │ │ └── 💡 Điều hướng bằng keyboard, focus rõ ràng, không trap focus
  │ ├── 📖 Understandable (clear labels) // Có Thể Hiểu
  │ │ └── 💡 Label rõ ràng, error messages dễ hiểu, ngôn ngữ đơn giản
  │ └── 🛡️ Robust (valid HTML, ARIA) // Mạnh Mẽ
  │ └── 💡 HTML hợp lệ, ARIA đúng cách, tương thích screen reader
  │
  ├── 🏷️ ARIA (Accessible Rich Internet Applications - thuộc tính hỗ trợ truy cập) Attributes (Thuộc Tính ARIA)
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
      │   └── 💡 Kết nối WebSocket → update data real-time (trading, chat...)
      ├── Async transaction updates // Cập Nhật Giao Dịch Bất Đồng Bộ
      │   └── 💡 applyTransactionAsync() → update không block UI
      └── Cell flash on value change // Nhấp Nháy Ô Khi Giá Trị Thay Đổi
          └── 💡 Cell flash màu khi value thay đổi → user thấy thay đổi ngay

  ```

  ---

  ## 🎯 **LEARNING PATH BY EXPERIENCE (Lộ trình học theo kinh nghiệm)**

  ### **🌱 Junior (0-1 năm)**

  ```
  Tuần 1-2: JS Fundamentals (Nền tảng JS - Q01-Q08)
  Tuần 3-4: ES6+ Features (Tính năng ES6+ - Q09-Q10)
  Tuần 5-6: DOM & Events (DOM và sự kiện - Q11-Q12)
  Tuần 7-8: Async/Promises (Bất đồng bộ/Promise - Q13, Q19)
  Tuần 9-10: React Hooks Basic (Hooks cơ bản - Q35)
  Tuần 11-12: CSS Architecture (Kiến trúc CSS - Q59)
  ```

  ### **🚀 Mid-Level (1-3 năm)**

  ```
  Tháng 1: Event Loop sâu (Q06), Closures (Q08)
  Tháng 2: React Query (Q17), Performance (Q38)
  Tháng 3: Next.js (Q26), TypeScript (Q52)
  Tháng 4: Testing (Q50), State Management (Q57)
  ```

  ### **🔥 Senior (3+ năm)**

  ```
  Focus Areas (Trọng tâm):
  ├── System Design (Thiết kế hệ thống - Q49)
  ├── Security (Bảo mật - Q39, Q43)
  ├── CI/CD (Tích hợp & triển khai liên tục - Q53)
  ├── Docker & Containerization (Container hóa - Q63)
  ├── Micro-frontends (Vi frontend - Q44)
  ├── Performance Monitoring (Giám sát hiệu năng - Q51)
  └── Design Patterns (Mẫu thiết kế - Q60)
  ```

  ---

  ### **6.10 Internationalization (i18n - đa ngôn ngữ) & Localization** ⭐⭐⭐⭐

  ```
  🌍 INTERNATIONALIZATION (I18N) - Đa Ngôn Ngữ
  ├── 📚 Libraries (Thư Viện)
  │   ├── react-i18next (most popular) // Phổ biến nhất
  │   │   └── 💡 Wrapper cho i18next, hooks support, namespace, fallback
  │   ├── react-intl (FormatJS) // FormatJS
  │   │   └── 💡 ICU message format, React components, date/number formatting
  │   └── next-intl (Next.js specific) // Dành riêng Next.js
  │       └── 💡 Server Components support, App Router, tích hợp tốt Next.js
  │
  ├── 🎯 Core Concepts (Khái Niệm Cốt Lõi)
  │   ├── Translation files (JSON/YAML) // File dịch
  │   │   └── 💡 en.json: { "welcome": "Welcome" }, vi.json: { "welcome": "Chào mừng" }
  │   ├── Interpolation (dynamic values) // Nội suy (giá trị động)
  │   │   └── 💡 t('hello', { name: 'John' }) → "Hello John" / "Xin chào John"
  │   ├── Pluralization // Số nhiều
  │   │   └── 💡 "1 item" vs "2 items" → Quy tắc khác nhau mỗi ngôn ngữ
  │   └── Namespace organization // Tổ chức namespace
  │       └── 💡 common.json, auth.json, dashboard.json → Tách file cho dễ quản lý
  │
  ├── 🔄 Language Switching (Chuyển Ngôn Ngữ)
  │   ├── URL-based (/en/about, /vi/about) // Dựa trên URL
  │   │   └── 💡 SEO-friendly, sharable links, Next.js i18n routing
  │   ├── Cookie/localStorage // Cookie/lưu trữ cục bộ
  │   │   └── 💡 Remember user preference, persist across sessions
  │   └── Accept-Language header (SSR) // Header Accept-Language
  │       └── 💡 Auto-detect user language từ browser settings
  │
  ├── 📅 Formatting (Định Dạng)
  │   ├── Intl.DateTimeFormat // Định dạng ngày/giờ
  │   │   └── 💡 new Intl.DateTimeFormat('vi-VN').format(date) → "15/01/2024"
  │   ├── Intl.NumberFormat (currency, percent) // Định dạng số
  │   │   └── 💡 new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' })
  │   └── Intl.RelativeTimeFormat // Định dạng thời gian tương đối
  │       └── 💡 "2 days ago", "trong 3 giờ" → Format tự động theo locale
  │
  ├── 🌐 RTL (Right-to-Left - phải sang trái) Support (Hỗ Trợ RTL - Right-to-Left)
  │   ├── dir="rtl" attribute // Thuộc tính dir
  │   │   └── 💡 Arabic, Hebrew → text direction phải sang trái
  │   ├── CSS logical properties // Thuộc tính CSS logic
  │   │   └── 💡 margin-inline-start thay vì margin-left → tự động flip RTL
  │   └── Flip icons & layouts // Lật icon & layout
  │       └── 💡 Arrow icons, navigation phải flip cho RTL
  │
  └── ✅ Best Practices (Thực Hành Tốt)
      ├── Lazy load translations (code split per language) // Tải chậm
      │   └── 💡 Chỉ load ngôn ngữ hiện tại → giảm bundle size
      ├── Separate content from code // Tách nội dung khỏi code
      │   └── 💡 Không hardcode text → dễ dịch, maintain
      ├── Use keys, not text as identifiers // Dùng key, không phải text
      │   └── 💡 t('auth.login') thay vì t('Login') → ngắn gọn, rõ ràng
      └── Test with long translations (German, Finnish) // Test với dịch dài
          └── 💡 German text dài hơn 30% → test layout không vỡ
  ```

  **📝 EXAMPLE:**

  ```typescript
  // react-i18next - Thư viện i18n phổ biến nhất cho React
  import { useTranslation } from 'react-i18next';

  function Component() {
    // t: function dịch text, i18n: object quản lý ngôn ngữ
    const { t, i18n } = useTranslation();

    return (
      <>
        {/* Dịch key 'welcome' và truyền biến name */}
        <h1>{t('welcome', { name: 'John' })}</h1>

        {/* Đổi ngôn ngữ sang tiếng Việt */}
        <button onClick={() => i18n.changeLanguage('vi')}>
          Tiếng Việt
        </button>
      </>
    );
  }

  // Translation files - File dịch theo ngôn ngữ
  // en.json: { "welcome": "Welcome, {{name}}!" }  // {{name}} = placeholder
  // vi.json: { "welcome": "Chào mừng, {{name}}!" }
  ```

  ---

  ### **6.11 Forms & Validation** ⭐⭐⭐⭐⭐

  ```
  📝 FORM MANAGEMENT (Quản Lý Form)
  ├── 📚 Libraries (Thư Viện)
  │   ├── React Hook Form (recommended) // Khuyến nghị
  │   │   ├── Uncontrolled approach → minimal re-renders // Không điều khiển → ít re-render
  │   │   ├── Built-in validation // Validation có sẵn
  │   │   ├── Small bundle (~9KB) // Bundle nhỏ
  │   │   └── 💡 Performance tốt nhất, API đơn giản, DevTools support
  │   │
  │   ├── Formik (popular but heavy) // Phổ biến nhưng nặng
  │   │   ├── Controlled approach → more re-renders // Điều khiển → nhiều re-render hơn
  │   │   ├── ~13KB bundle
  │   │   └── 💡 Dễ học, nhiều examples, nhưng performance kém hơn RHF
  │   │
  │   └── TanStack Form (new, lightweight) // Mới, nhẹ
  │       └── 💡 Framework-agnostic, type-safe, ~5KB
  │
  ├── ✅ Validation Libraries (Thư Viện Validation)
  │   ├── Zod (TypeScript-first) // TypeScript trước tiên
  │   │   ├── Type inference → auto-generate TS types // Suy luận type tự động
  │   │   ├── Runtime validation // Validation runtime
  │   │   └── 💡 const schema = z.object({ email: z.string().email() })
  │   │
  │   ├── Yup (popular with Formik) // Phổ biến với Formik
  │   │   ├── Schema-based validation // Validation dựa trên schema
  │   │   └── 💡 yup.object().shape({ email: yup.string().required() })
  │   │
  │   └── Joi (Node.js origin) // Gốc Node.js
  │       └── 💡 Powerful, nhiều validators, nhưng bundle lớn
  │
  ├── 🎯 Key Concepts (Khái Niệm Chính)
  │   ├── Controlled vs Uncontrolled // Điều khiển vs Không điều khiển
  │   │   ├── Controlled: React controls value (useState) // React điều khiển
  │   │   │   └── 💡 value={state}, onChange={setState} → React quản lý
  │   │   └── Uncontrolled: DOM controls value (ref) // DOM điều khiển
  │   │       └── 💡 ref={inputRef}, không dùng state → ít re-render
  │   │
  │   ├── Field-level vs Form-level validation // Validation theo field vs form
  │   │   ├── Field-level: Validate khi blur/change // Theo field
  │   │   └── Form-level: Validate khi submit // Theo form
  │   │
  │   ├── Async validation (username availability) // Validation bất đồng bộ
  │   │   └── 💡 Check username đã tồn tại chưa → debounce, loading state
  │   │
  │   └── Error handling & display // Xử lý & hiển thị lỗi
  │       └── 💡 Field-level errors, server errors, summary errors
  │
  ├── ⚡ Performance (Hiệu Suất)
  │   ├── Debounce validation // Debounce validation
  │   │   └── 💡 Validate sau 300ms user ngừng gõ → tránh spam
  │   ├── Avoid unnecessary re-renders // Tránh re-render không cần thiết
  │   │   └── 💡 RHF uncontrolled → chỉ re-render khi submit
  │   └── Lazy validation (on blur, not on change) // Validation chậm
  │       └── 💡 Validate khi blur thay vì mỗi keystroke → ít validation hơn
  │
  └── ✅ Accessibility (Khả Năng Truy Cập)
      ├── aria-invalid, aria-describedby // ARIA attributes
      │   └── 💡 <input aria-invalid="true" aria-describedby="email-error">
      ├── Error announcements (aria-live) // Thông báo lỗi
      │   └── 💡 Screen reader announce errors
      ├── Focus management // Quản lý focus
      │   └── 💡 Focus vào field đầu tiên có lỗi khi submit
      └── Required fields indication // Chỉ báo trường bắt buộc
          └── 💡 Visual indicator (*) + aria-required="true"
  ```

  **📝 REACT HOOK FORM EXAMPLE:**

  ```typescript
  import { useForm } from 'react-hook-form'; // Form management - Quản lý form
  import { zodResolver } from '@hookform/resolvers/zod'; // Zod resolver - Tích hợp Zod
  import { z } from 'zod'; // Schema validation - Validation schema

  // 🎯 Define validation schema - Định nghĩa schema validation
  const schema = z.object({
    email: z.string().email('Email không hợp lệ'), // Validate email format
    password: z.string().min(8, 'Mật khẩu ít nhất 8 ký tự'), // Min 8 chars
  });

  // ✅ Auto infer TypeScript type từ schema - Tự động sinh type
  type FormData = z.infer<typeof schema>;

  function LoginForm() {
    // 📝 useForm hook - register: đăng ký field, handleSubmit: xử lý submit, errors: lỗi validation
    const { register, handleSubmit, formState: { errors } } = useForm<FormData>({
      resolver: zodResolver(schema), // Sử dụng Zod để validate
    });

    // ✅ Callback khi form valid - Chỉ chạy khi không có lỗi
    const onSubmit = (data: FormData) => {
      console.log(data); // Data đã validated, type-safe
    };

    return (
      <form onSubmit={handleSubmit(onSubmit)}>
        {/* 🔗 register('email') - Đăng ký field, uncontrolled approach */}
        <input {...register('email')} aria-invalid={!!errors.email} />
        {/* ⚠️ Hiển thị lỗi nếu có - Accessibility với role="alert" */}
        {errors.email && <span role="alert">{errors.email.message}</span>}

        {/* 🔒 Password field */}
        <input {...register('password')} type="password" />
        {errors.password && <span role="alert">{errors.password.message}</span>}

        {/* 🚀 Submit button - trigger validation */}
        <button type="submit">Login</button>
      </form>
    );
  }
  ```

  ---

  ### **6.12 SEO & Meta Tags** ⭐⭐⭐⭐⭐

  ```
  🔍 SEO OPTIMIZATION (Tối Ưu SEO)
  ├── 📄 Meta Tags (Thẻ Meta)
  │   ├── Next.js Metadata API (App Router) // API Metadata Next.js
  │   │   └── 💡 export const metadata = { title: '...', description: '...' }
  │   ├── Open Graph (Facebook/LinkedIn) // Open Graph
  │   │   └── 💡 og:title, og:description, og:image → Preview khi share
  │   ├── Twitter Cards // Thẻ Twitter
  │   │   └── 💡 twitter:card, twitter:title, twitter:image → Preview Twitter
  │   └── Canonical URLs // URL chuẩn
  │       └── 💡 <link rel="canonical" href="..."> → Tránh duplicate content
  │
  ├── 🗂️ Structured Data (JSON-LD) // Dữ Liệu Có Cấu Trúc
  │   ├── Schema.org types // Các loại Schema.org
  │   │   ├── Article, Product, Organization, Person, Recipe...
  │   │   └── 💡 Google Rich Results → Hiển thị đẹp hơn trên search
  │   └── Implementation // Triển khai
  │       └── 💡 <script type="application/ld+json">{JSON.stringify(schema)}</script>
  │
  ├── 🗺️ Sitemap & Robots.txt (Sơ Đồ Trang & Robots)
  │   ├── XML Sitemap generation // Tạo sitemap XML
  │   │   └── 💡 Next.js: app/sitemap.ts → auto-generate sitemap.xml
  │   ├── robots.txt configuration // Cấu hình robots.txt
  │   │   └── 💡 Allow/Disallow paths, Sitemap location
  │   └── Dynamic sitemap (for large sites) // Sitemap động
  │       └── 💡 Generate sitemap on-demand cho 1000+ pages
  │
  ├── ⚡ Performance & SEO (Hiệu Suất & SEO)
  │   ├── Core Web Vitals (LCP, FID, CLS) // Chỉ Số Web Cốt Lõi
  │   │   └── 💡 Google ranking factor → Trang nhanh rank cao hơn
  │   ├── Mobile-first indexing // Lập chỉ mục Mobile trước
  │   │   └── 💡 Google index mobile version → phải responsive
  │   └── Image optimization // Tối ưu hình ảnh
  │       └── 💡 next/image, lazy loading, alt text, WebP format
  │
  ├── 🔗 Link Optimization (Tối Ưu Liên Kết)
  │   ├── Internal linking strategy // Chiến lược liên kết nội bộ
  │   │   └── 💡 Link pages liên quan → giúp crawling, distribute page authority
  │   ├── Descriptive anchor text // Text liên kết mô tả
  │   │   └── 💡 "Learn React hooks" thay vì "Click here"
  │   └── External links (rel="nofollow"/"noopener") // Liên kết ngoài
  │       └── 💡 nofollow: Không pass authority, noopener: Security
  │
  └── ✅ Best Practices (Thực Hành Tốt)
      ├── Server-Side Rendering (SSR/SSG) // Render phía server
      │   └── 💡 Google crawl HTML content → SSR/SSG tốt hơn CSR
      ├── Semantic HTML (h1, nav, article, footer) // HTML Ngữ Nghĩa
      │   └── 💡 Helps search engines understand content structure
      ├── Unique title & description per page // Title & description riêng mỗi trang
      │   └── 💡 Tránh duplicate, mỗi trang có title unique
      └── Monitor with Google Search Console // Giám sát với Search Console
          └── 💡 Track indexing, performance, errors, search queries
  ```

  **📝 NEXT.JS METADATA EXAMPLE:**

  ```typescript
  // app/blog/[slug]/page.tsx - Dynamic route cho blog post
  // 🎯 generateMetadata - Next.js 13+ App Router API tự động generate meta tags
  export async function generateMetadata({ params }): Promise<Metadata> {
    // 📡 Fetch dữ liệu post từ API/Database
    const post = await getPost(params.slug);

    return {
      // 🔍 SEO: Title tag cho Google Search
      title: post.title,
      description: post.excerpt,

      // 📱 Open Graph: Meta tags cho Facebook, LinkedIn khi share link
      openGraph: {
        title: post.title,
        description: post.excerpt,
        images: [{ url: post.coverImage }], // Preview image khi share
      },

      // 🐦 Twitter Cards: Meta tags cho Twitter preview
      twitter: {
        card: 'summary_large_image', // Large image card
        title: post.title,
        description: post.excerpt,
        images: [post.coverImage],
      },
    };
  }

  // 📊 JSON-LD Structured Data - Giúp Google hiểu nội dung trang
  // ✅ Result: Google Rich Results (hiển thị đẹp hơn trên search)
  const structuredData = {
    '@context': 'https://schema.org', // Schema.org vocabulary
    '@type': 'Article', // Loại: Article, Product, Person, Recipe...
    headline: post.title,
    image: post.coverImage,
    datePublished: post.publishedAt, // Ngày publish
    author: { '@type': 'Person', name: post.author.name }, // Tác giả
  };
  ```

  ---

  ### **6.13 Animation & Micro-interactions** ⭐⭐⭐⭐

  ```
  🎬 ANIMATION LIBRARIES (Thư Viện Animation)
  ├── 💫 Framer Motion (recommended) // Khuyến nghị
  │   ├── React-specific, declarative API // Chuyên React, API khai báo
  │   ├── Layout animations (auto-animate on layout change) // Animation layout
  │   │   └── 💡 <motion.div layout> → tự động animate khi layout thay đổi
  │   ├── Gestures (drag, pan, hover) // Cử chỉ
  │   │   └── 💡 drag, whileHover, whileTap → interactive animations
  │   ├── Variants (reusable animation states) // Biến thể
  │   │   └── 💡 Define animation states, orchestrate children
  │   └── Exit animations (AnimatePresence) // Animation thoát
  │       └── 💡 Animate elements khi unmount → smooth transitions
  │
  ├── 🌊 React Spring (physics-based) // Dựa trên vật lý
  │   ├── Natural, physics-based animations // Animation tự nhiên
  │   │   └── 💡 Spring physics → more realistic than keyframes
  │   ├── Hooks API (useSpring, useTrail) // API Hooks
  │   │   └── 💡 const props = useSpring({ opacity: 1, from: { opacity: 0 } })
  │   └── Interpolation (transform values) // Nội suy
  │       └── 💡 Animate numbers, colors, transforms smoothly
  │
  ├── ⚡ GSAP (GreenSock) // GreenSock
  │   ├── Most powerful, industry-standard // Mạnh nhất, tiêu chuẩn công nghiệp
  │   ├── Complex timeline animations // Animation timeline phức tạp
  │   │   └── 💡 gsap.timeline().to(el, {}).to(el2, {}) → sequence animations
  │   ├── ScrollTrigger (scroll-based) // Trigger cuộn
  │   │   └── 💡 Animate on scroll position → parallax, reveals
  │   └── Browser compatibility (IE11+) // Tương thích browser
  │       └── 💡 Works everywhere, even old browsers
  │
  ├── 🎨 CSS Animations (Native) // Animation CSS (Gốc)
  │   ├── @keyframes + animation property // Keyframes + thuộc tính animation
  │   │   └── 💡 Lightweight, no JS needed, GPU-accelerated
  │   ├── transition property // Thuộc tính transition
  │   │   └── 💡 transition: opacity 0.3s ease → simple animations
  │   └── Performance (use transform & opacity only) // Hiệu suất
  │       └── 💡 transform, opacity → không trigger layout/paint → 60fps
  │
  ├── 🎭 Micro-interactions (Tương Tác Nhỏ)
  │   ├── Button hover effects // Hiệu ứng hover nút
  │   │   └── 💡 Scale, color change, shadow → feedback
  │   ├── Loading states // Trạng thái loading
  │   │   └── 💡 Skeleton screens, spinners, progress bars
  │   ├── Form field feedback // Phản hồi trường form
  │   │   └── 💡 Shake on error, checkmark on success
  │   └── Toast notifications // Thông báo toast
  │       └── 💡 Slide in/out, auto-dismiss → non-intrusive
  │
  └── ✅ Performance Best Practices (Thực Hành Tốt Hiệu Suất)
      ├── Use will-change sparingly // Dùng will-change tiết kiệm
      │   └── 💡 will-change: transform → hint browser, but memory cost
      ├── Prefer transform over position/width // Ưu tiên transform
      │   └── 💡 transform: translateX() thay vì left → không trigger layout
      ├── RequestAnimationFrame for JS animations // RequestAnimationFrame
      │   └── 💡 Sync với browser refresh rate → 60fps smooth
      └── Reduced motion (prefers-reduced-motion) // Chuyển động giảm
          └── 💡 Respect user preference → disable animations nếu cần
  ```

  **📝 FRAMER MOTION EXAMPLE:**

  ```typescript
  import { motion, AnimatePresence } from 'framer-motion';

  function Component() {
    const [isVisible, setIsVisible] = useState(true);

    return (
      // 🎬 AnimatePresence: Cho phép animate khi component unmount
      <AnimatePresence>
        {isVisible && (
          <motion.div
            // 🎯 initial: State ban đầu (opacity 0, y -20px)
            initial={{ opacity: 0, y: -20 }}
            // ✨ animate: State sau khi mount (fade in + slide down)
            animate={{ opacity: 1, y: 0 }}
            // 🚪 exit: State khi unmount (fade out + slide down)
            exit={{ opacity: 0, y: 20 }}
            // ⏱️ transition: Thời gian animation (0.3s)
            transition={{ duration: 0.3 }}
            // 🖱️ whileHover: Scale 1.05 khi hover (phóng to 5%)
            whileHover={{ scale: 1.05 }}
            // 🤏 drag: Cho phép kéo element (draggable)
            drag
          >
            Content
          </motion.div>
        )}
      </AnimatePresence>
    );
  }
  // 💡 Tips: Framer Motion tự động tạo smooth animations, không cần CSS
  ```

  ---

  ### **6.14 Advanced React Patterns** ⭐⭐⭐⭐⭐

  ```
  ⚛️ REACT 19 & CONCURRENT FEATURES (React 19 & Tính Năng Concurrent)
  ├── 🆕 React 19 New Features (Tính Năng Mới React 19)
  │   ├── use() hook (read promises/context) // Hook use
  │   │   └── 💡 const data = use(promise) → Suspend until resolved
  │   ├── useActionState (form actions) // Hook useActionState
  │   │   └── 💡 Handle form submissions với pending/error states
  │   ├── useFormStatus (form status) // Hook useFormStatus
  │   │   └── 💡 const { pending } = useFormStatus() → Biết form đang submit
  │   ├── useOptimistic (optimistic updates) // Hook useOptimistic
  │   │   └── 💡 Update UI trước, rollback nếu lỗi → Better UX
  │   └── Server Components improvements // Cải tiến Server Components
  │       └── 💡 Async components, better streaming, nested suspense
  │
  ├── 🔄 React Server Components (RSC) Deep Dive
  │   ├── 'use client' boundary // Ranh giới 'use client'
  │   │   └── 💡 Mark components cần interactivity → hydrate chỉ những cái này
  │   ├── Data fetching in Server Components // Lấy dữ liệu trong Server Components
  │   │   └── 💡 async function Component() { const data = await fetch() }
  │   ├── Cannot use hooks (useState, useEffect) // Không dùng được hooks
  │   │   └── 💡 Server Components: No state, no effects → chỉ render HTML
  │   └── Pass Server Components as props to Client // Truyền làm props
  │       └── 💡 <ClientComponent children={<ServerComponent />} /> → Composition
  │
  ├── ⏸️ Suspense & Streaming (Suspense & Streaming)
  │   ├── <Suspense fallback={<Loading />}> // Suspense với fallback
  │   │   └── 💡 Show fallback khi component đang fetch data
  │   ├── Nested Suspense boundaries // Suspense lồng nhau
  │   │   └── 💡 Multiple Suspense → stream từng phần, không đợi tất cả
  │   ├── Error boundaries with Suspense // Error boundaries với Suspense
  │   │   └── 💡 Catch errors từ async components
  │   └── Streaming SSR // Streaming SSR
  │       └── 💡 Send HTML từng phần → TTFB nhanh hơn, không đợi toàn bộ page
  │
  ├── 🚀 Concurrent Rendering Features (Tính Năng Render Concurrent)
  │   ├── useTransition // Hook useTransition
  │   │   └── 💡 const [isPending, startTransition] = useTransition()
  │   │   └── 💡 Mark non-urgent updates → UI responsive hơn
  │   ├── useDeferredValue // Hook useDeferredValue
  │   │   └── 💡 const deferredValue = useDeferredValue(value)
  │   │   └── 💡 Defer updates của value → prioritize urgent updates
  │   └── <Suspense> + startTransition // Suspense + startTransition
  │       └── 💡 Show stale content khi fetch new → không flash loading
  │
  ├── 🛡️ Error Boundaries Best Practices (Thực Hành Tốt Error Boundaries)
  │   ├── Wrap feature boundaries // Bọc ranh giới tính năng
  │   │   └── 💡 <ErrorBoundary fallback={<Error />}><Feature /></ErrorBoundary>
  │   ├── Reset error state // Reset trạng thái lỗi
  │   │   └── 💡 Provide "Retry" button → reset error boundary
  │   ├── Log errors to monitoring service // Log lỗi
  │   │   └── 💡 componentDidCatch() → send to Sentry/DataDog
  │   └── Nested error boundaries // Error boundaries lồng nhau
  │       └── 💡 Granular error handling → chỉ crash phần bị lỗi
  │
  └── 📊 State Machines (XState) // Máy Trạng Thái
      ├── Finite State Machine (FSM) // Máy Trạng Thái Hữu Hạn
      │   └── 💡 Define all states, transitions → predictable behavior
      ├── XState library // Thư viện XState
      │   └── 💡 createMachine(), useMachine() → type-safe state management
      ├── Visualize state machine // Visualize máy trạng thái
      │   └── 💡 XState Visualizer → see all states, transitions
      └── Use cases // Trường hợp sử dụng
          └── 💡 Form wizards, authentication flows, complex UI states
  ```

  **📝 REACT 19 EXAMPLE:**

  ```typescript
  // 🖥️ Server Component (async) - Chạy trên server, không ship JS cho client
  async function BlogPost({ id }: { id: string }) {
    // ✅ Có thể await trực tiếp trong component - Không cần useEffect
    const post = await fetchPost(id);
    return <article>{post.content}</article>;
  }
  // 💡 Benefits: Giảm bundle size, SEO tốt, fetch data nhanh

  // 💻 Client Component với useOptimistic - Optimistic UI updates
  'use client' // ⚠️ Directive: Mark component chạy trên client
  function LikeButton({ postId, initialLikes }) {
    // 🚀 useOptimistic: Hook mới React 19 - Update UI ngay, không đợi API
    const [optimisticLikes, setOptimisticLikes] = useOptimistic(
      initialLikes, // State ban đầu
      (current, amount) => current + amount // Updater function
    );

    async function handleLike() {
      setOptimisticLikes(1); // ⚡ UI update ngay lập tức → Better UX
      await likePost(postId); // 📡 API call sau → nếu fail thì rollback
    }

    return <button onClick={handleLike}>❤️ {optimisticLikes}</button>;
  }
  // 💡 Use case: Like buttons, cart updates, any instant feedback

  // ⏸️ useTransition - Phân biệt urgent và non-urgent updates
  function SearchResults() {
    const [isPending, startTransition] = useTransition();
    const [query, setQuery] = useState('');

    function handleSearch(value: string) {
      setQuery(value); // ✅ URGENT: Update input field ngay (typing responsive)
      startTransition(() => {
        // ⏳ NON-URGENT: Fetch results có thể defer → UI không bị block
        fetchResults(value);
      });
    }

    return (
      <>
        {/* Input luôn responsive dù fetch results chậm */}
        <input value={query} onChange={(e) => handleSearch(e.target.value)} />
        {/* 🔄 Show loading indicator khi transition pending */}
        {isPending && <Spinner />}
        <Results />
      </>
    );
  }
  // 💡 Kết quả: User typing mượt mà, không bị giật khi fetch data
  ```

  ---

  ### **6.15 Web Workers & Service Workers** ⭐⭐⭐⭐

  ```
  👷 WEB WORKERS (Workers Web)
  ├── 🧵 Dedicated Workers (Workers Chuyên Dụng)
  │   ├── Run JavaScript in background thread // Chạy JS trong thread nền
  │   │   └── 💡 Không block main thread → UI vẫn responsive
  │   ├── Use cases (Trường Hợp Sử Dụng)
  │   │   ├── Heavy calculations (hashing, encryption) // Tính toán nặng
  │   │   ├── Data processing (parsing large JSON/CSV) // Xử lý dữ liệu
  │   │   └── Image manipulation (Canvas operations) // Xử lý ảnh
  │   └── Communication via postMessage // Giao tiếp qua postMessage
  │       └── 💡 worker.postMessage(data); worker.onmessage = (e) => {...}
  │
  ├── 📦 Transferable Objects (Đối Tượng Có Thể Chuyển Giao)
  │   └── 💡 Transfer ArrayBuffer thay vì copy → zero-copy performance
  │   └── 💡 postMessage(arrayBuffer, [arrayBuffer]) → transfer ownership
  │
  ├── 🔄 Shared Workers (Workers Chia Sẻ)
  │   └── 💡 Shared across multiple tabs/windows → sync state cross-tab
  │
  ├── 🎨 OffscreenCanvas (Canvas Ngoài Màn Hình)
  │   └── 💡 Canvas rendering in Worker → không block main thread
  │
  ├── 🔧 Comlink Library (Thư Viện Comlink)
  │   └── 💡 RPC abstraction cho Workers → gọi functions như local
  │   └── 💡 import * as Comlink from 'comlink'
  │
  └── ⚠️ Limitations (Hạn Chế)
      ├── No DOM access // Không truy cập DOM
      ├── No window object // Không có đối tượng window
      └── Cannot import ES modules directly (need importScripts) // Không import ESM

  🌐 SERVICE WORKERS (Workers Dịch Vụ)
  ├── 📡 Offline-First (Offline Trước)
  │   ├── Cache API // API Cache
  │   │   └── 💡 caches.open('v1').then(cache => cache.add('/index.html'))
  │   ├── Strategies (Chiến Lược)
  │   │   ├── Cache First → nhanh, offline-ready // Cache trước
  │   │   ├── Network First → fresh data, fallback cache // Network trước
  │   │   ├── Stale-While-Revalidate → cache ngay, fetch sau // Cũ khi revalidate
  │   │   └── Cache Only, Network Only // Chỉ cache, chỉ network
  │   └── Workbox // Thư viện Workbox
  │       └── 💡 Google library → simplify Service Worker development
  │
  ├── 🔔 Push Notifications (Thông Báo Đẩy)
  │   └── 💡 Background notifications → work khi app đóng
  │   └── 💡 Push API + Notification API
  │
  ├── 🔄 Background Sync (Đồng Bộ Nền)
  │   └── 💡 Retry failed requests khi online trở lại
  │   └── 💡 registration.sync.register('sync-tag')
  │
  ├── 📱 Progressive Web Apps (PWA)
  │   ├── manifest.json (app metadata) // Metadata ứng dụng
  │   ├── Add to Home Screen // Thêm vào màn hình chính
  │   ├── Offline functionality // Chức năng offline
  │   └── App-like experience // Trải nghiệm giống app
  │
  └── ✅ Best Practices (Thực Hành Tốt)
      ├── Version your caches // Đánh phiên bản cache
      │   └── 💡 const CACHE_NAME = 'v1' → xóa cache cũ khi update
      ├── Clean up old caches // Dọn cache cũ
      │   └── 💡 self.addEventListener('activate', event => {...})
      └── Test offline behavior // Test hành vi offline
          └── 💡 Chrome DevTools → Application → Service Workers → Offline
  ```

  **📝 WEB WORKER EXAMPLE:**

  ```typescript
  // main.ts - Main thread (UI thread)
  // 👷 Tạo Web Worker - Chạy JavaScript trong background thread
  const worker = new Worker('/worker.js');

  // 📤 Gửi message đến Worker - postMessage API
  worker.postMessage({ type: 'hash', data: largeData });

  // 📥 Nhận kết quả từ Worker - onmessage handler
  worker.onmessage = (event) => {
    console.log('Result:', event.data); // ✅ Main thread không bị block
  };

  // worker.js - Worker thread (background)
  // 🔧 Worker nhận message từ main thread
  self.onmessage = (event) => {
    if (event.data.type === 'hash') {
      // 🏋️ Heavy computation - Chạy ở background, không lag UI
      const result = expensiveHashFunction(event.data.data);
      // 📤 Gửi kết quả về main thread
      self.postMessage(result);
    }
  };
  // 💡 Use case: Hashing, encryption, parsing large JSON/CSV

  // 🚀 Với Comlink (RPC-style) - Gọi Worker functions như local functions
  import * as Comlink from 'comlink';

  const worker = new Worker('/worker.js');
  // 🎁 Wrap worker thành API object
  const api = Comlink.wrap(worker);

  // ✨ Gọi như async function thường - Không cần postMessage!
  const result = await api.heavyComputation(data);
  // 💡 Comlink tự động handle serialization, promises, callbacks
  ```

  ---

  ### **6.16 Module Federation & Micro-Frontends** ⭐⭐⭐⭐

  ```
  🏗️ MODULE FEDERATION (Liên Kết Module)
  ├── 🎯 Core Concepts (Khái Niệm Cốt Lõi)
  │   ├── Host App (Ứng Dụng Chủ)
  │   │   └── 💡 Ứng dụng chính, consume remote modules
  │   ├── Remote App (Ứng Dụng Từ Xa)
  │   │   └── 💡 Expose modules cho host → có thể deploy độc lập
  │   ├── Shared Dependencies (Phụ Thuộc Chia Sẻ)
  │   │   └── 💡 React, React-DOM shared → chỉ load 1 lần
  │   └── Runtime Loading (Tải Runtime)
  │       └── 💡 Load remote modules at runtime → không cần rebuild host
  │
  ├── 🔧 Webpack Module Federation (Webpack)
  │   └── 💡 Built into Webpack 5, plugin configuration
  │   └── 💡 ModuleFederationPlugin({ name, filename, exposes, remotes, shared })
  │
  ├── ⚡ Vite Module Federation (@originjs/vite-plugin-federation)
  │   └── 💡 Vite port of Webpack Module Federation
  │
  ├── 📦 Nx Module Federation (Nx Framework)
  │   └── 💡 nx g @nx/react:host → scaffold Module Federation setup
  │
  ├── 🎨 Use Cases (Trường Hợp Sử Dụng)
  │   ├── Micro-frontends → teams deploy độc lập // Micro-frontends
  │   ├── Shared component library → centralized components // Thư viện component chia sẻ
  │   └── A/B testing → load different versions dynamically // A/B testing
  │
  └── ⚠️ Challenges (Thách Thức)
      ├── Version conflicts (shared deps) // Xung đột phiên bản
      │   └── 💡 singleton: true → enforce 1 version only
      ├── Type safety (TypeScript) // An toàn kiểu
      │   └── 💡 Generate types for exposed modules
      ├── Error handling (remote fails to load) // Xử lý lỗi
      │   └── 💡 Error boundaries, fallback UI
      └── Testing (integration testing) // Testing
          └── 💡 Test host + remote together → E2E tests

  🌐 MICRO-FRONTEND ARCHITECTURES (Kiến Trúc Micro-Frontend)
  ├── 🏛️ Patterns (Mẫu)
  │   ├── Monorepo (Nx, Turborepo) // Monorepo
  │   │   └── 💡 Single repo, multiple apps → shared code, atomic commits
  │   ├── Multi-repo (Separate repos per team) // Đa repo
  │   │   └── 💡 Independent repos → team autonomy, versioning
  │   └── Hybrid (Monorepo for shared, multi-repo for apps) // Kết hợp
  │       └── 💡 Balance between sharing and autonomy
  │
  ├── 🔗 Integration Strategies (Chiến Lược Tích Hợp)
  │   ├── Build-time integration (npm packages) // Tích hợp build-time
  │   │   └── 💡 Publish components as packages → import like normal
  │   ├── Runtime integration (Module Federation) // Tích hợp runtime
  │   │   └── 💡 Load remotes at runtime → deploy độc lập
  │   └── iFrame-based (legacy) // Dựa trên iFrame (cũ)
  │       └── 💡 Simple, isolated, nhưng performance/UX kém
  │
  ├── 🎯 Routing (Định Tuyến)
  │   ├── Shell routing (host owns routes) // Định tuyến shell
  │   │   └── 💡 Host router: /app1/* → load remote 1
  │   └── Distributed routing (each app owns routes) // Định tuyến phân tán
  │       └── 💡 Each micro-frontend manages own routes
  │
  └── ✅ Best Practices (Thực Hành Tốt)
      ├── Clear ownership boundaries // Ranh giới sở hữu rõ ràng
      │   └── 💡 Each team owns specific features/routes
      ├── Shared design system // Hệ thống thiết kế chia sẻ
      │   └── 💡 Component library cho consistent UI
      ├── API contracts (BFF per micro-frontend) // Hợp đồng API
      │   └── 💡 Backend For Frontend → mỗi MFE có BFF riêng
      └── Independent deployments // Triển khai độc lập
          └── 💡 Deploy micro-frontends riêng lẻ → không ảnh hưởng lẫn nhau
  ```

  ---

  ### **6.17 Advanced Build Optimization** ⭐⭐⭐⭐⭐

  ```
  📦 CODE SPLITTING STRATEGIES (Chiến Lược Tách Code)
  ├── 🎯 Types of Code Splitting (Các Loại Tách Code)
  │   ├── Route-based splitting // Tách theo route
  │   │   └── 💡 React.lazy(() => import('./Page')) → mỗi route 1 bundle
  │   ├── Component-based splitting // Tách theo component
  │   │   └── 💡 Lazy load heavy components (charts, editors)
  │   └── Vendor splitting // Tách vendor
  │       └── 💡 node_modules riêng bundle → cache lâu hơn
  │
  ├── 📊 Bundle Analysis (Phân Tích Bundle)
  │   ├── webpack-bundle-analyzer // Webpack
  │   │   └── 💡 Visualize bundle size → identify bloat
  │   ├── @next/bundle-analyzer (Next.js) // Next.js
  │   │   └── 💡 ANALYZE=true next build → generate report
  │   └── rollup-plugin-visualizer (Vite) // Vite
  │       └── 💡 stats.html → interactive treemap
  │
  ├── 🌲 Tree Shaking (Lắc Cây)
  │   ├── ES Modules only (not CommonJS) // Chỉ ES Modules
  │   │   └── 💡 import/export → static analysis → remove dead code
  │   ├── sideEffects flag (package.json) // Flag sideEffects
  │   │   └── 💡 "sideEffects": false → safe to tree-shake
  │   └── Named imports (not default) // Import có tên
  │       └── 💡 import { Button } from 'lib' thay vì import Lib
  │
  ├── 🖼️ Image Optimization (Tối Ưu Hình Ảnh)
  │   ├── Next.js Image component // Component Image của Next.js
  │   │   └── 💡 <Image /> → auto lazy load, srcset, WebP/AVIF
  │   ├── Responsive images (srcset) // Hình ảnh responsive
  │   │   └── 💡 <img srcset="small.jpg 480w, large.jpg 1080w">
  │   ├── Lazy loading (loading="lazy") // Tải chậm
  │   │   └── 💡 Native browser lazy load → no JS needed
  │   └── Image CDN (Cloudinary, Imgix) // CDN hình ảnh
  │       └── 💡 On-the-fly resizing, optimization, caching
  │
  ├── 🎨 Critical CSS Extraction (Trích Xuất CSS Quan Trọng)
  │   └── 💡 Extract above-the-fold CSS → inline in <head> → fast FCP
  │   └── 💡 Tools: critters (Next.js built-in), critical package
  │
  └── ✅ Performance Budgets (Ngân Sách Hiệu Suất)
      ├── Set bundle size limits // Đặt giới hạn kích thước bundle
      │   └── 💡 Webpack: performance.maxAssetSize, maxEntrypointSize
      ├── CI/CD enforcement // Thực thi CI/CD
      │   └── 💡 Fail build nếu bundle quá lớn → prevent regressions
      └── Per-route budgets // Ngân sách theo route
          └── 💡 /home: 200KB, /dashboard: 500KB → granular control
  ```

  **📝 CODE SPLITTING EXAMPLE:**

  ```typescript
  // 🗺️ Route-based splitting (React Router) - Tách code theo route
  import { lazy, Suspense } from 'react';

  // 📦 lazy() - Dynamic import, chỉ load khi user vào route
  const Dashboard = lazy(() => import('./Dashboard')); // Bundle riêng
  const Profile = lazy(() => import('./Profile'));     // Bundle riêng

  function App() {
    return (
      // ⏸️ Suspense: Hiển thị fallback khi lazy component đang load
      <Suspense fallback={<Loading />}>
        <Routes>
          {/* ✅ Route /dashboard chỉ load Dashboard.js khi cần */}
          <Route path="/dashboard" element={<Dashboard />} />
          {/* ✅ Route /profile chỉ load Profile.js khi cần */}
          <Route path="/profile" element={<Profile />} />
        </Routes>
      </Suspense>
    );
  }
  // 💡 Kết quả: Initial bundle nhỏ hơn, load nhanh hơn

  // 🧩 Component-based splitting - Tách component nặng
  const HeavyChart = lazy(() => import('./HeavyChart')); // Chart library lớn

  function Analytics() {
    const [showChart, setShowChart] = useState(false);

    return (
      <div>
        {/* 👆 User click button mới load chart */}
        <button onClick={() => setShowChart(true)}>Show Chart</button>
        {showChart && (
          // ⏸️ Suspense: Show spinner khi đang load chart
          <Suspense fallback={<Spinner />}>
            <HeavyChart /> {/* ⚡ Lazy load on demand */}
          </Suspense>
        )}
      </div>
    );
  }
  // 💡 Use case: Charts, editors, modals - Components nặng không cần ngay
  ```

  ---

  ### **6.18 Edge Computing & CDN Strategies** ⭐⭐⭐⭐

  ```
  ⚡ EDGE COMPUTING (Tính Toán Biên)
  ├── 🌍 Edge Functions (Hàm Biên)
  │   ├── Vercel Edge Functions // Vercel
  │   │   └── 💡 Run code closer to users → low latency
  │   │   └── 💡 Edge Runtime (subset of Node.js) → lightweight
  │   ├── Cloudflare Workers // Cloudflare
  │   │   └── 💡 V8 isolates → faster cold starts than containers
  │   │   └── 💡 KV storage, Durable Objects → stateful edge
  │   ├── AWS Lambda@Edge // AWS
  │   │   └── 💡 Run at CloudFront edge locations
  │   └── Netlify Edge Functions // Netlify
  │       └── 💡 Deno runtime, TypeScript first-class support
  │
  ├── 🎯 Use Cases (Trường Hợp Sử Dụng)
  │   ├── Geolocation-based content // Nội dung dựa trên vị trí
  │   │   └── 💡 Show different content per country
  │   ├── A/B testing // A/B testing
  │   │   └── 💡 Route users to variants at edge → no client-side flash
  │   ├── Authentication // Xác thực
  │   │   └── 💡 Verify JWT at edge → protect origin server
  │   ├── Dynamic image resizing // Resize ảnh động
  │   │   └── 💡 Resize on-the-fly per device → save bandwidth
  │   └── Bot detection // Phát hiện bot
  │       └── 💡 Block malicious traffic at edge → protect origin
  │
  ├── 📊 CDN (Content Delivery Network - mạng phân phối nội dung) Strategies (Chiến Lược CDN)
  │   ├── Static asset caching // Cache tài sản tĩnh
  │   │   └── 💡 JS, CSS, images → cache-control: max-age=31536000
  │   ├── HTML caching (stale-while-revalidate) // Cache HTML
  │   │   └── 💡 Serve stale content, revalidate in background
  │   ├── Cache purging // Xóa cache
  │   │   └── 💡 Purge specific URLs khi deploy → immediate updates
  │   └── Cache warming // Làm nóng cache
  │       └── 💡 Pre-populate CDN cache → first user sees fast load
  │
  └── ⚠️ Limitations (Hạn Chế)
      ├── Cold start latency (AWS Lambda@Edge) // Độ trễ khởi động lạnh
      ├── Limited runtime APIs // API runtime hạn chế
      │   └── 💡 No Node.js APIs (fs, child_process) → only Web APIs
      └── Execution time limits (Cloudflare: 50ms CPU time) // Giới hạn thời gian thực thi
          └── 💡 Keep functions fast → offload heavy work to origin
  ```

  **📝 EDGE FUNCTION EXAMPLE:**

  ```typescript
  // ⚡ Vercel Edge Function (middleware.ts) - Chạy trên Edge, gần user
  import { NextResponse } from 'next/server';
  import type { NextRequest } from 'next/server';

  // 🌍 Edge Middleware: Chạy trước khi request đến server
  export function middleware(request: NextRequest) {
    // 📍 Get user country từ geo IP - request.geo API
    const country = request.geo?.country || 'US';

    // ✅ Geolocation-based routing - Hiển thị content khác theo quốc gia
    if (country === 'VN') {
      // 🔄 rewrite: Hiển thị /vi nhưng URL không đổi (transparent)
      return NextResponse.rewrite(new URL('/vi', request.url));
    }

    // 🧪 A/B testing - Chia user vào variant A hoặc B
    const bucket = Math.random() < 0.5 ? 'A' : 'B'; // 50/50 split
    const response = NextResponse.next(); // Tiếp tục request
    // 🍪 Set cookie để track variant - persist across pages
    response.cookies.set('ab-test', bucket);

    return response;
  }

  // 🎯 Config: Chỉ chạy middleware cho homepage
  export const config = {
    matcher: '/', // Có thể dùng pattern: '/api/*', '/dashboard/:path*'
  };
  // 💡 Benefits: Low latency (chạy gần user), không cần server roundtrip
  ```

  ---

  ### **6.19 Monitoring & Observability** ⭐⭐⭐⭐⭐

  ```
  📊 ERROR TRACKING (Theo Dõi Lỗi)
  ├── 🔴 Sentry (Industry Standard) // Tiêu chuẩn công nghiệp
  │   ├── Error capture (automatic + manual) // Bắt lỗi tự động + thủ công
  │   │   └── 💡 Sentry.captureException(error) → send to dashboard
  │   ├── Source maps (debug minified code) // Source maps
  │   │   └── 💡 Upload source maps → see original code in stack traces
  │   ├── Breadcrumbs (user actions before error) // Breadcrumbs
  │   │   └── 💡 Track user journey → reproduce errors
  │   └── Release tracking // Theo dõi phát hành
  │       └── 💡 Tag errors by release version → identify bad releases
  │
  ├── 📈 DataDog (Full Stack Monitoring) // Giám sát Full Stack
  │   ├── RUM (Real User Monitoring) // Giám sát người dùng thực
  │   │   └── 💡 Track real user performance → identify slow pages
  │   ├── APM (Application Performance Monitoring) // Giám sát hiệu suất ứng dụng
  │   │   └── 💡 Trace requests from frontend → backend → database
  │   └── Logs & Metrics // Logs & Metrics
  │       └── 💡 Centralized logging → search/analyze all logs
  │
  ├── 🎬 LogRocket (Session Replay) // Session Replay
  │   └── 💡 Record user sessions → watch video replay of bugs
  │   └── 💡 See console logs, network requests, Redux state
  │
  └── ✅ Best Practices (Thực Hành Tốt)
      ├── Error boundaries // Error boundaries
      │   └── 💡 componentDidCatch() → catch React errors, log to Sentry
      ├── Global error handlers // Xử lý lỗi toàn cục
      │   └── 💡 window.onerror, window.onunhandledrejection → catch all errors
      ├── Structured logging // Logging có cấu trúc
      │   └── 💡 JSON logs với context → easy to search/analyze
      └── PII filtering // Lọc PII (Personally Identifiable Information)
          └── 💡 Remove passwords, credit cards from error logs → privacy

  🚀 PERFORMANCE MONITORING (Giám Sát Hiệu Suất)
  ├── 📊 Core Web Vitals Tracking (Theo Dõi Core Web Vitals)
  │   ├── LCP, FID, CLS, TTFB // Các chỉ số cốt lõi
  │   │   └── 💡 Track in production → identify slow pages
  │   ├── web-vitals library // Thư viện web-vitals
  │   │   └── 💡 import { getCLS, getFID, getLCP } from 'web-vitals'
  │   └── Send to analytics // Gửi đến analytics
  │       └── 💡 Report vitals → Google Analytics, DataDog, custom backend
  │
  ├── 🔍 RUM vs Synthetic Monitoring (RUM vs Giám Sát Tổng Hợp)
  │   ├── RUM (Real User Monitoring) // Giám sát người dùng thực
  │   │   └── 💡 Measure real user performance → reflects actual experience
  │   └── Synthetic (Lighthouse CI, Playwright) // Tổng hợp
  │       └── 💡 Automated tests from fixed location → consistent baseline
  │
  ├── 📈 Distributed Tracing (Tracing Phân Tán)
  │   └── 💡 Trace request từ frontend → backend services → database
  │   └── 💡 OpenTelemetry, Jaeger, Zipkin → visualize request flow
  │
  └── 📝 Logging Strategies (Chiến Lược Logging)
      ├── Log levels (error, warn, info, debug) // Các cấp độ log
      │   └── 💡 Production: error/warn only → reduce noise
      ├── Structured logging (JSON) // Logging có cấu trúc
      │   └── 💡 { level: 'error', message: '...', userId: '...', timestamp: ... }
      └── Correlation IDs // ID tương quan
          └── 💡 Track request across services → trace distributed transactions
  ```

  **📝 MONITORING EXAMPLE:**

  ```typescript
  // 🔴 Sentry setup - Error tracking & monitoring
  import * as Sentry from '@sentry/react';

  Sentry.init({
    dsn: 'your-dsn', // 🔑 DSN key từ Sentry dashboard
    environment: process.env.NODE_ENV, // 🌍 dev/staging/production
    tracesSampleRate: 0.1, // 📊 Track 10% of transactions (giảm cost)
    beforeSend(event) {
      // 🔒 Filter PII (Personally Identifiable Information) - Privacy
      if (event.request?.headers?.authorization) {
        delete event.request.headers.authorization; // ⚠️ Xóa token
      }
      return event;
    },
  });

  // 🛡️ Error boundary với Sentry - Catch React errors
  class ErrorBoundary extends React.Component {
    componentDidCatch(error, errorInfo) {
      // 📤 Send error to Sentry dashboard với React context
      Sentry.captureException(error, { contexts: { react: errorInfo } });
    }
  }
  // 💡 Sentry shows: Stack trace, breadcrumbs, user info, release version

  // 📊 Track Core Web Vitals - Performance monitoring
  import { getCLS, getFID, getLCP } from 'web-vitals';

  function sendToAnalytics(metric) {
    // 📈 Send to DataDog, Google Analytics, custom backend
    fetch('/analytics', {
      method: 'POST',
      body: JSON.stringify(metric), // 📦 Metric: name, value, delta, id
    });
  }

  // 🎯 Track từng chỉ số - Tự động gọi khi user interact
  getCLS(sendToAnalytics); // ⚡ Cumulative Layout Shift - Đo độ ổn định layout
  getFID(sendToAnalytics); // ⏱️ First Input Delay - Đo thời gian phản hồi tương tác đầu
  getLCP(sendToAnalytics); // 🖼️ Largest Contentful Paint - Đo tốc độ load content chính
  // 💡 Google dùng Core Web Vitals làm ranking factor cho SEO
  ```

  ---

  ## 🤖 **6.20 AI & AUTOMATIC (OpenClaw, n8n)** ⭐⭐⭐⭐

  ```
  🤖 AI & AUTOMATION (AI & Tự động hóa)
  ├── 🦀 OpenClaw (Trợ lý AI cá nhân - self-hosted, open-source)
  │   ├── 🎯 Định vị (Positioning)
  │   │   └── "The AI That Actually Does Things" — AI thực sự thực thi tác vụ (không chỉ chat)
  │   │   └── 💡 Kết nối AI agent với chat app & công cụ; chạy local, dữ liệu riêng tư
  │   │
  │   ├── 📡 Multi-Channel (Đa kênh)
  │   │   ├── WhatsApp, Telegram, Discord, Slack, Signal, iMessage
  │   │   └── 💡 Tương tác với trợ lý AI từ bất kỳ app nhắn tin nào
  │   │
  │   ├── 🔒 Local & Private (Chạy local & riêng tư)
  │   │   ├── Chạy trên máy của bạn (macOS, Windows, Linux) — không bắt buộc cloud
  │   │   ├── Hỗ trợ: Anthropic, OpenAI, hoặc local models (mô hình chạy local)
  │   │   └── 💡 Data không gửi lên server bên thứ ba → bảo mật mặc định
  │   │
  │   ├── 🔧 System Integration (Tích hợp hệ thống)
  │   │   ├── Browser control (điều khiển trình duyệt - web automation)
  │   │   ├── File read/write (đọc/ghi file)
  │   │   ├── Shell command execution (chạy lệnh shell)
  │   │   ├── Full system access với optional sandboxed mode (chế độ cát tùy chọn)
  │   │   └── 💡 AI có thể tự động điền form, mở trang, chạy script...
  │   │
  │   ├── 🧠 Persistent Memory & Skills (Bộ nhớ bền vững & Kỹ năng)
  │   │   ├── Nhớ preference và context theo thời gian
  │   │   ├── Custom skills (kỹ năng tùy chỉnh) / community plugins
  │   │   └── 💡 Mở rộng năng lực qua plugin, không chỉ prompt đơn thuần
  │   │
  │   ├── 🎯 Use Cases (Trường hợp dùng)
  │   │   ├── CI/CD pipeline monitoring & failure alerts (giám sát pipeline, cảnh báo lỗi)
  │   │   ├── Inbox management (quản lý hộp thư), calendar automation (tự động lịch)
  │   │   ├── Web form filling (điền form web), expense processing (xử lý chi phí)
  │   │   ├── Code refactoring (tái cấu trúc code), deployment tasks (triển khai)
  │   │   ├── Cron jobs (tác vụ định kỳ), admin workflows (luồng quản trị)
  │   │   └── 💡 Tự chạy tác vụ nền, không cần người bấm từng bước
  │   │
  │   └── 🏢 Enterprise (OpenClaw24)
  │       └── 💡 Managed implementation, integrations, security guardrails, monitoring, support
  │       └── 💡 Triển khai production với compliance (tuân thủ), kiểm soát bảo mật
  │
  ├── ⚡ n8n (Workflow Automation - Tự động hóa luồng công việc)
  │   ├── 🎯 Định vị (Positioning)
  │   │   └── Fair-code, open-source workflow automation; no-code visual + custom code
  │   │   └── 💡 Kéo thả node + viết JS/Python; 400+ tích hợp; self-host hoặc cloud
  │   │
  │   ├── 🧩 Hybrid Approach (Cách tiếp cận lai)
  │   │   ├── Drag-and-drop UI (giao diện kéo thả) + custom code (JS/Python)
  │   │   ├── Thêm npm packages, paste cURL (gọi API nhanh)
  │   │   ├── Re-run single steps (chạy lại từng bước), replay data, inline logs (debug)
  │   │   └── 💡 Vừa no-code cho PM/BA, vừa code cho dev — một nền tảng
  │   │
  │   ├── 🤖 AI Capabilities (Khả năng AI)
  │   │   ├── Native AI nodes (node AI sẵn có)
  │   │   ├── LangChain support (xây workflow AI agent)
  │   │   └── 💡 Nối chuỗi: trigger → LLM → tool → action (RAG, chatbot, phân loại...)
  │   │
  │   ├── 📦 Integrations & Deploy (Tích hợp & Triển khai)
  │   │   ├── 400+ integrations (app, DB, API, email, sheet...)
  │   │   ├── Self-host: Docker, Kubernetes, npm (npx n8n)
  │   │   ├── Cloud option (n8n cloud)
  │   │   └── 💡 Full source trên GitHub; 1700+ template workflow
  │   │
  │   ├── 🏢 Enterprise (Doanh nghiệp)
  │   │   ├── RBAC (Role-Based Access Control - phân quyền theo vai trò)
  │   │   ├── SSO, SAML, LDAP (đăng nhập tập trung)
  │   │   ├── Encrypted secret stores (lưu secret mã hóa)
  │   │   ├── Version control (phiên bản workflow), audit logs (nhật ký kiểm toán)
  │   │   └── 💡 Phù hợp team lớn, compliance, audit
  │   │
  │   └── 🎯 Use Cases (Trường hợp dùng)
  │       ├── ETL / Data pipeline (trích-biến-tải dữ liệu)
  │       ├── Slack/Email → DB/Sheet (đồng bộ dữ liệu giữa app)
  │       ├── Webhook → LLM → CRM (tự động xử lý lead, ticket)
  │       ├── Scheduled reports (báo cáo định kỳ), backup automation
  │       └── 💡 Bất kỳ luồng "khi A xảy ra → làm B, C" đều mô hình được
  │
  └── 📊 So sánh nhanh (OpenClaw vs n8n)
      ├── OpenClaw: Trọng tâm AI agent + chat (WhatsApp, Slack...), local-first, "AI làm việc thay người"
      │   └── 💡 Dùng khi: Cần trợ lý AI đa kênh, tự động hóa cá nhân/team, CI alert, inbox, calendar
      ├── n8n: Trọng tâm workflow (trigger → node → node), visual + code, 400+ app
      │   └── 💡 Dùng khi: Cần pipeline dữ liệu, tích hợp app, ETL, webhook, báo cáo định kỳ
      └── Có thể kết hợp: n8n gọi API/ webhook → OpenClaw thực thi tác vụ phức tạp có AI
  ```

  **🔑 Key Points (Ý chính):**

  - **OpenClaw (openclaw.ai / openclaws.io):** Self-hosted AI assistant — chạy trên máy bạn, kết nối WhatsApp/Telegram/Slack…, dùng OpenAI/Anthropic/local model; có browser control, file, shell, persistent memory, skills/plugins. Phù hợp giám sát CI/CD, inbox, calendar, điền form, refactor code, cron.
  - **n8n (n8n.io):** Workflow automation open-source — kéo thả node + code JS/Python, 400+ tích hợp, AI/LangChain; self-host (Docker, K8s, `npx n8n`) hoặc cloud. Phù hợp ETL, webhook, đồng bộ app, báo cáo, RBAC/SSO cho team.

  **📝 Quick Start:**

  ```bash
  # OpenClaw - cài đặt (xem docs.openclaw.ai / GitHub)
  # One-liner + setup wizard theo OS

  # n8n - chạy nhanh
  npx n8n
  # Hoặc Docker
  docker run -it --rm -p 5678:5678 n8nio/n8n
  ```

  ---

  ## 📝 **INTERVIEW PREPARATION CHECKLIST**

  _Đối chiếu với Mind Map: Nhánh 1–5 + Nhánh 6 (6.1–6.20). Đánh dấu [x] khi đã nắm vững._

  ---

  ### **✅ Must-Know (Tất cả cấp) — Nền tảng** ↔ _Mind map: §1, §2.1–2.2, §3.1 cơ bản_

  - [ ] **Data Types & Memory** (1.1): 8 types, primitives vs reference, Stack/Heap, == vs ===, falsy values
  - [ ] **Scope, Hoisting, TDZ** (1.2): Scope chain, var vs let/const, Temporal Dead Zone
  - [ ] **Closures** (1.2): Closure = function + lexical environment, use cases & memory leak
  - [ ] **Event Loop** (2.1): Call Stack → Microtasks → Render → Macrotask, thứ tự thực thi
  - [ ] **Async/Await & Promises** (2.2): Promise.all, race, allSettled, any; sequential vs parallel
  - [ ] **`this` Binding** (1.4): 4 quy tắc (new → explicit → implicit → default), arrow vs regular
  - [ ] **ES6+** (1.3): destructuring, spread/rest, arrow functions, optional chaining (?.), nullish coalescing (??)
  - [ ] **Shallow vs Deep Copy** (1.1): structuredClone(), reference vs clone
  - [ ] **DOM Events** (6.2 Browser APIs): bubbling, capturing, delegation, stopPropagation vs preventDefault
  - [ ] **React Hooks cơ bản** (3.1): useState, useEffect, useMemo, useCallback

  ---

  ### **✅ Mid-Level (1–3 năm)** ↔ _Mind map: §2.3, §3.2–3.3, §4, §6.1–6.6, 6.2–6.5 (Browser/CSS/Git)_

  - [ ] **React Query / SWR** (6.1): data fetching, cache, staleTime/cacheTime, useMutation
  - [ ] **Next.js App Router** (3.2): SSR/SSG/ISR/CSR, Server Components, Client Components, Server Actions
  - [ ] **Performance** (2.3, 3.1): Core Web Vitals (LCP, FID, CLS), memo, lazy loading, virtualization
  - [ ] **TypeScript** (4.3): Generics, Utility Types (Partial, Pick, Omit, Record), type guards
  - [ ] **State Management** (3.3): Redux vs Zustand vs Jotai vs Context, khi nào dùng gì
  - [ ] **ESM vs CommonJS** (4.2): import/export vs require, tree shaking, top-level await
  - [ ] **Build tools cơ bản** (4.1): Vite, Webpack, Turbopack — HMR, code split, tree shaking
  - [ ] **Browser Storage** (6.5, 6.2): localStorage, sessionStorage, IndexedDB, Cache API
  - [ ] **Observer APIs** (6.2): IntersectionObserver, ResizeObserver, MutationObserver
  - [ ] **HTTP Caching** (2.3): Cache-Control, ETag, stale-while-revalidate
  - [ ] **CSS Architecture** (6.4): BEM, CSS Modules, CSS-in-JS, Tailwind, responsive
  - [ ] **Git Workflow** (6.5): branching (Git Flow, GitHub Flow), merge/rebase, conventional commits
  - [ ] **AG Grid / Data Grid** (6.2, 6.9): virtual scrolling, sorting/filtering, server-side model (khi cần)
  - [ ] **UI Library** (6.3): MUI hoặc tương đương — theming, components, DataGrid
  - [ ] **Broadcast Channel** (6.4): cross-tab communication (khi cần sync tab)

  ---

  ### **✅ Senior (3+ năm)** ↔ _Mind map: §5, §6.6–6.20_

  - [ ] **System Design & Architecture** (5.1): Micro-frontends, BFF, Monorepo, Feature Flags
  - [ ] **Security** (5.2): XSS, CSRF, Auth (JWT, refresh token), CSP, secure storage
  - [ ] **Testing Strategy** (5.3): Unit (Jest/Vitest), Integration (RTL, MSW), E2E (Playwright), Visual regression
  - [ ] **CI/CD & DevOps** (5.4): Build → Test → Deploy, Docker (multi-stage, Compose), K8s cơ bản
  - [ ] **Micro-frontends & Module Federation** (6.16): Host/Remote, shared deps, runtime loading
  - [ ] **WebSocket & Real-time** (6.6): WebSocket, Socket.IO, SSE, patterns (heartbeat, reconnection)
  - [ ] **Performance Monitoring** (5.5, 6.19): Core Web Vitals, APM, Error tracking (Sentry), RUM, Distributed tracing
  - [ ] **Code Review & Leadership**: review culture, team processes
  - [ ] **Accessibility** (6.6): WCAG, ARIA, keyboard nav, focus, screen reader
  - [ ] **JavaScript Design Patterns** (6.3): Creational/Structural/Behavioral, Observer, Strategy, Command
  - [ ] **i18n** (6.10): react-i18next, RTL, date/number formatting
  - [ ] **Forms & Validation** (6.11): React Hook Form, Zod/Yup, controlled vs uncontrolled
  - [ ] **SEO & Meta Tags** (6.12): Next.js Metadata, Open Graph, JSON-LD, sitemap
  - [ ] **Animation** (6.13): Framer Motion, GSAP, CSS performance (transform/opacity)
  - [ ] **React 19 & Advanced** (6.14): Server Components, Suspense, useTransition, useOptimistic, Error Boundaries
  - [ ] **Web Workers & Service Workers** (6.15): Dedicated/Shared Worker, PWA, Workbox
  - [ ] **Edge Computing & CDN** (6.18): Vercel/Cloudflare Edge, CDN caching, cache purge
  - [ ] **Build Optimization** (6.17): Code splitting, bundle analysis, tree shaking, performance budgets
  - [ ] **API Design & GraphQL** (6.7): REST vs GraphQL, pagination, rate limiting, HTTP client best practices
  - [ ] **Date & Time** (6.8): Intl, date-fns/Day.js, timezone (UTC/store, local display)
  - [ ] **Git & Collaboration** (6.5): merge strategies, conflict resolution, pre-commit hooks
  - [ ] **AI & Automatic** (6.20): OpenClaw (trợ lý AI self-hosted, đa kênh), n8n (workflow automation)

  ---

  ### **✅ Tech Lead / Architect** ↔ _Mind map: §4–5, §6.16–6.17_

  - [ ] Large-scale System Design (thiết kế hệ thống quy mô lớn)
  - [ ] Build Tool Deep Knowledge (Vite/Webpack/Turbopack bên trong)
  - [ ] Monorepo (Nx, Turborepo) — caching, dependency graph
  - [ ] Docker & Kubernetes (container orchestration, production deployment)
  - [ ] API Design (REST vs GraphQL trade-offs, versioning)
  - [ ] Performance Budgets & Optimization strategies (bundle limits, per-route)
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

  ## 💡 **BONUS: COMMON INTERVIEW PATTERNS (Mẫu câu hỏi phỏng vấn thường gặp)**

  ```
  📍 Câu hỏi theo combo thường gặp:

  🟢 Junior (0-2 năm): Event Loop là gì? → Closures? → var vs let? → React hooks?

  🟡 Mid-level (2-4 năm): Optimize React app? → SSR vs CSR? → Handle API errors? → TypeScript generics? → Testing approach?

  🔴 Senior (4+ năm): Design chat system? → Micro-frontend architecture? → Security in banking app? → CI/CD pipeline? → Lead code review process?

  🟣 System Design Round (Vòng thiết kế hệ thống):
  - Design infinite scroll feed (luồng cuộn vô hạn)
  - Build real-time stock trading dashboard (bảng giao dịch chứng khoán thời gian thực)
  - Architect e-commerce checkout flow (luồng thanh toán thương mại điện tử)
  - Design collaborative document editor (trình soạn thảo cộng tác)
  ```

  ---

  **Happy Learning! 🚀**

  > _"The best way to predict the future is to implement it."_ - David Heinemeier Hansson

  ---

  ## 📅 **CHANGELOG**

  - **v1.0** - Initial mindmap với 5 sections chính
  - **v2.0** - Bổ sung Section 6: WebSocket, Browser APIs, CSS Architecture, Git Workflow, Accessibility, GraphQL, AG Grid, Design Patterns
  - **v2.1** - Bổ sung Q63: Docker & Containerization for Frontend (Multi-stage builds, Docker Compose, Kubernetes basics)
  - **v3.0** - 🆕 **MAJOR UPDATE** - Bổ sung 10 topics quan trọng cho Senior Frontend:
    - **6.10** Internationalization (i18n) & Localization (react-i18next, RTL support, date/number formatting)
    - **6.11** Forms & Validation (React Hook Form, Zod/Yup, controlled vs uncontrolled, async validation)
    - **6.12** SEO & Meta Tags (Next.js Metadata API, Open Graph, Structured Data JSON-LD, sitemap generation)
    - **6.13** Animation & Micro-interactions (Framer Motion, React Spring, GSAP, CSS performance)
    - **6.14** Advanced React Patterns (React 19 features, RSC deep dive, Suspense/Streaming, useTransition, Error Boundaries, XState)
    - **6.15** Web Workers & Service Workers (Dedicated Workers, Comlink, PWA strategies, Workbox, Background Sync)
    - **6.16** Module Federation & Micro-Frontends (Webpack/Vite Module Federation, Monorepo vs Multi-repo, Integration strategies)
    - **6.17** Advanced Build Optimization (Code splitting, Bundle analysis, Tree shaking, Image optimization, Performance budgets)
    - **6.18** Edge Computing & CDN Strategies (Vercel/Cloudflare Edge Functions, CDN caching, A/B testing at edge)
    - **6.19** Monitoring & Observability (Sentry, DataDog, LogRocket, RUM vs Synthetic, Distributed tracing, Structured logging)
  - **Topics covered**: **73+ câu hỏi** từ Junior đến Tech Lead (tăng từ 63 lên 73)

  ---

  **🎯 SUMMARY OF v3.0 ADDITIONS:**

  Phiên bản 3.0 bổ sung **10 kiến thức thiết yếu** cho Senior Frontend Developer mà v2.1 chưa cover đầy đủ:

  ✅ **i18n/l10n** - Quan trọng cho ứng dụng toàn cầu, nhiều ngôn ngữ
  ✅ **Forms & Validation** - React Hook Form + Zod pattern là standard hiện nay
  ✅ **SEO** - Critical cho production apps, Next.js Metadata API approach
  ✅ **Animation** - Framer Motion là go-to library cho React animations
  ✅ **React 19 & Advanced Patterns** - RSC, Suspense, Concurrent features, Error Boundaries chi tiết
  ✅ **Web Workers** - Offload heavy computation, không block UI
  ✅ **Module Federation** - Micro-frontend runtime integration standard
  ✅ **Build Optimization** - Code splitting, bundle analysis, performance budgets
  ✅ **Edge Computing** - Vercel/Cloudflare Workers cho low-latency
  ✅ **Monitoring** - Sentry, DataDog, observability strategies
