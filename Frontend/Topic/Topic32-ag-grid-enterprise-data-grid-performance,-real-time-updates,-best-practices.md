# 📊 Q32: AG Grid - Enterprise Data Grid: Performance, Real-time Updates & Best Practices

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"AG Grid = data grid doanh nghiệp với virtual scrolling, transaction API, cập nhật thời gian thực cho 100K+ hàng.**

**🚀 Top 3 Tối Ưu Hiệu Năng:**

1. **`getRowId`**: Cung cấp ID hàng ổn định → tra cứu O(1) (nhanh hơn 1000 lần so với mặc định).
   ```ts
   getRowId: (params) => params.data.id; // Phải unique & stable!
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

// 💡 Example: Performance với large dataset
// 🎯 Mục đích: Hiển thị 100,000 rows mà vẫn mượt mà
function LargeDatasetExample() {
  // 📊 Tạo 100,000 rows dữ liệu mẫu
  // 💡 Array.from() tạo array với 100,000 phần tử
  // 💡 { length: 100000 }: Tạo array có 100,000 phần tử rỗng
  // 💡 (_, i) => {...}: Callback function, i là index (0, 1, 2...)
  const rowData = Array.from({ length: 100000 }, (_, i) => ({
    id: i, // 💡 ID duy nhất cho mỗi row - dùng làm key để tìm nhanh
    name: `User ${i}`, // 💡 Tên user - template string tạo "User 0", "User 1"...
    email: `user${i}@example.com`, // 💡 Email user - template string
    age: 20 + (i % 50), // 💡 Tuổi từ 20-69 (lặp lại)
    // 💡 i % 50: Lấy số dư khi chia cho 50 → 0-49
    // 💡 20 + (i % 50) → Tuổi từ 20-69, lặp lại sau mỗi 50 rows
  }));

  return (
    <AgGridReact
      rowData={rowData} // 📦 Truyền 100,000 rows vào grid
      getRowId={(params) => params.data.id} // ⚡ O(1) lookup - QUAN TRỌNG!
      // 💡 getRowId: Function trả về unique ID cho mỗi row
      // 💡 params.data.id: Lấy id từ data object (VD: 0, 1, 2...)
      // 💡 O(1): Tìm row trong 1 bước (dùng Map/Hash table)
      // 💡 Không có getRowId: Phải duyệt 100,000 rows → O(n) → Chậm!
      // → AG Grid chỉ render ~30 rows trong viewport (virtual scrolling)
      // → Scroll mượt mà, không lag!
      // 💡 Memory: Chỉ ~8MB thay vì 200MB nếu render tất cả!
    />
  );
}

// 💡 Example: Real-time updates với WebSocket
// 🎯 Mục đích: Cập nhật grid theo thời gian thực từ WebSocket
function RealTimeExample() {
  // 🔧 State: Lưu Grid API để có thể gọi methods
  // useState: React hook để quản lý state
  const [gridApi, setGridApi] = useState<GridApi | null>(null);
  // 💡 gridApi: Object chứa tất cả methods để control grid (update, filter, sort...)
  // 💡 <GridApi | null>: TypeScript type - có thể là GridApi hoặc null
  // 💡 null ban đầu vì grid chưa ready (chưa mount)

  // useEffect: React hook chạy sau khi component render
  useEffect(() => {
    if (!gridApi) return; // ⚠️ Guard: Đợi gridApi ready - không làm gì nếu chưa có

    // 🌐 WebSocket: Kết nối đến server streaming data
    // 💡 WebSocket: Protocol 2 chiều, server có thể push data đến client
    // 💡 wss://: WebSocket Secure (HTTPS cho WebSocket)
    // 💡 1000 updates/giây từ WebSocket (high-frequency updates)
    const ws = new WebSocket('wss://stream.example.com');

    // 📨 Event: Nhận message từ WebSocket
    // onmessage: Event handler khi server gửi data đến
    ws.onmessage = (event) => {
      // event.data: String JSON từ server
      const updates = JSON.parse(event.data);
      // 💡 Parse JSON: Convert string → JavaScript object/array
      // 💡 updates: Array of 10-20 row updates (mỗi update là 1 object)

      // ⚡ applyTransactionAsync: Update grid với batching
      // applyTransactionAsync: Gộp nhiều updates lại, render 1 lần sau delay
      gridApi.applyTransactionAsync({ update: updates });
      // ✅ AG Grid tự động batch → chỉ render 20 lần/s thay vì 1000 lần/s
      // 💡 Batching: Gộp nhiều updates trong 50ms → render 1 lần
      // 💡 Thay vì render 1000 lần/giây → chỉ render 20 lần/giây
      // ✅ CPU: 15% (vs MUI: 80% - không có batching)
      // 💡 Performance: Giảm 80% số lần render!
    };

    // 🧹 Cleanup: Đóng WebSocket khi component unmount
    // Return function: React sẽ gọi khi component bị unmount
    return () => ws.close();
    // 💡 Quan trọng: Tránh memory leak, đóng connection
    // 💡 Nếu không cleanup → WebSocket vẫn mở → Memory leak!
  }, [gridApi]); // [gridApi]: Chỉ chạy lại khi gridApi thay đổi

  return (
    <AgGridReact
      onGridReady={(params) => setGridApi(params.api)}
      // 💡 onGridReady: Callback khi grid đã sẵn sàng (đã mount xong)
      // 💡 params: Object chứa thông tin grid
      // 💡 params.api: Grid API object → Lưu vào state để dùng sau
      asyncTransactionWaitMillis={50}
      // ⚡ Batch mỗi 50ms: Gộp updates trong 50ms → render 1 lần
      // 💡 50ms = 20 renders/giây (1000ms ÷ 50ms = 20)
      // 💡 Đủ mượt cho mắt người (mắt chỉ nhận biết ~24 FPS)
      // 💡 Nếu set 16ms = 60 FPS (mượt nhất nhưng tốn CPU hơn)
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
// 🚨 VẤN ĐỀ: Dùng AG Grid cho table nhỏ → Lãng phí bundle size
function SimpleTableBad() {
  const data = [
    { name: 'John', age: 30 }, // 💡 Chỉ 2 rows dữ liệu
    { name: 'Jane', age: 25 },
  ]; // ⚠️ Chỉ 2 rows!

  return (
    <AgGridReact rowData={data} />
    // ❌ 150KB bundle cho 2 rows!
    // 💡 Lãng phí: Tải 150KB code để hiển thị 2 rows
    // 💡 HTML table chỉ cần vài dòng code → 0KB bundle
  );
}

// ✅ Better: Dùng HTML table
// 🎯 Giải pháp: Dùng HTML native cho table đơn giản
function SimpleTableGood() {
  return (
    <table>
      {/* 📋 Header: Tên các cột */}
      <thead>
        <tr>
          <th>Name</th> {/* 💡 Cột 1: Tên */}
          <th>Age</th> {/* 💡 Cột 2: Tuổi */}
        </tr>
      </thead>
      {/* 📊 Body: Dữ liệu các hàng */}
      <tbody>
        <tr>
          <td>John</td> {/* 💡 Hàng 1: John, 30 */}
          <td>30</td>
        </tr>
        <tr>
          <td>Jane</td> {/* 💡 Hàng 2: Jane, 25 */}
          <td>25</td>
        </tr>
      </tbody>
    </table>
    // ✅ 0KB bundle, đơn giản, đủ dùng!
    // 💡 HTML native: Browser render trực tiếp, không cần JS library
    // 💡 Performance: Nhanh hơn, nhẹ hơn cho table nhỏ
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
  const { rowCount, realTime, complexFeatures, budgetForLicense } =
    requirements;

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
console.log(
  chooseDataGrid({
    rowCount: 50000,
    realTime: true,
    complexFeatures: false,
    budgetForLicense: false,
  })
); // → "AG Grid ⭐⭐⭐⭐⭐"

console.log(
  chooseDataGrid({
    rowCount: 500,
    realTime: false,
    complexFeatures: false,
    budgetForLicense: false,
  })
); // → "MUI DataGrid hoặc React Table ⭐⭐⭐"
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

// ✅ Basic Grid - Grid cơ bản nhất
// 🎯 Mục đích: Hiển thị dữ liệu crypto với 3 cột
function CryptoGrid() {
  // 📊 Row Data: Dữ liệu các hàng (rows)
  // useState: React hook để lưu state
  // [rowData]: Destructuring - chỉ lấy giá trị, không cần setter (vì không update)
  const [rowData] = useState([
    { ticker: 'BTCUSDT', price: 50000, volume: 1234 },  // 💰 Bitcoin - object 1
    { ticker: 'ETHUSDT', price: 3000, volume: 5678 }   // 💰 Ethereum - object 2
  ]);
  // 💡 useState: Lưu dữ liệu grid - chỉ khởi tạo 1 lần khi component mount
  // 💡 Mỗi object = 1 row trong grid
  // 💡 ticker: Mã coin (Bitcoin, Ethereum...)
  // 💡 price: Giá hiện tại (USD)
  // 💡 volume: Khối lượng giao dịch

  // 📋 Column Definitions: Định nghĩa các cột (columns)
  // useMemo: React hook để cache giá trị, tránh tính toán lại
  const columnDefs = useMemo(() => [
    { field: 'ticker', headerName: 'Symbol' },   // 📊 Cột 1: Mã coin
    { field: 'price', headerName: 'Price' },      // 💰 Cột 2: Giá
    { field: 'volume', headerName: 'Volume' }     // 📈 Cột 3: Khối lượng
  ], []);
  // ✅ useMemo: Tránh re-create columnDefs mỗi render
  // 💡 () => [...]: Function trả về array column definitions
  // 💡 [] deps: Empty dependency array - chỉ tạo 1 lần khi component mount
  // 💡 field: Tên property trong rowData object (phải khớp với key trong data)
  // 💡 headerName: Text hiển thị ở header cột (tiêu đề cột)

  return (
    // 🎨 Wrapper: Theme + kích thước
    <div className="ag-theme-quartz" style={{ height: 500 }}>
      {/* 💡 ag-theme-quartz: Theme sáng, hiện đại - CSS class từ AG Grid */}
      {/* 💡 style={{ height: 500 }}: Inline style - chiều cao grid 500px */}
      <AgGridReact
        rowData={rowData}           // 📦 Dữ liệu hiển thị - array các objects
        columnDefs={columnDefs}     // 📋 Cấu hình cột - array các column definitions
      />
      {/* 🎯 Kết quả: Grid 3 cột x 2 hàng */}
      {/*
        Grid hiển thị:
        ┌──────────┬────────┬─────────┐
        │ Symbol   │ Price  │ Volume  │
        ├──────────┼────────┼─────────┤
        │ BTCUSDT  │ 50000  │ 1234    │
        │ ETHUSDT  │ 3000   │ 5678    │
        └──────────┴────────┴─────────┘
      */}
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
// 🚨 VẤN ĐỀ: AG Grid dùng index (0, 1, 2...) làm ID mặc định
// 💡 O(n): Độ phức tạp tuyến tính - phải duyệt từ đầu đến cuối
// 💡 Khi update row → Phải duyệt TOÀN BỘ array để tìm: O(n)
// 💡 1,000 rows → Phải check 1,000 lần! (duyệt từ row 0 đến row 999)
// 💡 10,000 rows → Phải check 10,000 lần → CHẬM!
// 💡 Càng nhiều rows → Càng chậm (tỷ lệ thuận)

// ✅ ĐÚNG: Có getRowId → O(1) lookup
<AgGridReact
  rowData={data}
  getRowId={(params) => params.data.ticker} // ✅ Unique ID
  // 💡 getRowId: Function trả về unique ID cho mỗi row
  // 💡 params: Object chứa thông tin row
  // 💡 params.data: Data object của row (VD: { ticker: 'BTCUSDT', price: 50000 })
  // 💡 params.data.ticker: Lấy ticker từ data object (VD: 'BTCUSDT')
  // 💡 ticker phải là unique (không trùng lặp) và stable (không thay đổi)
/>
// ✅ AG Grid tạo Map: { 'BTCUSDT': rowNode, 'ETHUSDT': rowNode }
// 💡 Map/Hash table: Cấu trúc dữ liệu cho phép tìm kiếm O(1)
// 💡 Khi update 'BTCUSDT' → Tìm ngay trong Map: O(1)
// 💡 O(1): Độ phức tạp hằng số - tìm trong 1 bước, không phụ thuộc số lượng rows
// 💡 1,000 rows hay 10,000 rows → Vẫn tìm trong 1 bước!
// 🚀 Nhanh hơn 1000x so với không có getRowId!

/**
 * 📊 Performance Impact:
 * - 1,000 rows: 100ms → 1ms (100x faster)
 * - 10,000 rows: 1000ms → 1ms (1000x faster)
 */
```

### **2.2. applyTransaction - Incremental Updates** ⭐⭐⭐⭐⭐

```typescript
// ❌ SAI: setRowData → Re-render toàn bộ
// 🚨 CÁCH CŨ - CHẬM: Dùng React state để update
const [rowData, setRowData] = useState(initialData);
// 💡 useState: React hook để quản lý state
// 💡 initialData: Dữ liệu ban đầu khi component mount

setRowData((prev) =>
  // 💡 prev: Giá trị hiện tại của rowData
  prev.map(
    // 💡 map(): Duyệt qua từng row trong array
    (row) =>
      row.ticker === ticker
        ? // 💡 So sánh: Nếu ticker khớp với row cần update
          { ...row, price: newPrice } // 💡 Tạo row mới với giá mới
        : // 💡 Spread operator: Copy tất cả properties cũ, ghi đè price
          row // 💡 Giữ nguyên row khác - không thay đổi
  )
);
// 🚨 VẤN ĐỀ:
// 1. setState → React re-render component (toàn bộ component)
// 2. rowData thay đổi → AG Grid nhận props mới (rowData prop thay đổi)
// 3. AG Grid so sánh: rowData cũ vs rowData mới (reference comparison)
// 4. Khác nhau → Re-render TOÀN BỘ grid! (tất cả rows, tất cả cells)
// 5. 10,000 rows × 5 cột = 50,000 cells re-render ❌
// 6. Mất ~500ms, CPU 80-100%, UI giật lag!
// 💡 Vấn đề: Chỉ cần update 1 cell nhưng phải render lại 50,000 cells!

// ✅ ĐÚNG: applyTransaction → Chỉ update 1 row
// 🚀 CÁCH MỚI - NHANH: Dùng Transaction API
const [gridApi, setGridApi] = useState<GridApi | null>(null);
// 💡 gridApi: Object chứa methods để control grid (update, filter, sort...)
// 💡 <GridApi | null>: TypeScript type - có thể là GridApi hoặc null

function updatePrice(ticker: string, newPrice: number) {
  // 💡 ticker: ID của row cần update (VD: 'BTCUSDT')
  // 💡 newPrice: Giá mới cần cập nhật
  if (!gridApi) return; // ⚠️ Guard: Đợi gridApi ready - không làm gì nếu chưa có

  // BƯỚC 1: Lấy row node với O(1) (nhờ getRowId)
  const rowNode = gridApi.getRowNode(ticker);
  // 💡 getRowNode: Method tìm row trong Map → O(1) thay vì O(n)
  // 💡 ticker: ID của row (VD: 'BTCUSDT') - phải khớp với getRowId
  // 💡 rowNode: Object chứa thông tin row (data, index, selected...)
  // 💡 O(1): Tìm trong 1 bước, không cần duyệt array

  if (!rowNode?.data) return; // ⚠️ Guard: Row không tồn tại
  // 💡 Optional chaining (?.): Nếu rowNode null/undefined → return
  // 💡 Nếu rowNode.data không tồn tại → return (không update)

  // BƯỚC 2: Tạo data mới (immutable - QUAN TRỌNG!)
  const updatedData = { ...rowNode.data, price: newPrice };
  // 💡 Spread operator (...): Copy tất cả properties từ rowNode.data
  // 💡 Ghi đè price với giá mới (price: newPrice)
  // 💡 Tạo object MỚI với địa chỉ bộ nhớ mới → AG Grid detect thay đổi
  // 💡 Immutable: Không sửa object cũ, tạo object mới

  // BƯỚC 3: Update chỉ 1 row qua Transaction API
  gridApi.applyTransaction({ update: [updatedData] });
  // 💡 applyTransaction: Method update grid với incremental update
  // 💡 { update: [...] }: Object chứa array các rows cần update
  // 💡 AG Grid chỉ update rows trong array, không re-render toàn bộ
  // ✅ AG Grid chỉ re-render:
  //    - 1 row (thay vì 10,000 rows) - chỉ row có ticker khớp
  //    - 5 cells (thay vì 50,000 cells) - chỉ cells trong row đó
  //    - Mất ~2ms (thay vì 500ms) - nhanh hơn 250 lần!
  //    - CPU 5-10% (thay vì 80-100%) - tiết kiệm CPU
  //    - UI mượt mà! - không giật lag
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
// 🚨 VẤN ĐỀ: Render ngay mỗi lần có update
socket.on('price-update', (update) => {
  // 💡 socket.on: Event listener - lắng nghe event 'price-update'
  // 💡 update: Object chứa thông tin giá mới (VD: { ticker: 'BTCUSDT', price: 50001 })
  gridApi.applyTransaction({ update: [update] });
  // ⚠️ Render ngay lập tức! - không đợi, không batch
  // 💡 applyTransaction: Sync - render ngay khi gọi
  // 💡 Mỗi lần có update → render ngay → tốn CPU
});
// 🚨 KẾT QUẢ:
// → 100 updates/s → 100 renders/s → CPU 70%
// 💡 100 updates/giây: Server gửi 100 lần update trong 1 giây
// 💡 100 renders/s: Grid render 100 lần trong 1 giây
// 💡 Browser chỉ refresh 60 lần/giây (60 FPS - Frames Per Second)
// 💡 40 lần render BỊ LÃNG PHÍ! (browser không kịp hiển thị)
// 💡 CPU cao (70%), UI giật lag ❌
// 💡 Vấn đề: Render nhiều hơn mức cần thiết

// ✅ ĐÚNG: Async transaction → Batch renders
// 🚀 GIẢI PHÁP: Gộp nhiều updates thành 1 render
const gridOptions = {
  asyncTransactionWaitMillis: 50,
  // ⚡ Gộp updates mỗi 50ms - delay trước khi render
  // 💡 AG Grid sẽ đợi 50ms, gộp TẤT CẢ updates trong khoảng đó
  // 💡 Sau 50ms → Render 1 lần duy nhất với tất cả updates
  // 💡 50ms: Thời gian đợi để batch - cân bằng giữa responsive và performance
};

socket.on('price-update', (update) => {
  // 💡 socket.on: Event listener - lắng nghe event 'price-update'
  gridApi.applyTransactionAsync({ update: [update] });
  // ✅ applyTransactionAsync: Async - thêm vào queue, không render ngay
  // 💡 update: Object chứa thông tin giá mới
  // 💡 AG Grid sẽ đợi 50ms, gộp nhiều updates lại, sau đó render 1 lần
});
// ✅ KẾT QUẢ:
// → 100 updates/s → CHỈ 20 renders/s (1000ms ÷ 50ms = 20)
// 💡 100 updates/giây: Server gửi 100 lần update
// 💡 20 renders/s: Grid chỉ render 20 lần (gộp 5 updates mỗi lần)
// 💡 Giảm 80% số lần render! (100 → 20)
// → CPU 15% (thay vì 70%) - giảm 79%!
// 💡 CPU giảm 79%! (70% → 15%)
// → UI mượt mà, FPS ổn định 60 ✅
// 💡 FPS 60: 60 frames/giây - mượt mà, không giật lag

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
// 🚨 VẤN ĐỀ: Sửa trực tiếp object gốc
rowNode.data.price = newPrice;
// ⚠️ Sửa trực tiếp object gốc → Vẫn cùng địa chỉ bộ nhớ
// 💡 Mutable: Thay đổi object gốc, không tạo object mới
// 💡 rowNode.data vẫn trỏ đến cùng địa chỉ bộ nhớ (memory address)
gridApi.applyTransaction({ update: [rowNode.data] });
// 🚨 VẤN ĐỀ:
// 1. rowNode.data vẫn trỏ đến ĐỊA CHỈ BỘ NHỚ cũ
// 💡 Reference (tham chiếu) không thay đổi - vẫn cùng object
// 2. AG Grid so sánh: oldRef === newRef → TRUE (cùng địa chỉ)
// 💡 Reference comparison: So sánh địa chỉ bộ nhớ, không so sánh giá trị
// 💡 oldRef === newRef: Cùng địa chỉ → AG Grid nghĩ không có gì thay đổi
// 3. AG Grid kết luận: "Không có gì thay đổi"
// 💡 AG Grid bỏ qua update vì nghĩ data không thay đổi
// 4. UI KHÔNG cập nhật, user vẫn thấy giá cũ ❌
// 💡 Grid không re-render → UI không cập nhật → User thấy giá cũ

// ✅ ĐÚNG: Immutable (tạo object mới)
// 🚀 GIẢI PHÁP: Tạo object mới với địa chỉ bộ nhớ mới
const updatedData = {
  ...rowNode.data, // 📦 Spread: Copy TẤT CẢ properties từ rowNode.data
  price: newPrice, // 🔧 Ghi đè property mới - thay thế giá cũ
};
// 💡 { ...obj } tạo object MỚI với ĐỊA CHỈ BỘ NHỚ mới
// 💡 Spread operator: Copy tất cả properties, sau đó ghi đè price
// 💡 Giống như Ctrl+C Ctrl+V: Tạo file copy, không sửa file gốc
// 💡 Immutable: Không thay đổi object cũ, tạo object mới

gridApi.applyTransaction({ update: [updatedData] });
// ✅ HOẠT ĐỘNG:
// 1. updatedData có ĐỊA CHỈ BỘ NHỚ mới
// 💡 Object mới → địa chỉ bộ nhớ khác với object cũ
// 2. AG Grid so sánh: oldRef !== newRef → TRUE (khác địa chỉ)
// 💡 Reference comparison: So sánh địa chỉ bộ nhớ
// 💡 oldRef !== newRef: Khác địa chỉ → AG Grid phát hiện thay đổi
// 3. AG Grid kết luận: "Có thay đổi!"
// 💡 AG Grid nhận biết data đã thay đổi → cần update
// 4. Re-render cell với giá mới ✅
// 💡 Grid re-render cell price → UI hiển thị giá mới

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
// 🎯 Mục đích: Hiển thị giá crypto cập nhật theo thời gian thực từ Binance
function CryptoGrid() {
  // 🔧 State: Lưu Grid API để control grid
  // useState: React hook để quản lý state
  const [gridApi, setGridApi] = useState<GridApi | null>(null);
  // 💡 gridApi: Object chứa methods để update grid (applyTransaction, getRowNode...)
  // 💡 <GridApi | null>: TypeScript type - có thể là GridApi hoặc null
  // 💡 null ban đầu vì grid chưa ready (chưa mount xong)

  // useEffect: React hook chạy sau khi component render
  useEffect(() => {
    if (!gridApi) return; // ⚠️ Guard: Đợi gridApi ready - không làm gì nếu chưa có

    // 🌐 WebSocket: Kết nối đến Binance streaming API
    // 💡 WebSocket: Protocol 2 chiều, server có thể push data đến client real-time
    // 💡 wss:// = WebSocket Secure (HTTPS cho WebSocket) - kết nối an toàn
    const ws = new WebSocket('wss://stream.binance.com/ws');
    // 💡 Binance WebSocket: Stream giá crypto real-time - cập nhật liên tục
    // 💡 URL: Binance WebSocket endpoint để nhận giá crypto

    // 📨 Event: Nhận message từ WebSocket
    // onmessage: Event handler khi server gửi data đến
    ws.onmessage = (event) => {
      // event.data: String JSON từ server (VD: '{"s":"BTCUSDT","c":"50000.5","v":"1234.56"}')
      const update = JSON.parse(event.data);
      // 💡 Parse JSON: Convert string → JavaScript object
      // 💡 update: Object chứa thông tin giá mới
      // 💡 VD: { s: 'BTCUSDT', c: '50000.5', v: '1234.56' }
      // 💡 s: Symbol (mã coin), c: Current price (giá hiện tại), v: Volume (khối lượng)

      // ⚡ Update grid với Transaction API (async batching)
      gridApi.applyTransactionAsync({
        update: [
          {
            ticker: update.s, // 💡 Symbol (VD: 'BTCUSDT') - mã coin
            price: parseFloat(update.c), // 💡 Current price (convert string → number)
            // 💡 parseFloat(): Chuyển string '50000.5' → number 50000.5
            volume: parseFloat(update.v), // 💡 Volume (convert string → number)
            // 💡 parseFloat(): Chuyển string '1234.56' → number 1234.56
          },
        ],
      });
      // ✅ applyTransactionAsync: Gộp nhiều updates → render 1 lần
      // 💡 Async: Thêm vào queue, không render ngay
      // 💡 Batching: Nếu có 10 updates trong 50ms → chỉ render 1 lần
      // 💡 Performance: Giảm 80-90% số lần render!
      // 💡 Thay vì render 100 lần/giây → chỉ render 20 lần/giây
    };

    // 🧹 Cleanup: Đóng WebSocket khi component unmount
    // Return function: React sẽ gọi khi component bị unmount
    return () => ws.close();
    // 💡 Quan trọng: Tránh memory leak, đóng connection
    // 💡 Nếu không cleanup → WebSocket vẫn mở → Memory leak!
    // 💡 ws.close(): Đóng kết nối WebSocket, giải phóng tài nguyên
  }, [gridApi]); // [gridApi]: Chỉ chạy lại khi gridApi thay đổi

  return (
    <AgGridReact
      onGridReady={(params) => setGridApi(params.api)}
      // 💡 onGridReady: Callback khi grid đã sẵn sàng (đã mount xong)
      // 💡 params: Object chứa thông tin grid
      // 💡 params.api: Grid API object → Lưu vào state để dùng sau
      getRowId={(params) => params.data.ticker}
      // ⚡ O(1) lookup: Dùng ticker làm unique ID
      // 💡 params.data.ticker: Lấy ticker từ data (VD: 'BTCUSDT')
      // 💡 Cho phép tìm row nhanh khi update - không cần duyệt array
      asyncTransactionWaitMillis={50}
      // ⚡ Batch mỗi 50ms: Gộp updates trong 50ms → render 1 lần
      // 💡 50ms = 20 renders/giây (1000ms ÷ 50ms = 20)
      // 💡 Đủ mượt cho mắt người (mắt chỉ nhận biết ~24 FPS)
      // 💡 Cân bằng giữa responsive và performance
    />
  );
}
```

### **3.2. Cell Flash (Visual Feedback)**

```typescript
// 🎨 Column Definition: Cấu hình cột price với flash animation
// columnDefs: Array các object định nghĩa cột
const columnDefs = [
  {
    field: 'price',                              // 💡 Tên field trong data - phải khớp với key trong rowData
    enableCellChangeFlash: true,                  // ✅ Flash khi value thay đổi
    // 💡 enableCellChangeFlash: Bật animation flash khi giá thay đổi
    // 💡 Flash: Cell sẽ highlight (đổi màu nền) khi giá trị thay đổi
    // 💡 User dễ nhận biết cell nào vừa update - visual feedback

    // 🎨 Cell Class Rules: Dynamic CSS classes dựa trên giá trị
    // cellClassRules: Object chứa các rules để thêm/xóa CSS classes
    cellClassRules: {
      'price-up': (params) => params.value > params.oldValue,
      // 💡 'price-up': Tên CSS class sẽ được thêm vào cell
      // 💡 (params) => ...: Function trả về boolean - true = thêm class, false = xóa class
      // 💡 params.value: Giá hiện tại của cell
      // 💡 params.oldValue: Giá trước đó của cell
      // 💡 Giá tăng → Thêm class 'price-up' → Màu xanh
      // 💡 AG Grid tự động thêm/xóa class khi giá trị thay đổi

      'price-down': (params) => params.value < params.oldValue,
      // 💡 'price-down': Tên CSS class sẽ được thêm vào cell
      // 💡 params.value < params.oldValue: Giá hiện tại < giá cũ → giá giảm
      // 💡 Giá giảm → Thêm class 'price-down' → Màu đỏ
    }
  }
];

// 🎨 CSS: Định nghĩa styles cho các classes
.price-up {
  background-color: #00ff0030;  // 💡 Xanh lá với độ trong suốt 30%
  // 💡 #00ff00 = Xanh lá (RGB: 0, 255, 0)
  // 💡 30 = 30% opacity (hex) - trong suốt 30%, hiển thị 70%
  // 💡 Kết quả: Nền xanh lá nhạt khi giá tăng
}
.price-down {
  background-color: #ff000030;  // 💡 Đỏ với độ trong suốt 30%
  // 💡 #ff0000 = Đỏ (RGB: 255, 0, 0)
  // 💡 30 = 30% opacity (hex) - trong suốt 30%, hiển thị 70%
  // 💡 Kết quả: Nền đỏ nhạt khi giá giảm
}
// 💡 Kết quả: Cell flash màu xanh khi giá tăng, đỏ khi giá giảm
// 💡 User dễ nhận biết cell nào vừa thay đổi và thay đổi theo hướng nào
```

---

## **4. Column Definitions** 📊

```typescript
// 📋 Column Definitions: Định nghĩa các cột của grid
// useMemo: React hook để cache giá trị, tránh tính toán lại
const columnDefs = useMemo(
  () => [
    // 📊 Basic column: Cột đơn giản
    {
      field: 'ticker', // 💡 Tên field trong data - phải khớp với key trong rowData
      headerName: 'Symbol', // 💡 Text hiển thị ở header cột (tiêu đề cột)
      width: 120, // 💡 Độ rộng cố định (120px) - không thay đổi khi resize
      // 💡 width: Cố định, không tự động điều chỉnh
    },

    // 💰 Value formatter: Format giá trị hiển thị
    {
      field: 'price',
      valueFormatter: (params) => `$${params.value.toFixed(2)}`,
      // 💡 valueFormatter: Function format giá trị trước khi hiển thị
      // 💡 params: Object chứa thông tin cell
      // 💡 params.value: Giá trị gốc (VD: 50000.5) - number
      // 💡 toFixed(2): Làm tròn 2 chữ số thập phân (VD: 50000.50)
      // 💡 Template string: `$${...}` - thêm ký tự $ ở đầu
      // 💡 Kết quả: "$50000.50" - string được hiển thị trong cell
    },

    // 🎨 Cell class rules: Conditional styling (màu sắc theo điều kiện)
    {
      field: 'change24h', // 💡 Thay đổi giá trong 24h (%) - VD: +5.23% hoặc -2.15%
      cellClassRules: {
        // 💡 cellClassRules: Object chứa các rules để thêm/xóa CSS classes
        'text-green': (params) => params.value > 0,
        // 💡 'text-green': Tên CSS class sẽ được thêm vào cell
        // 💡 (params) => params.value > 0: Function trả về boolean
        // 💡 params.value > 0: Giá tăng (> 0) → true → Thêm class 'text-green' → Màu xanh
        'text-red': (params) => params.value < 0,
        // 💡 'text-red': Tên CSS class sẽ được thêm vào cell
        // 💡 params.value < 0: Giá giảm (< 0) → true → Thêm class 'text-red' → Màu đỏ
        // 💡 AG Grid tự động thêm/xóa class khi giá trị thay đổi
      },
    },

    // 📊 Column group: Nhóm các cột liên quan
    {
      headerName: 'Statistics', // 💡 Tên header nhóm - hiển thị ở trên các cột con
      children: [
        // 💡 children: Array các cột con trong nhóm
        { field: 'high24h', headerName: '24h High' }, // 💡 Giá cao nhất 24h
        { field: 'low24h', headerName: '24h Low' }, // 💡 Giá thấp nhất 24h
        // 💡 Các cột này sẽ được nhóm dưới header "Statistics"
      ],
    },
  ],
  [] // Empty dependency array
);
// ✅ useMemo → Chỉ tạo 1 lần khi component mount
// 💡 () => [...]: Function trả về array column definitions
// 💡 [] deps: Empty dependency array - không phụ thuộc vào props/state nào
// 💡 Tránh re-create columnDefs mỗi render → Tối ưu performance
// 💡 Nếu không dùng useMemo → columnDefs tạo mới mỗi render → Grid re-configure → Chậm!
```

---

## **5. Best Practices** 💡

### **✅ DO (NÊN LÀM):**

```typescript
// 1️⃣ Always use getRowId - LUÔN dùng getRowId
<AgGridReact getRowId={(params) => params.data.id} />
// ⚡ QUAN TRỌNG: O(1) lookup thay vì O(n)
// 💡 Nhanh hơn 1000x khi tìm row để update
// 💡 Bắt buộc cho real-time updates

// 2️⃣ Use applyTransactionAsync for high-frequency - Dùng cho updates nhiều
gridApi.applyTransactionAsync({ update: [data] });
// ⚡ Batching: Gộp nhiều updates → giảm 80% renders
// 💡 Dùng cho WebSocket, real-time data
// 💡 asyncTransactionWaitMillis: 50ms (khuyến nghị)

// 3️⃣ Immutable data - Dữ liệu bất biến
const updated = { ...oldData, field: newValue };
// ⚡ QUAN TRỌNG: Tạo object mới, không mutate object cũ
// 💡 AG Grid dùng reference comparison → Cần object mới
// 💡 Spread operator: { ...obj } tạo copy mới

// 4️⃣ useMemo for columnDefs - Tối ưu column definitions
const columnDefs = useMemo(() => [...], []);
// ⚡ Tránh re-create columnDefs mỗi render
// 💡 Giảm 50-100ms mỗi render cycle
// 💡 [] deps: Chỉ tạo 1 lần khi mount

// 5️⃣ Cleanup subscriptions - Dọn dẹp subscriptions
useEffect(() => {
  const ws = new WebSocket('...');
  return () => ws.close();  // 🧹 Cleanup khi unmount
}, []);
// ⚡ QUAN TRỌNG: Tránh memory leak
// 💡 Đóng WebSocket, unsubscribe events
// 💡 Return cleanup function trong useEffect
```

### **❌ DON'T (KHÔNG NÊN):**

```typescript
// 1️⃣ setRowData cho updates - KHÔNG dùng setRowData để update
setRowData(prev => prev.map(...));
// ❌ Re-render toàn bộ grid
// 🚨 VẤN ĐỀ: 10,000 rows → 50,000 cells re-render
// 💡 Thay vào đó: Dùng applyTransactionAsync

// 2️⃣ Mutable data - KHÔNG mutate object trực tiếp
rowNode.data.price = newPrice;
// ❌ AG Grid không detect thay đổi
// 🚨 VẤN ĐỀ: oldRef === newRef → AG Grid nghĩ không có gì thay đổi
// 💡 Thay vào đó: const updated = { ...rowNode.data, price: newPrice }

// 3️⃣ Recreate columnDefs mỗi render - KHÔNG tạo lại columnDefs
const columnDefs = [{ field: 'ticker' }];
// ❌ Re-configure grid mỗi lần render
// 🚨 VẤN ĐỀ: Grid phải setup lại → Chậm, tốn CPU
// 💡 Thay vào đó: useMemo(() => [...], [])

// 4️⃣ Bind trong columnDefs - KHÔNG bind trong columnDefs
cellRenderer: this.MyRenderer.bind(this)
// ❌ New function mỗi lần → ColumnDefs thay đổi
// 🚨 VẤN ĐỀ: Grid re-configure columns → Chậm
// 💡 Thay vào đó: Dùng arrow function hoặc useCallback

// 5️⃣ Forget cleanup - KHÔNG quên cleanup
const ws = new WebSocket('...');
// ❌ Memory leak: WebSocket không đóng
// 🚨 VẤN ĐỀ: Component unmount → WebSocket vẫn mở → Memory leak
// 💡 Thay vào đó: return () => ws.close() trong useEffect
```

---

## **6. Common Use Cases** 🎯

### **6.1. Crypto Trading Dashboard**

```typescript
// 🎯 Use Case: Crypto Trading Dashboard
// 💡 Mục đích: Hiển thị giá crypto với real-time updates
function CryptoTrading() {
  // 📋 Column Definitions: Định nghĩa các cột
  const columnDefs = useMemo(
    () => [
      {
        field: 'ticker',
        pinned: 'left', // 📌 Ghim cột ticker bên trái (luôn hiển thị khi scroll)
        // 💡 pinned: 'left' | 'right' | null
        // 💡 Khi scroll ngang → Cột ticker vẫn hiển thị
      },
      {
        field: 'price',
        valueFormatter: (p) => `$${p.value.toFixed(2)}`,
        // 💡 Format giá: $50000.50
        enableCellChangeFlash: true,
        // ⚡ Flash animation khi giá thay đổi
        // 💡 User dễ nhận biết cell nào vừa update
      },
      {
        field: 'change24h', // 💡 Thay đổi giá trong 24h (%)
        valueFormatter: (p) =>
          `${p.value > 0 ? '+' : ''}${p.value.toFixed(2)}%`,
        // 💡 Format: +5.23% hoặc -2.15%
        // 💡 Thêm dấu + nếu giá tăng
        cellClassRules: {
          'text-green': (p) => p.value > 0, // 💡 Giá tăng → Xanh
          'text-red': (p) => p.value < 0, // 💡 Giá giảm → Đỏ
        },
      },
    ],
    []
  ); // ✅ useMemo: Chỉ tạo 1 lần

  return (
    <AgGridReact
      columnDefs={columnDefs} // 📋 Cấu hình cột
      getRowId={(params) => params.data.ticker} // ⚡ O(1) lookup
      asyncTransactionWaitMillis={50} // ⚡ Batch 50ms
      enableCellChangeFlash={true} // ⚡ Flash animation
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
        { field: 'total' },
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
  getRowId={(params) => params.data.id} // ⭐ O(1) lookup
  asyncTransactionWaitMillis={50} // ⭐ Batching
  onGridReady={(params) => setGridApi(params.api)} // ⭐ API access
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
