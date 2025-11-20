# 🔐 Q14: Closure & Data Privacy




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
// Basic Closure
function outerFunction(x: number) {
  // Outer scope variable
  let outerVariable = x;

  // Inner function (closure)
  function innerFunction(y: number): number {
    return outerVariable + y; // Access outer variable
  }

  return innerFunction;
}

const closure = outerFunction(10);
console.log(closure(5)); // 15
// outerFunction đã return nhưng innerFunction vẫn access được outerVariable

// Data Privacy với Closure
function createCounter(): { increment: () => number; getCount: () => number } {
  let count = 0; // Private variable

  return {
    increment(): number {
      return ++count; // Access private variable
    },
    getCount(): number {
      return count; // Access private variable
    },
  };
}

const counter = createCounter();
console.log(counter.increment()); // 1
console.log(counter.increment()); // 2
console.log(counter.getCount()); // 2
// console.log(counter.count);     // ❌ Error: count is private

// Module Pattern
const userModule = (() => {
  let users: string[] = []; // Private data

  return {
    addUser(name: string): void {
      users.push(name);
    },
    getUsers(): string[] {
      return [...users]; // Return copy
    },
    getUserCount(): number {
      return users.length;
    },
  };
})();

userModule.addUser('John');
userModule.addUser('Jane');
console.log(userModule.getUsers()); // ["John", "Jane"]
console.log(userModule.getUserCount()); // 2
// users array is private
```

**Best Practices:**

- Sử dụng closure cho data privacy
- Sử dụng module pattern
- Tránh memory leaks
- Sử dụng TypeScript cho type safety

**Mistakes:**

```typescript
// ❌ Sai: Không hiểu closure scope
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100); // 3, 3, 3
}

// ✅ Đúng: Sử dụng closure đúng cách
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100); // 0, 1, 2
}

// Hoặc sử dụng closure với var
for (var i = 0; i < 3; i++) {
  ((index: number) => {
    setTimeout(() => console.log(index), 100); // 0, 1, 2
  })(i);
}
```

#### Vì sao Redux/Zustand dùng closure để lưu trạng thái?

- **Encapsulation (đóng gói state an toàn)**: State sống trong phạm vi từ vựng (lexical scope) của store, không thể bị thay đổi trực tiếp từ bên ngoài nếu không đi qua API công khai (getState, setState, subscribe). Tránh lộ biến toàn cục và hạn chế đột biến ngoài ý muốn.
- **API nhỏ gọn, không cần lớp/phụ trợ**: Một factory function tạo store trả về các hàm thao tác; closure giữ state và danh sách listeners. Không bắt buộc dùng class/this, giảm rủi ro context.
- **Hiệu năng dự đoán được**: Không cần Proxy hay getter/setter; cập nhật state là thao tác thuần (immutable/mutable tùy chiến lược), thông báo qua danh sách subscribers trong cùng closure → chi phí thấp, dễ tối ưu.
- **Khả năng multiple store độc lập**: Mỗi lần gọi factory tạo một scope mới với state riêng, không rò rỉ chéo. Dễ tạo nhiều store, test theo từng instance.

Ví dụ mô phỏng (đơn giản hóa theo phong cách Zustand):

```ts
type Listener<T> = (state: T, prev: T) => void;

function createStore<T>(
  initializer: (
    set: (p: Partial<T> | ((s: T) => Partial<T>)) => void,
    get: () => T
  ) => T
) {
  let state: T;
  const listeners = new Set<Listener<T>>();

  const get = () => state;
  const set = (patch: Partial<T> | ((s: T) => Partial<T>)) => {
    const prev = state;
    const next =
      typeof patch === 'function'
        ? (patch as (s: T) => Partial<T>)(prev)
        : patch;
    state = { ...prev, ...next };
    listeners.forEach((l) => l(state, prev));
  };

  state = initializer(set, get);

  return {
    getState: get,
    setState: set,
    subscribe(listener: Listener<T>) {
      listeners.add(listener);
      return () => listeners.delete(listener);
    },
  };
}
```

So với lựa chọn khác:

- **Class + this**: Cần ràng buộc ngữ cảnh, dễ lỗi khi truyền phương thức; khó tree-shake hơn nếu không cẩn thận.
- **Proxy**: Tiện reactive nhưng tốn chi phí bẫy (traps), phức tạp debug, không cần thiết khi chỉ cần pub/sub đơn giản.
- **Global singleton**: Dễ rò rỉ state giữa tests/SSR, khó tạo nhiều instance độc lập.

