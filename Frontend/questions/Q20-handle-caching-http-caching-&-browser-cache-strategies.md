# 💾 Q20: Handle Caching - HTTP Caching & Browser Cache Strategies

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"HTTP caching = giảm yêu cầu server bằng Cache-Control, ETag. Service Worker = hỗ trợ offline.**

**📦 Loại Cache & Phân Cấp:**
1. **Memory Cache**: Trong bộ nhớ RAM → nhanh nhất, xóa khi đóng tab.
2. **Disk Cache**: Trên ổ đĩa → duy trì qua các phiên.
3. **Service Worker Cache**: API cache theo chương trình → hỗ trợ offline, chiến lược tùy chỉnh.
4. **HTTP Cache**: Cache trình duyệt theo Cache-Control headers.
5. **CDN Cache**: Servers biên cache tài nguyên tĩnh toàn cầu.

**🔑 HTTP Cache Headers (Bắt Buộc Biết):**

| Header | Mục Đích | Ví Dụ |
|--------|----------|--------|
| **Cache-Control** | Chỉ thị cache chính | `max-age=3600, public` |
| **ETag** | Token xác thực | `"abc123"` (hash phiên bản) |
| **Last-Modified** | Thời gian cập nhật cuối | `Thu, 01 Jan 2024 00:00:00 GMT` |
| **Expires** | Ngày hết hạn (cũ) | `Thu, 01 Jan 2025 00:00:00 GMT` |
| **Vary** | Thay đổi cache theo header | `Vary: Accept-Encoding` |

**🔧 Chỉ Thị Cache-Control:**
- **`max-age=3600`**: Cache 1 giờ (3600 giây).
- **`public`**: Cache được bởi trình duyệt + CDN.
- **`private`**: Chỉ cache bởi trình duyệt (không CDN) → dữ liệu cá nhân.
- **`no-cache`**: Phải xác thực lại với server (304 Not Modified nếu không thay đổi).
- **`no-store`**: Không cache (dữ liệu nhạy cảm: mật khẩu, thẻ tín dụng).
- **`immutable`**: Tài nguyên không bao giờ thay đổi → không xác thực lại (tài nguyên tĩnh có hash).

**♻️ Chiến Lược Cache (Service Worker):**

1. **Cache First (Tài nguyên tĩnh)**:
   - Kiểm tra cache → nếu có trả về → nếu không lấy từ mạng.
   - ✅ Dùng cho: Fonts, hình ảnh, CSS, JS có tên file phiên bản.

2. **Network First (Dữ liệu động)**:
   - Lấy từ mạng → nếu thất bại trả về cache.
   - ✅ Dùng cho: Dữ liệu API, nội dung người dùng.

3. **Stale While Revalidate**:
   - Trả về cache ngay (nhanh) + lấy mạng background → cập nhật cache.
   - ✅ Dùng cho: Cân bằng tốc độ + độ mới (nguồn tin, mạng xã hội).

4. **Network Only**:
   - Luôn lấy từ mạng → không cache.
   - ✅ Dùng cho: Phân tích, dữ liệu thời gian thực.

5. **Cache Only**:
   - Chỉ dùng cache → ưu tiên offline.
   - ✅ Dùng cho: Vỏ ứng dụng PWA.

**🔍 ETag & Conditional Requests:**
- **ETag**: Hash của resource content → version identifier.
- **Flow**:
  1. Server response: `ETag: "abc123"`.
  2. Browser cache + store ETag.
  3. Next request: `If-None-Match: "abc123"`.
  4. Server check: Unchanged → `304 Not Modified` (no body) | Changed → `200 OK` (new content + new ETag).
- **Benefit**: Save bandwidth (304 response nhỏ hơn full response).

**⚠️ Common Pitfalls:**
- **Cache Busting**: Static assets thay đổi nhưng cùng filename → browser serve stale cache.
  - **Solution**: Hash trong filename (`app.abc123.js`) hoặc query param (`app.js?v=123`).
- **Over-caching**: Cache sensitive data (passwords) → security risk. Dùng `no-store`.
- **Under-caching**: Không cache static assets → waste bandwidth, slow load.
- **CDN cache**: Purge CDN cache khi deploy new version.

**💡 Senior Insights:**
- **Versioning Strategy**: Dùng content hash cho static assets (`webpack`/`vite` auto generate).
- **Immutable Resources**: Set `Cache-Control: max-age=31536000, immutable` cho versioned assets → never revalidate.
- **Service Worker**: Combine strategies (cache shell với Cache First, API với Network First).
- **Performance**: Cache reduce TTFB (Time To First Byte), improve Core Web Vitals (LCP, FCP).
- **DevTools**: Chrome DevTools → Network tab → check cache status (from disk cache, from memory cache).
- **Cache-Control vs Expires**: `Cache-Control` modern, `Expires` legacy. Nếu both, `Cache-Control` wins.

**🚀 Best Practices:**
1. **Static assets**: Long max-age (1 year) + immutable + hash filenames.
2. **HTML**: `no-cache` → always revalidate (ETag/Last-Modified).
3. **API**: Short max-age (5 minutes) hoặc `no-cache` + ETag.
4. **User-specific data**: `private` (not `public`).
5. **Sensitive data**: `no-store`.

---

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

---

## **📋 PHÂN TÍCH CHI TIẾT: Browser Cache HTML, CSS, JS, Images**

### **🎯 Cơ Chế Cache Của Browser**

Browser cache hoạt động dựa trên **3 yếu tố chính**:

```typescript
/**
 * 🔍 CƠ CHẾ QUYẾT ĐỊNH CACHE CỦA BROWSER
 * 
 * Browser quyết định cache NHƯ THẾ NÀO?
 * 
 * 1️⃣ URL (Cache Key)
 *    - Mỗi URL = 1 cache entry riêng
 *    - app.abc123.js ≠ app.xyz789.js → 2 entries khác nhau
 *    - Query string khác = Cache entry khác:
 *      /api/users?page=1 ≠ /api/users?page=2
 * 
 * 2️⃣ HTTP Response Headers (Cache Rules)
 *    - Cache-Control: Có cache không? Cache bao lâu?
 *    - Expires: Thời điểm cache hết hạn (legacy)
 *    - ETag: Version token để validate cache
 *    - Last-Modified: Timestamp lần cuối sửa
 * 
 * 3️⃣ Request Context (Ai request?)
 *    - Normal navigation (click link)
 *    - Reload (F5)
 *    - Hard reload (Cmd+Shift+R)
 *    - Programmatic fetch()
 */

// ============================================
// CƠ CHẾ CACHE - STEP BY STEP
// ============================================

/**
 * BƯỚC 1: Browser nhận request (từ HTML, JS, hoặc user)
 */
function browserRequest(url: string, context: 'navigation' | 'reload' | 'hard-reload') {
  const cacheKey = url; // URL = Cache key
  
  /**
   * BƯỚC 2: Tìm trong cache storage
   */
  const cachedEntry = diskCache.get(cacheKey);
  
  if (!cachedEntry) {
    // Cache miss → Request từ server
    return fetchFromServer(url);
  }
  
  /**
   * BƯỚC 3: Kiểm tra cache headers
   */
  const headers = cachedEntry.headers;
  const cacheControl = headers['cache-control'];
  const expires = headers['expires'];
  const etag = headers['etag'];
  
  /**
   * BƯỚC 4: Áp dụng cache logic
   */
  
  // 4.1. no-store → KHÔNG bao giờ dùng cache
  if (cacheControl.includes('no-store')) {
    return fetchFromServer(url);
  }
  
  // 4.2. Hard reload → Bỏ qua cache
  if (context === 'hard-reload') {
    return fetchFromServer(url, { 
      headers: { 'Cache-Control': 'no-cache' } 
    });
  }
  
  // 4.3. no-cache → Phải validate với server
  if (cacheControl.includes('no-cache')) {
    return revalidateWithServer(url, etag);
    // → Server trả 304 → Dùng cache
    // → Server trả 200 → Dùng response mới
  }
  
  // 4.4. Kiểm tra max-age (freshness)
  const maxAge = extractMaxAge(cacheControl); // VD: 3600 giây
  const cacheAge = Date.now() - cachedEntry.timestamp;
  
  if (cacheAge < maxAge * 1000) {
    // Cache còn fresh → Dùng cache TRỰC TIẾP
    console.log('✅ Cache hit (fresh)');
    return cachedEntry.response;
  }
  
  // 4.5. Cache stale (hết hạn)
  if (cacheControl.includes('must-revalidate')) {
    // Phải validate với server
    return revalidateWithServer(url, etag);
  }
  
  // 4.6. Cache hết hạn nhưng không bắt buộc revalidate
  // → Dùng stale cache (tuỳ browser implementation)
  return cachedEntry.response;
}

/**
 * REVALIDATION với ETag
 */
async function revalidateWithServer(url: string, etag?: string) {
  const headers: Record<string, string> = {};
  
  if (etag) {
    headers['If-None-Match'] = etag; // Gửi ETag để so sánh
  }
  
  const response = await fetch(url, { headers });
  
  if (response.status === 304) {
    // 304 Not Modified → Dùng cached response
    console.log('✅ Cache revalidated (304)');
    return diskCache.get(url).response;
  }
  
  // 200 OK → Response mới, update cache
  console.log('📥 New response (200)');
  diskCache.set(url, { response, timestamp: Date.now() });
  return response;
}
```

---

### **📁 Browser Cache Từng Loại File - CHI TIẾT**

```typescript
/**
 * ┌─────────────────────────────────────────────────────────────────────────┐
 * │                    BROWSER CACHE THEO LOẠI FILE                          │
 * ├─────────────────────────────────────────────────────────────────────────┤
 * │                                                                          │
 * │  1️⃣  HTML FILES (index.html, app.html, ...)                            │
 * │  ═══════════════════════════════════════════════════════════════        │
 * │                                                                          │
 * │  📌 Cache Strategy: NO CACHE (luôn check mới nhất)                      │
 * │  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                     │
 * │                                                                          │
 * │  Server response headers:                                               │
 * │  ┌─────────────────────────────────────────────────┐                    │
 * │  │ Cache-Control: no-cache, no-store, must-revalidate                   │
 * │  │ Pragma: no-cache                                │                    │
 * │  │ Expires: 0                                      │                    │
 * │  └─────────────────────────────────────────────────┘                    │
 * │                                                                          │
 * │  🔄 Khi nào browser REQUEST MỚI?                                         │
 * │  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                       │
 * │  ✅ Mỗi lần navigate (click link, gõ URL, back/forward)                 │
 * │  ✅ Mỗi lần reload (F5)                                                  │
 * │  ✅ Mỗi lần hard reload (Cmd+Shift+R)                                    │
 * │  ✅ Programmatic: location.href = '/', router.push('/')                 │
 * │                                                                          │
 * │  🎯 TẠI SAO luôn no-cache?                                               │
 * │  ━━━━━━━━━━━━━━━━━━━━━━━━━                                              │
 * │  → HTML chứa references đến CSS/JS bundle                               │
 * │  → Deploy mới → HTML mới có hash mới trong <script src>                │
 * │  → Nếu cache HTML → User không nhận được bundle mới!                    │
 * │                                                                          │
 * │  📊 Flow:                                                                │
 * │  ┌──────────────────────────────────────────────────┐                   │
 * │  │ User visit /                                     │                   │
 * │  │ ↓                                                │                   │
 * │  │ Browser: GET /index.html                         │                   │
 * │  │ → Headers: Cache-Control: no-cache               │                   │
 * │  │ ↓                                                │                   │
 * │  │ Server: 200 OK                                   │                   │
 * │  │ <html>                                           │                   │
 * │  │   <script src="/app.abc123.js"></script>         │                   │
 * │  │ </html>                                          │                   │
 * │  │ ↓                                                │                   │
 * │  │ Browser parse HTML → Request app.abc123.js       │                   │
 * │  └──────────────────────────────────────────────────┘                   │
 * │                                                                          │
 * │  ⚠️ LƯU Ý: Tuy "no-cache" nhưng browser VẪN có thể cache HTML           │
 * │  → Mỗi lần dùng PHẢI hỏi server (revalidate)                            │
 * │  → Server trả 304 Not Modified → Dùng cached HTML                       │
 * │                                                                          │
 * ├─────────────────────────────────────────────────────────────────────────┤
 * │                                                                          │
 * │  2️⃣  CSS/JS BUNDLES (app.[hash].js, main.[hash].css)                   │
 * │  ═══════════════════════════════════════════════════════════════        │
 * │                                                                          │
 * │  📌 Cache Strategy: LONG-TERM IMMUTABLE CACHE (1 năm)                   │
 * │  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                     │
 * │                                                                          │
 * │  Server response headers:                                               │
 * │  ┌─────────────────────────────────────────────────┐                    │
 * │  │ Cache-Control: public, max-age=31536000, immutable                   │
 * │  │                        ↑↑↑↑↑↑↑↑   ↑↑↑↑↑↑↑↑↑     │                    │
 * │  │                       31536000 = 1 năm          │                    │
 * │  │                       immutable = không đổi     │                    │
 * │  └─────────────────────────────────────────────────┘                    │
 * │                                                                          │
 * │  🔄 Khi nào browser REQUEST MỚI?                                         │
 * │  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                       │
 * │  ✅ URL thay đổi (hash khác):                                            │
 * │     app.abc123.js → app.xyz789.js                                       │
 * │     ↑ URL cũ       ↑ URL mới (browser thấy là file khác!)               │
 * │                                                                          │
 * │  ❌ KHÔNG request mới nếu:                                               │
 * │  ❌ Normal reload (F5) → Vẫn dùng cache (chưa hết 1 năm)                │
 * │  ❌ Navigate trong SPA → Vẫn dùng cache                                 │
 * │  ❌ Back/Forward → Vẫn dùng cache                                        │
 * │                                                                          │
 * │  ⚠️ CHỈ request mới khi:                                                 │
 * │  1. Hard reload (Cmd+Shift+R / Ctrl+F5)                                 │
 * │  2. Clear browser cache                                                 │
 * │  3. URL thay đổi (hash mới)                                             │
 * │                                                                          │
 * │  🎯 CACHE BUSTING với Content Hash:                                     │
 * │  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                        │
 * │  Build lần 1:                                                           │
 * │  ┌────────────────────────────────────────┐                             │
 * │  │ File: src/App.tsx                      │                             │
 * │  │ Content: "const App = () => <div>Hello</div>"                        │
 * │  │ ↓ Build tool hash content              │                             │
 * │  │ Hash: abc123def456                     │                             │
 * │  │ ↓ Generate filename                    │                             │
 * │  │ Output: app.abc123def456.js            │                             │
 * │  │ ↓ Update HTML                          │                             │
 * │  │ <script src="/app.abc123def456.js">    │                             │
 * │  └────────────────────────────────────────┘                             │
 * │                                                                          │
 * │  Build lần 2 (sửa code):                                                │
 * │  ┌────────────────────────────────────────┐                             │
 * │  │ File: src/App.tsx                      │                             │
 * │  │ Content: "const App = () => <div>Hi</div>"  ← Sửa "Hello" → "Hi"    │
 * │  │ ↓ Hash KHÁC vì content khác            │                             │
 * │  │ Hash: xyz789abc123                     │                             │
 * │  │ ↓ Filename MỚI                         │                             │
 * │  │ Output: app.xyz789abc123.js            │                             │
 * │  │ ↓ HTML MỚI                             │                             │
 * │  │ <script src="/app.xyz789abc123.js">    │                             │
 * │  └────────────────────────────────────────┘                             │
 * │                                                                          │
 * │  📊 User reload sau deploy:                                             │
 * │  ┌──────────────────────────────────────────────────┐                   │
 * │  │ 1. Browser request: GET /index.html              │                   │
 * │  │    → no-cache → Phải hỏi server                  │                   │
 * │  │    → Server trả HTML mới                         │                   │
 * │  │                                                  │                   │
 * │  │ 2. Browser parse HTML mới:                       │                   │
 * │  │    <script src="/app.xyz789abc123.js">           │                   │
 * │  │                    ↑↑↑↑↑↑↑↑↑↑↑↑                  │                   │
 * │  │                  URL mới! (hash khác)            │                   │
 * │  │                                                  │                   │
 * │  │ 3. Browser check cache:                          │                   │
 * │  │    cacheKey = "https://example.com/app.xyz789abc123.js"              │
 * │  │    cache.has(cacheKey) → FALSE ❌                │                   │
 * │  │    (Chưa từng request URL này)                   │                   │
 * │  │                                                  │                   │
 * │  │ 4. Browser request: GET /app.xyz789abc123.js     │                   │
 * │  │    → Download file mới                           │                   │
 * │  │    → Cache với max-age=31536000                  │                   │
 * │  └──────────────────────────────────────────────────┘                   │
 * │                                                                          │
 * │  ✅ File cũ (app.abc123def456.js) VẪN trong cache nhưng KHÔNG dùng!     │
 * │  → Sẽ bị xóa khi browser cleanup cache (LRU eviction)                   │
 * │                                                                          │
 * ├─────────────────────────────────────────────────────────────────────────┤
 * │                                                                          │
 * │  3️⃣  IMAGES (logo.png, banner.jpg, icon.svg, ...)                      │
 * │  ═══════════════════════════════════════════════════════════════        │
 * │                                                                          │
 * │  📌 Cache Strategy: MEDIUM-TERM CACHE (7-30 ngày)                       │
 * │  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                            │
 * │                                                                          │
 * │  Server response headers:                                               │
 * │  ┌─────────────────────────────────────────────────┐                    │
 * │  │ Cache-Control: public, max-age=604800           │                    │
 * │  │                               ↑↑↑↑↑↑            │                    │
 * │  │                          604800 = 7 ngày        │                    │
 * │  │ Vary: Accept                                    │                    │
 * │  │       ↑↑↑↑↑↑                                    │                    │
 * │  │   Cache riêng cho WebP/JPEG/PNG                 │                    │
 * │  └─────────────────────────────────────────────────┘                    │
 * │                                                                          │
 * │  🔄 Khi nào browser REQUEST MỚI?                                         │
 * │  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                       │
 * │  ✅ Sau 7 ngày (max-age hết hạn)                                         │
 * │  ✅ Hard reload (Cmd+Shift+R)                                            │
 * │  ✅ Clear browser cache                                                 │
 * │  ✅ URL thay đổi: logo.png?v=2                                           │
 * │                   ↑↑↑↑↑↑↑↑                                              │
 * │              Query string khác = URL khác                               │
 * │                                                                          │
 * │  ❌ KHÔNG request mới nếu:                                               │
 * │  ❌ Normal reload (F5) → Dùng cache (chưa hết 7 ngày)                   │
 * │  ❌ Navigate → Dùng cache                                               │
 * │                                                                          │
 * │  🎯 Cache Busting cho Images:                                           │
 * │  ━━━━━━━━━━━━━━━━━━━━━━━━━━━                                            │
 * │  Option 1: Query string versioning                                      │
 * │  <img src="/images/logo.png?v=1.0.0">                                   │
 * │  → Update mới: ?v=1.0.1                                                 │
 * │  → URL khác → Browser request mới                                       │
 * │                                                                          │
 * │  Option 2: Filename hash (giống JS/CSS)                                 │
 * │  <img src="/images/logo.abc123.png">                                    │
 * │  → Build tool hash file content                                         │
 * │  → File đổi → Hash đổi → URL đổi                                        │
 * │                                                                          │
 * │  Option 3: Directory versioning                                         │
 * │  <img src="/v1/images/logo.png">                                        │
 * │  → Deploy mới: /v2/images/logo.png                                      │
 * │                                                                          │
 * ├─────────────────────────────────────────────────────────────────────────┤
 * │                                                                          │
 * │  4️⃣  API RESPONSES (/api/users, /api/products, ...)                    │
 * │  ═══════════════════════════════════════════════════════════════        │
 * │                                                                          │
 * │  📌 Cache Strategy: SHORT-TERM + REVALIDATE (30s - 5 phút)              │
 * │  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                    │
 * │                                                                          │
 * │  Server response headers:                                               │
 * │  ┌─────────────────────────────────────────────────┐                    │
 * │  │ Cache-Control: public, max-age=300, must-revalidate                  │
 * │  │                               ↑↑↑   ↑↑↑↑↑↑↑↑↑↑↑↑↑│                    │
 * │  │                             300s   Phải check    │                    │
 * │  │                             (5m)   với server    │                    │
 * │  │ ETag: "abc123def456"                            │                    │
 * │  │ Vary: Accept, Accept-Encoding                   │                    │
 * │  └─────────────────────────────────────────────────┘                    │
 * │                                                                          │
 * │  🔄 Khi nào browser REQUEST MỚI?                                         │
 * │  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                       │
 * │  ✅ Sau 5 phút (max-age hết)                                             │
 * │  ✅ ETag thay đổi (data thay đổi)                                        │
 * │  ✅ Hard reload                                                         │
 * │  ✅ Query params khác: /api/users?page=2                                │
 * │                                                                          │
 * │  📊 Revalidation Flow với ETag:                                         │
 * │  ┌──────────────────────────────────────────────────┐                   │
 * │  │ Lần 1: Request đầu tiên                          │                   │
 * │  │ ━━━━━━━━━━━━━━━━━━━━━━━━                         │                   │
 * │  │ GET /api/users                                   │                   │
 * │  │ → Server: 200 OK                                 │                   │
 * │  │   Headers:                                       │                   │
 * │  │     Cache-Control: max-age=300                   │                   │
 * │  │     ETag: "abc123"                               │                   │
 * │  │   Body: [{ id: 1, name: "John" }]                │                   │
 * │  │ → Browser cache response + ETag                  │                   │
 * │  │                                                  │                   │
 * │  │ Lần 2: Sau 2 phút (chưa hết max-age)             │                   │
 * │  │ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                 │                   │
 * │  │ GET /api/users                                   │                   │
 * │  │ → Browser: ✅ Dùng cache (fresh)                 │                   │
 * │  │ → KHÔNG request server!                          │                   │
 * │  │                                                  │                   │
 * │  │ Lần 3: Sau 6 phút (hết max-age)                  │                   │
 * │  │ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                    │                   │
 * │  │ GET /api/users                                   │                   │
 * │  │ → must-revalidate → Phải hỏi server              │                   │
 * │  │ → Headers: If-None-Match: "abc123"               │                   │
 * │  │                                                  │                   │
 * │  │ → Server check: ETag vẫn "abc123" (không đổi)    │                   │
 * │  │ → Server: 304 Not Modified (no body)             │                   │
 * │  │ → Browser: ✅ Dùng cached data                   │                   │
 * │  │                                                  │                   │
 * │  │ Lần 4: Sau deploy mới (data thay đổi)            │                   │
 * │  │ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                │                   │
 * │  │ GET /api/users                                   │                   │
 * │  │ → Headers: If-None-Match: "abc123"               │                   │
 * │  │                                                  │                   │
 * │  │ → Server check: ETag mới "xyz789" (data đổi!)    │                   │
 * │  │ → Server: 200 OK                                 │                   │
 * │  │   Headers: ETag: "xyz789"                        │                   │
 * │  │   Body: [{ id: 1, name: "Jane" }]  ← Data mới!   │                   │
 * │  │ → Browser: Cache response mới với ETag mới       │                   │
 * │  └──────────────────────────────────────────────────┘                   │
 * │                                                                          │
 * └─────────────────────────────────────────────────────────────────────────┘
 */
```

---

### **🔍 Khi Nào Browser Request Tài Nguyên Mới? (Không Dùng Cache)**

```typescript
/**
 * ❓ KHI NÀO BROWSER REQUEST MỚI? (KHÔNG DÙNG CACHE)
 * 
 * ════════════════════════════════════════════════════════════════
 * 
 * 1️⃣  CACHE HEADERS YÊU CẦU
 * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 */

// ❌ no-store: KHÔNG bao giờ cache
// Response headers:
'Cache-Control: no-store'
// → Browser KHÔNG lưu vào disk/memory cache
// → Mỗi request = request mới 100%
// → Use case: Sensitive data (banking, medical records)

// Example:
app.get('/api/sensitive', (req, res) => {
  res.setHeader('Cache-Control', 'no-store, no-cache, must-revalidate, private');
  res.setHeader('Pragma', 'no-cache');
  res.json({ ssn: '123-45-6789' });
});
// → Mỗi fetch() = request server (KHÔNG cache)


// ⚠️ no-cache: Phải revalidate với server
// Response headers:
'Cache-Control: no-cache'
// → Browser CÓ THỂ lưu cache
// → NHƯNG phải hỏi server trước khi dùng
// → Server trả 304 → Dùng cache
// → Server trả 200 → Data mới

// Example:
app.get('/index.html', (req, res) => {
  res.setHeader('Cache-Control', 'no-cache, must-revalidate');
  res.setHeader('ETag', generateETag(htmlContent));
  
  // Check If-None-Match
  if (req.headers['if-none-match'] === currentETag) {
    return res.status(304).end(); // Dùng cache
  }
  
  res.send(htmlContent); // Data mới
});


// 🔄 max-age=0: Cache hết hạn ngay
'Cache-Control: max-age=0, must-revalidate'
// → Browser lưu cache NHƯNG coi như hết hạn ngay
// → Mỗi lần dùng phải revalidate

/**
 * ════════════════════════════════════════════════════════════════
 * 
 * 2️⃣  CACHE HẾT HẠN (max-age expired)
 * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 */

// Timeline example:
const cacheTimeline = {
  '10:00 AM': 'Request đầu tiên',
  headers: 'Cache-Control: max-age=3600', // 1 giờ
  
  '10:30 AM': 'Request lần 2 (sau 30 phút)',
  result: '✅ Dùng cache (còn fresh: 30m < 1h)',
  
  '11:05 AM': 'Request lần 3 (sau 1h5m)',
  result: '❌ Cache hết hạn → Request server',
  reason: '1h5m > max-age (1h)',
};

// Code simulation:
function isCacheFresh(cachedTime: number, maxAge: number): boolean {
  const age = Date.now() - cachedTime;
  return age < maxAge * 1000; // Convert max-age (seconds) to ms
}

// Example usage:
const cachedAt = new Date('2024-01-01 10:00:00').getTime();
const maxAge = 3600; // 1 hour

console.log(isCacheFresh(cachedAt, maxAge)); 
// → true nếu < 1h
// → false nếu > 1h → Browser request mới

/**
 * ════════════════════════════════════════════════════════════════
 * 
 * 3️⃣  USER ACTION (Hành động của user)
 * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 */

const userActions = {
  // 🔄 Hard Refresh (Cmd+Shift+R / Ctrl+F5)
  'Hard Refresh': {
    behavior: 'Bypass TẤT CẢ cache',
    headers: 'Cache-Control: no-cache, Pragma: no-cache',
    result: 'Request lại HTML, CSS, JS, Images, API',
    useCase: 'Developer testing, force reload mới nhất',
  },
  
  // 🔄 Normal Refresh (F5)
  'Normal Refresh': {
    behavior: 'Revalidate HTML, dùng cache cho static assets',
    result: {
      HTML: 'Request mới (vì no-cache)',
      'CSS/JS (với max-age)': 'Dùng cache nếu chưa hết hạn',
      'Images (với max-age)': 'Dùng cache nếu chưa hết hạn',
    },
    useCase: 'User muốn thấy content mới nhất',
  },
  
  // 🗑️ Clear Browser Cache
  'Clear Cache': {
    behavior: 'Xóa TẤT CẢ cache entries',
    result: 'Lần load tiếp = request lại tất cả',
    howTo: {
      Chrome: 'DevTools → Application → Clear storage',
      Firefox: 'Preferences → Privacy → Clear Data',
      Safari: 'Develop → Empty Caches',
    },
  },
  
  // ⬅️ Back/Forward Navigation
  'Back/Forward': {
    behavior: 'Dùng BFCache (Back-Forward Cache)',
    result: 'Restore toàn bộ page từ memory (instant)',
    note: 'KHÔNG request server, thậm chí không check cache headers',
  },
};

/**
 * ════════════════════════════════════════════════════════════════
 * 
 * 4️⃣  URL THAY ĐỔI (Cache key changed)
 * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 */

// Cache key = Full URL (including query string)

// Example 1: Filename hash thay đổi
const deployment = {
  old: '<script src="/static/js/app.abc123.js">',
  new: '<script src="/static/js/app.xyz789.js">',
  //                               ↑↑↑↑↑↑
  //                         Hash khác = URL khác
  
  cacheCheck: {
    oldURL: 'https://example.com/static/js/app.abc123.js',
    newURL: 'https://example.com/static/js/app.xyz789.js',
    comparison: 'oldURL !== newURL',
    result: '❌ Cache miss → Request file mới',
  },
};

// Example 2: Query string thay đổi
const queryStringCache = {
  url1: '/api/users?page=1',
  url2: '/api/users?page=2',
  //                   ↑↑
  //             Query khác = URL khác
  
  cacheKeys: {
    key1: 'GET:https://api.example.com/api/users?page=1',
    key2: 'GET:https://api.example.com/api/users?page=2',
    // → 2 cache entries riêng biệt!
  },
};

// Example 3: Image versioning
const imageVersioning = {
  // Deploy cũ
  old: '<img src="/images/logo.png?v=1.0.0">',
  
  // Deploy mới
  new: '<img src="/images/logo.png?v=1.0.1">',
  //                             ↑↑↑↑↑
  //                      Version khác = URL khác
  
  result: 'Browser thấy URL mới → Request image mới',
};

/**
 * ════════════════════════════════════════════════════════════════
 * 
 * 5️⃣  CONDITIONAL REQUEST với ETag
 * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 */

// ETag workflow (detailed)
async function etagWorkflow() {
  // ━━━ Lần 1: Request đầu tiên ━━━
  const response1 = await fetch('/api/users');
  console.log(response1.headers.get('ETag')); // "abc123"
  
  // Browser cache:
  const cacheEntry = {
    url: '/api/users',
    response: await response1.json(),
    etag: 'abc123',
    cachedAt: Date.now(),
    maxAge: 300, // 5 phút
  };
  
  // ━━━ Lần 2: Sau 6 phút (cache hết hạn) ━━━
  // Browser gửi ETag để check
  const response2 = await fetch('/api/users', {
    headers: {
      'If-None-Match': 'abc123', // ETag từ cache
    },
  });
  
  if (response2.status === 304) {
    // ✅ Server trả 304 Not Modified
    console.log('Data không đổi, dùng cache');
    // Browser dùng cached response
    return cacheEntry.response;
  }
  
  if (response2.status === 200) {
    // ❌ Server trả 200 OK → Data mới
    console.log('Data đã thay đổi, update cache');
    const newETag = response2.headers.get('ETag'); // "xyz789"
    const newData = await response2.json();
    
    // Update cache
    cacheEntry.response = newData;
    cacheEntry.etag = newETag;
    cacheEntry.cachedAt = Date.now();
    
    return newData;
  }
}

// Server-side ETag generation
import crypto from 'crypto';

function generateETag(data: any): string {
  const hash = crypto
    .createHash('md5')
    .update(JSON.stringify(data))
    .digest('hex');
  
  return `"${hash}"`; // ETag format: "abc123"
}

app.get('/api/users', (req, res) => {
  const users = database.getUsers();
  const etag = generateETag(users);
  
  // Check If-None-Match header
  if (req.headers['if-none-match'] === etag) {
    // Data không đổi → 304 (no body, save bandwidth)
    return res.status(304).end();
  }
  
  // Data mới hoặc không có ETag → 200 OK
  res.setHeader('ETag', etag);
  res.setHeader('Cache-Control', 'public, max-age=300, must-revalidate');
  res.json(users);
});

/**
 * ════════════════════════════════════════════════════════════════
 * 
 * 6️⃣  VARY HEADER (Cache riêng theo request headers)
 * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 */

// Vary header tạo cache entries riêng biệt dựa trên request headers

// Example 1: Vary by Accept-Encoding
app.get('/static/app.js', (req, res) => {
  res.setHeader('Vary', 'Accept-Encoding');
  // → Browser cache riêng cho mỗi encoding:
  //   - app.js (gzip)
  //   - app.js (brotli)
  //   - app.js (identity/no compression)
  
  const encoding = req.headers['accept-encoding'];
  if (encoding?.includes('br')) {
    res.sendFile('app.js.br'); // Brotli compressed
  } else if (encoding?.includes('gzip')) {
    res.sendFile('app.js.gz'); // Gzip compressed
  } else {
    res.sendFile('app.js'); // Uncompressed
  }
});

// Example 2: Vary by Accept (WebP vs JPEG)
app.get('/images/photo.jpg', (req, res) => {
  res.setHeader('Vary', 'Accept');
  // → Cache riêng cho mỗi image format:
  //   - photo.jpg (WebP-capable browsers)
  //   - photo.jpg (JPEG-only browsers)
  
  const accept = req.headers['accept'];
  if (accept?.includes('image/webp')) {
    res.sendFile('photo.webp'); // WebP (smaller)
  } else {
    res.sendFile('photo.jpg'); // JPEG (fallback)
  }
});

// Example 3: Vary by User-Agent (Mobile vs Desktop)
app.get('/api/config', (req, res) => {
  res.setHeader('Vary', 'User-Agent');
  
  const isMobile = /Mobile|Android|iPhone/i.test(req.headers['user-agent'] || '');
  
  res.json({
    layout: isMobile ? 'mobile' : 'desktop',
    features: isMobile 
      ? ['touch', 'accelerometer'] 
      : ['mouse', 'keyboard'],
  });
  
  // → Browser cache riêng cho mobile và desktop
});

/**
 * ════════════════════════════════════════════════════════════════
 * 
 * 📊 TÓM TẮT - KHI NÀO REQUEST MỚI?
 * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 */

const requestNewResourceWhen = {
  '1. Cache Headers': [
    'Cache-Control: no-store → KHÔNG cache',
    'Cache-Control: no-cache → Phải revalidate',
    'Cache-Control: max-age=0 → Hết hạn ngay',
  ],
  
  '2. Cache Expired': [
    'max-age hết hạn (VD: 3600s đã qua)',
    'Expires header qua thời điểm',
    'must-revalidate → Bắt buộc check server',
  ],
  
  '3. User Action': [
    'Hard Refresh (Cmd+Shift+R) → Bypass tất cả',
    'Clear Cache → Xóa hết cache',
    'Normal Refresh (F5) → Revalidate HTML',
  ],
  
  '4. URL Changed': [
    'Filename hash: app.abc123.js → app.xyz789.js',
    'Query string: ?page=1 → ?page=2',
    'Version param: ?v=1.0.0 → ?v=1.0.1',
  ],
  
  '5. ETag Mismatch': [
    'If-None-Match: "abc123" → Server check',
    'Server ETag khác → 200 OK (data mới)',
    'Server ETag giống → 304 (dùng cache)',
  ],
  
  '6. Vary Header': [
    'Accept-Encoding khác (gzip vs brotli)',
    'Accept khác (webp vs jpeg)',
    'User-Agent khác (mobile vs desktop)',
  ],
};
```

---

---

### **❓ Browser Có Check Hash Của Bundle Không?**

```typescript
/**
 * ════════════════════════════════════════════════════════════════
 * ❓ BROWSER CÓ VERIFY HASH TRONG FILENAME KHÔNG?
 * ════════════════════════════════════════════════════════════════
 * 
 * 🎯 TL;DR: KHÔNG! Browser KHÔNG extract và verify hash.
 * 
 * Browser chỉ làm:
 * 1. So sánh URL as string (full URL comparison)
 * 2. Check cache headers (max-age, ETag, etc.)
 * 3. Download file nếu URL chưa thấy hoặc cache hết hạn
 * 
 * Hash trong filename CHỈ là convention của build tools!
 */

// ════════════════════════════════════════════════════════════════
// ❌ BROWSER KHÔNG LÀM VIỆC NÀY (Misconception)
// ════════════════════════════════════════════════════════════════

function browserMisconception(url: string) {
  // ❌ Browser KHÔNG extract hash từ filename
  const filename = 'app.abc123def456.js';
  const extractedHash = extractHashFromFilename(filename); 
  //                    ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
  //              Function này KHÔNG tồn tại trong browser!
  
  // ❌ Browser KHÔNG hash file content để verify
  const fileContent = await fetch(url).then(r => r.text());
  const computedHash = hashContent(fileContent);
  //                   ↑↑↑↑↑↑↑↑↑↑↑
  //            Browser KHÔNG làm việc này!
  
  // ❌ Browser KHÔNG compare hash
  if (computedHash !== extractedHash) {
    throw new Error('Hash mismatch!'); 
    // ← Không bao giờ xảy ra vì browser không verify!
  }
}

// ════════════════════════════════════════════════════════════════
// ✅ BROWSER THỰC SỰ LÀM GÌ? (Reality)
// ════════════════════════════════════════════════════════════════

function browserReality(newUrl: string) {
  /**
   * BƯỚC 1: Parse HTML
   */
  const htmlContent = `
    <script src="/static/js/app.abc123def456.js"></script>
  `;
  
  // Browser extract URL từ src attribute
  const scriptUrl = '/static/js/app.abc123def456.js';
  //                                ↑↑↑↑↑↑↑↑↑↑↑↑
  //                  Browser coi "abc123def456" là PART OF FILENAME
  //                  KHÔNG phải hash để verify!
  
  /**
   * BƯỚC 2: Tạo cache key
   */
  const cacheKey = `https://example.com${scriptUrl}`;
  //               ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
  //          Full URL (including "hash") làm cache key
  
  /**
   * BƯỚC 3: Check cache
   */
  const cachedResponse = diskCache.get(cacheKey);
  
  if (cachedResponse) {
    // ✅ Cache hit → Dùng cached file
    console.log('✅ Using cached file');
    return cachedResponse;
  }
  
  /**
   * BƯỚC 4: Cache miss → Download file
   */
  console.log('❌ Cache miss, downloading...');
  const response = await fetch(cacheKey);
  
  // ✅ Browser chỉ download và cache
  // ❌ Browser KHÔNG verify hash trong filename!
  diskCache.set(cacheKey, response);
  
  return response;
}

/**
 * ════════════════════════════════════════════════════════════════
 * 🎯 HASH Ở ĐÂU TRONG URL? (Where is the hash?)
 * ════════════════════════════════════════════════════════════════
 */

const hashLocations = {
  // ❌ SAI: Hash ở query string (KHÔNG phải content hash!)
  wrongWay: {
    url: 'https://example.com/app.js?v=abc123',
    //                                  ↑↑↑↑↑↑
    //                          Query param (manual versioning)
    problem: 'Có thể thay đổi thủ công, không phản ánh content',
    note: 'Đây là CACHE BUSTING, không phải content hash',
  },
  
  // ✅ ĐÚNG: Hash nhúng trong tên file
  correctWay: {
    url: 'https://example.com/static/js/app.abc123def456.js',
    //                                      ↑↑↑↑↑↑↑↑↑↑↑↑
    //                              Content hash (MD5/SHA256 của file)
    benefit: 'Hash tự động thay đổi khi content thay đổi',
    security: 'HTTPS đảm bảo file không bị tamper',
  },
};

/**
 * ════════════════════════════════════════════════════════════════
 * 🏗️ BUILD TOOL TẠO HASH NHƯ THẾ NÀO?
 * ════════════════════════════════════════════════════════════════
 */

// Webpack/Vite config
const webpackConfig = {
  output: {
    filename: '[name].[contenthash].js',
    //               ↑↑↑↑↑↑↑↑↑↑↑↑
    //         Placeholder cho content hash
    
    chunkFilename: '[name].[contenthash].chunk.js',
  },
};

// Build process (step-by-step):
function buildProcess() {
  /**
   * STEP 1: Đọc source code
   */
  const sourceCode = `
    import React from 'react';
    const App = () => <div>Hello World</div>;
    export default App;
  `;
  
  /**
   * STEP 2: Bundle code (transpile, minify, etc.)
   */
  const bundledCode = `
    !function(){var e={};e.id=0,e.exports={},console.log("Hello World")}();
  `;
  
  /**
   * STEP 3: Hash bundled content
   */
  const hash = crypto
    .createHash('md5')
    .update(bundledCode)
    .digest('hex')
    .slice(0, 12); // First 12 chars: "abc123def456"
  
  /**
   * STEP 4: Generate filename với hash
   */
  const filename = `app.${hash}.js`; // "app.abc123def456.js"
  
  /**
   * STEP 5: Write file to disk
   */
  fs.writeFileSync(`dist/static/js/${filename}`, bundledCode);
  
  /**
   * STEP 6: Update HTML references
   */
  const html = `
    <!DOCTYPE html>
    <html>
      <head>
        <script src="/static/js/${filename}"></script>
        <!--                      ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
                          Hash nhúng trong filename -->
      </head>
      <body></body>
    </html>
  `;
  
  fs.writeFileSync('dist/index.html', html);
  
  return filename; // "app.abc123def456.js"
}

/**
 * ════════════════════════════════════════════════════════════════
 * 🔄 DEPLOY MỚI - HASH THAY ĐỔI
 * ════════════════════════════════════════════════════════════════
 */

const deploymentScenario = {
  /**
   * BUILD 1: Initial deployment
   */
  build1: {
    sourceCode: 'const App = () => <div>Hello World</div>',
    hash: 'abc123def456',
    filename: 'app.abc123def456.js',
    html: '<script src="/static/js/app.abc123def456.js"></script>',
  },
  
  /**
   * BUILD 2: Code changed
   */
  build2: {
    sourceCode: 'const App = () => <div>Hello React</div>',
    //                                    ↑↑↑↑↑ ↑↑↑↑↑
    //                              "World" → "React" (changed!)
    
    hash: 'xyz789abc123', // Hash MỚI vì content khác
    filename: 'app.xyz789abc123.js',
    html: '<script src="/static/js/app.xyz789abc123.js"></script>',
    //                                ↑↑↑↑↑↑↑↑↑↑↑↑
    //                          URL mới vì hash khác!
  },
  
  /**
   * USER EXPERIENCE
   */
  userFlow: {
    step1: 'User visit website (build 1)',
    action1: 'Browser downloads app.abc123def456.js',
    cache1: 'Cache với max-age=31536000 (1 năm)',
    
    step2: 'Developer deploys build 2',
    change: 'HTML mới reference app.xyz789abc123.js',
    
    step3: 'User reload page (F5)',
    action2: 'Browser requests /index.html (no-cache)',
    receive: 'HTML mới với <script src="app.xyz789abc123.js">',
    
    step4: 'Browser parse HTML',
    check: 'app.xyz789abc123.js ≠ app.abc123def456.js (URL khác!)',
    result: '❌ Cache miss → Download app.xyz789abc123.js mới',
    
    note: '✅ Cache busting TỰ ĐỘNG qua hash thay đổi!',
  },
};

/**
 * ════════════════════════════════════════════════════════════════
 * 🔐 TẠI SAO KHÔNG CẦN VERIFY HASH?
 * ════════════════════════════════════════════════════════════════
 */

const whyNoVerification = {
  reason1: {
    title: 'Build tool đảm bảo hash chính xác',
    detail: 'Webpack/Vite hash content → Filename luôn match content',
  },
  
  reason2: {
    title: 'HTTPS đảm bảo integrity',
    detail: 'SSL/TLS certificate verify → File không bị tamper',
    note: 'Man-in-the-middle attack prevented by HTTPS',
  },
  
  reason3: {
    title: 'Subresource Integrity (SRI) cho CDN',
    detail: `
      <script 
        src="https://cdn.example.com/lib.js"
        integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/ux..."
        crossorigin="anonymous">
      </script>
    `,
    note: 'Browser VERIFY hash nếu có SRI attribute',
  },
  
  reason4: {
    title: 'Cache busting đủ hiệu quả',
    detail: 'URL khác = File khác (theo browser logic)',
    performance: 'Verify hash = extra CPU cost (không cần thiết)',
  },
  
  reason5: {
    title: 'Không phải trách nhiệm của browser',
    detail: 'Browser chỉ load và execute code',
    security: 'App developer chịu trách nhiệm về code integrity',
  },
};

/**
 * ════════════════════════════════════════════════════════════════
 * 📊 SO SÁNH: Query String vs Filename Hash
 * ════════════════════════════════════════════════════════════════
 */

const comparisonTable = {
  queryString: {
    example: '/app.js?v=1.0.0',
    
    pros: [
      'Dễ implement (chỉ cần thêm ?v=...)',
      'Không cần build tool',
      'Có thể manual bump version',
    ],
    
    cons: [
      'Có thể quên update version',
      'Version không reflect content (v1.0.0 có thể có code khác)',
      'Một số proxy/CDN ignore query string',
      'Có thể bị stripped bởi intermediate caches',
    ],
    
    useCase: 'Small projects, manual versioning',
  },
  
  filenameHash: {
    example: '/app.abc123def456.js',
    
    pros: [
      '✅ Hash tự động (build tool)',
      '✅ Hash CHÍNH XÁC phản ánh content',
      '✅ Không bao giờ serve sai file (hash khác = file khác)',
      '✅ CDN/Proxy friendly',
      '✅ Long-term caching an toàn (immutable)',
    ],
    
    cons: [
      'Cần build tool (Webpack, Vite, Rollup, etc.)',
      'File cũ tích luỹ trong dist/ (cần cleanup)',
    ],
    
    useCase: 'Production apps, modern build pipeline',
  },
};

/**
 * ════════════════════════════════════════════════════════════════
 * ✅ BEST PRACTICES
 * ════════════════════════════════════════════════════════════════
 */

const bestPractices = {
  // 1. HTML: Luôn no-cache
  html: {
    headers: 'Cache-Control: no-cache, must-revalidate',
    reason: 'HTML chứa references đến bundle → Phải luôn mới nhất',
  },
  
  // 2. Static assets with hash: Long-term immutable cache
  staticAssets: {
    filename: '[name].[contenthash].[ext]',
    headers: 'Cache-Control: public, max-age=31536000, immutable',
    reason: 'Hash thay đổi = URL thay đổi = Auto cache bust',
  },
  
  // 3. Images without hash: Medium-term cache
  images: {
    headers: 'Cache-Control: public, max-age=604800', // 7 days
    versioning: 'Add ?v=... hoặc hash filename nếu cần',
  },
  
  // 4. API: Short cache + revalidate
  api: {
    headers: 'Cache-Control: public, max-age=300, must-revalidate',
    etag: 'Generate ETag từ data hash',
    reason: 'Balance giữa performance và freshness',
  },
};

/**
 * ════════════════════════════════════════════════════════════════
 * 📝 TÓM TẮT
 * ════════════════════════════════════════════════════════════════
 */

const summary = {
  question1: 'Browser có check hash trong filename không?',
  answer1: '❌ KHÔNG. Browser chỉ so sánh URL as string.',
  
  question2: 'Hash bundle ở đâu trong URL?',
  answer2: '✅ Nhúng TRONG TÊN FILE: app.abc123.js (không phải query string)',
  
  question3: 'Tại sao không cần verify hash?',
  answer3: `
    - Build tool đảm bảo hash chính xác
    - HTTPS đảm bảo integrity
    - Cache busting qua URL đủ hiệu quả
    - Verify hash = performance overhead không cần thiết
  `,
  
  question4: 'Cache busting hoạt động như thế nào?',
  answer4: `
    1. Code thay đổi → Hash thay đổi
    2. Hash thay đổi → Filename thay đổi
    3. Filename thay đổi → URL thay đổi
    4. URL thay đổi → Browser thấy là file mới
    5. Browser download file mới (bypass cache)
  `,
  
  question5: 'Best practice cho production?',
  answer5: `
    - HTML: no-cache (luôn check server)
    - JS/CSS với hash: max-age=31536000, immutable
    - Images: max-age=604800 (7 ngày) hoặc hash nếu thay đổi thường xuyên
    - API: max-age=300, must-revalidate, ETag
  `,
};
```

---

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


