# Topic 37: Date & Time Handling - Xử Lý Múi Giờ Đúng Cách

## Câu trả lời ngắn gọn

Trong frontend, nguyên tắc quan trọng nhất là: **lưu và truyền thời gian dưới dạng UTC hoặc timestamp, chỉ convert sang timezone/local format khi hiển thị cho user**.

Khi xử lý date/time cần phân biệt:

1. **Instant:** một thời điểm tuyệt đối trên timeline, ví dụ `2026-05-16T09:00:00.000Z`.
2. **Local date/time:** ngày giờ theo người dùng nhập, ví dụ `16/05/2026 09:00`, chưa đủ timezone.
3. **Timezone:** vùng quy tắc thời gian như `Asia/Ho_Chi_Minh`, `America/New_York`.
4. **Offset:** độ lệch tại một thời điểm như `+07:00`, `-05:00`. Offset không thay thế được timezone vì không biết DST/history.

Best practice:

- API nên truyền ISO 8601 có timezone, ví dụ `2026-05-16T09:00:00.000Z`.
- Database nên lưu UTC/timestamp cho event một lần.
- UI nên format bằng `Intl.DateTimeFormat` hoặc thư viện như `date-fns`, `Day.js`, `Luxon`.
- Không hardcode offset như `+7 * 60 * 60 * 1000`.
- Với recurring event, phải lưu timezone và rule lặp lại, không chỉ lưu UTC.

---

## 1. Mental model cần nhớ

### Instant

Instant là một thời điểm tuyệt đối, không phụ thuộc user ở đâu.

Ví dụ:

```txt
2026-05-16T09:00:00.000Z
```

Cùng một instant nhưng hiển thị khác nhau:

```txt
UTC:      2026-05-16 09:00
Vietnam: 2026-05-16 16:00
New York:2026-05-16 05:00
```

Timestamp cũng là instant:

```ts
const timestamp = 1778922000000;
```

Timestamp là số milliseconds từ Unix epoch `1970-01-01T00:00:00Z`, nên so sánh rất an toàn:

```ts
dateA.getTime() > dateB.getTime();
```

### Local date/time

Local date/time là giá trị user nhìn hoặc nhập.

Ví dụ:

```txt
16/05/2026 09:00
```

Giá trị này chưa đủ để biết instant thật sự nếu không biết timezone. `09:00` ở Việt Nam khác `09:00` ở New York.

### Timezone vs offset

Offset là độ lệch tại một thời điểm:

```txt
+07:00
-05:00
```

Timezone là vùng quy tắc:

```txt
Asia/Ho_Chi_Minh
America/New_York
Europe/London
```

Senior point: **nên lưu IANA timezone thay vì offset** nếu logic liên quan đến địa phương, lịch họp, thị trường, deadline hoặc recurring event.

### Source of truth cho timezone

Không phải lúc nào cũng dùng timezone của browser. Senior cần hỏi rõ timezone lấy từ đâu:

```txt
User profile timezone -> business/account timezone -> browser timezone -> default timezone
```

Lấy timezone browser:

```ts
const browserTimezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
```

Nhưng browser timezone chỉ là fallback. Với app tài chính, booking, vận hành hoặc admin dashboard, timezone thường phải đến từ user profile, tenant, market, branch hoặc setting nghiệp vụ.

---

## 2. Quy tắc lưu, truyền và hiển thị

### Lưu trong database

Với event xảy ra một lần:

```json
{
  "createdAt": "2026-05-16T09:00:00.000Z"
}
```

Hoặc:

```json
{
  "createdAt": 1778922000000
}
```

Không nên lưu:

```json
{
  "createdAt": "16/05/2026 09:00"
}
```

Vì string này không có timezone, không rõ là giờ Việt Nam, UTC hay timezone nào.

### Truyền qua API

API nên dùng ISO 8601 rõ timezone:

```json
{
  "startAt": "2026-05-16T09:00:00.000Z"
}
```

Hoặc có offset:

```json
{
  "startAt": "2026-05-16T16:00:00+07:00"
}
```

Cả hai đều rõ nghĩa. Tuy nhiên, dùng UTC `Z` thường dễ normalize và so sánh hơn.

### Hiển thị trên UI

Convert UTC sang timezone của user khi display:

```ts
const date = new Date('2026-05-16T09:00:00.000Z');

const result = new Intl.DateTimeFormat('vi-VN', {
  dateStyle: 'short',
  timeStyle: 'short',
  timeZone: 'Asia/Ho_Chi_Minh',
}).format(date);
```

Kết quả:

```txt
16/05/2026, 16:00
```

Với app global, nên hiển thị timezone rõ khi dữ liệu nhạy cảm:

```txt
16/05/2026 16:00 ICT
```

---

## 3. Native Date pitfalls

### Date object lưu instant, nhưng method có local và UTC

```ts
const date = new Date('2026-05-16T09:00:00.000Z');

date.getHours(); // giờ theo timezone máy chạy code
date.getUTCHours(); // giờ UTC
```

Nếu xử lý server timestamp, cẩn thận khi dùng `getHours`, `getDate`, `getMonth` vì chúng phụ thuộc timezone local.

### Parse string không rõ format

Không nên:

```ts
new Date('16/05/2026');
new Date('05/16/2026');
new Date('2026-05-16 09:00:00');
```

Các format này có thể khác nhau giữa browser/runtime.

Nên dùng:

```ts
new Date('2026-05-16T09:00:00.000Z');
new Date('2026-05-16T16:00:00+07:00');
```

Lưu ý quan trọng:

```ts
new Date('2026-05-16'); // date-only ISO, được hiểu là UTC midnight
new Date('2026-05-16T09:00:00'); // date-time không timezone, hiểu là local time
```

### Month zero-indexed

```ts
new Date(2026, 0, 16); // January 16
new Date(2026, 1, 16); // February 16
```

Month bắt đầu từ `0`, day bắt đầu từ `1`.

### Date mutable

Không tốt:

```ts
const date = new Date('2026-05-16T09:00:00.000Z');
const next = date;
next.setDate(20);

console.log(date.getDate()); // bị đổi theo
```

Tốt hơn:

```ts
const date = new Date('2026-05-16T09:00:00.000Z');
const next = new Date(date.getTime());
next.setDate(20);
```

### So sánh Date bằng `===`

Không tốt:

```ts
new Date('2026-05-16T09:00:00.000Z') ===
  new Date('2026-05-16T09:00:00.000Z'); // false
```

Tốt:

```ts
dateA.getTime() === dateB.getTime();
dateA.getTime() > dateB.getTime();
```

---

## 4. User input: local -> UTC

Khi user chọn ngày giờ trong form, giá trị thường là local date/time. Trước khi gửi server, cần biết timezone của user rồi convert sang UTC.

Ví dụ user Việt Nam chọn:

```txt
16/05/2026 16:00 Asia/Ho_Chi_Minh
```

Server nên nhận:

```txt
2026-05-16T09:00:00.000Z
```

Với `Day.js`:

```ts
import dayjs from 'dayjs';
import utc from 'dayjs/plugin/utc';
import timezone from 'dayjs/plugin/timezone';
import customParseFormat from 'dayjs/plugin/customParseFormat';

dayjs.extend(utc);
dayjs.extend(timezone);
dayjs.extend(customParseFormat);

function parseUserInputToUtc(input: string, userTimezone: string) {
  return dayjs
    .tz(input, 'DD/MM/YYYY HH:mm', userTimezone)
    .utc()
    .toISOString();
}

parseUserInputToUtc('16/05/2026 16:00', 'Asia/Ho_Chi_Minh');
// "2026-05-16T09:00:00.000Z"
```

---

## 5. Scheduling và recurring event

### Event xảy ra một lần

Ví dụ: user đặt lịch gọi vào đúng một thời điểm.

Lưu:

```json
{
  "startAt": "2026-05-16T09:00:00.000Z",
  "timezone": "Asia/Ho_Chi_Minh"
}
```

`startAt` dùng để so sánh, sort, notify. `timezone` dùng để display hoặc audit theo context ban đầu.

### Deadline theo ngày nghiệp vụ

Một deadline kiểu “hết hạn vào cuối ngày 16/05 theo giờ Việt Nam” không nên hiểu đơn giản là `2026-05-16T00:00:00Z`.

Nên biểu diễn rõ:

```json
{
  "dueDate": "2026-05-16",
  "timezone": "Asia/Ho_Chi_Minh",
  "deadlinePolicy": "end_of_day"
}
```

Sau đó backend hoặc shared date utility convert thành instant cuối ngày theo timezone đó.

### Recurring event

Ví dụ: “họp mỗi thứ Hai lúc 09:00 ở New York”.

Không nên chỉ lưu UTC đầu tiên, vì DST có thể làm các lần sau bị lệch giờ local.

Nên lưu:

```json
{
  "localTime": "09:00",
  "timezone": "America/New_York",
  "recurrenceRule": "FREQ=WEEKLY;BYDAY=MO"
}
```

Khi generate từng occurrence, tính theo timezone `America/New_York`. Như vậy sau DST, meeting vẫn là 09:00 local time.

Senior point: **event một lần dùng instant/UTC; event lặp lại dùng local rule + timezone**.

---

## 6. DST và vì sao không hardcode offset

Không tốt:

```ts
const vietnamTime = utcTime + 7 * 60 * 60 * 1000;
```

Với Việt Nam ít khi lộ bug vì không có DST hiện tại, nhưng với US/EU sẽ sai khi chuyển giờ mùa hè.

Ví dụ New York:

```txt
Winter: UTC-05:00
Summer: UTC-04:00
```

Vì vậy:

```txt
America/New_York != -05:00
```

Timezone là rule, offset chỉ là kết quả tại một thời điểm.

### Ambiguous và nonexistent local time

Ở timezone có DST, có hai case khó:

- **Nonexistent time:** giờ không tồn tại khi đồng hồ nhảy tới, ví dụ 02:30 bị skip.
- **Ambiguous time:** một giờ xảy ra hai lần khi đồng hồ lùi lại, ví dụ 01:30 xuất hiện 2 lần.

Với scheduling nghiêm túc, UI/API nên có policy rõ:

```txt
Nếu local time không tồn tại -> đẩy sang giờ hợp lệ tiếp theo hoặc báo lỗi
Nếu local time bị trùng -> chọn earlier/later offset theo business rule
```

Đây là điểm staff-level vì bug thường không xuất hiện ở Việt Nam nhưng sẽ xuất hiện ở US/EU.

---

## 7. Intl API

Nên dùng `Intl` cho format hiển thị vì native, nhẹ, hỗ trợ locale tốt.

### Format date/time

```ts
function formatDateTime(
  value: string | number | Date,
  locale: string,
  timeZone: string
) {
  return new Intl.DateTimeFormat(locale, {
    dateStyle: 'medium',
    timeStyle: 'short',
    timeZone,
  }).format(new Date(value));
}
```

```ts
formatDateTime(
  '2026-05-16T09:00:00.000Z',
  'vi-VN',
  'Asia/Ho_Chi_Minh'
);
```

### Format relative time

```ts
const rtf = new Intl.RelativeTimeFormat('vi-VN', {
  numeric: 'auto',
});

rtf.format(-2, 'day'); // "2 ngày trước"
rtf.format(1, 'hour'); // "sau 1 giờ"
```

---

## 8. Day.js setup gọn

Nếu cần parse custom format hoặc timezone conversion, dùng Day.js với plugin:

```ts
import dayjs from 'dayjs';
import utc from 'dayjs/plugin/utc';
import timezone from 'dayjs/plugin/timezone';
import customParseFormat from 'dayjs/plugin/customParseFormat';

dayjs.extend(utc);
dayjs.extend(timezone);
dayjs.extend(customParseFormat);
```

Không nên set global timezone cứng cho app global:

```ts
dayjs.tz.setDefault('Asia/Ho_Chi_Minh');
```

Chỉ nên làm vậy nếu app thực sự chỉ phục vụ một timezone. Với app global hoặc SSR, hãy truyền timezone rõ vào từng hàm.

Ví dụ display:

```ts
function formatApiDate(value: string, timezone: string) {
  return dayjs(value).tz(timezone).format('DD/MM/YYYY HH:mm');
}

formatApiDate('2026-05-16T09:00:00.000Z', 'Asia/Ho_Chi_Minh');
// "16/05/2026 16:00"
```

Ví dụ compare:

```ts
const a = dayjs('2026-05-16T16:00:00+07:00');
const b = dayjs('2026-05-16T09:00:00Z');

a.valueOf() === b.valueOf(); // true
```

---

## 9. Database/API notes cho senior

Tùy database mà kiểu date/time có behavior khác nhau.

Ví dụ:

- PostgreSQL: `timestamptz` phù hợp để lưu instant.
- MySQL: `TIMESTAMP` có conversion timezone, `DATETIME` không chứa timezone.
- Nếu dùng `DATETIME`, team phải thống nhất convention là UTC.
- API contract nên document rõ field nào là UTC instant, field nào là local date.

Ví dụ API rõ ràng:

```json
{
  "createdAt": "2026-05-16T09:00:00.000Z",
  "businessDate": "2026-05-16",
  "timezone": "Asia/Ho_Chi_Minh"
}
```

Trong đó:

- `createdAt`: instant.
- `businessDate`: ngày nghiệp vụ, không nhất thiết là instant.
- `timezone`: timezone dùng cho display/business rule.

### Query date range đúng cách

Không nên query bằng string ngày nếu data lưu instant:

```txt
createdAt date = "2026-05-16"
```

Nên convert range local date sang UTC boundary:

```ts
// User muốn lọc ngày 16/05/2026 theo Asia/Ho_Chi_Minh
const startUtc = dayjs
  .tz('2026-05-16 00:00', 'YYYY-MM-DD HH:mm', 'Asia/Ho_Chi_Minh')
  .utc()
  .toISOString();

const endUtc = dayjs
  .tz('2026-05-17 00:00', 'YYYY-MM-DD HH:mm', 'Asia/Ho_Chi_Minh')
  .utc()
  .toISOString();
```

API query nên dùng half-open interval:

```txt
createdAt >= startUtc AND createdAt < endUtc
```

Tránh dùng `<= 23:59:59` vì dễ sai milliseconds/microseconds/nanoseconds.

---

## 10. Timers, countdown và clock skew

Frontend thường có countdown, OTP expiry, flash sale, trading session hoặc token expiry. Không nên chỉ tin vào clock của client vì user có thể chỉnh giờ máy.

### Dùng server time làm mốc

API có thể trả:

```json
{
  "serverTime": "2026-05-16T09:00:00.000Z",
  "expiresAt": "2026-05-16T09:05:00.000Z"
}
```

Client tính offset:

```ts
const serverNow = new Date(response.serverTime).getTime();
const clientNow = Date.now();
const clockOffset = serverNow - clientNow;

function getTrustedNow() {
  return Date.now() + clockOffset;
}

function getTimeLeft(expiresAt: string) {
  return new Date(expiresAt).getTime() - getTrustedNow();
}
```

### Dùng monotonic clock cho elapsed time

Nếu cần đo duration trong UI, dùng `performance.now()` thay vì `Date.now()` vì `Date.now()` có thể nhảy khi hệ thống chỉnh giờ.

```ts
const startedAt = performance.now();

const elapsed = performance.now() - startedAt;
```

Rule:

```txt
Absolute time/deadline -> Date.now/server time/UTC instant
Elapsed duration/performance -> performance.now()
```

---

## 11. Testing date/time

Date/time rất dễ flaky test. Nên mock current time.

### Mock current time với Vitest

```ts
import { describe, it, expect, vi, afterEach } from 'vitest';

function isExpired(expiredAt: string) {
  return Date.now() > new Date(expiredAt).getTime();
}

describe('isExpired', () => {
  afterEach(() => {
    vi.useRealTimers();
  });

  it('returns true when current time is after expiredAt', () => {
    vi.useFakeTimers();
    vi.setSystemTime(new Date('2026-05-16T10:00:00.000Z'));

    expect(isExpired('2026-05-16T09:00:00.000Z')).toBe(true);
  });
});
```

### Test timezone bằng Intl

Không assert `getHours()` nếu muốn test timezone cụ thể, vì `getHours()` phụ thuộc timezone của máy chạy test.

Tốt hơn:

```ts
function formatInTimezone(value: string, timeZone: string) {
  return new Intl.DateTimeFormat('en-US', {
    hour: '2-digit',
    minute: '2-digit',
    hour12: false,
    timeZone,
  }).format(new Date(value));
}

formatInTimezone('2026-05-16T09:00:00.000Z', 'Asia/Ho_Chi_Minh');
// "16:00"
```

Các case cần test:

```txt
□ UTC -> local display
□ local input -> UTC payload
□ DST transition
□ end of day / start of day
□ month boundary
□ leap year: Feb 29
□ invalid date
□ recurring event across DST
□ client clock skew
□ date range query boundary
```

---

## 12. Common mistakes

### Lưu string không timezone

```txt
16/05/2026 09:00
```

Không rõ timezone, khó parse, dễ sai giữa các quốc gia.

### Hardcode offset

```ts
utc + 7 * 60 * 60 * 1000;
```

Sai với timezone có DST và làm logic khó maintain.

### Nhầm business date với instant

`2026-05-16` có thể là ngày nghiệp vụ, không phải một thời điểm cụ thể. Đừng ép mọi date thành timestamp nếu domain chỉ cần ngày.

Ví dụ ngày sinh:

```txt
1995-10-20
```

Ngày sinh không nên bị convert timezone làm lệch sang ngày trước/sau.

### Dùng local time trong server/client khác timezone

Code chạy trên máy dev, CI, server, browser user có timezone khác nhau. Nếu logic phụ thuộc timezone local, test và production có thể lệch.

### Không document API date contract

Team backend/frontend cần thống nhất:

```txt
createdAt: ISO 8601 UTC instant
settlementDate: YYYY-MM-DD business date
timezone: IANA timezone
```

---

## 13. Chọn library nào?

Không có library đúng cho mọi case.

```txt
Intl API:
- Tốt cho format display, nhẹ, native.
- Không đủ tiện nếu cần parse custom format/timezone math phức tạp.

date-fns:
- Functional, tree-shakable.
- Tốt cho date utilities.
- Cần thêm date-fns-tz nếu xử lý timezone.

Day.js:
- Nhẹ, API quen thuộc giống Moment.
- Cần plugin utc/timezone/customParseFormat.
- Cẩn thận global config trong SSR/app global.

Luxon:
- Timezone-aware tốt, immutable.
- API rõ mental model hơn Day.js.
- Bundle có thể lớn hơn tùy setup.

Temporal:
- Mental model tốt nhất về lâu dài.
- Cần kiểm tra runtime support/polyfill.
```

Senior answer: nếu chỉ format UI, dùng `Intl`. Nếu app có nhiều parse/convert timezone, chọn `Luxon` hoặc `Day.js` có plugin. Nếu domain cực nhạy về lịch/scheduling, cân nhắc `Temporal`/polyfill hoặc xử lý phần rule phức tạp ở backend.

---

## 14. Temporal API

`Date` có nhiều vấn đề lịch sử: mutable, parsing khó nhớ, timezone yếu, month zero-indexed.

`Temporal` là API mới để xử lý date/time tốt hơn:

```ts
Temporal.Instant;
Temporal.PlainDate;
Temporal.PlainDateTime;
Temporal.ZonedDateTime;
```

Mental model:

- `Temporal.Instant`: một instant tuyệt đối.
- `Temporal.PlainDate`: ngày không timezone, ví dụ birthday/business date.
- `Temporal.PlainDateTime`: ngày giờ local chưa gắn timezone.
- `Temporal.ZonedDateTime`: ngày giờ có timezone đầy đủ.

Trong dự án hiện tại, cần kiểm tra browser/runtime support hoặc dùng polyfill trước khi áp dụng rộng.

---

## 15. Câu trả lời senior nên nói

**"Em phân biệt rõ instant, local date/time, timezone và offset. Với event xảy ra một lần, em lưu và truyền UTC ISO string hoặc timestamp, sau đó chỉ convert sang timezone của user khi hiển thị bằng Intl hoặc library như Day.js/Luxon. Em tránh parse string mơ hồ, tránh hardcode offset, tránh so sánh Date object bằng reference và luôn document API date contract. Với scheduling hoặc recurring event, em không chỉ lưu UTC mà lưu local time, IANA timezone và recurrence rule để xử lý DST đúng. Với filter theo ngày, em convert local date range sang UTC half-open interval. Với countdown/expiry, em dùng server time để tránh clock skew. Khi test, em mock current time và test timezone bằng Intl/library thay vì phụ thuộc timezone máy chạy test."**

---

## 16. Checklist phỏng vấn

```txt
□ Biết nguyên tắc lưu/truyền UTC, display local
□ Phân biệt instant, local date/time, timezone, offset
□ Biết chọn source of truth cho timezone
□ Biết timestamp là absolute time point
□ Biết ISO 8601 `Z` và offset `+07:00`
□ Biết Date có local methods và UTC methods
□ Biết tránh parse string không rõ format
□ Biết month zero-indexed và Date mutable
□ Biết so sánh bằng getTime/valueOf
□ Biết dùng IANA timezone thay vì hardcode offset
□ Biết DST là gì và vì sao recurring event khó
□ Biết event một lần khác recurring event
□ Biết ambiguous/nonexistent time khi DST chuyển giờ
□ Biết dùng Intl.DateTimeFormat
□ Biết Day.js/Luxon/date-fns dùng khi nào
□ Biết query date range bằng UTC half-open interval
□ Biết countdown/expiry nên dùng server time để tránh clock skew
□ Biết performance.now dùng cho elapsed duration
□ Biết test bằng fake timers
□ Biết document API date contract
□ Biết birthday/business date không phải lúc nào cũng là timestamp
```
