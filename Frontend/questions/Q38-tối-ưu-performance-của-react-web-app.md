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

// 📦 A. Cấu Hình Vite (Công cụ build hiện đại - nhanh hơn Webpack)
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
    // Lý do: Browser chỉ tải file cần thiết → giảm Initial Load time
    rollupOptions: {
      output: {
        manualChunks: {
          // Tách React libraries riêng (ít thay đổi → cache browser tốt)
          // Khi update app code, React vendor vẫn dùng cache cũ
          'react-vendor': ['react', 'react-dom', 'react-router-dom'],

          // Tách chart libraries (rất nặng - 500KB+)
          // Chỉ load khi user vào trang có chart
          'chart-vendor': ['recharts', 'lightweight-charts'],

          // Tách utilities thành bundle riêng
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
// Giải thích: Thay vì load toàn bộ app lúc đầu, chỉ load trang user cần
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
// Hoạt động: React so sánh props cũ vs mới (shallow comparison)
// → Nếu giống nhau → KHÔNG re-render → Tăng performance
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
  // ✅ useCallback: Lưu lại function reference
  // Vấn đề: Mỗi lần render → tạo function mới → OrderItem re-render vì onDelete khác
  // Giải pháp: useCallback lưu function → reference giống nhau → OrderItem KHÔNG re-render
  const handleDelete = useCallback((id: string) => {
    console.log('Xóa order:', id);
    // Call API xóa order...
  }, []); // [] = function không đổi, tạo 1 lần duy nhất

  // ✅ useMemo: Cache kết quả tính toán nặng
  // Vấn đề: Mỗi render → sort lại 10,000 orders → chậm
  // Giải pháp: useMemo cache kết quả → chỉ sort lại KHI orders thay đổi
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
// Giải thích: Thay vì render 10,000 items → chỉ render items hiển thị trên màn hình
// VD: Màn hình cao 600px, mỗi item 50px → chỉ render 12 items (600/50)
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

// 🏪 Zustand: Thư viện state management nhẹ, nhanh hơn Redux
// Ưu điểm:
// - Không cần Provider wrapper
// - Selective subscription (chỉ subscribe state cần thiết)
// - API đơn giản, ít boilerplate
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

// ✅ Selective Subscription: Chỉ subscribe phần state cần thiết
// Component này CHỈ re-render khi orders thay đổi
// Khi prices update → component KHÔNG re-render (vì không subscribe prices)
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

// 🧹 Cleanup useEffect: Dọn dẹp resources khi component unmount
// Vấn đề: Không cleanup → memory leak (bộ nhớ tăng dần 50MB → 500MB)

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

    // ✅ QUAN TRỌNG: Cleanup function
    // Chạy khi component unmount hoặc dependencies thay đổi
    return () => {
      console.log('Dọn dẹp WebSocket...');

      // Đóng WebSocket connection
      if (
        ws.readyState === WebSocket.OPEN ||
        ws.readyState === WebSocket.CONNECTING
      ) {
        ws.close(); // Ngắt kết nối → giải phóng memory
      }

      // Nếu không cleanup:
      // - WebSocket vẫn mở → nhận data → update state của component đã unmount
      // - Gây memory leak + warning "Can't perform state update on unmounted component"
    };
  }, []); // [] = chỉ chạy 1 lần khi mount

  return <div>Biểu đồ trading...</div>;
}

// 🧹 B. Cancel API Requests với AbortController
function OrderHistory() {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    // Tạo AbortController để cancel request
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

// 🧹 C. Clear Timers & Intervals
function PriceRefresh() {
  const [price, setPrice] = useState(0);

  useEffect(() => {
    // Refresh giá mỗi 5 giây
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

// 🧹 D. Remove Event Listeners
function ResizableChart() {
  const chartRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // Handler cho window resize
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
