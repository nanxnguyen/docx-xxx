# 📊 Q67: Data Visualization - Biểu Đồ, Canvas, Dữ Liệu Real-time & Performance

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút)**

**"Data visualization là trực quan hóa dữ liệu để người dùng hiểu nhanh. 3 cách chính:"**

- **SVG (Recharts, ECharts)** - Khai báo, linh hoạt, tốt cho 100-1000 điểm
- **Canvas (Visx, Plotly)** - Mệnh lệnh, nhanh, tiết kiệm bộ nhớ, tốt cho 10k+ điểm
- **WebGL (Three.js, Babylon.js)** - Cực kỳ nhanh cho hàng triệu điểm

**"Tôi đã implement real-time trading dashboard với 50K data points:"**

- **ECharts** cho static charts (order book, price history)
- **Canvas rendering** (Visx + D3) cho live tick updates (1000 updates/sec)
- **WebWorker** offload data aggregation → 60fps smooth
- **Virtual scrolling** cho large datasets → render only visible rows
- **Decimation algorithm** (LTTB) → 50K → 1K points (visual quality preserved)
- **Kết quả**: 60fps smooth, < 100ms latency cho data update → visual change

**Key considerations:**

| Loại | Ưu Điểm | Nhược Điểm | Use Case |
|------|---------|-----------|----------|
| **SVG** | Tương tác dễ dàng (zoom, tooltip), DOM elements, WCAG | DOM overhead, slow với 1000+ points | < 1000 points, interactive charts |
| **Canvas** | Hiệu suất cao, memory efficient, 10k+ points | Khó tương tác, khó debug | > 10k points, real-time updates |
| **Hybrid** | Canvas background + SVG overlay | Phức tạp hơn | Best of both worlds |

---

## **📋 GIẢI THÍCH CHI TIẾT CẤP SENIOR/STAFF**

### **⚖️ 1. SVG vs Canvas Trade-offs**

#### **🖼️ 1.1 SVG (Scalable Vector Graphics)**

**Ưu Điểm:**
- ✅ DOM elements → Tương tác dễ dàng (click, hover, tooltip)
- ✅ Semantic HTML → Accessibility tốt (screen readers)
- ✅ Scalable → Sharp ở mọi resolution (Retina displays)
- ✅ Easy to debug → Inspect từng element trong DevTools
- ✅ CSS styling → Style bằng CSS, responsive design dễ
- ✅ Transformations → CSS transforms, zoom/pan/scale dễ

**Nhược Điểm:**
- ❌ DOM overhead → Slower với 1000+ elements
- ❌ Memory intensive → Mỗi element là DOM node riêng
- ❌ Rendering cost → Browser render từng shape, re-render tốn kém
- ❌ Not ideal for real-time → Quá chậm cho high-frequency updates
- ❌ Performance degrades → Exponential slowdown > 1000 points

**Performance Metrics:**
- 100 points: ✅ Smooth (16ms)
- 500 points: ⚠️ Acceptable (50-100ms)
- 1000+ points: ❌ Laggy (>200ms)

**ECharts Implementation:**

```typescript
import * as echarts from 'echarts';

const chart = echarts.init(document.getElementById('chart'));

const option = {
  xAxis: { type: 'category', data: ['Mon', 'Tue', 'Wed', ...] },
  yAxis: { type: 'value' },
  series: [
    {
      data: [120, 200, 150, 80, ...], // ✅ 1000 data points
      type: 'line',
      smooth: true,
      symbolSize: 4,
    },
  ],
};

chart.setOption(option);

// ✅ Tương tác dễ dàng
chart.on('click', (params) => {
  console.log('Clicked:', params.dataIndex, params.value);
});

// ⚠️ Vấn đề: Cập nhật 1000+ điểm thường xuyên → quá chậm
setInterval(() => {
  const newData = generateNewData(); // ✅ 1000 points
  chart.setOption({
    series: [{ data: newData }], // ⚠️ Cập nhật chậm (100-200ms)
  });
}, 100);
// ⚠️ Không thể refresh 10x/giây với SVG → dùng Canvas
```

#### **🎨 1.2 Canvas (Raster Graphics)**

**Ưu Điểm:**
- ✅ Fast rendering → Native GPU acceleration possible
- ✅ Memory efficient → Pixel data, không phải DOM nodes
- ✅ Handles large datasets → Hàng triệu points possible
- ✅ Smooth animations → 60fps với 10k+ points
- ✅ Perfect for real-time → Cập nhật 1000 lần/giây
- ✅ WebGL capable → Ultra-fast với GPU

**Nhược Điểm:**
- ❌ No DOM elements → Khó tương tác (no native click events)
- ❌ Pixel-based → Có thể mờ khi zoom
- ❌ Hard to debug → Không biết pixel nào được vẽ
- ❌ Requires manual event handling → Complex tooltip/zoom logic
- ❌ No semantic HTML → Bad for accessibility
- ❌ More code → Cần quản lý rendering pipeline

**Performance Metrics:**
- 10k points: ✅ Smooth (16ms)
- 100k points: ✅ Smooth with optimization
- 1M points: ⚠️ Possible nhưng cần decimation

**Canvas Implementation (Visx + D3):**

```typescript
import { useRef, useEffect } from 'react';
import { scaleLinear } from 'd3-scale';

export function RealTimeChart({ data }: { data: number[] }) {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    const width = canvas.width;
    const height = canvas.height;
    const padding = 40;

    // Xóa canvas
    ctx.fillStyle = '#fff';
    ctx.fillRect(0, 0, width, height);

    // Scales
    const xScale = scaleLinear()
      .domain([0, data.length])
      .range([padding, width - padding]);

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

    // ✅ Fast: Thậm chí với 10k points, chạy < 16ms
  }, [data]);

  return <canvas ref={canvasRef} width={800} height={400} />;
}

// ⚠️ Manual event handling cho interactivity
function ChartWithTooltip() {
  const [hoveredPoint, setHoveredPoint] = useState<number | null>(null);

  const handleMouseMove = (e: React.MouseEvent<HTMLCanvasElement>) => {
    const canvas = e.currentTarget;
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    // 🚨 Manual hit detection cần implement
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

#### **🧭 1.3 Khi Nào Dùng Cái Nào?**

| Tiêu Chí | SVG | Canvas | WebGL |
|----------|-----|--------|-------|
| **Data Points** | < 1000 | 10k-100k | > 1M |
| **Need Interactions** | ✅ Yes | ❌ Manual | ❌ Manual |
| **Update Frequency** | < 1/sec | > 10/sec | Real-time |
| **Need Accessibility** | ✅ Yes | ❌ No | ❌ No |
| **3D Visualization** | ❌ No | ❌ No | ✅ Yes |
| **Example** | Dashboard | Stock Ticker | 3D Maps |

---

### **📈 2. ECHARTS - Popular SVG Library**

#### **🛠️ 2.1 ECharts Setup & Basic Usage**

```typescript
import * as echarts from 'echarts';

export function initChart(elementId: string, option: echarts.EChartsOption) {
  const chart = echarts.init(document.getElementById(elementId));
  chart.setOption(option);

  // Responsive resize
  window.addEventListener('resize', () => {
    chart.resize();
  });

  return chart;
}

// Usage: Line chart với 1000 data points
const option: echarts.EChartsOption = {
  title: { text: 'Stock Price' },
  tooltip: { trigger: 'axis', formatter: '{b}: ${c}' },
  legend: { data: ['AAPL'] },
  xAxis: {
    type: 'category',
    data: generateDates(1000),
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
      data: generateStockPrices(1000),
      smooth: true,
      areaStyle: { color: 'rgba(31, 119, 180, 0.2)' },
      symbolSize: 0,
    },
  ],
};

const chart = initChart('chart-container', option);
```

#### **⏱️ 2.2 Real-time Updates (Batched)**

```typescript
// ❌ CÁCH TỆ - Update Mỗi Lần Nhận Data
setInterval(() => {
  const newPoint = generatePrice();
  chart.setOption({
    series: [{ data: [...currentData, newPoint] }],
    // ⚠️ Full update mỗi 100ms → tốn kém
  });
}, 100);

// ✅ CÁCH TỐT - Batch Updates
const updateQueue: number[] = [];

// Collect updates (10ms)
setInterval(() => {
  updateQueue.push(generatePrice());
}, 10);

// Batch update (100ms)
setInterval(() => {
  if (updateQueue.length > 0) {
    chart.appendData({
      seriesIndex: 0,
      data: updateQueue.splice(0), // Clear queue
      // ✅ appendData: Chỉ thêm data, không re-render toàn bộ
    });
  }
}, 100);

// ✅✅ Best: Use WebSocket với appendData
const socket = new WebSocket('wss://api.example.com/prices');

socket.onmessage = (event) => {
  const price = JSON.parse(event.data);
  chart.appendData({
    seriesIndex: 0,
    data: [price],
  });
};
```

#### **⚡ 2.3 Advanced: WebGL Renderer (Canvas-based)**

```typescript
import * as echarts from 'echarts/core';
import { CanvasRenderer } from 'echarts/renderers';

echarts.use([CanvasRenderer]);

const option: echarts.EChartsOption = {
  series: [
    {
      type: 'scatter',
      symbolSize: 2,
      data: generateLargeDataset(100000), // 100k points
      renderAs: 'canvas', // ✅ Use canvas
      sampling: 'lttb', // Decimation
      progressive: 1000,
      progressiveThreshold: 5000,
    },
  ],
};

const chart = echarts.init(document.getElementById('chart'), null, {
  renderer: 'canvas', // ✅ Canvas renderer
  useDirtyRect: true, // ✅ Only redraw changed areas
});

chart.setOption(option);
```

---

### **🧩 3. VISX - Low-level Composable Primitives**

**Visx là gì:**
- Low-level building blocks (scales, axes, shapes)
- Full control over rendering
- Có thể dùng Canvas hoặc SVG
- Best for custom visualizations, high performance
- Learning curve: Steeper than ECharts/Recharts

**Ví Dụ So Sánh:**
- ECharts = Cho bạn cả chiếc xe hoàn chỉnh (dễ dùng nhưng ít tùy chỉnh)
- Visx = Cho bạn các bộ phận (động cơ, bánh xe, khung) - bạn tự lắp ráp (khó hơn nhưng linh hoạt hơn)

#### **🖼️ 3.1 Visx with SVG**

```typescript
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

#### **🚀 3.2 Visx with Canvas (High Performance)**

```typescript
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

### **⏱️ 4. Real-time Data Visualization**

#### **⚡ 4.1 High-Frequency Updates**

```typescript
import { useEffect, useRef, useState } from 'react';
import * as echarts from 'echarts';

export function RealtimeStockChart() {
  const chartRef = useRef<echarts.ECharts | null>(null);
  const dataRef = useRef<Array<[string, number]>>([]);
  const maxPoints = 500; // Chỉ giữ 500 points cuối cùng

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
      dataRef.current.push([timestamp, price]);

      // Circular buffer: Chỉ giữ 500 points
      if (dataRef.current.length > maxPoints) {
        dataRef.current.shift();
      }
    };

    // Batch update: Cập nhật chart mỗi 100ms
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
export interface PriceUpdate {
  timestamp: number;
  price: number;
}

// Aggregate data (tính OHLC candles)
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

// Listen for messages
self.onmessage = (event) => {
  const { updates, intervalMs } = event.data;

  // Process trong worker (không block UI)
  const candles = aggregateCandles(updates, intervalMs);

  // Send back
  self.postMessage({ candles });
};

// Main thread usage
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

### **🚀 5. Performance Optimization for Large Datasets**

#### **✂️ 5.1 Decimation: LTTB Algorithm**

```typescript
// Largest-Triangle-Three-Buckets Algorithm
// Giảm 10k điểm → 1k điểm + visual quality vẫn giữ nguyên

function largestTriangleThreeBuckets(
  data: Array<{ x: number; y: number }>,
  threshold: number
): Array<{ x: number; y: number }> {
  if (data.length <= threshold) return data;

  const bucketSize = (data.length - 2) / (threshold - 2);
  const decimated = [data[0]]; // Luôn gồm first point

  for (let i = 0; i < threshold - 2; i++) {
    const avgRangeStart = Math.floor((i + 1) * bucketSize) + 1;
    const avgRangeEnd = Math.floor((i + 2) * bucketSize) + 1;
    const avgRangeLength = avgRangeEnd - avgRangeStart;

    // Calculate average point
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

  decimated.push(data[data.length - 1]);
  return decimated;
}

// Usage
const rawData = generateMillionPoints(); // 1M points
const decimated = largestTriangleThreeBuckets(rawData, 2000); // Giảm → 2000 points
// ✅ Visual quality giữ nguyên, 500x nhanh hơn
chart.setOption({ series: [{ data: decimated }] });
```

#### **🌀 5.2 Virtual Scrolling for Tables**

```typescript
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
      itemSize={30}
      width="100%"
    >
      {Row}
    </List>
  );
}

// ✅ 100k rows → chỉ render ~20 visible rows (không phải 100k)
// Memory: O(visible rows) thay vì O(total rows)
```

#### **🔧 5.3 Canvas Optimization Techniques**

```typescript
// Technique 1: Offscreen Canvas (double buffering)
const offscreenCanvas = new OffscreenCanvas(width, height);
const offscreenCtx = offscreenCanvas.getContext('2d');

function renderFrame() {
  // Render vào offscreen (không block display)
  offscreenCtx.fillRect(0, 0, width, height);
  // ... vẽ mọi thứ ...

  // Swap sang main canvas (fast copy)
  const bitmap = offscreenCanvas.convertToImageBitmap();
  mainCtx.drawImage(bitmap, 0, 0);
}

// Technique 2: RequestAnimationFrame (60fps cap)
let frameId: number;

function animate() {
  render();
  frameId = requestAnimationFrame(animate); // Max 60 lần/giây
}

animate();

// Technique 3: Chỉ redraw changed areas
let dirtyRect = { x: 0, y: 0, width, height };

function renderOnly(dirty: DirtyRect) {
  ctx.clearRect(dirty.x, dirty.y, dirty.width, dirty.height);
  // Redraw chỉ trong dirty region
}

// Technique 4: Web Workers cho data processing
const worker = new Worker('chart-worker.js');

worker.postMessage({ data: largeDataset });
worker.onmessage = (e) => {
  const { aggregatedData } = e.data;
  render(aggregatedData); // ✅ Render data đã được process
};
```

---

### **⚖️ 6. Comparison: ECharts vs Visx vs Canvas**

| Tiêu Chí | ECharts | Recharts | Visx | Canvas |
|----------|---------|----------|------|--------|
| **Learning Curve** | Rất dễ (config) | Dễ (React) | Medium (API) | Khó (Manual) |
| **Data Points** | < 1k smooth | < 1k smooth | < 5k fast | > 10k very fast |
| **Interaction** | ✅ Excellent | ✅ Good | Manual | Manual |
| **Real-time** | ⚠️ Okay | ⚠️ Okay | ✅ Good | ✅ Excellent |
| **Styling** | CSS + Config | CSS + React | CSS | Manual |
| **Bundle Size** | Small (200KB) | Medium (300KB) | Small (100KB) | Minimal |
| **Best For** | Dashboards | React Apps | Custom Charts | Real-time Streaming |

---

### **🏭 7. Production Example: Real-time Trading Dashboard**

```typescript
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

    // WebSocket cho trades
    const socket = new WebSocket('wss://api.example.com/trades');

    socket.onmessage = (event) => {
      const trade: Trade = JSON.parse(event.data);
      tradesRef.current.push(trade);

      // Chỉ giữ 1 giờ cuối cùng
      const oneHourAgo = Date.now() - 3600000;
      tradesRef.current = tradesRef.current.filter((t) => t.timestamp > oneHourAgo);
    };

    // Update chart mỗi 100ms
    const updateInterval = setInterval(() => {
      if (tradesRef.current.length === 0) return;

      // Decimation cho performance
      const decimated = largestTriangleThreeBuckets(
        tradesRef.current.map((t) => ({ x: t.timestamp, y: t.price })),
        1000 // Giữ 1000 visible points
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

## **💡 SENIOR TIPS & BEST PRACTICES**

### **✅ Visualization Optimization Checklist**

- ☑️ Chọn đúng tool (SVG cho < 1k, Canvas cho > 10k)
- ☑️ Decimation (LTTB algorithm) cho large datasets
- ☑️ Virtual scrolling cho tables
- ☑️ Batch updates (không mỗi tick)
- ☑️ WebWorkers cho data processing
- ☑️ Offscreen canvas (double buffering)
- ☑️ RequestAnimationFrame (60fps cap)
- ☑️ Chỉ redraw changed areas (dirty rect)
- ☑️ Lazy load heavy libraries
- ☑️ Profile với DevTools (target 60fps)
- ☑️ Test trên mobile devices
- ☑️ Canvas + SVG overlay (best of both)

### **📊 Typical Performance Targets**

- **60fps smooth**: < 16.67ms per frame
  - Data processing: < 8ms
  - Rendering: < 8ms
  - Browser overhead: < 0.67ms

---

## **⚠️ Common Mistakes**

### **❌ Mistake 1: Render Tất Cả Data Points**

```typescript
// ❌ CÁCH TỆ
data.forEach(point => {
  ctx.arc(...); // ❌ 10k circles = 10k draw calls = slow
});

// ✅ CÁCH TỐT
const decimated = LTTB(data, 1000);
decimated.forEach(point => {
  ctx.arc(...); // ✅ 1k circles = 1k draw calls = 10x nhanh
});
```

### **❌ Mistake 2: Update Chart Mỗi Lần Nhận Data**

```typescript
// ❌ CÁCH TỆ
socket.onmessage = () => {
  chart.setOption(...); // ⚠️ Expensive re-render mỗi lần
};

// ✅ CÁCH TỐT
const updateQueue = [];
socket.onmessage = (data) => {
  updateQueue.push(data);
};

setInterval(() => {
  if (updateQueue.length > 0) {
    chart.setOption(...); // ✅ Update 10x/second max
  }
}, 100);
```

### **❌ Mistake 3: Render Invisible Elements**

```typescript
// ❌ CÁCH TỆ
<canvas /> // 100k points, nhưng chỉ 50 visible
// ❌ Render 99,950 points không cần thiết

// ✅ CÁCH TỐT
<FixedSizeList /> // Chỉ render visible rows
// ✅ 100k rows → render ~20 rows visible
```

---

## **🎯 Interview Answer**

**"Khi được hỏi về Data Visualization:"**

**"Tôi chọn theo dataset size và update frequency:**

- **Small datasets (< 1k):** Use ECharts/Recharts để có rich interactions và dễ develop
  - SVG vẫn mượt với < 1k points
  - Built-in tooltip, zoom, drill-down
  - Config-based, dễ dùng

- **Large datasets (> 10k):** Use Canvas với Visx hoặc pure D3 để có performance
  - SVG không thể xử lý > 10k points
  - Canvas nhanh hơn SVG rất nhiều
  - Full control, high performance

- **Real-time (high-frequency updates):** Use Canvas + WebWorkers cho data processing + decimation (LTTB)
  - WebWorkers: Process data trong background thread → không block UI
  - Decimation (LTTB): Giảm points nhưng giữ visual quality
  - Kết quả: 60fps smooth

**Example:** Built real-time trading dashboard với 50k data points/second:
- Aggregate ticks thành 1-minute candles trong WebWorker
- Decimate từ 1M points → 1k với LTTB algorithm
- Canvas rendering với batch updates mỗi 100ms
- Kết quả: 60fps smooth, < 100ms latency

Key techniques: decimation, batching, WebWorkers, virtual rendering, offscreen canvas."**

Điều này thể hiện **practical performance optimization** ✅
