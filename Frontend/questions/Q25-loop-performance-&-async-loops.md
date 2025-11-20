# 🔁 Q25: Loop Performance & Async Loops




**⚡ Quick Summary:**
> for loop = fastest. forEach = readable. map/filter = functional. Async loops = Promise.all hoặc for await

**💡 Ghi Nhớ:**
- ⚡ **Performance**: for > for...of > forEach > map
- 🔄 **Async**: Dùng `for await...of` hoặc `Promise.all()`
- ⚠️ **Trap**: forEach không work với async/await!

**Trả lời:**

Có nhiều cách để loop qua array/object trong JavaScript, mỗi cách có performance và behavior khác nhau:

**🔄 Các loại Loops & Performance:**

1. **`for` loop** - Nhanh nhất ⚡

   - Performance: ⭐⭐⭐⭐⭐ (fastest)
   - Control: Full control (break, continue)
   - Use case: Performance-critical code, large arrays

2. **`for...of`** - Modern, readable 📖

   - Performance: ⭐⭐⭐⭐ (slower than for, faster than forEach)
   - Control: Support break, continue
   - Use case: Readable code, iterables (Array, Set, Map, String)

3. **`forEach`** - Functional style 🎨

   - Performance: ⭐⭐⭐ (slowest - function call overhead)
   - Control: KHÔNG support break, continue
   - Use case: Functional programming, side effects

4. **`for...in`** - Cho objects 🔑

   - Performance: ⭐⭐ (slow - prototype chain lookup)
   - Control: Support break, continue
   - Use case: Iterate object keys (KHÔNG nên dùng cho arrays)

5. **`map/filter/reduce`** - Functional transformations 🔄
   - Performance: ⭐⭐⭐ (similar to forEach)
   - Control: KHÔNG support break (phải loop hết array)
   - Use case: Transform data, create new arrays

**⚠️ QUAN TRỌNG: Async/Await trong Loops**

**Sequential vs Parallel execution:**

- **Sequential**: Chờ từng promise xong mới chạy tiếp (slow but controlled)
- **Parallel**: Chạy tất cả promises cùng lúc (fast but less control)

**Hoạt động:**

```
┌────────────────────────────────────────────────────────┐
│           LOOP PERFORMANCE COMPARISON                  │
├────────────────────────────────────────────────────────┤
│                                                        │
│  Synchronous Performance (1M items):                  │
│  ┌──────────────────────────────────────┐             │
│  │  for loop:        ~2ms   ⚡⚡⚡⚡⚡    │             │
│  │  for...of:        ~5ms   ⚡⚡⚡⚡      │             │
│  │  forEach:         ~8ms   ⚡⚡⚡        │             │
│  │  map:            ~10ms   ⚡⚡⚡        │             │
│  │  for...in:       ~50ms   ⚡          │             │
│  └──────────────────────────────────────┘             │
│                                                        │
│  Async Execution (3 items, 1s delay each):           │
│  ┌──────────────────────────────────────┐             │
│  │  Sequential (for/for...of): ~3s      │             │
│  │  ├─ Item 1: 1s ━━━━━━━━━━┐          │             │
│  │  ├─ Item 2: 1s           ━━━━━━━━━━┐│             │
│  │  └─ Item 3: 1s                     ━━│             │
│  │                                                    │             │
│  │  Parallel (Promise.all):   ~1s       │             │
│  │  ├─ Item 1: 1s ━━━━━━━━━━┐          │             │
│  │  ├─ Item 2: 1s ━━━━━━━━━━┤          │             │
│  │  └─ Item 3: 1s ━━━━━━━━━━┘          │             │
│  └──────────────────────────────────────┘             │
└────────────────────────────────────────────────────────┘
```

**Ưu điểm:**

- ✅ **for loop**: Nhanh nhất, full control (break/continue), cache length
- ✅ **for...of**: Modern, readable, support break/continue, work với iterables
- ✅ **forEach**: Functional style, chain methods, readable
- ✅ **Async for...of**: Sequential execution, dễ control
- ✅ **Promise.all**: Parallel execution, nhanh nhất cho async

**Nhược điểm:**

- ❌ **for loop**: Verbose, dễ lỗi (index out of bounds)
- ❌ **for...of**: Chậm hơn for loop ~2-3x
- ❌ **forEach**: Chậm nhất, KHÔNG support break/continue, KHÔNG support async/await
- ❌ **for...in**: RẤT chậm, iterate prototype chain, KHÔNG nên dùng cho arrays
- ❌ **Async sequential**: Chậm (chờ từng promise), không tận dụng concurrency

**Chú thích:**

**🔄 Loop Control Keywords:**

- **`break`**: Thoát loop ngay lập tức
- **`continue`**: Skip iteration hiện tại, tiếp tục iteration tiếp theo
- **`return`**: Thoát function (KHÔNG chỉ loop)

**⚡ Performance Tips:**

- Cache array length: `const len = arr.length` → tránh re-calculate mỗi iteration
- Avoid nested loops: O(n²) → rất chậm với large arrays
- Use `for` loop cho performance-critical code (>10K items)
- Use `for...of` cho readable code (trade-off: ~2-3x slower)

**🔁 Async/Await Behavior:**

- `for`/`for...of`: Support `await` → **sequential** execution
- `forEach`: KHÔNG support `await` đúng cách → callbacks chạy **parallel** nhưng không đợi
- `map` + `Promise.all`: Best practice cho **parallel** async operations
- `for await...of`: Dành cho **async iterables** (streams, generators)

**Code Example (TypeScript):**

```typescript
// ============================================
// 1. SYNCHRONOUS LOOPS - Performance Comparison
// ============================================

const numbers = [1, 2, 3, 4, 5];

// 🚀 A. for loop - FASTEST (traditional)
console.time('for loop');
for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
}
console.timeEnd('for loop'); // ~0.1ms

// 🚀 B. for loop - OPTIMIZED (cache length)
console.time('for loop optimized');
const len = numbers.length; // ✅ Cache length
for (let i = 0; i < len; i++) {
  console.log(numbers[i]);
}
console.timeEnd('for loop optimized'); // ~0.08ms (faster)

// 📖 C. for...of - MODERN & READABLE
console.time('for...of');
for (const number of numbers) {
  console.log(number);
  // ✅ Support break, continue
  if (number === 3) break;
}
console.timeEnd('for...of'); // ~0.2ms (2x slower than for)

// 🎨 D. forEach - FUNCTIONAL STYLE
console.time('forEach');
numbers.forEach((number, index) => {
  console.log(number);
  // ❌ CANNOT use break or continue!
  // if (number === 3) break; // ❌ SyntaxError
});
console.timeEnd('forEach'); // ~0.3ms (slowest)

// 🔑 E. for...in - FOR OBJECTS (KHÔNG nên dùng cho arrays!)
const obj = { a: 1, b: 2, c: 3 };
console.time('for...in');
for (const key in obj) {
  if (obj.hasOwnProperty(key)) {
    // ✅ Check own properties
    console.log(key, obj[key]);
  }
}
console.timeEnd('for...in'); // ~0.5ms (rất chậm với arrays)

// ❌ BAD: for...in với array
const arr = [1, 2, 3];
for (const index in arr) {
  console.log(index); // '0', '1', '2' (STRING, không phải number!)
}

// 🔄 F. map/filter/reduce - FUNCTIONAL TRANSFORMATIONS
console.time('map');
const doubled = numbers.map((n) => n * 2); // [2, 4, 6, 8, 10]
console.timeEnd('map'); // ~0.3ms

const evens = numbers.filter((n) => n % 2 === 0); // [2, 4]
const sum = numbers.reduce((acc, n) => acc + n, 0); // 15

// ============================================
// 2. PERFORMANCE TEST - Large Arrays
// ============================================

function performanceTest(): void {
  const largeArray = Array.from({ length: 1_000_000 }, (_, i) => i);
  let result = 0;

  // 🚀 for loop - FASTEST
  console.time('for loop (1M items)');
  const len = largeArray.length;
  for (let i = 0; i < len; i++) {
    result += largeArray[i];
  }
  console.timeEnd('for loop (1M items)'); // ~2ms

  // 📖 for...of
  result = 0;
  console.time('for...of (1M items)');
  for (const item of largeArray) {
    result += item;
  }
  console.timeEnd('for...of (1M items)'); // ~5ms (2.5x slower)

  // 🎨 forEach
  result = 0;
  console.time('forEach (1M items)');
  largeArray.forEach((item) => {
    result += item;
  });
  console.timeEnd('forEach (1M items)'); // ~8ms (4x slower)

  // 🔄 reduce
  console.time('reduce (1M items)');
  result = largeArray.reduce((acc, item) => acc + item, 0);
  console.timeEnd('reduce (1M items)'); // ~10ms (5x slower)

  console.log('Result:', result);
}

performanceTest();

// ============================================
// 3. ASYNC/AWAIT trong LOOPS - QUAN TRỌNG! ⚠️
// ============================================

// Mock API call (1 giây delay)
async function fetchUserData(userId: number): Promise<string> {
  console.log(`🚀 Bắt đầu fetch user ${userId}...`);
  await new Promise((resolve) => setTimeout(resolve, 1000)); // 1s delay
  console.log(`✅ Hoàn thành fetch user ${userId}`);
  return `User ${userId} data`;
}

const userIds = [1, 2, 3];

// ❌ BAD: forEach với async/await - KHÔNG HOẠT ĐỘNG ĐÚNG!
async function badForEach() {
  console.log('❌ BAD: forEach với async/await');
  console.time('forEach async');

  userIds.forEach(async (id) => {
    const data = await fetchUserData(id); // ❌ await bị IGNORE!
    console.log(data);
  });

  console.timeEnd('forEach async'); // ~0ms (KHÔNG đợi promises!)
  console.log('forEach done (nhưng chưa fetch xong!)');

  // 🚨 Vấn đề:
  // - forEach KHÔNG đợi async callbacks
  // - Tất cả promises chạy parallel nhưng không control được
  // - console.log 'done' chạy TRƯỚC khi fetch xong
}

// ✅ GOOD: for...of với async/await - SEQUENTIAL (Tuần tự)
async function goodSequential() {
  console.log('✅ GOOD: for...of - Sequential execution');
  console.time('for...of sequential');

  for (const id of userIds) {
    const data = await fetchUserData(id); // ✅ Đợi từng promise xong
    console.log(data);
  }

  console.timeEnd('for...of sequential'); // ~3s (1s × 3)
  console.log('Sequential done!');

  // ✅ Hoạt động:
  // 1s: Fetch user 1 → đợi xong
  // 1s: Fetch user 2 → đợi xong
  // 1s: Fetch user 3 → đợi xong
  // Total: 3s
}

// ✅ BETTER: Promise.all - PARALLEL (Song song)
async function goodParallel() {
  console.log('✅ BETTER: Promise.all - Parallel execution');
  console.time('Promise.all parallel');

  const promises = userIds.map((id) => fetchUserData(id));
  const results = await Promise.all(promises); // ✅ Chạy song song

  results.forEach((data) => console.log(data));

  console.timeEnd('Promise.all parallel'); // ~1s (3 requests cùng lúc!)
  console.log('Parallel done!');

  // ✅ Hoạt động:
  // 0s: Khởi tạo 3 promises cùng lúc
  // 1s: Cả 3 promises resolve cùng lúc
  // Total: 1s (NHANH GẤP 3 LẦN!)
}

// ✅ ADVANCED: for...of với batch processing
async function goodBatch() {
  console.log('✅ ADVANCED: Batch processing');
  console.time('Batch processing');

  const batchSize = 2; // Chạy 2 requests cùng lúc

  for (let i = 0; i < userIds.length; i += batchSize) {
    const batch = userIds.slice(i, i + batchSize);
    const promises = batch.map((id) => fetchUserData(id));
    const results = await Promise.all(promises); // Đợi batch xong

    results.forEach((data) => console.log(data));
  }

  console.timeEnd('Batch processing'); // ~2s
  console.log('Batch done!');

  // ✅ Hoạt động:
  // Batch 1 (users 1, 2): 1s parallel
  // Batch 2 (user 3):      1s
  // Total: 2s (balance giữa speed & control)
}

// ============================================
// 4. ASYNC LOOPS - Real-world Trading Example
// ============================================

interface Order {
  id: number;
  symbol: string;
  quantity: number;
}

// Mock API: Submit order to exchange
async function submitOrder(order: Order): Promise<string> {
  console.log(`📤 Submitting order ${order.id}: ${order.symbol}...`);
  await new Promise((resolve) => setTimeout(resolve, 500)); // 500ms delay
  return `Order ${order.id} confirmed`;
}

const orders: Order[] = [
  { id: 1, symbol: 'AAPL', quantity: 100 },
  { id: 2, symbol: 'GOOGL', quantity: 50 },
  { id: 3, symbol: 'MSFT', quantity: 75 },
];

// ❌ SCENARIO 1: Sequential (chậm nhưng an toàn)
async function submitOrdersSequential() {
  console.log('📊 Submitting orders SEQUENTIALLY...');
  console.time('Sequential orders');

  for (const order of orders) {
    const result = await submitOrder(order); // Đợi từng order
    console.log(`✅ ${result}`);

    // ✅ Có thể handle errors từng order:
    // if (error) continue; // Skip order lỗi, chạy tiếp
  }

  console.timeEnd('Sequential orders'); // ~1.5s (500ms × 3)

  // 💡 Use case:
  // - Orders phụ thuộc nhau (order 2 cần order 1 xong)
  // - Rate limiting (không gửi quá nhiều requests)
  // - Error handling riêng từng order
}

// ✅ SCENARIO 2: Parallel (nhanh nhưng rủi ro)
async function submitOrdersParallel() {
  console.log('🚀 Submitting orders PARALLEL...');
  console.time('Parallel orders');

  const promises = orders.map((order) => submitOrder(order));
  const results = await Promise.all(promises); // Tất cả cùng lúc

  results.forEach((result) => console.log(`✅ ${result}`));

  console.timeEnd('Parallel orders'); // ~500ms (tất cả cùng lúc!)

  // 💡 Use case:
  // - Orders độc lập (không phụ thuộc nhau)
  // - Muốn nhanh nhất
  // - Exchange support concurrent requests

  // ⚠️ Rủi ro:
  // - 1 order lỗi → Promise.all reject (tất cả fail)
  // - Có thể vượt rate limit
}

// ✅ SCENARIO 3: Parallel with error handling
async function submitOrdersParallelSafe() {
  console.log('🛡️ Submitting orders PARALLEL (safe)...');
  console.time('Parallel safe orders');

  const promises = orders.map(async (order) => {
    try {
      const result = await submitOrder(order);
      return { status: 'fulfilled', value: result };
    } catch (error) {
      return { status: 'rejected', reason: error };
    }
  });

  const results = await Promise.all(promises);

  results.forEach((result, index) => {
    if (result.status === 'fulfilled') {
      console.log(`✅ ${result.value}`);
    } else {
      console.log(`❌ Order ${orders[index].id} failed:`, result.reason);
    }
  });

  console.timeEnd('Parallel safe orders');

  // ✅ Lợi ích:
  // - Nhanh (parallel)
  // - 1 order lỗi KHÔNG ảnh hưởng orders khác
  // - Handle errors riêng từng order
}

// Alternative: Promise.allSettled
async function submitOrdersAllSettled() {
  console.log('✨ Using Promise.allSettled...');
  console.time('allSettled orders');

  const promises = orders.map((order) => submitOrder(order));
  const results = await Promise.allSettled(promises); // ✅ KHÔNG reject khi có lỗi

  results.forEach((result, index) => {
    if (result.status === 'fulfilled') {
      console.log(`✅ ${result.value}`);
    } else {
      console.log(`❌ Order ${orders[index].id} failed:`, result.reason);
    }
  });

  console.timeEnd('allSettled orders');
}

// ============================================
// 5. LOOP CONTROL - break, continue, return
// ============================================

function loopControl() {
  const numbers = [1, 2, 3, 4, 5];

  // ✅ break: Thoát loop ngay lập tức
  console.log('--- break example ---');
  for (const num of numbers) {
    if (num === 3) break; // Dừng khi gặp 3
    console.log(num); // 1, 2
  }

  // ✅ continue: Skip iteration hiện tại
  console.log('--- continue example ---');
  for (const num of numbers) {
    if (num === 3) continue; // Skip 3
    console.log(num); // 1, 2, 4, 5
  }

  // ✅ return: Thoát function (KHÔNG chỉ loop!)
  console.log('--- return example ---');
  function findNumber(target: number): string {
    for (const num of numbers) {
      if (num === target) {
        return `Found ${target}`; // Thoát function
      }
    }
    return 'Not found';
  }
  console.log(findNumber(3)); // 'Found 3'

  // ❌ forEach: CANNOT use break/continue/return
  console.log('--- forEach (no control) ---');
  numbers.forEach((num) => {
    // if (num === 3) break;    // ❌ SyntaxError
    // if (num === 3) continue; // ❌ SyntaxError
    if (num === 3) return; // ✅ OK nhưng chỉ skip iteration này (như continue)
    console.log(num); // 1, 2, 4, 5
  });
}

loopControl();
```

---

**Best Practices:**

1. **Chọn Loop Type đúng Use Case**

   ```typescript
   // ⚡ Performance-critical (>100K items)
   for (let i = 0; i < arr.length; i++) {}

   // 📖 Readable code (<100K items)
   for (const item of arr) {
   }

   // 🎨 Functional transformations
   const doubled = arr.map((x) => x * 2);

   // 🔑 Objects only
   for (const key in obj) {
   }
   ```

2. **Cache Array Length**

   ```typescript
   // ❌ BAD: Re-calculate length mỗi iteration
   for (let i = 0; i < arr.length; i++) {}

   // ✅ GOOD: Cache length
   const len = arr.length;
   for (let i = 0; i < len; i++) {}
   ```

3. **Async/Await đúng cách**

   ```typescript
   // ❌ NEVER use forEach với async/await
   arr.forEach(async (item) => {
     await doSomething(item); // KHÔNG đợi!
   });

   // ✅ Sequential: for...of + await
   for (const item of arr) {
     await doSomething(item); // Đợi từng cái
   }

   // ✅ Parallel: Promise.all
   await Promise.all(arr.map((item) => doSomething(item)));
   ```

4. **Avoid Nested Loops (O(n²))**

   ```typescript
   // ❌ BAD: O(n²) - RẤT CHẬM
   for (const item1 of arr1) {
     for (const item2 of arr2) {
       // ...
     }
   }

   // ✅ GOOD: Use Map/Set O(n)
   const map = new Map(arr2.map((item) => [item.id, item]));
   for (const item1 of arr1) {
     const item2 = map.get(item1.id); // O(1) lookup
   }
   ```

5. **Error Handling trong Async Loops**

   ```typescript
   // ✅ Sequential: try/catch từng operation
   for (const item of items) {
     try {
       await process(item);
     } catch (error) {
       console.error(`Failed to process ${item}:`, error);
       continue; // Skip lỗi, chạy tiếp
     }
   }

   // ✅ Parallel: Promise.allSettled
   const results = await Promise.allSettled(items.map((item) => process(item)));
   ```

---

**Common Mistakes:**

1. **❌ forEach với async/await**

   ```typescript
   // ❌ BAD: await bị IGNORE!
   items.forEach(async (item) => {
     await fetchData(item); // KHÔNG đợi!
   });
   console.log('Done'); // Chạy TRƯỚC khi fetch xong!

   // ✅ GOOD: Dùng for...of
   for (const item of items) {
     await fetchData(item); // Đợi đúng
   }
   ```

2. **❌ for...in với Arrays**

   ```typescript
   // ❌ BAD: index là STRING, iterate prototype
   const arr = [1, 2, 3];
   for (const index in arr) {
     console.log(typeof index); // 'string'!
   }

   // ✅ GOOD: Dùng for...of
   for (const value of arr) {
     console.log(value); // 1, 2, 3
   }
   ```

3. **❌ Không Cache Length**

   ```typescript
   // ❌ BAD: arr.length tính lại mỗi iteration
   for (let i = 0; i < arr.length; i++) {}

   // ✅ GOOD: Cache length
   const len = arr.length;
   for (let i = 0; i < len; i++) {}
   ```

4. **❌ Nested Loops O(n²)**

   ```typescript
   // ❌ BAD: 1000 × 1000 = 1,000,000 iterations!
   for (const user of users) {
     // 1000 users
     for (const order of orders) {
       // 1000 orders
       if (order.userId === user.id) {
       }
     }
   }

   // ✅ GOOD: O(n) với Map
   const ordersByUser = new Map();
   orders.forEach((order) => {
     if (!ordersByUser.has(order.userId)) {
       ordersByUser.set(order.userId, []);
     }
     ordersByUser.get(order.userId).push(order);
   });

   users.forEach((user) => {
     const userOrders = ordersByUser.get(user.id); // O(1)
   });
   ```

5. **❌ Promise.all mà không handle errors**

   ```typescript
   // ❌ BAD: 1 promise fail → TẤT CẢ fail
   await Promise.all(items.map((item) => fetchData(item)));

   // ✅ GOOD: Dùng Promise.allSettled
   const results = await Promise.allSettled(
     items.map((item) => fetchData(item))
   );

   results.forEach((result, i) => {
     if (result.status === 'rejected') {
       console.error(`Item ${i} failed:`, result.reason);
     }
   });
   ```

---
