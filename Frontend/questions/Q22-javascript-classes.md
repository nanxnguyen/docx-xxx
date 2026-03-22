# 🏛️ Q22: JavaScript Classes

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"ES6 Classes là syntactic sugar trên prototype-based inheritance, cung cấp cleaner syntax cho constructor functions, inheritance, và encapsulation."**

**🔑 4 Khái Niệm Chính:**

**1. Class Basics:**
- Syntax: `class Person { constructor(name) { this.name = name } method() {} }`
- **Syntactic sugar** trên constructor functions + prototypes
- `new` keyword bắt buộc (không như functions)
- Methods tự động **non-enumerable**

**2. Inheritance (`extends`):**
- `class Child extends Parent` - kế thừa prototype chain
- **`super()`** bắt buộc trong constructor (call parent constructor)
- `super.method()` - gọi parent methods
- Method overriding: child method override parent cùng tên

**3. Static Methods/Properties:**
- `static method()` - class-level, **không cần instance**
- Call trực tiếp: `Person.staticMethod()`
- Use case: utility functions, factory methods (`Array.from()`, `Object.keys()`)

**4. Private Fields (ES2022):**
- `#privateField` - truly private (không access từ ngoài)
- Khác `_convention` (chỉ là naming, vẫn access được)

**⚠️ Lỗi Thường Gặp:**
- Quên `super()` trong child constructor → ReferenceError
- Dùng arrow functions cho methods → `this` binding issues
- Pass method as callback mà không bind → `this` = undefined
- Nghĩ class tạo scope mới → Sai! Chỉ là syntax sugar

**💡 Kiến Thức Senior:**
- **Classes ARE functions**: `typeof MyClass === 'function'`
- **Hoisting difference**: Class declarations **không hoist** (TDZ), function declarations hoist
- **`this` binding**: Class methods không auto-bind `this` → dùng arrow functions hoặc `.bind()` trong constructor
- **Mixins pattern**: Combine multiple classes với `Object.assign(MyClass.prototype, Mixin)`
- Composition > Inheritance (prefer "has-a" over "is-a" relationships)




**⚡ Quick Summary:**
> ES6 Classes = syntactic sugar over prototypes. constructor, methods, static, inheritance

**💡 Ghi Nhớ:**
- 🏗️ **Class**: `class Name { constructor() {} method() {} }`
- 🔗 **Extends**: `class Child extends Parent { super() }`
- 📌 **Static**: Class-level methods, không cần instance

**Trả lời:**

- **Classes**: Syntactic sugar cho constructor functions
- **Hoạt động**: Tạo objects với methods và properties
- **Ưu điểm**: Cleaner syntax, inheritance, encapsulation
- **Nhược điểm**: Có thể gây confusion với this binding

**Code Example:**

```typescript
// Basic class
class Person {
  name: string;
  age: number;

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }

  greet(): string {
    return `Hello, I'm ${this.name}`;
  }

  getAge(): number {
    return this.age;
  }
}

const person = new Person('John', 25);
console.log(person.greet()); // "Hello, I'm John"

// Inheritance
class Student extends Person {
  grade: string;

  constructor(name: string, age: number, grade: string) {
    super(name, age);
    this.grade = grade;
  }

  study(): string {
    return `${this.name} is studying`;
  }

  greet(): string {
    return `Hello, I'm ${this.name} and I'm a student`;
  }
}

const student = new Student('Jane', 20, 'A');
console.log(student.greet()); // "Hello, I'm Jane and I'm a student"

// Static methods
class MathUtils {
  static add(a: number, b: number): number {
    return a + b;
  }

  static multiply(a: number, b: number): number {
    return a * b;
  }
}

console.log(MathUtils.add(5, 3)); // 8

// Getters and setters
class Circle {
  private _radius: number;

  constructor(radius: number) {
    this._radius = radius;
  }

  get radius(): number {
    return this._radius;
  }

  set radius(value: number) {
    if (value < 0) {
      throw new Error('Radius cannot be negative');
    }
    this._radius = value;
  }

  get area(): number {
    return Math.PI * this._radius * this._radius;
  }
}

const circle = new Circle(5);
console.log(circle.area); // 78.54
circle.radius = 10;
console.log(circle.area); // 314.16
```

**Best Practices:**

- Sử dụng classes cho object-oriented programming
- Sử dụng inheritance khi cần
- Sử dụng static methods cho utility functions
- Sử dụng getters/setters cho data validation




Phần 2 # OOP (Object-Oriented Programming) trong JavaScript - Classes, Inheritance, Encapsulation & SOLID Principles?

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (4-5 phút):**

**"OOP trong JS bao gồm Classes (ES6 sugar trên prototypes), Encapsulation (#private fields), Inheritance (extends), Polymorphism (override methods), + SOLID principles để thiết kế maintainable code."**

**🔑 5 Pillars của OOP:**

**1. Classes (Lớp):**
- **Blueprint** để tầo objects: `class User { constructor(name) {...} }`
- **Syntactic sugar** trên prototype-based inheritance
- Methods tự động **non-enumerable**, khác function constructors

**2. Encapsulation (Đóng gói):**
- **Private fields**: `#balance` - truly private (ES2022), không access từ ngoài
- **Public API**: Chỉ expose cần thiết (`getBalance()`, `deposit()`)
- Protect implementation details, prevent invalid state

**3. Inheritance (Kế thừa):**
- `class Admin extends User` - **"is-a" relationship**
- `super()` bắt buộc trong constructor, `super.method()` gọi parent
- Prototype chain: `admin.__proto__` → `Admin.prototype` → `User.prototype` → `Object.prototype`

**4. Polymorphism (Đa hình):**
- **Override methods**: `Admin.login()` khác `User.login()`
- Cùng interface, behavior khác nhau
- Duck typing: "If it walks like a duck..."

**5. Composition (Kết hợp):**
- **"Has-a" relationship** - inject dependencies
- `class UserService { constructor(logger, db) {...} }`
- **Prefer over Inheritance** - flexible, loosely coupled

**🔑 SOLID Principles:**

- **S**ingle Responsibility: 1 class = 1 nhiệm vụ
- **O**pen/Closed: Mở rộng, đóng sửa đổi (extend, không modify existing)
- **L**iskov Substitution: Subclass thay thế parent không break code
- **I**nterface Segregation: Nhiều interfaces nhỏ > 1 interface lớn
- **D**ependency Inversion: Depend on abstractions, not concretions (inject)

**⚠️ Lỗi Thường Gặp:**
- Quên `super()` trong child constructor → ReferenceError
- Dùng `_privateField` (convention) như truly private → vẫn access được, dùng `#` thay vì
- **Deep inheritance chains** (>3 levels) → fragile, hard maintain
- Pass methods as callbacks không bind `this` → `this` = undefined

**💡 Kiến Thức Senior:**
- **Composition > Inheritance**: Avoid "gorilla-banana problem" (muốn banana nhưng nhận cả gorilla + jungle)
- **Mixins**: `Object.assign(MyClass.prototype, Loggable, Serializable)` - multiple behaviors
- **Static methods** for factories: `User.fromJSON(json)`, `Array.from()`
- **Private class fields** (#) không inherit (khác public properties)
- Modern approach: **Functional programming** + **Hooks** (React) thay classes




**Trả lời:****
OOP (Lập trình Hướng Đối Tượng) là **paradigm lập trình** dựa trên **objects** (đối tượng) chứa:

- **Data** (dữ liệu) → properties/fields (thuộc tính)
- **Behavior** (hành vi) → methods (phương thức)

JavaScript hỗ trợ OOP thông qua 5 concepts chính:

1. **Classes (Lớp)** - ES6+

   - Là "bản thiết kế" (blueprint) để tạo objects
   - Syntactic sugar cho prototype-based inheritance
   - **Ví dụ**: `class User { ... }` → tạo ra nhiều user objects

2. **Encapsulation (Đóng gói)**

   - Ẩn implementation details (chi tiết triển khai) bên trong class
   - Chỉ expose ra public API cần thiết
   - Dùng **private fields** (`#fieldName`) để bảo vệ data
   - **Ví dụ**: `#balance` trong BankAccount không thể truy cập từ bên ngoài

3. **Inheritance (Kế thừa)**

   - Class con (child) kế thừa properties/methods từ class cha (parent)
   - Tái sử dụng code, tránh duplication
   - Dùng keyword `extends`
   - **Ví dụ**: `Admin extends User` → Admin có tất cả methods của User + thêm methods riêng

4. **Polymorphism (Đa hình)**

   - Subclass có thể override (ghi đè) methods của parent
   - Cùng method name nhưng behavior khác nhau
   - **Ví dụ**: `Admin.login()` khác `User.login()` (Admin có thêm audit log)

5. **Composition (Kết hợp)**
   - "Has-a" relationship thay vì "Is-a" (inheritance)
   - Inject dependencies vào class thay vì kế thừa
   - **Ưu tiên hơn Inheritance** (Composition > Inheritance)
   - **Ví dụ**: `UserService` có `logger` và `emailService` (inject vào) thay vì kế thừa từ Logger

**🎯 SOLID Principles (5 nguyên tắc thiết kế OOP):**

- **S**ingle Responsibility: 1 class chỉ làm 1 việc
- **O**pen/Closed: Mở cho mở rộng, đóng cho sửa đổi
- **L**iskov Substitution: Subclass thay thế được parent
- **I**nterface Segregation: Interfaces nhỏ, tập trung
- **D**ependency Inversion: Phụ thuộc vào abstractions, không phải concretions

**Hoạt động:**

```
┌──────────────────────────────────────────────────────────┐
│              OOP Concepts Flow                           │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  1. CLASS DEFINITION (Blueprint)                        │
│  ┌─────────────────────────────────────┐                │
│  │ class User {                        │                │
│  │   #password // Private field       │                │
│  │   constructor(name) { ... }        │                │
│  │   login() { ... }                  │                │
│  │ }                                   │                │
│  └─────────────────────────────────────┘                │
│               ↓                                          │
│  2. INSTANTIATION (Create object)                       │
│  ┌─────────────────────────────────────┐                │
│  │ const user = new User('John')       │                │
│  │ user.login() // Call method        │                │
│  └─────────────────────────────────────┘                │
│               ↓                                          │
│  3. INHERITANCE (Reuse code)                            │
│  ┌─────────────────────────────────────┐                │
│  │ class Admin extends User {          │                │
│  │   deleteUser() { ... }              │                │
│  │ }                                   │                │
│  └─────────────────────────────────────┘                │
│               ↓                                          │
│  4. POLYMORPHISM (Override behavior)                    │
│  ┌─────────────────────────────────────┐                │
│  │ class Admin extends User {          │                │
│  │   login() { // Override             │                │
│  │     super.login()                   │                │
│  │     this.logAudit()                 │                │
│  │   }                                  │                │
│  │ }                                   │                │
│  └─────────────────────────────────────┘                │
│               ↓                                          │
│  5. COMPOSITION (Combine objects)                       │
│  ┌─────────────────────────────────────┐                │
│  │ class User {                        │                │
│  │   constructor(logger) {             │                │
│  │     this.logger = logger // Inject │                │
│  │   }                                  │                │
│  │ }                                   │                │
│  └─────────────────────────────────────┘                │
└──────────────────────────────────────────────────────────┘
```

**Ưu điểm:**

1. **✅ Code Reusability (Tái sử dụng Code)**

   - **Giải thích**: Inheritance cho phép class con kế thừa tất cả properties/methods từ class cha
   - **Lợi ích**: Không phải viết lại code → giảm duplication, dễ maintain
   - **Ví dụ**:
     - `Admin extends User` → Admin có sẵn `login()`, `logout()` từ User
     - Chỉ cần viết thêm methods riêng như `deleteUser()`, `manageRoles()`
   - **Thực tế**:
     - Base class `Animal` có `eat()`, `sleep()`
     - `Dog`, `Cat`, `Bird` đều kế thừa → không viết lại 3 lần

2. **✅ Maintainability (Dễ Bảo trì)**

   - **Giải thích**: Encapsulation (đóng gói) ẩn implementation details, chỉ expose public API
   - **Lợi ích**:
     - Thay đổi internal logic không ảnh hưởng code bên ngoài
     - Tách biệt concerns (data vs behavior)
     - Dễ refactor
   - **Ví dụ**:
     - `#balance` trong BankAccount là private → thay đổi cách tính balance không ảnh hưởng caller
     - External code chỉ gọi `getBalance()` (stable API)
   - **Thực tế**:
     - Sửa validation logic trong `UserValidator` → không ảnh hưởng `UserService`
     - Thay database trong `UserRepository` → không ảnh hưởng business logic

3. **✅ Scalability (Khả năng Mở rộng)**

   - **Giải thích**: Dễ dàng thêm tính năng mới qua subclasses hoặc composition
   - **Lợi ích**:
     - Extend functionality mà không sửa code cũ (Open/Closed Principle)
     - Thêm classes mới độc lập
   - **Ví dụ**:
     - Có `PaymentMethod` abstract → thêm `MomoPayment`, `ZaloPayPayment` dễ dàng
     - Không cần sửa code xử lý payment hiện tại
   - **Thực tế**:
     - E-commerce có `StandardShipping` → thêm `ExpressShipping`, `SameDayShipping`
     - Trading system có `MarketOrder` → thêm `LimitOrder`, `StopLossOrder`

4. **✅ Type Safety (An toàn Kiểu)**

   - **Giải thích**: TypeScript interfaces/abstract classes enforce contracts, catch errors at compile-time
   - **Lợi ích**:
     - IDE autocomplete đầy đủ
     - Catch errors trước khi run code
     - Documentation tự động qua types
   - **Ví dụ**:

     ```typescript
     interface ILogger {
       log(message: string): void; // Contract
     }

     class Service {
       constructor(private logger: ILogger) {} // Type-safe
     }

     new Service(123); // ❌ Error: 123 không phải ILogger
     ```

   - **Thực tế**:
     - `UserService` require `ILogger` → không thể pass `string` hay `number`
     - Refactor method signature → TypeScript báo lỗi tất cả nơi gọi

5. **✅ Testability (Dễ Kiểm thử)**

   - **Giải thích**: Dependency Injection với composition cho phép inject mocks khi test
   - **Lợi ích**:
     - Test isolated (không phụ thuộc external services)
     - Fast (không call API/database thật)
     - Predictable (mock return cố định)
   - **Ví dụ**:

     ```typescript
     // Production
     const service = new UserService(new RealLogger(), new RealEmailService());

     // Testing
     const service = new UserService(new MockLogger(), new MockEmailService());
     ```

   - **Thực tế**:
     - Test `TradingService` với mock `OrderExecutor` → không gửi lệnh thật lên sàn
     - Test `PaymentService` với mock `PaymentGateway` → không charge tiền thật

**Nhược điểm:**

1. **❌ Over-Engineering (Thiết kế Quá phức tạp)**

   - **Giải thích**: Inheritance hierarchy quá sâu (nhiều tầng kế thừa) → khó hiểu, khó maintain
   - **Vấn đề**:
     - Phải đọc nhiều classes để hiểu logic
     - Khó trace method được gọi từ đâu
     - Thêm tính năng mới phải hiểu cả hierarchy
   - **Ví dụ BAD**:
     ```typescript
     class Animal {}
     class Mammal extends Animal {}
     class Carnivore extends Mammal {}
     class Feline extends Carnivore {}
     class Cat extends Feline {}
     class PersianCat extends Cat {} // QUÁ SÂU! 6 tầng
     ```
   - **Vấn đề thực tế**:
     - Sửa `Animal` → phải test lại 5 classes con
     - Thêm method trong `Mammal` → có thể break `PersianCat`
   - **Giải pháp**: Giới hạn 2-3 tầng, prefer composition

2. **❌ Tight Coupling (Liên kết Chặt chẽ)**

   - **Giải thích**: Subclass phụ thuộc chặt chẽ vào parent → thay đổi parent có thể break child
   - **Vấn đề**:
     - Cannot remove/change parent methods (children đang dùng)
     - Subclass biết quá nhiều về parent internals
     - Khó refactor
   - **Ví dụ BAD**:

     ```typescript
     class UserService extends Logger {
       registerUser() {
         this.log('Registering...'); // Phụ thuộc vào Logger.log()
       }
     }

     // Nếu Logger.log() đổi signature → UserService break!
     ```

   - **Vấn đề thực tế**:
     - `Admin extends User` → nếu User thêm required param trong constructor → tất cả subclasses phải update
     - `PremiumAccount extends BankAccount` → nếu BankAccount đổi cách tính balance → PremiumAccount có thể sai
   - **Giải pháp**: Dùng composition thay vì inheritance

3. **❌ Fragile Base Class Problem (Vấn đề Class Cha Dễ vỡ)**

   - **Giải thích**: Thay đổi nhỏ trong parent class có thể break tất cả children classes
   - **Vấn đề**:
     - Sửa bug trong parent → introduce bugs trong children
     - Không dám refactor parent vì sợ break children
     - Side effects không mong muốn
   - **Ví dụ BAD**:

     ```typescript
     class Counter {
       count = 0;
       increment() {
         this.count++;
       }
       incrementTwice() {
         this.increment();
         this.increment();
       }
     }

     class SpecialCounter extends Counter {
       increment() {
         super.increment();
         console.log('Incremented!'); // Log mỗi lần increment
       }
     }

     const counter = new SpecialCounter();
     counter.incrementTwice(); // Logs 2 lần (expected)

     // ❌ Nếu parent refactor incrementTwice():
     // incrementTwice() { this.count += 2; }
     // → KHÔNG gọi increment() nữa → SpecialCounter KHÔNG log!
     ```

   - **Vấn đề thực tế**:
     - Parent thêm validation trong method → children override mà quên gọi `super()` → bypass validation
     - Parent đổi order của operations → children expect old order → behavior sai
   - **Giải pháp**: Document parent behavior, use protected methods carefully

4. **❌ Memory Overhead (Tốn Bộ nhớ) - Trước ES6**

   - **Giải thích**: Trước ES6 (không có class syntax), mỗi instance duplicate methods → tốn memory
   - **Vấn đề**:
     - Tạo 1000 objects → 1000 copies của cùng 1 method
     - Memory usage tăng tuyến tính với số instances
   - **Ví dụ BAD (Pre-ES6)**:

     ```typescript
     function User(name) {
       this.name = name;
       this.login = function () {
         // ❌ Method trong constructor
         console.log('Logging in...');
       };
     }

     const user1 = new User('A');
     const user2 = new User('B');
     // user1.login !== user2.login (2 copies khác nhau!)
     ```

   - **Giải thích**:
     - Mỗi instance có 1 copy riêng của `login()` method
     - 1000 users → 1000 copies → waste memory
   - **Giải pháp (ES6+)**:

     ```typescript
     class User {
       constructor(name) {
         this.name = name;
       }
       login() {
         // ✅ Method trên prototype
         console.log('Logging in...');
       }
     }

     // Tất cả instances share 1 login() trên prototype
     // user1.login === user2.login (cùng 1 method!)
     ```

   - **Lưu ý**: ES6 classes tự động đặt methods trên prototype → không còn vấn đề này

5. **❌ Harder Debugging (Khó Debug hơn)**

   - **Giải thích**: Method lookup qua prototype chain → khó trace method được gọi từ đâu
   - **Vấn đề**:
     - Stack trace dài, nhiều tầng
     - Không biết method override ở đâu
     - Breakpoint phải set nhiều nơi
   - **Ví dụ**:

     ```typescript
     class A {
       method() {
         console.log('A');
       }
     }

     class B extends A {
       method() {
         super.method(); // Gọi A.method()
         console.log('B');
       }
     }

     class C extends B {
       method() {
         super.method(); // Gọi B.method() → gọi A.method()
         console.log('C');
       }
     }

     new C().method();
     // Stack trace: C.method() → B.method() → A.method()
     // Phải trace qua 3 tầng để hiểu flow
     ```

   - **Vấn đề thực tế**:
     - Bug trong `PremiumAccount.withdraw()` → phải check cả `BankAccount.withdraw()`
     - Method được override ở nhiều levels → không biết đang chạy implementation nào
     - Debugging tools hiển thị prototype chain phức tạp
   - **Giải pháp**:
     - Giới hạn inheritance depth (2-3 tầng max)
     - Document override behavior rõ ràng
     - Use composition khi có thể

**Chú thích:**

**🔒 Private Fields `#` (Thực sự Private):**

- Syntax: `#fieldName` (bắt đầu bằng dấu `#`)
- **Không thể truy cập** từ bên ngoài class, kể cả subclass
- Khác `_prefix` (chỉ là convention, vẫn access được)
- Ví dụ: `account.#balance` → ❌ Error

**🔗 `extends` (Kế thừa):**

- Tạo class con kế thừa từ class cha
- Tạo **prototype chain**: Child.prototype → Parent.prototype
- Child có tất cả properties/methods của Parent
- Ví dụ: `class Admin extends User { ... }`

**⬆️ `super` (Gọi Parent):**

- Trong constructor: `super()` gọi parent constructor (bắt buộc gọi trước `this`)
- Trong method: `super.methodName()` gọi parent method
- Ví dụ:
  ```typescript
  constructor(name) {
    super(name); // Gọi User constructor
    this.role = 'admin';
  }
  ```

**🧩 Composition > Inheritance (Ưu tiên Kết hợp hơn Kế thừa):**

- **Inheritance**: "Is-a" relationship (Admin **là** User)
- **Composition**: "Has-a" relationship (UserService **có** Logger)
- Composition linh hoạt hơn, ít tight coupling hơn
- Dễ test hơn (mock dependencies)
- Ví dụ:

  ```typescript
  // ❌ Inheritance: phụ thuộc parent
  class UserService extends Logger {}

  // ✅ Composition: inject dependency
  class UserService {
    constructor(private logger: Logger) {}
  }
  ```

**📐 SOLID Principles (Giải thích đơn giản):**

1. **Single Responsibility (Trách nhiệm Đơn lẻ)**

   - 1 class chỉ làm 1 việc duy nhất
   - Dễ hiểu, dễ maintain, dễ test
   - Ví dụ: `UserValidator` chỉ validate, `UserRepository` chỉ save/load

2. **Open/Closed (Mở-Đóng)**

   - Mở cho **extension** (thêm tính năng mới)
   - Đóng cho **modification** (không sửa code cũ)
   - Dùng abstract class/interface để extend
   - Ví dụ: Thêm `BuyOneGetOne` discount mà không sửa class `Discount`

3. **Liskov Substitution (Thay thế Liskov)**

   - Subclass phải thay thế được parent mà không break code
   - Child phải tuân thủ "contract" của parent
   - Ví dụ: `CreditCardPayment` và `BankTransferPayment` đều work với `PaymentMethod`

4. **Interface Segregation (Tách Interface)**

   - Nhiều interfaces nhỏ > 1 interface lớn
   - Class chỉ implement methods cần thiết
   - Ví dụ: `IReadable`, `IWritable`, `IDeletable` riêng biệt thay vì 1 interface có tất cả

5. **Dependency Inversion (Đảo ngược Phụ thuộc)**
   - Phụ thuộc vào **abstractions** (interfaces/abstract classes)
   - Không phụ thuộc vào **concretions** (concrete classes)
   - Dễ swap implementations, dễ test
   - Ví dụ: `OrderService` nhận `ILogger` (interface) thay vì `ConsoleLogger` (concrete)

**Code Example (TypeScript):**

```typescript
// ============================================
// 1. BASIC CLASS WITH ENCAPSULATION (Đóng gói)
// ============================================
// 🏦 Ví dụ: Tài khoản ngân hàng - ẩn số dư bên trong
class BankAccount {
  // 🔒 Private field: chỉ class này access được
  #balance: number = 0; // Số dư (truly private)

  constructor(
    public readonly accountNumber: string, // Số tài khoản (readonly: không sửa được)
    private owner: string // Chủ tài khoản (private: chỉ trong class)
  ) {
    // accountNumber là public → có thể đọc: account.accountNumber
    // owner là private → KHÔNG thể đọc từ bên ngoài: account.owner ❌
  }

  // 💰 Public method: gửi tiền (deposit = nạp tiền)
  deposit(amount: number): void {
    if (amount <= 0) throw new Error('Số tiền phải > 0');
    this.#balance += amount; // Cộng vào số dư
    console.log(`✅ Đã nạp ${amount}đ. Số dư: ${this.#balance}đ`);
  }

  // 💸 Public method: rút tiền (withdraw = rút)
  withdraw(amount: number): void {
    if (amount > this.#balance) {
      throw new Error('Số dư không đủ!');
    }
    this.#balance -= amount; // Trừ số dư
    console.log(`✅ Đã rút ${amount}đ. Còn lại: ${this.#balance}đ`);
  }

  // 📊 Public method: xem số dư (getBalance = lấy số dư)
  getBalance(): number {
    return this.#balance; // Chỉ đọc, không sửa được từ bên ngoài
  }
}

// 🎯 Sử dụng class
const account = new BankAccount('123456', 'Nguyễn Văn A');
account.deposit(1000); // ✅ Nạp 1000đ
console.log(account.getBalance()); // 1000
account.withdraw(300); // ✅ Rút 300đ

// ❌ KHÔNG thể truy cập trực tiếp private field
// console.log(account.#balance);  // ❌ Error: Private field '#balance' must be declared in an enclosing class
// console.log(account.owner);     // ❌ Error: Property 'owner' is private
console.log(account.accountNumber); // ✅ OK: '123456' (public readonly)

// ============================================
// 2. INHERITANCE (Kế thừa) & POLYMORPHISM (Đa hình)
// ============================================
// 💎 Tài khoản Premium: kế thừa BankAccount + thêm tính năng mới
class PremiumAccount extends BankAccount {
  private creditLimit: number; // Hạn mức tín dụng (credit limit)

  constructor(accountNumber: string, owner: string, creditLimit: number) {
    // ⬆️ super() BẮT BUỘC gọi TRƯỚC khi dùng 'this'
    super(accountNumber, owner); // Gọi constructor của BankAccount
    this.creditLimit = creditLimit;
  }

  // 🔄 Override (ghi đè) method withdraw của parent (Polymorphism)
  withdraw(amount: number): void {
    // 💡 PremiumAccount có thể rút quá số dư nhờ credit limit
    const available = this.getBalance() + this.creditLimit;

    if (amount > available) {
      throw new Error(`Vượt hạn mức! Khả dụng: ${available}đ`);
    }

    // Rút số dư trước
    const balanceToWithdraw = Math.min(amount, this.getBalance());
    if (balanceToWithdraw > 0) {
      super.withdraw(balanceToWithdraw); // Gọi method của parent
    }

    // Nếu còn thiếu → dùng credit
    const creditUsed = amount - balanceToWithdraw;
    if (creditUsed > 0) {
      console.log(`💳 Sử dụng credit: ${creditUsed}đ`);
    }
  }

  // ➕ Method MỚI chỉ có ở PremiumAccount (không có ở BankAccount)
  getCreditInfo() {
    return {
      balance: this.getBalance(), // Số dư hiện tại
      creditLimit: this.creditLimit, // Hạn mức tín dụng
      available: this.getBalance() + this.creditLimit, // Tổng khả dụng
    };
  }
}

// 🎯 Sử dụng inheritance
const premium = new PremiumAccount('789', 'Trần Thị B', 5000);
premium.deposit(2000); // ✅ Có method từ parent (BankAccount)
premium.withdraw(3000); // ✅ Override: rút quá số dư nhờ credit
console.log(premium.getCreditInfo()); // ✅ Method mới của PremiumAccount
// Output: { balance: 0, creditLimit: 5000, available: 5000 }

// 📝 Giải thích Polymorphism:
// - BankAccount.withdraw() → chỉ rút trong số dư
// - PremiumAccount.withdraw() → rút cả credit limit (behavior khác)
// Cùng tên method nhưng hành vi khác nhau!

// ============================================
// 3. ABSTRACT CLASS (Lớp Trừu tượng) & INTERFACE
// ============================================
// 📐 Abstract class: KHÔNG thể tạo instance trực tiếp, chỉ để kế thừa
abstract class PaymentMethod {
  constructor(public provider: string) {} // provider = nhà cung cấp (Visa, Mastercard, VNPay...)

  // 🔴 Abstract method: BẮT BUỘC implement ở subclass
  // Không có implementation (body) ở đây
  abstract processPayment(amount: number): Promise<boolean>;

  // ✅ Concrete method: có implementation, các subclass dùng chung
  validateAmount(amount: number): boolean {
    return amount > 0 && amount < 1_000_000; // Giới hạn 1 triệu
  }
}

// 📋 Interface: "hợp đồng" (contract) - class implement phải có đủ methods
interface IRefundable {
  refund(transactionId: string): Promise<void>; // Hoàn tiền
}

// 💳 Thanh toán thẻ tín dụng: extends abstract class + implements interface
class CreditCardPayment extends PaymentMethod implements IRefundable {
  constructor(
    provider: string, // VD: 'Visa', 'Mastercard'
    private cardNumber: string // Số thẻ
  ) {
    super(provider); // Gọi constructor của PaymentMethod
  }

  // ✅ Implement abstract method (BẮT BUỘC)
  async processPayment(amount: number): Promise<boolean> {
    // Validate bằng method của parent
    if (!this.validateAmount(amount)) {
      console.log('❌ Số tiền không hợp lệ!');
      return false;
    }

    // Xử lý thanh toán thẻ
    console.log(`💳 Đang charge ${amount}đ vào thẻ ${this.cardNumber}...`);
    // Gọi API gateway (VNPay, Stripe...)
    return true;
  }

  // ✅ Implement interface IRefundable
  async refund(transactionId: string): Promise<void> {
    console.log(`💰 Đang hoàn tiền giao dịch ${transactionId}...`);
    // Logic hoàn tiền...
  }
}

// 🏦 Chuyển khoản ngân hàng: chỉ extends abstract class (KHÔNG implement IRefundable)
class BankTransferPayment extends PaymentMethod {
  constructor(
    provider: string, // VD: 'VCB', 'ACB'
    private bankCode: string // Mã ngân hàng
  ) {
    super(provider);
  }

  // ✅ Implement abstract method (BẮT BUỘC)
  async processPayment(amount: number): Promise<boolean> {
    if (!this.validateAmount(amount)) return false;

    console.log(`🏦 Đang chuyển khoản ${amount}đ qua ${this.bankCode}...`);
    return true;
  }

  // ❌ KHÔNG có method refund() vì không implement IRefundable
  // (Chuyển khoản thường không hoàn tiền tự động)
}

// 🎯 Sử dụng
const creditCard = new CreditCardPayment('Visa', '4111-1111-1111-1111');
await creditCard.processPayment(500_000); // ✅ Thanh toán
await creditCard.refund('TXN123'); // ✅ Hoàn tiền

const bankTransfer = new BankTransferPayment('VietcomBank', '970436');
await bankTransfer.processPayment(1_000_000); // ✅ Chuyển khoản
// await bankTransfer.refund('TXN456');      // ❌ Error: không có method refund()

// ============================================
// 4. COMPOSITION OVER INHERITANCE (TỐI ƯU NHẤT!)
// ============================================
// ❌ BAD: Deep inheritance hierarchy (Cây kế thừa sâu - khó maintain)
class Animal {} // Động vật
class Mammal extends Animal {} // Động vật có vú
class Dog extends Mammal {} // Chó
class Labrador extends Dog {} // Chó Labrador - QUÁ SÂU! Khó hiểu và maintain

// 🤔 Vấn đề:
// - Nếu sửa Animal → ảnh hưởng tất cả classes con
// - Tight coupling: Labrador phụ thuộc vào Dog, Mammal, Animal
// - Khó test: phải setup cả chain

// ✅ GOOD: Composition pattern (Kết hợp - linh hoạt hơn)
// 📝 Định nghĩa interfaces (contracts)
interface ILogger {
  log(message: string): void; // Ghi log
}

interface IEmailService {
  sendEmail(to: string, subject: string): Promise<void>; // Gửi email
}

// 🔧 Implementations cụ thể
class ConsoleLogger implements ILogger {
  log(message: string): void {
    console.log(`[LOG] ${new Date().toISOString()}: ${message}`);
  }
}

class EmailService implements IEmailService {
  async sendEmail(to: string, subject: string): Promise<void> {
    console.log(`📧 Gửi email đến ${to}: ${subject}`);
    // Gọi API SendGrid, AWS SES, SMTP...
  }
}

// 🎯 UserService: COMPOSE (kết hợp) thay vì INHERIT (kế thừa)
// "Has-a" relationship thay vì "Is-a"
class UserService {
  // 💉 Dependency Injection: inject qua constructor
  constructor(
    private logger: ILogger, // UserService HAS-A logger
    private emailService: IEmailService // UserService HAS-A emailService
  ) {
    // ✅ Ưu điểm:
    // - Dễ swap implementation (ConsoleLogger → FileLogger)
    // - Dễ test (inject mock logger, mock emailService)
    // - Loose coupling (không phụ thuộc concrete classes)
  }

  async registerUser(email: string, password: string): Promise<void> {
    this.logger.log(`🚀 Đang đăng ký user: ${email}`);

    // Logic đăng ký user...
    // 1. Validate email/password
    // 2. Hash password
    // 3. Lưu vào database

    // Gửi email chào mừng
    await this.emailService.sendEmail(email, 'Chào mừng bạn đến với nền tảng!');

    this.logger.log(`✅ User đã đăng ký thành công: ${email}`);
  }
}

// 🎯 Sử dụng Dependency Injection
const userService = new UserService(
  new ConsoleLogger(), // Inject logger implementation
  new EmailService() // Inject email implementation
);

await userService.registerUser('user@example.com', 'password123');

// 💡 Dễ dàng thay đổi implementation:
class FileLogger implements ILogger {
  log(message: string): void {
    // Ghi vào file thay vì console
  }
}

const userServiceWithFileLog = new UserService(
  new FileLogger(), // ✅ Swap logger → không cần sửa UserService!
  new EmailService()
);

// 🧪 Dễ dàng test với mocks:
class MockLogger implements ILogger {
  logs: string[] = [];
  log(message: string): void {
    this.logs.push(message); // Lưu logs để verify
  }
}

class MockEmailService implements IEmailService {
  sentEmails: Array<{ to: string; subject: string }> = [];
  async sendEmail(to: string, subject: string): Promise<void> {
    this.sentEmails.push({ to, subject }); // Lưu emails để verify
  }
}

const mockLogger = new MockLogger();
const mockEmailService = new MockEmailService();
const testService = new UserService(mockLogger, mockEmailService);

await testService.registerUser('test@example.com', 'pass');
console.log(mockLogger.logs); // Verify logs
console.log(mockEmailService.sentEmails); // Verify emails sent

// ============================================
// 5. SOLID PRINCIPLES IN ACTION (Các Nguyên Tắc SOLID)
// ============================================

// 📐 S - Single Responsibility Principle (Nguyên tắc Trách nhiệm Đơn)
// "Mỗi class chỉ làm 1 việc duy nhất"

// ❌ BAD: God class - làm quá nhiều việc
class UserManager {
  validateEmail(email: string): boolean {
    /* ... */
  } // 1. Validate
  hashPassword(password: string): string {
    /* ... */
  } // 2. Hash
  saveToDatabase(user: any): void {
    /* ... */
  } // 3. Database
  sendWelcomeEmail(email: string): void {
    /* ... */
  } // 4. Email
  logActivity(message: string): void {
    /* ... */
  } // 5. Logging
  // TOO MANY RESPONSIBILITIES!
}

// ✅ GOOD: Tách ra thành nhiều classes, mỗi class 1 trách nhiệm
class User {
  // Chỉ chứa data (entity/model)
  constructor(
    public id: string,
    public email: string,
    public password: string
  ) {}
}

class UserValidator {
  // CHỈ làm validate
  validate(user: User): boolean {
    return user.email.includes('@') && user.password.length >= 8;
  }
}

class UserRepository {
  // CHỈ làm database operations
  async save(user: User): Promise<void> {
    console.log('💾 Lưu user vào database...');
    // Database logic: INSERT INTO users...
  }

  async findById(id: string): Promise<User | null> {
    console.log(`🔍 Tìm user theo ID: ${id}`);
    // Database logic: SELECT * FROM users WHERE id = ?
    return null;
  }
}

// 💡 Lợi ích:
// - Dễ hiểu: đọc tên class là biết làm gì
// - Dễ maintain: sửa validation → chỉ sửa UserValidator
// - Dễ test: test từng class riêng biệt
// - Dễ reuse: UserValidator có thể dùng cho nhiều nơi

// 📐 O - Open/Closed Principle (Nguyên tắc Mở-Đóng)
// "Mở cho mở rộng (extension), đóng cho sửa đổi (modification)"

// ❌ BAD: Phải sửa code mỗi khi thêm discount type mới
class DiscountCalculator {
  calculate(price: number, type: string, value: number): number {
    if (type === 'percentage') {
      return price * (1 - value / 100);
    } else if (type === 'fixed') {
      return price - value;
    } else if (type === 'bogo') {
      // Thêm type mới → PHẢI SỬA CODE
      return price / 2;
    }
    return price;
  }
}

// ✅ GOOD: Dùng abstract class + inheritance
abstract class Discount {
  abstract calculate(price: number): number; // Abstract method
}

// 1️⃣ Giảm giá theo %
class PercentageDiscount extends Discount {
  constructor(private percent: number) {
    super();
  }

  calculate(price: number): number {
    return price * (1 - this.percent / 100);
  }
}

// 2️⃣ Giảm giá cố định
class FixedDiscount extends Discount {
  constructor(private amount: number) {
    super();
  }

  calculate(price: number): number {
    return Math.max(0, price - this.amount);
  }
}

// 3️⃣ Mua 1 tặng 1 (Buy One Get One)
class BuyOneGetOne extends Discount {
  calculate(price: number): number {
    return price / 2;
  }
}

// 4️⃣ Thêm discount type MỚI → KHÔNG CẦN SỬA code cũ!
class SeasonalDiscount extends Discount {
  constructor(private multiplier: number) {
    super();
  }

  calculate(price: number): number {
    return price * this.multiplier;
  }
}

// 🎯 Sử dụng
function applyDiscount(price: number, discount: Discount): number {
  return discount.calculate(price); // Polymorphism
}

const price = 100_000;
console.log(applyDiscount(price, new PercentageDiscount(20))); // 80,000
console.log(applyDiscount(price, new FixedDiscount(15_000))); // 85,000
console.log(applyDiscount(price, new BuyOneGetOne())); // 50,000
console.log(applyDiscount(price, new SeasonalDiscount(0.7))); // 70,000

// 💡 Lợi ích:
// - Thêm tính năng mới → chỉ cần thêm class mới
// - KHÔNG sửa code cũ → không risk break existing features
// - Tuân thủ Open/Closed: Open for extension, Closed for modification

// 📐 L - Liskov Substitution Principle (Nguyên tắc Thay thế Liskov)
// "Subclass phải thay thế được parent mà không làm break code"

// ❌ BAD: Subclass vi phạm "contract" của parent
abstract class Bird {
  abstract fly(): void; // Tất cả birds đều fly
}

class Sparrow extends Bird {
  fly(): void {
    console.log('🐦 Chim sẻ bay!');
  }
}

class Penguin extends Bird {
  fly(): void {
    // ❌ Chim cánh cụt KHÔNG bay được!
    throw new Error('Penguins cannot fly!');
  }
}

function makeBirdFly(bird: Bird) {
  bird.fly(); // Expect tất cả birds đều fly
}

makeBirdFly(new Sparrow()); // ✅ OK
makeBirdFly(new Penguin()); // ❌ Error! Violate LSP

// ✅ GOOD: Subclass tuân thủ parent contract
abstract class PaymentMethod {
  abstract processPayment(amount: number): Promise<boolean>;

  validateAmount(amount: number): boolean {
    return amount > 0 && amount < 1_000_000;
  }
}

class CreditCardPayment extends PaymentMethod {
  constructor(private provider: string, private cardNumber: string) {
    super();
  }

  async processPayment(amount: number): Promise<boolean> {
    console.log(`💳 Thanh toán ${amount}đ qua thẻ ${this.provider}`);
    return true; // ✅ Tuân thủ contract: return boolean
  }
}

class BankTransferPayment extends PaymentMethod {
  constructor(private bank: string, private bankCode: string) {
    super();
  }

  async processPayment(amount: number): Promise<boolean> {
    console.log(`🏦 Chuyển khoản ${amount}đ qua ${this.bank}`);
    return true; // ✅ Tuân thủ contract: return boolean
  }
}

// 🎯 Function chấp nhận BẤT KỲ PaymentMethod nào
async function processPayment(method: PaymentMethod, amount: number) {
  // Works với TẤT CẢ subclasses → LSP satisfied
  if (method.validateAmount(amount)) {
    const success = await method.processPayment(amount);
    console.log(success ? '✅ Thành công' : '❌ Thất bại');
  }
}

// ✅ Cả 2 đều work perfect (Liskov Substitution)
await processPayment(new CreditCardPayment('Visa', '1234'), 100_000);
await processPayment(new BankTransferPayment('ACB', '970416'), 200_000);

// 💡 Lợi ích:
// - Code predictable: subclass behave như parent
// - Safe refactoring: thay parent → subclass mà không break
// - Polymorphism đúng nghĩa: "nhiều hình dạng, cùng interface"

// 📐 I - Interface Segregation Principle (Nguyên tắc Tách Interface)
// "Nhiều interfaces nhỏ > 1 interface lớn"
// "Class chỉ implement methods cần thiết, không bị ép implement methods không dùng"

// ❌ BAD: Interface quá lớn, ép implement methods không cần
interface IFile {
  read(): string;
  write(data: string): void;
  delete(): void;
  compress(): void;
  encrypt(): void;
}

// ReadOnlyFile bị ép implement write/delete/compress/encrypt (không cần!)
class ReadOnlyFile implements IFile {
  read(): string {
    return 'file content';
  }

  write(data: string): void {
    throw new Error('Read-only!'); // ❌ Không cần nhưng phải implement
  }

  delete(): void {
    throw new Error('Cannot delete!'); // ❌ Không cần nhưng phải implement
  }

  compress(): void {
    throw new Error('Cannot compress!'); // ❌ Không cần nhưng phải implement
  }

  encrypt(): void {
    throw new Error('Cannot encrypt!'); // ❌ Không cần nhưng phải implement
  }
}

// ✅ GOOD: Tách thành nhiều interfaces nhỏ, focused
interface IReadable {
  read(): string;
}

interface IWritable {
  write(data: string): void;
}

interface IDeletable {
  delete(): void;
}

interface ICompressible {
  compress(): void;
}

interface IEncryptable {
  encrypt(key: string): void;
}

// ✅ ReadOnlyFile: chỉ implement IReadable
class ReadOnlyFile implements IReadable {
  read(): string {
    return '📄 Đọc file content...';
  }
  // KHÔNG cần implement write/delete/compress/encrypt
}

// ✅ FullAccessFile: implement nhiều interfaces tùy nhu cầu
class FullAccessFile implements IReadable, IWritable, IDeletable {
  read(): string {
    return '📄 Đọc file...';
  }

  write(data: string): void {
    console.log(`✍️ Ghi data: ${data}`);
  }

  delete(): void {
    console.log('🗑️ Xóa file...');
  }
}

// ✅ SecureFile: implement read/write + encrypt
class SecureFile implements IReadable, IWritable, IEncryptable {
  read(): string {
    return '🔒 Đọc encrypted file...';
  }

  write(data: string): void {
    console.log(`🔒 Ghi encrypted data...`);
  }

  encrypt(key: string): void {
    console.log(`🔐 Mã hóa file với key: ${key}`);
  }
}

// 🎯 Sử dụng
const readOnly = new ReadOnlyFile();
readOnly.read(); // ✅ OK

const fullAccess = new FullAccessFile();
fullAccess.read();
fullAccess.write('new data');
fullAccess.delete();

const secure = new SecureFile();
secure.read();
secure.write('sensitive data');
secure.encrypt('my-secret-key');

// 💡 Lợi ích:
// - Class chỉ implement methods cần thiết
// - Tránh "fat interfaces" khó maintain
// - Dễ compose: kết hợp nhiều small interfaces
// - Follow Single Responsibility: mỗi interface 1 mục đích

// 📐 D - Dependency Inversion Principle (Nguyên tắc Đảo ngược Phụ thuộc)
// "Phụ thuộc vào ABSTRACTIONS (interfaces/abstract classes), KHÔNG phụ thuộc vào CONCRETIONS (concrete classes)"

// ❌ BAD: Phụ thuộc trực tiếp vào concrete classes (tight coupling)
class OrderService {
  private paymentProcessor = new CreditCardPayment('Visa', '1234'); // ❌ Hardcoded
  private logger = new ConsoleLogger(); // ❌ Hardcoded

  async checkout(amount: number): Promise<void> {
    this.logger.log(`Processing order: $${amount}`);
    await this.paymentProcessor.processPayment(amount);
  }

  // 🤔 Vấn đề:
  // - Không thể thay đổi payment method (bị lock vào CreditCardPayment)
  // - Không thể test với mock logger (bị lock vào ConsoleLogger)
  // - Tight coupling: OrderService phụ thuộc vào concrete implementations
}

// ✅ GOOD: Phụ thuộc vào abstractions (interfaces) → Dependency Injection
class OrderService {
  constructor(
    private paymentProcessor: PaymentMethod, // ✅ Abstraction (abstract class)
    private logger: ILogger // ✅ Abstraction (interface)
  ) {
    // ✅ Ưu điểm:
    // - Inject bất kỳ PaymentMethod implementation nào (CreditCard, BankTransfer, Momo...)
    // - Inject bất kỳ ILogger implementation nào (ConsoleLogger, FileLogger, RemoteLogger...)
    // - Dễ test: inject mock implementations
  }

  async checkout(amount: number): Promise<void> {
    this.logger.log(`🛒 Đang xử lý đơn hàng: ${amount}đ`);
    const success = await this.paymentProcessor.processPayment(amount);

    if (success) {
      this.logger.log('✅ Thanh toán thành công!');
    } else {
      this.logger.log('❌ Thanh toán thất bại!');
    }
  }
}

// 🎯 Production: Dùng real implementations
const productionOrderService = new OrderService(
  new CreditCardPayment('Mastercard', '5678'),
  new ConsoleLogger()
);

// 🧪 Testing: Dùng mock implementations
class MockPaymentMethod extends PaymentMethod {
  async processPayment(amount: number): Promise<boolean> {
    console.log(`[MOCK] Processing ${amount}`);
    return true; // Always success for testing
  }
  validateAmount(amount: number): boolean {
    return true;
  }
}

class MockLogger implements ILogger {
  logs: string[] = [];
  log(message: string): void {
    this.logs.push(message); // Capture logs để verify
  }
}

const mockLogger = new MockLogger();
const testOrderService = new OrderService(new MockPaymentMethod(), mockLogger);

await testOrderService.checkout(100_000);
console.log(mockLogger.logs); // ['🛒 Đang xử lý đơn hàng: 100000đ', '✅ Thanh toán thành công!']

// 🌍 Different environments: Dễ dàng swap implementations
class FileLogger implements ILogger {
  log(message: string): void {
    // Ghi vào file thay vì console
    console.log(`[FILE] ${message}`);
  }
}

const fileLoggerOrderService = new OrderService(
  new BankTransferPayment('VietcomBank', '970436'),
  new FileLogger() // ✅ Thay logger mà không sửa OrderService!
);

// 💡 Lợi ích:
// - Loose coupling: OrderService không phụ thuộc concrete classes
// - Flexible: dễ swap implementations (dev/staging/production)
// - Testable: inject mocks cho unit tests
// - Follow SOLID: Single Responsibility + Open/Closed + Dependency Inversion

// ============================================
// 6. VÍ DỤ THỰC TẾ: HỆ THỐNG TRADING (Giao dịch Chứng khoán)
// ============================================
// 🎯 Áp dụng TẤT CẢ SOLID principles + Composition + Dependency Injection

// 📋 1. Định nghĩa Interfaces (Contracts)
interface IOrderValidator {
  validate(order: Order): boolean; // Validate lệnh giao dịch
}

interface IOrderExecutor {
  execute(order: Order): Promise<void>; // Thực thi lệnh
}

interface IRiskManager {
  checkRisk(order: Order): boolean; // Kiểm tra rủi ro
}

// 📦 2. Entity: Order (Lệnh giao dịch)
class Order {
  constructor(
    public symbol: string, // Mã CK: 'AAPL', 'VNM', 'HPG'...
    public quantity: number, // Số lượng: 100, 500...
    public price: number, // Giá: 150, 75.5...
    public side: 'BUY' | 'SELL' // Mua/Bán
  ) {}

  // Helper method: tính giá trị lệnh
  getValue(): number {
    return this.quantity * this.price;
  }
}

// 🔍 3. OrderValidator: Validate lệnh (Single Responsibility)
class OrderValidator implements IOrderValidator {
  validate(order: Order): boolean {
    // Kiểm tra số lượng và giá hợp lệ
    if (order.quantity <= 0) {
      console.log('❌ Số lượng phải > 0');
      return false;
    }

    if (order.price <= 0) {
      console.log('❌ Giá phải > 0');
      return false;
    }

    if (!order.symbol || order.symbol.trim() === '') {
      console.log('❌ Mã CK không hợp lệ');
      return false;
    }

    console.log('✅ Lệnh hợp lệ');
    return true;
  }
}

// ⚠️ 4. RiskManager: Kiểm tra rủi ro (Single Responsibility)
class RiskManager implements IRiskManager {
  constructor(
    private maxOrderValue: number // Giá trị lệnh tối đa (VD: 100 triệu)
  ) {}

  checkRisk(order: Order): boolean {
    const orderValue = order.getValue();

    if (orderValue > this.maxOrderValue) {
      console.log(
        `⚠️ Vượt hạn mức! Giá trị lệnh: ${orderValue}đ > Hạn mức: ${this.maxOrderValue}đ`
      );
      return false;
    }

    console.log(`✅ Trong hạn mức. Giá trị lệnh: ${orderValue}đ`);
    return true;
  }
}

// 🚀 5. OrderExecutor: Thực thi lệnh (Single Responsibility)
class OrderExecutor implements IOrderExecutor {
  async execute(order: Order): Promise<void> {
    console.log(
      `🚀 Đang gửi lệnh ${order.side} ${order.quantity} ${order.symbol} @ ${order.price}đ...`
    );

    // Call Exchange API (HOSE, HNX, NASDAQ...)
    await this.callExchangeAPI(order);

    console.log('✅ Lệnh đã được gửi đến sàn');
  }

  private async callExchangeAPI(order: Order): Promise<void> {
    // Simulate API call
    await new Promise((resolve) => setTimeout(resolve, 100));
    // Real: await axios.post('/api/orders', order);
  }
}

// 🎯 6. TradingService: Orchestrate (điều phối) tất cả services
// ✅ Dependency Inversion: phụ thuộc vào interfaces, không phải concrete classes
class TradingService {
  constructor(
    private validator: IOrderValidator, // ✅ Interface
    private riskManager: IRiskManager, // ✅ Interface
    private executor: IOrderExecutor, // ✅ Interface
    private logger: ILogger // ✅ Interface
  ) {
    // 💉 Dependency Injection: inject tất cả dependencies qua constructor
  }

  async placeOrder(order: Order): Promise<void> {
    this.logger.log(
      `📝 Đặt lệnh: ${order.side} ${order.quantity} ${order.symbol}`
    );

    // 1️⃣ Validate lệnh
    if (!this.validator.validate(order)) {
      throw new Error('Lệnh không hợp lệ!');
    }

    // 2️⃣ Kiểm tra rủi ro
    if (!this.riskManager.checkRisk(order)) {
      throw new Error('Vượt hạn mức rủi ro!');
    }

    // 3️⃣ Thực thi lệnh
    await this.executor.execute(order);

    this.logger.log(`✅ Đặt lệnh thành công: ${order.symbol}`);
  }
}

// 🔧 7. Wire up dependencies (Dependency Injection Container)
const tradingService = new TradingService(
  new OrderValidator(), // Inject validator
  new RiskManager(100_000_000), // Inject risk manager (hạn mức 100 triệu)
  new OrderExecutor(), // Inject executor
  new ConsoleLogger() // Inject logger
);

// 🎯 8. Sử dụng
const buyOrder = new Order('AAPL', 100, 150, 'BUY');
await tradingService.placeOrder(buyOrder);

const sellOrder = new Order('VNM', 500, 75.5, 'SELL');
await tradingService.placeOrder(sellOrder);

// ❌ Lệnh không hợp lệ
try {
  const invalidOrder = new Order('HPG', -10, 50, 'BUY'); // Số lượng âm
  await tradingService.placeOrder(invalidOrder);
} catch (error) {
  console.log(error.message); // 'Lệnh không hợp lệ!'
}

// ❌ Vượt hạn mức
try {
  const bigOrder = new Order('AAPL', 1_000_000, 200, 'BUY'); // 200 triệu > 100 triệu
  await tradingService.placeOrder(bigOrder);
} catch (error) {
  console.log(error.message); // 'Vượt hạn mức rủi ro!'
}

// 💡 Lợi ích của architecture này:
// ✅ Single Responsibility: mỗi class 1 nhiệm vụ
// ✅ Open/Closed: thêm validator/risk rule mới mà không sửa code cũ
// ✅ Liskov Substitution: thay OrderValidator bằng AdvancedOrderValidator
// ✅ Interface Segregation: interfaces nhỏ, focused
// ✅ Dependency Inversion: TradingService phụ thuộc interfaces
// ✅ Testable: dễ inject mocks cho unit tests
// ✅ Maintainable: dễ hiểu, dễ sửa, dễ extend

// ============================================
// 7. TESTING với Vitest (Dễ mock nhờ Composition + DI)
// ============================================
import { describe, it, expect, vi } from 'vitest';

describe('TradingService', () => {
  it('✅ should place order when valid (khi lệnh hợp lệ)', async () => {
    // 🧪 Tạo mocks cho tất cả dependencies
    const mockValidator = {
      validate: vi.fn(() => true), // Mock return true (lệnh hợp lệ)
    };
    const mockRiskManager = {
      checkRisk: vi.fn(() => true), // Mock return true (trong hạn mức)
    };
    const mockExecutor = {
      execute: vi.fn(), // Mock execute (không thực thi thật)
    };
    const mockLogger = {
      log: vi.fn(), // Mock log (capture logs)
    };

    // 💉 Inject mocks vào TradingService
    const service = new TradingService(
      mockValidator,
      mockRiskManager,
      mockExecutor,
      mockLogger
    );

    // 🎯 Test action: đặt lệnh
    const order = new Order('AAPL', 100, 150, 'BUY');
    await service.placeOrder(order);

    // ✅ Verify: các methods đã được gọi với đúng params
    expect(mockValidator.validate).toHaveBeenCalledWith(order);
    expect(mockValidator.validate).toHaveBeenCalledTimes(1);

    expect(mockRiskManager.checkRisk).toHaveBeenCalledWith(order);
    expect(mockRiskManager.checkRisk).toHaveBeenCalledTimes(1);

    expect(mockExecutor.execute).toHaveBeenCalledWith(order);
    expect(mockExecutor.execute).toHaveBeenCalledTimes(1);

    expect(mockLogger.log).toHaveBeenCalledTimes(2); // log 2 lần (bắt đầu + kết thúc)
  });

  it('❌ should throw error when validation fails (khi validate fail)', async () => {
    // 🧪 Mock validator return false
    const mockValidator = {
      validate: vi.fn(() => false), // ❌ Lệnh không hợp lệ
    };
    const mockRiskManager = { checkRisk: vi.fn() };
    const mockExecutor = { execute: vi.fn() };
    const mockLogger = { log: vi.fn() };

    const service = new TradingService(
      mockValidator,
      mockRiskManager,
      mockExecutor,
      mockLogger
    );

    const order = new Order('AAPL', -10, 150, 'BUY'); // Số lượng âm

    // ✅ Expect throw error
    await expect(service.placeOrder(order)).rejects.toThrow(
      'Lệnh không hợp lệ!'
    );

    // ✅ Verify: executor KHÔNG được gọi (vì validate fail)
    expect(mockExecutor.execute).not.toHaveBeenCalled();
  });

  it('❌ should throw error when risk check fails (khi vượt hạn mức)', async () => {
    // 🧪 Mock risk manager return false
    const mockValidator = { validate: vi.fn(() => true) };
    const mockRiskManager = {
      checkRisk: vi.fn(() => false), // ❌ Vượt hạn mức
    };
    const mockExecutor = { execute: vi.fn() };
    const mockLogger = { log: vi.fn() };

    const service = new TradingService(
      mockValidator,
      mockRiskManager,
      mockExecutor,
      mockLogger
    );

    const order = new Order('AAPL', 1_000_000, 200, 'BUY'); // Lệnh quá lớn

    // ✅ Expect throw error
    await expect(service.placeOrder(order)).rejects.toThrow(
      'Vượt hạn mức rủi ro!'
    );

    // ✅ Verify: executor KHÔNG được gọi (vì risk check fail)
    expect(mockExecutor.execute).not.toHaveBeenCalled();
  });

  it('📊 should log correct messages (kiểm tra logs)', async () => {
    const mockValidator = { validate: vi.fn(() => true) };
    const mockRiskManager = { checkRisk: vi.fn(() => true) };
    const mockExecutor = { execute: vi.fn() };
    const mockLogger = { log: vi.fn() };

    const service = new TradingService(
      mockValidator,
      mockRiskManager,
      mockExecutor,
      mockLogger
    );

    const order = new Order('VNM', 500, 75.5, 'SELL');
    await service.placeOrder(order);

    // ✅ Verify logs
    expect(mockLogger.log).toHaveBeenCalledWith('📝 Đặt lệnh: SELL 500 VNM');
    expect(mockLogger.log).toHaveBeenCalledWith('✅ Đặt lệnh thành công: VNM');
  });
});

// 💡 Lợi ích của testing với Composition + DI:
// ✅ Dễ mock: inject mock dependencies thay vì real implementations
// ✅ Isolated tests: test từng unit riêng biệt, không phụ thuộc external services
// ✅ Fast: không call API thật, không database thật
// ✅ Predictable: mock return cố định → tests deterministic
// ✅ Coverage: dễ test edge cases (validation fail, risk fail, errors...)
```

---

**Best Practices:**

1. **Prefer Composition Over Inheritance**

   ```typescript
   // ❌ BAD: Inheritance
   class UserService extends Logger {}

   // ✅ GOOD: Composition
   class UserService {
     constructor(private logger: Logger) {}
   }
   ```

2. **Use Private Fields `#` cho Encapsulation**

   ```typescript
   class User {
     #password: string; // Truly private

     // ❌ NOT this._password (convention only)
   }
   ```

3. **Dependency Injection cho Testability**

   ```typescript
   // ✅ GOOD: Inject dependencies
   class Service {
     constructor(private db: IDatabase, private logger: ILogger) {}
   }
   ```

4. **Abstract Classes cho Shared Logic**

   ```typescript
   abstract class BaseRepository<T> {
     abstract tableName: string;

     // Shared method
     async findById(id: string): Promise<T | null> {
       // Common query logic
     }
   }
   ```

5. **Interfaces cho Contract**

   ```typescript
   interface IPaymentGateway {
     charge(amount: number): Promise<boolean>;
     refund(transactionId: string): Promise<void>;
   }
   ```

6. **Single Responsibility Principle**

   ```typescript
   // ✅ One class = one job
   class UserValidator {
     validate() {}
   }
   class UserRepository {
     save() {}
   }
   class UserService {
     register() {}
   }
   ```

7. **Readonly Properties cho Immutability**
   ```typescript
   class Order {
     constructor(public readonly id: string, public readonly createdAt: Date) {}
   }
   ```

---

**Common Mistakes:**

1. **❌ Deep Inheritance Hierarchies**

   ```typescript
   // TOO DEEP!
   class A {}
   class B extends A {}
   class C extends B {}
   class D extends C {} // Hard to maintain

   // ✅ Use composition instead
   ```

2. **❌ Exposing Internal State**

   ```typescript
   class User {
     public password: string; // ❌ Exposed!

     // ✅ Use private field + getter
     #password: string;
     setPassword(pwd: string) {
       this.#password = hashPassword(pwd);
     }
   }
   ```

3. **❌ God Classes (Too Many Responsibilities)**

   ```typescript
   class UserManager {
     validateUser() {}
     saveUser() {}
     sendEmail() {}
     logActivity() {}
     // ❌ Too many jobs! Split into separate classes
   }
   ```

4. **❌ Tight Coupling với Concrete Classes**

   ```typescript
   class Service {
     private logger = new ConsoleLogger(); // ❌ Hardcoded

     // ✅ Inject abstraction
     constructor(private logger: ILogger) {}
   }
   ```

5. **❌ Không Override `constructor` Correctly**

   ```typescript
   class Child extends Parent {
     constructor(name: string) {
       this.name = name; // ❌ Must call super() first!
       super();
     }

     // ✅ Correct order
     constructor(name: string) {
       super();
       this.name = name;
     }
   }
   ```

6. **❌ Overriding Private Methods**

   ```typescript
   class Parent {
     #privateMethod() {} // Cannot override in child
   }

   // ✅ Use protected in TypeScript
   class Parent {
     protected method() {} // Can override
   }
   ```

7. **❌ Không Validate trong Constructor**

   ```typescript
   class User {
     constructor(email: string) {
       this.email = email; // ❌ No validation
     }

     // ✅ Validate immediately
     constructor(email: string) {
       if (!email.includes('@')) throw new Error('Invalid email');
       this.email = email;
     }
   }
   ```

---
