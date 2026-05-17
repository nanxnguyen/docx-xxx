# 🔄 Topic03: Event Loop, Async Runtime & Deferring Execution

> Mục tiêu: hiểu chính xác JavaScript chạy code đồng bộ, async callback, Promise, render UI và các kỹ thuật trì hoãn execution trong frontend production.

---

## ⭐ Senior/Staff Summary

`Event Loop` là cơ chế giúp JavaScript xử lý async trong môi trường **single-threaded**:

- ✅ JavaScript chỉ có **một Call Stack chính** để chạy code JS.
- ✅ Việc async như `setTimeout`, DOM event, `fetch`, I/O không tự chạy trong JS engine; chúng được runtime như Browser/Node xử lý bên ngoài.
- ✅ Khi async hoàn tất, callback được đưa vào queue phù hợp.
- ✅ Event Loop chỉ đưa callback vào Call Stack khi stack đang trống.
- ✅ `Microtask Queue` có ưu tiên cao hơn `Macrotask/Task Queue`.
- ✅ Browser có thêm bước render: style, layout, paint, composite.
- ⚠️ Code đồng bộ nặng hoặc microtask vô hạn có thể chặn UI, event, timer và render.

Thứ tự mental model quan trọng:

```txt
Sync Call Stack
→ process.nextTick (Node.js only)
→ Microtasks: Promise.then / catch / finally, queueMicrotask, MutationObserver
→ Browser may render: requestAnimationFrame, style, layout, paint
→ One macrotask/task: setTimeout, setInterval, DOM event, I/O, MessageChannel...
→ Repeat
```

> 💡 Câu nhớ nhanh: **Sync chạy trước, microtask chạy hết, browser có cơ hội render, rồi mới tới một macrotask.**

---

## 🧠 Key Mental Model

Hãy nhìn JavaScript runtime như một hệ thống có nhiều phần:

- **Call Stack**
  - Nơi chạy code JS hiện tại.
  - LIFO: hàm gọi sau cùng được trả về trước.
  - Khi stack bận, UI event, timer callback, Promise callback đều chưa thể chạy.

- **Heap**
  - Vùng nhớ chứa object, array, function, closure.
  - Event Loop không quản lý memory trực tiếp, nhưng callback/closure có thể giữ reference gây memory leak.

- **Runtime APIs**
  - Browser: `setTimeout`, `fetch`, DOM events, `FileReader`, `IntersectionObserver`, `requestAnimationFrame`, `Web Workers`.
  - Node.js: timers, file I/O, network I/O, `setImmediate`, `process.nextTick`.

- **Microtask Queue**
  - Chứa việc nhỏ, ưu tiên cao, chạy ngay sau khi Call Stack trống.
  - Ví dụ: `Promise.then`, `queueMicrotask`, `MutationObserver`.
  - Event Loop sẽ chạy **hết tất cả microtasks** trước khi qua bước tiếp theo.

- **Macrotask / Task Queue**
  - Chứa task lớn hơn hoặc callback từ runtime.
  - Ví dụ: `setTimeout`, `setInterval`, DOM event, I/O, `MessageChannel`.
  - Event Loop thường lấy **một task** mỗi vòng.

- **Rendering Pipeline**
  - Browser không render khi Call Stack còn bận.
  - `requestAnimationFrame` chạy trước paint của frame tiếp theo.
  - Nếu JS task lâu hơn khoảng 16ms ở màn 60Hz, UI dễ bị jank.

---

## 📚 Main Concepts

### 1. Call Stack: nơi code đồng bộ chạy

`Call Stack` chỉ xử lý một việc tại một thời điểm.

```ts
function c() {
  console.log('c');
}

function b() {
  c();
  console.log('b');
}

function a() {
  b();
  console.log('a');
}

a();

// Output:
// c
// b
// a
```

Luồng stack:

```txt
push a()
  push b()
    push c()
    pop c()
  pop b()
pop a()
```

⚠️ Nếu recursion không có điều kiện dừng, stack sẽ đầy:

```ts
function loop(): void {
  loop();
}

// loop(); // ❌ RangeError: Maximum call stack size exceeded
```

> ✅ Senior key: Event Loop không cứu được code sync đang kẹt trong Call Stack. Muốn UI phản hồi, phải chia nhỏ work hoặc đưa ra thread khác.

---

### 2. Web APIs / Node APIs: async không nằm trong JS engine thuần

Ví dụ `setTimeout`:

```ts
console.log('start');

setTimeout(() => {
  console.log('timer');
}, 0);

console.log('end');

// Output:
// start
// end
// timer
```

Giải thích:

- `console.log('start')` chạy sync.
- `setTimeout` đăng ký timer với Browser/Node runtime.
- Callback chưa chạy ngay, dù delay là `0`.
- `console.log('end')` chạy sync.
- Khi stack trống và microtask xong, Event Loop mới lấy timer callback.

Các API runtime thường gặp:

- `setTimeout`, `setInterval`: timer callback.
- DOM events: click, input, scroll, resize.
- `fetch`: network request, Promise resolution vào microtask.
- `FileReader`: đọc file từ input.
- `IntersectionObserver`: detect element vào viewport.
- `Geolocation`: lấy vị trí người dùng.
- `Web Workers`: chạy JS ở thread khác.
- Node.js I/O: file system, network, database driver.

---

### 3. Microtask Queue: ưu tiên cao

Microtask chạy sau sync code và trước task/timer thông thường.

Nguồn microtask phổ biến:

- `Promise.then`
- `Promise.catch`
- `Promise.finally`
- `queueMicrotask`
- `MutationObserver`
- `await` continuation
- Node.js: `process.nextTick` có priority đặc biệt, cao hơn Promise microtasks trong Node.

```ts
console.log('1 sync');

Promise.resolve().then(() => {
  console.log('2 promise microtask');
});

queueMicrotask(() => {
  console.log('3 queueMicrotask');
});

console.log('4 sync');

// Output:
// 1 sync
// 4 sync
// 2 promise microtask
// 3 queueMicrotask
```

✅ Dùng microtask khi:

- Cần chạy sau đoạn code sync hiện tại.
- Cần batch nhiều update trong cùng tick.
- Cần normalize API sync/async.

⚠️ Không dùng microtask cho work nặng hoặc vòng lặp dài vì browser chưa có cơ hội render.

---

### 4. Promise chain cũng là nhiều microtasks

```ts
Promise.resolve()
  .then(() => {
    console.log('A');
  })
  .then(() => {
    console.log('B');
  });

Promise.resolve().then(() => {
  console.log('C');
});

console.log('D');

// Output:
// D
// A
// C
// B
```

Vì sao `C` trước `B`?

- `.then(A)` được queue trước.
- `.then(B)` chỉ được queue sau khi `A` chạy xong.
- `.then(C)` đã có trong queue trước khi `B` được tạo.

> 💡 Key phỏng vấn: Promise chain không chạy nguyên một mạch như sync code. Mỗi `.then` là một microtask mới.

---

### 5. `queueMicrotask` vs `Promise.resolve().then`

Hai cách này đều đưa callback vào microtask queue:

```ts
queueMicrotask(() => {
  console.log('microtask');
});

Promise.resolve().then(() => {
  console.log('promise microtask');
});
```

Khác nhau thực tế:

- `queueMicrotask`
  - ✅ API trực tiếp cho microtask.
  - ✅ Không cần tạo Promise để thể hiện intent.
  - ⚠️ Error throw trong callback behave như exception async/report error.

- `Promise.resolve().then`
  - ✅ Phổ biến, tương thích tốt.
  - ✅ Error trở thành rejected Promise.
  - ⚠️ Dễ bị hiểu nhầm là đang làm async network/data flow.

Senior guideline:

- Dùng `queueMicrotask` cho batching nội bộ của library/app.
- Dùng Promise khi đang ở flow Promise thật sự.

---

### 6. Macrotask / Task Queue: timer, event, I/O

Macrotask có priority thấp hơn microtask.

Ví dụ:

```ts
setTimeout(() => console.log('timeout 1'), 0);
setTimeout(() => console.log('timeout 2'), 0);

Promise.resolve().then(() => console.log('promise'));

console.log('sync');

// Output:
// sync
// promise
// timeout 1
// timeout 2
```

Nguồn task phổ biến:

- `setTimeout`
- `setInterval`
- DOM events như `click`, `input`, `scroll`
- Network/I/O callback tùy runtime
- `MessageChannel`
- Node.js `setImmediate`

✅ Dùng macrotask khi:

- Muốn nhường browser render/input giữa các chunks.
- Muốn tách một phần work sang tick sau.
- Muốn tránh microtask starvation.

---

### 7. Browser rendering pipeline

Browser không paint khi JS đang chiếm Call Stack.

Một frame thường có các bước:

```txt
Input events
→ JS task
→ Microtasks
→ requestAnimationFrame callbacks
→ Style recalculation
→ Layout
→ Paint
→ Composite
```

Các thuật ngữ cần nắm:

- **Style recalculation**: tính CSS cuối cùng cho element.
- **Layout / Reflow**: tính kích thước và vị trí.
- **Paint**: vẽ pixels.
- **Composite**: ghép layer lên màn hình.

⚠️ Nếu đọc/ghi layout lẫn lộn nhiều lần:

```ts
// ❌ Có thể gây layout thrashing
items.forEach((el) => {
  const height = el.offsetHeight;
  el.style.height = `${height + 10}px`;
});
```

Tốt hơn:

```ts
// ✅ Batch read trước, write sau
const heights = items.map((el) => el.offsetHeight);

items.forEach((el, index) => {
  el.style.height = `${heights[index] + 10}px`;
});
```

---

### 8. `requestAnimationFrame`: chạy trước paint

`requestAnimationFrame` phù hợp cho animation/DOM visual updates vì browser gọi callback trước frame paint.

```ts
let start: number | null = null;

function animate(timestamp: number) {
  start ??= timestamp;

  const elapsed = timestamp - start;
  const progress = Math.min(elapsed / 300, 1);

  box.style.transform = `translateX(${progress * 200}px)`;

  if (progress < 1) {
    requestAnimationFrame(animate);
  }
}

requestAnimationFrame(animate);
```

✅ Dùng `requestAnimationFrame` cho:

- Animation.
- DOM read/write gắn với frame.
- Canvas update.
- Scroll-linked visual effect, nếu thật sự cần JS.

❌ Không dùng `setTimeout(fn, 16)` để làm animation chính; nó không đồng bộ chính xác với refresh rate và tab visibility.

---

### 9. `requestIdleCallback`: chạy khi browser rảnh

`requestIdleCallback` dùng cho việc không critical:

- prefetch nhẹ
- analytics
- warm cache
- background cleanup
- serialize dữ liệu không gấp

```ts
type IdleCallback = (deadline: IdleDeadline) => void;

function scheduleIdle(callback: IdleCallback, timeout = 2000): void {
  if ('requestIdleCallback' in window) {
    window.requestIdleCallback(callback, { timeout });
    return;
  }

  setTimeout(() => {
    callback({
      didTimeout: true,
      timeRemaining: () => 0,
    } as IdleDeadline);
  }, 1);
}

scheduleIdle((deadline) => {
  while (deadline.timeRemaining() > 0 && tasks.length > 0) {
    runBackgroundTask(tasks.shift()!);
  }
});
```

⚠️ Không dùng `requestIdleCallback` cho:

- render UI quan trọng
- response cho user input
- validation cần phản hồi ngay
- security/auth flow

---

### 10. Node.js Event Loop khác Browser

Browser có render pipeline. Node.js không có UI render nhưng có event loop phases.

Các phase chính trong Node.js:

- **timers**: `setTimeout`, `setInterval`.
- **pending callbacks**: một số system callbacks.
- **idle/prepare**: internal.
- **poll**: I/O callbacks.
- **check**: `setImmediate`.
- **close callbacks**: socket close.

Priority cần nhớ trong Node:

```txt
sync code
→ process.nextTick queue
→ Promise microtasks
→ event loop phases
```

Ví dụ:

```ts
console.log('sync');

setTimeout(() => console.log('timeout'), 0);
setImmediate(() => console.log('immediate'));

Promise.resolve().then(() => console.log('promise'));
process.nextTick(() => console.log('nextTick'));

// Node.js thường:
// sync
// nextTick
// promise
// timeout/immediate order có thể phụ thuộc context
```

⚠️ `process.nextTick` lạm dụng có thể starve Promise và I/O.

---

### 11. `async/await` hoạt động với microtask

Code trước `await` chạy sync. Code sau `await` được resume qua microtask.

```ts
async function run() {
  console.log('2 before await');
  await Promise.resolve();
  console.log('4 after await');
}

console.log('1 start');
run();
Promise.resolve().then(() => console.log('5 promise'));
console.log('3 end');

// Output:
// 1 start
// 2 before await
// 3 end
// 4 after await
// 5 promise
```

Giải thích:

- `run()` chạy ngay tới trước `await`.
- `await Promise.resolve()` tạm dừng function.
- Phần sau `await` được queue như microtask.
- Microtask nào được queue trước thì chạy trước.

> ⚠️ Thứ tự giữa `await` continuation và Promise callback phụ thuộc thời điểm queue. Đừng viết logic production dựa trên thứ tự tinh vi nếu có thể tránh.

---

### 12. Microtask starvation

Microtask queue phải trống trước khi browser có thể qua task/render tiếp theo.

```ts
function starve(): void {
  queueMicrotask(() => {
    // ❌ Tạo microtask mới mãi mãi
    starve();
  });
}

// starve(); // UI freeze

setTimeout(() => {
  console.log('never reached');
}, 0);
```

Fix bằng cách yield qua macrotask hoặc chunking:

```ts
function processInChunks<T>(
  items: T[],
  processItem: (item: T) => void,
  chunkSize = 500
): void {
  let index = 0;

  function runChunk() {
    const end = Math.min(index + chunkSize, items.length);

    while (index < end) {
      processItem(items[index]);
      index += 1;
    }

    if (index < items.length) {
      setTimeout(runChunk, 0); // ✅ cho browser cơ hội render/input
    }
  }

  runChunk();
}
```

---

### 13. Deferring execution: chọn đúng kỹ thuật

Các kỹ thuật trì hoãn execution nên hiểu theo mục tiêu:

- **`queueMicrotask`**
  - Dùng cho batch logic nhỏ ngay sau sync code.
  - Ví dụ: gom nhiều update trước khi emit event.

- **`setTimeout(fn, 0)`**
  - Dùng để chuyển work sang task sau.
  - Cho browser cơ hội xử lý input/render giữa các task.

- **`MessageChannel`**
  - Dùng để schedule task nhanh hơn timer trong một số scheduler.
  - Hay gặp trong scheduler/polyfill nội bộ.

- **`requestAnimationFrame`**
  - Dùng cho visual update trước paint.

- **`requestIdleCallback`**
  - Dùng cho background work không critical.

- **`debounce`**
  - Dùng khi chỉ muốn chạy sau khi user ngừng thao tác.
  - Ví dụ: search input, resize recalculation.

- **`throttle`**
  - Dùng khi muốn giới hạn tần suất chạy.
  - Ví dụ: scroll tracking, drag, resize.

- **`IntersectionObserver`**
  - Tốt hơn scroll listener cho lazy loading/visibility tracking.

- **`Web Worker`**
  - Dùng cho CPU-heavy computation thật sự.

- **`scheduler.postTask`**
  - API mới hơn để schedule task theo priority ở browser hỗ trợ.
  - Cần feature detect, không assume có ở mọi browser.

---

## 🧪 Practical TypeScript/JavaScript Examples

### Example 1: Thứ tự kinh điển

```ts
console.log('1');

setTimeout(() => console.log('2 timeout'), 0);

Promise.resolve().then(() => console.log('3 promise'));

queueMicrotask(() => console.log('4 microtask'));

console.log('5');

// Output:
// 1
// 5
// 3 promise
// 4 microtask
// 2 timeout
```

Key:

- Sync: `1`, `5`.
- Microtasks theo FIFO: Promise rồi `queueMicrotask`.
- Timer là macrotask nên chạy sau.

---

### Example 2: Nested microtask

```ts
Promise.resolve().then(() => {
  console.log('A');

  queueMicrotask(() => {
    console.log('B');
  });
});

Promise.resolve().then(() => {
  console.log('C');
});

setTimeout(() => {
  console.log('D');
}, 0);

// Output:
// A
// C
// B
// D
```

Vì `B` được queue trong lúc `A` đang chạy, còn `C` đã nằm trong queue trước đó.

---

### Example 3: Batching bằng microtask

Frontend scenario: dashboard nhận nhiều update trong cùng một tick, chỉ muốn render một lần.

```ts
type PriceUpdate = {
  symbol: string;
  price: number;
};

class PriceBoard {
  private pending = new Map<string, PriceUpdate>();
  private scheduled = false;

  receive(update: PriceUpdate): void {
    this.pending.set(update.symbol, update);

    if (this.scheduled) return;

    this.scheduled = true;

    queueMicrotask(() => {
      this.flush();
    });
  }

  private flush(): void {
    const updates = Array.from(this.pending.values());

    this.pending.clear();
    this.scheduled = false;

    this.render(updates);
  }

  private render(updates: PriceUpdate[]): void {
    console.log('render once:', updates);
  }
}
```

✅ Lợi ích:

- 100 updates sync có thể thành 1 render.
- Giảm reflow/repaint.
- Pattern tương tự batching trong UI frameworks.

⚠️ Nếu update đến liên tục qua nhiều task khác nhau, vẫn cần strategy khác như debounce/throttle/windowing.

---

### Example 4: Heavy work phải chia nhỏ

```ts
type Row = {
  id: string;
  value: number;
};

function normalizeRows(rows: Row[]): Promise<Map<string, Row>> {
  const result = new Map<string, Row>();
  let index = 0;

  return new Promise((resolve) => {
    function work() {
      const deadline = performance.now() + 8;

      while (index < rows.length && performance.now() < deadline) {
        const row = rows[index];
        result.set(row.id, row);
        index += 1;
      }

      if (index < rows.length) {
        setTimeout(work, 0);
        return;
      }

      resolve(result);
    }

    work();
  });
}
```

✅ Ý tưởng:

- Mỗi chunk chạy khoảng 8ms.
- Browser còn thời gian handle input/render.
- Tốt hơn một vòng loop sync dài 200ms.

🔥 Nếu data cực lớn hoặc CPU-heavy, cân nhắc `Web Worker`.

---

### Example 5: Debounce search + AbortController

Search input thường cần `debounce` và cancel request cũ để tránh race condition.

```ts
function debounce<TArgs extends unknown[]>(
  fn: (...args: TArgs) => void,
  delay: number
) {
  let timer: ReturnType<typeof setTimeout> | undefined;

  return (...args: TArgs) => {
    if (timer) clearTimeout(timer);

    timer = setTimeout(() => {
      fn(...args);
    }, delay);
  };
}

function createSearch() {
  let controller: AbortController | undefined;

  return debounce(async (keyword: string) => {
    controller?.abort();
    controller = new AbortController();

    const response = await fetch(`/api/search?q=${encodeURIComponent(keyword)}`, {
      signal: controller.signal,
    });

    const data = await response.json();
    console.log(data);
  }, 300);
}

const search = createSearch();

input.addEventListener('input', (event) => {
  const target = event.target as HTMLInputElement;
  search(target.value);
});
```

Key production:

- ✅ Debounce giảm số request.
- ✅ `AbortController` tránh response cũ ghi đè response mới.
- ⚠️ Vẫn cần handle `AbortError` trong app thật.

---

### Example 6: Throttle scroll + passive listener

```ts
function throttle<TArgs extends unknown[]>(
  fn: (...args: TArgs) => void,
  interval: number
) {
  let lastRun = 0;
  let trailingTimer: ReturnType<typeof setTimeout> | undefined;

  return (...args: TArgs) => {
    const now = Date.now();
    const remaining = interval - (now - lastRun);

    if (remaining <= 0) {
      if (trailingTimer) clearTimeout(trailingTimer);
      trailingTimer = undefined;
      lastRun = now;
      fn(...args);
      return;
    }

    if (!trailingTimer) {
      trailingTimer = setTimeout(() => {
        lastRun = Date.now();
        trailingTimer = undefined;
        fn(...args);
      }, remaining);
    }
  };
}

const onScroll = throttle(() => {
  console.log(window.scrollY);
}, 100);

window.addEventListener('scroll', onScroll, { passive: true });
```

✅ `passive: true` nói với browser rằng handler không gọi `preventDefault`, giúp scroll mượt hơn.

⚠️ Với lazy loading image/section, ưu tiên `IntersectionObserver` hơn scroll throttle.

---

### Example 7: IntersectionObserver cho lazy loading

```ts
const observer = new IntersectionObserver(
  (entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;

      const image = entry.target as HTMLImageElement;
      const src = image.dataset.src;

      if (src) {
        image.src = src;
        image.removeAttribute('data-src');
      }

      observer.unobserve(image);
    }
  },
  {
    rootMargin: '200px',
  }
);

document.querySelectorAll<HTMLImageElement>('img[data-src]').forEach((image) => {
  observer.observe(image);
});
```

✅ Browser tối ưu visibility tracking tốt hơn tự nghe mọi scroll event.

---

### Example 8: React animation bằng `requestAnimationFrame`

```tsx
import { useEffect, useRef, useState } from 'react';

export function ProgressBar() {
  const [progress, setProgress] = useState(0);
  const frameRef = useRef<number | null>(null);
  const startRef = useRef<number | null>(null);

  useEffect(() => {
    function animate(timestamp: number) {
      startRef.current ??= timestamp;

      const elapsed = timestamp - startRef.current;
      const nextProgress = Math.min(elapsed / 1000, 1);

      setProgress(nextProgress);

      if (nextProgress < 1) {
        frameRef.current = requestAnimationFrame(animate);
      }
    }

    frameRef.current = requestAnimationFrame(animate);

    return () => {
      if (frameRef.current !== null) {
        cancelAnimationFrame(frameRef.current);
      }
    };
  }, []);

  return <div style={{ transform: `scaleX(${progress})` }} />;
}
```

Production notes:

- ✅ Cleanup trong `useEffect` để tránh update sau unmount.
- ⚠️ `setState` mỗi frame có thể đắt nếu component tree lớn.
- ✅ Với animation đơn giản, CSS transition/animation thường tốt hơn JS.

---

### Example 9: `MessageChannel`

```ts
const channel = new MessageChannel();

channel.port1.onmessage = () => {
  console.log('message channel task');
};

console.log('sync');

setTimeout(() => {
  console.log('timeout');
}, 0);

Promise.resolve().then(() => {
  console.log('promise');
});

channel.port2.postMessage(null);

// Thường thấy:
// sync
// promise
// message channel task
// timeout
```

⚠️ Đừng dùng order của từng task source như contract tuyệt đối giữa mọi browser. Dùng `MessageChannel` khi bạn đang viết scheduler/library hoặc cần fallback có kiểm soát.

---

### Example 10: Web Worker cho CPU-heavy work

Main thread:

```ts
const worker = new Worker(new URL('./normalize.worker.ts', import.meta.url), {
  type: 'module',
});

worker.postMessage({ rows });

worker.onmessage = (event: MessageEvent<{ count: number }>) => {
  console.log('done:', event.data.count);
};
```

Worker:

```ts
self.onmessage = (event: MessageEvent<{ rows: Array<{ id: string }> }>) => {
  const count = event.data.rows.length;

  self.postMessage({ count });
};
```

✅ Dùng worker khi:

- parse dữ liệu lớn
- sort/filter dataset lớn
- encode/decode
- image/canvas processing
- crypto/compression phía client

⚠️ Chi phí `postMessage`/serialize cũng đáng kể. Không đưa mọi việc nhỏ vào worker.

---

### Example 11: `scheduler.postTask` với feature detection

```ts
type TaskPriority = 'user-blocking' | 'user-visible' | 'background';

function postTask(callback: () => void, priority: TaskPriority = 'user-visible') {
  const scheduler = globalThis.scheduler as
    | { postTask: (cb: () => void, options?: { priority: TaskPriority }) => void }
    | undefined;

  if (scheduler?.postTask) {
    scheduler.postTask(callback, { priority });
    return;
  }

  setTimeout(callback, 0);
}

postTask(() => {
  console.log('background sync');
}, 'background');
```

✅ Đây là progressive enhancement. Không viết logic bắt buộc phụ thuộc vào API chưa phổ biến toàn bộ.

---

## ⚛️ Production Notes / React Implications

### React batching và Event Loop

React có cơ chế batching state updates. Tùy version, root mode và context, update trong event handler, Promise, timeout có thể được batch khác nhau.

Điểm cần nhớ:

- ✅ `setState` không đồng nghĩa DOM update ngay lập tức.
- ✅ React render cũng chạy trên main thread, vẫn bị block bởi JS sync nặng.
- ✅ Long task trong event handler làm click/input bị lag.
- ✅ Microtask dài có thể trì hoãn paint, dù React đã tính xong update.
- ⚠️ `flushSync` ép update sync, chỉ dùng khi thật cần vì có thể làm UI kém mượt.

Ví dụ tránh stale state:

```tsx
setCount((count) => count + 1);
setCount((count) => count + 1);
```

Thay vì:

```tsx
setCount(count + 1);
setCount(count + 1);
```

---

### Cleanup timer, rAF, request, observer

Trong React component, mọi side effect async nên có cleanup:

```tsx
useEffect(() => {
  const controller = new AbortController();
  const timer = setTimeout(loadData, 300);

  const observer = new IntersectionObserver(handleEntries);

  const frameId = requestAnimationFrame(() => {
    // visual update
  });

  fetch('/api/user', { signal: controller.signal });

  return () => {
    controller.abort();
    clearTimeout(timer);
    cancelAnimationFrame(frameId);
    observer.disconnect();
  };
}, []);
```

Checklist cleanup:

- `clearTimeout`
- `clearInterval`
- `cancelAnimationFrame`
- `AbortController.abort`
- `observer.disconnect`
- `worker.terminate`
- remove event listener nếu không dùng option/signal cleanup

---

### SSR/Hydration

Event Loop là runtime behavior của client, nhưng SSR vẫn liên quan:

- ⚠️ `window`, `document`, `requestAnimationFrame`, `IntersectionObserver` không tồn tại trên server.
- ✅ Chỉ gọi browser APIs trong `useEffect` hoặc sau guard `typeof window !== 'undefined'`.
- ⚠️ Hydration có thể mismatch nếu render phụ thuộc `Date.now()`, timer, viewport size ngay trong render.

Ví dụ guard:

```tsx
useEffect(() => {
  if (!('IntersectionObserver' in window)) return;

  const observer = new IntersectionObserver(() => {});

  return () => observer.disconnect();
}, []);
```

---

### Performance debugging

Dấu hiệu Event Loop bị block:

- click/input delay
- scroll jank
- animation drop frames
- timer chạy trễ
- Promise callback bị trì hoãn
- Chrome DevTools báo Long Task

Cách debug:

- Chrome Performance panel.
- Long Animation Frame/Long Task markers.
- `performance.mark` / `performance.measure`.
- React Profiler nếu lag đến từ render tree.
- Tách CPU-heavy work sang worker hoặc chunking.

```ts
performance.mark('normalize:start');
normalizeLargeData(rows);
performance.mark('normalize:end');

performance.measure('normalize', 'normalize:start', 'normalize:end');
```

---

### Accessibility impact

Event Loop không chỉ là performance; nó ảnh hưởng accessibility:

- Screen reader announcement có thể bị delay nếu main thread bận.
- Keyboard navigation lag nếu keydown handler quá nặng.
- Focus management sai nếu đọc DOM trước khi React commit/paint.
- Animation JS không cleanup có thể gây motion khó chịu.

✅ Với UI tương tác cao, ưu tiên:

- task ngắn
- CSS animation khi có thể
- `prefers-reduced-motion`
- virtualized list cho danh sách lớn
- worker/chunking cho xử lý dữ liệu lớn

---

## ⚠️ Common Pitfalls

### ❌ 1. Nghĩ `setTimeout(fn, 0)` chạy ngay

Sai. Nó chỉ chạy sau:

- sync code xong
- microtasks xong
- browser/runtime chọn task đó

---

### ❌ 2. Quên Promise là microtask

```ts
setTimeout(() => console.log('timeout'), 0);
Promise.resolve().then(() => console.log('promise'));

// promise trước timeout
```

---

### ❌ 3. Dùng microtask cho work dài

```ts
queueMicrotask(() => {
  expensiveCalculation(); // ❌ có thể block paint
});
```

Microtask không phải background thread.

---

### ❌ 4. Tạo microtask recursive vô hạn

```ts
function loop() {
  Promise.resolve().then(loop);
}
```

Kết quả: timer, input, render đều có thể bị starve.

---

### ❌ 5. Dùng debounce nhưng không cancel request cũ

Debounce chỉ giảm tần suất gọi. Nó không tự giải quyết race condition.

✅ Dùng thêm:

- `AbortController`
- request id/versioning
- ignore stale response

---

### ❌ 6. Dùng throttle scroll cho lazy loading khi có IntersectionObserver

Scroll listener vẫn chạy nhiều và dễ làm main thread bận.

✅ Lazy load/visibility tracking nên ưu tiên `IntersectionObserver`.

---

### ❌ 7. Quên cleanup trong React

Timer, rAF, observer, worker, fetch không cleanup có thể gây:

- memory leak
- state update sau unmount
- request thừa
- animation chạy ngầm
- observer giữ DOM reference

---

### ❌ 8. Dựa vào exact ordering giữa mọi task source

Order tổng quát cần nhớ:

```txt
sync → microtasks → render opportunity → tasks
```

Nhưng order chi tiết giữa `setTimeout`, `MessageChannel`, event, rAF, I/O có thể phụ thuộc runtime/browser/context.

---

## ✅ Decision Guide / Checklist

### Chọn công cụ theo tình huống

- Cần chạy sau sync code hiện tại, trước timer:
  - ✅ `queueMicrotask`
  - ✅ Promise microtask nếu đang trong Promise flow

- Cần cho UI có cơ hội render/input:
  - ✅ `setTimeout(fn, 0)` hoặc chunking
  - ✅ `scheduler.postTask` nếu có feature detect

- Cần animation hoặc visual update theo frame:
  - ✅ `requestAnimationFrame`
  - ✅ CSS animation/transition nếu đơn giản

- Cần chạy khi browser rảnh:
  - ✅ `requestIdleCallback`
  - ⚠️ chỉ cho non-critical work

- User gõ search input:
  - ✅ debounce
  - ✅ AbortController/request versioning

- Scroll/resize fire liên tục:
  - ✅ throttle
  - ✅ passive listener cho scroll/touch

- Lazy load khi element vào viewport:
  - ✅ `IntersectionObserver`

- CPU-heavy:
  - ✅ Web Worker
  - ✅ chunking nếu worker quá phức tạp

---

### Checklist review code async frontend

- ✅ Có long sync task nào trên main thread không?
- ✅ Promise chain có thể tạo microtask quá dài không?
- ✅ Timer/rAF/observer/request có cleanup không?
- ✅ Search/autocomplete có chống race condition không?
- ✅ Scroll handler có throttle/passive hoặc thay bằng IntersectionObserver không?
- ✅ Animation có dùng rAF/CSS thay vì setTimeout không?
- ✅ Heavy computation có chunking hoặc worker không?
- ✅ SSR có guard browser APIs không?
- ✅ Có đo bằng Performance panel/React Profiler thay vì đoán không?

---

## 🗣️ Short Interview Answer

Em nghĩ Event Loop là cơ chế giúp JavaScript chạy async trong khi bản thân JS vẫn chỉ có một Call Stack chính. Code đồng bộ sẽ chạy trước. Những việc như timer, DOM event, network request được Browser hoặc Node runtime xử lý bên ngoài; khi xong thì callback được đưa vào queue.

Điểm em thường nhấn mạnh là không phải queue nào cũng giống nhau. `Promise.then`, `queueMicrotask`, `await` continuation là microtask nên sẽ chạy sau sync code nhưng trước `setTimeout`. Event Loop sẽ chạy hết microtasks trước, rồi browser mới có cơ hội render, sau đó mới lấy một macrotask. Vì vậy `setTimeout(fn, 0)` không có nghĩa là chạy ngay.

Trong frontend production, em quan tâm nhất đến việc không block main thread. Nếu work nặng thì em chia chunk, dùng Web Worker, hoặc schedule đúng công cụ: `requestAnimationFrame` cho animation, `debounce` cho search, `throttle` cho scroll, `IntersectionObserver` cho lazy loading, `requestIdleCallback` cho background task. Em cũng luôn cleanup timer, rAF, observer và request trong React để tránh leak hoặc update sau unmount.

---

## 🧠 Ghi nhớ nhanh

- ✅ JavaScript chạy sync code trên một Call Stack chính.
- ✅ Async API được runtime xử lý, callback quay lại qua queue.
- ✅ Microtask chạy trước macrotask.
- ✅ Event Loop chạy hết microtasks trước khi qua task tiếp theo.
- ✅ Browser chỉ render khi main thread rảnh.
- ✅ `requestAnimationFrame` chạy trước paint.
- ✅ `requestIdleCallback` chỉ dành cho background work.
- ✅ `setTimeout(0)` không chạy ngay.
- ✅ Microtask vô hạn có thể làm UI đứng.
- ✅ Long sync task làm input, scroll, animation bị lag.
- ✅ Debounce không tự fix race condition; cần cancel/ignore stale request.
- ✅ React render cũng nằm trên main thread, vẫn bị Event Loop block.
- ✅ Cleanup side effects là bắt buộc trong component production.

---

## 📖 Giải thích các thuật ngữ trong topic

- **Event Loop**
  - Vòng lặp của runtime dùng để lấy callback từ queue đưa vào Call Stack khi stack trống.

- **Call Stack**
  - Ngăn xếp chạy function đồng bộ của JavaScript.

- **Heap**
  - Vùng nhớ lưu object, array, function, closure.

- **Web APIs**
  - API do browser cung cấp như timer, DOM event, fetch, observer, worker.

- **Node APIs**
  - API do Node.js cung cấp như file I/O, network I/O, timers, `setImmediate`.

- **Microtask**
  - Task ưu tiên cao, chạy sau sync code và trước macrotask. Ví dụ: Promise callback, `queueMicrotask`.

- **Macrotask / Task**
  - Task thông thường như timer, event, I/O callback.

- **`process.nextTick`**
  - Queue đặc biệt trong Node.js, chạy trước Promise microtasks. Không có trong browser.

- **`setTimeout(fn, 0)`**
  - Schedule callback vào task queue sớm nhất có thể, không phải chạy ngay lập tức.

- **`setInterval`**
  - Chạy callback lặp lại theo interval, cần `clearInterval` khi không dùng nữa.

- **`setImmediate`**
  - API Node.js chạy ở check phase của Event Loop.

- **`Promise.then`**
  - Đăng ký callback vào microtask queue khi Promise resolve.

- **`queueMicrotask`**
  - API trực tiếp để đưa callback vào microtask queue.

- **`MutationObserver`**
  - Browser API theo dõi DOM mutation, callback chạy dạng microtask.

- **`requestAnimationFrame`**
  - Schedule callback trước lần paint tiếp theo, phù hợp cho animation.

- **`requestIdleCallback`**
  - Schedule callback khi browser rảnh, phù hợp background task không critical.

- **`MessageChannel`**
  - API tạo kênh message; có thể dùng để schedule task trong scheduler/polyfill.

- **`IntersectionObserver`**
  - API theo dõi element có vào viewport hay không, tốt cho lazy loading.

- **`Web Worker`**
  - Thread riêng để chạy JS CPU-heavy mà không block main thread.

- **`scheduler.postTask`**
  - API schedule task theo priority ở browser hỗ trợ; cần feature detection.

- **Debounce**
  - Chỉ chạy function sau khi event ngừng xảy ra một khoảng thời gian.

- **Throttle**
  - Giới hạn function chỉ chạy tối đa một lần trong một khoảng thời gian.

- **Microtask starvation**
  - Tình trạng microtask sinh liên tục khiến macrotask/render không được chạy.

- **Long Task**
  - Task trên main thread chạy lâu, thường trên 50ms, gây lag input/render.

- **Reflow/Layout**
  - Browser tính lại kích thước/vị trí layout.

- **Paint**
  - Browser vẽ pixels lên layer.

- **Composite**
  - Browser ghép các layer để hiển thị frame cuối cùng.

- **Race condition**
  - Lỗi xảy ra khi kết quả phụ thuộc vào thứ tự hoàn tất không chắc chắn, ví dụ request search cũ về sau request mới.

- **AbortController**
  - API cancel request/fetch hoặc cleanup async flow có hỗ trợ signal.
