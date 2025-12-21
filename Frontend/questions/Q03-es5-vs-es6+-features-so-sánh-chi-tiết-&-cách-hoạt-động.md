# ⚡ Q03: ES5 vs ES6+ Features - So Sánh Chi Tiết & Cách Hoạt Động

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"ES6+ (2015+) mang lại JavaScript hiện đại với classes, modules, arrow functions, async/await.**

**📊 ES5 vs ES6+ (Key Differences):**

| Feature       | ES5 (2009)              | ES6+ (2015+)                     |
| ------------- | ----------------------- | -------------------------------- |
| **Variables** | `var` (function scope)  | `let/const` (block scope)        |
| **Functions** | `function() {}`         | Arrow `() => {}`                 |
| **Classes**   | Prototype + constructor | `class` syntax                   |
| **Modules**   | CommonJS/AMD            | `import/export`                  |
| **Strings**   | Concatenation `+`       | Template literals `` `${}` ``    |
| **Objects**   | Manual copy             | Spread `{...obj}`, destructuring |
| **Async**     | Callbacks               | Promises, async/await            |
| **Loops**     | `for`, `while`          | `for...of`, `forEach`, `map`     |

**🔥 ES6+ Must-Know Features:**

1. **let/const**: Block scope → avoid hoisting issues, `const` prevent reassignment.
2. **Arrow Functions**: Lexical `this`, concise syntax, no `arguments` object.
3. **Destructuring**: `const { name } = user`, `const [a, b] = arr` → extract values easily.
4. **Spread/Rest**: `...` operator → copy arrays/objects, function params.
5. **Template Literals**: `` `Hello ${name}` `` → multi-line strings, interpolation.
6. **Classes**: `class Person extends User` → OOP syntax (syntactic sugar cho prototypes).
7. **Modules**: `import { fn } from './module'` → static imports, tree-shaking.
8. **Promises & Async/Await**: Better async handling than callbacks.
9. **Default Parameters**: `function fn(a = 1)` → không cần `a = a || 1`.
10. **Optional Chaining**: `user?.address?.city` → safe navigation (ES2020).
11. **Nullish Coalescing**: `value ?? 'default'` → khác với `||` (chỉ check null/undefined).

**⚡ ES2016-ES2023 Highlights:**

- **ES2016**: `**` (exponentiation), `Array.includes()`.
- **ES2017**: `async/await`, `Object.values/entries()`, string padding.
- **ES2018**: Rest/spread for objects, async iteration.
- **ES2019**: `Array.flat/flatMap()`, `Object.fromEntries()`.
- **ES2020**: Optional chaining `?.`, nullish coalescing `??`, `BigInt`, dynamic import.
- **ES2021**: `String.replaceAll()`, numeric separators `1_000_000`.
- **ES2022**: Top-level await, private fields `#private`, `Array.at()`.
- **ES2023**: `Array.findLast()`, `toSorted()`, `toReversed()` (immutable array methods).

**⚠️ Browser Compatibility:**

- **ES5**: Universal support (IE9+, all browsers).
- **ES6+**: Modern browsers (Chrome 51+, Firefox 54+, Safari 10+).
- **Solution**: Babel transpile ES6+ → ES5 cho legacy browsers.
- **Trend**: Evergreen browsers auto-update → ES6+ safe cho 95%+ users.

**💡 Senior Insights:**

- **Transpilation**: Babel transform ES6+ → ES5 at build time → support old browsers.
- **Polyfills**: Add missing features (e.g., `Promise`, `Array.includes()`) at runtime.
- **Bundle Size**: ES6+ code nhỏ hơn sau minify (classes, arrow functions compact hơn ES5).
- **Performance**: Modern engines optimize ES6+ better (e.g., arrow functions, spread).
- **Best Practice**: Write ES6+, transpile for production, use feature detection (`if ('fetch' in window)`).

**🎯 Migration Tips:**

- Replace `var` → `let/const` (use ESLint rule).
- Replace `function` → arrow functions (except methods, constructors).
- Use destructuring để extract values.
- Replace string concat → template literals.
- Use `async/await` thay vì `.then()` chains.

---

**⚡ Quick Summary:**

> ES6+ = let/const, arrow functions, classes, destructuring, promises, modules. ES5 = var, function, callbacks

**💡 Ghi Nhớ:**

- 🔥 **ES6 Key Features**: let/const, =>, class, {...spread}, [destructuring], `template`, Promise, import/export
- 📦 **Block Scope**: let/const có block scope, var có function scope
- ⚡ **Arrow Function**: Không có `this` riêng, không có `arguments`, không dùng làm constructor
- 🎯 **Classes**: Syntactic sugar cho prototype-based inheritance

**Trả lời:**

- **ES5 (ECMAScript 5, 2009)**: JavaScript cơ bản với function declarations, var, prototype-based inheritance, callbacks
- **ES6/ES2015+ (2015-now)**: Modern JavaScript với classes, modules, arrow functions, destructuring, promises, async/await
- **🔥 Ưu điểm ES6+**: Code ngắn gọn hơn 30-50%, type-safe hơn với const/let, performance tốt hơn với optimizations, syntax hiện đại dễ đọc
- **⚠️ Nhược điểm ES6+**: Cần transpilation (Babel) cho IE11 và older browsers, learning curve cao hơn, bundle size có thể lớn hơn

**🎯 Timeline & Browser Support:**

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    JAVASCRIPT EVOLUTION TIMELINE                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  📅 ES5 (2009) - Stable, Universal Support                              │
│     ✅ All browsers (IE9+)                                              │
│     ✅ No transpilation needed                                          │
│     ❌ Verbose syntax, limited features                                 │
│                                                                          │
│  📅 ES6/ES2015 (2015) - Major Update                                    │
│     • Classes, Modules, Arrow Functions                                 │
│     • let/const, Template Literals                                      │
│     • Destructuring, Spread/Rest                                        │
│     • Promises, Symbols, Iterators                                      │
│     ✅ Modern browsers (Chrome 51+, Firefox 54+, Safari 10+)           │
│     ⚠️  Needs Babel for IE11                                            │
│                                                                          │
│  📅 ES2016-ES2023 (Yearly Updates)                                      │
│     • Async/Await (ES2017)                                              │
│     • Optional Chaining ?. (ES2020)                                     │
│     • Nullish Coalescing ?? (ES2020)                                    │
│     • BigInt, Dynamic Import                                            │
│     • Private Fields, Top-level await                                   │
│     ✅ Evergreen browsers auto-update                                   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

**Code Example - Comprehensive Comparison:**

```typescript
// ============================================
// 1. VARIABLES - var vs let/const
// ============================================

// 🔴 ES5 - var (Function Scoped, Hoisted - Phạm Vi Function, Hoisted)
// Cách hoạt động: var được hoist lên đầu function scope
function es5Variables() {
  // 💡 es5Variables: Function để demo var behavior
  // 💡 var: Function scoped → Accessible trong toàn bộ function

  console.log(x); // undefined (hoisted nhưng chưa gán giá trị)
  // 💡 Hoisting: var x được "nâng lên" đầu function scope
  // 💡 Nhưng giá trị chưa được assign → undefined
  // 💡 Không bị ReferenceError → Khác với let/const

  var x = 10; // Function scoped - accessible trong toàn bộ function
  // 💡 var x = 10: Declare và assign giá trị
  // 💡 Function scoped: Accessible trong toàn bộ function (không chỉ trong block)
  // 💡 Có thể access x từ bất kỳ đâu trong function

  if (true) {
    var x = 20; // CÙNG biến x (không tạo scope mới)
    // 💡 var x = 20: Không tạo biến mới → Ghi đè biến x ở trên
    // 💡 if block không tạo scope mới cho var
    // 💡 → x trong if block = x trong function scope
  }

  console.log(x); // 20 (bị ghi đè bởi if block)
  // 💡 x = 20: Bị ghi đè bởi if block
  // 💡 ⚠️ Vấn đề: Khó debug, dễ gây bugs

  // var có thể redeclare (var có thể khai báo lại)
  var x = 30; // ✅ OK - không error
  // 💡 var x = 30: Redeclare cùng biến → Không error
  // 💡 ⚠️ Vấn đề: Có thể vô tình redeclare → Khó maintain

  console.log(x); // 30
  // 💡 x = 30: Giá trị cuối cùng
}

// 🟢 ES6+ - let/const (Block Scoped, Temporal Dead Zone - Phạm Vi Block, Vùng Chết Tạm Thời)
// Cách hoạt động: let/const chỉ tồn tại trong {} block, có TDZ
function es6Variables() {
  // 💡 es6Variables: Function để demo let/const behavior
  // 💡 let/const: Block scoped → Chỉ accessible trong block {}

  // console.log(y); // ❌ ReferenceError: Cannot access before initialization
  // 💡 TDZ (Temporal Dead Zone): Vùng từ đầu block đến khi declare
  // 💡 Không thể access y trước khi declare → ReferenceError
  // 💡 Khác với var: var → undefined, let/const → ReferenceError
  // Temporal Dead Zone (TDZ) - từ đầu block đến khi declare

  let y = 10; // Block scoped - chỉ trong function này
  // 💡 let y = 10: Declare và assign
  // 💡 Block scoped: Chỉ accessible trong function scope này
  // 💡 Không thể redeclare trong cùng scope

  const z = 100; // Immutable reference - không thể reassign
  // 💡 const z = 100: Declare và assign (phải assign ngay)
  // 💡 Immutable reference: Không thể reassign z
  // 💡 Nhưng object/array properties vẫn có thể thay đổi

  if (true) {
    let y = 20; // BIẾN MỚI - scope riêng trong if block
    // 💡 let y = 20: Tạo biến MỚI trong if block scope
    // 💡 Không ghi đè y ở function scope → Block scoped
    // 💡 ✅ Tốt: Mỗi block có scope riêng → Dễ debug

    const z = 200; // BIẾN MỚI - scope riêng
    // 💡 const z = 200: Tạo biến MỚI trong if block scope
    // 💡 Không ghi đè z ở function scope → Block scoped

    console.log(y); // 20 (biến local của if)
    // 💡 y = 20: Lấy từ if block scope → Không ảnh hưởng function scope
    console.log(z); // 200
    // 💡 z = 200: Lấy từ if block scope
  }

  console.log(y); // 10 (biến của function scope, không bị ảnh hưởng)
  // 💡 y = 10: Lấy từ function scope → Không bị ảnh hưởng bởi if block
  // 💡 ✅ Tốt: Block scoped → Không bị ghi đè → Predictable
  console.log(z); // 100
  // 💡 z = 100: Lấy từ function scope → Không bị ảnh hưởng

  // let y = 30;  // ❌ SyntaxError: Identifier 'y' has already been declared
  // 💡 Không thể redeclare let trong cùng scope
  // 💡 ✅ Tốt: Prevent accidental redeclaration → Type safety

  // z = 300;     // ❌ TypeError: Assignment to constant variable
  // 💡 Không thể reassign const
  // 💡 ✅ Tốt: Prevent accidental reassignment → Immutability

  // const cho objects - reference immutable, nhưng properties mutable
  const obj = { name: 'John' }; // 📦 Object với const
  // 💡 const obj: Reference immutable → Không thể reassign obj
  // 💡 Nhưng properties của object vẫn mutable

  obj.name = 'Jane'; // ✅ OK - thay đổi property
  // 💡 obj.name = 'Jane': Thay đổi property → OK
  // 💡 const chỉ prevent reassign reference, không prevent mutate properties
  // 💡 obj vẫn point đến cùng object → Chỉ properties thay đổi

  // obj = {};      // ❌ Error - không thể reassign reference
  // 💡 obj = {}: Reassign reference → Error
  // 💡 const prevent reassign reference → Immutable reference
}

// Hoisting Comparison (Cách hoạt động của hoisting)
console.log('=== VAR HOISTING ===');
console.log(varVariable); // undefined - hoisted, chưa assigned
var varVariable = 'ES5';

console.log('=== LET/CONST HOISTING ===');
// console.log(letVariable); // ❌ ReferenceError - TDZ
let letVariable = 'ES6';
// const constVariable; // ❌ SyntaxError - const phải init ngay

// ============================================
// 2. FUNCTIONS - Regular vs Arrow
// ============================================

// 🔴 ES5 - Regular Functions (có own this binding - Có Binding This Riêng)
// Cách hoạt động: this binding dynamic, phụ thuộc vào cách gọi
var Calculator = {
  // 💡 Calculator: Object với methods
  value: 0, // 📊 Property: Giá trị hiện tại

  // Method với regular function (Method với Function Thông Thường)
  add: function (num) {
    // 💡 add: Method với regular function
    // 💡 Regular function: Có own this binding → this = object gọi method

    this.value += num; // this = Calculator object
    // 💡 this.value: this = Calculator → Access Calculator.value
    // 💡 Dynamic binding: this phụ thuộc vào cách gọi function
    // 💡 Method call: calculator.add(5) → this = calculator

    return this.value; // 📤 Return giá trị mới
  },

  // Callback problem (Vấn Đề Callback)
  delayedAdd: function (num) {
    // 💡 delayedAdd: Method với callback
    // 💡 setTimeout: Callback function → this binding khác

    setTimeout(function () {
      // 💡 setTimeout callback: Regular function → this binding khác
      // this ở đây = window (hoặc undefined trong strict mode)
      // 💡 this trong callback ≠ Calculator → this = window/undefined
      // Không phải Calculator object!
      // 💡 ⚠️ Vấn đề: this binding bị mất → Không access được Calculator

      console.log(this); // window/undefined
      // 💡 this = window (non-strict) hoặc undefined (strict mode)
      // 💡 Không phải Calculator → Không access được Calculator.value

      // this.value += num; // ❌ Error hoặc NaN
      // 💡 this.value: undefined.value → Error
      // 💡 Hoặc window.value (undefined) + num → NaN
    }, 1000);
  },

  // ES5 solution: bind hoặc that = this (Giải Pháp ES5)
  delayedAddFixed: function (num) {
    // 💡 delayedAddFixed: Solution với closure
    var that = this; // Lưu reference
    // 💡 that = this: Lưu reference đến Calculator vào biến that
    // 💡 Closure: that accessible trong callback → Preserve this

    setTimeout(function () {
      // 💡 setTimeout callback: Access that từ closure
      that.value += num; // ✅ Hoạt động
      // 💡 that.value: that = Calculator → Access Calculator.value
      // 💡 ✅ Solution: Closure preserve this → Hoạt động đúng
    }, 1000);
  },

  // Hoặc dùng bind (Hoặc Dùng Bind)
  delayedAddBind: function (num) {
    // 💡 delayedAddBind: Solution với bind
    setTimeout(
      function () {
        // 💡 Regular function: Cần bind this
        this.value += num; // ✅ Hoạt động vì đã bind
        // 💡 this.value: this đã được bind = Calculator
        // 💡 ✅ Solution: bind(this) → Preserve this binding
      }.bind(this), // 🔗 Bind this = Calculator
      // 💡 .bind(this): Bind this của delayedAddBind vào callback
      // 💡 this trong callback = Calculator → Hoạt động đúng
      1000
    );
  },
};

// 🟢 ES6+ - Arrow Functions (lexical this binding - Binding This Từ Lexical Scope)
// Cách hoạt động: Arrow function KHÔNG có own this, inherit từ parent scope
const ModernCalculator = {
  // 💡 ModernCalculator: Object với ES6+ syntax
  value: 0, // 📊 Property: Giá trị hiện tại

  // Method shorthand syntax (Cú Pháp Method Ngắn Gọn)
  add(num: number) {
    // 💡 add: Method shorthand (ES6+)
    // 💡 add(num) = add: function(num) → Ngắn gọn hơn
    // 💡 Regular function → this = ModernCalculator

    this.value += num; // ✅ this = ModernCalculator
    // 💡 this.value: this = ModernCalculator → Access value
    // 💡 Method call: modernCalculator.add(5) → this = modernCalculator

    return this.value; // 📤 Return giá trị mới
  },

  // Arrow function trong callback - this tự động đúng (Arrow Function Trong Callback)
  delayedAdd(num: number) {
    // 💡 delayedAdd: Method với arrow function callback
    // 💡 Arrow function: Không có own this → Inherit từ parent scope

    setTimeout(() => {
      // 💡 Arrow function: () => {} → Không có own this
      // this = ModernCalculator (inherit từ delayedAdd method)
      // 💡 Lexical this: this = this của delayedAdd method
      // 💡 delayedAdd là method → this = ModernCalculator
      // 💡 Arrow function inherit this → this = ModernCalculator

      this.value += num; // ✅ Hoạt động perfect
      // 💡 this.value: this = ModernCalculator → Access value
      // 💡 ✅ Perfect: Không cần bind, không cần that → Tự động đúng
      // 💡 Arrow function: Lexical this → Preserve this tự động
    }, 1000);
  },

  // Arrow function không thể dùng làm constructor (Arrow Function Không Thể Làm Constructor)
  // MyClass: () => { } // ❌ Không có prototype, không thể new
  // 💡 Arrow function: Không có prototype property
  // 💡 Không thể dùng với new → TypeError
  // 💡 Chỉ dùng cho: Callbacks, short functions, không cần this binding
};

// Arrow function syntax variations (Các Biến Thể Cú Pháp Arrow Function)
const simple = (x: number) => x * 2; // Implicit return (1 expression)
// 💡 simple: Arrow function với implicit return
// 💡 (x: number) => x * 2: Không có {} → Tự động return x * 2
// 💡 Implicit return: Chỉ 1 expression → Không cần return keyword
// 💡 ✅ Ngắn gọn: Perfect cho simple transformations

const withBlock = (x: number) => {
  // 💡 withBlock: Arrow function với block body
  const result = x * 2; // 📊 Tính toán
  return result; // Explicit return (multiple statements)
  // 💡 Block body {}: Nhiều statements → Cần return explicit
  // 💡 Explicit return: Phải dùng return keyword
};
// 💡 ✅ Flexible: Có thể có nhiều statements

const noParams = () => console.log('Hello'); // No parameters
// 💡 noParams: Arrow function không có parameters
// 💡 (): Bắt buộc khi không có params
// 💡 ✅ Ngắn gọn: Perfect cho simple actions

const oneParam = (x) => x * 2; // Single param - có thể bỏ ()
// 💡 oneParam: Arrow function với 1 parameter
// 💡 (x): Có thể bỏ () nếu chỉ 1 param → x => x * 2
// 💡 ✅ Optional: () có thể bỏ cho single param

const multiParams = (x: number, y: number) => x + y; // Multiple params - cần ()
// 💡 multiParams: Arrow function với nhiều parameters
// 💡 (x, y): Bắt buộc có () khi nhiều params
// 💡 ✅ Required: () bắt buộc cho multiple params

const returnObject = () => ({ name: 'John' }); // Return object - cần wrap ()
// 💡 returnObject: Arrow function return object
// 💡 ({ name: 'John' }): Phải wrap object trong () để return
// 💡 Không có () → { name: 'John' } được hiểu là block body
// 💡 ✅ Wrap required: () để return object literal

// ============================================
// 3. CLASSES - Prototype vs Class Syntax
// ============================================

// 🔴 ES5 - Prototype-based Inheritance (Kế Thừa Dựa Trên Prototype)
// Cách hoạt động: Constructor function + prototype chain
function Animal(name) {
  // 💡 Animal: Constructor function (phải gọi với new)
  // Constructor function (phải gọi với new)
  // 💡 Constructor: Function được dùng với new keyword
  // 💡 new Animal(): Tạo instance mới → this = instance mới

  this.name = name; // Instance property
  // 💡 this.name: Instance property → Mỗi instance có name riêng
  // 💡 this: Trong constructor → this = instance đang được tạo
}

// Methods trên prototype (share giữa instances - Methods Trên Prototype)
Animal.prototype.speak = function () {
  // 💡 Animal.prototype.speak: Method trên prototype
  // 💡 Prototype: Object chứa methods được share giữa tất cả instances
  // 💡 ✅ Efficient: Methods chỉ định nghĩa 1 lần → Tất cả instances share
  // 💡 this.name: this = instance gọi method

  console.log(this.name + ' makes a sound');
  // 💡 String concatenation: ES5 style
};

// Static methods (Methods Tĩnh)
Animal.createAnimal = function (name) {
  // 💡 Animal.createAnimal: Static method
  // 💡 Static: Method trên constructor function (không phải prototype)
  // 💡 Gọi: Animal.createAnimal() → Không cần instance
  // 💡 this: Trong static method → this = constructor function

  return new Animal(name); // 🔧 Tạo instance mới
};

// Inheritance qua prototype chain (Kế Thừa Qua Prototype Chain)
function Dog(name, breed) {
  // 💡 Dog: Constructor function cho Dog
  // 💡 Inheritance: Dog kế thừa từ Animal

  Animal.call(this, name); // Gọi parent constructor
  // 💡 Animal.call(this, name): Gọi Animal constructor với this = Dog instance
  // 💡 .call(): Set this context → this trong Animal = Dog instance
  // 💡 ✅ Setup: Gọi parent constructor để init parent properties

  this.breed = breed; // 📊 Dog-specific property
}

// Set up prototype chain (inheritance - Thiết Lập Prototype Chain)
Dog.prototype = Object.create(Animal.prototype);
// 💡 Object.create(Animal.prototype): Tạo object mới với Animal.prototype là prototype
// 💡 Dog.prototype: Set prototype của Dog = Animal.prototype
// 💡 ✅ Inheritance: Dog instances có thể access Animal methods
// 💡 Prototype chain: dog → Dog.prototype → Animal.prototype → Object.prototype

Dog.prototype.constructor = Dog; // Fix constructor reference
// 💡 Fix constructor: Set constructor = Dog (bị ghi đè bởi Object.create)
// 💡 ✅ Important: Giữ constructor reference đúng → dog.constructor = Dog

// Override method (Ghi Đè Method)
Dog.prototype.speak = function () {
  // 💡 Dog.prototype.speak: Override Animal.speak
  // 💡 Override: Ghi đè method từ parent → Dog có speak riêng
  // 💡 Prototype chain: Tìm speak → Tìm thấy ở Dog.prototype → Dùng Dog.speak

  console.log(this.name + ' barks!');
  // 💡 Dog-specific behavior: "barks" thay vì "makes a sound"
};

const dog = new Dog('Rex', 'Labrador'); // 🐕 Tạo Dog instance
// 💡 new Dog(): Gọi constructor → Tạo instance mới
// 💡 'Rex': name → this.name = 'Rex'
// 💡 'Labrador': breed → this.breed = 'Labrador'

dog.speak(); // "Rex barks!"
// 💡 dog.speak(): Tìm speak trong prototype chain
// 💡 Tìm thấy Dog.prototype.speak → Gọi → "Rex barks!"

// 🟢 ES6+ - Class Syntax (Syntactic Sugar - Cú Pháp Ngọt Ngào)
// Cách hoạt động: Bên trong vẫn là prototype, nhưng syntax dễ đọc hơn
class ModernAnimal {
  // 💡 ModernAnimal: ES6+ class syntax
  // 💡 Class: Syntactic sugar cho prototype-based inheritance
  // 💡 Bên trong: Vẫn dùng prototype, nhưng syntax dễ đọc hơn

  // Class fields (ES2022 - Các Trường Class)
  species = 'Unknown'; // Public field
  // 💡 species: Class field (ES2022)
  // 💡 Public field: Mỗi instance có species = 'Unknown'
  // 💡 ✅ Modern: Không cần khai báo trong constructor

  // Constructor (Hàm Khởi Tạo)
  constructor(public name: string) {
    // 💡 constructor: Hàm khởi tạo instance
    // Parameter properties (TypeScript)
    // 💡 public name: TypeScript parameter property
    // Tự động tạo this.name = name
    // 💡 ✅ Shortcut: public name = this.name = name tự động
    // 💡 Không cần: this.name = name (TypeScript tự động)
  }

  // Instance method (trên prototype - Method Instance)
  speak() {
    // 💡 speak: Instance method
    // 💡 Instance method: Method trên prototype → Share giữa instances
    // 💡 this: this = instance gọi method

    console.log(`${this.name} makes a sound`);
    // 💡 Template literal: ES6+ string interpolation
    // 💡 ${this.name}: Embed expression trong string
  }

  // Static method (trên class itself - Method Tĩnh)
  static createAnimal(name: string) {
    // 💡 static createAnimal: Static method
    // 💡 Static: Method trên class (không phải instance)
    // 💡 Gọi: ModernAnimal.createAnimal() → Không cần instance
    // 💡 this: Trong static method → this = ModernAnimal class

    return new ModernAnimal(name); // 🔧 Tạo instance mới
  }

  // Getter (Bộ Lấy Giá Trị)
  get info() {
    // 💡 get info: Getter property
    // 💡 Getter: Access như property → animal.info (không phải animal.info())
    // 💡 ✅ Clean: Syntax như property nhưng là method

    return `Animal: ${this.name}`;
    // 💡 Return: Computed value từ this.name
  }

  // Setter (Bộ Gán Giá Trị)
  set info(value: string) {
    // 💡 set info: Setter property
    // 💡 Setter: Assign như property → animal.info = 'value'
    // 💡 ✅ Clean: Syntax như property assignment

    this.name = value.replace('Animal: ', '');
    // 💡 Transform: Remove 'Animal: ' prefix → Set this.name
  }
}

// Inheritance với extends (Kế Thừa Với Extends)
class ModernDog extends ModernAnimal {
  // 💡 ModernDog extends ModernAnimal: Inheritance với extends
  // 💡 extends: Kế thừa từ ModernAnimal → ModernDog có tất cả methods/properties của Animal
  // 💡 ✅ Clean: Syntax đơn giản hơn prototype chain

  constructor(name: string, public breed: string) {
    // 💡 constructor: Constructor của ModernDog
    // 💡 public breed: TypeScript parameter property → this.breed = breed tự động

    super(name); // Gọi parent constructor - BẮT BUỘC
    // 💡 super(name): Gọi parent constructor (ModernAnimal.constructor)
    // Phải call super() trước khi dùng this
    // 💡 ✅ Required: Phải gọi super() trước khi access this
    // 💡 super: Reference đến parent class → Gọi parent constructor
  }

  // Override method (Ghi Đè Method)
  speak() {
    // 💡 speak: Override parent speak method
    // 💡 Override: Ghi đè method từ parent → ModernDog có speak riêng
    // 💡 Method resolution: Tìm speak → Tìm thấy ở ModernDog → Dùng ModernDog.speak

    console.log(`${this.name} barks!`);
    // 💡 Dog-specific: "barks" thay vì "makes a sound"
  }

  // Call parent method (Gọi Method Của Parent)
  speakLikeParent() {
    // 💡 speakLikeParent: Method gọi parent method
    super.speak(); // Gọi Animal.speak()
    // 💡 super.speak(): Gọi parent method (ModernAnimal.speak)
    // 💡 super: Reference đến parent class → Access parent methods
    // 💡 ✅ Useful: Gọi parent method từ child class
  }

  // Private fields (ES2022 - Trường Riêng Tư)
  #privateField = 'secret'; // Chỉ accessible trong class
  // 💡 #privateField: Private field (ES2022)
  // 💡 Private: Chỉ accessible trong class → Không thể access từ bên ngoài
  // 💡 #: Syntax cho private fields → Encapsulation
  // 💡 ✅ Encapsulation: Hide internal implementation

  getPrivate() {
    // 💡 getPrivate: Public method để access private field
    return this.#privateField; // ✅ OK
    // 💡 this.#privateField: Access private field từ trong class → OK
    // 💡 ✅ Controlled access: Public method expose private field
  }
}

const modernDog = new ModernDog('Rex', 'Labrador'); // 🐕 Tạo instance
// 💡 new ModernDog(): Gọi constructor → Tạo instance mới
// 💡 'Rex': name → this.name = 'Rex' (từ parent)
// 💡 'Labrador': breed → this.breed = 'Labrador'

modernDog.speak(); // "Rex barks!"
// 💡 modernDog.speak(): Gọi speak method
// 💡 Method resolution: Tìm speak → ModernDog.speak → "Rex barks!"

// console.log(modernDog.#privateField); // ❌ SyntaxError: Private field
// 💡 ❌ Error: Không thể access private field từ bên ngoài
// 💡 ✅ Encapsulation: Private field được bảo vệ → Chỉ access từ trong class

// ============================================
// 4. TEMPLATE LITERALS vs String Concatenation
// ============================================

// 🔴 ES5 - String Concatenation (verbose, error-prone)
var name = 'John';
var age = 25;
var city = 'Ha Noi';

// Single line
var message = 'Hello ' + name + ', you are ' + age + ' years old';

// Multi-line (phải dùng \n và +)
var multiLine = 'Name: ' + name + '\n' + 'Age: ' + age + '\n' + 'City: ' + city;

// HTML generation (nightmare)
var html =
  '<div class="user">' +
  '<h2>' +
  name +
  '</h2>' +
  '<p>Age: ' +
  age +
  '</p>' +
  '<p>City: ' +
  city +
  '</p>' +
  '</div>';

// 🟢 ES6+ - Template Literals (clean, readable - Sạch, Dễ Đọc)
// Cách hoạt động: Backticks `` cho phép embedded expressions ${} và multi-line
const modernMessage = `Hello ${name}, you are ${age} years old`;
// 💡 Template literal: Backticks `` thay vì quotes
// 💡 ${name}: Embedded expression → Interpolate giá trị
// 💡 ${age}: Embedded expression → Interpolate giá trị
// 💡 ✅ Clean: Không cần + concatenation → Dễ đọc hơn

// Multi-line (tự nhiên, giữ nguyên indentation - Nhiều Dòng)
const modernMultiLine = `
  Name: ${name}
  Age: ${age}
  City: ${city}
`;
// 💡 Multi-line: Giữ nguyên line breaks và indentation
// 💡 ✅ Natural: Không cần \n → Tự nhiên như viết text
// 💡 ✅ Preserve: Giữ nguyên formatting → Dễ đọc

// Expression trong template (không chỉ variables - Biểu Thức Trong Template)
const calculation = `2 + 2 = ${2 + 2}`; // "2 + 2 = 4"
// 💡 ${2 + 2}: Expression → Tính toán → 4
// 💡 ✅ Flexible: Có thể dùng bất kỳ expression nào

const conditional = `Status: ${age >= 18 ? 'Adult' : 'Minor'}`; // Ternary
// 💡 ${age >= 18 ? 'Adult' : 'Minor'}: Ternary operator
// 💡 ✅ Conditional: Có thể dùng conditional logic

const methodCall = `Upper: ${name.toUpperCase()}`; // Method call
// 💡 ${name.toUpperCase()}: Method call → Transform string
// 💡 ✅ Methods: Có thể gọi methods trong template

// HTML generation (dễ đọc hơn nhiều)
const modernHtml = `
  <div class="user">
    <h2>${name}</h2>
    <p>Age: ${age}</p>
    <p>City: ${city}</p>
  </div>
`;

// Tagged Templates (advanced feature)
function highlight(strings: TemplateStringsArray, ...values: any[]) {
  return strings.reduce((result, str, i) => {
    return result + str + (values[i] ? `<mark>${values[i]}</mark>` : '');
  }, '');
}

const highlighted = highlight`Hello ${name}, you are ${age} years old`;
// "Hello <mark>John</mark>, you are <mark>25</mark> years old"

// ============================================
// 5. DESTRUCTURING - Elegant Data Extraction
// ============================================

const user = {
  name: 'John Doe',
  age: 30,
  address: {
    city: 'Ha Noi',
    country: 'Vietnam',
  },
  hobbies: ['coding', 'reading'],
};

// 🔴 ES5 - Manual Assignment (verbose, repetitive)
var userName = user.name;
var userAge = user.age;
var userCity = user.address.city;
var userCountry = user.address.country;
var firstHobby = user.hobbies[0];
var secondHobby = user.hobbies[1];

// 🟢 ES6+ - Destructuring (concise, readable - Ngắn Gọn, Dễ Đọc)
// Object destructuring (Phân Rã Object)
const { name: userName2, age: userAge2 } = user; // Rename variables
// 💡 Destructuring: Extract properties từ object
// 💡 name: userName2: Rename name → userName2
// 💡 age: userAge2: Rename age → userAge2
// 💡 ✅ Clean: Không cần user.name, user.age → Trực tiếp userName2, userAge2

// Nested destructuring (Phân Rã Lồng Nhau)
const {
  address: { city, country },
} = user;
// 💡 Nested: Destructure nested object
// 💡 address: { city, country }: Extract city và country từ user.address
// 💡 ✅ Deep: Có thể destructure nhiều levels

// Array destructuring (Phân Rã Array)
const [firstHobby2, secondHobby2] = user.hobbies;
// 💡 Array destructuring: Extract elements từ array
// 💡 [firstHobby2, secondHobby2]: firstHobby2 = hobbies[0], secondHobby2 = hobbies[1]
// 💡 ✅ Positional: Extract theo vị trí

// Default values (Giá Trị Mặc Định)
const { email = 'no-email@example.com' } = user; // email không tồn tại → dùng default
// 💡 email = '...': Default value nếu email không tồn tại
// 💡 ✅ Safe: Tránh undefined → Dùng default value
// 💡 Chỉ dùng default nếu property là undefined

// Rest properties (lấy phần còn lại - Thu Thập Phần Còn Lại)
const { name: n, ...rest } = user; // rest = { age, address, hobbies }
// 💡 ...rest: Rest operator → Thu thập properties còn lại
// 💡 rest: Object chứa tất cả properties trừ name
// 💡 ✅ Flexible: Lấy một số properties, giữ lại phần còn lại

// Function parameter destructuring (Phân Rã Tham Số Function)
function greetUser({ name, age }: { name: string; age: number }) {
  // 💡 { name, age }: Destructure parameters
  // 💡 Function nhận object → Tự động destructure → name và age
  // 💡 ✅ Clean: Không cần user.name, user.age → Trực tiếp name, age

  console.log(`Hello ${name}, ${age} years old`);
}

greetUser(user); // Truyền object, tự động destructure
// 💡 greetUser(user): Truyền object → Tự động destructure
// 💡 ✅ Convenient: Không cần destructure trước khi truyền

// Array destructuring với skip (Phân Rã Array Với Bỏ Qua)
const numbers = [1, 2, 3, 4, 5];
const [first, , third] = numbers; // Skip second element
// 💡 [first, , third]: Bỏ qua phần tử thứ 2
// 💡 first = numbers[0], third = numbers[2]
// 💡 ✅ Skip: Có thể bỏ qua elements không cần

// Swap variables (elegant - Hoán Đổi Biến)
let a = 1,
  b = 2;
[a, b] = [b, a]; // a=2, b=1 (không cần temp variable)
// 💡 [a, b] = [b, a]: Swap values
// 💡 Destructuring assignment: a = b cũ, b = a cũ
// 💡 ✅ Elegant: Không cần temp variable → Ngắn gọn

// ============================================
// 6. SPREAD & REST OPERATORS
// ============================================

// 🔴 ES5 - Array/Object Operations (cumbersome)
var arr1 = [1, 2, 3];
var arr2 = [4, 5, 6];

// Concatenate arrays
var combined = arr1.concat(arr2); // [1,2,3,4,5,6]

// Copy array
var copy = arr1.slice(); // [1,2,3]

// Copy object
var obj1 = { a: 1, b: 2 };
var obj2 = Object.assign({}, obj1); // { a: 1, b: 2 }

// Function với variable arguments
function sum() {
  var args = Array.prototype.slice.call(arguments); // Convert arguments to array
  return args.reduce(function (total, num) {
    return total + num;
  }, 0);
}

// 🟢 ES6+ - Spread & Rest (intuitive, powerful - Trực Quan, Mạnh Mẽ)
// Cách hoạt động: ... operator "spreads" iterable elements
// 💡 Spread: Phân rã iterable thành individual elements
// 💡 Rest: Thu thập elements thành array/object

// Spread arrays (phân rã array thành individual elements - Phân Rã Array)
const spreadArr1 = [1, 2, 3]; // 📦 Array 1
const spreadArr2 = [4, 5, 6]; // 📦 Array 2
const spreadCombined = [...spreadArr1, ...spreadArr2]; // [1,2,3,4,5,6]
// 💡 [...spreadArr1, ...spreadArr2]: Spread arrays → Combine
// 💡 ...spreadArr1: Phân rã [1,2,3] → 1, 2, 3
// 💡 ...spreadArr2: Phân rã [4,5,6] → 4, 5, 6
// 💡 ✅ Combine: Kết hợp arrays dễ dàng

// Copy array (shallow - Sao Chép Array)
const spreadCopy = [...spreadArr1]; // [1,2,3]
// 💡 [...spreadArr1]: Spread → Tạo array mới
// 💡 Shallow copy: Copy array, nhưng nested objects vẫn reference
// 💡 ✅ Immutable: Tạo array mới → Không mutate original

// Add elements (Thêm Phần Tử)
const withExtra = [...spreadArr1, 4, 5]; // [1,2,3,4,5]
// 💡 [...spreadArr1, 4, 5]: Spread + thêm elements
// 💡 ✅ Add: Thêm elements vào cuối array

const atBeginning = [0, ...spreadArr1]; // [0,1,2,3]
// 💡 [0, ...spreadArr1]: Thêm element vào đầu
// 💡 ✅ Prepend: Thêm elements vào đầu array

// Spread objects (phân rã object properties - Phân Rã Object)
const spreadObj1 = { a: 1, b: 2 }; // 📦 Object 1
const spreadObj2 = { c: 3, d: 4 }; // 📦 Object 2
const spreadObjCombined = { ...spreadObj1, ...spreadObj2 }; // {a:1, b:2, c:3, d:4}
// 💡 { ...spreadObj1, ...spreadObj2 }: Spread objects → Merge
// 💡 ...spreadObj1: Phân rã {a:1, b:2} → a: 1, b: 2
// 💡 ...spreadObj2: Phân rã {c:3, d:4} → c: 3, d: 4
// 💡 ✅ Merge: Kết hợp objects → Tạo object mới

// Override properties (Ghi Đè Properties)
const overridden = { ...spreadObj1, b: 99 }; // {a:1, b:99} - b bị ghi đè
// 💡 { ...spreadObj1, b: 99 }: Spread + override
// 💡 b: 99: Ghi đè property b → b = 99 (thay vì 2)
// 💡 ✅ Override: Update properties dễ dàng

// Spread trong function calls (Spread Trong Lời Gọi Function)
const maxNum = Math.max(...spreadArr1); // Math.max(1, 2, 3) = 3
// 💡 Math.max(...spreadArr1): Spread array thành arguments
// 💡 ...spreadArr1: [1,2,3] → Math.max(1, 2, 3)
// 💡 ✅ Arguments: Convert array thành function arguments

// Rest parameters (thu thập remaining arguments vào array - Tham Số Còn Lại)
function modernSum(...numbers: number[]) {
  // 💡 ...numbers: Rest parameter → Thu thập arguments thành array
  // numbers là array [1,2,3,...]
  // 💡 Rest: Thu thập tất cả arguments → numbers = [1,2,3,...]
  // 💡 ✅ Flexible: Function nhận variable arguments

  return numbers.reduce((total, num) => total + num, 0);
  // 💡 reduce: Tính tổng tất cả numbers
}

modernSum(1, 2, 3, 4, 5); // 15
// 💡 modernSum(1,2,3,4,5): Arguments → numbers = [1,2,3,4,5]
// 💡 ✅ Variable args: Có thể truyền bao nhiêu arguments cũng được

// Rest in destructuring (Rest Trong Destructuring)
const [head, ...tail] = [1, 2, 3, 4]; // head=1, tail=[2,3,4]
// 💡 [head, ...tail]: Destructure với rest
// 💡 head: Phần tử đầu tiên → head = 1
// 💡 ...tail: Phần còn lại → tail = [2,3,4]
// 💡 ✅ Split: Tách array thành first + rest

const { x, ...others } = { x: 1, y: 2, z: 3 }; // x=1, others={y:2, z:3}
// 💡 { x, ...others }: Destructure object với rest
// 💡 x: Property x → x = 1
// 💡 ...others: Properties còn lại → others = {y:2, z:3}
// 💡 ✅ Extract: Tách object thành một property + rest

// ============================================
// 7. DEFAULT PARAMETERS
// ============================================

// 🔴 ES5 - Manual Default Values
function greetES5(name, greeting) {
  // Check và assign default
  name = name || 'Guest'; // ⚠️ Falsy values (0, '', false) cũng bị replace
  greeting = typeof greeting !== 'undefined' ? greeting : 'Hello';

  return greeting + ' ' + name;
}

// 🟢 ES6+ - Native Default Parameters (Tham Số Mặc Định)
// Cách hoạt động: Default chỉ apply khi argument là undefined
function greetES6(name = 'Guest', greeting = 'Hello') {
  // 💡 greetES6: Function với default parameters
  // 💡 name = 'Guest': Default value nếu name là undefined
  // 💡 greeting = 'Hello': Default value nếu greeting là undefined
  // 💡 ✅ Clean: Không cần manual check → Tự động dùng default

  return `${greeting} ${name}`;
  // 💡 Template literal: Interpolate values
}

greetES6(); // "Hello Guest"
// 💡 Không truyền arguments → name = 'Guest', greeting = 'Hello'
greetES6('John'); // "Hello John"
// 💡 name = 'John', greeting = 'Hello' (default)
greetES6('John', 'Hi'); // "Hi John"
// 💡 name = 'John', greeting = 'Hi'
greetES6(undefined, 'Hey'); // "Hey Guest" - name dùng default
// 💡 name = undefined → Dùng default 'Guest'
// 💡 greeting = 'Hey'
// 💡 ✅ Undefined only: Chỉ dùng default khi undefined (không phải null, '', 0)

// Default với expressions (Mặc Định Với Biểu Thức)
function createUser(name = 'User', id = generateId()) {
  // 💡 createUser: Function với default expression
  // generateId() chỉ chạy khi id undefined
  // 💡 id = generateId(): Default là function call
  // 💡 generateId(): Chỉ chạy khi id là undefined → Lazy evaluation
  // 💡 ✅ Lazy: Function chỉ chạy khi cần → Performance tốt

  return { name, id };
}

// Default destructured parameters (Mặc Định Với Phân Rã Tham Số)
function configAPI({
  url = 'https://api.example.com',
  timeout = 5000,
  retries = 3,
} = {}) {
  // 💡 configAPI: Function với destructured default parameters
  // = {} để tránh error khi không truyền argument
  // 💡 = {}: Default cho destructured parameter
  // 💡 Nếu không truyền argument → {} → Destructure với defaults
  // 💡 ✅ Safe: Tránh error khi không truyền argument

  console.log({ url, timeout, retries });
  // 💡 Destructure: Extract properties với defaults
}

// ============================================
// 8. PROMISES vs CALLBACKS
// ============================================

// 🔴 ES5 - Callback Hell (pyramid of doom)
function fetchUserES5(userId, callback) {
  setTimeout(function () {
    // Simulate API call
    var user = { id: userId, name: 'John' };

    // Nested callbacks
    fetchPostsES5(userId, function (posts) {
      fetchCommentsES5(posts[0].id, function (comments) {
        fetchLikesES5(comments[0].id, function (likes) {
          // 😱 Callback hell - hard to read, maintain, error handle
          callback({ user, posts, comments, likes });
        });
      });
    });
  }, 100);
}

// Error handling với callbacks (phức tạp)
function fetchDataES5(callback) {
  setTimeout(function () {
    var error = Math.random() > 0.5 ? new Error('Failed') : null;
    var data = error ? null : { value: 42 };
    callback(error, data); // Node.js style: error-first callback
  }, 100);
}

// 🟢 ES6+ - Promises (chainable, readable - Có Thể Nối Chuỗi, Dễ Đọc)
// Cách hoạt động: Promise là object đại diện cho eventual completion/failure
function fetchUserES6(userId: string): Promise<any> {
  // 💡 fetchUserES6: Function return Promise
  // 💡 Promise: Object đại diện cho async operation

  return new Promise((resolve, reject) => {
    // 💡 new Promise: Tạo Promise mới
    // executor function chạy immediately
    // 💡 (resolve, reject): Executor function chạy ngay lập tức
    // 💡 resolve: Function để resolve Promise (success)
    // 💡 reject: Function để reject Promise (failure)

    setTimeout(() => {
      // 💡 setTimeout: Simulate async operation
      const user = { id: userId, name: 'John' }; // 📦 Data
      resolve(user); // Success
      // 💡 resolve(user): Resolve Promise với user data
      // 💡 Promise state: pending → fulfilled
      // 💡 .then() callbacks sẽ được gọi với user

      // reject(new Error('Failed')); // Failure
      // 💡 reject(): Reject Promise với error
      // 💡 Promise state: pending → rejected
      // 💡 .catch() callback sẽ được gọi với error
    }, 100);
  });
}

// Promise chaining (flat, readable - Nối Chuỗi Promise)
fetchUserES6('123')
  // 💡 fetchUserES6('123'): Return Promise
  // 💡 Promise chaining: Nối nhiều async operations

  .then((user) => {
    // 💡 .then(): Callback khi Promise resolve
    // 💡 user: Data từ resolve(user)
    console.log('User:', user);
    return fetchPosts(user.id); // Return promise → chain tiếp
    // 💡 return fetchPosts(): Return Promise → Chain tiếp
    // 💡 ✅ Chain: Promise chain → Flat, readable
  })
  .then((posts) => {
    // 💡 .then(): Callback với data từ Promise trước
    // 💡 posts: Data từ fetchPosts Promise
    console.log('Posts:', posts);
    return fetchComments(posts[0].id); // 🔗 Chain tiếp
  })
  .then((comments) => {
    // 💡 .then(): Callback với comments
    console.log('Comments:', comments);
    return fetchLikes(comments[0].id); // 🔗 Chain tiếp
  })
  .then((likes) => {
    // 💡 .then(): Callback cuối cùng
    console.log('Likes:', likes);
  })
  .catch((error) => {
    // Single catch cho tất cả errors
    // 💡 .catch(): Callback khi bất kỳ Promise nào reject
    // 💡 error: Error từ reject() hoặc throw
    // 💡 ✅ Single catch: Một catch handle tất cả errors
    console.error('Error:', error);
  })
  .finally(() => {
    // Chạy dù thành công hay fail
    // 💡 .finally(): Callback luôn chạy (success hoặc fail)
    // 💡 ✅ Cleanup: Perfect cho cleanup code
    console.log('Cleanup');
  });

// Promise combinators (Các Bộ Kết Hợp Promise)
const promise1 = fetchUserES6('1'); // 📦 Promise 1
const promise2 = fetchUserES6('2'); // 📦 Promise 2
const promise3 = fetchUserES6('3'); // 📦 Promise 3
// 💡 Tạo 3 Promises → Dùng combinators để xử lý

// Promise.all - chờ tất cả resolve (hoặc 1 reject - Chờ Tất Cả)
Promise.all([promise1, promise2, promise3]).then((results) => {
  // 💡 Promise.all: Chờ TẤT CẢ Promises resolve
  // 💡 Nếu 1 Promise reject → Promise.all reject ngay
  // 💡 results: Array kết quả theo thứ tự [result1, result2, result3]
  // 💡 ✅ All or nothing: Tất cả thành công hoặc fail ngay

  console.log('All users:', results); // [user1, user2, user3]
});

// Promise.race - lấy kết quả của promise nhanh nhất (Đua)
Promise.race([promise1, promise2, promise3]).then((result) => {
  // 💡 Promise.race: Lấy Promise resolve/reject NHANH NHẤT
  // 💡 result: Kết quả của Promise nhanh nhất
  // 💡 ✅ Fastest: Dùng cho timeout, fastest response
  console.log('First user:', result); // user nào resolve trước
});

// Promise.allSettled - chờ tất cả settle (resolve hoặc reject - Chờ Tất Cả Hoàn Thành)
Promise.allSettled([promise1, promise2, promise3]).then((results) => {
  // 💡 Promise.allSettled: Chờ TẤT CẢ Promises settle (resolve hoặc reject)
  // 💡 Không reject ngay → Chờ tất cả hoàn thành
  // 💡 results: Array với status (fulfilled/rejected) và value/reason
  // 💡 ✅ All settled: Luôn resolve → Có thể có một số fail

  results.forEach((result) => {
    if (result.status === 'fulfilled') {
      // 💡 fulfilled: Promise resolve → Có value
      console.log('Success:', result.value);
    } else {
      // 💡 rejected: Promise reject → Có reason
      console.log('Failed:', result.reason);
    }
  });
});

// Promise.any - lấy promise fulfilled đầu tiên (Bất Kỳ Thành Công)
Promise.any([promise1, promise2, promise3]).then((result) => {
  // 💡 Promise.any: Lấy Promise FULFILLED đầu tiên
  // 💡 Bỏ qua rejected → Chỉ lấy fulfilled
  // 💡 result: Kết quả của Promise fulfilled đầu tiên
  // 💡 ✅ First success: Dùng cho fallback, fastest success
  console.log('First successful:', result);
});

// ============================================
// 9. ASYNC/AWAIT - Promise Syntax Sugar
// ============================================

// 🟢 ES2017 - Async/Await (looks synchronous, actually async - Trông Như Đồng Bộ, Thực Tế Bất Đồng Bộ)
// Cách hoạt động: async function tự động return Promise, await pause execution
async function fetchAllData() {
  // 💡 async function: Function tự động return Promise
  // 💡 async: Keyword để khai báo async function
  // 💡 Return: Tự động wrap return value trong Promise

  try {
    // 💡 try-catch: Error handling như synchronous code
    // await "pauses" execution until promise resolves
    const user = await fetchUserES6('123'); // Looks synchronous!
    // 💡 await: Pause execution → Đợi Promise resolve
    // 💡 fetchUserES6('123'): Return Promise
    // 💡 await: Đợi Promise resolve → user = resolved value
    // 💡 ✅ Synchronous look: Code trông như synchronous → Dễ đọc

    console.log('User:', user);

    const posts = await fetchPosts(user.id); // Wait for user first
    // 💡 await fetchPosts: Đợi user xong mới fetch posts
    // 💡 Sequential: Mỗi await đợi Promise trước → Sequential execution
    console.log('Posts:', posts);

    const comments = await fetchComments(posts[0].id);
    // 💡 await fetchComments: Đợi posts xong mới fetch comments
    console.log('Comments:', comments);

    const likes = await fetchLikes(comments[0].id);
    // 💡 await fetchLikes: Đợi comments xong mới fetch likes
    console.log('Likes:', likes);

    return { user, posts, comments, likes }; // 📤 Return object
    // 💡 return: Tự động wrap trong Promise.resolve()
  } catch (error) {
    // Try-catch cho error handling (như synchronous code)
    // 💡 catch: Handle errors từ bất kỳ await nào
    // 💡 ✅ Synchronous error handling: Try-catch như synchronous code
    console.error('Error:', error);
    throw error; // Re-throw nếu cần
    // 💡 throw: Re-throw error → Caller có thể catch
  } finally {
    // 💡 finally: Luôn chạy (success hoặc fail)
    console.log('Cleanup');
    // 💡 ✅ Cleanup: Perfect cho cleanup code
  }
}

// Parallel execution với Promise.all (Thực Thi Song Song)
async function fetchMultipleUsers() {
  // ❌ Sequential (slow) - mỗi request đợi previous
  const user1 = await fetchUserES6('1'); // Wait 100ms
  // 💡 await: Đợi Promise resolve → Mất 100ms
  const user2 = await fetchUserES6('2'); // Wait thêm 100ms
  // 💡 await: Đợi user1 xong mới fetch user2 → Mất thêm 100ms
  const user3 = await fetchUserES6('3'); // Wait thêm 100ms
  // 💡 await: Đợi user2 xong mới fetch user3 → Mất thêm 100ms
  // Total: 300ms
  // 💡 ⚠️ Slow: Sequential → Tổng thời gian = tổng các requests

  // ✅ Parallel (fast) - tất cả requests cùng lúc
  const [user1, user2, user3] = await Promise.all([
    // 💡 Promise.all: Fetch song song → Tất cả requests cùng lúc
    fetchUserES6('1'), // ⚡ Start ngay
    fetchUserES6('2'), // ⚡ Start ngay (song song với 1)
    fetchUserES6('3'), // ⚡ Start ngay (song song với 1, 2)
  ]);
  // Total: 100ms (chỉ chờ slowest request)
  // 💡 ✅ Fast: Parallel → Tổng thời gian = max của các requests
  // 💡 Destructuring: [user1, user2, user3] = results array
}

// Top-level await (ES2022) - await ngoài async function
// const config = await fetch('/api/config').then(r => r.json());
// console.log(config); // ✅ OK trong module scope

// ============================================
// 10. MODULES - Import/Export
// ============================================

// 🔴 ES5 - No Native Modules
// Phải dùng patterns như IIFE, CommonJS (Node.js), AMD (RequireJS)

// IIFE Pattern (Immediately Invoked Function Expression)
var MyModule = (function () {
  var privateVar = 'secret';

  function privateMethod() {
    console.log(privateVar);
  }

  return {
    publicMethod: function () {
      privateMethod();
    },
  };
})();

// CommonJS (Node.js)
// module.exports = { name: 'John', greet: function() {} };
// const user = require('./user');

// 🟢 ES6+ - Native Modules (static analysis, tree-shaking - Phân Tích Tĩnh, Loại Bỏ Code Không Dùng)
// Cách hoạt động: Import/export statements, module scope riêng biệt
// 💡 Modules: File scope riêng biệt → Không pollute global
// 💡 Static analysis: Build tools có thể analyze → Tree-shaking
// 💡 Tree-shaking: Loại bỏ code không dùng → Bundle size nhỏ hơn

// Named exports (có thể nhiều per file - Export Có Tên)
export const PI = 3.14159;
// 💡 export const: Named export → Có thể export nhiều
// 💡 Named: Export với tên → Import với cùng tên
export function calculateArea(radius: number) {
  // 💡 export function: Named export function
  return PI * radius * radius;
}
export class Circle {
  // 💡 export class: Named export class
  constructor(public radius: number) {}
}
// 💡 ✅ Multiple exports: Có thể export nhiều từ 1 file

// Default export (chỉ 1 per file - Export Mặc Định)
export default class User {
  // 💡 export default: Default export → Chỉ 1 per file
  // 💡 Default: Export chính của module → Import không cần {}
  constructor(public name: string) {}
}
// 💡 ✅ Single export: Export chính của module

// Import named exports (Import Export Có Tên)
import { PI, calculateArea, Circle } from './math';
// 💡 import { ... }: Import named exports
// 💡 { PI, calculateArea, Circle }: Destructure imports
// 💡 './math': Path đến module file
// 💡 ✅ Named imports: Import với tên cụ thể

// Import default export (Import Export Mặc Định)
import User from './user';
// 💡 import User: Import default export
// 💡 Không cần {} → Default export
// 💡 ✅ Default import: Import export chính

// Import both (Import Cả Hai)
import User, { PI, calculateArea } from './combined';
// 💡 import User, { ... }: Import default + named exports
// 💡 User: Default export
// 💡 { PI, calculateArea }: Named exports
// 💡 ✅ Mixed: Có thể import cả default và named

// Rename imports (Đổi Tên Import)
import { PI as PIValue } from './math';
// 💡 PI as PIValue: Rename import → Tránh conflict
// 💡 PIValue: Tên mới để dùng trong file này
// 💡 ✅ Rename: Tránh naming conflicts

// Import all (Import Tất Cả)
import * as MathUtils from './math';
// 💡 import * as: Import tất cả exports vào namespace
// 💡 MathUtils: Namespace object chứa tất cả exports
MathUtils.PI; // 3.14159
// 💡 MathUtils.PI: Access qua namespace
MathUtils.calculateArea(5);
// 💡 ✅ Namespace: Group imports → Tránh pollute scope

// Re-export (module aggregation - Tái Export)
export { PI, calculateArea } from './math';
// 💡 export { ... } from: Re-export từ module khác
// 💡 ✅ Aggregation: Tập hợp exports từ nhiều modules
export { default as User } from './user';
// 💡 export { default as User }: Re-export default với tên mới

// Dynamic imports (code splitting - Import Động)
const module = await import('./heavy-module'); // Lazy load
// 💡 await import(): Dynamic import → Load module khi cần
// 💡 Lazy load: Chỉ load khi code chạy đến → Code splitting
module.doSomething();
// 💡 ✅ Code splitting: Giảm initial bundle size

// Conditional imports (Import Có Điều Kiện)
if (condition) {
  // 💡 Conditional: Chỉ import khi condition = true
  const { feature } = await import('./feature');
  // 💡 await import(): Dynamic import trong condition
  feature();
  // 💡 ✅ Conditional loading: Load module khi cần
}
```

**🎯 Best Practices (Thực Hành Tốt):**

1. **✅ Always use const/let** thay vì var - block scoping an toàn hơn
2. **✅ Prefer arrow functions** cho callbacks và short functions
3. **✅ Use template literals** cho string manipulation
4. **✅ Destructure objects/arrays** để code ngắn gọn
5. **✅ Use spread operator** cho cloning và merging
6. **✅ Prefer async/await** over promise chains - dễ đọc hơn
7. **✅ Use ES6 modules** thay vì CommonJS trong modern projects
8. **✅ Use default parameters** thay vì manual checks
9. **✅ Use class syntax** cho OOP - cleaner than prototypes
10. **✅ Enable Babel** hoặc TypeScript cho transpilation và type safety

**❌ Common Mistakes (Lỗi Thường Gặp):**

```typescript
// ❌ LỖI 1: Dùng var trong modern code (Dùng Var Trong Code Hiện Đại)
var name = 'John'; // ❌ Function scoped, có thể gây bugs
// 💡 var: Function scoped → Có thể gây bugs với hoisting
// 💡 ⚠️ Problem: Hoisting, redeclaration → Khó debug

// ✅ ĐÚNG: Dùng const/let
const name = 'John'; // ✅ Block scoped, immutable
// 💡 const: Block scoped, immutable → An toàn hơn
let age = 25; // ✅ Block scoped, mutable
// 💡 let: Block scoped, mutable → An toàn hơn var

// ❌ LỖI 2: Arrow function làm method (lose this binding - Mất Binding This)
const obj = {
  value: 42,
  getValue: () => this.value, // ❌ this = window, không phải obj
  // 💡 Arrow function: Không có own this → this = window
  // 💡 ⚠️ Problem: this không point đến obj → undefined.value
};

// ✅ ĐÚNG: Regular function cho methods
const obj = {
  value: 42,
  getValue() {
    // 💡 Method shorthand: Regular function → this = obj
    return this.value; // ✅ this = obj
    // 💡 ✅ Correct: this point đến obj → Access value
  },
};

// ❌ LỖI 3: Quên await trong async function (Quên Await)
async function fetchData() {
  const data = fetchUserES6('123'); // ❌ data là Promise, không phải value
  // 💡 fetchUserES6(): Return Promise → data = Promise object
  // 💡 ⚠️ Problem: Không await → data là Promise, không phải resolved value
  console.log(data.name); // undefined
  // 💡 data.name: Promise không có name → undefined
}

// ✅ ĐÚNG: Await promise
async function fetchData() {
  const data = await fetchUserES6('123'); // ✅ Chờ promise resolve
  // 💡 await: Đợi Promise resolve → data = resolved value
  // 💡 ✅ Correct: data là object với name property
  console.log(data.name); // "John"
  // 💡 data.name: Access property từ resolved value
}

// ❌ LỖI 4: Sequential await khi có thể parallel (Tuần Tự Khi Có Thể Song Song)
async function slow() {
  const user1 = await fetchUser('1'); // 100ms
  // 💡 await: Đợi Promise resolve → Mất 100ms
  const user2 = await fetchUser('2'); // 100ms
  // 💡 await: Đợi user1 xong → Mất thêm 100ms
  const user3 = await fetchUser('3'); // 100ms
  // 💡 await: Đợi user2 xong → Mất thêm 100ms
  // Total: 300ms
  // 💡 ⚠️ Slow: Sequential → Tổng thời gian = tổng các requests
}

// ✅ ĐÚNG: Parallel với Promise.all
async function fast() {
  const [user1, user2, user3] = await Promise.all([
    // 💡 Promise.all: Fetch song song → Tất cả cùng lúc
    fetchUser('1'), // ⚡ Start ngay
    fetchUser('2'), // ⚡ Start ngay (song song)
    fetchUser('3'), // ⚡ Start ngay (song song)
  ]);
  // Total: 100ms
  // 💡 ✅ Fast: Parallel → Tổng thời gian = max của các requests
}

// ❌ LỖI 5: Spread shallow copy cho nested objects (Sao Chép Nông Cho Object Lồng Nhau)
const original = { a: 1, nested: { b: 2 } }; // 📦 Object với nested
const copied = { ...original }; // 📋 Shallow copy
copied.nested.b = 99; // ❌ original.nested.b cũng = 99!
// 💡 Spread: Chỉ copy level 1 → nested vẫn reference
// 💡 ⚠️ Problem: Mutate copied.nested → original.nested cũng thay đổi
// 💡 Shallow copy: Chỉ copy properties level 1

// ✅ ĐÚNG: Deep copy cho nested structures
const copied = JSON.parse(JSON.stringify(original)); // Simple way
// 💡 JSON.parse(JSON.stringify()): Deep copy (simple way)
// 💡 ✅ Deep copy: Copy tất cả levels → nested không reference
// Hoặc dùng lodash cloneDeep, structuredClone
// 💡 structuredClone(): Native deep copy (ES2022)

// ❌ LỖI 6: Destructuring với missing properties (no default - Thiếu Giá Trị Mặc Định)
const { email } = user; // ❌ email = undefined nếu không tồn tại
// 💡 Destructure: email không tồn tại → email = undefined
// 💡 ⚠️ Problem: undefined có thể gây bugs

// ✅ ĐÚNG: Provide default values
const { email = 'no-email@example.com' } = user; // ✅
// 💡 email = '...': Default value nếu email undefined
// 💡 ✅ Safe: Luôn có giá trị → Tránh undefined bugs

// ❌ LỖI 7: Confuse default export vs named export (Nhầm Export Mặc Định vs Có Tên)
import User from './user'; // ❌ Nếu file export named, không phải default
// 💡 import User: Import default export
// 💡 ⚠️ Problem: Nếu file export named → User = undefined

// ✅ ĐÚNG: Match export type
import { User } from './user'; // ✅ Named export
// 💡 import { User }: Import named export
// 💡 ✅ Correct: Match với export type
import User from './user'; // ✅ Default export
// 💡 import User: Import default export
// 💡 ✅ Correct: Match với export type
```

**📊 Performance Comparison:**

```
┌─────────────────────────────────────────────────────────────┐
│              ES5 vs ES6+ PERFORMANCE IMPACT                  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Feature                    ES5 Speed    ES6+ Speed  Winner │
│  ────────────────────────── ──────────── ────────── ────── │
│  Variable access (var)      ⚡⚡⚡⚡⚡      -          ES5   │
│  Variable access (let)      -            ⚡⚡⚡⚡      ES6   │
│  Function call (regular)    ⚡⚡⚡⚡⚡      -          ES5   │
│  Function call (arrow)      -            ⚡⚡⚡⚡⚡     ES6   │
│  String concat (+)          ⚡⚡⚡⚡       -          ES5   │
│  Template literals (``)     -            ⚡⚡⚡⚡⚡     ES6   │
│  Object creation            ⚡⚡⚡⚡       -          ES5   │
│  Class instantiation        -            ⚡⚡⚡⚡      ES6   │
│  Array iteration (.map)     ⚡⚡⚡⚡       -          ES5   │
│  For-of loop                -            ⚡⚡⚡⚡⚡     ES6   │
│  Promise                    N/A          ⚡⚡⚡        ES6   │
│  Async/Await                N/A          ⚡⚡⚡        ES6   │
│                                                              │
│  💡 Note: Performance khác biệt minimal trong most cases    │
│     Code readability & maintainability quan trọng hơn!      │
└─────────────────────────────────────────────────────────────┘
```

**✅ Khi Nào Dùng ES5 vs ES6+:**

**🔴 Dùng ES5 khi:**

- Target IE11 và không thể dùng Babel
- Working với legacy codebase không thể refactor
- Extreme performance critical code (rare cases)

**🟢 Dùng ES6+ khi:**

- Modern project (>99% cases)
- Target modern browsers (Chrome, Firefox, Safari, Edge)
- Want maintainable, readable code
- Using build tools (Webpack, Vite, Babel)
- TypeScript project
