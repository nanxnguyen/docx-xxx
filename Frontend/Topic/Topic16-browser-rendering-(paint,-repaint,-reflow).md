# 🎨 Topic 16: Browser Rendering - Paint, Repaint, Reflow

## 1. ⭐ Senior/Staff Summary

Browser rendering là quá trình biến HTML/CSS/JS thành pixels trên màn hình. Với frontend performance, điểm quan trọng nhất là hiểu **đổi gì sẽ làm browser phải tính layout lại**, **đổi gì chỉ cần vẽ lại**, và **đổi gì có thể chỉ composite trên GPU**.

Tóm tắt senior:

- 🧱 **Layout/Reflow**: browser tính lại kích thước/vị trí element. Đây thường là bước đắt nhất.
- 🖌️ **Paint/Repaint**: browser vẽ pixels như text, color, background, border, shadow. Rẻ hơn layout nhưng vẫn có thể tốn nếu vùng vẽ lớn.
- 🧩 **Composite**: browser ghép các layers. `transform` và `opacity` thường chỉ cần composite, nên phù hợp animation.
- ⚠️ **Layout thrashing**: xen kẽ đọc layout (`offsetWidth`) và ghi style (`style.width`) làm browser bị ép reflow đồng bộ nhiều lần.
- 🚀 **Optimization**: batch DOM changes, đọc trước ghi sau, dùng `transform/opacity`, `requestAnimationFrame`, virtualization, CSS containment và profiling bằng DevTools.

| Thay đổi | Thường kích hoạt | Ví dụ | Chi phí |
|---|---|---|---|
| Kích thước/vị trí | Layout + Paint + Composite | `width`, `height`, `margin`, `display`, text thay đổi | Cao |
| Hình ảnh không đổi layout | Paint + Composite | `color`, `background`, `box-shadow`, `visibility` | Trung bình |
| Layer transform/opacity | Composite | `transform`, `opacity` | Thấp nhất nếu đã ở layer phù hợp |

> 🔥 Điểm phỏng vấn: “Reflow đắt hơn repaint” là đúng nhưng chưa đủ. Câu senior cần nói thêm: **đọc layout sau khi ghi DOM có thể force synchronous reflow**, và animation nên ưu tiên **compositor-friendly properties** như `transform`/`opacity`.

## 2. 🧠 Key Mental Model

- Browser render theo pipeline: **HTML/CSS → DOM/CSSOM → Render Tree → Layout → Paint → Composite**.
- JavaScript, CSS và DOM đều có thể làm pipeline chạy lại một phần.
- Không phải mọi CSS property đều có chi phí giống nhau.
- Layout change có thể lan rộng lên/xuống cây DOM nếu element ảnh hưởng flow.
- Paint có thể rẻ hoặc đắt tùy diện tích repaint, shadow/filter phức tạp, ảnh lớn, text nhiều.
- Composite nhanh vì thường chạy trên compositor/GPU thread, nhưng tạo quá nhiều layers cũng tốn memory.
- Trong React, render component nhiều chưa chắc DOM đổi nhiều, nhưng commit DOM/style sai cách vẫn có thể gây reflow/repaint.

## 3. 📚 Main Concepts

### 3.1. 🧭 Rendering Pipeline

Pipeline cơ bản:

```txt
HTML -> DOM
CSS -> CSSOM
DOM + CSSOM -> Render Tree
Render Tree -> Layout/Reflow
Layout -> Paint
Painted layers -> Composite -> Screen
```

**DOM**

- Browser parse HTML thành tree node.
- JavaScript có thể thay đổi DOM qua insert/remove/update.

**CSSOM**

- Browser parse CSS thành style rules.
- CSSOM kết hợp với DOM để tính computed styles.

**Render Tree**

- Chỉ gồm node cần render.
- `display: none` không có trong render tree.
- `visibility: hidden` vẫn chiếm layout, thường vẫn có box nhưng không visible.

**Layout / Reflow**

- Browser tính kích thước và vị trí box.
- Phụ thuộc viewport, font, content, CSS layout mode, parent/child relationship.

**Paint**

- Browser vẽ pixels: text, color, background, border, image, shadow.

**Composite**

- Browser ghép các layers thành frame cuối.
- Transform/opacity animation thường tối ưu vì có thể tránh layout/paint mỗi frame.

### 3.2. 🧱 Reflow là gì?

`Reflow` hay `layout` là quá trình browser tính lại geometry của element: width, height, x/y position, line breaks, scroll size.

Các thay đổi thường gây reflow:

- Thêm/xóa DOM node.
- Đổi text làm element đổi kích thước.
- Đổi `width`, `height`, `margin`, `padding`, `border`.
- Đổi `display`, `position`, `top`, `left`, `font-size`.
- Resize viewport.
- Font load làm text metrics thay đổi.
- Đọc layout property sau khi DOM/style vừa bị thay đổi.

Ví dụ property đọc layout có thể force reflow:

```ts
element.offsetWidth;
element.offsetHeight;
element.clientWidth;
element.scrollHeight;
element.getBoundingClientRect();
window.getComputedStyle(element);
```

> ⚠️ Highlight: Browser thường batch style/layout work. Nhưng khi code hỏi “element rộng bao nhiêu ngay bây giờ?”, browser phải flush pending changes để trả lời chính xác.

### 3.3. 🖌️ Paint và Repaint là gì?

`Paint` là lần browser vẽ pixels đầu tiên. `Repaint` là vẽ lại pixels khi visual style đổi nhưng layout không đổi.

Các thay đổi thường gây repaint:

- `color`
- `background-color`
- `visibility`
- `outline`
- `box-shadow`
- `text-shadow`
- `border-color`

Repaint thường rẻ hơn reflow vì không cần tính lại geometry. Nhưng repaint vẫn có thể đắt nếu:

- Vùng repaint rất lớn.
- Có shadow/filter phức tạp.
- Có nhiều text/image.
- Animation repaint xảy ra mỗi frame.

### 3.4. 🧩 Composite và Layers

Compositing ghép nhiều layer thành frame cuối. Một số property thường compositor-friendly:

- `transform`
- `opacity`
- Một số video/canvas/composited layer tùy browser.

Animation tốt:

```css
.card {
  transition: transform 180ms ease, opacity 180ms ease;
}

.card:hover {
  transform: translateY(-4px);
  opacity: 0.96;
}
```

Animation dễ gây layout:

```css
.card:hover {
  top: -4px;
}
```

> 💡 `transform` thay đổi cách element được vẽ/composite, không làm element chiếm chỗ khác trong normal layout flow.

### 3.5. ⚡ Layout Thrashing

Layout thrashing là pattern đọc layout và ghi layout xen kẽ, khiến browser phải reflow nhiều lần.

❌ Tệ:

```ts
for (const item of items) {
  const width = container.offsetWidth; // read layout
  item.style.width = `${width / 3}px`; // write layout
}
```

✅ Tốt hơn: đọc trước, ghi sau.

```ts
const width = container.offsetWidth;
const nextWidth = `${width / 3}px`;

for (const item of items) {
  item.style.width = nextWidth;
}
```

Pattern senior:

- Read phase: đo DOM.
- Compute phase: tính toán.
- Write phase: apply class/style.
- Schedule writes bằng `requestAnimationFrame` nếu liên quan frame rendering.

### 3.6. 🧠 `requestAnimationFrame`

`requestAnimationFrame` chạy callback trước frame paint tiếp theo, đồng bộ với refresh rate của browser.

```ts
let x = 0;
let frameId = 0;

function animate() {
  element.style.transform = `translateX(${x}px)`;
  x += 2;
  frameId = requestAnimationFrame(animate);
}

frameId = requestAnimationFrame(animate);

function stop() {
  cancelAnimationFrame(frameId);
}
```

Dùng `requestAnimationFrame` cho animation vì:

- Đồng bộ với browser paint cycle.
- Browser có thể pause/throttle khi tab background.
- Tránh drift và frame timing kém hơn `setTimeout`.

### 3.7. 🧊 `will-change` và CSS Containment

`will-change` báo trước cho browser rằng property sắp thay đổi.

```css
.drawer {
  will-change: transform;
}
```

⚠️ Không lạm dụng:

- Có thể tạo layer mới.
- Tốn GPU memory.
- Dùng quá nhiều có thể làm performance tệ hơn.

CSS containment giới hạn phạm vi ảnh hưởng layout/paint/style.

```css
.widget {
  contain: layout paint;
}
```

Hợp cho component độc lập như card/widget/sidebar item, nơi thay đổi bên trong không nên ảnh hưởng layout bên ngoài.

### 3.8. 📜 Long Lists và DOM Size

DOM càng lớn, layout/paint càng đắt. Với list dài, đừng render mọi item nếu user chỉ nhìn thấy vài chục item.

Giải pháp:

- Virtualization với `react-window`, `react-virtualized`, TanStack Virtual.
- Pagination/infinite scroll có giới hạn.
- Memoized row component khi props ổn định.
- Avoid heavy shadows/filters trên hàng nghìn nodes.

## 4. 🧪 Practical TypeScript/JavaScript Examples

### 4.1. ✅ Batch DOM changes bằng class

❌ Ghi nhiều style rời rạc:

```ts
element.style.width = "240px";
element.style.height = "120px";
element.style.margin = "16px";
element.style.padding = "12px";
```

✅ Dùng class để browser xử lý style change gọn hơn:

```ts
element.classList.add("is-expanded");
```

```css
.is-expanded {
  width: 240px;
  height: 120px;
  margin: 16px;
  padding: 12px;
}
```

### 4.2. ✅ Đọc trước, ghi sau

```ts
function resizeCards(cards: HTMLElement[], container: HTMLElement) {
  const containerWidth = container.getBoundingClientRect().width;
  const cardWidth = Math.floor(containerWidth / 3);

  for (const card of cards) {
    card.style.width = `${cardWidth}px`;
  }
}
```

### 4.3. ✅ Animation bằng `transform`

❌ Gây layout mỗi frame:

```ts
function moveBad(element: HTMLElement, x: number) {
  element.style.left = `${x}px`;
}
```

✅ Chỉ composite-friendly:

```ts
function moveGood(element: HTMLElement, x: number) {
  element.style.transform = `translateX(${x}px)`;
}
```

### 4.4. ✅ React: đo DOM bằng `useLayoutEffect` khi thật sự cần

```tsx
function MeasuredBox() {
  const ref = React.useRef<HTMLDivElement>(null);
  const [height, setHeight] = React.useState(0);

  React.useLayoutEffect(() => {
    if (!ref.current) return;

    const rect = ref.current.getBoundingClientRect();
    setHeight(rect.height);
  }, []);

  return (
    <section>
      <div ref={ref}>Content</div>
      <p>Height: {height}px</p>
    </section>
  );
}
```

> ⚠️ `useLayoutEffect` block paint. Nếu không cần đo trước paint, dùng `useEffect`.

### 4.5. ✅ React: cleanup animation frame

```tsx
function MovingDot() {
  const ref = React.useRef<HTMLDivElement>(null);

  React.useEffect(() => {
    let x = 0;
    let frameId = 0;

    function tick() {
      if (ref.current) {
        ref.current.style.transform = `translateX(${x}px)`;
      }

      x = (x + 1) % 200;
      frameId = requestAnimationFrame(tick);
    }

    frameId = requestAnimationFrame(tick);

    return () => cancelAnimationFrame(frameId);
  }, []);

  return <div ref={ref} className="dot" />;
}
```

### 4.6. ✅ Debug bằng Performance API đơn giản

```ts
performance.mark("layout-work-start");

resizeCards(cards, container);

performance.mark("layout-work-end");
performance.measure("layout-work", "layout-work-start", "layout-work-end");

console.log(performance.getEntriesByName("layout-work"));
```

Trong Chrome DevTools, dùng **Performance tab** để xem `Layout`, `Paint`, `Composite Layers`, long tasks và FPS drops.

## 5. 🏭 Production Notes / React Implications

- ⚛️ **React render vs browser render:** React render tạo virtual tree; browser render pipeline xảy ra sau DOM commit. Tối ưu React không tự động tối ưu layout nếu DOM/CSS vẫn gây reflow nặng.
- 🧩 **State placement:** State đặt quá cao làm nhiều component commit DOM/style hơn, gián tiếp tăng layout/paint work.
- 📏 **Measurement:** Đo DOM trong `useLayoutEffect` khi cần tránh flicker; dùng `ResizeObserver` nếu cần theo dõi size dài hạn.
- 🧾 **Lists:** Với bảng/list lớn, ưu tiên virtualization trước khi micro-optimize CSS.
- 🎞️ **Animation:** Ưu tiên `transform`/`opacity`; tránh animate `width`, `height`, `top`, `left`, `margin`.
- 🧠 **Memoization:** `React.memo` giảm React render, nhưng không giúp nếu layout vẫn bị trigger bởi CSS/DOM mutation ngoài React.
- 🌐 **SSR/hydration:** Tránh đo layout trong render server. Browser-only measurement phải chạy client-side.
- ♿ **Accessibility:** Animation nên tôn trọng `prefers-reduced-motion`.
- 📦 **Images/fonts:** Font loading và image dimensions thiếu `width/height` có thể gây layout shift.
- 📊 **Profiling:** Dùng Chrome Performance, Rendering panel, Layout Shift track, React Profiler, Web Vitals như CLS/INP.

## 6. ⚠️ Common Pitfalls

- ❌ Đọc `offsetWidth` ngay sau khi đổi style, force synchronous reflow.
- ❌ Đọc/ghi layout xen kẽ trong loop.
- ❌ Animate `width`, `height`, `top`, `left` cho animation mỗi frame.
- ❌ Lạm dụng `will-change` trên quá nhiều elements.
- ❌ Render list hàng nghìn rows mà không virtualization.
- ❌ Dùng box-shadow/filter nặng trên nhiều item animated.
- ❌ Không cleanup `requestAnimationFrame`, timer, observer trong React.
- ❌ Đo layout trong render function.
- ❌ Dùng `useLayoutEffect` cho mọi effect, làm block paint không cần thiết.
- ❌ Không set image dimensions, gây layout shift.
- ❌ Tối ưu theo cảm giác mà không xem DevTools Performance.

## 7. ✅ Decision Guide / Checklist

### Chọn kỹ thuật nào?

| Nhu cầu | Chọn | Lý do |
|---|---|---|
| Move/fade animation | `transform`, `opacity` | Thường chỉ composite |
| Thay đổi nhiều style | Toggle class | Batch và dễ maintain |
| Đo DOM rồi cập nhật | Read first, write later | Tránh layout thrashing |
| Animation per frame | `requestAnimationFrame` | Sync với browser paint |
| List lớn | Virtualization | Giảm DOM nodes/layout/paint |
| Component độc lập | `contain: layout paint` | Giới hạn phạm vi reflow/paint |
| Chuẩn bị animation ngắn hạn | `will-change` có kiểm soát | Tránh promote layer trễ |
| Debug jank | Chrome Performance tab | Thấy Layout/Paint/Composite thật |

### Checklist trước khi merge UI nặng

| Câu hỏi | Trả lời ngắn |
|---|---|
| Có animate layout properties không? | Tránh animate `width`, `height`, `top`, `left`; ưu tiên `transform`/`opacity`. |
| Có read-after-write layout trong loop không? | Nếu có, tách read phase và write phase để tránh layout thrashing. |
| DOM size có quá lớn không? | Nếu DOM nhiều node, giảm render, tách component hoặc dùng virtualization. |
| List/table có cần virtualization không? | Cần khi list lớn và chỉ một phần nhỏ hiển thị trong viewport. |
| Image/video có width/height hoặc aspect-ratio ổn định không? | Nên set trước để tránh layout shift. |
| Font loading có gây layout shift không? | Dùng `font-display`, preload hợp lý hoặc fallback font gần kích thước. |
| Có cleanup animation frame/observer không? | Phải `cancelAnimationFrame`, `disconnect`, hoặc remove listener khi unmount. |
| Có tôn trọng `prefers-reduced-motion` không? | Nên giảm/tắt animation mạnh cho user chọn reduced motion. |
| Chrome Performance có Layout/Paint long task bất thường không? | Nếu có, xem nguyên nhân ở DOM size, layout thrashing, paint vùng lớn hoặc CSS nặng. |
| CLS/INP có bị ảnh hưởng không? | Nếu có, fix layout shift và giảm main-thread work trong interaction path. |

## 8. 🗣️ Short Interview Answer

Theo em, browser rendering nên hiểu theo pipeline: DOM/CSSOM tạo render tree, sau đó browser layout để tính vị trí/kích thước, paint để vẽ pixels, rồi composite để ghép layer lên màn hình. Reflow hay layout thường đắt hơn repaint vì nó phải tính lại geometry, còn repaint chỉ vẽ lại visual như màu sắc hoặc background. Tối ưu tốt nhất cho animation là dùng `transform` và `opacity` vì thường chỉ cần composite.

Điểm em luôn chú ý trong production là tránh layout thrashing: không đọc `offsetWidth/getBoundingClientRect` xen kẽ với ghi style trong loop. Em sẽ đọc trước, tính toán, rồi ghi sau, thường schedule bằng `requestAnimationFrame` nếu liên quan frame. Với React, em phân biệt React render với browser rendering; `React.memo` không giải quyết được layout jank nếu DOM/CSS vẫn gây reflow nặng. Em thường dùng Chrome Performance tab để xác nhận bottleneck trước khi tối ưu.

## 9. 📖 Giải thích các thuật ngữ trong topic

- `DOM`: Cây object biểu diễn HTML document.
- `CSSOM`: Cây object biểu diễn CSS rules và computed styles.
- `Render Tree`: Cây gồm các node thực sự cần render lên màn hình.
- `Layout`: Bước tính kích thước và vị trí element.
- `Reflow`: Cách gọi phổ biến của việc layout lại.
- `Paint`: Bước vẽ pixels như text, color, image, border, shadow.
- `Repaint`: Paint lại khi visual thay đổi nhưng layout không đổi.
- `Composite`: Ghép các painted layers thành frame cuối.
- `Layer`: Lớp render riêng có thể được compositor xử lý độc lập.
- `Compositor thread`: Thread ghép layers, có thể hoạt động độc lập hơn main thread trong một số trường hợp.
- `GPU acceleration`: Dùng GPU để xử lý composite/transform hiệu quả hơn.
- `Layout thrashing`: Pattern đọc layout và ghi layout xen kẽ gây nhiều reflow đồng bộ.
- `Forced synchronous reflow`: Khi browser buộc phải flush layout ngay để trả về giá trị đo chính xác.
- `requestAnimationFrame`: API chạy callback trước frame paint tiếp theo.
- `will-change`: CSS hint báo browser chuẩn bị tối ưu property sắp thay đổi.
- `CSS containment`: CSS giới hạn phạm vi ảnh hưởng layout/paint/style của element.
- `Virtualization`: Chỉ render phần list đang thấy để giảm DOM nodes.
- `CLS`: Cumulative Layout Shift, Web Vital đo layout shift ngoài ý muốn.
- `INP`: Interaction to Next Paint, Web Vital đo độ phản hồi tương tác.
- `Jank`: Cảm giác giật/lag khi frame bị miss hoặc main thread bị block.
