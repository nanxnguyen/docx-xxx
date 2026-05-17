# 🚀 Topic 27: Tối Ưu Performance của React Web App

## 1. ⭐ Senior/Staff Summary

React performance không phải là “thêm `useMemo` ở mọi nơi”. Performance tốt đến từ việc hiểu **render cost**, **state propagation**, **bundle/network cost**, **large list rendering**, **server-state caching**, **memory leaks**, và **đo đúng bottleneck trước khi tối ưu**.

Tư duy senior:

- 🧱 **Build-time:** giảm bundle, code splitting, tree-shaking, bundle budget.
- 🌐 **Network:** CDN, compression, resource hints, image/font optimization.
- ⚛️ **React rendering:** giảm re-render không cần thiết, giữ reference ổn định khi cần, memo đúng chỗ.
- 📦 **State management:** đặt state đúng scope, split context, selective subscription, server-state cache.
- 📜 **Large data UI:** virtualization, pagination, windowing, batch realtime updates.
- 🧹 **Memory:** cleanup effects, abort requests, unsubscribe WebSocket/listeners, detect leaks.
- 📊 **Measurement:** React Profiler, Chrome Performance/Memory, Web Vitals, production monitoring.

> 🔥 Senior point: Nếu chưa đo, đừng tối ưu theo cảm giác. `React.memo`, `useMemo`, `useCallback` đều có cost và chỉ đáng dùng khi render/calculation/reference churn thật sự là bottleneck.

## 2. 🧠 Key Mental Model or Key Points

React performance có 2 lớp cần tách rõ:

```txt
React work:
  state update -> render components -> diff/reconciliation -> commit DOM

Browser work:
  DOM/style changes -> layout/reflow -> paint -> composite
```

Các mental model quan trọng:

- **Render không đồng nghĩa DOM update:** Component render lại nhưng DOM có thể không đổi nhiều.
- **Parent render có thể kéo child render:** Trừ khi child memoized và props shallow-equal.
- **Reference equality quyết định nhiều tối ưu:** Object/function/array mới mỗi render làm `React.memo` khó có ích.
- **Context update re-render consumers:** Nếu context value đổi, nhiều consumer có thể render lại.
- **Server state khác client state:** Data từ API nên dùng cache như TanStack Query/SWR thay vì tự nhét mọi thứ vào global client state.
- **Large list là vấn đề DOM + React:** 10k rows cần virtualization/pagination, không chỉ memo.
- **Realtime update cần batching:** WebSocket 1000 msg/s không thể setState từng message.
- **Hydration/JS cost ảnh hưởng INP:** SSR có thể giúp LCP nhưng JS/hydration nặng vẫn làm tương tác chậm.

## 3. 📚 Main Concepts

### 3.1. 🏗️ 5 lớp tối ưu React performance

| Lớp | Mục tiêu | Kỹ thuật chính | Khi đáng làm |
|---|---|---|---|
| Build-time | Giảm JS/CSS phải tải | Code splitting, tree-shaking, bundle analyzer | Bundle lớn, initial load chậm |
| Network | Tải tài nguyên nhanh hơn | CDN, Brotli, preload/preconnect, cache | LCP/TTFB/network waterfall xấu |
| Rendering | Giảm render/commit cost | `React.memo`, `useMemo`, `useCallback`, virtualization | Profiler chỉ ra render chậm |
| State | Giảm propagation | Split context, selectors, colocate state, React Query | Nhiều component render vì state chung |
| Memory | Tránh leak/jank lâu dài | cleanup, `AbortController`, unsubscribe, heap snapshot | App chạy lâu bị chậm/crash |

### 3.2. ⚛️ Reconciliation và render lifecycle

Khi state/props/context đổi, React render component tree để tạo React elements mới, sau đó reconciliation so sánh tree mới/cũ.

Keys giúp React nhận diện item:

```tsx
{orders.map((order) => (
  <OrderRow key={order.id} order={order} />
))}
```

Không dùng index làm key nếu list có insert/delete/reorder:

```tsx
{orders.map((order, index) => (
  <OrderRow key={index} order={order} />
))}
```

Vì index key có thể gây:

- State row bị gán nhầm.
- Focus/input nhảy sai.
- Animation sai.
- Reconciliation kém hiệu quả.

> 💡 Trước khi memo, hãy kiểm tra key, state placement, context và list size. Sai key hoặc state đặt quá cao thường gây vấn đề lớn hơn thiếu `useMemo`.

### 3.3. 🧠 `React.memo`: shallow comparison, không phải magic

`React.memo` skip render nếu props shallow-equal.

```tsx
type OrderRowProps = {
  order: Order;
  onSelect: (id: string) => void;
};

const OrderRow = React.memo(function OrderRow({ order, onSelect }: OrderRowProps) {
  return (
    <button onClick={() => onSelect(order.id)}>
      {order.symbol} - {order.price}
    </button>
  );
});
```

`React.memo` có ích khi:

- Component render đắt.
- Props thường không đổi.
- Parent render thường xuyên.
- Props reference ổn định.

`React.memo` ít có ích khi:

- Component rất rẻ.
- Props luôn là object/function mới.
- Component tự đọc context thường xuyên đổi.
- Bottleneck nằm ở browser layout/paint, không phải React render.

### 3.4. 🧩 `useMemo` vs `useCallback`

`useMemo` cache value:

```tsx
const filteredOrders = React.useMemo(() => {
  return orders.filter((order) => order.symbol.includes(query));
}, [orders, query]);
```

`useCallback` cache function reference:

```tsx
const handleSelect = React.useCallback((id: string) => {
  setSelectedOrderId(id);
}, []);
```

Decision:

| Hook | Cache gì? | Dùng khi |
|---|---|---|
| `useMemo` | Kết quả tính toán | Filter/sort/map nặng, derived data lớn |
| `useCallback` | Function reference | Truyền callback xuống memoized child hoặc dependency của hook khác |

⚠️ Không dùng `useMemo` để “fix bug”. Nếu bỏ `useMemo` mà logic sai, có thể bạn đang mutate data hoặc dựa vào reference sai.

### 3.5. 📦 State management và context re-render

Context dễ dùng nhưng có thể gây re-render rộng.

❌ Một context chứa mọi thứ:

```tsx
const AppContext = React.createContext<{
  user: User;
  theme: Theme;
  prices: PriceMap;
  updatePrice: (price: Price) => void;
} | null>(null);
```

Khi `prices` đổi realtime, mọi consumer của `AppContext` có thể bị ảnh hưởng.

✅ Tách theo tần suất thay đổi:

```tsx
const AuthContext = React.createContext<AuthState | null>(null);
const ThemeContext = React.createContext<ThemeState | null>(null);
const PriceStoreContext = React.createContext<PriceStore | null>(null);
```

Với global state:

- Redux Toolkit: selectors + memoized selectors.
- Zustand: subscribe theo slice.
- Jotai/Recoil: atom-level subscription.
- TanStack Query/SWR: server-state cache.

> 🔥 Server data không nên tự quản lý bằng Context lớn nếu cần caching, retry, stale time, refetch, pagination.

### 3.6. 📜 Virtualization cho list/table lớn

Nếu render 10,000 rows, React và browser đều mệt. Virtualization chỉ render phần visible.

Use cases:

- Orders table.
- Logs viewer.
- Chat history.
- Large select/search results.
- Infinite scrolling feed.

Libraries:

- `react-window`
- `react-virtualized`
- TanStack Virtual

Tradeoff:

- Cần xử lý row height.
- Accessibility/focus/keyboard navigation phức tạp hơn.
- Browser find-in-page có thể không thấy item chưa render.
- SEO không phù hợp cho content public cần crawl đầy đủ.

### 3.7. ⏱️ Debounce, throttle và batching realtime updates

Debounce: chờ user ngừng gõ mới chạy.

```ts
function debounce<T extends (...args: never[]) => void>(fn: T, delay: number) {
  let timer: number | undefined;

  return (...args: Parameters<T>) => {
    window.clearTimeout(timer);
    timer = window.setTimeout(() => fn(...args), delay);
  };
}
```

Throttle: chạy tối đa một lần trong khoảng thời gian.

Use cases:

- Debounce search input.
- Throttle scroll/resize.
- Batch WebSocket updates mỗi 50-100ms.

Realtime trading problem:

```txt
1000 price updates/s
-> setState 1000 lần/s
-> 60+ components render liên tục
-> main thread nghẽn, UI freeze
```

Better:

```txt
Buffer updates
-> flush mỗi 50-100ms
-> update store theo batch
-> components subscribe theo symbol/orderId cần dùng
-> virtualize table
```

### 3.8. 🌐 Server-state caching với React Query/SWR

Server state có đặc điểm:

- Có cache/stale time.
- Có loading/error/refetch.
- Có pagination/infinite query.
- Có optimistic update.
- Có retry và dedup request.

TanStack Query giúp tránh tự viết quá nhiều state/cache:

```tsx
function useOrders() {
  return useQuery({
    queryKey: ["orders"],
    queryFn: fetchOrders,
    staleTime: 30_000,
  });
}
```

Performance wins:

- Giảm duplicate API calls.
- Cache giữa route/components.
- Background refetch.
- Select/transform data có kiểm soát.

### 3.9. 🖼️ Image, font và asset optimization

React performance không chỉ là component render. LCP thường bị ảnh hưởng bởi image/font.

Best practices:

- Dùng `width`/`height` hoặc `aspect-ratio` để tránh CLS.
- Dùng `srcset`/`sizes` cho responsive images.
- Dùng WebP/AVIF khi phù hợp.
- `loading="lazy"` cho ảnh dưới fold.
- `fetchpriority="high"` cho hero image quan trọng.
- Preload font quan trọng, dùng `font-display: swap` hoặc strategy phù hợp.

```html
<img
  src="/hero-800.webp"
  srcset="/hero-400.webp 400w, /hero-800.webp 800w, /hero-1200.webp 1200w"
  sizes="(min-width: 1024px) 800px, 100vw"
  width="800"
  height="500"
  fetchpriority="high"
  alt="Trading dashboard overview"
/>
```

### 3.10. 📊 Metrics và profiling

Core metrics cần nói:

| Metric | Đo gì? | React liên quan thế nào |
|---|---|---|
| LCP | Nội dung lớn nhất hiển thị | Bundle/image/server response ảnh hưởng |
| INP | Độ phản hồi sau tương tác | JS long tasks, render nặng, hydration ảnh hưởng |
| CLS | Layout shift | Image/font/layout không ổn định |
| TTFB | Byte đầu tiên | SSR/server/cache/network |
| Bundle size | JS tải/parse/execute | Code splitting, dependency bloat |

> Lưu ý: FID đã được thay bằng **INP** trong Core Web Vitals hiện tại. Khi phỏng vấn, nên nói INP để thể hiện cập nhật.

Tools:

- React DevTools Profiler.
- Chrome Performance tab.
- Chrome Memory tab.
- Lighthouse/WebPageTest.
- Web Vitals field data.
- Bundle analyzer.
- Production monitoring: Sentry, Datadog, New Relic, custom Web Vitals endpoint.

### 3.11. ⚛️ React 18 Concurrent Features

`useTransition` đánh dấu update không khẩn cấp:

```tsx
const [isPending, startTransition] = React.useTransition();

function onSearch(nextQuery: string) {
  setQuery(nextQuery);

  startTransition(() => {
    setFilteredItems(expensiveSearch(items, nextQuery));
  });
}
```

`useDeferredValue` trì hoãn value cho UI nặng:

```tsx
const deferredQuery = React.useDeferredValue(query);
const results = React.useMemo(
  () => expensiveSearch(items, deferredQuery),
  [items, deferredQuery],
);
```

Ý nghĩa:

- Giữ input/click phản hồi nhanh hơn.
- Không làm computation biến mất, chỉ đổi priority.
- Vẫn cần reduce work nếu work quá nặng.

### 3.12. 🧹 Memory management

Memory leak thường đến từ:

- Event listener không remove.
- Timer/interval không clear.
- WebSocket/subscription không unsubscribe.
- Request cũ update state sau unmount.
- Cache không có eviction.
- Closure giữ data lớn.

Pattern cleanup:

```tsx
React.useEffect(() => {
  const controller = new AbortController();

  fetch("/api/orders", { signal: controller.signal });

  return () => controller.abort();
}, []);
```

WebSocket cleanup:

```tsx
React.useEffect(() => {
  const socket = new WebSocket(url);

  socket.addEventListener("message", handleMessage);

  return () => {
    socket.removeEventListener("message", handleMessage);
    socket.close();
  };
}, [url, handleMessage]);
```

## 4. 🧪 Practical TypeScript/JavaScript Examples

### 4.1. ✅ Before/After: inline object làm memo mất tác dụng

❌ Mỗi render tạo object/function mới:

```tsx
<OrderRow
  order={order}
  style={{ color: "green" }}
  onSelect={() => selectOrder(order.id)}
/>
```

✅ Giữ reference ổn định khi child memoized:

```tsx
const rowStyle = React.useMemo(() => ({ color: "green" }), []);

const handleSelect = React.useCallback(
  (id: string) => {
    selectOrder(id);
  },
  [selectOrder],
);

<OrderRow order={order} style={rowStyle} onSelect={handleSelect} />;
```

Nhưng nếu `OrderRow` không memoized hoặc render rất rẻ, tối ưu này có thể không đáng.

### 4.2. ✅ Debounced search input

```tsx
function SearchBox({ onSearch }: { onSearch: (query: string) => void }) {
  const [query, setQuery] = React.useState("");

  const debouncedSearch = React.useMemo(() => {
    let timer: number | undefined;

    return (value: string) => {
      window.clearTimeout(timer);
      timer = window.setTimeout(() => onSearch(value), 300);
    };
  }, [onSearch]);

  return (
    <input
      value={query}
      onChange={(event) => {
        const nextQuery = event.target.value;
        setQuery(nextQuery);
        debouncedSearch(nextQuery);
      }}
    />
  );
}
```

### 4.3. ✅ Batch WebSocket updates

```tsx
type PriceUpdate = {
  symbol: string;
  price: number;
};

function useBatchedPrices(socket: WebSocket) {
  const [prices, setPrices] = React.useState<Record<string, number>>({});
  const bufferRef = React.useRef<PriceUpdate[]>([]);

  React.useEffect(() => {
    const handleMessage = (event: MessageEvent) => {
      bufferRef.current.push(JSON.parse(event.data) as PriceUpdate);
    };

    const intervalId = window.setInterval(() => {
      const batch = bufferRef.current;
      if (batch.length === 0) return;

      bufferRef.current = [];

      setPrices((prev) => {
        const next = { ...prev };
        for (const update of batch) {
          next[update.symbol] = update.price;
        }
        return next;
      });
    }, 100);

    socket.addEventListener("message", handleMessage);

    return () => {
      socket.removeEventListener("message", handleMessage);
      window.clearInterval(intervalId);
    };
  }, [socket]);

  return prices;
}
```

### 4.4. ✅ Virtualized list concept

```tsx
import { FixedSizeList } from "react-window";

function OrdersList({ orders }: { orders: Order[] }) {
  return (
    <FixedSizeList
      height={600}
      itemCount={orders.length}
      itemSize={48}
      width="100%"
    >
      {({ index, style }) => (
        <div style={style}>
          <OrderRow order={orders[index]} />
        </div>
      )}
    </FixedSizeList>
  );
}
```

### 4.5. ✅ Profiler callback

```tsx
function onRender(
  id: string,
  phase: "mount" | "update" | "nested-update",
  actualDuration: number,
  baseDuration: number,
) {
  console.table({ id, phase, actualDuration, baseDuration });
}

function App() {
  return (
    <React.Profiler id="OrdersTable" onRender={onRender}>
      <OrdersTable />
    </React.Profiler>
  );
}
```

### 4.6. ✅ Code splitting route nặng

```tsx
const AnalyticsPage = React.lazy(() => import("./pages/AnalyticsPage"));

function Routes() {
  return (
    <React.Suspense fallback={<PageSkeleton />}>
      <AnalyticsPage />
    </React.Suspense>
  );
}
```

## 5. 🏭 Production Notes / React Implications

- **Measure first:** Dùng React Profiler và Chrome Performance trước khi thêm memoization.
- **State colococation:** Đặt state gần nơi dùng để giảm render tree bị ảnh hưởng.
- **Context splitting:** Tách context theo tần suất đổi, tránh một Provider chứa mọi thứ.
- **Server state:** Dùng React Query/SWR cho API data, cache, retry, pagination.
- **Bundle budget:** Set budget trong CI, phân tích dependency lớn như chart/editor/date libraries.
- **Realtime UI:** Batch updates, selective subscription, virtualization, backpressure.
- **SSR/hydration:** SSR giúp content sớm hơn nhưng hydration JS vẫn ảnh hưởng INP.
- **Accessibility:** Virtualized list cần xử lý keyboard navigation, focus, screen reader expectations.
- **Memory:** Cleanup mọi subscription/timer/listener/request; profile heap cho app chạy lâu.
- **Observability:** Gửi Web Vitals và render/interaction metrics từ production, không chỉ đo local.

## 6. ⚠️ Common Pitfalls

- ❌ Dùng `useMemo/useCallback` khắp nơi mà không đo bottleneck.
- ❌ Truyền object/function inline vào memoized child rồi thắc mắc child vẫn render.
- ❌ Context value chứa object mới mỗi render làm toàn bộ consumers render lại.
- ❌ Dùng index làm key cho list động.
- ❌ Render 10k rows thay vì virtualization/pagination.
- ❌ Filter/sort data lớn trực tiếp trong render mà không memo/cache.
- ❌ WebSocket setState từng message.
- ❌ Không cleanup `useEffect`: timer, listener, WebSocket, request.
- ❌ Chỉ tối ưu React render nhưng bỏ qua image/font/layout/browser work.
- ❌ Bundle nặng do import cả library khi chỉ cần một phần.
- ❌ Tin Lighthouse local là đủ, không đo field data/real devices.
- ❌ So sánh deep trong `React.memo` custom comparator quá đắt.

## 7. ✅ Decision Guide or Checklist

### Chọn kỹ thuật nào?

| Vấn đề | Kỹ thuật | Trả lời ngắn |
|---|---|---|
| Initial load chậm | Code splitting, bundle analyzer | Giảm JS tải/parse/execute ban đầu. |
| Route nặng ít dùng | `React.lazy` + Suspense | Chỉ tải khi vào route đó. |
| Child render lại do parent | `React.memo` + stable props | Hữu ích nếu child render đắt. |
| Tính toán filter/sort lớn | `useMemo` hoặc cache derived data | Tránh tính lại khi input không đổi. |
| Callback làm child memo fail | `useCallback` | Giữ function reference ổn định. |
| Context gây render rộng | Split context/selectors | Chỉ consumer cần thiết render lại. |
| List/table lớn | Virtualization/pagination | Giảm DOM nodes và render cost. |
| Input search gọi API liên tục | Debounce | Chờ user ngừng gõ rồi fetch. |
| Scroll/resize handler nặng | Throttle/rAF | Giới hạn tần suất xử lý. |
| Realtime updates quá nhiều | Batch + selective subscription | Không setState từng message. |
| Memory tăng theo thời gian | Cleanup + heap snapshot | Tìm listener/cache/request leak. |
| INP xấu | Reduce JS long tasks, transition/defer | Giữ interaction responsive. |

### Checklist trước khi tối ưu

| Câu hỏi | Trả lời ngắn |
|---|---|
| Bottleneck là network, JS, render hay layout? | Đo bằng DevTools/Profiler trước. |
| Component nào render chậm nhất? | Xem React Profiler `actualDuration`. |
| State có đặt quá cao không? | Colocate hoặc split state nếu được. |
| Props của memoized child có ổn định không? | Tránh object/function inline khi cần memo. |
| Context value có đổi quá thường xuyên không? | Split context hoặc dùng selector store. |
| List có quá nhiều DOM nodes không? | Dùng virtualization/pagination. |
| Bundle có dependency lớn không? | Dùng bundle analyzer và dynamic import. |
| API data có cache/stale strategy chưa? | Dùng React Query/SWR hoặc cache layer rõ. |
| Effects có cleanup đầy đủ không? | Clear timer, remove listener, abort request. |
| Metrics production có xác nhận cải thiện không? | Theo dõi LCP/INP/CLS và user timing. |

## 8. 🗣️ Short Interview Answer

Theo em, tối ưu React performance phải bắt đầu bằng đo đạc. Em sẽ dùng React Profiler để xem component nào render chậm, Chrome Performance để xem main thread/layout/paint, bundle analyzer để xem JS nặng, và Web Vitals như LCP, INP, CLS để biết user thật bị ảnh hưởng ở đâu.

Nếu vấn đề là initial load, em xử lý bundle: code splitting, lazy route, tree-shaking, giảm dependency lớn và tối ưu image/font. Nếu vấn đề là runtime render, em xem state đặt có quá cao không, context có làm render rộng không, list có cần virtualization không, props có phá `React.memo` không. Em dùng `useMemo` cho derived data đắt, `useCallback` khi cần stable callback cho memoized child, nhưng không lạm dụng.

Với app realtime như trading platform, em sẽ batch WebSocket updates, dùng selective subscription theo symbol/order, virtualize table và cleanup subscription để tránh memory leak. Điểm quan trọng là mỗi tối ưu phải gắn với bottleneck thật và có metric xác nhận, không tối ưu theo cảm giác.

## 9. 🧾 Ghi nhớ nhanh

- Đo trước, tối ưu sau.
- `React.memo` shallow compare props, không phải thuốc chữa mọi re-render.
- `useMemo` cache value; `useCallback` cache function reference.
- Object/function inline phá memo nếu child phụ thuộc reference equality.
- Context update có thể re-render nhiều consumer.
- Large list cần virtualization/pagination.
- Realtime updates cần batching/selective subscription.
- Server-state nên có cache như React Query/SWR.
- Bundle size ảnh hưởng load, parse, execute và INP.
- Image/font cũng ảnh hưởng LCP/CLS.
- Cleanup effect để tránh memory leak.
- INP là metric hiện tại thay cho FID trong Core Web Vitals.

## 10. 📖 Giải thích các thuật ngữ trong topic

- `Re-render`: Component function chạy lại để tạo React elements mới.
- `Commit`: Giai đoạn React áp dụng thay đổi vào DOM.
- `Reconciliation`: Quá trình React so sánh tree mới/cũ.
- `Reference equality`: Object/function/array chỉ bằng nhau nếu cùng reference.
- `Shallow comparison`: So sánh một tầng property/reference, không deep compare.
- `React.memo`: HOC giúp skip render nếu props shallow-equal.
- `useMemo`: Hook cache kết quả tính toán.
- `useCallback`: Hook cache function reference.
- `Virtualization`: Chỉ render item đang visible trong list lớn.
- `Debounce`: Chờ sự kiện ngừng một khoảng mới chạy.
- `Throttle`: Giới hạn function chạy tối đa theo chu kỳ.
- `Server state`: Data đến từ server, cần cache/refetch/stale handling.
- `Client state`: State thuần UI như modal, selected tab, draft input.
- `Code splitting`: Chia bundle để tải code theo nhu cầu.
- `Tree-shaking`: Loại bỏ code không dùng khi build.
- `Bundle budget`: Giới hạn kích thước bundle được phép.
- `LCP`: Largest Contentful Paint, đo nội dung chính hiển thị.
- `INP`: Interaction to Next Paint, đo độ phản hồi tương tác.
- `CLS`: Cumulative Layout Shift, đo layout shift ngoài ý muốn.
- `Profiler`: Công cụ đo thời gian render React component.
- `Memory leak`: Bộ nhớ không được giải phóng do còn reference/listener/cache.
