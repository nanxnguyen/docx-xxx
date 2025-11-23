# 🗂️ Q05: Set/Map, WeakSet/WeakMap, WeakRef & FinalizationRegistry - Collections & Weak References




**⚡ Quick Summary:**
> **Set** = unique values, **Map** = key-value (any type). **Weak** = không prevent GC, keys phải là objects

**💡 Ghi Nhớ:**
- 🎯 **Set**: Array nhưng unique, `.add()`, `.has()`, `.delete()`
- 📦 **Map**: Object nhưng keys có thể là any type (object, function...), maintain insertion order
- 🔥 **WeakSet/WeakMap**: Keys là objects, tự động GC khi không còn reference
- ⚡ **Use Cases**: Set = dedupe, Map = cache, WeakMap = private data

**Trả lời:**

**🎯 Core Concepts:**

- **Set**: Collection của unique values, không có keys, có thể iterate
- **Map**: Collection của key-value pairs, keys có thể là bất kỳ type nào (objects, functions, primitives)
- **WeakSet/WeakMap**: Weak references đến objects, không prevent garbage collection, không iterable
- **WeakRef**: Tạo weak reference đến một object cụ thể, object có thể bị GC bất cứ lúc nào
- **FinalizationRegistry**: Đăng ký callback cleanup khi object được garbage collected

**✅ Ưu điểm:**

- Set/Map: Performance tốt hơn Object cho lookups, iteration, và unique values
- WeakSet/WeakMap: Tự động cleanup, tránh memory leaks
- WeakRef: Cho phép tạo caches mà không prevent GC
- FinalizationRegistry: Cleanup resources (file handles, database connections) khi objects die

**⚠️ Nhược điểm:**

- WeakSet/WeakMap: Không iterable, không có size property, keys phải là objects
- WeakRef: Non-deterministic (không biết khi nào object bị GC), không nên dùng cho core logic
- FinalizationRegistry: Callback có thể chạy muộn hoặc không chạy, không predictable

**Code Example:**

```typescript
// ============================================
// 1. SET - Collection Unique Values
// ============================================
/**
 * Vietnamese Explanation:
 * - Set lưu trữ unique values (không duplicate)
 * - Có thể iterate qua các values
 * - Performance O(1) cho add, delete, has operations
 */
let numberSet: Set<number> = new Set([1, 2, 3, 3, 4]);
console.log(numberSet); // Set(4) {1, 2, 3, 4} - duplicate removed

numberSet.add(5);
numberSet.delete(1);
console.log(numberSet.has(2)); // true
console.log(numberSet.size); // 4

// Iterate Set
for (let value of numberSet) {
  console.log(value); // 2, 3, 4, 5
}

// Use cases cho Set
// 1. Remove duplicates từ array
const numbers = [1, 2, 2, 3, 3, 4, 5, 5];
const uniqueNumbers = [...new Set(numbers)]; // [1, 2, 3, 4, 5]

// 2. Check membership (nhanh hơn array.includes)
const validIds = new Set([1, 5, 10, 15]);
console.log(validIds.has(5)); // true - O(1) time

// 3. Set operations
const setA = new Set([1, 2, 3, 4]);
const setB = new Set([3, 4, 5, 6]);

// Union (hợp)
const union = new Set([...setA, ...setB]); // {1, 2, 3, 4, 5, 6}

// Intersection (giao)
const intersection = new Set([...setA].filter((x) => setB.has(x))); // {3, 4}

// Difference (hiệu)
const difference = new Set([...setA].filter((x) => !setB.has(x))); // {1, 2}

// ============================================
// 2. MAP - Key-Value Pairs với Any Type Keys
// ============================================
/**
 * Vietnamese Explanation:
 * - Map cho phép keys là BẤT KỲ TYPE NÀO (objects, functions, primitives)
 * - Object chỉ cho phép string/symbol keys
 * - Map giữ insertion order
 * - Performance tốt hơn Object cho frequent additions/deletions
 */
let userMap: Map<string, { name: string; age: number }> = new Map();
userMap.set('user1', { name: 'John', age: 25 });
userMap.set('user2', { name: 'Jane', age: 30 });

console.log(userMap.get('user1')); // {name: "John", age: 25}
console.log(userMap.has('user1')); // true
console.log(userMap.size); // 2

// Iterate Map
for (let [key, value] of userMap) {
  console.log(`${key}: ${value.name}`);
}

// Map vs Object - Key Types
let obj: { [key: string]: any } = {};
obj[1] = 'one'; // key becomes STRING "1"
obj[true] = 'true'; // key becomes STRING "true"
console.log(Object.keys(obj)); // ["1", "true"]

let map = new Map();
map.set(1, 'one'); // key is NUMBER 1
map.set(true, 'true'); // key is BOOLEAN true
map.set({ id: 1 }, 'object key'); // key is OBJECT

console.log(map.get(1)); // "one"
console.log(map.get(true)); // "true"

// Use cases cho Map
// 1. Metadata storage với object keys
const metadataMap = new Map<object, { createdAt: Date; author: string }>();
const element = document.querySelector('.btn');
metadataMap.set(element, {
  createdAt: new Date(),
  author: 'John',
});

// 2. Cache với function keys
const memoCache = new Map<Function, any>();
function expensiveOperation(fn: Function) {
  if (memoCache.has(fn)) {
    return memoCache.get(fn);
  }
  const result = fn();
  memoCache.set(fn, result);
  return result;
}

// 3. Counting occurrences
const wordCount = new Map<string, number>();
const words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple'];
words.forEach((word) => {
  wordCount.set(word, (wordCount.get(word) || 0) + 1);
});
console.log(wordCount); // Map { "apple" => 3, "banana" => 2, "cherry" => 1 }

// ============================================
// 3. WEAKSET - Weak References cho Objects
// ============================================
/**
 * Vietnamese Explanation:
 * - WeakSet chỉ chứa objects (không chứa primitives)
 * - Weak reference: không prevent garbage collection
 * - Không iterable, không có size, không có clear()
 * - Use case: Track objects mà không prevent chúng bị GC
 */
let weakSet: WeakSet<object> = new WeakSet();
let obj1: any = { name: 'A' };
let obj2: any = { name: 'B' };

weakSet.add(obj1);
weakSet.add(obj2);
console.log(weakSet.has(obj1)); // true

obj1 = null; // obj1 có thể bị garbage collected ngay
// weakSet KHÔNG prevent obj1 khỏi bị GC

// Use case: Track DOM elements mà không prevent cleanup
class DOMElementTracker {
  private processedElements = new WeakSet<HTMLElement>();

  markAsProcessed(element: HTMLElement): void {
    this.processedElements.add(element);
  }

  isProcessed(element: HTMLElement): boolean {
    return this.processedElements.has(element);
  }

  // Khi element removed khỏi DOM và không còn references,
  // nó sẽ tự động removed khỏi WeakSet qua GC
}

// ============================================
// 4. WEAKMAP - Weak References cho Key-Value Pairs
// ============================================
/**
 * Vietnamese Explanation:
 * - WeakMap keys PHẢI là objects (không phải primitives)
 * - Keys là weak references - không prevent GC
 * - Không iterable, không có size
 * - Use case: Private data, metadata cho objects
 */
let weakMap: WeakMap<object, string> = new WeakMap();
let keyObj: any = { id: 1 };
weakMap.set(keyObj, 'value');
console.log(weakMap.get(keyObj)); // "value"

keyObj = null; // keyObj có thể bị GC, entry tự động removed

// Use case 1: Private properties
const privateData = new WeakMap<object, { password: string }>();

class User {
  constructor(public username: string, password: string) {
    // Store password privately
    privateData.set(this, { password });
  }

  checkPassword(input: string): boolean {
    const data = privateData.get(this);
    return data?.password === input;
  }
}

const user = new User('john', 'secret123');
console.log(user.checkPassword('secret123')); // true
// Không thể access password từ bên ngoài

// Use case 2: Metadata cho DOM elements
const elementMetadata = new WeakMap<HTMLElement, { clicks: number; lastClicked: Date }>();

function trackClicks(element: HTMLElement): void {
  const metadata = elementMetadata.get(element) || { clicks: 0, lastClicked: new Date() };
  metadata.clicks++;
  metadata.lastClicked = new Date();
  elementMetadata.set(element, metadata);
}

// Khi element removed khỏi DOM, metadata tự động cleaned up

// Use case 3: Cache cho object methods
const resultCache = new WeakMap<object, Map<string, any>>();

function memoize(obj: any, methodName: string, fn: Function) {
  if (!resultCache.has(obj)) {
    resultCache.set(obj, new Map());
  }

  const cache = resultCache.get(obj)!;
  const key = JSON.stringify(arguments);

  if (cache.has(key)) {
    return cache.get(key);
  }

  const result = fn();
  cache.set(key, result);
  return result;
}

// ============================================
// 5. WEAKREF - Weak Reference đến Single Object
// ============================================
/**
 * Vietnamese Explanation:
 * - WeakRef cho phép hold weak reference đến một object
 * - Object có thể bị GC bất cứ lúc nào
 * - Dùng deref() để get object (có thể return undefined nếu đã GC)
 * - KHÔNG dùng cho core logic vì non-deterministic
 * - Use case: Caches, observer patterns
 */
let targetObj: any = { x: 1, data: 'important' };
const weakRef = new WeakRef(targetObj);

// Truy cập object qua weak reference
console.log(weakRef.deref()?.x); // 1

// Sau khi remove tất cả strong references
targetObj = null;

// Object có thể bị GC, deref() có thể return undefined
setTimeout(() => {
  const obj = weakRef.deref();
  if (obj) {
    console.log('Object still alive:', obj.x);
  } else {
    console.log('Object was garbage collected');
  }
}, 1000);

// Use case: Image cache với automatic cleanup
class ImageCache {
  private cache = new Map<string, WeakRef<HTMLImageElement>>();

  set(url: string, image: HTMLImageElement): void {
    this.cache.set(url, new WeakRef(image));
  }

  get(url: string): HTMLImageElement | undefined {
    const ref = this.cache.get(url);
    if (!ref) return undefined;

    const image = ref.deref();
    if (!image) {
      // Image was GC'd, cleanup cache entry
      this.cache.delete(url);
      return undefined;
    }

    return image;
  }
}

const imageCache = new ImageCache();

// ============================================
// 6. FINALIZATIONREGISTRY - Cleanup Callback khi Object Dies
// ============================================
/**
 * Vietnamese Explanation:
 * - FinalizationRegistry cho phép đăng ký callback khi object được GC
 * - Callback nhận "held value" (metadata) không phải object itself
 * - KHÔNG reliable - callback có thể chạy muộn hoặc không chạy
 * - Use case: Cleanup external resources (files, connections, timers)
 */
const registry = new FinalizationRegistry<string>((heldValue) => {
  console.log(`Object ${heldValue} was garbage collected`);
  // Cleanup external resources here
  // e.g., close file handles, database connections, etc.
});

let myObj: any = { x: 1 };
// Register object với held value "my-obj"
registry.register(myObj, 'my-obj');

myObj = null; // Object có thể bị GC sau đó
// Callback sẽ chạy: "Object my-obj was garbage collected"

// Use case: Resource cleanup
class FileHandle {
  private static registry = new FinalizationRegistry<number>((fileDescriptor) => {
    console.log(`Closing file descriptor ${fileDescriptor}`);
    // Close actual file handle
    // closeFile(fileDescriptor);
  });

  constructor(private fd: number) {
    // Register for cleanup
    FileHandle.registry.register(this, fd);
  }

  read(): string {
    // Read file using this.fd
    return 'file content';
  }
}

// Use case: Database connection pool
class DatabaseConnection {
  private static registry = new FinalizationRegistry<string>((connectionId) => {
    console.log(`Cleanup connection ${connectionId}`);
    // Return connection to pool or close it
  });

  constructor(private id: string) {
    DatabaseConnection.registry.register(this, id);
  }
}

// Use case: Timer cleanup
const timerRegistry = new FinalizationRegistry<number>((timerId) => {
  console.log(`Clearing timer ${timerId}`);
  clearInterval(timerId);
});

class AutoTimer {
  private timerId: number;

  constructor(callback: () => void, interval: number) {
    this.timerId = window.setInterval(callback, interval);
    timerRegistry.register(this, this.timerId);
  }
}

// ============================================
// 7. PRACTICAL COMPARISON - When to Use What
// ============================================
/**
 * Vietnamese Explanation:
 * 
 * Use SET when:
 * - Cần unique values
 * - Cần check membership nhanh (O(1))
 * - Cần set operations (union, intersection)
 * 
 * Use MAP when:
 * - Cần key-value pairs với non-string keys
 * - Cần preserve insertion order
 * - Frequent additions/deletions
 * 
 * Use WEAKSET when:
 * - Track objects mà không prevent GC
 * - Mark/tag objects temporarily
 * 
 * Use WEAKMAP when:
 * - Private data cho objects
 * - Metadata/cache cho objects
 * - Automatic cleanup when objects die
 * 
 * Use WEAKREF when:
 * - Caches có thể expire
 * - Observer patterns
 * - Không cần guarantee object availability
 * 
 * Use FINALIZATIONREGISTRY when:
 * - Cleanup external resources
 * - Close file handles, connections
 * - NOT for critical logic (unreliable timing)
 */

// Performance comparison
console.time('Set operations');
const set = new Set();
for (let i = 0; i < 100000; i++) {
  set.add(i);
}
console.timeEnd('Set operations'); // ~5ms

console.time('Object operations');
const obj = {};
for (let i = 0; i < 100000; i++) {
  obj[i] = true;
}
console.timeEnd('Object operations'); // ~8ms

console.time('Map operations');
const map = new Map();
for (let i = 0; i < 100000; i++) {
  map.set(i, true);
}
console.timeEnd('Map operations'); // ~6ms
```

**🎯 Best Practices:**

1. **Set**: Sử dụng cho unique values, remove duplicates, membership checks
2. **Map**: Sử dụng cho key-value pairs với non-string keys, preserve insertion order
3. **WeakSet**: Track objects temporarily mà không prevent GC (DOM elements, event handlers)
4. **WeakMap**: Private properties, metadata, caches for objects
5. **WeakRef**: Soft caches mà không prevent GC, luôn có fallback khi deref() returns undefined
6. **FinalizationRegistry**: Cleanup external resources (files, connections), KHÔNG dùng cho critical logic
7. **Map vs Object**: Prefer Map khi cần frequent additions/deletions hoặc non-string keys
8. **WeakMap for Privacy**: Use WeakMap để implement private properties trong classes

**⚠️ Common Mistakes:**

```typescript
// ❌ Sai: Sử dụng Object cho unique values
let uniqueValues: { [key: string]: boolean } = {};
uniqueValues['a'] = true;
uniqueValues['b'] = true;
uniqueValues['a'] = true; // Duplicate, nhưng không bị detect
console.log(Object.keys(uniqueValues).length); // 2 (phải manually check)

// ✅ Đúng: Sử dụng Set
let uniqueValues2 = new Set(['a', 'b', 'a']); // Set(2) {"a", "b"}
console.log(uniqueValues2.size); // 2 (automatic)

// ❌ Sai: WeakSet với primitives
const weakSet = new WeakSet();
// weakSet.add('string'); // TypeError: Invalid value used in weak set

// ✅ Đúng: WeakSet chỉ với objects
const weakSet2 = new WeakSet();
weakSet2.add({ id: 1 }); // OK

// ❌ Sai: Iterate WeakMap
const weakMap = new WeakMap();
// for (let [key, value] of weakMap) { } // TypeError: weakMap is not iterable

// ✅ Đúng: WeakMap không iterable, chỉ get/set/has/delete
weakMap.get(someKey);

// ❌ Sai: Dựa vào WeakRef cho critical logic
function getCachedData(key: string) {
  const ref = cache.get(key);
  return ref.deref().data; // Error nếu object đã GC!
}

// ✅ Đúng: Always check deref() result
function getCachedData2(key: string) {
  const ref = cache.get(key);
  const obj = ref?.deref();
  if (obj) {
    return obj.data;
  }
  // Fallback: fetch fresh data
  return fetchData(key);
}

// ❌ Sai: Expect FinalizationRegistry callback chạy ngay
registry.register(obj, 'data');
obj = null;
// Callback KHÔNG chạy ngay lập tức!

// ✅ Đúng: FinalizationRegistry cho optional cleanup only
// Không rely on timing, có backup cleanup mechanism
```

**📊 Performance & Memory Considerations:**

- **Set/Map**: ~2-3x faster than Object cho frequent lookups/additions/deletions
- **WeakSet/WeakMap**: Nhỏ hơn về memory vì automatic cleanup
- **WeakRef**: Minimal memory overhead, nhưng có CPU cost cho deref() checks
- **FinalizationRegistry**: Minimal overhead, callback chạy async trong idle time

