# Frontend Topic Interview Mindmap V2 - Senior/Staff Edition

> V2 được tạo từ `FRONTEND-TOPIC-MINDMAP.md` nhưng không ghi đè file gốc.
>
> Mục tiêu của V2: biến mỗi topic thành một khung trả lời phỏng vấn có thể dùng thật, gồm bản ngắn 30 giây, bản sâu 2 phút, case production, cách debug/đo đạc và follow-up thường gặp.

---

## Cách Dùng File Này

Mỗi topic nên luyện theo 4 vòng:

1. **30s answer**: trả lời gọn, đúng trọng tâm.
2. **2min deep answer**: thêm tradeoff, production concern và ví dụ.
3. **Production case**: kể một tình huống thật hoặc gần thật.
4. **Debug/Measure**: nói được bạn kiểm chứng bằng công cụ nào.

Cấu trúc trả lời senior:

```text
Em hiểu đơn giản là...
Trong production, vấn đề hay gặp là...
Tradeoff ở đây là...
Em sẽ debug/đo bằng...
Nếu phải thiết kế/fix, em sẽ...
```

Điểm khác biệt giữa middle và senior không nằm ở việc biết nhiều keyword hơn, mà ở khả năng nối keyword với correctness, UX, performance, security, maintainability và cách kiểm chứng.

---

## 📌 **Topic01 - Claude Code Workflow**

### ⚡ **30 Giây - Quick Answer**

Claude Code là AI coding assistant trong repo. Em dùng nó có kiểm soát: task rõ, context gọn, file path cụ thể, review diff và chạy check sau khi edit. AI giúp tăng tốc, nhưng quyết định cuối cùng vẫn là engineer.

### 📚 **2 Phút - Deep Dive**

Với task nhỏ em đưa yêu cầu trực tiếp kèm file liên quan. Với task lớn em yêu cầu plan trước, chia bước, rồi mới sửa. Em dùng memory/instruction cho convention ổn định, custom command cho workflow lặp lại, hook cho validate/lint/secret check. Khi đổi task em clear context để tránh nhiễu. Khi session dài nhưng còn cần history, em compact. Em không hỏi kiểu "xem toàn bộ repo" nếu không cần, vì context dài làm tốn token và dễ sai.

### 💼 **Trường Hợp Thực Tế**

AI sửa một component nhưng vô tình đổi behavior của form validation. Cách xử lý đúng là đọc diff, chạy test, kiểm UI flow, rồi mới merge.

### 🔍 **Cách Kiểm Chứng**

`git diff`, unit/integration test, typecheck, lint, build, visual check nếu có UI.

### 🤔 **Câu Hỏi Follow-up**

- Khi nào dùng plan mode?
  Trả lời ngắn: Khi task lớn, nhiều file, nhiều tradeoff hoặc có rủi ro sửa sai phạm vi.
- Làm sao tránh AI sửa ngoài phạm vi?
  Trả lời ngắn: Giao file path rõ, scope rõ, yêu cầu không refactor ngoài task và luôn review diff.
- Hook nào nên có trong repo frontend?
  Trả lời ngắn: Lint, typecheck, format check, test liên quan và secret scan nếu repo có nguy cơ lộ key.

### ❌ **Lỗi Cần Tránh**

- Tin output AI mà không review.
- Nhồi quá nhiều tài liệu vào context.
- Dùng một session cho nhiều task không liên quan.

---

## 📌 **Topic02 - Data Types & Memory Management**

### ⚡ **30 Giây - Quick Answer**

Primitive copy theo value, object/array/function được truy cập qua reference. Trong React, reference equality rất quan trọng vì state, props, memo và shallow compare đều bị ảnh hưởng.

### 📚 **2 Phút - Deep Dive**

`{ a: 1 } === { a: 1 }` là false vì là hai reference khác nhau. Shallow copy chỉ copy lớp ngoài, nested object vẫn dùng chung reference. Deep clone có thể tốn CPU và phá structural sharing. GC giữ object còn sống nếu vẫn reachable từ root. Với money, decimal hoặc large id, em không xử lý bừa bằng `number`, vì precision và safe integer có thể gây bug production.

### 💼 **Trường Hợp Thực Tế**

Một reducer mutate nested state rồi return cùng reference. UI không update hoặc memoized component không render lại đúng.

### 🔍 **Cách Kiểm Chứng**

React DevTools, console reference check, profiler, kiểm immutable update path, heap snapshot nếu nghi leak.

### 🤔 **Câu Hỏi Follow-up**

- Shallow copy khác deep clone thế nào?
  Trả lời ngắn: Shallow copy chỉ copy lớp ngoài; deep clone copy cả object lồng bên trong.
- Vì sao React cần immutable update?
  Trả lời ngắn: React và memoization thường dựa vào reference equality để biết dữ liệu đã đổi.
- Khi nào large id nên giữ dạng string?
  Trả lời ngắn: Khi id có thể vượt `Number.MAX_SAFE_INTEGER` hoặc cần giữ chính xác tuyệt đối.

### ❌ **Lỗi Cần Tránh**

- Dùng `JSON.stringify` để clone/compare mọi object.
- Mutate state rồi nghĩ React lỗi.
- Dùng float cho tiền.

---

## 📌 **Topic03 - Event Loop**

### ⚡ **30 Giây - Quick Answer**

Event loop điều phối call stack, microtask, macrotask và rendering. Code sync chạy trước, microtask như Promise chạy trước macrotask như timer.

### 📚 **2 Phút - Deep Dive**

JavaScript chạy trên main thread cho phần lớn UI work. Sau khi call stack rỗng, browser xử lý microtask queue đến hết rồi mới sang phase khác như macrotask hoặc render. Vì vậy `Promise.then` thường chạy trước `setTimeout(fn, 0)`. Nếu có long task hoặc microtask loop quá dài, browser không kịp paint, input bị trễ và app cảm giác bị đơ.

### 💼 **Trường Hợp Thực Tế**

Một màn hình import file xử lý hàng chục nghìn row sync trên main thread làm click/scroll bị freeze.

### 🔍 **Cách Kiểm Chứng**

Chrome Performance, Long Task marker, Event Log, INP/Core Web Vitals, Web Worker nếu CPU-bound.

### 🤔 **Câu Hỏi Follow-up**

- Microtask và macrotask khác nhau thế nào?
  Trả lời ngắn: Microtask như Promise chạy sau sync code và trước macrotask như timer.
- Vì sao `setTimeout(0)` không chạy ngay?
  Trả lời ngắn: Nó chỉ đưa callback vào macrotask queue, phải chờ call stack và microtask xong.
- Khi nào dùng Web Worker?
  Trả lời ngắn: Khi có CPU-heavy work có thể tách khỏi main thread để tránh đơ UI.

### ❌ **Lỗi Cần Tránh**

- Nghĩ timer 0ms chạy tức thì.
- Không biết Promise callback là microtask.
- Dùng loop CPU nặng trên main thread.

---

## 📌 **Topic04 - Async/Await vs Promise vs Callback**

### ⚡ **30 Giây - Quick Answer**

`async/await` là syntax trên Promise, không biến async thành sync. Chọn sequential hay parallel phụ thuộc dependency và error strategy.

### 📚 **2 Phút - Deep Dive**

Nếu request phụ thuộc nhau, em `await` tuần tự. Nếu độc lập, em dùng `Promise.all`. Nếu dashboard cần lấy cả success/fail, dùng `allSettled`. Nếu cần timeout hoặc lấy kết quả đầu tiên, dùng `race` hoặc `any` tùy logic. Em tránh `forEach(async)` vì nó không await tổng thể. Error handling nên đủ hẹp để không nuốt lỗi và vẫn có context debug.

### 💼 **Trường Hợp Thực Tế**

Trang dashboard gọi 8 API độc lập nhưng code await tuần tự làm load chậm gấp nhiều lần.

### 🔍 **Cách Kiểm Chứng**

Network waterfall, request timing, logging correlation id, test error path.

### 🤔 **Câu Hỏi Follow-up**

- `Promise.all` fail-fast nghĩa là gì?
  Trả lời ngắn: Chỉ cần một Promise reject thì toàn bộ `Promise.all` reject ngay.
- `allSettled` dùng khi nào?
  Trả lời ngắn: Khi cần lấy cả kết quả thành công và thất bại, ví dụ dashboard partial data.
- Làm timeout request bằng Promise thế nào?
  Trả lời ngắn: Race request với một Promise reject sau timeout, hoặc dùng `AbortController`.

### ❌ **Lỗi Cần Tránh**

- Await tuần tự không cần thiết.
- `forEach(async)` rồi nghĩ đã đợi xong.
- `try/catch` quá rộng làm mất context lỗi.

---

## 📌 **Topic05 - ES5 vs ES6+**

### ⚡ **30 Giây - Quick Answer**

ES6+ không chỉ là syntax ngắn hơn. Nó thay đổi scope, module, Promise, class syntax, arrow `this`, và yêu cầu hiểu transpile/polyfill khi deploy.

### 📚 **2 Phút - Deep Dive**

`let/const` có block scope và TDZ, khác `var`. Arrow function không có `this` riêng. ESM static hơn nên hỗ trợ tree-shaking tốt hơn. Class là syntax trên prototype. Khi đi production, syntax mới cần transpile nếu browser target chưa hỗ trợ; API mới cần polyfill. Transpile và polyfill là hai vấn đề khác nhau.

### 💼 **Trường Hợp Thực Tế**

Build chạy được trên Chrome mới nhưng lỗi ở browser cũ vì dùng API mới mà chỉ transpile syntax, chưa polyfill.

### 🔍 **Cách Kiểm Chứng**

Browserslist, Babel/SWC config, bundle analyzer, production build test, caniuse/MDN khi cần.

### 🤔 **Câu Hỏi Follow-up**

- `const` có làm object immutable không?
  Trả lời ngắn: Không; `const` chỉ cố định binding, object bên trong vẫn có thể mutate.
- Transpile khác polyfill thế nào?
  Trả lời ngắn: Transpile đổi syntax; polyfill bổ sung runtime API còn thiếu.
- Vì sao ESM hỗ trợ tree-shaking tốt hơn?
  Trả lời ngắn: Import/export của ESM static hơn nên bundler phân tích dependency trước khi chạy.

### ❌ **Lỗi Cần Tránh**

- Nghĩ spread là deep copy.
- Quên polyfill runtime API.
- Không test production build.

---

## 📌 **Topic06 - Closure & Data Privacy**

### ⚡ **30 Giây - Quick Answer**

Closure là function giữ reference tới lexical environment nơi nó được tạo ra. Nó hữu ích cho private state, debounce, memoize, nhưng cũng gây stale closure hoặc memory leak.

### 📚 **2 Phút - Deep Dive**

Closure không giữ snapshot; nó giữ binding/reference. Trong React, `setInterval` trong `useEffect([])` có thể đọc state cũ nếu callback đóng trên value cũ. Giải pháp có thể là functional updater, dependency đúng, hoặc ref. Closure cũng có thể giữ object lớn sống lâu hơn cần nếu listener/timer không cleanup.

### 💼 **Trường Hợp Thực Tế**

Polling interval luôn gửi filter cũ vì callback bị stale closure sau khi user đổi filter.

### 🔍 **Cách Kiểm Chứng**

React hooks lint, console trace callback value, Chrome Memory heap snapshot, kiểm cleanup effect.

### 🤔 **Câu Hỏi Follow-up**

- Closure giữ snapshot hay reference?
  Trả lời ngắn: Closure giữ binding/reference tới lexical environment, không phải snapshot cố định.
- Stale closure trong React xử lý thế nào?
  Trả lời ngắn: Dùng dependency đúng, functional updater, `useRef`, hoặc recreate callback khi cần.
- Closure có gây memory leak không?
  Trả lời ngắn: Có thể, nếu callback giữ object lớn và listener/timer không được cleanup.

### ❌ **Lỗi Cần Tránh**

- Gọi closure là snapshot.
- Quên cleanup listener/timer.
- Return reference private data ra ngoài.

---

## 📌 **Topic07 - Arrow vs Regular Function & `this`**

### ⚡ **30 Giây - Quick Answer**

Regular function có `this` động theo cách gọi. Arrow function không có `this` riêng, nó lấy `this` từ scope bên ngoài.

### 📚 **2 Phút - Deep Dive**

Em dùng arrow cho callback khi muốn giữ lexical `this`. Với object method, prototype method hoặc method cần dynamic receiver, em dùng regular function. `call/apply/bind` chỉ đổi được `this` của regular function, không đổi được arrow. Trong class, method không auto bind; arrow field tiện nhưng tạo function riêng trên mỗi instance.

### 💼 **Trường Hợp Thực Tế**

Pass class method vào event handler làm mất `this`, runtime báo `undefined`.

### 🔍 **Cách Kiểm Chứng**

Stack trace, breakpoint tại callsite, kiểm cách function được gọi, lint rule cho unbound method nếu có.

### 🤔 **Câu Hỏi Follow-up**

- Vì sao destructure method làm mất `this`?
  Trả lời ngắn: Vì method bị gọi như function thường, mất object receiver ban đầu.
- Khi nào không nên dùng arrow?
  Trả lời ngắn: Khi function cần dynamic `this`, ví dụ object/prototype method.
- Arrow field trong class có tradeoff gì?
  Trả lời ngắn: Tự bind tiện hơn nhưng tạo function riêng cho mỗi instance, tốn memory hơn prototype method.

### ❌ **Lỗi Cần Tránh**

- Dùng arrow cho method cần dynamic `this`.
- Tin `bind` sửa được arrow.
- Không hiểu callsite quyết định `this`.

---

## 📌 **Topic08 - IIFE & Functional Programming**

### ⚡ **30 Giây - Quick Answer**

IIFE từng dùng để tạo scope trước ES Modules. Functional programming trong frontend là pure function, immutability và composition để code dễ test, dễ memoize.

### 📚 **2 Phút - Deep Dive**

IIFE ít cần hơn trong app hiện đại vì module đã tạo scope riêng. Functional style tốt khi transform data, reducer, selector, validation. Nhưng không nên áp dụng máy móc: chain quá dài khó đọc, clone sâu tốn CPU, memoization cũng có cost. Senior biết chọn declarative hay imperative dựa trên readability và đo đạc.

### 💼 **Trường Hợp Thực Tế**

Một selector dùng nhiều chain `map/filter/reduce` trên dataset lớn mỗi render gây lag; đổi sang memoized selector và `Map` lookup.

### 🔍 **Cách Kiểm Chứng**

React Profiler, flamegraph JS cost, unit test pure function, benchmark nhỏ nếu hot path.

### 🤔 **Câu Hỏi Follow-up**

- Pure function giúp gì cho test?
  Trả lời ngắn: Cùng input luôn ra cùng output, ít side effect nên dễ unit test.
- Immutability liên quan React thế nào?
  Trả lời ngắn: Immutable update tạo reference mới giúp React detect change và memo hóa đúng.
- Khi nào imperative loop tốt hơn?
  Trả lời ngắn: Khi hot path cần performance hoặc functional chain làm code khó đọc.

### ❌ **Lỗi Cần Tránh**

- Spread shallow nhưng tưởng deep.
- Lạm dụng `useMemo`.
- Functional chain dài khó maintain.

---

## 📌 **Topic09 - JavaScript Proxy**

### ⚡ **30 Giây - Quick Answer**

Proxy bọc object/function để intercept operation như get, set, delete, apply. Nó mạnh cho reactivity, validation, logging nhưng có overhead và identity issue.

### 📚 **2 Phút - Deep Dive**

Proxy nên forward bằng `Reflect` để giữ behavior chuẩn và tôn trọng invariant của JS engine. Proxy không tự deep cho nested object, muốn deep reactive phải wrap nested object. Nó tạo identity khác object gốc nên compare bằng reference cần cẩn thận. Em tránh dùng Proxy ở hot path nếu không đo.

### 💼 **Trường Hợp Thực Tế**

Form tracking dùng Proxy nhưng nested object không được wrap, nên thay đổi sâu không trigger dirty state.

### 🔍 **Cách Kiểm Chứng**

Breakpoint trap `get/set`, unit test nested behavior, performance profile nếu wrap data lớn.

### 🤔 **Câu Hỏi Follow-up**

- Proxy khác getter/setter thế nào?
  Trả lời ngắn: Proxy intercept nhiều operation hơn và bọc object từ bên ngoài.
- Vì sao nên dùng `Reflect`?
  Trả lời ngắn: `Reflect` giúp forward operation theo behavior chuẩn và giảm sai invariant.
- Vue 3 dùng Proxy để làm gì?
  Trả lời ngắn: Để track get/set trên object và trigger reactivity khi state thay đổi.

### ❌ **Lỗi Cần Tránh**

- Dùng Proxy cho mọi data path.
- Quên invariant.
- So sánh proxy với object gốc bằng identity.

---

## 📌 **Topic10 - JavaScript Classes**

### ⚡ **30 Giây - Quick Answer**

Class trong JavaScript là syntax dễ đọc hơn trên prototype chain. Em dùng class khi object có invariant, lifecycle hoặc dependency rõ.

### 📚 **2 Phút - Deep Dive**

Class hợp cho SDK client, service, custom error, domain model. Prototype method tiết kiệm memory hơn arrow field. `#private` là private runtime thật, còn TypeScript `private` chủ yếu là compile-time. Trong frontend lớn, em tránh inheritance sâu và ưu tiên composition/dependency injection để dễ test.

### 💼 **Trường Hợp Thực Tế**

API client class giữ token refresh strategy, retry config và request id, thay vì rải logic HTTP khắp UI.

### 🔍 **Cách Kiểm Chứng**

Unit test class invariant, inspect prototype, stack trace khi mất `this`, dependency injection trong test.

### 🤔 **Câu Hỏi Follow-up**

- Class có phải object-oriented thật không?
  Trả lời ngắn: Có hỗ trợ OOP style, nhưng bản chất vẫn dựa trên prototype chain.
- TS `private` khác `#private` thế nào?
  Trả lời ngắn: TS `private` chủ yếu compile-time; `#private` là private thật ở runtime.
- Composition hơn inheritance ở điểm nào?
  Trả lời ngắn: Composition linh hoạt hơn, ít coupling hơn và dễ test hơn inheritance sâu.

### ❌ **Lỗi Cần Tránh**

- Lạm dụng inheritance.
- Pass method làm callback rồi mất `this`.
- Dùng class chỉ để gom function không có state/invariant.

---

## 📌 **Topic11 - DOM Query, Manipulation & Events**

### ⚡ **30 Giây - Quick Answer**

DOM là cây UI browser tạo từ HTML. Event đi qua capture, target, bubble. Trong React app, sửa DOM trực tiếp phải cẩn thận vì có thể lệch source of truth.

### 📚 **2 Phút - Deep Dive**

Event delegation hữu ích cho list động hoặc nhiều item vì gắn listener ở parent. Khi manipulate DOM, em ưu tiên `textContent`, `classList`, `dataset`; tránh `innerHTML` nếu không sanitize vì XSS. Listener cần cleanup bằng `removeEventListener` hoặc `AbortController`. Passive listener giúp scroll mượt hơn. Focus và accessibility cũng là một phần của DOM work.

### 💼 **Trường Hợp Thực Tế**

Third-party widget tự mutate DOM trong vùng React quản lý, gây UI flicker và state không khớp.

### 🔍 **Cách Kiểm Chứng**

Elements panel, Event Listeners tab, breakpoint event, Accessibility tree, Performance scroll profile.

### 🤔 **Câu Hỏi Follow-up**

- Capture và bubble khác nhau thế nào?
  Trả lời ngắn: Capture đi từ ancestor xuống target; bubble đi từ target ngược lên ancestor.
- Event delegation hoạt động ra sao?
  Trả lời ngắn: Gắn listener ở parent và dùng event bubbling để xử lý child.
- Vì sao `innerHTML` nguy hiểm?
  Trả lời ngắn: Nếu render input không sanitize, attacker có thể chèn script gây XSS.

### ❌ **Lỗi Cần Tránh**

- XSS qua raw HTML.
- Quên cleanup listener.
- DOM manipulation conflict với React render.

---

## 📌 **Topic12 - Axios & Axios Interceptors**

### ⚡ **30 Giây - Quick Answer**

Interceptor là API boundary để xử lý logic HTTP dùng chung như token, locale, error normalization, refresh token, retry và cancellation.

### 📚 **2 Phút - Deep Dive**

Request interceptor có thể gắn token, request id, locale. Response interceptor normalize error, đo duration, xử lý `401`. Refresh token cần lock/queue để nhiều request 401 không gọi refresh đồng thời. Retry chỉ nên áp dụng lỗi tạm thời như network, `429`, `5xx`, có max retry, backoff và jitter. Với POST tạo order/payment, chỉ retry nếu có idempotency key.

### 💼 **Trường Hợp Thực Tế**

Access token hết hạn, 10 request cùng nhận 401 và cùng refresh, làm server overload và race token.

### 🔍 **Cách Kiểm Chứng**

Network tab, request id, logs masked token/PII, mock server test 401/retry/cancel path.

### 🤔 **Câu Hỏi Follow-up**

- Refresh token race xử lý thế nào?
  Trả lời ngắn: Dùng shared refresh promise/queue để chỉ refresh một lần rồi replay request.
- Retry POST có an toàn không?
  Trả lời ngắn: Không mặc định; chỉ nên retry nếu operation idempotent hoặc có idempotency key.
- UI redirect nên nằm trong interceptor không?
  Trả lời ngắn: Nên tách signal auth error ra ngoài, tránh nhét UI flow sâu trong HTTP layer.

### ❌ **Lỗi Cần Tránh**

- Retry vô hạn.
- Nhét UI modal/business logic vào HTTP client.
- Log token hoặc PII.

---

## 📌 **Topic13 - Array/Object Methods & Immutability**

### ⚡ **30 Giây - Quick Answer**

Em chọn method theo ý định: `map` transform, `filter` lọc, `find` tìm, `reduce/Map` group. Trong React phải biết method nào mutate như `sort`, `reverse`, `push`.

### 📚 **2 Phút - Deep Dive**

Immutability giúp shallow compare và memoization hoạt động. `sort()` mutate array gốc nên sort props/state trực tiếp là bug phổ biến. Spread chỉ shallow copy, nested object vẫn chung reference. Deep clone mọi thứ không phải giải pháp vì tốn CPU và mất structural sharing. Với data phức tạp, normalize state giúp update nhỏ và dễ compare.

### 💼 **Trường Hợp Thực Tế**

Component nhận `props.items`, gọi `items.sort()` trực tiếp làm parent data đổi ngoài ý muốn, UI khác cũng bị ảnh hưởng.

### 🔍 **Cách Kiểm Chứng**

React DevTools, freeze object trong dev, unit test reducer, profiler render path.

### 🤔 **Câu Hỏi Follow-up**

- Method array nào mutate?
  Trả lời ngắn: Ví dụ `sort`, `reverse`, `push`, `pop`, `splice`, `shift`, `unshift`.
- Structural sharing là gì?
  Trả lời ngắn: Chỉ tạo object mới ở phần thay đổi, phần không đổi giữ lại reference cũ.
- Khi nào dùng `Map` thay vì `reduce`?
  Trả lời ngắn: Khi cần lookup/group theo key rõ ràng và muốn code dễ đọc hơn.

### ❌ **Lỗi Cần Tránh**

- Sort trực tiếp state/props.
- Clone sâu mọi update.
- Chain dài làm code khó đọc.

---

## 📌 **Topic14 - Loop Performance & Async Loops**

### ⚡ **30 Giây - Quick Answer**

Loop performance không phải chỉ `for` nhanh hơn `map`. Senior tối ưu Big-O trước, rồi mới micro-optimize nếu có đo đạc.

### 📚 **2 Phút - Deep Dive**

Nếu trong mỗi item lại `.find()` trên array khác, code dễ thành `O(n*m)`. Đổi sang `Map` lookup thường hiệu quả hơn đổi syntax loop. Với async loop, chọn sequential `for...of await`, parallel `Promise.all`, `allSettled`, hoặc concurrency limit tùy dependency, rate limit và error strategy. `Promise.all` không giới hạn có thể overload API.

### 💼 **Trường Hợp Thực Tế**

Join users và orders bằng nested find làm table 20k rows lag; build `Map<userId, user>` giảm đáng kể thời gian render.

### 🔍 **Cách Kiểm Chứng**

Chrome Performance, console timing có kiểm soát, flamegraph, Network concurrency, production-like dataset.

### 🤔 **Câu Hỏi Follow-up**

- Vì sao `.find()` trong loop nguy hiểm?
  Trả lời ngắn: Nó dễ biến thành `O(n*m)` khi data lớn.
- Khi nào cần concurrency limit?
  Trả lời ngắn: Khi nhiều request/task song song có thể overload API, browser hoặc device.
- `forEach(async)` sai ở đâu?
  Trả lời ngắn: `forEach` không await callback, nên outer flow không đợi async tasks hoàn tất.

### ❌ **Lỗi Cần Tránh**

- Micro-optimize khi bottleneck là thuật toán.
- Bắn hàng trăm request cùng lúc.
- Xử lý CPU lớn trên main thread.

---

## 📌 **Topic15 - Compare Data Types, Strings, Big Numbers & Decimals**

### ⚡ **30 Giây - Quick Answer**

So sánh dữ liệu phải hiểu kiểu dữ liệu: object theo reference, string theo locale/Unicode, number có precision và safe integer limit.

### 📚 **2 Phút - Deep Dive**

Object/array giống nội dung vẫn không bằng nhau nếu khác reference. String id/enum dùng `===` ổn, nhưng sort/search tên người theo tiếng Việt nên dùng normalize hoặc `Intl.Collator`. Tiền nên lưu smallest unit hoặc dùng decimal library, không dùng float tùy tiện. Large id từ API nên giữ string nếu vượt `Number.MAX_SAFE_INTEGER`.

### 💼 **Trường Hợp Thực Tế**

Transaction id dài bị convert sang number, mất precision và gọi API detail sai record.

### 🔍 **Cách Kiểm Chứng**

Unit test edge cases, property-based test nếu cần, `Intl.Collator` test theo locale, API contract check.

### 🤔 **Câu Hỏi Follow-up**

- Vì sao `0.1 + 0.2 !== 0.3`?
  Trả lời ngắn: Vì floating point binary không biểu diễn chính xác nhiều số thập phân.
- Khi nào giữ id dạng string?
  Trả lời ngắn: Khi id quá lớn, không cần tính toán số học, hoặc cần giữ nguyên format.
- Sort tiếng Việt nên làm thế nào?
  Trả lời ngắn: Dùng `Intl.Collator` với locale phù hợp thay vì so sánh string đơn giản.

### ❌ **Lỗi Cần Tránh**

- `JSON.stringify` compare mọi object.
- Dùng `toFixed` làm rounding nghiệp vụ.
- Parse large id thành number.

---

## 📌 **Topic16 - Browser Rendering: Paint, Repaint, Reflow**

### ⚡ **30 Giây - Quick Answer**

Browser render qua layout/reflow, paint/repaint và composite. Animation nên ưu tiên `transform` và `opacity` thay vì property gây layout.

### 📚 **2 Phút - Deep Dive**

Reflow tính lại vị trí/kích thước nên thường đắt hơn repaint. Đọc layout sau khi ghi style có thể gây forced synchronous layout. Với list lớn, virtualize. Với image/media, đặt `width/height/aspect-ratio` để tránh CLS. `will-change` chỉ dùng có kiểm soát vì tạo layer cũng tốn memory.

### 💼 **Trường Hợp Thực Tế**

Scroll list bị giật vì mỗi item hover thay đổi `height` và code đọc `offsetHeight` trong loop.

### 🔍 **Cách Kiểm Chứng**

Chrome Performance, Rendering tab, Layout Shift track, Lighthouse CLS/INP, DevTools Layers.

### 🤔 **Câu Hỏi Follow-up**

- Reflow khác repaint thế nào?
  Trả lời ngắn: Reflow tính lại layout; repaint chỉ vẽ lại visual như màu, text, shadow.
- Forced layout xảy ra khi nào?
  Trả lời ngắn: Khi code ghi style rồi đọc layout sync như `offsetHeight`, buộc browser tính ngay.
- Vì sao `transform` mượt hơn `top/left`?
  Trả lời ngắn: `transform` thường chạy ở composite layer, ít làm lại layout hơn.

### ❌ **Lỗi Cần Tránh**

- Animate layout property mỗi frame.
- Lạm dụng `will-change`.
- Không đặt kích thước media.

---

## 📌 **Topic17 - Browser Storage**

### ⚡ **30 Giây - Quick Answer**

Chọn browser storage theo dữ liệu: theme/language nhỏ dùng localStorage, tab data dùng sessionStorage, offline/large data dùng IndexedDB, auth token nhạy cảm ưu tiên HttpOnly Secure cookie nếu kiến trúc phù hợp.

### 📚 **2 Phút - Deep Dive**

localStorage sync và JS đọc được nên không hợp refresh token/PII. Cookie tự gửi theo request, cần `HttpOnly`, `Secure`, `SameSite`, và nếu dùng cookie auth phải nghĩ CSRF. IndexedDB hợp offline/PWA/blob/data lớn. Dữ liệu client không trusted, server vẫn validate. Cần handle quota, private mode và JSON parse error.

### 💼 **Trường Hợp Thực Tế**

Refresh token lưu localStorage, XSS nhỏ trong trang có thể đọc token và chiếm session.

### 🔍 **Cách Kiểm Chứng**

Application tab, security review token storage, E2E logout/multi-tab test, quota/private mode test.

### 🤔 **Câu Hỏi Follow-up**

- Cookie HttpOnly giải quyết và không giải quyết gì?
  Trả lời ngắn: Chống JS đọc token, nhưng không tự giải quyết CSRF nếu cookie tự gửi.
- localStorage có nhược điểm gì?
  Trả lời ngắn: JS đọc được, sync/blocking, dễ rủi ro nếu app bị XSS.
- IndexedDB dùng khi nào?
  Trả lời ngắn: Khi cần lưu data lớn, offline data, file/blob hoặc cache phức tạp.

### ❌ **Lỗi Cần Tránh**

- Lưu secret/PII trong localStorage.
- Tin storage data là trusted.
- Không handle parse/quota error.

---

## 📌 **Topic18 - HTTP Caching & Browser Cache**

### ⚡ **30 Giây - Quick Answer**

Cache phải theo loại tài nguyên. SPA thường để `index.html` revalidate, asset có content hash cache lâu, API cache theo sensitivity và freshness.

### 📚 **2 Phút - Deep Dive**

`no-cache` nghĩa là có thể lưu nhưng phải revalidate; `no-store` mới là không lưu. JS/CSS/image/font có content hash có thể `max-age=31536000, immutable`. HTML không nên cache quá lâu vì user kẹt version cũ. API public có thể dùng ETag/cache ngắn, user-specific dùng private/no-cache, payment/token/PII nên no-store. CDN cache key phải tính header/query/user dimension đúng.

### 💼 **Trường Hợp Thực Tế**

CDN cache nhầm response `/me` giữa user vì thiếu cache key hoặc header private.

### 🔍 **Cách Kiểm Chứng**

Network headers, CDN logs, cache status header, hard reload/disable cache, deploy rollback test.

### 🤔 **Câu Hỏi Follow-up**

- `no-cache` khác `no-store`?
  Trả lời ngắn: `no-cache` được lưu nhưng phải revalidate; `no-store` không lưu.
- Vì sao asset cần content hash?
  Trả lời ngắn: Để cache lâu an toàn vì nội dung đổi thì URL cũng đổi.
- Cache invalidation ở SPA làm sao?
  Trả lời ngắn: HTML revalidate, asset hash cache lâu, API cache theo freshness và sensitivity.

### ❌ **Lỗi Cần Tránh**

- Cache HTML quá lâu.
- Asset cache lâu không hash.
- CDN cache nhầm user data.

---

## 📌 **Topic19 - Observer APIs**

### ⚡ **30 Giây - Quick Answer**

Observer APIs giúp browser báo khi element vào viewport, đổi size hoặc DOM thay đổi, tránh polling/scroll handler thủ công quá nhiều.

### 📚 **2 Phút - Deep Dive**

`IntersectionObserver` hợp lazy load, infinite scroll, impression tracking. `ResizeObserver` hợp chart/grid responsive theo kích thước container. `MutationObserver` dùng khi cần theo dõi DOM ngoài framework như third-party widget. Callback vẫn chạy trên main thread nên phải nhẹ. Một observer có thể observe nhiều element. Luôn `disconnect` khi không cần.

### 💼 **Trường Hợp Thực Tế**

Infinite scroll thiếu `isLoading/hasMore`, observer trigger liên tục và gọi API trùng.

### 🔍 **Cách Kiểm Chứng**

Performance tab, logs guard state, memory profile observer leak, unit/E2E scroll scenario.

### 🤔 **Câu Hỏi Follow-up**

- IntersectionObserver hơn scroll listener ở đâu?
  Trả lời ngắn: Browser tối ưu việc detect visibility, ít phải tự tính layout mỗi scroll.
- ResizeObserver loop xảy ra khi nào?
  Trả lời ngắn: Khi callback thay đổi size chính element đang observe và trigger lại liên tục.
- MutationObserver nên dùng khi nào?
  Trả lời ngắn: Khi cần theo dõi DOM ngoài framework, ví dụ third-party widget.

### ❌ **Lỗi Cần Tránh**

- Quên disconnect.
- Observe phạm vi quá rộng.
- Callback làm work nặng.

---

## 📌 **Topic20 - CommonJS vs ES Modules & Bundling**

### ⚡ **30 Giây - Quick Answer**

CommonJS dùng `require/module.exports` và linh hoạt runtime. ES Modules dùng `import/export`, static hơn nên bundler dễ tree-shake và code split.

### 📚 **2 Phút - Deep Dive**

Frontend mới nên ưu tiên ESM, nhưng production cần để ý package interop, `main`, `module`, `exports`, `type`, và `sideEffects`. Dynamic import dùng cho lazy loading. `sideEffects: false` giúp tree-shaking nhưng khai báo sai có thể làm mất CSS/polyfill hoặc code có side effect. Dual package có thể gây duplicate bundle.

### 💼 **Trường Hợp Thực Tế**

Import sai entry của library làm kéo cả package lớn vào initial bundle.

### 🔍 **Cách Kiểm Chứng**

Bundle analyzer, production build, dependency graph, inspect package.json exports.

### 🤔 **Câu Hỏi Follow-up**

- Vì sao ESM tree-shake tốt hơn?
  Trả lời ngắn: ESM có import/export static, giúp bundler biết phần nào không dùng.
- Dynamic import khác static import?
  Trả lời ngắn: Dynamic import tải module theo nhu cầu runtime và thường tạo code split chunk.
- `sideEffects` nguy hiểm thế nào?
  Trả lời ngắn: Khai báo sai có thể khiến bundler xóa code có tác dụng phụ như CSS/polyfill.

### ❌ **Lỗi Cần Tránh**

- Nghĩ CJS/ESM chỉ khác syntax.
- Không test production bundle.
- Named import từ CJS mà không kiểm interop.

---

## 📌 **Topic21 - Frontend Tooling & Build Optimization**

### ⚡ **30 Giây - Quick Answer**

Build pipeline gồm transpile, polyfill, bundle, tree-shake, minify, code split và source map. Tối ưu phải dựa trên đo đạc.

### 📚 **2 Phút - Deep Dive**

Khi bundle nặng, em dùng analyzer để xem dependency nào lớn, duplicate không, import entry sai không. Sau đó mới lazy load, thay library, chỉnh browser target hoặc tách chunk. Code splitting giảm initial load nhưng quá nhiều chunk gây waterfall. Polyfill tăng compatibility nhưng tăng bundle. Source map production cần cân nhắc security và debugging.

### 💼 **Trường Hợp Thực Tế**

App import toàn bộ date library cho vài format đơn giản, làm initial JS tăng mạnh.

### 🔍 **Cách Kiểm Chứng**

Bundle analyzer, Lighthouse, WebPageTest, Chrome Coverage, production build size budget.

### 🤔 **Câu Hỏi Follow-up**

- Transpile khác polyfill?
  Trả lời ngắn: Transpile đổi syntax; polyfill thêm API runtime chưa có.
- Khi nào code splitting phản tác dụng?
  Trả lời ngắn: Khi tách quá nhỏ gây nhiều request, waterfall hoặc delay interaction.
- Source map production có rủi ro gì?
  Trả lời ngắn: Có thể lộ source, logic nhạy cảm hoặc làm attacker dễ phân tích app hơn.

### ❌ **Lỗi Cần Tránh**

- Chỉ test dev build.
- Split chunk quá nhỏ.
- Polyfill thừa cho browser target.

---

## 📌 **Topic22 - Cancellation, Concurrency, Retry, Race Condition**

### ⚡ **30 Giây - Quick Answer**

UI async cần kiểm soát cancel, concurrency, retry và race. Debounce chỉ giảm request, không đảm bảo response cũ không ghi đè UI mới.

### 📚 **2 Phút - Deep Dive**

Khi user đổi search/filter/navigate, request cũ có thể không còn hợp lệ. Em dùng `AbortController`, request id hoặc last-request-wins guard. Retry chỉ cho lỗi tạm thời, có max retry, backoff và jitter. `GET` retry an toàn hơn `POST`; POST tạo resource cần idempotency key. Concurrency limit bảo vệ cả client và server.

### 💼 **Trường Hợp Thực Tế**

User search "react", rồi "redux"; response "react" về sau và ghi đè kết quả "redux".

### 🔍 **Cách Kiểm Chứng**

Network throttling, request id logs, fake timer test, MSW/mock server, abort signal test.

### 🤔 **Câu Hỏi Follow-up**

- Cancel request và ignore response khác nhau thế nào?
  Trả lời ngắn: Cancel dừng request nếu được hỗ trợ; ignore chỉ không dùng kết quả khi nó về.
- Retry lỗi nào?
  Trả lời ngắn: Retry lỗi tạm thời như network, timeout, `429`, `5xx`, không retry lỗi business/client.
- Last-request-wins implement ra sao?
  Trả lời ngắn: Gắn request id/sequence và chỉ update UI nếu response thuộc request mới nhất.

### ❌ **Lỗi Cần Tránh**

- Chỉ debounce không guard.
- Retry mọi lỗi kể cả 400/401.
- Không cleanup khi unmount.

---

## 📌 **Topic23 - Big-O với Map, Set, Array, Object**

### ⚡ **30 Giây - Quick Answer**

Big-O giúp chọn data structure theo lookup, insert, delete và scale. Frontend vẫn cần Big-O khi xử lý table, list, selected ids hoặc join data.

### 📚 **2 Phút - Deep Dive**

Array tốt cho ordered list và render. `Set` tốt cho membership/dedupe. `Map` tốt cho lookup theo key và preserve insertion order. Object vẫn ổn cho dictionary string key đơn giản. Bottleneck phổ biến là nested loop hoặc array membership check lớn. Senior tối ưu thuật toán trước khi đổi cú pháp loop.

### 💼 **Trường Hợp Thực Tế**

Checkbox selected state dùng array `.includes()` với hàng nghìn row; đổi sang `Set` để membership check nhanh và code rõ hơn.

### 🔍 **Cách Kiểm Chứng**

Profiler, production-like dataset, complexity review, flamegraph transform data.

### 🤔 **Câu Hỏi Follow-up**

- `Map` khác Object?
  Trả lời ngắn: `Map` hỗ trợ key đa kiểu, preserve insertion order rõ và API size/iteration tốt hơn.
- Khi nào `Set` tốt hơn Array?
  Trả lời ngắn: Khi cần membership check hoặc dedupe nhiều phần tử.
- Big-O có phải lúc nào cũng quyết định performance?
  Trả lời ngắn: Không; constants, memory, engine optimization và data size thực tế cũng quan trọng.

### ❌ **Lỗi Cần Tránh**

- `.find()` trong loop lớn.
- Dùng array cho membership lớn.
- Bỏ qua memory tradeoff.

---

## 📌 **Topic24 - URL đến UI / Critical Rendering Path**

### ⚡ **30 Giây - Quick Answer**

Từ URL đến UI gồm DNS, TCP/TLS, request HTML, parse DOM/CSSOM, render tree, layout, paint, composite và chạy JS/hydration nếu có.

### 📚 **2 Phút - Deep Dive**

CSS thường render-blocking, JS có thể parser-blocking. SSR cải thiện first HTML nhưng vẫn có hydration cost. Tối ưu page load không chỉ là React; còn TTFB, cache, critical CSS, preload, image size, script defer/async, fetch waterfall và Core Web Vitals. Cần đặt size media để tránh CLS và giảm JS trên critical path.

### 💼 **Trường Hợp Thực Tế**

Landing page SSR nhưng tải ảnh hero quá lớn, CSS/JS block nhiều nên LCP vẫn tệ.

### 🔍 **Cách Kiểm Chứng**

Lighthouse, WebPageTest waterfall, Chrome Performance, Core Web Vitals, Network priority.

### 🤔 **Câu Hỏi Follow-up**

- CSS render-blocking nghĩa là gì?
  Trả lời ngắn: Browser thường phải tải/parse CSS trước khi paint để tránh render sai style.
- Hydration cost là gì?
  Trả lời ngắn: Chi phí JS gắn event/state vào HTML đã render từ server.
- Tối ưu LCP bắt đầu từ đâu?
  Trả lời ngắn: Xác định LCP element, rồi tối ưu TTFB, resource priority, image/font/CSS/JS blocking.

### ❌ **Lỗi Cần Tránh**

- Chỉ nhìn bundle mà bỏ qua network/cache.
- Fetch waterfall trong render path.
- Không đặt size ảnh gây CLS.

---

## 📌 **Topic25 - TypeScript Advanced Patterns**

### ⚡ **30 Giây - Quick Answer**

Em dùng TypeScript để encode domain rule, không chỉ để annotate object. Nhưng type không thay thế runtime validation ở API boundary.

### 📚 **2 Phút - Deep Dive**

Discriminated union hợp cho UI state như loading/success/error để tránh state không hợp lệ. Branded type giúp không nhầm `UserId` với `OrderId`. `unknown` tốt hơn `any` ở boundary vì buộc kiểm tra trước khi dùng. Type guard giúp narrow runtime data. Mapped/conditional type giúp giảm duplication, nhưng type quá phức tạp làm team khó maintain thì không đáng.

### 💼 **Trường Hợp Thực Tế**

State có `isLoading`, `data`, `error` riêng lẻ tạo trạng thái vô lý: vừa loading vừa có error. Đổi sang discriminated union làm UI xử lý rõ hơn.

### 🔍 **Cách Kiểm Chứng**

`tsc --noEmit`, type tests nếu có, schema validation bằng Zod/Yup/io-ts ở boundary, review generated API types.

### 🤔 **Câu Hỏi Follow-up**

- `unknown` khác `any`?
  Trả lời ngắn: `unknown` buộc kiểm tra/narrow trước khi dùng; `any` tắt type safety.
- Discriminated union giúp UI state ra sao?
  Trả lời ngắn: Nó biểu diễn các trạng thái hợp lệ riêng biệt và tránh combination vô lý.
- Branded type dùng khi nào?
  Trả lời ngắn: Khi nhiều giá trị cùng primitive type nhưng không được nhầm lẫn, như `UserId` và `OrderId`.

### ❌ **Lỗi Cần Tránh**

- Dùng `any` cho nhanh.
- Tin TypeScript validate runtime data.
- Viết type quá ảo không ai đọc nổi.

---

## 📌 **Topic26 - React Lifecycle**

### ⚡ **30 Giây - Quick Answer**

React lifecycle hiện đại là render, commit, effects. Render phải pure; side effect như fetch, subscribe, timer, DOM work nằm trong effect phù hợp và cần cleanup.

### 📚 **2 Phút - Deep Dive**

Render tính UI mới, commit thay đổi DOM, `useEffect` thường chạy sau paint, `useLayoutEffect` chạy trước paint nên chỉ dùng khi cần đo layout hoặc sync DOM trước khi user thấy. Dependency array là contract với closure, không phải thứ để tắt warning. StrictMode double invoke giúp lộ side effect sai trong dev.

### 💼 **Trường Hợp Thực Tế**

Component subscribe WebSocket nhưng không cleanup khi unmount, dẫn đến nhận message trùng và memory leak.

### 🔍 **Cách Kiểm Chứng**

React DevTools, hooks lint, console trace mount/unmount, memory profile, StrictMode test.

### 🤔 **Câu Hỏi Follow-up**

- `useEffect` khác `useLayoutEffect`?
  Trả lời ngắn: `useEffect` chạy sau paint; `useLayoutEffect` chạy trước paint và có thể block hiển thị.
- Vì sao render phải pure?
  Trả lời ngắn: React có thể render lại, bỏ render hoặc render nhiều lần; side effect trong render gây bug khó đoán.
- Dependency array liên quan closure thế nào?
  Trả lời ngắn: Dependency quyết định effect/callback capture version nào của biến bên ngoài.

### ❌ **Lỗi Cần Tránh**

- Side effect trong render.
- Tắt eslint deps để hết warning.
- Thiếu cleanup subscription/timer.

---

## 📌 **Topic27 - React Performance**

### ⚡ **30 Giây - Quick Answer**

React performance bắt đầu bằng đo đạc. Em tìm nguyên nhân re-render: props reference đổi, context update rộng, list lớn, calculation nặng hoặc component structure chưa hợp lý.

### 📚 **2 Phút - Deep Dive**

Em dùng React Profiler để xem component nào render nhiều và tốn thời gian. Sau đó mới chọn `React.memo`, `useMemo/useCallback`, split context, selector store, virtualization, code splitting hoặc move state xuống gần nơi dùng. Memoization có cost và làm code khó đọc nếu rải bừa. Key ổn định rất quan trọng khi list reorder.

### 💼 **Trường Hợp Thực Tế**

Một Context chứa user, theme, notification count, permissions. Notification update mỗi giây làm nhiều subtree re-render; tách context hoặc dùng selector store giảm render rộng.

### 🔍 **Cách Kiểm Chứng**

React DevTools Profiler flamegraph/ranked chart, why-did-you-render, Chrome Performance, production-like data.

### 🤔 **Câu Hỏi Follow-up**

- Khi nào `React.memo` không giúp?
  Trả lời ngắn: Khi props luôn đổi reference, render rẻ, hoặc bottleneck nằm ngoài component đó.
- Context gây re-render rộng thế nào?
  Trả lời ngắn: Khi provider value đổi, mọi consumer liên quan có thể re-render.
- Virtualization tradeoff là gì?
  Trả lời ngắn: Giảm DOM node nhưng tăng complexity về dynamic height, keyboard nav, a11y và scroll behavior.

### ❌ **Lỗi Cần Tránh**

- Memo mọi thứ không đo.
- Dùng index key với list reorder.
- Test với dataset quá nhỏ.

---

## 📌 **Topic28 - Web Security**

### ⚡ **30 Giây - Quick Answer**

Frontend không phải security boundary cuối. Server vẫn validate permission/input. Frontend giảm rủi ro XSS, CSRF, token leak, CORS misuse và dependency risk.

### 📚 **2 Phút - Deep Dive**

XSS có thể stored, reflected hoặc DOM-based; giảm bằng output encoding, sanitize raw HTML và CSP. Nếu dùng cookie auth, cần nghĩ CSRF bằng SameSite hoặc CSRF token. HttpOnly cookie chống JS đọc token nhưng không tự giải quyết CSRF. CORS không phải authentication. Frontend role chỉ phục vụ UX, backend vẫn authorize. Dependency supply-chain cũng cần lockfile, audit và review package.

### 💼 **Trường Hợp Thực Tế**

Rich text comment render bằng raw HTML không sanitize, attacker chèn script lấy user data.

### 🔍 **Cách Kiểm Chứng**

Security review, CSP report-only, dependency audit, SAST nếu có, E2E authz negative test, browser security headers.

### 🤔 **Câu Hỏi Follow-up**

- XSS stored/reflected/DOM-based khác nhau?
  Trả lời ngắn: Stored lưu payload trên server, reflected trả ngay trong response, DOM-based xảy ra do client JS xử lý unsafe.
- HttpOnly cookie có nhược điểm gì?
  Trả lời ngắn: JS không đọc được là tốt, nhưng cookie tự gửi nên vẫn cần CSRF strategy.
- CORS có phải auth không?
  Trả lời ngắn: Không; CORS chỉ là browser policy kiểm soát cross-origin request/response access.

### ❌ **Lỗi Cần Tránh**

- Lưu refresh token localStorage.
- Render raw HTML không sanitize.
- Tin frontend route guard là bảo mật.

---

## 📌 **Topic29 - Next.js Workflow**

### ⚡ **30 Giây - Quick Answer**

Với Next.js, em chọn route và rendering strategy trước. Giữ phần không cần interactivity ở Server Component, chỉ dùng Client Component khi cần state, event handler hoặc browser API.

### 📚 **2 Phút - Deep Dive**

App Router đưa thêm Server Component, streaming, loading/error boundary, fetch caching và Server Actions. Em tránh đặt `'use client'` quá rộng vì làm tăng JS client và mất lợi ích server rendering. Data fetching nên tránh waterfall, cache user-specific data phải cực kỳ cẩn thận. Debug Next cần kiểm cả server log, client hydration, cache layer và deployment platform.

### 💼 **Trường Hợp Thực Tế**

Developer thêm `'use client'` ở layout root, kéo nhiều dependency xuống client và bundle tăng mạnh.

### 🔍 **Cách Kiểm Chứng**

Next build output, bundle analyzer, server logs, Network waterfall, hydration warning, cache headers.

### 🤔 **Câu Hỏi Follow-up**

- Server Component khác Client Component?
  Trả lời ngắn: Server Component chạy trên server và không gửi JS component đó xuống client; Client Component hỗ trợ state/event/browser API.
- Fetch caching mặc định cần chú ý gì?
  Trả lời ngắn: Phải hiểu data static, dynamic hay user-specific để tránh stale hoặc leak dữ liệu.
- Streaming giúp gì?
  Trả lời ngắn: Cho phép gửi UI từng phần sớm hơn, cải thiện perceived performance.

### ❌ **Lỗi Cần Tránh**

- `'use client'` quá rộng.
- SSR xong client fetch lại toàn bộ.
- Cache nhầm user-specific data.

---

## 📌 **Topic30 - CSR vs SSR**

### ⚡ **30 Giây - Quick Answer**

CSR, SSR, SSG, ISR là rendering strategies. Không có strategy tốt nhất; chọn theo SEO, freshness, personalization, performance, infra cost và complexity.

### 📚 **2 Phút - Deep Dive**

CSR hợp app nội bộ, tương tác cao, không cần SEO nhiều. SSR hợp page cần SEO và data theo request nhưng có TTFB, server cost và hydration cost. SSG/ISR hợp content cacheable. SSR không tự làm app nhanh nếu JS/hydration nặng. Hybrid thường thực tế nhất: route nào cần gì dùng strategy đó.

### 💼 **Trường Hợp Thực Tế**

Dashboard nội bộ chuyển toàn bộ sang SSR nhưng không cải thiện UX vì bottleneck là API waterfall và client hydration nặng.

### 🔍 **Cách Kiểm Chứng**

TTFB, LCP, hydration timing, WebPageTest, server metrics, RUM theo route.

### 🤔 **Câu Hỏi Follow-up**

- SSR có luôn nhanh hơn CSR không?
  Trả lời ngắn: Không; SSR có thể cải thiện first HTML nhưng vẫn có TTFB và hydration cost.
- Hydration mismatch do đâu?
  Trả lời ngắn: Server HTML khác client render do time/random/browser API/data không đồng bộ.
- ISR hợp use case nào?
  Trả lời ngắn: Content cacheable, ít đổi nhưng cần refresh định kỳ như blog, catalog, docs.

### ❌ **Lỗi Cần Tránh**

- SSR mọi thứ.
- Leak secret/server data sang client.
- Bỏ qua cache strategy.

---

## 📌 **Topic31 - React Query**

### ⚡ **30 Giây - Quick Answer**

React Query quản lý server state: fetch, cache, dedupe, stale data, retry, refetch và invalidation. Nó không thay thế mọi client state.

### 📚 **2 Phút - Deep Dive**

Query key là contract cache, phải stable và đủ filter/page/user id. `staleTime` quyết định khi nào data cũ; `gcTime`/`cacheTime` quyết định giữ cache bao lâu sau khi không còn observer. Mutation xong cần invalidate hoặc update cache. Optimistic update phải có rollback. Cancellation giúp tránh response cũ ghi đè hoặc request không cần thiết.

### 💼 **Trường Hợp Thực Tế**

Query key thiếu `filter`, user đổi filter nhưng vẫn thấy cache cũ của filter trước.

### 🔍 **Cách Kiểm Chứng**

React Query Devtools, Network tab, query key review, MSW tests, cache invalidation tests.

### 🤔 **Câu Hỏi Follow-up**

- Server state khác client state?
  Trả lời ngắn: Server state thuộc backend, có cache/freshness/refetch; client state là UI/local interaction state.
- `staleTime` khác `gcTime`?
  Trả lời ngắn: `staleTime` là thời gian data còn fresh; `gcTime` là thời gian cache giữ sau khi không còn dùng.
- Optimistic update rollback thế nào?
  Trả lời ngắn: Lưu snapshot cache trước mutation, update tạm, nếu fail thì restore snapshot.

### ❌ **Lỗi Cần Tránh**

- Query key thiếu dimension.
- Refetch quá nhiều vì staleTime sai.
- Mutation xong quên invalidate.

---

## 📌 **Topic32 - AG Grid Enterprise**

### ⚡ **30 Giây - Quick Answer**

AG Grid không chỉ là table UI; nó là bài toán data grid performance, UX, server contract và update strategy.

### 📚 **2 Phút - Deep Dive**

Với data lớn, em dùng server-side row model hoặc pagination, row/column virtualization, stable `getRowId`, delta updates và debounce filter. Server-side sort/filter/pagination cần API contract rõ. Custom cell renderer phải nhẹ; column definitions nên stable/memoized. Realtime update cần batching, identity và tránh refresh toàn grid.

### 💼 **Trường Hợp Thực Tế**

Realtime price grid recreate `columnDefs` mỗi render và refresh toàn bảng mỗi tick, gây lag nghiêm trọng.

### 🔍 **Cách Kiểm Chứng**

AG Grid performance docs/tools, React Profiler, Chrome Performance, row id logs, large dataset test.

### 🤔 **Câu Hỏi Follow-up**

- Client-side row model giới hạn ở đâu?
  Trả lời ngắn: Khi data quá lớn hoặc sort/filter/pagination cần xử lý ở server để tránh lag và tải nặng.
- Vì sao `getRowId` quan trọng?
  Trả lời ngắn: Nó giúp grid nhận diện row ổn định để update delta thay vì refresh rộng.
- Realtime update grid nên batch thế nào?
  Trả lời ngắn: Gom nhiều update theo interval/frame rồi apply transaction một lần.

### ❌ **Lỗi Cần Tránh**

- Client filter hàng trăm nghìn rows.
- Custom cell renderer nặng.
- Recreate columnDefs mỗi render.

---

## 📌 **Topic33 - State Management: Redux vs Zustand vs Context**

### ⚡ **30 Giây - Quick Answer**

Em phân loại state trước khi chọn tool: local state, global UI state, server state, form state, URL state. Không dùng Redux/Zustand/Context theo trend.

### 📚 **2 Phút - Deep Dive**

Local state để gần component. Server state dùng React Query/SWR tốt hơn tự viết cache. Context hợp dependency/config hoặc state ít đổi, nhưng không nên chứa high-frequency state vì re-render rộng. Zustand nhẹ, ít boilerplate, hợp global UI state. Redux hợp enterprise cần convention, middleware, DevTools, audit trail và team scale.

### 💼 **Trường Hợp Thực Tế**

Đưa toàn bộ API data vào Redux rồi tự viết loading/error/cache/invalidation, cuối cùng phức tạp hơn React Query.

### 🔍 **Cách Kiểm Chứng**

React Profiler, Redux DevTools/Zustand devtools, render count, state ownership review.

### 🤔 **Câu Hỏi Follow-up**

- Context có phải state management tool không?
  Trả lời ngắn: Có thể dùng cho state đơn giản/ít đổi, nhưng không tối ưu cho high-frequency updates.
- Server state nên để đâu?
  Trả lời ngắn: Thường nên dùng React Query/SWR thay vì global client store tự viết cache.
- Khi nào Redux vẫn đáng dùng?
  Trả lời ngắn: Khi app/team lớn cần convention, middleware, DevTools, audit trail và flow rõ.

### ❌ **Lỗi Cần Tránh**

- Global store cho mọi thứ.
- Context chứa state update liên tục.
- Trộn server cache với UI state tùy tiện.

---

## 📌 **Topic34 - React 19 Migration**

### ⚡ **30 Giây - Quick Answer**

React 19 migration không chỉ bump version. Em kiểm ecosystem compatibility, test SSR/hydration/effects/forms, rồi rollout từng bước.

### 📚 **2 Phút - Deep Dive**

Trước migration cần kiểm framework, router, testing library, UI library, form library, build tool. Sau đó chạy typecheck/test/build, kiểm behavior thay vì chỉ fix compile. API mới như actions, form hooks, `use`, ref changes nên migrate có kiểm soát. StrictMode/effects có thể lộ bug cũ. Rollout từng phần giảm risk.

### 💼 **Trường Hợp Thực Tế**

Upgrade React nhưng UI library chưa support đầy đủ, modal/focus behavior lỗi trong production.

### 🔍 **Cách Kiểm Chứng**

Compatibility matrix, test suite, visual regression, SSR hydration logs, canary release metrics.

### 🤔 **Câu Hỏi Follow-up**

- Vì sao không upgrade đồng loạt?
  Trả lời ngắn: Vì blast radius lớn; migrate từng phần giúp dễ isolate bug và rollback.
- Kiểm hydration issue thế nào?
  Trả lời ngắn: Chạy SSR build, xem hydration warnings, test route quan trọng và so server/client output.
- Third-party package risk xử lý ra sao?
  Trả lời ngắn: Kiểm compatibility, changelog, peer deps, issue tracker và test behavior quan trọng.

### ❌ **Lỗi Cần Tránh**

- Chỉ bump version.
- Không test SSR/hydration.
- Bỏ qua ecosystem compatibility.

---

## 📌 **Topic35 - WebSocket & Real-Time Streaming**

### ⚡ **30 Giây - Quick Answer**

Realtime không chỉ mở socket. Cần reconnect, heartbeat, auth refresh, dedupe, ordering, backpressure và fallback strategy.

### 📚 **2 Phút - Deep Dive**

WebSocket hợp bidirectional như chat/trading. SSE hợp server-to-client notification đơn giản. Polling hợp case đơn giản hoặc fallback. Reconnect cần exponential backoff + jitter để tránh reconnect storm. Message nên có id/sequence để dedupe/order. Socket sống lâu phải xử lý token expiry/logout/multi-tab. Nếu data quá nhanh, cần batching/throttling/backpressure.

### 💼 **Trường Hợp Thực Tế**

Mất mạng làm hàng nghìn client reconnect cùng lúc, server spike vì không có backoff/jitter.

### 🔍 **Cách Kiểm Chứng**

Network WS inspector, message id logs, synthetic disconnect test, server connection metrics, client memory profile.

### 🤔 **Câu Hỏi Follow-up**

- WebSocket vs SSE vs polling?
  Trả lời ngắn: WebSocket hai chiều, SSE một chiều server-to-client, polling là client hỏi định kỳ.
- Reconnect storm là gì?
  Trả lời ngắn: Nhiều client reconnect cùng lúc sau outage, gây spike server.
- Message out-of-order xử lý ra sao?
  Trả lời ngắn: Dùng sequence/timestamp/id để reorder, dedupe hoặc bỏ message cũ.

### ❌ **Lỗi Cần Tránh**

- Tin message luôn đúng thứ tự.
- Không cleanup socket khi logout/unmount.
- Không handle token refresh.

---

## 📌 **Topic36 - Hashing, Encryption & Digital Signatures**

### ⚡ **30 Giây - Quick Answer**

Hash là one-way fingerprint, encryption mã hóa có thể giải mã, digital signature dùng private key ký và public key verify. Frontend không giữ secret an toàn.

### 📚 **2 Phút - Deep Dive**

Hash dùng kiểm toàn vẹn hoặc password hash ở backend với salt và slow algorithm. Encryption bảo vệ nội dung, cần key management. Signature xác minh nguồn gốc/toàn vẹn, ví dụ JWT thường signed chứ không encrypted. Secret trong frontend bundle không secret vì user inspect được. Không tự thiết kế crypto; dùng chuẩn và thư viện đáng tin.

### 💼 **Trường Hợp Thực Tế**

Đặt API secret trong `.env` public của frontend, build xong ai cũng xem được trong bundle.

### 🔍 **Cách Kiểm Chứng**

Bundle search secret, secret scanning, security review, JWT debugger chỉ cho dev, HTTPS/header check.

### 🤔 **Câu Hỏi Follow-up**

- Hash khác encryption?
  Trả lời ngắn: Hash one-way; encryption two-way nếu có key giải mã.
- JWT signed có nghĩa là dữ liệu được giấu không?
  Trả lời ngắn: Không; signed chỉ xác minh toàn vẹn/nguồn gốc, payload vẫn có thể đọc nếu không encrypted.
- Vì sao frontend không giữ secret?
  Trả lời ngắn: Code frontend nằm trên máy user và có thể inspect trong bundle/runtime.

### ❌ **Lỗi Cần Tránh**

- Gọi hash là encryption.
- Tự viết crypto.
- Đưa secret vào frontend env public.

---

## 📌 **Topic37 - Date & Time Handling**

### ⚡ **30 Giây - Quick Answer**

Date/time khó vì timezone, DST, locale và business rule. Em tách storage/transport và display rõ ràng.

### 📚 **2 Phút - Deep Dive**

Instant nên trao đổi bằng ISO UTC hoặc timestamp rõ timezone. Local date như ngày sinh/ngày booking có thể không phải instant UTC đơn giản. Display format theo locale/timezone của user hoặc business rule. Tránh parse string mơ hồ như `01/02/2024`. Date range nên định nghĩa inclusive/exclusive boundary. DST làm cộng ngày bằng milliseconds dễ sai.

### 💼 **Trường Hợp Thực Tế**

Report "today" lệch một ngày với user khác timezone vì backend/frontend hiểu timezone khác nhau.

### 🔍 **Cách Kiểm Chứng**

Unit test nhiều timezone, fake timer, test DST boundary, `Intl.DateTimeFormat`, API contract timezone.

### 🤔 **Câu Hỏi Follow-up**

- UTC instant khác local date?
  Trả lời ngắn: UTC instant là một thời điểm cụ thể; local date là ngày theo lịch ở một timezone/business context.
- DST gây bug gì?
  Trả lời ngắn: Một ngày có thể không đúng 24 giờ, nên cộng milliseconds dễ lệch.
- Date range nên lưu boundary thế nào?
  Trả lời ngắn: Nên định nghĩa rõ inclusive/exclusive, timezone và format trao đổi với API.

### ❌ **Lỗi Cần Tránh**

- Parse date string không timezone.
- Cộng ngày bằng `24*60*60*1000` qua DST.
- Quên timezone là requirement.

---

## 📌 **Topic38 - Build Tools: Vite, Webpack, Rollup, SWC, Babel, Turbopack, esbuild**

### ⚡ **30 Giây - Quick Answer**

Mỗi tool có vai trò khác nhau. Vite mạnh ở modern app/dev server, Webpack mạnh ecosystem legacy, Rollup hợp library, SWC/esbuild nhanh cho transform/minify, Turbopack gắn Next ecosystem.

### 📚 **2 Phút - Deep Dive**

Em không đổi tool chỉ vì trend hoặc benchmark dev server. Cần kiểm production build, plugin/loader, source map, CI, browser target, SSR support, monorepo support và migration cost. Dev speed khác production build quality. Library build khác app build vì cần output format, tree-shaking và external deps rõ.

### 💼 **Trường Hợp Thực Tế**

Đổi Webpack sang Vite nhanh hơn ở dev nhưng một plugin legacy và dynamic import edge case làm production build lỗi.

### 🔍 **Cách Kiểm Chứng**

Build time, HMR time, production bundle analyzer, CI timing, source map check, integration tests.

### 🤔 **Câu Hỏi Follow-up**

- Vite vì sao dev nhanh?
  Trả lời ngắn: Dev server dùng native ESM và transform theo nhu cầu, tránh bundle toàn app lúc start.
- Rollup hợp library ở đâu?
  Trả lời ngắn: Output sạch, tree-shaking tốt và kiểm soát format/external deps rõ.
- SWC/Babel khác nhau về vai trò?
  Trả lời ngắn: Cả hai transform JS/TS; SWC nhanh hơn nhờ Rust, Babel có ecosystem plugin lâu đời.

### ❌ **Lỗi Cần Tránh**

- Chỉ benchmark dev server.
- Không test production build.
- Bỏ qua plugin ecosystem.

---

## 📌 **Topic39 - JavaScript Design Patterns for Frontend**

### ⚡ **30 Giây - Quick Answer**

Pattern là giải pháp cho vấn đề lặp lại, không phải thứ để khoe. Em dùng pattern khi nó giảm complexity thật.

### 📚 **2 Phút - Deep Dive**

Factory hợp tạo service/object có setup ẩn. Strategy hợp nhiều thuật toán cùng interface như export/sort/payment. Adapter hợp chuyển API response sang UI model. Observer/PubSub hợp subscription/event system nhưng dễ thành global hidden flow. React patterns như compound component, render props, HOC, custom hooks đều có tradeoff. Simplicity vẫn là ưu tiên.

### 💼 **Trường Hợp Thực Tế**

API mỗi provider trả format khác nhau; dùng Adapter để UI nhận một shape thống nhất.

### 🔍 **Cách Kiểm Chứng**

Code review complexity, dependency graph, unit test per strategy/adapter, maintainability review.

### 🤔 **Câu Hỏi Follow-up**

- Strategy khác Factory?
  Trả lời ngắn: Strategy chọn thuật toán cùng interface; Factory tạo object/service với setup ẩn.
- Khi nào pattern thành over-engineering?
  Trả lời ngắn: Khi abstraction phức tạp hơn vấn đề và làm team khó đọc/maintain.
- Custom hook có phải pattern không?
  Trả lời ngắn: Có; custom hook là pattern để tái sử dụng stateful logic trong React.

### ❌ **Lỗi Cần Tránh**

- Áp pattern khi vấn đề chưa đủ lớn.
- Singleton/global state làm test khó.
- Pattern che giấu data flow.

---

## 📌 **Topic40 - Microfrontend & Monorepo**

### ⚡ **30 Giây - Quick Answer**

Microfrontend giải quyết team ownership và independent deployment, không tự làm app nhanh hơn. Monorepo là cách quản lý nhiều app/package trong một repo.

### 📚 **2 Phút - Deep Dive**

Microfrontend có tradeoff lớn: shared dependencies, duplicate React, version drift, routing/auth/shared state, runtime failure và debug khó. Module Federation cần contract shell/remote và shared deps chặt. Nếu chỉ một team hoặc app chưa quá lớn, modular monolith hoặc monorepo package boundary rõ thường đơn giản hơn. Monorepo cần build cache, dependency graph, ownership và release strategy.

### 💼 **Trường Hợp Thực Tế**

Hai remote dùng version React/UI lib khác nhau, shell load lỗi ở runtime sau deploy độc lập.

### 🔍 **Cách Kiểm Chứng**

Runtime logs, remote manifest/version, observability trace qua shell/remote, bundle duplicate analysis, CI affected builds.

### 🤔 **Câu Hỏi Follow-up**

- Khi nào microfrontend đáng dùng?
  Trả lời ngắn: Khi cần team ownership/deploy độc lập ở quy mô tổ chức đủ lớn.
- Monorepo khác microfrontend?
  Trả lời ngắn: Monorepo là cách quản lý source; microfrontend là kiến trúc runtime/deployment frontend.
- Shared dependency trong Module Federation quản lý ra sao?
  Trả lời ngắn: Khai báo shared/singleton/version chặt và test compatibility giữa shell/remote.

### ❌ **Lỗi Cần Tránh**

- Chia microfrontend theo page tùy tiện.
- Share global state lung tung.
- Không có rollback/versioning strategy.

---

## 📌 **Topic41 - Git Workflow & Team Collaboration**

### ⚡ **30 Giây - Quick Answer**

Git workflow phục vụ collaboration: PR nhỏ, commit rõ, checks tự động, review theo risk và branch strategy phù hợp release model.

### 📚 **2 Phút - Deep Dive**

Rebase giúp history sạch nhưng không nên rebase shared branch bừa. Merge giữ history branch, squash làm main gọn nhưng mất granular commits. Conflict resolution phải hiểu logic hai phía, không chọn file mới/cũ máy móc. PR tốt có scope nhỏ, summary rõ, test evidence và context cho reviewer. CODEOWNERS/checks giúp scale team.

### 💼 **Trường Hợp Thực Tế**

PR lớn đổi cả refactor và feature, reviewer miss bug permission vì diff quá rộng.

### 🔍 **Cách Kiểm Chứng**

CI checks, `git diff`, PR size metrics, CODEOWNERS, review checklist.

### 🤔 **Câu Hỏi Follow-up**

- Merge vs rebase vs squash?
  Trả lời ngắn: Merge giữ lịch sử branch, rebase làm history tuyến tính, squash gom commit khi merge.
- Resolve conflict an toàn thế nào?
  Trả lời ngắn: Hiểu logic hai phía, chạy test liên quan và không chọn máy móc theo file mới/cũ.
- Làm PR dễ review ra sao?
  Trả lời ngắn: Scope nhỏ, mô tả rõ, diff tập trung, test evidence đầy đủ.

### ❌ **Lỗi Cần Tránh**

- PR quá lớn.
- Rebase shared branch tùy tiện.
- Resolve conflict không hiểu business logic.

---

## 📌 **Topic42 - Frontend System Design**

### ⚡ **30 Giây - Quick Answer**

Frontend system design không chỉ vẽ component tree. Em thiết kế user flow, data flow, rendering, state/cache, auth, error handling, performance, security, observability và rollout.

### 📚 **2 Phút - Deep Dive**

Em bắt đầu từ requirement: user là ai, flow chính, data cần gì, freshness, permission, non-functional requirements. Sau đó thiết kế data model/API boundary, rendering strategy, state ownership, cache invalidation, loading/error/empty state, retry/cancel, accessibility, monitoring, feature flag và failure mode. Tradeoff cần nói rõ giữa UX, correctness, performance, security và maintainability.

### 💼 **Trường Hợp Thực Tế**

Thiết kế order dashboard: React Query cho server state, URL state cho filter/page, optimistic update có rollback, permission từ backend, virtualized table, error boundary, RUM và Sentry.

### 🔍 **Cách Kiểm Chứng**

Architecture review, sequence diagram, RUM, Sentry, logs with correlation id, Core Web Vitals, synthetic/E2E tests.

### 🤔 **Câu Hỏi Follow-up**

- Cache invalidation thiết kế thế nào?
  Trả lời ngắn: Xác định owner/freshness, dùng query key rõ, invalidate/update cache sau mutation.
- API chậm/fail thì UI ra sao?
  Trả lời ngắn: Có loading, timeout/retry hợp lý, error state, fallback và không làm mất dữ liệu user.
- Permission nằm ở frontend hay backend?
  Trả lời ngắn: Backend là nơi quyết định bảo mật; frontend chỉ tối ưu UX bằng hide/show.

### ❌ **Lỗi Cần Tránh**

- Chỉ vẽ component tree.
- Bỏ qua failure mode.
- Không có observability.

---

## 📌 **Topic43 - Component Libraries Comparison**

### ⚡ **30 Giây - Quick Answer**

Chọn component library theo product/team constraint, không theo demo đẹp. Cần đánh giá a11y, customization, theming, bundle, docs, ecosystem và maintainability.

### 📚 **2 Phút - Deep Dive**

Styled libraries như MUI/AntD giúp ship nhanh nhưng dễ lock-in visual system và override CSS nhiều. Headless libraries như Radix/React Aria cho control markup/style cao hơn nhưng cần tự build visual system. Với enterprise app, table/form/modal/date picker phải kiểm keyboard, screen reader, performance và design token integration.

### 💼 **Trường Hợp Thực Tế**

Team chọn styled library rồi override CSS quá nhiều để match design system, sau upgrade bị vỡ UI hàng loạt.

### 🔍 **Cách Kiểm Chứng**

Accessibility audit, bundle analyzer, keyboard test, visual regression, theme token review.

### 🤔 **Câu Hỏi Follow-up**

- Headless vs styled khác nhau?
  Trả lời ngắn: Headless cung cấp behavior/a11y ít style; styled cung cấp UI hoàn chỉnh hơn.
- Chọn MUI/AntD/Radix dựa trên gì?
  Trả lời ngắn: Dựa vào design system, tốc độ ship, customization, a11y, bundle và team skill.
- Component library ảnh hưởng bundle thế nào?
  Trả lời ngắn: Import sai hoặc component nặng có thể kéo nhiều JS/CSS vào initial bundle.

### ❌ **Lỗi Cần Tránh**

- Chọn theo trend/demo.
- Không test a11y.
- Override quá nhiều làm khó upgrade.

---

## 📌 **Topic44 - Code Quality & Standards**

### ⚡ **30 Giây - Quick Answer**

Code quality là guardrail: Prettier xử lý format, ESLint bắt bug/risk, review tập trung correctness, CI enforce lint/typecheck/test/build.

### 📚 **2 Phút - Deep Dive**

Rule tốt là rule team tin và tuân thủ. Prettier tránh style war. ESLint không nên quá noise; ưu tiên bug, security, hooks, imports, accessibility. Code review nên xem edge case, tests, performance/security risk, maintainability. CI cần chạy tự động để tránh regression. Auto-fix càng nhiều càng tốt để giảm friction.

### 💼 **Trường Hợp Thực Tế**

Missing hook dependency bị ESLint cảnh báo nhưng team tắt rule, production gặp stale closure.

### 🔍 **Cách Kiểm Chứng**

CI pipeline, lint/typecheck/test/build, review checklist, defect trend, flaky test tracking.

### 🤔 **Câu Hỏi Follow-up**

- ESLint khác Prettier?
  Trả lời ngắn: Prettier format code; ESLint bắt bug/risk/pattern và một số style rule.
- Review nên ưu tiên gì?
  Trả lời ngắn: Correctness, edge cases, tests, security/performance risk và maintainability.
- Rule quá nhiều có hại thế nào?
  Trả lời ngắn: Noise cao làm team ignore warning hoặc tìm cách bypass.

### ❌ **Lỗi Cần Tránh**

- Review nitpick style đã có Prettier.
- Rule noise làm team ignore.
- Không enforce trong CI.

---

## 📌 **Topic45 - CSS Architecture & Modern Styling**

### ⚡ **30 Giây - Quick Answer**

CSS scale khó vì cascade, specificity, global leak và design drift. Chọn approach theo team, design system và runtime needs.

### 📚 **2 Phút - Deep Dive**

CSS Modules hợp scoped style đơn giản. Utility CSS tăng tốc và consistency nếu có convention. CSS-in-JS hợp theme dynamic/colocation nhưng có runtime hoặc build tradeoff tùy library. Headless + tokens hợp design system nghiêm túc. Dù dùng gì, cần design tokens cho color/spacing/typography, responsive rules rõ, accessibility và cascade layer/specificity strategy.

### 💼 **Trường Hợp Thực Tế**

Global CSS của một page override button trong modal khác vì selector quá rộng và specificity cao.

### 🔍 **Cách Kiểm Chứng**

DevTools computed styles, specificity audit, visual regression, design token review, CSS bundle size.

### 🤔 **Câu Hỏi Follow-up**

- CSS Modules vs Tailwind vs CSS-in-JS?
  Trả lời ngắn: CSS Modules scoped đơn giản, Tailwind utility nhanh/consistent, CSS-in-JS hợp dynamic theme/colocation.
- Cascade layers giúp gì?
  Trả lời ngắn: Quản lý thứ tự ưu tiên CSS rõ hơn, giảm specificity war.
- Design token giải quyết vấn đề nào?
  Trả lời ngắn: Chuẩn hóa màu, spacing, typography và giúp consistency giữa sản phẩm/nền tảng.

### ❌ **Lỗi Cần Tránh**

- Hardcode màu/spacing khắp nơi.
- Specificity war.
- Global leak giữa component.

---

## 📌 **Topic46 - Keycloak**

### ⚡ **30 Giây - Quick Answer**

Keycloak là identity provider/auth server. Với SPA hiện đại, em ưu tiên Authorization Code Flow with PKCE thay vì implicit flow.

### 📚 **2 Phút - Deep Dive**

Frontend dùng access token để gọi API, refresh/session strategy tùy kiến trúc. UI có thể ẩn/hiện theo role để cải thiện UX, nhưng backend vẫn validate permission. Cần hiểu realm, client, role, token claims, token expiry, silent renew, logout nhiều tab và storage strategy. Token trong browser là rủi ro, nên phải cân nhắc cookie/session/BFF tùy app.

### 💼 **Trường Hợp Thực Tế**

Frontend chỉ ẩn button theo role nhưng API không check permission, user gọi trực tiếp endpoint vẫn thành công.

### 🔍 **Cách Kiểm Chứng**

JWT claim inspect trong dev, network auth flow, backend authz negative test, multi-tab logout test, token expiry test.

### 🤔 **Câu Hỏi Follow-up**

- PKCE hơn implicit ở đâu?
  Trả lời ngắn: PKCE dùng authorization code flow an toàn hơn cho public client, tránh trả token trực tiếp qua URL fragment.
- Role trong token có đủ để authorize không?
  Trả lời ngắn: Không; backend vẫn phải verify token và kiểm permission cho từng API.
- Token refresh xử lý thế nào?
  Trả lời ngắn: Theo session strategy: silent renew/refresh token/BFF, có xử lý expiry, logout và race.

### ❌ **Lỗi Cần Tránh**

- Dùng implicit flow cũ.
- Lưu token sai chỗ.
- Tin frontend role guard là bảo mật.

---

## 📌 **Topic47 - Form Handling & Validation**

### ⚡ **30 Giây - Quick Answer**

Form production gồm value, touched/dirty, validation, error mapping, loading, submit, accessibility, server error và idempotency.

### 📚 **2 Phút - Deep Dive**

React Hook Form tốt vì uncontrolled input giảm re-render. Zod/Yup giúp schema rõ, nhưng client validation chỉ cải thiện UX; server vẫn validate. Async validation cần debounce/cancel. Server field error nên map đúng field và focus error đầu tiên. Submit cần loading/disable hoặc idempotency để tránh double submit. Error phải accessible với label, aria-describedby và screen reader support.

### 💼 **Trường Hợp Thực Tế**

User double click submit tạo hai order vì button không disable và backend không có idempotency key.

### 🔍 **Cách Kiểm Chứng**

React Profiler render form, accessibility audit, E2E validation paths, server error mapping test, network duplicate submit.

### 🤔 **Câu Hỏi Follow-up**

- Controlled vs uncontrolled form?
  Trả lời ngắn: Controlled lưu value trong React state; uncontrolled để DOM giữ value và đọc qua ref/form library.
- Client validation có đủ không?
  Trả lời ngắn: Không; client validation chỉ hỗ trợ UX, server vẫn phải validate.
- Server error map về field thế nào?
  Trả lời ngắn: Backend trả error code/path theo field, frontend set error đúng field và focus lỗi đầu tiên.

### ❌ **Lỗi Cần Tránh**

- Chỉ validate client.
- Mất data khi submit fail.
- Error không accessible.

---

## 📌 **Topic48 - Internationalization & Localization**

### ⚡ **30 Giây - Quick Answer**

i18n không chỉ dịch text. Nó gồm date, number, currency, plural, fallback, namespace lazy load, RTL và locale-aware sort/search.

### 📚 **2 Phút - Deep Dive**

Tránh hardcode string và nối string thủ công vì thứ tự từ khác nhau theo ngôn ngữ. ICU message giúp plural/gender/context. Locale ảnh hưởng format ngày/tiền/số và collation. Namespace giúp lazy load translation theo route. RTL không chỉ đổi text direction; layout, icon direction, spacing cũng cần kiểm. Timezone/currency là business requirement, không đoán.

### 💼 **Trường Hợp Thực Tế**

Chuỗi `"Hello " + name` dịch sang ngôn ngữ khác sai thứ tự hoặc thiếu context.

### 🔍 **Cách Kiểm Chứng**

Pseudo-localization, RTL visual test, missing key report, `Intl` tests, screenshot regression.

### 🤔 **Câu Hỏi Follow-up**

- i18n khác l10n?
  Trả lời ngắn: i18n là chuẩn bị hệ thống hỗ trợ nhiều locale; l10n là bản địa hóa cho locale cụ thể.
- Vì sao không concatenate translated string?
  Trả lời ngắn: Ngữ pháp/thứ tự từ khác nhau giữa ngôn ngữ, nối chuỗi dễ dịch sai context.
- RTL cần test gì?
  Trả lời ngắn: Direction, layout, icon hướng, spacing, scroll, form và component overlay.

### ❌ **Lỗi Cần Tránh**

- Hardcode text.
- Quên plural/currency/timezone.
- Không test layout dài hơn tiếng Anh.

---

## 📌 **Topic49 - Mobile-First Development**

### ⚡ **30 Giây - Quick Answer**

Mobile-first là thiết kế từ constraint thật: màn hình nhỏ, touch, safe area, keyboard, viewport unit quirks, network/device chậm hơn; không chỉ viết media query.

### 📚 **2 Phút - Deep Dive**

Layout nên stack tự nhiên trên mobile, text không sát mép, touch target khoảng 44px, input đủ lớn để tránh iOS zoom. `100vh` có issue với mobile browser chrome nên cân nhắc `svh/dvh`. Fixed bottom bar cần safe area và keyboard behavior. Hover không tồn tại như desktop. Responsive image ảnh hưởng performance. Test trên viewport/device thật quan trọng hơn chỉ resize desktop browser.

### 💼 **Trường Hợp Thực Tế**

Checkout mobile có fixed bottom CTA bị iOS keyboard che, user không submit được.

### 🔍 **Cách Kiểm Chứng**

Device emulation, real device test, Lighthouse mobile, WebPageTest mobile, responsive screenshot, touch/keyboard E2E.

### 🤔 **Câu Hỏi Follow-up**

- Mobile-first khác responsive thế nào?
  Trả lời ngắn: Mobile-first thiết kế từ constraint mobile trước; responsive chỉ nói UI thích nghi nhiều viewport.
- `svh/dvh` giải quyết gì?
  Trả lời ngắn: Giúp xử lý chiều cao viewport khi browser chrome mobile co giãn.
- Touch target nên chú ý gì?
  Trả lời ngắn: Kích thước đủ lớn, khoảng cách đủ rộng và không phụ thuộc hover.

### ❌ **Lỗi Cần Tránh**

- Ép desktop layout xuống mobile.
- Button quá nhỏ.
- Không test keyboard/safe area.

---

## Senior/Staff FE Answer Framework

Khi gặp một câu hỏi frontend, đừng chỉ định nghĩa. Hãy trả lời theo khung:

```text
1. Define: khái niệm là gì.
2. Why it matters: nó ảnh hưởng correctness/UX/performance/security ra sao.
3. Tradeoff: khi nào dùng, khi nào không.
4. Production case: lỗi thật hay gặp.
5. Debug/measure: dùng công cụ nào để kiểm chứng.
```

Ví dụ câu chốt:

> Em nhìn frontend như một hệ thống chạy trên browser, không chỉ là React component. Khi chọn giải pháp, em kiểm tra data có đúng không, request có race không, UI có render quá nhiều không, token có an toàn không, cache có stale không, bundle có nặng không, và team có maintain/debug được không.

---

## Checklist Tự Đánh Giá Trước Interview

- [ ] Tôi có bản trả lời 30 giây cho mỗi topic.
- [ ] Tôi có bản đào sâu 2 phút có tradeoff.
- [ ] Tôi kể được ít nhất một production case.
- [ ] Tôi biết debug/measure bằng tool cụ thể.
- [ ] Tôi biết lỗi phổ biến và cách tránh.
- [ ] Tôi nối được topic với React/browser/API/security/performance.
- [ ] Tôi không trả lời kiểu "luôn luôn dùng X".
- [ ] Tôi biết khi nào giải pháp đúng về lý thuyết nhưng sai trong production.
