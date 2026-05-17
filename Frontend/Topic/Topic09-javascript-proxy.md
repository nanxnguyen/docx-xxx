# Topic 09: JavaScript Proxy - Meta Programming & Use Cases

## 🚀 Câu trả lời ngắn gọn

**Proxy** là tính năng JavaScript cho phép bọc một object/function và **chặn các thao tác** như đọc property, ghi property, kiểm tra `in`, xóa property, gọi function, gọi `new`, liệt kê keys.

```ts
const proxy = new Proxy(target, handler);
```

Trong đó:

```txt
🎯 target  -> object/function gốc
🪤 handler -> nơi định nghĩa các trap
🪞 trap    -> hàm chặn hành vi như get, set, has, apply
```

Proxy thường dùng cho:

```txt
✅ validation
✅ logging/debugging
✅ reactivity như Vue 3
✅ form state tracking như React Hook Form
✅ access control
✅ lazy loading
✅ API mocking
✅ default value/fallback
```

> **Highlight:** Proxy mạnh vì nó can thiệp được vào **hành vi của object**, không chỉ dữ liệu của object.

---

## 🧠 1. Proxy hoạt động như thế nào?

Ví dụ cơ bản:

```ts
const user = {
  name: 'An',
  age: 25,
};

const proxyUser = new Proxy(user, {
  get(target, property, receiver) {
    console.log(`Read ${String(property)}`);
    return Reflect.get(target, property, receiver);
  },

  set(target, property, value, receiver) {
    console.log(`Write ${String(property)} = ${value}`);
    return Reflect.set(target, property, value, receiver);
  },
});

proxyUser.name; // Read name
proxyUser.age = 26; // Write age = 26
```

Flow:

```txt
proxy.name
 -> get trap chạy
 -> Reflect.get lấy giá trị thật từ target
 -> trả kết quả
```

> **Highlight:** Code bên ngoài dùng `proxy` như object bình thường, nhưng mọi thao tác có thể bị intercept.

---

## 🪞 2. Reflect API là gì?

`Reflect` cung cấp hành vi mặc định tương ứng với các trap của Proxy.

Không nên tự làm:

```ts
get(target, property) {
  return target[property];
}
```

Nên dùng:

```ts
get(target, property, receiver) {
  return Reflect.get(target, property, receiver);
}
```

Lý do:

- giữ đúng behavior gốc
- xử lý `receiver` đúng với prototype/getter
- API nhất quán
- tránh bug khi object có inheritance hoặc accessor

Ví dụ `set`:

```ts
set(target, property, value, receiver) {
  if (property === 'age' && typeof value !== 'number') {
    throw new TypeError('age must be a number');
  }

  return Reflect.set(target, property, value, receiver);
}
```

> **Highlight senior:** Trong trap, ưu tiên dùng `Reflect.*` để forward operation thay vì thao tác trực tiếp trên `target`.

---

## 🪤 3. Các trap quan trọng

Bạn không cần học thuộc toàn bộ 13 trap, nhưng cần biết nhóm quan trọng.

### 📖 `get` - chặn đọc property

```ts
const config = new Proxy(
  { apiUrl: '/api' },
  {
    get(target, property, receiver) {
      if (!(property in target)) {
        throw new Error(`Missing config: ${String(property)}`);
      }

      return Reflect.get(target, property, receiver);
    },
  }
);

config.apiUrl; // "/api"
config.timeout; // Error
```

Dùng cho:

```txt
default value
lazy loading
logging
dependency tracking
safe config access
```

### ✍️ `set` - chặn ghi property

```ts
const user = new Proxy(
  { name: 'An', age: 25 },
  {
    set(target, property, value, receiver) {
      if (property === 'age' && value < 0) {
        throw new Error('age must be positive');
      }

      return Reflect.set(target, property, value, receiver);
    },
  }
);

user.age = 30; // ok
user.age = -1; // Error
```

Dùng cho:

```txt
validation
reactivity
dirty tracking
audit log
```

### 🔎 `has` - chặn toán tử `in`

```ts
const user = new Proxy(
  { name: 'An', _token: 'secret' },
  {
    has(target, property) {
      if (String(property).startsWith('_')) {
        return false;
      }

      return Reflect.has(target, property);
    },
  }
);

'name' in user; // true
'_token' in user; // false
```

### 🗑️ `deleteProperty` - chặn `delete`

```ts
const user = new Proxy(
  { id: 1, name: 'An' },
  {
    deleteProperty(target, property) {
      if (property === 'id') {
        throw new Error('Cannot delete id');
      }

      return Reflect.deleteProperty(target, property);
    },
  }
);
```

### 🔑 `ownKeys` - chặn `Object.keys`, `Reflect.ownKeys`

```ts
const user = new Proxy(
  { name: 'An', _password: 'secret' },
  {
    ownKeys(target) {
      return Reflect.ownKeys(target).filter(
        (key) => !String(key).startsWith('_')
      );
    },
  }
);

Object.keys(user); // ["name"]
```

### 📞 `apply` - chặn gọi function

```ts
function sum(a: number, b: number) {
  return a + b;
}

const loggedSum = new Proxy(sum, {
  apply(target, thisArg, args) {
    console.log('called with', args);
    return Reflect.apply(target, thisArg, args);
  },
});

loggedSum(1, 2); // 3
```

Dùng cho:

```txt
logging
memoization
rate limit
permission check
```

### 🏗️ `construct` - chặn `new`

```ts
class Service {
  constructor(public name: string) {}
}

const ServiceProxy = new Proxy(Service, {
  construct(target, args, newTarget) {
    console.log('creating service', args);
    return Reflect.construct(target, args, newTarget);
  },
});

new ServiceProxy('api');
```

---

## 🧩 4. Proxy invariants - luật không được phá

Proxy không được nói dối trái với constraint của target.

Ví dụ property không configurable thì trap không được giấu sai cách.

```ts
const target = {};

Object.defineProperty(target, 'id', {
  value: 1,
  configurable: false,
});

const proxy = new Proxy(target, {
  ownKeys() {
    return []; // có thể gây TypeError vì giấu non-configurable key
  },
});
```

Senior cần biết: Proxy mạnh nhưng vẫn bị ràng buộc bởi **invariants** của JavaScript engine để giữ object model nhất quán.

> **Highlight:** Nếu trap trả kết quả vi phạm invariant, runtime sẽ throw `TypeError`.

---

## 🔥 5. Use case thực tế

### ✅ Validation

```ts
type User = {
  name: string;
  age: number;
};

const user = new Proxy<User>(
  { name: 'An', age: 25 },
  {
    set(target, property, value, receiver) {
      if (property === 'name' && typeof value !== 'string') {
        throw new TypeError('name must be string');
      }

      if (property === 'age' && typeof value !== 'number') {
        throw new TypeError('age must be number');
      }

      return Reflect.set(target, property, value, receiver);
    },
  }
);
```

### 🧾 Logging/debugging

```ts
function createLoggedObject<T extends object>(target: T): T {
  return new Proxy(target, {
    get(target, property, receiver) {
      console.log('get', String(property));
      return Reflect.get(target, property, receiver);
    },
    set(target, property, value, receiver) {
      console.log('set', String(property), value);
      return Reflect.set(target, property, value, receiver);
    },
  });
}
```

### 🧠 Reactivity đơn giản

```ts
function reactive<T extends object>(target: T, onChange: () => void): T {
  return new Proxy(target, {
    set(target, property, value, receiver) {
      const oldValue = Reflect.get(target, property, receiver);
      const result = Reflect.set(target, property, value, receiver);

      if (oldValue !== value) {
        onChange();
      }

      return result;
    },
  });
}

const state = reactive({ count: 0 }, () => {
  console.log('state changed');
});

state.count++;
```

Đây là ý tưởng nền tảng của reactivity, nhưng framework thật như Vue 3 phức tạp hơn nhiều: track dependency khi `get`, trigger effect khi `set`.

### 🧾 Form state tracking

Proxy có thể dùng để track field nào được đọc hoặc thay đổi.

Ý tưởng:

```ts
const formState = new Proxy(
  { isDirty: false, errors: {}, touchedFields: {} },
  {
    get(target, property, receiver) {
      console.log('component subscribed to', String(property));
      return Reflect.get(target, property, receiver);
    },
  }
);
```

Trong các form library, proxy giúp chỉ subscribe vào phần state component thật sự đọc, giảm re-render không cần thiết.

> **Highlight:** React Hook Form tận dụng proxy-style tracking để tối ưu form state subscription, không phải render lại toàn bộ form mỗi lần một field đổi.

### 🔐 Access control

```ts
function createSecureObject<T extends object>(
  target: T,
  allowedKeys: Set<PropertyKey>
): T {
  return new Proxy(target, {
    get(target, property, receiver) {
      if (!allowedKeys.has(property)) {
        throw new Error(`Access denied: ${String(property)}`);
      }

      return Reflect.get(target, property, receiver);
    },
  });
}
```

Lưu ý: đây là runtime guard, không thay thế security thật ở backend.

---

## 🆚 6. Proxy vs Object.defineProperty

| Tiêu chí | Object.defineProperty | Proxy |
|---|---|---|
| Chặn đọc/ghi property có sẵn | Có | Có |
| Chặn property mới | Không tốt | Có |
| Chặn delete, in, Object.keys | Không | Có |
| Chặn array index/length tốt | Hạn chế | Tốt hơn |
| Dễ support IE11 | Có | Không |
| Dùng trong Vue | Vue 2 | Vue 3 |

Vue 2 dùng `Object.defineProperty`, nên khó detect:

```txt
thêm property mới
xóa property
array index change
```

Vue 3 dùng Proxy nên reactivity tổng quát hơn.

---

## 🧨 7. Performance và trade-off

Proxy có overhead vì mỗi operation phải đi qua trap.

Không nên dùng Proxy cho:

```txt
❌ hot path cần performance cực cao
❌ loop lớn đọc/ghi hàng triệu lần
❌ object đơn giản không cần intercept
❌ data structure performance-critical
```

Nên dùng Proxy khi:

```txt
✅ cần metaprogramming
✅ cần runtime validation/logging
✅ cần dependency tracking/reactivity
✅ cần API đẹp hơn cho library/framework
```

> **Highlight:** Proxy là công cụ thiết kế abstraction mạnh, không phải replacement cho object thường.

---

## 🧯 8. Pitfalls thường gặp

### ⚠️ Quên return boolean trong `set`

`set` trap nên return `true/false`.

```ts
set(target, property, value, receiver) {
  return Reflect.set(target, property, value, receiver);
}
```

Trong strict mode, return `false` có thể gây `TypeError`.

### ⚠️ Dùng `target[property]` thay vì Reflect

Có thể sai với getter/setter, prototype hoặc receiver.

### ⚠️ Proxy không tự deep proxy

```ts
const state = new Proxy({ user: { name: 'An' } }, handler);

state.user.name = 'Binh'; // nested object không tự bị proxy nếu chưa wrap
```

Muốn deep reactivity phải tạo proxy cho nested object.

### ⚠️ Proxy identity khác target

```ts
const target = {};
const proxy = new Proxy(target, {});

proxy === target; // false
```

Điều này ảnh hưởng cache, Map key, Set, referential equality.

### ⚠️ Khó debug

Proxy che hành vi thật của object, stack trace và log có thể khó hiểu hơn.

---

## 🔌 9. Revocable Proxy

`Proxy.revocable()` tạo proxy có thể vô hiệu hóa.

```ts
const { proxy, revoke } = Proxy.revocable(
  { token: 'abc' },
  {
    get(target, property, receiver) {
      return Reflect.get(target, property, receiver);
    },
  }
);

proxy.token; // "abc"

revoke();

proxy.token; // TypeError
```

Dùng cho:

```txt
cleanup
security boundary
temporary access
plugin sandbox
```

---

## 🎤 10. Câu trả lời senior nên nói

**"Proxy là cơ chế meta programming cho phép wrap object hoặc function để intercept operation như get, set, has, deleteProperty, ownKeys, apply và construct. Khi viết trap nên dùng Reflect để forward hành vi mặc định đúng với receiver/prototype. Proxy hữu ích cho validation, logging, access control, lazy loading, reactivity như Vue 3 và form state tracking như React Hook Form. Tuy nhiên Proxy có overhead, khó debug, không tự deep proxy nested object và có invariant của JS engine không được vi phạm. Em chỉ dùng Proxy khi cần abstraction/runtime interception thật sự, không dùng thay object thường trong hot path performance-critical."**

---

## ✅ 11. Checklist phỏng vấn

```txt
□ Biết Proxy = wrapper intercept object/function operations
□ Biết syntax new Proxy(target, handler)
□ Biết trap là gì
□ Biết get/set/has/deleteProperty/ownKeys/apply/construct
□ Biết Reflect dùng để forward default behavior
□ Biết set trap cần return boolean
□ Biết Proxy invariants có thể throw TypeError
□ Biết Proxy không tự deep proxy nested object
□ Biết proxy !== target
□ Biết Vue 3 dùng Proxy, Vue 2 dùng Object.defineProperty
□ Biết React Hook Form/form library dùng proxy-style subscription để giảm re-render
□ Biết use cases: validation, logging, reactivity, access control
□ Biết performance overhead và không dùng cho hot path
□ Biết Revocable Proxy
□ Biết Proxy không thay thế backend security
```
