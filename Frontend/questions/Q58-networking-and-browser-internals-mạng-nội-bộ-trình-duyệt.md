# 🌐 Q58: Networking & Browser Internals - Mạng & Nội Tế Trình Duyệt

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (4-5 phút):**

**"HTTP/2 = multiplexing (1 TCP), HTTP/3 = QUIC (UDP, no TCP HoL). CORS = cross-origin security (preflight OPTIONS). CSP = prevent XSS. Cache: immutable, stale-while-revalidate. CDN = edge caching, băng thông, latency."**

**🔑 Network Fundamentals:**

**1. HTTP Versions:**
- **HTTP/1.1**: 1 request/connection, head-of-line blocking
- **HTTP/2**: Multiplexing (many requests/1 TCP), header compression (HPACK), server push
- **HTTP/3**: QUIC (UDP), faster handshake (0-RTT), no TCP HoL blocking
- **Impact**: HTTP/2/3 = fewer requests overhead, không cần concat files

**2. CORS (Cross-Origin Resource Sharing):**
- **Same-origin policy**: Browser block cross-origin requests
- **Simple requests**: GET/POST → check `Access-Control-Allow-Origin`
- **Preflight**: OPTIONS request trước PUT/DELETE/custom headers
- **Credentials**: `credentials: 'include'` + `Access-Control-Allow-Credentials: true`

**3. CSP (Content Security Policy):**
- **Prevent XSS**: Whitelist script sources
- Header: `Content-Security-Policy: script-src 'self' cdn.example.com`
- **Nonce**: `<script nonce="random123">` - random per request
- **Report-only mode**: Test CSP without blocking

**4. Browser Cache:**
- **`Cache-Control: immutable`**: File không bao giờ thay đổi (hashed filenames)
- **`stale-while-revalidate`**: Serve stale, fetch fresh background
- **`max-age=3600`**: Cache 1 giờ
- **ETag**: Validate cached file (304 Not Modified)

**5. CDN (Content Delivery Network):**
- **Edge caching**: Assets gần user (lower latency)
- **Bandwidth**: Offload origin server
- **Security**: DDoS protection, WAF

**⚠️ Lỗi Thường Gặp:**
- CORS errors → check server headers, proxy trong dev
- Không cache static assets → waste bandwidth
- CSP too strict → break inline scripts, dùng nonces
- HTTP/1.1 concat files → không cần với HTTP/2

**💡 Kiến Thức Senior:**
- **DNS prefetch**: `<link rel="dns-prefetch" href="//cdn.example.com">`
- **Preconnect**: Early TCP+TLS handshake
- **Brotli compression**: Better than gzip (~20% smaller)
- **Service Workers**: Network proxy, offline caching, cache strategies

> **Câu hỏi phỏng vấn Senior Frontend Developer**
> **Độ khó:** ⭐⭐⭐⭐⭐ (Advanced)  
> **Thời gian trả lời:** 15-25 phút---

## 📋 Mục lục
1. [HTTP/1.1, HTTP/2, HTTP/3 - So sánh ngắn gọn](#1-http-11-http2-http3)
2. [CORS (Cross-Origin Resource Sharing)](#2-cors)
3. [CSP (Content Security Policy)](#3-csp)
4. [Browser cache - immutable, revalidate, stale-while-revalidate](#4-browser-cache)
5. [DNS, TCP, TLS - Tổng quan handshake và ảnh hưởng tới frontend](#5-dns-tcp-tls)
6. [Fetch API & Streaming (ReadableStream, Response.body)](#6-fetch-streaming)
7. [Compression: gzip, brotli - khi nào và làm sao](#7-compression)
8. [CDN - Vai trò và best practices](#8-cdn)
9. [Các câu hỏi phỏng vấn thực tế & checklist trả lời nhanh](#9-qa-checklist)

---

## 1. HTTP/1.1, HTTP/2, HTTP/3

### 1.1 Tổng quan
- HTTP/1.1: text-based, request/response theo kết nối, mỗi kết nối thường xử lý 1 request tại một thời điểm (pipelining support hạn chế vì head-of-line blocking).
- HTTP/2: binary protocol, multiplexing trên một kết nối TCP, header compression (HPACK), server push (ít dùng), giảm latency bằng cách gửi nhiều stream trên 1 TCP connection.
- HTTP/3: dựa trên QUIC (UDP-based), tránh Head-of-Line blocking của TCP bằng stream-level multiplexing, cải thiện handshake (0-RTT trong 1 số trường hợp), tốt hơn cho kết nối mạng thay đổi (mobile).

📌 Ý nghĩa cho frontend:
- HTTP/2/3 giúp giảm latency, ít cần concat/sprites/phiên bản bundling cũ vì nhiều request nhỏ được xử lý hiệu quả.
- HTTP/3 đặc biệt có lợi khi mạng hay chuyển đổi (Wi-Fi -> Cellular).

### 1.2 So sánh nhanh
- Multiplexing: HTTP/1.1 (no) → HTTP/2 (yes on TCP) → HTTP/3 (yes on QUIC/UDP)
- Head-of-line blocking: HTTP/1.1 (yes) → HTTP/2 (minimized but still TCP-HoL) → HTTP/3 (avoided)
- TLS: HTTP/1.1/2 thường TLS over TCP; HTTP/3 tích hợp TLS-like vào QUIC (TLS 1.3 handshake on UDP)

### 1.3 Khi nào dùng gì
- Server + CDN hiện đại: bật HTTP/2/3 khi có thể.
- Nếu dùng legacy proxies hoặc load balancer không hỗ trợ HTTP/2/3, đảm bảo fallback an toàn.

---

## 2. CORS (Cross-Origin Resource Sharing)

### 2.1 Vấn đề: Same-origin policy
Trình duyệt chặn request hoặc truy cập tài nguyên cross-origin (domain/port/protocol khác) từ JavaScript nếu server không cho phép.

### 2.2 Cách hoạt động (tóm tắt)
- Simple requests: GET/POST với headers không đặc biệt -> browser gửi request, server cần trả header `Access-Control-Allow-Origin`.
- Preflighted requests: khi method hoặc headers đặc biệt (e.g., `PUT`, `DELETE`, custom headers), browser gửi `OPTIONS` preflight trước để kiểm tra.

### 2.3 Ví dụ header server
```http
# 🌐 Server phản hồi cho request cross-origin
HTTP/1.1 200 OK
Access-Control-Allow-Origin: https://example.com   # 🌍 Domain được phép (hoặc '*' cho tất cả)
Access-Control-Allow-Methods: GET, POST, OPTIONS   # 🔧 HTTP methods được phép
Access-Control-Allow-Headers: Content-Type, Authorization  # 📋 Headers được phép
Access-Control-Allow-Credentials: true            # 🔐 Cho phép gửi cookie/credentials
Access-Control-Max-Age: 86400                    # ⏱️ Cache preflight response (86400s = 24h)
```

### 2.4 Important notes
- `Access-Control-Allow-Origin: *` không cho phép credential (cookie) cùng lúc; để gửi cookie cần trả chính xác domain và `Access-Control-Allow-Credentials: true`.
- Preflight `OPTIONS` phải trả status 200/204 cùng các header cần thiết.
- CORS là cơ chế trình duyệt; server có thể (và nên) kiểm tra Origin để tránh lạm dụng.

### 2.5 Ví dụ Express.js middleware
```js
// 🔧 Express middleware đơn giản cho CORS
app.use((req, res, next) => {
  const origin = req.headers.origin; // 🌍 Lấy origin từ request header
  const allowed = ['https://app.example.com', 'https://admin.example.com']; // 📋 Whitelist domains
  if (allowed.includes(origin)) {
    res.setHeader('Access-Control-Allow-Origin', origin); // ✅ Cho phép origin này
    res.setHeader('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS'); // 🔧 Methods được phép
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization'); // 📋 Headers được phép
    res.setHeader('Access-Control-Allow-Credentials', 'true'); // 🔐 Cho phép credentials
  }
  if (req.method === 'OPTIONS') return res.sendStatus(204); // ✋ Preflight request trả 204
  next();
});
```

---

## 3. CSP (Content Security Policy)

### 3.1 Mục tiêu
CSP giúp giảm XSS bằng cách kiểm soát nguồn của script, styles, images, fonts, frame, etc. Thay vì dựa hoàn toàn vào escaping, CSP đặt whitelist nguồn cho các loại tài nguyên.

### 3.2 Ví dụ header CSP
```http
Content-Security-Policy: default-src 'self';  # 🔒 Default: chỉ từ same origin
  script-src 'self' https://cdn.example.com 'sha256-abc123...';  # 📜 Scripts: self + CDN + hash
  style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;  # 💅 Styles: self + inline + fonts
  img-src 'self' data: https://images.example.com;  # 🖼️ Images: self + data URIs + CDN
  connect-src 'self' https://api.example.com;  # 🔌 Fetch/XHR: self + API domain
  frame-ancestors 'none';  # 🚫 Không cho phép embed trong iframe
  object-src 'none';  # 🚫 Không cho phép <object>/<embed>
  base-uri 'self';  # 🔗 Base URL chỉ từ same origin
```

### 3.3 Ghi chú quan trọng
- `'unsafe-inline'` cho style hoặc script yếu về bảo mật — tránh dùng nếu có thể.
- Dùng `nonce-` hoặc `sha256-` để cho phép inline script an toàn.
- `report-uri` (legacy) hoặc `report-to` để nhận báo cáo vi phạm CSP.

### 3.4 CSP và SPA
- Với SPA dùng inlined scripts (e.g., Vite/CRA inject runtime), dùng `nonce` hoặc tạo strict policy tránh `'unsafe-inline'`.

---

## 4. Browser cache (Cache-Control trực tiếp)

### 4.1 Các chỉ dẫn phổ biến
- `Cache-Control: immutable, max-age=31536000, public` — nghĩa là resource có thể cache lâu dài và không thay đổi (ví dụ: file có hash trong tên).
- `Cache-Control: no-cache` — browser phải revalidate với server (conditional request using If-None-Match/If-Modified-Since).
- `Cache-Control: no-store` — không lưu cache ở bất kỳ nơi nào (thường dùng cho sensitive data)
- `stale-while-revalidate` — trả cache cũ ngay lập tức nhưng fetch bộ mới ở background (useful for performance)
- `stale-if-error` — nếu fetch fail, vẫn dùng bản cũ

### 4.2 Ví dụ header
```http
# 1) 📦 Immutable static asset versioned (file có hash trong tên)
Cache-Control: public, max-age=31536000, immutable  # ⏱️ Cache 1 năm, không thay đổi

# 2) 🔄 API response cần revalidate (check server mỗi lần)
Cache-Control: public, max-age=60, must-revalidate  # ⏱️ Cache 60s, sau đó phải revalidate
ETag: "abc123"  # 🔖 Version identifier cho conditional request

# 3) ⚡ Stale-while-revalidate pattern (fast serve + background update)
Cache-Control: public, max-age=60, stale-while-revalidate=30  # ⏱️ Fresh 60s, stale 30s thêm
```

### 4.3 Giải thích nhanh
- immutable: dùng cho asset có fingerprint (ví dụ `app.abcdef.js`) → browser có thể cache lâu mà không revalidate.
- revalidate (no-cache): browser giữ resource nhưng mỗi lần phải hỏi server xem còn mới không (If-None-Match / 304 Not Modified)
- `stale-while-revalidate`: tradeoff giữa luôn nhanh (serve stale) và vẫn cập nhật bản mới ở background.

---

## 5. DNS, TCP, TLS (handshake)

### 5.1 DNS (Domain Name System)
- Chuyển tên miền `example.com` → IP address.
- Thời gian DNS lookup ảnh hưởng tới initial connection latency.
- DNS records: A, AAAA, CNAME, NS, TXT, etc.
- DNS TTL ảnh hưởng caching: tăng TTL giảm lookup, nhưng làm deploy/trỏ domain lâu hơn.

### 5.2 TCP (3-way handshake)
- Client → SYN → Server (SYN/ACK) → Client ACK → connection established.
- Thiết lập TCP tốn RTT (round-trip time); reusing connections (keep-alive) giảm overhead.

### 5.3 TLS (TLS 1.2 / 1.3)
- TLS handshake thiết lập encrypted channel.
- TLS 1.3 cải tiến: fewer round-trips, faster handshake, 0-RTT resume.
- TLS handshake + TCP handshake = latency; QUIC (HTTP/3) tích hợp transport + crypto cho hiệu năng tốt hơn.

📌 Frontend implications:
- DNS prefetch ( `<link rel="dns-prefetch" href="//example.com">` ) và preconnect ( `<link rel="preconnect" href="https://example.cdn.com" crossorigin>` ) giúp giảm latency bằng cách bắt đầu DNS/TCP/TLS sớm.

Example:
```html
<!-- 🔍 DNS prefetch: Resolve DNS sớm (không tốn nhiều tài nguyên) -->
<link rel="dns-prefetch" href="//fonts.gstatic.com">
<!-- 🔗 Preconnect: DNS + TCP + TLS handshake sớm (full connection) -->
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```

---

## 6. Fetch & streaming

### 6.1 Fetch cơ bản
```js
fetch('/api/data')
  .then(res => res.json())
  .then(data => console.log(data));
```

### 6.2 Streaming response (ReadableStream)
- `response.body` là một `ReadableStream` có thể đọc từng chunk khi server stream data (useful for large files, server-sent events, or progressive rendering).

```js
// 📥 Ví dụ đọc streaming text (progressive data loading)
const resp = await fetch('/stream-endpoint');
const reader = resp.body.getReader(); // 🔍 Lấy ReadableStream reader
const decoder = new TextDecoder(); // 🔤 Decode binary → text
let result = '';
while (true) {
  const { done, value } = await reader.read(); // 📦 Đọc từng chunk
  if (done) break; // ✅ Stream kết thúc
  result += decoder.decode(value, { stream: true }); // 🔤 Decode chunk
  console.log('Chunk:', result); // 📊 Log progressive data
}
console.log('Complete:', result); // ✅ Data đầy đủ
```

### 6.3 Streaming JSON (ndjson) hoặc server-side render progressive
- Server gửi nhiều JSON lines (`\n`-delimited). Client parse line-by-line, render từng phần ngay khi nhận.

### 6.4 AbortController
```js
// 🛑 AbortController - Cancel fetch requests
const controller = new AbortController();
fetch('/api/long', { signal: controller.signal }) // 🔗 Attach abort signal
  .then(r => r.json())
  .catch(err => { if (err.name === 'AbortError') console.log('Aborted'); }); // ❌ Handle abort error

// 🛑 Cancel when needed (user navigate away, timeout, etc.)
controller.abort();
```

---

## 7. Compression (gzip, brotli)

### 7.1 gzip vs brotli
- gzip: phổ biến, nhanh compress/decompress, support rộng.
- brotli: compression ratio tốt hơn (smaller size), đặc biệt hiệu quả với text (HTML/CSS/JS). Tuy nhiên CPU cost compress cao hơn; nên dùng pre-compressed assets at build time.

### 7.2 Server response header
```http
Content-Encoding: br        # 🗜️ Brotli compression (better ratio)
# hoặc
Content-Encoding: gzip      # 🗜️ Gzip compression (faster, universal)

# ⚠️ Vary header quan trọng để cache proxies biết phân biệt theo encoding
Vary: Accept-Encoding       # 🔄 Cache riêng cho br vs gzip
```

### 7.3 Best practice
- Pre-compress assets (build step) and let CDN serve .br/.gz depending on Accept-Encoding.
- Brotli level 4-6 tradeoff tốc độ và ratio; level 11 chậm và không cần thiết cho CI/CD.
- Dynamic compress (on-the-fly) cho API responses có thể tốt cho small payloads, nhưng cần cân CPU.

---

## 8. CDN (Content Delivery Network)

### 8.1 Vai trò
- Cache và serve static assets từ edge locations gần user → giảm latency.
- Offload origin server.
- Một số CDN cung cấp features: image optimization, edge functions, A/B testing, geo routing.

### 8.2 Cache key và invalidation
- CDN cache key thường dựa vào URL + querystring + headers (configurable).
- Invalidate/ purge: theo path hoặc cache-tag/Surrogate-Key patterns (báo cache-purge cho nhiều file cùng lúc).

### 8.3 Example: Serve hashed assets + long TTL
- Build: `app.abc123.js` → `Cache-Control: public, max-age=31536000, immutable`
- Deploy new version: new filename `app.def456.js` → no need to purge old file immediately.

### 8.4 CDN + security
- Use CDN to serve TLS termination (Let’s Encrypt) và enable HTTP/2 or HTTP/3 support.
- Use WAF (Web Application Firewall) at CDN edge to block suspicious traffic.

---

## 9. Câu hỏi phỏng vấn & Checklist trả lời nhanh

- Trình bày sự khác nhau chính giữa HTTP/1.1, HTTP/2 và HTTP/3? (Multiplexing, HoL blocking, QUIC)
- Khi nào dùng `Cache-Control: immutable`? (assets versioned với hash)
- Giải thích preflight CORS và khi nào browser gửi `OPTIONS`? (method/custom headers)
- CSP là gì? Làm sao để whitelist inline script an toàn? (nonce/sha256)
- Tại sao `Vary: Accept-Encoding` là quan trọng khi dùng compression? (proxy caches cần tách theo header)
- Lợi ích của streaming fetch? (progressive render, giảm TTFB user-perceived)
- So sánh gzip & brotli về compression ratio và CPU cost.
- Làm sao `preconnect` giúp giảm TLS/TCP latency? (bắt đầu DNS/TCP/TLS trước khi request asset)

---

## Tài liệu tham khảo nhanh
- MDN: fetch, Streams API, Service Worker docs
- RFCs: HTTP/2 (RFC 7540), QUIC (IETF RFCs), HTTP/3
- Google Web Fundamentals: Caching, Performance
- OWASP: Content Security Policy

---

**Ghi chú:** File này là bản tóm tắt kỹ thuật dành cho câu hỏi phỏng vấn Senior Frontend; nếu bạn muốn, tôi sẽ thêm ví dụ hands-on (mini-labs) cho từng phần: ví dụ deploy CDN config, demo streaming server, hoặc sample Express server trả header cache/CORS/CSP.
