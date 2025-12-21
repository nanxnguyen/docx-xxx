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
'2024-01-15' // Ambiguous! 00:00 múi giờ nào?
'2024-01-15 14:30' // Múi giờ nào?

// ✅ Timestamp KHÔNG BỊ ẢNH HƯỞNG
1705329000000 // LUÔN LÀ 2024-01-15 14:30:00 UTC
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

**1. Store UTC:**

```typescript
// ✅ Database/API: Always UTC
await db.save({
  createdAt: Date.now(), // Timestamp
  // Or: new Date().toISOString(), // "2024-01-15T14:30:00.000Z"
});

// ✅ Parse ISO 8601 (auto UTC với Z)
const date = new Date('2024-01-15T14:30:00.000Z');
```

**2. Display Local:**

```typescript
// ✅ Convert to user timezone
const formatter = new Intl.DateTimeFormat('en-US', {
  timeZone: 'Asia/Ho_Chi_Minh',
  dateStyle: 'long',
  timeStyle: 'short',
});
console.log(formatter.format(date)); // "January 15, 2024 at 9:30 PM"
```

**3. Compare Timestamps:**

```typescript
// ✅ So sánh không bị ảnh hưởng timezone
const isAfter = date1.getTime() > date2.getTime();
const daysDiff = Math.floor(
  (date2.getTime() - date1.getTime()) / (1000 * 60 * 60 * 24)
);
```

**4. Date Arithmetic:**

```typescript
// ✅ Cộng/trừ ngày
function addDays(date: Date, days: number): Date {
  return new Date(date.getTime() + days * 24 * 60 * 60 * 1000);
}

// ✅ Start/End of day (UTC)
const startOfDay = new Date(Date.UTC(
  date.getUTCFullYear(),
  date.getUTCMonth(),
  date.getUTCDate()
));
```

---

#### **📚 Libraries (Recommend)**

**date-fns (Functional, Tree-shakeable):**

```typescript
import { format, parseISO, addDays, formatDistanceToNow } from 'date-fns';
import { utcToZonedTime } from 'date-fns-tz';

const date = parseISO('2024-01-15T14:30:00.000Z');
format(date, 'yyyy-MM-dd HH:mm:ss'); // "2024-01-15 14:30:00"

const vnTime = utcToZonedTime(date, 'Asia/Ho_Chi_Minh');
formatDistanceToNow(date, { addSuffix: true }); // "2 hours ago"
```

**Luxon (OOP, Timezone-aware):**

```typescript
import { DateTime } from 'luxon';

const dt = DateTime.fromISO('2024-01-15T14:30:00.000Z');
dt.setZone('Asia/Ho_Chi_Minh').toFormat('yyyy-MM-dd HH:mm:ss');
dt.plus({ days: 7 }).toRelative(); // "in 7 days"
```

**Day.js (Lightweight 2KB):**

```typescript
import dayjs from 'dayjs';
import utc from 'dayjs/plugin/utc';
import timezone from 'dayjs/plugin/timezone';

dayjs.extend(utc);
dayjs.extend(timezone);

dayjs('2024-01-15T14:30:00.000Z')
  .tz('Asia/Ho_Chi_Minh')
  .format('YYYY-MM-DD HH:mm:ss');
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
const flexibleParse = dayjs('15-01-2024', [
  'DD/MM/YYYY',
  'DD-MM-YYYY',
  'YYYY-MM-DD'
], true); // strict mode = true
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
  createdAt: dayjs().format('YYYY-MM-DD HH:mm:ss')
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
  createdAt: dayjs().utc().toISOString()
  // → "2024-01-15T14:30:00.000Z" (UTC, có 'Z' suffix)
});

// Hoặc dùng timestamp
await db.save({
  createdAt: dayjs().valueOf() // 1705329000000 (milliseconds)
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
    scheduledAt: utcDate.toISOString() // "2024-01-15T14:30:00.000Z"
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
console.log(now.format('YY'));   // "24"   - 2 digits

// MONTH
console.log(now.format('MM'));   // "01"      - 2 digits
console.log(now.format('M'));    // "1"       - 1-2 digits
console.log(now.format('MMM'));  // "Jan"     - Short name
console.log(now.format('MMMM')); // "January" - Full name

// DAY
console.log(now.format('DD'));   // "15" - 2 digits
console.log(now.format('D'));    // "15" - 1-2 digits

// HOUR
console.log(now.format('HH'));   // "14" - 24h format (00-23)
console.log(now.format('H'));    // "14" - 24h format (0-23)
console.log(now.format('hh'));   // "02" - 12h format (01-12)
console.log(now.format('h'));    // "2"  - 12h format (1-12)

// MINUTE
console.log(now.format('mm'));   // "30" - Always 2 digits
console.log(now.format('m'));    // "30" - 1-2 digits

// SECOND
console.log(now.format('ss'));   // "45" - Always 2 digits
console.log(now.format('s'));    // "45" - 1-2 digits

// MILLISECOND
console.log(now.format('SSS'));  // "123" - 3 digits

// AM/PM
console.log(now.format('A'));    // "PM"
console.log(now.format('a'));    // "pm"

// TIMEZONE
console.log(now.format('Z'));    // "+00:00" - Offset
console.log(now.format('ZZ'));   // "+0000"  - Offset compact

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
  return dayjs.tz(dateString, inputFormat, userTimezone)
    .utc()
    .toISOString();
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
    return `${startDate.format('DD/MM/YYYY')} (${startDate.format('HH:mm')} - ${endDate.format('HH:mm')})`;
  }
  
  // Khác ngày
  return `${startDate.format('DD/MM/YYYY HH:mm')} - ${endDate.format('DD/MM/YYYY HH:mm')}`;
}

/**
 * Validate date string
 */
export function isValidDate(
  dateString: string,
  format?: string
): boolean {
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
  showRelative = false
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
  timezone = 'Asia/Ho_Chi_Minh'
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
  schedules
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
          {items.map(item => (
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
    body: JSON.stringify(payload)
  });
  
  return response.json();
}

// ✅ Fetch events: Receive UTC, display in user timezone
export async function getEvents(userTimezone: string) {
  const response = await fetch('/api/events');
  const events: ApiEvent[] = await response.json();
  
  // Transform for display
  return events.map(event => ({
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
  const startUTC = dayjs.tz(start, 'DD/MM/YYYY', userTimezone)
    .startOf('day')
    .utc()
    .toISOString();
  
  const endUTC = dayjs.tz(end, 'DD/MM/YYYY', userTimezone)
    .endOf('day')
    .utc()
    .toISOString();
  
  const response = await fetch(
    `/api/events?start=${startUTC}&end=${endUTC}`
  );
  
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
  isValidDate
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
{ createdAt: "2024-01-15T14:30:00.000Z" }

// Compare timestamps
date1.getTime() > date2.getTime()

// Use library
import { format, parseISO } from 'date-fns';
```

**❌ DON'T:**

```typescript
// ❌ Store without timezone
{ date: "2024-01-15" } // Ambiguous!

// ❌ Use local Date
new Date() // Timezone-dependent!

// ❌ Compare dates with ===
date1 === date2 // Always false

// ❌ Mutate
date.setMonth(2) // Side effect!
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
"2024-01-15T14:30:00.000Z"
//                      ↑
//                      Z = UTC

// 2. Timestamp (Comparison)
1705329000000  // milliseconds từ 1970

// 3. Display Format (User)
"15/01/2024 21:30" // Vietnam
"01/15/2024 9:30 PM" // US
```

---

#### **⚠️ 3 LỖI CHẾT NGƯỜI**

```typescript
// ❌ LỖI 1: Lưu local time
localStorage.setItem('date', '15/01/2024')
// → Không biết timezone nào!

// ❌ LỖI 2: Format sai
dayjs().format('yyyy-mm-dd')
// → "2024-30-15" (mm = minutes!)

// ❌ LỖI 3: Parse không format
dayjs('15/01/2024')
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
const utc = dayjs.tz(userInput, 'DD/MM/YYYY HH:mm', 'Asia/Ho_Chi_Minh')
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

