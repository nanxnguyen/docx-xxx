# 📊 Q51: Performance Monitoring & APM - Giám Sát Hiệu Suất Ứng Dụng (Bản Tiếng Việt)

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (4-5 phút):**

**"APM tracking: Core Web Vitals (LCP, INP, CLS), Sentry (error tracking), DataDog RUM (user monitoring). Performance budgets, source maps trong production, Chrome DevTools profiling, custom metrics."**

**🔑 7 Thành Phần APM:**

**1. Core Web Vitals - Google Metrics:**
- **LCP** (Largest Contentful Paint): < 2.5s (time to main content)
- **INP** (Interaction to Next Paint): < 200ms (user interaction lag) - thay FID
- **CLS** (Cumulative Layout Shift): < 0.1 (visual stability)
- **Tool**: Lighthouse, PageSpeed Insights, Web Vitals library
- **Impact**: SEO ranking, user experience

**2. Sentry - Error Tracking:**
- **Setup**: `Sentry.init()` với DSN, environment, release
- **Features**: Error grouping, breadcrumbs, user context, performance tracing
- **Source maps**: Upload để debug minified code trong production
- **Alerts**: Email/Slack khi error spike
- **Best practice**: Sampling rate (avoid quota), filter sensitive data

**3. DataDog RUM (Real User Monitoring):**
- **Metrics**: Page load, JS errors, resources, user actions, long tasks
- **Session replay**: Record user sessions (find bugs)
- **APM Integration**: Connect frontend errors với backend traces
- **Custom events**: Track business metrics (purchases, clicks)

**4. Performance Budgets:**
- **Define**: Max bundle size (JS < 200KB), max LCP < 2.5s
- **Enforce**: Webpack BundleBudgetPlugin, Lighthouse CI fail build
- **Monitor**: Track trends, alert khi vượt budget

**5. Source Maps Production:**
- **Purpose**: Debug minified code trong production errors
- **Security**: Upload private (Sentry/DataDog), không serve public
- **Generate**: `webpack devtool: 'hidden-source-map'`

**6. Chrome DevTools Profiling:**
- **Performance tab**: Record timeline, find bottlenecks (long tasks)
- **Coverage tab**: Unused JS/CSS (tree-shake candidates)
- **Memory tab**: Heap snapshots, memory leaks (detached nodes)
- **Network tab**: Waterfall, slow resources

**7. Custom Performance Metrics:**
```javascript
// Performance API
performance.mark('checkout-start');
// ... logic
performance.mark('checkout-end');
performance.measure('checkout', 'checkout-start', 'checkout-end');
const measure = performance.getEntriesByName('checkout')[0];
// Send to APM: Sentry, DataDog
```

**⚠️ Lỗi Thường Gặp:**
- Không set performance budgets → bundle bloat
- Source maps public → security risk (expose code)
- Không filter PII trong error logs → GDPR violation
- Quá nhiều custom events → quota limit, performance overhead

**💡 Kiến Thức Senior:**
- **PerformanceObserver**: Monitor FCP, LCP, INP realtime (không dùng polling)
- **Session replay privacy**: Mask sensitive inputs, credit cards
- **Distributed tracing**: Trace request từ frontend → backend → DB
- **Synthetic monitoring**: Automated tests (Pingdom, Checkly) để catch issues
- **Alerting thresholds**: P95, P99 thay vì average (avoid outliers skew data)

> **Câu hỏi phỏng vấn Senior Frontend Developer**  
> **Độ khó:** ⭐⭐⭐⭐⭐ (Expert Level)  
> **Thời gian trả lời:** 15-20 phút

---

## 📋 **Mục Lục**

1. [Core Web Vitals - Chỉ Số Hiệu Suất Web Cốt Lõi](#1-core-web-vitals)
2. [Sentry Error Tracking - Theo Dõi Lỗi](#2-sentry-error-tracking)
3. [DataDog RUM (Real User Monitoring) - Giám Sát Người Dùng Thực](#3-datadog-rum)
4. [Performance Budgets - Ngân Sách Hiệu Suất](#4-performance-budgets)
5. [Source Maps trong Production](#5-source-maps-in-production)
6. [Chrome DevTools Profiling - Phân Tích Hiệu Suất](#6-chrome-devtools-profiling)
7. [Custom Performance Metrics - Chỉ Số Tùy Chỉnh](#7-custom-performance-metrics)
8. [Alerting & Monitoring Dashboard - Cảnh Báo & Dashboard Giám Sát](#8-alerting-monitoring-dashboard)

---

## 1. Core Web Vitals

### **1.1. Core Web Vitals là gì?**

> **Core Web Vitals** là tập hợp các **chỉ số hiệu suất quan trọng** do Google định nghĩa, ảnh hưởng trực tiếp đến **trải nghiệm người dùng** và **thứ hạng SEO**.

**📌 3 chỉ số cốt lõi:**

```
┌──────────────────────────────────────────────────────────────┐
│            CORE WEB VITALS (2024) - CHỈ SỐ HIỆU SUẤT         │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  📊 **LCP (Largest Contentful Paint)**                      │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                    │
│  🇻🇳 ĐO TỐCĐỘ TẢI TRANG                                    │
│  Thời gian để phần tử lớn nhất hiển thị trên màn hình       │
│                                                              │
│  ✅ Tốt: ≤ 2.5 giây                                         │
│  ⚠️  Cần cải thiện: 2.5-4 giây                              │
│  ❌ Kém: > 4 giây                                           │
│                                                              │
│  💡 Ví dụ phần tử "lớn nhất":                               │
│     - Ảnh hero (banner chính)                                │
│     - Video thumbnail                                        │
│     - Block text lớn                                         │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ⚡ **INP (Interaction to Next Paint)** [MỚI từ 2024]      │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                    │
│  🇻🇳 ĐO TỐC ĐỘ PHẢN HỒI TƯƠNG TÁC                          │
│  Thời gian từ khi user click/tap đến khi màn hình cập nhật  │
│                                                              │
│  ✅ Tốt: ≤ 200ms                                            │
│  ⚠️  Cần cải thiện: 200-500ms                               │
│  ❌ Kém: > 500ms                                            │
│                                                              │
│  💡 Ví dụ tương tác:                                        │
│     - Click button "Add to Cart"                             │
│     - Mở dropdown menu                                       │
│     - Nhập text vào form                                     │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  📐 **CLS (Cumulative Layout Shift)**                       │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                    │
│  🇻🇳 ĐO ĐỘ ỔN ĐỊNH GIAO DIỆN                               │
│  Điểm số tích lũy của các lần layout bị "nhảy" bất ngờ      │
│                                                              │
│  ✅ Tốt: ≤ 0.1                                              │
│  ⚠️  Cần cải thiện: 0.1-0.25                                │
│  ❌ Kém: > 0.25                                             │
│                                                              │
│  💡 Ví dụ layout shift:                                     │
│     - Ảnh load muộn → đẩy content xuống                     │
│     - Quảng cáo hiện bất ngờ → đẩy button xuống             │
│     - Font load muộn → thay đổi kích thước text             │
│                                                              │
└──────────────────────────────────────────────────────────────┘

⚠️  **LƯU Ý:** FID (First Input Delay) đã NGƯNG SỬ DỤNG từ tháng 3/2024
   → Thay bằng INP (Interaction to Next Paint)
```

### **1.2. Đo Lường Core Web Vitals**

```typescript
// ===================================================
// 📊 **TÍCH HỢP THƯ VIỆN WEB-VITALS**
// ===================================================

// Cài đặt: npm install web-vitals
import { onCLS, onINP, onLCP, onFCP, onTTFB } from 'web-vitals';

// ✅ Interface cho metric data
interface Metric {
  name: 'CLS' | 'INP' | 'LCP' | 'FCP' | 'TTFB';
  value: number;              // 🇻🇳 Giá trị metric (ms hoặc score)
  rating: 'good' | 'needs-improvement' | 'poor'; // 🇻🇳 Đánh giá
  delta: number;              // 🇻🇳 Thay đổi so với lần đo trước
  id: string;                 // 🇻🇳 ID duy nhất cho page load này
  navigationType: 'navigate' | 'reload' | 'back-forward'; // 🇻🇳 Loại navigation
}

// ✅ Function gửi metrics đến analytics server
function sendToAnalytics(metric: Metric) {
  const body = JSON.stringify({
    name: metric.name,
    value: metric.value,
    rating: metric.rating,
    delta: metric.delta,
    id: metric.id,
    navigationType: metric.navigationType,
    // 🇻🇳 Thêm thông tin context
    url: window.location.href,
    userAgent: navigator.userAgent,
    timestamp: Date.now(),
  });

  // ✅ Dùng navigator.sendBeacon() - GỬI DỮ LIỆU NGAY CẢ KHI USER RỜI TRANG
  // 🇻🇳 sendBeacon() đảm bảo request vẫn được gửi khi user close tab/navigate đi
  if (navigator.sendBeacon) {
    navigator.sendBeacon('/analytics/web-vitals', body);
  } else {
    // 🇻🇳 Fallback cho browser cũ không hỗ trợ sendBeacon
    fetch('/analytics/web-vitals', {
      method: 'POST',
      body,
      keepalive: true, // 🇻🇳 Giữ request alive khi page unload
    });
  }
}

// ✅ Khởi tạo tracking cho TẤT CẢ Core Web Vitals
export function initWebVitals() {
  // 🇻🇳 Đo 3 chỉ số chính
  onLCP(sendToAnalytics);  // 📊 Largest Contentful Paint
  onINP(sendToAnalytics);  // ⚡ Interaction to Next Paint
  onCLS(sendToAnalytics);  // 📐 Cumulative Layout Shift
  
  // 🇻🇳 Đo thêm 2 chỉ số phụ (không phải Core Web Vitals nhưng hữu ích)
  onFCP(sendToAnalytics);  // 🎨 First Contentful Paint (trang bắt đầu hiển thị nội dung)
  onTTFB(sendToAnalytics); // 🚀 Time to First Byte (thời gian server phản hồi)
}

// ===================================================
// 🎯 **SỬ DỤNG TRONG APP**
// ===================================================

// main.tsx (hoặc index.tsx)
import { initWebVitals } from './analytics/web-vitals';

// 🇻🇳 CHỈ khởi động tracking ở PRODUCTION (không track ở local dev)
if (import.meta.env.PROD) { // Hoặc: process.env.NODE_ENV === 'production'
  initWebVitals();
}

// 💡 CÁCH HOẠT ĐỘNG:
// 1. User truy cập trang
// 2. web-vitals library tự động đo các metrics
// 3. Khi có metric (LCP, INP, CLS...), callback sendToAnalytics được gọi
// 4. Dữ liệu được gửi về server analytics
// 5. Server lưu vào database → Visualize trên dashboard
```

---

## 2. Sentry Error Tracking

### **2.1. Sentry là gì?**

> **Sentry** là nền tảng **giám sát lỗi real-time** giúp phát hiện, theo dõi và khắc phục lỗi trong production.

**📌 Tính năng chính:**
- ✅ **Error Tracking:** Bắt tất cả JavaScript errors, unhandled promises
- ✅ **Performance Monitoring:** Đo thời gian load, API calls
- ✅ **Session Replay:** Xem lại video màn hình user khi gặp lỗi
- ✅ **Breadcrumbs:** Theo dõi các hành động user trước khi lỗi xảy ra
- ✅ **Source Maps:** Hiển thị code gốc (chưa minify) khi debug

### **2.2. Cấu Hình Sentry**

```typescript
// ===================================================
// 🔧 **CÀI ĐẶT SENTRY**
// ===================================================

// 1️⃣ Cài package
// npm install @sentry/react

// 2️⃣ Khởi tạo Sentry
// sentry.ts
import * as Sentry from '@sentry/react';
import { BrowserTracing } from '@sentry/tracing';

// ✅ Khởi tạo Sentry với đầy đủ config
Sentry.init({
  // 🇻🇳 DSN (Data Source Name) - URL để gửi lỗi về Sentry server
  dsn: 'https://examplePublicKey@o0.ingest.sentry.io/0',
  
  // 🇻🇳 Tên môi trường (dev/staging/production)
  environment: import.meta.env.MODE,
  
  // 🇻🇳 Version app (để tracking lỗi theo version)
  release: `my-app@${import.meta.env.VITE_APP_VERSION}`,
  
  // ✅ Tích hợp Performance Monitoring
  integrations: [
    // 🇻🇳 Tự động track navigation, XHR/Fetch requests
    new BrowserTracing({
      // 🇻🇳 Track React Router navigation
      routingInstrumentation: Sentry.reactRouterV6Instrumentation(
        React.useEffect,
        useLocation,
        useNavigationType,
        createRoutesFromChildren,
        matchRoutes
      ),
    }),
    
    // 🇻🇳 Session Replay - Ghi lại video màn hình user
    new Sentry.Replay({
      maskAllText: false,      // 🇻🇳 Có che (mask) toàn bộ text không?
      blockAllMedia: false,    // 🇻🇳 Có block images/videos không?
    }),
  ],
  
  // 🇻🇳 % session được ghi lại (0.1 = 10%)
  replaysSessionSampleRate: 0.1,
  
  // 🇻🇳 % session có LỖI được ghi lại (1.0 = 100% - ghi lại TẤT CẢ session có lỗi)
  replaysOnErrorSampleRate: 1.0,
  
  // 🇻🇳 % transactions được track (0.5 = 50% traffic)
  tracesSampleRate: 0.5,
  
  // ✅ Lọc bớt errors không cần thiết
  beforeSend(event, hint) {
    // 🇻🇳 Bỏ qua lỗi từ browser extensions
    if (event.exception?.values?.[0]?.value?.includes('chrome-extension://')) {
      return null; // 🇻🇳 Không gửi lên Sentry
    }
    
    // 🇻🇳 Bỏ qua network errors (API down)
    if (event.exception?.values?.[0]?.type === 'NetworkError') {
      return null;
    }
    
    return event; // 🇻🇳 Gửi event bình thường
  },
  
  // ✅ Thêm thông tin context cho mỗi error
  beforeBreadcrumb(breadcrumb, hint) {
    // 🇻🇳 Thêm timestamp cho mỗi breadcrumb
    breadcrumb.timestamp = Date.now() / 1000;
    
    // 🇻🇳 Che giấu sensitive data trong breadcrumb
    if (breadcrumb.category === 'console' && breadcrumb.message) {
      breadcrumb.message = breadcrumb.message.replace(/password=\w+/g, 'password=[REDACTED]');
    }
    
    return breadcrumb;
  },
});

// ===================================================
// 🎯 **SỬ DỤNG ERROR BOUNDARY**
// ===================================================

import { ErrorBoundary } from '@sentry/react';

export const App = () => {
  return (
    <ErrorBoundary
      // 🇻🇳 Fallback UI khi có lỗi
      fallback={({ error, resetError }) => (
        <div>
          <h1>❌ Đã xảy ra lỗi!</h1>
          <p>{error.message}</p>
          <button onClick={resetError}>🔄 Thử lại</button>
        </div>
      )}
      
      // 🇻🇳 Callback khi có lỗi xảy ra
      onError={(error, errorInfo) => {
        // 🇻🇳 Thêm context cho error
        Sentry.setContext('componentStack', {
          stack: errorInfo.componentStack,
        });
        
        console.error('Error caught by boundary:', error);
      }}
    >
      <YourApp />
    </ErrorBoundary>
  );
};

// ===================================================
// 🎯 **MANUAL ERROR REPORTING - BÁO LỖI THỦ CÔNG**
// ===================================================

// 🇻🇳 Ví dụ: Bắt lỗi trong async function
async function fetchUserData(userId: string) {
  try {
    const response = await fetch(`/api/users/${userId}`);
    if (!response.ok) throw new Error('Failed to fetch user');
    return await response.json();
  } catch (error) {
    // ✅ Gửi lỗi lên Sentry với context
    Sentry.captureException(error, {
      tags: {
        section: 'user-fetch',  // 🇻🇳 Tag để phân loại
        userId,
      },
      extra: {
        endpoint: `/api/users/${userId}`, // 🇻🇳 Thông tin thêm
        timestamp: new Date().toISOString(),
      },
    });
    
    throw error; // 🇻🇳 Re-throw để component có thể handle
  }
}

// 🇻🇳 Ví dụ: Track user actions (breadcrumbs)
function handleCheckout() {
  // ✅ Thêm breadcrumb để biết user đã làm gì trước khi lỗi
  Sentry.addBreadcrumb({
    category: 'user-action',
    message: 'User clicked checkout button',
    level: 'info',
    data: {
      cartValue: 299.99,
      itemCount: 3,
    },
  });
  
  // ... checkout logic
}
```

---

## 3. DataDog RUM (Real User Monitoring)

### **3.1. DataDog RUM là gì?**

> **DataDog RUM (Real User Monitoring)** là nền tảng giám sát **trải nghiệm người dùng thực tế** (không phải synthetic testing), giúp theo dõi hiệu suất frontend trong production.

**📌 Khác biệt với Sentry:**

```
┌─────────────────────────────────────────────────────────────┐
│              SENTRY vs DATADOG - SO SÁNH                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  SENTRY 🐛                    │  DATADOG 📊                │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━│━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  ✅ Error Tracking chuyên sâu │ ✅ RUM (Real User Monitor)  │
│  ✅ Session Replay           │ ✅ APM (Application Perf)   │
│  ✅ Performance Monitoring   │ ✅ Log Management           │
│  ⚠️  Metrics/Logs hạn chế    │ ✅ Infrastructure Monitor   │
│                              │ ✅ Tích hợp Backend/Infra   │
│                              │                             │
│  🎯 Use case:                │ 🎯 Use case:               │
│  - Chỉ cần track errors      │ - Cần full observability    │
│  - Budget hạn chế            │ - Monitor cả FE + BE + Infra│
│  - Small/Mid team            │ - Large enterprise team     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### **3.2. Cấu Hình DataDog RUM**

```typescript
// ===================================================
// 🔧 **CÀI ĐẶT DATADOG RUM**
// ===================================================

// 1️⃣ Cài package
// npm install @datadog/browser-rum

// 2️⃣ Khởi tạo DataDog RUM
// datadog.ts
import { datadogRum } from '@datadog/browser-rum';

datadogRum.init({
  // 🇻🇳 Application ID (lấy từ DataDog dashboard)
  applicationId: 'your-app-id',
  
  // 🇻🇳 Client Token (public token, safe to expose)
  clientToken: 'your-client-token',
  
  // 🇻🇳 Site region (us1, us3, us5, eu1, ap1...)
  site: 'datadoghq.com',
  
  // 🇻🇳 Service name (để phân biệt các service khác nhau)
  service: 'my-frontend-app',
  
  // 🇻🇳 Environment
  env: import.meta.env.MODE, // 'production', 'staging', 'development'
  
  // 🇻🇳 Version app
  version: '1.0.0',
  
  // ✅ % session được sample (0.5 = 50% traffic)
  sessionSampleRate: 100, // 🇻🇳 100% trong dev, giảm xuống 20-50% ở production
  
  // ✅ % session được Replay (ghi lại video)
  sessionReplaySampleRate: 20, // 🇻🇳 Chỉ replay 20% sessions để tiết kiệm chi phí
  
  // ✅ Track các loại interactions
  trackInteractions: true, // 🇻🇳 Track clicks, hovers, scrolls
  
  // ✅ Track Resources (JS, CSS, Images...)
  trackResources: true,
  
  // ✅ Track Long Tasks (tasks chạy > 50ms)
  trackLongTasks: true,
  
  // ✅ Default privacy level
  defaultPrivacyLevel: 'mask-user-input', // 🇻🇳 'allow' | 'mask' | 'mask-user-input'
  
  // ✅ Allowed tracing origins (cho Distributed Tracing)
  allowedTracingOrigins: [
    'https://api.example.com',  // 🇻🇳 API backend
    /https:\/\/.*\.example\.com/, // 🇻🇳 Regex cho subdomains
  ],
  
  // ✅ Before Send callback - lọc/chỉnh sửa data trước khi gửi
  beforeSend: (event) => {
    // 🇻🇳 Che giấu sensitive data
    if (event.type === 'resource' && event.resource.url.includes('api/auth')) {
      event.resource.url = event.resource.url.replace(/token=\w+/g, 'token=[REDACTED]');
    }
    
    return true; // 🇻🇳 Trả về false để KHÔNG gửi event này
  },
});

// ✅ Bắt đầu tracking
datadogRum.startSessionReplayRecording();

// ===================================================
// 🎯 **CUSTOM USER ACTIONS - TRACKING HÀNH ĐỘNG USER**
// ===================================================

import { datadogRum } from '@datadog/browser-rum';

// 🇻🇳 Track custom action
function handleAddToCart(product: Product) {
  datadogRum.addAction('add-to-cart', {
    productId: product.id,
    productName: product.name,
    price: product.price,
    category: product.category,
  });
  
  // ... add to cart logic
}

// 🇻🇳 Track tình trạng user
datadogRum.setUser({
  id: '123',
  name: 'Nguyen Van A',
  email: 'nguyenvana@example.com',
  plan: 'premium', // 🇻🇳 Custom attribute
});

// 🇻🇳 Thêm context cho toàn bộ session
datadogRum.setGlobalContextProperty('experiment_variant', 'B'); // 🇻🇳 A/B testing
datadogRum.setGlobalContextProperty('user_segment', 'enterprise');

// ===================================================
// 🎯 **CUSTOM TIMING - ĐO THỜI GIAN TÙY CHỈNH**
// ===================================================

// 🇻🇳 Ví dụ: Đo thời gian render React component
import { datadogRum } from '@datadog/browser-rum';
import { useEffect } from 'react';

const HeavyComponent = () => {
  useEffect(() => {
    // ✅ Bắt đầu đo
    const startTime = performance.now();
    
    // ... component mount logic
    
    // ✅ Kết thúc đo và gửi lên DataDog
    const duration = performance.now() - startTime;
    datadogRum.addTiming('heavy_component_mount', duration);
  }, []);
  
  return <div>...</div>;
};
```

---

## 4. Performance Budgets

### **4.1. Performance Budget là gì?**

> **Performance Budget** là **ngân sách hiệu suất** - giới hạn cứng cho các metrics (bundle size, load time...). Nếu vượt budget → **build fail!**

**📌 Tại sao cần Performance Budget?**

```
🚨 VẤN ĐỀ THƯỜNG GẶP:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❌ Dev thêm library → Bundle tăng từ 200KB lên 500KB
❌ Không ai để ý → Deploy lên production
❌ User phàn nàn trang load chậm
❌ SEO ranking giảm
❌ Conversion rate giảm

✅ GIẢI PHÁP: PERFORMANCE BUDGET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Set limit: "Bundle chính không được > 300KB"
✅ CI/CD check mỗi commit
✅ Vượt budget → Build fail → Force developer optimize
```

### **4.2. Cấu Hình Performance Budget**

```json
// ===================================================
// 📦 **WEBPACK PERFORMANCE BUDGET**
// ===================================================

// webpack.config.js
export default {
  // ... other config
  
  performance: {
    // 🇻🇳 Cảnh báo khi vượt ngưỡng (không block build)
    hints: 'warning', // 'warning' | 'error' | false
    
    // 🇻🇳 Giới hạn kích thước ENTRYPOINT (main bundle) - 250KB
    maxEntrypointSize: 250 * 1024, // 250KB
    
    // 🇻🇳 Giới hạn kích thước mỗi FILE asset (JS/CSS/Image) - 300KB
    maxAssetSize: 300 * 1024, // 300KB
    
    // 🇻🇳 Chỉ check các file .js
    assetFilter: function(assetFilename) {
      return assetFilename.endsWith('.js');
    },
  },
};
```

```javascript
// ===================================================
// 📊 **LIGHTHOUSE CI BUDGET**
// ===================================================

// lighthouserc.json
{
  "ci": {
    "collect": {
      "numberOfRuns": 3 // 🇻🇳 Chạy Lighthouse 3 lần lấy trung bình
    },
    "assert": {
      "preset": "lighthouse:recommended", // 🇻🇳 Dùng preset khuyến nghị của Google
      "assertions": {
        // 🇻🇳 Core Web Vitals budgets
        "largest-contentful-paint": ["error", { "maxNumericValue": 2500 }], // ≤ 2.5s
        "cumulative-layout-shift": ["error", { "maxNumericValue": 0.1 }],   // ≤ 0.1
        "total-blocking-time": ["error", { "maxNumericValue": 300 }],       // ≤ 300ms
        
        // 🇻🇳 Performance score phải ≥ 90/100
        "performance-budget": ["error", { "minScore": 0.9 }],
        
        // 🇻🇳 Resource budgets
        "resource-summary:document:size": ["error", { "maxNumericValue": 50000 }],  // HTML ≤ 50KB
        "resource-summary:script:size": ["error", { "maxNumericValue": 300000 }],   // JS ≤ 300KB
        "resource-summary:stylesheet:size": ["error", { "maxNumericValue": 50000 }], // CSS ≤ 50KB
        "resource-summary:image:size": ["error", { "maxNumericValue": 500000 }],    // Images ≤ 500KB
        "resource-summary:font:size": ["error", { "maxNumericValue": 100000 }],     // Fonts ≤ 100KB
        
        // 🇻🇳 Không được có quá nhiều requests
        "resource-summary:third-party:count": ["warn", { "maxNumericValue": 10 }],  // ≤ 10 third-party requests
      }
    },
    "upload": {
      "target": "temporary-public-storage" // 🇻🇳 Hoặc upload lên Lighthouse CI server riêng
    }
  }
}
```

```yaml
# ===================================================
# 🔄 **GITHUB ACTIONS - LIGHTHOUSE CI**
# ===================================================

# .github/workflows/lighthouse-ci.yml
name: Lighthouse CI
on: [pull_request]

jobs:
  lighthouse:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Build app
        run: npm run build
      
      - name: Run Lighthouse CI
        run: |
          npm install -g @lhci/cli
          lhci autorun
        env:
          LHCI_GITHUB_APP_TOKEN: ${{ secrets.LHCI_GITHUB_APP_TOKEN }}
      
      # 🇻🇳 Kết quả sẽ comment trực tiếp vào PR
      # ✅ Pass: Performance score 92/100, all budgets met
      # ❌ Fail: LCP 3.2s (budget: 2.5s), JS bundle 450KB (budget: 300KB)
```

---

## 5. Source Maps trong Production

### **5.1. Source Maps là gì?**

> **Source Maps** là file mapping giúp **chuyển code đã minify/transpile** (production code) về **code gốc** (source code) để dễ debug.

**📌 Vấn đề:**

```javascript
// 🇻🇳 CODE GỐC (dễ đọc)
function calculateTotal(items) {
  return items.reduce((sum, item) => sum + item.price, 0);
}

// 🇻🇳 SAU KHI MINIFY (production - khó đọc)
function c(i){return i.reduce((s,t)=>s+t.p,0)}

// 🚨 Khi có lỗi trong production:
// ❌ Error at c:1:42
// 👤 Developer: "c là cái gì? 1:42 ở đâu?"

// ✅ VỚI SOURCE MAP:
// ✅ Error at calculateTotal (cart.ts:15:42)
// 👤 Developer: "Ah, lỗi ở hàm calculateTotal dòng 15!"
```

### **5.2. Cấu Hình Source Maps**

```typescript
// ===================================================
// 🔧 **VITE SOURCE MAPS CONFIG**
// ===================================================

// vite.config.ts
import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    // 🇻🇳 Loại source map (trade-off giữa tốc độ build và chất lượng map)
    sourcemap: 'hidden', // 'hidden' | true | false | 'inline'
    
    // 🇻🇳 Các loại source map:
    // ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    // 'hidden':  Tạo .map file NHƯNG không reference trong .js
    //            → User không download, chỉ upload lên Sentry
    //            → TỐT NHẤT cho production
    //
    // true:      Tạo .map file VÀ reference trong .js
    //            → User sẽ download .map file
    //            → Tốt cho staging/dev
    //
    // 'inline':  Embed source map vào trong .js file
    //            → File .js rất lớn
    //            → CHỈ dùng cho dev
    //
    // false:     KHÔNG tạo source map
    //            → Không debug được trong production
    //            → CHỈ dùng khi đã có monitoring tốt
  },
});
```

```typescript
// ===================================================
// 🚀 **UPLOAD SOURCE MAPS LÊN SENTRY**
// ===================================================

// vite.config.ts
import { defineConfig } from 'vite';
import { sentryVitePlugin } from '@sentry/vite-plugin';

export default defineConfig({
  build: {
    sourcemap: 'hidden', // 🇻🇳 Tạo .map file nhưng không expose cho user
  },
  
  plugins: [
    // ✅ Plugin tự động upload source maps lên Sentry khi build
    sentryVitePlugin({
      // 🇻🇳 Sentry org & project
      org: 'your-org',
      project: 'your-project',
      
      // 🇻🇳 Auth token (lấy từ Sentry settings)
      authToken: process.env.SENTRY_AUTH_TOKEN,
      
      // 🇻🇳 Tự động tạo release trong Sentry
      release: {
        name: process.env.VITE_APP_VERSION, // e.g. "1.2.3"
        uploadSourceMaps: true,
        cleanArtifacts: true, // 🇻🇳 Xóa source maps cũ
      },
      
      // 🇻🇳 CHỈ upload trong production build
      disable: process.env.NODE_ENV !== 'production',
      
      // 🇻🇳 Silent mode (không log ra console)
      silent: true,
    }),
  ],
});

// 🇻🇳 CÁCH HOẠT ĐỘNG:
// 1. Build app → Tạo main.js + main.js.map
// 2. sentryVitePlugin upload main.js.map lên Sentry
// 3. XÓA main.js.map trên server production (không deploy file .map)
// 4. Deploy chỉ có main.js (không có .map reference)
// 5. Khi có lỗi → Sentry dùng .map đã upload để hiển thị code gốc
```

---

## 6. Chrome DevTools Profiling

### **6.1. Performance Panel**

> **Performance Panel** trong Chrome DevTools giúp phân tích **hiệu suất runtime** của app (CPU usage, rendering, network...).

**📌 Các bước profiling:**

```
┌─────────────────────────────────────────────────────────────┐
│         CHROME DEVTOOLS PERFORMANCE PROFILING               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1️⃣ Mở Chrome DevTools → Tab "Performance"                │
│                                                             │
│  2️⃣ Click "Record" 🔴                                      │
│                                                             │
│  3️⃣ Thực hiện hành động cần test:                         │
│     - Load trang                                            │
│     - Click button                                          │
│     - Scroll                                                │
│     - Navigate giữa các routes                             │
│                                                             │
│  4️⃣ Click "Stop" ⏹️                                        │
│                                                             │
│  5️⃣ Phân tích kết quả:                                    │
│     📊 FPS Chart: Xem có bị drop frame không (< 60fps)     │
│     🔥 CPU Chart: Phần nào tốn CPU (Scripting/Rendering)   │
│     🎨 Main Thread: Xem long tasks (> 50ms)                │
│     🌐 Network: Xem requests nào chậm                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**📌 Phân tích Long Tasks:**

```typescript
// 🇻🇳 CÁCH PHÁT HIỆN LONG TASKS TRONG CODE

// ❌ VÍ DỤ: Long Task (blocking main thread)
function processLargeData(data: any[]) {
  // 🚨 Loop qua 10,000 items → Block main thread 2-3 giây!
  const result = [];
  for (let i = 0; i < 10000; i++) {
    result.push(heavyCalculation(data[i])); // Mỗi lần tính 0.3ms → Tổng 3 giây!
  }
  return result;
}

// ✅ GIẢI PHÁP 1: Dùng Web Worker (chạy ở background thread)
// worker.ts
self.addEventListener('message', (e) => {
  const { data } = e.data;
  
  // 🇻🇳 Chạy heavy calculation trong worker (không block UI)
  const result = data.map(item => heavyCalculation(item));
  
  // 🇻🇳 Gửi kết quả về main thread
  self.postMessage({ result });
});

// main.ts
const worker = new Worker(new URL('./worker.ts', import.meta.url));

function processLargeDataAsync(data: any[]): Promise<any[]> {
  return new Promise((resolve) => {
    worker.postMessage({ data });
    
    worker.addEventListener('message', (e) => {
      resolve(e.data.result);
    }, { once: true });
  });
}

// ✅ GIẢI PHÁP 2: Chia nhỏ task (chunking)
async function processLargeDataChunked(data: any[]) {
  const CHUNK_SIZE = 100; // 🇻🇳 Mỗi lần xử lý 100 items
  const result = [];
  
  for (let i = 0; i < data.length; i += CHUNK_SIZE) {
    const chunk = data.slice(i, i + CHUNK_SIZE);
    
    // 🇻🇳 Xử lý 1 chunk
    result.push(...chunk.map(item => heavyCalculation(item)));
    
    // ✅ Yield về main thread để browser có thể render
    await new Promise(resolve => setTimeout(resolve, 0));
  }
  
  return result;
}
```

---

## 7. Custom Performance Metrics

### **7.1. Performance API**

```typescript
// ===================================================
// ⏱️  **PERFORMANCE.MARK() & PERFORMANCE.MEASURE()**
// ===================================================

// 🇻🇳 Đo thời gian CHÍNH XÁC của 1 đoạn code

// ✅ Đánh dấu thời điểm BẮT ĐẦU
performance.mark('data-fetch-start');

// ... fetch data từ API
await fetchData();

// ✅ Đánh dấu thời điểm KẾT THÚC
performance.mark('data-fetch-end');

// ✅ Tính thời gian giữa 2 marks
performance.measure(
  'data-fetch-duration',    // 🇻🇳 Tên measure
  'data-fetch-start',       // 🇻🇳 Start mark
  'data-fetch-end'          // 🇻🇳 End mark
);

// ✅ Lấy kết quả
const measure = performance.getEntriesByName('data-fetch-duration')[0];
console.log(`Data fetch took: ${measure.duration}ms`);

// ✅ Gửi lên analytics
sendToAnalytics({
  metric: 'data-fetch-duration',
  value: measure.duration,
});

// ===================================================
// 🎯 **VÍ DỤ THỰC TẾ: ĐO THỜI GIAN RENDER COMPONENT**
// ===================================================

import { useEffect } from 'react';

const HeavyComponent = () => {
  useEffect(() => {
    // ✅ Đánh dấu khi component mount
    performance.mark('heavy-component-mount-end');
    
    // ✅ Tính thời gian từ khi navigation start đến khi component mount
    performance.measure(
      'heavy-component-mount-time',
      'navigationStart', // 🇻🇳 Built-in mark của browser
      'heavy-component-mount-end'
    );
    
    const measure = performance.getEntriesByName('heavy-component-mount-time')[0];
    
    // 🇻🇳 Gửi lên DataDog/Sentry
    datadogRum.addTiming('heavy-component-mount', measure.duration);
  }, []);
  
  return <div>...</div>;
};
```

### **7.2. User Timing API - Đo các metrics tùy chỉnh**

```typescript
// ===================================================
// 📊 **ĐO THỜI GIAN INTERACTIVE CỦA FORM**
// ===================================================

const LoginForm = () => {
  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    
    // ✅ Bắt đầu đo
    performance.mark('login-start');
    
    try {
      const response = await login(username, password);
      
      // ✅ Đo thời gian thành công
      performance.mark('login-success');
      performance.measure('login-duration-success', 'login-start', 'login-success');
      
      const measure = performance.getEntriesByName('login-duration-success')[0];
      
      // 🇻🇳 Gửi metric: Thời gian login thành công
      datadogRum.addTiming('login-success-time', measure.duration);
      
    } catch (error) {
      // ✅ Đo thời gian thất bại
      performance.mark('login-error');
      performance.measure('login-duration-error', 'login-start', 'login-error');
      
      const measure = performance.getEntriesByName('login-duration-error')[0];
      
      // 🇻🇳 Gửi metric: Thời gian login thất bại (để detect slow API)
      datadogRum.addTiming('login-error-time', measure.duration);
    }
  };
  
  return <form onSubmit={handleSubmit}>...</form>;
};
```

---

## 8. Alerting & Monitoring Dashboard

### **8.1. Thiết Lập Alerts trong Sentry**

```javascript
// ===================================================
// 🚨 **SENTRY ALERTS CONFIG**
// ===================================================

// 🇻🇳 Cấu hình Alert Rules trong Sentry UI:

/*
1️⃣ ERROR RATE SPIKE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Condition: Error rate tăng > 50% so với 1 giờ trước
Action:
  - Slack notification → #alerts channel
  - Email → team-lead@example.com
  - PagerDuty incident (severity: HIGH)

2️⃣ NEW ERROR TYPE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Condition: Xuất hiện error chưa từng thấy
Action:
  - Slack notification với stack trace
  - Assign to on-call engineer

3️⃣ HIGH FREQUENCY ERROR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Condition: Error xảy ra > 100 lần trong 5 phút
Action:
  - Email + Slack
  - Auto-create JIRA ticket

4️⃣ SLOW TRANSACTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Condition: Transaction duration > 3 giây (P95)
Action:
  - Slack notification với transaction details
  - Tag: performance-issue
*/
```

### **8.2. Thiết Lập Alerts trong DataDog**

```javascript
// ===================================================
// 📊 **DATADOG ALERTS (via API hoặc UI)**
// ===================================================

// 🇻🇳 Ví dụ: Tạo Monitor qua DataDog API

const monitorConfig = {
  // 🇻🇳 Tên monitor
  name: 'High Error Rate - Frontend',
  
  // 🇻🇳 Loại monitor
  type: 'metric alert',
  
  // 🇻🇳 Query: Đếm số errors trong 5 phút
  query: 'sum(last_5m):sum:frontend.errors{env:production} > 50',
  
  // 🇻🇳 Message khi alert trigger
  message: `
    🚨 **High Error Rate Detected!**
    
    Error count: {{value}} errors in last 5 minutes
    Threshold: 50 errors
    
    **Quick Actions:**
    - Check Sentry: https://sentry.io/your-project
    - Check Recent Deploys: {{#is_alert}}@slack-deploys{{/is_alert}}
    
    **On-call:** @pagerduty-frontend
  `,
  
  // 🇻🇳 Tags để phân loại
  tags: ['env:production', 'team:frontend', 'severity:high'],
  
  // 🇻🇳 Priority
  priority: 1, // 1 = P1 (highest), 5 = P5 (lowest)
  
  // 🇻🇳 Notification channels
  notify: [
    '@slack-alerts',
    '@pagerduty-frontend',
    'email@example.com',
  ],
};

// 🇻🇳 POST lên DataDog API
fetch('https://api.datadoghq.com/api/v1/monitor', {
  method: 'POST',
  headers: {
    'DD-API-KEY': process.env.DD_API_KEY,
    'DD-APPLICATION-KEY': process.env.DD_APP_KEY,
  },
  body: JSON.stringify(monitorConfig),
});
```

### **8.3. Grafana Dashboard**

```javascript
// ===================================================
// 📈 **GRAFANA DASHBOARD JSON CONFIG**
// ===================================================

// 🇻🇳 Ví dụ: Dashboard theo dõi Core Web Vitals

{
  "dashboard": {
    "title": "Frontend Performance - Core Web Vitals",
    "tags": ["frontend", "performance", "web-vitals"],
    "timezone": "browser",
    "panels": [
      // 📊 Panel 1: LCP Over Time
      {
        "title": "LCP (Largest Contentful Paint) - P75",
        "type": "graph",
        "datasource": "DataDog",
        "targets": [
          {
            "query": "avg:rum.performance.lcp{env:production} by {page}",
            "alias": "{{page}}"
          }
        ],
        "yaxis": {
          "label": "Time (ms)",
          "format": "ms"
        },
        "alert": {
          "conditions": [
            {
              "query": "avg() OF query(A, 5m, now) IS ABOVE 2500" // Alert if LCP > 2.5s
            }
          ],
          "notifications": [
            { "uid": "slack-alerts" }
          ]
        }
      },
      
      // 📊 Panel 2: INP Over Time
      {
        "title": "INP (Interaction to Next Paint) - P75",
        "type": "graph",
        "datasource": "DataDog",
        "targets": [
          {
            "query": "percentile:rum.performance.inp{env:production}.75 by {page}"
          }
        ],
        "yaxis": {
          "label": "Time (ms)",
          "format": "ms"
        }
      },
      
      // 📊 Panel 3: Error Rate
      {
        "title": "JavaScript Error Rate",
        "type": "graph",
        "datasource": "Sentry",
        "targets": [
          {
            "query": "sum(rate(errors{project:frontend}[5m]))"
          }
        ]
      },
      
      // 📊 Panel 4: Page Load Distribution
      {
        "title": "Page Load Time Distribution (Histogram)",
        "type": "histogram",
        "datasource": "DataDog",
        "targets": [
          {
            "query": "histogram:rum.performance.navigation.load_time{env:production}"
          }
        ]
      }
    ]
  }
}
```

---

## 🎯 **TỔNG KẾT**

### **Checklist APM cho Production:**

```
✅ MONITORING ESSENTIALS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Track Core Web Vitals (LCP, INP, CLS)
✅ Error tracking với Sentry/DataDog
✅ Session Replay cho critical errors
✅ Performance Budgets trong CI/CD
✅ Source Maps upload tự động
✅ Custom metrics cho business-critical flows
✅ Alerts cho error spikes/performance degradation
✅ Dashboard hiển thị metrics real-time

✅ BEST PRACTICES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Sample rate hợp lý (20-50% production traffic)
✅ Privacy: Mask sensitive data
✅ Cost optimization: Chỉ replay sessions có errors
✅ Alert fatigue: Chỉ alert cho issues QUAN TRỌNG
✅ Actionable metrics: Metrics phải dẫn đến action cụ thể
```

**📚 Tài Liệu Tham Khảo:**
- [Web Vitals Library](https://github.com/GoogleChrome/web-vitals)
- [Sentry Performance Monitoring](https://docs.sentry.io/product/performance/)
- [DataDog RUM](https://docs.datadoghq.com/real_user_monitoring/)
- [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci)

---

**✍️ Viết bởi:** GitHub Copilot  
**🗓️ Ngày cập nhật:** 2024
