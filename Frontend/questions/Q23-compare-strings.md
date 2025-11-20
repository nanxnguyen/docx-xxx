# 📝 Q23: Compare Strings




**⚡ Quick Summary:**
> Compare strings: `===`, `localeCompare()` (i18n), ignore case với toLowerCase()

**💡 Ghi Nhớ:**
- 🎯 **Exact**: `str1 === str2`
- 🌍 **Locale**: `str1.localeCompare(str2)` - dùng cho sorting
- 🔤 **Case-insensitive**: `str1.toLowerCase() === str2.toLowerCase()`

**Trả lời:**

- **Khái niệm**: So sánh chuỗi cần xử lý đúng **Unicode, dấu thanh tiếng Việt, case sensitivity, và locale** để có kết quả chính xác
- **Kỹ thuật cơ bản**: `===`, `==`, `<`, `>` (so sánh theo Unicode code points - không phù hợp tiếng Việt)
- **Kỹ thuật nâng cao**: `localeCompare()`, `Intl.Collator` (so sánh đúng theo ngôn ngữ, hỗ trợ dấu thanh)
- **Ưu điểm**: `Intl.Collator` tốt nhất cho sort, search tiếng Việt; performance cao khi so sánh nhiều lần
- **Nhược điểm**: `===` không xử lý được dấu thanh, accents; cần normalize() cho Unicode variants

**Các Vấn Đề Khi So Sánh Chuỗi:**

1. **Case Sensitivity** (Phân biệt hoa/thường): "Apple" ≠ "apple"
2. **Unicode Normalization** (Chuẩn hóa Unicode): "é" có thể là 1 char (`\u00e9`) hoặc 2 chars (`e` + `\u0301`)
3. **Diacritics/Accents** (Dấu thanh): Tiếng Việt "à", "á", "ả", "ã", "ạ" cần xử lý đúng
4. **Locale-specific** (Theo ngôn ngữ): Tiếng Việt "đ" khác "d", nhưng một số ngôn ngữ coi là giống nhau
5. **Whitespace** (Khoảng trắng): "  Hello  " vs "Hello"

**Code Example (TypeScript):**

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

// B. Collator với options khác nhau
const caseSensitiveCollator = new Intl.Collator('vi', {
  sensitivity: 'case', // Phân biệt hoa/thường
});

console.log(caseSensitiveCollator.compare('Việt Nam', 'việt nam')); // -1 (khác case)

const accentSensitiveCollator = new Intl.Collator('vi', {
  sensitivity: 'accent', // Phân biệt dấu thanh
});

console.log(accentSensitiveCollator.compare('nha', 'nhà')); // -1 (khác dấu)

// C. Search/Filter với Collator
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
// 5. PRACTICAL EXAMPLES (Ví Dụ Thực Tế)
// ============================================

// A. Tìm kiếm sản phẩm (không phân biệt dấu, hoa/thường)
interface Product {
  id: number;
  name: string;
}

const products: Product[] = [
  { id: 1, name: 'Cà phê Đà Lạt' },
  { id: 2, name: 'Trà Ô Long' },
  { id: 3, name: 'Cà phê Sữa' },
  { id: 4, name: 'Trà Sữa Trân Châu' },
];

function searchProducts(query: string): Product[] {
  const normalizedQuery = query.normalize('NFD').toLowerCase();
  
  return products.filter((product) => {
    const normalizedName = product.name.normalize('NFD').toLowerCase();
    return normalizedName.includes(normalizedQuery);
  });
}

console.log(searchProducts('ca phe')); 
// ✅ [{ id: 1, name: 'Cà phê Đà Lạt' }, { id: 3, name: 'Cà phê Sữa' }]

console.log(searchProducts('tra')); 
// ✅ [{ id: 2, name: 'Trà Ô Long' }, { id: 4, name: 'Trà Sữa Trân Châu' }]

// B. Sort danh sách tên tiếng Việt
const students = [
  'Nguyễn Văn A',
  'Trần Thị B',
  'Lê Hoàng C',
  'Đặng Minh D',
  'Phạm Thu E',
];

const collator = new Intl.Collator('vi');
const sortedStudents = students.sort((a, b) => collator.compare(a, b));
console.log(sortedStudents);
// ✅ ['Đặng Minh D', 'Lê Hoàng C', 'Nguyễn Văn A', 'Phạm Thu E', 'Trần Thị B']

// C. Validate duplicate names (tránh trùng lặp)
function hasDuplicateName(names: string[], newName: string): boolean {
  const collator = new Intl.Collator('vi', { sensitivity: 'base' });
  
  return names.some((name) => collator.compare(name, newName) === 0);
}

const existingNames = ['Nguyễn Văn A', 'Trần Thị B'];

console.log(hasDuplicateName(existingNames, 'NGUYỄN VĂN A')); // true - trùng (không phân biệt hoa/thường)
console.log(hasDuplicateName(existingNames, 'Lê Văn C')); // false - không trùng

// D. Compare versions/file names với số
const versions = ['v1.2.10', 'v1.2.2', 'v1.10.0', 'v1.2.1'];

const numericCollator = new Intl.Collator('en', { numeric: true });
const sortedVersions = versions.sort((a, b) => numericCollator.compare(a, b));
console.log(sortedVersions);
// ✅ ['v1.2.1', 'v1.2.2', 'v1.2.10', 'v1.10.0'] - đúng thứ tự số

// ============================================
// 6. PERFORMANCE COMPARISON
// ============================================

// Benchmark: So sánh 10,000 lần
const testData = Array.from({ length: 10000 }, (_, i) => `Nguyễn ${i}`);

// Method 1: localeCompare (chậm khi gọi nhiều lần)
console.time('localeCompare');
testData.sort((a, b) => a.localeCompare(b, 'vi'));
console.timeEnd('localeCompare'); // ~50-100ms

// Method 2: Intl.Collator (nhanh hơn nhiều)
console.time('Intl.Collator');
const collatorBenchmark = new Intl.Collator('vi');
testData.sort((a, b) => collatorBenchmark.compare(a, b));
console.timeEnd('Intl.Collator'); // ~10-20ms - ⚡ Nhanh gấp 5x

// ============================================
// 7. HELPER FUNCTIONS (Hàm Tiện Ích)
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

// C. Compare with options
function compareStrings(
  str1: string,
  str2: string,
  options: {
    caseSensitive?: boolean;
    accentSensitive?: boolean;
    locale?: string;
  } = {}
): number {
  const {
    caseSensitive = false,
    accentSensitive = false,
    locale = 'vi',
  } = options;

  let sensitivity: 'base' | 'accent' | 'case' | 'variant' = 'base';
  
  if (caseSensitive && accentSensitive) {
    sensitivity = 'variant'; // Phân biệt tất cả
  } else if (accentSensitive) {
    sensitivity = 'accent'; // Chỉ phân biệt dấu
  } else if (caseSensitive) {
    sensitivity = 'case'; // Chỉ phân biệt hoa/thường
  }

  return str1.localeCompare(str2, locale, { sensitivity });
}

console.log(compareStrings('Hà Nội', 'Hà Nội')); // 0 (equal)
console.log(compareStrings('Hà Nội', 'HA NOI')); // 0 (không phân biệt case)
console.log(compareStrings('Hà Nội', 'HA NOI', { caseSensitive: true })); // -1 (khác case)
```

**Best Practices (Thực Hành Tốt):**

1. **✅ Sử dụng `Intl.Collator` khi sort/compare nhiều lần** (performance tốt hơn `localeCompare`)
2. **✅ Luôn `normalize()` trước khi so sánh** nếu có Unicode variants
3. **✅ Chọn `sensitivity` phù hợp**:
   - `base`: Không phân biệt case, accent (search)
   - `accent`: Phân biệt accent, không phân biệt case
   - `case`: Phân biệt case, không phân biệt accent
   - `variant`: Phân biệt tất cả (strict)
4. **✅ Dùng `numeric: true`** khi sort file names, versions
5. **✅ Remove accents cho fuzzy search** (tìm kiếm gần đúng)

**Common Mistakes (Lỗi Thường Gặp):**

```typescript
// ❌ LỖI 1: So sánh trực tiếp tiếng Việt
const bad1 = 'Hà Nội' < 'Huế'; // ❌ Sai thứ tự

// ✅ ĐÚNG: Dùng localeCompare
const good1 = 'Hà Nội'.localeCompare('Huế', 'vi') < 0; // ✅ true

// ❌ LỖI 2: Không normalize Unicode
const bad2 = 'café' === 'café'; // ❌ Có thể false nếu khác Unicode

// ✅ ĐÚNG: Normalize trước
const good2 = 'café'.normalize('NFC') === 'café'.normalize('NFC'); // ✅ true

// ❌ LỖI 3: Dùng toLowerCase() cho tiếng Việt
const bad3 = 'NGUYỄN'.toLowerCase() === 'nguyễn'; // ✅ true (OK)
const bad4 = 'İstanbul'.toLowerCase() === 'istanbul'; // ❌ false (Turkish)

// ✅ ĐÚNG: Dùng toLocaleLowerCase() với locale
const good3 = 'İstanbul'.toLocaleLowerCase('tr') === 'istanbul'; // ✅ true

// ❌ LỖI 4: localeCompare trong loop lớn
const badArray = bigArray.sort((a, b) => a.localeCompare(b, 'vi')); // ❌ Chậm

// ✅ ĐÚNG: Tạo Collator trước
const collator = new Intl.Collator('vi');
const goodArray = bigArray.sort((a, b) => collator.compare(a, b)); // ✅ Nhanh hơn
```

**📊 So Sánh Các Phương Pháp:**

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

**✅ Tổng Kết:**

- **So sánh ASCII**: Dùng `===`, `<`, `>`
- **So sánh tiếng Việt (1-2 lần)**: Dùng `localeCompare()`
- **Sort/Search tiếng Việt (nhiều lần)**: Dùng `Intl.Collator`
- **Unicode variants**: Dùng `normalize('NFC')` hoặc `normalize('NFD')`
- **Fuzzy search**: Remove accents với `normalize('NFD')` + regex

