# 🔄 Q23: Generator Functions & Async Generators & Áp dụng Async Generator trong React

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"Generators (function*) là functions có thể pause/resume execution với `yield`, trả về iterator. Async generators kết hợp với async/await cho lazy async iteration."**

**🔑 3 Khái Niệm Chính:**

**1. Generator Functions:**
- Syntax: `function* gen() { yield 1; yield 2; }`
- **Pause execution** tại `yield`, resume với `.next()`
- Return **Iterator object** `{value, done}`
- Lazy evaluation - chỉ compute khi `.next()` được gọi

**2. Generator Methods:**
- `.next(value)` - resume, pass value vào yield expression
- `.return(value)` - terminate generator, set done=true
- `.throw(error)` - throw error tại yield statement
- `yield*` - delegate tới generator khác

**3. Async Generators:**
- Syntax: `async function* gen() { yield await fetch() }`
- Iterate với **`for await...of`**
- Use case: stream data (paginated API, file reading chunks, SSE)

**⚠️ Lỗi Thường Gặp:**
- Quên `*` trong `function*` → không phải generator
- Dùng arrow functions → **Không support** generators (`() =>*` invalid)
- Iterate generator nhiều lần → chỉ chạy 1 lần (exhausted), phải tạo mới
- `return` trong generator → set done=true nhưng `for...of` không nhận return value

**💡 Kiến Thức Senior:**
- **Use cases**:
  - **Infinite sequences**: `function* fibonacci() { let [a,b]=[0,1]; while(true) yield [a,b]=[b,a+b] }`
  - **Lazy evaluation**: chỉ compute khi cện (memory efficient)
  - **State machines**: pause/resume cho complex flows
  - **Co-routines**: bi-directional communication (pass values vào `yield`)
- **Redux-Saga** dùng generators cho side effects management
- **Async iteration protocol**: `Symbol.asyncIterator` cho custom async iterables
- Generators **không thể arrow functions** vì cần `this` binding




**⚡ Quick Summary:**
> Generator = function* với yield. Pause/resume execution. Async generator = for await...of

**💡 Ghi Nhớ:**
- ⏸️ **function***: Generator function với yield
- ▶️ **next()**: Resume execution, return {value, done}
- 🔄 **Async Gen**: async function* với for await...of

**Trả lời:**

- **Generator Functions**: Functions có thể pause và resume execution
- **yield**: Keyword để pause function và return value
- **yield\***: Delegate to another generator
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
function* counter(
  start: number,
  end: number
): Generator<number, void, unknown> {
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
  await new Promise((resolve) => setTimeout(resolve, 1000));
  yield 2;
  await new Promise((resolve) => setTimeout(resolve, 1000));
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
    await new Promise((resolve) => setTimeout(resolve, 500));
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
  let a = 0,
    b = 1;
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
- Sử dụng yield\* cho generator composition
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

