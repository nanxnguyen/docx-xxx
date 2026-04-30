# 🔄 Q23: Generator Functions & Async Generators & Áp dụng Async Generator trong React

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"Generators (function\*) là functions có thể pause/resume execution với `yield`, trả về iterator. Async generators kết hợp với async/await cho lazy async iteration."**

**💡 Giải thích đơn giản:**

- **Generator** giống như một **"máy phát điện"** - bạn có thể bật/tắt bất cứ lúc nào, không cần chạy hết một lần
- **Function thường**: Chạy từ đầu đến cuối, không thể dừng giữa chừng
- **Generator**: Có thể **tạm dừng** (pause) tại `yield`, sau đó **tiếp tục** (resume) khi cần

**🔑 3 Khái Niệm Chính:**

**1. Generator Functions:**

- Syntax: `function* gen() { yield 1; yield 2; }`
  - 💡 Dấu `*` sau `function` là bắt buộc - đây là cách JavaScript biết đây là generator
- **Pause execution** tại `yield`, resume với `.next()`
  - 💡 `yield` = "Tạm dừng ở đây và trả về giá trị này"
  - 💡 `.next()` = "Tiếp tục chạy từ chỗ đã dừng"
- Return **Iterator object** `{value, done}`
  - 💡 `value`: Giá trị được yield ra
  - 💡 `done`: `false` = còn chạy, `true` = đã xong
- Lazy evaluation - chỉ compute khi `.next()` được gọi
  - 💡 Giống như **"máy bán hàng tự động"** - chỉ làm khi bạn bấm nút, không làm trước

**2. Generator Methods:**

- `.next(value)` - resume, pass value vào yield expression
  - 💡 Tiếp tục chạy và có thể truyền giá trị vào generator
- `.return(value)` - terminate generator, set done=true
  - 💡 Dừng generator ngay lập tức (giống như bấm nút dừng khẩn cấp)
- `.throw(error)` - throw error tại yield statement
  - 💡 Ném lỗi vào generator tại điểm đang pause
- `yield*` - delegate tới generator khác
  - 💡 "Ủy quyền" - để generator khác xử lý thay vì mình

**3. Async Generators:**

- Syntax: `async function* gen() { yield await fetch() }`
  - 💡 Kết hợp `async` + `function*` = có thể yield các Promise
- Iterate với **`for await...of`**
  - 💡 Dùng `for await...of` thay vì `for...of` để đợi Promise resolve
- Use case: stream data (paginated API, file reading chunks, SSE)
  - 💡 **Paginated API**: Lấy dữ liệu từng trang, không cần load hết
  - 💡 **File reading**: Đọc file từng chunk, tiết kiệm memory
  - 💡 **SSE (Server-Sent Events)**: Nhận dữ liệu real-time từ server

**⚠️ Lỗi Thường Gặp:**

- **Quên `*` trong `function*` → không phải generator**

  - ❌ `function gen() { yield 1; }` → Lỗi: "Unexpected token 'yield'"
  - ✅ `function* gen() { yield 1; }` → Đúng
  - 💡 Dấu `*` là bắt buộc, không có thì không phải generator

- **Dùng arrow functions → Không support generators**

  - ❌ `const gen = () =>* { yield 1; }` → Syntax error
  - ✅ `function* gen() { yield 1; }` → Đúng
  - 💡 Arrow functions không thể là generator vì không có `this` binding

- **Iterate generator nhiều lần → chỉ chạy 1 lần (exhausted)**

  - ❌
    ```typescript
    const gen = numberGenerator();
    for (const v of gen) {
    } // Chạy lần 1
    for (const v of gen) {
    } // Không chạy nữa (đã exhausted)
    ```
  - ✅ Phải tạo generator mới:
    ```typescript
    for (const v of numberGenerator()) {
    } // Chạy lần 1
    for (const v of numberGenerator()) {
    } // Chạy lần 2 (generator mới)
    ```
  - 💡 Generator giống như **"băng cassette"** - chạy hết rồi phải quay lại từ đầu, không thể rewind

- **`return` trong generator → set done=true nhưng `for...of` không nhận return value**
  - ❌ `for (const v of gen) { }` → Không nhận được giá trị return
  - ✅ Dùng `.next()` để lấy return value:
    ```typescript
    const gen = numberGenerator();
    let result = gen.next();
    while (!result.done) {
      console.log(result.value);
      result = gen.next();
    }
    console.log(result.value); // Giá trị return
    ```
  - 💡 `for...of` chỉ lấy các giá trị `yield`, bỏ qua `return`

**💡 Kiến Thức Senior:**

- **Use cases**:

  - **Infinite sequences** (Dãy số vô hạn):

    ```typescript
    function* fibonacci() {
      let [a, b] = [0, 1];
      while (true) yield ([a, b] = [b, a + b]);
    }
    ```

    - 💡 Tạo dãy số vô hạn mà không tốn memory (chỉ tính khi cần)
    - 💡 Giống như **"máy tính bỏ túi"** - chỉ tính khi bạn bấm nút

  - **Lazy evaluation** (Tính toán lười biếng):

    - 💡 Chỉ compute khi cần (memory efficient)
    - 💡 Ví dụ: Không cần tạo array 1 triệu phần tử, chỉ tạo khi cần dùng

  - **State machines** (Máy trạng thái):

    - 💡 Pause/resume cho complex flows
    - 💡 Ví dụ: Game có nhiều state (menu → playing → pause → game over)

  - **Co-routines** (Hợp tác):
    - 💡 Bi-directional communication (pass values vào `yield`)
    - 💡 Generator có thể nhận giá trị từ bên ngoài khi resume

- **Redux-Saga** dùng generators cho side effects management

  - 💡 Redux-Saga dùng generators để quản lý các side effects (API calls, timers, etc.)
  - 💡 Giúp code dễ đọc và test hơn so với thunks

- **Async iteration protocol**: `Symbol.asyncIterator` cho custom async iterables

  - 💡 Cho phép tạo custom async iterable objects
  - 💡 Giống như `Symbol.iterator` nhưng cho async operations

- **Generators không thể arrow functions** vì cần `this` binding
  - 💡 Arrow functions không có `this` riêng, nên không thể dùng làm generator

**⚡ Quick Summary:**

> Generator = function\* với yield. Pause/resume execution. Async generator = for await...of

**💡 Ghi Nhớ:**

- ⏸️ **function\***: Generator function với yield
- ▶️ **next()**: Resume execution, return {value, done}
- 🔄 **Async Gen**: async function\* với for await...of

**Trả lời:**

- **Generator Functions**: Functions có thể pause và resume execution

  - 💡 Giống như **"video player"** - có thể pause, play, rewind bất cứ lúc nào
  - 💡 Khác với function thường: chạy từ đầu đến cuối, không thể dừng

- **yield**: Keyword để pause function và return value

  - 💡 `yield` = "Tạm dừng ở đây, trả về giá trị này, đợi lệnh tiếp theo"
  - 💡 Giống như **"checkpoint"** trong game - lưu điểm và có thể quay lại

- **yield\***: Delegate to another generator

  - 💡 "Ủy quyền" cho generator khác xử lý
  - 💡 Giống như **"chuyển cuộc gọi"** - để người khác xử lý thay

- **Async Generators**: Generators với async/await support

  - 💡 Có thể yield các Promise, đợi chúng resolve
  - 💡 Dùng cho **data streaming** - lấy dữ liệu từng phần, không cần đợi hết

- **Ưu điểm**:

  - ✅ Memory efficient - chỉ tính toán khi cần
  - ✅ Lazy evaluation - không tạo data trước khi cần
  - ✅ Complex iteration - xử lý các vòng lặp phức tạp dễ dàng
  - ✅ Infinite sequences - tạo dãy số vô hạn mà không tốn memory

- **Nhược điểm**:
  - ❌ Complex syntax - cú pháp phức tạp hơn function thường
  - ❌ Not widely used - ít được dùng trong thực tế
  - ❌ Hard to debug - khó debug hơn function thường
  - ❌ Performance overhead - có overhead nhỏ so với function thường

**Code Example:**

```typescript
// ═══════════════════════════════════════════════════════════
// GENERATOR CƠ BẢN - Ví dụ đơn giản nhất
// ═══════════════════════════════════════════════════════════

// 💡 Generator function - có dấu * sau function
// 💡 yield = tạm dừng và trả về giá trị
function* numberGenerator(): Generator<number, void, unknown> {
  yield 1; // Tạm dừng, trả về 1
  yield 2; // Tiếp tục, tạm dừng, trả về 2
  yield 3; // Tiếp tục, tạm dừng, trả về 3
  return 4; // Giá trị cuối cùng (khi done = true)
}

// Tạo generator instance
const gen = numberGenerator();
// 💡 Generator không chạy ngay, chỉ chạy khi gọi .next()

console.log(gen.next()); // { value: 1, done: false }
// 💡 Lần 1: Chạy đến yield 1, tạm dừng, trả về {value: 1, done: false}

console.log(gen.next()); // { value: 2, done: false }
// 💡 Lần 2: Tiếp tục từ yield 1, chạy đến yield 2, tạm dừng

console.log(gen.next()); // { value: 3, done: false }
// 💡 Lần 3: Tiếp tục từ yield 2, chạy đến yield 3, tạm dừng

console.log(gen.next()); // { value: 4, done: true }
// 💡 Lần 4: Tiếp tục từ yield 3, chạy đến return, done = true

// ═══════════════════════════════════════════════════════════
// GENERATOR VỚI PARAMETERS - Nhận tham số như function thường
// ═══════════════════════════════════════════════════════════

// 💡 Generator có thể nhận parameters như function thường
function* counter(
  start: number, // Số bắt đầu
  end: number // Số kết thúc
): Generator<number, void, unknown> {
  for (let i = start; i <= end; i++) {
    yield i; // Yield từng số trong khoảng
  }
}

// Tạo generator với tham số
const counterGen = counter(1, 5);
// 💡 Generator tạo ra nhưng chưa chạy, chỉ chạy khi iterate

// Dùng for...of để iterate (dễ hơn dùng .next())
for (const value of counterGen) {
  console.log(value); // 1, 2, 3, 4, 5
  // 💡 for...of tự động gọi .next() và lấy value
}

// ═══════════════════════════════════════════════════════════
// YIELD* - Ủy quyền cho generator khác (Generator Composition)
// ═══════════════════════════════════════════════════════════

// 💡 yield* = "Ủy quyền" - để generator khác xử lý thay
// 💡 Giống như "chuyển cuộc gọi" trong điện thoại

function* generator1(): Generator<number, void, unknown> {
  yield 1;
  yield 2;
}

function* generator2(): Generator<number, void, unknown> {
  yield 3;
  yield 4;
}

// Generator kết hợp - dùng yield* để gọi generator khác
function* combinedGenerator(): Generator<number, void, unknown> {
  yield* generator1(); // Ủy quyền cho generator1 → yield 1, 2
  yield* generator2(); // Ủy quyền cho generator2 → yield 3, 4
  yield 5; // Tự yield 5
}

const combined = combinedGenerator();
console.log([...combined]); // [1, 2, 3, 4, 5]
// 💡 Spread operator [...] tự động iterate generator và tạo array

// ═══════════════════════════════════════════════════════════
// GENERATOR VỚI INPUT VALUES - Nhận giá trị từ bên ngoài
// ═══════════════════════════════════════════════════════════

// 💡 Generator có thể NHẬN giá trị từ bên ngoài khi resume
// 💡 Giống như "2 chiều" - vừa trả về, vừa nhận vào

function* inputGenerator(): Generator<number, void, number> {
  // yield 1 → trả về 1, đợi giá trị từ .next(value)
  let value = yield 1;
  console.log('Received:', value); // Nhận giá trị từ .next(10)

  // yield 2 → trả về 2, đợi giá trị từ .next(value)
  value = yield 2;
  console.log('Received:', value); // Nhận giá trị từ .next(20)

  return value; // Trả về giá trị cuối cùng
}

const inputGen = inputGenerator();

// Lần 1: Bắt đầu generator, yield 1
console.log(inputGen.next());
// { value: 1, done: false }
// 💡 Generator tạm dừng tại yield 1, đợi giá trị tiếp theo

// Lần 2: Truyền 10 vào generator (thay thế yield 1)
console.log(inputGen.next(10));
// Received: 10
// { value: 2, done: false }
// 💡 Giá trị 10 được gán vào biến value, sau đó yield 2

// Lần 3: Truyền 20 vào generator (thay thế yield 2)
console.log(inputGen.next(20));
// Received: 20
// { value: 20, done: true }
// 💡 Giá trị 20 được gán vào value, sau đó return value

// ═══════════════════════════════════════════════════════════
// ASYNC GENERATOR - Generator với async/await
// ═══════════════════════════════════════════════════════════

// 💡 Async Generator = Generator + Promise
// 💡 Có thể yield các Promise và đợi chúng resolve

async function* asyncNumberGenerator(): AsyncGenerator<number, void, unknown> {
  yield 1; // Yield giá trị đồng bộ

  // Đợi 1 giây trước khi yield tiếp
  await new Promise((resolve) => setTimeout(resolve, 1000));
  yield 2;

  // Đợi thêm 1 giây
  await new Promise((resolve) => setTimeout(resolve, 1000));
  yield 3;
}

// Dùng for await...of để iterate async generator
async function consumeAsyncGenerator(): Promise<void> {
  // 💡 for await...of tự động đợi Promise resolve
  for await (const value of asyncNumberGenerator()) {
    console.log('Async value:', value);
    // 💡 Mỗi lần lặp sẽ đợi Promise resolve
  }
}

consumeAsyncGenerator();
// Logs:
// Async value: 1 (ngay lập tức)
// Async value: 2 (sau 1 giây)
// Async value: 3 (sau 2 giây)

// ═══════════════════════════════════════════════════════════
// VÍ DỤ THỰC TẾ: DATA STREAMING - Lấy dữ liệu từng phần
// ═══════════════════════════════════════════════════════════

// 💡 Use case thực tế: Lấy dữ liệu từng chunk (ví dụ: paginated API)
// 💡 Giống như "xem video" - load từng phần, không cần load hết

async function* dataStream(): AsyncGenerator<string, void, unknown> {
  const data = ['chunk1', 'chunk2', 'chunk3'];

  for (const chunk of data) {
    // Giả lập delay khi fetch data (ví dụ: API call)
    await new Promise((resolve) => setTimeout(resolve, 500));

    // Yield từng chunk (không cần đợi tất cả data)
    yield chunk;
  }
}

async function processStream(): Promise<void> {
  // 💡 Xử lý từng chunk ngay khi nhận được, không cần đợi hết
  for await (const chunk of dataStream()) {
    console.log('Processing chunk:', chunk);
    // 💡 Có thể xử lý chunk ngay, không cần đợi các chunk khác
  }
}

// 💡 Lợi ích:
// - Memory efficient: Không cần lưu hết data trong memory
// - Faster: Xử lý ngay khi có data, không đợi hết
// - Better UX: Hiển thị data từng phần cho user

processStream();
// Output:
// Processing chunk: chunk1 (sau 0.5s)
// Processing chunk: chunk2 (sau 1s)
// Processing chunk: chunk3 (sau 1.5s)

// ═══════════════════════════════════════════════════════════
// GENERATOR CHO INFINITE SEQUENCES - Dãy số vô hạn
// ═══════════════════════════════════════════════════════════

// 💡 Generator có thể tạo dãy số vô hạn mà không tốn memory
// 💡 Chỉ tính toán khi cần, không tạo array trước

function* fibonacci(): Generator<number, void, unknown> {
  let a = 0, // Số Fibonacci đầu tiên
    b = 1; // Số Fibonacci thứ hai

  while (true) {
    yield a; // Trả về số Fibonacci hiện tại
    [a, b] = [b, a + b]; // Tính số Fibonacci tiếp theo
    // 💡 Destructuring assignment: a = b, b = a + b
  }
  // 💡 while(true) không bao giờ kết thúc, nhưng generator có thể dừng
}

const fib = fibonacci();
// 💡 Generator tạo ra nhưng chưa tính toán gì

console.log(fib.next().value); // 0 - Tính số đầu tiên
console.log(fib.next().value); // 1 - Tính số thứ hai
console.log(fib.next().value); // 1 - Tính số thứ ba
console.log(fib.next().value); // 2 - Tính số thứ tư
console.log(fib.next().value); // 3 - Tính số thứ năm

// 💡 Lợi ích:
// - Không tốn memory: Không tạo array 1 triệu phần tử
// - Lazy evaluation: Chỉ tính khi cần
// - Infinite: Có thể lấy bao nhiêu số cũng được
```

**Best Practices:**

- **Sử dụng generators cho lazy evaluation**

  - 💡 Khi cần tính toán lớn nhưng không cần hết ngay
  - 💡 Ví dụ: Infinite sequences, large datasets
  - ✅ Tốt: `function* bigData() { for (let i = 0; i < 1e9; i++) yield i; }`
  - ❌ Không tốt: `const arr = Array.from({length: 1e9}, (_, i) => i);` (tốn memory)

- **Sử dụng async generators cho data streaming**

  - 💡 Khi cần lấy dữ liệu từng phần (paginated API, file chunks)
  - 💡 Giúp app responsive hơn, không block UI
  - ✅ Tốt: `async function* fetchPages() { for (let page = 1; ; page++) yield await fetch(page); }`
  - ❌ Không tốt: `const allData = await Promise.all(pages.map(fetch));` (đợi hết mới xử lý)

- **Sử dụng yield\* cho generator composition**

  - 💡 Khi cần kết hợp nhiều generators
  - 💡 Code gọn hơn, dễ maintain
  - ✅ Tốt: `function* combined() { yield* gen1(); yield* gen2(); }`
  - ❌ Không tốt: `function* combined() { for (const v of gen1()) yield v; for (const v of gen2()) yield v; }`

- **Sử dụng for...of với generators**
  - 💡 Dễ đọc hơn dùng `.next()` thủ công
  - 💡 Tự động handle `done` flag
  - ✅ Tốt: `for (const value of generator()) { }`
  - ❌ Không tốt: `while (!gen.next().done) { }` (phức tạp hơn)

**Mistakes:**

```typescript
// ═══════════════════════════════════════════════════════════
// ❌ SAI: Không hiểu generator state (trạng thái của generator)
// ═══════════════════════════════════════════════════════════

const gen = numberGenerator();
console.log(gen.next()); // { value: 1, done: false }
console.log(gen.next()); // { value: 2, done: false }

// ❌ Lỗi: Cố gắng iterate lại generator đã exhausted
for (const value of gen) {
  console.log(value); // Chỉ in 3 (vì đã dùng 2 lần .next() rồi)
}

// ❌ Lỗi: Generator giống như "băng cassette" - chạy hết rồi phải quay lại từ đầu
// Không thể rewind, phải tạo generator mới

// ═══════════════════════════════════════════════════════════
// ✅ ĐÚNG: Hiểu generator state và tạo mới khi cần
// ═══════════════════════════════════════════════════════════

// Cách 1: Tạo generator mới mỗi lần cần
const gen1 = numberGenerator();
const values1 = [...gen1]; // [1, 2, 3]

const gen2 = numberGenerator(); // Generator mới
const values2 = [...gen2]; // [1, 2, 3] - Có thể dùng lại

// Cách 2: Dùng function để tạo generator mới
function getNumbers() {
  return numberGenerator(); // Mỗi lần gọi tạo generator mới
}

const values3 = [...getNumbers()]; // [1, 2, 3]
const values4 = [...getNumbers()]; // [1, 2, 3] - Generator mới

// 💡 Nhớ: Generator chỉ chạy 1 lần, sau đó exhausted
// 💡 Muốn dùng lại → Tạo generator mới
```
