# 🪞 Q21: JavaScript Proxy - Chi Tiết & Use Cases Thực Tế

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"Proxy là tính năng lập trình meta cho phép chặn và tùy chỉnh hành vi của các thao tác trên object.**

**📦 Khái Niệm Cốt Lõi:**
- **Cú pháp**: `new Proxy(target, handler)` → Bọc object với hành vi tùy chỉnh.
- **Handler Traps (Bẫy)**: 13 bẫy để chặn các thao tác (get, set, has, deleteProperty, apply, construct, v.v.).
- **Reflect API**: API đồng hành cung cấp hành vi mặc định → dùng trong bẫy để chuyển tiếp thao tác đúng cách.
- **Trong suốt**: Proxy hoàn toàn trong suốt → code sử dụng không biết đang dùng proxy.

**🔧 13 Bẫy Proxy (Quan Trọng Nhất):**
1. **`get(target, property, receiver)`**: Chặn truy cập thuộc tính → validation, logging, lazy loading.
2. **`set(target, property, value, receiver)`**: Chặn gán giá trị → validation, reactivity (Vue, MobX).
3. **`has(target, property)`**: Chặn toán tử `in` → ẩn thuộc tính.
4. **`deleteProperty(target, property)`**: Chặn `delete` → ngăn xóa.
5. **`apply(target, thisArg, args)`**: Chặn gọi hàm → logging, giới hạn tần suất.
6. **`construct(target, args, newTarget)`**: Chặn toán tử `new` → singleton pattern.
7. **`getPrototypeOf()`, `setPrototypeOf()`**: Chặn truy cập chuỗi prototype.
8. **`defineProperty()`, `getOwnPropertyDescriptor()`**: Chặn định nghĩa thuộc tính.
9. **`ownKeys()`**: Chặn `Object.keys()`, `for...in` → lọc keys.
10. **`preventExtensions()`, `isExtensible()`**: Chặn tính mở rộng.

**🎯 Trường Hợp Sử Dụng Thực Tế:**
- **Validation (Xác thực)**: Tự động validate khi gán thuộc tính → xác thực form, kiểm tra kiểu dữ liệu.
- **Reactivity (Phản ứng - Vue 3)**: Proxy bọc state → theo dõi phụ thuộc → tự động render lại.
- **Logging/Debugging**: Ghi log mọi truy cập/sửa đổi thuộc tính → audit trail.
- **API Mocking**: Bọc API client → tự động thử lại, cache, xử lý lỗi.
- **React Hook Form**: Proxy bọc form state → theo dõi fields bị thay đổi, validate khi thay đổi.
- **Lazy Loading**: Truy cập thuộc tính kích hoạt tải bất đồng bộ → tối ưu kích thước bundle.
- **Kiểm soát truy cập**: Chặn truy cập thuộc tính không được phép → bảo mật.

**🔍 Cơ Chế React Hook Form (Chi Tiết):**
```typescript
// RHF dùng Proxy để:
1. **Theo dõi đăng ký field**: bẫy get → tự động đăng ký field khi truy cập.
2. **Validate khi thay đổi**: bẫy set → kích hoạt validation khi setValue.
3. **Theo dõi trạng thái dirty**: So sánh proxy state với giá trị mặc định.
4. **Hỗ trợ object lồng nhau**: Proxy đệ quy cho nested fields.
5. **Hiệu năng**: Chỉ render lại fields bị thay đổi (reactivity chi tiết).
```

**⚠️ Đánh Đổi Hiệu Năng:**
- **Chi phí thêm**: Mỗi thao tác có thêm lời gọi hàm → chậm hơn ~10-20%.
- **Bộ nhớ**: Proxy object + handler object → tăng sử dụng bộ nhớ.
- **Tối ưu hóa**: V8 không tối ưu được proxy như plain objects.
- **Thực hành tốt**: Chỉ dùng khi cần metaprogramming, tránh lạm dụng.

**💡 Kiến Thức Senior:**
- **Reflect vs Truy cập trực tiếp**: Luôn dùng `Reflect.get/set` trong bẫy → đúng hành vi với kế thừa.
- **Revocable Proxy**: `Proxy.revocable()` → tạo proxy có thể vô hiệu hóa (bảo mật, cleanup).
- **Proxy vs Object.defineProperty**: Proxy mạnh hơn (chặn 13 thao tác vs 1), nhưng không hỗ trợ IE11.
- **Vue 2 vs Vue 3**: Vue 2 dùng `Object.defineProperty` → không phát hiện thay đổi mảng. Vue 3 dùng Proxy → phát hiện tất cả.
- **Debugging**: Proxy khó debug → dùng `console.log` trong bẫy hoặc `Proxy.revocable` để vô hiệu.

---

## **I. Proxy Là Gì?**

### **1.1. Khái Niệm Cơ Bản**

```typescript
/**
 * 🎭 PROXY = INTERCEPTOR CHO OBJECT OPERATIONS
 * 
 * Syntax: new Proxy(target, handler)
 * • target: Object gốc cần wrap
 * • handler: Object chứa các "traps" (interceptors)
 */

// Ví dụ đơn giản nhất
const target = { name: 'John', age: 25 };

const proxy = new Proxy(target, {
  // Trap: intercept property access
  get(target, property, receiver) {
    console.log(`📖 Reading: ${String(property)}`);
    return Reflect.get(target, property, receiver);
  },
  
  // Trap: intercept property assignment
  set(target, property, value, receiver) {
    console.log(`✏️ Writing: ${String(property)} = ${value}`);
    return Reflect.set(target, property, value, receiver);
  }
});

console.log(proxy.name);  // 📖 Reading: name → "John"
proxy.age = 26;           // ✏️ Writing: age = 26
console.log(proxy.age);   // 📖 Reading: age → 26

/**
 * ⚠️ QUAN TRỌNG:
 * • Proxy ≠ modify target trực tiếp
 * • Proxy = wrapper object với custom behavior
 * • Target object vẫn nguyên vẹn
 */
```

---

### **1.2. Reflect API - Companion của Proxy**

```typescript
/**
 * 🔍 REFLECT = DEFAULT BEHAVIORS
 * 
 * Tại sao dùng Reflect thay vì thao tác trực tiếp?
 * 1. Consistent API (trả về boolean thay vì throw error)
 * 2. Forward receiver correctly (quan trọng cho inheritance)
 * 3. Chainable với Proxy
 */

// ❌ Không dùng Reflect
const proxy1 = new Proxy(target, {
  set(target, property, value) {
    target[property] = value;  // Direct assignment
    return true;
  }
});

// ✅ Dùng Reflect (Recommended)
const proxy2 = new Proxy(target, {
  set(target, property, value, receiver) {
    return Reflect.set(target, property, value, receiver);
  }
});

/**
 * Reflect API tương ứng với các traps:
 * 
 * • Reflect.get(target, property, receiver)
 * • Reflect.set(target, property, value, receiver)
 * • Reflect.has(target, property)
 * • Reflect.deleteProperty(target, property)
 * • Reflect.apply(target, thisArg, args)
 * • Reflect.construct(target, args, newTarget)
 * • Reflect.getPrototypeOf(target)
 * • Reflect.setPrototypeOf(target, prototype)
 * • Reflect.defineProperty(target, property, descriptor)
 * • Reflect.getOwnPropertyDescriptor(target, property)
 * • Reflect.ownKeys(target)
 * • Reflect.preventExtensions(target)
 * • Reflect.isExtensible(target)
 */
```

---

## **II. Tất Cả Proxy Traps (13 Traps)**

### **2.1. Property Access Traps**

```typescript
/**
 * ══════════════════════════════════════════════════════════
 * 1. GET TRAP - Intercept property reading
 * ══════════════════════════════════════════════════════════
 */
const getTrapExample = new Proxy({}, {
  get(target, property, receiver) {
    // Default value cho undefined properties
    if (!(property in target)) {
      return `Property "${String(property)}" not found`;
    }
    return Reflect.get(target, property, receiver);
  }
});

console.log(getTrapExample.name); // "Property "name" not found"

/**
 * ══════════════════════════════════════════════════════════
 * 2. SET TRAP - Intercept property writing
 * ══════════════════════════════════════════════════════════
 */
const setTrapExample = new Proxy({}, {
  set(target, property, value, receiver) {
    console.log(`Setting ${String(property)} to ${value}`);
    
    // Validation
    if (property === 'age' && typeof value !== 'number') {
      throw new TypeError('Age must be a number');
    }
    
    return Reflect.set(target, property, value, receiver);
  }
});

setTrapExample.name = 'John';  // ✅ OK
// setTrapExample.age = 'twenty'; // ❌ TypeError

/**
 * ══════════════════════════════════════════════════════════
 * 3. HAS TRAP - Intercept "in" operator
 * ══════════════════════════════════════════════════════════
 */
const hasTrapExample = new Proxy({
  _secret: 'password123',
  public: 'visible'
}, {
  has(target, property) {
    // Hide private properties
    if (String(property).startsWith('_')) {
      return false;
    }
    return Reflect.has(target, property);
  }
});

console.log('public' in hasTrapExample);  // true
console.log('_secret' in hasTrapExample); // false (hidden!)

/**
 * ══════════════════════════════════════════════════════════
 * 4. DELETE PROPERTY TRAP - Intercept property deletion
 * ══════════════════════════════════════════════════════════
 */
const deleteTrapExample = new Proxy({
  name: 'John',
  age: 25
}, {
  deleteProperty(target, property) {
    // Prevent deletion of specific properties
    if (property === 'name') {
      console.warn('Cannot delete name property');
      return false;
    }
    return Reflect.deleteProperty(target, property);
  }
});

delete deleteTrapExample.age;  // ✅ OK
delete deleteTrapExample.name; // ⚠️ Cannot delete name property

/**
 * ══════════════════════════════════════════════════════════
 * 5. OWN KEYS TRAP - Intercept Object.keys(), for...in
 * ══════════════════════════════════════════════════════════
 */
const ownKeysTrapExample = new Proxy({
  name: 'John',
  age: 25,
  _password: 'secret'
}, {
  ownKeys(target) {
    // Hide private properties from enumeration
    return Reflect.ownKeys(target).filter(
      key => !String(key).startsWith('_')
    );
  }
});

console.log(Object.keys(ownKeysTrapExample)); // ['name', 'age']

/**
 * ══════════════════════════════════════════════════════════
 * 6. GET OWN PROPERTY DESCRIPTOR TRAP
 * ══════════════════════════════════════════════════════════
 */
const descriptorTrapExample = new Proxy({
  name: 'John'
}, {
  getOwnPropertyDescriptor(target, property) {
    const descriptor = Reflect.getOwnPropertyDescriptor(target, property);
    
    // Make all properties appear non-configurable
    if (descriptor) {
      descriptor.configurable = false;
    }
    
    return descriptor;
  }
});

/**
 * ══════════════════════════════════════════════════════════
 * 7. DEFINE PROPERTY TRAP - Intercept Object.defineProperty()
 * ══════════════════════════════════════════════════════════
 */
const defineTrapExample = new Proxy({}, {
  defineProperty(target, property, descriptor) {
    console.log(`Defining property: ${String(property)}`);
    
    // Auto-add getter/setter
    if (descriptor.value !== undefined) {
      descriptor.writable = true;
      descriptor.enumerable = true;
    }
    
    return Reflect.defineProperty(target, property, descriptor);
  }
});
```

---

### **2.2. Function & Constructor Traps**

```typescript
/**
 * ══════════════════════════════════════════════════════════
 * 8. APPLY TRAP - Intercept function calls
 * ══════════════════════════════════════════════════════════
 */
function sum(a: number, b: number) {
  return a + b;
}

const sumProxy = new Proxy(sum, {
  apply(target, thisArg, args) {
    console.log(`Calling function with args: ${args}`);
    
    // Validate arguments
    if (args.some(arg => typeof arg !== 'number')) {
      throw new TypeError('All arguments must be numbers');
    }
    
    return Reflect.apply(target, thisArg, args);
  }
});

console.log(sumProxy(2, 3));  // Calling function with args: 2,3 → 5
// sumProxy(2, '3');           // ❌ TypeError

/**
 * ══════════════════════════════════════════════════════════
 * 9. CONSTRUCT TRAP - Intercept "new" operator
 * ══════════════════════════════════════════════════════════
 */
class User {
  constructor(public name: string, public age: number) {}
}

const UserProxy = new Proxy(User, {
  construct(target, args, newTarget) {
    console.log(`Creating new User with args: ${args}`);
    
    // Validate constructor arguments
    if (args.length < 2) {
      throw new Error('User requires name and age');
    }
    
    return Reflect.construct(target, args, newTarget);
  }
});

const user = new UserProxy('John', 25); // ✅ OK
// const user2 = new UserProxy('John');  // ❌ Error
```

---

### **2.3. Prototype & Extensibility Traps**

```typescript
/**
 * ══════════════════════════════════════════════════════════
 * 10. GET PROTOTYPE OF TRAP
 * ══════════════════════════════════════════════════════════
 */
const protoTrapExample = new Proxy({}, {
  getPrototypeOf(target) {
    console.log('Getting prototype');
    return Reflect.getPrototypeOf(target);
  }
});

Object.getPrototypeOf(protoTrapExample); // Getting prototype

/**
 * ══════════════════════════════════════════════════════════
 * 11. SET PROTOTYPE OF TRAP
 * ══════════════════════════════════════════════════════════
 */
const setProtoTrapExample = new Proxy({}, {
  setPrototypeOf(target, prototype) {
    console.log('Changing prototype is forbidden');
    return false; // Prevent prototype change
  }
});

// Object.setPrototypeOf(setProtoTrapExample, Array.prototype); // ❌ Fails silently

/**
 * ══════════════════════════════════════════════════════════
 * 12. IS EXTENSIBLE TRAP
 * ══════════════════════════════════════════════════════════
 */
const extensibleTrapExample = new Proxy({}, {
  isExtensible(target) {
    console.log('Checking extensibility');
    return Reflect.isExtensible(target);
  }
});

Object.isExtensible(extensibleTrapExample); // Checking extensibility

/**
 * ══════════════════════════════════════════════════════════
 * 13. PREVENT EXTENSIONS TRAP
 * ══════════════════════════════════════════════════════════
 */
const preventExtTrapExample = new Proxy({}, {
  preventExtensions(target) {
    console.log('Preventing extensions');
    return Reflect.preventExtensions(target);
  }
});

Object.preventExtensions(preventExtTrapExample); // Preventing extensions
```

---

## **III. Use Cases Thực Tế**

### **3.1. Validation & Type Safety**

```typescript
/**
 * 🛡️ VALIDATION PROXY
 */

interface User {
  name: string;
  age: number;
  email: string;
}

function createValidatedUser(schema: Record<string, (value: any) => boolean>): User {
  return new Proxy({} as User, {
    set(target, property, value) {
      const validator = schema[property as string];
      
      if (!validator) {
        throw new Error(`Unknown property: ${String(property)}`);
      }
      
      if (!validator(value)) {
        throw new Error(`Invalid value for ${String(property)}: ${value}`);
      }
      
      return Reflect.set(target, property, value);
    }
  });
}

const user = createValidatedUser({
  name: (val) => typeof val === 'string' && val.length > 0,
  age: (val) => typeof val === 'number' && val >= 0 && val <= 150,
  email: (val) => typeof val === 'string' && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val)
});

user.name = 'John';               // ✅ OK
user.age = 25;                    // ✅ OK
user.email = 'john@example.com';  // ✅ OK

// user.age = -5;                 // ❌ Error: Invalid value for age: -5
// user.email = 'invalid';        // ❌ Error: Invalid value for email: invalid
// user.unknown = 'test';         // ❌ Error: Unknown property: unknown
```

---

### **3.2. Reactive Data (Vue 3 Style)**

```typescript
/**
 * ⚡ REACTIVE SYSTEM - NHƯ VUE 3
 */

type Subscriber = () => void;
const subscribers = new Set<Subscriber>();
let activeEffect: Subscriber | null = null;

// Track dependencies
function track(target: object, property: string | symbol) {
  if (activeEffect) {
    const depsMap = getDepsMap(target);
    let deps = depsMap.get(property);
    
    if (!deps) {
      deps = new Set();
      depsMap.set(property, deps);
    }
    
    deps.add(activeEffect);
  }
}

// Trigger updates
function trigger(target: object, property: string | symbol) {
  const depsMap = getDepsMap(target);
  const deps = depsMap.get(property);
  
  if (deps) {
    deps.forEach(effect => effect());
  }
}

const targetMap = new WeakMap<object, Map<string | symbol, Set<Subscriber>>>();

function getDepsMap(target: object) {
  let depsMap = targetMap.get(target);
  if (!depsMap) {
    depsMap = new Map();
    targetMap.set(target, depsMap);
  }
  return depsMap;
}

// Create reactive object
function reactive<T extends object>(target: T): T {
  return new Proxy(target, {
    get(target, property, receiver) {
      track(target, property);
      return Reflect.get(target, property, receiver);
    },
    set(target, property, value, receiver) {
      const result = Reflect.set(target, property, value, receiver);
      trigger(target, property);
      return result;
    }
  });
}

// Watch effect
function watchEffect(effect: Subscriber) {
  activeEffect = effect;
  effect(); // Run once to collect dependencies
  activeEffect = null;
}

// Usage
const state = reactive({
  count: 0,
  name: 'John'
});

watchEffect(() => {
  console.log(`Count is: ${state.count}`);
});

state.count++; // Count is: 1
state.count++; // Count is: 2

/**
 * Cơ chế:
 * 1. reactive() tạo Proxy wrap object
 * 2. get trap → track() ghi nhận dependency
 * 3. set trap → trigger() chạy lại effects
 * 4. watchEffect() auto re-run khi dependencies thay đổi
 */
```

---

### **3.3. Logging & Debugging**

```typescript
/**
 * 📊 LOGGING PROXY
 */

function createLogger<T extends object>(target: T, name: string): T {
  return new Proxy(target, {
    get(target, property, receiver) {
      const value = Reflect.get(target, property, receiver);
      console.log(`[${name}] GET ${String(property)} = ${JSON.stringify(value)}`);
      return value;
    },
    
    set(target, property, value, receiver) {
      const oldValue = target[property as keyof T];
      const result = Reflect.set(target, property, value, receiver);
      console.log(
        `[${name}] SET ${String(property)}: ${JSON.stringify(oldValue)} → ${JSON.stringify(value)}`
      );
      return result;
    },
    
    deleteProperty(target, property) {
      const oldValue = target[property as keyof T];
      const result = Reflect.deleteProperty(target, property);
      console.log(`[${name}] DELETE ${String(property)} (was: ${JSON.stringify(oldValue)})`);
      return result;
    }
  });
}

const state = createLogger({ count: 0, name: 'John' }, 'AppState');

state.count++;        // [AppState] GET count = 0
                      // [AppState] SET count: 0 → 1

state.name = 'Jane';  // [AppState] SET name: "John" → "Jane"

delete state.name;    // [AppState] DELETE name (was: "Jane")
```

---

### **3.4. Default Values & Fallbacks**

```typescript
/**
 * 🎯 DEFAULT VALUES PROXY
 */

function withDefaults<T extends object>(target: T, defaults: Partial<T>): T {
  return new Proxy(target, {
    get(target, property, receiver) {
      // Return default if property doesn't exist
      if (!(property in target) && property in defaults) {
        return defaults[property as keyof T];
      }
      return Reflect.get(target, property, receiver);
    }
  });
}

const config = withDefaults(
  { apiUrl: 'https://api.example.com' },
  {
    timeout: 5000,
    retries: 3,
    apiUrl: 'https://default.com'
  }
);

console.log(config.apiUrl);  // "https://api.example.com" (from target)
console.log(config.timeout); // 5000 (from defaults)
console.log(config.retries); // 3 (from defaults)
```

---

### **3.5. Negative Array Indexing (Python Style)**

```typescript
/**
 * 🐍 NEGATIVE INDEXING
 */

function createNegativeArray<T>(arr: T[]): T[] {
  return new Proxy(arr, {
    get(target, property, receiver) {
      const index = Number(property);
      
      // Handle negative indices
      if (Number.isInteger(index) && index < 0) {
        return target[target.length + index];
      }
      
      return Reflect.get(target, property, receiver);
    }
  });
}

const arr = createNegativeArray([1, 2, 3, 4, 5]);

console.log(arr[0]);   // 1
console.log(arr[-1]);  // 5 (last element)
console.log(arr[-2]);  // 4 (second to last)
console.log(arr[-5]);  // 1 (first element)
```

---

### **3.6. Cache / Memoization**

```typescript
/**
 * 💾 MEMOIZATION PROXY
 */

function memoize<T extends (...args: any[]) => any>(fn: T): T {
  const cache = new Map<string, ReturnType<T>>();
  
  return new Proxy(fn, {
    apply(target, thisArg, args) {
      const key = JSON.stringify(args);
      
      if (cache.has(key)) {
        console.log(`Cache hit for ${key}`);
        return cache.get(key);
      }
      
      console.log(`Cache miss for ${key}`);
      const result = Reflect.apply(target, thisArg, args);
      cache.set(key, result);
      return result;
    }
  }) as T;
}

const fibonacci = memoize((n: number): number => {
  if (n <= 1) return n;
  return fibonacci(n - 1) + fibonacci(n - 2);
});

console.log(fibonacci(10)); // Cache misses on first call
console.log(fibonacci(10)); // Cache hit!

/**
 * Performance comparison:
 * • Without memoization: fibonacci(40) ~ 1-2 seconds
 * • With memoization: fibonacci(40) ~ < 1ms
 */
```

---

### **3.7. Access Control & Privacy**

```typescript
/**
 * 🔒 PRIVATE PROPERTIES
 */

function createPrivate<T extends object>(target: T): T {
  return new Proxy(target, {
    get(target, property, receiver) {
      // Block access to private properties (starting with _)
      if (String(property).startsWith('_')) {
        throw new Error(`Cannot access private property: ${String(property)}`);
      }
      return Reflect.get(target, property, receiver);
    },
    
    set(target, property, value, receiver) {
      if (String(property).startsWith('_')) {
        throw new Error(`Cannot set private property: ${String(property)}`);
      }
      return Reflect.set(target, property, value, receiver);
    },
    
    has(target, property) {
      // Hide private properties from "in" operator
      if (String(property).startsWith('_')) {
        return false;
      }
      return Reflect.has(target, property);
    },
    
    ownKeys(target) {
      // Hide from Object.keys()
      return Reflect.ownKeys(target).filter(
        key => !String(key).startsWith('_')
      );
    }
  });
}

const obj = createPrivate({
  name: 'John',
  _password: 'secret123'
});

console.log(obj.name);           // "John" ✅
// console.log(obj._password);   // ❌ Error: Cannot access private property

console.log('name' in obj);      // true
console.log('_password' in obj); // false (hidden!)

console.log(Object.keys(obj));   // ['name'] (no _password)
```

---

## **IV. React Hook Form & Proxy - Chi Tiết**

### **4.1. React Hook Form Internal Architecture**

```typescript
/**
 * 📝 REACT HOOK FORM SỬ DỤNG PROXY NHƯ THẾ NÀO?
 * 
 * React Hook Form (RHF) dùng Proxy để:
 * 1. Track field registrations
 * 2. Lazy register fields
 * 3. Optimize re-renders
 * 4. Type-safe field names
 */

// Simplified version of RHF's internal
interface FormState {
  [key: string]: any;
}

interface FieldState {
  _f: {
    ref: HTMLInputElement;
    name: string;
    value: any;
  };
}

class FormControl<T extends FormState> {
  private _formState: T;
  private _fields: Map<string, FieldState> = new Map();
  private _proxyFormState: T;
  
  constructor(defaultValues: T) {
    this._formState = defaultValues;
    
    // Create Proxy for formState
    this._proxyFormState = new Proxy(this._formState, {
      get: (target, property) => {
        // Track which fields are being accessed
        this.trackFieldUsage(property as string);
        return Reflect.get(target, property);
      }
    });
  }
  
  private trackFieldUsage(fieldName: string) {
    console.log(`Field accessed: ${fieldName}`);
    // RHF uses this to know which components depend on which fields
    // → Only re-render components that use changed fields!
  }
  
  // register() creates a Proxy for each field
  register(name: keyof T) {
    const fieldProxy = new Proxy({
      _f: {
        ref: null as any,
        name: name as string,
        value: this._formState[name]
      }
    } as FieldState, {
      get: (target, property) => {
        if (property === 'ref') {
          // Return ref setter
          return (ref: HTMLInputElement) => {
            target._f.ref = ref;
            this._fields.set(name as string, target);
          };
        }
        
        if (property === 'value') {
          return this._formState[name];
        }
        
        return Reflect.get(target, property);
      },
      
      set: (target, property, value) => {
        if (property === 'value') {
          // Update form state when field changes
          this._formState[name] = value;
          this.triggerValidation(name as string);
        }
        
        return Reflect.set(target, property, value);
      }
    });
    
    return fieldProxy;
  }
  
  private triggerValidation(fieldName: string) {
    console.log(`Validating field: ${fieldName}`);
    // Trigger validation for this field only
  }
  
  get formState() {
    return this._proxyFormState;
  }
}

// Usage (simplified)
interface LoginForm {
  email: string;
  password: string;
}

const form = new FormControl<LoginForm>({
  email: '',
  password: ''
});

// Register fields
const emailField = form.register('email');
const passwordField = form.register('password');

// When user types:
emailField.value = 'user@example.com';
// → Only triggers validation for email field
// → Only re-renders components using email

// Access formState
console.log(form.formState.email);
// → Tracks that this component uses "email"
// → Component will re-render only when email changes

/**
 * 🎯 BENEFITS OF PROXY IN RHF:
 * 
 * 1. LAZY REGISTRATION
 *    • Fields chỉ register khi được render
 *    • Không cần pre-define tất cả fields
 * 
 * 2. GRANULAR RE-RENDERS
 *    • Track component dependencies
 *    • Chỉ re-render components sử dụng changed fields
 * 
 * 3. TYPE SAFETY
 *    • TypeScript autocomplete cho field names
 *    • Compile-time error nếu typo
 * 
 * 4. PERFORMANCE
 *    • Không cần deep watching
 *    • Không cần virtual DOM diffing cho forms
 */
```

---

### **4.2. RHF Deep Dive - Actual Implementation**

```typescript
/**
 * 🔬 REACT HOOK FORM - ACTUAL PROXY USAGE
 */

import { useForm } from 'react-hook-form';

// RHF internally creates multiple Proxies:

// 1. FORM STATE PROXY
function createFormStateProxy<T>(formState: T, readFormState: Set<keyof T>) {
  return new Proxy(formState, {
    get(target, property) {
      // Track which properties are accessed
      if (property in target) {
        readFormState.add(property as keyof T);
      }
      return Reflect.get(target, property);
    }
  });
}

// 2. FIELDS PROXY
function createFieldsProxy<T>(
  fields: Map<string, any>,
  updateSubscriber: (name: string) => void
) {
  return new Proxy({} as T, {
    get(target, property) {
      const fieldName = String(property);
      
      // Lazy register field
      if (!fields.has(fieldName)) {
        console.log(`Lazy registering field: ${fieldName}`);
        fields.set(fieldName, createField(fieldName, updateSubscriber));
      }
      
      return fields.get(fieldName);
    }
  });
}

function createField(name: string, updateSubscriber: (name: string) => void) {
  return {
    onChange: (e: any) => {
      console.log(`Field ${name} changed to:`, e.target.value);
      updateSubscriber(name);
    },
    onBlur: () => {
      console.log(`Field ${name} blurred`);
      updateSubscriber(name);
    },
    name,
    ref: (element: any) => {
      console.log(`Field ${name} ref attached`);
    }
  };
}

// 3. WATCH PROXY
function createWatchProxy<T>(
  getValues: () => T,
  subscribeToField: (name: keyof T) => void
) {
  return new Proxy({} as T, {
    get(target, property) {
      // Subscribe to this field
      subscribeToField(property as keyof T);
      
      // Return current value
      const values = getValues();
      return values[property as keyof T];
    }
  });
}

// Example usage in actual React component
function LoginForm() {
  const { register, handleSubmit, watch, formState } = useForm<{
    email: string;
    password: string;
  }>();
  
  /**
   * register() returns Proxy:
   * • onChange, onBlur, name, ref properties
   * • Automatically tracked and validated
   */
  
  /**
   * watch() returns Proxy:
   * • Access any field: watch().email
   * • Auto-subscribes to that field
   * • Re-renders only when subscribed fields change
   */
  const emailValue = watch().email;
  
  /**
   * formState is Proxy:
   * • Tracks which properties you access
   * • errors, isDirty, isValid, etc.
   * • Only re-renders when accessed properties change
   */
  
  return (
    <form onSubmit={handleSubmit(data => console.log(data))}>
      <input {...register('email')} />
      <input {...register('password')} type="password" />
      
      {formState.errors.email && <span>Email is required</span>}
      
      <button type="submit">Submit</button>
    </form>
  );
}

/**
 * 🚀 PERFORMANCE BENEFITS:
 * 
 * Without Proxy (traditional forms):
 * • All form components re-render on any change
 * • Need useState for each field
 * • Manual subscription management
 * 
 * With Proxy (RHF):
 * • Only components using changed fields re-render
 * • Automatic dependency tracking
 * • Zero re-renders for unused fields
 * 
 * Example:
 * • Form có 100 fields
 * • Component chỉ dùng "email"
 * • User gõ vào "password"
 * • Component KHÔNG re-render! (vì không watch password)
 */
```

---

### **4.3. Build Your Own Mini RHF with Proxy**

```typescript
/**
 * 🛠️ MINI REACT HOOK FORM (Educational)
 */

import { useState, useRef, useCallback } from 'react';

interface FieldConfig {
  value: any;
  ref: HTMLInputElement | null;
  touched: boolean;
  error?: string;
}

function useMiniForm<T extends Record<string, any>>(defaultValues: T) {
  const [values, setValues] = useState<T>(defaultValues);
  const [errors, setErrors] = useState<Partial<Record<keyof T, string>>>({});
  const fieldsRef = useRef<Map<keyof T, FieldConfig>>(new Map());
  const subscribersRef = useRef<Map<keyof T, Set<() => void>>>(new Map());
  
  // Track which component uses which fields
  const subscribeToField = useCallback((fieldName: keyof T, callback: () => void) => {
    if (!subscribersRef.current.has(fieldName)) {
      subscribersRef.current.set(fieldName, new Set());
    }
    subscribersRef.current.get(fieldName)!.add(callback);
    
    return () => {
      subscribersRef.current.get(fieldName)?.delete(callback);
    };
  }, []);
  
  // Notify subscribers when field changes
  const notifySubscribers = useCallback((fieldName: keyof T) => {
    subscribersRef.current.get(fieldName)?.forEach(callback => callback());
  }, []);
  
  // register() returns Proxy
  const register = useCallback((name: keyof T, validation?: (value: any) => string | undefined) => {
    return new Proxy({} as any, {
      get(target, property) {
        if (property === 'name') {
          return name;
        }
        
        if (property === 'value') {
          return values[name];
        }
        
        if (property === 'onChange') {
          return (e: React.ChangeEvent<HTMLInputElement>) => {
            const newValue = e.target.value;
            
            setValues(prev => ({ ...prev, [name]: newValue }));
            
            // Validate
            if (validation) {
              const error = validation(newValue);
              setErrors(prev => ({ ...prev, [name]: error }));
            }
            
            // Notify subscribers
            notifySubscribers(name);
          };
        }
        
        if (property === 'onBlur') {
          return () => {
            const field = fieldsRef.current.get(name);
            if (field) {
              field.touched = true;
            }
          };
        }
        
        if (property === 'ref') {
          return (element: HTMLInputElement) => {
            if (!fieldsRef.current.has(name)) {
              fieldsRef.current.set(name, {
                value: values[name],
                ref: element,
                touched: false
              });
            }
          };
        }
        
        return Reflect.get(target, property);
      }
    });
  }, [values, notifySubscribers]);
  
  // watch() returns Proxy
  const watch = useCallback(() => {
    const [, forceUpdate] = useState({});
    
    return new Proxy({} as T, {
      get(target, property) {
        // Subscribe to this field
        subscribeToField(property as keyof T, () => {
          forceUpdate({});
        });
        
        return values[property as keyof T];
      }
    });
  }, [values, subscribeToField]);
  
  const handleSubmit = useCallback((onSubmit: (data: T) => void) => {
    return (e: React.FormEvent) => {
      e.preventDefault();
      
      // Validate all fields
      let hasErrors = false;
      fieldsRef.current.forEach((field, name) => {
        if (!field.value) {
          setErrors(prev => ({ ...prev, [name]: 'Required' }));
          hasErrors = true;
        }
      });
      
      if (!hasErrors) {
        onSubmit(values);
      }
    };
  }, [values]);
  
  return {
    register,
    watch,
    handleSubmit,
    formState: {
      errors
    }
  };
}

// Usage
function ExampleForm() {
  const { register, watch, handleSubmit, formState } = useMiniForm({
    email: '',
    password: ''
  });
  
  const emailValue = watch().email; // Auto-subscribes!
  
  return (
    <form onSubmit={handleSubmit(data => console.log(data))}>
      <input
        {...register('email', (value) => {
          if (!value) return 'Email is required';
          if (!/\S+@\S+\.\S+/.test(value)) return 'Invalid email';
          return undefined;
        })}
        placeholder="Email"
      />
      {formState.errors.email && <span>{formState.errors.email}</span>}
      
      <input
        {...register('password', (value) => {
          if (!value) return 'Password is required';
          if (value.length < 6) return 'Password must be at least 6 characters';
          return undefined;
        })}
        type="password"
        placeholder="Password"
      />
      {formState.errors.password && <span>{formState.errors.password}</span>}
      
      <p>Current email: {emailValue}</p>
      
      <button type="submit">Submit</button>
    </form>
  );
}

/**
 * 🎯 HOW IT WORKS:
 * 
 * 1. register() tạo Proxy với các properties:
 *    • name, value, onChange, onBlur, ref
 *    • Spread vào <input {...register('email')} />
 * 
 * 2. onChange handler:
 *    • Update values state
 *    • Run validation
 *    • Notify subscribers
 * 
 * 3. watch() tạo Proxy:
 *    • Track which fields component uses
 *    • Subscribe to those fields
 *    • Re-render only when subscribed fields change
 * 
 * 4. Performance:
 *    • Component chỉ dùng email → chỉ re-render khi email thay đổi
 *    • Password changes → component KHÔNG re-render
 */
```

---

## **V. Performance Considerations**

### **5.1. Proxy Performance**

```typescript
/**
 * ⚡ PERFORMANCE COMPARISON
 */

// Benchmark: 1 million operations
const iterations = 1_000_000;

// 1. Direct property access
const directObj = { count: 0 };
console.time('Direct access');
for (let i = 0; i < iterations; i++) {
  directObj.count++;
}
console.timeEnd('Direct access');
// Direct access: ~5ms

// 2. Proxy access (minimal trap)
const proxyObj = new Proxy({ count: 0 }, {
  get: (target, prop) => Reflect.get(target, prop),
  set: (target, prop, value) => Reflect.set(target, prop, value)
});
console.time('Proxy access');
for (let i = 0; i < iterations; i++) {
  proxyObj.count++;
}
console.timeEnd('Proxy access');
// Proxy access: ~15ms (3x slower)

// 3. Proxy with logging (heavy trap)
const loggedProxyObj = new Proxy({ count: 0 }, {
  get: (target, prop) => {
    console.log(`Getting ${String(prop)}`); // Heavy operation!
    return Reflect.get(target, prop);
  },
  set: (target, prop, value) => {
    console.log(`Setting ${String(prop)} to ${value}`);
    return Reflect.set(target, prop, value);
  }
});
// Much slower due to logging overhead

/**
 * 📊 PERFORMANCE TIPS:
 * 
 * 1. Keep traps lightweight
 *    ❌ Heavy computation in traps
 *    ✅ Minimal logic, delegate to Reflect
 * 
 * 2. Cache Proxy instances
 *    ❌ new Proxy() in loops
 *    ✅ Create once, reuse
 * 
 * 3. Use Proxy only when needed
 *    ❌ Proxy everything
 *    ✅ Proxy for specific use cases (validation, reactivity)
 * 
 * 4. Avoid deep nesting
 *    ❌ Proxy wrapping Proxy wrapping Proxy
 *    ✅ Single-level Proxy when possible
 */
```

---

### **5.2. When NOT to Use Proxy**

```typescript
/**
 * ❌ BAD USE CASES FOR PROXY
 */

// 1. Hot paths (performance-critical code)
// ❌ Don't use Proxy in tight loops
for (let i = 0; i < 1_000_000; i++) {
  const proxy = new Proxy({}, {}); // Creating Proxy each iteration!
  proxy.value = i;
}

// ✅ Use plain objects instead
const obj = {};
for (let i = 0; i < 1_000_000; i++) {
  obj.value = i;
}

// 2. Simple validation
// ❌ Overkill for basic checks
const proxy = new Proxy({}, {
  set(target, prop, value) {
    if (typeof value !== 'number') throw new Error('Must be number');
    return Reflect.set(target, prop, value);
  }
});

// ✅ Just use a function
function setValue(obj, prop, value) {
  if (typeof value !== 'number') throw new Error('Must be number');
  obj[prop] = value;
}

// 3. Deep objects
// ❌ Proxy doesn't auto-wrap nested objects
const proxy = new Proxy({ nested: { value: 1 } }, {
  set(target, prop, value) {
    console.log('Set:', prop);
    return Reflect.set(target, prop, value);
  }
});

proxy.nested.value = 2; // Doesn't trigger set trap!

// ✅ Need recursive Proxy (complex, slow)
function deepProxy(obj) {
  return new Proxy(obj, {
    get(target, prop) {
      const value = Reflect.get(target, prop);
      if (typeof value === 'object' && value !== null) {
        return deepProxy(value); // Wrap nested objects
      }
      return value;
    }
  });
}
```

---

## **VI. Advanced Patterns**

### **6.1. Revocable Proxy**

```typescript
/**
 * 🔐 REVOCABLE PROXY - Can be disabled
 */

const target = { data: 'sensitive' };
const { proxy, revoke } = Proxy.revocable(target, {
  get(target, prop) {
    console.log(`Accessing ${String(prop)}`);
    return Reflect.get(target, prop);
  }
});

console.log(proxy.data); // Accessing data → "sensitive"

// Revoke access
revoke();

// console.log(proxy.data); // ❌ TypeError: Cannot perform 'get' on a proxy that has been revoked

/**
 * Use cases:
 * • Temporary access tokens
 * • Resource cleanup
 * • Security (revoke access after timeout)
 */
```

---

### **6.2. Proxy for API Mocking**

```typescript
/**
 * 🎭 API MOCK PROXY
 */

function createAPIMock<T extends Record<string, (...args: any[]) => any>>(
  mockResponses: Partial<T>
): T {
  return new Proxy({} as T, {
    get(target, property) {
      const endpoint = String(property);
      
      // Return mock function
      return (...args: any[]) => {
        console.log(`API call: ${endpoint}(${args.join(', ')})`);
        
        // Check if mock exists
        if (endpoint in mockResponses) {
          return mockResponses[endpoint as keyof T]!(...args);
        }
        
        // Default response
        return Promise.resolve({ success: true, data: null });
      };
    }
  });
}

// Usage
interface API {
  getUser: (id: number) => Promise<{ name: string; age: number }>;
  getPosts: () => Promise<{ id: number; title: string }[]>;
}

const mockAPI = createAPIMock<API>({
  getUser: async (id) => {
    console.log(`Fetching user ${id} (mocked)`);
    return { name: 'John', age: 25 };
  }
});

await mockAPI.getUser(1);  // API call: getUser(1) → { name: 'John', age: 25 }
await mockAPI.getPosts();  // API call: getPosts() → { success: true, data: null }
```

---

## **VII. Best Practices Summary**

```typescript
/**
 * ✅ PROXY BEST PRACTICES
 */

const bestPractices = {
  
  // 1. Always use Reflect in traps
  goodTrap: {
    set(target, prop, value, receiver) {
      return Reflect.set(target, prop, value, receiver); // ✅ Correct
    }
  },
  
  badTrap: {
    set(target, prop, value) {
      target[prop] = value; // ❌ Incorrect (loses receiver context)
      return true;
    }
  },
  
  // 2. Handle edge cases
  robustTrap: {
    get(target, prop, receiver) {
      // Check if property exists
      if (!(prop in target)) {
        console.warn(`Property ${String(prop)} not found`);
        return undefined;
      }
      
      return Reflect.get(target, prop, receiver);
    }
  },
  
  // 3. Return correct types from traps
  correctTypes: {
    set() { return true; },           // Boolean
    has() { return true; },            // Boolean
    deleteProperty() { return true; }, // Boolean
    get() { return 'value'; },         // Any value
    ownKeys() { return []; }           // Array
  },
  
  // 4. Cache Proxy instances
  cached: (() => {
    const cache = new WeakMap();
    
    return function getProxy(obj) {
      if (!cache.has(obj)) {
        cache.set(obj, new Proxy(obj, {}));
      }
      return cache.get(obj);
    };
  })(),
  
  // 5. Document Proxy behavior
  documented: new Proxy({}, {
    /**
     * Intercepts property reads
     * @returns Default value if property doesn't exist
     */
    get(target, prop) {
      return target[prop] ?? 'default';
    }
  })
};

/**
 * 🎯 WHEN TO USE PROXY:
 * 
 * ✅ Good use cases:
 * • Validation & type checking
 * • Reactive data systems (Vue, Mobx)
 * • Access control & privacy
 * • Logging & debugging
 * • Lazy initialization
 * • Default values
 * • API mocking
 * 
 * ❌ Bad use cases:
 * • Performance-critical loops
 * • Simple property access
 * • When Object.defineProperty suffices
 * • Deep object mutation (use Immer instead)
 */
```

---

## **📚 Related Questions**

