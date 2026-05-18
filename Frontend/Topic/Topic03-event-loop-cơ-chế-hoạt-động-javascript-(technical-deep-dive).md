<div align="center" style="padding: 28px 24px; border: 1px solid #d0d7de; border-radius: 16px; background: linear-gradient(135deg, #0f172a 0%, #1e293b 52%, #0f766e 100%); color: #ffffff; margin-bottom: 24px;">

<h1 style="margin: 0 0 10px; font-size: 34px; line-height: 1.2;">🔄 Topic03: Event Loop, Async Runtime & Deferring Execution</h1>

<p style="margin: 0 0 16px; font-size: 16px; color: #dbeafe;"><strong>JavaScript Runtime · Microtask · Macrotask · Browser Rendering · Deferring Execution</strong></p>

<p style="margin: 0;">
  <code style="background: rgba(255,255,255,0.14); color: #ffffff; padding: 4px 8px; border-radius: 999px;">Call Stack</code>
  <code style="background: rgba(255,255,255,0.14); color: #ffffff; padding: 4px 8px; border-radius: 999px;">Promise</code>
  <code style="background: rgba(255,255,255,0.14); color: #ffffff; padding: 4px 8px; border-radius: 999px;">setTimeout</code>
  <code style="background: rgba(255,255,255,0.14); color: #ffffff; padding: 4px 8px; border-radius: 999px;">requestAnimationFrame</code>
  <code style="background: rgba(255,255,255,0.14); color: #ffffff; padding: 4px 8px; border-radius: 999px;">Web Worker</code>
</p>

</div>

<div style="padding: 14px 16px; border-left: 5px solid #0f766e; background: #ecfdf5; color: #064e3b; border-radius: 10px; margin: 18px 0;">
  <strong style="color: #065f46;">🎯 Mục tiêu:</strong> hiểu chính xác JavaScript chạy code đồng bộ, async callback, Promise, render UI và các kỹ thuật trì hoãn execution trong frontend production.
</div>

---

<h2 id="-quick-navigation" style="margin: 34px 0 14px; padding: 14px 18px; border-radius: 14px; background: #0f172a; color: #f8fafc; font-size: 26px; line-height: 1.25;">🧭 Quick Navigation</h2>

<div style="padding: 16px; border: 1px solid #cbd5e1; border-radius: 12px; background: #f8fafc; color: #0f172a; margin: 12px 0 18px;">
  <table style="width: 100%; border-collapse: collapse; color: #0f172a;">
    <thead>
      <tr>
        <th align="left" style="padding: 10px 12px; border-bottom: 1px solid #cbd5e1; color: #334155;">Khu vực</th>
        <th align="left" style="padding: 10px 12px; border-bottom: 1px solid #cbd5e1; color: #334155;">Dùng khi bạn muốn</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 10px 12px; border-bottom: 1px solid #e2e8f0;"><a href="#-seniorstaff-summary" style="color: #0369a1; text-decoration: none;">⭐ Senior/Staff Summary</a></td>
        <td style="padding: 10px 12px; border-bottom: 1px solid #e2e8f0; color: #334155;">Ôn nhanh trước phỏng vấn</td>
      </tr>
      <tr>
        <td style="padding: 10px 12px; border-bottom: 1px solid #e2e8f0;"><a href="#-key-mental-model" style="color: #0369a1; text-decoration: none;">🧠 Key Mental Model</a></td>
        <td style="padding: 10px 12px; border-bottom: 1px solid #e2e8f0; color: #334155;">Hiểu runtime hoạt động như hệ thống</td>
      </tr>
      <tr>
        <td style="padding: 10px 12px; border-bottom: 1px solid #e2e8f0;"><a href="#-main-concepts" style="color: #0369a1; text-decoration: none;">📚 Main Concepts</a></td>
        <td style="padding: 10px 12px; border-bottom: 1px solid #e2e8f0; color: #334155;">Đi từ call stack đến rendering, rAF, idle, Node.js</td>
      </tr>
      <tr>
        <td style="padding: 10px 12px; border-bottom: 1px solid #e2e8f0;"><a href="#-practical-typescriptjavascript-examples" style="color: #0369a1; text-decoration: none;">🧪 Practical Examples</a></td>
        <td style="padding: 10px 12px; border-bottom: 1px solid #e2e8f0; color: #334155;">Luyện đoán output và pattern production</td>
      </tr>
      <tr>
        <td style="padding: 10px 12px; border-bottom: 1px solid #e2e8f0;"><a href="#-production-notes--react-implications" style="color: #0369a1; text-decoration: none;">⚛️ React Implications</a></td>
        <td style="padding: 10px 12px; border-bottom: 1px solid #e2e8f0; color: #334155;">Liên hệ batching, cleanup, hydration, performance</td>
      </tr>
      <tr>
        <td style="padding: 10px 12px; border-bottom: 1px solid #e2e8f0;"><a href="#-common-pitfalls" style="color: #0369a1; text-decoration: none;">⚠️ Common Pitfalls</a></td>
        <td style="padding: 10px 12px; border-bottom: 1px solid #e2e8f0; color: #334155;">Tránh lỗi phỏng vấn và lỗi production</td>
      </tr>
      <tr>
        <td style="padding: 10px 12px;"><a href="#-decision-guide--checklist" style="color: #0369a1; text-decoration: none;">✅ Decision Guide</a></td>
        <td style="padding: 10px 12px; color: #334155;">Chọn đúng kỹ thuật defer/cancel/schedule</td>
      </tr>
    </tbody>
  </table>
</div>

---

<h2 id="-runtime-flow-at-a-glance" style="margin: 34px 0 14px; padding: 14px 18px; border-radius: 14px; background: #0f172a; color: #f8fafc; font-size: 26px; line-height: 1.25;">🧩 Runtime Flow At A Glance</h2>

<div style="padding: 18px; border: 1px solid #cbd5e1; border-radius: 12px; background: #ffffff; color: #0f172a; box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08); margin: 12px 0 18px;">
  <table style="width: 100%; border-collapse: collapse; color: #0f172a;">
    <thead>
      <tr>
        <th align="left" style="padding: 10px 12px; border-bottom: 1px solid #cbd5e1; color: #334155;">Phase</th>
        <th align="left" style="padding: 10px 12px; border-bottom: 1px solid #cbd5e1; color: #334155;">Chạy gì?</th>
        <th align="left" style="padding: 10px 12px; border-bottom: 1px solid #cbd5e1; color: #334155;">Ghi nhớ</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 10px 12px; border-bottom: 1px solid #e2e8f0;"><strong>Sync</strong></td>
        <td style="padding: 10px 12px; border-bottom: 1px solid #e2e8f0; color: #334155;">Code đang nằm trên Call Stack</td>
        <td style="padding: 10px 12px; border-bottom: 1px solid #e2e8f0; color: #334155;">Luôn chạy trước</td>
      </tr>
      <tr>
        <td style="padding: 10px 12px; border-bottom: 1px solid #e2e8f0;"><strong>Microtask</strong></td>
        <td style="padding: 10px 12px; border-bottom: 1px solid #e2e8f0; color: #334155;"><code>Promise.then</code>, <code>queueMicrotask</code>, <code>await</code> continuation</td>
        <td style="padding: 10px 12px; border-bottom: 1px solid #e2e8f0; color: #334155;">Chạy hết trước task tiếp theo</td>
      </tr>
      <tr>
        <td style="padding: 10px 12px; border-bottom: 1px solid #e2e8f0;"><strong>Render chance</strong></td>
        <td style="padding: 10px 12px; border-bottom: 1px solid #e2e8f0; color: #334155;"><code>requestAnimationFrame</code>, style, layout, paint</td>
        <td style="padding: 10px 12px; border-bottom: 1px solid #e2e8f0; color: #334155;">Browser chỉ render khi main thread rảnh</td>
      </tr>
      <tr>
        <td style="padding: 10px 12px;"><strong>Task/Macrotask</strong></td>
        <td style="padding: 10px 12px; color: #334155;"><code>setTimeout</code>, DOM event, I/O, MessageChannel</td>
        <td style="padding: 10px 12px; color: #334155;">Thường lấy một task mỗi vòng</td>
      </tr>
    </tbody>
  </table>
</div>

```txt
┌───────────────┐
│ Sync JS Stack │
└───────┬───────┘
        ↓
┌───────────────┐
│ Microtasks    │  Promise.then / queueMicrotask / await
└───────┬───────┘
        ↓
┌───────────────┐
│ Render Chance │  rAF → style → layout → paint
└───────┬───────┘
        ↓
┌───────────────┐
│ One Task      │  timer / event / I/O
└───────┬───────┘
        ↺
```

---

<h2 id="-seniorstaff-summary" style="margin: 34px 0 14px; padding: 14px 18px; border-radius: 14px; background: #0f172a; color: #f8fafc; font-size: 26px; line-height: 1.25;">⭐ Senior/Staff Summary</h2>

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

<div style="padding: 14px 16px; border-left: 5px solid #f59e0b; background: #fffbeb; color: #78350f; border-radius: 10px; margin: 16px 0;">
  💡 <strong>Câu nhớ nhanh:</strong> Sync chạy trước, microtask chạy hết, browser có cơ hội render, rồi mới tới một macrotask.
</div>

---

<h2 id="-key-mental-model" style="margin: 34px 0 14px; padding: 14px 18px; border-radius: 14px; background: #0f172a; color: #f8fafc; font-size: 26px; line-height: 1.25;">🧠 Key Mental Model</h2>

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

<h2 id="-main-concepts" style="margin: 34px 0 14px; padding: 14px 18px; border-radius: 14px; background: #0f172a; color: #f8fafc; font-size: 26px; line-height: 1.25;">📚 Main Concepts</h2>

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">1. Call Stack: nơi code đồng bộ chạy</h3>

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

<div style="padding: 14px 16px; border-left: 5px solid #10b981; background: #ecfdf5; color: #064e3b; border-radius: 10px; margin: 16px 0;">
  ✅ <strong>Senior key:</strong> Event Loop không cứu được code sync đang kẹt trong Call Stack. Muốn UI phản hồi, phải chia nhỏ work hoặc đưa ra thread khác.
</div>

---

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">2. Web APIs / Node APIs: async không nằm trong JS engine thuần</h3>

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

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">3. Microtask Queue: ưu tiên cao</h3>

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

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">4. Promise chain cũng là nhiều microtasks</h3>

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

<div style="padding: 14px 16px; border-left: 5px solid #f59e0b; background: #fffbeb; color: #78350f; border-radius: 10px; margin: 16px 0;">
  💡 <strong>Key phỏng vấn:</strong> Promise chain không chạy nguyên một mạch như sync code. Mỗi <code>.then</code> là một microtask mới.
</div>

---

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">5. `queueMicrotask` vs `Promise.resolve().then`</h3>

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

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">6. Macrotask / Task Queue: timer, event, I/O</h3>

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

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">7. Browser rendering pipeline</h3>

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

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">8. `requestAnimationFrame`: chạy trước paint</h3>

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

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">9. `requestIdleCallback`: chạy khi browser rảnh</h3>

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

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">10. Node.js Event Loop khác Browser</h3>

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

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">11. `async/await` hoạt động với microtask</h3>

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

<div style="padding: 14px 16px; border-left: 5px solid #f97316; background: #fff7ed; color: #7c2d12; border-radius: 10px; margin: 16px 0;">
  ⚠️ Thứ tự giữa <code>await</code> continuation và Promise callback phụ thuộc thời điểm queue. Đừng viết logic production dựa trên thứ tự tinh vi nếu có thể tránh.
</div>

---

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">12. Microtask starvation</h3>

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

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">13. Deferring execution: chọn đúng kỹ thuật</h3>

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

<h2 id="-practical-typescriptjavascript-examples" style="margin: 34px 0 14px; padding: 14px 18px; border-radius: 14px; background: #0f172a; color: #f8fafc; font-size: 26px; line-height: 1.25;">🧪 Practical TypeScript/JavaScript Examples</h2>

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">Example 1: Thứ tự kinh điển</h3>

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

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">Example 2: Nested microtask</h3>

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

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">Example 3: Batching bằng microtask</h3>

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

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">Example 4: Heavy work phải chia nhỏ</h3>

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

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">Example 5: Debounce search + AbortController</h3>

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

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">Example 6: Throttle scroll + passive listener</h3>

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

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">Example 7: IntersectionObserver cho lazy loading</h3>

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

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">Example 8: React animation bằng `requestAnimationFrame`</h3>

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

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">Example 9: `MessageChannel`</h3>

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

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">Example 10: Web Worker cho CPU-heavy work</h3>

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

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">Example 11: `scheduler.postTask` với feature detection</h3>

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

<h2 id="-production-notes--react-implications" style="margin: 34px 0 14px; padding: 14px 18px; border-radius: 14px; background: #0f172a; color: #f8fafc; font-size: 26px; line-height: 1.25;">⚛️ Production Notes / React Implications</h2>

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">React batching và Event Loop</h3>

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

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">Cleanup timer, rAF, request, observer</h3>

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

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">SSR/Hydration</h3>

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

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">Performance debugging</h3>

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

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">Accessibility impact</h3>

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

<h2 id="-common-pitfalls" style="margin: 34px 0 14px; padding: 14px 18px; border-radius: 14px; background: #0f172a; color: #f8fafc; font-size: 26px; line-height: 1.25;">⚠️ Common Pitfalls</h2>

<div style="padding: 18px; border: 1px solid #fecaca; border-radius: 12px; background: #fef2f2; color: #450a0a; margin: 14px 0 20px;">
  <table style="width: 100%; border-collapse: collapse; color: #450a0a;">
    <thead>
      <tr>
        <th align="left" style="padding: 10px 12px; border-bottom: 1px solid #fecaca; color: #7f1d1d;">Pitfall</th>
        <th align="left" style="padding: 10px 12px; border-bottom: 1px solid #fecaca; color: #7f1d1d;">Dấu hiệu</th>
        <th align="left" style="padding: 10px 12px; border-bottom: 1px solid #fecaca; color: #7f1d1d;">Cách nghĩ đúng</th>
      </tr>
    </thead>
    <tbody>
      <tr><td style="padding: 10px 12px; border-bottom: 1px solid #fee2e2;"><code>setTimeout(fn, 0)</code> chạy ngay</td><td style="padding: 10px 12px; border-bottom: 1px solid #fee2e2;">Output timer không như dự đoán</td><td style="padding: 10px 12px; border-bottom: 1px solid #fee2e2;">Timer là task, phải chờ sync + microtask</td></tr>
      <tr><td style="padding: 10px 12px; border-bottom: 1px solid #fee2e2;">Quên Promise là microtask</td><td style="padding: 10px 12px; border-bottom: 1px solid #fee2e2;">Promise log trước timer</td><td style="padding: 10px 12px; border-bottom: 1px solid #fee2e2;">Microtask có priority cao hơn task</td></tr>
      <tr><td style="padding: 10px 12px; border-bottom: 1px solid #fee2e2;">Microtask làm work dài</td><td style="padding: 10px 12px; border-bottom: 1px solid #fee2e2;">UI không paint, input lag</td><td style="padding: 10px 12px; border-bottom: 1px solid #fee2e2;">Microtask không phải background thread</td></tr>
      <tr><td style="padding: 10px 12px; border-bottom: 1px solid #fee2e2;">Recursive microtask</td><td style="padding: 10px 12px; border-bottom: 1px solid #fee2e2;">Timer/render bị starve</td><td style="padding: 10px 12px; border-bottom: 1px solid #fee2e2;">Microtask queue phải được drain hết</td></tr>
      <tr><td style="padding: 10px 12px; border-bottom: 1px solid #fee2e2;">Debounce không cancel request</td><td style="padding: 10px 12px; border-bottom: 1px solid #fee2e2;">Response cũ ghi đè UI mới</td><td style="padding: 10px 12px; border-bottom: 1px solid #fee2e2;">Debounce giảm request, không tự chống race</td></tr>
      <tr><td style="padding: 10px 12px; border-bottom: 1px solid #fee2e2;">Scroll listener quá nặng</td><td style="padding: 10px 12px; border-bottom: 1px solid #fee2e2;">Scroll jank</td><td style="padding: 10px 12px; border-bottom: 1px solid #fee2e2;">Throttle/passive hoặc IntersectionObserver</td></tr>
      <tr><td style="padding: 10px 12px; border-bottom: 1px solid #fee2e2;">Quên cleanup React side effects</td><td style="padding: 10px 12px; border-bottom: 1px solid #fee2e2;">Leak, update after unmount</td><td style="padding: 10px 12px; border-bottom: 1px solid #fee2e2;">Cleanup timer/rAF/observer/request</td></tr>
      <tr><td style="padding: 10px 12px;">Dựa vào exact ordering quá sâu</td><td style="padding: 10px 12px;">Khác browser/runtime có thể lệch</td><td style="padding: 10px 12px;">Chỉ dựa vào mental model tổng quát</td></tr>
    </tbody>
  </table>
</div>

---

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">❌ 1. Nghĩ `setTimeout(fn, 0)` chạy ngay</h3>

Sai. Nó chỉ chạy sau:

- sync code xong
- microtasks xong
- browser/runtime chọn task đó

---

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">❌ 2. Quên Promise là microtask</h3>

```ts
setTimeout(() => console.log('timeout'), 0);
Promise.resolve().then(() => console.log('promise'));

// promise trước timeout
```

---

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">❌ 3. Dùng microtask cho work dài</h3>

```ts
queueMicrotask(() => {
  expensiveCalculation(); // ❌ có thể block paint
});
```

Microtask không phải background thread.

---

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">❌ 4. Tạo microtask recursive vô hạn</h3>

```ts
function loop() {
  Promise.resolve().then(loop);
}
```

Kết quả: timer, input, render đều có thể bị starve.

---

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">❌ 5. Dùng debounce nhưng không cancel request cũ</h3>

Debounce chỉ giảm tần suất gọi. Nó không tự giải quyết race condition.

✅ Dùng thêm:

- `AbortController`
- request id/versioning
- ignore stale response

---

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">❌ 6. Dùng throttle scroll cho lazy loading khi có IntersectionObserver</h3>

Scroll listener vẫn chạy nhiều và dễ làm main thread bận.

✅ Lazy load/visibility tracking nên ưu tiên `IntersectionObserver`.

---

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">❌ 7. Quên cleanup trong React</h3>

Timer, rAF, observer, worker, fetch không cleanup có thể gây:

- memory leak
- state update sau unmount
- request thừa
- animation chạy ngầm
- observer giữ DOM reference

---

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">❌ 8. Dựa vào exact ordering giữa mọi task source</h3>

Order tổng quát cần nhớ:

```txt
sync → microtasks → render opportunity → tasks
```

Nhưng order chi tiết giữa `setTimeout`, `MessageChannel`, event, rAF, I/O có thể phụ thuộc runtime/browser/context.

---

<h2 id="-decision-guide--checklist" style="margin: 34px 0 14px; padding: 14px 18px; border-radius: 14px; background: #0f172a; color: #f8fafc; font-size: 26px; line-height: 1.25;">✅ Decision Guide / Checklist</h2>

<div style="padding: 18px; border: 1px solid #bfdbfe; border-radius: 12px; background: #eff6ff; color: #172554; margin: 14px 0 20px;">
  <table style="width: 100%; border-collapse: collapse; color: #172554;">
    <thead>
      <tr>
        <th align="left" style="padding: 10px 12px; border-bottom: 1px solid #bfdbfe; color: #1e3a8a;">Tình huống</th>
        <th align="left" style="padding: 10px 12px; border-bottom: 1px solid #bfdbfe; color: #1e3a8a;">Ưu tiên dùng</th>
        <th align="left" style="padding: 10px 12px; border-bottom: 1px solid #bfdbfe; color: #1e3a8a;">Tránh dùng</th>
      </tr>
    </thead>
    <tbody>
      <tr><td style="padding: 10px 12px; border-bottom: 1px solid #dbeafe;">Chạy sau sync code hiện tại</td><td style="padding: 10px 12px; border-bottom: 1px solid #dbeafe;"><code>queueMicrotask</code>, Promise microtask</td><td style="padding: 10px 12px; border-bottom: 1px solid #dbeafe;">Work CPU nặng</td></tr>
      <tr><td style="padding: 10px 12px; border-bottom: 1px solid #dbeafe;">Cho UI có cơ hội render</td><td style="padding: 10px 12px; border-bottom: 1px solid #dbeafe;"><code>setTimeout(0)</code>, chunking, <code>scheduler.postTask</code></td><td style="padding: 10px 12px; border-bottom: 1px solid #dbeafe;">Microtask loop dài</td></tr>
      <tr><td style="padding: 10px 12px; border-bottom: 1px solid #dbeafe;">Animation theo frame</td><td style="padding: 10px 12px; border-bottom: 1px solid #dbeafe;"><code>requestAnimationFrame</code>, CSS transition</td><td style="padding: 10px 12px; border-bottom: 1px solid #dbeafe;"><code>setTimeout</code> để animate frame</td></tr>
      <tr><td style="padding: 10px 12px; border-bottom: 1px solid #dbeafe;">Background non-critical work</td><td style="padding: 10px 12px; border-bottom: 1px solid #dbeafe;"><code>requestIdleCallback</code></td><td style="padding: 10px 12px; border-bottom: 1px solid #dbeafe;">Logic quan trọng cần chạy ngay</td></tr>
      <tr><td style="padding: 10px 12px; border-bottom: 1px solid #dbeafe;">Search input</td><td style="padding: 10px 12px; border-bottom: 1px solid #dbeafe;">Debounce + <code>AbortController</code></td><td style="padding: 10px 12px; border-bottom: 1px solid #dbeafe;">Chỉ debounce mà không chống race</td></tr>
      <tr><td style="padding: 10px 12px; border-bottom: 1px solid #dbeafe;">Scroll/resize liên tục</td><td style="padding: 10px 12px; border-bottom: 1px solid #dbeafe;">Throttle + passive listener</td><td style="padding: 10px 12px; border-bottom: 1px solid #dbeafe;">Handler nặng chạy mỗi event</td></tr>
      <tr><td style="padding: 10px 12px; border-bottom: 1px solid #dbeafe;">Lazy load/visibility</td><td style="padding: 10px 12px; border-bottom: 1px solid #dbeafe;"><code>IntersectionObserver</code></td><td style="padding: 10px 12px; border-bottom: 1px solid #dbeafe;">Tự tính viewport bằng scroll liên tục</td></tr>
      <tr><td style="padding: 10px 12px;">CPU-heavy work</td><td style="padding: 10px 12px;">Web Worker hoặc chunking</td><td style="padding: 10px 12px;">Chạy sync trên main thread</td></tr>
    </tbody>
  </table>
</div>

---

<h3 style="margin: 28px 0 12px; padding: 10px 14px; border-left: 5px solid #0f766e; border-radius: 10px; background: #ecfdf5; color: #064e3b; font-size: 20px; line-height: 1.35;">Chọn công cụ theo tình huống</h3>

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

<h2 id="-short-interview-answer" style="margin: 34px 0 14px; padding: 14px 18px; border-radius: 14px; background: #0f172a; color: #f8fafc; font-size: 26px; line-height: 1.25;">🗣️ Short Interview Answer</h2>

Em nghĩ Event Loop là cơ chế giúp JavaScript chạy async trong khi bản thân JS vẫn chỉ có một Call Stack chính. Code đồng bộ sẽ chạy trước. Những việc như timer, DOM event, network request được Browser hoặc Node runtime xử lý bên ngoài; khi xong thì callback được đưa vào queue.

Điểm em thường nhấn mạnh là không phải queue nào cũng giống nhau. `Promise.then`, `queueMicrotask`, `await` continuation là microtask nên sẽ chạy sau sync code nhưng trước `setTimeout`. Event Loop sẽ chạy hết microtasks trước, rồi browser mới có cơ hội render, sau đó mới lấy một macrotask. Vì vậy `setTimeout(fn, 0)` không có nghĩa là chạy ngay.

Trong frontend production, em quan tâm nhất đến việc không block main thread. Nếu work nặng thì em chia chunk, dùng Web Worker, hoặc schedule đúng công cụ: `requestAnimationFrame` cho animation, `debounce` cho search, `throttle` cho scroll, `IntersectionObserver` cho lazy loading, `requestIdleCallback` cho background task. Em cũng luôn cleanup timer, rAF, observer và request trong React để tránh leak hoặc update sau unmount.

---

<h2 id="-ghi-nhớ-nhanh" style="margin: 34px 0 14px; padding: 14px 18px; border-radius: 14px; background: #0f172a; color: #f8fafc; font-size: 26px; line-height: 1.25;">🧠 Ghi nhớ nhanh</h2>

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

<h2 id="-giải-thích-các-thuật-ngữ-trong-topic" style="margin: 34px 0 14px; padding: 14px 18px; border-radius: 14px; background: #0f172a; color: #f8fafc; font-size: 26px; line-height: 1.25;">📖 Giải thích các thuật ngữ trong topic</h2>

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
