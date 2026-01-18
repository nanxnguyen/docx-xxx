# 🚀 Q68: Progressive Web Apps (PWA) - Service Workers, Offline-first & App Shell

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"PWA = Web App + Native App Features"**
// 💡 PWA: Progressive Web App (Progressive Web App)
// 💡 Web App: Ứng dụng web (Web application)
// 💡 Native App Features: Tính năng app native (Native app features)
// 💡 Kết hợp ưu điểm của cả hai (Combine advantages of both)

**3 Core Pillars:** (3 Trụ Cột Chính)
// 💡 Core Pillars: Trụ cột chính (Core pillars)
// 💡 3 yêu cầu bắt buộc cho PWA (3 required features for PWA)

1. **HTTPS + Secure** - All communication encrypted
   // 💡 HTTPS: HyperText Transfer Protocol Secure (HyperText Transfer Protocol Secure)
   // 💡 Secure: Bảo mật (Secure)
   // 💡 All communication encrypted: Tất cả giao tiếp được mã hóa (All communication encrypted)
   // 💡 Bắt buộc cho PWA (Required for PWA)

2. **Service Worker** - Offline capability, push notifications
   // 💡 Service Worker: Background script (Background script)
   // 💡 Offline capability: Khả năng offline (Offline capability)
   // 💡 push notifications: Thông báo đẩy (Push notifications)
   // 💡 Cho phép app hoạt động offline (Allow app to work offline)

3. **Web App Manifest** - Install on home screen, metadata
   // 💡 Web App Manifest: File JSON mô tả app (JSON file describing app)
   // 💡 Install on home screen: Cài đặt trên màn hình chính (Install on home screen)
   // 💡 metadata: Siêu dữ liệu (Metadata)
   // 💡 Cho phép app cài đặt như native app (Allow app to install like native app)

**Tôi đã implement PWA cho e-commerce app:**
// 💡 implement: Triển khai (Implement)
// 💡 e-commerce app: Ứng dụng thương mại điện tử (E-commerce application)

- **Service Worker** với cache strategies (Network First cho API, Cache First cho assets)
  // 💡 Service Worker: Background worker (Background worker)
  // 💡 cache strategies: Chiến lược cache (Caching strategies)
  // 💡 Network First cho API: Network trước cho API (Network first for API)
  // 💡 Cache First cho assets: Cache trước cho assets (Cache first for assets)

- **Offline mode** - User có thể browse products, checkout flow lưu vào IndexedDB (sync khi online)
  // 💡 Offline mode: Chế độ offline (Offline mode)
  // 💡 browse products: Duyệt sản phẩm (Browse products)
  // 💡 checkout flow: Quy trình thanh toán (Checkout flow)
  // 💡 lưu vào IndexedDB: Lưu vào IndexedDB (Save to IndexedDB)
  // 💡 sync khi online: Đồng bộ khi online (Sync when online)

- **Push notifications** - Real-time order updates
  // 💡 Push notifications: Thông báo đẩy (Push notifications)
  // 💡 Real-time order updates: Cập nhật đơn hàng real-time (Real-time order updates)

- **App Shell Architecture** - Instant loading (< 1s), render API data after
  // 💡 App Shell Architecture: Kiến trúc App Shell (App Shell Architecture)
  // 💡 Instant loading: Tải tức thì (Instant loading)
  // 💡 < 1s: Dưới 1 giây (Less than 1 second)
  // 💡 render API data after: Render dữ liệu API sau (Render API data after)

- **Result**: (Kết quả)
  // 💡 Result: Kết quả đạt được (Results achieved)
  - ✅ 45% increase in mobile engagement
    // 💡 45% increase: Tăng 45% (45% increase)
    // 💡 mobile engagement: Tương tác mobile (Mobile engagement)
  - ✅ 70% offline retention (users stay on app without network)
    // 💡 70% offline retention: 70% giữ lại khi offline (70% offline retention)
    // 💡 users stay on app without network: User ở lại app không cần mạng (Users stay on app without network)
  - ✅ Can install on home screen (looks like native app)
    // 💡 Can install: Có thể cài đặt (Can install)
    // 💡 home screen: Màn hình chính (Home screen)
    // 💡 looks like native app: Trông như app native (Looks like native app)
  - ✅ Works on iOS, Android, Web
    // 💡 Works on: Hoạt động trên (Works on)
    // 💡 iOS, Android, Web: Tất cả platforms (All platforms)

**Key strategies:** (Chiến Lược Chính)
// 💡 Key strategies: Các chiến lược quan trọng (Important strategies)
// 💡 Cache strategies cho PWA (Cache strategies for PWA)

- **Network First** - API calls (try online, fallback to cache)
  // 💡 Network First: Network trước (Network first)
  // 💡 API calls: Gọi API (API calls)
  // 💡 try online: Thử online trước (Try online first)
  // 💡 fallback to cache: Quay về cache nếu fail (Fallback to cache if fail)
  // 💡 Đảm bảo data mới nhất (Ensure latest data)

- **Cache First** - JS/CSS/Images (use cache, update in background)
  // 💡 Cache First: Cache trước (Cache first)
  // 💡 JS/CSS/Images: JavaScript, CSS, Images (JavaScript, CSS, Images)
  // 💡 use cache: Dùng cache (Use cache)
  // 💡 update in background: Cập nhật nền (Update in background)
  // 💡 Tối ưu tốc độ load (Optimize load speed)

- **Stale While Revalidate** - User gets cached version fast, update in background
  // 💡 Stale While Revalidate: Dùng cache cũ, cập nhật nền (Use stale cache, update in background)
  // 💡 User gets cached version fast: User nhận version cache nhanh (User gets cached version fast)
  // 💡 update in background: Cập nhật nền (Update in background)
  // 💡 Best of both: Nhanh + data mới (Best of both: Fast + new data)

- **IndexedDB** - Store orders/cart for sync when online
  // 💡 IndexedDB: Database trong browser (Database in browser)
  // 💡 Store orders/cart: Lưu đơn hàng/giỏ hàng (Store orders/cart)
  // 💡 sync when online: Đồng bộ khi online (Sync when online)
  // 💡 Offline-first approach (Offline-first approach)

- **Background Sync** - Auto-sync pending actions when reconnected
  // 💡 Background Sync: Đồng bộ nền (Background sync)
  // 💡 Auto-sync: Tự động đồng bộ (Auto sync)
  // 💡 pending actions: Các hành động đang chờ (Pending actions)
  // 💡 when reconnected: Khi kết nối lại (When reconnected)
  // 💡 Tự động sync khi có mạng (Auto sync when network available)

- **Web Push API** - Real-time notifications (orders, discounts, new messages)
  // 💡 Web Push API: API thông báo đẩy (Push notification API)
  // 💡 Real-time notifications: Thông báo real-time (Real-time notifications)
  // 💡 orders, discounts, new messages: Đơn hàng, giảm giá, tin nhắn mới (Orders, discounts, new messages)
  // 💡 Tăng engagement (Increase engagement)

**Performance impact:** (Ảnh Hưởng Hiệu Suất)
// 💡 Performance impact: Tác động đến hiệu suất (Performance impact)
// 💡 Kết quả đo lường (Measurement results)

- Load time: 3s (online) → 300ms (offline cached)
  // 💡 Load time: Thời gian tải (Load time)
  // 💡 3s (online): 3 giây khi online (3 seconds when online)
  // 💡 300ms (offline cached): 300ms khi offline có cache (300ms when offline with cache)
  // 💡 Giảm 90% thời gian load (Reduce 90% load time)

- Lighthouse PWA score: 90+
  // 💡 Lighthouse PWA score: Điểm PWA từ Lighthouse (Lighthouse PWA score)
  // 💡 90+: Trên 90 điểm (Above 90 points)
  // 💡 Excellent score (Excellent score)

- Network request count: -60% (cache hits)
  // 💡 Network request count: Số lượng request mạng (Network request count)
  // 💡 -60%: Giảm 60% (Reduce 60%)
  // 💡 cache hits: Cache trúng (Cache hits)
  // 💡 Giảm bandwidth (Reduce bandwidth)

---

## **📋 GIẢI THÍCH CHI TIẾT CẤP SENIOR/STAFF**

### **1️⃣ What is PWA? (PWA Là Gì?)**

**🎯 Mục đích**: Hiểu rõ PWA là gì và tại sao nó quan trọng
// 💡 PWA: Progressive Web App - Kết hợp ưu điểm của Web và Native App
// 💡 Progressive: Hoạt động cho mọi người, tính năng nâng cao cho browser có khả năng
// 💡 Web: Xây dựng bằng web tech (HTML, CSS, JS)
// 💡 App: Cài đặt trên home screen, hoạt động offline, push notifications

```
// ============================================
// 📱 PWA ĐỊNH NGHĨA
// ============================================
PWA = Progressive Web App
├─ Progressive: Works for everyone, enhanced features for capable browsers
│  💡 Progressive: Hoạt động cho mọi người
│  💡 Enhanced features: Tính năng nâng cao cho browser có khả năng
│  💡 Graceful degradation: Từ từ nâng cấp tính năng
│
├─ Web: Built with web tech (HTML, CSS, JS, not native code)
│  💡 Web: Xây dựng bằng web tech
│  💡 HTML, CSS, JS: Không cần native code
│  💡 Cross-platform: Chạy trên mọi platform
│
└─ App: Install on home screen, work offline, push notifications
   💡 App: Cài đặt trên home screen
   💡 Work offline: Hoạt động offline
   💡 Push notifications: Thông báo đẩy
   💡 Giống native app nhưng là web app

// ============================================
// 📊 SO SÁNH PWA vs WEB vs NATIVE APP
// ============================================
PWA vs Web vs Native App:

┌────────────────────────────────────────────────────────────┐
│         PWA            Web App         Native App          │
├────────────────────────────────────────────────────────────┤
│ Install:  Yes (home)   No              Yes (app store)     │
│           💡 Cài trên home screen      💡 Không cài được    💡 Cài từ app store
│           💡 Giống native app          💡 Chỉ mở browser   💡 Phải qua review
│
│ Offline:  Yes          No              Yes                 │
│           💡 Service Worker cache      💡 Không hoạt động  💡 Native offline
│           💡 IndexedDB storage        💡 Cần mạng          💡 Local storage
│
│ Sync:    Background   No              Yes                 │
│           💡 Background Sync API        💡 Không có         💡 Native sync
│           💡 Tự động sync khi online  💡 Manual sync      💡 Auto sync
│
│ Notify:   Push         No              Yes                 │
│           💡 Web Push API              💡 Không có         💡 Native push
│           💡 Real-time notifications   💡 Không có         💡 System notifications
│
│ Dev:      Quick        Quick           Slow (iOS/Android) │
│           💡 Web tech, nhanh           💡 Web tech, nhanh  💡 Native code, chậm
│           💡 Deploy ngay               💡 Deploy ngay      💡 Phải build riêng
│
│ Update:   Instant      Instant         App store (slow)    │
│           💡 Update ngay lập tức       💡 Update ngay      💡 Phải qua review
│           💡 Không cần app store       💡 Không cần        💡 Phải đợi approval
│
│ Size:     ~ 1MB        N/A             50-200MB            │
│           💡 Nhỏ, nhanh                💡 Không cài        💡 Lớn, tốn storage
└────────────────────────────────────────────────────────────┘

// ============================================
// 🏆 KẾT LUẬN
// ============================================
PWA = "Best of both worlds"
💡 Best of both: Tốt nhất của cả hai thế giới
💡 Web: Dễ phát triển, deploy nhanh
💡 Native: Cài đặt, offline, notifications
💡 PWA: Kết hợp cả hai → Perfect solution
```

#### **1.1 PWA Requirements Checklist**

```typescript
// PWA Checklist (Lighthouse audit) (Danh sách kiểm tra PWA)
// 💡 PWA Checklist: Các yêu cầu để app được coi là PWA (Requirements for app to be considered PWA)
// 💡 Lighthouse: Tool tự động audit PWA (Tool to automatically audit PWA)
const pwaChecklist = {
  '1. HTTPS': {
    // 💡 HTTPS: Bắt buộc cho PWA (Required for PWA)
    description: 'All content over HTTPS',
    // 💡 Tất cả content phải qua HTTPS (All content must be over HTTPS)
    // 💡 Security: Bảo vệ data khỏi man-in-the-middle attacks (Security: Protect data from MITM attacks)
    check: () => location.protocol === 'https:',
    // 💡 check: Function kiểm tra điều kiện (Function to check condition)
    // 💡 location.protocol: Protocol của URL (URL protocol)
    // 💡 "https:": Phải là HTTPS (Must be HTTPS)
    // 💡 "http:": Không phải HTTPS → không đạt (Not HTTPS → fail)
  },
  '2. Web App Manifest': {
    // 💡 Web App Manifest: File JSON mô tả app (JSON file describing app)
    description: 'manifest.json with name, icon, colors',
    // 💡 manifest.json: File chứa metadata (File containing metadata)
    // 💡 name, icon, colors: Thông tin cần thiết (Required information)
    check: () => document.querySelector('link[rel="manifest"]'),
    // 💡 check: Kiểm tra có link manifest không (Check if manifest link exists)
    // 💡 document.querySelector: Tìm element (Find element)
    // 💡 'link[rel="manifest"]': Link tag với rel="manifest" (Link tag with rel="manifest")
    // 💡 <link rel="manifest" href="/manifest.json"> (Link tag)
  },
  '3. Service Worker': {
    // 💡 Service Worker: Background script cho offline (Background script for offline)
    description: 'SW registered and responds to fetch events',
    // 💡 SW registered: Service Worker đã được đăng ký (Service Worker is registered)
    // 💡 Responds to fetch events: Xử lý fetch requests (Handle fetch requests)
    check: () => navigator.serviceWorker?.controller,
    // 💡 check: Kiểm tra có Service Worker controller không (Check if Service Worker controller exists)
    // 💡 navigator.serviceWorker: Service Worker API (Service Worker API)
    // 💡 ?.controller: Optional chaining, controller nếu có (Optional chaining, controller if exists)
    // 💡 controller: Active Service Worker (Active Service Worker)
  },
  '4. Responsive Design': {
    // 💡 Responsive Design: Layout thích ứng với màn hình (Layout adapts to screen)
    description: 'Mobile-friendly (viewport meta tag)',
    // 💡 Mobile-friendly: Thân thiện với mobile (Mobile-friendly)
    // 💡 viewport meta tag: Tag để config viewport (Tag to config viewport)
    check: () => document.querySelector('meta[name="viewport"]'),
    // 💡 check: Kiểm tra có viewport meta tag không (Check if viewport meta tag exists)
    // 💡 <meta name="viewport" content="width=device-width, initial-scale=1"> (Viewport meta tag)
  },
  '5. Fast on 3G': {
    // 💡 Fast on 3G: Nhanh trên mạng 3G (Fast on 3G network)
    description: '< 3 seconds on slow 3G network',
    // 💡 < 3 seconds: Load trong vòng 3 giây (Load within 3 seconds)
    // 💡 slow 3G: Mạng 3G chậm (Slow 3G network)
    check: () => false,
    // ⚠️ Lighthouse measures this (Lighthouse đo lường điều này)
    // 💡 false: Không thể check bằng code (Cannot check with code)
    // 💡 Lighthouse tự động test trên slow 3G (Lighthouse automatically tests on slow 3G)
  },
  '6. Installable': {
    // 💡 Installable: Có thể cài đặt (Can be installed)
    description: 'No errors, manifest + SW + HTTPS + icons',
    // 💡 No errors: Không có lỗi (No errors)
    // 💡 manifest + SW + HTTPS + icons: Tất cả yêu cầu (All requirements)
    check: () => false,
    // ⚠️ Lighthouse measures this (Lighthouse đo lường điều này)
    // 💡 false: Không thể check bằng code (Cannot check with code)
    // 💡 Lighthouse kiểm tra tất cả yêu cầu (Lighthouse checks all requirements)
  },
};
```

---

### **2️⃣ Service Workers Fundamentals (Kiến Thức Cơ Bản Service Workers)**

**🎯 Mục đích**: Hiểu rõ Service Worker và lifecycle của nó
// 💡 Service Worker: Background script cho offline capability
// 💡 Lifecycle: Vòng đời của Service Worker từ install đến activate
// 💡 Quan trọng: Hiểu lifecycle để implement đúng

#### **2.1 Service Worker Lifecycle (Vòng Đời Service Worker)**

```
// ============================================
// 🔄 SERVICE WORKER LIFECYCLE STATES
// ============================================
┌──────────────────────────────────────────────────────────────┐
│          SERVICE WORKER LIFECYCLE STATES                     │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  1️⃣  PARSING (Phân Tích)                                   │
│      └─ Browser parses SW JavaScript file                   │
│         💡 Browser đọc và parse file SW JavaScript
│         💡 Kiểm tra syntax, errors
│         ✅ Success → Continue                               │
│         💡 Parse thành công → tiếp tục
│         ❌ Error → Stop, retry on next page visit            │
│         💡 Parse lỗi → dừng, thử lại lần sau
│                                                              │
│  2️⃣  INSTALLING (Đang Cài Đặt)                             │
│      └─ 'install' event fires                               │
│         💡 Event 'install' được trigger
│         💡 Đây là nơi cache resources
│      └─ Cache resources for offline                         │
│         💡 Cache các resources cho offline
│         💡 HTML, CSS, JS, images, etc.
│      └─ Wait for all promises to resolve                    │
│         💡 Đợi tất cả promises resolve
│         💡 event.waitUntil() đảm bảo điều này
│         ✅ Success → INSTALLED                              │
│         💡 Thành công → chuyển sang INSTALLED
│         ❌ Error → SW discarded, old SW still controls      │
│         💡 Lỗi → SW bị loại bỏ, SW cũ vẫn control
│                                                              │
│  3️⃣  INSTALLED (Waiting) - Đã Cài Đặt (Đang Chờ)           │
│      └─ SW ready but not controlling pages yet             │
│         💡 SW đã sẵn sàng nhưng chưa control pages
│         💡 Old SW vẫn đang control pages hiện tại
│      └─ Old SW still controls current page                  │
│         💡 SW cũ vẫn control page hiện tại
│         💡 Đảm bảo không bị gián đoạn
│      └─ skipWaiting() → Move to ACTIVATING                 │
│         💡 skipWaiting(): Bỏ qua waiting, activate ngay
│         💡 Dùng khi muốn update ngay lập tức
│         ← User closes all tabs → Activate                   │
│         💡 User đóng tất cả tabs → activate tự động
│                                                              │
│  4️⃣  ACTIVATING (Đang Kích Hoạt)                            │
│      └─ 'activate' event fires                              │
│         💡 Event 'activate' được trigger
│         💡 Đây là nơi cleanup old caches
│      └─ Delete old cache versions                           │
│         💡 Xóa các cache versions cũ
│         💡 Giải phóng storage
│      └─ Cleanup resources                                   │
│         💡 Dọn dẹp resources không cần thiết
│         ✅ Success → ACTIVATED                              │
│         💡 Thành công → chuyển sang ACTIVATED
│                                                              │
│  5️⃣  ACTIVATED (Controlling) - Đã Kích Hoạt (Đang Control) │
│      └─ Now controls all pages                              │
│         💡 Bây giờ control tất cả pages
│         💡 Có thể intercept network requests
│      └─ 'fetch', 'message', 'sync' events available        │
│         💡 Các events có sẵn: fetch, message, sync
│         💡 fetch: Intercept network requests
│         💡 message: Nhận messages từ main thread
│         💡 sync: Background sync
│      └─ Can intercept network requests                      │
│         💡 Có thể chặn và xử lý network requests
│         💡 Đây là tính năng chính của SW
│                                                              │
│  6️⃣  REDUNDANT (Dư Thừa)                                    │
│      └─ SW replaced by newer version                        │
│         💡 SW bị thay thế bởi version mới
│         💡 Không còn được sử dụng
│      └─ Removed from memory                                 │
│         💡 Bị xóa khỏi memory
│         💡 Không còn hoạt động
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

#### **2.2 Service Worker Registration**

```typescript
// sw-register.ts - Main thread (not in SW)

// ✅ Register service worker
if ('serviceWorker' in navigator) {
  navigator.serviceWorker
    .register('/sw.js', {
      scope: '/', // Control all pages under /
    })
    .then((registration) => {
      console.log('SW registered:', registration.scope);

      // Check for updates periodically
      setInterval(() => {
        registration.update(); // Check for new SW
      }, 60000); // Every 1 minute

      // Listen for new SW waiting
      registration.addEventListener('updatefound', () => {
        const newWorker = registration.installing;
        newWorker?.addEventListener('statechange', () => {
          if (
            newWorker.state === 'installed' &&
            navigator.serviceWorker.controller
          ) {
            // New SW waiting, prompt user to reload
            showUpdatePrompt('New version available!');
          }
        });
      });
    })
    .catch((error) => {
      console.error('SW registration failed:', error);
    });
}

// Handle messages from SW
navigator.serviceWorker?.addEventListener('message', (event) => {
  const { type, data } = event.data;

  if (type === 'CACHE_UPDATED') {
    console.log('Cache updated:', data.files);
  }

  if (type === 'SYNC_COMPLETED') {
    console.log('Offline actions synced:', data.actions);
  }
});
```

#### **2.3 Basic Service Worker**

```typescript
// sw.ts - Service Worker thread

const CACHE_VERSION = 'v1';
const CACHE_NAME = `app-cache-${CACHE_VERSION}`;

// Install: Cache resources
self.addEventListener('install', (event: ExtendableEvent) => {
  console.log('SW installing...');

  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      // Cache critical resources
      return cache.addAll([
        '/',
        '/index.html',
        '/css/styles.css',
        '/js/app.js',
        '/js/vendor.js',
        '/images/logo.png',
        '/offline.html',
      ]);
    })
  );

  // Skip waiting: Activate immediately (don't wait for tab close)
  // self.skipWaiting();
});

// Activate: Clean old caches
self.addEventListener('activate', (event: ExtendableEvent) => {
  console.log('SW activating...');

  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            console.log('Deleting old cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );

  // Claim all clients immediately
  self.clients.claim();
});

// Fetch: Intercept network requests
self.addEventListener('fetch', (event: FetchEvent) => {
  const { request } = event;

  // Skip non-GET requests
  if (request.method !== 'GET') {
    return;
  }

  // Different strategies for different resource types
  if (isApiRequest(request)) {
    event.respondWith(networkFirstStrategy(request));
  } else if (isAssetRequest(request)) {
    event.respondWith(cacheFirstStrategy(request));
  } else {
    event.respondWith(staleWhileRevalidateStrategy(request));
  }
});

function isApiRequest(request: Request): boolean {
  return request.url.includes('/api/');
}

function isAssetRequest(request: Request): boolean {
  return /\.(js|css|jpg|png|svg|woff2)$/.test(request.url);
}
```

---

### **3️⃣ Cache Strategies (Chiến Lược Cache)**

**🎯 Mục đích**: Hiểu các chiến lược cache và khi nào dùng cái nào
// 💡 Cache strategies: Các cách cache khác nhau cho các loại resources khác nhau
// 💡 Network First: Thử network trước, fallback cache
// 💡 Cache First: Dùng cache trước, update nền
// 💡 Stale While Revalidate: Dùng cache cũ, update nền

#### **3.1 Network First (API Calls) - Network Trước (Cho API)**

```typescript
// ============================================
// 🌐 NETWORK FIRST STRATEGY
// ============================================
// Try network, fallback to cache
// Good for: API calls, fresh data important
// 💡 Network First: Thử network trước, nếu fail thì dùng cache
// 💡 Tốt cho: API calls, data cần mới nhất
// 💡 Ưu tiên: Fresh data > Speed

async function networkFirstStrategy(request: Request): Promise<Response> {
  // 💡 networkFirstStrategy: Chiến lược network trước
  // 💡 request: Request object từ fetch event
  // 💡 Return: Response object

  const cacheName = 'api-cache-v1';
  // 💡 cacheName: Tên cache store
  // 💡 'api-cache-v1': Version 1 của API cache

  try {
    // Try network first
    const networkResponse = await fetch(request.clone());
    // 💡 fetch(request.clone()): Thử fetch từ network
    // 💡 clone(): Clone request để có thể dùng lại
    // 💡 Nếu network thành công → dùng response này

    // Cache successful response
    if (networkResponse.ok) {
      // 💡 networkResponse.ok: Response thành công (status 200-299)
      const cache = await caches.open(cacheName);
      // 💡 caches.open(): Mở cache store
      cache.put(request.url, networkResponse.clone());
      // 💡 cache.put(): Lưu response vào cache
      // 💡 clone(): Clone response để cache (response chỉ đọc được 1 lần)
      // 💡 Lưu để dùng khi offline
    }

    return networkResponse;
    // 💡 Return network response → user nhận data mới nhất
  } catch (error) {
    // Network failed, try cache
    // 💡 Network fail → thử dùng cache
    const cachedResponse = await caches.match(request);
    // 💡 caches.match(): Tìm response trong cache
    // 💡 Nếu có cache → dùng cache

    if (cachedResponse) {
      console.log('Using cached response:', request.url);
      // 💡 Log để debug
      return cachedResponse;
      // 💡 Return cached response → user vẫn có data (có thể cũ)
    }

    // No cache, return offline page
    return caches.match('/offline.html') || new Response('Offline');
    // 💡 Không có cache → return offline page
    // 💡 Hoặc return response "Offline" nếu không có offline page
    // 💡 User biết là đang offline
  }
}

// Real example: Stock prices API
// ✅ Try to get fresh prices from network
// ✅ If offline, show last cached prices
// ✅ Update cache as prices come in
```

#### **3.2 Cache First (Static Assets) - Cache Trước (Cho Assets Tĩnh)**

```typescript
// ============================================
// 💾 CACHE FIRST STRATEGY
// ============================================
// Check cache first, update from network in background
// Good for: CSS, JS, images (don't change often)
// 💡 Cache First: Dùng cache trước, update nền
// 💡 Tốt cho: CSS, JS, images (ít thay đổi)
// 💡 Ưu tiên: Speed > Fresh data

async function cacheFirstStrategy(request: Request): Promise<Response> {
  // 💡 cacheFirstStrategy: Chiến lược cache trước
  // 💡 request: Request object từ fetch event
  // 💡 Return: Response object

  const cacheName = 'asset-cache-v1';
  // 💡 cacheName: Tên cache store cho assets
  // 💡 'asset-cache-v1': Version 1 của asset cache

  // Check cache first
  const cachedResponse = await caches.match(request);
  // 💡 caches.match(): Tìm response trong cache
  // 💡 Nếu có cache → dùng ngay (nhanh ✅)

  if (cachedResponse) {
    // Found in cache, return immediately (fast ✅)
    // But update in background
    // 💡 Tìm thấy trong cache → return ngay (nhanh)
    // 💡 Nhưng update cache nền để có version mới
    updateCacheInBackground(request, cacheName);
    // 💡 updateCacheInBackground: Update cache trong background
    // 💡 Không block response → user nhận ngay
    return cachedResponse;
    // 💡 Return cached response → user nhận ngay lập tức
  }

  // Not in cache, fetch from network
  // 💡 Không có cache → fetch từ network
  try {
    const networkResponse = await fetch(request.clone());
    // 💡 fetch(request.clone()): Fetch từ network
    // 💡 Clone request để có thể dùng lại

    if (networkResponse.ok) {
      // 💡 networkResponse.ok: Response thành công
      const cache = await caches.open(cacheName);
      // 💡 caches.open(): Mở cache store
      cache.put(request.url, networkResponse.clone());
      // 💡 cache.put(): Lưu response vào cache
      // 💡 Lần sau sẽ dùng cache này
    }

    return networkResponse;
    // 💡 Return network response → user nhận asset mới
  } catch (error) {
    // Network failed, no cache fallback
    // 💡 Network fail, không có cache → throw error
    throw error;
    // 💡 User sẽ thấy error (không có fallback)
  }
}

async function updateCacheInBackground(
  request: Request,
  cacheName: string
): Promise<void> {
  try {
    const networkResponse = await fetch(request.clone());
    if (networkResponse.ok) {
      const cache = await caches.open(cacheName);
      cache.put(request.url, networkResponse);
    }
  } catch (error) {
    // Failed to update, that's okay (cache is fresh enough)
  }
}
```

#### **3.3 Stale While Revalidate (Optimal Performance) - Dùng Cache Cũ, Cập Nhật Nền**

```typescript
// ============================================
// ⚡ STALE WHILE REVALIDATE STRATEGY
// ============================================
// Return cached version immediately, update in background
// Good for: Content that can be slightly stale (blog posts, etc)
// 💡 Stale While Revalidate: Dùng cache cũ ngay, update nền
// 💡 Tốt cho: Content có thể hơi cũ (blog posts, articles)
// 💡 Best of both: Nhanh + data mới

async function staleWhileRevalidateStrategy(
  request: Request
): Promise<Response> {
  // 💡 staleWhileRevalidateStrategy: Chiến lược stale while revalidate
  // 💡 request: Request object từ fetch event
  // 💡 Return: Response object (cached hoặc network)

  const cacheName = 'swr-cache-v1';
  // 💡 cacheName: Tên cache store
  // 💡 'swr-cache-v1': Version 1 của SWR cache

  // Return cached version immediately (if available)
  // 💡 Return cached version ngay lập tức (nếu có)
  const cachedResponse = await caches.match(request);
  // 💡 caches.match(): Tìm response trong cache
  // 💡 Nếu có cache → return ngay (nhanh ✅)

  // Update cache in background (fire and forget)
  // 💡 Update cache trong background (fire and forget)
  // 💡 Không đợi update → return cached response ngay
  const updatePromise = fetch(request.clone())
    // 💡 fetch(request.clone()): Fetch từ network
    // 💡 Clone request để có thể dùng lại
    .then((networkResponse) => {
      // 💡 networkResponse: Response từ network
      if (networkResponse.ok) {
        // 💡 networkResponse.ok: Response thành công
        const cache = caches.open(cacheName);
        // 💡 caches.open(): Mở cache store
        cache.then((c) => c.put(request.url, networkResponse.clone()));
        // 💡 cache.put(): Lưu response mới vào cache
        // 💡 Lần sau sẽ dùng version mới này
      }
      return networkResponse;
      // 💡 Return network response (không dùng, chỉ để cache)
    })
    .catch((error) => {
      // 💡 Network fail → không sao, vẫn có cached response
      console.error('Background update failed:', error);
      // 💡 Log error để debug
    });

  // Return cached version immediately, or wait for network if no cache
  // 💡 Return cached version ngay, hoặc đợi network nếu không có cache
  return cachedResponse || updatePromise;
  // 💡 cachedResponse: Có cache → return ngay (nhanh)
  // 💡 updatePromise: Không có cache → đợi network
  // 💡 Best of both worlds: Nhanh + data mới
}

// Timeline:
// User navigates to /articles/123
// 1️⃣ SW serves cached version (if exists) → Page loads instantly
// 2️⃣ Meanwhile, fetch fresh version in background
// 3️⃣ When fresh version arrives, cache it for next visit
// 4️⃣ User can see update notification
```

#### **3.4 Complete Cache Strategy Implementation**

```typescript
// sw-advanced.ts

const STRATEGIES = {
  NETWORK_FIRST: 'network-first',
  CACHE_FIRST: 'cache-first',
  SWR: 'swr', // Stale While Revalidate
  NETWORK_ONLY: 'network-only',
  CACHE_ONLY: 'cache-only',
};

// Route-specific strategy mapping
const routeStrategies = [
  { pattern: /^https:\/\/api\./, strategy: STRATEGIES.NETWORK_FIRST },
  { pattern: /\.(js|css)$/, strategy: STRATEGIES.CACHE_FIRST },
  { pattern: /\.(jpg|png|svg)$/, strategy: STRATEGIES.CACHE_FIRST },
  { pattern: /^https:\/\/.*/, strategy: STRATEGIES.SWR }, // Fallback
];

self.addEventListener('fetch', (event: FetchEvent) => {
  const { request } = event;

  // Find matching strategy
  const strategy =
    routeStrategies.find((route) => route.pattern.test(request.url))
      ?.strategy || STRATEGIES.SWR;

  switch (strategy) {
    case STRATEGIES.NETWORK_FIRST:
      event.respondWith(networkFirstStrategy(request));
      break;
    case STRATEGIES.CACHE_FIRST:
      event.respondWith(cacheFirstStrategy(request));
      break;
    case STRATEGIES.SWR:
      event.respondWith(staleWhileRevalidateStrategy(request));
      break;
    default:
      event.respondWith(fetch(request));
  }
});
```

---

### **4️⃣ Offline-First Architecture (Kiến Trúc Offline-First)**

**🎯 Mục đích**: Xây dựng app hoạt động offline-first
// 💡 Offline-First: App hoạt động offline trước, sync khi online
// 💡 IndexedDB: Database trong browser để lưu data offline
// 💡 Background Sync: Tự động sync khi có mạng

#### **4.1 IndexedDB for Offline Storage (IndexedDB Cho Lưu Trữ Offline)**

```typescript
// ============================================
// 💾 INDEXEDDB FOR OFFLINE STORAGE
// ============================================
// db.ts - IndexedDB for offline data
// 💡 IndexedDB: Database trong browser
// 💡 Tốt hơn localStorage: Lưu được objects, arrays, large data
// 💡 Async API: Không block main thread

class OfflineDB {
  // 💡 OfflineDB: Class để quản lý IndexedDB
  // 💡 Encapsulate IndexedDB operations

  private db: IDBDatabase | null = null;
  // 💡 db: Reference đến IndexedDB database
  // 💡 null: Chưa được khởi tạo

  async init() {
    // 💡 init: Khởi tạo database
    // 💡 Return: Promise<void>
    return new Promise<void>((resolve, reject) => {
      // 💡 Promise: Wrapper cho IndexedDB async operations
      const request = indexedDB.open('ecommerce-db', 1);
      // 💡 indexedDB.open(): Mở database
      // 💡 'ecommerce-db': Tên database
      // 💡 1: Version (tăng khi cần thay đổi schema)

      request.onerror = () => reject(request.error);

      request.onupgradeneeded = (event) => {
        const db = (event.target as IDBOpenDBRequest).result;

        // Create object stores
        if (!db.objectStoreNames.contains('products')) {
          const store = db.createObjectStore('products', { keyPath: 'id' });
          store.createIndex('category', 'category');
        }

        if (!db.objectStoreNames.contains('cart')) {
          db.createObjectStore('cart', { keyPath: 'id' });
        }

        if (!db.objectStoreNames.contains('orders')) {
          const orders = db.createObjectStore('orders', { keyPath: 'id' });
          orders.createIndex('status', 'status');
        }

        if (!db.objectStoreNames.contains('pendingActions')) {
          db.createObjectStore('pendingActions', { keyPath: 'id' });
        }
      };

      request.onsuccess = () => {
        this.db = request.result;
        resolve();
      };
    });
  }

  // Save products for offline browsing
  async saveProducts(products: any[]): Promise<void> {
    return new Promise((resolve, reject) => {
      const transaction = this.db!.transaction(['products'], 'readwrite');
      const store = transaction.objectStore('products');

      products.forEach((product) => {
        store.put(product);
      });

      transaction.oncomplete = () => resolve();
      transaction.onerror = () => reject(transaction.error);
    });
  }

  // Get products (works offline)
  async getProducts(category?: string): Promise<any[]> {
    return new Promise((resolve, reject) => {
      const transaction = this.db!.transaction(['products'], 'readonly');
      const store = transaction.objectStore('products');

      let request: IDBRequest;

      if (category) {
        const index = store.index('category');
        request = index.getAll(category);
      } else {
        request = store.getAll();
      }

      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error);
    });
  }

  // Add to cart (works offline)
  async addToCart(item: any): Promise<void> {
    return new Promise((resolve, reject) => {
      const transaction = this.db!.transaction(['cart'], 'readwrite');
      const store = transaction.objectStore('cart');
      const request = store.put(item);

      request.onsuccess = () => resolve();
      request.onerror = () => reject(request.error);
    });
  }

  // Queue action for sync when online
  async queueAction(action: {
    id: string;
    type: 'order' | 'review' | 'wishlist';
    data: any;
    timestamp: number;
  }): Promise<void> {
    return new Promise((resolve, reject) => {
      const transaction = this.db!.transaction(['pendingActions'], 'readwrite');
      const store = transaction.objectStore('pendingActions');
      const request = store.put(action);

      request.onsuccess = () => resolve();
      request.onerror = () => reject(request.error);
    });
  }

  // Get pending actions
  async getPendingActions(): Promise<any[]> {
    return new Promise((resolve, reject) => {
      const transaction = this.db!.transaction(['pendingActions'], 'readonly');
      const store = transaction.objectStore('pendingActions');
      const request = store.getAll();

      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error);
    });
  }
}

export const offlineDB = new OfflineDB();
```

#### **4.2 Offline UI & Sync**

```typescript
// offline-sync.ts

class OfflineSync {
  private isOnline = navigator.onLine;

  constructor() {
    window.addEventListener('online', () => this.onOnline());
    window.addEventListener('offline', () => this.onOffline());
  }

  private onOnline() {
    console.log('✅ Back online, syncing...');
    this.isOnline = true;
    this.syncPendingActions();
  }

  private onOffline() {
    console.log('❌ No connection, queuing actions...');
    this.isOnline = false;
  }

  async addOrder(order: any) {
    if (this.isOnline) {
      // Online: Send immediately
      try {
        const response = await fetch('/api/orders', {
          method: 'POST',
          body: JSON.stringify(order),
        });
        return response.json();
      } catch (error) {
        // Network error, queue for later
        console.warn('Failed to send, queuing...');
        await this.queueOrder(order);
        throw error;
      }
    } else {
      // Offline: Queue for sync
      console.log('Offline, queuing order...');
      await this.queueOrder(order);
    }
  }

  private async queueOrder(order: any) {
    await offlineDB.queueAction({
      id: Math.random().toString(36),
      type: 'order',
      data: order,
      timestamp: Date.now(),
    });

    // Notify user
    showNotification('Order saved locally, will sync when online', 'info');
  }

  async syncPendingActions() {
    const actions = await offlineDB.getPendingActions();

    for (const action of actions) {
      try {
        if (action.type === 'order') {
          const response = await fetch('/api/orders', {
            method: 'POST',
            body: JSON.stringify(action.data),
          });

          if (response.ok) {
            // Delete from pending
            await offlineDB.deleteAction(action.id);
            showNotification('Order synced!', 'success');
          }
        }
      } catch (error) {
        console.error('Sync failed:', error);
      }
    }
  }
}

// Background Sync API (more reliable)
// Syncs even if app is closed
if ('sync' in ServiceWorkerRegistration.prototype) {
  async function registerBackgroundSync() {
    const registration = await navigator.serviceWorker.ready;
    try {
      await registration.sync.register('sync-pending-orders');
      console.log('Background sync registered');
    } catch (error) {
      console.error('Background sync failed:', error);
    }
  }
}

// In Service Worker
self.addEventListener('sync', (event: any) => {
  if (event.tag === 'sync-pending-orders') {
    event.waitUntil(syncPendingActions());
  }
});
```

---

### **5️⃣ Web App Manifest**

#### **5.1 Complete manifest.json**

```json
{
  "name": "My E-Commerce App",
  "short_name": "Shop",
  "description": "Mobile shopping experience optimized for offline",
  "start_url": "/?utm_source=pwa",
  "scope": "/",
  "display": "standalone",
  "orientation": "portrait-primary",
  "theme_color": "#1976d2",
  "background_color": "#ffffff",

  "icons": [
    {
      "src": "/icons/icon-192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "any"
    },
    {
      "src": "/icons/icon-512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "any"
    },
    {
      "src": "/icons/icon-maskable-192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "maskable"
    }
  ],

  "screenshots": [
    {
      "src": "/screenshots/narrow.png",
      "sizes": "540x720",
      "type": "image/png",
      "form_factor": "narrow"
    },
    {
      "src": "/screenshots/wide.png",
      "sizes": "1280x720",
      "type": "image/png",
      "form_factor": "wide"
    }
  ],

  "shortcuts": [
    {
      "name": "View Cart",
      "short_name": "Cart",
      "description": "View your shopping cart",
      "url": "/cart?utm_source=pwa_shortcut",
      "icons": [{ "src": "/icons/cart.png", "sizes": "192x192" }]
    },
    {
      "name": "Browse Products",
      "short_name": "Browse",
      "description": "Browse our product catalog",
      "url": "/products?utm_source=pwa_shortcut",
      "icons": [{ "src": "/icons/products.png", "sizes": "192x192" }]
    }
  ],

  "categories": ["shopping", "productivity"],
  "screenshots": [...],
  "share_target": {
    "action": "/share",
    "method": "POST",
    "enctype": "multipart/form-data",
    "params": {
      "title": "title",
      "text": "text",
      "url": "url",
      "files": [{ "name": "image", "accept": ["image/*"] }]
    }
  }
}
```

#### **5.2 Link in HTML**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Web App Manifest -->
    <link rel="manifest" href="/manifest.json" />

    <!-- Theme Colors -->
    <meta name="theme-color" content="#1976d2" />
    <meta name="msapplication-TileColor" content="#1976d2" />

    <!-- Viewport for responsive -->
    <meta name="viewport" content="width=device-width, initial-scale=1" />

    <!-- iOS specific -->
    <meta name="apple-mobile-web-app-capable" content="yes" />
    <meta
      name="apple-mobile-web-app-status-bar-style"
      content="black-translucent"
    />
    <meta name="apple-mobile-web-app-title" content="Shop" />
    <link rel="apple-touch-icon" href="/icons/icon-192.png" />
  </head>
  <body>
    <div id="root"></div>

    <script>
      // Register Service Worker
      if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/sw.js');
      }
    </script>
  </body>
</html>
```

---

### **6️⃣ Push Notifications**

#### **6.1 Request Permission & Subscribe**

```typescript
// push-notifications.ts

class PushNotifications {
  async requestPermission(): Promise<boolean> {
    if (!('Notification' in window)) {
      console.log('Notifications not supported');
      return false;
    }

    if (Notification.permission === 'granted') {
      return true;
    }

    if (Notification.permission !== 'denied') {
      const permission = await Notification.requestPermission();
      return permission === 'granted';
    }

    return false;
  }

  async subscribe(): Promise<void> {
    const registration = await navigator.serviceWorker.ready;

    try {
      const subscription = await registration.pushManager.subscribe({
        userVisibleOnly: true,
        applicationServerKey: this.urlBase64ToUint8Array(
          process.env.REACT_APP_VAPID_PUBLIC_KEY || ''
        ),
      });

      // Send subscription to server
      await fetch('/api/notifications/subscribe', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(subscription),
      });

      console.log('✅ Push subscribed:', subscription);
    } catch (error) {
      console.error('Push subscription failed:', error);
    }
  }

  private urlBase64ToUint8Array(base64String: string): Uint8Array {
    const padding = '='.repeat((4 - (base64String.length % 4)) % 4);
    const base64 = (base64String + padding)
      .replace(/\-/g, '+')
      .replace(/_/g, '/');

    const rawData = window.atob(base64);
    const outputArray = new Uint8Array(rawData.length);

    for (let i = 0; i < rawData.length; ++i) {
      outputArray[i] = rawData.charCodeAt(i);
    }

    return outputArray;
  }

  async unsubscribe(): Promise<void> {
    const registration = await navigator.serviceWorker.ready;
    const subscription = await registration.pushManager.getSubscription();

    if (subscription) {
      await subscription.unsubscribe();
      console.log('✅ Push unsubscribed');
    }
  }
}

// Usage
const notifications = new PushNotifications();

// Request permission when user interacts
button.addEventListener('click', async () => {
  const granted = await notifications.requestPermission();
  if (granted) {
    await notifications.subscribe();
  }
});
```

#### **6.2 Handle Push in Service Worker**

```typescript
// sw-push.ts - Service Worker

self.addEventListener('push', (event: PushEvent) => {
  const data = event.data?.json() || {
    title: 'Default notification',
    body: 'New update available',
  };

  const options: NotificationOptions = {
    body: data.body,
    icon: '/icons/icon-192.png',
    badge: '/icons/badge-72.png',
    tag: data.tag || 'notification', // Group notifications
    requireInteraction: data.requireInteraction || false,
    data: data.data || {},
    actions: [
      {
        action: 'open',
        title: 'Open',
      },
      {
        action: 'close',
        title: 'Close',
      },
    ],
  };

  event.waitUntil(self.registration.showNotification(data.title, options));
});

// Handle notification click
self.addEventListener('notificationclick', (event: NotificationEvent) => {
  event.notification.close();

  const urlToOpen = event.notification.data.url || '/';

  event.waitUntil(
    clients.matchAll({ type: 'window' }).then((clientList) => {
      // Check if app already open
      for (const client of clientList) {
        if (client.url === urlToOpen && 'focus' in client) {
          return client.focus();
        }
      }

      // Open new window/tab
      if (clients.openWindow) {
        return clients.openWindow(urlToOpen);
      }
    })
  );
});
```

#### **6.3 Send Push from Backend (Node.js)**

```typescript
// backend/push-notifications.ts

import webpush from 'web-push';

const vapidPublicKey = process.env.VAPID_PUBLIC_KEY!;
const vapidPrivateKey = process.env.VAPID_PRIVATE_KEY!;

webpush.setVapidDetails(
  'mailto:admin@example.com',
  vapidPublicKey,
  vapidPrivateKey
);

export async function sendPushNotification(
  subscription: PushSubscription,
  payload: {
    title: string;
    body: string;
    data?: any;
  }
) {
  try {
    await webpush.sendNotification(subscription, JSON.stringify(payload));
    console.log('✅ Push sent');
  } catch (error: any) {
    if (error.statusCode === 410) {
      // Subscription expired, delete from DB
      console.log('Removing expired subscription');
    } else {
      console.error('Push failed:', error);
    }
  }
}

// Example: Send order update
router.post('/api/orders/:id/notify', async (req, res) => {
  const { subscriptions } = req.body;

  const promises = subscriptions.map((sub: any) =>
    sendPushNotification(sub, {
      title: 'Order Update',
      body: 'Your order has been shipped!',
      data: {
        url: `/orders/${req.params.id}`,
      },
    })
  );

  await Promise.all(promises);
  res.json({ success: true });
});
```

---

### **7️⃣ App Shell Architecture**

#### **7.1 App Shell Pattern**

```
App Shell = Minimal HTML/CSS/JS needed to display app structure

┌─────────────────────────────────────────┐
│         App Shell (cached)              │
│  ┌────────────────────────────────────┐ │
│  │  Header (logo, nav, menu)          │ │
│  ├────────────────────────────────────┤ │
│  │  Sidebar (loading skeleton)        │ │
│  ├────────────────────────────────────┤ │
│  │  Content Area (loading skeleton)   │ │
│  │  (filled with data from API)       │ │
│  ├────────────────────────────────────┤ │
│  │  Footer                            │ │
│  └────────────────────────────────────┘ │
└─────────────────────────────────────────┘

Benefits:
├─ Instant app loading (< 1s)
├─ Works offline (shell cached)
└─ Content loads after (from API/cache)

Time to Interactive:
├─ Without App Shell: 3s (wait for HTML + JS + data)
└─ With App Shell: 0.5s (show shell) + 1s (load data) = perceived fast
```

#### **7.2 App Shell Implementation**

```typescript
// App Shell HTML (static, cached)
const appShellHTML = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="/styles.css">
</head>
<body>
  <header>
    <h1>ShopApp</h1>
    <nav>...</nav>
  </header>

  <aside class="sidebar">
    <div class="skeleton"></div>
  </aside>

  <main class="content">
    <div class="skeleton"></div>
    <div class="skeleton"></div>
  </main>

  <script src="/app.js"></script>
</body>
</html>
`;

// Service Worker: Serve app shell for unknown routes
self.addEventListener('fetch', (event: FetchEvent) => {
  const { request } = event;

  // API requests
  if (request.url.includes('/api/')) {
    event.respondWith(networkFirstStrategy(request));
    return;
  }

  // Navigation requests (HTML pages)
  if (request.mode === 'navigate') {
    event.respondWith(
      fetch(request)
        .then((response) => {
          // Cache the page
          caches.open('pages-cache').then((cache) => {
            cache.put(request, response.clone());
          });
          return response;
        })
        .catch(() => {
          // Offline: Return cached page or app shell
          return caches.match(request).then((cachedResponse) => {
            return cachedResponse || caches.match('/index.html');
          });
        })
    );
    return;
  }

  // Assets
  event.respondWith(cacheFirstStrategy(request));
});
```

#### **7.3 Loading Skeleton UI**

```typescript
// skeleton.tsx - Show during app shell loading

export function ProductSkeleton() {
  return (
    <div className="product-card skeleton">
      <div className="skeleton-image"></div>
      <div className="skeleton-title"></div>
      <div className="skeleton-price"></div>
    </div>
  );
}

// CSS animations
const skeletonStyles = `
.skeleton {
  background: linear-gradient(
    90deg,
    #f0f0f0 25%,
    #e0e0e0 50%,
    #f0f0f0 75%
  );
  background-size: 200% 100%;
  animation: loading 1.5s infinite;
}

@keyframes loading {
  0% {
    background-position: 200% 0;
  }
  100% {
    background-position: -200% 0;
  }
}

.skeleton-image {
  width: 100%;
  height: 200px;
  border-radius: 8px;
}

.skeleton-title {
  width: 80%;
  height: 16px;
  margin-top: 8px;
  border-radius: 4px;
}

.skeleton-price {
  width: 60%;
  height: 20px;
  margin-top: 8px;
  border-radius: 4px;
}
`;
```

---

### **8️⃣ Production PWA Example: E-Commerce**

```typescript
// Complete e-commerce PWA

// 1. Register SW + Request Notification Permission
function initPWA() {
  // Register service worker
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js');
  }

  // Initialize offline DB
  offlineDB.init();

  // Request notification permission
  const notificationButton = document.getElementById('enable-notifications');
  notificationButton?.addEventListener('click', async () => {
    const notifications = new PushNotifications();
    const granted = await notifications.requestPermission();
    if (granted) {
      await notifications.subscribe();
      notificationButton.textContent = 'Notifications enabled';
    }
  });
}

// 2. Product Listing (Works Offline)
async function loadProducts() {
  try {
    // Try network first
    const response = await fetch('/api/products');
    const products = await response.json();

    // Cache for offline
    await offlineDB.saveProducts(products);

    renderProducts(products);
  } catch (error) {
    // Network failed, use cached
    const products = await offlineDB.getProducts();
    renderProducts(products);
    showNotification('Showing cached products', 'info');
  }
}

// 3. Add to Cart (Works Offline)
async function addToCart(product: any) {
  const cartItem = {
    id: Math.random().toString(),
    ...product,
    addedAt: Date.now(),
  };

  await offlineDB.addToCart(cartItem);

  if (navigator.onLine) {
    // Sync immediately if online
    await syncCart();
  }

  showNotification('Added to cart', 'success');
}

// 4. Checkout (Queue if Offline)
async function checkout(order: any) {
  if (navigator.onLine) {
    try {
      const response = await fetch('/api/orders', {
        method: 'POST',
        body: JSON.stringify(order),
      });
      const result = await response.json();
      showNotification('Order placed!', 'success');
      return result;
    } catch (error) {
      // Fallback: queue for sync
      await offlineDB.queueAction({
        id: Math.random().toString(),
        type: 'order',
        data: order,
        timestamp: Date.now(),
      });
    }
  } else {
    // Queue for sync when online
    await offlineDB.queueAction({
      id: Math.random().toString(),
      type: 'order',
      data: order,
      timestamp: Date.now(),
    });

    showNotification('Order saved, will sync when online', 'info');
  }
}

// Listen for online event to sync
window.addEventListener('online', async () => {
  showNotification('Back online, syncing...', 'info');
  await syncCart();
  await offlineDB.syncPendingActions?.();
});

initPWA();
```

---

## **💡 SENIOR TIPS & BEST PRACTICES (Mẹo & Thực Hành Tốt Nhất)**

```
// ============================================
// ✅ PWA BEST PRACTICES CHECKLIST
// ============================================
✅ PWA BEST PRACTICES CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
☑️  HTTPS everywhere (required for SW)
   💡 HTTPS: Bắt buộc cho Service Worker
   💡 Security: Bảo vệ data khỏi MITM attacks
   💡 Localhost: OK cho development

☑️  manifest.json with icons, colors, display mode
   💡 manifest.json: File mô tả app
   💡 icons: Icons cho home screen
   💡 colors: Theme colors
   💡 display mode: standalone, fullscreen, etc.

☑️  Service Worker with proper caching strategy
   💡 Service Worker: Background script
   💡 Caching strategy: Network First, Cache First, SWR
   💡 Khác nhau cho khác loại resources

☑️  Offline page/mode (don't let users see blank page)
   💡 Offline page: Trang hiển thị khi offline
   💡 Không để user thấy blank page
   💡 UX: Thông báo rõ ràng

☑️  IndexedDB for offline data (not localStorage)
   💡 IndexedDB: Database trong browser
   💡 Tốt hơn localStorage: Lưu được objects, large data
   💡 Async: Không block main thread

☑️  Background Sync for queued actions
   💡 Background Sync: Tự động sync khi online
   💡 Queue actions: Lưu actions khi offline
   💡 Sync: Tự động sync khi có mạng

☑️  Push notifications (engage offline users)
   💡 Push notifications: Thông báo đẩy
   💡 Engage: Tăng engagement
   💡 Offline users: User không online

☑️  App Shell pattern (instant loading)
   💡 App Shell: Cấu trúc app cơ bản
   💡 Instant loading: Load ngay lập tức
   💡 < 1s: Load trong vòng 1 giây

☑️  Loading skeletons (better UX than spinners)
   💡 Loading skeletons: Placeholder khi load
   💡 Better UX: Tốt hơn spinners
   💡 Perceived performance: Cảm giác nhanh hơn

☑️  Update notification (let user know about new version)
   💡 Update notification: Thông báo version mới
   💡 User biết: Có version mới
   💡 Reload: User có thể reload để update

☑️  Test on slow networks (Chrome DevTools 3G)
   💡 Test: Kiểm tra trên mạng chậm
   💡 Chrome DevTools: Simulate 3G
   💡 Real-world: Mạng thật có thể chậm

☑️  Lighthouse PWA audit (90+ score)
   💡 Lighthouse: Tool audit PWA
   💡 90+ score: Điểm trên 90
   💡 Excellent: Xuất sắc

☑️  Installability check (2-minute rule)
   💡 Installability: Khả năng cài đặt
   💡 2-minute rule: User có thể cài trong 2 phút
   💡 Easy: Dễ dàng cài đặt

// ============================================
// 📊 PERFORMANCE TARGETS
// ============================================
📊 PERFORMANCE TARGETS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
└─ First Contentful Paint (FCP): < 2.5s (3G)
   💡 FCP: Thời gian hiển thị content đầu tiên
   💡 < 2.5s: Dưới 2.5 giây
   💡 3G: Trên mạng 3G
   ├─ Online: 2-3s
   │  💡 Online: Khi có mạng
   │  💡 2-3s: Chấp nhận được
   └─ Offline (cached): < 500ms
      💡 Offline: Khi không có mạng
      💡 Cached: Có cache
      💡 < 500ms: Rất nhanh

└─ Lighthouse PWA Score: ≥ 90
   💡 Lighthouse: Tool audit
   💡 PWA Score: Điểm PWA
   💡 ≥ 90: Trên 90 điểm
   ├─ Installable ✅
   │  💡 Có thể cài đặt
   ├─ Progressive ✅
   │  💡 Progressive enhancement
   ├─ Fast on 3G ✅
   │  💡 Nhanh trên 3G
   └─ Offline capable ✅
      💡 Có thể hoạt động offline

└─ Installation Rate: Target 2-3% of visitors
   💡 Installation Rate: Tỷ lệ cài đặt
   💡 2-3%: Mục tiêu 2-3% visitors
   ├─ Show install prompt after user engaged
   │  💡 Show prompt: Hiển thị prompt
   │  💡 After engaged: Sau khi user tương tác
   └─ Include benefits (offline, notifications, home screen)
      💡 Benefits: Lợi ích
      💡 Offline: Hoạt động offline
      💡 Notifications: Thông báo
      💡 Home screen: Cài trên home screen
```

---

## **⚠️ COMMON MISTAKES**

```js
// ❌ No HTTPS
// Service workers REQUIRE HTTPS (except localhost)
// User won't be able to install as PWA

// ✅ Always use HTTPS in production

// ❌ Caching everything
self.addEventListener('fetch', (event) => {
  event.respondWith(cacheFirstStrategy(request)); // ❌ Cache everything
});

// ✅ Different strategies for different resources
if (isApiRequest) {
  event.respondWith(networkFirstStrategy(request)); // APIs need fresh data
} else {
  event.respondWith(cacheFirstStrategy(request)); // Assets are stable
}

// ❌ Blocking install on fetch error
self.addEventListener('install', (event) => {
  event.waitUntil(
    cache.addAll(['/page1', '/page2', '/invalid-url']) // ❌ One failed = all fails
  );
});

// ✅ Handle failures gracefully
self.addEventListener('install', (event) => {
  event.waitUntil(
    cache.addAll(criticalAssets).then(() => {
      // Load critical only
      return cache.addAll(optionalAssets).catch(() => {}); // Optional can fail
    })
  );
});

// ❌ Not handling service worker updates
// User gets old version even after you deployed new version

// ✅ Notify user of updates
registration.addEventListener('updatefound', () => {
  const newWorker = registration.installing;
  newWorker?.addEventListener('statechange', () => {
    if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
      // New version available
      showUpdatePrompt('New version available!');
    }
  });
});
```

---

## **🎯 INTERVIEW ANSWER (Câu Trả Lời Phỏng Vấn)**

**💡 KHI ĐƯỢC HỎI VỀ PWA:**
// 💡 Luôn mention: Service Workers, Web App Manifest, Cache Strategies
// 💡 Thể hiện hiểu rõ offline-first architecture

"PWA combines web + native capabilities using Service Workers and Web App Manifest.

// ============================================
// 🏗️ CORE PILLARS (Trụ Cột Chính)
// ============================================
**Core pillars:**

1. **HTTPS + Manifest** - Installable on home screen
   💡 HTTPS: Bắt buộc cho Service Worker
   💡 Manifest: File mô tả app
   💡 Installable: Có thể cài trên home screen
   💡 Home screen: Màn hình chính

2. **Service Worker** - Offline capability
   💡 Service Worker: Background script
   💡 Offline capability: Khả năng hoạt động offline
   💡 Cache: Cache resources cho offline
   💡 Intercept: Chặn network requests

3. **Push Notifications** - Real-time engagement
   💡 Push Notifications: Thông báo đẩy
   💡 Real-time: Real-time updates
   💡 Engagement: Tăng engagement
   💡 Web Push API: API cho push notifications

// ============================================
// 💼 REAL-WORLD EXAMPLE (Ví Dụ Thực Tế)
// ============================================
**Real-world example:** Built e-commerce PWA where users can:

- Browse products offline (cached)
  💡 Browse: Duyệt sản phẩm
  💡 Offline: Không cần mạng
  💡 Cached: Dữ liệu đã được cache
  💡 Service Worker: Cache products khi online

- Add to cart offline (IndexedDB)
  💡 Add to cart: Thêm vào giỏ hàng
  💡 Offline: Không cần mạng
  💡 IndexedDB: Lưu vào IndexedDB
  💡 Sync: Đồng bộ khi online

- Checkout when online (queue actions if offline)
  💡 Checkout: Thanh toán
  💡 When online: Khi có mạng
  💡 Queue actions: Lưu actions nếu offline
  💡 Background Sync: Tự động sync khi online

- Get push notifications for order updates
  💡 Push notifications: Thông báo đẩy
  💡 Order updates: Cập nhật đơn hàng
  💡 Real-time: Real-time updates
  💡 Engagement: Tăng engagement

// ============================================
// 📦 CACHE STRATEGY (Chiến Lược Cache)
// ============================================
**Cache strategy:**

- **Network First** for APIs (fresh data priority)
  💡 Network First: Network trước
  💡 APIs: API calls
  💡 Fresh data: Data mới nhất
  💡 Priority: Ưu tiên data mới

- **Cache First** for JS/CSS/images (speed priority)
  💡 Cache First: Cache trước
  💡 JS/CSS/images: Static assets
  💡 Speed: Tốc độ
  💡 Priority: Ưu tiên tốc độ

- **Stale While Revalidate** for semi-static content
  💡 Stale While Revalidate: Dùng cache cũ, update nền
  💡 Semi-static: Nửa tĩnh
  💡 Content: Nội dung
  💡 Best of both: Nhanh + data mới

// ============================================
// 📊 RESULTS (Kết Quả)
// ============================================
**Result:**

- 45% increase in mobile engagement
  💡 45% increase: Tăng 45%
  💡 Mobile engagement: Tương tác mobile
  💡 PWA: Tăng engagement đáng kể

- 70% users return with offline support
  💡 70% users: 70% người dùng
  💡 Return: Quay lại
  💡 Offline support: Hỗ trợ offline
  💡 Retention: Tăng retention

- Can install on home screen
  💡 Install: Cài đặt
  💡 Home screen: Màn hình chính
  💡 Native-like: Giống native app
  💡 UX: Trải nghiệm tốt hơn

- Push notifications drive 2-3x engagement
  💡 Push notifications: Thông báo đẩy
  💡 2-3x engagement: Tăng 2-3 lần engagement
  💡 Real-time: Real-time updates
  💡 Retention: Tăng retention

// ============================================
// 🔑 KEY LEARNINGS (Bài Học Quan Trọng)
// ============================================
**Key learnings:**

- Different resources need different strategies
  💡 Different resources: Các resources khác nhau
  💡 Different strategies: Chiến lược khác nhau
  💡 APIs: Network First
  💡 Assets: Cache First
  💡 Content: Stale While Revalidate

- IndexedDB > localStorage for offline
  💡 IndexedDB: Database trong browser
  💡 localStorage: Local storage
  💡 >: Tốt hơn
  💡 Offline: Cho offline data
  💡 Lý do: Lưu được objects, large data, async

- Background Sync for reliable sync (even when app closed)
  💡 Background Sync: Đồng bộ nền
  💡 Reliable: Đáng tin cậy
  💡 Even when app closed: Ngay cả khi app đóng
  💡 Auto: Tự động sync khi có mạng

- Monitor cache size (storage limits)
  💡 Monitor: Theo dõi
  💡 Cache size: Kích thước cache
  💡 Storage limits: Giới hạn storage
  💡 Quota: Kiểm tra quota
  💡 Cleanup: Dọn dẹp cache cũ

- Test on slow networks (3G simulation)
  💡 Test: Kiểm tra
  💡 Slow networks: Mạng chậm
  💡 3G simulation: Mô phỏng 3G
  💡 Real-world: Mạng thật có thể chậm
  💡 Performance: Đảm bảo performance tốt

This demonstrates **practical PWA architecture** with real business metrics ✅
// 💡 Interviewer sẽ đánh giá cao approach này
// 💡 Thể hiện bạn hiểu rõ PWA architecture
// 💡 Có kinh nghiệm thực tế với PWA
// 💡 Biết cách optimize và measure success
```
