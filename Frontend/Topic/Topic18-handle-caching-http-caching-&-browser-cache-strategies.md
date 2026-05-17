# 💾 Topic 18: HTTP Caching & Browser Cache Strategies

## ⭐ Senior/Staff Summary

HTTP caching là cơ chế để browser, CDN/proxy và service worker tái sử dụng response thay vì luôn tải lại từ origin. Với frontend production, chiến lược tốt thường là:

- ✅ `index.html`: revalidate thường xuyên bằng `Cache-Control: no-cache` để luôn lấy manifest/bundle hash mới.
- ✅ JS/CSS/assets có content hash: cache rất lâu bằng `Cache-Control: public, max-age=31536000, immutable`.
- ✅ API/public data: cache ngắn, dùng `ETag`/`Last-Modified` để conditional request trả `304 Not Modified`.
- ✅ Private/user-specific data: `private`, TTL ngắn hoặc revalidate.
- ❌ Sensitive data: `no-store`.
- ✅ CDN/proxy cache: tách rõ cache public, purge/invalidate khi cần, kiểm soát bằng `s-maxage`, `Surrogate-Control` hoặc platform config.

> 🔥 Điểm senior cần nói được: browser không "hiểu" bundle hash. Hash trong filename chỉ làm URL thay đổi. URL khác = cache key khác = browser download resource mới.

## 🧠 Key Mental Model

Browser quyết định dùng cache dựa trên 3 lớp chính:

| Lớp | Ý nghĩa | Ví dụ |
| --- | --- | --- |
| Cache key | Thường là URL đầy đủ + method + một số request header theo `Vary` | `/app.abc.js` khác `/app.xyz.js`; `/api/users?page=1` khác `?page=2` |
| Freshness | Response còn mới không | `Cache-Control: max-age=3600`, `Expires` |
| Validation | Nếu stale thì hỏi server xem có đổi chưa | `ETag`/`If-None-Match`, `Last-Modified`/`If-Modified-Since` |

Flow đơn giản:

```text
Request resource
  → Có cache entry?
    → Không: tải từ server/CDN
    → Có:
      → no-store: không dùng cache
      → còn fresh: dùng cache trực tiếp
      → stale/no-cache: revalidate
        → 304: dùng cached body
        → 200: nhận body mới và cập nhật cache
```

## 📌 Main Concepts

### 1. Browser Cache Theo Loại Storage

| Loại cache | Đặc điểm | Khi thường gặp |
| --- | --- | --- |
| Memory cache | Nhanh nhất, sống ngắn trong RAM/tab/process | Reload nhanh trong cùng phiên |
| Disk cache | Lưu trên ổ đĩa, sống qua nhiều phiên | Static assets, images, fonts |
| HTTP cache | Luật cache do HTTP headers quyết định | HTML/CSS/JS/API/images |
| BFCache | Lưu cả page state khi back/forward | Back/forward navigation gần như instant |
| Cache Storage | API do service worker/app quản lý | Offline, PWA, runtime caching |

⚠️ `from memory cache`/`from disk cache` trong DevTools chỉ nói resource lấy từ đâu, không nói strategy đúng hay sai. Muốn debug phải xem headers, status `200/304`, age và request headers.

### 2. HTTP Cache Headers Bắt Buộc Biết

| Header | Vai trò | Production note |
| --- | --- | --- |
| `Cache-Control` | Header chính để định nghĩa cache policy | Ưu tiên hơn `Expires` |
| `ETag` | Version token của response | Dùng với `If-None-Match`, mạnh hơn timestamp |
| `Last-Modified` | Thời điểm resource đổi lần cuối | Dùng với `If-Modified-Since`, ít chính xác hơn `ETag` |
| `Expires` | Thời điểm hết hạn kiểu cũ | Legacy; dùng khi cần hỗ trợ cache cũ |
| `Vary` | Cache biến đổi theo request header | Cần cho `Accept-Encoding`, `Accept`, `Origin`, nhưng đừng lạm dụng |
| `Age` | Response đã nằm trong shared cache bao lâu | Hữu ích khi debug CDN |

### 3. `Cache-Control` Directives

| Directive | Ý nghĩa | Dùng khi nào |
| --- | --- | --- |
| `public` | Browser và shared cache/CDN được cache | Static assets, public API |
| `private` | Chỉ browser cache, shared cache không được dùng chung | User-specific response |
| `max-age=3600` | Fresh trong 3600 giây tại browser | Assets/API public |
| `max-age=0` | Cache hết hạn ngay, thường phải revalidate | Muốn lưu nhưng luôn check lại |
| `s-maxage=600` | TTL riêng cho shared cache/CDN | CDN cache API/HTML public |
| `no-cache` | Có thể lưu, nhưng phải revalidate trước khi dùng | HTML, API cần freshness |
| `no-store` | Không lưu ở bất kỳ cache nào | Token, banking, PII nhạy cảm |
| `must-revalidate` | Khi stale phải hỏi server, không tự ý dùng stale | API cần nhất quán |
| `immutable` | Trong TTL không cần revalidate | File có content hash |
| `stale-while-revalidate=60` | Được dùng stale trong lúc update nền | CDN/API có thể chấp nhận stale ngắn |

💡 `no-cache` không có nghĩa là "không cache". Nó nghĩa là "được lưu, nhưng trước khi dùng phải hỏi server". Muốn cấm lưu thật sự thì dùng `no-store`.

Legacy headers vẫn gặp trong hệ thống cũ:

```http
Cache-Control: no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: 0
```

`Pragma` và `Expires: 0` chủ yếu để tương thích cache cũ. Với browser/CDN hiện đại, `Cache-Control` là nguồn quyết định chính.

### 4. Conditional Requests: `ETag` và `Last-Modified`

`ETag` flow:

```text
1. Server trả: ETag: "users-v42"
2. Browser lưu response + ETag
3. Lần sau cache stale/no-cache:
   If-None-Match: "users-v42"
4. Server:
   - Không đổi → 304 Not Modified, no body
   - Đã đổi → 200 OK, body mới, ETag mới
```

`Last-Modified` flow tương tự nhưng dùng timestamp:

```text
Last-Modified: Tue, 14 May 2026 10:00:00 GMT
If-Modified-Since: Tue, 14 May 2026 10:00:00 GMT
```

✅ `ETag` phù hợp khi content có thể đổi nhưng timestamp không đủ chính xác.
⚠️ Tránh ETag không ổn định giữa nhiều origin server, vì nó làm cache revalidation mất hiệu quả.

### 5. `Vary`: Cache Key Không Chỉ Là URL

`Vary` nói cache phải tách entry theo request header.

| `Vary` | Tác dụng | Pitfall |
| --- | --- | --- |
| `Vary: Accept-Encoding` | Tách gzip/br/identity | Gần như luôn cần |
| `Vary: Accept` | Tách WebP/AVIF/JPEG hoặc API content type | Dễ tăng số entry |
| `Vary: Origin` | Tách response theo CORS origin | Cẩn thận với CDN |
| `Vary: User-Agent` | Tách mobile/desktop | Dễ làm cache fragmentation rất nặng |

### 6. Browser Cache Từng Loại Resource

| Resource | Header gợi ý | Vì sao |
| --- | --- | --- |
| HTML (`index.html`) | `Cache-Control: no-cache` | HTML chứa link tới bundle hash mới, cần revalidate sau deploy |
| JS/CSS có hash | `Cache-Control: public, max-age=31536000, immutable` | URL đổi khi content đổi, cache dài hạn an toàn |
| Images/fonts có hash | `public, max-age=31536000, immutable` | Ít đổi, nên version bằng filename |
| Images không hash | `public, max-age=604800` hoặc TTL ngắn hơn | Phải chấp nhận stale hoặc version bằng query/path |
| Public API | `public, max-age=60, stale-while-revalidate=300` hoặc `max-age=300, must-revalidate` | Tùy mức chấp nhận stale |
| User API | `private, no-cache` hoặc TTL ngắn | Không để CDN dùng chung |
| Sensitive API | `no-store` | Không lưu token/PII nhạy cảm |

### 7. Khi Nào Browser Request Resource Mới?

| Trường hợp | Ví dụ | Kết quả |
| --- | --- | --- |
| Cache miss | Chưa từng tải URL | Request server/CDN |
| Cache expired | `max-age` đã qua | Revalidate hoặc fetch lại |
| `no-cache` | HTML/API cần check | Gửi conditional request nếu có validator |
| `no-store` | Sensitive response | Luôn request, không lưu |
| Hard reload | `Cmd+Shift+R`/`Ctrl+F5` | Bypass nhiều cache browser |
| URL đổi | `app.abc.js` → `app.xyz.js` | Cache key mới, download mới |
| `Vary` khác | `Accept: image/avif` khác `image/webp` | Entry khác |
| ETag mismatch | Server thấy version khác | `200 OK` body mới thay vì `304` |

Normal reload thường revalidate HTML, nhưng vẫn có thể dùng fresh static assets. Back/forward có thể dùng BFCache và không request server.

### 8. Browser Có Check Bundle Hash Không?

❌ Không. Browser không extract hash từ `app.abc123.js`, không hash content để so sánh, và không biết `abc123` là gì.

Browser chỉ thấy:

```text
/static/app.abc123.js
/static/app.xyz789.js
```

Hai string URL khác nhau nên là hai cache entry khác nhau. Hash là convention của build tool như Vite/Webpack/Rollup.

```js
// Webpack/Rollup/Vite-style output naming
{
  filename: "[name].[contenthash].js",
  chunkFilename: "[name].[contenthash].chunk.js",
}
```

Nếu cần browser verify integrity của file từ CDN bên thứ ba, dùng `Subresource Integrity`:

```html
<script
  src="https://cdn.example.com/lib.js"
  integrity="sha384-..."
  crossorigin="anonymous"
></script>
```

### 9. Cache Busting

Cache busting là làm URL thay đổi khi content thay đổi.

| Cách | Ví dụ | Đánh giá |
| --- | --- | --- |
| Filename content hash | `/app.abc123.js` | ✅ Tốt nhất cho production bundle |
| Query version | `/logo.png?v=2` | Dễ làm, nhưng có thể quên bump; một số proxy config có thể bỏ qua query |
| Directory version | `/v42/logo.png` | Hữu ích cho asset pipeline/CDN |
| Manual purge | Purge CDN path/tag | Cần cho HTML/API hoặc asset không version |

Flow deploy chuẩn:

```text
Code đổi
  → build tool tạo content hash mới
  → HTML mới trỏ tới bundle URL mới
  → browser revalidate HTML
  → thấy URL bundle mới
  → cache miss và download bundle mới
```

File cũ vẫn có thể nằm trong disk cache, nhưng không còn được HTML mới tham chiếu và sẽ bị browser cleanup theo quota/LRU.

### 10. CDN/Proxy Cache

CDN là shared cache nên phải phân biệt rõ public/private.

| Mục tiêu | Header/config gợi ý |
| --- | --- |
| Cache static hashed assets | `Cache-Control: public, max-age=31536000, immutable` |
| Cache public API ở CDN lâu hơn browser | `Cache-Control: public, max-age=30, s-maxage=300, stale-while-revalidate=60` |
| Không cache user data ở CDN | `Cache-Control: private, no-cache` hoặc `no-store` |
| Purge theo release | Versioned filenames, cache tags, surrogate keys |
| Debug CDN | Xem `Age`, `Via`, `X-Cache`, CDN-specific headers |

⚠️ Không để response có cookie/auth header bị cache public nếu không chắc CDN đã key theo đúng user/context.

### 11. Service Worker & Cache Storage

Service worker nằm trước network và có thể override HTTP cache behavior. Nó phù hợp cho offline/PWA, nhưng cũng là nguồn bug "deploy rồi user vẫn thấy app cũ".

Các strategy phổ biến:

| Strategy | Cách chạy | Dùng cho |
| --- | --- | --- |
| Cache First | Tìm Cache Storage trước, miss mới network | Hashed assets, fonts |
| Network First | Network trước, fail mới cache | HTML/API cần mới nhưng hỗ trợ offline |
| Stale While Revalidate | Trả cache ngay, update cache nền | Feed, catalog, avatar |
| Network Only | Luôn network | Sensitive mutation/auth |
| Cache Only | Chỉ cache | Precached offline shell |

Production note:

- Version service worker cache name: `app-shell-v42`.
- Cleanup cache cũ trong `activate`.
- Với app shell, cân nhắc thông báo user reload khi service worker mới activated.
- Đừng cache API user-specific bằng key quá rộng.

## 🧪 Practical TypeScript/JavaScript Examples

### Example 1: Express Headers Cho SPA

```typescript
import express from 'express';

const app = express();

app.use('/assets', express.static('dist/assets', {
  immutable: true,
  maxAge: '1y',
  setHeaders(res) {
    res.setHeader('Cache-Control', 'public, max-age=31536000, immutable');
  },
}));

app.get('/api/public-products', (_req, res) => {
  res.setHeader(
    'Cache-Control',
    'public, max-age=60, s-maxage=300, stale-while-revalidate=120'
  );
  res.json([{ id: 'p1', name: 'Keyboard' }]);
});

app.get('/api/me', (_req, res) => {
  res.setHeader('Cache-Control', 'private, no-cache');
  res.json({ id: 'u1', name: 'An' });
});

app.get('/api/token', (_req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  res.json({ token: 'secret' });
});

app.get('*', (_req, res) => {
  res.setHeader('Cache-Control', 'no-cache');
  res.sendFile('dist/index.html', { root: process.cwd() });
});
```

### Example 2: ETag Cho API

```typescript
import crypto from 'node:crypto';
import type { Request, Response } from 'express';

function createETag(value: unknown): string {
  return `"${crypto.createHash('sha256').update(JSON.stringify(value)).digest('hex')}"`;
}

export function getUsers(req: Request, res: Response) {
  const users = [{ id: 1, name: 'Jane' }];
  const etag = createETag(users);

  res.setHeader('Cache-Control', 'public, max-age=300, must-revalidate');
  res.setHeader('ETag', etag);
  res.setHeader('Vary', 'Accept-Encoding');

  if (req.header('If-None-Match') === etag) {
    return res.status(304).end();
  }

  return res.status(200).json(users);
}
```

### Example 3: Client Fetch Với Cache Mode

```typescript
async function fetchDashboard() {
  const response = await fetch('/api/dashboard', {
    cache: 'no-cache', // cho phép cache nhưng buộc revalidate
    headers: { Accept: 'application/json' },
  });

  if (!response.ok) throw new Error(`Dashboard failed: ${response.status}`);
  return response.json() as Promise<{ revenue: number }>;
}

async function fetchSensitiveData() {
  const response = await fetch('/api/payment-methods', {
    cache: 'no-store', // request không đọc/ghi HTTP cache
  });

  return response.json();
}
```

⚠️ `fetch(..., { cache: 'reload' })`, `no-cache`, `force-cache`, `only-if-cached` có behavior khác nhau theo browser/context. Đừng dùng để "fix cache" production nếu server headers sai.

### Example 4: Service Worker Stale-While-Revalidate

```typescript
const RUNTIME_CACHE = 'runtime-v1';

self.addEventListener('fetch', (event: FetchEvent) => {
  const request = event.request;
  const url = new URL(request.url);

  if (request.method !== 'GET') return;
  if (!url.pathname.startsWith('/api/catalog')) return;

  event.respondWith(staleWhileRevalidate(request));
});

async function staleWhileRevalidate(request: Request): Promise<Response> {
  const cache = await caches.open(RUNTIME_CACHE);
  const cached = await cache.match(request);

  const networkPromise = fetch(request).then((response) => {
    if (response.ok) cache.put(request, response.clone());
    return response;
  });

  return cached ?? networkPromise;
}
```

## 🚀 Production Notes / React Implications

- HTML phải dễ update hơn bundle. Nếu HTML bị cache lâu, user có thể kẹt ở bundle cũ hoặc gọi chunk đã bị xóa.
- Hashed assets nên giữ lại vài release trên CDN/origin để tránh lỗi user đang mở tab cũ request lazy chunk cũ.
- React SPA thường có lazy chunks. Khi deploy, cần xử lý `ChunkLoadError`: báo user reload hoặc retry sau khi lấy HTML mới.
- Data fetching layer như React Query/SWR có cache riêng trong memory. Nó không thay thế HTTP cache; hai lớp này cần TTL/stale policy nhất quán.
- `stale-while-revalidate` ở HTTP/CDN giống mental model của SWR: trả dữ liệu cũ nhanh, update nền. Nhưng với dữ liệu giao dịch/permission, stale có thể nguy hiểm.
- Cache public API phải xét auth, cookie, `Authorization`, `Vary` và CDN key. Sai ở đây là lỗi bảo mật, không chỉ lỗi performance.
- Khi dùng service worker, deploy flow phải kiểm soát cache version và activation. Bug thường không nằm ở browser HTTP cache mà nằm ở Cache Storage cũ.
- Core Web Vitals hưởng lợi từ cache vì giảm TTFB, FCP/LCP cho repeat visit, nhưng first visit vẫn phụ thuộc bundle size, preload, CDN và server latency.

## ⚠️ Common Pitfalls

| Pitfall | Hậu quả | Cách tránh |
| --- | --- | --- |
| Cache HTML quá lâu | User không nhận bundle hash mới | `Cache-Control: no-cache` cho HTML |
| Không hash JS/CSS nhưng cache 1 năm | User kẹt code cũ | Dùng content hash hoặc TTL ngắn |
| Dùng `no-cache` cho dữ liệu nhạy cảm | Dữ liệu vẫn có thể được lưu | Dùng `no-store` |
| `Vary: *` hoặc vary quá rộng | Cache miss liên tục | Chỉ vary theo header thật sự ảnh hưởng response |
| CDN cache response có cookie | Lộ dữ liệu user | `private/no-store`, cache key đúng, bypass auth responses |
| Purge CDN nhưng browser vẫn giữ asset cũ | User vẫn dùng cache local | Version URL bằng hash |
| Xóa asset cũ ngay sau deploy | Tab cũ/lazy chunk cũ lỗi 404 | Giữ assets cũ vài release |
| Service worker không cleanup | User thấy app rất cũ | Version cache, cleanup trong `activate` |
| Debug khi DevTools bật "Disable cache" | Kết luận sai | Tắt option này khi kiểm tra real behavior |

## ✅ Decision Guide / Checklist

### Chọn Header Nhanh

| Bạn đang cache gì? | Policy nên dùng |
| --- | --- |
| `index.html` / app shell URL chính | `Cache-Control: no-cache` |
| Bundle JS/CSS có content hash | `public, max-age=31536000, immutable` |
| Font/image có hash | `public, max-age=31536000, immutable` |
| Image không hash, có thể stale | `public, max-age=604800` |
| Public API ít đổi | `public, max-age=60, s-maxage=300, stale-while-revalidate=120` |
| API cần check mỗi lần nhưng tiết kiệm bandwidth | `no-cache` + `ETag` |
| User profile/settings | `private, no-cache` hoặc TTL ngắn |
| Token, payment, medical/banking data | `no-store` |

### Debug Checklist

- [ ] Kiểm tra response headers: `Cache-Control`, `ETag`, `Last-Modified`, `Expires`, `Vary`.
- [ ] Kiểm tra request headers: `If-None-Match`, `If-Modified-Since`, `Cache-Control`.
- [ ] Phân biệt `200 from disk/memory cache`, `304`, `200 network`.
- [ ] Tắt `Disable cache` trong DevTools khi test hành vi thật.
- [ ] Xem CDN headers: `Age`, `X-Cache`, `CF-Cache-Status`, `Via`.
- [ ] Kiểm tra URL đã đổi chưa: filename hash/query/path.
- [ ] Kiểm tra service worker: tab Application → Service Workers → Cache Storage.
- [ ] Test normal reload, hard reload, tab cũ sau deploy, back/forward.
- [ ] Với chunk lỗi, kiểm tra asset cũ còn tồn tại trên CDN/origin không.

## 🧩 Tóm Tắt 4 Câu Hỏi Chính

| Câu hỏi | Trả lời ngắn |
| --- | --- |
| Browser cache HTML/CSS/JS/images thế nào? | Theo HTTP headers. HTML thường `no-cache`; hashed JS/CSS/images cache dài hạn; API tùy data freshness. |
| Khi nào browser request resource mới? | Cache miss/expired, `no-cache/no-store`, hard reload, URL đổi, `Vary` khác, ETag mismatch. |
| Browser có check bundle hash không? | Không. Browser chỉ so sánh URL string và headers. |
| Hash trong filename để làm gì? | Cache busting: content đổi → hash đổi → URL đổi → download file mới. |

## 🎤 Short Interview Answer

Em nghĩ HTTP caching quan trọng nhất là chọn đúng policy theo loại resource. Với SPA, em thường để `index.html` là `Cache-Control: no-cache` để mỗi lần vào app browser revalidate và lấy được bundle hash mới. Còn JS/CSS/fonts/images đã có content hash thì em cache rất lâu bằng `public, max-age=31536000, immutable`, vì khi content đổi thì URL đổi.

Theo em điểm hay bị nhầm là `no-cache` không phải không lưu cache; nó chỉ bắt browser hỏi lại server trước khi dùng, thường qua `ETag` hoặc `Last-Modified` và có thể nhận `304`. Nếu là token, payment, dữ liệu nhạy cảm thì em dùng `no-store`.

Em thấy ở production cần nhìn thêm CDN/proxy và service worker, vì browser cache chỉ là một lớp. Với CDN phải tránh cache nhầm user data, dùng `s-maxage`/purge/versioned assets hợp lý. Với service worker phải version Cache Storage và cleanup cache cũ, nếu không deploy mới vẫn có thể bị app shell cũ giữ lại. Khi debug em xem Network headers, status `200/304/from disk cache`, `Vary`, CDN `Age/X-Cache`, và kiểm tra cả Cache Storage trong Application tab.
