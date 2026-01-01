# 📈 Q35: Độ Phức Tạp Thuật Toán (Big O) - Map, Set, Array, Object

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"Big O mô tả performance khi data scale. Map/Set = O(1) average (hash table), Array = O(1) index access nhưng O(n) search, Object = O(1) property access."**

**🔑 Performance Comparison:**

| **Operation** | **Map/Set**     | **Object**       | **Array**                       |
| ------------- | --------------- | ---------------- | ------------------------------- |
| **Access**    | O(1) avg        | O(1)             | O(1) - index, O(n) - search     |
| **Insert**    | O(1) avg        | O(1)             | O(1) - end, O(n) - start/middle |
| **Delete**    | O(1) avg        | O(1)             | O(1) - end, O(n) - start/middle |
| **Search**    | O(1) - `.has()` | O(n) - loop keys | O(n) - `.indexOf()`             |
| **Iterate**   | O(n)            | O(n)             | O(n)                            |

**🔑 Chi Tiết Từng Cấu Trúc:**

**1. Map/Set - Hash Table (O(1) average):**

- **Internal**: Hash function → bucket index → direct access
- **Collision**: Cùng hash → linked list/tree trong bucket
- **Average O(1)**: Hash function phân bố đều → ít collision
- **Worst O(n)**: Tất cả keys cùng hash (rất hiếm)

**2. Object - Similar Map (O(1) average):**

- **Keys**: Chỉ strings/symbols (Map dùng any type)
- **Property access**: `obj.prop` hoặc `obj['prop']` → O(1)
- **Search value**: Phải loop `Object.values()` → O(n)
- **Prototype chain**: Lookup theo chain nếu không có own property

**3. Array - Contiguous Memory (mixed):**

- **Index access**: `arr[5]` → O(1) (direct memory offset)
- **Search**: `.indexOf()`, `.includes()` → **O(n)** (linear scan)
- **Push/pop** (end): O(1) - không shift
- **Unshift/shift** (start): **O(n)** - phải shift tất cả elements
- **Splice** (middle): **O(n)** - shift elements sau insertion point

**⚠️ Lỗi Thường Gặp:**

- Dùng `array.indexOf()` trong loop → O(n²), dùng Set cho O(n)
- `array.unshift()` nhiều lần → O(n²), dùng `.push()` rồi `.reverse()`
- Nghĩ Object lookup **luôn O(1)** → Sai! Prototype chain có thể O(k) với k = chain depth
- Dùng `delete obj.key` trong hot path → deoptimize V8, dùng `obj.key = undefined` thay vì

**💡 Kiến Thức Senior:**

- **Map vs Object performance**: Map nhanh hơn cho **frequent add/delete** (Object shape changes → deoptimize)
- **Set for uniqueness**: `[...new Set(arr)]` dedup = O(n), `arr.filter((v,i,a) => a.indexOf(v)===i)` = O(n²)
- **Sparse arrays**: `arr[1000] = 1` tạo holes → kiểu dữ liệu thay đổi (dictionary mode), chậm hơn
- **WeakMap/WeakSet**: O(1) nhưng không prevent GC, không iterable

**Trả lời:\*\***

- Khái niệm: Big O notation mô tả hiệu năng thuật toán khi data tăng lên; quan trọng để chọn cấu trúc dữ liệu phù hợp.
- Map/Set: O(1) average cho get/set/delete nhờ hash table; O(n) worst case khi hash collision nhiều (rất hiếm).
- Object: O(1) average cho property access; tương tự Map nhưng chỉ key string/symbol.
- Array: O(1) index access; O(n) search (indexOf, includes); O(n) insert/delete đầu/giữa (phải shift elements).

**Hoạt động Chi Tiết:**

**Map/Set - Tại sao O(1)?**

1. **Hash Function**: Key được hash thành index (0-buckets.length)
2. **Direct Access**: Truy cập bucket qua index → O(1)
3. **Collision Handling**: Cùng hash → lưu linked list/tree trong bucket
4. **Average Case**: Ít collision → O(1); hash tốt phân bố đều
5. **Worst Case**: Nhiều collision → O(n) (tất cả key cùng bucket)

**Internal Structure:**

```
Map internal:
buckets: [
  0: null,
  1: { key: 'a', value: 1, next: { key: 'x', value: 2 } }, // collision chain
  2: { key: 'b', value: 3 },
  ...
]

Hash('a') % buckets.length = 1 → bucket[1]
Hash('x') % buckets.length = 1 → collision → chain với 'a'
```

**✅ Ưu điểm:**

**🗺️ Map/Set:**

- ⚡ **O(1) thao tác**: Get, set, delete cực nhanh nhờ hash table
- 🔑 **Key linh hoạt**: Key có thể là bất kỳ type (object, function, number, string...)
- 📋 **Maintain insertion order**: Duyệt theo thứ tự thêm vào (quan trọng cho UI rendering)
- 📏 **Size property built-in**: `map.size` - không cần `Object.keys().length`
- 🔄 **Iterate dễ dàng**: `.forEach()`, `for...of` hoặc spread `[...map]`

**📦 Object:**

- ✍️ **Syntax ngắn gọn**: Literal syntax `{ key: value }` - viết nhanh
- 📡 **JSON serializable**: `JSON.stringify()` trực tiếp, dễ gửi qua API
- 🔗 **Prototype chain**: Kế thừa methods từ prototype (toString, hasOwnProperty...)
- 🏃 **V8 optimized**: Engine tối ưu cho object shapes cố định

**📚 Array:**

- 🎯 **O(1) index access**: Truy cập `arr[i]` cực nhanh, nhanh nhất trong tất cả
- 🛠️ **Nhiều built-in methods**: map, filter, reduce, sort, slice... rất tiện
- 📋 **Maintain order**: Giữ thứ tự phần tử, quan trọng cho list data
- 🔄 **Stack/Queue operations**: push/pop (O(1)) cho stack, shift/unshift cho queue

**❌ Nhược điểm:**

**🗺️ Map/Set:**

- 📝 **Syntax dài hơn**: `.set()`, `.get()` thay vì `obj.key` - verbose hơn
- 🚫 **Không serialize JSON**: Phải convert: `JSON.stringify([...map])` hoặc `Array.from(map)`
- 💾 **Tốn memory hơn**: Hash table overhead ~2x so với Object (buckets + pointers)
- 🔍 **Debugging khó hơn**: DevTools preview không rõ bằng Object literal

**📦 Object:**

- 🔤 **Chỉ string/symbol keys**: Không dùng được object/number làm key trực tiếp
- 📏 **Không có size built-in**: Phải dùng `Object.keys(obj).length` - O(n)
- ⚠️ **Prototype pollution risk**: Thêm `__proto__` có thể gây security issue
- 🐌 **Delete chậm**: `delete obj.key` deoptimize V8 shape, gây chậm
- 🔗 **Prototype chain overhead**: Lookup property phải traverse chain

**📚 Array:**

- 🐢 **O(n) search**: `.indexOf()`, `.includes()` phải duyệt tuần tự - chậm với data lớn
- 🐌 **O(n) insert/delete đầu/giữa**: `unshift()`, `shift()`, `splice()` phải dịch chuyển elements
- 💾 **Memory fragmentation**: Sparse array `arr[1000] = 1` tạo holes, chuyển sang dictionary mode
- 🔢 **Type changes**: Từ packed → holey → dictionary mode khi thay đổi cấu trúc

**💡 Chú Thích - Khi Nào Dùng Gì:**

**🗺️ Dùng Map khi:**

- 🔑 Cần key không phải string (object, number, Date, function...)
- ➕ Thao tác thêm/xóa thường xuyên (Map nhanh hơn Object khi shape changes)
- 📏 Cần track size real-time: `map.size` thay vì `Object.keys().length`
- 🔄 Cần iterate theo thứ tự insertion
- 💼 **Use case**: Cache (key = object), lookup table với composite keys

**📦 Dùng Object khi:**

- 📝 Config/options đơn giản, ít thay đổi
- 📡 Cần serialize JSON để gửi API: `JSON.stringify(obj)`
- 🔤 Keys chỉ là string/symbol
- 🏃 Performance critical với V8 optimization (fixed shape)
- 💼 **Use case**: API response, component props, settings

**📚 Dùng Array khi:**

- 📋 Cần maintain order và iterate nhiều: `map()`, `filter()`, `reduce()`
- 🎯 Truy cập theo index thường xuyên: `arr[i]`
- 📊 List data homogeneous (cùng type): users[], products[]
- 🔄 Stack/queue operations: push/pop
- 💼 **Use case**: Danh sách items, time series data, UI lists

**🎯 Dùng Set khi:**

- ✨ Loại duplicate O(1): `[...new Set(arr)]`
- ✅ Check existence nhanh: `set.has(item)` thay vì `arr.includes(item)`
- 🔢 Quản lý unique IDs, tags
- 🚀 Union/intersection operations: `new Set([...setA, ...setB])`
- 💼 **Use case**: Unique tags, visited IDs, deduplication

**Code Example:**

```ts
// ============================================
// 📊 BẢNG SO SÁNH ĐỘ PHỨC TẠP BIG O
// ============================================

/**
 * 📋 BẢNG THAM KHẢO NHANH:
 *
 * Thao tác          | Array      | Object     | Map        | Set
 * ------------------|------------|------------|------------|------------
 * Truy cập          | O(1)       | O(1)       | O(1)       | N/A
 * Tìm kiếm giá trị  | O(n)       | O(n)       | O(n)       | O(1)
 * Thêm vào cuối     | O(1)*      | O(1)       | O(1)       | O(1)
 * Thêm vào đầu      | O(n)       | O(1)       | O(1)       | O(1)
 * Xóa               | O(n)       | O(1)       | O(1)       | O(1)
 * Duyệt qua         | O(n)       | O(n)       | O(n)       | O(n)
 *
 * 💡 GIẢI THÍCH CHI TIẾT:
 *
 * *Array push() có độ phức tạp trung bình O(1):
 *   - Thêm vào cuối mảng: O(1) - chỉ cần ghi vào vị trí cuối
 *   - Khi hết capacity: Tự động resize (double size) → O(n) nhưng hiếm xảy ra
 *   - Trung bình: O(1) vì resize chỉ xảy ra log(n) lần trong n lần push
 *
 * Array tìm kiếm O(n):
 *   - Phải duyệt từ đầu đến cuối để tìm giá trị
 *   - Worst case: Phần tử ở cuối hoặc không tồn tại → duyệt hết n phần tử
 *
 * Set tìm kiếm O(1):
 *   - Dùng hash table → hash value → tìm bucket → O(1) trung bình
 *   - Nhanh hơn Array.includes() rất nhiều với data lớn
 */

// ============================================
// 1️⃣ MAP - TRUY CẬP/THÊM/XÓA O(1)
// ============================================

// ============================================
// 🗺️ MAP - TRUY CẬP/THÊM/XÓA O(1)
// ============================================

// 🗺️ Tạo Map để lưu trữ user với ID là key
// 💡 Map<number, string> = key là number, value là string
const userMap = new Map<number, string>();

// ➕ Thêm 1 triệu users - O(1) cho mỗi lần thêm
// 💡 Cách hoạt động chi tiết:
//   1. hash(key) → tính hash code của key (VD: hash(500000) = 12345)
//   2. bucket_index = hash % buckets.length → tìm bucket (VD: 12345 % 16 = 1)
//   3. Chèn entry vào bucket[1] → O(1) trung bình
console.time('Map insert 1M');
for (let i = 0; i < 1_000_000; i++) {
  userMap.set(i, `User${i}`);
  // ⚡ O(1) mỗi lần - siêu nhanh!
  // 💡 Không cần duyệt qua các phần tử khác
  // 💡 Hash function tự động tìm đúng bucket
}
console.timeEnd('Map insert 1M');
// ⏱️ ~100-200ms cho 1 triệu lần insert
// 💡 So sánh: Array.push() ~50-100ms (nhanh hơn vì memory liên tục)
// 💡 Nhưng Map.get() nhanh hơn Array.indexOf() rất nhiều!

// 🔍 Truy cập - O(1) nhờ hash table
// 💡 Cách hoạt động chi tiết:
//   1. hash(500000) → hash code
//   2. bucket_index = hash % buckets.length → tìm bucket
//   3. Truy cập trực tiếp bucket[index] → O(1)
//   4. Nếu có collision → duyệt chain (thường rất ngắn) → vẫn O(1) trung bình
console.time('Map get');
const user = userMap.get(500_000);
// ⚡ O(1) - tìm ngay lập tức
// 💡 Không cần duyệt qua 500,000 phần tử như Array.indexOf()
console.timeEnd('Map get');
// ⏱️ ~0.001ms (cực nhanh!)
// 💡 So sánh: Array.indexOf() ~5-10ms cho 1 triệu phần tử

// 🗑️ Xóa - O(1) tương tự get
// 💡 Cách hoạt động:
//   1. hash(key) → tìm bucket
//   2. Tìm entry trong bucket (hoặc chain)
//   3. Xóa entry → O(1) trung bình
console.time('Map delete');
userMap.delete(500_000);
// ⚡ O(1) - xóa ngay lập tức
// 💡 Không cần shift các phần tử khác như Array.splice()
console.timeEnd('Map delete');
// ⏱️ ~0.001ms

// ============================================
// ✅ SET - THÊM/KIỂM TRA/XÓA O(1)
// ============================================

// 🎯 Tạo Set để lưu các ID duy nhất (không trùng lặp)
// 💡 Set<number> = chỉ lưu các giá trị duy nhất (tự động loại trùng)
const uniqueIds = new Set<number>();

// ➕ Thêm vào Set - O(1) cho mỗi lần
// 💡 Cách hoạt động chi tiết:
//   1. hash(value) → tính hash code của giá trị
//   2. bucket_index = hash % buckets.length → tìm bucket
//   3. Kiểm tra bucket xem đã có value chưa
//   4. Nếu chưa có → chèn vào → O(1)
//   5. Nếu đã có → bỏ qua (tự động loại trùng)
console.time('Set add 1M');
for (let i = 0; i < 1_000_000; i++) {
  uniqueIds.add(i);
  // ⚡ O(1) - tự động loại bỏ trùng lặp
  // 💡 Nếu add(5) 2 lần → chỉ lưu 1 lần
  // 💡 Không cần check thủ công như Array.includes()
}
console.timeEnd('Set add 1M');
// ⏱️ ~100-200ms cho 1 triệu lần add
// 💡 Tương tự Map về performance

// ✅ Kiểm tra phần tử tồn tại - O(1)
// 💡 Cách hoạt động:
//   1. hash(value) → hash code
//   2. bucket_index = hash % buckets.length
//   3. Check bucket có chứa value không → O(1)
console.time('Set has');
const exists = uniqueIds.has(500_000);
// ⚡ O(1) - check cực nhanh
// 💡 So sánh: Array.includes(500000) → O(n) phải duyệt toàn bộ
console.timeEnd('Set has');
// ⏱️ ~0.001ms (cực nhanh!)
// 💡 Array.includes() ~5-10ms cho 1 triệu phần tử

// 🗑️ Xóa phần tử - O(1)
uniqueIds.delete(500_000);
// ⚡ O(1) - xóa ngay lập tức
// 💡 Tương tự Map.delete()

// 💡 Use case thực tế: Loại bỏ phần tử trùng lặp - O(n)
const arrWithDupes = [1, 2, 2, 3, 3, 3, 4];
// 📦 Mảng có trùng lặp: số 2 xuất hiện 2 lần, số 3 xuất hiện 3 lần

const unique = [...new Set(arrWithDupes)];
// ✨ O(n) duyệt + O(1) add = O(n) tổng
// 💡 Cách hoạt động:
//   1. new Set(arrWithDupes) → duyệt mảng, add vào Set → O(n)
//   2. Set tự động loại trùng → chỉ giữ lại giá trị duy nhất
//   3. [...set] → convert Set về Array → O(n)
//   4. Tổng: O(n) + O(n) = O(n) - NHANH!

console.log(unique);
// 📊 [1, 2, 3, 4] - chỉ giữ lại giá trị duy nhất

// 💡 So sánh với cách thủ công (CHẬM):
// ❌ Cách chậm: O(n²)
// const unique: number[] = [];
// for (const item of arrWithDupes) {
//   if (!unique.includes(item)) { // O(n) mỗi lần check
//     unique.push(item);
//   }
// } // Tổng: O(n²) - RẤT CHẬM với data lớn!
// ============================================
// 📦 OBJECT - TRUY CẬP PROPERTY O(1)
// ============================================

// 📦 Tạo Object rỗng để lưu users (key phải là string)
// 💡 Record<string, string> = object với key string, value string
// ⚠️ Object chỉ chấp nhận string/symbol làm key (không như Map)
const userObj: Record<string, string> = {};

// ➕ Thêm property - O(1) cho mỗi lần
// 💡 Cách hoạt động:
//   1. Hash key (string) → hash code
//   2. Tìm bucket trong internal hash table của Object
//   3. Chèn property vào bucket → O(1)
// 💡 Tương tự Map nhưng chỉ dùng được string/symbol keys
console.time('Object insert 1M');
for (let i = 0; i < 1_000_000; i++) {
  userObj[`user${i}`] = `User${i}`;
  // ⚡ O(1) - tương tự Map.set()
  // 💡 Syntax ngắn gọn hơn Map: obj.key thay vì map.set(key, value)
}
console.timeEnd('Object insert 1M');
// ⏱️ ~150-250ms (chậm hơn Map một chút)
// 💡 Lý do: V8 engine optimize Object cho fixed shape (cấu trúc cố định)
// 💡 Khi thêm/xóa nhiều → shape changes → deoptimize → chậm hơn Map

// 🔍 Truy cập property - O(1)
// 💡 Cách hoạt động:
//   1. Hash key → hash code
//   2. Tìm bucket → O(1)
//   3. Nếu không tìm thấy trong own properties → traverse prototype chain
console.time('Object access');
const objUser = userObj['user500000'];
// ⚡ O(1) - truy cập trực tiếp
// 💡 Nhanh nhất khi property là own property (không phải từ prototype)
console.timeEnd('Object access');
// ⏱️ ~0.001ms (cực nhanh, tương tự Map)

// 🗑️ Xóa property - O(1) nhưng có thể deoptimize V8
delete userObj['user500000'];
// ⚡ O(1) - xóa ngay lập tức
// ⚠️ LƯU Ý: delete có thể làm chậm V8 engine!
// 💡 Lý do: delete thay đổi object shape → V8 phải reoptimize
// ✅ TỐT HƠN: userObj['user500000'] = undefined (giữ shape, chỉ set undefined)

// ⚠️ LƯU Ý: Prototype chain có thể làm chậm!
// 💡 O(1) nếu là own property (property trực tiếp của object)
// 💡 O(k) nếu phải tìm trong prototype chain (k = độ sâu chain)
//
// Ví dụ:
// const obj = {};
// obj.prop = 'value'; // ✅ Own property → O(1)
//
// const parent = { inherited: 'value' };
// const child = Object.create(parent);
// child.inherited; // ⚠️ Phải traverse prototype chain → O(k) với k = 1
// ============================================
// 📚 ARRAY - ĐỘ PHỨC TẠP HỖN HỢP
// ============================================

// 📚 Tạo mảng rỗng
// 💡 Array lưu các phần tử trong memory liên tục (contiguous memory)
// 💡 Mỗi phần tử chiếm cùng số bytes → tính địa chỉ nhanh
const arr: number[] = [];

// ➕ Push (thêm vào cuối) - O(1) trung bình
// 💡 Cách hoạt động:
//   1. Ghi giá trị vào vị trí cuối cùng → O(1)
//   2. Tăng length lên 1 → O(1)
//   3. Nếu hết capacity → resize (double size) → O(n) nhưng hiếm
//   4. Trung bình: O(1) vì resize chỉ xảy ra log(n) lần
console.time('Array push 1M');
for (let i = 0; i < 1_000_000; i++) {
  arr.push(i);
  // ⚡ O(1) trung bình - cực nhanh
  // 💡 Memory liên tục → cache-friendly → CPU đọc nhanh
}
console.timeEnd('Array push 1M');
// ⏱️ ~50-100ms (NHANH NHẤT vì bộ nhớ liên tục)
// 💡 Nhanh hơn Map/Set vì không cần hash function

// 🔍 Truy cập theo index - O(1) siêu nhanh!
// 💡 Cách hoạt động:
//   1. Tính địa chỉ memory: address = base_address + (index × element_size)
//   2. Truy cập trực tiếp memory tại địa chỉ đó → O(1)
// 💡 Không cần hash, không cần duyệt → nhanh nhất!
console.time('Array access');
const val = arr[500_000];
// ⚡ O(1) - truy cập memory trực tiếp
// 💡 VD: base = 1000, index = 500000, size = 8 bytes
// 💡 address = 1000 + (500000 × 8) = 4,001,000 → đọc ngay!
console.timeEnd('Array access');
// ⏱️ ~0.0001ms (NHANH NHẤT!)

// 🔎 Tìm kiếm giá trị - O(n) CHẬM!
// 💡 Cách hoạt động:
//   1. Duyệt từ đầu mảng đến cuối
//   2. So sánh từng phần tử với giá trị cần tìm
//   3. Worst case: Phần tử ở cuối hoặc không tồn tại → duyệt hết n phần tử
console.time('Array indexOf');
const idx = arr.indexOf(500_000);
// 🐌 O(n) worst case - phải duyệt toàn bộ
// 💡 Phải check: arr[0] === 500000? → arr[1] === 500000? → ... → arr[500000] === 500000? ✓
// 💡 Tổng: 500,001 lần so sánh!
console.timeEnd('Array indexOf');
// ⏱️ ~5-10ms (chậm hơn nhiều so với Map.get() ~0.001ms)

// ✅ Kiểm tra tồn tại - O(n) CHẬM!
// 💡 Tương tự indexOf(), phải duyệt tuần tự
console.time('Array includes');
const has = arr.includes(500_000);
// 🐌 O(n) - phải duyệt tuần tự
// 💡 So sánh: Set.has() → O(1) cực nhanh!
console.timeEnd('Array includes');
// ⏱️ ~5-10ms

// ⬇️ Unshift (thêm vào đầu) - O(n) RẤT CHẬM!
// 💡 Cách hoạt động:
//   1. Dịch TẤT CẢ phần tử sang phải 1 vị trí
//   2. Ghi giá trị mới vào vị trí đầu
//   3. Tăng length lên 1
// 💡 Phải di chuyển n phần tử → O(n)
console.time('Array unshift');
arr.unshift(-1);
// 🐢 O(n) - phải di chuyển 1 TRIỆU phần tử!
// 💡 arr[0] → arr[1], arr[1] → arr[2], ..., arr[999999] → arr[1000000]
// 💡 Tổng: 1 triệu lần copy memory!
console.timeEnd('Array unshift');
// ⏱️ ~50-100ms (RẤT CHẬM!)

// ⬆️ Shift (xóa phần tử đầu) - O(n) RẤT CHẬM!
// 💡 Cách hoạt động:
//   1. Xóa phần tử đầu
//   2. Dịch TẤT CẢ phần tử còn lại sang trái 1 vị trí
//   3. Giảm length xuống 1
// 💡 Phải di chuyển n-1 phần tử → O(n)
console.time('Array shift');
arr.shift();
// 🐢 O(n) - phải di chuyển toàn bộ
// 💡 arr[1] → arr[0], arr[2] → arr[1], ..., arr[1000000] → arr[999999]
console.timeEnd('Array shift');
// ⏱️ ~50-100ms

// 💡 TIP: Nếu cần thêm vào đầu nhiều lần → dùng push() + reverse()
// ✅ CÁCH TỐT:
// items.forEach(item => arr.push(item)); // O(n) - nhanh
// arr.reverse(); // O(n) - 1 lần duyệt
// Tổng: O(n) thay vì O(n²) với unshift()
// ============================================
// 💼 SO SÁNH THỰC TẾ - CHỌN CẤU TRÚC NÀO?
// ============================================

// 💼 Scenario 1: Tìm kiếm user theo ID (thường xuyên)
// ❌ CÁCH TỆ: Dùng Array - O(n) mỗi lần tìm
const usersArr = [
  { id: 1, name: 'A' },
  { id: 2, name: 'B' },
  // ... 1 triệu users
];
const user1 = usersArr.find((u) => u.id === 500_000);
// 🐌 O(n) - phải duyệt toàn bộ, CHẬM!
// 💡 find() duyệt từ đầu: check id 1, 2, 3, ..., 500000
// 💡 Worst case: User ở cuối → duyệt hết 1 triệu phần tử
// ⏱️ Thời gian: ~5-10ms mỗi lần tìm

// ✅ CÁCH TỐT: Dùng Map - O(1) mỗi lần tìm
const usersMap = new Map([
  [1, { id: 1, name: 'A' }],
  [2, { id: 2, name: 'B' }],
  // ... build Map từ usersArr
]);
const user2 = usersMap.get(500_000);
// ⚡ O(1) - tìm ngay lập tức, NHANH!
// 💡 Hash(500000) → bucket → tìm ngay
// ⏱️ Thời gian: ~0.001ms mỗi lần tìm
// 💡 Nhanh hơn Array.find() ~5000-10000 lần!

// 💼 Scenario 2: Kiểm tra tag có tồn tại không
// ❌ CÁCH TỆ: Dùng Array - O(n)
const tags = ['js', 'ts', 'react', 'vue'];
const hasReact = tags.includes('react');
// 🐌 O(n) - phải duyệt từng phần tử
// 💡 Check: 'js' === 'react'? → 'ts' === 'react'? → 'react' === 'react'? ✓
// 💡 Phải check 3 phần tử mới tìm thấy

// ✅ CÁCH TỐT: Dùng Set - O(1)
const tagSet = new Set(['js', 'ts', 'react', 'vue']);
const hasReact2 = tagSet.has('react');
// ⚡ O(1) - check tức thì
// 💡 Hash('react') → bucket → check ngay
// 💡 Không cần duyệt qua các tag khác

// 💼 Scenario 3: Loại bỏ phần tử trùng lặp
// ❌ CÁCH TỆ: Dùng nested loop - O(n²) CỰC CHẬM!
function removeDupes(arr: number[]): number[] {
  const result: number[] = [];
  for (const item of arr) {
    // 🔁 Loop 1: O(n) - duyệt qua n phần tử
    if (!result.includes(item)) {
      // 🔁 Loop 2: O(n) - phải check toàn bộ result
      // 💡 Mỗi lần includes() phải duyệt result từ đầu đến cuối
      result.push(item);
    }
  }
  return result;
  // 🐢 O(n²) tổng cộng - RẤT CHẬM với data lớn!
  // 💡 VD: 1000 phần tử → 1000 × 1000 = 1 TRIỆU operations!
  // ⏱️ Thời gian: ~100-200ms cho 1000 phần tử
}

// ✅ CÁCH TỐT: Dùng Set - O(n) NHANH!
function removeDupesSet(arr: number[]): number[] {
  return [...new Set(arr)];
  // ⚡ O(n) duyệt + O(1) add = O(n) tổng - NHANH!
  // 💡 Cách hoạt động:
  //   1. new Set(arr) → duyệt arr, add vào Set → O(n)
  //   2. Set tự động loại trùng → O(1) mỗi lần add
  //   3. [...set] → convert về Array → O(n)
  //   4. Tổng: O(n) + O(n) = O(n)
  // ⏱️ Thời gian: ~1-2ms cho 1000 phần tử
  // 💡 Nhanh hơn cách tệ ~50-100 lần!
}

// ============================================
// 🎓 TẠI SAO MAP/SET LẠI O(1)? - MINH HỌA
// ============================================

/**
 * 🏗️ CẤU TRÚC BÊN TRONG HASH TABLE:
 *
 * 🔑 Hash Function: key → hash code (số nguyên)
 * 📍 Bucket Index: hash % buckets.length (lấy phần dư để tìm vị trí)
 *
 * 📦 Ví dụ: Map với 8 buckets (8 ngăn chứa)
 *
 * buckets = [
 *   0: null,                                   // 📭 Ngăn trống
 *   1: Entry('apple', 5) → null,              // 🍎 Không collision
 *   2: Entry('banana', 10) → Entry('blueberry', 12) → null, // 💥 Collision! 2 key cùng bucket
 *   3: null,                                   // 📭 Ngăn trống
 *   4: Entry('cherry', 8) → null,             // 🍒 Không collision
 *   5: null,                                   // 📭 Ngăn trống
 *   6: null,                                   // 📭 Ngăn trống
 *   7: null                                    // 📭 Ngăn trống
 * ]
 *
 * 🔍 THAO TÁC GET (Lấy giá trị):
 * map.get('banana')
 * 1. 🔢 hash('banana') = 18
 * 2. 📍 bucket_index = 18 % 8 = 2 (tìm ngăn số 2)
 * 3. ➡️ Đi tới buckets[2]
 * 4. 🔗 Duyệt linked list: 'banana' === 'banana' ✓ (tìm thấy!)
 * 5. 📤 Trả về value: 10
 * → ⚡ O(1) trung bình (vì chain ngắn)
 *
 * ➕ THAO TÁC SET (Thêm/Cập nhật):
 * map.set('grape', 15)
 * 1. 🔢 hash('grape') = 10
 * 2. 📍 bucket_index = 10 % 8 = 2 (ngăn số 2)
 * 3. 💥 Collision với 'banana' chain (cùng ngăn!)
 * 4. 🔗 Thêm vào cuối chain
 * → ⚡ O(1) trung bình
 *
 * 🛠️ GIẢI QUYẾT COLLISION:
 * - 🔗 Chaining: Dùng linked list trong mỗi bucket
 * - 🔄 Open Addressing: Tìm bucket trống tiếp theo
 * - 🚀 JS engines dùng chaining + tự động resize khi load factor cao
 */

// 🎓 Class minh họa Hash Map đơn giản
class SimpleHashMap<K, V> {
  // 🗄️ Mảng các buckets, mỗi bucket là 1 mảng các entry
  private buckets: Array<Array<{ key: K; value: V }>> = [];
  private size = 0;

  constructor(capacity = 16) {
    // 🏗️ Khởi tạo 16 buckets rỗng
    this.buckets = Array(capacity)
      .fill(null)
      .map(() => []);
  }

  // 🔢 Hash function: chuyển key thành số nguyên
  // 💡 Hash function là "trái tim" của hash table
  // 💡 Mục tiêu: Phân bố đều keys vào các buckets → ít collision
  private hash(key: K): number {
    const str = String(key);
    // 📝 Convert key thành string để hash
    // 💡 VD: number 123 → "123", object → "[object Object]"

    let hash = 0;
    for (let i = 0; i < str.length; i++) {
      // 🔄 Duyệt từng ký tự trong string
      hash = (hash << 5) - hash + str.charCodeAt(i);
      // 🧮 Tính hash code:
      //   - hash << 5 = hash × 32 (dịch bit sang trái 5 vị trí)
      //   - hash << 5 - hash = hash × 31 (tối ưu hơn phép nhân)
      //   - + str.charCodeAt(i) = cộng mã ASCII của ký tự
      // 💡 Công thức này phân bố đều → ít collision

      hash = hash & hash;
      // 🔢 Convert thành 32-bit integer (loại bỏ phần dư)
      // 💡 & hash = bitwise AND với chính nó (không đổi nhưng đảm bảo 32-bit)
    }
    return Math.abs(hash);
    // ✅ Trả về số dương (hash code)
    // 💡 VD: hash("apple") = 1234567890
  }

  // ➕ Thêm hoặc cập nhật entry
  // 💡 Độ phức tạp: O(1) trung bình, O(k) worst case (k = độ dài chain)
  set(key: K, value: V): void {
    const index = this.hash(key) % this.buckets.length;
    // 📍 Tìm bucket index:
    //   1. hash(key) → hash code (VD: 1234567890)
    //   2. % this.buckets.length → lấy phần dư (VD: 1234567890 % 16 = 2)
    //   3. → bucket index = 2
    // 💡 Modulo (%) đảm bảo index nằm trong phạm vi [0, buckets.length-1]

    const bucket = this.buckets[index];
    // 📦 Lấy bucket tại index đó
    // 💡 Bucket là một mảng các entry (có thể có collision chain)

    // 🔍 Kiểm tra key đã tồn tại chưa (để update)
    for (const entry of bucket) {
      // 💡 Duyệt qua chain trong bucket (nếu có collision)
      if (entry.key === key) {
        entry.value = value;
        // 🔄 Update value cũ (key đã tồn tại)
        // 💡 Không tăng size vì không thêm entry mới
        return;
      }
    }

    // ✨ Key mới → thêm vào cuối chain
    bucket.push({ key, value });
    // 💡 Thêm entry mới vào bucket
    // 💡 Nếu bucket rỗng → chain có 1 phần tử
    // 💡 Nếu bucket đã có entry → thêm vào chain (collision)
    this.size++;
    // 💡 Tăng số lượng entries
  }

  // 🔍 Lấy giá trị theo key
  // 💡 Độ phức tạp: O(1) trung bình, O(k) worst case (k = độ dài chain)
  get(key: K): V | undefined {
    const index = this.hash(key) % this.buckets.length;
    // 📍 Tìm bucket index (giống như set())
    // 💡 hash(key) → hash code → % buckets.length → bucket index

    const bucket = this.buckets[index];
    // 📦 Lấy bucket tại index đó

    // 🔗 Duyệt chain - O(k) với k = độ dài chain (thường rất ngắn)
    // 💡 Nếu không có collision → chain có 1 phần tử → O(1)
    // 💡 Nếu có collision → phải duyệt chain → O(k) với k thường < 5
    for (const entry of bucket) {
      if (entry.key === key) {
        return entry.value;
        // ✅ Tìm thấy!
        // 💡 So sánh key để tìm đúng entry trong chain
      }
    }

    return undefined;
    // ❌ Không tìm thấy
    // 💡 Đã duyệt hết chain nhưng không có key khớp
  }

  // 📊 Hiển thị cấu trúc buckets để debug
  visualize(): void {
    this.buckets.forEach((bucket, idx) => {
      if (bucket.length > 0) {
        console.log(
          `📦 Bucket ${idx}:`,
          bucket.map((e) => `${e.key}=${e.value}`).join(' → ')
        );
      }
    });
  }
}

// ============================================
// 🎬 Demo collision (va chạm hash)
// ============================================

// 🎬 Demo collision (va chạm hash)
// 💡 Collision = 2 key khác nhau nhưng có cùng hash code → cùng bucket
const hashMap = new SimpleHashMap<string, number>(8);
// 💡 Tạo hash map với 8 buckets (ít buckets → dễ collision hơn)

hashMap.set('apple', 1);
// 🍎 hash('apple') % 8 = ? → bucket index
hashMap.set('banana', 2);
// 🍌 hash('banana') % 8 = ? → bucket index
hashMap.set('cherry', 3);
// 🍒 hash('cherry') % 8 = ? → bucket index

hashMap.visualize();
// 💡 Output sẽ show collision nếu hash('apple') % 8 === hash('banana') % 8
// 💡 VD output:
//    📦 Bucket 2: apple=1 → banana=2  (collision!)
//    📦 Bucket 5: cherry=3
// 💡 Collision xảy ra khi 2 key khác nhau nhưng rơi vào cùng 1 bucket
// 💡 JS engines tự động resize khi có quá nhiều collision → maintain O(1)
```

**🎯 Best Practices - Tối Ưu Performance:**

**1️⃣ Chọn cấu trúc dữ liệu phù hợp:**

- 🔍 **Lookup thường xuyên** → Map/Object (O(1) vs Array O(n))
- ✅ **Check existence** → Set (O(1) vs Array O(n))
- 📋 **Ordered collection + iterate** → Array (cache-friendly, methods nhiều)
- ⚙️ **Simple config** → Object (syntax ngắn, JSON-friendly)
- 🔑 **Non-string keys** → Map (object, number, Date...)
- ✨ **Deduplication** → Set (tự động loại trùng)

**2️⃣ Performance Tips - Tối Ưu Tốc Độ:**

- 🚀 **Dùng Map thay Array.find()**: Lookup nhiều lần → O(n) thành O(1)

  ```ts
  // ❌ Chậm: O(n²) - CỰC CHẬM!
  posts.forEach((p) => users.find((u) => u.id === p.userId));
  // 💡 Giải thích:
  //   - Loop bên ngoài: posts.forEach() → n lần (n = số posts)
  //   - Loop bên trong: users.find() → O(m) mỗi lần (m = số users)
  //   - Tổng: O(n × m) = O(n²) nếu n ≈ m
  //   - VD: 1000 posts × 1000 users = 1 TRIỆU operations!

  // ✅ Nhanh: O(n) - NHANH HƠN RẤT NHIỀU!
  const userMap = new Map(users.map((u) => [u.id, u]));
  // 💡 Build Map 1 lần: O(m) - duyệt users, tạo Map
  // 💡 users.map() → O(m), new Map() → O(m) → Tổng O(m)

  posts.forEach((p) => userMap.get(p.userId));
  // 💡 Loop: n lần
  // 💡 Mỗi lần: userMap.get() → O(1) (hash lookup)
  // 💡 Tổng: O(m) + O(n) = O(n + m) ≈ O(n) nếu n > m
  // 💡 VD: 1000 posts → chỉ 1000 operations (thay vì 1 TRIỆU!)
  ```

- ⚡ **Dùng Set.has() thay Array.includes()**: O(1) vs O(n)

  ```ts
  // ❌ Chậm: O(n) - phải duyệt tuần tự
  const tags = ['js', 'ts', 'react'];
  if (tags.includes('react')) {
    /* ... */
  }
  // 💡 Giải thích:
  //   - includes() phải duyệt từ đầu: 'js' === 'react'? → 'ts' === 'react'? → 'react' === 'react'? ✓
  //   - Worst case: Phần tử ở cuối hoặc không tồn tại → duyệt hết n phần tử
  //   - VD: 1000 tags → phải check 1000 lần

  // ✅ Nhanh: O(1) - hash lookup tức thì
  const tagSet = new Set(['js', 'ts', 'react']);
  if (tagSet.has('react')) {
    /* ... */
  }
  // 💡 Giải thích:
  //   - Set.has() dùng hash table: hash('react') → bucket → check ngay
  //   - Không cần duyệt qua các tag khác
  //   - VD: 1000 tags → chỉ cần 1 operation (hash + check bucket)
  // 💡 Nhanh hơn Array.includes() ~1000 lần với 1000 phần tử!
  ```

- 🔄 **Avoid unshift/shift trong loop**: Dùng push + reverse thay vì

  ```ts
  // ❌ Chậm: O(n²) - RẤT CHẬM!
  items.forEach((item) => arr.unshift(item));
  // 💡 Giải thích:
  //   - Loop: n lần (n = số items)
  //   - Mỗi lần unshift(): Phải shift TẤT CẢ phần tử hiện có → O(m) với m = số phần tử hiện tại
  //   - Lần 1: unshift(item1) → shift 0 phần tử → O(1)
  //   - Lần 2: unshift(item2) → shift 1 phần tử → O(1)
  //   - Lần 3: unshift(item3) → shift 2 phần tử → O(2)
  //   - ...
  //   - Lần n: unshift(itemN) → shift n-1 phần tử → O(n-1)
  //   - Tổng: O(1 + 1 + 2 + ... + n-1) = O(n²)
  //   - VD: 1000 items → ~500,000 operations!

  // ✅ Nhanh: O(n) - NHANH HƠN RẤT NHIỀU!
  items.forEach((item) => arr.push(item));
  // 💡 push() vào cuối: O(1) mỗi lần
  // 💡 Tổng: O(n) cho n lần push

  arr.reverse();
  // 💡 reverse() 1 lần: O(n) - duyệt và đảo ngược
  // 💡 Tổng: O(n) + O(n) = O(n)
  // 💡 VD: 1000 items → chỉ ~2000 operations (thay vì 500,000!)
  ```

- 📦 **Pre-allocate Array size**: Tránh resize nhiều lần

  ```ts
  // ❌ Resize nhiều lần khi push - CHẬM HƠN
  const arr = [];
  for (let i = 0; i < 1000000; i++) arr.push(i);
  // 💡 Giải thích:
  //   - Array bắt đầu với capacity nhỏ (VD: 4)
  //   - Khi hết capacity → resize (double size) → copy toàn bộ elements
  //   - Resize xảy ra: 4 → 8 → 16 → 32 → ... → 1,048,576
  //   - Mỗi lần resize: O(n) copy elements
  //   - Tổng: O(n) cho push + O(n) cho resize = O(n) nhưng có overhead
  //   - VD: 1M items → resize ~20 lần → copy ~2M elements tổng cộng

  // ✅ Allocate 1 lần - NHANH HƠN
  const arr = new Array(1000000);
  // 💡 Pre-allocate 1 triệu slots ngay từ đầu
  // 💡 Không cần resize → không cần copy elements

  for (let i = 0; i < 1000000; i++) arr[i] = i;
  // 💡 Ghi trực tiếp vào slot đã allocate → O(1) mỗi lần
  // 💡 Tổng: O(n) không có overhead resize
  // 💡 Nhanh hơn cách trên ~10-20% với data lớn
  ```

**3️⃣ Memory Consideration - Quản Lý Bộ Nhớ:**

- 💾 **Map/Set overhead**: ~2x memory của Object/Array (buckets + pointers)

  - 💡 Trade-off: Tốn memory nhưng được O(1) lookup
  - ✅ Dùng khi performance quan trọng hơn memory

- 🕳️ **Sparse array tốn memory**: `arr[1000] = 1` tạo 999 holes

  ```ts
  // ❌ Tốn memory
  const arr = [];
  arr[1000000] = 1; // Tạo 1M holes, chuyển sang dictionary mode
  // ✅ Dùng Map
  const map = new Map();
  map.set(1000000, 1); // Chỉ lưu 1 entry
  ```

- 🔗 **Object prototype overhead**: Mỗi object có link tới prototype

  - 💡 Use `Object.create(null)` cho dictionary thuần (no prototype)

- ♻️ **WeakMap/WeakSet**: Không prevent garbage collection
  ```ts
  // ✅ Auto cleanup khi key bị GC
  const cache = new WeakMap();
  let obj = { data: 'heavy' };
  cache.set(obj, processedData);
  obj = null; // cache entry tự động bị xóa
  ```

**4️⃣ Hash Collision Mitigation - Tránh Va Chạm:**

- 🔄 **JS engines tự resize**: Load factor > 0.75 → double buckets size

  - 💡 Tự động maintain O(1) average case

- 🎲 **Good hash function**: Phân bố đều keys → ít collision

  - 🔐 V8 dùng SipHash cho security + performance

- 🚀 **Modern engines optimization**:

  - 🎯 Robin Hood hashing: Balance chain lengths
  - ⚡ Swiss Tables (Google): SIMD-accelerated lookup
  - 🔄 V8 transitions: Packed → Holey → Dictionary mode

- # 📊 **Monitor performance**: Chrome DevTools → Performance tab - ⏱️ Xem time spent trong map operations - 🔬 Profile với large datasets (>100k items)
  // ⚠️ CÁC LỖI THƯỜNG GẶP VÀ CÁCH SỬA
  // ============================================

// ============================================
// ⚠️ CÁC LỖI THƯỜNG GẶP VÀ CÁCH SỬA
// ============================================

// ❌ LỖI 1: Dùng Array.find() trong loop → O(n²) CỰC CHẬM!
const users = [
/* 1 triệu users */
];
const posts = [
/* 1 triệu posts */
];
posts.forEach((post) => {
// 🔁 Loop bên ngoài: 1M lần (duyệt qua 1 triệu posts)
const author = users.find((u) => u.id === post.authorId);
// 🔁 Loop bên trong: 1M lần (find() phải duyệt users mỗi lần)
// 💡 find() duyệt từ đầu: check user[0], user[1], ..., user[500000] mới tìm thấy
// 💀 Tổng: O(n²) = 1 triệu × 1 triệu = 1,000 TỶ operations!
// ⏱️ Có thể mất vài PHÚT để chạy xong!
// 💡 VD: 1 triệu posts × 500,000 users trung bình = 500 TỶ operations!
});

// ✅ CÁCH SỬA: Build Map trước → O(n) NHANH!
const userMap = new Map(users.map((u) => [u.id, u]));
// 🏗️ Build Map 1 lần: O(n)
// 💡 users.map() → O(n) duyệt users
// 💡 new Map() → O(n) tạo Map từ entries
// 💡 Tổng: O(n) cho việc build Map

posts.forEach((post) => {
// 🔁 Loop: 1M lần (duyệt qua 1 triệu posts)
const author = userMap.get(post.authorId);
// ⚡ Lookup: O(1) mỗi lần (hash lookup)
// 💡 Hash(post.authorId) → bucket → tìm ngay
// ✅ Tổng: O(n) = 1 triệu operations
// ⏱️ Chạy xong trong vài GIÂY!
// 💡 Nhanh hơn cách trên ~1000-10000 lần!
});

// ❌ LỖI 2: Check duplicate bằng includes → O(n²) CHẬM!
const unique: number[] = [];
arr.forEach((item) => {
// 🔁 Loop bên ngoài: n lần (duyệt qua n phần tử trong arr)
if (!unique.includes(item)) {
// 🔁 includes phải duyệt unique: O(m) với m = số phần tử trong unique hiện tại
// 💡 Lần 1: unique = [] → includes() check 0 phần tử → O(1)
// 💡 Lần 2: unique = [item1] → includes() check 1 phần tử → O(1)
// 💡 Lần 3: unique = [item1, item2] → includes() check 2 phần tử → O(2)
// 💡 ...
// 💡 Lần n: unique có n-1 phần tử → includes() check n-1 phần tử → O(n-1)
// 💀 Tổng: O(1 + 1 + 2 + ... + n-1) = O(n²) - càng nhiều item càng CHẬM!
unique.push(item);
}
});
// 💀 Tổng: O(n²) - RẤT CHẬM với data lớn!
// 💡 VD: 1000 phần tử → ~500,000 operations!

// ✅ CÁCH SỬA: Dùng Set → O(n) NHANH!
const unique2 = [...new Set(arr)];
// ⚡ O(n) - 1 lần duyệt, xong ngay!
// 💡 Giải thích:
// 1. new Set(arr) → duyệt arr, add vào Set → O(n)
// 2. Set.add() → O(1) mỗi lần (hash lookup)
// 3. Set tự động loại trùng → không cần check thủ công
// 4. [...set] → convert về Array → O(n)
// 5. Tổng: O(n) + O(n) = O(n)
// 💡 VD: 1000 phần tử → chỉ ~2000 operations (thay vì 500,000!)
// 💡 Nhanh hơn cách trên ~250 lần!

// ❌ LỖI 3: Xóa array items trong loop → O(n²) CHẬM!
for (let i = 0; i < arr.length; i++) {
if (condition) {
arr.splice(i, 1);
// 🐢 O(n) - phải shift TẤT CẢ elements phía sau
// 💡 splice(i, 1) xóa phần tử tại index i
// 💡 Sau đó phải shift: arr[i+1] → arr[i], arr[i+2] → arr[i+1], ...
// 💡 VD: Xóa arr[5] trong mảng 1000 phần tử → phải shift 995 phần tử!

    i--;
    // 🔄 Điều chỉnh index (dễ gây bug!)
    // 💡 Cần i-- vì sau khi xóa, phần tử tiếp theo đã chuyển lên vị trí i
    // 💡 Nếu không có i-- → sẽ bỏ sót phần tử tiếp theo
    // ⚠️ Dễ gây bug nếu quên i--

}
}
// 💀 Tổng: O(n²) - mỗi lần xóa phải shift, RẤT CHẬM!
// 💡 VD: Xóa 100 phần tử trong mảng 1000 phần tử
// 💡 Mỗi lần xóa shift ~500 phần tử trung bình
// 💡 Tổng: 100 × 500 = 50,000 operations!

// ✅ CÁCH SỬA: Dùng filter → O(n) NHANH VÀ AN TOÀN!
const filtered = arr.filter((item) => !condition);
// ⚡ O(n) - 1 lần duyệt, tạo mảng mới
// 💡 filter() duyệt qua arr 1 lần, tạo mảng mới với các phần tử thỏa điều kiện
// 💡 Không modify mảng gốc → tránh bug + dễ debug!
// 💡 VD: 1000 phần tử → chỉ 1000 operations (thay vì 50,000!)
// 💡 Nhanh hơn cách trên ~50 lần!

````

**🎓 Kết Luận - Tổng Kết Kiến Thức:**

**🔑 Những Điểm Chính Cần Nhớ:**

1. **📊 Map/Set - O(1) Performance:**
   - ⚡ Nhờ **hash table**: key → hash code → bucket index → direct access
   - 🎯 **Average case O(1)**: Hash function tốt phân bố đều → ít collision
   - 🐌 **Worst case O(n)**: Tất cả keys cùng hash (cực hiếm trong thực tế)
   - 💡 **Khi nào dùng**: Lookup/check existence thường xuyên, non-string keys

2. **📚 Array - Mixed Complexity:**
   - ⚡ **O(1) index access**: `arr[i]` nhanh nhất (direct memory calculation)
   - 🐌 **O(n) search**: `.indexOf()`, `.includes()` phải duyệt tuần tự
   - 🐢 **O(n) insert/delete đầu/giữa**: `unshift()`, `shift()`, `splice()` phải shift elements
   - 💡 **Khi nào dùng**: Ordered collection, iterate với map/filter/reduce

3. **📦 Object - O(1) Property Access:**
   - ⚡ **Tương tự Map**: Hash-based lookup cho properties
   - 🔤 **Giới hạn**: Chỉ string/symbol keys (Map dùng any type)
   - 🔗 **Prototype chain**: Có thể O(k) nếu property ở prototype (k = chain depth)
   - 💡 **Khi nào dùng**: Config, API response, JSON serialization

**🚀 Impact của Việc Chọn Đúng Data Structure:**

- 📈 **Performance boost**: O(n²) → O(n) khi convert Array.find() sang Map.get()
  - Ví dụ: 1M items → từ 1 TRIỆU TỶ operations xuống 1 TRIỆU operations
  - ⏱️ Thời gian: từ VÀI PHÚT xuống VÀI GIÂY!

- 💾 **Memory trade-off**: Map/Set tốn ~2x memory nhưng được O(1) lookup
  - 💡 Chọn dựa vào use case: Performance > Memory → Map/Set

- 🐛 **Code maintainability**: Set tự loại trùng, Map maintain order
  - ✅ Ít bug hơn, dễ debug hơn so với manual array manipulation

**📝 Checklist Khi Coding:**

- ✅ Có lookup/check nhiều lần? → Dùng **Map/Set** thay Array
- ✅ Cần iterate theo order? → Giữ **Array**, dùng map/filter/reduce
- ✅ Simple config ít thay đổi? → Dùng **Object** literal
- ✅ Cần loại duplicate? → `[...new Set(arr)]` thay vì filter + includes
- ✅ Insert/delete đầu mảng? → Dùng **push + reverse** thay unshift
- ✅ Check trong loop? → Build **Set/Map trước**, check O(1) trong loop

**🎯 Áp Dụng Vào Production:**

```ts
// ❌ BEFORE: Chậm, khó maintain - O(n × m × k)
function processOrders(orders, users, products) {
  return orders.map(order => ({
    // 🔁 Loop 1: orders.map() → n lần (n = số orders)
    ...order,
    user: users.find(u => u.id === order.userId),
    // 🔁 Loop 2: users.find() → O(m) mỗi lần (m = số users)
    // 💡 Mỗi order phải tìm user → n × m operations

    items: order.itemIds.map(id =>
      // 🔁 Loop 3: order.itemIds.map() → k lần (k = số items mỗi order)
      products.find(p => p.id === id)
      // 🔁 Loop 4: products.find() → O(p) mỗi lần (p = số products)
      // 💡 Mỗi item phải tìm product → n × k × p operations
    )
  }));
}
// 💀 Complexity: O(n × m × k × p) - CỰC CHẬM!
// 💡 VD: 1000 orders × 1000 users × 10 items × 500 products
// 💡 = 5 TỶ operations! → Có thể mất vài PHÚT!

// ✅ AFTER: Nhanh, scalable - O(n + m + p)
function processOrders(orders, users, products) {
  // 🏗️ Build lookup maps 1 lần: O(m + p)
  const userMap = new Map(users.map(u => [u.id, u]));
  // 💡 Build userMap: O(m) - duyệt users 1 lần

  const productMap = new Map(products.map(p => [p.id, p]));
  // 💡 Build productMap: O(p) - duyệt products 1 lần

  return orders.map(order => ({
    // 🔁 Loop: n lần (n = số orders)
    ...order,
    user: userMap.get(order.userId),
    // ⚡ O(1) - hash lookup tức thì
    // 💡 Không cần duyệt users nữa!

    items: order.itemIds.map(id => productMap.get(id))
    // ⚡ O(1) mỗi lần - hash lookup
    // 💡 Không cần duyệt products nữa!
  }));
}
// ✅ Complexity: O(m + p + n × k) ≈ O(n + m + p) - NHANH, scale tốt!
// 💡 VD: 1000 orders × 1000 users × 10 items × 500 products
// 💡 = 1,000 + 500 + (1000 × 10) = 11,500 operations!
// 💡 Nhanh hơn cách trên ~400,000 lần! ⚡
// ⏱️ Chạy xong trong vài GIÂY thay vì vài PHÚT!
````

**💪 Level Up Senior/Staff:**

- 🧠 **Hiểu internal**: Hash table, collision resolution, V8 optimization
- 📊 **Profile performance**: Chrome DevTools, measure actual impact
- 🎯 **Trade-offs**: Memory vs Speed, Readability vs Performance
- 🔬 **Advanced**: WeakMap/WeakSet cho memory management, TypedArray cho numeric data
- 📚 **Algorithm knowledge**: Biết khi nào O(n log n) sort tốt hơn O(n) linear scan

---

**🎓 Final Advice:**

> "Premature optimization is the root of all evil" - Donald Knuth
>
> ⚠️ **NHƯNG**: Biết Big O để chọn đúng data structure từ đầu ≠ premature optimization
>
> ✅ **Luôn**: Profile trước khi optimize, measure impact, document trade-offs!
