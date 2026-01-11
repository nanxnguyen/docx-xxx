# 🚀 Q38: Tối Ưu Performance của React Web App

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"Tối ưu hiệu năng React = 5 lớp (5 layers): Build-time (Lúc build), Mạng (Network), Rendering (Render), State (Trạng thái), Bộ nhớ (Memory).**

**🏗️ Chiến Lược Tối Ưu 5 Lớp (5-Layer Optimization Strategy):**

1. **Tối Ưu Build-time (Tối ưu lúc build)**:

   - **Chia Code (Code Splitting)**: `React.lazy()` + Suspense → tải routes theo yêu cầu (load routes on demand - tải khi cần).
   - **Tree-shaking**: Xóa code không dùng (remove unused code - ES modules + Webpack/Vite).
   - **Phân Tích Bundle (Bundle Analysis)**: `webpack-bundle-analyzer` → xác định dependencies lớn (identify large dependencies).
   - **Mục tiêu (Target)**: Giảm bundle 2.5MB → 500KB (nhanh hơn 5 lần - 5x faster).

2. **Tối Ưu Mạng (Network Optimization)**:

   - **HTTP/2 + Brotli**: Nén tài nguyên 70% (compress resources 70%).
   - **CDN**: Phục vụ tài nguyên tĩnh từ edge servers (serve static resources from edge servers - độ trễ thấp hơn - lower latency).
   - **Gợi ý Tài Nguyên (Resource Hints)**: `<link rel="preload">` fonts, CSS quan trọng (critical CSS).
   - **Service Worker**: Cache tài nguyên tĩnh (cache static resources) → hỗ trợ offline (offline support).

3. **Tối Ưu Rendering (Rendering Optimization)** (⚡ Quan Trọng Nhất - Most Important):

   - **React.memo()**: Ngăn con render lại khi props không đổi (prevent child re-render when props unchanged).
   - **useMemo/useCallback**: Cache tính toán/hàm tốn kém (cache expensive computations/functions).
   - **Virtual Scrolling**: `react-window` cho 10K+ items → chỉ render phần hiển thị (only render visible portion).
   - **Debounce/Throttle**: Giới hạn event handlers (limit event handlers - scroll, resize, input).
   - **Lazy Images**: `loading="lazy"` + Intersection Observer (tải ảnh khi cần).

4. **Quản Lý State (State Management)**:

   - **Tách Context (Context Splitting)**: Tách contexts nhỏ (split into small contexts) → ngăn re-renders không cần thiết (prevent unnecessary re-renders).
   - **Zustand/Redux Toolkit**: Đăng ký chọn lọc (selective subscriptions) → components chỉ render lại khi state thực sự dùng thay đổi (components only re-render when used state changes).
   - **React Query**: Cache dữ liệu server (cache server data) → giảm lời gọi API (reduce API calls).
   - **Immer**: Cập nhật bất biến hiệu quả (efficient immutable updates - ít boilerplate hơn - less boilerplate).

5. **Quản Lý Bộ Nhớ (Memory Management)**:
   - **Dọn Dẹp Effects (Cleanup Effects)**: `useEffect` trả về cleanup (return cleanup function) → xóa listeners (remove listeners), hủy timers (cancel timers).
   - **WeakMap**: Giữ tham chiếu yếu (hold weak references) → tự động GC (automatic garbage collection).
   - **Profiling**: Chrome DevTools Memory tab → phát hiện rò rỉ (detect memory leaks).

**🎯 Real-time Updates Optimization (Tối Ưu Cập Nhật Thời Gian Thực - WebSocket):**

- **Problem (Vấn đề)**: 1000 updates/s (1000 cập nhật/giây) → 60+ components re-render (60+ component render lại) → UI freeze (giao diện đóng băng).
- **Solution (Giải pháp)**:
  1. **Debounce updates (Gộp cập nhật)**: Batch 100 updates/100ms (gộp 100 cập nhật/100ms) → 10 batches/s instead of 1000 renders/s (10 lô/giây thay vì 1000 render/giây).
  2. **Selective subscriptions (Đăng ký chọn lọc)**: Components subscribe to specific data slices (component đăng ký các phần dữ liệu cụ thể).
  3. **Virtual scrolling (Cuộn ảo)**: Render only visible items (chỉ render các mục hiển thị).
  4. **Memoization (Ghi nhớ)**: `React.memo` + `useMemo` prevent unnecessary re-renders (ngăn render lại không cần thiết).

**📊 Performance Metrics (Chỉ Số Hiệu Năng - Web Vitals):**

- **LCP (Largest Contentful Paint - Vẽ nội dung lớn nhất)**: < 2.5s (good - tốt), 2.5-4s (needs improvement - cần cải thiện), > 4s (poor - kém).
- **FID (First Input Delay - Độ trễ đầu vào đầu tiên)**: < 100ms.
- **CLS (Cumulative Layout Shift - Dịch chuyển bố cục tích lũy)**: < 0.1.
- **Tools (Công cụ)**: Lighthouse, Web Vitals library, Chrome DevTools Performance tab.

**⚠️ Common Mistakes (Lỗi Thường Gặp):**

- **Inline functions/objects (Hàm/đối tượng nội tuyến)**: Tạo new reference mỗi render (tạo tham chiếu mới mỗi lần render) → child re-render (component con render lại).
  ```jsx
  // ❌ Bad (Sai)
  <Child onClick={() => handle()} data={{ id: 1 }} />;
  // ✅ Good (Đúng)
  const handleClick = useCallback(() => handle(), []);
  const data = useMemo(() => ({ id: 1 }), []);
  <Child onClick={handleClick} data={data} />;
  ```
- **Overuse useMemo/useCallback (Lạm dụng useMemo/useCallback)**: Premature optimization (tối ưu sớm) → chỉ dùng khi đo được bottleneck (chỉ dùng khi đã đo được điểm nghẽn).
- **Missing dependencies (Thiếu phụ thuộc)**: `useEffect([])` nhưng dùng props/state inside (nhưng dùng props/state bên trong) → stale closure (closure cũ - lỗi closure).

**💡 Senior Insights (Kiến Thức Senior):**

- **Profiler**: `<Profiler>` component + DevTools → measure render time (đo thời gian render).
- **Concurrent Mode (Chế độ đồng thời)**: React 18 `useTransition` → non-urgent updates không block UI (cập nhật không khẩn cấp không chặn giao diện).
- **Bundle Budget (Ngân sách bundle)**: Set budget (500KB) → CI fail nếu vượt (CI thất bại nếu vượt quá).
- **Lighthouse CI**: Auto performance testing trong CI/CD (kiểm thử hiệu năng tự động trong CI/CD).

---

**❓ Tình Huống (Scenario):**

Bạn là Senior Frontend Developer của một Trading Platform (Nền tảng giao dịch - React + TypeScript). App hiện tại có các vấn đề (Current app has issues):

- **Initial Load (Tải ban đầu)**: 5-7s trên 3G (trên mạng 3G), bundle size 2.5MB (kích thước bundle 2.5MB)
- **Runtime Performance (Hiệu năng thời gian chạy)**:
  - Real-time updates (Cập nhật thời gian thực - WebSocket) gây re-render toàn bộ app (60+ components - 60+ component)
  - List 10,000+ orders lag khi scroll (Danh sách 10,000+ đơn hàng lag khi cuộn - FPS drop 60 → 15 - FPS giảm từ 60 xuống 15)
  - Memory leak sau 2-3 giờ sử dụng (Rò rỉ bộ nhớ sau 2-3 giờ sử dụng - memory tăng từ 50MB → 500MB)
- **User Complaints (Khiếu nại người dùng)**: App chậm (slow), lag, sometimes crash (đôi khi sập)

**Yêu cầu (Requirements):** Thiết kế và implement chiến lược tối ưu toàn diện (Design and implement comprehensive optimization strategy - từ build-time đến runtime - from build-time to runtime).

**✅ Đáp Án Chi Tiết:**

**🎯 Chiến Lược Tối Ưu 5 Tầng (5-Layer Optimization Strategy):**

```
┌──────────────────────────────────────────────────────────────┐
│           PERFORMANCE OPTIMIZATION LAYERS                     │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  1️⃣ BUILD-TIME OPTIMIZATION (Tối ưu lúc build)              │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ • Bundle Size Reduction (Giảm kích thước bundle)        │ │
│  │ • Code Splitting (Chia nhỏ code)                        │ │
│  │ • Tree-shaking (Loại bỏ dead code)                      │ │
│  │ • Lazy Loading (Tải code khi cần)                       │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                               │
│  2️⃣ NETWORK OPTIMIZATION (Tối ưu mạng)                      │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ • Resource Hints (Prefetch, Preload, Preconnect)       │ │
│  │ • HTTP/2 + Compression (Gzip, Brotli)                  │ │
│  │ • CDN + Edge Caching                                    │ │
│  │ • Service Worker + Offline Cache                       │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                               │
│  3️⃣ RENDERING OPTIMIZATION (Tối ưu render)                  │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ • React.memo + useMemo + useCallback                   │ │
│  │ • Virtual Scrolling (10K+ items)                        │ │
│  │ • Debounce + Throttle                                   │ │
│  │ • Lazy Image Loading + Responsive Images               │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                               │
│  4️⃣ STATE MANAGEMENT OPTIMIZATION (Tối ưu state)            │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ • Context Splitting (Tách context nhỏ)                  │ │
│  │ • Zustand/Redux Toolkit (Selective subscriptions)      │ │
│  │ • Immer (Immutable updates hiệu quả)                    │ │
│  │ • React Query (Server state caching)                   │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                               │
│  5️⃣ MEMORY MANAGEMENT (Tối ưu bộ nhớ)                       │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ • Cleanup useEffect (Listeners, timers, subscriptions) │ │
│  │ • AbortController (Cancel requests)                     │ │
│  │ • WeakMap/WeakSet (Temporary references)               │ │
│  │ • Memory Profiling (Chrome DevTools)                   │ │
│  └─────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

**Hoạt động:**

**📊 Performance Metrics Target (Mục Tiêu Chỉ Số Hiệu Năng):**

- Initial Load (Tải ban đầu): 5-7s → **< 2s** (70% improvement - cải thiện 70%)
- Bundle Size (Kích thước bundle): 2.5MB → **< 500KB** (80% reduction - giảm 80%)
- FPS (Frames Per Second - Khung hình mỗi giây): 15 → **60 FPS** (4x improvement - cải thiện 4 lần)
- Memory (Bộ nhớ): 500MB → **< 100MB** (80% reduction - giảm 80%)

---

**Code Example (TypeScript + React):**

```typescript
// ============================================
// 1️⃣ BUILD-TIME OPTIMIZATION (TỐI ƯU LÚC BUILD)
// ============================================
// 💡 Giải thích: Tối ưu lúc build giúp giảm kích thước file JavaScript/CSS
// mà trình duyệt cần tải về → trang web load nhanh hơn
// Ví dụ thực tế: Giống như nén quần áo vào vali trước khi đi du lịch

// 📦 A. Cấu Hình Vite (Công cụ build hiện đại - nhanh hơn Webpack)
// 💡 Vite là gì? Công cụ giúp đóng gói (bundle) code React thành file tối ưu
// File: vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { visualizer } from 'rollup-plugin-visualizer';

export default defineConfig({
  plugins: [
    react(), // Plugin hỗ trợ React (Fast Refresh, JSX transform)
    visualizer({ open: true }), // Plugin phân tích bundle size (mở browser sau build)
  ],

  build: {
    // ✅ Code Splitting: Chia nhỏ bundle thành nhiều file
    // 💡 Lý do: Browser chỉ tải file cần thiết → giảm Initial Load time
    // 📚 Ví dụ: Thay vì đọc cả cuốn sách, chỉ đọc chương cần thiết
    rollupOptions: {
      output: {
        manualChunks: {
          // 📦 Tách React libraries riêng (ít thay đổi → cache browser tốt)
          // 💡 Giải thích: React ít khi cập nhật, nên tách riêng để browser
          // lưu cache lâu dài. Khi update app, React vẫn dùng cache cũ
          // → Chỉ tải code mới của app, không tải lại React
          'react-vendor': ['react', 'react-dom', 'react-router-dom'],

          // 📊 Tách chart libraries (rất nặng - 500KB+)
          // 💡 Giải thích: Thư viện vẽ biểu đồ rất nặng, chỉ load khi cần
          // 📈 Ví dụ: User vào trang Dashboard (không có chart) → không tải
          // User vào trang Analytics (có chart) → mới tải chart library
          'chart-vendor': ['recharts', 'lightweight-charts'],

          // 🛠️ Tách utilities (công cụ hỗ trợ) thành bundle riêng
          // 💡 lodash-es: Thư viện helper functions (map, filter, reduce...)
          // 💡 date-fns: Xử lý ngày tháng (format, parse...)
          // 💡 axios: Gọi API
          utils: ['lodash-es', 'date-fns', 'axios'],
        },
      },
    },

    // ✅ Minify: Nén code (xóa whitespace, rút ngắn tên biến)
    // Terser: Tool minify mạnh nhất hiện tại
    minify: 'terser',
    terserOptions: {
      compress: {
        drop_console: true, // Xóa tất cả console.log trong production
        drop_debugger: true, // Xóa debugger statements
      },
    },

    // ✅ Source Maps: 'hidden' = có source maps nhưng không expose
    // Lý do: Debug được lỗi production nhưng không lộ source code
    sourcemap: 'hidden',

    // ✅ Cảnh báo nếu chunk > 500KB (quá lớn → load chậm)
    chunkSizeWarningLimit: 500,
  },

  // ✅ Tree-shaking: Loại bỏ code không dùng đến
  // VD: import { map } from 'lodash' → chỉ bundle hàm map, bỏ 99% lodash
  optimizeDeps: {
    include: ['react', 'react-dom'], // Pre-bundle các deps quan trọng
  },
});

// 📦 B. Lazy Loading Routes (Tải Trang Theo Route)
// 💡 Giải thích đơn giản: Thay vì load toàn bộ app lúc đầu, chỉ load trang user cần
// 📚 Ví dụ thực tế: Giống như Netflix - chỉ load phim bạn chọn xem,
// không load hết tất cả phim trong thư viện ngay từ đầu
import { lazy, Suspense } from 'react';
import { Routes, Route } from 'react-router-dom';

// ✅ Lazy load pages: Tạo dynamic import → tạo separate chunk cho mỗi page
// VD: User vào "/" → chỉ tải Dashboard.js, KHÔNG tải Trading.js, Portfolio.js
// Kết quả: Initial bundle giảm từ 2.5MB → 300KB
const Dashboard = lazy(() => import('./pages/Dashboard')); // Tải khi vào "/"
const Trading = lazy(() => import('./pages/Trading')); // Tải khi vào "/trading"
const Portfolio = lazy(() => import('./pages/Portfolio')); // Tải khi vào "/portfolio"
const Analytics = lazy(() => import('./pages/Analytics')); // Tải khi vào "/analytics"

// Skeleton Loader: UI hiển thị trong lúc chờ page load
// Tốt hơn là màn hình trắng (UX tốt hơn)
const PageLoader = () => (
  <div className="flex items-center justify-center h-screen">
    {/* Spinner animation quay tròn */}
    <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
    <span className="ml-3">Đang tải...</span>
  </div>
);

export default function App() {
  return (
    // Suspense: Bắt loading state của lazy components
    // fallback: Component hiển thị trong lúc chờ load
    <Suspense fallback={<PageLoader />}>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/trading" element={<Trading />} />
        <Route path="/portfolio" element={<Portfolio />} />
        <Route path="/analytics" element={<Analytics />} />
      </Routes>
    </Suspense>
  );
}

// ============================================
// 3️⃣ RENDERING OPTIMIZATION (TỐI ƯU RENDER)
// ============================================

// 🎨 A. React.memo + useMemo + useCallback (Bộ 3 tối ưu render)
import { memo, useMemo, useCallback } from 'react';

// ✅ React.memo: Bọc component để SKIP re-render nếu props không đổi
// 💡 Hoạt động: React so sánh props cũ vs mới (shallow comparison)
// → Nếu giống nhau → KHÔNG re-render → Tăng performance
// 📚 Ví dụ thực tế: Giống như Excel - chỉ tính lại cell khi data thay đổi,
// không tính lại tất cả cells mỗi lần bạn nhập liệu
const OrderItem = memo(function OrderItem({ order, onDelete }) {
  console.log('OrderItem render'); // Log này CHỈ chạy khi props thay đổi
  return (
    <div>
      <span>{order.symbol}</span>
      <button onClick={() => onDelete(order.id)}>Xóa</button>
    </div>
  );
});
// Kết quả: 1000 orders → parent re-render → KHÔNG re-render 1000 OrderItem

// Component cha
function OrderList({ orders }) {
  // ✅ useCallback: Lưu lại function reference (tham chiếu hàm)
  // 🔴 Vấn đề: Mỗi lần render → tạo function mới → OrderItem re-render vì onDelete khác
  // 💡 Giải thích: Trong JavaScript, mỗi lần tạo function mới = địa chỉ bộ nhớ khác
  // → React nghĩ props thay đổi → re-render không cần thiết
  // 🟢 Giải pháp: useCallback lưu function → địa chỉ giống nhau → OrderItem KHÔNG re-render
  // 📚 Ví dụ: Giống như lưu số điện thoại - gọi cùng 1 số, không tạo số mới mỗi lần gọi
  const handleDelete = useCallback((id: string) => {
    console.log('Xóa order:', id);
    // Call API xóa order...
  }, []); // [] = function không đổi, tạo 1 lần duy nhất

  // ✅ useMemo: Cache (lưu trữ) kết quả tính toán nặng
  // 🔴 Vấn đề: Mỗi render → sort lại 10,000 orders → chậm (có thể mất 100-500ms)
  // 💡 Giải thích: Sort 10,000 items giống như sắp xếp 10,000 tờ giấy - mất thời gian!
  // 🟢 Giải pháp: useMemo lưu kết quả đã sort → chỉ sort lại KHI orders thay đổi
  // 📚 Ví dụ: Giống như lưu kết quả tính toán vào bảng - chỉ tính lại khi số liệu đầu vào thay đổi
  const sortedOrders = useMemo(() => {
    console.log('Đang sort orders...'); // Chỉ log khi orders thay đổi
    return orders.sort((a, b) => b.timestamp - a.timestamp); // Sort theo thời gian mới nhất
  }, [orders]); // [orders] = chỉ tính lại khi orders thay đổi

  return (
    <div>
      {sortedOrders.map((order) => (
        <OrderItem
          key={order.id} // key giúp React track item nào thay đổi
          order={order}
          onDelete={handleDelete} // Reference giống nhau → memo hoạt động
        />
      ))}
    </div>
  );
}
// Kết quả: Re-render chỉ mất 20ms thay vì 500ms

// 🎨 B. Virtual Scrolling (Cuộn Ảo cho 10K+ items)
// 💡 Giải thích đơn giản: Thay vì render 10,000 items → chỉ render items hiển thị trên màn hình
// 📊 Ví dụ cụ thể: Màn hình cao 600px, mỗi item 50px → chỉ render 12 items (600/50)
// 📚 Ví dụ thực tế: Giống như xem danh sách contact trong điện thoại -
// chỉ hiển thị tên bạn đang nhìn thấy, không load hết 1000 contacts cùng lúc
import { FixedSizeList as List } from 'react-window';

interface Order {
  id: string;
  symbol: string;
  quantity: number;
  price: number;
}

function GoodOrderList({ orders }: { orders: Order[] }) {
  // Row component: Render 1 order item
  // Nhận index + style từ react-window (style có position: absolute + top)
  const Row = ({ index, style }) => {
    const order = orders[index]; // Lấy order theo index
    return (
      // style chứa position absolute + top để đặt item đúng vị trí
      <div style={style} className="flex items-center border-b px-4">
        <span className="w-20 font-bold">{order.symbol}</span>
        <span className="w-32">
          {order.quantity} @ ${order.price}
        </span>
      </div>
    );
  };

  return (
    // FixedSizeList: Component virtual scrolling
    // Hoạt động: Tính toán item nào trong viewport → chỉ render items đó
    <List
      height={600} // Chiều cao container (px)
      itemCount={orders.length} // Tổng số items (10,000)
      itemSize={50} // Chiều cao mỗi item (px)
      width="100%" // Chiều rộng container
    >
      {Row} {/* Render function cho mỗi item */}
    </List>
  );
}
// Kết quả:
// ❌ Không dùng virtual scroll: Render 10,000 DOM nodes → lag, FPS 15
// ✅ Dùng virtual scroll: Chỉ render ~12 DOM nodes → mượt, FPS 60

// ============================================
// 4️⃣ STATE MANAGEMENT OPTIMIZATION (TỐI ƯU QUẢN LÝ STATE)
// ============================================

// 🏪 Zustand: Thư viện quản lý state (trạng thái) nhẹ, nhanh hơn Redux
// 💡 State là gì? Dữ liệu của app (VD: danh sách orders, giá cổ phiếu...)
// ✨ Ưu điểm của Zustand:
// - Không cần Provider wrapper (đơn giản hơn Context API)
// - Selective subscription: Component chỉ re-render khi state nó dùng thay đổi
// - API đơn giản, ít code boilerplate (code dài dòng không cần thiết)
// 📚 Ví dụ: Giống như đăng ký nhận thông báo - chỉ nhận tin về chủ đề quan tâm
import create from 'zustand';

interface Order {
  id: string;
  symbol: string;
  quantity: number;
  price: number;
}

interface TradingStore {
  orders: Order[]; // Danh sách orders
  prices: Record<string, number>; // Giá real-time
  addOrder: (order: Order) => void;
  updatePrice: (symbol: string, price: number) => void;
}

// Tạo store: Hàm nhận set function để update state
const useTradingStore = create<TradingStore>((set) => ({
  orders: [],
  prices: {},

  // Action thêm order
  addOrder: (order) =>
    set((state) => ({
      orders: [...state.orders, order], // Immutable update
    })),

  // Action update giá
  updatePrice: (symbol, price) =>
    set((state) => ({
      prices: { ...state.prices, [symbol]: price },
    })),
}));

// ✅ Selective Subscription (Đăng ký chọn lọc): Chỉ subscribe phần state cần thiết
// 💡 Giải thích: Component này CHỈ re-render khi orders thay đổi
// 🎯 Lợi ích: Khi prices update → component KHÔNG re-render (vì không subscribe prices)
// 📚 Ví dụ thực tế: Giống như đăng ký kênh YouTube - chỉ nhận thông báo từ kênh đã đăng ký,
// không nhận từ tất cả kênh trên YouTube
function OrderList() {
  // Selector function: state => state.orders
  // Zustand compare selector result → chỉ re-render nếu orders thay đổi
  const orders = useTradingStore((state) => state.orders);

  return (
    <div>
      {orders.map((order) => (
        <OrderItem key={order.id} order={order} />
      ))}
    </div>
  );
}

// Component này CHỈ re-render khi prices thay đổi
function PriceDisplay({ symbol }: { symbol: string }) {
  // Subscribe chỉ 1 giá cụ thể
  const price = useTradingStore((state) => state.prices[symbol]);

  return (
    <span>
      Giá {symbol}: ${price}
    </span>
  );
}
// Kết quả: WebSocket update 100 giá/giây → chỉ 100 components nhỏ re-render
// Thay vì toàn bộ app re-render (như Context API)

// ============================================
// 5️⃣ MEMORY MANAGEMENT (QUẢN LÝ BỘ NHỚ)
// ============================================
// 💡 Giải thích: Quản lý bộ nhớ giúp tránh memory leak (rò rỉ bộ nhớ)
// 🔴 Memory leak là gì? App chiếm dụng bộ nhớ không cần thiết → ngày càng chậm
// 📚 Ví dụ thực tế: Giống như không tắt vòi nước sau khi dùng → nước tràn ra

// 🧹 Cleanup useEffect: Dọn dẹp tài nguyên khi component unmount (bị gỡ bỏ)
// 🔴 Vấn đề: Không cleanup → memory leak (bộ nhớ tăng dần 50MB → 500MB)
// 💡 Unmount là gì? Khi user rời khỏi trang, component bị gỡ khỏi màn hình

import { useEffect, useState, useRef } from 'react';

function TradingChart() {
  const [chartData, setChartData] = useState([]);

  useEffect(() => {
    // Tạo WebSocket connection
    const ws = new WebSocket('wss://api.trading.com');

    // Lắng nghe data từ server
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setChartData((prev) => [...prev, data]); // Update chart data
    };

    ws.onerror = (error) => {
      console.error('WebSocket error:', error);
    };

    // ✅ QUAN TRỌNG: Cleanup function (Hàm dọn dẹp)
    // 💡 Khi chạy? Khi component unmount hoặc dependencies thay đổi
    // 📚 Ví dụ: User chuyển từ trang Chart sang trang Dashboard
    return () => {
      console.log('Dọn dẹp WebSocket...');

      // 🔌 Đóng kết nối WebSocket
      // 💡 Giải thích: Giống như ngắt kết nối điện thoại sau khi gọi xong
      if (
        ws.readyState === WebSocket.OPEN ||
        ws.readyState === WebSocket.CONNECTING
      ) {
        ws.close(); // Ngắt kết nối → giải phóng bộ nhớ
      }

      // Nếu không cleanup:
      // - WebSocket vẫn mở → nhận data → update state của component đã unmount
      // - Gây memory leak + warning "Can't perform state update on unmounted component"
    };
  }, []); // [] = chỉ chạy 1 lần khi mount

  return <div>Biểu đồ trading...</div>;
}

// 🧹 B. Cancel API Requests (Hủy yêu cầu API) với AbortController
// 💡 Tại sao cần cancel? User chuyển trang nhanh → API request cũ không cần nữa
// 🎯 Lợi ích: Tiết kiệm băng thông, tránh memory leak
function OrderHistory() {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    // 🛑 Tạo AbortController để hủy request khi cần
    // 💡 Giống như nút "Cancel" khi download file
    const abortController = new AbortController();
    const signal = abortController.signal;

    // Fetch data với signal
    fetch('/api/orders?limit=1000', { signal })
      .then((res) => res.json())
      .then((data) => setOrders(data))
      .catch((error) => {
        // AbortError = request bị cancel (KHÔNG phải lỗi thật)
        if (error.name === 'AbortError') {
          console.log('Request đã được cancel');
        } else {
          console.error('Lỗi:', error);
        }
      });

    // ✅ Cleanup: Cancel request khi unmount
    return () => {
      console.log('Cancel API request...');
      abortController.abort(); // Cancel request đang chạy

      // Tại sao cần cancel?
      // - User chuyển trang nhanh → request cũ vẫn chạy → waste bandwidth
      // - Request trả về → update state unmounted component → memory leak
    };
  }, []);

  return <div>Lịch sử orders...</div>;
}

// 🧹 C. Clear Timers & Intervals (Xóa bộ đếm thời gian)
// 💡 Timer/Interval là gì? Hàm tự động chạy sau một khoảng thời gian
// 📚 Ví dụ: Báo thức đổ chuông mỗi 5 phút để nhắc uống nước
function PriceRefresh() {
  const [price, setPrice] = useState(0);

  useEffect(() => {
    // ⏰ Refresh (làm mới) giá mỗi 5 giây
    // 💡 setInterval: Chạy hàm lặp lại sau mỗi khoảng thời gian
    const intervalId = setInterval(() => {
      fetch('/api/price')
        .then((res) => res.json())
        .then((data) => setPrice(data.price));
    }, 5000);

    // ✅ Cleanup: Clear interval khi unmount
    return () => {
      console.log('Clear interval...');
      clearInterval(intervalId); // Dừng interval

      // Nếu không clear:
      // - Interval vẫn chạy sau unmount → call API → update state
      // - Memory leak + nhiều intervals chạy song song
    };
  }, []);

  return <div>Giá hiện tại: ${price}</div>;
}

// 🧹 D. Remove Event Listeners (Xóa bộ lắng nghe sự kiện)
// 💡 Event Listener là gì? Hàm lắng nghe sự kiện như click, scroll, resize...
// 📚 Ví dụ: Giống như đặt chuông cửa - cần gỡ chuông khi chuyển nhà
function ResizableChart() {
  const chartRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // 📐 Handler (hàm xử lý) cho sự kiện window resize (thay đổi kích thước cửa sổ)
    // 💡 Khi nào chạy? Mỗi khi user phóng to/thu nhỏ cửa sổ browser
    const handleResize = () => {
      if (chartRef.current) {
        // Resize chart khi window thay đổi
        console.log('Resize chart to:', window.innerWidth);
      }
    };

    // Đăng ký event listener
    window.addEventListener('resize', handleResize);

    // ✅ Cleanup: Remove event listener
    return () => {
      console.log('Remove resize listener...');
      window.removeEventListener('resize', handleResize);

      // Nếu không remove:
      // - Listener vẫn tồn tại sau unmount
      // - Nhiều components → nhiều listeners → performance giảm
      // - Memory leak (function + closure không được garbage collected)
    };
  }, []);

  return <div ref={chartRef}>Chart có thể resize</div>;
}
// Kết quả cleanup đúng cách: Memory ổn định ~80MB thay vì leak đến 500MB
```

**🎯 Kết Quả Sau Optimization (Results After Optimization):**

```
┌────────────────────────────────────────────────────────────────┐
│           PERFORMANCE METRICS - BEFORE vs AFTER                 │
│           (CHỈ SỐ HIỆU NĂNG - TRƯỚC vs SAU)                     │
├────────────────────────────────────────────────────────────────┤
│  Metric (Chỉ số)              │ Before (Trước)      │ After (Sau)       │ Improvement (Cải thiện) │
│ ─────────────────────┼─────────────┼─────────────┼──────────── │
│  Initial Load (Tải ban đầu)        │ 5-7s        │ 1.5-2s      │ 70% faster (nhanh hơn 70%)  │
│  Bundle Size (Kích thước bundle)         │ 2.5MB       │ 450KB       │ 82% smaller (nhỏ hơn 82%) │
│  FCP (First Paint - Vẽ đầu tiên)   │ 3s          │ 0.8s        │ 73% faster (nhanh hơn 73%)  │
│  TTI (Interactive - Tương tác)   │ 6s          │ 2s          │ 67% faster (nhanh hơn 67%)  │
│  Scroll FPS (FPS cuộn)          │ 15 FPS      │ 60 FPS      │ 4x better (tốt hơn 4 lần)   │
│  Memory Usage (Sử dụng bộ nhớ)        │ 500MB       │ 80MB        │ 84% less (ít hơn 84%)    │
│  Re-renders/sec (Render lại/giây)      │ 200+        │ 10-20       │ 90% less (ít hơn 90%)    │
└────────────────────────────────────────────────────────────────┘
```

**Best Practices (Thực Hành Tốt Nhất):**

1. **Measure First (Đo lường trước)**: Dùng Lighthouse, Chrome DevTools Performance (Use Lighthouse, Chrome DevTools Performance)
2. **Bundle Analysis (Phân tích bundle)**: `npm run build -- --analyze`
3. **Code Splitting (Chia nhỏ code)**: Route-level + Component-level (Cấp route + cấp component)
4. **State Management (Quản lý trạng thái)**: Context cho static (Context cho tĩnh), Zustand cho complex state (Zustand cho trạng thái phức tạp)
5. **Memory Management (Quản lý bộ nhớ)**: Always cleanup useEffect (Luôn dọn dẹp useEffect)

**Common Mistakes (Lỗi Thường Gặp):**

```typescript
// ❌ LỖI 1: Inline functions trong render (Hàm nội tuyến trong render)
// Vấn đề (Problem): Mỗi render tạo function mới (create new function each render) → child component re-render không cần thiết (unnecessary child re-render)
{
  items.map((item) => (
    <Item
      key={item.id}
      onClick={() => handleClick(item)} // ❌ Function mới mỗi lần render (new function each render)
    />
  ));
}

// ✅ CÁCH SỬA (FIX): Dùng useCallback để memoize function (use useCallback to memoize function)
const handleClick = useCallback((item) => {
  console.log('Clicked:', item);
  // Xử lý logic... (Handle logic...)
}, []); // Function reference không đổi (function reference unchanged)

{
  items.map((item) => (
    <Item
      key={item.id}
      onClick={handleClick} // ✅ Reference giống nhau (same reference) → không re-render (no re-render)
      item={item}
    />
  ));
}

// ❌ LỖI 2: Không cleanup useEffect → Memory Leak (Rò rỉ bộ nhớ)
useEffect(() => {
  const ws = new WebSocket('wss://api.example.com');
  ws.onmessage = (e) => setData(e.data);
  // ❌ Thiếu cleanup (missing cleanup) → WebSocket không đóng (WebSocket not closed) → memory leak
}, []);

// ✅ CÁCH SỬA: Luôn cleanup resources (Always cleanup resources)
useEffect(() => {
  const ws = new WebSocket('wss://api.example.com');
  ws.onmessage = (e) => setData(e.data);

  return () => {
    ws.close(); // ✅ Đóng WebSocket khi unmount (Close WebSocket on unmount)
  };
}, []);

// ❌ LỖI 3: Quên dependencies trong useMemo/useCallback (Missing dependencies in useMemo/useCallback)
const sortedData = useMemo(() => {
  return data.sort((a, b) => a[sortBy] - b[sortBy]);
}, []); // ❌ Thiếu [data, sortBy] (missing [data, sortBy]) → không update khi data/sortBy thay đổi (not update when data/sortBy changes)

// ✅ CÁCH SỬA: Khai báo đầy đủ dependencies (Declare full dependencies)
const sortedData = useMemo(() => {
  return data.sort((a, b) => a[sortBy] - b[sortBy]);
}, [data, sortBy]); // ✅ Tính lại khi data hoặc sortBy thay đổi (recalculate when data or sortBy changes)

// ❌ LỖI 4: Render toàn bộ list lớn (Render entire large list)
function OrderList({ orders }) {
  return (
    <div>
      {orders.map((order) => (
        <OrderRow key={order.id} order={order} />
      ))}
    </div>
  );
} // ❌ 10,000 items → 10,000 DOM nodes → lag

// ✅ CÁCH SỬA: Dùng virtual scrolling (Use virtual scrolling)
import { FixedSizeList } from 'react-window';

function OrderList({ orders }) {
  return (
    <FixedSizeList height={600} itemCount={orders.length} itemSize={50}>
      {({ index, style }) => (
        <div style={style}>
          <OrderRow order={orders[index]} />
        </div>
      )}
    </FixedSizeList>
  );
} // ✅ Chỉ render ~12 items (only render ~12 items) → mượt mà (smooth)
```

---

## **🔬 DEEP DIVE: Hiểu Sâu Cơ Chế React (Deep Dive: Understanding React Mechanisms)**

### **⚛️ Phần 1: React Reconciliation - Thuật Toán Đối Chiếu (Part 1: React Reconciliation - Diffing Algorithm)**

```typescript
/**
 * 🧠 REACT RECONCILIATION - Cách React quyết định render gì
 * (REACT RECONCILIATION - How React decides what to render)
 *
 * Khi state/props thay đổi, React KHÔNG re-render toàn bộ app!
 * (When state/props change, React does NOT re-render entire app!)
 * Thay vào đó, React dùng thuật toán "Reconciliation" (Diffing) để:
 * (Instead, React uses "Reconciliation" (Diffing) algorithm to:)
 * 1. So sánh Virtual DOM cũ vs mới (Compare old vs new Virtual DOM)
 * 2. Tìm ra sự khác biệt (diff) (Find differences - diff)
 * 3. Chỉ update những phần khác biệt vào Real DOM (Only update different parts to Real DOM)
 *
 * 📊 Complexity (Độ phức tạp): O(n) thay vì O(n^3) (instead of O(n^3) - thuật toán diff chuẩn - standard diff algorithm)
 */

// 🌳 VIRTUAL DOM TREE EXAMPLE (Ví dụ cây Virtual DOM):
// Đây là cách React biểu diễn UI trong bộ nhớ (JavaScript objects)
// (This is how React represents UI in memory - JavaScript objects)

const virtualDOM_Before = {
  type: 'div',
  props: { className: 'container' },
  children: [
    {
      type: 'h1',
      props: { className: 'title' },
      children: ['Hello'], // 💡 Text node (Nút văn bản)
    },
    {
      type: 'ul',
      props: {},
      children: [
        { type: 'li', props: { key: '1' }, children: ['Item 1'] },
        { type: 'li', props: { key: '2' }, children: ['Item 2'] },
      ],
    },
  ],
};

// User click button → state thay đổi → React tạo Virtual DOM mới:
// (User click button → state changes → React creates new Virtual DOM:)
const virtualDOM_After = {
  type: 'div',
  props: { className: 'container' },
  children: [
    {
      type: 'h1',
      props: { className: 'title active' }, // 🔄 className changed! (className đã thay đổi!)
      children: ['Hello World'], // 🔄 Text changed! (Văn bản đã thay đổi!)
    },
    {
      type: 'ul',
      props: {},
      children: [
        { type: 'li', props: { key: '1' }, children: ['Item 1'] }, // ✅ Không đổi (Unchanged)
        { type: 'li', props: { key: '2' }, children: ['Item 2'] }, // ✅ Không đổi (Unchanged)
        { type: 'li', props: { key: '3' }, children: ['Item 3'] }, // ➕ Mới thêm (Newly added)
      ],
    },
  ],
};

/**
 * 🔍 DIFFING ALGORITHM - Thuật toán so sánh (Diffing Algorithm - Comparison Algorithm):
 *
 * React duyệt 2 trees song song (old vs new):
 * (React traverses 2 trees in parallel - old vs new:)
 */

function diff(oldNode, newNode) {
  // RULE 1 (Quy tắc 1): Nếu type khác nhau → XOÁ cũ, TẠO mới
  // (If type different → DELETE old, CREATE new)
  if (oldNode.type !== newNode.type) {
    // VD (Example): <div> → <span> = Destroy <div> + Create <span>
    return { action: 'REPLACE', node: newNode };
    // 💡 XOÁ toàn bộ subtree cũ, tạo mới hoàn toàn
    // (Delete entire old subtree, create completely new)
    // 💥 Tốn kém! Nên tránh thay đổi type
    // (Expensive! Should avoid changing type)
  }

  // RULE 2 (Quy tắc 2): Nếu type giống nhau → SO SÁNH PROPS
  // (If type same → COMPARE PROPS)
  if (oldNode.type === newNode.type) {
    const propsChanged = compareProps(oldNode.props, newNode.props);

    if (propsChanged) {
      // VD (Example): className="title" → className="title active"
      return { action: 'UPDATE_PROPS', changes: propsChanged };
      // 💡 CHỈ update attributes, GIỮ nguyên DOM node
      // (Only update attributes, KEEP DOM node unchanged)
      // ✅ Hiệu quả! Chỉ tốn 1 DOM operation
      // (Efficient! Only costs 1 DOM operation)
    }
  }

  // RULE 3 (Quy tắc 3): So sánh CHILDREN (recursive - đệ quy)
  // (Compare CHILDREN - recursive)
  const childrenChanges = diffChildren(oldNode.children, newNode.children);
  return { action: 'UPDATE_CHILDREN', changes: childrenChanges };
}

function compareProps(oldProps, newProps) {
  const changes = {};

  // Tìm props thay đổi
  for (const key in newProps) {
    if (oldProps[key] !== newProps[key]) {
      changes[key] = newProps[key];
      // VD: className changed → changes = { className: 'title active' }
    }
  }

  // Tìm props bị xoá
  for (const key in oldProps) {
    if (!(key in newProps)) {
      changes[key] = null; // Mark for removal
    }
  }

  return Object.keys(changes).length > 0 ? changes : null;
}

/**
 * 🔑 KEY PROP - Tại sao KEY quan trọng?
 * (KEY PROP - Why is KEY important?)
 *
 * Khi diff children list, React cần biết:
 * (When diffing children list, React needs to know:)
 * - Item nào giữ nguyên? (Which items remain unchanged?)
 * - Item nào mới thêm? (Which items are newly added?)
 * - Item nào bị xoá? (Which items are deleted?)
 * - Item nào thay đổi vị trí? (Which items changed position?)
 */

// ❌ KHÔNG CÓ KEY - React không biết item nào là item nào:
// (NO KEY - React doesn't know which item is which:)
const oldList = [
  <li>Apple</li>, // index 0
  <li>Banana</li>, // index 1
  <li>Cherry</li>, // index 2
];

const newList = [
  <li>Avocado</li>, // index 0 - 💥 React nghĩ "Apple" đổi thành "Avocado" (React thinks "Apple" changed to "Avocado")
  <li>Apple</li>, // index 1 - 💥 React nghĩ "Banana" đổi thành "Apple" (React thinks "Banana" changed to "Apple")
  <li>Banana</li>, // index 2 - 💥 React nghĩ "Cherry" đổi thành "Banana" (React thinks "Cherry" changed to "Banana")
  <li>Cherry</li>, // index 3 - 💥 React tạo mới "Cherry" (React creates new "Cherry")
];
// 💥 Kết quả (Result): UPDATE 3 items + CREATE 1 item = 4 DOM operations!
// 💥 Thực tế chỉ cần (Actually only need): CREATE 1 item (Avocado) = 1 operation

// ✅ CÓ KEY - React biết chính xác item nào là item nào:
// (WITH KEY - React knows exactly which item is which:)
const oldListWithKey = [
  <li key="apple">Apple</li>,
  <li key="banana">Banana</li>,
  <li key="cherry">Cherry</li>,
];

const newListWithKey = [
  <li key="avocado">Avocado</li>, // ➕ Mới - CREATE (New - CREATE)
  <li key="apple">Apple</li>, // ✅ Giữ nguyên - MOVE (Unchanged - MOVE)
  <li key="banana">Banana</li>, // ✅ Giữ nguyên - MOVE (Unchanged - MOVE)
  <li key="cherry">Cherry</li>, // ✅ Giữ nguyên - MOVE (Unchanged - MOVE)
];
// ✅ Kết quả (Result): CREATE 1 item + MOVE 3 items = Hiệu quả hơn nhiều! (Much more efficient!)
// 💡 DOM MOVE rẻ hơn DOM UPDATE (DOM MOVE cheaper than DOM UPDATE - không cần re-render content - no need to re-render content)

/**
 * ⚠️ KEY ANTI-PATTERNS - Các lỗi thường gặp:
 * (KEY ANTI-PATTERNS - Common mistakes:)
 */

// ❌ LỖI 1 (MISTAKE 1): Dùng index làm key (Use index as key)
items.map((item, index) => (
  <li key={index}>{item.name}</li> // 💥 Khi items thay đổi thứ tự = bug! (When items change order = bug!)
));
// Tại sao sai? (Why wrong?)
// - Thêm item mới ở đầu list → tất cả index thay đổi (Add new item at list start → all indexes change)
// - React nghĩ tất cả items thay đổi → re-render tất cả! (React thinks all items changed → re-render all!)
// - Input focus/state bị mất vì DOM node bị thay thế (Input focus/state lost because DOM node replaced)

// ❌ LỖI 2 (MISTAKE 2): Dùng random/generated key (Use random/generated key)
items.map((item) => (
  <li key={Math.random()}>{item.name}</li> // 💥 Key khác nhau mỗi render! (Key different each render!)
));
// Tại sao sai? (Why wrong?)
// - Mỗi render = key mới → React nghĩ là item mới (Each render = new key → React thinks it's new item)
// - Xóa cũ + tạo mới tất cả → mất state, performance tồi (Delete old + create new all → lose state, poor performance)

// ✅ ĐÚNG (CORRECT): Dùng stable, unique ID từ data (Use stable, unique ID from data)
items.map((item) => (
  <li key={item.id}>{item.name}</li> // ✅ ID từ database = stable + unique (ID from database = stable + unique)
));
// Tại sao đúng? (Why correct?)
// - item.id không thay đổi (stable - ổn định) (item.id doesn't change - stable)
// - Mỗi item có ID khác nhau (unique - duy nhất) (Each item has different ID - unique)
// - React track đúng item qua các lần render (React tracks correct item across renders)
```

---

### **📊 Phần 2: React.memo Deep Dive - Hiểu Rõ Memoization (Part 2: React.memo Deep Dive - Understanding Memoization)**

```typescript
/**
 * 🧠 REACT.MEMO - Shallow Comparison Explained
 * (REACT.MEMO - Giải thích so sánh nông)
 *
 * React.memo so sánh props bằng "shallow comparison":
 * (React.memo compares props using "shallow comparison":)
 * - Primitive values (Giá trị nguyên thủy): So sánh giá trị (===) (Compare values)
 * - Objects/Arrays (Đối tượng/Mảng): So sánh reference (===) (Compare references)
 */

// 🔍 Shallow Comparison Implementation (Triển khai so sánh nông):
function shallowEqual(objA: any, objB: any): boolean {
  // 1. Nếu cùng reference → giống nhau (If same reference → same)
  if (objA === objB) return true;

  // 2. Nếu không phải object → khác nhau (If not object → different)
  if (typeof objA !== 'object' || typeof objB !== 'object') return false;

  // 3. So sánh số lượng keys (Compare number of keys)
  const keysA = Object.keys(objA);
  const keysB = Object.keys(objB);
  if (keysA.length !== keysB.length) return false;

  // 4. So sánh từng key (chỉ 1 level, không deep)
  // (Compare each key - only 1 level, not deep)
  for (const key of keysA) {
    if (objA[key] !== objB[key]) return false;
    // 💡 Dùng !== = so sánh reference cho nested objects
    // (Use !== = compare reference for nested objects)
  }

  return true;
}

// 📊 VÍ DỤ (EXAMPLES): Props comparison examples (Ví dụ so sánh props)

// Example 1 (Ví dụ 1): Primitive props (Props nguyên thủy)
const props1 = { name: 'John', age: 30 };
const props2 = { name: 'John', age: 30 };
shallowEqual(props1, props2); // true - Values giống nhau (Values same)
// → React.memo SKIPs re-render ✅ (Bỏ qua render lại)

// Example 2 (Ví dụ 2): Different primitive (Nguyên thủy khác)
const props3 = { name: 'John', age: 31 }; // age changed (age đã thay đổi)
shallowEqual(props1, props3); // false
// → React.memo RE-RENDERS 🔄 (Render lại)

// Example 3 (Ví dụ 3): Nested object (reference) (Đối tượng lồng nhau - tham chiếu)
const props4 = { user: { name: 'John' } };
const props5 = { user: { name: 'John' } }; // New object! (Đối tượng mới!)
shallowEqual(props4, props5); // false - Khác reference! (Different reference!)
// 💡 Dù content giống nhau nhưng { } = new object = khác reference
// (Even though content same, { } = new object = different reference)
// → React.memo RE-RENDERS 🔄 (Render lại)

// Example 4 (Ví dụ 4): Same reference (Cùng tham chiếu)
const userObj = { name: 'John' };
const props6 = { user: userObj };
const props7 = { user: userObj }; // Same reference! (Cùng tham chiếu!)
shallowEqual(props6, props7); // true - Cùng reference (Same reference)
// → React.memo SKIPs re-render ✅ (Bỏ qua render lại)

/**
 * ⚡ TỐI ƯU VỚI USEMEMO - Giữ reference ổn định
 * (OPTIMIZE WITH USEMEMO - Keep stable reference)
 */

function ParentBad() {
  const [count, setCount] = useState(0);

  // ❌ Mỗi render = tạo object mới (Each render = create new object)
  const config = { theme: 'dark', lang: 'vi' };
  // 💡 Mỗi lần count thay đổi → ParentBad re-render → config mới
  // (Each time count changes → ParentBad re-render → new config)

  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Count: {count}</button>
      <ChildMemo config={config} />
      {/* 💥 config luôn khác reference → ChildMemo luôn re-render! */}
      {/* (config always different reference → ChildMemo always re-render!) */}
    </div>
  );
}

function ParentGood() {
  const [count, setCount] = useState(0);

  // ✅ useMemo lưu lại object, chỉ tạo mới khi dependencies thay đổi
  // (useMemo saves object, only create new when dependencies change)
  const config = useMemo(
    () => ({ theme: 'dark', lang: 'vi' }),
    [] // Empty deps = tạo 1 lần duy nhất (Empty deps = create once only)
  );
  // 💡 count thay đổi → config GIỮ NGUYÊN reference cũ
  // (count changes → config KEEPS old reference)

  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Count: {count}</button>
      <ChildMemo config={config} />
      {/* ✅ config cùng reference → ChildMemo SKIPs re-render! */}
      {/* (config same reference → ChildMemo SKIPs re-render!) */}
    </div>
  );
}

const ChildMemo = memo(function Child({ config }) {
  console.log('Child render'); // Chỉ log khi config thay đổi
  return <div>Theme: {config.theme}</div>;
});

/**
 * 📊 USECALLBACK - Memoize functions
 * (USECALLBACK - Ghi nhớ hàm)
 */

function ParentWithCallbacks() {
  const [count, setCount] = useState(0);
  const [items, setItems] = useState([1, 2, 3]);

  // ❌ Mỗi render = function mới (Each render = new function)
  const handleClickBad = () => {
    console.log('Clicked');
  };

  // ✅ useCallback lưu function reference (useCallback saves function reference)
  const handleClickGood = useCallback(() => {
    console.log('Clicked');
  }, []); // [] = function không đổi ([] = function unchanged)

  // 💡 Function với dependencies (Function with dependencies)
  const handleDelete = useCallback((id: number) => {
    setItems((items) => items.filter((item) => item !== id));
    // 💡 Dùng functional update → không cần items trong deps
    // (Use functional update → don't need items in deps)
  }, []); // [] vì dùng functional update ([] because using functional update)

  // ⚠️ Nếu dùng items trực tiếp (If use items directly):
  const handleDeleteBad = useCallback(
    (id: number) => {
      setItems(items.filter((item) => item !== id));
      // 💡 items = closure → PHẢI thêm vào deps
      // (items = closure → MUST add to deps)
    },
    [items]
  ); // items thay đổi → function mới → child re-render
  // (items changes → new function → child re-render)

  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Count: {count}</button>
      <ItemList items={items} onDelete={handleDelete} />
    </div>
  );
}

const ItemList = memo(function ItemList({ items, onDelete }) {
  console.log('ItemList render');
  return (
    <ul>
      {items.map((item) => (
        <li key={item}>
          {item}
          <button onClick={() => onDelete(item)}>Delete</button>
        </li>
      ))}
    </ul>
  );
});

/**
 * 🪤 KHI NÀO DÙNG MEMO/USEMEMO/USECALLBACK?
 * (WHEN TO USE MEMO/USEMEMO/USECALLBACK?)
 *
 * ✅ NÊN DÙNG KHI (SHOULD USE WHEN):
 * 1. Component render chậm (> 100ms) (Component renders slowly - > 100ms)
 * 2. Component render thường xuyên (parent re-render nhiều) (Component renders frequently - parent re-renders many times)
 * 3. Props là large objects/arrays (Props are large objects/arrays)
 * 4. Expensive calculations (sort 10k items, heavy math) (Tính toán tốn kém - sắp xếp 10k mục, toán nặng)
 *
 * ❌ KHÔNG NÊN DÙNG KHI (SHOULD NOT USE WHEN):
 * 1. Component nhỏ, render nhanh (< 10ms) (Small component, renders fast - < 10ms)
 * 2. Props đơn giản (strings, numbers) (Simple props - strings, numbers)
 * 3. Component hiếm khi re-render (Component rarely re-renders)
 * 4. Premature optimization (chưa đo được bottleneck) (Tối ưu sớm - haven't measured bottleneck)
 *
 * 💡 REMEMBER (NHỚ):
 * - useMemo/useCallback có overhead (memory + comparison cost) (has overhead - chi phí bộ nhớ + so sánh)
 * - Chỉ optimize khi thực sự cần (measure first!) (Only optimize when really needed - measure first!)
 */
```

---

### **🔍 Phần 3: Profiling & Performance Debugging (Part 3: Profiling & Performance Debugging)**

```typescript
/**
 * 🐛 CHROME DEVTOOLS - Performance Tab
 * (CHROME DEVTOOLS - Tab Hiệu Năng)
 *
 * Cách sử dụng (How to use):
 * 1. Mở DevTools → Performance tab (Open DevTools → Performance tab)
 * 2. Click Record ⏺ (Click Record)
 * 3. Tương tác với app (scroll, click, type) (Interact with app)
 * 4. Click Stop ⏹️ (Click Stop)
 * 5. Phân tích flame chart (Analyze flame chart)
 */

// 📊 Tích hợp Performance Profiler trong code (Integrate Performance Profiler in code):
import { Profiler, ProfilerOnRenderCallback } from 'react';

// Callback function nhận thông tin timing (Callback function receives timing info)
const onRenderCallback: ProfilerOnRenderCallback = (
  id, // "App" - Profiler ID (ID của Profiler)
  phase, // "mount" hoặc "update" (mount or update)
  actualDuration, // Thời gian render component + children (ms) (Time to render component + children - ms)
  baseDuration, // Thời gian render estimate nếu không có memo (Estimated render time without memo)
  startTime, // Timestamp bắt đầu render (Timestamp start render)
  commitTime, // Timestamp commit changes to DOM (Timestamp commit changes to DOM)
  interactions // Set of interactions tracked (experimental) (Tập các tương tác được theo dõi - thử nghiệm)
) => {
  // 📊 Log performance data (Ghi log dữ liệu hiệu năng)
  console.log('Profiler:', {
    id,
    phase,
    actualDuration: `${actualDuration.toFixed(2)}ms`,
    baseDuration: `${baseDuration.toFixed(2)}ms`,
    improvement: `${((1 - actualDuration / baseDuration) * 100).toFixed(1)}%`, // % cải thiện
  });

  // ⚠️ Cảnh báo nếu render quá chậm (Warn if render too slow)
  if (actualDuration > 100) {
    console.warn(
      `⚠️ Slow render detected: ${id} took ${actualDuration.toFixed(2)}ms`
    );
    // (Phát hiện render chậm)
  }

  // 📤 Gửi data đến analytics service (Send data to analytics service)
  if (process.env.NODE_ENV === 'production') {
    sendToAnalytics('performance', {
      component: id,
      duration: actualDuration,
      phase,
    });
  }
};

// Wrap component với Profiler
function App() {
  return (
    <Profiler id="App" onRender={onRenderCallback}>
      <Dashboard />
      <TradingView />
    </Profiler>
  );
}

/**
 * 📊 CUSTOM PERFORMANCE HOOKS
 */

// Hook đo thời gian render
function useRenderTime(componentName: string) {
  const renderStartTime = useRef<number>();

  // 🔜 Trước render
  renderStartTime.current = performance.now();

  useEffect(() => {
    // 🔚 Sau render (DOM updated)
    const renderEndTime = performance.now();
    const duration = renderEndTime - renderStartTime.current!;

    console.log(`${componentName} render time: ${duration.toFixed(2)}ms`);

    // Track trong production
    if (duration > 50) {
      reportSlowRender(componentName, duration);
    }
  });
}

// Usage:
function Dashboard() {
  useRenderTime('Dashboard');
  // ... component logic
}

// Hook track re-renders count
function useRenderCount(componentName: string) {
  const renderCount = useRef(0);

  useEffect(() => {
    renderCount.current++;
    console.log(`${componentName} rendered ${renderCount.current} times`);
  });

  return renderCount.current;
}

// Hook track props changes
function useWhyDidYouUpdate(name: string, props: any) {
  const previousProps = useRef<any>();

  useEffect(() => {
    if (previousProps.current) {
      // So sánh props cũ vs mới
      const allKeys = Object.keys({ ...previousProps.current, ...props });
      const changedProps: any = {};

      allKeys.forEach((key) => {
        if (previousProps.current[key] !== props[key]) {
          changedProps[key] = {
            from: previousProps.current[key],
            to: props[key],
          };
        }
      });

      if (Object.keys(changedProps).length > 0) {
        console.log('[why-did-you-update]', name, changedProps);
      }
    }

    previousProps.current = props;
  });
}

// Usage:
function OrderItem({ order, onDelete }) {
  useWhyDidYouUpdate('OrderItem', { order, onDelete });
  // 💡 Log ra props nào thay đổi gây re-render

  return <div>...</div>;
}

/**
 * 📈 WEB VITALS MONITORING
 */

import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals';

// Track Core Web Vitals
function setupWebVitals() {
  // 📊 Largest Contentful Paint (LCP)
  // Mục tiêu: < 2.5s
  getLCP((metric) => {
    console.log('LCP:', metric.value, 'ms');
    sendToAnalytics('web-vitals', {
      name: 'LCP',
      value: metric.value,
      rating: metric.rating, // 'good', 'needs-improvement', 'poor'
    });
  });

  // 📊 First Input Delay (FID)
  // Mục tiêu: < 100ms
  getFID((metric) => {
    console.log('FID:', metric.value, 'ms');
    sendToAnalytics('web-vitals', { name: 'FID', value: metric.value });
  });

  // 📊 Cumulative Layout Shift (CLS)
  // Mục tiêu: < 0.1
  getCLS((metric) => {
    console.log('CLS:', metric.value);
    sendToAnalytics('web-vitals', { name: 'CLS', value: metric.value });
  });

  // 📊 First Contentful Paint (FCP)
  // Mục tiêu: < 1.8s
  getFCP((metric) => {
    console.log('FCP:', metric.value, 'ms');
    sendToAnalytics('web-vitals', { name: 'FCP', value: metric.value });
  });

  // 📊 Time to First Byte (TTFB)
  // Mục tiêu: < 600ms
  getTTFB((metric) => {
    console.log('TTFB:', metric.value, 'ms');
    sendToAnalytics('web-vitals', { name: 'TTFB', value: metric.value });
  });
}

// Initialize trong app
if (typeof window !== 'undefined') {
  setupWebVitals();
}
```

---

### **⚛️ Phần 4: React 18 Concurrent Features (Part 4: React 18 Concurrent Features)**

```typescript
/**
 * 🚀 REACT 18 - Concurrent Rendering
 * (REACT 18 - Render Đồng Thời)
 *
 * Concurrent Mode cho phép React:
 * (Concurrent Mode allows React to:)
 * - Bắt đầu render update (Start rendering update)
 * - Tạm dừng giữa chừng (interruptible - có thể gián đoạn) (Pause mid-way - interruptible)
 * - Quay lại render cái khác quan trọng hơn (Return to render something more important)
 * - Hủy bỏ render không còn cần thiết (Cancel render no longer needed)
 *
 * → UI luôn responsive, không bị block!
 * (→ UI always responsive, not blocked!)
 */

import { useTransition, useDeferredValue, startTransition } from 'react';

/**
 * 🔄 USETRANSITION - Mark updates as non-urgent
 * (USETRANSITION - Đánh dấu cập nhật không khẩn cấp)
 */

function SearchComponent() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  // isPending = true khi transition đang chạy
  // (isPending = true when transition is running)
  const [isPending, startTransition] = useTransition();

  const handleSearch = (value: string) => {
    // ⚡ URGENT (Khẩn cấp): Cập nhật input ngay lập tức (không delay)
    // (Update input immediately - no delay)
    setQuery(value);
    // 💡 User thấy input update liền → responsive
    // (User sees input update immediately → responsive)

    // 🐌 NON-URGENT (Không khẩn cấp): Cập nhật results có thể delay
    // (Update results can be delayed)
    startTransition(() => {
      const filtered = heavySearch(value); // Tính toán nặng (100ms+) (Heavy computation - 100ms+)
      setResults(filtered);
      // 💡 React có thể delay update này nếu có việc quan trọng hơn
      // (React can delay this update if there's more important work)
    });
  };

  return (
    <div>
      <input
        value={query}
        onChange={(e) => handleSearch(e.target.value)}
        placeholder="Search..."
      />

      {/* Hiển thị loading state (Show loading state) */}
      {isPending && <Spinner />}

      {/* Results list (có thể delay update) (Results list - can delay update) */}
      <ResultsList results={results} />
    </div>
  );
}

/**
 * SO SÁNH: Without vs With Transition
 * (COMPARISON: Without vs With Transition)
 */

// ❌ WITHOUT TRANSITION (Không có Transition):
// User type "a" → "ab" → "abc" nhanh (User gõ nhanh)
// 1. Update input "a" (1ms) (Cập nhật input "a")
// 2. Heavy search "a" (100ms) ← BLOCKS UI! (Tìm kiếm nặng "a" - chặn giao diện!)
// 3. Update input "ab" (phải đợi search "a" xong) (Cập nhật input "ab" - phải đợi tìm "a" xong)
// 4. Heavy search "ab" (100ms) ← BLOCKS UI! (Tìm kiếm nặng "ab" - chặn giao diện!)
// 5. Update input "abc" (phải đợi...) (Cập nhật input "abc" - phải đợi...)
// → Input lag, user thấy chậm (Input lag, user thấy chậm)

// ✅ WITH TRANSITION (Có Transition):
// User type "a" → "ab" → "abc" nhanh (User gõ nhanh)
// 1. Update input "a" (1ms) → Hiển thị ngay! (Cập nhật input "a" → hiển thị ngay!)
// 2. Start search "a" (interruptible) (Bắt đầu tìm "a" - có thể gián đoạn)
// 3. Update input "ab" (1ms) → Hiển thị ngay! (Cập nhật input "ab" → hiển thị ngay!)
// 4. Cancel search "a", start search "ab" (Hủy tìm "a", bắt đầu tìm "ab")
// 5. Update input "abc" (1ms) → Hiển thị ngay! (Cập nhật input "abc" → hiển thị ngay!)
// 6. Cancel search "ab", start search "abc" (Hủy tìm "ab", bắt đầu tìm "abc")
// 7. Search "abc" finish → show results (Tìm "abc" xong → hiển thị kết quả)
// → Input mượt mà, responsive! (Input mượt mà, phản hồi tốt!)

/**
 * 📊 USEDEFERREDVALUE - Defer value updates
 * (USEDEFERREDVALUE - Trì hoãn cập nhật giá trị)
 */

function ProductList({ query }: { query: string }) {
  const [products, setProducts] = useState([]);

  // deferredQuery = giá trị "delay" của query
  // (deferredQuery = "delayed" value of query)
  const deferredQuery = useDeferredValue(query);
  // 💡 Khi query thay đổi nhanh, deferredQuery update chậm hơn
  // (When query changes fast, deferredQuery updates slower)

  useEffect(() => {
    // Tìm kiếm dựa trên deferredQuery (Search based on deferredQuery)
    const results = searchProducts(deferredQuery);
    setProducts(results);
  }, [deferredQuery]);

  // Hiển thị loading khi query và deferredQuery khác nhau
  // (Show loading when query and deferredQuery are different)
  const isStale = query !== deferredQuery;

  return (
    <div>
      {isStale && <div className="opacity-50">Updating...</div>}
      {/* (Đang cập nhật...) */}

      <div className={isStale ? 'opacity-50' : 'opacity-100'}>
        {products.map((product) => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
    </div>
  );
}

/**
 * 🎯 REAL-WORLD EXAMPLE: Tab Switching
 */

function TabsWithTransition() {
  const [activeTab, setActiveTab] = useState('posts');
  const [isPending, startTransition] = useTransition();

  const handleTabChange = (tab: string) => {
    // ⚡ Update tab indicator ngay (urgent)
    setActiveTab(tab);

    // 🐌 Render tab content có thể delay (non-urgent)
    startTransition(() => {
      // Tab content có thể nặng (1000+ posts)
      // React có thể delay để giữ UI responsive
    });
  };

  return (
    <div>
      {/* Tab buttons - update instantly */}
      <div className="tabs">
        <button
          className={activeTab === 'posts' ? 'active' : ''}
          onClick={() => handleTabChange('posts')}
        >
          Posts {isPending && '...'}
        </button>
        <button
          className={activeTab === 'comments' ? 'active' : ''}
          onClick={() => handleTabChange('comments')}
        >
          Comments {isPending && '...'}
        </button>
      </div>

      {/* Tab content - can be deferred */}
      <Suspense fallback={<Spinner />}>
        {activeTab === 'posts' && <PostsList />}
        {activeTab === 'comments' && <CommentsList />}
      </Suspense>
    </div>
  );
}

/**
 * 💡 CONCURRENT MODE BENEFITS:
 *
 * 1. Responsive UI:
 *    - Input, clicks, animations luôn instant
 *    - Không bị block bởi heavy renders
 *
 * 2. Better UX:
 *    - Show loading states (isPending)
 *    - Stale content visual feedback
 *
 * 3. Performance:
 *    - Skip unnecessary renders (hủy bỏ old work)
 *    - Prioritize important updates
 */
```

---

### **🏭 Phần 5: Production Optimization Checklist**

```typescript
/**
 * ✅ PRODUCTION CHECKLIST - Trước khi deploy
 */

// 1️⃣ BUNDLE ANALYSIS - Phân tích bundle size
// File: package.json
{
  "scripts": {
    "build": "vite build",
    "analyze": "vite build && vite-bundle-visualizer"
  }
}
// Chạy: npm run analyze
// → Mở browser, xem các dependencies lớn nhất
// 🎯 Tìm và thay thế libraries nặng:
// - moment.js (288KB) → date-fns (78KB)
// - lodash (72KB) → lodash-es + tree-shaking (10KB)
// - material-ui (500KB+) → headlessui (50KB)

// 2️⃣ CODE SPLITTING STRATEGY
const routes = [
  {
    path: '/',
    component: lazy(() => import('./pages/Dashboard'))
  },
  {
    path: '/trading',
    component: lazy(() => import('./pages/Trading'))
  },
  // ... tất cả routes lazy load
];

// Prefetch routes khi hover
const prefetchRoute = (path: string) => {
  const route = routes.find(r => r.path === path);
  if (route) {
    route.component.preload();  // Preload component
  }
};

// Usage:
<Link
  to="/trading"
  onMouseEnter={() => prefetchRoute('/trading')}
>
  Trading
</Link>
// 💡 Hover link → tải trước component → click instant!

// 3️⃣ IMAGE OPTIMIZATION
// - Dùng WebP format (30% nhỏ hơn JPEG)
// - Responsive images
<img
  src="logo.webp"
  srcSet="
    logo-320.webp 320w,
    logo-640.webp 640w,
    logo-1280.webp 1280w
  "
  sizes="(max-width: 640px) 320px, (max-width: 1280px) 640px, 1280px"
  loading="lazy"  // Native lazy loading
  alt="Logo"
/>

// 4️⃣ FONT OPTIMIZATION
// File: index.html
<head>
  {/* Preconnect đến Google Fonts */}
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin />

  {/* Preload critical font */}
  <link
    rel="preload"
    href="/fonts/inter-var.woff2"
    as="font"
    type="font/woff2"
    crossOrigin
  />

  {/* Font display swap - hiển thị fallback font trước */}
  <style>
    @font-face {{
      font-family: 'Inter';
      src: url('/fonts/inter-var.woff2') format('woff2');
      font-display: swap;  /* Show fallback, swap khi font ready */
    }}
  </style>
</head>

// 5️⃣ SERVICE WORKER - Offline caching
// File: sw.js (Service Worker)
const CACHE_NAME = 'app-v1';
const urlsToCache = [
  '/',
  '/static/css/main.css',
  '/static/js/main.js',
  '/logo.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // Return cached version or fetch from network
        return response || fetch(event.request);
      })
  );
});

// Register service worker
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js')
    .then(reg => console.log('Service Worker registered'));
}

// 6️⃣ BUNDLE SIZE BUDGET - CI/CD check
// File: .bundlewatch.config.json
{
  "files": [
    {
      "path": "dist/**/*.js",
      "maxSize": "500kb",  // Fail nếu vượt 500KB
      "compression": "gzip"
    },
    {
      "path": "dist/**/*.css",
      "maxSize": "50kb"
    }
  ]
}

// CI/CD script:
// npm run build && bundlewatch
// → Fail CI nếu bundle quá lớn!

// 7️⃣ PERFORMANCE MONITORING
import { onCLS, onFID, onLCP } from 'web-vitals';

function sendToGoogleAnalytics({ name, delta, id }) {
  gtag('event', name, {
    event_category: 'Web Vitals',
    value: Math.round(name === 'CLS' ? delta * 1000 : delta),
    event_label: id,
    non_interaction: true,
  });
}

onCLS(sendToGoogleAnalytics);
onFID(sendToGoogleAnalytics);
onLCP(sendToGoogleAnalytics);

/**
 * 📊 KẾT QUẢ SAU TỐI ƯU:
 *
 * Before:
 * - Bundle: 2.5MB
 * - Load time: 5-7s
 * - LCP: 4.5s
 * - FPS: 15
 * - Memory: 500MB
 *
 * After:
 * - Bundle: 450KB (↓ 82%)
 * - Load time: 1.5-2s (↓ 70%)
 * - LCP: 1.2s (↓ 73%)
 * - FPS: 60 (↑ 4x)
 * - Memory: 80MB (↓ 84%)
 */
```

---

} // ✅ Chỉ render ~12 items → mượt mà

```

---
```
