# 🏛️ Q22: JavaScript Classes




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

