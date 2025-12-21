# 🧠 FRONTEND DEVELOPER KNOWLEDGE MINDMAP

> **Tổng hợp kiến thức Frontend từ Junior đến Senior/Tech Lead**
> Dựa trên 60+ câu hỏi phỏng vấn thực tế

---

## 📊 **VISUAL MINDMAP**

```
                                    ┌─────────────────────────────────────┐
                                    │     🎯 FRONTEND DEVELOPER          │
                                    │         KNOWLEDGE MAP              │
                                    │      (60+ Topics Covered)          │
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
─────────    ─────────    ─────────────    ─────────────    ─────────────    ─────────────
```

---

## 🌳 **MINDMAP CHI TIẾT**

---

## 🟦 **1. JAVASCRIPT CORE FUNDAMENTALS**

### **1.1 Data Types & Memory** ⭐⭐⭐

```
📦 DATA TYPES (8 loại)
├── 🔷 Primitives (7 - Immutable)
│   ├── number (64-bit float, MAX_SAFE_INTEGER)
│   ├── string (UTF-16, immutable)
│   ├── boolean (true/false)
│   ├── null (intentional empty)
│   ├── undefined (uninitialized)
│   ├── symbol (unique identifier)
│   └── bigint (arbitrary precision)
│
├── 🔶 Reference Type (1 - Mutable)
│   └── object (arrays, functions, dates, maps, sets...)
│
└── 💾 MEMORY MANAGEMENT
    ├── Stack: primitives, references (fast, LIFO)
    ├── Heap: objects (larger, GC managed)
    └── Garbage Collection: mark-and-sweep algorithm
```

**Key Points:**

- `==` vs `===` (type coercion vs strict)
- Shallow vs Deep copy (`structuredClone()`)
- Falsy values: `0, "", null, undefined, false, NaN`
- `typeof null === "object"` (legacy bug)

---

### **1.2 Scope, Hoisting & Closures** ⭐⭐⭐⭐

```
🔒 SCOPE & HOISTING
├── Scope Chain
│   ├── Global Scope
│   ├── Function Scope
│   └── Block Scope (let/const)
│
├── Hoisting
│   ├── var: hoisted + undefined
│   ├── let/const: hoisted + TDZ (Temporal Dead Zone)
│   └── function declaration: fully hoisted
│
└── Closures
    ├── Function remembers outer scope
    ├── Private variables pattern
    ├── Factory functions
    └── ⚠️ Memory leak potential
```

**Interview Tips:**

- Closure = function + lexical environment
- TDZ = zone from start of block to declaration
- `var` là function-scoped, `let/const` là block-scoped

---

### **1.3 ES6+ Modern Features** ⭐⭐⭐

```
🚀 ES6+ FEATURES
├── Variables
│   ├── let/const (block scope)
│   └── Destructuring (object/array)
│
├── Functions
│   ├── Arrow functions (lexical this)
│   ├── Default parameters
│   └── Rest/Spread operators
│
├── OOP
│   ├── Classes (syntactic sugar)
│   ├── Inheritance (extends)
│   └── Static methods
│
├── Data Structures
│   ├── Map/Set
│   ├── WeakMap/WeakSet
│   └── Symbol
│
└── Syntax
    ├── Template literals
    ├── Optional chaining (?.)
    └── Nullish coalescing (??)
```

---

### **1.4 `this` Binding & Functions** ⭐⭐⭐⭐

```
🎯 THIS BINDING (Thứ tự ưu tiên)
1. new binding       → this = new object
2. explicit binding  → call/apply/bind
3. implicit binding  → obj.method()
4. default binding   → global / undefined (strict)

📌 Arrow vs Regular Functions
├── Arrow: lexical this, no arguments, no constructor
└── Regular: dynamic this, has arguments, can be constructor
```

---

## 🟩 **2. ASYNC & PERFORMANCE**

### **2.1 Event Loop** ⭐⭐⭐⭐⭐ (MUST KNOW!)

```
♻️ EVENT LOOP FLOW
┌─────────────────────────────────────────────────────────┐
│  Call Stack  →  Microtasks  →  Render  →  1 Macrotask  │
│      ↑__________________________________________________|
└─────────────────────────────────────────────────────────┘

📋 TASK QUEUES
├── Microtask Queue (HIGH PRIORITY)
│   ├── Promise.then/catch/finally
│   ├── queueMicrotask()
│   └── MutationObserver
│   → Chạy HẾT trước khi render
│
└── Macrotask Queue (LOW PRIORITY)
    ├── setTimeout/setInterval
    ├── I/O operations
    └── requestAnimationFrame
    → Chạy 1 task mỗi vòng
```

---

### **2.2 Async Patterns** ⭐⭐⭐⭐

```
⚡ ASYNC EVOLUTION
├── Callbacks (ES5) → Callback Hell
├── Promises (ES6)
│   ├── Promise.all() - Parallel, fail-fast
│   ├── Promise.allSettled() - Wait all, no fail
│   ├── Promise.race() - First settled
│   └── Promise.any() - First fulfilled
│
├── Async/Await (ES2017)
│   ├── Sequential: await a; await b;
│   └── Parallel: await Promise.all([a, b])
│
└── Advanced
    ├── AbortController (Cancellation)
    ├── p-limit (Concurrency control)
    └── Retry strategies (exponential backoff)
```

---

### **2.3 Caching & Performance** ⭐⭐⭐⭐

```
🗄️ CACHING STRATEGIES
├── HTTP Caching
│   ├── Cache-Control (max-age, no-cache, no-store)
│   ├── ETag / If-None-Match
│   └── Last-Modified / If-Modified-Since
│
├── Browser Caching
│   ├── Memory Cache (fastest, tab-specific)
│   ├── Disk Cache (persistent)
│   └── Service Worker Cache (offline)
│
└── Application Caching
    ├── React Query (stale-while-revalidate)
    ├── SWR
    └── Apollo Cache (GraphQL)

🎨 BROWSER RENDERING
├── Critical Rendering Path
│   DOM → CSSOM → Render Tree → Layout → Paint → Composite
│
├── Performance Metrics
│   ├── LCP (Largest Contentful Paint)
│   ├── FID (First Input Delay)
│   ├── CLS (Cumulative Layout Shift)
│   └── TTFB (Time To First Byte)
│
└── Optimization
    ├── Avoid forced synchronous layout
    ├── Batch DOM reads/writes
    └── Use requestAnimationFrame for animations
```

---

## 🟨 **3. REACT & FRAMEWORKS**

### **3.1 React Deep Dive** ⭐⭐⭐⭐⭐

```
⚛️ REACT CORE CONCEPTS
├── Component Types
│   ├── Functional Components (hooks)
│   └── Class Components (legacy)
│
├── Hooks
│   ├── State: useState, useReducer
│   ├── Effects: useEffect, useLayoutEffect
│   ├── Memoization: useMemo, useCallback
│   ├── Refs: useRef, useImperativeHandle
│   ├── Context: useContext
│   └── New (React 19): useOptimistic, useFormStatus, use
│
├── State Management
│   ├── Local: useState
│   ├── Global: Context, Redux, Zustand, Jotai
│   └── Server: React Query, SWR
│
├── Performance
│   ├── React.memo (prevent re-renders)
│   ├── useMemo (memoize values)
│   ├── useCallback (memoize functions)
│   ├── Code splitting (React.lazy)
│   └── Virtualization (react-window)
│
└── Patterns
    ├── Compound Components
    ├── Render Props
    ├── Higher-Order Components (HOC)
    ├── Custom Hooks
    └── Container/Presentational
```

---

### **3.2 Next.js 14/15/16** ⭐⭐⭐⭐⭐

```
🔺 NEXT.JS CONCEPTS
├── Rendering Strategies
│   ├── SSR (Server-Side Rendering) - cache: 'no-store'
│   ├── SSG (Static Site Generation) - cache: 'force-cache'
│   ├── ISR (Incremental Static Regen) - revalidate: N
│   └── CSR (Client-Side Rendering)
│
├── App Router (Next.js 13+)
│   ├── Server Components (default)
│   ├── Client Components ('use client')
│   ├── Server Actions ('use server')
│   ├── Route Handlers (API Routes)
│   └── Streaming & Suspense
│
├── Data Fetching
│   ├── fetch() with caching options
│   ├── Parallel fetching (Promise.all)
│   └── revalidatePath / revalidateTag
│
├── File-based Features
│   ├── page.tsx (routes)
│   ├── layout.tsx (shared UI)
│   ├── loading.tsx (loading UI)
│   ├── error.tsx (error boundary)
│   └── not-found.tsx (404)
│
└── Next.js 16 (NEW!)
    ├── Turbopack (default bundler)
    ├── React 19 support
    └── Enhanced Server Actions
```

---

### **3.3 State Management Comparison** ⭐⭐⭐⭐

```
🔄 STATE MANAGEMENT LIBRARIES

┌─────────────┬────────────┬───────────┬─────────────┐
│   Feature   │   Redux    │  Zustand  │   Jotai     │
├─────────────┼────────────┼───────────┼─────────────┤
│ Bundle Size │   ~8KB     │   ~2KB    │   ~3KB      │
│ Boilerplate │   High     │   Low     │   Minimal   │
│ DevTools    │   ✅ Rich  │   ✅ Good │   ✅ Good   │
│ Learning    │   Steep    │   Easy    │   Easy      │
│ Best For    │ Enterprise │ Mid-size  │ Fine-grain  │
└─────────────┴────────────┴───────────┴─────────────┘

📌 When to use:
├── Redux: Large apps, complex state, middleware needs
├── Zustand: Most apps, simple API, small bundle
├── Jotai: Fine-grained reactivity, atom-based
└── Context: Small apps, prop drilling solution
```

---

## 🟧 **4. BUILD TOOLS & DEVOPS**

### **4.1 Build Tools Comparison** ⭐⭐⭐⭐

```
🔧 BUILD TOOLS ECOSYSTEM

┌─────────────┬──────────────┬──────────────┬──────────────┐
│   Tool      │  Dev Speed   │  Build Speed │  Use Case    │
├─────────────┼──────────────┼──────────────┼──────────────┤
│ Vite        │  ⚡⚡⚡⚡⚡    │  ⚡⚡⚡⚡     │  Modern apps │
│ Turbopack   │  ⚡⚡⚡⚡⚡    │  ⚡⚡⚡⚡⚡   │  Next.js 16  │
│ Webpack     │  ⚡⚡        │  ⚡⚡⚡      │  Legacy/Complex│
│ esbuild     │  ⚡⚡⚡⚡⚡    │  ⚡⚡⚡⚡⚡   │  Bundler/Minify│
│ Rollup      │  ⚡⚡⚡      │  ⚡⚡⚡⚡     │  Libraries   │
└─────────────┴──────────────┴──────────────┴──────────────┘

📦 BUNDLER CONCEPTS
├── Tree Shaking (remove dead code)
├── Code Splitting (lazy loading)
├── Minification (uglify/terser)
├── Source Maps (debugging)
└── Hot Module Replacement (HMR)
```

---

### **4.2 Module Systems** ⭐⭐⭐

```
📦 ESM vs CommonJS

┌───────────────┬──────────────────┬──────────────────┐
│   Feature     │      ESM         │    CommonJS      │
├───────────────┼──────────────────┼──────────────────┤
│ Syntax        │ import/export    │ require/exports  │
│ Loading       │ Async (static)   │ Sync (dynamic)   │
│ Tree Shaking  │ ✅ Yes           │ ❌ Limited       │
│ Top-level     │ ✅ await         │ ❌ No            │
│ Browser       │ ✅ Native        │ ❌ Bundler       │
│ this value    │ undefined        │ module.exports   │
└───────────────┴──────────────────┴──────────────────┘
```

---

### **4.3 TypeScript Advanced** ⭐⭐⭐⭐⭐

```
📘 TYPESCRIPT PATTERNS
├── Generics
│   ├── Generic Functions
│   ├── Generic Constraints (extends)
│   └── Generic Utilities
│
├── Utility Types
│   ├── Partial<T>, Required<T>
│   ├── Pick<T, K>, Omit<T, K>
│   ├── Record<K, V>
│   └── ReturnType<T>, Parameters<T>
│
├── Advanced
│   ├── Mapped Types
│   ├── Conditional Types
│   ├── Type Guards (is, in)
│   ├── Branded Types
│   └── Template Literal Types
│
└── Best Practices
    ├── Prefer interfaces for objects
    ├── Use type for unions/intersections
    └── Avoid any, use unknown
```

---

## 🟥 **5. SENIOR-LEVEL TOPICS**

### **5.1 System Design & Architecture** ⭐⭐⭐⭐⭐

```
🏗️ FRONTEND ARCHITECTURE
├── Micro-Frontends
│   ├── Module Federation
│   ├── Multi-framework support
│   └── Communication patterns (Events, SharedState)
│
├── Monorepo
│   ├── Nx (recommended)
│   ├── Turborepo
│   └── Lerna (legacy)
│
├── Patterns
│   ├── BFF (Backend For Frontend)
│   ├── Feature Flags
│   ├── A/B Testing
│   └── Error Boundaries
│
└── Scalability
    ├── Lazy loading
    ├── CDN optimization
    ├── Edge computing
    └── Server-side caching
```

---

### **5.2 Security** ⭐⭐⭐⭐⭐

```
🔐 WEB SECURITY (7 LAYERS)
├── 1. HTTPS & TLS
│   └── Certificate pinning, HSTS
│
├── 2. XSS Prevention
│   ├── Input sanitization (DOMPurify)
│   ├── Output encoding
│   └── CSP headers
│
├── 3. CSRF Protection
│   ├── CSRF tokens
│   └── SameSite cookies
│
├── 4. Authentication
│   ├── Access Token (JWT - 15min)
│   ├── Refresh Token (7-30 days)
│   └── Token rotation strategy
│
├── 5. Secure Storage
│   ├── httpOnly cookies (tokens)
│   ├── localStorage (non-sensitive)
│   └── Avoid sessionStorage for auth
│
├── 6. API Security
│   ├── Rate limiting
│   ├── Request validation
│   └── CORS configuration
│
└── 7. Headers
    ├── Content-Security-Policy
    ├── X-Frame-Options
    ├── X-Content-Type-Options
    └── Referrer-Policy
```

---

### **5.3 Testing Strategy** ⭐⭐⭐⭐⭐

```
🧪 TEST PYRAMID
         /\
        /E2E\       ← Playwright/Cypress (10%)
       /------\
      /  INT   \    ← React Testing Library (20%)
     /----------\
    /    UNIT    \  ← Jest/Vitest (70%)
   /--------------\

📋 TESTING TOOLS
├── Unit Tests
│   ├── Jest / Vitest
│   └── Testing coverage (istanbul)
│
├── Integration Tests
│   ├── React Testing Library
│   └── MSW (Mock Service Worker)
│
├── E2E Tests
│   ├── Playwright (recommended)
│   └── Cypress
│
└── Visual Regression
    └── Chromatic / Percy
```

---

### **5.4 CI/CD & DevOps** ⭐⭐⭐⭐

```
🚀 CI/CD PIPELINE
├── Build Stage
│   ├── Install dependencies (cached)
│   ├── Lint & Type check
│   ├── Unit tests
│   └── Build artifacts
│
├── Test Stage
│   ├── Integration tests
│   ├── E2E tests
│   └── Visual regression
│
├── Deploy Stage
│   ├── Preview deployments (PR)
│   ├── Staging environment
│   └── Production (Blue-Green/Canary)
│
└── Tools
    ├── GitHub Actions
    ├── GitLab CI
    └── Vercel / Netlify
```

---

### **5.5 Performance Monitoring** ⭐⭐⭐⭐

```
📊 APM (Application Performance Monitoring)
├── Core Web Vitals
│   ├── LCP < 2.5s (Largest Contentful Paint)
│   ├── FID < 100ms (First Input Delay)
│   ├── CLS < 0.1 (Cumulative Layout Shift)
│   └── INP < 200ms (Interaction to Next Paint)
│
├── Monitoring Tools
│   ├── Sentry (Error tracking)
│   ├── DataDog (Full APM)
│   ├── LogRocket (Session replay)
│   └── Lighthouse (Audits)
│
└── Optimization
    ├── Performance budgets
    ├── Bundle analysis
    └── Real User Monitoring (RUM)
```

---

## 🟪 **6. BỔ SUNG - TOPICS QUAN TRỌNG KHÁC**

### **6.1 React Query (TanStack Query)** ⭐⭐⭐⭐⭐

```
🔄 DATA FETCHING & CACHING LIBRARY // Thư viện lấy dữ liệu & cache
├── Core Concepts // Khái niệm cốt lõi
│   ├── Server State Management (khác Redux/Zustand) // Quản lý state từ server
│   ├── Automatic Background Refetching // Tự động làm mới dữ liệu nền
│   ├── Caching & Deduplication // Cache và loại bỏ trùng lặp
│   └── Optimistic Updates // Cập nhật lạc quan (UI update trước, gọi API sau)
│
├── Key Features // Tính năng chính
│   ├── useQuery (GET data) // Hook lấy dữ liệu
│   │   ├── staleTime: 0 (data immediately stale) // Thời gian data cũ (0 = cũ ngay)
│   │   ├── cacheTime: 5 min (garbage collection) // Thời gian giữ cache
│   │   ├── refetchOnWindowFocus: true // Làm mới khi focus vào tab
│   │   └── retry: 3 lần // Thử lại 3 lần khi lỗi
│   │
│   ├── useMutation (POST/PUT/DELETE) // Hook thay đổi dữ liệu
│   │   ├── onSuccess/onError callbacks // Callback khi thành công/lỗi
│   │   ├── Invalidate queries after success // Xóa cache sau khi thành công
│   │   └── Optimistic updates // Cập nhật UI trước, call API sau
│   │
│   ├── useInfiniteQuery (Pagination/Infinite scroll) // Hook phân trang vô hạn
│   │   ├── getNextPageParam // Lấy tham số trang tiếp theo
│   │   └── fetchNextPage() // Hàm load thêm dữ liệu
│   │
│   └── Advanced // Nâng cao
│       ├── Prefetching (queryClient.prefetchQuery) // Tải trước dữ liệu
│       ├── Query Invalidation // Xóa cache query
│       ├── Query Cancellation // Hủy request đang chạy
│       └── Dependent Queries (enabled based on condition) // Query phụ thuộc điều kiện
│
├── Best Practices // Thực hành tốt
│   ├── Use query keys properly ['users', userId] // Dùng query key đúng cách
│   ├── Set appropriate staleTime & cacheTime // Đặt thời gian stale/cache phù hợp
│   ├── Handle loading/error states // Xử lý trạng thái loading/lỗi
│   └── Invalidate queries after mutations // Xóa cache sau khi mutation
│
└── Use Cases // Trường hợp sử dụng
    ├── ✅ API calls, data fetching // Gọi API, lấy dữ liệu
    ├── ✅ Real-time updates (polling/SSE) // Cập nhật real-time
    ├── ✅ Offline support with cache // Hỗ trợ offline với cache
    └── ❌ Client state (use Zustand/Redux) // KHÔNG dùng cho state client

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
📊 ENTERPRISE DATA GRID (Best for Complex Tables) // Bảng dữ liệu doanh nghiệp
├── Core Features // Tính năng cốt lõi
│   ├── Virtual Scrolling (handle millions of rows) // Cuộn ảo (xử lý hàng triệu dòng)
│   ├── Column Pinning (left/right) // Ghim cột (trái/phải)
│   ├── Row Grouping & Aggregation // Nhóm dòng & tổng hợp
│   ├── Sorting & Filtering (client & server-side) // Sắp xếp & lọc (client/server)
│   ├── Cell Editing (inline & popup) // Sửa ô (trực tiếp/popup)
│   └── CSV/Excel Export // Xuất CSV/Excel
│
├── Advanced Features // Tính năng nâng cao
│   ├── Master-Detail (expandable rows) // Dòng mở rộng (chi tiết)
│   ├── Tree Data // Dữ liệu dạng cây
│   ├── Pivot Mode // Chế độ pivot (xoay bảng)
│   ├── Charting Integration // Tích hợp biểu đồ
│   ├── Server-Side Row Model (lazy loading) // Model server (load từ từ)
│   └── Custom Cell Renderers/Editors // Tùy chỉnh hiển thị/sửa ô
│
├── Performance // Hiệu suất
│   ├── Row Virtualization (only render visible rows) // Chỉ render dòng hiển thị
│   ├── Column Virtualization // Ảo hóa cột
│   ├── Debounced Filtering // Lọc với debounce
│   └── Delta Updates (updateRowData) // Cập nhật từng phần
│
├── Comparison
│   ├── AG Grid vs TanStack Table
│   │   ├── AG Grid: Enterprise, full-featured, paid license
│   │   └── TanStack Table: Headless, free, more flexible
│   │
│   └── AG Grid vs MUI DataGrid
│       ├── AG Grid: Better performance, more features
│       └── MUI DataGrid: Better UI, Material Design
│
└── Best Practices
    ├── Use suppressColumnVirtualisation: false
    ├── Enable pagination for >10k rows
    ├── Use getRowId for stable row references
    └── Debounce filter changes

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
│   ├── Layout // Bố cục
│   │   ├── Box (base component với sx prop) // Component cơ bản nhất
│   │   ├── Container, Grid, Stack // Container, lưới, stack
│   │   └── Paper, Card // Giấy, thẻ
│   │
│   ├── Inputs // Đầu vào
│   │   ├── TextField, Select, Autocomplete // Ô nhập, chọn, tự động hoàn thành
│   │   ├── Checkbox, Radio, Switch // Hộp kiểm, nút radio, công tắc
│   │   └── DatePicker, TimePicker // Chọn ngày, chọn giờ
│   │
│   ├── Navigation // Điều hướng
│   │   ├── AppBar, Toolbar, Drawer // Thanh app, thanh công cụ, ngăn kéo
│   │   ├── Tabs, Breadcrumbs // Tab, đường dẫn breadcrumb
│   │   └── BottomNavigation // Điều hướng dưới
│   │
│   └── Feedback // Phản hồi
│       ├── Dialog, Snackbar, Alert // Hộp thoại, thông báo nhỏ, cảnh báo
│       ├── Progress (Linear/Circular) // Tiến trình (dạng thanh/tròn)
│       └── Skeleton // Khung xương (loading placeholder)
│
├── Theming System // Hệ thống theme
│   ├── createTheme() // Tạo theme
│   │   ├── palette (primary, secondary, error...) // Bảng màu
│   │   ├── typography (h1-h6, body1-2...) // Kiểu chữ
│   │   ├── spacing (8px base unit) // Khoảng cách (đơn vị 8px)
│   │   └── breakpoints (xs, sm, md, lg, xl) // Điểm breakpoint responsive
│   │
│   ├── ThemeProvider // Provider cung cấp theme
│   ├── Dark Mode (mode: 'light' | 'dark') // Chế độ tối
│   └── Custom Theme Variables // Biến theme tùy chỉnh
│
├── Styling Solutions // Giải pháp styling
│   ├── sx prop (recommended) // Prop sx (khuyến nghị)
│   ├── styled() utility // Hàm styled
│   ├── makeStyles (deprecated in v5) // makeStyles (đã bỏ v5)
│   └── Emotion (CSS-in-JS engine) // Engine CSS-in-JS
│
├── Data Display // Hiển thị dữ liệu
│   ├── DataGrid (basic - free) // Bảng dữ liệu cơ bản (miễn phí)
│   ├── DataGridPro (advanced - paid) // Bảng nâng cao (trả phí)
│   ├── Table (native HTML table) // Bảng HTML thuần
│   └── List, Accordion // Danh sách, Accordion
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
│   ├── Browser API for tab-to-tab messaging // API gửi tin nhắn giữa các tab
│   ├── Same origin only // Chỉ cùng origin
│   ├── Faster than localStorage events // Nhanh hơn localStorage events
│   └── Use: Sync state across tabs // Dùng để: Đồng bộ state giữa tabs
│
├── API
│   ├── new BroadcastChannel(name) // Tạo kênh broadcast
│   ├── channel.postMessage(data) // Gửi tin nhắn
│   ├── channel.onmessage = (event) => {} // Lắng nghe tin nhắn
│   └── channel.close() // Đóng kênh
│
├── Use Cases // Trường hợp sử dụng
│   ├── Logout all tabs when user logs out // Logout tất cả tab khi user logout
│   ├── Sync shopping cart across tabs // Đồng bộ giỏ hàng giữa các tab
│   ├── Real-time notifications // Thông báo real-time
│   └── Multi-tab collaboration // Cộng tác đa tab
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
│   ├── NoSQL key-value store // Lưu trữ key-value NoSQL
│   ├── Store large amounts of data (>250MB) // Lưu dữ liệu lớn (>250MB)
│   ├── Transactional (ACID) // Hỗ trợ giao dịch ACID
│   ├── Asynchronous API // API bất đồng bộ
│   └── Indexes for fast queries // Index để query nhanh
│
├── Use Cases // Trường hợp sử dụng
│   ├── ✅ Offline-first apps (PWA) // App offline-first (PWA)
│   ├── ✅ Caching API responses // Cache response API
│   ├── ✅ Store files/blobs // Lưu file/blob
│   └── ❌ Simple key-value (use localStorage) // Key-value đơn giản (dùng localStorage)
│
├── API (Low-level) // API cấp thấp
│   ├── indexedDB.open(dbName, version) // Mở database
│   ├── objectStore.add/put/get/delete // Thêm/sửa/lấy/xóa
│   ├── Indexes (createIndex) // Tạo index
│   └── Transactions // Giao dịch
│
├── Wrappers (Recommended) // Thư viện wrapper (khuyến nghị)
│   ├── Dexie.js (most popular) // Phổ biến nhất
│   ├── localForage (simple API) // API đơn giản
│   └── idb (Google's wrapper) // Wrapper của Google
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
│   ├── Persistent bidirectional TCP connection // Kết nối TCP 2 chiều liên tục
│   ├── Protocol: ws:// (unsecure) / wss:// (SSL) // Giao thức ws/wss
│   ├── Lower latency than polling (~50ms) // Độ trễ thấp hơn polling
│   └── Use: Trading, Chat, Live notifications // Dùng: Giao dịch, chat, thông báo
│
├── Socket.IO
│   ├── WebSocket wrapper + fallback to polling // Wrapper WebSocket + dự phòng polling
│   ├── Auto-reconnect // Tự động kết nối lại
│   ├── Rooms & Namespaces // Phòng & không gian tên
│   └── Event-based API: socket.emit() // API dựa trên sự kiện
│
├── Server-Sent Events (SSE)
│   ├── Server → Client only (unidirectional) // Chỉ 1 chiều Server → Client
│   ├── Auto-reconnect built-in // Tự động kết nối lại có sẵn
│   └── Simpler than WebSocket // Đơn giản hơn WebSocket
│
└── Patterns // Mẫu thiết kế
    ├── Heartbeat/Ping-Pong (detect dead connections) // Nhịp tim (phát hiện kết nối chết)
    ├── Reconnection with exponential backoff // Kết nối lại với backoff mũ
    └── Binary frames (faster than JSON) // Frame nhị phân (nhanh hơn JSON)

📊 COMPARISON
┌─────────────┬───────────┬───────────┬─────────────┐
│ Feature     │ WebSocket │ Socket.IO │ SSE         │
├─────────────┼───────────┼───────────┼─────────────┤
│ Direction   │ Bi-direct │ Bi-direct │ Server→Client│
│ Reconnect   │ Manual    │ Auto      │ Auto        │
│ Fallback    │ No        │ Yes       │ No          │
│ Binary      │ Yes       │ Yes       │ No          │
│ Use Case    │ Trading   │ Chat      │ Notifications│
└─────────────┴───────────┴───────────┴─────────────┘
```

---

### **6.2 Browser APIs & DOM** ⭐⭐⭐⭐

```
🌐 BROWSER APIs
├── Observer APIs
│   ├── IntersectionObserver (lazy load, infinite scroll)
│   ├── ResizeObserver (element size changes)
│   ├── MutationObserver (DOM changes)
│   └── PerformanceObserver (performance metrics)
│
├── Storage APIs
│   ├── localStorage (5MB, persistent)
│   ├── sessionStorage (5MB, tab-specific)
│   ├── IndexedDB (large data, async)
│   ├── Cookies (4KB, sent with requests)
│   └── Cache API (Service Worker caching)
│
├── DOM Events
│   ├── Event Flow: Capturing → Target → Bubbling
│   ├── Event Delegation (attach to parent)
│   ├── stopPropagation() vs preventDefault()
│   └── Passive listeners (improve scroll perf)
│
└── Web Workers
    ├── Dedicated Worker (single script)
    ├── Shared Worker (shared across tabs)
    └── Service Worker (offline, push notifications)
```

---

### **6.3 JavaScript Advanced Patterns** ⭐⭐⭐⭐⭐

```
🎨 DESIGN PATTERNS
├── Creational
│   ├── Singleton (one instance only)
│   ├── Factory (create objects)
│   └── Builder (step-by-step construction)
│
├── Structural
│   ├── Module (encapsulation)
│   ├── Facade (simplified interface)
│   └── Decorator (extend behavior)
│
├── Behavioral
│   ├── Observer/PubSub (event handling)
│   ├── Strategy (interchangeable algorithms)
│   └── Command (encapsulate actions)
│
└── Advanced JS Features
    ├── Proxy (intercept operations)
    │   └── Use: Validation, logging, reactivity (Vue)
    ├── Generators (yield, iterators)
    │   └── Use: Async iteration, infinite sequences
    ├── Reflect API
    └── WeakRef & FinalizationRegistry

📦 REACT DESIGN PATTERNS
├── Compound Components
│   └── <Tabs><Tab/><TabPanel/></Tabs>
├── Render Props
│   └── <DataProvider render={(data) => ...}/>
├── Higher-Order Components (HOC)
│   └── withAuth(Component)
├── Custom Hooks
│   └── useLocalStorage, useDebounce
├── Container/Presentational
│   └── Logic vs UI separation
└── Controlled vs Uncontrolled
    └── Form components
```

---

### **6.4 CSS Architecture & Styling** ⭐⭐⭐⭐

```
🎨 CSS METHODOLOGIES
├── BEM (Block Element Modifier)
│   └── .block__element--modifier
│
├── CSS Modules
│   └── Scoped styles, no conflicts
│
├── CSS-in-JS
│   ├── styled-components
│   ├── Emotion
│   └── Pros: Dynamic, scoped / Cons: Runtime cost
│
├── Utility-First (Tailwind CSS)
│   └── Pros: Fast, consistent / Cons: Verbose HTML
│
└── Modern CSS
    ├── CSS Variables (Custom Properties)
    ├── Container Queries
    ├── CSS Grid & Flexbox
    ├── CSS Layers (@layer)
    └── CSS Nesting (native)

📐 RESPONSIVE DESIGN
├── Mobile-First approach
├── Breakpoints strategy
├── Fluid typography (clamp())
└── Container queries vs Media queries
```

---

### **6.5 Git Workflow & Collaboration** ⭐⭐⭐

```
🔀 GIT STRATEGIES
├── Branching Models
│   ├── Git Flow (feature/develop/release/hotfix)
│   ├── GitHub Flow (main + feature branches)
│   └── Trunk-Based (small PRs to main)
│
├── Merge Strategies
│   ├── Merge commit (preserve history)
│   ├── Squash merge (clean history)
│   └── Rebase (linear history)
│
├── Best Practices
│   ├── Conventional Commits (feat:, fix:, docs:)
│   ├── Small, focused PRs
│   ├── Code review culture
│   └── Pre-commit hooks (Husky)
│
└── Conflict Resolution
    ├── git rebase --continue
    ├── git merge --abort
    └── Resolve in IDE (VS Code, JetBrains)
```

---

### **6.6 Accessibility (a11y)** ⭐⭐⭐⭐

```
♿ WEB ACCESSIBILITY
├── WCAG 2.1 Guidelines
│   ├── Perceivable (alt text, contrast)
│   ├── Operable (keyboard nav, focus)
│   ├── Understandable (clear labels)
│   └── Robust (valid HTML, ARIA)
│
├── ARIA Attributes
│   ├── role="button", role="dialog"
│   ├── aria-label, aria-labelledby
│   ├── aria-expanded, aria-hidden
│   └── aria-live (announcements)
│
├── Keyboard Navigation
│   ├── Tab order (tabindex)
│   ├── Focus management
│   └── Skip links
│
├── Testing Tools
│   ├── axe-core / axe DevTools
│   ├── Lighthouse accessibility
│   └── Screen reader testing (NVDA, VoiceOver)
│
└── Common Issues
    ├── Missing alt text
    ├── Low color contrast
    ├── No focus indicators
    └── Missing form labels
```

---

### **6.7 API Design & GraphQL** ⭐⭐⭐⭐

```
🔌 API PATTERNS
├── REST API
│   ├── Resources & HTTP methods
│   ├── Status codes (200, 400, 401, 404, 500)
│   ├── Pagination (offset, cursor)
│   └── Rate limiting
│
├── GraphQL
│   ├── Query (read), Mutation (write)
│   ├── Fragments (reusable fields)
│   ├── Subscriptions (real-time)
│   └── Apollo Client (caching, state)
│
├── GraphQL vs REST
│   ┌─────────────┬──────────────┬──────────────┐
│   │ Feature     │ REST         │ GraphQL      │
│   ├─────────────┼──────────────┼──────────────┤
│   │ Data fetch  │ Over/Under   │ Exact data   │
│   │ Endpoints   │ Multiple     │ Single       │
│   │ Versioning  │ /v1, /v2     │ Schema evolution│
│   │ Caching     │ HTTP cache   │ Apollo/Relay │
│   │ Learning    │ Easy         │ Steeper      │
│   └─────────────┴──────────────┴──────────────┘
│
└── HTTP Client Best Practices
    ├── Axios interceptors (auth, error handling)
    ├── Request/Response transformation
    ├── Retry strategies
    └── Request cancellation (AbortController)
```

---

### **6.8 Date & Time Handling** ⭐⭐⭐

```
📅 DATE/TIME IN JAVASCRIPT
├── Native APIs
│   ├── Date object (mutable, quirky)
│   ├── Intl.DateTimeFormat (localization)
│   └── Temporal API (upcoming standard)
│
├── Libraries
│   ├── date-fns (functional, tree-shakeable)
│   ├── Day.js (lightweight Moment alternative)
│   └── Luxon (Moment successor, immutable)
│
├── Timezone Handling
│   ├── Store in UTC, display in local
│   ├── ISO 8601 format (2024-01-15T10:30:00Z)
│   └── Intl.DateTimeFormat with timeZone option
│
└── Common Pitfalls
    ├── Month is 0-indexed (0 = January)
    ├── Date parsing inconsistency across browsers
    ├── Daylight Saving Time edge cases
    └── Comparing dates (use timestamps)
```

---

### **6.9 Enterprise Data Grids (AG Grid)** ⭐⭐⭐⭐

```
📊 AG GRID (Enterprise)
├── Core Concepts
│   ├── Column Definitions
│   ├── Row Data (client-side / server-side)
│   ├── Cell Renderers & Editors
│   └── Row Models (Client, Server, Infinite, Viewport)
│
├── Performance Optimization
│   ├── getRowId (stable row identity)
│   ├── deltaRowDataMode (update only changes)
│   ├── applyTransactionAsync (batch updates)
│   └── Column virtualization
│
├── Features
│   ├── Sorting, Filtering, Grouping
│   ├── Row selection (single, multi)
│   ├── Excel export
│   └── Master-Detail views
│
└── Real-time Updates
    ├── WebSocket integration
    ├── Async transaction updates
    └── Cell flash on value change
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
- **Topics covered**: 60+ câu hỏi từ Junior đến Tech Lead
