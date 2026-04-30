# Q23: Generator Functions & Async Generators

## Tóm Tắt Ngắn Gọn

**Generator function** là function có thể tạm dừng và chạy tiếp. Nó dùng cú pháp `function*` và `yield`.

Function bình thường chạy một mạch từ đầu đến cuối. Generator thì chạy đến `yield`, trả ra một giá trị, rồi dừng lại. Khi gọi `.next()`, nó chạy tiếp từ điểm vừa dừng.

**Async generator** là generator cho dữ liệu bất đồng bộ. Nó dùng `async function*`, có thể `await`, và được đọc bằng `for await...of`.

## 1. Generator Function Là Gì?

```ts
function* numbers() {
  yield 1;
  yield 2;
  yield 3;
}

const gen = numbers();

console.log(gen.next()); // { value: 1, done: false }
console.log(gen.next()); // { value: 2, done: false }
console.log(gen.next()); // { value: 3, done: false }
console.log(gen.next()); // { value: undefined, done: true }
```

Ý cần hiểu:

- `function*`: khai báo generator function.
- `yield`: tạm dừng function và trả về giá trị.
- `.next()`: cho generator chạy tiếp.
- Kết quả `.next()` luôn có dạng `{ value, done }`.
- `done: false` nghĩa là generator còn giá trị.
- `done: true` nghĩa là generator đã kết thúc.

Generator **không chạy ngay** khi được gọi. Nó chỉ chạy khi bạn gọi `.next()` hoặc iterate bằng `for...of`.

## 2. Dùng `for...of` Với Generator

Thay vì gọi `.next()` thủ công, có thể dùng `for...of`.

```ts
function* numbers() {
  yield 1;
  yield 2;
  yield 3;
}

for (const value of numbers()) {
  console.log(value);
}
```

Output:

```txt
1
2
3
```

Lưu ý: `for...of` chỉ lấy các giá trị `yield`. Nếu generator có `return`, giá trị `return` sẽ không được lặp qua.

```ts
function* demo() {
  yield 1;
  return 99;
}

for (const value of demo()) {
  console.log(value); // chỉ in 1
}
```

## 3. Generator Chỉ Dùng Được Một Lần

Một generator object sau khi chạy hết thì bị **exhausted**. Muốn lặp lại từ đầu, phải tạo generator mới.

```ts
function* numbers() {
  yield 1;
  yield 2;
}

const gen = numbers();

console.log([...gen]); // [1, 2]
console.log([...gen]); // []

console.log([...numbers()]); // [1, 2]
console.log([...numbers()]); // [1, 2]
```

## 4. `yield*` Là Gì?

`yield*` dùng để ủy quyền cho một iterable hoặc generator khác.

```ts
function* first() {
  yield 1;
  yield 2;
}

function* second() {
  yield 3;
  yield 4;
}

function* combined() {
  yield* first();
  yield* second();
  yield 5;
}

console.log([...combined()]); // [1, 2, 3, 4, 5]
```

Hiểu đơn giản: `yield* otherGenerator()` nghĩa là "lấy lần lượt tất cả giá trị từ generator kia".

## 5. Generator Có Thể Nhận Giá Trị Từ `.next(value)`

Generator không chỉ trả giá trị ra ngoài, nó còn có thể nhận giá trị từ bên ngoài khi resume.

```ts
function* askName() {
  const name = yield 'What is your name?';
  yield `Hello ${name}`;
}

const gen = askName();

console.log(gen.next().value); // "What is your name?"
console.log(gen.next('An').value); // "Hello An"
```

Lưu ý quan trọng: giá trị truyền vào `.next(value)` sẽ trở thành kết quả của biểu thức `yield` đang bị tạm dừng.

## 6. Async Generator Là Gì?

Async generator dùng khi mỗi giá trị cần xử lý bất đồng bộ, ví dụ fetch từng page API, đọc từng chunk file, nhận stream data.

```ts
async function* asyncNumbers() {
  yield 1;

  await delay(500);
  yield 2;

  await delay(500);
  yield 3;
}

function delay(ms: number) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function run() {
  for await (const value of asyncNumbers()) {
    console.log(value);
  }
}

run();
```

Ý cần nhớ:

- `async function*`: khai báo async generator.
- Bên trong có thể dùng `await`.
- Bên ngoài đọc bằng `for await...of`.
- Mỗi lần lặp có thể phải đợi Promise resolve.

## 7. Ví Dụ Thực Tế: Fetch API Theo Từng Trang

Async generator phù hợp khi API trả dữ liệu theo page và ta muốn xử lý từng page ngay khi có data.

```ts
type User = {
  id: string;
  name: string;
};

async function* fetchUsersByPage() {
  let page = 1;

  while (true) {
    const response = await fetch(`/api/users?page=${page}`);
    const users: User[] = await response.json();

    if (users.length === 0) {
      return;
    }

    yield users;
    page += 1;
  }
}

async function processUsers() {
  for await (const users of fetchUsersByPage()) {
    console.log('Processing page:', users);
  }
}
```

Lợi ích:

- Không cần load tất cả pages vào memory.
- Có page nào xử lý page đó.
- Phù hợp với data lớn, stream, pagination.

## 8. Khi Nào Nên Dùng Generator?

Nên dùng khi:

- Cần tạo data theo kiểu **lazy**: cần đến đâu tính đến đó.
- Cần lặp qua dãy có thể rất lớn hoặc vô hạn.
- Cần custom iterator.
- Cần compose nhiều iterator bằng `yield*`.
- Cần xử lý async stream/paginated data bằng async generator.

Không nên dùng khi:

- Chỉ cần map/filter/reduce array bình thường.
- Logic đơn giản, generator làm code khó đọc hơn.
- Team không quen với generator và không có use case rõ ràng.

## 9. Lỗi Thường Gặp

### Quên Dấu `*`

```ts
// Sai
function gen() {
  yield 1;
}

// Đúng
function* gen() {
  yield 1;
}
```

### Dùng Arrow Function Làm Generator

JavaScript không hỗ trợ generator arrow function.

```ts
// Sai
const gen = *() => {
  yield 1;
};

// Đúng
function* gen() {
  yield 1;
}
```

### Tưởng Generator Có Thể Lặp Lại Nhiều Lần

```ts
const gen = numbers();

console.log([...gen]); // có data
console.log([...gen]); // rỗng, vì đã chạy hết
```

### Quên `for await...of` Với Async Generator

```ts
// Sai
for (const value of asyncNumbers()) {
  console.log(value);
}

// Đúng
for await (const value of asyncNumbers()) {
  console.log(value);
}
```

## 10. Câu Trả Lời Phỏng Vấn

Có thể trả lời ngắn gọn:

> Generator là `function*` có thể pause/resume bằng `yield`. Khi gọi generator, nó trả về iterator; mỗi lần `.next()` sẽ chạy đến `yield` tiếp theo và trả `{ value, done }`. Generator hữu ích cho lazy iteration, custom iterator, infinite sequence và state machine. Async generator là biến thể bất đồng bộ, dùng `async function*` và được consume bằng `for await...of`, phù hợp với stream data hoặc paginated API.

## Key Takeaways

- `function*` tạo generator.
- `yield` tạm dừng và trả giá trị.
- `.next()` tiếp tục generator.
- Generator object chỉ iterate được một lần.
- `yield*` ủy quyền cho generator/iterable khác.
- `async function*` dùng cho async iteration.
- `for await...of` dùng để đọc async generator.
