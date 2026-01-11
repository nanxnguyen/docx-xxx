# 🖥️ Q42: Client-Side Rendering (CSR) vs Server-Side Rendering (SSR) - Phân Biệt & Cách Hoạt Động Chi Tiết

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"CSR = browser render (SPA - Single Page Application - Ứng dụng một trang), SSR = server render HTML (Server render HTML). CSR tốt cho interactive apps (ứng dụng tương tác), SSR tốt cho SEO/performance (hiệu suất). Modern: Hybrid (Kết hợp - SSR first paint + CSR hydration - Hydration là gắn events vào HTML)."**

**🔑 So Sánh Chi Tiết:**

| **Metric (Chỉ số)**            | **CSR**                                                           | **SSR**                                                    |
| ------------------------------ | ----------------------------------------------------------------- | ---------------------------------------------------------- |
| **Initial Load (Tải ban đầu)** | Chậm (download JS → execute - Tải JS → thực thi)                  | Nhanh (HTML ready - HTML sẵn sàng)                         |
| **SEO (Tối ưu SEO)**           | Kém (crawlers không chờ JS - Trình thu thập không chờ JavaScript) | Tốt (HTML đầy đủ - HTML có đầy đủ nội dung)                |
| **Navigation (Điều hướng)**    | Nhanh (no reload - Không tải lại trang)                           | Chậm (full page reload - Tải lại toàn bộ trang)            |
| **Server Load (Tải server)**   | Thấp (static CDN - CDN tĩnh)                                      | Cao (render mỗi request - Render cho mỗi yêu cầu)          |
| **Complexity (Độ phức tạp)**   | Đơn giản (frontend only - Chỉ frontend)                           | Phức tạp (isomorphic code - Code chạy cả server và client) |

**🔑 CSR (Client-Side Rendering):**

**Cách hoạt động:**

1. Server gửi empty HTML (HTML rỗng) + JS bundle (Gói JavaScript - 500KB-2MB)
2. Browser download (Tải xuống) → parse (Phân tích) → execute JS (Thực thi JavaScript)
3. React/Vue render UI (Vẽ giao diện) → attach events (Gắn sự kiện - hydration - Hydration là quá trình gắn JavaScript vào HTML đã render)

**Ưu điểm:**

- **Fast navigation (Điều hướng nhanh)** - no reload (Không tải lại trang), smooth SPA experience (Trải nghiệm SPA mượt mà - SPA = Single Page Application)
- **Rich interactions (Tương tác phong phú)** - full JS power (Sức mạnh JavaScript đầy đủ), real-time features (Tính năng thời gian thực)
- **Low server cost (Chi phí server thấp)** - CDN serving static files (CDN phục vụ file tĩnh - CDN = Content Delivery Network - Mạng phân phối nội dung)

**Nhược điểm:**

- **Slow First Paint (Vẽ lần đầu chậm)** - chờ download (Tải xuống) + execute JS (Thực thi JavaScript) (2-5s)
- **Poor SEO (SEO kém)** - crawlers (Trình thu thập dữ liệu như Google bot) không execute JS (Không thực thi JavaScript)
- **Large bundle (Gói lớn)** - 500KB+ initial load (Tải ban đầu - Initial load là lần tải đầu tiên)

**🔑 SSR (Server-Side Rendering):**

**Cách hoạt động:**

1. Server render React/Vue (Server render React/Vue thành) → HTML string (Chuỗi HTML)
2. Send full HTML (Gửi HTML đầy đủ - có content - có nội dung) về browser (Về trình duyệt)
3. Browser display ngay (Trình duyệt hiển thị ngay) → download JS (Tải JavaScript) → hydrate (Hydration - Gắn events để tương tác - interactivity)

**Ưu điểm:**

- **Fast First Paint (Vẽ lần đầu nhanh)** - HTML ready (HTML sẵn sàng), no JS blocking (Không bị chặn bởi JavaScript)
- **SEO-friendly (Thân thiện SEO)** - crawlers (Trình thu thập dữ liệu) thấy full content (Thấy đầy đủ nội dung)
- **Better performance (Hiệu suất tốt hơn)** on slow devices/networks (Trên thiết bị/mạng chậm)

**Nhược điểm:**

- **High server load (Tải server cao)** - render mỗi request (Render cho mỗi yêu cầu - Request là yêu cầu từ người dùng)
- **TTFB slower (TTFB chậm hơn)** - server processing time (Thời gian xử lý server - TTFB = Time To First Byte - Thời gian đến byte đầu tiên)
- **Complex setup (Thiết lập phức tạp)** - isomorphic code (Code isomorphic - Code chạy được cả server và client), hydration issues (Vấn đề hydration - Lỗi khi gắn events)

**⚠️ Lỗi Thường Gặp:**

- SSR dùng browser APIs (`window`, `localStorage`) → crash server
- Hydration mismatch (server HTML ≠ client HTML) → re-render flicker
- CSR không loading state → blank screen 3-5s
- SSR không cache → overload server

**💡 Kiến Thức Senior: (Kiến thức dành cho Senior Developer)**

- **Hybrid rendering (Render kết hợp)**: Next.js SSG (static - tĩnh) + ISR (revalidate - tái xác thực) + SSR (dynamic - động)
  // SSG = Static Site Generation (Tạo trang tĩnh)
  // ISR = Incremental Static Regeneration (Tái tạo tĩnh tăng dần)
  // SSR = Server-Side Rendering (Render phía server)
- **Streaming SSR (SSR luồng)**: Send HTML chunks progressively (Gửi HTML từng phần - React 18 Suspense)
  // Streaming = Gửi từng phần (Gửi dữ liệu từng phần thay vì chờ hết)
  // Suspense = Component React để xử lý async (Component React xử lý bất đồng bộ)
- **Partial Hydration (Hydration một phần)**: Chỉ hydrate interactive components (Chỉ hydrate component tương tác - Islands Architecture - Astro)
  // Islands Architecture = Kiến trúc đảo (Chỉ hydrate phần cần thiết)
  // Astro = Framework hỗ trợ Islands Architecture (Framework hỗ trợ kiến trúc đảo)
- **Edge SSR (SSR ở biên)**: Render on CDN edge (Render trên CDN edge - Vercel Edge, Cloudflare Workers) - faster TTFB (TTFB nhanh hơn)
  // Edge = Biên mạng (Gần user hơn - Giảm độ trễ)
  // CDN = Content Delivery Network (Mạng phân phối nội dung)
  // Vercel Edge = Edge functions của Vercel (Hàm edge của Vercel)
  // Cloudflare Workers = Workers của Cloudflare (Workers của Cloudflare)

**Trả lời:**

#### **🎯 Khái Niệm Cốt Lõi**

**CSR (Client-Side Rendering):**

- Server gửi **HTML rỗng** (chỉ có `<div id="root"></div>`) + **JavaScript bundle** (500KB-2MB)
- Browser **download JS → parse → execute → render** → hiển thị nội dung
- Giống như: Mua IKEA furniture (phải tự lắp ráp ở nhà)
- Rendering engine: Browser (Chrome V8, Firefox SpiderMonkey)

**SSR (Server-Side Rendering):**

- Server **render sẵn HTML đầy đủ** (có nội dung) rồi gửi về browser
- Browser **hiển thị ngay** HTML → sau đó download JS để tương tác
- Giống như: Mua furniture đã lắp ráp sẵn (chỉ cần đặt vào nhà)
- Rendering engine: Node.js server (React renderToString)

#### **✅ Ưu Điểm CSR (Client-Side Rendering)**

**1. Navigation Cực Nhanh (Fast SPA Navigation)**

```
User clicks link:
- CSR: 0ms (chỉ thay đổi DOM, không reload page)
- SSR: 500-1000ms (phải request server, đợi render)
→ Trải nghiệm mượt mà như native app
```

**2. Rich Interactions (Tương Tác Phong Phú)**

```typescript
// CSR: Dễ dàng làm real-time features
- Live chat, notifications
- Drag & drop, animations
- Real-time data updates
- Complex state management
→ Full JavaScript power trên browser
```

**3. Server Load Thấp (Less Server Load)**

```
- Server chỉ serve static files (HTML, JS, CSS)
- Không cần render cho mỗi request
- Dễ cache với CDN
- Cost thấp (chỉ cần CDN, không cần powerful server)
```

**4. Dễ Deploy & Scale**

```
- Deploy lên CDN (Vercel, Netlify, CloudFront)
- Không cần server-side logic
- Auto-scale với CDN
→ Chi phí thấp, dễ maintain
```

---

#### **❌ Nhược Điểm CSR**

**1. Initial Load Chậm (Slow First Load)**

```
Timeline:
[0s]   User clicks link
[0-1s] Download HTML (5KB) - ⚡ nhanh
[1-3s] Download JS bundle (500KB-2MB) - 🐌 CHẬM (tải file JS lớn)
[3-4s] Parse & Execute JS - 🐌 CHẬM (browser xử lý code)
[4-5s] Fetch API data - 🐌 CHẬM (gọi API lấy dữ liệu)
[5s]   User sees content - ❌ QUÁ LÂU!

→ 😱 User thấy blank screen trong 3-5 giây
→ 📉 Bounce rate cao (user rời trang)
```

**2. SEO Nghèo Nàn (Poor SEO)**

```html
<!-- Google bot sees: -->
<html>
  <body>
    <div id="root"></div>
    <!-- EMPTY! -->
    <script src="bundle.js"></script>
  </body>
</html>

→ Google không thấy nội dung → Không index được → SEO ranking thấp
```

**3. Blank Screen Problem**

```
User experience:
[0-3s] White/blank screen (nothing to see) - ⬜ Màn hình trắng (chưa có gì)
[3-5s] Loading spinner (still waiting...) - ⏳ Đang tải... (vẫn đợi)
[5s+] Content appears (finally!) - ✅ Cuối cùng cũng hiện!

→ 😤 User frustrated - User thất vọng
→ 🔴 Think website is broken - Nghĩ website bị lỗi
→ 🚪 Leave before content loads - Rời trang trước khi load xong
```

**4. Phụ Thuộc JavaScript**

```
- ❌ User disable JS → website không chạy
- 💥 JS error → website crash - Lỗi JS làm sập website
- 🐌 Slow device → website lag - Thiết bị yếu → chạy chậm
→ ⚠️ Không graceful degradation - Không có phương án dự phòng
```

---

#### **✅ Ưu Điểm SSR (Server-Side Rendering)**

**1. Initial Load Cực Nhanh (Fast Time to Content)**

```
Timeline:
[0s]   User clicks link
[0.5s] Server renders HTML - ⚡ nhanh (server có CPU mạnh)
[0.5s] Browser receives full HTML - 📦 HTML đầy đủ nội dung
[0.5s] User SEES content immediately! - ✅ Thấy nội dung ngay!
[1-2s] JS hydrates in background - 🔄 Gắn events (chạy ngầm)
[2s]   Fully interactive - 🎯 Hoàn toàn tương tác được

→ ⚡ User thấy nội dung trong 0.5-1 giây
→ 😊 First impression tốt
```

**2. SEO Xuất Sắc (SEO-Friendly)**

```html
<!-- Google bot sees: -->
<html>
  <body>
    <div id="root">
      <h1>Welcome to My Site</h1>
      <p>Full content here...</p>
      <article>Blog post content...</article>
      <!-- FULL CONTENT! -->
    </div>
  </body>
</html>

→ Google index đầy đủ nội dung → Better ranking → Social media previews work
(Open Graph)
```

**3. Better Performance (Đặc biệt cho slow devices)**

```
- 🚀 Server render nhanh (powerful CPU) - Server CPU mạnh render nhanh
- 📱 User device không cần làm việc nặng - Điện thoại không bị nặng
- 🆗 Suitable for low-end phones - Phù hợp với máy yếu
- 🔋 Ít JS → less battery drain - Ít JS → tiết kiệm pin
```

**4. Không Blank Screen**

```
User experience:
[0.5s] ✅ Content appears immediately! - Nội dung hiện ngay!
[1-2s] 🎯 Page becomes interactive - Trang có thể tương tác

→ 📈 Progressive enhancement - Cải thiện dần dần
→ ✅ Even if JS fails, HTML still works - JS lỗi vẫn thấy HTML
→ ⚡ Better perceived performance - User cảm thấy nhanh hơn
```

---

#### **❌ Nhược Điểm SSR**

**1. Server Load Cao (High Server Cost)**

```
CSR:
- 🖥️ Server: "Here's HTML + JS" (1 lần, cache được)
- 💰 Cost: $5/month (CDN) - Chỉ cần CDN phục vụ file tĩnh

SSR:
- 🖥️ Server: "Let me render this page..." (mỗi request phải render lại)
- ⚙️ Server: Parse React → Fetch data → Render HTML
- 💰 Cost: $50-500/month (cần server mạnh) - Phải xử lý nhiều

→ 💸 10-100x chi phí hơn CSR
```

**2. Navigation Chậm Hơn (Slower Navigation)**

```
User clicks internal link:

CSR:
- ⚡ Instant (0ms) - chỉ update DOM (không reload trang)
- ✨ Smooth transition - Chuyển trang mượt mà

SSR:
- 🌐 Request server (50-200ms network) - Gửi request tới server
- 🖥️ Server render (50-100ms) - Server render HTML
- 📥 Download HTML (50-200ms) - Tải HTML về
- ⏱️ Total: 500-1000ms - Tổng thời gian
→ ⚠️ Có thể thấy "flash" khi chuyển trang (trang nhấp nháy)
```

**3. Complexity Cao (Complex Setup)**

```typescript
// ✅ CSR: Simple (Đơn giản)
ReactDOM.render(<App />, root); // Chỉ 1 dòng code!

// ⚠️ SSR: Complex (Phức tạp)
- 🔧 Server setup (Express, Next.js) - Cần setup server
- 💧 Hydration issues (client-server mismatch) - Lỗi khi HTML server ≠ client
- 📊 Data fetching strategies - Nhiều cách fetch data
- 🗄️ Cache invalidation - Quản lý cache phức tạp
- 🔄 State management across server-client - Đồng bộ state
→ 🐛 Nhiều bugs tiềm ẩn, khó debug
```

**4. TTFB Cao Hơn (Time to First Byte)**

```
CSR:
- ⚡ TTFB: 50ms (serve static file) - Chỉ gửi file tĩnh

SSR:
- 🐌 TTFB: 200-500ms (render + fetch data) - Server phải xử lý
→ ⏳ User đợi lâu hơn trước khi thấy gì đó
→ 💡 (nhưng khi thấy thì đã có full content!)
```

**5. Hydration Issues**

```typescript
// 🖥️ Server renders: <div>Count: 0</div>
// 💻 Client state:   <div>Count: 1</div>
// → ⚠️ Mismatch! Warning! (HTML không khớp)

// 🐛 Common issues:
- ⏰ Date.now() khác nhau server vs client - Thời gian khác nhau
- 🎲 Random values - Giá trị random không giống
- 🌐 Browser-only APIs (window, localStorage) - API chỉ có trên browser
→ 💡 Requires careful coding (Cần code cẩn thận)
```

---

#### **📊 So Sánh Trực Quan**

```
┌─────────────────────────────────────────────────────────────────┐
│                    USER EXPERIENCE COMPARISON                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  CSR (Client-Side Rendering):                                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ 0s ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░  ← Blank screen          │  │
│  │ 1s ▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░  ← Downloading JS         │  │
│  │ 2s ▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░  ← Parsing JS             │  │
│  │ 3s ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░  ← Fetching data          │  │
│  │ 4s ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░  ← Rendering               │  │
│  │ 5s ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ✅ Content visible!      │  │
│  │                                                            │  │
│  │ First Content: 5 seconds                                  │  │
│  │ User sees: Blank → Loading → Content                     │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│  SSR (Server-Side Rendering):                                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ 0s ▓░░░░░░░░░░░░░░░░░░░░░░░░░░  ← Server rendering      │  │
│  │ 0.5s ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ✅ Content visible!      │  │
│  │ 1s ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ← Hydrating JS            │  │
│  │ 2s ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ✅ Interactive!           │  │
│  │                                                            │  │
│  │ First Content: 0.5 seconds                                │  │
│  │ Interactive: 2 seconds                                    │  │
│  │ User sees: Content immediately → Becomes interactive     │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

#### **🎯 Khi Nào Dùng Gì?**

**Dùng CSR khi:**

```
✅ Internal tools / Admin dashboard
   → Không cần SEO, user đã login
   → Example: Google Analytics, Jira, Notion

✅ Highly interactive apps
   → Real-time updates, complex interactions
   → Example: Figma, Trello, Games

✅ Budget thấp
   → Chỉ cần CDN, không cần server mạnh
   → Startup với limited resources
```

**Dùng SSR khi:**

```
✅ Public-facing websites
   → Cần SEO, social sharing
   → Example: Blog, News, E-commerce

✅ Landing pages / Marketing
   → First impression matters
   → Better conversion rate

✅ Content-heavy sites
   → Nhiều text, ít interaction
   → Example: Documentation, Wikipedia
```

**Dùng SSG (Hybrid) khi:**

```
✅ Static content with occasional updates
   → Blog posts, product pages
   → Example: Next.js with ISR

✅ Best of both worlds
   → Fast như CSR (served from CDN)
   → SEO-friendly như SSR
   → Cost-effective
```

---

#### **💡 Key Takeaways**

**CSR (Client-Side):**

- 🚀 Navigation nhanh, tương tác mượt
- 💰 Chi phí thấp, dễ deploy
- ❌ Initial load chậm (3-5s), SEO kém
- 🎯 **Dùng cho**: Internal tools, SPAs, interactive apps

**SSR (Server-Side):**

- ⚡ Initial load nhanh (0.5-1s), SEO tốt
- ✅ Không blank screen, better UX
- ❌ Server cost cao, navigation chậm hơn
- 🎯 **Dùng cho**: Public sites, marketing, e-commerce

**Modern Approach:**

- **Mix cả 3**: SSG (static pages) + SSR (dynamic) + CSR (interactive)
- **Framework**: Next.js, Remix, Nuxt.js hỗ trợ cả 3
- **Measure**: Dùng Lighthouse, Web Vitals để optimize

---

#### **📊 Sơ Đồ So Sánh CSR vs SSR**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CSR vs SSR COMPARISON                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  CLIENT-SIDE RENDERING (CSR)                                       │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │ 1. Browser Request → Server                                   │ │
│  │    GET https://example.com                                    │ │
│  │                                                                │ │
│  │ 2. Server Response (Minimal HTML)                             │ │
│  │    <!DOCTYPE html>                                            │ │
│  │    <html><head>...</head>                                     │ │
│  │    <body>                                                     │ │
│  │      <div id="root"></div>  ← Empty!                         │ │
│  │      <script src="/bundle.js"></script>                      │ │
│  │    </body></html>                                            │ │
│  │                                                                │ │
│  │ 3. Browser Downloads JS Bundle (Large!)                       │ │
│  │    bundle.js (500KB - 2MB)                                    │ │
│  │    ⏱️  Parsing + Execution time                               │ │
│  │                                                                │ │
│  │ 4. JavaScript Runs & Renders UI                               │ │
│  │    React.render(<App />, root)                               │ │
│  │    → API calls                                                │ │
│  │    → Fetch data                                               │ │
│  │    → Render components                                        │ │
│  │                                                                │ │
│  │ 5. User Sees Content                                          │ │
│  │    ⏱️  Total: 3-5 seconds                                     │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  SERVER-SIDE RENDERING (SSR)                                       │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │ 1. Browser Request → Server                                   │ │
│  │    GET https://example.com                                    │ │
│  │                                                                │ │
│  │ 2. Server Renders Full HTML                                   │ │
│  │    - Execute React on server                                  │ │
│  │    - Fetch data from database                                 │ │
│  │    - Generate complete HTML                                   │ │
│  │    ⏱️  Server processing time                                 │ │
│  │                                                                │ │
│  │ 3. Server Response (Full HTML)                                │ │
│  │    <!DOCTYPE html>                                            │ │
│  │    <html><head>...</head>                                     │ │
│  │    <body>                                                     │ │
│  │      <div id="root">                                          │ │
│  │        <h1>Welcome!</h1>                                      │ │
│  │        <p>Fully rendered content...</p>  ← Complete!         │ │
│  │      </div>                                                   │ │
│  │      <script src="/bundle.js"></script>                      │ │
│  │    </body></html>                                            │ │
│  │                                                                │ │
│  │ 4. Browser Shows Content Immediately                          │ │
│  │    ⏱️  User sees content: 0.5-1 second                        │ │
│  │                                                                │ │
│  │ 5. JavaScript Hydrates (Makes Interactive)                    │ │
│  │    React.hydrate(<App />, root)                              │ │
│  │    → Attach event listeners                                   │ │
│  │    → Make interactive                                         │ │
│  │    ⏱️  Total interactive: 2-3 seconds                         │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

#### **🔥 CSR (Client-Side Rendering) - Cách Hoạt Động Chi Tiết**

**Timeline:**

```
User clicks link
      ↓
[1] Browser → Server: GET /page
      ↓
[2] Server → Browser: Minimal HTML + <script src="bundle.js">
      ↓                 (5-50 KB)
      ↓
[3] Browser downloads bundle.js
      ↓                 (500KB - 2MB)
      ↓                 ⏱️  1-3 seconds
      ↓
[4] Browser parses & executes JS
      ↓                 ⏱️  0.5-1 second
      ↓
[5] React renders virtual DOM
      ↓
[6] React makes API calls
      ↓                 ⏱️  0.5-2 seconds
      ↓
[7] Data arrives → Re-render
      ↓
[8] User sees content
      ↓                 ⏱️  Total: 3-5 seconds
```

**Code Example (React CSR):**

```typescript
// ============================================
// CSR Example - React App
// ============================================

// index.html - Minimal HTML (chỉ có div rỗng)
// <!DOCTYPE html>
// <html>
// <head>
//   <title>My App</title>
// </head>
// <body>
//   <div id="root"></div>  ← EMPTY!
//   <script src="/bundle.js"></script>
// </body>
// </html>

// main.tsx - Entry point (Điểm vào - File bắt đầu chạy ứng dụng)
import React from 'react'; // Import React library (Thư viện React)
import ReactDOM from 'react-dom/client'; // Import ReactDOM để render (Để vẽ giao diện)
import App from './App'; // Import component App (Component chính)

// Render app on client (Vẽ ứng dụng trên client - Trình duyệt)
const root = ReactDOM.createRoot(document.getElementById('root')!); // Tạo root element (Tạo phần tử gốc - root là div#root trong HTML)
root.render(<App />); // Render component App vào root (Vẽ App vào phần tử gốc)

// App.tsx - Main component (Component chính)
import { useState, useEffect } from 'react'; // Import hooks (useState = quản lý state, useEffect = chạy side effects)

interface User {
  // Interface định nghĩa kiểu dữ liệu User (Định nghĩa cấu trúc dữ liệu người dùng)
  id: number; // ID người dùng (Số)
  name: string; // Tên người dùng (Chuỗi)
  email: string; // Email người dùng (Chuỗi)
}

function App() {
  // Component App - Component chính của ứng dụng
  const [users, setUsers] = useState<User[]>([]); // State lưu danh sách users (Trạng thái lưu danh sách người dùng - ban đầu là mảng rỗng)
  const [loading, setLoading] = useState(true); // State lưu trạng thái loading (Trạng thái đang tải - ban đầu là true)

  // Fetch data on client (Lấy dữ liệu trên client - Trình duyệt)
  useEffect(() => {
    // useEffect chạy sau khi component render (Chạy sau khi vẽ component)
    fetch('https://api.example.com/users') // Gọi API lấy danh sách users (Gửi request đến API)
      .then((res) => res.json()) // Chuyển response thành JSON (Chuyển phản hồi thành JSON)
      .then((data) => {
        // Khi có data (Khi có dữ liệu)
        setUsers(data); // Cập nhật state users (Cập nhật danh sách người dùng)
        setLoading(false); // Tắt loading (Tắt trạng thái đang tải)
      });
  }, []); // [] = chỉ chạy 1 lần khi component mount (Mảng rỗng = chỉ chạy 1 lần khi component được gắn vào)

  if (loading) {
    // Nếu đang loading (Nếu đang tải)
    return <div>Loading...</div>; // Hiển thị "Loading..." (User sees loading state - Người dùng thấy trạng thái đang tải)
  }

  return (
    // Return JSX (Trả về JSX - JavaScript XML - Cú pháp giống HTML)
    <div>
      <h1>Users</h1> {/* Tiêu đề */}
      <ul>
        {/* Danh sách không có thứ tự */}
        {users.map((user) => (
          // Duyệt qua mảng users và render mỗi user (Lặp qua danh sách người dùng)
          <li key={user.id}>
            {/* Mỗi item cần key (Mỗi phần tử cần key để React theo dõi) */}
            {user.name} - {user.email} {/* Hiển thị tên và email */}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;

// ============================================
// What happens in browser:
// ============================================
// 1. Download HTML (5KB) - instant
// 2. Download bundle.js (500KB) - 1-2 seconds
// 3. Parse & execute JS - 0.5 seconds
// 4. React renders <div>Loading...</div>
// 5. Fetch API - 0.5-1 second
// 6. Re-render with data
// Total: 3-5 seconds until user sees content
```

---

#### **🚀 SSR (Server-Side Rendering) - Cách Hoạt Động Chi Tiết**

**Timeline:**

```
User clicks link
      ↓
[1] Browser → Server: GET /page
      ↓
[2] Server executes React
      ↓
[3] Server fetches data from DB
      ↓                 ⏱️  0.1-0.5 seconds
      ↓
[4] Server renders HTML
      ↓                 ⏱️  0.1-0.3 seconds
      ↓
[5] Server → Browser: Full HTML
      ↓                 (50-200 KB)
      ↓
[6] Browser displays HTML immediately
      ↓                 ⏱️  User sees content: 0.5-1 second
      ↓
[7] Browser downloads JS bundle
      ↓                 (background)
      ↓
[8] Hydration - Make interactive
      ↓                 ⏱️  0.5-1 second
      ↓
[9] Fully interactive
      ↓                 ⏱️  Total interactive: 2-3 seconds
```

**Code Example (Next.js SSR):**

```typescript
// ============================================
// SSR Example - Next.js
// ============================================

// pages/users.tsx - SSR page (Trang SSR - Server-Side Rendering)
import { GetServerSideProps } from 'next'; // Import type từ Next.js (Import kiểu dữ liệu từ Next.js)

interface User {
  // Interface định nghĩa kiểu User (Định nghĩa cấu trúc dữ liệu người dùng)
  id: number; // ID người dùng
  name: string; // Tên người dùng
  email: string; // Email người dùng
}

interface Props {
  // Interface định nghĩa props của component (Props là dữ liệu truyền vào component)
  users: User[]; // Mảng users (Danh sách người dùng)
}

// This function runs on SERVER for every request (Hàm này chạy trên SERVER cho mỗi request - Mỗi yêu cầu)
export const getServerSideProps: GetServerSideProps<Props> = async () => {
  // Export function getServerSideProps (Xuất hàm getServerSideProps - Next.js sẽ gọi hàm này trên server)
  // Fetch data on server (Lấy dữ liệu trên server)
  const res = await fetch('https://api.example.com/users'); // Gọi API (Gửi request đến API)
  const users = await res.json(); // Chuyển response thành JSON (Chuyển phản hồi thành JSON)

  // Pass data to component as props (Truyền dữ liệu vào component qua props)
  return {
    // Trả về object với props (Trả về đối tượng chứa props)
    props: {
      users, // This data is already available! (Dữ liệu này đã có sẵn! - Không cần đợi trên client)
    },
  };
};

// Component renders on server (Component render trên server)
function UsersPage({ users }: Props) {
  // Component nhận users từ props (Component nhận danh sách users từ props)
  // No loading state needed - data is already here! (Không cần loading state - Dữ liệu đã có sẵn!)
  return (
    <div>
      <h1>Users</h1> {/* Tiêu đề */}
      <ul>
        {/* Danh sách */}
        {users.map((user) => (
          // Duyệt qua users và render (Lặp qua danh sách người dùng)
          <li key={user.id}>
            {/* Mỗi item cần key (Mỗi phần tử cần key) */}
            {user.name} - {user.email} {/* Hiển thị tên và email */}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default UsersPage;

// ============================================
// What happens:
// ============================================
// 1️⃣ User requests /users
// 2️⃣ Next.js server:
//    - 🔄 Runs getServerSideProps() - Chạy hàm fetch data
//    - 📡 Fetches data from API - Lấy data từ API
//    - 🖨️ Renders component to HTML string - Render thành HTML
//    - 📤 Sends full HTML to browser - Gửi HTML đầy đủ
// 3️⃣ Browser displays HTML immediately (0.5-1s) - ⚡ Hiển thị ngay!
// 4️⃣ JavaScript hydrates in background - 💧 Hydrate (chạy ngầm)
// 5️⃣ Page becomes interactive (2-3s total) - 🎯 Có thể tương tác

// ============================================
// HTML sent to browser (Full content!):
// ============================================
// <!DOCTYPE html>
// <html>
// <head>
//   <title>My App</title>
// </head>
// <body>
//   <div id="__next">
//     <div>
//       <h1>Users</h1>
//       <ul>
//         <li>John Doe - john@example.com</li>
//         <li>Jane Smith - jane@example.com</li>
//         <!-- Full content already rendered! -->
//       </ul>
//     </div>
//   </div>
//   <script src="/_next/static/bundle.js"></script>
// </body>
// </html>
```

---

#### **📊 So Sánh Chi Tiết CSR vs SSR**

```
┌──────────────────────┬──────────────────────────┬──────────────────────────┐
│ Tiêu Chí             │ CSR (Client-Side)        │ SSR (Server-Side)        │
├──────────────────────┼──────────────────────────┼──────────────────────────┤
│ Initial Load         │ ❌ 3-5 seconds           │ ✅ 0.5-1 second          │
│ Time to Interactive  │ ✅ 3-5 seconds           │ ⚠️  2-3 seconds          │
│ SEO                  │ ❌ Poor (empty HTML)     │ ✅ Excellent (full HTML) │
│ Server Load          │ ✅ Low (serve static)    │ ❌ High (render per req) │
│ Complexity           │ ✅ Simple                │ ❌ Complex               │
│ Navigation Speed     │ ✅ Instant               │ ⚠️  Slower (re-render)   │
│ Bundle Size          │ ❌ Large (500KB-2MB)     │ ⚠️  Medium (same JS)     │
│ Blank Screen         │ ❌ Yes (before hydrate)  │ ✅ No (HTML ready)       │
│ API Calls            │ ❌ Client (slow)         │ ✅ Server (fast)         │
│ Caching              │ ✅ Easy (CDN)            │ ⚠️  Complex (per-user)   │
│ Cost                 │ ✅ Low (CDN only)        │ ❌ High (servers)        │
│ User Experience      │ ⚠️  Initial: Poor        │ ✅ Initial: Great        │
│                      │ ✅ After load: Great     │ ⚠️  Navigation: OK       │
└──────────────────────┴──────────────────────────┴──────────────────────────┘
```

---

#### **🎯 Use Cases - Khi Nào Dùng CSR vs SSR?**

**✅ Dùng CSR khi:**

```typescript
// 1. Admin Dashboard / Internal Tools
// - Không cần SEO
// - User đã logged in
// - Rich interactions
// - Example: Analytics dashboard, CRM

// 2. SPAs with Auth
// - Dashboard, Settings
// - User profile pages
// - Tools, calculators

// 3. Highly Interactive Apps
// - Drawing apps
// - Games
// - Real-time collaboration tools

// Example: (Ví dụ)
const AdminDashboard = () => {
  // Component AdminDashboard (Component bảng điều khiển admin)
  return (
    <div>
      <Chart data={realtimeData} />{' '}
      {/* Real-time updates (Cập nhật thời gian thực) */}
      {/* Chart = Biểu đồ (Component biểu đồ với dữ liệu thời gian thực) */}
      <DataGrid onEdit={handleEdit} />{' '}
      {/* Complex interactions (Tương tác phức tạp) */}
      {/* DataGrid = Bảng dữ liệu (Component bảng với chức năng chỉnh sửa) */}
      {/* onEdit = Callback khi edit (Hàm gọi lại khi chỉnh sửa) */}
    </div>
  );
};
```

**✅ Dùng SSR khi:**

```typescript
// 1. Public Content / Marketing
// - Landing pages
// - Blogs, News
// - E-commerce product pages
// - Example: Company website, Blog

// 2. SEO-Critical Pages
// - Product listings
// - Article pages
// - Search result pages

// 3. Dynamic Content
// - Personalized homepages
// - Location-based content
// - User-specific dashboards

// Example: (Ví dụ)
export const getServerSideProps = async (context) => {
  // Export getServerSideProps (Xuất hàm getServerSideProps - Chạy trên server)
  // context = Context chứa request info (Context chứa thông tin request)
  // Fetch based on user location (Lấy dữ liệu dựa trên vị trí người dùng)
  const { country } = context.req.geo; // Lấy country từ geo (Lấy quốc gia từ thông tin địa lý)
  // context.req.geo = Thông tin địa lý từ request (Thông tin địa lý từ yêu cầu)
  const products = await fetchProductsByCountry(country); // Lấy sản phẩm theo country (Lấy sản phẩm theo quốc gia)

  return { props: { products } }; // Trả về props (Trả về dữ liệu sản phẩm)
};

const ProductPage = ({ products }) => {
  // Component nhận products từ props (Component nhận danh sách sản phẩm)
  return (
    <div>
      <h1>Products in Your Region</h1>{' '}
      {/* Tiêu đề (Sản phẩm trong khu vực của bạn) */}
      {products.map((p) => (
        // Duyệt qua products (Lặp qua danh sách sản phẩm)
        <ProductCard key={p.id} {...p} />
        // ProductCard = Component hiển thị sản phẩm (Component thẻ sản phẩm)
        // key = Key cho React (Key để React theo dõi)
        // {...p} = Spread props (Truyền tất cả thuộc tính của p vào component)
      ))}
    </div>
  );
};
```

---

#### **⚡ Hybrid Approach - Static Site Generation (SSG)**

Next.js còn có SSG (Static Site Generation) - best of both worlds:

```typescript
// ============================================
// SSG Example - Next.js
// ============================================

// Build time: Generate static HTML (Thời gian build: Tạo HTML tĩnh)
export const getStaticProps: GetStaticProps = async () => {
  // Export function getStaticProps (Xuất hàm getStaticProps - Chạy khi build, không phải mỗi request)
  // This runs at BUILD TIME, not per request (Chạy khi BUILD, không phải mỗi request - Chỉ chạy 1 lần khi build)
  const res = await fetch('https://api.example.com/posts'); // Gọi API lấy posts (Gửi request lấy bài viết)
  const posts = await res.json(); // Chuyển thành JSON (Chuyển phản hồi thành JSON)

  return {
    // Trả về props (Trả về dữ liệu)
    props: { posts }, // Truyền posts vào component (Truyền danh sách bài viết)
    revalidate: 60, // Re-generate every 60 seconds (ISR) (Tái tạo mỗi 60 giây - ISR = Incremental Static Regeneration - Tái tạo tĩnh tăng dần)
  };
};

// Component (Component)
const BlogPage = ({ posts }) => {
  // Component nhận posts từ props (Component nhận danh sách bài viết)
  return (
    <div>
      <h1>Blog Posts</h1> {/* Tiêu đề */}
      {posts.map((post) => (
        // Duyệt qua posts (Lặp qua danh sách bài viết)
        <article key={post.id}>
          {/* Mỗi bài viết cần key (Mỗi phần tử cần key) */}
          <h2>{post.title}</h2> {/* Tiêu đề bài viết */}
          <p>{post.excerpt}</p> {/* Tóm tắt bài viết */}
        </article>
      ))}
    </div>
  );
};

// ============================================
// Benefits:
// ============================================
// ✅ Fast as CSR (served from CDN)
// ✅ SEO-friendly like SSR
// ✅ No server rendering cost
// ✅ ISR (Incremental Static Regeneration)

// Timeline:
// [Build] Generate HTML → Deploy to CDN
//    ↓
// [Request] CDN → Browser (instant!)
//    ↓
// [Background] Re-validate every 60s
```

---

#### **📋 Best Practices**

**1. CSR Optimization:**

```typescript
// ✅ Code splitting - Tách code thành nhiều file nhỏ (Chia nhỏ code để tải nhanh hơn)
import { lazy, Suspense } from 'react'; // Import lazy và Suspense (lazy = tải chậm, Suspense = hiển thị loading)

// 📦 Lazy load component (chỉ tải khi cần - Lazy loading = Tải khi cần thiết)
const HeavyComponent = lazy(() => import('./HeavyComponent')); // Tạo component lazy (Tạo component tải chậm - chỉ tải khi dùng)

function App() {
  return (
    // 🔄 Suspense: Hiển thị Loading trong khi đợi component tải (Suspense = Hiển thị loading khi đợi)
    <Suspense fallback={<Loading />}>
      {/* fallback = Hiển thị gì khi đang tải (fallback = phần tử hiển thị khi đang tải) */}
      <HeavyComponent /> {/* Component sẽ được tải khi cần (Component này sẽ tải khi cần) */}
    </Suspense>
  );
}

// ✅ Preload critical data - Tải trước data quan trọng (Preload = Tải trước dữ liệu quan trọng)
<link rel="preload" href="/api/users" as="fetch" crossOrigin="anonymous" />;
// rel="preload" = Báo browser tải trước (Báo trình duyệt tải trước)
// as="fetch" = Kiểu tải là fetch (Kiểu tải là fetch - Gọi API)
// crossOrigin="anonymous" = Cho phép cross-origin (Cho phép tải từ domain khác)

// ✅ Service Worker caching - Cache offline (Service Worker = Cache để dùng offline)
if ('serviceWorker' in navigator) {
  // Kiểm tra browser có hỗ trợ Service Worker (Kiểm tra trình duyệt có hỗ trợ Service Worker)
  // 🗄️ Đăng ký service worker để cache file (Đăng ký service worker để lưu cache file)
  navigator.serviceWorker.register('/sw.js'); // Đăng ký service worker (Đăng ký file service worker)
}
```

**2. SSR Optimization:**

```typescript
// ✅ Cache rendered pages - Cache trang đã render (Lưu cache trang đã render)
import { NextResponse } from 'next/server'; // Import NextResponse từ Next.js (Import NextResponse để xử lý response)

export async function middleware(request) {
  // Export function middleware (Xuất hàm middleware - Middleware = Xử lý trước khi render)
  const response = NextResponse.next(); // Tạo response tiếp theo (Tạo phản hồi tiếp theo)
  // 🗄️ Cache Control: Lưu cache 60s, dùng stale trong 120s (Lưu cache 60 giây, dùng dữ liệu cũ trong 120 giây)
  response.headers.set(
    // Set header Cache-Control (Thiết lập header Cache-Control)
    'Cache-Control',
    'public, max-age=60, stale-while-revalidate=120'
    // public = Cache công khai (Cache có thể dùng chung)
    // max-age=60 = Cache 60 giây (Lưu cache 60 giây)
    // stale-while-revalidate=120 = Dùng dữ liệu cũ trong khi tái xác thực 120 giây (Dùng dữ liệu cũ trong khi kiểm tra lại)
  );
  return response; // Trả về response (Trả về phản hồi)
}

// ✅ Streaming SSR (React 18) - Gửi HTML từng phần (Streaming SSR = Gửi HTML từng phần thay vì chờ hết)
import { renderToReadableStream } from 'react-dom/server'; // Import renderToReadableStream (Import hàm render thành stream)

// 📡 Stream HTML thay vì chờ render hết (faster TTFB) (Gửi HTML từng phần thay vì chờ render hết - TTFB nhanh hơn)
const stream = await renderToReadableStream(<App />); // Render App thành stream (Vẽ App thành luồng dữ liệu)
return new Response(stream); // Trả về Response với stream (Trả về Response chứa stream)

// ✅ Selective hydration - Chỉ hydrate một phần (Selective hydration = Chỉ hydrate phần cần thiết)
// 💧 suppressHydrationWarning: Bỏ qua warning khi nội dung server-only (Bỏ qua cảnh báo khi nội dung chỉ có trên server)
<div suppressHydrationWarning>{serverOnlyContent}</div>;
// suppressHydrationWarning = Bỏ qua cảnh báo hydration (Bỏ qua cảnh báo khi HTML server khác client)
// serverOnlyContent = Nội dung chỉ có trên server (Nội dung chỉ render trên server)
```

**3. Hybrid Strategy:**

```typescript
// ✅ Mix CSR + SSR + SSG (Kết hợp CSR + SSR + SSG)
// - SSG: Static pages (blog, docs) (SSG cho trang tĩnh - Blog, tài liệu)
// - SSR: Dynamic pages (user profile) (SSR cho trang động - Hồ sơ người dùng)
// - CSR: Interactive parts (comments, likes) (CSR cho phần tương tác - Bình luận, like)

// pages/post/[id].tsx (Trang bài viết với dynamic route - [id] = tham số động)
export const getStaticProps = async ({ params }) => {
  // Export getStaticProps (Xuất hàm getStaticProps - Chạy khi build)
  const post = await fetchPost(params.id); // SSG - Lấy bài viết theo ID (Lấy bài viết - SSG = Static Site Generation)
  return { props: { post } }; // Trả về props (Trả về dữ liệu bài viết)
};

const PostPage = ({ post }) => {
  // Component nhận post từ props (Component nhận bài viết)
  return (
    <div>
      {/* SSG content (Nội dung SSG - Đã render sẵn) */}
      <article>{post.content}</article>
      {/* Article = Bài viết (Nội dung bài viết đã được render sẵn) */}
      {/* CSR interactive part (Phần tương tác CSR - Render trên client) */}
      <Comments postId={post.id} />{' '}
      {/* Component Comments - Tải và render trên client (Component bình luận) */}
      <LikeButton postId={post.id} /> {/* Component LikeButton - Tải và render trên client (Component nút like) */}
    </div>
  );
};
```

---

#### **🔍 Debugging & Measuring**

```typescript
// 1️⃣ Measure Time to First Byte (TTFB) - Đo thời gian đến byte đầu tiên
// ⏱️ TTFB: Thời gian từ khi click đến khi nhận byte đầu từ server (TTFB = Time To First Byte)
performance.getEntriesByType('navigation')[0].responseStart;
// performance.getEntriesByType('navigation') = Lấy thông tin navigation (Lấy thông tin điều hướng)
// [0].responseStart = Thời điểm bắt đầu nhận response (Thời điểm bắt đầu nhận phản hồi)

// 2️⃣ Measure First Contentful Paint (FCP) - Đo thời gian vẽ nội dung đầu
// 🎨 FCP: Thời gian đến khi user thấy nội dung đầu tiên (FCP = First Contentful Paint - Vẽ nội dung đầu tiên)
new PerformanceObserver((list) => {
  // Tạo PerformanceObserver để theo dõi performance (Tạo người quan sát hiệu suất)
  for (const entry of list.getEntries()) {
    // Duyệt qua các entry (Lặp qua các mục)
    console.log('FCP:', entry.startTime); // Log thời gian FCP (Ghi log thời gian FCP)
  }
}).observe({ entryTypes: ['paint'] }); // Quan sát các sự kiện paint (Theo dõi các sự kiện vẽ)

// 3️⃣ Detect SSR vs CSR - Phát hiện đang render ở đâu (Phát hiện đang render trên server hay client)
// 🔍 Check môi trường: Server (no window) hay Client (có window) (Kiểm tra môi trường)
const isSSR = typeof window === 'undefined'; // Kiểm tra có window không (window chỉ có trên browser)
// typeof window === 'undefined' = Không có window = đang ở server (Không có window = đang ở server)
console.log('Rendering on:', isSSR ? 'Server' : 'Client'); // Log môi trường render (Ghi log môi trường)

// 4️⃣ Chrome DevTools - Công cụ debug (Công cụ gỡ lỗi Chrome)
// 🌐 Network tab: Check HTML size (SSR = lớn, CSR = nhỏ) (Tab Network: Kiểm tra kích thước HTML)
// ⚡ Performance tab: Xem timeline render (Tab Performance: Xem dòng thời gian render)
// 💯 Lighthouse: Chạy audit để so sánh SSR vs CSR (Lighthouse: Chạy kiểm tra để so sánh)
```

---

#### **❌ Common Mistakes**

```typescript
// ❌ MISTAKE 1: Using window/document in SSR (LỖI 1: Dùng window/document trong SSR)
function MyComponent() {
  // Component MyComponent (Component của tôi)
  // 🐛 Lỗi: window chỉ có trên browser, server không có! (window chỉ có trên trình duyệt, server không có)
  const width = window.innerWidth; // ❌ Error: window is not defined (Lỗi: window không được định nghĩa)
  // window.innerWidth = Chiều rộng cửa sổ (window chỉ có trên browser)
  return <div style={{ width }}></div>; // Return JSX với style (Trả về JSX với style)
}

// ✅ FIX: Check environment - Kiểm tra môi trường (SỬA: Kiểm tra môi trường)
function MyComponent() {
  // Component đã sửa (Component đã được sửa)
  const [width, setWidth] = useState(0); // State lưu width (Trạng thái lưu chiều rộng - ban đầu là 0)

  // 🔧 useEffect chỉ chạy trên client, an toàn! (useEffect chỉ chạy trên client, an toàn)
  useEffect(() => {
    // useEffect chạy sau khi render (Chạy sau khi vẽ component)
    // 🔍 Check nếu có window (= browser environment) (Kiểm tra nếu có window = môi trường browser)
    if (typeof window !== 'undefined') {
      // Nếu window tồn tại (Nếu có window)
      setWidth(window.innerWidth); // ✅ An toàn - Set width (An toàn - Thiết lập chiều rộng)
    }
  }, []); // [] = chỉ chạy 1 lần (Mảng rỗng = chỉ chạy 1 lần)

  return <div style={{ width }}></div>; // Return JSX (Trả về JSX)
}

// ❌ MISTAKE 2: Fetching data in useEffect for SSR (LỖI 2: Lấy dữ liệu trong useEffect cho SSR)
export default function Page() {
  // Component Page (Component trang)
  const [data, setData] = useState(null); // State lưu data (Trạng thái lưu dữ liệu - ban đầu là null)

  useEffect(() => {
    // useEffect chạy trên client (Chạy trên trình duyệt)
    // 🐛 Lỗi: useEffect chạy trên client → SEO không thấy data! (useEffect chạy trên client → SEO không thấy dữ liệu)
    fetch('/api/data').then(/* ... */); // ❌ Runs on client! (Chạy trên client - Google bot không thấy)
    // fetch = Gọi API (Gửi request đến API)
  }, []); // [] = chỉ chạy 1 lần (Mảng rỗng = chỉ chạy 1 lần)

  return <div>{data?.title}</div>; // ⚠️ Google bot thấy null (Google bot thấy null - Không có dữ liệu)
  // data?.title = Optional chaining (Truy cập an toàn - Nếu data null thì trả về undefined)
}

// ✅ FIX: Use getServerSideProps - Fetch data trên server (SỬA: Dùng getServerSideProps - Lấy dữ liệu trên server)
export const getServerSideProps = async () => {
  // Export getServerSideProps (Xuất hàm getServerSideProps - Chạy trên server)
  // 🖥️ Chạy trên server → SEO-friendly (Chạy trên server → Thân thiện SEO)
  const data = await fetch('/api/data').then((r) => r.json()); // Gọi API và chuyển thành JSON (Gửi request và chuyển thành JSON)
  return { props: { data } }; // 📦 Truyền data vào component (Truyền dữ liệu vào component qua props)
};

export default function Page({ data }) {
  // Component nhận data từ props (Component nhận dữ liệu từ props)
  // ✅ Data đã có sẵn, Google bot thấy ngay! (Dữ liệu đã có sẵn, Google bot thấy ngay)
  return <div>{data.title}</div>; // Return JSX với data (Trả về JSX với dữ liệu)
}

// ❌ MISTAKE 3: Over-using SSR - Dùng SSR cho mọi thứ
// 💡 Don't SSR everything - mix strategies! (Đừng SSR hết!)

// ✅ GOOD: Strategic mix - Kết hợp chiến lược
// - 📄 SSG: Blog posts, docs (static) - Nội dung tĩnh
// - 🖥️ SSR: User dashboard (dynamic) - Nội dung động theo user
// - 💻 CSR: Admin panel (no SEO needed) - Không cần SEO
```

---

#### **📊 Real-world Performance Comparison**

```typescript
// Example: E-commerce Product Page

// CSR (Create React App):
// - Initial Load: 3.5 seconds
// - Time to Interactive: 3.5 seconds
// - Lighthouse Score: 40/100
// - SEO: ❌ Poor (Google sees empty HTML)

// SSR (Next.js):
// - Initial Load: 1.2 seconds
// - Time to Interactive: 2.8 seconds
// - Lighthouse Score: 85/100
// - SEO: ✅ Excellent (Google sees full content)

// SSG (Next.js ISR):
// - Initial Load: 0.5 seconds (CDN)
// - Time to Interactive: 1.8 seconds
// - Lighthouse Score: 95/100
// - SEO: ✅ Excellent + fast delivery
```

---

#### **🎯 Decision Tree**

```
Start
  ↓
SEO needed?
  ├─ No → CSR (React, Vue, Angular SPA)
  │
  └─ Yes → Content changes frequently?
           ├─ No → SSG (Next.js, Gatsby)
           │        - Blog, docs, marketing
           │
           └─ Yes → Per-user content?
                    ├─ No → SSR with cache
                    │        - News, products
                    │
                    └─ Yes → SSR + ISR
                             - User dashboards
                             - Personalized pages
```

---

#### **💡 Summary**

**CSR (Client-Side Rendering):**

- ✅ Best for: SPAs, admin tools, internal apps
- ✅ Pros: Simple, fast navigation, low server cost
- ❌ Cons: Slow initial load, poor SEO, blank screen

**SSR (Server-Side Rendering):**

- ✅ Best for: Public pages, SEO-critical, e-commerce
- ✅ Pros: Fast initial load, SEO-friendly, no blank screen
- ❌ Cons: High server cost, complex, slower navigation

**SSG (Static Site Generation):**

- ✅ Best for: Blogs, docs, marketing pages
- ✅ Pros: Fastest, SEO-friendly, low cost (CDN)
- ❌ Cons: Stale data (solved with ISR)

**Modern Approach: (Cách tiếp cận hiện đại)**

```typescript
// Mix all three strategies! (Kết hợp cả 3 chiến lược!)
// - SSG for static pages (blog, docs) (SSG cho trang tĩnh - Blog, tài liệu)
// - SSR for dynamic pages (user profile, search) (SSR cho trang động - Hồ sơ người dùng, tìm kiếm)
// - CSR for interactive parts (comments, likes) (CSR cho phần tương tác - Bình luận, like)

// Example: E-commerce site (Ví dụ: Trang thương mại điện tử)
// - Homepage: SSG (revalidate hourly) (Trang chủ: SSG - Tái xác thực mỗi giờ)
//   // revalidate = Tái xác thực (Tái tạo lại sau một khoảng thời gian)
// - Product page: SSR (real-time inventory) (Trang sản phẩm: SSR - Hàng tồn kho thời gian thực)
//   // real-time inventory = Hàng tồn kho thời gian thực (Cần cập nhật liên tục)
// - Cart: CSR (no SEO needed) (Giỏ hàng: CSR - Không cần SEO)
//   // Cart = Giỏ hàng (Chỉ user đã login mới thấy)
// - Checkout: SSR (security + UX) (Thanh toán: SSR - Bảo mật + Trải nghiệm người dùng)
//   // Checkout = Thanh toán (Cần bảo mật và UX tốt)
```

**Key Takeaway: (Điểm quan trọng)**

- There's NO "best" approach - choose based on requirements (Không có cách "tốt nhất" - Chọn dựa trên yêu cầu)
- Modern frameworks (Next.js, Remix) support all strategies (Framework hiện đại hỗ trợ tất cả chiến lược)
  // Next.js = Framework React với SSR/SSG (Framework React hỗ trợ SSR/SSG)
  // Remix = Framework React với SSR (Framework React tập trung vào SSR)
- Measure with real data: TTFB, FCP, TTI, Lighthouse (Đo bằng dữ liệu thực: TTFB, FCP, TTI, Lighthouse)
  // TTFB = Time To First Byte (Thời gian đến byte đầu tiên)
  // FCP = First Contentful Paint (Vẽ nội dung đầu tiên)
  // TTI = Time To Interactive (Thời gian đến khi tương tác được)
  // Lighthouse = Công cụ đo performance (Công cụ đo hiệu suất của Google)
- SEO + Performance = SSR/SSG (SEO + Hiệu suất = SSR/SSG)
- Interactivity + Simple = CSR (Tương tác + Đơn giản = CSR)

```
💧 Hydration là quá trình Server render ra HTML → Browser hiển thị ngay → Sau đó React "gắn" event listeners vào HTML → UI trở nên tương tác được.
// Hydration = Quá trình gắn JavaScript vào HTML đã render sẵn (Quá trình làm cho HTML tĩnh trở nên tương tác)
// event listeners = Bộ lắng nghe sự kiện (Các hàm xử lý sự kiện như click, hover)
// UI = User Interface (Giao diện người dùng)

"Hydration là bước React biến HTML do SSR hoặc SSG render sẵn thành UI có thể tương tác, bằng cách attach event listeners và khôi phục state.
// attach = Gắn (Gắn event listeners vào các phần tử HTML)
// state = Trạng thái (Trạng thái của component - Dữ liệu động)

HTML từ server ngay lập tức giúp cải thiện SEO và First Contentful Paint, còn hydration giúp UI hoạt động như SPA. Thách thức lớn nhất là tránh hydration mismatch và tối ưu cost hydration trong các trang lớn bằng techniques như partial/lazy hydration.
// SEO = Search Engine Optimization (Tối ưu hóa công cụ tìm kiếm)
// First Contentful Paint = Vẽ nội dung đầu tiên (Thời điểm user thấy nội dung đầu tiên)
// SPA = Single Page Application (Ứng dụng một trang)
// hydration mismatch = HTML server khác HTML client (HTML server không khớp với HTML client)
// partial hydration = Hydration một phần (Chỉ hydrate phần cần thiết)
// lazy hydration = Hydration chậm (Hydrate khi cần)
```
