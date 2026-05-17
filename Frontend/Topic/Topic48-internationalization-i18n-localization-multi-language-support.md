# Q66: Internationalization (i18n) & Localization - Multi-Language Support

## 1. 🧭 Senior/Staff Summary

**Internationalization (`i18n`)** là thiết kế app để hỗ trợ nhiều ngôn ngữ/vùng miền ngay từ kiến trúc.
**Localization (`l10n`)** là phần triển khai cho từng locale cụ thể: dịch nội dung, format ngày giờ, số, tiền tệ, timezone, layout RTL, văn hóa nội dung và kiểm thử UI.

Một hệ thống i18n production-ready không chỉ là `t('key')`. Nó cần:

| Mảng | Việc cần làm | Ví dụ |
|---|---|---|
| Translation | Tách text khỏi code, dùng key rõ nghĩa | `useTranslation('auth'); t('loginButton')` |
| Namespace | Chia translation theo domain/route | `common`, `auth`, `dashboard`, `order` |
| Interpolation | Dịch cả câu có biến | `Welcome, {{name}}` |
| Pluralization | Dùng plural rule theo locale | `item_one`, `item_other` |
| Formatting | Dùng `Intl` cho date/time/number/currency | `Intl.NumberFormat('vi-VN')` |
| Locale detection | Chọn ngôn ngữ theo priority rõ ràng | URL -> profile -> storage -> browser |
| Fallback | Không crash khi thiếu key | `vi -> en -> key` |
| RTL | Hỗ trợ Arabic/Hebrew/Persian nếu cần | `dir="rtl"`, CSS logical properties |
| Performance | Lazy load locale/namespace | route-level translation loading |
| Workflow | Có quy trình với translator/TMS | Lokalise, Phrase, Crowdin, Transifex |

> ✅ Staff mindset: i18n là contract giữa code, product, content, design, QA và translation workflow. Nếu chỉ dịch text ở component thì app vẫn dễ lỗi format, layout, SEO, accessibility và SSR.

---

## 2. 🧠 Key Mental Model

### i18n vs l10n

| Khái niệm | Ý nghĩa | Ví dụ dễ hiểu |
|---|---|---|
| `i18n` | Chuẩn bị app để đổi ngôn ngữ/vùng miền mà không sửa component | `<button>{t('auth.login')}</button>` |
| `l10n` | Dịch và điều chỉnh cho một locale cụ thể | `vi-VN`: `31/12/2026`, `1.000.000 ₫` |

**Không tốt: hardcode text**

```tsx
export function LoginButton() {
  return <button>Đăng nhập</button>;
}
```

**Tốt hơn: text là dữ liệu theo locale**

```tsx
export function LoginButton() {
  const { t } = useTranslation('auth');

  return <button>{t('loginButton')}</button>;
}
```

### Locale không chỉ là language

`en-US`, `en-GB`, `vi-VN`, `ja-JP` khác nhau ở format ngày, tiền, số, timezone, đơn vị đo và đôi khi cả nội dung.

```txt
en-US: 12/31/2026, $1,000.00
vi-VN: 31/12/2026, 1.000,00 US$
ja-JP: 2026/12/31, $1,000.00
```

---

## 3. 🧩 Main Concepts

### 3.1 Translation keys và namespaces

Nên tổ chức translation theo locale + namespace để dễ scale theo feature.

```txt
src/
└── i18n/
    ├── index.ts
    ├── formatters.ts
    └── locales/
        ├── en/
        │   ├── common.json
        │   ├── auth.json
        │   └── dashboard.json
        ├── vi/
        │   ├── common.json
        │   ├── auth.json
        │   └── dashboard.json
        └── ja/
            ├── common.json
            ├── auth.json
            └── dashboard.json
```

| Pattern | Khi dùng | Ví dụ key |
|---|---|---|
| `common` namespace | Button/label dùng toàn app | `useTranslation('common'); t('save')` |
| Feature namespace | Text thuộc một domain rõ ràng | `useTranslation('auth'); t('loginTitle')` |
| Context-rich key | Khi một từ có nhiều nghĩa | `useTranslation('trading'); t('orderBook')` |

> ✅ Convention dùng trong topic này: **namespace nằm ở file/hook**, key bên trong namespace là key ngắn có context đủ rõ. Ví dụ `useTranslation('auth'); t('loginTitle')`, không trộn lẫn với `t('auth.loginTitle')` nếu team chưa thống nhất.

⚠️ Tránh key quá chung:

```json
{
  "title": "Title"
}
```

✅ Key nên có ngữ cảnh:

```json
{
  "loginTitle": "Login to your account",
  "createButton": "Create order",
  "orderBookTitle": "Order book"
}
```

### 3.2 Interpolation

Dịch cả câu, không nối từng mảnh text trong code, vì thứ tự từ thay đổi theo ngôn ngữ.

❌ Before:

```tsx
return <p>{t('hello') + ' ' + userName + ', ' + t('welcomeBack')}</p>;
```

✅ After:

```json
{
  "welcomeBack": "Welcome back, {{name}}"
}
```

```tsx
return <p>{t('welcomeBack', { name: userName })}</p>;
```

### 3.3 Rich text translation với `Trans`

Không đưa raw HTML từ translator vào `dangerouslySetInnerHTML`. Nếu câu dịch cần link, bold, hoặc component React, dùng `Trans` để map component an toàn.

❌ Không tốt:

```tsx
return <p dangerouslySetInnerHTML={{ __html: t('termsHtml') }} />;
```

✅ Tốt hơn:

```json
{
  "acceptTerms": "I agree to the <termsLink>terms</termsLink>"
}
```

```tsx
import { Trans } from 'react-i18next';

export function TermsText() {
  return (
    <Trans
      i18nKey="acceptTerms"
      ns="auth"
      components={{
        termsLink: <a href="/terms" />,
      }}
    />
  );
}
```

### 3.4 Pluralization

Không tự viết `"item(s)"`. Mỗi ngôn ngữ có plural rule khác nhau.

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

💡 Production example: message trong cart/order nên để i18n library quyết định plural form.

```tsx
export function CartSummary({ count }: { count: number }) {
  const { t } = useTranslation('cart');

  return <p>{t('itemsInCart', { count })}</p>;
}
```

### 3.5 Context, tone và formal/casual variants

Một số ngôn ngữ cần biến thể theo ngữ cảnh, giới tính, mức độ trang trọng hoặc domain. Không nên dùng lại một key chỉ vì English giống nhau.

```json
{
  "saveButton": "Save",
  "saveDraftAction": "Save draft",
  "formalGreeting": "Welcome, {{name}}",
  "casualGreeting": "Hi {{name}}"
}
```

💡 Với sản phẩm fintech/trading/B2B, wording thường phải được product/legal review. Key nên mang đủ context để translator không đoán.

### 3.6 Fallback language

Fallback giúp UI không crash khi thiếu bản dịch.

```txt
vi -> en -> key
```

| Case | Hành vi nên có |
|---|---|
| Thiếu `vi.auth.loginButton` | Hiển thị bản `en` |
| Thiếu cả `en` | Hiển thị key hoặc marker dễ phát hiện |
| Production build | Log/report missing key để fix workflow |

### 3.7 Locale detection

Thứ tự phổ biến:

```txt
URL locale -> user profile -> localStorage -> browser language -> default language
```

| Nguồn | Ưu điểm | Lưu ý |
|---|---|---|
| URL, ví dụ `/vi/dashboard` | Tốt cho SEO, share link, SSR | Cần routing strategy rõ |
| User profile | Đúng preference đã lưu | Cần chờ auth/user API |
| `localStorage` | Nhanh cho dashboard/internal app | Không tốt cho SSR ban đầu |
| Browser language | Default hợp lý | Không luôn đúng với user intent |

---

## 4. 🧪 Practical TypeScript/JavaScript Examples

### 4.1 React setup với `react-i18next`

```bash
npm install i18next react-i18next i18next-browser-languagedetector
```

```json
// src/i18n/locales/en/auth.json
{
  "loginButton": "Login",
  "welcome": "Welcome, {{name}}"
}
```

```json
// src/i18n/locales/vi/auth.json
{
  "loginButton": "Đăng nhập",
  "welcome": "Xin chào, {{name}}"
}
```

```json
// src/i18n/locales/ja/auth.json
{
  "loginButton": "ログイン",
  "welcome": "{{name}}さん、おかえりなさい"
}
```

```ts
// src/i18n/index.ts
import i18n from 'i18next';
import LanguageDetector from 'i18next-browser-languagedetector';
import { initReactI18next } from 'react-i18next';

import enAuth from './locales/en/auth.json';
import enCommon from './locales/en/common.json';
import jaAuth from './locales/ja/auth.json';
import jaCommon from './locales/ja/common.json';
import viAuth from './locales/vi/auth.json';
import viCommon from './locales/vi/common.json';

i18n
  .use(LanguageDetector)
  .use(initReactI18next)
  .init({
    fallbackLng: 'en',
    supportedLngs: ['en', 'vi', 'ja'],
    defaultNS: 'common',
    ns: ['common', 'auth'],
    resources: {
      en: { common: enCommon, auth: enAuth },
      vi: { common: viCommon, auth: viAuth },
      ja: { common: jaCommon, auth: jaAuth },
    },
    detection: {
      order: ['path', 'localStorage', 'navigator'],
      lookupFromPathIndex: 0,
      lookupLocalStorage: 'language',
      caches: ['localStorage'],
    },
    interpolation: {
      escapeValue: false, // React đã escape output text.
    },
  });

export default i18n;
```

```ts
// main.tsx
import './i18n';
```

```tsx
import { useTranslation } from 'react-i18next';

export function LoginHeader({ name }: { name: string }) {
  const { t } = useTranslation('auth');

  return (
    <header>
      <h1>{t('loginButton')}</h1>
      <p>{t('welcome', { name })}</p>
    </header>
  );
}
```

### 4.2 Date, time, number, currency bằng `Intl`

Không format thủ công bằng string vì locale khác nhau về dấu phân cách, thứ tự ngày/tháng/năm và currency symbol.

```ts
export function formatDate(value: Date, locale: string, timeZone = 'UTC') {
  return new Intl.DateTimeFormat(locale, {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    timeZone,
  }).format(value);
}

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

export function formatCompactNumber(value: number, locale: string) {
  return new Intl.NumberFormat(locale, {
    notation: 'compact',
    maximumFractionDigits: 1,
  }).format(value);
}

export function formatRelativeDays(value: number, locale: string) {
  return new Intl.RelativeTimeFormat(locale, { numeric: 'auto' }).format(
    value,
    'day'
  );
}

export function formatList(values: string[], locale: string) {
  return new Intl.ListFormat(locale, {
    style: 'long',
    type: 'conjunction',
  }).format(values);
}
```

```ts
formatDate(new Date('2026-05-16T00:00:00Z'), 'en-US', 'UTC'); // 05/16/2026
formatDate(new Date('2026-05-16T00:00:00Z'), 'vi-VN', 'UTC'); // 16/05/2026
formatCurrency(100000, 'vi-VN', 'VND'); // 100.000 ₫
formatCompactNumber(1200000, 'en-US'); // 1.2M
formatRelativeDays(-1, 'en-US'); // yesterday
formatList(['React', 'TypeScript', 'Vite'], 'en-US'); // React, TypeScript, and Vite
```

🔥 Senior point: gom formatter vào module chung hoặc hook như `useFormatters()` để table, chart, form, export, email preview dùng cùng một quy tắc.

Nếu cần sort/search theo locale, dùng `Intl.Collator` thay vì so sánh string thủ công:

```ts
const collator = new Intl.Collator('vi-VN', {
  sensitivity: 'base',
  numeric: true,
});

['Tầng 10', 'Tầng 2'].sort(collator.compare);
```

### 4.3 Language switcher

Khi đổi language, cần cập nhật i18n instance, persisted preference, `html lang`, `html dir`, và route nếu locale nằm trong URL.

```tsx
import { useTranslation } from 'react-i18next';

const rtlLanguages = new Set(['ar', 'he', 'fa']);

function syncHtmlLocale(language: string) {
  const baseLanguage = language.split('-')[0].toLowerCase();

  document.documentElement.lang = language;
  document.documentElement.dir = rtlLanguages.has(baseLanguage) ? 'rtl' : 'ltr';
}

export function LanguageSwitcher() {
  const { i18n } = useTranslation();

  async function changeLanguage(language: string) {
    await i18n.changeLanguage(language);
    localStorage.setItem('language', language);
    syncHtmlLocale(language);
  }

  return (
    <select
      aria-label="Language"
      value={i18n.resolvedLanguage}
      onChange={(event) => changeLanguage(event.target.value)}
    >
      <option value="en">English</option>
      <option value="vi">Tiếng Việt</option>
      <option value="ja">日本語</option>
    </select>
  );
}
```

### 4.4 RTL bằng CSS logical properties

❌ Before:

```css
.card {
  margin-left: 16px;
  text-align: left;
}
```

✅ After:

```css
.card {
  margin-inline-start: 16px;
  text-align: start;
}
```

Các vùng cần test kỹ khi bật RTL:

- grid/flex layout
- drawer/sidebar
- icon mũi tên và breadcrumb
- table, chart, pagination
- input, validation message
- animation direction

### 4.5 Lazy load translation theo locale/namespace

Không nên đưa toàn bộ ngôn ngữ vào initial bundle.

```txt
10 languages x 50KB = 500KB translation JSON
```

```ts
import i18n from './i18n';

export async function loadTranslations(language: string, namespace: string) {
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

Production refinement:

```ts
export async function ensureDashboardTranslations(language: string) {
  await Promise.all([
    loadTranslations(language, 'common'),
    loadTranslations(language, 'dashboard'),
  ]);
}
```

---

## 5. 🚀 Production Notes / React & Next.js Implications

### React implications

| Vấn đề | Hướng xử lý |
|---|---|
| Component re-render khi đổi language | Bình thường, nhưng tránh format nặng trong từng cell/table row |
| Table/list lớn format ngày tiền nhiều lần | Memoize formatter hoặc format ở selector/view-model |
| Hardcode text trong `aria-label`, placeholder, toast | Tất cả user-facing text đều phải qua translation |
| Dynamic import translation | Có loading state/suspense boundary phù hợp |

Ví dụ tối ưu formatter:

```tsx
import { useMemo } from 'react';
import { useTranslation } from 'react-i18next';

export function PriceCell({ value }: { value: number }) {
  const { i18n } = useTranslation();

  const formatter = useMemo(
    () =>
      new Intl.NumberFormat(i18n.resolvedLanguage, {
        style: 'currency',
        currency: 'USD',
      }),
    [i18n.resolvedLanguage]
  );

  return <span>{formatter.format(value)}</span>;
}
```

### SSR / Next.js considerations

| Chủ đề | Lưu ý |
|---|---|
| URL locale | Dùng `/vi/...`, `/en/...` cho SEO, canonical, share link |
| Server render | Locale phải được resolve trên server để tránh hydration mismatch |
| `localStorage` | Chỉ có ở client, không nên là nguồn duy nhất cho initial locale |
| Metadata | `title`, `description`, `openGraph`, `hreflang` cũng cần localized |
| Dynamic namespace | Load đúng namespace trước khi render route |
| Cookies/profile | Có thể dùng để nhớ language giữa request |
| SEO alternates | Thêm canonical và `hreflang` cho từng locale public page |

Ví dụ Next.js mental model:

```txt
request /vi/orders
-> server resolve locale = vi
-> load messages: common + order
-> render HTML lang="vi"
-> client hydrate cùng locale/messages
```

Ví dụ metadata route-level:

```tsx
export function ProductSeo({ locale }: { locale: string }) {
  return (
    <>
      <link rel="canonical" href={`https://example.com/${locale}/products`} />
      <link rel="alternate" hrefLang="en" href="https://example.com/en/products" />
      <link rel="alternate" hrefLang="vi" href="https://example.com/vi/products" />
    </>
  );
}
```

### Translation workflow

Khi app lớn, nên có quy trình rõ thay vì sửa JSON thủ công mãi:

```txt
Developer tạo key
-> export keys
-> translator dịch trong TMS
-> reviewer kiểm context
-> import translations
-> test missing key, layout, E2E
```

TMS thường gặp: **Lokalise**, **Phrase**, **Crowdin**, **Transifex**.

CI nên kiểm tra tự động:

```txt
- Missing keys giữa default locale và locale khác
- Unused keys bị bỏ quên
- JSON invalid
- Key naming không đúng convention
- Translation chứa HTML raw không được phép
```

---

## 6. ♿ Accessibility, Testing & Quality

### Accessibility

| Element | Cần dịch |
|---|---|
| Button/link text | `Save`, `Cancel`, `View details` |
| `aria-label` | Icon-only button, close modal |
| Form label/helper/error | Validation message theo locale |
| Toast/dialog | Nội dung trạng thái và lỗi |
| Document | `html lang`, `html dir` |

```tsx
<button aria-label={t('common.closeDialog')}>
  <XIcon aria-hidden="true" />
</button>
```

### Testing checklist

```txt
□ Missing translation key có fallback
□ Text dài không vỡ button, tab, menu, card
□ Date/time/number/currency đúng locale
□ Timezone đúng với business requirement
□ Language switch không làm mất state quan trọng
□ URL locale hoạt động nếu app dùng routing theo locale
□ RTL không làm ngược icon sai hoặc vỡ layout
□ Form validation, placeholder, aria-label đều được dịch
□ Email/PDF/export dùng đúng language
□ E2E ít nhất một flow chính với language khác default
```

Pseudo-locale giúp phát hiện hardcode text và overflow:

```txt
Login -> [!! Łôôôĝîîîn !!]
Save -> [!! Šââvêê !!]
```

---

## 7. ⚠️ Common Pitfalls

| Pitfall | Vì sao nguy hiểm | Cách sửa |
|---|---|---|
| Hardcode text trong component | Không đổi được locale, khó audit | Dùng `t('namespace.key')` |
| Dịch từng từ rồi nối chuỗi | Sai grammar ở nhiều ngôn ngữ | Dịch cả câu với interpolation |
| Key quá chung | Translator thiếu context | Key theo domain/action |
| Chỉ dịch text | Sai date, number, currency, timezone | Dùng `Intl` và formatter chung |
| Không test text dài | UI vỡ ở German/French/pseudo-locale | Visual regression/responsive test |
| Quên RTL | Arabic/Hebrew layout sai | `dir`, logical CSS, RTL QA |
| Load tất cả translations | Tăng initial bundle | Lazy load locale/namespace |
| Dùng `localStorage` cho SSR locale | Hydration mismatch | Resolve locale từ URL/cookie/request |
| Không có workflow dịch | Missing key, sai context, drift | TMS + review + CI check |
| Dùng raw translated HTML | XSS hoặc layout khó kiểm soát | Dùng `Trans`/component interpolation |
| RTL check theo full locale | `ar-SA` không match `ar` | Normalize base language trước |
| Date không set timezone | Ngày lệch theo máy user/server | Set timezone theo business rule |

Before/after cho lỗi phổ biến nhất:

```tsx
// ❌ Không tốt
<span>Submit</span>
```

```tsx
// ✅ Tốt hơn
<span>{t('common.submit')}</span>
```

```tsx
// ❌ Không tốt
<p>{t('hello')} {userName}, {t('welcomeBack')}</p>
```

```tsx
// ✅ Tốt hơn
<p>{t('auth.welcomeBack', { name: userName })}</p>
```

---


## 9. 🎤 Short Interview Answer

**"Theo em, i18n là thiết kế app để hỗ trợ nhiều ngôn ngữ từ kiến trúc, còn l10n là dịch và điều chỉnh cho từng locale cụ thể. Em thường tách text ra translation files theo locale và namespace, dùng key có context, hỗ trợ interpolation, pluralization, fallback language và language detection theo priority như URL, user profile, localStorage rồi browser language.**

**Em thấy điểm quan trọng là không chỉ dịch chữ. App production còn phải format date/time/number/currency bằng `Intl`, xử lý timezone rõ ràng, dùng `Trans` cho rich text an toàn, cập nhật `html lang`, `dir` cho RTL, dùng CSS logical properties, lazy load translation bundles để không phình initial bundle, và với Next.js thì resolve locale/messages ở server để tránh hydration mismatch. Khi scale, em sẽ thêm workflow với TMS như Lokalise/Phrase/Crowdin, CI check missing/unused keys, test pseudo-locale, text dài, accessibility label, RTL và ít nhất một E2E flow bằng language khác default."**
