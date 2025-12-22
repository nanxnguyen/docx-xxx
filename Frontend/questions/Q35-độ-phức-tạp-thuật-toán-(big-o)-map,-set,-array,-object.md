# 📈 Q35: Độ Phức Tạp Thuật Toán (Big O) - Map, Set, Array, Object

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"Big O mô tả performance khi data scale. Map/Set = O(1) average (hash table), Array = O(1) index access nhưng O(n) search, Object = O(1) property access."**

**🔑 Performance Comparison:**

| **Operation** | **Map/Set** | **Object** | **Array** |
|--------------|------------|-----------|----------|
| **Access** | O(1) avg | O(1) | O(1) - index, O(n) - search |
| **Insert** | O(1) avg | O(1) | O(1) - end, O(n) - start/middle |
| **Delete** | O(1) avg | O(1) | O(1) - end, O(n) - start/middle |
| **Search** | O(1) - `.has()` | O(n) - loop keys | O(n) - `.indexOf()` |
| **Iterate** | O(n) | O(n) | O(n) |

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




**Trả lời:****

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
 * *Array push() có độ phức tạp trung bình O(1) (tự động resize khi cần)
 */

// ============================================
// 1️⃣ MAP - TRUY CẬP/THÊM/XÓA O(1)
// ============================================

// 🗺️ Tạo Map để lưu trữ user với ID là key
const userMap = new Map<number, string>();

// ➕ Thêm 1 triệu users - O(1) cho mỗi lần thêm
// Cách hoạt động: hash key → tìm bucket → chèn vào bucket
console.time('Map insert 1M');
for (let i = 0; i < 1_000_000; i++) {
  userMap.set(i, `User${i}`); // ⚡ O(1) mỗi lần - siêu nhanh!
}
console.timeEnd('Map insert 1M'); // ⏱️ ~100-200ms

// 🔍 Truy cập - O(1) nhờ hash table
// Cách hoạt động: hash key → truy cập trực tiếp bucket
console.time('Map get');
const user = userMap.get(500_000); // ⚡ O(1) - tìm ngay lập tức
console.timeEnd('Map get'); // ⏱️ ~0.001ms (cực nhanh!)

// 🗑️ Xóa - O(1) tương tự get
// Cách hoạt động: hash key → tìm bucket → xóa entry
console.time('Map delete');
userMap.delete(500_000); // ⚡ O(1)
console.timeEnd('Map delete'); // ⏱️ ~0.001ms

// ✅️⃣ SET - THÊM/KIỂM TRA/XÓA O(1)
// ============================================

// 🎯 Tạo Set để lưu các ID duy nhất (không trùng lặp)
const uniqueIds = new Set<number>();

// ➕ Thêm vào Set - O(1) cho mỗi lần
// Cách hoạt động: hash value → bucket → kiểm tra trùng → chèn
console.time('Set add 1M');
for (let i = 0; i < 1_000_000; i++) {
  uniqueIds.add(i); // ⚡ O(1) - tự động loại bỏ trùng lặp
}
console.timeEnd('Set add 1M'); // ⏱️ ~100-200ms

// ✅ Kiểm tra phần tử tồn tại - O(1)
// Cách hoạt động: hash value → check bucket
console.time('Set has');
const exists = uniqueIds.has(500_000); // ⚡ O(1) - check cực nhanh
console.timeEnd('Set has'); // ⏱️ ~0.001ms

// 🗑️ Xóa phần tử - O(1)
uniqueIds.delete(500_000); // ⚡ O(1)

// 💡 Use case thực tế: Loại bỏ phần tử trùng lặp - O(n)
const arrWithDupes = [1, 2, 2, 3, 3, 3, 4]; // 📦 Mảng có trùng lặp
const unique = [...new Set(arrWithDupes)]; // ✨ O(n) duyệt + O(1) add = O(n) tổng
console.log(unique); // 📊 [1, 2, 3, 4] - chỉ giữ lại giá trị duy nhất
// Use case: Remove duplicates O(n)
const arrWithDupes = [1, 2, 2, 3, 3, 3, 4];
const unique = [...new Set(arrWithDupes)]; // O(n) iterate + O(1) add = O(n) total
cons️⃣ OBJECT - TRUY CẬP PROPERTY O(1)
// ============================================

// 📦 Tạo Object rỗng để lưu users (key phải là string)
const userObj: Record<string, string> = {};

// ➕ Thêm property - O(1) cho mỗi lần
// Cách hoạt động: hash key (string) → bucket
console.time('Object insert 1M');
for (let i = 0; i < 1_000_000; i++) {
  userObj[`user${i}`] = `User${i}`; // ⚡ O(1)
}
console.timeEnd('Object insert 1M'); // ⏱️ ~150-250ms (chậm hơn Map một chút)

// 🔍 Truy cập property - O(1)
console.time('Object access');
const objUser = userObj['user500000']; // ⚡ O(1) - truy cập trực tiếp
console.timeEnd('Object access'); // ⏱️ ~0.001ms

// 🗑️ Xóa property - O(1)
delete userObj['user500000']; // ⚡ O(1)

// ⚠️ LƯU Ý: Prototype chain có thể làm chậm!
// O(1) nếu là own property, O(k) nếu phải tìm trong chain (k = độ sâu chain)
cons️⃣ ARRAY - ĐỘ PHỨC TẠP HỖN HỢP
// ============================================

// 📚 Tạo mảng rỗng
const arr: number[] = [];

// ➕ Push (thêm vào cuối) - O(1) trung bình
// Tự động resize khi hết capacity
console.time('Array push 1M');
for (let i = 0; i < 1_000_000; i++) {
  arr.push(i); // ⚡ O(1) trung bình - cực nhanh
}
console.timeEnd('Array push 1M'); // ⏱️ ~50-100ms (NHANH NHẤT vì bộ nhớ liên tục)

// 🔍 Truy cập theo index - O(1) siêu nhanh!
// Tính toán trực tiếp: địa chỉ = base + (index * size)
console.time('Array access');
const val = arr[500_000]; // ⚡ O(1) - truy cập memory trực tiếp
console.timeEnd('Array access'); // ⏱️ ~0.0001ms (NHANH NHẤT!)

// 🔎 Tìm kiếm giá trị - O(n) CHẬM!
// Phải duyệt từng phần tử một
console.time('Array indexOf');
const idx = arr.indexOf(500_000); // 🐌 O(n) worst case - phải duyệt toàn bộ
console.timeEnd('Array indexOf'); // ⏱️ ~5-10ms (chậm hơn nhiều)

// ✅ Kiểm tra tồn tại - O(n) CHẬM!
console.time('Array includes');
const has = arr.includes(500_000); // 🐌 O(n) - phải duyệt tuần tự
console.timeEnd('Array includes'); // ⏱️ ~5-10ms

// ⬇️ Unshift (thêm vào đầu) - O(n) RẤT CHẬM!
// Phải dịch chuyển TẤT CẢ phần tử sang phải
console.time('Array unshift');
arr.unshift(-1); // 🐢 O(n) - phải di chuyển 1 TRIỆU phần tử!
console.timeEnd('Array unshift'); // ⏱️ ~50-100ms (RẤT CHẬM!)

// ⬆️ Shift (xóa phần tử đầu) - O(n) RẤT CHẬM!
// Phải dịch chuyển TẤT CẢ phần tử sang trái
console.time('Array shift');
arr.shift(); // 🐢 O(n) - phải di chuyển toàn bộ
cons️⃣ SO SÁNH THỰC TÉ - CHỌN CẤU TRÚC NÀO?
// ============================================

// 💼 Scenario 1: Tìm kiếm user theo ID (thường xuyên)
// ❌ CÁCH TỆ: Dùng Array - O(n) mỗi lần tìm
const usersArr = [
  { id: 1, name: 'A' },
  { id: 2, name: 'B' },
  // ... 1 triệu users
];
const user1 = usersArr.find((u) => u.id === 500_000); // 🐌 O(n) - phải duyệt toàn bộ, CHẬM!

// ✅ CÁCH TỐT: Dùng Map - O(1) mỗi lần tìm
const usersMap = new Map([
  [1, { id: 1, name: 'A' }],
  [2, { id: 2, name: 'B' }],
]);
const user2 = usersMap.get(500_000); // ⚡ O(1) - tìm ngay lập tức, NHANH!

// 💼 Scenario 2: Kiểm tra tag có tồn tại không
// ❌ CÁCH TỆ: Dùng Array - O(n)
const tags = ['js', 'ts', 'react', 'vue'];
const hasReact = tags.includes('react'); // 🐌 O(n) - phải duyệt từng phần tử

// ✅ CÁCH TỐT: Dùng Set - O(1)
const tagSet = new Set(['js', 'ts', 'react', 'vue']);
const hasReact2 = tagSet.has('react'); // ⚡ O(1) - check tức thì

// 💼 Scenario 3: Loại bỏ phần tử trùng lặp
// ❌ CÁCH TỆ: Dùng nested loop - O(n²) CỰC CHẬM!
function removeDupes(arr: number[]): number[] {
  const result: number[] = [];
  for (const item of arr) {
    // 🔁 Loop 1: O(n)
    if (!result.includes(item)) {
      // 🔁 Loop 2: O(n) - phải check toàn bộ result
      result.push(item);
    }
  }
  return result; // 🐢 O(n²) tổng cộng - RẤT CHẬM với data lớn!
}

// ✅ CÁCH TỐT: Dùng Set - O(n) NHANH!
function removeDupesSet(arr: number[]): number[] {
  return [...new Set(arr)]; // ⚡ O(n) duyệt + O(1) add = O(n) tổng - NHANH!
  for (const item of arr) {
    // O(n)
    if (!result.includes(item)) {
      // O(n)
      result.push(item);
    }
  }️⃣ TẠI SAO MAP/SET LẠI O(1)? - MINH HỌA
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
  private hash(key: K): number {
    const str = String(key); // 📝 Convert key thành string
    let hash = 0;
    for (let i = 0; i < str.length; i++) {
      // 🔄 Duyệt từng ký tự
      hash = (hash << 5) - hash + str.charCodeAt(i); // 🧮 Tính hash
      hash = hash & hash; // 🔢 Convert thành 32-bit integer
    }
    return Math.abs(hash); // ✅ Trả về số dương
  }

  // ➕ Thêm hoặc cập nhật entry
  set(key: K, value: V): void {
    const index = this.hash(key) % this.buckets.length; // 📍 Tìm bucket index
    const bucket = this.buckets[index]; // 📦 Lấy bucket

    // 🔍 Kiểm tra key đã tồn tại chưa (để update)
    for (const entry of bucket) {
      if (entry.key === key) {
        entry.value = value; // 🔄 Update value cũ
        return;
      }
    }

    // ✨ Key mới → thêm vào cuối chain
    bucket.push({ key, value });
    this.size++;
  }

  // 🔍 Lấy giá trị theo key
  get(key: K): V | undefined {
    const index = this.hash(key) % this.buckets.length; // 📍 Tìm bucket
    const bucket = this.buckets[index]; // 📦 Lấy bucket

    // 🔗 Duyệt chain - O(k) với k = độ dài chain (thường rất ngắn)
    for (const entry of bucket) {
      if (entry.key === key) {
        return entry.value; // ✅ Tìm thấy!
      }
    }

    return undefined; // ❌ Không tìm thấy
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

// 🎬 Demo collision (va chạm hash)
const hashMap = new SimpleHashMap<string, number>(8);
hashMap.set('apple', 1); // 🍎
hashMap.set('banana', 2); // 🍌
hashMap.set('cherry', 3); // 🍒
hashMap.visualize();
// 💡 Output sẽ show collision nếu hash('apple') % 8 === hash('banana') % 8
// (2 key khác nhau nhưng rơi vào cùng 1 bucket)
  }
}

// Demo collision
const hashMap = new SimpleHashMap<string, number>(8);
hashMap.set('apple', 1);
hashMap.set('banana', 2);
hashMap.set('cherry', 3);
hashMap.visualize();
// Output sẽ show collision nếu hash('apple') % 8 === hash('banana') % 8
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
     // ❌ Chậm: O(n²)
     posts.forEach(p => users.find(u => u.id === p.userId));
     // ✅ Nhanh: O(n)
     const userMap = new Map(users.map(u => [u.id, u]));
     posts.forEach(p => userMap.get(p.userId));
     ```
   
   - ⚡ **Dùng Set.has() thay Array.includes()**: O(1) vs O(n)
     ```ts
     // ❌ Chậm: O(n)
     const tags = ['js', 'ts', 'react'];
     if (tags.includes('react')) { /* ... */ }
     // ✅ Nhanh: O(1)
     const tagSet = new Set(['js', 'ts', 'react']);
     if (tagSet.has('react')) { /* ... */ }
     ```
   
   - 🔄 **Avoid unshift/shift trong loop**: Dùng push + reverse thay vì
     ```ts
     // ❌ Chậm: O(n²)
     items.forEach(item => arr.unshift(item)); // mỗi lần shift toàn bộ
     // ✅ Nhanh: O(n)
     items.forEach(item => arr.push(item));
     arr.reverse(); // 1 lần duy nhất
     ```
   
   - 📦 **Pre-allocate Array size**: Tránh resize nhiều lần
     ```ts
     // ❌ Resize nhiều lần khi push
     const arr = [];
     for (let i = 0; i < 1000000; i++) arr.push(i);
     // ✅ Allocate 1 lần
     const arr = new Array(1000000);
     for (let i = 0; i < 1000000; i++) arr[i] = i;
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
   
   - 📊 **Monitor performance**: Chrome DevTools → Performance tab
     - ⏱️ Xem time spent trong map operations
     - 🔬 Profile với large datasets (>100k items)
   ============================================
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
  // 🔁 Loop bên ngoài: 1M lần
  const author = users.find((u) => u.id === post.authorId); // 🔁 Loop bên trong: 1M lần
  // 💀 Tổng: O(n²) = 1 triệu × 1 triệu = 1,000 TỶ operations!
  // ⏱️ Có thể mất vài PHÚT để chạy xong!
});

// ✅ CÁCH SỬA: Build Map trước → O(n) NHANH!
const userMap = new Map(users.map((u) => [u.id, u])); // 🏗️ Build Map 1 lần: O(n)
posts.forEach((post) => {
  // 🔁 Loop: 1M lần
  const author = userMap.get(post.authorId); // ⚡ Lookup: O(1)
  // ✅ Tổng: O(n) = 1 triệu operations
  // ⏱️ Chạy xong trong vài GIÂY!
});

// ❌ LỖI 2: Check duplicate bằng includes → O(n²) CHẬM!
const unique: number[] = [];
arr.forEach((item) => {
  // 🔁 Loop bên ngoài: n lần
  if (!unique.includes(item)) {
    // 🔁 includes phải duyệt unique: O(n)
    unique.push(item);
  }
}); // 💀 Tổng: O(n²) - càng nhiều item càng CHẬM!

// ✅ CÁCH SỬA: Dùng Set → O(n) NHANH!
const unique2 = [...new Set(arr)]; // ⚡ O(n) - 1 lần duyệt, xong ngay!

// ❌ LỖI 3: Xóa array items trong loop → O(n²) CHẬM!
for (let i = 0; i < arr.length; i++) {
  if (condition) {
    arr.splice(i, 1); // 🐢 O(n) - phải shift TẤT CẢ elements phía sau
    i--; // 🔄 Điều chỉnh index (dễ gây bug!)
  }
} // 💀 Tổng: O(n²) - mỗi lần xóa phải shift, RẤT CHẬM!

// ✅ CÁCH SỬA: Dùng filter → O(n) NHANH VÀ AN TOÀN!
const filtered = arr.filter((item) => !condition); // ⚡ O(n) - 1 lần duyệt, tạo mảng mới
// 💡 Không modify mảng gốc → tránh bug + dễ debug!
    unique.push(item);
  }
}); // Total O(n²)

// ✅ Đúng: Dùng Set → O(n)
const unique2 = [...new Set(arr)]; // O(n)

// ❌ Sai: Delete array items trong loop → O(n²)
for (let i = 0; i < arr.length; i++) {
  if (condition) {
    arr.splice(i, 1); // O(n) - shift elements
    i--; // adjust index
  }
} // Total O(n²)

// ✅ Đúng: Filter → O(n)
const filtered = arr.filter((item) => !condition); // O(n)
```

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
// ❌ BEFORE: Chậm, khó maintain
function processOrders(orders, users, products) {
  return orders.map(order => ({
    ...order,
    user: users.find(u => u.id === order.userId), // O(n) mỗi lần
    items: order.itemIds.map(id => 
      products.find(p => p.id === id) // O(n) mỗi lần
    )
  }));
}
// 💀 Complexity: O(n × m × k) - CỰC CHẬM!

// ✅ AFTER: Nhanh, scalable
function processOrders(orders, users, products) {
  // 🏗️ Build lookup maps 1 lần: O(n + m)
  const userMap = new Map(users.map(u => [u.id, u]));
  const productMap = new Map(products.map(p => [p.id, p]));
  
  return orders.map(order => ({
    ...order,
    user: userMap.get(order.userId), // ⚡ O(1)
    items: order.itemIds.map(id => productMap.get(id)) // ⚡ O(1)
  }));
}
// ✅ Complexity: O(n + m + k) - NHANH, scale tốt!
```

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

