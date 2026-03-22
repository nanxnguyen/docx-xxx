# 🔐 Keycloak - Hướng Dẫn Toàn Diện

> **Keycloak từ cấu trúc – hoạt động nội bộ – token – cơ chế bảo mật – flow FE → BE → Keycloak, theo chuẩn ngân hàng / doanh nghiệp lớn / bảo mật cấp cao.**

---

## 📚 Mục Lục

1. [Tổng quan về Keycloak](#i-tổng-quan-về-keycloak)
2. [Cấu trúc & Thành phần](#ii-cấu-trúc--thành-phần-trong-keycloak)
3. [Cơ chế hoạt động nội bộ](#iii-cơ-chế-hoạt-động-nội-bộ-của-keycloak)
4. [Flow chi tiết: FE → BE → Keycloak](#iv-flow-chi-tiết-fe--be--keycloak)
5. [Các loại Token](#v-giải-thích-chi-tiết-các-loại-token)
6. [Cơ chế bảo mật](#vi-cơ-chế-bảo-mật-trong-flow-fe--be--keycloak)
7. [Ưu & Nhược điểm](#vii-ưu--nhược-điểm)
8. [Sơ đồ tổng quan](#viii-tóm-tắt-sơ-đồ)
9. [SSO - Single Sign-On](#ix-keycloak-sso--cách-hoạt-động-chuyên-sâu)
10. [Đồng bộ tài khoản LDAP/AD](#x-đồng-bộ-tài-khoản-nhân-viên-ldapad--keycloak)
11. [Flow Internal vs External](#xi-2-flow-đăng-nhập-internal-vs-external)
12. [So sánh Internal vs External](#xii-so-sánh-internal-vs-external-flow)
13. [Vấn đề thường gặp](#xiii-vấn-đề-thường-gặp--cách-giải-quyết)
14. [Phân chia Realm tối ưu](#xiv-phân-chia-realm-tối-ưu)
15. [Phân quyền (RBAC/ABAC)](#xv-phân-quyền-rolegroupscope)
16. [Quản lý Client](#xvi-cơ-chế-client--phân-loại)
17. [Token Exchange](#xvii-token-exchange--chuẩn-ngân-hàng--chứng-khoán)
18. [Token Design tối ưu](#xviii-token-design-tối-ưu)
19. [Bảo mật nâng cao (Zero Trust)](#xix-bảo-mật-nâng-cao-zero-trust)
20. [Kiến trúc chuẩn](#xx-kiến-trúc-chuẩn-nhất)
21. [SSO vs Shared Cookie](#xxi-sso-vs-shared-cookie)

---

## 🔐 I. Tổng quan về Keycloak

### 1️⃣ Keycloak là gì?

**Keycloak** là một **Identity & Access Management Server (IAM - Máy chủ quản lý danh tính và truy cập)** – nghĩa là một máy chủ quản lý danh tính và truy cập.

Nó chịu trách nhiệm:

- ✅ **Xác thực người dùng** (Authentication - Kiểm tra danh tính - Xác minh user là ai)
- ✅ **Cấp quyền truy cập** (Authorization - Kiểm tra quyền hạn - Xác định user được làm gì)
- ✅ **Cấp và quản lý JWT token** (Phát token cho client - JWT = JSON Web Token - Token dạng JSON)
- ✅ **Quản lý phiên đăng nhập** (session - Theo dõi ai đã login - Session = Phiên đăng nhập)
- ✅ **Hỗ trợ SSO** (Single Sign-On - Đăng nhập 1 lần - Đăng nhập 1 lần dùng nhiều app) và **SLO** (Single Logout - Logout toàn hệ thống - Logout 1 lần logout tất cả app)

> 🎯 **Keycloak giúp Frontend / Backend không cần tự xây dựng logic đăng nhập phức tạp mà chỉ cần ủy quyền xác thực cho Keycloak.**

---

## 🧩 II. Cấu trúc & Thành phần trong Keycloak

| Thành phần                  | Vai trò                                                                                             | Ví dụ thực tế                               |
| --------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| **Realm**                   | 🌐 Không gian quản lý độc lập (giống 1 tenant - Đơn vị thuê) chứa user, client, role, group         | `momo-ttt`, `hrm-portal`, `finance-system`  |
|                             | // Realm = Vùng quản lý độc lập (Mỗi realm có user, client, role riêng - Giống như 1 công ty riêng) |
| **Client**                  | 📱 Một ứng dụng được đăng ký trong realm (FE hoặc BE - Frontend hoặc Backend)                       | `portal-frontend`, `portal-backend`         |
|                             | // Client = Ứng dụng đã đăng ký (Mỗi app phải đăng ký làm client trong Keycloak)                    |
| **User**                    | 👤 Người dùng có thể đăng nhập                                                                      | `nguyenvana`, `tranthihoa`                  |
|                             | // User = Người dùng (Người có thể login vào hệ thống)                                              |
| **Group**                   | 👥 Nhóm người dùng (gán sẵn role - Gán vai trò sẵn)                                                 | `admin-group`, `customer-group`             |
|                             | // Group = Nhóm (Tập hợp user - User trong group tự động có role của group)                         |
| **Role**                    | 🏆 Vai trò (quyền hạn)                                                                              | `admin`, `viewer`, `manager`                |
|                             | // Role = Vai trò (Quyền hạn của user - Ví dụ: admin có quyền cao, viewer chỉ xem)                  |
| **Scope**                   | 🎯 Quyền truy cập cụ thể theo API                                                                   | `read:users`, `update:reports`              |
|                             | // Scope = Phạm vi quyền (Quyền chi tiết theo API - Ví dụ: đọc user, cập nhật báo cáo)              |
| **Identity Provider (IdP)** | 🔗 Hệ thống xác thực bên ngoài                                                                      | Google Workspace, LDAP, Microsoft AD        |
|                             | // IdP = Nhà cung cấp danh tính (Hệ thống xác thực bên ngoài - LDAP/AD/Google)                      |
| **Token**                   | 🎫 Gói thông tin được cấp sau khi đăng nhập                                                         | `access_token`, `refresh_token`, `id_token` |
|                             | // Token = Chứng chỉ (Thông tin được mã hóa - Dùng để xác thực)                                     |
| **Session**                 | ⏱️ Phiên đăng nhập; Keycloak theo dõi user đã login ở app nào                                       | Giúp thực hiện SSO & SLO                    |
|                             | // Session = Phiên đăng nhập (Keycloak theo dõi user đã login ở app nào - Giúp SSO)                 |
| **Policy / Mapper**         | ⚙️ Quy tắc xác định cách map role hoặc scope                                                        | Gán role từ AD sang client role             |
|                             | // Policy = Chính sách (Quy tắc phân quyền), Mapper = Bộ ánh xạ (Chuyển đổi thông tin)              |

---

## ⚙️ III. Cơ chế hoạt động nội bộ của Keycloak

Keycloak hoạt động dựa trên chuẩn **OIDC (OpenID Connect - Kết nối mở ID)** – mở rộng từ **OAuth2 (Ủy quyền mở phiên bản 2)**.
// OIDC = OpenID Connect (Giao thức xác thực mở - Mở rộng từ OAuth2)
// OAuth2 = Open Authorization 2.0 (Giao thức ủy quyền mở - Cho phép app truy cập tài nguyên)

### 🧠 3 loại flow phổ biến trong OIDC: (3 loại luồng phổ biến)

| Flow                                   | Mô tả                                                                                               | Dành cho                               |
| -------------------------------------- | --------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **Authorization Code Flow (với PKCE)** | 🔐 FE lấy "code" rồi BE đổi thành token                                                             | Web app, SPA có backend (bảo mật nhất) |
|                                        | // Authorization Code Flow = Luồng mã ủy quyền (FE nhận code, BE đổi code lấy token - Bảo mật nhất) |
|                                        | // PKCE = Proof Key for Code Exchange (Bảo vệ code khỏi bị đánh cắp)                                |
| **Implicit Flow**                      | ⚠️ FE nhận token trực tiếp từ Keycloak                                                              | App cũ (ít dùng vì kém bảo mật)        |
|                                        | // Implicit Flow = Luồng ngầm (FE nhận token trực tiếp - Không an toàn, không nên dùng)             |
| **Client Credentials Flow**            | 🤖 Dành cho BE–BE (service account)                                                                 | Hệ thống vi mô nội bộ                  |
|                                        | // Client Credentials Flow = Luồng xác thực client (BE-BE, không có user - Service account)         |

---

## 🧭 IV. Flow chi tiết: FE → BE → Keycloak

> **Backend-for-Frontend Model (Mô hình Backend cho Frontend - BFF)** - Flow an toàn nhất, được khuyến nghị bởi:
> // BFF = Backend for Frontend (Backend chuyên phục vụ Frontend - Tất cả token ở BE, FE chỉ có cookie)
>
> - 🏦 Ngân hàng (Vietcombank, Techcombank, HSBC…)
> - 🧱 Doanh nghiệp lớn (MoMo, VNG, Grab, Shopee…)
> - 🧩 Các hệ thống microservice (Kiến trúc vi dịch vụ), đa ứng dụng (Nhiều app), có SSO (Đăng nhập 1 lần)

### 🔹 1️⃣ Giai đoạn đăng nhập (Login Flow)

#### 🔸 Các bước:

**(1) FE → BE: `/auth/login`**

- Người dùng click "Login" trên FE.
- FE gửi yêu cầu login tới BE.

**(2) BE → Keycloak: `/realms/momo-ttt/protocol/openid-connect/auth`**

- BE redirect người dùng đến trang đăng nhập Keycloak.
- URL chứa tham số:

```http
# 🌐🔗 Authorization endpoint - bước đầu tiên trong OIDC flow (Điểm cuối ủy quyền - Bước đầu trong luồng OIDC)
response_type=code              # 🎯 Yêu cầu lấy authorization code (không trả token trực tiếp vì bảo mật)
                                # response_type = Loại phản hồi (code = Yêu cầu code, không phải token - Bảo mật hơn)
client_id=portal-frontend       # 🏷️ ID của client app đã đăng ký trong Keycloak realm
                                # client_id = ID ứng dụng (ID của app đã đăng ký trong Keycloak)
redirect_uri=https://be.momo.vn/auth/callback  # 🔙 URL redirect sau khi login thành công (phải whitelist trong Keycloak)
                                # redirect_uri = URL chuyển hướng (URL Keycloak sẽ redirect về sau khi login - Phải đăng ký trước)
code_challenge=XYZ              # 🔐🔑 PKCE code challenge (SHA256 hash của code_verifier - ngăn authorization code interception)
                                # code_challenge = Thử thách PKCE (Hash SHA256 của code_verifier - Bảo vệ code khỏi bị đánh cắp)
code_challenge_method=S256      # ⚙️ Phương thức hash PKCE (S256 = SHA-256, plain không khuyến nghị)
                                # code_challenge_method = Phương thức hash (S256 = SHA-256 - Không dùng plain text)
scope=openid profile email      # 📋 Scope yêu cầu (openid bắt buộc cho OIDC, profile+email cho user info)
                                # scope = Phạm vi quyền (openid = Bắt buộc cho OIDC, profile+email = Thông tin user)
state=random_state_xyz          # 🎲 Random string chống CSRF attack (FE/BE verify sau khi redirect)
                                # state = Chuỗi ngẫu nhiên (Chống tấn công CSRF - FE/BE kiểm tra sau khi redirect)
```

**(3) User → Keycloak:**

- Nhập username/password (hoặc login Google / Microsoft / LDAP).
- Nếu bật MFA → nhập OTP.

**(4) Keycloak → BE: redirect về `BE/callback?code=ABC`**

- Sau khi xác thực thành công, Keycloak gửi code về BE (qua redirect).

**(5) BE → Keycloak: POST `/token`**

BE gọi API `/protocol/openid-connect/token`:

```json
{
  "grant_type": "authorization_code", // 🎯🔄 Kiểu grant - đổi authorization code lấy access token (OAuth2 standard)
  // grant_type = Loại cấp quyền (authorization_code = Đổi code lấy token - Chuẩn OAuth2)
  "code": "ABC", // 🎫📝 Authorization code nhận được từ Keycloak (1 lần dùng, hết hạn sau 60s)
  // code = Mã ủy quyền (Code nhận được từ Keycloak - Chỉ dùng 1 lần, hết hạn sau 60 giây)
  "client_id": "portal-frontend", // 🏷️ Client ID (bắt buộc ngay cả khi có client_secret)
  // client_id = ID ứng dụng (Bắt buộc phải có)
  "client_secret": "********", // 🔐🔒 Secret của confidential client (KHÔNG bao giờ để ở FE, chỉ BE giữ)
  // client_secret = Mật khẩu ứng dụng (KHÔNG BAO GIỜ để ở Frontend, chỉ Backend giữ)
  "redirect_uri": "https://be.momo.vn/auth/callback", // 🔙✅ Phải trùng CHÍNH XÁC với redirect_uri trong authorize request
  // redirect_uri = URL chuyển hướng (Phải TRÙNG CHÍNH XÁC với lúc authorize)
  "code_verifier": "XYZ" // 🔑🛡️ PKCE code verifier - Keycloak hash và so sánh với code_challenge (ngăn MITM attack)
  // code_verifier = Xác minh PKCE (Keycloak hash và so sánh với code_challenge - Chống tấn công MITM)
}
```

Keycloak trả:

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...", // 🎫🔑 JWT Access Token - gửi kèm mỗi API request (Bearer token), hết hạn nhanh (5-10 phút)
  // access_token = Token truy cập (JWT - Gửi kèm mỗi API request, hết hạn nhanh 5-10 phút)
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...", // 🔄💾 Refresh Token - lấy access_token mới khi hết hạn (15-60 phút), chỉ BE giữ trong Redis
  // refresh_token = Token làm mới (Dùng để lấy access_token mới khi hết hạn, chỉ BE giữ trong Redis)
  "id_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...", // 🎫👤 ID Token (OIDC) - chứa thông tin user (sub, name, email, roles), FE có thể decode để hiển thị
  // id_token = Token ID (Chứa thông tin user - sub=user ID, name, email, roles - FE có thể decode)
  "token_type": "Bearer", // 🏷️ Loại token - dùng trong Authorization header: "Bearer {access_token}"
  // token_type = Loại token (Bearer = Dùng trong header: "Bearer {access_token}")
  "expires_in": 300, // ⏱️⏰ Access token hết hạn sau 300 giây (5 phút) - FE/BE phải refresh trước khi hết hạn
  // expires_in = Thời gian hết hạn (300 giây = 5 phút - Phải refresh trước khi hết hạn)
  "refresh_expires_in": 1800, // 🔄⏱️ Refresh token hết hạn sau 1800 giây (30 phút)
  // refresh_expires_in = Thời gian hết hạn refresh token (1800 giây = 30 phút)
  "scope": "openid profile email" // 📋 Scope được cấp (có thể ít hơn scope request nếu user không consent)
  // scope = Phạm vi quyền được cấp (Có thể ít hơn scope yêu cầu nếu user không đồng ý)
}
```

**(6) BE → FE: Set cookie HTTP-only (session)**

- BE lưu `refresh_token` vào Redis (server-side).
- BE trả FE một cookie HTTP-only chứa session ID (không đọc được bằng JS).
- FE **không có** `access_token` / `refresh_token`.

**(7) FE → BE: gọi API `/user/profile`**

- Cookie gửi kèm mỗi request.
- BE tra session → lấy `access_token` → xác thực → trả dữ liệu.

---

### 🔹 2️⃣ Giai đoạn refresh token

```javascript
// 🔹 Bước 1: Access token hết hạn sau 300 giây (5 phút)
// ⏰❌ BE nhận biết access_token đã expired (check exp claim trong JWT)
// expired = Hết hạn (Token đã hết hạn - BE kiểm tra exp claim trong JWT)
// exp claim = Trường hết hạn (Trường trong JWT cho biết thời gian hết hạn)

// 🔹 Bước 2: FE → BE: /auth/refresh
// 🔄📤 FE gọi request với cookie HTTP-only chứa session ID
// HTTP-only cookie = Cookie chỉ đọc được bởi server (Không đọc được bằng JavaScript - Bảo mật)
// session ID = ID phiên (ID để BE tìm refresh_token trong Redis)

// 🔹 Bước 3: BE → Keycloak: POST /token
POST /protocol/openid-connect/token
{
  grant_type: "refresh_token",           // 🔄🎯 Grant type cho refresh flow
                                         // grant_type = Loại cấp quyền (refresh_token = Làm mới token)
  refresh_token: "<from_redis>",         // 💾🔑 Lấy refresh token từ Redis theo session ID
                                         // refresh_token = Token làm mới (Lấy từ Redis theo session ID)
  client_id: "portal-frontend",         // 🏷️ Client ID
                                         // client_id = ID ứng dụng
  client_secret: "********"              // 🔐🔒 Client secret (confidential client)
                                         // client_secret = Mật khẩu ứng dụng (Chỉ confidential client có)
}

// 🔹 Bước 4: Keycloak → BE: trả new tokens
// ✅🎫 Keycloak trả access_token mới + refresh_token mới (Token Rotation)
// Token Rotation = Xoay token (Mỗi lần refresh, token mới được tạo)
// ❌🚫 Refresh token cũ bị vô hiệu hóa ngay lập tức (chống reuse attack)
// reuse attack = Tấn công tái sử dụng (Hacker dùng token cũ - Token rotation ngăn điều này)

// 🔹 Bước 5: BE update Redis, trả FE cookie mới
// 💾🔄 BE lưu refresh_token mới vào Redis, xoá token cũ
// Redis = Cơ sở dữ liệu bộ nhớ (Lưu refresh_token nhanh)
// 🍪✅ Trả về FE cookie HTTP-only mới (update session)
// cookie mới = Cookie mới (Cập nhật session cho FE)
```

> ⚙️ Sử dụng **Refresh Token Rotation** – mỗi lần refresh, token cũ bị vô hiệu hóa → chống reuse.

---

### 🔹 3️⃣ Giai đoạn logout (Single Logout)

```javascript
// 🔹 Bước 1: FE → BE: /auth/logout
// 🚪📤 User click logout, FE gọi request tới BE với cookie session
// logout = Đăng xuất (User muốn thoát khỏi hệ thống)

// 🔹 Bước 2: BE → Keycloak: GET/POST /logout
GET /realms/<realm>/protocol/openid-connect/logout
// realm = Vùng quản lý (Tên realm trong Keycloak)
?id_token_hint=<id_token>              // 🎫👤 ID token để Keycloak biết user nào logout
                                       // id_token_hint = Gợi ý token ID (Keycloak biết user nào logout)
&post_logout_redirect_uri=https://fe.app/logout-success  // 🔙🎯 Redirect sau khi logout xong
                                       // post_logout_redirect_uri = URL chuyển hướng sau logout (Redirect về FE)
&refresh_token=<refresh_token>         // 🔄❌ Gửi refresh token để Keycloak revoke (optional)
                                       // refresh_token = Token làm mới (Gửi để Keycloak vô hiệu hóa - Tùy chọn)
                                       // revoke = Vô hiệu hóa (Làm cho token không còn hiệu lực)

// 🔹 Bước 3: Keycloak xoá SSO session
// ❌💾 Keycloak xoá session của user trong database
// SSO session = Phiên đăng nhập một lần (Session cho phép login 1 lần dùng nhiều app)
// ❌🎫 Vô hiệu hoá tất cả access_token và refresh_token liên quan
// Vô hiệu hóa = Làm cho không còn hiệu lực (Token không còn dùng được)

// 🔹 Bước 4: Keycloak broadcast "backchannel logout"
// 📡🚪 Keycloak gửi POST request tới tất cả ứng dụng khác user đang login
// broadcast = Phát sóng (Gửi đến tất cả)
// backchannel logout = Logout kênh ngầm (Keycloak gửi logout event đến các app khác)
// 📤🚫 Từng app nhận logout event → xoá session local của user
// logout event = Sự kiện logout (App nhận được thông báo user đã logout)
// ✅🌐 Đảm bảo Single Logout (SLO) - logout toàn hệ thống
// SLO = Single Logout (Logout một lần, logout tất cả app)

// 🔹 Bước 5: BE + FE xoá session/cookie
// 💾❌ BE xoá refresh_token khỏi Redis
// Redis = Cơ sở dữ liệu bộ nhớ (Xóa refresh_token khỏi Redis)
// 🍪❌ BE xoá cookie HTTP-only (Set-Cookie với Max-Age=0)
// Max-Age=0 = Thời gian sống = 0 (Cookie sẽ bị xóa ngay)
// 💻❌ FE xoá local session/state, redirect về login page
// local session = Phiên đăng nhập local (Xóa thông tin đăng nhập ở FE)
```

> 🧠 Giúp logout toàn hệ thống (nếu user đang đăng nhập ở nhiều app, tất cả cùng bị logout).

---

### 🔹 4️⃣ Giai đoạn token exchange (cross-realm / microservice)

Khi cần gọi sang hệ thống khác (ví dụ realm khác hoặc microservice khác):

```javascript
// 🔹 Bước 1: BE gọi microservice nhưng KHÔNG gửi user token gốc
// 🚫🔐 KHÔNG forward user access_token trực tiếp (rủi ro PII leak, quyền quá rộng)
// forward = Chuyển tiếp (Không chuyển tiếp token gốc)
// PII leak = Rò rỉ thông tin cá nhân (Personal Identifiable Information - Thông tin nhận dạng cá nhân)
// quyền quá rộng = Quyền quá nhiều (Token có quá nhiều quyền - Nguy hiểm nếu bị lộ)

// 🔹 Bước 2: BE → Keycloak: /token (grant_type=token_exchange)
POST /protocol/openid-connect/token
{
  grant_type: "urn:ietf:params:oauth:grant-type:token-exchange",  // 🔄🔗 Token Exchange grant type (RFC 8693)
                                                                  // grant_type = Loại cấp quyền (token-exchange = Đổi token - Chuẩn RFC 8693)
  subject_token: "<user_access_token>",                          // 🎫👤 Token gốc của user
                                                                  // subject_token = Token chủ thể (Token gốc của user)
  subject_token_type: "urn:ietf:params:oauth:token-type:access_token",
                                                                  // subject_token_type = Loại token chủ thể (access_token = Token truy cập)
  requested_token_type: "urn:ietf:params:oauth:token-type:access_token",  // 🎯 Yêu cầu access token mới
                                                                  // requested_token_type = Loại token yêu cầu (access_token mới)
  audience: "trading-service",                                   // 🎯💻 Service cần gọi (giới hạn scope chỉ cho service này)
                                                                  // audience = Đối tượng (Service nào sẽ nhận token - Giới hạn quyền)
  client_id: "portal-backend",                                   // 🏷️ Client gọi request
                                                                  // client_id = ID ứng dụng (Backend gọi request)
  client_secret: "********"                                       // 🔐🔒 Secret của backend client
                                                                  // client_secret = Mật khẩu ứng dụng (Secret của backend)
}

// 🔹 Bước 3: Keycloak kiểm tra policy → trả token mới
// ✅🔍 Keycloak check Token Exchange Policy (ai được đổi token cho service nào)
// Token Exchange Policy = Chính sách đổi token (Quy tắc ai được đổi token cho service nào)
// 🎫⬇️ Trả về service_access_token với scope giảm (chỉ quyền tối thiểu cho trading-service)
// service_access_token = Token truy cập dịch vụ (Token mới với quyền giảm)
// scope giảm = Phạm vi quyền giảm (Chỉ quyền tối thiểu cần thiết)
// 🔒👤 Service token không chứa PII của user, chỉ chứa user ID + role cần thiết
// PII = Personal Identifiable Information (Thông tin nhận dạng cá nhân - Không chứa trong service token)
// 🌐✅ Hỗ trợ SSO cross-realm - giữ danh tính user nhưng tăng bảo mật
// cross-realm = Xuyên realm (Giữa các realm khác nhau - Vẫn giữ danh tính user)
```

> Dùng để ủy quyền chéo giữa hệ thống mà vẫn giữ được danh tính người dùng (SSO thật sự).

---

## 🧠 V. Giải thích chi tiết các loại token

| Token             | Vai trò                                                                           | Thời hạn              | Ai giữ     |
| ----------------- | --------------------------------------------------------------------------------- | --------------------- | ---------- |
| **Access Token**  | 🎫 Cho phép truy cập API                                                          | Ngắn (5–10 phút)      | BE         |
|                   | // Access Token = Token truy cập (Dùng để gọi API - Hết hạn nhanh)                |
| **Refresh Token** | 🔄 Dùng để lấy token mới                                                          | Dài (15–60 phút)      | BE (Redis) |
|                   | // Refresh Token = Token làm mới (Dùng để lấy access_token mới - Hết hạn lâu hơn) |
| **ID Token**      | 👤 Thông tin người dùng (name, email, role...)                                    | Ngắn                  | BE         |
|                   | // ID Token = Token ID (Chứa thông tin user - name, email, role)                  |
| **Session**       | ⏱️ Theo dõi người dùng login ở app nào                                            | Được Keycloak quản lý | Keycloak   |
|                   | // Session = Phiên đăng nhập (Keycloak theo dõi user đã login ở app nào)          |

> 💡 **Tất cả token đều là JWT (JSON Web Token - Token dạng JSON)**, có thể xác minh bằng public key (JWKS - Bộ khóa công khai) mà không cần gọi Keycloak mỗi lần.
> // JWT = JSON Web Token (Token dạng JSON - Có thể xác minh mà không cần gọi Keycloak)
> // JWKS = JSON Web Key Set (Bộ khóa công khai - Dùng để xác minh JWT)

---

## 🧩 VI. Cơ chế bảo mật trong flow FE → BE → Keycloak

| Cơ chế                                 | Mục đích                                                                                              | Ghi chú                      |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------- | ---------------------------- |
| **PKCE** (Proof Key for Code Exchange) | 🔐 Ngăn hacker lấy cắp code trong redirect URL                                                        | Bắt buộc cho public client   |
|                                        | // PKCE = Bằng chứng khóa cho trao đổi code (Chống đánh cắp code trong URL)                           |
| **HTTPS (TLS 1.3)**                    | 🔒 Mã hóa dữ liệu giữa FE–BE–Keycloak                                                                 | Tất cả request               |
|                                        | // HTTPS = HTTP Secure (Mã hóa dữ liệu - TLS 1.3 = Giao thức bảo mật phiên bản 1.3)                   |
| **HTTP-only cookie**                   | 🚫 FE không đọc được token bằng JS                                                                    | Ngăn XSS                     |
|                                        | // HTTP-only cookie = Cookie chỉ đọc được bởi server (Ngăn XSS - Tấn công script chéo)                |
| **CSRF Token**                         | 🛑 Chống request giả mạo                                                                              | FE gửi kèm                   |
|                                        | // CSRF = Cross-Site Request Forgery (Tấn công giả mạo request - Token chống điều này)                |
| **Refresh Token Rotation**             | 🔄 Token chỉ dùng 1 lần                                                                               | Bật trong Keycloak           |
|                                        | // Refresh Token Rotation = Xoay token làm mới (Token chỉ dùng 1 lần - Chống tái sử dụng)             |
| **MFA / OTP**                          | 🔐 Tăng lớp xác thực                                                                                  | Dùng Keycloak OTP Policy     |
|                                        | // MFA = Multi-Factor Authentication (Xác thực đa yếu tố), OTP = One-Time Password (Mật khẩu một lần) |
| **Token Exchange Policy**              | 🔗 Giới hạn quyền truy cập giữa các realm                                                             | Giảm rủi ro lateral movement |
|                                        | // Token Exchange Policy = Chính sách đổi token (Giới hạn quyền giữa các realm)                       |
|                                        | // lateral movement = Di chuyển ngang (Hacker di chuyển giữa các hệ thống)                            |
| **Audit Logging**                      | 📊 Ghi lại toàn bộ login / logout / token exchange                                                    | Phục vụ audit ngân hàng      |
|                                        | // Audit Logging = Ghi log kiểm toán (Ghi lại tất cả hoạt động - Phục vụ kiểm toán)                   |

---

## ⚖️ VII. Ưu – Nhược điểm

### ✅ Ưu điểm:

- ✅ Bảo mật theo chuẩn quốc tế (OIDC/OAuth2/SAML2)
- ✅ Hỗ trợ SSO/SLO toàn hệ thống => Đăng nhập một lần, dùng được nhiều ứng dụng
- ✅ Dễ tích hợp với các công nghệ: React, NestJS, Spring, .NET
- ✅ Có Admin UI, REST API, audit log đầy đủ
- ✅ Mở rộng dễ dàng qua Realm, Role, Group, Policy
- ✅ Có thể federated với LDAP / Google / Microsoft

### ❌ Nhược điểm:

- ❌ Cần hiểu rõ OAuth2/OIDC để triển khai đúng
- ❌ Cấu hình phức tạp (Realm, Redirect URI, Secret, CORS…)
- ❌ Docker nặng, cần tài nguyên RAM (2–4GB)
- ❌ Với quy mô lớn cần caching layer (Redis) và HA setup (cluster)

---

## 🧭 VIII. Tóm tắt sơ đồ

```
Frontend (React)
      │
      │ 1. /auth/login
      ▼
Backend (NestJS)
      │
      │ 2. redirect /authorize
      ▼
Keycloak
      │ 3. User login (password / OTP)
      │ 4. return ?code
      ▼
Backend
      │ 5. exchange code → tokens
      │ 6. set session cookie (HTTP-only)
      ▼
Frontend
      │ 7. call API with cookie
      ▼
Backend verify via JWKS
```

> 💎 **Đây là flow tối ưu nhất cho hệ thống có yêu cầu bảo mật cao (ngân hàng, fintech, tài chính, chính phủ…).**

---

## 🔐 IX. Keycloak SSO – Cách hoạt động chuyên sâu

> **Chuẩn ngân hàng**

Keycloak hỗ trợ SSO theo chuẩn **OpenID Connect Session Management (Quản lý phiên OpenID Connect)** và **SAML2 Web SSO (SSO Web SAML2)**.
// SSO = Single Sign-On (Đăng nhập một lần)
// OpenID Connect Session Management = Quản lý phiên OpenID Connect (Chuẩn quản lý phiên)
// SAML2 = Security Assertion Markup Language 2 (Ngôn ngữ khẳng định bảo mật - Chuẩn SSO)

Dựa trên mô hình:

- 🔹 1 user login → dùng cho nhiều ứng dụng (1 người dùng đăng nhập → dùng được nhiều app)
- 🔹 Session được Keycloak quản lý tập trung (Session được quản lý tập trung bởi Keycloak)
- 🔹 Logout 1 nơi → toàn bộ ứng dụng logout (SLO) (Logout 1 chỗ → tất cả app logout - SLO)
  // SLO = Single Logout (Logout một lần - Logout tất cả app)

### 🔥 1️⃣ SSO hoạt động chi tiết

**(1) FE → BE → Keycloak login**

User được redirect đến:

```http
# 🌐🔐 OIDC Authorization endpoint cho SSO
GET /realms/<realm>/protocol/openid-connect/auth
?client_id=app1-frontend                  # 🏷️🎉 App thứ nhất user login
&response_type=code                       # 🎯 Authorization Code Flow
&redirect_uri=https://app1.com/callback   # 🔙 Callback URI của app1
&scope=openid profile email               # 📋 Scope yêu cầu
```

Keycloak tạo SSO session:

```javascript
// ✅💾 User login thành công → Keycloak tạo SSO session trong database
// User login thành công = Người dùng đăng nhập thành công
// SSO session = Phiên đăng nhập một lần (Session cho phép login 1 lần dùng nhiều app)
SSO Session ID: "5ae2a02c-b3d0-4b79-bc23-..."  // 🎫🔑 Unique session ID cho user
// SSO Session ID = ID phiên SSO (ID duy nhất cho user - Dùng để theo dõi phiên)
// 🍪🔐 Keycloak set cookie "KEYCLOAK_SESSION" vào browser (domain: keycloak.company.com)
// set cookie = Thiết lập cookie (Keycloak đặt cookie vào trình duyệt)
// KEYCLOAK_SESSION = Tên cookie (Cookie chứa thông tin phiên SSO)
// domain = Tên miền (Cookie chỉ hoạt động trong domain này)
// 💾 Session lưu: user_id, realm, client_ids đã login, timestamp
// user_id = ID người dùng (ID của user đã login)
// realm = Vùng quản lý (Realm user thuộc về)
// client_ids = ID các ứng dụng (Danh sách app user đã login)
// timestamp = Dấu thời gian (Thời điểm tạo session)
// ⏰ Session timeout: 15-30 phút (internal) hoặc 60 phút (external)
// Session timeout = Thời gian hết hạn phiên (15-30 phút cho nội bộ, 60 phút cho bên ngoài)
// internal = Nội bộ (Nhân viên công ty)
// external = Bên ngoài (Khách hàng)
```

**(2) Khi user mở thêm ứng dụng thứ 2**

```javascript
// 🎉💻 User mở App2 (ví dụ: trading.company.com) và click "Login"
// 🔹 Bước 1: App2 → BE2 → redirect tới Keycloak
GET /realms/<realm>/protocol/openid-connect/auth
?client_id=app2-frontend                  # 🏷️🎯 App thứ 2 (khác app1)
&response_type=code
&redirect_uri=https://app2.com/callback   # 🔙 Callback URI của app2

// 🔹 Bước 2: Keycloak check SSO session
// 🔍🍪 Keycloak đọc cookie "KEYCLOAK_SESSION" từ browser
// ✅💾 Tìm thấy SSO session còn tồn tại (chưa timeout) → user đã login rồi!

Keycloak thấy session user còn tồn tại:
  ➡️ ✅🎯 KHÔNG cần nhập lại username/password (SSO magic!)
  ➡️ 🎫✅ Keycloak trả trực tiếp Authorization Code cho App2
  ➡️ 🔄🎫 BE2 đổi code → access_token + refresh_token của App2
  ➡️ 💾 Keycloak update SSO session: thêm app2 vào danh sách clients đã login
```

> ✅ **Người dùng đăng nhập một lần, dùng được toàn hệ thống.**

**(3) Logout App1 → Keycloak → Logout toàn hệ thống**

Khi logout:

```http
BE → Keycloak:
/logout?id_token_hint=...&refresh_token=...
```

Keycloak:

- Xóa session gốc
- Gửi backchannel logout đến từng client đã đăng nhập
- BE xoá cookie
- FE xoá session

> 👉 Đảm bảo **Single Logout (SLO)** toàn bộ apps.

---

## 🔐 X. Đồng bộ tài khoản nhân viên (LDAP/AD → Keycloak)

Ngân hàng và các tập đoàn lớn không tạo user trực tiếp trong Keycloak mà dùng **Identity Federation**:

### 🔹 Identity Provider:

- LDAP (OpenLDAP)
- Active Directory / Azure AD
- Microsoft Entra ID

### 🔥 1️⃣ Flow Employee Sync (Đồng bộ nhân viên)

```
Keycloak → Identity Provider → tự động:
  - Lấy thông tin user từ LDAP/AD
  - Đồng bộ password (hoặc pass-through)
  - Đồng bộ group (department, branch)
  - Đồng bộ role (manager, teller, risk, audit)
```

### 🔥 2️⃣ Có 2 mode:

#### **(A) Import Mode**

Keycloak copy thông tin user về database của mình.

**✔️ Ưu điểm:**

- Keycloak hoạt động ngay cả khi LDAP/AD tạm lỗi
- Tốc độ nhanh, truy cập local
- Có thể thêm attribute/role riêng ở Keycloak

**✖️ Nhược điểm:**

- User thay đổi mật khẩu ở LDAP phải đồng bộ lại
- Có độ trễ sync 5-10 phút

#### **(B) Pass-Through Authentication**

User login tại Keycloak → Keycloak gửi password sang LDAP/AD kiểm tra.

**✔️ Ưu điểm:**

- Không lưu password ở Keycloak
- Password thay đổi phản ánh ngay
- Đạt chuẩn ISO 27001 / PCI-DSS

**✖️ Nhược điểm:**

- Keycloak phụ thuộc LDAP/AD uptime

---

## 🔐 XI. 2 Flow Đăng Nhập: Internal vs External

> **Chuẩn Ngân hàng**

### 🟦 1️⃣ External Users (Khách hàng) – Chuẩn Fintech / Banking

External users (khách hàng cá nhân/doanh nghiệp) luôn được xác thực qua Keycloak trực tiếp.

#### 📌 Lý do bảo mật:

- Tách biệt hoàn toàn với nội bộ (ngăn xâm nhập lateral)
- Áp dụng MFA/OTP theo chuẩn PCI-DSS
- Hỗ trợ KYC, eKYC, risk scoring
- Dễ scale theo lượng user lớn (10M – 50M)

#### 🧭 External Login Flow (chuẩn nhất)

```
FE → BE → Keycloak → OTP/MFA → Token → FE/BE
```

#### 🔥 Cấu hình cần thiết:

- OTP (TOTP / SMS OTP / Smart OTP)
- Brute Force Detector
- Refresh Token Rotation
- HTTP-only Cookie (BE session based)
- Fine-grained CORS + Client Roles
- Read-only Realm (không tự tạo user)

---

### 🟩 2️⃣ Internal Users (Nhân viên) – Chuẩn Enterprise IAM

Nhân viên ngân hàng phải:

- Login bằng tài khoản AD/LDAP
- Có MFA (Hard Token hoặc Smart-card)
- Role theo phòng ban, chi nhánh, chức vụ
- Audit bắt buộc đầy đủ 100% (SIEM integration)

#### Hai hướng triển khai chuẩn:

#### 🟢 Flow A – Internal Login Trực Tiếp FE → Keycloak (OIDC + PKCE)

Tốt nhất cho Portal nội bộ / ứng dụng web chuẩn.

**Flow:**

```
FE → Keycloak (login redirect)
Keycloak → LDAP/AD (check password)
Keycloak → FE (code)
FE → BE (send code)
BE → Keycloak (exchange token)
BE set session cookie
```

**✔️ Ưu:**

- Nhanh – đơn giản – phù hợp app nội bộ có browser.

**✖️ Nhược:**

- Không dùng được cho ứng dụng legacy hoặc desktop app.

---

#### 🔵 Flow B – Internal Login FE → BE → Keycloak (Managed by BE)

Flow chuẩn nhất cho ngân hàng lớn.

- Tất cả token nằm ở BE.
- FE chỉ có cookie HTTP-only.
- Không rò rỉ token lên trình duyệt.

**✔️ Ưu:**

- Bảo mật tối đa (token không vào browser)
- BE kiểm soát session, refresh, revoke
- Phù hợp Microservices
- Tích hợp SIEM dễ hơn
- Triển khai Zero-Trust dễ

**✖️ Nhược:**

- BE phức tạp hơn
- Cần Redis cache session + JWKS rotate

---

### 🟣 Internal Security Policies bắt buộc có:

| Vấn đề                 | Giải pháp                          |
| ---------------------- | ---------------------------------- |
| **Password & MFA**     | AD kiểm soát, Keycloak federated   |
| **SSO**                | SSO bằng SSO Session Keycloak      |
| **Session Hijack**     | Cookie HTTP-only + SameSite=Strict |
| **CSRF**               | Anti-CSRF Token ký bằng HMAC       |
| **Replay Attack**      | PKCE + Refresh Token Rotation      |
| **Brute Force**        | Keycloak brute-force protection    |
| **Audit & Monitoring** | Export log sang Splunk/ELK         |

---

## 🔐 XII. So sánh Internal vs External Flow

> **Chuẩn ngân hàng**

| Tiêu chí           | Internal (Nhân viên)      | External (Khách hàng)  |
| ------------------ | ------------------------- | ---------------------- |
| **Identity**       | LDAP/AD                   | Keycloak DB / CRM      |
| **Federation**     | Bắt buộc                  | Không hoặc optional    |
| **SSO**            | Có                        | Có                     |
| **MFA**            | Smart Card, TOTP          | OTP/SMS/Auth App       |
| **Token Location** | BE                        | BE                     |
| **Session**        | NGHIÊM NGẶT, timeout ngắn | Timeout dài hơn        |
| **Role**           | Department-based          | Product-based          |
| **Audit**          | 100%, SIEM bắt buộc       | Chỉ bắt buộc giao dịch |
| **Token Exchange** | Nhiều                     | Ít                     |
| **Security Level** | Cấp cao nhất              | Cao                    |

---

## 🔐 XIII. Vấn đề thường gặp & Cách giải quyết

### ✔️ 1. Role/Group không đồng bộ từ AD → Keycloak

**→ Giải pháp:**

- Dùng LDAP Mapper
- Hoặc Sync Mode: Force / Periodic (5 phút)

### ✔️ 2. SSO không logout toàn hệ thống

**→ Giải pháp:**

- Phải bật Backchannel Logout (không dùng front-channel)

### ✔️ 3. Client secret bị lộ

**→ Giải pháp:**

- Internal apps nên dùng confidential client + BE exchange code
- Không bao giờ để secret ở FE

### ✔️ 4. Token bị lộ qua localStorage

**→ Giải pháp:**

- Không được lưu `access_token` trên FE
- Chỉ dùng cookie HTTP-only + BE session

### ✔️ 5. Cross-realm integration phức tạp

**→ Giải pháp:**

- Dùng Token Exchange Policy
- Áp dụng cho liên kết giữa các hệ thống ngân hàng core

---

## 🧩 XIV. Phân chia Realm tối ưu

> **Cho hệ thống ngân hàng / tài chính / chứng khoán**

### 🎯 Mục tiêu chính của tách Realm:

- Isolate (cô lập) dữ liệu người dùng
- Tách biệt đối tượng: internal vs external vs service
- Tách biệt môi trường: portal nội bộ / app khách hàng / dịch vụ nội bộ / hệ thống chứng khoán
- Giảm rủi ro lateral movement nếu 1 realm bị xâm nhập
- Tối ưu hóa SSO
- Phân quyền & policy riêng biệt

### 🟦 1. Mô hình phân chia Realm khuyến nghị

```plaintext
# 🏛️ Kiến trúc Realm tách biệt theo đối tượng và hệ thống

├── REALM_INTERNAL             # 👥🏛️ Realm cho nhân viên nội bộ (AD/LDAP federated)
│     ├── client_portal_fe      # 💻 Portal frontend (React/Vue)
│     ├── client_portal_be      # ⚙️ Portal backend (NestJS/Spring)
│     ├── role-based:           # 🎯 Roles theo chức vụ
│     │     ├── teller            # 💵 Giao dịch viên (quyền giao dịch cơ bản)
│     │     ├── auditor           # 🔍 Kiểm toán (read-only, full audit log)
│     │     ├── risk              # 🚨 Quản lý rủi ro (risk dashboard, alerts)
│     │     └── manager           # 👔 Quản lý chi nhánh (approve, reports)
│     ├── 🔐🔒 MFA: bắt buộc (Smart Card, TOTP)
│     ├── 🌐🚫 IP Restriction: chỉ IP công ty
│     └── 📊 Audit: 100% SIEM (Splunk/ELK)
│
├── REALM_EXTERNAL             # 👤🌎 Realm cho khách hàng (Keycloak DB hoặc CRM)
│     ├── client_mobile_app     # 📱 Mobile app (React Native/Flutter)
│     ├── client_web_app        # 🌐 Web app (Next.js/Angular)
│     ├── role-based:           # 🎯 Roles theo sản phẩm
│     │     ├── customer-normal   # 👤 Khách hàng thường (basic features)
│     │     ├── vip               # 🌟 VIP khách hàng (premium features, priority)
│     │     └── business          # 🏛️ Doanh nghiệp (bulk operations)
│     ├── 🔐📱 MFA: OTP/SMS/TOTP (optional cho normal, bắt buộc cho VIP)
│     ├── 🌐✅ IP: không giới hạn (global access)
│     └── 📊 Audit: chỉ giao dịch quan trọng
│
├── REALM_FUNDS_SERVICE        # 💰⚙️ Realm cho dịch vụ tài chính/quỹ
│     ├── microservice-fund-a   # 💼 Quỹ A (service account, client credentials)
│     ├── microservice-fund-b   # 💼 Quỹ B
│     ├── 🔐 Client type: confidential, bearer-only
│     └── 🔗 Token Exchange: enabled (cross-realm allowed)
│
├── REALM_TRADING_SERVICE      # 📊🏛️ Realm cho core chứng khoán
│     ├── trading-engine        # ⚡ Engine giao dịch chứng khoán
│     ├── settlement-service    # 💵 Dịch vụ thanh toán
│     ├── price-stream-service  # 📈 Stream giá real-time
│     ├── 🔐🎯 Zero-Trust: mỗi service có token riêng, scope giới hạn
│     └── 🌐🚫 IP DMZ only (không public internet)
│
└── REALM_ADMIN                # 🔧🔐 Realm quản trị hệ thống
      ├── client-admin-console  # 🖥️ Keycloak Admin Console
      ├── client-reporting      # 📊 Hệ thống báo cáo
      ├── 🔐🔑 MFA: bắt buộc 2FA + IP whitelist
      └── 📊 Audit: 100% full logging
```

### ✔️ Ưu điểm:

- Block lateral movement giữa Internal – External – Trading
- Policy rõ ràng: internal không thể dùng token external và ngược lại
- Audit dễ truy vết theo từng realm
- Mỗi realm có thể scale độc lập
- Bảo vệ dữ liệu PII khách hàng

### ❌ Không nên:

- ❌ Gộp tất cả vào 1 realm → rủi ro bảo mật cực lớn

---

## 🧩 XV. Phân quyền (Role/Group/Scope)

> **Theo chuẩn ngân hàng**

### 1. RBAC (Role-based - Dựa trên vai trò) – vai trò theo chức vụ

// RBAC = Role-Based Access Control (Kiểm soát truy cập dựa trên vai trò - Phân quyền theo role)

#### Ví dụ Internal:

```javascript
// 🎯👥 Roles cho nhân viên ngân hàng/chứng khoán
teller; // 💵👤 Giao dịch viên (transaction:create, account:read)
branch_manager; // 🏛️👔 Trưởng chi nhánh (approve:transaction, reports:branch, users:manage)
ops_manager; // ⚙️👔 Quản lý vận hành (system:config, workflow:manage, bulk:operations)
risk_officer; // 🚨🔍 Quản lý rủi ro (risk:view, alerts:manage, reports:risk, users:investigate)
auditor; // 🔍📊 Kiểm toán (logs:view:all, reports:audit, read-only everything)
it_support; // 🔧💻 CNTT (system:support, users:reset-password, debug:access)

// 📋 Mỗi role có permissions map:
// teller -> ["transaction:create", "account:read", "customer:search"]
// auditor -> ["*:read", "logs:view", "reports:*"] (read-only tất cả)
```

#### External:

```javascript
// 🎯👤 Roles cho khách hàng
customer; // 👤✅ Khách hàng thường (account:view, transaction:basic, transfer:limit-1M)
vip_customer; // 🌟💰 VIP (transaction:premium, transfer:limit-10M, priority:support)
business_customer; // 🏛️💼 Doanh nghiệp (bulk:transfer, payroll:manage, api:access, reports:advanced)
broker; // 📈💹 Môi giới chứng khoán (trading:execute, portfolio:manage, market:data:realtime)

// 📋 Permission mapping:
// customer -> ["account:view", "transaction:self", "transfer:max:1000000"]
// broker -> ["trading:*", "portfolio:*", "market:realtime", "reports:trading"]
```

---

### 2. ABAC (Attribute-based - Dựa trên thuộc tính) – vai trò theo thuộc tính

// ABAC = Attribute-Based Access Control (Kiểm soát truy cập dựa trên thuộc tính - Phân quyền theo attribute)

| Attribute          | Ý nghĩa                                                                          |
| ------------------ | -------------------------------------------------------------------------------- |
| `branch=700`       | Chi nhánh 700                                                                    |
|                    | // branch = Chi nhánh (Thuộc tính chi nhánh)                                     |
| `region=NORTH`     | Miền Bắc                                                                         |
|                    | // region = Vùng (Thuộc tính vùng địa lý)                                        |
| `level=4`          | Cấp lãnh đạo                                                                     |
|                    | // level = Cấp độ (Thuộc tính cấp bậc)                                           |
| `kyc_level=3`      | Hoàn thành định danh cấp 3                                                       |
|                    | // kyc_level = Cấp độ định danh (Know Your Customer - Mức độ xác minh danh tính) |
| `risk_score <= 50` | Rủi ro thấp                                                                      |
|                    | // risk_score = Điểm rủi ro (Thuộc tính đánh giá rủi ro)                         |

> 💡 ABAC giúp kiểm soát truy cập theo dữ liệu, không chỉ theo vai trò.
> // ABAC = Phân quyền linh hoạt hơn (Dựa trên thuộc tính cụ thể, không chỉ role)

---

### 3. Scope-based / Permission-based

Dùng khi bạn muốn phân quyền chi tiết theo API.

**Ví dụ:**

```
account:read
account:update
transaction:approve
trading:buy
trading:sell
portfolio:view
report:download
```

---

### 4. Policy-based

Keycloak hỗ trợ:

```javascript
// 🎯🔐 Các loại Policy trong Keycloak Authorization Services

// 1️⃣ 🎯 Role-based Policy
// Nếu user có role "risk_officer" -> cho phép truy cập risk dashboard
{
  type: "role",
  logic: "POSITIVE",              // ✅ Phải có role
  roles: ["risk_officer"],         // 🎯 Danh sách role yêu cầu
  description: "Allow risk officers only"  // 📝 Mô tả
}

// 2️⃣ 🏷️ Client-based Policy
// Chỉ cho phép client "trading-app" truy cập trading API
{
  type: "client",
  clients: ["trading-app", "mobile-app"],  // 📱💻 Danh sách client cho phép
  logic: "POSITIVE"                        // ✅ Phải từ client này
}

// 3️⃣ 👤🏷️ User Attribute Policy
// Chỉ cho nhân viên "branch=700" truy cập dữ liệu chi nhánh 700
{
  type: "user-attribute",
  attributes: {
    branch: "700",                         // 🏛️ Chi nhánh 700
    department: "risk"                     // 🚨 Phòng rủi ro
  },
  logic: "POSITIVE"                        // ✅ Phải match tất cả attributes
}

// 4️⃣ 👥 Group-based Policy
// Chỉ cho thành viên group "senior-management"
{
  type: "group",
  groups: ["/senior-management", "/board-of-directors"],  // 🎯👥 Hierarchical groups
  extendChildren: true                     // ✅ Bao gồm sub-groups
}

// 5️⃣ 🔧📋 JavaScript Logic Policy (custom logic)
function canAccess(context) {
  var user = context.identity.attributes;  // 👤 Lấy attributes của user
  var riskScore = user.risk_score[0];      // 🚨 Risk score của user

  // ✅ Chỉ cho user có risk_score <= 50
  if (riskScore <= 50) {
    return true;   // ✅ Cho phép truy cập
  }
  return false;    // ❌ Từ chối
}

// 6️⃣ ⏰📅 Time-based Policy
// Chỉ cho truy cập trong giờ làm việc
{
  type: "time",
  notBefore: "2024-01-01 00:00:00",        // 📅 Từ ngày
  notOnOrAfter: "2024-12-31 23:59:59",     // 📅 Đến ngày
  dayOfMonth: "*",                         // 📅 Mọi ngày trong tháng
  month: "*",                              // 📅 Mọi tháng
  year: "*",                               // 📅 Mọi năm
  hour: "8-18",                            // ⏰ 8h-18h (giờ hành chính)
  minute: "*"
}

// 7️⃣ 🌐🚫 IP Range Policy (ngân hàng dùng nhiều)
// Chỉ cho IP từ công ty (10.0.0.0/8 - private network)
// Hoặc whitelist IP cụ thể
// (Chú ý: Keycloak không có built-in IP policy, cần custom SPI)

// 8️⃣ 🔗📋 Aggregated Policy (kết hợp nhiều policies)
{
  type: "aggregated",
  policies: [
    "role-risk-officer",                   // 🎯 Policy 1: phầi có role
    "time-business-hours",                 // ⏰ Policy 2: trong giờ làm việc
    "ip-corporate-network"                 // 🌐 Policy 3: từ IP công ty
  ],
  decisionStrategy: "UNANIMOUS"            // ✅✅✅ Tất cả policies phải pass (AND logic)
  // decisionStrategy: "AFFIRMATIVE"       // ✅ Chỉ cần 1 policy pass (OR logic)
}
```

- Role-based Policy // 🎯 Kiểm tra role của user
- Client-based Policy // 🏷️ Kiểm tra client nào gọi request
- User Attribute Policy // 👤 Kiểm tra thuộc tính user (branch, level, kyc_level)
- Group-based Policy // 👥 Kiểm tra group/department
- JavaScript Logic Policy // 🔧 Custom logic phc tạp (risk score, business rules)
- Time-based Policy // ⏰ Giới hạn theo thời gian (business hours only)
- IP Range Policy (ngân hàng dùng nhiều) // 🌐🚫 Chỉ IP công ty (cần custom SPI)
- Aggregated Policy // 🔗 Kết hợp nhiều policies (AND/OR logic)

#### 📌 Ví dụ Policy:

- Chỉ cho phép `risk_officer` truy cập từ IP công ty
- Auditor phải có MFA + time-of-day 8:00–18:00
- Trading API chỉ nhận request từ BE trong DMZ

---

## 🧩 XVI. Cơ chế Client – phân loại

> **Cực quan trọng**

Ngân hàng chia client theo mức độ tin cậy:

### 1. Public Client (FE - Frontend)

```javascript
// 🌐💻 Public Client - dành cho Frontend apps (browser/mobile)
// Public Client = Client công khai (Dành cho Frontend - Browser/Mobile - Không giữ được secret)

// 🔴 Đặc điểm:
- ❌🔐 Không có `client_secret` (không giữ được secret an toàn trong browser/mobile)
  // client_secret = Mật khẩu ứng dụng (Không có vì browser/mobile không an toàn để giữ secret)
- ✅🔑 CHỈ dùng PKCE (Proof Key for Code Exchange - RFC 7636)
  // PKCE = Bằng chứng khóa cho trao đổi code (Bắt buộc cho public client - RFC 7636 = Chuẩn)
- ❌🔄 KHÔNG bao giờ giữ refresh token trong browser/localStorage
  // refresh token = Token làm mới (KHÔNG BAO GIỜ lưu trong browser/localStorage - Không an toàn)
  // localStorage = Bộ nhớ local (Không an toàn để lưu token)
- ✅🍪 Nếu cần session -> dùng cookie HTTP-only từ BE
  // cookie HTTP-only = Cookie chỉ đọc được bởi server (An toàn hơn - Từ Backend)
- ✅🔗 Flow: Authorization Code + PKCE (không Implicit Flow)
  // Authorization Code Flow = Luồng mã ủy quyền (Flow an toàn nhất)
  // Implicit Flow = Luồng ngầm (Không an toàn - Không dùng)

// 🎯 Keycloak config:
{
  clientId: "portal-frontend",
  clientAuthenticatorType: "client-secret",  // Nhưng secret để trống!
  publicClient: true,                        // ✅🌐 Đánh dấu là public client
  standardFlowEnabled: true,                 // ✅ Authorization Code Flow
  implicitFlowEnabled: false,                // ❌ Tắt Implicit (không bảo mật)
  directAccessGrantsEnabled: false,          // ❌ Tắt Resource Owner Password (không nên dùng)
  redirectUris: ["https://app.com/*"],       // 🔙 Whitelist redirect URIs
  webOrigins: ["https://app.com"],           // 🌐 CORS whitelist
  pkceRequired: true                         // ✅🔑 Bắt buộc PKCE (chuẩn hiện đại)
}
```

**Ứng dụng:**

- ⚡💻 React, Vue, Angular SPA
- 📱 Mobile App (React Native, Flutter, Swift, Kotlin)
- 🌐 Web App chạy trong browser

> 🔐⚠️ **KHÔNG bao giờ để token vào localStorage**
> -> Dùng cookie HTTP-only từ BE (BFF pattern) hoặc in-memory storage

---

### 2. Confidential Client (Backend - Backend)

```javascript
// 🔐⚙️ Confidential Client - dành cho Backend services
// Confidential Client = Client bí mật (Dành cho Backend - Có thể giữ secret an toàn)

// 🟢 Đặc điểm:
- ✅🔐🔒 Có `client_secret` hoặc private key JWT (RS256/ES256)
  // client_secret = Mật khẩu ứng dụng (Có thể giữ an toàn ở Backend)
  // private key JWT = Khóa riêng JWT (RS256/ES256 = Thuật toán ký - RSA/ECDSA)
- ✅💾 BE giữ refresh token trong Redis/Database (server-side storage)
  // Redis = Cơ sở dữ liệu bộ nhớ (Lưu refresh_token nhanh)
  // server-side storage = Lưu trữ phía server (An toàn - Không ở client)
- ✅🔄 BE gọi được token exchange (cross-realm, microservice)
  // token exchange = Đổi token (Backend có thể đổi token cho microservice khác)
  // cross-realm = Xuyên realm (Giữa các realm khác nhau)
  // microservice = Vi dịch vụ (Hệ thống vi dịch vụ)
- ✅🍪 Có session BE → Redis (distributed session)
  // distributed session = Phiên phân tán (Session lưu trong Redis - Nhiều server dùng chung)
- ✅🔑 Validate token local bằng JWKS (không gọi Keycloak mỗi request)
  // validate token = Xác minh token (Kiểm tra token có hợp lệ không)
  // JWKS = JSON Web Key Set (Bộ khóa công khai - Xác minh token local, không cần gọi Keycloak)

// 🎯 Keycloak config:
{
  clientId: "portal-backend",
  clientAuthenticatorType: "client-secret",  // 🔐 Hoặc "client-jwt" (RS256 signature)
  secret: "********************************",  // 🔒 Secret 256-bit (hoặc private key)
  publicClient: false,                       // ❌🔐 Confidential client
  serviceAccountsEnabled: true,              // ✅🤖 Cho phép Client Credentials Flow
  authorizationServicesEnabled: true,        // ✅🎯 Fine-grained authorization (UMA 2.0)
  standardFlowEnabled: true,                 // ✅ Authorization Code Flow
  directAccessGrantsEnabled: false,          // ❌ Tắt Resource Owner Password
  redirectUris: ["https://be.com/callback"], // 🔙 Backend callback URI
  webOrigins: ["+"]                          // 🌐 Cho phép tất cả origins (BE không có CORS issue)
}

// 💾 Session management:
{
  storage: "Redis",                          // 💾 Lưu session trong Redis cluster
  ttl: 1800,                                 // ⏰ 30 phút session timeout
  refreshTokenRotation: true,                // 🔄 Mỗi lần refresh -> token mới
  revokeRefreshToken: true                   // ❌ Token cũ bị revoke ngay
}
```

**Ứng dụng:**

- ⚙️🌐 API Gateway (Kong, Nginx, Traefik)
- 🔄💻 BFF (Backend for Frontend - NestJS, Express, Spring)
- 📊⚡ Trading Service (Core business logic)
- 📊📈 Reporting Service (Analytics, BI)

---

### 3. Bearer-only client

- Không login
- Chỉ validate Bearer Token
- Không redirect đến login page

**Ứng dụng:**

- Microservice Backend → Backend

---

## 🧩 XVII. Token Exchange – chuẩn ngân hàng & chứng khoán

### 🎯 Mục tiêu Token Exchange: (Mục tiêu đổi token)

- Giảm rủi ro lộ token gốc (Giảm nguy cơ token gốc bị lộ)
  // token gốc = Token ban đầu (Token của user - Nếu lộ sẽ nguy hiểm)
- Tách biệt quyền của microservice (Tách quyền của từng microservice)
  // tách biệt quyền = Phân tách quyền (Mỗi service chỉ có quyền cần thiết)
- Giảm phạm vi quyền nếu service bị hack (Giảm quyền nếu service bị tấn công)
  // phạm vi quyền = Scope (Nếu service bị hack, chỉ mất quyền của service đó)
- Không cho microservice cầm token người dùng đầy đủ (PII protection)
  // PII protection = Bảo vệ thông tin cá nhân (Microservice không thấy đầy đủ thông tin user)
- Chuẩn Zero-Trust (Chuẩn không tin tưởng mặc định)
  // Zero-Trust = Không tin tưởng mặc định (Không tin bất kỳ ai, luôn xác minh)

---

### 🔥 Flow Token Exchange tối ưu nhất ("Gold Standard")

#### 🟣 1. User login → nhận User Token

Chỉ dùng giữa FE ↔ BE.

#### 🟠 2. BE gọi microservice → BE không gửi User Token

➡️ BE dùng Token Exchange để lấy Service Token:

```http
# 🔄🔗 Token Exchange endpoint - RFC 8693 standard (Điểm cuối đổi token - Chuẩn RFC 8693)
POST /protocol/openid-connect/token
Content-Type: application/x-www-form-urlencoded
// Content-Type = Loại nội dung (application/x-www-form-urlencoded = Form URL encoded)

# 📋 Request body: (Nội dung yêu cầu)
grant_type=urn:ietf:params:oauth:grant-type:token-exchange  # 🔄🔗 Token Exchange grant (RFC 8693)
// grant_type = Loại cấp quyền (token-exchange = Đổi token - Chuẩn RFC 8693)
subject_token=<user_access_token>                          # 🎫👤 Token gốc của user (từ login)
// subject_token = Token chủ thể (Token gốc của user - Từ lúc login)
subject_token_type=urn:ietf:params:oauth:token-type:access_token  # 📋 Loại token đầu vào
// subject_token_type = Loại token chủ thể (access_token = Token truy cập)
requested_token_type=urn:ietf:params:oauth:token-type:access_token  # 🎯🎫 Yêu cầu access token mới
// requested_token_type = Loại token yêu cầu (access_token mới = Token truy cập mới)
audience=trading-service                                   # 🎯🏢 Service cần gọi (giới hạn scope chỉ cho service này)
// audience = Đối tượng (Service nào sẽ nhận token - Giới hạn quyền chỉ cho service này)
client_id=portal-backend                                   # 🏷️ Client gọi request (BFF/Backend)
// client_id = ID ứng dụng (Backend gọi request)
client_secret=********                                      # 🔐🔒 Secret của backend client (confidential)
// client_secret = Mật khẩu ứng dụng (Secret của backend - Confidential client)
scope=trading:read trading:execute                         # 📋⬇️ Scope giảm xuống (chỉ quyền tối thiểu cho trading)
// scope = Phạm vi quyền (Giảm xuống - Chỉ quyền tối thiểu cho trading)
// trading:read = Đọc giao dịch, trading:execute = Thực thi giao dịch
actor_token=<service_account_token>                        # 🤖 Optional: service account token (delegation)
// actor_token = Token người thực hiện (Token service account - Tùy chọn - Ủy quyền)
// service account = Tài khoản dịch vụ (Tài khoản cho service, không phải user)
// delegation = Ủy quyền (Service account ủy quyền thay user)
actor_token_type=urn:ietf:params:oauth:token-type:access_token
// actor_token_type = Loại token người thực hiện (access_token = Token truy cập)
```

Keycloak trả:

```json
{
  "access_token": "eyJhbGc...", // 🎫⬇️ Service access token với scope giảm
  // access_token = Token truy cập dịch vụ (Token mới với quyền giảm)
  "issued_token_type": "urn:ietf:params:oauth:token-type:access_token",
  // issued_token_type = Loại token được phát hành (access_token = Token truy cập)
  "token_type": "Bearer",
  // token_type = Loại token (Bearer = Dùng trong header Authorization)
  "expires_in": 300, // ⏱️ Hết hạn nhanh (5 phút)
  // expires_in = Thời gian hết hạn (300 giây = 5 phút - Hết hạn nhanh)
  // ❌🚫 KHÔNG trả refresh_token - service token không refresh được
  // refresh_token = Token làm mới (KHÔNG có - Service token không thể refresh)
  "scope": "trading:read trading:execute" // 📋✅ Scope đã giảm (không có user:*, admin:*)
  // scope = Phạm vi quyền (Đã giảm - Chỉ trading:read và trading:execute)
  // Không có user:* = Không có quyền user đầy đủ
  // Không có admin:* = Không có quyền admin
}
```

✔ Quyền được giảm -> chỉ những permission mà trading-service cần.

#### 🟡 3. BE gửi Service Token → Microservice

Microservice chỉ validate token = JWKS, không biết user token gốc.

```javascript
// 🔹 Bước 1: BE gửi service token tới microservice
POST https://trading-service/api/orders
Authorization: Bearer <service_access_token>  // 🎫⬇️ Service token (không phải user token)
Content-Type: application/json

// 🔹 Bước 2: Microservice validate token local (không gọi Keycloak)
// 🔑📥 Microservice có JWKS public key của Keycloak (cached)
// ✅🔍 Verify JWT signature bằng public key (RS256/ES256)
// ✅📋 Check exp (expiration), iat (issued at), nbf (not before)
// ✅🎯 Check aud (audience) = "trading-service" (chỉ accept token cho mình)
// ✅🏷️ Check iss (issuer) = Keycloak realm URL
// ✅📋 Check scope: có "trading:execute" không?

// 🔹 Bước 3: Token hợp lệ → Execute business logic
// ✅💼 Microservice thực thi lệnh trading
// 🚫👤 Microservice KHÔNG thấy full user info (PII protected)
// 📋 Chỉ thấy: user_id, minimal claims, scopes cho trading
// ❌🔄 Microservice KHÔNG có refresh token → không tự renew được
```

> 👉 **Microservice không bao giờ giữ Refresh Token**

---

### 🧨 Tại sao token exchange cực quan trọng?

| Rủi ro nếu không dùng                  | Giải pháp token exchange                              |
| -------------------------------------- | ----------------------------------------------------- |
| Microservice thấy full user info (PII) | User token → Service token (ẩn PII)                   |
| Microservice cầm refresh token         | Không bao giờ xảy ra                                  |
| Lateral movement nếu 1 service bị hack | Chỉ quyền tối thiểu của service đó                    |
| Risk đánh cắp token qua log            | Token đã giảm quyền; log bị hack cũng không nguy hiểm |
| Không kiểm soát được role cross-realm  | Token Exchange Policy + Audience + Scope              |

---

## 🧩 XVIII. Token Design tối ưu

### 🔵 Access Token (5 phút)

- Quyền thấp nhất có thể
- Audience = tên microservice
- Không chứa PII

### 🟣 Refresh Token (30 phút)

- Chỉ nằm ở BFF/Backend
- Có Rotation → 1 lần dùng → bị revoke
- Lưu trong Redis với TTL

### 🟢 ID Token (1 phút)

- Dùng cho FE hiển thị tên user (optional)

### 🔴 User Session (Keycloak)

- Dùng cho SSO
- Timeout 15–30 phút (internal) / 60 phút (external)

---

## 🧩 XIX. Bảo mật nâng cao (Zero Trust - Không tin tưởng mặc định)

> Ngân hàng / chứng khoán bắt buộc có:
> // Zero Trust = Không tin tưởng mặc định (Không tin bất kỳ ai, luôn xác minh)

### 1. MFA bắt buộc (MFA = Multi-Factor Authentication - Xác thực đa yếu tố)

- **Internal:** Smart-card, RSA Token, Microsoft Authenticator
  // Internal = Nội bộ (Nhân viên công ty)
  // Smart-card = Thẻ thông minh (Thẻ vật lý có chip)
  // RSA Token = Token RSA (Thiết bị tạo mã OTP)
  // Microsoft Authenticator = Ứng dụng xác thực Microsoft (App tạo mã OTP)
- **External:** SMS OTP, Smart OTP, TOTP
  // External = Bên ngoài (Khách hàng)
  // SMS OTP = Mã OTP qua SMS (One-Time Password qua tin nhắn)
  // Smart OTP = OTP thông minh (OTP từ app)
  // TOTP = Time-based One-Time Password (Mật khẩu một lần theo thời gian)

### 2. IP Restriction (Giới hạn IP)

- Internal chỉ cho phép IP công ty (Internal chỉ cho phép IP từ công ty)
  // IP công ty = IP nội bộ (Chỉ IP từ mạng công ty mới được truy cập)
- Trading Engine chỉ cho phép IP từ DMZ (Trading Engine chỉ cho phép IP từ DMZ)
  // Trading Engine = Động cơ giao dịch (Hệ thống giao dịch chứng khoán)
  // DMZ = Demilitarized Zone (Vùng phi quân sự - Mạng trung gian)

### 3. Token Replay Protection (Bảo vệ chống tái phát token)

- PKCE (Proof Key for Code Exchange - Bằng chứng khóa cho trao đổi code)
  // PKCE = Chống đánh cắp code trong URL
- Refresh Token Rotation (Xoay token làm mới)
  // Refresh Token Rotation = Token chỉ dùng 1 lần
- Time-based nonce (Nonce dựa trên thời gian)
  // nonce = Số chỉ dùng một lần (Số ngẫu nhiên dùng 1 lần - Chống tái phát)

### 4. Audit Logging (Ghi log kiểm toán)

Gửi sang Splunk / ELK / Datadog: (Gửi đến hệ thống log)
// Splunk = Hệ thống phân tích log (Công cụ phân tích dữ liệu)
// ELK = Elasticsearch, Logstash, Kibana (Stack công cụ log)
// Datadog = Dịch vụ giám sát (Dịch vụ giám sát và phân tích)

- login (Đăng nhập)
- logout (Đăng xuất)
- token exchange (Đổi token)
- permission denied (Từ chối quyền)

### 5. Rate limiting & Brute Force Detection (Giới hạn tốc độ & Phát hiện tấn công vũ phu)

Bật trong Keycloak. (Bật trong Keycloak)
// Rate limiting = Giới hạn tốc độ (Giới hạn số request mỗi giây)
// Brute Force Detection = Phát hiện tấn công vũ phu (Phát hiện đăng nhập sai nhiều lần)

---

## 🧩 XX. Kiến trúc chuẩn nhất

> **Cho ngân hàng / chứng khoán**

```
          +-------------+
           |  Keycloak   |
           +-------------+
      / Realm Internal  \
     / Realm External    \
    / Realm Trading      \
   +-------------------------+
        ^            ^
        | SSO        | Token Exchange
        |            |
+-------------+     +------------------+
| Portal BFF  | <-- | Trading BFF      |
| (Internal)  |     | (Service Layer)  |
+-------------+     +------------------+
       ^                     ^
       | session cookie      | service token
       |                     |
   +----------+          +--------------+
   | FE Web   |          | Microservice |
   | Internal |          | Trading Core |
   +----------+          +--------------+
```

---

## 🧩 XXI. SSO vs Shared Cookie

### 🟥 1. Trên cùng 1 domain không phải SSO

**Ví dụ:**

- `app1.momo.vn`
- `app2.momo.vn`
- `dashboard.momo.vn`

Nếu backend set cùng 1 cookie domain = `.momo.vn` → tất cả app con đều đọc được cookie → user không cần login lại.

> ⚠️ **Nhưng đây không phải SSO, mà là:**
>
> - 👉 "Shared Session Cookie"
> - 👉 "Domain-level Authentication"

Nó chỉ hoạt động vì trình duyệt chia sẻ cookie cho subdomain, không phải vì hệ thống hỗ trợ SSO.

#### 📌 Điểm yếu lớn:

Chỉ hoạt động trong cùng domain, nếu bạn có:

- `external.app`
- `trading.app`
- `internal.app`
- `admin.app`

→ KHÔNG dùng chung cookie được → không phải SSO thật sự.

---

### 🟦 2. Vậy SSO thực sự là gì?

**SSO = Single Sign-On**, nghĩa là:

- đăng nhập một lần → dùng được trên nhiều hệ thống
- không cần chung domain
- phiên đăng nhập được lưu ở Identity Provider (Keycloak)
- mọi ứng dụng xác nhận qua OIDC / SAML / session SSO Keycloak

> 🔥 **SSO không dựa vào cookie domain**
> → Mà dựa vào SSO Session mà IdP quản lý.

```
SSO = xác thực tập trung tại Keycloak
Not = chia sẻ cookie
```

---

### 🟩 3. Khi nào mới được gọi là SSO thật sự?

Một hệ thống là SSO khi:

1. FE redirect đến Keycloak để login
2. Keycloak tạo SSO session
3. App 2 redirect đến Keycloak → Keycloak thấy user đã login → trả về code/token mà không cần nhập password
4. Dù app 1 và app 2 ở **khác domain**:
   - `portal.momo.vn`
   - `trading.momo.vn`
   - `service.company.com`
   - `admin.company.org`

→ Chỉ cần chung realm → vẫn SSO.

> 📌 **Đây mới gọi là Federated SSO hoặc OIDC SSO.**

---

### 🟨 4. Vậy trên cùng domain thì gọi bằng thuật ngữ gì?

#### 1️⃣ Nếu chỉ dùng chung cookie → "Domain Shared Authentication"

Không phải SSO.

#### 2️⃣ Nếu cả app 1 + app 2 đều login qua Keycloak → dù cùng domain → vẫn là SSO

Dùng thuật ngữ:

> 👉 **"SSO with Same-site Deployment"**
> (SSO nhưng cả apps nằm cùng domain/subdomain)

#### 3️⃣ Nếu BE quản lý session chung →

> 👉 **"Centralized Session Authentication"**

---

### 🟧 5. So sánh nhanh

| Cơ chế                            | Cookie Shared         | SSO Keycloak (chuẩn ngân hàng) |
| --------------------------------- | --------------------- | ------------------------------ |
| **Dựa trên cookie domain?**       | Có                    | Không                          |
| **Login 1 lần dùng nhiều app?**   | Chỉ trong cùng domain | Trong mọi domain               |
| **Hỗ trợ logout toàn hệ thống?**  | Không                 | Có (Backchannel Logout)        |
| **MFA / Policy / Role**           | Không                 | Có                             |
| **Token Exchange**                | Không                 | Có                             |
| **Phù hợp ngân hàng/chứng khoán** | ❌ Không              | ✔️ Chuẩn                       |

---

### 🟥 6. Kết luận cực ngắn

> **Trùng domain KHÔNG phải SSO.**
>
> **SSO là xác thực tập trung tại Keycloak, không phụ thuộc domain.**

Một hệ thống ngân hàng/chứng khoán chuẩn luôn dùng:

- ✅ SSO via Keycloak (OIDC/SAML)
- ✅ Không phụ thuộc cookie domain
- ✅ Có SSO session
- ✅ Có Backchannel Logout
- ✅ Có MFA, Role, Policy
- ✅ Có Token Exchange

---

## 🎯 Tổng Kết

Tài liệu này cung cấp kiến thức chuyên sâu về Keycloak theo chuẩn ngân hàng/tài chính/chứng khoán, bao gồm:

- ✅ Kiến trúc và cấu trúc Keycloak
- ✅ Flow xác thực chi tiết (Login/Refresh/Logout/Token Exchange)
- ✅ Phân chia Realm tối ưu
- ✅ Phân quyền RBAC/ABAC
- ✅ Token management và bảo mật
- ✅ SSO và Federation
- ✅ Best practices cho môi trường production

> 💡 **Lưu ý:** Đây là kiến thức nền tảng cho việc triển khai hệ thống IAM cấp doanh nghiệp với yêu cầu bảo mật cao.

---

**© 2024 - Keycloak Documentation**
