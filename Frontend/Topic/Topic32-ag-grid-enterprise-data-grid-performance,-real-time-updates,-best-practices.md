# 📊 Topic 32: AG Grid - Enterprise Data Grid Performance, Real-time Updates & Best Practices

## 1. ⭐ Senior/Staff Summary

AG Grid là data grid mạnh cho dashboard doanh nghiệp: nhiều cột, nhiều hàng, sort/filter/grouping, editing, export, real-time updates và server-side data. Điểm mạnh nhất của AG Grid là nó không render toàn bộ bảng như HTML table thường, mà dùng **row/column virtualization**, **row identity**, **transaction updates** và nhiều row model khác nhau.

Khi dùng AG Grid trong production, cần nhớ 4 ý:

- ✅ **Dùng `getRowId`** để AG Grid nhận diện row ổn định khi update.
- ✅ **Dùng transaction API** (`applyTransaction`, `applyTransactionAsync`) cho update tăng dần, không set lại toàn bộ `rowData`.
- ✅ **Memoize `columnDefs`, `defaultColDef`, callbacks** trong React để tránh grid bị reset/re-render không cần thiết.
- ✅ **Chọn đúng row model**: client-side cho data vừa, server-side/infinite cho data lớn hoặc query nặng.

> 💡 Mental model: AG Grid nhanh khi bạn cho nó biết **row nào thay đổi**, thay vì bắt nó đoán lại toàn bộ dataset.

## 2. 🧠 Key Mental Model

### 2.1. Ba lớp hiệu năng chính

```text
Rendering
  → virtual scrolling: chỉ render rows/cells đang thấy

Data identity
  → getRowId: mỗi row có ID ổn định

Update strategy
  → transaction: add/update/remove đúng phần thay đổi
```

### 2.2. `rowData` vs Transaction API

| Cách update | Khi dùng | Ý nghĩa |
|---|---|---|
| `rowData={data}` | Load ban đầu, data nhỏ/vừa, replace toàn dataset | React truyền lại data cho grid |
| `api.applyTransaction({ update })` | Update ít row ngay lập tức | Cập nhật tăng dần |
| `api.applyTransactionAsync({ update })` | Real-time/high-frequency updates | Batch nhiều update để giảm render |
| Server-Side Row Model | Data rất lớn, sort/filter/group trên server | Grid request block data từ server |

### 2.3. AG Grid phù hợp khi nào?

AG Grid hợp với:

- admin dashboard nhiều cột
- trading/order book/market data
- inventory/logs/analytics table
- bảng cần grouping, pivoting, aggregation
- enterprise app cần export, filtering, editing mạnh

Không nhất thiết dùng AG Grid khi:

- chỉ cần table đơn giản vài trăm rows
- UI custom hoàn toàn và ít feature grid
- bundle budget rất chặt
- team chưa cần Enterprise features

## 3. 📚 Main Concepts

### 3.1. Community vs Enterprise

| Bản | Có gì | Khi chọn |
|---|---|---|
| Community | sorting, filtering, editing, CSV export, custom renderers, themes | Data grid phổ thông |
| Enterprise | row grouping, aggregation, pivot, Excel export, server-side row model, master/detail, range selection | Enterprise dashboard/data-heavy app |

> ⚠️ Kiểm tra license trước khi dùng Enterprise modules trong sản phẩm thật.

### 3.2. `getRowId` - key của performance update

`getRowId` giúp AG Grid map row theo ID ổn định. Nếu không có ID, grid phải dựa vào object reference hoặc cách so sánh kém rõ ràng hơn.

```tsx
<AgGridReact
  rowData={rows}
  getRowId={(params) => params.data.id}
/>
```

Yêu cầu:

- ID unique.
- ID không đổi trong vòng đời row.
- Không dùng index nếu row có sort/filter/remove/reorder.

### 3.3. Transaction updates

Transaction nói rõ row nào thêm, sửa, xóa.

```ts
gridApi.applyTransaction({
  add: [{ id: '4', name: 'New row' }],
  update: [{ id: '2', name: 'Updated row' }],
  remove: [{ id: '3' }],
});
```

Use case:

- update giá realtime
- edit cell rồi sync lại
- websocket stream
- add/remove row theo event

### 3.4. `applyTransactionAsync` cho high-frequency updates

Khi update liên tục, dùng async transaction để AG Grid batch nhiều update.

```ts
gridApi.applyTransactionAsync({
  update: priceUpdates,
});
```

Có thể chỉnh batch window:

```tsx
<AgGridReact asyncTransactionWaitMillis={50} />
```

> ✅ Thay vì update 500 lần/giây, batch lại theo khung thời gian ngắn để UI mượt hơn và CPU nhẹ hơn.

### 3.5. Virtual scrolling

AG Grid chỉ render phần đang thấy trong viewport. Vì vậy 100k rows không đồng nghĩa 100k DOM nodes.

Điều làm virtual scrolling chậm:

- cell renderer quá nặng
- row height dynamic phức tạp
- quá nhiều pinned columns
- quá nhiều custom components trong mỗi cell
- render object/function mới liên tục từ React

### 3.6. Column definitions

`columnDefs` là config quan trọng. Trong React, nếu tạo array mới mỗi render, AG Grid có thể phải xử lý lại column state.

```tsx
const columnDefs = useMemo<ColDef<Order>[]>(() => [
  { field: 'symbol', pinned: 'left' },
  { field: 'price', type: 'rightAligned', valueFormatter: currencyFormatter },
  { field: 'quantity', type: 'rightAligned' },
], []);

const defaultColDef = useMemo<ColDef>(() => ({
  sortable: true,
  filter: true,
  resizable: true,
}), []);
```

### 3.7. Cell renderers

Cell renderer nên nhẹ. Nếu chỉ format text, ưu tiên `valueFormatter`. Chỉ dùng React cell renderer khi cần UI thật sự như button, icon, badge, action menu.

```tsx
const columnDefs = useMemo<ColDef<Order>[]>(() => [
  {
    field: 'status',
    cellRenderer: StatusBadge,
  },
], []);
```

Rule đơn giản:

- Format text/number/date → `valueFormatter`.
- Tính value từ data → `valueGetter`.
- UI tương tác → `cellRenderer`.
- Edit custom → `cellEditor`.

### 3.8. Server-Side Row Model

Server-Side Row Model phù hợp khi dataset quá lớn để đưa hết vào browser hoặc sort/filter/grouping phải chạy trên backend.

```tsx
<AgGridReact
  rowModelType="serverSide"
  serverSideDatasource={datasource}
/>
```

Server cần hiểu request từ grid:

- range/block cần load
- sort model
- filter model
- grouping/pivot request

### 3.9. Real-time updates

Luồng realtime tốt:

```text
WebSocket message
  ↓
parse + validate event
  ↓
group updates theo row ID
  ↓
applyTransactionAsync({ update })
  ↓
AG Grid update đúng cells
```

Không nên:

- `setRowData` lại toàn bộ mỗi message
- update từng row bằng loop gọi transaction nhiều lần
- mutate object cũ mà không rõ change strategy

### 3.10. So sánh nhanh

| Library | Điểm mạnh | Tradeoff |
|---|---|---|
| AG Grid | Feature enterprise, realtime, performance tốt cho grid lớn | API nhiều, bundle/license cần cân nhắc |
| MUI Data Grid | Hợp hệ MUI, DX quen thuộc | Feature nâng cao thường cần paid tier |
| TanStack Table | Headless, nhẹ, cực linh hoạt | Tự build UI/virtualization/editing nhiều hơn |
| react-data-grid | Nhẹ hơn, đủ cho nhiều grid | Ecosystem/enterprise feature ít hơn AG Grid |

## 4. 💻 Practical TypeScript/JavaScript Examples

### 4.1. Basic React setup

```tsx
import { useCallback, useMemo } from 'react';
import { AgGridReact } from 'ag-grid-react';
import type { ColDef, GetRowIdParams } from 'ag-grid-community';

type Order = {
  id: string;
  symbol: string;
  price: number;
  quantity: number;
};

export function OrdersGrid({ rows }: { rows: Order[] }) {
  const columnDefs = useMemo<ColDef<Order>[]>(() => [
    { field: 'symbol' },
    { field: 'price', type: 'rightAligned' },
    { field: 'quantity', type: 'rightAligned' },
  ], []);

  const defaultColDef = useMemo<ColDef>(() => ({
    sortable: true,
    filter: true,
    resizable: true,
  }), []);

  const getRowId = useCallback((params: GetRowIdParams<Order>) => {
    return params.data.id;
  }, []);

  return (
    <AgGridReact<Order>
      rowData={rows}
      columnDefs={columnDefs}
      defaultColDef={defaultColDef}
      getRowId={getRowId}
    />
  );
}
```

### 4.2. WebSocket realtime updates

```tsx
import { useEffect, useMemo, useRef } from 'react';
import { AgGridReact } from 'ag-grid-react';
import type { GridApi, GridReadyEvent } from 'ag-grid-community';

type PriceRow = {
  id: string;
  symbol: string;
  price: number;
};

export function PricesGrid({ initialRows }: { initialRows: PriceRow[] }) {
  const apiRef = useRef<GridApi<PriceRow> | null>(null);

  useEffect(() => {
    const ws = new WebSocket('wss://example.com/prices');

    ws.onmessage = (event) => {
      const updates = JSON.parse(event.data) as PriceRow[];
      apiRef.current?.applyTransactionAsync({ update: updates });
    };

    return () => ws.close();
  }, []);

  const columnDefs = useMemo(() => [
    { field: 'symbol' },
    { field: 'price', enableCellChangeFlash: true },
  ], []);

  return (
    <AgGridReact<PriceRow>
      rowData={initialRows}
      columnDefs={columnDefs}
      getRowId={(params) => params.data.id}
      asyncTransactionWaitMillis={50}
      onGridReady={(event: GridReadyEvent<PriceRow>) => {
        apiRef.current = event.api;
      }}
    />
  );
}
```

### 4.3. Server-side datasource

```ts
import type { IServerSideDatasource } from 'ag-grid-community';

export const datasource: IServerSideDatasource = {
  async getRows(params) {
    try {
      const response = await fetch('/api/orders/search', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(params.request),
      });

      const result: { rows: Order[]; total: number } = await response.json();

      params.success({
        rowData: result.rows,
        rowCount: result.total,
      });
    } catch {
      params.fail();
    }
  },
};
```

### 4.4. Before/after: tránh tạo config mới mỗi render

```tsx
// ❌ Mỗi render tạo array/object mới.
<AgGridReact
  columnDefs={[{ field: 'name' }, { field: 'price' }]}
  defaultColDef={{ sortable: true, filter: true }}
/>
```

```tsx
// ✅ Stable references.
const columnDefs = useMemo(() => [{ field: 'name' }, { field: 'price' }], []);
const defaultColDef = useMemo(() => ({ sortable: true, filter: true }), []);

<AgGridReact columnDefs={columnDefs} defaultColDef={defaultColDef} />;
```

## 5. 🏗️ Production Notes / React Implications

### 5.1. React rendering

Trong React, AG Grid nhạy với reference của props:

- `columnDefs`
- `defaultColDef`
- `rowSelection`
- callbacks
- framework components/cell renderers

Dùng `useMemo`/`useCallback` cho config ổn định. Không cần memoize mọi thứ mù quáng, nhưng với grid lớn thì config stability rất quan trọng.

### 5.2. Performance

Checklist performance ngắn:

- có `getRowId`
- update bằng transaction
- batch realtime bằng `applyTransactionAsync`
- cell renderer nhẹ
- tránh auto-size liên tục trên dataset lớn
- dùng server-side row model khi data quá lớn
- đo bằng React Profiler/Performance tab, không đo bằng cảm giác

### 5.3. Security

Grid chỉ là UI. Backend vẫn phải kiểm soát:

- permission theo row/action
- filter/sort request từ client không được tin tuyệt đối
- export data phải kiểm tra quyền
- HTML trong cell phải escape/sanitize nếu render rich content
- tránh lộ PII qua CSV/Excel export

### 5.4. Accessibility

AG Grid có hỗ trợ keyboard navigation và ARIA, nhưng app vẫn cần:

- label/title rõ cho grid
- cell action có accessible name
- focus không bị mất khi update realtime
- contrast/theme đạt chuẩn
- không dùng màu duy nhất để báo trạng thái

### 5.5. Observability

Với grid production, nên log/track:

- thời gian load data
- số rows/columns render
- update rate từ WebSocket
- transaction batch size
- lỗi datasource
- export failures
- slow cell renderer

## 6. ⚠️ Common Pitfalls

### 6.1. Không dùng `getRowId`

Realtime update sẽ khó tối ưu vì grid không biết row nào tương ứng với update nào.

### 6.2. Dùng `setRowData` cho realtime

`setRowData`/replace toàn data phù hợp load lại dataset, không phù hợp update từng row liên tục.

### 6.3. Gọi transaction trong loop

```ts
// ❌ 100 updates = 100 transactions.
updates.forEach((row) => api.applyTransaction({ update: [row] }));

// ✅ 100 updates = 1 transaction.
api.applyTransaction({ update: updates });
```

### 6.4. Cell renderer quá nặng

Nếu mỗi cell render chart/button phức tạp, virtual scrolling vẫn có thể lag. Dùng renderer nhẹ và chỉ render UI tương tác khi cần.

### 6.5. Tạo lại `columnDefs`

Tạo `columnDefs` inline làm grid mất column state hoặc xử lý lại config không cần thiết.

### 6.6. Dùng client-side model cho data quá lớn

Nếu dữ liệu hàng triệu rows hoặc filter/sort nặng, chuyển sang server-side row model.

### 6.7. Không cleanup WebSocket

Không đóng WebSocket khi unmount sẽ gây memory leak và duplicate updates.

### 6.8. Tin dữ liệu export ở client

Export cần kiểm tra permission. Không phải user thấy grid là được quyền export toàn bộ dataset.

## 7. ✅ Decision Guide / Checklist

### 7.1. Chọn row model

| Nhu cầu | Chọn |
|---|---|
| Data nhỏ/vừa, load một lần | Client-Side Row Model |
| Scroll data theo block từ server | Infinite Row Model |
| Sort/filter/group/pivot trên server | Server-Side Row Model |
| Tree/group data phức tạp | Server-Side Row Model hoặc Tree Data |
| Realtime update nhiều row đã có sẵn | Client-Side + Transaction API |

### 7.2. Checklist trước khi merge grid lớn

- [ ] Có `getRowId`.
- [ ] `columnDefs` và `defaultColDef` ổn định bằng `useMemo`.
- [ ] Realtime dùng `applyTransactionAsync`.
- [ ] Không replace toàn `rowData` cho update nhỏ.
- [ ] Cell renderer đã được kiểm tra performance.
- [ ] Server-side datasource xử lý lỗi bằng `params.fail()`.
- [ ] WebSocket/event source có cleanup.
- [ ] Export có kiểm tra quyền.
- [ ] Keyboard navigation và focus đã test.
- [ ] Có monitoring cho load time/update rate.

### 7.3. Khi nào không chọn AG Grid?

- Table đơn giản, ít rows, không cần feature enterprise.
- UI cần custom hoàn toàn và không giống grid truyền thống.
- Bundle/license là constraint quan trọng.
- Team chỉ cần headless table để tự build UI.

Khi đó cân nhắc TanStack Table, MUI Data Grid hoặc table custom.

## 8. 🎤 Short Interview Answer

Theo em, AG Grid phù hợp khi app cần data grid thật sự nặng: nhiều rows/columns, filtering, sorting, grouping, editing, export hoặc realtime updates. Điểm quan trọng nhất để performance tốt là phải có `getRowId` để grid nhận diện row ổn định, dùng transaction API cho update tăng dần, và memoize các config như `columnDefs` trong React.

Với realtime data, em không set lại toàn bộ `rowData` mỗi lần WebSocket gửi message. Em sẽ batch updates và gọi `applyTransactionAsync`, đồng thời cleanup WebSocket khi unmount. Nếu dataset quá lớn hoặc sort/filter/grouping cần chạy trên backend, em sẽ dùng Server-Side Row Model thay vì đẩy toàn bộ data xuống browser.

Trong production, em còn kiểm tra license Enterprise, quyền export data, accessibility, cell renderer performance và monitoring cho load time/update rate. AG Grid mạnh, nhưng chỉ đáng dùng khi bài toán thật sự là enterprise data grid.

## 9. 🧾 Ghi nhớ nhanh

- **`getRowId`**: bắt buộc cho update ổn định.
- **Transaction API**: update add/remove/update đúng phần thay đổi.
- **`applyTransactionAsync`**: batch realtime updates.
- **Virtual scrolling**: chỉ render phần đang thấy.
- **`useMemo`**: giữ `columnDefs/defaultColDef` ổn định.
- **Cell renderer**: càng nhẹ càng tốt.
- **Server-Side Row Model**: dùng khi data lớn/query nặng.
- **Client validation không đủ**: export/filter/action vẫn phải kiểm tra quyền ở server.
- **Không dùng AG Grid cho table quá đơn giản** nếu bundle/license không đáng.

## 10. 📖 Giải thích các thuật ngữ trong topic

| Thuật ngữ | Giải thích ngắn |
|---|---|
| AG Grid | Data grid library cho web app, có bản Community và Enterprise |
| Data grid | Bảng dữ liệu có sort/filter/edit/export/virtualization |
| Virtual scrolling | Chỉ render rows/cells trong vùng nhìn thấy |
| `getRowId` | Hàm trả ID ổn định cho mỗi row |
| Row identity | Cách grid nhận diện row qua các lần update |
| Transaction API | API add/update/remove rows tăng dần |
| `applyTransaction` | Áp transaction ngay |
| `applyTransactionAsync` | Batch transaction để xử lý update tần suất cao |
| `columnDefs` | Cấu hình cột của grid |
| `defaultColDef` | Cấu hình mặc định áp cho các cột |
| Cell renderer | Component/function render nội dung cell |
| `valueFormatter` | Format giá trị hiển thị mà không đổi data gốc |
| `valueGetter` | Tính value hiển thị từ row data |
| Server-Side Row Model | Row model tải/query data theo block từ server |
| Datasource | Object cung cấp data cho server-side/infinite row model |
| Cell flash | Hiệu ứng báo cell vừa thay đổi |
| Pinned column | Cột cố định trái/phải khi scroll ngang |
| Row grouping | Nhóm rows theo field |
| Pivoting | Xoay/biến đổi dữ liệu như pivot table |
| Hydration | Đồng bộ UI client với HTML/server state ban đầu |

## 11. 📚 Nguồn chính thức đã đối chiếu

- React Best Practices: <https://www.ag-grid.com/react-data-grid/react-hooks/>
- High Frequency Updates: <https://www.ag-grid.com/javascript-data-grid/data-update-high-frequency/>
- Server-Side Row Model: <https://www.ag-grid.com/javascript-data-grid/server-side-model/>
- SSRM Datasource: <https://www.ag-grid.com/javascript-data-grid/server-side-model-datasource/>
