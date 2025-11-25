# 👷 Q29: Web Workers, Service Worker & Background processesing & Share Worker

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"Web Workers chạy JavaScript parallel không block UI, Service Workers proxy network requests cho offline PWA, Shared Workers share giữa tabs."**

**🔑 3 Loại Workers:**

**1. Web Worker (Dedicated Worker):**
- Chạy **background thread** riêng, không access DOM
- Communication: **`postMessage()` + `onmessage`**
- Use case: Heavy computations (image processing, large data parsing, crypto)
- Transferable objects (ArrayBuffer) cho performance cao

**2. Service Worker:**
- **Proxy network requests**, cache resources cho offline
- Lifecycle: install → activate → fetch intercept
- **Cần HTTPS** (trừ localhost), scope-based (control URLs in folder)
- Use case: PWA (offline support), background sync, push notifications

**3. Shared Worker:**
- **Share state giữa multiple tabs/windows** cùng origin
- Communication qua MessagePort
- Use case: Shared WebSocket connection, centralized state management

**⚠️ Lỗi Thường Gặp:**
- Dùng DOM APIs trong Worker → **KHÔNG có** `window`, `document`
- Gửi large objects với `postMessage` → chậm (clone overhead), dùng **Transferable** thay vì
- Service Worker cache không version → stale data, dùng cache versioning
- Quên `self.skipWaiting()` → SW mới không activate ngay

**💡 Kiến Thức Senior:**
- **Transferable Objects**: `postMessage(data, [data.buffer])` → **zero-copy** transfer (nhanh hơn structured clone)
- **Service Worker strategies**:
  - **Cache First**: Offline-first (cache → network fallback)
  - **Network First**: Fresh data priority (network → cache fallback)
  - **Stale-While-Revalidate**: Instant response (cache) + background update
- **Workbox** (Google): Production-ready SW library với precaching, routing, strategies
- **SharedArrayBuffer** cho shared memory giữa workers (cần COOP/COEP headers)
- Module Workers: `new Worker('worker.js', {type: 'module'})` - support ES6 imports




**Trả lời:****

- Web Worker: chạy song song, không truy cập DOM
- Service Worker: proxy network, cache offline, cần HTTPS/origin chuẩn
- PWA: manifest + SW + HTTPS

**Code Example:**

```ts
// worker.ts
self.onmessage = (e) => {
  const n: number = e.data;
  postMessage(n * 2);
};

// main.ts
const worker = new Worker(new URL('./worker.ts', import.meta.url));
worker.postMessage(21);
worker.onmessage = (e) => console.log(e.data); // 42

// service worker (sw.js)
self.addEventListener('install', (e) => {
  e.waitUntil(caches.open('v1').then((c) => c.addAll(['/', '/style.css'])));
});
self.addEventListener('fetch', (e) => {
  e.respondWith(caches.match(e.request).then((r) => r || fetch(e.request)));
});
```

**Best Practices:**

- Worker: truyền dữ liệu nhỏ/gọn; dùng transferable (ArrayBuffer) cho hiệu năng
- SW: version cache, chiến lược network (Stale-While-Revalidate, CacheFirst,...)

**Mistakes:**

```ts
// ❌ Dùng DOM API bên trong Worker → không có sẵn
```

