# Topic 11: DOM Query/Manipulation và DOM Events/Delegation

## Tóm tắt phỏng vấn

**DOM API** dùng để query/manipulate DOM nodes; **DOM Events** dùng để xử lý tương tác và event flow trong browser.

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### DOM API & Query Methods

**"DOM API cung cấp methods để query và manipulate DOM. Query methods có performance và behaviors khác nhau - cần hiểu live vs static collections."**

**4 Query Methods Chính:**

**1. `getElementById`:**

- **Nhanh nhất** vì browser có thể optimize lookup theo id.
- Return **single element** hoặc `null`.
- IDs nên unique trong document.

**2. `querySelector` / `querySelectorAll`:**

- Nhận **CSS selectors** (`.class`, `#id`, `[attr]`, `:nth-child()`).
- `querySelector`: first match.
- `querySelectorAll`: trả về **static `NodeList`**, không tự update khi DOM thay đổi.

**3. `getElementsByClassName` / `getElementsByTagName`:**

- Trả về **live `HTMLCollection`**.
- Collection tự update khi DOM thay đổi, tiện nhưng dễ gây bug khi vừa loop vừa modify DOM.
- Nhanh và đơn giản hơn selector phức tạp, nhưng ít flexible hơn `querySelectorAll`.

**4. Performance:**

- `getElementById` thường nhanh nhất cho single id.
- Selector càng phức tạp thì query càng tốn chi phí.
- Cache references nếu dùng lại nhiều lần.
- Query trong container thay vì toàn document khi có thể.

**Lỗi thường gặp:**

- Nghĩ `querySelectorAll` là Array: cần `Array.from(nodeList)` hoặc `[...nodeList]` nếu muốn dùng array methods đầy đủ.
- Iterate live `HTMLCollection` trong lúc sửa DOM.
- Query toàn document khi chỉ cần query trong một container.
- Dùng `innerHTML` với user input, dễ tạo XSS.

**Kiến thức senior:**

- `getElementsBy*` -> live `HTMLCollection`.
- `querySelectorAll` -> static `NodeList`.
- `childNodes` -> live `NodeList`.
- DOM manipulation có thể trigger reflow/repaint.
- Batch updates bằng `DocumentFragment` hoặc render một lần.
- Read layout trước, write style sau để tránh **layout thrashing**.
- `MutationObserver` tốt hơn polling khi cần theo dõi DOM changes.

### DOM Events, Event Flow & Delegation

**"Sự kiện DOM có 3 giai đoạn: Capturing từ trên xuống -> Target -> Bubbling từ dưới lên."**

**Luồng sự kiện:**

1. **Capturing phase:** event đi từ `window` -> `document` -> `html` -> ... -> target.
2. **Target phase:** event chạm element thật sự phát event.
3. **Bubbling phase:** event đi từ target -> ... -> `html` -> `document` -> `window`.

**Khái niệm cốt lõi:**

- Mặc định listener chạy trong **bubbling phase**.
- Dùng `{ capture: true }` để nghe ở capturing phase.
- `event.stopPropagation()` ngừng event lan truyền.
- `event.preventDefault()` ngăn hành vi mặc định như submit form hoặc mở link.

```typescript
element.addEventListener('click', handler);
element.addEventListener('click', handler, { capture: true });
```

**Event delegation:**

- Gắn một listener ở parent thay vì gắn cho từng child.
- Tận dụng bubbling để xử lý event từ children.
- Tốt cho performance và dynamic content.

```typescript
document.querySelector('.list')?.addEventListener('click', (event) => {
  const target = event.target as HTMLElement;
  const item = target.closest('.item');

  if (!item) return;

  handleItemClick(item);
});
```

**`target` vs `currentTarget`:**

- `event.target`: element thật sự phát event.
- `event.currentTarget`: element đang gắn listener.
- Trong delegation: `currentTarget` là parent/container, `target` là child được click.

```typescript
parent.addEventListener('click', (event) => {
  console.log(event.target); // child được click
  console.log(event.currentTarget); // parent đang xử lý listener
});
```

**Lỗi thường gặp:**

- Lạm dụng `stopPropagation()`, làm hỏng analytics/global handlers/click-outside.
- Nhầm `preventDefault()` với `stopPropagation()`.
- Delegation nhưng không check target đúng selector.
- Không dùng `closest()` khi user có thể click vào element con bên trong button/item.

**Kiến thức senior:**

- Event delegation giảm memory vì 1 listener thay vì nhiều listener.
- `{ passive: true }` cải thiện scroll/touch performance vì browser biết handler không gọi `preventDefault()`.
- `{ once: true }` tự remove listener sau lần chạy đầu.
- Capturing hữu ích để intercept/debug event trước khi child xử lý.

## 1. DOM Query Methods

| API | Trả về | Live/static | Khi dùng |
| --- | --- | --- | --- |
| `getElementById(id)` | `Element | null` | Single reference | Chọn element theo id, rất nhanh |
| `querySelector(selector)` | First match hoặc `null` | Single reference | CSS selector linh hoạt |
| `querySelectorAll(selector)` | `NodeList` | Static snapshot | Chọn nhiều element bằng CSS selector |
| `getElementsByClassName(name)` | `HTMLCollection` | Live | Chọn theo class, tự update khi DOM đổi |
| `getElementsByTagName(tag)` | `HTMLCollection` | Live | Chọn theo tag, tự update khi DOM đổi |

```typescript
const root = document.getElementById('app');
const firstButton = document.querySelector('button.primary');
const buttons = document.querySelectorAll('button');
const cards = document.getElementsByClassName('card');
```

**Senior note:**

- `querySelector`/`querySelectorAll` nhận CSS selector nên linh hoạt hơn.
- `getElementById` thường nhanh nhất cho single element.
- Query trong container tốt hơn query toàn document nếu scope đã biết:

```typescript
const list = document.querySelector('.todo-list');
const activeItems = list?.querySelectorAll('.todo-item.active');
```

## 2. Live vs Static Collections

`querySelectorAll()` trả về static `NodeList`: DOM thay đổi thì collection cũ không tự update.

`getElementsByClassName()` và `getElementsByTagName()` trả về live `HTMLCollection`: DOM thay đổi thì collection tự update.

```typescript
const staticItems = document.querySelectorAll('.item');
const liveItems = document.getElementsByClassName('item');

document.body.appendChild(document.createElement('div')).className = 'item';

console.log(staticItems.length); // không đổi
console.log(liveItems.length); // tăng
```

**Lỗi hay gặp:** vừa iterate live collection vừa sửa DOM có thể skip item hoặc loop sai.

```typescript
const items = document.getElementsByClassName('item');

// An toàn hơn: convert sang array trước khi modify DOM
Array.from(items).forEach((item) => item.remove());
```

## 3. DOM Manipulation

Các API thường dùng:

```typescript
const div = document.createElement('div');

div.textContent = 'Safe text';
div.className = 'card';
div.id = 'profile-card';
div.dataset.userId = '123';

div.setAttribute('role', 'button');
div.getAttribute('role'); // button
div.removeAttribute('role');

div.classList.add('active');
div.classList.remove('hidden');
div.classList.toggle('selected');
div.classList.contains('active');

document.body.appendChild(div);
div.remove();
```

### `textContent` vs `innerText` vs `innerHTML`

| API | Đặc điểm | Khi dùng |
| --- | --- | --- |
| `textContent` | Text thuần, không parse HTML, không phụ thuộc CSS visibility | Set text an toàn |
| `innerText` | Text hiển thị, có thể trigger layout vì xét CSS | Khi cần text như user thấy |
| `innerHTML` | Parse HTML string | Chỉ dùng với HTML trusted/sanitized |

```typescript
const userInput = '<img src=x onerror=alert(1) />';

element.textContent = userInput; // an toàn
element.innerHTML = userInput; // nguy cơ XSS nếu input không trusted
```

## 4. DOM Performance

Các thao tác DOM có thể gây reflow/repaint. Vấn đề lớn thường là **layout thrashing**: đọc layout rồi ghi style lặp lại nhiều lần.

```typescript
// Không tốt: read/write xen kẽ
items.forEach((item) => {
  const height = item.offsetHeight; // read layout
  item.style.height = `${height + 10}px`; // write layout
});

// Tốt hơn: gom reads trước, writes sau
const heights = items.map((item) => item.offsetHeight);
items.forEach((item, index) => {
  item.style.height = `${heights[index] + 10}px`;
});
```

Khi thêm nhiều nodes, dùng `DocumentFragment` hoặc render một lần.

```typescript
const fragment = document.createDocumentFragment();

for (const user of users) {
  const li = document.createElement('li');
  li.textContent = user.name;
  fragment.appendChild(li);
}

list.appendChild(fragment);
```

**Best practices:**

- Cache DOM references nếu dùng nhiều lần.
- Query trong container thay vì toàn document.
- Batch DOM updates.
- Dùng `MutationObserver` thay vì polling DOM.
- Framework như React/Vue hạn chế direct DOM manipulation, nhưng vẫn cần hiểu DOM thật để debug performance/event issues.

## 5. DOM Event Flow

Khi event xảy ra, browser đi qua 3 phase:

1. **Capturing:** `window -> document -> html -> body -> ... -> target`.
2. **Target:** event đến element thật sự phát event.
3. **Bubbling:** `target -> ... -> body -> html -> document -> window`.

Mặc định `addEventListener` chạy ở bubbling phase.

```typescript
element.addEventListener('click', handler); // bubbling mặc định
element.addEventListener('click', handler, { capture: true }); // capturing
```

```typescript
parent.addEventListener(
  'click',
  () => {
    console.log('capture parent');
  },
  { capture: true }
);

child.addEventListener('click', () => {
  console.log('target child');
});

parent.addEventListener('click', () => {
  console.log('bubble parent');
});
```

Nếu click `child`, thứ tự chính là: capture parent -> target child -> bubble parent.

## 6. Event APIs

```typescript
const handler = (event: MouseEvent) => {
  console.log('clicked');
};

button.addEventListener('click', handler);
button.removeEventListener('click', handler);
```

Listener options:

| Option | Ý nghĩa | Khi dùng |
| --- | --- | --- |
| `capture: true` | Listen ở capturing phase | Intercept/debug trước child |
| `once: true` | Tự remove sau lần chạy đầu | Modal intro, one-time action |
| `passive: true` | Cam kết không gọi `preventDefault()` | Scroll/touch performance |

```typescript
window.addEventListener('scroll', onScroll, { passive: true });
button.addEventListener('click', onClickOnce, { once: true });
```

## 7. `preventDefault` vs `stopPropagation`

`preventDefault()` ngăn hành vi mặc định của browser.

```typescript
form.addEventListener('submit', (event) => {
  event.preventDefault();
  submitWithAjax();
});
```

`stopPropagation()` ngăn event tiếp tục đi qua capturing/bubbling.

```typescript
child.addEventListener('click', (event) => {
  event.stopPropagation();
});
```

**Không lạm dụng `stopPropagation()`** vì có thể làm hỏng analytics, global shortcut, click-outside handler hoặc parent delegation.

## 8. Event Delegation

Event delegation là pattern gắn listener ở parent và dùng bubbling để xử lý event từ children.

```typescript
const list = document.querySelector('.todo-list');

list?.addEventListener('click', (event) => {
  const target = event.target as HTMLElement;
  const deleteButton = target.closest('[data-action="delete"]');

  if (!deleteButton || !list.contains(deleteButton)) return;

  const item = deleteButton.closest('.todo-item');
  item?.remove();
});
```

Lợi ích:

- Ít listener hơn, tiết kiệm memory.
- Tự xử lý được dynamic content thêm sau.
- Code tập trung ở parent/container.

Khi dùng delegation, nên dùng `closest()` thay vì chỉ `matches()` nếu user có thể click vào icon/text bên trong button.

## 9. `target` vs `currentTarget`

| Property | Ý nghĩa |
| --- | --- |
| `event.target` | Element thật sự phát event, có thể là child rất sâu |
| `event.currentTarget` | Element đang gắn listener và đang xử lý callback |

```typescript
parent.addEventListener('click', (event) => {
  console.log(event.target); // child được click
  console.log(event.currentTarget); // parent
});
```

Trong event delegation, `currentTarget` thường là container, còn `target` là element con được user tương tác.

## 10. Common Mistakes

### Không check `null`

```typescript
const button = document.querySelector('button');
button?.addEventListener('click', onClick);
```

### Dùng `innerHTML` với user input

```typescript
element.textContent = userInput; // ưu tiên nếu là text
```

Nếu bắt buộc render HTML từ user/content bên ngoài, phải sanitize trước.

### Nhầm `NodeList` là Array

```typescript
const nodes = document.querySelectorAll('.item');
const items = Array.from(nodes);
items.map((node) => node.textContent);
```

### Quên remove listener khi không còn cần

```typescript
const controller = new AbortController();

window.addEventListener('resize', onResize, {
  signal: controller.signal,
});

controller.abort(); // remove listener
```

### Delegation nhưng không kiểm tra target

```typescript
container.addEventListener('click', (event) => {
  const target = event.target as HTMLElement;
  const button = target.closest('button[data-action]');
  if (!button) return;

  handleAction(button.dataset.action);
});
```

## 11. Câu trả lời ngắn

> DOM query/manipulation là nhóm API để chọn và sửa DOM nodes. Cần hiểu `querySelector` linh hoạt, `getElementById` nhanh cho id, `querySelectorAll` trả static `NodeList`, còn `getElementsBy*` trả live `HTMLCollection`. Khi sửa DOM cần tránh XSS với `innerHTML`, batch updates và tránh layout thrashing. DOM events đi qua capturing -> target -> bubbling; mặc định listener chạy ở bubbling. Event delegation gắn listener ở parent, dùng `target`/`closest()` để xử lý children, giúp performance tốt và hỗ trợ dynamic content. `target` là element thật sự phát event, `currentTarget` là element đang gắn listener.
