# 🌍 Q36: Từ URL đến UI - Quá Trình Browser Render Một Trang Web (Critical Rendering Path)

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (4-5 phút):**

**"Từ URL → UI gồm: Network (DNS, TCP, TLS, HTTP), Parsing (HTML → DOM, CSS → CSSOM), Rendering (Layout, Paint, Composite). Critical Rendering Path optimize = faster First Paint."**

**🔑 12 Bước Chính:**

**PHASE 1: NETWORK (~300-1000ms)**

**1. DNS Lookup** (~20-120ms):

- Resolve `example.com` → IP address `93.184.216.34`
- Cache: Browser → OS → Router → ISP DNS

**2. TCP Handshake** (~100-300ms):

- 3-way: SYN → SYN-ACK → ACK
- Thiết lập kết nối giữa client-server

**3. TLS Handshake** (~100-300ms - nếu HTTPS):

- Certificate verification, key exchange
- Encrypted connection setup

**4. HTTP Request/Response** (~50-500ms):

- Browser gửi GET request
- Server return HTML (+ headers: cache, encoding...)

**PHASE 2: PARSING (~50-200ms)**

**5. HTML Parsing → DOM Tree:**

- Tokenize HTML → parse tags → construct DOM tree
- **Blocking**: `<script>` without `async/defer`

**6. CSS Parsing → CSSOM Tree:**

- Parse CSS → compute styles → CSSOM tree
- **Render-blocking**: CSS blocks rendering

**7. JavaScript Execution:**

- Parser-blocking: `<script>` stops HTML parsing
- Execute JS → modify DOM/CSSOM
- `async` = execute when downloaded, `defer` = execute after DOM

**PHASE 3: RENDERING (~100-500ms)**

**8. Render Tree Construction:**

- DOM + CSSOM → **Render Tree** (chỉ visible elements)
- Skip `display:none`, `<head>`, `<script>`

**9. Layout (Reflow):**

- Tính toán **position & size** của mọi element
- Output: **Box Model** (width, height, x, y)

**10. Paint:**

- Tạo **paint records** (fill text, colors, images, borders...)
- Output: **Paint layers**

**11. Composite:**

- Kết hợp layers thành final image
- GPU-accelerated (CSS transforms, opacity)

**12. Display:**

- Browser hiển thị pixels trên màn hình

**⚠️ Lỗi Thường Gặp:**

- `<script>` ở `<head>` không `async/defer` → block HTML parsing
- CSS ở cuối `<body>` → **FOUC** (Flash of Unstyled Content)
- Large DOM (>1500 nodes) → chậm layout/paint
- Force sync layout (read `offsetHeight` → modify style → read again) → **layout thrashing**

**💡 Kiến Thức Senior:**

- **Critical Rendering Path optimization**:
  - Minimize **render-blocking resources** (inline critical CSS, defer non-critical)
  - **Preload** key resources: `<link rel="preload" href="font.woff2">`
  - **HTTP/2 Server Push** critical assets
- **Metrics**: FCP (First Contentful Paint), LCP (Largest), TTI (Time to Interactive)
- **`will-change: transform`**: Hint browser tạo composite layer trước (optimize animations)
- **Resource Hints**: `dns-prefetch`, `preconnect`, `prefetch`, `prerender`

**Trả lời:\*\***

Khi user nhập URL `https://example.com` và nhấn Enter, có **12 bước chính** xảy ra:

**🌐 PHASE 1: NETWORK (Mạng) - Lấy tài nguyên từ server**

1. **DNS Lookup (Tra cứu DNS)** - ~20-120ms

   - Browser kiểm tra DNS cache (browser → OS → router → ISP)
   - Nếu không có, query DNS server để resolve `example.com` → IP `93.184.216.34`
   - **Chú thích**: Giống tra số điện thoại trong danh bạ để biết địa chỉ nhà

2. **TCP Handshake (Bắt tay 3 bước)** - ~100-300ms

   - Client gửi `SYN` (synchronize) → Server
   - Server gửi `SYN-ACK` (acknowledge) → Client
   - Client gửi `ACK` → Server
   - **Kết nối TCP được thiết lập**
   - **Chú thích**: Giống 2 người gọi điện xác nhận nghe thấy nhau trước khi nói chuyện

3. **TLS Handshake (Nếu HTTPS)** - ~100-300ms

   - Client gửi `ClientHello` (supported cipher suites)
   - Server gửi `ServerHello` + Certificate (SSL cert)
   - Client verify certificate với CA (Certificate Authority)
   - Trao đổi keys và thiết lập encrypted connection
   - **Chú thích**: Giống kiểm tra CMND trước khi chia sẻ thông tin mật

4. **HTTP Request** - ~50-200ms

   ```http
   GET / HTTP/1.1
   Host: example.com
   User-Agent: Chrome/120.0
   Accept: text/html
   Accept-Encoding: gzip, deflate, br
   Cookie: session=abc123
   ```

   - Browser gửi request lên server
   - **Chú thích**: Giống bạn yêu cầu món ăn ở nhà hàng

5. **Server Processing** - ~100-1000ms

   - Server nhận request
   - Xử lý logic (query database, run business logic)
   - Generate HTML response
   - **Chú thích**: Bếp nấu món ăn bạn yêu cầu

6. **HTTP Response** - ~50-500ms

   ```http
   HTTP/1.1 200 OK
   Content-Type: text/html; charset=utf-8
   Content-Encoding: gzip
   Content-Length: 1234
   Cache-Control: max-age=3600

   <!DOCTYPE html>
   <html>...</html>
   ```

   - Server gửi HTML về browser
   - **Chú thích**: Món ăn được mang ra bàn

**🎨 PHASE 2: PARSING (Phân tích) - Browser xử lý HTML/CSS/JS**

7. **HTML Parsing → DOM Tree** - ~100-500ms

   ```
   HTML: <div><p>Hello</p></div>

   DOM Tree:
   Document
   └── html
       └── body
           └── div
               └── p
                   └── "Hello"
   ```

   - Browser parse HTML từ trên xuống (top-to-bottom)
   - Tạo **DOM (Document Object Model)** tree
   - **⚠️ Blocking**: Khi gặp `<script>`, dừng parsing cho đến khi script execute xong
   - **Chú thích**: Đọc công thức nấu ăn và chuẩn bị nguyên liệu

8. **CSS Parsing → CSSOM Tree** - ~50-200ms

   ```
   CSS: div { color: red; }

   CSSOM Tree:
   StyleSheet
   └── div
       └── color: red
   ```

   - Parse `<link>` và `<style>` tags
   - Tạo **CSSOM (CSS Object Model)** tree
   - **⚠️ Render-blocking**: Phải đợi tất cả CSS load xong mới render
   - **Chú thích**: Chuẩn bị gia vị và cách trang trí món ăn

9. **JavaScript Execution** - ~100-2000ms
   ```javascript
   // Khi gặp <script src="app.js">
   // 1. Download app.js (nếu external)
   // 2. Parse & Compile JS
   // 3. Execute code (có thể modify DOM/CSSOM)
   ```
   - **⚠️ Parser-blocking**: `<script>` chặn HTML parsing
   - **✅ async/defer**: Không chặn parsing
     - `async`: Download parallel, execute ngay khi xong (không đảm bảo thứ tự)
     - `defer`: Download parallel, execute sau khi HTML parse xong (đảm bảo thứ tự)
   - **Chú thích**: Thêm hành động đặc biệt vào món ăn (vd: flambe)

**🖼️ PHASE 3: RENDERING (Vẽ lên màn hình) - Critical Rendering Path**

10. **Render Tree Construction** - ~50-200ms

    ```
    DOM + CSSOM → Render Tree

    Render Tree chỉ chứa:
    - Visible elements (không có display: none)
    - Với computed styles (font, color, position...)
    ```

    - Kết hợp DOM + CSSOM
    - Loại bỏ invisible nodes (`display: none`, `<head>`, `<script>`)
    - **Chú thích**: Sắp xếp món ăn lên đĩa theo cách đẹp mắt

11. **Layout (Reflow)** - ~50-500ms

    ```
    Tính toán:
    - Vị trí (x, y) của mỗi element
    - Kích thước (width, height)
    - Box model (margin, padding, border)
    ```

    - Browser tính toán **geometry** (hình học) của mỗi element
    - **⚠️ Expensive**: Thay đổi layout triggers reflow toàn bộ tree
    - **Chú thích**: Đo kích thước và vị trí từng thành phần trên đĩa

12. **Paint & Composite** - ~50-200ms
    - **Paint**: Chuyển elements thành pixels (fill colors, draw text, images...)
    - **Composite**: Kết hợp các layers thành final image
    - GPU acceleration cho `transform`, `opacity`
    - **Chú thích**: Vẽ món ăn lên giấy và ghép các lớp lại thành hình hoàn chỉnh

**🎯 Total Time: ~800ms - 5000ms** (phụ thuộc network, server, complexity)

**Hoạt động:**

**📊 Timeline minh họa:**

```
Time →  0ms          200ms        400ms        600ms        800ms       1000ms
        │             │            │            │            │            │
DNS     ████
TCP         █████
TLS              ████
Request               ██
Server                  ████████████
Response                            ████
HTML Parse                              ████████
CSS Parse                                   ████
JS Exec                                         ██████
Layout                                                 ███
Paint                                                     ██
        │             │            │            │            │            │
        └─ NETWORK ──┴── PARSING ──┴─────────── RENDERING ─────────────┘
```

**🔥 Critical Rendering Path (Con đường render quan trọng):**

```
HTML → DOM Tree ─┐
                  ├─→ Render Tree → Layout → Paint → Composite → Display
CSS → CSSOM Tree ─┘
        ↑
        │
    JS có thể modify DOM/CSSOM (triggering reflow/repaint)
```

---

**Ưu điểm:**

1. **Efficient Pipeline**: Browser optimize mỗi bước để render nhanh nhất
2. **Progressive Rendering**: Browser render từng phần khi có data (không đợi full page load)
3. **Caching**: DNS, TCP connections, assets được cache để lần sau nhanh hơn
4. **Parallel Processing**: Browser download multiple resources đồng thời (HTTP/2, HTTP/3)
5. **GPU Acceleration**: Dùng GPU cho animations (`transform`, `opacity`) thay vì CPU

---

**Nhược điểm:**

1. **Render-blocking CSS**: Phải load hết CSS mới render → tăng FCP (First Contentful Paint)
2. **Parser-blocking JS**: `<script>` chặn HTML parsing → delay DOM construction
3. **Network Latency**: Mỗi RTT (Round-Trip Time) thêm ~100-300ms delay
4. **Reflow/Repaint Expensive**: Thay đổi layout trigger reflow toàn bộ page
5. **Third-party Scripts**: Ads, analytics làm chậm page load

---

**Chú thích:**

**🎯 Các metrics quan trọng (Web Vitals):**

- **FCP (First Contentful Paint)**: Thời gian browser render first content (~1-2s)

  - 💡 **Định nghĩa**: Thời điểm browser render bất kỳ nội dung nào lên màn hình
  - 💡 **Bao gồm**: Text, image, canvas, SVG (không tính background)
  - 💡 **Target**: < 1.8s (Google recommendation)
  - 💡 **Ý nghĩa**: User cảm nhận page load nhanh hay chậm
  - 💡 **Cách optimize**: Inline critical CSS, minimize render-blocking resources

- **LCP (Largest Contentful Paint)**: Thời gian render largest content (~2-3s)

  - 💡 **Định nghĩa**: Thời điểm element lớn nhất trong viewport được render
  - 💡 **Elements**: `<img>`, `<video>`, background images, block-level text
  - 💡 **Target**: < 2.5s (Google recommendation) - **QUAN TRỌNG NHẤT!**
  - 💡 **Ý nghĩa**: User cảm nhận main content load nhanh hay chậm
  - 💡 **Cách optimize**: Optimize images, preload LCP element, reduce server response time

- **TTI (Time to Interactive)**: Thời gian page có thể tương tác (~3-5s)

  - 💡 **Định nghĩa**: Thời điểm page đã load xong và có thể tương tác (click, scroll, type)
  - 💡 **Điều kiện**:
    - FCP đã xảy ra
    - Tất cả critical resources đã load
    - Main thread idle (không có long tasks > 50ms)
  - 💡 **Target**: < 3.8s (Google recommendation)
  - 💡 **Ý nghĩa**: User có thể tương tác với page
  - 💡 **Cách optimize**: Code splitting, minimize JavaScript, defer non-critical scripts

- **CLS (Cumulative Layout Shift)**: Đo lường layout shift (< 0.1 là tốt)

  - 💡 **Định nghĩa**: Tổng điểm layout shift trong suốt page lifetime
  - 💡 **Layout Shift**: Element bị dịch chuyển khi load (VD: Image load sau → push content xuống)
  - 💡 **Công thức**: CLS = Σ (impact fraction × distance fraction)
  - 💡 **Target**: < 0.1 (Google recommendation)
  - 💡 **Ý nghĩa**: Page ổn định, không bị "nhảy" khi load
  - 💡 **Cách optimize**: Set size cho images/videos, reserve space cho ads, avoid inserting content above existing content

- **FID (First Input Delay)**: Delay từ khi user click đến khi browser respond (< 100ms)
  - 💡 **Định nghĩa**: Thời gian từ khi user tương tác (click, tap, keypress) đến khi browser bắt đầu xử lý
  - 💡 **Nguyên nhân**: Main thread đang busy (parse JS, execute code, render)
  - 💡 **Target**: < 100ms (Google recommendation)
  - 💡 **Ý nghĩa**: Page responsive, user cảm thấy mượt mà
  - 💡 **Cách optimize**: Minimize JavaScript, code splitting, use Web Workers, optimize third-party scripts

**⚡ Optimization techniques:**

1. **DNS Prefetch**: `<link rel="dns-prefetch" href="//api.example.com">`

   - 💡 **DNS Prefetch**: Resolve DNS trước khi cần
   - 💡 **Cách hoạt động**:
     - Browser resolve DNS cho domain (api.example.com → IP)
     - Lưu vào cache
     - Khi cần gọi API → không cần DNS lookup nữa
     - → Tiết kiệm 20-120ms mỗi request!
   - 💡 **Dùng khi**: Có external domains (API, CDN, fonts)
   - 💡 **Ví dụ**: API calls, third-party services

2. **Preconnect**: `<link rel="preconnect" href="//cdn.example.com">`

   - 💡 **Preconnect**: DNS + TCP + TLS handshake trước
   - 💡 **Cách hoạt động**:
     - Resolve DNS
     - Thiết lập TCP connection
     - Thiết lập TLS (nếu HTTPS)
     - Khi cần request → chỉ cần gửi HTTP request
     - → Tiết kiệm 200-600ms!
   - 💡 **Dùng khi**: Chắc chắn sẽ dùng domain đó (CDN, API)
   - 💡 **Khác với DNS Prefetch**: Preconnect làm nhiều hơn (TCP + TLS)

3. **Resource Hints**: `<link rel="preload" as="script" href="critical.js">`

   - 💡 **Preload**: Download resource với high priority
   - 💡 **Cách hoạt động**:
     - Browser download resource ngay (high priority)
     - Lưu vào cache
     - Khi cần dùng → lấy từ cache
     - → Giảm delay khi cần resource
   - 💡 **as="script"**: Chỉ định loại resource (script, style, font, image...)
   - 💡 **Dùng khi**: Resource quan trọng nhưng không block render
   - 💡 **Ví dụ**: Critical fonts, hero images, critical scripts

4. **Critical CSS**: Inline critical CSS, defer non-critical

   - 💡 **Critical CSS** = CSS cho phần user thấy ngay (above-the-fold)
   - 💡 **Strategy**:
     - Inline critical CSS trong `<head>` (không cần HTTP request)
     - Defer non-critical CSS (load sau, không block render)
     - → FCP nhanh hơn 200-500ms!
   - 💡 **Cách làm**:
     1. Extract CSS cho phần đầu trang (header, hero, navigation)
     2. Inline vào `<head>`
     3. Load CSS đầy đủ sau (defer)
   - 💡 **Tools**: critical, purgecss, uncss

5. **Async/Defer JS**: `<script async src="analytics.js">`

   - 💡 **Async**: Download parallel, execute ngay khi xong (không đảm bảo thứ tự)
   - 💡 **Defer**: Download parallel, execute sau DOM ready (đảm bảo thứ tự)
   - 💡 **Cách hoạt động**:
     - `async`: Không block HTML parsing, execute ngay khi download xong
     - `defer`: Không block HTML parsing, execute sau DOM ready
     - → HTML parsing không bị block!
   - 💡 **Dùng async**: Third-party scripts (analytics, ads)
   - 💡 **Dùng defer**: Scripts cần DOM (app.js, jquery.js)

6. **Code Splitting**: Load only needed code first

   - 💡 **Code Splitting**: Chia code thành nhiều chunks, load khi cần
   - 💡 **Cách hoạt động**:
     - Initial bundle: Chỉ code cần thiết cho first render
     - Lazy load: Load code khác khi cần (dynamic import)
     - → Initial bundle nhỏ hơn → FCP nhanh hơn!
   - 💡 **Ví dụ**:
     - Initial: 100KB (header, sidebar, skeleton)
     - Lazy load chart.js: 200KB (khi user vào tab Chart)
     - Lazy load tradingview: 500KB (khi user click tab Trading)
   - 💡 **Tools**: Webpack, Vite, Rollup (tự động code splitting)

7. **Image Optimization**: WebP, lazy loading, responsive images

   - 💡 **Image Optimization**: Giảm size + load thông minh
   - 💡 **Techniques**:
     - WebP format: Nhỏ hơn JPEG 25-35%, nhỏ hơn PNG 26%
     - Lazy loading: Chỉ load khi image sắp vào viewport
     - Responsive images: Browser chọn size phù hợp (srcset, sizes)
     - Compression: Optimize quality/size balance
     - → Tiết kiệm bandwidth + tăng tốc độ load!
   - 💡 **Ví dụ**: `<img src="hero.webp" loading="lazy" srcset="small.webp 400w, large.webp 1200w">`
   - 💡 **Tools**: imagemin, sharp, squoosh

8. **CDN**: Serve static assets from edge locations closer to users

   - 💡 **CDN (Content Delivery Network)**: Phân phối assets từ servers gần user
   - 💡 **Cách hoạt động**:
     - Assets (JS, CSS, images) được cache ở edge servers
     - User request → Lấy từ edge server gần nhất (thay vì origin server)
     - → Giảm latency (từ 200ms → 20ms)!
   - 💡 **Lợi ích**:
     - Latency thấp hơn (edge server gần user hơn)
     - Giảm load cho origin server
     - Better performance cho users ở xa
   - 💡 **Providers**: Cloudflare, AWS CloudFront, Fastly, Vercel

9. **HTTP/2 or HTTP/3**: Multiplexing, server push

   - 💡 **HTTP/2**: Nhiều cải tiến so với HTTP/1.1
   - 💡 **Features**:
     - Multiplexing: Nhiều requests trên 1 connection (không cần queue)
     - Server Push: Server gửi resources trước khi browser request
     - Header compression: Giảm overhead
     - → Nhanh hơn HTTP/1.1 20-50%!
   - 💡 **HTTP/3**: Dùng QUIC protocol (UDP-based)
   - 💡 **Features**:
     - Faster connection setup (0-RTT)
     - Better handling packet loss
     - Multiplexing không bị head-of-line blocking
     - → Nhanh hơn HTTP/2 thêm 10-20%!
   - 💡 **Lưu ý**: Cần server support (Nginx, Apache, Cloudflare)

10. **Service Worker**: Cache assets for offline/fast subsequent loads
    - 💡 **Service Worker**: JavaScript worker chạy ở background
    - 💡 **Cách hoạt động**:
      - Intercept network requests
      - Cache responses (strategies: cache-first, network-first, stale-while-revalidate)
      - Serve từ cache khi offline hoặc khi cần tốc độ
      - → Subsequent loads nhanh hơn (từ cache)!
    - 💡 **Use cases**:
      - Cache static assets (JS, CSS, images)
      - Cache API responses (với TTL)
      - Offline support (PWA)
      - Background sync
    - 💡 **Strategies**:
      - Cache-First: Lấy từ cache, nếu không có → network
      - Network-First: Lấy từ network, nếu fail → cache
      - Stale-While-Revalidate: Lấy từ cache ngay, update cache ở background
    - 💡 **Example**: `navigator.serviceWorker.register('/sw.js')` → Cache assets → Subsequent loads từ cache (0ms network time)!

---

**Code Example:**

**🔍 Ví dụ 1: Waterfall Network Requests (Sequential loading - SLOW)**

```html
<!DOCTYPE html>
<html>
  <head>
    <!-- ❌ BAD: Blocking CSS -->
    <!-- 💡 Render-blocking: Browser PHẢI đợi CSS load xong mới render -->
    <!-- 💡 Cách hoạt động:
         1. Browser gặp <link rel="stylesheet">
         2. Download styles.css (200ms)
         3. Parse CSS → CSSOM
         4. CHỈ SAU ĐÓ mới render HTML
         → User thấy màn hình trắng trong 200ms! -->
    <link rel="stylesheet" href="styles.css" />
    <!-- ⏱️ Wait 200ms - Browser đợi CSS load xong -->

    <!-- ❌ BAD: Parser-blocking script -->
    <!-- 💡 Parser-blocking: <script> CHẶN HTML parsing -->
    <!-- 💡 Cách hoạt động:
         1. Browser đang parse HTML
         2. Gặp <script src="jquery.js">
         3. DỪNG parsing HTML ngay lập tức
         4. Download jquery.js (300ms)
         5. Execute JavaScript
         6. CHỈ SAU ĐÓ mới tiếp tục parse HTML
         → DOM construction bị delay 300ms! -->
    <script src="jquery.js"></script>
    <!-- ⏱️ Wait 300ms, blocks HTML parsing -->
    <!-- 💡 HTML parsing bị dừng → Không thể build DOM tree -->

    <script src="app.js"></script>
    <!-- ⏱️ Wait 200ms, blocks HTML parsing -->
    <!-- 💡 Tiếp tục block parsing thêm 200ms -->
  </head>
  <body>
    <h1>Hello World</h1>
    <!-- 💡 Element này chỉ render SAU KHI CSS + JS load xong! -->

    <!-- ❌ BAD: Synchronous image loading -->
    <!-- 💡 Image loading block rendering (nếu không có lazy loading) -->
    <!-- 💡 Browser đợi image download xong mới render -->
    <img src="hero.jpg" width="1200" height="600" />
    <!-- ⏱️ Wait 500ms - Download 5MB image -->
    <!-- 💡 Image lớn → tốn bandwidth → chậm -->
  </body>
</html>

<!--
📊 TỔNG KẾT:
Total blocking time: 200 + 300 + 200 = 700ms
💡 Giải thích:
   - CSS blocking: 200ms (phải đợi CSS mới render)
   - JS blocking: 300ms + 200ms = 500ms (chặn HTML parsing)
   - Tổng: 700ms blocking time

FCP: ~900ms (after styles.css + scripts loaded)
💡 First Contentful Paint = Thời điểm user thấy nội dung đầu tiên
💡 900ms = 700ms blocking + 200ms render

❌ User sees blank white screen for ~900ms
💡 Trải nghiệm xấu: User nhìn màn hình trắng gần 1 giây!
💡 Có thể mất user nếu họ nghĩ site bị lỗi
-->
```

**✅ Ví dụ 2: Optimized Loading (Parallel + Progressive - FAST)**

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <!-- ✅ GOOD: DNS prefetch for external domains -->
    <!-- 💡 DNS Prefetch: Resolve DNS trước khi cần -->
    <!-- 💡 Cách hoạt động:
         1. Browser resolve DNS cho api.example.com ngay
         2. Lưu vào cache
         3. Khi cần gọi API → không cần DNS lookup nữa
         → Tiết kiệm 20-120ms mỗi request! -->
    <link rel="dns-prefetch" href="//api.example.com" />
    <!-- 💡 Prefetch DNS cho API domain -->

    <!-- 💡 Preconnect: DNS + TCP + TLS handshake trước -->
    <!-- 💡 Cách hoạt động:
         1. Resolve DNS
         2. Thiết lập TCP connection
         3. Thiết lập TLS (nếu HTTPS)
         4. Khi cần request → chỉ cần gửi HTTP request
         → Tiết kiệm 200-600ms! -->
    <link rel="preconnect" href="//cdn.example.com" crossorigin />
    <!-- 💡 Preconnect đến CDN (DNS + TCP + TLS) -->

    <!-- ✅ GOOD: Inline critical CSS (above-the-fold styles) -->
    <!-- 💡 Critical CSS = CSS cho phần nội dung user thấy ngay (không cần scroll) -->
    <!-- 💡 Cách hoạt động:
         1. CSS được inline trong HTML → không cần HTTP request
         2. Browser parse CSS ngay lập tức (0ms delay)
         3. Render ngay được phần đầu trang
         4. Non-critical CSS load sau (không block render)
         → FCP nhanh hơn 200-500ms! -->
    <style>
      /* Critical CSS: chỉ styles cho nội dung đầu trang */
      /* 💡 Above-the-fold = Phần user thấy ngay khi vào trang (không cần scroll) */
      /* 💡 VD: Header, hero section, navigation */
      body {
        margin: 0;
        font-family: sans-serif;
        /* 💡 Styles cơ bản cho body - cần ngay */
      }
      .hero {
        height: 100vh;
        background: #f0f0f0;
        /* 💡 Hero section styles - user thấy ngay */
      }
      h1 {
        font-size: 3rem;
        /* 💡 Heading styles - hiển thị ngay */
      }
    </style>
    <!-- 💡 Inline CSS = Không block render, parse ngay lập tức -->

    <!-- ✅ GOOD: Preload critical resources -->
    <!-- 💡 Preload: Browser download resource với priority cao -->
    <!-- 💡 Cách hoạt động:
         1. Browser download font/image ngay (high priority)
         2. Lưu vào cache
         3. Khi cần dùng → lấy từ cache (không cần download lại)
         → Giảm delay khi render -->
    <link rel="preload" as="font" href="/fonts/main.woff2" crossorigin />
    <!-- 💡 Preload font: Download font trước khi cần -->
    <!-- 💡 crossorigin: Cần cho CORS khi load từ CDN -->
    <!-- 💡 Lợi ích: Font sẵn sàng khi cần → không bị FOIT (Flash of Invisible Text) -->

    <link rel="preload" as="image" href="/hero.webp" />
    <!-- 💡 Preload image: Download hero image với priority cao -->
    <!-- 💡 Lợi ích: Image sẵn sàng khi render → không bị layout shift -->

    <!-- ✅ GOOD: Defer non-critical CSS -->
    <!-- 💡 Defer CSS: Load CSS nhưng KHÔNG block render -->
    <!-- 💡 Cách hoạt động:
         1. rel="preload" as="style": Download CSS với low priority
         2. onload: Khi download xong → chuyển thành stylesheet
         3. Browser render ngay với critical CSS (inline)
         4. Non-critical CSS apply sau (không block)
         → User thấy content ngay, CSS apply sau! -->
    <link
      rel="preload"
      as="style"
      href="styles.css"
      onload="this.onload=null;this.rel='stylesheet'"
    />
    <!-- 💡 rel="preload": Download nhưng không apply ngay -->
    <!-- 💡 onload: Khi download xong → chuyển thành stylesheet -->
    <!-- 💡 this.onload=null: Tránh chạy lại onload handler -->

    <noscript><link rel="stylesheet" href="styles.css" /></noscript>
    <!-- 💡 Fallback: Nếu JS bị tắt → load CSS bình thường -->
    <!-- 💡 Đảm bảo site vẫn hoạt động khi JS disabled -->
  </head>
  <body>
    <div class="hero">
      <h1>Hello World</h1>

      <!-- ✅ GOOD: Responsive images with lazy loading -->
      <!-- 💡 Responsive images: Browser chọn image phù hợp với screen size -->
      <!-- 💡 Lazy loading: Chỉ load image khi sắp vào viewport -->
      <!-- 💡 Cách hoạt động:
         1. srcset: Cung cấp nhiều kích thước image
         2. sizes: Browser tính toán kích thước cần
         3. Browser tự động chọn image phù hợp
         4. loading="lazy": Chỉ load khi image sắp visible
         5. decoding="async": Decode image ở background (không block rendering)
         → Tiết kiệm bandwidth + tăng tốc độ load! -->
      <img src="hero-small.webp"
      <!-- 💡 Fallback: Image mặc định cho browser cũ -->
      srcset=" hero-small.webp 400w,
      <!-- 💡 Image nhỏ (400px) cho mobile -->
      hero-medium.webp 800w,
      <!-- 💡 Image vừa (800px) cho tablet -->
      hero-large.webp 1200w
      <!-- 💡 Image lớn (1200px) cho desktop -->
      " sizes="100vw"
      <!-- 💡 sizes: Image chiếm 100% viewport width -->
      <!-- 💡 Browser dùng thông tin này để chọn image phù hợp -->
      loading="lazy"
      <!-- 💡 Lazy loading: Chỉ load khi image sắp vào viewport -->
      <!-- 💡 Lợi ích: Không block initial render, tiết kiệm bandwidth -->
      decoding="async"
      <!-- 💡 Async decoding: Decode image ở background thread -->
      <!-- 💡 Lợi ích: Không block main thread → render mượt hơn -->
      alt="Hero image"
      <!-- 💡 Alt text: Accessibility + SEO -->
      />
    </div>

    <!-- ✅ GOOD: Defer non-critical scripts -->
    <!-- 💡 Defer: Download parallel, execute SAU KHI HTML parse xong -->
    <!-- 💡 Cách hoạt động:
         1. Browser download script parallel (không block HTML parsing)
         2. Tiếp tục parse HTML → build DOM tree
         3. Khi HTML parse xong → execute scripts theo thứ tự
         4. Đảm bảo thứ tự: jquery.js → app.js (vì app.js depend vào jquery)
         → HTML parsing không bị block! -->
    <script src="jquery.js" defer></script>
    <!-- 💡 defer: Download parallel, execute sau DOM ready -->
    <!-- 💡 Thứ tự: jquery.js execute trước app.js -->

    <script src="app.js" defer></script>
    <!-- 💡 defer: Download parallel, execute sau DOM ready -->
    <!-- 💡 Thứ tự: app.js execute sau jquery.js (đảm bảo dependency) -->

    <!-- ✅ GOOD: Async third-party scripts -->
    <!-- 💡 Async: Download parallel, execute NGAY KHI download xong -->
    <!-- 💡 Cách hoạt động:
         1. Browser download script parallel (không block HTML parsing)
         2. Khi download xong → execute ngay (không đợi HTML parse)
         3. KHÔNG đảm bảo thứ tự (script nào download xong trước execute trước)
         → Phù hợp cho third-party scripts (analytics, ads) -->
    <script async src="https://analytics.com/script.js"></script>
    <!-- 💡 async: Download parallel, execute ngay khi xong -->
    <!-- 💡 Phù hợp: Analytics, ads (không depend vào DOM) -->
    <!-- 💡 Lợi ích: Không block rendering, không cần đợi -->
  </body>
</html>

<!--
📊 TỔNG KẾT OPTIMIZATIONS:

Critical CSS inline: 0ms blocking
💡 CSS inline trong HTML → không cần HTTP request
💡 Browser parse ngay → render ngay được
💡 Tiết kiệm: 200ms (thay vì đợi download CSS)

Images lazy load: không block render
💡 loading="lazy" → chỉ load khi image sắp visible
💡 decoding="async" → decode ở background
💡 Tiết kiệm: 500ms initial load (không load image ngay)

Scripts defer: download parallel, execute after DOM ready
💡 Download parallel → không block HTML parsing
💡 Execute sau DOM ready → đảm bảo DOM đã sẵn sàng
💡 Tiết kiệm: 500ms blocking time (thay vì block parsing)

✅ FCP: ~200-400ms (user sees content immediately!)
💡 First Contentful Paint = Thời điểm user thấy nội dung đầu tiên
💡 So với cách cũ (900ms) → Nhanh hơn 2-4 lần!
💡 User experience: Thấy content ngay, không phải đợi màn hình trắng
-->
```

**🔍 Ví dụ 3: Measuring Performance với Performance API**

```typescript
// Đo các Web Vitals metrics
interface PerformanceMetrics {
  dns: number;
  tcp: number;
  request: number;
  response: number;
  domParse: number;
  domReady: number;
  load: number;
  fcp: number;
  lcp: number;
}

function measurePerformance(): PerformanceMetrics {
  // 💡 Performance API: Browser cung cấp timing data cho page load
  // 💡 performance.timing: Chứa timestamps của các sự kiện quan trọng
  const perfData = performance.timing;
  //    💡 performance.timing = Object chứa các timestamp (milliseconds)
  //    💡 VD: navigationStart, domainLookupStart, domContentLoadedEventEnd...

  const navigation = performance.getEntriesByType(
    'navigation'
  )[0] as PerformanceNavigationTiming;
  //    💡 getEntriesByType('navigation'): Lấy navigation timing entry
  //    💡 NavigationTiming: Thông tin chi tiết về page navigation
  //    💡 Bao gồm: fetchStart, responseStart, domContentLoadedEventStart...

  return {
    // Network metrics - Đo lường thời gian network
    dns: perfData.domainLookupEnd - perfData.domainLookupStart,
    // 💡 DNS Lookup time: Thời gian resolve domain → IP
    // 💡 domainLookupStart: Bắt đầu DNS lookup
    // 💡 domainLookupEnd: Kết thúc DNS lookup
    // 💡 VD: 45ms = Thời gian resolve "example.com" → "93.184.216.34"

    tcp: perfData.connectEnd - perfData.connectStart,
    // 💡 TCP Handshake time: Thời gian thiết lập TCP connection
    // 💡 connectStart: Bắt đầu TCP handshake
    // 💡 connectEnd: Kết thúc TCP handshake (bao gồm TLS nếu HTTPS)
    // 💡 VD: 123ms = Thời gian SYN → SYN-ACK → ACK

    request: perfData.responseStart - perfData.requestStart,
    // 💡 Request time: Thời gian từ khi gửi request đến khi nhận response đầu tiên
    // 💡 requestStart: Bắt đầu gửi HTTP request
    // 💡 responseStart: Nhận byte đầu tiên từ server
    // 💡 VD: 87ms = Thời gian server xử lý request

    response: perfData.responseEnd - perfData.responseStart,
    // 💡 Response time: Thời gian download response
    // 💡 responseStart: Nhận byte đầu tiên
    // 💡 responseEnd: Nhận byte cuối cùng
    // 💡 VD: 234ms = Thời gian download HTML (phụ thuộc size)

    // Parsing metrics - Đo lường thời gian parsing
    domParse: perfData.domInteractive - perfData.domLoading,
    // 💡 DOM Parse time: Thời gian parse HTML → DOM tree
    // 💡 domLoading: Bắt đầu parse HTML
    // 💡 domInteractive: DOM tree đã sẵn sàng (có thể tương tác)
    // 💡 VD: 456ms = Thời gian parse HTML và build DOM

    domReady: perfData.domContentLoadedEventEnd - perfData.navigationStart,
    // 💡 DOM Ready time: Từ khi bắt đầu navigation đến khi DOM ready
    // 💡 navigationStart: User nhấn Enter hoặc click link
    // 💡 domContentLoadedEventEnd: DOMContentLoaded event kết thúc
    // 💡 VD: 789ms = Tổng thời gian từ URL → DOM ready

    load: perfData.loadEventEnd - perfData.navigationStart,
    // 💡 Page Load time: Từ khi bắt đầu navigation đến khi page load hoàn toàn
    // 💡 loadEventEnd: window.onload event kết thúc (tất cả resources loaded)
    // 💡 VD: 1234ms = Tổng thời gian load page hoàn chỉnh

    // Web Vitals (approximate)
    fcp: navigation.responseStart - navigation.fetchStart,
    // 💡 FCP (First Contentful Paint): Thời gian render nội dung đầu tiên
    // 💡 fetchStart: Bắt đầu fetch resource
    // 💡 responseStart: Nhận response đầu tiên
    // 💡 Approximate: Thực tế FCP đo bằng PerformanceObserver chính xác hơn
    // 💡 VD: 567ms = Thời gian user thấy nội dung đầu tiên

    lcp: 0, // Cần dùng PerformanceObserver
    // 💡 LCP (Largest Contentful Paint): Thời gian render element lớn nhất
    // 💡 Phải dùng PerformanceObserver để đo chính xác
    // 💡 Xem code bên dưới để đo LCP
  };
}

// Observe LCP (Largest Contentful Paint)
// 💡 PerformanceObserver: API để observe performance events real-time
// 💡 LCP = Element lớn nhất được render (VD: hero image, heading lớn)
// 💡 Metric quan trọng: User cảm nhận page load nhanh hay chậm
const observer = new PerformanceObserver((list) => {
  // 💡 Callback được gọi mỗi khi có LCP event mới
  // 💡 LCP có thể thay đổi nhiều lần (VD: image load sau → trở thành LCP mới)
  const entries = list.getEntries();
  //    💡 entries: Array các LCP entries (mỗi entry = 1 element được render)
  //    💡 Entry cuối cùng = LCP hiện tại (element lớn nhất)

  const lastEntry = entries[entries.length - 1] as PerformanceEntry & {
    renderTime: number;
  };
  //    💡 Lấy entry cuối cùng (LCP mới nhất)
  //    💡 renderTime: Thời điểm element được render lên màn hình
  //    💡 startTime: Thời điểm bắt đầu load element

  console.log('LCP:', lastEntry.renderTime || lastEntry.startTime);
  // 💡 Log LCP time: renderTime (chính xác) hoặc startTime (fallback)
  // 💡 VD: 1200ms = Thời gian render element lớn nhất
  // 💡 Target: < 2.5s (Google recommendation)
});

observer.observe({ entryTypes: ['largest-contentful-paint'] });
// 💡 Observe LCP events: Browser sẽ gọi callback mỗi khi có LCP mới
// 💡 entryTypes: ['largest-contentful-paint'] = Chỉ observe LCP events

// Log metrics after page load
// 💡 Đợi page load hoàn toàn trước khi đo metrics
window.addEventListener('load', () => {
  // 💡 'load' event: Tất cả resources (images, scripts, styles) đã load xong
  // 💡 Đây là thời điểm tốt để đo performance metrics

  setTimeout(() => {
    // 💡 setTimeout(0): Đợi browser hoàn tất các tasks hiện tại
    // 💡 Đảm bảo metrics được tính chính xác
    const metrics = measurePerformance();
    //    💡 Gọi function đo performance → trả về object metrics
    console.table(metrics);
    //    💡 console.table: Hiển thị metrics dạng bảng (dễ đọc)

    /* Example output:
    ┌───────────┬────────┐
    │  Metric   │ Time   │
    ├───────────┼────────┤
    │ dns       │ 45ms   │   ← DNS lookup: Nhanh (có cache)
    │ tcp       │ 123ms  │   ← TCP handshake: Bình thường
    │ request   │ 87ms   │   ← Server processing: Nhanh
    │ response  │ 234ms  │   ← Download HTML: Bình thường
    │ domParse  │ 456ms  │   ← Parse HTML → DOM: Phụ thuộc HTML size
    │ domReady  │ 789ms  │   ← DOM ready: Tổng thời gian từ đầu
    │ load      │ 1234ms │   ← Page load hoàn chỉnh: Tất cả resources
    │ fcp       │ 567ms  │   ← First Contentful Paint: User thấy content
    └───────────┴────────┘
    💡 Phân tích:
       - DNS + TCP + Request + Response = 489ms (Network phase)
       - DOM Parse = 456ms (Parsing phase)
       - FCP = 567ms (Rendering phase bắt đầu)
       - Total Load = 1234ms (Page hoàn chỉnh)
    */
  }, 0);
});
```

**🔍 Ví dụ 4: Tối Ưu Critical Rendering Path trong Trading App**

```typescript
// ❌ BAD: Load tất cả chart libraries upfront
// 💡 Vấn đề: Load tất cả libraries ngay từ đầu → Bundle size lớn
// 💡 Impact: User phải đợi download 1000KB trước khi thấy UI
import { Chart } from 'chart.js'; // 200KB
// 💡 Chart.js: Library vẽ biểu đồ (200KB minified)
import { TradingView } from 'tradingview'; // 500KB
// 💡 TradingView: Library chart trading nặng (500KB)
import { DataGrid } from 'ag-grid'; // 300KB
// 💡 AG Grid: Data grid enterprise (300KB)
// 💡 Tổng: 1000KB = 1MB JavaScript!

class TradingApp {
  async init() {
    // Load all libs → 1000KB → 3-5s load time!
    // 💡 Vấn đề:
    //   1. Download 1000KB JavaScript (3-5 giây trên 3G)
    //   2. Parse & compile JavaScript (500ms-1s)
    //   3. Execute code (200-500ms)
    //   4. Tổng: 3-5 giây trước khi user thấy UI!
    // 💡 User experience: Màn hình trắng 3-5 giây → Rất xấu!
    this.chart = new Chart();
    // 💡 Khởi tạo Chart ngay (dù user chưa vào tab Chart)
    this.tradingView = new TradingView();
    // 💡 Khởi tạo TradingView ngay (dù user chưa cần)
    this.grid = new DataGrid();
    // 💡 Khởi tạo Grid ngay (dù user chưa scroll đến)
  }
}

// ✅ GOOD: Code splitting + Lazy loading
// 💡 Strategy: Chỉ load code cần thiết ngay, load code khác khi cần
// 💡 Lợi ích: Initial bundle nhỏ → FCP nhanh → User thấy UI ngay
class TradingAppOptimized {
  private chart?: any;
  // 💡 Optional: Chart chỉ được khởi tạo khi cần
  private tradingView?: any;
  // 💡 Optional: TradingView chỉ được khởi tạo khi user click tab
  private grid?: any;
  // 💡 Optional: Grid chỉ được khởi tạo khi cần

  async init() {
    // Load critical UI first (header, sidebar)
    // 💡 Critical UI = Phần user thấy ngay (header, sidebar, skeleton)
    // 💡 Load ngay → User thấy UI trong 200-400ms
    this.renderCriticalUI();

    // Lazy load chart when needed
    // 💡 Chart library (200KB) chỉ load khi user vào tab Chart
    // 💡 Không block initial render
    this.loadChartLazy();
  }

  renderCriticalUI() {
    // Inline critical CSS
    // 💡 Critical CSS = Styles cho header, sidebar (phần user thấy ngay)
    // 💡 Inline trong HTML → không cần HTTP request → render ngay
    document.head.insertAdjacentHTML(
      'beforeend',
      // 💡 insertAdjacentHTML: Thêm HTML vào DOM
      // 💡 'beforeend': Thêm vào cuối <head>
      `
      <style>
        .header { /* critical styles */ }
        /* 💡 Header styles: Cần ngay để render header */
        .sidebar { /* critical styles */ }
        /* 💡 Sidebar styles: Cần ngay để render sidebar */
      </style>
    `
    );

    // Render skeleton UI immediately
    // 💡 Skeleton UI = Placeholder UI (loading state)
    // 💡 User thấy ngay → Cảm giác page load nhanh
    document.body.innerHTML = `
      <div class="header">Trading Platform</div>
      <!-- 💡 Header: Render ngay, user thấy ngay -->
      <div class="sidebar">Menu...</div>
      <!-- 💡 Sidebar: Render ngay, user thấy ngay -->
      <div id="chart-container">
        <div class="skeleton-loader"></div>
        <!-- 💡 Skeleton loader: Placeholder cho chart (đang load) -->
        <!-- 💡 User thấy loading state → Biết chart đang load -->
      </div>
    `;
    // 💡 Tổng: Render UI trong < 100ms (thay vì đợi 3-5s!)
  }

  async loadChartLazy() {
    // Dynamic import: chỉ load khi cần
    // 💡 Dynamic import = Code splitting: Tách chart.js ra chunk riêng
    // 💡 Cách hoạt động:
    //   1. Browser download chart.js chunk (200KB) khi gọi import()
    //   2. Parse & compile JavaScript
    //   3. Execute code
    //   4. Khởi tạo Chart
    // 💡 Lợi ích: Initial bundle không chứa chart.js → nhỏ hơn 200KB
    const { Chart } = await import(
      /* webpackChunkName: "chart" */
      // 💡 webpackChunkName: Đặt tên chunk là "chart.js"
      // 💡 Output: chunks/chart.js (thay vì tên hash ngẫu nhiên)
      /* webpackPrefetch: true */
      // 💡 webpackPrefetch: Browser download chunk ở background (idle time)
      // 💡 Lợi ích: Khi user cần → chunk đã sẵn sàng (từ cache)
      'chart.js'
    );
    // 💡 await import(): Download + parse + execute chart.js
    // 💡 Thời gian: ~200-300ms (download 200KB)

    this.chart = new Chart();
    // 💡 Khởi tạo Chart sau khi library đã load
    this.renderChart();
    // 💡 Render chart lên UI
  }

  // Lazy load trading view chỉ khi user click tab
  // 💡 On-demand loading: Chỉ load khi user thực sự cần
  // 💡 TradingView rất nặng (500KB) → không nên load ngay
  async loadTradingView() {
    if (!this.tradingView) {
      // 💡 Check: Nếu chưa load → mới load
      // 💡 Tránh load nhiều lần (nếu user click tab nhiều lần)
      const { TradingView } = await import('tradingview');
      // 💡 Dynamic import: Download tradingview chunk (500KB)
      // 💡 Thời gian: ~500-800ms (download 500KB)
      this.tradingView = new TradingView();
      // 💡 Khởi tạo TradingView sau khi library đã load
    }
    return this.tradingView;
    // 💡 Return instance (đã load hoặc vừa load)
  }
}

// Resource hints để pre-load chunks
// 💡 Resource hints: Hướng dẫn browser download resources trước khi cần
// 💡 Lợi ích: Khi user cần → resource đã sẵn sàng (từ cache)
document.head.insertAdjacentHTML(
  'beforeend',
  `
  <link rel="prefetch" href="/chunks/chart.js">
  <!-- 💡 Prefetch: Download chunk ở background (low priority) -->
  <!-- 💡 Browser download khi idle (không block critical resources) -->
  <!-- 💡 Khi user vào tab Chart → chunk đã sẵn sàng → load ngay! -->

  <link rel="preload" as="script" href="/critical.js">
  <!-- 💡 Preload: Download với high priority -->
  <!-- 💡 Critical.js = Code cần thiết cho initial render -->
  <!-- 💡 Browser download ngay → sẵn sàng khi cần execute -->
`
);

/*
📊 KẾT QUẢ SO SÁNH:

❌ BAD (Load tất cả upfront):
  - Bundle size: 1000KB
  // 💡 Tất cả libraries trong 1 bundle → rất nặng
  - FCP: 3-5s
  // 💡 First Contentful Paint: User phải đợi 3-5 giây mới thấy UI
  // 💡 Lý do: Phải download + parse 1000KB trước
  - TTI: 5-7s
  // 💡 Time to Interactive: User phải đợi 5-7 giây mới tương tác được
  // 💡 Lý do: Phải execute tất cả JavaScript

✅ GOOD (Code splitting + Lazy loading):
  - Initial bundle: 100KB
  // 💡 Chỉ code cần thiết cho initial render
  // 💡 Giảm 90% bundle size (1000KB → 100KB)
  - FCP: 500ms-1s
  // 💡 First Contentful Paint: User thấy UI trong 0.5-1 giây
  // 💡 Nhanh hơn 3-5 lần so với cách cũ!
  - TTI: 1-2s
  // 💡 Time to Interactive: User tương tác được trong 1-2 giây
  // 💡 Nhanh hơn 3-4 lần so với cách cũ!
  - Load chart.js khi cần: +200ms
  // 💡 Khi user vào tab Chart → load thêm 200KB
  // 💡 Thời gian: +200ms (download) + 50ms (parse) = ~250ms
  // 💡 User experience: Thấy skeleton → Chart load → Smooth!
*/
```

---

**Best Practices:**

```typescript
// ✅ DO: Optimize Critical Rendering Path

// 1. Minimize Critical Resources
// - Inline critical CSS (above-the-fold)
// - Defer non-critical CSS
// - Async/defer non-critical JS

// 2. Reduce Number of Critical Bytes
// - Minify HTML/CSS/JS
// - Compress with Gzip/Brotli
// - Remove unused code (tree-shaking)

// 3. Optimize Critical Path Length
// - Reduce redirects
// - Use CDN
// - HTTP/2 multiplexing
// - Preconnect to required origins

// 4. Resource Hints
<link rel="dns-prefetch" href="//api.example.com">
<link rel="preconnect" href="//cdn.example.com">
<link rel="prefetch" href="/next-page.js">
<link rel="preload" as="script" href="/critical.js">

// 5. Code Splitting
const ChartComponent = lazy(() => import('./Chart'));

// 6. Image Optimization
<img
  src="image.webp"
  loading="lazy"
  decoding="async"
  srcset="small.webp 400w, large.webp 1200w"
>

// 7. Service Worker for Caching
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js');
}

// 8. Measure & Monitor
const observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    console.log('LCP:', entry.renderTime || entry.startTime);

    // Send to analytics
    sendToAnalytics({
      metric: 'lcp',
      value: entry.renderTime || entry.startTime,
      url: window.location.href
    });
  }
});

observer.observe({ entryTypes: ['largest-contentful-paint'] });
```

---

**Common Mistakes:**

```typescript
// ❌ MISTAKE 1: Render-blocking CSS
<link rel="stylesheet" href="styles.css">
// Browser phải download + parse CSS trước khi render bất cứ gì!

// ✅ FIX: Inline critical CSS, defer rest
<style>/* inline critical CSS */</style>
<link rel="preload" as="style" href="styles.css"
      onload="this.rel='stylesheet'">

// ❌ MISTAKE 2: Parser-blocking scripts
<script src="app.js"></script>
// Chặn HTML parsing!

// ✅ FIX: Defer scripts
<script src="app.js" defer></script>

// ❌ MISTAKE 3: Không optimize images
<img src="huge-image.jpg"> <!-- 5MB image! -->

// ✅ FIX: Responsive images + lazy loading
<img
  src="small.webp"
  srcset="small.webp 400w, large.webp 1200w"
  sizes="(max-width: 600px) 400px, 1200px"
  loading="lazy"
  decoding="async"
>

// ❌ MISTAKE 4: Quá nhiều synchronous requests
// 💡 Vấn đề: Gọi API tuần tự → Tổng thời gian = Tổng thời gian từng request
fetch('/api/user');
// 💡 Request 1: ~1s (download user data)
fetch('/api/orders');
// 💡 Request 2: ~1s (chờ request 1 xong mới bắt đầu)
fetch('/api/positions');
// 💡 Request 3: ~1s (chờ request 2 xong mới bắt đầu)
// Sequential → ~3s total
// 💡 Tổng: 1s + 1s + 1s = 3 giây
// 💡 Lãng phí: Browser có thể gọi parallel nhưng code không cho phép!

// ✅ FIX: Parallel requests
// 💡 Promise.all: Gọi tất cả requests đồng thời
Promise.all([
  fetch('/api/user'),
  // 💡 Request 1: Bắt đầu ngay
  fetch('/api/orders'),
  // 💡 Request 2: Bắt đầu ngay (không đợi request 1)
  fetch('/api/positions')
  // 💡 Request 3: Bắt đầu ngay (không đợi request 1, 2)
]);
// Parallel → ~1s total
// 💡 Tổng: max(1s, 1s, 1s) = 1 giây (thay vì 3 giây!)
// 💡 Browser gọi 3 requests đồng thời → Nhanh hơn 3 lần!
// 💡 Lợi ích: HTTP/2 multiplexing cho phép nhiều requests trên 1 connection

// ❌ MISTAKE 5: Layout thrashing
// 💡 Layout Thrashing = Đọc layout → Sửa style → Đọc layout → Sửa style...
// 💡 Vấn đề: Mỗi lần đọc/sửa trigger reflow → Rất chậm!
for (let i = 0; i < 100; i++) {
  const height = element.offsetHeight; // Read (trigger layout)
  // 💡 offsetHeight: Đọc chiều cao element → Browser phải tính layout
  // 💡 Browser trigger reflow để tính toán layout hiện tại
  // 💡 Reflow = Tính toán lại vị trí & kích thước TẤT CẢ elements

  element.style.height = height + 10 + 'px'; // Write (trigger reflow)
  // 💡 Sửa style → Browser invalidate layout
  // 💡 Browser phải reflow lại để tính toán layout mới
  // 💡 Reflow lại = Tính toán lại TẤT CẢ elements
}
// 100 reflows! Rất chậm!
// 💡 Mỗi iteration: 1 read (reflow) + 1 write (reflow) = 2 reflows
// 💡 Tổng: 100 × 2 = 200 reflows!
// 💡 Mỗi reflow tốn ~1-5ms → Tổng: 200-1000ms (RẤT CHẬM!)

// ✅ FIX: Batch reads/writes
// 💡 Strategy: Đọc TẤT CẢ trước, sau đó sửa TẤT CẢ
// 💡 Browser optimize: Batch reads → 1 reflow, batch writes → 1 reflow
const heights = [];
for (let i = 0; i < 100; i++) {
  heights.push(element.offsetHeight); // Read all
  // 💡 Phase 1: Đọc tất cả heights
  // 💡 Browser batch reads → chỉ 1 reflow duy nhất
  // 💡 Lợi ích: Browser tính layout 1 lần cho tất cả reads
}
for (let i = 0; i < 100; i++) {
  element.style.height = heights[i] + 10 + 'px'; // Write all
  // 💡 Phase 2: Sửa tất cả styles
  // 💡 Browser batch writes → chỉ 1 reflow duy nhất
  // 💡 Lợi ích: Browser tính layout 1 lần cho tất cả writes
}
// Chỉ 1 reflow!
// 💡 Tổng: 1 reflow (reads) + 1 reflow (writes) = 2 reflows
// 💡 So với cách cũ: 200 reflows → Giảm 100 lần!
// 💡 Thời gian: ~2-10ms (thay vì 200-1000ms) → Nhanh hơn 100 lần!

// ❌ MISTAKE 6: Không measure performance
// Làm sao biết optimize có hiệu quả?
// 💡 Vấn đề: Không đo lường → Không biết performance tốt hay xấu
// 💡 Không biết optimization có hiệu quả → Lãng phí thời gian optimize sai chỗ

// ✅ FIX: Monitor Web Vitals
// 💡 Web Vitals = Metrics quan trọng nhất cho user experience
// 💡 Google dùng để rank website (SEO)
// 💡 web-vitals library: Tool chính thức để đo Web Vitals
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals';

getCLS(console.log);
// 💡 CLS (Cumulative Layout Shift): Đo layout shift
// 💡 Layout shift = Element bị dịch chuyển khi load (VD: Image load sau → push content xuống)
// 💡 Target: < 0.1 (Google recommendation)
// 💡 VD: 0.05 = Layout shift nhỏ → Tốt!

getFID(console.log);
// 💡 FID (First Input Delay): Delay từ khi user click đến khi browser respond
// 💡 Đo lường responsiveness của page
// 💡 Target: < 100ms (Google recommendation)
// 💡 VD: 50ms = User click → Browser respond ngay → Tốt!

getFCP(console.log);
// 💡 FCP (First Contentful Paint): Thời gian render nội dung đầu tiên
// 💡 Đo lường perceived load speed
// 💡 Target: < 1.8s (Google recommendation)
// 💡 VD: 800ms = User thấy content nhanh → Tốt!

getLCP(console.log);
// 💡 LCP (Largest Contentful Paint): Thời gian render element lớn nhất
// 💡 Đo lường perceived load speed (quan trọng nhất!)
// 💡 Target: < 2.5s (Google recommendation)
// 💡 VD: 1.5s = User thấy main content nhanh → Tốt!

getTTFB(console.log);
// 💡 TTFB (Time to First Byte): Thời gian từ request đến byte đầu tiên
// 💡 Đo lường server response time
// 💡 Target: < 800ms (Google recommendation)
// 💡 VD: 300ms = Server respond nhanh → Tốt!
```

---

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
