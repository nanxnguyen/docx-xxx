# Frontend Topic Interview Mindmap — Topic01 → Topic49

> Mục tiêu: mỗi topic trong `Frontend/Topic` đều có một block trả lời phỏng vấn rõ ràng.
>
> Format cố định:
>
> - **Interviewer muốn nghe**: điều nhà tuyển dụng thật sự kiểm tra.
> - **Giải thích dễ hiểu**: nói sao cho người mới hiểu.
> - **Nói mẫu**: câu trả lời tự nhiên khi phỏng vấn.
> - **Điểm senior**: phần làm câu trả lời có chiều sâu.
> - **Lỗi cần tránh**: bẫy thường gặp.

---

## Cách Dùng File Này

Đừng học thuộc từng câu. Hãy dùng mỗi block để luyện theo 3 vòng:

1. Đọc **giải thích dễ hiểu** để hiểu bản chất.
2. Tập nói lại phần **nói mẫu** bằng lời của bạn.
3. Thêm **điểm senior** và **lỗi cần tránh** để câu trả lời có tradeoff.

Câu trả lời tốt thường có cấu trúc:

```text
Em hiểu đơn giản là...
Trong project thật nó xuất hiện khi...
Điểm cần cẩn thận là...
Nếu cần kiểm chứng/debug thì em sẽ...
```

---

## Topic01 — Claude Code Workflow

**Interviewer muốn nghe**

- Bạn biết dùng AI coding tool có kiểm soát, không phó mặc.
- Bạn hiểu context, token, memory, command, hook, agent.
- Bạn biết dùng AI để tăng tốc nhưng vẫn review, test, verify.

**Giải thích dễ hiểu**

Claude Code giống một assistant trong repo. Nó làm tốt khi được đưa đúng file, đúng task, đúng context. Context càng dài càng tốn token và dễ nhiễu.

**Nói mẫu**

> Em dùng Claude Code như một workflow có kiểm soát: task rõ, file path rõ, context gọn. Với task lớn em dùng plan mode trước, sau đó mới cho sửa. Em dùng custom command cho workflow lặp lại như rewrite topic, review topic, generate HTML. Em cũng setup hooks để sau khi edit có validate/lint. Điểm quan trọng là AI giúp tăng tốc, nhưng em vẫn phải đọc diff, chạy check và quyết định cuối cùng.

**Điểm senior**

- `/clear` khi đổi task để giảm context nhiễu.
- `/compact` khi session dài nhưng còn cần giữ history.
- `CLAUDE.md` chỉ nên chứa convention quan trọng, không nhồi tài liệu dài.
- Hook tốt cho rule không muốn AI quên: lint, validate, secret check.

**Lỗi cần tránh**

- Để session kéo dài nhiều task không clear.
- Hỏi quá chung kiểu “xem toàn bộ repo”.
- Tin output AI mà không kiểm diff/test.

---

## Topic02 — Data Types & Memory Management

**Interviewer muốn nghe**

- Bạn phân biệt primitive và object.
- Bạn hiểu value vs reference.
- Bạn liên hệ được với React render và immutable update.

**Giải thích dễ hiểu**

Primitive như `number`, `string`, `boolean` là giá trị trực tiếp. Object/array/function là dữ liệu được truy cập qua reference. Hai object nhìn giống nhau chưa chắc bằng nhau vì chúng có thể là hai reference khác nhau.

**Nói mẫu**

> Em hiểu data type trong JavaScript quan trọng nhất ở chỗ primitive copy theo value, còn object copy theo reference. Vì vậy `{ a: 1 } === { a: 1 }` là false. Trong React, điều này ảnh hưởng trực tiếp đến rendering vì React thường dựa vào reference equality. Nếu mình mutate state cũ rồi set lại cùng reference, React hoặc memoization có thể không nhận ra thay đổi đúng cách.

**Điểm senior**

- Shallow copy chỉ copy lớp ngoài.
- Deep clone tốn CPU và có thể phá structural sharing.
- GC dựa trên reachability: còn reference là còn sống.
- Money/decimal/large id không nên xử lý bừa bằng `number`.

**Lỗi cần tránh**

- Dùng `JSON.stringify` để compare/clone mọi object.
- Mutate state rồi nghĩ React lỗi.
- Dùng float cho tiền.

---

## Topic03 — Event Loop

**Interviewer muốn nghe**

- Bạn hiểu JS single-thread.
- Bạn phân biệt call stack, microtask, macrotask, render.
- Bạn dự đoán được thứ tự chạy của Promise/timer.

**Giải thích dễ hiểu**

Event loop là cơ chế giúp JavaScript xử lý code sync, Promise, timer, event và render UI theo thứ tự.

**Nói mẫu**

> Em hiểu event loop là cơ chế điều phối giữa call stack, microtask queue, macrotask queue và render. Code sync chạy trước. Sau đó microtask như `Promise.then` được xử lý trước macrotask như `setTimeout`. Vì vậy Promise thường log trước timer. Trong UI thật, nếu có long task hoặc microtask loop quá nhiều, browser không kịp paint và user thấy app bị đơ.

**Điểm senior**

- Microtask chạy hết trước khi browser chuyển phase tiếp theo.
- Long task ảnh hưởng input responsiveness.
- Rendering không xảy ra khi main thread đang bị block.
- Debug bằng Chrome Performance.

**Lỗi cần tránh**

- Nói `setTimeout(fn, 0)` chạy ngay.
- Không biết Promise callback là microtask.
- Dùng loop nặng trên main thread.

---

## Topic04 — Async/Await vs Promise vs Callback

**Interviewer muốn nghe**

- Bạn biết async/await là syntax trên Promise.
- Bạn chọn đúng `Promise.all`, `allSettled`, `race`, `any`.
- Bạn hiểu sequential vs parallel.

**Giải thích dễ hiểu**

Callback là cách truyền hàm chạy sau. Promise đại diện kết quả tương lai. Async/await giúp viết Promise dễ đọc hơn.

**Nói mẫu**

> Async/await không biến async thành sync, nó chỉ làm Promise dễ đọc hơn. Khi các request không phụ thuộc nhau, em chạy song song bằng `Promise.all`. Nếu cần lấy cả kết quả thành công và thất bại, em dùng `allSettled`. Nếu cần timeout hoặc lấy cái xong trước, em dùng `race`. Quan trọng là chọn theo dependency và error strategy.

**Điểm senior**

- `Promise.all` fail-fast.
- `allSettled` hợp dashboard partial data.
- `race` hợp timeout.
- `any` hợp fallback nhiều nguồn.

**Lỗi cần tránh**

- Await tuần tự không cần thiết.
- `forEach(async)` rồi nghĩ đã await.
- `try/catch` quá rộng làm khó debug.

---

## Topic05 — ES5 vs ES6+

**Interviewer muốn nghe**

- Bạn không chỉ kể syntax mới.
- Bạn hiểu runtime behavior: scope, TDZ, lexical `this`, modules.
- Bạn biết browser target, transpile, polyfill.

**Giải thích dễ hiểu**

ES6+ giúp JavaScript hiện đại hơn, nhưng khi chạy production phải đảm bảo browser target hiểu được code hoặc được build tool hỗ trợ.

**Nói mẫu**

> ES6+ không chỉ là viết code ngắn hơn. Nó thay đổi cách mình viết scope bằng `let/const`, tránh nhiều lỗi của `var`, dùng arrow function với lexical `this`, class syntax trên prototype, Promise và ES Modules. Khi đi production, em còn quan tâm browser target: syntax mới cần transpile, còn API mới cần polyfill nếu browser chưa hỗ trợ.

**Điểm senior**

- `let/const` có TDZ.
- Arrow không có `this` riêng.
- ESM giúp tree-shaking tốt hơn.
- Transpile khác polyfill.

**Lỗi cần tránh**

- Nghĩ `const` làm object immutable.
- Spread là deep copy.
- Quên polyfill runtime API.

---

## Topic06 — Closure & Data Privacy

**Interviewer muốn nghe**

- Bạn định nghĩa closure đúng.
- Bạn biết closure giữ reference, không phải snapshot.
- Bạn liên hệ được stale closure và memory leak.

**Giải thích dễ hiểu**

Closure là function vẫn nhớ biến ở scope ngoài dù scope đó đã chạy xong.

**Nói mẫu**

> Closure là function cộng với lexical environment nơi nó được tạo ra. Inner function giữ reference tới biến outer, không phải copy giá trị. Vì vậy closure rất hữu ích cho private state, debounce, memoize hoặc store kiểu Zustand. Nhưng trong React nó cũng gây stale closure, ví dụ `setInterval` trong `useEffect([])` đọc mãi state cũ nếu mình không dùng functional updater hoặc ref.

**Điểm senior**

- Closure là cơ chế, privacy chỉ là use case.
- Closure có thể giữ object lớn sống lâu hơn cần.
- `#private` và `WeakMap` là alternative cho private data.

**Lỗi cần tránh**

- Gọi closure là snapshot.
- Quên cleanup listener/timer.
- Return reference private data ra ngoài.

---

## Topic07 — Arrow vs Regular Function & `this`

**Interviewer muốn nghe**

- Bạn biết `this` phụ thuộc cách gọi function.
- Bạn phân biệt arrow và regular function.
- Bạn biết `call/apply/bind` dùng khi nào.

**Giải thích dễ hiểu**

Regular function có `this` động. Arrow function không có `this` riêng, nó lấy `this` từ scope bên ngoài.

**Nói mẫu**

> Em dùng arrow function cho callback vì nó giữ `this` từ scope ngoài. Nhưng với object method, class method hoặc prototype method, em thường dùng regular function vì `this` cần phụ thuộc object gọi method. `call`, `apply`, `bind` chỉ đổi được `this` của regular function, không đổi được `this` của arrow.

**Điểm senior**

- Class method không auto bind.
- Arrow field tạo function riêng mỗi instance.
- Prototype method tiết kiệm memory hơn.

**Lỗi cần tránh**

- Destructure method làm mất `this`.
- Dùng arrow cho method cần dynamic `this`.
- Tin `bind` sửa được arrow function.

---

## Topic08 — IIFE & Functional Programming

**Interviewer muốn nghe**

- Bạn biết IIFE từng dùng để tạo scope riêng trước ES Modules.
- Bạn hiểu functional programming ở frontend là pure function, immutability, composition.
- Bạn biết tradeoff giữa declarative và imperative.

**Giải thích dễ hiểu**

IIFE là function được gọi ngay sau khi tạo. Functional programming là cách viết code ít side effect, dễ test và dễ compose hơn.

**Nói mẫu**

> IIFE ngày xưa dùng nhiều để tạo scope riêng và tránh pollute global scope. Bây giờ ES Modules thay phần lớn vai trò đó. Còn functional programming trong frontend em hiểu thực tế là viết pure function, update immutable và compose logic để React/Redux dễ memoize, dễ test và ít bug hơn. Nhưng em không áp dụng máy móc; với hot path hoặc logic quá khó đọc, loop imperative đôi khi rõ và nhanh hơn sau khi đo.

**Điểm senior**

- Pure function giúp test dễ.
- Immutable update giúp React shallow compare.
- Memoization cần giới hạn cache.

**Lỗi cần tránh**

- Spread shallow nhưng tưởng deep.
- Lạm dụng `useMemo`.
- Viết functional chain dài khó đọc.

---

## Topic09 — JavaScript Proxy

**Interviewer muốn nghe**

- Bạn hiểu Proxy intercept operation trên object/function.
- Bạn biết use case: validation, logging, reactivity.
- Bạn biết overhead và identity issue.

**Giải thích dễ hiểu**

Proxy là lớp bọc cho phép chặn thao tác đọc, ghi, xóa, gọi hàm hoặc tạo instance.

**Nói mẫu**

> Proxy cho phép bọc object để intercept các thao tác như `get`, `set`, `deleteProperty`, `apply`, `construct`. Nó rất mạnh cho validation, logging, access control, reactivity kiểu Vue 3 hoặc form tracking. Khi dùng thực tế, em thường forward bằng `Reflect` để giữ behavior chuẩn. Tradeoff là Proxy không tự deep cho nested object, identity khác object gốc và có overhead nên em tránh dùng ở hot path.

**Điểm senior**

- Vue 3 reactivity dựa nhiều vào Proxy.
- Proxy phải tôn trọng invariant của JS engine.
- Nested object cần wrap riêng nếu muốn deep reactive.

**Lỗi cần tránh**

- Dùng Proxy cho mọi data path.
- Quên `Reflect`.
- So sánh proxy và object gốc bằng identity.

---

## Topic10 — JavaScript Classes

**Interviewer muốn nghe**

- Bạn biết class là syntax trên prototype chain.
- Bạn biết khi nào nên dùng class.
- Bạn hiểu tradeoff class vs factory/composition.

**Giải thích dễ hiểu**

Class giúp gom state và behavior vào một kiểu object có cấu trúc rõ hơn.

**Nói mẫu**

> JavaScript class là cú pháp dễ đọc hơn trên prototype chain. Em dùng class khi object có invariant, lifecycle hoặc dependency rõ ràng, ví dụ service, SDK client, custom error hoặc domain model. Nhưng trong frontend lớn em tránh inheritance sâu, ưu tiên composition và dependency injection để dễ test hơn. Em cũng để ý `#private` mới là private thật ở runtime, còn class method không tự bind `this`.

**Điểm senior**

- Prototype method tiết kiệm memory.
- Arrow field tiện binding nhưng tạo function mỗi instance.
- Composition thường dễ maintain hơn inheritance.

**Lỗi cần tránh**

- Lạm dụng inheritance.
- Nghĩ TypeScript `private` là runtime private.
- Mất `this` khi pass method làm callback.

---

## Topic11 — DOM Query, Manipulation & Events

**Interviewer muốn nghe**

- Bạn hiểu DOM là cây element browser tạo từ HTML.
- Bạn biết event flow: capture, target, bubble.
- Bạn biết event delegation, cleanup và XSS risk.

**Giải thích dễ hiểu**

DOM là cấu trúc mà browser dùng để biểu diễn UI. Event là cách browser báo user đang click, input, scroll hoặc tương tác.

**Nói mẫu**

> Em hiểu DOM event theo flow capture → target → bubble. Với list động hoặc nhiều item, em ưu tiên event delegation bằng cách gắn listener ở parent thay vì từng child. Khi manipulate DOM, em cẩn thận với `innerHTML` vì có XSS risk, thường ưu tiên `textContent`, `classList`, `dataset`. Trong React app, nếu DOM đã được quản lý bởi state/props thì em tránh sửa DOM trực tiếp để không làm lệch source of truth.

**Điểm senior**

- Cleanup listener bằng `removeEventListener` hoặc `AbortController`.
- Passive listener giúp scroll mượt hơn.
- Focus/accessibility cũng là phần của DOM work.

**Lỗi cần tránh**

- XSS qua `innerHTML`.
- Quên cleanup listener.
- DOM manipulation conflict với React render.

---

## Topic12 — Axios & Axios Interceptors

**Interviewer muốn nghe**

- Bạn biết interceptor là API boundary.
- Bạn xử lý auth, refresh token, retry, cancellation, error normalization.
- Bạn không nhét business logic/UI logic vào HTTP client.

**Giải thích dễ hiểu**

Interceptor là lớp chạy trước request hoặc sau response để xử lý logic HTTP dùng chung.

**Nói mẫu**

> Em dùng Axios interceptor như một API boundary. Request interceptor gắn token, locale, request id. Response interceptor normalize error, đo duration và xử lý `401`. Với refresh token, em tránh để nhiều request `401` gọi refresh nhiều lần bằng một shared refresh promise rồi replay request cũ. Retry thì em chỉ retry lỗi tạm thời như network, `429`, `5xx`, có max retry và backoff. Với `POST` tạo order/payment, em chỉ retry nếu có idempotency key.

**Điểm senior**

- Refresh token cần queue/lock.
- Retry cần max count, backoff, jitter.
- Abort/cancel giúp tránh response cũ ghi đè UI mới.
- Log phải mask token/PII.

**Lỗi cần tránh**

- Retry vô hạn.
- Refresh race.
- Redirect/UI modal nằm sâu trong HTTP layer.

---

## Topic13 — Array/Object Methods & Immutability

**Interviewer muốn nghe**

- Bạn biết method nào mutate, method nào trả array/object mới.
- Bạn hiểu immutability trong React.
- Bạn biết shallow vs deep.

**Giải thích dễ hiểu**

Array/object methods giúp xử lý data như map, filter, find, group, sort, merge. Nhưng một số method thay đổi data gốc.

**Nói mẫu**

> Em chọn array/object method theo ý định xử lý data. `map` để transform, `filter` để lọc, `find` để tìm một item, `reduce` hoặc `Map` để group. Trong React, em rất để ý method nào mutate như `sort`, `reverse`, `push`, vì mutate state có thể làm React không nhận ra thay đổi đúng cách. Em thường update immutable và giữ structural sharing để shallow compare hoạt động.

**Điểm senior**

- `sort()` mutate array gốc.
- Spread chỉ shallow copy.
- Deep compare trong render path có thể tốn CPU.
- Normalize state khi data phức tạp.

**Lỗi cần tránh**

- Sort trực tiếp props/state.
- Clone sâu mọi thứ không cần thiết.
- Dùng chain dài làm code khó đọc.

---

## Topic14 — Loop Performance & Async Loops

**Interviewer muốn nghe**

- Bạn không chỉ nói `for` nhanh hơn.
- Bạn tối ưu Big-O trước micro-optimization.
- Bạn biết async loop pitfalls.

**Giải thích dễ hiểu**

Loop là cách lặp qua data. Performance phụ thuộc cách lặp, kích thước data và thuật toán.

**Nói mẫu**

> Với loop performance, em ưu tiên Big-O trước. Nếu đang có nested loop `.find()` trong mỗi item, em sẽ đổi sang `Map` để lookup `O(1)` thay vì chỉ đổi `map` sang `for`. Với async loop, em tránh `forEach(async)` vì nó không await như nhiều người nghĩ. Em chọn sequential `for...of await`, parallel `Promise.all`, `allSettled`, hoặc concurrency limit tùy dependency, rate limit và error handling.

**Điểm senior**

- `Map/Set` thường giải quyết bottleneck lớn hơn đổi syntax loop.
- `Promise.all` không giới hạn có thể overload API.
- UI có thể block nếu xử lý CPU lớn trên main thread.

**Lỗi cần tránh**

- `forEach(async)`.
- Gửi hàng trăm request cùng lúc.
- Micro-optimize khi bottleneck là network/render/Big-O.

---

## Topic15 — Compare Data Types, Strings, Big Numbers & Decimals

**Interviewer muốn nghe**

- Bạn biết so sánh object theo reference.
- Bạn biết string locale/Unicode issue.
- Bạn biết money/decimal không nên dùng float thường.

**Giải thích dễ hiểu**

So sánh dữ liệu phải hiểu dữ liệu đó là object, string, số thường, số lớn hay tiền.

**Nói mẫu**

> Khi so sánh dữ liệu trong JavaScript, em không dùng một cách máy móc. Object/array so bằng reference, nên hai object giống nội dung vẫn có thể không bằng nhau. String nếu là id/enum thì `===` ổn, nhưng sort/search tên tiếng Việt nên dùng normalize hoặc `Intl.Collator`. Với tiền hoặc số lớn, em tránh dùng float thường vì precision issue, thường lưu smallest unit hoặc dùng decimal library.

**Điểm senior**

- React shallow compare dựa vào reference.
- `0.1 + 0.2 !== 0.3` là precision issue.
- Large number từ API nên giữ dạng string nếu vượt safe integer.

**Lỗi cần tránh**

- `JSON.stringify` compare mọi object.
- Convert large id sang number.
- Dùng `toFixed` làm business rounding cho tiền.

---

## Topic16 — Browser Rendering: Paint, Repaint, Reflow

**Interviewer muốn nghe**

- Bạn hiểu layout/reflow, paint/repaint, composite.
- Bạn biết animation property nào nhẹ.
- Bạn biết đo bằng DevTools.

**Giải thích dễ hiểu**

Browser phải tính vị trí/kích thước rồi vẽ UI. Một số thay đổi buộc browser tính lại layout, rất tốn.

**Nói mẫu**

> Em hiểu browser rendering theo 3 phần chính: layout/reflow là tính vị trí và kích thước, paint/repaint là vẽ màu/text/image, composite là ghép layer. Reflow thường đắt hơn repaint. Vì vậy khi làm animation, em ưu tiên `transform` và `opacity` thay vì animate `width`, `height`, `top`, `left`. Khi nghi ngờ performance, em dùng Chrome Performance để xác nhận layout/paint cost thay vì đoán.

**Điểm senior**

- Batch DOM read/write.
- Tránh forced synchronous layout.
- Virtualize list lớn.
- Đặt `width/height/aspect-ratio` cho media để tránh CLS.

**Lỗi cần tránh**

- Animate layout property mỗi frame.
- Đọc `offsetHeight` sau khi ghi style trong loop.
- Lạm dụng `will-change`.

---

## Topic17 — Browser Storage

**Interviewer muốn nghe**

- Bạn biết chọn storage theo data.
- Bạn hiểu cookie/localStorage/sessionStorage/IndexedDB.
- Bạn biết auth token storage tradeoff.

**Giải thích dễ hiểu**

Browser có nhiều nơi lưu data. Mỗi loại khác nhau về dung lượng, thời gian sống, server có đọc được không và JS có đọc được không.

**Nói mẫu**

> Em không chọn storage theo thói quen. Theme/language nhỏ thì `localStorage` ổn. Data tạm trong một tab thì `sessionStorage`. Data lớn/offline thì IndexedDB. Auth token nhạy cảm thì em ưu tiên cookie do server set với `HttpOnly`, `Secure`, `SameSite` để JavaScript không đọc được. Và em luôn nhớ dữ liệu ở browser không đáng tin tuyệt đối, server vẫn phải validate.

**Điểm senior**

- localStorage sync và JS đọc được.
- Cookie tự gửi theo request nên không nên chứa data lớn.
- IndexedDB hợp offline/PWA/file/blob.

**Lỗi cần tránh**

- Lưu refresh token/PII trong localStorage.
- Không handle `JSON.parse` error/quota/private mode.
- Tin dữ liệu storage là trusted.

---

## Topic18 — HTTP Caching & Browser Cache

**Interviewer muốn nghe**

- Bạn biết cache theo tài nguyên.
- Bạn phân biệt `no-cache` và `no-store`.
- Bạn biết SPA deploy cache strategy.

**Giải thích dễ hiểu**

Cache giúp browser không tải lại thứ đã có, nhưng cache sai có thể khiến user bị kẹt version cũ hoặc lộ data.

**Nói mẫu**

> Với SPA, em thường để `index.html` là `Cache-Control: no-cache` để browser phải revalidate và nhận deploy mới. JS/CSS/image/font có content hash thì cache lâu với `max-age=31536000, immutable` vì file đổi thì URL đổi. Với API, public data có thể cache ngắn với ETag, user-specific data dùng `private/no-cache`, còn token/payment/PII nên `no-store`.

**Điểm senior**

- `no-cache` không phải không lưu, mà phải hỏi lại server.
- `no-store` mới là không lưu.
- CDN cache key cực kỳ quan trọng.

**Lỗi cần tránh**

- Cache HTML quá lâu.
- Asset cache lâu nhưng không có content hash.
- CDN cache nhầm response user.

---

## Topic19 — Observer APIs

**Interviewer muốn nghe**

- Bạn biết Observer API thay polling/scroll handler thủ công.
- Bạn phân biệt Intersection/Resize/MutationObserver.
- Bạn cleanup observer.

**Giải thích dễ hiểu**

Observer API cho phép browser báo khi element vào viewport, đổi kích thước hoặc DOM thay đổi.

**Nói mẫu**

> Em dùng `IntersectionObserver` khi cần biết element vào viewport, như lazy load image, infinite scroll hoặc impression tracking. `ResizeObserver` dùng khi component cần phản ứng theo kích thước thật của chính nó, ví dụ chart/grid. `MutationObserver` chỉ dùng khi cần theo dõi DOM ngoài tầm kiểm soát của framework, như third-party widget. Trong production, em luôn `disconnect` khi không cần nữa và giữ callback nhẹ.

**Điểm senior**

- Observer callback vẫn chạy trên main thread.
- Một observer có thể observe nhiều element cùng options.
- ResizeObserver callback sửa size target có thể gây loop.

**Lỗi cần tránh**

- Quên `disconnect()`.
- Observe `document.body` quá rộng.
- Infinite scroll thiếu `isLoading/hasMore`.

---

## Topic20 — CommonJS vs ES Modules & Bundling

**Interviewer muốn nghe**

- Bạn hiểu CJS runtime-first, ESM static-first.
- Bạn biết tree-shaking/code splitting liên quan ESM.
- Bạn hiểu interop package.

**Giải thích dễ hiểu**

CommonJS dùng `require/module.exports`. ES Modules dùng `import/export`. ESM dễ được bundler phân tích trước khi chạy.

**Nói mẫu**

> CommonJS linh hoạt ở runtime nhưng khó tối ưu bundle vì `require` có thể dynamic. ES Modules static hơn, import/export rõ từ build time nên bundler dễ tree-shake và code split. Với frontend mới em ưu tiên ESM, nhưng khi làm production vẫn phải để ý interop với package CJS, các field trong `package.json` như `main`, `module`, `exports`, `type`, và `sideEffects`.

**Điểm senior**

- Dynamic import dùng cho lazy loading.
- `sideEffects: false` giúp tree-shaking nhưng khai báo sai rất nguy hiểm.
- Dual package có thể làm bundle duplicate.

**Lỗi cần tránh**

- Nghĩ CJS/ESM chỉ khác syntax.
- Named import từ CJS rồi tin luôn đúng.
- Không test production build.

---

## Topic21 — Frontend Tooling & Build Optimization

**Interviewer muốn nghe**

- Bạn hiểu build pipeline.
- Bạn phân biệt transpile, polyfill, bundling, minify, tree-shaking.
- Bạn biết tối ưu dựa trên đo đạc.

**Giải thích dễ hiểu**

Build tool biến source code thành code browser tải được, chạy được và tối ưu hơn cho production.

**Nói mẫu**

> Em hiểu build optimization là tối ưu cả pipeline: transpile syntax theo browser target, polyfill API còn thiếu, bundle module graph, tree-shake dead code, minify và split chunk. Khi bundle nặng, em không đoán mà dùng bundle analyzer để xem dependency nào lớn, có duplicate không, import sai entry không. Sau đó mới quyết định lazy load, thay library, chỉnh browser target hoặc tách chunk.

**Điểm senior**

- Code splitting giảm initial load nhưng quá nhiều chunk gây waterfall.
- Polyfill tăng compatibility nhưng làm bundle nặng.
- Source map production cần cân nhắc security.

**Lỗi cần tránh**

- Chỉ test dev build.
- Polyfill thừa cho browser không cần.
- Split chunk quá nhỏ.

---

## Topic22 — Cancellation, Concurrency, Retry, Race Condition

**Interviewer muốn nghe**

- Bạn biết kiểm soát async flow trong UI.
- Bạn hiểu last-request-wins.
- Bạn retry có điều kiện.

**Giải thích dễ hiểu**

Khi user đổi filter/search/navigate, request cũ có thể không còn cần nữa. Nếu response cũ về sau và update UI, đó là race condition.

**Nói mẫu**

> Em xử lý async request theo 4 lớp: hủy request không còn cần bằng `AbortController`, giới hạn concurrency để không bắn quá nhiều request, retry lỗi tạm thời bằng backoff+jitter, và chống race bằng request id hoặc last-request-wins guard. Debounce chỉ giảm số request, không tự đảm bảo response cũ không ghi đè UI mới.

**Điểm senior**

- Retry `GET` an toàn hơn `POST`.
- `POST /orders` cần idempotency key nếu retry.
- Concurrency limit bảo vệ cả client và server.

**Lỗi cần tránh**

- Không cleanup khi unmount.
- Retry mọi lỗi kể cả `400/401/403/404`.
- Chỉ debounce mà không cancel/guard.

---

## Topic23 — Big-O với Map, Set, Array, Object

**Interviewer muốn nghe**

- Bạn biết chọn data structure theo lookup/insert/delete.
- Bạn tối ưu thuật toán trước syntax.
- Bạn liên hệ list/table lớn.

**Giải thích dễ hiểu**

Big-O giúp ước lượng code chậm nhanh thế nào khi data lớn lên.

**Nói mẫu**

> Em dùng Big-O để tránh bottleneck lớn. Ví dụ nếu có list users và orders, mà với mỗi order lại `.find()` user trong array thì dễ thành `O(n*m)`. Em sẽ build `Map<userId, user>` trước để lookup gần `O(1)`. Trong frontend, điều này rất thực tế với table, selected ids, dedupe, join data từ nhiều API.

**Điểm senior**

- `Set` tốt cho dedupe/membership check.
- `Map` tốt khi key không chỉ là string hoặc cần preserve insertion order.
- Object vẫn ổn cho simple dictionary string key.

**Lỗi cần tránh**

- `.find()` trong loop lớn.
- Dùng array cho membership check lớn.
- Tối ưu micro khi thuật toán đang `O(n²)`.

---

## Topic24 — URL đến UI / Critical Rendering Path

**Interviewer muốn nghe**

- Bạn hiểu từ network đến render.
- Bạn biết DNS/TCP/TLS/request/parse/render.
- Bạn liên hệ Core Web Vitals.

**Giải thích dễ hiểu**

Khi user nhập URL, browser phải tìm server, tải HTML/CSS/JS, parse và render UI.

**Nói mẫu**

> Khi user nhập URL, browser đi qua DNS lookup, TCP/TLS connection, request HTML, parse HTML tạo DOM, parse CSS tạo CSSOM, kết hợp thành render tree, layout, paint và composite. JS/CSS có thể block render nếu cấu hình sai. Vì vậy tối ưu page load không chỉ là tối ưu React, mà còn TTFB, cache, critical CSS, preload, image size, script defer/async và hydration cost.

**Điểm senior**

- CSS thường render-blocking.
- JS có thể parser-blocking.
- SSR cải thiện first HTML nhưng có hydration cost.

**Lỗi cần tránh**

- Chỉ nhìn bundle mà bỏ qua server/network/cache.
- Không đặt size ảnh gây CLS.
- Fetch waterfall trong render path.

---

## Topic25 — TypeScript Advanced Patterns

**Interviewer muốn nghe**

- Bạn dùng TS để encode domain rule.
- Bạn biết type không thay runtime validation.
- Bạn cân bằng type safety và readability.

**Giải thích dễ hiểu**

TypeScript giúp mô tả shape và rule của data để bắt lỗi trước khi chạy.

**Nói mẫu**

> Em dùng TypeScript để encode domain rule quan trọng. Discriminated union rất hợp cho UI state như `loading/success/error`. Branded type giúp tránh nhầm `UserId` với string thường. Type guard giúp xử lý data từ API an toàn hơn. Nhưng em không cố viết type quá phức tạp nếu team khó maintain, và data từ API vẫn cần runtime validation ở boundary.

**Điểm senior**

- `unknown` tốt hơn `any` ở boundary.
- Generic phải phục vụ reuse thật.
- Utility/mapped/conditional types giúp giảm duplication.

**Lỗi cần tránh**

- Dùng `any` cho nhanh.
- Tin TypeScript validate runtime data.
- Type quá “ảo” làm code khó đọc.

---

## Topic26 — React Lifecycle

**Interviewer muốn nghe**

- Bạn hiểu render → commit → effects.
- Bạn biết render phải pure.
- Bạn hiểu cleanup/dependency.

**Giải thích dễ hiểu**

React render để tính UI mới, commit vào DOM, rồi chạy effect sau đó.

**Nói mẫu**

> Em nhìn React lifecycle hiện đại theo flow render → commit → effects. Render phải pure, không fetch, không subscribe, không mutate DOM. Sau commit, `useEffect` chạy sau paint; `useLayoutEffect` chạy trước paint nên chỉ dùng khi cần đo layout hoặc sync DOM trước khi user thấy. Với effect có listener, timer, request hoặc subscription, em luôn cleanup để tránh leak và stale update.

**Điểm senior**

- StrictMode double invoke giúp lộ side effect sai.
- Dependency array là contract với closure.
- `useRef` giữ value mới nhất nhưng không trigger render.

**Lỗi cần tránh**

- Side effect trong render.
- Thiếu cleanup.
- Tắt eslint deps để hết warning.

---

## Topic27 — React Performance

**Interviewer muốn nghe**

- Bạn đo trước khi tối ưu.
- Bạn biết memo không phải thuốc chữa mọi thứ.
- Bạn hiểu source của re-render.

**Giải thích dễ hiểu**

React chậm khi render quá nhiều, calculation nặng, list quá lớn hoặc context/props thay đổi rộng.

**Nói mẫu**

> Khi optimize React, em dùng React Profiler trước để biết chậm ở đâu. Em xem component render nhiều vì props reference đổi, context update rộng, list quá lớn hay calculation nặng. Sau đó mới chọn stable reference, `React.memo`, `useMemo/useCallback`, split context, virtualization hoặc code splitting. Em không rải memoization khắp nơi vì nó cũng có cost và làm code khó đọc hơn.

**Điểm senior**

- Virtualization hiệu quả với list lớn.
- Context split giảm re-render rộng.
- Stable key quan trọng.

**Lỗi cần tránh**

- Dùng index key với list reorder.
- Memo mọi thứ không đo.
- Không test với production-like data.

---

## Topic28 — Web Security

**Interviewer muốn nghe**

- Bạn biết frontend không phải security boundary cuối.
- Bạn hiểu XSS, CSRF, CSP, CORS, token storage.
- Bạn biết server vẫn phải validate.

**Giải thích dễ hiểu**

Frontend security là giảm khả năng user bị chạy script độc hại, lộ token hoặc gọi API sai quyền.

**Nói mẫu**

> Em không xem frontend là nơi validate bảo mật cuối cùng; server vẫn phải validate permission và input. Ở frontend, em giảm XSS bằng output encoding, sanitize và CSP; giảm CSRF bằng SameSite cookie hoặc CSRF token; và lưu token nhạy cảm bằng HttpOnly Secure cookie nếu kiến trúc cho phép. CORS chỉ kiểm soát browser cho phép gọi cross-origin, nó không phải authentication.

**Điểm senior**

- HttpOnly chống JS đọc token nhưng cần xử lý CSRF.
- localStorage dễ dùng nhưng rủi ro nếu XSS.
- CSP giảm blast radius của XSS.

**Lỗi cần tránh**

- Nghĩ CORS là auth.
- Lưu refresh token ở localStorage.
- Render raw HTML không sanitize.

---

## Topic29 — Next.js Workflow

**Interviewer muốn nghe**

- Bạn hiểu App Router, Server/Client Component, data fetching, caching.
- Bạn biết build/deploy/debug workflow.
- Bạn không thêm `'use client'` bừa.

**Giải thích dễ hiểu**

Next.js giúp làm routing, rendering, data fetching, caching và deploy React app theo cách fullstack hơn.

**Nói mẫu**

> Với Next.js, em bắt đầu từ route và rendering strategy. Phần không cần interactivity em giữ ở Server Component để giảm JS gửi xuống client. Phần cần `useState`, event handler hoặc browser API thì mới là Client Component. Em cũng để ý `fetch` caching, parallel data fetching, streaming/loading UI, error boundary và server actions. Điểm quan trọng là không thêm `'use client'` quá rộng vì sẽ làm mất lợi ích Server Component.

**Điểm senior**

- Fetch waterfall làm trang chậm.
- Cache user-specific data sai là lỗi bảo mật.
- Streaming giúp cải thiện perceived performance.

**Lỗi cần tránh**

- `'use client'` ở layout/root quá rộng.
- SSR rồi client fetch lại toàn bộ.
- Không hiểu cache mặc định của `fetch`.

---

## Topic30 — CSR vs SSR

**Interviewer muốn nghe**

- Bạn chọn rendering strategy theo use case.
- Bạn hiểu SEO, TTFB, hydration, infra cost.
- Bạn biết hybrid strategy.

**Giải thích dễ hiểu**

CSR render ở browser. SSR render HTML ở server. SSG render sẵn lúc build. ISR render tĩnh nhưng có thể refresh theo thời gian.

**Nói mẫu**

> Em không chọn SSR cho mọi trang. Nếu cần SEO và data theo request, SSR hợp lý nhưng có TTFB, hydration và infra cost. Nếu content ít đổi, SSG hoặc ISR thường tốt hơn vì cache tốt và nhanh. Với dashboard nội bộ nhiều tương tác, CSR hoặc hybrid có thể đủ. Em chọn theo SEO, data freshness, user personalization, performance và độ phức tạp vận hành.

**Điểm senior**

- SSR không tự làm app nhanh hơn nếu hydration nặng.
- SSG/ISR hợp content cacheable.
- CSR hợp app nội bộ/tương tác cao không cần SEO.

**Lỗi cần tránh**

- SSR mọi thứ.
- Hydration mismatch.
- Leak secret/server data sang client.

---

## Topic31 — React Query

**Interviewer muốn nghe**

- Bạn phân biệt server state và client state.
- Bạn hiểu query key, staleTime, gc/cacheTime, invalidation.
- Bạn biết optimistic update và cancellation.

**Giải thích dễ hiểu**

React Query quản lý data từ server: fetch, cache, loading, error, retry, refetch.

**Nói mẫu**

> React Query không thay thế Redux/Zustand cho mọi state; nó chuyên cho server state. Em dùng nó cho API data vì nó xử lý cache, dedupe, stale data, retry, refetch và invalidation tốt hơn tự viết. Điểm quan trọng là query key phải stable và đủ thông tin. Sau mutation, em invalidate hoặc update cache để UI đồng bộ. Với optimistic update, em rollback nếu mutation fail.

**Điểm senior**

- `staleTime` quyết định khi nào data được coi là cũ.
- Query key là contract cache.
- Server state có lifecycle khác UI state.

**Lỗi cần tránh**

- Query key thiếu filter/page/user id.
- Refetch quá nhiều vì staleTime không phù hợp.
- Mutation xong quên invalidate.

---

## Topic32 — AG Grid Enterprise

**Interviewer muốn nghe**

- Bạn hiểu data grid là bài toán performance + UX + server data.
- Bạn biết virtualization và server-side row model.
- Bạn xử lý real-time/update/filter/sort đúng.

**Giải thích dễ hiểu**

AG Grid là grid mạnh cho bảng dữ liệu lớn, có sort/filter/group/edit/export/virtualization.

**Nói mẫu**

> Với AG Grid, em không xem nó chỉ là table UI. Với data lớn, em dùng server-side row model hoặc pagination, bật row/column virtualization, debounce filter, dùng `getRowId` ổn định và update delta để tránh re-render toàn bảng. Với custom cell renderer, em giữ component nhẹ và memo column definitions. Nếu có realtime updates, em quan tâm batching, row identity và không làm grid refresh quá rộng.

**Điểm senior**

- Client-side model chỉ hợp data nhỏ/vừa.
- Server-side sort/filter/pagination cần contract API rõ.
- Stable row id rất quan trọng cho update.

**Lỗi cần tránh**

- Client filter hàng trăm nghìn rows.
- Custom cell renderer quá nặng.
- Recreate columnDefs mỗi render.

---

## Topic33 — State Management: Redux vs Zustand vs Context

**Interviewer muốn nghe**

- Bạn phân loại state trước khi chọn tool.
- Bạn không dùng Redux/Zustand/Context theo trend.
- Bạn hiểu Context re-render issue.

**Giải thích dễ hiểu**

State có nhiều loại: local component state, global UI state, server state, form state. Mỗi loại hợp tool khác nhau.

**Nói mẫu**

> Em thường phân loại state trước. State chỉ dùng trong một component thì để local. UI state dùng nhiều nơi như sidebar/modal/theme có thể dùng Context hoặc Zustand tùy tần suất update. Server state như API list/detail/cache/refetch em ưu tiên React Query. Redux hợp app enterprise cần convention chặt, middleware, DevTools, audit trail. Context đơn giản nhưng không nên dùng cho state thay đổi liên tục vì dễ re-render rộng.

**Điểm senior**

- Server state không nên đưa hết vào client global store.
- Zustand nhẹ và ít boilerplate.
- Redux mạnh khi team lớn cần convention.

**Lỗi cần tránh**

- Context chứa state high-frequency.
- Dùng global store cho mọi thứ.
- Tự viết cache server state phức tạp.

---

## Topic34 — React 19 Migration

**Interviewer muốn nghe**

- Bạn biết migration cần plan, test và ecosystem check.
- Bạn hiểu API/behavior mới.
- Bạn không chỉ bump version.

**Giải thích dễ hiểu**

Migration là nâng React version mà vẫn giữ app chạy đúng, test đúng và thư viện tương thích.

**Nói mẫu**

> Với React 19 migration, em không chỉ bump version. Em kiểm tra compatibility của framework, router, testing library, UI library, form library trước. Sau đó em chạy test, kiểm SSR/hydration, effects, forms và third-party packages. Với API mới như actions, form hooks, `use`, ref changes, em migrate từng phần có kiểm soát thay vì rewrite rộng.

**Điểm senior**

- Test behavior quan trọng hơn chỉ fix compile.
- StrictMode/effects có thể lộ bug cũ.
- Rollout từng bước giảm risk.

**Lỗi cần tránh**

- Upgrade đồng loạt không plan.
- Không test SSR/hydration.
- Dependency chưa support React 19.

---

## Topic35 — WebSocket & Real-Time Streaming

**Interviewer muốn nghe**

- Bạn biết realtime không chỉ mở socket.
- Bạn xử lý reconnect, heartbeat, ordering, dedupe, backpressure.
- Bạn chọn WebSocket/SSE/polling theo use case.

**Giải thích dễ hiểu**

WebSocket giữ kết nối 2 chiều liên tục. SSE là server gửi một chiều. Polling là client hỏi server định kỳ.

**Nói mẫu**

> Với realtime, em không chỉ mở socket rồi listen message. Em cần heartbeat để phát hiện dead connection, reconnect bằng exponential backoff, auth refresh, dedupe message, xử lý out-of-order và backpressure nếu data quá nhanh. WebSocket hợp bidirectional như chat/trading, SSE hợp notification server-to-client đơn giản, polling hợp case đơn giản hoặc fallback.

**Điểm senior**

- Reconnect cần jitter/backoff.
- Message cần id/sequence để dedupe/order.
- Cleanup socket khi unmount/logout.

**Lỗi cần tránh**

- Reconnect storm.
- Tin message luôn đúng thứ tự.
- Không handle token refresh khi socket sống lâu.

---

## Topic36 — Hashing, Encryption & Digital Signatures

**Interviewer muốn nghe**

- Bạn phân biệt hash, encryption, signature.
- Bạn biết frontend không giữ secret an toàn.
- Bạn không tự thiết kế crypto.

**Giải thích dễ hiểu**

Hash tạo dấu vân tay dữ liệu. Encryption giấu nội dung và có thể giải mã. Digital signature xác minh dữ liệu do đúng người/key ký.

**Nói mẫu**

> Em phân biệt rõ hashing, encryption và signature. Hash là one-way, dùng để kiểm tra toàn vẹn như checksum hoặc password hash ở backend. Encryption dùng để mã hóa/giải mã nội dung. Digital signature dùng private key để ký và public key để verify, ví dụ JWT signature. Trên frontend, em không đặt secret key vì user có thể inspect bundle, nên crypto nhạy cảm phải nằm ở backend hoặc secure environment.

**Điểm senior**

- Password nên hash với salt và slow algorithm ở backend.
- JWT thường là signed, không nhất thiết encrypted.
- HTTPS bảo vệ data in transit.

**Lỗi cần tránh**

- Gọi hash là encryption.
- Tự viết thuật toán crypto.
- Đặt secret trong frontend env public.

---

## Topic37 — Date & Time Handling

**Interviewer muốn nghe**

- Bạn biết date/time khó vì timezone, DST, locale.
- Bạn lưu/trao đổi data theo chuẩn rõ ràng.
- Bạn format ở UI theo locale.

**Giải thích dễ hiểu**

Cùng một thời điểm có thể hiển thị khác nhau theo timezone. Ngày tháng còn bị ảnh hưởng bởi DST và format địa phương.

**Nói mẫu**

> Với date/time, em cố tách storage và display. Khi trao đổi với API, em ưu tiên ISO UTC hoặc timestamp rõ timezone. Khi hiển thị, em format theo locale/timezone của user hoặc business rule. Em tránh parse date string mơ hồ như `01/02/2024` vì mỗi locale hiểu khác nhau. Với date range, booking, report, em đặc biệt cẩn thận DST và inclusive/exclusive boundary.

**Điểm senior**

- UTC cho instant, local date cho ngày lịch business.
- DST làm cộng ngày bằng milliseconds dễ sai.
- Timezone phải là requirement rõ.

**Lỗi cần tránh**

- Parse date string không timezone.
- Lưu local time mơ hồ.
- Cộng ngày bằng `24*60*60*1000` qua DST.

---

## Topic38 — Build Tools: Vite, Webpack, Rollup, SWC, Babel, Turbopack, esbuild

**Interviewer muốn nghe**

- Bạn biết mỗi tool phục vụ vai trò khác nhau.
- Bạn chọn tool theo project constraint.
- Bạn không đổi tool chỉ vì trend.

**Giải thích dễ hiểu**

Build tools giúp dev server, transform, bundle, minify và optimize code.

**Nói mẫu**

> Em chọn build tool theo use case. Vite rất tốt cho modern app và dev server nhanh nhờ native ESM. Webpack mạnh với legacy/complex plugin ecosystem. Rollup hợp build library vì output sạch và tree-shaking tốt. esbuild/SWC rất nhanh cho transform/minify. Turbopack gắn nhiều với Next ecosystem. Nhưng em không đổi tool chỉ vì “nhanh”; em kiểm plugin, production build, CI, source map, compatibility và migration cost.

**Điểm senior**

- Dev speed khác production build quality.
- Plugin ecosystem là constraint lớn.
- Library build khác app build.

**Lỗi cần tránh**

- Chỉ benchmark dev server.
- Không test production build.
- Bỏ qua plugin/loader edge cases.

---

## Topic39 — JavaScript Design Patterns for Frontend

**Interviewer muốn nghe**

- Bạn hiểu pattern là giải pháp cho vấn đề lặp lại.
- Bạn dùng pattern để giảm complexity, không khoe kiến thức.
- Bạn liên hệ được UI/API/state.

**Giải thích dễ hiểu**

Design pattern là cách đặt tên cho những cách tổ chức code hay dùng khi gặp vấn đề tương tự.

**Nói mẫu**

> Em dùng design pattern khi nó giải quyết complexity thật. Factory hợp khi cần tạo object/service với setup ẩn. Observer/PubSub hợp event system hoặc subscription. Strategy hợp khi có nhiều thuật toán cùng interface, ví dụ payment/export/sort. Adapter hợp khi API response khác shape UI cần. Em tránh áp dụng pattern chỉ để code trông advanced vì over-engineering làm team maintain khó hơn.

**Điểm senior**

- Pattern phải đi kèm problem.
- React patterns cũng có tradeoff: compound, render props, HOC, custom hooks.
- Simplicity vẫn là ưu tiên.

**Lỗi cần tránh**

- Over-engineering.
- Dùng singleton/global state gây test khó.
- Pattern làm code khó đọc hơn vấn đề.

---

## Topic40 — Microfrontend & Monorepo

**Interviewer muốn nghe**

- Bạn hiểu microfrontend giải quyết org scale.
- Bạn biết tradeoff runtime integration.
- Bạn phân biệt monorepo và microfrontend.

**Giải thích dễ hiểu**

Microfrontend chia app thành nhiều frontend độc lập. Monorepo là cách quản lý nhiều app/package trong một repo.

**Nói mẫu**

> Em chỉ chọn microfrontend khi bài toán chính là team ownership và independent deployment. Nó không tự làm app nhanh hơn. Tradeoff là shared dependency, duplicate React, version drift, routing/auth/shared state phức tạp và debug runtime khó hơn. Nếu chỉ một team hoặc app chưa quá lớn, monolith modular hoặc monorepo với package boundary rõ có thể đơn giản hơn.

**Điểm senior**

- Module Federation cần quản lý shared deps chặt.
- Contract shell/remote phải rõ.
- Observability cần trace qua remote.

**Lỗi cần tránh**

- Chia microfrontend theo page tùy tiện.
- Share global state lung tung.
- Không có rollback/versioning strategy.

---

## Topic41 — Git Workflow & Team Collaboration

**Interviewer muốn nghe**

- Bạn biết Git workflow phục vụ collaboration.
- Bạn hiểu merge/rebase/squash tradeoff.
- Bạn biết làm PR dễ review.

**Giải thích dễ hiểu**

Git giúp nhiều người cùng làm code mà vẫn kiểm soát lịch sử, review và release.

**Nói mẫu**

> Em xem Git workflow là cách giảm conflict và làm review dễ hơn. Với feature work, em giữ PR nhỏ, commit message rõ, rebase hoặc merge theo convention team. Rebase giúp history sạch nhưng không nên rebase shared branch bừa. Squash giúp main gọn hơn nhưng mất granular commits. Khi conflict, em không chọn bừa theo file mới/cũ mà hiểu logic hai phía rồi mới resolve.

**Điểm senior**

- PR nhỏ tăng chất lượng review.
- Branch strategy phải fit release model.
- CODEOWNERS/checks giúp scale team.

**Lỗi cần tránh**

- PR quá lớn.
- Rebase shared branch.
- Resolve conflict không hiểu business logic.

---

## Topic42 — Frontend System Design

**Interviewer muốn nghe**

- Bạn thiết kế frontend như một hệ thống.
- Bạn không chỉ vẽ component tree.
- Bạn nghĩ tới data flow, cache, auth, error, monitoring.

**Giải thích dễ hiểu**

Frontend system design là thiết kế cách UI, API, state, cache, auth, rendering và monitoring phối hợp.

**Nói mẫu**

> Khi design frontend system, em bắt đầu từ user flow và data flow: màn hình cần data gì, data fresh tới mức nào, loading/error/empty state ra sao, permission/auth thế nào, cache ở client/CDN/server layer nào. Sau đó em chọn rendering strategy, state ownership, API layer, retry/cancel, error boundary, monitoring và rollout. Em không chỉ vẽ component tree vì production thường hỏng ở stale data, network failure, permission hoặc thiếu observability.

**Điểm senior**

- Nêu tradeoff UX, correctness, performance, security, maintainability.
- Có fallback và failure mode.
- Có logging/RUM/error tracking.

**Lỗi cần tránh**

- Bỏ qua auth/permission.
- Không nói cache invalidation.
- Không có plan khi API fail/chậm.

---

## Topic43 — Component Libraries Comparison

**Interviewer muốn nghe**

- Bạn chọn library theo constraint, không theo demo đẹp.
- Bạn biết headless vs styled.
- Bạn quan tâm a11y, customization, bundle, design system.

**Giải thích dễ hiểu**

Component library cung cấp UI component có sẵn như button, modal, table, form control.

**Nói mẫu**

> Em chọn component library theo product và team. Nếu cần ship nhanh với UI đầy đủ, MUI/AntD có lợi. Nếu team có design system riêng và cần control markup/style, headless như Radix hoặc React Aria hợp hơn. Em đánh giá accessibility, theme/token support, customization, bundle size, docs, ecosystem và khả năng maintain lâu dài, không chỉ nhìn demo đẹp.

**Điểm senior**

- Headless cho control cao nhưng cần tự style nhiều.
- Styled library nhanh nhưng dễ lock-in visual system.
- Data grid/form component cần kiểm performance/a11y kỹ.

**Lỗi cần tránh**

- Chọn theo trend.
- Override CSS quá nhiều làm maintain khó.
- Không kiểm keyboard/screen reader behavior.

---

## Topic44 — Code Quality & Standards

**Interviewer muốn nghe**

- Bạn hiểu lint/format/review là guardrail.
- Bạn tránh style war.
- Bạn biết CI enforce quality.

**Giải thích dễ hiểu**

Code quality là bộ rule và quy trình giúp code nhất quán, ít bug và dễ review hơn.

**Nói mẫu**

> Em xem ESLint, Prettier và code review là guardrail cho team. Prettier xử lý format để tránh tranh luận style. ESLint nên tập trung vào bug/risk/maintainability, không bật quá nhiều rule gây noise. Code review nên ưu tiên correctness, edge cases, tests, performance/security risk thay vì sở thích cá nhân. Trong CI, em muốn có lint, typecheck, test và build để tránh regression.

**Điểm senior**

- Rule tốt là rule team tin và tuân thủ.
- Auto-fix càng nhiều càng tốt.
- Review checklist nên theo risk.

**Lỗi cần tránh**

- Rule quá nhiều làm team ignore.
- Review nitpick style đã có Prettier.
- Không chạy check trong CI.

---

## Topic45 — CSS Architecture & Modern Styling

**Interviewer muốn nghe**

- Bạn biết CSS scale khó vì cascade/specificity/global leak.
- Bạn chọn approach theo team/design system.
- Bạn hiểu design tokens/responsive strategy.

**Giải thích dễ hiểu**

CSS architecture giúp style không rối khi app lớn lên.

**Nói mẫu**

> CSS architecture quan trọng vì app lớn dễ gặp global leak, specificity war và design drift. Em chọn approach theo context: CSS Modules cho scoped styles đơn giản, utility CSS cho tốc độ và consistency, CSS-in-JS khi cần theme dynamic hoặc colocated styles, headless + tokens khi có design system nghiêm túc. Dù dùng gì, em muốn có design tokens cho color/spacing/typography và responsive rules rõ.

**Điểm senior**

- Cascade layers giúp quản lý priority.
- Tokens giúp consistency cross-platform.
- A11y/responsive là một phần của styling.

**Lỗi cần tránh**

- Hardcode màu/spacing khắp nơi.
- Specificity war.
- Global CSS leak giữa component.

---

## Topic46 — Keycloak

**Interviewer muốn nghe**

- Bạn hiểu Keycloak là IdP/auth server.
- Bạn biết realm/client/role/token flow.
- Bạn hiểu frontend không tự quyết định quyền cuối cùng.

**Giải thích dễ hiểu**

Keycloak quản lý login, SSO, token, role và permission cho ứng dụng.

**Nói mẫu**

> Em hiểu Keycloak là identity provider. Với SPA hiện đại, em ưu tiên Authorization Code Flow với PKCE thay vì implicit flow. Frontend dùng access token để gọi API, refresh token để lấy token mới nếu kiến trúc cho phép. UI có thể ẩn/hiện theo role, nhưng backend vẫn phải validate permission. Em cũng quan tâm token storage, silent renew, logout nhiều tab và token expiry handling.

**Điểm senior**

- PKCE bảo vệ SPA tốt hơn implicit.
- Role trong token phục vụ UX, không thay backend authz.
- Refresh/session strategy phải rõ.

**Lỗi cần tránh**

- Dùng implicit flow cũ.
- Lưu token sai chỗ.
- Frontend tin role mà backend không check.

---

## Topic47 — Form Handling & Validation

**Interviewer muốn nghe**

- Bạn biết form production phức tạp hơn input/submit.
- Bạn hiểu validation client và server.
- Bạn quan tâm UX/a11y/error mapping.

**Giải thích dễ hiểu**

Form cần quản lý value, touched/dirty, validation, error, loading, submit và server response.

**Nói mẫu**

> Với form production, em quan tâm cả client validation, server validation, error display, focus management, loading state và submit idempotency. React Hook Form tốt vì giảm re-render với uncontrolled input. Zod/Yup giúp schema validation rõ. Nhưng client validation chỉ để UX tốt hơn; server vẫn phải validate. Khi server trả field error, em map về đúng field và focus error đầu tiên để accessible.

**Điểm senior**

- Controlled input dễ hiểu nhưng có thể re-render nhiều.
- Async validation cần debounce/cancel.
- Form error phải accessible.

**Lỗi cần tránh**

- Chỉ validate client.
- Mất data khi submit fail.
- Error không gắn với field/screen reader.

---

## Topic48 — Internationalization & Localization

**Interviewer muốn nghe**

- Bạn biết i18n không chỉ dịch text.
- Bạn xử lý date/number/currency/plural/RTL/fallback.
- Bạn tránh hardcode string.

**Giải thích dễ hiểu**

i18n là chuẩn bị app để hỗ trợ nhiều ngôn ngữ/thị trường. Localization là bản cụ thể cho từng locale.

**Nói mẫu**

> i18n không chỉ là thay text tiếng Anh sang tiếng Việt. Em còn phải xử lý format ngày, số, tiền tệ, plural rules, fallback language, lazy load namespace và đôi khi RTL layout. Trong code, em tránh nối string thủ công vì thứ tự từ khác nhau theo ngôn ngữ. Với sort/search tên người hoặc nội dung theo locale, em dùng API như `Intl.Collator` thay vì so sánh string đơn giản.

**Điểm senior**

- ICU message giúp plural/gender/context.
- Translation namespace giúp lazy load.
- Locale ảnh hưởng date/currency/sort.

**Lỗi cần tránh**

- Hardcode text.
- Concatenate translated string.
- Quên timezone/currency.

---

## Topic49 — Mobile-First Development

**Interviewer muốn nghe**

- Bạn hiểu mobile-first là constraint thật, không chỉ media query.
- Bạn quan tâm touch, viewport, safe area, input quirks.
- Bạn test trên viewport/device thật.

**Giải thích dễ hiểu**

Mobile-first là thiết kế từ màn hình nhỏ, touch interaction và network/device constraint trước rồi mở rộng lên desktop.

**Nói mẫu**

> Mobile-first với em không chỉ là viết `@media`. Em thiết kế từ constraint thật: width nhỏ, touch target tối thiểu khoảng 44px, safe area, keyboard iOS, viewport unit quirks, scroll performance và network chậm hơn. Layout nên stack tự nhiên trên mobile, text không sát mép, form input đủ lớn để tránh zoom iOS. Sau đó mới scale lên tablet/desktop.

**Điểm senior**

- `100vh` có issue với mobile browser chrome, cân nhắc `svh/dvh`.
- Touch event và hover behavior khác desktop.
- Responsive image ảnh hưởng performance.

**Lỗi cần tránh**

- Desktop layout ép xuống mobile.
- Button quá nhỏ.
- Fixed bottom bar bị keyboard/safe area che.

---

## Câu Chốt Tổng Quan Cho Senior/Staff FE

> Em nhìn frontend như một hệ thống chạy trên browser, không chỉ là React component. Một câu trả lời tốt phải nối được từ JavaScript runtime, API flow, rendering, cache, state, security, build cho tới monitoring. Khi chọn giải pháp, em luôn hỏi: data có đúng không, request có race không, UI có render quá nhiều không, token có an toàn không, cache có stale không, bundle có nặng không, và team có maintain/debug được không.

---

## Checklist Tự Đánh Giá Trước Interview

- [ ] Tôi giải thích được topic bằng câu đơn giản trước khi nói thuật ngữ.
- [ ] Tôi luôn có ví dụ production thật.
- [ ] Tôi nói được tradeoff, không nói kiểu “luôn luôn dùng X”.
- [ ] Tôi biết pitfall phổ biến của topic.
- [ ] Tôi biết debug/đo/test bằng công cụ nào.
- [ ] Tôi nối được topic với React/browser/API/security/performance.
- [ ] Tôi có câu trả lời ngắn 30 giây và bản sâu 2 phút.
