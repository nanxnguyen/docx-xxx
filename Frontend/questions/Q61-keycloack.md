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

**Keycloak** là một **Identity & Access Management Server (IAM)** – nghĩa là một máy chủ quản lý danh tính và truy cập.

Nó chịu trách nhiệm:

- ✅ **Xác thực người dùng** (Authentication)
- ✅ **Cấp quyền truy cập** (Authorization)
- ✅ **Cấp và quản lý JWT token**
- ✅ **Quản lý phiên đăng nhập** (session)
- ✅ **Hỗ trợ SSO** (Single Sign-On) và **SLO** (Single Logout)

> 🎯 **Keycloak giúp Frontend / Backend không cần tự xây dựng logic đăng nhập phức tạp mà chỉ cần ủy quyền xác thực cho Keycloak.**

---

## 🧩 II. Cấu trúc & Thành phần trong Keycloak

| Thành phần                  | Vai trò                                                                    | Ví dụ thực tế                               |
| --------------------------- | -------------------------------------------------------------------------- | ------------------------------------------- |
| **Realm**                   | Không gian quản lý độc lập (giống 1 tenant) chứa user, client, role, group | `momo-ttt`, `hrm-portal`, `finance-system`  |
| **Client**                  | Một ứng dụng được đăng ký trong realm (FE hoặc BE)                         | `portal-frontend`, `portal-backend`         |
| **User**                    | Người dùng có thể đăng nhập                                                | `nguyenvana`, `tranthihoa`                  |
| **Group**                   | Nhóm người dùng (gán sẵn role)                                             | `admin-group`, `customer-group`             |
| **Role**                    | Vai trò (quyền hạn)                                                        | `admin`, `viewer`, `manager`                |
| **Scope**                   | Quyền truy cập cụ thể theo API                                             | `read:users`, `update:reports`              |
| **Identity Provider (IdP)** | Hệ thống xác thực bên ngoài                                                | Google Workspace, LDAP, Microsoft AD        |
| **Token**                   | Gói thông tin được cấp sau khi đăng nhập                                   | `access_token`, `refresh_token`, `id_token` |
| **Session**                 | Phiên đăng nhập; Keycloak theo dõi user đã login ở app nào                 | Giúp thực hiện SSO & SLO                    |
| **Policy / Mapper**         | Quy tắc xác định cách map role hoặc scope                                  | Gán role từ AD sang client role             |

---

## ⚙️ III. Cơ chế hoạt động nội bộ của Keycloak

Keycloak hoạt động dựa trên chuẩn **OIDC (OpenID Connect)** – mở rộng từ **OAuth2**.

### 🧠 3 loại flow phổ biến trong OIDC:

| Flow                                   | Mô tả                                | Dành cho                               |
| -------------------------------------- | ------------------------------------ | -------------------------------------- |
| **Authorization Code Flow (với PKCE)** | FE lấy "code" rồi BE đổi thành token | Web app, SPA có backend (bảo mật nhất) |
| **Implicit Flow**                      | FE nhận token trực tiếp từ Keycloak  | App cũ (ít dùng vì kém bảo mật)        |
| **Client Credentials Flow**            | Dành cho BE–BE (service account)     | Hệ thống vi mô nội bộ                  |

---

## 🧭 IV. Flow chi tiết: FE → BE → Keycloak

> **Backend-for-Frontend Model** - Flow an toàn nhất, được khuyến nghị bởi:
>
> - 🏦 Ngân hàng (Vietcombank, Techcombank, HSBC…)
> - 🧱 Doanh nghiệp lớn (MoMo, VNG, Grab, Shopee…)
> - 🧩 Các hệ thống microservice, đa ứng dụng, có SSO

### 🔹 1️⃣ Giai đoạn đăng nhập (Login Flow)

#### 🔸 Các bước:

**(1) FE → BE: `/auth/login`**

- Người dùng click "Login" trên FE.
- FE gửi yêu cầu login tới BE.

**(2) BE → Keycloak: `/realms/momo-ttt/protocol/openid-connect/auth`**

- BE redirect người dùng đến trang đăng nhập Keycloak.
- URL chứa tham số:

```http
response_type=code
client_id=portal-frontend
redirect_uri=https://be.momo.vn/auth/callback
code_challenge=XYZ
code_challenge_method=S256
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
  "grant_type": "authorization_code",
  "code": "ABC",
  "client_secret": "********",
  "redirect_uri": "https://be.momo.vn/auth/callback",
  "code_verifier": "XYZ"
}
```

Keycloak trả:

```json
{
  "access_token": "...",
  "refresh_token": "...",
  "id_token": "...",
  "expires_in": 300
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

```
(1) Access token hết hạn (300s)
(2) FE → BE: /auth/refresh
(3) BE → Keycloak: /token { grant_type=refresh_token }
(4) Keycloak → BE: new tokens
(5) BE update Redis, trả về FE cookie mới
```

> ⚙️ Sử dụng **Refresh Token Rotation** – mỗi lần refresh, token cũ bị vô hiệu hóa → chống reuse.

---

### 🔹 3️⃣ Giai đoạn logout (Single Logout)

```
(1) FE → BE: /auth/logout
(2) BE → Keycloak: /logout?id_token_hint=...&refresh_token=...
(3) Keycloak xoá session người dùng.
(4) Keycloak broadcast "backchannel logout" tới các ứng dụng khác.
(5) FE xoá cookie.
```

> 🧠 Giúp logout toàn hệ thống (nếu user đang đăng nhập ở nhiều app, tất cả cùng bị logout).

---

### 🔹 4️⃣ Giai đoạn token exchange (cross-realm / microservice)

Khi cần gọi sang hệ thống khác (ví dụ realm khác hoặc microservice khác):

```
(1) BE → Keycloak: /token (grant_type=token_exchange)
(2) Keycloak kiểm tra policy → trả về token mới thuộc realm khác.
```

> Dùng để ủy quyền chéo giữa hệ thống mà vẫn giữ được danh tính người dùng (SSO thật sự).

---

## 🧠 V. Giải thích chi tiết các loại token

| Token             | Vai trò                                     | Thời hạn              | Ai giữ     |
| ----------------- | ------------------------------------------- | --------------------- | ---------- |
| **Access Token**  | Cho phép truy cập API                       | Ngắn (5–10 phút)      | BE         |
| **Refresh Token** | Dùng để lấy token mới                       | Dài (15–60 phút)      | BE (Redis) |
| **ID Token**      | Thông tin người dùng (name, email, role...) | Ngắn                  | BE         |
| **Session**       | Theo dõi người dùng login ở app nào         | Được Keycloak quản lý | Keycloak   |

> 💡 **Tất cả token đều là JWT (JSON Web Token)**, có thể xác minh bằng public key (JWKS) mà không cần gọi Keycloak mỗi lần.

---

## 🧩 VI. Cơ chế bảo mật trong flow FE → BE → Keycloak

| Cơ chế                                 | Mục đích                                        | Ghi chú                      |
| -------------------------------------- | ----------------------------------------------- | ---------------------------- |
| **PKCE** (Proof Key for Code Exchange) | Ngăn hacker lấy cắp code trong redirect URL     | Bắt buộc cho public client   |
| **HTTPS (TLS 1.3)**                    | Mã hóa dữ liệu giữa FE–BE–Keycloak              | Tất cả request               |
| **HTTP-only cookie**                   | FE không đọc được token bằng JS                 | Ngăn XSS                     |
| **CSRF Token**                         | Chống request giả mạo                           | FE gửi kèm                   |
| **Refresh Token Rotation**             | Token chỉ dùng 1 lần                            | Bật trong Keycloak           |
| **MFA / OTP**                          | Tăng lớp xác thực                               | Dùng Keycloak OTP Policy     |
| **Token Exchange Policy**              | Giới hạn quyền truy cập giữa các realm          | Giảm rủi ro lateral movement |
| **Audit Logging**                      | Ghi lại toàn bộ login / logout / token exchange | Phục vụ audit ngân hàng      |

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

Keycloak hỗ trợ SSO theo chuẩn **OpenID Connect Session Management** và **SAML2 Web SSO**.

Dựa trên mô hình:

- 🔹 1 user login → dùng cho nhiều ứng dụng
- 🔹 Session được Keycloak quản lý tập trung
- 🔹 Logout 1 nơi → toàn bộ ứng dụng logout (SLO)

### 🔥 1️⃣ SSO hoạt động chi tiết

**(1) FE → BE → Keycloak login**

User được redirect đến:

```
/realms/<realm>/protocol/openid-connect/auth
```

Keycloak tạo SSO session:

```
SSO Session ID: 5ae2a02c-b3d0-4b79-bc23-...
```

**(2) Khi user mở thêm ứng dụng thứ 2**

```
App2 → BE2 → redirect tới Keycloak.
Keycloak thấy session user còn tồn tại:
  ➡️ Không cần nhập lại username/password
  ➡️ Keycloak trả trực tiếp code (Authorization Code)
  ➡️ BE2 đổi code → token
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

```
├── REALM_INTERNAL             (nhân viên, AD/LDAP)
│     ├── client_portal_fe
│     ├── client_portal_be
│     ├── role-based: teller, auditor, risk, manager
│
├── REALM_EXTERNAL             (khách hàng)
│     ├── client_mobile_app
│     ├── client_web_app
│     ├── role-based: customer-normal, vip, business
│
├── REALM_FUNDS_SERVICE        (dịch vụ tài chính / quỹ)
│     ├── microservice A
│     ├── microservice B
│
├── REALM_TRADING_SERVICE      (core chứng khoán)
│     ├── trading-engine
│     ├── settlement-service
│     ├── price-stream-service
│
└── REALM_ADMIN                (Keycloak admin, back-office)
      ├── client-admin-console
      ├── client-reporting
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

### 1. RBAC (Role-based) – vai trò theo chức vụ

#### Ví dụ Internal:

```
teller                (giao dịch viên)
branch_manager        (trưởng chi nhánh)
ops_manager           (quản lý vận hành)
risk_officer          (quản lý rủi ro)
auditor               (kiểm toán)
it_support            (CNTT)
```

#### External:

```
customer
vip_customer
business_customer
broker (chứng khoán)
```

---

### 2. ABAC (Attribute-based) – vai trò theo thuộc tính

| Attribute          | Ý nghĩa                    |
| ------------------ | -------------------------- |
| `branch=700`       | Chi nhánh 700              |
| `region=NORTH`     | Miền Bắc                   |
| `level=4`          | Cấp lãnh đạo               |
| `kyc_level=3`      | Hoàn thành định danh cấp 3 |
| `risk_score <= 50` | Rủi ro thấp                |

> 💡 ABAC giúp kiểm soát truy cập theo dữ liệu, không chỉ theo vai trò.

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

- Role-based Policy
- Client-based Policy
- User Attribute Policy
- Group-based Policy
- JavaScript Logic Policy
- Time-based Policy
- IP Range Policy (ngân hàng dùng nhiều)
- Aggregated Policy

#### 📌 Ví dụ Policy:

- Chỉ cho phép `risk_officer` truy cập từ IP công ty
- Auditor phải có MFA + time-of-day 8:00–18:00
- Trading API chỉ nhận request từ BE trong DMZ

---

## 🧩 XVI. Cơ chế Client – phân loại

> **Cực quan trọng**

Ngân hàng chia client theo mức độ tin cậy:

### 1. Public Client (FE)

- Không có `client_secret`
- Chỉ dùng PKCE
- Không bao giờ giữ refresh token trong browser

**Ứng dụng:**

- React, Mobile App, Web SPA

> 🔐 **Không bao giờ để token vào localStorage**

---

### 2. Confidential Client (Backend)

- Có `client_secret` hoặc private key JWT
- BE giữ refresh token
- BE gọi được token exchange
- Có session BE → Redis

**Ứng dụng:**

- API Gateway
- BFF (Backend for Frontend)
- Trading Service
- Reporting Service

---

### 3. Bearer-only client

- Không login
- Chỉ validate Bearer Token
- Không redirect đến login page

**Ứng dụng:**

- Microservice Backend → Backend

---

## 🧩 XVII. Token Exchange – chuẩn ngân hàng & chứng khoán

### 🎯 Mục tiêu Token Exchange:

- Giảm rủi ro lộ token gốc
- Tách biệt quyền của microservice
- Giảm phạm vi quyền nếu service bị hack
- Không cho microservice cầm token người dùng đầy đủ (PII protection)
- Chuẩn Zero-Trust

---

### 🔥 Flow Token Exchange tối ưu nhất ("Gold Standard")

#### 🟣 1. User login → nhận User Token

Chỉ dùng giữa FE ↔ BE.

#### 🟠 2. BE gọi microservice → BE không gửi User Token

➡️ BE dùng Token Exchange để lấy Service Token:

```http
POST /protocol/openid-connect/token
grant_type=token_exchange
subject_token=<user_access_token>
requested_token_type=urn:ietf:params:oauth:token-type:access_token
audience=trading-service
```

Keycloak trả:

```
service_access_token
```

✔ Quyền được giảm -> chỉ những permission mà trading-service cần.

#### 🟡 3. BE gửi Service Token → Microservice

Microservice chỉ validate token = JWKS, không biết user token gốc.

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

## 🧩 XIX. Bảo mật nâng cao (Zero Trust)

> Ngân hàng / chứng khoán bắt buộc có:

### 1. MFA bắt buộc

- **Internal:** Smart-card, RSA Token, Microsoft Authenticator
- **External:** SMS OTP, Smart OTP, TOTP

### 2. IP Restriction

- Internal chỉ cho phép IP công ty
- Trading Engine chỉ cho phép IP từ DMZ

### 3. Token Replay Protection

- PKCE
- Refresh Token Rotation
- Time-based nonce

### 4. Audit Logging

Gửi sang Splunk / ELK / Datadog:

- login
- logout
- token exchange
- permission denied

### 5. Rate limiting & Brute Force Detection

Bật trong Keycloak.

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
