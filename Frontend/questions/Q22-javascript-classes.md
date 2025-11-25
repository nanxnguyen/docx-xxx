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

