# 📊 Q67: Data Visualization - Charts, Canvas, Real-time Data & Performance

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"Data visualization là biểu diễn dữ liệu visual để user hiểu nhanh. 3 cách chính:**
// 💡 Data visualization: Trực quan hóa dữ liệu (Data visualization)
// 💡 biểu diễn dữ liệu visual: Hiển thị dữ liệu dạng hình ảnh (Display data visually)
// 💡 user hiểu nhanh: User hiểu nhanh hơn (User understands faster)
// 💡 3 cách chính: 3 phương pháp chính (3 main methods)

- **SVG (Recharts, ECharts)** - declarative, semantic, flexible (good for 100-1000 points)
  // 💡 SVG: Scalable Vector Graphics (Scalable Vector Graphics)
  // 💡 Recharts, ECharts: Libraries dùng SVG (Libraries using SVG)
  // 💡 declarative: Khai báo, dễ đọc (Declarative, easy to read)
  // 💡 semantic: Có ý nghĩa, dễ hiểu (Semantic, easy to understand)
  // 💡 flexible: Linh hoạt (Flexible)
  // 💡 good for 100-1000 points: Tốt cho 100-1000 điểm (Good for 100-1000 points)

- **Canvas (Visx, Plotly)** - imperative, fast, memory-efficient (good for 10k+ points)
  // 💡 Canvas: HTML5 Canvas element (HTML5 Canvas element)
  // 💡 Visx, Plotly: Libraries dùng Canvas (Libraries using Canvas)
  // 💡 imperative: Mệnh lệnh, code trực tiếp (Imperative, direct code)
  // 💡 fast: Nhanh (Fast)
  // 💡 memory-efficient: Tiết kiệm bộ nhớ (Memory efficient)
  // 💡 good for 10k+ points: Tốt cho 10k+ điểm (Good for 10k+ points)

- **WebGL (Three.js, Babylon.js)** - ultra-fast for millions of points
  // 💡 WebGL: Web Graphics Library (Web Graphics Library)
  // 💡 Three.js, Babylon.js: Libraries dùng WebGL (Libraries using WebGL)
  // 💡 ultra-fast: Cực kỳ nhanh (Ultra fast)
  // 💡 for millions of points: Cho hàng triệu điểm (For millions of points)

**Tôi đã implement real-time trading dashboard với 50K data points:**
// 💡 implement: Triển khai (Implement)
// 💡 real-time trading dashboard: Dashboard giao dịch real-time (Real-time trading dashboard)
// 💡 50K data points: 50 nghìn điểm dữ liệu (50 thousand data points)

- **ECharts** cho static charts (order book, price history)
  // 💡 ECharts: Library visualization (Visualization library)
  // 💡 static charts: Biểu đồ tĩnh (Static charts)
  // 💡 order book: Sổ lệnh (Order book)
  // 💡 price history: Lịch sử giá (Price history)

- **Canvas rendering** (Visx + D3) cho live tick updates (1000 updates/sec)
  // 💡 Canvas rendering: Render bằng Canvas (Rendering with Canvas)
  // 💡 Visx + D3: Libraries visualization (Visualization libraries)
  // 💡 live tick updates: Cập nhật tick real-time (Real-time tick updates)
  // 💡 1000 updates/sec: 1000 cập nhật/giây (1000 updates per second)

- **WebWorker** offload data aggregation → 60fps smooth
  // 💡 WebWorker: Background thread (Background thread)
  // 💡 offload: Chuyển công việc sang worker (Offload work to worker)
  // 💡 data aggregation: Tổng hợp dữ liệu (Data aggregation)
  // 💡 60fps smooth: Mượt 60 khung hình/giây (Smooth 60 frames per second)

- **Virtual scrolling** cho large datasets → render only visible rows
  // 💡 Virtual scrolling: Cuộn ảo (Virtual scrolling)
  // 💡 large datasets: Datasets lớn (Large datasets)
  // 💡 render only visible rows: Chỉ render các hàng hiển thị (Only render visible rows)
  // 💡 Tối ưu performance (Optimize performance)

- **Decimation algorithm** (LTTB - Largest Triangle Three Buckets) → 50K → 1K points (visual quality preserved)
  // 💡 Decimation algorithm: Thuật toán giảm mẫu (Decimation algorithm)
  // 💡 LTTB: Largest Triangle Three Buckets (Largest Triangle Three Buckets)
  // 💡 50K → 1K points: Giảm từ 50K xuống 1K điểm (Reduce from 50K to 1K points)
  // 💡 visual quality preserved: Chất lượng hình ảnh được giữ nguyên (Visual quality preserved)

- **Result**: 60fps smooth, < 100ms latency for data update → visual change\*\*
  // 💡 Result: Kết quả (Result)
  // 💡 60fps smooth: Mượt 60fps (Smooth 60fps)
  // 💡 < 100ms latency: Độ trễ < 100ms (Latency < 100ms)
  // 💡 data update → visual change: Cập nhật dữ liệu → thay đổi hình ảnh (Data update → visual change)

**Key considerations:** (Các Lưu Ý Quan Trọng)
// 💡 Key considerations: Các điểm cần lưu ý (Important considerations)
// 💡 Trade-offs giữa các phương pháp (Trade-offs between methods)

- **SVG**: Good for interactions (zoom, tooltip), bad for large datasets (DOM overhead)
  // 💡 SVG: Scalable Vector Graphics (Scalable Vector Graphics)
  // 💡 Good for interactions: Tốt cho tương tác (Good for interactions)
  // 💡 zoom, tooltip: Phóng to, tooltip (Zoom, tooltip)
  // 💡 bad for large datasets: Không tốt cho datasets lớn (Bad for large datasets)
  // 💡 DOM overhead: Chi phí DOM (DOM overhead)
  // 💡 Mỗi element là DOM node (Each element is DOM node)

- **Canvas**: Bad for interactions, good for performance, hard to debug
  // 💡 Canvas: HTML5 Canvas (HTML5 Canvas)
  // 💡 Bad for interactions: Không tốt cho tương tác (Bad for interactions)
  // 💡 good for performance: Tốt cho hiệu suất (Good for performance)
  // 💡 hard to debug: Khó debug (Hard to debug)
  // 💡 Pixel-based, không có DOM elements (Pixel-based, no DOM elements)

- **Hybrid**: Canvas background + SVG overlay (best of both)
  // 💡 Hybrid: Kết hợp (Hybrid)
  // 💡 Canvas background: Nền Canvas (Canvas background)
  // 💡 SVG overlay: Lớp phủ SVG (SVG overlay)
  // 💡 best of both: Tốt nhất của cả hai (Best of both)
  // 💡 Canvas cho performance, SVG cho interactions (Canvas for performance, SVG for interactions)

- **Real-time**: Use WebWorkers, decimation, virtual scrolling, canvas rendering
  // 💡 Real-time: Real-time updates (Real-time updates)
  // 💡 Use WebWorkers: Dùng WebWorkers (Use WebWorkers)
  // 💡 decimation: Giảm mẫu (Decimation)
  // 💡 virtual scrolling: Cuộn ảo (Virtual scrolling)
  // 💡 canvas rendering: Render bằng Canvas (Rendering with Canvas)
  // 💡 Tối ưu cho real-time (Optimize for real-time)

---

## **📋 GIẢI THÍCH CHI TIẾT CẤP SENIOR/STAFF**

### **⚖️ 1️⃣ SVG vs Canvas Trade-offs (So Sánh SVG và Canvas)**

**🎯 Mục đích**: Hiểu rõ khi nào dùng SVG, khi nào dùng Canvas
// 💡 SVG: Tốt cho interactions, không tốt cho datasets lớn
// 💡 Canvas: Tốt cho performance, không tốt cho interactions
// 💡 Quan trọng: Chọn đúng tool cho đúng use case

#### **🖼️ 1.1 SVG (Scalable Vector Graphics)**

```
// ============================================
// ✅ ƯU ĐIỂM CỦA SVG
// ============================================
✅ ADVANTAGES:
├─ DOM elements → Easy interaction (click, hover, tooltip)
│  💡 Mỗi element là DOM node → dễ dàng thêm event listeners
│  💡 Click, hover, tooltip hoạt động tự nhiên
│
├─ Semantic HTML → Good for accessibility
│  💡 Screen readers có thể đọc được
│  💡 WCAG compliance dễ dàng hơn
│
├─ Scalable → Sharp at any resolution
│  💡 Vector graphics → không bị mờ khi zoom
│  💡 Perfect cho Retina displays
│
├─ Easy to debug → Inspect in DevTools
│  💡 Có thể inspect từng element trong DevTools
│  💡 Dễ tìm bug, dễ style
│
├─ CSS styling → Style with CSS
│  💡 Có thể dùng CSS để style
│  💡 Responsive design dễ dàng
│
└─ Transformations → Easy zoom/pan/scale
   💡 CSS transforms hoạt động tốt
   💡 Zoom/pan dễ implement

// ============================================
// ❌ NHƯỢC ĐIỂM CỦA SVG
// ============================================
❌ DISADVANTAGES:
├─ DOM overhead → Slower with 1000+ elements
│  💡 Mỗi element là DOM node → tốn memory
│  💡 Browser phải quản lý nhiều DOM nodes
│
├─ Memory intensive → Each element is separate DOM node
│  💡 1000 points = 1000 DOM nodes
│  💡 Memory usage tăng nhanh
│
├─ Rendering cost → Browser has to render each shape
│  💡 Browser phải render từng shape
│  💡 Re-render tốn kém khi update
│
├─ Not ideal for: Real-time data, high-frequency updates
│  💡 Không phù hợp cho real-time updates
│  💡 Quá chậm cho high-frequency updates
│
└─ Performance degrades → Exponential slowdown past 1000 points
   💡 Performance giảm nhanh khi > 1000 points
   💡 Exponential slowdown → không linear

// ============================================
// 📊 PERFORMANCE METRICS
// ============================================
📊 Performance:
└─ 100 points: ✅ Smooth (16ms)
   💡 100 điểm → render trong 16ms → 60fps mượt mà

   500 points: ⚠️ Acceptable (50-100ms)
   💡 500 điểm → render trong 50-100ms → vẫn chấp nhận được
   💡 Nhưng đã bắt đầu chậm

   1000+ points: ❌ Laggy (>200ms)
   💡 1000+ điểm → render > 200ms → lag rõ ràng
   💡 User cảm thấy app bị đơ
   💡 Nên dùng Canvas thay vì SVG
```

**💻 SVG Implementation (ECharts/Recharts):**

```typescript
// ECharts example - Good for static/infrequent updates (Ví dụ ECharts - Tốt cho static/ít cập nhật)
// 💡 ECharts: Library visualization mạnh mẽ (Powerful visualization library)
// 💡 Good for: Static charts, infrequent updates (Tốt cho: Static charts, ít cập nhật)
import * as echarts from 'echarts';
// 💡 echarts: Import ECharts library (Import ECharts library)

const chart = echarts.init(document.getElementById('chart'));
// 💡 echarts.init: Khởi tạo chart instance (Initialize chart instance)
// 💡 document.getElementById('chart'): DOM element để render chart (DOM element to render chart)
// 💡 chart: Chart instance để config và update (Chart instance to config and update)

const option = {
  // 💡 option: Cấu hình chart (Chart configuration)
  xAxis: { type: 'category', data: ['Mon', 'Tue', 'Wed', ...] },
  // 💡 xAxis: Trục X (X axis)
  // 💡 type: 'category': Dữ liệu dạng category (Category data type)
  // 💡 data: Labels cho trục X (Labels for X axis)

  yAxis: { type: 'value' },
  // 💡 yAxis: Trục Y (Y axis)
  // 💡 type: 'value': Dữ liệu dạng số (Numeric data type)

  series: [
    // 💡 series: Dữ liệu để vẽ (Data to draw)
    {
      data: [120, 200, 150, 80, ...],
      // ✅ 1000 data points (1000 điểm dữ liệu)
      // 💡 data: Array các giá trị (Array of values)
      // 💡 1000 points: Có thể xử lý được với SVG (Can handle with SVG)

      type: 'line',
      // 💡 type: 'line': Line chart (Biểu đồ đường)
      // 💡 Các loại khác: 'bar', 'pie', 'scatter' (Other types: 'bar', 'pie', 'scatter')

      smooth: true,
      // 💡 smooth: Làm mượt đường (Smooth line)
      // 💡 true: Đường cong mượt (Smooth curve)

      symbolSize: 4,
      // 💡 symbolSize: Kích thước điểm (Point size)
      // 💡 4: Kích thước nhỏ (Small size)

      // ✅ ECharts handles SVG rendering internally (ECharts xử lý SVG rendering bên trong)
      // 💡 ECharts tự động render bằng SVG (ECharts automatically renders with SVG)
      // 💡 Không cần code SVG manually (No need to code SVG manually)
    },
  ],
};

chart.setOption(option);
// 💡 setOption: Set cấu hình chart (Set chart configuration)
// 💡 option: Config object (Config object)
// 💡 Chart sẽ render theo config (Chart will render according to config)

// ✅ Easy interactions (Tương tác dễ dàng)
chart.on('click', (params) => {
  // 💡 on('click'): Event listener cho click (Event listener for click)
  // 💡 params: Thông tin về điểm được click (Info about clicked point)
  console.log('Clicked:', params);
  // 💡 Log thông tin điểm được click (Log clicked point info)
  // 💡 params.dataIndex: Index của điểm (Point index)
  // 💡 params.value: Giá trị của điểm (Point value)
});
// 💡 SVG: Dễ dàng thêm interactions (SVG: Easy to add interactions)
// 💡 Mỗi điểm là DOM element → có thể click (Each point is DOM element → can click)

// ⚠️ Problem: Updating 1000+ points frequently (Vấn đề: Cập nhật 1000+ điểm thường xuyên)
setInterval(() => {
  // 💡 setInterval: Lặp lại mỗi 100ms (Repeat every 100ms)
  const newData = generateNewData();
  // ✅ 1000 points (1000 điểm)
  // 💡 generateNewData: Tạo data mới (Generate new data)
  // 💡 1000 points: Số lượng điểm (Number of points)

  chart.setOption({
    // ⚠️ Slow update (100-200ms) (Cập nhật chậm)
    // 💡 setOption: Update chart với data mới (Update chart with new data)
    // 💡 100-200ms: Thời gian update (Update time)
    // 💡 SVG: Phải re-render tất cả DOM elements (SVG: Must re-render all DOM elements)
    series: [{ data: newData }],
    // 💡 Update series data (Cập nhật dữ liệu series)
  });
}, 100);
// ⚠️ Can't refresh 10x/second with SVG (Không thể refresh 10 lần/giây với SVG)
// 💡 100ms = 10 updates/second (100ms = 10 updates/second)
// 💡 SVG quá chậm cho real-time updates (SVG too slow for real-time updates)
// 💡 Nên dùng Canvas cho real-time (Should use Canvas for real-time)
```

#### **🎨 1.2 Canvas (Raster Graphics)**

```
// ============================================
// ✅ ƯU ĐIỂM CỦA CANVAS
// ============================================
✅ ADVANTAGES:
├─ Fast rendering → Native GPU acceleration possible
│  💡 Render nhanh hơn SVG rất nhiều
│  💡 Có thể dùng GPU acceleration
│  💡 Browser optimize tốt hơn
│
├─ Memory efficient → Pixel data, not DOM nodes
│  💡 Chỉ lưu pixel data, không phải DOM nodes
│  💡 Memory usage thấp hơn SVG rất nhiều
│  💡 1M points vẫn OK về memory
│
├─ Handles large datasets → Millions of points possible
│  💡 Có thể xử lý hàng triệu điểm
│  💡 SVG không thể làm được điều này
│
├─ Smooth animations → 60fps with 10k+ points
│  💡 60fps mượt mà ngay cả với 10k+ points
│  💡 SVG chỉ đạt 60fps với < 1000 points
│
├─ Perfect for: Real-time data, high-frequency updates
│  💡 Hoàn hảo cho real-time data
│  💡 Có thể update 1000 lần/giây
│
└─ WebGL capable → Ultra-fast with GPU
   💡 Có thể dùng WebGL → cực kỳ nhanh
   💡 GPU rendering → xử lý hàng triệu points

// ============================================
// ❌ NHƯỢC ĐIỂM CỦA CANVAS
// ============================================
❌ DISADVANTAGES:
├─ No DOM elements → Hard to interact (no native click events)
│  💡 Không có DOM elements → không có native click events
│  💡 Phải tự implement hit detection
│  💡 Phức tạp hơn SVG rất nhiều
│
├─ Pixel-based → Blurry at high DPI / when scaled
│  💡 Pixel-based → có thể bị mờ khi zoom
│  💡 SVG vector → không bao giờ bị mờ
│
├─ Hard to debug → "What pixel did I draw?"
│  💡 Khó debug → không biết pixel nào được vẽ
│  💡 SVG: Có thể inspect trong DevTools
│
├─ Requires manual event handling → Complex tooltip/zoom logic
│  💡 Phải tự implement tooltip, zoom
│  💡 SVG: Built-in support
│
├─ No semantic HTML → Bad for accessibility
│  💡 Không có semantic HTML
│  💡 Screen readers không đọc được
│
└─ More code → Need to manage rendering pipeline
   💡 Cần nhiều code hơn
   💡 Phải tự quản lý rendering pipeline

// ============================================
// 📊 PERFORMANCE METRICS
// ============================================
📊 Performance:
└─ 10k points: ✅ Smooth (16ms)
   💡 10k điểm → render trong 16ms → 60fps mượt mà
   💡 SVG không thể làm được điều này

   100k points: ✅ Smooth with optimization
   💡 100k điểm → vẫn mượt với optimization
   💡 Cần decimation, batching

   1M points: ⚠️ Possible but need decimation
   💡 1M điểm → có thể nhưng cần decimation
   💡 Giảm xuống ~10k points để render
   💡 Visual quality vẫn được giữ nguyên
```

**🖥️ Canvas Implementation (Visx + D3):**

```typescript
// Canvas example - Good for real-time, large datasets (Ví dụ Canvas - Tốt cho real-time, datasets lớn)
// 💡 Canvas: Raster graphics, nhanh hơn SVG (Raster graphics, faster than SVG)
// 💡 Good for: Real-time data, large datasets (Tốt cho: Real-time data, datasets lớn)
import { ScaleLinear, scaleLinear } from 'd3-scale';
// 💡 d3-scale: D3 library để tạo scales (D3 library to create scales)
// 💡 scaleLinear: Linear scale để map data → pixel coordinates (Linear scale to map data → pixel coordinates)

import { useRef, useEffect } from 'react';
// 💡 useRef: React hook để reference DOM element (React hook to reference DOM element)
// 💡 useEffect: React hook để side effects (React hook for side effects)

export function RealTimeChart({ data }: { data: number[] }) {
  // 💡 RealTimeChart: Component cho real-time chart (Component for real-time chart)
  // 💡 data: Array các giá trị (Array of values)
  // 💡 number[]: TypeScript type (TypeScript type)

  const canvasRef = useRef<HTMLCanvasElement>(null);
  // 💡 canvasRef: Reference đến canvas element (Reference to canvas element)
  // 💡 useRef<HTMLCanvasElement>: Type-safe ref (Type-safe ref)
  // 💡 null: Initial value (Giá trị ban đầu)

  useEffect(() => {
    // 💡 useEffect: Hook để render canvas (Hook to render canvas)
    // 💡 Chạy khi component mount hoặc data thay đổi (Runs when component mounts or data changes)
    const canvas = canvasRef.current;
    // 💡 canvas: Canvas element (Canvas element)
    if (!canvas) return;
    // 💡 Early return nếu canvas không tồn tại (Early return if canvas doesn't exist)

    const ctx = canvas.getContext('2d');
    // 💡 getContext('2d'): Lấy 2D rendering context (Get 2D rendering context)
    // 💡 ctx: Context để vẽ lên canvas (Context to draw on canvas)
    if (!ctx) return;
    // 💡 Early return nếu không lấy được context (Early return if can't get context)

    // Setup canvas (Thiết lập canvas)
    const width = canvas.width;
    // 💡 width: Chiều rộng canvas (Canvas width)
    const height = canvas.height;
    // 💡 height: Chiều cao canvas (Canvas height)
    const padding = 40;
    // 💡 padding: Khoảng cách từ edge (Distance from edge)
    // 💡 40px: Padding cho axes labels (Padding for axes labels)

    // Clear canvas (Xóa canvas)
    ctx.fillStyle = '#fff';
    // 💡 fillStyle: Màu fill (Fill color)
    // 💡 '#fff': Màu trắng (White color)
    ctx.fillRect(0, 0, width, height);
    // 💡 fillRect: Vẽ hình chữ nhật (Draw rectangle)
    // 💡 0, 0: Vị trí bắt đầu (Start position)
    // 💡 width, height: Kích thước (Size)
    // 💡 Xóa canvas trước khi vẽ mới (Clear canvas before drawing new)

    // Scales (Tỷ lệ)
    const xScale = scaleLinear()
      // 💡 scaleLinear: Tạo linear scale (Create linear scale)
      .domain([0, data.length])
      // 💡 domain: Phạm vi dữ liệu (Data range)
      // 💡 [0, data.length]: Từ 0 đến số lượng data points (From 0 to number of data points)
      .range([padding, width - padding]);
    // 💡 range: Phạm vi pixel (Pixel range)
    // 💡 [padding, width - padding]: Từ padding đến width - padding (From padding to width - padding)
    // 💡 Map data index → x coordinate (Map data index → x coordinate)

    const yScale = scaleLinear()
      .domain([0, Math.max(...data)])
      .range([height - padding, padding]);

    // Draw grid
    ctx.strokeStyle = '#eee';
    ctx.lineWidth = 1;
    for (let i = 0; i < 10; i++) {
      const y = (height - 2 * padding) * (i / 10) + padding;
      ctx.beginPath();
      ctx.moveTo(padding, y);
      ctx.lineTo(width - padding, y);
      ctx.stroke();
    }

    // Draw line chart
    ctx.strokeStyle = '#1f77b4';
    ctx.lineWidth = 2;
    ctx.beginPath();

    data.forEach((value, i) => {
      const x = xScale(i);
      const y = yScale(value);

      if (i === 0) {
        ctx.moveTo(x, y);
      } else {
        ctx.lineTo(x, y);
      }
    });

    ctx.stroke();

    // Draw points
    ctx.fillStyle = '#1f77b4';
    data.forEach((value, i) => {
      const x = xScale(i);
      const y = yScale(value);
      ctx.beginPath();
      ctx.arc(x, y, 3, 0, Math.PI * 2);
      ctx.fill();
    });

    // ✅ Fast: Even with 10k points, this runs in <16ms
  }, [data]);

  return <canvas ref={canvasRef} width={800} height={400} />;
}

// ⚠️ Manual event handling for interactivity
function ChartWithTooltip() {
  const [hoveredPoint, setHoveredPoint] = useState<number | null>(null);

  const handleMouseMove = (e: React.MouseEvent<HTMLCanvasElement>) => {
    const canvas = e.currentTarget;
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    // 🚨 Manual hit detection
    const pointIndex = findNearestPoint(x, y, data, scales);
    setHoveredPoint(pointIndex);
  };

  return (
    <>
      <canvas onMouseMove={handleMouseMove} />
      {hoveredPoint !== null && (
        <Tooltip x={x} y={y} data={data[hoveredPoint]} />
      )}
    </>
  );
}
```

#### **🧭 1.3 When to Use Which? (Khi Nào Dùng Cái Nào?)**

```
// ============================================
// 🎯 HƯỚNG DẪN CHỌN VISUALIZATION LIBRARY
// ============================================
┌──────────────────────────────────────────────────────────┐
│              CHOOSE VISUALIZATION LIBRARY                │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  📊 SVG-Based (Recharts, ECharts, Nivo)                │
│  ├─ < 1000 data points                                  │
│  │  💡 Dưới 1000 điểm → SVG vẫn mượt                    │
│  │  💡 > 1000 điểm → nên dùng Canvas                    │
│  │                                                       │
│  ├─ Need rich interactions (tooltip, zoom, drill-down)  │
│  │  💡 Cần nhiều tương tác → SVG tốt hơn                │
│  │  💡 Tooltip, zoom, drill-down dễ implement          │
│  │                                                       │
│  ├─ Static or slow updates (< 1/second)                │
│  │  💡 Static hoặc update chậm → SVG OK                 │
│  │  💡 Real-time updates → nên dùng Canvas             │
│  │                                                       │
│  ├─ Need accessibility (WCAG compliance)                │
│  │  💡 Cần accessibility → SVG tốt hơn                  │
│  │  💡 Screen readers đọc được SVG                      │
│  │                                                       │
│  └─ Example: Dashboard with 20 charts, 500 points each  │
│     💡 Dashboard với nhiều charts nhỏ                    │
│     💡 Mỗi chart 500 điểm → SVG perfect                 │
│                                                          │
│  🎨 Canvas-Based (Visx + D3, Plotly, Apache ECharts WebGL)
│  ├─ > 10k data points                                   │
│  │  💡 Trên 10k điểm → Canvas bắt buộc                  │
│  │  💡 SVG không thể xử lý được                          │
│  │                                                       │
│  ├─ Real-time updates (frequent, high-frequency)         │
│  │  💡 Real-time updates → Canvas tốt hơn               │
│  │  💡 Có thể update 1000 lần/giây                      │
│  │                                                       │
│  ├─ Smooth animations (60fps)                           │
│  │  💡 Cần 60fps mượt mà → Canvas                       │
│  │  💡 SVG chỉ đạt 60fps với < 1000 points              │
│  │                                                       │
│  ├─ Performance critical                                │
│  │  💡 Performance là ưu tiên → Canvas                 │
│  │  💡 Trading dashboard, real-time monitoring         │
│  │                                                       │
│  └─ Example: Live stock ticker with 50k points/second    │
│     💡 Live stock ticker với 50k điểm/giây              │
│     💡 Canvas là lựa chọn duy nhất                       │
│                                                          │
│  🚀 WebGL (Three.js, Babylon.js, Cesium)               │
│  ├─ > 1M data points                                    │
│  │  💡 Trên 1M điểm → cần WebGL                         │
│  │  💡 Canvas cũng không đủ nhanh                       │
│  │                                                       │
│  ├─ 3D visualization                                    │
│  │  💡 3D visualization → WebGL                         │
│  │  💡 Canvas chỉ hỗ trợ 2D                             │
│  │                                                       │
│  ├─ Geographic data (maps)                              │
│  │  💡 Maps với nhiều markers → WebGL                    │
│  │  💡 Cesium cho 3D maps                               │
│  │                                                       │
│  └─ Example: Visualize 1M atoms in 3D space             │
│     💡 Visualize 1M atoms trong không gian 3D           │
│     💡 WebGL là lựa chọn duy nhất                        │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

### **📈 2️⃣ ECHARTS - Popular SVG Library**

**🎯 Mục đích**: Hướng dẫn sử dụng ECharts - library visualization phổ biến
// 💡 ECharts: Library mạnh mẽ, dễ sử dụng
// 💡 Hỗ trợ nhiều loại charts: line, bar, pie, scatter, etc.
// 💡 Tốt cho: Dashboards, business charts, static data

#### **🛠️ 2.1 ECharts Setup & Basic Usage**

```typescript
// ============================================
// 📦 ECHARTS SETUP (Cài Đặt ECharts)
// ============================================
// echarts-setup.ts
import * as echarts from 'echarts';
// 💡 echarts: Import ECharts library
// 💡 npm install echarts

export function initChart(elementId: string, option: echarts.EChartsOption) {
  // ============================================
  // 🎨 INITIALIZE CHART (Khởi Tạo Chart)
  // ============================================
  // Initialize chart
  const chart = echarts.init(document.getElementById(elementId));
  // 💡 echarts.init: Khởi tạo chart instance
  // 💡 elementId: ID của DOM element để render chart
  // 💡 chart: Chart instance để config và update

  // Set option
  chart.setOption(option);
  // 💡 setOption: Set cấu hình chart
  // 💡 option: Config object chứa data, style, etc.

  // Handle resize
  window.addEventListener('resize', () => {
    chart.resize();
    // 💡 resize: Tự động resize chart khi window resize
    // 💡 Responsive chart → tự động fit container
  });

  return chart;
  // 💡 Return chart instance để dùng sau
}

// Usage: Line chart with 1000 data points
const option: echarts.EChartsOption = {
  title: { text: 'Stock Price' },

  tooltip: {
    trigger: 'axis',
    formatter: '{b}: ${c}', // Format tooltip
  },

  legend: { data: ['AAPL'] },

  xAxis: {
    type: 'category',
    data: generateDates(1000), // 1000 dates
    boundaryGap: false,
  },

  yAxis: {
    type: 'value',
    min: 150,
    max: 180,
  },

  series: [
    {
      name: 'AAPL',
      type: 'line',
      data: generateStockPrices(1000), // 1000 prices
      smooth: true,
      areaStyle: { color: 'rgba(31, 119, 180, 0.2)' },
      itemStyle: { color: '#1f77b4' },
      lineStyle: { width: 2 },
      symbolSize: 0, // Hide points for cleaner look
    },
  ],
};

const chart = initChart('chart-container', option);
```

#### **⏱️ 2.2 Real-time Updates (Batched) - Cập Nhật Real-time (Gộp Lô)**

```typescript
// ============================================
// ❌ CÁCH TỆ - Update Mỗi Lần Nhận Data
// ============================================
// Real-time update - BAD way ❌
setInterval(() => {
  const newPoint = generatePrice();
  chart.setOption({
    series: [{ data: [...currentData, newPoint] }],
    // ⚠️ Full update every 100ms
    // 💡 VẤN ĐỀ: Update toàn bộ chart mỗi 100ms
    // 💡 setOption: Re-render toàn bộ chart → tốn kém
    // 💡 Performance: Chậm, lag, không mượt
  });
}, 100);
// 💡 Update 10 lần/giây → quá nhiều
// 💡 Mỗi lần update → re-render toàn bộ → lag

// ============================================
// ✅ CÁCH TỐT - Batch Updates (Gộp Lô)
// ============================================
// Real-time update - GOOD way ✅ (Batched)
const updateQueue: number[] = [];
// 💡 updateQueue: Queue để lưu các updates
// 💡 Collect updates → batch update → hiệu quả hơn

setInterval(() => {
  // Collect updates for 100ms
  updateQueue.push(generatePrice());
  // 💡 Collect mỗi 10ms → lưu vào queue
  // 💡 Không update chart ngay → chỉ collect
}, 10); // Collect every 10ms
// 💡 Collect 100 lần/giây → nhưng không update chart

setInterval(() => {
  if (updateQueue.length > 0) {
    // Batch update once every 100ms
    chart.appendData({
      seriesIndex: 0,
      data: updateQueue.splice(0), // Clear queue
      // ✅ appendData: Chỉ thêm data mới, không re-render toàn bộ
      // 💡 Hiệu quả hơn setOption rất nhiều
      // 💡 Performance: Nhanh, mượt, 60fps
    });
  }
}, 100);
// 💡 Update chart 10 lần/giây → đủ mượt
// 💡 Batch 10 updates → 1 update → hiệu quả hơn 10x

// Best way ✅✅ (Use appendData for streaming)
const socket = new WebSocket('wss://api.example.com/prices');

socket.onmessage = (event) => {
  const price = JSON.parse(event.data);

  // ✅ ECharts optimized append
  chart.appendData({
    seriesIndex: 0,
    data: [price],
  });
};
```

#### **⚡ 2.3 Advanced: GL Renderer (Canvas-based)**

```typescript
// Use WebGL renderer for 100k+ points
import * as echarts from 'echarts/core';
import { CanvasRenderer } from 'echarts/renderers';
import { GLGraphicGL } from 'echarts/gl';

// Register GL renderer
echarts.use([CanvasRenderer, GLGraphicGL]);

const option: echarts.EChartsOption = {
  series: [
    {
      type: 'scatter',
      symbolSize: 2,
      data: generateLargeDataset(100000), // 100k points

      // ✅ Use GL renderer
      renderAs: 'canvas', // Use canvas instead of SVG
      sampling: 'lttb', // Largest-Triangle-Three-Buckets decimation
      progressive: 1000, // Render 1000 points at a time
      progressiveThreshold: 5000, // Start progressive rendering above 5k points
    },
  ],
};

const chart = echarts.init(document.getElementById('chart'), null, {
  renderer: 'canvas', // ✅ Use canvas
  useDirtyRect: true, // ✅ Only redraw changed areas
});

chart.setOption(option);
```

---

### **🧩 3️⃣ VISX - Low-level Composable Primitives**

**🎯 Mục đích**: Hướng dẫn sử dụng Visx - low-level visualization library
// 💡 Visx: Building blocks để build custom charts
// 💡 Full control: Bạn quyết định mọi thứ
// 💡 Best for: Custom visualizations, high performance requirements

#### **📐 3.1 Visx Philosophy (Triết Lý Visx)**

```
// ============================================
// 🧩 VISX LÀ GÌ?
// ============================================
Visx = Visualization Components
- Low-level building blocks (scales, axes, shapes)
  💡 Low-level: Các building blocks cơ bản
  💡 Scales: Chuyển đổi data → pixel coordinates
  💡 Axes: Vẽ trục X, Y
  💡 Shapes: Vẽ đường, hình tròn, v.v.

- Full control over rendering
  💡 Full control: Bạn quyết định mọi thứ
  💡 ECharts: Config-based → ít control
  💡 Visx: Code-based → full control

- Can use Canvas or SVG (your choice)
  💡 Flexible: Có thể dùng Canvas hoặc SVG
  💡 Bạn quyết định dựa trên use case
  💡 Canvas: Performance
  💡 SVG: Interactions

- Best for: Custom visualizations, high performance
  💡 Custom: Charts không có trong ECharts/Recharts
  💡 High performance: Cần optimize từng chi tiết

- Learning curve: Steeper than ECharts/Recharts
  💡 Khó học hơn ECharts/Recharts
  💡 Cần hiểu D3, scales, coordinates
  💡 Nhưng linh hoạt hơn rất nhiều

// ============================================
// 🚗 ANALOGY (Ví Dụ So Sánh)
// ============================================
Analogy:
- ECharts = High-level "Chart" component (gives you the whole car)
  💡 ECharts: Cho bạn cả chiếc xe hoàn chỉnh
  💡 Chỉ cần config → có chart ngay
  💡 Dễ dùng nhưng ít tùy chỉnh

- Visx = Building blocks (engine, wheels, frame) - assemble yourself
  💡 Visx: Cho bạn các bộ phận (động cơ, bánh xe, khung)
  💡 Bạn tự lắp ráp → có chart của riêng bạn
  💡 Khó hơn nhưng linh hoạt hơn rất nhiều
```

#### **🖼️ 3.2 Visx with SVG**

```typescript
// visx-line-chart.tsx
import { Group } from '@visx/group';
import { LinePath } from '@visx/shape';
import { scaleLinear } from 'd3-scale';
import { extent } from 'd3-array';

interface DataPoint {
  date: Date;
  value: number;
}

export function VisxLineChart({
  data,
  width,
  height,
}: {
  data: DataPoint[];
  width: number;
  height: number;
}) {
  const padding = 40;

  // Get data bounds
  const xExtent = extent(data, (d) => d.date.getTime()) as [number, number];
  const yExtent = extent(data, (d) => d.value) as [number, number];

  // Create scales
  const xScale = scaleLinear({
    domain: xExtent,
    range: [padding, width - padding],
  });

  const yScale = scaleLinear({
    domain: yExtent,
    range: [height - padding, padding],
  });

  return (
    <svg width={width} height={height}>
      {/* Grid lines */}
      <Group>
        {yScale.ticks(5).map((tick) => (
          <line
            key={`grid-${tick}`}
            x1={padding}
            x2={width - padding}
            y1={yScale(tick)}
            y2={yScale(tick)}
            stroke="#eee"
          />
        ))}
      </Group>

      {/* Line path */}
      <LinePath
        data={data}
        x={(d) => xScale(d.date.getTime())}
        y={(d) => yScale(d.value)}
        stroke="#1f77b4"
        strokeWidth={2}
      />

      {/* Points */}
      <Group>
        {data.map((d, i) => (
          <circle
            key={i}
            cx={xScale(d.date.getTime())}
            cy={yScale(d.value)}
            r={3}
            fill="#1f77b4"
          />
        ))}
      </Group>

      {/* Axes */}
      <line
        x1={padding}
        x2={padding}
        y1={padding}
        y2={height - padding}
        stroke="black"
      />
      <line
        x1={padding}
        x2={width - padding}
        y1={height - padding}
        y2={height - padding}
        stroke="black"
      />
    </svg>
  );
}
```

#### **🚀 3.3 Visx with Canvas (High Performance)**

```typescript
// visx-canvas-chart.tsx
import { useRef, useEffect } from 'react';
import { scaleLinear } from 'd3-scale';
import { extent } from 'd3-array';

export function VisxCanvasChart({
  data,
  width,
  height,
}: {
  data: Array<{ date: Date; value: number }>;
  width: number;
  height: number;
}) {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    if (!canvasRef.current) return;

    const ctx = canvasRef.current.getContext('2d');
    if (!ctx) return;

    const padding = 40;

    // Scales
    const xExtent = extent(data, (d) => d.date.getTime()) as [number, number];
    const yExtent = extent(data, (d) => d.value) as [number, number];

    const xScale = scaleLinear({
      domain: xExtent,
      range: [padding, width - padding],
    });

    const yScale = scaleLinear({
      domain: yExtent,
      range: [height - padding, padding],
    });

    // Clear canvas
    ctx.fillStyle = '#fff';
    ctx.fillRect(0, 0, width, height);

    // Draw grid
    ctx.strokeStyle = '#eee';
    yScale.ticks(5).forEach((tick) => {
      const y = yScale(tick);
      ctx.beginPath();
      ctx.moveTo(padding, y);
      ctx.lineTo(width - padding, y);
      ctx.stroke();
    });

    // Draw line
    ctx.strokeStyle = '#1f77b4';
    ctx.lineWidth = 2;
    ctx.beginPath();

    data.forEach((d, i) => {
      const x = xScale(d.date.getTime());
      const y = yScale(d.value);

      if (i === 0) {
        ctx.moveTo(x, y);
      } else {
        ctx.lineTo(x, y);
      }
    });

    ctx.stroke();

    // Draw points
    ctx.fillStyle = '#1f77b4';
    data.forEach((d) => {
      const x = xScale(d.date.getTime());
      const y = yScale(d.value);
      ctx.beginPath();
      ctx.arc(x, y, 3, 0, Math.PI * 2);
      ctx.fill();
    });
  }, [data, width, height]);

  return <canvas ref={canvasRef} width={width} height={height} />;
}
```

---

### **⏱️ 4️⃣ Real-time Data Visualization (Trực Quan Hóa Dữ Liệu Real-time)**

**🎯 Mục đích**: Xử lý real-time data với high-frequency updates
// 💡 Real-time: Dữ liệu cập nhật liên tục (ví dụ: stock prices)
// 💡 High-frequency: Cập nhật nhiều lần/giây (1000+ updates/second)
// 💡 Challenge: Phải render nhanh, không lag

#### **⚡ 4.1 High-Frequency Updates (Cập Nhật Tần Suất Cao)**

```typescript
// ============================================
// ⚡ REAL-TIME STOCK CHART
// ============================================
// real-time-chart.tsx
import { useEffect, useRef, useState } from 'react';
import * as echarts from 'echarts';

export function RealtimeStockChart() {
  // 💡 RealtimeStockChart: Component cho real-time stock chart
  // 💡 Real-time: Cập nhật liên tục từ WebSocket

  const chartRef = useRef<echarts.ECharts | null>(null);
  // 💡 chartRef: Reference đến chart instance
  // 💡 Dùng ref để update chart mà không re-render component

  const dataRef = useRef<Array<[string, number]>>([]);
  // 💡 dataRef: Reference đến data array
  // 💡 Dùng ref để lưu data mà không trigger re-render
  // 💡 Array<[string, number]>: [timestamp, price] pairs

  const maxPoints = 500; // Keep last 500 points in memory
  // 💡 maxPoints: Giới hạn số lượng points
  // 💡 Circular buffer: Chỉ giữ 500 points gần nhất
  // 💡 Giảm memory usage → performance tốt hơn

  useEffect(() => {
    // Initialize chart
    const chart = echarts.init(document.getElementById('chart'));
    chartRef.current = chart;

    chart.setOption({
      xAxis: { type: 'time', name: 'Time' },
      yAxis: { type: 'value' },
      series: [{ type: 'line', data: [], symbolSize: 0 }],
    });

    // WebSocket connection
    const socket = new WebSocket('wss://api.example.com/price-stream');

    socket.onmessage = (event) => {
      const { timestamp, price } = JSON.parse(event.data);

      // Add to data
      dataRef.current.push([timestamp, price]);

      // Keep only last N points (circular buffer)
      if (dataRef.current.length > maxPoints) {
        dataRef.current.shift();
      }

      // ✅ Batch updates: only update chart every 100ms
      // (instead of every tick)
    };

    // Batch update timer
    const updateInterval = setInterval(() => {
      if (chartRef.current && dataRef.current.length > 0) {
        chartRef.current.setOption({
          series: [{ data: dataRef.current }],
        });
      }
    }, 100); // Update 10x/second max

    return () => {
      socket.close();
      clearInterval(updateInterval);
    };
  }, []);

  return <div id="chart" style={{ width: '100%', height: '400px' }} />;
}
```

#### **🧵 4.2 WebWorker for Data Processing**

```typescript
// data-processor.worker.ts
// Run in separate thread to avoid blocking UI

export interface PriceUpdate {
  timestamp: number;
  price: number;
}

// Aggregate data (calculate OHLC candles)
function aggregateCandles(
  updates: PriceUpdate[],
  intervalMs: number
): Array<{
  time: number;
  open: number;
  high: number;
  low: number;
  close: number;
}> {
  const candles = [];
  let currentCandle: any = null;

  updates.forEach((update) => {
    const candleTime = Math.floor(update.timestamp / intervalMs) * intervalMs;

    if (!currentCandle || currentCandle.time !== candleTime) {
      if (currentCandle) candles.push(currentCandle);
      currentCandle = {
        time: candleTime,
        open: update.price,
        high: update.price,
        low: update.price,
        close: update.price,
      };
    } else {
      currentCandle.high = Math.max(currentCandle.high, update.price);
      currentCandle.low = Math.min(currentCandle.low, update.price);
      currentCandle.close = update.price;
    }
  });

  if (currentCandle) candles.push(currentCandle);
  return candles;
}

// Listen for messages from main thread
self.onmessage = (event) => {
  const { updates, intervalMs } = event.data;

  // Process in worker (doesn't block UI)
  const candles = aggregateCandles(updates, intervalMs);

  // Send back to main thread
  self.postMessage({ candles });
};

// Usage in main thread
const worker = new Worker('data-processor.worker.ts');

function processPrice(updates: PriceUpdate[]) {
  worker.postMessage({
    updates,
    intervalMs: 60000, // 1-minute candles
  });

  worker.onmessage = (event) => {
    const { candles } = event.data;
    chart.setOption({ series: [{ data: candles }] }); // ✅ Fast update
  };
}
```

---

### **🚀 5️⃣ Performance Optimization for Large Datasets**

**🎯 Mục đích**: Tối ưu performance cho datasets lớn
// 💡 Large datasets: Datasets với hàng nghìn, hàng triệu points
// 💡 Optimization techniques: Decimation, virtual scrolling, canvas optimization
// 💡 Goal: 60fps mượt mà ngay cả với datasets lớn

#### **✂️ 5.1 Decimation: Reduce Points Without Losing Quality (Giảm Điểm Không Mất Chất Lượng)**

```typescript
// ============================================
// 📉 DECIMATION ALGORITHM - LTTB
// ============================================
// LTTB Algorithm (Largest-Triangle-Three-Buckets)
// Reduces 10k points to 1k while preserving visual shape
// 💡 LTTB: Thuật toán giảm số lượng điểm nhưng giữ nguyên hình dạng
// 💡 Ví dụ: 10k points → 1k points → visual quality vẫn giữ nguyên
// 💡 Performance: Nhanh hơn 10x nhưng vẫn đẹp

function largestTriangleThreeBuckets(
  data: Array<{ x: number; y: number }>,
  threshold: number
): Array<{ x: number; y: number }> {
  // 💡 data: Array các điểm cần decimate
  // 💡 threshold: Số lượng điểm muốn giữ lại (ví dụ: 1000)
  // 💡 Return: Array các điểm đã được decimate

  if (data.length <= threshold) return data;
  // 💡 Nếu số điểm <= threshold → không cần decimate
  // 💡 Return nguyên data

  const bucketSize = (data.length - 2) / (threshold - 2);
  const decimated = [data[0]]; // Always include first point

  for (let i = 0; i < threshold - 2; i++) {
    const avgRangeStart = Math.floor((i + 1) * bucketSize) + 1;
    const avgRangeEnd = Math.floor((i + 2) * bucketSize) + 1;
    const avgRangeLength = avgRangeEnd - avgRangeStart;

    // Calculate average point in next bucket
    let avgX = 0;
    let avgY = 0;
    for (let j = avgRangeStart; j < avgRangeEnd && j < data.length; j++) {
      avgX += data[j].x;
      avgY += data[j].y;
    }
    avgX /= avgRangeLength;
    avgY /= avgRangeLength;

    // Find point with largest triangle area
    const rangeStart = Math.floor(i * bucketSize) + 1;
    const rangeEnd = Math.floor((i + 1) * bucketSize) + 1;

    const lastPoint = decimated[decimated.length - 1];
    let maxArea = -1;
    let maxAreaIndex = -1;

    for (let j = rangeStart; j < rangeEnd && j < data.length; j++) {
      const area = Math.abs(
        (lastPoint.x * (data[j].y - avgY) +
          data[j].x * (avgY - lastPoint.y) +
          avgX * (lastPoint.y - data[j].y)) /
          2
      );

      if (area > maxArea) {
        maxArea = area;
        maxAreaIndex = j;
      }
    }

    decimated.push(data[maxAreaIndex]);
  }

  decimated.push(data[data.length - 1]); // Always include last point
  return decimated;
}

// Usage
const rawData = generateMillionPoints(); // 1M points
const decimated = largestTriangleThreeBuckets(
  rawData,
  2000 // Reduce to 2000 points
); // ✅ Visual quality preserved, 500x faster rendering

chart.setOption({ series: [{ data: decimated }] });
```

#### **🌀 5.2 Virtual Scrolling for Tables**

```typescript
// Virtual scroll for 100k+ rows (only render visible rows)
import { FixedSizeList as List } from 'react-window';

export function DataTable({ rows }: { rows: any[] }) {
  const Row = ({
    index,
    style,
  }: {
    index: number;
    style: React.CSSProperties;
  }) => (
    <div style={style} className="row">
      <span>{rows[index].id}</span>
      <span>${rows[index].price.toFixed(2)}</span>
      <span>{rows[index].volume}</span>
    </div>
  );

  return (
    <List
      height={600}
      itemCount={rows.length}
      itemSize={30} // height of each row
      width="100%"
    >
      {Row}
    </List>
  );
}

// ✅ With 100k rows, only ~20 visible rows rendered (not 100k)
// Memory: O(visible rows) instead of O(total rows)
```

#### **🔧 5.3 Canvas Optimization Techniques**

```typescript
// Technique 1: Offscreen Canvas (double buffering)
const offscreenCanvas = new OffscreenCanvas(width, height);
const offscreenCtx = offscreenCanvas.getContext('2d');

function renderFrame() {
  // Render to offscreen (doesn't block display)
  offscreenCtx.fillRect(0, 0, width, height);
  // ... draw everything ...

  // Swap to main canvas (single fast copy)
  const bitmap = offscreenCanvas.convertToImageBitmap();
  mainCtx.drawImage(bitmap, 0, 0);
}

// Technique 2: Request Animation Frame (60fps cap)
let frameId: number;

function animate() {
  // Only called max 60 times/second
  render();
  frameId = requestAnimationFrame(animate);
}

animate();

// Technique 3: Only redraw changed areas
let dirtyRect = { x: 0, y: 0, width, height };

function renderOnly(dirty: DirtyRect) {
  ctx.clearRect(dirty.x, dirty.y, dirty.width, dirty.height);
  // Redraw only in dirty region
}

// Technique 4: Use requestIdleCallback for non-urgent work
requestIdleCallback(() => {
  // Process data when browser is idle (not blocking animations)
  processLargeDataset();
});

// Technique 5: Web Workers for data processing
const worker = new Worker('chart-worker.js');

worker.postMessage({ data: largeDataset });
worker.onmessage = (e) => {
  const { aggregatedData } = e.data;
  render(aggregatedData); // ✅ Render already-processed data
};
```

---

### **⚖️ 6️⃣ Comparison: ECharts vs Visx vs Canvas**

```
┌─────────────────────────────────────────────────────────────┐
│         VISUALIZATION LIBRARY COMPARISON                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│                  ECharts    Recharts   Visx    Canvas      │
│  ─────────────────────────────────────────────────────      │
│  Learning     Very easy    Easy       Medium   Hard        │
│  Curve        (config)     (React)    (API)    (Manual)    │
│                                                              │
│  Data         < 1k         < 1k       < 5k    > 10k        │
│  Points       (smooth)     (smooth)   (fast)  (very fast) │
│                                                              │
│  Interaction  Excellent    Good       Manual   Manual       │
│  (Zoom,       (built-in)   (React)    (code)   (code)      │
│   Tooltip)                                                  │
│                                                              │
│  Real-time    ⚠️ Okay      ⚠️ Okay    ✅ Good  ✅ Excellent
│  Updates      (< 1/sec)    (< 1/sec)  (fast)   (fastest)   │
│                                                              │
│  Styling      CSS + config CSS + React CSS    Manual       │
│                                                              │
│  Bundle       Small        Medium     Small    Minimal      │
│  Size         (200KB)      (300KB)    (100KB)  (0KB)       │
│                                                              │
│  Best For     Dashboards   React      Custom   Real-time   │
│               Business     Apps       Charts   Streaming   │
│               Charts                                        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

### **🏭 7️⃣ Production Example: Real-time Trading Dashboard**

```typescript
// trading-dashboard.tsx
import { useState, useEffect, useRef } from 'react';
import * as echarts from 'echarts';
import { largestTriangleThreeBuckets } from './decimation';

interface Trade {
  timestamp: number;
  price: number;
  volume: number;
}

export function TradingDashboard() {
  const chartRef = useRef<echarts.ECharts>();
  const tradesRef = useRef<Trade[]>([]);
  const [stats, setStats] = useState({ high: 0, low: Infinity, avgPrice: 0 });

  useEffect(() => {
    // Initialize chart
    const chart = echarts.init(document.getElementById('chart'));
    chartRef.current = chart;

    chart.setOption({
      title: { text: 'Real-time Price' },
      xAxis: { type: 'time' },
      yAxis: { type: 'value' },
      series: [{ type: 'line', data: [], sampling: 'lttb' }],
    });

    // WebSocket for trades
    const socket = new WebSocket('wss://api.example.com/trades');

    socket.onmessage = (event) => {
      const trade: Trade = JSON.parse(event.data);
      tradesRef.current.push(trade);

      // Keep only last 1 hour of trades
      const oneHourAgo = Date.now() - 3600000;
      tradesRef.current = tradesRef.current.filter(
        (t) => t.timestamp > oneHourAgo
      );
    };

    // Update chart every 100ms
    const updateInterval = setInterval(() => {
      if (tradesRef.current.length === 0) return;

      // Decimate for performance
      const decimated = largestTriangleThreeBuckets(
        tradesRef.current.map((t) => ({ x: t.timestamp, y: t.price })),
        1000 // Keep 1000 visible points
      );

      // Update chart
      chartRef.current?.setOption({
        series: [
          {
            data: decimated.map((d) => [d.x, d.y]),
          },
        ],
      });

      // Update stats
      const prices = tradesRef.current.map((t) => t.price);
      setStats({
        high: Math.max(...prices),
        low: Math.min(...prices),
        avgPrice: prices.reduce((a, b) => a + b, 0) / prices.length,
      });
    }, 100);

    return () => {
      socket.close();
      clearInterval(updateInterval);
    };
  }, []);

  return (
    <div>
      <div id="chart" style={{ width: '100%', height: '500px' }} />
      <div className="stats">
        <p>High: ${stats.high.toFixed(2)}</p>
        <p>Low: ${stats.low.toFixed(2)}</p>
        <p>Avg: ${stats.avgPrice.toFixed(2)}</p>
      </div>
    </div>
  );
}
```

---

## **💡 SENIOR TIPS & BEST PRACTICES (Mẹo & Thực Hành Tốt Nhất)**

```
// ============================================
// ✅ VISUALIZATION OPTIMIZATION CHECKLIST
// ============================================
✅ VISUALIZATION OPTIMIZATION CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
☑️  Choose right tool (SVG for < 1k, Canvas for > 10k)
   💡 Chọn đúng tool → performance tốt ngay từ đầu
   💡 SVG: < 1k points, Canvas: > 10k points

☑️  Decimate large datasets (LTTB algorithm)
   💡 Giảm số lượng points nhưng giữ visual quality
   💡 LTTB: Thuật toán tốt nhất cho decimation

☑️  Use virtual scrolling for tables
   💡 Chỉ render visible rows → memory efficient
   💡 100k rows → chỉ render ~20 rows

☑️  Batch updates (not every tick)
   💡 Gộp nhiều updates → 1 update
   💡 Update 10 lần/giây thay vì 1000 lần/giây

☑️  Use WebWorkers for data processing
   💡 Process data trong background thread
   💡 Không block UI → mượt mà hơn

☑️  Offscreen canvas (double buffering)
   💡 Render vào offscreen canvas trước
   💡 Swap sang main canvas → smooth animation

☑️  RequestAnimationFrame (60fps cap)
   💡 Tự động cap ở 60fps
   💡 Browser optimize tốt hơn

☑️  Only redraw changed areas (dirty rect)
   💡 Chỉ redraw phần thay đổi
   💡 Giảm rendering cost đáng kể

☑️  Lazy load heavy libraries
   💡 Chỉ load khi cần
   💡 Giảm initial bundle size

☑️  Profile with DevTools (60fps target)
   💡 Luôn profile với DevTools
   💡 Target: 60fps mượt mà

☑️  Test on mobile devices (slower GPU)
   💡 Mobile có GPU yếu hơn
   💡 Test để đảm bảo performance tốt

☑️  Use canvas + SVG overlay (best of both)
   💡 Canvas: Background rendering (performance)
   💡 SVG: Overlay cho interactions (tooltip, zoom)
   💡 Best of both worlds

// ============================================
// 📊 TYPICAL PERFORMANCE TARGETS
// ============================================
📊 TYPICAL PERFORMANCE TARGETS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
└─ 60fps smooth: < 16.67ms per frame
   💡 60fps = 16.67ms per frame
   💡 Mục tiêu: Mỗi frame < 16.67ms

   ├─ Data processing: < 8ms
   │  💡 Process data trong < 8ms
   │  💡 Nếu > 8ms → dùng WebWorker
   │
   ├─ Rendering: < 8ms
   │  💡 Render trong < 8ms
   │  💡 Nếu > 8ms → optimize rendering
   │
   └─ Browser overhead: < 0.67ms
      💡 Browser overhead: < 0.67ms
      💡 Không thể control → browser tự optimize
```

---

## **⚠️ COMMON MISTAKES (Lỗi Thường Gặp)**

```js
// ============================================
// ❌ MISTAKE 1: Render Tất Cả Data Points
// ============================================
// ❌ Rendering every single data point
data.forEach(point => {
  ctx.arc(...); // ❌ 10k circles = 10k draw calls = slow
  // 💡 VẤN ĐỀ: Render tất cả 10k points
  // 💡 10k draw calls → rất chậm
  // 💡 Performance: Lag, không mượt
});

// ✅ Batch or decimate first
const decimated = LTTB(data, 1000);
// 💡 Decimate: Giảm từ 10k xuống 1k points
// 💡 Visual quality vẫn giữ nguyên
decimated.forEach(point => {
  ctx.arc(...); // ✅ 1k circles = 1k draw calls = fast
  // 💡 Chỉ render 1k points → nhanh hơn 10x
  // 💡 Performance: Mượt, 60fps
});

// ============================================
// ❌ MISTAKE 2: Update Chart Mỗi Lần Nhận Data
// ============================================
// ❌ Updating chart on every data point
socket.onmessage = () => {
  chart.setOption(...); // ⚠️ Expensive re-render
  // 💡 VẤN ĐỀ: Update chart mỗi lần nhận data
  // 💡 setOption: Re-render toàn bộ chart → tốn kém
  // 💡 Nếu nhận 1000 updates/giây → update 1000 lần → lag
};

// ✅ Batch updates
const updateQueue = [];
socket.onmessage = (data) => {
  updateQueue.push(data); // Collect updates
};

setInterval(() => {
  if (updateQueue.length > 0) {
    chart.setOption(...); // ✅ Update 10x/second max
    // 💡 Batch updates: Gộp nhiều updates → 1 update
    // 💡 Update 10 lần/giây → đủ mượt
    // 💡 Performance: Nhanh, mượt
  }
}, 100);

// ============================================
// ❌ MISTAKE 3: Render Invisible Elements
// ============================================
// ❌ Rendering invisible elements
<canvas /> // 1920x1080 canvas with 100k points
// All 100k points rendered even if only 50 visible
// 💡 VẤN ĐỀ: Render tất cả 100k points
// 💡 Nhưng chỉ 50 points visible trên màn hình
// 💡 Lãng phí: Render 99,950 points không cần thiết
// 💡 Performance: Rất chậm, lag

// ✅ Virtual rendering
<FixedSizeList /> // Only render visible rows/points
// 💡 Virtual scrolling: Chỉ render visible rows
// 💡 100k rows → chỉ render ~20 rows visible
// 💡 Performance: Nhanh, mượt, memory efficient
```

---

## **🎯 INTERVIEW ANSWER (Câu Trả Lời Phỏng Vấn)**

**💡 KHI ĐƯỢC HỎI VỀ DATA VISUALIZATION:**
// 💡 Luôn mention: dataset size, update frequency, performance optimization
// 💡 Thể hiện hiểu rõ trade-offs giữa SVG và Canvas

"For data visualization, I choose based on dataset size and update frequency:

// ============================================
// 📊 SMALL DATASETS (< 1K POINTS)
// ============================================
**Small datasets (< 1k):** Use ECharts/Recharts for rich interactions and easy development.
// 💡 < 1k points → SVG vẫn mượt
// 💡 ECharts/Recharts: Dễ dùng, nhiều features
// 💡 Rich interactions: Tooltip, zoom, drill-down built-in
// 💡 Easy development: Config-based, không cần code nhiều

// ============================================
// 📈 LARGE DATASETS (> 10K POINTS)
// ============================================
**Large datasets (> 10k):** Use Canvas with Visx or pure D3 for performance.
// 💡 > 10k points → Canvas bắt buộc
// 💡 SVG không thể xử lý được
// 💡 Canvas: Nhanh hơn SVG rất nhiều
// 💡 Visx/D3: Full control, high performance

// ============================================
// ⚡ REAL-TIME (HIGH-FREQUENCY UPDATES)
// ============================================
**Real-time (high-frequency updates):** Use Canvas + WebWorkers for data processing + decimation (LTTB) to reduce points without losing visual quality.
// 💡 Real-time → Canvas + WebWorkers
// 💡 WebWorkers: Process data trong background thread
// 💡 Decimation (LTTB): Giảm points nhưng giữ visual quality
// 💡 Result: 60fps mượt mà

// ============================================
// 💼 REAL EXAMPLE (Ví Dụ Thực Tế)
// ============================================
**Example:** Built real-time trading dashboard with 50k data points/second:
// 💡 Trading dashboard: Dashboard giao dịch real-time
// 💡 50k points/second: 50 nghìn điểm mỗi giây
// 💡 Challenge: Phải xử lý và render nhanh

- Aggregate ticks into 1-minute candles in WebWorker
  💡 Aggregate: Tổng hợp ticks thành candles
  💡 WebWorker: Process trong background → không block UI
  💡 1-minute candles: Giảm số lượng data points

- Decimate from 1M points to 1k with LTTB algorithm
  💡 Decimate: Giảm từ 1M xuống 1k points
  💡 LTTB: Largest-Triangle-Three-Buckets algorithm
  💡 Visual quality: Vẫn giữ nguyên hình dạng

- Use Canvas rendering with batch updates every 100ms
  💡 Canvas: Render nhanh hơn SVG
  💡 Batch updates: Gộp nhiều updates → 1 update
  💡 100ms: Update 10 lần/giây → đủ mượt

- Result: 60fps smooth, < 100ms latency
  💡 60fps: Mượt mà, không lag
  💡 < 100ms latency: Độ trễ thấp, user không cảm nhận delay

// ============================================
// 🔑 KEY TECHNIQUES (Kỹ Thuật Quan Trọng)
// ============================================
Key techniques: decimation, batching, WebWorkers, virtual rendering, offscreen canvas.
// 💡 Decimation: Giảm số lượng points
// 💡 Batching: Gộp nhiều updates
// 💡 WebWorkers: Process data trong background
// 💡 Virtual rendering: Chỉ render visible elements
// 💡 Offscreen canvas: Double buffering cho smooth animation

This shows **practical performance optimization** ✅
// 💡 Interviewer sẽ đánh giá cao approach này
// 💡 Thể hiện bạn hiểu rõ performance optimization
// 💡 Có kinh nghiệm thực tế với data visualization
```
