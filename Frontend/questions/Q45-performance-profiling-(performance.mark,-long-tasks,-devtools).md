# 📊 Q45: Performance Profiling (performance.mark, Long Tasks, DevTools)

<details>
<summary><span style="font-size:1.25em;font-weight:bold;">📊 Q45: Performance Profiling (performance.mark, Long Tasks, DevTools)</span></summary>


**❓ Câu Hỏi:**
Làm thế nào để profile và debug performance issues trong web app? Phân tích các tools và techniques hiệu quả nhất.



#### **📊 Performance Profiling - Tổng Quan**

Performance profiling là quá trình **đo lường, phân tích và tối ưu** hiệu năng ứng dụng. Nguyên tắc vàng:

> **"Measure first, optimize later. Never guess, always measure!"**
> (Đo trước, tối ưu sau. Không bao giờ đoán, luôn đo!)

**🎯 Performance Profiling Workflow:**

```
1. MEASURE (Đo đạc)
   ↓
2. ANALYZE (Phân tích bottlenecks)
   ↓
3. OPTIMIZE (Tối ưu)
   ↓
4. MEASURE AGAIN (Đo lại để verify)
   ↓
5. REPEAT (Lặp lại cho đến khi đạt target)
```

---

#### **1️⃣ Performance API - User Timing API**

**🔹 performance.mark() & performance.measure()**

API chuẩn của browser để đo timing các operations.

```typescript
// =====================================
// PERFORMANCE.MARK & MEASURE
// =====================================

// 🔹 CƠ BẢN - Đo một operation đơn giản
function measureOperation() {
  // Mark bắt đầu
  performance.mark('operation-start');
  
  // Code cần đo
  expensiveCalculation();
  
  // Mark kết thúc
  performance.mark('operation-end');
  
  // Measure khoảng thời gian giữa 2 marks
  performance.measure('operation-duration', 'operation-start', 'operation-end');
  
  // Lấy kết quả
  const measure = performance.getEntriesByName('operation-duration')[0];
  console.log(`Operation took: ${measure.duration.toFixed(2)}ms`);
}

// 🔹 THỰC TẾ - Đo API calls trong React app
async function fetchUserProfile(userId: string) {
  const markName = `fetch-user-${userId}`;
  
  performance.mark(`${markName}-start`);
  
  try {
    const response = await fetch(`/api/users/${userId}`);
    const data = await response.json();
    
    performance.mark(`${markName}-end`);
    performance.measure(markName, `${markName}-start`, `${markName}-end`);
    
    // Log performance
    const measure = performance.getEntriesByName(markName)[0];
    console.log(`✅ Fetched user ${userId} in ${measure.duration.toFixed(2)}ms`);
    
    return data;
  } catch (error) {
    performance.mark(`${markName}-error`);
    console.error(`❌ Failed to fetch user ${userId}`);
    throw error;
  }
}

// 🔹 COMPONENT RENDER TIME - React
function ProfileComponent({ userId }: { userId: string }) {
  useEffect(() => {
    performance.mark('profile-render-start');
    
    return () => {
      performance.mark('profile-render-end');
      performance.measure('profile-render', 'profile-render-start', 'profile-render-end');
      
      const measure = performance.getEntriesByName('profile-render')[0];
      console.log(`Profile rendered in ${measure.duration.toFixed(2)}ms`);
      
      // Cleanup marks để tránh memory leak
      performance.clearMarks('profile-render-start');
      performance.clearMarks('profile-render-end');
      performance.clearMeasures('profile-render');
    };
  }, [userId]);
  
  return <div>Profile for {userId}</div>;
}

// 🔹 NESTED OPERATIONS - Đo nhiều operations lồng nhau
async function loadDashboard() {
  performance.mark('dashboard-load-start');
  
  // Sub-operation 1: Fetch user
  performance.mark('fetch-user-start');
  const user = await fetchUser();
  performance.mark('fetch-user-end');
  performance.measure('fetch-user', 'fetch-user-start', 'fetch-user-end');
  
  // Sub-operation 2: Fetch orders
  performance.mark('fetch-orders-start');
  const orders = await fetchOrders(user.id);
  performance.mark('fetch-orders-end');
  performance.measure('fetch-orders', 'fetch-orders-start', 'fetch-orders-end');
  
  // Sub-operation 3: Render charts
  performance.mark('render-charts-start');
  renderCharts(orders);
  performance.mark('render-charts-end');
  performance.measure('render-charts', 'render-charts-start', 'render-charts-end');
  
  performance.mark('dashboard-load-end');
  performance.measure('dashboard-load', 'dashboard-load-start', 'dashboard-load-end');
  
  // Print all measurements
  const measures = performance.getEntriesByType('measure');
  console.table(
    measures.map(m => ({
      name: m.name,
      duration: `${m.duration.toFixed(2)}ms`,
    }))
  );
}

// 🔹 HELPER - Performance Monitor Utility
class PerformanceMonitor {
  private marks = new Map<string, number>();
  
  start(label: string) {
    this.marks.set(label, performance.now());
    performance.mark(`${label}-start`);
  }
  
  end(label: string) {
    const startTime = this.marks.get(label);
    if (!startTime) {
      console.warn(`No start mark for ${label}`);
      return;
    }
    
    const endTime = performance.now();
    const duration = endTime - startTime;
    
    performance.mark(`${label}-end`);
    performance.measure(label, `${label}-start`, `${label}-end`);
    
    console.log(`⏱️ ${label}: ${duration.toFixed(2)}ms`);
    
    // Cleanup
    this.marks.delete(label);
    performance.clearMarks(`${label}-start`);
    performance.clearMarks(`${label}-end`);
    
    return duration;
  }
  
  clearAll() {
    performance.clearMarks();
    performance.clearMeasures();
    this.marks.clear();
  }
}

// Usage
const monitor = new PerformanceMonitor();

monitor.start('data-processing');
processLargeDataset();
monitor.end('data-processing'); // ⏱️ data-processing: 234.56ms
```

**💡 Best Practices:**
- ✅ Dùng meaningful labels: `fetch-user-123` thay vì `op1`
- ✅ Cleanup marks/measures sau khi dùng (tránh memory leak)
- ✅ Group related operations: `dashboard-load`, `dashboard-load/fetch-user`, etc.
- ✅ Log vào analytics service (không chỉ console.log)

---

#### **2️⃣ Long Tasks API - PerformanceObserver**

**🔹 Detect Long Tasks (>50ms)**

Long tasks là các tasks chạy **quá 50ms**, block main thread và gây lag UI.

```typescript
// =====================================
// LONG TASKS DETECTION
// =====================================

// 🔹 CƠ BẢN - Detect all long tasks
const observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    console.warn('🐌 Long task detected:', {
      name: entry.name,
      duration: `${entry.duration.toFixed(2)}ms`,
      startTime: entry.startTime,
    });
  }
});

observer.observe({ type: 'longtask', buffered: true });

// 🔹 THỰC TẾ - Long Task Monitor với alerts
class LongTaskMonitor {
  private longTasks: PerformanceEntry[] = [];
  private observer: PerformanceObserver | null = null;
  
  start(options = { threshold: 50, alertThreshold: 100 }) {
    this.observer = new PerformanceObserver((list) => {
      for (const entry of list.getEntries()) {
        this.longTasks.push(entry);
        
        // Alert nếu task quá dài
        if (entry.duration > options.alertThreshold) {
          console.error(`🚨 CRITICAL: Task blocked UI for ${entry.duration.toFixed(2)}ms`);
          
          // Gửi alert đến monitoring service
          this.sendAlert({
            type: 'LONG_TASK',
            duration: entry.duration,
            timestamp: Date.now(),
            url: window.location.href,
          });
        }
      }
    });
    
    this.observer.observe({ type: 'longtask', buffered: true });
  }
  
  stop() {
    this.observer?.disconnect();
  }
  
  getReport() {
    return {
      totalLongTasks: this.longTasks.length,
      averageDuration: this.longTasks.reduce((sum, t) => sum + t.duration, 0) / this.longTasks.length,
      maxDuration: Math.max(...this.longTasks.map(t => t.duration)),
      tasks: this.longTasks.map(t => ({
        duration: t.duration,
        startTime: t.startTime,
      })),
    };
  }
  
  private sendAlert(data: any) {
    // Gửi đến Sentry, Datadog, etc.
    fetch('/api/monitoring/alert', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    });
  }
}

// Usage
const longTaskMonitor = new LongTaskMonitor();
longTaskMonitor.start({ threshold: 50, alertThreshold: 100 });

// Sau 5 phút, lấy report
setTimeout(() => {
  const report = longTaskMonitor.getReport();
  console.log('📊 Long Tasks Report:', report);
}, 5 * 60 * 1000);

// 🔹 OBSERVE MULTIPLE TYPES - Theo dõi nhiều loại performance entries
const multiObserver = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    switch (entry.entryType) {
      case 'longtask':
        console.warn('🐌 Long task:', entry.duration);
        break;
      case 'measure':
        console.log('⏱️ Measure:', entry.name, entry.duration);
        break;
      case 'navigation':
        console.log('🌐 Navigation timing:', entry);
        break;
      case 'resource':
        console.log('📦 Resource loaded:', entry.name, entry.duration);
        break;
    }
  }
});

multiObserver.observe({ entryTypes: ['longtask', 'measure', 'navigation', 'resource'] });
```

**💡 Tại Sao 50ms?**
- 60 FPS = 16.67ms per frame
- 50ms = 3 frames dropped → user thấy lag rõ ràng
- Google recommends: Keep tasks <50ms để UI mượt

---

#### **3️⃣ Chrome DevTools - Performance Tab**

**🔹 Cách Sử Dụng Performance Tab Hiệu Quả**

```
CHROME DEVTOOLS → PERFORMANCE TAB
┌─────────────────────────────────────────────────────────────┐
│  🎬 RECORD                                                   │
│  ├─ Start recording                                         │
│  ├─ Perform actions (load page, click, scroll)              │
│  └─ Stop recording                                          │
│                                                              │
│  📊 ANALYZE                                                  │
│  ├─ Main Thread (flame chart)                               │
│  │  └─ Identify long tasks (yellow/red bars)                │
│  ├─ Network (waterfall)                                     │
│  │  └─ Check slow requests                                  │
│  ├─ Frames (FPS)                                            │
│  │  └─ Find dropped frames (<60 FPS)                        │
│  └─ Bottom-Up / Call Tree / Event Log                       │
│     └─ Find heaviest functions                              │
└─────────────────────────────────────────────────────────────┘
```

**🔹 Performance Tab - Step by Step Guide:**

```typescript
// STEP 1: Prepare
// - Mở DevTools (F12 → Performance tab)
// - Enable "Screenshots" để thấy visual timeline
// - Enable "Memory" để track memory usage

// STEP 2: Record
// - Click Record button (●)
// - Perform user actions (load page, click buttons, scroll)
// - Click Stop (■) after 5-10 seconds

// STEP 3: Analyze Flame Chart
/*
┌──────────────────────────────────────────────────────────┐
│ Main Thread (Flame Chart)                                │
├──────────────────────────────────────────────────────────┤
│                                                           │
│  ████████████████ Task (120ms) ⚠️ Long task!             │
│    ████████ Layout (80ms)                                │
│      ████ JavaScript (60ms)                              │
│        ██ my-function (40ms) ← BOTTLENECK!               │
│                                                           │
└──────────────────────────────────────────────────────────┘

COLOR CODING:
- 🟨 Yellow: JavaScript execution
- 🟪 Purple: Rendering (Layout, Paint)
- 🟩 Green: Painting
- 🟦 Blue: Loading (HTML parsing)
- 🟥 Red: Long tasks (>50ms)
*/

// STEP 4: Identify Bottlenecks
// - Tìm red/yellow bars dài (long tasks)
// - Click vào bar → xem Call Tree ở bottom panel
// - Tìm function nào chiếm nhiều thời gian nhất

// STEP 5: Fix Issues
// Example: Tìm thấy my-function() chiếm 40ms
function myFunction() {
  // ❌ BEFORE: Blocking operation
  const result = heavyCalculation(); // 40ms
  return result;
}

// ✅ AFTER: Break into chunks với setTimeout
function myFunctionOptimized() {
  return new Promise(resolve => {
    const chunks = splitIntoChunks(data, 1000);
    let index = 0;
    
    function processChunk() {
      processData(chunks[index]);
      index++;
      
      if (index < chunks.length) {
        setTimeout(processChunk, 0); // Yield to browser
      } else {
        resolve();
      }
    }
    
    processChunk();
  });
}
```

**💡 Performance Tab - Key Metrics:**

```typescript
// Trong Performance recording, focus vào:

// 1. FPS (Frames Per Second)
// ✅ Target: 60 FPS (green bars)
// ⚠️ Warning: <60 FPS (yellow bars)
// ❌ Critical: <30 FPS (red bars)

// 2. CPU Usage
// ✅ Good: <50% average
// ⚠️ Warning: 50-80%
// ❌ Bad: >80% sustained

// 3. Main Thread Activity
// ✅ Good: Short tasks (<50ms)
// ❌ Bad: Long tasks (>50ms, red bars)

// 4. Memory
// ✅ Good: Stable (sawtooth pattern = GC working)
// ❌ Bad: Continuously increasing (memory leak)
```

---

#### **4️⃣ Lighthouse - Automated Audits**

**🔹 Lighthouse CI - Performance Audits**

Lighthouse là tool audit tự động của Google, tích hợp trong Chrome DevTools.

```typescript
// =====================================
// LIGHTHOUSE AUDITS
// =====================================

// 🔹 RUN LIGHTHOUSE
// Method 1: Chrome DevTools
// - F12 → Lighthouse tab
// - Select categories: Performance, Accessibility, Best Practices, SEO
// - Click "Analyze page load"

// Method 2: CLI
// npm install -g lighthouse
// lighthouse https://example.com --view

// Method 3: CI/CD (GitHub Actions)
/*
name: Lighthouse CI
on: [pull_request]
jobs:
  lighthouse:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: treosh/lighthouse-ci-action@v9
        with:
          urls: |
            https://example.com
          uploadArtifacts: true
*/

// 🔹 LIGHTHOUSE SCORES
interface LighthouseScores {
  performance: number;        // 0-100 (Target: >90)
  accessibility: number;      // 0-100 (Target: >90)
  bestPractices: number;      // 0-100 (Target: >90)
  seo: number;                // 0-100 (Target: >90)
  pwa: number;                // 0-100 (optional)
}

// 🔹 KEY METRICS - Web Vitals
interface WebVitals {
  // LOADING PERFORMANCE
  FCP: number;  // First Contentful Paint (<1.8s ✅)
  LCP: number;  // Largest Contentful Paint (<2.5s ✅)
  
  // INTERACTIVITY
  FID: number;  // First Input Delay (<100ms ✅)
  TBT: number;  // Total Blocking Time (<200ms ✅)
  TTI: number;  // Time to Interactive (<3.8s ✅)
  
  // VISUAL STABILITY
  CLS: number;  // Cumulative Layout Shift (<0.1 ✅)
  
  // SPEED INDEX
  SI: number;   // Speed Index (<3.4s ✅)
}

// 🔹 IMPROVE LIGHTHOUSE SCORE - Common Fixes
const lighthouseOptimizations = {
  // 1. IMAGES
  images: {
    problem: "Unoptimized images",
    solution: [
      "✅ Use WebP format",
      "✅ Compress images (TinyPNG, ImageOptim)",
      "✅ Lazy load below-the-fold images",
      "✅ Use responsive images (srcset)",
      "✅ Add width/height to prevent CLS",
    ],
    example: `
      <img 
        src="image.webp" 
        srcset="image-320w.webp 320w, image-640w.webp 640w" 
        sizes="(max-width: 600px) 320px, 640px"
        width="640" 
        height="360" 
        loading="lazy"
        alt="Description"
      />
    `,
  },
  
  // 2. JAVASCRIPT
  javascript: {
    problem: "Render-blocking JS, large bundles",
    solution: [
      "✅ Code splitting (React.lazy, dynamic import)",
      "✅ Tree shaking (remove unused code)",
      "✅ Minify & compress (Vite, webpack)",
      "✅ Defer non-critical JS",
      "✅ Remove unused libraries",
    ],
    example: `
      // Code splitting
      const Dashboard = React.lazy(() => import('./Dashboard'));
      
      // Dynamic import
      button.addEventListener('click', async () => {
        const module = await import('./heavy-module.js');
        module.run();
      });
    `,
  },
  
  // 3. CSS
  css: {
    problem: "Render-blocking CSS, unused CSS",
    solution: [
      "✅ Inline critical CSS",
      "✅ Defer non-critical CSS",
      "✅ Remove unused CSS (PurgeCSS)",
      "✅ Minify CSS",
    ],
    example: `
      <!-- Critical CSS inline -->
      <style>
        /* Above-the-fold styles */
        .header { ... }
      </style>
      
      <!-- Non-critical CSS deferred -->
      <link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
    `,
  },
  
  // 4. FONTS
  fonts: {
    problem: "Render-blocking fonts, FOIT/FOUT",
    solution: [
      "✅ Preload fonts",
      "✅ Use font-display: swap",
      "✅ Self-host fonts (avoid Google Fonts latency)",
      "✅ Subset fonts (remove unused glyphs)",
    ],
    example: `
      <!-- Preload critical fonts -->
      <link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>
      
      <!-- CSS -->
      @font-face {
        font-family: 'MyFont';
        src: url('font.woff2') format('woff2');
        font-display: swap; /* Show fallback immediately */
      }
    `,
  },
};

// 🔹 MEASURE WEB VITALS IN CODE
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals';

function sendToAnalytics(metric: any) {
  // Gửi đến Google Analytics, Datadog, etc.
  console.log(metric.name, metric.value);
  
  fetch('/api/analytics', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(metric),
  });
}

getCLS(sendToAnalytics);  // Cumulative Layout Shift
getFID(sendToAnalytics);  // First Input Delay
getFCP(sendToAnalytics);  // First Contentful Paint
getLCP(sendToAnalytics);  // Largest Contentful Paint
getTTFB(sendToAnalytics); // Time to First Byte
```

---

#### **5️⃣ Advanced Debugging Tools**

**🔹 React DevTools Profiler**

```typescript
// =====================================
// REACT DEVTOOLS PROFILER
// =====================================

// USAGE:
// 1. Install React DevTools extension
// 2. Open DevTools → Profiler tab
// 3. Click Record → interact with app → Stop
// 4. Analyze flame graph

// INTERPRET RESULTS:
/*
┌──────────────────────────────────────────────────────────┐
│ Profiler - Flame Graph                                   │
├──────────────────────────────────────────────────────────┤
│  App (120ms)                                             │
│    Dashboard (100ms) ⚠️ Slow component!                  │
│      UserList (80ms) ← BOTTLENECK                        │
│        UserItem (5ms) x 200 renders = 1000ms total!      │
└──────────────────────────────────────────────────────────┘
*/

// FIX: Memoize UserItem để avoid re-renders
const UserItem = React.memo(({ user }) => {
  return <div>{user.name}</div>;
});

// 🔹 PROFILER API - Programmatic profiling
import { Profiler } from 'react';

function onRenderCallback(
  id: string,
  phase: 'mount' | 'update',
  actualDuration: number,
  baseDuration: number,
  startTime: number,
  commitTime: number
) {
  console.log(`${id} ${phase} phase took ${actualDuration.toFixed(2)}ms`);
  
  // Send to analytics nếu render quá lâu
  if (actualDuration > 16) { // >1 frame (60 FPS)
    sendToAnalytics({
      component: id,
      phase,
      duration: actualDuration,
    });
  }
}

function App() {
  return (
    <Profiler id="Dashboard" onRender={onRenderCallback}>
      <Dashboard />
    </Profiler>
  );
}
```

**🔹 Chrome DevTools - Memory Profiler**

```typescript
// =====================================
// MEMORY PROFILING
// =====================================

// DETECT MEMORY LEAKS:
// 1. DevTools → Memory tab
// 2. Take Heap Snapshot
// 3. Interact with app (add/remove items)
// 4. Take another snapshot
// 5. Compare snapshots → find increasing objects

// EXAMPLE: Memory leak detection
class MemoryLeakDetector {
  private snapshots: number[] = [];
  
  takeSnapshot() {
    // @ts-ignore
    if (performance.memory) {
      // @ts-ignore
      this.snapshots.push(performance.memory.usedJSHeapSize);
    }
  }
  
  analyze() {
    if (this.snapshots.length < 2) return;
    
    const growth = this.snapshots.map((snapshot, i) => {
      if (i === 0) return 0;
      return snapshot - this.snapshots[i - 1];
    });
    
    const avgGrowth = growth.reduce((a, b) => a + b, 0) / growth.length;
    
    if (avgGrowth > 1_000_000) { // >1MB growth per snapshot
      console.warn(`🚨 Possible memory leak! Average growth: ${(avgGrowth / 1_000_000).toFixed(2)}MB`);
    }
    
    return {
      snapshots: this.snapshots.map(s => (s / 1_000_000).toFixed(2) + 'MB'),
      growth: growth.map(g => (g / 1_000_000).toFixed(2) + 'MB'),
      avgGrowth: (avgGrowth / 1_000_000).toFixed(2) + 'MB',
    };
  }
}

// Usage: Take snapshot mỗi 10 giây
const detector = new MemoryLeakDetector();
setInterval(() => {
  detector.takeSnapshot();
  console.log(detector.analyze());
}, 10000);
```

**🔹 Network Panel - Performance**

```typescript
// =====================================
// NETWORK PERFORMANCE ANALYSIS
// =====================================

// CHROME DEVTOOLS → NETWORK TAB
// - Enable "Disable cache"
// - Throttle: "Fast 3G" để test slow connections
// - Reload page (Cmd+R)

// KEY METRICS:
// 1. DOMContentLoaded (blue line) - HTML parsed
// 2. Load (red line) - All resources loaded
// 3. Waterfall - Visual timeline của requests

// ANALYZE:
/*
┌──────────────────────────────────────────────────────────┐
│ Resource             Size      Time    Waterfall          │
├──────────────────────────────────────────────────────────┤
│ index.html           5 KB      100ms   ████               │
│ app.js               200 KB    800ms   ████████████       │ ⚠️ Large JS
│ vendor.js            500 KB    2000ms  ████████████████   │ 🚨 HUGE!
│ image.png            2 MB      5000ms  ████████████████   │ 🚨 Unoptimized
└──────────────────────────────────────────────────────────┘
*/

// OPTIMIZATIONS:
const networkOptimizations = {
  largeJavaScript: [
    "✅ Code splitting",
    "✅ Tree shaking",
    "✅ Gzip compression",
    "✅ CDN delivery",
  ],
  
  largeImages: [
    "✅ WebP format",
    "✅ Lazy loading",
    "✅ Responsive images",
    "✅ CDN + image optimization service (Cloudinary, Imgix)",
  ],
  
  manyRequests: [
    "✅ Bundle files",
    "✅ HTTP/2 multiplexing",
    "✅ Inline critical resources",
    "✅ Remove unused libraries",
  ],
};
```

---

#### **📚 Tools Summary - Khi Nào Dùng Tool Gì?**

| Tool | Use Case | When to Use |
|------|----------|-------------|
| **performance.mark/measure** | Đo timing specific operations | Development, production monitoring |
| **PerformanceObserver** | Detect long tasks, monitor vitals | Production monitoring |
| **Performance Tab** | Deep dive bottlenecks | Development debugging |
| **Lighthouse** | Overall performance audit | CI/CD, before deployment |
| **React DevTools** | React component profiling | Development, optimize re-renders |
| **Memory Profiler** | Detect memory leaks | Development debugging |
| **Network Panel** | Analyze loading performance | Development, optimize resources |

---

#### **🔥 Best Practices**

**✅ DO:**
1. **Measure first, optimize later**: Don't guess bottlenecks
2. **Set performance budgets**: 
   - LCP <2.5s
   - FID <100ms
   - CLS <0.1
   - JS bundle <200KB
3. **Monitor in production**: Use RUM (Real User Monitoring)
4. **Automate audits**: Lighthouse CI in GitHub Actions
5. **Test on real devices**: Don't rely only on desktop Chrome
6. **Profile regularly**: Weekly performance reviews
7. **Track over time**: Monitor trends, not just snapshots

**❌ DON'T:**
1. **Premature optimization**: Measure before optimizing
2. **Ignore real-world conditions**: Test on 3G, slow devices
3. **Optimize in isolation**: Consider user experience holistically
4. **Forget cleanup**: Remove performance marks/observers
5. **Rely only on lab data**: Monitor real users (RUM)

---

#### **🎯 Common Mistakes & Corrections**

**❌ Mistake 1: Optimizing without measuring**
```typescript
// ❌ BAD - Guessing bottleneck
function processData(data: any[]) {
  // Developer thinks: "Maybe sorting is slow?"
  return data.sort(); // Optimizes sorting without proof
}
```

**✅ Correction:**
```typescript
// ✅ GOOD - Measure first
performance.mark('process-start');
const result = processData(data);
performance.mark('process-end');
performance.measure('process', 'process-start', 'process-end');

const measure = performance.getEntriesByName('process')[0];
console.log(`Process took: ${measure.duration}ms`);
// Result: 5ms → sorting is NOT the bottleneck!
```

---

**❌ Mistake 2: Ignoring long tasks**
```typescript
// ❌ BAD - Long blocking operation
function calculateAll() {
  for (let i = 0; i < 1000000; i++) {
    heavyCalculation(i); // Blocks UI for 2000ms!
  }
}
```

**✅ Correction:**
```typescript
// ✅ GOOD - Break into chunks
async function calculateAll() {
  const chunks = 100;
  const itemsPerChunk = 10000;
  
  for (let chunk = 0; chunk < chunks; chunk++) {
    for (let i = 0; i < itemsPerChunk; i++) {
      heavyCalculation(chunk * itemsPerChunk + i);
    }
    
    // Yield to browser every chunk
    await new Promise(resolve => setTimeout(resolve, 0));
  }
}
```

---

**❌ Mistake 3: Not testing on slow devices**
```typescript
// ❌ BAD - Only test on MacBook Pro M3
// Result: 60 FPS, loads in 1s ✅
// Reality on iPhone 8: 20 FPS, loads in 8s ❌
```

**✅ Correction:**
```typescript
// ✅ GOOD - Test on real devices & throttling
// 1. Chrome DevTools → Performance tab
// 2. CPU throttling: 4x slowdown
// 3. Network throttling: Fast 3G
// 4. Test on real iPhone 8 / Android mid-range
```

---

**🎯 Kết Luận:**

**Performance Profiling Checklist:**
- ✅ Use `performance.mark/measure` for custom timing
- ✅ Monitor long tasks with `PerformanceObserver`
- ✅ Deep dive with Chrome DevTools Performance Tab
- ✅ Automate audits with Lighthouse CI
- ✅ Profile React components with React DevTools
- ✅ Monitor memory with Memory Profiler
- ✅ Analyze network with Network Panel
- ✅ Track Web Vitals in production

**💡 Key Takeaway:**
> **"You can't improve what you don't measure. Always measure, analyze, optimize, then measure again!"**

---
</details>