# 🧹 Q31: Memory Management, Garbage Collection & Memory Leaks




**⚡ Quick Summary:**
> JavaScript tự động quản lý memory qua GC (Mark & Sweep). Memory leaks xảy ra khi references không được cleanup: event listeners, timers, closures, DOM refs, global vars

**💡 Ghi Nhớ:**
- 🎯 **GC Algorithm**: Mark & Sweep - đánh dấu objects còn dùng, xóa objects không dùng
- 🚨 **Top 5 Memory Leaks**: Event listeners, Timers, Closures, DOM refs, Global vars
- ✅ **Prevention**: Cleanup listeners, clear timers, remove refs, use WeakMap/WeakSet
- 🔍 **Detection**: Chrome DevTools → Memory → Heap snapshot

---

## 📚 PART 1: MEMORY MANAGEMENT & GARBAGE COLLECTION

### **1.1. Cách JavaScript Quản Lý Memory**

```typescript
// ═══════════════════════════════════════════════════════
// MEMORY LIFECYCLE (Vòng đời bộ nhớ)
// ═══════════════════════════════════════════════════════

// BƯỚC 1: ALLOCATION (Cấp phát)
let user = { name: 'John', age: 30 };
// → JS tự động cấp phát memory cho object

// BƯỚC 2: USAGE (Sử dụng)
console.log(user.name); // Đọc/ghi memory

// BƯỚC 3: RELEASE (Giải phóng)
user = null; // Xóa reference
// → GC sẽ tự động thu hồi memory (không cần manual free như C/C++)

/**
 * 🧠 GARBAGE COLLECTION (GC) - Thu Gom Rác
 * 
 * JavaScript dùng thuật toán "Mark and Sweep":
 * 
 * 1. MARK (Đánh dấu):
 *    - Bắt đầu từ "roots" (global vars, stack)
 *    - Duyệt tất cả objects có thể reach được
 *    - Đánh dấu chúng là "còn dùng"
 * 
 * 2. SWEEP (Quét):
 *    - Duyệt toàn bộ heap
 *    - Thu hồi objects KHÔNG được đánh dấu
 *    - Giải phóng memory
 * 
 * ⏱️ TIMING: GC chạy tự động, không dự đoán được
 * 🎯 GOAL: Giải phóng memory không còn dùng
 */
```

### **1.2. Heap Memory vs Stack Memory**

```typescript
// ═══════════════════════════════════════════════════════
// STACK (LIFO - Last In First Out)
// ═══════════════════════════════════════════════════════
function calculate() {
  let a = 10;      // Stack: primitive value
  let b = 20;      // Stack: primitive value
  let sum = a + b; // Stack: primitive value
  return sum;
}
// → Khi function return, stack tự động cleared
// → NHANH, kích thước CỐ ĐỊNH

// ═══════════════════════════════════════════════════════
// HEAP (Dynamic memory)
// ═══════════════════════════════════════════════════════
function createUser() {
  let user = { name: 'John' }; // Heap: object
  let posts = [1, 2, 3];       // Heap: array
  return { user, posts };
}
// → Objects/Arrays được lưu trong HEAP
// → Stack chỉ chứa REFERENCE (pointer) đến heap
// → CHẬM hơn stack, kích thước ĐỘNG

/**
 * 📊 So sánh:
 * 
 * STACK:
 * ├─ Lưu: Primitives (number, string, boolean, null, undefined)
 * ├─ Lưu: Function calls, local variables
 * ├─ Tốc độ: ⚡⚡⚡⚡⚡ (rất nhanh)
 * ├─ Kích thước: ~1MB (cố định, nhỏ)
 * └─ Cleanup: Tự động khi function return
 * 
 * HEAP:
 * ├─ Lưu: Objects, Arrays, Functions
 * ├─ Lưu: Dynamic data structures
 * ├─ Tốc độ: ⚡⚡⚡ (chậm hơn stack)
 * ├─ Kích thước: ~2GB (động, lớn)
 * └─ Cleanup: Garbage Collection (GC)
 */
```

### **1.3. Weak References (WeakMap, WeakSet)**

```typescript
// ═══════════════════════════════════════════════════════
// NORMAL MAP/SET (Strong References)
// ═══════════════════════════════════════════════════════
const normalMap = new Map();
const normalSet = new Set();

let obj1 = { data: 'important' };

normalMap.set(obj1, 'metadata');
normalSet.add(obj1);

obj1 = null; // ❌ Object KHÔNG được GC!
// Vì normalMap và normalSet vẫn giữ reference

// ═══════════════════════════════════════════════════════
// WEAK MAP/SET (Weak References)
// ═══════════════════════════════════════════════════════
const weakMap = new WeakMap();
const weakSet = new WeakSet();

let obj2 = { data: 'important' };

weakMap.set(obj2, 'metadata');
weakSet.add(obj2);

obj2 = null; // ✅ Object được GC ngay!
// WeakMap/WeakSet KHÔNG ngăn GC
// Entries tự động bị xóa khi object được GC

/**
 * 💡 WHEN TO USE:
 * 
 * ✅ WeakMap/WeakSet:
 * - Cache/memoization (tránh memory leaks)
 * - Private data for objects
 * - DOM element metadata
 * 
 * ❌ Normal Map/Set:
 * - Cần iterate over entries
 * - Cần keys là primitives (string, number)
 * - Cần size property
 */

// Example: Cache với WeakMap
const cache = new WeakMap();

function expensiveOperation(obj: object) {
  if (cache.has(obj)) {
    return cache.get(obj); // Cache hit
  }
  
  const result = { /* expensive computation */ };
  cache.set(obj, result); // Cache miss
  return result;
}

// Khi obj được GC → cache entry tự động bị xóa ✅
```

---

## 🚨 PART 2: MEMORY LEAKS - 10 TRƯỜNG HỢP PHỔ BIẾN

### **2.1. Event Listeners Không Cleanup** ⭐⭐⭐⭐⭐

```typescript
// ❌ MEMORY LEAK
class BadComponent {
  private element: HTMLElement;
  
  constructor() {
    this.element = document.createElement('div');
    
    // Leak: Bind tạo new function mỗi lần → không remove được
    this.element.addEventListener('click', this.handleClick.bind(this));
  }
  
  private handleClick() {
    console.log('Clicked');
  }
  
  // destroy() không remove được listener vì bind() tạo function mới!
}

// ✅ FIXED
class GoodComponent {
  private element: HTMLElement;
  private boundHandler: EventListener;
  
  constructor() {
    this.element = document.createElement('div');
    this.boundHandler = this.handleClick.bind(this); // Lưu reference
    this.element.addEventListener('click', this.boundHandler);
  }
  
  private handleClick() {
    console.log('Clicked');
  }
  
  destroy() {
    this.element.removeEventListener('click', this.boundHandler); // ✅ Remove được
    this.element.remove();
  }
}

/**
 * 🔥 TẠI SAO LEAK?
 * 
 * Event listener giữ reference đến:
 * ├─ Element (DOM node)
 * ├─ Handler function
 * └─ Closure scope (this, outer variables)
 * 
 * Nếu không removeEventListener():
 * → Element không được GC (vì listener giữ ref)
 * → Handler function không được GC
 * → Toàn bộ closure scope không được GC
 * 
 * 💡 SOLUTION:
 * 1. Lưu bound function vào variable
 * 2. removeEventListener() trong cleanup
 * 3. Hoặc dùng AbortController (modern)
 */

// ✅ Modern way: AbortController
class ModernComponent {
  private element: HTMLElement;
  private abortController = new AbortController();
  
  constructor() {
    this.element = document.createElement('div');
    
    this.element.addEventListener('click', this.handleClick, {
      signal: this.abortController.signal // ✅ Auto cleanup
    });
  }
  
  private handleClick = () => {
    console.log('Clicked');
  }
  
  destroy() {
    this.abortController.abort(); // ✅ Remove tất cả listeners cùng lúc
    this.element.remove();
  }
}
```

### **2.2. Timers Không Clear** ⭐⭐⭐⭐⭐

```typescript
// ❌ MEMORY LEAK
class BadTimer {
  private data = new Array(100000).fill('data');
  
  constructor() {
    setInterval(() => {
      console.log(this.data.length); // Closure giữ ref đến this.data
    }, 1000);
    
    // ❌ Interval chạy mãi, giữ reference đến BadTimer instance
  }
}

// ✅ FIXED
class GoodTimer {
  private data = new Array(100000).fill('data');
  private intervalId: number | null = null;
  
  constructor() {
    this.intervalId = setInterval(() => {
      console.log(this.data.length);
    }, 1000);
  }
  
  destroy() {
    if (this.intervalId !== null) {
      clearInterval(this.intervalId); // ✅ Clear timer
      this.intervalId = null;
    }
  }
}

/**
 * 🔥 CÁC LOẠI TIMERS CẦN CLEANUP:
 * 
 * 1. setInterval() - chạy lặp lại
 * 2. setTimeout() - chạy 1 lần (nhưng vẫn cần clear nếu unmount sớm)
 * 3. requestAnimationFrame() - animation loop
 * 4. requestIdleCallback() - idle time tasks
 */

// Example: React Hook cleanup
function useInterval(callback: () => void, delay: number) {
  useEffect(() => {
    const id = setInterval(callback, delay);
    return () => clearInterval(id); // ✅ Cleanup
  }, [callback, delay]);
}
```

### **2.3. Closures Giữ Large Data** ⭐⭐⭐⭐

```typescript
// ❌ MEMORY LEAK
function createLeak() {
  const largeData = new Array(1000000).fill('data'); // 8MB
  
  return function smallFunction() {
    console.log('Hello'); // Không dùng largeData
  };
  
  // ❌ Closure vẫn giữ reference đến largeData!
  // Mặc dù không dùng, nhưng largeData nằm trong scope
}

const fn = createLeak();
// → largeData (8MB) không được GC!

// ✅ FIXED 1: Nullify unused variables
function createFixed1() {
  let largeData: any[] | null = new Array(1000000).fill('data');
  
  // Process data here...
  const result = largeData.length;
  
  largeData = null; // ✅ Clear reference
  
  return function smallFunction() {
    console.log(result); // Chỉ giữ result, không giữ largeData
  };
}

// ✅ FIXED 2: Separate scopes
function createFixed2() {
  let result: number;
  
  {
    const largeData = new Array(1000000).fill('data');
    result = largeData.length;
    // largeData out of scope here
  }
  
  return function smallFunction() {
    console.log(result);
  };
}

/**
 * 🔥 TẠI SAO CLOSURE GIỮ MEMORY?
 * 
 * Closure = Function + Lexical Environment (scope chain)
 * 
 * function outer() {
 *   const data = [1, 2, 3]; ← Outer scope
 *   
 *   return function inner() {
 *     console.log(data); ← Access outer scope
 *   };
 * }
 * 
 * inner() giữ reference đến toàn bộ outer scope,
 * kể cả những variables không dùng!
 * 
 * 💡 SOLUTION:
 * 1. Nullify variables sau khi dùng xong
 * 2. Tách scope (block scope với {})
 * 3. Chỉ return những gì cần thiết
 */
```

### **2.4. DOM References** ⭐⭐⭐⭐⭐

```typescript
// ❌ MEMORY LEAK
class BadDOMManager {
  private elements: HTMLElement[] = [];
  
  addElements() {
    for (let i = 0; i < 1000; i++) {
      const el = document.createElement('div');
      document.body.appendChild(el);
      this.elements.push(el); // ❌ Giữ reference
    }
  }
  
  removeFromDOM() {
    this.elements.forEach(el => el.remove());
    // ❌ DOM removed nhưng this.elements vẫn giữ references!
    // → Elements không được GC
  }
}

// ✅ FIXED
class GoodDOMManager {
  private elements: HTMLElement[] = [];
  
  addElements() {
    for (let i = 0; i < 1000; i++) {
      const el = document.createElement('div');
      document.body.appendChild(el);
      this.elements.push(el);
    }
  }
  
  cleanup() {
    this.elements.forEach(el => el.remove());
    this.elements.length = 0; // ✅ Clear references
    // hoặc: this.elements = [];
  }
}

/**
 * 🔥 DETACHED DOM NODES
 * 
 * Element đã bị remove khỏi DOM nhưng vẫn có reference trong JS
 * → "Detached" (tách rời) nhưng không được GC
 * 
 * Common causes:
 * 1. Arrays giữ DOM references
 * 2. Event handlers giữ element refs
 * 3. Closures capture DOM elements
 * 
 * 💡 DETECTION:
 * Chrome DevTools → Memory → Heap Snapshot
 * → Filter by "Detached" → Xem elements nào leak
 */

// ✅ Use WeakMap for DOM metadata
const domMetadata = new WeakMap<HTMLElement, any>();

function attachMetadata(el: HTMLElement, data: any) {
  domMetadata.set(el, data);
  // ✅ Khi el được GC → entry tự động bị xóa
}
```

### **2.5. Global Variables** ⭐⭐⭐

```typescript
// ❌ MEMORY LEAK
var globalCache = []; // ❌ Global var, không bao giờ được GC

function addToCache(data: any) {
  globalCache.push(data);
  // ❌ globalCache phình to mãi, không bao giờ clear
}

// ✅ FIXED 1: Limited size cache
class LRUCache<K, V> {
  private cache = new Map<K, V>();
  private maxSize = 100;
  
  set(key: K, value: V) {
    if (this.cache.size >= this.maxSize) {
      const firstKey = this.cache.keys().next().value;
      this.cache.delete(firstKey); // ✅ Remove oldest
    }
    this.cache.set(key, value);
  }
  
  get(key: K): V | undefined {
    return this.cache.get(key);
  }
}

// ✅ FIXED 2: WeakMap cache
const weakCache = new WeakMap<object, any>();

function cacheResult(obj: object, result: any) {
  weakCache.set(obj, result);
  // ✅ Khi obj được GC → cache entry tự động clear
}

/**
 * 🔥 TẠI SAO GLOBAL VARIABLES NGUY HIỂM?
 * 
 * Global vars = "Roots" trong GC algorithm
 * → Luôn được mark là "còn dùng"
 * → Không bao giờ được GC
 * 
 * 💡 SOLUTIONS:
 * 1. Tránh global vars (dùng modules, closures)
 * 2. Giới hạn kích thước (LRU cache)
 * 3. Cleanup định kỳ
 * 4. Dùng WeakMap cho object keys
 */
```

### **2.6. Circular References** ⭐⭐⭐

```typescript
// ❌ MEMORY LEAK (Old browsers, IE6-8)
function createCircular() {
  const obj1: any = {};
  const obj2: any = {};
  
  obj1.ref = obj2; // obj1 → obj2
  obj2.ref = obj1; // obj2 → obj1 (circular!)
  
  // ❌ Old browsers: Reference counting GC → leak!
  // ✅ Modern browsers: Mark & Sweep → OK!
}

/**
 * 🔥 TẠI SAO CIRCULAR REFS KHÔNG CÒN LÀ VẤN ĐỀ?
 * 
 * Old GC (Reference Counting):
 * - Count số references đến object
 * - Object có 0 refs → GC
 * - ❌ Circular refs: obj1 (1 ref) ← → obj2 (1 ref)
 *   → Không bao giờ về 0 → Leak!
 * 
 * Modern GC (Mark & Sweep):
 * - Bắt đầu từ roots, đánh dấu reachable objects
 * - ✅ Circular refs OK nếu không reachable từ roots
 * 
 * 💡 KẾT LUẬN:
 * Modern browsers (Chrome, Firefox, Safari) không leak với circular refs!
 * Chỉ cần lo với old IE6-8 (nếu vẫn support)
 */

// ✅ Manual cleanup (nếu cần support old browsers)
function cleanupCircular() {
  const obj1: any = {};
  const obj2: any = {};
  
  obj1.ref = obj2;
  obj2.ref = obj1;
  
  // Cleanup
  obj1.ref = null;
  obj2.ref = null;
}
```

### **2.7. Console.log() References** ⭐⭐

```typescript
// ⚠️ SUBTLE LEAK
function processLargeData() {
  const data = new Array(1000000).fill('data');
  
  console.log(data); // ⚠️ DevTools giữ reference!
  // → data không được GC khi DevTools mở
  
  return 'Processed';
}

/**
 * 🔥 TẠI SAO console.log() LEAK?
 * 
 * Browser DevTools lưu console history
 * → Giữ references đến logged objects
 * → Objects không được GC khi DevTools mở
 * 
 * 💡 SOLUTIONS:
 * 1. Remove console.log() trong production
 * 2. Hoặc log primitive values thay vì objects:
 */

// ✅ BETTER
function processLargeDataBetter() {
  const data = new Array(1000000).fill('data');
  
  console.log('Data length:', data.length); // ✅ Chỉ log number
  // hoặc
  console.log('Data:', data.slice(0, 10)); // ✅ Log sample
  
  return 'Processed';
}

// ✅ Production: Remove logs
const log = process.env.NODE_ENV === 'production' 
  ? () => {} 
  : console.log;

log(largeData); // No-op in production
```

### **2.8. Forgotten Subscriptions** ⭐⭐⭐⭐

```typescript
// ❌ MEMORY LEAK (RxJS, EventEmitter, etc.)
class BadComponent {
  constructor(private dataService: DataService) {
    // ❌ Không unsubscribe
    this.dataService.data$.subscribe(data => {
      console.log(data);
    });
  }
}

// ✅ FIXED
class GoodComponent {
  private subscription: Subscription;
  
  constructor(private dataService: DataService) {
    this.subscription = this.dataService.data$.subscribe(data => {
      console.log(data);
    });
  }
  
  destroy() {
    this.subscription.unsubscribe(); // ✅ Cleanup
  }
}

// ✅ React Hook cleanup
function useDataSubscription() {
  useEffect(() => {
    const subscription = dataService.data$.subscribe(data => {
      console.log(data);
    });
    
    return () => subscription.unsubscribe(); // ✅ Cleanup
  }, []);
}

/**
 * 🔥 COMMON SUBSCRIPTION SOURCES:
 * 
 * 1. RxJS Observables
 * 2. EventEmitter (Node.js)
 * 3. WebSocket connections
 * 4. Firebase/Firestore listeners
 * 5. Redux store subscriptions
 * 
 * 💡 ALWAYS UNSUBSCRIBE!
 */
```

### **2.9. Cached Computations** ⭐⭐⭐

```typescript
// ❌ UNBOUNDED CACHE
const fibCache: Record<number, number> = {};

function fibonacci(n: number): number {
  if (n <= 1) return n;
  if (fibCache[n]) return fibCache[n];
  
  fibCache[n] = fibonacci(n - 1) + fibonacci(n - 2);
  return fibCache[n];
  // ❌ Cache phình to vô hạn!
}

// ✅ FIXED: LRU Cache với size limit
class LRUCache<K, V> {
  private cache = new Map<K, V>();
  
  constructor(private maxSize = 100) {}
  
  get(key: K): V | undefined {
    const value = this.cache.get(key);
    if (value !== undefined) {
      // Move to end (most recently used)
      this.cache.delete(key);
      this.cache.set(key, value);
    }
    return value;
  }
  
  set(key: K, value: V) {
    if (this.cache.has(key)) {
      this.cache.delete(key);
    } else if (this.cache.size >= this.maxSize) {
      // Remove least recently used (first item)
      const firstKey = this.cache.keys().next().value;
      this.cache.delete(firstKey);
    }
    this.cache.set(key, value);
  }
}

const fibCache2 = new LRUCache<number, number>(100);

function fibonacciFixed(n: number): number {
  if (n <= 1) return n;
  
  const cached = fibCache2.get(n);
  if (cached !== undefined) return cached;
  
  const result = fibonacciFixed(n - 1) + fibonacciFixed(n - 2);
  fibCache2.set(n, result);
  return result;
}
```

### **2.10. Web Workers / Service Workers** ⭐⭐

```typescript
// ❌ MEMORY LEAK
let worker: Worker;

function startWorker() {
  worker = new Worker('worker.js');
  
  worker.onmessage = (e) => {
    console.log(e.data);
  };
  
  // ❌ Không terminate worker
}

// ✅ FIXED
let workerFixed: Worker | null = null;

function startWorkerFixed() {
  workerFixed = new Worker('worker.js');
  
  workerFixed.onmessage = (e) => {
    console.log(e.data);
  };
}

function stopWorker() {
  if (workerFixed) {
    workerFixed.terminate(); // ✅ Cleanup
    workerFixed = null;
  }
}

/**
 * 🔥 WORKERS LEAK MEMORY IF NOT TERMINATED
 * 
 * Web Workers run in separate thread
 * → Có own memory space
 * → Phải terminate() để free memory
 * 
 * Service Workers persist across page loads
 * → Cần unregister() khi không dùng
 */
```

---

## 🔍 PART 3: DETECTION & MONITORING

### **3.1. Chrome DevTools Memory Profiler**

```typescript
/**
 * 🛠️ CHROME DEVTOOLS - MEMORY TAB
 * 
 * 1. HEAP SNAPSHOT:
 *    - Chụp ảnh memory tại 1 thời điểm
 *    - So sánh snapshots để tìm leaks
 *    - Filter: "Detached" → tìm DOM leaks
 * 
 * 2. ALLOCATION TIMELINE:
 *    - Record allocations over time
 *    - Xem memory tăng liên tục → leak!
 * 
 * 3. ALLOCATION SAMPLING:
 *    - Lightweight profiling
 *    - Tìm functions allocate nhiều memory
 * 
 * 📊 WORKFLOW:
 * Step 1: Take snapshot 1
 * Step 2: Perform actions (click, navigate, etc.)
 * Step 3: Take snapshot 2
 * Step 4: Compare → objects tăng lên = leak candidates
 */

// Example: Find leak source
function findLeak() {
  // 1. Open DevTools → Memory tab
  // 2. Take Heap Snapshot (before)
  
  for (let i = 0; i < 100; i++) {
    createPotentialLeak();
  }
  
  // 3. Take Heap Snapshot (after)
  // 4. Compare → objects tăng 100 = leak!
}
```

### **3.2. Performance.memory API**

```typescript
// Monitor memory usage
function monitorMemory() {
  if ('memory' in performance) {
    const memory = (performance as any).memory;
    
    const used = (memory.usedJSHeapSize / 1024 / 1024).toFixed(2);
    const total = (memory.totalJSHeapSize / 1024 / 1024).toFixed(2);
    const limit = (memory.jsHeapSizeLimit / 1024 / 1024).toFixed(2);
    
    console.log(`Memory: ${used}MB / ${total}MB (limit: ${limit}MB)`);
    
    // Alert if high
    if (memory.usedJSHeapSize / memory.jsHeapSizeLimit > 0.9) {
      console.warn('⚠️ Memory usage > 90%!');
    }
  }
}

// Continuous monitoring
setInterval(monitorMemory, 5000); // Every 5s
```

### **3.3. Memory Leak Detector (Custom)**

```typescript
class MemoryLeakDetector {
  private static instances = new WeakSet<object>();
  private static counts = new Map<string, number>();
  
  static track(obj: object, label: string) {
    this.instances.add(obj);
    this.counts.set(label, (this.counts.get(label) || 0) + 1);
  }
  
  static untrack(obj: object, label: string) {
    if (this.instances.has(obj)) {
      this.counts.set(label, (this.counts.get(label) || 0) - 1);
    }
  }
  
  static report() {
    console.table(Array.from(this.counts.entries()));
  }
}

// Usage
class TrackedComponent {
  constructor() {
    MemoryLeakDetector.track(this, 'Component');
  }
  
  destroy() {
    MemoryLeakDetector.untrack(this, 'Component');
  }
}

// Check leaks
setInterval(() => {
  MemoryLeakDetector.report();
  // Nếu count cứ tăng → leak!
}, 10000);
```

---

## 💡 BEST PRACTICES

### **Checklist - Tránh Memory Leaks**

```typescript
/**
 * ✅ CLEANUP CHECKLIST
 * 
 * 1. EVENT LISTENERS:
 *    □ removeEventListener() hoặc AbortController
 *    □ Lưu bound functions để remove được
 * 
 * 2. TIMERS:
 *    □ clearInterval() / clearTimeout()
 *    □ cancelAnimationFrame()
 * 
 * 3. SUBSCRIPTIONS:
 *    □ unsubscribe() RxJS
 *    □ off() EventEmitter
 *    □ Close WebSocket/SSE connections
 * 
 * 4. DOM REFERENCES:
 *    □ Clear arrays holding elements
 *    □ Remove event listeners before element.remove()
 *    □ Nullify refs: element = null
 * 
 * 5. CLOSURES:
 *    □ Nullify large variables after use
 *    □ Tách scope với {} blocks
 * 
 * 6. GLOBAL STATE:
 *    □ Limit cache sizes (LRU)
 *    □ Periodic cleanup
 *    □ Use WeakMap for object keys
 * 
 * 7. WORKERS:
 *    □ worker.terminate()
 *    □ serviceWorker.unregister()
 * 
 * 8. MONITORING:
 *    □ Heap snapshots (DevTools)
 *    □ performance.memory tracking
 *    □ Automated leak detection
 */

// ✅ Pattern: Resource Manager
class ResourceManager {
  private cleanups: Array<() => void> = [];
  
  add(cleanup: () => void) {
    this.cleanups.push(cleanup);
  }
  
  cleanup() {
    this.cleanups.forEach(fn => fn());
    this.cleanups = [];
  }
}

// Usage
const rm = new ResourceManager();

// Add event listener
const handler = () => console.log('click');
element.addEventListener('click', handler);
rm.add(() => element.removeEventListener('click', handler));

// Add timer
const id = setInterval(() => {}, 1000);
rm.add(() => clearInterval(id));

// Add subscription
const sub = observable.subscribe();
rm.add(() => sub.unsubscribe());

// Cleanup all
rm.cleanup(); // ✅ One call to cleanup everything!
```

---

## 📊 SUMMARY TABLE

```
┌────────────────────────┬──────────┬─────────────────────────────────┐
│ Leak Type              │ Severity │ Solution                        │
├────────────────────────┼──────────┼─────────────────────────────────┤
│ Event Listeners        │ ⭐⭐⭐⭐⭐ │ removeEventListener/AbortCtrl   │
│ Timers                 │ ⭐⭐⭐⭐⭐ │ clearInterval/clearTimeout      │
│ DOM References         │ ⭐⭐⭐⭐⭐ │ Nullify refs, use WeakMap       │
│ Closures               │ ⭐⭐⭐⭐   │ Nullify unused vars             │
│ Global Variables       │ ⭐⭐⭐    │ LRU cache, WeakMap              │
│ Subscriptions          │ ⭐⭐⭐⭐   │ unsubscribe()                   │
│ Console.log            │ ⭐⭐      │ Remove in production            │
│ Cached Computations    │ ⭐⭐⭐    │ LRU cache with size limit       │
│ Workers                │ ⭐⭐      │ terminate()/unregister()        │
│ Circular Refs          │ ⭐        │ OK in modern browsers           │
└────────────────────────┴──────────┴─────────────────────────────────┘
```

**🎯 Top 3 Most Common Leaks:**
1. **Event Listeners** - Quên removeEventListener
2. **Timers** - Quên clearInterval/clearTimeout  
3. **DOM References** - Arrays giữ detached elements

**🔍 Detection Tools:**
- Chrome DevTools → Memory → Heap Snapshot
- `performance.memory` API
- Custom leak detectors (WeakSet tracking)

**✅ Prevention:**
- Always cleanup trong destroy/unmount
- Use WeakMap/WeakSet cho temporary refs
- Implement Resource Manager pattern
- Monitor memory usage

```typescript
// Memory allocation
function createLargeObject(): object {
  return {
    data: new Array(1000000).fill('large data'),
    timestamp: Date.now(),
  };
}

// Object lifecycle
let largeObject = createLargeObject();
console.log('Object created');

// Object becomes eligible for GC when no references
largeObject = null;
console.log('Object reference removed');

// Garbage Collection triggers
function triggerGC(): void {
  // Force garbage collection (if available)
  if (window.gc) {
    window.gc();
  }
}

// Memory monitoring
function monitorMemory(): void {
  if ('memory' in performance) {
    const memory = (performance as any).memory;
    console.log('Used:', memory.usedJSHeapSize / 1024 / 1024, 'MB');
    console.log('Total:', memory.totalJSHeapSize / 1024 / 1024, 'MB');
    console.log('Limit:', memory.jsHeapSizeLimit / 1024 / 1024, 'MB');
  }
}

// Weak references (don't prevent GC)
const weakMap = new WeakMap();
const weakSet = new WeakSet();

function useWeakReferences(): void {
  const obj = { data: 'important' };

  // These don't prevent garbage collection
  weakMap.set(obj, 'metadata');
  weakSet.add(obj);

  // obj can be garbage collected even with weak references
  // weakMap and weakSet will automatically remove the entries
}

// Memory leaks examples
function createMemoryLeak(): void {
  const elements: HTMLElement[] = [];

  // Memory leak: keeping references to DOM elements
  for (let i = 0; i < 1000; i++) {
    const element = document.createElement('div');
    elements.push(element); // Keeps reference
  }

  // Elements won't be garbage collected
}

// Proper cleanup
function properCleanup(): void {
  const elements: HTMLElement[] = [];

  for (let i = 0; i < 1000; i++) {
    const element = document.createElement('div');
    elements.push(element);
  }

  // Cleanup: remove references
  elements.length = 0;
  // Now elements can be garbage collected
}

// Event listener cleanup
function addEventListenerWithCleanup(): () => void {
  const handler = (event: Event) => {
    console.log('Event:', event);
  };

  document.addEventListener('click', handler);

  // Return cleanup function
  return () => {
    document.removeEventListener('click', handler);
  };
}

const cleanup = addEventListenerWithCleanup();
// Later: cleanup(); // Remove event listener
```

**Best Practices:**

- Sử dụng WeakMap/WeakSet cho temporary references
- Cleanup event listeners
- Remove DOM references khi không cần
- Monitor memory usage
- Sử dụng proper cleanup functions

**Mistakes:**

```typescript
// ❌ Sai: Không cleanup event listeners
document.addEventListener('click', handler);
// Memory leak nếu không removeEventListener

// ✅ Đúng: Cleanup event listeners
const cleanup = () => document.removeEventListener('click', handler);
cleanup(); // Remove listener
```

