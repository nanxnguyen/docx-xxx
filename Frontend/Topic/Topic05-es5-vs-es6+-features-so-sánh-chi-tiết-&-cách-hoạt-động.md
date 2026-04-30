# Q03: ES5 vs ES6+ Features - So sánh chi tiết & cách hoạt động

## Tóm tắt phỏng vấn

**ES5** là JavaScript kiểu cũ, chủ yếu dùng `var`, function constructor, prototype, callback và không có module native.

**ES6+** là JavaScript hiện đại từ ES2015 trở đi, thêm `let/const`, arrow function, class, module, destructuring, spread/rest, Promise, async/await và nhiều API mới.

**Câu trả lời ngắn gọn:**

> ES6+ giúp code ngắn hơn, rõ scope hơn, xử lý async dễ đọc hơn và hỗ trợ module hoá tốt hơn. Tuy nhiên bản chất JavaScript vẫn là prototype-based, async vẫn dựa trên Promise/microtask, và khi hỗ trợ browser cũ cần phân biệt transpilation với polyfill.

## Bảng so sánh nhanh

| Chủ đề | ES5 | ES6+ |
| --- | --- | --- |
| Biến | `var`, function scope | `let/const`, block scope |
| Hoisting | `var` được init `undefined` | `let/const` có TDZ |
| Function | `function () {}` | Arrow `() => {}` |
| `this` | Dynamic, phụ thuộc cách gọi | Arrow dùng lexical `this` |
| OOP | Constructor function + prototype | `class`, `extends`, `super` |
| String | Nối chuỗi bằng `+` | Template literal `` `${}` `` |
| Object/Array | Gán thủ công, `Object.assign` | Destructuring, spread/rest |
| Async | Callback, callback hell | Promise, async/await |
| Module | IIFE, CommonJS, AMD | `import/export` |
| Collections | Object/Array là chính | `Map`, `Set`, `WeakMap`, `WeakSet` |
| Meta-programming | Hạn chế | `Symbol`, iterator, generator, `Proxy`, `Reflect` |
| Browser cũ | Hỗ trợ rộng | Có thể cần Babel/polyfill |

## Các thuật ngữ cần nắm

| Thuật ngữ | Hiểu nhanh |
| --- | --- |
| Scope | Phạm vi truy cập của biến |
| Function scope | Biến sống trong toàn bộ function, điển hình là `var` |
| Block scope | Biến chỉ sống trong cặp `{}`, điển hình là `let/const` |
| Hoisting | Engine xử lý khai báo trước khi chạy code |
| TDZ | Vùng không được đọc `let/const` trước dòng khai báo |
| Lexical this | `this` lấy từ scope nơi function được định nghĩa |
| Dynamic this | `this` phụ thuộc cách function được gọi |
| Prototype chain | Cơ chế tìm property/method từ object lên prototype cha |
| Transpile | Chuyển cú pháp mới về cú pháp cũ, ví dụ Babel |
| Polyfill | Thêm API runtime còn thiếu, ví dụ `Promise`, `Array.includes` |
| Shallow copy | Copy lớp ngoài, object lồng nhau vẫn chung reference |
| Iterable | Object có thể được duyệt bằng `for...of` nếu có `Symbol.iterator` |
| Microtask | Queue ưu tiên cao hơn macrotask, Promise/`await` resume chạy ở đây |

## ES2015-ES2023 đáng nhớ

- **ES2015/ES6**: `let/const`, arrow function, class, module, Promise, destructuring, spread/rest, `Map`, `Set`.
- **ES2016**: `Array.includes()`, toán tử `**`.
- **ES2017**: `async/await`, `Object.values()`, `Object.entries()`.
- **ES2018**: Object rest/spread, async iteration.
- **ES2019**: `Array.flat()`, `Array.flatMap()`, `Object.fromEntries()`.
- **ES2020**: Optional chaining `?.`, nullish coalescing `??`, `BigInt`, dynamic import.
- **ES2021**: `String.replaceAll()`, numeric separators `1_000_000`.
- **ES2022**: Private fields `#field`, top-level await, `Array.at()`.
- **ES2023**: `findLast()`, `toSorted()`, `toReversed()`, `toSpliced()`.

## 1. Variables: `var` vs `let/const`

Điểm quan trọng nhất: `var` là function scope và được hoist với giá trị `undefined`; `let/const` là block scope và có TDZ.

```typescript
function varExample() {
  console.log(x); // undefined
  var x = 10;

  if (true) {
    var x = 20; // cùng biến x ở function scope
  }

  console.log(x); // 20
}

function letConstExample() {
  // console.log(y); // ReferenceError: đang trong TDZ
  let y = 10;
  const z = 100;

  if (true) {
    let y = 20; // biến mới trong block
    const z = 200;
    console.log(y, z); // 20, 200
  }

  console.log(y, z); // 10, 100
}
```

**Nên nhớ:**

- Mặc định dùng `const`.
- Dùng `let` khi cần gán lại.
- Tránh `var` trong code hiện đại vì dễ gây bug do hoisting và redeclare.

### Hoisting & Temporal Dead Zone đầy đủ

Hoisting không có nghĩa là JavaScript thật sự "di chuyển code". Đúng hơn là trong **creation phase**, engine scan declarations và tạo binding trước; đến **execution phase** mới chạy từng dòng.

| Loại khai báo | Có hoisted? | Có initialized trước không? | Dùng trước dòng khai báo |
| --- | --- | --- | --- |
| `var` | Có | Có, bằng `undefined` | Được, trả `undefined` |
| `let` | Có | Không, nằm trong TDZ | `ReferenceError` |
| `const` | Có | Không, nằm trong TDZ | `ReferenceError` |
| Function declaration | Có | Có, toàn bộ function | Gọi được |
| Function expression với `var` | Biến được hoisted | `undefined` | Thường `TypeError` khi gọi |
| Function expression với `let/const` | Binding được hoisted | Không, nằm trong TDZ | `ReferenceError` |
| `class` | Có | Không, nằm trong TDZ | `ReferenceError` |

```typescript
// Function declaration: hoisted toàn bộ
sayHello(); // OK

function sayHello() {
  console.log('Hello');
}

// Function expression với var: chỉ biến được hoisted
// sayGoodbye(); // TypeError: sayGoodbye is not a function
var sayGoodbye = function () {
  console.log('Goodbye');
};

// Function expression với const: nằm trong TDZ
// sayHi(); // ReferenceError
const sayHi = () => console.log('Hi');

// Class cũng có TDZ
// const user = new User(); // ReferenceError
class User {}
```

TDZ bắt đầu từ đầu block scope đến dòng khai báo. Trong TDZ, kể cả `typeof` cũng không còn "safe".

```typescript
console.log(typeof undeclaredValue); // 'undefined'

{
  // console.log(typeof value); // ReferenceError
  let value = 1;
}
```

Các edge cases hay hỏi phỏng vấn:

```typescript
// 1. var trong loop dùng chung một binding
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0); // 3, 3, 3
}

// let trong loop tạo binding riêng cho mỗi iteration
for (let j = 0; j < 3; j++) {
  setTimeout(() => console.log(j), 0); // 0, 1, 2
}

// 2. Nested scope TDZ: inner binding che outer binding
let status = 'outer';
{
  // console.log(status); // ReferenceError, không đọc outer được
  let status = 'inner';
}

// 3. Default parameter cũng có thứ tự initialize
// function wrong(a = b, b = 1) {} // ReferenceError
function correct(a = 1, b = a) {
  return [a, b];
}
```

**Cách trả lời senior:** `var` được hoist và init `undefined`; `let/const/class` cũng được hoist nhưng chưa initialized nên nằm trong TDZ; function declaration được hoist cả thân function; function expression phụ thuộc biến chứa nó. TDZ tồn tại để bắt lỗi dùng biến trước khi khai báo.

## 2. Arrow function

Arrow function ngắn gọn và không có `this` riêng. Nó lấy `this` từ scope bên ngoài.

```typescript
const counter = {
  value: 0,

  incrementLater() {
    setTimeout(() => {
      this.value += 1; // this là counter
    }, 100);
  },
};
```

Không nên dùng arrow function làm object method nếu method cần `this` trỏ về object.

```typescript
const wrong = {
  value: 42,
  getValue: () => this.value, // sai: this không phải wrong
};

const correct = {
  value: 42,
  getValue() {
    return this.value;
  },
};
```

**Nên dùng arrow cho:** callback, `.map()`, `.filter()`, handler ngắn, function không cần `this` riêng.

**Tránh dùng arrow cho:** constructor, object method cần `this`, method cần `arguments`, method cần `super`.

## 3. Class và prototype

`class` không biến JavaScript thành class-based language như Java/C#. Nó là cú pháp dễ đọc hơn trên prototype chain.

```typescript
// ES5
function Animal(name) {
  this.name = name;
}

Animal.prototype.speak = function () {
  return this.name + ' makes a sound';
};

function Dog(name, breed) {
  Animal.call(this, name);
  this.breed = breed;
}

Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

Dog.prototype.speak = function () {
  return this.name + ' barks';
};

// ES6+
class ModernAnimal {
  constructor(public name: string) {}

  speak() {
    return `${this.name} makes a sound`;
  }
}

class ModernDog extends ModernAnimal {
  constructor(name: string, public breed: string) {
    super(name);
  }

  speak() {
    return `${this.name} barks`;
  }
}
```

**Bản chất:**

- Method trong class nằm trên `Constructor.prototype`, không copy vào từng instance.
- `extends` thiết lập prototype chain.
- `super()` gọi constructor của parent class.
- Private field `#field` là private thật ở runtime, khác convention `_field`.

## 4. Template literal

Template literal giúp nối chuỗi, viết multiline string và nhúng biểu thức dễ đọc hơn.

```typescript
const name = 'John';
const age = 25;

// ES5
const oldMessage = 'Hello ' + name + ', age ' + age;

// ES6+
const message = `Hello ${name}, age ${age}`;

const html = `
  <div class="user">
    <h2>${name}</h2>
    <p>Age: ${age}</p>
  </div>
`;
```

## 5. Destructuring

Destructuring là cú pháp rút giá trị từ object/array ra biến.

```typescript
const user = {
  name: 'John',
  age: 30,
  address: { city: 'Ha Noi' },
};

const { name, age } = user;
const {
  address: { city },
} = user;

const numbers = [1, 2, 3];
const [first, second] = numbers;

const { email = 'no-email@example.com' } = user;
```

**Lưu ý quan trọng:** default value chỉ dùng khi giá trị là `undefined`, không dùng khi là `null`.

```typescript
const data = { a: null, b: undefined };
const { a = 'A', b = 'B' } = data;

console.log(a); // null
console.log(b); // 'B'
```

## 6. Spread và rest

Cùng là cú pháp `...`, nhưng ý nghĩa phụ thuộc vị trí dùng.

```typescript
// Spread: trải ra
const arr1 = [1, 2];
const arr2 = [3, 4];
const merged = [...arr1, ...arr2]; // [1, 2, 3, 4]

const user = { name: 'John', age: 30 };
const updated = { ...user, age: 31 };

// Rest: gom lại
function sum(...numbers: number[]) {
  return numbers.reduce((total, n) => total + n, 0);
}

const [head, ...tail] = [1, 2, 3, 4];
const { name, ...profile } = user;
```

**Cẩn thận:** spread chỉ shallow copy.

```typescript
const original = { nested: { count: 1 } };
const copied = { ...original };

copied.nested.count = 99;
console.log(original.nested.count); // 99
```

Nếu cần deep copy, cân nhắc `structuredClone()`, `cloneDeep()` hoặc cách clone phù hợp với data.

## 7. Default parameters

ES5 thường dùng `||`, nhưng cách này sai với các giá trị falsy hợp lệ như `0`, `''`, `false`.

```typescript
function greetES5(name) {
  name = name || 'Guest'; // '' cũng bị đổi thành Guest
  return 'Hello ' + name;
}

function greetES6(name = 'Guest') {
  return `Hello ${name}`;
}

greetES6(undefined); // Hello Guest
greetES6(''); // Hello
```

Default parameter chỉ chạy khi argument là `undefined`.

## 8. Promise và async/await

Promise đại diện cho kết quả async trong tương lai. `async/await` là cú pháp dễ đọc hơn trên Promise.

```typescript
function fetchUser(id: string): Promise<{ id: string; name: string }> {
  return fetch(`/api/users/${id}`).then((res) => res.json());
}

async function loadUser() {
  try {
    const user = await fetchUser('123');
    return user;
  } catch (error) {
    console.error(error);
    throw error;
  }
}
```

### Sequential vs parallel

Khi các request không phụ thuộc nhau, dùng `Promise.all`.

```typescript
// Chậm: chạy tuần tự
const user = await fetchUser('1');
const posts = await fetchPosts('1');
const comments = await fetchComments('1');

// Nhanh hơn: chạy song song
const [user, posts, comments] = await Promise.all([
  fetchUser('1'),
  fetchPosts('1'),
  fetchComments('1'),
]);
```

### Promise combinators

| API | Ý nghĩa | Khi dùng |
| --- | --- | --- |
| `Promise.all()` | Tất cả fulfilled, một reject là reject ngay | Các tác vụ đều bắt buộc thành công |
| `Promise.allSettled()` | Chờ tất cả xong dù success/fail | Báo cáo kết quả từng task |
| `Promise.race()` | Lấy promise settle đầu tiên | Timeout hoặc lấy kết quả nhanh nhất |
| `Promise.any()` | Lấy fulfilled đầu tiên, bỏ qua reject | Fallback nhiều nguồn |

## 9. Modules

ES Modules dùng `import/export`, có module scope riêng và giúp bundler tree-shake tốt hơn.

```typescript
// math.ts
export const PI = 3.14159;

export function area(radius: number) {
  return PI * radius * radius;
}

export default class Circle {
  constructor(public radius: number) {}
}

// app.ts
import Circle, { area, PI } from './math';
import * as MathUtils from './math';

const module = await import('./heavy-module'); // dynamic import
```

**Nên nhớ:**

- Static import phải ở top-level, bundler phân tích được trước khi chạy.
- Dynamic import chạy runtime và trả về Promise, phù hợp cho code-splitting.
- Module được cache, import nhiều lần vẫn dùng cùng một instance.
- ES Modules dùng live binding: import là tham chiếu sống tới export.

## 10. Optional chaining và nullish coalescing

Hai cú pháp này rất hay gặp trong code frontend vì API response thường có field thiếu hoặc nullable.

```typescript
const user = {
  profile: {
    name: 'John',
    settings: null,
  },
};

// Optional chaining: tránh lỗi Cannot read properties of undefined/null
const theme = user.profile.settings?.theme;

// Nullish coalescing: chỉ fallback khi value là null hoặc undefined
const displayName = user.profile.name ?? 'Anonymous';
```

Khác biệt lớn giữa `??` và `||`:

```typescript
const count = 0;
const label1 = count || 10; // 10, vì 0 là falsy
const label2 = count ?? 10; // 0, vì 0 không phải null/undefined

const text = '';
const value1 = text || 'default'; // default
const value2 = text ?? 'default'; // ''
```

**Khi phỏng vấn:** nói rõ `?.` không thay thế validation. Nó chỉ giúp đọc property an toàn hơn. Nếu business logic yêu cầu field bắt buộc, vẫn phải validate và báo lỗi đúng.

## 11. Symbol, iterator và generator

### Symbol

`Symbol` tạo key unique, thường dùng cho protocol nội bộ của JavaScript như `Symbol.iterator`.

```typescript
const id = Symbol('id');

const user = {
  name: 'John',
  [id]: 123,
};

Object.keys(user); // ['name']
user[id]; // 123
```

`Symbol` hữu ích khi cần tránh đụng tên property, nhưng trong app frontend thông thường ít khi phải tự tạo nhiều.

### Iterator và `for...of`

Một object được xem là iterable nếu nó có method `[Symbol.iterator]()` trả về iterator.

```typescript
const range = {
  from: 1,
  to: 3,
  [Symbol.iterator]() {
    let current = this.from;
    const end = this.to;

    return {
      next() {
        if (current <= end) {
          return { value: current++, done: false };
        }
        return { value: undefined, done: true };
      },
    };
  },
};

for (const n of range) {
  console.log(n); // 1, 2, 3
}
```

### Generator

Generator là function có thể pause/resume bằng `yield`. Nó tạo iterator tự động.

```typescript
function* range(from: number, to: number) {
  for (let i = from; i <= to; i++) {
    yield i;
  }
}

for (const n of range(1, 3)) {
  console.log(n); // 1, 2, 3
}
```

Trong frontend hiện đại, generator ít dùng hơn `async/await`, nhưng vẫn đáng biết vì liên quan iterator, lazy sequence, Redux Saga và một số thư viện async cũ.

## 12. Proxy và Reflect

`Proxy` cho phép intercept thao tác trên object như get/set/delete. `Reflect` cung cấp API chuẩn để thực hiện lại thao tác gốc.

```typescript
const state = { count: 0 };

const proxy = new Proxy(state, {
  get(target, key, receiver) {
    console.log('read', key);
    return Reflect.get(target, key, receiver);
  },
  set(target, key, value, receiver) {
    console.log('write', key, value);
    return Reflect.set(target, key, value, receiver);
  },
});

proxy.count; // log read
proxy.count = 1; // log write
```

**Senior note:** Proxy rất mạnh nhưng có overhead và khó debug nếu lạm dụng. Vue 3 dùng Proxy cho reactivity; Immer cũng dựa vào proxy/draft để tạo immutable update tiện hơn.

## 13. Transpilation, polyfill và browser support

Đây là phần hay bị hỏi ở Senior Frontend vì liên quan production build.

| Khái niệm | Giải thích | Ví dụ |
| --- | --- | --- |
| Transpile | Đổi cú pháp mới thành cú pháp cũ | `class`, arrow, optional chaining qua Babel/TS |
| Polyfill | Thêm API runtime còn thiếu | `Promise`, `Array.includes`, `Object.fromEntries` |
| Ponyfill | Function thay thế không patch global | Import helper riêng thay vì sửa prototype |
| Browserslist | Khai báo browser target cho build tool | `last 2 versions`, `>0.5%`, `not dead` |

Ví dụ: Babel có thể đổi cú pháp optional chaining, nhưng nếu browser không có `Promise` hoặc `WeakMap` thì cần polyfill/runtime tương ứng.

```typescript
// Syntax cần transpile nếu target cũ
const city = user?.address?.city ?? 'Unknown';

// API cần polyfill nếu runtime cũ không hỗ trợ
Object.fromEntries(entries);
Array.prototype.includes.call(items, 'a');
```

**Cách trả lời phỏng vấn:**

- Babel/TypeScript chủ yếu xử lý syntax transform.
- Polyfill xử lý API runtime.
- Không nên import toàn bộ polyfill nếu chỉ cần một phần; cấu hình theo target để tránh tăng bundle size.
- Với evergreen browsers, thường dùng ES6+ trực tiếp và để build tool tối ưu theo Browserslist.

## Lỗi thường gặp

### 1. Dùng `var` trong modern code

```typescript
var name = 'John'; // tránh
const name = 'John'; // ưu tiên
let age = 25; // dùng khi cần reassign
```

### 2. Dùng arrow function sai chỗ

```typescript
const obj = {
  value: 42,
  getValue: () => this.value, // sai nếu cần this là obj
};
```

### 3. Quên `await`

```typescript
async function wrong() {
  const user = fetchUser('1');
  console.log(user.name); // user là Promise
}

async function correct() {
  const user = await fetchUser('1');
  console.log(user.name);
}
```

### 4. Await tuần tự không cần thiết

```typescript
// Nếu độc lập nhau, dùng Promise.all
const [a, b, c] = await Promise.all([fetchA(), fetchB(), fetchC()]);
```

### 5. Nhầm shallow copy với deep copy

```typescript
const copied = { ...original }; // chỉ copy level 1
```

### 6. Nhầm default export và named export

```typescript
import User from './user'; // default export
import { User } from './user'; // named export
```

### 7. Dùng `||` khi cần giữ `0`, `''`, `false`

```typescript
const pageSize = input.pageSize || 20; // sai nếu pageSize = 0 là giá trị hợp lệ
const safePageSize = input.pageSize ?? 20;
```

### 8. Tin rằng optional chaining thay validation

```typescript
const price = product?.price;

if (price == null) {
  throw new Error('Product price is required');
}
```

## Cơ chế bên dưới

### Hoisting và TDZ

- Khi tạo execution context, engine scan declarations trước.
- `var` được tạo và gán sẵn `undefined`.
- `let/const` cũng được biết trước, nhưng chưa được initialize.
- Khoảng từ đầu block đến dòng khai báo `let/const` là TDZ.
- Đọc biến trong TDZ gây `ReferenceError`, kể cả với `typeof`.

```typescript
console.log(typeof undeclaredVar); // 'undefined'

{
  // console.log(typeof x); // ReferenceError
  let x = 1;
}
```

### Arrow function và `this`

- Regular function có `this` riêng.
- `this` của regular function được quyết định lúc gọi.
- Arrow function không có `this` riêng.
- `call`, `apply`, `bind` không đổi được `this` của arrow function.

### Destructuring

- Destructuring gần như là cú pháp ngắn cho property/index access.
- Nested destructuring càng sâu thì càng nhiều lần access property.
- Performance khác biệt rất nhỏ, ưu tiên readability.
- Rest trong array tạo array mới bằng cơ chế tương tự `slice()`.

### Class

- `class` là syntactic sugar trên prototype.
- Instance method được share qua prototype.
- Static method nằm trên class/constructor.
- `extends` tạo prototype chain giữa child và parent.

### Modules

- Browser/bundler build module graph trước khi execute.
- Import/export tĩnh giúp tree-shaking.
- Dynamic import dùng khi cần lazy load.
- Circular dependency có thể hoạt động nhờ live binding, nhưng vẫn nên tránh thiết kế vòng phụ thuộc phức tạp.

### Async/await

- `async function` luôn trả về Promise.
- Mỗi `await` tạm dừng phần còn lại của function.
- Khi Promise settle, phần sau `await` được đưa vào microtask queue.
- `try/catch` trong async function tương đương xử lý Promise rejection.

Ví dụ thứ tự chạy:

```typescript
console.log('A');

setTimeout(() => console.log('B'), 0);

Promise.resolve().then(() => console.log('C'));

(async () => {
  await null;
  console.log('D');
})();

console.log('E');

// Output: A, E, C, D, B
```

Promise callback và phần sau `await` là microtask nên chạy trước `setTimeout` macrotask.

## Performance thực tế

Đừng tối ưu kiểu ES5 vs ES6+ một cách máy móc. Với frontend app thông thường, khác biệt giữa `var`/`let`, function/arrow, class/prototype thường không phải nguyên nhân chậm chính.

| Trường hợp | Khuyến nghị |
| --- | --- |
| Code thông thường | Ưu tiên readability và maintainability |
| Array/object rất lớn | Cẩn thận với spread vì tạo copy mới |
| Nhiều request độc lập | Dùng `Promise.all` thay vì await tuần tự |
| Hot path cực nặng | Benchmark thực tế trước khi tối ưu |
| Browser cũ | Dùng Babel cho syntax, polyfill cho API runtime |

## Best practices

1. Dùng `const` mặc định, `let` khi cần reassign.
2. Dùng arrow function cho callback, không dùng làm object method cần `this`.
3. Dùng destructuring khi giúp code dễ đọc, tránh destructuring quá sâu.
4. Dùng spread/rest cho immutable update, nhưng nhớ đó là shallow copy.
5. Dùng `async/await` cho flow tuần tự, `Promise.all` cho task độc lập.
6. Dùng ES Modules trong modern project.
7. Phân biệt transpilation và polyfill khi hỗ trợ browser cũ.
8. Đừng rewrite class về prototype chỉ vì performance nếu chưa benchmark.

## Checklist trả lời Senior Frontend

Khi được hỏi "ES5 khác ES6+ thế nào?", nên trả lời theo 5 lớp:

1. **Syntax/readability:** `let/const`, arrow, template literal, destructuring, spread/rest, class.
2. **Runtime behavior:** block scope, TDZ, lexical `this`, prototype chain, Promise/microtask.
3. **Architecture:** ES Modules, static import, tree-shaking, dynamic import/code splitting.
4. **Compatibility:** Babel/TypeScript cho syntax, polyfill cho API, Browserslist để kiểm soát target.
5. **Trade-off:** readability quan trọng hơn micro-optimization; cẩn thận shallow copy, await tuần tự, bundle size và API browser cũ.

Một câu trả lời tốt không chỉ liệt kê feature, mà giải thích được "feature đó thay đổi cách code chạy như thế nào" và "khi nào dùng sai sẽ gây bug gì".

---

# Q05: Set/Map, WeakSet/WeakMap, WeakRef & FinalizationRegistry

## Tóm tắt phỏng vấn

**Set/Map** là collections hiện đại của JavaScript. **WeakSet/WeakMap/WeakRef** dùng weak reference, nghĩa là không ngăn object bị garbage collected.

> Set dùng cho unique values. Map dùng cho key-value với key bất kỳ. WeakMap/WeakSet dùng khi muốn gắn metadata vào object mà không giữ object sống mãi. WeakRef và FinalizationRegistry là API nâng cao, không dùng cho core logic vì garbage collection không deterministic.

## Bảng so sánh

| API | Lưu gì | Key/value type | Iterable | Use case chính |
| --- | --- | --- | --- | --- |
| `Set` | Unique values | Bất kỳ value | Có | Dedupe, membership check |
| `Map` | Key-value pairs | Key bất kỳ type | Có | Cache, dictionary, ordered data |
| `WeakSet` | Object references | Chỉ object | Không | Track object tạm thời |
| `WeakMap` | Object key -> value | Key chỉ object | Không | Private data, metadata, cache theo object |
| `WeakRef` | Weak reference tới một object | Object | Không | Soft cache, observer nâng cao |
| `FinalizationRegistry` | Cleanup callback khi object bị GC | Object target | Không | Cleanup optional resource |

## Set

`Set` lưu unique values và check membership nhanh hơn `Array.includes()` khi dữ liệu lớn.

```typescript
const numbers = [1, 2, 2, 3, 3, 4];
const uniqueNumbers = [...new Set(numbers)]; // [1, 2, 3, 4]

const validIds = new Set([1, 5, 10]);
validIds.has(5); // true

const a = new Set([1, 2, 3]);
const b = new Set([3, 4, 5]);

const union = new Set([...a, ...b]); // 1,2,3,4,5
const intersection = new Set([...a].filter((x) => b.has(x))); // 3
const difference = new Set([...a].filter((x) => !b.has(x))); // 1,2
```

## Map

`Map` giống object dictionary nhưng key có thể là bất kỳ type nào, kể cả object/function.

```typescript
const userMap = new Map<string, { name: string; age: number }>();
userMap.set('user1', { name: 'John', age: 25 });

userMap.get('user1'); // { name: 'John', age: 25 }
userMap.has('user1'); // true
userMap.size; // 1

const objectKey = { id: 1 };
const cache = new Map<object, string>();
cache.set(objectKey, 'cached value');
cache.get(objectKey); // cached value
```

**Map vs Object:**

- Object key thường bị convert sang string/symbol.
- Map giữ insertion order rõ ràng.
- Map có `.size`, `.set()`, `.get()`, `.has()`, `.delete()`.
- Map phù hợp khi thêm/xoá nhiều hoặc key không phải string.

## WeakSet và WeakMap

Weak collections chỉ nhận object làm key/value chính và không ngăn garbage collection.

```typescript
const processed = new WeakSet<object>();

let node: HTMLElement | null = document.createElement('div');
processed.add(node);
processed.has(node); // true

node = null; // object có thể bị GC nếu không còn reference khác
```

`WeakMap` rất hợp để lưu metadata/private data theo object.

```typescript
const privateData = new WeakMap<object, { password: string }>();

class User {
  constructor(public username: string, password: string) {
    privateData.set(this, { password });
  }

  checkPassword(input: string) {
    return privateData.get(this)?.password === input;
  }
}
```

**Vì sao WeakMap không iterable và không có `.size`?**

Vì entry có thể biến mất bất kỳ lúc nào sau garbage collection. Nếu cho iterate hoặc đọc size, kết quả sẽ không ổn định.

## WeakRef

`WeakRef` giữ weak reference tới một object. Khi cần dùng object, gọi `.deref()`. Kết quả có thể là object hoặc `undefined`.

```typescript
let image: HTMLImageElement | null = new Image();
const ref = new WeakRef(image);

image = null;

const currentImage = ref.deref();
if (currentImage) {
  console.log('still alive');
} else {
  console.log('already garbage collected');
}
```

**Quy tắc:** luôn check kết quả của `.deref()`. Không dùng WeakRef cho logic bắt buộc phải chạy đúng.

## FinalizationRegistry

`FinalizationRegistry` cho phép đăng ký callback khi object bị garbage collected, nhưng callback không có thời điểm chạy đảm bảo.

```typescript
const registry = new FinalizationRegistry<string>((id) => {
  console.log(`Object ${id} was collected`);
});

let obj: object | null = { id: 1 };
registry.register(obj, 'object-1');

obj = null;
```

**Chỉ dùng cho cleanup phụ trợ**, ví dụ resource native, WASM memory, file handle hoặc cache bookkeeping. Không dùng cho business logic.

## Khi nào dùng gì?

| Nhu cầu | Nên dùng |
| --- | --- |
| Loại duplicate khỏi array | `Set` |
| Check một value có tồn tại không | `Set` |
| Dictionary với key là object/function | `Map` |
| Counting occurrences | `Map` |
| Metadata cho DOM node | `WeakMap` |
| Private data trước khi có `#private` | `WeakMap` |
| Track object đã xử lý mà không giữ sống object | `WeakSet` |
| Cache mềm có thể mất data khi GC | `WeakRef` |
| Cleanup optional sau GC | `FinalizationRegistry` |

## Lỗi thường gặp với collections

### 1. Dùng object thay Map khi key không phải string

```typescript
const obj: Record<string, string> = {};
obj[String({ id: 1 })] = 'value'; // key thành '[object Object]'

const map = new Map<object, string>();
const key = { id: 1 };
map.set(key, 'value');
```

### 2. Dùng primitive trong WeakMap/WeakSet

```typescript
const weakMap = new WeakMap();
// weakMap.set('id', 123); // TypeError

weakMap.set({ id: 1 }, 123); // OK
```

### 3. Iterate WeakMap/WeakSet

```typescript
const weakMap = new WeakMap<object, string>();
// for (const item of weakMap) {} // sai: WeakMap không iterable
```

### 4. Tin rằng WeakRef luôn còn object

```typescript
const value = ref.deref();
if (!value) {
  // fallback: fetch/rebuild lại data
}
```

### 5. Dựa vào FinalizationRegistry để chạy logic quan trọng

Garbage collection không deterministic. Callback có thể chạy muộn hoặc không chạy trước khi process kết thúc.

## Ghi nhớ senior

- `Set` và `Map` dùng thuật toán SameValueZero: gần giống `===`, nhưng `NaN` bằng `NaN`.
- `WeakMap` giúp tránh memory leak khi gắn metadata vào object/DOM node.
- Weak collections không enumerable vì GC có thể xoá entry bất kỳ lúc nào.
- `WeakRef` và `FinalizationRegistry` là API nâng cao, nên rất hiếm khi cần trong frontend app thông thường.
- Performance của `Set/Map` thường tốt cho lookup/add/delete nhiều, nhưng vẫn nên benchmark nếu dữ liệu rất lớn.

## References

- [ECMAScript 2015 Spec](https://www.ecma-international.org/ecma-262/6.0/)
- [TC39 Proposals](https://github.com/tc39/proposals)
- [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
- [MDN JavaScript Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference)
