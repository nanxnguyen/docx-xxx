# ⏰ Topic37: Date & Time Handling

## ⭐ Senior/Staff Summary

> **Date/time bug thường không nằm ở format đẹp hay xấu, mà nằm ở việc team không phân biệt rõ `instant`, `local date`, `timezone`, `offset` và `display`.**

- ✅ **Storage/API**: lưu và truyền `UTC` bằng ISO 8601 có timezone (`2024-01-15T14:30:00.000Z`) hoặc Unix timestamp.
- ✅ **Display**: convert UTC sang timezone/locale của user bằng `Intl.DateTimeFormat` hoặc library.
- ✅ **Compare/sort**: dùng timestamp (`getTime()`) hoặc instant UTC, không so sánh string display.
- ⚠️ **User input**: date/time user nhập là local theo một timezone cụ thể; phải parse rõ format + timezone rồi convert sang UTC.
- ⚠️ **Recurring events**: tính theo timezone của lịch, không cộng timestamp đơn giản.
- ⚠️ **DST**: không hardcode offset như `GMT-5`; dùng IANA timezone như `America/New_York`.
- 💡 **Native `Date` vẫn dùng được**, nhưng phải biết các trap: mutable, parse string rủi ro, month zero-indexed, local vs UTC methods.
- 🔮 **Temporal**: API mới hơn, immutable và timezone-aware; ưu tiên khi runtime/polyfill cho phép.

## 🧠 Key Mental Model

### 1. Phân biệt 4 khái niệm

| Khái niệm | Ý nghĩa | Ví dụ |
|---|---|---|
| `Instant` | Một thời điểm tuyệt đối trên timeline | `2024-01-15T14:30:00Z` |
| `Local date/time` | Ngày giờ user nhìn thấy tại một nơi | `15/01/2024 21:30` ở Việt Nam |
| `Timezone` | Bộ rule của vùng, có thể có DST/lịch sử | `Asia/Ho_Chi_Minh`, `America/New_York` |
| `Offset` | Độ lệch tại một thời điểm cụ thể | `+07:00`, `-05:00` |

💡 **Timezone không phải offset.** `America/New_York` có thể là `-05:00` hoặc `-04:00` tùy mùa vì DST.

### 2. Golden Rule

```text
Storage/API  -> UTC ISO hoặc timestamp
Business rule -> timezone rõ ràng
Display      -> locale + timezone của user
Compare      -> timestamp/UTC
User input   -> parse theo format + timezone rồi convert UTC
```

### 3. Câu hỏi senior cần hỏi trước khi code

- Đây là **absolute time** hay **calendar date**?
- User đang nhập giờ theo timezone nào?
- Server/API có contract date rõ chưa?
- Có recurring event, DST, hoặc multi-timezone không?
- UI cần show timezone label không?
- Test có chạy ổn khi máy dev/CI ở timezone khác không?

## 📚 Main Concepts

### 🌍 UTC, ISO 8601 và timestamp

**Timestamp** là số milliseconds từ Unix epoch `1970-01-01T00:00:00Z`.

```typescript
const timestamp = 1705329000000;

const vn = new Date(timestamp);
const ny = new Date(timestamp);

console.log(vn.getTime() === ny.getTime()); // true
console.log(new Date(timestamp).toISOString());
// "2024-01-15T14:30:00.000Z"
```

Cùng một timestamp có thể hiển thị khác nhau:

- Việt Nam: `21:30`, UTC+7.
- New York mùa đông: `09:30`, UTC-5.
- London: `14:30`, UTC+0.

Nhưng **value thật vẫn là cùng một instant**.

### 📦 API contract nên rõ ràng

```typescript
type OrderDTO = {
  id: string;
  createdAt: string; // ISO 8601 UTC, e.g. "2024-01-15T14:30:00.000Z"
  expiresAt?: string;
};

type OrderViewModel = {
  id: string;
  createdAtMs: number;
  createdAtLabel: string;
};
```

✅ Nên:

- API trả ISO 8601 UTC có `Z` hoặc offset.
- Field name rõ nghĩa: `createdAt`, `scheduledAt`, `expiresAt`.
- Nếu thời gian phụ thuộc lịch địa phương, lưu thêm `timezone`.

❌ Tránh:

- `"15/01/2024"` trong API.
- `"2024-01-15 14:30"` không có timezone.
- Backend trả format phụ thuộc locale.

### 🧩 Date-only vs Date-time

Đây là lỗi rất hay gặp trong frontend.

- **Date-time**: `meeting starts at 2024-01-15T14:30:00Z`.
- **Date-only**: birthday, due date, ngày nghỉ lễ: `2024-01-15`.
- **Time-only**: business hour: `09:00`.

```typescript
type Birthday = {
  // Không convert birthday thành UTC midnight nếu chỉ cần ngày sinh.
  date: string; // "1998-05-20"
};

type Meeting = {
  startsAt: string; // UTC ISO
  timezone: string; // "Asia/Ho_Chi_Minh"
};
```

⚠️ `new Date("2024-01-15")` dễ tạo bug khi app chỉ cần **calendar date**. Với date-only, hãy giữ string `YYYY-MM-DD` hoặc dùng `Temporal.PlainDate`/library.

### 🕒 Display bằng `Intl.DateTimeFormat`

`Intl.DateTimeFormat` là API built-in, đủ tốt cho nhiều case format.

```typescript
const startedAt = new Date("2024-01-15T14:30:00.000Z");

const formatter = new Intl.DateTimeFormat("vi-VN", {
  timeZone: "Asia/Ho_Chi_Minh",
  dateStyle: "medium",
  timeStyle: "short",
});

console.log(formatter.format(startedAt));
// "15 thg 1, 2024, 21:30"
```

💡 Với list lớn, cache formatter:

```typescript
const dateTimeFormatter = new Intl.DateTimeFormat("vi-VN", {
  timeZone: "Asia/Ho_Chi_Minh",
  dateStyle: "short",
  timeStyle: "short",
});

const labels = orders.map((order) =>
  dateTimeFormatter.format(new Date(order.createdAt))
);
```

### 🧨 Native `Date` pitfalls

#### 1. Parse string không rõ timezone

```typescript
new Date("2024-01-15"); // ⚠️ dễ gây hiểu nhầm date-only vs UTC midnight
new Date("01/15/2024"); // ❌ locale/browser dependent
new Date("15/01/2024"); // ❌ có thể Invalid Date

new Date("2024-01-15T14:30:00.000Z"); // ✅ explicit UTC
new Date("2024-01-15T21:30:00+07:00"); // ✅ explicit offset
```

#### 2. Month zero-indexed

```typescript
new Date(2024, 1, 15); // February 15, không phải January
new Date(2024, 0, 15); // January 15
```

#### 3. `Date` là mutable

```typescript
function addDaysBad(date: Date, days: number) {
  date.setDate(date.getDate() + days);
  return date;
}

function addDaysSafe(date: Date, days: number) {
  const next = new Date(date.getTime());
  next.setDate(next.getDate() + days);
  return next;
}
```

#### 4. Local methods vs UTC methods

```typescript
const date = new Date("2024-01-15T14:30:00.000Z");

date.getHours(); // local hour, phụ thuộc máy chạy code
date.getUTCHours(); // 14, ổn định theo UTC
date.toISOString(); // luôn UTC
```

✅ Rule:

- Logic server/API/query range: ưu tiên UTC/timestamp.
- Display cho user: dùng locale/timezone rõ ràng.

### 🌞 DST và IANA timezone

DST tạo 2 edge cases nguy hiểm:

- **Spring forward**: một khoảng giờ không tồn tại.
- **Fall back**: một khoảng giờ xảy ra 2 lần.

```typescript
const beforeDst = new Date("2024-03-10T06:59:00.000Z");
const afterDst = new Date("2024-03-10T07:01:00.000Z");

const formatter = new Intl.DateTimeFormat("en-US", {
  timeZone: "America/New_York",
  timeStyle: "long",
  dateStyle: "medium",
});

console.log(formatter.format(beforeDst));
console.log(formatter.format(afterDst));
```

✅ Dùng `America/New_York`, `Europe/London`, `Asia/Ho_Chi_Minh`.

❌ Không hardcode:

```typescript
const NEW_YORK_OFFSET = -5; // ❌ sai vào mùa hè
```

### 🔁 Recurring events

Meeting "mỗi thứ Hai 9:00 AM New York" không nên tính bằng cách cộng `7 * 24h`.

```typescript
type RecurringMeeting = {
  localTime: string; // "09:00"
  weekday: "monday";
  timezone: string; // "America/New_York"
  durationMinutes: number;
};
```

Vì sao?

- DST có thể đổi offset.
- User kỳ vọng luôn là `9:00 AM` theo local calendar.
- Nếu cộng timestamp, sau DST có thể lệch 1 giờ trên display.

💡 Với recurring/scheduling nghiêm túc, nên dùng library timezone-aware hoặc `Temporal.ZonedDateTime`.

### 📚 Library choice

| Library/API | Nên dùng khi | Lưu ý |
|---|---|---|
| `Intl.DateTimeFormat` | Format display/i18n cơ bản | Built-in, cache formatter khi render nhiều |
| `date-fns` | Functional utilities, tree-shaking tốt | Cần thêm `date-fns-tz` cho timezone |
| `Day.js` | Nhẹ, API quen kiểu Moment | Timezone cần plugin |
| `Luxon` | Timezone/DST rõ, immutable | Bundle lớn hơn |
| `Temporal` | Date/time chính xác, immutable, timezone-aware | Check runtime support hoặc dùng polyfill |

### 🔮 Temporal API

Temporal giải quyết nhiều vấn đề của `Date`: immutable, rõ type, timezone-aware, tách `Instant`, `PlainDate`, `ZonedDateTime`.

```typescript
// Ví dụ khi có Temporal runtime/polyfill.
const instant = Temporal.Instant.from("2024-01-15T14:30:00Z");

const vnTime = instant.toZonedDateTimeISO("Asia/Ho_Chi_Minh");
console.log(vnTime.toString());
// "2024-01-15T21:30:00+07:00[Asia/Ho_Chi_Minh]"

const birthday = Temporal.PlainDate.from("1998-05-20");
```

💡 Ghi chú cập nhật: Temporal đã được TC39 đưa lên Stage 4 draft trong năm 2026; khi dùng production vẫn cần kiểm tra support của browser/runtime mục tiêu hoặc dùng polyfill.

## 🧪 Practical TypeScript Examples

### ✅ 1. Format API date cho user

```typescript
type FormatDateOptions = {
  locale?: string;
  timeZone?: string;
};

export function formatApiDate(
  isoUtc: string,
  {
    locale = "vi-VN",
    timeZone = "Asia/Ho_Chi_Minh",
  }: FormatDateOptions = {}
) {
  const date = new Date(isoUtc);

  if (Number.isNaN(date.getTime())) {
    return "Invalid date";
  }

  return new Intl.DateTimeFormat(locale, {
    timeZone,
    dateStyle: "medium",
    timeStyle: "short",
  }).format(date);
}

formatApiDate("2024-01-15T14:30:00.000Z");
// "15 thg 1, 2024, 21:30"
```

### ✅ 2. Convert user input sang UTC

Native `Date` không parse tốt format `DD/MM/YYYY HH:mm`, nên production thường dùng library.

```typescript
import dayjs from "dayjs";
import customParseFormat from "dayjs/plugin/customParseFormat";
import timezone from "dayjs/plugin/timezone";
import utc from "dayjs/plugin/utc";

dayjs.extend(customParseFormat);
dayjs.extend(utc);
dayjs.extend(timezone);

export function userInputToUtcIso(
  input: string,
  userTimeZone: string,
  format = "DD/MM/YYYY HH:mm"
) {
  const parsed = dayjs.tz(input, format, userTimeZone);

  if (!parsed.isValid()) {
    throw new Error("Invalid date input");
  }

  return parsed.utc().toISOString();
}

userInputToUtcIso("15/01/2024 21:30", "Asia/Ho_Chi_Minh");
// "2024-01-15T14:30:00.000Z"
```

### ✅ 3. Query records trong ngày theo timezone user

User chọn `15/01/2024` ở Việt Nam. API cần query UTC range tương ứng.

```typescript
import dayjs from "dayjs";

export function getUtcRangeForLocalDate(
  localDate: string,
  timeZone: string
) {
  const start = dayjs.tz(localDate, "YYYY-MM-DD", timeZone).startOf("day");
  const end = start.endOf("day");

  return {
    startUtc: start.utc().toISOString(),
    endUtc: end.utc().toISOString(),
  };
}

getUtcRangeForLocalDate("2024-01-15", "Asia/Ho_Chi_Minh");
// {
//   startUtc: "2024-01-14T17:00:00.000Z",
//   endUtc: "2024-01-15T16:59:59.999Z"
// }
```

⚠️ Đây là lý do không nên query `createdAt >= 2024-01-15T00:00:00Z` nếu user đang chọn ngày local.

### ✅ 4. Compare/sort bằng timestamp

```typescript
type Event = {
  id: string;
  startsAt: string; // UTC ISO
};

export function sortEvents(events: Event[]) {
  return [...events].sort(
    (a, b) =>
      new Date(a.startsAt).getTime() - new Date(b.startsAt).getTime()
  );
}

export function isExpired(expiresAt: string, now = Date.now()) {
  return new Date(expiresAt).getTime() <= now;
}
```

### ✅ 5. Zod validation cho API/input

```typescript
import { z } from "zod";

const utcIsoDateTimeSchema = z
  .string()
  .datetime({ offset: true })
  .refine((value) => !Number.isNaN(new Date(value).getTime()), {
    message: "Invalid date-time",
  });

const eventSchema = z.object({
  title: z.string().min(1),
  startsAt: utcIsoDateTimeSchema,
  endsAt: utcIsoDateTimeSchema,
  timezone: z.string().min(1),
});

const parsed = eventSchema.parse({
  title: "Frontend interview",
  startsAt: "2024-01-15T14:30:00.000Z",
  endsAt: "2024-01-15T15:30:00.000Z",
  timezone: "Asia/Ho_Chi_Minh",
});
```

### ✅ 6. React component display ổn định

```tsx
import * as React from "react";

type DateDisplayProps = {
  value: string;
  locale?: string;
  timeZone?: string;
};

export function DateDisplay({
  value,
  locale = "vi-VN",
  timeZone = "Asia/Ho_Chi_Minh",
}: DateDisplayProps) {
  const formatter = React.useMemo(
    () =>
      new Intl.DateTimeFormat(locale, {
        timeZone,
        dateStyle: "medium",
        timeStyle: "short",
      }),
    [locale, timeZone]
  );

  const label = React.useMemo(() => {
    const date = new Date(value);
    return Number.isNaN(date.getTime()) ? "Invalid date" : formatter.format(date);
  }, [formatter, value]);

  return (
    <time dateTime={value} title={value}>
      {label}
    </time>
  );
}
```

💡 Dùng `<time dateTime="...">` giúp semantic HTML/accessibility tốt hơn.

## ⚛️ Production Notes / React Implications

### 🧭 SSR / Next.js hydration

Bug thường gặp:

- Server format theo timezone của server.
- Client format theo timezone của user.
- Kết quả text khác nhau -> hydration mismatch.

✅ Cách xử lý:

- Format bằng timezone đã biết từ user profile/cookie.
- Hoặc render ISO/time placeholder trên server, format sau khi client mount.
- Hoặc dùng `suppressHydrationWarning` rất hạn chế, chỉ khi đã hiểu tradeoff.

```tsx
function ClientDate({ value }: { value: string }) {
  const [label, setLabel] = React.useState(value);

  React.useEffect(() => {
    const timeZone = Intl.DateTimeFormat().resolvedOptions().timeZone;
    setLabel(formatApiDate(value, { timeZone }));
  }, [value]);

  return <time dateTime={value}>{label}</time>;
}
```

### 📈 Performance

- Cache `Intl.DateTimeFormat` khi format nhiều rows.
- Tránh tạo formatter trong từng item của list/table.
- Với relative time như "2 phút trước", không cần update mỗi giây cho mọi item.
- Large table nên format ở selector/memoized layer, không format lại toàn bộ mỗi render.

### ♿ Accessibility

- Dùng `<time dateTime={iso}>`.
- Nếu date quan trọng cho quyết định tài chính/y tế/legal, show timezone rõ.
- Với countdown, không spam screen reader mỗi giây; cập nhật `aria-live` hợp lý.

### 🔐 Security / Privacy

- Timezone có thể góp phần fingerprint user; chỉ gửi timezone khi cần.
- Không tin client time cho business-critical checks như flash sale, token expiry, payment deadline.
- Server vẫn phải validate thời gian.

### 🧪 Testing strategy

Test date/time phải kiểm soát "now" và timezone.

```typescript
import { describe, expect, it, vi } from "vitest";

describe("date utils", () => {
  it("checks expiry with fixed time", () => {
    vi.setSystemTime(new Date("2024-01-15T14:30:00.000Z"));

    expect(isExpired("2024-01-15T14:29:59.000Z")).toBe(true);
    expect(isExpired("2024-01-15T14:31:00.000Z")).toBe(false);

    vi.useRealTimers();
  });
});
```

Nên có test cho:

- UTC -> Vietnam/New York display.
- Local date -> UTC range.
- DST transition dates.
- Invalid input.
- SSR/client timezone khác nhau.

## ⚠️ Common Pitfalls

- ❌ Lưu `"DD/MM/YYYY"` vào database/API.
- ❌ Parse `new Date("15/01/2024")`.
- ❌ Quên `new Date(2024, 1, 15)` là tháng 2.
- ❌ Mutate `Date` bằng `setDate`, `setMonth` rồi làm thay đổi object gốc.
- ❌ So sánh `date1 === date2` thay vì `date1.getTime() === date2.getTime()`.
- ❌ Query "ngày của user" bằng UTC start/end mà không convert theo timezone user.
- ❌ Hardcode offset thay vì IANA timezone.
- ❌ Recurring event bằng cách cộng milliseconds.
- ❌ Format date trên server bằng timezone server rồi hydrate trên client timezone khác.
- ❌ Tin vào clock của client cho rule quan trọng.
- ❌ Tạo `Intl.DateTimeFormat` mới trong mỗi row render.

## ✅ Decision Guide / Checklist

**Khi lưu/truyền dữ liệu:**

- Có dùng UTC ISO/timestamp không?
- ISO string có `Z` hoặc offset không?
- API contract có ghi rõ timezone semantics không?
- Date-only có đang bị convert nhầm sang UTC midnight không?

**Khi nhận user input:**

- Input format có explicit không?
- User timezone lấy từ đâu: profile, browser, setting?
- Có validate invalid date như `31/02/2024` không?
- Có convert local -> UTC trước khi gửi server không?

**Khi display:**

- Có dùng locale đúng không?
- Có timezone đúng không?
- Có cần hiển thị timezone label không?
- SSR có nguy cơ hydration mismatch không?

**Khi schedule/recurring:**

- Có DST không?
- Có lưu `timezone` kèm rule không?
- Có dùng library/Temporal thay vì cộng milliseconds không?

**Khi test:**

- Có mock `Date.now()`/system time không?
- Có test nhiều timezone không?
- Có test DST transition không?
- Có test invalid parsing không?

## 🗣️ Short Interview Answer

Em nghĩ xử lý date/time tốt nhất là phải tách rõ storage, business logic và display. Với API/database, em ưu tiên lưu UTC bằng ISO 8601 có `Z` hoặc timestamp. Khi hiển thị thì convert sang locale và timezone của user bằng `Intl.DateTimeFormat` hoặc library như `date-fns`, `Day.js`, `Luxon`.

Theo em, lỗi hay gặp nhất là parse string không rõ timezone như `"15/01/2024"` hoặc `"2024-01-15 10:00"`, dùng `Date` mutable mà không clone, nhầm month zero-indexed, hoặc hardcode offset nên sai ở DST. Với scheduling hoặc recurring events, em sẽ lưu thêm IANA timezone như `America/New_York`, vì offset không đủ để biểu diễn rule theo mùa.

Trong frontend production, em cũng để ý React/SSR: server và client có thể format khác timezone gây hydration mismatch. Với list lớn thì em cache `Intl.DateTimeFormat`. Với rule quan trọng như expiry/payment/flash sale, client chỉ display, server vẫn là nguồn sự thật.
