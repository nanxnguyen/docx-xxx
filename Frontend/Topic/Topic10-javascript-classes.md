# Topic10: JavaScript Classes

## ⭐ Mục tiêu phỏng vấn Senior/Staff

> **JavaScript class không phải là class kiểu Java/C# thuần túy. Nó là cú pháp hiện đại trên prototype-based inheritance, giúp code OOP dễ đọc hơn nhưng vẫn chạy dựa trên prototype chain.**

Khi phỏng vấn senior/staff, cần trả lời được:

- 🧠 Class trong JS thật sự hoạt động như thế nào.
- 🔗 `extends`, `super`, prototype chain chạy ra sao.
- 🔒 Private fields `#field` khác `_field` thế nào.
- 🏗️ Khi nào dùng inheritance, khi nào nên dùng composition.
- ⚠️ Các lỗi thực tế: `this`, callback, deep inheritance, mutable state.
- 🧩 Cách liên hệ với React/Frontend architecture.

---

## 1. 🏛️ Class Là Gì?

**Class trong JavaScript là syntactic sugar trên constructor function và prototype.**

Ví dụ:

```ts
class User {
  constructor(name: string) {
    this.name = name;
  }

  sayHi() {
    return `Hi, ${this.name}`;
  }
}

const user = new User("Anna");
user.sayHi();
```

Về bản chất gần giống:

```ts
function User(name) {
  this.name = name;
}

User.prototype.sayHi = function () {
  return `Hi, ${this.name}`;
};
```

### 🔥 Highlight

> **Class syntax mới hơn, dễ đọc hơn, nhưng mental model vẫn là prototype.**

---

## 2. 🧠 Những Điểm Cần Nhớ Về Class

### ✅ Class thực chất là function

```ts
class User {}

typeof User; // "function"
```

Class được gọi bằng `new`:

```ts
const user = new User();
```

Nếu gọi class như function sẽ lỗi:

```ts
User(); // TypeError
```

### ✅ Method nằm trên prototype

```ts
class User {
  login() {}
}

const a = new User();
const b = new User();

a.login === b.login; // true
```

`login` không được copy vào từng object. Nó được share qua `User.prototype`.

### ✅ Class method không enumerable

```ts
Object.keys(new User()); // không thấy login
```

Điểm này khác với việc gán method trực tiếp vào object.

### ✅ Class declaration có Temporal Dead Zone

```ts
new User(); // ReferenceError

class User {}
```

Không nên nói đơn giản là class "hoisted giống function declaration". Thực tế tên class có binding nhưng không dùng được trước khi khai báo.

---

## 3. 🏗️ Constructor

`constructor` dùng để khởi tạo state ban đầu cho instance.

```ts
class Product {
  constructor(
    public id: string,
    public name: string,
    public price: number
  ) {}
}

const product = new Product("p1", "Keyboard", 100);
```

Trong JavaScript thuần:

```ts
class Product {
  constructor(id, name, price) {
    this.id = id;
    this.name = name;
    this.price = price;
  }
}
```

### ⚠️ Lưu ý

Constructor nên làm việc đơn giản:

- Gán state ban đầu.
- Validate input cơ bản.
- Không nên gọi API.
- Không nên làm side effect nặng.
- Không nên chứa business logic phức tạp.

> **Constructor càng nặng, object càng khó test và khó tái sử dụng.**

---

## 4. 🔗 Prototype Chain

Khi gọi:

```ts
user.sayHi();
```

JavaScript tìm method theo thứ tự:

```txt
user
  -> User.prototype
  -> Object.prototype
  -> null
```

Ví dụ:

```ts
class User {
  sayHi() {
    return "hi";
  }
}

const user = new User();

Object.getPrototypeOf(user) === User.prototype; // true
```

### 🔥 Highlight

> **Muốn hiểu class trong JS, phải hiểu prototype chain. Class chỉ là cú pháp đẹp hơn.**

---

## 5. 🧬 Inheritance Với `extends`

`extends` tạo quan hệ kế thừa giữa class con và class cha.

```ts
class User {
  constructor(public name: string) {}

  login() {
    return `${this.name} logged in`;
  }
}

class Admin extends User {
  deleteUser(userId: string) {
    return `Deleted ${userId}`;
  }
}

const admin = new Admin("Root");

admin.login();
admin.deleteUser("u1");
```

Prototype chain:

```txt
admin
  -> Admin.prototype
  -> User.prototype
  -> Object.prototype
  -> null
```

---

## 6. 📞 `super()`

Trong class con, nếu có `constructor`, phải gọi `super()` trước khi dùng `this`.

```ts
class Admin extends User {
  constructor(name: string, public role: string) {
    super(name);
  }
}
```

Sai:

```ts
class Admin extends User {
  constructor(name: string) {
    this.name = name; // ReferenceError
    super(name);
  }
}
```

`super()` gọi constructor của parent.

`super.method()` gọi method của parent:

```ts
class Admin extends User {
  login() {
    const result = super.login();
    return `${result} as admin`;
  }
}
```

### 🔥 Highlight

> **Trong subclass, `super()` phải chạy trước `this` vì parent cần khởi tạo instance trước.**

---

## 7. 🎭 Polymorphism

Polymorphism nghĩa là cùng một interface/method name nhưng behavior khác nhau.

```ts
class PaymentMethod {
  pay(amount: number) {
    throw new Error("Not implemented");
  }
}

class CreditCard extends PaymentMethod {
  pay(amount: number) {
    return `Paid ${amount} by card`;
  }
}

class Paypal extends PaymentMethod {
  pay(amount: number) {
    return `Paid ${amount} by PayPal`;
  }
}

function checkout(method: PaymentMethod) {
  return method.pay(100);
}
```

Code gọi `checkout` không cần biết payment cụ thể là gì.

Trong TypeScript, thường dùng interface thay vì abstract base class nếu chỉ cần contract:

```ts
interface PaymentMethod {
  pay(amount: number): string;
}
```

---

## 8. 🔒 Encapsulation

Encapsulation là giấu implementation detail và chỉ expose public API cần thiết.

### `_field` chỉ là convention

```ts
class BankAccount {
  _balance = 0;
}

const account = new BankAccount();
account._balance = -999; // vẫn sửa được
```

`_balance` không private thật.

### `#field` là private thật

```ts
class BankAccount {
  #balance = 0;

  deposit(amount: number) {
    if (amount <= 0) throw new Error("Invalid amount");
    this.#balance += amount;
  }

  getBalance() {
    return this.#balance;
  }
}

const account = new BankAccount();

account.deposit(100);
account.getBalance(); // 100
account.#balance; // SyntaxError
```

### 🔥 Highlight

> **Private field `#field` bảo vệ invariant của object. `_field` chỉ là naming convention.**

---

## 9. 🧮 Getter Và Setter

Getter/setter tạo API giống property nhưng có logic kiểm soát.

```ts
class Circle {
  #radius: number;

  constructor(radius: number) {
    this.radius = radius;
  }

  get radius() {
    return this.#radius;
  }

  set radius(value: number) {
    if (value <= 0) {
      throw new Error("Radius must be positive");
    }

    this.#radius = value;
  }

  get area() {
    return Math.PI * this.#radius ** 2;
  }
}
```

Nên dùng getter/setter khi:

- Cần validate khi set value.
- Cần computed property.
- Muốn giữ API ổn định nhưng đổi implementation bên trong.

Không nên lạm dụng setter có side effect khó đoán.

---

## 10. 🧰 Static Methods Và Static Fields

Static thuộc về class, không thuộc về instance.

```ts
class User {
  static role = "user";

  static fromJSON(json: string) {
    const data = JSON.parse(json);
    return new User(data.name);
  }

  constructor(public name: string) {}
}

User.role;
User.fromJSON('{"name":"Anna"}');
```

Use cases:

- Factory method: `User.fromJSON`.
- Utility method: `Date.now`, `Object.keys`.
- Shared metadata/config.

### ⚠️ Lưu ý

Không nên biến static thành global mutable state:

```ts
class Session {
  static currentUser = null; // dễ gây coupling, khó test
}
```

Với frontend app lớn, state nên nằm trong store, server cache, context hoặc dependency rõ ràng.

---

## 11. 🎯 `this` Trong Class

Class method không tự bind `this`.

```ts
class Counter {
  count = 0;

  increment() {
    this.count += 1;
  }
}

const counter = new Counter();
const fn = counter.increment;

fn(); // TypeError hoặc this undefined
```

### Cách xử lý

Bind trong constructor:

```ts
class Counter {
  count = 0;

  constructor() {
    this.increment = this.increment.bind(this);
  }

  increment() {
    this.count += 1;
  }
}
```

Dùng class field arrow function:

```ts
class Counter {
  count = 0;

  increment = () => {
    this.count += 1;
  };
}
```

### ⚠️ Trade-off

- Prototype method: share một function giữa instances, tiết kiệm memory.
- Arrow field: mỗi instance có một function riêng, tiện bind `this` nhưng tốn memory hơn.

> **Senior cần nói được trade-off này, không chỉ nói arrow function là tốt hơn.**

---

## 12. 🧱 Instance Field Vs Prototype Method

```ts
class User {
  name = "Anna"; // instance field

  login() {
    return "login"; // prototype method
  }

  logout = () => {
    return "logout"; // instance field chứa function
  };
}
```

Khác nhau:

| Thành phần | Nằm ở đâu | Share giữa instances? | Ghi chú |
|---|---:|---:|---|
| `name` | instance | Không | Mỗi object có value riêng |
| `login()` | prototype | Có | Tốt cho method thông thường |
| `logout = () => {}` | instance | Không | Auto-bind `this`, tốn memory hơn |

---

## 13. 🧩 Composition > Inheritance

Inheritance phù hợp khi có quan hệ **is-a** rõ ràng:

```txt
Admin is a User
CreditCardPayment is a PaymentMethod
```

Nhưng nếu chỉ muốn tái sử dụng behavior, nên ưu tiên composition:

```ts
class UserService {
  constructor(
    private apiClient: ApiClient,
    private logger: Logger
  ) {}

  async loadUser(id: string) {
    this.logger.info(`Load user ${id}`);
    return this.apiClient.get(`/users/${id}`);
  }
}
```

Composition tốt hơn khi:

- Muốn inject dependency để test dễ hơn.
- Muốn thay implementation mà không đổi inheritance tree.
- Muốn tránh parent class quá lớn.
- Muốn module độc lập, ít coupling.

### 🔥 Highlight

> **Inheritance reuse code theo chiều dọc. Composition ghép capability theo chiều ngang, linh hoạt hơn cho hệ thống lớn.**

---

## 14. 🧪 SOLID Khi Dùng Class

### S - Single Responsibility

Một class nên có một lý do chính để thay đổi.

```ts
// Không tốt: vừa validate, call API, format UI message
class UserManager {}
```

Tách ra:

```ts
class UserValidator {}
class UserRepository {}
class UserPresenter {}
```

### O - Open/Closed

Mở để mở rộng, đóng để sửa trực tiếp.

```ts
interface DiscountStrategy {
  calculate(price: number): number;
}

class StudentDiscount implements DiscountStrategy {
  calculate(price: number) {
    return price * 0.8;
  }
}

class Checkout {
  constructor(private discount: DiscountStrategy) {}

  total(price: number) {
    return this.discount.calculate(price);
  }
}
```

Muốn thêm discount mới thì thêm class mới, không sửa logic `Checkout`.

### L - Liskov Substitution

Subclass phải thay thế được parent mà không làm hỏng behavior mong đợi.

Ví dụ kinh điển: `Square extends Rectangle` thường dễ sai vì thay đổi invariant của width/height.

### I - Interface Segregation

Không ép class implement method nó không cần.

```ts
interface Printable {
  print(): void;
}

interface Scannable {
  scan(): void;
}
```

Tốt hơn một interface lớn:

```ts
interface Machine {
  print(): void;
  scan(): void;
  fax(): void;
}
```

### D - Dependency Inversion

Class cấp cao nên phụ thuộc vào abstraction, không phụ thuộc implementation cụ thể.

```ts
interface HttpClient {
  get<T>(url: string): Promise<T>;
}

class UserRepository {
  constructor(private http: HttpClient) {}

  getUser(id: string) {
    return this.http.get(`/users/${id}`);
  }
}
```

Test dễ hơn vì có thể inject fake client.

---

## 15. 🧠 Class Trong Frontend Hiện Đại

Frontend hiện đại ít dùng class component React, nhưng class vẫn quan trọng ở nhiều nơi.

### Dùng class tốt cho

- Domain model có invariant rõ ràng.
- SDK/client wrapper.
- Service có dependency injection.
- Error custom.
- Strategy pattern.
- Adapter/facade.
- Data structure.

Ví dụ custom error:

```ts
class ApiError extends Error {
  constructor(
    message: string,
    public status: number,
    public code: string
  ) {
    super(message);
    this.name = "ApiError";
  }
}
```

Ví dụ API client:

```ts
class ApiClient {
  constructor(private baseUrl: string) {}

  async get<T>(path: string): Promise<T> {
    const response = await fetch(`${this.baseUrl}${path}`);

    if (!response.ok) {
      throw new ApiError("Request failed", response.status, "REQUEST_FAILED");
    }

    return response.json();
  }
}
```

### Không nên dùng class cho

- UI component React mới nếu function component + hooks đủ tốt.
- Simple data object không behavior.
- State management phức tạp nếu framework đã có store/query cache.
- Logic dễ biểu diễn bằng pure function.

---

## 16. 🧬 Class Vs Object Literal Vs Function

| Cách viết | Khi dùng | Điểm mạnh |
|---|---|---|
| `class` | Object có state + behavior + lifecycle rõ | Encapsulation, inheritance, DI |
| Object literal | Config, simple object, singleton nhỏ | Đơn giản |
| Function | Transform data, pure logic, utility | Dễ test, ít state |
| Factory function | Tạo object không cần `new` | Linh hoạt, dễ private bằng closure |

Factory function:

```ts
function createCounter() {
  let count = 0;

  return {
    increment() {
      count += 1;
    },
    getCount() {
      return count;
    },
  };
}
```

Factory có private state qua closure, không cần `#`.

---

## 17. ⚠️ Lỗi Thường Gặp

### 1. Nghĩ class trong JS giống class trong Java

Sai. JS vẫn là prototype-based.

### 2. Lạm dụng inheritance

```txt
BaseComponent
  -> FormComponent
    -> ValidatedFormComponent
      -> AsyncValidatedFormComponent
```

Inheritance sâu làm code fragile, khó refactor.

### 3. Quên bind `this`

Hay gặp khi truyền method làm callback/event handler.

### 4. Dùng class cho mọi thứ

Không phải logic nào cũng cần object. Pure function thường dễ test hơn.

### 5. Dùng `_private` và tưởng là private

`_private` vẫn public. Muốn private thật dùng `#private`.

### 6. Static mutable state

Static state dễ tạo global hidden dependency.

### 7. Constructor làm quá nhiều việc

Object creation không nên tự gọi network, đọc storage, mutate global state.

---

## 18. 🧭 Khi Nào Nên Dùng Class?

Nên dùng class khi:

- Có object sống lâu với state riêng.
- Cần bảo vệ invariant.
- Cần public API rõ ràng.
- Cần dependency injection.
- Có nhiều implementation cùng contract.
- Cần custom error hoặc data structure.

Không cần class khi:

- Chỉ map/filter/format data.
- Chỉ chứa constants/config.
- Logic stateless.
- Framework đã có abstraction tốt hơn.

### Rule thực tế

> **Nếu behavior xoay quanh state nội bộ và cần bảo vệ invariant, class hợp lý. Nếu chỉ biến đổi input thành output, function thường tốt hơn.**

---

## 19. 🧾 Câu Trả Lời Phỏng Vấn 2 Phút

> **JavaScript class là cú pháp ES6 giúp viết OOP dễ đọc hơn, nhưng bên dưới vẫn dựa trên prototype chain. Method khai báo trong class nằm trên prototype và được share giữa instances. `constructor` khởi tạo state, `extends` tạo inheritance, còn `super()` dùng để gọi parent constructor hoặc parent method.**
>
> **Điểm quan trọng ở senior level là không lạm dụng class. Inheritance chỉ nên dùng khi có quan hệ is-a rõ ràng. Trong frontend architecture, composition và dependency injection thường linh hoạt hơn, dễ test hơn và ít coupling hơn. Với encapsulation, `_field` chỉ là convention, còn `#privateField` mới là private thật. Ngoài ra cần cẩn thận với `this` vì class method không auto-bind khi truyền làm callback.**

---

## 20. 🎯 Câu Trả Lời Staff-Level

> **Ở staff level, tôi nhìn class như một công cụ để mô hình hóa domain behavior và enforce invariants, không phải default abstraction cho mọi logic. Vì JavaScript là prototype-based, class chỉ nên được dùng khi nó làm API rõ hơn: ví dụ API client, domain entity, custom error, strategy, adapter hoặc service có dependency injection.**
>
> **Tôi tránh deep inheritance vì nó tạo coupling theo chiều dọc và dễ vi phạm Liskov Substitution. Với hệ thống frontend lớn, tôi thường ưu tiên composition: inject API client, logger, cache, formatter hoặc strategy vào class/service. Cách này giúp test dễ hơn, thay implementation dễ hơn và giảm hidden dependency.**
>
> **Tôi cũng phân biệt rõ method trên prototype với instance field arrow function. Prototype method tiết kiệm memory, còn arrow field tiện bind `this` nhưng tạo function mới cho mỗi instance. Khi thiết kế library hoặc SDK, chi tiết này ảnh hưởng đến performance và memory nếu số lượng instance lớn.**

---

## 21. ✅ Checklist Senior/Staff

- ✅ Biết class là syntactic sugar trên prototype.
- ✅ Hiểu method nằm trên `Class.prototype`.
- ✅ Biết `typeof ClassName === "function"`.
- ✅ Hiểu `new`, `constructor`, `this`.
- ✅ Biết `extends` tạo prototype chain.
- ✅ Biết `super()` phải gọi trước `this` trong subclass.
- ✅ Phân biệt `_private` và `#private`.
- ✅ Biết getter/setter dùng để validate/computed property.
- ✅ Biết static method dùng cho factory/utility, tránh global mutable state.
- ✅ Hiểu class method không auto-bind `this`.
- ✅ Phân biệt prototype method và arrow field.
- ✅ Ưu tiên composition khi inheritance không rõ ràng.
- ✅ Biết áp dụng SOLID ở mức thực tế, không giáo điều.
- ✅ Biết khi nào class phù hợp trong frontend hiện đại.

---

## 22. 🧠 Ghi Nhớ Nhanh

| Icon | Ý chính |
|---|---|
| 🏛️ | Class là syntax đẹp hơn cho prototype |
| 🔗 | `extends` nối prototype chain |
| 📞 | `super()` gọi parent constructor/method |
| 🔒 | `#field` mới private thật |
| 🎯 | Method thường nằm trên prototype |
| ⚠️ | Class method không auto-bind `this` |
| 🧩 | Composition thường scale tốt hơn inheritance |
| 🧪 | Dependency injection giúp test dễ hơn |

---

## 23. 🚀 Kết Luận

> **JavaScript Classes giúp code OOP rõ ràng hơn, nhưng senior/staff frontend cần hiểu bản chất prototype, quản lý `this`, encapsulation, trade-off giữa inheritance và composition, và biết khi nào không nên dùng class.**

Một câu nhớ nhanh:

> **Class là công cụ để đóng gói state + behavior. Prototype là cơ chế thật. Composition là lựa chọn scale tốt hơn trong đa số frontend architecture hiện đại.**
