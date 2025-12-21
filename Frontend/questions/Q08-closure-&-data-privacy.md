# 🔐 Q08: Closure & Data Privacy

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (1-2 phút):**

**"Closure = hàm + môi trường từ vựng (các biến xung quanh nó). Hàm bên trong giữ tham chiếu đến biến scope bên ngoài.**

**📦 Core Concepts:**
- **Definition**: Function nhớ được và access được biến từ outer scope, ngay cả khi outer function đã return.
- **Mechanism**: Inner function giữ reference đến [[Scope]] (lexical environment) của outer function.
- **Data Privacy**: Dùng closure để tạo private variables/methods (encapsulation).

**🎯 Use Cases:**
1. **Private Variables**: Factory functions trả về object với methods access private state.
2. **Module Pattern**: IIFE + closure → private state + public API.
3. **Event Handlers**: Callback giữ reference đến outer variables.
4. **Partial Application**: Currying, function factories (e.g., `makeAdder(5)`).
5. **Memoization**: Cache results của expensive functions.

**⚠️ Common Pitfalls:**
- **Memory Leaks**: Closure giữ reference → biến không bị GC → memory leak nếu không cleanup.
  ```js
  function setupButton() {
    const hugeArray = new Array(1000000); // 8MB
    document.getElementById('btn').onclick = () => {
      console.log(hugeArray.length); // Closure giữ reference → không GC!
    };
  }
  // Fix: Xóa reference khi không dùng
  ```
- **Loop + Closures**: `var` trong loop → mọi closure chia sẻ cùng biến.
  ```js
  // ❌ Sai
  for (var i = 0; i < 3; i++) {
    setTimeout(() => console.log(i), 100); // 3, 3, 3
  }
  // ✅ Đúng: Dùng let (block scope) hoặc IIFE
  for (let i = 0; i < 3; i++) {
    setTimeout(() => console.log(i), 100); // 0, 1, 2
  }
  ```

**💡 Senior Insights:**
- **Performance**: Closures có overhead nhỏ (memory + lookup time), nhưng negligible trong hầu hết cases.
- **DevTools**: Chrome DevTools → Memory Profiler → check closure retaining objects.
- **ES6 Modules**: Replace IIFE module pattern → native private scope.
- **WeakMap**: Alternative cho private data không dùng closure → auto GC khi object không còn reference.

---

**⚡ Quick Summary:**
> Closure = function nhớ được biến từ outer scope ngay cả khi outer function đã return. Dùng để private data

**💡 Ghi Nhớ:**
- 🔥 **Definition**: Function + Lexical Environment (biến xung quanh nó)
- 🎯 **Use Cases**: Private variables, Factory functions, Callbacks, Event handlers
- ⚡ **Memory**: Closure giữ reference → biến không bị GC → cẩn thận memory leak
- 📦 **Module Pattern**: IIFE + Closure = private state

**Trả lời:**

- **Closure**: Function có thể access variables từ outer scope ngay cả khi outer function đã return
- **Data Privacy**: Sử dụng closure để tạo private variables
- **Hoạt động**: Inner function giữ reference đến outer scope
- **Ưu điểm**: Encapsulation, data privacy, module pattern
- **Nhược điểm**: Có thể gây memory leaks nếu không quản lý tốt

**Code Example:**

```typescript
// 🔹 Basic Closure (Closure cơ bản)
function outerFunction(x: number) {  // 📦 Outer function
  // 🔹 Outer scope variable (biến scope ngoài)
  let outerVariable = x;  // 💾 Biến này sẽ được "nhớ" bởi inner function

  // 🔹 Inner function (closure) - Hàm bên trong
  function innerFunction(y: number): number {
    return outerVariable + y;  // ✅ Access outer variable (truy cập biến bên ngoài)
    // Inner function "đóng" (close over) biến outerVariable
    // → Tạo thành closure (hàm + lexical environment)
  }

  return innerFunction;  // 🎁 Trả về inner function (nhưng vẫn giữ reference đến outerVariable)
}

const closure = outerFunction(10);  // 🏗️ Gọi outer function → trả về inner function
console.log(closure(5)); // 15  // ✅ outerFunction đã return nhưng innerFunction vẫn access được outerVariable!
// 🔑 Key point: outerVariable vẫn "sống" trong memory vì closure giữ reference

// 🔐 Data Privacy với Closure (Tạo private variables)
function createCounter(): { increment: () => number; getCount: () => number } {
  let count = 0;  // 🔒 Private variable (biến private - không access trực tiếp từ bên ngoài)
  // count chỉ có thể access qua methods được return

  return {  // 📦 Return object với public methods
    increment(): number {  // 🔼 Public method để tăng count
      return ++count;  // ✅ Access private variable (closure giữ reference)
    },
    getCount(): number {  // 👁️ Public method để đọc count
      return count;  // ✅ Access private variable
    },
  };
  // 🎯 Bên ngoài KHÔNG thể trực tiếp sửa count, chỉ qua increment()
}

const counter = createCounter();  // 🏗️ Tạo instance mới
console.log(counter.increment()); // 1  // 🔼 Tăng lên 1
console.log(counter.increment()); // 2  // 🔼 Tăng lên 2
console.log(counter.getCount()); // 2   // 👁️ Đọc giá trị
// console.log(counter.count);     // ❌ Error: count is private (không tồn tại property này)

// 📦 Module Pattern (IIFE + Closure)
const userModule = (() => {  // 🔹 IIFE (Immediately Invoked Function Expression)
  let users: string[] = [];  // 🔒 Private data (array private - không access từ bên ngoài)
  // users chỉ access được qua public methods bên dưới

  return {  // 🎁 Return object với public API
    addUser(name: string): void {  // ➕ Public method: Thêm user
      users.push(name);  // ✅ Access private array
    },
    getUsers(): string[] {  // 📋 Public method: Lấy users
      return [...users];  // ✅ Return copy (spread operator) - không expose reference gốc
      // Trả về copy để bảo vệ private array (bên ngoài không sửa được original)
    },
    getUserCount(): number {  // 🔢 Public method: Đếm số users
      return users.length;  // ✅ Access private array length
    },
  };
})();  // 🔥 () cuối cùng = gọi ngay lập tức (IIFE)
// → Function chạy ngay, return object, gán vào userModule

userModule.addUser('John');  // ➕ Thêm user "John"
userModule.addUser('Jane');  // ➕ Thêm user "Jane"
console.log(userModule.getUsers()); // ["John", "Jane"]  // 📋 Lấy danh sách
console.log(userModule.getUserCount()); // 2  // 🔢 Đếm users
// 🔒 users array is private - không thể access userModule.users
```

**Best Practices:**

- Sử dụng closure cho data privacy
- Sử dụng module pattern
- Tránh memory leaks
- Sử dụng TypeScript cho type safety

**Mistakes:**

```typescript
// ❌ Sai: Không hiểu closure scope với var trong loop
for (var i = 0; i < 3; i++) {  // 🔴 var = function scope (không phải block scope)
  setTimeout(() => console.log(i), 100);  // ❌ 3, 3, 3 (cả 3 closures đều share cùng biến i)
  // Khi setTimeout callback chạy (sau 100ms), loop đã chạy xong → i = 3
  // Tất cả 3 closures đều reference đến CÙNG biến i → in ra 3, 3, 3
}

// ✅ Đúng: Sử dụng let (block scope - ES6)
for (let i = 0; i < 3; i++) {  // 🟢 let = block scope (mỗi iteration có i riêng)
  setTimeout(() => console.log(i), 100);  // ✅ 0, 1, 2
  // Mỗi iteration tạo ra một block scope mới với biến i riêng
  // → 3 closures khác nhau, mỗi cái giữ i riêng (0, 1, 2)
}

// ✅ Cách khác: Sử dụng IIFE (Immediately Invoked Function Expression) với var
for (var i = 0; i < 3; i++) {  // 🔴 var vẫn dùng được nếu wrap trong IIFE
  ((index: number) => {  // 🔹 IIFE tạo scope mới, capture giá trị i hiện tại
    setTimeout(() => console.log(index), 100);  // ✅ 0, 1, 2
    // Mỗi IIFE có parameter index riêng (copy từ i tại thời điểm đó)
    // → 3 closures khác nhau với index = 0, 1, 2
  })(i);  // 🎯 Truyền i hiện tại vào IIFE
}
// 💡 Nhưng trong thực tế, nên dùng let (đơn giản hơn, rõ ràng hơn)
```

#### Vì sao Redux/Zustand dùng closure để lưu trạng thái?

- **🔒 Encapsulation (đóng gói state an toàn)**: State sống trong phạm vi từ vựng (lexical scope) của store, không thể bị thay đổi trực tiếp từ bên ngoài nếu không đi qua API công khai (getState, setState, subscribe). Tránh lộ biến toàn cục và hạn chế đột biến ngoài ý muốn.
  
- **📦 API nhỏ gọn, không cần lớp/phụ trợ**: Một factory function tạo store trả về các hàm thao tác; closure giữ state và danh sách listeners. Không bắt buộc dùng class/this, giảm rủi ro context.
  
- **⚡ Hiệu năng dự đoán được**: Không cần Proxy hay getter/setter; cập nhật state là thao tác thuần (immutable/mutable tùy chiến lược), thông báo qua danh sách subscribers trong cùng closure → chi phí thấp, dễ tối ưu.
  
- **🏗️ Khả năng multiple store độc lập**: Mỗi lần gọi factory tạo một scope mới với state riêng, không rò rỉ chéo. Dễ tạo nhiều store, test theo từng instance.

Ví dụ mô phỏng (đơn giản hóa theo phong cách Zustand):

```ts
type Listener<T> = (state: T, prev: T) => void;  // 📡 Kiểu hàm lắng nghe (callback khi state thay đổi)

function createStore<T>(  // 🏗️ Factory function tạo store
  initializer: (  // 🎛️ Hàm khởi tạo state (nhận set, get)
    set: (p: Partial<T> | ((s: T) => Partial<T>)) => void,  // 🔧 Hàm set state
    get: () => T  // 👁️ Hàm get state
  ) => T
) {
  let state: T;  // 🔒 PRIVATE state (closure variable - chỉ access qua get/set)
  const listeners = new Set<Listener<T>>();  // 📡 PRIVATE listeners (danh sách callbacks)
  // state và listeners được "closure" bởi các hàm bên dưới

  const get = () => state;  // 👁️ Getter: Trả về state hiện tại
  
  const set = (patch: Partial<T> | ((s: T) => Partial<T>)) => {  // 🔧 Setter: Cập nhật state
    const prev = state;  // 💾 Lưu state cũ (cho listeners)
    const next =  // 🎯 Tính state mới
      typeof patch === 'function'  // ❓ Kiểm tra patch là function hay object
        ? (patch as (s: T) => Partial<T>)(prev)  // 🔧 Nếu là function: gọi với prev
        : patch;  // 📦 Nếu là object: dùng luôn
    state = { ...prev, ...next };  // 🔄 Merge state (immutable update)
    listeners.forEach((l) => l(state, prev));  // 📢 Thông báo cho tất cả listeners
  };

  state = initializer(set, get);  // 🎛️ Khởi tạo state ban đầu (gọi initializer)

  return {  // 🎁 Return PUBLIC API (object với 3 methods)
    getState: get,  // 👁️ Public getter
    setState: set,  // 🔧 Public setter
    subscribe(listener: Listener<T>) {  // 📡 Đăng ký listener
      listeners.add(listener);  // ➕ Thêm vào Set
      return () => listeners.delete(listener);  // 🗄️ Return unsubscribe function
    },
  };
  // 🔑 KEY: state và listeners là PRIVATE (chỉ access qua getState/setState/subscribe)
  // → Bên ngoài KHÔNG thể trực tiếp sửa state, phải qua setState
}
```

So với lựa chọn khác:

- **🏛️ Class + this**: Cần ràng buộc ngữ cảnh (bind context), dễ lỗi khi truyền phương thức; khó tree-shake hơn nếu không cẩn thận.
  ```ts
  // ❌ Vấn đề với class:
  class Store {
    state = { count: 0 };
    increment() {
      this.state.count++;  // 💀 'this' có thể bị lose khi truyền method
    }
  }
  const store = new Store();
  const { increment } = store;  // 🚨 Destructure làm mất 'this' binding
  increment();  // ❌ Error: Cannot read 'state' of undefined
  ```
  
- **🧙 Proxy**: Tiện reactive nhưng tốn chi phí bẫy (traps), phức tạp debug, không cần thiết khi chỉ cần pub/sub đơn giản.
  ```ts
  // 🧙 Proxy overhead:
  const state = new Proxy({ count: 0 }, {
    get(target, prop) {  // ⚡ Mỗi lần access property đều gọi trap
      console.log(`Get ${String(prop)}`);  // 🚨 Performance cost
      return target[prop];
    },
  });
  ```
  
- **🌍 Global singleton**: Dễ rò rỉ state giữa tests/SSR, khó tạo nhiều instance độc lập.
  ```ts
  // ❌ Vấn đề với global:
  const globalStore = { state: {} };  // 🌍 Global variable
  // 🚨 Tests share cùng state → side effects giữa tests
  // 🚨 SSR: Server-side và client-side share state → data leaks
  ```

📊 **Tại sao Closure thắng:**
- ✅ **Simple**: Không cần class, proxy, global
- ✅ **Safe**: Private state, không rò rỉ context
- ✅ **Fast**: Không có traps/overhead, chỉ là function calls
- ✅ **Flexible**: Dễ tạo multiple instances, test isolation
- ✅ **Predictable**: Pure JavaScript, không magic

