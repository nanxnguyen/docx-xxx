# Q16: Compare Data Types - Objects, Strings, Big Numbers & Decimals

## ⭐ Senior/Staff Summary

> So sánh dữ liệu trong JavaScript không chỉ là chọn `===` hay deep compare. Cần hiểu **data semantics**: object so sánh theo reference, string có Unicode/locale, number có floating point precision, còn tiền/số lớn cần boundary rõ ràng.

### 🔑 Key Mental Model

- 📦 **Object / Array / Function**
  - `===` và `Object.is` so sánh **reference**, không so sánh nội dung.
  - Shallow compare hiệu quả khi code dùng **immutability + structural sharing**.
  - Deep compare chỉ nên dùng ở boundary rõ ràng: test, form dirty check, config nhỏ, cache key nhỏ.

- 📝 **String**
  - `===` phù hợp cho id, enum, token, slug đã chuẩn hóa.
  - Unicode có nhiều representation cho cùng ký tự, nên cần `normalize()`.
  - Sort/search tiếng Việt nên dùng `Intl.Collator` hoặc search index đã normalize, không dùng `<`/`>`.

- 🔢 **Number / BigInt / Decimal**
  - `number` là IEEE 754 double, nhanh nhưng có lỗi decimal precision.
  - `BigInt` dành cho integer lớn, không dành cho decimal.
  - Tiền nên lưu bằng **smallest unit** như cents, dong, satoshi, hoặc dùng decimal library khi cần precision/rounding phức tạp.

### ⚠️ Bẫy Nhanh

```ts
{} === {}; // false: khác reference
Object.is(NaN, NaN); // true
+0 === -0; // true
Object.is(+0, -0); // false

0.1 + 0.2 === 0.3; // false
9007199254740992 + 1 === 9007199254740992 + 2; // true

'file10' < 'file2'; // true: lexicographic, không phải numeric sort
```

---

## 1. 📦 Main Concepts: Compare Objects

### Reference Equality

Object, array và function được so sánh theo **identity/reference**.

```ts
const a = { id: 1 };
const b = { id: 1 };
const c = a;

a === b; // false
a === c; // true
```

✅ Dùng reference equality khi:

- Kiểm tra cùng một instance object.
- Tận dụng React/Redux/Zustand selector optimization.
- Cache theo object identity bằng `WeakMap` hoặc `Map`.

⚠️ Không dùng để kết luận 2 object có cùng nội dung.

### `===` vs `Object.is`

`Object.is` gần giống `===`, nhưng xử lý khác ở `NaN` và signed zero.

```ts
NaN === NaN; // false
Object.is(NaN, NaN); // true

+0 === -0; // true
Object.is(+0, -0); // false
```

💡 **React note:** React dùng semantics gần với `Object.is` cho state bailout và dependency comparison. Vì vậy mutate object rồi set lại cùng reference thường không trigger render đúng kỳ vọng.

```tsx
// ❌ Mutate cùng reference
user.name = 'Anna';
setUser(user);

// ✅ Immutable update tạo reference mới cho branch thay đổi
setUser((prev) => ({ ...prev, name: 'Anna' }));
```

### Shallow Compare

Shallow compare chỉ so sánh level đầu tiên. Đây là nền tảng của `React.memo`, `useMemo`, `useCallback`, Redux selector và nhiều store libraries.

```ts
function shallowEqual(
  a: Record<string, unknown>,
  b: Record<string, unknown>,
) {
  if (Object.is(a, b)) return true;

  const aKeys = Object.keys(a);
  const bKeys = Object.keys(b);
  if (aKeys.length !== bKeys.length) return false;

  return aKeys.every((key) => Object.is(a[key], b[key]));
}

shallowEqual({ id: 1 }, { id: 1 }); // true
shallowEqual({ user: { id: 1 } }, { user: { id: 1 } }); // false
```

✅ Shallow compare tốt khi:

- State được update immutable.
- Nested branches không đổi giữ nguyên reference.
- Data normalized theo `id`, ví dụ `entities.users[id]`.

```ts
const nextState = {
  ...state,
  user: {
    ...state.user,
    name: 'Anna',
  },
};

state.settings === nextState.settings; // true: branch không đổi
state.user === nextState.user; // false: branch thay đổi
```

### Deep Compare

Deep compare so sánh recursive toàn bộ nested structure.

```ts
import isEqual from 'lodash/isEqual';

const oldFilters = { status: ['OPEN'], range: { from: 1, to: 10 } };
const newFilters = { status: ['OPEN'], range: { from: 1, to: 10 } };

isEqual(oldFilters, newFilters); // true
```

✅ Dùng deep compare khi:

- Check form dirty state với object nhỏ.
- Test API response hoặc expected UI state.
- So sánh config nhỏ, ít thay đổi, không nằm trong hot path.

⚠️ Tránh deep compare khi:

- Chạy trong render path, animation frame, list lớn, table lớn.
- Object có circular reference.
- Object có function, class instance, getter, prototype phức tạp.
- Data có `Date`, `Map`, `Set`, `RegExp`, `Error`, `ArrayBuffer`, typed array nhưng library không support đúng semantics.

### Stable Object Equality Caveats

"Stable equality" chỉ đáng tin khi bạn kiểm soát shape và canonicalization của data.

- `Date`: so sánh bằng `getTime()` nếu muốn cùng timestamp.
- `Map`: cần quyết định order có quan trọng không. Hai `Map` cùng entries nhưng insert order khác có thể serialize khác.
- `Set`: cần so sánh membership, không phải index.
- `RegExp`: so sánh `source` và `flags`.
- Function: thường chỉ so sánh reference, không so sánh source code.
- Symbol keys/non-enumerable properties: `Object.keys()` không thấy.
- Prototype/class instance: `{ x: 1 }` không giống instance có method/prototype dù JSON giống.

```ts
const sameDate = (a: Date, b: Date) => a.getTime() === b.getTime();

const sameSet = <T>(a: Set<T>, b: Set<T>) =>
  a.size === b.size && [...a].every((item) => b.has(item));
```

### `JSON.stringify` Pitfalls

`JSON.stringify(a) === JSON.stringify(b)` chỉ dùng được cho object cực đơn giản và đã canonical.

```ts
JSON.stringify({ a: 1, b: 2 }) === JSON.stringify({ b: 2, a: 1 }); // false
JSON.stringify({ a: undefined }); // "{}"
JSON.stringify({ date: new Date('2026-01-01') }); // Date thành string ISO
```

⚠️ Pitfalls:

- Phụ thuộc key insertion order.
- Mất `undefined`, function, symbol.
- Không xử lý `BigInt`.
- Throw với circular reference.
- Không giữ prototype/class semantics.

---

## 2. 📝 Main Concepts: Compare Strings

### Exact Equality

Dùng `===` khi dữ liệu cần exact match.

```ts
const role = 'ADMIN';

role === 'ADMIN'; // true
```

✅ Phù hợp cho:

- Token, password hash, signature.
- ID, enum, feature flag key.
- Slug hoặc code đã canonical từ backend.

⚠️ Với security/auth data, không tự normalize nếu backend yêu cầu exact bytes.

### Unicode Normalization

Cùng một ký tự nhìn giống nhau có thể có nhiều Unicode representation khác nhau.

```ts
const composed = '\u00E9'; // é: single code point
const decomposed = 'e\u0301'; // e + combining accent

composed === decomposed; // false
composed.normalize('NFC') === decomposed.normalize('NFC'); // true
```

✅ Rule thực tế:

- Dùng `NFC` cho lưu trữ/display phổ thông.
- Dùng `NFD` khi cần tách dấu để search không dấu.
- Normalize ở ingestion/search boundary, không normalize rải rác trong UI.

### Locale-Aware Sort With `Intl.Collator`

Không sort tên người, địa danh, sản phẩm tiếng Việt bằng `<`, `>` hoặc default `sort()`.

```ts
const viCollator = new Intl.Collator('vi', {
  sensitivity: 'base',
  numeric: true,
  ignorePunctuation: true,
});

const cities = ['Hà Nội', 'Đà Nẵng', 'Cần Thơ', 'Huế', 'Hồ Chí Minh'];

const sortedCities = [...cities].sort(viCollator.compare);
```

💡 Notes:

- `numeric: true`: `file2` đứng trước `file10`.
- `sensitivity: 'base'`: bỏ qua case và dấu, thường hợp với search.
- `sensitivity: 'accent'`: phân biệt dấu, bỏ qua case.
- `sensitivity: 'case'`: phân biệt case.
- Tạo `Intl.Collator` một lần rồi reuse khi sort/filter nhiều lần.

⚠️ `Array.prototype.sort()` mutate array gốc. Trong React state hoặc selector, hãy clone trước:

```ts
const sortedUsers = [...users].sort((a, b) =>
  viCollator.compare(a.fullName, b.fullName),
);
```

### Vietnamese Search

Với search không dấu, nên normalize trước và có thể precompute search key cho list lớn.

```ts
function removeVietnameseAccents(value: string) {
  return value
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/đ/g, 'd')
    .replace(/Đ/g, 'D');
}

function normalizeSearch(value: string) {
  return removeVietnameseAccents(value).toLocaleLowerCase('vi').trim();
}

function includesText(text: string, query: string) {
  return normalizeSearch(text).includes(normalizeSearch(query));
}

includesText('Cà phê Đà Lạt', 'ca phe da lat'); // true
```

Production version cho table/list lớn:

```ts
type User = {
  id: string;
  fullName: string;
};

type SearchableUser = User & {
  searchKey: string;
};

function buildSearchIndex(users: User[]): SearchableUser[] {
  return users.map((user) => ({
    ...user,
    searchKey: normalizeSearch(user.fullName),
  }));
}

function searchUsers(users: SearchableUser[], query: string) {
  const normalizedQuery = normalizeSearch(query);
  return users.filter((user) => user.searchKey.includes(normalizedQuery));
}
```

💡 Precompute giúp tránh normalize hàng nghìn string ở mỗi keystroke.

---

## 3. 🔢 Main Concepts: Numbers, BigInt & Decimals

### JavaScript `number`

JavaScript `number` là IEEE 754 double. Nó phù hợp cho đa số UI calculation, nhưng không an toàn tuyệt đối cho decimal và integer quá lớn.

```ts
0.1 + 0.2; // 0.30000000000000004
Number.MAX_SAFE_INTEGER; // 9007199254740991
Number.isSafeInteger(9007199254740993); // false
```

### Compare Floating Point With Relative Epsilon

Absolute epsilon đơn giản, nhưng relative epsilon tốt hơn khi số có scale khác nhau.

```ts
function nearlyEqual(a: number, b: number, epsilon = Number.EPSILON) {
  const diff = Math.abs(a - b);
  const scale = Math.max(1, Math.abs(a), Math.abs(b));
  return diff <= epsilon * scale;
}

nearlyEqual(0.1 + 0.2, 0.3, 1e-10); // true
nearlyEqual(1_000_000.1 + 0.2, 1_000_000.3, 1e-10); // true
```

✅ Dùng cho:

- Chart, animation, layout measurement.
- UI calculation không phải financial ledger.
- So sánh số từ sensor, canvas, geometry, percentage.

❌ Không dùng epsilon để quyết định tiền, balance, invoice, tax, trading order.

### BigInt

`BigInt` phù hợp cho integer lớn: ID numeric lớn, blockchain smallest unit, counter rất lớn.

```ts
const a = 9007199254740993n;
const b = 9007199254740994n;

a < b; // true
a + 1n; // 9007199254740994n
```

⚠️ Không mix trực tiếp `number` và `bigint`.

```ts
1n + 1; // TypeError
1n + BigInt(1); // 2n
```

### API JSON Large Numbers

JSON parse trong JavaScript sẽ biến number thành `number`, nên integer lớn có thể mất precision trước khi app xử lý.

```ts
JSON.parse('{"id":9007199254740993}').id; // 9007199254740992
```

✅ API contract nên gửi số lớn dưới dạng string:

```ts
type OrderDto = {
  id: string; // large numeric id
  amountMinor: string; // parse to bigint/decimal ở boundary
  currency: 'USD' | 'VND';
};

const amountMinor = BigInt(order.amountMinor);
```

### Money: Smallest Unit

Với tiền, cách đơn giản và robust nhất là lưu bằng đơn vị nhỏ nhất: cents, đồng, satoshi.

```ts
type Currency = 'USD' | 'VND';

type Money = {
  amountMinor: bigint;
  currency: Currency;
};

function compareMoney(a: Money, b: Money): -1 | 0 | 1 {
  if (a.currency !== b.currency) {
    throw new Error('Cannot compare different currencies');
  }

  if (a.amountMinor === b.amountMinor) return 0;
  return a.amountMinor < b.amountMinor ? -1 : 1;
}

compareMoney(
  { amountMinor: 1999n, currency: 'USD' },
  { amountMinor: 2000n, currency: 'USD' },
); // -1
```

### Safe BigInt Money Formatting

Không convert `bigint` lớn sang `number` để format vì có thể mất precision. Format bằng string ở display layer.

```ts
function formatMinorUnits(amountMinor: bigint, fractionDigits: number) {
  const sign = amountMinor < 0n ? '-' : '';
  const value = amountMinor < 0n ? -amountMinor : amountMinor;
  const base = 10n ** BigInt(fractionDigits);
  const major = value / base;
  const minor = (value % base).toString().padStart(fractionDigits, '0');

  return fractionDigits === 0
    ? `${sign}${major.toString()}`
    : `${sign}${major.toString()}.${minor}`;
}

formatMinorUnits(1999n, 2); // "19.99"
formatMinorUnits(123456789012345678901n, 2); // "1234567890123456789.01"
```

💡 Có thể đưa string này vào UI formatter/currency label riêng. Chỉ dùng `Intl.NumberFormat` với `Number(...)` khi chắc chắn giá trị nằm trong safe range.

### Decimal Libraries

Khi cần decimal precision thật sự, dùng library như `big.js`, `decimal.js`, hoặc `bignumber.js`.

- `big.js`
  - Nhẹ, API nhỏ.
  - Phù hợp e-commerce và phép tính decimal phổ biến.

- `decimal.js`
  - Nhiều config precision/rounding.
  - Phù hợp financial/scientific calculation phức tạp hơn.

- `bignumber.js`
  - Hay gặp trong crypto/blockchain ecosystem.
  - Hỗ trợ nhiều API cho integer/decimal lớn.

```ts
import Decimal from 'decimal.js';

const total = new Decimal('0.1').plus('0.2');

total.equals(new Decimal('0.3')); // true
total.toFixed(2); // "0.30"
```

⚠️ Không tạo decimal từ float đã sai:

```ts
new Decimal(0.1 + 0.2).equals(new Decimal('0.3')); // false
new Decimal('0.1').plus('0.2').equals(new Decimal('0.3')); // true
```

---

## 4. ⚛️ Production Notes & React Implications

- ✅ **React state:** immutable update giúp reference thay đổi đúng chỗ, shallow compare mới hiệu quả.
- ✅ **Dependencies:** object/function tạo mới mỗi render sẽ làm `useEffect`, `useMemo`, `useCallback` chạy lại.
- ✅ **Memoization:** dùng `React.memo`/selector khi có profiling hoặc component thật sự expensive, không bọc đại trà.
- ✅ **Sort:** `sort()` mutate array, nên clone trước khi sort state/props.
- ✅ **Search:** normalize/precompute search key cho list lớn, kết hợp debounce nếu input search gọi API hoặc filter nặng.
- ✅ **API boundary:** large number, money, decimal nên đi qua JSON dưới dạng string, parse ở boundary có validation.
- ✅ **SSR/locale:** server và browser có thể khác ICU/locale data. Với sort quan trọng, cố định locale/options và test snapshot cẩn thận.
- ✅ **Testing:** test edge cases: `NaN`, `+0/-0`, Unicode composed/decomposed, tiếng Việt có `đ`, large integer, rounding, currency mismatch.
- ✅ **Performance:** deep compare, normalize string và decimal calculation đều có cost. Đặt ở event handler, selector memoized, worker, hoặc ingestion step nếu data lớn.

---

## 5. 🔥 Common Pitfalls

- ❌ Dùng `JSON.stringify` làm generic deep equality.
- ❌ Mutate nested state rồi kỳ vọng React re-render/memo hoạt động đúng.
- ❌ Deep compare trong render path để "fix" object dependency thay vì ổn định data flow.
- ❌ Sort props/state trực tiếp bằng `array.sort()`.
- ❌ Search tiếng Việt bằng `toLowerCase().includes()` mà không normalize dấu.
- ❌ Tạo `Intl.Collator` trong từng comparator call.
- ❌ Dùng `Number` cho API ID lớn hoặc money minor unit lớn.
- ❌ Convert `bigint` lớn sang `number` để format.
- ❌ Dùng `toFixed()` làm business logic rounding.
- ❌ So sánh tiền khác currency.
- ❌ Truyền `new Decimal(0.1 + 0.2)` thay vì string input.

---

## 6. 🧭 Decision Guide / Checklist

### Object

- Same instance?
  - Dùng `a === b`.
- React dependency/state bailout?
  - Nghĩ theo `Object.is` semantics.
- Props/state level 1, immutable update?
  - Dùng shallow compare.
- Nested config nhỏ hoặc test assertion?
  - Dùng deep compare library có support type cần thiết.
- Cần equality ổn định cross-process/cache key?
  - Canonicalize data, sort keys có chủ đích, define schema rõ ràng.

### String

- ID/token/enum?
  - Dùng `===`.
- Dữ liệu từ nhiều nguồn có thể khác Unicode representation?
  - Normalize `NFC`.
- Sort/search theo tiếng Việt hoặc tên người?
  - Dùng `Intl.Collator('vi', options)`.
- Search không dấu?
  - Normalize `NFD`, remove combining marks, xử lý `đ/Đ`, precompute search key nếu list lớn.
- Sort trong React state?
  - Clone trước: `[...items].sort(...)`.

### Number / Money / Decimal

- Integer nằm trong safe range?
  - `Number.isSafeInteger(value)` rồi mới dùng `number`.
- Float UI calculation?
  - Dùng relative epsilon.
- Money?
  - Lưu smallest unit + currency, không dùng float.
- Large integer từ API?
  - Nhận string, parse `BigInt` hoặc decimal ở boundary.
- Decimal precision/rounding phức tạp?
  - Dùng decimal library, input bằng string, define rounding rule.
- Display money từ `bigint`?
  - Format bằng string, chỉ convert sang `number` khi chắc chắn safe.

---

## 7. 🎯 Short Interview Answer

> Em nghĩ điểm quan trọng là phải so sánh theo đúng semantics của dữ liệu. Với object, JavaScript so sánh reference, nên trong React em thường dùng immutability và structural sharing để shallow compare đủ nhanh và đúng; deep compare chỉ dùng ở boundary nhỏ như form dirty check hoặc test. Với string, `===` chỉ hợp cho exact match như id/token, còn sort/search tiếng Việt thì em dùng `Intl.Collator` và normalize Unicode, đặc biệt với search không dấu. Với number, em không dùng float cho tiền vì có precision issue như `0.1 + 0.2`; tiền nên lưu smallest unit hoặc dùng decimal library, còn số nguyên rất lớn thì API nên gửi string và frontend parse sang `BigInt` hoặc decimal ở boundary. Em thấy các lỗi production hay nằm ở chỗ mutate state, `sort()` làm đổi array gốc, `JSON.stringify` deep compare bừa bãi, và convert big number sang `number` quá sớm.
