# 📊 Q32: AG Grid - Enterprise Data Grid: Performance, Real-time Updates & Best Practices

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"AG Grid = data grid doanh nghiệp với virtual scrolling, transaction API, cập nhật thời gian thực cho 100K+ hàng.**

**🚀 Top 3 Tối Ưu Hiệu Năng:**
1. **`getRowId`**: Cung cấp ID hàng ổn định → tra cứu O(1) (nhanh hơn 1000 lần so với mặc định). 
   ```ts
   getRowId: (params) => params.data.id // Phải unique & stable!
   ```
2. **`applyTransactionAsync`**: Gộp cập nhật → giảm 80% re-renders.
   ```ts
   gridRef.current.api.applyTransactionAsync({ update: rows });
   ```
3. **Virtual Scrolling**: Chỉ render hàng hiển thị (DOM ảo → cực nhẹ).

**♻️ Cập Nhật Thời Gian Thực (WebSocket):**
- **Luồng**: Tin nhắn WebSocket → cập nhật state cục bộ → `applyTransactionAsync` → AG Grid cập nhật tăng dần.
- **Batching**: Gộp 100 updates/100ms → 1 transaction thay vì 100 re-renders.
- **Tính bất biến**: Tạo objects mới cho updates → React phát hiện thay đổi đúng.

**🔑 Khái Niệm Cốt Lõi:**
- **Row Data vs Transaction API**:
  - `setRowData`: Re-render toàn bộ (chậm) → chỉ dùng tải ban đầu.
  - `applyTransaction`: Cập nhật tăng dần (nhanh) → dùng cho thời gian thực.
- **Column Definitions**: `useMemo` → ngăn tạo lại mỗi render.
- **Cell Renderers**: Components tùy chỉnh → định dạng cells (icons, buttons, charts).
- **Server-side Row Model**: Tải dữ liệu lười từ server → cuộn vô hạn.

**⚠️ Lỗi Thường Gặp:**
- **Không dùng getRowId**: Tạo ID mặc định chậm hơn 1000 lần.
- **Dùng forEach với applyTransaction**: Gọi 100 lần thay vì 1 batch.
- **Dữ liệu có thể thay đổi**: Sửa object trực tiếp → AG Grid không phát hiện thay đổi.
- **Tạo lại columnDefs**: Không useMemo → grid khởi tạo lại mỗi render.

**💡 Kiến Thức Senior:**
- **Hiệu năng**: AG Grid xử lý 100K hàng mượt (vs MUI DataGrid lag ở 10K).
- **Kích thước Bundle**: ~150KB gzipped → đánh đổi cho tính năng.
- **Enterprise vs Community**: Enterprise có pivoting, grouping, excel export ($999/dev/năm).
- **So sánh**: AG Grid > MUI DataGrid (hiệu năng), React Table (linh hoạt nhưng làm thủ công).
- **Trường hợp**: Nền tảng trading, dashboards quản trị, công cụ phân tích (datasets lớn + thời gian thực).

---

**⚡ Quick Summary:**
> AG Grid = Enterprise data grid cho high-frequency updates. getRowId (O(1)) + applyTransactionAsync (batching) + Virtual scrolling = xử lý 100K+ rows mượt mà.

**💡 Ghi Nhớ:**
- 🚀 **Top 3 Performance**: getRowId, applyTransactionAsync, Virtual scrolling
- ⚡ **Real-time**: WebSocket → applyTransactionAsync (batch updates)
- 🎯 **Must-Have**: getRowId (1000x faster), immutable data, useMemo columnDefs
- ⚠️ **Never**: setRowData cho updates, mutable data, forEach async

---

## **0. Tại Sao Chọn AG Grid?** 🤔

### **0.1. So Sánh Với Các Thư Viện Khác**

```typescript
/**
 * 📊 SO SÁNH CÁC DATA GRID LIBRARIES
 * 
 * ┌──────────────────┬─────────────┬──────────────┬─────────────┬──────────────┐
 * │ Library          │ Performance │ Features     │ Bundle Size │ License      │
 * ├──────────────────┼─────────────┼──────────────┼─────────────┼──────────────┤
 * │ AG Grid          │ ⭐⭐⭐⭐⭐    │ ⭐⭐⭐⭐⭐     │ ~150KB gz   │ MIT + Paid   │
 * │ MUI DataGrid     │ ⭐⭐⭐       │ ⭐⭐⭐⭐      │ ~200KB gz   │ MIT + Paid   │
 * │ React Table      │ ⭐⭐⭐⭐     │ ⭐⭐⭐        │ ~15KB gz    │ MIT (Free)   │
 * │ Tanstack Table   │ ⭐⭐⭐⭐     │ ⭐⭐⭐⭐      │ ~15KB gz    │ MIT (Free)   │
 * │ react-data-grid  │ ⭐⭐⭐       │ ⭐⭐⭐        │ ~80KB gz    │ MIT (Free)   │
 * └──────────────────┴─────────────┴──────────────┴─────────────┴──────────────┘
 * 
 * 🎯 ĐIỂM MẠNH AG GRID:
 * 1. Performance tốt nhất cho large datasets (100K+ rows)
 * 2. Real-time updates (WebSocket, streaming data)
 * 3. Virtual scrolling mạnh mẽ
 * 4. Enterprise features (pivoting, aggregation, excel export)
 * 5. Mature ecosystem (9+ years development)
 * 
 * ⚠️ ĐIỂM YẾU AG GRID:
 * 1. Bundle size lớn (~150KB)
 * 2. Learning curve cao
 * 3. Enterprise features cần trả phí ($999+/dev/năm)
 * 4. API phức tạp
 */
```

### **0.2. Ưu Điểm AG Grid** ✅

```typescript
/**
 * ✅ ƯU ĐIỂM (PROS):
 * 
 * 1️⃣ PERFORMANCE CỰC TỐT:
 *    - Virtual scrolling: Chỉ render cells trong viewport
 *    - Row node cache: O(1) lookup với getRowId
 *    - Transaction API: Incremental updates (không re-render toàn bộ)
 *    - Async batching: Gộp nhiều updates → giảm 80% renders
 *    
 *    📊 Numbers:
 *    - 100,000 rows: Render trong ~200ms (vs MUI: ~2000ms)
 *    - Real-time: 1000 updates/s mượt mà (vs others: lag)
 *    - Memory: 10MB cho 10K rows (vs others: 50-100MB)
 * 
 * 2️⃣ REAL-TIME UPDATES:
 *    - WebSocket integration tốt
 *    - Cell flash animations (visual feedback)
 *    - Batch updates tự động
 *    - Change detection thông minh
 *    
 *    🎯 Use cases:
 *    - Crypto trading platforms
 *    - Stock market dashboards
 *    - Real-time analytics
 *    - Order books
 * 
 * 3️⃣ FEATURES PHONG PHÚ:
 *    Community (Free):
 *    - Sorting, filtering, pagination
 *    - Column resizing, pinning, moving
 *    - Cell editing, validation
 *    - Custom cell renderers
 *    - Export CSV
 *    
 *    Enterprise (Paid):
 *    - Excel-like pivot tables
 *    - Server-side row model (infinite scroll)
 *    - Advanced filtering
 *    - Grouping & aggregation
 *    - Export Excel/PDF
 *    - Range selection
 *    - Master/detail views
 * 
 * 4️⃣ CUSTOMIZATION:
 *    - Cell renderers (React components)
 *    - Custom filters & editors
 *    - Themes (Quartz, Alpine, Balham, Material)
 *    - CSS variables để customize colors
 *    - Full TypeScript support
 * 
 * 5️⃣ MATURE ECOSYSTEM:
 *    - 9+ years phát triển
 *    - Active community
 *    - Excellent documentation
 *    - Regular updates
 *    - Framework integrations (React, Angular, Vue, Vanilla JS)
 */

// Example: Performance với large dataset
function LargeDatasetExample() {
  // 100,000 rows
  const rowData = Array.from({ length: 100000 }, (_, i) => ({
    id: i,
    name: `User ${i}`,
    email: `user${i}@example.com`,
    age: 20 + (i % 50)
  }));

  return (
    <AgGridReact
      rowData={rowData}
      getRowId={(params) => params.data.id} // ⚡ O(1) lookup
      // → AG Grid chỉ render ~30 rows trong viewport
      // → Scroll mượt mà, không lag!
    />
  );
}

// Example: Real-time updates
function RealTimeExample() {
  const [gridApi, setGridApi] = useState<GridApi | null>(null);

  useEffect(() => {
    if (!gridApi) return;

    // 1000 updates/giây từ WebSocket
    const ws = new WebSocket('wss://stream.example.com');
    
    ws.onmessage = (event) => {
      const updates = JSON.parse(event.data); // Array of 10-20 updates
      
      gridApi.applyTransactionAsync({ update: updates });
      // ✅ AG Grid tự động batch → chỉ render 20 lần/s thay vì 1000 lần/s
      // ✅ CPU: 15% (vs MUI: 80%)
    };

    return () => ws.close();
  }, [gridApi]);

  return (
    <AgGridReact
      onGridReady={(params) => setGridApi(params.api)}
      asyncTransactionWaitMillis={50} // Batch mỗi 50ms
    />
  );
}
```

### **0.3. Nhược Điểm AG Grid** ❌

```typescript
/**
 * ❌ NHƯỢC ĐIỂM (CONS):
 * 
 * 1️⃣ BUNDLE SIZE LỚN:
 *    - Community: ~150KB gzipped (~450KB raw)
 *    - Enterprise: ~250KB gzipped (~750KB raw)
 *    
 *    So sánh:
 *    - React Table: ~15KB (10x nhỏ hơn!)
 *    - Tanstack Table: ~15KB
 *    - MUI DataGrid: ~200KB
 *    
 *    💡 Solution:
 *    - Tree shaking (chỉ import modules cần dùng)
 *    - Code splitting (lazy load grid)
 *    - CDN cho production
 * 
 * 2️⃣ LEARNING CURVE CAO:
 *    - API phức tạp (500+ config options)
 *    - Nhiều concepts mới (Row Node, Grid API, Column API)
 *    - Documentation dày (1000+ pages)
 *    
 *    ⏱️ Time to learn:
 *    - Basic: 1-2 ngày
 *    - Intermediate: 1-2 tuần
 *    - Advanced: 1-2 tháng
 * 
 * 3️⃣ ENTERPRISE FEATURES PAID:
 *    - Pivot tables: $999/dev/năm
 *    - Excel export: $999/dev/năm
 *    - Server-side row model: $999/dev/năm
 *    - Range selection: $999/dev/năm
 *    
 *    💰 Pricing:
 *    - Single Dev: $999/năm
 *    - Team (5 devs): $4,495/năm
 *    - Enterprise (unlimited): $14,995/năm
 *    
 *    ⚠️ NOTE: Community edition vẫn rất mạnh, đủ cho 80% use cases!
 * 
 * 4️⃣ OVERKILL CHO SIMPLE TABLES:
 *    - Nếu chỉ cần sort/filter → React Table nhẹ hơn
 *    - Nếu < 1000 rows → MUI DataGrid đơn giản hơn
 *    - Nếu static data → HTML table + CSS đủ
 *    
 *    ❌ ĐỪng dùng AG Grid nếu:
 *    - < 1000 rows
 *    - Không cần real-time updates
 *    - Không cần advanced features
 *    - Bundle size quan trọng hơn performance
 * 
 * 5️⃣ API PHỨC TẠP:
 *    - Nhiều cách làm 1 việc (confusing cho beginners)
 *    - Breaking changes giữa major versions
 *    - TypeScript types phức tạp
 *    
 *    Example:
 *    // Update data có 3 cách:
 *    setRowData(newData);              // Cách 1: Re-render toàn bộ
 *    gridApi.applyTransaction(...);    // Cách 2: Incremental
 *    gridApi.applyTransactionAsync(...);// Cách 3: Batched
 *    // → Beginners không biết chọn cách nào!
 */

// ❌ Example: Overkill cho simple table
function SimpleTableBad() {
  const data = [
    { name: 'John', age: 30 },
    { name: 'Jane', age: 25 }
  ]; // Chỉ 2 rows!

  return (
    <AgGridReact rowData={data} /> // ❌ 150KB bundle cho 2 rows!
  );
}

// ✅ Better: Dùng HTML table
function SimpleTableGood() {
  return (
    <table>
      <thead>
        <tr><th>Name</th><th>Age</th></tr>
      </thead>
      <tbody>
        <tr><td>John</td><td>30</td></tr>
        <tr><td>Jane</td><td>25</td></tr>
      </tbody>
    </table>
    // ✅ 0KB bundle, đơn giản, đủ dùng!
  );
}
```

### **0.4. Khi Nào Nên Dùng AG Grid?** 🎯

```typescript
/**
 * ✅ NÊN DÙNG AG GRID KHI:
 * 
 * 1. Large datasets (10K+ rows):
 *    - Stock market data
 *    - Transaction history
 *    - Log viewers
 *    - Analytics dashboards
 * 
 * 2. Real-time updates:
 *    - Trading platforms (crypto, stocks)
 *    - Live sports scores
 *    - IoT sensor data
 *    - Chat/messaging apps
 * 
 * 3. Complex data operations:
 *    - Grouping, pivoting
 *    - Aggregations (sum, avg, count)
 *    - Advanced filtering
 *    - Excel-like editing
 * 
 * 4. Performance critical:
 *    - Smooth scrolling required
 *    - Low latency updates
 *    - High-frequency data (100+ updates/s)
 * 
 * ❌ KHÔNG NÊN DÙNG KHI:
 * 
 * 1. Small datasets (< 1000 rows):
 *    → Dùng MUI DataGrid, React Table, hoặc HTML table
 * 
 * 2. Static data (không update):
 *    → Dùng React Table hoặc Tanstack Table (15KB)
 * 
 * 3. Simple requirements:
 *    → Chỉ cần sort/filter → React Table đủ
 * 
 * 4. Bundle size critical:
 *    → Mobile apps, low-end devices → React Table
 * 
 * 5. Budget limited:
 *    → Cần pivot/excel export nhưng không có budget
 *    → Dùng React Table + custom implementation
 */

// Decision tree
function chooseDataGrid(requirements: {
  rowCount: number;
  realTime: boolean;
  complexFeatures: boolean;
  budgetForLicense: boolean;
}): string {
  const { rowCount, realTime, complexFeatures, budgetForLicense } = requirements;

  // Large dataset + Real-time → AG Grid
  if (rowCount > 10000 && realTime) {
    return 'AG Grid ⭐⭐⭐⭐⭐';
  }

  // Need enterprise features + có budget → AG Grid Enterprise
  if (complexFeatures && budgetForLicense) {
    return 'AG Grid Enterprise ⭐⭐⭐⭐⭐';
  }

  // Medium dataset + performance important → AG Grid Community
  if (rowCount > 5000) {
    return 'AG Grid Community ⭐⭐⭐⭐';
  }

  // Small dataset + simple → MUI DataGrid
  if (rowCount < 1000) {
    return 'MUI DataGrid hoặc React Table ⭐⭐⭐';
  }

  // Default: React Table (lightweight)
  return 'React Table / Tanstack Table ⭐⭐⭐⭐';
}

// Examples
console.log(chooseDataGrid({
  rowCount: 50000,
  realTime: true,
  complexFeatures: false,
  budgetForLicense: false
})); // → "AG Grid ⭐⭐⭐⭐⭐"

console.log(chooseDataGrid({
  rowCount: 500,
  realTime: false,
  complexFeatures: false,
  budgetForLicense: false
})); // → "MUI DataGrid hoặc React Table ⭐⭐⭐"
```

### **0.5. AG Grid vs Competitors - Chi Tiết** 📊

```typescript
/**
 * 🥊 AG GRID VS MUI DATAGRID
 * 
 * ┌──────────────────────┬─────────────────┬─────────────────┐
 * │ Feature              │ AG Grid         │ MUI DataGrid    │
 * ├──────────────────────┼─────────────────┼─────────────────┤
 * │ Performance          │ ⭐⭐⭐⭐⭐        │ ⭐⭐⭐           │
 * │ Bundle Size          │ ~150KB gz       │ ~200KB gz       │
 * │ Learning Curve       │ Cao             │ Trung bình      │
 * │ Virtual Scrolling    │ Excellent       │ Good            │
 * │ Real-time Updates    │ Excellent       │ OK              │
 * │ Free Features        │ Nhiều           │ Ít hơn          │
 * │ Paid License         │ $999/dev/năm    │ $1000/dev/năm   │
 * │ TypeScript Support   │ Excellent       │ Excellent       │
 * │ Documentation        │ Excellent       │ Good            │
 * │ Community            │ Large           │ Large           │
 * │ UI/UX                │ Functional      │ Beautiful (MUI) │
 * └──────────────────────┴─────────────────┴─────────────────┘
 * 
 * 🎯 CHỌN AG GRID khi: Performance > UI design
 * 🎯 CHỌN MUI khi: UI design > Performance, đã dùng MUI ecosystem
 * 
 * 
 * 🥊 AG GRID VS REACT TABLE (TANSTACK TABLE)
 * 
 * ┌──────────────────────┬─────────────────┬─────────────────┐
 * │ Feature              │ AG Grid         │ React Table     │
 * ├──────────────────────┼─────────────────┼─────────────────┤
 * │ Performance          │ ⭐⭐⭐⭐⭐        │ ⭐⭐⭐⭐         │
 * │ Bundle Size          │ ~150KB gz       │ ~15KB gz        │
 * │ Out-of-box Features  │ Nhiều           │ Ít (headless)   │
 * │ Customization        │ Trung bình      │ Rất cao         │
 * │ Virtual Scrolling    │ Built-in        │ Cần thêm lib    │
 * │ Real-time            │ Built-in        │ Tự implement    │
 * │ Learning Curve       │ Cao             │ Trung bình      │
 * │ License              │ MIT + Paid      │ MIT (Free)      │
 * │ Setup Time           │ 5 phút          │ 30-60 phút      │
 * └──────────────────────┴─────────────────┴─────────────────┘
 * 
 * 🎯 CHỌN AG GRID khi: Cần features ngay, không muốn custom nhiều
 * 🎯 CHỌN REACT TABLE khi: Bundle size critical, cần full control, thích headless
 * 
 * 
 * 🎯 RECOMMENDATION (Khuyến nghị):
 * 
 * 📈 LARGE ENTERPRISE APP (10K+ rows, real-time):
 *    → AG Grid Community/Enterprise
 *    Lý do: Performance tốt nhất, features đầy đủ
 * 
 * 🏢 MEDIUM BUSINESS APP (1K-10K rows):
 *    → AG Grid Community hoặc MUI DataGrid
 *    Lý do: Cân bằng features/performance/DX
 * 
 * 🏠 SMALL APP (< 1K rows):
 *    → React Table, Tanstack Table, hoặc MUI DataGrid
 *    Lý do: Nhẹ, đơn giản, đủ dùng
 * 
 * 📱 MOBILE/PWA (bundle size critical):
 *    → React Table, Tanstack Table
 *    Lý do: Bundle size nhỏ nhất (15KB)
 * 
 * 💰 STARTUP (limited budget):
 *    → AG Grid Community hoặc React Table
 *    Lý do: Free, đủ features cho MVP
 */
```

---

## **1. Setup & Basic Usage**

```typescript
// 📦 Installation
npm install ag-grid-react ag-grid-community

// 🎨 Import
import { AgGridReact } from 'ag-grid-react';
import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-quartz.css';

// ✅ Basic Grid
function CryptoGrid() {
  const [rowData] = useState([
    { ticker: 'BTCUSDT', price: 50000, volume: 1234 },
    { ticker: 'ETHUSDT', price: 3000, volume: 5678 }
  ]);

  const columnDefs = useMemo(() => [
    { field: 'ticker', headerName: 'Symbol' },
    { field: 'price', headerName: 'Price' },
    { field: 'volume', headerName: 'Volume' }
  ], []);

  return (
    <div className="ag-theme-quartz" style={{ height: 500 }}>
      <AgGridReact
        rowData={rowData}
        columnDefs={columnDefs}
      />
    </div>
  );
}
```

---

## **2. Performance Optimizations** 🚀

### **2.1. getRowId - QUAN TRỌNG NHẤT** ⭐⭐⭐⭐⭐

```typescript
// ❌ SAI: Không có getRowId → O(n) lookup
<AgGridReact rowData={data} />
// Problem: AG Grid dùng index → tìm row phải duyệt array

// ✅ ĐÚNG: Có getRowId → O(1) lookup
<AgGridReact
  rowData={data}
  getRowId={(params) => params.data.ticker} // Unique ID
/>
// → AG Grid tạo Map: { 'BTCUSDT': rowNode } → tìm ngay lập tức!

/**
 * 📊 Performance Impact:
 * - 1,000 rows: 100ms → 1ms (100x faster)
 * - 10,000 rows: 1000ms → 1ms (1000x faster)
 */
```

### **2.2. applyTransaction - Incremental Updates** ⭐⭐⭐⭐⭐

```typescript
// ❌ SAI: setRowData → Re-render toàn bộ
const [rowData, setRowData] = useState(initialData);
setRowData(prev => prev.map(row => 
  row.ticker === ticker ? { ...row, price: newPrice } : row
));
// → 10,000 rows × 5 cells = 50,000 cells re-render ❌

// ✅ ĐÚNG: applyTransaction → Chỉ update 1 row
const [gridApi, setGridApi] = useState<GridApi | null>(null);

function updatePrice(ticker: string, newPrice: number) {
  const rowNode = gridApi.getRowNode(ticker); // O(1) thanks to getRowId
  const updatedData = { ...rowNode.data, price: newPrice }; // Immutable
  gridApi.applyTransaction({ update: [updatedData] });
  // → Chỉ re-render 1 row = 5 cells ✅
}

/**
 * 📊 Performance (10,000 rows, update 1 row):
 * - setRowData: ~500ms, 50,000 cells
 * - applyTransaction: ~2ms, 5 cells
 * → 250x faster!
 */
```

### **2.3. applyTransactionAsync - Batch Updates** ⭐⭐⭐⭐⭐

```typescript
// ❌ SAI: Sync transaction → 100 renders/giây
socket.on('price-update', (update) => {
  gridApi.applyTransaction({ update: [update] }); // Render ngay!
});
// → 100 updates/s → 100 renders/s → CPU 70%

// ✅ ĐÚNG: Async transaction → Batch renders
const gridOptions = {
  asyncTransactionWaitMillis: 50, // Gộp updates mỗi 50ms
};

socket.on('price-update', (update) => {
  gridApi.applyTransactionAsync({ update: [update] });
});
// → 100 updates/s → CHỈ 20 renders/s → CPU 15%

/**
 * 📊 Timeline (50ms batching):
 * 0ms:  Update 1,2,3 → Queue
 * 50ms: ⚡ Render 3 updates cùng lúc
 * → Giảm 80% renders!
 */
```

### **2.4. Immutable Data** ⭐⭐⭐⭐

```typescript
// ❌ SAI: Mutable (AG Grid không detect change)
rowNode.data.price = newPrice; // Sửa trực tiếp
gridApi.applyTransaction({ update: [rowNode.data] });
// → oldRef === newRef → AG Grid nghĩ "không có gì thay đổi" ❌

// ✅ ĐÚNG: Immutable (tạo object mới)
const updatedData = { ...rowNode.data, price: newPrice };
gridApi.applyTransaction({ update: [updatedData] });
// → oldRef !== newRef → AG Grid biết có thay đổi ✅

/**
 * 💡 Tại sao?
 * AG Grid dùng reference comparison (O(1)) thay vì deep comparison (O(n))
 * → Nhanh hơn 100x với objects lớn
 */
```

### **2.5. Virtual Scrolling** (Mặc định bật)

```typescript
/**
 * 🌟 Virtual Scrolling tự động bật
 * 
 * 10,000 rows → CHỈ render ~30 rows (viewport + buffer)
 * → Memory: 200MB → 8MB (96% giảm)
 * → Initial render: 2000ms → 80ms (25x faster)
 */

const gridOptions = {
  rowBuffer: 10, // Render thêm 10 rows ngoài viewport
};
```

---

## **3. Real-time Updates** ⚡

### **3.1. WebSocket Integration**

```typescript
// ✅ Real-time crypto prices
function CryptoGrid() {
  const [gridApi, setGridApi] = useState<GridApi | null>(null);

  useEffect(() => {
    if (!gridApi) return;

    // WebSocket connection
    const ws = new WebSocket('wss://stream.binance.com/ws');

    ws.onmessage = (event) => {
      const update = JSON.parse(event.data);
      
      gridApi.applyTransactionAsync({
        update: [{
          ticker: update.s,
          price: parseFloat(update.c),
          volume: parseFloat(update.v)
        }]
      });
    };

    return () => ws.close(); // Cleanup
  }, [gridApi]);

  return (
    <AgGridReact
      onGridReady={(params) => setGridApi(params.api)}
      getRowId={(params) => params.data.ticker}
      asyncTransactionWaitMillis={50}
    />
  );
}
```

### **3.2. Cell Flash (Visual Feedback)**

```typescript
const columnDefs = [
  {
    field: 'price',
    enableCellChangeFlash: true, // ✅ Flash khi value thay đổi
    cellClassRules: {
      'price-up': (params) => params.value > params.oldValue,   // Xanh
      'price-down': (params) => params.value < params.oldValue, // Đỏ
    }
  }
];

// CSS
.price-up { background-color: #00ff0030; }
.price-down { background-color: #ff000030; }
```

---

## **4. Column Definitions** 📊

```typescript
const columnDefs = useMemo(() => [
  // Basic column
  { field: 'ticker', headerName: 'Symbol', width: 120 },
  
  // Value formatter
  {
    field: 'price',
    valueFormatter: (params) => `$${params.value.toFixed(2)}`,
  },
  
  // Cell class rules (conditional styling)
  {
    field: 'change24h',
    cellClassRules: {
      'text-green': (params) => params.value > 0,
      'text-red': (params) => params.value < 0,
    }
  },
  
  // Column group
  {
    headerName: 'Statistics',
    children: [
      { field: 'high24h', headerName: '24h High' },
      { field: 'low24h', headerName: '24h Low' },
    ]
  }
], []); // ✅ useMemo → Chỉ tạo 1 lần
```

---

## **5. Best Practices** 💡

### **✅ DO:**

```typescript
// 1. Always use getRowId
<AgGridReact getRowId={(params) => params.data.id} />

// 2. Use applyTransactionAsync for high-frequency
gridApi.applyTransactionAsync({ update: [data] });

// 3. Immutable data
const updated = { ...oldData, field: newValue };

// 4. useMemo for columnDefs
const columnDefs = useMemo(() => [...], []);

// 5. Cleanup subscriptions
useEffect(() => {
  const ws = new WebSocket('...');
  return () => ws.close();
}, []);
```

### **❌ DON'T:**

```typescript
// 1. setRowData cho updates
setRowData(prev => prev.map(...)); // ❌ Re-render toàn bộ

// 2. Mutable data
rowNode.data.price = newPrice; // ❌ AG Grid không detect

// 3. Recreate columnDefs mỗi render
const columnDefs = [{ field: 'ticker' }]; // ❌ Re-configure mỗi lần

// 4. Bind trong columnDefs
cellRenderer: this.MyRenderer.bind(this) // ❌ New function mỗi lần

// 5. Forget cleanup
const ws = new WebSocket('...'); // ❌ Memory leak
```

---

## **6. Common Use Cases** 🎯

### **6.1. Crypto Trading Dashboard**

```typescript
function CryptoTrading() {
  const columnDefs = useMemo(() => [
    { field: 'ticker', pinned: 'left' },
    { 
      field: 'price', 
      valueFormatter: (p) => `$${p.value.toFixed(2)}`,
      enableCellChangeFlash: true,
    },
    { 
      field: 'change24h',
      valueFormatter: (p) => `${p.value > 0 ? '+' : ''}${p.value.toFixed(2)}%`,
      cellClassRules: {
        'text-green': (p) => p.value > 0,
        'text-red': (p) => p.value < 0,
      }
    }
  ], []);

  return (
    <AgGridReact
      columnDefs={columnDefs}
      getRowId={(params) => params.data.ticker}
      asyncTransactionWaitMillis={50}
      enableCellChangeFlash={true}
    />
  );
}
```

### **6.2. Order Book**

```typescript
function OrderBook() {
  return (
    <AgGridReact
      getRowId={(params) => params.data.price}
      asyncTransactionWaitMillis={16} // 60 FPS
      suppressCellFocus={true}
      suppressRowClickSelection={true}
      columnDefs={[
        { field: 'price', sort: 'desc' },
        { field: 'amount' },
        { field: 'total' }
      ]}
    />
  );
}
```

---

## **7. Performance Checklist** ✅

```
□ getRowId implemented (unique ID)
□ applyTransactionAsync for updates (not setRowData)
□ Immutable data ({ ...old, new })
□ useMemo for columnDefs
□ asyncTransactionWaitMillis configured (50ms recommended)
□ Virtual scrolling enabled (default)
□ Cleanup WebSocket/subscriptions
□ valueFormatter instead of cellRenderer (when possible)
□ suppressCellFocus if not needed
□ rowBuffer = 10 (default OK)
```

---

## **8. Troubleshooting** 🔧

```typescript
/**
 * ❌ Problem: Updates không hiển thị
 * → Check: Có dùng immutable data không?
 * 
 * ❌ Problem: Lag khi scroll
 * → Check: Có dùng cellRenderer phức tạp không? Dùng valueFormatter
 * 
 * ❌ Problem: Memory leak
 * → Check: Có cleanup WebSocket/subscriptions không?
 * 
 * ❌ Problem: Chậm khi update nhiều rows
 * → Check: Có dùng applyTransactionAsync không?
 * 
 * ❌ Problem: getRowNode(id) chậm
 * → Check: Có implement getRowId không?
 */
```

---

## **📊 Performance Comparison**

```
┌─────────────────────┬──────────────┬─────────────┬──────────────┐
│ Method              │ 10K rows     │ CPU         │ Use Case     │
├─────────────────────┼──────────────┼─────────────┼──────────────┤
│ setRowData          │ ~500ms       │ 80-100%     │ ❌ Never     │
│ applyTransaction    │ ~2ms         │ 5-10%       │ ✅ Updates   │
│ applyTransactionAsync│ ~2ms batched│ 5-10%       │ ⭐ Real-time │
│ getRowNode (no ID)  │ O(n)         │ High        │ ❌ Slow      │
│ getRowNode (w/ ID)  │ O(1)         │ Low         │ ✅ Fast      │
└─────────────────────┴──────────────┴─────────────┴──────────────┘
```

---

## **🎯 Quick Reference**

**Setup:**
```typescript
npm install ag-grid-react ag-grid-community
import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-quartz.css';
```

**Must-Have Props:**
```typescript
<AgGridReact
  getRowId={(params) => params.data.id}           // ⭐ O(1) lookup
  asyncTransactionWaitMillis={50}                 // ⭐ Batching
  onGridReady={(params) => setGridApi(params.api)}// ⭐ API access
/>
```

**Update Data:**
```typescript
// ✅ Right way
gridApi.applyTransactionAsync({ 
  update: [{ ...oldData, price: newPrice }] 
});

// ❌ Wrong way
setRowData(prev => prev.map(...));
```

**Styling:**
```typescript
<div className="ag-theme-quartz" style={{ height: 500 }}>
  <AgGridReact ... />
</div>
```

---

**🎓 Key Takeaways:**
1. **getRowId** = 1000x faster lookups
2. **applyTransactionAsync** = 80% less renders  
3. **Immutable data** = Change detection works
4. **useMemo** = Prevent re-configurations
5. **Cleanup** = No memory leaks
  // 👉 Mỗi property = 1 cột (column)

  // 🏗️ Column Definitions: Cấu hình các cột
  const columnDefs = useMemo(() => [
    { field: 'ticker', headerName: 'Symbol' },   // Cột 1: Mã coin
    { field: 'price', headerName: 'Price' },     // Cột 2: Giá
    { field: 'volume', headerName: 'Volume' }    // Cột 3: Khối lượng
  ], []);
  // ✅ useMemo: Tránh re-create columnDefs mỗi render (tối ưu performance)
  // ✅ [] deps: Chỉ tạo 1 lần khi component mount

  return (
    // 🎨 Wrapper: className = theme, style = kích thước
    <div className="ag-theme-quartz" style={{ height: 500 }}>
      {/* 📊 AG Grid Component */}
      <AgGridReact
        rowData={rowData}           // ✅ Dữ liệu hiển thị
        columnDefs={columnDefs}     // ✅ Cấu hình cột
      />
      {/* 🎯 Kết quả: Grid 3 cột x 2 hàng */}
    </div>
  );
}

/**
 * 📊 Kết quả hiển thị:
 * 
 * ┌──────────┬────────┬─────────┐
 * │ Symbol   │ Price  │ Volume  │
 * ├──────────┼────────┼─────────┤
 * │ BTCUSDT  │ 50000  │ 1234    │
 * │ ETHUSDT  │ 3000   │ 5678    │
 * └──────────┴────────┴─────────┘
 */
```

---

### **1.2. Ưu & Nhược điểm**

```typescript
/**
 * ✅ ƯU ĐIỂM:
 * 
 * 1️⃣ Performance Vượt trội:
 * - 🚀 Xử lý 100,000+ rows mượt mà
 * - ⚡ Virtual Scrolling: Chỉ render rows trong viewport
 * - 🔄 Transaction API: Update từng row thay vì re-render toàn bộ
 * - ⏱️ Async Transactions: Batch updates tự động (giảm 90% render cycles)
 * - 📊 Benchmark: Nhanh hơn 2-3x so với Material-UI DataGrid, React Table
 * 
 * 2️⃣ Features Phong phú:
 * Community Edition (Free):
 * - Sorting, Filtering, Pagination
 * - Row Selection, Cell Editing
 * - Column Groups, Pinned Columns
 * - CSV Export, Clipboard
 * - Custom Cell Renderers
 * - Themes & Styling
 * 
 * Enterprise Edition (Trả phí):
 * - Advanced Filtering (Set, Multi Filter)
 * - Row Grouping & Aggregation
 * - Pivoting & Charting
 * - Excel Export
 * - Master/Detail
 * - Server-Side Row Model
 * 
 * 3️⃣ Real-time Updates Tốt:
 * - 🔴 WebSocket Integration dễ dàng
 * - 📡 Xử lý được 1000+ updates/giây
 * - 💫 Cell Flash Animation: Highlight cells khi data thay đổi
 * - 🎯 Row Node Cache: O(1) lookup để update nhanh
 * 
 * 4️⃣ Developer Experience:
 * - 📚 Documentation xuất sắc
 * - 🔧 TypeScript Support đầy đủ
 * - 🌐 Community lớn
 * - 🔄 Regular Updates
 * 
 * 5️⃣ Production-Ready:
 * - 🏢 Dùng bởi Fortune 500 (Bloomberg, J.P. Morgan, NASA, Google)
 * - 🛡️ Stable & Reliable (phát triển từ 2015)
 * - 📱 Cross-platform (Web, Desktop, Mobile)
 * 
 * ❌ NHƯỢC ĐIỂM:
 * 
 * 1️⃣ Bundle Size Lớn:
 * - 📦 Community: ~500KB minified (~150KB gzip)
 * - 📦 Enterprise: ~800KB minified (~250KB gzip)
 * - 💡 Giải pháp: Tree-shaking, code-splitting, lazy load
 * 
 * 2️⃣ Enterprise Features Trả phí:
 * - 💰 Pricing: $999+/developer/năm
 * - 🔒 Locked: Row Grouping, Pivoting, Excel Export
 * - 💡 Giải pháp: Dùng Community cho hầu hết use cases
 * 
 * 3️⃣ Learning Curve (Advanced):
 * - 📚 Nhiều concepts: Row Models, Cell Renderers, Value Getters
 * - 🧩 API phức tạp: 200+ options
 * - 💡 Giải pháp: Bắt đầu basic, học dần theo use case
 * 
 * 4️⃣ Styling phức tạp:
 * - 🎨 CSS Deep: Phải override nhiều class nội bộ
 * - 🔧 Theme System: Nhiều CSS variables (50+)
 * - 💡 Giải pháp: Dùng built-in themes + override từng phần
 * 
 * 5️⃣ React Integration không "React-like":
 * - ⚛️ Imperative API: Dùng gridApi thay vì declarative
 * - 🔄 State Management: Grid tự quản lý state
 * - 💡 Giải pháp: Chấp nhận imperative (faster), wrap trong hooks
 * 
 * 6️⃣ SSR (Server-Side Rendering) khó:
 * - 🌐 Next.js Issues: AG Grid cần window, document
 * - 💡 Giải pháp: Dynamic import với ssr: false
 */

// Dynamic import cho Next.js
import dynamic from 'next/dynamic';

const AgGridReact = dynamic(
  () => import('ag-grid-react').then(mod => mod.AgGridReact),
  { ssr: false } // ✅ Chỉ load ở client-side
);
```

---

## **2. Performance Optimization - Tối ưu Hiệu suất**

### **2.1. Performance Checklist**

```typescript
/**
 * 🔴 CRITICAL (Phải làm):
 * 
 * 1️⃣ Dùng getRowId để định nghĩa unique ID
 * 2️⃣ Dùng applyTransaction thay vì setRowData
 * 3️⃣ Dùng applyTransactionAsync cho high-frequency updates
 * 4️⃣ Enable Virtual Scrolling (mặc định đã bật)
 * 5️⃣ Immutable Data cho Transactions
 * 
 * 🟡 RECOMMENDED (Nên làm):
 * 
 * 6️⃣ Suppress unnecessary events
 * 7️⃣ Optimize Column Definitions với useMemo
 * 8️⃣ Debounce Cell Editing
 * 9️⃣ Lazy Load Data (Infinite Scroll)
 * 🔟 Optimize Cell Renderers
 * 
 * 🟢 OPTIONAL (Tùy use case):
 * 
 * 11. Reduce Cell Flash Duration
 * 12. Disable Animations
 * 13. Use suppressChangeDetection cho static columns
 * 14. Column Virtualization
 * 15. Web Worker cho Heavy Computations
 */
```

---

### **2.2. Critical Optimizations**

#### **Optimization 1: getRowId - Unique Row Identification**

```typescript
/**
 * ✅ QUAN TRỌNG NHẤT!
 * 
 * getRowId cho phép AG Grid tìm row cần update với O(1) complexity.
 * Không có getRowId → AG Grid phải duyệt toàn bộ array O(n).
 */

// ❌ SAI: Không có getRowId
<AgGridReact rowData={data} />
// 🚨 VẤN ĐỀ:
// - AG Grid dùng INDEX làm ID (0, 1, 2, 3...)
// - Khi update row → Phải duyệt TOÀN BỘ array để tìm: O(n)
// - 1,000 rows → Phải check 1,000 lần!
// - 10,000 rows → Phải check 10,000 lần!

// ✅ ĐÚNG: Có getRowId
<AgGridReact
  rowData={data}
  getRowId={(params) => params.data.ticker} // ✅ Dùng ticker làm unique ID
/>
// 🚀 LỢI ÍCH:
// - AG Grid tạo Map: { 'BTCUSDT': rowNode, 'ETHUSDT': rowNode }
// - Khi update 'BTCUSDT' → Tìm ngay trong Map: O(1)
// - 1,000 rows hay 10,000 rows → Vẫn tìm trong 1 bước!
// - Nhanh hơn 1000x so với không có getRowId

/**
 * 📊 So sánh Performance:
 * 
 * Không có getRowId (O(n) - Linear Search):
 * - 100 rows: 10ms
 * - 1,000 rows: 100ms
 * - 10,000 rows: 1000ms (1 giây!) ❌
 * 
 * Có getRowId (O(1) - Hash Map Lookup):
 * - 100 rows: 1ms
 * - 1,000 rows: 1ms
 * - 10,000 rows: 1ms ✅
 * 
 * 🎯 Kết luận: getRowId là QUAN TRỌNG NHẤT!
 */

/**
 * 📊 Performance Impact:
 * - 1,000 rows: 100ms → 1ms (100x faster)
 * - 10,000 rows: 1000ms → 1ms (1000x faster)
 */
```

---

#### **Optimization 2: applyTransaction - Incremental Updates**

```typescript
/**
 * 🚀 applyTransaction chỉ update rows thay đổi
 * 
 * setRowData: Re-render TOÀN BỘ grid (chậm)
 * applyTransaction: Chỉ update rows cụ thể (nhanh)
 */

// ❌ SAI: Re-render toàn bộ grid (CÁCH CŨ - CHẬM)
const [rowData, setRowData] = useState(initialData);

function updatePrice(ticker: string, newPrice: number) {
  setRowData(prev => prev.map(row => 
    row.ticker === ticker 
      ? { ...row, price: newPrice }  // Tạo row mới
      : row
  ));
  // 🚨 VẤN ĐỀ:
  // 1. setState → React re-render component
  // 2. rowData thay đổi → AG Grid nhận props mới
  // 3. AG Grid so sánh: rowData cũ vs rowData mới
  // 4. Khác nhau → Re-render TOÀN BỘ grid!
  // 5. 10,000 rows × 5 cột = 50,000 cells re-render ❌
  // 6. Mất ~500ms, CPU 80-100%, UI giật lag!
}

// ✅ ĐÚNG: Chỉ update 1 row (CÁCH MỚI - NHANH)
const [gridApi, setGridApi] = useState<GridApi | null>(null);

function updatePrice(ticker: string, newPrice: number) {
  if (!gridApi) return;  // Guard: Đợi gridApi ready
  
  // BƯỚC 1: Lấy row node với O(1) (nhờ getRowId)
  const rowNode = gridApi.getRowNode(ticker);
  if (!rowNode?.data) return;  // Guard: Row không tồn tại
  
  // BƯỚC 2: Tạo data mới (immutable - QUAN TRỌNG!)
  const updatedData = { ...rowNode.data, price: newPrice };
  // 👉 Spread operator tạo object MỚI
  // 👉 AG Grid so sánh reference: old !== new → Có thay đổi!
  
  // BƯỚC 3: Update chỉ 1 row qua Transaction API
  gridApi.applyTransaction({ update: [updatedData] });
  // ✅ AG Grid chỉ re-render:
  //    - 1 row
  //    - 3 cells (ticker, price, volume)
  //    - Mất ~2ms
  //    - CPU 5-10%
  //    - UI mượt mà!
}

/**
 * 📊 So sánh Chi tiết (10,000 rows, update 1 row):
 * 
 * ❌ setRowData (Re-render toàn bộ):
 * ├─ Cells re-render: 10,000 rows × 5 cột = 50,000 cells
 * ├─ Thời gian: ~500ms
 * ├─ CPU: 80-100%
 * ├─ FPS: 10-15 (giật lag)
 * └─ User experience: ❌ Tệ
 * 
 * ✅ applyTransaction (Chỉ update 1 row):
 * ├─ Cells re-render: 1 row × 5 cột = 5 cells
 * ├─ Thời gian: ~2ms
 * ├─ CPU: 5-10%
 * ├─ FPS: 55-60 (mượt mà)
 * └─ User experience: ✅ Tuyệt vời
 * 
 * 🚀 Nhanh hơn 250 LẦN!
 */

/**
 * 📊 Performance Comparison (10,000 rows, update 1 row):
 * 
 * setRowData:
 * - Re-render: 10,000 rows × 5 cells = 50,000 cells
 * - Time: ~500ms
 * - CPU: 80-100%
 * 
 * applyTransaction:
 * - Re-render: 1 row × 5 cells = 5 cells
 * - Time: ~2ms
 * - CPU: 5-10%
 * 
 * 🚀 250x faster!
 */
```

---

#### **Optimization 3: applyTransactionAsync - Batch Updates**

```typescript
/**
 * ⚡ applyTransactionAsync gộp nhiều updates thành 1 render
 * 
 * Critical cho high-frequency updates (WebSocket, real-time data)
 */

// 🔧 BƯỚC 1: Cấu hình batch delay
const gridOptions = {
  asyncTransactionWaitMillis: 50, // ✅ Gộp updates mỗi 50ms
  // 👉 AG Grid sẽ đợi 50ms, gộp TẤT CẢ updates trong khoảng đó
  // 👉 Sau 50ms → Render 1 lần duy nhất
};

// ❌ SAI: Sync transaction (render MỖI LẦN update)
function handleWebSocketMessage(message: any) {
  const ticker = message.s;
  const rowNode = gridApi.getRowNode(ticker);
  
  const updatedData = { ...rowNode.data, price: message.c };
  gridApi.applyTransaction({ update: [updatedData] });
  // 🚨 VẤN ĐỀ:
  // - 100 messages/giây → 100 lần render/giây
  // - Browser chỉ refresh 60 lần/giây (60 FPS)
  // - 40 lần render BỊ LÃNG PHÍ! (browser không kịp hiển thị)
  // - CPU 80-100%, UI giật lag ❌
}

// ✅ ĐÚNG: Async transaction (GỘP updates)
function handleWebSocketMessage(message: any) {
  const ticker = message.s;
  const rowNode = gridApi.getRowNode(ticker);
  
  const updatedData = { ...rowNode.data, price: message.c };
  gridApi.applyTransactionAsync({ update: [updatedData] });
  // ✅ LỢI ÍCH:
  // - 100 messages trong 50ms → AG Grid gộp lại
  // - Chỉ render 1 LẦN sau 50ms
  // - 100 messages/giây → CHỈ 20 lần render/giây (1000ms ÷ 50ms)
  // - CPU 15-25%, FPS ổn định 60 ✅
}

/**
 * 📊 So sánh Performance Chi tiết (100 updates/giây):
 * 
 * ❌ applyTransaction (Sync - Render ngay):
 * ├─ Renders: 100 lần/giây
 * ├─ Wasted renders: 40 lần (vượt quá 60 FPS)
 * ├─ CPU: 80-100%
 * ├─ FPS: 15-20 (giật lag)
 * ├─ Memory: Spike mỗi render
 * └─ User experience: ❌ Tệ
 * 
 * ✅ applyTransactionAsync (Batch 50ms):
 * ├─ Renders: 20 lần/giây (1000ms ÷ 50ms = 20)
 * ├─ Wasted renders: 0 lần
 * ├─ CPU: 15-25%
 * ├─ FPS: 55-60 (mượt mà)
 * ├─ Memory: Ổn định
 * └─ User experience: ✅ Tuyệt vời
 * 
 * 🚀 Giảm 80% renders (100 → 20)!
 * 🚀 CPU giảm 75% (100% → 25%)!
 */

/**
 * 💡 TIMELINE MINH HỌA (asyncTransactionWaitMillis: 50ms):
 * 
 * ┌─────────────────────────────────────────────────────┐
 * │ Thời gian │ Event                │ Action           │
 * ├───────────┼──────────────────────┼──────────────────┤
 * │ 0ms       │ Update 1 đến         │ → Thêm vào queue │
 * │ 10ms      │ Update 2 đến         │ → Thêm vào queue │
 * │ 20ms      │ Update 3 đến         │ → Thêm vào queue │
 * │ 30ms      │ Update 4, 5 đến      │ → Thêm vào queue │
 * │ 45ms      │ Update 6, 7, 8 đến   │ → Thêm vào queue │
 * │ 50ms      │ ⚡ TIMER HẾT!         │ ✅ RENDER cả 8   │
 * │           │                      │    updates!      │
 * │ 55ms      │ Update 9 đến         │ → Queue mới      │
 * │ 70ms      │ Update 10, 11 đến    │ → Thêm vào queue │
 * │ 100ms     │ ⚡ TIMER HẾT!         │ ✅ RENDER cả 3   │
 * └─────────────────────────────────────────────────────┘
 * 
 * KẾT QUẢ: 11 updates → CHỈ 2 lần render!
 * Nếu dùng sync: 11 updates → 11 lần render ❌
 */

/**
 * 🎯 CHỌN GIÁ TRỊ asyncTransactionWaitMillis:
 * 
 * 16ms (60 FPS):
 * ├─ Ưu: Responsive nhất
 * ├─ Nhược: Nhiều renders nếu data đến nhanh
 * └─ Dùng khi: Updates vừa phải (~10-50/s)
 * 
 * 50ms (20 FPS):
 * ├─ Ưu: Cân bằng tốt giữa responsive & performance
 * ├─ Nhược: Độ trễ nhận thấy được (~50ms)
 * └─ Dùng khi: High-frequency updates (50-200/s) ✅ KHUYẾN NGHỊ
 * 
 * 100ms (10 FPS):
 * ├─ Ưu: Performance tốt nhất
 * ├─ Nhược: Lag rõ ràng (100ms delay)
 * └─ Dùng khi: Very high frequency (>500/s)
 * 
 * 1000ms (1 FPS):
 * ├─ Ưu: Cực kỳ tiết kiệm CPU
 * ├─ Nhược: UI cảm giác "freeze" 1 giây
 * └─ Dùng khi: Chỉ cần update định kỳ (dashboards)
 */
```
 */
```

---

#### **Optimization 4: Virtual Scrolling**

```typescript
/**
 * 🌟 Virtual Scrolling (Mặc định đã bật)
 * 
 * Chỉ render rows trong viewport + buffer.
 * 10,000 rows → chỉ render ~30 rows.
 */

const gridOptions = {
  rowBuffer: 10, // ✅ Render thêm 10 rows ngoài viewport
  // Viewport: 20 rows visible
  // Buffer: 10 rows above + 10 rows below
  // Total rendered: 40 rows (instead of 10,000!)
};

/**
 * 📊 Memory Impact (10,000 rows × 5 columns):
 * 
 * Without Virtual Scrolling:
 * - DOM nodes: 50,000 (10,000 × 5)
 * - Memory: ~200MB
 * - Initial render: 2000ms
 * 
 * With Virtual Scrolling:
 * - DOM nodes: 200 (40 × 5)
 * - Memory: ~8MB
 * - Initial render: 80ms
 * 
 * 🚀 25x faster, 96% less memory!
 */
```

---

#### **Optimization 5: Immutable Data**

```typescript
/**
 * ⚠️ RẤT QUAN TRỌNG!
 * 
 * AG Grid yêu cầu immutable data để detect changes.
 * LUÔN tạo object mới, KHÔNG mutate object cũ.
 */

// ❌ SAI: Mutate object (AG Grid KHÔNG detect change)
const rowNode = gridApi.getRowNode(ticker);
rowNode.data.price = newPrice; // ⚠️ Sửa trực tiếp object gốc
gridApi.applyTransaction({ update: [rowNode.data] });
// 🚨 VẤN ĐỀ:
// 1. rowNode.data vẫn trỏ đến ĐỊA CHỈ BỘ NHỚ cũ
// 2. AG Grid so sánh: oldRef === newRef → TRUE (cùng địa chỉ)
// 3. AG Grid kết luận: "Không có gì thay đổi"
// 4. UI KHÔNG cập nhật, user vẫn thấy giá cũ ❌

// ✅ ĐÚNG: Tạo object mới (immutable)
const rowNode = gridApi.getRowNode(ticker);
const updatedData = { 
  ...rowNode.data,        // 📦 Spread: Copy TẤT CẢ properties
  price: newPrice         // 🔧 Ghi đè property mới
}; 
// 👉 { ...obj } tạo object MỚI với ĐỊA CHỈ BỘ NHỚ mới
// 👉 Giống như Ctrl+C Ctrl+V: Tạo file copy, không sửa file gốc

gridApi.applyTransactionAsync({ update: [updatedData] });
// ✅ HOẠT ĐỘNG:
// 1. updatedData có ĐỊA CHỈ BỘ NHỚ mới
// 2. AG Grid so sánh: oldRef !== newRef → FALSE (khác địa chỉ)
// 3. AG Grid kết luận: "Có thay đổi!"
// 4. Re-render cell với giá mới ✅

/**
 * 💡 NGUYÊN TẮC IMMUTABILITY (Bất Biến):
 * 
 * 🎯 QUY TẮC VÀNG:
 * 1. LUÔN tạo object/array MỚI
 * 2. KHÔNG BAOGIỜ sửa object/array cũ
 * 
 * ✅ CÁCH LÀM ĐÚNG:
 * 
 * // Object: Dùng spread operator
 * const newObj = { ...oldObj, field: newValue };
 * 
 * // Array: Dùng spread/map/filter (KHÔNG push/pop/splice)
 * const newArr = [...oldArr, newItem];           // Thêm
 * const newArr = oldArr.map(item => ...);        // Sửa
 * const newArr = oldArr.filter(item => ...);     // Xóa
 * 
 * ❌ TRÁNH:
 * oldObj.field = newValue;      // ❌ Mutate object
 * oldArr.push(item);            // ❌ Mutate array
 * oldArr[0] = newItem;          // ❌ Mutate array
 * Object.assign(oldObj, {...}); // ❌ Mutate object (nếu không clone trước)
 */

/**
 * 🧠 TẠI SAO AG GRID DÙNG REFERENCE COMPARISON?
 * 
 * CÁCH 1: Deep Comparison (So sánh từng property)
 * ────────────────────────────────────────────────
 * function hasChanged(oldData, newData) {
 *   for (let key in oldData) {
 *     if (oldData[key] !== newData[key]) {
 *       return true;  // Tìm thấy khác biệt
 *     }
 *   }
 *   return false;  // Không có gì khác
 * }
 * 
 * Object có 100 properties:
 * ├─ Phải loop 100 lần
 * ├─ Mất ~50 microseconds
 * ├─ 10,000 rows → 500ms ❌
 * └─ Độ phức tạp: O(n × m) - n rows, m properties
 * 
 * CÁCH 2: Reference Comparison (So sánh địa chỉ bộ nhớ)
 * ──────────────────────────────────────────────────────
 * function hasChanged(oldData, newData) {
 *   return oldData !== newData;  // Chỉ 1 phép so sánh!
 * }
 * 
 * Object có 100 properties:
 * ├─ Chỉ so sánh 1 lần (địa chỉ bộ nhớ)
 * ├─ Mất ~0.5 microseconds
 * ├─ 10,000 rows → 5ms ✅
 * └─ Độ phức tạp: O(1) - constant time
 * 
 * 🚀 NHANH HƠN 100 LẦN!
 */

// 📚 EXAMPLE: Merge nhiều updates cùng lúc
const rowNode = gridApi.getRowNode(ticker);

const updatedData = {
  ...rowNode.data,            // 📦 Clone toàn bộ properties cũ
  price: message.price,       // 🔧 Update field 1
  volume: message.volume,     // 🔧 Update field 2  
  timestamp: Date.now(),      // 🔧 Update field 3
  change24h: message.change   // 🔧 Update field 4
};
// 👉 1 lần spread = Clone TẤT CẢ properties
// 👉 Sau đó ghi đè các properties cần thay đổi
// 👉 Hiệu quả hơn nhiều lần spread: { ...obj, a: 1, ...obj, b: 2 } ❌

gridApi.applyTransactionAsync({ update: [updatedData] });

/**
 * 🎓 KỸ THUẬT NÂNG CAO: Nested Objects
 * 
 * ❌ SAI: Spread chỉ clone level 1 (shallow)
 * const user = {
 *   name: 'John',
 *   address: { city: 'NYC', zip: 10001 }
 * };
 * 
 * const updated = { ...user };
 * updated.address.city = 'LA';  // ❌ Vẫn mutate object gốc!
 * // Vì address vẫn trỏ đến địa chỉ cũ
 * 
 * ✅ ĐÚNG: Clone nested objects
 * const updated = {
 *   ...user,
 *   address: { ...user.address, city: 'LA' }  // ✅ Clone address
 * };
 * 
 * ✅ HOẶC: Dùng thư viện Immer (khuyến nghị cho nested phức tạp)
 * import { produce } from 'immer';
 * 
 * const updated = produce(user, draft => {
 *   draft.address.city = 'LA';  // Viết như mutable
 * });
 * // Immer tự động tạo immutable copy!
 */
```
};

gridApi.applyTransactionAsync({ update: [updatedData] });
```

---

### **2.3. Recommended Optimizations**

#### **Optimization 6: Suppress Unnecessary Events**

```typescript
/**
 * 🎯 Tắt events không dùng để giảm overhead
 */

const gridOptions = {
  suppressCellFocus: true,           // ✅ Bỏ focus border (nếu không cần)
  suppressRowClickSelection: true,   // ✅ Bỏ select on click
  suppressColumnVirtualisation: false, // ✅ Giữ column virtualization
  suppressHorizontalScroll: false,   // ✅ Giữ horizontal scroll
  suppressRowHoverHighlight: false,  // ✅ Giữ row hover (UX tốt)
};

/**
 * 💡 Khi nào suppress:
 * - suppressCellFocus: Nếu không cho user edit cells
 * - suppressRowClickSelection: Nếu dùng checkbox selection
 * - suppressColumnMoveAnimation: Nếu cần max performance
 */
```

---

#### **Optimization 7: Optimize Column Definitions**

```typescript
/**
 * 📊 useMemo cho columnDefs tránh re-create mỗi render
 */

// ❌ WRONG: Tạo mới mỗi render
function CryptoGrid() {
  const columnDefs = [
    { field: 'ticker', headerName: 'Symbol' },
    { field: 'price', headerName: 'Price' }
  ];
  // 🚨 Mỗi render → array mới → AG Grid re-configure columns!
  
  return <AgGridReact columnDefs={columnDefs} />;
}

// ✅ RIGHT: useMemo - chỉ tạo 1 lần
function CryptoGrid() {
  const columnDefs = useMemo(() => [
    { field: 'ticker', headerName: 'Symbol' },
    { field: 'price', headerName: 'Price' }
  ], []); // ✅ Empty deps → chỉ tạo lúc mount
  
  const defaultColDef = useMemo(() => ({
    sortable: true,
    resizable: false,
  }), []);
  
  return (
    <AgGridReact
      columnDefs={columnDefs}
      defaultColDef={defaultColDef}
    />
  );
}

/**
 * 📊 Performance Impact:
 * - Tránh re-configure columns mỗi render
 * - Giảm 50-100ms mỗi render cycle
 */
```

---

#### **Optimization 8: Optimize Cell Renderers**

```typescript
/**
 * 🎨 Cell Renderers: Dùng valueFormatter thay vì custom component
 */

// ❌ CHẬM: Custom Cell Renderer (React component)
const PriceCellRenderer = (props: ICellRendererParams) => {
  return (
    <div style={{ display: 'flex', alignItems: 'center' }}>
      <span style={{ color: props.value > 50000 ? 'green' : 'red' }}>
        ${props.value.toFixed(2)}
      </span>
    </div>
  );
};

const columnDef = {
  field: 'price',
  cellRenderer: PriceCellRenderer // 🚨 Render React component cho MỖI cell
  // VẤN ĐỀ:
  // 1. 1000 rows → 1000 React components
  // 2. Mỗi component có lifecycle (mount, update, unmount)
  // 3. Mỗi component tạo Virtual DOM
  // 4. React phải reconcile 1000 components
  // 5. Mất ~200ms chỉ để render cells ❌
};

// ✅ NHANH: valueFormatter + cellClassRules (Pure JS + CSS)
const columnDef = {
  field: 'price',
  
  // BƯỚC 1: Format value (string transformation)
  valueFormatter: (params) => 
    params.value ? `$${params.value.toFixed(2)}` : '-',
  // 👉 Chỉ chạy 1 hàm JS đơn giản
  // 👉 Trả về string, AG Grid render thành text node
  // 👉 KHÔNG tạo React component!
  
  // BƯỚC 2: Apply CSS class based on conditions
  cellClassRules: {
    'price-high': (params) => params.value > 50000, // ✅ Màu xanh
    'price-low': (params) => params.value <= 50000  // ✅ Màu đỏ
  }
  // 👉 AG Grid tự động thêm/xóa CSS classes
  // 👉 Browser apply styles qua CSS engine (NHANH!)
};

// 🎨 CSS (trong file .css)
.price-high { 
  color: #00c087;        /* Xanh lá */
  font-weight: 600;      /* Bold */
}
.price-low { 
  color: #ff5252;        /* Đỏ */
  font-weight: 400;      /* Normal */
}

/**
 * 📊 So sánh Performance Chi tiết (1000 rows):
 * 
 * ❌ Custom Cell Renderer (React Component):
 * ├─ React components: 1000
 * ├─ Virtual DOM nodes: ~3000 (div + span + text)
 * ├─ Initial render: ~200ms
 * ├─ Update 1 cell: ~5ms (React reconciliation)
 * ├─ Memory: ~2MB (component instances + Virtual DOM)
 * └─ Khi scroll: Re-mount components → Lag ❌
 * 
 * ✅ valueFormatter + CSS:
 * ├─ React components: 0
 * ├─ DOM nodes: 1000 text nodes
 * ├─ Initial render: ~20ms
 * ├─ Update 1 cell: ~0.5ms (native DOM update)
 * ├─ Memory: ~200KB (chỉ text nodes)
 * └─ Khi scroll: Chỉ update text → Mượt ✅
 * 
 * 🚀 NHANH HƠN 10 LẦN!
 * 🚀 ÍT BỘ NHỚ HƠN 10 LẦN!
 */

/**
 * 💡 KHI NÀO DÙNG GÌ?
 * 
 * ✅ valueFormatter + cellClassRules (90% trường hợp):
 * ├─ Format numbers: $1,234.56
 * ├─ Format dates: 2024-01-15
 * ├─ Color coding: Green/Red based on value
 * ├─ Font styles: Bold, italic
 * ├─ Icons: Dùng CSS ::before với content
 * └─ 🎯 KHUYẾN NGHỊ: Dùng cái này trước!
 * 
 * ⚠️ Custom Cell Renderer (10% trường hợp):
 * ├─ Interactive elements: Buttons, dropdowns
 * ├─ Complex layouts: Multiple nested components
 * ├─ Charts/Graphs: Sparklines, mini charts
 * ├─ Images: Avatar, product thumbnails
 * └─ 🎯 CHỈ DÙNG khi KHÔNG THỂ làm bằng CSS!
 */

/**
 * 🎓 EXAMPLE: Kết hợp valueFormatter + cellClassRules
 */
const advancedColumnDef = {
  field: 'change24h',
  headerName: '24h Change',
  
  // Format: +5.23% hoặc -2.15%
  valueFormatter: (params) => {
    if (!params.value) return '-';
    const sign = params.value >= 0 ? '+' : '';
    return `${sign}${params.value.toFixed(2)}%`;
  },
  
  // Conditional CSS classes
  cellClassRules: {
    'change-positive': (params) => params.value > 0,   // Xanh
    'change-negative': (params) => params.value < 0,   // Đỏ
    'change-neutral': (params) => params.value === 0,  // Xám
    'change-big': (params) => Math.abs(params.value) > 10, // Bold nếu > 10%
  }
};

// CSS
.change-positive { color: #00c087; }                    /* Xanh */
.change-negative { color: #ff5252; }                    /* Đỏ */
.change-neutral { color: #9e9e9e; }                     /* Xám */
.change-big { font-weight: 700; font-size: 14px; }      /* Bold + Lớn */

/**
 * 🎨 ADVANCED: Dùng CSS Icons (thay vì React component)
 */
const iconColumnDef = {
  field: 'trend',
  headerName: 'Trend',
  
  cellClassRules: {
    'trend-up': (params) => params.value === 'up',
    'trend-down': (params) => params.value === 'down',
  }
};

// CSS với Unicode icons
.trend-up::before {
  content: '▲ ';       /* Triangle up */
  color: #00c087;
}
.trend-down::before {
  content: '▼ ';       /* Triangle down */
  color: #ff5252;
}

// 👉 KHÔNG cần import icon library!
// 👉 KHÔNG cần render React component!
// 👉 Pure CSS → Cực kỳ nhanh! ✅
```
 * 
 * valueFormatter + CSS:
 * - Render: Plain text + CSS class
 * - Time: ~20ms
 * - Memory: Low
 * 
 * 🚀 10x faster!
 * 
 * 💡 Khi nào dùng Cell Renderer:
 * - Complex UI (buttons, charts, images...)
 * - Interactive elements (input, checkbox...)
 * - Không thể làm với formatter + CSS
 */
```

---

### **2.4. Performance Benchmarks**

```typescript
/**
 * 📊 Real-world Performance Benchmarks
 * 
 * Scenario 1: Crypto Priceboard (50 symbols, real-time updates)
 * 
 * | Method                      | Updates/sec | CPU Usage | Smoothness |
 * |-----------------------------|-------------|-----------|------------|
 * | ❌ setRowData               | 10          | 80-100%   | Laggy      |
 * | ⚠️ applyTransaction         | 50          | 40-60%    | OK         |
 * | ✅ applyTransactionAsync    | 1000+       | 15-25%    | Smooth     |
 * 
 * 
 * Scenario 2: Large Dataset (10,000 rows)
 * 
 * | Feature                     | Without Optimization | With Optimization |
 * |-----------------------------|---------------------|-------------------|
 * | Initial Render              | 2000ms              | 300ms             |
 * | Scroll FPS                  | 15-20               | 55-60             |
 * | Memory Usage                | 200MB               | 50MB              |
 * | Update 100 rows             | 500ms               | 20ms              |
 * 
 * 
 * 💡 Optimization Impact Summary:
 * 
 * Critical optimizations (1-5):
 * - getRowId: 100-1000x faster row lookup
 * - applyTransaction: 250x faster than setRowData
 * - applyTransactionAsync: 98% reduction in render cycles
 * - Virtual scrolling: 25x faster initial render, 96% less memory
 * - Immutable data: Enables all above optimizations
 * 
 * Recommended optimizations (6-10):
 * - Suppress events: 10-20% CPU reduction
 * - useMemo columnDefs: 50-100ms saved per render
 * - Optimize cell renderers: 10x faster rendering
 * - Lazy loading: Instant initial load
 * - Debounce editing: Smooth UX
 */
```

---

## **3. Column Definitions - Định nghĩa Cột**

### **3.1. Basic Column Definition**

```typescript
/**
 * 📋 Column Definition Properties
 */

const columnDefs: ColDef[] = [
  {
    // ============= BASIC =============
    field: 'ticker',           // ✅ Tên field trong data object
    headerName: 'Symbol',      // ✅ Text hiển thị ở header
    colId: 'tickerCol',        // Unique column ID (optional)
    
    // ============= DIMENSIONS =============
    width: 100,                // Độ rộng cố định (px)
    minWidth: 50,              // Độ rộng tối thiểu
    maxWidth: 500,             // Độ rộng tối đa
    flex: 1,                   // Flex sizing (thay vì width)
    
    // ============= PINNING =============
    pinned: 'left',            // Ghim cột: 'left' | 'right' | null
    lockPinned: false,         // Lock pinned state
    
    // ============= BEHAVIOR =============
    sortable: true,            // Cho phép sort
    resizable: false,          // Không cho resize
    editable: false,           // Không cho edit
    filter: true,              // Cho phép filter
    
    // ============= CELL RENDERING =============
    cellClass: 'my-cell',      // CSS class cho cell
    cellStyle: { color: 'red' }, // Inline style (static)
    cellClassRules: {          // Dynamic CSS classes
      'price-up': (params) => params.value > params.data.reference
    },
    
    // ============= VALUE HANDLING =============
    valueFormatter: (params) => { // Format giá trị hiển thị
      return params.value?.toFixed(2) ?? '-';
    },
    valueGetter: (params) => {    // Tính giá trị từ data khác
      return params.data.price - params.data.reference;
    },
    
    // ============= TYPE =============
    type: 'numericColumn',     // Column type (căn phải)
  }
];

/**
 * 💡 Common Column Types:
 * - 'numericColumn': Số, căn phải
 * - 'rightAligned': Căn phải
 * - 'dateColumn': Date filter
 */
```

---

### **3.2. Column Groups**

```typescript
/**
 * 📊 Column Groups - Nhóm các cột liên quan
 */

const columnDefs: (ColDef | ColGroupDef)[] = [
  {
    headerName: 'Bid Side',    // ✅ Tên header nhóm
    marryChildren: true,       // ✅ Giữ cột con luôn ở cạnh nhau
    headerClass: 'bid-header', // CSS cho header nhóm
    children: [                // ✅ Các cột con
      {
        field: 'bid1',
        headerName: 'Price',
        minWidth: 110,
      },
      {
        field: 'bidVol1',
        headerName: 'Volume',
        minWidth: 100,
      }
    ]
  },
  {
    headerName: 'Ask Side',
    marryChildren: true,
    headerClass: 'ask-header',
    children: [
      { field: 'ask1', headerName: 'Price' },
      { field: 'askVol1', headerName: 'Volume' }
    ]
  }
];

/**
 * 📊 Result:
 * 
 * ┌─────────────┬─────────────┐
 * │  Bid Side   │  Ask Side   │
 * ├──────┬──────┼──────┬──────┤
 * │Price │Volume│Price │Volume│
 * ├──────┼──────┼──────┼──────┤
 * │50000 │ 1.2  │50001 │ 0.8  │
 * └──────┴──────┴──────┴──────┘
 */
```

---

### **3.3. Default Column Definition**

```typescript
/**
 * 🎯 defaultColDef - Cấu hình mặc định cho TẤT CẢ cột
 */

const defaultColDef: ColDef = {
  resizable: false,            // ✅ Không cho resize (tất cả cột)
  sortable: true,              // ✅ Cho phép sort
  unSortIcon: true,            // ✅ Hiển thị icon unsort
  enableCellChangeFlash: true, // ✅ Flash khi cell thay đổi
  type: 'numericColumn',       // ✅ Mặc định là số (căn phải)
  minWidth: 80,                // ✅ Min width cho tất cả
};

<AgGridReact
  defaultColDef={defaultColDef}  // ✅ Apply cho tất cả cột
  columnDefs={columnDefs}         // Cột cụ thể có thể override
/>

/**
 * 💡 Override trong columnDefs:
 */
const columnDefs = [
  {
    field: 'ticker',
    sortable: false,  // ✅ Override defaultColDef.sortable
    type: 'textColumn' // ✅ Override defaultColDef.type
  }
];
```

---

### **3.4. Value Formatters & Getters**

```typescript
/**
 * 🎨 Value Formatters - Format hiển thị
 */

// Formatter class để reuse
class GridValueFormatter {
  // Format giá (2 số thập phân)
  static price(params: ValueFormatterParams): string {
    if (params.value == null) return '-';
    return params.value.toFixed(2); // 115799.99
  }
  
  // Format volume (K, M, B)
  static volume(params: ValueFormatterParams): string {
    if (params.value == null) return '-';
    const value = params.value;
    
    if (value >= 1_000_000_000) {
      return (value / 1_000_000_000).toFixed(1) + 'B';
    }
    if (value >= 1_000_000) {
      return (value / 1_000_000).toFixed(1) + 'M';
    }
    if (value >= 1_000) {
      return (value / 1_000).toFixed(1) + 'K';
    }
    return value.toString();
  }
  
  // Format percentage
  static percentage(params: ValueFormatterParams): string {
    if (params.value == null) return '-';
    const sign = params.value >= 0 ? '+' : '';
    return `${sign}${params.value.toFixed(2)}%`;
  }
}

// Sử dụng
const columnDefs = [
  {
    field: 'price',
    valueFormatter: GridValueFormatter.price // ✅ Reuse formatter
  },
  {
    field: 'volume',
    valueFormatter: GridValueFormatter.volume
  },
  {
    field: 'changePercent',
    valueFormatter: GridValueFormatter.percentage
  }
];

/**
 * 🔢 Value Getters - Tính giá trị dẫn xuất
 */

const columnDefs = [
  {
    field: 'change',
    headerName: 'Change',
    valueGetter: (params) => {
      // Tính chênh lệch: current - reference
      const current = params.data?.lastPrice ?? 0;
      const reference = params.data?.reference ?? 0;
      return current - reference; // VD: +1488
    },
    valueFormatter: (params) => {
      if (params.value == null) return '-';
      const sign = params.value >= 0 ? '+' : '';
      return `${sign}${params.value.toFixed(0)}`;
    }
  },
  {
    field: 'changePercent',
    headerName: 'Change %',
    valueGetter: (params) => {
      const current = params.data?.lastPrice ?? 0;
      const reference = params.data?.reference ?? 0;
      if (reference === 0) return 0;
      return ((current - reference) / reference) * 100; // VD: +1.28%
    },
    valueFormatter: GridValueFormatter.percentage
  }
];

/**
 * 💡 valueGetter vs valueFormatter:
 * 
 * valueGetter:
 * - Tính toán GIÁ TRỊ từ data khác
 * - Return value thực (number, string, object...)
 * - Dùng cho sort, filter
 * 
 * valueFormatter:
 * - Format STRING hiển thị
 * - Chỉ ảnh hưởng UI
 * - Không ảnh hưởng sort/filter
 * 
 * Flow: data → valueGetter → value → valueFormatter → display
 */
```

---

### **3.5. Cell Class Rules - Dynamic Styling**

```typescript
/**
 * 🎨 cellClassRules - Dynamic CSS classes dựa trên giá trị
 */

const columnDefs = [
  {
    field: 'lastPrice',
    cellClassRules: {
      // ✅ Giá tăng → màu xanh
      'price-up': (params) => {
        const current = params.value ?? 0;
        const reference = params.data?.reference ?? 0;
        return current > reference;
      },
      
      // ✅ Giá giảm → màu đỏ
      'price-down': (params) => {
        const current = params.value ?? 0;
        const reference = params.data?.reference ?? 0;
        return current < reference;
      },
      
      // ✅ Giá không đổi → màu vàng
      'price-ref': (params) => {
        const current = params.value ?? 0;
        const reference = params.data?.reference ?? 0;
        return current === reference;
      }
    }
  }
];

// CSS tương ứng
.ag-theme-quartz {
  .price-up {
    color: #00c087 !important;  // Xanh lá
    font-weight: bold;
  }
  
  .price-down {
    color: #ff5252 !important;  // Đỏ
    font-weight: bold;
  }
  
  .price-ref {
    color: #ffc107 !important;  // Vàng
  }
}

/**
 * 💡 cellClassRules Best Practices:
 * 
 * 1. Return boolean (true = apply class, false = remove)
 * 2. Function được gọi mỗi lần cell render/update
 * 3. Tránh heavy computation trong function
 * 4. Dùng với cellFlash để highlight changes
 */
```

---

## **4. Real-time Updates - WebSocket Integration**

### **4.1. WebSocket Pattern**

```typescript
/**
 * 🔴 Real-time Data Flow Architecture
 * 
 * ┌─────────────────┐
 * │   Grid UI       │ ← Chỉ render & display
 * └────────┬────────┘
 *          │ gridApi
 *          │
 * ┌────────▼────────┐
 * │   DataFlow      │ ← WebSocket & data management
 * └─────────────────┘
 */

// 1️⃣ Initialize Grid với empty data
useEffect(() => {
  if (!gridApi) return;
  
  const initialData = symbols.map(symbol => ({
    ticker: symbol,
    price: 0,
    volume: 0,
    // ... other fields
  }));
  
  gridApi.updateGridOptions({ rowData: initialData });
}, [gridApi]);

// 2️⃣ Handle WebSocket Messages
const handleWebSocketMessage = useCallback((event: MessageEvent) => {
  if (!gridApi) return;
  
  const message = JSON.parse(event.data);
  const ticker = message.s; // Symbol (e.g., 'BTCUSDT')
  
  // Get existing row với O(1)
  const rowNode = gridApi.getRowNode(ticker);
  if (!rowNode?.data) return;
  
  // Merge new data (immutable)
  const updatedData = {
    ...rowNode.data,
    price: parseFloat(message.c),     // Current price
    volume: parseFloat(message.v),    // Volume
    timestamp: Date.now()
  };
  
  // Update grid với async transaction
  gridApi.applyTransactionAsync({ update: [updatedData] });
}, [gridApi]);

// 3️⃣ Connect WebSocket
useEffect(() => {
  if (!gridApi) return;
  
  const ws = new WebSocket('wss://stream.binance.com/ws/!ticker@arr');
  
  ws.onopen = () => console.log('✅ WebSocket connected');
  ws.onmessage = handleWebSocketMessage;
  ws.onerror = (error) => console.error('❌ WebSocket error:', error);
  ws.onclose = () => console.log('🔌 WebSocket closed');
  
  // Cleanup
  return () => {
    if (ws.readyState === WebSocket.OPEN) {
      ws.close();
    }
  };
}, [gridApi, handleWebSocketMessage]);

/**
 * 📊 Flow:
 * 
 * 1. Component mount → Initialize grid với empty data
 * 2. gridApi ready → Connect WebSocket
 * 3. WebSocket message → Parse data
 * 4. getRowNode(ticker) → O(1) lookup
 * 5. Merge new data → Immutable object
 * 6. applyTransactionAsync → Batch update (50ms)
 * 7. Grid render → Only changed cells
 * 8. Cell flash → Highlight changes
 */
```

---

### **4.2. Component Separation Pattern**

```typescript
/**
 * 🏗️ Tách biệt concerns: UI vs Data Management
 */

// ============= Grid Component (UI Only) =============
interface BinanceGridProps {
  onGridReady: (params: GridReadyEvent) => void;
}

export const BinanceGrid: React.FC<BinanceGridProps> = ({ onGridReady }) => {
  const columnDefs = useBinanceColumnDefs(); // Custom hook
  
  const defaultColDef = useMemo(() => ({
    sortable: true,
    resizable: false,
    enableCellChangeFlash: true,
  }), []);
  
  const gridOptions = useMemo(() => ({
    asyncTransactionWaitMillis: 50,
    cellFlashDuration: 500,
    cellFadeDuration: 1000,
  }), []);
  
  return (
    <div className="ag-theme-quartz-dark" style={{ height: '100%' }}>
      <AgGridReact
        columnDefs={columnDefs}
        defaultColDef={defaultColDef}
        gridOptions={gridOptions}
        getRowId={(params) => params.data.ticker}
        onGridReady={onGridReady}
      />
    </div>
  );
};

// ============= DataFlow Component (WebSocket) =============
interface BinanceDataFlowProps {
  gridApi: GridApi | null;
  symbols: string[];
}

export const BinanceDataFlow: React.FC<BinanceDataFlowProps> = ({
  gridApi,
  symbols
}) => {
  // Initialize data
  useEffect(() => {
    if (!gridApi) return;
    
    const initialData = createInitialData(symbols);
    gridApi.updateGridOptions({ rowData: initialData });
  }, [gridApi, symbols]);
  
  // WebSocket connection
  useEffect(() => {
    if (!gridApi) return;
    
    const ws = connectWebSocket(symbols);
    
    ws.onmessage = (event) => {
      const message = JSON.parse(event.data);
      handleUpdate(gridApi, message);
    };
    
    return () => ws.close();
  }, [gridApi, symbols]);
  
  return null; // ✅ No UI
};

// ============= Main Component =============
export const BinancePriceboard: React.FC = () => {
  const [gridApi, setGridApi] = useState<GridApi | null>(null);
  const symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT'];
  
  const handleGridReady = useCallback((params: GridReadyEvent) => {
    setGridApi(params.api);
  }, []);
  
  return (
    <>
      <BinanceGrid onGridReady={handleGridReady} />
      <BinanceDataFlow gridApi={gridApi} symbols={symbols} />
    </>
  );
};

/**
 * ✅ Ưu điểm:
 * - Separation of Concerns: UI riêng, Data riêng
 * - Testable: Test Grid UI và DataFlow riêng biệt
 * - Reusable: Dùng BinanceGrid cho UI khác
 * - Maintainable: Dễ debug, dễ mở rộng
 */
```

---

### **4.3. Cell Flash Animation**

```typescript
/**
 * 💫 Cell Flash - Highlight cells khi value thay đổi
 */

// 1️⃣ Enable flash trong defaultColDef
const defaultColDef = {
  enableCellChangeFlash: true, // ✅ Bật flash cho tất cả cột
};

// 2️⃣ Configure flash duration
const gridOptions = {
  cellFlashDuration: 500,      // ✅ Flash 500ms
  cellFadeDuration: 1000,      // ✅ Fade 1000ms
};

// 3️⃣ Custom flash colors với CSS
.ag-theme-quartz {
  // Default flash color
  --ag-value-change-value-highlight-background-color: rgba(0, 192, 135, 0.3);
  
  // Flash khi cell thay đổi
  .ag-cell-data-changed {
    background-color: var(--ag-value-change-value-highlight-background-color) !important;
  }
  
  // Custom flash cho price up/down
  .price-up.ag-cell-data-changed {
    background-color: rgba(0, 192, 135, 0.2) !important; // Xanh lá
  }
  
  .price-down.ag-cell-data-changed {
    background-color: rgba(255, 82, 82, 0.2) !important; // Đỏ
  }
}

/**
 * 📊 Flash Timeline (khi price thay đổi):
 * 
 * 0ms:   Cell value updated
 * 0ms:   Cell background → Flash color (instant)
 * 500ms: Flash duration end → Start fade
 * 1500ms: Fade complete → Back to normal color
 * 
 * 💡 User Experience:
 * - 500ms flash: User nhận biết cell thay đổi
 * - 1000ms fade: Smooth transition về màu cũ
 * - Total: 1.5s highlight → Dễ track changes
 */
```

---

## **5. Styling & Theming**

### **5.1. Built-in Themes**

```typescript
/**
 * 🎨 AG Grid Built-in Themes
 */

// Light theme
<div className="ag-theme-quartz">
  <AgGridReact />
</div>

// Dark theme
<div className="ag-theme-quartz-dark">
  <AgGridReact />
</div>

// Dynamic theme với React state
const { mode } = useThemeMode(); // 'light' | 'dark'
const themeClass = `ag-theme-quartz${mode === 'dark' ? '-dark' : ''}`;

<div className={themeClass}>
  <AgGridReact />
</div>

/**
 * 💡 Available Themes:
 * - ag-theme-quartz (modern, Material Design-like)
 * - ag-theme-quartz-dark
 * - ag-theme-alpine (classic)
 * - ag-theme-alpine-dark
 * - ag-theme-balham
 * - ag-theme-material
 */
```

---

### **5.2. Custom Theme Variables**

```scss
/**
 * 🎨 Customize Theme với CSS Variables
 */

.ag-theme-quartz {
  // ============= COLORS =============
  --ag-background-color: #1a1a1a;           // Grid background
  --ag-foreground-color: #ffffff;           // Text color
  --ag-header-background-color: #2a2a2a;    // Header background
  --ag-odd-row-background-color: #1e1e1e;   // Odd row background
  --ag-row-hover-color: #2a2a2a;            // Row hover color
  
  // ============= BORDERS =============
  --ag-border-color: #333333;               // Border color
  --ag-row-border-color: #2a2a2a;           // Row border
  
  // ============= FONTS =============
  --ag-font-family: 'SF Pro Display', -apple-system, sans-serif;
  --ag-font-size: 13px;
  
  // ============= SPACING =============
  --ag-grid-size: 4px;                      // Base grid size
  --ag-cell-horizontal-padding: calc(var(--ag-grid-size) * 2);
  
  // ============= HEADER =============
  --ag-header-height: 40px;
  --ag-header-foreground-color: #999999;    // Header text color
  
  // ============= ROW =============
  --ag-row-height: 32px;
  
  // ============= CELL FLASH =============
  --ag-value-change-value-highlight-background-color: rgba(0, 192, 135, 0.3);
}

/**
 * 💡 Custom Header Styling
 */
.ag-theme-quartz {
  .ag-header-cell {
    font-weight: 600;
    text-transform: uppercase;
    font-size: 11px;
    letter-spacing: 0.5px;
  }
  
  // Colored headers cho groups
  .bid-side-header {
    background-color: rgba(0, 192, 135, 0.1);
    color: #00c087;
  }
  
  .ask-side-header {
    background-color: rgba(255, 82, 82, 0.1);
    color: #ff5252;
  }
}
```

---

## **6. Best Practices Summary**

### **6.1. Golden Rules**

```typescript
/**
 * 🏆 AG Grid Golden Rules
 * 
 * 1️⃣ "Update smarter, not harder"
 *    → Dùng applyTransaction, không setState
 * 
 * 2️⃣ "Batch everything"
 *    → asyncTransactionWaitMillis = 50ms
 * 
 * 3️⃣ "Immutable always wins"
 *    → Tạo object mới, đừng mutate
 * 
 * 4️⃣ "Measure before optimize"
 *    → Dùng React DevTools Profiler
 * 
 * 5️⃣ "Less is more"
 *    → Bỏ features không dùng (events, animations)
 * 
 * 6️⃣ "Separate concerns"
 *    → UI component riêng, Data flow riêng
 * 
 * 7️⃣ "useMemo everything"
 *    → columnDefs, defaultColDef, gridOptions
 * 
 * 8️⃣ "O(1) is king"
 *    → getRowId để tìm row nhanh
 */
```

---

### **6.2. Performance Checklist**

```typescript
/**
 * ✅ Performance Optimization Checklist
 */

// 🔴 CRITICAL (Must Do)
[ ] ✅ Set getRowId for unique row identification
[ ] ✅ Use applyTransaction instead of setRowData
[ ] ✅ Use applyTransactionAsync for high-frequency updates
[ ] ✅ Enable Virtual Scrolling (default enabled)
[ ] ✅ Use Immutable Data (spread operator)

// 🟡 RECOMMENDED (Should Do)
[ ] ⚡ Suppress unnecessary events
[ ] ⚡ useMemo for columnDefs & defaultColDef
[ ] ⚡ Optimize cell renderers (formatter + CSS)
[ ] ⚡ Lazy load data (infinite scroll)
[ ] ⚡ Debounce cell editing

// 🟢 OPTIONAL (Nice to Have)
[ ] 💡 Reduce cell flash duration
[ ] 💡 Disable animations (max performance)
[ ] 💡 Column virtualization (100+ columns)
[ ] 💡 Web Workers for heavy compute
[ ] 💡 suppressChangeDetection for static columns

/**
 * 📊 Expected Results:
 * 
 * After optimization:
 * - Initial render: 2000ms → 300ms (85% faster)
 * - Update 100 rows: 500ms → 20ms (96% faster)
 * - Memory: 200MB → 50MB (75% reduction)
 * - CPU: 80-100% → 15-25% (75-85% reduction)
 * - FPS: 15-20 → 55-60 (3-4x smoother)
 */
```

---

### **6.3. Code Organization**

```typescript
/**
 * 🏗️ Recommended Project Structure
 */

BinancePriceboard/
├── index.tsx                           # Main component
├── components/
│   └── BinanceGrid.tsx                 # Grid UI component
├── data-flow/
│   └── BinanceDataFlow.tsx             # WebSocket & data management
├── hooks/
│   ├── useBinanceColumnDef.tsx         # Column definitions hook
│   └── useWebSocket.tsx                # WebSocket hook
├── utils/
│   ├── binanceDataMapper.ts            # Data transformation
│   ├── binanceGridValueFormatter.ts    # Value formatters
│   ├── binanceGridCellClassRule.ts     # Cell class rules
│   └── binanceGridValueGetter.ts       # Value getters
├── constants/
│   ├── agGrid.ts                       # Grid options
│   └── symbols.ts                      # Symbol list
└── style.scss                          # Styling

/**
 * ✅ Benefits:
 * - Clear separation of concerns
 * - Easy to test each module
 * - Reusable utilities
 * - Scalable architecture
 */
```

---

## **7. Common Use Cases & Solutions**

### **7.1. Crypto/Stock Priceboard**

```typescript
/**
 * 📊 Use Case: Real-time Crypto Priceboard
 * 
 * Requirements:
 * - 50+ symbols
 * - WebSocket updates (1000+ updates/sec)
 * - Price color coding (up/down)
 * - Cell flash on change
 * - Sort by change %
 */

// Solution Architecture
const CryptoPriceboard = () => {
  const [gridApi, setGridApi] = useState<GridApi | null>(null);
  
  // 1️⃣ Column Definitions
  const columnDefs = useMemo(() => [
    { field: 'ticker', headerName: 'Symbol', pinned: 'left' },
    {
      field: 'price',
      headerName: 'Price',
      valueFormatter: GridValueFormatter.price,
      cellClassRules: {
        'price-up': (p) => p.value > p.data.reference,
        'price-down': (p) => p.value < p.data.reference,
      }
    },
    {
      field: 'change',
      headerName: 'Change %',
      valueGetter: (p) => ((p.data.price - p.data.reference) / p.data.reference) * 100,
      valueFormatter: GridValueFormatter.percentage,
      sort: 'desc' // Sort by change % descending
    }
  ], []);
  
  // 2️⃣ Grid Options
  const gridOptions = useMemo(() => ({
    asyncTransactionWaitMillis: 50,
    cellFlashDuration: 500,
  }), []);
  
  // 3️⃣ WebSocket Integration
  useEffect(() => {
    if (!gridApi) return;
    
    const ws = new WebSocket('wss://stream.binance.com/ws/!ticker@arr');
    
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      
      data.forEach((ticker: any) => {
        const rowNode = gridApi.getRowNode(ticker.s);
        if (rowNode) {
          gridApi.applyTransactionAsync({
            update: [{
              ...rowNode.data,
              price: parseFloat(ticker.c),
              volume: parseFloat(ticker.v)
            }]
          });
        }
      });
    };
    
    return () => ws.close();
  }, [gridApi]);
  
  return (
    <div className="ag-theme-quartz-dark" style={{ height: '100vh' }}>
      <AgGridReact
        columnDefs={columnDefs}
        gridOptions={gridOptions}
        getRowId={(params) => params.data.ticker}
        onGridReady={(params) => setGridApi(params.api)}
      />
    </div>
  );
};
```

---

### **7.2. Trading Order Book**

```typescript
/**
 * 📊 Use Case: Order Book (Bid/Ask Levels)
 * 
 * Requirements:
 * - 10 bid levels + 10 ask levels
 * - Real-time updates
 * - Color-coded sides (green/red)
 * - Pinned symbol column
 */

const OrderBook = () => {
  const columnDefs = useMemo(() => [
    // Pinned ticker
    { field: 'ticker', pinned: 'left', minWidth: 100 },
    
    // Bid Side (Green)
    {
      headerName: 'Bid',
      marryChildren: true,
      headerClass: 'bid-header',
      children: Array.from({ length: 10 }, (_, i) => ([
        {
          field: `bid${i + 1}`,
          headerName: 'Price',
          valueFormatter: GridValueFormatter.price,
          cellClass: 'bid-cell'
        },
        {
          field: `bidVol${i + 1}`,
          headerName: 'Volume',
          valueFormatter: GridValueFormatter.volume,
          cellClass: 'bid-cell'
        }
      ])).flat()
    },
    
    // Ask Side (Red)
    {
      headerName: 'Ask',
      marryChildren: true,
      headerClass: 'ask-header',
      children: Array.from({ length: 10 }, (_, i) => ([
        {
          field: `ask${i + 1}`,
          headerName: 'Price',
          valueFormatter: GridValueFormatter.price,
          cellClass: 'ask-cell'
        },
        {
          field: `askVol${i + 1}`,
          headerName: 'Volume',
          valueFormatter: GridValueFormatter.volume,
          cellClass: 'ask-cell'
        }
      ])).flat()
    }
  ], []);
  
  return (
    <div className="ag-theme-quartz-dark" style={{ height: '100%' }}>
      <AgGridReact
        columnDefs={columnDefs}
        getRowId={(params) => params.data.ticker}
      />
    </div>
  );
};

// CSS
.bid-header {
  background-color: rgba(0, 192, 135, 0.1);
  color: #00c087;
}

.ask-header {
  background-color: rgba(255, 82, 82, 0.1);
  color: #ff5252;
}

.bid-cell {
  color: #00c087;
}

.ask-cell {
  color: #ff5252;
}
```

---

**💡 Remember:**
> "AG Grid = Performance king cho real-time data. getRowId + applyTransactionAsync + immutable data = 100x faster. Virtual scrolling + O(1) lookup + batch updates = handle millions of rows mượt mà!" 🚀

---

**📚 Resources:**
- [AG Grid Documentation](https://www.ag-grid.com/react-data-grid/)
- [AG Grid API Reference](https://www.ag-grid.com/react-data-grid/grid-api/)
- [AG Grid Examples](https://www.ag-grid.com/react-data-grid/examples/)
