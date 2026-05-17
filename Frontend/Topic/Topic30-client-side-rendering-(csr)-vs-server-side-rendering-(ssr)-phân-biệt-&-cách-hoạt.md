# Topic 30: CSR vs SSR - Phân Biệt & Cách Hoạt Động

## 🚀 Câu trả lời ngắn gọn

**CSR (Client-Side Rendering)** là mô hình server gửi HTML gần như rỗng và JavaScript bundle, sau đó browser tải JS, chạy JS, fetch data và render UI.

**SSR (Server-Side Rendering)** là mô hình server render sẵn HTML có nội dung, gửi về browser để user thấy content sớm hơn, sau đó JavaScript chạy trên client để hydrate và gắn tương tác.

Nói ngắn gọn:

```txt
🧠 CSR: render ở browser
🖥️ SSR: render HTML ở server, hydrate ở browser
```

CSR phù hợp với app nội bộ, dashboard, admin tool, app tương tác nhiều và không quá phụ thuộc SEO.  
SSR phù hợp với page cần SEO, content public, landing page, e-commerce, blog, marketplace hoặc page cần first content nhanh trên device yếu.

Senior/staff không nên chỉ chọn CSR hoặc SSR. Cần chọn theo từng route:

```txt
🔎 Public SEO page -> SSR/SSG/ISR
📊 Dashboard sau login -> CSR hoặc SSR nhẹ
📄 Content ít đổi -> SSG
♻️ Content đổi theo thời gian -> ISR
👤 Personalized/dynamic page -> SSR
🏝️ Interactive widget nhỏ -> partial hydration/islands
```

---

## 🧠 1. CSR hoạt động như thế nào?

Flow cơ bản:

```txt
1. User request /dashboard
2. Server/CDN trả HTML shell
3. Browser tải JS bundle
4. Browser parse và execute JS
5. App fetch API data
6. React/Vue render UI trong browser
7. User thấy content và tương tác
```

Ví dụ HTML ban đầu:

```html
<html>
  <body>
    <div id="root"></div>
    <script src="/assets/app.js"></script>
  </body>
</html>
```

> **Highlight:** CSR mạnh ở **interactivity/navigation**, yếu ở **initial load/SEO** nếu bundle lớn.

Vấn đề: trước khi JS tải và chạy xong, user có thể thấy màn hình trắng hoặc loading.

### ✅ Ưu điểm CSR

- Navigation sau lần load đầu thường nhanh vì không reload full page.
- Dễ làm app giàu tương tác: dashboard, trading screen, chat, admin tool.
- Dễ deploy static lên CDN.
- Server load thấp vì server chủ yếu serve file tĩnh và API.
- Kiến trúc frontend/backend tách biệt rõ.

### ⚠️ Nhược điểm CSR

- Initial load chậm nếu bundle lớn.
- SEO kém hơn nếu crawler không render JS đầy đủ hoặc page không có content ban đầu.
- User trên device yếu phải parse/execute nhiều JS.
- Dễ có blank screen nếu app không tối ưu loading state.
- Core Web Vitals có thể xấu, đặc biệt LCP và INP nếu JS nặng.

---

## 🖥️ 2. SSR hoạt động như thế nào?

Flow cơ bản:

```txt
1. User request /products/123
2. Server fetch data cần thiết
3. Server render React/Vue thành HTML string/stream
4. Browser nhận HTML có content và hiển thị sớm
5. Browser tải JS bundle
6. Hydration chạy để gắn event handlers
7. Page trở nên interactive
```

Ví dụ HTML SSR:

```html
<html>
  <body>
    <div id="root">
      <h1>iPhone 16</h1>
      <p>Product description...</p>
    </div>
    <script src="/assets/product.js"></script>
  </body>
</html>
```

### 💧 Hydration là gì?

Hydration là quá trình client JavaScript “gắn lại” logic React/Vue vào HTML đã render từ server.

HTML SSR giúp user thấy nội dung sớm, nhưng page chưa tương tác đầy đủ cho đến khi hydration xong.

```txt
👀 HTML visible != 🖱️ fully interactive
```

> **Highlight:** SSR giúp user **thấy content sớm**, nhưng vẫn phải trả **hydration cost** để tương tác.

### ✅ Ưu điểm SSR

- User thấy content sớm hơn, tốt cho perceived performance.
- SEO tốt vì HTML đã có nội dung.
- Social preview/Open Graph dễ hoạt động.
- Tốt cho device yếu vì phần render đầu được làm trên server.
- Có thể giảm blank screen.

### ⚠️ Nhược điểm SSR

- Server load cao hơn vì phải render theo request.
- TTFB có thể chậm nếu fetch data hoặc render server chậm.
- Setup phức tạp hơn CSR.
- Dễ gặp hydration mismatch.
- Code phải chạy được trong cả server và browser.
- Cần cache tốt, nếu không dễ overload.

---

## ⚖️ 3. So sánh CSR vs SSR

| Tiêu chí | CSR | SSR |
|---|---|---|
| Render lần đầu | Browser | Server |
| HTML ban đầu | Shell/rỗng | Có content |
| SEO | Yếu hơn | Tốt hơn |
| First content | Thường chậm hơn | Thường nhanh hơn |
| TTFB | Thường nhanh | Có thể chậm hơn |
| Server load | Thấp | Cao hơn |
| JS requirement | Rất phụ thuộc JS | Vẫn cần JS để hydrate |
| Navigation sau load | Nhanh | Tùy framework/cache |
| Complexity | Thấp hơn | Cao hơn |
| Phù hợp | App sau login, dashboard | Public page, SEO, e-commerce |

Senior point: SSR không tự động nhanh hơn mọi mặt. SSR thường cải thiện **FCP/LCP**, nhưng có thể làm **TTFB** tăng và vẫn bị **hydration cost** nếu JS bundle lớn.

### 🧩 Bảng nhớ nhanh

```txt
CSR = Client làm nhiều việc hơn
SSR = Server làm render đầu tiên
SSG = Build time render
ISR = Static + revalidate
Streaming = Gửi HTML từng phần
Hydration = Gắn JS vào HTML server-rendered
RSC = Component chạy server, giảm JS xuống client
```

---

## 🧱 4. Các mô hình rendering hiện đại

### 📄 SSG - Static Site Generation

Render HTML tại build time.

Phù hợp:

- blog
- docs
- marketing page
- landing page ít đổi

Ưu điểm:

- rất nhanh
- cache CDN tốt
- server cost thấp

Nhược điểm:

- content thay đổi cần rebuild
- không phù hợp dữ liệu cá nhân hóa theo request

### ♻️ ISR - Incremental Static Regeneration

Kết hợp SSG và cập nhật định kỳ.

Ví dụ Next.js:

```txt
Product page được render tĩnh, sau 60s có thể revalidate.
```

Phù hợp:

- product detail
- news/category page
- page có content đổi nhưng không cần realtime tuyệt đối

### 🖥️ SSR per request

Render mỗi request.

Phù hợp:

- dữ liệu cá nhân hóa
- auth/session dependent page
- giá/tồn kho nhạy thời gian
- A/B testing theo request

Nhược điểm là cần cache và tối ưu server tốt.

### 🌊 Streaming SSR

Server gửi HTML theo từng chunk thay vì chờ tất cả data xong.

```txt
Header/shell render trước
Content async stream sau
```

Ưu điểm:

- user thấy shell/content sớm
- tốt với React 18 Suspense
- giảm cảm giác chờ

### 🏝️ Partial hydration / Islands architecture

Chỉ hydrate những component cần tương tác.

Ví dụ:

```txt
Article page: HTML static
Interactive search box: hydrate
Comment widget: hydrate
```

Phù hợp:

- content-heavy site
- docs/blog/news
- page có ít interactive components

Framework: Astro, Qwik, một số pattern trong Next/Remix.

### 🧩 React Server Components

React Server Components cho phép một phần component chạy ở server và không gửi JS của phần đó xuống client.

Ý nghĩa:

- giảm client bundle
- fetch data gần server hơn
- tách server-only logic khỏi client component

Nhưng cần hiểu rõ boundary:

```txt
🖥️ Server Component: fetch data, render static UI, không dùng browser API
🧠 Client Component: useState, useEffect, event handlers, browser API
```

---

## 💧 5. Hydration mismatch

Hydration mismatch xảy ra khi HTML server render khác HTML client render lần đầu.

Ví dụ nguyên nhân:

- 🕒 dùng `Date.now()` trong render
- 🎲 dùng `Math.random()` trong render
- 🌐 đọc `window`, `localStorage` khi render server
- 🌍 server và client khác locale/timezone
- 🚩 feature flag khác giá trị giữa server/client
- 🔄 data trên server và client không đồng bộ

Ví dụ không tốt:

```tsx
export function Clock() {
  return <span>{new Date().toLocaleTimeString()}</span>;
}
```

Server render một giờ, client render giờ khác -> mismatch.

Cách xử lý:

- ✅ render deterministic output trên server
- ✅ đưa logic browser-only vào `useEffect`
- ✅ dùng placeholder cho phần phụ thuộc client
- ✅ đảm bảo server/client dùng cùng data snapshot
- ✅ kiểm soát timezone/locale khi format

Ví dụ:

```tsx
export function ClientClock() {
  const [time, setTime] = useState<string | null>(null);

  useEffect(() => {
    setTime(new Date().toLocaleTimeString());
  }, []);

  return <span>{time ?? '--:--'}</span>;
}
```

---

## 🌐 6. Browser API trong SSR

Trong SSR, code render chạy trên server, nên không có:

```txt
window
document
localStorage
sessionStorage
navigator
IntersectionObserver
ResizeObserver
```

Không tốt:

```tsx
const theme = localStorage.getItem('theme');
```

Tốt hơn:

```tsx
useEffect(() => {
  const theme = localStorage.getItem('theme');
  setTheme(theme);
}, []);
```

Hoặc lấy theme từ cookie trên server để render đúng ngay từ đầu.

Staff point: nếu giá trị ảnh hưởng UI ban đầu như theme, locale, currency, auth state, nên đưa vào request/cookie/header để server render đúng, tránh flicker.

> **Highlight:** Nếu dữ liệu ảnh hưởng HTML đầu tiên, ưu tiên lấy từ **cookie/header/request** thay vì đợi `useEffect`.

---

## 🔌 7. Data fetching

### 🧠 CSR data fetching

```txt
HTML shell -> JS loads -> fetch API -> render data
```

Ưu điểm:

- đơn giản
- dễ cache bằng React Query/SWR
- phù hợp dashboard sau login

Nhược điểm:

- waterfall dễ xảy ra
- content đến muộn
- SEO yếu nếu data là content public

### 🖥️ SSR data fetching

```txt
request -> server fetch data -> render HTML -> browser hydrate
```

Ưu điểm:

- HTML có data ngay
- SEO tốt
- giảm loading spinner ban đầu

Nhược điểm:

- TTFB phụ thuộc data source
- cần timeout/retry/cache
- server dễ bị chậm nếu gọi nhiều API nối tiếp

Best practice:

- ✅ fetch song song khi có thể
- ✅ cache response/server render
- ✅ tránh waterfall
- ✅ đặt timeout cho upstream API
- ✅ dùng stale-while-revalidate nếu data không cần realtime

---

## 🗄️ 8. Caching strategy

SSR mà không cache dễ tốn server và chậm.

Các lớp cache:

```txt
🌐 Browser cache
🧊 CDN/Edge cache
🖥️ Server response cache
🔌 Data/API cache
⚛️ React cache/framework cache
```

Ví dụ strategy:

```txt
📣 Marketing page -> SSG + CDN cache
🛍️ Product detail -> ISR 60s + CDN
🔎 Search result -> SSR + short cache
👤 User dashboard -> CSR + API cache per user
💳 Checkout/payment -> SSR/CSR dynamic, no shared cache
```

Cần cẩn thận không cache nhầm dữ liệu cá nhân:

```txt
✅ Public cache: product, blog, category
🔒 Private/no-store: account, portfolio, order, payment
```

---

## 📊 9. Performance metrics cần nói

CSR/SSR nên được đánh giá bằng metrics, không chỉ cảm tính.

- ⏱️ **TTFB:** thời gian nhận byte đầu tiên. SSR có thể làm TTFB tăng.
- 🎨 **FCP:** lần đầu có content render.
- 🖼️ **LCP:** phần tử lớn nhất render xong. SSR/SSG thường giúp LCP tốt hơn.
- 🖱️ **TTI:** thời điểm page tương tác ổn định.
- ⚡ **INP:** độ phản hồi tương tác. JS/hydration nặng có thể làm INP xấu.
- 📐 **CLS:** layout shift. SSR không tự động giải quyết CLS nếu image/font/layout chưa ổn.

Senior point:

```txt
✅ SSR improves "see content early".
⚠️ It does not automatically reduce JavaScript cost.
💧 Hydration can still block interactivity.
```

---

## 🧭 10. Khi nào chọn CSR, SSR, SSG, ISR?

### 🧠 Chọn CSR khi

- app nằm sau login
- SEO không quan trọng
- tương tác dày đặc
- dữ liệu cá nhân hóa nhiều
- team muốn deploy static đơn giản
- ví dụ: admin dashboard, trading terminal, internal CRM

### 🖥️ Chọn SSR khi

- cần SEO
- cần social preview
- content phụ thuộc request
- cần first content nhanh
- page có personalization nhẹ
- ví dụ: product page có price theo location, marketplace listing, profile public

### 📄 Chọn SSG khi

- content ít đổi
- không cần personalization
- cần tốc độ cao và chi phí thấp
- ví dụ: docs, blog, landing page

### ♻️ Chọn ISR khi

- content public có thay đổi định kỳ
- chấp nhận stale ngắn
- muốn performance gần SSG
- ví dụ: e-commerce product page, category page, news listing

### 🧬 Chọn hybrid khi

Một app thực tế thường cần nhiều mode:

```txt
/                    -> 📄 SSG
/blog/[slug]         -> 📄 SSG / ♻️ ISR
/products/[id]       -> ♻️ ISR / 🖥️ SSR
/search              -> 🖥️ SSR
/dashboard           -> 🧠 CSR
/checkout            -> 🔒 SSR/CSR dynamic, no-store
```

---

## 🚨 11. Common mistakes

### ⚠️ Nghĩ SSR luôn nhanh hơn CSR

Sai. SSR giúp content xuất hiện sớm hơn, nhưng nếu server chậm hoặc hydration nặng thì UX vẫn tệ.

### 🌐 Render browser-only logic trên server

Ví dụ `window.innerWidth`, `localStorage`, `navigator.language` trong render.

### 💧 Không xử lý hydration mismatch

Random value, current date/time, locale khác nhau giữa server/client đều có thể gây mismatch.

### 🗄️ SSR nhưng không cache

Mỗi request render từ đầu, gọi nhiều API, không cache -> server quá tải, TTFB cao.

### 📦 CSR bundle quá lớn

Dashboard CSR vẫn cần code splitting, lazy loading, route splitting, bundle analysis.

### 🔒 Cache nhầm private data

Đây là lỗi nghiêm trọng. Dữ liệu user/account/order/payment không được cache public.

### 📊 Không đo metrics

Không nên tranh luận CSR vs SSR bằng cảm tính. Phải đo TTFB, LCP, INP, bundle size, server latency.

---

## 🎤 12. Câu trả lời senior nên nói

**"CSR là browser render UI sau khi tải và chạy JS, phù hợp app tương tác nhiều như dashboard hoặc admin sau login. SSR là server render HTML có content trước, sau đó client hydrate để tương tác, phù hợp page public cần SEO, first content nhanh hoặc social preview. Trade-off là SSR cải thiện FCP/LCP và SEO nhưng tăng server complexity, TTFB và có hydration cost; CSR đơn giản, deploy static dễ, navigation mượt nhưng initial load và SEO yếu hơn nếu bundle/data lớn. Ở senior/staff level, em không chọn một mode cho toàn app mà chọn theo từng route: SSG cho content tĩnh, ISR cho content public đổi định kỳ, SSR cho dynamic SEO/personalized page, CSR cho app sau login. Em cũng sẽ thiết kế cache, data fetching, hydration boundary và đo bằng TTFB, LCP, INP thay vì đoán."**

---

## ✅ 13. Checklist phỏng vấn

| Câu hỏi | Trả lời ngắn |
|---|---|
| CSR render ở đâu? | CSR render UI trong browser sau khi tải và chạy JavaScript. |
| SSR render ở đâu? | SSR render HTML có content trên server rồi gửi về browser. |
| Hydration là gì? | Client JS gắn event/state vào HTML đã render từ server. |
| HTML visible khác fully interactive thế nào? | User thấy content trước, nhưng phải đợi hydration xong mới tương tác đầy đủ. |
| CSR mạnh ở đâu? | App tương tác nhiều, sau login, dashboard, deploy static đơn giản. |
| CSR yếu ở đâu? | Initial load, SEO, bundle lớn và device yếu. |
| SSR mạnh ở đâu? | SEO, social preview, first content nhanh, page public/dynamic theo request. |
| SSR yếu ở đâu? | Tăng server load, TTFB, complexity và hydration cost. |
| SSR có luôn nhanh hơn CSR không? | Không; SSR chỉ giúp content sớm hơn, vẫn có thể chậm nếu server/hydration nặng. |
| TTFB là gì? | Thời gian nhận byte đầu tiên; SSR có thể làm TTFB tăng. |
| FCP/LCP là gì? | FCP là content đầu tiên; LCP là phần tử lớn nhất render xong. |
| INP/CLS là gì? | INP đo độ phản hồi tương tác; CLS đo layout shift. |
| Hydration mismatch do đâu? | Server/client render khác nhau vì `Date.now`, `Math.random`, browser API, locale, data lệch. |
| Browser API dùng thế nào trong SSR? | Không dùng trực tiếp trong render server; đưa vào `useEffect` hoặc lấy từ request/cookie. |
| CSR data fetching khác SSR thế nào? | CSR fetch sau khi JS chạy; SSR fetch trên server trước khi gửi HTML. |
| SSR cần cache gì? | CDN/edge cache, server response cache, data/API cache và framework cache. |
| Tránh cache private data thế nào? | Dùng `private`, `no-store`, cache theo user hoặc không cache account/order/payment. |
| SSG là gì? | Render HTML tại build time, hợp docs/blog/landing page ít đổi. |
| ISR là gì? | Static page có revalidate định kỳ, hợp product/news/category đổi không quá realtime. |
| Streaming SSR là gì? | Server gửi HTML từng phần để user thấy shell/content sớm hơn. |
| Partial hydration/islands là gì? | Chỉ hydrate widget cần tương tác thay vì toàn page. |
| RSC boundary là gì? | Server Component chạy server, không dùng hooks/browser API; Client Component dùng interactivity. |
| Chọn rendering mode theo route thế nào? | Public SEO dùng SSG/ISR/SSR; dashboard sau login dùng CSR; checkout dùng dynamic no-store. |
| Ví dụ route architecture thực tế? | `/blog` SSG, `/products/[id]` ISR/SSR, `/search` SSR, `/dashboard` CSR, `/checkout` no-store. |
