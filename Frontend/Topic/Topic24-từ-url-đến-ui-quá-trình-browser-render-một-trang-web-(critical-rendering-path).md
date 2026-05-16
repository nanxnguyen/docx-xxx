# Topic 24: Từ URL đến UI - Browser Render Một Trang Web

## Câu trả lời ngắn gọn

Khi user nhập URL và nhấn Enter, browser sẽ đi qua 3 nhóm bước chính:

1. **Network:** tìm IP bằng DNS, tạo kết nối TCP/TLS, gửi HTTP request và nhận HTML response.
2. **Parsing:** parse HTML thành DOM, parse CSS thành CSSOM, tải và chạy JavaScript nếu có.
3. **Rendering:** kết hợp DOM + CSSOM thành render tree, tính layout, paint pixels và composite layers để hiển thị UI.

**Critical Rendering Path** là chuỗi công việc tối thiểu browser phải làm để render nội dung đầu tiên lên màn hình. Muốn trang load nhanh thì phải giảm tài nguyên blocking, giảm JS/CSS nặng, tối ưu ảnh/font và đo bằng các metrics như **FCP**, **LCP**, **CLS**, **INP**.

---

## 1. Network: Từ URL đến HTML

### 1. DNS Lookup

Browser cần đổi domain thành IP.

Ví dụ:

```txt
example.com -> 93.184.216.34
```

Browser sẽ kiểm tra cache theo thứ tự:

```txt
Browser cache -> OS cache -> Router cache -> DNS server
```

### 2. TCP Handshake

Browser tạo kết nối TCP với server bằng 3 bước:

```txt
Client -> SYN
Server -> SYN-ACK
Client -> ACK
```

Mục tiêu là xác nhận hai bên có thể giao tiếp ổn định.

### 3. TLS Handshake

Nếu URL là `https`, browser và server sẽ thực hiện TLS handshake:

- Server gửi certificate.
- Browser verify certificate.
- Hai bên thống nhất key mã hóa.
- Kết nối an toàn được thiết lập.

### 4. HTTP Request / Response

Browser gửi request:

```http
GET / HTTP/1.1
Host: example.com
Accept: text/html
```

Server xử lý và trả HTML:

```http
HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>...</html>
```

Sau khi nhận HTML, browser bắt đầu parse ngay, không cần đợi toàn bộ file tải xong.

---

## 2. Parsing: HTML, CSS, JavaScript

### 1. HTML -> DOM

Browser đọc HTML từ trên xuống dưới và tạo **DOM tree**.

Ví dụ:

```html
<body>
  <h1>Hello</h1>
  <p>World</p>
</body>
```

Thành:

```txt
Document
└── html
    └── body
        ├── h1
        └── p
```

DOM mô tả cấu trúc nội dung của page.

### 2. CSS -> CSSOM

Browser tải CSS và parse thành **CSSOM tree**.

CSS là **render-blocking**, vì browser cần biết style trước khi vẽ UI.

Ví dụ:

```css
h1 {
  color: red;
}
```

CSSOM giúp browser biết element nào có style nào.

### 3. JavaScript Execution

JavaScript có thể đọc/sửa DOM và CSSOM, nên nó có thể chặn quá trình parse/render.

Các loại script:

```html
<script src="app.js"></script>
```

- Chặn HTML parsing.
- Browser tải, parse và chạy JS trước khi tiếp tục parse HTML.

```html
<script async src="app.js"></script>
```

- Tải song song.
- Chạy ngay khi tải xong.
- Không đảm bảo thứ tự.

```html
<script defer src="app.js"></script>
```

- Tải song song.
- Chạy sau khi HTML parse xong.
- Giữ đúng thứ tự script.
- Thường phù hợp cho app JS chính.

---

## 3. Rendering: Từ DOM/CSSOM đến UI

### 1. Render Tree

Browser kết hợp:

```txt
DOM + CSSOM -> Render Tree
```

Render tree chỉ chứa các node cần hiển thị.

Không có trong render tree:

- `<head>`
- `<script>`
- element `display: none`

Lưu ý: `visibility: hidden` vẫn chiếm layout nên vẫn có thể nằm trong render tree.

### 2. Layout / Reflow

Browser tính kích thước và vị trí của từng element:

```txt
width, height, x, y, margin, padding, border
```

Layout bị chạy lại khi có thay đổi ảnh hưởng geometry, ví dụ:

- đổi width/height
- đổi font-size
- thêm/xóa DOM node
- resize viewport

### 3. Paint

Browser vẽ từng element thành pixels:

- text
- color
- border
- background
- shadow
- image

Paint tốn chi phí nếu UI phức tạp hoặc thay đổi nhiều vùng lớn.

### 4. Composite

Browser ghép các layer lại thành frame cuối cùng để hiển thị.

Một số thuộc tính thường được GPU xử lý tốt:

```css
transform: translateX(10px);
opacity: 0.8;
```

Vì vậy animation nên ưu tiên `transform` và `opacity`, tránh animate `width`, `height`, `top`, `left`.

---

## 4. Critical Rendering Path

Critical Rendering Path là luồng tối thiểu để browser render nội dung đầu tiên:

```txt
HTML
 -> DOM
 -> CSS
 -> CSSOM
 -> Render Tree
 -> Layout
 -> Paint
 -> Composite
 -> UI
```

Các tài nguyên ảnh hưởng mạnh nhất:

- HTML document
- CSS blocking
- JavaScript blocking
- font
- image quan trọng như hero image

Mục tiêu tối ưu là cho user thấy nội dung hữu ích càng sớm càng tốt.

---

## 5. Các lỗi thường gặp

### Script blocking

Sai:

```html
<head>
  <script src="main.js"></script>
</head>
```

Script này chặn HTML parsing.

Tốt hơn:

```html
<script defer src="main.js"></script>
```

### CSS quá lớn

CSS lớn làm browser chờ lâu trước khi render.

Cách tối ưu:

- tách critical CSS
- remove unused CSS
- minify CSS
- preload CSS quan trọng nếu cần

### Layout thrashing

Layout thrashing xảy ra khi code liên tục đọc layout rồi ghi style.

Ví dụ không tốt:

```js
const height = element.offsetHeight;
element.style.height = height + 10 + 'px';
const newHeight = element.offsetHeight;
```

Cách tốt hơn là batch reads và writes riêng.

### DOM quá lớn

DOM quá nhiều node làm layout và paint chậm.

Nên:

- chia component hợp lý
- dùng virtualization cho list lớn
- tránh render dữ liệu không nhìn thấy

---

## 6. Metrics cần biết

- **TTFB (Time To First Byte):** thời gian từ request đến byte đầu tiên từ server.
- **FCP (First Contentful Paint):** lần đầu browser render text/image/content.
- **LCP (Largest Contentful Paint):** thời gian render phần tử lớn nhất trong viewport.
- **CLS (Cumulative Layout Shift):** mức độ layout bị nhảy.
- **INP (Interaction to Next Paint):** độ phản hồi khi user tương tác.
- **TTI (Time To Interactive):** thời điểm page có thể tương tác ổn định.

Trong phỏng vấn senior, nên nhấn mạnh **LCP, CLS, INP** vì chúng gắn trực tiếp với Core Web Vitals.

---

## 7. Cách tối ưu

### Network

- Dùng CDN cho static assets.
- Bật compression: gzip hoặc brotli.
- Cache assets bằng `Cache-Control`.
- Dùng HTTP/2 hoặc HTTP/3.
- Dùng `preconnect` cho domain quan trọng.

```html
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```

### CSS

- Inline critical CSS cho above-the-fold nếu cần.
- Minify CSS.
- Remove unused CSS.
- Tránh import CSS quá nhiều tầng.

### JavaScript

- Dùng `defer` cho script chính.
- Code splitting theo route.
- Lazy load component nặng.
- Tree-shaking.
- Giảm third-party scripts.

### Images / Fonts

- Dùng WebP/AVIF.
- Set width/height cho image để tránh CLS.
- Lazy load ảnh ngoài viewport.
- Preload hero image hoặc font quan trọng.

```html
<link rel="preload" as="image" href="/hero.webp">
```

---

## 8. Câu trả lời senior nên nói

**"Khi user nhập URL, browser sẽ resolve DNS, tạo TCP/TLS connection, gửi HTTP request và nhận HTML. Sau đó browser parse HTML thành DOM, parse CSS thành CSSOM, JavaScript có thể block parsing nếu không dùng async/defer. DOM và CSSOM được kết hợp thành render tree, browser tính layout, paint pixels và composite layers để hiển thị UI. Critical Rendering Path là chuỗi tối thiểu để render nội dung đầu tiên, nên tối ưu bằng cách giảm render-blocking CSS/JS, dùng defer, code splitting, preload resource quan trọng, tối ưu image/font, cache/CDN và theo dõi FCP, LCP, CLS, INP."**

---

## 9. Checklist phỏng vấn

```txt
□ Nói được flow: DNS -> TCP -> TLS -> HTTP -> HTML
□ Giải thích DOM, CSSOM, render tree
□ Biết CSS render-blocking
□ Biết JS parser-blocking và khác nhau giữa async/defer
□ Giải thích layout, paint, composite
□ Biết Critical Rendering Path là gì
□ Biết FCP, LCP, CLS, INP
□ Biết cách tối ưu CSS, JS, image, font, cache, CDN
□ Biết tránh layout thrashing và DOM quá lớn
```



**📋 Tóm tắt 12 Bước từ URL → UI:**

```
1. DNS Lookup       → Resolve domain → IP
2. TCP Handshake    → Establish connection (SYN, SYN-ACK, ACK)
3. TLS Handshake    → Secure connection (HTTPS)
4. HTTP Request     → Browser → Server
5. Server Process   → Generate response
6. HTTP Response    → Server → Browser (HTML)
7. HTML Parse       → DOM Tree
8. CSS Parse        → CSSOM Tree
9. JS Execution     → Modify DOM/CSSOM (nếu có)
10. Render Tree     → DOM + CSSOM = Render Tree
11. Layout          → Tính toán vị trí & kích thước
12. Paint+Composite → Vẽ pixels lên màn hình → ✅ USER SEES UI!
```

**🎯 Critical Rendering Path:** `HTML → DOM + CSS → CSSOM = Render Tree → Layout → Paint`

**⚡ Tối ưu:** Minimize critical resources, reduce bytes, optimize path length!

---
