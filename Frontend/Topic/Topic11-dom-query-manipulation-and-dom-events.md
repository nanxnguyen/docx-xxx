# Topic 11: DOM Query, Manipulation và DOM Events

## ✅ Senior/Staff Summary

- **DOM query** là cách chọn node trong cây DOM. Senior cần hiểu tradeoff giữa API nhanh/chuyên dụng (`getElementById`) và API linh hoạt (`querySelector`), cũng như **static `NodeList` vs live `HTMLCollection`**.
- **DOM manipulation** không chỉ là thêm/xóa element. Điểm quan trọng là update đúng, an toàn với XSS, không gây layout thrashing, và giữ accessibility/focus state ổn định.
- **DOM events** đi qua 3 phase: **capturing -> target -> bubbling**. Mặc định listener chạy ở bubbling phase.
- **Event delegation** giúp giảm số listener, xử lý dynamic content tốt, nhưng phải check `target`, `closest()`, containment, và Shadow DOM boundary khi cần.
- **Production code** nên cleanup listener bằng `removeEventListener` hoặc `AbortController`, dùng `{ passive, once, capture }` đúng ngữ cảnh, tránh lạm dụng `stopPropagation()`.
- **React/Vue/Angular** che bớt DOM trực tiếp, nhưng hiểu DOM thật vẫn rất quan trọng để debug hydration, focus, scroll, portal, custom event, performance và third-party integration.

## 🧠 Mental Model

- **Query:** chọn đúng node, đúng scope, đúng thời điểm.
  - Query trong container thay vì toàn `document` nếu đã biết phạm vi.
  - Cache reference khi dùng lặp lại trên hot path.
  - Không assume element luôn tồn tại, đặc biệt trong SSR/hydration hoặc lazy-rendered UI.

- **Manipulation:** thay đổi DOM càng ít lần càng tốt.
  - Tạo node bằng API (`createElement`, `textContent`, `classList`, `dataset`) thay vì nối string HTML nếu không cần.
  - Gom read layout trước, write layout sau để tránh forced reflow.
  - Dùng `DocumentFragment`, `<template>`, `replaceChildren()` hoặc framework render một lần khi thêm nhiều node.

- **Events:** event là một luồng đi qua cây DOM.
  - `event.target`: node thật sự phát event.
  - `event.currentTarget`: node đang gắn listener.
  - `preventDefault()` chặn default browser behavior.
  - `stopPropagation()` chặn event flow, nên dùng rất có chủ đích.

## 1. 🔎 DOM Query APIs

### API chính

- **`document.getElementById(id)`**
  - Trả về một `HTMLElement | null`.
  - Thường nhanh nhất cho single id vì browser có thể optimize lookup.
  - Phù hợp khi id là unique contract rõ ràng, ví dụ root app, modal container, form id.
  - Không nhận CSS selector, nên không cần escape ký tự đặc biệt kiểu CSS selector.

- **`querySelector(selector)` / `querySelectorAll(selector)`**
  - Nhận CSS selector: `.class`, `#id`, `[data-x]`, `:not()`, `:nth-child()`.
  - `querySelector()` trả về first match hoặc `null`.
  - `querySelectorAll()` trả về **static `NodeList`**: snapshot không tự update khi DOM đổi.
  - Rất linh hoạt nhưng selector phức tạp có thể khó đọc, dễ chậm hơn nếu query rộng và lặp nhiều.
  - Nếu selector chứa dữ liệu động, dùng `CSS.escape()` để tránh selector lỗi hoặc injection selector.

- **`getElementsByClassName()` / `getElementsByTagName()`**
  - Trả về **live `HTMLCollection`**: collection tự update khi DOM thay đổi.
  - Có thể hữu ích khi cần trạng thái live, nhưng dễ bug nếu vừa loop vừa add/remove node.
  - Ít linh hoạt hơn CSS selector.

- **`childNodes` / `children`**
  - `childNodes` gồm cả text/comment nodes; thường là live `NodeList`.
  - `children` chỉ gồm element nodes; trả về live `HTMLCollection`.
  - Khi xử lý UI element, thường dùng `children` hoặc selector rõ ràng thay vì `childNodes`.

```typescript
const app = document.getElementById('app');
const firstPrimaryButton = document.querySelector<HTMLButtonElement>('button.primary');
const allCards = document.querySelectorAll<HTMLElement>('.card');
const liveRows = document.getElementsByClassName('row');

const table = document.querySelector<HTMLElement>('[data-table="orders"]');
const selectedRows = table?.querySelectorAll<HTMLElement>('[data-state="selected"]');
```

### `getElementById` vs `querySelector`

- Dùng **`getElementById('app')`** khi:
  - Chỉ cần tìm theo id.
  - Id là contract ổn định.
  - Muốn API đơn giản, nhanh, ít lỗi selector.

- Dùng **`querySelector('#app')`** khi:
  - Cần selector phức tạp hoặc query scoped trong container.
  - Muốn cùng một style query cho class/attribute/relationship.
  - Cần generic helper nhận CSS selector.

```typescript
// ✅ Scoped query tốt hơn query toàn document khi container đã biết
const dialog = document.querySelector<HTMLDialogElement>('[data-dialog="profile"]');
const closeButton = dialog?.querySelector<HTMLButtonElement>('[data-action="close"]');
```

## 2. 🔁 Static `NodeList` vs Live `HTMLCollection`

- **Static `NodeList`**
  - Tạo bởi `querySelectorAll()`.
  - Không đổi khi DOM thay đổi sau đó.
  - Dễ predict hơn trong đa số production code.

- **Live `HTMLCollection`**
  - Tạo bởi `getElementsByClassName()`, `getElementsByTagName()`, `children`.
  - Tự update khi DOM thay đổi.
  - Có thể gây bug khi iterate và mutate cùng lúc.

```typescript
const staticItems = document.querySelectorAll<HTMLElement>('.item');
const liveItems = document.getElementsByClassName('item');

const newItem = document.createElement('div');
newItem.className = 'item';
document.body.appendChild(newItem);

console.log(staticItems.length); // không đổi
console.log(liveItems.length); // tăng
```

```typescript
const items = document.getElementsByClassName('item');

// ✅ Convert sang array trước khi remove để tránh live collection thay đổi trong lúc loop
Array.from(items).forEach((item) => item.remove());
```

## 3. 🧱 DOM Manipulation

### Node, attribute, class, dataset, style

```typescript
const card = document.createElement('article');

card.id = 'profile-card';
card.dataset.userId = 'u_123';
card.setAttribute('aria-label', 'User profile');

card.classList.add('card', 'is-active');
card.classList.toggle('is-selected', true);
card.classList.remove('is-loading');

card.textContent = 'Nguyen Anh Nhut';
document.body.appendChild(card);
```

- **`dataset`**
  - Dùng cho state/metadata nhỏ cần nằm trên DOM: `data-user-id`, `data-action`.
  - Trong JS đọc bằng camelCase: `element.dataset.userId`.
  - Giá trị luôn là string hoặc `undefined`, không nên nhét object lớn vào dataset.

- **`classList`**
  - Ưu tiên hơn nối chuỗi `className` khi add/remove/toggle class.
  - Giảm bug mất class cũ hoặc duplicated class.

- **Inline `style`**
  - Phù hợp cho value runtime như width/transform/tọa độ.
  - Với style có ý nghĩa UI state, ưu tiên class CSS để dễ maintain.
  - Nếu update nhiều style, gom lại để tránh layout work lặp.

```typescript
// ✅ Batch style writes
Object.assign(card.style, {
  transform: 'translateY(8px)',
  opacity: '1',
});
```

### `textContent` vs `innerText` vs `innerHTML`

- **`textContent`**
  - Set/get text thuần, không parse HTML.
  - An toàn hơn cho user input.
  - Không phụ thuộc CSS visibility.

- **`innerText`**
  - Gần với text user nhìn thấy.
  - Có thể trigger layout vì phải xét CSS/rendered state.
  - Dùng khi thật sự cần visible text.

- **`innerHTML`**
  - Parse HTML string thành DOM.
  - Chỉ dùng với HTML trusted hoặc đã sanitize.
  - Với content từ user/CMS/third-party, cần DOMPurify hoặc cơ chế tương đương; ở hệ thống nghiêm ngặt có thể dùng **Trusted Types** để giảm XSS sink.

```typescript
const userInput = '<img src=x onerror=alert(1) />';

element.textContent = userInput; // ✅ render như text
element.innerHTML = userInput; // ❌ XSS nếu input không trusted
```

### `DocumentFragment`, `<template>` và render nhiều node

```typescript
const fragment = document.createDocumentFragment();

for (const user of users) {
  const li = document.createElement('li');
  li.dataset.userId = user.id;
  li.textContent = user.name;
  fragment.appendChild(li);
}

list.replaceChildren(fragment);
```

```typescript
const template = document.querySelector<HTMLTemplateElement>('#user-row-template');

if (template) {
  const row = template.content.firstElementChild?.cloneNode(true) as HTMLElement | null;
  row?.querySelector('[data-field="name"]')?.replaceChildren('Ada Lovelace');
  if (row) tableBody.appendChild(row);
}
```

💡 **Production note:** `DocumentFragment` giúp build subtree ngoài DOM rồi append một lần. `<template>` hữu ích khi HTML structure dài nhưng vẫn muốn clone an toàn hơn so với tự nối string HTML.

## 4. ⚡ DOM Performance: Reflow, Repaint, Layout Thrashing

- **Reflow/layout:** browser tính lại kích thước/vị trí element.
- **Repaint:** browser vẽ lại pixels nhưng không nhất thiết đổi layout.
- **Layout thrashing:** code đọc layout rồi ghi style xen kẽ liên tục, ép browser flush layout nhiều lần.

```typescript
// ❌ Read/write xen kẽ trong loop
items.forEach((item) => {
  const height = item.offsetHeight; // read layout
  item.style.height = `${height + 10}px`; // write layout
});

// ✅ Gom reads trước, writes sau
const heights = items.map((item) => item.offsetHeight);

items.forEach((item, index) => {
  item.style.height = `${heights[index] + 10}px`;
});
```

- Ưu tiên `classList`/CSS transitions thay vì set nhiều inline style rời rạc.
- Dùng `requestAnimationFrame()` cho DOM writes liên quan animation/frame.
- Dùng `transform`/`opacity` cho animation thường mượt hơn `top/left/width/height`.
- Dùng `MutationObserver` khi cần theo dõi DOM change thay vì polling.
- Profile bằng Chrome DevTools Performance tab trước khi tối ưu quá sớm.

## 5. 🧭 DOM Event Flow

Khi event xảy ra, browser dispatch theo 3 phase:

1. **Capturing:** `window -> document -> html -> body -> ... -> target`.
2. **Target:** event đến node thật sự phát event.
3. **Bubbling:** `target -> ... -> body -> html -> document -> window`.

```typescript
element.addEventListener('click', onClick); // bubbling mặc định
element.addEventListener('click', onClickCapture, { capture: true }); // capturing
```

```typescript
parent.addEventListener(
  'click',
  () => console.log('capture parent'),
  { capture: true }
);

child.addEventListener('click', () => console.log('target child'));
parent.addEventListener('click', () => console.log('bubble parent'));

// Click child: capture parent -> target child -> bubble parent
```

### `target`, `currentTarget`, `composedPath()`

```typescript
container.addEventListener('click', (event) => {
  const target = event.target as HTMLElement;
  const currentTarget = event.currentTarget as HTMLElement;

  console.log(target); // element thật sự được click
  console.log(currentTarget); // container đang gắn listener
  console.log(event.composedPath()); // đường đi event, hữu ích với Shadow DOM/portal-like UI
});
```

- `event.target` có thể là icon/text node sâu bên trong button.
- `event.currentTarget` là element đang chạy listener hiện tại.
- `event.composedPath()` hữu ích khi làm click-outside, Shadow DOM, Web Components, hoặc UI được render qua boundary phức tạp.

## 6. 🎛️ Event Listener APIs và Cleanup

```typescript
const onResize = () => {
  console.log(window.innerWidth);
};

window.addEventListener('resize', onResize);
window.removeEventListener('resize', onResize);
```

- **`capture: true`**
  - Nghe ở capturing phase.
  - Hữu ích để intercept/debug trước khi child xử lý.

- **`once: true`**
  - Tự remove sau lần chạy đầu.
  - Phù hợp với one-time action: onboarding step, first interaction, transition end.

- **`passive: true`**
  - Báo với browser rằng handler không gọi `preventDefault()`.
  - Tốt cho scroll/touch/wheel performance.
  - Không dùng nếu cần chặn scroll/default behavior.

- **`signal: AbortSignal`**
  - Cleanup nhiều listener cùng lúc, rất hữu ích trong component lifecycle hoặc imperative integration.

```typescript
const controller = new AbortController();

window.addEventListener('resize', onResize, { signal: controller.signal });
document.addEventListener('keydown', onKeyDown, { signal: controller.signal });

controller.abort(); // remove tất cả listener dùng signal này
```

⚠️ `removeEventListener` cần cùng function reference và option capture tương ứng. Anonymous function inline rất khó remove thủ công.

## 7. 🛑 `preventDefault()` vs `stopPropagation()`

- **`preventDefault()`**
  - Chặn default behavior của browser.
  - Ví dụ: chặn form submit reload page, chặn link navigation, chặn drag/drop default.
  - Chỉ có tác dụng nếu event `cancelable`.

- **`stopPropagation()`**
  - Chặn event tiếp tục lan qua capture/bubble.
  - Không chặn default behavior.
  - Dễ làm hỏng analytics, global shortcuts, click-outside, parent delegation.

- **`stopImmediatePropagation()`**
  - Chặn propagation và chặn các listener khác trên cùng element chạy sau đó.
  - Rất mạnh, hiếm khi nên dùng trong app code.

```typescript
form.addEventListener('submit', (event) => {
  event.preventDefault();
  submitWithAjax(new FormData(form));
});

child.addEventListener('click', (event) => {
  event.stopPropagation(); // dùng khi thật sự muốn parent không nhận event
});
```

## 8. 🧩 Event Delegation

Event delegation là pattern gắn listener ở parent/container, rồi dùng bubbling để xử lý event từ child.

```typescript
const list = document.querySelector<HTMLElement>('.todo-list');

list?.addEventListener('click', (event) => {
  const target = event.target as HTMLElement;
  const deleteButton = target.closest<HTMLButtonElement>('[data-action="delete"]');

  if (!deleteButton || !list.contains(deleteButton)) return;

  const item = deleteButton.closest<HTMLElement>('.todo-item');
  item?.remove();
});
```

✅ Lợi ích:

- Ít listener hơn, giảm memory và setup cost.
- Tự xử lý dynamic content thêm sau.
- Logic tập trung ở container, hợp với list/table/menu lớn.

⚠️ Cẩn thận:

- Dùng `closest()` thay vì chỉ `matches()` khi user có thể click icon/text bên trong button.
- Luôn kiểm tra `container.contains(matchedElement)` để tránh match element ngoài container.
- Một số event không bubble như `focus`/`blur`; có thể dùng `focusin`/`focusout` hoặc capture.
- Trong Shadow DOM, event retargeting có thể làm `target` khác kỳ vọng; cân nhắc `composedPath()`.

## 9. ⌨️ Forms, Keyboard, Pointer và Focus

### Forms và input events

- `input`: chạy khi value thay đổi theo từng lần nhập, phù hợp search/autosave.
- `change`: thường chạy khi commit value, ví dụ blur/select change.
- `submit`: xử lý submit ở form, không chỉ click button.
- `FormData`: lấy dữ liệu form theo name attributes, tốt cho progressive enhancement.

```typescript
searchInput.addEventListener('input', (event) => {
  const value = (event.currentTarget as HTMLInputElement).value;
  debouncedSearch(value);
});

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const data = new FormData(event.currentTarget as HTMLFormElement);
  saveProfile(Object.fromEntries(data));
});
```

### Keyboard events

- Dùng `event.key` cho ý nghĩa phím (`Enter`, `Escape`, `ArrowDown`) thay vì keycode cũ.
- Không phá native keyboard behavior của input/select/textarea.
- Với shortcut global, bỏ qua khi focus đang ở editable field.

```typescript
document.addEventListener('keydown', (event) => {
  const target = event.target as HTMLElement;
  const isTyping = target.matches('input, textarea, select, [contenteditable="true"]');

  if (isTyping) return;
  if (event.key === 'Escape') closeTopLayer();
});
```

### Pointer events

- Ưu tiên **Pointer Events** (`pointerdown`, `pointermove`, `pointerup`) khi cần hỗ trợ mouse, touch, pen bằng một model chung.
- `click` vẫn tốt cho action đơn giản vì thân thiện với keyboard/screen reader khi dùng button/link đúng semantic.
- Dùng `setPointerCapture()` cho drag interaction cần tiếp tục nhận move/up dù pointer rời khỏi element.

```typescript
slider.addEventListener('pointerdown', (event) => {
  slider.setPointerCapture(event.pointerId);
  startDrag(event.clientX);
});
```

### Focus và accessibility

- Dùng element semantic (`button`, `a`, `input`) trước khi tự build div có role.
- Khi mở modal/menu, quản lý focus: đưa focus vào UI mới, trap focus nếu cần, restore focus khi đóng.
- Với dynamic status, dùng `aria-live` để screen reader biết nội dung vừa thay đổi.
- Đừng chỉ listen `click`; action quan trọng phải hoạt động bằng keyboard.

```typescript
statusElement.setAttribute('aria-live', 'polite');
statusElement.textContent = 'Đã lưu thay đổi';
```

## 10. ⚛️ React Integration và Escape Hatches

- React dùng Synthetic Events nhưng vẫn dựa trên native DOM events. Khi cần event thật, dùng `event.nativeEvent`.
- Direct DOM manipulation trong React nên giới hạn ở escape hatch:
  - focus/selection/scroll measurement;
  - third-party widget;
  - canvas/video/map;
  - imperative animation.
- Dùng `ref` + `useEffect`/`useLayoutEffect` để đọc hoặc sửa DOM sau render.
- Cleanup listener trong effect return hoặc dùng `AbortController`.
- SSR/hydration: không query `document` trong render path; browser-only DOM code chạy trong effect.
- Hydration mismatch có thể xảy ra nếu DOM bị third-party script sửa trước khi React hydrate.

```typescript
function SearchBox() {
  const inputRef = React.useRef<HTMLInputElement>(null);

  React.useEffect(() => {
    inputRef.current?.focus();
  }, []);

  return <input ref={inputRef} type="search" />;
}
```

```typescript
function useWindowResize(onResize: () => void) {
  React.useEffect(() => {
    const controller = new AbortController();

    window.addEventListener('resize', onResize, {
      passive: true,
      signal: controller.signal,
    });

    return () => controller.abort();
  }, [onResize]);
}
```

## 11. 🧪 Testing và Debugging

- **Unit/component tests**
  - Dùng Testing Library query theo role/label/text thay vì class nội bộ.
  - Test behavior: user click, keyboard, submit, focus, aria state.
  - Với jsdom, lưu ý layout APIs như `offsetHeight`, `getBoundingClientRect()` thường không phản ánh layout thật.

- **E2E tests**
  - Dùng Playwright/Cypress cho pointer, keyboard, focus trap, drag/drop, scroll, dialog, real browser behavior.
  - Test a11y flow quan trọng: tab order, Escape close, restore focus.

- **Debugging**
  - Chrome DevTools: Event Listeners panel, break on subtree modification, Performance tab.
  - Log `event.target`, `event.currentTarget`, `event.eventPhase`, `event.composedPath()`.
  - Dùng `getEventListeners(element)` trong DevTools console khi browser hỗ trợ.

## 12. ⚠️ Common Pitfalls

- ❌ **Không check `null` sau query**

```typescript
const button = document.querySelector<HTMLButtonElement>('[data-save]');
button?.addEventListener('click', save);
```

- ❌ **Dùng `innerHTML` với user input**

```typescript
output.textContent = userInput; // ✅ nếu chỉ cần text
```

- ❌ **Nhầm `NodeList` là Array đầy đủ**

```typescript
const nodes = document.querySelectorAll('.item');
const items = Array.from(nodes);
items.map((node) => node.textContent);
```

- ❌ **Loop live collection trong lúc mutate DOM**

```typescript
Array.from(document.getElementsByClassName('toast')).forEach((toast) => {
  toast.remove();
});
```

- ❌ **Quên cleanup listener**

```typescript
const controller = new AbortController();
window.addEventListener('resize', onResize, { signal: controller.signal });

// Khi unmount/destroy
controller.abort();
```

- ❌ **Delegation nhưng match sai target**

```typescript
container.addEventListener('click', (event) => {
  const target = event.target as HTMLElement;
  const button = target.closest<HTMLButtonElement>('button[data-action]');

  if (!button || !container.contains(button)) return;
  handleAction(button.dataset.action);
});
```

- ❌ **Lạm dụng `stopPropagation()`**
  - Có thể làm hỏng parent handler, analytics, global shortcut, click-outside.
  - Ưu tiên thiết kế selector/condition rõ ràng trước khi chặn propagation.

## 13. 🧭 Decision Guide / Checklist

- **Query**
  - Cần id duy nhất? Dùng `getElementById`.
  - Cần selector linh hoạt? Dùng `querySelector`/`querySelectorAll`.
  - Cần nhiều item ổn định để loop/mutate? Dùng static `NodeList` hoặc convert sang array.
  - Selector có dữ liệu động? Dùng `CSS.escape()`.

- **Manipulation**
  - Chỉ render text? Dùng `textContent`.
  - Render HTML không trusted? Sanitize bằng DOMPurify hoặc Trusted Types policy.
  - Add nhiều node? Dùng `DocumentFragment`, `<template>`, `replaceChildren()`.
  - Update style nhiều lần? Batch reads/writes, ưu tiên class.

- **Events**
  - Handler chỉ chạy một lần? `{ once: true }`.
  - Scroll/touch/wheel không gọi `preventDefault()`? `{ passive: true }`.
  - Cần intercept trước child? `{ capture: true }`.
  - Cần cleanup gọn? `AbortController`.
  - List/table dynamic lớn? Event delegation.
  - Click-outside/Shadow DOM? Kiểm tra `composedPath()`.

- **Accessibility**
  - Action dùng được bằng keyboard chưa?
  - Focus có được move/restore đúng khi mở/đóng modal chưa?
  - Dynamic status quan trọng có `aria-live` chưa?
  - Có đang thay button bằng `div` không cần thiết không?

- **React/SSR**
  - DOM code có chạy trong effect thay vì render path không?
  - Listener/observer có cleanup không?
  - Direct DOM write có xung đột với React render/hydration không?

## 14. 💬 Short Interview Answer

> Em nghĩ DOM query/manipulation không khó ở API, mà khó ở việc hiểu browser behavior và production tradeoff. Theo em, `getElementById` phù hợp khi cần một id rõ ràng và nhanh, còn `querySelector`/`querySelectorAll` linh hoạt hơn vì dùng CSS selector; cần nhớ `querySelectorAll` trả static `NodeList`, còn `getElementsBy*` thường trả live `HTMLCollection`.
>
> Khi sửa DOM, em thường ưu tiên `textContent`, `classList`, `dataset`, `createElement` và batch update bằng `DocumentFragment` hoặc render một lần. Với HTML string từ user/CMS, em không gán thẳng vào `innerHTML` mà phải sanitize, ví dụ DOMPurify hoặc Trusted Types trong hệ thống có yêu cầu cao.
>
> Về events, em thấy điểm quan trọng là event flow gồm capturing, target và bubbling. Delegation giúp giảm listener và xử lý dynamic list tốt, nhưng phải dùng `closest()`, check containment, hiểu `target` vs `currentTarget`, và cẩn thận với Shadow DOM qua `composedPath()`. Em cũng tránh lạm dụng `stopPropagation()`, dùng `preventDefault()` đúng mục đích, và cleanup listener bằng `removeEventListener` hoặc `AbortController`, đặc biệt khi tích hợp với React hoặc third-party DOM code.
