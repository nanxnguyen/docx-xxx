# 💾 Q26: Handle Caching - HTTP Caching & Browser Cache Strategies




**⚡ Quick Summary:**
> HTTP Cache = Cache-Control, ETag. Browser Cache = disk/memory cache. Service Worker = offline cache

**💡 Ghi Nhớ:**
- 📦 **Cache-Control**: max-age, no-cache, no-store
- 🏷️ **ETag**: Validation token cho conditional requests
- 💾 **Storage**: localStorage (persist), sessionStorage (tab), Cache API (PWA)

**Trả lời:**

- **HTTP Caching**: Cơ chế lưu trữ responses để tránh tải lại resources, giảm latency và bandwidth
- **Cache Types**: Browser Cache, Service Worker Cache, Memory Cache, Disk Cache, CDN Cache
- **Cache Headers**: Cache-Control, ETag, Last-Modified, Expires, Vary
- **🔥 Ưu điểm**: Tăng tốc độ load page, giảm server load, tiết kiệm bandwidth, cải thiện UX
- **⚠️ Nhược điểm**: Có thể serve stale data, phức tạp khi manage cache invalidation, storage limitations

**🎯 HTTP Cache Headers & Directives:**

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     HTTP CACHE ARCHITECTURE                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1️⃣  BROWSER CACHE (Memory + Disk)                                     │
│      ┌─────────────────────────────────────────────────────────┐       │
│      │  📦 Cache-Control: max-age=3600 (1 hour)               │       │
│      │  📦 Cache-Control: public/private                       │       │
│      │  📦 Cache-Control: no-cache/no-store                    │       │
│      │  📦 ETag: "abc123" (version tag)                        │       │
│      │  📦 Last-Modified: Thu, 01 Jan 2024 00:00:00 GMT        │       │
│      └─────────────────────────────────────────────────────────┘       │
│                                                                          │
│  2️⃣  SERVICE WORKER CACHE                                              │
│      ┌─────────────────────────────────────────────────────────┐       │
│      │  🚀 Cache First (Static Assets)                         │       │
│      │  🌐 Network First (Dynamic Data)                        │       │
│      │  ⚡ Stale While Revalidate (Balance)                    │       │
│      │  📱 Cache Only (Offline First)                          │       │
│      └─────────────────────────────────────────────────────────┘       │
│                                                                          │
│  3️⃣  CDN CACHE (Edge Servers)                                          │
│      ┌─────────────────────────────────────────────────────────┐       │
│      │  🌍 Cloudflare, AWS CloudFront, Fastly                  │       │
│      │  📡 Geographic distribution                             │       │
│      │  ⚡ Edge caching for static assets                      │       │
│      └─────────────────────────────────────────────────────────┘       │
│                                                                          │
│  4️⃣  APPLICATION CACHE (LocalStorage, IndexedDB)                       │
│      ┌─────────────────────────────────────────────────────────┐       │
│      │  💾 localStorage (5-10MB, synchronous)                  │       │
│      │  💾 sessionStorage (per-tab)                            │       │
│      │  💾 IndexedDB (large data, async)                       │       │
│      └─────────────────────────────────────────────────────────┘       │
└─────────────────────────────────────────────────────────────────────────┘
```

**Code Example:**

```typescript
// ============================================
// 1. HTTP CACHE HEADERS - Server-Side Setup
// ============================================

// Express.js example - Setting cache headers
import express, { Request, Response } from 'express';
import path from 'path';

const app = express();

// 🔥 Static Assets - Long-term caching (1 năm)
// Cho các file có hash trong tên: app.abc123.js
app.use(
  '/static',
  express.static('public', {
    maxAge: '365d', // Cache 1 năm
    immutable: true, // Báo browser file này không bao giờ thay đổi
    setHeaders: (res: Response, filePath: string) => {
      // Set cache headers chi tiết
      res.setHeader('Cache-Control', 'public, max-age=31536000, immutable');
      res.setHeader('Vary', 'Accept-Encoding'); // Cache riêng cho gzip/brotli
    },
  })
);

// 🎯 HTML Files - No cache (luôn kiểm tra mới nhất)
app.get('*.html', (req: Request, res: Response) => {
  res.setHeader('Cache-Control', 'no-cache, no-store, must-revalidate');
  res.setHeader('Pragma', 'no-cache'); // HTTP/1.0 backward compatibility
  res.setHeader('Expires', '0'); // Legacy browsers
  res.sendFile(path.join(__dirname, 'public', req.path));
});

// ⚡ API Responses - Short-term caching (5 phút)
app.get('/api/data', (req: Request, res: Response) => {
  const data = { message: 'Hello World', timestamp: Date.now() };

  // Cache 5 phút, nhưng revalidate với server
  res.setHeader('Cache-Control', 'public, max-age=300, must-revalidate');

  // ETag để conditional requests
  const etag = generateETag(data); // Hash của data
  res.setHeader('ETag', etag);

  // Last-Modified header
  res.setHeader('Last-Modified', new Date().toUTCString());

  // Kiểm tra If-None-Match header (ETag matching)
  if (req.headers['if-none-match'] === etag) {
    // Data không đổi → 304 Not Modified (không gửi body)
    return res.status(304).end();
  }

  res.json(data);
});

// 📦 Images - Medium-term caching (1 tuần)
app.use('/images', (req: Request, res: Response, next) => {
  res.setHeader('Cache-Control', 'public, max-age=604800'); // 7 days
  res.setHeader('Vary', 'Accept'); // Cache riêng cho WebP/JPEG
  next();
});

// ============================================
// 2. ETAG GENERATION (Tạo Version Tag)
// ============================================

import crypto from 'crypto';

function generateETag(data: any): string {
  // Hash nội dung để tạo ETag unique
  const hash = crypto
    .createHash('md5')
    .update(JSON.stringify(data))
    .digest('hex');

  return `"${hash}"`; // ETag format: "abc123"
}

// Sử dụng ETag cho conditional requests
async function fetchWithETag(url: string, cachedETag?: string): Promise<any> {
  const headers: HeadersInit = {};

  // Gửi ETag đã cache để kiểm tra
  if (cachedETag) {
    headers['If-None-Match'] = cachedETag;
  }

  const response = await fetch(url, { headers });

  // 304 Not Modified → Dùng cached data
  if (response.status === 304) {
    console.log('✅ Sử dụng cached data (304 Not Modified)');
    return null; // Không có data mới
  }

  // 200 OK → Data mới, lưu ETag
  const newETag = response.headers.get('ETag');
  const data = await response.json();

  console.log('📥 Data mới, lưu ETag:', newETag);

  return { data, etag: newETag };
}

// ============================================
// 3. BROWSER CACHE API - Client-Side Caching
// ============================================

// 🔥 Cache Manager Class
class CacheManager {
  private cacheName = 'my-app-cache-v1';

  // Lưu response vào cache
  async cacheResponse(url: string, response: Response): Promise<void> {
    try {
      const cache = await caches.open(this.cacheName);

      // Clone response vì response.body chỉ đọc được 1 lần
      await cache.put(url, response.clone());

      console.log(`✅ Cached: ${url}`);
    } catch (error) {
      console.error('❌ Cache error:', error);
    }
  }

  // Lấy response từ cache
  async getCachedResponse(url: string): Promise<Response | undefined> {
    try {
      const cache = await caches.open(this.cacheName);
      const cachedResponse = await cache.match(url);

      if (cachedResponse) {
        console.log(`✅ Cache hit: ${url}`);
        return cachedResponse;
      }

      console.log(`❌ Cache miss: ${url}`);
      return undefined;
    } catch (error) {
      console.error('❌ Cache read error:', error);
      return undefined;
    }
  }

  // Xóa cache cũ
  async clearOldCaches(): Promise<void> {
    const cacheNames = await caches.keys();

    await Promise.all(
      cacheNames.map((name) => {
        // Xóa cache không phải version hiện tại
        if (name !== this.cacheName) {
          console.log(`🗑️ Deleting old cache: ${name}`);
          return caches.delete(name);
        }
      })
    );
  }

  // Cache nhiều URLs cùng lúc
  async cacheUrls(urls: string[]): Promise<void> {
    const cache = await caches.open(this.cacheName);
    await cache.addAll(urls); // Tự động fetch và cache
    console.log(`✅ Cached ${urls.length} URLs`);
  }
}

// Sử dụng Cache Manager
const cacheManager = new CacheManager();

// Fetch với cache fallback
async function fetchWithCache(url: string): Promise<any> {
  try {
    // 1. Kiểm tra cache trước
    const cachedResponse = await cacheManager.getCachedResponse(url);

    if (cachedResponse) {
      return await cachedResponse.json();
    }

    // 2. Cache miss → Fetch từ network
    const response = await fetch(url);

    // 3. Lưu vào cache cho lần sau
    await cacheManager.cacheResponse(url, response);

    return await response.json();
  } catch (error) {
    console.error('❌ Fetch error:', error);
    throw error;
  }
}

**📋 PHÂN TÍCH CHI TIẾT: Browser Cache HTML, CSS, JS, Images**

**🎯 Cơ Chế Cache Của Browser:**

Browser cache dựa vào **HTTP Headers** từ server để quyết định:
- **Có cache không?** → `Cache-Control`, `Expires`
- **Cache bao lâu?** → `max-age`
- **Khi nào cần revalidate?** → `ETag`, `Last-Modified`

**📁 Cache Theo Từng Loại File:**

```
┌─────────────────────────────────────────────────────────────────┐
│  FILE TYPE    CACHE STRATEGY           KHI NÀO REQUEST MỚI      │
├─────────────────────────────────────────────────────────────────┤
│  HTML         Cache-Control: no-cache  Mỗi lần load page        │
│  index.html   → Luôn hỏi server        (có thể trả 304)         │
│               → Server trả 304 nếu     Browser dùng cache        │
│                  không đổi             nếu server trả 304        │
│                                                                  │
│  CSS/JS       max-age=31536000         Khi URL/hash thay đổi    │
│  app.[hash]   immutable                app.abc123.css →         │
│  .css/.js     → Cache 1 năm            app.xyz789.css           │
│               → KHÔNG bao giờ          (URL mới = request mới)  │
│                 request lại                                     │
│                 nếu hash không đổi                              │
│                                                                  │
│  Images       max-age=604800           - Sau 7 ngày             │
│  logo.png     → Cache 7 ngày           - Hard refresh           │
│               → Browser tự động        - Clear cache            │
│                 request lại sau        - URL thêm query:        │
│                 7 ngày                   logo.png?v=2           │
│                                                                  │
│  API Data     max-age=300              - Sau 5 phút             │
│  /api/users   must-revalidate          - ETag thay đổi          │
│               → Recheck mỗi 5 phút     - Manual refresh         │
└─────────────────────────────────────────────────────────────────┘
```

**🔍 Khi Nào Browser REQUEST TÀI NGUYÊN MỚI (Không Dùng Cache)?**

**1. Cache Headers Yêu Cầu:**
```http
Cache-Control: no-cache  → Phải hỏi server (có thể dùng cache nếu server trả 304)
Cache-Control: no-store  → KHÔNG bao giờ cache, luôn request mới
Cache-Control: max-age=0 → Cache hết hạn ngay, phải revalidate
```

**2. Cache Hết Hạn:**
```javascript
// max-age hết hạn
Response headers: Cache-Control: max-age=3600 (1 giờ)
→ Sau 1 giờ, browser request lại

// Expires hết hạn
Response headers: Expires: Thu, 01 Jan 2024 00:00:00 GMT
→ Sau thời điểm này, browser request lại
```

**3. User Action:**
```
- Hard Refresh (Cmd+Shift+R / Ctrl+F5)
  → Bỏ qua TẤT CẢ cache, request lại tất cả
  → Gửi header: Cache-Control: no-cache

- Normal Refresh (F5)
  → HTML request lại (vì no-cache)
  → CSS/JS/Images: dùng cache nếu chưa hết max-age

- Clear Browser Cache
  → Xóa hết cache
  → Lần load tiếp theo request lại tất cả
```

**4. URL Thay Đổi:**
```html
<!-- Deploy cũ -->
<link href="/static/app.abc123.css">

<!-- Deploy mới → Hash khác -->
<link href="/static/app.xyz789.css">

→ Browser thấy URL mới → Request file mới
→ app.abc123.css vẫn trong cache nhưng không dùng nữa
```

**5. Conditional Request với ETag:**
```http
# Lần 1: Browser request
GET /api/users
Response:
  ETag: "abc123"
  Cache-Control: max-age=300

# Lần 2: Sau 5 phút (max-age hết)
GET /api/users
Request headers: If-None-Match: "abc123"

→ Server check:
  - Data không đổi → 304 Not Modified (browser dùng cache)
  - Data đã đổi → 200 OK với data mới + ETag mới
```

**❓ BROWSER CÓ CHECK BUNDLE HASH KHÔNG?**

**TL;DR: KHÔNG! Browser KHÔNG verify hash trong filename.**

**Chi tiết:**

1. **Hash chỉ là convention, không phải browser feature:**
```javascript
// ❌ Browser KHÔNG làm việc này
const filename = 'app.abc123.js';
const hash = extractHash(filename); // ← KHÔNG tồn tại
const content = downloadFile(filename);
if (hashContent(content) !== hash) {
  throw new Error('Mismatch'); // ← Không bao giờ xảy ra
}

// ✅ Browser chỉ làm việc này
const cachedURL = 'app.abc123.js';
const newURL = 'app.xyz789.js';

if (cachedURL === newURL) {
  useCachedFile(); // Dùng cache
} else {
  downloadNewFile(); // URL khác → Download mới
}
```

2. **Browser cache dựa vào URL string comparison:**
```
Cache key = Full URL
- https://example.com/app.abc123.js → Cache entry 1
- https://example.com/app.xyz789.js → Cache entry 2

Browser KHÔNG extract hash 'abc123' hoặc 'xyz789'
Browser CHỈ so sánh URL as string
```

3. **Hash được dùng NHƯ THẾ NÀO? (HASH BUNDLE Ở ĐÂU TRONG URL?)**

**Hash bundle = Content hash được nhúng vào TÊN FILE trong URL:**

```javascript
// ❌ SAI LẦM THƯỜNG GẶP: Nghĩ hash ở query string
https://example.com/app.js?v=abc123  // ← Đây KHÔNG phải hash bundle
                         ↑
                    Query param (có thể thay đổi thủ công)

// ✅ ĐÚNG: Hash bundle nhúng TRONG TÊN FILE
https://example.com/static/app.abc123.js
                              ↑↑↑↑↑↑
                         Hash của file content
                         
https://example.com/static/css/main.8f7d6e2a.css
                                   ↑↑↑↑↑↑↑↑
                              Hash của CSS content

https://example.com/static/js/vendors.chunk.3a4b5c.js
                                          ↑↑↑↑↑↑
                                    Hash của chunk vendors
```

**Cụ thể hơn - VÍ DỤ THỰC TẾ:**

**Build lần 1:**
```bash
# Build tool (Webpack/Vite) tạo files:
dist/
  index.html
  static/
    js/
      main.abc123def.js      ← Hash của main bundle
      vendors.456789.js      ← Hash của vendors chunk
    css/
      styles.fedcba987.css   ← Hash của CSS
    
# index.html reference:
<script src="/static/js/main.abc123def.js"></script>
<link href="/static/css/styles.fedcba987.css">
```

**Build lần 2 (sau khi sửa code):**
```bash
# Chỉ sửa file main.tsx → Chỉ hash của main thay đổi
dist/
  index.html
  static/
    js/
      main.xyz789abc.js      ← Hash MỚI (content thay đổi)
      vendors.456789.js      ← Hash GIỮ NGUYÊN (không sửa)
    css/
      styles.fedcba987.css   ← Hash GIỮ NGUYÊN (không sửa)

# index.html mới:
<script src="/static/js/main.xyz789abc.js"></script>
           ↑ URL mới vì hash khác ↑
<link href="/static/css/styles.fedcba987.css">
     ↑ URL giữ nguyên vì hash không đổi ↑
```

**SO SÁNH URL CŨ vs MỚI:**

```
┌─────────────────────────────────────────────────────────────────┐
│  FILE          URL CŨ                    URL MỚI                │
├─────────────────────────────────────────────────────────────────┤
│  Main JS       /static/js/               /static/js/            │
│                main.abc123def.js         main.xyz789abc.js      │
│                     ↑↑↑↑↑↑                    ↑↑↑↑↑↑            │
│                   Hash cũ                  Hash mới             │
│                                                                 │
│  Vendors       /static/js/               /static/js/            │
│                vendors.456789.js         vendors.456789.js      │
│                       ↑↑↑↑↑↑                    ↑↑↑↑↑↑           │
│                     Giữ nguyên (không sửa code)                 │
│                                                                 │
│  CSS           /static/css/              /static/css/           │
│                styles.fedcba987.css      styles.fedcba987.css   │
│                       ↑↑↑↑↑↑↑↑                  ↑↑↑↑↑↑↑↑         │
│                     Giữ nguyên (không sửa CSS)                  │
└─────────────────────────────────────────────────────────────────┘
```

**QUY TRÌNH BUILD TOOL TẠO HASH:**

```typescript
// Webpack/Vite config
export default {
  output: {
    filename: '[name].[contenthash].js',
    //               ↑↑↑↑↑↑↑↑↑↑↑↑
    //         Placeholder cho content hash
    
    chunkFilename: '[name].[contenthash].chunk.js',
  },
  
  css: {
    filename: '[name].[contenthash].css'
  }
}

// Build process:
1. Đọc file content:   "const App = () => { return <div>Hello</div> }"
2. Hash content:       MD5/SHA256 → "abc123def456"
3. Tạo filename:       "main.abc123def456.js"
4. Ghi file ra disk:   dist/static/js/main.abc123def456.js
5. Update HTML:        <script src="/static/js/main.abc123def456.js">
```

**BROWSER XỬ LÝ NHƯ THẾ NÀO:**

```javascript
// Browser KHÔNG biết "abc123" là hash
// Browser CHỈ coi đây là tên file bình thường

// Bước 1: Parse HTML
<script src="/static/js/main.abc123def.js"></script>

// Bước 2: Chuẩn bị request
const url = "https://example.com/static/js/main.abc123def.js";
                                           ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
                                    Browser coi đây là tên file hoàn chỉnh

// Bước 3: Check cache
const cacheKey = url; // Full URL làm key
if (cache.has(cacheKey)) {
  // Có cache → Dùng cache
} else {
  // Không có → Request server
  fetch(url);
}

// Bước 4: Khi deploy mới, HTML có URL mới
<script src="/static/js/main.xyz789abc.js"></script>
                                ↑↑↑↑↑↑↑↑↑
                            Hash khác = URL khác

const newUrl = "https://example.com/static/js/main.xyz789abc.js";

// Browser check cache:
cache.has(newUrl) // → false (vì URL chưa từng thấy)
// → Request file mới từ server
```

Build tool (Webpack/Vite/Rollup):
1. Hash file content → 'abc123'
2. Tạo file: app.abc123.js  ← Hash ở đây
             ↑↑↑ ↑↑↑↑↑↑
           Tên  Hash nhúng trong tên file
3. Update HTML: <script src="app.abc123.js">

Content thay đổi:
1. Hash mới → 'xyz789'
2. File mới: app.xyz789.js  ← Hash mới ở đây
3. HTML mới: <script src="app.xyz789.js">
                          ↑↑↑↑↑↑
                    URL thay đổi vì hash khác

Browser:
→ URL mới (app.xyz789.js ≠ app.abc123.js)
→ File mới → Request mới
→ Bypass cache TẰT NHIÊN ✅
```

4. **Tại sao không cần verify hash?**
```
✅ Build tool đảm bảo hash chính xác
✅ HTTPS đảm bảo file không bị tamper
✅ URL khác = File khác (theo browser)
✅ Cache busting tự động

❌ Browser verify hash = Không cần thiết
❌ Browser verify hash = Tốn performance
❌ Browser verify hash = KHÔNG phải trách nhiệm của browser
```

**🎯 Flow Hoàn Chỉnh - Deploy Mới:**

```
┌──────────────────────────────────────────────────────────────┐
│  STEP 1: User visit lần đầu                                  │
├──────────────────────────────────────────────────────────────┤
│  GET /index.html                                             │
│  → Response: Cache-Control: no-cache                         │
│  → Body: <link href="app.abc123.css">                        │
│                                                              │
│  GET /app.abc123.css                                         │
│  → Response: Cache-Control: max-age=31536000, immutable      │
│  → Browser cache CSS (1 năm)                                 │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│  STEP 2: Developer deploy version mới                        │
├──────────────────────────────────────────────────────────────┤
│  Build tool → CSS content thay đổi                           │
│  → Hash mới: xyz789                                          │
│  → File mới: app.xyz789.css                                  │
│  → HTML mới: <link href="app.xyz789.css">                    │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│  STEP 3: User reload (F5)                                    │
├──────────────────────────────────────────────────────────────┤
│  GET /index.html                                             │
│  → no-cache → Phải hỏi server                                │
│  → Response: HTML mới với app.xyz789.css                     │
│                                                              │
│  Browser parse HTML → Thấy app.xyz789.css                    │
│  → Check cache: KHÔNG có app.xyz789.css                      │
│  → GET /app.xyz789.css (request mới)                         │
│  → Cache CSS mới                                             │
│                                                              │
│  ✅ app.abc123.css vẫn trong cache nhưng không dùng          │
└──────────────────────────────────────────────────────────────┘
```

**💡 Best Practices:**

```typescript
// 1. HTML: Luôn no-cache
app.get('*.html', (req, res) => {
  res.setHeader('Cache-Control', 'no-cache, no-store, must-revalidate');
  res.sendFile(/* ... */);
});

// 2. Static assets với hash: Cache dài hạn
app.use('/static', express.static('public', {
  maxAge: '365d',
  immutable: true,
  setHeaders: (res) => {
    res.setHeader('Cache-Control', 'public, max-age=31536000, immutable');
  }
}));

// 3. Images: Cache trung bình
app.use('/images', (req, res, next) => {
  res.setHeader('Cache-Control', 'public, max-age=604800'); // 7 days
  next();
});

// 4. API: Short cache + revalidate
app.get('/api/*', (req, res) => {
  res.setHeader('Cache-Control', 'public, max-age=300, must-revalidate');
  res.setHeader('ETag', generateETag(data));
  // ...
});
```

**✅ TÓM TẮT:**

| Câu hỏi | Trả lời |
|---------|---------|
| Browser cache HTML/CSS/JS/Images thế nào? | Dựa vào Cache-Control, max-age, ETag từ server |
| Khi nào browser request tài nguyên mới? | 1. Cache hết hạn<br>2. no-cache/no-store<br>3. Hard refresh<br>4. URL thay đổi<br>5. ETag không khớp |
| Browser có check bundle hash không? | **KHÔNG**. Chỉ so sánh URL string.<br>Hash để tạo URL mới → Force download |
| Hash trong filename để làm gì? | Cache busting: Content đổi → Hash đổi → URL đổi → Browser download mới |


