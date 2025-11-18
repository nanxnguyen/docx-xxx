

## **Phần 16: Senior-Level Questions (Câu Hỏi Cấp Senior)**

### **Q69: Tối Ưu Performance của React Web App**

**❓ Tình Huống:**

Bạn là Senior Frontend Developer của một Trading Platform (React + TypeScript). App hiện tại có các vấn đề:
- **Initial Load**: 5-7s trên 3G, bundle size 2.5MB
- **Runtime Performance**: 
  - Real-time updates (WebSocket) gây re-render toàn bộ app (60+ components)
  - List 10,000+ orders lag khi scroll (FPS drop 60 → 15)
  - Memory leak sau 2-3 giờ sử dụng (memory tăng từ 50MB → 500MB)
- **User Complaints**: App chậm, lag, sometimes crash

**Yêu cầu:** Thiết kế và implement chiến lược tối ưu toàn diện (từ build-time đến runtime).

---

**✅ Đáp Án Chi Tiết:**

**🎯 Chiến Lược Tối Ưu 5 Tầng (5-Layer Optimization Strategy):**

```
┌──────────────────────────────────────────────────────────────┐
│           PERFORMANCE OPTIMIZATION LAYERS                     │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  1️⃣ BUILD-TIME OPTIMIZATION (Tối ưu lúc build)              │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ • Bundle Size Reduction (Giảm kích thước bundle)        │ │
│  │ • Code Splitting (Chia nhỏ code)                        │ │
│  │ • Tree-shaking (Loại bỏ dead code)                      │ │
│  │ • Lazy Loading (Tải code khi cần)                       │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                               │
│  2️⃣ NETWORK OPTIMIZATION (Tối ưu mạng)                      │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ • Resource Hints (Prefetch, Preload, Preconnect)       │ │
│  │ • HTTP/2 + Compression (Gzip, Brotli)                  │ │
│  │ • CDN + Edge Caching                                    │ │
│  │ • Service Worker + Offline Cache                       │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                               │
│  3️⃣ RENDERING OPTIMIZATION (Tối ưu render)                  │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ • React.memo + useMemo + useCallback                   │ │
│  │ • Virtual Scrolling (10K+ items)                        │ │
│  │ • Debounce + Throttle                                   │ │
│  │ • Lazy Image Loading + Responsive Images               │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                               │
│  4️⃣ STATE MANAGEMENT OPTIMIZATION (Tối ưu state)            │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ • Context Splitting (Tách context nhỏ)                  │ │
│  │ • Zustand/Redux Toolkit (Selective subscriptions)      │ │
│  │ • Immer (Immutable updates hiệu quả)                    │ │
│  │ • React Query (Server state caching)                   │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                               │
│  5️⃣ MEMORY MANAGEMENT (Tối ưu bộ nhớ)                       │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ • Cleanup useEffect (Listeners, timers, subscriptions) │ │
│  │ • AbortController (Cancel requests)                     │ │
│  │ • WeakMap/WeakSet (Temporary references)               │ │
│  │ • Memory Profiling (Chrome DevTools)                   │ │
│  └─────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

**Hoạt động:**

**📊 Performance Metrics Target (Mục tiêu):**
- Initial Load: 5-7s → **< 2s** (70% improvement)
- Bundle Size: 2.5MB → **< 500KB** (80% reduction)
- FPS: 15 → **60 FPS** (4x improvement)
- Memory: 500MB → **< 100MB** (80% reduction)

---

**Code Example (TypeScript + React):**

```typescript
// ============================================
// 1️⃣ BUILD-TIME OPTIMIZATION
// ============================================

// 📦 A. Vite Configuration (Modern bundler - faster than Webpack)
// vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { visualizer } from 'rollup-plugin-visualizer';

export default defineConfig({
  plugins: [
    react(),
    visualizer({ open: true }) // Phân tích bundle size
  ],
  
  build: {
    // ✅ Code splitting: tách vendor libraries
    rollupOptions: {
      output: {
        manualChunks: {
          // Tách React libs riêng (thay đổi ít → cache tốt)
          'react-vendor': ['react', 'react-dom', 'react-router-dom'],
          
          // Tách chart libraries (nặng - 500KB+)
          'chart-vendor': ['recharts', 'lightweight-charts'],
          
          // Tách utilities
          'utils': ['lodash-es', 'date-fns', 'axios']
        }
      }
    },
    
    // ✅ Minify + Compress
    minify: 'terser',
    terserOptions: {
      compress: {
        drop_console: true, // Remove console.log trong production
        drop_debugger: true
      }
    },
    
    // ✅ Source maps: hidden (bảo mật source code)
    sourcemap: 'hidden',
    
    // ✅ Chunk size warning
    chunkSizeWarningLimit: 500
  },
  
  // ✅ Tree-shaking: loại bỏ unused exports
  optimizeDeps: {
    include: ['react', 'react-dom']
  }
});

// 📦 B. Lazy Loading Routes (Code Splitting by Route)
import { lazy, Suspense } from 'react';
import { Routes, Route } from 'react-router-dom';

// ✅ Lazy load pages (chỉ load khi user navigate đến)
const Dashboard = lazy(() => import('./pages/Dashboard'));
const Trading = lazy(() => import('./pages/Trading'));
const Portfolio = lazy(() => import('./pages/Portfolio'));
const Analytics = lazy(() => import('./pages/Analytics'));

// Skeleton loader
const PageLoader = () => (
  <div className="flex items-center justify-center h-screen">
    <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
    <span className="ml-3">Loading...</span>
  </div>
);

export default function App() {
  return (
    <Suspense fallback={<PageLoader />}>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/trading" element={<Trading />} />
        <Route path="/portfolio" element={<Portfolio />} />
        <Route path="/analytics" element={<Analytics />} />
      </Routes>
    </Suspense>
  );
}

// ============================================
// 3️⃣ RENDERING OPTIMIZATION
// ============================================

// 🎨 A. React.memo + useMemo + useCallback
import { memo, useMemo, useCallback } from 'react';

// ✅ React.memo - chỉ re-render khi props thay đổi
const OrderItem = memo(function OrderItem({ order, onDelete }) {
  return (
    <div>
      <span>{order.symbol}</span>
      <button onClick={() => onDelete(order.id)}>Delete</button>
    </div>
  );
});

// Parent component
function OrderList({ orders }) {
  // ✅ useCallback - memoize function
  const handleDelete = useCallback((id: string) => {
    console.log('Delete', id);
  }, []);
  
  // ✅ useMemo: memoize expensive calculations
  const sortedOrders = useMemo(() => {
    return orders.sort((a, b) => b.timestamp - a.timestamp);
  }, [orders]);
  
  return (
    <div>
      {sortedOrders.map(order => (
        <OrderItem 
          key={order.id} 
          order={order} 
          onDelete={handleDelete}
        />
      ))}
    </div>
  );
}

// 🎨 B. Virtual Scrolling (10K+ items)
import { FixedSizeList as List } from 'react-window';

function GoodOrderList({ orders }: { orders: Order[] }) {
  const Row = ({ index, style }) => {
    const order = orders[index];
    return (
      <div style={style} className="flex items-center border-b px-4">
        <span className="w-20 font-bold">{order.symbol}</span>
        <span className="w-32">{order.quantity} @ ${order.price}</span>
      </div>
    );
  };

  return (
    <List
      height={600}
      itemCount={orders.length}
      itemSize={50}
      width="100%"
    >
      {Row}
    </List>
  );
}

// ============================================
// 4️⃣ STATE MANAGEMENT OPTIMIZATION
// ============================================

// 🏪 Zustand (State management tối ưu)
import create from 'zustand';

interface TradingStore {
  orders: Order[];
  addOrder: (order: Order) => void;
}

const useTradingStore = create<TradingStore>((set) => ({
  orders: [],
  addOrder: (order) => set((state) => ({
    orders: [...state.orders, order]
  }))
}));

// ✅ Selective subscription
function OrderList() {
  const orders = useTradingStore(state => state.orders);
  return (
    <div>
      {orders.map(order => (
        <OrderItem key={order.id} order={order} />
      ))}
    </div>
  );
}

// ============================================
// 5️⃣ MEMORY MANAGEMENT
// ============================================

// 🧹 Cleanup useEffect
function TradingChart() {
  useEffect(() => {
    const ws = new WebSocket('wss://api.trading.com');
    
    ws.onmessage = (event) => {
      // Handle data
    };
    
    // ✅ Cleanup on unmount
    return () => {
      if (ws.readyState === WebSocket.OPEN) {
        ws.close();
      }
    };
  }, []);
  
  return <div>Chart...</div>;
}
```

**🎯 Kết Quả Sau Optimization:**

```
┌────────────────────────────────────────────────────────────────┐
│           PERFORMANCE METRICS - BEFORE vs AFTER                 │
├────────────────────────────────────────────────────────────────┤
│  Metric              │ Before      │ After       │ Improvement │
│ ─────────────────────┼─────────────┼─────────────┼──────────── │
│  Initial Load        │ 5-7s        │ 1.5-2s      │ 70% faster  │
│  Bundle Size         │ 2.5MB       │ 450KB       │ 82% smaller │
│  FCP (First Paint)   │ 3s          │ 0.8s        │ 73% faster  │
│  TTI (Interactive)   │ 6s          │ 2s          │ 67% faster  │
│  Scroll FPS          │ 15 FPS      │ 60 FPS      │ 4x better   │
│  Memory Usage        │ 500MB       │ 80MB        │ 84% less    │
│  Re-renders/sec      │ 200+        │ 10-20       │ 90% less    │
└────────────────────────────────────────────────────────────────┘
```

**Best Practices:**

1. **Measure First**: Dùng Lighthouse, Chrome DevTools Performance
2. **Bundle Analysis**: `npm run build -- --analyze`
3. **Code Splitting**: Route-level + Component-level
4. **State Management**: Context cho static, Zustand cho complex state
5. **Memory Management**: Always cleanup useEffect

**Common Mistakes:**

```typescript
// ❌ MISTAKE: Inline functions trong render
{items.map(item => (
  <Item onClick={() => handleClick(item)} />
))}

// ✅ FIX: useCallback
const handleClick = useCallback((item) => { ... }, []);

// ❌ MISTAKE: Không cleanup useEffect
useEffect(() => {
  const ws = new WebSocket('...');
}, []);

// ✅ FIX: Cleanup
useEffect(() => {
  const ws = new WebSocket('...');
  return () => ws.close();
}, []);
```

---

### **Q70: Bảo Mật Security trên Web Application**

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

---

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
// 1️⃣ HTTPS + TLS
// ============================================

// Server: nginx.conf
server {
  listen 443 ssl http2;
  
  # HSTS: Force HTTPS for 1 year
  add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
  
  # SSL/TLS Configuration
  ssl_certificate /path/to/cert.pem;
  ssl_certificate_key /path/to/key.pem;
  ssl_protocols TLSv1.2 TLSv1.3;
  ssl_ciphers HIGH:!aNULL:!MD5;
}

// ============================================
// 2️⃣ XSS PREVENTION
// ============================================

// 🛡️ A. Input Sanitization (DOMPurify)
import DOMPurify from 'dompurify';

function CommentForm({ onSubmit }) {
  const [comment, setComment] = useState('');
  
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    // ✅ Sanitize input
    const sanitized = DOMPurify.sanitize(comment, {
      ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'a'],
      ALLOWED_ATTR: ['href']
    });
    
    onSubmit(sanitized);
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <textarea 
        value={comment}
        onChange={(e) => setComment(e.target.value)}
      />
      <button type="submit">Submit</button>
    </form>
  );
}

// ✅ Safe display
function SafeComment({ content }) {
  const sanitized = useMemo(() => {
    return DOMPurify.sanitize(content, {
      ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'a', 'p'],
      ALLOWED_ATTR: ['href', 'target'],
      ALLOW_DATA_ATTR: false
    });
  }, [content]);
  
  return <div dangerouslySetInnerHTML={{ __html: sanitized }} />;
}

// 🛡️ B. Content Security Policy (CSP)
// Server: Express.js
app.use((req, res, next) => {
  res.setHeader(
    'Content-Security-Policy',
    [
      "default-src 'self'",
      "script-src 'self' https://trusted-cdn.com",
      "style-src 'self' 'unsafe-inline'",
      "img-src 'self' data: https:",
      "connect-src 'self' https://api.example.com",
      "frame-ancestors 'none'"
    ].join('; ')
  );
  next();
});

// ============================================
// 3️⃣ CSRF PROTECTION
// ============================================

// Server: Generate CSRF token
app.get('/api/csrf-token', (req, res) => {
  const token = randomBytes(32).toString('hex');
  req.session.csrfToken = token;
  res.json({ csrfToken: token });
});

app.post('/api/transfer', (req, res) => {
  const { csrfToken } = req.body;
  
  // ✅ Verify CSRF token
  if (csrfToken !== req.session.csrfToken) {
    return res.status(403).json({ error: 'Invalid CSRF token' });
  }
  
  // Process transfer...
});

// Client: Use CSRF token
function useCsrfToken() {
  const [csrfToken, setCsrfToken] = useState('');
  
  useEffect(() => {
    fetch('/api/csrf-token')
      .then(res => res.json())
      .then(data => setCsrfToken(data.csrfToken));
  }, []);
  
  return csrfToken;
}

function TransferForm() {
  const csrfToken = useCsrfToken();
  const [amount, setAmount] = useState('');
  
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    // ✅ Send CSRF token
    await fetch('/api/transfer', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRF-Token': csrfToken
      },
      body: JSON.stringify({ amount, csrfToken })
    });
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <input 
        type="number" 
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
      />
      <button type="submit">Transfer</button>
    </form>
  );
}

// ============================================
// 4️⃣ AUTHENTICATION & AUTHORIZATION
// ============================================

// Server: JWT tokens
app.post('/api/login', async (req, res) => {
  const { email, password } = req.body;
  const user = await verifyCredentials(email, password);
  
  if (!user) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }
  
  // ✅ Generate Access Token (short-lived: 15min)
  const accessToken = jwt.sign(
    { userId: user.id, email: user.email },
    process.env.JWT_SECRET!,
    { expiresIn: '15m' }
  );
  
  // ✅ Generate Refresh Token (long-lived: 7days)
  const refreshToken = jwt.sign(
    { userId: user.id },
    process.env.REFRESH_TOKEN_SECRET!,
    { expiresIn: '7d' }
  );
  
  // ✅ Store refresh token in httpOnly cookie
  res.cookie('refreshToken', refreshToken, {
    httpOnly: true,
    secure: true,
    sameSite: 'strict',
    maxAge: 7 * 24 * 60 * 60 * 1000
  });
  
  res.json({ accessToken });
});

// Client: Auth Context with auto-refresh
function AuthProvider({ children }) {
  const [accessToken, setAccessToken] = useState<string | null>(null);
  
  // ✅ Auto-refresh token before expire
  useEffect(() => {
    const refreshInterval = setInterval(async () => {
      const res = await fetch('/api/refresh', {
        method: 'POST',
        credentials: 'include'
      });
      
      if (res.ok) {
        const data = await res.json();
        setAccessToken(data.accessToken);
      }
    }, 14 * 60 * 1000); // 14 minutes
    
    return () => clearInterval(refreshInterval);
  }, []);
  
  return (
    <AuthContext.Provider value={{ accessToken }}>
      {children}
    </AuthContext.Provider>
  );
}

// ============================================
// 5️⃣ SECURE STORAGE
// ============================================

// ❌ BAD: Store sensitive data in localStorage
localStorage.setItem('token', accessToken); // XSS can steal!
localStorage.setItem('creditCard', cardNumber); // Never do this!

// ✅ GOOD: HttpOnly cookies for tokens
// Set in server response, cannot access via JS
res.cookie('refreshToken', token, {
  httpOnly: true,
  secure: true,
  sameSite: 'strict'
});

// ✅ GOOD: Memory-only for access tokens
const [accessToken, setAccessToken] = useState<string | null>(null);

// ============================================
// 6️⃣ API SECURITY
// ============================================

// 🛡️ Rate Limiting
const rateLimit = require('express-rate-limit');

const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Limit to 100 requests per window
  message: 'Too many requests, please try again later'
});

app.use('/api/', apiLimiter);

// 🛡️ Input Validation
import { z } from 'zod';

const transferSchema = z.object({
  amount: z.number().positive().max(1000000),
  accountNumber: z.string().regex(/^\d{10}$/),
  description: z.string().max(200).optional()
});

app.post('/api/transfer', async (req, res) => {
  try {
    // ✅ Validate input
    const data = transferSchema.parse(req.body);
    
    // Process transfer...
  } catch (error) {
    res.status(400).json({ error: 'Invalid input' });
  }
});

// ============================================
// 7️⃣ SECURITY HEADERS
// ============================================

// Helmet.js - Set security headers
import helmet from 'helmet';

app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'", "'unsafe-inline'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      imgSrc: ["'self'", "data:", "https:"],
    }
  },
  xFrameOptions: { action: 'deny' }, // Clickjacking protection
  noSniff: true, // X-Content-Type-Options
  referrerPolicy: { policy: 'no-referrer' }
}));
```

**🎯 Security Checklist:**

```typescript
// ✅ Security Checklist cho Trading Platform

const securityChecklist = {
  transport: {
    https: true,
    hsts: true,
    tlsVersion: 'TLS 1.3',
    certificateExpiry: 'Valid'
  },
  
  xssPrevention: {
    inputSanitization: true,
    outputEncoding: true,
    cspHeaders: true,
    dompurify: true
  },
  
  csrfProtection: {
    csrfTokens: true,
    sameSiteCookies: true,
    customHeaders: true
  },
  
  authentication: {
    jwtTokens: true,
    refreshTokens: true,
    tokenExpiry: '15m',
    passwordHashing: 'bcrypt'
  },
  
  storage: {
    noSensitiveLocalStorage: true,
    httpOnlyCookies: true,
    encryptedData: true
  },
  
  apiSecurity: {
    rateLimiting: true,
    inputValidation: true,
    cors: true,
    apiKeys: true
  },
  
  headers: {
    contentSecurityPolicy: true,
    xFrameOptions: true,
    xContentTypeOptions: true,
    referrerPolicy: true
  }
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

**Common Mistakes:**

```typescript
// ❌ MISTAKE 1: Store tokens in localStorage
localStorage.setItem('token', token); // XSS can steal

// ✅ FIX: HttpOnly cookies
res.cookie('token', token, { httpOnly: true, secure: true });

// ❌ MISTAKE 2: No input sanitization
<div dangerouslySetInnerHTML={{ __html: userInput }} />

// ✅ FIX: Sanitize
<div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(userInput) }} />

// ❌ MISTAKE 3: No CSRF protection
fetch('/api/transfer', { method: 'POST', body: data });

// ✅ FIX: Include CSRF token
fetch('/api/transfer', {
  method: 'POST',
  headers: { 'X-CSRF-Token': csrfToken },
  body: data
});

// ❌ MISTAKE 4: Weak password requirements
password.length >= 6

// ✅ FIX: Strong password policy
const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{12,}$/;

// ❌ MISTAKE 5: No rate limiting
app.post('/api/login', loginHandler);

// ✅ FIX: Rate limit login attempts
app.post('/api/login', loginRateLimiter, loginHandler);
```

**Monitoring & Logging:**

```typescript
// ✅ Security event logging
const securityLogger = {
  logFailedLogin(email: string, ip: string) {
    console.log(`[SECURITY] Failed login attempt: ${email} from ${ip}`);
    // Send to SIEM (Security Information and Event Management)
  },
  
  logSuspiciousActivity(userId: string, action: string) {
    console.log(`[SECURITY] Suspicious activity: User ${userId} - ${action}`);
    // Alert security team
  },
  
  logXSSAttempt(input: string, ip: string) {
    console.log(`[SECURITY] XSS attempt detected from ${ip}: ${input}`);
    // Block IP, notify admin
  }
};
```

---

**🎯 Kết Luận:**

**Performance Optimization (Q69):**
- ✅ 5-layer strategy: Build-time → Network → Rendering → State → Memory
- ✅ Measurable results: 70% faster load, 82% smaller bundle, 60 FPS
- ✅ Tools: Vite, React.memo, Zustand, react-window, Chrome DevTools

**Security (Q70):**
- ✅ 7-layer defense: HTTPS → XSS → CSRF → Auth → Storage → API → Headers
- ✅ Comprehensive protection: Input sanitization, JWT tokens, rate limiting
- ✅ Tools: DOMPurify, Helmet, Zod, bcrypt

**💡 Key Takeaway:**
- Performance & Security KHÔNG phải optional - là MUST-HAVE cho production apps
- Measure & Monitor trong production
- Defense in depth: Multiple layers of protection

---
