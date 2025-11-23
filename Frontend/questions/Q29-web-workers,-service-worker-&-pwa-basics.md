# 👷 Q29: Web Workers, Service Worker & Background processesing & Share Worker




**Trả lời:**

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

