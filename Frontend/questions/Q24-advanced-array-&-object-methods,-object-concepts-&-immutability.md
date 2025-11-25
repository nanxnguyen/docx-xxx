# 🛠️ Q24: Advanced Array & Object Methods, Object Concepts & Immutability

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"Advanced methods bao gồm flat/flatMap, Array.from, Object.entries/values/keys; Object concepts gồm prototype chain, Object.create, property descriptors; Immutability control với freeze/seal/preventExtensions."**

**🔑 3 Nhóm Chính:**

**1. Advanced Array Methods:**
- **`flat(depth)`**: Flatten nested arrays - `[1,[2,[3]]].flat(2)` → `[1,2,3]`
- **`flatMap(fn)`**: map + flatten (efficient hơn `.map().flat()`)
- **`Array.from(iterable, mapFn)`**: Tạo array từ iterable + optional map
  - Ví dụ: `Array.from({length: 5}, (_, i) => i)` → `[0,1,2,3,4]`
- **`entries/keys/values`**: Iterate index-value pairs

**2. Advanced Object Methods:**
- **`Object.entries(obj)`**: `{a:1, b:2}` → `[['a',1], ['b',2]]` (iterate objects)
- **`Object.fromEntries()`**: Ngược lại entries → object
- **`Object.values(obj)`**: Lấy một values (không cần keys)
- **`Object.assign(target, ...sources)`**: Shallow merge (mutate target)

**3. Object Concepts & Immutability:**
- **`Object.create(proto)`**: Tạo object với specific prototype (không inherit Object.prototype)
- **`Object.freeze(obj)`**: **Deep immutable** - không thể add/delete/modify properties
- **`Object.seal(obj)`**: Không add/delete nhưng **vẫn modify** được values
- **`Object.preventExtensions(obj)`**: Chỉ không add properties mới
- **Property Descriptors**: `Object.defineProperty()` - control writable, enumerable, configurable

**⚠️ Lỗi Thường Gặp:**
- `Object.freeze()` chỉ **shallow** → nested objects vẫn mutable (dùng deep-freeze libraries)
- `Object.assign()` **mutate target** → dùng `{...obj1, ...obj2}` cho immutable merge
- `.flat()` không specify depth → default = 1 (không flatten hết)
- Dùng `for...in` iterate object mà không check `hasOwnProperty` → iterate cả prototype

**💡 Kiến Thức Senior:**
- **Prototype chain**: `obj.__proto__` (deprecated) vs `Object.getPrototypeOf(obj)`
- **Mixins pattern**: `Object.assign(MyClass.prototype, Mixin1, Mixin2)` - share behavior
- **Property descriptors**: `{value, writable, enumerable, configurable}` - fine-grained control
  - `Object.keys()` chỉ lấy enumerable properties
- **Immutability libraries**: Immer (structural sharing), Immutable.js (persistent data structures)
- **Performance**: `Object.create(null)` nhanh hơn `{}` (không có prototype overhead)




**Trả lời:**

**Part 1: Advanced Array & Object Methods**
- **Advanced Array Methods**: flat, flatMap, from, of, entries, values, keys
- **Advanced Object Methods**: Object.assign, Object.entries, Object.values, Object.keys

**Part 2: Advanced Object Concepts**
- **Object.create()**: Tạo object với specific prototype
- **Prototype Chain**: Mechanism cho inheritance
- **Mixin Pattern**: Share functionality between objects
- **Object.freeze/seal/preventExtensions**: Control object mutability
- **Property Descriptors**: Fine-grained property control

**Ưu điểm**: Powerful manipulation, flexible inheritance, immutability control
**Nhược điểm**: Complex prototype chain, browser compatibility, learning curve

**Code Example:**

```typescript
// Array.flat() - Flatten nested arrays
const nestedArray = [1, [2, 3], [4, [5, 6]]];
const flattened = nestedArray.flat(); // [1, 2, 3, 4, [5, 6]]
const deeplyFlattened = nestedArray.flat(2); // [1, 2, 3, 4, 5, 6]

// Array.flatMap() - Map và flatten
const numbers = [1, 2, 3, 4];
const doubled = numbers.flatMap((n) => [n, n * 2]); // [1, 2, 2, 4, 3, 6, 4, 8]

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
    .flatMap((user) => user.hobbies || []) // Flatten hobbies
    .filter((hobby) => hobby.length > 3) // Filter long hobbies
    .map((hobby) => hobby.toUpperCase()); // Transform
}

function createLookupTable(objects: any[]): Map<string, any> {
  return new Map(
    objects.flatMap((obj) =>
      Object.entries(obj).map(([key, value]) => [key, obj])
    )
  );
}

function mergeObjects(...objects: any[]): any {
  return objects.reduce((acc, obj) => Object.assign(acc, obj), {});
}

function getObjectStats(obj: any): {
  keys: number;
  values: any[];
  entries: [string, any][];
} {
  return {
    keys: Object.keys(obj).length,
    values: Object.values(obj),
    entries: Object.entries(obj),
  };
}

// Advanced usage
function transformData(data: any[]): any[] {
  return data
    .flatMap((item) => item.items || []) // Flatten nested items
    .map((item) => ({
      ...item,
      processed: true,
      timestamp: Date.now(),
    }))
    .filter((item) => item.active);
}

function createIndexMap(data: any[]): Map<string, any[]> {
  const indexMap = new Map();

  data.forEach((item) => {
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

**Mistakes - Array Methods:**

```typescript
// ❌ Sai: Không hiểu flat depth
const nested = [1, [2, [3, [4]]]];
const flattened = nested.flat(); // [1, 2, [3, [4]]] - only 1 level

// ✅ Đúng: Specify depth
const deeplyFlattened = nested.flat(Infinity); // [1, 2, 3, 4]
```

**Part 2: Advanced Object Concepts - Prototype, Inheritance & Immutability**

**Code Example - Object.create() & Prototype Chain:**

```typescript
// Object.create() - Create object with specific prototype
const personPrototype = {
  greet(): string {
    return `Hello, I'm ${this.name}`;
  },
  getAge(): number {
    return this.age;
  },
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

Person.prototype.greet = function (): string {
  return `Hello, I'm ${this.name}`;
};

function Student(name: string, age: number, grade: string) {
  Person.call(this, name, age);
  this.grade = grade;
}

// Set up inheritance
Student.prototype = Object.create(Person.prototype);
Student.prototype.constructor = Student;

Student.prototype.study = function (): string {
  return `${this.name} is studying`;
};

const student = new Student('Jane', 20, 'A');
console.log(student.greet()); // "Hello, I'm Jane"
console.log(student.study()); // "Jane is studying"

// Mixin pattern
const canFly = {
  fly(): string {
    return `${this.name} is flying`;
  },
};

const canSwim = {
  swim(): string {
    return `${this.name} is swimming`;
  },
};

function mixin(target: any, ...sources: any[]): any {
  sources.forEach((source) => {
    Object.getOwnPropertyNames(source).forEach((name) => {
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
    city: 'HCM',
  },
});

// frozenObject.name = 'Jane'; // Error in strict mode
// frozenObject.address.city = 'HN'; // Still works (shallow freeze)

// Deep freeze function
function deepFreeze(obj: any): any {
  Object.getOwnPropertyNames(obj).forEach((prop) => {
    if (obj[prop] !== null && typeof obj[prop] === 'object') {
      deepFreeze(obj[prop]);
    }
  });
  return Object.freeze(obj);
}

const deeplyFrozen = deepFreeze({
  name: 'John',
  address: {
    city: 'HCM',
  },
});

// Object.seal() - Prevent adding/removing properties
const sealedObject = Object.seal({
  name: 'John',
  age: 30,
});

// sealedObject.name = 'Jane'; // OK
// sealedObject.city = 'HCM'; // Error in strict mode
// delete sealedObject.age; // Error in strict mode

// Object.preventExtensions() - Prevent adding properties
const nonExtensibleObject = Object.preventExtensions({
  name: 'John',
  age: 30,
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
  configurable: false,
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
  enumerable: false,
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
      acc[key] =
        typeof data[key] === 'object' ? deepFreeze(data[key]) : data[key];
      return acc;
    }, {} as any)
  );
}

function createMixin(...mixins: any[]): any {
  return function (target: any): any {
    mixins.forEach((mixin) => {
      Object.getOwnPropertyNames(mixin).forEach((name) => {
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
  },
});

function User(name: string) {
  this.name = name;
}

withLogging(User.prototype);

const user = new User('John');
user.log('Hello'); // "John: Hello"
```

**Best Practices - Combined:**

- **Array Methods**: Sử dụng flat() cho nested arrays, flatMap() cho map và flatten
- **Object Methods**: Sử dụng Object.entries() cho iteration, Object.assign() cho merging
- **Prototype**: Sử dụng Object.create() cho prototype-based inheritance
- **Mixins**: Sử dụng mixins cho functionality sharing
- **Immutability**: Sử dụng Object.freeze() cho immutability, Object.seal() cho controlled mutability
- **Property Descriptors**: Sử dụng proper property descriptors cho fine-grained control

**Mistakes - Object Concepts:**

```typescript
// ❌ Sai: Không hiểu shallow vs deep freeze
const obj = Object.freeze({ a: { b: 1 } });
obj.a.b = 2; // Still works!

// ✅ Đúng: Deep freeze
const obj = deepFreeze({ a: { b: 1 } });
obj.a.b = 2; // Error in strict mode
```

---
