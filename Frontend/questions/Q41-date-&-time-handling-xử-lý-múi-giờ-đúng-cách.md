# ⏰ Q41: Date & Time Handling - Xử Lý Múi Giờ Đúng Cách

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"Dùng Timestamps (Unix milliseconds) hoặc ISO 8601 UTC cho storage/transmission, convert sang local timezone chỉ khi display. Libraries: date-fns, dayjs, Luxon."**

**🔑 Best Practices:**

**1. Storage & Transmission - Luôn UTC:**

- **Timestamp** (Unix ms): `Date.now()` = 1705329000000 - absolute time point
- **ISO 8601 UTC**: `new Date().toISOString()` = "2024-01-15T14:30:00.000Z"
- Database lưu TIMESTAMP hoặc DATETIME UTC
- API truyền ISO 8601 với 'Z' suffix (UTC)

**2. Display - Convert to Local:**

- `new Date(timestamp).toLocaleString('vi-VN', {timeZone: 'Asia/Ho_Chi_Minh'})`
- `Intl.DateTimeFormat` cho i18n formatting
- Show timezone explicitly: "15/01/2024 21:30 ICT"

**3. Avoid Native Date Pitfalls:**

- ❌ `new Date('2024-01-15')` → depends on browser timezone
- ❌ Months zero-indexed: `new Date(2024, 1, 15)` = Feb 15
- ❌ Mutable: `date.setMonth()` modifies original
- ✅ Use libraries: **date-fns** (functional, tree-shakable), **dayjs** (lightweight), **Luxon** (immutable, timezone-aware)

**4. Common Scenarios:**

- **User selects date**: Convert local → UTC before send server
- **Display server date**: Parse UTC → convert local timezone
- **Scheduling**: Store UTC + user's timezone separately
- **Recurring events**: Calculate in user's timezone (handle DST)

**⚠️ Lỗi Thường Gặp:**

- Lưu date string "DD/MM/YYYY" → parsing issues, dùng ISO 8601
- Compare dates không normalize timezone → sai kết quả
- Quên Daylight Saving Time (DST) → sai 1 giờ 2 lần/năm
- Dùng `Date()` constructor với string → browser-dependent parsing

**💡 Kiến Thức Senior:**

- **IANA timezone database**: "Asia/Ho_Chi_Minh", không dùng "GMT+7" (không handle DST)
- **ISO 8601 formats**: `2024-01-15T14:30:00Z` (UTC) vs `2024-01-15T14:30:00+07:00` (offset)
- **Temporal API** (TC39 Stage 3): Future replacement for Date - `Temporal.ZonedDateTime`
- **UTC Offset vs Timezone**: Offset = static (+7), Timezone = rules (handle DST, history)

**❓ Câu Hỏi:**
Làm thế nào xử lý Date/Time trong JavaScript không bị ảnh hưởng bởi múi giờ?

#### **⚠️ Vấn Đề Core**

```typescript
// ❌ VẤN ĐỀ: Timezone-dependent
const date = new Date('2024-01-15'); // Local timezone!
// User Vietnam (UTC+7): 2024-01-15 07:00:00 UTC
// User US (UTC-5):      2024-01-15 05:00:00 UTC
// → Cùng code, khác kết quả!

// ❌ VẤN ĐỀ: Month zero-indexed
new Date(2024, 1, 15); // February 15! (month 1 = Feb)

// ❌ VẤN ĐỀ: Mutable
date.setMonth(2); // Thay đổi date gốc!
```

---

#### **💡 Timestamp - Tại Sao Không Bị Ảnh Hưởng Timezone?**

**Timestamp = Số milliseconds từ 1970-01-01 00:00:00 UTC (Unix Epoch)**

```typescript
// =====================================
// TIMESTAMP LÀ MỘT CON SỐ TUYỆT ĐỐI
// =====================================

// Ví dụ: 2024-01-15 14:30:00 UTC
const timestamp = 1705329000000; // milliseconds

// ✅ Timestamp đại diện cho 1 ĐIỂM THỜI GIAN DUY NHẤT trên toàn cầu
// - Không phụ thuộc múi giờ
// - Không phụ thuộc vị trí địa lý
// - Chỉ là 1 con số: số milli-giây từ 1970-01-01 00:00:00 UTC

// GIẢI THÍCH:
// ┌─────────────────────────────────────────────────────────┐
// │  Timestamp 1705329000000 = "2024-01-15 14:30:00 UTC"   │
// │                                                         │
// │  Cùng 1 timestamp, DISPLAY khác múi giờ:               │
// │  - Vietnam (UTC+7):  2024-01-15 21:30:00               │
// │  - New York (UTC-5): 2024-01-15 09:30:00               │
// │  - London (UTC+0):   2024-01-15 14:30:00               │
// │                                                         │
// │  Nhưng timestamp VẪN LÀ 1705329000000                  │
// │  → Cùng 1 điểm thời gian, chỉ HIỂN THỊ khác!           │
// └─────────────────────────────────────────────────────────┘
```

**So Sánh Trực Quan:**

```typescript
// =====================================
// VÍ DỤ THỰC TẾ
// =====================================

// Server gửi timestamp
const serverTimestamp = 1705329000000; // 2024-01-15 14:30:00 UTC

// User ở Vietnam nhận được
const vnDate = new Date(serverTimestamp);
console.log(vnDate.toString());
// "Mon Jan 15 2024 21:30:00 GMT+0700 (Indochina Time)"
// ✅ Display: 21:30:00 (UTC+7)
// ✅ Timestamp: 1705329000000

// User ở US nhận được
const usDate = new Date(serverTimestamp);
console.log(usDate.toString());
// "Mon Jan 15 2024 09:30:00 GMT-0500 (Eastern Standard Time)"
// ✅ Display: 09:30:00 (UTC-5)
// ✅ Timestamp: 1705329000000

// So sánh timestamps
console.log(vnDate.getTime() === usDate.getTime()); // ✅ TRUE!
console.log(vnDate.getTime()); // 1705329000000
console.log(usDate.getTime()); // 1705329000000

// =====================================
// TẠI SAO TIMESTAMP KHÔNG BỊ ẢNH HƯỞNG?
// =====================================

// 1. Timestamp là CON SỐ, không phải string hay object
const ts = 1705329000000; // Chỉ là 1 số nguyên

// 2. Timestamp luôn tính từ UTC EPOCH (1970-01-01 00:00:00 UTC)
// → Chuẩn quốc tế, không đổi

// 3. Khi convert timestamp → Date, browser tự động hiển thị theo local timezone
// Nhưng INTERNAL VALUE vẫn là timestamp (không đổi)
const date = new Date(1705329000000);
date.getTime(); // 1705329000000 (giống nhau mọi nơi)
date.toString(); // Khác nhau theo timezone (chỉ là display)

// =====================================
// MINH HỌA BẰ NG SỐ
// =====================================

// Giả sử có 3 user ở 3 múi giờ khác nhau cùng click "Submit" 1 lúc

// User Vietnam (UTC+7) - Hiển thị: 2024-01-15 21:30:00
const vnTimestamp = new Date('2024-01-15T21:30:00+07:00').getTime();
console.log(vnTimestamp); // 1705329000000

// User US (UTC-5) - Hiển thị: 2024-01-15 09:30:00
const usTimestamp = new Date('2024-01-15T09:30:00-05:00').getTime();
console.log(usTimestamp); // 1705329000000

// User UK (UTC+0) - Hiển thị: 2024-01-15 14:30:00
const ukTimestamp = new Date('2024-01-15T14:30:00Z').getTime();
console.log(ukTimestamp); // 1705329000000

// ✅ CÙNG 1 TIMESTAMP = CÙNG 1 THỜI ĐIỂM
// → Lưu vào database: 1705329000000
// → Compare: So sánh 1 số duy nhất
// → Không bị sai lệch múi giờ
```

**Kết Luận:**

```typescript
// =====================================
// TIMESTAMP = UNIVERSAL TIME REFERENCE
// =====================================

// ✅ Timestamp là "ngôn ngữ chung" của thời gian
// - Mọi timezone đều convert về 1 số duy nhất
// - Database lưu 1 giá trị, không phụ thuộc múi giờ
// - API truyền 1 số, không bị nhầm lẫn
// - So sánh đơn giản: a > b, a === b

// ❌ String date BỊ ẢNH HƯỞNG timezone
'2024-01-15'; // Ambiguous! 00:00 múi giờ nào?
'2024-01-15 14:30'; // Múi giờ nào?

// ✅ Timestamp KHÔNG BỊ ẢNH HƯỞNG
1705329000000; // LUÔN LÀ 2024-01-15 14:30:00 UTC
// Display tùy timezone, nhưng VALUE không đổi
```

---

#### **💡 Nguyên Tắc Vàng**

```
┌────────────────────────────────────────┐
│   STORAGE:  UTC/Timestamp             │
│   TRANSMIT: ISO 8601 + timezone       │
│   DISPLAY:  User local timezone       │
│   COMPUTE:  UTC/Timestamp             │
└────────────────────────────────────────┘
```

---

#### **✅ Giải Pháp Đúng**

**1. Store UTC (Lưu UTC vào Database/API):**

```typescript
// ===================================================
// ✅ Database/API: Luôn lưu UTC
// ===================================================

// Cách 1: Lưu Timestamp (số milliseconds)
await db.save({
  createdAt: Date.now(), // 💡 1705329000000 (timestamp)
  // ✅ Ưu điểm: Số nguyên, dễ so sánh, không phụ thuộc timezone
  // ✅ Database: Lưu kiểu BIGINT hoặc NUMBER
});

// Cách 2: Lưu ISO 8601 UTC string
await db.save({
  createdAt: new Date().toISOString(),
  // 💡 "2024-01-15T14:30:00.000Z"
  // ✅ Ưu điểm: Human-readable, có timezone info (Z = UTC)
  // ✅ Database: Lưu kiểu VARCHAR hoặc TIMESTAMP
});

// ===================================================
// ✅ Parse ISO 8601 từ API (tự động UTC với Z)
// ===================================================
const date = new Date('2024-01-15T14:30:00.000Z');
// 💡 'Z' suffix = UTC (Zulu time)
// 💡 Browser tự động parse thành UTC
// ✅ getTime() = 1705329000000 (timestamp)
// ✅ toISOString() = "2024-01-15T14:30:00.000Z" (giữ nguyên)
```

**2. Display Local (Hiển Thị Theo Múi Giờ Người Dùng):**

```typescript
// ===================================================
// ✅ Convert UTC → User's local timezone để hiển thị
// ===================================================

// Cách 1: Dùng Intl.DateTimeFormat (Built-in, không cần library)
const formatter = new Intl.DateTimeFormat('en-US', {
  timeZone: 'Asia/Ho_Chi_Minh', // 💡 Múi giờ Vietnam (UTC+7)
  dateStyle: 'long', // 💡 "January 15, 2024"
  timeStyle: 'short', // 💡 "9:30 PM"
});
console.log(formatter.format(date));
// 💡 Input: "2024-01-15T14:30:00.000Z" (UTC)
// 💡 Output: "January 15, 2024 at 9:30 PM" (Vietnam time)
// ✅ 14:30 UTC + 7 giờ = 21:30 Vietnam

// Cách 2: Dùng toLocaleString() (Đơn giản hơn)
const vnTime = date.toLocaleString('vi-VN', {
  timeZone: 'Asia/Ho_Chi_Minh',
  dateStyle: 'long',
  timeStyle: 'short',
});
console.log(vnTime);
// 💡 "15 tháng 1, 2024 lúc 21:30" (tiếng Việt)

// Cách 3: Custom format với Intl.DateTimeFormat
const customFormatter = new Intl.DateTimeFormat('vi-VN', {
  timeZone: 'Asia/Ho_Chi_Minh',
  year: 'numeric',
  month: '2-digit',
  day: '2-digit',
  hour: '2-digit',
  minute: '2-digit',
  hour12: false, // 💡 24h format (21:30 thay vì 9:30 PM)
});
console.log(customFormatter.format(date));
// 💡 "15/01/2024, 21:30"
```

**3. Compare Timestamps (So Sánh Thời Gian):**

````typescript
// ===================================================
// ✅ So sánh bằng Timestamp - KHÔNG bị ảnh hưởng timezone
// ===================================================

const date1 = new Date('2024-01-15T14:30:00.000Z'); // UTC
const date2 = new Date('2024-01-20T18:45:00.000Z'); // UTC

// ✅ So sánh: date1 có sau date2 không?
const isAfter = date1.getTime() > date2.getTime();
// 💡 getTime() trả về timestamp (số milliseconds)
// 💡 So sánh số → Không phụ thuộc timezone
// ✅ date1.getTime() = 1705329000000
// ✅ date2.getTime() = 1705761900000
// ✅ 1705329000000 > 1705761900000 = false (date1 trước date2)

// ✅ Tính số ngày chênh lệch
const daysDiff = Math.floor(
  (date2.getTime() - date1.getTime()) / (1000 * 60 * 60 * 24)
);
// 💡 Công thức: (timestamp2 - timestamp1) / milliseconds_per_day
// 💡 1000 ms × 60 s × 60 min × 24 h = 86,400,000 ms/ngày
// ✅ (1705761900000 - 1705329000000) / 86400000 = 5.01 ngày
// ✅ Math.floor() = 5 ngày

// ✅ So sánh bằng nhau
const isSame = date1.getTime() === date2.getTime();
// ✅ Chính xác hơn so sánh object (date1 === date2 luôn false)

// ✅ So sánh cùng ngày (bỏ qua giờ)
const isSameDay = date1.toDateString() === date2.toDateString();
// 💡 toDateString() = "Mon Jan 15 2024" (chỉ ngày, không có giờ)
// ⚠️ Lưu ý: toDateString() dùng local timezone!

**4. Date Arithmetic (Tính Toán Thời Gian):**

````typescript
// ===================================================
// ✅ Cộng/trừ ngày (dùng timestamp arithmetic)
// ===================================================

function addDays(date: Date, days: number): Date {
  // 💡 Công thức: Timestamp + (số ngày × milliseconds/ngày)
  // 💡 1 ngày = 24 giờ × 60 phút × 60 giây × 1000 milliseconds
  return new Date(date.getTime() + days * 24 * 60 * 60 * 1000);
}

// ✅ Ví dụ: Thêm 7 ngày
const today = new Date('2024-01-15T14:30:00.000Z');
const nextWeek = addDays(today, 7);
console.log(nextWeek.toISOString());
// 💡 "2024-01-22T14:30:00.000Z" (cùng giờ, khác ngày)

// ✅ Trừ ngày (dùng số âm)
const yesterday = addDays(today, -1);
console.log(yesterday.toISOString());
// 💡 "2024-01-14T14:30:00.000Z"

// ===================================================
// ✅ Start/End of day (UTC) - Đầu/cuối ngày
// ===================================================

const date = new Date('2024-01-15T14:30:45.123Z');

// ✅ Start of day: 00:00:00.000 UTC
const startOfDay = new Date(Date.UTC(
  date.getUTCFullYear(),  // 💡 2024
  date.getUTCMonth(),     // 💡 0 (January, zero-indexed)
  date.getUTCDate(),      // 💡 15
  // 💡 Không truyền hour, minute, second → mặc định 0
));
console.log(startOfDay.toISOString());
// 💡 "2024-01-15T00:00:00.000Z" (đầu ngày)

// ✅ End of day: 23:59:59.999 UTC
const endOfDay = new Date(Date.UTC(
  date.getUTCFullYear(),
  date.getUTCMonth(),
  date.getUTCDate(),
  23, 59, 59, 999  // 💡 23:59:59.999
));
console.log(endOfDay.toISOString());
// 💡 "2024-01-15T23:59:59.999Z" (cuối ngày)

// 💡 Dùng cho query database: Tìm tất cả records trong ngày
// WHERE createdAt >= startOfDay AND createdAt <= endOfDay
````

---

#### **� Native Date API Deep Dive - Hiểu Rõ Để Tránh Lỗi**

**🎯 Date Constructor - 4 Cách Tạo Date Object:**

```typescript
/**
 * 🏗️ CONSTRUCTOR #1: new Date() - Current time
 */

// 📅 Tạo Date object với thời gian hiện tại
const now = new Date();
// 💡 Lấy thời gian từ system clock của máy (browser hoặc server)
// 💡 Timezone = local timezone của máy đang chạy code
// 💡 Internal value = timestamp (milliseconds từ 1970-01-01 UTC)

console.log(now.toString());
// "Mon Dec 22 2025 14:30:45 GMT+0700 (Indochina Time)"
// 💡 toString() tự động format theo local timezone

console.log(now.toISOString());
// "2025-12-22T07:30:45.123Z"
// 💡 toISOString() LUÔN trả về UTC (Z suffix)
// 💡 Chênh 7 giờ so với toString() ở Vietnam (UTC+7)

console.log(now.getTime());
// 1734858645123
// 💡 Timestamp = milliseconds từ Unix Epoch (1970-01-01 00:00:00 UTC)
// 💡 Giá trị này GIỐNG NHAU trên mọi timezone

/**
 * 🏗️ CONSTRUCTOR #2: new Date(timestamp) - From milliseconds
 */

const fromTimestamp = new Date(1705329000000);
// 💡 timestamp = 1705329000000 = "2024-01-15 14:30:00 UTC"
// 💡 Tạo Date object từ absolute time point
// 💡 KHÔNG phụ thuộc timezone (timestamp là universal)

console.log(fromTimestamp.toString());
// Vietnam: "Mon Jan 15 2024 21:30:00 GMT+0700"
// US:      "Mon Jan 15 2024 09:30:00 GMT-0500"
// 💡 Cùng timestamp, display khác nhau theo local timezone
// 💡 Nhưng getTime() trả về cùng 1 số: 1705329000000

// ✅ BEST PRACTICE: Dùng timestamp cho storage/comparison
const serverTime = 1705329000000;
const clientDate = new Date(serverTime);
// 🚀 Không bị lỗi timezone, luôn đúng trên mọi máy

/**
 * 🏗️ CONSTRUCTOR #3: new Date(dateString) - Parse string
 * ⚠️ NGUY HIỂM: Kết quả phụ thuộc browser implementation!
 */

// ❌ ISO 8601 WITHOUT timezone → Browser-dependent!
const date1 = new Date('2024-01-15');
// 💡 Spec không rõ ràng: Là UTC hay local timezone?
// 🐛 Chrome/Firefox: Parse as UTC → "2024-01-15T00:00:00Z"
// 🐛 Safari (older): Parse as local → "2024-01-15T00:00:00+07:00"
// 💥 KHÁC NHAU giữa browsers!

console.log(date1.toISOString());
// Chrome: "2024-01-15T00:00:00.000Z" (UTC)
// Safari: "2024-01-14T17:00:00.000Z" (UTC, converted from local)
// 💡 Cùng code, khác kết quả!

// ✅ CORRECT: ISO 8601 WITH timezone (Z = UTC)
const date2 = new Date('2024-01-15T14:30:00.000Z');
// 💡 'Z' suffix = UTC explicit
// 💡 Tất cả browsers parse giống nhau
// 🚀 LUÔN dùng format này cho API responses

// ✅ CORRECT: ISO 8601 WITH offset
const date3 = new Date('2024-01-15T21:30:00+07:00');
// 💡 +07:00 = Vietnam timezone offset
// 💡 Browser convert về UTC: "2024-01-15T14:30:00.000Z"
// 💡 getTime() = 1705329000000 (giống date2)

// ❌ Non-ISO format → VERY RISKY!
const date4 = new Date('01/15/2024');
// 🐛 US browsers: MM/DD/YYYY (Jan 15)
// 🐛 VN browsers: DD/MM/YYYY? (May 01?) → Invalid!
// 💥 TUYỆT ĐỐI TRÁNH!

const date5 = new Date('15 Jan 2024');
// 💡 Có thể work, nhưng kết quả không đảm bảo
// 💡 Timezone handling không rõ ràng
// ⚠️ Chỉ dùng nếu bắt buộc, luôn test kỹ

/**
 * 🏗️ CONSTRUCTOR #4: new Date(year, month, day, ...) - Components
 * ⚠️ PITFALL: Month zero-indexed!
 */

const date6 = new Date(2024, 0, 15); // January 15, 2024
// 💡 Params: (year, month, day, hour, minute, second, millisecond)
// 🐛 month = 0-indexed: 0=Jan, 1=Feb, ..., 11=Dec
// 💡 KHÔNG có timezone param → tạo theo LOCAL timezone

console.log(date6.toString());
// "Mon Jan 15 2024 00:00:00 GMT+0700 (Indochina Time)"
// 💡 Tạo midnight local time (00:00 Vietnam)

// ❌ COMMON MISTAKE: Month 1-indexed
const wrongDate = new Date(2024, 1, 15); // ❌ Không phải Jan 15!
console.log(wrongDate.toString());
// "Thu Feb 15 2024 00:00:00 GMT+0700"
// 💡 month=1 là FEBRUARY, không phải January!

// ✅ CORRECT: Nhớ month zero-indexed
const correctDate = new Date(2024, 0, 15); // ✅ January 15

// 💡 Day, hour, minute, second, ms đều 1-indexed (bình thường)
const fullDate = new Date(2024, 0, 15, 14, 30, 45, 123);
// → "Mon Jan 15 2024 14:30:45.123 GMT+0700"

// ✅ Dùng Date.UTC() để tạo UTC time
const utcDate = new Date(Date.UTC(2024, 0, 15, 14, 30));
console.log(utcDate.toISOString());
// "2024-01-15T14:30:00.000Z"
// 💡 Date.UTC() returns timestamp (number)
// 💡 new Date(timestamp) converts to Date object
```

---

**🔧 Date Methods - Get/Set và UTC vs Local:**

```typescript
/**
 * 📖 GET METHODS - 2 Versions: Local vs UTC
 */

const date = new Date('2024-01-15T14:30:45.123Z'); // UTC time

// 🌍 LOCAL timezone methods (Vietnam UTC+7)
console.log(date.getFullYear()); // 2024
console.log(date.getMonth()); // 0 (January, zero-indexed!)
console.log(date.getDate()); // 15 (day of month)
console.log(date.getDay()); // 1 (Monday, 0=Sunday)
console.log(date.getHours()); // 21 (14 + 7 = 21:30 Vietnam)
console.log(date.getMinutes()); // 30
console.log(date.getSeconds()); // 45
console.log(date.getMilliseconds()); // 123

// 💡 get*() methods trả về LOCAL timezone values
// 💡 Vietnam UTC+7: 14:30 UTC → 21:30 local

// 🌐 UTC methods (always UTC, không phụ thuộc local timezone)
console.log(date.getUTCFullYear()); // 2024
console.log(date.getUTCMonth()); // 0 (January)
console.log(date.getUTCDate()); // 15
console.log(date.getUTCDay()); // 1 (Monday)
console.log(date.getUTCHours()); // 14 (giữ nguyên UTC)
console.log(date.getUTCMinutes()); // 30
console.log(date.getUTCSeconds()); // 45
console.log(date.getUTCMilliseconds()); // 123

// 💡 getUTC*() methods luôn trả về UTC values
// 💡 Kết quả GIỐNG NHAU trên mọi timezone
// ✅ BEST PRACTICE: Dùng getUTC*() cho logic, get*() cho display

// 📊 COMPARISON:
// ┌─────────────────┬──────────────┬──────────────┐
// │ Method          │ Vietnam      │ New York     │
// ├─────────────────┼──────────────┼──────────────┤
// │ getHours()      │ 21 (local)   │ 9 (local)    │ ← KHÁC NHAU
// │ getUTCHours()   │ 14 (UTC)     │ 14 (UTC)     │ ← GIỐNG NHAU
// └─────────────────┴──────────────┴──────────────┘

/**
 * 🔧 SET METHODS - Mutable (Thay đổi object gốc!)
 * ⚠️ NGUY HIỂM: Side effects!
 */

const original = new Date('2024-01-15T14:30:00.000Z');
console.log(original.toISOString());
// "2024-01-15T14:30:00.000Z"

// ❌ setMonth() mutates original object!
original.setMonth(2); // Set to March (month=2)
console.log(original.toISOString());
// "2024-03-15T14:30:00.000Z"  ← Original đã BỊ THAY ĐỔI!

// 💥 PROBLEM: Unexpected side effects
function displayNextMonth(date: Date) {
  date.setMonth(date.getMonth() + 1); // ❌ Mutate input!
  return date.toISOString();
}

const myDate = new Date('2024-01-15T14:30:00.000Z');
console.log(displayNextMonth(myDate));
// "2024-02-15T14:30:00.000Z"

console.log(myDate.toISOString());
// "2024-02-15T14:30:00.000Z"  ← myDate ĐÃ BỊ THAY ĐỔI!
// 💡 Caller không expect myDate thay đổi → BUG!

// ✅ SOLUTION 1: Clone trước khi modify
function displayNextMonthSafe(date: Date) {
  const clone = new Date(date.getTime()); // 📋 Clone
  clone.setMonth(clone.getMonth() + 1);
  return clone.toISOString();
}

const myDate2 = new Date('2024-01-15T14:30:00.000Z');
console.log(displayNextMonthSafe(myDate2));
// "2024-02-15T14:30:00.000Z"

console.log(myDate2.toISOString());
// "2024-01-15T14:30:00.000Z"  ← myDate2 KHÔNG thay đổi ✅

// ✅ SOLUTION 2: Immutable approach (recommended)
function addMonths(date: Date, months: number): Date {
  const result = new Date(date.getTime()); // Clone
  result.setMonth(result.getMonth() + months);
  return result; // Return new object
}

const myDate3 = new Date('2024-01-15T14:30:00.000Z');
const nextMonth = addMonths(myDate3, 1);
console.log(nextMonth.toISOString()); // "2024-02-15T14:30:00.000Z"
console.log(myDate3.toISOString()); // "2024-01-15T14:30:00.000Z" ✅

// ✅ SOLUTION 3: Dùng library (date-fns, Luxon) - immutable by default
// import { addMonths } from 'date-fns';
// const result = addMonths(date, 1);  // date không bị thay đổi
```

---

**⏰ Timezone Offset và Daylight Saving Time (DST):**

```typescript
/**
 * 🌍 getTimezoneOffset() - Offset giữa UTC và local
 */

const date = new Date('2024-01-15T14:30:00.000Z');

// 📏 getTimezoneOffset() returns minutes BEHIND UTC
const offset = date.getTimezoneOffset();
// Vietnam (UTC+7): -420 (negative = ahead of UTC)
// New York (UTC-5): 300 (positive = behind UTC)
// 💡 Counterintuitive: Positive = behind, Negative = ahead

console.log(offset); // Vietnam: -420 minutes
console.log(offset / 60); // Vietnam: -7 hours

// 💡 Convert offset to string
function formatOffset(offset: number): string {
  const hours = Math.floor(Math.abs(offset) / 60);
  const minutes = Math.abs(offset) % 60;
  const sign = offset <= 0 ? '+' : '-'; // Inverted!
  return `UTC${sign}${hours.toString().padStart(2, '0')}:${minutes
    .toString()
    .padStart(2, '0')}`;
}

console.log(formatOffset(offset)); // "UTC+07:00" (Vietnam)

/**
 * 🌞 DAYLIGHT SAVING TIME (DST) - Thay đổi offset theo mùa
 *
 * 💡 KHÁ I NIỆM:
 * - DST = Giờ mùa hè (Summer Time)
 * - Một số quốc gia chỉnh đồng hồ:
 *   + Mùa hè: +1 giờ (tiết kiệm điện)
 *   + Mùa đông: -1 giờ (về giờ chuẩn)
 * - Vietnam KHÔNG có DST
 * - US, Europe CÓ DST
 */

// 📅 New York timezone:
// - Winter (Standard Time): UTC-5
// - Summer (Daylight Time): UTC-4

const winterDate = new Date('2024-01-15T12:00:00Z'); // January (winter)
const summerDate = new Date('2024-07-15T12:00:00Z'); // July (summer)

// 💡 Giả sử chạy trên máy New York:
// winterDate.getTimezoneOffset() = 300 (UTC-5)
// summerDate.getTimezoneOffset() = 240 (UTC-4)
// 💥 CÙNG timezone nhưng offset KHÁC NHAU!

// 🐛 COMMON BUG: Hardcode offset
const VIETNAM_OFFSET_HOURS = 7; // ❌ Giả định offset luôn +7

function toVietnamTime(utcDate: Date): Date {
  // ❌ SAI: Không xét DST (nếu có)
  return new Date(utcDate.getTime() + VIETNAM_OFFSET_HOURS * 60 * 60 * 1000);
}

// 💡 Vietnam không có DST nên OK, nhưng US sẽ SAI!

// ✅ CORRECT: Dùng timezone database (IANA)
function toTimezone(utcDate: Date, timezone: string): Date {
  // Dùng Intl.DateTimeFormat hoặc library (date-fns-tz, Luxon)
  const formatted = new Intl.DateTimeFormat('en-US', {
    timeZone: timezone,
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    hour12: false,
  }).format(utcDate);

  // Parse formatted string back to Date
  // (Simplified, production code cần robust parsing)
  return new Date(formatted);
}

// ✅ Handle DST automatically
const nyTime = toTimezone(winterDate, 'America/New_York');
// 💡 Intl.DateTimeFormat tự động xét DST rules

/**
 * 🗓️ DST TRANSITION - Edge cases nguy hiểm
 */

// 🌅 DST begins: 2:00 AM → 3:00 AM (spring forward)
// 💥 2:30 AM KHÔNG TỒN TẠI (skipped)!

const springForward = new Date('2024-03-10T07:30:00Z'); // 2:30 AM EST
// 💡 Thời gian này bị skip do DST
// 💡 Browser/library tự động điều chỉnh

// 🌇 DST ends: 2:00 AM → 1:00 AM (fall back)
// 💥 1:30 AM XẢY RA 2 LẦN!

const fallBack1 = new Date('2024-11-03T05:30:00Z'); // 1:30 AM EDT (first)
const fallBack2 = new Date('2024-11-03T06:30:00Z'); // 1:30 AM EST (second)

// 💡 Cùng local time "1:30 AM" nhưng khác UTC!
// 💡 Ambiguous: Không biết lần nào

// ✅ BEST PRACTICE:
// 1. Lưu UTC (timestamp/ISO) → Không ambiguous
// 2. Dùng timezone database (IANA) → Auto-handle DST
// 3. Test với DST transition dates
// 4. Hiển thị timezone rõ ràng: "1:30 AM EST" vs "1:30 AM EDT"
```

---

**🧮 Date Arithmetic - Cộng/Trừ Thời Gian:**

```typescript
/**
 * ➕ ADD/SUBTRACT Days, Hours, Minutes...
 */

const date = new Date('2024-01-15T14:30:00.000Z');

// ✅ Add days (timestamp arithmetic)
function addDays(date: Date, days: number): Date {
  const MS_PER_DAY = 24 * 60 * 60 * 1000; // 86,400,000 ms
  return new Date(date.getTime() + days * MS_PER_DAY);
}

const tomorrow = addDays(date, 1);
console.log(tomorrow.toISOString());
// "2024-01-16T14:30:00.000Z"

const yesterday = addDays(date, -1);
console.log(yesterday.toISOString());
// "2024-01-14T14:30:00.000Z"

// ✅ Add hours
function addHours(date: Date, hours: number): Date {
  const MS_PER_HOUR = 60 * 60 * 1000; // 3,600,000 ms
  return new Date(date.getTime() + hours * MS_PER_HOUR);
}

// ✅ Add minutes
function addMinutes(date: Date, minutes: number): Date {
  const MS_PER_MINUTE = 60 * 1000; // 60,000 ms
  return new Date(date.getTime() + minutes * MS_PER_MINUTE);
}

// ⚠️ PITFALL: Add months (không đơn giản!)
function addMonthsNaive(date: Date, months: number): Date {
  const result = new Date(date.getTime());
  result.setMonth(result.getMonth() + months); // ❌ Có thể sai!
  return result;
}

// 🐛 PROBLEM: Month lengths khác nhau
const jan31 = new Date('2024-01-31T14:30:00.000Z');
const feb = addMonthsNaive(jan31, 1);
console.log(feb.toISOString());
// "2024-03-02T14:30:00.000Z"  ← Feb 31 không tồn tại → rolled to Mar 2!
// 💡 Jan 31 + 1 month = Feb 31 → overflow → Mar 2

// ✅ CORRECT: Clamp to last day of month
function addMonthsSafe(date: Date, months: number): Date {
  const result = new Date(date.getTime());
  const originalDay = result.getDate();

  result.setMonth(result.getMonth() + months);

  // Nếu ngày bị thay đổi (overflow), set về ngày cuối tháng
  if (result.getDate() !== originalDay) {
    result.setDate(0); // Set to last day of previous month
  }

  return result;
}

const feb2 = addMonthsSafe(jan31, 1);
console.log(feb2.toISOString());
// "2024-02-29T14:30:00.000Z"  ← Clamped to Feb 29 (leap year)

// 💡 Library handle edge cases này tốt hơn!
// import { addMonths } from 'date-fns';
// const result = addMonths(jan31, 1);  // Feb 29 ✅

/**
 * 📊 DIFFERENCE Between Dates
 */

const date1 = new Date('2024-01-15T14:30:00.000Z');
const date2 = new Date('2024-01-20T18:45:00.000Z');

// ✅ Difference in milliseconds
const diffMs = date2.getTime() - date1.getTime();
console.log(diffMs); // 450900000 ms

// ✅ Difference in days
const diffDays = diffMs / (1000 * 60 * 60 * 24);
console.log(diffDays); // 5.177083333... days
console.log(Math.floor(diffDays)); // 5 days (rounded down)

// ✅ Difference in hours
const diffHours = diffMs / (1000 * 60 * 60);
console.log(diffHours); // 124.25 hours

// ✅ Business days (exclude weekends)
function getBusinessDays(start: Date, end: Date): number {
  let count = 0;
  const current = new Date(start.getTime());

  while (current <= end) {
    const dayOfWeek = current.getDay();
    // 0 = Sunday, 6 = Saturday
    if (dayOfWeek !== 0 && dayOfWeek !== 6) {
      count++;
    }
    current.setDate(current.getDate() + 1);
  }

  return count;
}

const businessDays = getBusinessDays(date1, date2);
console.log(businessDays); // Số ngày làm việc (exclude Sat/Sun)

/**
 * 🗓️ START/END of Period
 */

const now = new Date('2024-01-15T14:30:45.123Z');

// ✅ Start of day (UTC)
const startOfDayUTC = new Date(
  Date.UTC(
    now.getUTCFullYear(),
    now.getUTCMonth(),
    now.getUTCDate(),
    0,
    0,
    0,
    0 // 00:00:00.000
  )
);
console.log(startOfDayUTC.toISOString());
// "2024-01-15T00:00:00.000Z"

// ✅ End of day (UTC)
const endOfDayUTC = new Date(
  Date.UTC(
    now.getUTCFullYear(),
    now.getUTCMonth(),
    now.getUTCDate(),
    23,
    59,
    59,
    999 // 23:59:59.999
  )
);
console.log(endOfDayUTC.toISOString());
// "2024-01-15T23:59:59.999Z"

// ✅ Start of month (UTC)
const startOfMonthUTC = new Date(
  Date.UTC(
    now.getUTCFullYear(),
    now.getUTCMonth(),
    1, // First day
    0,
    0,
    0,
    0
  )
);
console.log(startOfMonthUTC.toISOString());
// "2024-01-01T00:00:00.000Z"

// ✅ End of month (UTC)
const endOfMonthUTC = new Date(
  Date.UTC(
    now.getUTCFullYear(),
    now.getUTCMonth() + 1, // Next month
    0, // Day 0 = last day of previous month
    23,
    59,
    59,
    999
  )
);
console.log(endOfMonthUTC.toISOString());
// "2024-01-31T23:59:59.999Z"

// 💡 Day 0 trick: Month N, Day 0 = Last day of Month N-1
const lastDayOfJan = new Date(Date.UTC(2024, 1, 0)); // Feb 0 = Jan 31
console.log(lastDayOfJan.getUTCDate()); // 31

const lastDayOfFeb = new Date(Date.UTC(2024, 2, 0)); // Mar 0 = Feb 29 (leap)
console.log(lastDayOfFeb.getUTCDate()); // 29
```

---

#### **�📚 Libraries (Recommend)**

**date-fns (Functional, Tree-shakeable - Khuyến Nghị):**

```typescript
// ===================================================
// 📦 date-fns - Functional Programming Style
// ===================================================
// ✅ Ưu điểm: Tree-shakeable (chỉ import functions cần dùng)
// ✅ Ưu điểm: Immutable (không thay đổi date gốc)
// ✅ Ưu điểm: Functional style (dễ test, dễ compose)

import { format, parseISO, addDays, formatDistanceToNow } from 'date-fns';
import { utcToZonedTime } from 'date-fns-tz';

// ✅ Parse ISO string từ API
const date = parseISO('2024-01-15T14:30:00.000Z');
// 💡 parseISO() tự động parse ISO 8601 format
// 💡 Trả về Date object

// ✅ Format date theo pattern
format(date, 'yyyy-MM-dd HH:mm:ss');
// 💡 "2024-01-15 14:30:00"
// 💡 Pattern: yyyy=year, MM=month, dd=day, HH=hour24, mm=minute, ss=second

// ✅ Convert UTC → Vietnam timezone
const vnTime = utcToZonedTime(date, 'Asia/Ho_Chi_Minh');
// 💡 Input: UTC date
// 💡 Output: Date object với Vietnam timezone
format(vnTime, 'yyyy-MM-dd HH:mm:ss');
// 💡 "2024-01-15 21:30:00" (UTC+7)

// ✅ Relative time ("2 giờ trước", "3 ngày nữa")
formatDistanceToNow(date, { addSuffix: true });
// 💡 "2 hours ago" (tiếng Anh)
// 💡 Cần import locale để có tiếng Việt: import { vi } from 'date-fns/locale'
// 💡 formatDistanceToNow(date, { addSuffix: true, locale: vi }) → "2 giờ trước"

// ✅ Add days (immutable - không thay đổi date gốc)
const nextWeek = addDays(date, 7);
// 💡 date không bị thay đổi
// 💡 nextWeek là Date object mới
```

**Luxon (OOP, Timezone-aware - Mạnh Mẽ):**

```typescript
// ===================================================
// 📦 Luxon - Object-Oriented Programming Style
// ===================================================
// ✅ Ưu điểm: Immutable by default
// ✅ Ưu điểm: Timezone-aware tốt nhất
// ✅ Ưu điểm: API rõ ràng, dễ đọc
// ⚠️ Nhược điểm: Bundle size lớn hơn date-fns

import { DateTime } from 'luxon';

// ✅ Parse ISO string
const dt = DateTime.fromISO('2024-01-15T14:30:00.000Z');
// 💡 DateTime object (không phải Date object)
// 💡 Immutable - mọi method trả về DateTime mới

// ✅ Convert timezone và format
const vnTime = dt.setZone('Asia/Ho_Chi_Minh').toFormat('yyyy-MM-dd HH:mm:ss');
// 💡 setZone() → Convert sang Vietnam timezone
// 💡 toFormat() → Format theo pattern
// 💡 "2024-01-15 21:30:00"

// ✅ Add time (immutable)
const nextWeek = dt.plus({ days: 7 });
// 💡 dt không bị thay đổi
// 💡 nextWeek là DateTime mới

// ✅ Relative time
dt.plus({ days: 7 }).toRelative();
// 💡 "in 7 days" (tiếng Anh)
// 💡 Cần set locale: dt.setLocale('vi').toRelative() → "7 ngày nữa"

// ✅ So sánh dates
const isAfter = dt1 > dt2; // ✅ Có thể so sánh trực tiếp
const isSame = dt1.hasSame(dt2, 'day'); // ✅ Cùng ngày?

// ✅ Start/End of period
const startOfDay = dt.startOf('day'); // 💡 00:00:00
const endOfMonth = dt.endOf('month'); // 💡 Ngày cuối tháng, 23:59:59
```

**Day.js (Lightweight 2KB - Nhẹ Nhàng):**

```typescript
// ===================================================
// 📦 Day.js - Lightweight Alternative
// ===================================================
// ✅ Ưu điểm: Chỉ 2KB gzipped (nhỏ nhất!)
// ✅ Ưu điểm: API giống Moment.js (dễ migrate)
// ✅ Ưu điểm: Immutable by default
// ⚠️ Nhược điểm: Cần extend plugins cho timezone support

import dayjs from 'dayjs';
import utc from 'dayjs/plugin/utc'; // 💡 Plugin cho UTC
import timezone from 'dayjs/plugin/timezone'; // 💡 Plugin cho timezone

// ✅ Extend plugins (chỉ làm 1 lần, nên để trong setup file)
dayjs.extend(utc);
dayjs.extend(timezone);

// ✅ Parse ISO string và convert timezone
dayjs('2024-01-15T14:30:00.000Z')
  .tz('Asia/Ho_Chi_Minh') // 💡 Convert sang Vietnam timezone
  .format('YYYY-MM-DD HH:mm:ss');
// 💡 "2024-01-15 21:30:00"

// ✅ Format tokens (khác date-fns!)
// 💡 YYYY = year (2024)
// 💡 MM = month (01)
// 💡 DD = day (15)
// 💡 HH = hour 24h (21)
// 💡 mm = minute (30) ⚠️ Lưu ý: mm = minute, không phải MM!
// 💡 ss = second (45)

// ✅ Add time
const nextWeek = dayjs('2024-01-15T14:30:00.000Z').add(7, 'day');
// 💡 dayjs object immutable → add() trả về dayjs mới

// ✅ UTC operations
const utcDate = dayjs.utc('2024-01-15T14:30:00.000Z');
// 💡 Tạo dayjs object ở UTC mode
const localDate = utcDate.local(); // 💡 Convert về local timezone

// ✅ So sánh
const isAfter = dayjs(date1).isAfter(dayjs(date2));
const isSame = dayjs(date1).isSame(dayjs(date2), 'day'); // ✅ Cùng ngày?
```

---

#### **🌍 Real-World Scenarios - Tình Huống Thực Tế**

**Scenario 1: E-Commerce Flash Sale - Xử Lý Giờ Khuyến Mãi:**

```typescript
/**
 * 🛍️ REQUIREMENT (Yêu Cầu):
 * - Flash sale bắt đầu: 21:00 ngày 15/01/2024 (Vietnam time)
 * - Hiển thị countdown cho users ở nhiều timezone
 * - Server lưu UTC, client display local time
 */

// ===================================================
// 🏛️ SERVER-SIDE: Lưu flash sale time
// ===================================================

interface FlashSale {
  id: string;
  name: string;
  startTime: string; // 💡 ISO 8601 UTC string
  endTime: string; // 💡 ISO 8601 UTC string
  timezone: string; // 💡 Timezone nơi tổ chức (reference - để hiển thị)
}

// Admin tạo flash sale (Vietnam timezone)
const createFlashSale = (localStartTime: string) => {
  // 💡 Input: localStartTime = "2024-01-15 21:00" (Vietnam time)
  // 💡 Admin nhập giờ Vietnam → Cần convert sang UTC để lưu

  // 🔄 Bước 1: Tạo Date object từ Vietnam time với offset
  const vietnamTime = new Date(`${localStartTime}+07:00`);
  // 💡 "+07:00" = Vietnam timezone offset
  // 💡 Browser parse → "2024-01-15T21:00:00+07:00"

  // 🔄 Bước 2: Convert sang UTC
  const utcTime = vietnamTime.toISOString();
  // 💡 toISOString() LUÔN trả về UTC với 'Z' suffix
  // 💡 "2024-01-15T14:00:00.000Z" (UTC)
  // 💡 21:00 Vietnam = 14:00 UTC (21 - 7 = 14)

  // 🔄 Bước 3: Tính endTime (3 giờ sau)
  const endTime = new Date(
    vietnamTime.getTime() + 3 * 60 * 60 * 1000
  ).toISOString();
  // 💡 +3 hours = 24:00 Vietnam = 17:00 UTC
  // 💡 vietnamTime.getTime() = timestamp
  // 💡 + 3 * 60 * 60 * 1000 = + 3 giờ (milliseconds)

  const flashSale: FlashSale = {
    id: 'sale123',
    name: 'Tết Sale',
    startTime: utcTime, // ✅ Lưu UTC vào database
    endTime: endTime, // ✅ Lưu UTC vào database
    timezone: 'Asia/Ho_Chi_Minh', // 💡 Reference timezone (để hiển thị)
  };

  return flashSale;
};

// ===================================================
// 📱 CLIENT-SIDE: Hiển thị cho users
// ===================================================

const FlashSaleCountdown = ({ sale }: { sale: FlashSale }) => {
  const [timeLeft, setTimeLeft] = useState('');

  useEffect(() => {
    // ⏱️ Countdown timer: Update mỗi giây
    const interval = setInterval(() => {
      const now = Date.now(); // 💡 Current timestamp (UTC-based)
      // 💡 Date.now() = milliseconds từ 1970-01-01 UTC
      // 💡 Giống nhau trên mọi timezone

      const startTime = new Date(sale.startTime).getTime();
      // 💡 Parse UTC ISO string → timestamp
      // 💡 sale.startTime = "2024-01-15T14:00:00.000Z"
      // 💡 getTime() = 1705320000000

      const diff = startTime - now;
      // 💡 Số milliseconds còn lại đến khi flash sale bắt đầu

      if (diff <= 0) {
        // ✅ Flash sale đã bắt đầu
        setTimeLeft('Flash sale đã bắt đầu!');
        clearInterval(interval);
        return;
      }

      // 📊 Calculate hours, minutes, seconds từ milliseconds
      const hours = Math.floor(diff / (1000 * 60 * 60));
      // 💡 diff / 3,600,000 ms = số giờ

      const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
      // 💡 Phần dư sau khi trừ giờ / 60,000 ms = số phút

      const seconds = Math.floor((diff % (1000 * 60)) / 1000);
      // 💡 Phần dư sau khi trừ phút / 1,000 ms = số giây

      setTimeLeft(`${hours}h ${minutes}m ${seconds}s`);
      // 💡 "2h 30m 45s" → Update mỗi giây
    }, 1000); // 💡 Update mỗi 1000ms (1 giây)

    return () => clearInterval(interval); // 🧹 Cleanup
  }, [sale.startTime]);

  // 📋 Display local time cho user
  const userTimezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
  // 💡 Auto-detect user's timezone từ browser
  // 💡 Vietnam: "Asia/Ho_Chi_Minh"
  // 💡 US: "America/New_York"

  const localStartTime = new Date(sale.startTime).toLocaleString('vi-VN', {
    timeZone: userTimezone, // 💡 Convert UTC → user's timezone
    dateStyle: 'long', // 💡 "15 tháng 1, 2024"
    timeStyle: 'short', // 💡 "21:00"
  });

  return (
    <div>
      <h2>{sale.name}</h2>
      <p>Bắt đầu: {localStartTime}</p>
      {/* 💡 Vietnam user thấy: "21:00, 15 tháng 1, 2024"
           US user thấy: "9:00 AM, January 15, 2024"
           → Cùng 1 UTC time, hiển thị khác nhau theo timezone */}
      <p>Còn lại: {timeLeft}</p>
      {/* 💡 Countdown giống nhau cho mọi user (dựa trên UTC)
           → Tất cả users thấy cùng countdown, nhưng local time khác nhau */}
    </div>
  );
};

/**
 * 💡 KẾT QUẢ (Results):
 *
 * Database lưu:
 * - startTime: "2024-01-15T14:00:00.000Z" (UTC, universal)
 * - endTime: "2024-01-15T17:00:00.000Z" (UTC)
 *
 * Users ở các timezone khác nhau thấy:
 * - Vietnam user (UTC+7): "21:00 - 00:00" (15/01/2024)
 * - Singapore user (UTC+8): "22:00 - 01:00" (15-16/01/2024)
 * - US user (UTC-5): "9:00 AM - 12:00 PM" (15/01/2024)
 * - UK user (UTC+0): "14:00 - 17:00" (15/01/2024)
 *
 * Countdown:
 * - Tất cả users thấy CÙNG countdown (dựa trên UTC)
 * - VD: "2h 30m 15s" → Giống nhau cho mọi user
 * - Khi countdown = 0 → Flash sale bắt đầu cùng lúc (theo UTC)
 *
 * ✅ LỢI ÍCH:
 * - 1 giá trị UTC trong database → Hiển thị đúng cho mọi timezone
 * - Không cần lưu nhiều timezone khác nhau
 * - Countdown chính xác, không bị lệch múi giờ
 */
```

---

**Scenario 2: Meeting Scheduler - Nhiều Timezone:**

```typescript
/**
 * 💼 REQUIREMENT:
 * - Boss ở New York schedule meeting: "9:00 AM my time"
 * - Dev ở Vietnam nhận invite
 * - Auto-convert và hiển thị đúng giờ local
 */

interface Meeting {
  id: string;
  title: string;
  startTime: string; // UTC ISO
  duration: number; // minutes
  organizerTimezone: string;
  participants: Array<{
    email: string;
    timezone: string;
  }>;
}

// ===================================================
// 👔 Boss tạo meeting (New York)
// ===================================================

const scheduleMeeting = () => {
  // 💡 Boss input: "9:00 AM" (New York time - local time của organizer)
  const localTime = '2024-01-15 09:00';

  // 🔄 Bước 1: Convert New York time → UTC
  // 💡 New York winter: UTC-5 (EST - Eastern Standard Time)
  // 💡 New York summer: UTC-4 (EDT - Eastern Daylight Time)
  // ⚠️ Lưu ý: Offset thay đổi theo DST!

  const nyTime = new Date(`${localTime}-05:00`);
  // 💡 "+localTime-05:00" = New York time với offset UTC-5
  // 💡 Browser parse → "2024-01-15T09:00:00-05:00"

  const utcTime = nyTime.toISOString();
  // 💡 toISOString() convert về UTC
  // 💡 "2024-01-15T14:00:00.000Z" (UTC)
  // 💡 9:00 AM NY (UTC-5) = 14:00 UTC (9 + 5 = 14)

  const meeting: Meeting = {
    id: 'meet123',
    title: 'Sprint Planning',
    startTime: utcTime, // ✅ Lưu UTC vào database
    duration: 60, // 💡 60 phút
    organizerTimezone: 'America/New_York', // 💡 Reference timezone
    participants: [
      { email: 'dev@vn.com', timezone: 'Asia/Ho_Chi_Minh' },
      { email: 'pm@sg.com', timezone: 'Asia/Singapore' },
    ],
  };

  return meeting;
};

// ===================================================
// 📧 Send calendar invites (Gửi lời mời lịch)
// ===================================================

const sendInvites = (meeting: Meeting) => {
  meeting.participants.forEach((participant) => {
    // 🔄 Convert UTC → participant's timezone để hiển thị
    const localTime = new Date(meeting.startTime).toLocaleString('en-US', {
      timeZone: participant.timezone, // 💡 Timezone của người tham gia
      dateStyle: 'full', // 💡 "Monday, January 15, 2024"
      timeStyle: 'short', // 💡 "9:00 PM"
    });

    // 💡 Vietnam dev nhận email:
    // Subject: "Meeting: Sprint Planning"
    // Body: "Meeting time: Monday, January 15, 2024 at 9:00 PM"
    // 💡 14:00 UTC + 7 giờ = 21:00 Vietnam (9:00 PM)

    // 💡 Singapore PM nhận email:
    // Subject: "Meeting: Sprint Planning"
    // Body: "Meeting time: Monday, January 15, 2024 at 10:00 PM"
    // 💡 14:00 UTC + 8 giờ = 22:00 Singapore (10:00 PM)

    // 💡 US Boss (organizer) thấy:
    // "Meeting time: Monday, January 15, 2024 at 9:00 AM"
    // 💡 14:00 UTC - 5 giờ = 9:00 AM New York

    sendEmail(participant.email, {
      subject: `Meeting: ${meeting.title}`,
      body: `
        Meeting time: ${localTime}
        Duration: ${meeting.duration} minutes

        Join link: https://meet.example.com/${meeting.id}
      `,
    });
  });
};

// ===================================================
// 📅 iCalendar format (cho Outlook, Google Calendar)
// ===================================================

const generateICS = (meeting: Meeting, participantTimezone: string) => {
  // ✅ Parse UTC start time
  const start = new Date(meeting.startTime);
  // 💡 meeting.startTime = "2024-01-15T14:00:00.000Z" (UTC)

  // ✅ Calculate end time (start + duration)
  const end = new Date(start.getTime() + meeting.duration * 60 * 1000);
  // 💡 meeting.duration = 60 phút
  // 💡 + 60 * 60 * 1000 = + 3,600,000 ms
  // 💡 end = "2024-01-15T15:00:00.000Z" (UTC)

  // 💡 iCalendar format: YYYYMMDDTHHMMSSZ (UTC, không có dấu gạch ngang)
  // 💡 VD: "20240115T140000Z" = 2024-01-15 14:00:00 UTC
  const formatICS = (date: Date) => {
    return date
      .toISOString()
      .replace(/[-:]/g, '') // 💡 Xóa dấu "-" và ":"
      .replace(/\.\d{3}/, ''); // 💡 Xóa milliseconds ".000"
    // 💡 "2024-01-15T14:00:00.000Z" → "20240115T140000Z"
  };

  // ✅ Generate iCalendar content
  return `
BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
DTSTART:${formatICS(start)}    💡 Start time (UTC)
DTEND:${formatICS(end)}        💡 End time (UTC)
SUMMARY:${meeting.title}       💡 Event title
DESCRIPTION:Meeting scheduled by organizer
END:VEVENT
END:VCALENDAR
  `.trim();

  // 💡 Calendar app (Outlook, Google Calendar) tự động:
  // 1. Parse UTC time từ DTSTART/DTEND
  // 2. Convert UTC → user's local timezone
  // 3. Hiển thị đúng giờ local cho user
  //
  // VD: User Vietnam mở calendar:
  // - DTSTART: 20240115T140000Z (14:00 UTC)
  // - Calendar hiển thị: "21:00" (14:00 + 7 = 21:00 Vietnam)
};
```

---

**Scenario 3: Subscription Renewal - Handle Exact Time:**

```typescript
/**
 * 💳 REQUIREMENT:
 * - User mua subscription: 15/01/2024 21:30 (Vietnam)
 * - Renewal sau 30 ngày: 14/02/2024 21:30 (Vietnam)
 * - Lưu exact time để charge vào đúng giờ
 */

interface Subscription {
  userId: string;
  planId: string;
  startDate: string; // UTC ISO
  renewalDate: string; // UTC ISO
  timezone: string; // User's timezone khi mua
}

// ===================================================
// 🛍️ User mua subscription
// ===================================================

const purchaseSubscription = (userId: string, planId: string) => {
  const now = new Date(); // 💡 Current time (local timezone của user)
  // 💡 VD: User ở Vietnam → now = "2024-01-15T21:30:00+07:00"

  // 🔐 Lưu user's timezone (để hiển thị thông báo đúng giờ sau này)
  const userTimezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
  // 💡 Auto-detect từ browser
  // 💡 Vietnam: "Asia/Ho_Chi_Minh"
  // 💡 US: "America/New_York"

  // 📊 Calculate renewal date (30 ngày sau, cùng giờ)
  const renewalDate = new Date(now.getTime() + 30 * 24 * 60 * 60 * 1000);
  // 💡 Công thức: Timestamp hiện tại + (30 ngày × milliseconds/ngày)
  // 💡 30 * 24 * 60 * 60 * 1000 = 2,592,000,000 ms = 30 ngày
  // 💡 Timestamp arithmetic → Tự động handle DST (nếu có)
  // ✅ VD: Jan 15 21:30 → Feb 14 21:30 (cùng giờ local)

  const subscription: Subscription = {
    userId,
    planId,
    startDate: now.toISOString(), // ✅ UTC: "2024-01-15T14:30:00.000Z"
    renewalDate: renewalDate.toISOString(), // ✅ UTC: "2024-02-14T14:30:00.000Z"
    timezone: userTimezone, // 💡 Lưu timezone để hiển thị thông báo đúng giờ
  };

  return subscription;
};

// ===================================================
// ⏰ Cron job: Check renewals mỗi 5 phút
// ===================================================

const processRenewals = async () => {
  const now = Date.now();
  // 💡 Current timestamp (UTC-based)
  // 💡 VD: 1705329000000 = "2024-01-15T14:30:00.000Z"

  // 🔍 Query subscriptions cần renew (renewalDate ≤ now)
  const dueSubscriptions = await db.subscriptions.find({
    renewalDate: { $lte: new Date(now) }, // 💡 ≤ current time
    // 💡 $lte = less than or equal
    // 💡 So sánh timestamp → Chính xác, không bị lỗi timezone
  });

  for (const sub of dueSubscriptions) {
    try {
      // 💳 Charge user (charge vào đúng giờ renewal)
      await chargeUser(sub.userId, sub.planId);

      // 🔄 Update next renewal (30 ngày sau, cùng giờ)
      const nextRenewal = new Date(
        new Date(sub.renewalDate).getTime() + 30 * 24 * 60 * 60 * 1000
      );
      // 💡 sub.renewalDate = "2024-01-15T14:30:00.000Z" (UTC)
      // 💡 + 30 ngày = "2024-02-14T14:30:00.000Z" (UTC)
      // ✅ Giữ nguyên giờ UTC → User thấy cùng giờ local

      await db.subscriptions.updateOne(
        { _id: sub._id },
        {
          $set: {
            renewalDate: nextRenewal.toISOString(), // ✅ UTC
            lastChargedAt: new Date().toISOString(), // ✅ UTC
          },
        }
      );

      // 📧 Send notification to user (hiển thị giờ local)
      const localRenewalTime = nextRenewal.toLocaleString('vi-VN', {
        timeZone: sub.timezone, // 💡 User's timezone đã lưu
        dateStyle: 'long', // 💡 "15 tháng 1, 2024"
        timeStyle: 'short', // 💡 "21:30"
      });
      // 💡 nextRenewal = UTC → Convert sang user's timezone
      // 💡 Vietnam user: "15 tháng 2, 2024 lúc 21:30"

      await sendEmail(sub.userId, {
        subject: 'Subscription Renewed',
        body: `Your subscription has been renewed.
Next renewal: ${localRenewalTime}`,
        // 💡 User thấy giờ đúng múi giờ của họ
      });
    } catch (error) {
      console.error(`Failed to renew subscription ${sub._id}:`, error);
      // 🚨 Log và retry sau (có thể dùng retry pattern từ Q28)
    }
  }
};

// 💡 Run every 5 minutes (cron job)
setInterval(processRenewals, 5 * 60 * 1000);
// 💡 5 * 60 * 1000 = 300,000 ms = 5 phút
// 💡 Check mỗi 5 phút → Không miss renewal

/**
 * ✅ ADVANTAGES (Ưu Điểm):
 *
 * 1. Lưu UTC → Không bị lỗi timezone khi server/database migrate
 *    - Server ở US → Database ở Singapore → Vẫn đúng
 *    - Chỉ cần convert UTC → local khi display
 *
 * 2. Timestamp arithmetic → Handle DST automatically
 *    - +30 ngày = +2,592,000,000 ms
 *    - Không cần tính DST thủ công
 *    - Library tự động handle DST transitions
 *
 * 3. Lưu user timezone → Display thông báo đúng giờ local
 *    - User Vietnam: "21:30" (đúng giờ họ mua)
 *    - User US: "9:30 AM" (đúng giờ họ mua)
 *    - Cùng 1 UTC time, hiển thị khác nhau theo timezone
 *
 * 4. Query database hiệu quả
 *    - So sánh timestamp (số nguyên) → Fast index
 *    - Không cần parse string mỗi lần query
 */
```

---

**Scenario 4: Logging & Debugging - Timestamp Everything:**

```typescript
/**
 * 📝 REQUIREMENT:
 * - Log mọi hành động của user với timestamp
 * - Admin xem logs với timezone của họ
 * - Filter logs theo time range
 */

interface LogEntry {
  id: string;
  userId: string;
  action: string;
  timestamp: number; // 💡 Unix milliseconds (không phải ISO string)
  metadata: Record<string, any>;
}

// ===================================================
// 📝 Logger service - Log mọi hành động với timestamp
// ===================================================

class Logger {
  static log(
    userId: string,
    action: string,
    metadata: Record<string, any> = {}
  ) {
    const entry: LogEntry = {
      id: generateId(),
      userId,
      action,
      timestamp: Date.now(), // ✅ Timestamp (universal - milliseconds)
      // 💡 Date.now() = 1705329000000 (số nguyên)
      // 💡 Không phụ thuộc timezone
      // ✅ Database lưu NUMBER (BIGINT) → Fast query, efficient index
      metadata,
    };

    // 💾 Save to database
    db.logs.insert(entry);
    // 💡 Database lưu: { timestamp: 1705329000000 }
    // ✅ Index timestamp → Query nhanh

    // 🖨️ Console log (for debugging - hiển thị local time)
    const localTime = new Date(entry.timestamp).toLocaleString('vi-VN', {
      timeZone: 'Asia/Ho_Chi_Minh', // 💡 Convert UTC → Vietnam để đọc dễ
    });
    console.log(`[${localTime}] User ${userId}: ${action}`);
    // 💡 "[15/01/2024, 21:30:45] User user123: LOGIN"
    // 💡 Developer đọc log dễ hơn với local time
  }
}

// Usage
Logger.log('user123', 'LOGIN', { ip: '1.2.3.4', userAgent: '...' });
Logger.log('user123', 'PLACE_ORDER', { orderId: 'order456', amount: 1000000 });

// ===================================================
// 🔍 Admin query logs (Truy vấn logs theo khoảng thời gian)
// ===================================================

const getLogsInRange = async (startTime: number, endTime: number) => {
  // 💡 Input: startTime, endTime là timestamps (số milliseconds)
  // 💡 VD: startTime = 1705329000000, endTime = 1705415400000

  // ✅ Query với timestamp (efficient, indexed)
  const logs = await db.logs
    .find({
      timestamp: { $gte: startTime, $lte: endTime },
      // 💡 $gte = greater than or equal (≥)
      // 💡 $lte = less than or equal (≤)
      // 💡 So sánh số nguyên → Rất nhanh (có index)
    })
    .sort({ timestamp: -1 }); // 💡 Newest first (-1 = descending)

  return logs;
};

// 💡 Helper: Convert user input (date strings) → timestamps
const getLogsForDateRange = async (
  startDate: string, // 💡 "15/01/2024" (user input)
  endDate: string, // 💡 "20/01/2024"
  userTimezone: string = 'Asia/Ho_Chi_Minh'
) => {
  // 🔄 Convert user's local dates → UTC timestamps
  const startTimestamp = new Date(
    `${startDate} 00:00:00+07:00` // 💡 Start of day Vietnam
  ).getTime();

  const endTimestamp = new Date(
    `${endDate} 23:59:59+07:00` // 💡 End of day Vietnam
  ).getTime();

  return getLogsInRange(startTimestamp, endTimestamp);
};

// 📊 Admin UI: Display logs
const LogsTable = ({
  logs,
  adminTimezone,
}: {
  logs: LogEntry[];
  adminTimezone: string;
}) => {
  return (
    <table>
      <thead>
        <tr>
          <th>Time</th>
          <th>User</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        {logs.map((log) => {
          // 🔄 Convert timestamp → admin's local time để hiển thị
          const localTime = new Date(log.timestamp).toLocaleString('en-US', {
            timeZone: adminTimezone, // 💡 Admin's timezone
            dateStyle: 'short', // 💡 "1/15/2024" hoặc "15/01/2024"
            timeStyle: 'medium', // 💡 "9:30:45 AM" hoặc "21:30:45"
          });
          // 💡 log.timestamp = 1705329000000 (UTC)
          // 💡 Convert → admin's timezone → "1/15/2024, 9:30:45 AM"

          return (
            <tr key={log.id}>
              <td>{localTime}</td>
              {/* 💡 Admin ở Vietnam: "15/01/2024, 21:30:45"
                   Admin ở US: "1/15/2024, 9:30:45 AM"
                   Admin ở UK: "15/01/2024, 14:30:45"
                   → Cùng 1 timestamp, hiển thị khác nhau theo admin's timezone */}
              <td>{log.userId}</td>
              <td>{log.action}</td>
            </tr>
          );
        })}
      </tbody>
    </table>
  );
};

/**
 * ✅ BENEFITS (Lợi Ích):
 *
 * 1. Timestamp (number) → Fast query, efficient index
 *    - Database index trên NUMBER → Rất nhanh
 *    - So sánh số nguyên: timestamp1 > timestamp2 → O(1)
 *    - Không cần parse string mỗi lần query
 *
 * 2. Universal → Không bị lỗi timezone khi admin ở nơi khác
 *    - Admin Vietnam xem logs → Thấy giờ Vietnam
 *    - Admin US xem logs → Thấy giờ US
 *    - Cùng 1 database, không cần lưu nhiều timezone
 *
 * 3. Convert on display → Mỗi admin thấy giờ local của họ
 *    - Database: 1705329000000 (universal)
 *    - Display: Convert UTC → admin's timezone
 *    - User experience tốt (đúng giờ local)
 *
 * 4. Query range dễ dàng
 *    - WHERE timestamp BETWEEN start AND end
 *    - Không cần tính toán timezone phức tạp
 */
```

---

**Scenario 5: Recurring Events - Weekly Meeting:**

```typescript
/**
 * 🔄 REQUIREMENT:
 * - Weekly standup: Mỗi thứ 2 lúc 9:00 AM (Vietnam)
 * - Generate 10 occurrences tiếp theo
 * - Handle DST (nếu user ở timezone có DST)
 */

interface RecurringEvent {
  id: string;
  title: string;
  startTime: string; // UTC ISO (first occurrence)
  recurrence: {
    frequency: 'daily' | 'weekly' | 'monthly';
    interval: number; // Every N days/weeks/months
    dayOfWeek?: number; // 0=Sun, 1=Mon, ..., 6=Sat
    endAfter?: number; // Stop after N occurrences
  };
  timezone: string; // Timezone event được định nghĩa
}

// ===================================================
// 📋 Tạo recurring event (Sự kiện lặp lại)
// ===================================================

const createRecurringEvent = () => {
  // 💡 First occurrence: Thứ 2 tiếp theo lúc 9:00 AM Vietnam
  const firstOccurrence = getNextMonday(new Date());
  // 💡 Tìm thứ 2 tiếp theo từ hôm nay

  firstOccurrence.setHours(9, 0, 0, 0); // 💡 9:00 AM local time
  // 💡 setHours() dùng LOCAL timezone
  // 💡 Vietnam: 9:00 AM = 09:00 local

  const event: RecurringEvent = {
    id: 'recurring123',
    title: 'Weekly Standup',
    startTime: firstOccurrence.toISOString(), // ✅ UTC: "2024-01-15T02:00:00.000Z"
    // 💡 9:00 AM Vietnam (UTC+7) = 2:00 AM UTC (9 - 7 = 2)
    recurrence: {
      frequency: 'weekly', // 💡 Hàng tuần
      interval: 1, // 💡 Mỗi 1 tuần (có thể 2 tuần = interval: 2)
      dayOfWeek: 1, // 💡 Thứ 2 (0=Sunday, 1=Monday, ..., 6=Saturday)
      endAfter: 10, // 💡 10 lần (có thể null = vô hạn)
    },
    timezone: 'Asia/Ho_Chi_Minh', // 💡 Timezone định nghĩa event
  };

  return event;
};

// ===================================================
// 🔍 Helper: Tìm thứ 2 tiếp theo
// ===================================================

function getNextMonday(from: Date): Date {
  const result = new Date(from.getTime()); // 💡 Clone date
  const currentDay = result.getDay(); // 💡 0=Sunday, 1=Monday, ..., 6=Saturday

  // 💡 Tính số ngày đến thứ 2 tiếp theo
  const daysUntilMonday = (1 - currentDay + 7) % 7 || 7;
  // 💡 Công thức: (1 - currentDay + 7) % 7
  // 💡 VD: Hôm nay = Thứ 2 (1) → (1-1+7)%7 = 7 → Thứ 2 tuần sau
  // 💡 VD: Hôm nay = Thứ 3 (2) → (1-2+7)%7 = 6 → 6 ngày nữa = Thứ 2
  // 💡 || 7: Nếu hôm nay là Chủ nhật (0) → 7 ngày nữa

  result.setDate(result.getDate() + daysUntilMonday);
  // 💡 Thêm số ngày vào date
  return result;
}

// ===================================================
// 📊 Generate occurrences (Tạo danh sách các lần xảy ra)
// ===================================================

const generateOccurrences = (event: RecurringEvent): Date[] => {
  const occurrences: Date[] = [];
  let current = new Date(event.startTime); // 💡 Bắt đầu từ lần đầu tiên
  // 💡 event.startTime = "2024-01-15T02:00:00.000Z" (UTC)

  const maxOccurrences = event.recurrence.endAfter || 10;
  // 💡 Số lần tối đa (mặc định 10 nếu không có endAfter)

  for (let i = 0; i < maxOccurrences; i++) {
    occurrences.push(new Date(current)); // 💡 Clone date vào array
    // 💡 Lần 1: "2024-01-15T02:00:00.000Z"
    // 💡 Lần 2: "2024-01-22T02:00:00.000Z"
    // 💡 Lần 3: "2024-01-29T02:00:00.000Z"
    // ...

    // 🔄 Add interval (weeks) để tính lần tiếp theo
    current = new Date(
      current.getTime() + event.recurrence.interval * 7 * 24 * 60 * 60 * 1000
    );
    // 💡 Công thức: + (interval × 7 ngày × milliseconds/ngày)
    // 💡 interval = 1 → + 7 ngày
    // 💡 interval = 2 → + 14 ngày (2 tuần)
    // 💡 Timestamp arithmetic → Tự động handle DST
  }

  return occurrences;
};

// ===================================================
// 📌 Display occurrences (Hiển thị các lần xảy ra)
// ===================================================

const RecurringEventCalendar = ({ event }: { event: RecurringEvent }) => {
  const occurrences = generateOccurrences(event);
  // 💡 Array of Date objects (UTC)
  // 💡 [Date1, Date2, Date3, ...]

  return (
    <div>
      <h3>{event.title}</h3>
      <p>Every {event.recurrence.frequency}</p>
      {/* 💡 "Every weekly" */}

      <ul>
        {occurrences.map((date, index) => {
          // 🔄 Convert UTC → event timezone để hiển thị
          const localTime = date.toLocaleString('vi-VN', {
            timeZone: event.timezone, // 💡 'Asia/Ho_Chi_Minh'
            dateStyle: 'full', // 💡 "Thứ Hai, 15 tháng 1, 2024"
            timeStyle: 'short', // 💡 "9:00"
          });
          // 💡 date = UTC "2024-01-15T02:00:00.000Z"
          // 💡 Convert → Vietnam: "Thứ Hai, 15 tháng 1, 2024 lúc 9:00"

          return (
            <li key={index}>
              Occurrence {index + 1}: {localTime}
              {/* 💡 "Occurrence 1: Thứ Hai, 15 tháng 1, 2024 lúc 9:00"
                   "Occurrence 2: Thứ Hai, 22 tháng 1, 2024 lúc 9:00"
                   "Occurrence 3: Thứ Hai, 29 tháng 1, 2024 lúc 9:00"
                   ... */}
            </li>
          );
        })}
      </ul>
    </div>
  );
};

/**
 * 💡 NOTES (Lưu Ý Quan Trọng):
 *
 * 1. Vietnam KHÔNG có DST → 9:00 AM luôn là 9:00 AM
 *    - UTC offset luôn +7 giờ
 *    - Không có thay đổi giờ theo mùa
 *    - Đơn giản hơn!
 *
 * 2. Nếu user ở US (có DST):
 *    - Winter (EST): 9:00 AM EST = UTC-5 → UTC = 14:00
 *    - Summer (EDT): 9:00 AM EDT = UTC-4 → UTC = 13:00
 *    - 💥 UTC time KHÁC NHAU giữa winter/summer!
 *    - VD: "9:00 AM" mùa đông = "2024-01-15T14:00:00.000Z"
 *          "9:00 AM" mùa hè = "2024-07-15T13:00:00.000Z"
 *
 * 3. Library (dayjs, Luxon) handle DST tốt hơn manual calculation
 *    - dayjs.tz('2024-01-15 09:00', 'America/New_York') → Tự động dùng EST
 *    - dayjs.tz('2024-07-15 09:00', 'America/New_York') → Tự động dùng EDT
 *    - Không cần tính offset thủ công!
 *
 * 4. Best Practice cho recurring events:
 *    - Lưu UTC time của lần đầu tiên
 *    - Lưu timezone định nghĩa event
 *    - Generate occurrences bằng timestamp arithmetic
 *    - Display bằng timezone đã lưu
 */
```

---

### **⭐ DAY.JS BEST PRACTICES - Xử Lý Thời Gian Đúng Cách**

#### **🔧 Setup Đúng Cách**

```typescript
// =====================================
// STEP 1: Install & Import Plugins Cần Thiết
// =====================================

// npm install dayjs

import dayjs from 'dayjs';
import utc from 'dayjs/plugin/utc';
import timezone from 'dayjs/plugin/timezone';
import customParseFormat from 'dayjs/plugin/customParseFormat';
import isSameOrBefore from 'dayjs/plugin/isSameOrBefore';
import isSameOrAfter from 'dayjs/plugin/isSameOrAfter';
import advancedFormat from 'dayjs/plugin/advancedFormat';
import relativeTime from 'dayjs/plugin/relativeTime';
import duration from 'dayjs/plugin/duration';
import weekday from 'dayjs/plugin/weekday';
import isoWeek from 'dayjs/plugin/isoWeek';
import 'dayjs/locale/vi'; // Locale tiếng Việt

// ✅ EXTEND PLUGINS (Làm 1 lần duy nhất, nên để trong setup file)
dayjs.extend(utc);
dayjs.extend(timezone);
dayjs.extend(customParseFormat);
dayjs.extend(isSameOrBefore);
dayjs.extend(isSameOrAfter);
dayjs.extend(advancedFormat);
dayjs.extend(relativeTime);
dayjs.extend(duration);
dayjs.extend(weekday);
dayjs.extend(isoWeek);

// Set locale mặc định
dayjs.locale('vi');

// ✅ Set default timezone (optional, nên để user chọn)
dayjs.tz.setDefault('Asia/Ho_Chi_Minh');
```

---

#### **❌ LỖI #1: Parse String Sai Format**

```typescript
// =====================================
// PROBLEMATIC CODE
// =====================================

// ❌ SAI: Parse string không rõ ràng format
const date1 = dayjs('15/01/2024');
// → Invalid Date (dayjs không hiểu DD/MM/YYYY mặc định)

const date2 = dayjs('2024-01-15');
// → Có thể đúng, nhưng không chỉ định timezone → risky!

const date3 = dayjs('01/15/2024');
// → Browser Mỹ hiểu MM/DD/YYYY, browser Việt Nam có thể sai!

// =====================================
// ✅ CORRECT: Chỉ định format rõ ràng
// =====================================

// ✅ Parse với format string
const correctDate1 = dayjs('15/01/2024', 'DD/MM/YYYY');
console.log(correctDate1.format('YYYY-MM-DD')); // "2024-01-15"

// ✅ Parse ISO 8601 (preferred cho API)
const correctDate2 = dayjs('2024-01-15T14:30:00.000Z');
console.log(correctDate2.isValid()); // true

// ✅ Parse với timezone
const correctDate3 = dayjs.tz('2024-01-15 14:30', 'Asia/Ho_Chi_Minh');
console.log(correctDate3.format()); // "2024-01-15T14:30:00+07:00"

// ✅ Parse multiple formats (tự động detect)
const flexibleParse = dayjs(
  '15-01-2024',
  ['DD/MM/YYYY', 'DD-MM-YYYY', 'YYYY-MM-DD'],
  true
); // strict mode = true
```

---

#### **❌ LỖI #2: Không Xử Lý Múi Giờ Đúng Cách**

```typescript
// =====================================
// PROBLEMATIC CODE
// =====================================

// ❌ SAI: Không chỉ định timezone
const now = dayjs(); // Local timezone của browser/server
// User Vietnam: "2024-01-15T21:30:00+07:00"
// User US:      "2024-01-15T09:30:00-05:00"
// → Khác nhau!

// ❌ SAI: Lưu local time vào database
await db.save({
  createdAt: dayjs().format('YYYY-MM-DD HH:mm:ss'),
  // → Lưu "2024-01-15 21:30:00" (không có timezone info)
  // → Không biết đây là timezone nào!
});

// ❌ SAI: Display UTC time cho user
const utcTime = dayjs.utc();
console.log(utcTime.format('HH:mm')); // "14:30" (UTC)
// User Vietnam thấy "14:30" → Confused! Nên là 21:30

// =====================================
// ✅ CORRECT: Xử lý timezone đúng
// =====================================

// ✅ RULE 1: Luôn lưu UTC vào database
await db.save({
  createdAt: dayjs().utc().toISOString(),
  // → "2024-01-15T14:30:00.000Z" (UTC, có 'Z' suffix)
});

// Hoặc dùng timestamp
await db.save({
  createdAt: dayjs().valueOf(), // 1705329000000 (milliseconds)
});

// ✅ RULE 2: Convert UTC → Local timezone khi display
const dbTime = '2024-01-15T14:30:00.000Z'; // UTC từ database

// Display cho user Vietnam
const vnTime = dayjs(dbTime).tz('Asia/Ho_Chi_Minh');
console.log(vnTime.format('DD/MM/YYYY HH:mm')); // "15/01/2024 21:30"

// Display cho user New York
const nyTime = dayjs(dbTime).tz('America/New_York');
console.log(nyTime.format('MM/DD/YYYY hh:mm A')); // "01/15/2024 09:30 AM"

// ✅ RULE 3: User input → Convert to UTC trước khi save
function saveUserSelectedDate(dateString: string, userTimezone: string) {
  // User chọn: "15/01/2024 21:30" (Vietnam time)
  const localDate = dayjs.tz(dateString, 'DD/MM/YYYY HH:mm', userTimezone);

  // Convert to UTC
  const utcDate = localDate.utc();

  // Save to database
  return db.save({
    scheduledAt: utcDate.toISOString(), // "2024-01-15T14:30:00.000Z"
  });
}

// ✅ RULE 4: So sánh thời gian → Dùng UTC hoặc timestamp
const date1 = dayjs('2024-01-15T21:30:00+07:00'); // Vietnam
const date2 = dayjs('2024-01-15T09:30:00-05:00'); // New York

// So sánh trực tiếp (dayjs tự động normalize)
console.log(date1.isSame(date2)); // true (cùng 1 thời điểm!)

// Hoặc dùng timestamp
console.log(date1.valueOf() === date2.valueOf()); // true
```

---

#### **❌ LỖI #3: Format String Sai**

```typescript
// =====================================
// PROBLEMATIC CODE
// =====================================

// ❌ SAI: Format tokens không đúng
const date = dayjs('2024-01-15T14:30:00Z');

console.log(date.format('yyyy-mm-dd'));
// → "2024-30-15" (SAI! mm = minutes, không phải month)

console.log(date.format('DD/MM/YY HH:MM'));
// → "15/01/24 14:30" (MM = month, không phải minute!)

// ❌ SAI: Nhầm lẫn 12h vs 24h
console.log(date.format('hh:mm')); // "02:30" (12h format, thiếu AM/PM)
console.log(date.format('HH:mm')); // "14:30" (24h format) ✅

// =====================================
// ✅ CORRECT: Format tokens đúng
// =====================================

// Cheat Sheet: Format Tokens
const now = dayjs('2024-01-15T14:30:45.123Z');

// YEAR
console.log(now.format('YYYY')); // "2024" - 4 digits
console.log(now.format('YY')); // "24"   - 2 digits

// MONTH
console.log(now.format('MM')); // "01"      - 2 digits
console.log(now.format('M')); // "1"       - 1-2 digits
console.log(now.format('MMM')); // "Jan"     - Short name
console.log(now.format('MMMM')); // "January" - Full name

// DAY
console.log(now.format('DD')); // "15" - 2 digits
console.log(now.format('D')); // "15" - 1-2 digits

// HOUR
console.log(now.format('HH')); // "14" - 24h format (00-23)
console.log(now.format('H')); // "14" - 24h format (0-23)
console.log(now.format('hh')); // "02" - 12h format (01-12)
console.log(now.format('h')); // "2"  - 12h format (1-12)

// MINUTE
console.log(now.format('mm')); // "30" - Always 2 digits
console.log(now.format('m')); // "30" - 1-2 digits

// SECOND
console.log(now.format('ss')); // "45" - Always 2 digits
console.log(now.format('s')); // "45" - 1-2 digits

// MILLISECOND
console.log(now.format('SSS')); // "123" - 3 digits

// AM/PM
console.log(now.format('A')); // "PM"
console.log(now.format('a')); // "pm"

// TIMEZONE
console.log(now.format('Z')); // "+00:00" - Offset
console.log(now.format('ZZ')); // "+0000"  - Offset compact

// ✅ Common Format Patterns
const vnDate = dayjs().tz('Asia/Ho_Chi_Minh');

// Ngày Việt Nam: "15/01/2024"
console.log(vnDate.format('DD/MM/YYYY'));

// Ngày Mỹ: "01/15/2024"
console.log(vnDate.format('MM/DD/YYYY'));

// ISO 8601: "2024-01-15T21:30:45+07:00"
console.log(vnDate.format());

// Custom: "15 tháng 01, 2024 lúc 21:30"
vnDate.locale('vi');
console.log(vnDate.format('DD [tháng] MM, YYYY [lúc] HH:mm'));

// Timestamp: "15 Jan 2024, 9:30 PM"
console.log(vnDate.format('DD MMM YYYY, h:mm A'));

// Full: "Thứ Hai, 15 tháng 01 năm 2024, 21:30:45"
console.log(vnDate.format('dddd, DD [tháng] MM [năm] YYYY, HH:mm:ss'));
```

---

#### **✅ BEST PRACTICE #1: Utility Functions**

```typescript
// =====================================
// dateUtils.ts - Reusable Helper Functions
// =====================================

import dayjs, { Dayjs } from 'dayjs';

/**
 * Parse date từ API (luôn UTC)
 */
export function parseApiDate(dateString: string): Dayjs {
  return dayjs.utc(dateString);
}

/**
 * Format date cho display (auto convert to user timezone)
 */
export function formatForDisplay(
  date: string | Dayjs,
  userTimezone: string = 'Asia/Ho_Chi_Minh',
  format: string = 'DD/MM/YYYY HH:mm'
): string {
  return dayjs(date).tz(userTimezone).format(format);
}

/**
 * Convert user input to UTC (để save vào database)
 */
export function userInputToUTC(
  dateString: string,
  userTimezone: string,
  inputFormat: string = 'DD/MM/YYYY HH:mm'
): string {
  return dayjs.tz(dateString, inputFormat, userTimezone).utc().toISOString();
}

/**
 * Check if date is in the past
 */
export function isPast(date: string | Dayjs): boolean {
  return dayjs(date).isBefore(dayjs());
}

/**
 * Get relative time ("2 giờ trước", "3 ngày nữa")
 */
export function getRelativeTime(
  date: string | Dayjs,
  locale: string = 'vi'
): string {
  return dayjs(date).locale(locale).fromNow();
}

/**
 * Format date range
 */
export function formatDateRange(
  start: string | Dayjs,
  end: string | Dayjs,
  timezone: string = 'Asia/Ho_Chi_Minh'
): string {
  const startDate = dayjs(start).tz(timezone);
  const endDate = dayjs(end).tz(timezone);

  // Cùng ngày
  if (startDate.isSame(endDate, 'day')) {
    return `${startDate.format('DD/MM/YYYY')} (${startDate.format(
      'HH:mm'
    )} - ${endDate.format('HH:mm')})`;
  }

  // Khác ngày
  return `${startDate.format('DD/MM/YYYY HH:mm')} - ${endDate.format(
    'DD/MM/YYYY HH:mm'
  )}`;
}

/**
 * Validate date string
 */
export function isValidDate(dateString: string, format?: string): boolean {
  if (format) {
    return dayjs(dateString, format, true).isValid();
  }
  return dayjs(dateString).isValid();
}

/**
 * Get start/end of day in UTC
 */
export function getStartOfDayUTC(date?: string | Dayjs): Dayjs {
  return dayjs(date).utc().startOf('day');
}

export function getEndOfDayUTC(date?: string | Dayjs): Dayjs {
  return dayjs(date).utc().endOf('day');
}

/**
 * Calculate business days between 2 dates
 */
export function getBusinessDays(
  start: string | Dayjs,
  end: string | Dayjs
): number {
  let current = dayjs(start);
  const endDate = dayjs(end);
  let businessDays = 0;

  while (current.isSameOrBefore(endDate, 'day')) {
    // Weekday 0 = Sunday, 6 = Saturday
    if (current.day() !== 0 && current.day() !== 6) {
      businessDays++;
    }
    current = current.add(1, 'day');
  }

  return businessDays;
}
```

---

#### **✅ BEST PRACTICE #2: React Component Examples**

```typescript
// =====================================
// DateDisplay.tsx - Hiển thị thời gian
// =====================================

import React from 'react';
import dayjs from 'dayjs';
import { formatForDisplay, getRelativeTime } from './dateUtils';

interface DateDisplayProps {
  date: string; // ISO 8601 UTC từ API
  timezone?: string;
  showRelative?: boolean;
}

export const DateDisplay: React.FC<DateDisplayProps> = ({
  date,
  timezone = 'Asia/Ho_Chi_Minh',
  showRelative = false,
}) => {
  // ✅ Always validate date
  if (!dayjs(date).isValid()) {
    return <span className="text-red-500">Invalid date</span>;
  }

  const formatted = formatForDisplay(date, timezone);
  const relative = getRelativeTime(date);

  return (
    <time dateTime={date} title={formatted}>
      {showRelative ? relative : formatted}
    </time>
  );
};

// Usage:
// <DateDisplay date="2024-01-15T14:30:00.000Z" showRelative />
// → "2 giờ trước"

// =====================================
// DatePicker.tsx - User chọn ngày giờ
// =====================================

import React, { useState } from 'react';
import dayjs from 'dayjs';
import { userInputToUTC } from './dateUtils';

interface DatePickerProps {
  onDateChange: (utcDate: string) => void;
  timezone?: string;
}

export const DatePicker: React.FC<DatePickerProps> = ({
  onDateChange,
  timezone = 'Asia/Ho_Chi_Minh',
}) => {
  const [dateInput, setDateInput] = useState('');
  const [timeInput, setTimeInput] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = () => {
    try {
      // ✅ Validate input
      const inputString = `${dateInput} ${timeInput}`;
      if (!dayjs(inputString, 'DD/MM/YYYY HH:mm', true).isValid()) {
        setError('Ngày giờ không hợp lệ');
        return;
      }

      // ✅ Convert to UTC
      const utcDate = userInputToUTC(inputString, timezone);

      // ✅ Pass UTC date to parent
      onDateChange(utcDate);
      setError('');
    } catch (err) {
      setError('Lỗi xử lý ngày giờ');
    }
  };

  return (
    <div>
      <input
        type="text"
        placeholder="DD/MM/YYYY"
        value={dateInput}
        onChange={(e) => setDateInput(e.target.value)}
      />
      <input
        type="text"
        placeholder="HH:mm"
        value={timeInput}
        onChange={(e) => setTimeInput(e.target.value)}
      />
      <button onClick={handleSubmit}>Submit</button>
      {error && <p className="error">{error}</p>}
    </div>
  );
};

// =====================================
// ScheduleList.tsx - Hiển thị lịch trình
// =====================================

interface Schedule {
  id: string;
  title: string;
  startTime: string; // UTC ISO string
  endTime: string;
}

export const ScheduleList: React.FC<{ schedules: Schedule[] }> = ({
  schedules,
}) => {
  const userTimezone = 'Asia/Ho_Chi_Minh';

  // ✅ Sort by time
  const sorted = [...schedules].sort((a, b) =>
    dayjs(a.startTime).diff(dayjs(b.startTime))
  );

  // ✅ Group by date
  const grouped = sorted.reduce((acc, schedule) => {
    const date = dayjs(schedule.startTime)
      .tz(userTimezone)
      .format('YYYY-MM-DD');

    if (!acc[date]) acc[date] = [];
    acc[date].push(schedule);
    return acc;
  }, {} as Record<string, Schedule[]>);

  return (
    <div>
      {Object.entries(grouped).map(([date, items]) => (
        <div key={date}>
          <h3>{dayjs(date).format('DD/MM/YYYY - dddd')}</h3>
          {items.map((item) => (
            <div key={item.id}>
              <span>{item.title}</span>
              <span>
                {formatDateRange(item.startTime, item.endTime, userTimezone)}
              </span>
            </div>
          ))}
        </div>
      ))}
    </div>
  );
};
```

---

#### **✅ BEST PRACTICE #3: API Integration**

```typescript
// =====================================
// api.ts - API Request/Response
// =====================================

import dayjs from 'dayjs';

// ✅ Type-safe date handling
interface ApiEvent {
  id: string;
  title: string;
  startTime: string; // Always ISO 8601 UTC
  endTime: string;
  createdAt: string;
  updatedAt: string;
}

// ✅ Create event: Convert user input to UTC
export async function createEvent(data: {
  title: string;
  startTime: string; // User's local time string
  endTime: string;
  timezone: string;
}) {
  // Convert to UTC before sending
  const payload = {
    title: data.title,
    startTime: dayjs.tz(data.startTime, data.timezone).utc().toISOString(),
    endTime: dayjs.tz(data.endTime, data.timezone).utc().toISOString(),
  };

  const response = await fetch('/api/events', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });

  return response.json();
}

// ✅ Fetch events: Receive UTC, display in user timezone
export async function getEvents(userTimezone: string) {
  const response = await fetch('/api/events');
  const events: ApiEvent[] = await response.json();

  // Transform for display
  return events.map((event) => ({
    ...event,
    displayStart: dayjs(event.startTime)
      .tz(userTimezone)
      .format('DD/MM/YYYY HH:mm'),
    displayEnd: dayjs(event.endTime)
      .tz(userTimezone)
      .format('DD/MM/YYYY HH:mm'),
  }));
}

// ✅ Filter events by date range (UTC)
export async function getEventsBetween(
  start: string,
  end: string,
  userTimezone: string
) {
  // Convert user's local dates to UTC for API query
  const startUTC = dayjs
    .tz(start, 'DD/MM/YYYY', userTimezone)
    .startOf('day')
    .utc()
    .toISOString();

  const endUTC = dayjs
    .tz(end, 'DD/MM/YYYY', userTimezone)
    .endOf('day')
    .utc()
    .toISOString();

  const response = await fetch(`/api/events?start=${startUTC}&end=${endUTC}`);

  return response.json();
}
```

---

#### **✅ BEST PRACTICE #4: Testing**

```typescript
// =====================================
// dateUtils.test.ts - Unit tests
// =====================================

import dayjs from 'dayjs';
import {
  parseApiDate,
  formatForDisplay,
  userInputToUTC,
  isValidDate,
} from './dateUtils';

describe('dateUtils', () => {
  // ✅ Mock current time for consistent tests
  beforeAll(() => {
    jest.useFakeTimers();
    jest.setSystemTime(new Date('2024-01-15T14:30:00.000Z'));
  });

  afterAll(() => {
    jest.useRealTimers();
  });

  describe('parseApiDate', () => {
    it('should parse UTC ISO string correctly', () => {
      const date = parseApiDate('2024-01-15T14:30:00.000Z');
      expect(date.utc().format()).toBe('2024-01-15T14:30:00Z');
    });
  });

  describe('formatForDisplay', () => {
    it('should convert UTC to Vietnam timezone', () => {
      const utcDate = '2024-01-15T14:30:00.000Z';
      const result = formatForDisplay(utcDate, 'Asia/Ho_Chi_Minh');
      expect(result).toBe('15/01/2024 21:30'); // UTC+7
    });

    it('should convert UTC to New York timezone', () => {
      const utcDate = '2024-01-15T14:30:00.000Z';
      const result = formatForDisplay(utcDate, 'America/New_York');
      expect(result).toBe('15/01/2024 09:30'); // UTC-5
    });
  });

  describe('userInputToUTC', () => {
    it('should convert Vietnam time to UTC', () => {
      const vnTime = '15/01/2024 21:30';
      const result = userInputToUTC(vnTime, 'Asia/Ho_Chi_Minh');
      expect(result).toBe('2024-01-15T14:30:00.000Z');
    });
  });

  describe('isValidDate', () => {
    it('should validate correct format', () => {
      expect(isValidDate('15/01/2024', 'DD/MM/YYYY')).toBe(true);
      expect(isValidDate('32/01/2024', 'DD/MM/YYYY')).toBe(false);
      expect(isValidDate('15/13/2024', 'DD/MM/YYYY')).toBe(false);
    });
  });
});
```

---

#### **🎯 Checklist: Tránh Lỗi Thời Gian**

```typescript
// =====================================
// ✅ CHECKLIST TRƯỚC KHI DEPLOY
// =====================================

// [ ] Đã install đầy đủ plugins cần thiết?
import utc from 'dayjs/plugin/utc';
import timezone from 'dayjs/plugin/timezone';
dayjs.extend(utc);
dayjs.extend(timezone);

// [ ] Luôn lưu UTC vào database?
const dbDate = dayjs().utc().toISOString(); // ✅
// KHÔNG: dayjs().format() // ❌

// [ ] Parse date với format rõ ràng?
dayjs('15/01/2024', 'DD/MM/YYYY'); // ✅
// KHÔNG: dayjs('15/01/2024') // ❌

// [ ] Convert timezone khi display?
dayjs(dbDate).tz('Asia/Ho_Chi_Minh').format(); // ✅

// [ ] Validate date input từ user?
if (!dayjs(input, 'DD/MM/YYYY', true).isValid()) {
  throw new Error('Invalid date');
}

// [ ] Handle Daylight Saving Time (DST)?
// dayjs tự động handle nếu dùng timezone plugin

// [ ] Test với multiple timezones?
// Test với Asia/Ho_Chi_Minh, America/New_York, Europe/London

// [ ] Consistent format trong toàn app?
// Tạo constants cho formats
const DATE_FORMAT = 'DD/MM/YYYY';
const DATETIME_FORMAT = 'DD/MM/YYYY HH:mm';
const API_FORMAT = 'YYYY-MM-DDTHH:mm:ss.SSSZ';
```

---

#### **🚀 Temporal API (Future)**

```typescript
import { Temporal } from '@js-temporal/polyfill';

// ✅ Instant (UTC)
const instant = Temporal.Instant.from('2024-01-15T14:30:00Z');

// ✅ ZonedDateTime (Timezone-aware)
const vnTime = instant.toZonedDateTimeISO('Asia/Ho_Chi_Minh');
console.log(vnTime.toString()); // "2024-01-15T21:30:00+07:00[Asia/Ho_Chi_Minh]"

// ✅ Immutable, No month zero-indexing, Better API
```

---

#### **🎯 Best Practices**

**✅ DO:**

```typescript
// Store UTC
{
  createdAt: '2024-01-15T14:30:00.000Z';
}

// Compare timestamps
date1.getTime() > date2.getTime();

// Use library
import { format, parseISO } from 'date-fns';
```

**❌ DON'T:**

```typescript
// ❌ Store without timezone
{
  date: '2024-01-15';
} // Ambiguous!

// ❌ Use local Date
new Date(); // Timezone-dependent!

// ❌ Compare dates with ===
date1 === date2; // Always false

// ❌ Mutate
date.setMonth(2); // Side effect!
```

**💡 Key Takeaway:**

- **Store UTC** → **Display Local**
- Dùng **timestamp** cho comparison
- Dùng **library** (date-fns/Luxon/Day.js)
- **Temporal API** = future standard

---

## **🏛️ PRODUCTION PATTERNS - CÁC MẪu THIẾT KẾ SẢN XUẤT**

### **📦 Pattern 1: API Date Transfer Object (DTO)**

```typescript
/**
 * 🎯 GOAL: Chuẩn hóa date format giữa client-server
 * - Client gửi: ISO 8601 UTC
 * - Server trả về: ISO 8601 UTC
 * - Client convert → local timezone để hiển thị
 */

// 🔗 Backend API Response (NestJS)
class OrderResponseDto {
  id: string;

  @ApiProperty({
    type: String,
    format: 'date-time',
    example: '2024-01-15T14:30:00.000Z',
  })
  createdAt: string; // 💡 ISO 8601 UTC string

  @ApiProperty({ type: String, format: 'date-time' })
  updatedAt: string;

  @ApiProperty({ type: String, format: 'date-time', nullable: true })
  completedAt?: string; // 💡 Optional: Chưa hoàn thành = null
}

// 🌐 Frontend Type
interface Order {
  id: string;
  createdAt: Date; // 💡 Convert string → Date object
  updatedAt: Date;
  completedAt?: Date;
}

// 🔄 Transform API response → Domain model
const parseOrderFromAPI = (dto: OrderResponseDto): Order => {
  return {
    id: dto.id,
    createdAt: new Date(dto.createdAt), // 💡 Parse ISO string
    updatedAt: new Date(dto.updatedAt),
    completedAt: dto.completedAt ? new Date(dto.completedAt) : undefined,
  };
};

// 🔄 Transform Domain model → API request
const serializeOrderForAPI = (order: Order): OrderResponseDto => {
  return {
    id: order.id,
    createdAt: order.createdAt.toISOString(), // 💡 Date → ISO string
    updatedAt: order.updatedAt.toISOString(),
    completedAt: order.completedAt?.toISOString(),
  };
};

// 🚀 Axios interceptor: Auto-parse dates
axios.interceptors.response.use((response) => {
  // 🔍 Find all ISO date strings in response
  const isoDateRegex = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{3})?Z$/;

  const parseDates = (obj: any): any => {
    if (obj === null || obj === undefined) return obj;

    if (typeof obj === 'string' && isoDateRegex.test(obj)) {
      return new Date(obj); // 🔄 Convert ISO string → Date
    }

    if (Array.isArray(obj)) {
      return obj.map(parseDates);
    }

    if (typeof obj === 'object') {
      return Object.fromEntries(
        Object.entries(obj).map(([key, value]) => [key, parseDates(value)])
      );
    }

    return obj;
  };

  response.data = parseDates(response.data);
  return response;
});

/**
 * ✅ BENEFITS:
 * - Tự động parse tất cả ISO strings → Date objects
 * - Không cần parse thủ công ở mỗi API call
 * - Type-safe: Response luôn có Date objects
 */
```

---

### **🔐 Pattern 2: Date Validation Schema (Zod)**

```typescript
/**
 * 🎯 GOAL: Validate date inputs từ user
 * - Check format
 * - Check range (min/max)
 * - Check business rules
 */

import { z } from 'zod';

// 📋 Date schema basics
const DateSchema = z
  .string()
  .datetime({ message: 'Phải là ISO 8601 format' })
  .transform((val) => new Date(val)); // 🔄 Auto-convert to Date

// 📊 Date range schema
const BirthdateSchema = z
  .string()
  .datetime()
  .transform((val) => new Date(val))
  .refine(
    (date) => {
      const age =
        (Date.now() - date.getTime()) / (365.25 * 24 * 60 * 60 * 1000);
      return age >= 18 && age <= 120; // 💡 18-120 tuổi
    },
    { message: 'Tuổi phải từ 18-120' }
  );

// 📋 Booking schema (start < end)
const BookingSchema = z
  .object({
    checkIn: z
      .string()
      .datetime()
      .transform((val) => new Date(val)),
    checkOut: z
      .string()
      .datetime()
      .transform((val) => new Date(val)),
  })
  .refine((data) => data.checkOut.getTime() > data.checkIn.getTime(), {
    message: 'Ngày check-out phải sau check-in',
    path: ['checkOut'], // 💡 Error vào field checkOut
  })
  .refine(
    (data) => {
      const daysDiff =
        (data.checkOut.getTime() - data.checkIn.getTime()) /
        (24 * 60 * 60 * 1000);
      return daysDiff <= 30; // 💡 Tối đa 30 ngày
    },
    { message: 'Đặt phòng tối đa 30 ngày' }
  );

// 📝 Meeting schema (future date only)
const MeetingSchema = z.object({
  title: z.string().min(1),
  scheduledAt: z
    .string()
    .datetime()
    .transform((val) => new Date(val))
    .refine((date) => date.getTime() > Date.now(), {
      message: 'Phải là thời gian tương lai',
    })
    .refine(
      (date) => {
        const hour = date.getHours();
        return hour >= 8 && hour < 18; // 💡 8 AM - 6 PM
      },
      { message: 'Giờ họp phải trong 8h-18h' }
    ),
});

// 🚀 Usage in React Hook Form
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';

const BookingForm = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: zodResolver(BookingSchema),
  });

  const onSubmit = (data: z.infer<typeof BookingSchema>) => {
    // 💡 data.checkIn, data.checkOut là Date objects (validated)
    console.log('Check-in:', data.checkIn.toISOString());
    console.log('Check-out:', data.checkOut.toISOString());
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input type="datetime-local" {...register('checkIn')} />
      {errors.checkIn && <span>{errors.checkIn.message}</span>}

      <input type="datetime-local" {...register('checkOut')} />
      {errors.checkOut && <span>{errors.checkOut.message}</span>}

      <button type="submit">Đặt phòng</button>
    </form>
  );
};
```

---

### **⏰ Pattern 3: Time-based Feature Flags**

```typescript
/**
 * 🎯 GOAL: Bật/tắt features theo thời gian
 * - Tết sale: Từ 01/02 → 15/02
 * - Beta feature: Từ 01/01 → vô hạn
 * - Deprecated feature: Dừng từ 01/03
 */

interface FeatureFlag {
  id: string;
  enabled: boolean;
  startDate?: string; // UTC ISO
  endDate?: string; // UTC ISO
}

// 🚩 Feature flag service
class FeatureFlagService {
  private flags: Map<string, FeatureFlag> = new Map();

  constructor(flags: FeatureFlag[]) {
    flags.forEach((flag) => this.flags.set(flag.id, flag));
  }

  isEnabled(flagId: string): boolean {
    const flag = this.flags.get(flagId);
    if (!flag) return false;
    if (!flag.enabled) return false;

    const now = Date.now();

    // 💡 Check start date
    if (flag.startDate) {
      const start = new Date(flag.startDate).getTime();
      if (now < start) return false; // Chưa đến giờ
    }

    // 💡 Check end date
    if (flag.endDate) {
      const end = new Date(flag.endDate).getTime();
      if (now > end) return false; // Đã quá giờ
    }

    return true;
  }
}

// 📊 Setup flags
const featureFlags = new FeatureFlagService([
  {
    id: 'tet-sale-2024',
    enabled: true,
    startDate: '2024-02-01T00:00:00.000Z', // 01/02 00:00 UTC
    endDate: '2024-02-15T23:59:59.999Z', // 15/02 23:59 UTC
  },
  {
    id: 'new-checkout-flow',
    enabled: true,
    startDate: '2024-01-01T00:00:00.000Z', // Bắt đầu từ 01/01
    // No endDate = permanent
  },
  {
    id: 'old-payment-gateway',
    enabled: false, // ❌ Disabled manually
    endDate: '2024-03-01T00:00:00.000Z', // Dừng từ 01/03
  },
]);

// 🚀 Usage in React
const CheckoutPage = () => {
  const showTetSale = featureFlags.isEnabled('tet-sale-2024');
  const useNewCheckout = featureFlags.isEnabled('new-checkout-flow');

  return (
    <div>
      {showTetSale && <Banner>🎉 Tết Sale - Giảm đến 50%!</Banner>}

      {useNewCheckout ? <NewCheckoutFlow /> : <OldCheckoutFlow />}
    </div>
  );
};

/**
 * ✅ BENEFITS:
 * - Tự động bật/tắt features theo thời gian
 * - Không cần deploy để enable/disable
 * - A/B testing theo thời gian
 */
```

---

### **🔍 Pattern 4: Date Caching & Memoization**

```typescript
/**
 * 🎯 GOAL: Cache expensive date calculations
 * - Format dates (Intl.DateTimeFormat)
 * - Relative time ("2 hours ago")
 * - Business days calculation
 */

import { useMemo } from 'react';

// 📊 Expensive: Format date
const ExpensiveComponent = ({ dates }: { dates: Date[] }) => {
  // ❌ BAD: Format mỗi render
  return (
    <ul>
      {dates.map((date) => (
        <li key={date.getTime()}>
          {new Intl.DateTimeFormat('vi-VN', {
            dateStyle: 'long',
            timeStyle: 'short',
          }).format(date)}
          {/* 💡 Tạo Intl.DateTimeFormat mới mỗi item! */}
        </li>
      ))}
    </ul>
  );
};

// ✅ GOOD: Cache formatter
const OptimizedComponent = ({ dates }: { dates: Date[] }) => {
  // 💡 Tầo formatter 1 lần, reuse cho tất cả
  const formatter = useMemo(
    () =>
      new Intl.DateTimeFormat('vi-VN', {
        dateStyle: 'long',
        timeStyle: 'short',
      }),
    [] // Empty deps = tạo 1 lần duy nhất
  );

  return (
    <ul>
      {dates.map((date) => (
        <li key={date.getTime()}>{formatter.format(date)}</li>
      ))}
    </ul>
  );
};

// 📊 Cache relative time
const useRelativeTime = (date: Date, updateInterval = 60000) => {
  const [relativeTime, setRelativeTime] = useState('');

  useEffect(() => {
    const updateTime = () => {
      const now = Date.now();
      const diff = now - date.getTime();
      const minutes = Math.floor(diff / 60000);
      const hours = Math.floor(minutes / 60);
      const days = Math.floor(hours / 24);

      if (minutes < 1) {
        setRelativeTime('Vừa xong');
      } else if (minutes < 60) {
        setRelativeTime(`${minutes} phút trước`);
      } else if (hours < 24) {
        setRelativeTime(`${hours} giờ trước`);
      } else if (days < 7) {
        setRelativeTime(`${days} ngày trước`);
      } else {
        setRelativeTime(date.toLocaleDateString('vi-VN'));
      }
    };

    updateTime(); // Initial
    const interval = setInterval(updateTime, updateInterval);
    // 💡 Update mỗi 60s (hoặc custom interval)

    return () => clearInterval(interval);
  }, [date, updateInterval]);

  return relativeTime;
};

// Usage
const CommentItem = ({
  comment,
}: {
  comment: { createdAt: Date; text: string };
}) => {
  const relativeTime = useRelativeTime(comment.createdAt);

  return (
    <div>
      <p>{comment.text}</p>
      <span>{relativeTime}</span>
      {/* 💡 "2 giờ trước" → auto-update mỗi 60s */}
    </div>
  );
};
```

---

## **🧪 TESTING DATE/TIME CODE - KIỂM THỬ**

### **⏰ Mock Current Time (Jest/Vitest)**

```typescript
/**
 * 🎯 GOAL: Test code phụ thuộc vào current time
 * - Mock Date.now()
 * - Mock new Date()
 * - Test time-based logic
 */

// 📋 Code to test
const isWeekend = (date: Date = new Date()): boolean => {
  const day = date.getDay();
  return day === 0 || day === 6; // Sunday = 0, Saturday = 6
};

const getGreeting = (): string => {
  const hour = new Date().getHours();
  if (hour < 12) return 'Chào buổi sáng';
  if (hour < 18) return 'Chào buổi chiều';
  return 'Chào buổi tối';
};

// 🧪 Test with mocked time
describe('Date utilities', () => {
  beforeEach(() => {
    // 🔐 Enable fake timers
    vi.useFakeTimers();
  });

  afterEach(() => {
    // 🔓 Restore real timers
    vi.useRealTimers();
  });

  it('should detect weekend', () => {
    // 💡 Mock: Saturday, Jan 13, 2024
    vi.setSystemTime(new Date('2024-01-13T10:00:00.000Z'));

    expect(isWeekend()).toBe(true); // ✅ Saturday
  });

  it('should detect weekday', () => {
    // 💡 Mock: Monday, Jan 15, 2024
    vi.setSystemTime(new Date('2024-01-15T10:00:00.000Z'));

    expect(isWeekend()).toBe(false); // ✅ Monday
  });

  it('should greet morning', () => {
    // 💡 Mock: 9:00 AM
    vi.setSystemTime(new Date('2024-01-15T02:00:00.000Z')); // 9 AM Vietnam (UTC+7)

    expect(getGreeting()).toBe('Chào buổi sáng');
  });

  it('should greet evening', () => {
    // 💡 Mock: 8:00 PM
    vi.setSystemTime(new Date('2024-01-15T13:00:00.000Z')); // 8 PM Vietnam

    expect(getGreeting()).toBe('Chào buổi tối');
  });
});

// 📊 Test time progression
describe('Countdown timer', () => {
  it('should countdown correctly', () => {
    vi.useFakeTimers();

    const targetTime = Date.now() + 10000; // +10 seconds
    const callback = vi.fn();

    // Start countdown
    const interval = setInterval(() => {
      const timeLeft = targetTime - Date.now();
      if (timeLeft <= 0) {
        clearInterval(interval);
        callback();
      }
    }, 1000);

    // 💡 Fast-forward 5 seconds
    vi.advanceTimersByTime(5000);
    expect(callback).not.toHaveBeenCalled(); // Chưa hết 10s

    // 💡 Fast-forward thêm 5 seconds (total 10s)
    vi.advanceTimersByTime(5000);
    expect(callback).toHaveBeenCalled(); // ✅ Đã hết 10s

    vi.useRealTimers();
  });
});
```

---

### **🌍 Test Timezone-dependent Code**

```typescript
/**
 * 🎯 GOAL: Test code với nhiều timezones
 * - Mock timezone
 * - Test DST transitions
 * - Test edge cases
 */

// 📋 Code to test
const formatLocalTime = (date: Date): string => {
  return date.toLocaleString('vi-VN', {
    timeZone: 'Asia/Ho_Chi_Minh',
    dateStyle: 'short',
    timeStyle: 'short',
  });
};

const getBusinessHours = (date: Date): { start: Date; end: Date } => {
  const start = new Date(date);
  start.setHours(9, 0, 0, 0); // 9 AM

  const end = new Date(date);
  end.setHours(18, 0, 0, 0); // 6 PM

  return { start, end };
};

// 🧪 Tests
describe('Timezone handling', () => {
  it('should format Vietnam time correctly', () => {
    const utcDate = new Date('2024-01-15T14:30:00.000Z'); // 14:30 UTC

    const formatted = formatLocalTime(utcDate);
    expect(formatted).toContain('21:30'); // 14:30 UTC + 7 = 21:30 Vietnam
  });

  it('should handle business hours in Vietnam timezone', () => {
    // 💡 Input: Jan 15, 2024 (any time)
    const date = new Date('2024-01-15T10:00:00.000Z');

    const { start, end } = getBusinessHours(date);

    // 💡 Expected: 9 AM and 6 PM same day (local time)
    expect(start.getHours()).toBe(9);
    expect(end.getHours()).toBe(18);
    expect(start.getDate()).toBe(date.getDate());
  });

  it('should handle DST transition (US timezone)', () => {
    // 💡 DST start: March 10, 2024 2:00 AM → 3:00 AM (US)
    const beforeDST = new Date('2024-03-10T06:59:00.000Z'); // 1:59 AM EST (UTC-5)
    const afterDST = new Date('2024-03-10T07:01:00.000Z'); // 3:01 AM EDT (UTC-4)

    // 💡 Test: 2:00-3:00 AM không tồn tại!
    const missing = new Date('2024-03-10T07:00:00.000Z'); // Should be 3:00 AM
    expect(missing.getHours()).toBe(3); // Skipped 2:00 AM
  });
});

// 💡 Test with different locales
describe('Locale formatting', () => {
  const testCases = [
    { locale: 'vi-VN', expected: '15/01/2024' },
    { locale: 'en-US', expected: '1/15/2024' },
    { locale: 'en-GB', expected: '15/01/2024' },
  ];

  testCases.forEach(({ locale, expected }) => {
    it(`should format date in ${locale}`, () => {
      const date = new Date('2024-01-15T00:00:00.000Z');
      const formatted = date.toLocaleDateString(locale);
      expect(formatted).toBe(expected);
    });
  });
});
```

---

### **💡 Test Best Practices**

```typescript
/**
 * ✅ DO:
 */

// 1. Always use fake timers for time-dependent tests
vi.useFakeTimers();
vi.setSystemTime(new Date('2024-01-15'));

// 2. Test edge cases
- Midnight (00:00)
- End of day (23:59)
- DST transitions
- Leap years (Feb 29)
- Month boundaries (Jan 31 + 1 month)

// 3. Use UTC for test fixtures
const testDate = new Date('2024-01-15T14:30:00.000Z');  // ✅ Explicit UTC

// 4. Clean up timers
afterEach(() => {
  vi.useRealTimers();
});

/**
 * ❌ DON'T:
 */

// ❌ Rely on system time
const now = new Date();  // Flaky! Depends on test run time

// ❌ Hardcode timezone offsets
const vietnamTime = utcTime + 7 * 60 * 60 * 1000;  // ❌ Wrong approach

// ❌ Use sleep/delays in tests
await new Promise(resolve => setTimeout(resolve, 1000));  // ❌ Slow!
vi.advanceTimersByTime(1000);  // ✅ Fast!
```

---

## **🚨 COMMON PITFALLS & SOLUTIONS - LỐI THƯỜNG GẶP**

### **🐛 Pitfall 1: Month is Zero-indexed**

```typescript
// ❌ WRONG
const january = new Date(2024, 1, 15); // 💡 Tháng 2 (February)!
console.log(january.getMonth()); // 1 (February)

// ✅ CORRECT
const january = new Date(2024, 0, 15); // Tháng 1 (January)
console.log(january.getMonth()); // 0 (January)

// 💡 GHI NHỌ: Months: 0-11, Days: 1-31
```

---

### **🐛 Pitfall 2: Date Parsing is Browser-dependent**

```typescript
// ❌ RISKY
const date1 = new Date('2024-01-15');
// Chrome: Jan 15, 2024 00:00 UTC
// Safari: Jan 15, 2024 00:00 LOCAL (khác nhau!)

const date2 = new Date('01/15/2024');
// Chrome: Jan 15, 2024 (US format)
// Some browsers: Invalid Date

// ✅ SAFE
const date = new Date('2024-01-15T00:00:00.000Z'); // ISO 8601 UTC
const date = new Date(2024, 0, 15); // Constructor
const date = dayjs('2024-01-15').toDate(); // Library
```

---

### **🐛 Pitfall 3: Mutable Date Objects**

```typescript
// ❌ WRONG
const original = new Date('2024-01-15');
const modified = original;
modified.setDate(20); // Mutate!

console.log(original.getDate()); // 20 (🚨 Original bị thay đổi!)

// ✅ CORRECT
const original = new Date('2024-01-15');
const modified = new Date(original.getTime()); // Clone
modified.setDate(20);

console.log(original.getDate()); // 15 (✅ Original không đổi)
```

---

### **🐛 Pitfall 4: Comparing Dates with === **

```typescript
// ❌ WRONG
const date1 = new Date('2024-01-15');
const date2 = new Date('2024-01-15');

console.log(date1 === date2); // false (💡 Khác object reference!)

// ✅ CORRECT
console.log(date1.getTime() === date2.getTime()); // true
console.log(+date1 === +date2); // true (unary +)
console.log(dayjs(date1).isSame(date2, 'day')); // true (library)
```

---

### **🐛 Pitfall 5: UTC vs Local Confusion**

```typescript
// ❌ WRONG
const date = new Date('2024-01-15T21:00:00.000Z'); // 21:00 UTC
console.log(date.getHours()); // 💡 4 (Vietnam: UTC+7 → 21+7=28 → 4 AM next day)

// ✅ CORRECT
const date = new Date('2024-01-15T21:00:00.000Z');
console.log(date.getUTCHours()); // 21 (UTC time)
console.log(date.getHours()); // 4 (Local time Vietnam)

// 💡 ALWAYS use UTC methods for server timestamps
const year = date.getUTCFullYear();
const month = date.getUTCMonth();
const day = date.getUTCDate();
```

---

## **📊 PERFORMANCE TIPS**

```typescript
/**
 * ✅ FAST:
 */

// 1. Use timestamps for comparison (fastest)
const isAfter = date1.getTime() > date2.getTime();

// 2. Cache Intl.DateTimeFormat
const formatter = new Intl.DateTimeFormat('vi-VN');
const formatted = formatter.format(date); // Reuse formatter

// 3. Avoid repeated date creation
const now = Date.now(); // ✅ Timestamp (fast)
const now = new Date(); // ❌ Object creation (slower)

/**
 * ❌ SLOW:
 */

// ❌ Creating new formatter every time
list.map(
  (date) => new Intl.DateTimeFormat('vi-VN').format(date) // 🐌 Slow!
);

// ❌ Using string operations
const month = dateString.split('-')[1]; // ❌ Error-prone
```

---

**❌ DON'T:**

```typescript
// ❌ Store without timezone
{
  date: '2024-01-15';
} // Ambiguous!

// ❌ Use local Date
new Date(); // Timezone-dependent!

// ❌ Compare dates with ===
date1 === date2; // Always false

// ❌ Mutate
date.setMonth(2); // Side effect!
```

**💡 Key Takeaway:**

- **Store UTC** → **Display Local**
- Dùng **timestamp** cho comparison
- Dùng **library** (date-fns/Luxon/Day.js)
- **Temporal API** = future standard

---

## **🧠 TÓM TẮT & KỸ THUẬT GHI NHỚ NHANH**

### **📌 QUY TẮC 3-3-3 (Nhớ Trong 3 Giây)**

#### **🎯 3 NGUYÊN TẮC VÀNG**

```
1️⃣ LƯU UTC - HIỂN THỊ LOCAL
   Database/API → UTC
   Display → User timezone

2️⃣ DÙNG LIBRARY - TRÁNH NATIVE DATE
   ❌ new Date('2024-01-15')  → Risky!
   ✅ dayjs.utc('2024-01-15') → Safe!

3️⃣ FORMAT RÕ RÀNG - TRÁNH NHẦM LẪN
   ❌ dayjs('15/01/2024')           → Invalid
   ✅ dayjs('15/01/2024', 'DD/MM/YYYY') → Valid
```

---

#### **🔢 3 FORMAT QUAN TRỌNG**

```typescript
// 1. UTC ISO 8601 (Storage/API)
'2024-01-15T14:30:00.000Z';
//                      ↑
//                      Z = UTC

// 2. Timestamp (Comparison)
1705329000000; // milliseconds từ 1970

// 3. Display Format (User)
('15/01/2024 21:30'); // Vietnam
('01/15/2024 9:30 PM'); // US
```

---

#### **⚠️ 3 LỖI CHẾT NGƯỜI**

```typescript
// ❌ LỖI 1: Lưu local time
localStorage.setItem('date', '15/01/2024');
// → Không biết timezone nào!

// ❌ LỖI 2: Format sai
dayjs().format('yyyy-mm-dd');
// → "2024-30-15" (mm = minutes!)

// ❌ LỖI 3: Parse không format
dayjs('15/01/2024');
// → Invalid Date
```

---

### **🎨 SƠ ĐỒ TƯ DUY (Mind Map)**

```
                    ⏰ DATE & TIME HANDLING
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
    📦 STORAGE          🔄 CONVERT          🖥️ DISPLAY
        │                   │                   │
    ┌───┴───┐           ┌───┴───┐           ┌───┴───┐
    │       │           │       │           │       │
   UTC   Timestamp     Parse  Format     Timezone  Locale
    │       │           │       │           │       │
    └───────┴───────────┴───────┴───────────┴───────┘
                            │
                    🛠️ DAYJS LIBRARY
                            │
            ┌───────────────┼───────────────┐
            │               │               │
         Plugins         Methods         Utils
            │               │               │
        utc, tz        format, tz      isValid
```

---

### **🎭 CHUYỆN KỂ GHI NHỚ (Story Method)**

**Câu chuyện "Anh Thợ Sửa Đồng Hồ UTC"**

```
🕐 Ngày xửa ngày xưa, có anh thợ sửa đồng hồ tên UTC...

Anh UTC có quy tắc:
1. MỌI đồng hồ phải chỉnh về giờ London (UTC) trước khi cất vào tủ (Storage)
2. Khi khách đến lấy, mới chỉnh về giờ địa phương (Display)
3. Khi so sánh 2 đồng hồ, đưa về cùng 1 chuẩn (Timestamp)

Nhờ vậy:
✅ Không bao giờ nhầm lẫn múi giờ
✅ So sánh chính xác
✅ Khách hàng thấy giờ đúng múi giờ của họ

Bài học: "Store UTC, Display Local, Compare Timestamp"
```

---

### **🎯 FLASHCARDS (Thẻ Ghi Nhớ)**

#### **Thẻ 1: Lưu Database**

```
❓ QUESTION: Lưu thời gian vào database như thế nào?

✅ ANSWER:
- UTC ISO 8601: "2024-01-15T14:30:00.000Z"
- Hoặc Timestamp: 1705329000000
- KHÔNG BAO GIỜ: "15/01/2024" (không có timezone)

🔑 KEYWORD: "Store UTC, not local"
```

#### **Thẻ 2: Hiển Thị User**

```
❓ QUESTION: Hiển thị thời gian cho user?

✅ ANSWER:
dayjs(utcDate).tz('Asia/Ho_Chi_Minh').format('DD/MM/YYYY HH:mm')

🔑 KEYWORD: "Convert UTC → Local timezone"
```

#### **Thẻ 3: Format String**

```
❓ QUESTION: Format tokens đúng?

✅ ANSWER:
YYYY = year (2024)
MM   = month (01)
DD   = day (15)
HH   = hour 24h (14)
mm   = minute (30)
ss   = second (45)

⚠️ TRÁNH: yyyy, mm (month!), MM (minute!)

🔑 KEYWORD: "YYYY-MM-DD HH:mm:ss"
```

#### **Thẻ 4: Parse Input**

```
❓ QUESTION: Parse user input an toàn?

✅ ANSWER:
dayjs('15/01/2024', 'DD/MM/YYYY', true)
//                                 ↑
//                          strict mode

🔑 KEYWORD: "Specify format explicitly"
```

---

### **🎵 VẦN ĐIỆU GHI NHỚ (Mnemonic)**

**"UTC SỮA - DỊ LOCAL TRÀ"**

```
U = UTC lưu Storage
T = Timezone convert
C = Comparison dùng timestamp

S = Specify format rõ ràng
Ữ = Ừ thì extend plugins
A = Always validate input

D = Display local timezone
Ị = Ị... ISO 8601 format
L = Library đừng native Date
O = Offset không bằng timezone
C = Constructor với format
A = API luôn gửi UTC
L = Locale cho i18n
T = Testing multiple timezones
R = Rules: 3 nguyên tắc vàng
À = À... check isValid() trước
```

---

### **🏋️ BÀI TẬP THỰC HÀNH (Hands-on)**

#### **Challenge 1: Fix Bug**

```typescript
// 🐛 BUG: Code này sai ở đâu?
const date = dayjs('15/01/2024');
await db.save({ createdAt: date.format('YYYY-MM-DD') });

// 💡 SOLUTION:
const date = dayjs('15/01/2024', 'DD/MM/YYYY');
await db.save({ createdAt: date.utc().toISOString() });

// ✅ WHY:
// 1. Parse cần format rõ ràng
// 2. Lưu UTC ISO, không phải local string
```

#### **Challenge 2: Timezone Convert**

```typescript
// 📝 TASK: User Vietnam chọn "15/01/2024 21:30"
// Convert to UTC để gửi API

// YOUR CODE:
const userInput = '15/01/2024 21:30';
const utc = dayjs
  .tz(userInput, 'DD/MM/YYYY HH:mm', 'Asia/Ho_Chi_Minh')
  .utc()
  .toISOString();

console.log(utc); // "2024-01-15T14:30:00.000Z" ✅
```

#### **Challenge 3: Display Logic**

```typescript
// 📝 TASK: API trả về "2024-01-15T14:30:00.000Z"
// Hiển thị cho user ở New York

// YOUR CODE:
const apiDate = '2024-01-15T14:30:00.000Z';
const display = dayjs(apiDate)
  .tz('America/New_York')
  .format('MM/DD/YYYY hh:mm A');

console.log(display); // "01/15/2024 09:30 AM" ✅
```

---

### **🔁 REVIEW CYCLE (Ôn Tập Định Kỳ)**

#### **📅 Lịch Ôn Tập Theo Đường Cong망Quên**

```
Ngày 1️⃣: Học lần đầu
  ↓
Ngày 2️⃣: Ôn lại (sau 1 ngày)
  ↓ Retention: 90%
Ngày 4️⃣: Ôn lại (sau 2 ngày)
  ↓ Retention: 85%
Ngày 8️⃣: Ôn lại (sau 4 ngày)
  ↓ Retention: 80%
Ngày 16: Ôn lại (sau 8 ngày)
  ↓ Retention: 75%
Ngày 30: Ôn lại (sau 14 ngày)
  → LONG-TERM MEMORY ✅
```

#### **⏱️ 5 Phút Mỗi Ngày**

**Ngày 1-3: Nhớ 3 Nguyên Tắc**

- Store UTC, Display Local, Compare Timestamp
- Làm Flashcard 1-2

**Ngày 4-7: Practice Format**

- YYYY-MM-DD HH:mm:ss
- Làm Challenge 1

**Ngày 8-14: Timezone Conversion**

- UTC → Local, Local → UTC
- Làm Challenge 2-3

**Ngày 15-30: Real Project**

- Apply vào dự án thực tế
- Debug timezone issues

---

### **📊 CHECKLIST GHI NHỚ**

```markdown
## ✅ TỰ KIỂM TRA (Không xem tài liệu)

### Level 1: Cơ Bản

- [ ] Nêu được 3 nguyên tắc vàng
- [ ] Viết được UTC ISO 8601 format
- [ ] Phân biệt YYYY vs yyyy, MM vs mm
- [ ] Biết khi nào dùng UTC, khi nào Local

### Level 2: Trung Cấp

- [ ] Parse date với format rõ ràng
- [ ] Convert timezone (UTC ↔ Local)
- [ ] Format date đúng cho Vietnam/US
- [ ] Validate date input

### Level 3: Nâng Cao

- [ ] Setup dayjs với plugins
- [ ] Viết được utility functions
- [ ] Handle DST (Daylight Saving Time)
- [ ] Test với multiple timezones

### Level 4: Production-Ready

- [ ] Integrate với API (create/fetch events)
- [ ] Build React components (DatePicker, Display)
- [ ] Write unit tests
- [ ] Debug timezone issues nhanh
```

---

### **🎬 VIDEO SCENARIOS (Hình Dung)**

#### **Scenario 1: E-commerce Flash Sale**

```
🛒 User Vietnam: "Flash sale 21:00 hôm nay!"

Backend save:
{
  flashSaleStart: "2024-01-15T14:00:00.000Z" // UTC
}

Display cho users:
- Vietnam: "21:00 ICT" ✅
- Singapore: "22:00 SGT" ✅
- US: "9:00 AM EST" ✅

→ Mọi người thấy giờ đúng múi giờ của họ!
```

#### **Scenario 2: Meeting Scheduler**

```
👔 Boss US: "Meeting lúc 9 AM my time"
👨‍💻 Dev VN: Nhận "22:00 tối nay"

Backend save:
{
  meetingTime: "2024-01-15T14:00:00.000Z"
}

Display:
- US Boss: "9:00 AM EST"
- VN Dev: "22:00 ICT"

→ Cùng 1 timestamp, hiển thị khác nhau!
```

---

### **🎯 KEY TAKEAWAYS (Mang Đi)**

```
┌─────────────────────────────────────────────────┐
│  📝 GHI NHỚ 10 GIÂY                            │
├─────────────────────────────────────────────────┤
│  1. Store UTC, Display Local                    │
│  2. dayjs.utc().toISOString()                  │
│  3. dayjs(utcDate).tz(timezone).format()       │
│  4. Parse với format: ('15/01', 'DD/MM')       │
│  5. Test: isValid() trước khi dùng             │
└─────────────────────────────────────────────────┘
```

**🔖 Bookmark This:**

```typescript
// Copy-paste snippet cho mọi project
import dayjs from 'dayjs';
import utc from 'dayjs/plugin/utc';
import timezone from 'dayjs/plugin/timezone';

dayjs.extend(utc);
dayjs.extend(timezone);

// Save to DB
const saveDate = dayjs().utc().toISOString();

// Display to user
const displayDate = dayjs(saveDate)
  .tz('Asia/Ho_Chi_Minh')
  .format('DD/MM/YYYY HH:mm');
```

---

### **💪 THỰC HÀNH HẰNG NGÀY**

```
📱 MỖI KHI CODE DATE/TIME:

1. Tự hỏi: "UTC hay Local?"
2. Check: Format string có rõ ràng?
3. Validate: isValid() trước khi dùng
4. Test: Thử với timezone khác
5. Document: Comment timezone cho team
```

**Lời Khuyên Cuối:**

> "Đừng cố nhớ tất cả chi tiết.
> Nhớ 3 nguyên tắc vàng, còn lại Google/ChatGPT.
> Practice makes perfect - Code thực tế 10 lần
> thì não sẽ nhớ tự động!"

---

**🎯 Kết Luận Tổng Thể:**

**Performance Optimization (Q56):**

- ✅ 5-layer strategy: Build-time → Network → Rendering → State → Memory
- ✅ Measurable results: 70% faster load, 82% smaller bundle, 60 FPS
- ✅ Tools: Vite, React.memo, Zustand, react-window, Chrome DevTools

**Security (Q57):**

- ✅ 7-layer defense: HTTPS → XSS → CSRF → Auth → Storage → API → Headers
- ✅ Comprehensive protection: Input sanitization, JWT tokens, rate limiting
- ✅ Tools: DOMPurify, Helmet, Zod, bcrypt

**Cryptography (Q58):**

- ✅ Hash (bcrypt, SHA-256): Passwords, checksums, integrity
- ✅ Encryption (AES, RSA): Sensitive data, HTTPS, key exchange
- ✅ Digital Signatures (RS256, HMAC): JWT, API auth, webhooks

**Date & Time Handling (Q59):**

- ✅ UTC-first approach: Store UTC, display local timezone
- ✅ ISO 8601 standard: "2024-01-15T14:30:00.000Z"
- ✅ Libraries: date-fns (functional), Luxon (OOP), Day.js (lightweight)
- ✅ Temporal API: Future standard (Stage 3 proposal)

**💡 Key Takeaway:**

- Performance & Security KHÔNG phải optional - là MUST-HAVE cho production apps
- Date/Time: Always UTC for storage, convert to local for display
- Measure & Monitor trong production
- Defense in depth: Multiple layers of protection
- Use proven libraries - NEVER roll your own crypto or date handling!
