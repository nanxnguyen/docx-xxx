# ➡️ Q09: Arrow vs Regular Functions & this Binding (call, apply, bind)

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"Arrow function khác regular function ở cách gắn `this`: từ vựng (scope bên ngoài) vs động (ngữ cảnh runtime).**

**📊 Arrow vs Regular Functions (Key Differences):**
1. **`this` Binding**:
   - **Arrow**: Lexical `this` → inherit từ outer scope (không có `this` riêng).
   - **Regular**: Dynamic `this` → phụ thuộc cái gì gọi function (runtime).

2. **`arguments` Object**:
   - **Arrow**: Không có `arguments` → dùng rest params `(...args)`.
   - **Regular**: Có `arguments` (array-like object).

3. **Constructor**:
   - **Arrow**: Không dùng được `new` → throw error.
   - **Regular**: Có thể dùng `new` → tạo instance.

4. **Hoisting**:
   - **Arrow**: Không hoisted (nếu dùng `const/let`).
   - **Regular**: Hoisted (function declaration).

**🔧 `this` Binding Methods (call, apply, bind):**
- **`call(thisArg, arg1, arg2)`**: Invoke ngay với arguments riêng lẻ.
  ```js
  fn.call({ name: 'John' }, 1, 2); // this = { name: 'John' }, args: 1, 2
  ```
- **`apply(thisArg, [args])`**: Invoke ngay với arguments array.
  ```js
  fn.apply({ name: 'John' }, [1, 2]); // this = { name: 'John' }, args: [1, 2]
  ```
- **`bind(thisArg)`**: Return function mới với `this` cố định (không invoke).
  ```js
  const boundFn = fn.bind({ name: 'John' }); // Return new function
  boundFn(1, 2); // this = { name: 'John' }
  ```

**🎯 `this` Binding Rules (4 Rules - Priority Order):**
1. **`new` Binding**: `new Fn()` → `this` = new object.
2. **Explicit Binding**: `call/apply/bind` → `this` = thisArg.
3. **Implicit Binding**: `obj.method()` → `this` = obj.
4. **Default Binding**: Standalone function → `this` = global object (window/global) hoặc undefined (strict mode).

**⚠️ Common Mistakes:**
- **Arrow trong object methods**: `this` không point to object!
  ```js
  const obj = {
    name: 'John',
    greet: () => console.log(this.name) // ❌ undefined! (this = outer scope)
  };
  // ✅ Dùng regular function hoặc method shorthand
  ```
- **Event handlers**: Regular function → `this` = event target. Arrow → `this` = outer scope.
- **Class methods as callbacks**: Mất context → dùng arrow hoặc bind.
  ```js
  class Component {
    handleClick() { console.log(this); }
    render() {
      // ❌ this = undefined (mất context)
      button.addEventListener('click', this.handleClick);
      // ✅ Fix: Arrow hoặc bind
      button.addEventListener('click', () => this.handleClick());
      button.addEventListener('click', this.handleClick.bind(this));
    }
  }
  ```

**💡 Senior Insights:**
- **React Class Components**: Arrow class fields = auto-bind `this` (babel transform).
- **Performance**: Arrow functions trong render → tạo new reference mỗi lần → child re-render. Dùng `useCallback`.
- **call vs apply**: `apply` hữu ích khi arguments đã là array (e.g., `Math.max.apply(null, [1,2,3])`).
- **Polyfill bind**: Implement bind manually để hiểu cơ chế:
  ```js
  Function.prototype.myBind = function(context, ...args) {
    const fn = this;
    return function(...newArgs) {
      return fn.apply(context, [...args, ...newArgs]);
    };
  };
  ```

---

**⚡ Quick Summary:**
> Arrow function = lexical `this` (từ outer scope), không có arguments, không dùng new. `this` trong JS = context object, dùng call/apply/bind để set `this` manually.

**💡 Ghi Nhớ:**
- 🎯 **Arrow**: `() => {}` - this từ outer scope, không có arguments/constructor
- 📌 **Regular**: `function(){}` - this runtime, có arguments, hoisted
- 📞 **call**: `fn.call(thisArg, arg1, arg2)` - invoke ngay với args riêng lẻ
- 📋 **apply**: `fn.apply(thisArg, [args])` - invoke ngay với array
- 🔗 **bind**: `fn.bind(thisArg)` - return function mới với this cố định


### **1. Arrow vs Regular Functions - Sự Khác Biệt Quan Trọng**

#### **1.1. Syntax & Declaration**

```typescript
// ═══════════════════════════════════════════════════════════
// SYNTAX - Cú pháp
// ═══════════════════════════════════════════════════════════

// Regular Function
function regularFunction(name: string): string {
  return `Hello ${name}`;
}

// Arrow Function - ngắn gọn hơn
const arrowFunction = (name: string): string => `Hello ${name}`;

// Arrow với 1 parameter - bỏ được ()
const single = name => `Hello ${name}`;

// Arrow return object - phải bọc trong ()
const getUser = (id: number) => ({ id, name: 'John' });
// Không có () sẽ bị nhầm với block { }

// Arrow multiline - cần return
const calculate = (a: number, b: number) => {
  const sum = a + b;
  const product = a * b;
  return { sum, product };
};
```

#### **1.2. this Binding - Khác Biệt QUAN TRỌNG Nhất**

```typescript
// ═══════════════════════════════════════════════════════════
// THIS BINDING - Điểm khác biệt QUAN TRỌNG nhất
// ═══════════════════════════════════════════════════════════

class Person {
  name: string = 'John';

  // ❌ Regular function - this là ĐỘNG (dynamic binding)
  // this phụ thuộc vào CÁI GÌ gọi function (runtime)
  regularMethod(): void {
    setTimeout(function () {
      console.log(this.name); 
      // ❌ undefined!
      // Vì function được gọi bởi setTimeout → this = window/global
    }, 100);
  }

  // ✅ Arrow function - this là TĨNH (lexical binding)
  // this được "kế thừa" từ outer scope (Person instance)
  arrowMethod(): void {
    setTimeout(() => {
      console.log(this.name); 
      // ✅ "John"!
      // Arrow function KHÔNG có this riêng → lấy this từ Person
    }, 100);
  }

  // 🔧 Cách fix cho regular function
  regularMethodFixed(): void {
    const self = this; // Lưu this vào biến
    setTimeout(function () {
      console.log(self.name); // ✅ "John" - dùng biến self
    }, 100);
  }

  regularMethodBind(): void {
    setTimeout(function () {
      console.log(this.name); // ✅ "John" - bind this
    }.bind(this), 100);
  }
}

// ═══════════════════════════════════════════════════════════
// THIS trong Object Methods
// ═══════════════════════════════════════════════════════════

const user = {
  name: 'Alice',
  
  // ❌ SAI: Arrow function trong object method
  greetArrow: () => {
    console.log(this.name); 
    // ❌ undefined!
    // Arrow function lấy this từ OUTER SCOPE (window/global)
    // Không phải object `user`!
  },
  
  // ✅ ĐÚNG: Regular function
  greetRegular() {
    console.log(this.name); 
    // ✅ "Alice"
    // Regular function: this = object gọi method (user)
  },
  
  // ✅ Use case ĐÚNG cho arrow function
  registerEvents() {
    document.addEventListener('click', () => {
      console.log(this.name); 
      // ✅ "Alice"
      // Arrow lấy this từ registerEvents → this = user
    });
    
    // ❌ Regular function sẽ sai
    document.addEventListener('click', function() {
      console.log(this.name); 
      // ❌ undefined
      // this = document (object gọi callback)
    });
  }
};
```

**💡 Quy tắc this:**
```typescript
// Regular function: this phụ thuộc vào CÁI GÌ gọi function
obj.method()      // this = obj
fn()              // this = window/global
new Fn()          // this = instance mới
fn.call(obj)      // this = obj

// Arrow function: this = this của OUTER SCOPE (nơi function được định nghĩa)
// Không quan tâm CÁI GÌ gọi function!
```

#### **1.3. arguments Object**

```typescript
// ═══════════════════════════════════════════════════════════
// ARGUMENTS OBJECT
// ═══════════════════════════════════════════════════════════

// Regular function - CÓ arguments object
function regularWithArgs(a: number, b: number): void {
  console.log(arguments); 
  // ✅ Arguments { '0': 10, '1': 20, '2': 30 }
  console.log(arguments.length); // 3
  console.log(arguments[2]); // 30 - extra argument
}

regularWithArgs(10, 20, 30);

// Arrow function - KHÔNG có arguments
const arrowWithArgs = (a: number, b: number): void => {
  // console.log(arguments);  
  // ❌ ReferenceError: arguments is not defined
};

// ✅ Giải pháp: Dùng rest parameters
const arrowWithRest = (...args: number[]): void => {
  console.log(args); // ✅ [10, 20, 30]
  console.log(args.length); // 3
};

arrowWithRest(10, 20, 30);
```

#### **1.4. Constructor & new**

```typescript
// ═══════════════════════════════════════════════════════════
// CONSTRUCTOR - Chỉ regular function có thể làm constructor
// ═══════════════════════════════════════════════════════════

// ✅ Regular function - có thể dùng new
function RegularConstructor(name: string) {
  this.name = name;
}

const instance1 = new RegularConstructor('John');
console.log(instance1.name); // "John" ✅

// ❌ Arrow function - KHÔNG thể dùng new
const ArrowConstructor = (name: string) => {
  this.name = name;
};

// const instance2 = new ArrowConstructor('John');
// ❌ TypeError: ArrowConstructor is not a constructor
```

#### **1.5. Hoisting**

```typescript
// ═══════════════════════════════════════════════════════════
// HOISTING
// ═══════════════════════════════════════════════════════════

// ✅ Regular function - HOISTED (có thể gọi trước khi khai báo)
console.log(regularHoisted()); // ✅ "Hello" - works!

function regularHoisted(): string {
  return 'Hello';
}

// ❌ Arrow function - KHÔNG hoisted
// console.log(arrowHoisted()); 
// ❌ ReferenceError: Cannot access 'arrowHoisted' before initialization

const arrowHoisted = (): string => 'Hello';
```

#### **1.6. Methods & Prototype**

```typescript
// ═══════════════════════════════════════════════════════════
// PROTOTYPE - Regular có prototype, Arrow không
// ═══════════════════════════════════════════════════════════

function RegularFn() {}
console.log(RegularFn.prototype); // ✅ { constructor: f }

const ArrowFn = () => {};
console.log(ArrowFn.prototype); // ❌ undefined

// Use case: Thêm methods vào prototype
function Person(name: string) {
  this.name = name;
}

Person.prototype.greet = function() {
  return `Hello, I'm ${this.name}`;
  // ✅ Phải dùng regular function để có this
};

const person = new Person('John');
console.log(person.greet()); // "Hello, I'm John"
```

---

### **2. this Binding - call, apply, bind**

#### **2.1. Understanding `this` Context**

```typescript
// ═══════════════════════════════════════════════════════════
// THIS CONTEXT - 4 quy tắc
// ═══════════════════════════════════════════════════════════

// 1️⃣ Default binding (strict mode: undefined, non-strict: window)
function showThis() {
  console.log(this);
}
showThis(); // window (non-strict) hoặc undefined (strict)

// 2️⃣ Implicit binding (object gọi method)
const obj = {
  name: 'John',
  greet() {
    console.log(this.name); // "John" - this = obj
  }
};
obj.greet();

// 3️⃣ Explicit binding (call, apply, bind)
function greet() {
  console.log(this.name);
}
const user = { name: 'Alice' };
greet.call(user); // "Alice" - this = user

// 4️⃣ new binding (constructor)
function Person(name: string) {
  this.name = name;
}
const p = new Person('Bob'); // this = instance mới
```

#### **2.2. call() - Gọi ngay với arguments riêng lẻ**

```typescript
// ═══════════════════════════════════════════════════════════
// CALL - fn.call(thisArg, arg1, arg2, arg3, ...)
// ═══════════════════════════════════════════════════════════

function introduce(age: number, city: string): string {
  return `I'm ${this.name}, ${age} years old, from ${city}`;
}

const person1 = { name: 'John' };
const person2 = { name: 'Alice' };

// Gọi introduce với this = person1
console.log(introduce.call(person1, 25, 'HCM')); 
// "I'm John, 25 years old, from HCM"

// Gọi introduce với this = person2
console.log(introduce.call(person2, 30, 'HN')); 
// "I'm Alice, 30 years old, from HN"

// ═══════════════════════════════════════════════════════════
// Use case: Function borrowing
// ═══════════════════════════════════════════════════════════

const car = {
  brand: 'Toyota',
  model: 'Camry',
  getInfo() {
    return `${this.brand} ${this.model}`;
  }
};

const bike = { brand: 'Honda', model: 'CBR' };

// "Mượn" method getInfo của car cho bike
console.log(car.getInfo.call(bike)); 
// "Honda CBR" ✅ - this = bike

// ═══════════════════════════════════════════════════════════
// Use case: Array-like to Array
// ═══════════════════════════════════════════════════════════

function argsToArray() {
  // arguments là array-like, không phải array
  // Mượn method slice của Array
  const arr = Array.prototype.slice.call(arguments);
  console.log(arr); // [1, 2, 3] - thành array thật ✅
}

argsToArray(1, 2, 3);
```

#### **2.3. apply() - Gọi ngay với array of arguments**

```typescript
// ═══════════════════════════════════════════════════════════
// APPLY - fn.apply(thisArg, [arg1, arg2, arg3, ...])
// ═══════════════════════════════════════════════════════════

function introduce(age: number, city: string): string {
  return `I'm ${this.name}, ${age} years old, from ${city}`;
}

const person = { name: 'John' };

// apply - arguments là ARRAY
const args = [25, 'HCM'];
console.log(introduce.apply(person, args)); 
// "I'm John, 25 years old, from HCM"

// So sánh với call
console.log(introduce.call(person, 25, 'HCM')); // Giống kết quả

// ═══════════════════════════════════════════════════════════
// Use case: Math.max với array
// ═══════════════════════════════════════════════════════════

const numbers = [5, 6, 2, 3, 7, 1];

// ❌ Math.max nhận arguments riêng lẻ, không nhận array
// console.log(Math.max(numbers)); // NaN

// ✅ Dùng apply để "spread" array thành arguments
console.log(Math.max.apply(null, numbers)); // 7

// Modern: Dùng spread operator (ES6+)
console.log(Math.max(...numbers)); // 7 - dễ đọc hơn ✅

// ═══════════════════════════════════════════════════════════
// call vs apply - Khi nào dùng cái nào?
// ═══════════════════════════════════════════════════════════

// call: Khi biết CHÍNH XÁC số lượng arguments
fn.call(obj, arg1, arg2, arg3);

// apply: Khi arguments là ARRAY hoặc ĐỘNG
fn.apply(obj, argsArray);
fn.apply(obj, [...dynamicArgs]);
```

#### **2.4. bind() - Tạo function mới với this cố định**

```typescript
// ═══════════════════════════════════════════════════════════
// BIND - fn.bind(thisArg, arg1, arg2, ...)
// Trả về FUNCTION MỚI, KHÔNG gọi ngay!
// ═══════════════════════════════════════════════════════════

function introduce(age: number, city: string): string {
  return `I'm ${this.name}, ${age} years old, from ${city}`;
}

const person = { name: 'John' };

// bind tạo function MỚI với this = person
const boundIntroduce = introduce.bind(person);

// Gọi function mới
console.log(boundIntroduce(25, 'HCM')); 
// "I'm John, 25 years old, from HCM"

// this luôn luôn là person, không thay đổi được!
const anotherPerson = { name: 'Alice' };
console.log(boundIntroduce.call(anotherPerson, 30, 'HN')); 
// "I'm John, 30, from HN" 
// ⚠️ Vẫn là "John", không phải "Alice"!
// this đã bị "khóa cứng" = person

// ═══════════════════════════════════════════════════════════
// Use case 1: Event handlers
// ═══════════════════════════════════════════════════════════

class Button {
  constructor(public label: string) {}

  // ❌ SAI: this sẽ mất khi làm event handler
  handleClickWrong() {
    console.log(this.label); // undefined khi click
  }

  // ✅ ĐÚNG: Bind this trong constructor
  constructor(public label: string) {
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    console.log(this.label); // ✅ Works!
  }
}

const btn = new Button('Submit');
document.addEventListener('click', btn.handleClick); 
// ✅ this = btn instance

// ═══════════════════════════════════════════════════════════
// Use case 2: Partial application (Currying)
// ═══════════════════════════════════════════════════════════

function multiply(a: number, b: number, c: number): number {
  return a * b * c;
}

// "Khóa" argument đầu tiên = 2
const double = multiply.bind(null, 2); 
// double = (b, c) => 2 * b * c

console.log(double(3, 4)); // 2 * 3 * 4 = 24
console.log(double(5, 6)); // 2 * 5 * 6 = 60

// "Khóa" 2 arguments đầu
const multiplyBy2And3 = multiply.bind(null, 2, 3);
// multiplyBy2And3 = (c) => 2 * 3 * c

console.log(multiplyBy2And3(4)); // 2 * 3 * 4 = 24

// ═══════════════════════════════════════════════════════════
// Use case 3: setTimeout/setInterval
// ═══════════════════════════════════════════════════════════

class Timer {
  constructor(public count: number = 0) {}

  // ❌ SAI: this mất trong setTimeout
  startWrong() {
    setTimeout(function() {
      this.count++; // ❌ this = window/undefined
      console.log(this.count);
    }, 1000);
  }

  // ✅ ĐÚNG: Bind this
  startBind() {
    setTimeout(function() {
      this.count++; // ✅ this = Timer instance
      console.log(this.count);
    }.bind(this), 1000);
  }

  // ✅ ĐÚNG: Arrow function (khuyến nghị)
  startArrow() {
    setTimeout(() => {
      this.count++; // ✅ Arrow lấy this từ outer scope
      console.log(this.count);
    }, 1000);
  }
}
```

---

### **3. So Sánh Tổng Quan**

#### **3.1. Arrow vs Regular Functions**

| Feature | Arrow Function | Regular Function |
|---------|---------------|------------------|
| **Syntax** | `() => {}` | `function() {}` |
| **this binding** | Lexical (từ outer scope) | Dynamic (runtime) |
| **arguments** | ❌ Không có | ✅ Có |
| **Constructor** | ❌ Không dùng `new` | ✅ Dùng được `new` |
| **Hoisting** | ❌ Không hoisted | ✅ Hoisted |
| **prototype** | ❌ undefined | ✅ Có prototype |
| **Method** | ❌ Không nên dùng | ✅ Nên dùng |
| **Callback** | ✅ Nên dùng | ❌ Mất this |

#### **3.2. call vs apply vs bind**

| Method | Syntax | Invoke ngay? | Use case |
|--------|--------|--------------|----------|
| **call** | `fn.call(thisArg, arg1, arg2)` | ✅ Có | Biết chính xác số arguments |
| **apply** | `fn.apply(thisArg, [args])` | ✅ Có | Arguments là array |
| **bind** | `fn.bind(thisArg, arg1)` | ❌ Không | Event handlers, partial application |

---

### **4. Best Practices & Common Mistakes**

#### **4.1. Best Practices**

```typescript
// ═══════════════════════════════════════════════════════════
// ✅ BEST PRACTICES
// ═══════════════════════════════════════════════════════════

// 1️⃣ Arrow functions cho CALLBACKS
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(n => n * 2); // ✅ Clean

// 2️⃣ Regular functions cho OBJECT METHODS
const user = {
  name: 'John',
  greet() { // ✅ Shorthand method syntax
    console.log(`Hello, ${this.name}`);
  }
};

// 3️⃣ Arrow functions cho NESTED FUNCTIONS (tránh mất this)
class Component {
  data = [];
  
  fetchData() {
    fetch('/api/data')
      .then(response => response.json())
      .then(data => {
        this.data = data; // ✅ Arrow giữ this = Component
      });
  }
}

// 4️⃣ bind() trong CONSTRUCTOR cho event handlers
class Button {
  constructor() {
    this.handleClick = this.handleClick.bind(this); // ✅
  }
  
  handleClick() {
    console.log(this); // ✅ this = Button instance
  }
}

// 5️⃣ Hoặc dùng CLASS FIELDS với arrow (modern)
class ButtonModern {
  handleClick = () => {
    console.log(this); // ✅ Arrow giữ this
  }
}
```

#### **4.2. Common Mistakes**

```typescript
// ═══════════════════════════════════════════════════════════
// ❌ COMMON MISTAKES
// ═══════════════════════════════════════════════════════════

// ❌ 1. Arrow function cho object methods
const obj = {
  name: 'John',
  greet: () => {
    console.log(this.name); // ❌ undefined (this = window)
  }
};

// ✅ Fix: Dùng regular function hoặc method shorthand
const obj = {
  name: 'John',
  greet() {
    console.log(this.name); // ✅ "John"
  }
};

// ❌ 2. Quên bind this cho event handlers
class Component {
  name = 'MyComponent';
  
  handleClick() {
    console.log(this.name); // ❌ undefined
  }
  
  componentDidMount() {
    button.addEventListener('click', this.handleClick);
    // ❌ this mất khi click!
  }
}

// ✅ Fix: Bind hoặc arrow function
class Component {
  name = 'MyComponent';
  
  // Option 1: Bind trong constructor
  constructor() {
    this.handleClick = this.handleClick.bind(this);
  }
  
  handleClick() {
    console.log(this.name); // ✅ "MyComponent"
  }
  
  // Option 2: Arrow function (khuyến nghị)
  handleClickArrow = () => {
    console.log(this.name); // ✅ "MyComponent"
  }
}

// ❌ 3. Dùng arguments trong arrow function
const sum = (...numbers) => {
  // console.log(arguments); // ❌ ReferenceError
  console.log(numbers); // ✅ Dùng rest parameters
  return numbers.reduce((a, b) => a + b, 0);
};

// ❌ 4. Bind nhiều lần (không cần thiết)
const fn = function() { console.log(this.name); };
const obj = { name: 'John' };

const bound1 = fn.bind(obj);
const bound2 = bound1.bind({ name: 'Alice' });
bound2(); // "John" - ❌ Bind chỉ có hiệu lực lần đầu!

// ❌ 5. Nhầm lẫn call/apply/bind
fn.call(obj);   // ✅ Gọi NGAY
fn.apply(obj);  // ✅ Gọi NGAY
fn.bind(obj);   // ❌ KHÔNG gọi, trả về function mới!
fn.bind(obj)(); // ✅ Phải gọi thêm ()
```

---

### **5. Real-World Examples**

```typescript
// ═══════════════════════════════════════════════════════════
// REACT COMPONENT
// ═══════════════════════════════════════════════════════════

class TodoList extends React.Component {
  state = {
    todos: [],
    newTodo: ''
  };

  // ✅ Arrow function - auto bind this
  handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    this.setState({ newTodo: e.target.value });
  }

  // ✅ Arrow function - auto bind this
  addTodo = () => {
    this.setState(prev => ({
      todos: [...prev.todos, prev.newTodo],
      newTodo: ''
    }));
  }

  // ✅ Regular function OK cho lifecycle methods
  componentDidMount() {
    // Fetch data...
    fetch('/api/todos')
      .then(res => res.json())
      .then(todos => {
        this.setState({ todos }); // ✅ Arrow trong callback
      });
  }

  render() {
    return (
      <div>
        <input 
          value={this.state.newTodo}
          onChange={this.handleInputChange} // ✅ No need .bind(this)
        />
        <button onClick={this.addTodo}>Add</button>
      </div>
    );
  }
}

// ═══════════════════════════════════════════════════════════
// DEBOUNCE FUNCTION với bind
// ═══════════════════════════════════════════════════════════

function debounce<T extends (...args: any[]) => any>(
  fn: T,
  delay: number
): (...args: Parameters<T>) => void {
  let timeoutId: NodeJS.Timeout;

  return function(this: any, ...args: Parameters<T>) {
    clearTimeout(timeoutId);
    
    timeoutId = setTimeout(() => {
      fn.apply(this, args); // ✅ Giữ this context
    }, delay);
  };
}

class SearchBox {
  searchTerm = '';

  search(query: string) {
    console.log(`Searching for: ${query}`);
    console.log(`Current term: ${this.searchTerm}`);
  }

  // Debounce với bind
  debouncedSearch = debounce(this.search, 300).bind(this);
}
```

---

### **💡 Key Takeaways**

**Arrow Functions:**
- ✅ Dùng cho callbacks, array methods (map, filter, forEach...)
- ✅ Dùng khi muốn giữ this từ outer scope
- ❌ Không dùng cho object methods
- ❌ Không dùng làm constructors

**Regular Functions:**
- ✅ Dùng cho object methods
- ✅ Dùng khi cần arguments object
- ✅ Dùng làm constructors
- ❌ Dễ mất this trong callbacks (phải bind)

**call/apply/bind:**
- 📞 **call**: Gọi ngay với args riêng lẻ → function borrowing
- 📋 **apply**: Gọi ngay với array args → Math.max(array)
- 🔗 **bind**: Tạo function mới → event handlers, partial application

**Remember:**
> "Arrow function = lexical this (từ outer scope). Regular function = dynamic this (runtime). Dùng call/apply khi cần gọi ngay, bind khi cần function mới với this cố định!" 🎯

