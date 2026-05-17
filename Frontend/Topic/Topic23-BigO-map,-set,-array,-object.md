# 📈 Topic 23: Big O với `Map`, `Set`, `Array`, `Object`

## 1. ⭐ Senior/Staff Summary

`Big O` mô tả chi phí của thuật toán khi dữ liệu tăng lên. Trong frontend, nó quyết định cách ta xử lý search, filter, dedupe, table lớn, state normalization, cache, permission checks và render performance.

Ý chính cần nói trong phỏng vấn:

- `Map`/`Set`: `get`, `set`, `has`, `delete` là **O(1) average** nhờ hash table, nhưng có worst case khi collision nhiều.
- `Object`: property access thường **O(1) average**, hợp cho plain data/JSON/config, nhưng key chỉ là `string`/`symbol` và có rủi ro prototype.
- `Array`: truy cập theo index là **O(1)**, nhưng search bằng `find`, `includes`, `indexOf` là **O(n)**; insert/delete đầu hoặc giữa thường **O(n)**.
- Performance tốt không chỉ là chọn cấu trúc nhanh nhất, mà là chọn đúng theo **access pattern**, dữ liệu lớn cỡ nào, có qua JSON/API boundary không, và React state có update immutable không.

### 🔑 Performance Comparison

| Operation | `Array` | `Object` | `Map` | `Set` |
|---|---:|---:|---:|---:|
| Access by index/key | `arr[i]`: O(1) | O(1) average | O(1) average | N/A |
| Search by value | O(n) | O(n) | O(n) | membership `.has()`: O(1) average |
| Insert | cuối: O(1) amortized, đầu/giữa: O(n) | O(1) average | O(1) average | O(1) average |
| Delete | cuối: O(1), đầu/giữa: O(n) | O(1) average, có thể deopt | O(1) average | O(1) average |
| Iterate | O(n) | O(n) | O(n) | O(n) |
| Size | `.length`: O(1) | `Object.keys(obj).length`: O(n) | `.size`: O(1) | `.size`: O(1) |

⚠️ Câu senior nên dùng: `Map`/`Set` là **O(1) trung bình**, không phải “luôn O(1)”. Collision, resize, memory overhead và engine implementation vẫn ảnh hưởng trong hot path.

## 2. 🧠 Key Mental Model or Key Points

- `Array` tối ưu cho **ordered list** và render UI bằng `.map()`. Nếu lookup theo `id` lặp lại nhiều lần, scan array sẽ tốn O(n) mỗi lần.
- `Map` tối ưu cho **dynamic key-value lookup**: cache, index theo id, composite key, key là object/function/Date.
- `Set` tối ưu cho **membership và uniqueness**: selected IDs, visited IDs, dedupe primitive values, permission checks.
- `Object` tối ưu cho **plain record**: API response, DTO, config, component props, JSON serialization.
- Big O nói về tốc độ tăng trưởng, không thay thế profiling. Với data nhỏ, readability thường quan trọng hơn micro-optimization.
- Trong React, `Map`, `Set`, `Array`, `Object` đều phải update immutable nếu nằm trong state, vì React dựa vào `reference equality`.

## 3. 📚 Main Concepts

### 3.1. Big O là gì?

`Big O` mô tả xu hướng tăng chi phí khi input lớn lên.

- `O(1)`: gần như không đổi theo số lượng phần tử.
- `O(n)`: tăng tuyến tính theo số phần tử.
- `O(n log n)`: thường gặp ở sort hiệu quả.
- `O(n²)`: thường xuất hiện khi loop lồng nhau hoặc search tuyến tính bên trong loop.

Ví dụ dễ thấy:

```ts
const users = [{ id: 1 }, { id: 2 }, { id: 3 }];

users[0]; // O(1)
users.find((user) => user.id === 3); // O(n)
```

### 3.2. `Array`: tốt cho thứ tự, không tốt cho lookup lặp lại

`Array` phù hợp nhất cho list UI vì giữ thứ tự và có API tiện như `.map()`, `.filter()`, `.reduce()`.

| Operation | Big O | Ghi chú |
|---|---:|---|
| `arr[i]` | O(1) | Truy cập index trực tiếp |
| `push`, `pop` | O(1) amortized | Có lúc resize nội bộ, nhưng trung bình vẫn O(1) |
| `find`, `includes`, `indexOf` | O(n) | Duyệt tuyến tính |
| `shift`, `unshift` | O(n) | Phải dời phần tử |
| `splice` đầu/giữa | O(n) | Phải dời phần sau điểm insert/delete |
| `sort` | thường O(n log n) | Tùy engine, comparator và dữ liệu |

⚠️ `arr[1000] = value` trên array nhỏ có thể tạo sparse array/hole. Engine có thể chuyển representation từ packed sang holey/dictionary mode, làm nhiều thao tác chậm hơn.

### 3.3. `Map`: dynamic dictionary rõ nghĩa hơn `Object`

`Map` lưu key-value, key có thể là primitive hoặc object reference.

```ts
type User = { id: number; name: string };

const usersById = new Map<number, User>();

usersById.set(42, { id: 42, name: "Ada" }); // O(1) average
usersById.get(42); // O(1) average
usersById.has(42); // O(1) average
usersById.delete(42); // O(1) average
```

Dùng `Map` khi:

- Key không chỉ là `string`/`symbol`.
- Thêm/xóa thường xuyên.
- Cần `.size` O(1).
- Cần giữ insertion order khi iterate.
- Làm cache, lookup table, normalized index nội bộ.

⚠️ `Map` không JSON-serializable trực tiếp:

```ts
const serialized = JSON.stringify([...usersById]);
const restored = new Map<number, User>(JSON.parse(serialized));
```

Nếu dùng `Object.fromEntries(map)`, key number sẽ thành string. Chỉ làm vậy khi boundary chấp nhận key string.

### 3.4. `Set`: membership và uniqueness

`Set` lưu các giá trị unique và rất hợp cho membership check.

```ts
const selectedIds = new Set<number>([1, 2, 3]);

selectedIds.has(2); // O(1) average
selectedIds.add(4); // O(1) average
selectedIds.delete(1); // O(1) average
```

Use cases thực tế:

- Selected row IDs trong table.
- Visited IDs khi traverse tree/graph.
- Unique tags/search results.
- Permission/feature flag checks.
- Dedupe primitive values.

⚠️ `Set` so sánh object bằng reference, không deep compare:

```ts
const set = new Set([{ id: 1 }]);

set.has({ id: 1 }); // false
```

Nếu cần unique theo `id`, dùng `Set<number>` hoặc `Map<number, Item>`.

### 3.5. `Object`: plain data, JSON và fixed shape

`Object` phù hợp cho API response, config, component props, DTO và dictionary có key string.

```ts
type User = { id: number; name: string };

const byId: Record<string, User> = {
  "42": { id: 42, name: "Ada" },
};

byId["42"]; // O(1) average
```

Điểm cần nhớ:

- Object key là `string` hoặc `symbol`; number key bị stringify.
- `Object.keys(obj).length` là O(n), không giống `map.size`.
- Lookup có thể đi qua prototype chain nếu property không phải own property.
- `delete obj.key` trong hot path có thể làm object shape thay đổi và khiến engine deopt.
- Dictionary nhận key từ user input cần tránh prototype pollution.

An toàn hơn khi key đến từ bên ngoài:

```ts
const safeDict: Record<string, User> = Object.create(null);
```

Hoặc dùng `Map` để tránh đụng các key như `__proto__`, `constructor`, `toString`.

### 3.6. Map/Set: tại sao thường O(1)?

Mental model:

```txt
key/value -> hash -> bucket index -> entry
```

**Map/Set - tại sao O(1)?**

1. **Hash Function:** key được chuyển thành hash rồi map về bucket index, thường theo dạng `hash % buckets.length`.
2. **Direct Access:** engine truy cập thẳng bucket theo index, nên bước tìm bucket là O(1).
3. **Collision Handling:** nếu nhiều key rơi vào cùng bucket, engine lưu nhiều entry trong bucket đó, ví dụ collision chain hoặc cấu trúc tương đương.
4. **Average Case:** hash phân bố đều, ít collision, mỗi bucket ngắn nên `get`, `set`, `has`, `delete` gần O(1).
5. **Worst Case:** nếu quá nhiều key cùng rơi vào một bucket, lookup phải duyệt nhiều entry và có thể tiến tới O(n).

**Internal Structure minh họa:**

```txt
Map internal:
buckets: [
  0: null,
  1: { key: "a", value: 1, next: { key: "x", value: 2 } },
  2: { key: "b", value: 3 },
  ...
]

hash("a") % buckets.length = 1 -> bucket[1]
hash("x") % buckets.length = 1 -> collision -> chain with "a"
```

💡 Đây là mô hình học để hiểu Big O, không phải mô tả chính xác 100% implementation của mọi JavaScript engine. V8, SpiderMonkey và JavaScriptCore có thể dùng layout và chiến lược collision khác nhau, nhưng ý chính vẫn là lookup nhanh nhờ hash table, còn collision làm chi phí tăng.

### 3.7. Ưu và nhược điểm

**`Map` / `Set`**

✅ Ưu điểm:

- O(1) average cho lookup/membership.
- Key linh hoạt hơn object.
- `.size` O(1).
- Iteration giữ insertion order.
- Hợp cho frequent add/delete và cache nội bộ.

⚠️ Nhược điểm:

- Không serialize JSON trực tiếp.
- Tốn memory hơn array/object đơn giản.
- Syntax dài hơn object literal.
- Debug/inspect đôi khi kém trực quan hơn plain object.

**`Object`**

✅ Ưu điểm:

- Literal syntax ngắn.
- JSON serialization tự nhiên.
- Hợp với fixed shape data, props, API payload.
- Engine tối ưu tốt cho object shape ổn định.

⚠️ Nhược điểm:

- Key giới hạn `string`/`symbol`.
- Không có `.size` O(1).
- Có prototype chain và prototype pollution risk.
- Add/delete dynamic nhiều có thể làm mất tối ưu engine.

**`Array`**

✅ Ưu điểm:

- Giữ order tự nhiên.
- API mạnh cho transform/render list.
- Index access O(1).
- `push`/`pop` O(1) amortized.

⚠️ Nhược điểm:

- Search O(n).
- Insert/delete đầu/giữa O(n).
- `includes` trong loop dễ thành O(n²).
- Sparse/holey arrays có thể làm engine xử lý chậm hơn.

### 3.8. WeakMap / WeakSet

`WeakMap` và `WeakSet` dùng object làm key/value yếu, không giữ object khỏi garbage collection.

Dùng khi cần gắn metadata với object mà không muốn tạo memory leak:

```ts
const meta = new WeakMap<object, { measuredAt: number }>();

const node = document.createElement("div");
meta.set(node, { measuredAt: Date.now() });
```

Điểm cần nhớ:

- Key của `WeakMap` phải là object.
- Không iterable.
- Không có `.size`.
- Hợp cho cache metadata, DOM node metadata, private data theo object lifecycle.

## 4. 🧪 Practical TypeScript/JavaScript Examples

### 4.1. Lookup user theo id: array scan vs normalized map

❌ O(n) mỗi lần tìm:

```ts
type User = { id: number; name: string; role: "admin" | "user" };

function findUserName(users: User[], id: number): string | undefined {
  return users.find((user) => user.id === id)?.name;
}
```

✅ Build index một lần O(n), lookup O(1) average:

```ts
function indexUsers(users: User[]): Map<number, User> {
  return new Map(users.map((user) => [user.id, user]));
}

const usersById = indexUsers(users);
const name = usersById.get(42)?.name;
```

Tradeoff: build index tốn thêm memory. Đáng làm khi lookup lặp lại nhiều lần, ví dụ table 10k rows, joining API responses, permission checks.

### 4.2. Tránh O(n²) khi filter theo selected IDs

❌ `includes` bên trong `filter` có thể thành O(n * m):

```ts
const selectedIds = [1, 5, 9, 42];
const selectedUsers = users.filter((user) => selectedIds.includes(user.id));
```

✅ Convert sang `Set`:

```ts
const selectedIdSet = new Set(selectedIds);
const selectedUsers = users.filter((user) => selectedIdSet.has(user.id));
```

### 4.3. Dedupe primitive và object

✅ Dedupe primitive values:

```ts
const tags = ["react", "next", "react", "security"];
const uniqueTags = [...new Set(tags)];
```

❌ `Set<object>` không dedupe theo nội dung:

```ts
const items = [{ id: 1 }, { id: 1 }];
const unique = [...new Set(items)];

console.log(unique.length); // 2
```

✅ Dedupe object theo `id`:

```ts
type Product = { id: string; name: string };

function uniqueByLastId(products: Product[]): Product[] {
  return [...new Map(products.map((product) => [product.id, product])).values()];
}
```

Giữ item đầu tiên:

```ts
function uniqueByFirstId(products: Product[]): Product[] {
  const seen = new Set<string>();
  const result: Product[] = [];

  for (const product of products) {
    if (seen.has(product.id)) continue;
    seen.add(product.id);
    result.push(product);
  }

  return result;
}
```

### 4.4. Object dictionary: own property và prototype pollution

❌ Dễ sai khi key đến từ user input:

```ts
const dict: Record<string, number> = {};

function increment(key: string) {
  dict[key] = (dict[key] ?? 0) + 1;
}
```

✅ Dùng `Map` hoặc object không prototype:

```ts
const counts = new Map<string, number>();

function increment(key: string) {
  counts.set(key, (counts.get(key) ?? 0) + 1);
}
```

Hoặc:

```ts
const safeCounts: Record<string, number> = Object.create(null);
```

Khi đọc object thường, ưu tiên own property:

```ts
if (Object.hasOwn(dict, key)) {
  // key là own property, không phải từ prototype chain
}
```

### 4.5. React state với `Set`

❌ Mutate `Set` cũ: React có thể không render lại vì reference không đổi.

```tsx
setSelectedIds((prev) => {
  prev.add(id);
  return prev;
});
```

✅ Tạo reference mới:

```tsx
setSelectedIds((prev) => {
  const next = new Set(prev);
  next.add(id);
  return next;
});
```

Toggle selection:

```tsx
function toggleId(id: number) {
  setSelectedIds((prev) => {
    const next = new Set(prev);

    if (next.has(id)) {
      next.delete(id);
    } else {
      next.add(id);
    }

    return next;
  });
}
```

### 4.6. React memoization cho membership check

```tsx
type Row = { id: number; name: string };

function UserTable({
  rows,
  selectedIds,
}: {
  rows: Row[];
  selectedIds: number[];
}) {
  const selectedIdSet = React.useMemo(
    () => new Set(selectedIds),
    [selectedIds],
  );

  return (
    <tbody>
      {rows.map((row) => (
        <tr key={row.id} data-selected={selectedIdSet.has(row.id)}>
          <td>{row.name}</td>
        </tr>
      ))}
    </tbody>
  );
}
```

💡 `useMemo` chỉ có ích nếu `selectedIds` reference ổn định và membership check xảy ra nhiều lần trong render. Nếu list nhỏ, code đơn giản có thể tốt hơn.

### 4.7. `unshift` nhiều lần vs `push` rồi `reverse`

❌ `unshift` trong loop dễ tạo O(n²):

```ts
const result: number[] = [];

for (const item of items) {
  result.unshift(item);
}
```

✅ `push` O(1) amortized rồi `reverse` O(n):

```ts
const result: number[] = [];

for (const item of items) {
  result.push(item);
}

result.reverse();
```

## 5. 🏭 Production Notes / React Implications

- **State normalization:** Với entities, cân nhắc `{ ids: string[]; byId: Record<string, Entity> }` hoặc `Map` nội bộ để lookup/update rõ hơn.
- **React reference equality:** Không mutate `Array`, `Object`, `Map`, `Set` trong state. Tạo reference mới để React render và memoization hoạt động đúng.
- **Memoization:** `useMemo(() => new Set(ids), [ids])` hợp lý khi membership check lặp lại trong render hoặc data lớn.
- **API/SSR/localStorage boundary:** JSON ưu tiên `Array`/plain `Object`. `Map`/`Set` nên convert ở boundary.
- **Performance:** Chỉ tối ưu khi có hot path thật: virtualized table, autocomplete lớn, drag/drop, filter/search liên tục, real-time updates.
- **Security:** Với dictionary nhận key từ input, dùng validation, `Object.hasOwn`, `Object.create(null)` hoặc `Map` để giảm prototype pollution risk.
- **Memory:** `Map`/`Set` có overhead. Với list nhỏ hoặc one-off iteration, `Array` thường đơn giản và đủ nhanh.
- **Engine behavior:** Object fixed shape thường được optimize tốt; add/delete dynamic nhiều có thể làm engine deopt. Sparse arrays cũng có thể chậm hơn packed arrays.
- **Testing:** Test duplicate IDs, missing keys, empty list, object keys, numeric-string key conversion, và update immutable trong React.

## 6. ⚠️ Common Pitfalls

- ❌ Nói `Map`/`Set` “luôn O(1)” thay vì “O(1) average”.
- ❌ Dùng `array.includes()` bên trong loop lớn rồi vô tình tạo O(n²).
- ❌ Dedupe object bằng `new Set(objects)` và tưởng rằng nó so sánh deep value.
- ❌ Mutate `Map`/`Set` trong React state rồi return cùng reference.
- ❌ Dùng `delete obj.key` liên tục trong hot path khiến object shape thay đổi.
- ❌ Dùng object dictionary với untrusted keys mà không nghĩ tới prototype pollution.
- ❌ Quên `Object.keys(obj).length` là O(n), không giống `map.size`.
- ❌ Tạo sparse array bằng cách gán index quá xa rồi kỳ vọng performance như packed array.
- ❌ Convert `Map<number, T>` sang object và quên rằng key number thành string.
- ❌ Tối ưu sớm: đổi mọi array nhỏ sang map/set làm code khó đọc hơn mà không có bottleneck thật.

## 7. ✅ Decision Guide or Checklist

### Chọn cấu trúc nào?

| Nhu cầu | Chọn | Lý do |
|---|---|---|
| Render list theo thứ tự | `Array` | Tự nhiên cho `.map()` và UI ordering |
| Truy cập theo index | `Array` | O(1), API đơn giản |
| Tìm item theo `id` nhiều lần | `Map` hoặc `Record` | Tránh scan O(n) lặp lại |
| Key là object/function/Date | `Map` | Object không giữ object key đúng nghĩa |
| Check membership nhiều lần | `Set` | `.has()` O(1) average |
| Dedupe primitive values | `Set` | Ngắn và O(n) tổng |
| Dedupe object theo id | `Map` hoặc `Set` theo id | Không phụ thuộc reference object |
| Gửi qua API/JSON | `Object`/`Array` | Serialize trực tiếp |
| Config/props/API payload | `Object` | Plain shape dễ đọc và dễ debug |
| Dynamic add/delete nhiều | `Map` | API rõ, ít phụ thuộc object shape |
| Dictionary với untrusted keys | `Map` hoặc `Object.create(null)` | Giảm prototype pollution risk |
| Metadata gắn với object lifecycle | `WeakMap` | Không giữ object khỏi GC |


## 8. 🗣️ Short Interview Answer

Theo em, Big O ở nhóm `Map`, `Set`, `Array`, `Object` chủ yếu giúp mình chọn data structure theo access pattern. `Array` rất tốt cho list có thứ tự và render UI, truy cập index O(1), nhưng search bằng `find/includes/indexOf` là O(n). Nếu lookup theo `id` nhiều lần, em thường normalize sang `Map` hoặc `Record` để tránh scan lặp lại.

`Map` và `Set` thường có `get/has/set/delete` O(1) trung bình nhờ hash table: key được hash ra bucket index rồi truy cập trực tiếp. Nhưng em sẽ nói rõ đây là average case, vì collision hoặc engine implementation có thể làm worst case xấu hơn. `Object` cũng O(1) average cho property access và rất hợp cho JSON/config/API payload, nhưng key chỉ là string/symbol và phải cẩn thận prototype pollution.

Trong React, điểm quan trọng là không mutate array/object/map/set tại chỗ trong state. React dựa vào reference equality, nên phải tạo reference mới. Em chỉ đổi sang `Map`/`Set` khi lookup hoặc membership check thật sự lặp lại trong hot path; còn với list nhỏ, readability thường quan trọng hơn.

## 9. 🧾 Ghi nhớ nhanh

- `Array.find/includes/indexOf` là O(n); dùng trong loop có thể thành O(n²).
- `Array.push/pop` là O(1) amortized; `shift/unshift/splice` đầu/giữa là O(n).
- `Map`/`Set` lookup là O(1) average nhờ hash table, không phải guarantee tuyệt đối.
- Collision làm bucket dài hơn, worst case có thể tiến tới O(n).
- `Object` tốt cho plain data và JSON; `Map` tốt cho dynamic dictionary/cache.
- `Object.keys(obj).length` là O(n); `map.size` và `set.size` là O(1).
- `Set<object>` so sánh bằng reference, không so sánh deep value.
- React state với `Array/Object/Map/Set`: update immutable, tạo reference mới.
- Dictionary từ user input: cân nhắc `Map`, `Object.create(null)`, `Object.hasOwn`.
- Tối ưu theo access pattern và profiling, không theo cảm giác.

## 10. 📖 Giải thích các thuật ngữ trong topic

- `Big O`: Ký hiệu mô tả tốc độ tăng chi phí khi input lớn lên.
- `O(1)`: Chi phí gần như không đổi theo kích thước dữ liệu.
- `O(n)`: Chi phí tăng tuyến tính theo số phần tử.
- `O(n²)`: Chi phí tăng theo bình phương, thường do loop lồng nhau hoặc search tuyến tính trong loop.
- `O(n log n)`: Chi phí thường gặp ở thuật toán sort hiệu quả.
- `Amortized O(1)`: Trung bình nhiều lần thao tác là O(1), dù một vài lần có thể đắt hơn, ví dụ array resize khi `push`.
- `Hash table`: Cấu trúc dùng hash để tìm bucket, là mental model quan trọng cho `Map`/`Set`.
- `Hash function`: Hàm chuyển key/value thành hash code để chọn bucket.
- `Bucket`: Vị trí lưu entry trong hash table.
- `Collision`: Nhiều key rơi vào cùng bucket, khiến lookup cần thêm bước xử lý.
- `Insertion order`: Thứ tự phần tử được thêm vào, được `Map`/`Set` giữ khi iterate.
- `Prototype chain`: Chuỗi prototype mà object có thể tra cứu property khi own property không tồn tại.
- `Prototype pollution`: Lỗi bảo mật khi input thay đổi prototype của object, có thể ảnh hưởng toàn app.
- `Object shape`: Cấu trúc property mà JavaScript engine dùng để tối ưu object.
- `Deopt`: Khi engine bỏ tối ưu đã áp dụng vì object/code thay đổi theo hướng khó tối ưu.
- `Sparse array`: Array có nhiều hole do index không liên tục, có thể làm engine dùng representation chậm hơn.
- `Reference equality`: Hai object/array/map/set chỉ bằng nhau nếu cùng reference, không phải cùng nội dung.
- `Structural sharing`: Tạo object mới nhưng tái sử dụng phần không đổi, giúp immutable update hiệu quả.
- `Serialization boundary`: Ranh giới cần chuyển dữ liệu sang dạng serialize được, ví dụ JSON qua API, SSR payload, localStorage.
- `Hot path`: Đoạn code chạy rất thường xuyên hoặc ảnh hưởng trực tiếp tới trải nghiệm, đáng profiling và tối ưu.
