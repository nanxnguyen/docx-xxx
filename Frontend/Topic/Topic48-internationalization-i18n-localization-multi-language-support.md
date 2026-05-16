# Q66: Internationalization (i18n) & Localization - Multi-Language Support

## Câu trả lời ngắn gọn

**Internationalization (i18n)** là thiết kế ứng dụng để có thể hỗ trợ nhiều ngôn ngữ, nhiều vùng miền ngay từ đầu.  
**Localization (l10n)** là phần triển khai cụ thể cho từng ngôn ngữ/vùng miền: dịch text, format ngày giờ, tiền tệ, số, timezone, layout RTL và kiểm thử UI.

Một hệ thống i18n production-ready thường có:

1. **Translation library:** `react-i18next`, `next-intl`, `next-i18next`, `vue-i18n`.
2. **Translation files:** tách theo locale và namespace như `common`, `auth`, `dashboard`, `order`.
3. **Language detection:** lấy từ URL, user setting, localStorage hoặc browser language.
4. **Locale formatting:** dùng `Intl.DateTimeFormat`, `Intl.NumberFormat`, `Intl.RelativeTimeFormat`.
5. **Pluralization & interpolation:** xử lý số ít/số nhiều và biến động như `Hello {{name}}`.
6. **RTL support:** hỗ trợ ngôn ngữ phải sang trái như Arabic, Hebrew.
7. **Lazy loading:** chỉ load ngôn ngữ/namespace cần dùng để giảm bundle size.
8. **Testing & fallback:** test text dài, missing key, fallback language và visual regression.

---

## 1. i18n và l10n khác nhau thế nào?

### i18n

i18n là chuẩn bị kiến trúc để app không bị phụ thuộc vào một ngôn ngữ cố định.

Ví dụ:

```tsx
// Không tốt
<button>Đăng nhập</button>

// Tốt
<button>{t('auth.login')}</button>
```

i18n bao gồm:

- tách text khỏi code
- hỗ trợ nhiều translation files
- format date/time/number/currency theo locale
- thiết kế UI chịu được text dài/ngắn khác nhau
- hỗ trợ RTL nếu sản phẩm cần

### l10n

l10n là dịch và điều chỉnh app cho một locale cụ thể.

Ví dụ:

```txt
en-US: 12/31/2026, $1,000.00
vi-VN: 31/12/2026, 1.000,00 US$
ja-JP: 2026/12/31, $1,000.00
```

l10n không chỉ là dịch text. Nó còn gồm:

- ngày giờ
- tiền tệ
- số thập phân
- timezone
- đơn vị đo
- hình ảnh, màu sắc, nội dung phù hợp văn hóa

---

## 2. Kiến trúc i18n nên thiết kế thế nào?

Một kiến trúc đơn giản, dễ scale:

```txt
src/
├── i18n/
│   ├── index.ts
│   ├── locales/
│   │   ├── en/
│   │   │   ├── common.json
│   │   │   ├── auth.json
│   │   │   └── dashboard.json
│   │   ├── vi/
│   │   │   ├── common.json
│   │   │   ├── auth.json
│   │   │   └── dashboard.json
│   │   └── ja/
│   │       ├── common.json
│   │       ├── auth.json
│   │       └── dashboard.json
│   └── formatters.ts
```

Ý tưởng chính:

- **Locale:** ngôn ngữ + vùng miền, ví dụ `en-US`, `vi-VN`, `ja-JP`.
- **Namespace:** nhóm translation theo feature, ví dụ `auth`, `order`, `common`.
- **Fallback language:** nếu thiếu `vi.auth.login`, fallback sang `en.auth.login`.
- **User preference:** ưu tiên language user chọn, sau đó mới browser language.

Thứ tự chọn language thường dùng:

```txt
URL locale -> user profile -> localStorage -> browser language -> default language
```

Ví dụ URL:

```txt
/vi/dashboard
/en/dashboard
/ja/dashboard
```

URL-based locale tốt cho SEO và share link. LocalStorage tốt cho app internal/dashboard.

---

## 3. Setup React với react-i18next

### Cài packages

```bash
npm install i18next react-i18next i18next-browser-languagedetector
```

### Translation files

```json
// src/i18n/locales/en/common.json
{
  "appName": "Trading App",
  "save": "Save",
  "cancel": "Cancel"
}
```

```json
// src/i18n/locales/vi/common.json
{
  "appName": "Ứng dụng giao dịch",
  "save": "Lưu",
  "cancel": "Hủy"
}
```

```json
// src/i18n/locales/en/auth.json
{
  "login": "Login",
  "welcome": "Welcome, {{name}}"
}
```

```json
// src/i18n/locales/vi/auth.json
{
  "login": "Đăng nhập",
  "welcome": "Xin chào, {{name}}"
}
```

### Khởi tạo i18n

```ts
// src/i18n/index.ts
import i18n from 'i18next';
import LanguageDetector from 'i18next-browser-languagedetector';
import { initReactI18next } from 'react-i18next';

import enCommon from './locales/en/common.json';
import enAuth from './locales/en/auth.json';
import viCommon from './locales/vi/common.json';
import viAuth from './locales/vi/auth.json';

i18n
  .use(LanguageDetector)
  .use(initReactI18next)
  .init({
    fallbackLng: 'en',
    supportedLngs: ['en', 'vi'],
    defaultNS: 'common',
    ns: ['common', 'auth'],
    resources: {
      en: {
        common: enCommon,
        auth: enAuth,
      },
      vi: {
        common: viCommon,
        auth: viAuth,
      },
    },
    interpolation: {
      escapeValue: false,
    },
  });

export default i18n;
```

Import ở entry point:

```ts
// main.tsx
import './i18n';
```

### Sử dụng trong component

```tsx
import { useTranslation } from 'react-i18next';

export function LoginButton() {
  const { t } = useTranslation('auth');

  return <button>{t('login')}</button>;
}
```

Interpolation:

```tsx
const { t } = useTranslation('auth');

return <p>{t('welcome', { name: 'An' })}</p>;
```

Kết quả:

```txt
en: Welcome, An
vi: Xin chào, An
```

---

## 4. Pluralization, context và fallback

### Pluralization

Không nên tự nối chuỗi kiểu:

```ts
`${count} item(s)`
```

Dùng plural rule của i18n library:

```json
{
  "item_one": "{{count}} item",
  "item_other": "{{count}} items"
}
```

```tsx
t('item', { count: 1 }); // 1 item
t('item', { count: 5 }); // 5 items
```

Mỗi ngôn ngữ có plural rule khác nhau. Đây là lý do không nên hardcode logic số nhiều trong code.

### Context

Cùng một từ có thể dịch khác nhau theo ngữ cảnh.

Ví dụ `Order`:

- danh từ: lệnh đặt hàng
- động từ: đặt hàng
- trong trading: lệnh giao dịch

Nên đặt key rõ nghĩa:

```json
{
  "order.createButton": "Place order",
  "order.historyTitle": "Order history",
  "trading.orderBook": "Order book"
}
```

### Fallback

Nếu thiếu translation, app nên fallback:

```txt
vi -> en -> key
```

Không nên để UI crash vì thiếu một key dịch.

---

## 5. Format ngày giờ, số và tiền tệ

Không nên format bằng string thủ công vì mỗi locale có quy tắc khác nhau.

### Date

```ts
export function formatDate(value: Date, locale: string) {
  return new Intl.DateTimeFormat(locale, {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
  }).format(value);
}
```

Ví dụ:

```txt
en-US: 05/16/2026
vi-VN: 16/05/2026
```

### Currency

```ts
export function formatCurrency(
  value: number,
  locale: string,
  currency: string
) {
  return new Intl.NumberFormat(locale, {
    style: 'currency',
    currency,
  }).format(value);
}
```

Ví dụ:

```ts
formatCurrency(100000, 'vi-VN', 'VND');
```

```txt
100.000 ₫
```

### Number

```ts
new Intl.NumberFormat('en-US').format(1000000); // 1,000,000
new Intl.NumberFormat('vi-VN').format(1000000); // 1.000.000
```

Senior point: nên gom formatters vào một module chung để toàn app format nhất quán.

---

## 6. Language switching

Ví dụ switch language:

```tsx
import { useTranslation } from 'react-i18next';

export function LanguageSwitcher() {
  const { i18n } = useTranslation();

  const changeLanguage = (language: string) => {
    i18n.changeLanguage(language);
    localStorage.setItem('language', language);
    document.documentElement.lang = language;
  };

  return (
    <select
      value={i18n.language}
      onChange={(event) => changeLanguage(event.target.value)}
    >
      <option value="en">English</option>
      <option value="vi">Tiếng Việt</option>
    </select>
  );
}
```

Khi đổi language cần cập nhật:

- i18n instance
- persisted preference
- `html lang`
- `html dir` nếu có RTL
- route nếu app dùng locale trong URL

---

## 7. RTL support

RTL là layout cho ngôn ngữ đọc từ phải sang trái như Arabic, Hebrew, Persian.

Nên tránh hardcode `left/right` khi có thể:

```css
/* Không tốt */
.card {
  margin-left: 16px;
  text-align: left;
}
```

Dùng CSS logical properties:

```css
/* Tốt hơn */
.card {
  margin-inline-start: 16px;
  text-align: start;
}
```

Ví dụ:

```ts
const rtlLanguages = ['ar', 'he', 'fa'];

function updateDirection(language: string) {
  const direction = rtlLanguages.includes(language) ? 'rtl' : 'ltr';

  document.documentElement.dir = direction;
  document.documentElement.lang = language;
}
```

Các điểm cần test với RTL:

- layout grid/flex
- icon mũi tên
- drawer/sidebar
- chart
- table
- form input
- animation direction

---

## 8. Lazy loading và performance

Không nên load tất cả ngôn ngữ vào bundle đầu tiên nếu app lớn.

Vấn đề:

```txt
10 languages x 50KB = 500KB translations
```

Giải pháp:

- load locale hiện tại trước
- load namespace theo route/feature
- cache translation files
- preload language nếu user có khả năng đổi

Ví dụ dynamic import:

```ts
async function loadTranslations(language: string, namespace: string) {
  const translations = await import(
    `./locales/${language}/${namespace}.json`
  );

  i18n.addResourceBundle(
    language,
    namespace,
    translations.default,
    true,
    true
  );
}
```

Với app lớn, translation có thể được quản lý qua CMS/TMS:

- Lokalise
- Phrase
- Crowdin
- Transifex

---

## 9. Testing i18n

Cần test nhiều hơn happy path tiếng Anh.

Checklist test:

```txt
□ Missing translation key có fallback
□ Text dài không vỡ layout
□ Button, tab, menu không bị overflow
□ Date/time/number/currency đúng locale
□ Language switch không reload sai state
□ URL locale hoạt động đúng nếu có
□ RTL layout không bị ngược icon sai
□ Form validation message được dịch
□ Email/PDF/export dùng đúng language
□ E2E test ít nhất 1 flow chính với language khác default
```

Pseudo-locale rất hữu ích để phát hiện text hardcode và overflow:

```txt
Login -> [!! Łôôôĝîîîn !!]
```

---

## 10. Lỗi thường gặp

### Hardcode text trong component

Không tốt:

```tsx
<span>Submit</span>
```

Tốt:

```tsx
<span>{t('common.submit')}</span>
```

### Dịch từng từ thay vì dịch theo câu

Không tốt:

```tsx
t('hello') + ' ' + userName + ', ' + t('welcomeBack')
```

Tốt:

```tsx
t('welcomeBack', { name: userName })
```

Vì thứ tự từ trong mỗi ngôn ngữ có thể khác nhau.

### Dùng key quá chung chung

Không tốt:

```json
{
  "title": "Title"
}
```

Tốt:

```json
{
  "auth.loginTitle": "Login to your account"
}
```

### Quên format locale

Chỉ dịch text là chưa đủ. Senior cần nhắc cả:

- date
- time
- number
- currency
- timezone
- pluralization
- RTL
- accessibility label

### Không có quy trình dịch

Khi app lớn, cần quy trình rõ:

```txt
Developer tạo key -> export key -> translator dịch -> review -> import -> test
```

Nếu không có process, translation dễ thiếu, sai context hoặc không đồng bộ.

---

## 11. Câu trả lời senior nên nói

**"i18n là thiết kế app để hỗ trợ nhiều ngôn ngữ ngay từ kiến trúc, còn l10n là dịch và điều chỉnh cho từng locale cụ thể. Em sẽ tách toàn bộ text ra translation files theo locale và namespace, dùng thư viện như react-i18next, có fallback language, interpolation, pluralization và language detection. Ngoài text, em dùng Intl API để format date/time/number/currency theo locale, xử lý timezone, hỗ trợ RTL bằng `dir` và CSS logical properties, đồng thời lazy load translation bundles để không tăng initial bundle size. Với production, em sẽ test missing keys, text expansion, layout overflow, RTL, E2E flow chính và dùng TMS như Lokalise/Phrase/Crowdin nếu team dịch thuật lớn."**

---

## 12. Checklist phỏng vấn

```txt
□ Phân biệt được i18n và l10n
□ Biết dùng translation key thay vì hardcode text
□ Biết tổ chức locale + namespace
□ Biết fallback language và language detection
□ Biết interpolation và pluralization
□ Biết format date/time/number/currency bằng Intl API
□ Biết xử lý timezone
□ Biết RTL và CSS logical properties
□ Biết lazy load translation files
□ Biết test text expansion, missing key, RTL, E2E
□ Biết trade-off URL locale vs localStorage/user setting
□ Biết quy trình tích hợp TMS cho team lớn
```
