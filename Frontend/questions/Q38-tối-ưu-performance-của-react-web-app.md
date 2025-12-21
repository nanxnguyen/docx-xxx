# 🚀 Q38: Tối Ưu Performance của React Web App

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"Tối ưu hiệu năng React = 5 lớp: Build-time, Mạng, Rendering, State, Bộ nhớ.**

**🏗️ Chiến Lược Tối ƪu 5 Lớp:**

1. **Tối ƪu Build-time**:
   - **Chia Code**: `React.lazy()` + Suspense → tải routes theo yêu cầu.
   - **Tree-shaking**: Xóa code không dùng (ES modules + Webpack/Vite).
   - **Phân Tích Bundle**: `webpack-bundle-analyzer` → xác định dependencies lớn.
   - **Mục tiêu**: Giảm bundle 2.5MB → 500KB (nhanh hơn 5 lần).

2. **Tối ƪu Mạng**:
   - **HTTP/2 + Brotli**: Nén tài nguyên 70%.
   - **CDN**: Phục vụ tài nguyên tĩnh từ edge servers (độ trễ thấp hơn).
   - **Gợi ý Tài Nguyên**: `<link rel="preload">` fonts, CSS quan trọng.
   - **Service Worker**: Cache tài nguyên tĩnh → hỗ trợ offline.

3. **Tối ƪu Rendering** (⚡ Quan Trọng Nhất):
   - **React.memo()**: Ngăn con render lại khi props không đổi.
   - **useMemo/useCallback**: Cache tính toán/hàm tốn kém.
   - **Virtual Scrolling**: `react-window` cho 10K+ items → chỉ render phần hiển thị.
   - **Debounce/Throttle**: Giới hạn event handlers (scroll, resize, input).
   - **Lazy Images**: `loading="lazy"` + Intersection Observer.

4. **Quản Lý State**:
   - **Tách Context**: Tách contexts nhỏ → ngăn re-renders không cần thiết.
   - **Zustand/Redux Toolkit**: Đăng ký chọn lọc → components chỉ render lại khi state thực sự dùng thay đổi.
   - **React Query**: Cache dữ liệu server → giảm lời gọi API.
   - **Immer**: Cập nhật bất biến hiệu quả (ít boilerplate hơn).

5. **Quản Lý Bộ Nhớ**:
   - **Dọn Dẹp Effects**: `useEffect` trả về cleanup → xóa listeners, hủy timers.
   - **WeakMap**: Giữ tham chiếu yếu → tự động GC.
   - **Profiling**: Chrome DevTools Memory tab → phát hiện rò rỉ.

**🎯 Real-time Updates Optimization (WebSocket):**
- **Problem**: 1000 updates/s → 60+ components re-render → UI freeze.
- **Solution**:
  1. **Debounce updates**: Batch 100 updates/100ms → 10 batches/s instead of 1000 renders/s.
  2. **Selective subscriptions**: Components subscribe to specific data slices.
  3. **Virtual scrolling**: Render only visible items.
  4. **Memoization**: `React.memo` + `useMemo` prevent unnecessary re-renders.

**📊 Performance Metrics (Web Vitals):**
- **LCP (Largest Contentful Paint)**: < 2.5s (good), 2.5-4s (needs improvement), > 4s (poor).
- **FID (First Input Delay)**: < 100ms.
- **CLS (Cumulative Layout Shift)**: < 0.1.
- **Tools**: Lighthouse, Web Vitals library, Chrome DevTools Performance tab.

**⚠️ Common Mistakes:**
- **Inline functions/objects**: Tạo new reference mỗi render → child re-render.
  ```jsx
  // ❌ Bad
  <Child onClick={() => handle()} data={{ id: 1 }} />
  // ✅ Good
  const handleClick = useCallback(() => handle(), []);
  const data = useMemo(() => ({ id: 1 }), []);
  <Child onClick={handleClick} data={data} />
  ```
- **Overuse useMemo/useCallback**: Premature optimization → chỉ dùng khi đo được bottleneck.
- **Missing dependencies**: `useEffect([])` nhưng dùng props/state inside → stale closure.

**💡 Senior Insights:**
- **Profiler**: `<Profiler>` component + DevTools → measure render time.
- **Concurrent Mode**: React 18 `useTransition` → non-urgent updates không block UI.
- **Bundle Budget**: Set budget (500KB) → CI fail nếu vượt.
- **Lighthouse CI**: Auto performance testing trong CI/CD.

---

**❓ Tình Huống:**

Bạn là Senior Frontend Developer của một Trading Platform (React + TypeScript). App hiện tại có các vấn đề:

- **Initial Load**: 5-7s trên 3G, bundle size 2.5MB
- **Runtime Performance**:
  - Real-time updates (WebSocket) gây re-render toàn bộ app (60+ components)
  - List 10,000+ orders lag khi scroll (FPS drop 60 → 15)
  - Memory leak sau 2-3 giờ sử dụng (memory tăng từ 50MB → 500MB)
- **User Complaints**: App chậm, lag, sometimes crash

**Yêu cầu:** Thiết kế và implement chiến lược tối ưu toàn diện (từ build-time đến runtime).

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

**📊 Performance Metrics Target (Mục tiêu):**

- Initial Load: 5-7s → **< 2s** (70% improvement)
- Bundle Size: 2.5MB → **< 500KB** (80% reduction)
- FPS: 15 → **60 FPS** (4x improvement)
- Memory: 500MB → **< 100MB** (80% reduction)

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

**🎯 Kết Quả Sau Optimization:**

```
┌────────────────────────────────────────────────────────────────┐
│           PERFORMANCE METRICS - BEFORE vs AFTER                 │
├────────────────────────────────────────────────────────────────┤
│  Metric              │ Before      │ After       │ Improvement │
│ ─────────────────────┼─────────────┼─────────────┼──────────── │
│  Initial Load        │ 5-7s        │ 1.5-2s      │ 70% faster  │
│  Bundle Size         │ 2.5MB       │ 450KB       │ 82% smaller │
│  FCP (First Paint)   │ 3s          │ 0.8s        │ 73% faster  │
│  TTI (Interactive)   │ 6s          │ 2s          │ 67% faster  │
│  Scroll FPS          │ 15 FPS      │ 60 FPS      │ 4x better   │
│  Memory Usage        │ 500MB       │ 80MB        │ 84% less    │
│  Re-renders/sec      │ 200+        │ 10-20       │ 90% less    │
└────────────────────────────────────────────────────────────────┘
```

**Best Practices:**

1. **Measure First**: Dùng Lighthouse, Chrome DevTools Performance
2. **Bundle Analysis**: `npm run build -- --analyze`
3. **Code Splitting**: Route-level + Component-level
4. **State Management**: Context cho static, Zustand cho complex state
5. **Memory Management**: Always cleanup useEffect

**Common Mistakes (Lỗi Thường Gặp):**

```typescript
// ❌ LỖI 1: Inline functions trong render
// Vấn đề: Mỗi render tạo function mới → child component re-render không cần thiết
{
  items.map((item) => (
    <Item
      key={item.id}
      onClick={() => handleClick(item)} // ❌ Function mới mỗi lần render
    />
  ));
}

// ✅ CÁCH SỬA: Dùng useCallback để memoize function
const handleClick = useCallback((item) => {
  console.log('Clicked:', item);
  // Xử lý logic...
}, []); // Function reference không đổi

{
  items.map((item) => (
    <Item
      key={item.id}
      onClick={handleClick} // ✅ Reference giống nhau → không re-render
      item={item}
    />
  ));
}

// ❌ LỖI 2: Không cleanup useEffect → Memory Leak
useEffect(() => {
  const ws = new WebSocket('wss://api.example.com');
  ws.onmessage = (e) => setData(e.data);
  // ❌ Thiếu cleanup → WebSocket không đóng → memory leak
}, []);

// ✅ CÁCH SỬA: Luôn cleanup resources
useEffect(() => {
  const ws = new WebSocket('wss://api.example.com');
  ws.onmessage = (e) => setData(e.data);

  return () => {
    ws.close(); // ✅ Đóng WebSocket khi unmount
  };
}, []);

// ❌ LỖI 3: Quên dependencies trong useMemo/useCallback
const sortedData = useMemo(() => {
  return data.sort((a, b) => a[sortBy] - b[sortBy]);
}, []); // ❌ Thiếu [data, sortBy] → không update khi data/sortBy thay đổi

// ✅ CÁCH SỬA: Khai báo đầy đủ dependencies
const sortedData = useMemo(() => {
  return data.sort((a, b) => a[sortBy] - b[sortBy]);
}, [data, sortBy]); // ✅ Tính lại khi data hoặc sortBy thay đổi

// ❌ LỖI 4: Render toàn bộ list lớn
function OrderList({ orders }) {
  return (
    <div>
      {orders.map((order) => (
        <OrderRow key={order.id} order={order} />
      ))}
    </div>
  );
} // ❌ 10,000 items → 10,000 DOM nodes → lag

// ✅ CÁCH SỬA: Dùng virtual scrolling
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
} // ✅ Chỉ render ~12 items → mượt mà
```

---

## **🔬 DEEP DIVE: Hiểu Sâu Cơ Chế React**

### **⚛️ Phần 1: React Reconciliation - Thuật Toán Đối Chiếu**

```typescript
/**
 * 🧠 REACT RECONCILIATION - Cách React quyết định render gì
 * 
 * Khi state/props thay đổi, React KHÔNG re-render toàn bộ app!
 * Thay vào đó, React dùng thuật toán "Reconciliation" (Diffing) để:
 * 1. So sánh Virtual DOM cũ vs mới
 * 2. Tìm ra sự khác biệt (diff)
 * 3. Chỉ update những phần khác biệt vào Real DOM
 * 
 * 📊 Complexity: O(n) thay vì O(n^3) (thuật toán diff chuẩn)
 */

// 🌳 VIRTUAL DOM TREE EXAMPLE:
// Đây là cách React biểu diễn UI trong bộ nhớ (JavaScript objects)

const virtualDOM_Before = {
  type: 'div',
  props: { className: 'container' },
  children: [
    {
      type: 'h1',
      props: { className: 'title' },
      children: ['Hello']  // 💡 Text node
    },
    {
      type: 'ul',
      props: {},
      children: [
        { type: 'li', props: { key: '1' }, children: ['Item 1'] },
        { type: 'li', props: { key: '2' }, children: ['Item 2'] }
      ]
    }
  ]
};

// User click button → state thay đổi → React tạo Virtual DOM mới:
const virtualDOM_After = {
  type: 'div',
  props: { className: 'container' },
  children: [
    {
      type: 'h1',
      props: { className: 'title active' },  // 🔄 className changed!
      children: ['Hello World']  // 🔄 Text changed!
    },
    {
      type: 'ul',
      props: {},
      children: [
        { type: 'li', props: { key: '1' }, children: ['Item 1'] },  // ✅ Không đổi
        { type: 'li', props: { key: '2' }, children: ['Item 2'] },  // ✅ Không đổi
        { type: 'li', props: { key: '3' }, children: ['Item 3'] }   // ➕ Mới thêm
      ]
    }
  ]
};

/**
 * 🔍 DIFFING ALGORITHM - Thuật toán so sánh:
 * 
 * React duyệt 2 trees song song (old vs new):
 */

function diff(oldNode, newNode) {
  // RULE 1: Nếu type khác nhau → XOÁ cũ , TẠO mới
  if (oldNode.type !== newNode.type) {
    // VD: <div> → <span> = Destroy <div> + Create <span>
    return { action: 'REPLACE', node: newNode };
    // 💡 XOÁ toàn bộ subtree cũ, tạo mới hoàn toàn
    // 💥 Tốn kém! Nên tránh thay đổi type
  }
  
  // RULE 2: Nếu type giống nhau → SO SÁNH PROPS
  if (oldNode.type === newNode.type) {
    const propsChanged = compareProps(oldNode.props, newNode.props);
    
    if (propsChanged) {
      // VD: className="title" → className="title active"
      return { action: 'UPDATE_PROPS', changes: propsChanged };
      // 💡 CHỈ update attributes, GIỮ nguyên DOM node
      // ✅ Hiệu quả! Chỉ tốn 1 DOM operation
    }
  }
  
  // RULE 3: So sánh CHILDREN (recursive)
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
      changes[key] = null;  // Mark for removal
    }
  }
  
  return Object.keys(changes).length > 0 ? changes : null;
}

/**
 * 🔑 KEY PROP - Tại sao KEY quan trọng?
 * 
 * Khi diff children list, React cần biết:
 * - Item nào giữ nguyên?
 * - Item nào mới thêm?
 * - Item nào bị xoá?
 * - Item nào thay đổi vị trí?
 */

// ❌ KHÔNG CÓ KEY - React không biết item nào là item nào:
const oldList = [
  <li>Apple</li>,   // index 0
  <li>Banana</li>,  // index 1
  <li>Cherry</li>   // index 2
];

const newList = [
  <li>Avocado</li>,  // index 0 - 💥 React nghĩ "Apple" đổi thành "Avocado"
  <li>Apple</li>,    // index 1 - 💥 React nghĩ "Banana" đổi thành "Apple"
  <li>Banana</li>,   // index 2 - 💥 React nghĩ "Cherry" đổi thành "Banana"
  <li>Cherry</li>    // index 3 - 💥 React tạo mới "Cherry"
];
// 💥 Kết quả: UPDATE 3 items + CREATE 1 item = 4 DOM operations!
// 💥 Thực tế chỉ cần: CREATE 1 item (Avocado) = 1 operation

// ✅ CÓ KEY - React biết chính xác item nào là item nào:
const oldListWithKey = [
  <li key="apple">Apple</li>,
  <li key="banana">Banana</li>,
  <li key="cherry">Cherry</li>
];

const newListWithKey = [
  <li key="avocado">Avocado</li>,  // ➕ Mới - CREATE
  <li key="apple">Apple</li>,      // ✅ Giữ nguyên - MOVE
  <li key="banana">Banana</li>,    // ✅ Giữ nguyên - MOVE
  <li key="cherry">Cherry</li>     // ✅ Giữ nguyên - MOVE
];
// ✅ Kết quả: CREATE 1 item + MOVE 3 items = Hiệu quả hơn nhiều!
// 💡 DOM MOVE rẻ hơn DOM UPDATE (không cần re-render content)

/**
 * ⚠️ KEY ANTI-PATTERNS - Các lỗi thường gặp:
 */

// ❌ LỖI 1: Dùng index làm key
items.map((item, index) => (
  <li key={index}>{item.name}</li>  // 💥 Khi items thay đổi thứ tự = bug!
));
// Tại sao sai?
// - Thêm item mới ở đầu list → tất cả index thay đổi
// - React nghĩ tất cả items thay đổi → re-render tất cả!
// - Input focus/state bị mất vì DOM node bị thay thế

// ❌ LỖI 2: Dùng random/generated key
items.map(item => (
  <li key={Math.random()}>{item.name}</li>  // 💥 Key khác nhau mỗi render!
));
// Tại sao sai?
// - Mỗi render = key mới → React nghĩ là item mới
// - Xóa cũ + tạo mới tất cả → mất state, performance tồi

// ✅ ĐÚNG: Dùng stable, unique ID từ data
items.map(item => (
  <li key={item.id}>{item.name}</li>  // ✅ ID từ database = stable + unique
));
// Tại sao đúng?
// - item.id không thay đổi (stable)
// - Mỗi item có ID khác nhau (unique)
// - React track đúng item qua các lann render
```

---

### **📊 Phần 2: React.memo Deep Dive - Hiểu Rõ Memoization**

```typescript
/**
 * 🧠 REACT.MEMO - Shallow Comparison Explained
 * 
 * React.memo so sánh props bằng "shallow comparison":
 * - Primitive values: So sánh giá trị (===)
 * - Objects/Arrays: So sánh reference (===)
 */

// 🔍 Shallow Comparison Implementation:
function shallowEqual(objA: any, objB: any): boolean {
  // 1. Nếu cùng reference → giống nhau
  if (objA === objB) return true;
  
  // 2. Nếu không phải object → khác nhau
  if (typeof objA !== 'object' || typeof objB !== 'object') return false;
  
  // 3. So sánh số lượng keys
  const keysA = Object.keys(objA);
  const keysB = Object.keys(objB);
  if (keysA.length !== keysB.length) return false;
  
  // 4. So sánh từng key (chỉ 1 level, không deep)
  for (const key of keysA) {
    if (objA[key] !== objB[key]) return false;
    // 💡 Dùng !== = so sánh reference cho nested objects
  }
  
  return true;
}

// 📊 VIỆC DỤ: Props comparison examples

// Example 1: Primitive props
const props1 = { name: 'John', age: 30 };
const props2 = { name: 'John', age: 30 };
shallowEqual(props1, props2);  // true - Values giống nhau
// → React.memo SKIPs re-render ✅

// Example 2: Different primitive
const props3 = { name: 'John', age: 31 };  // age changed
shallowEqual(props1, props3);  // false
// → React.memo RE-RENDERS 🔄

// Example 3: Nested object (reference)
const props4 = { user: { name: 'John' } };
const props5 = { user: { name: 'John' } };  // New object!
shallowEqual(props4, props5);  // false - Khác reference!
// 💡 Dù content giống nhau nhưng { } = new object = khác reference
// → React.memo RE-RENDERS 🔄

// Example 4: Same reference
const userObj = { name: 'John' };
const props6 = { user: userObj };
const props7 = { user: userObj };  // Same reference!
shallowEqual(props6, props7);  // true - Cùng reference
// → React.memo SKIPs re-render ✅

/**
 * ⚡ TỐI ƯU VỚI USEMEMO - Giữ reference ổn định
 */

function ParentBad() {
  const [count, setCount] = useState(0);
  
  // ❌ Mỗi render = tạo object mới
  const config = { theme: 'dark', lang: 'vi' };
  // 💡 Mỗi lần count thay đổi → ParentBad re-render → config mới
  
  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Count: {count}</button>
      <ChildMemo config={config} />
      {/* 💥 config luôn khác reference → ChildMemo luôn re-render! */}
    </div>
  );
}

function ParentGood() {
  const [count, setCount] = useState(0);
  
  // ✅ useMemo lưu lại object, chỉ tạo mới khi dependencies thay đổi
  const config = useMemo(
    () => ({ theme: 'dark', lang: 'vi' }),
    []  // Empty deps = tạo 1 lần duy nhất
  );
  // 💡 count thay đổi → config GIỮ NGUYÊN reference cũ
  
  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Count: {count}</button>
      <ChildMemo config={config} />
      {/* ✅ config cùng reference → ChildMemo SKIPs re-render! */}
    </div>
  );
}

const ChildMemo = memo(function Child({ config }) {
  console.log('Child render');  // Chỉ log khi config thay đổi
  return <div>Theme: {config.theme}</div>;
});

/**
 * 📊 USECALLBACK - Memoize functions
 */

function ParentWithCallbacks() {
  const [count, setCount] = useState(0);
  const [items, setItems] = useState([1, 2, 3]);
  
  // ❌ Mỗi render = function mới
  const handleClickBad = () => {
    console.log('Clicked');
  };
  
  // ✅ useCallback lưu function reference
  const handleClickGood = useCallback(() => {
    console.log('Clicked');
  }, []);  // [] = function không đổi
  
  // 💡 Function với dependencies
  const handleDelete = useCallback((id: number) => {
    setItems(items => items.filter(item => item !== id));
    // 💡 Dùng functional update → không cần items trong deps
  }, []);  // [] vì dùng functional update
  
  // ⚠️ Nếu dùng items trực tiếp:
  const handleDeleteBad = useCallback((id: number) => {
    setItems(items.filter(item => item !== id));
    // 💡 items = closure → PHẢI thêm vào deps
  }, [items]);  // items thay đổi → function mới → child re-render
  
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
      {items.map(item => (
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
 * 
 * ✅ NÊN DÙNG KHI:
 * 1. Component render chậm (> 100ms)
 * 2. Component render thường xuyên (parent re-render nhiều)
 * 3. Props là large objects/arrays
 * 4. Expensive calculations (sort 10k items, heavy math)
 * 
 * ❌ KHÔNG NÊN DÙNG KHI:
 * 1. Component nhỏ, render nhanh (< 10ms)
 * 2. Props đơn giản (strings, numbers)
 * 3. Component hiếm khi re-render
 * 4. Premature optimization (chưa đo được bottleneck)
 * 
 * 💡 REMEMBER:
 * - useMemo/useCallback có overhead (memory + comparison cost)
 * - Chỉ optimize khi thực sự cần (measure first!)
 */
```

---

### **🔍 Phần 3: Profiling & Performance Debugging**

```typescript
/**
 * 🐛 CHROME DEVTOOLS - Performance Tab
 * 
 * Cách sử dụng:
 * 1. Mở DevTools → Performance tab
 * 2. Click Record ⏺
 * 3. Tương tác với app (scroll, click, type)
 * 4. Click Stop ⏹️
 * 5. Phân tích flame chart
 */

// 📊 Tích hợp Performance Profiler trong code:
import { Profiler, ProfilerOnRenderCallback } from 'react';

// Callback function nhận thông tin timing
const onRenderCallback: ProfilerOnRenderCallback = (
  id,                  // "App" - Profiler ID
  phase,               // "mount" hoặc "update"
  actualDuration,      // Thời gian render component + children (ms)
  baseDuration,        // Thời gian render estimate nếu không có memo
  startTime,           // Timestamp bắt đầu render
  commitTime,          // Timestamp commit changes to DOM
  interactions         // Set of interactions tracked (experimental)
) => {
  // 📊 Log performance data
  console.log('Profiler:', {
    id,
    phase,
    actualDuration: `${actualDuration.toFixed(2)}ms`,
    baseDuration: `${baseDuration.toFixed(2)}ms`,
    improvement: `${((1 - actualDuration / baseDuration) * 100).toFixed(1)}%`
  });
  
  // ⚠️ Cảnh báo nếu render quá chậm
  if (actualDuration > 100) {
    console.warn(`⚠️ Slow render detected: ${id} took ${actualDuration.toFixed(2)}ms`);
  }
  
  // 📤 Gửi data đến analytics service
  if (process.env.NODE_ENV === 'production') {
    sendToAnalytics('performance', {
      component: id,
      duration: actualDuration,
      phase
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
      
      allKeys.forEach(key => {
        if (previousProps.current[key] !== props[key]) {
          changedProps[key] = {
            from: previousProps.current[key],
            to: props[key]
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
  getLCP(metric => {
    console.log('LCP:', metric.value, 'ms');
    sendToAnalytics('web-vitals', {
      name: 'LCP',
      value: metric.value,
      rating: metric.rating  // 'good', 'needs-improvement', 'poor'
    });
  });
  
  // 📊 First Input Delay (FID)
  // Mục tiêu: < 100ms
  getFID(metric => {
    console.log('FID:', metric.value, 'ms');
    sendToAnalytics('web-vitals', { name: 'FID', value: metric.value });
  });
  
  // 📊 Cumulative Layout Shift (CLS)
  // Mục tiêu: < 0.1
  getCLS(metric => {
    console.log('CLS:', metric.value);
    sendToAnalytics('web-vitals', { name: 'CLS', value: metric.value });
  });
  
  // 📊 First Contentful Paint (FCP)
  // Mục tiêu: < 1.8s
  getFCP(metric => {
    console.log('FCP:', metric.value, 'ms');
    sendToAnalytics('web-vitals', { name: 'FCP', value: metric.value });
  });
  
  // 📊 Time to First Byte (TTFB)
  // Mục tiêu: < 600ms
  getTTFB(metric => {
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

### **⚛️ Phần 4: React 18 Concurrent Features**

```typescript
/**
 * 🚀 REACT 18 - Concurrent Rendering
 * 
 * Concurrent Mode cho phép React:
 * - Bắt đầu render update
 * - Tạm dừng giữa chừng (interruptible)
 * - Quay lại render cái khác quan trọng hơn
 * - Hủy bỏ render không còn cần thiết
 * 
 * → UI luôn responsive, không bị block!
 */

import { useTransition, useDeferredValue, startTransition } from 'react';

/**
 * 🔄 USETRANSITION - Mark updates as non-urgent
 */

function SearchComponent() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  
  // isPending = true khi transition đang chạy
  const [isPending, startTransition] = useTransition();
  
  const handleSearch = (value: string) => {
    // ⚡ URGENT: Cập nhật input ngay lập tức (không delay)
    setQuery(value);
    // 💡 User thấy input update liền → responsive
    
    // 🐌 NON-URGENT: Cập nhật results có thể delay
    startTransition(() => {
      const filtered = heavySearch(value);  // Tính toán nặng (100ms+)
      setResults(filtered);
      // 💡 React có thể delay update này nếu có việc quan trọng hơn
    });
  };
  
  return (
    <div>
      <input
        value={query}
        onChange={(e) => handleSearch(e.target.value)}
        placeholder="Search..."
      />
      
      {/* Hiển thị loading state */}
      {isPending && <Spinner />}
      
      {/* Results list (có thể delay update) */}
      <ResultsList results={results} />
    </div>
  );
}

/**
 * SO SÁNH: Without vs With Transition
 */

// ❌ WITHOUT TRANSITION:
// User type "a" → "ab" → "abc" nhanh
// 1. Update input "a" (1ms)
// 2. Heavy search "a" (100ms) ← BLOCKS UI!
// 3. Update input "ab" (phải đợi search "a" xong)
// 4. Heavy search "ab" (100ms) ← BLOCKS UI!
// 5. Update input "abc" (phải đợi...)
// → Input lag, user thấy chậm

// ✅ WITH TRANSITION:
// User type "a" → "ab" → "abc" nhanh
// 1. Update input "a" (1ms) → Hiển thị ngay!
// 2. Start search "a" (interruptible)
// 3. Update input "ab" (1ms) → Hiển thị ngay!
// 4. Cancel search "a", start search "ab"
// 5. Update input "abc" (1ms) → Hiển thị ngay!
// 6. Cancel search "ab", start search "abc"
// 7. Search "abc" finish → show results
// → Input mượt mà, responsive!

/**
 * 📊 USEDEFERREDVALUE - Defer value updates
 */

function ProductList({ query }: { query: string }) {
  const [products, setProducts] = useState([]);
  
  // deferredQuery = giá trị "delay" của query
  const deferredQuery = useDeferredValue(query);
  // 💡 Khi query thay đổi nhanh, deferredQuery update chậm hơn
  
  useEffect(() => {
    // Tìm kiếm dựa trên deferredQuery
    const results = searchProducts(deferredQuery);
    setProducts(results);
  }, [deferredQuery]);
  
  // Hiển thị loading khi query và deferredQuery khác nhau
  const isStale = query !== deferredQuery;
  
  return (
    <div>
      {isStale && <div className="opacity-50">Updating...</div>}
      
      <div className={isStale ? 'opacity-50' : 'opacity-100'}>
        {products.map(product => (
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
