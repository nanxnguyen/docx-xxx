# 📈 Q47: Độ Phức Tạp Thuật Toán (Big O) - Map, Set, Array, Object

<details>
<summary><span style="font-size:1.25em;font-weight:bold;">📈 Q47: Độ Phức Tạp Thuật Toán (Big O) - Map, Set, Array, Object</span></summary>


**Trả lời:**

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

**Ưu điểm:**

- Map/Set: O(1) thao tác, key có thể là bất kỳ type, maintain insertion order, có size property
- Object: Syntax ngắn gọn, JSON serializable, prototype chain
- Array: O(1) index access, nhiều built-in methods, maintain order

**Nhược điểm:**

- Map/Set: Syntax dài hơn Object, không serialize JSON trực tiếp, tốn memory hơn (hash table overhead)
- Object: Chỉ string/symbol keys, không có size built-in, có thể bị prototype pollution
- Array: O(n) search/insert/delete (không phải cuối mảng), memory fragmentation với sparse array

**Chú thích:**

- Dùng Map khi cần key không phải string hoặc thao tác thêm/xóa thường xuyên
- Dùng Object cho config/options đơn giản
- Dùng Array khi cần maintain order và iterate nhiều
- Dùng Set để loại duplicate O(1)

**Code Example:**

```ts
// ============================================
// BIG O COMPARISON TABLE
// ============================================

/**
 * COMPLEXITY CHEAT SHEET:
 *
 * Operation           | Array      | Object     | Map        | Set
 * -------------------|------------|------------|------------|------------
 * Access by key/index | O(1)       | O(1)       | O(1)       | N/A
 * Search by value    | O(n)       | O(n)       | O(n)       | O(1)
 * Insert (end)       | O(1)*      | O(1)       | O(1)       | O(1)
 * Insert (start)     | O(n)       | O(1)       | O(1)       | O(1)
 * Delete             | O(n)       | O(1)       | O(1)       | O(1)
 * Iterate            | O(n)       | O(n)       | O(n)       | O(n)
 *
 * *Array push() amortized O(1) (resize khi cần)
 */

// ============================================
// 1. MAP - O(1) ACCESS/INSERT/DELETE
// ============================================

const userMap = new Map<number, string>();

// Insert O(1) - hash key → tìm bucket → insert
console.time('Map insert 1M');
for (let i = 0; i < 1_000_000; i++) {
  userMap.set(i, `User${i}`); // O(1) mỗi lần
}
console.timeEnd('Map insert 1M'); // ~100-200ms

// Access O(1) - hash key → direct bucket access
console.time('Map get');
const user = userMap.get(500_000); // O(1)
console.timeEnd('Map get'); // ~0.001ms

// Delete O(1) - hash key → tìm bucket → xóa
console.time('Map delete');
userMap.delete(500_000); // O(1)
console.timeEnd('Map delete'); // ~0.001ms

// Has O(1) - tương tự get
console.log(userMap.has(500_000)); // O(1)

// ============================================
// 2. SET - O(1) ADD/HAS/DELETE
// ============================================

const uniqueIds = new Set<number>();

// Add O(1) - hash value → bucket → check duplicate → insert
console.time('Set add 1M');
for (let i = 0; i < 1_000_000; i++) {
  uniqueIds.add(i); // O(1)
}
console.timeEnd('Set add 1M'); // ~100-200ms

// Has O(1) - hash value → check bucket
console.time('Set has');
const exists = uniqueIds.has(500_000); // O(1)
console.timeEnd('Set has'); // ~0.001ms

// Delete O(1)
uniqueIds.delete(500_000); // O(1)

// Use case: Remove duplicates O(n)
const arrWithDupes = [1, 2, 2, 3, 3, 3, 4];
const unique = [...new Set(arrWithDupes)]; // O(n) iterate + O(1) add = O(n) total
console.log(unique); // [1, 2, 3, 4]

// ============================================
// 3. OBJECT - O(1) PROPERTY ACCESS
// ============================================

const userObj: Record<string, string> = {};

// Insert O(1) - hash key (string) → bucket
console.time('Object insert 1M');
for (let i = 0; i < 1_000_000; i++) {
  userObj[`user${i}`] = `User${i}`; // O(1)
}
console.timeEnd('Object insert 1M'); // ~150-250ms (chậm hơn Map chút)

// Access O(1)
console.time('Object access');
const objUser = userObj['user500000']; // O(1)
console.timeEnd('Object access'); // ~0.001ms

// Delete O(1)
delete userObj['user500000']; // O(1)

// ⚠️ Prototype chain: O(1) nếu own property, O(k) nếu trong chain (k = độ sâu)
console.log(userObj.toString); // O(k) - tìm trong prototype chain

// ============================================
// 4. ARRAY - MIXED COMPLEXITY
// ============================================

const arr: number[] = [];

// Push O(1) amortized (resize khi capacity đầy)
console.time('Array push 1M');
for (let i = 0; i < 1_000_000; i++) {
  arr.push(i); // O(1) average
}
console.timeEnd('Array push 1M'); // ~50-100ms (nhanh nhất vì sequential memory)

// Access by index O(1) - direct memory offset
console.time('Array access');
const val = arr[500_000]; // O(1)
console.timeEnd('Array access'); // ~0.0001ms (nhanh nhất)

// Search O(n) - phải iterate toàn bộ
console.time('Array indexOf');
const idx = arr.indexOf(500_000); // O(n) worst case
console.timeEnd('Array indexOf'); // ~5-10ms

// Includes O(n)
console.time('Array includes');
const has = arr.includes(500_000); // O(n)
console.timeEnd('Array includes'); // ~5-10ms

// Unshift O(n) - phải shift tất cả elements sang phải
console.time('Array unshift');
arr.unshift(-1); // O(n) - phải move 1M elements
console.timeEnd('Array unshift'); // ~50-100ms

// Shift O(n) - phải shift tất cả elements sang trái
console.time('Array shift');
arr.shift(); // O(n)
console.timeEnd('Array shift'); // ~50-100ms

// Splice O(n) - insert/delete ở giữa
arr.splice(500_000, 1); // O(n) - phải shift elements sau vị trí xóa

// ============================================
// 5. PRACTICAL COMPARISON
// ============================================

// Scenario 1: Lookup by ID (frequent)
// ❌ Array - O(n) every time
const usersArr = [
  { id: 1, name: 'A' },
  { id: 2, name: 'B' },
  // ... 1 million users
];
const user1 = usersArr.find((u) => u.id === 500_000); // O(n) - chậm!

// ✅ Map - O(1)
const usersMap = new Map([
  [1, { id: 1, name: 'A' }],
  [2, { id: 2, name: 'B' }],
]);
const user2 = usersMap.get(500_000); // O(1) - nhanh!

// Scenario 2: Check existence
// ❌ Array - O(n)
const tags = ['js', 'ts', 'react', 'vue'];
const hasReact = tags.includes('react'); // O(n)

// ✅ Set - O(1)
const tagSet = new Set(['js', 'ts', 'react', 'vue']);
const hasReact2 = tagSet.has('react'); // O(1)

// Scenario 3: Remove duplicates
// ❌ Array - O(n²) với nested loop
function removeDupes(arr: number[]): number[] {
  const result: number[] = [];
  for (const item of arr) {
    // O(n)
    if (!result.includes(item)) {
      // O(n)
      result.push(item);
    }
  }
  return result; // O(n²) total
}

// ✅ Set - O(n)
function removeDupesSet(arr: number[]): number[] {
  return [...new Set(arr)]; // O(n) iterate + O(1) add = O(n)
}

// ============================================
// 6. WHY MAP/SET ARE O(1) - VISUALIZATION
// ============================================

/**
 * HASH TABLE INTERNAL STRUCTURE:
 *
 * Hash Function: key → hash code (number)
 * Bucket Index: hash % buckets.length
 *
 * Example: Map với 8 buckets
 *
 * buckets = [
 *   0: null,
 *   1: Entry('apple', 5) → null,              // No collision
 *   2: Entry('banana', 10) → Entry('blueberry', 12) → null, // Collision!
 *   3: null,
 *   4: Entry('cherry', 8) → null,
 *   5: null,
 *   6: null,
 *   7: null
 * ]
 *
 * GET OPERATION:
 * map.get('banana')
 * 1. hash('banana') = 18
 * 2. bucket_index = 18 % 8 = 2
 * 3. Go to buckets[2]
 * 4. Walk linked list: 'banana' === 'banana' ✓
 * 5. Return value: 10
 * → O(1) average (chain ngắn)
 *
 * SET OPERATION:
 * map.set('grape', 15)
 * 1. hash('grape') = 10
 * 2. bucket_index = 10 % 8 = 2
 * 3. Collision với 'banana' chain
 * 4. Append to chain end
 * → O(1) average
 *
 * COLLISION RESOLUTION:
 * - Chaining: Linked list trong bucket
 * - Open Addressing: Tìm bucket trống kế tiếp
 * - JS engines dùng chaining + resize khi load factor cao
 */

// Minh họa hash collision
class SimpleHashMap<K, V> {
  private buckets: Array<Array<{ key: K; value: V }>> = [];
  private size = 0;

  constructor(capacity = 16) {
    this.buckets = Array(capacity)
      .fill(null)
      .map(() => []);
  }

  private hash(key: K): number {
    const str = String(key);
    let hash = 0;
    for (let i = 0; i < str.length; i++) {
      hash = (hash << 5) - hash + str.charCodeAt(i);
      hash = hash & hash; // Convert to 32-bit integer
    }
    return Math.abs(hash);
  }

  set(key: K, value: V): void {
    const index = this.hash(key) % this.buckets.length;
    const bucket = this.buckets[index];

    // Check if key exists (update)
    for (const entry of bucket) {
      if (entry.key === key) {
        entry.value = value;
        return;
      }
    }

    // New key (append to chain)
    bucket.push({ key, value });
    this.size++;
  }

  get(key: K): V | undefined {
    const index = this.hash(key) % this.buckets.length;
    const bucket = this.buckets[index];

    // Walk chain O(k) where k = chain length (usually small)
    for (const entry of bucket) {
      if (entry.key === key) {
        return entry.value;
      }
    }

    return undefined;
  }

  // Visualize buckets
  visualize(): void {
    this.buckets.forEach((bucket, idx) => {
      if (bucket.length > 0) {
        console.log(
          `Bucket ${idx}:`,
          bucket.map((e) => `${e.key}=${e.value}`).join(' → ')
        );
      }
    });
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

**Best Practices:**

1. **Chọn cấu trúc dữ liệu phù hợp:**

   - Lookup thường xuyên → Map/Object
   - Check existence → Set
   - Ordered collection + iterate → Array
   - Simple config → Object

2. **Performance tips:**

   - Dùng Map thay Array.find() cho lookup nhiều lần
   - Dùng Set.has() thay Array.includes()
   - Avoid unshift/shift trong loop → dùng push + reverse
   - Pre-allocate Array size nếu biết trước: `new Array(1000000)`

3. **Memory consideration:**

   - Map/Set tốn memory hơn (~2x overhead cho hash table)
   - Sparse array tốn memory thừa
   - Object có prototype overhead

4. **Hash collision mitigation:**
   - JS engines tự resize hash table khi load factor cao
   - Good hash function phân bố đều keys
   - Modern engines dùng advanced techniques (Robin Hood hashing, etc.)

**Mistakes:**

```ts
// ❌ Sai: Dùng Array.find() trong loop → O(n²)
const users = [
  /* 1M users */
];
const posts = [
  /* 1M posts */
];
posts.forEach((post) => {
  const author = users.find((u) => u.id === post.authorId); // O(n) mỗi lần
  // Total: O(n²) = 1 triệu * 1 triệu = 1,000 tỷ operations 😱
});

// ✅ Đúng: Build Map trước → O(n)
const userMap = new Map(users.map((u) => [u.id, u])); // O(n)
posts.forEach((post) => {
  const author = userMap.get(post.authorId); // O(1)
  // Total: O(n) = 1 triệu operations ✅
});

// ❌ Sai: Check duplicate bằng includes → O(n²)
const unique: number[] = [];
arr.forEach((item) => {
  if (!unique.includes(item)) {
    // O(n)
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

**Kết Luận:**

- **Map/Set O(1)** nhờ hash table: hash key → direct bucket access
- **Array O(1)** index access nhưng O(n) search/insert/delete
- **Object O(1)** property access, tương tự Map nhưng key string/symbol only
- Chọn đúng data structure → performance tăng exponentially (O(n²) → O(n))

</details>