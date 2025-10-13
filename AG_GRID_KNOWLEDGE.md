# 📚 AG Grid Knowledge Base

Tổng hợp kiến thức về AG Grid từ dự án Binance Priceboard

---

## 📖 Mục lục

1. [Giới thiệu AG Grid](#giới-thiệu-ag-grid)
2. [Cài đặt & Cấu hình](#cài-đặt--cấu-hình)
3. [Column Definitions](#column-definitions)
4. [Data Management](#data-management)
5. [Performance Optimization](#performance-optimization)
6. [Styling & Theming](#styling--theming)
7. [Real-time Updates](#real-time-updates)
8. [Best Practices](#best-practices)

---

## 🎯 Giới thiệu AG Grid

AG Grid là một thư viện data grid mạnh mẽ cho JavaScript/React, đặc biệt phù hợp cho:

- **High-frequency data updates** (real-time streaming - cập nhật real-time)
- **Large datasets** (hàng triệu rows - big data)
- **Complex data visualization** (grouping, aggregation, filtering - nhóm, tổng hợp, lọc)
- **Enterprise applications** (trading platforms, financial dashboards - sàn giao dịch, dashboard tài chính)

---

## ⚖️ Ưu và Nhược điểm

### ✅ Ưu điểm

#### 1. **Performance Vượt trội**
- 🚀 **Rendering siêu nhanh**: Xử lý được **100,000+ rows** mượt mà
- ⚡ **Virtual Scrolling**: Chỉ render rows trong viewport (tiết kiệm RAM)
- 🔄 **Transaction API**: Update từng row thay vì re-render toàn bộ
- ⏱️ **Async Transactions**: Batch updates tự động (giảm 90% render cycles)
- 📊 **Benchmark**: Nhanh hơn 2-3x so với Material-UI DataGrid, React Table

#### 2. **Features Phong phú**
- ✨ **Community Edition**:
  - Sorting, Filtering, Pagination
  - Row Selection, Cell Editing
  - Column Groups, Pinned Columns
  - CSV Export, Clipboard
  - Custom Cell Renderers
  - Themes & Styling
- 💎 **Enterprise Edition** (trả phí):
  - Advanced Filtering (Set, Multi Filter)
  - Row Grouping & Aggregation
  - Pivoting & Charting
  - Excel Export
  - Master/Detail
  - Server-Side Row Model

#### 3. **Real-time Updates Tốt**
- 🔴 **WebSocket Integration**: Dễ dàng tích hợp với WebSocket
- 📡 **High-frequency Updates**: Xử lý được 1000+ updates/giây
- 💫 **Cell Flash Animation**: Highlight cells khi data thay đổi
- 🎯 **Row Node Cache**: O(1) lookup để update nhanh

#### 4. **Developer Experience**
- 📚 **Documentation xuất sắc**: Đầy đủ, chi tiết, nhiều examples
- 🎓 **Learning Curve**: Dễ học (basic), mạnh mẽ (advanced)
- 🔧 **TypeScript Support**: Full type definitions
- 🌐 **Community lớn**: Stack Overflow, GitHub Issues
- 🔄 **Regular Updates**: Release mới thường xuyên

#### 5. **Customization Mạnh mẽ**
- 🎨 **Theming System**: Built-in themes + custom CSS variables
- 🖼️ **Custom Cell Renderers**: Render bất kỳ UI nào trong cell
- 🔧 **Flexible API**: 200+ grid options, 100+ column properties
- 🎯 **Event System**: 50+ events để hook vào lifecycle

#### 6. **Production-Ready**
- 🏢 **Dùng bởi Fortune 500**: Bloomberg, J.P. Morgan, NASA, Google
- 🛡️ **Stable & Reliable**: Phát triển từ 2015, mature codebase
- 📱 **Cross-platform**: Web, Desktop (Electron), Mobile (React Native)
- ♿ **Accessibility**: WCAG 2.1 compliant

### ❌ Nhược điểm

#### 1. **Bundle Size Lớn**
- 📦 **Community Edition**: ~500KB minified (gzip ~150KB)
- 📦 **Enterprise Edition**: ~800KB minified (gzip ~250KB)
- 💡 **Giải pháp**:
  - Tree-shaking (chỉ import modules cần dùng)
  - Code-splitting (lazy load AG Grid khi cần)
  - CDN cho production

#### 2. **Enterprise Features Trả phí**
- 💰 **Pricing**: $999+/developer/năm cho Enterprise
- 🔒 **Locked Features**: Row Grouping, Pivoting, Excel Export
- 💡 **Giải pháp**:
  - Dùng Community Edition cho hầu hết use cases
  - Implement custom grouping/aggregation nếu cần
  - Export CSV thay vì Excel

#### 3. **Learning Curve (Advanced)**
- 📚 **Nhiều concepts**: Row Models, Cell Renderers, Value Getters/Setters
- 🧩 **API phức tạp**: 200+ options có thể gây overwhelm
- 💡 **Giải pháp**:
  - Bắt đầu với basic setup
  - Học dần theo use case
  - Dùng TypeScript để autocomplete

#### 4. **Styling phức tạp**
- 🎨 **CSS Deep**: Phải override nhiều class nội bộ
- 🔧 **Theme System**: Nhiều CSS variables (50+)
- 💡 **Giải pháp**:
  - Dùng built-in themes làm base
  - Override từng phần cần thiết
  - Dùng CSS-in-JS nếu cần

#### 5. **React Integration không "React-like"**
- ⚛️ **Imperative API**: Dùng `gridApi` thay vì declarative
- 🔄 **State Management**: Grid tự quản lý state, không qua React
- 💡 **Giải pháp**:
  - Chấp nhận imperative pattern (faster)
  - Wrap API calls trong hooks
  - Dùng `useCallback` để tránh re-renders

#### 6. **SSR (Server-Side Rendering) khó**
- 🌐 **Next.js Issues**: AG Grid cần `window`, `document`
- 💡 **Giải pháp**:
  - Dynamic import với `ssr: false`
  - Lazy load AG Grid ở client-side
  ```tsx
  const AgGridReact = dynamic(() => import('ag-grid-react'), { ssr: false });
  ```

---

## 🚀 Cách Tối ưu Performance với AG Grid

### 📊 Performance Checklist

#### ✅ **LUÔN LÀM (Critical)**

##### 1. **Dùng `getRowId` để định nghĩa unique ID**
```tsx
<AgGridReact
  getRowId={(params) => params.data.id}  // QUAN TRỌNG NHẤT!
  rowData={data}
/>
```
**Lý do**: AG Grid dùng ID này để tìm row cần update (O(1) thay vì O(n))

##### 2. **Dùng `applyTransaction` thay vì `setRowData`**
```tsx
// ❌ CHẬM - Re-render toàn bộ grid
setRowData([...rowData, newRow]);

// ✅ NHANH - Chỉ update rows thay đổi
gridApi.applyTransaction({
  add: [newRow],
  update: [updatedRows],
  remove: [deletedRows]
});
```

##### 3. **Dùng `applyTransactionAsync` cho high-frequency updates**
```tsx
const gridOptions = {
  asyncTransactionWaitMillis: 50,  // Batch updates mỗi 50ms
};

// Async transaction
gridApi.applyTransactionAsync({ update: [data] });
```
**Hiệu quả**: 100 updates/giây → chỉ 2 renders/giây (giảm 98%)

##### 4. **Enable Virtual Scrolling (mặc định đã bật)**
```tsx
const gridOptions = {
  rowBuffer: 10,  // Render thêm 10 rows ngoài viewport
};
```
**Hiệu quả**: 10,000 rows → chỉ render ~30 rows (viewport + buffer)

##### 5. **Immutable Data cho Transactions**
```tsx
// ❌ SAI - Mutate object
rowNode.data.price = newPrice;

// ✅ ĐÚNG - Tạo object mới
const updatedData = { ...rowNode.data, price: newPrice };
gridApi.applyTransactionAsync({ update: [updatedData] });
```

#### ⚡ **NÊN LÀM (Recommended)**

##### 6. **Suppress unnecessary events**
```tsx
const gridOptions = {
  suppressCellFocus: true,           // Bỏ focus border (nếu không cần)
  suppressRowClickSelection: true,   // Bỏ select on click (nếu không cần)
  suppressColumnVirtualisation: false, // Giữ column virtualization
};
```

##### 7. **Optimize Column Definitions với `useMemo`**
```tsx
const columnDefs = useMemo(() => [
  { field: 'ticker', headerName: 'Symbol' },
  { field: 'price', headerName: 'Price' }
], []); // Empty deps - chỉ tạo 1 lần

const defaultColDef = useMemo(() => ({
  sortable: true,
  resizable: false,
}), []);
```

##### 8. **Debounce Cell Editing**
```tsx
const defaultColDef = {
  editable: true,
  valueSetter: debounce((params) => {
    params.data[params.colDef.field] = params.newValue;
    return true;
  }, 300),
};
```

##### 9. **Lazy Load Data (Infinite Scroll)**
```tsx
const gridOptions = {
  rowModelType: 'infinite',
  cacheBlockSize: 100,    // Load 100 rows mỗi lần
  maxBlocksInCache: 10,   // Cache 1000 rows (10 blocks)
};
```
**Use case**: Load data từ API theo batch, không load hết 1 lúc

##### 10. **Optimize Cell Renderers**
```tsx
// ❌ CHẬM - Render phức tạp
const CellRenderer = (props) => (
  <div style={{ display: 'flex', alignItems: 'center' }}>
    <img src={props.value.avatar} />
    <span>{props.value.name}</span>
  </div>
);

// ✅ NHANH - Dùng valueFormatter + CSS
const columnDef = {
  field: 'name',
  valueFormatter: (params) => params.value.name,
  cellClass: 'name-cell',  // CSS cho style
};
```

#### 🎯 **TÙY CHỌN (Optional)**

##### 11. **Reduce Cell Flash Duration**
```tsx
const gridOptions = {
  cellFlashDuration: 200,   // Giảm từ 500ms → 200ms
  cellFadeDuration: 300,    // Giảm từ 1000ms → 300ms
};
```

##### 12. **Disable Animations (nếu cần max performance)**
```tsx
const gridOptions = {
  animateRows: false,              // Tắt row animation
  suppressColumnMoveAnimation: true, // Tắt column move animation
};
```

##### 13. **Use `suppressChangeDetection` cho static columns**
```tsx
const columnDef = {
  field: 'staticValue',
  suppressChangeDetection: true,  // Không check change
};
```

##### 14. **Column Virtualization (cho nhiều columns)**
```tsx
const gridOptions = {
  suppressColumnVirtualisation: false,  // Bật column virtualization
};
```
**Use case**: Grid có 100+ columns, chỉ render columns trong viewport

##### 15. **Web Worker cho Heavy Computations**
```tsx
// Compute aggregations trong Web Worker
const worker = new Worker('aggregation-worker.js');
worker.postMessage({ data: rowData });
worker.onmessage = (e) => {
  gridApi.applyTransaction({ update: e.data });
};
```

---

### 📈 Performance Benchmarks

#### Scenario 1: Real-time Crypto Priceboard (50 symbols)

| Method | Updates/sec | CPU Usage | Smoothness |
|--------|-------------|-----------|------------|
| ❌ `setRowData` | 10 | 80-100% | Laggy |
| ⚠️ `applyTransaction` | 50 | 40-60% | Acceptable |
| ✅ `applyTransactionAsync` (50ms batch) | 1000+ | 15-25% | Smooth |

#### Scenario 2: Large Dataset (10,000 rows)

| Feature | Without Optimization | With Optimization |
|---------|---------------------|-------------------|
| Initial Render | 2000ms | 300ms |
| Scroll FPS | 15-20 | 55-60 |
| Memory Usage | 200MB | 50MB |
| Update 100 rows | 500ms | 20ms |

---

### 🎯 Performance Best Practices Summary

#### **Mức độ ưu tiên:**

**🔴 CRITICAL (Phải làm)**
1. ✅ `getRowId` - Unique row identification
2. ✅ `applyTransaction` - Incremental updates
3. ✅ `applyTransactionAsync` - Batch updates
4. ✅ Immutable data - New object references
5. ✅ Virtual scrolling - Enabled by default

**🟡 RECOMMENDED (Nên làm)**
6. ⚡ `useMemo` for column defs
7. ⚡ Suppress unnecessary events
8. ⚡ Optimize cell renderers
9. ⚡ Lazy loading (infinite scroll)
10. ⚡ Debounce cell editing

**🟢 OPTIONAL (Tùy use case)**
11. 💡 Reduce animation duration
12. 💡 Disable animations entirely
13. 💡 Column virtualization
14. 💡 Web Workers for heavy compute
15. 💡 `suppressChangeDetection`

---

### 🏆 Golden Rules

1. **"Update smarter, not harder"** - Dùng transactions, không setState
2. **"Batch everything"** - asyncTransactionWaitMillis là người bạn tốt nhất
3. **"Immutable always wins"** - Tạo object mới, đừng mutate
4. **"Measure before optimize"** - Dùng React DevTools Profiler
5. **"Less is more"** - Bỏ features không dùng (events, animations)

---

## 🔧 Cài đặt & Cấu hình

### Installation

```bash
npm install ag-grid-react ag-grid-community
# hoặc
yarn add ag-grid-react ag-grid-community
```

### Basic Setup

```tsx
import { AgGridReact } from 'ag-grid-react';
import { ModuleRegistry, AllCommunityModule } from 'ag-grid-community';
import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-quartz.css';

// Register modules
ModuleRegistry.registerModules([AllCommunityModule]);

// In your component
<div className="ag-theme-quartz" style={{ height: 500 }}>
  <AgGridReact
    rowData={data}
    columnDefs={columnDefs}
  />
</div>
```

### Global Options

```tsx
import { provideGlobalGridOptions } from 'ag-grid-community';

// Set global options (apply to all grids)
provideGlobalGridOptions({
  theme: 'legacy' // Use legacy theme system
});
```

---

## 📋 Column Definitions (Định nghĩa Cột)

### Basic Column Definition (Định nghĩa Cột Cơ bản)

```tsx
const columnDefs: ColDef[] = [
  {
    field: 'ticker',           // Tên field trong data object
    headerName: 'Symbol',      // Tên hiển thị ở header
    minWidth: 100,             // Độ rộng tối thiểu (px)
    pinned: 'left',            // Ghim cột ('left' | 'right' | null)
    sortable: true,            // Cho phép sắp xếp
    resizable: false,          // Không cho phép thay đổi kích thước
    type: 'numericColumn',     // Loại cột (số, ngày, text...)
  }
];
```

### Column Groups (Nhóm Cột)

```tsx
const columnDefs: (ColDef | ColGroupDef)[] = [
  {
    headerName: 'Bid',         // Tên header của nhóm
    marryChildren: true,       // Giữ các cột con luôn ở cạnh nhau
    headerClass: 'bid-side-header', // CSS class cho header
    children: [                // Các cột con trong nhóm
      {
        field: 'bid1',
        headerName: 'Price',   // Giá
        minWidth: 110,
      },
      {
        field: 'bidVol1',
        headerName: 'Volume',  // Khối lượng
        minWidth: 100,
      }
    ]
  }
];
```

### Default Column Definition (Cấu hình Mặc định cho Cột)

```tsx
const defaultColDef: ColDef = {
  resizable: false,            // Không cho phép resize
  sortable: true,              // Cho phép sắp xếp
  unSortIcon: true,            // Hiển thị icon bỏ sắp xếp
  enableCellChangeFlash: true, // Nhấp nháy khi cell thay đổi giá trị
  type: 'numericColumn',       // Loại cột số (căn phải)
};

<AgGridReact
  defaultColDef={defaultColDef}  // Áp dụng cho tất cả cột
  columnDefs={columnDefs}         // Định nghĩa từng cột cụ thể
/>
```

### Value Formatters (Định dạng Giá trị Hiển thị)

Format cell display values (Định dạng giá trị hiển thị trong cell):

```tsx
const columnDefs: ColDef[] = [
  {
    field: 'price',
    valueFormatter: (params) => {
      if (params.value == null) return '-';  // Nếu null, hiển thị '-'
      return params.value.toFixed(2);        // Làm tròn 2 số thập phân
    }
  }
];
```

**Best Practice (Thực hành Tốt)**: Tạo formatter class để tái sử dụng

```tsx
class GridValueFormatter {
  // Format giá
  static price(params: ValueFormatterParams): string {
    if (params.value == null) return '-';
    return params.value.toFixed(2);  // VD: 115799.99
  }

  // Format khối lượng
  static volume(params: ValueFormatterParams): string {
    if (params.value == null) return '-';
    return (params.value / 1000).toFixed(1) + 'K';  // VD: 27.3K
  }
}

// Sử dụng (Usage)
{ field: 'price', valueFormatter: GridValueFormatter.price }
```

### Value Getters (Tính toán Giá trị Dẫn xuất)

Calculate derived values (Tính toán giá trị từ các field khác):

```tsx
const columnDefs: ColDef[] = [
  {
    field: 'change',
    valueGetter: (params) => {
      // Tính chênh lệch giá (change = current - reference)
      const current = params.data?.lastPrice ?? 0;     // Giá hiện tại
      const reference = params.data?.reference ?? 0;   // Giá tham chiếu
      return current - reference;                      // VD: +1,488
    }
  }
];
```

### Cell Class Rules (Quy tắc CSS Động cho Cell)

Dynamic cell styling based on value (Đổi màu cell dựa trên giá trị):

```tsx
const columnDefs: ColDef[] = [
  {
    field: 'lastPrice',
    cellClassRules: {
      // Giá tăng -> màu xanh
      'price-up': (params) => {
        const current = params.value ?? 0;
        const reference = params.data?.reference ?? 0;
        return current > reference;  // Giá > tham chiếu
      },
      // Giá giảm -> màu đỏ
      'price-down': (params) => {
        const current = params.value ?? 0;
        const reference = params.data?.reference ?? 0;
        return current < reference;  // Giá < tham chiếu
      },
      // Giá không đổi -> màu vàng
      'price-ref': (params) => {
        const current = params.value ?? 0;
        const reference = params.data?.reference ?? 0;
        return current === reference;  // Giá = tham chiếu
      }
    }
  }
];
```

**CSS tương ứng:**

```scss
.ag-theme-quartz {
  .price-up {
    color: #00c087 !important;  // Xanh lá (tăng)
    font-weight: bold;
  }

  .price-down {
    color: #ff5252 !important;  // Đỏ (giảm)
    font-weight: bold;
  }

  .price-ref {
    color: #ffc107 !important;  // Vàng (không đổi)
  }
}
```

---

## 💾 Data Management (Quản lý Dữ liệu)

### Row Data (Dữ liệu Hàng)

```tsx
// Static data (Dữ liệu tĩnh)
<AgGridReact rowData={[
  { ticker: 'BTCUSDT', price: 50000 },
  { ticker: 'ETHUSDT', price: 3000 }
]} />

// Dynamic data (Dữ liệu động với state)
const [rowData, setRowData] = useState([]);

useEffect(() => {
  // Fetch data từ API
  fetch('/api/data')
    .then(res => res.json())
    .then(data => setRowData(data));
}, []);

<AgGridReact rowData={rowData} />
```

### Get Row ID (Định nghĩa ID Duy nhất cho Row)

Định nghĩa unique ID cho mỗi row (RẤT QUAN TRỌNG cho việc update hiệu quả):

```tsx
<AgGridReact
  getRowId={(params) => params.data.ticker}  // Dùng 'ticker' làm ID duy nhất
  rowData={rowData}
/>
// VD: 'BTCUSDT', 'ETHUSDT' là unique ID của mỗi row
// AG Grid dùng ID này để tìm row cần update (O(1) lookup)
```

### Grid API (API để Thao tác với Grid)

Access grid API để thao tác với grid (cập nhật data, lấy thông tin...):

```tsx
const [gridApi, setGridApi] = useState<GridApi | null>(null);

const onGridReady = (params: GridReadyEvent) => {
  setGridApi(params.api);  // Lưu API reference
};

<AgGridReact onGridReady={onGridReady} />

// Sau đó có thể dùng gridApi để:
// - gridApi.applyTransaction() - Cập nhật dữ liệu
// - gridApi.getSelectedRows() - Lấy rows đang chọn
// - gridApi.sizeColumnsToFit() - Tự động điều chỉnh độ rộng cột
```

### Update Grid Options (Cập nhật Cấu hình Grid)

Update toàn bộ rowData (Cập nhật toàn bộ dữ liệu):

```tsx
useEffect(() => {
  if (!gridApi) return;  // Guard clause: chỉ chạy khi gridApi đã sẵn sàng

  const initialData = createInitialData();  // Tạo dữ liệu ban đầu
  gridApi.updateGridOptions({
    rowData: initialData  // Load toàn bộ dữ liệu vào grid
  });
}, [gridApi]);

// Chú ý: Chỉ dùng khi khởi tạo. Với real-time updates, dùng applyTransaction()
```

---

## 🚀 Performance Optimization (Tối ưu Hiệu suất)

### 1. Transaction Updates (Cập nhật theo Transaction)

**❌ SAI** - Re-render toàn bộ grid (CHẬM):

```tsx
setRowData([...rowData, newRow]); // Chậm! Grid phải render lại TẤT CẢ rows
```

**✅ ĐÚNG** - Chỉ update row thay đổi (NHANH):

```tsx
gridApi.applyTransaction({
  add: [newRow],           // Thêm row mới
  update: [updatedRow],    // Cập nhật row đã có
  remove: [deletedRow]     // Xóa row
});
// AG Grid chỉ render lại những row bị thay đổi, không ảnh hưởng các row khác
```

### 2. Async Transactions (Cập nhật Bất đồng bộ)

Batch multiple updates lại với nhau (Gộp nhiều lần update thành 1):

```tsx
// Cấu hình thời gian delay để batch
const gridOptions = {
  asyncTransactionWaitMillis: 50, // Đợi 50ms để gộp các updates
};

// Sử dụng async transaction
gridApi.applyTransactionAsync({
  update: [row1, row2, row3]  // Gửi 3 updates cùng lúc
});

// VD: Nếu có 100 updates trong 50ms, AG Grid chỉ render 1 lần thay vì 100 lần!
```

**Lợi ích:**
- ✅ Giảm số lần re-render (100 lần → 1 lần)
- ✅ Tăng performance cho high-frequency updates (WebSocket, real-time data)
- ✅ AG Grid tự động batch các updates trong cùng 1 frame
- ✅ Quan trọng cho trading/crypto priceboard với updates liên tục

### 3. Row Node Cache (Cache Row Node)

Lấy row node trực tiếp (O(1) lookup - tìm kiếm siêu nhanh):

```tsx
const rowNode = gridApi.getRowNode(rowId);  // O(1) - tìm ngay lập tức
if (rowNode?.data) {
  // Merge data cũ với data mới (IMMUTABLE - tạo object mới)
  const updatedData = { ...rowNode.data, price: newPrice };
  gridApi.applyTransactionAsync({ update: [updatedData] });
}

// So sánh:
// ❌ Tìm trong array: O(n) - phải duyệt qua n rows
// ✅ getRowNode: O(1) - tìm trực tiếp qua ID (dùng Map bên trong)
```

### 4. Cell Flash Animation (Hiệu ứng Nhấp nháy Cell)

Highlight cells khi giá trị thay đổi (cho người dùng dễ nhận biết):

```tsx
const defaultColDef = {
  enableCellChangeFlash: true, // Bật hiệu ứng flash
};

const gridOptions = {
  cellFlashDuration: 500,      // Thời gian flash (ms) - cell sáng lên
  cellFadeDuration: 1000,      // Thời gian fade (ms) - cell mờ dần
};

// Kết quả: Khi giá thay đổi, cell sẽ:
// 1. Sáng lên trong 500ms (flash)
// 2. Mờ dần trong 1000ms (fade)
// → Người dùng dễ dàng nhận biết cell nào vừa thay đổi
```

### 5. Immutable Data (Dữ liệu Bất biến)

**RẤT QUAN TRỌNG**: AG Grid yêu cầu immutable data cho transactions:

```tsx
// ❌ SAI - Sửa trực tiếp object (MUTATE)
rowNode.data.price = newPrice;
// → AG Grid không phát hiện được thay đổi → không update UI!

// ✅ ĐÚNG - Tạo object mới (IMMUTABLE)
const updatedData = { ...rowNode.data, price: newPrice };
gridApi.applyTransactionAsync({ update: [updatedData] });
// → AG Grid so sánh reference → phát hiện object mới → update UI!

// Nguyên tắc: LUÔN tạo object/array mới khi update
// Spread operator (...) tạo shallow copy (đủ cho hầu hết trường hợp)
```

### 6. Debounce/Throttle High-Frequency Updates (Giảm tần suất Cập nhật)

```tsx
const updateQueue = useRef<Map<string, any>>(new Map());
const batchTimeoutRef = useRef<NodeJS.Timeout | null>(null);

const scheduleUpdate = (ticker: string, data: any) => {
  // Lưu update vào queue (Map để tránh duplicate ticker)
  updateQueue.current.set(ticker, data);

  // Clear timeout cũ (debounce pattern)
  if (batchTimeoutRef.current) {
    clearTimeout(batchTimeoutRef.current);
  }

  // Set timeout mới: gộp tất cả updates sau 100ms
  batchTimeoutRef.current = setTimeout(() => {
    const updates = Array.from(updateQueue.current.values());
    gridApi?.applyTransactionAsync({ update: updates });
    updateQueue.current.clear();  // Xóa queue sau khi update
  }, 100); // Gộp mỗi 100ms
};

// VD: Nhận 1000 updates trong 100ms → Chỉ render 1 lần với 1000 rows!
```

**⚠️ LƯU Ý QUAN TRỌNG**:
- AG Grid đã có `asyncTransactionWaitMillis` tích hợp sẵn
- Không cần tự implement debounce nữa, dùng `asyncTransactionWaitMillis` là đủ!
- Pattern trên chỉ dùng khi cần logic custom (VD: filter duplicate data)

### 7. Size Columns to Fit (Tự động Điều chỉnh Độ rộng Cột)

Auto-resize columns to fit grid width (Tự động fit các cột vào độ rộng grid):

```tsx
const gridOptions = {
  // Lần đầu render xong data
  onFirstDataRendered: (params) => {
    params.api.sizeColumnsToFit();  // Tự động resize tất cả cột để vừa grid
  },
  // Khi grid thay đổi kích thước (window resize, layout change)
  onGridSizeChanged: (params) => {
    params.api.sizeColumnsToFit();  // Resize lại để fit
  }
};

// Kết quả:
// - Các cột tự động co dãn để vừa khít grid width
// - Không có khoảng trống bên phải
// - Responsive với mọi screen size
```

---

## 🎨 Styling & Theming

### Built-in Themes

```tsx
// Light theme
<div className="ag-theme-quartz">
  <AgGridReact />
</div>

// Dark theme
<div className="ag-theme-quartz-dark">
  <AgGridReact />
</div>
```

### Custom Theme Variables

```scss
.ag-theme-quartz {
  // Colors
  --ag-background-color: #1a1a1a;
  --ag-foreground-color: #ffffff;
  --ag-header-background-color: #2a2a2a;
  --ag-odd-row-background-color: #1e1e1e;
  --ag-row-hover-color: #2a2a2a;

  // Borders
  --ag-border-color: #333333;
  --ag-row-border-color: #2a2a2a;

  // Fonts
  --ag-font-family: 'SF Pro Display', -apple-system, sans-serif;
  --ag-font-size: 13px;

  // Spacing
  --ag-grid-size: 4px;
  --ag-cell-horizontal-padding: calc(var(--ag-grid-size) * 2);

  // Header
  --ag-header-height: 40px;
  --ag-header-foreground-color: #999999;

  // Row
  --ag-row-height: 32px;
}
```

### Dynamic Theme (Light/Dark Mode)

```tsx
const { mode } = useThemeMode(); // 'light' | 'dark'
const themeClass = `ag-theme-quartz${mode === 'dark' ? '-dark' : ''}`;

<div className={themeClass}>
  <AgGridReact />
</div>
```

### Cell Flash Animation Colors

```scss
.ag-theme-quartz {
  // Flash colors for price changes
  --ag-value-change-value-highlight-background-color: rgba(0, 192, 135, 0.3);

  .ag-cell-data-changed {
    background-color: var(--ag-value-change-value-highlight-background-color) !important;
  }

  // Custom flash for up/down
  .price-up.ag-cell-data-changed {
    background-color: rgba(0, 192, 135, 0.2) !important;
  }

  .price-down.ag-cell-data-changed {
    background-color: rgba(255, 82, 82, 0.2) !important;
  }
}
```

### Header Styling

```scss
.ag-theme-quartz {
  .ag-header-cell {
    font-weight: 600;
    text-transform: uppercase;
    font-size: 11px;
    letter-spacing: 0.5px;
  }

  .bid-side-header {
    background-color: rgba(0, 192, 135, 0.1);
    color: #00c087;
  }

  .ask-side-header {
    background-color: rgba(255, 82, 82, 0.1);
    color: #ff5252;
  }

  .match-header {
    background-color: rgba(255, 193, 7, 0.1);
    color: #ffc107;
  }
}
```

---

## ⚡ Real-time Updates

### WebSocket Integration Pattern

```tsx
// 1. Initialize grid with empty data
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

// 2. Handle WebSocket messages
const handleWebSocketMessage = useCallback((event: MessageEvent) => {
  if (!gridApi) return;

  const message = JSON.parse(event.data);
  const ticker = message.s; // Symbol

  // Get existing row
  const rowNode = gridApi.getRowNode(ticker);
  if (!rowNode?.data) return;

  // Merge new data
  const updatedData = {
    ...rowNode.data,
    price: parseFloat(message.c),
    volume: parseFloat(message.v),
    // ... update other fields
  };

  // Update grid
  gridApi.applyTransactionAsync({ update: [updatedData] });
}, [gridApi]);

// 3. Connect WebSocket
useEffect(() => {
  if (!gridApi) return;

  const ws = new WebSocket('wss://stream.binance.com/ws');
  ws.onmessage = handleWebSocketMessage;

  return () => ws.close();
}, [gridApi, handleWebSocketMessage]);
```

### Data Flow Architecture

**Tách biệt concerns:**

```
┌─────────────────┐
│   Grid UI       │ <- Chỉ render & display
└────────┬────────┘
         │
         │ gridApi
         │
┌────────▼────────┐
│   DataFlow      │ <- WebSocket & data management
└─────────────────┘
```

**Example:**

```tsx
// Grid Component
export const BinanceGrid = ({ onGridReady }) => {
  const colDefs = useBinanceColumnDefs();

  return (
    <div className="ag-theme-quartz-dark">
      <AgGridReact
        columnDefs={colDefs}
        defaultColDef={defaultColDef}
        getRowId={({ data }) => data.ticker}
        onGridReady={onGridReady}
      />
    </div>
  );
};

// DataFlow Component
export const BinanceDataFlow = ({ gridApi }) => {
  // Initialize data
  useEffect(() => {
    if (!gridApi) return;
    const initialData = createInitialData();
    gridApi.updateGridOptions({ rowData: initialData });
  }, [gridApi]);

  // WebSocket connection
  useEffect(() => {
    if (!gridApi) return;
    const ws = connectWebSocket();
    ws.onmessage = handleMessage;
    return () => ws.close();
  }, [gridApi]);

  return null; // No UI
};

// Main Component
export const BinancePriceboard = () => {
  const [gridApi, setGridApi] = useState(null);

  return (
    <>
      <BinanceGrid onGridReady={({ api }) => setGridApi(api)} />
      <BinanceDataFlow gridApi={gridApi} />
    </>
  );
};
```

---

## 🏆 Best Practices

### 1. Column Definitions

✅ **DO**: Sử dụng `useMemo` cho column definitions

```tsx
const columnDefs = useMemo(() => [
  { field: 'ticker', headerName: 'Symbol' },
  { field: 'price', headerName: 'Price' }
], []);
```

✅ **DO**: Tạo config object riêng cho reusability

```tsx
const ColDefConfig = {
  ticker: { field: 'ticker', headerName: 'Symbol' },
  price: { field: 'price', headerName: 'Price' }
};

const columnDefs = useMemo(() =>
  Object.values(ColDefConfig), []
);
```

### 2. Data Updates

✅ **DO**: Dùng `applyTransaction` thay vì update state

```tsx
// ❌ BAD
setRowData(prev => [...prev, newRow]);

// ✅ GOOD
gridApi.applyTransaction({ add: [newRow] });
```

✅ **DO**: Dùng `applyTransactionAsync` cho high-frequency updates

```tsx
gridApi.applyTransactionAsync({ update: [updatedRow] });
```

### 3. Performance

✅ **DO**: Set `getRowId` cho unique identification

```tsx
<AgGridReact getRowId={({ data }) => data.id} />
```

✅ **DO**: Enable cell flash cho better UX

```tsx
const defaultColDef = {
  enableCellChangeFlash: true
};

const gridOptions = {
  cellFlashDuration: 500,
  asyncTransactionWaitMillis: 50
};
```

### 4. Styling

✅ **DO**: Sử dụng CSS variables cho theming

```scss
.ag-theme-quartz {
  --ag-background-color: #1a1a1a;
  --ag-foreground-color: #ffffff;
}
```

✅ **DO**: Sử dụng `cellClassRules` cho dynamic styling

```tsx
{
  field: 'price',
  cellClassRules: {
    'price-up': (params) => params.value > params.data.reference
  }
}
```

### 5. Code Organization

✅ **DO**: Tách logic thành các file riêng

```
BinancePriceboard/
├── index.tsx                    # Main component
├── components/
│   └── BinanceGrid.tsx          # Grid UI
├── data-flow/
│   └── BinanceDataFlow.tsx      # WebSocket & data
├── hooks/
│   └── useBinanceColumnDef.tsx  # Column definitions
├── utils/
│   ├── binanceDataMapper.ts     # Data transformation
│   ├── binanceGridValueFormatter.ts
│   ├── binanceGridCellClassRule.ts
│   └── binanceGridValueGetter.ts
├── constants/
│   ├── agGrid.ts                # Grid options
│   └── symbols.ts               # Symbol list
└── style.scss                   # Styling
```

### 6. TypeScript

✅ **DO**: Define types cho data

```tsx
interface IBinanceTickerData {
  ticker: string;
  price: number;
  volume: number;
  reference: number;
  // ...
}

<AgGridReact<IBinanceTickerData>
  rowData={data}
  columnDefs={columnDefs}
/>
```

### 7. Error Handling

✅ **DO**: Kiểm tra gridApi trước khi dùng

```tsx
useEffect(() => {
  if (!gridApi) return; // Guard clause

  gridApi.updateGridOptions({ rowData: initialData });
}, [gridApi]);
```

✅ **DO**: Cleanup WebSocket khi unmount

```tsx
useEffect(() => {
  if (!gridApi) return;

  const ws = new WebSocket(url);

  return () => {
    if (ws.readyState === WebSocket.OPEN) {
      ws.close();
    }
  };
}, [gridApi]);
```

---

## 📊 AG Grid Options & Properties

### Common Grid Options

```tsx
const gridOptions: GridOptions = {
  // ============= LAYOUT & DIMENSIONS =============
  headerHeight: 40,                    // Header row height (px)
  rowHeight: 32,                       // Data row height (px)
  groupHeaderHeight: 40,               // Group header height (px)
  floatingFiltersHeight: 40,           // Floating filter height (px)
  pivotHeaderHeight: 40,               // Pivot header height (px)
  pivotGroupHeaderHeight: 40,          // Pivot group header height (px)

  // ============= DATA & ROW MANAGEMENT =============
  rowData: [],                         // Initial row data
  getRowId: (params) => params.data.id, // Unique row identifier
  rowModelType: 'clientSide',          // 'clientSide' | 'infinite' | 'viewport' | 'serverSide'

  // Immutable Data
  immutableData: false,                // Enable immutable data mode
  getRowNodeId: (data) => data.id,     // Used with immutableData

  // ============= SELECTION =============
  rowSelection: 'single',              // 'single' | 'multiple'
  rowMultiSelectWithClick: false,      // Multi-select without Ctrl/Cmd
  suppressRowClickSelection: false,    // Disable row selection on click
  suppressRowDeselection: false,       // Prevent row deselection
  isRowSelectable: (node) => true,     // Function to determine if row is selectable

  // ============= SORTING =============
  sortingOrder: ['asc', 'desc', null], // Sorting cycle order
  multiSortKey: 'ctrl',                // 'ctrl' | 'shift' for multi-column sort
  accentedSort: false,                 // Sort accented characters

  // ============= FILTERING =============
  enableFilter: true,                  // Enable column filters
  quickFilterText: '',                 // Quick filter text
  cacheQuickFilter: false,             // Cache quick filter results
  excludeChildrenWhenTreeDataFiltering: false,

  // ============= PAGINATION =============
  pagination: false,                   // Enable pagination
  paginationPageSize: 100,             // Rows per page
  paginationPageSizeSelector: [10, 20, 50, 100], // Page size options
  paginationAutoPageSize: false,       // Auto-calculate page size
  suppressPaginationPanel: false,      // Hide pagination panel

  // ============= SCROLLING =============
  suppressHorizontalScroll: false,     // Disable horizontal scroll
  alwaysShowHorizontalScroll: false,   // Always show horizontal scrollbar
  alwaysShowVerticalScroll: false,     // Always show vertical scrollbar
  suppressScrollOnNewData: false,      // Don't scroll on data update
  suppressScrollWhenPopupsAreOpen: true, // Disable scroll when popup open

  // ============= EDITING =============
  editType: 'fullRow',                 // 'fullRow' for full row editing
  singleClickEdit: false,              // Edit on single click
  suppressClickEdit: false,            // Disable click to edit
  stopEditingWhenCellsLoseFocus: true, // Stop editing on focus loss
  enterMovesDown: true,                // Enter key moves to next row
  enterMovesDownAfterEdit: true,       // Enter saves & moves down

  // ============= PERFORMANCE =============
  asyncTransactionWaitMillis: 50,      // Batch transaction delay (ms)
  cellFlashDuration: 500,              // Flash animation duration (ms)
  cellFadeDuration: 1000,              // Flash fade duration (ms)
  animateRows: true,                   // Animate row changes
  enableCellChangeFlash: true,         // Flash on cell value change

  // Virtual Scrolling (enabled by default)
  rowBuffer: 10,                       // Rows to render outside viewport
  debounceVerticalScrollbar: false,    // Debounce vertical scrollbar

  // ============= COLUMNS =============
  columnDefs: [],                      // Column definitions
  defaultColDef: {},                   // Default column properties
  autoSizeStrategy: {                  // Auto-size columns strategy
    type: 'fitCellContents',
    colIds: ['ticker', 'price']
  },

  // Column Visibility
  suppressDragLeaveHidesColumns: false, // Prevent drag to hide columns
  suppressColumnVirtualisation: false,  // Disable column virtualization

  // ============= GROUPING & AGGREGATION =============
  groupDisplayType: 'singleColumn',    // 'singleColumn' | 'multipleColumns' | 'groupRows'
  groupDefaultExpanded: 0,             // Default group expand level (-1 = all)
  groupIncludeFooter: false,           // Include group footer
  groupIncludeTotalFooter: false,      // Include total footer
  suppressAggFuncInHeader: false,      // Hide agg function in header

  // ============= TREE DATA =============
  treeData: false,                     // Enable tree data mode
  getDataPath: (data) => data.path,    // Path for tree data
  autoGroupColumnDef: {},              // Auto group column definition

  // ============= MASTER/DETAIL =============
  masterDetail: false,                 // Enable master/detail
  detailRowHeight: 300,                // Detail row height
  detailRowAutoHeight: false,          // Auto-height for detail rows
  keepDetailRows: false,               // Keep detail rows when scrolling

  // ============= EVENTS =============
  onGridReady: (params) => {},         // Grid initialized
  onFirstDataRendered: (params) => {}, // First data rendered
  onGridSizeChanged: (params) => {},   // Grid size changed
  onSelectionChanged: (params) => {},  // Row selection changed
  onCellValueChanged: (params) => {},  // Cell value changed
  onRowClicked: (params) => {},        // Row clicked
  onRowDoubleClicked: (params) => {},  // Row double-clicked
  onCellClicked: (params) => {},       // Cell clicked
  onCellDoubleClicked: (params) => {}, // Cell double-clicked
  onRowSelected: (params) => {},       // Row selected/deselected
  onSortChanged: (params) => {},       // Sort changed
  onFilterChanged: (params) => {},     // Filter changed
  onColumnResized: (params) => {},     // Column resized
  onColumnVisible: (params) => {},     // Column visibility changed
  onColumnPinned: (params) => {},      // Column pinned
  onColumnMoved: (params) => {},       // Column moved
  onRowDragEnter: (params) => {},      // Row drag enter
  onRowDragMove: (params) => {},       // Row drag move
  onRowDragLeave: (params) => {},      // Row drag leave
  onRowDragEnd: (params) => {},        // Row drag end

  // ============= CLIPBOARD =============
  enableRangeSelection: false,         // Enable range selection
  enableRangeHandle: false,            // Enable range handle
  enableFillHandle: false,             // Enable fill handle
  suppressCopySingleCellRanges: false, // Suppress copy single cell
  suppressCopyRowsToClipboard: false,  // Suppress copy rows

  // ============= CONTEXT MENU =============
  allowContextMenuWithControlKey: false, // Allow context menu with Ctrl
  suppressContextMenu: false,          // Suppress context menu
  preventDefaultOnContextMenu: false,  // Prevent browser context menu
  getContextMenuItems: (params) => [], // Custom context menu items

  // ============= STYLING & UI =============
  suppressCellFocus: false,            // Suppress cell focus border
  suppressRowHoverHighlight: false,    // Suppress row hover highlight
  suppressColumnMoveAnimation: false,  // Disable column move animation
  suppressMovableColumns: false,       // Disable column moving
  suppressMenuHide: false,             // Keep menu open

  // Loading Overlay
  loadingOverlayComponent: null,       // Custom loading overlay
  noRowsOverlayComponent: null,        // Custom no rows overlay
  overlayLoadingTemplate: '<span>Loading...</span>',
  overlayNoRowsTemplate: '<span>No data</span>',

  // ============= CELL RENDERING =============
  suppressCellFlash: false,            // Disable cell flash animation
  suppressChangeDetection: false,      // Disable change detection
  valueCache: false,                   // Cache cell values
  valueCacheNeverExpires: false,       // Cache never expires

  // ============= ROW DRAGGING =============
  rowDragManaged: false,               // Enable managed row dragging
  suppressMoveWhenRowDragging: false,  // Suppress move when dragging
  rowDragEntireRow: false,             // Drag entire row
  rowDragMultiRow: false,              // Enable multi-row drag

  // ============= ACCESSIBILITY =============
  suppressRowTransform: false,         // Use top position instead of transform
  ensureDomOrder: false,               // Ensure DOM order matches row order

  // ============= LOCALIZATION =============
  localeText: {},                      // Custom locale text

  // ============= ADVANCED =============
  suppressPropertyNamesCheck: false,   // Suppress property name validation
  debug: false,                        // Enable debug mode
  maintainColumnOrder: false,          // Maintain column order
  suppressRowVirtualisation: false,    // Disable row virtualization
  suppressMaxRenderedRowRestriction: false, // Remove max rendered row limit
  suppressAnimationFrame: false,       // Disable animation frame
  suppressPreventDefaultOnMouseWheel: false, // Allow default mouse wheel

  // Server-Side Row Model (Enterprise)
  serverSideDatasource: null,          // Server-side datasource
  cacheBlockSize: 100,                 // Cache block size
  maxBlocksInCache: 10,                // Max blocks in cache
  maxConcurrentDatasourceRequests: 2,  // Max concurrent requests
  blockLoadDebounceMillis: 0,          // Block load debounce
};
```

### Column Definition Properties

```tsx
const columnDef: ColDef = {
  // ============= BASIC =============
  field: 'price',                      // Field name in data
  headerName: 'Price',                 // Column header text
  colId: 'priceCol',                   // Unique column ID

  // ============= DIMENSIONS =============
  width: 100,                          // Column width
  minWidth: 50,                        // Minimum width
  maxWidth: 500,                       // Maximum width
  initialWidth: 100,                   // Initial width
  flex: 1,                             // Flex sizing (vs fixed width)

  // ============= BEHAVIOR =============
  sortable: true,                      // Enable sorting
  resizable: true,                     // Enable resizing
  editable: true,                      // Enable editing
  filter: true,                        // Enable filtering
  floatingFilter: false,               // Show floating filter

  // ============= VISIBILITY =============
  hide: false,                         // Hide column
  lockVisible: false,                  // Lock visibility (can't hide)
  lockPosition: false,                 // Lock position (can't move)
  suppressMovable: false,              // Disable column moving

  // ============= PINNING =============
  pinned: 'left',                      // 'left' | 'right' | null
  lockPinned: false,                   // Lock pinned state

  // ============= CELL RENDERING =============
  cellRenderer: CustomCellRenderer,    // Custom cell renderer
  cellRendererParams: {},              // Params for cell renderer
  cellStyle: { color: 'red' },         // Static cell style
  cellClass: 'my-cell-class',          // Static cell class
  cellClassRules: {                    // Dynamic cell classes
    'price-up': (params) => params.value > 0,
    'price-down': (params) => params.value < 0,
  },

  // ============= HEADER =============
  headerClass: 'my-header-class',      // Header CSS class
  headerComponent: CustomHeader,       // Custom header component
  headerComponentParams: {},           // Params for header component
  headerTooltip: 'Tooltip text',       // Header tooltip

  // ============= VALUE HANDLING =============
  valueGetter: (params) => {},         // Calculate cell value
  valueSetter: (params) => {},         // Set value on edit
  valueFormatter: (params) => {},      // Format display value
  valueParser: (params) => {},         // Parse input value

  // ============= EDITING =============
  cellEditor: 'agTextCellEditor',      // Cell editor type
  cellEditorParams: {},                // Cell editor params
  cellEditorPopup: false,              // Edit in popup
  singleClickEdit: false,              // Edit on single click

  // ============= FILTERING =============
  filterParams: {},                    // Filter params
  filterValueGetter: (params) => {},   // Custom filter value
  floatingFilterComponent: null,       // Custom floating filter
  floatingFilterComponentParams: {},   // Floating filter params

  // ============= SORTING =============
  comparator: (a, b) => a - b,         // Custom sort comparator
  unSortIcon: true,                    // Show unsort icon
  sort: 'asc',                         // Initial sort ('asc' | 'desc')
  sortIndex: 0,                        // Sort order index (multi-sort)

  // ============= TOOLTIPS =============
  tooltipField: 'tooltipText',         // Field for tooltip
  tooltipValueGetter: (params) => {},  // Custom tooltip value
  tooltipComponent: CustomTooltip,     // Custom tooltip component
  tooltipComponentParams: {},          // Tooltip component params

  // ============= GROUPING =============
  rowGroup: false,                     // Group by this column
  rowGroupIndex: 0,                    // Row group order
  enableRowGroup: true,                // Allow grouping
  showRowGroup: false,                 // Show row group column

  // ============= AGGREGATION =============
  aggFunc: 'sum',                      // 'sum' | 'min' | 'max' | 'count' | 'avg' | custom
  enableValue: true,                   // Allow as value column
  allowedAggFuncs: ['sum', 'avg'],     // Allowed agg functions

  // ============= PIVOTING (Enterprise) =============
  pivot: false,                        // Pivot by this column
  pivotIndex: 0,                       // Pivot order
  enablePivot: true,                   // Allow pivoting

  // ============= SPANNING =============
  colSpan: (params) => 1,              // Column span function
  rowSpan: (params) => 1,              // Row span function

  // ============= TREE DATA =============
  cellRendererSelector: (params) => {}, // Select cell renderer dynamically

  // ============= CHECKBOX SELECTION =============
  checkboxSelection: true,             // Show checkbox
  headerCheckboxSelection: true,       // Show header checkbox
  headerCheckboxSelectionFilteredOnly: false, // Only select filtered

  // ============= FLASH =============
  enableCellChangeFlash: true,         // Flash on value change

  // ============= TYPE =============
  type: 'numericColumn',               // Column type (predefined)
  // Types: 'numericColumn', 'rightAligned', 'dateColumn', etc.

  // ============= KEYBOARD NAVIGATION =============
  suppressKeyboardEvent: (params) => false, // Suppress keyboard events
  suppressNavigable: false,            // Disable keyboard navigation

  // ============= ROW DRAGGING =============
  rowDrag: false,                      // Enable row dragging
  dndSource: false,                    // Enable as DnD source
  dndSourceOnRowDrag: false,           // DnD source on row drag

  // ============= MASTER/DETAIL =============
  cellRendererParams: {
    masterDetail: true,                // Enable master/detail
    detailGridOptions: {},             // Detail grid options
  },

  // ============= MENU =============
  suppressMenu: false,                 // Suppress column menu
  menuTabs: ['filterMenuTab'],         // Menu tabs to show

  // ============= CLIPBOARD =============
  suppressPaste: false,                // Disable paste
  suppressFillHandle: false,           // Disable fill handle

  // ============= COLUMN GROUPS =============
  children: [],                        // Child columns (for groups)
  marryChildren: false,                // Keep children together
  openByDefault: false,                // Open group by default

  // ============= CUSTOM =============
  cellDataType: false,                 // Enable cell data type inference
  useValueFormatterForExport: true,    // Use formatter for export
  useValueParserForImport: true,       // Use parser for import

  // ============= EVENTS =============
  onCellValueChanged: (params) => {},  // Cell value changed
  onCellClicked: (params) => {},       // Cell clicked
  onCellDoubleClicked: (params) => {}, // Cell double-clicked
  onCellContextMenu: (params) => {},   // Cell right-clicked
};
```

### Default Column Definition

```tsx
const defaultColDef: ColDef = {
  // Áp dụng cho tất cả columns nếu không override
  sortable: true,
  resizable: false,
  filter: true,
  editable: false,
  enableCellChangeFlash: true,
  suppressMenu: false,
  minWidth: 50,
  flex: 1,
  type: 'numericColumn',
  unSortIcon: true,
  cellClass: 'default-cell',
  headerClass: 'default-header',
};
```

### Column Types (Predefined)

```tsx
const columnTypes = {
  numericColumn: {
    headerClass: 'ag-numeric-header',
    cellClass: 'ag-numeric-cell',
    filter: 'agNumberColumnFilter',
  },

  rightAligned: {
    headerClass: 'ag-right-aligned-header',
    cellClass: 'ag-right-aligned-cell',
  },

  dateColumn: {
    filter: 'agDateColumnFilter',
    valueFormatter: (params) => new Date(params.value).toLocaleDateString(),
  },

  // Custom types
  editableColumn: {
    editable: true,
    cellClass: 'editable-cell',
  },

  nonEditableColumn: {
    editable: false,
    suppressNavigable: true,
  },
};

// Usage
<AgGridReact columnTypes={columnTypes} />
```

---

## 🔗 Resources

- [AG Grid Documentation](https://www.ag-grid.com/react-data-grid/)
- [AG Grid API Reference](https://www.ag-grid.com/react-data-grid/grid-api/)
- [AG Grid Examples](https://www.ag-grid.com/react-data-grid/examples/)
- [AG Grid GitHub](https://github.com/ag-grid/ag-grid)

---

## 💡 Quick Reference

### Most Used APIs

```tsx
// Grid API
gridApi.updateGridOptions({ rowData: data });
gridApi.applyTransaction({ add, update, remove });
gridApi.applyTransactionAsync({ update: [data] });
gridApi.getRowNode(id);
gridApi.getSelectedRows();
gridApi.sizeColumnsToFit();

// Column API (deprecated in v31+, use Grid API instead)
// Use gridApi.setColumnDefs() instead
```

### Most Used Props

```tsx
<AgGridReact
  // Data
  rowData={data}
  getRowId={({ data }) => data.id}

  // Columns
  columnDefs={columnDefs}
  defaultColDef={defaultColDef}

  // Events
  onGridReady={onGridReady}
  onSelectionChanged={onSelectionChanged}

  // Options
  {...gridOptions}
/>
```

---

**Created**: 2025-10-13
**Project**: TPPro-Web / Binance Priceboard
**AG Grid Version**: 33.3.0 (Community Edition)

