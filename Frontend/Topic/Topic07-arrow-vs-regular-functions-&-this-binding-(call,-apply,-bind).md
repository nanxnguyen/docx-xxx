# ➡️ Topic 07 — Arrow vs Regular Functions & `this` Binding (`call`, `apply`, `bind`)

## ⭐ 1. Senior/Staff Summary

> Arrow function dùng **lexical `this`** (lấy từ scope nơi nó được định nghĩa). Regular function dùng **dynamic `this`** (quyết định lúc runtime, theo cách nó được gọi). `call`/`apply`/`bind` là 3 cách để **set `this` thủ công** — `call`/`apply` gọi ngay, `bind` trả về function mới đã "khoá" context.

Trong code thật, 90% bug `this` đến từ 3 tình huống: (1) callback bị tách khỏi receiver (`setTimeout`, event listener, `Promise.then`), (2) dùng arrow nhầm chỗ object method / prototype method, (3) re-create inline arrow trong render loop làm vỡ memoization. Senior cần phân biệt được khi nào lexical là *bạn*, khi nào lexical là *kẻ thù*.

---

## 🧠 2. Key Mental Model

- **Regular function = "tôi nhận `this` khi được gọi"**. Có `this` riêng, có `arguments`, có `prototype`, dùng được `new`.
- **Arrow function = "tôi không có `this` của riêng tôi"**. `this`, `arguments`, `super`, `new.target` đều xuyên qua arrow lên scope ngoài — y hệt một biến closure.
- 4 quy tắc gán `this` cho regular function (priority cao → thấp):
  1. 🔥 `new Fn()` → `this` = instance vừa tạo.
  2. 📌 `fn.call/apply/bind(ctx)` → `this` = `ctx` (explicit).
  3. 🎯 `obj.fn()` → `this` = `obj` (implicit).
  4. 💨 `fn()` standalone → `this` = `undefined` ở strict mode, `globalThis` ở sloppy.
- Arrow **không** tham gia 4 quy tắc trên — `call/apply/bind` set được argument nhưng **không đổi được `this`**.
- `bind` tạo **function mới**. Bind lần 2 không có tác dụng — `this` đã bị khoá lần đầu.

---

## 📚 3. Main Concepts

### 3.1. Arrow vs Regular — 8 điểm khác biệt

| Khía cạnh | Regular function | Arrow function |
|---|---|---|
| **`this`** | Dynamic — theo cách gọi | Lexical — từ scope ngoài, không thay được |
| **`arguments`** | ✅ Có (array-like) | ❌ Không — dùng rest `(...args)` |
| **`new` / constructor** | ✅ Dùng được | ❌ `TypeError: not a constructor` |
| **`prototype` property** | ✅ Có | ❌ `undefined` |
| **Hoisting** | ✅ Function declaration được hoist toàn bộ | ❌ Như `const/let` — TDZ |
| **`super`** | Có (trong method) | Lexical — kế thừa `super` từ method bao quanh |
| **`new.target`** | Có | Lexical — từ scope ngoài |
| **Generator (`function*`)** | ✅ Được | ❌ Không |

> 💡 Arrow không phải "regular function viết tắt". Nó là một loại function khác về mặt ngữ nghĩa — chỉ tình cờ ngắn hơn.

### 3.2. Bốn quy tắc binding `this` (cho regular function)

```ts
// 1️⃣ Default — strict mode: undefined, sloppy: globalThis
function show() { return this; }
show();                    // undefined (strict) | window (sloppy)

// 2️⃣ Implicit — receiver bên trái dấu chấm
const obj = { name: 'A', fn() { return this.name; } };
obj.fn();                  // 'A'   — receiver = obj
const detached = obj.fn;
detached();                // undefined — receiver đã mất

// 3️⃣ Explicit — call/apply/bind
function greet() { return this.name; }
greet.call({ name: 'B' });  // 'B'

// 4️⃣ new — this = instance mới, override 2 và 3
function User(name) { this.name = name; }
new User('C');             // { name: 'C' }
```

⚠️ Priority: `new` > `bind` > `call/apply` > `obj.fn()` > standalone.

### 3.3. `call` vs `apply` vs `bind`

- 📞 **`fn.call(thisArg, a, b, c)`** — gọi ngay, args **riêng lẻ**.
- 📋 **`fn.apply(thisArg, [a, b, c])`** — gọi ngay, args **trong array**. Ngày nay thường thay bằng spread: `fn.call(ctx, ...args)`.
- 🔗 **`fn.bind(thisArg, a, b)`** — **không gọi**, trả về function mới với `this` đã khoá + (optional) partial args. Bind chồng không có tác dụng.

```ts
function introduce(age, city) {
  return `${this.name}, ${age}, ${city}`;
}
const u = { name: 'John' };

introduce.call(u, 25, 'HCM');         // 'John, 25, HCM'
introduce.apply(u, [25, 'HCM']);      // 'John, 25, HCM'
const bound = introduce.bind(u, 25);  // partial application
bound('HCM');                          // 'John, 25, HCM'

bound.call({ name: 'Alice' }, 'HN');  // 'John, 25, HN' — ⚠️ vẫn là John
```

---

## 🛠 4. Practical TypeScript Examples

### 4.1. Callback giữ `this` — arrow thay vì `bind`

```ts
class PriceFeed {
  private symbol = 'VN30F1M';

  subscribe() {
    // ❌ Regular function trong setTimeout — this = undefined
    setTimeout(function () { console.log(this.symbol); }, 0);

    // ✅ Arrow — this kế thừa từ subscribe() → PriceFeed instance
    setTimeout(() => console.log(this.symbol), 0);
  }
}
```

### 4.2. Object method — đừng dùng arrow

```ts
const user = {
  name: 'Alice',
  greetArrow: () => this.name,   // ❌ this lấy từ module scope, không phải user
  greet() { return this.name; }, // ✅ shorthand method, this = user
};
```

### 4.3. Function borrowing với `call`

```ts
// Convert array-like (NodeList, arguments) thành array thật
function toArray(arrLike: ArrayLike<unknown>) {
  return Array.prototype.slice.call(arrLike);
  // Modern: Array.from(arrLike) hoặc [...arrLike]
}
```

### 4.4. Partial application với `bind`

```ts
function track(event: string, payload: Record<string, unknown>, userId: string) {
  return { event, payload, userId };
}

// Khoá userId cho session hiện tại
const trackForUser = track.bind(null, undefined as any, undefined as any, 'u-123');
// Thực tế: prefer closure rõ ràng hơn bind cho readability
const trackForUserClean =
  (event: string, payload: Record<string, unknown>) =>
    track(event, payload, 'u-123');
```

> 💡 `bind` cho partial application giờ ít dùng so với arrow + closure vì kém type-safe với TypeScript.

### 4.5. `apply` để spread vào API "variadic"

```ts
const prices = [101.2, 99.8, 105.0];
Math.max.apply(null, prices); // 105
Math.max(...prices);          // 105 — ✅ modern, type-safe
```

---

## ⚛️ 5. Production Notes / React Implications

### 5.1. Class field arrow vs prototype method

```tsx
class Toolbar extends React.Component {
  // ❌ Mỗi instance một copy hàm → tốn memory với danh sách lớn
  onClick = () => this.props.onSelect(this.props.id);

  // ✅ Một copy trên prototype, nhưng phải bind hoặc dùng inline arrow
  onClick() { this.props.onSelect(this.props.id); }
}
```

- **Class field arrow**: tự bind `this`, đơn giản, nhưng tạo function **riêng cho từng instance** → với list 10k row có thể đáng kể.
- **Prototype method + `bind` trong constructor**: chia sẻ qua prototype, ít tốn memory hơn, nhưng verbose.
- Trong codebase hiện đại (functional components + hooks), tranh luận này gần như biến mất.

### 5.2. Inline arrow trong render — vấn đề reference equality

```tsx
// ❌ Mỗi render tạo arrow mới → child memoized vẫn re-render
<Row onClick={() => onSelect(row.id)} />

// ✅ useCallback ổn định reference
const handleSelect = useCallback((id: string) => onSelect(id), [onSelect]);
<Row onClick={handleSelect} rowId={row.id} />
```

- Chỉ tối ưu khi child có `React.memo` / `PureComponent` / là item trong list lớn.
- Đừng `useCallback` mọi thứ — có cost (deps array compare + closure capture).

### 5.3. Event listener — phải giữ reference để `removeEventListener`

```ts
// ❌ Anonymous bind → reference khác → remove không tháo được
el.addEventListener('click', this.onClick.bind(this));
el.removeEventListener('click', this.onClick.bind(this)); // KHÔNG remove được

// ✅ Bind 1 lần, lưu reference
this.boundOnClick = this.onClick.bind(this);
el.addEventListener('click', this.boundOnClick);
el.removeEventListener('click', this.boundOnClick);
```

### 5.4. `super` trong arrow — lexical, không dùng bừa

```ts
class Base { greet() { return 'base'; } }
class Child extends Base {
  greet() {
    const inner = () => super.greet(); // ✅ arrow kế thừa super từ greet()
    return inner();
  }
}
```

Arrow trong class method giữ được `super` của method bao quanh — tiện cho callback trong override.

### 5.5. SSR / Node: cẩn thận `globalThis`

Ở sloppy mode trên Node, `this` trong top-level function = `globalThis` chứ không phải `window`. Code dựa vào `this === window` sẽ fail khi SSR.

---

## ⚠️ 6. Common Pitfalls

- ❌ **Arrow trong object literal làm method**: `{ greet: () => this.x }` → `this` là scope ngoài, không phải object.
- ❌ **Arrow làm prototype method**: `Foo.prototype.bar = () => this.x` — không bao giờ thấy instance.
- ❌ **`call/apply/bind` lên arrow để đổi `this`**: silent no-op. Chỉ pass args được.
- ❌ **Bind chồng**: `fn.bind(a).bind(b)` → `this` mãi là `a`.
- ❌ **`bind` trong `addEventListener` rồi muốn `remove`**: tạo reference mới, gỡ không được. Phải lưu reference.
- ❌ **`arguments` trong arrow**: throw `ReferenceError`. Dùng `...args`.
- ❌ **Dùng arrow cho constructor**: `new (() => {})()` → `TypeError`.
- ❌ **Tin rằng class field arrow miễn phí**: mỗi instance tạo function riêng → có cost trong list lớn.
- ⚠️ **Mất `this` qua destructuring**: `const { fn } = obj; fn()` → `this = undefined`. Phải `obj.fn()` hoặc `fn.bind(obj)`.
- ⚠️ **`new.target` trong arrow**: lấy từ scope ngoài, không phản ánh việc arrow có được `new` hay không (vì arrow không `new` được).

---

## ✅ 7. Decision Guide

**Khi nào dùng arrow?**

- ✅ Callback ngắn (`map`, `filter`, `then`, `setTimeout`) — muốn giữ `this` outer.
- ✅ Hàm thuần tuý không cần `this`.
- ✅ Class field handler khi rõ ràng cần auto-bind và list không quá lớn.

**Khi nào dùng regular function?**

- ✅ Object method (shorthand `obj.fn() {}`).
- ✅ Prototype method, class instance method.
- ✅ Constructor (hoặc `class`).
- ✅ Cần `arguments`, `new.target`, generator, hoặc `this` động cho function borrowing.

**Khi nào dùng `call` / `apply` / `bind`?**

- `call` → function borrowing, gọi với `this` cụ thể, args đã biết.
- `apply` → legacy variadic. Modern dùng spread `fn(...args)`.
- `bind` → tạo handler để pass đi (event listener, `setTimeout`), partial application.

**Checklist trước khi merge:**

- [ ] Object method dùng regular function (không arrow).
- [ ] Callback giữ context đã dùng arrow hoặc bind đúng chỗ.
- [ ] Inline arrow trong render đã cân nhắc `useCallback` nếu child memo.
- [ ] `addEventListener` có `remove` tương ứng → bind reference đã được lưu.
- [ ] Không gọi `new` lên arrow / không gọi `call(ctx)` lên arrow kỳ vọng đổi `this`.
- [ ] Strict mode bật → không dựa vào `this === window`.

---

## 💬 8. Short Interview Answer

> Em nghĩ điểm quan trọng nhất giữa arrow và regular function là cách gắn `this`. Arrow lấy `this` lexical từ scope ngoài — nó không có `this` của riêng nó, kéo theo cũng không có `arguments`, không dùng `new`, không có `prototype`. Còn regular function thì `this` được quyết định lúc runtime theo 4 quy tắc: `new` > `call/apply/bind` > `obj.fn()` > standalone (mà standalone ở strict mode là `undefined`).
>
> Trong React em thường dùng arrow cho callback và class field handler để tự bind `this`, nhưng em vẫn để ý 2 thứ: một là inline arrow trong render sẽ tạo reference mới mỗi lần, làm hỏng `React.memo` của child — chỗ đó em sẽ `useCallback`. Hai là class field arrow tạo function riêng cho từng instance, nên nếu render list cực lớn em sẽ cân nhắc prototype method với `bind` trong constructor.
>
> `call` và `apply` thì em coi như một — `call` truyền args rời, `apply` truyền args dạng array, mà giờ thường thay bằng spread `fn(...args)` cho rõ. `bind` thì khác — nó không gọi, mà trả về function mới đã khoá `this`, hay dùng cho event handler và partial application. Có một trap em hay nhắc team là `bind` chồng nhau không có tác dụng, và `bind` lên arrow cũng không đổi được `this`, chỉ truyền được args.

---

**📌 Ghi nhớ nhanh:**

- 🎯 Arrow = lexical `this`, không `arguments`, không `new`, không `prototype`.
- 📌 Regular = dynamic `this` theo 4 quy tắc — priority: `new` > `bind` > `call/apply` > implicit > default.
- 📞 `call` / 📋 `apply` = gọi ngay; 🔗 `bind` = function mới, khoá `this` (lần đầu duy nhất).
- ⚛️ React: cẩn thận inline arrow trong render + reference của event handler khi `removeEventListener`.
