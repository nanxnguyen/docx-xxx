# 🔀 Q16: Compare Data Types - Objects, Strings, Big Numbers & Decimals




**⚡ Quick Summary:**
> So sánh dữ liệu phức tạp: Objects (deep/shallow), Strings (localeCompare, Unicode), Big Numbers/Decimals (precision handling)

**💡 Ghi Nhớ:**
- 🎯 **Objects**: Shallow (reference) vs Deep (recursive) - dùng lodash isEqual cho circular refs
- 🌍 **Strings**: `localeCompare()` cho tiếng Việt, `Intl.Collator` cho performance
- 💰 **Big Numbers**: Dùng libraries (decimal.js, big.js) - KHÔNG dùng `===` cho floating point
- ⚠️ **Traps**: `{a:1} === {a:1}` = false, `0.1 + 0.2 !== 0.3`, Unicode variants

---

## 📦 PART 1: COMPARE OBJECTS

**Trả lời:**

- **Shallow Comparison**: So sánh references và primitive values ở level đầu tiên
- **Deep Comparison**: So sánh đệ quy tất cả nested properties, arrays, objects
- **Hoạt động**: Objects được so sánh bằng **reference** (địa chỉ bộ nhớ), không phải **value**
- **Ưu điểm**: Deep comparison chính xác với nested data; Shallow comparison nhanh, phù hợp React memo
- **Nhược điểm**: Deep comparison chậm O(n), có thể infinite loop với circular refs; Shallow comparison không phát hiện nested changes

**Code Example:**

```typescript
// Shallow comparison
const obj1 = { name: 'John', age: 25 };
const obj2 = { name: 'John', age: 25 };
const obj3 = obj1;

console.log(obj1 === obj2); // false (different references)
console.log(obj1 === obj3); // true (same reference)

// Deep comparison function
function deepEqual(obj1: any, obj2: any): boolean {
  if (obj1 === obj2) return true;

  if (obj1 == null || obj2 == null) return false;

  if (typeof obj1 !== typeof obj2) return false;

  if (typeof obj1 !== 'object') return obj1 === obj2;

  if (Array.isArray(obj1) !== Array.isArray(obj2)) return false;

  const keys1 = Object.keys(obj1);
  const keys2 = Object.keys(obj2);

  if (keys1.length !== keys2.length) return false;

  for (let key of keys1) {
    if (!keys2.includes(key)) return false;
    if (!deepEqual(obj1[key], obj2[key])) return false;
  }

  return true;
}

// Usage
const obj1 = { name: 'John', age: 25, address: { city: 'HCM' } };
const obj2 = { name: 'John', age: 25, address: { city: 'HCM' } };

console.log(deepEqual(obj1, obj2)); // true
```

**Best Practices - Objects:**

- ✅ Sử dụng **shallow comparison** cho React.memo, useMemo dependencies (performance)
- ✅ Sử dụng **deep comparison** khi cần so sánh nested objects chính xác
- ✅ Dùng **Lodash `_.isEqual()`** hoặc **fast-deep-equal** cho production (handle edge cases)
- ✅ Dùng **JSON.stringify()** chỉ khi objects đơn giản, không có functions/Date/RegExp
- ⚠️ **TRÁNH**: Deep comparison trong tight loops hoặc high-frequency updates
- ✅ Dùng **WeakMap** để cache comparison results nếu so sánh nhiều lần
- ✅ Sử dụng TypeScript cho type safety và autocomplete

---

## 📝 PART 2: COMPARE STRINGS

**Khái niệm:**

So sánh chuỗi cần xử lý đúng **Unicode, dấu thanh tiếng Việt, case sensitivity, và locale** để có kết quả chính xác.

**Các Vấn Đề Khi So Sánh Chuỗi:**

1. **Case Sensitivity** (Phân biệt hoa/thường): "Apple" ≠ "apple"
2. **Unicode Normalization** (Chuẩn hóa Unicode): "é" có thể là 1 char (`\u00e9`) hoặc 2 chars (`e` + `\u0301`)
3. **Diacritics/Accents** (Dấu thanh): Tiếng Việt "à", "á", "ả", "ã", "ạ" cần xử lý đúng
4. **Locale-specific** (Theo ngôn ngữ): Tiếng Việt "đ" khác "d", nhưng một số ngôn ngữ coi là giống nhau
5. **Whitespace** (Khoảng trắng): "  Hello  " vs "Hello"

**Kỹ thuật:**

- **Cơ bản**: `===`, `==`, `<`, `>` (so sánh theo Unicode code points - không phù hợp tiếng Việt)
- **Nâng cao**: `localeCompare()`, `Intl.Collator` (so sánh đúng theo ngôn ngữ, hỗ trợ dấu thanh)
- **Ưu điểm**: `Intl.Collator` tốt nhất cho sort, search tiếng Việt; performance cao khi so sánh nhiều lần
- **Nhược điểm**: `===` không xử lý được dấu thanh, accents; cần normalize() cho Unicode variants

**Code Example - Strings (TypeScript):**

```typescript
// ============================================
// 1. SO SÁNH CƠ BẢN (Basic Comparison)
// ============================================

// A. Equality (So sánh bằng)
const str1 = 'Hello';
const str2 = 'Hello';
const str3 = 'hello';

console.log(str1 === str2); // true - Giống nhau hoàn toàn
console.log(str1 === str3); // false - Khác case

// B. Case-insensitive comparison (Không phân biệt hoa/thường)
console.log(str1.toLowerCase() === str3.toLowerCase()); // true
console.log(str1.toUpperCase() === str3.toUpperCase()); // true

// C. Lexicographic comparison (So sánh từ điển - theo Unicode)
console.log('apple' < 'banana'); // true - 'a' (97) < 'b' (98)
console.log('Apple' < 'banana'); // true - 'A' (65) < 'b' (98)
console.log('10' < '2'); // true - ⚠️ So sánh string, không phải number!

// ============================================
// 2. VẤN ĐỀ VỚI TIẾNG VIỆT (Vietnamese Issues)
// ============================================

// ❌ SAI: So sánh trực tiếp không xử lý dấu thanh
const vn1 = 'Hà Nội';
const vn2 = 'Hải Phòng';
const vn3 = 'Huế';

console.log(vn1 < vn2); // false - ⚠️ 'à' (U+00E0) > 'ả' (U+1EA3) theo Unicode
console.log(vn2 < vn3); // false - ⚠️ Không đúng thứ tự alphabet tiếng Việt

// ❌ SAI: Unicode variants (Cùng ký tự nhưng khác Unicode)
const e1 = 'café'; // é = \u00e9 (1 character - precomposed)
const e2 = 'café'; // é = e + \u0301 (2 characters - decomposed)
console.log(e1 === e2); // false - ⚠️ Khác Unicode representation
console.log(e1.length); // 4
console.log(e2.length); // 5

// ✅ ĐÚNG: Normalize trước khi so sánh
console.log(e1.normalize('NFC') === e2.normalize('NFC')); // true
console.log(e1.normalize('NFD') === e2.normalize('NFD')); // true

// ============================================
// 3. localeCompare() - SO SÁNH THEO LOCALE
// ============================================

// Syntax: str1.localeCompare(str2, locale, options)
// Return: -1 (str1 < str2), 0 (equal), 1 (str1 > str2)

const city1 = 'Hà Nội';
const city2 = 'Hải Phòng';
const city3 = 'Huế';

// A. So sánh theo tiếng Việt (đúng thứ tự alphabet)
console.log(city1.localeCompare(city2, 'vi')); // -1 (Hà Nội < Hải Phòng)
console.log(city2.localeCompare(city3, 'vi')); // -1 (Hải Phòng < Huế)
console.log(city1.localeCompare(city1, 'vi')); // 0 (equal)

// B. Case-insensitive comparison với localeCompare
const name1 = 'Nguyễn Văn A';
const name2 = 'NGUYỄN VĂN A';

console.log(name1.localeCompare(name2, 'vi', { sensitivity: 'base' })); // 0 (equal - không phân biệt hoa/thường)
console.log(name1.localeCompare(name2, 'vi', { sensitivity: 'case' })); // -1 (khác case)

// C. Ignore accents (Bỏ qua dấu thanh)
const word1 = 'nha';
const word2 = 'nhà';

console.log(word1.localeCompare(word2, 'vi', { sensitivity: 'base' })); // 0 (coi là giống nhau)
console.log(word1.localeCompare(word2, 'vi', { sensitivity: 'accent' })); // -1 (khác dấu)

// D. Numeric comparison (So sánh số trong string)
const file1 = 'file2.txt';
const file2 = 'file10.txt';

console.log(file1 < file2); // false - ⚠️ String comparison: '2' > '1'
console.log(file1.localeCompare(file2, 'en', { numeric: true })); // -1 - ✅ 2 < 10

// ============================================
// 4. Intl.Collator - SO SÁNH HIỆU QUẢ (Reusable)
// ============================================

// Khi cần so sánh nhiều lần → tạo Collator instance (hiệu quả hơn)

// A. Tạo Collator cho tiếng Việt
const vietnameseCollator = new Intl.Collator('vi', {
  sensitivity: 'base', // Không phân biệt hoa/thường, dấu thanh
  numeric: true, // So sánh số đúng
  ignorePunctuation: true, // Bỏ qua dấu câu
});

const cities = ['Hà Nội', 'Đà Nẵng', 'Hồ Chí Minh', 'Cần Thơ', 'Huế'];

// Sort theo thứ tự tiếng Việt
const sortedCities = cities.sort((a, b) => vietnameseCollator.compare(a, b));
console.log(sortedCities);
// ✅ ['Cần Thơ', 'Đà Nẵng', 'Hà Nội', 'Hồ Chí Minh', 'Huế']

// B. Search/Filter với Collator
const names = ['Nguyễn Văn A', 'Nguyễn Văn B', 'Trần Thị C', 'NGUYỄN VĂN A'];
const searchTerm = 'nguyễn văn a';

const vietnameseSearchCollator = new Intl.Collator('vi', {
  sensitivity: 'base', // Không phân biệt hoa/thường, dấu thanh
});

const results = names.filter(
  (name) => vietnameseSearchCollator.compare(name, searchTerm) === 0
);
console.log(results); // ['Nguyễn Văn A', 'NGUYỄN VĂN A']

// ============================================
// 5. HELPER FUNCTIONS (Hàm Tiện Ích)
// ============================================

// A. Remove accents (Bỏ dấu tiếng Việt)
function removeAccents(str: string): string {
  return str
    .normalize('NFD') // Tách dấu ra
    .replace(/[\u0300-\u036f]/g, '') // Xóa dấu
    .replace(/đ/g, 'd')
    .replace(/Đ/g, 'D');
}

console.log(removeAccents('Hà Nội')); // 'Ha Noi'
console.log(removeAccents('Nguyễn Văn A')); // 'Nguyen Van A'

// B. Fuzzy search (Tìm gần đúng)
function fuzzyMatch(str: string, query: string): boolean {
  const normalizedStr = removeAccents(str.toLowerCase());
  const normalizedQuery = removeAccents(query.toLowerCase());
  
  return normalizedStr.includes(normalizedQuery);
}

console.log(fuzzyMatch('Cà phê Đà Lạt', 'ca phe')); // true
console.log(fuzzyMatch('Trà Sữa', 'tra sua')); // true
```

**Best Practices - Strings:**

- ✅ **Sử dụng `Intl.Collator` khi sort/compare nhiều lần** (performance tốt hơn `localeCompare`)
- ✅ **Luôn `normalize()` trước khi so sánh** nếu có Unicode variants
- ✅ **Chọn `sensitivity` phù hợp**: `base` (search), `accent` (phân biệt dấu), `case` (phân biệt hoa/thường), `variant` (strict)
- ✅ **Dùng `numeric: true`** khi sort file names, versions
- ✅ **Remove accents cho fuzzy search** (tìm kiếm gần đúng)

**📊 So Sánh Các Phương Pháp Strings:**

```
┌──────────────────────┬────────────────┬──────────────┬─────────────────┬──────────────┐
│ Phương Pháp          │ Performance    │ Tiếng Việt   │ Case/Accent     │ Use Case     │
├──────────────────────┼────────────────┼──────────────┼─────────────────┼──────────────┤
│ === / < / >          │ ⚡⚡⚡⚡⚡       │ ❌           │ Phân biệt       │ ASCII only   │
│ toLowerCase() + ===  │ ⚡⚡⚡⚡         │ ❌           │ Không phân biệt │ Simple       │
│ localeCompare()      │ ⚡⚡⚡          │ ✅           │ Tùy chỉnh       │ 1-2 lần      │
│ Intl.Collator        │ ⚡⚡⚡⚡⚡       │ ✅           │ Tùy chỉnh       │ Sort, nhiều  │
│ normalize() + ===    │ ⚡⚡⚡⚡         │ Partial      │ Tùy chỉnh       │ Unicode fix  │
└──────────────────────┴────────────────┴──────────────┴─────────────────┴──────────────┘
```

---

## 💰 PART 3: COMPARE BIG NUMBERS & DECIMALS

**Vấn Đề Floating Point Precision:**

```typescript
// ❌ VẤN ĐỀ: JavaScript numbers là IEEE 754 floating-point
console.log(0.1 + 0.2); // 0.30000000000000004 ❌
console.log(0.1 + 0.2 === 0.3); // false ❌

// Vấn đề với số lớn (> Number.MAX_SAFE_INTEGER)
const bigNum = 9007199254740992; // 2^53
console.log(bigNum + 1 === bigNum + 2); // true ❌ (mất precision!)

// Vấn đề với tiền tệ/financial calculations
const price = 0.07;
const quantity = 100;
console.log(price * quantity); // 7.000000000000001 ❌
```

**Giải Pháp:**

### 3.1. So Sánh Decimals với Epsilon (Ngưỡng Sai Số)

```typescript
// ✅ CÁCH 1: Epsilon comparison (cho số nhỏ)
function areEqual(a: number, b: number, epsilon = Number.EPSILON): boolean {
  return Math.abs(a - b) < epsilon;
}

console.log(areEqual(0.1 + 0.2, 0.3)); // true ✅
console.log(areEqual(0.07 * 100, 7)); // true ✅

// Epsilon lớn hơn cho financial calculations
const FINANCIAL_EPSILON = 0.0001; // 4 decimal places

function areFinanciallyEqual(a: number, b: number): boolean {
  return Math.abs(a - b) < FINANCIAL_EPSILON;
}

console.log(areFinanciallyEqual(99.9999, 100.0001)); // true
console.log(areFinanciallyEqual(99.99, 100.01)); // false

// ✅ CÁCH 2: So sánh bằng toFixed() (convert to string)
function compareDecimals(a: number, b: number, decimals = 2): boolean {
  return a.toFixed(decimals) === b.toFixed(decimals);
}

console.log(compareDecimals(0.1 + 0.2, 0.3, 10)); // true
console.log(compareDecimals(99.999, 100.001, 2)); // true (cả 2 → "100.00")

// ✅ CÁCH 3: Chuyển sang cents/smallest unit (cho tiền tệ)
function compareMoney(a: number, b: number): boolean {
  // Convert to cents (multiply by 100)
  return Math.round(a * 100) === Math.round(b * 100);
}

console.log(compareMoney(0.07 * 100, 7)); // true
console.log(compareMoney(19.99, 20.00)); // false
```

### 3.2. So Sánh Big Numbers với Libraries

```typescript
// ============================================
// LIBRARY 1: decimal.js (Khuyến nghị cho financial)
// ============================================
import Decimal from 'decimal.js';

// A. Basic comparison
const a = new Decimal('0.1');
const b = new Decimal('0.2');
const c = new Decimal('0.3');

console.log(a.plus(b).equals(c)); // true ✅

// B. Big numbers (> Number.MAX_SAFE_INTEGER)
const big1 = new Decimal('9007199254740993');
const big2 = new Decimal('9007199254740994');

console.log(big1.lessThan(big2)); // true ✅
console.log(big1.greaterThan(big2)); // false
console.log(big1.equals(big2)); // false

// C. Financial calculations
const price = new Decimal('19.99');
const quantity = new Decimal('100');
const total = price.times(quantity);

console.log(total.toString()); // "1999.00"
console.log(total.equals(new Decimal('1999'))); // true ✅

// D. Comparison operators
const x = new Decimal('123.456');
const y = new Decimal('123.457');

console.log(x.comparedTo(y)); // -1 (x < y)
console.log(y.comparedTo(x)); // 1 (y > x)
console.log(x.comparedTo(x)); // 0 (x === x)

// E. Precision control
Decimal.set({ precision: 10 }); // 10 significant digits

const result = new Decimal('1').dividedBy('3');
console.log(result.toString()); // "0.3333333333"

// ============================================
// LIBRARY 2: big.js (Nhẹ hơn, đơn giản hơn)
// ============================================
import Big from 'big.js';

const num1 = new Big('0.1');
const num2 = new Big('0.2');
const num3 = new Big('0.3');

console.log(num1.plus(num2).eq(num3)); // true ✅

// Comparison methods
console.log(num1.lt(num2)); // true (less than)
console.log(num1.lte(num2)); // true (less than or equal)
console.log(num1.gt(num2)); // false (greater than)
console.log(num1.gte(num2)); // false (greater than or equal)
console.log(num1.eq(num2)); // false (equal)

// ============================================
// LIBRARY 3: bignumber.js (Nhiều features nhất)
// ============================================
import BigNumber from 'bignumber.js';

const bn1 = new BigNumber('12345678901234567890');
const bn2 = new BigNumber('12345678901234567891');

console.log(bn1.isEqualTo(bn2)); // false
console.log(bn1.isLessThan(bn2)); // true
console.log(bn1.isGreaterThan(bn2)); // false

// Comparison với tolerance
console.log(bn1.comparedTo(bn2)); // -1

// Crypto/Blockchain calculations
const wei = new BigNumber('1000000000000000000'); // 1 ETH in wei
const gwei = wei.dividedBy('1000000000');
console.log(gwei.toString()); // "1000000000"
```

### 3.3. Helper Functions cho Big Number Comparison

```typescript
// ============================================
// HELPER FUNCTIONS
// ============================================

// 1. Compare với epsilon (built-in Number)
function compareNumbers(
  a: number,
  b: number,
  options: {
    epsilon?: number;
    decimals?: number;
  } = {}
): -1 | 0 | 1 {
  const { epsilon = Number.EPSILON, decimals } = options;

  // Option 1: Use epsilon
  if (!decimals) {
    const diff = a - b;
    if (Math.abs(diff) < epsilon) return 0;
    return diff < 0 ? -1 : 1;
  }

  // Option 2: Use toFixed
  const aFixed = a.toFixed(decimals);
  const bFixed = b.toFixed(decimals);
  
  if (aFixed === bFixed) return 0;
  return aFixed < bFixed ? -1 : 1;
}

console.log(compareNumbers(0.1 + 0.2, 0.3)); // 0 (equal)
console.log(compareNumbers(99.999, 100.001, { decimals: 2 })); // 0 (equal)
console.log(compareNumbers(1.5, 2.5)); // -1 (less than)

// 2. Safe comparison cho financial
interface Money {
  amount: number;
  currency: string;
}

function compareMoney(a: Money, b: Money): -1 | 0 | 1 {
  if (a.currency !== b.currency) {
    throw new Error('Cannot compare different currencies');
  }

  // Convert to smallest unit (cents)
  const aCents = Math.round(a.amount * 100);
  const bCents = Math.round(b.amount * 100);

  if (aCents === bCents) return 0;
  return aCents < bCents ? -1 : 1;
}

const price1: Money = { amount: 19.99, currency: 'USD' };
const price2: Money = { amount: 20.00, currency: 'USD' };

console.log(compareMoney(price1, price2)); // -1 (cheaper)

// 3. Compare arrays of numbers
function compareNumberArrays(
  a: number[],
  b: number[],
  epsilon = Number.EPSILON
): boolean {
  if (a.length !== b.length) return false;
  
  return a.every((val, index) => Math.abs(val - b[index]) < epsilon);
}

console.log(compareNumberArrays([0.1, 0.2], [0.1, 0.2])); // true
console.log(compareNumberArrays([0.1 + 0.2], [0.3])); // true ✅

// 4. Range comparison (a trong khoảng [min, max])
function isInRange(
  value: number,
  min: number,
  max: number,
  inclusive = true
): boolean {
  if (inclusive) {
    return value >= min && value <= max;
  }
  return value > min && value < max;
}

console.log(isInRange(5, 1, 10)); // true
console.log(isInRange(10, 1, 10, false)); // false (exclusive)
```

### 3.4. Real-World Examples

```typescript
// ============================================
// EXAMPLE 1: E-commerce Price Comparison
// ============================================
import Decimal from 'decimal.js';

interface Product {
  id: string;
  name: string;
  price: Decimal;
}

function findCheapest(products: Product[]): Product {
  return products.reduce((cheapest, current) =>
    current.price.lessThan(cheapest.price) ? current : cheapest
  );
}

const products: Product[] = [
  { id: '1', name: 'A', price: new Decimal('19.99') },
  { id: '2', name: 'B', price: new Decimal('19.989') }, // Cheaper by 0.001
  { id: '3', name: 'C', price: new Decimal('20.00') },
];

console.log(findCheapest(products)); // Product B

// ============================================
// EXAMPLE 2: Crypto Trading (High Precision)
// ============================================
import BigNumber from 'bignumber.js';

interface Trade {
  price: BigNumber;
  amount: BigNumber;
}

function calculateTotal(trades: Trade[]): BigNumber {
  return trades.reduce(
    (total, trade) => total.plus(trade.price.times(trade.amount)),
    new BigNumber(0)
  );
}

const trades: Trade[] = [
  { 
    price: new BigNumber('50000.123456789'), // BTC price
    amount: new BigNumber('0.00123456') 
  },
  {
    price: new BigNumber('50000.987654321'),
    amount: new BigNumber('0.00234567')
  },
];

const total = calculateTotal(trades);
console.log(total.toFixed(8)); // "178.93831959" (8 decimals)

// ============================================
// EXAMPLE 3: Percentage Comparison (Tax, Discount)
// ============================================
import Decimal from 'decimal.js';

function applyDiscount(
  price: Decimal,
  discountPercent: Decimal
): Decimal {
  const discount = price.times(discountPercent).dividedBy(100);
  return price.minus(discount);
}

const originalPrice = new Decimal('100.00');
const discount = new Decimal('10.5'); // 10.5%

const finalPrice = applyDiscount(originalPrice, discount);
console.log(finalPrice.toString()); // "89.50"

// Verify discount calculation
const expectedPrice = new Decimal('89.50');
console.log(finalPrice.equals(expectedPrice)); // true ✅

// ============================================
// EXAMPLE 4: Scientific Calculations
// ============================================
import Decimal from 'decimal.js';

// Configure for scientific precision
Decimal.set({ precision: 50 });

const pi = new Decimal('3.1415926535897932384626433832795028841971693993751');
const radius = new Decimal('10');

const area = pi.times(radius.pow(2));
console.log(area.toString()); // Very high precision

// Compare with tolerance
function compareScientific(
  a: Decimal,
  b: Decimal,
  significantDigits: number
): boolean {
  return a.toSignificantDigits(significantDigits)
    .equals(b.toSignificantDigits(significantDigits));
}

const result1 = new Decimal('3.14159265358979');
const result2 = new Decimal('3.14159265358980');

console.log(compareScientific(result1, result2, 10)); // true (first 10 digits match)
```

**Best Practices - Big Numbers & Decimals:**

- ✅ **KHÔNG BAO GIỜ dùng `===` cho floating point** - dùng epsilon hoặc libraries
- ✅ **Financial calculations**: Dùng `decimal.js` hoặc chuyển sang cents (smallest unit)
- ✅ **Crypto/Blockchain**: Dùng `bignumber.js` với precision cao (>18 decimals)
- ✅ **E-commerce**: Dùng `big.js` (nhẹ, đủ features) hoặc store prices as cents (integer)
- ✅ **Scientific**: Dùng `decimal.js` với custom precision
- ⚠️ **TRÁNH**: `toFixed()` cho calculations (chỉ dùng cho display)
- ✅ **Always validate currency** trước khi so sánh Money objects
- ✅ **Document precision requirements** trong code comments

**📊 So Sánh Libraries:**

```
┌──────────────────┬─────────────┬─────────────┬──────────────┬─────────────────┐
│ Library          │ Size        │ Precision   │ Performance  │ Use Case        │
├──────────────────┼─────────────┼─────────────┼──────────────┼─────────────────┤
│ decimal.js       │ ~32KB       │ Unlimited   │ ⚡⚡⚡        │ Financial       │
│ big.js           │ ~6KB        │ Unlimited   │ ⚡⚡⚡⚡      │ E-commerce      │
│ bignumber.js     │ ~23KB       │ Unlimited   │ ⚡⚡⚡        │ Crypto/Science  │
│ Native (epsilon) │ 0KB         │ Limited     │ ⚡⚡⚡⚡⚡    │ Simple cases    │
└──────────────────┴─────────────┴─────────────┴──────────────┴─────────────────┘
```

**Common Mistakes - Big Numbers:**

```typescript
// ❌ LỖI 1: So sánh trực tiếp floating point
const bad1 = (0.1 + 0.2 === 0.3); // false ❌

// ✅ ĐÚNG: Dùng epsilon
const good1 = Math.abs((0.1 + 0.2) - 0.3) < Number.EPSILON; // true ✅

// ❌ LỖI 2: Dùng toFixed() cho calculations
const bad2 = parseFloat((0.1 + 0.2).toFixed(1)); // 0.3 nhưng không chính xác

// ✅ ĐÚNG: Dùng Decimal cho calculations, toFixed() chỉ cho display
const good2 = new Decimal('0.1').plus('0.2').toFixed(1); // "0.3"

// ❌ LỖI 3: Quên validate currency
const bad3 = compareMoney(
  { amount: 100, currency: 'USD' },
  { amount: 100, currency: 'EUR' }
); // ❌ Comparing different currencies!

// ✅ ĐÚNG: Validate trước
function safeCom pareMoney(a: Money, b: Money) {
  if (a.currency !== b.currency) throw new Error('Currency mismatch');
  return compareMoney(a, b);
}
```

---

## ✅ TỔNG KẾT

**Khi nào dùng gì?**

| Loại So Sánh | Phương Pháp | Use Case |
|---------------|-------------|----------|
| **Objects - Shallow** | `Object.is()`, `===` | React.memo, primitive checks |
| **Objects - Deep** | Lodash `_.isEqual()`, custom recursive | Form validation, API response comparison |
| **Strings - ASCII** | `===`, `toLowerCase()` | Simple text, English only |
| **Strings - Unicode/Tiếng Việt** | `Intl.Collator`, `localeCompare()` | Sort names, search, i18n |
| **Decimals - Simple** | Epsilon comparison | Basic math, UI calculations |
| **Decimals - Financial** | `decimal.js`, cents conversion | E-commerce, billing, accounting |
| **Big Numbers** | `bignumber.js` | Crypto, scientific, blockchain |

