# 📚 JavaScript Core Fundamentals - Câu Hỏi Phỏng Vấn

> **Tất cả examples được viết bằng TypeScript với chú thích tiếng Việt chi tiết**
> **Highlight các nội dung quan trọng để dễ hiểu và nhớ lâu**

## 🎯 **Mục Lục**

### **Phần 1: Data Types & Memory Management**
- [Q1: Primitive vs Reference Values - Giá Trị Nguyên Thủy vs Tham Chiếu](#q1-primitive-vs-reference-values---giá-trị-nguyên-thủy-vs-tham-chiếu)
- [Q2: Immutable vs Mutable](#q2-immutable-vs-mutable)
- [Q3: Deep Copy vs Shallow Copy](#q3-deep-copy-vs-shallow-copy)
- [Q4: Spread Operator (...)](#q4-spread-operator-)

### **Phần 2: ES5 vs ES6+ Features**
- [Q5: ES5 vs ES6+ Features - So Sánh Chi Tiết](#q5-es5-vs-es6-features---so-sánh-chi-tiết)
- [Q6: let, const, var](#q6-let-const-var)
- [Q7: Hoisting](#q7-hoisting)
- [Q8: Set/Map, WeakSet/WeakMap](#q8-setmap-weaksetweakmap)

### **Phần 3: JavaScript Engine & Event Loop**
- [Q9: Call Stack, Callback Queue, Event Loop - Cơ Chế Hoạt Động JavaScript](#q9-call-stack-callback-queue-event-loop---cơ-chế-hoạt-động-javascript)
- [Q10: Event Loop - Giải thích đơn giản](#q10-event-loop---giải-thích-đơn-giản)
- [Q11: Web APIs (setTimeout, DOM Events)](#q11-web-apis-settimeout-dom-events)
- [Q12: Microtask vs Macrotask](#q12-microtask-vs-macrotask)

### **Phần 4: Functions & Context**
- [Q13: Closure & Data Privacy](#q13-closure--data-privacy)
- [Q14: Arrow vs Regular Functions](#q14-arrow-vs-regular-functions)
- [Q15: this Binding (call, apply, bind)](#q15-this-binding-call-apply-bind)
- [Q16: IIFE (Immediately Invoked Function Expression)](#q16-iife-immediately-invoked-function-expression)

### **Phần 5: DOM & Events**
- [Q17: Event Bubbling vs Event Capturing](#q17-event-bubbling-vs-event-capturing)
- [Q18: Event Delegation](#q18-event-delegation)
- [Q19: currentTarget vs target](#q19-currenttarget-vs-target)
- [Q20: DOM API & Query Methods](#q20-dom-api--query-methods)

### **Phần 6: Type Checking & Operators**
- [Q21: Falsy/Truthy Values](#q21-falsytruthy-values)
- [Q22: == vs === (Type Coercion)](#q22--vs--type-coercion)
- [Q23: null vs undefined](#q23-null-vs-undefined)
- [Q24: typeof Operator](#q24-typeof-operator)
- [Q25: || && ?? và Optional Chaining](#q25----và-optional-chaining)

### **Phần 7: Asynchronous JavaScript**
- [Q26: Async/Await vs Promises vs Callbacks](#q26-asyncawait-vs-promises-vs-callbacks)
- [Q27: Promise.all, Promise.any, Promise.race](#q27-promiseall-promiseany-promiserace)
- [Q28: Axios Interceptors](#q28-axios-interceptors)

### **Phần 8: Object Manipulation**
- [Q29: Remove Property from Object](#q29-remove-property-from-object)
- [Q30: Compare Objects](#q30-compare-objects)
- [Q31: Combine Strings](#q31-combine-strings)

### **Phần 9: Advanced Topics**
- [Q32: Functional Programming - Pure Functions, Currying & HOF](#q32-functional-programming---pure-functions-currying--hof)
- [Q33: Browser Rendering (Paint, Repaint, Reflow)](#q33-browser-rendering-paint-repaint-reflow)
- [Q34: Loop Performance](#q34-loop-performance)
- [Q35: Strict Mode](#q35-strict-mode)
- [Q36: JavaScript Proxy](#q36-javascript-proxy)
- [Q37: JavaScript Classes](#q37-javascript-classes)

### **Phần 10: Advanced Functional Programming**
- [Q38: Polyfill & Transpiling](#q38-polyfill--transpiling)

### **Phần 11: Advanced Asynchronous Patterns**
- [Q39: EventEmitter & Observer Pattern](#q39-eventemitter--observer-pattern)
- [Q40: Generator Functions & Async Generators](#q40-generator-functions--async-generators)

### **Phần 12: Memory Management & Performance**
- [Q41: Memory Management & Garbage Collection](#q41-memory-management--garbage-collection)
- [Q42: Memory Leaks Detection & Prevention](#q42-memory-leaks-detection--prevention)

### **Phần 13: Module System & Advanced Object Concepts**
- [Q43: Dynamic Import & Module System](#q43-dynamic-import--module-system)
- [Q44: Advanced Array & Object Methods](#q44-advanced-array--object-methods)
- [Q45: Advanced Object Concepts](#q45-advanced-object-concepts)

### **Phần 14: Advanced Mistakes & Security**
- [Q46: Common JavaScript Mistakes - Lỗi Thường Gặp](#q46-common-javascript-mistakes---lỗi-thường-gặp)
- [Q47: JavaScript Security Vulnerabilities - Lỗ Hổng Bảo Mật](#q47-javascript-security-vulnerabilities---lỗ-hổng-bảo-mật)
- [Q48: Performance Anti-Patterns - Anti-Patterns Hiệu Suất](#q48-performance-anti-patterns---anti-patterns-hiệu-suất)

---

## **Phần 1: Data Types & Memory Management**

### **Q1: Primitive vs Reference Values - Giá Trị Nguyên Thủy vs Tham Chiếu**

**Trả lời:**
- **🔥 Primitive Values (Giá trị nguyên thủy)**: Là các giá trị cơ bản được lưu trữ trực tiếp trong memory stack (lưu trực tiếp trong ngăn xếp bộ nhớ)
- **🎯 Reference Values (Giá trị tham chiếu)**: Là các object được lưu trữ trong heap, chỉ có địa chỉ được lưu trong stack (đối tượng lưu trong heap, chỉ địa chỉ trong stack)
- **✅ Ưu điểm Primitive**: Nhanh hơn, an toàn hơn, không có side effects (không có tác dụng phụ)
- **⚠️ Nhược điểm Reference**: Có thể gây memory leak, thay đổi không mong muốn khi copy (có thể gây rò rỉ bộ nhớ)

**Code Example:**
```typescript
// 🔥 Primitive Values (Giá trị nguyên thủy) - lưu trực tiếp giá trị
let name: string = "Nguyen Van A";        // string - chuỗi
let age: number = 25;                     // number - số
let isActive: boolean = true;             // boolean - true/false
let data: null = null;                    // null - rỗng
let info: undefined = undefined;          // undefined - chưa định nghĩa
let id: symbol = Symbol('id');            // symbol - duy nhất
let bigNum: bigint = 123n;                // bigint - số nguyên lớn

// 🎯 Reference Values (Giá trị tham chiếu) - lưu địa chỉ trong stack, data trong heap
let person: object = { name: "A", age: 25 };  // object - đối tượng
let numbers: number[] = [1, 2, 3];            // array - mảng
let func: Function = () => console.log("Hi"); // function - hàm

// 🔥 So sánh Primitive vs Reference (So sánh giá trị nguyên thủy vs tham chiếu)
let a: number = 10;
let b: number = a;  // b = 10 (copy giá trị - sao chép giá trị)
b = 20;             // a vẫn = 10, b = 20 (a không bị ảnh hưởng)

let obj1: object = { x: 10 };
let obj2: object = obj1;  // obj2 trỏ đến cùng địa chỉ với obj1 (cùng tham chiếu)
obj2.x = 20;              // obj1.x cũng = 20 (cùng reference - cả hai thay đổi)

// 🎯 Practical Example (Ví dụ thực tế)
// Primitive - an toàn
let userName = "John";
let displayName = userName;               // Copy giá trị
displayName = "Jane";
console.log(userName);    // "John" - không thay đổi
console.log(displayName); // "Jane" - chỉ displayName thay đổi

// Reference - cần cẩn thận
let user = { name: "John", age: 25 };
let userCopy = user;                      // Copy địa chỉ
userCopy.name = "Jane";
console.log(user.name);     // "Jane" - user bị thay đổi!
console.log(userCopy.name); // "Jane" - cả hai cùng thay đổi
```

**🎯 Best Practices:**
- **✅ Sử dụng primitive values** khi có thể để tránh side effects
- **✅ Cẩn thận với reference values** khi pass vào functions - có thể bị thay đổi
- **✅ Sử dụng const cho reference values** để tránh reassignment (tránh gán lại)
- **✅ Sử dụng spread operator** để shallow copy: `{...obj}`, `[...array]`
- **✅ Sử dụng deep copy** cho nested objects: `JSON.parse(JSON.stringify(obj))`

**❌ Common Mistakes:**
```typescript
// ❌ Sai: Không hiểu reference copy (không hiểu sao chép tham chiếu)
let arr1 = [1, 2, 3];
let arr2 = arr1;        // Copy địa chỉ, không phải giá trị
arr2.push(4);           // arr1 cũng bị thay đổi!

// ✅ Đúng: Tạo copy mới (tạo bản sao mới)
let arr1 = [1, 2, 3];
let arr2 = [...arr1];   // shallow copy (sao chép nông)
arr2.push(4);           // arr1 không bị ảnh hưởng

// ❌ Sai: So sánh reference values (so sánh giá trị tham chiếu)
let obj1 = { name: "John" };
let obj2 = { name: "John" };
console.log(obj1 === obj2); // false - khác địa chỉ

// ✅ Đúng: So sánh nội dung (so sánh nội dung)
console.log(JSON.stringify(obj1) === JSON.stringify(obj2)); // true

// ❌ Sai: Thay đổi object gốc (thay đổi đối tượng gốc)
function updateUser(user: any) {
  user.name = "Updated"; // Thay đổi object gốc
}

// ✅ Đúng: Tạo object mới (tạo đối tượng mới)
function updateUser(user: any) {
  return { ...user, name: "Updated" }; // Trả về object mới
}
```

---

### **Q2: Immutable vs Mutable**

**Trả lời:**
- **Immutable**: Không thể thay đổi sau khi tạo, tạo ra giá trị mới khi modify
- **Mutable**: Có thể thay đổi trực tiếp giá trị hiện tại
- **Ưu điểm**: Immutable an toàn hơn, dễ debug, tránh side effects
- **Nhược điểm**: Immutable tốn memory hơn, performance chậm hơn

**Code Example:**
```typescript
// Mutable - có thể thay đổi trực tiếp
let mutableArray: number[] = [1, 2, 3];
mutableArray.push(4);        // Thay đổi array gốc
mutableArray[0] = 10;        // Thay đổi phần tử

let mutableObject: {name: string, age: number} = { name: "A", age: 25 };
mutableObject.age = 26;      // Thay đổi object gốc

// Immutable - tạo giá trị mới
let immutableArray: readonly number[] = [1, 2, 3] as const;
// immutableArray.push(4);   // ❌ Error: Cannot modify readonly array

// Tạo array mới thay vì modify
let newArray: number[] = [...immutableArray, 4];  // [1, 2, 3, 4]
let updatedArray: number[] = immutableArray.map(x => x * 2);  // [2, 4, 6]

// Immutable object với spread operator
let immutableObj: {name: string, age: number} = { name: "A", age: 25 };
let newObj: {name: string, age: number} = { ...immutableObj, age: 26 };
```

**Best Practices:**
- Sử dụng `readonly` cho arrays và objects khi có thể
- Sử dụng spread operator để tạo copy
- Sử dụng `Object.freeze()` để làm immutable object
- Sử dụng libraries như Immer cho complex immutable operations

**Mistakes:**
```typescript
// ❌ Sai: Modify trực tiếp
let users = [{ name: "A", age: 25 }];
users[0].age = 26;  // Modify trực tiếp

// ✅ Đúng: Tạo object mới
let users = [{ name: "A", age: 25 }];
let updatedUsers = users.map(user =>
  user.name === "A" ? { ...user, age: 26 } : user
);
```

---

### **Q3: Deep Copy vs Shallow Copy**

**Trả lời:**
- **Shallow Copy**: Copy cấp đầu tiên, nested objects vẫn share reference
- **Deep Copy**: Copy toàn bộ, tạo ra object hoàn toàn mới
- **Ưu điểm**: Deep copy an toàn hơn, shallow copy nhanh hơn
- **Nhược điểm**: Deep copy tốn memory và thời gian hơn

**Code Example:**
```typescript
// Shallow Copy - chỉ copy cấp đầu
let original: {name: string, address: {city: string}} = {
  name: "Nguyen Van A",
  address: { city: "Ho Chi Minh" }
};

// Các cách shallow copy
let shallow1 = { ...original };                    // Spread operator
let shallow2 = Object.assign({}, original);        // Object.assign
let shallow3 = original.slice();                   // Array slice (cho arrays)

// Vấn đề với shallow copy
shallow1.name = "Nguyen Van B";           // ✅ OK - primitive
shallow1.address.city = "Ha Noi";         // ❌ Ảnh hưởng original!

console.log(original.address.city);       // "Ha Noi" - bị thay đổi!

// Deep Copy - copy toàn bộ
function deepCopy<T>(obj: T): T {
  if (obj === null || typeof obj !== "object") return obj;
  if (obj instanceof Date) return new Date(obj.getTime()) as any;
  if (obj instanceof Array) return obj.map(item => deepCopy(item)) as any;
  if (typeof obj === "object") {
    const copy: any = {};
    Object.keys(obj).forEach(key => {
      copy[key] = deepCopy((obj as any)[key]);
    });
    return copy;
  }
  return obj;
}

let deepCopied = deepCopy(original);
deepCopied.address.city = "Da Nang";      // ✅ Không ảnh hưởng original
console.log(original.address.city);       // "Ho Chi Minh" - không đổi

// Sử dụng JSON (có hạn chế)
let jsonDeepCopy = JSON.parse(JSON.stringify(original));
// ❌ Mất functions, undefined, symbols, dates
```

**Best Practices:**
- Sử dụng shallow copy cho simple objects
- Sử dụng deep copy cho nested objects
- Sử dụng `structuredClone()` (modern browsers)
- Sử dụng libraries như Lodash `cloneDeep()`

**Mistakes:**
```typescript
// ❌ Sai: Nghĩ spread operator là deep copy
let obj = { a: { b: 1 } };
let copy = { ...obj };
copy.a.b = 2;  // obj.a.b cũng = 2!

// ✅ Đúng: Sử dụng deep copy
let copy = structuredClone(obj);  // hoặc custom deep copy function
```

---

### **Q4: Spread Operator (...)**

**Trả lời:**
- **Spread Operator**: Toán tử `...` để expand iterable values
- **Hoạt động**: Copy elements từ array/object vào vị trí mới
- **Ưu điểm**: Code ngắn gọn, dễ đọc, immutable operations
- **Nhược điểm**: Có thể gây confusion với rest parameters

**Code Example:**
```typescript
// Array Spread
let arr1: number[] = [1, 2, 3];
let arr2: number[] = [4, 5, 6];
let combined: number[] = [...arr1, ...arr2];  // [1, 2, 3, 4, 5, 6]

// Thêm phần tử
let newArr: number[] = [...arr1, 4, 5];       // [1, 2, 3, 4, 5]

// Copy array
let arrCopy: number[] = [...arr1];             // [1, 2, 3] - shallow copy

// Object Spread
let person: {name: string, age: number} = { name: "A", age: 25 };
let updatedPerson: {name: string, age: number, city: string} = {
  ...person,
  city: "HCM",
  age: 26  // Override age
};

// Merge objects
let obj1: {a: number} = { a: 1 };
let obj2: {b: number} = { b: 2 };
let merged: {a: number, b: number} = { ...obj1, ...obj2 };  // {a: 1, b: 2}

// Function arguments
function sum(...numbers: number[]): number {
  return numbers.reduce((total, num) => total + num, 0);
}
sum(1, 2, 3, 4);  // 10

// Destructuring với spread
let [first, ...rest]: number[] = [1, 2, 3, 4];
console.log(first);  // 1
console.log(rest);   // [2, 3, 4]
```

**Best Practices:**
- Sử dụng cho array/object copying
- Sử dụng cho function parameters
- Sử dụng cho destructuring
- Cẩn thận với nested objects (shallow copy)

**Mistakes:**
```typescript
// ❌ Sai: Spread với non-iterable
let obj = { a: 1, b: 2 };
let arr = [...obj];  // ❌ Error: obj is not iterable

// ✅ Đúng: Spread với arrays
let arr = [...Object.values(obj)];  // [1, 2]

// ❌ Sai: Nghĩ spread là deep copy
let nested = { a: { b: 1 } };
let copy = { ...nested };
copy.a.b = 2;  // nested.a.b cũng = 2!
```

---

## **Phần 2: ES5 vs ES6+ Features**

### **Q5: ES5 vs ES6+ Features - So Sánh Chi Tiết**

**Trả lời:**
- **ES5 (2009)**: JavaScript cơ bản với function declarations, var, basic objects
- **ES6+ (2015+)**: Modern JavaScript với classes, modules, arrow functions, destructuring
- **🔥 Ưu điểm ES6+**: Code ngắn gọn hơn, type-safe hơn, performance tốt hơn, syntax hiện đại
- **⚠️ Nhược điểm ES6+**: Cần transpilation cho older browsers, learning curve cao hơn

**Code Example:**
```typescript
// 🔥 ES5 vs ES6+ - So sánh chi tiết

// 📝 Variables (Biến)
// ES5 - Chỉ có var
var nameES5 = "Nguyen Van A";        // Function scoped
var ageES5 = 25;                     // Có thể redeclare

// ES6+ - let và const
let nameES6 = "Nguyen Van A";        // Block scoped
const ageES6 = 25;                   // Không thể reassign

// 📝 Functions (Hàm)
// ES5 - Function declarations
function PersonES5(name: string, age: number) {
  this.name = name;                  // Constructor function
  this.age = age;
}
PersonES5.prototype.greet = function() {
  return "Hello, I'm " + this.name;  // String concatenation
};

// ES6+ - Classes và Arrow functions
class PersonES6 {
  constructor(public name: string, public age: number) {} // Constructor shorthand

  greet(): string {
    return `Hello, I'm ${this.name}`; // Template literals
  }
}

// ES5 - Function declarations
function multiplyES5(a: number, b: number): number {
  return a * b;
}

// ES6+ - Arrow functions (ngắn gọn hơn)
const multiplyES6 = (a: number, b: number): number => a * b;

// 📝 Objects (Đối tượng)
// ES5 - Object creation
var userES5 = {
  name: "John",
  getName: function() {              // Method syntax cũ
    return this.name;
  }
};

// ES6+ - Object shorthand và method syntax
const userES6 = {
  name: "John",
  getName() {                        // Method shorthand
    return this.name;
  }
};

// 📝 Destructuring (Phân rã)
// ES5 - Manual assignment
var user = { name: 'John', age: 25 };
var name = user.name;
var age = user.age;

// ES6+ - Destructuring assignment
const { name, age } = user;          // Destructuring

// 📝 Modules (Mô-đun)
// ES5 - No native modules
// Phải sử dụng libraries như RequireJS

// ES6+ - Native modules
export const name = 'John';          // Named export
export default function greet() { }  // Default export
import { name } from './module';     // Import

// 📝 Promises (Lời hứa)
// ES5 - No native promises
// Phải sử dụng libraries như Bluebird

// ES6+ - Native promises
const promise = new Promise((resolve, reject) => {
  // async operation
});
```

**🎯 Best Practices:**
- **✅ Sử dụng ES6+ features** khi có thể để code ngắn gọn và hiện đại
- **✅ Sử dụng Babel** để transpile cho older browsers
- **✅ Sử dụng TypeScript** cho type safety và better development experience
- **✅ Sử dụng modern syntax** cho better performance và maintainability

**❌ Common Mistakes:**
```typescript
// ❌ Sai: Sử dụng var thay vì let/const
var name = "John";  // Function scoped, có thể gây confusion

// ✅ Đúng: Sử dụng let/const
let name = "John";  // Block scoped, rõ ràng hơn
const age = 25;     // Immutable, an toàn hơn

// ❌ Sai: Không sử dụng template literals
const message = "Hello " + name + ", you are " + age + " years old";

// ✅ Đúng: Sử dụng template literals
const message = `Hello ${name}, you are ${age} years old`;
```

---

### **Q6: let, const, var**

**Trả lời:**
- **var**: Function-scoped, hoisted, có thể redeclare
- **let**: Block-scoped, hoisted nhưng không initialized, không thể redeclare
- **const**: Block-scoped, hoisted nhưng không initialized, không thể reassign
- **Ưu điểm**: let/const an toàn hơn, tránh hoisting issues
- **Nhược điểm**: var có thể gây confusion với scope

**Code Example:**
```typescript
// var - Function scoped
function varExample(): void {
  if (true) {
    var x: number = 10;  // Function scoped
  }
  console.log(x);  // 10 - accessible outside block
}

// let - Block scoped
function letExample(): void {
  if (true) {
    let y: number = 20;  // Block scoped
  }
  // console.log(y);  // ❌ Error: y is not defined
}

// const - Block scoped, immutable
function constExample(): void {
  const z: number = 30;  // Cannot reassign
  // z = 40;  // ❌ Error: Cannot assign to const

  const obj: {name: string} = { name: "A" };
  obj.name = "B";  // ✅ OK - object properties can change
  // obj = {};  // ❌ Error: Cannot reassign const
}

// Hoisting differences
console.log(a);  // undefined (hoisted but not initialized)
var a: number = 5;

// console.log(b);  // ❌ Error: Cannot access before initialization
let b: number = 10;

// console.log(c);  // ❌ Error: Cannot access before initialization
const c: number = 15;
```

**Best Practices:**
- Sử dụng `const` mặc định
- Sử dụng `let` khi cần reassign
- Tránh sử dụng `var`
- Sử dụng TypeScript cho type safety

**Mistakes:**
```typescript
// ❌ Sai: Sử dụng var trong loops
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);  // 3, 3, 3
}

// ✅ Đúng: Sử dụng let
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);  // 0, 1, 2
}
```

---

### **Q7: Hoisting**

**Trả lời:**
- **Hoisting**: Cơ chế JavaScript move declarations lên top của scope
- **Hoạt động**: Function declarations hoisted hoàn toàn, var hoisted nhưng undefined
- **Ưu điểm**: Có thể gọi function trước khi declare
- **Nhược điểm**: Có thể gây confusion, bugs khó debug

**Code Example:**
```typescript
// Function Declaration - hoisted hoàn toàn
console.log(sayHello("World"));  // "Hello World" - hoạt động!

function sayHello(name: string): string {
  return `Hello ${name}`;
}

// Function Expression - không hoisted
// console.log(sayGoodbye("World"));  // ❌ Error: Cannot access before initialization
const sayGoodbye = function(name: string): string {
  return `Goodbye ${name}`;
};

// var - hoisted nhưng undefined
console.log(x);  // undefined (không error)
var x: number = 5;
console.log(x);  // 5

// let/const - hoisted nhưng không accessible
// console.log(y);  // ❌ Error: Cannot access before initialization
let y: number = 10;

// Class - không hoisted
// const person = new Person("John");  // ❌ Error: Cannot access before initialization
class Person {
  constructor(public name: string) {}
}
```

**Best Practices:**
- Declare variables ở top của scope
- Sử dụng let/const thay vì var
- Sử dụng function declarations cho hoisting
- Sử dụng TypeScript để catch hoisting issues

**Mistakes:**
```typescript
// ❌ Sai: Nghĩ var có giá trị khi hoisted
console.log(a);  // undefined, không phải 5
var a = 5;

// ✅ Đúng: Hiểu hoisting behavior
let a = 5;
console.log(a);  // 5
```

---

### **Q8: Set/Map, WeakSet/WeakMap**

**Trả lời:**
- **Set**: Collection unique values, không có keys
- **Map**: Collection key-value pairs, keys có thể là bất kỳ type nào
- **WeakSet/WeakMap**: Weak references, không prevent garbage collection
- **Ưu điểm**: Set/Map performance tốt hơn objects, WeakSet/WeakMap tránh memory leaks
- **Nhược điểm**: WeakSet/WeakMap không iterable, không có size property

**Code Example:**
```typescript
// Set - Collection unique values
let numberSet: Set<number> = new Set([1, 2, 3, 3, 4]);
console.log(numberSet);  // Set(4) {1, 2, 3, 4} - duplicate removed

numberSet.add(5);
numberSet.delete(1);
console.log(numberSet.has(2));  // true
console.log(numberSet.size);    // 4

// Iterate Set
for (let value of numberSet) {
  console.log(value);  // 2, 3, 4, 5
}

// Map - Key-value pairs
let userMap: Map<string, {name: string, age: number}> = new Map();
userMap.set("user1", { name: "John", age: 25 });
userMap.set("user2", { name: "Jane", age: 30 });

console.log(userMap.get("user1"));  // {name: "John", age: 25}
console.log(userMap.has("user1"));  // true
console.log(userMap.size);          // 2

// Map vs Object
let obj: {[key: string]: any} = {};
obj[1] = "one";        // key becomes string "1"
obj[true] = "true";    // key becomes string "true"

let map = new Map();
map.set(1, "one");     // key is number 1
map.set(true, "true"); // key is boolean true

// WeakSet - Weak references
let weakSet: WeakSet<object> = new WeakSet();
let obj1: object = { name: "A" };
let obj2: object = { name: "B" };

weakSet.add(obj1);
weakSet.add(obj2);
console.log(weakSet.has(obj1));  // true

obj1 = null;  // obj1 có thể bị garbage collected
// weakSet không prevent garbage collection

// WeakMap - Weak references với keys
let weakMap: WeakMap<object, string> = new WeakMap();
let keyObj: object = { id: 1 };
weakMap.set(keyObj, "value");
console.log(weakMap.get(keyObj));  // "value"

keyObj = null;  // keyObj có thể bị garbage collected
```

**Best Practices:**
- Sử dụng Set cho unique values
- Sử dụng Map cho key-value pairs với non-string keys
- Sử dụng WeakSet/WeakMap cho temporary references
- Sử dụng Map thay vì Object khi cần performance

**Mistakes:**
```typescript
// ❌ Sai: Sử dụng Object cho unique values
let uniqueValues: {[key: string]: boolean} = {};
uniqueValues["a"] = true;
uniqueValues["b"] = true;
uniqueValues["a"] = true;  // Duplicate, nhưng không bị detect

// ✅ Đúng: Sử dụng Set
let uniqueValues = new Set(["a", "b", "a"]);  // Set(2) {"a", "b"}
```

---

## **Phần 3: JavaScript Engine & Event Loop**

### **Q9: Call Stack, Callback Queue, Event Loop - Cơ Chế Hoạt Động JavaScript**

**Trả lời:**
- **🔥 Call Stack (Ngăn xếp gọi)**: LIFO stack chứa function calls đang thực thi (ngăn xếp LIFO chứa các lời gọi hàm đang thực thi)
- **🎯 Callback Queue (Hàng đợi callback)**: Queue chứa callbacks từ Web APIs (hàng đợi chứa callback từ Web APIs)
- **⚡ Event Loop (Vòng lặp sự kiện)**: Cơ chế kiểm tra Call Stack và Callback Queue (cơ chế kiểm tra ngăn xếp gọi và hàng đợi callback)
- **🔄 Hoạt động**: Event Loop đợi Call Stack empty, sau đó move callbacks từ Queue vào Stack (vòng lặp sự kiện đợi ngăn xếp rỗng, sau đó chuyển callback từ hàng đợi vào ngăn xếp)
- **✅ Ưu điểm**: Non-blocking I/O, responsive UI (I/O không chặn, giao diện phản hồi)
- **⚠️ Nhược điểm**: Có thể gây callback hell nếu không quản lý tốt (có thể gây địa ngục callback)

**Code Example:**
```typescript
// Call Stack Example
function first(): void {
  console.log("1. First function");
  second();
  console.log("4. First function end");
}

function second(): void {
  console.log("2. Second function");
  third();
  console.log("3. Second function end");
}

function third(): void {
  console.log("3. Third function");
}

first();
// Output: 1, 2, 3, 3, 4

// Callback Queue Example
console.log("1. Start");

setTimeout(() => {
  console.log("4. setTimeout callback");
}, 0);

console.log("2. Middle");

setTimeout(() => {
  console.log("5. Another setTimeout");
}, 0);

console.log("3. End");

// Output: 1, 2, 3, 4, 5
// Call Stack: main execution
// Callback Queue: setTimeout callbacks
// Event Loop: moves callbacks to stack when stack is empty
```

**Best Practices:**
- Hiểu thứ tự execution
- Sử dụng async/await thay vì callbacks
- Tránh blocking operations
- Sử dụng proper error handling

---

### **Q10: Event Loop - Giải thích đơn giản**

**Trả lời:**
Event Loop giống như một người bảo vệ ở cửa hàng:
1. **Call Stack** = Quầy thanh toán (chỉ 1 người thanh toán tại 1 thời điểm)
2. **Callback Queue** = Hàng chờ (những người đợi thanh toán)
3. **Event Loop** = Người bảo vệ (kiểm tra quầy thanh toán có trống không)

**Quy trình:**
- Khi quầy thanh toán trống → Người bảo vệ gọi người tiếp theo từ hàng chờ
- Khi quầy thanh toán bận → Mọi người phải đợi
- setTimeout, DOM events, fetch requests → Được đưa vào hàng chờ

**Code Example:**
```typescript
// Giải thích bằng ví dụ thực tế
console.log("🍕 Đặt pizza");

setTimeout(() => {
  console.log("📞 Pizza giao đến (sau 2 giây)");
}, 2000);

console.log("📺 Xem TV trong khi đợi");

setTimeout(() => {
  console.log("🚪 Mở cửa nhận pizza");
}, 2000);

console.log("🍿 Ăn bỏng ngô");

// Output:
// 🍕 Đặt pizza
// 📺 Xem TV trong khi đợi
// 🍿 Ăn bỏng ngô
// 📞 Pizza giao đến (sau 2 giây)
// 🚪 Mở cửa nhận pizza

// Giải thích:
// 1. "Đặt pizza" - thực thi ngay
// 2. "Pizza giao đến" - đưa vào hàng chờ (2 giây)
// 3. "Xem TV" - thực thi ngay
// 4. "Mở cửa" - đưa vào hàng chờ (2 giây)
// 5. "Ăn bỏng ngô" - thực thi ngay
// 6. Sau 2 giây: Event Loop đưa callbacks từ hàng chờ vào thực thi
```

**Best Practices:**
- Hiểu rằng JavaScript là single-threaded
- Sử dụng async operations cho I/O
- Tránh blocking operations
- Sử dụng proper timing

---

### **Q11: Web APIs (setTimeout, DOM Events)**

**Trả lời:**
- **Web APIs**: APIs được cung cấp bởi browser, không phải JavaScript engine
- **setTimeout**: Đặt timer, callback được đưa vào Callback Queue sau delay
- **DOM Events**: Event listeners được đưa vào Callback Queue khi event xảy ra
- **Ưu điểm**: Non-blocking, responsive UI
- **Nhược điểm**: Có thể gây memory leaks nếu không cleanup

**Code Example:**
```typescript
// setTimeout - Web API
console.log("1. Start");

setTimeout(() => {
  console.log("3. setTimeout callback");
}, 0);

console.log("2. End");

// Output: 1, 2, 3
// Giải thích: setTimeout đưa callback vào Callback Queue

// DOM Events - Web API
document.addEventListener('click', (event: MouseEvent) => {
  console.log('Button clicked!', event.target);
});

// fetch - Web API
fetch('/api/data')
  .then(response => response.json())
  .then(data => console.log(data));

// XMLHttpRequest - Web API
const xhr = new XMLHttpRequest();
xhr.open('GET', '/api/data');
xhr.onload = () => console.log(xhr.responseText);
xhr.send();

// Intersection Observer - Web API
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      console.log('Element is visible');
    }
  });
});

// Geolocation - Web API
navigator.geolocation.getCurrentPosition((position) => {
  console.log('Latitude:', position.coords.latitude);
});
```

**Best Practices:**
- Cleanup event listeners
- Sử dụng AbortController cho fetch
- Sử dụng proper error handling
- Tránh memory leaks

**Mistakes:**
```typescript
// ❌ Sai: Không cleanup event listeners
document.addEventListener('click', handleClick);
// Memory leak nếu không removeEventListener

// ✅ Đúng: Cleanup event listeners
const controller = new AbortController();
document.addEventListener('click', handleClick, {
  signal: controller.signal
});
// controller.abort() để cleanup
```

---

### **Q12: Microtask vs Macrotask**

**Trả lời:**
- **Microtask**: Promise callbacks, queueMicrotask, có priority cao hơn
- **Macrotask**: setTimeout, setInterval, DOM events, có priority thấp hơn
- **Thứ tự**: Microtask được thực thi trước Macrotask
- **Ưu điểm**: Microtask đảm bảo consistency, Macrotask cho timing
- **Nhược điểm**: Microtask có thể block UI nếu quá nhiều

**Code Example:**
```typescript
// Microtask vs Macrotask Priority
console.log("1. Start");

// Macrotask
setTimeout(() => {
  console.log("6. setTimeout (Macrotask)");
}, 0);

// Microtask
Promise.resolve().then(() => {
  console.log("4. Promise (Microtask)");
});

// Macrotask
setTimeout(() => {
  console.log("7. Another setTimeout (Macrotask)");
}, 0);

// Microtask
queueMicrotask(() => {
  console.log("5. queueMicrotask (Microtask)");
});

console.log("2. Middle");

// Microtask
Promise.resolve().then(() => {
  console.log("3. Another Promise (Microtask)");
});

console.log("3. End");

// Output: 1, 2, 3, 4, 5, 6, 7
// Giải thích:
// 1. Call Stack: 1, 2, 3
// 2. Microtask Queue: 4, 5 (thực thi trước)
// 3. Macrotask Queue: 6, 7 (thực thi sau)

// Promise chain - Microtask
Promise.resolve()
  .then(() => console.log("Microtask 1"))
  .then(() => console.log("Microtask 2"))
  .then(() => console.log("Microtask 3"));

// setTimeout chain - Macrotask
setTimeout(() => console.log("Macrotask 1"), 0);
setTimeout(() => console.log("Macrotask 2"), 0);
setTimeout(() => console.log("Macrotask 3"), 0);
```

**Best Practices:**
- Sử dụng Promise cho async operations
- Sử dụng setTimeout cho timing
- Tránh quá nhiều microtasks
- Hiểu thứ tự execution

**Mistakes:**
```typescript
// ❌ Sai: Nghĩ setTimeout có priority cao
setTimeout(() => console.log("1"), 0);
Promise.resolve().then(() => console.log("2"));
// Output: 2, 1 (Promise thực thi trước)

// ✅ Đúng: Hiểu priority
Promise.resolve().then(() => console.log("1"));
setTimeout(() => console.log("2"), 0);
// Output: 1, 2 (đúng thứ tự)
```

---

## **Phần 4: Functions & Context**

### **Q13: Closure & Data Privacy**

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
    return outerVariable + y;  // Access outer variable
  }

  return innerFunction;
}

const closure = outerFunction(10);
console.log(closure(5));  // 15
// outerFunction đã return nhưng innerFunction vẫn access được outerVariable

// Data Privacy với Closure
function createCounter(): {increment: () => number, getCount: () => number} {
  let count = 0;  // Private variable

  return {
    increment(): number {
      return ++count;  // Access private variable
    },
    getCount(): number {
      return count;    // Access private variable
    }
  };
}

const counter = createCounter();
console.log(counter.increment());  // 1
console.log(counter.increment());  // 2
console.log(counter.getCount());   // 2
// console.log(counter.count);     // ❌ Error: count is private

// Module Pattern
const userModule = (() => {
  let users: string[] = [];  // Private data

  return {
    addUser(name: string): void {
      users.push(name);
    },
    getUsers(): string[] {
      return [...users];  // Return copy
    },
    getUserCount(): number {
      return users.length;
    }
  };
})();

userModule.addUser("John");
userModule.addUser("Jane");
console.log(userModule.getUsers());    // ["John", "Jane"]
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
  setTimeout(() => console.log(i), 100);  // 3, 3, 3
}

// ✅ Đúng: Sử dụng closure đúng cách
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);  // 0, 1, 2
}

// Hoặc sử dụng closure với var
for (var i = 0; i < 3; i++) {
  ((index: number) => {
    setTimeout(() => console.log(index), 100);  // 0, 1, 2
  })(i);
}
```

---

### **Q14: Arrow vs Regular Functions**

**Trả lời:**
- **Arrow Functions**: Shorter syntax, không có own `this`, không hoisted
- **Regular Functions**: Có own `this`, hoisted, có `arguments` object
- **Ưu điểm**: Arrow functions ngắn gọn, `this` binding rõ ràng
- **Nhược điểm**: Arrow functions không thể dùng làm constructor

**Code Example:**
```typescript
// Regular Function
function regularFunction(name: string): string {
  return `Hello ${name}`;
}

// Arrow Function
const arrowFunction = (name: string): string => `Hello ${name}`;

// this binding differences
class Person {
  name: string = "John";

  // Regular function - có own this
  regularMethod(): void {
    setTimeout(function() {
      console.log(this.name);  // ❌ undefined (this = window/global)
    }, 100);
  }

  // Arrow function - inherit this từ outer scope
  arrowMethod(): void {
    setTimeout(() => {
      console.log(this.name);  // ✅ "John" (this = Person instance)
    }, 100);
  }
}

// arguments object
function regularWithArgs(): void {
  console.log(arguments);  // ✅ Có arguments object
}

const arrowWithArgs = (): void => {
  // console.log(arguments);  // ❌ Error: arguments is not defined
};

// Constructor
function RegularConstructor(name: string) {
  this.name = name;
}

// const ArrowConstructor = (name: string) => {
//   this.name = name;  // ❌ Error: Arrow functions cannot be constructors
// };

// Hoisting
console.log(regularHoisted());  // ✅ "Hello" - hoisted
function regularHoisted(): string {
  return "Hello";
}

// console.log(arrowHoisted());  // ❌ Error: Cannot access before initialization
const arrowHoisted = (): string => "Hello";
```

**Best Practices:**
- Sử dụng arrow functions cho callbacks
- Sử dụng regular functions cho methods
- Sử dụng arrow functions cho `this` binding
- Sử dụng regular functions cho constructors

**Mistakes:**
```typescript
// ❌ Sai: Sử dụng arrow function cho object method
const obj = {
  name: "John",
  greet: () => {
    console.log(this.name);  // undefined (this = window)
  }
};

// ✅ Đúng: Sử dụng regular function
const obj = {
  name: "John",
  greet() {
    console.log(this.name);  // "John"
  }
};
```

---

### **Q15: this Binding (call, apply, bind)**

**Trả lời:**
- **this**: Context object mà function được gọi
- **call**: Gọi function với `this` và arguments riêng lẻ
- **apply**: Gọi function với `this` và array of arguments
- **bind**: Tạo function mới với `this` được bind
- **Ưu điểm**: Flexible context, function borrowing
- **Nhược điểm**: Có thể gây confusion nếu không hiểu rõ

**Code Example:**
```typescript
// this binding
const person = {
  name: "John",
  greet(): string {
    return `Hello, I'm ${this.name}`;
  }
};

// call - gọi với this và arguments riêng lẻ
function introduce(age: number, city: string): string {
  return `I'm ${this.name}, ${age} years old, from ${city}`;
}

console.log(introduce.call(person, 25, "HCM"));  // "I'm John, 25 years old, from HCM"

// apply - gọi với this và array of arguments
console.log(introduce.apply(person, [25, "HCM"]));  // "I'm John, 25 years old, from HCM"

// bind - tạo function mới với this được bind
const boundIntroduce = introduce.bind(person);
console.log(boundIntroduce(25, "HCM"));  // "I'm John, 25 years old, from HCM"

// Function borrowing
const car = {
  brand: "Toyota",
  model: "Camry"
};

const bike = {
  brand: "Honda",
  model: "CBR"
};

function getInfo(): string {
  return `${this.brand} ${this.model}`;
}

console.log(getInfo.call(car));   // "Toyota Camry"
console.log(getInfo.call(bike));  // "Honda CBR"

// Partial application với bind
function multiply(a: number, b: number, c: number): number {
  return a * b * c;
}

const double = multiply.bind(null, 2);  // a = 2
console.log(double(3, 4));  // 2 * 3 * 4 = 24

const triple = multiply.bind(null, 3);  // a = 3
console.log(triple(2, 4));  // 3 * 2 * 4 = 24
```

**Best Practices:**
- Sử dụng call/apply cho function borrowing
- Sử dụng bind cho partial application
- Hiểu rõ this context
- Sử dụng arrow functions để tránh this issues

**Mistakes:**
```typescript
// ❌ Sai: Mất this context
const obj = {
  name: "John",
  greet() {
    setTimeout(function() {
      console.log(this.name);  // undefined
    }, 100);
  }
};

// ✅ Đúng: Giữ this context
const obj = {
  name: "John",
  greet() {
    setTimeout(() => {
      console.log(this.name);  // "John"
    }, 100);
  }
};

// Hoặc sử dụng bind
const obj = {
  name: "John",
  greet() {
    setTimeout(function() {
      console.log(this.name);  // "John"
    }.bind(this), 100);
  }
};
```

---

### **Q16: IIFE (Immediately Invoked Function Expression)**

**Trả lời:**
- **IIFE**: Function được gọi ngay lập tức sau khi được định nghĩa
- **Hoạt động**: Tạo scope riêng, tránh global namespace pollution
- **Ưu điểm**: Module pattern, data privacy, tránh hoisting issues
- **Nhược điểm**: Có thể gây confusion, khó debug

**Code Example:**
```typescript
// Basic IIFE
(function(): void {
  console.log("IIFE executed immediately");
})();

// IIFE với parameters
(function(name: string): void {
  console.log(`Hello ${name}`);
})("John");

// IIFE với return value
const result = (function(x: number, y: number): number {
  return x + y;
})(5, 10);
console.log(result);  // 15

// IIFE cho module pattern
const calculator = (function() {
  let result = 0;  // Private variable

  return {
    add(x: number): number {
      result += x;
      return result;
    },
    subtract(x: number): number {
      result -= x;
      return result;
    },
    getResult(): number {
      return result;
    }
  };
})();

calculator.add(10);      // 10
calculator.subtract(3);  // 7
console.log(calculator.getResult());  // 7

// IIFE với async/await
(async function(): Promise<void> {
  try {
    const response = await fetch('/api/data');
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('Error:', error);
  }
})();

// IIFE để tránh hoisting issues
(function(): void {
  // Tất cả variables trong đây là local
  let x = 10;
  let y = 20;

  function localFunction(): void {
    console.log(x + y);
  }

  localFunction();
})();

// console.log(x);  // ❌ Error: x is not defined
```

**Best Practices:**
- Sử dụng IIFE cho module pattern
- Sử dụng IIFE để tránh global pollution
- Sử dụng IIFE cho one-time execution
- Sử dụng TypeScript cho type safety

**Mistakes:**
```typescript
// ❌ Sai: Không sử dụng IIFE khi cần
let x = 10;
let y = 20;
// x, y pollute global scope

// ✅ Đúng: Sử dụng IIFE
(function(): void {
  let x = 10;
  let y = 20;
  // x, y chỉ tồn tại trong scope này
})();
```

---

## **Phần 5: DOM & Events**

### **Q17: Event Bubbling vs Event Capturing**

**Trả lời:**
- **Event Bubbling**: Event lan truyền từ element con lên element cha
- **Event Capturing**: Event lan truyền từ element cha xuống element con
- **Hoạt động**: DOM events có 3 phases: Capturing → Target → Bubbling
- **Ưu điểm**: Event delegation, flexible event handling
- **Nhược điểm**: Có thể gây unexpected behavior nếu không hiểu rõ

**Code Example:**
```typescript
// HTML Structure
// <div id="parent">
//   <div id="child">
//     <button id="button">Click me</button>
//   </div>
// </div>

// Event Bubbling (default)
document.getElementById('button')?.addEventListener('click', (e: Event) => {
  console.log('Button clicked (bubbling)');
});

document.getElementById('child')?.addEventListener('click', (e: Event) => {
  console.log('Child clicked (bubbling)');
});

document.getElementById('parent')?.addEventListener('click', (e: Event) => {
  console.log('Parent clicked (bubbling)');
});

// Output khi click button: Button → Child → Parent

// Event Capturing
document.getElementById('button')?.addEventListener('click', (e: Event) => {
  console.log('Button clicked (capturing)');
}, true);  // true = capturing phase

document.getElementById('child')?.addEventListener('click', (e: Event) => {
  console.log('Child clicked (capturing)');
}, true);

document.getElementById('parent')?.addEventListener('click', (e: Event) => {
  console.log('Parent clicked (capturing)');
}, true);

// Output khi click button: Parent → Child → Button

// Stop Propagation
document.getElementById('button')?.addEventListener('click', (e: Event) => {
  console.log('Button clicked');
  e.stopPropagation();  // Dừng event propagation
});

// Prevent Default
document.getElementById('link')?.addEventListener('click', (e: Event) => {
  e.preventDefault();  // Ngăn default behavior (navigate to URL)
  console.log('Link clicked but navigation prevented');
});
```

**Best Practices:**
- Sử dụng event delegation cho dynamic content
- Sử dụng stopPropagation khi cần
- Sử dụng preventDefault cho form submissions
- Hiểu rõ event phases

**Mistakes:**
```typescript
// ❌ Sai: Không hiểu event phases
document.getElementById('parent')?.addEventListener('click', (e: Event) => {
  console.log('Parent clicked');
}, true);  // Capturing phase

document.getElementById('child')?.addEventListener('click', (e: Event) => {
  console.log('Child clicked');
});  // Bubbling phase (default)

// Output: Parent → Child (không phải Child → Parent)

// ✅ Đúng: Hiểu rõ event phases
document.getElementById('parent')?.addEventListener('click', (e: Event) => {
  console.log('Parent clicked (capturing)');
}, true);

document.getElementById('child')?.addEventListener('click', (e: Event) => {
  console.log('Child clicked (bubbling)');
}, false);  // Explicitly set to bubbling
```

---

### **Q18: Event Delegation**

**Trả lời:**
- **Event Delegation**: Sử dụng event bubbling để handle events trên parent element
- **Hoạt động**: Thay vì attach event listener cho từng child, attach cho parent
- **Ưu điểm**: Performance tốt hơn, handle dynamic content, ít memory usage
- **Nhược điểm**: Có thể phức tạp với nested events

**Code Example:**
```typescript
// HTML Structure
// <ul id="todoList">
//   <li class="todo-item" data-id="1">Task 1</li>
//   <li class="todo-item" data-id="2">Task 2</li>
// </ul>

// ❌ Không hiệu quả: Attach event cho từng item
const todoItems = document.querySelectorAll('.todo-item');
todoItems.forEach(item => {
  item.addEventListener('click', (e: Event) => {
    console.log('Todo clicked:', item.dataset.id);
  });
});

// ✅ Hiệu quả: Event delegation
document.getElementById('todoList')?.addEventListener('click', (e: Event) => {
  const target = e.target as HTMLElement;

  // Check if clicked element is a todo item
  if (target.classList.contains('todo-item')) {
    console.log('Todo clicked:', target.dataset.id);
  }
});

// Dynamic content với event delegation
function addTodoItem(text: string): void {
  const todoList = document.getElementById('todoList');
  const newItem = document.createElement('li');
  newItem.className = 'todo-item';
  newItem.dataset.id = Date.now().toString();
  newItem.textContent = text;
  todoList?.appendChild(newItem);

  // Không cần attach event listener - event delegation sẽ handle
}

// Complex event delegation
document.getElementById('todoList')?.addEventListener('click', (e: Event) => {
  const target = e.target as HTMLElement;

  if (target.classList.contains('todo-item')) {
    console.log('Todo clicked:', target.dataset.id);
  } else if (target.classList.contains('delete-btn')) {
    const todoItem = target.closest('.todo-item');
    console.log('Delete clicked for:', todoItem?.dataset.id);
  } else if (target.classList.contains('edit-btn')) {
    const todoItem = target.closest('.todo-item');
    console.log('Edit clicked for:', todoItem?.dataset.id);
  }
});
```

**Best Practices:**
- Sử dụng event delegation cho dynamic content
- Sử dụng closest() để find parent elements
- Sử dụng dataset cho data attributes
- Sử dụng proper event target checking

**Mistakes:**
```typescript
// ❌ Sai: Không check event target
document.getElementById('todoList')?.addEventListener('click', (e: Event) => {
  console.log('List clicked');  // Fires for any click in list
});

// ✅ Đúng: Check event target
document.getElementById('todoList')?.addEventListener('click', (e: Event) => {
  const target = e.target as HTMLElement;
  if (target.classList.contains('todo-item')) {
    console.log('Todo clicked');
  }
});
```

---

### **Q19: currentTarget vs target**

**Trả lời:**
- **target**: Element thực sự được click (có thể là child element)
- **currentTarget**: Element có event listener (luôn là element được attach listener)
- **Hoạt động**: Trong event delegation, target và currentTarget thường khác nhau
- **Ưu điểm**: Flexible event handling, precise event targeting
- **Nhược điểm**: Có thể gây confusion nếu không hiểu rõ

**Code Example:**
```typescript
// HTML Structure
// <div id="parent">
//   <button id="child">Click me</button>
// </div>

// Event listener trên parent
document.getElementById('parent')?.addEventListener('click', (e: Event) => {
  console.log('target:', e.target);           // <button id="child">
  console.log('currentTarget:', e.currentTarget); // <div id="parent">

  // target = element được click (button)
  // currentTarget = element có listener (div)
});

// Practical example với event delegation
document.getElementById('todoList')?.addEventListener('click', (e: Event) => {
  const target = e.target as HTMLElement;
  const currentTarget = e.currentTarget as HTMLElement;

  console.log('Clicked element:', target.tagName);        // LI, BUTTON, SPAN, etc.
  console.log('Listener element:', currentTarget.tagName); // UL

  // Find the actual todo item
  const todoItem = target.closest('.todo-item');
  if (todoItem) {
    console.log('Todo ID:', todoItem.dataset.id);
  }
});

// Nested elements example
// <div class="card">
//   <div class="card-header">
//     <h3>Title</h3>
//   </div>
//   <div class="card-body">
//     <p>Content</p>
//   </div>
// </div>

document.querySelectorAll('.card').forEach(card => {
  card.addEventListener('click', (e: Event) => {
    const target = e.target as HTMLElement;
    const currentTarget = e.currentTarget as HTMLElement;

    console.log('Clicked:', target.tagName);     // H3, P, DIV, etc.
    console.log('Card:', currentTarget.className); // card

    // Handle different clicks
    if (target.tagName === 'H3') {
      console.log('Header clicked');
    } else if (target.tagName === 'P') {
      console.log('Content clicked');
    }
  });
});
```

**Best Practices:**
- Sử dụng target để identify clicked element
- Sử dụng currentTarget để access listener element
- Sử dụng closest() để find parent elements
- Hiểu rõ sự khác biệt giữa target và currentTarget

**Mistakes:**
```typescript
// ❌ Sai: Sử dụng target thay vì currentTarget
document.getElementById('parent')?.addEventListener('click', (e: Event) => {
  const target = e.target as HTMLElement;
  console.log(target.id);  // Có thể là child element ID
});

// ✅ Đúng: Sử dụng currentTarget
document.getElementById('parent')?.addEventListener('click', (e: Event) => {
  const currentTarget = e.currentTarget as HTMLElement;
  console.log(currentTarget.id);  // Luôn là parent element ID
});
```

---

### **Q20: DOM API & Query Methods**

**Trả lời:**
- **DOM API**: Các methods để manipulate DOM elements
- **Query Methods**: Các methods để select elements từ DOM
- **Hoạt động**: getElementById, querySelector, getElementsByClassName, etc.
- **Ưu điểm**: Flexible element selection, powerful manipulation
- **Nhược điểm**: Có thể chậm với large DOM, cần hiểu rõ performance

**Code Example:**
```typescript
// Query Methods
// getElementById - trả về single element
const element = document.getElementById('myId');
if (element) {
  element.textContent = 'Hello World';
}

// querySelector - trả về first matching element
const firstDiv = document.querySelector('div');
const firstClass = document.querySelector('.my-class');
const firstId = document.querySelector('#my-id');

// querySelectorAll - trả về NodeList
const allDivs = document.querySelectorAll('div');
const allClasses = document.querySelectorAll('.my-class');

// getElementsByClassName - trả về HTMLCollection
const elementsByClass = document.getElementsByClassName('my-class');

// getElementsByTagName - trả về HTMLCollection
const elementsByTag = document.getElementsByTagName('div');

// DOM Manipulation
const div = document.createElement('div');
div.textContent = 'New element';
div.className = 'my-class';
div.id = 'new-id';

// Append to DOM
document.body.appendChild(div);

// Insert before
const existingElement = document.getElementById('existing');
existingElement?.parentNode?.insertBefore(div, existingElement);

// Remove element
div.remove();

// Update attributes
div.setAttribute('data-id', '123');
div.getAttribute('data-id'); // '123'
div.removeAttribute('data-id');

// Update classes
div.classList.add('new-class');
div.classList.remove('old-class');
div.classList.toggle('active');
div.classList.contains('active'); // true/false

// Update styles
div.style.color = 'red';
div.style.backgroundColor = 'blue';
div.style.display = 'none';

// Update content
div.textContent = 'Text content';
div.innerHTML = '<span>HTML content</span>';
div.innerText = 'Text only (no HTML)';

// Event handling
div.addEventListener('click', (e: Event) => {
  console.log('Div clicked');
});

// Remove event listener
const clickHandler = (e: Event) => console.log('Clicked');
div.addEventListener('click', clickHandler);
div.removeEventListener('click', clickHandler);
```

**Best Practices:**
- Sử dụng querySelector cho modern development
- Sử dụng getElementById cho single elements
- Sử dụng addEventListener thay vì onclick
- Sử dụng proper error handling

**Mistakes:**
```typescript
// ❌ Sai: Không check null
const element = document.getElementById('myId');
element.textContent = 'Hello';  // Error nếu element null

// ✅ Đúng: Check null
const element = document.getElementById('myId');
if (element) {
  element.textContent = 'Hello';
}

// ❌ Sai: Sử dụng innerHTML với user input
const userInput = '<script>alert("XSS")</script>';
div.innerHTML = userInput;  // XSS vulnerability

// ✅ Đúng: Sử dụng textContent
div.textContent = userInput;  // Safe
```

---

## **Phần 6: Type Checking & Operators**

### **Q21: Falsy/Truthy Values**

**Trả lời:**
- **Falsy Values**: Các giá trị được coi là false trong boolean context
- **Truthy Values**: Các giá trị được coi là true trong boolean context
- **Hoạt động**: JavaScript tự động convert values sang boolean khi cần
- **Ưu điểm**: Flexible type coercion, concise code
- **Nhược điểm**: Có thể gây confusion, bugs khó debug

**Code Example:**
```typescript
// Falsy Values
console.log(Boolean(false));     // false
console.log(Boolean(0));         // false
console.log(Boolean(-0));        // false
console.log(Boolean(0n));        // false (BigInt)
console.log(Boolean(''));        // false (empty string)
console.log(Boolean(null));      // false
console.log(Boolean(undefined)); // false
console.log(Boolean(NaN));       // false

// Truthy Values
console.log(Boolean(true));      // true
console.log(Boolean(1));         // true
console.log(Boolean(-1));        // true
console.log(Boolean('hello'));   // true
console.log(Boolean('0'));       // true (string)
console.log(Boolean('false'));   // true (string)
console.log(Boolean([]));        // true (empty array)
console.log(Boolean({}));        // true (empty object)
console.log(Boolean(function(){})); // true (function)

// Practical usage
function greet(name: string | null | undefined): string {
  if (name) {  // Truthy check
    return `Hello ${name}`;
  }
  return 'Hello Guest';
}

greet('John');    // "Hello John"
greet('');        // "Hello Guest" (empty string is falsy)
greet(null);      // "Hello Guest"
greet(undefined); // "Hello Guest"

// Array filtering
const numbers = [0, 1, 2, 3, 4, 5];
const truthyNumbers = numbers.filter(Boolean); // [1, 2, 3, 4, 5]

// Default values
function getValue(value: string | null | undefined): string {
  return value || 'default';  // Falsy values get 'default'
}

getValue('hello');  // "hello"
getValue('');       // "default"
getValue(null);     // "default"
getValue(undefined); // "default"

// Short-circuit evaluation
const user = null;
const name = user && user.name;  // null (short-circuit)
const age = user?.age || 0;      // 0 (nullish coalescing)
```

**Best Practices:**
- Sử dụng explicit boolean conversion khi cần
- Sử dụng nullish coalescing (??) thay vì || cho default values
- Sử dụng optional chaining (?.) cho safe property access
- Hiểu rõ falsy/truthy values

**Mistakes:**
```typescript
// ❌ Sai: Sử dụng || cho default values
function getValue(value: string | null | undefined): string {
  return value || 'default';  // '' sẽ trả về 'default'
}

// ✅ Đúng: Sử dụng ?? cho default values
function getValue(value: string | null | undefined): string {
  return value ?? 'default';  // '' sẽ trả về ''
}

// ❌ Sai: Không hiểu array truthy
const arr = [];
if (arr) {
  console.log('Array exists');  // True, nhưng array rỗng
}

// ✅ Đúng: Check array length
if (arr.length > 0) {
  console.log('Array has items');
}
```

---

### **Q22: == vs === (Type Coercion)**

**Trả lời:**
- **== (Loose Equality)**: So sánh với type coercion, convert types trước khi so sánh
- **=== (Strict Equality)**: So sánh không có type coercion, so sánh cả value và type
- **Hoạt động**: == có thể gây unexpected results do type coercion
- **Ưu điểm**: === predictable hơn, == flexible hơn
- **Nhược điểm**: == có thể gây bugs, === strict hơn

**Code Example:**
```typescript
// == vs === Examples
console.log(5 == '5');   // true (type coercion)
console.log(5 === '5');  // false (no type coercion)

console.log(0 == false); // true (0 is falsy)
console.log(0 === false); // false (different types)

console.log('' == false); // true (both falsy)
console.log('' === false); // false (different types)

console.log(null == undefined); // true (special case)
console.log(null === undefined); // false (different types)

console.log(NaN == NaN); // false (NaN is never equal to anything)
console.log(NaN === NaN); // false (NaN is never equal to anything)

// Type coercion rules
console.log('5' - 3);    // 2 (string to number)
console.log('5' + 3);    // '53' (number to string)
console.log('5' * 3);    // 15 (string to number)
console.log('5' / 3);    // 1.666... (string to number)

// Object comparison
const obj1 = { name: 'John' };
const obj2 = { name: 'John' };
const obj3 = obj1;

console.log(obj1 == obj2);  // false (different references)
console.log(obj1 === obj2); // false (different references)
console.log(obj1 == obj3);  // true (same reference)
console.log(obj1 === obj3); // true (same reference)

// Array comparison
const arr1 = [1, 2, 3];
const arr2 = [1, 2, 3];
const arr3 = arr1;

console.log(arr1 == arr2);  // false (different references)
console.log(arr1 === arr2); // false (different references)
console.log(arr1 == arr3);  // true (same reference)
console.log(arr1 === arr3); // true (same reference)

// Practical examples
function checkValue(value: any): void {
  if (value == null) {  // Check for both null and undefined
    console.log('Value is null or undefined');
  }

  if (value === null) {  // Check only for null
    console.log('Value is null');
  }

  if (value === undefined) {  // Check only for undefined
    console.log('Value is undefined');
  }
}
```

**Best Practices:**
- Sử dụng === mặc định
- Sử dụng == chỉ khi cần type coercion
- Sử dụng == null để check cả null và undefined
- Sử dụng Object.is() cho special cases

**Mistakes:**
```typescript
// ❌ Sai: Sử dụng == không cẩn thận
if (user.age == '25') {  // Có thể gây confusion
  console.log('User is 25');
}

// ✅ Đúng: Sử dụng ===
if (user.age === 25) {  // Rõ ràng hơn
  console.log('User is 25');
}

// ❌ Sai: Không hiểu type coercion
console.log([] == false); // true (array to string to number)
console.log([] === false); // false

// ✅ Đúng: Hiểu rõ type coercion
console.log([] == false); // true (coercion: [] -> '' -> 0 -> false)
console.log([] === false); // false (no coercion)
```

---

### **Q23: null vs undefined**

**Trả lời:**
- **null**: Intentional absence of value, được assign explicitly
- **undefined**: Unintentional absence of value, default value của uninitialized variables
- **Hoạt động**: null là object type, undefined là undefined type
- **Ưu điểm**: Rõ ràng về intent, có thể distinguish giữa intentional và unintentional
- **Nhược điểm**: Có thể gây confusion, cần handle cả hai cases

**Code Example:**
```typescript
// null vs undefined
let x: number | null = null;        // Explicitly set to null
let y: number;                      // undefined (uninitialized)
let z: number | undefined = undefined; // Explicitly set to undefined

console.log(typeof null);      // "object" (historical bug)
console.log(typeof undefined); // "undefined"

// null examples
function findUser(id: number): User | null {
  // Return null when user not found
  return null;
}

const user = findUser(123);
if (user === null) {
  console.log('User not found');
}

// undefined examples
function getProperty(obj: any, key: string): any {
  return obj[key]; // Returns undefined if key doesn't exist
}

const obj = { name: 'John' };
const age = getProperty(obj, 'age'); // undefined

// Default parameters
function greet(name: string = 'Guest'): string {
  return `Hello ${name}`;
}

greet();        // "Hello Guest" (default parameter)
greet('John');  // "Hello John"

// Optional properties
interface User {
  name: string;
  age?: number;  // Optional property (can be undefined)
}

const user1: User = { name: 'John' };           // age is undefined
const user2: User = { name: 'Jane', age: 25 }; // age is 25

// Nullish coalescing
function getValue(value: string | null | undefined): string {
  return value ?? 'default';  // Only null and undefined get 'default'
}

getValue('hello');  // "hello"
getValue('');       // "" (empty string is not nullish)
getValue(null);     // "default"
getValue(undefined); // "default"

// Optional chaining
const user = { name: 'John', address: { city: 'HCM' } };
const city = user?.address?.city;        // "HCM"
const country = user?.address?.country;  // undefined

// Array methods
const numbers = [1, 2, 3, 4, 5];
const found = numbers.find(n => n > 10); // undefined (not found)
const index = numbers.findIndex(n => n > 10); // -1 (not found)
```

**Best Practices:**
- Sử dụng null cho intentional absence
- Sử dụng undefined cho unintentional absence
- Sử dụng nullish coalescing (??) cho default values
- Sử dụng optional chaining (?.) cho safe access

**Mistakes:**
```typescript
// ❌ Sai: Không distinguish null và undefined
function processValue(value: any): void {
  if (value == null) {  // Check both null and undefined
    console.log('Value is null or undefined');
  }
}

// ✅ Đúng: Distinguish null và undefined
function processValue(value: any): void {
  if (value === null) {
    console.log('Value is null');
  } else if (value === undefined) {
    console.log('Value is undefined');
  }
}

// ❌ Sai: Sử dụng || cho default values
function getValue(value: string | null | undefined): string {
  return value || 'default';  // '' sẽ trả về 'default'
}

// ✅ Đúng: Sử dụng ?? cho default values
function getValue(value: string | null | undefined): string {
  return value ?? 'default';  // '' sẽ trả về ''
}
```

---

### **Q24: typeof Operator**

**Trả lời:**
- **typeof**: Operator trả về string mô tả type của operand
- **Hoạt động**: Trả về primitive types, có một số special cases
- **Ưu điểm**: Type checking, runtime type detection
- **Nhược điểm**: Có một số quirks, không perfect cho all cases

**Code Example:**
```typescript
// Basic typeof examples
console.log(typeof 42);           // "number"
console.log(typeof 'hello');      // "string"
console.log(typeof true);         // "boolean"
console.log(typeof undefined);    // "undefined"
console.log(typeof Symbol('id')); // "symbol"
console.log(typeof 123n);         // "bigint"

// Special cases
console.log(typeof null);         // "object" (historical bug)
console.log(typeof []);           // "object"
console.log(typeof {});           // "object"
console.log(typeof function(){}); // "function"

// Type checking functions
function isString(value: any): value is string {
  return typeof value === 'string';
}

function isNumber(value: any): value is number {
  return typeof value === 'number' && !isNaN(value);
}

function isBoolean(value: any): value is boolean {
  return typeof value === 'boolean';
}

function isUndefined(value: any): value is undefined {
  return typeof value === 'undefined';
}

function isFunction(value: any): value is Function {
  return typeof value === 'function';
}

// Array and object checking
function isArray(value: any): value is any[] {
  return Array.isArray(value);
}

function isObject(value: any): value is object {
  return typeof value === 'object' && value !== null;
}

function isNull(value: any): value is null {
  return value === null;
}

// Practical usage
function processValue(value: any): void {
  switch (typeof value) {
    case 'string':
      console.log('String:', value.toUpperCase());
      break;
    case 'number':
      console.log('Number:', value * 2);
      break;
    case 'boolean':
      console.log('Boolean:', !value);
      break;
    case 'undefined':
      console.log('Undefined value');
      break;
    case 'object':
      if (value === null) {
        console.log('Null value');
      } else if (Array.isArray(value)) {
        console.log('Array:', value.length);
      } else {
        console.log('Object:', Object.keys(value));
      }
      break;
    case 'function':
      console.log('Function');
      break;
    default:
      console.log('Other type:', typeof value);
  }
}

// Type guards
function isStringOrNumber(value: any): value is string | number {
  return typeof value === 'string' || typeof value === 'number';
}

function processStringOrNumber(value: any): void {
  if (isStringOrNumber(value)) {
    // TypeScript knows value is string | number
    console.log(value.toString());
  }
}
```

**Best Practices:**
- Sử dụng typeof cho primitive types
- Sử dụng Array.isArray() cho arrays
- Sử dụng === null cho null checking
- Sử dụng type guards cho complex types

**Mistakes:**
```typescript
// ❌ Sai: Không hiểu typeof quirks
console.log(typeof null);  // "object" (not "null")

// ✅ Đúng: Sử dụng proper null checking
console.log(value === null);  // true/false

// ❌ Sai: Không check array properly
function isArray(value: any): boolean {
  return typeof value === 'object' && value !== null;  // Wrong
}

// ✅ Đúng: Sử dụng Array.isArray()
function isArray(value: any): boolean {
  return Array.isArray(value);  // Correct
}
```

---

### **Q25: || && ?? và Optional Chaining**

**Trả lời:**
- **|| (Logical OR)**: Trả về first truthy value hoặc last value
- **&& (Logical AND)**: Trả về first falsy value hoặc last value
- **?? (Nullish Coalescing)**: Trả về right operand khi left operand is nullish
- **?. (Optional Chaining)**: Safe property access, trả về undefined nếu property không tồn tại
- **Ưu điểm**: Concise code, safe access, flexible defaults
- **Nhược điểm**: Có thể gây confusion nếu không hiểu rõ

**Code Example:**
```typescript
// Logical OR (||)
const name = user.name || 'Guest';        // 'Guest' if user.name is falsy
const age = user.age || 0;                // 0 if user.age is falsy
const city = user.city || 'Unknown';      // 'Unknown' if user.city is falsy

// Logical AND (&&)
const isAdmin = user.role === 'admin' && user.isActive;  // true if both true
const message = user.isLoggedIn && 'Welcome back!';      // 'Welcome back!' or false
const count = items && items.length;                     // items.length or false

// Nullish Coalescing (??)
const name = user.name ?? 'Guest';        // 'Guest' only if user.name is null/undefined
const age = user.age ?? 0;                // 0 only if user.age is null/undefined
const city = user.city ?? 'Unknown';      // 'Unknown' only if user.city is null/undefined

// Difference between || and ??
const value1 = '' || 'default';           // 'default' (empty string is falsy)
const value2 = '' ?? 'default';           // '' (empty string is not nullish)

const value3 = 0 || 'default';            // 'default' (0 is falsy)
const value4 = 0 ?? 'default';            // 0 (0 is not nullish)

const value5 = false || 'default';        // 'default' (false is falsy)
const value6 = false ?? 'default';        // false (false is not nullish)

// Optional Chaining (?.)
const user = { name: 'John', address: { city: 'HCM' } };
const city = user?.address?.city;         // 'HCM'
const country = user?.address?.country;   // undefined (safe access)

// Method calls
const result = user?.getName?.();         // Safe method call
const length = user?.name?.length;        // Safe property access

// Array access
const firstItem = items?.[0];             // Safe array access
const item = items?.[index];              // Safe array access with variable

// Function calls
const callback = user?.onClick;
callback?.();                             // Safe function call

// Practical examples
function getUserInfo(user: any): string {
  const name = user?.name ?? 'Unknown';
  const age = user?.age ?? 0;
  const city = user?.address?.city ?? 'Unknown';

  return `${name}, ${age} years old, from ${city}`;
}

// Chaining operators
const value = user?.preferences?.theme ?? 'light';
const isEnabled = user?.settings?.notifications?.email ?? false;

// Error handling
function processUser(user: any): void {
  try {
    const name = user?.name ?? 'Guest';
    const email = user?.contact?.email ?? 'no-email@example.com';

    console.log(`Processing user: ${name} (${email})`);
  } catch (error) {
    console.error('Error processing user:', error);
  }
}
```

**Best Practices:**
- Sử dụng ?? cho default values thay vì ||
- Sử dụng ?. cho safe property access
- Sử dụng && cho conditional execution
- Sử dụng || cho fallback values

**Mistakes:**
```typescript
// ❌ Sai: Sử dụng || cho default values
const theme = user.preferences?.theme || 'light';  // '' sẽ trả về 'light'

// ✅ Đúng: Sử dụng ?? cho default values
const theme = user.preferences?.theme ?? 'light';  // '' sẽ trả về ''

// ❌ Sai: Không sử dụng optional chaining
const city = user.address.city;  // Error nếu address is null

// ✅ Đúng: Sử dụng optional chaining
const city = user.address?.city;  // Safe access

// ❌ Sai: Không hiểu operator precedence
const result = user?.name || 'Guest' ?? 'Default';  // Syntax error

// ✅ Đúng: Sử dụng parentheses
const result = (user?.name || 'Guest') ?? 'Default';
```

---

## **Phần 7: Asynchronous JavaScript**

### **Q26: Async/Await vs Promises vs Callbacks**

**Trả lời:**
- **Callbacks**: Functions được pass vào other functions để execute sau
- **Promises**: Objects đại diện cho eventual completion/failure của async operation
- **Async/Await**: Syntactic sugar cho Promises, làm code dễ đọc hơn
- **Ưu điểm**: Async/await dễ đọc nhất, Promises flexible, Callbacks simple
- **Nhược điểm**: Callbacks có thể gây callback hell, Promises complex, Async/await cần modern JS

**Code Example:**
```typescript
// Callbacks
function fetchData(callback: (error: Error | null, data?: any) => void): void {
  setTimeout(() => {
    const data = { message: 'Hello World' };
    callback(null, data);
  }, 1000);
}

fetchData((error, data) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log('Data:', data);
  }
});

// Promises
function fetchDataPromise(): Promise<any> {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const data = { message: 'Hello World' };
      resolve(data);
    }, 1000);
  });
}

fetchDataPromise()
  .then(data => console.log('Data:', data))
  .catch(error => console.error('Error:', error));

// Async/Await
async function fetchDataAsync(): Promise<any> {
  try {
    const data = await fetchDataPromise();
    console.log('Data:', data);
    return data;
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
}
```

**Best Practices:**
- Sử dụng async/await cho modern code
- Sử dụng proper error handling
- Tránh callback hell
- Sử dụng TypeScript cho type safety

---

### **Q27: Promise.all, Promise.any, Promise.race**

**Trả lời:**
- **Promise.all**: Đợi tất cả promises resolve, reject nếu có 1 promise reject
- **Promise.any**: Resolve khi có 1 promise resolve, reject nếu tất cả reject
- **Promise.race**: Resolve/reject với promise đầu tiên hoàn thành
- **Ưu điểm**: Flexible promise handling, parallel operations
- **Nhược điểm**: Cần hiểu rõ behavior của từng method

**Code Example:**
```typescript
// Promise.all - tất cả phải thành công
async function fetchAllData(): Promise<void> {
  const promises = [
    fetch('/api/users'),
    fetch('/api/posts'),
    fetch('/api/comments')
  ];

  try {
    const [users, posts, comments] = await Promise.all(promises);
    console.log('All data fetched successfully');
  } catch (error) {
    console.error('One or more requests failed:', error);
  }
}

// Promise.any - 1 thành công là đủ
async function fetchFromAnySource(): Promise<void> {
  const promises = [
    fetch('/api/primary'),
    fetch('/api/backup1'),
    fetch('/api/backup2')
  ];

  try {
    const response = await Promise.any(promises);
    console.log('Data fetched from:', response.url);
  } catch (error) {
    console.error('All sources failed:', error);
  }
}

// Promise.race - ai nhanh nhất
async function fetchWithTimeout(): Promise<void> {
  const dataPromise = fetch('/api/data');
  const timeoutPromise = new Promise((_, reject) => {
    setTimeout(() => reject(new Error('Timeout')), 5000);
  });

  try {
    const result = await Promise.race([dataPromise, timeoutPromise]);
    console.log('Data fetched:', result);
  } catch (error) {
    console.error('Request failed or timed out:', error);
  }
}
```

**Best Practices:**
- Sử dụng Promise.all cho parallel operations
- Sử dụng Promise.any cho fallback mechanisms
- Sử dụng Promise.race cho timeout handling
- Sử dụng proper error handling

---

### **Q28: Axios Interceptors**

**Trả lời:**
- **Interceptors**: Functions được execute trước/sau requests/responses
- **Request Interceptors**: Modify requests trước khi gửi
- **Response Interceptors**: Handle responses và errors
- **Ưu điểm**: Centralized request/response handling, authentication, error handling
- **Nhược điểm**: Có thể gây side effects nếu không cẩn thận

**Code Example:**
```typescript
import axios, { AxiosRequestConfig, AxiosResponse, AxiosError } from 'axios';

// Request interceptor
axios.interceptors.request.use(
  (config: AxiosRequestConfig) => {
    // Add auth token
    const token = localStorage.getItem('authToken');
    if (token) {
      config.headers = {
        ...config.headers,
        Authorization: `Bearer ${token}`
      };
    }

    console.log('Request:', config);
    return config;
  },
  (error: AxiosError) => {
    console.error('Request error:', error);
    return Promise.reject(error);
  }
);

// Response interceptor
axios.interceptors.response.use(
  (response: AxiosResponse) => {
    console.log('Response:', response);
    return response;
  },
  (error: AxiosError) => {
    // Handle common errors
    if (error.response?.status === 401) {
      localStorage.removeItem('authToken');
      window.location.href = '/login';
    }

    return Promise.reject(error);
  }
);
```

**Best Practices:**
- Sử dụng interceptors cho common functionality
- Sử dụng proper error handling
- Sử dụng TypeScript cho type safety
- Sử dụng cleanup functions

---

## **Phần 8: Object Manipulation**

### **Q29: Remove Property from Object**

**Trả lời:**
- **delete operator**: Xóa property từ object
- **Destructuring + Rest**: Tạo object mới không có property
- **Object.assign**: Copy object và xóa property
- **Ưu điểm**: Destructuring immutable, delete mutable
- **Nhược điểm**: delete có thể gây performance issues

**Code Example:**
```typescript
// delete operator
const user = { name: 'John', age: 25, city: 'HCM' };
delete user.age;
console.log(user); // { name: 'John', city: 'HCM' }

// Destructuring + Rest operator
const user = { name: 'John', age: 25, city: 'HCM' };
const { age, ...userWithoutAge } = user;
console.log(userWithoutAge); // { name: 'John', city: 'HCM' }

// Function to remove property
function removeProperty<T extends object, K extends keyof T>(
  obj: T,
  key: K
): Omit<T, K> {
  const { [key]: removed, ...rest } = obj;
  return rest;
}

const user = { name: 'John', age: 25, city: 'HCM' };
const userWithoutAge = removeProperty(user, 'age');
console.log(userWithoutAge); // { name: 'John', city: 'HCM' }
```

**Best Practices:**
- Sử dụng destructuring cho immutable operations
- Sử dụng delete cho mutable operations
- Sử dụng TypeScript cho type safety
- Sử dụng utility functions cho complex operations

---

### **Q30: Compare Objects**

**Trả lời:**
- **Shallow Comparison**: So sánh references và primitive values
- **Deep Comparison**: So sánh tất cả nested properties
- **Hoạt động**: Objects được so sánh bằng reference, không phải value
- **Ưu điểm**: Deep comparison chính xác, shallow comparison nhanh
- **Nhược điểm**: Deep comparison chậm, shallow comparison không chính xác

**Code Example:**
```typescript
// Shallow comparison
const obj1 = { name: 'John', age: 25 };
const obj2 = { name: 'John', age: 25 };
const obj3 = obj1;

console.log(obj1 === obj2); // false (different references)
console.log(obj1 === obj3); // true (same reference)

// Deep comparison function
function deepEqual(obj1: any, obj2: any): boolean {
  if (obj1 === obj2) return true;

  if (obj1 == null || obj2 == null) return false;

  if (typeof obj1 !== typeof obj2) return false;

  if (typeof obj1 !== 'object') return obj1 === obj2;

  if (Array.isArray(obj1) !== Array.isArray(obj2)) return false;

  const keys1 = Object.keys(obj1);
  const keys2 = Object.keys(obj2);

  if (keys1.length !== keys2.length) return false;

  for (let key of keys1) {
    if (!keys2.includes(key)) return false;
    if (!deepEqual(obj1[key], obj2[key])) return false;
  }

  return true;
}

// Usage
const obj1 = { name: 'John', age: 25, address: { city: 'HCM' } };
const obj2 = { name: 'John', age: 25, address: { city: 'HCM' } };

console.log(deepEqual(obj1, obj2)); // true
```

**Best Practices:**
- Sử dụng deep comparison cho object comparison
- Sử dụng shallow comparison cho performance
- Sử dụng libraries như Lodash cho complex comparisons
- Sử dụng TypeScript cho type safety

---

### **Q31: Combine Strings**

**Trả lời:**
- **String Concatenation**: Sử dụng + operator
- **Template Literals**: Sử dụng backticks và ${}
- **Array.join()**: Sử dụng array methods
- **Ưu điểm**: Template literals dễ đọc nhất, + operator simple
- **Nhược điểm**: + operator có thể chậm với nhiều strings

**Code Example:**
```typescript
// String concatenation
const firstName = 'John';
const lastName = 'Doe';
const fullName = firstName + ' ' + lastName;
console.log(fullName); // "John Doe"

// Template literals
const firstName = 'John';
const lastName = 'Doe';
const age = 25;
const fullName = `${firstName} ${lastName}`;
const greeting = `Hello, I'm ${fullName} and I'm ${age} years old`;
console.log(greeting); // "Hello, I'm John Doe and I'm 25 years old"

// Array.join()
const words = ['Hello', 'World', 'JavaScript'];
const sentence = words.join(' ');
console.log(sentence); // "Hello World JavaScript"

// Multi-line strings
const multiLine = `
  This is a
  multi-line
  string
`;

// Conditional strings
const isActive = true;
const status = `User is ${isActive ? 'active' : 'inactive'}`;
```

**Best Practices:**
- Sử dụng template literals cho complex strings
- Sử dụng + operator cho simple concatenation
- Sử dụng array.join() cho multiple strings
- Sử dụng proper escaping

---

## **Phần 9: Advanced Topics**

### **Q32: Functional Programming - Pure Functions, Currying & HOF**

**Trả lời:**
- **🔥 Pure Functions**: Functions không có side effects, same input → same output (cùng input → cùng output)
- **🎯 Currying**: Transform function với multiple arguments thành sequence of functions (chuyển đổi hàm nhiều tham số thành chuỗi hàm)
- **⚡ Higher-Order Functions (HOF)**: Functions nhận functions làm arguments hoặc return functions (hàm nhận hàm làm tham số hoặc trả về hàm)
- **✅ Ưu điểm**: Predictable (dự đoán được), testable (dễ test), composable (có thể kết hợp), reusable (tái sử dụng)
- **⚠️ Nhược điểm**: Có thể phức tạp cho beginners, performance overhead nhẹ

**Code Example:**
```typescript
// 🔥 Pure Functions (Hàm thuần túy)
function add(a: number, b: number): number {
  return a + b; // ✅ Không có side effects, predictable
}

function multiply(a: number, b: number): number {
  return a * b; // ✅ Pure function - cùng input luôn cho cùng output
}

// ❌ Impure function (hàm không thuần túy - có side effects)
let counter = 0;
function increment(): number {
  counter++; // ❌ Side effect - thay đổi state bên ngoài
  return counter;
}

// 🎯 Currying (Currying - chuyển đổi hàm)
// Cách 1: Function declaration
function add(a: number) {
  return function(b: number) {
    return a + b;
  };
}

const add5 = add(5);        // Tạo function mới với a = 5
console.log(add5(3));       // 8 - gọi function với b = 3

// Cách 2: Arrow function currying (ngắn gọn hơn)
const add = (a: number) => (b: number) => a + b;
const add5 = add(5);
console.log(add5(3));       // 8

// Currying với nhiều tham số
const multiply = (a: number) => (b: number) => (c: number) => a * b * c;
const multiplyBy2 = multiply(2);           // a = 2
const multiplyBy2And3 = multiplyBy2(3);    // b = 3
console.log(multiplyBy2And3(4));           // 2 * 3 * 4 = 24

// ⚡ Higher-Order Functions (HOF - Hàm bậc cao)
// HOF nhận function làm argument
function withLogging<T extends (...args: any[]) => any>(
  fn: T
): (...args: Parameters<T>) => ReturnType<T> {
  return (...args: Parameters<T>) => {
    console.log('🔍 Function called with:', args);
    const result = fn(...args);
    console.log('✅ Function returned:', result);
    return result;
  };
}

const add = (a: number, b: number): number => a + b;
const loggedAdd = withLogging(add);
loggedAdd(5, 3); // Logs: Function called with: [5, 3], Function returned: 8

// HOF return function (hàm trả về hàm)
function createMultiplier(factor: number): (value: number) => number {
  return (value: number): number => value * factor;
}

const double = createMultiplier(2);    // Tạo function nhân đôi
const triple = createMultiplier(3);    // Tạo function nhân ba
console.log(double(5));                // 10
console.log(triple(5));                // 15

// 🔥 Array methods là HOF (các phương thức mảng là HOF)
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(x => x * 2);        // [2, 4, 6, 8, 10] - transform
const evens = numbers.filter(x => x % 2 === 0); // [2, 4] - filter
const sum = numbers.reduce((acc, x) => acc + x, 0); // 15 - accumulate

// 🎯 Function Composition (Kết hợp hàm)
function compose<T>(...fns: Array<(arg: T) => T>): (arg: T) => T {
  return (arg: T): T => fns.reduceRight((acc, fn) => fn(acc), arg);
}

const addOne = (x: number): number => x + 1;
const multiplyByTwo = (x: number): number => x * 2;
const square = (x: number): number => x * x;

const composed = compose(square, multiplyByTwo, addOne);
console.log(composed(3)); // ((3 + 1) * 2)² = 64

// 🔥 Practical Example: Data Processing Pipeline
const users = [
  { name: 'John', age: 25, active: true },
  { name: 'Jane', age: 30, active: false },
  { name: 'Bob', age: 35, active: true }
];

// Functional approach - dễ đọc và maintain
const activeUserNames = users
  .filter(user => user.active)           // Lọc user active
  .map(user => user.name.toUpperCase())  // Chuyển tên thành uppercase
  .sort();                               // Sắp xếp alphabetically

console.log(activeUserNames); // ['BOB', 'JOHN']
```

**🎯 Best Practices:**
- **✅ Sử dụng pure functions** khi có thể để code predictable và testable
- **✅ Sử dụng currying** cho function reuse và partial application
- **✅ Sử dụng HOF** cho abstraction và code reusability
- **✅ Sử dụng function composition** thay vì nested function calls
- **✅ Sử dụng array methods** (map, filter, reduce) thay vì loops

**❌ Common Mistakes:**
```typescript
// ❌ Sai: Không sử dụng HOF khi có thể
const numbers = [1, 2, 3, 4, 5];
const doubled = [];
for (let i = 0; i < numbers.length; i++) {
  doubled.push(numbers[i] * 2);
}

// ✅ Đúng: Sử dụng HOF
const doubled = numbers.map(x => x * 2);

// ❌ Sai: Impure function với side effects
let total = 0;
function addToTotal(value: number): number {
  total += value;  // Side effect
  return total;
}

// ✅ Đúng: Pure function
function add(a: number, b: number): number {
  return a + b;  // No side effects
}

// ❌ Sai: Không sử dụng currying khi cần reuse
function calculateTax(rate: number, amount: number): number {
  return amount * rate;
}
const tax1 = calculateTax(0.1, 1000);
const tax2 = calculateTax(0.1, 2000);  // Lặp lại rate

// ✅ Đúng: Sử dụng currying
const calculateTax = (rate: number) => (amount: number) => amount * rate;
const calculateVAT = calculateTax(0.1);  // Tạo function với rate cố định
const tax1 = calculateVAT(1000);
const tax2 = calculateVAT(2000);
```

---

### **Q33: Browser Rendering (Paint, Repaint, Reflow)**

**Trả lời:**
- **Paint**: Vẽ pixels lên screen
- **Repaint**: Vẽ lại elements với same layout
- **Reflow**: Recalculate layout và repaint
- **Hoạt động**: Reflow → Repaint → Composite
- **Ưu điểm**: Optimized rendering, smooth animations
- **Nhược điểm**: Reflow expensive, có thể gây performance issues

**Code Example:**
```typescript
// Reflow triggers
function triggerReflow(): void {
  const element = document.getElementById('myElement');
  if (element) {
    // These trigger reflow
    element.style.width = '200px';
    element.style.height = '100px';
    element.style.margin = '10px';
    element.style.padding = '5px';

    // Reading layout properties also triggers reflow
    const width = element.offsetWidth;
    const height = element.offsetHeight;
  }
}

// Optimized - batch DOM changes
function optimizedReflow(): void {
  const element = document.getElementById('myElement');
  if (element) {
    // Batch all changes
    element.style.cssText = 'width: 200px; height: 100px; margin: 10px; padding: 5px;';

    // Or use class
    element.className = 'new-style';
  }
}

// Use transform for animations (tránh reflow)
function animateWithTransform(): void {
  const element = document.getElementById('myElement');
  if (element) {
    // Transform doesn't trigger reflow
    element.style.transform = 'translateX(100px)';
    element.style.transition = 'transform 0.3s ease';
  }
}
```

**Best Practices:**
- Tránh reflow khi có thể
- Sử dụng transform cho animations
- Sử dụng requestAnimationFrame
- Batch DOM changes

---

### **Q34: Loop Performance**

**Trả lời:**
- **for loop**: Nhanh nhất, flexible
- **for...of**: Modern, readable, slower than for
- **forEach**: Functional style, slowest
- **for...in**: Cho objects, có thể chậm
- **Ưu điểm**: for loop nhanh nhất, for...of readable
- **Nhược điểm**: forEach chậm nhất, for...in có thể gây issues

**Code Example:**
```typescript
const numbers = [1, 2, 3, 4, 5];

// for loop - fastest
for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
}

// for...of - modern, readable
for (const number of numbers) {
  console.log(number);
}

// forEach - functional style
numbers.forEach(number => {
  console.log(number);
});

// Performance comparison
function performanceTest(): void {
  const largeArray = Array.from({ length: 1000000 }, (_, i) => i);

  // for loop
  console.time('for loop');
  for (let i = 0; i < largeArray.length; i++) {
    largeArray[i] * 2;
  }
  console.timeEnd('for loop');

  // for...of
  console.time('for...of');
  for (const item of largeArray) {
    item * 2;
  }
  console.timeEnd('for...of');

  // forEach
  console.time('forEach');
  largeArray.forEach(item => {
    item * 2;
  });
  console.timeEnd('forEach');
}

// for...in for objects
const obj = { a: 1, b: 2, c: 3 };
for (const key in obj) {
  console.log(key, obj[key]);
}
```

**Best Practices:**
- Sử dụng for loop cho performance
- Sử dụng for...of cho readability
- Sử dụng forEach cho functional style
- Cache array length trong for loops

---

### **Q35: Strict Mode**

**Trả lời:**
- **Strict Mode**: ES5 feature để catch common mistakes
- **Hoạt động**: Thêm restrictions và error throwing
- **Ưu điểm**: Catch errors early, prevent common mistakes
- **Nhược điểm**: Có thể break existing code

**Code Example:**
```typescript
// Enable strict mode
'use strict';

// Strict mode catches these errors:

// 1. Undeclared variables
// x = 10; // ReferenceError: x is not defined

// 2. Duplicate parameter names
// function test(a, a) { } // SyntaxError: Duplicate parameter name

// 3. Octal literals
// var x = 010; // SyntaxError: Octal literals are not allowed

// 4. this in functions
function test() {
  console.log(this); // undefined in strict mode
}

// 5. eval creates new scope
eval('var x = 10;');
// console.log(x); // ReferenceError: x is not defined

// 6. Cannot delete variables
var x = 10;
// delete x; // SyntaxError: Delete of an unqualified identifier

// 7. Function declarations in blocks
if (true) {
  // function test() { } // SyntaxError: Function declarations in blocks
}

// Benefits of strict mode
function strictModeExample(): void {
  'use strict';

  // More predictable behavior
  // Better error messages
  // Prevents common mistakes
  // Enables optimizations
}
```

**Best Practices:**
- Sử dụng strict mode trong production
- Sử dụng strict mode cho new projects
- Sử dụng proper error handling
- Sử dụng TypeScript cho additional safety

---

### **Q36: JavaScript Proxy**

**Trả lời:**
- **Proxy**: Object để intercept và customize operations
- **Hoạt động**: Wrap target object và intercept property access
- **Ưu điểm**: Powerful metaprogramming, validation, logging
- **Nhược điểm**: Performance overhead, complexity

**Code Example:**
```typescript
// Basic proxy
const target = { name: 'John', age: 25 };
const proxy = new Proxy(target, {
  get(target, property) {
    console.log(`Getting ${String(property)}`);
    return target[property as keyof typeof target];
  },
  set(target, property, value) {
    console.log(`Setting ${String(property)} to ${value}`);
    target[property as keyof typeof target] = value;
    return true;
  }
});

console.log(proxy.name); // Getting name, John
proxy.age = 26; // Setting age to 26

// Validation proxy
const userProxy = new Proxy({}, {
  set(target, property, value) {
    if (property === 'age' && (typeof value !== 'number' || value < 0)) {
      throw new Error('Age must be a positive number');
    }
    if (property === 'name' && typeof value !== 'string') {
      throw new Error('Name must be a string');
    }
    target[property as keyof typeof target] = value;
    return true;
  }
});

userProxy.name = 'John'; // OK
userProxy.age = 25; // OK
// userProxy.age = -5; // Error: Age must be a positive number

// Logging proxy
const loggingProxy = new Proxy({}, {
  get(target, property) {
    console.log(`Accessing property: ${String(property)}`);
    return target[property as keyof typeof target];
  },
  set(target, property, value) {
    console.log(`Setting property: ${String(property)} = ${value}`);
    target[property as keyof typeof target] = value;
    return true;
  }
});
```

**Best Practices:**
- Sử dụng proxy cho validation
- Sử dụng proxy cho logging
- Sử dụng proxy cho metaprogramming
- Sử dụng proper error handling

---


### **Q37: JavaScript Classes**

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

---

## **Phần 10: Advanced Functional Programming**


### **Q38: Polyfill & Transpiling**

**Trả lời:**
- **Polyfill**: Code cung cấp functionality cho older browsers không support feature mới
- **Transpiling**: Convert code từ syntax này sang syntax khác (ES6+ → ES5)
- **Hoạt động**: Polyfill thêm methods/APIs, Transpiling convert syntax
- **Ưu điểm**: Browser compatibility, modern development
- **Nhược điểm**: Bundle size tăng, complexity

**Code Example:**
```typescript
// Polyfill cho Array.includes (ES2016)
if (!Array.prototype.includes) {
  Array.prototype.includes = function(searchElement: any, fromIndex?: number): boolean {
    const O = Object(this);
    const len = parseInt(O.length) || 0;
    if (len === 0) return false;

    const n = parseInt(fromIndex) || 0;
    let k = n >= 0 ? n : Math.max(len + n, 0);

    while (k < len) {
      if (O[k] === searchElement) return true;
      k++;
    }
    return false;
  };
}

// Polyfill cho Promise (ES2015)
if (!window.Promise) {
  window.Promise = class Promise {
    private state: 'pending' | 'fulfilled' | 'rejected' = 'pending';
    private value: any;
    private reason: any;
    private onFulfilledCallbacks: Function[] = [];
    private onRejectedCallbacks: Function[] = [];

    constructor(executor: (resolve: Function, reject: Function) => void) {
      const resolve = (value: any) => {
        if (this.state === 'pending') {
          this.state = 'fulfilled';
          this.value = value;
          this.onFulfilledCallbacks.forEach(callback => callback(value));
        }
      };

      const reject = (reason: any) => {
        if (this.state === 'pending') {
          this.state = 'rejected';
          this.reason = reason;
          this.onRejectedCallbacks.forEach(callback => callback(reason));
        }
      };

      try {
        executor(resolve, reject);
      } catch (error) {
        reject(error);
      }
    }

    then(onFulfilled?: Function, onRejected?: Function): Promise {
      return new Promise((resolve, reject) => {
        if (this.state === 'fulfilled') {
          try {
            const result = onFulfilled ? onFulfilled(this.value) : this.value;
            resolve(result);
          } catch (error) {
            reject(error);
          }
        } else if (this.state === 'rejected') {
          try {
            const result = onRejected ? onRejected(this.reason) : this.reason;
            resolve(result);
          } catch (error) {
            reject(error);
          }
        } else {
          this.onFulfilledCallbacks.push(onFulfilled || ((value: any) => resolve(value)));
          this.onRejectedCallbacks.push(onRejected || ((reason: any) => reject(reason)));
        }
      });
    }
  };
}

// Transpiling: ES6+ → ES5
// ES6+ Code
const greet = (name: string): string => `Hello ${name}`;
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(n => n * 2);

// Transpiled ES5 Code
var greet = function(name) {
  return "Hello " + name;
};
var numbers = [1, 2, 3, 4, 5];
var doubled = numbers.map(function(n) {
  return n * 2;
});

// Khi nào cần viết polyfill
function needsPolyfill(): boolean {
  // Check if feature exists
  if (!Array.prototype.includes) {
    console.log('Array.includes needs polyfill');
    return true;
  }

  if (!window.fetch) {
    console.log('Fetch API needs polyfill');
    return true;
  }

  if (!Object.assign) {
    console.log('Object.assign needs polyfill');
    return true;
  }

  return false;
}
```

**Best Practices:**
- Sử dụng polyfill cho missing APIs
- Sử dụng Babel cho transpiling
- Sử dụng core-js cho comprehensive polyfills
- Sử dụng feature detection

**Mistakes:**
```typescript
// ❌ Sai: Không check feature support
const result = [1, 2, 3].includes(2); // Error in IE

// ✅ Đúng: Check feature support
if (Array.prototype.includes) {
  const result = [1, 2, 3].includes(2);
} else {
  // Use alternative or polyfill
  const result = [1, 2, 3].indexOf(2) !== -1;
}
```

---

## **Phần 11: Advanced Asynchronous Patterns**

### **Q39: EventEmitter & Observer Pattern**

**Trả lời:**
- **EventEmitter**: Pattern để emit và listen events
- **Observer Pattern**: Design pattern cho one-to-many dependency
- **Pub/Sub**: Publisher-Subscriber pattern cho loose coupling
- **Ưu điểm**: Decoupled components, flexible communication
- **Nhược điểm**: Có thể gây memory leaks, hard to debug

**Code Example:**
```typescript
// Custom EventEmitter
class EventEmitter {
  private events: Map<string, Function[]> = new Map();

  on(event: string, listener: Function): void {
    if (!this.events.has(event)) {
      this.events.set(event, []);
    }
    this.events.get(event)!.push(listener);
  }

  off(event: string, listener: Function): void {
    const listeners = this.events.get(event);
    if (listeners) {
      const index = listeners.indexOf(listener);
      if (index > -1) {
        listeners.splice(index, 1);
      }
    }
  }

  emit(event: string, ...args: any[]): void {
    const listeners = this.events.get(event);
    if (listeners) {
      listeners.forEach(listener => listener(...args));
    }
  }

  once(event: string, listener: Function): void {
    const onceWrapper = (...args: any[]) => {
      listener(...args);
      this.off(event, onceWrapper);
    };
    this.on(event, onceWrapper);
  }
}

// Usage
const emitter = new EventEmitter();

// Subscribe to events
emitter.on('user:login', (user: any) => {
  console.log('User logged in:', user.name);
});

emitter.on('user:logout', (user: any) => {
  console.log('User logged out:', user.name);
});

// Emit events
emitter.emit('user:login', { name: 'John', id: 1 });
emitter.emit('user:logout', { name: 'John', id: 1 });

// Observer Pattern
interface Observer {
  update(data: any): void;
}

class Subject {
  private observers: Observer[] = [];
  private state: any;

  addObserver(observer: Observer): void {
    this.observers.push(observer);
  }

  removeObserver(observer: Observer): void {
    const index = this.observers.indexOf(observer);
    if (index > -1) {
      this.observers.splice(index, 1);
    }
  }

  notifyObservers(): void {
    this.observers.forEach(observer => observer.update(this.state));
  }

  setState(newState: any): void {
    this.state = newState;
    this.notifyObservers();
  }
}

// Concrete Observer
class UserNotificationObserver implements Observer {
  update(data: any): void {
    console.log('Notification: User state changed to', data);
  }
}

// Usage
const subject = new Subject();
const notificationObserver = new UserNotificationObserver();

subject.addObserver(notificationObserver);
subject.setState('logged_in');

// Pub/Sub Pattern
class PubSub {
  private subscribers: Map<string, Function[]> = new Map();

  subscribe(topic: string, callback: Function): () => void {
    if (!this.subscribers.has(topic)) {
      this.subscribers.set(topic, []);
    }
    this.subscribers.get(topic)!.push(callback);

    // Return unsubscribe function
    return () => {
      const callbacks = this.subscribers.get(topic);
      if (callbacks) {
        const index = callbacks.indexOf(callback);
        if (index > -1) {
          callbacks.splice(index, 1);
        }
      }
    };
  }

  publish(topic: string, data: any): void {
    const callbacks = this.subscribers.get(topic);
    if (callbacks) {
      callbacks.forEach(callback => callback(data));
    }
  }
}

// Usage
const pubsub = new PubSub();

const unsubscribe = pubsub.subscribe('user:update', (user: any) => {
  console.log('User updated:', user);
});

pubsub.publish('user:update', { name: 'John', age: 30 });

// Cleanup
unsubscribe();
```

**Best Practices:**
- Sử dụng EventEmitter cho component communication
- Sử dụng Observer pattern cho state management
- Sử dụng Pub/Sub cho loose coupling
- Cleanup listeners để tránh memory leaks

**Mistakes:**
```typescript
// ❌ Sai: Không cleanup listeners
emitter.on('event', handler);
// Memory leak nếu không remove listener

// ✅ Đúng: Cleanup listeners
const cleanup = () => emitter.off('event', handler);
// Call cleanup when component unmounts
```

---

### **Q40: Generator Functions & Async Generators**

**Trả lời:**
- **Generator Functions**: Functions có thể pause và resume execution
- **yield**: Keyword để pause function và return value
- **yield***: Delegate to another generator
- **Async Generators**: Generators với async/await support
- **Ưu điểm**: Memory efficient, lazy evaluation, complex iteration
- **Nhược điểm**: Complex syntax, not widely used

**Code Example:**
```typescript
// Basic Generator Function
function* numberGenerator(): Generator<number, void, unknown> {
  yield 1;
  yield 2;
  yield 3;
  return 4; // Final value
}

const gen = numberGenerator();
console.log(gen.next()); // { value: 1, done: false }
console.log(gen.next()); // { value: 2, done: false }
console.log(gen.next()); // { value: 3, done: false }
console.log(gen.next()); // { value: 4, done: true }

// Generator với parameters
function* counter(start: number, end: number): Generator<number, void, unknown> {
  for (let i = start; i <= end; i++) {
    yield i;
  }
}

const counterGen = counter(1, 5);
for (const value of counterGen) {
  console.log(value); // 1, 2, 3, 4, 5
}

// yield* - Delegate to another generator
function* generator1(): Generator<number, void, unknown> {
  yield 1;
  yield 2;
}

function* generator2(): Generator<number, void, unknown> {
  yield 3;
  yield 4;
}

function* combinedGenerator(): Generator<number, void, unknown> {
  yield* generator1();
  yield* generator2();
  yield 5;
}

const combined = combinedGenerator();
console.log([...combined]); // [1, 2, 3, 4, 5]

// Generator với input values
function* inputGenerator(): Generator<number, void, number> {
  let value = yield 1;
  console.log('Received:', value);
  value = yield 2;
  console.log('Received:', value);
  return value;
}

const inputGen = inputGenerator();
console.log(inputGen.next()); // { value: 1, done: false }
console.log(inputGen.next(10)); // Received: 10, { value: 2, done: false }
console.log(inputGen.next(20)); // Received: 20, { value: 20, done: true }

// Async Generator
async function* asyncNumberGenerator(): AsyncGenerator<number, void, unknown> {
  yield 1;
  await new Promise(resolve => setTimeout(resolve, 1000));
  yield 2;
  await new Promise(resolve => setTimeout(resolve, 1000));
  yield 3;
}

async function consumeAsyncGenerator(): Promise<void> {
  for await (const value of asyncNumberGenerator()) {
    console.log('Async value:', value);
  }
}

consumeAsyncGenerator(); // Logs: Async value: 1, then 2, then 3

// Practical example: Data streaming
async function* dataStream(): AsyncGenerator<string, void, unknown> {
  const data = ['chunk1', 'chunk2', 'chunk3'];
  for (const chunk of data) {
    await new Promise(resolve => setTimeout(resolve, 500));
    yield chunk;
  }
}

async function processStream(): Promise<void> {
  for await (const chunk of dataStream()) {
    console.log('Processing chunk:', chunk);
  }
}

processStream();

// Generator for infinite sequences
function* fibonacci(): Generator<number, void, unknown> {
  let a = 0, b = 1;
  while (true) {
    yield a;
    [a, b] = [b, a + b];
  }
}

const fib = fibonacci();
console.log(fib.next().value); // 0
console.log(fib.next().value); // 1
console.log(fib.next().value); // 1
console.log(fib.next().value); // 2
console.log(fib.next().value); // 3
```

**Best Practices:**
- Sử dụng generators cho lazy evaluation
- Sử dụng async generators cho data streaming
- Sử dụng yield* cho generator composition
- Sử dụng for...of với generators

**Mistakes:**
```typescript
// ❌ Sai: Không hiểu generator state
const gen = numberGenerator();
console.log(gen.next()); // { value: 1, done: false }
console.log(gen.next()); // { value: 2, done: false }
// Generator state is maintained

// ✅ Đúng: Hiểu generator state
const gen = numberGenerator();
const values = [...gen]; // [1, 2, 3]
// Generator is exhausted after iteration
```

---

## **Phần 12: Memory Management & Performance**

### **Q41: Memory Management & Garbage Collection**

**Trả lời:**
- **Memory Management**: JavaScript tự động quản lý memory thông qua Garbage Collection
- **Garbage Collection**: Process tự động free memory không còn được sử dụng
- **Mark and Sweep**: Algorithm chính để detect và collect garbage
- **Ưu điểm**: Automatic memory management, developer không cần manual free
- **Nhược điểm**: Có thể gây performance issues, unpredictable timing

**Code Example:**
```typescript
// Memory allocation
function createLargeObject(): object {
  return {
    data: new Array(1000000).fill('large data'),
    timestamp: Date.now()
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

---

### **Q42: Memory Leaks Detection & Prevention**

**Trả lời:**
- **Memory Leaks**: Memory được allocate nhưng không được free
- **Common Causes**: Event listeners, DOM references, closures, timers
- **Detection**: Browser DevTools, memory profiling
- **Prevention**: Proper cleanup, weak references, monitoring
- **Ưu điểm**: Better performance, stable applications
- **Nhược điểm**: Cần careful coding, monitoring overhead

**Code Example:**
```typescript
// Common memory leak patterns

// 1. Event listeners không được cleanup
class Component {
  private element: HTMLElement;

  constructor() {
    this.element = document.createElement('div');
    // Memory leak: không cleanup event listener
    this.element.addEventListener('click', this.handleClick.bind(this));
  }

  private handleClick(): void {
    console.log('Clicked');
  }

  // Fix: Add cleanup method
  destroy(): void {
    this.element.removeEventListener('click', this.handleClick.bind(this));
    this.element.remove();
  }
}

// 2. DOM references
function createMemoryLeak(): void {
  const elements: HTMLElement[] = [];

  for (let i = 0; i < 1000; i++) {
    const element = document.createElement('div');
    elements.push(element); // Keeps reference
  }

  // Fix: Clear references
  elements.length = 0;
}

// 3. Closures giữ references
function createClosureLeak(): void {
  const largeData = new Array(1000000).fill('data');

  return function() {
    // Closure giữ reference đến largeData
    console.log('Closure executed');
  };
}

// Fix: Clear references
function createProperClosure(): () => void {
  const largeData = new Array(1000000).fill('data');

  return function() {
    console.log('Closure executed');
    // Clear reference when done
    largeData.length = 0;
  };
}

// 4. Timers không được clear
function createTimerLeak(): void {
  const interval = setInterval(() => {
    console.log('Timer tick');
  }, 1000);

  // Memory leak: không clear interval
}

// Fix: Clear timers
function createProperTimer(): () => void {
  const interval = setInterval(() => {
    console.log('Timer tick');
  }, 1000);

  return () => clearInterval(interval);
}

// Memory leak detection
class MemoryLeakDetector {
  private static instances: Set<object> = new Set();

  static track(obj: object): void {
    this.instances.add(obj);
  }

  static untrack(obj: object): void {
    this.instances.delete(obj);
  }

  static getInstanceCount(): number {
    return this.instances.size;
  }
}

// Usage
class TrackedComponent {
  constructor() {
    MemoryLeakDetector.track(this);
  }

  destroy(): void {
    MemoryLeakDetector.untrack(this);
  }
}

// Memory profiling
function profileMemory(): void {
  if ('memory' in performance) {
    const memory = (performance as any).memory;
    const used = memory.usedJSHeapSize / 1024 / 1024;
    const total = memory.totalJSHeapSize / 1024 / 1024;

    console.log(`Memory usage: ${used.toFixed(2)}MB / ${total.toFixed(2)}MB`);

    // Alert if memory usage is high
    if (used > 100) {
      console.warn('High memory usage detected!');
    }
  }
}

// Weak references để tránh memory leaks
class WeakReferenceManager {
  private weakMap = new WeakMap<object, any>();

  setReference(obj: object, data: any): void {
    this.weakMap.set(obj, data);
  }

  getReference(obj: object): any {
    return this.weakMap.get(obj);
  }

  // No need to cleanup - WeakMap automatically removes entries
}

// Proper cleanup pattern
class ResourceManager {
  private resources: Set<() => void> = new Set();

  addResource(cleanup: () => void): void {
    this.resources.add(cleanup);
  }

  cleanup(): void {
    this.resources.forEach(cleanup => cleanup());
    this.resources.clear();
  }
}

// Usage
const manager = new ResourceManager();

// Add event listener
const cleanup1 = addEventListenerWithCleanup();
manager.addResource(cleanup1);

// Add timer
const cleanup2 = createProperTimer();
manager.addResource(cleanup2);

// Later: manager.cleanup(); // Cleanup all resources
```

**Best Practices:**
- Sử dụng WeakMap/WeakSet cho temporary references
- Cleanup event listeners và timers
- Remove DOM references
- Sử dụng resource managers
- Monitor memory usage
- Sử dụng proper cleanup patterns

**Mistakes:**
```typescript
// ❌ Sai: Không cleanup resources
const interval = setInterval(() => {}, 1000);
// Memory leak

// ✅ Đúng: Cleanup resources
const interval = setInterval(() => {}, 1000);
clearInterval(interval); // Cleanup
```

---

## **Phần 13: Module System & Advanced Object Concepts**

### **Q43: Dynamic Import & Module System**

**Trả lời:**
- **Dynamic Import**: Import modules at runtime thay vì compile time
- **Module System**: ES6 modules, CommonJS, AMD
- **Hoạt động**: Dynamic import trả về Promise, cho phép lazy loading
- **Ưu điểm**: Code splitting, lazy loading, better performance
- **Nhược điểm**: Complexity, async handling required

**Code Example:**
```typescript
// Static import (compile time)
import { utils } from './utils';
import React from 'react';

// Dynamic import (runtime)
async function loadModule(): Promise<void> {
  try {
    // Dynamic import trả về Promise
    const module = await import('./heavy-module');
    const result = module.default();
    console.log('Module loaded:', result);
  } catch (error) {
    console.error('Failed to load module:', error);
  }
}

// Conditional loading
async function loadModuleConditionally(condition: boolean): Promise<void> {
  if (condition) {
    const { heavyFunction } = await import('./heavy-module');
    heavyFunction();
  }
}

// Lazy loading components
async function loadComponent(): Promise<React.ComponentType> {
  const module = await import('./LazyComponent');
  return module.default;
}

// Code splitting với dynamic import
function createRouteLoader(routeName: string) {
  return async () => {
    switch (routeName) {
      case 'home':
        return await import('./routes/Home');
      case 'about':
        return await import('./routes/About');
      case 'contact':
        return await import('./routes/Contact');
      default:
        throw new Error(`Unknown route: ${routeName}`);
    }
  };
}

// Usage
const homeLoader = createRouteLoader('home');
const HomeComponent = await homeLoader();

// Dynamic import với error handling
async function safeImport(modulePath: string): Promise<any> {
  try {
    const module = await import(modulePath);
    return module;
  } catch (error) {
    console.error(`Failed to import ${modulePath}:`, error);
    return null;
  }
}

// Lazy loading với React
const LazyComponent = React.lazy(() => import('./LazyComponent'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <LazyComponent />
    </Suspense>
  );
}

// Module system comparison
// ES6 Modules
export const name = 'John';
export default function greet() { }

// CommonJS
module.exports = {
  name: 'John',
  greet: function() { }
};

// AMD
define(['dependency'], function(dependency) {
  return {
    name: 'John',
    greet: function() { }
  };
});

// Dynamic import với multiple modules
async function loadMultipleModules(): Promise<void> {
  const [module1, module2, module3] = await Promise.all([
    import('./module1'),
    import('./module2'),
    import('./module3')
  ]);

  console.log('All modules loaded');
}

// Khi nào nên dùng dynamic import
function shouldUseDynamicImport(): boolean {
  // 1. Large modules không cần ngay
  // 2. Conditional loading
  // 3. Code splitting
  // 4. Lazy loading
  return true;
}
```

**Best Practices:**
- Sử dụng dynamic import cho large modules
- Sử dụng cho conditional loading
- Sử dụng cho code splitting
- Sử dụng proper error handling
- Sử dụng với React.lazy cho components

**Mistakes:**
```typescript
// ❌ Sai: Không handle errors
const module = await import('./module');
// Có thể throw error

// ✅ Đúng: Handle errors
try {
  const module = await import('./module');
} catch (error) {
  console.error('Import failed:', error);
}
```

---

### **Q44: Advanced Array & Object Methods**

**Trả lời:**
- **Advanced Array Methods**: flat, flatMap, from, of, entries, values, keys
- **Advanced Object Methods**: Object.assign, Object.entries, Object.values, Object.keys
- **Hoạt động**: Các methods mới trong ES6+ cho array và object manipulation
- **Ưu điểm**: Powerful manipulation, functional programming support
- **Nhược điểm**: Browser compatibility, learning curve

**Code Example:**
```typescript
// Array.flat() - Flatten nested arrays
const nestedArray = [1, [2, 3], [4, [5, 6]]];
const flattened = nestedArray.flat(); // [1, 2, 3, 4, [5, 6]]
const deeplyFlattened = nestedArray.flat(2); // [1, 2, 3, 4, 5, 6]

// Array.flatMap() - Map và flatten
const numbers = [1, 2, 3, 4];
const doubled = numbers.flatMap(n => [n, n * 2]); // [1, 2, 2, 4, 3, 6, 4, 8]

// Array.from() - Create array from iterable
const arrayFromString = Array.from('hello'); // ['h', 'e', 'l', 'l', 'o']
const arrayFromSet = Array.from(new Set([1, 2, 2, 3])); // [1, 2, 3]
const arrayWithMapping = Array.from({ length: 5 }, (_, i) => i * 2); // [0, 2, 4, 6, 8]

// Array.of() - Create array from arguments
const arrayOf = Array.of(1, 2, 3, 4); // [1, 2, 3, 4]
const arrayOfSingle = Array.of(7); // [7]

// Array.entries() - Get index-value pairs
const fruits = ['apple', 'banana', 'orange'];
for (const [index, fruit] of fruits.entries()) {
  console.log(`${index}: ${fruit}`);
}

// Array.values() - Get values
const values = fruits.values();
for (const value of values) {
  console.log(value);
}

// Array.keys() - Get indices
const keys = fruits.keys();
for (const key of keys) {
  console.log(key);
}

// Object.assign() - Copy properties
const target = { a: 1, b: 2 };
const source = { b: 3, c: 4 };
const result = Object.assign(target, source); // { a: 1, b: 3, c: 4 }

// Object.entries() - Get key-value pairs
const person = { name: 'John', age: 30, city: 'HCM' };
const entries = Object.entries(person); // [['name', 'John'], ['age', 30], ['city', 'HCM']]

// Object.values() - Get values
const values = Object.values(person); // ['John', 30, 'HCM']

// Object.keys() - Get keys
const keys = Object.keys(person); // ['name', 'age', 'city']

// Practical examples
function processUserData(users: any[]): any[] {
  return users
    .flatMap(user => user.hobbies || []) // Flatten hobbies
    .filter(hobby => hobby.length > 3) // Filter long hobbies
    .map(hobby => hobby.toUpperCase()); // Transform
}

function createLookupTable(objects: any[]): Map<string, any> {
  return new Map(
    objects.flatMap(obj =>
      Object.entries(obj).map(([key, value]) => [key, obj])
    )
  );
}

function mergeObjects(...objects: any[]): any {
  return objects.reduce((acc, obj) => Object.assign(acc, obj), {});
}

function getObjectStats(obj: any): { keys: number, values: any[], entries: [string, any][] } {
  return {
    keys: Object.keys(obj).length,
    values: Object.values(obj),
    entries: Object.entries(obj)
  };
}

// Advanced usage
function transformData(data: any[]): any[] {
  return data
    .flatMap(item => item.items || []) // Flatten nested items
    .map(item => ({
      ...item,
      processed: true,
      timestamp: Date.now()
    }))
    .filter(item => item.active);
}

function createIndexMap(data: any[]): Map<string, any[]> {
  const indexMap = new Map();

  data.forEach(item => {
    Object.entries(item).forEach(([key, value]) => {
      if (!indexMap.has(key)) {
        indexMap.set(key, []);
      }
      indexMap.get(key).push(value);
    });
  });

  return indexMap;
}
```

**Best Practices:**
- Sử dụng flat() cho nested arrays
- Sử dụng flatMap() cho map và flatten
- Sử dụng Object.entries() cho iteration
- Sử dụng Object.assign() cho object merging
- Sử dụng Array.from() cho array creation

**Mistakes:**
```typescript
// ❌ Sai: Không hiểu flat depth
const nested = [1, [2, [3, [4]]]];
const flattened = nested.flat(); // [1, 2, [3, [4]]] - only 1 level

// ✅ Đúng: Specify depth
const deeplyFlattened = nested.flat(Infinity); // [1, 2, 3, 4]
```

---

### **Q45: Advanced Object Concepts**

**Trả lời:**
- **Object.create()**: Tạo object với specific prototype
- **Prototype Chain**: Mechanism cho inheritance
- **Inheritance**: Object-oriented programming concept
- **Mixin**: Pattern để share functionality
- **Object.freeze/seal/preventExtensions**: Control object mutability
- **Ưu điểm**: Flexible object creation, inheritance, immutability
- **Nhược điểm**: Complex prototype chain, performance overhead

**Code Example:**
```typescript
// Object.create() - Create object with specific prototype
const personPrototype = {
  greet(): string {
    return `Hello, I'm ${this.name}`;
  },
  getAge(): number {
    return this.age;
  }
};

const person = Object.create(personPrototype);
person.name = 'John';
person.age = 30;

console.log(person.greet()); // "Hello, I'm John"
console.log(person.getAge()); // 30

// Prototype chain
function Person(name: string, age: number) {
  this.name = name;
  this.age = age;
}

Person.prototype.greet = function(): string {
  return `Hello, I'm ${this.name}`;
};

function Student(name: string, age: number, grade: string) {
  Person.call(this, name, age);
  this.grade = grade;
}

// Set up inheritance
Student.prototype = Object.create(Person.prototype);
Student.prototype.constructor = Student;

Student.prototype.study = function(): string {
  return `${this.name} is studying`;
};

const student = new Student('Jane', 20, 'A');
console.log(student.greet()); // "Hello, I'm Jane"
console.log(student.study()); // "Jane is studying"

// Mixin pattern
const canFly = {
  fly(): string {
    return `${this.name} is flying`;
  }
};

const canSwim = {
  swim(): string {
    return `${this.name} is swimming`;
  }
};

function mixin(target: any, ...sources: any[]): any {
  sources.forEach(source => {
    Object.getOwnPropertyNames(source).forEach(name => {
      if (name !== 'constructor') {
        target[name] = source[name];
      }
    });
  });
  return target;
}

function Bird(name: string) {
  this.name = name;
}

mixin(Bird.prototype, canFly);

const bird = new Bird('Eagle');
console.log(bird.fly()); // "Eagle is flying"

// Object.freeze() - Make object immutable
const frozenObject = Object.freeze({
  name: 'John',
  age: 30,
  address: {
    city: 'HCM'
  }
});

// frozenObject.name = 'Jane'; // Error in strict mode
// frozenObject.address.city = 'HN'; // Still works (shallow freeze)

// Deep freeze function
function deepFreeze(obj: any): any {
  Object.getOwnPropertyNames(obj).forEach(prop => {
    if (obj[prop] !== null && typeof obj[prop] === 'object') {
      deepFreeze(obj[prop]);
    }
  });
  return Object.freeze(obj);
}

const deeplyFrozen = deepFreeze({
  name: 'John',
  address: {
    city: 'HCM'
  }
});

// Object.seal() - Prevent adding/removing properties
const sealedObject = Object.seal({
  name: 'John',
  age: 30
});

// sealedObject.name = 'Jane'; // OK
// sealedObject.city = 'HCM'; // Error in strict mode
// delete sealedObject.age; // Error in strict mode

// Object.preventExtensions() - Prevent adding properties
const nonExtensibleObject = Object.preventExtensions({
  name: 'John',
  age: 30
});

// nonExtensibleObject.name = 'Jane'; // OK
// nonExtensibleObject.city = 'HCM'; // Error in strict mode
// delete nonExtensibleObject.age; // OK

// Property descriptors
const obj = { name: 'John' };

Object.defineProperty(obj, 'age', {
  value: 30,
  writable: false,
  enumerable: true,
  configurable: false
});

// obj.age = 40; // Error in strict mode
// delete obj.age; // Error in strict mode

// Get property descriptor
const descriptor = Object.getOwnPropertyDescriptor(obj, 'age');
console.log(descriptor); // { value: 30, writable: false, enumerable: true, configurable: false }

// Object.getOwnPropertyNames() vs Object.keys()
const obj = { a: 1, b: 2 };
Object.defineProperty(obj, 'c', {
  value: 3,
  enumerable: false
});

console.log(Object.keys(obj)); // ['a', 'b']
console.log(Object.getOwnPropertyNames(obj)); // ['a', 'b', 'c']

// hasOwnProperty vs in operator
const obj = { a: 1 };
console.log(obj.hasOwnProperty('a')); // true
console.log('a' in obj); // true
console.log(obj.hasOwnProperty('toString')); // false
console.log('toString' in obj); // true

// Practical examples
function createImmutableObject(data: any): any {
  return Object.freeze(
    Object.keys(data).reduce((acc, key) => {
      acc[key] = typeof data[key] === 'object' ? deepFreeze(data[key]) : data[key];
      return acc;
    }, {} as any)
  );
}

function createMixin(...mixins: any[]): any {
  return function(target: any): any {
    mixins.forEach(mixin => {
      Object.getOwnPropertyNames(mixin).forEach(name => {
        if (name !== 'constructor') {
          target[name] = mixin[name];
        }
      });
    });
    return target;
  };
}

// Usage
const withLogging = createMixin({
  log(message: string): void {
    console.log(`${this.name}: ${message}`);
  }
});

function User(name: string) {
  this.name = name;
}

withLogging(User.prototype);

const user = new User('John');
user.log('Hello'); // "John: Hello"
```

**Best Practices:**
- Sử dụng Object.create() cho prototype-based inheritance
- Sử dụng mixins cho functionality sharing
- Sử dụng Object.freeze() cho immutability
- Sử dụng Object.seal() cho controlled mutability
- Sử dụng proper property descriptors

**Mistakes:**
```typescript
// ❌ Sai: Không hiểu shallow vs deep freeze
const obj = Object.freeze({ a: { b: 1 } });
obj.a.b = 2; // Still works!

// ✅ Đúng: Deep freeze
const obj = deepFreeze({ a: { b: 1 } });
obj.a.b = 2; // Error in strict mode
```

---

## **Phần 14: Advanced Mistakes & Security**

### **Q46: Common JavaScript Mistakes - Lỗi Thường Gặp**

**Trả lời:**
- **🔥 Type Coercion Mistakes**: Sử dụng `==` thay vì `===`, unexpected type conversions
- **🎯 Scope & Hoisting Issues**: `var` hoisting, temporal dead zone với `let/const`
- **⚡ Async/Await Mistakes**: Không handle errors, missing await keywords
- **✅ Memory Leaks**: Event listeners không cleanup, circular references
- **⚠️ Performance Issues**: Inefficient loops, DOM manipulation trong loops

**Code Example:**
```typescript
// 🔥 Type Coercion Mistakes (Lỗi ép kiểu)
// ❌ Sai: Sử dụng == thay vì ===
console.log(0 == false);     // true - unexpected!
console.log("" == 0);        // true - dangerous!
console.log(null == undefined); // true - confusing!

// ✅ Đúng: Sử dụng ===
console.log(0 === false);    // false - clear
console.log("" === 0);       // false - safe
console.log(null === undefined); // false - explicit

// 🎯 Scope & Hoisting Issues (Vấn đề phạm vi và hoisting)
// ❌ Sai: var hoisting confusion
console.log(x); // undefined - not error!
var x = 5;

// ❌ Sai: temporal dead zone
console.log(y); // ReferenceError!
let y = 5;

// ✅ Đúng: declare trước khi sử dụng
let z = 5;
console.log(z); // 5

// ⚡ Async/Await Mistakes (Lỗi async/await)
// ❌ Sai: Không handle errors
async function fetchData() {
  const response = await fetch('/api/data');
  const data = await response.json(); // Có thể throw error
  return data;
}

// ✅ Đúng: Handle errors properly
async function fetchData() {
  try {
    const response = await fetch('/api/data');
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Fetch error:', error);
    throw error;
  }
}

// ✅ Memory Leaks (Rò rỉ bộ nhớ)
// ❌ Sai: Event listeners không cleanup
function addClickListener() {
  document.addEventListener('click', handleClick);
  // Không remove listener - memory leak!
}

// ✅ Đúng: Cleanup event listeners
function addClickListener() {
  const handler = (e: Event) => handleClick(e);
  document.addEventListener('click', handler);

  // Return cleanup function
  return () => {
    document.removeEventListener('click', handler);
  };
}

// ✅ Performance Issues (Vấn đề hiệu suất)
// ❌ Sai: DOM manipulation trong loop
const items = [1, 2, 3, 4, 5];
for (let i = 0; i < items.length; i++) {
  document.getElementById('list').innerHTML += `<li>${items[i]}</li>`;
  // Mỗi lần thay đổi DOM trigger reflow!
}

// ✅ Đúng: Batch DOM updates
const items = [1, 2, 3, 4, 5];
const listElement = document.getElementById('list');
const fragment = document.createDocumentFragment();

items.forEach(item => {
  const li = document.createElement('li');
  li.textContent = item.toString();
  fragment.appendChild(li);
});

listElement.appendChild(fragment); // Single DOM update

// 🔥 Advanced Mistakes (Lỗi nâng cao)
// ❌ Sai: Circular references
let obj1: any = { name: 'obj1' };
let obj2: any = { name: 'obj2' };
obj1.ref = obj2;
obj2.ref = obj1; // Circular reference - memory leak!

// ✅ Đúng: WeakMap cho circular references
const refs = new WeakMap();
let obj1: any = { name: 'obj1' };
let obj2: any = { name: 'obj2' };
refs.set(obj1, obj2);
refs.set(obj2, obj1); // WeakMap allows garbage collection

// ❌ Sai: Prototype pollution
const obj: any = {};
obj.__proto__.isAdmin = true; // Dangerous!

// ✅ Đúng: Object.create(null) hoặc Object.freeze
const obj = Object.create(null); // No prototype
// hoặc
Object.freeze(Object.prototype); // Prevent modification
```

**🎯 Best Practices:**
- **✅ Luôn sử dụng `===`** thay vì `==` để tránh type coercion
- **✅ Sử dụng `let/const`** thay vì `var` để tránh hoisting issues
- **✅ Handle errors** trong async/await với try/catch
- **✅ Cleanup resources** (event listeners, timers, subscriptions)
- **✅ Batch DOM updates** để tránh multiple reflows
- **✅ Sử dụng WeakMap/WeakSet** cho circular references

---

### **Q47: JavaScript Security Vulnerabilities - Lỗ Hổng Bảo Mật**

**Trả lời:**
- **🔥 XSS (Cross-Site Scripting)**: Inject malicious scripts vào web pages
- **🎯 CSRF (Cross-Site Request Forgery)**: Force users thực hiện unwanted actions
- **⚡ Prototype Pollution**: Modify Object.prototype gây unexpected behavior
- **✅ Code Injection**: Execute arbitrary code thông qua eval() hoặc similar
- **⚠️ Information Disclosure**: Expose sensitive data trong client-side code

**Code Example:**
```typescript
// 🔥 XSS (Cross-Site Scripting) Vulnerabilities
// ❌ Nguy hiểm: Direct innerHTML với user input
function displayUserInput(userInput: string) {
  document.getElementById('output').innerHTML = userInput;
  // Nếu userInput = "<script>alert('XSS')</script>" - nguy hiểm!
}

// ✅ An toàn: Sanitize input hoặc sử dụng textContent
function displayUserInput(userInput: string) {
  const output = document.getElementById('output');
  output.textContent = userInput; // Safe - không execute HTML
}

// ✅ An toàn: Sử dụng DOMPurify để sanitize
import DOMPurify from 'dompurify';
function displayUserInput(userInput: string) {
  const cleanInput = DOMPurify.sanitize(userInput);
  document.getElementById('output').innerHTML = cleanInput;
}

// 🎯 CSRF (Cross-Site Request Forgery) Protection
// ❌ Nguy hiểm: Không có CSRF token
async function transferMoney(amount: number, toAccount: string) {
  const response = await fetch('/api/transfer', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ amount, toAccount })
  });
  // Có thể bị CSRF attack!
}

// ✅ An toàn: Sử dụng CSRF token
async function transferMoney(amount: number, toAccount: string) {
  const csrfToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content');

  const response = await fetch('/api/transfer', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRF-Token': csrfToken || ''
    },
    body: JSON.stringify({ amount, toAccount })
  });
}

// ⚡ Prototype Pollution Prevention
// ❌ Nguy hiểm: Merge objects không kiểm tra
function mergeObjects(target: any, source: any) {
  for (const key in source) {
    target[key] = source[key]; // Có thể modify prototype!
  }
  return target;
}

// ✅ An toàn: Kiểm tra hasOwnProperty
function mergeObjects(target: any, source: any) {
  for (const key in source) {
    if (source.hasOwnProperty(key)) {
      target[key] = source[key];
    }
  }
  return target;
}

// ✅ An toàn: Sử dụng Object.create(null)
const safeObject = Object.create(null); // No prototype
safeObject.__proto__ = { malicious: true }; // Không hoạt động

// ✅ Code Injection Prevention
// ❌ Nguy hiểm: Sử dụng eval()
function executeUserCode(userCode: string) {
  return eval(userCode); // Cực kỳ nguy hiểm!
}

// ✅ An toàn: Sử dụng Function constructor với validation
function executeUserCode(userCode: string) {
  // Validate code trước khi execute
  if (!isValidCode(userCode)) {
    throw new Error('Invalid code');
  }

  // Sử dụng sandbox environment
  return new Function('return ' + userCode)();
}

// ✅ Information Disclosure Prevention
// ❌ Nguy hiểm: Expose sensitive data trong client
const API_KEY = 'secret-api-key-12345'; // Visible trong source code!
const DATABASE_URL = 'mongodb://user:password@localhost/db';

// ✅ An toàn: Sử dụng environment variables
const API_KEY = process.env.REACT_APP_API_KEY; // Chỉ trong build time
// Hoặc fetch từ secure endpoint
async function getApiKey() {
  const response = await fetch('/api/get-key', {
    credentials: 'include' // Include cookies
  });
  return response.json();
}

// 🔥 Content Security Policy (CSP)
// ✅ Implement CSP headers
const cspHeader = `
  default-src 'self';
  script-src 'self' 'unsafe-inline' https://trusted-cdn.com;
  style-src 'self' 'unsafe-inline';
  img-src 'self' data: https:;
  connect-src 'self' https://api.example.com;
`;

// ✅ Sử dụng nonce cho inline scripts
const nonce = generateNonce();
const script = document.createElement('script');
script.nonce = nonce;
script.textContent = 'console.log("Safe inline script")';
document.head.appendChild(script);

// 🎯 Secure Coding Practices
// ✅ Input validation
function validateInput(input: string): boolean {
  // Whitelist approach
  const allowedPattern = /^[a-zA-Z0-9\s]+$/;
  return allowedPattern.test(input) && input.length <= 100;
}

// ✅ Output encoding
function encodeOutput(input: string): string {
  return input
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#x27;');
}

// ✅ Secure random generation
function generateSecureToken(): string {
  const array = new Uint8Array(32);
  crypto.getRandomValues(array);
  return Array.from(array, byte => byte.toString(16).padStart(2, '0')).join('');
}
```

**🎯 Security Best Practices:**
- **✅ Luôn validate và sanitize** user input
- **✅ Sử dụng HTTPS** cho tất cả communications
- **✅ Implement CSP** để prevent XSS attacks
- **✅ Sử dụng CSRF tokens** cho state-changing operations
- **✅ Không expose sensitive data** trong client-side code
- **✅ Sử dụng secure random generators** cho tokens và keys
- **✅ Regular security audits** và dependency updates

---

### **Q48: Performance Anti-Patterns - Anti-Patterns Hiệu Suất**

**Trả lời:**
- **🔥 Memory Leaks**: Event listeners, timers, closures không cleanup
- **🎯 Inefficient DOM Operations**: Multiple reflows, unnecessary DOM queries
- **⚡ Blocking Operations**: Synchronous operations trong main thread
- **✅ Inefficient Loops**: Nested loops, unnecessary iterations
- **⚠️ Poor Caching**: Không cache expensive operations

**Code Example:**
```typescript
// 🔥 Memory Leak Anti-Patterns
// ❌ Sai: Event listeners không cleanup
class Component {
  constructor() {
    window.addEventListener('resize', this.handleResize);
    // Không cleanup - memory leak!
  }

  handleResize = () => {
    // Handle resize
  };
}

// ✅ Đúng: Cleanup event listeners
class Component {
  private cleanup: (() => void)[] = [];

  constructor() {
    const handler = this.handleResize.bind(this);
    window.addEventListener('resize', handler);

    this.cleanup.push(() => {
      window.removeEventListener('resize', handler);
    });
  }

  destroy() {
    this.cleanup.forEach(cleanup => cleanup());
  }

  private handleResize = () => {
    // Handle resize
  };
}

// 🎯 Inefficient DOM Operations
// ❌ Sai: Multiple DOM queries và reflows
function updateElements() {
  for (let i = 0; i < 1000; i++) {
    const element = document.getElementById(`item-${i}`); // DOM query mỗi lần
    element.style.width = '100px';  // Trigger reflow
    element.style.height = '100px'; // Trigger reflow again
    element.style.backgroundColor = 'red'; // Trigger repaint
  }
}

// ✅ Đúng: Batch DOM operations
function updateElements() {
  const elements = document.querySelectorAll('[id^="item-"]'); // Single query
  const fragment = document.createDocumentFragment();

  elements.forEach(element => {
    // Batch style changes
    element.style.cssText = 'width: 100px; height: 100px; background-color: red;';
  });

  // Single reflow/repaint
}

// ⚡ Blocking Operations Anti-Patterns
// ❌ Sai: Blocking main thread
function processLargeData(data: number[]) {
  let result = 0;
  for (let i = 0; i < data.length; i++) {
    result += Math.sqrt(data[i]); // Blocking operation
  }
  return result;
}

// ✅ Đúng: Use Web Workers hoặc chunking
function processLargeData(data: number[]): Promise<number> {
  return new Promise((resolve) => {
    const chunkSize = 1000;
    let result = 0;
    let index = 0;

    function processChunk() {
      const end = Math.min(index + chunkSize, data.length);

      for (let i = index; i < end; i++) {
        result += Math.sqrt(data[i]);
      }

      index = end;

      if (index < data.length) {
        // Yield control back to browser
        setTimeout(processChunk, 0);
      } else {
        resolve(result);
      }
    }

    processChunk();
  });
}

// ✅ Inefficient Loop Anti-Patterns
// ❌ Sai: Nested loops với unnecessary operations
function findDuplicates(arr1: number[], arr2: number[]): number[] {
  const duplicates: number[] = [];

  for (let i = 0; i < arr1.length; i++) {
    for (let j = 0; j < arr2.length; j++) {
      if (arr1[i] === arr2[j]) {
        duplicates.push(arr1[i]);
      }
    }
  }

  return duplicates;
}

// ✅ Đúng: Sử dụng Set cho O(1) lookup
function findDuplicates(arr1: number[], arr2: number[]): number[] {
  const set2 = new Set(arr2);
  return arr1.filter(item => set2.has(item));
}

// ✅ Poor Caching Anti-Patterns
// ❌ Sai: Không cache expensive operations
function expensiveCalculation(n: number): number {
  // Simulate expensive operation
  let result = 0;
  for (let i = 0; i < n * 1000000; i++) {
    result += Math.random();
  }
  return result;
}

// Gọi nhiều lần với cùng input
console.log(expensiveCalculation(5)); // Expensive
console.log(expensiveCalculation(5)); // Expensive again!

// ✅ Đúng: Implement caching
const calculationCache = new Map<number, number>();

function expensiveCalculation(n: number): number {
  if (calculationCache.has(n)) {
    return calculationCache.get(n)!;
  }

  let result = 0;
  for (let i = 0; i < n * 1000000; i++) {
    result += Math.random();
  }

  calculationCache.set(n, result);
  return result;
}

// 🔥 Advanced Performance Anti-Patterns
// ❌ Sai: Unnecessary object creation trong loops
function processItems(items: string[]) {
  const results: string[] = [];

  items.forEach(item => {
    const processor = new ItemProcessor(); // New object mỗi lần
    results.push(processor.process(item));
  });

  return results;
}

// ✅ Đúng: Reuse objects
function processItems(items: string[]) {
  const processor = new ItemProcessor(); // Single instance
  return items.map(item => processor.process(item));
}

// ❌ Sai: Inefficient string concatenation
function buildString(parts: string[]): string {
  let result = '';
  for (const part of parts) {
    result += part; // Creates new string mỗi lần
  }
  return result;
}

// ✅ Đúng: Sử dụng array join
function buildString(parts: string[]): string {
  return parts.join('');
}
```

**🎯 Performance Best Practices:**
- **✅ Cleanup resources** (event listeners, timers, subscriptions)
- **✅ Batch DOM operations** để minimize reflows/repaints
- **✅ Use Web Workers** cho CPU-intensive tasks
- **✅ Implement caching** cho expensive operations
- **✅ Optimize algorithms** (use appropriate data structures)
- **✅ Profile và measure** performance trước khi optimize
- **✅ Use browser DevTools** để identify bottlenecks

---

## **🎯 Tổng Kết - JavaScript Core Fundamentals**

> **📊 Tổng quan**: 48 câu hỏi cốt lõi JavaScript được phân chia thành 14 chủ đề chính, từ cơ bản đến nâng cao

---

## **📋 Sơ Đồ Tư Duy - Tư Duy Senior**

```mermaid
graph TD
    A[JavaScript Core] --> B[Quản Lý Bộ Nhớ & Kiểu Dữ Liệu]
    A --> C[Engine & Runtime]
    A --> D[Hàm & Context]
    A --> E[DOM & Events]
    A --> F[Lập Trình Bất Đồng Bộ]
    A --> G[Patterns Nâng Cao]

    B --> B1[Primitive vs Reference<br/>Giá trị nguyên thủy vs tham chiếu]
    B --> B2[Immutable vs Mutable<br/>Bất biến vs có thể thay đổi]
    B --> B3[Deep vs Shallow Copy<br/>Sao chép sâu vs nông]
    B --> B4[Spread Operator<br/>Toán tử trải rộng]

    C --> C1[Call Stack & Event Loop<br/>Ngăn xếp gọi & vòng lặp sự kiện]
    C --> C2[Microtask vs Macrotask<br/>Tác vụ vi mô vs vĩ mô]
    C --> C3[Hoisting & Scope<br/>Nâng cao & phạm vi]
    C --> C4[Web APIs<br/>API trình duyệt]

    D --> D1[Closure & Privacy<br/>Đóng gói & riêng tư]
    D --> D2[Arrow vs Regular<br/>Mũi tên vs thường]
    D --> D3[this Binding<br/>Ràng buộc this]
    D --> D4[IIFE Pattern<br/>Hàm tự thực thi]

    E --> E1[Event Bubbling/Capturing<br/>Nổi bọt/Bắt sự kiện]
    E --> E2[Event Delegation<br/>Ủy quyền sự kiện]
    E --> E3[DOM Manipulation<br/>Thao tác DOM]
    E --> E4[Performance Optimization<br/>Tối ưu hiệu suất]

    F --> F1[Promises vs Async/Await<br/>Lời hứa vs chờ bất đồng bộ]
    F --> F2[Promise Combinators<br/>Kết hợp Promise]
    F --> F3[Error Handling<br/>Xử lý lỗi]
    F --> F4[HTTP Interceptors<br/>Chặn HTTP]

    G --> G1[Functional Programming<br/>Lập trình hàm]
    G --> G2[Proxy & Metaprogramming<br/>Proxy & siêu lập trình]
    G --> G3[Classes & OOP<br/>Lớp & OOP]
    G --> G4[Performance Patterns<br/>Patterns hiệu suất]
```

---

## **🔥 Khái Niệm Cốt Lõi - Phải Biết**

### **🧠 Quản Lý Bộ Nhớ (Q1-Q4)**
| Khái Niệm | Hiểu Biết Chính | Lời Khuyên Senior |
|-----------|-----------------|-------------------|
| **Primitive vs Reference** | Cấp phát Stack vs Heap | Luôn xem xét dấu chân bộ nhớ trong ứng dụng lớn |
| **Immutable vs Mutable** | Thay đổi trạng thái có thể dự đoán | Sử dụng patterns bất biến cho quản lý state React |
| **Deep vs Shallow Copy** | Sao chép tham chiếu vs giá trị | `structuredClone()` cho sao chép sâu hiện đại |
| **Spread Operator** | Cú pháp ES6+ | Ưu tiên spread hơn `Object.assign()` để dễ đọc |

### **⚡ Engine & Runtime (Q5-Q12)**
| Khái Niệm | Hiểu Biết Chính | Lời Khuyên Senior |
|-----------|-----------------|-------------------|
| **Event Loop** | Mô hình bất đồng bộ đơn luồng | Hiểu ưu tiên microtask để debug |
| **Hoisting** | Khai báo vs Khởi tạo | Sử dụng `let/const` để tránh temporal dead zone |
| **Set/Map vs Object** | Hiệu suất vs Tiện lợi | Sử dụng Map cho key động, Set cho tính duy nhất |
| **Web APIs** | Trình duyệt vs JS Engine | Biết API nào đồng bộ vs bất đồng bộ |

### **🎯 Hàm & Context (Q13-Q16)**
| Khái Niệm | Hiểu Biết Chính | Lời Khuyên Senior |
|-----------|-----------------|-------------------|
| **Closure** | Bảo tồn phạm vi từ vựng | Cần thiết cho module patterns và riêng tư dữ liệu |
| **this Binding** | Context động vs từ vựng | Arrow functions kế thừa `this`, regular functions tạo `this` mới |
| **IIFE** | Phạm vi thực thi ngay lập tức | Sử dụng cho khởi tạo module và tránh ô nhiễm global |

---

## **🚀 Patterns Nâng Cao - Cấp Senior**

### **🎨 DOM & Events (Q17-Q20)**
```typescript
// 🎯 Pattern Senior: Event Delegation (Ủy quyền sự kiện)
document.addEventListener('click', (e) => {
  const target = e.target as HTMLElement;
  const action = target.dataset.action;

  // Một handler cho nhiều elements
  switch(action) {
    case 'delete': handleDelete(target); break;
    case 'edit': handleEdit(target); break;
    case 'view': handleView(target); break;
  }
});
```

### **⚡ Làm Chủ Async (Q26-Q28)**
```typescript
// 🎯 Pattern Senior: Promise Orchestration (Điều phối Promise)
class APIService {
  async fetchUserData(userId: string) {
    const [user, posts, comments] = await Promise.allSettled([
      this.fetchUser(userId),
      this.fetchPosts(userId),
      this.fetchComments(userId)
    ]);

    return {
      user: user.status === 'fulfilled' ? user.value : null,
      posts: posts.status === 'fulfilled' ? posts.value : [],
      comments: comments.status === 'fulfilled' ? comments.value : []
    };
  }
}
```

### **🧩 Lập Trình Hàm (Q32)**
```typescript
// 🎯 Pattern Senior: Function Composition (Kết hợp hàm)
const pipe = (...fns: Function[]) => (value: any) =>
  fns.reduce((acc, fn) => fn(acc), value);

const processUser = pipe(
  validateUser,        // Xác thực user
  enrichUserData,      // Làm giàu dữ liệu user
  formatUserOutput,    // Định dạng output
  logUserActivity      // Ghi log hoạt động
);
```

---

## **💡 Hiểu Biết Senior & Best Practices**

### **🎯 Tối Ưu Hiệu Suất**
- **Hiệu suất vòng lặp**: `for` > `for...of` > `forEach` (Q34)
- **Thao tác DOM**: Gộp thay đổi, sử dụng `transform` cho animation (Q33)
- **Quản lý bộ nhớ**: Sử dụng WeakMap/WeakSet cho tham chiếu tạm thời (Q8)

### **🛡️ Ngăn Chặn Lỗi**
- **An toàn kiểu**: Luôn sử dụng `===` thay vì `==` (Q22)
- **An toàn null**: Sử dụng optional chaining `?.` và nullish coalescing `??` (Q25)
- **Strict Mode**: Bật để bắt lỗi tốt hơn (Q35)

### **🏗️ Patterns Kiến Trúc**
- **Module Pattern**: Sử dụng IIFE cho đóng gói (Q16)
- **Factory Pattern**: Sử dụng closure để tạo object (Q13)
- **Proxy Pattern**: Sử dụng cho validation và logging (Q36)

---

## **📚 Lộ Trình Học - Từ Junior Đến Senior**

### **🟢 Cấp Junior (Q1-Q15)**
**Tập trung**: Hiểu cơ bản, tránh lỗi thường gặp
- Cơ bản quản lý bộ nhớ
- Các loại hàm và phạm vi
- Thao tác DOM cơ bản
- Patterns async đơn giản

### **🟡 Cấp Mid (Q16-Q25)**
**Tập trung**: Patterns nâng cao, nhận thức hiệu suất
- Tối ưu xử lý sự kiện
- Kiểm tra kiểu và toán tử
- Kỹ thuật thao tác object
- Chiến lược xử lý lỗi

### **🔴 Cấp Senior (Q26-Q48)**
**Tập trung**: Kiến trúc, hiệu suất, khả năng bảo trì
- Patterns async nâng cao
- Khái niệm lập trình hàm
- Tối ưu rendering trình duyệt
- Kỹ thuật metaprogramming
- Lỗi thường gặp và cách tránh
- Bảo mật và lỗ hổng JavaScript
- Anti-patterns hiệu suất

---

## **🎯 Chiến Lược Phỏng Vấn**

### **🔥 Câu Hỏi Tác Động Cao (Phải Thành Thạo)**
1. **Event Loop & Async** (Q9-Q12) - Hiểu biết cốt lõi JavaScript
2. **Closure & Scope** (Q13) - Khái niệm hàm nâng cao
3. **this Binding** (Q15) - Hiểu biết context
4. **Promise Patterns** (Q26-Q27) - Xử lý async hiện đại
5. **Hiệu suất** (Q33-Q34) - Tư duy tối ưu

### **💼 Ứng Dụng Thực Tế**
- **Phát triển React**: Patterns bất biến, xử lý sự kiện, hiệu suất
- **Backend Node.js**: Patterns async, xử lý lỗi, quản lý bộ nhớ
- **Tối ưu trình duyệt**: Hiệu suất rendering, thao tác DOM
- **Kiến trúc code**: Module patterns, lập trình hàm
- **Bảo mật ứng dụng**: XSS, CSRF, input validation, secure coding
- **Debugging & Performance**: Memory leaks, anti-patterns, optimization

---

## **🚀 Bước Tiếp Theo - Học Liên Tục**

### **📖 Tài Nguyên Khuyến Nghị**
- **MDN Web Docs**: Tài liệu JavaScript chính thức
- **JavaScript.info**: Hướng dẫn JavaScript hiện đại toàn diện
- **You Don't Know JS**: Đi sâu vào nội bộ JavaScript
- **Functional-Light JavaScript**: Patterns lập trình hàm

### **🛠️ Dự Án Thực Hành**
- Xây dựng hệ thống sự kiện tùy chỉnh sử dụng closure
- Tạo HTTP client dựa trên promise với interceptors
- Triển khai virtual DOM với thuật toán diffing
- Phát triển thư viện quản lý state sử dụng proxy

---

## **🎯 Điểm Quan Trọng**

> **💡 Tư Duy Senior**: JavaScript không chỉ là ngôn ngữ, mà là một platform. Hiểu biết engine, runtime và browser APIs là quan trọng để xây dựng ứng dụng có thể mở rộng.

> **🔥 Hiệu Suất Trước Tiên**: Luôn xem xét tác động hiệu suất của lựa chọn code. Biết khi nào tối ưu và khi nào ưu tiên khả năng đọc.

> **🛡️ Lập Trình Phòng Thủ**: Viết code xử lý edge cases một cách duyên dáng. Sử dụng TypeScript, strict mode và xử lý lỗi đúng cách.

> **🏗️ Kiến Trúc Quan Trọng**: Chọn đúng patterns cho đúng vấn đề. Đừng over-engineer, nhưng cũng đừng under-engineer.

